# 03 · 구미호의 마지막 밤 / The Fox Spirit's Last Night

v2 · story_id=`03_gumiho_last_night` · 한국풍 창작 설화 / Original Korean-Inspired Tale.

공통 v2 문서 4개를 읽고 공용 Flow 7컷으로 KO/EN 두 편을 만든다. 각 28초/840프레임, 두 언어 합산 Flow 최대 50/예상 49. 등장인물 대사·속삭임·립싱크 없이 화면 밖 내레이션만. narration/03_gumiho_last_night.ko.txt와 .en.txt가 연속 낭독용 파일이다.

## 스토리 재설계

천 년의 기회가 구슬 하나에 담겼다는 규칙을 먼저 보여준다. 아이를 발견 → 망설임 → 구슬을 내줌 → 아이의 회복과 빛의 소멸을 같은 순간에 보여줌 → 꿈을 잃음 → 여우로 남은 존재의 인간적인 마음. 마지막 희생이 우연한 마법처럼 보이지 않게 원인과 대가를 연결한다.

이 작품의 새벽/천 년/한 번뿐인 구슬/아이 구원 규칙은 창작이다. 실제 지역 전설의 정본으로 소개하지 않는다. 변신은 얼굴/신체 모핑이 아니라 안개 가림 뒤 별도 여우 컷으로 표현한다.

## 캐릭터 잠금

```text
Human-form fox spirit: adult Korean woman, oval face, long black hair tied
low by one narrow pale-jade ribbon, ivory hanbok with blue-gray cuffs,
compassionate expression, no visible animal ears. Child: one child about
eight in an indigo coat and ivory scarf, no injury. Orb: one small pearl,
pale-jade mineral-pigment light, never multiple gems or neon. Fox form only
in shot seven: one slender white fox, black brush ear tips and the same
jade neck ribbon. One snowy Korean pine forest throughout.
```

먹·아이보리 눈·은청색·구슬/리본의 작은 비취색. 각 이미지에 공통 화풍과 참조를, 모션에 공통 Flow/NO_SPEECH를 결합한다. 꼬리 아홉 개는 생성모델에 맡기지 않고 후반 먹 그림자 9경로로 구현한다.

## 컷 01 · 0~4초 · f0~119 · 새벽의 기회

**KO:** 새벽이 오면, 이 여우는 사람이 될 수 있었다.
**EN:** At dawn, this fox spirit could finally become human.

**이미지 프롬프트**
```text
The approved woman stands alone among snowy pines, medium close-up. One
pale-jade pearl rests in her steady open palm at chest height. Her low jade
hair ribbon and ivory sleeve are clearly visible. A thin pale band of dawn
lies far behind the trees; restrained silver ink and spacious ivory snow.
```
**Flow 모션 프롬프트**
```text
She lowers her eyes toward the single pearl and takes one subtle breath.
Her hair ribbon moves lightly in the wind. Keep face, closed mouth, hand
and pearl stable. Snow drifts behind her. No transformation or new objects.
```
**편집·음향:** 0.2~2초 시선과 숨. 첫 컷에 여우 귀나 꼬리가 몸에서 돋아나지 않음. 하나의 낮고 맑은 음, 배경은 눈밭 바람. 내레이터가 `fox spirit`으로 정체를 설명.

## 컷 02 · 4~8초 · f120~239 · 한 번뿐인 구슬

**KO:** 천 년을 모은 구슬, 단 한 번의 기회였다.
**EN:** One pearl held a thousand years of waiting.

**이미지 프롬프트**
```text
Macro view of the same single pearl in her still palm. Ivory sleeve with
blue-gray cuff frames the lower edge. A faint crescent reflection rests on
the surface. Quiet pale-jade light, clear round pearl, no engraved words
or magic symbols, clean hanji background.
```
**Flow 모션 프롬프트**
```text
A small reflection moves over the pearl while the sleeve edge flutters.
Keep palm, fingers and pearl roundness unchanged. Locked macro shot,
no floating bead, no multiplication, no light beam or pulsating neon.
```
**편집·음향:** 4.3~6.5초 반사 이동. 구슬이 빛을 가졌음을 명확히 보여 5컷의 소멸과 대비. 숫자 카운터·천 년 역사 몽타주는 추가하지 않는다.

## 컷 03 · 8~12초 · f240~359 · 눈 속의 아이

**KO:** 그때 눈밭에서, 아이 하나가 숨을 잃어 갔다.
**EN:** Then she found a child freezing in the snow.

**이미지 프롬프트**
```text
One fully clothed child rests weakly against a pine in the same snowy grove,
eyes closed, indigo coat and ivory scarf. Non-graphic, no wounds. A little
snow lies on the scarf. Mid-shot with empty snow on one side and dark pine
trunk on the other, stable child proportions.
```
**Flow 모션 프롬프트**
```text
One faint breath gently moves the scarf, and a few snowflakes slip off it.
The child remains resting with eyes closed. Subtle camera drift closer,
no fall, convulsion, exaggerated pain or speech-like mouth movement.
```
**편집·음향:** 8.2~10.5초 스카프의 작은 호흡. 기절/위험은 목소리와 자세로만 전달, 죽음 장면/심전도/의료 설명은 없음. 낭독 아래 음악을 줄여 발견의 의미를 살림.

## 컷 04 · 12~16초 · f360~479 · 선택의 순간

**KO:** 여우는 망설이다, 구슬을 아이에게 내주었다.
**EN:** She hesitated, then gave the child her pearl.

