# `src/host_docker_access.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `running_in_container` — function, line 21
- **called from:**
- `routes/cookbook_routes.py:364`
- `routes/cookbook_routes.py:2071`
- `src/host_docker_access.py:59`
- `tests/test_cookbook_docker_access.py:184`

## `host_docker_access_enabled` — function, line 35
- **called from:**
- `routes/cookbook_routes.py:2072`
- `src/host_docker_access.py:62`
- `tests/test_cookbook_docker_access.py:185`

## `local_docker_available` — function, line 50
- **called from:**
- `routes/cookbook_routes.py:335`
- `routes/cookbook_routes.py:350`
