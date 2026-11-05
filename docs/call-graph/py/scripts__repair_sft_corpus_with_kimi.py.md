# `scripts/repair_sft_corpus_with_kimi.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `decrypt` — function, line 23
- **called from:**
- `core/database.py:186`
- `routes/calendar_routes.py:994`
- `routes/calendar_routes.py:1047`
- `routes/calendar_routes.py:1150`
- `routes/contacts/contacts_routes.py:56`
- `routes/cookbook_helpers.py:106`
- `routes/cookbook_routes.py:457`
- `scripts/audit_email_sft_with_deepseek.py:34`
- `scripts/audit_sft_corpus_with_deepseek.py:48`
- `scripts/odysseus_conversation_qa.py:294`
- `scripts/repair_email_sft_with_kimi.py:31`
- `scripts/repair_sft_corpus_with_kimi.py:27`
- `scripts/repair_sft_corpus_with_kimi.py:47`
- `src/api_key_manager.py:48`
- `src/caldav_sync.py:637`
- `src/caldav_writeback.py:290`
- `src/email_attachment_text.py:16`
- `src/embedding_lanes.py:106`
- `src/embeddings.py:272`
- `src/integrations.py:188`
- `src/secret_storage.py:77`
- `tests/test_security_regressions.py:62`
- `tests/test_security_regressions.py:68`
- `tests/test_security_regressions.py:84`
- `tests/test_security_regressions.py:100`

## `endpoint` — function, line 30
- **called from:**
- `scripts/generate_sft_environment_expansion.py:313`
- `scripts/generate_sft_flow_variants_with_kimi.py:160`
- `scripts/judge_seeded_harness_replay.py:159`
- `scripts/repair_email_sft_with_kimi.py:199`
- `scripts/repair_sft_corpus_with_kimi.py:195`
- `tests/test_api_token_tool_authority.py:578`
- `tests/test_auth_policy.py:96`
- `tests/test_auth_policy.py:107`
- `tests/test_auth_policy.py:157`
- `tests/test_auth_policy.py:172`
- `tests/test_auth_policy.py:191`
- `tests/test_auth_policy.py:203`
- `tests/test_auth_policy.py:215`
- `tests/test_auth_policy.py:268`
- `tests/test_auth_policy.py:283`
- `tests/test_auth_policy.py:301`
- `tests/test_auth_session_revocation.py:83`
- `tests/test_auth_session_revocation.py:177`
- `tests/test_auth_session_revocation.py:195`
- `tests/test_auth_session_revocation.py:215`
- `tests/test_auth_username_policy.py:35`
- `tests/test_auth_username_policy.py:49`
- `tests/test_backup_import_cross_user_dedup.py:51`
- `tests/test_backup_import_cross_user_dedup.py:60`
- `tests/test_backup_import_skills.py:54`
- `tests/test_backup_import_skills.py:88`
- `tests/test_chat_route_tool_policy.py:325`
- `tests/test_codeql_python_residual_closure.py:430`
- `tests/test_codeql_python_residual_closure.py:473`
- `tests/test_codeql_python_residual_followup.py:198`
- `tests/test_codeql_python_residual_followup.py:254`
- `tests/test_codeql_python_residual_followup.py:255`
- `tests/test_codeql_python_residual_security.py:32`
- `tests/test_codeql_python_residual_security.py:66`
- `tests/test_codeql_python_residual_security.py:152`
- `tests/test_codex_ssh_host_validation.py:138`
- `tests/test_codex_ssh_host_validation.py:151`
- `tests/test_codex_ssh_host_validation.py:162`
- `tests/test_codex_ssh_host_validation.py:173`
- `tests/test_codex_ssh_host_validation.py:184`
- `tests/test_codex_ssh_host_validation.py:194`
- `tests/test_codex_ssh_host_validation.py:220`
- `tests/test_codex_ssh_host_validation.py:239`
- `tests/test_context_resolution_route.py:143`
- `tests/test_context_resolution_route.py:229`
- `tests/test_context_resolution_route.py:465`
- `tests/test_cookbook_dependency_completion_regression.py:1113`
- `tests/test_cookbook_dependency_completion_regression.py:1338`
- `tests/test_cookbook_remote_windows_diffusers.py:53`
- `tests/test_document_library_literal_search.py:47`
- `tests/test_document_library_literal_search.py:50`
- `tests/test_document_library_literal_search.py:71`
- `tests/test_editor_generation_model_routing.py:112`
- `tests/test_editor_model_discovery.py:83`
- `tests/test_editor_model_discovery.py:121`
- `tests/test_editor_model_discovery.py:146`
- `tests/test_editor_model_discovery.py:215`
- `tests/test_editor_model_discovery.py:242`
- `tests/test_editor_model_discovery.py:277`
- `tests/test_editor_model_discovery.py:300`
- … +200 more (grep the name in repo)

