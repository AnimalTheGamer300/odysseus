# `src/research_handler.py` — definitions & call sites

36 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_bounded_int` — function, line 27
- **called from:**
- `src/research_handler.py:283`
- `src/research_handler.py:792`
- `src/research_handler.py:798`
- `src/research_handler.py:804`
- `src/research_handler.py:810`

## `_format_probe_failure` — function, line 35
- **called from:**
- `src/research_handler.py:738`
- `tests/test_research_probe_errors.py:19`
- `tests/test_research_probe_errors.py:30`
- `tests/test_research_probe_errors.py:36`

## `_research_json_path` — function, line 53
- **called from:**
- `src/research_handler.py:265`
- `src/research_handler.py:429`
- `src/research_handler.py:470`
- `src/research_handler.py:494`
- `src/research_handler.py:513`
- `src/research_handler.py:590`
- `src/research_handler.py:604`
- `src/research_handler.py:643`
- `src/research_handler.py:655`
- `src/research_handler.py:684`
- `src/research_handler.py:704`
- `tests/test_research_handler_path_confinement.py:19`
- `tests/test_research_handler_path_confinement.py:28`
- `tests/test_research_handler_path_confinement.py:45`

## `ResearchHandler` — class, line 65
- **called from:**
- `services/research/service.py:46`
- `src/app_initializer.py:130`
- `tests/test_research_query_fallback.py:23`

## `ResearchHandler.__init__` — method, line 68
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

## `ResearchHandler._initialize_legacy_engine` — method, line 74
- **called from:**
- `services/research/research_handler.py:31`
- `src/research_handler.py:71`

## `ResearchHandler.synthesize_query` — method (async), line 92
- **called from:**
- `routes/chat_routes.py:1924`
- `tests/test_research_query_fallback.py:38`
- `tests/test_research_query_fallback.py:49`
- `tests/test_research_query_fallback.py:61`
- `tests/test_research_query_fallback.py:73`
- `tests/test_research_query_fallback.py:81`
- `tests/test_research_query_fallback.py:98`

## `ResearchHandler._normalize` — method, line 122
- **called from:**
- `src/research_handler.py:126`
- `src/research_handler.py:132`

## `ResearchHandler._fallback` — method, line 125
- **called from:**
- `src/research_handler.py:137`
- `src/research_handler.py:171`
- `static/js/emailInbox.js:818`
- `static/js/emailInbox.js:819`
- `static/js/emailInbox.js:820`
- `static/js/emailInbox.js:821`
- `static/js/emailInbox.js:822`
- `static/js/emailInbox.js:823`
- `static/js/emailInbox.js:824`

## `ResearchHandler.generate_plan` — method (async), line 173
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResearchHandler.rename_owner` — method, line 224
- **called from:**
- `routes/auth_routes.py:483`
- `routes/auth_routes.py:529`
- `routes/personal_routes.py:115`
- `tests/test_rag_vector_rename_owner.py:66`
- `tests/test_rename_user_owner_sync.py:323`
- `tests/test_rename_user_owner_sync.py:337`
- `tests/test_upload_handler_rename_owner.py:58`
- `tests/test_upload_handler_rename_owner.py:91`

## `ResearchHandler.start_research` — method, line 240
- **called from:**
- `routes/chat_routes.py:1929`
- `routes/research/research_routes.py:563`
- `services/research/service.py:157`
- `tests/test_research_handler_path_confinement.py:83`

## `ResearchHandler.on_progress` — method, line 310
- **called from:**
- `src/research_handler.py:376`
- `src/research_handler.py:398`

## `ResearchHandler._guarded_complete` — method, line 315
- **called from:**
- `src/research_handler.py:353`
- `src/research_handler.py:371`
- `src/research_handler.py:395`

## `ResearchHandler._run` — method (async), line 323
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

## `ResearchHandler.get_status` — method, line 407
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

## `ResearchHandler.cancel_research` — method, line 447
- **called from:**
- `routes/research/research_routes.py:295`
- `services/research/research_handler.py:66`
- `services/research/service.py:167`
- `src/research_handler.py:294`

## `ResearchHandler.get_result` — method, line 463
- **called from:**
- `routes/research/research_routes.py:304`
- `routes/research/research_routes.py:619`
- `routes/research/research_routes.py:656`
- `tests/test_research_handler_path_confinement.py:55`

## `ResearchHandler.get_sources` — method, line 483
- **called from:**
- `routes/chat_routes.py:1963`
- `routes/research/research_routes.py:307`
- `routes/research/research_routes.py:631`
- `routes/research/research_routes.py:657`
- `tests/test_research_handler_path_confinement.py:56`

