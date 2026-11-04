# `src/preset_manager.py` — definitions & call sites

12 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `PresetManager` — class, line 8
- **called from:**
- `src/app_initializer.py:99`
- `tests/test_preset_atomic_save.py:26`
- `tests/test_preset_atomic_save.py:39`
- `tests/test_preset_atomic_save.py:42`
- `tests/test_preset_fill_missing_defaults.py:33`
- `tests/test_preset_fill_missing_defaults.py:63`
- `tests/test_preset_fill_missing_defaults.py:76`
- `tests/test_preset_store_shape.py:9`
- `tests/test_review_regressions.py:262`
- `tests/test_review_regressions.py:278`
- `tests/test_review_regressions.py:284`
- `tests/test_review_regressions.py:308`

## `PresetManager.__init__` — method, line 67
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

## `PresetManager.load` — method, line 71
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

## `PresetManager.save` — method, line 115
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

## `PresetManager.get` — method, line 130
- **called from:**
- `app.py:359`
- `app.py:383`
- `app.py:389`
- `app.py:416`
- `app.py:428`
- `app.py:470`
- `app.py:538`
- `app.py:512`
- `app.py:595`
- `app.py:891`
- `app.py:903`
- `app.py:907`
- `app.py:915`
- `app.py:919`
- `app.py:923`
- `app.py:927`
- `app.py:931`
- `app.py:935`
- `app.py:939`
- `app.py:944`
- `app.py:950`
- `app.py:955`
- `app.py:967`
- `app.py:968`
- `app.py:969`
- `app.py:969`
- `app.py:971`
- `app.py:971`
- `app.py:975`
- `app.py:996`
- `app.py:987`
- `app.py:998`
- `app.py:1117`
- `app.py:1151`
- `app.py:1165`
- `app.py:1198`
- `app.py:1201`
- `app.py:1216`
- `companion/pairing.py:116`
- `companion/pairing.py:126`
- `companion/pairing.py:173`
- `companion/pairing.py:177`
- `companion/routes.py:85`
- `companion/routes.py:97`
- `companion/routes.py:109`
- `companion/routes.py:168`
- `companion/routes.py:222`
- `core/auth.py:143`
- `core/auth.py:164`
- `core/auth.py:187`
- `core/auth.py:214`
- `core/auth.py:226`
- `core/auth.py:230`
- `core/auth.py:299`
- `core/auth.py:299`
- `core/auth.py:325`
- `core/auth.py:349`
- `core/auth.py:349`
- `core/auth.py:357`
- `core/auth.py:370`
- … +7551 more (grep the name in repo)

## `PresetManager.update_custom` — method, line 134
- **called from:**
- `routes/preset_routes.py:36`
- `tests/test_review_regressions.py:264`

## `PresetManager.get_all` — method, line 157
- **called from:**
- `routes/backup_routes.py:29`
- `routes/backup_routes.py:185`
- `tests/test_memory_imports.py:35`
- `tests/test_memory_imports.py:43`

## `PresetManager.get_user_templates` — method, line 161
- **called from:**
- `routes/preset_routes.py:54`

## `PresetManager.save_user_template` — method, line 165
- **called from:**
- `routes/preset_routes.py:61`

## `PresetManager.delete_user_template` — method, line 177
- **called from:**
- `routes/preset_routes.py:68`

## `PresetManager.get_group_presets` — method, line 183
- **called from:**
- `routes/preset_routes.py:117`

## `PresetManager.save_group_presets` — method, line 187
- **called from:**
- `routes/preset_routes.py:123`
