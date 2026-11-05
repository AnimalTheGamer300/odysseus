# `src/task_scheduler.py` — definitions & call sites

58 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `TaskEndpointAuthorityError` — class, line 24
- **called from:**
- `src/task_scheduler.py:30`
- `src/task_scheduler.py:2049`
- `src/task_scheduler.py:2252`

## `_require_task_owner` — function, line 28
- **called from:**
- `src/task_scheduler.py:1377`
- `src/task_scheduler.py:1667`
- `src/task_scheduler.py:2018`
- `src/task_scheduler.py:2205`
- `src/task_scheduler.py:2386`

## `_is_sft_fixture_owner` — function, line 33
- **called from:**
- `src/task_scheduler.py:799`
- `src/task_scheduler.py:807`
- `tests/test_task_scheduler_fixture_isolation.py:5`
- `tests/test_task_scheduler_fixture_isolation.py:6`
- `tests/test_task_scheduler_fixture_isolation.py:10`
- `tests/test_task_scheduler_fixture_isolation.py:11`

## `_background_owner_filter` — function, line 38
- **called from:**
- `src/task_scheduler.py:636`
- `src/task_scheduler.py:713`
- `src/task_scheduler.py:833`
- `src/task_scheduler.py:862`

## `_utcnow` — function, line 44
- **called from:**
- `src/cleanup_service.py:86`
- `src/cleanup_service.py:101`
- `src/cleanup_service.py:127`
- `src/cleanup_service.py:235`
- `src/cleanup_service.py:236`
- `src/task_scheduler.py:181`
- `src/task_scheduler.py:186`
- `src/task_scheduler.py:493`
- `src/task_scheduler.py:511`
- `src/task_scheduler.py:514`
- `src/task_scheduler.py:516`
- `src/task_scheduler.py:520`
- `src/task_scheduler.py:534`
- `src/task_scheduler.py:610`
- `src/task_scheduler.py:631`
- `src/task_scheduler.py:836`
- `src/task_scheduler.py:848`
- `src/task_scheduler.py:896`
- `src/task_scheduler.py:953`
- `src/task_scheduler.py:955`
- `src/task_scheduler.py:981`
- `src/task_scheduler.py:996`
- `src/task_scheduler.py:999`
- `src/task_scheduler.py:1022`
- `src/task_scheduler.py:1031`
- `src/task_scheduler.py:1094`
- `src/task_scheduler.py:1129`
- `src/task_scheduler.py:1130`
- `src/task_scheduler.py:1135`
- `src/task_scheduler.py:1151`
- `src/task_scheduler.py:1154`
- `src/task_scheduler.py:1163`
- `src/task_scheduler.py:1251`
- `src/task_scheduler.py:1256`
- `src/task_scheduler.py:1261`
- `src/task_scheduler.py:1286`
- `src/task_scheduler.py:1291`
- `src/task_scheduler.py:1292`
- `src/task_scheduler.py:1496`
- `src/task_scheduler.py:1499`
- `src/task_scheduler.py:1503`
- `src/task_scheduler.py:1710`
- `src/task_scheduler.py:1711`
- `src/task_scheduler.py:1890`
- `src/task_scheduler.py:1891`
- `src/task_scheduler.py:1940`
- `src/task_scheduler.py:1948`
- `src/task_scheduler.py:2290`
- `src/task_scheduler.py:2291`
- `src/task_scheduler.py:2624`
- `src/task_scheduler.py:2652`
- `src/task_scheduler.py:2687`
- `src/task_scheduler.py:2705`
- `src/task_scheduler.py:2845`
- `src/task_scheduler.py:2846`
- `src/webhook_manager.py:418`
- `src/webhook_manager.py:432`
- `src/webhook_manager.py:441`
- `tests/test_cleanup_service_utcnow.py:13`
- `tests/test_cleanup_service_utcnow.py:23`
- … +2 more (grep the name in repo)

## `compose_task_relevant_tools` — function, line 63
- **called from:**
- `tests/test_task_shell_tools.py:30`
- `tests/test_task_shell_tools.py:37`
- `tests/test_task_shell_tools.py:50`
- `tests/test_task_shell_tools.py:65`
- `tests/test_task_shell_tools.py:80`

## `_cached` — function (async), line 87
- **called from:**
- `src/builtin_actions.py:1390`
- `src/task_scheduler.py:1593`
- `src/task_scheduler.py:1630`
- `tests/test_task_scheduler_cache.py:25`
- `tests/test_task_scheduler_cache.py:31`
- `tests/test_task_scheduler_cache.py:46`
- `tests/test_task_scheduler_cache.py:62`
- `tests/test_task_scheduler_cache.py:68`
- `tests/test_task_scheduler_cache.py:86`

