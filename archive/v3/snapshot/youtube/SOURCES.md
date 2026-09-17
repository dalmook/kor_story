# 업로드 문구의 근거와 확인 범위

확인일: 2026-09-17. 제목·설명·채널 소개는 이 프로젝트를 위해 새로 작성한 창작 문구입니다. 검색량·순위·조회수·클릭률을 실측한 SEO 결과가 아니며 성과를 보장하지 않습니다.

## 제작 내용의 근거

GitHub `dalmook/kor_story`, 기준 커밋 `82a1874f20c247db4f7a4402e95e0158f18f9ea6`, 활성 `narration/manifest.json`의 8개 episode_id 및 v3 파트 구성. 해당 manifest Git blob: `949fb3d02db2df48221e54d05bed80c1c221e85e`. 구미호·매화령은 실제 현재 원고를 읽고 창작 및 반전 범위를 확인했습니다. 기존 내레이션·스토리·Flow 지시는 변경하지 않습니다.

영문 채널명 Dalbong Korean Tales는 사용자가 선택한 이름입니다. 한국어 채널명과 두 채널의 실제 ID·핸들·공개 영상 주소는 확인되지 않았습니다. 이름으로 URL을 만들어 넣지 않습니다.

## 공식 플랫폼 근거

**S1 — YouTube Data API, Videos**
https://developers.google.com/youtube/v3/docs/videos
제목 최대100자, 설명 최대5,000 UTF-8 bytes, 태그 합산500자와 쉼표/공백 태그의 따옴표 계산 규칙을 검사기에 적용합니다. Studio 화면 표기와 별개로 API에도 맞도록 보수적으로 바이트를 검사합니다. 문구는 제한보다 충분히 짧게 작성했습니다.

**S2 — Add tags to your YouTube videos**
https://support.google.com/youtube/answer/146402?hl=en
일반 태그는 전용 입력란용입니다. 제목·설명·썸네일이 더 중요하며 태그만으로 노출을 보장하지 않습니다. 설명을 일반 태그의 나열로 채우지 않습니다.

**S3 — Find playlists & videos using hashtags**
https://support.google.com/youtube/answer/6390658?hl=en
해시태그는 제목/설명에 쓰는 별도 요소입니다. 관련 없는 해시태그를 넣지 않습니다. 본 패키지의 3개는 편집 선택이며 플랫폼 상한을 뜻하지 않습니다.

**S4 — Sharing links with your audiences**
https://support.google.com/youtube/answer/13748639?hl=en
공식 검색 결과에서 Shorts 설명/댓글의 일반 URL이 비클릭형임을 확인했습니다. 직접 페이지 열기는 오류가 있었으므로 그 한계를 구분합니다. 복사 문구에는 임의의 다음 편 URL을 넣지 않았습니다.

**S5 — Add a related video to your YouTube Shorts**
https://support.google.com/youtube/answer/14075157?hl=en
같은 채널의 실제 공개/일부공개 콘텐츠를 관련 동영상으로 연결할 수 있으며 고급 기능 접근이 필요합니다. 다음 편의 존재·공개 상태는 별도로 확인해야 합니다.

**S6 — Determining if your content is made for kids**
https://support.google.com/youtube/answer/9528076?hl=en
대상 시청자와 콘텐츠 요소를 종합해 검토할 항목입니다. 이 문구 패키지에서 아동용 여부를 자동 지정하지 않습니다.

**S7 — Disclosing use of GenAI content**
https://support.google.com/youtube/answer/14328491?hl=en
최종 영상/오디오의 AI 사용과 사실성을 공식 기준에 대조할 항목입니다. 단순히 애니메이션이라는 이유로 모든 공개 판단을 완료 처리하지 않습니다.

## 검수의 범위

로컬 검사기는 제목/설명/태그 길이, 해시태그와 일반 태그 구분, 언어별 파일 연결, 파트번호·앞뒤 연결의 manifest 일치, 창작 표시, 지정한 반전 단어, Markdown과 JSON의 일치를 검사합니다. 테스트는 로컬에서 실행하며 계정·영상·업로드에 접근하지 않습니다.

이번 작업은 메타데이터 작성과 텍스트 검수입니다. 실제 MP4·음성 자연스러움·시청자 분류·공개 설정·채널 연결·게시 결과를 검증한 것은 아닙니다.
