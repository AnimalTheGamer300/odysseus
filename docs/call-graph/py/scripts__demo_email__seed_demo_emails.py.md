# `scripts/demo_email/seed_demo_emails.py` — definitions & call sites

11 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_connect` — function, line 56
- **called from:**
- `scripts/demo_email/seed_demo_emails.py:363`
- `tests/test_chatgpt_subscription_routes.py:94`
- `tests/test_chatgpt_subscription_routes.py:95`
- `tests/test_chatgpt_subscription_routes.py:125`
- `tests/test_chatgpt_subscription_routes.py:126`
- `tests/test_chatgpt_subscription_routes.py:127`
- `tests/test_chatgpt_subscription_routes.py:137`
- `tests/test_chatgpt_subscription_routes.py:139`
- `tests/test_chatgpt_subscription_routes.py:141`
- `tests/test_chatgpt_subscription_routes.py:147`
- `tests/test_chatgpt_subscription_routes.py:151`
- `tests/test_chatgpt_subscription_routes.py:156`
- `tests/test_chatgpt_subscription_routes.py:157`
- `tests/test_chatgpt_subscription_routes.py:159`
- `tests/test_chatgpt_subscription_routes.py:179`
- `tests/test_chatgpt_subscription_routes.py:195`
- `tests/test_chatgpt_subscription_routes.py:197`
- `tests/test_chatgpt_subscription_routes.py:229`
- `tests/test_chatgpt_subscription_routes.py:454`
- `tests/test_chatgpt_subscription_routes.py:455`
- `tests/test_chatgpt_subscription_routes.py:480`
- `tests/test_chatgpt_subscription_routes.py:481`
- `tests/test_chatgpt_subscription_routes.py:528`
- `tests/test_chatgpt_subscription_routes.py:529`

## `_tiny_pdf` — function, line 64
- **called from:**
- `scripts/demo_email/seed_demo_emails.py:209`

## `_ics` — function, line 93
- **called from:**
- `scripts/demo_email/seed_demo_emails.py:222`
- `tests/test_calendar_import_zero_duration.py:100`
- `tests/test_calendar_import_zero_duration.py:114`
- `tests/test_calendar_import_zero_duration.py:153`
- `tests/test_calendar_import_zero_duration.py:167`

## `_msg` — function, line 109
- **called from:**
- `scripts/demo_email/seed_demo_emails.py:143`
- `scripts/demo_email/seed_demo_emails.py:159`
- `scripts/demo_email/seed_demo_emails.py:173`
- `scripts/demo_email/seed_demo_emails.py:185`
- `scripts/demo_email/seed_demo_emails.py:192`
- `scripts/demo_email/seed_demo_emails.py:202`
- `scripts/demo_email/seed_demo_emails.py:214`
- `scripts/demo_email/seed_demo_emails.py:225`
- `scripts/demo_email/seed_demo_emails.py:234`
- `scripts/demo_email/seed_demo_emails.py:244`

## `build_dataset` — function, line 134
- **called from:**
- `scripts/demo_email/seed_demo_emails.py:377`

## `add` — function, line 138
- **called from:**
- `companion/pairing.py:196`
- `core/database.py:554`
- `core/database.py:2269`
- `core/platform_compat.py:227`
- `core/session_manager.py:418`
- `core/session_manager.py:480`
- `core/session_manager.py:714`
- `core/session_manager.py:763`
- `core/session_manager.py:950`
- `mcp_servers/email_server.py:65`
- `mcp_servers/email_server.py:582`
- `mcp_servers/email_server.py:1027`
- `mcp_servers/email_server.py:1261`
- `mcp_servers/email_server.py:1345`
- `mcp_servers/email_server.py:2037`
- `mcp_servers/email_server.py:2224`
- `mcp_servers/email_server.py:2859`
- `mcp_servers/email_server.py:2905`
- `mcp_servers/email_server.py:2906`
- `mcp_servers/email_server.py:3075`
- `mcp_servers/email_server.py:3435`
- `mcp_servers/email_server.py:3441`
- `mcp_servers/email_server.py:3502`
- `mcp_servers/image_gen_server.py:144`
- `mcp_servers/memory_server.py:190`
- `mcp_servers/memory_server.py:219`
- `routes/api_token_routes.py:135`
- `routes/api_token_routes.py:179`
- `routes/backup_routes.py:105`
- `routes/backup_routes.py:176`
- `routes/backup_routes.py:178`
- `routes/backup_routes.py:179`
- `routes/calendar_routes.py:202`
- `routes/calendar_routes.py:330`
- `routes/calendar_routes.py:338`
- `routes/calendar_routes.py:760`
- `routes/calendar_routes.py:1390`
- `routes/calendar_routes.py:1545`
- `routes/calendar_routes.py:1612`
- `routes/calendar_routes.py:1713`
- `routes/chat_helpers.py:371`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:3587`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3924`
- `routes/chatgpt_subscription_routes.py:91`
- `routes/chatgpt_subscription_routes.py:155`
- `routes/chatgpt_subscription_routes.py:185`
- `routes/compare/compare_routes.py:218`
- `routes/compare/compare_routes.py:313`
- `routes/contacts/contacts_routes.py:590`
- `routes/contacts/contacts_routes.py:718`
- `routes/cookbook_routes.py:1479`
- `routes/cookbook_routes.py:1837`
- `routes/cookbook_routes.py:2885`
- `routes/cookbook_routes.py:3694`
- `routes/cookbook_routes.py:3761`
- `routes/cookbook_routes.py:3877`
- `routes/cookbook_routes.py:3964`
- `routes/copilot_routes.py:77`
- … +2017 more (grep the name in repo)

## `_seed_cache` — function, line 254
- **called from:**
- `scripts/demo_email/seed_demo_emails.py:382`

## `_clear_cache` — function, line 297
- **called from:**
- `scripts/demo_email/seed_demo_emails.py:372`

## `_ensure_mailbox` — function, line 313
- **called from:**
- `scripts/demo_email/seed_demo_emails.py:379`

## `_wipe` — function, line 321
- **called from:**
- `scripts/demo_email/seed_demo_emails.py:371`

## `main` — function, line 356
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
