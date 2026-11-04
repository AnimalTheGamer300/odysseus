# `src/deep_research.py` — definitions & call sites

24 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `current_date_context` — function, line 25
- **called from:**
- `src/deep_research.py:401`
- `src/deep_research.py:477`
- `src/research_handler.py:181`
- `tests/test_deep_research_date_context.py:25`

## `DeepResearcher` — class, line 184
- **called from:**
- `services/research/research_handler.py:265`
- `src/research_handler.py:817`
- `src/task_scheduler.py:2066`
- `tests/test_deep_research_extraction_controls.py:83`
- `tests/test_deep_research_extraction_controls.py:106`
- `tests/test_deep_research_extraction_controls.py:117`

## `DeepResearcher.__init__` — method, line 192
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

## `DeepResearcher.cancel` — method, line 245
- **called from:**
- `app.py:1283`
- `routes/shell_routes.py:723`
- `routes/shell_routes.py:1108`
- `routes/skills_routes.py:1800`
- `services/research/research_handler.py:140`
- `services/research/research_handler.py:143`
- `services/shell/service.py:163`
- `src/agent_loop.py:5124`
- `src/agent_loop.py:6401`
- `src/agent_runs.py:84`
- `src/agent_runs.py:195`
- `src/agent_runs.py:198`
- `src/agent_runs.py:237`
- `src/agent_runs.py:286`
- `src/agent_tools/subprocess_tools.py:273`
- `src/agent_tools/subprocess_tools.py:275`
- `src/agent_tools/subprocess_tools.py:279`
- `src/ai_interaction.py:1379`
- `src/ai_interaction.py:1646`
- `src/llm_core.py:109`
- `src/mcp_manager.py:400`
- `src/mcp_oauth.py:63`
- `src/research_handler.py:456`
- `src/research_handler.py:459`
- `src/task_scheduler.py:100`
- `src/task_scheduler.py:591`
- `src/task_scheduler.py:599`
- `src/task_scheduler.py:917`
- `src/task_scheduler.py:1012`
- `src/task_scheduler.py:2272`
- `src/task_scheduler.py:2296`
- `tests/test_builtin_mcp_bg_tasks.py:101`
- `tests/test_compare_stop_disconnect_poll.py:376`
- `tests/test_compare_stop_disconnect_poll.py:433`
- `tests/test_email_summary_llm.py:192`
- `tests/test_email_urgency_checkpoint.py:419`
- `tests/test_email_urgency_checkpoint.py:554`
- `tests/test_task_scheduler_cache.py:34`
- `tests/test_task_scheduler_cache.py:70`
- `static/js/chat.js:2849`
- `static/js/chat.js:5749`
- `static/js/chat.js:5764`
- `static/js/documentLibrary.js:182`
- `static/js/gallery.js:2576`
- `static/js/gallery.js:2584`
- `static/js/liveThinkingThrottle.js:20`
- `static/js/liveThinkingThrottle.js:22`
- `static/js/liveThinkingThrottle.js:193`
- `static/js/liveThinkingThrottle.js:198`
- `static/js/liveThinkingThrottle.js:199`
- `static/js/settings.js:883`
- `static/js/slashCommands.js:2439`
- `static/js/tasks.js:1076`
- `static/js/tts-ai.js:241`
- `static/js/windowDrag.js:157`

## `DeepResearcher.research` — method (async), line 252
- **called from:**
- `services/research/research_handler.py:278`
- `src/research_handler.py:837`
- `src/task_scheduler.py:2078`
- `tests/test_research_service.py:70`
- `tests/test_research_service.py:75`
- `tests/test_research_service.py:81`
- `tests/test_research_service.py:91`
- `tests/test_research_service.py:97`
- `tests/test_research_service.py:102`
- `tests/test_research_service.py:149`
- `static/js/research/panel.js:1213`

## `DeepResearcher._llm` — method (async), line 381
- **called from:**
- `src/deep_research.py:403`
- `src/deep_research.py:437`
- `src/deep_research.py:487`
- `src/deep_research.py:636`
- `src/deep_research.py:687`
- `src/deep_research.py:716`
- `src/deep_research.py:748`
- `src/deep_research.py:759`