**이미지 프롬프트**
```text
Simple side view of the woman kneeling beside the resting child. Her open
palm already holds the pearl just above the child's scarf. Both faces and
bodies stay separate, her sleeve drapes clearly, the pearl is the focal point.
No touching mouths, no swallowing, no medical instrument.
```
**Flow 모션 프롬프트**
```text
She pauses briefly, then lowers the already-extended palm a few centimeters
toward the scarf. The child remains still. Her sleeve follows softly.
Keep hand anatomy and pearl consistent. No complex transfer, no bright blast.
```
**편집·음향:** 12.3~13초 짧은 망설임, 13~15.2초 내려놓는 방향의 동작. 내레이션이 그 망설임을 과장된 한숨/대사로 대체하지 않음. 손 사이 전달/입에 넣기 없음.

## 컷 05 · 16~20초 · f480~599 · 대가가 보이는 순간

**KO:** 아이가 눈을 뜨자, 구슬의 마지막 빛이 꺼졌다.
**EN:** The child woke. The pearl's last light went out.

**이미지 프롬프트**
```text
The child rests more upright against the same pine, eyes still gently closed
before opening. The same pearl already lies on the ivory scarf; its base
surface is pale but not strongly glowing. The woman kneels beside the child,
mostly back-view. Leave clean snow behind her for a later shadow overlay.
```
**Flow 모션 프롬프트**
```text
The child slowly opens their eyes once and breathes gently. The woman stays
still with slight hair-ribbon movement. Keep the pearl fixed on the scarf.
No generated tails, no transformation, no bright flash and no speaking.
```
**편집·음향:** 실제 눈뜨는 시점(목표 17~18초)에 맞춰 후반의 구슬 glow를 10~16프레임 동안 낮춘다. Flow 시작은 무발광 구슬이므로 glow를 로컬에서 붙였다가 없앤다. 17.8~19.2초 여인 뒤 눈에 먹 꼬리 **9개 경로**를 드러냄. 양쪽 낭독의 `빛이 꺼졌다 / light went out`는 실제 소멸 부근에 정렬한다. 순간 섬광/폭발 없음.

## 컷 06 · 20~24초 · f600~719 · 사라진 꿈

**KO:** 여우가 천 년을 기다린 기회도 함께 사라졌다.
**EN:** So did her only chance to become human.

**이미지 프롬프트**
```text
Back view of the same woman on the snowy path, empty hand lowered beside
her ivory robe, jade hair ribbon clear. The now-awake child is a small
seated figure far behind. Pale dawn reaches the pine trunks. Clean snow
for the existing shadow motif, no body changes or new creatures.
```
**Flow 모션 프롬프트**
```text
She turns her head slightly away from the child and lets her empty hand
settle. Hair and ribbon move in the wind. The distant child remains still.
No walking cycle, vanishing body or transformation into an animal.
```
**편집·음향:** 20.5~22.4초 빈손과 돌아서는 고개. 5컷의 아홉 경로 그림자를 필요시 그대로 재사용. 천 년 설명을 새로 늘리지 말고 대가를 한 문장으로 마침. 후반 안개가 7컷으로 가림.

## 컷 07 · 24~28초 · f720~839 · 남은 마음

**KO:** 사람이 되진 못했다. 하지만 그 마음은 사람이었다.
**EN:** She stayed a fox. Her kindness was entirely human.

**이미지 프롬프트**
```text
One white fox already sits on the same snowy path in three-quarter rear
view, black brush ear tips and the same narrow jade ribbon at its neck.
One simple physical tail, clear snow for a separate nine-tail shadow.
The recovered child is small in the distance. Warm ivory dawn, no woman.
```
**Flow 모션 프롬프트**
```text
The fox slowly turns its head back toward the distant child once. Its ribbon
moves and snow drifts gently. Keep anatomy and the simple tail stable.
No human-to-fox morph, no tail growth, no extra animals or talking mouth.
```
**편집·음향:** 24.3~26.5초 돌아봄과 마지막 문장. 9개의 먹 그림자 경로는 고정, 27.2초 전 낭독을 마치고 눈발 여운. 울음 연기 대신 따뜻하고 담담한 narrator.

## 공용 전환

| 경계 | 종류 / 길이 | 구현 |
|---|---|---|
| f120 | MOON_WASH / 18f | 가슴 앞 구슬 (0.5W,0.5H)에서 부드럽게 가리고 접사 |
| f240 | FOG_VEIL / 18f | 은청색 눈안개 우→좌, 소나무 아래 아이 |
| f360 | INK_BLOOM / 18f | 나무줄기 먹에서 번져 두 인물 측면 |
| f480 | MOON_WASH / 18f | 손 위 구슬과 스카프 위 구슬 중심 (0.55W,0.58H) 연결 |
| f600 | DRY_BRUSH_WIPE / 12f | 꼬리 그림자 방향 좌하→우상, 빈손의 뒷모습 |
| f720 | FOG_VEIL / 18f | 안개 전면 가림 때 사람 컷에서 이미 앉은 여우 컷으로 |

## 추가 QA

구슬 1개/아이 1명, 같은 비취 리본, 눈뜨기와 구슬 빛 소멸의 인과, 아홉 꼬리 그림자의 경로 수, 몸 변형 없는 전환, 마지막 여우 정체 확인. 03의 구슬 규칙을 실제 전승/의학 사실로 설명하지 않는다. 두 언어에서 선택과 대가가 같고 동일한 공용 마스터를 사용하는지 확인.
