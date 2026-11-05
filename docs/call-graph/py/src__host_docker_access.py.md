# `src/host_docker_access.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `running_in_container` — function, line 21
- **called from:**
- `routes/cookbook_routes.py:376`
- `routes/cookbook_routes.py:1982`
- `src/host_docker_access.py:59`
- `tests/test_cookbook_docker_access.py:190`

## `host_docker_access_enabled` — function, line 35
- **called from:**
- `routes/cookbook_routes.py:1983`
- `src/host_docker_access.py:62`
- `tests/test_cookbook_docker_access.py:191`

## `local_docker_available` — function, line 50
- **called from:**
- `routes/cookbook_routes.py:347`
- `routes/cookbook_routes.py:362`
