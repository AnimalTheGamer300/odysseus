# `src/copilot.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `device_code_url` — function, line 65
- **called from:**
- `src/copilot.py:155`

## `access_token_url` — function, line 69
- **called from:**
- `src/copilot.py:170`

## `normalize_domain` — function, line 73
- **called from:**
- `routes/copilot_routes.py:106`
- `src/copilot.py:86`

## `enterprise_base` — function, line 78
- **called from:**
- `routes/copilot_routes.py:147`
- `tests/test_copilot.py:33`
- `tests/test_copilot.py:34`
- `tests/test_copilot.py:35`

## `is_copilot_base` — function, line 89
- **called from:**
- `src/llm_core.py:1020`
- `src/llm_core.py:1155`
- `src/model_context.py:509`
- `tests/test_copilot.py:21`

## `copilot_headers` — function, line 108
- **called from:**
- `src/copilot.py:191`
- `src/endpoint_resolver.py:329`
- `src/llm_core.py:1135`
- `tests/test_copilot.py:41`
- `tests/test_copilot.py:51`
- `tests/test_copilot.py:57`

## `_oauth_post_headers` — function, line 142
- **called from:**
- `src/copilot.py:156`
- `src/copilot.py:171`

## `request_device_code` — function, line 150
- **called from:**
- `routes/chatgpt_subscription_routes.py:111`
- `routes/copilot_routes.py:108`
- `tests/test_copilot.py:159`

## `poll_access_token` — function, line 164
- **called from:**
- `routes/copilot_routes.py:141`
- `tests/test_copilot.py:174`

## `fetch_models` — function, line 183
- **called from:**
- `routes/copilot_routes.py:48`
- `tests/test_copilot.py:129`
- `tests/test_copilot.py:142`

## `_parse` — function, line 195
- **called from:**
- `routes/skills_routes.py:272`
- `src/copilot.py:207`
- `static/js/cookbook-hwfit.js:1572`
- `static/js/cookbook-hwfit.js:1572`
- `static/js/emailLibrary.js:3637`
- `static/js/emailLibrary.js:3638`

## `request_flags` — function, line 222
- **called from:**
- `src/copilot.py:251`
- `tests/test_copilot.py:75`
- `tests/test_copilot.py:80`
- `tests/test_copilot.py:88`
- `tests/test_copilot.py:95`
- `tests/test_copilot.py:96`
- `tests/test_copilot.py:100`
- `tests/test_copilot.py:101`

## `apply_request_headers` — function, line 248
- **called from:**
- `src/llm_core.py:2333`
- `src/llm_core.py:2753`
- `src/llm_core.py:3051`
- `tests/test_copilot.py:106`
