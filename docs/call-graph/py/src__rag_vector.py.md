# `src/rag_vector.py` — definitions & call sites

24 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_generate_doc_id` — function, line 48
- **called from:**
- `src/rag_vector.py:191`
- `src/rag_vector.py:227`

## `_rewrite_owner_path` — function, line 58
- **called from:**
- `src/rag_vector.py:322`

## `VectorRAG` — class, line 75
- **called from:**
- `src/rag_manager.py:31`
- `src/rag_singleton.py:49`
- `tests/test_embedding_lanes_rag.py:25`
- `tests/test_embedding_lanes_rag.py:46`
- `tests/test_embedding_lanes_rag.py:68`
- `tests/test_embedding_lanes_rag.py:103`

## `VectorRAG.__init__` — method, line 78
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

## `VectorRAG._initialize_system` — method, line 92
- **called from:**
- `src/rag_vector.py:86`

## `VectorRAG._embed` — method, line 116
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `VectorRAG.healthy` — method, line 126
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `VectorRAG.collection` — method, line 132
- decorator: `property`
- **called from:**
- `src/agent_runtime/owned_resources.py:292`
- `src/agent_runtime/owned_resources.py:323`
- `src/agent_runtime/owned_resources.py:337`
- `src/agent_runtime/owned_resources.py:353`
- `src/agent_runtime/owned_resources.py:391`

## `VectorRAG._active_collections` — method, line 136
- **called from:**
- `src/rag_vector.py:156`
- `src/rag_vector.py:407`
- `src/rag_vector.py:412`

## `VectorRAG._collections_for_delete` — method, line 143
- **called from:**
- `src/memory_vector.py:126`
- `src/rag_vector.py:297`
- `src/rag_vector.py:577`
- `src/rag_vector.py:685`

## `VectorRAG.add` — method, line 147
- **called from:**
- `companion/pairing.py:196`
- `core/database.py:554`
- `core/database.py:2269`
- `core/platform_compat.py:227`
- `core/session_manager.py:418`
- `core/session_manager.py:480`
- `core/session_manager.py:714`
- `core/session_manager.py:763`
- `core/session_manager.py:950`
- `mcp_servers/email_server.py:65`
- `mcp_servers/email_server.py:582`
- `mcp_servers/email_server.py:1027`
- `mcp_servers/email_server.py:1261`
- `mcp_servers/email_server.py:1345`
- `mcp_servers/email_server.py:2037`
- `mcp_servers/email_server.py:2224`
- `mcp_servers/email_server.py:2859`
- `mcp_servers/email_server.py:2905`
- `mcp_servers/email_server.py:2906`
- `mcp_servers/email_server.py:3075`
- `mcp_servers/email_server.py:3435`
- `mcp_servers/email_server.py:3441`
- `mcp_servers/email_server.py:3502`
- `mcp_servers/image_gen_server.py:144`
- `mcp_servers/memory_server.py:190`
- `mcp_servers/memory_server.py:219`
- `routes/api_token_routes.py:135`
- `routes/api_token_routes.py:179`
- `routes/backup_routes.py:105`
- `routes/backup_routes.py:176`
- `routes/backup_routes.py:178`
- `routes/backup_routes.py:179`
- `routes/calendar_routes.py:202`
- `routes/calendar_routes.py:330`
- `routes/calendar_routes.py:338`
- `routes/calendar_routes.py:760`
- `routes/calendar_routes.py:1390`
- `routes/calendar_routes.py:1545`
- `routes/calendar_routes.py:1612`
- `routes/calendar_routes.py:1713`
- `routes/chat_helpers.py:371`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:3606`
- `routes/chat_routes.py:3707`
- `routes/chat_routes.py:3943`
- `routes/chatgpt_subscription_routes.py:91`
- `routes/chatgpt_subscription_routes.py:155`
- `routes/chatgpt_subscription_routes.py:185`
- `routes/compare/compare_routes.py:218`
- `routes/compare/compare_routes.py:313`
- `routes/contacts/contacts_routes.py:590`
- `routes/contacts/contacts_routes.py:718`
- `routes/cookbook_routes.py:1479`
- `routes/cookbook_routes.py:1837`
- `routes/cookbook_routes.py:2885`
- `routes/cookbook_routes.py:3694`
- `routes/cookbook_routes.py:3761`
- `routes/cookbook_routes.py:3877`
- `routes/cookbook_routes.py:3964`
- `routes/copilot_routes.py:77`
- … +2020 more (grep the name in repo)

## `VectorRAG.add_document` — method, line 182
- **called from:**
- `routes/personal_routes.py:367`
- `services/docs/service.py:113`
- `src/rag_manager.py:66`
- `src/rag_vector.py:540`
- `tests/test_embedding_lanes_rag.py:26`

## `VectorRAG.add_documents_batch` — method, line 210
- **called from:**
- `src/rag_manager.py:70`
- `tests/test_embedding_lanes_rag.py:47`
- `tests/test_embedding_lanes_rag.py:69`

