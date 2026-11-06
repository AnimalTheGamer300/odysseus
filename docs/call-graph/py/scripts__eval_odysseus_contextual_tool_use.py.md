# `scripts/eval_odysseus_contextual_tool_use.py` — definitions & call sites

12 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `malformed_text_surface` — function, line 493
- **called from:**
- `scripts/eval_odysseus_contextual_tool_use.py:791`

## `canonical_tool` — function, line 529
- **called from:**
- `scripts/audit_historical_tool_routing.py:26`
- `scripts/eval_followup_domain_continuity.py:132`
- `scripts/eval_followup_domain_continuity.py:161`
- `scripts/eval_odysseus_contextual_tool_use.py:748`
- `scripts/eval_odysseus_contextual_tool_use.py:758`
- `scripts/eval_odysseus_contextual_tool_use.py:779`
- `src/agent_runtime/authority.py:61`
- `src/agent_runtime/authority.py:89`
- `src/agent_runtime/authority.py:139`
- `src/agent_runtime/authority.py:228`
- `src/agent_runtime/authority.py:487`
- `src/agent_runtime/authority.py:487`
- `src/agent_runtime/authority.py:488`
- `src/agent_runtime/authority.py:519`
- `src/agent_runtime/authority.py:522`
- `src/agent_runtime/authority.py:531`
- `src/tool_routing_experiment.py:77`
- `src/tool_routing_experiment.py:92`
- `src/tool_routing_experiment.py:107`
- `src/tool_routing_experiment.py:107`
- `src/tool_routing_experiment.py:118`
- `src/tool_routing_experiment.py:125`
- `src/tool_routing_experiment.py:126`
- `src/tool_routing_experiment.py:134`
- `src/tool_routing_experiment.py:141`
- `src/tool_routing_experiment.py:151`
- `src/tool_routing_experiment.py:163`
- `src/tool_routing_experiment.py:167`
- `src/tool_routing_experiment.py:173`
- `src/tool_routing_experiment.py:178`
- `src/tool_routing_experiment.py:185`
- `src/tool_routing_experiment.py:190`
- `src/tool_routing_experiment.py:211`
- `src/turn_contract.py:2190`
- `src/turn_contract.py:2198`
- `src/turn_contract.py:2207`
- `src/turn_contract.py:2622`
- `src/turn_contract.py:2633`
- `src/turn_contract.py:2743`
- `src/turn_contract.py:2756`
- `src/turn_contract.py:2854`
- `src/turn_contract.py:3310`
- `src/turn_contract.py:3490`
- `src/turn_contract.py:3989`
- `src/turn_contract.py:3990`
- `src/turn_contract.py:3996`
- `src/turn_contract.py:3996`
- `src/turn_contract.py:4061`
- `src/turn_contract.py:4465`
- `src/turn_contract.py:4560`
- `src/turn_contract.py:4596`
- `src/turn_contract.py:4625`
- `src/turn_contract.py:5572`
- `src/turn_contract.py:6324`
- `src/turn_contract.py:6329`
- `src/turn_contract.py:6329`
- `src/turn_contract.py:6365`
- `src/turn_contract.py:6367`
- `src/turn_contract.py:6369`
- `src/turn_contract.py:6408`
- … +18 more (grep the name in repo)

## `parse_action` — function, line 535
- **called from:**
- `scripts/eval_odysseus_contextual_tool_use.py:649`
- `scripts/eval_odysseus_contextual_tool_use.py:759`

## `_fixture_owner` — function, line 549
- **called from:**
- `scripts/eval_odysseus_contextual_tool_use.py:555`
- `scripts/eval_odysseus_tool_use.py:291`

## `_cleanup_crud_fixtures` — function, line 553
- **called from:**
- `scripts/eval_odysseus_contextual_tool_use.py:633`
- `scripts/eval_odysseus_contextual_tool_use.py:638`

## `_crud_fixture_cleanup` — function, line 631
- decorator: `contextlib.contextmanager`
- **called from:**
- `scripts/eval_odysseus_contextual_tool_use.py:878`

## `output_ok` — function, line 641
- **called from:**
- `scripts/eval_odysseus_contextual_tool_use.py:781`
- `scripts/eval_odysseus_crud.py:453`

## `event_action` — function, line 648
- **called from:**
- `scripts/eval_odysseus_contextual_tool_use.py:780`

## `create_session` — function, line 652
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

## `run_turn` — function, line 669
- **called from:**
- `scripts/eval_odysseus_contextual_tool_use.py:893`
- `scripts/odysseus_conversation_qa.py:798`
- `tests/test_odysseus_conversation_qa.py:137`

## `write_output` — function, line 827
- **called from:**
- `scripts/eval_odysseus_contextual_tool_use.py:935`
- `scripts/eval_odysseus_contextual_tool_use.py:938`
- `scripts/pr_blocker_audit.py:1043`

## `main` — function, line 846
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
