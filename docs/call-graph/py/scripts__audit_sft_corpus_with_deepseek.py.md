# `scripts/audit_sft_corpus_with_deepseek.py` — definitions & call sites

11 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `decrypt_secret` — function, line 42
- **called from:**
- `scripts/audit_email_sft_with_deepseek.py:74`
- `scripts/audit_sft_corpus_with_deepseek.py:73`
- `scripts/repair_email_sft_with_kimi.py:55`

## `deepseek_endpoint` — function, line 51
- **called from:**
- `scripts/audit_email_sft_with_deepseek.py:250`
- `scripts/audit_sft_corpus_with_deepseek.py:287`
- `scripts/build_odysseus_everyday_deepseek_heldout_cases.py:253`
- `scripts/build_odysseus_everyday_deepseek_heldout_v3_cases.py:332`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:429`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:458`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:480`
- `scripts/build_odysseus_web_teacher_sft.py:380`
- `scripts/odysseus_domain_audit.py:385`

## `load_rows` — function, line 78
- **called from:**
- `scripts/audit_sft_corpus_with_deepseek.py:218`

## `live_session_ids` — function, line 93
- **called from:**
- `scripts/audit_sft_corpus_with_deepseek.py:220`

## `row_flags` — function, line 101
- **called from:**
- `scripts/audit_sft_corpus_with_deepseek.py:140`
- `scripts/audit_sft_corpus_with_deepseek.py:235`
- `scripts/audit_sft_corpus_with_deepseek.py:240`
- `scripts/audit_sft_corpus_with_deepseek.py:283`

## `compact_row` — function, line 129
- **called from:**
- `scripts/audit_sft_corpus_with_deepseek.py:292`

## `clip` — function, line 130
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

## `_parse_json_message` — function, line 153
- **called from:**
- `scripts/audit_sft_corpus_with_deepseek.py:191`

## `judge` — function, line 165
- **called from:**
- `scripts/audit_sft_corpus_with_deepseek.py:299`

## `main` — function, line 202
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

## `run_batch` — function, line 295
- **called from:**
- `services/skills/audit_workflow.py:434`
- `services/skills/job_coordinator.py:189`
