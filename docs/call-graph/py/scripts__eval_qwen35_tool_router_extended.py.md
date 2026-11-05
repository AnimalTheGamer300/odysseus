# `scripts/eval_qwen35_tool_router_extended.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `cleanup_notes` — function, line 162
- **called from:**
- `scripts/eval_qwen35_tool_router_extended.py:488`
- `scripts/eval_qwen35_tool_router_extended.py:549`
- `tests/test_eval_script_contract.py:297`

## `seed_note` — function, line 182
- **called from:**
- `scripts/eval_qwen35_tool_router_extended.py:492`

## `_raw_round_text` — function, line 199
- **called from:**
- `scripts/eval_qwen35_tool_router_extended.py:310`

## `_extract_raw_tool` — function, line 205
- **called from:**
- `scripts/eval_qwen35_tool_router_extended.py:311`

## `_extract_raw_action` — function, line 219
- **called from:**
- `scripts/eval_qwen35_tool_router_extended.py:312`

## `_canonical_tool` — function, line 232
- **called from:**
- `scripts/eval_qwen35_tool_router_extended.py:345`
- `scripts/eval_qwen35_tool_router_extended.py:346`

## `hard_timeout` — function, line 239
- decorator: `contextlib.contextmanager`
- **called from:**
- `scripts/eval_odysseus_crud.py:215`
- `scripts/eval_odysseus_tool_use.py:1065`
- `scripts/eval_qwen35_tool_router_extended.py:502`

## `_raise_timeout` — function, line 244
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `timeout_record` — function, line 256
- **called from:**
- `scripts/eval_qwen35_tool_router_extended.py:511`

## `_discover_router_model` — function, line 275
- **called from:**
- `scripts/eval_qwen35_tool_router_extended.py:466`

## `annotate` — function, line 309
- **called from:**
- `scripts/eval_qwen35_implicit_memory.py:230`
- `scripts/eval_qwen35_tool_router_extended.py:512`
- `static/js/document.js:15296`

## `write_checkpoint` — function, line 401
- **called from:**
- `scripts/eval_odysseus_crud.py:916`
- `scripts/eval_odysseus_crud.py:920`
- `scripts/eval_qwen35_tool_router_extended.py:516`
- `scripts/eval_qwen35_tool_router_extended.py:566`

## `main` — function, line 421
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