## `parse_json` — function, line 51
- **called from:**
- `scripts/generate_sft_environment_expansion.py:190`
- `scripts/generate_sft_flow_variants_with_kimi.py:105`
- `scripts/judge_seeded_harness_replay.py:110`
- `scripts/repair_sft_corpus_with_kimi.py:131`

## `compact_turn` — function, line 60
- **called from:**
- `scripts/odysseus_conversation_qa.py:801`
- `scripts/repair_sft_corpus_with_kimi.py:108`
- `tests/test_odysseus_conversation_qa.py:33`

## `clip` — function, line 61
- **called from:**
- `scripts/audit_sft_corpus_with_deepseek.py:137`
- `scripts/audit_sft_corpus_with_deepseek.py:138`
- `scripts/audit_sft_corpus_with_deepseek.py:139`
- `scripts/audit_sft_corpus_with_deepseek.py:144`
- `scripts/audit_sft_corpus_with_deepseek.py:145`
- `scripts/build_sft_environment_inventories.py:42`
- `scripts/build_sft_environment_inventories.py:43`
- `scripts/build_sft_environment_inventories.py:80`
- `scripts/build_sft_environment_inventories.py:80`
- `scripts/build_sft_environment_inventories.py:81`
- `scripts/build_sft_environment_inventories.py:82`
- `scripts/build_sft_environment_inventories.py:82`
- `scripts/build_sft_environment_inventories.py:83`
- `scripts/build_sft_environment_inventories.py:85`
- `scripts/build_sft_environment_inventories.py:86`
- `scripts/diffusion_server.py:1247`
- `scripts/diffusion_server.py:1286`
- `scripts/repair_sft_corpus_with_kimi.py:67`
- `scripts/repair_sft_corpus_with_kimi.py:68`
- `scripts/repair_sft_corpus_with_kimi.py:69`
- `scripts/repair_sft_corpus_with_kimi.py:73`
- `scripts/repair_sft_corpus_with_kimi.py:74`
- `static/js/editor/layer-styles.js:80`
- `static/js/editor/layer-styles.js:93`
- `static/js/editor/layer-styles.js:99`
- `static/js/editor/tools/crop.js:179`
- `static/js/galleryEditor.js:4126`

## `repair_prompt` — function, line 82
- **called from:**
- `scripts/repair_sft_corpus_with_kimi.py:117`

## `call_kimi` — function, line 114
- **called from:**
- `scripts/repair_email_sft_with_kimi.py:217`
- `scripts/repair_sft_corpus_with_kimi.py:203`

## `validate_and_apply` — function, line 134
- **called from:**
- `scripts/repair_sft_corpus_with_kimi.py:204`

