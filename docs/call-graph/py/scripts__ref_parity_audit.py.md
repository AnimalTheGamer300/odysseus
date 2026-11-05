# `scripts/ref_parity_audit.py` — definitions & call sites

26 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `GitError` — class, line 85
- **called from:**
- `scripts/ref_parity_audit.py:148`
- `scripts/ref_parity_audit.py:238`

## `Commit` — class, line 90
- decorator: `dataclass`
- **called from:**
- `scripts/ref_parity_audit.py:197`

## `CommitVerdict` — class, line 99
- decorator: `dataclass`
- **called from:**
- `scripts/ref_parity_audit.py:350`

## `CommitVerdict.verdict` — method, line 106
- decorator: `property`
- **called from:**
- `routes/shell_routes.py:741`
- `routes/shell_routes.py:784`
- `routes/shell_routes.py:794`
- `scripts/verify_notes_browser_runtime.py:28`
- `scripts/verify_notes_browser_runtime.py:30`
- `src/process_lifecycle.py:148`
- `src/process_lifecycle.py:158`
- `src/process_lifecycle.py:556`
- `src/process_lifecycle.py:580`
- `src/process_lifecycle.py:597`
- `tests/test_process_lifecycle.py:170`
- `tests/test_process_lifecycle.py:191`
- `tests/test_process_lifecycle.py:342`
- `tests/test_runtime_resource_integration.py:506`

## `Report` — class, line 117
- decorator: `dataclass`
- **called from:**
- `scripts/ref_parity_audit.py:325`

## `Report.by_verdict` — method, line 131
- **called from:**
- `scripts/ref_parity_audit.py:393`
- `scripts/ref_parity_audit.py:394`
- `scripts/ref_parity_audit.py:395`
- `scripts/ref_parity_audit.py:396`
- `scripts/ref_parity_audit.py:477`
- `tests/test_ref_parity_audit.py:203`

## `run_git` — function, line 140
- **called from:**
- `scripts/ref_parity_audit.py:153`
- `scripts/ref_parity_audit.py:158`
- `scripts/ref_parity_audit.py:192`
- `scripts/ref_parity_audit.py:215`
- `scripts/ref_parity_audit.py:219`
- `scripts/ref_parity_audit.py:243`

## `resolve_ref` — function, line 152
- **called from:**
- `scripts/ref_parity_audit.py:327`
- `scripts/ref_parity_audit.py:329`

## `merge_base` — function, line 156
- **called from:**
- `scripts/ref_parity_audit.py:330`

## `list_commits` — function, line 164
- **called from:**
- `scripts/ref_parity_audit.py:337`

## `commit_diff` — function, line 208
- **called from:**
- `scripts/ref_parity_audit.py:346`

## `probe_present` — function, line 224
- **called from:**
- `scripts/ref_parity_audit.py:348`

## `list_tree` — function, line 242
- **called from:**
- `scripts/ref_parity_audit.py:360`
- `scripts/ref_parity_audit.py:361`

## `is_excluded` — function, line 252
- **called from:**
- `scripts/ref_parity_audit.py:269`
- `scripts/ref_parity_audit.py:360`
- `scripts/ref_parity_audit.py:361`
- `tests/test_ref_parity_audit.py:85`

## `added_lines` — function, line 260
- **called from:**
- `scripts/ref_parity_audit.py:346`
- `tests/test_ref_parity_audit.py:108`

## `probe_score` — function, line 277
- **called from:**
- `scripts/ref_parity_audit.py:305`

## `is_probe_candidate` — function, line 283
- **called from:**
- `scripts/ref_parity_audit.py:302`
- `tests/test_ref_parity_audit.py:30`
- `tests/test_ref_parity_audit.py:31`
- `tests/test_ref_parity_audit.py:33`
- `tests/test_ref_parity_audit.py:34`

## `pick_probes` — function, line 292
- **called from:**
- `scripts/ref_parity_audit.py:347`
- `tests/test_ref_parity_audit.py:45`
- `tests/test_ref_parity_audit.py:54`
- `tests/test_ref_parity_audit.py:65`

