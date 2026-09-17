# 수묵담채 공용 시각 마스터 / v2 편집 규격

이 수치들은 프로젝트의 디자인 목표다. Flow가 프롬프트의 시간을 정확히 지키거나 특정 동작을 보장한다는 뜻이 아니다. 실제 원본과 편집기 버전을 확인한다. 한국어/영어판의 영상·카메라·전환·색·사물 애니메이션은 동일하다.

## 1. 공통 이미지 블록

```text
Vertical 9:16. Dreamlike Korean ink-and-light-color painting on warm ivory
hanji paper, hand-brushed black and diluted indigo ink, dry-brush edges,
soft wet-ink bleeding, delicate stable paper fibers and layered mist.
Restrained mineral pigments, generous negative space and readable silhouettes.
Joseon-inspired Korean hanbok and rural architecture where applicable;
an original stylized world, not a historical reconstruction. Flat painterly
surfaces with subtle depth, never glossy 3D or photoreal live action.
Use approved character references consistently. Keep the action central
and reserve quiet lower-middle space for captions added later.
No text, calligraphy, seals, lettering, subtitles, logos or UI in the image.
```

## 2. 공통 Flow 블록

```text
Animate the supplied start image as one continuous four-second shot.
Preserve composition, identity, costume, brushwork and hanji texture.
One restrained main action, subtle secondary wind or mist. The subject
must move, not only the camera. Keep paper grain stable, not boiling.
No internal scene cuts, new characters, scene morphs or generated transitions.
Silent visual storytelling: no dialogue, no spoken words, no whispering,
chanting, singing, voiceover, lip sync or speech-like mouth movement.
No captions, subtitles or language-specific text. Narration is added later.
```

이미지/Flow에 narration 텍스트를 첨부하지 않는다. 실제 별도 음소거 옵션이 없으면 만들어내지 말고, 생성 원본 보존 후 편집 입력에서 원본 오디오 트랙을 제거한다. 입은 말하는 듯 움직이지 않아야 한다. 04의 한 번 깨무는 동작만 허용하며 반복 수다로 해석되는 모션은 금지.

## 3. 화풍/동작 제한

한국풍 복식과 시골 공간, 먹+한지에 이야기 강조색 소량만 쓴다. 플라스틱 피부, 실사 얼굴, 네온, 사이버펑크, 과도한 셀 외곽선, 레이저, 번쩍임, 기모노/도리이/중국 황실 궁궐을 섞지 않는다. 이는 본 작품의 미술 방향이다. 현대 캐릭터/영화 디자인을 복제하지 않는다. 서비스 표시/워터마크를 제거하지 않는다.

캐릭터 시트로 얼굴/머리/옷/소품/키 비율/이동 방향을 고정한다. 고개 5~10도, 손 몇 cm, 옷자락/구슬/눈발 등 작은 행동을 선호한다. 카메라 이동은 약 화면폭 2~5%, 줌 약 1.00→1.03을 의도로 전달하되 실제로 이미 움직이는 원본에 중복 줌을 얹지 않는다. 환경만 움직여도 정물 컷은 가능하나 인물 중심 컷에서 카메라 줌만 있는 결과는 불합격.

## 4. 28초를 보존하는 타임라인

30fps, 7컷 × 120프레임 = 840프레임. 컷 구간은 [0,120), [120,240), [240,360), [360,480), [480,600), [600,720), [720,840). 경계 f120/240/360/480/600/720.

**고정 컷 아래 hard cut + 경계 위 가림막 오버레이** 방식. 경계 b, 효과 길이 w가 짝수일 때 [b-w/2,b+w/2)에서 효과를 재생한다. b에서 완전히 덮고 다음 컷을 드러낸다. 첫 18f 예시는 [111,129). MATCH_CUT은 의도적으로 가림막 없이 즉시 전환한다.

전환을 겹쳐 총 길이가 짧아지는 TransitionSeries.Transition 또는 무계획 xfade를 사용하지 않는다. 부족분을 정지 프레임/검은 화면으로 메우지 않는다. 일반 Sequence와 전면 오버레이 또는 동일 원리의 합성을 사용한다. 설치 버전의 API 지원을 확인하고 메서드를 추측하지 않는다.

SVG/Canvas 효과의 난수는 story_id+boundary_frame으로 고정 시드. 매 프레임 Math.random, 실시간 타이머, 무한 CSS animation에 의존하지 않는다. **공용 마스터를 한 번 렌더하여 재사용**하므로 KO/EN에서 입자 배치가 달라지지 않는다. 제목/자막/언어별 라벨은 공용 마스터에 굽지 않는다.

## 5. 전환 사전

각 이야기의 경계 표가 실제 종류/길이/방향/anchor를 지정한다. 좌표는 화면 W/H의 비율이다. 작은 입자만 흩뿌려 화면이 가려졌다고 보지 않는다. 경계 b에 완전 가림을 만들되 한 프레임 백색 플래시는 금지한다.

