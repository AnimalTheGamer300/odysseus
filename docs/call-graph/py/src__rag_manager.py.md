# `src/rag_manager.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `RAGManager` — class, line 23
- **called from:**
- `scripts/index_documents.py:48`
- `services/docs/service.py:39`
- `tests/test_rag_search_signature.py:13`

## `RAGManager.__init__` — method, line 29
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

## `RAGManager.search` — method, line 35
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
- … +326 more (grep the name in repo)

## `RAGManager.index_personal_documents` — method, line 39
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

## `RAGManager.retrieve` — method, line 52
- **called from:**
- `src/rag_manager.py:54`
- `src/tool_index.py:534`
- `tests/test_embedding_lanes_tool_index.py:33`
- `tests/test_embedding_lanes_tool_index.py:116`
- `tests/test_embedding_lanes_tool_index.py:178`

## `RAGManager.rebuild_index` — method, line 56
- **called from:**
- `services/docs/service.py:121`
- `src/rag_manager.py:58`
- `tests/test_embedding_lanes_rag.py:106`

## `RAGManager.get_stats` — method, line 60
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

## `RAGManager.add_document` — method, line 64
- **called from:**
- `routes/personal_routes.py:381`
- `services/docs/service.py:113`
- `src/rag_manager.py:66`
- `src/rag_vector.py:540`
- `tests/test_embedding_lanes_rag.py:26`

## `RAGManager.add_documents_batch` — method, line 68
- **called from:**
- `src/rag_manager.py:70`
- `tests/test_embedding_lanes_rag.py:47`
- `tests/test_embedding_lanes_rag.py:69`
