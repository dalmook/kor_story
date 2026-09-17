"""Isolated regression tests using copies of the active text files."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('checker', ROOT / 'tools/check_narration_manifest.py')
assert SPEC and SPEC.loader
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class ManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / 'narration', self.root / 'narration')
        self.path = self.root / 'narration/manifest.json'
        self.data = json.loads(self.path.read_text(encoding='utf-8'))

    def tearDown(self) -> None:
        self.temp.cleanup()

    def save(self) -> None:
        self.path.write_text(json.dumps(self.data, ensure_ascii=False), encoding='utf-8')

    def test_valid(self) -> None:
        self.assertEqual(CHECKER.validate(self.root), [])

    def test_windows_line_endings(self) -> None:
        for path in (self.root / 'narration').glob('*.txt'):
            path.write_bytes(path.read_bytes().replace(b'\n', b'\r\n'))
        self.assertEqual(CHECKER.validate(self.root), [])

    def test_changed_text(self) -> None:
        path = self.root / self.data['episodes'][0]['locales']['ko']['file']
        path.write_text(path.read_text(encoding='utf-8').replace('엄마', '아빠', 1), encoding='utf-8')
        self.assertTrue(CHECKER.validate(self.root))

    def test_missing_text(self) -> None:
        (self.root / self.data['episodes'][0]['locales']['en']['file']).unlink()
        self.assertTrue(CHECKER.validate(self.root))

    def test_duplicate_episode(self) -> None:
        self.data['episodes'].append(self.data['episodes'][0])
        self.save()
        self.assertTrue(CHECKER.validate(self.root))

    def test_wrong_link(self) -> None:
        self.data['episodes'][0]['next_episode'] = '05_maehwa_spirit'
        self.save()
        self.assertTrue(CHECKER.validate(self.root))

    def test_missing_part(self) -> None:
        self.data['episodes'].pop(1)
        self.save()
        self.assertTrue(CHECKER.validate(self.root))

    def test_automatic_next_forbidden(self) -> None:
        self.data['auto_advance'] = True
        self.save()
        self.assertTrue(CHECKER.validate(self.root))

    def test_wrong_budget_unit(self) -> None:
        self.data['budget_unit'] = 'story'
        self.save()
        self.assertTrue(CHECKER.validate(self.root))

    def test_orphan_retired_text(self) -> None:
        (self.root / 'narration/01_sun_and_moon.ko.txt').write_text('retired', encoding='utf-8')
        self.assertTrue(CHECKER.validate(self.root))

    def test_invalid_json(self) -> None:
        self.path.write_text('{', encoding='utf-8')
        self.assertTrue(CHECKER.validate(self.root))

    def test_expected_total(self) -> None:
        self.assertEqual(len(self.data['episodes']), 8)
        self.assertEqual(8 * self.data['flow_clips_per_episode'], 56)
        self.assertEqual(8 * self.data['expected_initial_flow_credits_per_episode'], 392)
        self.assertEqual(2 * self.data['expected_initial_flow_credits_per_episode'], 98)


if __name__ == '__main__':
    unittest.main()
