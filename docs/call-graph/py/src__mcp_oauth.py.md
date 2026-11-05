# `src/mcp_oauth.py` — definitions & call sites

18 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_resolve_redirect_base` — function, line 19
- **called from:**
- `src/mcp_oauth.py:43`
- `tests/test_mcp_oauth.py:152`

## `_prune_stale` — function, line 54
- **called from:**
- `src/mcp_oauth.py:74`

## `_discard_pending` — function, line 66
- **called from:**
- `src/mcp_oauth.py:202`

## `register_pending` — function, line 73
- **called from:**
- `src/mcp_oauth.py:183`
- `tests/test_mcp_oauth.py:8`
- `tests/test_mcp_oauth.py:26`
- `tests/test_mcp_oauth.py:30`
- `tests/test_mcp_oauth.py:341`

## `resolve_pending` — function, line 81
- **called from:**
- `routes/mcp/mcp_routes.py:517`
- `routes/mcp/mcp_routes.py:554`
- `tests/test_mcp_oauth.py:9`
- `tests/test_mcp_oauth.py:17`

## `pop_auth_url` — function, line 89
- **called from:**
- `src/mcp_manager.py:365`

## `clear_auth_url` — function, line 93
- **called from:**
- `src/mcp_manager.py:418`
- `src/mcp_manager.py:443`

## `DbTokenStorage` — class, line 97
- **called from:**
- `src/mcp_oauth.py:208`
- `tests/test_mcp_oauth.py:74`
- `tests/test_mcp_oauth.py:109`

## `DbTokenStorage.__init__` — method, line 100
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email/email_helpers.py:205`
- `routes/email/email_helpers.py:220`
- `routes/email/email_helpers.py:232`
- `routes/email/email_helpers.py:248`
- `routes/email/email_routes.py:1664`
- `scripts/css_snapshot.py:194`
- `scripts/probe_browser_budget.py:56`
- `src/agent_tools/document_tools.py:759`
- `src/agent_tools/filesystem_tools.py:384`
- `src/builtin_actions.py:552`
- `src/chatgpt_subscription.py:495`
- `src/containment.py:170`
- `src/outbound_fetch.py:220`
- `src/path_confinement.py:81`
- `src/process_ownership.py:110`
- `src/report_math.py:31`
- `tests/conftest.py:199`
- `tests/test_admin_routes_auth_disabled.py:16`
- `tests/test_agent_state_dir_confinement.py:799`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_action_planning.py:11`
- `tests/test_deep_research_browser_fallback.py:10`
- `tests/test_deep_research_browser_fallback.py:29`
- `tests/test_deep_research_browser_fallback.py:56`
- `tests/test_deep_research_extraction_controls.py:13`
- `tests/test_deep_research_full_loop_navigation.py:11`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_llm_core_streaming.py:50`
- `tests/test_retired_settings_interfaces.py:31`
- `tests/test_searxng_ca_validation.py:35`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:155`

## `DbTokenStorage._load` — method, line 107
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

## `DbTokenStorage._update` — method, line 120
- **called from:**
- `src/mcp_oauth.py:144`
- `src/mcp_oauth.py:152`
- `tests/test_mcp_oauth.py:131`

## `DbTokenStorage.get_tokens` — method (async), line 138
- **called from:**
- `tests/test_mcp_oauth.py:78`
- `tests/test_mcp_oauth.py:123`

## `DbTokenStorage.set_tokens` — method (async), line 143
- **called from:**
- `tests/test_mcp_oauth.py:77`

## `DbTokenStorage.get_client_info` — method (async), line 146
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DbTokenStorage.set_client_info` — method (async), line 151
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `build_provider` — function, line 155
- **called from:**
- `src/mcp_manager.py:385`
- `tests/test_mcp_oauth.py:41`

## `redirect_handler` — function (async), line 180
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `callback_handler` — function (async), line 192
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
