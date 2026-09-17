# 04 · 도깨비방망이 — 개암 한 알

**헤르메스 실행 지시:** AGENTS.md와 공통 문서들을 읽고 story_id=`04_dokkaebi_club`만 제작한다. 최종 28초, 각 4초 Flow 7컷, 실제 최대 50크레딧. 프롬프트는 공통 화풍/동작/고정 캐릭터 블록과 결합한다.

구분: 전래설화 축약 각색. [원전 개요](https://encykorea.aks.ac.kr/Article/E0015530). 개암·부모를 먼저 생각함·놀라 도망간 도깨비·남긴 방망이·욕심쟁이의 모방이라는 요소를 유지한다. 매를 맞는 결말은 빈손 귀환으로 비폭력 축약한다.

## 감독 방향

첫 장면은 **작은 개암 열매**. 거대한 도깨비와 작은 소리의 대비를 살린다. 첫 컷의 한 알은 사건의 예고, 2컷부터 원인을 보여주는 구조. 공포가 아니라 어딘가 우스운 밤의 신비함. 4컷의 `딱`과 잠깐 비는 장단이 반전의 핵심이다.

색: 먹, 한지, 둔한 황토색. 금화는 번쩍이는 3D 폭포가 아니라 둥근 금빛 붓점. 도깨비는 이 작품만의 덩치 큰 먹 실루엣으로 고정한다. 도깨비의 형상은 다양하므로 특정 생김새를 유일한 한국 전통 원형이라고 주장하지 않는다.

## 캐릭터 고정

```text
Kind woodcutter: one young adult Korean man with a small tied topknot, gentle
rounded face, gray cotton jeogori with a small square patch on the left cuff,
ivory trousers, a simple straw pack, no hat. Keep the patch consistent.
Greedy neighbor: different adult Korean man, narrow face, neat topknot,
dark brown jeogori with an ochre collar, ivory trousers, no same cuff patch.
Two dokkaebi only: large original charcoal-brush silhouettes with tousled
hair, broad shoulders, rough simple Korean clothing and playful round eyes.
No red oni masks, no spiked metal clubs, no borrowed cartoon character design.
Magic club: one plain uneven wooden club, dark brown ink grain, cloth tie
near its handle. Hazelnuts are small brown round nuts, not acorns with caps.
```

## 연속 내레이션

> 도깨비를 쫓은 건, 개암 한 알이었다.
> 나무꾼은 부모님 몫부터 챙겼다.
> 밤이 되자, 빈집에 도깨비가 모였다.
> 딱! 개암 깨지는 소리에 모두 달아났다.
> 남겨진 방망이는 재물을 쏟아냈다.
> 욕심쟁이도 똑같이 따라 했지만.
> 돌아온 건, 금이 아니라 빈손이었다.

`딱!`은 한 화자가 자연스럽게 말하고 효과음은 작게 한 번 더 정렬한다. 문장마다 과장된 캐릭터 연기를 하지 않는다. 말끝 `했지만` 뒤 쉼으로 7컷의 대비를 만든다.

## 컷 01 · 0~4초 · [0,120) · 작디작은 주인공

**화면:** 오래된 나무판 위 이미 금이 간 개암 한 알. 얕은 그림자가 뒤에 큼직한 먹 실루엣을 암시하지만 도깨비 얼굴은 아직 없다.

**이미지 프롬프트**
```text
Extreme close-up of one small brown hazelnut with a fine existing crack,
resting on a rough old wooden floorboard. A tiny piece of shell sits beside
it. An indistinct large charcoal shadow falls in the distant background.
Minimal ivory negative space, dry-brush wood grain, muted ochre nut, no text.
```
**Flow 모션 프롬프트**
```text
The single hazelnut rocks gently once and settles on the board. A tiny shell
fragment slides a short distance. Keep the nut's shape and existing crack
stable. Locked macro camera, no magical transformation, no extra nuts and
no creature appearing in the foreground.
```
**타이밍/음향:** 0.2~1초 작은 흔들림으로 후킹, 1~3.6초 여운. 여기서는 큰 `딱`을 쓰지 않고 작은 나무/껍질 마찰만. 핵심 충격음은 4컷에 남긴다.

## 컷 02 · 4~8초 · [120,240) · 부모님 몫

**화면:** 착한 나무꾼의 손과 천주머니. 개암 3개 중 2개는 `부모 몫` 작은 보자기, 1개는 따로 남아 있는 구도. 글자로 부모 표시하지 않는다.

**이미지 프롬프트**
```text
Close-up of the kind woodcutter's gray patched cuff and one steady hand
beside a small open cloth pouch. Two brown hazelnuts already rest on an
ivory cloth square, and a third lies separately nearby. Gentle Korean forest
floor backdrop, pine needles, clear simple composition, no labels or writing.
```
**Flow 모션 프롬프트**
```text
His hand gently folds one edge of the small cloth over the two already-placed
nuts in a single short motion. The separate third nut stays still. Preserve
hand anatomy and nut count. A nearby pine needle moves in the breeze;
no complicated tying, no picking up multiple objects.
```
**타이밍/음향:** 4.3~6.4초 한 번 접음 → 6.4~7.8초 부모 몫이 따로 보임. 소박한 천 마찰음, 훈계조 과장 BGM 없음.

## 컷 03 · 8~12초 · [240,360) · 빈집의 잔치

**화면:** 빈집 안 도깨비 둘만, 한 도깨비가 방망이를 들고 다른 도깨비는 옆에서 지켜봄. 나무꾼은 구석의 작은 실루엣으로만 숨겨둠.

**이미지 프롬프트**
```text
Inside an abandoned Korean thatched house at night, exactly two large
charcoal-brush dokkaebi silhouettes stand around a low wooden floor area.
One already holds a plain wooden magic club slightly above the floor, the
other watches. A small hidden hint of the kind woodcutter's patched gray
sleeve appears behind a beam. Muted ochre lamp glow, no crowded party.
```
**Flow 모션 프롬프트**
```text
The club-holding dokkaebi taps the wooden floor once with a small controlled
motion. The other dokkaebi gives a slight shoulder bounce, staying in place.
Keep both silhouettes and the club stable. No dancing crowd, no multiplying
gold, no additional characters and no violent strike at a person.
```
**타이밍/음향:** 8.5~10초 방망이 한 타 → 10~11.7초 기대하는 어깨. 낮은 북 장단 1회. 금 생성은 다음 관련 컷에서만 표현해 사건을 늘리지 않음.

## 컷 04 · 12~16초 · [360,480) · 딱!

**화면:** 들보 뒤 착한 나무꾼의 측면, 개암이 이미 입술 가까이 있고 얼굴은 반신. 도깨비 둘은 반대편의 단순한 그림자로, 4초 동안 다른 장소로 도망가게 하지 않는다.

**이미지 프롬프트**
```text
Side view of the kind woodcutter hiding behind a thick wooden beam inside
the same house. One hand already holds a hazelnut at his lips; mouth detail
is minimal. Across the room, exactly two dokkaebi appear only as large soft
shadows on the paper wall. His patched gray cuff remains visible.
```
**Flow 모션 프롬프트**
```text
The man makes one tiny chewing motion with the nut already at his lips,
without moving his hand. In response, the two distant shadows jerk slightly
backward together and begin retreating toward the edge. Keep anatomy simple;
no close-up teeth, no huge mouth opening and no camera shake.
```
**로컬 연출:** 실제 깨무는 시점에 `딱`을 맞춘다(목표 13.0초 전후, 원본 우선). 이때 BGM 5~7프레임 살짝 낮춤. 들보 뒤 먼 그림자가 사라지는 부분은 기존 그림자 마스크를 약하게 걷는 방식으로 보조할 수 있다. 화면 전체를 흔들거나 만화 충격 글자를 그리지 않음.

**음향:** 개암 부러지는 짧은 딱 소리 1회 + 0.2초 장단의 빈자리. 도깨비 비명/욕설 없이 바람 같은 짧은 움직임만.

## 컷 05 · 16~20초 · [480,600) · 남겨진 방망이

**화면:** 동일 방망이가 바닥에 남아 있고 주변에 둥근 동전 몇 개. 도깨비는 없다. 떼로 금괴가 솟는 어려운 생성 대신 기존 소량 동전의 움직임과 로컬 금가루.

**이미지 프롬프트**
```text
The same plain wooden club lies abandoned on the floor of the now empty
house. A few small flat ochre-gold coin shapes already rest around its head.
The kind woodcutter's patched sleeve is barely visible at one edge, not
holding the club. Warm ivory space, handmade ink woodgrain, no gold mountains.
```
**Flow 모션 프롬프트**
```text
Two of the existing small coin shapes roll gently away from the still club
and settle. A loose cloth tie on the handle moves slightly. Keep all objects
flat and painterly. No coins bursting from a mouth, no endless gold fountain,
no multiplying people and no club changing shape.
```
**로컬 연출:** 17~18초 방망이 머리 주변 둔한 금빛 붓점 12개를 작은 호로 퍼뜨려 재물을 얻은 느낌을 보조. 클립 전체를 금색으로 덮지 않음. 한 번의 짧은 금속 잔향, 돈 효과음 반복 금지.

## 컷 06 · 20~24초 · [600,720) · 따라 한 욕심

**화면:** 다른 얼굴/황토 깃의 욕심쟁이가 같은 빈집 입구에 서서 개암을 입에 댄 상태. 실내에 두 도깨비의 고정된 눈만 암시. 인물 혼동 방지.

**이미지 프롬프트**
```text
The greedy neighbor with a narrow face and ochre collar stands in the doorway
of the same abandoned house, holding one hazelnut already near his lips.
He wears no patched cuff. In the dark interior, the same two dokkaebi are
partly visible as still broad silhouettes with calm round eyes. No violence.
```
**Flow 모션 프롬프트**
```text
The greedy neighbor makes one small chewing motion and then freezes in
expectation. The two distant dokkaebi shadows stay completely unmoved.
A loose edge of his collar flutters. Keep the scene stable, no attack,
no weapons raised and no comic facial distortion.
```
**타이밍/음향:** 20.6~22초 같은 작은 깨무는 동작 → 22~23.7초 반응 없는 고요. 4컷과 비슷한 소리지만 이번에는 장단의 해소가 오지 않음. 따라 했으나 결과가 다름을 소리로도 전달.

## 컷 07 · 24~28초 · [720,840) · 빈손

**화면:** 새벽 길, 욕심쟁이는 빈손을 내리고 서 있고 빈집 문은 뒤에. 폭력 흔적/멍/울음 희화화 없음. 옆에 남은 개암 껍질만 첫 컷과 대응.

**이미지 프롬프트**
```text
At pale dawn outside the same abandoned cottage, the greedy neighbor stands
with both empty hands lowered, his ochre collar clear. A single cracked
hazelnut shell lies beside his feet. The doorway is empty behind him and
mist opens onto a quiet Korean mountain path. No bruises, no injuries, no gold.
```
**Flow 모션 프롬프트**
```text
The neighbor slowly lowers his head once while keeping his empty hands
relaxed. A light breeze rolls the small shell fragment a little along the
path. Mist moves behind the doorway. No falling, no slapstick beating,
no newly appearing coins and no changing face.
```
**타이밍/음향:** 24.4~26.5초 고개 내려감 → 26.5~28초 껍질과 여백. 작은 나무 타악 1회 후 종료. 마지막엔 비웃는 군중 음성 없음.

## 6개 전환

| 경계 | 효과 / 길이 | 구체 구현 |
|---|---|---|
| f120 / 4초 | MATCH_CUT / 0f | 개암 원형 중심을 다음 천 위 개암 위치 (0.55W,0.55H)와 맞춤 |
| f240 / 8초 | DRY_BRUSH_WIPE / 12f | 접히는 천의 대각선 좌하→우상으로 한지 붓 가림, 밤의 빈집 |
| f360 / 12초 | INK_BLOOM / 18f | 집 들보 (0.25W,0.5H)의 검은 먹에서 번져 숨어 있는 나무꾼으로 |
| f480 / 16초 | DRY_BRUSH_WIPE / 12f | 도깨비가 물러난 방향 우→좌, 원래 그림자는 가리고 빈 방망이로 |
| f600 / 20초 | GOLD_DUST / 12f | 동전 지점의 황토 붓점+한지 밑칠, 욕심쟁이의 개암으로 연결 |
| f720 / 24초 | DRY_BRUSH_WIPE / 12f | 닫힌 듯한 어두운 문에서 아래→위, 새벽의 빈손으로 연결 |

## 추가 QA

개암을 도토리/밤/호두로 바꾸지 않는다. 도깨비는 둘, 방망이는 하나. 4컷에서는 놀란 반응, 6컷에서는 반응 없음이 대비되어야 한다. 착한 나무꾼의 왼쪽 소매 덧댐과 욕심쟁이의 황토 깃이 구별되어야 한다. 폭력 결말은 만들지 않는다. 금가루는 편집 합성이며 Flow 추가 생성 횟수가 아니다. 마지막 빈손이 실제로 보여야 한다. 840프레임, 원본 7개, 비용/검수 기록 필수.
