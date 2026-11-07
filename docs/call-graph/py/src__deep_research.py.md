# `src/deep_research.py` — definitions & call sites

52 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `current_date_context` — function, line 27
- **called from:**
- `src/deep_research.py:647`
- `src/deep_research.py:745`
- `src/deep_research.py:821`
- `src/research_handler.py:197`
- `tests/test_deep_research_date_context.py:25`

## `_infer_research_category` — function, line 259
- **called from:**
- `src/deep_research.py:674`
- `tests/test_visual_research_mode.py:60`

## `_is_meta_search_query` — function, line 295
- **called from:**
- `src/deep_research.py:765`
- `src/deep_research.py:781`
- `src/deep_research.py:896`

## `DeepResearcher` — class, line 337
- **called from:**
- `services/research/research_handler.py:265`
- `src/research_handler.py:1045`
- `src/task_scheduler.py:2259`
- `tests/test_deep_research_extraction_controls.py:69`
- `tests/test_deep_research_extraction_controls.py:103`
- `tests/test_deep_research_extraction_controls.py:114`
- `tests/test_deep_research_full_loop_navigation.py:62`
- `tests/test_review_research_relevance.py:26`

## `DeepResearcher.__init__` — method, line 345
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

## `DeepResearcher.cancel` — method, line 408
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

## `DeepResearcher._looks_like_small_local_model` — method, line 413
- decorator: `staticmethod`
- **called from:**
- `src/deep_research.py:369`
- `tests/test_deep_research_date_context.py:92`
- `tests/test_deep_research_date_context.py:93`
- `tests/test_deep_research_date_context.py:94`
- `tests/test_deep_research_date_context.py:95`

## `DeepResearcher._looks_like_simple_fact_question` — method, line 427
- decorator: `staticmethod`
- **called from:**
- `src/deep_research.py:455`

## `DeepResearcher.research` — method (async), line 438
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

## `DeepResearcher._llm` — method (async), line 627
- **called from:**
- `src/deep_research.py:649`
- `src/deep_research.py:697`
- `src/deep_research.py:755`
- `src/deep_research.py:833`
- `src/deep_research.py:1343`
- `src/deep_research.py:1719`
- `src/deep_research.py:1750`
- `src/deep_research.py:1785`
- `src/deep_research.py:1796`

## `DeepResearcher._create_plan` — method (async), line 645
- **called from:**
- `src/deep_research.py:478`
- `src/deep_research.py:489`
- `tests/test_deep_research_date_context.py:63`
- `tests/test_deep_research_extraction_controls.py:134`

## `DeepResearcher._classify_category` — method (async), line 672
- **called from:**
- `src/deep_research.py:492`

## `DeepResearcher._generate_queries` — method (async), line 721
- **called from:**
- `src/deep_research.py:524`
- `tests/test_deep_research_action_planning.py:434`
- `tests/test_deep_research_date_context.py:45`
- `tests/test_deep_research_date_context.py:82`
- `tests/test_deep_research_extraction_controls.py:135`

## `DeepResearcher._plan_research_actions` — method (async), line 802
- **called from:**
- `src/deep_research.py:515`
- `tests/test_deep_research_action_planning.py:120`
- `tests/test_deep_research_action_planning.py:371`
- `tests/test_deep_research_action_planning.py:398`
- `tests/test_deep_research_action_planning.py:475`

## `DeepResearcher._normalize_research_actions` — method, line 858
- **called from:**
- `src/deep_research.py:846`
- `src/deep_research.py:939`
- `tests/test_deep_research_action_planning.py:129`
- `tests/test_deep_research_action_planning.py:146`
- `tests/test_deep_research_action_planning.py:164`
- `tests/test_deep_research_action_planning.py:196`
- `tests/test_deep_research_action_planning.py:231`
- `tests/test_deep_research_action_planning.py:252`

## `DeepResearcher._reject` — method, line 864
- **called from:**
- `src/deep_research.py:884`
- `src/deep_research.py:891`
- `src/deep_research.py:894`
- `src/deep_research.py:897`
- `src/deep_research.py:904`
- `src/deep_research.py:907`
- `src/deep_research.py:922`
- `src/deep_research.py:925`

## `DeepResearcher._merge_seed_actions` — method, line 933
- **called from:**
- `src/deep_research.py:517`
- `tests/test_deep_research_action_planning.py:277`

## `DeepResearcher._explicit_url_actions` — method, line 944
- **called from:**
- `src/deep_research.py:518`
- `tests/test_deep_research_action_planning.py:278`
- `tests/test_deep_research_action_planning.py:344`

## `DeepResearcher._extract_explicit_urls` — method, line 961
- decorator: `staticmethod`
- **called from:**
- `src/deep_research.py:948`

