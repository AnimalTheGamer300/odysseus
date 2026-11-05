# `routes/note/note_routes.py` — definitions & call sites

20 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `NoteCreate` — class, line 26
- **called from:**
- `tests/test_upload_handler_cleanup.py:773`

## `NoteUpdate` — class, line 43
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_note_to_dict` — function, line 64
- **called from:**
- `routes/note/note_routes.py:649`
- `routes/note/note_routes.py:687`
- `routes/note/note_routes.py:704`
- `routes/note/note_routes.py:764`

## `_reminder_text_from_note` — function, line 104
- **called from:**
- `routes/note/note_routes.py:898`

## `dispatch_reminder` — function (async), line 143
- **called from:**
- `routes/note/note_routes.py:902`
- `src/builtin_actions.py:2457`
- `src/builtin_actions.py:3265`
- `tests/test_note_reminder_email_oauth.py:35`
- `tests/test_reminder_ntfy_ssrf.py:59`

## `_smtp_send` — function, line 390
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_note_routes` — function, line 581
- **called from:**
- `app.py:942`
- `tests/test_note_reminder_fire_scope.py:67`
- `tests/test_notes_clear_optional_fields.py:24`
- `tests/test_notes_fail_closed_auth.py:87`
- `tests/test_upload_handler_cleanup.py:765`

## `_owner` — function, line 591
- **called from:**
- `routes/assistant_routes.py:127`
- `routes/assistant_routes.py:140`
- `routes/assistant_routes.py:161`
- `routes/assistant_routes.py:279`
- `routes/assistant_routes.py:303`
- `routes/memory/memory_routes.py:88`
- `routes/memory/memory_routes.py:117`
- `routes/memory/memory_routes.py:151`
- `routes/memory/memory_routes.py:157`
- `routes/memory/memory_routes.py:173`
- `routes/memory/memory_routes.py:211`
- `routes/memory/memory_routes.py:246`
- `routes/memory/memory_routes.py:261`
- `routes/memory/memory_routes.py:274`
- `routes/memory/memory_routes.py:299`
- `routes/memory/memory_routes.py:357`
- `routes/memory/memory_routes.py:398`
- `routes/memory/memory_routes.py:512`
- `routes/memory/memory_routes.py:526`
- `routes/memory/memory_routes.py:537`
- `routes/memory/memory_routes.py:559`
- `routes/note/note_routes.py:632`
- `routes/note/note_routes.py:656`
- `routes/note/note_routes.py:694`
- `routes/note/note_routes.py:711`
- `routes/note/note_routes.py:771`
- `routes/note/note_routes.py:790`
- `routes/note/note_routes.py:809`
- `routes/note/note_routes.py:828`
- `routes/note/note_routes.py:867`
- `routes/note/note_routes.py:913`
- `routes/skills_routes.py:317`
- `routes/skills_routes.py:326`
- `routes/skills_routes.py:337`
- `routes/skills_routes.py:463`
- `routes/skills_routes.py:491`
- `routes/skills_routes.py:529`
- `routes/skills_routes.py:565`
- `routes/skills_routes.py:576`
- `routes/skills_routes.py:605`
- `routes/skills_routes.py:666`
- `routes/skills_routes.py:720`
- `routes/skills_routes.py:736`
- `routes/skills_routes.py:767`
- `routes/skills_routes.py:772`
- `routes/skills_routes.py:779`
- `routes/skills_routes.py:830`
- `routes/skills_routes.py:853`
- `routes/skills_routes.py:870`
- `routes/task/task_routes.py:353`
- `routes/task/task_routes.py:384`
- `routes/task/task_routes.py:393`
- `routes/task/task_routes.py:462`
- `routes/task/task_routes.py:580`
- `routes/task/task_routes.py:589`
- `routes/task/task_routes.py:617`
- `routes/task/task_routes.py:640`
- `routes/task/task_routes.py:719`
- `routes/task/task_routes.py:733`
- `routes/task/task_routes.py:830`
- … +16 more (grep the name in repo)

## `_reserve_note_uploads` — function, line 603
- **called from:**
- `routes/note/note_routes.py:657`
- `routes/note/note_routes.py:722`

## `_is_admin_or_single_user` — function, line 608
- **called from:**
- `routes/note/note_routes.py:869`

## `list_notes` — function, line 627
- decorator: `router.get("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_note` — function, line 655
- decorator: `router.post("")`
- **called from:**
- `tests/test_upload_handler_cleanup.py:771`

## `get_note` — function, line 693
- **route:** `GET /{note_id}`
- decorator: `router.get("/{note_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_note` — function, line 710
- **route:** `PUT /{note_id}`
- decorator: `router.put("/{note_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_note` — function, line 770
- **route:** `DELETE /{note_id}`
- decorator: `router.delete("/{note_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_pin` — function, line 789
- **route:** `POST /{note_id}/pin`
- decorator: `router.post("/{note_id}/pin")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_archive` — function, line 808
- **route:** `POST /{note_id}/archive`
- decorator: `router.post("/{note_id}/archive")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_item` — function, line 827
- **route:** `POST /{note_id}/items/{index}/toggle`
- decorator: `router.post("/{note_id}/items/{index}/toggle")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `fire_reminder` — function (async), line 853
- **route:** `POST /fire-reminder`
- decorator: `router.post("/fire-reminder")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `reorder_notes` — function (async), line 911
- **route:** `POST /reorder`
- decorator: `router.post("/reorder")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
