# `routes/upload_routes.py` — definitions & call sites

21 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_upload_ids_from_persisted_text` — function, line 43
- **called from:**
- `routes/upload_routes.py:83`
- `routes/upload_routes.py:103`
- `routes/upload_routes.py:107`
- `routes/upload_routes.py:110`
- `routes/upload_routes.py:116`
- `routes/upload_routes.py:127`
- `routes/upload_routes.py:130`
- `routes/upload_routes.py:138`

## `_upload_ids_from_message_metadata` — function, line 54
- **called from:**
- `routes/upload_routes.py:104`

## `_collect_persisted_upload_references` — function, line 87
- **called from:**
- `routes/upload_routes.py:146`
- `tests/test_upload_handler_cleanup.py:547`

## `_run_reference_safe_cleanup` — function, line 145
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_upload_routes` — function, line 152
- **called from:**
- `app.py:748`
- `tests/test_upload_confinement_compatibility.py:49`
- `tests/test_upload_handler_cleanup.py:99`
- `tests/test_upload_head_contract.py:79`
- `tests/test_upload_multifile.py:106`
- `tests/test_upload_multifile.py:116`
- `tests/test_upload_multifile.py:130`
- `tests/test_upload_multifile.py:191`
- `tests/test_upload_multifile.py:222`
- `tests/test_upload_no_login.py:37`
- `tests/test_upload_no_login.py:410`
- `tests/test_upload_no_login.py:491`
- `tests/test_upload_no_login.py:629`
- `tests/test_upload_no_login.py:728`
- `tests/test_upload_no_login.py:776`
- `tests/test_upload_no_login.py:816`
- `tests/test_upload_no_login.py:849`
- `tests/test_upload_routes_owner_scope.py:38`

## `_upload_root` — function, line 155
- **called from:**
- `routes/upload_routes.py:160`
- `routes/upload_routes.py:166`
- `routes/upload_routes.py:476`
- `routes/upload_routes.py:545`

## `_path_inside_upload_dir` — function, line 159
- **called from:**
- `routes/upload_routes.py:482`
- `routes/upload_routes.py:495`

## `_resolve_upload_path` — function, line 162
- **called from:**
- `routes/upload_routes.py:477`
- `routes/upload_routes.py:586`
- `routes/upload_routes.py:626`

## `_verify_upload_access` — function, line 202
- **called from:**
- `routes/upload_routes.py:475`
- `routes/upload_routes.py:584`
- `routes/upload_routes.py:624`

## `_valid_session_id_for_owner` — function, line 248
- **called from:**
- `routes/upload_routes.py:323`

## `_promote_chat_image_to_gallery` — function, line 258
- **called from:**
- `routes/upload_routes.py:395`

## `api_upload` — function (async), line 339
- decorator: `router.post("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `manual_cleanup` — function (async), line 424
- **route:** `POST /cleanup`
- decorator: `router.post("/cleanup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `upload_stats` — function (async), line 447
- **route:** `GET /stats`
- decorator: `router.get("/stats")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `download_file` — function (async), line 457
- **route:** `API_ROUTE /{file_id}`
- decorator: `router.api_route("/{file_id}", methods=["GET", "HEAD"])`
- **called from:**
- `tests/test_upload_routes_owner_scope.py:128`
- `tests/test_upload_routes_owner_scope.py:138`
- `tests/test_upload_routes_owner_scope.py:148`
- `tests/test_upload_routes_owner_scope.py:161`
- `tests/test_upload_routes_owner_scope.py:181`
- `tests/test_upload_routes_owner_scope.py:200`
- `tests/test_upload_routes_owner_scope.py:327`

## `_load_upload_info` — function, line 536
- **called from:**
- `routes/upload_routes.py:178`
- `routes/upload_routes.py:582`
- `routes/upload_routes.py:620`

## `_vision_cache_path` — function, line 543
- **called from:**
- `routes/upload_routes.py:591`
- `routes/upload_routes.py:634`

## `_sync_gallery_caption_for_upload` — function, line 549
- **called from:**
- `routes/upload_routes.py:596`
- `routes/upload_routes.py:611`
- `routes/upload_routes.py:636`

## `get_vision_text` — function (async), line 576
- **route:** `GET /{file_id}/vision`
- decorator: `router.get("/{file_id}/vision")`
- **called from:**
- `tests/test_upload_routes_owner_scope.py:220`
- `tests/test_upload_routes_owner_scope.py:240`
- `tests/test_upload_routes_owner_scope.py:265`

## `put_vision_text` — function (async), line 615
- **route:** `PUT /{file_id}/vision`
- decorator: `router.put("/{file_id}/vision")`
- **called from:**
- `tests/test_upload_routes_owner_scope.py:283`
- `tests/test_upload_routes_owner_scope.py:302`
- `tests/test_upload_routes_owner_scope.py:345`

## `periodic_rate_limit_cleanup` — function (async), line 639
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
