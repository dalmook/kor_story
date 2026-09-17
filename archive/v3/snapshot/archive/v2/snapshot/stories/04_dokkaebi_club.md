# 04 · 도깨비방망이 — 개암 한 알 / The Hazelnut and the Magic Club

v2 · story_id=`04_dokkaebi_club` · 전래설화 일부 각색 / Retold Korean Folktale.

공통 v2 문서 4개를 읽고 공용 Flow 7컷으로 KO/EN 두 편을 만든다. 각 28초/840프레임, 두 언어 합산 최대 50/예상 49크레딧. narrator 외 음성/도깨비 대사/립싱크 없음. narration/04_dokkaebi_club.ko.txt와 .en.txt를 각각 하나의 연속 음성으로 읽는다.

## 스토리 재설계

v1의 부모님 몫과 욕심쟁이 모방을 모두 넣으려던 구성을 줄였다. **이번 28초는 첫 나무꾼이 방망이를 얻는 사건 하나만 완결**한다. 버려진 보물의 미스터리 → 숨은 나무꾼 → 도깨비의 재물 → 개암 소리 → 집이 무너진다는 오해 → 도주 → 사소한 물건이 큰 존재를 이기는 반전.

첫 컷은 결과를 미리 보여주는 장면이며 2컷부터 그날 밤으로 돌아간다. `집이 무너지는 줄 알았다`는 소리와 도주를 이해시키기 위해 이 각색에서 택한 설명이다. 원전의 유일한 정본 문구로 제시하지 않는다. 원전의 개암 소리/도깨비 도주/남긴 방망이를 참고했다: https://encykorea.aks.ac.kr/Article/E0015530 . 욕심쟁이 후일담은 이번 편에 넣거나 자동으로 추가 생성하지 않는다.

## 캐릭터 잠금

```text
One young adult Korean woodcutter, kind rounded face, black hair in a small
tied topknot, gray cotton jeogori with a square patch on the left cuff,
ivory trousers. Exactly two dokkaebi: original large charcoal-brush figures,
tousled hair, broad shoulders, simple Korean clothing, round expressive eyes.
No red oni masks, borrowed cartoon design or spiked metal club. One plain
wooden magic club with a cloth tie. One small brown hazelnut, not an acorn.
Same abandoned Korean cottage and wooden beams in all interior shots.
```

먹·한지·둔한 황토색 담채. 도깨비는 이 작품의 창작 시각 디자인이지 한국 도깨비의 유일한 전통 형상이라고 주장하지 않는다. 이미지/모션에 공통 화풍과 NO_SPEECH 결합.

## 컷 01 · 0~4초 · f0~119 · 버리고 간 보물

**KO:** 도깨비들이 보물을 버리고 달아났다. 범인은 따로 있었다.
**EN:** The goblins fled, leaving their treasure. Something had terrified them.

**이미지 프롬프트**
```text
Aftermath inside an empty abandoned Korean cottage. One wooden magic club
and a few dull ochre coins lie on the floor, an open door and drifting dust
behind them. No people visible. The club's cloth tie and central floorboard
are clear. Do not show the hazelnut yet; preserve the mystery.
```
**Flow 모션 프롬프트**
```text
The already-open wooden door sways once and dust drifts through its opening.
One existing coin rocks and settles beside the still club. No new treasure,
no characters returning, no scene change. Slight low camera drift only.
```
**편집·음향:** 시작부터 방망이/금이 버려져 있음. 0.3초 문 삐걱임과 먼 바람, 도깨비 비명 없음. 아직 개암을 보여주지 않아 첫 문장의 질문을 남김.

## 컷 02 · 4~8초 · f120~239 · 그날 밤

**KO:** 그날 밤, 나무꾼은 빈집에 몸을 숨겼다.
**EN:** That night, a woodcutter hid inside an empty house.

**이미지 프롬프트**
```text
Earlier that night in the same cottage. The woodcutter is already partly
hidden behind a broad wooden beam, gray patched cuff and ivory trousers
visible. He holds one hazelnut low in a still hand. The room beyond the
beam is empty and dark. No second human and no subtitles.
```
**Flow 모션 프롬프트**
```text
He draws his shoulder a little farther behind the beam and becomes still.
His hand keeps the hazelnut steady. A loose sleeve edge moves slightly.
No walking cycle, no talking mouth, no exaggerated fear or extra hands.
```
**편집·음향:** `그날 밤 / That night`로 회상 시간 연결, 별도 타이틀 컷 없음. 4.5~6초 숨는 한 동작. 천 마찰만 낮게, 입/치아 접사는 하지 않음.

## 컷 03 · 8~12초 · f240~359 · 금을 부르는 방망이

**KO:** 도깨비들이 방망이를 두드리자, 금이 쏟아졌다.
**EN:** Goblins tapped a magic club, and gold appeared.

**이미지 프롬프트**
```text
Exactly two charcoal-brush dokkaebi stand in the same room. One holds the
same wooden club just above the floor, the other watches. A few flat ochre
coin shapes already lie near the striking spot. The woodcutter is out of
view behind the beam. Readable simple figures, no crowded feast.
```
**Flow 모션 프롬프트**
```text
The club-holding dokkaebi taps the floor once with a small controlled motion.
Two existing coins slide slightly and settle. The other dokkaebi leans in
a little. Preserve club and bodies, no crowd, no endless 3D gold fountain.
```
**편집·음향:** 실제 탭 시점에 둔한 황토 붓점/동전 레이어 8~12개를 짧게 드러내 금이 생기는 마법을 보조. Flow에 여러 사건을 동시에 요구하지 않음. 낮은 나무 타격 1회와 작은 금속 잔향.

## 컷 04 · 12~16초 · f360~479 · 작은 소리

