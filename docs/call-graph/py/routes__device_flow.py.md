# `routes/device_flow.py` — definitions & call sites

22 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `DeviceFlowStart` — class, line 18
- decorator: `dataclass(frozen=True)`
- **called from:**
- `routes/chatgpt_subscription_routes.py:120`
- `routes/copilot_routes.py:122`
- `tests/test_device_flow_routes.py:26`

## `DeviceFlowPoll` — class, line 28
- decorator: `dataclass(frozen=True)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DeviceFlowPoll.pending` — method, line 38
- decorator: `classmethod`
- **called from:**
- `routes/chatgpt_subscription_routes.py:140`
- `routes/chatgpt_subscription_routes.py:155`
- `routes/chatgpt_subscription_routes.py:160`
- `routes/copilot_routes.py:143`
- `routes/copilot_routes.py:157`
- `routes/copilot_routes.py:163`
- `tests/test_device_flow_routes.py:40`
- `tests/test_device_flow_routes.py:112`
- `tests/test_device_flow_routes.py:128`
- `static/app.js:608`

## `DeviceFlowPoll.slow_down` — method, line 42
- decorator: `classmethod`
- **called from:**
- `routes/chatgpt_subscription_routes.py:157`
- `routes/copilot_routes.py:159`
- `routes/device_flow.py:181`
- `tests/test_device_flow_routes.py:66`

## `DeviceFlowPoll.authorized` — method, line 46
- decorator: `classmethod`
- **called from:**
- `routes/chatgpt_subscription_routes.py:151`
- `routes/copilot_routes.py:153`
- `tests/test_device_flow_routes.py:67`
- `tests/test_device_flow_routes.py:87`

## `DeviceFlowPoll.failed` — method, line 50
- decorator: `classmethod`
- **called from:**
- `routes/chatgpt_subscription_routes.py:159`
- `routes/copilot_routes.py:161`
- `tests/test_device_flow_routes.py:88`
- `static/js/admin.js:1249`
- `static/js/cookbookRunning.js:3702`
- `static/js/cookbookSchedule.js:349`
- `static/js/cookbookServe.js:3871`
- `static/js/document.js:3927`
- `static/js/document.js:3929`
- `static/js/editor/keyboard-shortcuts.js:226`
- `static/js/galleryEditor.js:1046`
- `static/js/galleryEditor.js:2008`
- `static/js/providerDeviceFlow.js:60`
- `static/js/sessions.js:1783`
- `static/js/sessions.js:2416`
- `static/js/settings.js:4720`
- `static/js/slashCommands.js:2107`
- `static/js/slashCommands.js:5075`

## `PendingDeviceFlowStore` — class, line 54
- **called from:**
- `routes/chatgpt_subscription_routes.py:22`
- `routes/copilot_routes.py:42`
- `tests/test_device_flow_routes.py:11`

## `PendingDeviceFlowStore.__init__` — method, line 62
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
- `core/database.py:517`
- `core/database.py:1972`
- `core/platform_compat.py:205`
- `core/session_manager.py:402`
- `core/session_manager.py:464`
- `core/session_manager.py:698`
- `core/session_manager.py:747`
- `core/session_manager.py:924`
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
- … +1221 more (grep the name in repo)

## `PendingDeviceFlowStore.get_payload` — method, line 88
- **called from:**
- `mcp_servers/email_server.py:782`
- `mcp_servers/email_server.py:787`
- `mcp_servers/email_server.py:797`
- `mcp_servers/email_server.py:1176`
- `mcp_servers/email_server.py:1207`
- `routes/device_flow.py:162`
- `routes/email_helpers.py:1481`
- `routes/email_helpers.py:1544`
- `routes/email_helpers.py:1609`
- `routes/email_helpers.py:1633`
- `routes/email_helpers.py:1638`
- `routes/email_helpers.py:1652`
- `routes/email_helpers.py:1657`
- `routes/email_helpers.py:1667`
- `routes/email_routes.py:3638`
- `routes/email_routes.py:4810`
- `routes/email_routes.py:4816`
- `src/builtin_actions.py:2659`
- `src/builtin_actions.py:2662`

## `PendingDeviceFlowStore.is_throttled` — method, line 96
- **called from:**
- `routes/device_flow.py:165`

## `PendingDeviceFlowStore.schedule_next` — method, line 101
- **called from:**
- `routes/device_flow.py:184`

## `PendingDeviceFlowStore.slow_down` — method, line 108
- **called from:**
- `routes/chatgpt_subscription_routes.py:157`
- `routes/copilot_routes.py:159`
- `routes/device_flow.py:181`
- `tests/test_device_flow_routes.py:66`

## `PendingDeviceFlowStore.pop` — method, line 117
- **called from:**
- `core/auth.py:327`
- `core/auth.py:351`
- `core/auth.py:460`
- `core/auth.py:518`
- `core/auth.py:556`
- `core/auth.py:557`
- `core/auth.py:558`
- `core/auth.py:608`
- `core/auth.py:616`
- `core/auth.py:634`
- `core/auth.py:640`
- `core/auth.py:650`
- `core/auth.py:663`
- `core/session_manager.py:223`
- `core/session_manager.py:333`
- `core/session_manager.py:341`
- `core/session_manager.py:359`
- `core/session_manager.py:450`
- `core/session_manager.py:513`
- `core/session_manager.py:593`
- `core/session_manager.py:974`
- `mcp_servers/email_server.py:2457`
- `routes/auth_routes.py:468`
- `routes/calendar_routes.py:827`
- `routes/chat_helpers.py:98`
- `routes/chat_routes.py:1976`
- `routes/chat_routes.py:2047`
- `routes/chat_routes.py:2114`
- `routes/chat_routes.py:2119`
- `routes/chat_routes.py:2204`
- `routes/chat_routes.py:2642`
- `routes/chat_routes.py:3034`
- `routes/chat_routes.py:3043`
- `routes/codex_routes.py:650`
- `routes/codex_routes.py:652`
- `routes/cookbook_routes.py:429`
- `routes/cookbook_routes.py:610`
- `routes/cookbook_routes.py:629`
- `routes/cookbook_routes.py:630`
- `routes/cookbook_routes.py:631`
- `routes/cookbook_routes.py:632`
- `routes/device_flow.py:74`
- `routes/device_flow.py:119`
- `routes/device_flow.py:171`
- `routes/device_flow.py:175`
- `routes/device_flow.py:178`
- `routes/device_flow.py:190`
- `routes/email_pollers.py:414`
- `routes/email_routes.py:164`
- `routes/email_routes.py:1604`
- `routes/email_routes.py:1613`
- `routes/email_routes.py:1621`
- `routes/email_routes.py:1633`
- `routes/email_routes.py:1650`
- `routes/email_routes.py:1678`
- `routes/email_routes.py:1686`
- `routes/email_routes.py:1797`
- `routes/email_routes.py:5483`
- `routes/email_routes.py:5484`
- `routes/email_routes.py:5485`
- … +366 more (grep the name in repo)

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
- `routes/chatgpt_subscription_routes.py:164`
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