## `is_valid_cron` — function, line 135
- **called from:**
- `routes/task/task_routes.py:478`
- `routes/task/task_routes.py:788`
- `src/task_scheduler.py:195`
- `tests/test_manage_tasks_cron.py:179`
- `tests/test_manage_tasks_cron.py:185`

## `compute_next_run` — function, line 152
- **called from:**
- `routes/assistant_routes.py:233`
- `routes/assistant_routes.py:255`
- `routes/task/task_routes.py:420`
- `routes/task/task_routes.py:505`
- `routes/task/task_routes.py:816`
- `routes/task/task_routes.py:879`
- `routes/task/task_routes.py:919`
- `src/task_scheduler.py:518`
- `src/task_scheduler.py:1132`
- `src/task_scheduler.py:1160`
- `src/task_scheduler.py:1258`
- `src/task_scheduler.py:2622`
- `src/task_scheduler.py:2649`
- `src/task_scheduler.py:2684`
- `src/task_scheduler.py:2703`
- `src/tools/system.py:498`
- `src/tools/system.py:624`
- `src/tools/system.py:663`
- `tests/test_compute_next_run_monthly_clamp.py:27`
- `tests/test_compute_next_run_monthly_clamp.py:32`
- `tests/test_compute_next_run_monthly_clamp.py:39`
- `tests/test_compute_next_run_monthly_clamp.py:46`
- `tests/test_compute_next_run_monthly_clamp.py:53`
- `tests/test_manage_tasks_cron.py:191`
- `tests/test_scheduler_scheduled_time_validation.py:21`
- `tests/test_scheduler_scheduled_time_validation.py:26`
- `tests/tools/organizer_smoke.py:344`

## `_to_utc_naive` — function, line 188
- **called from:**
- `src/caldav_sync.py:386`
- `src/caldav_sync.py:390`
- `src/task_scheduler.py:204`
- `src/task_scheduler.py:210`
- `src/task_scheduler.py:234`
- `src/task_scheduler.py:243`
- `src/task_scheduler.py:270`

## `_resolve_task_timezone` — function, line 275
- **called from:**
- `src/task_scheduler.py:522`
- `src/task_scheduler.py:1137`
- `src/task_scheduler.py:1165`
- `src/task_scheduler.py:1263`
- `src/task_scheduler.py:1491`
- `src/task_scheduler.py:1756`
- `src/task_scheduler.py:2625`
- `src/task_scheduler.py:2653`
- `src/task_scheduler.py:2688`

## `_digest_windows` — function, line 314
- **called from:**
- `src/task_scheduler.py:1514`
- `tests/test_checkin_digest_owner_scope.py:86`
- `tests/test_digest_windows.py:9`
- `tests/test_digest_windows.py:21`

## `_checkin_calendar_events` — function, line 328
- **called from:**
- `src/task_scheduler.py:1518`
- `tests/test_checkin_digest_owner_scope.py:49`
- `tests/test_checkin_digest_owner_scope.py:51`
- `tests/test_checkin_digest_owner_scope.py:67`
- `tests/test_checkin_digest_owner_scope.py:87`
- `tests/test_checkin_digest_owner_scope.py:109`

## `_normalize_chat_endpoint` — function, line 351
- **called from:**
- `src/task_scheduler.py:1693`
- `src/task_scheduler.py:1878`
- `src/task_scheduler.py:2253`
- `tests/test_task_endpoint_normalization.py:16`
- `tests/test_task_endpoint_normalization.py:23`
- `tests/test_task_endpoint_normalization.py:25`
- `tests/test_task_endpoint_normalization.py:25`
- `tests/test_task_endpoint_normalization.py:30`
- `tests/test_task_endpoint_normalization.py:31`
- `tests/test_task_endpoint_normalization.py:35`
- `tests/test_task_endpoint_normalization.py:36`
- `tests/test_task_endpoint_normalization.py:41`

## `_resolve_research_settings` — function, line 387
- **called from:**
- `src/task_scheduler.py:2256`
- `tests/test_scheduler_research_settings_guard.py:41`
- `tests/test_scheduler_research_settings_guard.py:53`
- `tests/test_scheduler_research_settings_guard.py:65`
- `tests/test_scheduler_research_settings_guard.py:69`
- `tests/test_scheduler_research_settings_guard.py:81`
- `tests/test_scheduler_research_settings_guard.py:100`

