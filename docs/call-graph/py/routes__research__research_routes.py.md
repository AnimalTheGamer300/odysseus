# `routes/research/research_routes.py` — definitions & call sites

37 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_validate_session_id` — function, line 25
- **called from:**
- `routes/research/research_routes.py:37`
- `routes/research/research_routes.py:289`
- `routes/research/research_routes.py:324`
- `routes/research/research_routes.py:333`
- `routes/research/research_routes.py:377`
- `routes/research/research_routes.py:398`
- `routes/research/research_routes.py:409`
- `routes/research/research_routes.py:478`
- `routes/research/research_routes.py:493`
- `routes/research/research_routes.py:511`
- `routes/research/research_routes.py:663`
- `routes/research/research_routes.py:718`
- `routes/research/research_routes.py:768`

## `_research_storage_root` — function, line 31
- **called from:**
- `routes/research/research_routes.py:38`

## `_find_research_path` — function, line 35
- **called from:**
- `routes/research/research_routes.py:54`
- `routes/research/research_routes.py:61`
- `routes/research/research_routes.py:512`
- `tests/test_research_routes_path_confinement.py:72`
- `tests/test_research_routes_path_confinement.py:79`
- `tests/test_research_routes_path_confinement.py:108`
- `tests/test_research_routes_path_confinement.py:135`
- `tests/test_research_routes_path_confinement.py:152`

## `_require_research_path` — function, line 53
- **called from:**
- `routes/research/research_routes.py:365`
- `routes/research/research_routes.py:479`
- `routes/research/research_routes.py:494`
- `tests/test_research_routes_path_confinement.py:87`
- `tests/test_research_routes_path_confinement.py:382`

## `_find_owned_research_path` — function, line 60
- **called from:**
- `routes/research/research_routes.py:234`
- `routes/research/research_routes.py:251`
- `routes/research/research_routes.py:256`
- `tests/test_research_routes_path_confinement.py:161`
- `tests/test_research_routes_path_confinement.py:169`

## `_is_research_icon_or_logo_url` — function, line 89
- **called from:**
- `routes/research/research_routes.py:112`

## `_research_thumbnail` — function, line 97
- **called from:**
- `routes/research/research_routes.py:456`

## `usable` — function, line 102
- **called from:**
- `routes/research/research_routes.py:120`
- `routes/research/research_routes.py:127`

## `_first_chat_model` — function, line 133
- **called from:**
- `routes/model_routes.py:2386`
- `routes/research/research_routes.py:203`
- `src/editor_agent_model.py:547`
- `src/endpoint_resolver.py:522`
- `src/endpoint_resolver.py:582`
- `tests/test_endpoint_resolver_models.py:21`
- `tests/test_endpoint_resolver_models.py:24`
- `tests/test_endpoint_resolver_models.py:27`
- `tests/test_endpoint_resolver_models.py:53`
- `tests/test_endpoint_resolver_models.py:66`
- `tests/test_provider_endpoints_models.py:15`
- `tests/test_provider_endpoints_models.py:20`
- `tests/test_provider_endpoints_models.py:25`

## `_resolve_research_endpoint` — function, line 141
- **called from:**
- `routes/chat_routes.py:2518`
- `routes/chat_routes.py:4129`

## `_owned_enabled_endpoint` — function, line 154
- **called from:**
- `routes/research/research_routes.py:582`
- `routes/research/research_routes.py:611`
- `routes/research/research_routes.py:830`
- `tests/test_research_endpoint_owner_scope.py:88`

## `_resolve_endpoint_runtime` — function, line 178
- **called from:**
- `routes/research/research_routes.py:585`
- `routes/research/research_routes.py:613`
- `routes/research/research_routes.py:832`
- `tests/test_pinned_model_route_selection.py:91`
- `tests/test_pinned_model_route_selection.py:98`
- `tests/test_pinned_model_route_selection.py:103`
- `tests/test_pinned_model_route_selection.py:108`
- `tests/test_research_endpoint_owner_scope.py:159`

## `setup_research_routes` — function, line 211
- **called from:**
- `app.py:791`
- `tests/test_auth_regressions.py:183`
- `tests/test_auth_regressions.py:206`
- `tests/test_auth_regressions.py:224`
- `tests/test_auth_regressions.py:235`
- `tests/test_auth_regressions.py:246`
- `tests/test_auth_regressions.py:256`
- `tests/test_auth_regressions.py:270`
- `tests/test_auth_regressions.py:286`
- `tests/test_background_tool_jobs.py:135`
- `tests/test_rename_user_owner_sync.py:298`
- `tests/test_research_owner_scope_routes.py:58`
- `tests/test_research_owner_scope_routes.py:79`
- `tests/test_research_owner_scope_routes.py:94`
- `tests/test_research_owner_scope_routes.py:109`
- `tests/test_research_owner_scope_routes.py:124`
- `tests/test_research_routes_path_confinement.py:179`
- `tests/test_research_routes_path_confinement.py:186`
- `tests/test_research_routes_path_confinement.py:196`
- `tests/test_research_routes_path_confinement.py:219`
- `tests/test_research_routes_path_confinement.py:228`
- `tests/test_research_routes_path_confinement.py:237`
- `tests/test_research_routes_path_confinement.py:255`
- `tests/test_research_routes_path_confinement.py:270`
- `tests/test_research_routes_path_confinement.py:286`
- `tests/test_research_routes_path_confinement.py:321`
- `tests/test_research_routes_path_confinement.py:336`
- `tests/test_research_routes_path_confinement.py:359`
- `tests/test_research_routes_path_confinement.py:389`
- `tests/test_research_routes_path_confinement.py:398`
- `tests/test_research_routes_path_confinement.py:429`
- `tests/test_research_routes_path_confinement.py:496`
- `tests/test_research_routes_path_confinement.py:555`
- `tests/test_session_load_404s.py:39`
- `tests/test_session_load_404s.py:56`

## `_require_user` — function, line 214
- **called from:**
- `routes/calendar_routes.py:984`
- `routes/calendar_routes.py:1008`
- `routes/calendar_routes.py:1038`
- `routes/calendar_routes.py:1063`
- `routes/calendar_routes.py:1088`
- `routes/calendar_routes.py:1115`
- `routes/calendar_routes.py:1129`
- `routes/calendar_routes.py:1228`
- `routes/calendar_routes.py:1235`
- `routes/calendar_routes.py:1255`
- `routes/calendar_routes.py:1278`
- `routes/calendar_routes.py:1344`
- `routes/calendar_routes.py:1415`
- `routes/calendar_routes.py:1426`
- `routes/calendar_routes.py:1489`
- `routes/calendar_routes.py:1534`
- `routes/calendar_routes.py:1557`
- `routes/calendar_routes.py:1587`
- `routes/calendar_routes.py:1741`
- `routes/calendar_routes.py:1806`
- `routes/research/research_routes.py:264`
- `routes/research/research_routes.py:288`
- `routes/research/research_routes.py:323`
- `routes/research/research_routes.py:332`
- `routes/research/research_routes.py:376`
- `routes/research/research_routes.py:397`
- `routes/research/research_routes.py:408`
- `routes/research/research_routes.py:424`
- `routes/research/research_routes.py:477`
- `routes/research/research_routes.py:492`
- `routes/research/research_routes.py:510`
- `routes/research/research_routes.py:655`
- `routes/research/research_routes.py:662`
- `routes/research/research_routes.py:717`
- `routes/research/research_routes.py:767`

## `_owns_in_memory` — function, line 226
- **called from:**
- `routes/research/research_routes.py:296`
- `routes/research/research_routes.py:325`
- `routes/research/research_routes.py:334`
- `routes/research/research_routes.py:664`

## `_require_owned_or_active_research_path` — function, line 238
- **called from:**
- `routes/research/research_routes.py:719`
- `routes/research/research_routes.py:773`

## `research_active` — function (async), line 262
- **route:** `GET /api/research/active`
- decorator: `router.get("/api/research/active")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_status` — function (async), line 287
- **route:** `GET /api/research/status/{session_id}`
- decorator: `router.get("/api/research/status/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_cancel` — function (async), line 322
- **route:** `POST /api/research/cancel/{session_id}`
- decorator: `router.post("/api/research/cancel/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_result` — function (async), line 331
- **route:** `POST /api/research/result/{session_id}`
- decorator: `router.post("/api/research/result/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_assert_owns_research` — function, line 362
- **called from:**
- `routes/research/research_routes.py:378`
- `routes/research/research_routes.py:399`
- `routes/research/research_routes.py:410`

## `research_report` — function (async), line 374
- **route:** `GET /api/research/report/{session_id}`
- decorator: `router.get("/api/research/report/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `HideImageRequest` — class, line 390
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_hide_image` — function (async), line 394
- **route:** `POST /api/research/{session_id}/hide-image`
- decorator: `router.post("/api/research/{session_id}/hide-image")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_unhide_images` — function (async), line 406
- **route:** `POST /api/research/{session_id}/unhide-images`
- decorator: `router.post("/api/research/{session_id}/unhide-images")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_library` — function (async), line 417
- **route:** `GET /api/research/library`
- decorator: `router.get("/api/research/library")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_detail` — function (async), line 474
- **route:** `GET /api/research/detail/{session_id}`
- decorator: `router.get("/api/research/detail/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_archive` — function (async), line 490
- **route:** `POST /api/research/{session_id}/archive`
- decorator: `router.post("/api/research/{session_id}/archive")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_delete` — function (async), line 508
- **route:** `DELETE /api/research/{session_id}`
- decorator: `router.delete("/api/research/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResearchStartRequest` — class, line 532
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_start` — function (async), line 546
- **route:** `POST /api/research/start`
- decorator: `router.post("/api/research/start")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `chat_research_jobs` — function (async), line 654
- **route:** `GET /api/research/chat-jobs/{chat_id}`
- decorator: `router.get('/api/research/chat-jobs/{chat_id}')`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_stream` — function (async), line 660
- **route:** `GET /api/research/stream/{session_id}`
- decorator: `router.get("/api/research/stream/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_generate` — function (async), line 666
- **called from:**
- `routes/research/research_routes.py:709`

## `research_result_peek` — function (async), line 715
- **route:** `POST /api/research/result-peek/{session_id}`
- decorator: `router.post("/api/research/result-peek/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_spinoff` — function (async), line 758
- **route:** `POST /api/research/spinoff/{session_id}`
- decorator: `router.post("/api/research/spinoff/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_merge` — function, line 810
- **called from:**
- `routes/research/research_routes.py:820`
- `routes/research/research_routes.py:822`
- `routes/research/research_routes.py:824`
- `routes/research/research_routes.py:834`
