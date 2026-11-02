# `routes/personal_routes.py` — definitions & call sites

18 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_personal_upload_dir_for_owner` — function, line 23
- **called from:**
- `routes/personal_routes.py:87`
- `routes/personal_routes.py:88`
- `routes/personal_routes.py:329`
- `routes/personal_routes.py:430`
- `tests/test_personal_upload_isolation.py:11`
- `tests/test_personal_upload_isolation.py:12`
- `tests/test_personal_upload_isolation.py:37`
- `tests/test_personal_upload_isolation.py:51`
- `tests/test_personal_upload_isolation.py:73`
- `tests/test_rename_user_owner_sync.py:495`
- `tests/test_rename_user_owner_sync.py:521`

## `_unique_personal_upload_path` — function, line 35
- **called from:**
- `routes/personal_routes.py:344`
- `tests/test_personal_upload_isolation.py:18`
- `tests/test_personal_upload_isolation.py:22`
- `tests/test_personal_upload_isolation.py:38`

## `_unique_existing_target` — function, line 51
- **called from:**
- `routes/personal_routes.py:100`

## `_remove_empty_tree` — function, line 62
- **called from:**
- `routes/personal_routes.py:104`

## `rename_personal_upload_owner` — function, line 79
- **called from:**
- `routes/auth_routes.py:541`
- `tests/test_personal_upload_isolation.py:66`

## `setup_personal_routes` — function, line 131
- **called from:**
- `app.py:736`
- `tests/test_add_directory_event_loop.py:95`
- `tests/test_personal_delete_file_confinement.py:26`
- `tests/test_personal_upload_privilege.py:12`

## `_rag` — function, line 161
- **called from:**
- `routes/personal_routes.py:229`
- `routes/personal_routes.py:289`
- `routes/personal_routes.py:325`
- `routes/personal_routes.py:417`

## `_resolve_allowed_personal_dir` — function, line 165
- **called from:**
- `routes/personal_routes.py:217`
- `routes/personal_routes.py:285`

## `api_personal_list` — function, line 185
- decorator: `router.get("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `api_personal_reload` — function (async), line 192
- **route:** `POST /reload`
- decorator: `router.post("/reload")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_directory_to_rag` — function (async), line 201
- **route:** `POST /add_directory`
- decorator: `router.post("/add_directory")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_index_directory` — function, line 231
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `remove_directory_from_rag` — function (async), line 270
- **route:** `DELETE /remove_directory`
- decorator: `router.delete("/remove_directory")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_remove_directory` — function, line 291
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `upload_files_to_rag` — function (async), line 322
- **route:** `POST /upload`
- decorator: `router.post("/upload")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_index_upload` — function, line 353
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_file_from_rag` — function (async), line 411
- **route:** `DELETE /file`
- decorator: `router.delete("/file")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_delete_file` — function, line 414
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
