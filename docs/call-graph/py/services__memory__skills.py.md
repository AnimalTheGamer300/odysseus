# `services/memory/skills.py` — definitions & call sites

29 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_tokenize` — function, line 37
- **called from:**
- `services/memory/skills.py:330`
- `services/memory/skills.py:337`
- `services/memory/skills.py:691`
- `services/memory/skills.py:701`
- `services/memory/skills.py:705`

## `_jaccard` — function, line 41
- **called from:**
- `services/memory/skills.py:342`
- `services/memory/skills.py:701`

## `_to_float` — function, line 47
- **called from:**
- `services/memory/skills.py:682`
- `services/memory/skills.py:686`
- `services/memory/skills.py:710`

## `SkillsManager` — class, line 62
- **called from:**
- `src/agent_loop.py:3072`
- `src/agent_loop.py:3383`
- `src/agent_loop.py:4551`
- `src/app_initializer.py:91`
- `src/builtin_actions.py:1927`
- `src/builtin_actions.py:2056`
- `src/tools/system.py:55`
- `tests/test_skill_frontmatter_escape_roundtrip.py:201`
- `tests/test_skill_index_toolset_gating.py:68`
- `tests/test_skill_index_toolset_gating.py:78`
- `tests/test_skill_index_toolset_gating.py:91`
- `tests/test_skill_save_no_rename.py:102`
- `tests/test_skills_delete_owner.py:55`
- `tests/test_skills_delete_owner.py:80`
- `tests/test_skills_manager_owner_isolation.py:100`
- `tests/test_skills_manager_owner_isolation.py:200`
- `tests/test_skills_manager_owner_isolation.py:235`
- `tests/test_skills_manager_owner_isolation.py:252`
- `tests/test_skills_manager_owner_isolation.py:289`
- `tests/test_skills_routes_owner_update.py:83`
- `tests/test_skills_routes_owner_update.py:107`
- `tests/test_skills_routes_owner_update.py:150`
- `tests/test_skills_tag_token_match.py:24`
- `tests/test_skills_tag_token_match.py:33`

## `SkillsManager.__init__` — method, line 65
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

## `SkillsManager._skill_dir` — method, line 76
- **called from:**
- `services/memory/skills.py:82`
- `services/memory/skills.py:410`

## `SkillsManager._skill_file` — method, line 81
- **called from:**
- `services/memory/skills.py:176`
- `services/memory/skills.py:428`
- `services/memory/skills.py:429`
- `services/memory/skills.py:486`

## `SkillsManager._load_usage` — method, line 88
- **called from:**
- `services/memory/skills.py:128`
- `services/memory/skills.py:145`
- `services/memory/skills.py:219`
- `services/memory/skills.py:496`
- `services/memory/skills.py:524`
- `services/memory/skills.py:533`

## `SkillsManager._save_usage` — method, line 98
- **called from:**
- `services/memory/skills.py:138`
- `services/memory/skills.py:153`
- `services/memory/skills.py:500`
- `services/memory/skills.py:528`
- `services/memory/skills.py:538`

## `SkillsManager._usage_key` — method, line 109
- decorator: `staticmethod`
- **called from:**
- `services/memory/skills.py:115`
- `services/memory/skills.py:129`
- `services/memory/skills.py:146`
- `services/memory/skills.py:497`
- `services/memory/skills.py:499`
- `services/memory/skills.py:525`
- `services/memory/skills.py:534`

## `SkillsManager._usage_entry` — method, line 114
- **called from:**
- `services/memory/skills.py:227`

## `SkillsManager.set_audit` — method, line 121
- **called from:**
- `routes/skills_routes.py:532`
- `routes/skills_routes.py:904`
- `routes/skills_routes.py:946`
- `routes/skills_routes.py:972`
- `routes/skills_routes.py:978`
- `routes/skills_routes.py:993`
- `routes/skills_routes.py:1017`
- `routes/skills_routes.py:1030`
- `src/builtin_actions.py:2007`
- `tests/test_skills_manager_owner_isolation.py:291`

## `SkillsManager.set_necessity` — method, line 140
- **called from:**
- `routes/skills_routes.py:627`
- `routes/skills_routes.py:699`
- `routes/skills_routes.py:890`
- `routes/skills_routes.py:906`
- `routes/skills_routes.py:908`
- `tests/test_skills_manager_owner_isolation.py:292`

## `SkillsManager._iter_skill_files` — method, line 159
- **called from:**
- `services/memory/skills.py:196`
- `services/memory/skills.py:222`
- `services/memory/skills.py:447`
- `services/memory/skills.py:506`
- `services/memory/skills.py:545`
- `services/memory/skills.py:561`

## `SkillsManager._read_skill` — method, line 166
- **called from:**
- `services/memory/skills.py:197`
- `services/memory/skills.py:223`
- `services/memory/skills.py:448`
- `services/memory/skills.py:507`
- `services/memory/skills.py:546`
- `services/memory/skills.py:562`

## `SkillsManager._write_skill` — method, line 175
- **called from:**
- `services/memory/skills.py:207`
- `services/memory/skills.py:380`
- `services/memory/skills.py:501`

## `SkillsManager.backfill_owner` — method, line 183
- **called from:**
- `app.py:1207`

## `SkillsManager.load_all` — method, line 217
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

## `SkillsManager.load` — method, line 278
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

## `SkillsManager.add_skill` — method, line 293
- **called from:**
- `routes/backup_routes.py:150`
- `routes/skills_routes.py:1383`
- `services/memory/skill_extractor.py:276`
- `src/tools/system.py:118`
- `tests/test_skill_frontmatter_escape_roundtrip.py:202`
- `tests/test_skills_manager_owner_isolation.py:253`
- `tests/test_skills_manager_owner_isolation.py:262`

## `SkillsManager.import_bundle_from_files` — method, line 384
- **called from:**
- `routes/skills_routes.py:1362`

## `SkillsManager.update_skill` — method, line 432
- **called from:**
- `routes/skills_routes.py:538`
- `routes/skills_routes.py:708`
- `routes/skills_routes.py:724`
- `routes/skills_routes.py:865`
- `routes/skills_routes.py:903`
- `routes/skills_routes.py:1027`
- `routes/skills_routes.py:1827`
- `routes/skills_routes.py:1868`
- `src/tools/system.py:177`
- `src/tools/system.py:201`
- `src/tools/system.py:214`
- `tests/test_skill_frontmatter_escape_roundtrip.py:205`
- `tests/test_skills_manager_owner_isolation.py:110`
- `tests/test_skills_manager_owner_isolation.py:237`

## `SkillsManager.delete_skill` — method, line 505
- **called from:**
- `routes/skills_routes.py:1883`
- `src/tools/system.py:220`
- `tests/test_skills_delete_owner.py:58`
- `tests/test_skills_delete_owner.py:62`

## `SkillsManager.record_use` — method, line 532
- **called from:**
- `routes/skills_routes.py:1440`
- `services/memory/skills.py:347`
- `src/agent_loop.py:3107`
- `tests/test_skills_manager_owner_isolation.py:290`

## `SkillsManager.read_skill_md` — method, line 544
- **called from:**
- `routes/skills_routes.py:869`
- `routes/skills_routes.py:1436`
- `routes/skills_routes.py:1473`
- `routes/skills_routes.py:1500`
- `src/builtin_actions.py:1979`
- `src/tools/system.py:80`
- `src/tools/system.py:187`
- `tests/test_skills_manager_owner_isolation.py:202`
- `tests/test_skills_manager_owner_isolation.py:206`
- `tests/test_skills_manager_owner_isolation.py:210`
- `tests/test_skills_manager_owner_isolation.py:215`

## `SkillsManager.read_skill_reference` — method, line 558
- **called from:**
- `src/tools/system.py:91`
- `tests/test_skills_manager_owner_isolation.py:216`
- `tests/test_skills_manager_owner_isolation.py:217`

## `SkillsManager.index_for` — method, line 584
- **called from:**
- `routes/skills_routes.py:1218`
- `routes/skills_routes.py:1231`
- `routes/skills_routes.py:1428`
- `src/agent_loop.py:3385`
- `src/chat_processor.py:522`
- `tests/test_skill_index_toolset_gating.py:71`
- `tests/test_skill_index_toolset_gating.py:72`
- `tests/test_skill_index_toolset_gating.py:81`
- `tests/test_skill_index_toolset_gating.py:82`
- `tests/test_skill_index_toolset_gating.py:85`
- `tests/test_skill_index_toolset_gating.py:95`
- `tests/test_skill_index_toolset_gating.py:96`
- `tests/test_skill_index_toolset_gating.py:98`

## `SkillsManager.get_relevant_skills` — method, line 645
- **called from:**
- `routes/skills_routes.py:1896`
- `src/agent_loop.py:3093`
- `src/agent_loop.py:4561`
- `src/tools/system.py:227`
- `tests/test_skills_tag_token_match.py:28`
- `tests/test_skills_tag_token_match.py:35`

## `SkillsManager._passes` — method, line 669
- **called from:**
- `services/memory/skills.py:687`