**KO:** 배고픈 나무꾼이 개암을 깨물자, 큰 소리가 울렸다.
**EN:** Hungry, he cracked a hazelnut. The sound rang out.

**이미지 프롬프트**
```text
Side view behind the same beam. The woodcutter already holds the hazelnut
at his gently closed lips, mouth detail minimal, patched cuff visible.
Dark empty space separates him from the distant room. No teeth close-up,
no captions, no other person and no second nut.
```
**Flow 모션 프롬프트**
```text
He makes one tiny deliberate biting motion with the nut already at his
lips, then stops. His hand remains steady. A faint existing shell crack
widens slightly. No repetitive chewing, no speech-like mouth motion,
no wide-open mouth or facial distortion.
```
**편집·음향:** 깨무는 순간(목표 약 13.6초)에 개암 부러지는 `딱` 효과음을 **SFX로만** 한 번, 이후 실내 울림 0.2~0.3초. narrator는 의성어를 연기하지 않는다. BGM을 5~7프레임 낮춰 소리를 읽히게 하고 볼륨 급등/화면 흔들기 금지.

## 컷 05 · 16~20초 · f480~599 · 큰 오해

**KO:** 집이 무너지는 줄 안 도깨비들은 그대로 달아났다.
**EN:** The goblins thought the house was collapsing. They fled.

**이미지 프롬프트**
```text
The same two dokkaebi stand near the already-open doorway, turned away from
the club left on the floor. They look upward toward an intact dark ceiling
beam with round startled eyes. A little dust hangs below the beam. Keep
all walls and roof structurally intact, no real collapse.
```
**Flow 모션 프롬프트**
```text
Both simplified dokkaebi silhouettes make one short backward retreat toward
the open doorway. A little dust falls from the intact beam. The club stays
behind. No full running choreography, extra characters, attack or collapsing roof.
```
**편집·음향:** 16.2~17.2초 위쪽 시선/먼지, 17.2~19초 물러남. 필요시 문쪽 전경 먹 가림으로 도주를 마무리하되 실제 영상 움직임은 남긴다. 집이 실제 붕괴하면 잘못된 인과이므로 FAIL. 소리만 오해, 도깨비 대사는 없음.

## 컷 06 · 20~24초 · f600~719 · 남은 행운

**KO:** 남겨진 방망이는 고스란히 나무꾼 차지가 됐다.
**EN:** The abandoned club was now the woodcutter's to keep.

**이미지 프롬프트**
```text
The woodcutter kneels in the empty room beside the same abandoned club.
His patched-cuff hand already rests on its handle; a few coins remain near
the head. His face shows quiet surprise, mouth closed. Same floorboard and
open doorway from shot one, no dokkaebi remaining.
```
**Flow 모션 프롬프트**
```text
He gently raises the already-held club handle a short distance, keeping its
head close to the floor. The cloth tie shifts softly. Preserve hand and
club anatomy, no swinging, no new magic burst or speaking mouth.
```
**편집·음향:** 20.5~22.5초 손잡이 들기. 원인을 이해한 뒤 보상이 도착하게 순서 유지. 동전 폭포를 또 넣지 않음. 짧은 목재 소리와 장단의 작은 해소.

## 컷 07 · 24~28초 · f720~839 · 진짜 무기

**KO:** 도깨비를 이긴 건, 칼도 부적도 아닌 개암 한 알이었다.
**EN:** No sword. No charm. Just one tiny hazelnut.

**이미지 프롬프트**
```text
Macro foreground of the single cracked hazelnut and a small shell fragment
on the same wooden floor. Behind them, the club and the woodcutter's patched
gray sleeve are softly visible. The tiny nut is the hero of the composition.
Warm ivory dawn at the doorway, no swords or charms appearing literally.
```
**Flow 모션 프롬프트**
```text
The small shell fragment rolls a short distance and stops against the nut.
The woodcutter's sleeve moves softly in the background. A tiny slow camera
move closer emphasizes the nut. No new objects, no multiplying shell or magic.
```
**편집·음향:** 24.5~26.5초 껍질과 개암을 읽힘. narrator가 `칼도 부적도 아닌 / No sword. No charm.`을 말해도 새 칼/부적을 생성하지 않는다. 마지막 개암을 따뜻하게 강조하고 설명을 추가하지 않음.

## 공용 전환

| 경계 | 종류 / 길이 | 구현 |
|---|---|---|
| f120 | DRY_BRUSH_WIPE / 12f | 바닥 나뭇결 아래→위, 들보 뒤 회상 장면으로 |
| f240 | INK_BLOOM / 18f | 들보 (0.25W,0.5H) 먹에서 번져 도깨비 둘 등장 |
| f360 | DRY_BRUSH_WIPE / 12f | 방망이 내려친 방향 위→아래, 숨은 나무꾼 접사 |
| f480 | MATCH_CUT / 0f | 앞 컷의 소리 잔향을 이어 받으며 위를 보는 도깨비 반응으로 직접 컷 |
| f600 | FOG_VEIL / 18f | 문쪽 먼지가 좌→우로 덮이고 빈 방/나무꾼 |
| f720 | GOLD_DUST / 12f | 방망이 앞 황토 붓점과 한지 밑칠로 가린 뒤 작은 개암 접사 |

## 추가 QA

작은 소리→큰 오해→도주가 이해되는지 실제로 본다. 두 도깨비/한 방망이/한 개암을 유지. 집은 무너지지 않음. 부모/욕심쟁이 후일담, 추가 인물, 별도 8번째 컷을 넣지 않는다. 입 동작은 4컷의 단 한 번 깨물기만이며 대사처럼 반복되면 FAIL. 공용 마스터의 동일성과 두 언어별 SFX/자막 싱크를 확인한다.
