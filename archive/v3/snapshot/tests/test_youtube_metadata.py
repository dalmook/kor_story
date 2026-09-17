"""Offline tests of draft metadata. No account or upload operations."""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('youtube_metadata_tool', ROOT / 'tools/youtube_metadata.py')
assert SPEC and SPEC.loader
TOOL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TOOL)


class MetadataTests(unittest.TestCase):
    def setUp(self):
        self.data = TOOL.load(ROOT)
        self.manifest = json.loads((ROOT / 'narration/manifest.json').read_text(encoding='utf-8'))
        self.ko = self.data['episodes'][0]['locales']['ko']
        self.en = self.data['episodes'][0]['locales']['en']

    def test_valid(self):
        self.assertEqual(TOOL.validate(self.data, self.manifest), [])

    def test_count(self):
        self.assertEqual(len(self.data['episodes']), 8)
        self.assertEqual(sum(len(e['locales']) for e in self.data['episodes']), 16)

    def test_long_title(self):
        self.ko['title'] = '가' * 101
        self.assertTrue(TOOL.validate(self.data, self.manifest))

    def test_description_utf8_bytes(self):
        self.ko['description'] = '가' * 1667
        self.assertTrue(TOOL.validate(self.data, self.manifest))

    def test_tag_accounting(self):
        self.assertEqual(TOOL.tag_units(['Foo-Baz', 'Foo Baz']), 17)
        self.en['tags'] = ['x' * 501]
        self.assertTrue(TOOL.validate(self.data, self.manifest))

    def test_missing_locale(self):
        del self.data['episodes'][0]['locales']['en']
        self.assertTrue(TOOL.validate(self.data, self.manifest))

    def test_wrong_filename(self):
        self.en['expected_filename'] = '01_sun_and_moon_p01_ko.mp4'
        self.assertTrue(TOOL.validate(self.data, self.manifest))

    def test_no_publication_authority(self):
        self.data['upload_authorized'] = True
        self.assertTrue(TOOL.validate(self.data, self.manifest))

    def test_no_korean_leak(self):
        self.en['title'] += ' 한국어'
        self.assertTrue(TOOL.validate(self.data, self.manifest))

    def test_original_label(self):
        self.data['episodes'][-1]['locales']['en']['description'] = self.data['episodes'][-1]['locales']['en']['description'].replace('An original Korean-inspired tale.', 'A true story.')
        self.assertTrue(TOOL.validate(self.data, self.manifest))

    def test_spoiler(self):
        self.data['episodes'][-1]['locales']['ko']['title'] = '무덤의 비밀'
        self.assertTrue(TOOL.validate(self.data, self.manifest))

    def test_wrong_part(self):
        self.data['episodes'][0]['part_number'] = 2
        self.assertTrue(TOOL.validate(self.data, self.manifest))

    def test_no_fake_url(self):
        self.ko['description'] = 'https://youtube.com/watch?v=not-real\n' + self.ko['description']
        self.assertTrue(TOOL.validate(self.data, self.manifest))

    def test_markdown_matches_json(self):
        for ep in self.data['episodes']:
            actual = (ROOT / 'youtube/episodes' / f"{ep['episode_id']}.md").read_text(encoding='utf-8')
            self.assertEqual(actual, TOOL.document(ep))

    def test_no_duplicate_tags(self):
        self.en['tags'].append(self.en['tags'][0].upper())
        self.assertTrue(TOOL.validate(self.data, self.manifest))

    def test_all_active_ids(self):
        self.data['episodes'].pop()
        self.assertTrue(TOOL.validate(self.data, self.manifest))


if __name__ == '__main__':
    unittest.main()
