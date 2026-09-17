# 05 · 매화령 — 돌아오지 못한 봄

**헤르메스 실행 지시:** AGENTS.md, docs/MASTER_PRODUCTION.md, docs/INK_EDITING_SPEC.md를 먼저 읽고 story_id=`05_maehwa_spirit` 한 편만 제작한다. 최종 세로 28초, 독립 4초 Flow 영상 7개, 편당 최대 50크레딧. 각 이미지/Flow 블록은 공통 화풍·고정 캐릭터와 함께 사용한다.

**구분: 한국풍 창작 설화.** 약속을 찾아온 선비와 세상을 떠난 여인의 매화나무 아래 재회는 새로 만든 이야기다. 실제 특정 사찰·지역에 전하는 전설처럼 설명하지 않는다. 첫 컷 작은 분류 표기와 영상 설명에 `한국풍 창작 설화`를 넣는다.

## 감독 방향

눈 속의 붉은 매화 → 약속을 찾아온 선비 → 기다리던 여인 → 손을 뻗음 → 꽃잎뿐 → 나무 아래 묘표 → 봄의 귀환. 6컷의 묘표가 여인의 정체를 알려주는 반전이다. 공포 점프스케어 대신 잠시 멈춘 음성과 빈자리를 쓴다.

색: 한지/먹/아주 옅은 청람 눈그늘, **붉은 매화와 여인의 매듭만** 절제된 진사색. 다른 색으로 화면을 꾸미지 않는다. 벚꽃/복숭아꽃의 화려한 분홍 숲으로 바꾸지 않는다. 매화는 오래된 굽은 가지에 붙은 작고 다섯 장인 꽃잎 형태를 미술적 기준으로 고정한다.

## 캐릭터와 공간 잠금

```text
Scholar: adult Korean man in his early thirties, slim face, black hair in a
neat topknot, plain ivory inner robe and muted blue-gray durumagi, simple
black headband, no ornate crown and no sword. His face remains identical.
Woman: adult Korean woman with a calm oval face, long black hair in a low
braid, ivory jeogori and ivory chima, one small muted-cinnabar knot at her
waist. No translucent naked body, no horror makeup, no glowing red eyes.
Setting: one old crooked red plum tree beside a small Korean wooden pavilion
in a snowy mountain grove. The main trunk bends toward screen right and
has one fork near its middle; preserve the same tree silhouette throughout.
A small weathered stone memorial stands near the roots, without legible writing.
```

## 연속 내레이션

> 눈 속에서, 붉은 매화가 피었다.
> 선비는 오래된 약속을 찾아왔다.
> 나무 아래, 기다리던 여인이 있었다.
> 봄이 오면, 돌아온다 하셨지요.
> 손을 뻗자, 꽃잎만 흩어졌다.
> 나무 아래엔, 그녀의 이름이 잠들어 있었다.
> 그가 울자, 겨울 숲에 봄이 번졌다.

4컷은 여인의 말이지만 **같은 내레이터가 인용하듯** 읽는다. 다른 음색의 TTS를 조각내지 않는다. 6컷의 의미가 충분히 들리도록 실제 길이를 보고 조정한다. 죽음을 공포 광고처럼 읽지 않는다.

## 컷 01 · 0~4초 · [0,120) · 겨울의 붉은 점

**화면:** 눈 쌓인 검은 매화 가지 접사. 꽃은 이미 반쯤 열려 있고 시작부터 작은 움직임. 빈 설산을 오래 보여주지 않는다. 강조어 `붉은 매화`.

**이미지 프롬프트**
```text
Macro view of a crooked black plum-tree twig carrying a small red plum
blossom already half open beneath a little snow. Five simple cinnabar petals,
a delicate dark center, dry-brushed branch and soft ivory hanji background.
A pale mountain-pavilion silhouette is barely visible far behind. Minimal,
poetic, crisp flower shape, no cherry-blossom clusters and no calligraphy.
```
**Flow 모션 프롬프트**
```text
The already half-open plum blossom gently opens a little further in one
small motion. A tiny piece of snow slips from the twig. Keep the petal count,
branch shape and ink texture stable. Locked macro camera, no rapid flowering
of the whole tree and no new branches appearing.
```
**타이밍/음향:** 0.2~2초 작게 열림 → 2~3.6초 눈 조각. 첫 음은 아주 작은 맑은 현음, 겨울 바람은 낮게. 붉은 꽃을 네온으로 발광시키지 않는다.

## 컷 02 · 4~8초 · [120,240) · 돌아온 선비

**화면:** 정자 쪽 좁은 길에서 선비가 이미 나무를 바라보고 멈춰 있다. 나무가 같은 방향으로 굽었는지 확인. 너무 긴 걷기·카메라 비행 없음.

