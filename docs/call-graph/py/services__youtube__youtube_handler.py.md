# `services/youtube/youtube_handler.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_find_ytdlp` — function, line 39
- **called from:**
- `services/youtube/youtube_handler.py:217`

## `init_youtube` — function, line 48
- **called from:**
- `app.py:556`
- `tests/test_youtube_handler_consolidation.py:53`

## `is_youtube_url` — function, line 61
- **called from:**
- `src/chat_handler.py:149`
- `src/chat_processor.py:477`
- `tests/test_is_youtube_url_nonstring.py:7`
- `tests/test_is_youtube_url_nonstring.py:8`
- `tests/test_is_youtube_url_nonstring.py:9`
- `tests/test_is_youtube_url_nonstring.py:13`
- `tests/test_is_youtube_url_nonstring.py:14`
- `tests/test_is_youtube_url_nonstring_svc.py:6`
- `tests/test_is_youtube_url_nonstring_svc.py:7`
- `tests/test_is_youtube_url_nonstring_svc.py:8`
- `tests/test_is_youtube_url_nonstring_svc.py:12`
- `tests/test_is_youtube_url_nonstring_svc.py:13`
- `tests/test_youtube_handler_consolidation.py:103`

## `extract_youtube_id` — function, line 78
- **called from:**
- `routes/diagnostics_routes.py:77`
- `src/chat_handler.py:150`
- `tests/test_youtube_extract_id_nonstring.py:8`
- `tests/test_youtube_extract_id_nonstring.py:9`
- `tests/test_youtube_extract_id_nonstring.py:10`
- `tests/test_youtube_extract_id_nonstring.py:14`
- `tests/test_youtube_extract_id_nonstring.py:15`
- `tests/test_youtube_handler_consolidation.py:93`
- `tests/test_youtube_handler_consolidation.py:104`

## `extract_transcript_async` — function (async), line 104
- **called from:**
- `routes/diagnostics_routes.py:81`
- `src/chat_handler.py:156`

## `format_transcript_for_context` — function, line 161
- **called from:**
- `src/chat_handler.py:165`
- `tests/test_youtube_transcript_seg_nondict.py:17`

## `fetch_youtube_comments` — function (async), line 208
- **called from:**
- `src/chat_handler.py:157`
- `tests/test_youtube_comments_timeout.py:40`

## `format_comments_for_context` — function, line 282
- **called from:**
- `src/chat_handler.py:167`
- `tests/test_youtube_svc_comments_nondict.py:13`
