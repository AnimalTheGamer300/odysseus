# `src/memory.py` — definitions & call sites

21 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `MemoryStoreUnreadable` — class, line 14
- **called from:**
- `src/memory.py:141`
- `src/memory.py:156`
- `src/memory.py:161`

## `tokenize` — function, line 25
- **called from:**
- `src/memory.py:34`
- `src/memory.py:35`
- `src/memory.py:414`
- `src/memory.py:415`
- `src/personal_docs.py:145`
- `src/personal_docs.py:154`

## `get_text_similarity` — function, line 29
- **called from:**
- `src/memory.py:356`

## `MemoryManager` — class, line 47
- **called from:**
- `mcp_servers/memory_server.py:104`
- `services/memory/service.py:43`
- `src/app_initializer.py:90`
- `src/builtin_actions.py:474`
- `tests/test_mcp_memory_owner_scope.py:42`
- `tests/test_mcp_memory_owner_scope.py:99`
- `tests/test_mcp_memory_owner_scope.py:121`
- `tests/test_memory_extract_chat_nondict.py:7`
- `tests/test_memory_extractor_vector_degraded.py:69`
- `tests/test_memory_extractor_vector_degraded.py:103`
- `tests/test_memory_imports.py:49`
- `tests/test_memory_owner_isolation.py:8`
- `tests/test_memory_provider.py:32`
- `tests/test_memory_provider.py:58`
- `tests/test_memory_provider.py:80`
- `tests/test_memory_provider.py:100`
- `tests/test_memory_store_unreadable_no_wipe.py:44`
- `tests/test_memory_validate_entries_nondict.py:9`

## `MemoryManager.__init__` — method, line 48
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

## `MemoryManager.extract_memory_from_chat` — method, line 52
- **called from:**
- `routes/memory/memory_routes.py:285`
- `tests/test_memory_bullet_extraction.py:31`
- `tests/test_memory_extract_chat_nondict.py:14`

## `MemoryManager.process_inline_memory_command` — method, line 99
- **called from:**
- `src/chat_handler.py:341`

## `MemoryManager.ensure_file_exists` — method, line 119
- **called from:**
- `src/memory.py:50`

## `MemoryManager._read_entries` — method, line 125
- **called from:**
- `src/memory.py:175`
- `src/memory.py:187`

## `MemoryManager.load_all` — method, line 166
- **called from:**
- `mcp_servers/memory_server.py:74`
- `routes/backup_routes.py:112`
- `services/memory/service.py:113`
- `services/memory/service.py:118`
- `services/memory/skills.py:279`
- `services/memory/skills.py:327`
- `services/memory/skills.py:403`
- `services/memory/skills.py:654`
- `src/ai_interaction.py:426`
- `src/ai_interaction.py:457`
- `src/builtin_actions.py:475`
- `src/memory.py:191`
- `tests/test_mcp_memory_owner_scope.py:75`
- `tests/test_mcp_memory_owner_scope.py:88`
- `tests/test_mcp_memory_owner_scope.py:95`
- `tests/test_mcp_memory_owner_scope.py:104`
- `tests/test_mcp_memory_owner_scope.py:117`
- `tests/test_mcp_memory_owner_scope.py:136`
- `tests/test_mcp_memory_owner_scope.py:146`
- `tests/test_mcp_memory_owner_scope.py:150`
- `tests/test_memory_imports.py:55`
- `tests/test_memory_store_unreadable_no_wipe.py:105`
- `tests/test_memory_store_unreadable_no_wipe.py:125`
- `tests/test_memory_store_unreadable_no_wipe.py:144`
- `tests/test_memory_store_unreadable_no_wipe.py:152`
- `tests/test_memory_store_unreadable_no_wipe.py:160`
- `tests/test_skill_frontmatter_escape_roundtrip.py:207`

## `MemoryManager.load_all_for_update` — method, line 180
- **called from:**
- `mcp_servers/memory_server.py:70`
- `routes/backup_routes.py:83`
- `routes/memory/memory_routes.py:46`
- `services/memory/memory_extractor.py:573`
- `services/memory/memory_extractor.py:824`
- `src/ai_interaction.py:396`
- `src/memory.py:199`
- `src/memory.py:304`
- `src/memory_provider.py:164`
- `src/memory_provider.py:233`
- `tests/test_memory_store_unreadable_no_wipe.py:67`
- `tests/test_memory_store_unreadable_no_wipe.py:75`
- `tests/test_memory_store_unreadable_no_wipe.py:84`
- `tests/test_memory_store_unreadable_no_wipe.py:89`
- `tests/test_memory_store_unreadable_no_wipe.py:96`
- `tests/test_memory_store_unreadable_no_wipe.py:119`
- `tests/test_memory_store_unreadable_no_wipe.py:140`
- `tests/test_memory_store_unreadable_no_wipe.py:254`

## `MemoryManager.load` — method, line 189
- **called from:**
- `app.py:1151`
- `app.py:1198`
- `companion/pairing.py:168`
- `core/auth.py:118`
- `core/auth.py:141`
- `core/database.py:1468`
- `core/database.py:1526`
- `core/database.py:1544`
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
- … +80 more (grep the name in repo)

## `MemoryManager.claim_ownerless` — method, line 196
- **called from:**
- `tests/test_memory_imports.py:53`
- `tests/test_memory_store_unreadable_no_wipe.py:159`

## `MemoryManager._validate_entries` — method, line 215
- **called from:**
- `src/memory.py:164`
- `tests/test_memory_validate_entries_nondict.py:10`

## `MemoryManager._migrate_from_legacy` — method, line 234
- **called from:**
- `src/memory.py:153`

## `MemoryManager.save` — method, line 261
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
- … +87 more (grep the name in repo)

## `MemoryManager.add_entry` — method, line 280
- **called from:**
- `mcp_servers/memory_server.py:185`
- `routes/memory/memory_routes.py:132`
- `services/memory/memory_extractor.py:626`
- `src/ai_interaction.py:390`
- `src/chat_handler.py:347`
- `src/memory_provider.py:149`
- `tests/test_mcp_memory_owner_scope.py:27`
- `tests/test_memory_extractor_vector_degraded.py:106`
- `tests/test_memory_imports.py:50`
- `tests/test_memory_owner_isolation.py:9`
- `tests/test_memory_owner_isolation.py:10`
- `tests/test_memory_store_unreadable_no_wipe.py:114`

## `MemoryManager.increment_uses` — method, line 297
- **called from:**
- `src/chat_processor.py:370`
- `tests/test_memory_store_unreadable_no_wipe.py:151`

## `MemoryManager.find_duplicates` — method, line 317
- **called from:**
- `routes/memory/memory_routes.py:122`
- `services/memory/memory_extractor.py:619`
- `src/chat_handler.py:346`

## `MemoryManager.categorize_memory_by_relevance` — method, line 325
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `MemoryManager.get_relevant_memories` — method, line 361
- **called from:**
- `mcp_servers/memory_server.py:261`
- `routes/memory/memory_routes.py:90`
- `routes/memory/memory_routes.py:166`
- `src/ai_interaction.py:493`
- `src/memory_provider.py:204`
