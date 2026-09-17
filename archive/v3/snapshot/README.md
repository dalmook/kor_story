# 먹빛설화 — Inkbound Tales / v3 파트 분할

**설화 하나를 28초에 압축하지 않습니다. 28초는 한 파트의 길이입니다.**

해와 달·선녀와 나무꾼·도깨비방망이는 각각 2파트, 구미호·매화령은 기존 단편을 유지합니다. 총 **5개 이야기 / 8개 에피소드 / 56개 시각 컷 / KO·EN 완성본 16개**를 위한 제작 명령서입니다. 아직 실제 영상·음성은 생성하지 않았습니다.

| 이야기 | PART 1 | PART 2 | 언어별 이야기 길이 |
|---|---|---|---:|
| [해와 달이 된 오누이](stories/01_sun_and_moon.md) | [문밖의 엄마](episodes/01_sun_and_moon_p01.md) | [하늘에서 내려온 동아줄](episodes/01_sun_and_moon_p02.md) | 56초 |
| [선녀와 나무꾼](stories/02_fairy_and_woodcutter.md) | [훔친 날개옷](episodes/02_fairy_and_woodcutter_p01.md) | [돌아간 날개](episodes/02_fairy_and_woodcutter_p02.md) | 56초 |
| [도깨비방망이](stories/04_dokkaebi_club.md) | [개암 한 알](episodes/04_dokkaebi_club_p01.md) | [욕심쟁이가 따라 한 밤](episodes/04_dokkaebi_club_p02.md) | 56초 |
| [구미호의 마지막 밤](stories/03_gumiho_last_night.md) | 단편 유지 | 없음 | 28초 |
| [매화령](stories/05_maehwa_spirit.md) | 단편 유지 | 없음 | 28초 |

## 실행

[HERMES_COMMANDS.md](HERMES_COMMANDS.md)에서 episode_id 하나를 선택합니다. 예: `01_sun_and_moon_p01` 또는 `04_dokkaebi_club_p02`. 시리즈 이름만 주면 그 시리즈의 p01만 시작하며, 다음 파트로 자동 진행하지 않습니다. 이번 저장소 수정은 제작 지침 변경이지 생성 실행 승인이 아닙니다.

[최종 전달문](docs/HERMES_BILINGUAL_HANDOFF.md) · [파트 구성/연속성/마이그레이션](docs/PART_PRODUCTION.md) · [제작 단계](docs/MASTER_PRODUCTION.md) · [두 언어 내레이션](docs/BILINGUAL_NARRATION.md) · [수묵 효과](docs/INK_EDITING_SPEC.md)

## 한 파트의 제작 구조

```text
시리즈 캐릭터·소품 참조 공유
  └ 선택한 파트: 이미지 7장 → Flow 4초 영상 7개 → 공용 무음·무문자 28초 마스터
                                              ├ 한국어 내레이션·자막 → *_ko.mp4
                                              └ 영어 내레이션·자막  → *_en.mp4
```

등장인물 대사·인용 연기·립싱크 없이 언어별 외부 내레이터 한 명만 사용합니다. 이미지 확대 슬라이드쇼로 대체하지 않습니다. 각 새 파트에는 7개 이미지 프롬프트·7개 Flow 동작 지시·6개 전환 경계·시간/효과음 방향·KO/EN 원고가 있습니다. 구미호/매화령의 기존 상세 연출과 대본은 보존했습니다.

## 예산의 단위는 이야기 전체가 아니라 파트

2026-09-17 Google 공식 검색 결과에 표시된 Gemini Omni Flash 720p/4초/결과1개=7크레딧 기준의 **계획 계산**입니다. 실행 전 계정 UI의 실제 단가/설정/잔액을 다시 확인합니다.

| 범위 | 시각 원본 | KO/EN 출력 | 예상 Flow 크레딧 |
|---|---:|---:|---:|
| 한 파트, 28초 | 7개 | 2개 | 49 |
| 한 이야기의 2파트, 총56초 | 14개 | 4개 | 98 |
| 현재 전체8편 | 56개 | 16개 | 392 |

한 파트 최대50. 2파트가49 또는50으로 된다는 뜻이 아닙니다. 두 언어는 같은 파트 원본을 재사용하므로 추가 Flow 생성0회입니다. 7개 첫 생성 후 여유1로 동일 설정 재시도는 불가능하며 양품7개를 보장하지 않습니다. 자동 재시도·유료 Edit/Extend/Upscale·추가 결제 금지. 이미지/TTS/음원/외부 렌더 비용은 별도 확인하며 같은 Flow 잔액을 쓰면 파트 예산에 합산합니다. [공식 비용표](https://support.google.com/flow/answer/16526234?hl=ko)

## 파트 분할 원칙

기존28초를 두 개의14초로 자르거나 느리게 늘리지 않습니다. 각 파트마다 새28초/7컷 구성을 설계합니다. 1부는 한 사건의 작은 결말, 2부는 맥락을 알 수 있는 시작과 이야기 결말을 가집니다. 별도 지난 이야기/예고/타이틀 컷을 붙이지 않습니다. 제목·파트 표시는 28초 안의 작은 후반 오버레이입니다.

내레이션은 그림을 볼 여유를 남깁니다. 새6파트 영어 원고는42~45단어이며 이는 실제 길이 검증이 아닙니다. 각 언어 연속 음성을 직접 듣고 호흡·자막·사건 시점을 맞춥니다. 파트 사이에는 캐릭터/소품/동선/마지막 상태를 공유합니다.

## 원고와 검사

활성 원고 목록은 [narration/manifest.json](narration/manifest.json)이며 episode_id별 KO/EN TXT 총16개입니다. 줄7개는 의미 구분이지 TTS7회 또는 고정4초 자막이 아닙니다.

```sh
python tools/check_narration_manifest.py
python -m unittest discover -s tests -v
```

검사는 원고 해시/줄 수/파트 연결/예산 설정의 구조 검사입니다. 실제 TTS 길이·자연스러움·영상 품질을 대신하지 않습니다. 과거 단일편01/02/04 원고와 관련 v2 문서는 [archive/v2](archive/v2/README.md)에 보존했습니다. 활성 지시는 v3만 사용합니다.

## 상태

BRIEFS_READY_MEDIA_NOT_GENERATED. 실제 이미지·Flow 영상·TTS·최종 MP4를 생성하거나 시청/청취 검수한 상태가 아닙니다. 이 업데이트는 Flow 크레딧을 사용하지 않습니다. 게시/예약 발행/다음 파트의 자동 제작도 실행하지 않습니다.

## 유튜브 업로드 문구 — 한국어·영어 16세트

[youtube/README.md](youtube/README.md)에 8편의 한국어·영어 기본 제목, 대체 제목, 설명, 해시태그와 Studio 태그를 정리했습니다. [채널 소개와 공통 키워드](youtube/CHANNELS.md), [헤르메스 추가 전달문](youtube/HERMES_HANDOFF.md)도 함께 있습니다.

자동화 원본은 [youtube/metadata.json](youtube/metadata.json)입니다. 헤르메스는 선택한 episode_id와 언어에 맞는 문구를 로컬 파일로 내보내고, 완성 영상과 대조한 뒤 전달합니다. 기존 스토리·원고·파트 구성은 유지합니다. 이번 추가는 문구 준비이며 YouTube 업로드·예약·채널 변경은 실행하지 않습니다.

```sh
python tools/youtube_metadata.py --check
python -m unittest discover -s tests -p 'test_youtube_metadata.py' -v
```