## `TaskScheduler` — class, line 417
- **called from:**
- `app.py:868`
- `tests/test_email_urgency_checkpoint.py:526`
- `tests/test_headless_completion_consumers.py:75`
- `tests/test_headless_completion_consumers.py:115`
- `tests/test_headless_completion_consumers.py:160`
- `tests/test_request_authority.py:365`
- `tests/test_request_authority.py:399`
- `tests/test_request_authority.py:553`
- `tests/test_scheduler_prompt_cache_time.py:64`
- `tests/test_scheduler_prompt_cache_time.py:110`
- `tests/test_scheduler_prompt_cache_time.py:144`
- `tests/test_task_mcp_delivery.py:18`
- `tests/test_task_mcp_delivery.py:39`
- `tests/test_task_mcp_delivery.py:49`
- `tests/test_task_mcp_delivery.py:61`
- `tests/test_task_mcp_delivery.py:72`
- `tests/test_task_scheduler_cancel.py:146`
- `tests/test_task_scheduler_cancel.py:211`
- `tests/test_task_shell_tools.py:121`

## `TaskScheduler.__init__` — method, line 418
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

## `TaskScheduler._executing_guard` — method (async), line 439
- decorator: `contextlib.asynccontextmanager`
- **called from:**
- `src/task_scheduler.py:855`
- `src/task_scheduler.py:937`
- `src/task_scheduler.py:1306`
- `src/task_scheduler.py:2338`
- `src/task_scheduler.py:2455`
- `src/task_scheduler.py:2472`
- `src/task_scheduler.py:2488`

## `TaskScheduler._set_run_progress` — method, line 456
- **called from:**
- `src/task_scheduler.py:1399`

## `TaskScheduler._mark_run_aborted` — method, line 473
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TaskScheduler._finish_cancelled_run` — method, line 502
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TaskScheduler.add_notification` — method, line 528
- **called from:**
- `routes/note/note_routes.py:523`
- `src/task_scheduler.py:1184`
- `src/task_scheduler.py:1192`
- `src/task_scheduler.py:1243`
- `tests/test_auth_regressions.py:320`
- `tests/test_auth_regressions.py:321`
- `tests/test_auth_regressions.py:322`
- `tests/test_auth_regressions.py:323`

## `TaskScheduler.pop_notifications` — method, line 570
- **called from:**
- `routes/task/task_routes.py:583`
- `tests/test_auth_regressions.py:324`
- `tests/test_auth_regressions.py:332`
- `tests/test_email_urgency_checkpoint.py:543`