## `main` — function, line 176
- **called from:**
- `integrations/claude/skills/odysseus/scripts/odysseus_api.py:218`
- `integrations/codex/scripts/odysseus_api.py:218`
- `scripts/add_hwfit_models.py:512`
- `scripts/agent_migration_manifest.py:635`
- `scripts/analyze_odysseus_eval_targets.py:180`
- `scripts/assemble_sft_clean_corpus.py:74`
- `scripts/audit_c5_benchmark_evidence.py:1637`
- `scripts/audit_email_sft_with_deepseek.py:323`
- `scripts/audit_historical_tool_routing.py:121`
- `scripts/audit_sft_corpus_with_deepseek.py:344`
- `scripts/audit_typo_tool_routing.py:99`
- `scripts/backfill_model_release_dates.py:136`
- `scripts/build_frontend.py:148`
- `scripts/build_historical_harness_queue.py:333`
- `scripts/build_odysseus_everyday_deepseek_heldout_cases.py:274`
- `scripts/build_odysseus_everyday_deepseek_heldout_v3_cases.py:353`
- `scripts/build_odysseus_realistic_web_synthesis_rows.py:361`
- `scripts/build_odysseus_search_teacher_edited_rows.py:267`
- `scripts/build_odysseus_sft_repair_manifest.py:230`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:447`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:557`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:519`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:551`
- `scripts/build_odysseus_v61_app_route_web_rows.py:394`
- `scripts/build_odysseus_v62_teacher_trace_web_rows.py:288`
- `scripts/build_odysseus_web_teacher_sft.py:500`
- `scripts/build_odysseus_web_v53_repair_sft.py:483`
- `scripts/build_sft_environment_inventories.py:97`
- `scripts/build_sft_expansion_manifest.py:161`
- `scripts/build_sft_expansion_splits.py:110`
- `scripts/build_v66_calendar_heldout_cases.py:113`
- `scripts/check_brotli.py:122`
- `scripts/check_ca_trust.py:180`
- `scripts/claim_ownerless.py:106`
- `scripts/cook_sft_alex_conversations.py:298`
- `scripts/css_snapshot.py:295`
- `scripts/curate_public_search_seed_cases.py:324`
- `scripts/curate_sft_trace_run.py:178`
- `scripts/demo_email/seed_demo_emails.py:394`
- `scripts/dump_agent_prompt.py:545`
- `scripts/eval_ajax_basic_tools.py:71`
- `scripts/eval_exact_file_routing.py:202`
- `scripts/eval_followup_domain_continuity.py:209`
- `scripts/eval_odysseus_app_route_smoke.py:400`
- `scripts/eval_odysseus_contextual_tool_use.py:944`
- `scripts/eval_odysseus_crud.py:925`
- `scripts/eval_odysseus_everyday_live_hard.py:590`
- `scripts/eval_odysseus_live_hard_direct.py:261`
- `scripts/eval_odysseus_live_hard_examples.py:468`
- `scripts/eval_odysseus_tool_use.py:1490`
- `scripts/eval_qwen35_document_shape_direct.py:303`
- `scripts/eval_qwen35_implicit_memory.py:279`
- `scripts/eval_qwen35_tool_router_extended.py:571`
- `scripts/filter_sft_seed_hygiene.py:90`
- `scripts/generate_env_reference.py:1270`
- `scripts/generate_sft_environment_expansion.py:399`
- `scripts/generate_sft_flow_variants_with_kimi.py:211`
- `scripts/hf_download.py:182`
- `scripts/import_from_vllm_recipes.py:348`
- `scripts/index_documents.py:117`
- … +139 more (grep the name in repo)

## `process` — function, line 198
- **called from:**
- `tests/test_process_resource_identity.py:23`
- `tests/test_process_resource_identity.py:28`
- `tests/test_process_resource_identity.py:35`
- `tests/test_process_resource_identity.py:47`
- `tests/test_process_resource_identity.py:67`
- `tests/test_process_resource_identity.py:73`
- `static/js/cookbookServe.js:3086`
- `static/js/cookbookServe.js:3134`
- `static/js/cookbookServe.js:3157`
- `static/js/cookbookServe.js:3160`
