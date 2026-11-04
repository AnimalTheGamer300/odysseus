# `routes/memory/memory_routes.py` — definitions & call sites

19 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_strip_list_prefix` — function, line 19
- **called from:**
- `routes/memory/memory_routes.py:425`
- `routes/memory/memory_routes.py:430`
- `routes/memory/memory_routes.py:483`
- `routes/memory/memory_routes.py:486`
- `routes/memory/memory_routes.py:496`

## `_load_for_update` — function, line 38
- **called from:**
- `routes/memory/memory_routes.py:135`
- `routes/memory/memory_routes.py:506`
- `routes/memory/memory_routes.py:531`
- `routes/memory/memory_routes.py:553`

## `setup_memory_routes` — function, line 54
- **called from:**
- `app.py:695`
- `tests/test_memory_owner_isolation.py:14`
- `tests/test_memory_routes_session_owner.py:42`
- `tests/test_memory_routes_session_owner.py:99`
- `tests/test_memory_routes_session_owner.py:162`
- `tests/test_memory_routes_session_owner.py:208`
- `tests/test_memory_routes_session_owner.py:225`
- `tests/test_memory_routes_session_owner.py:252`
- `tests/test_memory_routes_session_owner.py:276`

## `_owner` — function, line 58
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

## `_assert_session_owner` — function, line 61
- **called from:**
- `routes/memory/memory_routes.py:130`
- `routes/memory/memory_routes.py:193`
- `routes/memory/memory_routes.py:216`
- `routes/memory/memory_routes.py:246`
- `routes/memory/memory_routes.py:302`
- `routes/memory/memory_routes.py:358`

## `_verify_memory_owner` — function, line 73
- **called from:**
- `routes/memory/memory_routes.py:509`
- `routes/memory/memory_routes.py:534`
- `routes/memory/memory_routes.py:559`

## `debug_memory_relevance` — function, line 86
- **route:** `POST /debug`
- decorator: `router.post("/debug")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `api_add_memory` — function (async), line 101
- **route:** `POST /add`
- decorator: `router.post("/add", response_model=Dict[str, Any])`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `api_get_memory` — function, line 149
- decorator: `router.get("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `search_memories` — function, line 155
- **route:** `POST /search`
- decorator: `router.post("/search")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `memory_timeline` — function, line 171
- **route:** `GET /timeline`
- decorator: `router.get("/timeline")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_memory_by_session` — function, line 209
- **route:** `GET /by-session/{session_id}`
- decorator: `router.get("/by-session/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `extract_memory` — function (async), line 239
- **route:** `POST /extract`
- decorator: `router.post("/extract")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `api_audit_memories` — function (async), line 289
- **route:** `POST /audit`
- decorator: `router.post("/audit")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `import_memories_from_file` — function (async), line 340
- **route:** `POST /import`
- decorator: `router.post("/import")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `pin_memory` — function, line 503
- **route:** `POST /{memory_id}/pin`
- decorator: `router.post("/{memory_id}/pin")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_memory_item` — function, line 517
- **route:** `GET /{memory_id}`
- decorator: `router.get("/{memory_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_memory` — function, line 528
- **route:** `PUT /{memory_id}`
- decorator: `router.put("/{memory_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_memory` — function, line 550
- **route:** `DELETE /{memory_id}`
- decorator: `router.delete("/{memory_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
