# `scripts/build_odysseus_tool_efficiency_sft_slice.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `stable_id` — function, line 79
- **called from:**
- `scripts/agent_migration_manifest.py:140`
- `scripts/agent_migration_manifest.py:329`
- `scripts/agent_migration_manifest.py:391`
- `scripts/agent_migration_manifest.py:486`
- `scripts/build_odysseus_realistic_web_synthesis_rows.py:272`
- `scripts/build_odysseus_search_teacher_edited_rows.py:199`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:157`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:248`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:290`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:346`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:391`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:359`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:358`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:364`
- `scripts/build_odysseus_v61_app_route_web_rows.py:183`
- `scripts/build_odysseus_v61_app_route_web_rows.py:231`
- `scripts/build_odysseus_v62_teacher_trace_web_rows.py:117`
- `scripts/build_odysseus_v62_teacher_trace_web_rows.py:189`
- `scripts/build_odysseus_web_teacher_sft.py:319`
- `scripts/build_odysseus_web_v53_repair_sft.py:345`
- `scripts/curate_public_search_seed_cases.py:82`
- `scripts/curate_public_search_seed_cases.py:148`
- `scripts/run_odysseus_search_teacher_pipeline.py:556`

## `tool_call` — function, line 84
- **called from:**
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:141`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:198`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:203`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:208`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:274`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:324`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:309`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:310`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:321`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:333`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:378`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:388`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:389`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:375`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:395`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:396`
- `scripts/build_odysseus_web_teacher_sft.py:275`
- `scripts/build_odysseus_web_teacher_sft.py:276`
- `scripts/build_odysseus_web_teacher_sft.py:297`
- `scripts/build_odysseus_web_v53_repair_sft.py:266`
- `scripts/build_odysseus_web_v53_repair_sft.py:296`
- `scripts/build_odysseus_web_v53_repair_sft.py:297`
- `scripts/build_odysseus_web_v53_repair_sft.py:321`
- `tests/test_clean_agent_preview.py:5581`
- `tests/test_clean_agent_preview.py:5582`
- `tests/test_clean_agent_preview.py:5583`

## `memory_rows` — function, line 95
- **called from:**
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:418`

## `memory_crud_rows` — function, line 162
- **called from:**
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:418`

## `task_rows` — function, line 253
- **called from:**
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:418`

## `web_followup_rows` — function, line 295
- **called from:**
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:418`

## `no_tool_rows` — function, line 351
- **called from:**
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:418`

## `split_rows` — function, line 396
- **called from:**
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:419`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:495`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:461`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:483`
- `scripts/build_odysseus_v61_app_route_web_rows.py:358`
- `scripts/build_odysseus_v62_teacher_trace_web_rows.py:252`
- `scripts/build_odysseus_web_teacher_sft.py:435`
- `scripts/build_odysseus_web_v53_repair_sft.py:424`

## `write_jsonl` — function, line 404
- **called from:**
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:421`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:422`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:423`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:497`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:498`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:499`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:464`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:465`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:466`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:486`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:487`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:488`
- `scripts/build_odysseus_web_teacher_sft.py:437`
- `scripts/build_odysseus_web_teacher_sft.py:438`
- `scripts/build_odysseus_web_teacher_sft.py:439`
- `scripts/build_odysseus_web_v53_repair_sft.py:427`
- `scripts/build_odysseus_web_v53_repair_sft.py:428`
- `scripts/build_odysseus_web_v53_repair_sft.py:429`
- `scripts/curate_sft_trace_run.py:169`
- `scripts/run_sft_overnight_fixture_flows.py:706`
- `scripts/run_sft_overnight_fixture_flows.py:708`
- `tests/test_agent_trace.py:42`
- `tests/test_curate_sft_trace_run.py:102`

## `main` — function, line 409
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
