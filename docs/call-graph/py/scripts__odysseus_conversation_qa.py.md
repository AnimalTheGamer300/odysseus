# `scripts/odysseus_conversation_qa.py` — definitions & call sites

36 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `compact_tool_catalog` — function, line 224
- **called from:**
- `scripts/cook_sft_alex_conversations.py:218`
- `scripts/generate_sft_environment_expansion.py:170`
- `scripts/judge_seeded_harness_replay.py:92`
- `scripts/odysseus_conversation_qa.py:412`
- `scripts/odysseus_conversation_qa.py:902`
- `tests/test_odysseus_conversation_qa.py:818`
- `tests/test_odysseus_conversation_qa.py:1119`

## `TeacherEndpoint` — class, line 283
- decorator: `dataclass(frozen=True)`
- **called from:**
- `scripts/odysseus_conversation_qa.py:316`
- `scripts/odysseus_conversation_qa.py:1409`
- `tests/test_odysseus_conversation_qa.py:594`
- `tests/test_odysseus_conversation_qa.py:595`
- `tests/test_odysseus_conversation_qa.py:612`
- `tests/test_odysseus_conversation_qa.py:613`

## `_decrypt` — function, line 289
- **called from:**
- `mcp_servers/email_server.py:369`
- `mcp_servers/email_server.py:378`
- `routes/email/email_helpers.py:1215`
- `routes/email/email_helpers.py:1219`
- `routes/email/email_routes.py:7758`
- `routes/email/email_routes.py:7764`
- `scripts/odysseus_conversation_qa.py:313`

## `endpoint_from_db` — function, line 301
- **called from:**
- `scripts/cook_sft_alex_conversations.py:260`
- `scripts/odysseus_conversation_qa.py:1408`

## `_json_from_text` — function, line 319
- **called from:**
- `scripts/odysseus_conversation_qa.py:384`
- `tests/test_odysseus_conversation_qa.py:19`
- `tests/test_odysseus_conversation_qa.py:23`
- `tests/test_odysseus_conversation_qa.py:29`

## `teacher_json` — function, line 351
- **called from:**
- `scripts/cook_sft_alex_conversations.py:197`
- `scripts/odysseus_conversation_qa.py:396`
- `scripts/odysseus_conversation_qa.py:905`
- `scripts/odysseus_conversation_qa.py:925`

## `generate_flows` — function, line 394
- **called from:**
- `scripts/odysseus_conversation_qa.py:1440`

## `flows_from_file` — function, line 438
- **called from:**
- `scripts/odysseus_conversation_qa.py:1435`
- `scripts/odysseus_conversation_qa.py:1520`
- `tests/test_odysseus_conversation_qa.py:836`
- `tests/test_odysseus_conversation_qa.py:849`
- `tests/test_odysseus_conversation_qa.py:864`
- `tests/test_odysseus_conversation_qa.py:879`
- `tests/test_odysseus_conversation_qa.py:895`
- `tests/test_odysseus_conversation_qa.py:908`
- `tests/test_odysseus_conversation_qa.py:1153`

## `source_seed_id` — function, line 485
- **called from:**
- `scripts/build_odysseus_sft_repair_manifest.py:129`
- `scripts/odysseus_conversation_qa.py:478`
- `scripts/odysseus_conversation_qa.py:585`
- `scripts/odysseus_conversation_qa.py:632`
- `scripts/odysseus_conversation_qa.py:642`
- `scripts/odysseus_conversation_qa.py:642`
- `scripts/odysseus_conversation_qa.py:648`
- `scripts/odysseus_conversation_qa.py:1442`
- `scripts/odysseus_conversation_qa.py:1515`
- `scripts/odysseus_conversation_qa.py:1516`

