# `app.py` — definitions & call sites

53 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `register_static_mime_types` — function, line 20
- **called from:**
- `app.py:33`
- `tests/test_app_static_mime.py:24`

## `_RequestTimeoutMiddleware` — class, line 206
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_RequestTimeoutMiddleware.dispatch` — method (async), line 207
- **called from:**
- `tests/test_browser_identity_transport.py:86`
- `tests/test_browser_identity_transport.py:101`
- `tests/test_browser_identity_transport.py:110`
- `tests/test_browser_identity_transport.py:132`
- `tests/test_browser_identity_transport.py:157`
- `tests/test_browser_resource_identity.py:128`
- `tests/test_browser_resource_identity.py:257`
- `tests/test_browser_resource_identity.py:260`
- `tests/test_browser_resource_identity.py:273`
- `tests/test_browser_resource_identity.py:286`
- `tests/test_document_render_pdf_iframe.py:47`
- `tests/test_owned_resource_identity.py:100`
- `tests/test_owned_resource_identity.py:113`
- `tests/test_owned_resource_identity.py:146`
- `tests/test_owned_resource_identity.py:155`
- `tests/test_owned_resource_identity.py:169`
- `tests/test_owned_resource_identity.py:171`
- `tests/test_owned_resource_identity.py:172`
- `tests/test_owned_resource_identity.py:185`
- `tests/test_owned_resource_identity.py:188`
- `tests/test_owned_resource_identity.py:189`
- `tests/test_owned_resource_identity.py:300`
- `tests/test_owned_resource_identity.py:302`
- `tests/test_owned_resource_identity.py:314`
- `tests/test_owned_resource_identity.py:350`
- `tests/test_owned_resource_identity.py:384`
- `tests/test_owned_resource_identity.py:399`
- `tests/test_owned_resource_identity.py:402`
- `tests/test_owned_resource_identity.py:409`
- `tests/test_remote_resource_identity.py:69`
- `tests/test_remote_resource_identity.py:77`
- `tests/test_remote_resource_identity.py:80`
- `tests/test_remote_resource_identity.py:100`
- `tests/test_remote_resource_identity.py:122`
- `tests/test_remote_resource_identity.py:134`
- `tests/test_remote_resource_identity.py:136`
- `tests/test_remote_resource_identity.py:148`
- `tests/test_remote_resource_identity.py:190`
- `tests/test_remote_resource_identity.py:223`
- `tests/test_remote_resource_identity.py:246`
- `tests/test_remote_resource_identity.py:248`
- `tests/test_remote_resource_identity.py:253`
- `tests/test_remote_resource_identity.py:261`
- `tests/test_remote_resource_identity.py:266`
- `tests/test_remote_resource_identity.py:269`
- `tests/test_remote_resource_identity.py:287`
- `tests/test_remote_resource_identity.py:304`
- `tests/test_remote_resource_identity.py:317`
- `tests/test_remote_resource_identity.py:328`
- `tests/test_remote_resource_identity.py:337`
- `tests/test_remote_resource_identity.py:355`
- `tests/test_remote_resource_identity.py:367`
- `tests/test_remote_resource_identity.py:377`
- `tests/test_remote_resource_identity.py:392`
- `tests/test_remote_resource_identity.py:397`
- `tests/test_resource_identity.py:166`
- `tests/test_resource_identity.py:201`
- `tests/test_resource_identity.py:213`
- `tests/test_resource_identity.py:224`
- `tests/test_resource_identity.py:254`
- … +51 more (grep the name in repo)

## `_InteractiveActivityMiddleware` — class, line 220
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_InteractiveActivityMiddleware.dispatch` — method (async), line 221
- **called from:**
- `tests/test_browser_identity_transport.py:86`
- `tests/test_browser_identity_transport.py:101`
- `tests/test_browser_identity_transport.py:110`
- `tests/test_browser_identity_transport.py:132`
- `tests/test_browser_identity_transport.py:157`
- `tests/test_browser_resource_identity.py:128`
- `tests/test_browser_resource_identity.py:257`
- `tests/test_browser_resource_identity.py:260`
- `tests/test_browser_resource_identity.py:273`
- `tests/test_browser_resource_identity.py:286`
- `tests/test_document_render_pdf_iframe.py:47`
- `tests/test_owned_resource_identity.py:100`
- `tests/test_owned_resource_identity.py:113`
- `tests/test_owned_resource_identity.py:146`
- `tests/test_owned_resource_identity.py:155`
- `tests/test_owned_resource_identity.py:169`
- `tests/test_owned_resource_identity.py:171`
- `tests/test_owned_resource_identity.py:172`
- `tests/test_owned_resource_identity.py:185`
- `tests/test_owned_resource_identity.py:188`
- `tests/test_owned_resource_identity.py:189`
- `tests/test_owned_resource_identity.py:300`
- `tests/test_owned_resource_identity.py:302`
- `tests/test_owned_resource_identity.py:314`
- `tests/test_owned_resource_identity.py:350`
- `tests/test_owned_resource_identity.py:384`
- `tests/test_owned_resource_identity.py:399`
- `tests/test_owned_resource_identity.py:402`
- `tests/test_owned_resource_identity.py:409`
- `tests/test_remote_resource_identity.py:69`
- `tests/test_remote_resource_identity.py:77`
- `tests/test_remote_resource_identity.py:80`
- `tests/test_remote_resource_identity.py:100`
- `tests/test_remote_resource_identity.py:122`
- `tests/test_remote_resource_identity.py:134`
- `tests/test_remote_resource_identity.py:136`
- `tests/test_remote_resource_identity.py:148`
- `tests/test_remote_resource_identity.py:190`
- `tests/test_remote_resource_identity.py:223`
- `tests/test_remote_resource_identity.py:246`
- `tests/test_remote_resource_identity.py:248`
- `tests/test_remote_resource_identity.py:253`
- `tests/test_remote_resource_identity.py:261`
- `tests/test_remote_resource_identity.py:266`
- `tests/test_remote_resource_identity.py:269`
- `tests/test_remote_resource_identity.py:287`
- `tests/test_remote_resource_identity.py:304`
- `tests/test_remote_resource_identity.py:317`
- `tests/test_remote_resource_identity.py:328`
- `tests/test_remote_resource_identity.py:337`
- `tests/test_remote_resource_identity.py:355`
- `tests/test_remote_resource_identity.py:367`
- `tests/test_remote_resource_identity.py:377`
- `tests/test_remote_resource_identity.py:392`
- `tests/test_remote_resource_identity.py:397`
- `tests/test_resource_identity.py:166`
- `tests/test_resource_identity.py:201`
- `tests/test_resource_identity.py:213`
- `tests/test_resource_identity.py:224`
- `tests/test_resource_identity.py:254`
- … +51 more (grep the name in repo)

