# `routes/editor_draft_routes.py` — definitions & call sites

17 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `DraftCreate` — class, line 35
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DraftUpdate` — class, line 44
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_owns` — function, line 52
- **called from:**
- `routes/editor_draft_routes.py:152`
- `routes/editor_draft_routes.py:204`
- `routes/editor_draft_routes.py:234`

## `_summary` — function, line 58
- **called from:**
- `routes/editor_draft_routes.py:140`
- `routes/editor_draft_routes.py:155`
- `routes/editor_draft_routes.py:182`
- `routes/editor_draft_routes.py:218`
- `tests/cli/test_skills_cli_preview.py:31`

## `_load_payload` — function, line 72
- **called from:**
- `routes/editor_draft_routes.py:156`
- `tests/test_editor_draft_payload.py:24`
- `tests/test_editor_draft_payload.py:25`
- `tests/test_editor_draft_payload.py:26`
- `tests/test_editor_draft_payload.py:27`

## `_draft_too_large` — function, line 80
- **called from:**
- `routes/editor_draft_routes.py:104`
- `routes/editor_draft_routes.py:124`

## `reject_oversized_draft_body` — function, line 87
- **called from:**
- `routes/editor_draft_routes.py:115`
- `tests/test_review_20260923_fixes.py:452`
- `tests/test_review_20260923_fixes.py:466`

## `EditorDraftRoute` — class, line 107
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EditorDraftRoute.get_route_handler` — method, line 110
- **called from:**
- `routes/editor_draft_routes.py:111`

## `EditorDraftRoute.custom_route_handler` — method (async), line 113
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_dump_payload` — function, line 121
- **called from:**
- `routes/editor_draft_routes.py:176`
- `routes/editor_draft_routes.py:213`
- `tests/test_editor_draft_payload.py:34`
- `tests/test_editor_draft_payload.py:36`
- `tests/test_review_20260923_fixes.py:456`
- `tests/test_review_20260923_fixes.py:473`

## `setup_editor_draft_routes` — function, line 128
- **called from:**
- `app.py:860`
- `tests/test_review_20260923_fixes.py:352`

## `list_drafts` — function (async), line 132
- **route:** `GET /api/editor-drafts`
- decorator: `router.get("/api/editor-drafts")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_draft` — function (async), line 145
- **route:** `GET /api/editor-drafts/{draft_id}`
- decorator: `router.get("/api/editor-drafts/{draft_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_draft` — function (async), line 162
- **route:** `POST /api/editor-drafts`
- decorator: `router.post("/api/editor-drafts")`
- **called from:**
- `routes/chat_routes.py:1597`

## `update_draft` — function (async), line 193
- **route:** `PUT /api/editor-drafts/{draft_id}`
- decorator: `router.put("/api/editor-drafts/{draft_id}")`
- **called from:**
- `routes/chat_routes.py:1595`

## `delete_draft` — function (async), line 229
- **route:** `DELETE /api/editor-drafts/{draft_id}`
- decorator: `router.delete("/api/editor-drafts/{draft_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
