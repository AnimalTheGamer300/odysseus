# `src/rate_limiter.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `RateLimiter` — class, line 9
- **called from:**
- `routes/auth_routes.py:119`
- `routes/auth_routes.py:120`
- `routes/auth_routes.py:121`
- `tests/test_rate_limiter.py:10`
- `tests/test_rate_limiter.py:16`
- `tests/test_rate_limiter.py:22`
- `tests/test_rate_limiter.py:31`
- `tests/test_rate_limiter.py:40`

## `RateLimiter.__init__` — method, line 18
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email_routes.py:1455`
- `src/builtin_actions.py:428`
- `src/outbound_fetch.py:220`
- `tests/test_agent_state_dir_confinement.py:648`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_extraction_controls.py:14`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_retired_settings_interfaces.py:30`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:148`

## `RateLimiter.check` — method, line 26
- **called from:**
- `routes/auth_routes.py:130`
- `routes/auth_routes.py:148`
- `routes/auth_routes.py:167`
- `src/llm_core.py:3117`
- `src/llm_core.py:3623`
- `src/llm_core.py:3632`
- `tests/markdown_browser_check.py:80`
- `tests/markdown_browser_check.py:82`
- `tests/markdown_browser_check.py:84`
- `tests/markdown_browser_check.py:86`
- `tests/markdown_browser_check.py:88`
- `tests/markdown_browser_check.py:90`
- `tests/markdown_browser_check.py:92`
- `tests/markdown_browser_check.py:95`
- `tests/markdown_browser_check.py:100`
- `tests/markdown_browser_check.py:101`
- `tests/markdown_browser_check.py:104`
- `tests/markdown_browser_check.py:117`
- `tests/markdown_browser_check.py:118`
- `tests/markdown_browser_check.py:126`
- `tests/test_llm_core_fallback.py:1026`
- `tests/test_rate_limiter.py:11`
- `tests/test_rate_limiter.py:12`
- `tests/test_rate_limiter.py:13`
- `tests/test_rate_limiter.py:18`
- `tests/test_rate_limiter.py:19`
- `tests/test_rate_limiter.py:23`
- `tests/test_rate_limiter.py:24`
- `tests/test_rate_limiter.py:25`
- `tests/test_rate_limiter.py:26`
- `tests/test_rate_limiter.py:32`
- `tests/test_rate_limiter.py:33`
- `tests/test_rate_limiter.py:35`
- `tests/test_rate_limiter.py:42`
- `tests/test_rate_limiter.py:45`
- `static/js/skills.js:1352`

## `RateLimiter._maybe_cleanup` — method, line 41
- **called from:**
- `src/rate_limiter.py:30`
