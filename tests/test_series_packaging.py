"""Offline regression tests using explicit synthetic media/source fixtures.

The real eight-episode packaging data is used. No rendered media is evaluated.
Existing test_codex_production.py remains the repository-source regression suite.
"""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('series_director_test', ROOT/'tools/codex_production.py')
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
P = M.packaging


class SeriesPackagingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)/'repo'
        self.root.mkdir()
        self.data = json.loads((ROOT/P.SPEC).read_text(encoding='utf-8'))
        self.cfg = {
            'executor':'codex_direct',
            'frame':dict(width=1080,height=1920,fps=30,intro_frames=60,core_shots=7,shot_frames=120,outro_frames=90,total_frames=990),
            'image_assets':dict(count=9,baked_text=False),
            'video_assets':dict(count=7,normal_playback_rate=1,global_speedup_allowed=False),
            'type':dict(ko_caption_px=72,en_caption_px=68,caption_min_px=64,caption_max_lines=2,caption_top=1296,caption_line_height_px=88,caption_max_bottom=1472,caption_x=96,caption_width=828,word_by_word=False,karaoke=False,caption_min_seconds=1.8,ko_cps_max=12,en_cps_max=17),
            'transitions':dict(black_blobs=False,polygon_wipes=False,full_frame_color_veils=False,all_boundaries_must_be_hidden=False,allowed=['cut','dissolve'],max_dissolve_frames=10,max_dissolves_in_core=2),
            'budget':dict(expected_unit_credits=7,expected_initial_credits=49,flow_cap=50,outputs_per_request=1,automatic_paid_retries=0,additional_cash_cap=0),
        }
        self.cat = dict(runtime_seconds=33,auto_advance=False,image_prefix='APPROVED ART',flow_suffix='NO SPEECH',episodes=[])
        self.details = {}
        metadata = {'episodes':[]}
        for item in self.data['episodes']:
            eid = item['episode_id']
            next_id = eid[:-3]+'p02' if eid.endswith('p01') else None
            card = dict(episode_id=eid,brief=f'sources/{eid}.md',parent=None,next_episode=next_id,outro_mode='teaser' if next_id else 'closing',opener_title={'ko':'원제','en':'Original'},outro_title={'ko':'끝','en':'End'},opener_kicker={'ko':'설화 · 1부' if next_id else '설화 · 완결','en':'TALE · PART 1' if next_id else 'TALE · FINAL'},opener_prompt='OLD OPENER',outro_prompt='APPROVED OUTRO',core_transitions=['cut']*6)
            self.cat['episodes'].append(card)
            brief='\n'.join(f'IMAGE:\n```text\nApproved scene {i}.\n```\nFLOW:\n```text\nApproved motion {i}.\n```' for i in range(1,8))
            path=self.root/card['brief'];path.parent.mkdir(exist_ok=True);path.write_text(brief)
            for locale in ('ko','en'):
                path=self.root/f'narration/{eid}.{locale}.txt';path.parent.mkdir(exist_ok=True)
                path.write_text('\n'.join(f'Original {locale} line {i}' for i in range(1,8))+'\n')
            if item.get('detail_override'):
                detail=dict(episode_id=eid,character_reference='APPROVED SIBLINGS',shots=[dict(image=f'Detail scene {i}',flow=f'Detail motion {i}',narration_ko=f'상세 원고 {i}',narration_en=f'Detail line {i}',caption_lines_ko=[f'상세 원고 {i}'],caption_lines_en=[f'Detail line {i}'],speech_target_seconds=[2.2+(i-1)*4,5.2+(i-1)*4]) for i in range(1,8)])
                self.details[eid]=detail;self.write(item['detail_override'],detail)
            metadata['episodes'].append(dict(episode_id=eid,locales={loc:dict(title='ORIGINAL TITLE',description='28초 / 28-second tale. Original classification retained.',tags=['original-tag']) for loc in ('ko','en')}))
        self.write(P.SPEC,self.data)
        self.write('production/director_v4.json',self.cfg)
        self.write('production/catalog_v4.json',self.cat)
        self.write('youtube/metadata.json',metadata)

    def write(self,path,data): M.write_json(self.root/path,data)
    def load(self): self.write(P.SPEC,self.data);return P.load(self.root,self.cat)
    def run_episode(self,index=0):
        out=Path(self.tmp.name)/f'run_{index}'
        M.prepare(self.root,self.data['episodes'][index]['episode_id'],out)
        return out

    def test_real_spec_covers_eight_episodes(self): self.assertEqual(len(self.load()['episodes']),8)
    def test_missing_episode_rejected(self):
        self.data['episodes'].pop()
        with self.assertRaises(ValueError):self.load()
    def test_duplicate_episode_rejected(self):
        self.data['episodes'][1]=copy.deepcopy(self.data['episodes'][0])
        with self.assertRaises(ValueError):self.load()
    def test_extra_paid_assets_rejected(self):
        self.data['extra_flow_clips']=1
        with self.assertRaises(ValueError):self.load()
    def test_extra_images_rejected(self):
        self.data['extra_image_assets']=1
        with self.assertRaises(ValueError):self.load()
    def test_missing_focus_rejected(self):
        self.data['episodes'][0]['shot_focus'].pop()
        with self.assertRaises(ValueError):self.load()
    def test_three_line_title_rejected(self):
        self.data['episodes'][0]['title']['ko']='첫\n둘\n셋'
        with self.assertRaises(ValueError):self.load()
    def test_unverified_evidence_claim_rejected(self):
        self.data['evidence_scope']='WATCHED_ALL_VIDEOS'
        with self.assertRaises(ValueError):self.load()
    def test_missing_detail_rejected(self):
        (self.root/self.data['episodes'][1]['detail_override']).unlink()
        with self.assertRaises(ValueError):self.load()
    def test_wrong_detail_episode_rejected(self):
        e=self.data['episodes'][1];d=copy.deepcopy(self.details[e['episode_id']]);d['episode_id']='other';self.write(e['detail_override'],d)
        with self.assertRaises(ValueError):self.load()
    def test_unsafe_detail_path_rejected(self):
        self.data['episodes'][1]['detail_override']='../outside.json'
        with self.assertRaises(ValueError):self.load()
    def test_obscuring_transition_rejected(self):
        self.data['episodes'][1]['core_transitions'][0]='ink_wipe'
        with self.assertRaises(ValueError):self.load()
    def test_catalog_and_spec_not_mutated(self):
        original=copy.deepcopy(self.cat);data=copy.deepcopy(self.data)
        result=P.apply_catalog(self.cat,self.load())
        self.assertEqual(original,self.cat);self.assertEqual(data,self.data)
        self.assertNotEqual(result['episodes'][0]['opener_prompt'],'OLD OPENER')
    def test_teaser_matches_next_short_title(self):
        result=P.apply_catalog(self.cat,self.load())
        for card in result['episodes']:
            if card['next_episode']:
                self.assertEqual(card['outro_title'],P.episode(self.data,card['next_episode'])['title'])
            else:self.assertEqual(card['outro_title'],{'ko':'끝','en':'End'})
    def test_all_eight_prepare_preserve_contract(self):
        for i in range(8):
            with self.subTest(episode=i):
                out=self.run_episode(i);plan=M.read_json(out/'run_plan.json')
                self.assertEqual(len(list((out/'image_prompts').glob('*.txt'))),9)
                self.assertEqual(len(list((out/'flow_prompts').glob('*.txt'))),7)
                self.assertEqual(sum(s['frames'] for s in plan['segments']),990)
                self.assertEqual(plan['budgets']['expected_initial_credits'],49)
                self.assertFalse(plan['next_episode_autorun'])
                self.assertEqual(plan['status'],'PREPARED_NOT_GENERATED')
    def test_p02_uses_detailed_narration_and_alignment(self):
        out=self.run_episode(1)
        self.assertEqual((out/'audio/narration_ko.txt').read_text(encoding='utf-8'),'\n'.join(f'상세 원고 {i}' for i in range(1,8))+'\n')
        cues=M.read_json(out/'captions/ko.target.json');self.assertEqual(len(cues),7)
        self.assertEqual(cues[0]['timing_source'],'TARGET_NOT_MEASURED')
        plan=M.read_json(out/'run_plan.json');self.assertEqual(plan['boundaries'][0]['type'],'cut')
        self.assertEqual(plan['boundaries'][2]['type'],'dissolve')
    def test_source_images_and_flow_preserved(self):
        out=self.run_episode()
        for i in range(1,8):
            self.assertIn(f'Approved scene {i}.',(out/f'image_prompts/{i:02d}.txt').read_text(encoding='utf-8'))
            self.assertEqual((out/f'flow_prompts/{i:02d}.txt').read_text(encoding='utf-8'),f'Approved motion {i}.\n\n\nNO SPEECH\n')
    def test_narration_not_replaced_by_hook(self):
        out=self.run_episode()
        self.assertEqual((out/'audio/narration_en.txt').read_text(encoding='utf-8'),'\n'.join(f'Original en line {i}' for i in range(1,8))+'\n')
    def test_no_render_or_fake_review_pass(self):
        out=self.run_episode();brief=M.read_json(out/'packaging/brief.json')
        self.assertFalse(brief['cover_rendered']);self.assertEqual(brief['cover_source'],'images/00_opening.png')
        self.assertFalse(brief['upload_authorized'])
        for item in M.read_json(out/'evidence/packaging_review.json')['checks'].values():
            self.assertEqual(item,{'status':'PENDING','evidence':None})
        self.assertFalse(list(out.rglob('*.png')));self.assertFalse(list(out.rglob('*.mp4')))
    def test_metadata_is_localized_draft_and_keeps_source(self):
        out=self.run_episode()
        for loc in ('ko','en'):
            item=M.read_json(out/f'youtube/{loc}/metadata_draft.json')
            self.assertEqual(item['source_title'],'ORIGINAL TITLE')
            self.assertIn(' '.join(self.data['episodes'][0]['title'][loc].splitlines()),item['title'])
            self.assertIn('33초',item['description']);self.assertEqual(item['tags'],['original-tag'])
            self.assertFalse(item['upload_authorized'])
        self.assertEqual(M.read_json(self.root/'youtube/metadata.json')['episodes'][0]['locales']['ko']['title'],'ORIGINAL TITLE')
    def test_existing_run_not_overwritten(self):
        out=self.run_episode();marker=out/'keep.txt';marker.write_text('keep')
        with self.assertRaises(FileExistsError):M.prepare(self.root,self.data['episodes'][0]['episode_id'],out)
        self.assertEqual(marker.read_text(encoding='utf-8'),'keep')
    def test_unknown_episode_has_no_output(self):
        out=Path(self.tmp.name)/'unknown'
        with self.assertRaises(ValueError):M.prepare(self.root,'99_unknown',out)
        self.assertFalse(out.exists())

if __name__=='__main__':unittest.main()