## `TaskScheduler.start` — method (async), line 595
- **called from:**
- `app.py:1410`
- `launcher.py:73`
- `launcher.py:145`
- `launcher.py:147`
- `mcp_servers/email_server.py:2023`
- `routes/auth_routes.py:895`
- `routes/chat_helpers.py:94`
- `routes/chat_helpers.py:94`
- `routes/chat_helpers.py:1714`
- `routes/chat_helpers.py:1777`
- `routes/chat_helpers.py:1778`
- `routes/chat_helpers.py:1779`
- `routes/chat_routes.py:5522`
- `routes/cookbook_routes.py:3584`
- `routes/email/email_helpers.py:399`
- `routes/email/email_routes.py:1130`
- `routes/email/email_routes.py:1596`
- `routes/email/email_routes.py:1898`
- `routes/model_routes.py:1666`
- `scripts/add_hwfit_models.py:117`
- `scripts/css_snapshot.py:211`
- `services/hwfit/hf_discovery.py:115`
- `services/search/core.py:411`
- `services/search/core.py:800`
- `services/skills/evaluation.py:463`
- `src/agent_evidence.py:225`
- `src/agent_evidence.py:225`
- `src/agent_evidence.py:245`
- `src/agent_evidence.py:308`
- `src/agent_loop.py:1143`
- `src/agent_loop.py:2639`
- `src/agent_loop.py:2644`
- `src/agent_loop.py:2652`
- `src/agent_loop.py:2653`
- `src/agent_loop.py:3180`
- `src/agent_loop.py:9123`
- `src/agent_loop.py:9123`
- `src/agent_loop.py:9169`
- `src/agent_loop.py:12041`
- `src/agent_loop.py:12044`
- `src/agent_loop.py:14160`
- `src/agent_loop.py:14164`
- `src/agent_runtime/completion.py:90`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:94`
- `src/agent_tools/document_tools.py:240`
- `src/agent_tools/document_tools.py:384`
- `src/agent_tools/document_tools.py:431`
- `src/agent_tools/document_tools.py:729`
- `src/agent_tools/document_tools.py:734`
- `src/agent_tools/document_tools.py:898`
- `src/agent_tools/filesystem_tools.py:1153`
- `src/agent_tools/filesystem_tools.py:1154`
- `src/agent_tools/filesystem_tools.py:1266`
- `src/agent_tools/web_tools.py:954`
- `src/agent_tools/web_tools.py:975`
- `src/agent_tools/web_tools.py:978`
- `src/agent_tools/web_tools_prewave3.py:958`
- … +213 more (grep the name in repo)

## `TaskScheduler.stop` — method (async), line 730
- **called from:**
- `app.py:1477`
- `launcher.py:96`
- `routes/chat_routes.py:5561`
- `tests/smoke/stub_provider.py:172`
- `tests/test_client_tool_routing.py:88`
- `tests/test_compare_stop_disconnect_poll.py:147`
- `tests/test_compare_stop_disconnect_poll.py:233`
- `tests/test_compare_stop_disconnect_poll.py:234`
- `tests/test_compare_stop_disconnect_poll.py:236`
- `tests/test_nested_invocation_ownership.py:77`
- `tests/test_notes_native_cleanup.py:30`
- `static/js/admin.js:1379`
- `static/js/chat.js:6534`
- `static/js/chat.js:6625`
- `static/js/chatRenderer.js:543`
- `static/js/compare/stream.js:306`
- `static/js/compare/stream.js:343`
- `static/js/cookbookRunning.js:2951`
- `static/js/documentLibrary.js:3346`
- `static/js/documentLibrary.js:3499`
- `static/js/editor/editor-bridge.js:96`
- `static/js/emailLibrary/aiReply.js:56`
- `static/js/fileHandler.js:389`
- `static/js/galleryEditor.js:12858`
- `static/js/galleryEditor.js:13203`
- `static/js/galleryEditor.js:14092`
- `static/js/keyboard-shortcuts.js:172`
- `static/js/models.js:222`
- `static/js/settings.js:2365`
- `static/js/spinner.js:260`
- `static/js/spinner.js:268`
- `static/js/spinner.js:274`
- `static/js/spinner.js:288`
- `static/js/spinner.js:367`
- `static/js/spinner.js:408`
- `static/js/spinner.js:425`
- `static/js/spinner.js:437`
- `static/js/tasks.js:3011`
- `static/js/tts-ai.js:179`
- `static/js/tts-ai.js:224`
- `static/js/tts-ai.js:503`
- `static/js/tts-ai.js:517`
- `static/js/voiceRecorder.js:102`
- `static/js/voiceRecorder.js:178`
- `static/js/voiceRecorder.js:251`

## `TaskScheduler._note_pings_loop` — method (async), line 746
- **called from:**
- `src/task_scheduler.py:700`

## `TaskScheduler._event_pings_loop` — method (async), line 766
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TaskScheduler._known_task_owners` — method, line 786
- **called from:**
- `src/task_scheduler.py:756`
- `src/task_scheduler.py:776`

## `TaskScheduler._loop` — method (async), line 815
- **called from:**
- `src/agent_jobs.py:363`
- `src/bg_monitor.py:245`
- `src/task_scheduler.py:691`

## `TaskScheduler._check_due_tasks` — method (async), line 844
- **called from:**
- `src/task_scheduler.py:819`
- `tests/test_scheduler_restart_doublefire.py:134`
- `tests/test_scheduler_restart_doublefire.py:135`

## `TaskScheduler._execute_task` — method (async), line 881
- **called from:**
- `src/task_scheduler.py:877`
- `src/task_scheduler.py:2342`
- `src/task_scheduler.py:2453`
- `src/task_scheduler.py:2459`
- `tests/test_task_scheduler_cancel.py:83`
- `tests/test_task_scheduler_cancel.py:151`

## `TaskScheduler._defer_immediately_due_task` — method, line 940
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TaskScheduler._execute_task_locked` — method (async), line 962
- **called from:**
- `src/task_scheduler.py:909`
- `src/task_scheduler.py:918`
- `tests/test_task_cookbook_admin_gate.py:277`

## `TaskScheduler._cancel_if_foreground_active` — method (async), line 1051
- **called from:**
- `src/task_scheduler.py:1066`

## `TaskScheduler._task_needs_model_slot` — method, line 1343
- **called from:**
- `src/task_scheduler.py:908`

## `TaskScheduler._log_to_assistant` — method, line 1360
- **called from:**
- `src/task_scheduler.py:1205`

## `TaskScheduler._execute_action` — method (async), line 1375
- **called from:**
- `src/task_scheduler.py:1069`
- `tests/test_request_authority.py:365`
- `tests/test_task_mcp_delivery.py:61`

## `TaskScheduler._progress` — method, line 1398
- **called from:**
- `src/containment.py:1164`
- `src/deep_research.py:1829`
- `src/research_navigator.py:211`

## `TaskScheduler._format_email_output` — method, line 1453
- decorator: `staticmethod`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TaskScheduler._execute_checkin` — method (async), line 1485
- **called from:**
- `src/task_scheduler.py:1729`

