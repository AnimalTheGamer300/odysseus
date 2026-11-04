# `src/memory_provider.py` — definitions & call sites

28 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `MemoryRecord` — class, line 11
- decorator: `dataclass`
- **called from:**
- `src/memory_provider.py:128`

## `MemorySearchHit` — class, line 25
- decorator: `dataclass`
- **called from:**
- `src/memory_provider.py:195`
- `src/memory_provider.py:210`

## `MemoryProvider` — class, line 33
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `MemoryProvider.initialize` — method (async), line 45
- **called from:**
- `src/mcp_manager.py:204`
- `src/mcp_manager.py:273`
- `src/mcp_manager.py:360`
- `static/js/markdown.js:91`

## `MemoryProvider.shutdown` — method (async), line 48
- **called from:**
- `mcp_servers/email_server.py:398`
- `mcp_servers/email_server.py:410`
- `routes/email_helpers.py:1181`
- `routes/email_helpers.py:1245`
- `src/service_health.py:180`
- `tests/test_caldav_redirect_hardening.py:83`
- `tests/test_caldav_redirect_hardening.py:84`
- `tests/test_webhook_dns_rebinding_pin.py:107`
- `tests/test_webhook_dns_rebinding_pin.py:156`

## `MemoryProvider.remember` — method (async), line 52
- decorator: `abstractmethod`
- **called from:**
- `services/memory/service.py:87`
- `tests/test_memory_imports.py:31`
- `tests/test_memory_provider.py:36`
- `tests/test_memory_provider.py:62`
- `tests/test_memory_provider.py:63`
- `tests/test_memory_provider.py:102`
- `tests/test_memory_store_unreadable_no_wipe.py:239`

## `MemoryProvider.recall` — method (async), line 65
- decorator: `abstractmethod`
- **called from:**
- `services/memory/service.py:102`
- `tests/test_memory_imports.py:38`
- `tests/test_memory_provider.py:69`
- `tests/test_memory_provider.py:90`
- `tests/test_memory_provider.py:108`
- `tests/test_memory_recall_nondict_rows.py:22`

## `MemoryProvider.list_memories` — method (async), line 75
- decorator: `abstractmethod`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `MemoryProvider.delete` — method (async), line 84
- decorator: `abstractmethod`
- **called from:**
- `app.py:1044`
- `app.py:1045`
- `core/auth.py:309`
- `core/database.py:2699`
- `core/session_manager.py:1092`
- `core/session_manager.py:1097`
- `core/session_manager.py:1348`
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
- `routes/gallery/gallery_routes.py:2161`
- … +97 more (grep the name in repo)

## `MemoryProvider.get_tool_schemas` — method, line 87
- **called from:**
- `src/memory_provider.py:285`
- `src/memory_provider.py:300`
- `tests/test_memory_provider.py:143`
- `tests/test_memory_provider.py:177`

## `MemoryProvider.handle_tool_call` — method (async), line 91
- **called from:**
- `src/memory_provider.py:312`

## `NativeMemoryProvider` — class, line 96
- **called from:**
- `services/memory/service.py:47`
- `src/app_initializer.py:125`
- `tests/test_memory_provider.py:34`
- `tests/test_memory_provider.py:60`
- `tests/test_memory_provider.py:82`
- `tests/test_memory_provider.py:101`
- `tests/test_memory_store_unreadable_no_wipe.py:236`

## `NativeMemoryProvider.__init__` — method, line 114
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

## `NativeMemoryProvider._to_record` — method, line 118
- **called from:**
- `src/memory_provider.py:171`
- `src/memory_provider.py:196`
- `src/memory_provider.py:211`
- `src/memory_provider.py:225`

## `NativeMemoryProvider.remember` — method (async), line 139
- **called from:**
- `services/memory/service.py:87`
- `tests/test_memory_imports.py:31`
- `tests/test_memory_provider.py:36`
- `tests/test_memory_provider.py:62`
- `tests/test_memory_provider.py:63`
- `tests/test_memory_provider.py:102`
- `tests/test_memory_store_unreadable_no_wipe.py:239`

## `NativeMemoryProvider.recall` — method (async), line 173
- **called from:**
- `services/memory/service.py:102`
- `tests/test_memory_imports.py:38`
- `tests/test_memory_provider.py:69`
- `tests/test_memory_provider.py:90`
- `tests/test_memory_provider.py:108`
- `tests/test_memory_recall_nondict_rows.py:22`

## `NativeMemoryProvider.list_memories` — method (async), line 218
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `NativeMemoryProvider.delete` — method (async), line 229
- **called from:**
- `app.py:1044`
- `app.py:1045`
- `core/auth.py:309`
- `core/database.py:2699`
- `core/session_manager.py:1092`
- `core/session_manager.py:1097`
- `core/session_manager.py:1348`
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
- `routes/gallery/gallery_routes.py:2161`
- … +97 more (grep the name in repo)

## `NativeMemoryProvider._vector_available` — method, line 254
- **called from:**
- `src/memory_provider.py:168`
- `src/memory_provider.py:183`
- `src/memory_provider.py:250`

## `MemoryProviderRegistry` — class, line 258
- **called from:**
- `src/app_initializer.py:124`
- `tests/test_memory_provider.py:138`
- `tests/test_memory_provider.py:171`

## `MemoryProviderRegistry.__init__` — method, line 261
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

## `MemoryProviderRegistry.register` — method, line 266
- **called from:**
- `src/memory_provider.py:264`
- `static/js/calendar.js:3503`
- `static/js/cookbook.js:3378`
- `static/js/document.js:6870`
- `static/js/editor/fx/adj-popup.js:226`
- `static/js/editor/history-panel.js:58`
- `static/js/emailLibrary.js:2694`
- `static/js/emailLibrary.js:7055`
- `static/js/gallery.js:2115`
- `static/js/modalManager.js:15`
- `static/js/modalManager.js:1141`
- `static/js/modalManager.js:1146`
- `static/js/modalManager.js:1329`
- `static/js/modalManager.js:1432`
- `static/js/notes.js:1620`