## `DeepResearcher._result_host` — method, line 971
- decorator: `staticmethod`
- **called from:**
- `src/deep_research.py:1071`

## `DeepResearcher._topic_terms` — method, line 976
- decorator: `staticmethod`
- **called from:**
- `src/deep_research.py:999`
- `src/deep_research.py:1018`
- `src/deep_research.py:1063`

## `DeepResearcher._topic_overlap` — method, line 997
- decorator: `classmethod`
- **called from:**
- `src/deep_research.py:1021`

## `DeepResearcher._topic_relevant` — method, line 1012
- decorator: `classmethod`
- **called from:**
- `src/deep_research.py:1096`
- `src/deep_research.py:1312`
- `src/deep_research.py:1319`
- `tests/test_review_research_relevance.py:16`
- `tests/test_review_research_relevance.py:20`

## `DeepResearcher._deterministic_search_topic` — method, line 1028
- decorator: `staticmethod`
- **called from:**
- `src/deep_research.py:773`

## `DeepResearcher._prioritize_search_results` — method, line 1041
- **called from:**
- `src/deep_research.py:1182`
- `tests/test_deep_research_action_planning.py:445`

## `DeepResearcher._execute_research_actions` — method (async), line 1136
- **called from:**
- `src/deep_research.py:536`
- `src/deep_research.py:1240`
- `tests/test_deep_research_action_planning.py:133`
- `tests/test_deep_research_action_planning.py:150`
- `tests/test_deep_research_action_planning.py:169`
- `tests/test_deep_research_action_planning.py:204`
- `tests/test_deep_research_action_planning.py:282`
- `tests/test_deep_research_action_planning.py:297`
- `tests/test_deep_research_action_planning.py:321`
- `tests/test_deep_research_action_planning.py:501`
- `tests/test_deep_research_action_planning.py:523`

## `DeepResearcher._bounded_extract` — method (async), line 1212
- **called from:**
- `src/deep_research.py:1224`

## `DeepResearcher._search_and_extract` — method (async), line 1236
- **called from:**
- `tests/test_deep_research_extraction_controls.py:41`
- `tests/test_deep_research_extraction_controls.py:52`

## `DeepResearcher._search` — method (async), line 1242
- **called from:**
- `src/deep_research.py:1148`
- `tests/test_deep_research_search_error.py:47`
- `tests/test_deep_research_search_error.py:65`
- `tests/test_deep_research_search_error.py:81`

## `DeepResearcher._fetch_and_extract` — method (async), line 1271
- **called from:**
- `src/deep_research.py:1217`
- `src/deep_research.py:1222`
- `tests/test_deep_research_browser_fallback.py:102`
- `tests/test_deep_research_browser_fallback.py:125`
- `tests/test_deep_research_browser_fallback.py:146`
- `tests/test_deep_research_browser_fallback.py:199`
- `tests/test_deep_research_extraction_controls.py:96`
- `tests/test_review_research_relevance.py:42`

## `DeepResearcher._browser_fallback` — method (async), line 1451
- **called from:**
- `src/deep_research.py:1301`
- `src/deep_research.py:1314`
- `src/deep_research.py:1401`

## `DeepResearcher._mark_analyzed_url` — method, line 1485
- **called from:**
- `src/deep_research.py:1380`
- `src/deep_research.py:1381`
- `src/deep_research.py:1432`

## `DeepResearcher._record_navigation` — method, line 1491
- **called from:**
- `src/deep_research.py:1259`
- `src/deep_research.py:1268`
- `src/deep_research.py:1293`
- `src/deep_research.py:1321`
- `src/deep_research.py:1354`
- `src/deep_research.py:1390`
- `src/deep_research.py:1406`
- `src/deep_research.py:1423`
- `src/deep_research.py:1470`
- `src/deep_research.py:1481`
- `tests/test_deep_research_action_planning.py:537`

## `DeepResearcher._record_action_plan` — method, line 1518
- **called from:**
- `src/deep_research.py:526`
- `src/deep_research.py:853`
- `tests/test_deep_research_action_planning.py:168`
- `tests/test_deep_research_action_planning.py:203`

## `DeepResearcher._record_action_rejections` — method, line 1540
- **called from:**
- `src/deep_research.py:855`

## `DeepResearcher._navigation_trace_summary` — method, line 1562
- **called from:**
- `src/deep_research.py:827`
- `src/deep_research.py:1715`
- `src/deep_research.py:1779`
- `tests/test_deep_research_action_planning.py:541`
- `tests/test_deep_research_browser_fallback.py:172`

