# `launcher.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `NullWriter` — class, line 25
- **called from:**
- `launcher.py:34`
- `launcher.py:36`
- `tests/test_launcher.py:21`

## `NullWriter.write` — method, line 26
- **called from:**
- `core/atomic_io.py:57`
- `mcp_servers/email_server.py:1213`
- `routes/codex_routes.py:229`
- `routes/codex_routes.py:905`
- `routes/cookbook_routes.py:877`
- `routes/cookbook_routes.py:878`
- `routes/email_helpers.py:1492`
- `routes/email_helpers.py:1620`
- `routes/email_routes.py:3364`
- `routes/email_routes.py:4029`
- `routes/email_routes.py:4053`
- `routes/email_routes.py:4176`
- `routes/gallery/gallery_routes.py:1032`
- `routes/memory/memory_routes.py:391`
- `routes/personal_routes.py:355`
- `routes/upload_routes.py:490`
- `routes/upload_routes.py:523`
- `scripts/_lib/cli.py:72`
- `scripts/_lib/cli.py:77`
- `scripts/_lib/cli.py:109`
- `scripts/_lib/cli.py:116`
- `scripts/agent_migration_manifest.py:630`
- `scripts/backfill_model_release_dates.py:125`
- `scripts/import_from_vllm_recipes.py:333`
- `scripts/migrate_searxng_settings.py:132`
- `scripts/pr_blocker_audit.py:124`
- `scripts/pr_blocker_audit.py:137`
- `scripts/pr_blocker_audit.py:143`
- `scripts/pr_blocker_audit.py:150`
- `scripts/pr_blocker_audit.py:1004`
- `scripts/pr_blocker_audit.py:1036`
- `scripts/pr_blocker_audit.py:1045`
- `services/stt/stt_service.py:98`
- `src/agent_loop.py:3193`
- `src/agent_tools/filesystem_tools.py:215`
- `src/agent_tools/filesystem_tools.py:329`
- `src/agent_tools/filesystem_tools.py:401`
- `src/api_key_manager.py:29`
- `src/chat_handler.py:280`
- `src/readiness.py:41`
- `src/tool_utils.py:94`
- `src/tools_doc.py:139`
- `src/tools_doc.py:152`
- `src/upload_handler.py:1384`
- `tests/test_api_key_file_permissions.py:40`
- `tests/test_code_nav_tools.py:23`
- `tests/test_code_nav_tools.py:26`
- `tests/test_code_nav_tools.py:29`
- `tests/test_code_nav_tools.py:32`
- `tests/test_code_nav_tools.py:36`
- `tests/test_code_nav_tools.py:117`
- `tests/test_code_nav_tools.py:119`
- `tests/test_code_nav_tools.py:121`
- `tests/test_code_nav_tools.py:200`
- `tests/test_cookbook_dead_download_status.py:63`
- `tests/test_cookbook_dead_download_status.py:68`
- `tests/test_edit_file.py:49`
- `tests/test_edit_file.py:63`
- `tests/test_edit_file.py:74`
- `tests/test_edit_file.py:83`
- … +27 more (grep the name in repo)

## `NullWriter.flush` — method, line 28
- **called from:**
- `core/atomic_io.py:37`
- `core/atomic_io.py:58`
- `core/database.py:518`
- `routes/calendar_routes.py:317`
- `routes/calendar_routes.py:325`
- `routes/email_routes.py:5756`
- `scripts/demo_email/demo_account.py:117`
- `scripts/demo_email/demo_account.py:165`
- `scripts/migrate_searxng_settings.py:133`
- `scripts/pr_blocker_audit.py:125`
- `scripts/pr_blocker_audit.py:138`
- `scripts/pr_blocker_audit.py:144`
- `scripts/pr_blocker_audit.py:151`
- `src/api_key_manager.py:94`
- `src/email_thread_parser.py:328`
- `src/email_thread_parser.py:334`
- `src/email_thread_parser.py:371`
- `src/email_thread_parser.py:385`
- `src/llm_core.py:3209`
- `src/llm_core.py:3227`
- `src/llm_core.py:3486`
- `src/llm_core.py:3728`
- `src/task_scheduler.py:2616`
- `src/upload_handler.py:745`
- `tests/test_atomic_io.py:101`
- `tests/test_launcher.py:24`
- `static/js/chat.js:2832`
- `static/js/emailLibrary.js:6387`
- `static/js/emailLibrary.js:6393`
- `static/js/emailLibrary.js:6398`
- `static/js/liveThinkingThrottle.js:18`
- `static/js/liveThinkingThrottle.js:191`

## `NullWriter.isatty` — method, line 30
- **called from:**
- `scripts/_lib/cli.py:65`
- `scripts/pr_blocker_audit.py:854`
- `scripts/pr_blocker_audit.py:868`
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
