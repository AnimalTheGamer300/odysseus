# `src/bg_monitor.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_background_result_message` — function, line 29
- **called from:**
- `src/bg_monitor.py:122`
- `tests/test_bg_monitor_stream.py:46`

## `_drain_agent` — function (async), line 39
- **called from:**
- `src/agent_jobs.py:317`
- `src/bg_monitor.py:124`
- `tests/test_bg_monitor_stream.py:31`
- `tests/test_bg_monitor_stream.py:85`

## `_run_followup` — function (async), line 92
- **called from:**
- `src/agent_jobs.py:346`
- `src/bg_monitor.py:151`
- `tests/test_agent_jobs.py:228`
- `tests/test_agent_jobs.py:250`
- `tests/test_agent_jobs.py:263`
- `tests/test_agent_jobs.py:274`
- `tests/test_agent_jobs.py:284`

## `_loop` — function (async), line 146
- **called from:**
- `src/agent_jobs.py:363`
- `src/bg_monitor.py:166`
- `src/task_scheduler.py:550`

## `start_bg_monitor` — function, line 161
- **called from:**
- `app.py:1063`
