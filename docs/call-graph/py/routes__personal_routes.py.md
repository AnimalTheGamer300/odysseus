# `routes/personal_routes.py` — definitions & call sites

18 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_personal_upload_dir_for_owner` — function, line 24
- **called from:**
- `routes/personal_routes.py:82`
- `routes/personal_routes.py:83`
- `routes/personal_routes.py:315`
- `routes/personal_routes.py:418`
- `tests/test_personal_upload_isolation.py:11`
- `tests/test_personal_upload_isolation.py:12`
- `tests/test_personal_upload_isolation.py:37`
- `tests/test_personal_upload_isolation.py:51`
- `tests/test_personal_upload_isolation.py:73`
- `tests/test_rename_user_owner_sync.py:495`
- `tests/test_rename_user_owner_sync.py:521`

## `_unique_personal_upload_path` — function, line 33
- **called from:**
- `routes/personal_routes.py:330`
- `tests/test_personal_upload_isolation.py:18`
- `tests/test_personal_upload_isolation.py:22`
- `tests/test_personal_upload_isolation.py:38`

## `_unique_existing_target` — function, line 46
- **called from:**
- `routes/personal_routes.py:95`

## `_remove_empty_tree` — function, line 57
- **called from:**
- `routes/personal_routes.py:99`

## `rename_personal_upload_owner` — function, line 74
- **called from:**
- `routes/auth_routes.py:591`
- `tests/test_personal_upload_isolation.py:66`

## `setup_personal_routes` — function, line 126
- **called from:**
- `app.py:816`
- `tests/test_add_directory_event_loop.py:95`
- `tests/test_personal_delete_file_confinement.py:26`
- `tests/test_personal_upload_privilege.py:12`

## `_rag` — function, line 156
- **called from:**
- `routes/personal_routes.py:215`
- `routes/personal_routes.py:275`
- `routes/personal_routes.py:311`
- `routes/personal_routes.py:403`

## `_resolve_allowed_personal_dir` — function, line 160
- **called from:**
- `routes/personal_routes.py:203`
- `routes/personal_routes.py:271`

## `api_personal_list` — function, line 171
- decorator: `router.get("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `api_personal_reload` — function (async), line 178
- **route:** `POST /reload`
- decorator: `router.post("/reload")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_directory_to_rag` — function (async), line 187
- **route:** `POST /add_directory`
- decorator: `router.post("/add_directory")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_index_directory` — function, line 217
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `remove_directory_from_rag` — function (async), line 256
- **route:** `DELETE /remove_directory`
- decorator: `router.delete("/remove_directory")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_remove_directory` — function, line 277
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `upload_files_to_rag` — function (async), line 308
- **route:** `POST /upload`
- decorator: `router.post("/upload")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_index_upload` — function, line 339
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_file_from_rag` — function (async), line 397
- **route:** `DELETE /file`
- decorator: `router.delete("/file")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_delete_file` — function, line 400
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
