# `routes/assistant_routes.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `CheckInUpdate` — class, line 23
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AssistantSettingsUpdate` — class, line 31
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_crew_to_dict` — function, line 46
- **called from:**
- `routes/assistant_routes.py:150`
- `routes/assistant_routes.py:262`

## `_task_to_checkin_dict` — function, line 67
- **called from:**
- `routes/assistant_routes.py:151`
- `routes/assistant_routes.py:263`

## `setup_assistant_routes` — function, line 80
- **called from:**
- `app.py:791`

## `_owner` — function, line 83
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

## `_get_or_create` — function (async), line 96
- **called from:**
- `routes/assistant_routes.py:127`
- `routes/assistant_routes.py:140`
- `routes/assistant_routes.py:161`

## `get_assistant_session` — function (async), line 124
- **route:** `GET /session`
- decorator: `router.get("/session")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_assistant_settings` — function (async), line 137
- **route:** `GET /settings`
- decorator: `router.get("/settings")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_assistant_settings` — function (async), line 158
- **route:** `PATCH /settings`
- decorator: `router.patch("/settings")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `run_check_in_now` — function (async), line 270
- **route:** `POST /run/{task_id}`
- decorator: `router.post("/run/{task_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `run_status` — function (async), line 293
- **route:** `GET /run-status/{task_id}`
- decorator: `router.get("/run-status/{task_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_timezones` — function (async), line 318
- **route:** `GET /available-timezones`
- decorator: `router.get("/available-timezones")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
