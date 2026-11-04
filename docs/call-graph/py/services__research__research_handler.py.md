# `services/research/research_handler.py` — definitions & call sites

19 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ResearchHandler` — class, line 25
- **called from:**
- `services/research/service.py:46`
- `src/app_initializer.py:130`
- `tests/test_research_query_fallback.py:23`

## `ResearchHandler.__init__` — method, line 28
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email_routes.py:1455`
- `src/builtin_actions.py:428`
- `src/outbound_fetch.py:220`
- `tests/test_agent_state_dir_confinement.py:648`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_extraction_controls.py:14`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_retired_settings_interfaces.py:30`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:148`

## `ResearchHandler._initialize_legacy_engine` — method, line 34
- **called from:**
- `services/research/research_handler.py:31`
- `src/research_handler.py:71`

## `ResearchHandler.start_research` — method, line 52
- **called from:**
- `routes/chat_routes.py:1929`
- `routes/research/research_routes.py:563`
- `services/research/service.py:157`
- `tests/test_research_handler_path_confinement.py:83`

## `ResearchHandler.on_progress` — method, line 79
- **called from:**
- `src/research_handler.py:376`
- `src/research_handler.py:398`

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
- `services/search/providers.py:198`
- `services/search/providers.py:217`
- `services/search/providers.py:226`
- `services/search/providers.py:234`
- `src/research_handler.py:403`
- `tests/test_agent_rounds_exhausted.py:18`
- `tests/test_app_config_shared_fetch_js.py:89`
- `tests/test_app_config_shared_fetch_js.py:107`
- `tests/test_app_config_shared_fetch_js.py:125`
- `tests/test_app_config_shared_fetch_js.py:144`
- `tests/test_app_config_shared_fetch_js.py:163`
- `tests/test_app_config_shared_fetch_js.py:188`
- `tests/test_app_config_shared_fetch_js.py:277`
- `tests/test_app_config_shared_fetch_js.py:322`
- `tests/test_ask_user_persistence.py:22`
- `tests/test_ask_user_tool.py:31`
- `tests/test_ask_user_tool.py:48`
- `tests/test_ask_user_tool.py:55`
- `tests/test_ask_user_tool.py:65`
- `tests/test_ask_user_tool.py:71`
- `tests/test_ask_user_tool.py:78`
- `tests/test_bg_job_tools.py:90`
- `tests/test_bg_job_tools.py:96`
- `tests/test_bg_job_tools.py:102`
- `tests/test_bg_job_tools.py:108`
- `tests/test_bg_job_tools.py:114`
- `tests/test_bg_job_tools.py:122`
- `tests/test_bg_job_tools.py:128`
- `tests/test_bg_job_tools.py:132`
- `tests/test_bg_job_tools.py:138`
- … +122 more (grep the name in repo)

## `ResearchHandler.get_status` — method, line 106
- **called from:**
- `routes/chat_routes.py:1943`
- `routes/research/research_routes.py:284`
- `routes/research/research_routes.py:589`
- `services/research/service.py:163`
- `tests/test_research_handler_path_confinement.py:54`
- `tests/test_research_status_avg_duration.py:22`
- `tests/test_research_status_avg_duration.py:34`
- `tests/test_research_status_avg_duration.py:35`
- `tests/test_research_status_avg_duration.py:36`

## `ResearchHandler.cancel_research` — method, line 131
- **called from:**
- `routes/research/research_routes.py:295`
- `services/research/research_handler.py:66`
- `services/research/service.py:167`
- `src/research_handler.py:294`

## `ResearchHandler.get_result` — method, line 147
- **called from:**
- `routes/research/research_routes.py:304`
- `routes/research/research_routes.py:619`
- `routes/research/research_routes.py:656`
- `tests/test_research_handler_path_confinement.py:55`

## `ResearchHandler.get_sources` — method, line 163
- **called from:**
- `routes/chat_routes.py:1963`
- `routes/research/research_routes.py:307`
- `routes/research/research_routes.py:631`
- `routes/research/research_routes.py:657`
- `tests/test_research_handler_path_confinement.py:56`

## `ResearchHandler._extract_sources` — method, line 184
- decorator: `staticmethod`
- **called from:**
- `services/research/research_handler.py:172`
- `services/research/research_handler.py:216`
- `src/research_handler.py:369`
- `src/research_handler.py:393`
- `src/research_handler.py:492`
- `src/research_handler.py:613`
- `src/task_scheduler.py:2119`
- `tests/test_research_handler_sources_nondict.py:14`
- `tests/test_services_research_low_quality_sources.py:44`
- `tests/test_services_research_low_quality_sources.py:49`
- `tests/test_services_research_low_quality_sources.py:56`
- `tests/test_services_research_low_quality_sources.py:66`
- `tests/test_svc_research_sources_nondict.py:14`

## `ResearchHandler.clear_result` — method, line 199
- **called from:**
- `routes/chat_routes.py:1974`
- `routes/research/research_routes.py:309`
- `tests/test_research_handler_path_confinement.py:70`

## `ResearchHandler._save_result` — method, line 209
- **called from:**
- `services/research/research_handler.py:93`
- `src/research_handler.py:347`
- `src/research_handler.py:367`
- `src/research_handler.py:391`
- `tests/test_research_handler_path_confinement.py:71`

## `ResearchHandler.call_research_service` — method (async), line 233
- **called from:**
- `routes/chat_routes.py:1009`
- `routes/diagnostics_routes.py:100`
- `services/research/research_handler.py:84`
- `services/research/service.py:73`
- `src/research_handler.py:328`

## `ResearchHandler._fallback_research` — method (async), line 297
- **called from:**
- `services/research/research_handler.py:295`
- `src/research_handler.py:859`

## `ResearchHandler._get_legacy_stats` — method, line 320
- **called from:**
- `services/research/research_handler.py:311`
- `src/research_handler.py:875`

## `ResearchHandler._format_research_report` — method, line 335
- **called from:**
- `services/research/research_handler.py:286`
- `services/research/research_handler.py:313`
- `src/research_handler.py:362`
- `src/research_handler.py:386`
- `src/research_handler.py:855`
- `src/research_handler.py:877`
- `tests/test_research_handler_analyzed_urls.py:6`
- `tests/test_research_handler_analyzed_urls.py:17`
- `tests/test_services_research_low_quality_sources.py:74`

## `ResearchHandler._format_error_response` — method, line 420
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResearchHandler._handle_research_failure` — method, line 439
- **called from:**
- `services/research/research_handler.py:318`
- `src/research_handler.py:882`
