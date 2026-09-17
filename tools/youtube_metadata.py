"""Validate, document and export local YouTube metadata drafts. Never uploads."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def tag_units(tags: list[str]) -> int:
    """YouTube API: include comma separators and quotes around tags with spaces."""
    return sum(len(tag) + (2 if ' ' in tag else 0) for tag in tags) + max(0, len(tags) - 1)


def load(root: Path) -> dict[str, Any]:
    return json.loads((root / 'youtube/metadata.json').read_text(encoding='utf-8'))


def validate(data: dict[str, Any], manifest: dict[str, Any]) -> list[str]:
    """Check fields/limits/episode routing; does not check a video or publish."""
    errors: list[str] = []
    try:
        if data.get('upload_authorized') is not False:
            errors.append('Metadata preparation must not authorize upload.')
        if data.get('schema_version') != 1 or set(data['channels']) != {'ko', 'en'}:
            errors.append('Unsupported schema or channel keys.')
        source = {e['episode_id']: e for e in manifest['episodes']}
        rows = data['episodes']
        if not isinstance(rows, list) or not rows:
            return errors + ['Expected a nonempty episode list.']
        ids = [r['episode_id'] for r in rows]
        if len(ids) != len(set(ids)):
            errors.append('Duplicate episode_id.')
        if set(ids) != set(source):
            errors.append('Metadata episode IDs differ from the active narration manifest.')
        seen_titles: set[tuple[str, str]] = set()
        for ep in rows:
            eid = ep['episode_id']
            if not re.fullmatch(r'[0-9]{2}_[a-z0-9_]+', eid):
                errors.append(f'{eid}: unsafe episode ID.')
                continue
            src = source.get(eid)
            if src is None:
                continue
            for key in ['story_id', 'part_number', 'part_count', 'classification', 'previous_episode', 'next_episode']:
                if ep[key] != src[key]:
                    errors.append(f'{eid}: {key} differs from the active manifest.')
            if ep['source_brief'] != src['brief']:
                errors.append(f'{eid}: wrong source brief.')
            if set(ep['locales']) != {'ko', 'en'}:
                errors.append(f'{eid}: both locales are required.')
                continue
            for loc, text in ep['locales'].items():
                prefix = f'{eid}/{loc}'
                for key in ['title', 'alternate_title']:
                    title = text[key]
                    if not isinstance(title, str) or not title.strip() or len(title) > 100 or any(c in title for c in '<>\r\n'):
                        errors.append(f'{prefix}: invalid {key} (100-character limit).')
                if text['title'] == text['alternate_title']:
                    errors.append(f'{prefix}: alternative duplicates primary title.')
                if (loc, text['title']) in seen_titles:
                    errors.append(f'{prefix}: primary title duplicates another video.')
                seen_titles.add((loc, text['title']))
                desc = text['description']
                if not isinstance(desc, str) or not desc.strip() or len(desc.encode('utf-8')) > 5000 or '<' in desc or '>' in desc:
                    errors.append(f'{prefix}: invalid description (API limit: 5000 UTF-8 bytes).')
                hashes = text['hashtags']
                if not isinstance(hashes, list) or len(hashes) != 3 or len(set(hashes)) != 3:
                    errors.append(f'{prefix}: this pack uses exactly three distinct hashtags.')
                elif not all(re.fullmatch(r'#[\w]+', h, flags=re.UNICODE) for h in hashes):
                    errors.append(f'{prefix}: invalid hashtag.')
                elif not desc.endswith(' '.join(hashes)):
                    errors.append(f'{prefix}: description must contain its hashtags once at the end.')
                elif any(desc.count(h) != 1 for h in hashes):
                    errors.append(f'{prefix}: duplicate hashtag in description.')
                tags = text['tags']
                if not isinstance(tags, list) or not tags or not all(isinstance(t, str) and t.strip() == t and t for t in tags):
                    errors.append(f'{prefix}: invalid tags.')
                elif len({t.casefold() for t in tags}) != len(tags) or any(any(c in t for c in '#,\r\n') for t in tags):
                    errors.append(f'{prefix}: duplicate tags or hashtag/CSV syntax in a tag.')
                elif tag_units(tags) > 500:
                    errors.append(f'{prefix}: tags exceed 500 API-counted characters.')
                if text['expected_filename'] != f'{eid}_{loc}.mp4':
                    errors.append(f'{prefix}: wrong video filename routing.')
                if text['video_language'] != loc or text['metadata_language'] != loc:
                    errors.append(f'{prefix}: wrong language routing.')
                public = '\n'.join([text['title'], text['alternate_title'], desc, ' '.join(tags)])
                if loc == 'en' and re.search(r'[가-힣]', public):
                    errors.append(f'{prefix}: Korean text leaked into the English upload fields.')
                if re.search(r'https?://|\{\{|\bTODO\b|\bTBD\b', public, flags=re.I):
                    errors.append(f'{prefix}: unapproved URL or placeholder in public fields.')
                if ep['classification'] == 'original':
                    label = '한국풍 창작 설화' if loc == 'ko' else 'original Korean-inspired tale'
                    if label.casefold() not in desc.casefold():
                        errors.append(f'{prefix}: original-story label missing.')
                for term in ep['editorial_review']['avoid_spoilers'][loc]:
                    found = term in public if loc == 'ko' else re.search(r'\b' + re.escape(term) + r'\b', public, flags=re.I)
                    if found:
                        errors.append(f'{prefix}: listed spoiler leaked: {term}.')
    except (KeyError, TypeError, AttributeError, ValueError) as exc:
        errors.append(f'Malformed metadata or manifest: {exc}')
    return errors


def document(ep: dict[str, Any]) -> str:
    """Generate copy-ready blocks; backstage tags are deliberately separate."""
    eid = ep['episode_id']
    lines = [f'# {eid} — 유튜브 업로드 문구', '',
             '기준 데이터: `../metadata.json`. 실제 완성 영상과 일치하는지 확인한 뒤 사용한다. 이 문서는 게시 승인이 아니다.', '',
             f"구성: {ep['part_number']}/{ep['part_count']} · {ep['classification']} · 28초 · 같은 시각 마스터의 KO/EN 출력", '']
    for loc, label in [('ko', '한국어 채널'), ('en', '영어 채널 — Dalbong Korean Tales')]:
        t = ep['locales'][loc]
        lines += [f'## {label}', '', f"대상 파일: `{t['expected_filename']}`", '',
                  '### 기본 제목', '```text', t['title'], '```', '',
                  '### 대체 제목 — 두 제목 중 하나만 사용', '```text', t['alternate_title'], '```', '',
                  '### 설명 — 마지막 해시태그까지 전체 복사', '```text', t['description'], '```', '',
                  '### Studio 태그 입력란 — 설명란에 붙이지 않음', '```text', ', '.join(t['tags']), '```', '',
                  '### 해시태그 — 위 설명에 이미 포함, 중복 추가하지 않음', '```text', ' '.join(t['hashtags']), '```', '',
                  f"검사 수치: 제목 {len(t['title'])}자 / 대체 제목 {len(t['alternate_title'])}자 / 설명 {len(t['description'].encode('utf-8'))} UTF-8 bytes / 태그 {tag_units(t['tags'])}자(API 방식).", '']
    neighbor = ep['next_episode'] or ep['previous_episode']
    if neighbor:
        lines += ['## 파트 연결 — 운영용, 위 설명에 자동 추가하지 않음', '',
                  f'연결 후보: `{neighbor}`의 **같은 언어·같은 실제 채널** 영상.',
                  '해당 영상의 공개/일부공개 상태와 실제 ID를 확인한 후 Studio의 관련 동영상으로 연결한다. 다음 파트가 아직 없으면 비워 둔다. 미공개 파트를 볼 수 있다고 쓰거나 링크를 지어내지 않는다.', '']
    return '\n'.join(lines).rstrip() + '\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Read-only validation, including generated Markdown.')
    parser.add_argument('--write-docs', action='store_true', help='Regenerate youtube/episodes/*.md from metadata.json.')
    parser.add_argument('--episode')
    parser.add_argument('--locale', choices=['ko', 'en'])
    parser.add_argument('--out', type=Path, help='New local output directory; existing outputs are not overwritten.')
    args = parser.parse_args()
    if args.write_docs and (args.check or args.episode or args.out):
        parser.error('--write-docs must be used alone.')
    if any([args.episode, args.locale, args.out]) and not all([args.episode, args.locale, args.out]):
        parser.error('--episode, --locale and --out must be provided together.')
    try:
        data = load(ROOT)
        manifest = json.loads((ROOT / 'narration/manifest.json').read_text(encoding='utf-8'))
        errors = validate(data, manifest)
        if errors:
            raise ValueError('\n'.join(errors))
        if args.write_docs:
            folder = ROOT / 'youtube/episodes'
            folder.mkdir(parents=True, exist_ok=True)
            for ep in data['episodes']:
                (folder / f"{ep['episode_id']}.md").write_text(document(ep), encoding='utf-8')
            print('Generated copy-ready Markdown from the canonical JSON. No upload.')
            return 0
        for ep in data['episodes']:
            path = ROOT / 'youtube/episodes' / f"{ep['episode_id']}.md"
            if not path.exists() or path.read_text(encoding='utf-8') != document(ep):
                raise ValueError(f'{path.name}: docs are missing or stale; run --write-docs after review.')
        if args.episode:
            ep = next((e for e in data['episodes'] if e['episode_id'] == args.episode), None)
            if ep is None:
                raise ValueError('Unknown episode_id.')
            text = ep['locales'][args.locale]
            out = args.out.resolve()
            out.mkdir(parents=True, exist_ok=False)
            outputs = {'title.txt': text['title'], 'description.txt': text['description'],
                       'tags.txt': ', '.join(text['tags']), 'hashtags.txt': ' '.join(text['hashtags']),
                       'metadata_draft.json': json.dumps({'episode_id': ep['episode_id'], 'locale': args.locale,
                           'channel_id': data['channels'][args.locale]['channel_id'], 'upload_authorized': False,
                           'status': 'DRAFT_FINAL_VIDEO_REVIEW_REQUIRED', **text}, ensure_ascii=False, indent=2)}
            for name, content in outputs.items():
                (out / name).write_text(content + '\n', encoding='utf-8')
            print(f'Exported local drafts to {out}. No upload or scheduling.')
        else:
            print(f"PASS: {len(data['episodes'])} episodes / {len(data['episodes'])*2} locale sets; fields, limits, routing and Markdown match.")
            print('Metadata text checks only. Final video, audience/disclosure settings and channel IDs need human review.')
        return 0
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        print(f'FAIL: {exc}')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