## `flow_may_mutate` — function, line 490
- **called from:**
- `scripts/odysseus_conversation_qa.py:537`
- `scripts/odysseus_conversation_qa.py:1445`
- `scripts/odysseus_conversation_qa.py:1448`
- `scripts/odysseus_conversation_qa.py:1452`
- `scripts/odysseus_conversation_qa.py:1457`
- `scripts/odysseus_conversation_qa.py:1460`
- `tests/test_odysseus_conversation_qa.py:164`
- `tests/test_odysseus_conversation_qa.py:168`
- `tests/test_odysseus_conversation_qa.py:175`
- `tests/test_odysseus_conversation_qa.py:179`
- `tests/test_odysseus_conversation_qa.py:186`
- `tests/test_odysseus_conversation_qa.py:190`
- `tests/test_odysseus_conversation_qa.py:194`
- `tests/test_odysseus_conversation_qa.py:198`
- `tests/test_odysseus_conversation_qa.py:205`
- `tests/test_odysseus_conversation_qa.py:212`
- `tests/test_odysseus_conversation_qa.py:221`
- `tests/test_odysseus_conversation_qa.py:230`
- `tests/test_odysseus_conversation_qa.py:234`
- `tests/test_odysseus_conversation_qa.py:238`
- `tests/test_odysseus_conversation_qa.py:242`
- `tests/test_odysseus_conversation_qa.py:246`
- `tests/test_odysseus_conversation_qa.py:253`
- `tests/test_odysseus_conversation_qa.py:257`
- `tests/test_odysseus_conversation_qa.py:264`
- `tests/test_odysseus_conversation_qa.py:271`
- `tests/test_odysseus_conversation_qa.py:278`
- `tests/test_odysseus_conversation_qa.py:285`
- `tests/test_odysseus_conversation_qa.py:292`
- `tests/test_odysseus_conversation_qa.py:299`
- `tests/test_odysseus_conversation_qa.py:306`
- `tests/test_odysseus_conversation_qa.py:313`
- `tests/test_odysseus_conversation_qa.py:320`
- `tests/test_odysseus_conversation_qa.py:327`
- `tests/test_odysseus_conversation_qa.py:334`
- `tests/test_odysseus_conversation_qa.py:341`
- `tests/test_odysseus_conversation_qa.py:350`
- `tests/test_odysseus_conversation_qa.py:357`
- `tests/test_odysseus_conversation_qa.py:369`
- `tests/test_odysseus_conversation_qa.py:376`
- `tests/test_odysseus_conversation_qa.py:451`
- `tests/test_odysseus_conversation_qa.py:455`

## `positive_only` — function, line 504
- **called from:**
- `scripts/odysseus_conversation_qa.py:510`
- `scripts/odysseus_conversation_qa.py:511`

## `flow_has_locally_restorable_mutation` — function, line 534
- **called from:**
- `scripts/odysseus_conversation_qa.py:1452`
- `scripts/odysseus_conversation_qa.py:1457`
- `tests/test_odysseus_conversation_qa.py:386`
- `tests/test_odysseus_conversation_qa.py:390`
- `tests/test_odysseus_conversation_qa.py:394`
- `tests/test_odysseus_conversation_qa.py:398`
- `tests/test_odysseus_conversation_qa.py:402`

## `flow_has_orphaned_opening_followup` — function, line 542
- **called from:**
- `scripts/odysseus_conversation_qa.py:586`
- `tests/test_odysseus_conversation_qa.py:465`
- `tests/test_odysseus_conversation_qa.py:471`
- `tests/test_odysseus_conversation_qa.py:474`
- `tests/test_odysseus_conversation_qa.py:477`
- `tests/test_odysseus_conversation_qa.py:486`
- `tests/test_odysseus_conversation_qa.py:504`
- `tests/test_odysseus_conversation_qa.py:510`

## `flow_is_auditable` — function, line 568
- **called from:**
- `scripts/odysseus_conversation_qa.py:1443`
- `scripts/odysseus_conversation_qa.py:1523`
- `tests/test_odysseus_conversation_qa.py:503`
- `tests/test_odysseus_conversation_qa.py:516`
- `tests/test_odysseus_conversation_qa.py:520`
- `tests/test_odysseus_conversation_qa.py:527`
- `tests/test_odysseus_conversation_qa.py:531`
- `tests/test_odysseus_conversation_qa.py:538`
- `tests/test_odysseus_conversation_qa.py:542`
- `tests/test_odysseus_conversation_qa.py:546`
- `tests/test_odysseus_conversation_qa.py:553`

## `balanced_flows` — function, line 591
- **called from:**
- `scripts/odysseus_conversation_qa.py:1466`
- `tests/test_odysseus_conversation_qa.py:1017`
- `tests/test_odysseus_conversation_qa.py:1018`
- `tests/test_odysseus_conversation_qa.py:1030`

## `audited_source_seed_ids` — function, line 609
- **called from:**
- `scripts/odysseus_conversation_qa.py:1412`
- `tests/test_odysseus_conversation_qa.py:927`
- `tests/test_odysseus_conversation_qa.py:940`
- `tests/test_odysseus_conversation_qa.py:967`

## `write_coverage_manifest` — function, line 638
- **called from:**
- `scripts/odysseus_conversation_qa.py:1525`
- `tests/test_odysseus_conversation_qa.py:977`

## `latest_cookie` — function, line 670
- **called from:**
- `scripts/odysseus_conversation_qa.py:1434`

## `sse_events` — function, line 682
- **called from:**
- `scripts/odysseus_conversation_qa.py:756`
- `scripts/sft_email_overseer.py:541`

## `create_session` — function, line 708
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

