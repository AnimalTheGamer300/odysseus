# `src/tools/notes.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `do_manage_notes` — function (async), line 19
- **called from:**
- `routes/codex_routes.py:240`
- `routes/codex_routes.py:249`
- `src/task_scheduler.py:1392`
- `src/tool_execution.py:1233`
- `tests/test_manage_notes_owner_gate.py:58`
- `tests/test_notes_update_due_date.py:73`
- `tests/test_upload_handler_cleanup.py:712`

## `_norm_note_title` — function, line 45
- **called from:**
- `src/tools/notes.py:194`
- `src/tools/notes.py:196`

## `_note_visible_to_owner` — function, line 50
- **called from:**
- `src/tools/notes.py:125`
- `src/tools/notes.py:250`
- `src/tools/notes.py:299`
- `src/tools/notes.py:312`

## `_note_by_prefix` — function, line 58
- **called from:**
- `src/tools/notes.py:122`
- `src/tools/notes.py:247`
- `src/tools/notes.py:296`
- `src/tools/notes.py:309`

## `_format_note_list` — function, line 66
- **called from:**
- `src/tools/notes.py:118`
- `src/tools/notes.py:127`
