# `launcher.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `NullWriter` — class, line 25
- **called from:**
- `launcher.py:34`
- `launcher.py:36`
- `tests/test_launcher.py:21`

## `NullWriter.write` — method, line 26
- **called from:**
- `core/atomic_io.py:42`
- `core/atomic_io.py:96`
- `mcp_servers/email_server.py:2401`
- `routes/auth_routes.py:852`
- `routes/chat_helpers.py:246`
- `routes/chat_helpers.py:284`
- `routes/chat_helpers.py:288`
- `routes/chat_helpers.py:348`
- `routes/chat_helpers.py:351`
- `routes/codex_routes.py:275`
- `routes/codex_routes.py:951`
- `routes/cookbook_routes.py:751`
- `routes/cookbook_routes.py:752`
- `routes/email/email_helpers.py:1639`
- `routes/email/email_helpers.py:1767`
- `routes/email/email_routes.py:4199`
- `routes/email/email_routes.py:5663`
- `routes/email/email_routes.py:5687`
- `routes/email/email_routes.py:5810`
- `routes/gallery/gallery_routes.py:1542`
- `routes/history/history_routes.py:90`
- `routes/history/history_routes.py:95`
- `routes/memory/memory_routes.py:395`
- `routes/personal_routes.py:341`
- `routes/upload_routes.py:608`
- `routes/upload_routes.py:635`
- `scripts/_lib/cli.py:72`
- `scripts/_lib/cli.py:77`
- `scripts/_lib/cli.py:109`
- `scripts/_lib/cli.py:116`
- `scripts/agent_migration_manifest.py:630`
- `scripts/audit_c5_benchmark_evidence.py:1247`
- `scripts/audit_email_sft_with_deepseek.py:278`
- `scripts/audit_sft_corpus_with_deepseek.py:283`
- `scripts/audit_sft_corpus_with_deepseek.py:320`
- `scripts/backfill_model_release_dates.py:128`
- `scripts/cook_sft_alex_conversations.py:234`
- `scripts/curate_sft_trace_run.py:141`
- `scripts/eval_exact_file_routing.py:157`
- `scripts/import_from_vllm_recipes.py:340`
- `scripts/migrate_searxng_settings.py:132`
- `scripts/odysseus_conversation_qa.py:1231`
- `scripts/odysseus_domain_audit.py:509`
- `scripts/odysseus_domain_audit.py:522`
- `scripts/odysseus_related_flow_audit.py:769`
- `scripts/odysseus_related_flow_audit.py:784`
- `scripts/odysseus_remaining_tool_audit.py:308`
- `scripts/odysseus_remaining_tool_audit.py:316`
- `scripts/pr_blocker_audit.py:124`
- `scripts/pr_blocker_audit.py:137`
- `scripts/pr_blocker_audit.py:143`
- `scripts/pr_blocker_audit.py:150`
- `scripts/pr_blocker_audit.py:1004`
- `scripts/pr_blocker_audit.py:1036`
- `scripts/pr_blocker_audit.py:1045`
- `scripts/probe_browser_budget.py:104`
- `scripts/probe_empty_search_recovery.py:85`
- `scripts/repair_email_sft_with_kimi.py:234`
- `scripts/repair_sft_corpus_with_kimi.py:228`
- `scripts/repair_sft_corpus_with_kimi.py:231`
- … +118 more (grep the name in repo)

## `NullWriter.flush` — method, line 28
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
- `src/llm_core.py:3669`
- `src/llm_core.py:3687`
- `src/llm_core.py:3971`
- `src/llm_core.py:4308`
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

## `NullWriter.isatty` — method, line 30
- **called from:**
- `scripts/_lib/cli.py:65`
- `scripts/pr_blocker_audit.py:854`
- `scripts/pr_blocker_audit.py:868`
- `scripts/ref_parity_audit.py:571`
- `tests/test_launcher.py:25`

## `show_splash_instantly` — function, line 45
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_tray_image` — function, line 76
- **called from:**
- `launcher.py:103`
- `tests/test_launcher.py:31`

## `on_open_browser` — function, line 91
- **called from:**
- `launcher.py:105`
- `tests/test_launcher.py:43`

## `on_exit` — function, line 95
- **called from:**
- `tests/test_launcher.py:51`

## `setup_system_tray` — function, line 100
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `open_browser` — function, line 119
- **called from:**
- `tests/test_launcher.py:62`
- `tests/test_launcher.py:71`
