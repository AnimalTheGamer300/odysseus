# `src/research_handler.py` — definitions & call sites

47 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_bounded_int` — function, line 39
- **called from:**
- `src/research_handler.py:299`
- `src/research_handler.py:1020`
- `src/research_handler.py:1026`
- `src/research_handler.py:1032`
- `src/research_handler.py:1038`

## `_format_probe_failure` — function, line 47
- **called from:**
- `src/research_handler.py:959`
- `tests/test_research_probe_errors.py:19`
- `tests/test_research_probe_errors.py:30`
- `tests/test_research_probe_errors.py:36`

## `_research_json_path` — function, line 65
- **called from:**
- `src/research_handler.py:281`
- `src/research_handler.py:453`
- `src/research_handler.py:516`
- `src/research_handler.py:540`
- `src/research_handler.py:559`
- `src/research_handler.py:720`
- `src/research_handler.py:734`
- `src/research_handler.py:797`
- `src/research_handler.py:873`
- `src/research_handler.py:905`
- `src/research_handler.py:925`
- `tests/test_research_handler_path_confinement.py:19`
- `tests/test_research_handler_path_confinement.py:28`
- `tests/test_research_handler_path_confinement.py:45`

## `ResearchHandler` — class, line 77
- **called from:**
- `services/research/service.py:46`
- `src/app_initializer.py:130`
- `tests/test_research_query_fallback.py:23`
- `tests/test_research_source_metadata.py:53`
- `tests/test_research_source_metadata.py:67`
- `tests/test_research_source_metadata.py:86`

## `ResearchHandler.__init__` — method, line 80
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

## `ResearchHandler._initialize_legacy_engine` — method, line 86
- **called from:**
- `services/research/research_handler.py:31`
- `src/research_handler.py:83`

## `ResearchHandler.synthesize_query` — method (async), line 104
- **called from:**
- `routes/chat_routes.py:4195`
- `tests/test_research_query_fallback.py:38`
- `tests/test_research_query_fallback.py:49`
- `tests/test_research_query_fallback.py:60`
- `tests/test_research_query_fallback.py:72`
- `tests/test_research_query_fallback.py:84`
- `tests/test_research_query_fallback.py:92`
- `tests/test_research_query_fallback.py:109`

## `ResearchHandler._normalize` — method, line 134
- **called from:**
- `src/research_handler.py:138`
- `src/research_handler.py:142`

## `ResearchHandler._is_continuation` — method, line 137
- **called from:**
- `src/research_handler.py:143`
- `src/research_handler.py:148`

## `ResearchHandler._fallback` — method, line 141
- **called from:**
- `src/research_handler.py:153`
- `src/research_handler.py:187`
- `static/js/emailInbox.js:836`
- `static/js/emailInbox.js:837`
- `static/js/emailInbox.js:838`
- `static/js/emailInbox.js:839`
- `static/js/emailInbox.js:840`
- `static/js/emailInbox.js:841`
- `static/js/emailInbox.js:842`

## `ResearchHandler.generate_plan` — method (async), line 189
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResearchHandler.rename_owner` — method, line 240
- **called from:**
- `routes/auth_routes.py:533`
- `routes/auth_routes.py:579`
- `routes/personal_routes.py:110`
- `tests/test_rag_vector_rename_owner.py:66`
- `tests/test_rename_user_owner_sync.py:323`
- `tests/test_rename_user_owner_sync.py:337`
- `tests/test_upload_handler_rename_owner.py:58`
- `tests/test_upload_handler_rename_owner.py:91`

## `ResearchHandler.start_research` — method, line 256
- **called from:**
- `routes/chat_routes.py:4200`
- `routes/research/research_routes.py:629`
- `services/research/service.py:157`
- `tests/test_research_handler_path_confinement.py:83`

## `ResearchHandler.on_progress` — method, line 327
- **called from:**
- `src/research_handler.py:394`
- `src/research_handler.py:416`

