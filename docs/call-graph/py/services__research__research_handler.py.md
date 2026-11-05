# `services/research/research_handler.py` — definitions & call sites

19 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ResearchHandler` — class, line 25
- **called from:**
- `services/research/service.py:46`
- `src/app_initializer.py:130`
- `tests/test_research_query_fallback.py:23`
- `tests/test_research_source_metadata.py:53`
- `tests/test_research_source_metadata.py:67`
- `tests/test_research_source_metadata.py:86`

## `ResearchHandler.__init__` — method, line 28
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

## `ResearchHandler._initialize_legacy_engine` — method, line 34
- **called from:**
- `services/research/research_handler.py:31`
- `src/research_handler.py:83`

## `ResearchHandler.start_research` — method, line 52
- **called from:**
- `routes/chat_routes.py:4200`
- `routes/research/research_routes.py:629`
- `services/research/service.py:157`
- `tests/test_research_handler_path_confinement.py:83`

## `ResearchHandler.on_progress` — method, line 79
- **called from:**
- `src/research_handler.py:394`
- `src/research_handler.py:416`

## `ResearchHandler._run` — method (async), line 82
- **called from:**
- `services/hwfit/hardware.py:87`
- `services/hwfit/hardware.py:94`
- `services/hwfit/hardware.py:108`
- `services/hwfit/hardware.py:110`
- `services/hwfit/hardware.py:211`
- `services/hwfit/hardware.py:221`
- `services/hwfit/hardware.py:237`
- `services/hwfit/hardware.py:237`
- `services/hwfit/hardware.py:293`
- `services/hwfit/hardware.py:293`
- `services/hwfit/hardware.py:294`
- `services/hwfit/hardware.py:323`
- `services/hwfit/hardware.py:325`
- `services/hwfit/hardware.py:338`
- `services/hwfit/hardware.py:341`
- `services/hwfit/hardware.py:376`
- `services/hwfit/hardware.py:378`
- `services/hwfit/hardware.py:393`
- `services/hwfit/hardware.py:422`
- `services/hwfit/hardware.py:466`
- `services/hwfit/hardware.py:491`
- `services/hwfit/hardware.py:503`
- `services/hwfit/hardware.py:503`
- `services/hwfit/hardware.py:531`
- `services/hwfit/hardware.py:549`
- `services/hwfit/hardware.py:554`
- `services/hwfit/hardware.py:557`
- `services/hwfit/hardware.py:562`
- `services/hwfit/hardware.py:635`
- `services/research/research_handler.py:102`
- `services/search/providers.py:268`
- `services/search/providers.py:281`
- `services/search/providers.py:290`
- `services/search/providers.py:298`
- `src/research_handler.py:421`
- `tests/test_agent_evidence_loop.py:128`
- `tests/test_agent_evidence_loop.py:140`
- `tests/test_agent_evidence_loop.py:152`
- `tests/test_agent_evidence_loop.py:163`
- `tests/test_agent_evidence_loop.py:189`
- `tests/test_agent_evidence_loop.py:222`
- `tests/test_agent_evidence_loop.py:262`
- `tests/test_agent_evidence_loop.py:304`
- `tests/test_agent_evidence_loop.py:356`
- `tests/test_agent_evidence_loop.py:399`
- `tests/test_agent_evidence_loop.py:439`
- `tests/test_agent_evidence_loop.py:461`
- `tests/test_agent_evidence_loop.py:627`
- `tests/test_agent_evidence_loop.py:649`
- `tests/test_agent_evidence_loop.py:677`
- `tests/test_agent_evidence_loop.py:715`
- `tests/test_agent_rounds_exhausted.py:24`
- `tests/test_agent_runtime_context.py:28`
- `tests/test_app_config_shared_fetch_js.py:89`
- `tests/test_app_config_shared_fetch_js.py:107`
- `tests/test_app_config_shared_fetch_js.py:125`
- `tests/test_app_config_shared_fetch_js.py:144`
- `tests/test_app_config_shared_fetch_js.py:163`
- `tests/test_app_config_shared_fetch_js.py:188`
- `tests/test_app_config_shared_fetch_js.py:277`
- … +208 more (grep the name in repo)

## `ResearchHandler.get_status` — method, line 106
- **called from:**
- `routes/chat_routes.py:4214`
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

## `ResearchHandler.cancel_research` — method, line 131
- **called from:**
- `routes/research/research_routes.py:327`
- `services/research/research_handler.py:66`
- `services/research/service.py:167`
- `src/research_handler.py:310`

## `ResearchHandler.get_result` — method, line 147
- **called from:**
- `routes/research/research_routes.py:336`
- `routes/research/research_routes.py:720`
- `routes/research/research_routes.py:778`
- `src/background_tool_jobs.py:136`
- `tests/test_research_handler_path_confinement.py:55`

## `ResearchHandler.get_sources` — method, line 163
- **called from:**
- `routes/chat_routes.py:4234`
- `routes/research/research_routes.py:339`
- `routes/research/research_routes.py:737`
- `routes/research/research_routes.py:779`
- `src/background_tool_jobs.py:137`
- `tests/test_research_handler_path_confinement.py:56`

## `ResearchHandler._extract_sources` — method, line 184
- decorator: `staticmethod`
- **called from:**
- `services/research/research_handler.py:172`
- `services/research/research_handler.py:216`
- `src/research_handler.py:387`
- `src/research_handler.py:411`
- `src/research_handler.py:538`
- `src/research_handler.py:743`
- `src/task_scheduler.py:2313`
- `tests/test_research_handler_sources_nondict.py:14`
- `tests/test_research_source_metadata.py:8`
- `tests/test_services_research_low_quality_sources.py:44`
- `tests/test_services_research_low_quality_sources.py:49`
- `tests/test_services_research_low_quality_sources.py:56`
- `tests/test_services_research_low_quality_sources.py:66`
- `tests/test_svc_research_sources_nondict.py:14`

## `ResearchHandler.clear_result` — method, line 199
- **called from:**
- `routes/chat_routes.py:4245`
- `routes/research/research_routes.py:348`
- `tests/test_research_handler_path_confinement.py:70`

## `ResearchHandler._save_result` — method, line 209
- **called from:**
- `services/research/research_handler.py:93`
- `src/research_handler.py:365`
- `src/research_handler.py:385`
- `src/research_handler.py:409`
- `tests/test_research_handler_path_confinement.py:71`
- `tests/test_research_source_metadata.py:130`

## `ResearchHandler.call_research_service` — method (async), line 233
- **called from:**
- `routes/chat_routes.py:2519`
- `routes/diagnostics_routes.py:100`
- `services/research/research_handler.py:84`
- `services/research/service.py:73`
- `src/research_handler.py:345`

## `ResearchHandler._fallback_research` — method (async), line 297
- **called from:**
- `services/research/research_handler.py:295`
- `src/research_handler.py:1091`

## `ResearchHandler._get_legacy_stats` — method, line 320
- **called from:**
- `services/research/research_handler.py:311`
- `src/research_handler.py:1107`

## `ResearchHandler._format_research_report` — method, line 335
- **called from:**
- `services/research/research_handler.py:286`
- `services/research/research_handler.py:313`
- `src/research_handler.py:380`
- `src/research_handler.py:404`
- `src/research_handler.py:1087`
- `src/research_handler.py:1109`
- `tests/test_research_handler_analyzed_urls.py:6`
- `tests/test_research_handler_analyzed_urls.py:17`
- `tests/test_services_research_low_quality_sources.py:74`

## `ResearchHandler._format_error_response` — method, line 420
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResearchHandler._handle_research_failure` — method, line 439
- **called from:**
- `services/research/research_handler.py:318`
- `src/research_handler.py:1114`
