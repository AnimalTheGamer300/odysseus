# `routes/upload_routes.py` — definitions & call sites

20 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_upload_ids_from_persisted_text` — function, line 38
- **called from:**
- `routes/upload_routes.py:78`
- `routes/upload_routes.py:98`
- `routes/upload_routes.py:102`
- `routes/upload_routes.py:105`
- `routes/upload_routes.py:111`
- `routes/upload_routes.py:122`
- `routes/upload_routes.py:125`
- `routes/upload_routes.py:133`

## `_upload_ids_from_message_metadata` — function, line 49
- **called from:**
- `routes/upload_routes.py:99`

## `_collect_persisted_upload_references` — function, line 82
- **called from:**
- `routes/upload_routes.py:141`
- `tests/test_upload_handler_cleanup.py:547`

## `_run_reference_safe_cleanup` — function, line 140
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_upload_routes` — function, line 147
- **called from:**
- `app.py:670`
- `tests/test_upload_handler_cleanup.py:99`
- `tests/test_upload_multifile.py:106`
- `tests/test_upload_multifile.py:116`
- `tests/test_upload_multifile.py:130`
- `tests/test_upload_multifile.py:191`
- `tests/test_upload_multifile.py:222`
- `tests/test_upload_routes_owner_scope.py:38`

## `_upload_root` — function, line 150
- **called from:**
- `routes/upload_routes.py:156`
- `routes/upload_routes.py:156`
- `routes/upload_routes.py:386`
- `routes/upload_routes.py:421`

## `_path_inside_upload_dir` — function, line 154
- **called from:**
- `routes/upload_routes.py:165`
- `routes/upload_routes.py:175`

## `_resolve_upload_path` — function, line 160
- **called from:**
- `routes/upload_routes.py:379`
- `routes/upload_routes.py:468`
- `routes/upload_routes.py:514`

## `_valid_session_id_for_owner` — function, line 183
- **called from:**
- `routes/upload_routes.py:242`

## `_promote_chat_image_to_gallery` — function, line 193
- **called from:**
- `routes/upload_routes.py:292`

## `api_upload` — function (async), line 258
- decorator: `router.post("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `manual_cleanup` — function (async), line 321
- **route:** `POST /cleanup`
- decorator: `router.post("/cleanup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `upload_stats` — function (async), line 344
- **route:** `GET /stats`
- decorator: `router.get("/stats")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `download_file` — function (async), line 354
- **route:** `GET /{file_id}`
- decorator: `router.get("/{file_id}")`
- **called from:**
- `tests/test_upload_routes_owner_scope.py:128`
- `tests/test_upload_routes_owner_scope.py:138`
- `tests/test_upload_routes_owner_scope.py:148`
- `tests/test_upload_routes_owner_scope.py:161`
- `tests/test_upload_routes_owner_scope.py:181`
- `tests/test_upload_routes_owner_scope.py:200`
- `tests/test_upload_routes_owner_scope.py:326`

## `_load_upload_info` — function, line 413
- **called from:**
- `routes/upload_routes.py:458`
- `routes/upload_routes.py:502`

## `_vision_cache_path` — function, line 420
- **called from:**
- `routes/upload_routes.py:473`
- `routes/upload_routes.py:522`

## `_sync_gallery_caption_for_upload` — function, line 425
- **called from:**
- `routes/upload_routes.py:478`
- `routes/upload_routes.py:493`
- `routes/upload_routes.py:524`

## `get_vision_text` — function (async), line 452
- **route:** `GET /{file_id}/vision`
- decorator: `router.get("/{file_id}/vision")`
- **called from:**
- `tests/test_upload_routes_owner_scope.py:220`
- `tests/test_upload_routes_owner_scope.py:240`
- `tests/test_upload_routes_owner_scope.py:265`

## `put_vision_text` — function (async), line 497
- **route:** `PUT /{file_id}/vision`
- decorator: `router.put("/{file_id}/vision")`
- **called from:**
- `tests/test_upload_routes_owner_scope.py:283`
- `tests/test_upload_routes_owner_scope.py:302`
- `tests/test_upload_routes_owner_scope.py:343`

## `periodic_rate_limit_cleanup` — function (async), line 527
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
