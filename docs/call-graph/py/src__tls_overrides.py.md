# `src/tls_overrides.py` — definitions & call sites

2 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_build_ssl_context` — function, line 50
- **called from:**
- `src/tls_overrides.py:83`

## `llm_verify` — function, line 86
- **called from:**
- `routes/model_routes.py:744`
- `routes/model_routes.py:942`
- `routes/model_routes.py:988`
- `routes/model_routes.py:1009`
- `routes/model_routes.py:1052`
- `routes/model_routes.py:1129`
- `routes/model_routes.py:1140`
- `routes/model_routes.py:1148`
- `src/llm_core.py:523`
- `src/llm_core.py:898`
- `tests/test_tls_overrides_scope.py:130`
- `tests/test_tls_overrides_scope.py:132`
- `tests/test_tls_overrides_scope.py:147`
