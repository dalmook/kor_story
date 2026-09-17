# 헤르메스 실행 명령 v2 — 내레이션 전용 / KO + EN

아래에서 **한 이야기 블록만** 붙여넣는다. 5편 전체를 동시에 생성하지 않는다. 각 블록은 공용 Flow 원본 7개로 한국어와 영어 완성본 두 개를 만드는 명령이다. 캐릭터 대사/인용 연기/립싱크는 없다.

## 01 해와 달이 된 오누이

```text
https://github.com/dalmook/kor_story main의 최신 v2를 읽어.
AGENTS.md, docs/MASTER_PRODUCTION.md, docs/BILINGUAL_NARRATION.md,
docs/INK_EDITING_SPEC.md, stories/01_sun_and_moon.md를 전부 읽고 01편만 제작해.

몽환적인 한국풍 수묵담채화, 7컷/28초다. 엄마 목소리와 발톱의 모순,
추격, 말 없는 기도, 두 종류의 동아줄, 해와 달이라는 인과를 유지해.
기도문을 아이 목소리로 읽거나 인물이 말하는 장면을 만들지 마.
너는 감독, Codex CLI는 공용 편집·두 언어 내레이션/자막·검수 담당이야.

narration/01_sun_and_moon.ko.txt와 .en.txt로 각각 한 명의 내레이터가
이야기를 들려주는 한국어판·영어판 두 개를 만들어.
7장 이미지를 먼저 검수하고 Flow는 공용으로만 7회 생성해.
실제 720p/4초/x1/7크레딧 확인 후 예상49, 두 언어 합산 최대50을 지켜.
영어판 때문에 다시7컷 생성하거나 Flow 번역/더빙을 호출하지 마.

같은 무음·무자막 picture_master.mp4에 각 언어 음성과 자막만 입혀.
두 파일 모두 28초/30fps/840프레임, 자막 타임코드는 음성별로 따로 만들어.
TTS 추가 비용·자동 재생성·유료 업스케일·업로드는 임의 실행하지 마.
기존 파일/환경을 보존하고 연동 없으면 준비물과 NEEDS_FLOW_INPUT을 남겨.
한 언어만 완성되면 완료가 아니라 PARTIAL_LOCALIZATION으로 보고해.
```

## 02 선녀와 나무꾼 — 돌아간 날개

```text
https://github.com/dalmook/kor_story main의 최신 v2를 읽어.
AGENTS.md, docs/MASTER_PRODUCTION.md, docs/BILINGUAL_NARRATION.md,
docs/INK_EDITING_SPEC.md, stories/02_fairy_and_woodcutter.md를 전부 읽고 02편만 제작해.

한지 수묵담채화로 감춘 날개옷→나무꾼의 방심→선녀와 두 아이의 귀환→
빈 궤짝을 7컷/28초로 보여줘. 날개옷이 우연히 나타나는 게 아니라
나무꾼이 직접 꺼내는 장면을 지켜. 대사·인용 연기·립싱크는 전부 빼.
너는 감독, Codex CLI는 공용 편집과 두 언어 출력 담당이야.

narration/02_fairy_and_woodcutter.ko.txt와 .en.txt를 사용해
한 화자의 연속 내레이션으로 KO/EN 완성본을 각각 만들어.
이미지7장 선검수, Flow 공용7컷만. 720p/4초/x1/7크레딧 실표시 확인,
최초49/두 언어 합산 최대50. 영어용 영상·이미지 재생성은 하지 마.
비단·물결·운무 전환은 공용 마스터에 한 번만 합성해.

같은 무음·무자막 마스터를 재사용하고 각 언어 음성/자막만 달리해.
28초/30fps/840프레임 유지, 영어가 길면 문장을 줄이지 영상을 늘리지 마.
실제 음성마다 별도 SRT를 만들고 두 언어를 각각 시청/청취 검수해.
추가 결제·자동 재시도·유료 업스케일·게시 작업 금지.
연동 없으면 준비물을 끝내고 NEEDS_FLOW_INPUT, 한 언어만 되면
PARTIAL_LOCALIZATION. 기존 로컬 변경과 인증은 보존해.
```

## 03 구미호의 마지막 밤

