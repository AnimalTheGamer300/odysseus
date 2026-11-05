# `src/browser_lifecycle.py` — definitions & call sites

35 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `runtime_root` — function, line 46
- **called from:**
- `src/agent_tools/web_tools.py:2482`
- `src/agent_tools/web_tools.py:2534`
- `src/agent_tools/web_tools.py:2701`
- `src/agent_tools/web_tools_prewave3.py:2491`
- `src/agent_tools/web_tools_prewave3.py:2543`
- `src/agent_tools/web_tools_prewave3.py:3837`
- `src/browser_lifecycle.py:357`
- `tests/test_browser_lifecycle.py:65`
- `tests/test_browser_lifecycle.py:66`
- `tests/test_browser_lifecycle.py:69`

## `_get` — function, line 56
- **called from:**
- `src/browser_lifecycle.py:59`
- `src/browser_lifecycle.py:62`
- `src/browser_lifecycle.py:65`
- `tests/test_manage_tasks_admin_action_policy.py:111`
- `tests/test_manage_tasks_admin_action_policy.py:141`
- `tests/test_manage_tasks_admin_action_policy.py:152`
- `tests/test_manage_tasks_admin_action_policy.py:164`
- `tests/test_manage_tasks_admin_action_policy.py:174`
- `tests/test_manage_tasks_admin_action_policy.py:185`
- `tests/test_manage_tasks_admin_action_policy.py:262`
- `tests/test_manage_tasks_owner_scope.py:81`
- `tests/test_manage_tasks_owner_scope.py:92`
- `tests/test_manage_tasks_owner_scope.py:103`
- `tests/test_manage_tasks_owner_scope.py:124`
- `tests/test_manage_tasks_owner_scope.py:135`
- `tests/test_manage_tasks_owner_scope.py:148`
- `tests/test_manage_tasks_owner_scope.py:160`
- `tests/test_manage_tasks_owner_scope.py:176`
- `tests/test_manage_tasks_owner_scope.py:177`
- `tests/test_manage_tasks_owner_scope.py:248`
- `tests/test_manage_tasks_owner_scope.py:267`
- `tests/test_manage_tasks_owner_scope.py:268`
- `tests/test_manage_tasks_owner_scope.py:272`
- `tests/test_manage_tasks_owner_scope.py:273`
- `tests/test_manage_tasks_owner_scope.py:278`
- `tests/test_manage_tasks_owner_scope.py:279`
- `static/js/appConfig.js:52`
- `static/js/appConfig.js:70`
- `static/js/appConfig.js:75`

## `_read_cmdline` — function, line 69
- **called from:**
- `src/browser_lifecycle.py:122`
- `src/browser_lifecycle.py:141`

## `_read_stat` — function, line 78
- **called from:**
- `src/browser_lifecycle.py:119`
- `src/browser_lifecycle.py:138`

## `_live_pids` — function, line 95
- **called from:**
- `src/browser_lifecycle.py:154`

## `daemon_pid` — function, line 105
- **called from:**
- `src/browser_lifecycle.py:278`
- `src/browser_lifecycle.py:456`

## `is_verified_daemon` — function, line 114
- **called from:**
- `src/browser_lifecycle.py:461`

## `_Member` — class, line 127
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/browser_lifecycle.py:159`

## `_read_member_facts` — function, line 137
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_snapshot` — function, line 144
- **called from:**
- `src/browser_lifecycle.py:176`
- `tests/test_cookbook_error_tail_lines.py:19`
- `tests/test_cookbook_error_tail_lines.py:28`
- `tests/test_cookbook_error_tail_lines.py:38`
- `tests/test_cookbook_error_tail_lines.py:51`
- `static/js/features/notes/ui/drawing.js:205`
- `static/js/features/notes/ui/drawing.js:280`

## `browser_members` — function, line 167
- **called from:**
- `src/browser_lifecycle.py:195`
- `src/browser_lifecycle.py:226`

## `browser_tree` — function, line 192
- **called from:**
- `src/browser_lifecycle.py:299`
- `tests/test_browser_lifecycle.py:78`
- `tests/test_browser_lifecycle.py:88`

## `_profiles_of` — function, line 198
- **called from:**
- `src/browser_lifecycle.py:187`
- `src/browser_lifecycle.py:227`

## `kill_browser_tree` — function, line 210
- **called from:**
- `src/browser_lifecycle.py:289`
- `tests/test_browser_lifecycle.py:149`

## `CleanupReceipt` — class, line 242
- decorator: `dataclass`
- **called from:**
- `src/browser_lifecycle.py:279`

## `CleanupReceipt.as_dict` — method, line 252
- **called from:**
- `src/agent_tools/web_tools.py:2483`
- `src/agent_tools/web_tools_prewave3.py:2492`

## `force_cleanup` — function, line 265
- **called from:**
- `src/agent_tools/web_tools.py:2483`
- `src/agent_tools/web_tools.py:2701`
- `src/agent_tools/web_tools.py:2708`
- `src/agent_tools/web_tools_prewave3.py:2492`
- `src/agent_tools/web_tools_prewave3.py:3855`
- `tests/test_browser_lifecycle.py:103`
- `tests/test_browser_lifecycle.py:169`
- `tests/test_browser_lifecycle.py:183`
- `tests/test_browser_lifecycle.py:186`
- `tests/test_browser_lifecycle.py:300`
- `tests/test_browser_producer_live_contract.py:40`

## `_remove_runtime_files` — function, line 303
- **called from:**
- `src/browser_lifecycle.py:282`
- `src/browser_lifecycle.py:293`

