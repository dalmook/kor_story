# Codex 실행 명령 모음 — v4 / 8편 각각 복사·붙여넣기

`episode_id만 바꾸세요`라는 축약 지시를 폐기합니다. 아래 블록 중 **제작할 한 편의 블록 하나만** Codex에 전달합니다. 각 명령은 공통 v4 설계, 해당 episode 문서, catalog 카드, 기존 자산 재사용, 33초 구조, KO/EN 두 버전, 자막·전환·음성·QA까지 명시합니다.

## 모든 명령에 공통인 강제 조건

- Hermes에 넘기지 말고 Codex가 직접 수행.
- 기존 사용자 파일·미커밋 변경·깨끗한 이미지/Flow 원본을 먼저 찾아 보존·재사용.
- 오프닝 원화 2초 + Flow 본문 7×4초 = 28초 + 엔딩/다음편 예고 원화 3초 = **총 33초 / 30fps / 990프레임**.
- 오프닝·엔딩 원화는 로컬 미세 모션만. Flow 비용은 본문7개만.
- 실제 UI가 720p/4초/x1/7크레딧일 때 신규7개 예상49/최대50. 첫 신규1개를 실제 확인 후 나머지 진행. 자동 유료 재시도 금지.
- 같은 시각 마스터로 KO/EN 2개. 언어별 한 명의 자연스러운 narrator, 직접 대사·립싱크 없음.
- 1080×1920 기준 제목 KO108px/EN92px, 자막 KO72px/EN68px, 자막 최소64px. 자막 x96..924/y1296..1472, 최대2줄, 문장 단위. 가라오케·단어별 점멸 금지.
- 검은 먹덩어리/삼각형/다각형 wipe/전면 베이지·백색 가림/플래시/속도램프 금지. 기본 cut과 문서에서 허용한 8f dissolve만.
- 내레이션이 빠르면 전체 배속 금지. 원고를 줄이고 호흡을 수정해 다시 음성을 생성. 실제 속도로 청취 검수.
- 허가된 BGM/SFX 또는 직접 만든 앰비언스를 사용하고 목소리를 가리지 않게 믹스. 미확인 OST 사용 금지.
- Flow 전에 원화·실제 폰트·자막·전환 미리보기를 검수. 준비 파일만 만들고 완료라고 보고하지 않음.
- 유튜브 업로드/예약·다음편 자동 제작·추가 결제 금지.

---

## 01-1 해와 달이 된 오누이 — 문밖의 엄마

```text
https://github.com/dalmook/kor_story 최신 main을 읽어.
AGENTS.md, START_CODEX.md, docs/CODEX_WORKFLOW_V4.md,
docs/DESIGN_BIBLE_V4.md, docs/VIDEO_AUDIT_V4.md, docs/RESEARCH_V4.md,
episodes/01_sun_and_moon_p01.md, stories/01_sun_and_moon.md,
production/catalog_v4.json, production/director_v4.json,
production/01_sun_and_moon_p01_v4.json을 전부 읽어.

실행 대상은 01_sun_and_moon_p01 하나다. 위 공통 강제 조건을 모두 지켜.
문밖의 엄마 목소리→발톱 발견→뒷문 탈출→나무 피신→호랑이가 올려다보는
작은 결말까지 제작해. 동아줄·해와 달 결말은 본문에 넣지 마.

production/01_sun_and_moon_p01_v4.json의 7컷별 이미지·Flow·자막 줄바꿈·
목표 발화창·음향·편집 지시를 우선한다. 마지막 3초는 catalog의 2부예고 원화를
사용하되 구출/썩은줄/해와달을 스포일러하지 마.

먼저 기존 clean Flow 원본7개를 찾고 재사용 가능성을 검수해. 없거나 부적합한
컷만 생성해. 원화9장→레이아웃 사전검수→필요 Flow→KO/EN 연속음성→편집→
실제 시청/청취 QA까지 끝내. 두MP4, master, 원화9장, 원본7개, 두WAV/SRT,
실지출·자산출처·QA를 남겨. 다른 episode와 YouTube 업로드는 하지 마.
```

## 01-2 해와 달이 된 오누이 — 하늘에서 내려온 동아줄

