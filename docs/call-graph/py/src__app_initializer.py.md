# `src/app_initializer.py` — definitions & call sites

2 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `create_directories` — function, line 30
- **called from:**
- `src/app_initializer.py:74`
- `src/config.py:205`
- `tests/test_agent_state_dir_confinement.py:183`
- `tests/test_agent_state_dir_confinement.py:204`

## `initialize_managers` — function, line 63
- **called from:**
- `app.py:585`
- `tests/test_app_initializer_memory_vector_degraded.py:55`