**이미지 프롬프트**
```text
The approved scholar stands on a narrow snowy path, three-quarter back view,
facing the same crooked plum tree and a small wooden Korean pavilion. His
blue-gray outer robe is clear against the ivory snow. One old cloth bundle
rests at his side. The tree bends right with the same fork, layered ink mountains.
```
**Flow 모션 프롬프트**
```text
The scholar slowly raises his head toward the plum tree while remaining in
place. The hem of his blue-gray outer robe moves in a gentle wind and a few
snowflakes drift by. Preserve his silhouette and the tree structure. No long
walking sequence, no camera orbit and no new buildings.
```
**타이밍/음향:** 4.4~6.2초 시선 → 6.2~7.7초 도포 움직임. 도착을 나타내는 마지막 발자국 소리 한 번은 화면 동작에 맞을 때만 사용. 걷지 않으면 눈밟기 SFX도 넣지 않는다.

## 컷 03 · 8~12초 · [240,360) · 기다리던 여인

**화면:** 여인이 이미 나무 아래 서 있다. 갑자기 공중에서 뼈/몸이 생기는 변신 금지. 붉은 허리 매듭과 꽃의 색이 같다. 선비는 화면 가장자리의 뒷모습 일부.

**이미지 프롬프트**
```text
The approved fully clothed woman already stands beneath the same crooked red
plum tree, medium-wide view. Her ivory hanbok almost blends with the paper,
but her dark braid and single muted-cinnabar waist knot are readable. A small
edge of the scholar's blue-gray sleeve enters the far left. Quiet mist and
sparse red flowers; the stone memorial is not visible yet.
```
**Flow 모션 프롬프트**
```text
The woman slowly turns her face a few degrees toward the scholar at screen
left. Her braid end and red waist knot move gently in the same breeze.
Keep her body opaque and stable. A few existing blossoms tremble on the
branch. No apparition growth, no dissolving and no new people.
```
**타이밍/음향:** 8.2~10초 얼굴 방향 변화 → 10~11.7초 매듭. 음악 한 음을 부드럽게 얹되 정체를 벌써 공포음으로 누설하지 않는다.

## 컷 04 · 12~16초 · [360,480) · 오래된 약속

**화면:** 선비 왼쪽/여인 오른쪽의 안정된 측면 2인. 두 사람의 손은 아직 닿지 않음. 4컷에서 말하는 입 모양을 생성하지 않는다.

**이미지 프롬프트**
```text
Side-on two-person composition beneath the same plum tree: the scholar on
screen left, the ivory-clad woman on screen right. They face each other at
arm's length with a clear empty gap between them. Her cinnabar waist knot
matches the sparse flowers above. Stable hands lowered, no embrace, gentle
ink mist, reserved lower-middle area for captions.
```
**Flow 모션 프롬프트**
```text
The woman gives one very slight nod toward the scholar and the scholar
quietly lifts his gaze to meet hers. Their hands remain lowered and apart.
A few petals drift slowly through the empty gap. Keep both faces stable;
no lip sync, no touching, no hug and no costume changes.
```
**타이밍/음향:** 12.5~14초 작은 끄덕임 → 14~15.7초 꽃잎 사이 시선. 인용 문장 `돌아온다 하셨지요`가 묻히지 않도록 BGM 낮춤. 키스·멜로 OST 과장 없음.

## 컷 05 · 16~20초 · [480,600) · 닿지 않는 손

**화면:** 앞쪽 선비 소매와 이미 뻗은 손, 뒤쪽 여인의 옆모습. 손끝끼리 교차하지 않는다. Flow에는 작은 소매/꽃잎 움직임만, 사라짐은 로컬 편집.

**이미지 프롬프트**
```text
Close side view beneath the same tree. The scholar's blue-gray sleeve and
one already-extended open hand occupy the left foreground. The fully clothed
woman stands at a short distance on the right, her red waist knot readable,
not touching his hand. Keep an unobstructed ivory mist background behind her
for a later mask. A few red plum petals float between them.
```
**Flow 모션 프롬프트**
```text
The scholar extends his already-raised hand only a few centimeters toward
the woman and then stops. The woman's sleeve and a few plum petals move
softly in the wind while her face and body remain unchanged. No contact,
no body dissolution, no transformation into petals and no extra fingers.
```
**로컬 애니메이션:** 실제 영상 17초 전후부터 꽃잎을 좌하→우상으로 12~24개 이동. 품질 좋은 인물 마스크와 무료로 확보한 깨끗한 배경이 있으면 17.4~19.4초 사이 꽃잎 뒤에서 여인 opacity를 낮춘다. 얼굴이 깨지거나 배경이 지워지면 이 방식을 쓰지 않는다. 대안은 큰 꽃잎+한지색 안개가 여인을 완전히 가리는 동안 6컷의 빈 나무뿌리로 넘어가는 것으로, 생체 모핑 없이 `꽃잎만 남음`을 전달한다. 대안도 7컷/28초 유지.

