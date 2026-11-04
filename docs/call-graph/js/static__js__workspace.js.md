# `static/js/workspace.js` — definitions & call sites

15 definitions (regex-based, best-effort).
**Exports:** `applyMode`, `clearWorkspace`, `closeWorkspaceBrowser`, `default`, `getWorkspace`, `initWorkspace`, `openWorkspaceBrowser`, `setWorkspace`, `syncWorkspaceIndicator`, `vetAndSetWorkspace`

## `getWorkspace` — function, line 18
- **called from:**
- `static/js/slashCommands.js:1265`
- `static/js/workspace.js:18`
- `static/js/workspace.js:57`
- `static/js/workspace.js:189`
- `static/js/workspace.js:201`

## `_basename` — function, line 22
- **called from:**
- `static/js/workspace.js:22`
- `static/js/workspace.js:46`
- `static/js/workspace.js:176`

## `_isChatMode` — function, line 31
- **called from:**
- `static/js/workspace.js:31`
- `static/js/workspace.js:37`

## `syncWorkspaceIndicator` — function, line 36
- **called from:**
- `static/js/workspace.js:36`
- `static/js/workspace.js:57`
- `static/js/workspace.js:63`
- `static/js/workspace.js:201`

## `applyMode` — function, line 56
- **called from:**
- `static/app.js:1849`
- `static/js/workspace.js:56`

## `setWorkspace` — function, line 60
- **called from:**
- `static/js/chat.js:3664`
- `static/js/workspace.js:60`
- `static/js/workspace.js:78`
- `static/js/workspace.js:88`
- `static/js/workspace.js:175`

## `vetAndSetWorkspace` — function, line 72
- **called from:**
- `static/js/slashCommands.js:1275`
- `static/js/workspace.js:72`

## `clearWorkspace` — function, line 87
- **called from:**
- `static/js/slashCommands.js:1282`
- `static/js/workspace.js:87`

## `_load` — function, line 92
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

## `_render` — function, line 99
- **called from:**
- `static/js/calendar.js:137`
- `static/js/calendar.js:220`
- `static/js/calendar.js:265`
- `static/js/calendar.js:269`
- `static/js/calendar.js:298`
- `static/js/calendar.js:331`
- `static/js/calendar.js:356`
- `static/js/calendar.js:496`
- `static/js/calendar.js:750`
- `static/js/calendar.js:753`
- `static/js/calendar.js:793`
- `static/js/calendar.js:796`
- `static/js/calendar.js:803`
- `static/js/calendar.js:1202`
- `static/js/calendar.js:1477`
- `static/js/calendar.js:1481`
- `static/js/calendar.js:1485`
- `static/js/calendar.js:1535`
- `static/js/calendar.js:1539`
- `static/js/calendar.js:1544`
- `static/js/calendar.js:1845`
- `static/js/calendar.js:1855`
- `static/js/calendar.js:2089`
- `static/js/calendar.js:2183`
- `static/js/calendar.js:2192`
- `static/js/calendar.js:2194`
- `static/js/calendar.js:2200`
- `static/js/calendar.js:2210`
- `static/js/calendar.js:2226`
- `static/js/calendar.js:2229`
- `static/js/calendar.js:2232`
- `static/js/calendar.js:2301`
- `static/js/calendar.js:2333`
- `static/js/calendar.js:2338`
- `static/js/calendar.js:2385`
- `static/js/calendar.js:2397`
- `static/js/calendar.js:2473`
- `static/js/calendar.js:2607`
- `static/js/calendar.js:2613`
- `static/js/calendar.js:2628`
- `static/js/calendar.js:2670`
- `static/js/calendar.js:2685`
- `static/js/calendar.js:2708`
- `static/js/calendar.js:2747`
- `static/js/calendar.js:3130`
- `static/js/calendar.js:3205`
- `static/js/calendar.js:3340`
- `static/js/calendar.js:3477`
- `static/js/calendar.js:3527`
- `static/js/calendar.js:3547`
- `static/js/calendar.js:3566`
- `static/js/calendar.js:3584`
- `static/js/calendar.js:3675`
- `static/js/calendar.js:3698`
- `static/js/calendar.js:3713`
- `static/js/group.js:64`
- `static/js/group.js:78`
- `static/js/group.js:115`
- `static/js/group.js:314`
- `static/js/slashAutocomplete.js:159`
- … +6 more (grep the name in repo)

## `_navigate` — function, line 133
- **called from:**
- `static/js/workspace.js:122`
- `static/js/workspace.js:133`
- `static/js/workspace.js:171`

## `_getModal` — function, line 141
- **called from:**
- `static/js/calendar.js:668`
- `static/js/calendar.js:3491`
- `static/js/workspace.js:141`
- `static/js/workspace.js:186`

## `openWorkspaceBrowser` — function, line 185
- **called from:**
- `static/js/slashCommands.js:1287`
- `static/js/workspace.js:185`

## `closeWorkspaceBrowser` — function, line 195
- **called from:**
- `static/js/workspace.js:177`
- `static/js/workspace.js:195`

## `initWorkspace` — function, line 199
- **called from:**
- `static/app.js:1980`
- `static/js/workspace.js:199`
