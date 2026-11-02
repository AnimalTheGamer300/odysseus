# `routes/editor_draft_routes.py` — definitions & call sites

11 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `DraftCreate` — class, line 33
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DraftUpdate` — class, line 42
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_owns` — function, line 50
- **called from:**
- `routes/editor_draft_routes.py:102`
- `routes/editor_draft_routes.py:145`
- `routes/editor_draft_routes.py:175`

## `_summary` — function, line 56
- **called from:**
- `routes/editor_draft_routes.py:90`
- `routes/editor_draft_routes.py:105`
- `routes/editor_draft_routes.py:129`
- `routes/editor_draft_routes.py:159`
- `tests/cli/test_skills_cli_preview.py:31`

## `_load_payload` — function, line 70
- **called from:**
- `routes/editor_draft_routes.py:106`
- `tests/test_editor_draft_payload.py:21`
- `tests/test_editor_draft_payload.py:22`
- `tests/test_editor_draft_payload.py:23`
- `tests/test_editor_draft_payload.py:24`

## `setup_editor_draft_routes` — function, line 78
- **called from:**
- `app.py:780`

## `list_drafts` — function (async), line 82
- **route:** `GET /api/editor-drafts`
- decorator: `router.get("/api/editor-drafts")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_draft` — function (async), line 95
- **route:** `GET /api/editor-drafts/{draft_id}`
- decorator: `router.get("/api/editor-drafts/{draft_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_draft` — function (async), line 112
- **route:** `POST /api/editor-drafts`
- decorator: `router.post("/api/editor-drafts")`
- **called from:**
- `routes/chat_routes.py:401`
- `tests/test_draft_promotion_keeps_live_media.py:76`
- `tests/test_draft_promotion_keeps_live_media.py:121`

## `update_draft` — function (async), line 138
- **route:** `PUT /api/editor-drafts/{draft_id}`
- decorator: `router.put("/api/editor-drafts/{draft_id}")`
- **called from:**
- `routes/chat_routes.py:399`

## `delete_draft` — function (async), line 170
- **route:** `DELETE /api/editor-drafts/{draft_id}`
- decorator: `router.delete("/api/editor-drafts/{draft_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
