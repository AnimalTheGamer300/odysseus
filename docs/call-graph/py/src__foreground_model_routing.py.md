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
- `tests/test_foreground_model_routing.py:1665`
- `tests/test_foreground_model_routing.py:1712`
- `tests/test_foreground_model_routing.py:1803`
- `tests/test_foreground_model_routing.py:1837`
- `tests/test_foreground_model_routing.py:1969`
- `tests/test_foreground_model_routing.py:1991`
- `tests/test_foreground_model_routing.py:2015`
- `tests/test_foreground_model_routing.py:2020`
- `tests/test_foreground_model_routing.py:2072`
- `tests/test_foreground_model_routing.py:2107`
- `tests/test_foreground_model_routing.py:2108`
- `tests/test_foreground_model_routing.py:2133`
- `tests/test_foreground_model_routing.py:2212`

## `_load_policy_preferences` — function, line 36
- **called from:**
- `src/foreground_model_routing.py:71`

## `resolve_foreground_model_policy` — function, line 59
- **called from:**
- `routes/chat_routes.py:982`
- `routes/chat_routes.py:1544`
- `src/foreground_model_routing.py:152`
- `src/foreground_model_routing.py:164`
- `src/foreground_model_routing.py:183`
- `tests/test_foreground_model_routing.py:1837`
- `tests/test_foreground_model_routing.py:1863`
- `tests/test_foreground_model_routing.py:1904`
- `tests/test_foreground_model_routing.py:1939`
- `tests/test_foreground_model_routing.py:1968`
- `tests/test_foreground_model_routing.py:1969`
- `tests/test_foreground_model_routing.py:1991`
- `tests/test_foreground_model_routing.py:2015`
- `tests/test_foreground_model_routing.py:2020`
- `tests/test_foreground_model_routing.py:2072`
- `tests/test_foreground_model_routing.py:2107`
- `tests/test_foreground_model_routing.py:2108`
- `tests/test_foreground_model_routing.py:2132`
- `tests/test_foreground_model_routing.py:2133`
- `tests/test_foreground_model_routing.py:2155`
- `tests/test_foreground_model_routing.py:2186`
- `tests/test_foreground_model_routing.py:2209`

## `resolve_foreground_fallback_candidates` — function, line 149
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `build_foreground_model_candidates` — function, line 155
- **called from:**
- `routes/chat_routes.py:1022`
- `routes/chat_routes.py:2062`
- `tests/test_foreground_model_routing.py:1667`
- `tests/test_foreground_model_routing.py:1798`

## `build_foreground_route_descriptors` — function, line 173
- **called from:**
- `routes/chat_routes.py:1029`
- `routes/chat_routes.py:2069`
- `tests/test_foreground_model_routing.py:1707`