## `run_turn` — function, line 736
- **called from:**
- `scripts/eval_odysseus_contextual_tool_use.py:893`
- `scripts/odysseus_conversation_qa.py:798`
- `tests/test_odysseus_conversation_qa.py:137`

## `compact_turn` — function, line 759
- **called from:**
- `scripts/odysseus_conversation_qa.py:801`
- `scripts/repair_sft_corpus_with_kimi.py:108`
- `tests/test_odysseus_conversation_qa.py:33`

## `replay_flow` — function, line 791
- **called from:**
- `scripts/odysseus_conversation_qa.py:838`
- `scripts/odysseus_conversation_qa.py:1477`
- `tests/test_odysseus_conversation_qa.py:1176`

## `replay_flows_with_fixture_isolation` — function, line 823
- **called from:**
- `scripts/odysseus_conversation_qa.py:1474`
- `tests/test_odysseus_conversation_qa.py:425`
- `tests/test_odysseus_conversation_qa.py:448`

## `_validated_judge_verdict` — function, line 847
- **called from:**
- `scripts/odysseus_conversation_qa.py:907`
- `scripts/odysseus_conversation_qa.py:929`

## `judge_flow` — function, line 878
- **called from:**
- `scripts/odysseus_conversation_qa.py:1181`
- `scripts/odysseus_conversation_qa.py:1185`
- `tests/test_odysseus_conversation_qa.py:641`
- `tests/test_odysseus_conversation_qa.py:664`
- `tests/test_odysseus_conversation_qa.py:683`

## `replay_transport_failure` — function, line 936
- **called from:**
- `scripts/odysseus_conversation_qa.py:469`
- `scripts/odysseus_conversation_qa.py:629`
- `scripts/odysseus_conversation_qa.py:1165`

## `normalize_judge_ownership` — function, line 959
- **called from:**
- `scripts/odysseus_conversation_qa.py:1181`
- `scripts/odysseus_conversation_qa.py:1185`
- `tests/test_odysseus_conversation_qa.py:1138`

## `ungrounded_visible_referent` — function, line 1106
- **called from:**
- `scripts/odysseus_conversation_qa.py:1177`
- `tests/test_odysseus_conversation_qa.py:61`
- `tests/test_odysseus_conversation_qa.py:79`

## `safe_judge_flow` — function, line 1163
- **called from:**
- `tests/test_odysseus_conversation_qa.py:564`
- `tests/test_odysseus_conversation_qa.py:574`
- `tests/test_odysseus_conversation_qa.py:597`
- `tests/test_odysseus_conversation_qa.py:615`
- `tests/test_odysseus_conversation_qa.py:696`
- `tests/test_odysseus_conversation_qa.py:712`
- `tests/test_odysseus_conversation_qa.py:726`
- `tests/test_odysseus_conversation_qa.py:747`
- `tests/test_odysseus_conversation_qa.py:764`
- `tests/test_odysseus_conversation_qa.py:781`
- `tests/test_odysseus_conversation_qa.py:797`

## `append_ledger` — function, line 1199
- **called from:**
- `scripts/odysseus_conversation_qa.py:1513`
- `tests/test_odysseus_conversation_qa.py:1000`

## `atomic_write_json` — function, line 1234
- **called from:**
- `routes/auth_routes.py:548`
- `routes/auth_routes.py:568`
- `routes/auth_routes.py:633`
- `routes/codex_routes.py:920`
- `routes/contacts/contacts_routes.py:47`
- `routes/contacts/contacts_routes.py:138`
- `routes/cookbook_routes.py:3383`
- `routes/cookbook_routes.py:3769`
- `routes/email/email_helpers.py:1146`
- `routes/prefs_routes.py:27`
- `scripts/odysseus_conversation_qa.py:1282`
- `scripts/odysseus_conversation_qa.py:1480`
- `scripts/odysseus_conversation_qa.py:1504`
- `services/memory/skills.py:122`
- `src/agent_jobs.py:111`
- `src/agent_runtime/authority.py:705`
- `src/agent_runtime/process_resources.py:425`
- `src/agent_runtime/process_resources.py:521`
- `src/bg_jobs.py:70`
- `src/builtin_actions.py:3662`
- `src/containment.py:450`
- `src/containment_worker.py:114`
- `src/cookbook_serve_lifecycle.py:186`
- `src/integrations.py:257`
- `src/preset_manager.py:124`
- `src/settings.py:291`
- `src/settings.py:391`
- `tests/process_resource_helpers.py:63`
- `tests/test_atomic_io.py:46`
- `tests/test_atomic_io.py:54`
- `tests/test_atomic_io.py:64`
- `tests/test_atomic_io.py:72`
- `tests/test_atomic_io.py:74`
- `tests/test_atomic_io.py:84`
- `tests/test_atomic_io.py:106`
- `tests/test_atomic_io.py:130`
- `tests/test_atomic_io.py:136`
- `tests/test_atomic_io.py:145`
- `tests/test_atomic_io.py:154`
- `tests/test_background_resource_identity.py:92`
- `tests/test_background_resource_identity.py:201`
- `tests/test_background_resource_identity.py:254`
- `tests/test_wave3_launch_cost_lifecycle.py:131`
- `tests/test_wave3_launch_cost_lifecycle.py:147`
- `tests/test_wave3_launch_cost_lifecycle.py:195`