## `MemoryProviderRegistry.get` — method, line 271
- **called from:**
- `app.py:359`
- `app.py:383`
- `app.py:389`
- `app.py:416`
- `app.py:428`
- `app.py:470`
- `app.py:538`
- `app.py:512`
- `app.py:595`
- `app.py:891`
- `app.py:903`
- `app.py:907`
- `app.py:915`
- `app.py:919`
- `app.py:923`
- `app.py:927`
- `app.py:931`
- `app.py:935`
- `app.py:939`
- `app.py:944`
- `app.py:950`
- `app.py:955`
- `app.py:967`
- `app.py:968`
- `app.py:969`
- `app.py:969`
- `app.py:971`
- `app.py:971`
- `app.py:975`
- `app.py:996`
- `app.py:987`
- `app.py:998`
- `app.py:1117`
- `app.py:1151`
- `app.py:1165`
- `app.py:1198`
- `app.py:1201`
- `app.py:1216`
- `companion/pairing.py:116`
- `companion/pairing.py:126`
- `companion/pairing.py:173`
- `companion/pairing.py:177`
- `companion/routes.py:85`
- `companion/routes.py:97`
- `companion/routes.py:109`
- `companion/routes.py:168`
- `companion/routes.py:222`
- `core/auth.py:143`
- `core/auth.py:164`
- `core/auth.py:187`
- `core/auth.py:214`
- `core/auth.py:226`
- `core/auth.py:230`
- `core/auth.py:299`
- `core/auth.py:299`
- `core/auth.py:325`
- `core/auth.py:349`
- `core/auth.py:349`
- `core/auth.py:357`
- `core/auth.py:370`
- … +7551 more (grep the name in repo)

## `MemoryProviderRegistry.all` — method, line 274
- **called from:**
- `app.py:320`
- `app.py:1042`
- `app.py:1168`
- `companion/routes.py:141`
- `core/database.py:2804`
- `core/session_manager.py:99`
- `core/session_manager.py:137`
- `core/session_manager.py:150`
- `core/session_manager.py:264`
- `core/session_manager.py:630`
- `core/session_manager.py:702`
- `core/session_manager.py:799`
- `core/session_manager.py:1190`
- `core/session_manager.py:1329`
- `mcp_servers/email_server.py:926`
- `routes/api_token_routes.py:83`
- `routes/assistant_routes.py:145`
- `routes/assistant_routes.py:242`
- `routes/assistant_routes.py:257`
- `routes/auth_routes.py:395`
- `routes/auth_routes.py:407`
- `routes/calendar_routes.py:1125`
- `routes/calendar_routes.py:1183`
- `routes/calendar_routes.py:1570`
- `routes/chat_helpers.py:534`
- `routes/chat_helpers.py:609`
- `routes/chat_routes.py:595`
- `routes/chat_routes.py:660`
- `routes/chat_routes.py:729`
- `routes/chat_routes.py:844`
- `routes/compare/compare_routes.py:329`
- `routes/cookbook_routes.py:1890`
- `routes/cookbook_routes.py:1921`
- `routes/document/document_routes.py:147`
- `routes/document/document_routes.py:359`
- `routes/document/document_routes.py:416`
- `routes/document/document_routes.py:463`
- `routes/document/document_routes.py:586`
- `routes/document/document_routes.py:775`
- `routes/document/document_routes.py:865`
- `routes/document/document_routes.py:948`
- `routes/document/document_routes.py:992`
- `routes/document/document_routes.py:1454`
- `routes/document/document_routes.py:1540`
- `routes/document/document_routes.py:1589`
- `routes/document/document_routes.py:1678`
- `routes/document/document_routes.py:1721`
- `routes/editor_draft_routes.py:89`
- `routes/email_helpers.py:1134`
- `routes/email_pollers.py:463`
- `routes/email_routes.py:1315`
- `routes/email_routes.py:5622`
- `routes/gallery/gallery_routes.py:300`
- `routes/gallery/gallery_routes.py:313`
- `routes/gallery/gallery_routes.py:661`
- `routes/gallery/gallery_routes.py:694`
- `routes/gallery/gallery_routes.py:707`
- `routes/gallery/gallery_routes.py:769`
- `routes/gallery/gallery_routes.py:776`
- `routes/gallery/gallery_routes.py:791`
- … +282 more (grep the name in repo)

## `MemoryProviderRegistry.active` — method, line 277
- **called from:**
- `src/memory_provider.py:284`
- `src/memory_provider.py:299`
- `tests/test_rename_user_owner_sync.py:304`
- `tests/test_rename_user_owner_sync.py:307`
- `static/app.js:988`
- `static/app.js:989`
- `static/js/chat.js:5195`
- `static/js/document.js:1333`
- `static/js/gallery.js:2504`
- `static/js/gallery.js:2603`
- `static/js/notes.js:4156`

## `MemoryProviderRegistry.get_tool_schemas` — method, line 280
- **called from:**
- `src/memory_provider.py:285`
- `src/memory_provider.py:300`
- `tests/test_memory_provider.py:143`
- `tests/test_memory_provider.py:177`

## `MemoryProviderRegistry.handle_tool_call` — method (async), line 297
- **called from:**
- `src/memory_provider.py:312`

## `MemoryProviderRegistry._tool_name` — method, line 316
- decorator: `staticmethod`
- **called from:**
- `src/memory_provider.py:286`
- `src/memory_provider.py:301`
