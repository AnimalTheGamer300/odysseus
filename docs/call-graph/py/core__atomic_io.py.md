# `core/atomic_io.py` — definitions & call sites

2 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `atomic_write_json` — function, line 22
- **called from:**
- `routes/auth_routes.py:498`
- `routes/auth_routes.py:518`
- `routes/auth_routes.py:583`
- `routes/codex_routes.py:874`
- `routes/contacts/contacts_routes.py:44`
- `routes/contacts/contacts_routes.py:120`
- `routes/cookbook_routes.py:3504`
- `routes/cookbook_routes.py:3863`
- `routes/email_helpers.py:1008`
- `routes/prefs_routes.py:27`
- `services/memory/skills.py:101`
- `src/agent_jobs.py:111`
- `src/bg_jobs.py:70`
- `src/builtin_actions.py:3377`
- `src/cookbook_serve_lifecycle.py:206`
- `src/integrations.py:257`
- `src/preset_manager.py:123`
- `src/settings.py:278`
- `src/settings.py:363`
- `tests/test_atomic_io.py:46`
- `tests/test_atomic_io.py:54`
- `tests/test_atomic_io.py:64`
- `tests/test_atomic_io.py:72`
- `tests/test_atomic_io.py:74`
- `tests/test_atomic_io.py:84`
- `tests/test_atomic_io.py:106`
- `tests/test_atomic_io.py:130`
- `tests/test_atomic_io.py:136`
- `tests/test_atomic_io.py:145`
- `tests/test_atomic_io.py:154`

## `atomic_write_text` — function, line 49
- **called from:**
- `routes/auth_routes.py:565`
- `services/memory/skills.py:179`
- `services/memory/skills.py:418`
- `services/memory/skills.py:428`
- `tests/test_atomic_io.py:168`
- `tests/test_atomic_io.py:176`
- `tests/test_atomic_io.py:184`
- `tests/test_atomic_io.py:186`
- `tests/test_atomic_io.py:194`
- `tests/test_atomic_io.py:203`
- `tests/test_atomic_io.py:214`
- `tests/test_atomic_io.py:223`
- `tests/test_atomic_io.py:232`
- `tests/test_atomic_io.py:246`
