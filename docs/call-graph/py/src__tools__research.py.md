# `src/tools/research.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `do_manage_research` — function (async), line 17
- **called from:**
- `src/tool_execution.py:1293`
- `tests/test_research_report_read.py:45`
- `tests/test_research_report_read.py:56`

## `_load` — function, line 42
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

## `do_trigger_research` — function (async), line 95
- **called from:**
- `src/tool_execution.py:1290`
