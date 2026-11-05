# `src/interactive_gate.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_enabled` — function, line 23
- **called from:**
- `src/interactive_gate.py:86`
- `src/interactive_gate.py:94`
- `src/interactive_gate.py:108`
- `src/interactive_gate.py:131`
- `src/interactive_gate.py:167`
- `src/interactive_gate.py:191`

## `_quiet_seconds` — function, line 27
- **called from:**
- `src/interactive_gate.py:136`
- `src/interactive_gate.py:194`

## `_max_wait_seconds` — function, line 34
- **called from:**
- `src/interactive_gate.py:195`

## `_browser_active_seconds` — function, line 42
- **called from:**
- `src/interactive_gate.py:117`

## `_condition` — function, line 50
- **called from:**
- `src/interactive_gate.py:110`
- `src/interactive_gate.py:171`
- `src/interactive_gate.py:197`

## `maybe_stop_background_tasks_for_heartbeat` — function (async), line 80
- **called from:**
- `app.py:733`
- `tests/test_poll_endpoint_no_task_interrupt.py:41`
- `tests/test_poll_endpoint_no_task_interrupt.py:60`

## `should_track_interactive_request` — function, line 93
- **called from:**
- `app.py:225`
- `tests/test_interactive_gate_passive_paths.py:7`
- `tests/test_interactive_gate_passive_paths.py:8`
- `tests/test_interactive_gate_passive_paths.py:12`
- `tests/test_interactive_gate_passive_paths.py:13`
- `tests/test_interactive_gate_passive_paths.py:14`
- `tests/test_interactive_gate_passive_paths.py:18`
- `tests/test_interactive_gate_passive_paths.py:19`
- `tests/test_poll_endpoint_no_task_interrupt.py:17`
- `tests/test_poll_endpoint_no_task_interrupt.py:26`

## `mark_browser_activity` — function (async), line 105
- **called from:**
- `app.py:729`

## `_has_recent_browser_activity` — function, line 116
- **called from:**
- `src/interactive_gate.py:138`
- `src/interactive_gate.py:205`

## `has_foreground_activity` — function, line 123
- **called from:**
- `src/llm_core.py:151`
- `src/task_scheduler.py:852`
- `src/task_scheduler.py:1059`

## `_has_active_chat_stream` — function, line 141
- **called from:**
- `src/interactive_gate.py:138`
- `src/interactive_gate.py:204`

## `track_interactive_request` — function (async), line 165
- decorator: `asynccontextmanager`
- **called from:**
- `app.py:233`

## `wait_for_interactive_quiet` — function (async), line 185
- **called from:**
- `src/builtin_actions.py:726`
- `src/builtin_actions.py:1622`
- `src/builtin_actions.py:1909`
- `src/builtin_actions.py:3011`
- `src/task_endpoint.py:105`
- `src/task_scheduler.py:1014`
- `src/task_scheduler.py:2063`
