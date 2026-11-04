# `static/js/chatStreamErrors.js` — definitions & call sites

3 definitions (regex-based, best-effort).
**Exports:** `createTerminalStreamError`, `isRecoverableStreamError`

## `createTerminalStreamError` — function, line 2
- **called from:**
- `static/js/chat.js:3265`
- `static/js/chat.js:4468`
- `static/js/chat.js:5770`
- `static/js/chatStreamErrors.js:2`

## `stream` — class, line 16
- **called from:**
- `src/llm_core.py:3075`
- `src/llm_core.py:3196`
- `src/llm_core.py:3295`
- `src/llm_core.py:3500`
- `src/outbound_fetch.py:297`
- `tests/test_compare_stop_disconnect_poll.py:200`
- `tests/test_compare_stop_disconnect_poll.py:206`
- `tests/test_shell_service.py:52`
- `tests/test_web_fetch_size_caps.py:56`
- `tests/test_web_fetch_size_caps.py:63`
- `static/js/chat.js:342`
- `static/js/sessions.js:2217`
- `static/js/sessions.js:2796`

## `isRecoverableStreamError` — function, line 17
- **called from:**
- `static/js/chat.js:5043`
- `static/js/chatStreamErrors.js:17`