## `audit` — function, line 314
- **called from:**
- `scripts/audit_c5_benchmark_evidence.py:1560`
- `scripts/ref_parity_audit.py:562`
- `src/agent_loop.py:21717`
- `src/agent_loop.py:21730`
- `src/agent_loop.py:21762`
- `src/clean_agent_preview.py:6013`
- `src/clean_agent_preview.py:7158`
- `src/clean_agent_preview.py:7450`
- `src/clean_agent_preview.py:7837`
- `src/turn_contract.py:6341`
- `tests/test_audit_c5_benchmark_evidence.py:67`
- `tests/test_audit_c5_benchmark_evidence.py:183`
- `tests/test_audit_c5_benchmark_evidence.py:204`
- `tests/test_audit_c5_benchmark_evidence.py:212`
- `tests/test_audit_c5_benchmark_evidence.py:300`
- `tests/test_audit_c5_benchmark_evidence.py:301`
- `tests/test_audit_c5_benchmark_evidence.py:1191`
- `tests/test_audit_c5_benchmark_evidence.py:1222`
- `tests/test_audit_c5_benchmark_evidence.py:1239`
- `tests/test_audit_c5_benchmark_evidence.py:1243`
- `tests/test_audit_c5_benchmark_evidence.py:1366`
- `tests/test_audit_c5_benchmark_evidence.py:1385`
- `tests/test_audit_c5_benchmark_evidence.py:1406`
- `tests/test_audit_c5_benchmark_evidence.py:1433`
- `tests/test_audit_c5_benchmark_evidence.py:1460`
- `tests/test_audit_c5_benchmark_evidence.py:1475`
- `tests/test_audit_c5_benchmark_evidence.py:1491`
- `tests/test_audit_c5_benchmark_evidence.py:1741`
- `tests/test_audit_c5_benchmark_evidence.py:1757`
- `tests/test_audit_c5_benchmark_evidence.py:1772`
- `tests/test_audit_c5_benchmark_evidence.py:1787`
- `tests/test_audit_c5_benchmark_evidence.py:1802`
- `tests/test_audit_c5_benchmark_evidence.py:1817`
- `tests/test_audit_c5_benchmark_evidence.py:1832`
- `tests/test_audit_c5_benchmark_evidence.py:1847`
- `tests/test_audit_c5_benchmark_evidence.py:1862`
- `tests/test_audit_c5_benchmark_evidence.py:1877`
- `tests/test_audit_c5_benchmark_evidence.py:1897`
- `tests/test_audit_c5_benchmark_evidence.py:1912`
- `tests/test_audit_c5_benchmark_evidence.py:1927`
- `tests/test_audit_c5_benchmark_evidence.py:1952`
- `tests/test_audit_c5_benchmark_evidence.py:1978`
- `tests/test_audit_c5_benchmark_evidence.py:2012`
- `tests/test_audit_c5_benchmark_evidence.py:2041`
- `tests/test_audit_c5_benchmark_evidence.py:2071`
- `tests/test_audit_c5_benchmark_evidence.py:2093`
- `tests/test_audit_c5_benchmark_evidence.py:2117`
- `tests/test_audit_c5_benchmark_evidence.py:2180`
- `tests/test_audit_c5_benchmark_evidence.py:2214`
- `tests/test_audit_c5_benchmark_evidence.py:2273`
- `tests/test_audit_c5_benchmark_evidence.py:2297`
- `tests/test_audit_c5_benchmark_evidence.py:2325`
- `tests/test_audit_c5_benchmark_evidence.py:2342`
- `tests/test_audit_c5_benchmark_evidence.py:2358`
- `tests/test_audit_c5_benchmark_evidence.py:2371`
- `tests/test_audit_c5_benchmark_evidence.py:2388`
- `tests/test_audit_c5_benchmark_evidence.py:2415`
- `tests/test_audit_c5_benchmark_evidence.py:2435`
- `tests/test_audit_c5_benchmark_evidence.py:2556`
- `tests/test_audit_c5_benchmark_evidence.py:2640`
- … +21 more (grep the name in repo)

## `_commit_table` — function, line 372
- **called from:**
- `scripts/ref_parity_audit.py:423`
- `scripts/ref_parity_audit.py:434`
- `scripts/ref_parity_audit.py:442`

## `_file_list` — function, line 385
- **called from:**
- `scripts/ref_parity_audit.py:454`
- `scripts/ref_parity_audit.py:461`

## `render_markdown` — function, line 392
- **called from:**
- `scripts/pr_blocker_audit.py:1042`
- `scripts/ref_parity_audit.py:577`
- `tests/test_pr_blocker_audit.py:583`
- `tests/test_pr_blocker_audit.py:604`
- `tests/test_pr_blocker_audit.py:691`
- `tests/test_ref_parity_audit.py:298`

## `render_json` — function, line 466
- **called from:**
- `scripts/pr_blocker_audit.py:1040`
- `scripts/ref_parity_audit.py:577`
- `tests/test_pr_blocker_audit.py:934`
- `tests/test_pr_blocker_audit.py:935`

## `positive_int` — function, line 511
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `build_parser` — function, line 518
- **called from:**
- `scripts/pr_blocker_audit.py:1025`
- `scripts/ref_parity_audit.py:556`
- `tests/run_focus.py:299`
- `tests/run_order_report.py:137`
- `tests/test_pr_blocker_audit.py:239`
- `tests/test_pr_blocker_audit.py:960`
- `tests/test_ref_parity_audit.py:351`

## `main` — function, line 555
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
