# `scripts/run_sft_overnight_fixture_flows.py` — definitions & call sites

26 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `atomic_write_text` — function, line 42
- **called from:**
- `routes/auth_routes.py:615`
- `scripts/run_sft_overnight_fixture_flows.py:658`
- `scripts/run_sft_overnight_fixture_flows.py:677`
- `scripts/run_sft_overnight_fixture_flows.py:712`
- `scripts/run_sft_overnight_fixture_flows.py:713`
- `services/memory/skills.py:227`
- `services/memory/skills.py:489`
- `services/memory/skills.py:499`
- `src/containment_worker.py:116`
- `tests/test_atomic_io.py:168`
- `tests/test_atomic_io.py:176`
- `tests/test_atomic_io.py:184`
- `tests/test_atomic_io.py:186`
- `tests/test_atomic_io.py:194`
- `tests/test_atomic_io.py:203`
- `tests/test_atomic_io.py:214`
- `tests/test_atomic_io.py:223`
- `tests/test_atomic_io.py:232`
- `tests/test_atomic_io.py:246`
- `tests/test_sft_overnight_fixture_flows.py:293`

## `CaseTimeoutError` — class, line 53
- **called from:**
- `scripts/run_sft_environment_expansion.py:64`
- `scripts/run_sft_overnight_fixture_flows.py:58`

## `_case_timeout_handler` — function, line 57
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `login` — function, line 61
- **called from:**
- `mcp_servers/email_server.py:435`
- `mcp_servers/email_server.py:2560`
- `routes/email/email_helpers.py:270`
- `routes/email/email_helpers.py:1384`
- `routes/email/email_routes.py:7637`
- `routes/email/email_routes.py:7701`
- `scripts/demo_email/seed_demo_emails.py:60`
- `scripts/diffusion_server.py:365`
- `scripts/run_sft_environment_expansion.py:696`
- `scripts/run_sft_environment_expansion.py:733`
- `scripts/run_sft_overnight_fixture_flows.py:774`
- `scripts/sft_email_overseer.py:651`
- `tests/test_auth_event_loop.py:111`

## `ensure_calendar` — function, line 72
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:761`

## `seed_case` — function, line 92
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:569`
- `tests/test_sft_overnight_fixture_flows.py:228`

## `collect_state_and_cleanup` — function, line 164
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:572`
- `scripts/run_sft_overnight_fixture_flows.py:576`

## `create_session` — function, line 205
- **called from:**
- `core/session_manager.py:1113`
- `routes/compare/compare_routes.py:187`
- `routes/history/history_routes.py:1101`
- `routes/research/research_routes.py:849`
- `routes/session_routes.py:656`
- `routes/session_routes.py:1279`
- `routes/webhook/webhook_routes.py:306`
- `routes/webhook/webhook_routes.py:367`
- `scripts/eval_odysseus_contextual_tool_use.py:880`
- `scripts/odysseus_conversation_qa.py:796`
- `scripts/run_sft_environment_expansion.py:697`
- `scripts/run_sft_overnight_fixture_flows.py:570`
- `scripts/sft_email_overseer.py:653`
- `src/agent_tools/session_tools.py:61`
- `src/agent_tools/session_tools.py:460`
- `src/agent_tools/session_tools.py:501`
- `tests/test_admin_listing_authorization.py:45`
- `tests/test_auth_session_revocation.py:52`
- `tests/test_auth_session_revocation.py:53`
- `tests/test_auth_session_revocation.py:96`
- `tests/test_auth_session_revocation.py:97`
- `tests/test_auth_session_revocation.py:98`
- `tests/test_auth_session_revocation.py:110`
- `tests/test_auth_session_revocation.py:111`
- `tests/test_auth_session_revocation.py:124`
- `tests/test_auth_session_revocation.py:125`
- `tests/test_chat_document_owner_context.py:80`
- `tests/test_chatgpt_session_binding.py:42`
- `tests/test_database_test_isolation.py:43`
- `tests/test_delete_user_revokes_api_tokens.py:120`
- `tests/test_history_add_message_validation.py:41`
- `tests/test_history_add_message_validation.py:57`
- `tests/test_history_truncate_validation.py:21`
- `tests/test_odysseus_conversation_qa.py:103`
- `tests/test_session_cwd_persistence.py:24`
- `tests/test_session_discovery_message_count.py:33`
- `tests/test_session_header_persistence.py:23`
- `tests/test_truncate_message_count_regression.py:28`
- `tests/test_truncate_message_count_regression.py:58`

## `stream_turn` — function, line 223
- **called from:**
- `scripts/run_sft_environment_expansion.py:702`
- `scripts/run_sft_overnight_fixture_flows.py:571`
- `scripts/sft_email_overseer.py:668`

## `tool_names` — function, line 255
- **called from:**
- `scripts/run_sft_environment_expansion.py:407`
- `scripts/run_sft_environment_expansion.py:711`
- `scripts/run_sft_overnight_fixture_flows.py:269`
- `scripts/run_sft_overnight_fixture_flows.py:594`
- `scripts/sft_email_overseer.py:685`

## `tool_outputs` — function, line 259
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:270`

