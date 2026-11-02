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
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

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
- `core/database.py:524`
- `core/database.py:2010`
- `core/platform_compat.py:205`
- `core/session_manager.py:416`
- `core/session_manager.py:478`
- `core/session_manager.py:807`
- `core/session_manager.py:856`
- `core/session_manager.py:1053`
- `mcp_servers/email_server.py:552`
- `mcp_servers/email_server.py:1665`
- `mcp_servers/email_server.py:1706`
- `mcp_servers/email_server.py:1707`
- `mcp_servers/email_server.py:1828`
- `mcp_servers/image_gen_server.py:143`
- `mcp_servers/memory_server.py:190`
- `mcp_servers/memory_server.py:219`
- `routes/api_token_routes.py:135`
- `routes/api_token_routes.py:179`
- `routes/backup_routes.py:105`
- `routes/backup_routes.py:176`
- `routes/backup_routes.py:178`
- `routes/backup_routes.py:179`
- `routes/calendar_routes.py:190`
- `routes/calendar_routes.py:316`
- `routes/calendar_routes.py:324`
- `routes/calendar_routes.py:1253`
- `routes/calendar_routes.py:1374`
- `routes/calendar_routes.py:1441`
- `routes/calendar_routes.py:1540`
- `routes/chat_helpers.py:86`
- `routes/chat_routes.py:1688`
- `routes/chat_routes.py:1742`
- `routes/chatgpt_subscription_routes.py:54`
- `routes/chatgpt_subscription_routes.py:79`
- `routes/compare/compare_routes.py:218`
- `routes/compare/compare_routes.py:313`
- `routes/contacts/contacts_routes.py:476`
- `routes/contacts/contacts_routes.py:604`
- `routes/cookbook_routes.py:1579`
- `routes/cookbook_routes.py:1916`
- `routes/cookbook_routes.py:3006`
- `routes/cookbook_routes.py:3788`
- `routes/cookbook_routes.py:3855`
- `routes/cookbook_routes.py:3971`
- `routes/cookbook_routes.py:4058`
- `routes/copilot_routes.py:77`
- `routes/device_flow.py:154`
- `routes/document/document_routes.py:165`
- `routes/document/document_routes.py:201`
- `routes/document/document_routes.py:202`
- `routes/document/document_routes.py:545`
- `routes/document/document_routes.py:604`
- `routes/document/document_routes.py:683`
- `routes/document/document_routes.py:839`
- `routes/editor_draft_routes.py:126`
- `routes/email_helpers.py:1700`
- `routes/email_helpers.py:1732`
- `routes/email_helpers.py:1868`
- `routes/email_pollers.py:810`
- … +1237 more (grep the name in repo)

## `VectorRAG.add_document` — method, line 182
- **called from:**
- `routes/personal_routes.py:381`
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
- `routes/auth_routes.py:483`
- `routes/auth_routes.py:529`
- `routes/personal_routes.py:115`
- `tests/test_rag_vector_rename_owner.py:66`
- `tests/test_rename_user_owner_sync.py:323`
- `tests/test_rename_user_owner_sync.py:337`
- `tests/test_upload_handler_rename_owner.py:58`
- `tests/test_upload_handler_rename_owner.py:91`

## `VectorRAG.search` — method, line 348
- **called from:**
- `mcp_servers/email_server.py:427`
- `mcp_servers/email_server.py:433`
- `mcp_servers/email_server.py:446`
- `mcp_servers/email_server.py:530`
- `mcp_servers/email_server.py:599`
- `mcp_servers/email_server.py:1529`
- `routes/calendar_routes.py:1706`
- `routes/chat_helpers.py:66`
- `routes/chat_helpers.py:1148`
- `routes/chat_helpers.py:1176`
- `routes/chat_routes.py:493`
- `routes/chat_routes.py:495`
- `routes/chat_routes.py:500`
- `routes/chat_routes.py:502`
- `routes/chat_routes.py:550`
- `routes/chat_routes.py:1205`
- `routes/chat_routes.py:1209`
- `routes/contacts/contacts_routes.py:503`
- `routes/contacts/contacts_routes.py:507`
- `routes/contacts/contacts_routes.py:511`
- `routes/cookbook_helpers.py:680`
- `routes/cookbook_helpers.py:1129`
- `routes/cookbook_helpers.py:1132`
- `routes/cookbook_helpers.py:1436`
- `routes/cookbook_helpers.py:1438`
- `routes/cookbook_helpers.py:1438`
- `routes/cookbook_output.py:56`
- `routes/cookbook_routes.py:124`
- `routes/cookbook_routes.py:147`
- `routes/cookbook_routes.py:590`
- `routes/cookbook_routes.py:592`
- `routes/cookbook_routes.py:592`
- `routes/cookbook_routes.py:918`
- `routes/cookbook_routes.py:990`
- `routes/cookbook_routes.py:1528`
- `routes/cookbook_routes.py:1787`
- `routes/cookbook_routes.py:1788`
- `routes/cookbook_routes.py:1808`
- `routes/cookbook_routes.py:1823`
- `routes/cookbook_routes.py:2046`
- `routes/cookbook_routes.py:2173`
- `routes/cookbook_routes.py:2293`
- `routes/cookbook_routes.py:2684`
- `routes/cookbook_routes.py:3547`
- `routes/cookbook_routes.py:3751`
- `routes/cookbook_routes.py:3753`
- `routes/cookbook_routes.py:3755`
- `routes/cookbook_routes.py:3757`
- `routes/cookbook_routes.py:3763`
- `routes/cookbook_routes.py:3824`
- `routes/cookbook_routes.py:3827`
- `routes/cookbook_routes.py:3829`
- `routes/cookbook_routes.py:3973`
- `routes/cookbook_routes.py:4238`
- `routes/cookbook_routes.py:4488`
- `routes/cookbook_routes.py:4494`
- `routes/cookbook_routes.py:4513`
- `routes/document/document_helpers.py:227`
- `routes/document/document_routes.py:63`
- `routes/document/document_routes.py:64`
- … +331 more (grep the name in repo)

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
- `src/research_handler.py:364`
- `src/research_handler.py:388`
- `src/research_handler.py:845`
- `src/task_scheduler.py:2081`
- `tests/test_tts_cache_stats.py:10`
- `tests/test_tts_speed_malformed.py:22`

## `VectorRAG.index_personal_documents` — method, line 495
- **called from:**
- `mcp_servers/rag_server.py:116`
- `routes/personal_routes.py:232`
- `scripts/index_documents.py:85`
- `services/docs/service.py:104`
- `src/ai_interaction.py:581`
- `src/personal_docs.py:302`
- `src/personal_docs.py:459`
- `src/personal_docs.py:475`
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
- `routes/personal_routes.py:296`
- `routes/personal_routes.py:300`
- `src/ai_interaction.py:602`
- `src/personal_docs.py:333`
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
- `routes/personal_routes.py:369`
- `src/rag_vector.py:539`

## `VectorRAG.delete_by_source` — method, line 678
- **called from:**
- `routes/personal_routes.py:420`
- `tests/test_embedding_lanes_rag.py:212`

## `VectorRAG.retrieve` — method, line 704
- **called from:**
- `src/rag_manager.py:54`
- `src/tool_index.py:534`
- `tests/test_embedding_lanes_tool_index.py:33`
- `tests/test_embedding_lanes_tool_index.py:116`
- `tests/test_embedding_lanes_tool_index.py:178`
