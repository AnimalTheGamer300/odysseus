# `scripts/eval_odysseus_tool_use.py` — definitions & call sites

34 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_email_fixture` — function, line 163
- decorator: `contextlib.contextmanager`
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1430`

## `_cleanup_notes` — function, line 206
- **called from:**
- `scripts/eval_odysseus_tool_use.py:376`
- `scripts/eval_odysseus_tool_use.py:385`

## `_seed_note` — function, line 224
- **called from:**
- `scripts/eval_odysseus_tool_use.py:377`

## `_fixture_owner` — function, line 241
- **called from:**
- `scripts/eval_odysseus_contextual_tool_use.py:555`
- `scripts/eval_odysseus_tool_use.py:291`

## `_cleanup_db_fixtures` — function, line 245
- **called from:**
- `scripts/eval_odysseus_tool_use.py:379`
- `scripts/eval_odysseus_tool_use.py:387`

## `_seed_db_fixtures` — function, line 278
- **called from:**
- `scripts/eval_odysseus_tool_use.py:380`

## `_content_fixtures` — function, line 367
- decorator: `contextlib.contextmanager`
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1431`

## `_command_contract_ok` — function, line 390
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1241`
- `tests/test_eval_script_contract.py:92`
- `tests/test_eval_script_contract.py:99`
- `tests/test_eval_script_contract.py:109`
- `tests/test_eval_script_contract.py:113`
- `tests/test_eval_script_contract.py:117`
- `tests/test_eval_script_contract.py:124`
- `tests/test_eval_script_contract.py:128`
- `tests/test_eval_script_contract.py:132`
- `tests/test_eval_script_contract.py:136`

## `host_commands` — function, line 392
- **called from:**
- `scripts/eval_odysseus_tool_use.py:445`

## `_cookie` — function, line 618
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:363`
- `scripts/eval_odysseus_contextual_tool_use.py:872`
- `scripts/eval_odysseus_tool_use.py:1401`
- `scripts/eval_qwen35_implicit_memory.py:218`
- `scripts/eval_qwen35_tool_router_extended.py:483`

## `_sse_events` — function, line 627
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:267`
- `scripts/eval_odysseus_contextual_tool_use.py:695`
- `scripts/eval_odysseus_tool_use.py:1076`
- `scripts/odysseus_domain_audit.py:304`
- `scripts/run_sft_environment_expansion.py:291`
- `scripts/run_sft_overnight_fixture_flows.py:244`
- `tests/test_eval_script_contract.py:61`

## `flush` — function, line 631
- **called from:**
- `core/atomic_io.py:43`
- `core/atomic_io.py:76`
- `core/atomic_io.py:97`
- `core/database.py:555`
- `routes/calendar_routes.py:331`
- `routes/calendar_routes.py:339`
- `routes/email/email_routes.py:7545`
- `scripts/cook_sft_alex_conversations.py:235`
- `scripts/demo_email/demo_account.py:117`
- `scripts/demo_email/demo_account.py:165`
- `scripts/eval_exact_file_routing.py:158`
- `scripts/eval_odysseus_tool_use.py:658`
- `scripts/eval_odysseus_tool_use.py:661`
- `scripts/migrate_searxng_settings.py:133`
- `scripts/pr_blocker_audit.py:125`
- `scripts/pr_blocker_audit.py:138`
- `scripts/pr_blocker_audit.py:144`
- `scripts/pr_blocker_audit.py:151`
- `scripts/run_sft_environment_expansion.py:517`
- `src/agent_tools/filesystem_tools.py:615`
- `src/api_key_manager.py:94`
- `src/browser_identity.py:254`
- `src/containment_worker.py:80`
- `src/email_thread_parser.py:328`
- `src/email_thread_parser.py:334`
- `src/email_thread_parser.py:371`
- `src/email_thread_parser.py:385`
- `src/llm_core.py:3659`
- `src/llm_core.py:3677`
- `src/llm_core.py:3961`
- `src/llm_core.py:4298`
- `src/task_scheduler.py:2849`
- `src/upload_handler.py:799`
- `tests/smoke/stub_provider.py:136`
- `tests/test_atomic_io.py:101`
- `tests/test_codeql_python_residual_closure.py:140`
- `tests/test_codeql_python_residual_closure.py:149`
- `tests/test_codeql_python_residual_closure.py:155`
- `tests/test_codeql_python_residual_closure.py:157`
- `tests/test_daily_brief_local_calendar.py:56`
- `tests/test_launcher.py:24`
- `static/js/chat.js:4225`
- `static/js/emailLibrary/bodyRender.js:746`
- `static/js/emailLibrary/bodyRender.js:752`
- `static/js/emailLibrary/bodyRender.js:757`
- `static/js/liveThinkingThrottle.js:18`
- `static/js/liveThinkingThrottle.js:191`

