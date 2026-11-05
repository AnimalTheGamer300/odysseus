# `src/cookbook_serve_lifecycle.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_internal_headers` — function, line 28
- **called from:**
- `src/agent_runtime/local_model_control.py:42`
- `src/agent_tools/editor_tools.py:94`
- `src/agent_tools/editor_tools.py:492`
- `src/cookbook_serve_lifecycle.py:52`
- `src/cookbook_serve_lifecycle.py:99`
- `src/tools/cookbook.py:225`
- `src/tools/cookbook.py:288`
- `src/tools/cookbook.py:396`
- `src/tools/cookbook.py:434`
- `src/tools/cookbook.py:935`
- `src/tools/cookbook.py:1198`
- `src/tools/cookbook.py:1358`
- `src/tools/cookbook.py:1477`
- `src/tools/cookbook.py:1658`
- `src/tools/cookbook.py:1808`
- `src/tools/cookbook.py:1858`
- `src/tools/cookbook.py:1956`
- `src/tools/research.py:145`
- `src/tools/system.py:851`
- `src/tools/system.py:929`

## `_delete_endpoint_for_task` — function (async), line 33
- **called from:**
- `src/cookbook_serve_lifecycle.py:160`
- `tests/test_cookbook_serve_lifecycle.py:80`
- `tests/test_cookbook_serve_lifecycle.py:88`
- `tests/test_cookbook_serve_lifecycle.py:107`
- `tests/test_cookbook_serve_lifecycle.py:132`
- `tests/test_cookbook_serve_lifecycle.py:149`
- `tests/test_cookbook_serve_lifecycle.py:221`
- `tests/test_cookbook_serve_lifecycle.py:259`
- `tests/test_cookbook_serve_lifecycle.py:267`

## `_stop_serve` — function (async), line 73
- **called from:**
- `src/cookbook_serve_lifecycle.py:150`

## `_tick` — function (async), line 117
- **called from:**
- `src/cookbook_serve_lifecycle.py:196`
- `tests/test_cookbook_serve_lifecycle.py:48`

## `cookbook_serve_lifecycle_loop` — function (async), line 191
- **called from:**
- `app.py:1443`
