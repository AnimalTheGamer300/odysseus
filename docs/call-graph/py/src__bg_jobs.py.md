# `src/bg_jobs.py` — definitions & call sites

14 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_load` — function, line 57
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

## `_save` — function, line 69
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

## `_pid_alive` — function, line 73
- **called from:**
- `src/bg_jobs.py:218`

## `launch` — function, line 81
- **called from:**
- `src/tool_execution.py:1118`
- `tests/markdown_browser_check.py:66`
- `tests/markdown_screenshot.py:80`
- `static/js/cookbookRunning.js:3496`
- `static/js/cookbookServe.js:1643`
- `static/js/emailLibrary.js:8322`
- `static/js/emailLibrary.js:8327`

## `_read_output` — function, line 162
- **called from:**
- `src/bg_jobs.py:258`
- `src/bg_jobs.py:288`

## `_prune` — function, line 175
- **called from:**
- `src/bg_jobs.py:226`
- `tests/test_caldav_sync_prune_local_events.py:82`
- `tests/test_caldav_sync_prune_local_events.py:96`

## `refresh` — function, line 191
- **called from:**
- `routes/calendar_routes.py:1443`
- `routes/document/document_routes.py:174`
- `routes/document/document_routes.py:204`
- `routes/document/document_routes.py:317`
- `routes/document/document_routes.py:687`
- `routes/document/document_routes.py:726`
- `routes/document/document_routes.py:841`
- `routes/editor_draft_routes.py:128`
- `routes/editor_draft_routes.py:158`
- `routes/gallery/gallery_routes.py:978`
- `routes/note/note_routes.py:682`
- `routes/note/note_routes.py:754`
- `routes/signature_routes.py:121`
- `routes/task/task_routes.py:556`
- `routes/task/task_routes.py:751`
- `routes/task/task_routes.py:852`
- `src/bg_jobs.py:241`
- `src/bg_jobs.py:254`
- `src/bg_jobs.py:263`
- `src/chatgpt_subscription.py:271`
- `src/chatgpt_subscription.py:281`
- `src/tools/image.py:83`
- `static/js/chatRenderer.js:3112`
- `static/js/chatStream.js:171`
- `static/js/cookbookDownload.js:174`
- `static/js/editor/tools/transform-session.js:148`
- `static/js/editor/tools/transform-session.js:161`
- `static/js/search.js:42`
- `static/js/settings.js:488`
- `static/js/settings.js:775`
- `static/js/settings.js:1167`
- `static/js/slashAutocomplete.js:253`
- `static/js/slashAutocomplete.js:266`

## `_kill` — function, line 233
- **called from:**
- `src/bg_jobs.py:212`
- `src/bg_jobs.py:276`

## `pending_followups` — function, line 238
- **called from:**
- `src/bg_monitor.py:149`

## `mark_followed_up` — function, line 246
- **called from:**
- `src/bg_monitor.py:152`

## `get` — function, line 253
- **called from:**
- `app.py:359`
- `app.py:383`
- `app.py:389`
- `app.py:416`
- `app.py:428`
- `app.py:470`
- `app.py:538`
- `app.py:512`
- `app.py:595`
- `app.py:891`
- `app.py:903`
- `app.py:907`
- `app.py:915`
- `app.py:919`
- `app.py:923`
- `app.py:927`
- `app.py:931`
- `app.py:935`
- `app.py:939`
- `app.py:944`
- `app.py:950`
- `app.py:955`
- `app.py:967`
- `app.py:968`
- `app.py:969`
- `app.py:969`
- `app.py:971`
- `app.py:971`
- `app.py:975`
- `app.py:996`
- `app.py:987`
- `app.py:998`
- `app.py:1117`
- `app.py:1151`
- `app.py:1165`
- `app.py:1198`
- `app.py:1201`
- `app.py:1216`
- `companion/pairing.py:116`
- `companion/pairing.py:126`
- `companion/pairing.py:173`
- `companion/pairing.py:177`
- `companion/routes.py:85`
- `companion/routes.py:97`
- `companion/routes.py:109`
- `companion/routes.py:168`
- `companion/routes.py:222`
- `core/auth.py:143`
- `core/auth.py:164`
- `core/auth.py:187`
- `core/auth.py:214`
- `core/auth.py:226`
- `core/auth.py:230`
- `core/auth.py:299`
- `core/auth.py:299`
- `core/auth.py:325`
- `core/auth.py:349`
- `core/auth.py:349`
- `core/auth.py:357`
- `core/auth.py:370`
- … +7528 more (grep the name in repo)

## `list_for_session` — function, line 262
- **called from:**
- `src/agent_tools/bg_job_tools.py:71`

## `kill` — function, line 266
- **called from:**
- `core/platform_compat.py:106`
- `core/platform_compat.py:139`
- `routes/codex_routes.py:538`
- `routes/cookbook_helpers.py:1479`
- `routes/cookbook_routes.py:869`
- `routes/cookbook_routes.py:2944`
- `routes/cookbook_routes.py:2973`
- `routes/shell_routes.py:591`
- `routes/shell_routes.py:644`
- `routes/shell_routes.py:652`
- `routes/shell_routes.py:716`
- `routes/shell_routes.py:1082`
- `routes/shell_routes.py:1097`
- `services/shell/service.py:75`
- `services/shell/service.py:152`
- `services/youtube/youtube_handler.py:242`
- `src/agent_tools/bg_job_tools.py:89`
- `src/agent_tools/filesystem_tools.py:893`
- `src/agent_tools/filesystem_tools.py:1009`
- `src/agent_tools/subprocess_tools.py:56`
- `src/agent_tools/subprocess_tools.py:256`
- `src/agent_tools/subprocess_tools.py:265`
- `src/builtin_mcp.py:307`
- `src/builtin_mcp.py:316`
- `tests/test_bg_job_tools.py:56`
- `tests/test_bg_job_tools.py:66`
- `tests/test_bg_job_tools.py:71`
- `tests/test_bg_job_tools.py:78`
- `static/js/cookbookRunning.js:2910`

## `result_text` — function, line 286
- **called from:**
- `src/bg_monitor.py:32`
- `src/bg_monitor.py:137`
- `tests/test_bg_job_tools.py:79`
