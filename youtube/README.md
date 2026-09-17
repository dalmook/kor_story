# 유튜브 문구 — v4 실행 안내

기존 `metadata.json`, `episodes/`의 KO/EN 제목·대체제목·태그·설명 초안은 보존되어 있습니다. 현재 완성본은 오프닝/마지막원화를 포함한33초이므로 **옛 문서의28초 설명을 그대로 사용하지 않습니다.**

루트 `START_CODEX.md`에 따라 `python tools/codex_production.py prepare --episode ... --out ...`를 실행하면 해당 run의youtube/ko와youtube/en에33초로갱신한title.txt,description.txt,tags.txt,metadata_draft.json을만듭니다. 완성영상내용/음악크레딧/실제언어를대조한뒤이파일을전달합니다. 기존일반태그는Studio태그입력용이고해시태그는설명에이미있으므로중복하지않습니다.

원래8개에피소드×2언어의16세트,채널소개/키워드는그대로참조할수있습니다. 영어채널은Dalbong Korean Tales,실제채널ID는미확인입니다. 이름으로업로드대상을추측하지않습니다. 파트예고가있다고그영상이이미공개되었다고쓰지않고가짜링크도넣지않습니다.

`tools/youtube_metadata.py --check`는보존된문구의정합성검사이며v4영상을검수하지않습니다. `HERMES_HANDOFF.md`는폐기된진입점으로Codex문서를가리킵니다. 이번작업은문구준비까지만이며유튜브업로드·예약·채널변경을실행하지않습니다.