## `ResearchHandler._guarded_complete` — method, line 332
- **called from:**
- `src/research_handler.py:371`
- `src/research_handler.py:389`
- `src/research_handler.py:413`

## `ResearchHandler._run` — method (async), line 340
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

## `ResearchHandler.get_status` — method, line 425
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

## `ResearchHandler.get_category` — method, line 473
- **called from:**
- `routes/research/research_routes.py:281`
- `routes/research/research_routes.py:346`
- `routes/research/research_routes.py:678`
- `routes/research/research_routes.py:753`

## `ResearchHandler.get_mode` — method, line 486
- **called from:**
- `routes/research/research_routes.py:282`
- `routes/research/research_routes.py:347`
- `routes/research/research_routes.py:679`
- `routes/research/research_routes.py:754`

## `ResearchHandler.cancel_research` — method, line 493
- **called from:**
- `routes/research/research_routes.py:327`
- `services/research/research_handler.py:66`
- `services/research/service.py:167`
- `src/research_handler.py:310`

## `ResearchHandler.get_result` — method, line 509
- **called from:**
- `routes/research/research_routes.py:336`
- `routes/research/research_routes.py:720`
- `routes/research/research_routes.py:778`
- `src/background_tool_jobs.py:136`
- `tests/test_research_handler_path_confinement.py:55`

## `ResearchHandler.get_sources` — method, line 529
- **called from:**
- `routes/chat_routes.py:4234`
- `routes/research/research_routes.py:339`
- `routes/research/research_routes.py:737`
- `routes/research/research_routes.py:779`
- `src/background_tool_jobs.py:137`
- `tests/test_research_handler_path_confinement.py:56`

## `ResearchHandler.get_raw_findings` — method, line 551
- **called from:**
- `routes/chat_routes.py:4238`
- `routes/research/research_routes.py:340`
- `routes/research/research_routes.py:738`
- `tests/test_research_handler_path_confinement.py:57`

## `ResearchHandler.get_analyzed_urls` — method, line 570
- **called from:**
- `routes/research/research_routes.py:341`
- `routes/research/research_routes.py:739`

## `ResearchHandler.get_source_state` — method, line 581
- **called from:**
- `routes/research/research_routes.py:276`
- `routes/research/research_routes.py:302`
- `routes/research/research_routes.py:342`
- `routes/research/research_routes.py:682`
- `routes/research/research_routes.py:740`

## `ResearchHandler.get_source_coverage` — method, line 595
- **called from:**
- `routes/research/research_routes.py:277`
- `routes/research/research_routes.py:305`
- `routes/research/research_routes.py:343`
- `routes/research/research_routes.py:685`
- `routes/research/research_routes.py:741`
- `tests/test_research_source_metadata.py:99`

## `ResearchHandler.get_navigation_trace` — method, line 611
- **called from:**
- `routes/research/research_routes.py:278`
- `routes/research/research_routes.py:311`
- `routes/research/research_routes.py:344`
- `routes/research/research_routes.py:688`
- `routes/research/research_routes.py:742`
- `tests/test_research_source_metadata.py:61`

## `ResearchHandler.get_action_trace` — method, line 624
- **called from:**
- `routes/research/research_routes.py:279`
- `routes/research/research_routes.py:314`
- `routes/research/research_routes.py:345`
- `routes/research/research_routes.py:691`
- `routes/research/research_routes.py:743`
- `tests/test_research_source_metadata.py:80`
- `tests/test_research_source_metadata.py:145`

## `ResearchHandler._source_metadata` — method, line 638
- decorator: `staticmethod`
- **called from:**
- `src/research_handler.py:668`
- `src/research_handler.py:687`

## `ResearchHandler._extract_sources` — method, line 652
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

## `ResearchHandler._extract_raw_findings` — method, line 673
- decorator: `staticmethod`
- **called from:**
- `src/research_handler.py:370`
- `src/research_handler.py:388`
- `src/research_handler.py:412`
- `src/research_handler.py:557`
- `src/research_handler.py:744`
- `src/task_scheduler.py:2314`
- `tests/test_research_handler_raw_nondict.py:13`
- `tests/test_research_source_metadata.py:31`

