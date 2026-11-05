# `services/memory/service.py` — definitions & call sites

11 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `Memory` — class, line 15
- decorator: `dataclass`
- **called from:**
- `scripts/run_sft_environment_expansion.py:123`
- `services/memory/service.py:54`
- `services/memory/service.py:67`
- `static/js/tasks.js:451`

## `MemorySearchResult` — class, line 25
- decorator: `dataclass`
- **called from:**
- `services/memory/service.py:109`

## `MemoryService` — class, line 32
- **called from:**
- `tests/test_memory_imports.py:29`
- `tests/test_memory_recall_nondict_rows.py:20`

## `MemoryService.__init__` — method, line 42
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email/email_helpers.py:205`
- `routes/email/email_helpers.py:220`
- `routes/email/email_helpers.py:232`
- `routes/email/email_helpers.py:248`
- `routes/email/email_routes.py:1664`
- `scripts/css_snapshot.py:194`
- `scripts/probe_browser_budget.py:56`
- `src/agent_tools/document_tools.py:759`
- `src/agent_tools/filesystem_tools.py:384`
- `src/builtin_actions.py:552`
- `src/chatgpt_subscription.py:495`
- `src/containment.py:170`
- `src/outbound_fetch.py:220`
- `src/path_confinement.py:81`
- `src/process_ownership.py:110`
- `src/report_math.py:31`
- `tests/conftest.py:199`
- `tests/test_admin_routes_auth_disabled.py:16`
- `tests/test_agent_state_dir_confinement.py:799`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_action_planning.py:11`
- `tests/test_deep_research_browser_fallback.py:10`
- `tests/test_deep_research_browser_fallback.py:29`
- `tests/test_deep_research_browser_fallback.py:56`
- `tests/test_deep_research_extraction_controls.py:13`
- `tests/test_deep_research_full_loop_navigation.py:11`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_llm_core_streaming.py:50`
- `tests/test_retired_settings_interfaces.py:31`
- `tests/test_searxng_ca_validation.py:35`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:155`

## `MemoryService._sync_provider` — method, line 49
- **called from:**
- `services/memory/service.py:86`
- `services/memory/service.py:101`

## `MemoryService._to_memory` — method, line 53
- decorator: `staticmethod`
- **called from:**
- `services/memory/service.py:114`

## `MemoryService._record_to_memory` — method, line 63
- decorator: `staticmethod`
- **called from:**
- `services/memory/service.py:88`
- `services/memory/service.py:104`
- `services/memory/service.py:106`

## `MemoryService.remember` — method (async), line 75
- **called from:**
- `services/memory/service.py:87`
- `tests/test_memory_imports.py:31`
- `tests/test_memory_provider.py:36`
- `tests/test_memory_provider.py:62`
- `tests/test_memory_provider.py:63`
- `tests/test_memory_provider.py:102`
- `tests/test_memory_store_unreadable_no_wipe.py:239`

## `MemoryService.recall` — method (async), line 90
- **called from:**
- `services/memory/service.py:102`
- `tests/test_memory_imports.py:38`
- `tests/test_memory_provider.py:69`
- `tests/test_memory_provider.py:90`
- `tests/test_memory_provider.py:108`
- `tests/test_memory_recall_nondict_rows.py:22`

## `MemoryService.get_all` — method, line 111
- **called from:**
- `routes/backup_routes.py:29`
- `routes/backup_routes.py:185`
- `tests/test_memory_imports.py:35`
- `tests/test_memory_imports.py:43`

## `MemoryService.delete` — method, line 116
- **called from:**
- `app.py:1208`
- `app.py:1209`
- `core/auth.py:327`
- `core/auth.py:472`
- `core/database.py:3015`
- `core/session_manager.py:636`
- `core/session_manager.py:994`
- `core/session_manager.py:999`
- `core/session_manager.py:1151`
- `routes/admin_wipe/admin_wipe_routes.py:80`
- `routes/admin_wipe/admin_wipe_routes.py:81`
- `routes/admin_wipe/admin_wipe_routes.py:91`
- `routes/admin_wipe/admin_wipe_routes.py:128`
- `routes/admin_wipe/admin_wipe_routes.py:134`
- `routes/admin_wipe/admin_wipe_routes.py:136`
- `routes/admin_wipe/admin_wipe_routes.py:142`
- `routes/admin_wipe/admin_wipe_routes.py:144`
- `routes/admin_wipe/admin_wipe_routes.py:150`
- `routes/admin_wipe/admin_wipe_routes.py:151`
- `routes/admin_wipe/admin_wipe_routes.py:160`
- `routes/admin_wipe/admin_wipe_routes.py:162`
- `routes/admin_wipe/admin_wipe_routes.py:71`
- `routes/api_token_routes.py:205`
- `routes/api_token_routes.py:195`
- `routes/auth_routes.py:721`
- `routes/auth_routes.py:950`
- `routes/calendar_routes.py:727`
- `routes/calendar_routes.py:1112`
- `routes/calendar_routes.py:1239`
- `routes/calendar_routes.py:1240`
- `routes/calendar_routes.py:1233`
- `routes/calendar_routes.py:1518`
- `routes/calendar_routes.py:1487`
- `routes/codex_routes.py:527`
- `routes/codex_routes.py:534`
- `routes/codex_routes.py:541`
- `routes/compare/compare_routes.py:359`
- `routes/compare/compare_routes.py:346`
- `routes/contacts/contacts_routes.py:837`
- `routes/contacts/contacts_routes.py:1020`
- `routes/contacts/contacts_routes.py:1055`
- `routes/cookbook_routes.py:1658`
- `routes/document/document_routes.py:961`
- `routes/document/document_routes.py:1162`
- `routes/document/document_routes.py:1174`
- `routes/document/document_routes.py:1265`
- `routes/editor_draft_routes.py:228`
- `routes/email/email_routes.py:5275`
- `routes/email/email_routes.py:5326`
- `routes/email/email_routes.py:5458`
- `routes/email/email_routes.py:5865`
- `routes/email/email_routes.py:6016`
- `routes/email/email_routes.py:6083`
- `routes/email/email_routes.py:7541`
- `routes/email/email_routes.py:7530`
- `routes/embedding_routes.py:211`
- `routes/embedding_routes.py:335`
- `routes/gallery/gallery_routes.py:1749`
- `routes/gallery/gallery_routes.py:1646`
- `routes/gallery/gallery_routes.py:3053`
- … +224 more (grep the name in repo)
