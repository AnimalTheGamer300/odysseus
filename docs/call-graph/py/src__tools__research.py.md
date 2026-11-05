# `src/tools/research.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `do_manage_research` — function (async), line 18
- **called from:**
- `src/tool_execution.py:2477`
- `tests/test_research_report_read.py:44`
- `tests/test_research_report_read.py:55`

## `_load` — function, line 43
- **called from:**
- `core/auth.py:126`
- `routes/prefs_routes.py:32`
- `routes/prefs_routes.py:58`
- `scripts/analyze_odysseus_eval_targets.py:122`
- `scripts/summarize_odysseus_eval_delta.py:147`
- `scripts/summarize_odysseus_eval_delta.py:150`
- `src/agent_runtime/process_resources.py:171`
- `src/bg_jobs.py:175`
- `src/bg_jobs.py:244`
- `src/bg_jobs.py:363`
- `src/bg_jobs.py:375`
- `src/bg_jobs.py:387`
- `src/bg_jobs.py:397`
- `src/bg_jobs.py:413`
- `src/bg_jobs.py:457`
- `src/foreground_model_routing.py:51`
- `src/mcp_oauth.py:140`
- `src/mcp_oauth.py:148`
- `src/tools/research.py:55`
- `src/tools/research.py:82`
- `tests/cli/test_preset_cli_store.py:12`
- `tests/test_auth_config_lock_concurrency.py:83`
- `tests/test_background_resource_identity.py:39`
- `tests/test_background_resource_identity.py:114`
- `tests/test_background_resource_identity.py:259`
- `tests/test_background_resource_identity.py:270`
- `tests/test_bg_job_tools.py:55`
- `tests/test_bg_jobs_store.py:11`
- `tests/test_bg_jobs_store.py:28`
- `tests/test_foreground_model_routing.py:2105`
- `tests/test_foreground_model_routing.py:2186`
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
- `tests/test_orphan_reaping.py:357`
- `tests/test_orphan_reaping.py:382`
- `tests/test_orphan_reaping.py:392`
- `tests/test_prefs_routes.py:11`
- `tests/test_prefs_routes.py:39`
- `tests/test_runtime_resource_integration.py:272`
- `tests/test_search_query_nonstring.py:26`
- `tests/test_search_query_nonstring.py:37`
- `tests/test_wave3_background_followup.py:35`
- `static/js/workspace.js:109`
- `static/js/workspace.js:152`
- `static/js/workspace.js:212`

## `_completed_label` — function, line 96
- **called from:**
- `src/tools/research.py:103`

## `do_trigger_research` — function (async), line 109
- **called from:**
- `src/tool_execution.py:2474`
- `tests/test_background_tool_jobs.py:167`