## `ResearchHandler.get_raw_findings` — method, line 505
- **called from:**
- `routes/chat_routes.py:1967`
- `routes/research/research_routes.py:308`
- `routes/research/research_routes.py:632`
- `tests/test_research_handler_path_confinement.py:57`

## `ResearchHandler._extract_sources` — method, line 525
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

## `ResearchHandler._extract_raw_findings` — method, line 545
- decorator: `staticmethod`
- **called from:**
- `src/research_handler.py:352`
- `src/research_handler.py:370`
- `src/research_handler.py:394`
- `src/research_handler.py:511`
- `src/research_handler.py:614`
- `src/task_scheduler.py:2120`
- `tests/test_research_handler_raw_nondict.py:13`

## `ResearchHandler.get_avg_duration` — method, line 564
- **called from:**
- `src/research_handler.py:423`

## `ResearchHandler.clear_result` — method, line 584
- **called from:**
- `routes/chat_routes.py:1974`
- `routes/research/research_routes.py:309`
- `tests/test_research_handler_path_confinement.py:70`

## `ResearchHandler._save_result` — method, line 601
- **called from:**
- `services/research/research_handler.py:93`
- `src/research_handler.py:347`
- `src/research_handler.py:367`
- `src/research_handler.py:391`
- `tests/test_research_handler_path_confinement.py:71`

## `ResearchHandler._get_session_json` — method, line 641
- **called from:**
- `routes/chat_routes.py:1866`
- `routes/chat_routes.py:1914`
- `tests/test_research_handler_path_confinement.py:58`

## `ResearchHandler.get_report_html` — method, line 653
- **called from:**
- `routes/research/research_routes.py:331`
- `tests/test_research_handler_path_confinement.py:59`

## `ResearchHandler.hide_image` — method, line 682
- **called from:**
- `routes/research/research_routes.py:350`
- `tests/test_research_handler_path_confinement.py:68`

## `ResearchHandler.unhide_all_images` — method, line 702
- **called from:**
- `routes/research/research_routes.py:361`
- `tests/test_research_handler_path_confinement.py:69`

## `ResearchHandler._probe_endpoint` — method (async), line 720
- decorator: `staticmethod`
- **called from:**
- `routes/cookbook_routes.py:1878`
- `routes/cookbook_routes.py:1946`
- `routes/model_routes.py:1502`
- `routes/model_routes.py:1873`
- `routes/model_routes.py:2103`
- `routes/model_routes.py:2139`
- `routes/model_routes.py:2244`
- `routes/model_routes.py:2271`
- `routes/model_routes.py:2331`
- `src/research_handler.py:785`
- `tests/test_endpoint_probing.py:116`
- `tests/test_endpoint_probing.py:127`
- `tests/test_endpoint_probing.py:141`
- `tests/test_endpoint_probing.py:151`
- `tests/test_endpoint_probing.py:165`
- `tests/test_endpoint_probing.py:178`
- `tests/test_endpoint_probing.py:188`
- `tests/test_endpoint_probing.py:200`
- `tests/test_endpoint_probing.py:207`
- `tests/test_endpoint_probing.py:208`
- `tests/test_model_routes.py:289`
- `tests/test_model_routes.py:304`
- `tests/test_model_routes.py:320`
- `tests/test_model_routes.py:607`
- `tests/test_model_routes.py:618`
- `tests/test_model_routes.py:670`
- `tests/test_model_routes.py:695`
- `tests/test_model_routes.py:706`
- `tests/test_model_routes.py:725`
- `tests/test_model_routes.py:745`
- `tests/test_model_routes.py:757`
- `tests/test_research_probe_errors.py:52`

## `ResearchHandler.call_research_service` — method (async), line 740
- **called from:**
- `routes/chat_routes.py:1009`
- `routes/diagnostics_routes.py:100`
- `services/research/research_handler.py:84`
- `services/research/service.py:73`
- `src/research_handler.py:328`

## `ResearchHandler._fallback_research` — method (async), line 861
- **called from:**
- `services/research/research_handler.py:295`
- `src/research_handler.py:859`

## `ResearchHandler._get_legacy_stats` — method, line 884
- **called from:**
- `services/research/research_handler.py:311`
- `src/research_handler.py:875`

## `ResearchHandler._format_research_report` — method, line 899
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

## `ResearchHandler._format_error_response` — method, line 924
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResearchHandler._handle_research_failure` — method, line 943
- **called from:**
- `services/research/research_handler.py:318`
- `src/research_handler.py:882`
