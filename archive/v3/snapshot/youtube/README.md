# 유튜브 업로드 문구 — 한국어 채널 / 영어 채널

**v3의 8개 에피소드 × 2개 언어 = 16세트**입니다. 각 세트에 기본 제목, 대체 제목 1개, 설명, 해시태그 3개, Studio용 태그를 준비했습니다. 제목은 둘 중 하나만 사용합니다. 기존 파트 구성·대본·영상 생성 지시는 변경하지 않습니다.

| 영상 | 한국어·영어 복사 문구 |
|---|---|
| 해와 달 1부 — 문밖의 엄마 | [제목·설명·태그](episodes/01_sun_and_moon_p01.md) |
| 해와 달 2부 — 하늘에서 내려온 동아줄 | [제목·설명·태그](episodes/01_sun_and_moon_p02.md) |
| 선녀와 나무꾼 1부 — 훔친 날개옷 | [제목·설명·태그](episodes/02_fairy_and_woodcutter_p01.md) |
| 선녀와 나무꾼 2부 — 돌아간 날개 | [제목·설명·태그](episodes/02_fairy_and_woodcutter_p02.md) |
| 구미호의 마지막 밤 — 단편 | [제목·설명·태그](episodes/03_gumiho_last_night.md) |
| 도깨비방망이 1부 — 개암 한 알 | [제목·설명·태그](episodes/04_dokkaebi_club_p01.md) |
| 도깨비방망이 2부 — 욕심쟁이가 따라 한 밤 | [제목·설명·태그](episodes/04_dokkaebi_club_p02.md) |
| 매화령 — 단편 | [제목·설명·태그](episodes/05_maehwa_spirit.md) |

[채널 소개·공통 키워드](CHANNELS.md) · [헤르메스 전달·파트 연결·검수](HERMES_HANDOFF.md) · [공식 근거](SOURCES.md) · [자동화용 원본 JSON](metadata.json)

## 어디에 붙이나요?

제목 입력란에는 기본 제목 또는 대체 제목 하나를 넣습니다. 설명 입력란에는 설명 블록 전체를 넣습니다. 맨 아래 해시태그가 이미 포함되어 있으므로 다시 붙이지 않습니다. **쉼표로 구분한 태그는 Studio의 태그 입력란에만 넣고 설명에 붙이지 않습니다.** 해시태그와 일반 태그는 별개의 입력입니다. [공식 안내 S2·S3](SOURCES.md)

영어판은 영어 제목·설명과 영문 태그를, 한국어판은 한국어 문구를 사용합니다. 영문은 한국어의 기계적 직역이 아니라 같은 사건을 전달하는 영어로 작성했습니다. 창작 단편인 구미호·매화령은 설명에서 창작임을 밝혔습니다. 매화령의 무덤과 1부 이후의 결말은 업로드 문구에서 먼저 공개하지 않습니다.

## 채널과 게시 상태

영문 채널명은 사용자가 선택한 **Dalbong Korean Tales**를 반영했습니다. 한국어 채널명, 두 채널의 실제 ID·핸들은 아직 확인되지 않아 JSON의 channel_id는 null입니다. 이름이나 언어만으로 업로드 대상을 추측하지 않습니다. 한국어 채널명은 공개 설명에 지어 넣지 않았습니다.

문구는 **제작안 기준 초안**입니다. 영상이 완성되면 실제 컷·길이·음성과 일치하는지 최종 검수한 뒤 사용합니다. 아직 없는 다음 편이 공개되었다고 쓰거나 가짜 채널·영상 링크를 넣지 않습니다. 이 요청은 GitHub에 문구를 준비하는 작업이며 YouTube 업로드·예약·채널 변경 승인이 아닙니다.

## 자동화와 검사

`metadata.json`이 단일 원본이고 episodes의 Markdown은 여기서 생성합니다. 내용 변경 후 다음 명령을 사용합니다. 모든 명령은 로컬 파일 작업이며 네트워크·Flow·TTS·유튜브 업로드를 호출하지 않습니다.

```sh
python tools/youtube_metadata.py --write-docs
python tools/youtube_metadata.py --check
python -m unittest discover -s tests -p 'test_youtube_metadata.py' -v
```

한 영상의 문구만 별도 폴더로 내보내는 예시입니다. `runs` 출력 폴더는 기존 파일을 덮어쓰지 않습니다.

```sh
python tools/youtube_metadata.py --episode 01_sun_and_moon_p01 --locale ko --out runs/metadata/01_sun_and_moon_p01/ko
python tools/youtube_metadata.py --episode 01_sun_and_moon_p01 --locale en --out runs/metadata/01_sun_and_moon_p01/en
```

내보내는 파일: title.txt, description.txt, tags.txt, hashtags.txt, metadata_draft.json. hashtags.txt는 설명에 이미 들어 있는 해시태그의 확인용이며 추가 합성하지 않습니다. API 업로드 요청문이 아니라 초안이므로 실제 게시에는 채널 ID·파일·사용자 승인·시청자층·AI 공개 여부 등의 별도 검수가 필요합니다.

제목 100자, API 설명 5,000 UTF-8 bytes, 태그 합산 500자를 검사합니다. 태그의 쉼표와 공백 있는 태그의 따옴표까지 계산합니다. 해시태그 3개는 이 패키지의 편집 선택이며 플랫폼의 최대 허용 개수라는 뜻은 아닙니다. 문구가 노출·조회수를 보장하는 것은 아닙니다. [공식 근거 S1–S3](SOURCES.md)
