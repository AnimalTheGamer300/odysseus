# `src/foreground_model_routing.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ForegroundModelPolicy` — class, line 26
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/foreground_model_routing.py:73`
- `src/foreground_model_routing.py:76`
- `src/foreground_model_routing.py:80`
- `src/foreground_model_routing.py:92`
- `src/foreground_model_routing.py:138`
- `src/foreground_model_routing.py:140`
- `tests/test_foreground_model_routing.py:1719`
- `tests/test_foreground_model_routing.py:1766`
- `tests/test_foreground_model_routing.py:1887`
- `tests/test_foreground_model_routing.py:1921`
- `tests/test_foreground_model_routing.py:2053`
- `tests/test_foreground_model_routing.py:2075`
- `tests/test_foreground_model_routing.py:2099`
- `tests/test_foreground_model_routing.py:2104`
- `tests/test_foreground_model_routing.py:2156`
- `tests/test_foreground_model_routing.py:2191`
- `tests/test_foreground_model_routing.py:2192`
- `tests/test_foreground_model_routing.py:2217`
- `tests/test_foreground_model_routing.py:2296`

## `_load_policy_preferences` — function, line 36
- **called from:**
- `src/foreground_model_routing.py:71`

## `resolve_foreground_model_policy` — function, line 59
- **called from:**
- `routes/chat_routes.py:2508`
- `routes/chat_routes.py:3280`
- `src/foreground_model_routing.py:152`
- `src/foreground_model_routing.py:164`
- `src/foreground_model_routing.py:183`
- `tests/test_foreground_model_routing.py:1921`
- `tests/test_foreground_model_routing.py:1947`
- `tests/test_foreground_model_routing.py:1988`
- `tests/test_foreground_model_routing.py:2023`
- `tests/test_foreground_model_routing.py:2052`
- `tests/test_foreground_model_routing.py:2053`
- `tests/test_foreground_model_routing.py:2075`
- `tests/test_foreground_model_routing.py:2099`
- `tests/test_foreground_model_routing.py:2104`
- `tests/test_foreground_model_routing.py:2156`
- `tests/test_foreground_model_routing.py:2191`
- `tests/test_foreground_model_routing.py:2192`
- `tests/test_foreground_model_routing.py:2216`
- `tests/test_foreground_model_routing.py:2217`
- `tests/test_foreground_model_routing.py:2239`
- `tests/test_foreground_model_routing.py:2270`
- `tests/test_foreground_model_routing.py:2293`

## `resolve_foreground_fallback_candidates` — function, line 149
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `build_foreground_model_candidates` — function, line 155
- **called from:**
- `routes/chat_routes.py:2551`
- `routes/chat_routes.py:4356`
- `tests/test_foreground_model_routing.py:1721`
- `tests/test_foreground_model_routing.py:1882`

## `build_foreground_route_descriptors` — function, line 173
- **called from:**
- `routes/chat_routes.py:2558`
- `routes/chat_routes.py:4363`
- `tests/test_foreground_model_routing.py:1761`