## `_InteractiveActivityMiddleware._stop_background` — method (async), line 227
- **called from:**
- `app.py:232`
- `app.py:742`

## `_SlowRequestLogMiddleware` — class, line 254
- **called from:**
- `tests/test_stream_disconnect_middleware.py:20`
- `tests/test_stream_disconnect_middleware.py:31`

## `_SlowRequestLogMiddleware.dispatch` — method (async), line 255
- **called from:**
- `tests/test_browser_identity_transport.py:86`
- `tests/test_browser_identity_transport.py:101`
- `tests/test_browser_identity_transport.py:110`
- `tests/test_browser_identity_transport.py:132`
- `tests/test_browser_identity_transport.py:157`
- `tests/test_browser_resource_identity.py:128`
- `tests/test_browser_resource_identity.py:257`
- `tests/test_browser_resource_identity.py:260`
- `tests/test_browser_resource_identity.py:273`
- `tests/test_browser_resource_identity.py:286`
- `tests/test_document_render_pdf_iframe.py:47`
- `tests/test_owned_resource_identity.py:100`
- `tests/test_owned_resource_identity.py:113`
- `tests/test_owned_resource_identity.py:146`
- `tests/test_owned_resource_identity.py:155`
- `tests/test_owned_resource_identity.py:169`
- `tests/test_owned_resource_identity.py:171`
- `tests/test_owned_resource_identity.py:172`
- `tests/test_owned_resource_identity.py:185`
- `tests/test_owned_resource_identity.py:188`
- `tests/test_owned_resource_identity.py:189`
- `tests/test_owned_resource_identity.py:300`
- `tests/test_owned_resource_identity.py:302`
- `tests/test_owned_resource_identity.py:314`
- `tests/test_owned_resource_identity.py:350`
- `tests/test_owned_resource_identity.py:384`
- `tests/test_owned_resource_identity.py:399`
- `tests/test_owned_resource_identity.py:402`
- `tests/test_owned_resource_identity.py:409`
- `tests/test_remote_resource_identity.py:69`
- `tests/test_remote_resource_identity.py:77`
- `tests/test_remote_resource_identity.py:80`
- `tests/test_remote_resource_identity.py:100`
- `tests/test_remote_resource_identity.py:122`
- `tests/test_remote_resource_identity.py:134`
- `tests/test_remote_resource_identity.py:136`
- `tests/test_remote_resource_identity.py:148`
- `tests/test_remote_resource_identity.py:190`
- `tests/test_remote_resource_identity.py:223`
- `tests/test_remote_resource_identity.py:246`
- `tests/test_remote_resource_identity.py:248`
- `tests/test_remote_resource_identity.py:253`
- `tests/test_remote_resource_identity.py:261`
- `tests/test_remote_resource_identity.py:266`
- `tests/test_remote_resource_identity.py:269`
- `tests/test_remote_resource_identity.py:287`
- `tests/test_remote_resource_identity.py:304`
- `tests/test_remote_resource_identity.py:317`
- `tests/test_remote_resource_identity.py:328`
- `tests/test_remote_resource_identity.py:337`
- `tests/test_remote_resource_identity.py:355`
- `tests/test_remote_resource_identity.py:367`
- `tests/test_remote_resource_identity.py:377`
- `tests/test_remote_resource_identity.py:392`
- `tests/test_remote_resource_identity.py:397`
- `tests/test_resource_identity.py:166`
- `tests/test_resource_identity.py:201`
- `tests/test_resource_identity.py:213`
- `tests/test_resource_identity.py:224`
- `tests/test_resource_identity.py:254`
- … +51 more (grep the name in repo)

