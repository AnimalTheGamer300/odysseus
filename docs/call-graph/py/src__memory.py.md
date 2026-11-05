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
- `src/memory.py:375`
- `src/memory.py:400`
- `src/personal_docs.py:149`
- `src/personal_docs.py:158`

## `get_text_similarity` — function, line 29
- **called from:**
- `src/memory.py:356`

## `MemoryManager` — class, line 47
- **called from:**
- `mcp_servers/memory_server.py:104`
- `scripts/odysseus_domain_audit.py:339`
- `scripts/odysseus_domain_audit.py:370`
- `services/memory/service.py:43`
- `src/app_initializer.py:90`
- `src/builtin_actions.py:598`
- `tests/test_manage_memory_blank_id.py:18`
- `tests/test_manage_memory_blank_id.py:44`
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
- `tests/test_memory_relevance_ranking.py:9`
- `tests/test_memory_store_unreadable_no_wipe.py:44`
- `tests/test_memory_validate_entries_nondict.py:9`

## `MemoryManager.__init__` — method, line 48
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

## `MemoryManager.extract_memory_from_chat` — method, line 52
- **called from:**
- `routes/memory/memory_routes.py:288`
- `tests/test_memory_bullet_extraction.py:31`
- `tests/test_memory_extract_chat_nondict.py:14`

## `MemoryManager.process_inline_memory_command` — method, line 99
- **called from:**
- `src/chat_handler.py:357`

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
- `scripts/odysseus_domain_audit.py:340`
- `scripts/odysseus_domain_audit.py:371`
- `services/memory/builtin_skills.py:45`
- `services/memory/service.py:113`
- `services/memory/service.py:118`
- `services/memory/skills.py:346`
- `services/memory/skills.py:398`
- `services/memory/skills.py:474`
- `services/memory/skills.py:773`
- `src/ai_interaction.py:477`
- `src/ai_interaction.py:510`
- `src/builtin_actions.py:599`
- `src/memory.py:191`
- `tests/test_builtin_skills.py:76`
- `tests/test_builtin_skills.py:77`
- `tests/test_builtin_skills.py:78`
- `tests/test_builtin_skills.py:79`
- `tests/test_manage_memory_blank_id.py:30`
- `tests/test_manage_memory_blank_id.py:56`
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
- `services/memory/memory_extractor.py:736`
- `services/memory/memory_extractor.py:1121`
- `src/ai_interaction.py:445`
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
- `app.py:1335`
- `app.py:1390`
- `companion/pairing.py:168`
- `core/auth.py:136`
- `core/auth.py:159`
- `core/database.py:1682`
- `core/database.py:1740`
- `core/database.py:1758`
- `routes/backup_routes.py:26`
- `routes/backup_routes.py:32`
- `routes/email/email_routes.py:4999`
- `routes/mcp/mcp_routes.py:471`
- `routes/mcp/mcp_routes.py:587`
- `routes/memory/memory_routes.py:89`
- `routes/memory/memory_routes.py:121`
- `routes/memory/memory_routes.py:152`
- `routes/memory/memory_routes.py:158`
- `routes/memory/memory_routes.py:174`
- `routes/memory/memory_routes.py:217`
- `routes/memory/memory_routes.py:527`
- `routes/prefs_routes.py:20`
- `routes/session_routes.py:89`
- `routes/skills_routes.py:318`
- `routes/skills_routes.py:338`
- `routes/skills_routes.py:566`
- `routes/skills_routes.py:577`
- `routes/skills_routes.py:612`
- `routes/skills_routes.py:667`
- `routes/skills_routes.py:721`
- `routes/skills_routes.py:784`
- `routes/skills_routes.py:831`
- `routes/skills_routes.py:854`
- `routes/skills_routes.py:871`
- `scripts/add_hwfit_models.py:243`
- `scripts/add_hwfit_models.py:445`
- `scripts/agent_migration_manifest.py:73`
- `scripts/analyze_odysseus_eval_targets.py:14`
- `scripts/audit_c5_benchmark_evidence.py:1377`
- `scripts/backfill_model_release_dates.py:70`
- `scripts/claim_ownerless.py:53`
- `scripts/dump_agent_prompt.py:388`
- `scripts/dump_agent_prompt.py:421`
- `scripts/import_from_vllm_recipes.py:262`
- `scripts/migrate_faiss_to_chroma.py:32`
- `scripts/pr_blocker_audit.py:157`
- `scripts/summarize_odysseus_eval_delta.py:57`
- `services/hwfit/hf_discovery.py:304`
- `services/hwfit/hf_discovery.py:326`
- `services/hwfit/models.py:273`
- `services/memory/memory_extractor.py:58`
- `services/memory/memory_extractor.py:96`
- `services/memory/memory_extractor.py:992`
- `services/memory/skill_extractor.py:263`
- `services/memory/skills.py:114`
- `services/memory/skills.py:309`
- `services/memory/skills.py:705`
- `services/search/analytics.py:75`
- `services/search/content.py:307`
- `services/search/core.py:869`
- `services/skills/audit_workflow.py:62`
- … +135 more (grep the name in repo)

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
- `routes/auth_routes.py:285`
- `routes/backup_routes.py:107`
- `routes/backup_routes.py:191`
- `routes/gallery/gallery_routes.py:346`
- `routes/gallery/gallery_routes.py:378`
- `routes/gallery/gallery_routes.py:380`
- `routes/gallery/gallery_routes.py:394`
- `routes/gallery/gallery_routes.py:1054`
- `routes/gallery/gallery_routes.py:1866`
- `routes/gallery/gallery_routes.py:1869`
- `routes/gallery/gallery_routes.py:1914`
- `routes/gallery/gallery_routes.py:1986`
- `routes/gallery/gallery_routes.py:2515`
- `routes/gallery/gallery_routes.py:2566`
- `routes/gallery/gallery_routes.py:2616`
- `routes/gallery/gallery_routes.py:2925`
- `routes/gallery/gallery_routes.py:2976`
- `routes/gallery/gallery_routes.py:2990`
- `routes/memory/memory_routes.py:137`
- `routes/memory/memory_routes.py:518`
- `routes/memory/memory_routes.py:547`
- `routes/memory/memory_routes.py:569`
- `routes/upload_routes.py:524`
- `scripts/diffusion_server.py:253`
- `scripts/diffusion_server.py:1075`
- `scripts/diffusion_server.py:1170`
- `scripts/diffusion_server.py:1181`
- `scripts/diffusion_server.py:1407`
- `scripts/diffusion_server.py:1454`
- `scripts/mlx_image_server.py:181`
- `scripts/mlx_image_server.py:200`
- `scripts/mlx_image_server.py:318`
- `scripts/odysseus_domain_audit.py:343`
- `scripts/odysseus_domain_audit.py:371`
- `services/memory/memory_extractor.py:856`
- `services/memory/memory_extractor.py:1138`
- `services/memory/service.py:123`
- `src/agent_tools/editor_tools.py:307`
- `src/agent_tools/editor_tools.py:569`
- `src/agent_tools/media_tools.py:396`
- `src/agent_tools/media_tools.py:495`
- `src/agent_tools/media_tools.py:881`
- `src/agent_tools/media_tools.py:1004`
- `src/agent_tools/media_tools.py:1526`
- `src/agent_tools/media_tools.py:1537`
- `src/agent_tools/media_tools.py:1738`
- `src/agent_tools/media_tools.py:1847`
- `src/ai_interaction.py:450`
- `src/ai_interaction.py:491`
- `src/ai_interaction.py:525`
- `src/builtin_actions.py:858`
- `src/caldav_writeback.py:156`
- `src/chat_handler.py:365`
- `src/clean_agent_preview.py:5463`
- `src/document_processor.py:152`
- `src/document_processor.py:491`
- … +184 more (grep the name in repo)

