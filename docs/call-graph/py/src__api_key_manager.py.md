# `src/api_key_manager.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `APIKeyManager` — class, line 11
- **called from:**
- `src/app_initializer.py:98`
- `tests/test_api_key_file_permissions.py:30`
- `tests/test_api_key_file_permissions.py:37`
- `tests/test_api_key_file_permissions.py:48`
- `tests/test_api_key_manager_atomic_save.py:11`
- `tests/test_api_key_manager_atomic_save.py:27`
- `tests/test_api_key_manager_atomic_save.py:38`
- `tests/test_api_key_manager_atomic_save.py:54`
- `tests/test_api_key_manager_corrupt_load.py:12`
- `tests/test_api_key_manager_resilience.py:7`
- `tests/test_api_key_manager_resilience.py:39`

## `APIKeyManager.__init__` — method, line 12
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

## `APIKeyManager.get_or_create_key` — method, line 17
- **called from:**
- `src/api_key_manager.py:40`
- `src/api_key_manager.py:47`
- `tests/test_api_key_file_permissions.py:31`
- `tests/test_api_key_file_permissions.py:42`

## `APIKeyManager.encrypt_api_key` — method, line 36
- **called from:**
- `routes/webhook/webhook_routes.py:120`
- `src/api_key_manager.py:89`
- `tests/test_api_key_file_permissions.py:49`

## `APIKeyManager.decrypt_api_key` — method, line 43
- **called from:**
- `src/api_key_manager.py:111`
- `src/webhook_manager.py:354`
- `tests/test_api_key_file_permissions.py:51`

## `APIKeyManager._load_raw` — method, line 50
- **called from:**
- `src/api_key_manager.py:88`
- `src/api_key_manager.py:107`

## `APIKeyManager.save` — method, line 77
- **called from:**
- `companion/pairing.py:224`
- `mcp_servers/memory_server.py:187`
- `mcp_servers/memory_server.py:215`
- `mcp_servers/memory_server.py:243`
- `routes/auth_routes.py:261`
- `routes/backup_routes.py:107`
- `routes/backup_routes.py:191`
- `routes/gallery/gallery_routes.py:54`
- `routes/gallery/gallery_routes.py:548`
- `routes/gallery/gallery_routes.py:1337`
- `routes/gallery/gallery_routes.py:1340`
- `routes/gallery/gallery_routes.py:1410`
- `routes/gallery/gallery_routes.py:1443`
- `routes/gallery/gallery_routes.py:1445`
- `routes/gallery/gallery_routes.py:1733`
- `routes/gallery/gallery_routes.py:1782`
- `routes/gallery/gallery_routes.py:1830`
- `routes/gallery/gallery_routes.py:2052`
- `routes/gallery/gallery_routes.py:2102`
- `routes/gallery/gallery_routes.py:2116`
- `routes/memory/memory_routes.py:137`
- `routes/memory/memory_routes.py:511`
- `routes/memory/memory_routes.py:540`
- `routes/memory/memory_routes.py:562`
- `routes/upload_routes.py:401`
- `scripts/diffusion_server.py:253`
- `scripts/diffusion_server.py:1075`
- `scripts/diffusion_server.py:1170`
- `scripts/diffusion_server.py:1181`
- `scripts/diffusion_server.py:1407`
- `scripts/diffusion_server.py:1454`
- `scripts/mlx_image_server.py:181`
- `scripts/mlx_image_server.py:200`
- `scripts/mlx_image_server.py:318`
- `services/memory/memory_extractor.py:652`
- `services/memory/memory_extractor.py:841`
- `services/memory/service.py:123`
- `src/ai_interaction.py:401`
- `src/ai_interaction.py:440`
- `src/ai_interaction.py:472`
- `src/builtin_actions.py:730`
- `src/caldav_writeback.py:156`
- `src/chat_handler.py:349`
- `src/document_processor.py:141`
- `src/document_processor.py:385`
- `src/document_processor.py:509`
- `src/memory.py:212`
- `src/memory.py:255`
- `src/memory.py:315`
- `src/memory_provider.py:166`
- `src/memory_provider.py:249`
- `src/pdf_forms.py:253`
- `src/pdf_forms.py:362`
- `src/pdf_forms.py:398`
- `src/preset_manager.py:74`
- `src/preset_manager.py:97`
- `src/preset_manager.py:109`
- `src/preset_manager.py:155`
- `src/preset_manager.py:175`
- `src/preset_manager.py:181`
- … +85 more (grep the name in repo)

## `APIKeyManager.load` — method, line 105
- **called from:**
- `app.py:1151`
- `app.py:1198`
- `companion/pairing.py:168`
- `core/auth.py:118`
- `core/auth.py:141`
- `core/database.py:1430`
- `core/database.py:1488`
- `core/database.py:1506`
- `routes/backup_routes.py:26`
- `routes/backup_routes.py:32`
- `routes/mcp/mcp_routes.py:446`
- `routes/mcp/mcp_routes.py:540`
- `routes/memory/memory_routes.py:89`
- `routes/memory/memory_routes.py:121`
- `routes/memory/memory_routes.py:152`
- `routes/memory/memory_routes.py:158`
- `routes/memory/memory_routes.py:174`
- `routes/memory/memory_routes.py:217`
- `routes/memory/memory_routes.py:520`
- `routes/prefs_routes.py:20`
- `routes/skills_routes.py:609`
- `routes/skills_routes.py:692`
- `routes/skills_routes.py:884`
- `routes/skills_routes.py:930`
- `routes/skills_routes.py:973`
- `routes/skills_routes.py:994`
- `routes/skills_routes.py:1020`
- `routes/skills_routes.py:1062`
- `routes/skills_routes.py:1077`
- `routes/skills_routes.py:1161`
- `routes/skills_routes.py:1209`
- `routes/skills_routes.py:1229`
- `routes/skills_routes.py:1457`
- `routes/skills_routes.py:1468`
- `routes/skills_routes.py:1494`
- `routes/skills_routes.py:1568`
- `routes/skills_routes.py:1686`
- `routes/skills_routes.py:1733`
- `routes/skills_routes.py:1812`
- `routes/skills_routes.py:1859`
- `routes/skills_routes.py:1878`
- `routes/skills_routes.py:1895`
- `scripts/add_hwfit_models.py:190`
- `scripts/add_hwfit_models.py:365`
- `scripts/agent_migration_manifest.py:73`
- `scripts/backfill_model_release_dates.py:67`
- `scripts/claim_ownerless.py:53`
- `scripts/dump_agent_prompt.py:388`
- `scripts/dump_agent_prompt.py:421`
- `scripts/import_from_vllm_recipes.py:257`
- `scripts/migrate_faiss_to_chroma.py:32`
- `scripts/pr_blocker_audit.py:157`
- `services/hwfit/hf_discovery.py:286`
- `services/hwfit/hf_discovery.py:308`
- `services/hwfit/models.py:273`
- `services/memory/memory_extractor.py:57`
- `services/memory/memory_extractor.py:95`
- `services/memory/memory_extractor.py:699`
- `services/memory/skill_extractor.py:257`
- `services/memory/skills.py:93`
- … +79 more (grep the name in repo)