## `StageClock` — class, line 315
- **called from:**
- `src/agent_tools/web_tools_prewave3.py:2647`

## `StageClock.__init__` — method, line 318
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

## `StageClock.record` — method, line 323
- **called from:**
- `src/agent_tools/web_tools_prewave3.py:2712`
- `src/agent_tools/web_tools_prewave3.py:2731`
- `src/agent_tools/web_tools_prewave3.py:2977`
- `src/agent_tools/web_tools_prewave3.py:3018`
- `src/agent_tools/web_tools_prewave3.py:3044`
- `src/agent_tools/web_tools_prewave3.py:3064`
- `tests/smoke/stub_provider.py:105`
- `static/js/chat.js:6083`
- `static/js/chat.js:6627`
- `static/js/compare/scoreboard.js:21`

## `StageClock.total_ms` — method, line 332
- **called from:**
- `src/browser_lifecycle.py:419`

## `BrowserSession` — class, line 337
- decorator: `dataclass`
- **called from:**
- `src/browser_lifecycle.py:431`

## `BrowserSession.bind` — method, line 353
- **called from:**
- `scripts/verify_frontend_runtime.py:55`
- `scripts/verify_notes_browser_runtime.py:55`
- `scripts/verify_notes_browser_runtime.py:57`
- `src/agent_runtime/authority.py:577`
- `src/agent_runtime/completion.py:213`
- `src/agent_runtime/journal.py:245`
- `src/agent_runtime/resource_binding.py:159`
- `src/agent_runtime/resource_binding.py:192`
- `src/agent_tools/web_tools_prewave3.py:2969`
- `src/chat_helpers.py:229`
- `src/turn_contract.py:6508`
- `src/url_safety.py:267`
- `tests/cli/test_dev_cli_isolation.py:95`
- `tests/helpers/unix_sockets.py:42`
- `tests/runtime_evidence_helpers.py:26`
- `tests/test_chroma_client.py:19`
- `tests/test_chroma_client.py:32`
- `tests/test_codeql_python_residual_closure.py:127`
- `tests/test_codeql_python_residual_closure.py:557`
- `tests/test_security_regressions.py:1355`
- `tests/test_skill_importer_dns_pinning.py:163`
- `tests/test_worker_runtime.py:81`
- `static/js/editor/text-layer.js:121`
- `static/js/editor/text-layer.js:121`
- `static/js/editor/wire-extra-menus.js:116`
- `static/js/editor/wire-extra-menus.js:145`
- `static/js/editor/wire-extra-menus.js:172`
- `static/js/editor/wire-extra-menus.js:183`
- `static/js/editor/wire-extra-menus.js:199`
- `static/js/editor/wire-extra-menus.js:220`
- `static/js/editor/wire-extra-menus.js:243`
- `static/js/editor/wire-extra-menus.js:249`
- `static/js/editor/wire-extra-menus.js:255`
- `static/js/features/notes/application/state.js:36`
- `static/js/galleryEditor.js:12846`
- `static/js/providerDeviceFlow.js:77`
- `static/js/slashCommands.js:1273`

## `BrowserSession.lock` — method, line 360
- **called from:**
- `src/agent_tools/web_tools_prewave3.py:2650`

## `BrowserSession.navigated` — method, line 367
- **called from:**
- `src/agent_tools/web_tools_prewave3.py:3083`

## `BrowserSession.navigation_failed` — method, line 374
- **called from:**
- `src/agent_tools/web_tools_prewave3.py:3090`

## `BrowserSession.navigation_unknown` — method, line 379
- **called from:**
- `src/agent_tools/web_tools_prewave3.py:3092`

## `BrowserSession.discarded` — method, line 387
- **called from:**
- `src/agent_tools/web_tools_prewave3.py:2668`
- `src/agent_tools/web_tools_prewave3.py:2716`
- `src/agent_tools/web_tools_prewave3.py:2733`
- `src/agent_tools/web_tools_prewave3.py:2978`

## `BrowserSession.stale_observation_note` — method, line 395
- **called from:**
- `src/agent_tools/web_tools_prewave3.py:2981`

## `BrowserSession.receipt` — method, line 411
- **called from:**
- `src/agent_tools/web_tools_prewave3.py:2659`

## `session_for` — function, line 428
- **called from:**
- `src/agent_tools/web_tools_prewave3.py:2646`

## `forget` — function, line 436
- **called from:**
- `src/agent_tools/web_tools.py:2703`
- `src/agent_tools/web_tools_prewave3.py:2679`
- `src/agent_tools/web_tools_prewave3.py:3859`
- `src/process_reaper.py:71`
- `src/process_reaper.py:97`
- `src/process_reaper.py:106`
- `src/process_reaper.py:126`
- `tests/test_containment_contract.py:459`

## `registered` — function, line 440
- **called from:**
- `src/agent_tools/web_tools.py:2699`
- `src/agent_tools/web_tools_prewave3.py:3835`
- `src/browser_identity.py:484`
- `src/browser_identity.py:492`
- `src/browser_identity.py:498`
- `src/browser_identity.py:560`
- `src/browser_identity.py:584`
- `src/browser_identity.py:633`
- `src/browser_identity.py:644`
- `tests/test_browser_resource_identity.py:326`
- `static/js/modalManager.js:1238`

## `has_live_daemon` — function, line 444
- **called from:**
- `src/agent_tools/web_tools.py:2535`
- `src/agent_tools/web_tools_prewave3.py:2544`
- `src/agent_tools/web_tools_prewave3.py:3838`
