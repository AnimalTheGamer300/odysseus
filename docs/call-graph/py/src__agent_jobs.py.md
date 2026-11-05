# `src/agent_jobs.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_ensure_loaded` — function, line 63
- **called from:**
- `src/agent_jobs.py:145`
- `src/agent_jobs.py:268`
- `src/agent_jobs.py:399`
- `tests/test_agent_jobs.py:64`
- `tests/test_agent_jobs.py:75`
- `tests/test_agent_jobs.py:215`
- `tests/test_agent_jobs.py:241`
- `tests/test_agent_jobs.py:258`
- `tests/test_agent_jobs.py:270`
- `tests/test_agent_jobs.py:281`
- `tests/test_agent_jobs.py:293`
- `tests/test_agent_jobs.py:303`
- `tests/test_agent_jobs.py:309`
- `tests/test_agent_jobs.py:317`

## `_load_registry` — function, line 68
- **called from:**
- `src/agent_jobs.py:65`

## `_save_registry` — function, line 95
- **called from:**
- `src/agent_jobs.py:179`
- `src/agent_jobs.py:248`
- `src/agent_jobs.py:259`
- `src/agent_jobs.py:348`
- `src/agent_jobs.py:411`
- `src/agent_jobs.py:427`
- `tests/test_agent_jobs.py:66`
- `tests/test_agent_jobs.py:80`

## `_reset_for_tests` — function, line 116
- **called from:**
- `tests/test_agent_jobs.py:40`
- `tests/test_agent_jobs.py:43`
- `tests/test_agent_jobs.py:67`

## `launch_background_agent` — function (async), line 129
- **called from:**
- `src/agent_tools/spawn_agent_tools.py:274`
- `tests/test_agent_jobs.py:107`
- `tests/test_agent_jobs.py:136`
- `tests/test_agent_jobs.py:143`
- `tests/test_agent_jobs.py:159`
- `tests/test_agent_jobs.py:178`

## `_run_agent_job` — function (async), line 199
- **called from:**
- `src/agent_jobs.py:181`

## `pending_deliveries` — function, line 266
- **called from:**
- `src/agent_jobs.py:344`

## `_run_followup` — function (async), line 275
- **called from:**
- `src/agent_jobs.py:346`
- `src/bg_monitor.py:215`
- `tests/test_agent_jobs.py:228`
- `tests/test_agent_jobs.py:250`
- `tests/test_agent_jobs.py:263`
- `tests/test_agent_jobs.py:274`
- `tests/test_agent_jobs.py:284`

## `_loop` — function (async), line 341
- **called from:**
- `src/agent_jobs.py:363`
- `src/bg_monitor.py:245`
- `src/task_scheduler.py:691`

## `start_agent_job_monitor` — function, line 358
- **called from:**
- `app.py:1243`

## `_fmt_age` — function, line 372
- **called from:**
- `src/agent_jobs.py:383`
- `src/agent_jobs.py:388`

## `_fmt_rec` — function, line 381
- **called from:**
- `src/agent_jobs.py:407`
- `src/agent_jobs.py:421`

## `collect_status` — function, line 396
- **called from:**
- `src/agent_tools/spawn_agent_tools.py:321`
- `tests/test_agent_jobs.py:55`
- `tests/test_agent_jobs.py:68`
- `tests/test_agent_jobs.py:120`
- `tests/test_agent_jobs.py:123`
- `tests/test_agent_jobs.py:162`
- `tests/test_agent_jobs.py:296`
- `tests/test_agent_jobs.py:304`
- `tests/test_agent_jobs.py:311`
- `tests/test_agent_jobs.py:318`
