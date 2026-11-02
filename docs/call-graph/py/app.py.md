# `app.py` — definitions & call sites

51 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `register_static_mime_types` — function, line 18
- **called from:**
- `app.py:31`
- `tests/test_app_static_mime.py:24`

## `_RequestTimeoutMiddleware` — class, line 194
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_RequestTimeoutMiddleware.dispatch` — method (async), line 195
- **called from:**
- `tests/test_document_render_pdf_iframe.py:47`

## `_InteractiveActivityMiddleware` — class, line 208
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_InteractiveActivityMiddleware.dispatch` — method (async), line 209
- **called from:**
- `tests/test_document_render_pdf_iframe.py:47`

## `_InteractiveActivityMiddleware._stop_background` — method (async), line 215
- **called from:**
- `app.py:220`
- `app.py:664`

## `_SlowRequestLogMiddleware` — class, line 225
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_SlowRequestLogMiddleware.dispatch` — method (async), line 226
- **called from:**
- `tests/test_document_render_pdf_iframe.py:47`

## `_is_auth_exempt` — function, line 291
- **called from:**
- `app.py:375`

## `_token_cache_invalidate` — function, line 307
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_refresh_token_cache` — function, line 314
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_is_trusted_loopback` — function, line 347
- **called from:**
- `app.py:384`
- `app.py:404`

## `AuthMiddleware` — class, line 363
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AuthMiddleware.dispatch` — method (async), line 364
- **called from:**
- `tests/test_document_render_pdf_iframe.py:47`

## `AuthMiddleware._touch_last_used` — method (async), line 442
- **called from:**
- `app.py:456`

## `AuthMiddleware._do` — method, line 443
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_RevalidatingStatic` — class, line 493
- **called from:**
- `app.py:509`

## `_RevalidatingStatic.get_response` — method (async), line 502
- **called from:**
- `app.py:503`

## `serve_generated_image` — function (async), line 513
- **route:** `GET /api/generated-image/{filename}`
- decorator: `app.get("/api/generated-image/{filename}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `session_not_found_handler` — function (async), line 617
- decorator: `app.exception_handler(SessionNotFoundError)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `invalid_file_upload_handler` — function (async), line 621
- decorator: `app.exception_handler(InvalidFileUploadError)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `llm_service_error_handler` — function (async), line 625
- decorator: `app.exception_handler(LLMServiceError)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `web_search_error_handler` — function (async), line 629
- decorator: `app.exception_handler(WebSearchError)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `activity_heartbeat` — function (async), line 645
- **route:** `POST /api/activity/heartbeat`
- decorator: `app.post("/api/activity/heartbeat")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_stop_background` — function (async), line 653
- **called from:**
- `app.py:220`
- `app.py:664`

## `serve_index` — function (async), line 892
- **route:** `GET /`
- decorator: `app.get("/")`
- **called from:**
- `app.py:905`
- `app.py:909`
- `app.py:917`
- `app.py:921`
- `app.py:925`
- `app.py:929`
- `app.py:933`
- `app.py:937`

## `serve_notes` — function (async), line 904
- **route:** `GET /notes`
- decorator: `app.get("/notes")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_calendar` — function (async), line 908
- **route:** `GET /calendar`
- decorator: `app.get("/calendar")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_cookbook` — function (async), line 916
- **route:** `GET /cookbook`
- decorator: `app.get("/cookbook")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_email` — function (async), line 920
- **route:** `GET /email`
- decorator: `app.get("/email")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_memory` — function (async), line 924
- **route:** `GET /memory`
- decorator: `app.get("/memory")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_gallery` — function (async), line 928
- **route:** `GET /gallery`
- decorator: `app.get("/gallery")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_tasks` — function (async), line 932
- **route:** `GET /tasks`
- decorator: `app.get("/tasks")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_library` — function (async), line 936
- **route:** `GET /library`
- decorator: `app.get("/library")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_backgrounds` — function (async), line 940
- **route:** `GET /backgrounds`
- decorator: `app.get("/backgrounds")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_login` — function (async), line 945
- **route:** `GET /login`
- decorator: `app.get("/login")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_version` — function (async), line 951
- **route:** `GET /api/version`
- decorator: `app.get("/api/version")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `health_check` — function (async), line 956
- **route:** `GET /api/health`
- decorator: `app.get("/api/health")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `client_perf` — function (async), line 960
- **route:** `POST /api/client-perf`
- decorator: `app.post("/api/client-perf")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `readiness_check` — function (async), line 988
- **route:** `GET /api/ready`
- decorator: `app.get("/api/ready")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `runtime_info` — function (async), line 999
- **route:** `GET /api/runtime`
- decorator: `app.get("/api/runtime")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_lifespan` — function (async), line 1021
- decorator: `asynccontextmanager`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_startup_event` — function (async), line 1032
- **called from:**
- `app.py:1024`

## `_startup_mcp_connections` — function (async), line 1075
- **called from:**
- `app.py:1088`

## `_warmup_tool_index` — function (async), line 1095
- **called from:**
- `app.py:1105`

## `_warmup_endpoints` — function (async), line 1107
- **called from:**
- `app.py:1124`
- `app.py:1137`

## `_keepalive_loop` — function (async), line 1133
- **called from:**
- `app.py:1142`

## `_ensure_default_tasks` — function (async), line 1144
- **called from:**
- `app.py:1189`

## `_null_owner_sweep_loop` — function (async), line 1227
- **called from:**
- `app.py:1237`

## `_skill_audit_nightly_loop` — function (async), line 1244
- **called from:**
- `app.py:1267`

## `_shutdown_event` — function (async), line 1280
- **called from:**
- `app.py:1027`