## `_is_auth_exempt` — function, line 331
- **called from:**
- `app.py:416`

## `_token_cache_invalidate` — function, line 347
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_refresh_token_cache` — function, line 354
- **called from:**
- `tests/test_token_cache_atomic_swap.py:61`
- `tests/test_token_cache_atomic_swap.py:72`
- `tests/test_token_cache_atomic_swap.py:81`
- `tests/test_token_cache_atomic_swap.py:91`
- `tests/test_token_cache_atomic_swap.py:98`
- `tests/test_token_cache_atomic_swap.py:109`
- `tests/test_token_cache_atomic_swap.py:123`
- `tests/test_token_cache_atomic_swap.py:148`
- `tests/test_token_cache_atomic_swap.py:166`
- `tests/test_token_cache_atomic_swap.py:168`
- `tests/test_token_cache_atomic_swap.py:209`
- `tests/test_token_cache_atomic_swap.py:217`
- `tests/test_token_cache_atomic_swap.py:228`
- `tests/test_token_cache_atomic_swap.py:230`

## `_is_trusted_loopback` — function, line 388
- **called from:**
- `app.py:425`
- `app.py:445`

## `AuthMiddleware` — class, line 404
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AuthMiddleware.dispatch` — method (async), line 405
- **called from:**
- `tests/test_browser_identity_transport.py:86`
- `tests/test_browser_identity_transport.py:101`
- `tests/test_browser_identity_transport.py:110`
- `tests/test_browser_identity_transport.py:132`
- `tests/test_browser_identity_transport.py:157`
- `tests/test_browser_resource_identity.py:128`
- `tests/test_browser_resource_identity.py:257`
- `tests/test_browser_resource_identity.py:260`
- `tests/test_browser_resource_identity.py:273`
- `tests/test_browser_resource_identity.py:286`
- `tests/test_document_render_pdf_iframe.py:47`
- `tests/test_owned_resource_identity.py:100`
- `tests/test_owned_resource_identity.py:113`
- `tests/test_owned_resource_identity.py:146`
- `tests/test_owned_resource_identity.py:155`
- `tests/test_owned_resource_identity.py:169`
- `tests/test_owned_resource_identity.py:171`
- `tests/test_owned_resource_identity.py:172`
- `tests/test_owned_resource_identity.py:185`
- `tests/test_owned_resource_identity.py:188`
- `tests/test_owned_resource_identity.py:189`
- `tests/test_owned_resource_identity.py:300`
- `tests/test_owned_resource_identity.py:302`
- `tests/test_owned_resource_identity.py:314`
- `tests/test_owned_resource_identity.py:350`
- `tests/test_owned_resource_identity.py:384`
- `tests/test_owned_resource_identity.py:399`
- `tests/test_owned_resource_identity.py:402`
- `tests/test_owned_resource_identity.py:409`
- `tests/test_remote_resource_identity.py:69`
- `tests/test_remote_resource_identity.py:77`
- `tests/test_remote_resource_identity.py:80`
- `tests/test_remote_resource_identity.py:100`
- `tests/test_remote_resource_identity.py:122`
- `tests/test_remote_resource_identity.py:134`
- `tests/test_remote_resource_identity.py:136`
- `tests/test_remote_resource_identity.py:148`
- `tests/test_remote_resource_identity.py:190`
- `tests/test_remote_resource_identity.py:223`
- `tests/test_remote_resource_identity.py:246`
- `tests/test_remote_resource_identity.py:248`
- `tests/test_remote_resource_identity.py:253`
- `tests/test_remote_resource_identity.py:261`
- `tests/test_remote_resource_identity.py:266`
- `tests/test_remote_resource_identity.py:269`
- `tests/test_remote_resource_identity.py:287`
- `tests/test_remote_resource_identity.py:304`
- `tests/test_remote_resource_identity.py:317`
- `tests/test_remote_resource_identity.py:328`
- `tests/test_remote_resource_identity.py:337`
- `tests/test_remote_resource_identity.py:355`
- `tests/test_remote_resource_identity.py:367`
- `tests/test_remote_resource_identity.py:377`
- `tests/test_remote_resource_identity.py:392`
- `tests/test_remote_resource_identity.py:397`
- `tests/test_resource_identity.py:166`
- `tests/test_resource_identity.py:201`
- `tests/test_resource_identity.py:213`
- `tests/test_resource_identity.py:224`
- `tests/test_resource_identity.py:254`
- … +51 more (grep the name in repo)

