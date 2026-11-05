# `scripts/eval_odysseus_live_hard_examples.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_parse_sse` — function, line 122
- **called from:**
- `scripts/eval_odysseus_everyday_live_hard.py:272`
- `scripts/eval_odysseus_live_hard_examples.py:287`

## `_parse_tool_args` — function, line 134
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:138`
- `scripts/eval_odysseus_everyday_live_hard.py:287`
- `scripts/eval_odysseus_live_hard_examples.py:303`
- `src/agent_runtime/owned_resources.py:22`
- `src/agent_tools/admin_tools.py:26`
- `src/agent_tools/admin_tools.py:235`
- `src/agent_tools/admin_tools.py:391`
- `src/agent_tools/admin_tools.py:463`
- `src/agent_tools/admin_tools.py:515`
- `src/agent_tools/document_tools.py:1089`
- `src/tools/calendar.py:113`
- `src/tools/contacts.py:19`
- `src/tools/contacts.py:87`
- `src/tools/cookbook.py:739`
- `src/tools/cookbook.py:809`
- `src/tools/cookbook.py:1317`
- `src/tools/cookbook.py:1344`
- `src/tools/cookbook.py:1497`
- `src/tools/cookbook.py:1519`
- `src/tools/cookbook.py:1620`
- `src/tools/cookbook.py:1847`
- `src/tools/cookbook.py:1952`
- `src/tools/image.py:29`
- `src/tools/image.py:103`
- `src/tools/notes.py:40`
- `src/tools/research.py:25`
- `src/tools/research.py:117`
- `src/tools/system.py:45`
- `src/tools/system.py:355`
- `src/tools/system.py:836`
- `src/tools/vault.py:50`
- `src/tools/vault.py:99`
- `src/tools/vault.py:157`
- `tests/test_admin_tools_registry.py:72`
- `tests/test_admin_tools_registry.py:74`
- `tests/test_admin_tools_registry.py:77`
- `tests/test_admin_tools_registry.py:78`
- `tests/test_admin_tools_registry.py:79`

## `_tool_name_matches` — function, line 146
- **called from:**
- `scripts/eval_odysseus_everyday_live_hard.py:370`
- `scripts/eval_odysseus_everyday_live_hard.py:372`
- `scripts/eval_odysseus_everyday_live_hard.py:377`
- `scripts/eval_odysseus_everyday_live_hard.py:388`
- `scripts/eval_odysseus_everyday_live_hard.py:423`
- `scripts/eval_odysseus_live_hard_examples.py:175`
- `scripts/eval_odysseus_live_hard_examples.py:180`
- `scripts/eval_odysseus_live_hard_examples.py:184`
- `scripts/eval_odysseus_live_hard_examples.py:188`

## `_contains_all_subset` — function, line 158
- **called from:**
- `scripts/eval_odysseus_live_hard_examples.py:193`

## `_score_case` — function, line 167
- **called from:**
- `scripts/eval_odysseus_live_hard_examples.py:364`

## `_run_case` — function (async), line 225
- **called from:**
- `scripts/eval_exact_file_routing.py:169`
- `scripts/eval_exact_file_routing.py:183`
- `scripts/eval_odysseus_live_hard_examples.py:422`

## `_write_markdown` — function, line 370
- **called from:**
- `scripts/eval_odysseus_live_hard_examples.py:442`

## `_amain` — function (async), line 416
- **called from:**
- `scripts/eval_odysseus_live_hard_examples.py:464`

## `main` — function, line 447
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
