# 업로드 문구 전달 — Codex v4

Hermes를 거치지 않고 루트 [START_CODEX.md](../START_CODEX.md)로 실행합니다. 기존metadata.json의제목/태그/설명초안은참조용으로보존합니다.

`python tools/codex_production.py prepare --episode ... --out ...`가현재run/youtube/ko와en에**33초로갱신한**문구를준비합니다. 완성영상/언어/음악크레딧과대조하여이실행용파일을전달합니다. 과거28초설명을그대로사용하지않습니다. 유튜브업로드·예약·채널변경은실행하지않습니다.
