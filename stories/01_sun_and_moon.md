# 해와 달이 된 오누이 — v3 / 2파트

이 문서는 시리즈 안내·공통 캐릭터 기준이다. **설화 전체를 28초에 만들지 않는다.** 한 번에 episode_id 하나만 제작한다.

| 파트 | 실행 ID / 상세 명령 | 서사 범위 |
|---|---|---|
| 1 · 문밖의 엄마 | [01_sun_and_moon_p01](../episodes/01_sun_and_moon_p01.md) | 정체를 알아채고 집을 탈출해 나무에 숨지만 호랑이가 발견한다 |
| 2 · 하늘에서 내려온 동아줄 | [01_sun_and_moon_p02](../episodes/01_sun_and_moon_p02.md) | 나무 위 위기부터 동아줄의 구원, 호랑이의 실패, 해와 달까지 |

각 파트는 28초/7컷/KO+EN 2개 출력. 총 이야기 러닝타임은 언어별 56초. 단가가 7이면 각 파트 영상 49, 2파트 영상 합계 98크레딧 예상이다. 한 파트의 생성 원본은 두 언어가 공유하지만 **파트끼리는 다른 7컷**이다. 1부 생성 후 자동으로 2부에 과금하지 않는다. `해와 달`처럼 시리즈만 지정되면 기본 실행 대상은 p01 하나다.

## 공통 이미지 참조

```text
Boy: Korean child about ten, rounded face, black hair in a small tied topknot,
muted indigo jeogori and ivory trousers. Girl: Korean child about seven,
one black braid with muted red ribbon, ivory jeogori and blue-gray chima.
Maintain faces, height ratio, clothing and hands across both parts.
Tiger: one ochre-gray Korean folk-painting tiger, bold black brush stripes,
rounded ears, no clothes or monstrous anatomy. One thatched Korean cottage,
one paper lattice door with three horizontal bars, one old tree with its
main trunk on screen left and a broad branch extending right. Indigo night,
ivory moon high on screen right. No text or dialogue.
```

참조는 `series_assets/01_sun_and_moon/`의 캐릭터·집·나무·팔레트·미술 버전으로 고정한다. p01 마지막의 아이들 위치와 호랑이 위치를 기록하고 p02 첫 장면은 같은 밤/나무의 **다른 구도**로 시작한다. 전편 영상 4초를 재방송하거나 같은 클립을 새 생성이라고 세지 않는다. 달빛과 리본의 바람 방향 유지.

공통 필독: AGENTS.md, docs/MASTER_PRODUCTION.md, docs/PART_PRODUCTION.md, docs/BILINGUAL_NARRATION.md, docs/INK_EDITING_SPEC.md. 각 파트의 narration/<episode_id>.ko.txt와 .en.txt가 낭독 기준이다.

어머니의 산길 대결/살해/젖먹이 대목은 생략한 전래설화 각색이며 완전한 원전 복원이 아니다. 해와 달의 성별은 고정하지 않는다. 출처 및 각색 범위는 docs/SOURCES.md. 기존 v2 단일편은 archive/v2에 보존되며 실행 대상이 아니다.