## `MemoryManager.add_entry` — method, line 280
- **called from:**
- `mcp_servers/memory_server.py:185`
- `routes/memory/memory_routes.py:132`
- `scripts/odysseus_domain_audit.py:342`
- `services/memory/memory_extractor.py:827`
- `src/ai_interaction.py:439`
- `src/chat_handler.py:363`
- `src/memory_provider.py:149`
- `tests/test_mcp_memory_owner_scope.py:27`
- `tests/test_memory_extractor_vector_degraded.py:106`
- `tests/test_memory_imports.py:50`
- `tests/test_memory_owner_isolation.py:9`
- `tests/test_memory_owner_isolation.py:10`
- `tests/test_memory_store_unreadable_no_wipe.py:114`

## `MemoryManager.increment_uses` — method, line 297
- **called from:**
- `src/chat_processor.py:388`
- `tests/test_memory_store_unreadable_no_wipe.py:151`

## `MemoryManager.find_duplicates` — method, line 317
- **called from:**
- `routes/memory/memory_routes.py:122`
- `services/memory/memory_extractor.py:820`
- `src/chat_handler.py:362`

## `MemoryManager.categorize_memory_by_relevance` — method, line 325
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `MemoryManager.get_relevant_memories` — method, line 361
- **called from:**
- `mcp_servers/memory_server.py:261`
- `routes/memory/memory_routes.py:90`
- `routes/memory/memory_routes.py:166`
- `src/ai_interaction.py:555`
- `src/memory_provider.py:204`
- `tests/test_memory_relevance_ranking.py:16`
- `tests/test_memory_relevance_ranking.py:27`
- `tests/test_memory_relevance_ranking.py:33`
- `tests/test_memory_relevance_ranking.py:39`
- `tests/test_memory_relevance_ranking.py:40`
- `tests/test_memory_relevance_ranking.py:45`
- `tests/test_memory_relevance_ranking.py:50`
- `tests/test_memory_relevance_ranking.py:51`
- `tests/test_memory_relevance_ranking.py:52`
