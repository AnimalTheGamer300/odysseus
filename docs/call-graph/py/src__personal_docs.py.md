# `src/personal_docs.py` — definitions & call sites

28 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `extract_pdf_text` — function, line 16
- **called from:**
- `routes/email_helpers.py:1495`
- `routes/personal_routes.py:360`
- `src/personal_docs.py:123`
- `src/rag_vector.py:522`

## `extract_office_text` — function, line 31
- **called from:**
- `src/personal_docs.py:125`

## `PersonalDocsConfig` — class, line 42
- decorator: `dataclass`
- **called from:**
- `src/personal_docs.py:61`

## `PersonalDocsConfig.__post_init__` — method, line 52
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `read_text_file` — function, line 63
- **called from:**
- `src/document_processor.py:52`
- `src/personal_docs.py:127`

## `split_chunks` — function, line 71
- **called from:**
- `src/personal_docs.py:128`
- `tests/test_personal_docs_keyword_nondict.py:34`
- `tests/test_personal_docs_keyword_nondict.py:35`
- `tests/test_split_chunks_no_duplicate_tail.py:12`
- `tests/test_split_chunks_no_duplicate_tail.py:21`
- `tests/test_split_chunks_no_duplicate_tail.py:30`
- `tests/test_split_chunks_no_duplicate_tail.py:36`

## `tokenize` — function, line 92
- **called from:**
- `src/memory.py:34`
- `src/memory.py:35`
- `src/memory.py:414`
- `src/memory.py:415`
- `src/personal_docs.py:145`
- `src/personal_docs.py:154`

## `load_personal_index` — function, line 98
- **called from:**
- `src/personal_docs.py:389`
- `src/personal_docs.py:407`
- `tests/test_personal_docs_office_index.py:16`
- `tests/test_personal_docs_pdf_index.py:16`
- `tests/test_personal_index_hidden_dirs.py:19`
- `tests/test_personal_index_hidden_dirs.py:63`

## `retrieve_personal_keyword` — function, line 133
- **called from:**
- `src/personal_docs.py:201`
- `tests/test_personal_docs_keyword_nondict.py:14`
- `tests/test_personal_docs_keyword_nondict.py:20`
- `tests/test_personal_docs_keyword_nondict.py:27`
- `tests/test_personal_docs_keyword_nondict.py:28`

## `retrieve_personal` — function, line 164
- **called from:**
- `src/personal_docs.py:420`

## `_string_list` — function, line 204
- **called from:**
- `src/personal_docs.py:231`
- `src/personal_docs.py:243`
- `src/personal_docs.py:256`
- `src/personal_docs.py:266`
- `tests/test_personal_docs_lists.py:5`
- `tests/test_personal_docs_lists.py:6`

## `PersonalDocsManager` — class, line 208
- **called from:**
- `mcp_servers/rag_server.py:41`
- `src/app_initializer.py:97`
- `tests/test_personal_docs_exclusions.py:15`
- `tests/test_personal_docs_state_store.py:10`
- `tests/test_personal_docs_state_store.py:20`
- `tests/test_rag_remove_directory_scope.py:122`

## `PersonalDocsManager.__init__` — method, line 211
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

## `PersonalDocsManager.load_directories` — method, line 223
- **called from:**
- `src/personal_docs.py:219`

## `PersonalDocsManager.save_directories` — method, line 239
- **called from:**
- `src/personal_docs.py:294`
- `src/personal_docs.py:319`
- `src/personal_docs.py:365`

## `PersonalDocsManager._load_excluded` — method, line 248
- **called from:**
- `src/personal_docs.py:220`

## `PersonalDocsManager._save_excluded` — method, line 263
- **called from:**
- `src/personal_docs.py:273`
- `src/personal_docs.py:290`
- `src/personal_docs.py:375`

## `PersonalDocsManager.exclude_file` — method, line 270
- **called from:**
- `routes/personal_routes.py:446`

## `PersonalDocsManager.add_directory` — method, line 276
- **called from:**
- `mcp_servers/rag_server.py:124`
- `routes/personal_routes.py:238`
- `tests/test_personal_docs_exclusions.py:33`
- `tests/test_personal_docs_exclusions.py:48`

## `PersonalDocsManager.remove_directory` — method, line 312
- **called from:**
- `mcp_servers/rag_server.py:143`
- `mcp_servers/rag_server.py:145`
- `routes/personal_routes.py:296`
- `routes/personal_routes.py:300`
- `src/ai_interaction.py:602`
- `src/personal_docs.py:333`
- `src/rag_vector.py:602`
- `tests/test_embedding_lanes_rag.py:159`
- `tests/test_rag_remove_directory_scope.py:64`
- `tests/test_rag_remove_directory_scope.py:73`
- `tests/test_rag_remove_directory_scope.py:125`

## `PersonalDocsManager.rename_directory` — method, line 339
- **called from:**
- `routes/personal_routes.py:109`

## `PersonalDocsManager.rewrite` — method, line 345
- **called from:**
- `src/personal_docs.py:359`
- `src/personal_docs.py:370`
- `static/js/chat.js:7573`

## `PersonalDocsManager.get_indexed_directories` — method, line 380
- **called from:**
- `mcp_servers/rag_server.py:83`
- `routes/personal_routes.py:188`
- `src/ai_interaction.py:546`

## `PersonalDocsManager.refresh_index` — method, line 384
- **called from:**
- `src/personal_docs.py:221`
- `src/personal_docs.py:308`
- `src/personal_docs.py:323`
- `src/personal_docs.py:378`

## `PersonalDocsManager.retrieve` — method, line 418
- **called from:**
- `src/rag_manager.py:54`
- `src/tool_index.py:534`
- `tests/test_embedding_lanes_tool_index.py:33`
- `tests/test_embedding_lanes_tool_index.py:116`
- `tests/test_embedding_lanes_tool_index.py:178`

## `PersonalDocsManager.get_file_list` — method, line 422
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `PersonalDocsManager.get_stats` — method, line 426
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

## `PersonalDocsManager.index_all_directories` — method, line 448
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
