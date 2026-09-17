"""Offline Codex director helper: prepare prompts and validate plans/media.

Does not generate images, call Flow/TTS, automate a login, or publish to YouTube.
Those steps are performed by Codex using verified available tools.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import series_packaging as packaging


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding='utf-8'))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def normalized(text: str) -> str:
    return re.sub(r'[\s.,!?，。！？]', '', text).casefold()


def validate_contract(cfg: dict, catalog: dict) -> list[str]:
    errors = []
    try:
        f = cfg['frame']; ty = cfg['type']; tr = cfg['transitions']
        if cfg['executor'] != 'codex_direct': errors.append('Executor must be Codex direct.')
        if (f['width'], f['height'], f['fps']) != (1080,1920,30): errors.append('Expected 1080x1920/30fps.')
        if (f['intro_frames'],f['core_shots'],f['shot_frames'],f['outro_frames']) != (60,7,120,90): errors.append('Expected 2 + 7x4 + 3 seconds.')
        if f['total_frames'] != f['intro_frames'] + f['core_shots']*f['shot_frames'] + f['outro_frames'] or f['total_frames'] != 990: errors.append('Duration must be 990 frames, not 840.')
        if cfg['image_assets']['count'] != 9 or cfg['video_assets']['count'] != 7: errors.append('Nine still images, seven Flow clips required.')
        if cfg['image_assets']['baked_text']: errors.append('Image art must not contain baked titles.')
        if cfg['video_assets']['normal_playback_rate'] != 1 or cfg['video_assets']['global_speedup_allowed']: errors.append('No global video speedup.')
        if min(ty['ko_caption_px'],ty['en_caption_px']) < ty['caption_min_px'] or ty['caption_min_px'] < 64: errors.append('Captions below 64px are forbidden.')
        if ty['caption_max_lines'] != 2 or ty['caption_top'] + ty['caption_line_height_px']*2 > ty['caption_max_bottom']: errors.append('Invalid caption block geometry.')
        if ty['caption_x'] < 96 or ty['caption_x'] + ty['caption_width'] > 924 or ty['caption_max_bottom'] > 1472: errors.append('Caption leaves the reserved safe rectangle.')
        if ty['word_by_word'] or ty['karaoke'] or ty['caption_min_seconds'] < 1.8: errors.append('No word-flash captions.')
        if tr['black_blobs'] or tr['polygon_wipes'] or tr['full_frame_color_veils'] or tr['all_boundaries_must_be_hidden']: errors.append('Old obscuring transitions forbidden.')
        if tr['allowed'] != ['cut','dissolve'] or tr['max_dissolve_frames'] > 10: errors.append('Transition scope exceeded.')
        b = cfg['budget']
        if b['expected_unit_credits']*7 != b['expected_initial_credits'] or b['flow_cap'] != 50 or b['expected_initial_credits'] != 49: errors.append('Wrong Flow budget arithmetic.')
        if b['outputs_per_request'] != 1 or b['automatic_paid_retries'] != 0: errors.append('Only x1, no automatic paid retries.')
        if catalog['runtime_seconds'] != 33 or catalog['auto_advance']: errors.append('Catalog duration/auto-advance mismatch.')
        ids = [e['episode_id'] for e in catalog['episodes']]
        if len(ids) != 8 or len(set(ids)) != 8: errors.append('Expected eight unique episodes.')
        for e in catalog['episodes']:
            if not re.fullmatch(r'[0-9]{2}_[a-z0-9_]+',e['episode_id']): errors.append('Unsafe episode ID.')
            if len(e['core_transitions']) != 6 or any(v not in tr['allowed'] for v in e['core_transitions']): errors.append('Invalid core transitions.')
            if e['core_transitions'].count('dissolve') > tr['max_dissolves_in_core']: errors.append('Too many dissolves in core.')
            if (e['outro_mode'] == 'teaser') != bool(e['next_episode']): errors.append('Teaser must point to a real next episode.')
            if e['next_episode'] and e['next_episode'] not in ids: errors.append('Unknown next episode.')
            for loc in ('ko','en'):
                if not e['opener_title'][loc] or not e['outro_title'][loc]: errors.append('Missing localized card title.')
                if len(e['opener_title'][loc].splitlines()) > 2 or len(e['outro_title'][loc].splitlines()) > 2: errors.append('Card title exceeds two lines.')
    except (KeyError,TypeError,ValueError) as exc:
        errors.append(f'Malformed contract: {exc}')
    return errors


def validate_captions(cues: list[dict], locale: str, cfg: dict, final: bool=True) -> list[str]:
    errors=[]; previous_end=0.; ty=cfg['type']
    if locale not in ('ko','en'): return ['Unsupported locale.']
    if not cues: return ['No captions.']
    for i,c in enumerate(cues):
        try:
            start,end=float(c['start']),float(c['end']); lines=c['lines']; text=' '.join(lines)
            if not 2 <= start < end <= 30 or start < previous_end: errors.append(f'Cue {i}: overlap/outside core.')
            previous_end=end
            if len(lines)>2 or not lines or not all(isinstance(t,str) and t for t in lines): errors.append(f'Cue {i}: invalid lines.')
            if end-start < ty['caption_min_seconds']: errors.append(f'Cue {i}: visible duration too short.')
            # Conservative project reading metric: all non-whitespace characters.
            cps=len(re.sub(r'\s','',text))/(end-start)
            if cps>ty[f'{locale}_cps_max']: errors.append(f'Cue {i}: reading speed {cps:.1f} CPS too high.')
            if final and c.get('timing_source') not in ('audio_alignment_reviewed','manually_listened'): errors.append(f'Cue {i}: target timing is not measured/reviewed timing.')
            if c.get('font_px',ty[f'{locale}_caption_px'])<ty['caption_min_px']: errors.append(f'Cue {i}: font too small.')
        except (KeyError,TypeError,ValueError): errors.append(f'Cue {i}: malformed.')
    return errors


def prompt_blocks(brief: str) -> tuple[list[str],list[str]]:
    images=re.findall(r'(?:IMAGE:|\*\*이미지 프롬프트\*\*)\s*```text\s*\n(.*?)```',brief,re.S)
    flows=re.findall(r'(?:FLOW:|\*\*Flow 모션 프롬프트\*\*)\s*```text\s*\n(.*?)```',brief,re.S)
    if len(images)!=7 or len(flows)!=7: raise ValueError('Source brief must contain exactly seven image/motion blocks.')
    return images,flows


def prepare(root: Path, eid: str, out: Path) -> None:
    cfg=read_json(root/'production/director_v4.json'); cat=read_json(root/'production/catalog_v4.json')
    series=packaging.load(root,cat); cat=packaging.apply_catalog(cat,series)
    problems=validate_contract(cfg,cat)
    if problems: raise ValueError('\n'.join(problems))
    ep=next((e for e in cat['episodes'] if e['episode_id']==eid),None)
    if ep is None: raise ValueError('Unknown episode.')
    if out.exists(): raise FileExistsError('Output already exists; preserve it and choose a new run directory.')
    detail=read_json(root/ep['detail_override']) if ep.get('detail_override') else None
    if detail:
        images=[s['image'] for s in detail['shots']]; flows=[s['flow'] for s in detail['shots']]
        char=detail['character_reference']; texts={l:[s['narration_'+l] for s in detail['shots']] for l in ('ko','en')}
    else:
        brief=(root/ep['brief']).read_text(encoding='utf-8'); images,flows=prompt_blocks(brief)
        parent=(root/ep['parent']).read_text(encoding='utf-8') if ep['parent'] else brief
        blocks=re.findall(r'```text\s*\n(.*?)```',parent,re.S)
        char=blocks[0] if blocks else ''
        texts={l:(root/f'narration/{eid}.{l}.txt').read_text(encoding='utf-8').strip().splitlines() for l in ('ko','en')}
        if any(len(v)!=7 for v in texts.values()): raise ValueError('Narration requires seven semantic lines.')
    images=packaging.direct_images(series,eid,images)
    out.mkdir(parents=True)
    for folder in ('images','flow','image_prompts','flow_prompts','audio','captions','exports','evidence','youtube'):
        (out/folder).mkdir()
    for name,text in [('00_opening',ep['opener_prompt']),('08_outro',ep['outro_prompt'])]+[(f'{i:02d}',t) for i,t in enumerate(images,1)]:
        (out/'image_prompts'/f'{name}.txt').write_text(cat['image_prefix']+'\n\nAPPROVED CHARACTER REFERENCE:\n'+char+'\n\nSCENE:\n'+text+'\n',encoding='utf-8')
    for i,text in enumerate(flows,1):
        (out/'flow_prompts'/f'{i:02d}.txt').write_text(text+'\n\n'+cat['flow_suffix']+'\n',encoding='utf-8')
    for loc in ('ko','en'):
        (out/'audio'/f'narration_{loc}.txt').write_text('\n'.join(texts[loc])+'\n',encoding='utf-8')
        if detail:
            cues=[{'start':s['speech_target_seconds'][0],'end':s['speech_target_seconds'][1], 'lines':s['caption_lines_'+loc], 'timing_source':'TARGET_NOT_MEASURED', 'font_px':cfg['type'][loc+'_caption_px']} for s in detail['shots']]
            write_json(out/'captions'/f'{loc}.target.json',cues)
        else:
            write_json(out/'captions'/f'{loc}.target.json',{'status':'ALIGN_TO_REAL_AUDIO','texts':texts[loc]})
    segments=[{'id':'00_opening','kind':'still','from':0,'frames':60,'file':'images/00_opening.png'}]
    segments += [{'id':f'{i:02d}','kind':'video','from':60+(i-1)*120,'frames':120,'file':f'flow/{i:02d}.mp4','playback_rate':1.0} for i in range(1,8)]
    segments += [{'id':'08_outro','kind':'still','from':900,'frames':90,'file':'images/08_outro.png'}]
    opening=ep.get('opening_transition','dissolve')
    boundaries=[{'at':60,'type':opening,'frames':8 if opening=='dissolve' else 0}] + [{'at':180+i*120,'type':t,'frames':8 if t=='dissolve' else 0} for i,t in enumerate(ep['core_transitions'])] + [{'at':900,'type':'dissolve','frames':10}]
    write_json(out/'run_plan.json',{'version':4,'episode_id':eid,'runtime_seconds':33,'total_frames':990,'status':'PREPARED_NOT_GENERATED','segments':segments,'boundaries':boundaries,'cards':ep,'budgets':cfg['budget'],'next_episode_autorun':False,'packaging_revision':series['revision']})
    write_json(out/'asset_manifest.json',{'episode_id':eid,'status':'AWAITING_REAL_ASSETS','assets':[],'actual_flow_spent':None,'narration_provider':None,'master_sha256':None})
    write_json(out/'preflight.json',{'image_tool':None,'browser_tool':None,'flow_login_verified':False,'tts_tool':None,'music_license_verified':False,'actual_price_verified':False})
    packaging.write_handoff(out,series,eid,texts,ep,cfg)
    # Export duration-correct drafts; never alter or publish the original package.
    meta_path=root/'youtube/metadata.json'
    if meta_path.exists():
        meta=read_json(meta_path); m=next(e for e in meta['episodes'] if e['episode_id']==eid)
        for loc in ('ko','en'):
            item=copy.deepcopy(m['locales'][loc])
            item['source_title']=item['title']
            item['title']=packaging.metadata_title(series,eid,loc,ep['opener_kicker'][loc])
            item['description']=item['description'].replace('28초','33초').replace('28-second','33-second').replace('28 seconds','33 seconds')
            item['expected_filename']=f'{eid}_{loc}.mp4'
            item.update({'runtime_seconds':33,'upload_authorized':False,'status':'DRAFT_FINAL_VIDEO_REVIEW_REQUIRED'})
            folder=out/'youtube'/loc;folder.mkdir()
            for name,key in [('title.txt','title'),('description.txt','description')]: (folder/name).write_text(item[key]+'\n',encoding='utf-8')
            (folder/'tags.txt').write_text(', '.join(item['tags'])+'\n',encoding='utf-8')
            write_json(folder/'metadata_draft.json',item)
    (out/'STATUS.md').write_text('# PREPARED_NOT_GENERATED\n\nOnly prompts, target timing, packaging briefs and a run plan were prepared. No image, cover, Flow video, speech, music or final render has been generated. Follow START_CODEX.md and the v4 quality gates.\n',encoding='utf-8')


def qa_media(path: Path, cfg: dict) -> list[str]:
    if not path.is_file(): return [f'Missing final video: {path}']
    if not shutil.which('ffprobe'): return ['ffprobe unavailable.']
    try:
        data=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)],text=True,timeout=30))
        video=next(s for s in data['streams'] if s['codec_type']=='video')
        audio=next(s for s in data['streams'] if s['codec_type']=='audio')
        errors=[]
        if (video['width'],video['height'])!=(1080,1920): errors.append('Wrong resolution.')
        if video.get('avg_frame_rate')!='30/1': errors.append('Not CFR30 average rate; inspect timestamps.')
        if int(video.get('nb_frames',0))!=990: errors.append('Expected 990 video frames.')
        if abs(float(data['format']['duration'])-33)>0.05: errors.append('Expected 33 seconds.')
        if audio.get('channels')!=2 or audio.get('sample_rate')!='48000': errors.append('Expected 48kHz stereo delivery.')
        return errors
    except (StopIteration,KeyError,ValueError,subprocess.SubprocessError) as exc: return [f'Media inspection failed: {exc}']


def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__);sub=ap.add_subparsers(dest='command',required=True)
    sub.add_parser('check')
    p=sub.add_parser('prepare');p.add_argument('--episode',required=True);p.add_argument('--out',type=Path,required=True)
    p=sub.add_parser('qa');p.add_argument('--run',type=Path,required=True)
    args=ap.parse_args()
    try:
        cfg=read_json(ROOT/'production/director_v4.json');cat=read_json(ROOT/'production/catalog_v4.json')
        series=packaging.load(ROOT,cat);cat=packaging.apply_catalog(cat,series)
        errors=validate_contract(cfg,cat)
        if errors: raise ValueError('\n'.join(errors))
        if args.command=='prepare':
            prepare(ROOT,args.episode,args.out.resolve());print(f'Prepared local run: {args.out}. No generation or upload.');return 0
        if args.command=='qa':
            plan=read_json(args.run/'run_plan.json');eid=plan['episode_id']
            for loc in ('ko','en'):
                errors += qa_media(args.run/'exports'/f'{eid}_{loc}.mp4',cfg)
                cue_path=args.run/'captions'/f'{loc}.aligned.json'
                errors += validate_captions(read_json(cue_path),loc,cfg) if cue_path.exists() else [f'Missing measured {loc} captions.']
            report={'automated_issues':errors,'visual_review':'NOT_ASSESSED_BY_THIS_TOOL','listening_review':'NOT_ASSESSED_BY_THIS_TOOL','overall':'NEEDS_REVIEW'}
            write_json(args.run/'evidence/automated_qa.json',report)
            if errors: raise ValueError('\n'.join(errors))
            print('Technical fields passed. Actual font bounds, shot quality, music, listening and mobile preview still require review.');return 0
        print('PASS: v4 contract, 33s/990f, nine stills/seven clips, captions, budgets and eight episode packaging briefs.')
        print('This does not validate a generated image, Flow clip, voice or completed video.')
        return 0
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print(f'FAIL: {exc}',file=sys.stderr);return 1

if __name__=='__main__':
    raise SystemExit(main())
