# 시장·레퍼런스 재조사 — v4

확인일: 2026-09-17. 대상은 짧은 서사 애니메이션, 동양 회화 기반 영상, 자막 가독성, 실제 제작 도구다. **경쟁채널 조회수 순위/클릭률/완주율을 실측한 조사는 아니다.** 공식 소개 페이지·공식 안내·작품 스틸과 제작 크레딧을 검토한 정성 비교다. 타 작품 전체영상이나 트레일러를 프레임 단위로 분석했다고 주장하지 않는다. 직접 프레임 검토한 영상은 사용자 첨부2개다.

## 비교표

| 공식 레퍼런스 | 확인한 자료 | 이번 작업에 적용한 판단 | 그대로 가져오지 않는 것 |
|---|---|---|---|
| 국립중앙박물관 디지털 실감영상관 | 회화 기반 실감콘텐츠 소개, 산수화/원화 자료 | 종이·먹·여백을 배경의 질감으로 남기고 인물/구름/사물만 절제해 움직인다 | 대형 전시의 긴 재생시간을 쇼츠 정답으로 쓰지 않음 |
| GKIDS, The Tale of the Princess Kaguya | 공식 영화소개/스틸 | 선과 여백, 단순한 실루엣이 읽히는 회화적 방향을 참조 | 일본 복식/캐릭터/작품의 특정 그림을 복제하지 않음 |
| TED-Ed, Monkey King and Buddha | 공식 이야기 소개와 감독·내레이터·작곡/음향 크레딧 | 내레이션·시각행동·음악을 각각 설계하고 하나의 짧은 사건을 명확히 전달 | 중국 이야기를 한국 전래설화의 근거로 삼거나 장편분량을 이식하지 않음 |
| YouTube, Jenny Hoyos/Todd Sherman 대담 | 2025-01-28 공식 창작자 인터뷰 | 오프닝 첫프레임부터 이야기의 의문이 보이게 한다 | “모든 영상은1초마다컷”이라는 알고리즘 법칙으로 확대하지 않음 |
| Netflix KO/EN timed-text 안내 | 두줄/읽기속도/의미단위 규칙 | 문장 단위 자막과 실제 발화 정렬·읽기시간 검수 | Netflix 납품규격을 YouTube 의무규격 또는 동일한 문자계산법이라고 부르지 않음 |
| YouTube Shorts 편집안내 | UI 안전영역 가이드/가려짐 경고 | 오른쪽 버튼과 아래 설명영역에서 멀리 자막 배치, 실제 모바일미리보기 | 고정픽셀좌표를 모든 기기의 공식 안전영역이라고 주장하지 않음 |

선택한 방향은 “빠르게 번쩍이는 쇼츠 템플릿”이 아니라 **단서가 명확한 회화형 미니서사**다. 첫2초를 빈 로고로 쓰지 않고 원화 속 문/그림자로 긴장을 만든다. 자막은 크고 오래 유지하고, 전환은 기본컷과 소수 디졸브로 제한한다. 이는 레퍼런스와 실제 실패영상에서 도출한 편집 판단이며 조회수 상승 보장이 아니다.

## 자막 기준의 적용 범위

Netflix 한국어 안내의 일반 번역자막 구간은 최대2줄, 성인12CPS/어린이9CPS이고, 한국어 원어SDH 구간은 다른 상한을 안내한다. 영문 안내 역시 별도 읽기속도 기준이 있다. v4는 그 중 “읽기시간과 의미단위를 검수한다”는 원칙을 참고해 **프로젝트 자체 목표**를 KO9/상한12, EN15/상한17로 정했다. 검사기의 CPS는 공백을 제외한 문자 수를 사용하는 보수적 자체 지표이며 Netflix의 언어별 가중계산과 동일하지 않다. 이 선택으로 영상의 아동용 여부가 결정되지 않는다.

제목108/92px, 자막72/68px, y1296..1472, 8프레임 디졸브, 음악60~72BPM 등의 수치는 이 프로젝트용 디렉팅이다. 특정 플랫폼이 강제하는 값이나 시장평균으로 표시하지 않는다. 글꼴/장면별 실제 가독성을 함께 검사한다.

## 실제 자동화 가능성과 비용

OpenAI는2026-04-16 Codex 데스크톱의 이미지 생성과 컴퓨터제어 확장을 발표했다. 다만 발표가 사용자의 모든OS/CLI/현재세션에서 해당 도구가 켜져 있다는 뜻은 아니다. 네이티브 이미지 도구, 브라우저·컴퓨터제어, 로그인, 사용권을 실제로 확인한 뒤 실행한다. 네이티브 도구가 없다고 유료API를 임의 호출하거나 기능명을 발명하지 않는다.

Flow 공식 비용표의 검색결과에는 Omni Flash720p·4초·결과1개가7크레딧으로 안내된다. 영문페이지 직접열기는 오류가 있었으며 같은 공식 문서의 다른언어 검색결과도 확인했다. 실행 시 실제계정UI를 우선한다. 7×7=49는 신규본문7개만의 계산이고 앞뒤원화는 로컬모션이다. 원화생성/TTS/음원에 별도비용이 들거나 같은Flow잔액이 차감되면 합산한다. 추가비용을 무료라고 단정하지 않는다.

YouTube Studio Audio Library는 음악·효과음의 이용안내와 곡별 라이선스/크레딧표시 정보를 제공한다. 기존 허가된 음원을 우선하고, 이 라이브러리를 사용할 때는 실제 곡과 라이선스·표시문구를 확인해 기록한다. 곡명을 임의로 만들어 이미 확보한 것처럼 쓰지 않는다. 음악이 준비되지 않았는데 BGM없는 영상을 완성이라고 보고하지 않는다.

## 공식 출처

R1. 국립중앙박물관 실감1관: https://www.museum.go.kr/MUSEUM/contents/M0203020000.do

R2. GKIDS 영화 페이지: https://gkids.com/films/the-tale-of-the-princess-kaguya/

R3. TED-Ed: https://ed.ted.com/lessons/the-tale-of-the-monkey-king-and-the-buddha-ji-hao

R4. YouTube 창작자 대담: https://blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/

R5. Netflix Korean: https://partnerhelp.netflixstudios.com/hc/en-us/articles/216001127-Korean-Timed-Text-Style-Guide

R6. Netflix English: https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide

R7. YouTube Shorts 편집/가이드: https://support.google.com/youtube/answer/16215842?hl=en

R8. Codex 공식 기능 발표: https://openai.com/ko-KR/index/codex-for-almost-everything/

R9. Flow 비용: https://support.google.com/flow/answer/16526234?hl=en

R10. Audio Library: https://support.google.com/youtube/answer/3376882?hl=en

조사페이지는 설화의 역사적 원전이나 음원사용허가 자체를 대체하지 않는다. 실제 제작자산은 별도 asset_sources.json에 출처·도구·라이선스·확인시각을 기록한다.