```text
https://github.com/dalmook/kor_story 최신 main을 읽어.
AGENTS.md, START_CODEX.md, docs/CODEX_WORKFLOW_V4.md,
docs/DESIGN_BIBLE_V4.md, docs/VIDEO_AUDIT_V4.md, docs/RESEARCH_V4.md,
episodes/01_sun_and_moon_p02.md, stories/01_sun_and_moon.md,
production/catalog_v4.json, production/director_v4.json,
production/01_sun_and_moon_p02_v4.json을 전부 읽어.

실행 대상은 01_sun_and_moon_p02 하나다. 위 공통 강제 조건을 모두 지켜.
1부와 같은 아이들·호랑이·나무·달·바람방향을 유지해. 첫 장면은 같은 밤
나무 위 위기에서 바로 시작하고, 1부 영상을 재방송하지 마.

production/01_sun_and_moon_p02_v4.json의 7컷별 원화·Flow 동작·자막 줄바꿈·
목표 발화창·음향·편집 지시를 우선해. 구조는 호랑이의 감시→흔들리는 가지→
말없는 기도→새 동아줄→아이들의 상승→호랑이의 썩은 줄→해와 달 결말이다.
새 동아줄과 썩은 줄은 색·섬유 상태가 명확히 달라야 한다.

오프닝 2초에는 구출 결과/해와달을 미리 보이지 마. 본문 7컷은 실제 움직임을
유지하고, 사람 몸이 해·달로 변형되는 모핑은 금지해. 마지막 3초는 catalog의
완결 원화와 '이야기 끝/THE END'만 사용하고 3부 예고나 CTA를 만들지 마.

먼저 1부의 character refs/part_end와 기존 clean 원본을 확인하고 호환되는 자산만
재사용해. 필요한 원화/Flow만 새로 생성해. KO/EN 음성은 정상속도로 실제 들어보고
빠르면 원고를 압축해 다시 읽혀. 두MP4/master/원화9장/원본7개/두WAV/SRT/
실지출·출처·QA를 남기고 다른 episode와 YouTube 업로드는 하지 마.
```

## 02-1 선녀와 나무꾼 — 훔친 날개옷

```text
https://github.com/dalmook/kor_story 최신 main을 읽어.
AGENTS.md와 v4 공통 문서, episodes/02_fairy_and_woodcutter_p01.md,
stories/02_fairy_and_woodcutter.md, production/catalog_v4.json,
production/director_v4.json을 전부 읽어.
실행 대상은 02_fairy_and_woodcutter_p01 하나다. 공통 강제 조건을 모두 지켜.

날개옷이 사라짐→나무꾼이 감춤→다른 선녀들의 귀환→혼자 남음→나무꾼 등장→
산을 내려감→궤짝 속 귀환수단의 작은 결말로 33초를 완성해.
선녀는 전 컷 완전히 옷을 입고, 도난을 로맨틱한 성공담처럼 연출하지 마.
오프닝은 catalog의 빈 바위/비취 리본 원화, 마지막3초는 궤짝 속 비단으로
2부만 예고하고 아이들/귀환 결과는 스포일러하지 마.

기존 clean 자산을 우선 재사용하고, 필요한 원화9장/Flow7개만 만든 뒤 KO/EN,
큰 문장자막, 절제된 cut/dissolve, BGM/SFX와 실제 청취/시청QA까지 완료해.
다음편 자동제작과 업로드는 하지 마.
```

## 02-2 선녀와 나무꾼 — 돌아간 날개

```text
https://github.com/dalmook/kor_story 최신 main을 읽어.
AGENTS.md와 v4 공통 문서, episodes/02_fairy_and_woodcutter_p02.md,
stories/02_fairy_and_woodcutter.md, production/catalog_v4.json,
production/director_v4.json을 전부 읽어.
실행 대상은 02_fairy_and_woodcutter_p02 하나다. 공통 강제 조건을 모두 지켜.

1부의 같은 선녀·나무꾼·비취핀·날개옷·궤짝 흠집을 유지해.
세월/아이둘→하늘을 보는 선녀→나무꾼이 숨긴 옷을 꺼냄→되찾은 날개옷→
아이들과 함께함→귀환→빈 궤짝으로 끝내. 입는 과정·아이를 들어 올리는 복잡한
신체동작은 컷사이 생략하고 안정된 시작자세에서 작은 움직임만 생성해.
오프닝은 catalog의 선녀+아이둘+궤짝, 마지막3초는 빈 궤짝의 완결 원화.
3부 예고는 만들지 마.

같은 파트의 KO/EN은 동일 visual master를 사용하고 실제 음성 속도·자막 가독성을
검수해. 기존자산 우선, 필요한 Flow만 생성, 자동재시도/업로드 금지.
```

## 03 구미호의 마지막 밤 — 단편

