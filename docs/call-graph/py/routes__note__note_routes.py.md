# `routes/note/note_routes.py` — definitions & call sites

20 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `NoteCreate` — class, line 26
- **called from:**
- `tests/test_upload_handler_cleanup.py:773`

## `NoteUpdate` — class, line 42
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_note_to_dict` — function, line 62
- **called from:**
- `routes/note/note_routes.py:646`
- `routes/note/note_routes.py:683`
- `routes/note/note_routes.py:700`
- `routes/note/note_routes.py:755`

## `_reminder_text_from_note` — function, line 101
- **called from:**
- `routes/note/note_routes.py:889`

## `dispatch_reminder` — function (async), line 140
- **called from:**
- `routes/note/note_routes.py:893`
- `src/builtin_actions.py:2218`
- `src/builtin_actions.py:2982`
- `tests/test_note_reminder_email_oauth.py:35`
- `tests/test_reminder_ntfy_ssrf.py:59`

## `_smtp_send` — function, line 387
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_note_routes` — function, line 578
- **called from:**
- `app.py:858`
- `tests/test_note_reminder_fire_scope.py:67`
- `tests/test_notes_fail_closed_auth.py:87`
- `tests/test_upload_handler_cleanup.py:765`

## `_owner` — function, line 588
- **called from:**
- `routes/assistant_routes.py:126`
- `routes/assistant_routes.py:139`
- `routes/assistant_routes.py:160`
- `routes/assistant_routes.py:272`
- `routes/assistant_routes.py:296`
- `routes/memory/memory_routes.py:88`
- `routes/memory/memory_routes.py:117`
- `routes/memory/memory_routes.py:151`
- `routes/memory/memory_routes.py:157`
- `routes/memory/memory_routes.py:173`
- `routes/memory/memory_routes.py:211`
- `routes/memory/memory_routes.py:246`
- `routes/memory/memory_routes.py:261`
- `routes/memory/memory_routes.py:296`
- `routes/memory/memory_routes.py:353`
- `routes/memory/memory_routes.py:394`
- `routes/memory/memory_routes.py:505`
- `routes/memory/memory_routes.py:519`
- `routes/memory/memory_routes.py:530`
- `routes/memory/memory_routes.py:552`
- `routes/note/note_routes.py:629`
- `routes/note/note_routes.py:653`
- `routes/note/note_routes.py:690`
- `routes/note/note_routes.py:707`
- `routes/note/note_routes.py:762`
- `routes/note/note_routes.py:781`
- `routes/note/note_routes.py:800`
- `routes/note/note_routes.py:819`
- `routes/note/note_routes.py:858`
- `routes/note/note_routes.py:904`
- `routes/skills_routes.py:1208`
- `routes/skills_routes.py:1217`
- `routes/skills_routes.py:1228`
- `routes/skills_routes.py:1354`
- `routes/skills_routes.py:1382`
- `routes/skills_routes.py:1420`
- `routes/skills_routes.py:1456`
- `routes/skills_routes.py:1467`
- `routes/skills_routes.py:1490`
- `routes/skills_routes.py:1567`
- `routes/skills_routes.py:1685`
- `routes/skills_routes.py:1713`
- `routes/skills_routes.py:1778`
- `routes/skills_routes.py:1792`
- `routes/skills_routes.py:1807`
- `routes/skills_routes.py:1858`
- `routes/skills_routes.py:1877`
- `routes/skills_routes.py:1894`
- `routes/task/task_routes.py:344`
- `routes/task/task_routes.py:375`
- `routes/task/task_routes.py:384`
- `routes/task/task_routes.py:453`
- `routes/task/task_routes.py:566`
- `routes/task/task_routes.py:575`
- `routes/task/task_routes.py:654`
- `routes/task/task_routes.py:668`
- `routes/task/task_routes.py:758`
- `routes/task/task_routes.py:780`
- `routes/task/task_routes.py:796`
- `routes/task/task_routes.py:820`
- … +9 more (grep the name in repo)

## `_reserve_note_uploads` — function, line 600
- **called from:**
- `routes/note/note_routes.py:654`
- `routes/note/note_routes.py:718`

## `_is_admin_or_single_user` — function, line 605
- **called from:**
- `routes/note/note_routes.py:860`

## `list_notes` — function, line 624
- decorator: `router.get("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_note` — function, line 652
- decorator: `router.post("")`
- **called from:**
- `tests/test_upload_handler_cleanup.py:771`

## `get_note` — function, line 689
- **route:** `GET /{note_id}`
- decorator: `router.get("/{note_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_note` — function, line 706
- **route:** `PUT /{note_id}`
- decorator: `router.put("/{note_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_note` — function, line 761
- **route:** `DELETE /{note_id}`
- decorator: `router.delete("/{note_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_pin` — function, line 780
- **route:** `POST /{note_id}/pin`
- decorator: `router.post("/{note_id}/pin")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_archive` — function, line 799
- **route:** `POST /{note_id}/archive`
- decorator: `router.post("/{note_id}/archive")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_item` — function, line 818
- **route:** `POST /{note_id}/items/{index}/toggle`
- decorator: `router.post("/{note_id}/items/{index}/toggle")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `fire_reminder` — function (async), line 844
- **route:** `POST /fire-reminder`
- decorator: `router.post("/fire-reminder")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `reorder_notes` — function (async), line 902
- **route:** `POST /reorder`
- decorator: `router.post("/reorder")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
