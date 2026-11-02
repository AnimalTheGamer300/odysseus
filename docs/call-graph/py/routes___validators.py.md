# `routes/_validators.py` — definitions & call sites

2 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `validate_remote_host` — function, line 12
- **called from:**
- `routes/codex_routes.py:54`
- `routes/codex_routes.py:835`
- `routes/cookbook_routes.py:968`
- `routes/cookbook_routes.py:1081`
- `routes/cookbook_routes.py:1412`
- `routes/cookbook_routes.py:1614`
- `routes/cookbook_routes.py:1974`
- `routes/cookbook_routes.py:2841`
- `routes/cookbook_routes.py:3161`
- `routes/cookbook_routes.py:3330`
- `routes/cookbook_routes.py:3706`
- `routes/cookbook_routes.py:4361`
- `routes/hwfit_routes.py:22`
- `src/tools/cookbook.py:31`
- `tests/test_route_validators.py:22`
- `tests/test_route_validators.py:23`

## `validate_ssh_port` — function, line 23
- **called from:**
- `routes/codex_routes.py:55`
- `routes/cookbook_routes.py:969`
- `routes/cookbook_routes.py:1082`
- `routes/cookbook_routes.py:1413`
- `routes/cookbook_routes.py:1609`
- `routes/cookbook_routes.py:1975`
- `routes/cookbook_routes.py:2845`
- `routes/cookbook_routes.py:3162`
- `routes/cookbook_routes.py:3331`
- `routes/cookbook_routes.py:3713`
- `routes/cookbook_routes.py:4367`
- `routes/hwfit_routes.py:23`
- `src/tools/cookbook.py:32`
- `tests/test_route_validators.py:10`
- `tests/test_route_validators.py:11`