## `ResearchHandler.get_avg_duration` — method, line 694
- **called from:**
- `src/research_handler.py:447`

## `ResearchHandler.clear_result` — method, line 714
- **called from:**
- `routes/chat_routes.py:4245`
- `routes/research/research_routes.py:348`
- `tests/test_research_handler_path_confinement.py:70`

## `ResearchHandler._save_result` — method, line 731
- **called from:**
- `services/research/research_handler.py:93`
- `src/research_handler.py:365`
- `src/research_handler.py:385`
- `src/research_handler.py:409`
- `tests/test_research_handler_path_confinement.py:71`
- `tests/test_research_source_metadata.py:130`

## `ResearchHandler._get_session_json` — method, line 795
- **called from:**
- `routes/chat_routes.py:4137`
- `routes/chat_routes.py:4185`
- `src/research_handler.py:483`
- `src/research_handler.py:490`
- `src/research_handler.py:576`
- `src/research_handler.py:590`
- `src/research_handler.py:605`
- `src/research_handler.py:618`
- `src/research_handler.py:631`
- `tests/test_research_handler_path_confinement.py:58`

## `ResearchHandler._format_trace_value` — method, line 808
- decorator: `staticmethod`
- **called from:**
- `src/research_handler.py:837`
- `src/research_handler.py:838`
- `src/research_handler.py:839`
- `src/research_handler.py:840`
- `src/research_handler.py:842`
- `src/research_handler.py:853`
- `src/research_handler.py:854`
- `src/research_handler.py:855`
- `src/research_handler.py:860`

## `ResearchHandler._research_diagnostics_markdown` — method, line 813
- decorator: `staticmethod`
- **called from:**
- `src/research_handler.py:885`
- `tests/test_research_source_metadata.py:178`

## `ResearchHandler.get_report_html` — method, line 871
- **called from:**
- `routes/research/research_routes.py:381`
- `tests/test_research_handler_path_confinement.py:59`

## `ResearchHandler.hide_image` — method, line 903
- **called from:**
- `routes/research/research_routes.py:400`
- `tests/test_research_handler_path_confinement.py:68`

## `ResearchHandler.unhide_all_images` — method, line 923
- **called from:**
- `routes/research/research_routes.py:411`
- `tests/test_research_handler_path_confinement.py:69`

## `ResearchHandler._probe_endpoint` — method (async), line 941
- decorator: `staticmethod`
- **called from:**
- `routes/cookbook_routes.py:1814`
- `routes/cookbook_routes.py:1855`
- `routes/model_routes.py:1630`
- `routes/model_routes.py:2023`
- `routes/model_routes.py:2281`
- `routes/model_routes.py:2319`
- `routes/model_routes.py:2442`
- `routes/model_routes.py:2471`
- `routes/model_routes.py:2531`
- `src/research_handler.py:1013`
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
- `tests/test_featherless_provider.py:96`
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

## `ResearchHandler.call_research_service` — method (async), line 961
- **called from:**
- `routes/chat_routes.py:2519`
- `routes/diagnostics_routes.py:100`
- `services/research/research_handler.py:84`
- `services/research/service.py:73`
- `src/research_handler.py:345`

## `ResearchHandler._fallback_research` — method (async), line 1093
- **called from:**
- `services/research/research_handler.py:295`
- `src/research_handler.py:1091`

## `ResearchHandler._get_legacy_stats` — method, line 1116
- **called from:**
- `services/research/research_handler.py:311`
- `src/research_handler.py:1107`

## `ResearchHandler._format_research_report` — method, line 1131
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

## `ResearchHandler._format_error_response` — method, line 1156
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResearchHandler._handle_research_failure` — method, line 1175
- **called from:**
- `services/research/research_handler.py:318`
- `src/research_handler.py:1114`
