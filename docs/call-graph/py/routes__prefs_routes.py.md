# `routes/prefs_routes.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_load` — function, line 16
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

## `_save` — function, line 26
- **called from:**
- `core/auth.py:200`
- `core/auth.py:221`
- `core/auth.py:237`
- `core/auth.py:254`
- `core/auth.py:299`
- `core/auth.py:336`
- `core/auth.py:370`
- `core/auth.py:428`
- `core/auth.py:502`
- `core/auth.py:514`
- `core/auth.py:527`
- `core/auth.py:547`
- `core/auth.py:573`
- `core/auth.py:595`
- `core/auth.py:611`
- `routes/prefs_routes.py:89`
- `routes/prefs_routes.py:91`
- `routes/prefs_routes.py:100`
- `src/bg_jobs.py:177`
- `src/bg_jobs.py:313`
- `src/bg_jobs.py:369`
- `src/bg_jobs.py:382`
- `src/bg_jobs.py:432`
- `src/bg_jobs.py:481`
- `tests/test_background_containment.py:131`
- `tests/test_background_resource_identity.py:41`
- `tests/test_background_resource_identity.py:116`
- `tests/test_background_resource_identity.py:261`
- `tests/test_background_resource_identity.py:272`
- `tests/test_bg_job_tools.py:57`
- `tests/test_orphan_reaping.py:83`
- `tests/test_prefs_atomic_write.py:19`
- `tests/test_runtime_resource_integration.py:125`
- `tests/test_runtime_resource_integration.py:264`
- `tests/test_runtime_resource_integration.py:279`
- `tests/test_wave3_background_followup.py:38`
- `tests/test_wave3_background_followup.py:66`
- `tests/test_wave3_launch_cost_lifecycle.py:112`
- `tests/test_wave3_launch_cost_lifecycle.py:118`

## `_load_for_user` — function, line 30
- **called from:**
- `routes/backup_routes.py:42`
- `routes/backup_routes.py:211`
- `routes/calendar_routes.py:974`
- `routes/model_routes.py:2809`
- `routes/prefs_routes.py:109`
- `routes/prefs_routes.py:114`
- `routes/prefs_routes.py:120`
- `routes/task/task_routes.py:385`
- `routes/task/task_routes.py:394`
- `services/memory/skills.py:63`
- `services/skills/publication.py:15`
- `src/ai_interaction.py:829`
- `src/ai_interaction.py:838`
- `src/ai_interaction.py:930`
- `src/ai_interaction.py:1125`
- `src/builtin_actions.py:3597`
- `src/caldav_sync.py:593`
- `src/foreground_model_routing.py:48`
- `src/settings.py:350`
- `src/settings.py:360`
- `src/task_scheduler.py:2512`
- `tests/test_editor_generation_model_routing.py:482`
- `tests/test_editor_generation_model_routing.py:495`
- `tests/test_foreground_model_routing.py:2100`
- `tests/test_foreground_model_routing.py:2179`
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
- `routes/calendar_routes.py:977`
- `routes/prefs_routes.py:126`
- `routes/task/task_routes.py:399`
- `src/ai_interaction.py:851`
- `src/ai_interaction.py:940`
- `src/builtin_actions.py:3603`
- `src/caldav_sync.py:610`
- `tests/test_editor_generation_model_routing.py:136`
- `tests/test_editor_generation_model_routing.py:137`
- `tests/test_editor_generation_model_routing.py:312`
- `tests/test_editor_generation_model_routing.py:367`
- `tests/test_editor_generation_model_routing.py:422`
- `tests/test_editor_generation_model_routing.py:481`
- `tests/test_foreground_model_routing.py:2102`
- `tests/test_foreground_model_routing.py:2184`
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
- `app.py:903`
- `tests/test_editor_generation_model_routing.py:181`
- `tests/test_editor_generation_model_routing.py:485`

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
