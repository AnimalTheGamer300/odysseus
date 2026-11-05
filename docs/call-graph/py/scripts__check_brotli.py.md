# `scripts/check_brotli.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `command` — function, line 22
- **called from:**
- `scripts/check_brotli.py:31`
- `scripts/check_brotli.py:45`
- `scripts/check_brotli.py:95`
- `src/browser_identity.py:421`
- `src/browser_identity.py:422`
- `src/browser_identity.py:435`
- `src/browser_identity.py:461`
- `src/browser_identity.py:462`
- `src/browser_identity.py:589`
- `tests/test_browser_identity_transport.py:65`
- `tests/test_browser_producer_live_contract.py:33`
- `tests/test_browser_producer_live_contract.py:38`
- `tests/test_browser_producer_live_contract.py:54`
- `tests/test_browser_producer_live_contract.py:56`
- `tests/test_browser_producer_live_contract.py:59`
- `tests/test_browser_producer_live_contract.py:62`
- `tests/test_browser_producer_live_contract.py:65`
- `tests/test_browser_producer_live_contract.py:72`
- `tests/test_browser_producer_live_contract.py:79`
- `tests/test_browser_producer_live_contract.py:83`
- `tests/test_browser_producer_live_contract.py:85`
- `tests/test_browser_producer_live_contract.py:86`
- `tests/test_browser_producer_live_contract.py:91`
- `tests/test_browser_producer_live_contract.py:92`
- `tests/test_browser_producer_live_contract.py:106`
- `static/js/cookbook.js:1216`
- `static/js/cookbook.js:1728`
- `static/js/cookbookRunning.js:1640`
- `static/js/cookbookServe.js:3421`
- `static/js/slashAutocomplete.js:217`
- `static/js/slashAutocomplete.js:218`
- `static/js/slashCommands.js:6408`

## `check_package` — function, line 26
- **called from:**
- `scripts/check_brotli.py:106`
- `tests/test_brotli_image_gate.py:43`
- `tests/test_brotli_image_gate.py:46`
- `tests/test_brotli_image_gate.py:54`
- `tests/test_brotli_image_gate.py:61`

## `loaded_path` — function, line 53
- **called from:**
- `scripts/check_brotli.py:108`

## `DlInfo` — class, line 56
- **called from:**
- `scripts/check_brotli.py:63`

## `check_decoder` — function, line 69
- **called from:**
- `scripts/check_brotli.py:111`
- `tests/test_brotli_image_gate.py:167`
- `tests/test_brotli_image_gate.py:171`
- `tests/test_brotli_image_gate.py:176`
- `tests/test_brotli_image_gate.py:183`

## `check_node` — function, line 92
- **called from:**
- `scripts/check_brotli.py:113`
- `tests/test_brotli_image_gate.py:195`
- `tests/test_brotli_image_gate.py:198`

## `main` — function, line 101
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