## `AuthMiddleware._touch_last_used` — method (async), line 483
- **called from:**
- `app.py:497`

## `AuthMiddleware._do` — method, line 484
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_RevalidatingStatic` — class, line 534
- **called from:**
- `app.py:550`

## `_RevalidatingStatic.get_response` — method (async), line 543
- **called from:**
- `app.py:544`

## `serve_generated_image` — function (async), line 554
- **route:** `GET /api/generated-image/{filename}`
- decorator: `app.get("/api/generated-image/{filename}")`
- **called from:**
- `tests/test_generated_image_ownership.py:53`
- `tests/test_generated_image_ownership.py:73`
- `tests/test_generated_image_ownership.py:92`
- `tests/test_generated_image_ownership.py:112`
- `tests/test_generated_image_ownership.py:123`
- `tests/test_generated_image_ownership.py:143`
- `tests/test_generated_image_ownership.py:164`
- `tests/test_generated_image_ownership.py:192`
- `tests/test_generated_image_ownership.py:197`
- `tests/test_generated_image_ownership.py:219`
- `tests/test_generated_image_ownership.py:223`
- `tests/test_generated_image_ownership.py:245`
- `tests/test_generated_image_ownership.py:250`
- `tests/test_generated_image_ownership.py:266`
- `tests/test_generated_image_ownership.py:277`
- `tests/test_generated_image_ownership.py:281`
- `tests/test_generated_image_ownership.py:304`
- `tests/test_generated_image_ownership.py:309`

## `session_not_found_handler` — function (async), line 695
- decorator: `app.exception_handler(SessionNotFoundError)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `invalid_file_upload_handler` — function (async), line 699
- decorator: `app.exception_handler(InvalidFileUploadError)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `llm_service_error_handler` — function (async), line 703
- decorator: `app.exception_handler(LLMServiceError)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `web_search_error_handler` — function (async), line 707
- decorator: `app.exception_handler(WebSearchError)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `activity_heartbeat` — function (async), line 723
- **route:** `POST /api/activity/heartbeat`
- decorator: `app.post("/api/activity/heartbeat")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_stop_background` — function (async), line 731
- **called from:**
- `app.py:232`
- `app.py:742`

## `serve_index` — function (async), line 977
- **route:** `GET /`
- decorator: `app.get("/")`
- **called from:**
- `app.py:990`
- `app.py:994`
- `app.py:1002`
- `app.py:1006`
- `app.py:1010`
- `app.py:1014`
- `app.py:1018`
- `app.py:1022`

## `serve_notes` — function (async), line 989
- **route:** `GET /notes`
- decorator: `app.get("/notes")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_calendar` — function (async), line 993
- **route:** `GET /calendar`
- decorator: `app.get("/calendar")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_cookbook` — function (async), line 1001
- **route:** `GET /cookbook`
- decorator: `app.get("/cookbook")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_email` — function (async), line 1005
- **route:** `GET /email`
- decorator: `app.get("/email")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_memory` — function (async), line 1009
- **route:** `GET /memory`
- decorator: `app.get("/memory")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_gallery` — function (async), line 1013
- **route:** `GET /gallery`
- decorator: `app.get("/gallery")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_tasks` — function (async), line 1017
- **route:** `GET /tasks`
- decorator: `app.get("/tasks")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_library` — function (async), line 1021
- **route:** `GET /library`
- decorator: `app.get("/library")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_backgrounds` — function (async), line 1025
- **route:** `GET /backgrounds`
- decorator: `app.get("/backgrounds")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `serve_login` — function (async), line 1030
- **route:** `GET /login`
- decorator: `app.get("/login")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_version` — function (async), line 1036
- **route:** `GET /api/version`
- decorator: `app.get("/api/version")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_busy` — function (async), line 1046
- **route:** `GET /api/busy`
- decorator: `app.get("/api/busy")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `health_check` — function (async), line 1055
- **route:** `GET /api/health`
- decorator: `app.get("/api/health")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `client_perf` — function (async), line 1059
- **route:** `POST /api/client-perf`
- decorator: `app.post("/api/client-perf")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `readiness_check` — function (async), line 1087
- **route:** `GET /api/ready`
- decorator: `app.get("/api/ready")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `runtime_info` — function (async), line 1098
- **route:** `GET /api/runtime`
- decorator: `app.get("/api/runtime")`
- **called from:**
- `tests/test_runtime_info_route.py:18`
- `tests/test_runtime_info_route.py:46`
- `tests/test_runtime_info_route.py:71`
- `tests/test_runtime_info_route.py:96`

## `_docker_default_gateway_ip` — function, line 1166
- **called from:**
- `app.py:1128`

## `_lifespan` — function (async), line 1185
- decorator: `asynccontextmanager`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_startup_event` — function (async), line 1196
- **called from:**
- `app.py:1188`

## `_startup_mcp_connections` — function (async), line 1248
- **called from:**
- `app.py:1261`

## `_warmup_tool_index` — function (async), line 1268
- **called from:**
- `app.py:1283`

## `_warmup_endpoints` — function (async), line 1291
- **called from:**
- `app.py:1308`
- `app.py:1321`

## `_keepalive_loop` — function (async), line 1317
- **called from:**
- `app.py:1326`

## `_ensure_default_tasks` — function (async), line 1328
- **called from:**
- `app.py:1373`

## `_null_owner_sweep_loop` — function (async), line 1419
- **called from:**
- `app.py:1429`

## `_shutdown_event` — function (async), line 1455
- **called from:**
- `app.py:1191`

## `_handle_shutdown_signal` — function, line 1524
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
