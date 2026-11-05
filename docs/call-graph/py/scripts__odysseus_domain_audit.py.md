# `scripts/odysseus_domain_audit.py` — definitions & call sites

20 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `Case` — class, line 33
- decorator: `dataclass(frozen=True)`
- **called from:**
- `scripts/odysseus_domain_audit.py:43`
- `scripts/odysseus_related_flow_audit.py:369`
- `scripts/odysseus_remaining_tool_audit.py:187`
- `tests/test_odysseus_domain_audit.py:29`
- `tests/test_odysseus_domain_audit.py:37`
- `tests/test_odysseus_domain_audit.py:45`

## `_cases` — function, line 42
- **called from:**
- `scripts/odysseus_domain_audit.py:131`
- `scripts/odysseus_domain_audit.py:132`
- `scripts/odysseus_domain_audit.py:136`
- `scripts/odysseus_domain_audit.py:140`
- `scripts/odysseus_domain_audit.py:144`
- `scripts/odysseus_domain_audit.py:148`

## `prompt_matrix` — function, line 50
- **called from:**
- `scripts/odysseus_domain_audit.py:443`
- `tests/test_odysseus_domain_audit.py:15`

## `read_rows` — function, line 52
- **called from:**
- `scripts/odysseus_domain_audit.py:108`

## `_sse_events` — function, line 152
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:267`
- `scripts/eval_odysseus_contextual_tool_use.py:695`
- `scripts/eval_odysseus_tool_use.py:1076`
- `scripts/odysseus_domain_audit.py:304`
- `scripts/run_sft_environment_expansion.py:291`
- `scripts/run_sft_overnight_fixture_flows.py:244`
- `tests/test_eval_script_contract.py:61`

## `_event_text` — function, line 173
- **called from:**
- `scripts/odysseus_domain_audit.py:462`
- `scripts/odysseus_related_flow_audit.py:565`
- `scripts/odysseus_related_flow_audit.py:680`
- `scripts/odysseus_remaining_tool_audit.py:256`

## `_tool_events` — function, line 183
- **called from:**
- `scripts/odysseus_domain_audit.py:192`

## `score_case` — function, line 191
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

## `_session_payload` — function, line 221
- **called from:**
- `scripts/odysseus_domain_audit.py:459`
- `scripts/odysseus_domain_audit.py:468`
- `scripts/odysseus_related_flow_audit.py:673`
- `scripts/odysseus_related_flow_audit.py:698`
- `scripts/odysseus_remaining_tool_audit.py:252`
- `scripts/odysseus_remaining_tool_audit.py:265`
- `scripts/odysseus_remaining_tool_audit.py:276`

## `_durable_tool_events` — function, line 227
- **called from:**
- `scripts/odysseus_domain_audit.py:460`
- `scripts/odysseus_related_flow_audit.py:674`
- `scripts/odysseus_remaining_tool_audit.py:253`
- `tests/test_odysseus_domain_audit.py:75`

## `_history_pairs` — function, line 251
- **called from:**
- `scripts/odysseus_domain_audit.py:503`
- `scripts/odysseus_related_flow_audit.py:429`
- `scripts/odysseus_related_flow_audit.py:765`
- `scripts/odysseus_remaining_tool_audit.py:303`

## `_create_session` — function, line 269
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:210`
- `scripts/odysseus_domain_audit.py:454`
- `scripts/odysseus_related_flow_audit.py:639`
- `scripts/odysseus_remaining_tool_audit.py:245`

## `_run_turn` — function, line 283
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:368`
- `scripts/odysseus_domain_audit.py:458`
- `scripts/odysseus_related_flow_audit.py:564`
- `scripts/odysseus_remaining_tool_audit.py:251`
- `tests/test_runtime_behavior_regressions.py:123`
- `tests/test_runtime_behavior_regressions.py:156`

## `_render_prompt` — function, line 308
- **called from:**
- `scripts/odysseus_domain_audit.py:456`
- `scripts/odysseus_related_flow_audit.py:658`
- `scripts/odysseus_remaining_tool_audit.py:249`

## `_seed_fixtures` — function, line 312
- **called from:**
- `scripts/odysseus_domain_audit.py:455`
- `scripts/odysseus_related_flow_audit.py:654`

## `_cleanup_fixtures` — function, line 354
- **called from:**
- `scripts/odysseus_domain_audit.py:492`
- `scripts/odysseus_related_flow_audit.py:738`

## `_review_session` — function, line 377
- **called from:**
- `scripts/odysseus_domain_audit.py:475`

## `_snapshot_theme_preferences` — function, line 399
- **called from:**
- `scripts/odysseus_domain_audit.py:444`

## `_restore_theme_preferences` — function, line 407
- **called from:**
- `scripts/odysseus_domain_audit.py:493`

## `main` — function, line 416
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
