# `routes/prefs_routes.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_load` — function, line 16
- **called from:**
- `core/auth.py:108`
- `routes/prefs_routes.py:32`
- `routes/prefs_routes.py:58`
- `src/bg_jobs.py:156`
- `src/bg_jobs.py:194`
- `src/bg_jobs.py:247`
- `src/bg_jobs.py:255`
- `src/bg_jobs.py:271`
- `src/foreground_model_routing.py:51`
- `src/mcp_oauth.py:140`
- `src/mcp_oauth.py:148`
- `src/tools/research.py:54`
- `src/tools/research.py:81`
- `tests/cli/test_preset_cli_store.py:12`
- `tests/test_auth_config_lock_concurrency.py:83`
- `tests/test_bg_job_tools.py:42`
- `tests/test_bg_jobs_store.py:11`
- `tests/test_bg_jobs_store.py:28`
- `tests/test_foreground_model_routing.py:2021`
- `tests/test_foreground_model_routing.py:2102`
- `tests/test_gpu_compose_standalone.py:74`
- `tests/test_gpu_compose_standalone.py:81`
- `tests/test_gpu_compose_standalone.py:82`
- `tests/test_gpu_compose_standalone.py:87`
- `tests/test_gpu_compose_standalone.py:88`
- `tests/test_gpu_compose_standalone.py:97`
- `tests/test_gpu_compose_standalone.py:107`
- `tests/test_gpu_compose_standalone.py:115`
- `tests/test_gpu_compose_standalone.py:142`
- `tests/test_gpu_compose_standalone.py:171`
- `tests/test_gpu_compose_standalone.py:182`
- `tests/test_gpu_compose_standalone.py:183`
- `tests/test_gpu_compose_standalone.py:199`
- `tests/test_gpu_compose_standalone.py:200`
- `tests/test_mcp_oauth.py:116`
- `tests/test_prefs_routes.py:11`
- `tests/test_prefs_routes.py:39`
- `tests/test_search_query_nonstring.py:26`
- `tests/test_search_query_nonstring.py:37`
- `static/js/workspace.js:92`
- `static/js/workspace.js:135`
- `static/js/workspace.js:189`

## `_save` — function, line 26
- **called from:**
- `core/auth.py:182`
- `core/auth.py:203`
- `core/auth.py:219`
- `core/auth.py:236`
- `core/auth.py:281`
- `core/auth.py:318`
- `core/auth.py:352`
- `core/auth.py:401`
- `core/auth.py:464`
- `core/auth.py:476`
- `core/auth.py:496`
- `core/auth.py:522`
- `core/auth.py:544`
- `core/auth.py:560`
- `routes/prefs_routes.py:89`
- `routes/prefs_routes.py:91`
- `routes/prefs_routes.py:100`
- `src/bg_jobs.py:158`
- `src/bg_jobs.py:229`
- `src/bg_jobs.py:250`
- `src/bg_jobs.py:282`
- `tests/test_bg_job_tools.py:44`
- `tests/test_prefs_atomic_write.py:19`

## `_load_for_user` — function, line 30
- **called from:**
- `routes/backup_routes.py:42`
- `routes/backup_routes.py:211`
- `routes/calendar_routes.py:825`
- `routes/model_routes.py:2444`
- `routes/prefs_routes.py:109`
- `routes/prefs_routes.py:114`
- `routes/prefs_routes.py:120`
- `routes/skills_routes.py:552`
- `routes/task/task_routes.py:376`
- `routes/task/task_routes.py:385`
- `src/builtin_actions.py:3312`
- `src/caldav_sync.py:593`
- `src/foreground_model_routing.py:48`
- `src/settings.py:332`
- `src/task_scheduler.py:2309`
- `tests/test_foreground_model_routing.py:2016`
- `tests/test_foreground_model_routing.py:2095`
- `tests/test_prefs_atomic_write.py:37`
- `tests/test_prefs_atomic_write.py:48`
- `tests/test_prefs_routes.py:12`
- `tests/test_prefs_routes.py:20`
- `tests/test_prefs_routes.py:21`
- `tests/test_prefs_routes.py:35`
- `tests/test_prefs_single_user_no_clobber.py:27`
- `tests/test_prefs_single_user_no_clobber.py:70`
- `tests/test_prefs_single_user_no_clobber.py:96`

## `_save_for_user` — function, line 56
- **called from:**
- `routes/backup_routes.py:213`
- `routes/calendar_routes.py:828`
- `routes/prefs_routes.py:122`
- `routes/task/task_routes.py:390`
- `src/builtin_actions.py:3318`
- `src/caldav_sync.py:610`
- `tests/test_foreground_model_routing.py:2018`
- `tests/test_foreground_model_routing.py:2100`
- `tests/test_prefs_atomic_write.py:33`
- `tests/test_prefs_atomic_write.py:44`
- `tests/test_prefs_routes.py:37`
- `tests/test_prefs_single_user_no_clobber.py:29`
- `tests/test_prefs_single_user_no_clobber.py:43`
- `tests/test_prefs_single_user_no_clobber.py:53`
- `tests/test_prefs_single_user_no_clobber.py:75`
- `tests/test_prefs_single_user_no_clobber.py:102`

## `setup_prefs_routes` — function, line 103
- **called from:**
- `app.py:819`

## `get_all_prefs` — function (async), line 107
- decorator: `router.get("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_pref` — function (async), line 112
- **route:** `GET /{key}`
- decorator: `router.get("/{key}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_pref` — function (async), line 118
- **route:** `PUT /{key}`
- decorator: `router.put("/{key}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
