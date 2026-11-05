# `src/tools/notes.py` — definitions & call sites

11 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_search_tokens` — function, line 19
- **called from:**
- `src/tools/notes.py:235`
- `src/tools/notes.py:242`

## `do_manage_notes` — function (async), line 33
- **called from:**
- `routes/codex_routes.py:286`
- `routes/codex_routes.py:295`
- `src/task_scheduler.py:1546`
- `src/tool_execution.py:2415`
- `tests/test_failed_call_correction.py:29`
- `tests/test_manage_notes_owner_gate.py:58`
- `tests/test_manage_notes_search_contract.py:79`
- `tests/test_manage_notes_search_contract.py:87`
- `tests/test_manage_notes_search_contract.py:109`
- `tests/test_manage_notes_search_contract.py:137`
- `tests/test_manage_notes_search_contract.py:164`
- `tests/test_manage_notes_search_contract.py:190`
- `tests/test_manage_notes_search_contract.py:197`
- `tests/test_manage_notes_search_contract.py:215`
- `tests/test_manage_notes_search_contract.py:219`
- `tests/test_manage_notes_search_contract.py:250`
- `tests/test_notes_checklist_state.py:31`
- `tests/test_notes_checklist_state.py:99`
- `tests/test_notes_checklist_state.py:109`
- `tests/test_notes_checklist_state.py:125`
- `tests/test_notes_reminder_temporal_redos.py:39`
- `tests/test_notes_update_due_date.py:73`
- `tests/test_upload_handler_cleanup.py:712`
- `tests/tools/organizer_smoke.py:108`
- `tests/tools/organizer_smoke.py:118`
- `tests/tools/organizer_smoke.py:238`

## `_norm_note_title` — function, line 86
- **called from:**
- `src/tools/notes.py:153`
- `src/tools/notes.py:161`
- `src/tools/notes.py:349`
- `src/tools/notes.py:351`
- `src/tools/notes.py:435`
- `src/tools/notes.py:435`
- `src/tools/notes.py:509`
- `src/tools/notes.py:509`

## `_note_visible_to_owner` — function, line 91
- **called from:**
- `src/tools/notes.py:257`
- `src/tools/notes.py:447`
- `src/tools/notes.py:521`
- `src/tools/notes.py:540`

## `_is_calendar_reminder_note` — function, line 99
- **called from:**
- `src/tools/notes.py:225`

## `_note_by_prefix` — function, line 102
- **called from:**
- `src/tools/notes.py:254`
- `src/tools/notes.py:421`
- `src/tools/notes.py:495`
- `src/tools/notes.py:537`

## `_note_id_arg` — function, line 110
- **called from:**
- `src/tools/notes.py:253`
- `src/tools/notes.py:420`
- `src/tools/notes.py:494`
- `src/tools/notes.py:533`

## `_norm_note_text` — function, line 113
- **called from:**
- `src/tools/notes.py:124`
- `src/tools/notes.py:126`
- `src/tools/notes.py:130`
- `src/tools/notes.py:133`
- `src/tools/notes.py:154`
- `src/tools/notes.py:173`

## `_norm_note_items` — function, line 116
- **called from:**
- `src/tools/notes.py:155`
- `src/tools/notes.py:175`

## `_existing_exact_note` — function, line 139
- **called from:**
- `src/tools/notes.py:358`

## `_format_note_list` — function, line 180
- **called from:**
- `src/tools/notes.py:250`
- `src/tools/notes.py:259`