## `judge_replayed_flows` — function, line 1244
- **called from:**
- `scripts/odysseus_conversation_qa.py:1497`
- `tests/test_odysseus_conversation_qa.py:1043`
- `tests/test_odysseus_conversation_qa.py:1066`
- `tests/test_odysseus_conversation_qa.py:1092`

## `resume_replay_rows` — function, line 1294
- **called from:**
- `scripts/odysseus_conversation_qa.py:1426`
- `tests/test_odysseus_conversation_qa.py:1109`

## `parse_args` — function, line 1309
- **called from:**
- `scripts/_lib/cli.py:112`
- `scripts/agent_migration_manifest.py:617`
- `scripts/agent_migration_manifest.py:621`
- `scripts/analyze_odysseus_eval_targets.py:120`
- `scripts/assemble_sft_clean_corpus.py:24`
- `scripts/audit_c5_benchmark_evidence.py:1558`
- `scripts/audit_email_sft_with_deepseek.py:246`
- `scripts/audit_historical_tool_routing.py:60`
- `scripts/audit_sft_corpus_with_deepseek.py:216`
- `scripts/audit_typo_tool_routing.py:60`
- `scripts/backfill_model_release_dates.py:63`
- `scripts/build_frontend.py:134`
- `scripts/build_historical_harness_queue.py:323`
- `scripts/build_odysseus_everyday_deepseek_heldout_cases.py:238`
- `scripts/build_odysseus_everyday_deepseek_heldout_v3_cases.py:309`
- `scripts/build_odysseus_realistic_web_synthesis_rows.py:285`
- `scripts/build_odysseus_search_teacher_edited_rows.py:211`
- `scripts/build_odysseus_sft_repair_manifest.py:208`
- `scripts/build_odysseus_sft_repair_manifest.py:212`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:416`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:427`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:454`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:476`
- `scripts/build_odysseus_v61_app_route_web_rows.py:252`
- `scripts/build_odysseus_v62_teacher_trace_web_rows.py:208`
- `scripts/build_odysseus_web_teacher_sft.py:378`
- `scripts/build_odysseus_web_v53_repair_sft.py:415`
- `scripts/build_sft_environment_inventories.py:54`
- `scripts/build_sft_expansion_manifest.py:74`
- `scripts/build_sft_expansion_splits.py:25`
- `scripts/build_v66_calendar_heldout_cases.py:49`
- `scripts/check_brotli.py:104`
- `scripts/check_ca_trust.py:139`
- `scripts/cook_sft_alex_conversations.py:248`
- `scripts/cook_sft_alex_conversations.py:252`
- `scripts/css_snapshot.py:247`
- `scripts/curate_public_search_seed_cases.py:262`
- `scripts/curate_sft_trace_run.py:157`
- `scripts/demo_email/seed_demo_emails.py:360`
- `scripts/diffusion_server.py:1492`
- `scripts/dump_agent_prompt.py:382`
- `scripts/eval_ajax_basic_tools.py:32`
- `scripts/eval_exact_file_routing.py:202`
- `scripts/eval_followup_domain_continuity.py:209`
- `scripts/eval_odysseus_app_route_smoke.py:360`
- `scripts/eval_odysseus_contextual_tool_use.py:861`
- `scripts/eval_odysseus_crud.py:800`
- `scripts/eval_odysseus_everyday_live_hard.py:586`
- `scripts/eval_odysseus_live_hard_direct.py:67`
- `scripts/eval_odysseus_live_hard_direct.py:232`
- `scripts/eval_odysseus_live_hard_examples.py:464`
- `scripts/eval_odysseus_tool_use.py:1377`
- `scripts/eval_qwen35_document_shape_direct.py:142`
- `scripts/eval_qwen35_document_shape_direct.py:262`
- `scripts/eval_qwen35_implicit_memory.py:206`
- `scripts/eval_qwen35_tool_router_extended.py:450`
- `scripts/eval_qwen_tool_groups_stream.py:226`
- `scripts/filter_sft_seed_hygiene.py:46`
- `scripts/generate_env_reference.py:1230`
- `scripts/generate_sft_environment_expansion.py:307`
- … +30 more (grep the name in repo)

## `main` — function, line 1387
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
