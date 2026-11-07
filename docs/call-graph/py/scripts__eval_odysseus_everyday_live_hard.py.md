# `scripts/eval_odysseus_everyday_live_hard.py` — definitions & call sites

12 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `marker` — function, line 39
- **called from:**
- `scripts/eval_odysseus_everyday_live_hard.py:67`
- `scripts/eval_odysseus_everyday_live_hard.py:75`
- `scripts/eval_odysseus_everyday_live_hard.py:76`
- `scripts/eval_odysseus_everyday_live_hard.py:77`
- `scripts/eval_odysseus_everyday_live_hard.py:78`
- `scripts/eval_odysseus_everyday_live_hard.py:79`
- `scripts/run_sft_overnight_fixture_flows.py:462`
- `scripts/run_sft_overnight_fixture_flows.py:499`
- `static/js/calendar.js:3526`
- `static/js/chat.js:5689`
- `static/js/chatRenderer.js:3446`
- `static/js/cookbookRunning.js:3485`

## `_replace_marker_placeholders` — function, line 43
- **called from:**
- `scripts/eval_odysseus_everyday_live_hard.py:47`
- `scripts/eval_odysseus_everyday_live_hard.py:49`
- `scripts/eval_odysseus_everyday_live_hard.py:68`

## `load_cases` — function, line 53
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:361`
- `scripts/eval_odysseus_everyday_live_hard.py:552`

## `cases` — function, line 74
- **called from:**
- `scripts/eval_odysseus_everyday_live_hard.py:55`
- `scripts/eval_odysseus_live_hard_direct.py:241`
- `static/js/chat.js:3075`

## `_tool_name_matches` — function, line 174
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

## `_ensure_calendar` — function, line 184
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:64`
- `scripts/eval_odysseus_everyday_live_hard.py:196`

## `_precreate_calendar` — function, line 195
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:106`
- `scripts/eval_odysseus_everyday_live_hard.py:225`

## `run_case` — function (async), line 214
- **called from:**
- `scripts/eval_followup_domain_continuity.py:183`
- `scripts/eval_odysseus_everyday_live_hard.py:554`
- `scripts/eval_odysseus_live_hard_direct.py:242`
- `scripts/eval_odysseus_tool_use.py:1434`
- `scripts/eval_qwen35_document_shape_direct.py:271`
- `scripts/eval_qwen35_implicit_memory.py:223`
- `scripts/eval_qwen35_tool_router_extended.py:503`
- `scripts/run_sft_environment_expansion.py:819`
- `scripts/run_sft_overnight_fixture_flows.py:782`
- `tests/test_eval_script_contract.py:204`
- `tests/test_eval_script_contract.py:266`

## `score_case` — function, line 363
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:323`
- `scripts/eval_odysseus_everyday_live_hard.py:359`
- `scripts/eval_qwen35_document_shape_direct.py:236`
- `scripts/odysseus_domain_audit.py:462`
- `scripts/odysseus_related_flow_audit.py:375`
- `scripts/odysseus_remaining_tool_audit.py:257`
- `tests/test_odysseus_domain_audit.py:31`
- `tests/test_odysseus_domain_audit.py:39`
- `tests/test_odysseus_domain_audit.py:47`

## `write_markdown` — function, line 510
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:394`
- `scripts/eval_odysseus_everyday_live_hard.py:567`

## `amain` — function (async), line 549
- **called from:**
- `scripts/eval_odysseus_everyday_live_hard.py:586`

## `main` — function, line 572
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
