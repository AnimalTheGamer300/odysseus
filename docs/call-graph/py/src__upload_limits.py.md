# `src/upload_limits.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `format_byte_limit` — function, line 11
- **called from:**
- `src/chat_helpers.py:376`
- `src/upload_handler.py:1291`
- `src/upload_limits.py:81`
- `tests/test_direct_upload_limits.py:33`
- `tests/test_direct_upload_limits.py:34`
- `tests/test_direct_upload_limits.py:35`

## `read_byte_limit_env` — function, line 19
- **called from:**
- `src/upload_limits.py:33`
- `src/upload_limits.py:44`
- `src/upload_limits.py:52`
- `src/upload_limits.py:55`
- `src/upload_limits.py:58`
- `src/upload_limits.py:61`
- `src/upload_limits.py:64`
- `src/upload_limits.py:67`
- `src/upload_limits.py:70`
- `tests/test_chat_upload_limit_config.py:42`

## `get_chat_upload_max_bytes` — function, line 32
- **called from:**
- `src/chat_helpers.py:370`
- `src/upload_handler.py:217`
- `tests/test_chat_upload_limit_config.py:22`
- `tests/test_chat_upload_limit_config.py:28`
- `tests/test_chat_upload_limit_config.py:35`

## `get_chat_video_upload_max_bytes` — function, line 43
- **called from:**
- `src/upload_handler.py:1286`

## `read_upload_limited` — function (async), line 75
- **called from:**
- `routes/calendar_routes.py:1419`
- `routes/email_routes.py:4027`
- `routes/gallery/gallery_routes.py:365`
- `routes/gallery/gallery_routes.py:451`
- `routes/gallery/gallery_routes.py:571`
- `routes/gallery/gallery_routes.py:616`
- `routes/memory/memory_routes.py:379`
- `routes/stt_routes.py:35`
- `tests/test_direct_upload_limits.py:21`
- `tests/test_direct_upload_limits.py:26`