```text
https://github.com/dalmook/kor_story 최신 main을 읽어.
AGENTS.md와 v4 공통 문서, stories/03_gumiho_last_night.md,
production/catalog_v4.json, production/director_v4.json을 읽어.
실행 대상은 03_gumiho_last_night 하나다. 공통 강제 조건을 모두 지켜.

천년의 기회→구슬→눈밭의 아이→선택→아이의 회복과 구슬빛 소멸→기회상실→
여우로 남는 결말을 유지해. 아홉 꼬리는 신체 생성이 아니라 기존 로컬 먹 그림자
9경로로 보장하고, 몸이 여우로 뒤틀리는 모핑은 하지 마.
오프닝은 catalog의 눈숲+구슬, 마지막3초는 흰 여우와 안전한 아이의 완결 원화.
새 속편은 만들지 마. KO/EN 모두 창작설화 표시를 유지하고 실제 음성을 들어 검수해.
```

## 04-1 도깨비방망이 — 개암 한 알

```text
https://github.com/dalmook/kor_story 최신 main을 읽어.
AGENTS.md와 v4 공통 문서, episodes/04_dokkaebi_club_p01.md,
stories/04_dokkaebi_club.md, production/catalog_v4.json,
production/director_v4.json을 읽어.
실행 대상은 04_dokkaebi_club_p01 하나다. 공통 강제 조건을 모두 지켜.

부모몫 개암→빈집→도깨비둘→방망이 마법→숨은 나무꾼의 개암소리→도깨비도주→
방망이 획득의 작은 결말로 제작해. 개암 깨짐은 narrator의 '딱' 연기가 아니라
SFX1회. 도깨비 대사·폭력·오니 디자인 금지. 황토빛 금가루는 로컬 보조효과로
절제해. 마지막3초는 욕심쟁이 2부 질문만 예고하고 실패결말은 보이지 마.
```

## 04-2 도깨비방망이 — 욕심쟁이가 따라 한 밤

```text
https://github.com/dalmook/kor_story 최신 main을 읽어.
AGENTS.md와 v4 공통 문서, episodes/04_dokkaebi_club_p02.md,
stories/04_dokkaebi_club.md, production/catalog_v4.json,
production/director_v4.json을 읽어.
실행 대상은 04_dokkaebi_club_p02 하나다. 공통 강제 조건을 모두 지켜.

욕심쟁이의 탐욕→개암만 있으면 된다는 착각→전부 자기몫→같은 빈집→같은 소리→
도깨비가 도망가지 않음→빈손퇴장으로 완결해. 착한 나무꾼과 얼굴/옷을 구분하고,
1부 뒤 방망이는 나무꾼 소유라 도깨비집에 다시 나타나면 FAIL이야.
폭행·멍·코믹 추락 없이 거절/퇴장으로 끝내. 마지막3초는 빈손의 완결 원화,
3부 예고 없음. 같은 개암 SFX의 시점은 1부와 비슷하되 반응은 정반대로 보이게 해.
```

## 05 매화령 — 돌아오지 못한 봄

```text
https://github.com/dalmook/kor_story 최신 main을 읽어.
AGENTS.md와 v4 공통 문서, stories/05_maehwa_spirit.md,
production/catalog_v4.json, production/director_v4.json을 읽어.
실행 대상은 05_maehwa_spirit 하나다. 공통 강제 조건을 모두 지켜.

발자국없는 여인→돌아온 선비→변하지 않은 모습→늦어진 약속→닿지않는 손→
꽃잎 뒤 무덤의 반전→늦은 귀환의 결말을 유지해. 무덤/grave를 해당 공개컷 전에
음성·통문장 자막·제목으로 누설하지 마. 여인 신체를 꽃잎으로 녹이는 AI 모핑 대신
꽃잎 가림막+검수된 마스크/clean plate로 처리해.
오프닝은 발자국 없는 눈과 붉은 매화, 마지막3초는 홀로 남은 선비와 한 줄의
발자국 원화. 속편을 만들지 마. KO/EN 창작설화 표시와 실제 청취QA를 유지해.
```

## 완료 보고 규칙

각 명령 실행 후 `실제 생성/재사용 Flow 수`, `실제 크레딧`, `KO/EN 음성 실제 길이`, `최종 프레임 수`, `실제 시청·청취 여부`, `남은 차단요인`을 짧게 보고합니다. 프롬프트 생성·prepare·자동검사만 끝낸 상태를 영상 제작 완료라고 쓰지 않습니다.