## `DeepResearcher._source_state_summary` — method, line 1589
- **called from:**
- `src/deep_research.py:546`
- `src/deep_research.py:571`
- `src/deep_research.py:584`
- `src/deep_research.py:825`
- `src/deep_research.py:1713`
- `src/deep_research.py:1743`
- `src/deep_research.py:1777`
- `src/research_handler.py:587`
- `src/research_handler.py:758`
- `tests/test_deep_research_action_planning.py:636`

## `DeepResearcher._source_coverage` — method, line 1609
- **called from:**
- `src/deep_research.py:1591`
- `src/deep_research.py:1674`
- `src/deep_research.py:1682`
- `src/research_handler.py:601`
- `src/research_handler.py:759`
- `tests/test_deep_research_action_planning.py:667`

## `DeepResearcher._source_coverage_json` — method, line 1672
- **called from:**
- `src/deep_research.py:826`
- `src/deep_research.py:1714`
- `src/deep_research.py:1744`
- `src/deep_research.py:1778`

## `DeepResearcher._needs_more_evidence_before_stop` — method, line 1678
- **called from:**
- `src/deep_research.py:577`
- `tests/test_deep_research_action_planning.py:691`
- `tests/test_deep_research_action_planning.py:700`

## `DeepResearcher._synthesize` — method (async), line 1700
- **called from:**
- `src/deep_research.py:572`
- `tests/test_deep_research_action_planning.py:570`
- `tests/test_deep_research_synthesis_resilience.py:55`
- `tests/test_deep_research_synthesis_resilience.py:85`

## `DeepResearcher._should_stop` — method (async), line 1737
- **called from:**
- `src/deep_research.py:586`
- `tests/test_deep_research_action_planning.py:722`

## `DeepResearcher._final_report` — method (async), line 1771
- **called from:**
- `src/deep_research.py:615`
- `tests/test_deep_research_action_planning.py:610`

## `DeepResearcher._emit` — method, line 1825
- **called from:**
- `src/deep_research.py:470`
- `src/deep_research.py:482`
- `src/deep_research.py:511`
- `src/deep_research.py:531`
- `src/deep_research.py:542`
- `src/deep_research.py:553`
- `src/deep_research.py:568`
- `src/deep_research.py:580`
- `src/deep_research.py:592`
- `src/deep_research.py:669`
- `src/deep_research.py:790`
- `src/deep_research.py:799`
- `src/deep_research.py:841`
- `src/deep_research.py:1275`
- `src/deep_research.py:1466`
- `src/deep_research.py:1731`
- `src/deep_research.py:1795`

## `DeepResearcher._time_exceeded` — method, line 1833
- **called from:**
- `src/deep_research.py:506`
- `src/deep_research.py:1204`

## `DeepResearcher._strip_code_block` — method, line 1839
- decorator: `staticmethod`
- **called from:**
- `src/deep_research.py:1849`
- `src/deep_research.py:1908`

## `DeepResearcher._parse_json_array` — method, line 1847
- **called from:**
- `src/deep_research.py:761`
- `tests/test_deep_research_parse_json_array_echo.py:24`
- `tests/test_deep_research_parse_json_array_echo.py:32`
- `tests/test_deep_research_parse_json_array_echo.py:36`
- `tests/test_deep_research_parse_json_array_echo.py:40`
- `tests/test_deep_research_parse_json_array_echo.py:45`
- `tests/test_deep_research_parse_json_array_echo.py:50`
- `tests/test_deep_research_parse_json_array_echo.py:54`

## `DeepResearcher._parse_json_object` — method, line 1906
- **called from:**
- `src/deep_research.py:656`
- `src/deep_research.py:1364`

## `DeepResearcher._format_findings` — method, line 1924
- **called from:**
- `src/deep_research.py:1707`
- `src/deep_research.py:1949`

## `DeepResearcher._fallback_report` — method, line 1937
- **called from:**
- `src/deep_research.py:604`
- `tests/test_deep_research_synthesis_resilience.py:64`

## `DeepResearcher._compact_fact_report` — method, line 1952
- **called from:**
- `src/deep_research.py:565`

## `DeepResearcher.get_stats` — method, line 1963
- **called from:**
- `routes/diagnostics_routes.py:70`
- `routes/stt_routes.py:20`
- `routes/tts_routes.py:25`
- `scripts/index_documents.py:103`
- `services/docs/service.py:117`
- `services/research/research_handler.py:281`
- `src/rag_manager.py:62`
- `src/research_handler.py:382`
- `src/research_handler.py:406`
- `src/research_handler.py:1074`
- `src/task_scheduler.py:2275`
- `tests/test_deep_research_action_planning.py:490`
- `tests/test_tts_cache_stats.py:10`
- `tests/test_tts_speed_malformed.py:22`
