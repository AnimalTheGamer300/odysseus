# `src/bg_monitor.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `FollowupResult` — class, line 30
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_background_result_message` — function, line 36
- **called from:**
- `src/bg_monitor.py:184`
- `tests/test_bg_monitor_stream.py:46`

## `_settle_launch_effect` — function, line 46
- **called from:**
- `src/bg_monitor.py:152`
- `src/bg_monitor.py:177`
- `tests/test_effect_verification_adapters.py:179`

## `_drain_agent` — function (async), line 62
- **called from:**
- `src/agent_jobs.py:317`
- `src/bg_monitor.py:186`
- `tests/test_bg_monitor_stream.py:31`
- `tests/test_bg_monitor_stream.py:85`
- `tests/test_headless_completion_consumers.py:95`
- `tests/test_headless_completion_consumers.py:124`

## `_run_followup` — function (async), line 130
- **called from:**
- `src/agent_jobs.py:346`
- `src/bg_monitor.py:215`
- `tests/test_agent_jobs.py:228`
- `tests/test_agent_jobs.py:250`
- `tests/test_agent_jobs.py:263`
- `tests/test_agent_jobs.py:274`
- `tests/test_agent_jobs.py:284`

## `_process_followup` — function (async), line 214
- **called from:**
- `src/bg_monitor.py:231`
- `tests/test_wave3_background_followup.py:42`
- `tests/test_wave3_background_followup.py:55`
- `tests/test_wave3_background_followup.py:58`
- `tests/test_wave3_background_followup.py:68`
- `tests/test_wave3_background_followup.py:89`
- `tests/test_wave3_background_followup.py:99`
- `tests/test_wave3_background_followup.py:113`

## `_loop` — function (async), line 226
- **called from:**
- `src/agent_jobs.py:363`
- `src/bg_monitor.py:245`
- `src/task_scheduler.py:691`

## `start_bg_monitor` — function, line 240
- **called from:**
- `app.py:1236`
