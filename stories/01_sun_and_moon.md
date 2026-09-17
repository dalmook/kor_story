# 01 · 해와 달이 된 오누이

**헤르메스 실행 지시:** AGENTS.md, docs/MASTER_PRODUCTION.md, docs/INK_EDITING_SPEC.md를 먼저 읽고 이 문서를 끝까지 실행한다. story_id=`01_sun_and_moon`. 다른 편은 실행하지 않는다. 세로 28초/7컷/편당 Flow 최대 50크레딧. 각 영문 블록은 공통 화풍 또는 공통 Flow 블록과 결합해 파일로 저장한다.

구분: 전래설화 축약 각색. 원전 참고: [한국민족문화대백과사전](https://encykorea.aks.ac.kr/Article/E0062663). 집 앞 위협부터 시작하며 어머니의 죽음과 호랑이의 잔혹한 추락은 보여주지 않는다. 해/달이 어느 남매인지 특정하지 않는다.

## 감독 방향

예쁜 산수화 소개로 시간을 쓰지 않는다. 첫 0.4초 안에 창호지에 찍힌 **호랑이 발톱**이 보여야 한다. 먹의 농담으로 위협을, 위쪽의 여백으로 탈출 가능성을 보여준다. 마지막에 검은 밤이 두 개의 빛으로 열리도록 한다.

색: 먹/아이보리 기본, 청람 남매 옷과 달빛, 마지막 해에만 옅은 황토색. 호랑이는 붉은 눈이나 괴물 이빨 대신 민화적 검은 줄무늬 실루엣. 한지 텍스처는 카메라가 움직여도 무작위로 일렁이지 않게 한다.

## 캐릭터 고정 블록

```text
Older brother: a Korean boy about ten, rounded face, black hair in a simple
short tied topknot, muted indigo jeogori and ivory trousers, no hat.
Younger sister: a Korean girl about seven, one long black braid with a muted
red ribbon, ivory jeogori and a desaturated blue-gray chima.
Keep their faces, outfits and height ratio identical in every shot.
Tiger: one stylized Korean folk-painting tiger, ochre-gray fur, bold black
brush stripes, rounded ears, no clothing and no monstrous anatomy.
Setting: a humble Korean thatched house, paper lattice door, a single old
pine-like tall tree beside the yard, mountains rendered as diluted ink.
```

## 연속 내레이션

아래 문장을 한 화자로 이어 읽는다. 대괄호/컷 번호는 읽지 않는다. 실제 발화 길이와 자막 시점은 렌더 후 측정한다.

> 그날 밤, 엄마의 손엔 발톱이 있었다.
> 문밖의 목소리는 호랑이였다.
> 오누이는 나무 위로 달아났다.
> 하늘님, 저희를 살려 주세요.
> 구름 사이로 동아줄이 내려왔다.
> 호랑이가 잡은 줄은 썩어 있었다.
> 그 밤을 벗어난 둘은 해와 달이 되었다.

톤: 낮고 명료한 구연, 첫 문장은 비밀을 발견하듯, 기도는 빠르지 않게, 마지막은 따뜻하게. 호랑이 괴성이나 대사를 추가 생성하지 않는다.

## 컷 01 · 0~4초 · [0,120) · 창호지의 손

**화면/서사:** 어두운 방 안에서 본 창호문 접사. 왼쪽에 세로 나무틀, 오른쪽 중앙에 발의 검은 그림자. 인물 얼굴 없이 시작한다. 자막 강조어 `발톱`.

**이미지 프롬프트**
```text
Close-up from inside a dark Korean thatched cottage, an ivory paper lattice
door fills the vertical frame. A single tiger paw silhouette presses against
the outside of the paper at the right-center, three claw tips clearly outlined
without tearing flesh. A slim wooden door frame stands on the left. Diluted
indigo night shadows, warm paper light, dramatic empty space below the paw.
```
**Flow 모션 프롬프트**
```text
The single paw slowly presses the paper once, making the paper bow inward
slightly; then it pauses. Keep the paw anatomy and lattice rigid. A faint
shadow moves across the paper. Locked camera, one continuous shot, no door
opening and no new subject entering.
```
**4초 내부 연출:** 0~0.4초 이미 발톱이 보임 → 0.4~2.2초 한 번 누름 → 2.2~3.7초 그림자가 짙어짐. 발톱이 하나씩 돋는 변형은 금지. 끝 9프레임부터 INK_BLOOM 준비.

**음향:** 0.2초 낮은 나무 삐걱임 1회, 아주 작은 문풍지 떨림. 큰 놀람 효과 금지.

## 컷 02 · 4~8초 · [120,240) · 엄마가 아니다

**화면/서사:** 방 안에서 두 남매 반신. 오빠는 오른쪽 문을 보고 누이는 옷자락을 잡는다. 창호 그림자는 배경에서만 보인다. 강조어 `호랑이`.

**이미지 프롬프트**
```text
Inside the same small Korean cottage, the approved boy and girl stand close
together, waist-up, at the left-center of frame. The younger girl lightly holds
the boy's sleeve. Both look toward the paper door on screen right. Behind the
door, one broad tiger shadow is visible. Their fear is restrained, not screaming.
```
**Flow 모션 프롬프트**
```text
The boy turns his head a few degrees toward the door and gently draws his
sleeve closer to his sister. The girl stays beside him and blinks once.
A small oil-lamp shadow flickers softly. Preserve both faces and hands;
no walking, no extra people, no speaking mouths.
```
**내부 연출:** 4.1~5.6초 오빠의 시선 → 5.6~7.6초 두 아이가 서로 가까워짐. 과한 안면 표정 대신 어깨와 시선. 다음 컷의 나뭇결과 문틀 방향을 맞춘다.

**음향:** 낮은 바람 지속, 원본 호랑이 음성은 음소거. `호랑이였다` 뒤 0.15초의 작은 여백.

## 컷 03 · 8~12초 · [240,360) · 나무 위 피신

**화면/서사:** 아이들은 이미 높은 가지 위에 있다. 복잡한 나무 오르기를 4초 안에 생성하지 않는다. 아래쪽은 짙은 먹, 위쪽은 달빛 여백.

**이미지 프롬프트**
```text
Low-angle view of the same two children already safely seated on a thick high
branch of one old tree. The trunk rises along the left third. The boy shields
the girl with his shoulder. Far below, a small tiger silhouette stands at the
base, separated by mist. Huge pale moonlit sky above; no visible injury.
```
**Flow 모션 프롬프트**
```text
The thick branch sways very gently once in the night wind. The children tighten
their posture without changing their grip, while the girl's ribbon flutters.
Slow upward camera drift only. Keep all bodies stable and the distant tiger
still. No climbing action and no sudden jump.
```
**내부 연출:** 8~9.5초 남매 위치 인지 → 9.5~11.6초 위로 흐르는 리본과 시선. 카메라가 나무를 한 바퀴 돌지 않는다.

**음향:** 잎사귀·옷감, 짧은 낮은 북 울림 1회. 호랑이 포효 반복 금지.

## 컷 04 · 12~16초 · [360,480) · 기도

**화면/서사:** 누이 측면 접사, 두 손은 이미 모여 있고 자세는 유지. 위쪽 여백으로 기도를 받는다. 강조어 `살려 주세요`.

**이미지 프롬프트**
```text
Intimate side close-up of the approved girl on the same tree branch, her hands
already clasped near her chest, her braid and muted red ribbon visible. She
looks upward toward a broad empty ivory sky. A small edge of the boy's indigo
sleeve remains at the left. Soft diluted-ink moonlight, no tears exaggerated.
```
**Flow 모션 프롬프트**
```text
The girl slowly raises her gaze and tilts her chin slightly upward while
keeping her clasped hands still. Her ribbon lifts gently in the breeze.
A thin cloud drifts across the upper empty sky. Preserve her face and fingers;
no lip movement, no rope appearing yet.
```
**내부 연출:** 12.2~14초 시선 상승 → 14~15.7초 고요한 멈춤. 다음 로프가 내려올 x=중앙 방향에 시선을 맞춘다.

**음향:** 기도 문장 아래 BGM을 조금 낮춘다. 15.5초부터 가벼운 바람을 다음 컷으로 J-cut.

## 컷 05 · 16~20초 · [480,600) · 새 동아줄

**화면/서사:** 두 아이는 줄을 잡은 작은 뒷모습 실루엣으로 단순화한다. 새 동아줄의 굵은 섬유가 읽혀야 한다. 상승은 짧고 부드럽게.

**이미지 프롬프트**
```text
A strong pale braided rope descends vertically from layered ivory clouds.
The two approved children, shown as small clear back-view silhouettes with
recognizable clothing colors, already hold the rope just above their tree
branch. The rope is taut and intact. Vast sky, flowing ink mist, no angels,
no new people, no detailed finger close-up.
```
**Flow 모션 프롬프트**
```text
The taut rope gently lifts the two small silhouettes a short distance upward
together. Their grips and relative positions remain fixed. Clouds part slowly
behind them, and loose fabric trails downward. Keep the rope connected and
straight; no body transformation and no complete journey into another scene.
```
**내부 연출:** 16~17.4초 새 줄 확인 → 17.4~19.6초 작은 상승. 최소 상승 움직임이 없으면 정지 이미지 줌으로 대체하지 않는다.

**음향:** 마찰 없는 가벼운 바람, 낮은 현악이 조금 열림. 천사 합창·우주선 효과 금지.

## 컷 06 · 20~24초 · [600,720) · 썩은 줄

**화면/서사:** 화면 중앙의 썩은 동아줄 접사, 아래 모서리에 호랑이의 앞발 일부만. 동아줄 끊어짐이 핵심이며 추락 신체는 보이지 않는다.

**이미지 프롬프트**
```text
Close-up of a separate dark frayed rope against an ivory cloud background.
Rotten fibers at the center are nearly separated. One stylized tiger paw
holds the lower end at the bottom edge, with the rest of the animal out of
frame. Strong brush texture, readable loose strands, no falling body or injury.
```
**Flow 모션 프롬프트**
```text
The frayed rope strands separate once at the center, then the lower rope end
slips downward out of frame with the paw. Keep the event small and clear.
The upper end remains visible and sways gently. Locked camera; no tiger face,
no violent fall, no ground impact and no extra ropes.
```
**내부 연출:** 20.3~22초 실이 팽팽해짐 → 22초 전후 한 번 끊어짐 → 23초 구름 속 빈 공간. 실제 끊어진 시점에 SFX를 정렬한다.

**음향:** 짧은 섬유 끊김 1회. 비명·충돌·절규 없음.

## 컷 07 · 24~28초 · [720,840) · 두 개의 빛

**화면/서사:** 아이가 구체로 변하는 장면 대신 해와 달이 이미 존재하는 넓은 하늘. 왼쪽 위 옅은 황토 해, 오른쪽 위 은청색 달. 아래는 먹산수.

**이미지 프롬프트**
```text
A poetic Korean ink landscape under a vast ivory sky, layered mountains and
a tiny thatched roof far below. Two clearly separated celestial discs are
already present: a muted ochre sun on the upper left and a pale blue-gray moon
on the upper right. Soft cloud bands connect the composition without hiding
the discs. No children morphing, no faces drawn inside the sun or moon.
```
**Flow 모션 프롬프트**
```text
A thin cloud band drifts gently between the two stationary celestial discs.
Diluted ink mist moves slowly over the mountain ridges. Keep the sun and moon
shapes fixed and distinct. Subtle pullback only; no new objects, no sunrise
speed-ramp and no transformation.
```
**내부 연출:** 24~25.2초 두 빛을 동시에 인지 → 25.2~27.2초 달빛 먹 씻김을 낮은 강도로 합성 → 27.2~28초 구름만 움직이며 여운. 별도 엔딩 카드를 붙이지 않는다.

**음향:** 긴장 해소, 부드러운 한 음 뒤 자연스러운 잔향. 문장 끝을 마지막 프레임에서 자르지 않는다.

## 6개 경계의 정확한 편집

| 경계 | 효과 / 길이 | 시작 위치·방향·매치 |
|---|---|---|
| 4초 / f120 | INK_BLOOM / 18f | 발 그림자 중심 (0.66W,0.40H)에서 번져 덮은 뒤 아이들의 방 드러냄 |
| 8초 / f240 | DRY_BRUSH_WIPE / 12f | 왼쪽 문틀을 따라 아래→위, 다음 나무줄기 x=0.3W와 연결 |
| 12초 / f360 | FOG_VEIL / 18f | 나무 위 구름이 아래→위로 화면을 가리고 누이 접사로 |
| 16초 / f480 | MOON_WASH / 18f | 누이 시선 끝 (0.5W,0.25H)에서 번져 새 동아줄 드러냄 |
| 20초 / f600 | MATCH_CUT / 0f | 새 줄과 썩은 줄 중심 x=0.5W, 굵기 유사하게 맞춘 형태 연결 |
| 24초 / f720 | MOON_WASH / 18f | 끊어진 줄의 빈 하늘을 씻어내며 두 원반으로, 섬광 금지 |

좌표는 화면 너비/높이에 대한 정규화 값. 가림 효과는 경계에서 화면을 완전히 덮고 시간은 빼지 않는다.

## 이 편 추가 QA

첫 장면은 실제 발톱 형상이 보여야 한다. 남매의 성별/나이/옷/키 비율이 바뀌지 않아야 한다. 로프는 새 줄/썩은 줄 구분이 읽혀야 한다. 호랑이 추락이나 어머니 죽음을 끔찍하게 묘사하지 않는다. 마지막은 한 원반이 아니라 두 원반이다. 실제 원본 7개·49 이하 예상/50 실제 한도·840프레임과 청취/시청 상태를 기록한다.
