# `routes/research/research_routes.py` — definitions & call sites

36 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_validate_session_id` — function, line 24
- **called from:**
- `routes/research/research_routes.py:36`
- `routes/research/research_routes.py:281`
- `routes/research/research_routes.py:292`
- `routes/research/research_routes.py:301`
- `routes/research/research_routes.py:327`
- `routes/research/research_routes.py:348`
- `routes/research/research_routes.py:359`
- `routes/research/research_routes.py:426`
- `routes/research/research_routes.py:441`
- `routes/research/research_routes.py:459`
- `routes/research/research_routes.py:583`
- `routes/research/research_routes.py:617`
- `routes/research/research_routes.py:646`

## `_research_storage_root` — function, line 30
- **called from:**
- `routes/research/research_routes.py:37`

## `_find_research_path` — function, line 34
- **called from:**
- `routes/research/research_routes.py:53`
- `routes/research/research_routes.py:60`
- `routes/research/research_routes.py:460`
- `tests/test_research_routes_path_confinement.py:72`
- `tests/test_research_routes_path_confinement.py:79`
- `tests/test_research_routes_path_confinement.py:108`
- `tests/test_research_routes_path_confinement.py:135`
- `tests/test_research_routes_path_confinement.py:152`

## `_require_research_path` — function, line 52
- **called from:**
- `routes/research/research_routes.py:315`
- `routes/research/research_routes.py:427`
- `routes/research/research_routes.py:442`
- `tests/test_research_routes_path_confinement.py:87`
- `tests/test_research_routes_path_confinement.py:382`

## `_find_owned_research_path` — function, line 59
- **called from:**
- `routes/research/research_routes.py:232`
- `routes/research/research_routes.py:249`
- `routes/research/research_routes.py:254`
- `tests/test_research_routes_path_confinement.py:161`
- `tests/test_research_routes_path_confinement.py:169`

## `_is_research_icon_or_logo_url` — function, line 88
- **called from:**
- `routes/research/research_routes.py:111`

## `_research_thumbnail` — function, line 96
- **called from:**
- `routes/research/research_routes.py:404`

## `usable` — function, line 101
- **called from:**
- `routes/research/research_routes.py:119`
- `routes/research/research_routes.py:126`

## `_first_chat_model` — function, line 132
- **called from:**
- `routes/model_routes.py:2203`
- `routes/research/research_routes.py:201`
- `routes/research/research_routes.py:719`
- `src/endpoint_resolver.py:425`
- `src/endpoint_resolver.py:485`
- `tests/test_endpoint_resolver_models.py:21`
- `tests/test_endpoint_resolver_models.py:24`
- `tests/test_endpoint_resolver_models.py:27`
- `tests/test_endpoint_resolver_models.py:53`
- `tests/test_endpoint_resolver_models.py:66`
- `tests/test_provider_endpoints_models.py:15`
- `tests/test_provider_endpoints_models.py:20`
- `tests/test_provider_endpoints_models.py:25`

## `_resolve_research_endpoint` — function, line 140
- **called from:**
- `routes/chat_routes.py:1008`
- `routes/chat_routes.py:1858`

## `_owned_enabled_endpoint` — function, line 153
- **called from:**
- `routes/research/research_routes.py:520`
- `routes/research/research_routes.py:549`
- `routes/research/research_routes.py:709`
- `tests/test_research_endpoint_owner_scope.py:82`

## `_resolve_endpoint_runtime` — function, line 177
- **called from:**
- `routes/research/research_routes.py:523`
- `routes/research/research_routes.py:551`
- `tests/test_research_endpoint_owner_scope.py:153`

## `setup_research_routes` — function, line 209
- **called from:**
- `app.py:712`
- `tests/test_auth_regressions.py:181`
- `tests/test_auth_regressions.py:204`
- `tests/test_auth_regressions.py:222`
- `tests/test_auth_regressions.py:233`
- `tests/test_auth_regressions.py:243`
- `tests/test_auth_regressions.py:253`
- `tests/test_auth_regressions.py:267`
- `tests/test_auth_regressions.py:283`
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

## `_require_user` — function, line 212
- **called from:**
- `routes/calendar_routes.py:835`
- `routes/calendar_routes.py:859`
- `routes/calendar_routes.py:892`
- `routes/calendar_routes.py:917`
- `routes/calendar_routes.py:945`
- `routes/calendar_routes.py:975`
- `routes/calendar_routes.py:989`
- `routes/calendar_routes.py:1091`
- `routes/calendar_routes.py:1098`
- `routes/calendar_routes.py:1118`
- `routes/calendar_routes.py:1141`
- `routes/calendar_routes.py:1207`
- `routes/calendar_routes.py:1269`
- `routes/calendar_routes.py:1321`
- `routes/calendar_routes.py:1363`
- `routes/calendar_routes.py:1386`
- `routes/calendar_routes.py:1416`
- `routes/calendar_routes.py:1566`
- `routes/calendar_routes.py:1631`
- `routes/research/research_routes.py:262`
- `routes/research/research_routes.py:280`
- `routes/research/research_routes.py:291`
- `routes/research/research_routes.py:300`
- `routes/research/research_routes.py:326`
- `routes/research/research_routes.py:347`
- `routes/research/research_routes.py:358`
- `routes/research/research_routes.py:374`
- `routes/research/research_routes.py:425`
- `routes/research/research_routes.py:440`
- `routes/research/research_routes.py:458`
- `routes/research/research_routes.py:582`
- `routes/research/research_routes.py:616`
- `routes/research/research_routes.py:645`

## `_owns_in_memory` — function, line 224
- **called from:**
- `routes/research/research_routes.py:282`
- `routes/research/research_routes.py:293`
- `routes/research/research_routes.py:302`
- `routes/research/research_routes.py:584`

## `_require_owned_or_active_research_path` — function, line 236
- **called from:**
- `routes/research/research_routes.py:618`
- `routes/research/research_routes.py:651`

## `research_active` — function (async), line 260
- **route:** `GET /api/research/active`
- decorator: `router.get("/api/research/active")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_status` — function (async), line 279
- **route:** `GET /api/research/status/{session_id}`
- decorator: `router.get("/api/research/status/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_cancel` — function (async), line 290
- **route:** `POST /api/research/cancel/{session_id}`
- decorator: `router.post("/api/research/cancel/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_result` — function (async), line 299
- **route:** `POST /api/research/result/{session_id}`
- decorator: `router.post("/api/research/result/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_assert_owns_research` — function, line 312
- **called from:**
- `routes/research/research_routes.py:328`
- `routes/research/research_routes.py:349`
- `routes/research/research_routes.py:360`

## `research_report` — function (async), line 324
- **route:** `GET /api/research/report/{session_id}`
- decorator: `router.get("/api/research/report/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `HideImageRequest` — class, line 340
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_hide_image` — function (async), line 344
- **route:** `POST /api/research/{session_id}/hide-image`
- decorator: `router.post("/api/research/{session_id}/hide-image")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_unhide_images` — function (async), line 356
- **route:** `POST /api/research/{session_id}/unhide-images`
- decorator: `router.post("/api/research/{session_id}/unhide-images")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_library` — function (async), line 367
- **route:** `GET /api/research/library`
- decorator: `router.get("/api/research/library")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_detail` — function (async), line 422
- **route:** `GET /api/research/detail/{session_id}`
- decorator: `router.get("/api/research/detail/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_archive` — function (async), line 438
- **route:** `POST /api/research/{session_id}/archive`
- decorator: `router.post("/api/research/{session_id}/archive")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_delete` — function (async), line 456
- **route:** `DELETE /api/research/{session_id}`
- decorator: `router.delete("/api/research/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResearchStartRequest` — class, line 480
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_start` — function (async), line 493
- **route:** `POST /api/research/start`
- decorator: `router.post("/api/research/start")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_stream` — function (async), line 580
- **route:** `GET /api/research/stream/{session_id}`
- decorator: `router.get("/api/research/stream/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_generate` — function (async), line 586
- **called from:**
- `routes/research/research_routes.py:608`

## `research_result_peek` — function (async), line 614
- **route:** `POST /api/research/result-peek/{session_id}`
- decorator: `router.post("/api/research/result-peek/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `research_spinoff` — function (async), line 636
- **route:** `POST /api/research/spinoff/{session_id}`
- decorator: `router.post("/api/research/spinoff/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_merge` — function, line 688
- **called from:**
- `routes/research/research_routes.py:698`
- `routes/research/research_routes.py:700`
- `routes/research/research_routes.py:702`
- `routes/research/research_routes.py:722`
