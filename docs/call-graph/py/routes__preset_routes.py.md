# `routes/preset_routes.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `UserTemplateRequest` — class, line 18
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_preset_routes` — function, line 28
- **called from:**
- `app.py:804`
- `tests/test_preset_expand_owner_scope.py:27`

## `get_presets` — function (async), line 32
- **route:** `GET /api/presets`
- decorator: `router.get("/api/presets")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_custom_preset` — function (async), line 36
- **route:** `POST /api/presets/custom`
- decorator: `router.post("/api/presets/custom")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_user_templates` — function (async), line 59
- **route:** `GET /api/presets/templates`
- decorator: `router.get("/api/presets/templates")`
- **called from:**
- `routes/preset_routes.py:60`
- `src/preset_manager.py:160`

## `save_user_template` — function (async), line 63
- **route:** `POST /api/presets/templates`
- decorator: `router.post("/api/presets/templates")`
- **called from:**
- `routes/preset_routes.py:67`

## `delete_user_template` — function (async), line 73
- **route:** `DELETE /api/presets/templates/{template_id}`
- decorator: `router.delete("/api/presets/templates/{template_id}")`
- **called from:**
- `routes/preset_routes.py:74`

## `expand_character_prompt` — function (async), line 80
- **route:** `POST /api/presets/expand`
- decorator: `router.post("/api/presets/expand")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_group_presets` — function (async), line 121
- **route:** `GET /api/presets/groups`
- decorator: `router.get("/api/presets/groups")`
- **called from:**
- `routes/preset_routes.py:123`

## `save_group_presets` — function (async), line 126
- **route:** `POST /api/presets/groups`
- decorator: `router.post("/api/presets/groups")`
- **called from:**
- `routes/preset_routes.py:129`
