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
- `app.py:433`
- `app.py:433`
- `companion/pairing.py:192`
- `core/auth.py:74`
- `core/auth.py:78`
- `core/auth.py:78`
- `integrations/claude/skills/odysseus/scripts/odysseus_api.py:200`
- `integrations/codex/scripts/odysseus_api.py:200`
- `mcp_servers/email_server.py:42`
- `mcp_servers/email_server.py:690`
- `routes/api_token_routes.py:131`
- `routes/contacts/contacts_routes.py:307`
- `routes/contacts/contacts_routes.py:428`
- `routes/contacts/contacts_routes.py:517`
- `routes/contacts/contacts_routes.py:682`
- `routes/document/document_routes.py:1770`
- `routes/email_helpers.py:65`
- `routes/email_helpers.py:79`
- `routes/email_helpers.py:80`
- `routes/email_helpers.py:92`
- `routes/email_helpers.py:94`
- `routes/email_helpers.py:579`
- `routes/email_pollers.py:686`
- `routes/email_pollers.py:698`
- `routes/email_routes.py:500`
- `routes/email_routes.py:510`
- `routes/email_routes.py:711`
- `routes/email_routes.py:1762`
- `routes/email_routes.py:1996`
- `routes/email_routes.py:2061`
- `routes/email_routes.py:2554`
- `routes/email_routes.py:2982`
- `routes/email_routes.py:4099`
- `routes/model_routes.py:1375`
- `routes/note/note_routes.py:460`
- `routes/note/note_routes.py:484`
- `routes/vault/vault_routes.py:106`
- `scripts/agent_migration_manifest.py:51`
- `scripts/agent_migration_manifest.py:68`
- `scripts/demo_email/seed_demo_emails.py:66`
- `scripts/demo_email/seed_demo_emails.py:129`
- `scripts/migrate_faiss_to_chroma.py:111`
- `scripts/migrate_faiss_to_chroma.py:155`
- `scripts/migrate_searxng_settings.py:77`
- `scripts/migrate_searxng_settings.py:108`
- `services/hwfit/hardware.py:548`
- `services/memory/memory_extractor.py:43`
- `services/memory/skill_importer.py:408`
- `services/memory/skill_importer.py:419`
- `services/memory/skill_importer.py:428`
- `services/search/cache.py:37`
- `services/tts/tts_service.py:85`
- `src/agent_loop.py:2672`
- `src/agent_tools/admin_tools.py:467`
- `src/api_key_manager.py:41`
- `src/api_key_manager.py:48`
- `src/caldav_sync.py:150`
- `src/chatgpt_subscription.py:241`
- `src/embedding_lanes.py:39`
- `src/embedding_lanes.py:76`
- … +69 more (grep the name in repo)

## `EmbeddingLane.count` — method, line 42
- **called from:**
- `core/database.py:2713`
- `core/database.py:2714`
- `core/database.py:2715`
- `core/database.py:2716`
- `core/database.py:2717`
- `core/session_manager.py:150`
- `core/session_manager.py:971`
- `core/session_manager.py:973`
- `routes/admin_wipe/admin_wipe_routes.py:79`
- `routes/admin_wipe/admin_wipe_routes.py:90`
- `routes/admin_wipe/admin_wipe_routes.py:127`
- `routes/admin_wipe/admin_wipe_routes.py:135`
- `routes/admin_wipe/admin_wipe_routes.py:143`
- `routes/admin_wipe/admin_wipe_routes.py:149`
- `routes/admin_wipe/admin_wipe_routes.py:149`
- `routes/admin_wipe/admin_wipe_routes.py:161`
- `routes/chat_helpers.py:253`
- `routes/cookbook_routes.py:3475`
- `routes/cookbook_routes.py:3476`
- `routes/document/document_routes.py:354`
- `routes/document/document_routes.py:364`
- `routes/document/document_routes.py:404`
- `routes/email_routes.py:5693`
- `routes/gallery/gallery_routes.py:755`
- `routes/gallery/gallery_routes.py:758`
- `routes/gallery/gallery_routes.py:826`
- `routes/gallery/gallery_routes.py:883`
- `routes/gallery/gallery_routes.py:885`
- `routes/gallery/gallery_routes.py:886`
- `routes/gallery/gallery_routes.py:913`
- `routes/history/history_routes.py:287`
- `routes/session_routes.py:808`
- `routes/session_routes.py:998`
- `routes/session_routes.py:1319`
- `routes/session_routes.py:1321`
- `routes/task/task_routes.py:977`
- `src/agent_loop.py:5958`
- `src/agent_loop.py:5968`
- `src/agent_tools/filesystem_tools.py:208`
- `src/agent_tools/filesystem_tools.py:235`
- `src/agent_tools/filesystem_tools.py:504`
- `src/agent_tools/filesystem_tools.py:509`
- `src/agent_tools/interaction_tools.py:86`
- `src/agent_tools/interaction_tools.py:86`
- `src/agent_tools/interaction_tools.py:87`
- `src/app_initializer.py:109`
- `src/builtin_actions.py:882`
- `src/builtin_actions.py:970`
- `src/chat_helpers.py:33`
- `src/chat_helpers.py:33`
- `src/cleanup_service.py:133`
- `src/email_thread_parser.py:276`
- `src/embedding_lanes.py:44`
- `src/embedding_lanes.py:56`
- `src/embedding_lanes.py:340`
- `src/embedding_lanes.py:370`
- `src/llm_core.py:405`
- `src/llm_core.py:417`
- `src/memory_vector.py:53`
- `src/memory_vector.py:139`
- … +140 more (grep the name in repo)

## `EmbeddingLane.stats` — method, line 48
- **called from:**
- `src/memory_vector.py:250`
- `src/rag_vector.py:484`

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
- `src/tool_index.py:161`
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
- `src/tool_index.py:169`

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
- `src/tool_index.py:341`

## `query_lanes` — function, line 357
- **called from:**
- `src/rag_vector.py:361`
