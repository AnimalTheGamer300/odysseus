# `src/personal_docs.py` — definitions & call sites

28 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `extract_pdf_text` — function, line 16
- **called from:**
- `routes/email/email_helpers.py:1642`
- `routes/personal_routes.py:346`
- `src/personal_docs.py:127`
- `src/rag_vector.py:522`

## `extract_office_text` — function, line 31
- **called from:**
- `src/personal_docs.py:129`

## `PersonalDocsConfig` — class, line 46
- decorator: `dataclass`
- **called from:**
- `src/personal_docs.py:65`

## `PersonalDocsConfig.__post_init__` — method, line 56
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `read_text_file` — function, line 67
- **called from:**
- `src/document_processor.py:55`
- `src/personal_docs.py:131`

## `split_chunks` — function, line 75
- **called from:**
- `src/personal_docs.py:132`
- `tests/test_personal_docs_keyword_nondict.py:34`
- `tests/test_personal_docs_keyword_nondict.py:35`
- `tests/test_split_chunks_no_duplicate_tail.py:12`
- `tests/test_split_chunks_no_duplicate_tail.py:21`
- `tests/test_split_chunks_no_duplicate_tail.py:30`
- `tests/test_split_chunks_no_duplicate_tail.py:36`

## `tokenize` — function, line 96
- **called from:**
- `src/memory.py:34`
- `src/memory.py:35`
- `src/memory.py:375`
- `src/memory.py:400`
- `src/personal_docs.py:149`
- `src/personal_docs.py:158`

## `load_personal_index` — function, line 102
- **called from:**
- `src/personal_docs.py:393`
- `src/personal_docs.py:411`
- `tests/test_personal_docs_office_index.py:16`
- `tests/test_personal_docs_pdf_index.py:16`
- `tests/test_personal_index_hidden_dirs.py:19`
- `tests/test_personal_index_hidden_dirs.py:63`

## `retrieve_personal_keyword` — function, line 137
- **called from:**
- `src/personal_docs.py:205`
- `tests/test_personal_docs_keyword_nondict.py:14`
- `tests/test_personal_docs_keyword_nondict.py:20`
- `tests/test_personal_docs_keyword_nondict.py:27`
- `tests/test_personal_docs_keyword_nondict.py:28`

## `retrieve_personal` — function, line 168
- **called from:**
- `src/personal_docs.py:424`

## `_string_list` — function, line 208
- **called from:**
- `src/personal_docs.py:235`
- `src/personal_docs.py:247`
- `src/personal_docs.py:260`
- `src/personal_docs.py:270`
- `tests/test_personal_docs_lists.py:5`
- `tests/test_personal_docs_lists.py:6`

## `PersonalDocsManager` — class, line 212
- **called from:**
- `mcp_servers/rag_server.py:41`
- `src/app_initializer.py:97`
- `tests/test_personal_docs_exclusions.py:15`
- `tests/test_personal_docs_state_store.py:10`
- `tests/test_personal_docs_state_store.py:20`
- `tests/test_rag_remove_directory_scope.py:122`

## `PersonalDocsManager.__init__` — method, line 215
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

## `PersonalDocsManager.load_directories` — method, line 227
- **called from:**
- `src/personal_docs.py:223`

## `PersonalDocsManager.save_directories` — method, line 243
- **called from:**
- `src/personal_docs.py:298`
- `src/personal_docs.py:323`
- `src/personal_docs.py:369`

## `PersonalDocsManager._load_excluded` — method, line 252
- **called from:**
- `src/personal_docs.py:224`

## `PersonalDocsManager._save_excluded` — method, line 267
- **called from:**
- `src/personal_docs.py:277`
- `src/personal_docs.py:294`
- `src/personal_docs.py:379`

## `PersonalDocsManager.exclude_file` — method, line 274
- **called from:**
- `routes/personal_routes.py:432`

## `PersonalDocsManager.add_directory` — method, line 280
- **called from:**
- `mcp_servers/rag_server.py:124`
- `routes/personal_routes.py:224`
- `tests/test_personal_docs_exclusions.py:33`
- `tests/test_personal_docs_exclusions.py:48`

## `PersonalDocsManager.remove_directory` — method, line 316
- **called from:**
- `mcp_servers/rag_server.py:143`
- `mcp_servers/rag_server.py:145`
- `routes/personal_routes.py:282`
- `routes/personal_routes.py:286`
- `src/ai_interaction.py:687`
- `src/personal_docs.py:337`
- `src/rag_vector.py:602`
- `tests/test_embedding_lanes_rag.py:159`
- `tests/test_rag_remove_directory_scope.py:64`
- `tests/test_rag_remove_directory_scope.py:73`
- `tests/test_rag_remove_directory_scope.py:125`

## `PersonalDocsManager.rename_directory` — method, line 343
- **called from:**
- `routes/personal_routes.py:104`

## `PersonalDocsManager.rewrite` — method, line 349
- **called from:**
- `src/personal_docs.py:363`
- `src/personal_docs.py:374`
- `static/js/chat.js:9186`

## `PersonalDocsManager.get_indexed_directories` — method, line 384
- **called from:**
- `mcp_servers/rag_server.py:83`
- `routes/personal_routes.py:174`
- `src/ai_interaction.py:631`

## `PersonalDocsManager.refresh_index` — method, line 388
- **called from:**
- `src/personal_docs.py:225`
- `src/personal_docs.py:312`
- `src/personal_docs.py:327`
- `src/personal_docs.py:382`

## `PersonalDocsManager.retrieve` — method, line 422
- **called from:**
- `src/rag_manager.py:54`
- `src/tool_index.py:620`
- `src/tool_index.py:857`
- `tests/test_embedding_lanes_tool_index.py:33`
- `tests/test_embedding_lanes_tool_index.py:116`
- `tests/test_embedding_lanes_tool_index.py:178`

## `PersonalDocsManager.get_file_list` — method, line 426
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `PersonalDocsManager.get_stats` — method, line 430
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

## `PersonalDocsManager.index_all_directories` — method, line 452
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
