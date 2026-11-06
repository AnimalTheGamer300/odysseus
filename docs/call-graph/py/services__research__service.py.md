# `services/research/service.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ResearchSource` — class, line 16
- decorator: `dataclass`
- **called from:**
- `services/research/service.py:88`
- `services/research/service.py:144`

## `ResearchResult` — class, line 25
- decorator: `dataclass`
- **called from:**
- `services/research/service.py:97`
- `services/research/service.py:107`

## `ResearchService` — class, line 35
- **called from:**
- `tests/test_background_tool_jobs.py:61`
- `tests/test_background_tool_jobs.py:135`
- `tests/test_research_service.py:64`
- `tests/test_research_service.py:133`

## `ResearchService.__init__` — method, line 45
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

## `ResearchService.research` — method (async), line 49
- **called from:**
- `services/research/research_handler.py:278`
- `src/research_handler.py:1066`
- `src/task_scheduler.py:2272`
- `tests/test_deep_research_full_loop_navigation.py:115`
- `tests/test_research_service.py:70`
- `tests/test_research_service.py:75`
- `tests/test_research_service.py:81`
- `tests/test_research_service.py:91`
- `tests/test_research_service.py:97`
- `tests/test_research_service.py:102`
- `tests/test_research_service.py:149`
- `static/js/research/panel.js:1767`

## `ResearchService._parse_sources` — method, line 115
- decorator: `staticmethod`
- **called from:**
- `services/research/service.py:110`
- `tests/test_research_service.py:109`
- `tests/test_research_service.py:113`
- `tests/test_research_service.py:125`

## `ResearchService.start_background` — method, line 148
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResearchService.get_status` — method, line 161
- **called from:**
- `routes/chat_routes.py:4233`
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

## `ResearchService.cancel` — method, line 165
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
- `src/agent_loop.py:34341`
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