## `score` — function, line 267
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:573`
- `scripts/select_sft_expansion_seeds.py:115`
- `scripts/select_sft_expansion_seeds.py:127`
- `tests/test_sft_overnight_fixture_flows.py:115`

## `quarantine_sft_rows` — function, line 307
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:581`
- `tests/test_sft_overnight_fixture_flows.py:84`

## `delete_session` — function, line 337
- **called from:**
- `routes/session_routes.py:449`
- `routes/session_routes.py:918`
- `routes/session_routes.py:943`
- `routes/session_routes.py:980`
- `routes/session_routes.py:981`
- `routes/session_routes.py:1483`
- `routes/session_routes.py:1496`
- `scripts/run_sft_environment_expansion.py:740`
- `scripts/run_sft_overnight_fixture_flows.py:580`
- `src/agent_tools/session_tools.py:404`
- `tests/test_chat_image_preservation.py:28`
- `tests/test_chat_image_preservation.py:31`
- `tests/test_session_ghost_delete.py:123`
- `tests/test_session_ghost_delete.py:133`
- `tests/test_session_manager.py:106`

## `owner_profile` — function, line 414
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:419`
- `scripts/run_sft_overnight_fixture_flows.py:424`
- `scripts/run_sft_overnight_fixture_flows.py:459`
- `scripts/run_sft_overnight_fixture_flows.py:497`

## `marker` — function, line 418
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
- `static/js/chatRenderer.js:3435`
- `static/js/cookbookRunning.js:3485`

## `build_email_case` — function, line 423
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:549`
- `tests/test_sft_overnight_fixture_flows.py:135`
- `tests/test_sft_overnight_fixture_flows.py:141`
- `tests/test_sft_overnight_fixture_flows.py:147`
- `tests/test_sft_overnight_fixture_flows.py:152`
- `tests/test_sft_overnight_fixture_flows.py:173`

## `build_note_case` — function, line 458
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:551`
- `tests/test_sft_overnight_fixture_flows.py:136`
- `tests/test_sft_overnight_fixture_flows.py:142`
- `tests/test_sft_overnight_fixture_flows.py:148`
- `tests/test_sft_overnight_fixture_flows.py:153`
- `tests/test_sft_overnight_fixture_flows.py:169`
- `tests/test_sft_overnight_fixture_flows.py:181`
- `tests/test_sft_overnight_fixture_flows.py:182`

## `build_calendar_case` — function, line 496
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:553`
- `tests/test_sft_overnight_fixture_flows.py:137`
- `tests/test_sft_overnight_fixture_flows.py:138`
- `tests/test_sft_overnight_fixture_flows.py:143`
- `tests/test_sft_overnight_fixture_flows.py:144`
- `tests/test_sft_overnight_fixture_flows.py:149`
- `tests/test_sft_overnight_fixture_flows.py:154`

## `build_cases` — function, line 546
- **called from:**
- `scripts/build_odysseus_everyday_deepseek_heldout_cases.py:256`
- `scripts/build_odysseus_everyday_deepseek_heldout_v3_cases.py:335`
- `scripts/curate_public_search_seed_cases.py:291`
- `scripts/eval_followup_domain_continuity.py:178`
- `scripts/run_sft_overnight_fixture_flows.py:755`

## `run_case` — function, line 557
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

## `load_existing_results` — function, line 603
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:764`
- `tests/test_sft_overnight_fixture_flows.py:58`

## `write_outputs` — function, line 633
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:794`
- `scripts/run_sft_overnight_fixture_flows.py:799`

## `clean_counts_by_domain` — function, line 680
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:777`
- `scripts/run_sft_overnight_fixture_flows.py:801`
- `tests/test_sft_overnight_fixture_flows.py:122`

## `write_curated_trace_outputs` — function, line 690
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:811`
- `tests/test_sft_overnight_fixture_flows.py:267`

## `main` — function, line 727
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
