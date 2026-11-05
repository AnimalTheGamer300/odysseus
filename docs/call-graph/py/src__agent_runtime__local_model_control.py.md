# `src/agent_runtime/local_model_control.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_digest` — function, line 24
- **called from:**
- `src/agent_evidence.py:628`
- `src/agent_evidence.py:802`
- `src/agent_evidence.py:803`
- `src/agent_runtime/local_model_control.py:72`
- `src/agent_runtime/local_model_control.py:98`

## `_Capability` — class, line 30
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/local_model_control.py:72`

## `model_control_headers` — function, line 40
- decorator: `contextmanager`
- **called from:**
- `src/builtin_actions.py:3550`
- `src/tools/cookbook.py:776`
- `src/tools/cookbook.py:863`
- `src/tools/cookbook.py:1916`
- `tests/test_wave3_local_control.py:165`
- `tests/test_wave3_local_control.py:188`

## `consume_model_control` — function, line 84
- **called from:**
- `routes/cookbook_routes.py:425`
