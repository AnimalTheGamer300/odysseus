# `routes/preset_routes.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `UserTemplateRequest` — class, line 18
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_preset_routes` — function, line 26
- **called from:**
- `app.py:724`
- `tests/test_preset_expand_owner_scope.py:27`

## `get_presets` — function (async), line 30
- **route:** `GET /api/presets`
- decorator: `router.get("/api/presets")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_custom_preset` — function (async), line 34
- **route:** `POST /api/presets/custom`
- decorator: `router.post("/api/presets/custom")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_user_templates` — function (async), line 53
- **route:** `GET /api/presets/templates`
- decorator: `router.get("/api/presets/templates")`
- **called from:**
- `routes/preset_routes.py:54`

## `save_user_template` — function (async), line 57
- **route:** `POST /api/presets/templates`
- decorator: `router.post("/api/presets/templates")`
- **called from:**
- `routes/preset_routes.py:61`

## `delete_user_template` — function (async), line 67
- **route:** `DELETE /api/presets/templates/{template_id}`
- decorator: `router.delete("/api/presets/templates/{template_id}")`
- **called from:**
- `routes/preset_routes.py:68`

## `expand_character_prompt` — function (async), line 74
- **route:** `POST /api/presets/expand`
- decorator: `router.post("/api/presets/expand")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_group_presets` — function (async), line 115
- **route:** `GET /api/presets/groups`
- decorator: `router.get("/api/presets/groups")`
- **called from:**
- `routes/preset_routes.py:117`

## `save_group_presets` — function (async), line 120
- **route:** `POST /api/presets/groups`
- decorator: `router.post("/api/presets/groups")`
- **called from:**
- `routes/preset_routes.py:123`
