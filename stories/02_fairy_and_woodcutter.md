# 02 · 선녀와 나무꾼 — 돌아간 날개

**헤르메스 실행 지시:** AGENTS.md와 공통 제작/수묵 편집 규격을 읽고 story_id=`02_fairy_and_woodcutter` 한 편만 실행한다. 28초, 4초씩 7컷, Flow 최대 50크레딧. 이미지·Flow 블록에 공통 화풍/캐릭터 규칙을 결합한다.

구분: 전래설화의 선녀 귀환 대목 재해석. [원전 개요](https://encykorea.aks.ac.kr/Article/E0011342). 사슴의 보은과 천상 후일담은 생략한다. 전 컷 선녀는 옷을 입고 있으며, 날개옷은 평상복 위에 걸치는 외투 같은 옷으로 설계한다. 옷을 숨긴 행동을 사랑의 모범으로 표현하지 않는다.

## 감독 방향

첫 장면은 **궤짝 틈에 갇힌 빛과 날개옷**. 이어 옷을 숨긴 사연, 아이들과 보낸 시간, 되찾은 옷, 귀환으로 진행한다. 첫 컷은 상징적 후킹이며 2컷에서 같은 궤짝을 닫는 행동으로 연결한다. 선녀가 스스로 방향을 선택하는 시선을 중심에 둔다.

색: 먹과 아이보리, 날개옷의 옅은 비취색만 강조. 폭포·비단·운무의 흐름은 아래에서 위로 상승하는 방향을 유지한다. 실제 날개 달린 서양 요정으로 만들지 않는다.

## 캐릭터 고정

```text
Fairy: one adult Korean woman, serene oval face, black hair in a low braided
bun with a small jade pin, ivory jeogori and muted pale-jade chima, always
fully clothed. Her wing robe is a separate translucent pale-jade outer garment
with long silk ribbons, worn over her hanbok; no bird wings attached to her body.
Woodcutter: adult Korean man, simple dark topknot, rough gray-brown cotton
hanbok, straw sandals, no weapons shown, consistent rounded face.
Children: two small fully clothed figures in ivory and muted blue hanbok,
shown from behind or as simple silhouettes; no detailed toddler close-ups.
Props: one dark wooden chest with a small round brass latch; keep its design.
```

## 연속 내레이션

> 그녀의 하늘은, 궤짝에 갇혀 있었다.
> 나무꾼은 날개옷을 몰래 숨겼다.
> 아이들이 자라도, 하늘은 그리웠다.
> 마침내, 감춰 둔 옷이 나타났다.
> 선녀는 두 아이를 품에 안았다.
> 그리고, 제 하늘로 돌아갔다.
> 날개를 숨겨도, 마음은 가둘 수 없었다.

서정적이지만 늘어지지 않게. 마지막 문장은 이 작품의 새 해석. 한 화자/연속 음성, 오독과 실제 길이 검수 필수.

## 컷 01 · 0~4초 · [0,120) · 갇힌 하늘

**화면:** 궤짝 틈에서 옅은 비취 비단이 아주 조금 보임. 둥근 잠금쇠 중심을 다음 컷에도 유지. 강조어 `갇혀 있었다`.

**이미지 프롬프트**
```text
Macro close-up of a dark wooden Korean chest with a round brass latch at
center. Through a narrow existing gap beneath the lid, a small strip of
pale-jade silk is visible, lit softly from within. Ivory hanji background,
charcoal woodgrain, quiet mysterious composition. No hands or people yet.
```
**Flow 모션 프롬프트**
```text
The small silk strip flutters gently once through the narrow gap as a faint
breeze passes. Keep the chest and round latch completely fixed. A soft band
of light moves over the silk without becoming neon. Locked macro view,
no chest opening and no extra fabric appearing.
```
**내부 타이밍/음향:** 시작 0.3초 안에 비단이 움직임. 1~3초 틈의 빛 변화. 작은 천 마찰만; 음산한 비명 금지. f120에서 다음 컷의 잠금쇠에 매치컷.

## 컷 02 · 4~8초 · [120,240) · 숨긴 날개옷

**화면:** 동일 궤짝, 나무꾼의 몸과 한 손만 측면. 옷이 이미 안에 들어 있고 뚜껑을 한 번 닫음. 벗은 선녀나 목욕 장면은 넣지 않는다.

**이미지 프롬프트**
```text
Medium close-up of the same wooden chest in a humble Korean cottage. Its
lid is slightly open and the pale-jade outer wing robe is already folded
inside. The approved woodcutter stands at one side, one hand resting on the
lid, gray-brown sleeve visible. The round latch is aligned near center.
```
**Flow 모션 프롬프트**
```text
The woodcutter gently closes the chest lid in one restrained motion and
keeps his hand resting there. The last strip of silk retreats inside without
changing shape. Preserve the hand and hinge geometry. No locking mechanism
close-up, no extra action and no other character entering.
```
**내부 타이밍/음향:** 4.5~6.5초 닫힘, 6.5~7.6초 손의 멈춤. 1회의 나무 닫히는 소리를 낮게. 행동을 귀엽거나 낭만적인 코믹 장단으로 강조하지 않는다.

## 컷 03 · 8~12초 · [240,360) · 지상의 시간

**화면:** 처마 밑 선녀와 두 아이의 뒷모습. 선녀만 하늘을 바라본다. 여러 계절이 순식간에 변하는 모핑 대신 나뭇잎 두세 장으로 시간의 흔적을 암시.

**이미지 프롬프트**
```text
Back view of the approved fully clothed fairy sitting under a Korean cottage
eave with two small children beside her, one on each side. The children are
simple stable silhouettes. She looks toward an open pale sky beyond a
quiet courtyard. A few faded leaves rest on the wooden floor, pale-jade skirt.
```
**Flow 모션 프롬프트**
```text
The fairy slowly tilts her head upward toward the open sky while the two
children remain seated still. A few leaves drift across the distant yard and
her sleeve moves slightly. Keep three figures distinct, no aging morph,
no walking and no sudden change of season.
```
**내부 타이밍/음향:** 8.2~10초 시선 위로 → 10~11.7초 떨어지는 잎. 천천히 흐르는 대금 질감 음악 방향, 실제 허가된 음원만 사용.

## 컷 04 · 12~16초 · [360,480) · 되찾은 옷

**화면:** 같은 궤짝은 이미 열려 있다. 날개옷 한 끝이 선녀 손에서 살짝 들어 올려지는 단일 행동. 숨기기와 발견의 차이를 조명으로 표현.

**이미지 프롬프트**
```text
The same chest now stands open in soft dawn light. The fully clothed fairy
is seen from the side, one hand already holding the edge of the pale-jade
wing robe above the chest. Her face is calm but newly resolved. Simple
readable cloth folds, ivory space above, the same brass latch below.
```
**Flow 모션 프롬프트**
```text
She lifts the already-held edge of the wing robe slowly by a short distance.
The long silk ribbons unfold gently under gravity while her hand and body
remain stable. Soft light brightens the cloth. No dressing transformation,
no changing outfit and no extra hands.
```
**내부 타이밍/음향:** 12.3~14.8초 비단 상승 → 14.8~15.7초 빛. 비단 마찰음 한 번. 천이 얼굴을 지나가며 변형시키지 않음.

## 컷 05 · 16~20초 · [480,600) · 아이들과 함께

**화면:** 선녀는 날개옷을 이미 한복 위에 걸친 상태. 두 아이를 양옆으로 안은 단순한 뒷모습. 입는 과정·아이를 들어 올리는 복잡 동작은 생략.

**이미지 프롬프트**
```text
Back view of the fairy already wearing the pale-jade wing robe over her ivory
hanbok, standing at the edge of the courtyard. Her two children are already
held close, one at each side, as simple clear silhouettes. Long outer-robe
ribbons curve upward into the breeze. A pale path of cloud opens ahead.
```
**Flow 모션 프롬프트**
```text
The three figures gently lean together as the fairy's long outer ribbons
lift in the breeze. Keep the children securely in the same positions and
all bodies grounded for this shot. The camera drifts upward slightly;
no lifting of children, no extra limbs, no takeoff yet.
```
**내부 타이밍/음향:** 16~17.5초 한 덩어리 가족 형상 → 17.5~19.7초 비단 위로. BGM은 희망적으로 열되 승리의 팡파르 금지.

## 컷 06 · 20~24초 · [600,720) · 돌아간 하늘

**화면:** 먼 거리의 세 실루엣이 비단 구름 위로 작은 상승. 인물의 머리/다리는 세부 묘사하지 않는다. 세 존재가 하나로 합쳐지지 않도록 간격 고정.

**이미지 프롬프트**
```text
A distant back-view group of the same fairy and two children on a pale cloud
above layered Korean ink mountains. Their three silhouettes are distinct,
linked by the fairy's pale-jade outer robe. Wide ivory sky, upward-flowing
mist, the cottage tiny below. No feathered wings, angels or flying animals.
```
**Flow 모션 프롬프트**
```text
The cloud gently rises with the three fixed silhouettes as a single stable
group over a short distance. Silk ribbons trail below and mist parts slowly.
Keep all three figures separate and small. No spinning, no body morphing,
no flight across multiple locations and no new landscape.
```
**내부 타이밍/음향:** 실제 상승을 확인하고 20.5~23초에 서서히. 길이 부족한 결과를 초장거리 슬로모션으로 숨기지 않는다. 바람의 고음은 음성을 가리지 않게.

## 컷 07 · 24~28초 · [720,840) · 남겨진 빈자리

**화면:** 빈 궤짝과 열린 창. 나무꾼은 아주 작은 뒷모습으로 멀리 배치하거나 손/어깨만. 주제는 벌이 아니라 붙잡을 수 없는 마음.

**이미지 프롬프트**
```text
Quiet interior of the same cottage after departure. The wooden chest is
open and empty in the foreground, its round brass latch visible. An open
paper window frames an immense pale sky. The woodcutter is a small still
back-view silhouette far to the side. A plain ivory curtain hangs by the window.
```
**Flow 모션 프롬프트**
```text
The plain ivory curtain gently lifts toward the open window once and settles.
The chest stays empty and the distant man remains still. A soft cloud drifts
past the window. Slow minimal pullback, no returning fairy, no new objects
inside the chest and no dramatic crying.
```
**내부 타이밍/음향:** 24.2~26.5초 창 쪽으로 커튼 → 26.5~28초 여백. 끝말 `없었다` 이후 음악과 바람 잔향, 따로 엔딩 카드 없음.

## 6개 전환

| 경계 | 효과 / 길이 | 구체 구현 |
|---|---|---|
| f120 / 4초 | MATCH_CUT / 0f | 같은 둥근 잠금쇠를 (0.5W,0.52H)에 맞춰 접사→반신 구도 연결 |
| f240 / 8초 | WATER_RIPPLE / 16f | 잠금쇠 원에서 옅은 원형 파문, 한지색 가림 뒤 처마 아래 풍경 |
| f360 / 12초 | FOG_VEIL / 18f | 창 밖 여백의 안개가 좌→우로 덮이고 열린 궤짝 등장 |
| f480 / 16초 | CLOTH_WIPE / 16f | 들어 올린 비취 비단이 아래→위로 가림, 이미 입은 날개옷으로 연결 |
| f600 / 20초 | CLOTH_WIPE / 16f | 오른쪽 소매와 구름이 우하→좌상, 세 실루엣의 상승 장면을 드러냄 |
| f720 / 24초 | FOG_VEIL / 18f | 하늘 구름이 위→아래로 덮이고 빈 궤짝의 실내로, 대비는 부드럽게 |

## 추가 QA

전 컷 한복 착용, 아이는 정확히 두 명, 날개옷은 별도의 비단 외투, 서양식 날개/나비 요정 금지. 실루엣 3인이 뭉개지면 로컬 가림막으로 잠깐 감출 수 있는 수준인지 판단하고 실패는 기록한다. 1컷과 7컷의 궤짝/잠금쇠가 같아야 한다. 음성은 피해자의 귀환을 차분하게 전달하고 유괴 로맨스처럼 연출하지 않는다. 최종 840프레임과 비용원장 확인.
