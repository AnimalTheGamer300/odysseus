# `src/embeddings.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `EmbeddingClient` — class, line 42
- **called from:**
- `src/embeddings.py:262`
- `tests/test_embeddings.py:25`
- `tests/test_embeddings.py:42`
- `tests/test_embeddings_client.py:31`
- `tests/test_embeddings_client.py:51`
- `tests/test_embeddings_client.py:68`
- `tests/test_embeddings_client.py:83`

## `EmbeddingClient.__init__` — method, line 45
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

## `EmbeddingClient.get_sentence_embedding_dimension` — method, line 61
- **called from:**
- `src/embedding_lanes.py:118`
- `src/embedding_lanes.py:233`
- `src/embeddings.py:263`
- `src/embeddings.py:273`

## `EmbeddingClient.encode` — method, line 71
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

## `EmbeddingClient._embed_batch` — method, line 95
- **called from:**
- `src/embeddings.py:81`
- `src/embeddings.py:105`

## `EmbeddingClient._post_embeddings` — method, line 117
- **called from:**
- `src/embeddings.py:97`
- `src/embeddings.py:114`

## `FastEmbedClient` — class, line 132
- **called from:**
- `src/embedding_lanes.py:117`
- `src/embeddings.py:272`

## `FastEmbedClient.__init__` — method, line 135
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

## `FastEmbedClient.get_sentence_embedding_dimension` — method, line 186
- **called from:**
- `src/embedding_lanes.py:118`
- `src/embedding_lanes.py:233`
- `src/embeddings.py:263`
- `src/embeddings.py:273`

## `FastEmbedClient.encode` — method, line 194
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

## `_load_persisted_endpoint` — function, line 214
- **called from:**
- `src/embedding_lanes.py:93`
- `src/embeddings.py:246`

## `reset_http_embed_state` — function, line 231
- **called from:**
- `routes/embedding_routes.py:311`
- `routes/embedding_routes.py:352`
- `src/embedding_lanes.py:65`
- `tests/test_embedding_lanes.py:249`
- `tests/test_embedding_lanes.py:265`
- `tests/test_embedding_lanes.py:272`
- `tests/test_embedding_lanes.py:295`

## `get_embedding_client` — function, line 241
- **called from:**
- `scripts/migrate_faiss_to_chroma.py:87`
- `scripts/migrate_faiss_to_chroma.py:140`
- `src/embedding_lanes.py:125`
