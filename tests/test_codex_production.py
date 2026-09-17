"""Offline contract tests; no paid services or user files are altered."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('director',ROOT/'tools/codex_production.py')
M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)

class DirectorTests(unittest.TestCase):
    def setUp(self):
        self.cfg=M.read_json(ROOT/'production/director_v4.json')
        self.cat=M.read_json(ROOT/'production/catalog_v4.json')
    def bad(self): self.assertTrue(M.validate_contract(self.cfg,self.cat))
    def test_valid(self): self.assertEqual(M.validate_contract(self.cfg,self.cat),[])
    def test_old_duration_rejected(self): self.cfg['frame']['total_frames']=840;self.bad()
    def test_missing_teaser_time(self): self.cfg['frame']['outro_frames']=0;self.bad()
    def test_caption_small(self): self.cfg['type']['ko_caption_px']=40;self.bad()
    def test_low_position(self): self.cfg['type']['caption_top']=1660;self.bad()
    def test_word_flash(self): self.cfg['type']['word_by_word']=True;self.bad()
    def test_black_blob(self): self.cfg['transitions']['black_blobs']=True;self.bad()
    def test_full_veil(self): self.cfg['transitions']['full_frame_color_veils']=True;self.bad()
    def test_long_dissolve(self): self.cfg['transitions']['max_dissolve_frames']=24;self.bad()
    def test_bad_cost(self): self.cfg['budget']['expected_initial_credits']=98;self.bad()
    def test_two_outputs(self): self.cfg['budget']['outputs_per_request']=2;self.bad()
    def test_speedup(self): self.cfg['video_assets']['normal_playback_rate']=1.2;self.bad()
    def test_only_seven_images(self): self.cfg['image_assets']['count']=7;self.bad()
    def test_next_autorun(self): self.cat['auto_advance']=True;self.bad()
    def test_teaser_on_finale(self): self.cat['episodes'][1]['outro_mode']='teaser';self.bad()
    def test_provisional_captions_fail_final(self):
        d=M.read_json(ROOT/'production/01_sun_and_moon_p01_v4.json')
        c=[{'start':2.2,'end':5.3,'lines':d['shots'][0]['caption_lines_ko'],'timing_source':'TARGET_NOT_MEASURED'}]
        self.assertTrue(M.validate_captions(c,'ko',self.cfg))
        c[0]['timing_source']='manually_listened'
        self.assertEqual(M.validate_captions(c,'ko',self.cfg),[])
    def test_short_cue_rejected(self):
        self.assertTrue(M.validate_captions([{'start':2.2,'end':2.9,'lines':['Hello'],'timing_source':'manually_listened'}],'en',self.cfg))
    def test_prepare_nine_prompts_seven_flow(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'run';M.prepare(ROOT,'01_sun_and_moon_p01',out)
            self.assertEqual(len(list((out/'image_prompts').glob('*.txt'))),9)
            self.assertEqual(len(list((out/'flow_prompts').glob('*.txt'))),7)
            self.assertEqual(len(list((out/'flow').glob('*.mp4'))),0)
            plan=M.read_json(out/'run_plan.json')
            self.assertEqual(len(plan['segments']),9)
            self.assertEqual(sum(s['frames'] for s in plan['segments']),990)
            self.assertEqual([s['from'] for s in plan['segments']],[0,60,180,300,420,540,660,780,900])
            self.assertEqual(len(plan['boundaries']),8)
            self.assertIsNone(M.read_json(out/'asset_manifest.json')['actual_flow_spent'])
            with self.assertRaises(FileExistsError):M.prepare(ROOT,'01_sun_and_moon_p01',out)
    def test_narration_caption_match(self):
        d=M.read_json(ROOT/'production/01_sun_and_moon_p01_v4.json')
        for s in d['shots']:
            for loc in ('ko','en'):
                self.assertEqual(M.normalized(s['narration_'+loc]),M.normalized(' '.join(s['caption_lines_'+loc])))
    def test_prompt_parser(self):
        src='\n'.join('IMAGE:\n```text\nArt\n```\nFLOW:\n```text\nMove\n```' for _ in range(7))
        im,fl=M.prompt_blocks(src);self.assertEqual(len(im),7)
        with self.assertRaises(ValueError):M.prompt_blocks('')
    def test_missing_video_fail(self):
        self.assertTrue(M.qa_media(Path('/nonexistent/video.mp4'),self.cfg))
    def test_p1_target_times_fit_core(self):
        d=M.read_json(ROOT/'production/01_sun_and_moon_p01_v4.json')
        for s in d['shots']:
            a,b=s['speech_target_seconds'];start=s['start_frame']/30
            self.assertGreaterEqual(a,start);self.assertLessEqual(b,start+4)

if __name__=='__main__':unittest.main()
