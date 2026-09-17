# 01 · 해와 달이 된 오누이 / The Sun and the Moon

v2 · story_id=`01_sun_and_moon` · 전래설화 각색 / Retold Korean Folktale.

AGENTS.md, MASTER_PRODUCTION.md, BILINGUAL_NARRATION.md, INK_EDITING_SPEC.md를 먼저 읽는다. **공용 Flow 7컷만 생성하고 한국어판·영어판을 모두 제작한다.** 각 28초/840프레임, KO+EN 합산 Flow 최대 50, 예상 49크레딧. 인물 대사와 립싱크 없음. 아래 KO/EN은 컷의 서사 대응표이며 언어별 한 연속 음성으로 읽는다. 바로 읽을 파일은 narration/01_sun_and_moon.ko.txt와 .en.txt.

## 스토리 재설계

엄마 목소리인데 발톱이 보이는 모순으로 즉시 시작한다. 정체 확인 → 도망 → 막다른 가지 → 하늘의 구원 → 호랑이만 실패 → 해와 달로 완결한다. 기도는 아이의 직접 대사가 아니라 내레이터의 간접 서술이다. 어머니 살해·도끼 추격·호랑이의 피는 생략한다. 해와 달의 성별은 특정하지 않는다. 원전 참고: https://encykorea.aks.ac.kr/Article/E0062663

## 공통 캐릭터 / 화풍

먹·아이보리·옅은 청람, 마지막 해에만 황토색. 한국풍 한지 수묵담채화. 각 이미지 앞에 공통 화풍 블록과 아래 참조를 붙인다. 각 모션 뒤에는 공통 Flow 블록과 NO_SPEECH를 붙인다.

```text
Boy: about ten, rounded Korean face, black hair in a small tied topknot,
muted indigo jeogori and ivory trousers. Girl: about seven, one black braid
with a muted red ribbon, ivory jeogori and blue-gray chima. Preserve faces,
height ratio and clothing. Tiger: one ochre-gray Korean folk-painting tiger
with bold black brush stripes, no clothes or monstrous anatomy. One Korean
thatched cottage with paper lattice doors; one tall crooked tree beside it.
```

## 컷 01 · 0~4초 · f0~119 · 목소리와 발톱

**KO:** 엄마 목소리였다. 그런데 손에는 발톱이 있었다.
**EN:** It sounded like Mother. But that hand had claws.

**이미지 프롬프트**
```text
Close-up from inside a Korean cottage. One tiger paw silhouette presses
against ivory paper on the right-center of a lattice door; three claw tips
are clearly visible in its shadow. A vertical wooden frame on the left,
diluted indigo night, empty lower-middle area. No human hand changing shape.
```
**Flow 모션 프롬프트**
```text
The single paw presses the paper inward once and pauses. The paper bows
slightly while the lattice remains rigid. Locked camera. Keep the paw and
claws stable; no door opening, no transformation, no additional subject.
```
**편집·음향:** 0.2초부터 발 그림자, 0.4~2.2초 누름. 첫 문장에 실제 엄마 목소리를 깔지 않는다. 내레이터만 말하고 문풍지/나무 마찰은 낮게 한 번. `발톱 / claws` 자막을 실제 낭독에 맞춘다.

## 컷 02 · 4~8초 · f120~239 · 탈출

**KO:** 호랑이였다. 오누이는 뒷문으로 달아났다.
**EN:** A tiger. The children slipped out the back.

**이미지 프롬프트**
```text
The approved siblings at an already-open rear doorway of the same cottage,
three-quarter back view. The boy stands just across the threshold and the
girl holds his sleeve behind him. Snow-free yard and the tall tree outside.
A broad tiger shadow remains far away at the opposite paper door.
```
**Flow 모션 프롬프트**
```text
The two children take one small coordinated step through the open rear door,
keeping their sleeve connection and positions stable. The girl's ribbon
trails slightly. Fixed side camera; no long running cycle, no door-breaking,
no tiger entering this doorway and no extra limbs.
```
**편집·음향:** 4.4~6.5초 문턱을 넘는 한 걸음으로 도망을 암시하고 장거리 달리기는 다음 컷 생략으로 처리. 발소리는 실제 발 움직임에만 정렬. 7.7초부터 나뭇결 방향의 전환.

## 컷 03 · 8~12초 · f240~359 · 따라온 호랑이

**KO:** 나무 꼭대기까지 올랐지만, 호랑이도 따라왔다.
**EN:** They climbed a tree. The tiger followed.

**이미지 프롬프트**
```text
Low-angle view of the siblings already crouched on a broad high tree branch.
The trunk fills the left third. Far below, one small tiger has its front
paws resting at the trunk base. Vast ivory sky above, dark ink below.
Clear separation between the children and tiger, no contact or weapons.
```
**Flow 모션 프롬프트**
```text
The distant tiger shifts its weight against the trunk once. The branch
shivers gently and the children brace in place, their grips unchanged.
A very slight upward camera drift. No detailed climbing, no jumping or attack.
```
**편집·음향:** 8~9.5초 높은 위치 확인, 9.5~11.4초 아래 호랑이의 움직임과 가지 떨림. 반복 포효 없이 낮은 나무 울림. 위쪽 여백으로 다음 컷 시선 유도.