## `DeepResearcher._create_plan` — method (async), line 399
- **called from:**
- `src/deep_research.py:274`
- `src/deep_research.py:279`
- `tests/test_deep_research_date_context.py:63`
- `tests/test_deep_research_extraction_controls.py:137`

## `DeepResearcher._classify_category` — method (async), line 426
- **called from:**
- `src/deep_research.py:282`

## `DeepResearcher._generate_queries` — method (async), line 461
- **called from:**
- `src/deep_research.py:304`
- `tests/test_deep_research_date_context.py:45`
- `tests/test_deep_research_extraction_controls.py:138`

## `DeepResearcher._search_and_extract` — method (async), line 507
- **called from:**
- `src/deep_research.py:314`
- `tests/test_deep_research_extraction_controls.py:42`
- `tests/test_deep_research_extraction_controls.py:53`

## `DeepResearcher._bounded_extract` — method (async), line 544
- **called from:**
- `src/deep_research.py:548`

## `DeepResearcher._search` — method (async), line 560
- **called from:**
- `src/deep_research.py:513`
- `tests/test_deep_research_search_error.py:47`
- `tests/test_deep_research_search_error.py:65`
- `tests/test_deep_research_search_error.py:81`

## `DeepResearcher._fetch_and_extract` — method (async), line 609
- **called from:**
- `src/deep_research.py:546`
- `tests/test_deep_research_extraction_controls.py:99`

## `DeepResearcher._synthesize` — method (async), line 671
- **called from:**
- `src/deep_research.py:343`
- `tests/test_deep_research_synthesis_resilience.py:55`
- `tests/test_deep_research_synthesis_resilience.py:85`

## `DeepResearcher._should_stop` — method (async), line 705
- **called from:**
- `src/deep_research.py:347`

## `DeepResearcher._final_report` — method (async), line 737
- **called from:**
- `src/deep_research.py:369`

## `DeepResearcher._emit` — method, line 788
- **called from:**
- `src/deep_research.py:273`
- `src/deep_research.py:278`
- `src/deep_research.py:301`
- `src/deep_research.py:309`
- `src/deep_research.py:319`
- `src/deep_research.py:329`
- `src/deep_research.py:340`
- `src/deep_research.py:353`
- `src/deep_research.py:423`
- `src/deep_research.py:501`
- `src/deep_research.py:613`
- `src/deep_research.py:699`
- `src/deep_research.py:758`

## `DeepResearcher._time_exceeded` — method, line 796
- **called from:**
- `src/deep_research.py:296`
- `src/deep_research.py:536`

## `DeepResearcher._strip_code_block` — method, line 802
- decorator: `staticmethod`
- **called from:**
- `src/deep_research.py:812`
- `src/deep_research.py:871`

## `DeepResearcher._parse_json_array` — method, line 810
- **called from:**
- `src/deep_research.py:493`
- `tests/test_deep_research_parse_json_array_echo.py:24`
- `tests/test_deep_research_parse_json_array_echo.py:32`
- `tests/test_deep_research_parse_json_array_echo.py:36`
- `tests/test_deep_research_parse_json_array_echo.py:40`
- `tests/test_deep_research_parse_json_array_echo.py:45`
- `tests/test_deep_research_parse_json_array_echo.py:50`
- `tests/test_deep_research_parse_json_array_echo.py:54`

## `DeepResearcher._parse_json_object` — method, line 869
- **called from:**
- `src/deep_research.py:410`
- `src/deep_research.py:645`

## `DeepResearcher._format_findings` — method, line 887
- **called from:**
- `src/deep_research.py:678`
- `src/deep_research.py:912`

## `DeepResearcher._fallback_report` — method, line 900
- **called from:**
- `src/deep_research.py:365`
- `tests/test_deep_research_synthesis_resilience.py:64`

## `DeepResearcher.get_stats` — method, line 915
- **called from:**
- `routes/diagnostics_routes.py:70`
- `routes/stt_routes.py:20`
- `routes/tts_routes.py:25`
- `scripts/index_documents.py:103`
- `services/docs/service.py:117`
- `services/research/research_handler.py:281`
- `src/rag_manager.py:62`
- `src/research_handler.py:364`
- `src/research_handler.py:388`
- `src/research_handler.py:845`
- `src/task_scheduler.py:2081`
- `tests/test_tts_cache_stats.py:10`
- `tests/test_tts_speed_malformed.py:22`