**음향:** 손을 뻗는 순간 바람이 조금 강해졌다가 잦아듦. 마법 폭발, 유리 파열음 없음. 내레이션 `꽃잎만` 강조.

## 컷 06 · 20~24초 · [600,720) · 나무 아래 이름

**화면:** 같은 나무뿌리 옆 작은 낡은 묘표, 눈과 붉은 꽃잎 한 장. 묘표에 가짜 한자를 생성하지 않는다. 손글씨를 넣어야 이야기가 이해되는 구조로 만들지 않는다.

**이미지 프롬프트**
```text
Low close-up at the roots of the same crooked plum tree. A small weathered
stone memorial rests partly in snow, its surface worn and blank without
legible writing. One red plum petal lies on top and a trace of the woman's
cinnabar ribbon color appears only as a fallen small cloth knot beside it.
No human remains, no skulls, no horror symbols, quiet ivory mist.
```
**Flow 모션 프롬프트**
```text
A gentle breeze moves the single red petal a short distance across the top
of the stone. Fine snow slips softly along its edge. Keep the stone surface
blank and the tree roots fixed. Locked camera, no letters appearing,
no ghost emerging and no scene change.
```
**타이밍/음향:** 20~21.5초 묘표의 존재를 먼저 읽게 함 → 21.5~23.7초 꽃잎. `그녀의 이름이 잠들어 있었다`는 목소리로 설명한다. 반전 직전 0.2초 정도 음악만 줄이고 과도한 침묵으로 대본을 잘라내지 않는다.

## 컷 07 · 24~28초 · [720,840) · 늦게 온 봄

**화면:** 선비는 나무 아래 앉은 작은 뒷모습. 나무엔 이미 붉은 꽃 몇 송이가 더 있고 겨울 숲의 안개가 걷힘. 나무 전체를 다른 나무로 변형시키지 않는다.

**이미지 프롬프트**
```text
Wide Korean ink landscape of the same pavilion and crooked plum tree. The
scholar sits quietly beneath it, small back-view silhouette in blue-gray.
A few more red plum blossoms are already present on the existing branches,
while pale snow remains below. Gentle warm ivory dawn opens through the
mist. No woman present, no writing, no new buildings or crowded flowers.
```
**Flow 모션 프롬프트**
```text
A soft breeze moves the existing blossoms and the scholar's robe hem while
thin mist slowly clears around the tree. The seated scholar lowers his head
slightly. Preserve every main branch and the pavilion shape. No time-lapse
tree growth, no massive blooming burst and no return of the woman.
```
**로컬 애니메이션:** 24.5~26.4초 기존 가지 위치에만 작은 붉은 붓점/꽃 레이어 3~5개를 낮은 opacity로 드러내 봄을 은유. 새 가지를 그리거나 숲을 통째로 분홍색으로 칠하지 않는다. 26.5~28초 꽃잎 하나가 천천히 흐르며 여운. 실제 눈물 접사가 없더라도 고개/목소리로 슬픔을 전달한다.

**음향:** 마지막 문장 뒤 대금 같은 한 숨과 작은 현 잔향 방향. 적법한 실제 음원이 없으면 불명확한 OST 대신 단순한 직접 제작 앰비언스 사용.

## 6개 전환

| 경계 | 효과 / 길이 | 구체 구현 |
|---|---|---|
| f120 / 4초 | PETAL_VEIL / 18f | 첫 꽃의 붉은 꽃잎에서 시작, 우하→좌상 가림 뒤 선비의 길 |
| f240 / 8초 | FOG_VEIL / 18f | 정자의 안개가 좌→우로 덮이며 이미 서 있는 여인 등장 |
| f360 / 12초 | CLOTH_WIPE / 16f | 여인의 흰 소매를 닮은 곡선 아래→위, 안정된 2인 측면 구도로 |
| f480 / 16초 | PETAL_VEIL / 18f | 두 사람 사이 꽃잎이 좌하→우상, 손과 소매 접사로 연결 |
| f600 / 20초 | PETAL_VEIL / 18f | 5컷 사라짐을 마무리하는 큰 꽃잎+한지색 안개가 전면 가림, 빈 뿌리/묘표 |
| f720 / 24초 | MOON_WASH / 18f | 묘표 위 붉은 점 주변 (0.5W,0.6H)을 따뜻한 한지색으로 씻어 넓은 봄 풍경 |

## 추가 QA

매화나무의 주줄기와 정자는 전 컷 동일. 여인의 매듭/꽃잎 진사색 일치. 5컷에 사람이 녹는 신체 공포나 얼굴 찌그러짐이 없어야 한다. 6컷 묘표에 임의 글자/가짜 한자 없음. 7컷에 여인이 다시 나타나면 안 됨. 붉은 색이 화면 전체를 점유하지 않아야 한다. 6컷 반전이 무음 시청에서도 묘표+자막으로 이해되는지 확인. 창작 표기, 7개 원본, 실제 비용원장, 840프레임과 시청/청취 상태 확인.
