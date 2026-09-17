"""Read-only text checks. No TTS, network, rendering, or paid API calls."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


def validate(root: Path) -> list[str]:
    """Check the ten narration texts against the reviewed manifest."""
    root = root.resolve()
    errors: list[str] = []
    try:
        manifest = json.loads((root / 'narration/manifest.json').read_text(encoding='utf-8'))
        stories = manifest['stories']
        if not isinstance(stories, list) or len(stories) != 5:
            return ['Expected exactly five stories.']
        if manifest.get('locales') != ['ko', 'en'] or manifest.get('narration_only') is not True:
            return ['Expected narration-only ko/en manifest.']
        seen: set[str] = set()
        for story in stories:
            sid = story['story_id']
            if sid in seen:
                errors.append(f'Duplicate story_id: {sid}')
            seen.add(sid)
            locales = story['locales']
            if set(locales) != {'ko', 'en'}:
                errors.append(f'{sid}: expected ko and en only.')
                continue
            for locale, spec in locales.items():
                expected_path = f'narration/{sid}.{locale}.txt'
                if spec['file'] != expected_path:
                    errors.append(f'{sid}/{locale}: unexpected file path.')
                    continue
                path = (root / expected_path).resolve()
                try:
                    path.relative_to(root)
                    text = path.read_text(encoding='utf-8')
                except (ValueError, OSError, UnicodeError) as exc:
                    errors.append(f'{expected_path}: {exc}')
                    continue
                # A Windows CRLF checkout must validate against Git's LF bytes.
                normalized = text.replace('\r\n', '\n').replace('\r', '\n')
                raw = normalized.encode('utf-8')
                blob = hashlib.sha1(f'blob {len(raw)}\0'.encode('ascii') + raw).hexdigest()
                if blob != spec['git_blob_sha']:
                    errors.append(f'{expected_path}: reviewed text changed; reconcile story/TXT/manifest.')
                lines = [line for line in normalized.splitlines() if line.strip()]
                if len(lines) != 7 or spec.get('scene_lines') != 7:
                    errors.append(f'{expected_path}: expected seven nonempty scene-lines.')
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'Invalid or unreadable manifest: {exc}')
    return errors


def main() -> int:
    errors = validate(Path(__file__).resolve().parents[1])
    if errors:
        print('\n'.join(f'FAIL: {error}' for error in errors), file=sys.stderr)
        return 1
    print('PASS: 5 stories / 10 reviewed narration texts / 70 scene-lines.')
    print('Text integrity only. Audio timing, naturalness, and video QA are NOT verified.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
