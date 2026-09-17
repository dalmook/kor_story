"""Offline series art direction. No generation, network calls, or media approval."""
from __future__ import annotations
import copy
import json
from pathlib import Path

SPEC = 'production/series_packaging_v4.json'
CHECKS = (
    'first_frame_story_clue', 'one_focal_subject', 'title_mobile_ko',
    'title_mobile_en', 'approved_character_and_prop_continuity',
    'no_premature_resolution', 'seven_shot_causal_readability',
    'opening_closing_motif', 'cover_source_and_text_separation',
)


def load(root: Path, catalog: dict) -> dict:
    """Validate the complete overlay before any output directory is created."""
    spec = json.loads((root / SPEC).read_text(encoding='utf-8'))
    if spec.get('version') != 4 or spec.get('revision') != 'series-packaging-1':
        raise ValueError('Unsupported series packaging specification.')
    if spec.get('evidence_scope') != 'USER_SCREENSHOTS_NOT_FULL_VIDEO_AUDIT':
        raise ValueError('Packaging evidence scope must remain explicit.')
    if spec.get('extra_flow_clips') != 0 or spec.get('extra_image_assets') != 0:
        raise ValueError('Packaging must reuse the existing nine-image/seven-clip contract.')
    entries = spec.get('episodes', [])
    ids = [e['episode_id'] for e in entries]
    if len(ids) != len(set(ids)) or set(ids) != {e['episode_id'] for e in catalog['episodes']}:
        raise ValueError('Packaging must cover each catalog episode exactly once.')
    for entry in entries:
        for locale in ('ko', 'en'):
            title = entry['title'][locale]
            if not isinstance(title, str) or not title.strip() or len(title.splitlines()) > 2:
                raise ValueError('A cover title needs one or two nonempty lines.')
            if any(not line.strip() for line in title.splitlines()):
                raise ValueError('Blank title lines are forbidden.')
            if not isinstance(entry['question'][locale], str) or not entry['question'][locale].strip():
                raise ValueError('Missing localized visual question.')
        for key in ('opener_direction', 'motif', 'payoff', 'spoiler_guard', 'accent_rule'):
            if not isinstance(entry.get(key), str) or not entry[key].strip():
                raise ValueError(f'Missing directing field: {key}')
        focuses = entry.get('shot_focus', [])
        if len(focuses) != 7 or any(not isinstance(v, str) or not v.strip() for v in focuses):
            raise ValueError('Exactly seven shot-focus notes are required.')
        transitions = entry.get('core_transitions')
        if transitions is not None and (len(transitions) != 6 or
                any(t not in ('cut', 'dissolve') for t in transitions) or
                transitions.count('dissolve') > 2):
            raise ValueError('Invalid packaging transition override.')
        if entry.get('opening_transition', 'dissolve') not in ('cut', 'dissolve'):
            raise ValueError('Invalid opening transition.')
        override = entry.get('detail_override')
        if override:
            path = (root / override).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file():
                raise ValueError('Detail override must be an existing in-repository file.')
            detail = json.loads(path.read_text(encoding='utf-8'))
            if detail.get('episode_id') != entry['episode_id'] or len(detail.get('shots', [])) != 7:
                raise ValueError('Detail override episode/shot mismatch.')
    return spec


def episode(spec: dict, eid: str) -> dict:
    try:
        return next(e for e in spec['episodes'] if e['episode_id'] == eid)
    except StopIteration as exc:
        raise ValueError(f'No packaging for episode: {eid}') from exc


def apply_catalog(catalog: dict, spec: dict) -> dict:
    """Resolve card-only overrides without changing the caller's source catalog."""
    result = copy.deepcopy(catalog)
    for card in result['episodes']:
        entry = episode(spec, card['episode_id'])
        card['opener_title'] = copy.deepcopy(entry['title'])
        # This is a complete replacement of composition, not a contradictory suffix.
        card['opener_prompt'] = entry['opener_direction'] + '\n' + spec['visual_rules']
        card['packaging_revision'] = spec['revision']
        if entry.get('detail_override'):
            card['detail_override'] = entry['detail_override']
        for key in ('core_transitions', 'opening_transition'):
            if key in entry:
                card[key] = copy.deepcopy(entry[key])
        if card['next_episode']:
            card['outro_title'] = copy.deepcopy(episode(spec, card['next_episode'])['title'])
    return result