## 컷 04 · 12~16초 · f360~479 · 말 없는 기도

**KO:** 막다른 가지에서, 아이들은 하늘에 빌었다.
**EN:** Trapped above, they pleaded with the sky.

**이미지 프롬프트**
```text
Close side view of the girl on the same branch, hands already clasped at
her chest, lips gently closed. The boy's indigo shoulder is visible beside
her. Her gaze points toward broad empty ivory sky. Stable fingers, red braid
ribbon, quiet moonlight, no lettering or divine figure.
```
**Flow 모션 프롬프트**
```text
The girl slowly raises her gaze and chin slightly while keeping her hands
and closed mouth still. Her ribbon rises gently in the breeze. One thin
cloud drifts above. No speech-like mouth motion, no hand gesture sequence.
```
**편집·음향:** 12.3~14.2초 고개, 이후 고요. 내레이터가 설명할 뿐 아이 목소리·기도문·합창 없음. 15.5초 바람을 다음 컷으로 이어준다.

## 컷 05 · 16~20초 · f480~599 · 구원의 줄

**KO:** 그러자 동아줄이 내려와 둘을 끌어 올렸다.
**EN:** A rope descended and lifted them to safety.

**이미지 프롬프트**
```text
One strong pale braided rope descends vertically from ivory clouds. The
siblings already hold its lower part just above their tree branch, seen
as small back-view silhouettes with their approved clothing colors. Taut
intact rope, clear two-person shapes, wide sky, no angels or extra rope.
```
**Flow 모션 프롬프트**
```text
The taut rope lifts the two fixed silhouettes upward a short distance
together. Their grips and spacing remain unchanged. Clouds part gently
behind them; sleeves trail downward. No twisting bodies or transformation.
```
**편집·음향:** 16.2~17.0초 줄과 아이를 알아볼 여유, 17~19.5초 짧은 상승. 상승 없는 결과는 FAIL이지 이미지 줌 대체가 아니다. 부드러운 바람과 얇은 현음.

## 컷 06 · 20~24초 · f600~719 · 다른 줄

**KO:** 뒤쫓던 호랑이의 줄만, 썩어 끊어졌다.
**EN:** But the tiger's rope was rotten. It snapped.

**이미지 프롬프트**
```text
Close-up of a different dark frayed rope at center against ivory clouds.
Rotten fibers are nearly separated. One tiger paw holds the lower end at
the bottom edge, the animal otherwise out of frame. No falling body, no
blood, no impact scene. Align rope center with the preceding shot.
```
**Flow 모션 프롬프트**
```text
The rotten strands separate once. The lower rope end and partial paw slip
down out of frame; the upper end sways gently. Locked camera, one small
clear event. No visible fall, no new rope or additional animal.
```
**편집·음향:** 끊김 목표 21.8~22.6초, 실제 결과 우선. 영어 `It snapped`와 한국어 `끊어졌다` 및 SFX를 그 사건 근처로 각각 정렬. 비명·낙하 충돌음 없음.

## 컷 07 · 24~28초 · f720~839 · 밤을 밝히는 둘

**KO:** 밤을 피해 오른 오누이는, 해와 달이 되었다.
**EN:** The children escaped the night as sun and moon.

**이미지 프롬프트**
```text
Wide Korean ink mountains beneath an immense ivory sky. Two celestial discs
are already present, a muted ochre sun upper-left and pale blue-gray moon
upper-right. Tiny cottage below, flowing cloud bands. No faces inside the
discs and no human bodies morphing into celestial objects.
```
**Flow 모션 프롬프트**
```text
A cloud band slowly passes between the two fixed discs. Diluted ink mist
moves over the ridges; a minimal pullback opens the sky. Keep both discs
round and distinct, no new objects or rapid day-to-night transition.
```
**편집·음향:** 24~25초 둘을 동시에 인지. 25~26.5초 낮은 강도의 달빛 씻김으로 강조하고 27.2초 전 낭독 마감, 마지막 구름 움직임 유지. 별도 엔딩 카드 없음.

## 공용 전환 6개 / KO·EN 동일

| 경계 | 종류 / 길이 | 위치와 방향 |
|---|---|---|
| f120 | INK_BLOOM / 18f | 발 그림자 (0.66W,0.40H)에서 전면 먹 번짐 후 뒷문 |
| f240 | DRY_BRUSH_WIPE / 12f | 문틀을 따라 아래→위, 다음 나무줄기 x=0.3W에 맞춤 |
| f360 | FOG_VEIL / 18f | 가지의 안개가 아래→위로 덮이며 누이 접사 |
| f480 | MOON_WASH / 18f | 시선 끝 (0.5W,0.25H)에서 부드러운 한지색 가림 |
| f600 | MATCH_CUT / 0f | 새 줄/썩은 줄 x=0.5W와 굵기를 맞춘 즉시 컷 |
| f720 | MOON_WASH / 18f | 끊어진 줄 뒤 하늘을 씻어 해와 달, 섬광 없음 |

전환을 겹쳐 시간을 빼지 않는다. 실제 원본 7개, 두 언어 동일 마스터, 840프레임, 얼굴/옷 일관성, 새 줄과 썩은 줄 구분, 두 원반, 각 언어 발화와 반전 시점을 검수한다.
