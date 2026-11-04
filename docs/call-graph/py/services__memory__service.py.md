# `services/memory/service.py` — definitions & call sites

11 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `Memory` — class, line 15
- decorator: `dataclass`
- **called from:**
- `services/memory/service.py:54`
- `services/memory/service.py:67`
- `static/js/tasks.js:444`

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
- `routes/email_routes.py:1455`
- `src/builtin_actions.py:428`
- `src/outbound_fetch.py:220`
- `tests/test_agent_state_dir_confinement.py:648`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_extraction_controls.py:14`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_retired_settings_interfaces.py:30`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:148`

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
- `app.py:1044`
- `app.py:1045`
- `core/auth.py:309`
- `core/database.py:2660`
- `core/session_manager.py:620`
- `core/session_manager.py:963`
- `core/session_manager.py:968`
- `core/session_manager.py:1120`
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
- `routes/auth_routes.py:660`
- `routes/auth_routes.py:800`
- `routes/calendar_routes.py:972`
- `routes/calendar_routes.py:1102`
- `routes/calendar_routes.py:1103`
- `routes/calendar_routes.py:1096`
- `routes/calendar_routes.py:1347`
- `routes/calendar_routes.py:1319`
- `routes/codex_routes.py:481`
- `routes/codex_routes.py:488`
- `routes/codex_routes.py:495`
- `routes/compare/compare_routes.py:359`
- `routes/compare/compare_routes.py:346`
- `routes/contacts/contacts_routes.py:709`
- `routes/contacts/contacts_routes.py:881`
- `routes/contacts/contacts_routes.py:908`
- `routes/cookbook_routes.py:1750`
- `routes/cookbook_routes.py:1897`
- `routes/cookbook_routes.py:1928`
- `routes/document/document_routes.py:737`
- `routes/document/document_routes.py:938`
- `routes/document/document_routes.py:950`
- `routes/document/document_routes.py:1041`
- `routes/editor_draft_routes.py:169`
- `routes/email_routes.py:3796`
- `routes/email_routes.py:3811`
- `routes/email_routes.py:3827`
- `routes/email_routes.py:4231`
- `routes/email_routes.py:4382`
- `routes/email_routes.py:4449`
- `routes/email_routes.py:5752`
- `routes/email_routes.py:5741`
- `routes/embedding_routes.py:211`
- `routes/embedding_routes.py:335`
- `routes/gallery/gallery_routes.py:1239`
- `routes/gallery/gallery_routes.py:1136`
- `routes/gallery/gallery_routes.py:2171`
- … +95 more (grep the name in repo)
