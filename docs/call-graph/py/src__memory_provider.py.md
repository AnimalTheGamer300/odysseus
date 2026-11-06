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
- `src/mcp_manager.py:232`
- `src/mcp_manager.py:302`
- `src/mcp_manager.py:391`
- `static/js/markdown.js:91`

## `MemoryProvider.shutdown` — method (async), line 48
- **called from:**
- `mcp_servers/email_server.py:428`
- `mcp_servers/email_server.py:440`
- `routes/email/email_helpers.py:1327`
- `routes/email/email_helpers.py:1392`
- `scripts/css_snapshot.py:214`
- `scripts/css_snapshot.py:261`
- `src/service_health.py:194`
- `tests/conftest.py:241`
- `tests/smoke/stub_provider.py:164`
- `tests/test_caldav_redirect_hardening.py:118`
- `tests/test_caldav_redirect_hardening.py:119`
- `tests/test_css_computed_style_snapshot.py:98`
- `tests/test_css_computed_style_snapshot.py:170`
- `tests/test_editor_planner_ssrf_authorization.py:45`
- `tests/test_gallery_endpoint_enforcement.py:45`
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

## `MemoryProviderRegistry.register` — method, line 266
- **called from:**
- `routes/research/research_routes.py:628`
- `src/memory_provider.py:264`
- `src/report_math.py:84`
- `src/report_math.py:86`
- `src/report_math.py:87`
- `tests/test_background_tool_jobs.py:33`
- `tests/test_background_tool_jobs.py:62`
- `tests/test_background_tool_jobs.py:83`
- `tests/test_background_tool_jobs.py:107`
- `tests/test_background_tool_jobs.py:108`
- `tests/test_background_tool_jobs.py:202`
- `tests/test_background_tool_jobs.py:217`
- `tests/test_cookbook_endpoint_registration.py:63`
- `tests/test_cookbook_endpoint_registration.py:464`
- `tests/test_cookbook_serve_lifecycle.py:180`
- `static/js/calendar.js:4277`
- `static/js/cookbook.js:3558`
- `static/js/document.js:11821`
- `static/js/editor/fx/adj-popup.js:247`
- `static/js/editor/history-panel.js:62`
- `static/js/emailLibrary/index.js:2566`
- `static/js/emailLibrary/reader.js:181`
- `static/js/features/notes/ui/panel.js:96`
- `static/js/gallery.js:2405`
- `static/js/modalManager.js:15`
- `static/js/modalManager.js:1153`
- `static/js/modalManager.js:1158`
- `static/js/modalManager.js:1341`
- `static/js/modalManager.js:1444`

## `MemoryProviderRegistry.get` — method, line 271
- **called from:**
- `app.py:400`
- `app.py:424`
- `app.py:430`
- `app.py:457`
- `app.py:469`
- `app.py:511`
- `app.py:620`
- `app.py:553`
- `app.py:673`
- `app.py:976`
- `app.py:988`
- `app.py:992`
- `app.py:1000`
- `app.py:1004`
- `app.py:1008`
- `app.py:1012`
- `app.py:1016`
- `app.py:1020`
- `app.py:1024`
- `app.py:1029`
- `app.py:1035`
- `app.py:1045`
- `app.py:1054`
- `app.py:1066`
- `app.py:1067`
- `app.py:1068`
- `app.py:1068`
- `app.py:1070`
- `app.py:1070`
- `app.py:1074`
- `app.py:1095`
- `app.py:1086`
- `app.py:1097`
- `app.py:1270`
- `app.py:1273`
- `app.py:1273`
- `app.py:1274`
- `app.py:1275`
- `app.py:1280`
- `app.py:1280`
- `app.py:1301`
- `app.py:1335`
- `app.py:1349`
- `app.py:1390`
- `app.py:1393`
- `app.py:1408`
- `companion/pairing.py:116`
- `companion/pairing.py:126`
- `companion/pairing.py:173`
- `companion/pairing.py:177`
- `companion/routes.py:85`
- `companion/routes.py:97`
- `companion/routes.py:109`
- `companion/routes.py:168`
- `companion/routes.py:222`
- `core/auth.py:161`
- `core/auth.py:182`
- `core/auth.py:205`
- `core/auth.py:232`
- `core/auth.py:244`
- … +16891 more (grep the name in repo)

## `MemoryProviderRegistry.all` — method, line 274
- **called from:**
- `app.py:361`
- `app.py:1206`
- `app.py:1352`
- `companion/routes.py:141`
- `core/database.py:3118`
- `core/session_manager.py:99`
- `core/session_manager.py:137`
- `core/session_manager.py:149`
- `core/session_manager.py:258`
- `core/session_manager.py:630`
- `core/session_manager.py:706`
- `core/session_manager.py:1134`
- `mcp_servers/email_server.py:1391`
- `mcp_servers/email_server.py:2090`
- `routes/api_token_routes.py:83`
- `routes/assistant_routes.py:146`
- `routes/assistant_routes.py:249`
- `routes/assistant_routes.py:264`
- `routes/auth_routes.py:445`
- `routes/auth_routes.py:457`
- `routes/calendar_routes.py:669`
- `routes/calendar_routes.py:715`
- `routes/calendar_routes.py:1262`
- `routes/calendar_routes.py:1320`
- `routes/calendar_routes.py:1745`
- `routes/chat_helpers.py:1074`
- `routes/chat_helpers.py:1141`
- `routes/chat_routes.py:1804`
- `routes/chat_routes.py:1938`
- `routes/chat_routes.py:2015`
- `routes/chat_routes.py:2091`
- `routes/chat_routes.py:2220`
- `routes/chat_routes.py:3034`
- `routes/chatgpt_subscription_routes.py:40`
- `routes/chatgpt_subscription_routes.py:44`
- `routes/compare/compare_routes.py:329`
- `routes/document/document_routes.py:152`
- `routes/document/document_routes.py:548`
- `routes/document/document_routes.py:606`
- `routes/document/document_routes.py:653`
- `routes/document/document_routes.py:789`
- `routes/document/document_routes.py:804`
- `routes/document/document_routes.py:999`
- `routes/document/document_routes.py:1089`
- `routes/document/document_routes.py:1172`
- `routes/document/document_routes.py:1216`
- `routes/document/document_routes.py:1678`
- `routes/document/document_routes.py:1764`
- `routes/document/document_routes.py:1813`
- `routes/document/document_routes.py:1902`
- `routes/document/document_routes.py:1945`
- `routes/editor_agent_routes.py:1152`
- `routes/editor_agent_routes.py:2001`
- `routes/editor_draft_routes.py:139`
- `routes/email/email_helpers.py:1275`
- `routes/email/email_pollers.py:578`
- `routes/email/email_routes.py:1471`
- `routes/email/email_routes.py:2217`
- `routes/email/email_routes.py:7401`
- `routes/gallery/gallery_routes.py:339`
- … +565 more (grep the name in repo)

## `MemoryProviderRegistry.active` — method, line 277
- **called from:**
- `src/memory_provider.py:284`
- `src/memory_provider.py:299`
- `tests/test_rename_user_owner_sync.py:304`
- `tests/test_rename_user_owner_sync.py:307`
- `static/app.js:1021`
- `static/app.js:1022`
- `static/js/chat.js:6848`
- `static/js/document.js:2292`
- `static/js/editor/direct-manipulation-session.js:79`
- `static/js/features/notes/ui/drawing.js:234`
- `static/js/gallery.js:2864`
- `static/js/gallery.js:2983`
- `static/js/tasks.js:815`
- `static/js/tasks.js:843`

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