## `hard_timeout` — function, line 667
- decorator: `contextlib.contextmanager`
- **called from:**
- `scripts/eval_odysseus_crud.py:215`
- `scripts/eval_odysseus_tool_use.py:1065`
- `scripts/eval_qwen35_tool_router_extended.py:502`

## `_raise_timeout` — function, line 672
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_visible_event_text` — function, line 684
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:271`
- `scripts/eval_odysseus_contextual_tool_use.py:699`
- `scripts/eval_odysseus_tool_use.py:1078`
- `scripts/run_sft_environment_expansion.py:295`
- `scripts/run_sft_overnight_fixture_flows.py:246`

## `_tool_matches` — function, line 693
- **called from:**
- `scripts/eval_odysseus_tool_use.py:719`
- `scripts/eval_odysseus_tool_use.py:722`
- `scripts/eval_odysseus_tool_use.py:728`

## `_tool_sequence_matches` — function, line 711
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1240`
- `tests/test_eval_script_contract.py:83`
- `tests/test_eval_script_contract.py:86`

## `_no_tool_quality_ok` — function, line 735
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1255`

## `_email_action_quality_ok` — function, line 748
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1257`

## `_content_quality_ok` — function, line 768
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1259`

## `_malformed_text_surface` — function, line 810
- **called from:**
- `scripts/eval_odysseus_tool_use.py:736`
- `scripts/eval_odysseus_tool_use.py:750`
- `scripts/eval_odysseus_tool_use.py:1242`

## `_raise_for_status_with_body` — function, line 852
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:95`
- `scripts/eval_odysseus_app_route_smoke.py:123`
- `scripts/eval_odysseus_app_route_smoke.py:266`
- `scripts/eval_odysseus_contextual_tool_use.py:665`
- `scripts/eval_odysseus_contextual_tool_use.py:694`
- `scripts/eval_odysseus_tool_use.py:1027`
- `scripts/eval_odysseus_tool_use.py:1075`
- `scripts/run_sft_environment_expansion.py:231`
- `scripts/run_sft_environment_expansion.py:252`
- `scripts/run_sft_environment_expansion.py:290`
- `scripts/run_sft_overnight_fixture_flows.py:67`
- `scripts/run_sft_overnight_fixture_flows.py:219`
- `scripts/run_sft_overnight_fixture_flows.py:243`

## `_hard_turn_timeout` — function, line 868
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1065`
- `tests/test_eval_script_contract.py:18`
- `tests/test_eval_script_contract.py:22`

## `_reported_model` — function, line 885
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1450`
- `scripts/eval_qwen35_tool_router_extended.py:554`
- `tests/test_eval_script_contract.py:27`

## `_summary_exit_code` — function, line 894
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1486`
- `tests/test_eval_script_contract.py:78`
- `tests/test_eval_script_contract.py:79`

## `_is_infra_failure_error` — function, line 906
- **called from:**
- `scripts/analyze_odysseus_eval_targets.py:66`
- `scripts/eval_odysseus_tool_use.py:1121`
- `scripts/summarize_odysseus_eval_delta.py:52`

## `_exception_record` — function, line 930
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1436`

## `_is_infra_failure_tool_output` — function, line 963
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1188`

## `_stream_exception_if_empty` — function, line 984
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1112`
- `tests/test_eval_script_contract.py:71`
- `tests/test_eval_script_contract.py:72`

## `_tool_approval_from_event` — function, line 993
- **called from:**
- `scripts/eval_odysseus_contextual_tool_use.py:705`
- `scripts/eval_odysseus_tool_use.py:1089`

## `run_case` — function, line 1009
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

## `_output_ok` — function, line 1157
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1193`

## `_invocation_ok` — function, line 1168
- **called from:**
- `scripts/eval_odysseus_tool_use.py:1197`

## `main` — function, line 1323
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
