# `scripts/demo_email/seed_demo_emails.py` — definitions & call sites

11 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_connect` — function, line 56
- **called from:**
- `scripts/demo_email/seed_demo_emails.py:363`

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
- `core/database.py:524`
- `core/database.py:2010`
- `core/platform_compat.py:205`
- `core/session_manager.py:416`
- `core/session_manager.py:478`
- `core/session_manager.py:807`
- `core/session_manager.py:856`
- `core/session_manager.py:1053`
- `mcp_servers/email_server.py:552`
- `mcp_servers/email_server.py:1665`
- `mcp_servers/email_server.py:1706`
- `mcp_servers/email_server.py:1707`
- `mcp_servers/email_server.py:1828`
- `mcp_servers/image_gen_server.py:143`
- `mcp_servers/memory_server.py:190`
- `mcp_servers/memory_server.py:219`
- `routes/api_token_routes.py:135`
- `routes/api_token_routes.py:179`
- `routes/backup_routes.py:105`
- `routes/backup_routes.py:176`
- `routes/backup_routes.py:178`
- `routes/backup_routes.py:179`
- `routes/calendar_routes.py:190`
- `routes/calendar_routes.py:316`
- `routes/calendar_routes.py:324`
- `routes/calendar_routes.py:1253`
- `routes/calendar_routes.py:1374`
- `routes/calendar_routes.py:1441`
- `routes/calendar_routes.py:1540`
- `routes/chat_helpers.py:86`
- `routes/chat_routes.py:1688`
- `routes/chat_routes.py:1742`
- `routes/chatgpt_subscription_routes.py:54`
- `routes/chatgpt_subscription_routes.py:79`
- `routes/compare/compare_routes.py:218`
- `routes/compare/compare_routes.py:313`
- `routes/contacts/contacts_routes.py:476`
- `routes/contacts/contacts_routes.py:604`
- `routes/cookbook_routes.py:1579`
- `routes/cookbook_routes.py:1916`
- `routes/cookbook_routes.py:3006`
- `routes/cookbook_routes.py:3788`
- `routes/cookbook_routes.py:3855`
- `routes/cookbook_routes.py:3971`
- `routes/cookbook_routes.py:4058`
- `routes/copilot_routes.py:77`
- `routes/device_flow.py:154`
- `routes/document/document_routes.py:165`
- `routes/document/document_routes.py:201`
- `routes/document/document_routes.py:202`
- `routes/document/document_routes.py:545`
- `routes/document/document_routes.py:604`
- `routes/document/document_routes.py:683`
- `routes/document/document_routes.py:839`
- `routes/editor_draft_routes.py:126`
- `routes/email_helpers.py:1700`
- `routes/email_helpers.py:1732`
- `routes/email_helpers.py:1868`
- `routes/email_pollers.py:810`
- … +1237 more (grep the name in repo)

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
- `scripts/add_hwfit_models.py:422`
- `scripts/agent_migration_manifest.py:635`
- `scripts/backfill_model_release_dates.py:133`
- `scripts/claim_ownerless.py:106`
- `scripts/demo_email/seed_demo_emails.py:394`
- `scripts/dump_agent_prompt.py:545`
- `scripts/hf_download.py:182`
- `scripts/import_from_vllm_recipes.py:341`
- `scripts/index_documents.py:117`
- `scripts/migrate_searxng_settings.py:166`
- `scripts/mlx_image_server.py:470`
- `scripts/pr_blocker_audit.py:1051`
- `tests/run_focus.py:325`
- `tests/run_order_report.py:156`
- `tests/test_agent_migration_manifest.py:302`
- `tests/test_agent_migration_manifest.py:325`
- `tests/test_app.py:98`
- `tests/test_backup_import_skills_dedup.py:112`
- `tests/test_pr_blocker_audit.py:219`
- `tests/test_pr_blocker_audit.py:230`
- `tests/test_pr_blocker_audit.py:255`
- `tests/test_pr_blocker_audit.py:270`
- `tests/test_pr_blocker_audit.py:289`
- `tests/test_pr_blocker_audit.py:307`
- `tests/test_pr_blocker_audit.py:324`
- `tests/test_pr_blocker_audit.py:342`
- `tests/test_pr_blocker_audit.py:362`
- `tests/test_pr_blocker_audit.py:383`
- `tests/test_pr_blocker_audit.py:704`
- `tests/test_pr_blocker_audit.py:716`
- `tests/test_pr_blocker_audit.py:753`
- `tests/test_pr_blocker_audit.py:763`
- `tests/test_pr_blocker_audit.py:802`
- `tests/test_pr_blocker_audit.py:815`
- `tests/test_pr_blocker_audit.py:835`
- `tests/test_pr_blocker_audit.py:853`
- `tests/test_pr_blocker_audit.py:870`
- `tests/test_pr_blocker_audit.py:892`
- `tests/test_pr_blocker_audit.py:919`
- `tests/test_pr_blocker_audit.py:947`
- `tests/test_rag_search_signature.py:22`
- `tests/test_research_session_id_validation.py:55`
- `tests/test_setup_admin_user.py:61`
- `tests/tools/build_oversized_test_split_plan.py:574`
