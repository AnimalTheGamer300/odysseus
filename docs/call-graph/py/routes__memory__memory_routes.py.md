# `routes/memory/memory_routes.py` — definitions & call sites

19 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_strip_list_prefix` — function, line 19
- **called from:**
- `routes/memory/memory_routes.py:429`
- `routes/memory/memory_routes.py:434`
- `routes/memory/memory_routes.py:490`
- `routes/memory/memory_routes.py:493`
- `routes/memory/memory_routes.py:503`

## `_load_for_update` — function, line 38
- **called from:**
- `routes/memory/memory_routes.py:135`
- `routes/memory/memory_routes.py:513`
- `routes/memory/memory_routes.py:538`
- `routes/memory/memory_routes.py:560`

## `setup_memory_routes` — function, line 54
- **called from:**
- `app.py:774`
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

## `_assert_session_owner` — function, line 61
- **called from:**
- `routes/memory/memory_routes.py:130`
- `routes/memory/memory_routes.py:193`
- `routes/memory/memory_routes.py:216`
- `routes/memory/memory_routes.py:246`
- `routes/memory/memory_routes.py:305`
- `routes/memory/memory_routes.py:362`

## `_verify_memory_owner` — function, line 73
- **called from:**
- `routes/memory/memory_routes.py:516`
- `routes/memory/memory_routes.py:541`
- `routes/memory/memory_routes.py:566`

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

## `api_audit_memories` — function (async), line 292
- **route:** `POST /audit`
- decorator: `router.post("/audit")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `import_memories_from_file` — function (async), line 343
- **route:** `POST /import`
- decorator: `router.post("/import")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `pin_memory` — function, line 510
- **route:** `POST /{memory_id}/pin`
- decorator: `router.post("/{memory_id}/pin")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_memory_item` — function, line 524
- **route:** `GET /{memory_id}`
- decorator: `router.get("/{memory_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_memory` — function, line 535
- **route:** `PUT /{memory_id}`
- decorator: `router.put("/{memory_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_memory` — function, line 557
- **route:** `DELETE /{memory_id}`
- decorator: `router.delete("/{memory_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
