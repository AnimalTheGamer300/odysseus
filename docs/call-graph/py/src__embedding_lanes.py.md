# `src/embedding_lanes.py` — definitions & call sites

20 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `EmbeddingLane` — class, line 24
- decorator: `dataclass`
- **called from:**
- `src/embedding_lanes.py:240`
- `tests/test_embedding_lanes_memory.py:62`
- `tests/test_embedding_lanes_memory.py:72`
- `tests/test_embedding_lanes_memory.py:148`
- `tests/test_embedding_lanes_rag.py:141`
- `tests/test_embedding_lanes_rag.py:194`
- `tests/test_embedding_lanes_rag.py:231`
- `tests/test_embedding_lanes_tool_index.py:37`
- `tests/test_embedding_lanes_tool_index.py:47`
- `tests/test_embedding_lanes_tool_index.py:90`
- `tests/test_embedding_lanes_tool_index.py:100`
- `tests/test_embedding_lanes_tool_index.py:152`
- `tests/test_embedding_lanes_tool_index.py:162`

## `EmbeddingLane.healthy` — method, line 35
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EmbeddingLane.encode` — method, line 38
- **called from:**
- `app.py:474`
- `app.py:474`
- `companion/pairing.py:192`
- `core/auth.py:92`
- `core/auth.py:96`
- `core/auth.py:96`
- `integrations/claude/skills/odysseus/scripts/odysseus_api.py:200`
- `integrations/codex/scripts/odysseus_api.py:200`
- `mcp_servers/email_server.py:48`
- `mcp_servers/email_server.py:802`
- `mcp_servers/email_server.py:1296`
- `mcp_servers/email_server.py:3542`
- `mcp_servers/email_server.py:3545`
- `routes/api_token_routes.py:131`
- `routes/auth_routes.py:356`
- `routes/contacts/contacts_routes.py:378`
- `routes/contacts/contacts_routes.py:542`
- `routes/contacts/contacts_routes.py:631`
- `routes/contacts/contacts_routes.py:806`
- `routes/cookbook_routes.py:1335`
- `routes/document/document_routes.py:1994`
- `routes/editor_draft_routes.py:123`
- `routes/email/email_helpers.py:69`
- `routes/email/email_helpers.py:83`
- `routes/email/email_helpers.py:84`
- `routes/email/email_helpers.py:96`
- `routes/email/email_helpers.py:98`
- `routes/email/email_helpers.py:708`
- `routes/email/email_pollers.py:822`
- `routes/email/email_pollers.py:834`
- `routes/email/email_routes.py:567`
- `routes/email/email_routes.py:576`
- `routes/email/email_routes.py:600`
- `routes/email/email_routes.py:833`
- `routes/email/email_routes.py:2070`
- `routes/email/email_routes.py:2185`
- `routes/email/email_routes.py:2529`
- `routes/email/email_routes.py:2620`
- `routes/email/email_routes.py:3793`
- `routes/email/email_routes.py:4132`
- `routes/email/email_routes.py:4286`
- `routes/email/email_routes.py:4303`
- `routes/email/email_routes.py:4436`
- `routes/email/email_routes.py:4468`
- `routes/email/email_routes.py:4597`
- `routes/email/email_routes.py:4679`
- `routes/email/email_routes.py:5181`
- `routes/email/email_routes.py:5733`
- `routes/model_routes.py:1487`
- `routes/note/note_routes.py:463`
- `routes/note/note_routes.py:487`
- `routes/vault/vault_routes.py:120`
- `scripts/agent_migration_manifest.py:51`
- `scripts/agent_migration_manifest.py:68`
- `scripts/audit_c5_benchmark_evidence.py:102`
- `scripts/audit_c5_benchmark_evidence.py:1244`
- `scripts/audit_c5_benchmark_evidence.py:1418`
- `scripts/audit_email_sft_with_deepseek.py:34`
- `scripts/audit_email_sft_with_deepseek.py:222`
- `scripts/audit_sft_corpus_with_deepseek.py:48`
- … +261 more (grep the name in repo)

## `EmbeddingLane.count` — method, line 42
- **called from:**
- `core/database.py:3027`
- `core/database.py:3028`
- `core/database.py:3029`
- `core/database.py:3030`
- `core/database.py:3031`
- `core/session_manager.py:149`
- `core/session_manager.py:863`
- `routes/admin_wipe/admin_wipe_routes.py:79`
- `routes/admin_wipe/admin_wipe_routes.py:90`
- `routes/admin_wipe/admin_wipe_routes.py:127`
- `routes/admin_wipe/admin_wipe_routes.py:135`
- `routes/admin_wipe/admin_wipe_routes.py:143`
- `routes/admin_wipe/admin_wipe_routes.py:149`
- `routes/admin_wipe/admin_wipe_routes.py:149`
- `routes/admin_wipe/admin_wipe_routes.py:161`
- `routes/chat_helpers.py:540`
- `routes/cookbook_routes.py:3354`
- `routes/cookbook_routes.py:3355`
- `routes/document/document_routes.py:543`
- `routes/document/document_routes.py:553`
- `routes/document/document_routes.py:594`
- `routes/email/email_routes.py:7477`
- `routes/gallery/gallery_routes.py:1265`
- `routes/gallery/gallery_routes.py:1268`
- `routes/gallery/gallery_routes.py:1336`
- `routes/gallery/gallery_routes.py:1393`
- `routes/gallery/gallery_routes.py:1395`
- `routes/gallery/gallery_routes.py:1396`
- `routes/gallery/gallery_routes.py:1423`
- `routes/history/history_routes.py:425`
- `routes/session_routes.py:957`
- `routes/session_routes.py:1009`
- `routes/session_routes.py:1143`
- `routes/session_routes.py:1472`
- `routes/task/task_routes.py:1049`
- `scripts/build_odysseus_everyday_deepseek_heldout_v3_cases.py:258`
- `scripts/eval_odysseus_tool_use.py:1238`
- `scripts/run_sft_overnight_fixture_flows.py:281`
- `scripts/run_sft_overnight_fixture_flows.py:622`
- `src/agent_loop.py:10697`
- `src/agent_loop.py:14503`
- `src/agent_loop.py:19520`
- `src/agent_loop.py:19520`
- `src/agent_loop.py:19520`
- `src/agent_loop.py:26493`
- `src/agent_loop.py:30737`
- `src/agent_tools/document_tools.py:740`
- `src/agent_tools/document_tools.py:892`
- `src/agent_tools/document_tools.py:1030`
- `src/agent_tools/filesystem_tools.py:201`
- `src/agent_tools/filesystem_tools.py:271`
- `src/agent_tools/filesystem_tools.py:773`
- `src/agent_tools/filesystem_tools.py:778`
- `src/agent_tools/interaction_tools.py:86`
- `src/agent_tools/interaction_tools.py:86`
- `src/agent_tools/interaction_tools.py:87`
- `src/agent_tools/media_tools.py:994`
- `src/agent_tools/web_tools.py:518`
- `src/agent_tools/web_tools_prewave3.py:522`
- `src/app_initializer.py:109`
- … +315 more (grep the name in repo)

## `EmbeddingLane.stats` — method, line 48
- **called from:**
- `src/memory_vector.py:250`
- `src/rag_vector.py:484`
- `src/tool_index.py:748`

## `reset_embedding_lane_state` — function, line 61
- **called from:**
- `routes/embedding_routes.py:316`
- `routes/embedding_routes.py:357`

## `collection_name` — function, line 70
- **called from:**
- `src/embedding_lanes.py:237`
- `src/memory_vector.py:96`
- `src/memory_vector.py:199`
- `src/memory_vector.py:200`
- `src/rag_vector.py:170`
- `src/rag_vector.py:454`
- `src/rag_vector.py:455`

## `_fingerprint` — function, line 74
- **called from:**
- `src/embedding_lanes.py:236`

## `_metadata` — function, line 79
- **called from:**
- `src/agent_tools/web_tools.py:2034`
- `src/agent_tools/web_tools_prewave3.py:2038`
- `src/embedding_lanes.py:238`

## `_load_custom_endpoint` — function, line 90
- **called from:**
- `routes/embedding_routes.py:247`
- `tests/test_embedding_endpoint_config.py:11`
- `tests/test_embedding_endpoint_config.py:22`

## `_build_fastembed_client` — function, line 114
- **called from:**
- `src/embedding_lanes.py:267`

## `_build_custom_client` — function, line 122
- **called from:**
- `src/embedding_lanes.py:260`
- `tests/test_embedding_lanes.py:261`
- `tests/test_embedding_lanes.py:290`
- `tests/test_embedding_lanes.py:292`

## `_encode_with_client` — function, line 131
- **called from:**
- `src/embedding_lanes.py:178`

## `_get_or_reset_collection` — function, line 136
- **called from:**
- `src/embedding_lanes.py:239`

## `_create_lane` — function, line 232
- **called from:**
- `src/embedding_lanes.py:262`
- `src/embedding_lanes.py:268`

## `build_embedding_lanes` — function, line 252
- **called from:**
- `src/memory_vector.py:40`
- `src/memory_vector.py:209`
- `src/rag_vector.py:94`
- `src/rag_vector.py:463`
- `src/tool_index.py:218`
- `tests/test_embedding_lane_ndarray_restore.py:60`
- `tests/test_embedding_lanes.py:33`
- `tests/test_embedding_lanes.py:74`
- `tests/test_embedding_lanes.py:110`
- `tests/test_embedding_lanes.py:143`
- `tests/test_embedding_lanes.py:183`
- `tests/test_embedding_lanes.py:218`
- `tests/test_embedding_lanes.py:239`

## `migrate_legacy_collection` — function, line 275
- **called from:**
- `src/memory_vector.py:49`
- `src/rag_vector.py:102`
- `src/tool_index.py:226`

## `lane_count` — function, line 339
- **called from:**
- `src/memory_vector.py:72`
- `src/rag_vector.py:106`
- `src/rag_vector.py:353`
- `src/rag_vector.py:480`

## `dedupe_results` — function, line 343
- **called from:**
- `src/memory_vector.py:163`
- `src/rag_vector.py:397`
- `src/rag_vector.py:436`
- `src/tool_index.py:403`

## `query_lanes` — function, line 357
- **called from:**
- `src/rag_vector.py:361`