## `VectorRAG.rename_owner` — method, line 275
- **called from:**
- `routes/auth_routes.py:533`
- `routes/auth_routes.py:579`
- `routes/personal_routes.py:110`
- `tests/test_rag_vector_rename_owner.py:66`
- `tests/test_rename_user_owner_sync.py:323`
- `tests/test_rename_user_owner_sync.py:337`
- `tests/test_upload_handler_rename_owner.py:58`
- `tests/test_upload_handler_rename_owner.py:91`

## `VectorRAG.search` — method, line 348
- **called from:**
- `mcp_servers/email_server.py:63`
- `mcp_servers/email_server.py:457`
- `mcp_servers/email_server.py:463`
- `mcp_servers/email_server.py:476`
- `mcp_servers/email_server.py:560`
- `mcp_servers/email_server.py:629`
- `mcp_servers/email_server.py:1351`
- `mcp_servers/email_server.py:1354`
- `mcp_servers/email_server.py:2720`
- `routes/calendar_routes.py:1881`
- `routes/chat_helpers.py:39`
- `routes/chat_helpers.py:152`
- `routes/chat_helpers.py:698`
- `routes/chat_helpers.py:1379`
- `routes/chat_helpers.py:1776`
- `routes/chat_helpers.py:1804`
- `routes/chat_routes.py:247`
- `routes/chat_routes.py:256`
- `routes/chat_routes.py:266`
- `routes/chat_routes.py:276`
- `routes/chat_routes.py:291`
- `routes/chat_routes.py:314`
- `routes/chat_routes.py:325`
- `routes/chat_routes.py:346`
- `routes/chat_routes.py:347`
- `routes/chat_routes.py:355`
- `routes/chat_routes.py:359`
- `routes/chat_routes.py:388`
- `routes/chat_routes.py:389`
- `routes/chat_routes.py:1209`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1705`
- `routes/chat_routes.py:1818`
- `routes/chat_routes.py:1819`
- `routes/chat_routes.py:1822`
- `routes/chat_routes.py:1893`
- `routes/chat_routes.py:2776`
- `routes/chat_routes.py:2782`
- `routes/chat_routes.py:2798`
- `routes/chat_routes.py:2801`
- `routes/chat_routes.py:3466`
- `routes/chat_routes.py:3616`
- `routes/chat_routes.py:3617`
- `routes/contacts/contacts_routes.py:617`
- `routes/contacts/contacts_routes.py:621`
- `routes/contacts/contacts_routes.py:625`
- `routes/cookbook_helpers.py:684`
- `routes/cookbook_helpers.py:1302`
- `routes/cookbook_helpers.py:1305`
- `routes/cookbook_helpers.py:1623`
- `routes/cookbook_helpers.py:1625`
- `routes/cookbook_helpers.py:1625`
- `routes/cookbook_output.py:70`
- `routes/cookbook_routes.py:136`
- `routes/cookbook_routes.py:159`
- `routes/cookbook_routes.py:792`
- `routes/cookbook_routes.py:864`
- `routes/cookbook_routes.py:1423`
- `routes/cookbook_routes.py:1716`
- `routes/cookbook_routes.py:1717`
- … +2629 more (grep the name in repo)

## `VectorRAG._keyword_search_fallback` — method, line 405
- **called from:**
- `src/rag_vector.py:403`
- `tests/test_rag_keyword_fallback_owner.py:43`
- `tests/test_rag_keyword_fallback_owner.py:55`
- `tests/test_rag_vector_rename_owner.py:75`
- `tests/test_rag_vector_rename_owner.py:76`
- `tests/test_rag_vector_rename_owner.py:81`

## `VectorRAG.rebuild_index` — method, line 445
- **called from:**
- `services/docs/service.py:121`
- `src/rag_manager.py:58`
- `tests/test_embedding_lanes_rag.py:106`

## `VectorRAG.get_stats` — method, line 475
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

## `VectorRAG.index_personal_documents` — method, line 495
- **called from:**
- `mcp_servers/rag_server.py:116`
- `routes/personal_routes.py:218`
- `scripts/index_documents.py:85`
- `services/docs/service.py:104`
- `src/ai_interaction.py:666`
- `src/personal_docs.py:306`
- `src/personal_docs.py:463`
- `src/personal_docs.py:479`
- `src/rag_manager.py:46`
- `src/rag_vector.py:605`
- `tests/test_rag_index_hidden_dirs.py:46`
- `tests/test_rag_index_hidden_dirs.py:60`
- `tests/test_rag_index_hidden_dirs.py:75`
- `tests/test_rag_manager_owner_compat.py:25`

## `VectorRAG.remove_directory` — method, line 558
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

## `VectorRAG.reindex_directory` — method, line 599
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `VectorRAG._split_into_chunks` — method, line 621
- **called from:**
- `routes/personal_routes.py:355`
- `src/rag_vector.py:539`

## `VectorRAG.delete_by_source` — method, line 678
- **called from:**
- `routes/personal_routes.py:406`
- `tests/test_embedding_lanes_rag.py:212`

## `VectorRAG.retrieve` — method, line 704
- **called from:**
- `src/rag_manager.py:54`
- `src/tool_index.py:620`
- `src/tool_index.py:857`
- `tests/test_embedding_lanes_tool_index.py:33`
- `tests/test_embedding_lanes_tool_index.py:116`
- `tests/test_embedding_lanes_tool_index.py:178`