def direct_images(spec: dict, eid: str, images: list[str]) -> list[str]:
    if len(images) != 7:
        raise ValueError('Packaging cannot add or remove a core image.')
    entry = episode(spec, eid)
    return [image + '\n\nVISUAL PRIORITY (composition only, not another event):\n'
            + focus + '\nPreserve the source scene, approved identity, props, positions '
            'and its single action. Do not import any later-shot event. '
            'Approved existing assets are reused, not regenerated to satisfy this note.'
            for image, focus in zip(images, entry['shot_focus'])]


def metadata_title(spec: dict, eid: str, locale: str, kicker: str) -> str:
    title = ' '.join(episode(spec, eid)['title'][locale].splitlines())
    return f'{title} | {kicker}'


def write_handoff(out: Path, spec: dict, eid: str, texts: dict, card: dict, cfg: dict) -> None:
    entry = copy.deepcopy(episode(spec, eid))
    directory = out / 'packaging'
    directory.mkdir()
    entry.update({
        'status': 'PREPARED_NOT_GENERATED', 'revision': spec['revision'],
        'question_usage': 'EDITORIAL_BRIEF_ONLY_NOT_EXTRA_VO_OR_CAPTION',
        'approved_assets_win': True, 'existing_narration_preserved': texts,
        'cover_source': 'images/00_opening.png',
        'cover_outputs': {'ko': 'packaging/cover_ko.png', 'en': 'packaging/cover_en.png'},
        'cover_rendered': False, 'extra_flow_clips': 0, 'extra_image_assets': 0,
        'source_art_text_free': True, 'same_art_for_both_locales': True,
        'type': copy.deepcopy(cfg['type']), 'cards': copy.deepcopy(card),
        'proof_sizes': [[1080, 1920], [360, 640], [180, 320]],
        'proof_note': 'Project review sizes, not platform-mandated upload dimensions.',
        'upload_authorized': False,
    })
    (directory / 'brief.json').write_text(json.dumps(entry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    review = {'revision': spec['revision'], 'episode_id': eid,
              'status': 'PENDING_VISUAL_REVIEW',
              'checks': {name: {'status': 'PENDING', 'evidence': None} for name in CHECKS}}
    (out / 'evidence/packaging_review.json').write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [f'# {eid} — 패키징 검수 대기', '',
             '이 파일은 감독 지침이다. 표지·영상·검수 결과를 생성한 것이 아니다.', '',
             f"시각적 질문: {entry['question']['ko']}",
             f"소품/구도 모티프: {entry['motif']}",
             f"결말에서 회수: {entry['payoff']}",
             f"앞부분 스포일러 금지: {entry['spoiler_guard']}", '',
             '## 7컷의 역할 — 기존 사건과 음성은 유지', '']
    lines += [f'{i:02d}. {text}' for i, text in enumerate(entry['shot_focus'], 1)]
    lines += ['', '## 실제 자산으로 확인할 항목', '']
    lines += [f'- [ ] {name}' for name in CHECKS]
    lines += ['', '기존 승인 자산부터 재사용한다. 표지는 images/00_opening.png에 언어별 글자를 로컬 합성한다.',
              '그림 속 글자 생성, 추가 Flow, 자동 유료 재생성, 게시·예약은 하지 않는다.',
              '첫 프레임은 원화의 단서로 후킹한다. 오프닝에 음성이나 추가 문구를 얹지 않는다.',
              '정적 규격 검사는 실제 그림의 가독성·음성·시청 유지율 검사가 아니다.']
    (directory / 'REVIEW.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
