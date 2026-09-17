"""Read-only checks for episode text, part links and budget configuration.

No network, TTS, Flow, media rendering or paid API calls are made.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys


def git_blob_sha(text: str) -> str:
    """Normalize Windows checkout line endings before computing a Git blob ID."""
    raw = text.replace('\r\n', '\n').replace('\r', '\n').encode('utf-8')
    return hashlib.sha1(f'blob {len(raw)}\0'.encode('ascii') + raw).hexdigest()


def validate(root: Path) -> list[str]:
    """Validate active narration files; this does NOT measure speech or video."""
    root = root.resolve()
    errors: list[str] = []
    try:
        manifest = json.loads((root / 'narration/manifest.json').read_text(encoding='utf-8'))
        if not isinstance(manifest, dict) or manifest.get('schema_version') != 3:
            return ['Expected schema_version 3.']
        expected = {
            'narration_only': True, 'locales': ['ko', 'en'], 'budget_unit': 'episode',
            'flow_clips_per_episode': 7, 'seconds_per_clip': 4,
            'seconds_per_episode': 28, 'fps': 30, 'frames_per_episode': 840,
            'expected_initial_flow_credits_per_episode': 49,
            'flow_credit_cap_per_episode': 50, 'auto_advance': False,
        }
        for key, value in expected.items():
            if manifest.get(key) != value:
                errors.append(f'Invalid {key}: expected {value!r}.')
        episodes = manifest['episodes']
        if not isinstance(episodes, list) or not episodes:
            return errors + ['Expected a nonempty episode list.']
        by_id: dict[str, dict] = {}
        by_story: dict[str, list[dict]] = {}
        expected_texts: set[str] = set()
        for ep in episodes:
            eid, sid = ep['episode_id'], ep['story_id']
            if not all(isinstance(v, str) and re.fullmatch(r'[0-9]{2}_[a-z0-9_]+', v) for v in (eid, sid)):
                errors.append('Invalid episode/story identifier.')
                continue
            if eid in by_id:
                errors.append(f'Duplicate episode: {eid}.')
                continue
            by_id[eid] = ep
            by_story.setdefault(sid, []).append(ep)
            part, count = ep['part_number'], ep['part_count']
            if type(part) is not int or type(count) is not int or not 1 <= part <= count:
                errors.append(f'{eid}: invalid part range.')
                continue
            canonical_id = sid if count == 1 else f'{sid}_p{part:02d}'
            if eid != canonical_id:
                errors.append(f'{eid}: expected episode ID {canonical_id}.')
            canonical_brief = f'stories/{sid}.md' if count == 1 else f'episodes/{eid}.md'
            if ep['brief'] != canonical_brief:
                errors.append(f'{eid}: unexpected brief path.')
            if set(ep['locales']) != {'ko', 'en'}:
                errors.append(f'{eid}: expected ko and en.')
                continue
            for locale, spec in ep['locales'].items():
                relative = f'narration/{eid}.{locale}.txt'
                expected_texts.add(relative)
                if spec['file'] != relative:
                    errors.append(f'{eid}/{locale}: unexpected text path.')
                    continue
                path = (root / relative).resolve()
                try:
                    path.relative_to(root)
                    text = path.read_text(encoding='utf-8')
                except (ValueError, OSError, UnicodeError) as exc:
                    errors.append(f'{relative}: {exc}')
                    continue
                if git_blob_sha(text) != spec['git_blob_sha']:
                    errors.append(f'{relative}: reviewed text changed; reconcile brief/TXT/manifest.')
                if len([line for line in text.splitlines() if line.strip()]) != 7 or spec.get('scene_lines') != 7:
                    errors.append(f'{relative}: expected seven nonempty scene lines.')
        for sid, group in by_story.items():
            counts = {ep['part_count'] for ep in group}
            if len(counts) != 1:
                errors.append(f'{sid}: inconsistent part_count.')
                continue
            count = group[0]['part_count']
            if type(count) is not int or {ep['part_number'] for ep in group} != set(range(1, count + 1)):
                errors.append(f'{sid}: missing or duplicate part numbers.')
                continue
            ordered = sorted(group, key=lambda ep: ep['part_number'])
            for index, ep in enumerate(ordered):
                previous = ordered[index - 1]['episode_id'] if index else None
                following = ordered[index + 1]['episode_id'] if index + 1 < len(ordered) else None
                if ep.get('previous_episode') != previous or ep.get('next_episode') != following:
                    errors.append(f"{ep['episode_id']}: broken previous/next link.")
        actual_texts = {path.relative_to(root).as_posix() for path in (root / 'narration').glob('*.txt')}
        if actual_texts != expected_texts:
            errors.append('Active TXT set differs from manifest; archive retired texts or restore missing files.')
    except (OSError, UnicodeError, ValueError, KeyError, TypeError, AttributeError) as exc:
        errors.append(f'Invalid manifest or data: {exc}')
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print('\n'.join(f'FAIL: {item}' for item in errors), file=sys.stderr)
        return 1
    data = json.loads((root / 'narration/manifest.json').read_text(encoding='utf-8'))
    count = len(data['episodes'])
    stories = len({ep['story_id'] for ep in data['episodes']})
    print(f'PASS: {stories} stories / {count} episodes / {count * 2} texts / {count * 14} scene lines.')
    print('Text, links and budget structure only. Speech timing, naturalness and media QA are NOT verified.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
