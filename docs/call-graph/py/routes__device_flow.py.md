# `routes/device_flow.py` — definitions & call sites

22 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `DeviceFlowStart` — class, line 18
- decorator: `dataclass(frozen=True)`
- **called from:**
- `routes/chatgpt_subscription_routes.py:305`
- `routes/copilot_routes.py:122`
- `tests/test_device_flow_routes.py:26`

## `DeviceFlowPoll` — class, line 28
- decorator: `dataclass(frozen=True)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DeviceFlowPoll.pending` — method, line 38
- decorator: `classmethod`
- **called from:**
- `routes/chatgpt_subscription_routes.py:338`
- `routes/chatgpt_subscription_routes.py:359`
- `routes/chatgpt_subscription_routes.py:364`
- `routes/copilot_routes.py:143`
- `routes/copilot_routes.py:157`
- `routes/copilot_routes.py:163`
- `tests/test_device_flow_routes.py:40`
- `tests/test_device_flow_routes.py:112`
- `tests/test_device_flow_routes.py:128`
- `static/app.js:641`

## `DeviceFlowPoll.slow_down` — method, line 42
- decorator: `classmethod`
- **called from:**
- `routes/chatgpt_subscription_routes.py:361`
- `routes/copilot_routes.py:159`
- `routes/device_flow.py:181`
- `tests/test_device_flow_routes.py:66`

## `DeviceFlowPoll.authorized` — method, line 46
- decorator: `classmethod`
- **called from:**
- `routes/chatgpt_subscription_routes.py:355`
- `routes/copilot_routes.py:153`
- `tests/test_device_flow_routes.py:67`
- `tests/test_device_flow_routes.py:87`

## `DeviceFlowPoll.failed` — method, line 50
- decorator: `classmethod`
- **called from:**
- `routes/chatgpt_subscription_routes.py:363`
- `routes/copilot_routes.py:161`
- `tests/test_device_flow_routes.py:88`
- `static/js/admin.js:1658`
- `static/js/admin.js:2118`
- `static/js/cookbookRunning.js:3758`
- `static/js/cookbookSchedule.js:364`
- `static/js/cookbookServe.js:3975`
- `static/js/document.js:6299`
- `static/js/document.js:6415`
- `static/js/document.js:6417`
- `static/js/document.js:15660`
- `static/js/document.js:15999`
- `static/js/document.js:16032`
- `static/js/editor/image-generation.js:44`
- `static/js/editor/image-generation.js:46`
- `static/js/emailLibrary/unsubscribe.js:413`
- `static/js/emailLibrary/unsubscribe.js:426`
- `static/js/emailLibrary/unsubscribe.js:862`
- `static/js/features/notes/ui/draftEditor.js:35`
- `static/js/features/notes/ui/draftEditor.js:36`
- `static/js/galleryEditor.js:4370`
- `static/js/galleryEditor.js:7586`
- `static/js/providerDeviceFlow.js:60`
- `static/js/sessions.js:394`
- `static/js/sessions.js:2123`
- `static/js/sessions.js:2777`
- `static/js/settings.js:4435`
- `static/js/slashCommands.js:2111`
- `static/js/slashCommands.js:5086`

## `PendingDeviceFlowStore` — class, line 54
- **called from:**
- `routes/chatgpt_subscription_routes.py:29`
- `routes/copilot_routes.py:42`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:160`
- `tests/test_device_flow_routes.py:11`

## `PendingDeviceFlowStore.__init__` — method, line 62
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

## `PendingDeviceFlowStore._now` — method, line 67
- **called from:**
- `routes/device_flow.py:71`
- `routes/device_flow.py:83`
- `routes/device_flow.py:99`
- `routes/device_flow.py:102`
- `routes/device_flow.py:109`

## `PendingDeviceFlowStore.prune_expired` — method, line 70
- **called from:**
- `routes/device_flow.py:77`
- `routes/device_flow.py:89`

## `PendingDeviceFlowStore.add` — method, line 76
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
- `routes/chat_routes.py:3606`
- `routes/chat_routes.py:3707`
- `routes/chat_routes.py:3943`
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
- … +2020 more (grep the name in repo)

## `PendingDeviceFlowStore.get_payload` — method, line 88
- **called from:**
- `mcp_servers/email_server.py:2364`
- `mcp_servers/email_server.py:2395`
- `routes/device_flow.py:162`
- `routes/email/email_helpers.py:1628`
- `routes/email/email_helpers.py:1691`
- `routes/email/email_helpers.py:1756`
- `routes/email/email_pollers.py:103`
- `routes/email/email_routes.py:5114`
- `routes/email/email_routes.py:6506`
- `routes/email/email_routes.py:6512`
- `src/builtin_actions.py:2923`
- `src/builtin_actions.py:2926`
- `src/email_mime.py:5`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:162`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:164`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:166`

