# `services/memory/skills.py` — definitions & call sites

32 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_tokenize` — function, line 39
- **called from:**
- `services/memory/skills.py:401`
- `services/memory/skills.py:408`
- `services/memory/skills.py:822`
- `services/memory/skills.py:851`
- `services/memory/skills.py:855`

## `_jaccard` — function, line 43
- **called from:**
- `services/memory/skills.py:413`
- `services/memory/skills.py:851`

## `_to_float` — function, line 49
- **called from:**
- `services/memory/skills.py:722`
- `services/memory/skills.py:816`
- `services/memory/skills.py:864`

## `_approval_policy` — function, line 59
- **called from:**
- `services/memory/skills.py:703`

## `SkillsManager` — class, line 83
- **called from:**
- `scripts/odysseus_domain_audit.py:346`
- `scripts/odysseus_domain_audit.py:374`
- `src/agent_loop.py:10634`
- `src/agent_loop.py:14808`
- `src/agent_loop.py:15263`
- `src/agent_loop.py:15633`
- `src/agent_loop.py:23404`
- `src/app_initializer.py:91`
- `src/builtin_actions.py:2138`
- `src/builtin_actions.py:2271`
- `src/tools/system.py:55`
- `tests/test_builtin_skills.py:73`
- `tests/test_builtin_skills.py:83`
- `tests/test_builtin_skills.py:119`
- `tests/test_builtin_skills.py:127`
- `tests/test_builtin_skills.py:143`
- `tests/test_manage_skills_action_required.py:42`
- `tests/test_skill_frontmatter_escape_roundtrip.py:201`
- `tests/test_skill_index_local_model_gating.py:62`
- `tests/test_skill_index_local_model_gating.py:72`
- `tests/test_skill_index_local_model_gating.py:84`
- `tests/test_skill_index_local_model_gating.py:94`
- `tests/test_skill_index_toolset_gating.py:69`
- `tests/test_skill_index_toolset_gating.py:80`
- `tests/test_skill_index_toolset_gating.py:94`
- `tests/test_skill_index_toolset_gating.py:108`
- `tests/test_skill_index_toolset_gating.py:117`
- `tests/test_skill_index_toolset_gating.py:130`
- `tests/test_skill_index_toolset_gating.py:146`
- `tests/test_skill_rename_collision.py:19`
- `tests/test_skill_rename_collision.py:57`
- `tests/test_skill_save_no_rename.py:102`
- `tests/test_skill_semantic_retrieval.py:59`
- `tests/test_skill_semantic_retrieval.py:75`
- `tests/test_skill_semantic_retrieval.py:88`
- `tests/test_skill_semantic_retrieval.py:113`
- `tests/test_skill_semantic_retrieval.py:132`
- `tests/test_skill_semantic_retrieval.py:152`
- `tests/test_skill_tool_followup_contract.py:17`
- `tests/test_skill_tool_followup_contract.py:30`
- `tests/test_skill_tool_followup_contract.py:41`
- `tests/test_skill_tool_followup_contract.py:52`
- `tests/test_skill_tool_followup_contract.py:67`
- `tests/test_skill_tool_followup_contract.py:86`
- `tests/test_skill_version_preservation.py:51`
- `tests/test_skills_delete_owner.py:55`
- `tests/test_skills_delete_owner.py:80`
- `tests/test_skills_manager_owner_isolation.py:81`
- `tests/test_skills_manager_owner_isolation.py:174`
- `tests/test_skills_manager_owner_isolation.py:209`
- `tests/test_skills_manager_owner_isolation.py:226`
- `tests/test_skills_manager_owner_isolation.py:263`
- `tests/test_skills_manager_owner_isolation.py:311`
- `tests/test_skills_manager_owner_isolation.py:323`
- `tests/test_skills_manager_owner_isolation.py:326`
- `tests/test_skills_manager_owner_isolation.py:327`
- `tests/test_skills_routes_owner_update.py:83`
- `tests/test_skills_routes_owner_update.py:107`
- `tests/test_skills_routes_owner_update.py:150`
- `tests/test_skills_tag_token_match.py:24`
- … +2 more (grep the name in repo)

## `SkillsManager.__init__` — method, line 86
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

## `SkillsManager._skill_dir` — method, line 97
- **called from:**
- `services/memory/skills.py:103`
- `services/memory/skills.py:481`

## `SkillsManager._skill_file` — method, line 102
- **called from:**
- `services/memory/skills.py:224`
- `services/memory/skills.py:499`
- `services/memory/skills.py:500`
- `services/memory/skills.py:573`

## `SkillsManager._load_usage` — method, line 109
- **called from:**
- `services/memory/skills.py:153`
- `services/memory/skills.py:193`
- `services/memory/skills.py:273`
- `services/memory/skills.py:583`
- `services/memory/skills.py:611`
- `services/memory/skills.py:620`

## `SkillsManager._save_usage` — method, line 119
- **called from:**
- `services/memory/skills.py:186`
- `services/memory/skills.py:201`
- `services/memory/skills.py:587`
- `services/memory/skills.py:615`
- `services/memory/skills.py:625`

## `SkillsManager._usage_key` — method, line 130
- decorator: `staticmethod`
- **called from:**
- `services/memory/skills.py:136`
- `services/memory/skills.py:154`
- `services/memory/skills.py:194`
- `services/memory/skills.py:584`
- `services/memory/skills.py:586`
- `services/memory/skills.py:612`
- `services/memory/skills.py:621`

## `SkillsManager._usage_entry` — method, line 135
- **called from:**
- `services/memory/skills.py:281`

## `SkillsManager.set_audit` — method, line 142
- **called from:**
- `services/skills/agent_runner.py:175`
- `services/skills/audit_workflow.py:45`
- `services/skills/audit_workflow.py:181`
- `services/skills/audit_workflow.py:211`
- `services/skills/audit_workflow.py:224`
- `services/skills/audit_workflow.py:251`
- `services/skills/audit_workflow.py:287`
- `services/skills/audit_workflow.py:306`
- `services/skills/audit_workflow.py:361`
- `src/builtin_actions.py:2222`
- `tests/test_skill_index_local_model_gating.py:63`
- `tests/test_skill_index_local_model_gating.py:73`
- `tests/test_skill_index_local_model_gating.py:85`
- `tests/test_skill_index_local_model_gating.py:95`
- `tests/test_skill_index_toolset_gating.py:70`
- `tests/test_skill_index_toolset_gating.py:81`
- `tests/test_skill_index_toolset_gating.py:95`
- `tests/test_skill_index_toolset_gating.py:109`
- `tests/test_skill_index_toolset_gating.py:118`
- `tests/test_skills_manager_owner_isolation.py:265`
- `tests/test_skills_manager_owner_isolation.py:324`
- `tests/test_skills_manager_owner_isolation.py:328`

## `SkillsManager.set_necessity` — method, line 188
- **called from:**
- `services/skills/audit_workflow.py:46`
- `services/skills/audit_workflow.py:71`
- `services/skills/publication.py:90`
- `services/skills/publication.py:313`
- `tests/test_skills_manager_owner_isolation.py:275`

## `SkillsManager._iter_skill_files` — method, line 207
- **called from:**
- `services/memory/skills.py:248`
- `services/memory/skills.py:276`
- `services/memory/skills.py:510`
- `services/memory/skills.py:531`
- `services/memory/skills.py:593`
- `services/memory/skills.py:632`
- `services/memory/skills.py:656`

## `SkillsManager._read_skill` — method, line 214
- **called from:**
- `services/memory/skills.py:249`
- `services/memory/skills.py:277`
- `services/memory/skills.py:511`
- `services/memory/skills.py:532`
- `services/memory/skills.py:594`
- `services/memory/skills.py:633`
- `services/memory/skills.py:657`

## `SkillsManager._write_skill` — method, line 223
- **called from:**
- `services/memory/skills.py:233`
- `services/memory/skills.py:261`
- `services/memory/skills.py:451`
- `services/memory/skills.py:588`

## `SkillsManager.sync_builtin_skill` — method, line 231
- **called from:**
- `services/memory/builtin_skills.py:68`
- `services/memory/builtin_skills.py:72`

## `SkillsManager.backfill_owner` — method, line 235
- **called from:**
- `app.py:1399`
- `tests/test_builtin_skills.py:122`

## `SkillsManager.load_all` — method, line 271
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

## `SkillsManager.load` — method, line 345
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

## `SkillsManager.add_skill` — method, line 364
- **called from:**
- `routes/backup_routes.py:150`
- `routes/skills_routes.py:492`
- `scripts/odysseus_domain_audit.py:348`
- `services/memory/skill_extractor.py:272`
- `src/tools/system.py:114`
- `tests/test_skill_frontmatter_escape_roundtrip.py:202`
- `tests/test_skill_rename_collision.py:20`
- `tests/test_skill_rename_collision.py:22`
- `tests/test_skill_tool_followup_contract.py:18`
- `tests/test_skill_tool_followup_contract.py:30`
- `tests/test_skill_tool_followup_contract.py:41`
- `tests/test_skill_tool_followup_contract.py:52`
- `tests/test_skill_tool_followup_contract.py:67`
- `tests/test_skill_tool_followup_contract.py:86`
- `tests/test_skill_version_preservation.py:52`
- `tests/test_skills_manager_owner_isolation.py:227`
- `tests/test_skills_manager_owner_isolation.py:236`

## `SkillsManager.import_bundle_from_files` — method, line 455
- **called from:**
- `routes/skills_routes.py:471`

## `SkillsManager.has_skill` — method, line 503
- **called from:**
- `routes/skills_routes.py:842`
- `services/memory/skills.py:567`

## `SkillsManager.update_skill` — method, line 516
- **called from:**
- `routes/skills_routes.py:799`
- `routes/skills_routes.py:844`
- `services/skills/agent_runner.py:188`
- `services/skills/audit_workflow.py:28`
- `services/skills/audit_workflow.py:44`
- `services/skills/audit_workflow.py:303`
- `services/skills/publication.py:172`
- `services/skills/publication.py:219`
- `services/skills/publication.py:228`
- `services/skills/publication.py:322`
- `services/skills/publication.py:338`
- `src/tools/system.py:170`
- `src/tools/system.py:183`
- `src/tools/system.py:209`
- `src/tools/system.py:222`
- `tests/test_skill_frontmatter_escape_roundtrip.py:205`
- `tests/test_skill_rename_collision.py:34`
- `tests/test_skill_rename_collision.py:40`
- `tests/test_skill_rename_collision.py:49`
- `tests/test_skill_rename_collision.py:59`
- `tests/test_skill_rename_collision.py:67`
- `tests/test_skill_version_preservation.py:54`
- `tests/test_skills_manager_owner_isolation.py:90`
- `tests/test_skills_manager_owner_isolation.py:211`

## `SkillsManager.delete_skill` — method, line 592
- **called from:**
- `routes/skills_routes.py:859`
- `scripts/odysseus_domain_audit.py:374`
- `src/tools/system.py:229`
- `tests/test_skill_rename_collision.py:42`
- `tests/test_skills_delete_owner.py:58`
- `tests/test_skills_delete_owner.py:62`

## `SkillsManager.record_use` — method, line 619
- **called from:**
- `routes/skills_routes.py:549`
- `services/memory/skills.py:418`
- `src/agent_loop.py:15336`
- `tests/test_skills_manager_owner_isolation.py:264`

## `SkillsManager.read_skill_md` — method, line 631
- **called from:**
- `routes/skills_routes.py:545`
- `routes/skills_routes.py:586`
- `routes/skills_routes.py:618`
- `scripts/odysseus_domain_audit.py:347`
- `services/skills/audit_workflow.py:32`
- `src/builtin_actions.py:2194`
- `src/tools/system.py:82`
- `src/tools/system.py:195`
- `tests/test_skills_audit_services.py:97`
- `tests/test_skills_audit_services.py:120`
- `tests/test_skills_manager_owner_isolation.py:176`
- `tests/test_skills_manager_owner_isolation.py:180`
- `tests/test_skills_manager_owner_isolation.py:184`
- `tests/test_skills_manager_owner_isolation.py:189`

## `SkillsManager.read_skill_reference` — method, line 653
- **called from:**
- `src/tools/system.py:93`
- `tests/test_skills_manager_owner_isolation.py:190`
- `tests/test_skills_manager_owner_isolation.py:191`

## `SkillsManager.index_for` — method, line 687
- **called from:**
- `routes/session_routes.py:85`
- `routes/skills_routes.py:327`
- `routes/skills_routes.py:340`
- `routes/skills_routes.py:537`
- `src/agent_loop.py:15635`
- `src/chat_processor.py:551`
- `tests/test_skill_index_local_model_gating.py:66`
- `tests/test_skill_index_local_model_gating.py:75`
- `tests/test_skill_index_local_model_gating.py:77`
- `tests/test_skill_index_local_model_gating.py:78`
- `tests/test_skill_index_local_model_gating.py:87`
- `tests/test_skill_index_local_model_gating.py:88`
- `tests/test_skill_index_local_model_gating.py:98`
- `tests/test_skill_index_toolset_gating.py:73`
- `tests/test_skill_index_toolset_gating.py:74`
- `tests/test_skill_index_toolset_gating.py:84`
- `tests/test_skill_index_toolset_gating.py:85`
- `tests/test_skill_index_toolset_gating.py:88`
- `tests/test_skill_index_toolset_gating.py:99`
- `tests/test_skill_index_toolset_gating.py:100`
- `tests/test_skill_index_toolset_gating.py:102`
- `tests/test_skill_index_toolset_gating.py:111`
- `tests/test_skill_index_toolset_gating.py:120`
- `tests/test_skill_index_toolset_gating.py:132`

## `SkillsManager.get_relevant_skills` — method, line 761
- **called from:**
- `routes/skills_routes.py:872`
- `src/agent_loop.py:10636`
- `src/agent_loop.py:15295`
- `src/agent_loop.py:23413`
- `src/tools/system.py:236`
- `tests/test_skill_index_toolset_gating.py:133`
- `tests/test_skill_index_toolset_gating.py:150`
- `tests/test_skill_index_toolset_gating.py:152`
- `tests/test_skill_semantic_retrieval.py:65`
- `tests/test_skill_semantic_retrieval.py:81`
- `tests/test_skill_semantic_retrieval.py:82`
- `tests/test_skill_semantic_retrieval.py:97`
- `tests/test_skill_semantic_retrieval.py:102`
- `tests/test_skill_semantic_retrieval.py:122`
- `tests/test_skill_semantic_retrieval.py:138`
- `tests/test_skill_semantic_retrieval.py:142`
- `tests/test_skill_semantic_retrieval.py:156`
- `tests/test_skills_tag_token_match.py:28`
- `tests/test_skills_tag_token_match.py:35`
- `tests/test_skills_tag_token_match.py:46`

## `SkillsManager._passes` — method, line 810
- **called from:**
- `services/memory/skills.py:818`
