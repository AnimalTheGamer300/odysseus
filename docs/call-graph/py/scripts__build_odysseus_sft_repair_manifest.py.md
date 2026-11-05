# `scripts/build_odysseus_sft_repair_manifest.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `source_seed_id` — function, line 21
- **called from:**
- `scripts/build_odysseus_sft_repair_manifest.py:129`
- `scripts/odysseus_conversation_qa.py:478`
- `scripts/odysseus_conversation_qa.py:585`
- `scripts/odysseus_conversation_qa.py:632`
- `scripts/odysseus_conversation_qa.py:642`
- `scripts/odysseus_conversation_qa.py:642`
- `scripts/odysseus_conversation_qa.py:648`
- `scripts/odysseus_conversation_qa.py:1442`
- `scripts/odysseus_conversation_qa.py:1515`
- `scripts/odysseus_conversation_qa.py:1516`

## `behavior_category` — function, line 25
- **called from:**
- `scripts/build_odysseus_sft_repair_manifest.py:161`
- `tests/test_build_odysseus_sft_repair_manifest.py:95`

## `has_transport_failure` — function, line 61
- **called from:**
- `scripts/build_odysseus_sft_repair_manifest.py:133`
- `scripts/build_odysseus_sft_repair_manifest.py:149`

## `eligible_failed_turns` — function, line 69
- **called from:**
- `scripts/build_odysseus_sft_repair_manifest.py:151`

## `requires_native_workspace_tool` — function, line 86
- **called from:**
- `scripts/build_odysseus_sft_repair_manifest.py:147`
- `tests/test_build_odysseus_sft_repair_manifest.py:8`

## `build_manifest` — function, line 103
- **called from:**
- `scripts/agent_migration_manifest.py:622`
- `scripts/build_odysseus_sft_repair_manifest.py:213`
- `tests/test_build_odysseus_sft_repair_manifest.py:41`
- `tests/test_build_odysseus_sft_repair_manifest.py:54`
- `tests/test_build_odysseus_sft_repair_manifest.py:66`
- `tests/test_build_odysseus_sft_repair_manifest.py:74`
- `tests/test_build_odysseus_sft_repair_manifest.py:102`
- `tests/test_build_odysseus_sft_repair_manifest.py:112`
- `tests/test_build_odysseus_sft_repair_manifest.py:126`

## `parse_args` — function, line 195
- **called from:**
- `scripts/_lib/cli.py:112`
- `scripts/agent_migration_manifest.py:617`
- `scripts/agent_migration_manifest.py:621`
- `scripts/analyze_odysseus_eval_targets.py:120`
- `scripts/assemble_sft_clean_corpus.py:24`
- `scripts/audit_c5_benchmark_evidence.py:1558`
- `scripts/audit_email_sft_with_deepseek.py:246`
- `scripts/audit_historical_tool_routing.py:60`
- `scripts/audit_sft_corpus_with_deepseek.py:216`
- `scripts/audit_typo_tool_routing.py:60`
- `scripts/backfill_model_release_dates.py:63`
- `scripts/build_frontend.py:134`
- `scripts/build_historical_harness_queue.py:323`
- `scripts/build_odysseus_everyday_deepseek_heldout_cases.py:238`
- `scripts/build_odysseus_everyday_deepseek_heldout_v3_cases.py:309`
- `scripts/build_odysseus_realistic_web_synthesis_rows.py:285`
- `scripts/build_odysseus_search_teacher_edited_rows.py:211`
- `scripts/build_odysseus_sft_repair_manifest.py:208`
- `scripts/build_odysseus_sft_repair_manifest.py:212`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:416`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:427`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:454`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:476`
- `scripts/build_odysseus_v61_app_route_web_rows.py:252`
- `scripts/build_odysseus_v62_teacher_trace_web_rows.py:208`
- `scripts/build_odysseus_web_teacher_sft.py:378`
- `scripts/build_odysseus_web_v53_repair_sft.py:415`
- `scripts/build_sft_environment_inventories.py:54`
- `scripts/build_sft_expansion_manifest.py:74`
- `scripts/build_sft_expansion_splits.py:25`
- `scripts/build_v66_calendar_heldout_cases.py:49`
- `scripts/check_brotli.py:104`
- `scripts/check_ca_trust.py:139`
- `scripts/cook_sft_alex_conversations.py:248`
- `scripts/cook_sft_alex_conversations.py:252`
- `scripts/css_snapshot.py:247`
- `scripts/curate_public_search_seed_cases.py:262`
- `scripts/curate_sft_trace_run.py:157`
- `scripts/demo_email/seed_demo_emails.py:360`
- `scripts/diffusion_server.py:1492`
- `scripts/dump_agent_prompt.py:382`
- `scripts/eval_ajax_basic_tools.py:32`
- `scripts/eval_exact_file_routing.py:202`
- `scripts/eval_followup_domain_continuity.py:209`
- `scripts/eval_odysseus_app_route_smoke.py:360`
- `scripts/eval_odysseus_contextual_tool_use.py:861`
- `scripts/eval_odysseus_crud.py:800`
- `scripts/eval_odysseus_everyday_live_hard.py:586`
- `scripts/eval_odysseus_live_hard_direct.py:67`
- `scripts/eval_odysseus_live_hard_direct.py:232`
- `scripts/eval_odysseus_live_hard_examples.py:464`
- `scripts/eval_odysseus_tool_use.py:1377`
- `scripts/eval_qwen35_document_shape_direct.py:142`
- `scripts/eval_qwen35_document_shape_direct.py:262`
- `scripts/eval_qwen35_implicit_memory.py:206`
- `scripts/eval_qwen35_tool_router_extended.py:450`
- `scripts/eval_qwen_tool_groups_stream.py:226`
- `scripts/filter_sft_seed_hygiene.py:46`
- `scripts/generate_env_reference.py:1230`
- `scripts/generate_sft_environment_expansion.py:307`
- … +30 more (grep the name in repo)

## `main` — function, line 211
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