## `TaskScheduler._fetch_miniflux` — method (async), line 1573
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TaskScheduler._call_mcp` — method (async), line 1627
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TaskScheduler._execute_llm_task` — method (async), line 1664
- **called from:**
- `src/task_scheduler.py:1080`
- `tests/test_scheduler_prompt_cache_time.py:64`
- `tests/test_scheduler_prompt_cache_time.py:146`
- `tests/test_task_scheduler_endpoint_authority.py:70`
- `tests/test_task_shell_tools.py:138`

## `TaskScheduler._deliver_task_result` — method (async), line 1831
- **called from:**
- `src/task_scheduler.py:1087`
- `tests/test_task_scheduler_session_delivery.py:69`
- `tests/test_task_scheduler_session_delivery.py:101`

## `TaskScheduler._is_email_output_target` — method, line 1956
- decorator: `staticmethod`
- **called from:**
- `src/task_scheduler.py:1852`

## `TaskScheduler._deliver_via_email` — method (async), line 1964
- **called from:**
- `src/task_scheduler.py:1853`

## `TaskScheduler._run_agent_loop` — method (async), line 2011
- **called from:**
- `src/task_scheduler.py:1657`
- `src/task_scheduler.py:1796`
- `tests/test_headless_completion_consumers.py:75`
- `tests/test_headless_completion_consumers.py:115`
- `tests/test_headless_completion_consumers.py:160`
- `tests/test_request_authority.py:553`
- `tests/test_scheduler_prompt_cache_time.py:110`
- `tests/test_task_scheduler_endpoint_authority.py:72`

## `TaskScheduler._execute_research_task` — method (async), line 2188
- **called from:**
- `src/task_scheduler.py:1075`
- `tests/test_task_scheduler_endpoint_authority.py:75`

## `TaskScheduler._run_chained` — method (async), line 2334
- **called from:**
- `src/task_scheduler.py:1218`

## `TaskScheduler._has_chain_cycle` — method, line 2344
- **called from:**
- `src/task_scheduler.py:1216`
- `tests/test_task_chain_owner_scope.py:125`

## `TaskScheduler._resolve_defaults` — method, line 2361
- **called from:**
- `src/task_scheduler.py:1685`
- `src/task_scheduler.py:1872`
- `src/task_scheduler.py:2234`
- `src/task_scheduler.py:2776`

## `TaskScheduler._deliver_via_mcp` — method (async), line 2376
- **called from:**
- `src/task_scheduler.py:1849`
- `tests/test_task_mcp_delivery.py:18`
- `tests/test_task_mcp_delivery.py:39`
- `tests/test_task_mcp_delivery.py:49`
- `tests/test_task_mcp_delivery.py:72`

## `TaskScheduler.run_task_now` — method (async), line 2450
- **called from:**
- `routes/assistant_routes.py:296`
- `routes/task/task_routes.py:942`
- `routes/task/task_routes.py:1139`
- `src/event_bus.py:121`
- `src/tools/system.py:688`
- `tests/test_task_scheduler_cancel.py:212`

## `TaskScheduler.stop_task` — method (async), line 2462
- **called from:**
- `routes/task/task_routes.py:959`
- `tests/test_task_scheduler_cancel.py:98`
- `tests/test_task_scheduler_cancel.py:159`
- `tests/test_task_scheduler_cancel.py:164`
- `tests/test_task_scheduler_cancel.py:218`

## `TaskScheduler.stop_background_tasks_for_foreground` — method (async), line 2480
- **called from:**
- `app.py:229`
- `tests/test_task_scheduler_cancel.py:162`

## `TaskScheduler.ensure_defaults` — method (async), line 2507
- **called from:**
- `app.py:1365`
- `routes/task/task_routes.py:355`
- `routes/task/task_routes.py:369`
- `routes/task/task_routes.py:401`
- `tests/test_request_authority.py:405`

## `TaskScheduler._score` — method, line 2587
- **called from:**
- `src/agent_tools/web_tools.py:2242`
- `src/agent_tools/web_tools_prewave3.py:2246`

## `TaskScheduler.ensure_assistant_defaults` — method (async), line 2750
- **called from:**
- `routes/assistant_routes.py:113`
- `src/task_scheduler.py:2746`