```text
https://github.com/dalmook/kor_story main의 최신 v2를 읽어.
AGENTS.md, docs/MASTER_PRODUCTION.md, docs/BILINGUAL_NARRATION.md,
docs/INK_EDITING_SPEC.md, stories/03_gumiho_last_night.md를 전부 읽고 03편만 제작해.

몽환적인 눈밭 수묵화. 천 년의 기회→아이 발견→구슬을 내주는 선택→
아이의 회복과 구슬 빛 소멸→여우로 남는 결말을 7컷/28초에 담아.
구슬 하나와 아홉 꼬리의 먹 그림자를 고정하고 신체 변형은 금지해.
한국풍 창작 설화 표시는 locale별로 유지해. 캐릭터 대사·속삭임·립싱크 없음.
너는 감독, Codex CLI는 공용 편집과 KO/EN 내레이션·자막 담당.

narration/03_gumiho_last_night.ko.txt와 .en.txt를 각각 연속 낭독해
두 버전을 만들어. Flow는 이미지7장 선검수 후 공용7개만 생성해.
720p/4초/x1/7크레딧 실표시 조건에서 최초49/두 언어 합산 최대50.
영어판을 위해 원장을 초기화하거나 다시 생성하지 마.

공용 무음·무자막 마스터1개로 *_ko.mp4와 *_en.mp4를 각각 출력해.
각28초/30fps/840프레임, 각각의 실제 음성으로 자막을 정렬해.
두 언어 모두 구슬 빛이 꺼지는 순간과 내레이션의 인과를 맞춰.
임의 추가 결제·유료 업스케일·재시도·업로드 금지, 기존 파일 보존.
연동 없으면 NEEDS_FLOW_INPUT, 한 언어만 있으면 PARTIAL_LOCALIZATION.
```

## 04 도깨비방망이 — 개암 한 알

```text
https://github.com/dalmook/kor_story main의 최신 v2를 읽어.
AGENTS.md, docs/MASTER_PRODUCTION.md, docs/BILINGUAL_NARRATION.md,
docs/INK_EDITING_SPEC.md, stories/04_dokkaebi_club.md를 전부 읽고 04편만 제작해.

버려진 보물의 미스터리→숨어 있던 나무꾼→개암 소리→집이 무너진다는
도깨비의 오해→도주→방망이 획득, 이 사건 하나만 7컷/28초로 완결해.
욕심쟁이 후일담은 넣지 마. 집은 실제로 무너지지 않아.
대사·역할극·립싱크·의성어 낭독은 빼고 개암 소리는 SFX로만 한 번 넣어.
화풍은 몽환적인 한국 수묵담채화, 너는 감독이고 Codex CLI는 편집 담당.

narration/04_dokkaebi_club.ko.txt와 .en.txt를 한 화자씩 연속 낭독해
한국어판과 영어판 두 개를 제작해. Flow 원본은 공용으로7개만.
이미지 선검수, 실제720p/4초/x1/7크레딧 확인 후 최초49/합산최대50.
영어판이라고 영상14개를 생성하거나 Flow 더빙을 요청하지 마.

공용 무음·무자막 마스터1개, 언어별 음성·자막2벌, 각28초/840프레임.
자막 시간은 각 음성에서 따로 만들고 반응컷/SFX의 시각 시점은 공용으로 고정해.
기존 작업 보존, 임의 결제·자동 재시도·업스케일·업로드 금지.
연동 부재는 준비파일+NEEDS_FLOW_INPUT, 한 언어만 완성은 PARTIAL_LOCALIZATION.
```

## 05 매화령 — 돌아오지 못한 봄

```text
https://github.com/dalmook/kor_story main의 최신 v2를 읽어.
AGENTS.md, docs/MASTER_PRODUCTION.md, docs/BILINGUAL_NARRATION.md,
docs/INK_EDITING_SPEC.md, stories/05_maehwa_spirit.md를 전부 읽고 05편만 제작해.

발자국 없는 여인→돌아온 선비→변하지 않은 모습→늦어진 봄의 약속→
꽃잎으로 사라짐→오래된 무덤→늦은 귀환의 결말을 7컷/28초로 만들어.
한지 수묵담채화에 붉은 매화만 절제해 채색해. 무덤은 6컷 전 공개하지 마.
등장인물 대사·약속의 인용 연기·속삭임·립싱크를 전부 없애.
한국풍 창작 설화로 표시하고 너는 감독, Codex CLI는 편집 담당이야.

narration/05_maehwa_spirit.ko.txt와 .en.txt를 각각 한 명의 내레이터가
연속 낭독하는 한국어판/영어판 두 개로 만들어.
이미지7장 선검수 후 Flow 공용7컷만 생성해.
720p/4초/x1/7크레딧 실제 표시 확인, 최초49/두 언어 합산최대50.
영어용 영상 재생성·Flow 번역/더빙·원장 초기화 금지.

공용 무음·무자막 picture_master.mp4 하나에 KO/EN 음성과 자막만 따로 입혀.
둘 다28초/30fps/840프레임. 언어별 실제 음성으로 SRT를 만들고
무덤/grave가 시각적 공개보다 먼저 읽히거나 표시되지 않게 검수해.
추가 결제·자동 재시도·유료 업스케일·유튜브 업로드는 하지 마.
기존 파일 보존. 연동 없으면 준비물+NEEDS_FLOW_INPUT, 한 언어만 되면
PARTIAL_LOCALIZATION으로 실제 상태를 보고해.
```
