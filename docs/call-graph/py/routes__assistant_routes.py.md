# `routes/assistant_routes.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `CheckInUpdate` — class, line 24
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AssistantSettingsUpdate` — class, line 32
- **called from:**
- `tests/test_endpoint_registered_authority.py:291`
- `tests/test_endpoint_registered_authority.py:302`
- `tests/test_endpoint_registered_authority.py:314`

## `_crew_to_dict` — function, line 47
- **called from:**
- `routes/assistant_routes.py:151`
- `routes/assistant_routes.py:269`

## `_task_to_checkin_dict` — function, line 68
- **called from:**
- `routes/assistant_routes.py:152`
- `routes/assistant_routes.py:270`

## `setup_assistant_routes` — function, line 81
- **called from:**
- `app.py:875`
- `tests/test_endpoint_registered_authority.py:289`
- `tests/test_endpoint_registered_authority.py:301`
- `tests/test_endpoint_registered_authority.py:313`

## `_owner` — function, line 84
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

## `_get_or_create` — function (async), line 97
- **called from:**
- `routes/assistant_routes.py:128`
- `routes/assistant_routes.py:141`
- `routes/assistant_routes.py:162`

## `get_assistant_session` — function (async), line 125
- **route:** `GET /session`
- decorator: `router.get("/session")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_assistant_settings` — function (async), line 138
- **route:** `GET /settings`
- decorator: `router.get("/settings")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_assistant_settings` — function (async), line 159
- **route:** `PATCH /settings`
- decorator: `router.patch("/settings")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `run_check_in_now` — function (async), line 277
- **route:** `POST /run/{task_id}`
- decorator: `router.post("/run/{task_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `run_status` — function (async), line 300
- **route:** `GET /run-status/{task_id}`
- decorator: `router.get("/run-status/{task_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_timezones` — function (async), line 325
- **route:** `GET /available-timezones`
- decorator: `router.get("/available-timezones")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
