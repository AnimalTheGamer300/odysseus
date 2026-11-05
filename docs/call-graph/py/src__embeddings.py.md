# `src/embeddings.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `EmbeddingClient` — class, line 42
- **called from:**
- `src/embeddings.py:277`
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

## `EmbeddingClient.get_sentence_embedding_dimension` — method, line 61
- **called from:**
- `src/embedding_lanes.py:118`
- `src/embedding_lanes.py:233`
- `src/embeddings.py:278`
- `src/embeddings.py:288`

## `EmbeddingClient.encode` — method, line 71
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
- `src/embeddings.py:287`
- `tests/test_embeddings_thread_limit.py:27`
- `tests/test_embeddings_thread_limit.py:37`
- `tests/test_embeddings_thread_limit.py:51`

## `FastEmbedClient.__init__` — method, line 135
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

## `FastEmbedClient.get_sentence_embedding_dimension` — method, line 201
- **called from:**
- `src/embedding_lanes.py:118`
- `src/embedding_lanes.py:233`
- `src/embeddings.py:278`
- `src/embeddings.py:288`

## `FastEmbedClient.encode` — method, line 209
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

## `_load_persisted_endpoint` — function, line 229
- **called from:**
- `src/embedding_lanes.py:93`
- `src/embeddings.py:261`

## `reset_http_embed_state` — function, line 246
- **called from:**
- `routes/embedding_routes.py:311`
- `routes/embedding_routes.py:352`
- `src/embedding_lanes.py:65`
- `tests/test_embedding_lanes.py:249`
- `tests/test_embedding_lanes.py:265`
- `tests/test_embedding_lanes.py:272`
- `tests/test_embedding_lanes.py:295`

## `get_embedding_client` — function, line 256
- **called from:**
- `scripts/migrate_faiss_to_chroma.py:87`
- `scripts/migrate_faiss_to_chroma.py:140`
- `src/embedding_lanes.py:125`