| ID | 기본 길이 | 구현 |
|---|---:|---|
| INK_BLOOM | 18f | 지정 anchor에서 불규칙 젖은 먹 마스크 확대. 진행 0~0.45 덮기, 0.45~0.55 전면 가림, 0.55~1 걷기. 외곽 feather 20~40px/1080폭, 얼굴 대신 그림자/나무에서 시작 |
| DRY_BRUSH_WIPE | 12f | 넓은 붓 획을 방향대로 2f 시차 이동. 갈라진 붓털 외곽, 중앙 2f는 한지 밑칠+먹으로 빈틈 없이 가림. 글자 쓰기 아님 |
| FOG_VEIL | 18f | 불투명 한지색 안개 3겹, 다른 속도. 가장자리만 feather, 경계에서 중간층 전면 가림. 전후 바람 방향 일치 |
| CLOTH_WIPE | 16f | 원래 옷색의 넓은 2D 천 곡선을 전경으로 이동. path만 변형, 신체를 늘이지 않음. 중앙에서 천/한지 밑칠이 전면 가림 |
| WATER_RIPPLE | 16f | anchor에서 동심원 2개. 작은 변위만, 얼굴 왜곡 금지. 한지색 원형 가림막은 파문과 분리하여 경계를 덮음 |
| PETAL_VEIL | 18f | 직접 그린 5~7종 꽃잎 12~24개를 고정 시드 이동. 큰 전경 꽃잎 2~3개와 한지 안개가 b에서 전면 가림. 불꽃/네온 금지 |
| MOON_WASH | 18f | 달/구슬/붉은 점에서 은백 또는 한지색 마스크가 확대되어 먹을 씻음. 전면 가림 뒤 같은 위치의 다음 물체 공개. 매끄러운 밝기 변화 |
| GOLD_DUST | 12f | 황토색 붓점 최대 20개, 짧은 호 운동. 마른 붓+한지 밑칠로 b에서 가림. 광택 3D 금화 폭포 금지 |
| MATCH_CUT | 0f | 전후 원/로프/방향의 중심과 크기를 미리 맞춘 cut 또는 이야기의 의도적 반응 cut. 오버랩 없음, 시간 감소 없음 |

형태 매치컷은 1080폭 기준 중심 오차 약 20px 이내를 편집 목표로 잡되, 인물/서비스 표시를 잘라내 맞추지 않는다. 효과음은 전환마다 똑같은 whoosh를 반복하지 않고 필요한 곳만 종이/비단/바람을 낮게 사용한다.

## 6. 특수 동작의 로컬 합성

해/달: 준비 이미지의 기존 두 원반을 작은 먹 씻김으로 강조. 사람 몸을 원반으로 바꾸는 모핑 없음.

구미호: 인물 뒤 눈 위에 **정확히 9개**의 독립 붓 경로를 만들고 1~2f 위상차와 미세 흔들림만 준다. 몸에 꼬리를 생성하지 않는다. 5컷과 7컷에서 같은 모티프를 사용. 실제 끝부분이 9개로 읽히는지 확인. 구슬의 빛은 무발광 구슬 위 별도 glow 레이어를 붙였다가 10~16f에 걸쳐 줄여 소멸을 통제한다.

도깨비: 방망이 탭 순간 기존 동전 주변에 작은 금색 붓점 레이어를 추가. 실제 집은 무너지지 않으며 먼지/도깨비 시선/소리로 오해만 전달한다. 복잡한 달리기 대신 한 걸음 후 문쪽 먹 가림.

매화령: 실제 Flow 손/소매/꽃잎 움직임 위에 인물 마스크와 clean plate를 합성한다. 배경은 기존 이미지를 무료 로컬 편집해 확보하고 추가 유료 생성 금지. 마스크가 나쁘면 인물을 녹이지 말고 PETAL_VEIL이 몸을 완전히 가린 뒤 빈 무덤 컷으로 전환한다. 사라짐은 서사적 은유이며 신체 공포 모핑을 사용하지 않는다.

## 7. 두 언어 자막/타이틀

공용 마스터는 글자 없음. KO에는 한국어만, EN에는 영어만 후반으로 붙인다. 각 언어 실제 오디오에서 별도 정렬해 타임코드를 만들고 의미 단위 1~2줄을 유지한다. 자막을 컷 시작마다 통문장으로 공개해 반전을 누설하지 않는다. 언어별 지시는 BILINGUAL_NARRATION.md를 따른다.

1080×1920 시작점: 좌우 100px 이상 여백, 자막 x=110~970/y=1260~1490, 작은 제목/분류 x=100~850/y=200~340. 실제 게시 플랫폼 미리보기에서 가림을 확인한다. 본문 KO 약 50~58px, EN 약 48~56px에서 시작하되 실제 폰트/줄 길이로 조정, 읽기 어렵게 축소하지 않는다.

실제 사용 가능한 한글/영문 폰트를 확인한다. 한지 바탕은 먹색 글자+옅은 한지 받침, 어두운 바탕은 한지색 글자+먹 그림자. 강조는 이야기 색으로 단어 1~2개만. 진입 5~7f opacity + y8px 정도, 바운스/글자별 날아오기 금지. 별도 로고/엔딩 카드는 추가하지 않는다.

## 8. 음향/검수

내레이터 한 명의 목소리가 중심. 캐릭터 대사·인용 연기·노래·비명·흐느낌 연기는 제외한다. 사용 허가된 대금/해금/가야금 질감의 음악 또는 직접 만든 앰비언스만, 불명확한 OST 사용 금지. 확보한 음원이 없으면 BGM 없이도 진행 가능.

두 언어는 같은 BGM/SFX를 사용하되 각각의 voice에 맞춰 ducking을 조절한다. 음성 아래 BGM은 약 12~18dB 낮은 지각 수준에서 출발하여 실제로 들어본다. 최종 -16~-14 LUFS/true peak -1dBTP 이하는 목표이며 자연스러움의 보증 아님.

7컷 접촉표, 시작/중간/끝, 6개 경계 전후를 확인하고 정상 속도로 두 편을 실제 시청/청취한다. 형태/손/옷/먹결 깜빡임/입 움직임/반전/타이틀 언어/오탈자/잘림/음량/잔향 끊김을 검사. 원본 7개 해시와 공용 마스터 해시, 두 언어가 그 마스터를 참조하는 기록을 남긴다. 미디어가 없으면 검수 완료로 쓰지 않는다.
