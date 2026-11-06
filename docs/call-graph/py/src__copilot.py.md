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
- `src/agent_runtime/context_resolution.py:355`
- `src/llm_core.py:1165`
- `src/llm_core.py:1399`
- `src/model_context.py:525`
- `tests/test_copilot.py:21`

## `copilot_headers` — function, line 108
- **called from:**
- `src/copilot.py:191`
- `src/endpoint_resolver.py:426`
- `src/llm_core.py:1379`
- `tests/test_copilot.py:41`
- `tests/test_copilot.py:51`
- `tests/test_copilot.py:57`

## `_oauth_post_headers` — function, line 142
- **called from:**
- `src/copilot.py:156`
- `src/copilot.py:171`

## `request_device_code` — function, line 150
- **called from:**
- `routes/chatgpt_subscription_routes.py:270`
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
- `src/agent_runtime/effect_log.py:229`
- `src/agent_runtime/effect_log.py:420`
- `src/agent_tools/editor_tools.py:364`
- `src/agent_tools/editor_tools.py:392`
- `src/agent_tools/editor_tools.py:442`
- `src/agent_tools/editor_tools.py:468`
- `src/agent_tools/editor_tools.py:644`
- `src/copilot.py:207`
- `tests/test_calendar_config_body.py:23`
- `tests/test_calendar_config_body.py:28`
- `tests/test_calendar_config_body.py:34`
- `static/js/cookbook-hwfit.js:1653`
- `static/js/cookbook-hwfit.js:1653`
- `static/js/emailLibrary/index.js:3728`
- `static/js/emailLibrary/index.js:3729`

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
- `src/llm_core.py:2687`
- `src/llm_core.py:3153`
- `src/llm_core.py:3478`
- `tests/test_copilot.py:106`
