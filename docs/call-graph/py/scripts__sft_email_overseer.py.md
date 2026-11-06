# `scripts/sft_email_overseer.py` — definitions & call sites

35 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `read_json` — function, line 116
- **called from:**
- `scripts/agent_migration_manifest.py:115`
- `scripts/agent_migration_manifest.py:292`
- `scripts/sft_email_overseer.py:145`
- `scripts/sft_email_overseer.py:637`

## `write_json` — function, line 120
- **called from:**
- `scripts/sft_email_overseer.py:153`
- `scripts/sft_email_overseer.py:433`
- `scripts/sft_email_overseer.py:723`

## `db` — function, line 125
- **called from:**
- `scripts/audit_email_sft_with_deepseek.py:249`
- `scripts/repair_email_sft_with_kimi.py:198`
- `scripts/sft_email_overseer.py:302`
- `scripts/sft_email_overseer.py:574`
- `scripts/sft_email_overseer.py:585`

## `latest_deepseek_audit` — function, line 131
- **called from:**
- `scripts/sft_email_overseer.py:285`
- `scripts/sft_email_overseer.py:729`

## `repair_artifact_paths` — function, line 138
- **called from:**
- `scripts/sft_email_overseer.py:290`

## `fixture_rows` — function, line 144
- **called from:**
- `scripts/sft_email_overseer.py:250`
- `scripts/sft_email_overseer.py:728`

## `save_fixture_rows` — function, line 152
- **called from:**
- `scripts/sft_email_overseer.py:279`

## `owner_counts` — function, line 156
- **called from:**
- `scripts/sft_email_overseer.py:255`
- `scripts/sft_email_overseer.py:265`
- `scripts/sft_email_overseer.py:734`

## `account_counts` — function, line 160
- **called from:**
- `scripts/sft_email_overseer.py:735`

## `transform_text` — function, line 169
- **called from:**
- `scripts/sft_email_overseer.py:232`
- `scripts/sft_email_overseer.py:235`
- `scripts/sft_email_overseer.py:244`
- `scripts/sft_email_overseer.py:375`

## `transform_email_address` — function, line 193
- **called from:**
- `scripts/sft_email_overseer.py:235`

## `retarget_row` — function, line 201
- **called from:**
- `scripts/sft_email_overseer.py:263`

## `seed_target_fixtures` — function, line 249
- **called from:**
- `scripts/sft_email_overseer.py:786`

## `load_audit_rows` — function, line 284
- **called from:**
- `scripts/sft_email_overseer.py:317`
- `scripts/sft_email_overseer.py:729`

## `load_repair_rows` — function, line 288
- **called from:**
- `scripts/sft_email_overseer.py:318`
- `scripts/sft_email_overseer.py:730`

## `session_user_messages` — function, line 301
- **called from:**
- `scripts/sft_email_overseer.py:325`

## `usable_seed_records` — function, line 316
- **called from:**
- `scripts/sft_email_overseer.py:385`
- `scripts/sft_email_overseer.py:732`

## `seed_is_standalone` — function, line 365
- **called from:**
- `scripts/sft_email_overseer.py:386`

## `retarget_prompt` — function, line 374
- **called from:**
- `scripts/sft_email_overseer.py:392`

## `build_plan` — function, line 384
- **called from:**
- `scripts/sft_email_overseer.py:790`

## `write_plan` — function, line 431
- **called from:**
- `scripts/sft_email_overseer.py:791`

## `login` — function, line 437
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

## `create_session` — function, line 448
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

## `sse_events` — function, line 474
- **called from:**
- `scripts/odysseus_conversation_qa.py:756`
- `scripts/sft_email_overseer.py:541`

## `event_text` — function, line 504
- **called from:**
- `scripts/sft_email_overseer.py:546`

## `stream_turn` — function, line 512
- **called from:**
- `scripts/run_sft_environment_expansion.py:702`
- `scripts/run_sft_overnight_fixture_flows.py:571`
- `scripts/sft_email_overseer.py:668`

## `tool_names` — function, line 563
- **called from:**
- `scripts/run_sft_environment_expansion.py:407`
- `scripts/run_sft_environment_expansion.py:711`
- `scripts/run_sft_overnight_fixture_flows.py:269`
- `scripts/run_sft_overnight_fixture_flows.py:594`
- `scripts/sft_email_overseer.py:685`

## `assistant_count` — function, line 573
- **called from:**
- `scripts/sft_email_overseer.py:667`

## `latest_assistant_from_db` — function, line 584
- **called from:**
- `scripts/sft_email_overseer.py:678`

## `persisted_tool_names` — function, line 614
- **called from:**
- `scripts/sft_email_overseer.py:680`

## `score_run` — function, line 618
- **called from:**
- `scripts/sft_email_overseer.py:689`

## `run_plan` — function, line 636
- **called from:**
- `scripts/sft_email_overseer.py:795`

## `status` — function, line 727
- **called from:**
- `routes/auth_routes.py:232`
- `scripts/sft_email_overseer.py:783`
- `static/js/skills.js:1585`
- `static/js/tasks.js:2792`

## `parse_targets` — function, line 743
- **called from:**
- `scripts/sft_email_overseer.py:640`
- `scripts/sft_email_overseer.py:786`
- `scripts/sft_email_overseer.py:790`

## `main` — function, line 753
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