## `PendingDeviceFlowStore.is_throttled` — method, line 96
- **called from:**
- `routes/device_flow.py:165`

## `PendingDeviceFlowStore.schedule_next` — method, line 101
- **called from:**
- `routes/device_flow.py:184`

## `PendingDeviceFlowStore.slow_down` — method, line 108
- **called from:**
- `routes/chatgpt_subscription_routes.py:361`
- `routes/copilot_routes.py:159`
- `routes/device_flow.py:181`
- `tests/test_device_flow_routes.py:66`

## `PendingDeviceFlowStore.pop` — method, line 117
- **called from:**
- `core/auth.py:345`
- `core/auth.py:369`
- `core/auth.py:498`
- `core/auth.py:569`
- `core/auth.py:607`
- `core/auth.py:608`
- `core/auth.py:609`
- `core/auth.py:659`
- `core/auth.py:667`
- `core/auth.py:685`
- `core/auth.py:691`
- `core/auth.py:701`
- `core/auth.py:714`
- `core/session_manager.py:231`
- `core/session_manager.py:349`
- `core/session_manager.py:357`
- `core/session_manager.py:375`
- `core/session_manager.py:466`
- `core/session_manager.py:529`
- `core/session_manager.py:609`
- `core/session_manager.py:1005`
- `mcp_servers/email_server.py:1580`
- `mcp_servers/email_server.py:4041`
- `mcp_servers/email_server.py:4042`
- `routes/auth_routes.py:518`
- `routes/calendar_routes.py:976`
- `routes/chat_helpers.py:383`
- `routes/chat_routes.py:206`
- `routes/chat_routes.py:4269`
- `routes/chat_routes.py:4341`
- `routes/chat_routes.py:4414`
- `routes/chat_routes.py:4419`
- `routes/chat_routes.py:4502`
- `routes/chat_routes.py:4963`
- `routes/chat_routes.py:5506`
- `routes/chat_routes.py:5517`
- `routes/codex_routes.py:696`
- `routes/codex_routes.py:698`
- `routes/cookbook_routes.py:468`
- `routes/cookbook_routes.py:480`
- `routes/cookbook_routes.py:499`
- `routes/cookbook_routes.py:500`
- `routes/cookbook_routes.py:501`
- `routes/cookbook_routes.py:502`
- `routes/device_flow.py:74`
- `routes/device_flow.py:119`
- `routes/device_flow.py:171`
- `routes/device_flow.py:175`
- `routes/device_flow.py:178`
- `routes/device_flow.py:190`
- `routes/editor_agent_routes.py:1378`
- `routes/editor_agent_routes.py:1390`
- `routes/editor_agent_routes.py:1412`
- `routes/editor_agent_routes.py:1419`
- `routes/editor_agent_routes.py:1638`
- `routes/editor_agent_routes.py:1882`
- `routes/editor_agent_routes.py:1890`
- `routes/editor_agent_routes.py:2059`
- `routes/email/email_pollers.py:529`
- `routes/email/email_routes.py:206`
- … +685 more (grep the name in repo)

## `_maybe_await` — function (async), line 122
- **called from:**
- `routes/device_flow.py:151`
- `routes/device_flow.py:169`

## `_pending_response` — function, line 128
- **called from:**
- `routes/device_flow.py:182`
- `routes/device_flow.py:185`

## `create_device_flow_router` — function, line 135
- **called from:**
- `routes/chatgpt_subscription_routes.py:409`
- `routes/copilot_routes.py:167`
- `tests/test_device_flow_routes.py:12`

## `device_start` — function (async), line 148
- **route:** `POST /device/start`
- decorator: `router.post("/device/start")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `device_poll` — function (async), line 160
- **route:** `POST /device/poll`
- decorator: `router.post("/device/poll")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `device_cancel` — function, line 188
- **route:** `POST /device/cancel`
- decorator: `router.post("/device/cancel")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
