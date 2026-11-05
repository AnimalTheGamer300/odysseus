# `static/js/workspace.js` — definitions & call sites

16 definitions (regex-based, best-effort).
**Exports:** `applyMode`, `clearWorkspace`, `closeWorkspaceBrowser`, `default`, `getWorkspace`, `initWorkspace`, `loadDefaultWorkspace`, `openWorkspaceBrowser`, `setWorkspace`, `syncWorkspaceIndicator`, `vetAndSetWorkspace`

## `getWorkspace` — function, line 19
- **called from:**
- `static/js/slashCommands.js:1265`
- `static/js/workspace.js:19`
- `static/js/workspace.js:58`
- `static/js/workspace.js:94`
- `static/js/workspace.js:212`
- `static/js/workspace.js:224`

## `_basename` — function, line 23
- **called from:**
- `static/js/workspace.js:23`
- `static/js/workspace.js:47`
- `static/js/workspace.js:199`

## `_isChatMode` — function, line 32
- **called from:**
- `static/js/workspace.js:32`
- `static/js/workspace.js:38`

## `syncWorkspaceIndicator` — function, line 37
- **called from:**
- `static/js/workspace.js:37`
- `static/js/workspace.js:58`
- `static/js/workspace.js:64`
- `static/js/workspace.js:225`

## `applyMode` — function, line 57
- **called from:**
- `static/app.js:1905`
- `static/js/workspace.js:57`

## `setWorkspace` — function, line 61
- **called from:**
- `static/js/chat.js:5216`
- `static/js/slashCommands.js:1282`
- `static/js/slashCommands.js:1294`
- `static/js/workspace.js:61`
- `static/js/workspace.js:79`
- `static/js/workspace.js:95`
- `static/js/workspace.js:105`
- `static/js/workspace.js:198`

## `vetAndSetWorkspace` — function, line 73
- **called from:**
- `static/js/slashCommands.js:1275`
- `static/js/workspace.js:73`

## `loadDefaultWorkspace` — function, line 88
- **called from:**
- `static/js/workspace.js:88`
- `static/js/workspace.js:228`

## `clearWorkspace` — function, line 104
- **called from:**
- `static/js/slashCommands.js:1285`
- `static/js/workspace.js:104`
- `static/js/workspace.js:238`

## `_load` — function, line 109
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

## `_render` — function, line 116
- **called from:**
- `tests/test_codeql_python_residual_closure.py:583`
- `tests/test_codeql_python_residual_closure.py:586`
- `tests/test_codeql_python_residual_closure.py:591`
- `static/js/calendar.js:142`
- `static/js/calendar.js:225`
- `static/js/calendar.js:273`
- `static/js/calendar.js:278`
- `static/js/calendar.js:312`
- `static/js/calendar.js:341`
- `static/js/calendar.js:366`
- `static/js/calendar.js:585`
- `static/js/calendar.js:776`
- `static/js/calendar.js:881`
- `static/js/calendar.js:884`
- `static/js/calendar.js:924`
- `static/js/calendar.js:927`
- `static/js/calendar.js:934`
- `static/js/calendar.js:1342`
- `static/js/calendar.js:1914`
- `static/js/calendar.js:1918`
- `static/js/calendar.js:1922`
- `static/js/calendar.js:1972`
- `static/js/calendar.js:1976`
- `static/js/calendar.js:1981`
- `static/js/calendar.js:2361`
- `static/js/calendar.js:2373`
- `static/js/calendar.js:2650`
- `static/js/calendar.js:2745`
- `static/js/calendar.js:2761`
- `static/js/calendar.js:2768`
- `static/js/calendar.js:2775`
- `static/js/calendar.js:2785`
- `static/js/calendar.js:2801`
- `static/js/calendar.js:2804`
- `static/js/calendar.js:2807`
- `static/js/calendar.js:2876`
- `static/js/calendar.js:2924`
- `static/js/calendar.js:2929`
- `static/js/calendar.js:2976`
- `static/js/calendar.js:2990`
- `static/js/calendar.js:3066`
- `static/js/calendar.js:3217`
- `static/js/calendar.js:3223`
- `static/js/calendar.js:3238`
- `static/js/calendar.js:3280`
- `static/js/calendar.js:3301`
- `static/js/calendar.js:3324`
- `static/js/calendar.js:3366`
- `static/js/calendar.js:3802`
- `static/js/calendar.js:3880`
- `static/js/calendar.js:4015`
- `static/js/calendar.js:4227`
- `static/js/calendar.js:4244`
- `static/js/calendar.js:4304`
- `static/js/calendar.js:4324`
- `static/js/calendar.js:4344`
- `static/js/calendar.js:4366`
- `static/js/calendar.js:4504`
- `static/js/calendar.js:4547`
- `static/js/calendar.js:4570`
- … +12 more (grep the name in repo)

## `_navigate` — function, line 150
- **called from:**
- `static/js/workspace.js:139`
- `static/js/workspace.js:150`
- `static/js/workspace.js:194`

## `_getModal` — function, line 158
- **called from:**
- `static/js/calendar.js:757`
- `static/js/calendar.js:4231`
- `static/js/calendar.js:4265`
- `static/js/workspace.js:158`
- `static/js/workspace.js:209`

## `openWorkspaceBrowser` — function, line 208
- **called from:**
- `static/js/slashCommands.js:1290`
- `static/js/workspace.js:208`

## `closeWorkspaceBrowser` — function, line 218
- **called from:**
- `static/js/workspace.js:187`
- `static/js/workspace.js:200`
- `static/js/workspace.js:218`

## `initWorkspace` — function, line 222
- **called from:**
- `static/app.js:2038`
- `static/js/workspace.js:222`
