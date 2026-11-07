# `src/agent_runs.py` — definitions & call sites

19 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_Run` — class, line 26
- **called from:**
- `src/agent_runs.py:211`

## `_Run.__init__` — method, line 29
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

## `_publish` — function, line 56
- **called from:**
- `src/agent_runs.py:151`
- `src/agent_runs.py:155`
- `src/agent_runs.py:177`
- `src/agent_runs.py:182`

## `_wake_run_subscribers` — function, line 67
- **called from:**
- `src/agent_runs.py:133`
- `src/agent_runs.py:206`

## `_schedule_evict` — function, line 76
- **called from:**
- `src/agent_runs.py:189`
- `src/agent_runs.py:284`

## `_evict` — function (async), line 88
- **called from:**
- `src/agent_runs.py:97`

## `is_active` — function, line 100
- **called from:**
- `app.py:1225`
- `routes/chat_routes.py:5607`
- `routes/session_routes.py:242`
- `src/agent_jobs.py:295`
- `src/bg_monitor.py:161`

## `get_status` — function, line 105
- **called from:**
- `routes/chat_routes.py:4236`
- `routes/research/research_routes.py:298`
- `routes/research/research_routes.py:669`
- `services/research/service.py:163`
- `src/background_tool_jobs.py:82`
- `src/background_tool_jobs.py:133`
- `tests/test_research_handler_path_confinement.py:54`
- `tests/test_research_status_avg_duration.py:22`
- `tests/test_research_status_avg_duration.py:34`
- `tests/test_research_status_avg_duration.py:35`
- `tests/test_research_status_avg_duration.py:36`

## `get_run_id` — function, line 110
- **called from:**
- `tests/test_compare_stop_disconnect_poll.py:183`
- `tests/test_compare_stop_disconnect_poll.py:185`
- `tests/test_compare_stop_disconnect_poll.py:189`
- `tests/test_compare_stop_disconnect_poll.py:212`
- `tests/test_nested_invocation_ownership.py:75`
- `tests/test_nested_invocation_ownership.py:87`

## `get_active_run` — function, line 116
- **called from:**
- `routes/chat_routes.py:5562`

## `_drain` — function (async), line 122
- **called from:**
- `src/agent_runs.py:213`
- `src/containment.py:1109`
- `src/containment.py:1140`
- `src/llm_core.py:380`
- `src/llm_core.py:383`
- `tests/test_kv_cache_invalidation_2927.py:407`
- `tests/test_kv_cache_invalidation_2927.py:408`
- `tests/test_kv_cache_invalidation_2927.py:409`
- `tests/test_kv_cache_invalidation_2927.py:438`
- `tests/test_kv_cache_invalidation_2927.py:459`
- `tests/test_model_routes.py:1169`
- `tests/test_model_routes.py:1206`

## `_wake_subscribers` — function, line 128
- **called from:**
- `src/agent_runs.py:168`
- `src/agent_runs.py:185`

## `start` — function, line 192
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
- `routes/chat_routes.py:5544`
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

## `subscribe` — function (async), line 217
- **called from:**
- `routes/chat_routes.py:5546`
- `routes/chat_routes.py:5566`
- `tests/test_agent_runs_terminal_order.py:19`
- `tests/test_agent_runs_terminal_order.py:49`
- `tests/test_compare_stop_disconnect_poll.py:88`
- `tests/test_compare_stop_disconnect_poll.py:110`
- `tests/test_compare_stop_disconnect_poll.py:140`
- `tests/test_compare_stop_disconnect_poll.py:205`
- `tests/test_compare_stop_disconnect_poll.py:316`
- `tests/test_compare_stop_disconnect_poll.py:329`
- `tests/test_nested_invocation_ownership.py:82`
- `tests/test_nested_invocation_ownership.py:83`
- `tests/test_pr6020_browser_review_regressions.py:266`
- `tests/test_stream_error_redaction.py:32`
- `static/js/editor/panel-visibility.js:166`
- `static/js/galleryEditor.js:10651`

## `stop` — function, line 287
- **called from:**
- `app.py:1477`
- `launcher.py:96`
- `routes/chat_routes.py:5583`
- `tests/smoke/stub_provider.py:172`
- `tests/test_client_tool_routing.py:88`
- `tests/test_compare_stop_disconnect_poll.py:147`
- `tests/test_compare_stop_disconnect_poll.py:233`
- `tests/test_compare_stop_disconnect_poll.py:234`
- `tests/test_compare_stop_disconnect_poll.py:236`
- `tests/test_nested_invocation_ownership.py:77`
- `tests/test_notes_native_cleanup.py:30`
- `static/js/admin.js:1379`
- `static/js/chat.js:6498`
- `static/js/chat.js:6589`
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

## `cancel` — function, line 303
- **called from:**
- `app.py:1459`
- `app.py:1470`
- `routes/editor_agent_routes.py:1414`
- `routes/email/email_routes.py:6869`
- `routes/history/history_routes.py:613`
- `routes/shell_routes.py:957`
- `routes/shell_routes.py:1342`
- `services/research/research_handler.py:140`
- `services/research/research_handler.py:143`
- `services/shell/service.py:163`
- `services/skills/job_coordinator.py:215`
- `src/agent_loop.py:26037`
- `src/agent_loop.py:34383`
- `src/agent_runs.py:86`
- `src/agent_runs.py:207`
- `src/agent_runs.py:210`
- `src/agent_runs.py:249`
- `src/agent_runs.py:298`
- `src/agent_runs.py:315`
- `src/ai_interaction.py:1822`
- `src/ai_interaction.py:2094`
- `src/clean_agent_preview.py:5609`
- `src/clean_agent_preview.py:5617`
- `src/containment.py:1172`
- `src/containment.py:1182`
- `src/llm_core.py:141`
- `src/mcp_manager.py:440`
- `src/mcp_oauth.py:63`
- `src/research_handler.py:502`
- `src/research_handler.py:505`
- `src/task_scheduler.py:122`
- `src/task_scheduler.py:733`
- `src/task_scheduler.py:741`
- `src/task_scheduler.py:1063`
- `src/task_scheduler.py:1145`
- `src/task_scheduler.py:2470`
- `src/task_scheduler.py:2495`
- `tests/test_agent_editor_routes.py:1008`
- `tests/test_agent_editor_routes.py:1962`
- `tests/test_agent_editor_routes.py:1971`
- `tests/test_browser_identity_transport.py:39`
- `tests/test_browser_identity_transport.py:75`
- `tests/test_builtin_mcp_bg_tasks.py:101`
- `tests/test_client_tool_routing.py:867`
- `tests/test_compare_stop_disconnect_poll.py:377`
- `tests/test_compare_stop_disconnect_poll.py:434`
- `tests/test_completion_boundary.py:319`
- `tests/test_completion_boundary.py:324`
- `tests/test_containment_enforcement.py:382`
- `tests/test_containment_enforcement.py:384`
- `tests/test_containment_enforcement.py:408`
- `tests/test_containment_enforcement.py:410`
- `tests/test_cookbook_cache_scan_isolation.py:102`
- `tests/test_email_summary_llm.py:192`
- `tests/test_email_urgency_checkpoint.py:457`
- `tests/test_email_urgency_checkpoint.py:592`
- `tests/test_host_shell_polling.py:198`
- `tests/test_nested_invocation_ownership.py:93`
- `tests/test_nested_invocation_ownership.py:96`
- `tests/test_nested_invocation_ownership.py:448`
- … +84 more (grep the name in repo)

## `request_finish` — function, line 320
- **called from:**
- `routes/chat_routes.py:5591`
- `tests/test_agent_runs_terminal_order.py:44`
- `tests/test_agent_runs_terminal_order.py:46`
- `tests/test_nested_invocation_ownership.py:78`
- `tests/test_nested_invocation_ownership.py:80`

## `should_finish` — function, line 332
- **called from:**
- `src/clean_agent_preview.py:6174`
- `src/clean_agent_preview.py:6697`
- `src/clean_agent_preview.py:6777`
- `tests/test_agent_runs_terminal_order.py:45`
- `tests/test_agent_runs_terminal_order.py:47`
- `tests/test_agent_runs_terminal_order.py:51`
- `tests/test_nested_invocation_ownership.py:79`

## `get_finish_event` — function, line 337
- **called from:**
- `src/clean_agent_preview.py:6693`
