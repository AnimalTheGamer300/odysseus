# `scripts/odysseus_related_flow_audit.py` — definitions & call sites

17 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `FlowTurn` — class, line 45
- decorator: `dataclass(frozen=True)`
- **called from:**
- `scripts/odysseus_related_flow_audit.py:87`
- `tests/test_odysseus_domain_audit.py:263`

## `Flow` — class, line 53
- decorator: `dataclass(frozen=True)`
- **called from:**
- `scripts/odysseus_related_flow_audit.py:90`
- `tests/test_odysseus_domain_audit.py:259`

## `_flow` — function, line 74
- **called from:**
- `scripts/odysseus_related_flow_audit.py:95`
- `scripts/odysseus_related_flow_audit.py:101`
- `scripts/odysseus_related_flow_audit.py:106`
- `scripts/odysseus_related_flow_audit.py:112`
- `scripts/odysseus_related_flow_audit.py:117`
- `scripts/odysseus_related_flow_audit.py:123`
- `scripts/odysseus_related_flow_audit.py:129`
- `scripts/odysseus_related_flow_audit.py:135`
- `scripts/odysseus_related_flow_audit.py:141`
- `scripts/odysseus_related_flow_audit.py:146`
- `scripts/odysseus_related_flow_audit.py:152`
- `scripts/odysseus_related_flow_audit.py:158`
- `scripts/odysseus_related_flow_audit.py:163`
- `scripts/odysseus_related_flow_audit.py:169`
- `scripts/odysseus_related_flow_audit.py:175`
- `scripts/odysseus_related_flow_audit.py:180`
- `scripts/odysseus_related_flow_audit.py:186`
- `scripts/odysseus_related_flow_audit.py:192`
- `scripts/odysseus_related_flow_audit.py:197`
- `scripts/odysseus_related_flow_audit.py:203`
- `scripts/odysseus_related_flow_audit.py:208`
- `scripts/odysseus_related_flow_audit.py:214`
- `scripts/odysseus_related_flow_audit.py:219`
- `scripts/odysseus_related_flow_audit.py:225`
- `scripts/odysseus_related_flow_audit.py:230`
- `scripts/odysseus_related_flow_audit.py:235`
- `scripts/odysseus_related_flow_audit.py:240`
- `scripts/odysseus_related_flow_audit.py:246`
- `scripts/odysseus_related_flow_audit.py:251`
- `scripts/odysseus_related_flow_audit.py:256`
- `scripts/odysseus_related_flow_audit.py:262`
- `scripts/odysseus_related_flow_audit.py:268`
- `scripts/odysseus_related_flow_audit.py:274`
- `scripts/odysseus_related_flow_audit.py:280`
- `scripts/odysseus_related_flow_audit.py:285`
- `scripts/odysseus_related_flow_audit.py:290`
- `scripts/odysseus_related_flow_audit.py:295`
- `scripts/odysseus_related_flow_audit.py:300`
- `scripts/odysseus_related_flow_audit.py:305`
- `scripts/odysseus_related_flow_audit.py:311`
- `scripts/odysseus_related_flow_audit.py:340`

## `flow_matrix` — function, line 93
- **called from:**
- `scripts/generate_sft_flow_variants_with_kimi.py:153`
- `scripts/odysseus_related_flow_audit.py:622`

## `load_flow_spec` — function, line 320
- **called from:**
- `scripts/odysseus_related_flow_audit.py:622`

## `_tool_names` — function, line 344
- **called from:**
- `scripts/odysseus_related_flow_audit.py:376`

## `_score_turn` — function, line 368
- **called from:**
- `scripts/odysseus_related_flow_audit.py:676`
- `tests/test_odysseus_domain_audit.py:270`

## `_login_cookie` — function, line 395
- **called from:**
- `scripts/odysseus_related_flow_audit.py:618`
- `scripts/odysseus_remaining_tool_audit.py:230`

## `_safe_metadata` — function, line 409
- **called from:**
- `scripts/odysseus_related_flow_audit.py:435`
- `scripts/odysseus_related_flow_audit.py:779`
- `scripts/odysseus_related_flow_audit.py:780`
- `scripts/odysseus_remaining_tool_audit.py:313`
- `scripts/odysseus_remaining_tool_audit.py:314`

## `_latest_assistant_text` — function, line 417
- **called from:**
- `scripts/odysseus_related_flow_audit.py:680`
- `scripts/odysseus_remaining_tool_audit.py:256`

## `_flow_has_good_training_shape` — function, line 427
- **called from:**
- `scripts/odysseus_related_flow_audit.py:699`
- `scripts/odysseus_remaining_tool_audit.py:277`
- `tests/test_odysseus_domain_audit.py:90`
- `tests/test_odysseus_domain_audit.py:111`
- `tests/test_odysseus_domain_audit.py:136`
- `tests/test_odysseus_domain_audit.py:154`
- `tests/test_odysseus_domain_audit.py:184`
- `tests/test_odysseus_domain_audit.py:212`
- `tests/test_odysseus_domain_audit.py:230`
- `tests/test_odysseus_domain_audit.py:252`
- `tests/test_odysseus_domain_audit.py:355`
- `tests/test_odysseus_domain_audit.py:379`

## `_contains_false_tool_failure_claim` — function, line 507
- **called from:**
- `scripts/odysseus_related_flow_audit.py:445`

## `_looks_like_concatenated_repeat` — function, line 528
- **called from:**
- `scripts/odysseus_related_flow_audit.py:502`

## `_provider_failure` — function, line 543
- **called from:**
- `scripts/odysseus_related_flow_audit.py:565`
- `scripts/odysseus_related_flow_audit.py:685`
- `tests/test_odysseus_domain_audit.py:279`
- `tests/test_odysseus_domain_audit.py:289`
- `tests/test_odysseus_domain_audit.py:300`
- `tests/test_odysseus_domain_audit.py:306`

## `_run_turn_with_provider_retry` — function, line 555
- **called from:**
- `scripts/odysseus_related_flow_audit.py:672`

## `_write_json` — function, line 572
- **called from:**
- `scripts/odysseus_related_flow_audit.py:717`
- `scripts/odysseus_related_flow_audit.py:721`
- `scripts/odysseus_related_flow_audit.py:799`

## `main` — function, line 576
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
