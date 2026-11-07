# HTTP endpoints (FastAPI) ↔ JS fetch() callers

551 route decorators found. JS side: 1086 literal `fetch('/...')` call sites.

Match rule: fetch URL matched against route paths with `{param}` as `[^/]+`.

## `GET /`
- handler: `serve_index` — `app.py:977`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /`
- handler: `root` — `tests/test_diffusion_server_security.py:190`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /`
- handler: `root` — `tests/test_security_headers_middleware.py:26`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /accounts`
- handler: `list_accounts` — `routes/chatgpt_subscription_routes.py:418`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /accounts/{auth_id}/usage`
- handler: `account_usage` — `routes/chatgpt_subscription_routes.py:431`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/activity/heartbeat`
- handler: `activity_heartbeat` — `app.py:723`
- **JS callers:**
  - `static/app.js:149` → `/api/activity/heartbeat`
  - `static/app.js:152` → `/api/activity/heartbeat`

## `DELETE /api/admin/wipe/{kind}`
- handler: `wipe` — `routes/admin_wipe/admin_wipe_routes.py:72`
- **JS callers:**
  - `static/js/admin.js:3795` → `/api/admin/wipe/${k}`
  - `static/js/admin.js:3815` → `/api/admin/wipe/${kind}`

## `GET /api/assistant/available-timezones`
- handler: `list_timezones` — `routes/assistant_routes.py:325`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/assistant/run-status/{task_id}`
- handler: `run_status` — `routes/assistant_routes.py:300`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/assistant/run/{task_id}`
- handler: `run_check_in_now` — `routes/assistant_routes.py:277`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/assistant/session`
- handler: `get_assistant_session` — `routes/assistant_routes.py:125`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/assistant/settings`
- handler: `get_assistant_settings` — `routes/assistant_routes.py:138`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PATCH /api/assistant/settings`
- handler: `update_assistant_settings` — `routes/assistant_routes.py:159`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/auth/2fa/confirm`
- handler: `totp_confirm` — `routes/auth_routes.py:293`
- **JS callers:**
  - `static/js/settings.js:1847` → `/api/auth/2fa/confirm`

## `POST /api/auth/2fa/disable`
- handler: `totp_disable` — `routes/auth_routes.py:307`
- **JS callers:**
  - `static/js/settings.js:1801` → `/api/auth/2fa/disable`

## `POST /api/auth/2fa/setup`
- handler: `totp_setup` — `routes/auth_routes.py:270`
- **JS callers:**
  - `static/js/settings.js:1821` → `/api/auth/2fa/setup`

## `GET /api/auth/2fa/status`
- handler: `totp_status` — `routes/auth_routes.py:317`
- **JS callers:**
  - `static/js/settings.js:1782` → `/api/auth/2fa/status`

## `POST /api/auth/change-password`
- handler: `change_password` — `routes/auth_routes.py:252`
- **JS callers:**
  - `static/js/settings.js:1757` → `/api/auth/change-password`

## `GET /api/auth/features`
- handler: `get_features` — `routes/auth_routes.py:756`
- **JS callers:**
  - `static/app.js:1551` → `/api/auth/features`
  - `static/js/admin.js:3640` → `/api/auth/features`
  - `static/js/admin.js:3650` → `/api/auth/features`
  - `static/js/censor.js:62` → `/api/auth/features`
  - `static/js/slashCommands.js:889` → `/api/auth/features`
  - `static/js/slashCommands.js:893` → `/api/auth/features`
  - `static/js/slashCommands.js:5199` → `/api/auth/features`

## `POST /api/auth/features`
- handler: `set_features` — `routes/auth_routes.py:761`
- **JS callers:**
  - `static/app.js:1551` → `/api/auth/features`
  - `static/js/admin.js:3640` → `/api/auth/features`
  - `static/js/admin.js:3650` → `/api/auth/features`
  - `static/js/censor.js:62` → `/api/auth/features`
  - `static/js/slashCommands.js:889` → `/api/auth/features`
  - `static/js/slashCommands.js:893` → `/api/auth/features`
  - `static/js/slashCommands.js:5199` → `/api/auth/features`

## `GET /api/auth/integrations`
- handler: `list_integrations_route` — `routes/auth_routes.py:915`
- **JS callers:**
  - `static/js/settings.js:2050` → `/api/auth/integrations`
  - `static/js/settings.js:2077` → `/api/auth/integrations`
  - `static/js/settings.js:2147` → `/api/auth/integrations`
  - `static/js/settings.js:2984` → `/api/auth/integrations`
  - `static/js/settings.js:3017` → `/api/auth/integrations`
  - `static/js/settings.js:3071` → `/api/auth/integrations`
  - `static/js/settings.js:3227` → `/api/auth/integrations`
  - `static/js/settings.js:3514` → `/api/auth/integrations`
  - `static/js/settings.js:3560` → `/api/auth/integrations`

## `POST /api/auth/integrations`
- handler: `create_integration` — `routes/auth_routes.py:929`
- **JS callers:**
  - `static/js/settings.js:2050` → `/api/auth/integrations`
  - `static/js/settings.js:2077` → `/api/auth/integrations`
  - `static/js/settings.js:2147` → `/api/auth/integrations`
  - `static/js/settings.js:2984` → `/api/auth/integrations`
  - `static/js/settings.js:3017` → `/api/auth/integrations`
  - `static/js/settings.js:3071` → `/api/auth/integrations`
  - `static/js/settings.js:3227` → `/api/auth/integrations`
  - `static/js/settings.js:3514` → `/api/auth/integrations`
  - `static/js/settings.js:3560` → `/api/auth/integrations`

## `GET /api/auth/integrations/presets`
- handler: `list_presets` — `routes/auth_routes.py:924`
- **JS callers:**
  - `static/js/settings.js:2957` → `/api/auth/integrations/presets`
  - `static/js/settings.js:3394` → `/api/auth/integrations/presets`

## `DELETE /api/auth/integrations/{integration_id}`
- handler: `delete_integration_route` — `routes/auth_routes.py:951`
- **JS callers:**
  - `static/js/settings.js:2957` → `/api/auth/integrations/presets`
  - `static/js/settings.js:3111` → `/api/auth/integrations/${id}`
  - `static/js/settings.js:3358` → `/api/auth/integrations/${id}`
  - `static/js/settings.js:3394` → `/api/auth/integrations/presets`

## `PUT /api/auth/integrations/{integration_id}`
- handler: `update_integration_route` — `routes/auth_routes.py:939`
- **JS callers:**
  - `static/js/settings.js:2957` → `/api/auth/integrations/presets`
  - `static/js/settings.js:3111` → `/api/auth/integrations/${id}`
  - `static/js/settings.js:3358` → `/api/auth/integrations/${id}`
  - `static/js/settings.js:3394` → `/api/auth/integrations/presets`

## `POST /api/auth/integrations/{integration_id}/test`
- handler: `test_integration_route` — `routes/auth_routes.py:960`
- **JS callers:**
  - `static/js/settings.js:3097` → `/api/auth/integrations/${editingId}/test`
  - `static/js/settings.js:3579` → `/api/auth/integrations/${_editId}/test`

## `POST /api/auth/login`
- handler: `login` — `routes/auth_routes.py:190`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/auth/logout`
- handler: `logout` — `routes/auth_routes.py:222`
- **JS callers:**
  - `static/js/settings.js:1880` → `/api/auth/logout`

## `PUT /api/auth/open-signup`
- handler: `set_signup_enabled` — `routes/auth_routes.py:713`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/auth/policy`
- handler: `auth_policy` — `routes/auth_routes.py:247`
- **JS callers:**
  - `static/js/admin.js:429` → `/api/auth/policy`
  - `static/js/settings.js:1734` → `/api/auth/policy`

## `GET /api/auth/settings`
- handler: `get_settings` — `routes/auth_routes.py:775`
- **JS callers:**
  - `static/js/admin.js:411` → `/api/auth/settings`
  - `static/js/appConfig.js:33` → `/api/auth/settings`
  - `static/js/chat.js:933` → `/api/auth/settings`
  - `static/js/document.js:11362` → `/api/auth/settings`
  - `static/js/research/panel.js:789` → `/api/auth/settings`
  - `static/js/settings.js:394` → `/api/auth/settings`
  - `static/js/settings.js:525` → `/api/auth/settings`
  - `static/js/settings.js:631` → `/api/auth/settings`
  - `static/js/settings.js:724` → `/api/auth/settings`
  - `static/js/settings.js:864` → `/api/auth/settings`
  - `static/js/settings.js:885` → `/api/auth/settings`
  - `static/js/settings.js:1172` → `/api/auth/settings`
  - `static/js/settings.js:1290` → `/api/auth/settings`
  - `static/js/settings.js:1529` → `/api/auth/settings`
  - `static/js/settings.js:1978` → `/api/auth/settings`
  - `static/js/settings.js:2061` → `/api/auth/settings`
  - `static/js/settings.js:2159` → `/api/auth/settings`
  - `static/js/settings.js:2217` → `/api/auth/settings`
  - `static/js/settings/agent.js:18` → `/api/auth/settings`
  - `static/js/settings/api.js:8` → `/api/auth/settings`
  - … +6 more

## `POST /api/auth/settings`
- handler: `set_settings` — `routes/auth_routes.py:791`
- **JS callers:**
  - `static/js/admin.js:411` → `/api/auth/settings`
  - `static/js/appConfig.js:33` → `/api/auth/settings`
  - `static/js/chat.js:933` → `/api/auth/settings`
  - `static/js/document.js:11362` → `/api/auth/settings`
  - `static/js/research/panel.js:789` → `/api/auth/settings`
  - `static/js/settings.js:394` → `/api/auth/settings`
  - `static/js/settings.js:525` → `/api/auth/settings`
  - `static/js/settings.js:631` → `/api/auth/settings`
  - `static/js/settings.js:724` → `/api/auth/settings`
  - `static/js/settings.js:864` → `/api/auth/settings`
  - `static/js/settings.js:885` → `/api/auth/settings`
  - `static/js/settings.js:1172` → `/api/auth/settings`
  - `static/js/settings.js:1290` → `/api/auth/settings`
  - `static/js/settings.js:1529` → `/api/auth/settings`
  - `static/js/settings.js:1978` → `/api/auth/settings`
  - `static/js/settings.js:2061` → `/api/auth/settings`
  - `static/js/settings.js:2159` → `/api/auth/settings`
  - `static/js/settings.js:2217` → `/api/auth/settings`
  - `static/js/settings/agent.js:18` → `/api/auth/settings`
  - `static/js/settings/api.js:8` → `/api/auth/settings`
  - … +6 more

## `POST /api/auth/settings/document-style/extract`
- handler: `extract_document_writing_style` — `routes/auth_routes.py:833`
- **JS callers:**
  - `static/js/settings/writingStyle.js:56` → `/api/auth/settings/document-style/extract`

## `POST /api/auth/setup`
- handler: `first_run_setup` — `routes/auth_routes.py:150`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/auth/signup`
- handler: `signup` — `routes/auth_routes.py:169`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/auth/signup-toggle`
- handler: `toggle_signup` — `routes/auth_routes.py:697`
- **JS callers:**
  - `static/js/admin.js:397` → `/api/auth/signup-toggle`

## `GET /api/auth/status`
- handler: `auth_status` — `routes/auth_routes.py:230`
- **JS callers:**
  - `static/app.js:1364` → `/api/auth/status`
  - `static/js/admin.js:391` → `/api/auth/status`
  - `static/js/init.js:58` → `/api/auth/status`
  - `static/js/settings.js:1719` → `/api/auth/status`

## `DELETE /api/auth/users`
- handler: `admin_delete_user` — `routes/auth_routes.py:722`
- **JS callers:**
  - `static/js/admin.js:71` → `/api/auth/users`
  - `static/js/admin.js:256` → `/api/auth/users`
  - `static/js/admin.js:449` → `/api/auth/users`

## `GET /api/auth/users`
- handler: `list_users` — `routes/auth_routes.py:326`
- **JS callers:**
  - `static/js/admin.js:71` → `/api/auth/users`
  - `static/js/admin.js:256` → `/api/auth/users`
  - `static/js/admin.js:449` → `/api/auth/users`

## `POST /api/auth/users`
- handler: `admin_create_user` — `routes/auth_routes.py:333`
- **JS callers:**
  - `static/js/admin.js:71` → `/api/auth/users`
  - `static/js/admin.js:256` → `/api/auth/users`
  - `static/js/admin.js:449` → `/api/auth/users`

## `PUT /api/auth/users/{username}/admin`
- handler: `set_user_admin` — `routes/auth_routes.py:661`
- **JS callers:**
  - `static/js/admin.js:275` → `/api/auth/users/${encodeURIComponent(username)}/admin`

## `PUT /api/auth/users/{username}/password`
- handler: `reset_user_password` — `routes/auth_routes.py:350`
- **JS callers:**
  - `static/js/admin.js:201` → `/api/auth/users/${encodeURIComponent(u.username)}/password`

## `PUT /api/auth/users/{username}/privileges`
- handler: `update_user_privileges` — `routes/auth_routes.py:364`
- **JS callers:**
  - `static/js/admin.js:178` → `/api/auth/users/${encodeURIComponent(username)}/privileges`
  - `static/js/admin.js:365` → `/api/auth/users/${encodeURIComponent(username)}/privileges`

## `PUT /api/auth/users/{username}/rename`
- handler: `rename_user` — `routes/auth_routes.py:383`
- **JS callers:**
  - `static/js/admin.js:227` → `/api/auth/users/${encodeURIComponent(oldUsername)}/rename`

## `GET /api/busy`
- handler: `get_busy` — `app.py:1046`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/calendar/calendars`
- handler: `list_calendars` — `routes/calendar_routes.py:1254`
- **JS callers:**
  - `static/js/calendar.js:190` → `/api/calendar/calendars`
  - `static/js/calendar.js:3233` → `/api/calendar/calendars?name=`
  - `static/js/cookbookSchedule.js:311` → `/api/calendar/calendars`
  - `static/js/cookbookSchedule.js:315` → `/api/calendar/calendars?name=Cookbook&color=%233b82f6`
  - `static/js/settings.js:3235` → `/api/calendar/calendars`

## `POST /api/calendar/calendars`
- handler: `create_calendar` — `routes/calendar_routes.py:1533`
- **JS callers:**
  - `static/js/calendar.js:190` → `/api/calendar/calendars`
  - `static/js/calendar.js:3233` → `/api/calendar/calendars?name=`
  - `static/js/cookbookSchedule.js:311` → `/api/calendar/calendars`
  - `static/js/cookbookSchedule.js:315` → `/api/calendar/calendars?name=Cookbook&color=%233b82f6`
  - `static/js/settings.js:3235` → `/api/calendar/calendars`

## `DELETE /api/calendar/calendars/{cal_id}`
- handler: `delete_calendar` — `routes/calendar_routes.py:1234`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PUT /api/calendar/calendars/{cal_id}`
- handler: `update_calendar` — `routes/calendar_routes.py:1556`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/calendar/config`
- handler: `get_config` — `routes/calendar_routes.py:982`
- **JS callers:**
  - `static/js/admin.js:3667` → `/api/calendar/config`
  - `static/js/admin.js:3677` → `/api/calendar/config`
  - `static/js/admin.js:3693` → `/api/calendar/config`

## `POST /api/calendar/config`
- handler: `save_config` — `routes/calendar_routes.py:1006`
- **JS callers:**
  - `static/js/admin.js:3667` → `/api/calendar/config`
  - `static/js/admin.js:3677` → `/api/calendar/config`
  - `static/js/admin.js:3693` → `/api/calendar/config`

## `GET /api/calendar/config/accounts`
- handler: `list_caldav_accounts` — `routes/calendar_routes.py:1036`
- **JS callers:**
  - `static/js/settings.js:3228` → `/api/calendar/config/accounts`
  - `static/js/settings.js:3615` → `/api/calendar/config/accounts`
  - `static/js/settings.js:3670` → `/api/calendar/config/accounts`

## `POST /api/calendar/config/accounts`
- handler: `add_caldav_account` — `routes/calendar_routes.py:1060`
- **JS callers:**
  - `static/js/settings.js:3228` → `/api/calendar/config/accounts`
  - `static/js/settings.js:3615` → `/api/calendar/config/accounts`
  - `static/js/settings.js:3670` → `/api/calendar/config/accounts`

## `DELETE /api/calendar/config/accounts/{account_id}`
- handler: `delete_caldav_account` — `routes/calendar_routes.py:1113`
- **JS callers:**
  - `static/js/settings.js:3359` → `/api/calendar/config/accounts/${id}`
  - `static/js/settings.js:3676` → `/api/calendar/config/accounts/${editId}`

## `PUT /api/calendar/config/accounts/{account_id}`
- handler: `update_caldav_account` — `routes/calendar_routes.py:1086`
- **JS callers:**
  - `static/js/settings.js:3359` → `/api/calendar/config/accounts/${id}`
  - `static/js/settings.js:3676` → `/api/calendar/config/accounts/${editId}`

## `GET /api/calendar/events`
- handler: `list_events` — `routes/calendar_routes.py:1277`
- **JS callers:**
  - `static/js/calendar.js:128` → `/api/calendar/events?start=`
  - `static/js/calendar.js:169` → `/api/calendar/events?start=`
  - `static/js/calendar.js:263` → `/api/calendar/events`
  - `static/js/cookbookSchedule.js:346` → `/api/calendar/events`
  - `static/js/emailLibrary/settingsPage.js:166` → `/api/calendar/events?start=`
  - `static/js/emailLibrary/settingsPage.js:217` → `/api/calendar/events`
  - `static/js/slashCommands.js:1853` → `/api/calendar/events`

## `POST /api/calendar/events`
- handler: `create_event` — `routes/calendar_routes.py:1343`
- **JS callers:**
  - `static/js/calendar.js:128` → `/api/calendar/events?start=`
  - `static/js/calendar.js:169` → `/api/calendar/events?start=`
  - `static/js/calendar.js:263` → `/api/calendar/events`
  - `static/js/cookbookSchedule.js:346` → `/api/calendar/events`
  - `static/js/emailLibrary/settingsPage.js:166` → `/api/calendar/events?start=`
  - `static/js/emailLibrary/settingsPage.js:217` → `/api/calendar/events`
  - `static/js/slashCommands.js:1853` → `/api/calendar/events`

## `DELETE /api/calendar/events/{uid}`
- handler: `delete_event` — `routes/calendar_routes.py:1488`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/calendar/events/{uid}`
- handler: `get_event` — `routes/calendar_routes.py:1414`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PUT /api/calendar/events/{uid}`
- handler: `update_event` — `routes/calendar_routes.py:1425`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/calendar/export/{cal_id}`
- handler: `export_ics` — `routes/calendar_routes.py:1737`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/calendar/import`
- handler: `import_ics` — `routes/calendar_routes.py:1583`
- **JS callers:**
  - `static/js/calendar.js:3314` → `/api/calendar/import`
  - `static/js/emailLibrary/attachments.js:113` → `/api/calendar/import`

## `POST /api/calendar/quick-parse`
- handler: `quick_parse` — `routes/calendar_routes.py:1795`
- **JS callers:**
  - `static/js/calendar.js:2594` → `/api/calendar/quick-parse`

## `POST /api/calendar/sync`
- handler: `sync_caldav_endpoint` — `routes/calendar_routes.py:1224`
- **JS callers:**
  - `static/js/calendar.js:213` → `/api/calendar/sync`

## `POST /api/calendar/test`
- handler: `test_connection` — `routes/calendar_routes.py:1124`
- **JS callers:**
  - `static/js/admin.js:3698` → `/api/calendar/test`
  - `static/js/settings.js:3636` → `/api/calendar/test`

## `POST /api/chat`
- handler: `chat_endpoint` — `routes/chat_routes.py:2415`
- **JS callers:**
  - `static/js/editor/nl-edit.js:12` → `/api/chat`
  - `static/js/slashCommands.js:655` → `/api/chat`

## `POST /api/chat/finish/{session_id}`
- handler: `chat_finish` — `routes/chat_routes.py:5587`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/chat/reasoning-control`
- handler: `reasoning_control` — `routes/chat_routes.py:5660`
- **JS callers:**
  - `static/js/chat.js:7796` → `/api/chat/reasoning-control?model=`

## `GET /api/chat/resume/{session_id}`
- handler: `chat_resume` — `routes/chat_routes.py:5560`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/chat/stop/{session_id}`
- handler: `chat_stop` — `routes/chat_routes.py:5580`
- **JS callers:**
  - `static/js/chat.js:1919` → `/api/chat/stop/${encodeURIComponent(sessionId)}`

## `GET /api/chat/stream_status/{session_id}`
- handler: `chat_stream_status` — `routes/chat_routes.py:5598`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/chat_stream`
- handler: `chat_stream` — `routes/chat_routes.py:2654`
- **JS callers:**
  - `static/js/chat.js:3568` → `/api/chat_stream`
  - `static/js/compare/stream.js:299` → `/api/chat_stream`
  - `static/js/compare/stream.js:468` → `/api/chat_stream`
  - `static/js/features/notes/infrastructure/http.js:27` → `/api/chat_stream`
  - `static/js/group.js:857` → `/api/chat_stream`

## `GET /api/cleanup/preview`
- handler: `cleanup_preview` — `routes/cleanup/cleanup_routes.py:23`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/client-perf`
- handler: `client_perf` — `app.py:1059`
- **JS callers:**
  - `static/js/chat.js:1252` → `/api/client-perf`
  - `static/js/chat.js:1257` → `/api/client-perf`

## `GET /api/codex/calendar/events`
- handler: `codex_calendar_list` — `routes/codex_routes.py:467`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/calendar/events`
- handler: `codex_calendar_create` — `routes/codex_routes.py:474`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/codex/calendar/events/{uid}`
- handler: `codex_calendar_delete` — `routes/codex_routes.py:535`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/capabilities`
- handler: `capabilities` — `routes/codex_routes.py:182`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/chat/{session_id}`
- handler: `read_chat` — `routes/codex_routes.py:238`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/cookbook/adopt`
- handler: `codex_cookbook_adopt` — `routes/codex_routes.py:872`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/cookbook/cached`
- handler: `codex_cookbook_cached` — `routes/codex_routes.py:739`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/cookbook/output/{session_id}`
- handler: `codex_cookbook_output` — `routes/codex_routes.py:641`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/cookbook/preset/{name}`
- handler: `codex_cookbook_serve_preset` — `routes/codex_routes.py:822`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/cookbook/presets`
- handler: `codex_cookbook_presets` — `routes/codex_routes.py:801`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/cookbook/serve`
- handler: `codex_cookbook_serve` — `routes/codex_routes.py:683`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/cookbook/servers`
- handler: `codex_cookbook_servers` — `routes/codex_routes.py:622`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/cookbook/stop/{session_id}`
- handler: `codex_cookbook_stop` — `routes/codex_routes.py:722`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/cookbook/tasks`
- handler: `codex_cookbook_tasks` — `routes/codex_routes.py:615`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/documents`
- handler: `codex_documents_library` — `routes/codex_routes.py:489`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/documents`
- handler: `codex_documents_create` — `routes/codex_routes.py:549`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/codex/documents/{doc_id}`
- handler: `codex_documents_delete` — `routes/codex_routes.py:542`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/documents/{doc_id}`
- handler: `codex_documents_get` — `routes/codex_routes.py:515`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/emails`
- handler: `list_emails` — `routes/codex_routes.py:298`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/emails/draft`
- handler: `codex_email_draft` — `routes/codex_routes.py:410`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/emails/draft-document`
- handler: `codex_email_draft_document` — `routes/codex_routes.py:385`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/emails/send`
- handler: `codex_email_send` — `routes/codex_routes.py:423`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/emails/{uid}`
- handler: `read_email` — `routes/codex_routes.py:330`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/memory`
- handler: `codex_memory_list` — `routes/codex_routes.py:438`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/memory`
- handler: `codex_memory_add` — `routes/codex_routes.py:445`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/codex/memory/{memory_id}`
- handler: `codex_memory_delete` — `routes/codex_routes.py:528`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/plugin.zip`
- handler: `plugin_zip` — `routes/codex_routes.py:265`
- **JS callers:**
  - `static/js/settings.js:3145` → `/api/codex/plugin.zip`
  - `static/js/settings.js:3145` → `/api/codex/plugin.zip`
  - `static/js/settings.js:3150` → `/api/codex/plugin.zip`
  - `static/js/settings.js:3150` → `/api/codex/plugin.zip`

## `GET /api/codex/plugin.zip`
- handler: `plugin_zip` — `routes/codex_routes.py:938`
- **JS callers:**
  - `static/js/settings.js:3145` → `/api/codex/plugin.zip`
  - `static/js/settings.js:3145` → `/api/codex/plugin.zip`
  - `static/js/settings.js:3150` → `/api/codex/plugin.zip`
  - `static/js/settings.js:3150` → `/api/codex/plugin.zip`

## `GET /api/codex/todos`
- handler: `list_todos` — `routes/codex_routes.py:281`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/todos`
- handler: `manage_todos` — `routes/codex_routes.py:289`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/companion/info`
- handler: `info` — `companion/routes.py:98`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/companion/models`
- handler: `models` — `companion/routes.py:110`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/companion/pair`
- handler: `pair_page` — `companion/routes.py:169`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/companion/pair`
- handler: `pair_create` — `companion/routes.py:196`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/companion/ping`
- handler: `ping` — `companion/routes.py:86`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/compare/history`
- handler: `list_comparisons` — `routes/compare/compare_routes.py:321`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/compare/record`
- handler: `record_comparison` — `routes/compare/compare_routes.py:284`
- **JS callers:**
  - `static/js/compare/vote.js:131` → `/api/compare/record`

## `POST /api/compare/start`
- handler: `start_comparison` — `routes/compare/compare_routes.py:71`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/compare/{comp_id}`
- handler: `delete_comparison` — `routes/compare/compare_routes.py:347`
- **JS callers:**
  - `static/js/compare/vote.js:131` → `/api/compare/record`

## `POST /api/compare/{comp_id}/vote`
- handler: `vote_comparison` — `routes/compare/compare_routes.py:238`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/contacts/add`
- handler: `add_contact` — `routes/contacts/contacts_routes.py:894`
- **JS callers:**
  - `static/js/document.js:6466` → `/api/contacts/add`
  - `static/js/emailLibrary/menus.js:219` → `/api/contacts/add`
  - `static/js/settings.js:3789` → `/api/contacts/add`

## `DELETE /api/contacts/clear`
- handler: `clear_contacts` — `routes/contacts/contacts_routes.py:1021`
- **JS callers:**
  - `static/js/settings.js:3361` → `/api/contacts/clear`

## `GET /api/contacts/config`
- handler: `get_config` — `routes/contacts/contacts_routes.py:991`
- **JS callers:**
  - `static/js/settings.js:2782` → `/api/contacts/config`
  - `static/js/settings.js:2831` → `/api/contacts/config`
  - `static/js/settings.js:3229` → `/api/contacts/config`
  - `static/js/settings.js:3364` → `/api/contacts/config`
  - `static/js/settings.js:3746` → `/api/contacts/config`
  - `static/js/settings.js:3759` → `/api/contacts/config`

## `PUT /api/contacts/config`
- handler: `update_config` — `routes/contacts/contacts_routes.py:999`
- **JS callers:**
  - `static/js/settings.js:2782` → `/api/contacts/config`
  - `static/js/settings.js:2831` → `/api/contacts/config`
  - `static/js/settings.js:3229` → `/api/contacts/config`
  - `static/js/settings.js:3364` → `/api/contacts/config`
  - `static/js/settings.js:3746` → `/api/contacts/config`
  - `static/js/settings.js:3759` → `/api/contacts/config`

## `GET /api/contacts/export`
- handler: `export_contacts` — `routes/contacts/contacts_routes.py:965`
- **JS callers:**
  - `static/js/settings.js:3803` → `/api/contacts/export?format=${encodeURIComponent(format)}`
  - `static/js/settings.js:3803` → `/api/contacts/export?format=`

## `POST /api/contacts/import`
- handler: `import_vcf` — `routes/contacts/contacts_routes.py:946`
- **JS callers:**
  - `static/js/settings.js:3844` → `/api/contacts/import`

## `GET /api/contacts/list`
- handler: `list_contacts` — `routes/contacts/contacts_routes.py:870`
- **JS callers:**
  - `static/js/emailLibrary/index.js:3733` → `/api/contacts/list`
  - `static/js/settings.js:3230` → `/api/contacts/list`
  - `static/js/settings.js:3878` → `/api/contacts/list`

## `GET /api/contacts/search`
- handler: `search_contacts` — `routes/contacts/contacts_routes.py:876`
- **JS callers:**
  - `static/js/document.js:6047` → `/api/contacts/search?q=`

## `DELETE /api/contacts/{uid}`
- handler: `delete_contact` — `routes/contacts/contacts_routes.py:1056`
- **JS callers:**
  - `static/js/document.js:6047` → `/api/contacts/search?q=`
  - `static/js/document.js:6466` → `/api/contacts/add`
  - `static/js/emailLibrary/index.js:3733` → `/api/contacts/list`
  - `static/js/emailLibrary/menus.js:219` → `/api/contacts/add`
  - `static/js/settings.js:2782` → `/api/contacts/config`
  - `static/js/settings.js:2831` → `/api/contacts/config`
  - `static/js/settings.js:3229` → `/api/contacts/config`
  - `static/js/settings.js:3230` → `/api/contacts/list`
  - `static/js/settings.js:3361` → `/api/contacts/clear`
  - `static/js/settings.js:3364` → `/api/contacts/config`
  - `static/js/settings.js:3746` → `/api/contacts/config`
  - `static/js/settings.js:3759` → `/api/contacts/config`
  - `static/js/settings.js:3789` → `/api/contacts/add`
  - `static/js/settings.js:3803` → `/api/contacts/export?format=${encodeURIComponent(format)}`
  - `static/js/settings.js:3803` → `/api/contacts/export?format=`
  - `static/js/settings.js:3844` → `/api/contacts/import`
  - `static/js/settings.js:3878` → `/api/contacts/list`

## `PUT /api/contacts/{uid}`
- handler: `edit_contact` — `routes/contacts/contacts_routes.py:1038`
- **JS callers:**
  - `static/js/document.js:6047` → `/api/contacts/search?q=`
  - `static/js/document.js:6466` → `/api/contacts/add`
  - `static/js/emailLibrary/index.js:3733` → `/api/contacts/list`
  - `static/js/emailLibrary/menus.js:219` → `/api/contacts/add`
  - `static/js/settings.js:2782` → `/api/contacts/config`
  - `static/js/settings.js:2831` → `/api/contacts/config`
  - `static/js/settings.js:3229` → `/api/contacts/config`
  - `static/js/settings.js:3230` → `/api/contacts/list`
  - `static/js/settings.js:3361` → `/api/contacts/clear`
  - `static/js/settings.js:3364` → `/api/contacts/config`
  - `static/js/settings.js:3746` → `/api/contacts/config`
  - `static/js/settings.js:3759` → `/api/contacts/config`
  - `static/js/settings.js:3789` → `/api/contacts/add`
  - `static/js/settings.js:3803` → `/api/contacts/export?format=${encodeURIComponent(format)}`
  - `static/js/settings.js:3803` → `/api/contacts/export?format=`
  - `static/js/settings.js:3844` → `/api/contacts/import`
  - `static/js/settings.js:3878` → `/api/contacts/list`

## `GET /api/conversations/topics`
- handler: `get_conversation_topics` — `routes/history/history_routes.py:1183`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/cookbook/gpus`
- handler: `list_gpus` — `routes/cookbook_routes.py:3021`
- **JS callers:**
  - `static/js/cookbookRunning.js:1935` → `/api/cookbook/gpus`
  - `static/js/cookbookServe.js:2167` → `/api/cookbook/gpus`
  - `static/js/cookbookServe.js:3021` → `/api/cookbook/gpus`
  - `static/js/cookbookServe.js:3562` → `/api/cookbook/gpus`
  - `static/js/cookbookServe.js:3674` → `/api/cookbook/gpus`

## `GET /api/cookbook/hf-gguf-files`
- handler: `hf_gguf_files` — `routes/cookbook_routes.py:3774`
- **JS callers:**
  - `static/js/cookbook.js:2491` → `/api/cookbook/hf-gguf-files?repo_id=`

## `GET /api/cookbook/hf-latest`
- handler: `hf_latest` — `routes/cookbook_routes.py:3398`
- **JS callers:**
  - `static/js/cookbook.js:2824` → `/api/cookbook/hf-latest?`

## `POST /api/cookbook/install-system-deps`
- handler: `install_system_deps` — `routes/shell_routes.py:2083`
- **JS callers:**
  - `static/js/cookbook.js:1623` → `/api/cookbook/install-system-deps`

## `POST /api/cookbook/kill-pid`
- handler: `kill_pid` — `routes/cookbook_routes.py:3196`
- **JS callers:**
  - `static/js/cookbookServe.js:2914` → `/api/cookbook/kill-pid`
  - `static/js/cookbookServe.js:3138` → `/api/cookbook/kill-pid`
  - `static/js/cookbookServe.js:3162` → `/api/cookbook/kill-pid`

## `GET /api/cookbook/ollama/library`
- handler: `ollama_library` — `routes/cookbook_routes.py:3840`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:618` → `/api/cookbook/ollama/library`
  - `static/js/cookbook.js:2923` → `/api/cookbook/ollama/library`

## `GET /api/cookbook/packages`
- handler: `list_packages` — `routes/shell_routes.py:1419`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:138` → `/api/cookbook/packages`
  - `static/js/cookbook.js:1131` → `/api/cookbook/packages`
  - `static/js/cookbookServe.js:865` → `/api/cookbook/packages`
  - `static/js/galleryEditor.js:13328` → `/api/cookbook/packages`
  - `static/js/galleryEditor.js:13340` → `/api/cookbook/packages`

## `POST /api/cookbook/packages/install`
- handler: `install_package` — `routes/shell_routes.py:2035`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/cookbook/rebuild-engine`
- handler: `rebuild_engine` — `routes/shell_routes.py:2213`
- **JS callers:**
  - `static/js/cookbook.js:1811` → `/api/cookbook/rebuild-engine`

## `POST /api/cookbook/setup`
- handler: `server_setup` — `routes/cookbook_routes.py:2717`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:2763` → `/api/cookbook/setup`

## `GET /api/cookbook/ssh-key`
- handler: `get_cookbook_ssh_key` — `routes/cookbook_routes.py:800`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:2506` → `/api/cookbook/ssh-key`

## `POST /api/cookbook/ssh-key`
- handler: `generate_cookbook_ssh_key` — `routes/cookbook_routes.py:809`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:2506` → `/api/cookbook/ssh-key`

## `GET /api/cookbook/state`
- handler: `get_cookbook_state` — `routes/cookbook_routes.py:3247`
- **JS callers:**
  - `static/js/cookbookRunning.js:1381` → `/api/cookbook/state`
  - `static/js/cookbookRunning.js:1423` → `/api/cookbook/state`
  - `static/js/cookbookRunning.js:4194` → `/api/cookbook/state`

## `POST /api/cookbook/state`
- handler: `save_cookbook_state` — `routes/cookbook_routes.py:3275`
- **JS callers:**
  - `static/js/cookbookRunning.js:1381` → `/api/cookbook/state`
  - `static/js/cookbookRunning.js:1423` → `/api/cookbook/state`
  - `static/js/cookbookRunning.js:4194` → `/api/cookbook/state`

## `GET /api/cookbook/tasks/status`
- handler: `cookbook_tasks_status` — `routes/cookbook_routes.py:4103`
- **JS callers:**
  - `static/js/cookbookRunning.js:4217` → `/api/cookbook/tasks/status`

## `POST /api/cookbook/test-ssh`
- handler: `test_cookbook_ssh` — `routes/cookbook_routes.py:839`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:2460` → `/api/cookbook/test-ssh`

## `GET /api/cookbook/vllm-recipe`
- handler: `vllm_recipe` — `routes/cookbook_routes.py:3987`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/cookbook/vllm-recipe-manifest`
- handler: `vllm_recipe_manifest` — `routes/cookbook_routes.py:3927`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/db/stats`
- handler: `get_database_stats` — `routes/diagnostics_routes.py:57`
- **JS callers:**
  - `static/js/slashCommands.js:1999` → `/api/db/stats`

## `GET /api/default-chat`
- handler: `get_default_chat` — `routes/model_routes.py:2780`
- **JS callers:**
  - `static/app.js:232` → `/api/default-chat`
  - `static/js/chat.js:2804` → `/api/default-chat`
  - `static/js/editor/nl-edit.js:13` → `/api/default-chat`
  - `static/js/emailInbox.js:1437` → `/api/default-chat`
  - `static/js/features/notes/infrastructure/http.js:25` → `/api/default-chat`
  - `static/js/gallery.js:1742` → `/api/default-chat`
  - `static/js/modelPicker.js:141` → `/api/default-chat`
  - `static/js/sessions.js:2645` → `/api/default-chat`
  - `static/js/slashCommands.js:967` → `/api/default-chat`
  - `static/js/tasks.js:2676` → `/api/default-chat`

## `GET /api/diagnostics/logs`
- handler: `get_diagnostics_logs` — `routes/diagnostics_routes.py:33`
- **JS callers:**
  - `static/js/admin.js:3915` → `/api/diagnostics/logs?limit=${limit}`
  - `static/js/admin.js:3915` → `/api/diagnostics/logs?limit=`

## `GET /api/diagnostics/services`
- handler: `get_service_health` — `routes/diagnostics_routes.py:25`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/discover`
- handler: `discover_local` — `routes/model_routes.py:2075`
- **JS callers:**
  - `static/js/admin.js:2562` → `/api/discover`

## `POST /api/document`
- handler: `create_document` — `routes/document/document_routes.py:111`
- **JS callers:**
  - `static/js/chat.js:3179` → `/api/document`
  - `static/js/chat.js:3179` → `/api/document`
  - `static/js/chat.js:9439` → `/api/document`
  - `static/js/chat.js:9439` → `/api/document`
  - `static/js/document.js:7296` → `/api/document`
  - `static/js/document.js:7296` → `/api/document`
  - `static/js/document.js:12003` → `/api/document`
  - `static/js/document.js:12003` → `/api/document`
  - `static/js/document.js:12031` → `/api/document`
  - `static/js/document.js:12031` → `/api/document`
  - `static/js/document.js:14949` → `/api/document`
  - `static/js/document.js:14949` → `/api/document`
  - `static/js/document.js:15193` → `/api/document`
  - `static/js/document.js:15193` → `/api/document`
  - `static/js/documentLibrary.js:1309` → `/api/document`
  - `static/js/documentLibrary.js:1309` → `/api/document`
  - `static/js/documentLibrary.js:1786` → `/api/document`
  - `static/js/documentLibrary.js:1786` → `/api/document`
  - `static/js/documentLibrary.js:1796` → `/api/document`
  - `static/js/documentLibrary.js:1796` → `/api/document`
  - … +4 more

## `POST /api/document`
- handler: `create_document` — `tests/test_codex_ssh_host_validation.py:232`
- **JS callers:**
  - `static/js/chat.js:3179` → `/api/document`
  - `static/js/chat.js:3179` → `/api/document`
  - `static/js/chat.js:9439` → `/api/document`
  - `static/js/chat.js:9439` → `/api/document`
  - `static/js/document.js:7296` → `/api/document`
  - `static/js/document.js:7296` → `/api/document`
  - `static/js/document.js:12003` → `/api/document`
  - `static/js/document.js:12003` → `/api/document`
  - `static/js/document.js:12031` → `/api/document`
  - `static/js/document.js:12031` → `/api/document`
  - `static/js/document.js:14949` → `/api/document`
  - `static/js/document.js:14949` → `/api/document`
  - `static/js/document.js:15193` → `/api/document`
  - `static/js/document.js:15193` → `/api/document`
  - `static/js/documentLibrary.js:1309` → `/api/document`
  - `static/js/documentLibrary.js:1309` → `/api/document`
  - `static/js/documentLibrary.js:1786` → `/api/document`
  - `static/js/documentLibrary.js:1786` → `/api/document`
  - `static/js/documentLibrary.js:1796` → `/api/document`
  - `static/js/documentLibrary.js:1796` → `/api/document`
  - … +4 more

## `DELETE /api/document/{doc_id}`
- handler: `delete_document` — `routes/document/document_routes.py:962`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}`
- handler: `get_document` — `routes/document/document_routes.py:660`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PATCH /api/document/{doc_id}`
- handler: `patch_document` — `routes/document/document_routes.py:923`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PUT /api/document/{doc_id}`
- handler: `update_document` — `routes/document/document_routes.py:848`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/document/{doc_id}/ai-fill-annotations`
- handler: `ai_fill_annotations` — `routes/document/document_routes.py:1463`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/document/{doc_id}/archive`
- handler: `archive_document` — `routes/document/document_routes.py:700`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/convert-original/{target}`
- handler: `convert_original_document` — `routes/document/document_routes.py:432`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/export-pdf`
- handler: `export_pdf` — `routes/document/document_routes.py:1703`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/document/{doc_id}/export-pdf/preview`
- handler: `export_pdf_preview` — `routes/document/document_routes.py:1289`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/document/{doc_id}/extract-pdf-text`
- handler: `extract_pdf_text` — `routes/document/document_routes.py:716`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/page/{page_no}.png`
- handler: `render_page_png` — `routes/document/document_routes.py:1422`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/document/{doc_id}/prepare-signed-reply`
- handler: `prepare_signed_reply` — `routes/document/document_routes.py:1839`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/render-docx`
- handler: `render_docx` — `routes/document/document_routes.py:402`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/render-pages`
- handler: `render_pages` — `routes/document/document_routes.py:1351`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/render-pdf`
- handler: `render_pdf` — `routes/document/document_routes.py:1603`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/render-pdf`
- handler: `render_pdf` — `tests/test_security_headers_pdf_preview.py:17`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/document/{doc_id}/restore/{num}`
- handler: `restore_version` — `routes/document/document_routes.py:1036`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/version/{num}`
- handler: `get_version` — `routes/document/document_routes.py:1015`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/versions`
- handler: `list_versions` — `routes/document/document_routes.py:990`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/visual-report`
- handler: `document_visual_report` — `routes/document/document_routes.py:674`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/documents/ai-tidy`
- handler: `ai_tidy_documents` — `routes/document/document_routes.py:1192`
- **JS callers:**
  - `static/js/documentLibrary.js:3569` → `/api/documents/ai-tidy`

## `POST /api/documents/export-zip`
- handler: `documents_export_zip` — `routes/document/document_routes.py:776`
- **JS callers:**
  - `static/js/documentLibrary.js:1533` → `/api/documents/export-zip`

## `POST /api/documents/import-docx`
- handler: `import_docx` — `routes/document/document_routes.py:329`
- **JS callers:**
  - `static/js/document.js:15178` → `/api/documents/import-docx`
  - `static/js/documentLibrary.js:1763` → `/api/documents/import-docx`

## `POST /api/documents/import-pdf`
- handler: `import_pdf` — `routes/document/document_routes.py:227`
- **JS callers:**
  - `static/js/chat.js:9434` → `/api/documents/import-pdf`
  - `static/js/document.js:15169` → `/api/documents/import-pdf`
  - `static/js/document.js:16047` → `/api/documents/import-pdf`
  - `static/js/documentLibrary.js:1745` → `/api/documents/import-pdf`

## `GET /api/documents/library`
- handler: `documents_library` — `routes/document/document_routes.py:513`
- **JS callers:**
  - `static/js/document.js:5401` → `/api/documents/library?`
  - `static/js/document.js:5401` → `/api/documents/library?`
  - `static/js/documentLibrary.js:458` → `/api/documents/library?`
  - `static/js/documentLibrary.js:458` → `/api/documents/library?`
  - `static/js/documentLibrary.js:2591` → `/api/documents/library?archived=true&limit=50`
  - `static/js/documentLibrary.js:2591` → `/api/documents/library?archived=true&limit=50`
  - `static/js/sessions.js:3955` → `/api/documents/library?`
  - `static/js/sessions.js:3955` → `/api/documents/library?`
  - `static/js/slashCommands.js:4833` → `/api/documents/library?limit=1&sort=recent`
  - `static/js/slashCommands.js:4833` → `/api/documents/library?limit=1&sort=recent`

## `GET /api/documents/library`
- handler: `documents_library` — `tests/test_codex_ssh_host_validation.py:108`
- **JS callers:**
  - `static/js/document.js:5401` → `/api/documents/library?`
  - `static/js/document.js:5401` → `/api/documents/library?`
  - `static/js/documentLibrary.js:458` → `/api/documents/library?`
  - `static/js/documentLibrary.js:458` → `/api/documents/library?`
  - `static/js/documentLibrary.js:2591` → `/api/documents/library?archived=true&limit=50`
  - `static/js/documentLibrary.js:2591` → `/api/documents/library?archived=true&limit=50`
  - `static/js/sessions.js:3955` → `/api/documents/library?`
  - `static/js/sessions.js:3955` → `/api/documents/library?`
  - `static/js/slashCommands.js:4833` → `/api/documents/library?limit=1&sort=recent`
  - `static/js/slashCommands.js:4833` → `/api/documents/library?limit=1&sort=recent`

## `POST /api/documents/tidy`
- handler: `tidy_documents` — `routes/document/document_routes.py:1077`
- **JS callers:**
  - `static/js/documentLibrary.js:3558` → `/api/documents/tidy`

## `GET /api/documents/{session_id}`
- handler: `list_documents` — `routes/document/document_routes.py:636`
- **JS callers:**
  - `static/js/chat.js:9434` → `/api/documents/import-pdf`
  - `static/js/document.js:5401` → `/api/documents/library?`
  - `static/js/document.js:15169` → `/api/documents/import-pdf`
  - `static/js/document.js:15178` → `/api/documents/import-docx`
  - `static/js/document.js:16047` → `/api/documents/import-pdf`
  - `static/js/documentLibrary.js:458` → `/api/documents/library?`
  - `static/js/documentLibrary.js:1533` → `/api/documents/export-zip`
  - `static/js/documentLibrary.js:1745` → `/api/documents/import-pdf`
  - `static/js/documentLibrary.js:1763` → `/api/documents/import-docx`
  - `static/js/documentLibrary.js:2591` → `/api/documents/library?archived=true&limit=50`
  - `static/js/documentLibrary.js:3558` → `/api/documents/tidy`
  - `static/js/documentLibrary.js:3569` → `/api/documents/ai-tidy`
  - `static/js/sessions.js:3955` → `/api/documents/library?`
  - `static/js/slashCommands.js:4833` → `/api/documents/library?limit=1&sort=recent`

## `GET /api/editor-drafts`
- handler: `list_drafts` — `routes/editor_draft_routes.py:132`
- **JS callers:**
  - `static/js/gallery.js:1033` → `/api/editor-drafts`
  - `static/js/galleryEditor.js:4725` → `/api/editor-drafts`
  - `static/js/galleryEditor.js:4737` → `/api/editor-drafts`
  - `static/js/galleryEditor.js:4816` → `/api/editor-drafts`

## `POST /api/editor-drafts`
- handler: `create_draft` — `routes/editor_draft_routes.py:162`
- **JS callers:**
  - `static/js/gallery.js:1033` → `/api/editor-drafts`
  - `static/js/galleryEditor.js:4725` → `/api/editor-drafts`
  - `static/js/galleryEditor.js:4737` → `/api/editor-drafts`
  - `static/js/galleryEditor.js:4816` → `/api/editor-drafts`

## `DELETE /api/editor-drafts/{draft_id}`
- handler: `delete_draft` — `routes/editor_draft_routes.py:229`
- **JS callers:**
  - `static/js/galleryEditor.js:4717` → `/api/editor-drafts/${encodeURIComponent(draftIdAtStart)}`
  - `static/js/galleryEditor.js:4801` → `/api/editor-drafts/${encodeURIComponent(draftId)}`
  - `static/js/galleryEditor.js:4830` → `/api/editor-drafts/${encodeURIComponent(draftId)}`

## `GET /api/editor-drafts/{draft_id}`
- handler: `get_draft` — `routes/editor_draft_routes.py:145`
- **JS callers:**
  - `static/js/galleryEditor.js:4717` → `/api/editor-drafts/${encodeURIComponent(draftIdAtStart)}`
  - `static/js/galleryEditor.js:4801` → `/api/editor-drafts/${encodeURIComponent(draftId)}`
  - `static/js/galleryEditor.js:4830` → `/api/editor-drafts/${encodeURIComponent(draftId)}`

## `PUT /api/editor-drafts/{draft_id}`
- handler: `update_draft` — `routes/editor_draft_routes.py:193`
- **JS callers:**
  - `static/js/galleryEditor.js:4717` → `/api/editor-drafts/${encodeURIComponent(draftIdAtStart)}`
  - `static/js/galleryEditor.js:4801` → `/api/editor-drafts/${encodeURIComponent(draftId)}`
  - `static/js/galleryEditor.js:4830` → `/api/editor-drafts/${encodeURIComponent(draftId)}`

## `POST /api/editor/agent`
- handler: `editor_agent` — `routes/editor_agent_routes.py:1688`
- **JS callers:**
  - `static/js/editor/editor-agent.js:21` → `/api/editor/agent`
  - `static/js/galleryEditor.js:12867` → `/api/editor/agent`

## `GET /api/editor/agent-models`
- handler: `editor_agent_models` — `routes/editor_agent_routes.py:2041`
- **JS callers:**
  - `static/js/editor/ai-models.js:202` → `/api/editor/agent-models`

## `POST /api/editor/bridge/await`
- handler: `bridge_await` — `routes/editor_agent_routes.py:1626`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/editor/bridge/command`
- handler: `bridge_command` — `routes/editor_agent_routes.py:1534`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/editor/bridge/events`
- handler: `bridge_events` — `routes/editor_agent_routes.py:1581`
- **JS callers:**
  - `static/js/editor/editor-bridge.js:27` → `/api/editor/bridge/events?session=`

## `POST /api/editor/bridge/result`
- handler: `bridge_result` — `routes/editor_agent_routes.py:1602`
- **JS callers:**
  - `static/js/editor/editor-bridge.js:28` → `/api/editor/bridge/result`

## `GET /api/editor/image-models`
- handler: `editor_image_models` — `routes/editor_agent_routes.py:1977`
- **JS callers:**
  - `static/js/editor/ai-models.js:251` → `/api/editor/image-models`
  - `static/js/gallery.js:2652` → `/api/editor/image-models`

## `POST /api/editor/plan`
- handler: `plan` — `routes/editor_agent_routes.py:1429`
- **JS callers:**
  - `static/js/editor/nl-edit.js:11` → `/api/editor/plan`

## `POST /api/editor/self-check`
- handler: `editor_self_check` — `routes/editor_agent_routes.py:2079`
- **JS callers:**
  - `static/js/galleryEditor.js:2651` → `/api/editor/self-check`

## `GET /api/editor/style-guide`
- handler: `style_guide_route` — `routes/editor_agent_routes.py:1968`
- **JS callers:**
  - `static/js/editor/nl-edit.js:161` → `/api/editor/style-guide`
  - `static/js/editor/nl-edit.js:452` → `/api/editor/style-guide`

## `GET /api/email/accounts`
- handler: `list_email_accounts` — `routes/email/email_routes.py:7384`
- **JS callers:**
  - `static/js/document.js:99` → `/api/email/accounts`
  - `static/js/emailLibrary/index.js:2136` → `/api/email/accounts`
  - `static/js/emailLibrary/index.js:2327` → `/api/email/accounts`
  - `static/js/emailLibrary/index.js:3130` → `/api/email/accounts`
  - `static/js/settings.js:2023` → `/api/email/accounts`
  - `static/js/settings.js:2033` → `/api/email/accounts`
  - `static/js/settings.js:2137` → `/api/email/accounts`
  - `static/js/settings.js:2472` → `/api/email/accounts`
  - `static/js/settings.js:2653` → `/api/email/accounts`
  - `static/js/settings.js:2705` → `/api/email/accounts`
  - `static/js/settings.js:3231` → `/api/email/accounts`
  - `static/js/settings.js:4000` → `/api/email/accounts`
  - `static/js/settings.js:4291` → `/api/email/accounts`
  - `static/js/settings.js:4474` → `/api/email/accounts`
  - `static/js/tasks.js:264` → `/api/email/accounts`

## `POST /api/email/accounts`
- handler: `create_email_account` — `routes/email/email_routes.py:7428`
- **JS callers:**
  - `static/js/document.js:99` → `/api/email/accounts`
  - `static/js/emailLibrary/index.js:2136` → `/api/email/accounts`
  - `static/js/emailLibrary/index.js:2327` → `/api/email/accounts`
  - `static/js/emailLibrary/index.js:3130` → `/api/email/accounts`
  - `static/js/settings.js:2023` → `/api/email/accounts`
  - `static/js/settings.js:2033` → `/api/email/accounts`
  - `static/js/settings.js:2137` → `/api/email/accounts`
  - `static/js/settings.js:2472` → `/api/email/accounts`
  - `static/js/settings.js:2653` → `/api/email/accounts`
  - `static/js/settings.js:2705` → `/api/email/accounts`
  - `static/js/settings.js:3231` → `/api/email/accounts`
  - `static/js/settings.js:4000` → `/api/email/accounts`
  - `static/js/settings.js:4291` → `/api/email/accounts`
  - `static/js/settings.js:4474` → `/api/email/accounts`
  - `static/js/tasks.js:264` → `/api/email/accounts`

## `POST /api/email/accounts/test`
- handler: `test_account_config` — `routes/email/email_routes.py:7722`
- **JS callers:**
  - `static/js/settings.js:4415` → `/api/email/accounts/test`

## `DELETE /api/email/accounts/{account_id}`
- handler: `delete_email_account` — `routes/email/email_routes.py:7531`
- **JS callers:**
  - `static/js/settings.js:2514` → `/api/email/accounts/${id}`
  - `static/js/settings.js:3366` → `/api/email/accounts/${id}`
  - `static/js/settings.js:4415` → `/api/email/accounts/test`

## `PUT /api/email/accounts/{account_id}`
- handler: `update_email_account` — `routes/email/email_routes.py:7488`
- **JS callers:**
  - `static/js/settings.js:2514` → `/api/email/accounts/${id}`
  - `static/js/settings.js:3366` → `/api/email/accounts/${id}`
  - `static/js/settings.js:4415` → `/api/email/accounts/test`

## `POST /api/email/accounts/{account_id}/set-default`
- handler: `set_default_account` — `routes/email/email_routes.py:7787`
- **JS callers:**
  - `static/js/settings.js:2504` → `/api/email/accounts/${id}/set-default`

## `POST /api/email/ai-reply`
- handler: `ai_reply` — `routes/email/email_routes.py:6853`
- **JS callers:**
  - `static/js/document.js:6823` → `/api/email/ai-reply`
  - `static/js/emailInbox.js:872` → `/api/email/ai-reply`

## `POST /api/email/archive/{uid}`
- handler: `archive_email` — `routes/email/email_routes.py:5258`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/attachment-as-doc/{uid}/{index}`
- handler: `attachment_as_doc` — `routes/email/email_routes.py:4810`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/attachment-path/{uid}/{index}`
- handler: `get_attachment_path` — `routes/email/email_routes.py:5171`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/attachment/{uid}/{index}`
- handler: `download_attachment` — `routes/email/email_routes.py:4122`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/attachments-download-bulk`
- handler: `download_bulk_attachments` — `routes/email/email_routes.py:4216`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/attachments-download/{uid}`
- handler: `download_all_attachments` — `routes/email/email_routes.py:4163`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/attachments/{uid}`
- handler: `list_attachments` — `routes/email/email_routes.py:4094`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/clear-answered/{uid}`
- handler: `clear_answered` — `routes/email/email_routes.py:5639`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/compose-from-attachment/{uid}/{index}`
- handler: `compose_from_attachment` — `routes/email/email_routes.py:5826`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/compose-from-odysseus`
- handler: `compose_from_odysseus` — `routes/email/email_routes.py:5750`
- **JS callers:**
  - `static/js/document.js:5275` → `/api/email/compose-from-odysseus`

## `POST /api/email/compose-from-odysseus-zip`
- handler: `compose_from_odysseus_zip` — `routes/email/email_routes.py:5774`
- **JS callers:**
  - `static/js/document.js:5296` → `/api/email/compose-from-odysseus-zip`

## `POST /api/email/compose-upload`
- handler: `compose_upload` — `routes/email/email_routes.py:5654`
- **JS callers:**
  - `static/js/document.js:5163` → `/api/email/compose-upload`

## `DELETE /api/email/compose-upload/{token}`
- handler: `delete_compose_upload` — `routes/email/email_routes.py:5866`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/config`
- handler: `get_email_config` — `routes/email/email_routes.py:7237`
- **JS callers:**
  - `static/js/emailLibrary/aiReply.js:31` → `/api/email/config`
  - `static/js/emailLibrary/settingsPage.js:63` → `/api/email/config`
  - `static/js/emailLibrary/settingsPage.js:262` → `/api/email/config`
  - `static/js/emailLibrary/settingsPage.js:661` → `/api/email/config`
  - `static/js/emailLibrary/settingsPage.js:721` → `/api/email/config`
  - `static/js/settings.js:2022` → `/api/email/config`
  - `static/js/settings.js:2767` → `/api/email/config`
  - `static/js/settings.js:2807` → `/api/email/config`

## `PUT /api/email/config`
- handler: `update_email_config` — `routes/email/email_routes.py:7281`
- **JS callers:**
  - `static/js/emailLibrary/aiReply.js:31` → `/api/email/config`
  - `static/js/emailLibrary/settingsPage.js:63` → `/api/email/config`
  - `static/js/emailLibrary/settingsPage.js:262` → `/api/email/config`
  - `static/js/emailLibrary/settingsPage.js:661` → `/api/email/config`
  - `static/js/emailLibrary/settingsPage.js:721` → `/api/email/config`
  - `static/js/settings.js:2022` → `/api/email/config`
  - `static/js/settings.js:2767` → `/api/email/config`
  - `static/js/settings.js:2807` → `/api/email/config`

## `GET /api/email/contacts`
- handler: `list_contacts` — `routes/email/email_routes.py:3492`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/delete-bulk`
- handler: `delete_email_bulk` — `routes/email/email_routes.py:5343`
- **JS callers:**
  - `static/js/emailLibrary/menus.js:710` → `/api/email/delete-bulk`
  - `static/js/emailLibrary/menus.js:831` → `/api/email/delete-bulk`

## `DELETE /api/email/delete-permanent/{uid}`
- handler: `delete_email_permanent` — `routes/email/email_routes.py:5327`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/email/delete/{uid}`
- handler: `delete_email` — `routes/email/email_routes.py:5276`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/draft`
- handler: `save_draft` — `routes/email/email_routes.py:6390`
- **JS callers:**
  - `static/js/document.js:6276` → `/api/email/draft`
  - `static/js/document.js:6536` → `/api/email/draft`

## `POST /api/email/extract-style`
- handler: `extract_writing_style` — `routes/email/email_routes.py:6471`
- **JS callers:**
  - `static/js/emailLibrary/settingsPage.js:845` → `/api/email/extract-style`
  - `static/js/settings.js:2872` → `/api/email/extract-style`

## `POST /api/email/flag/{uid}`
- handler: `flag_email` — `routes/email/email_routes.py:5218`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/folders`
- handler: `list_folders` — `routes/email/email_routes.py:5552`
- **JS callers:**
  - `static/js/emailInbox.js:454` → `/api/email/folders`
  - `static/js/emailLibrary/index.js:3521` → `/api/email/folders`

## `GET /api/email/inline-image/{uid}`
- handler: `inline_image` — `routes/email/email_routes.py:4759`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/list`
- handler: `list_emails` — `routes/email/email_routes.py:2888`
- **JS callers:**
  - `static/js/emailInbox.js:428` → `/api/email/list?folder=`
  - `static/js/emailInbox.js:435` → `/api/email/list?folder=`
  - `static/js/emailLibrary/attachments.js:7` → `/api/email/list`
  - `static/js/emailLibrary/index.js:2176` → `/api/email/list`
  - `static/js/emailLibrary/index.js:2220` → `/api/email/list`
  - `static/js/emailLibrary/index.js:4560` → `/api/email/list?`
  - `static/js/emailLibrary/index.js:5006` → `/api/email/list?folder=`
  - `static/js/emailLibrary/index.js:5133` → `/api/email/list?folder=`
  - `static/js/emailLibrary/index.js:5161` → `/api/email/list?folder=`

## `POST /api/email/mark-answered/{uid}`
- handler: `mark_answered` — `routes/email/email_routes.py:5623`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/mark-read/{uid}`
- handler: `mark_read` — `routes/email/email_routes.py:5238`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/mark-unread/{uid}`
- handler: `mark_unread` — `routes/email/email_routes.py:5203`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/messages-download-bulk`
- handler: `download_bulk_messages` — `routes/email/email_routes.py:4351`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/move/{uid}`
- handler: `move_email` — `routes/email/email_routes.py:5534`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/oauth/google/authorize`
- handler: `google_oauth_authorize` — `routes/email/email_routes.py:7810`
- **JS callers:**
  - `static/js/settings.js:2659` → `/api/email/oauth/google/authorize?account_id=`
  - `static/js/settings.js:4297` → `/api/email/oauth/google/authorize?account_id=`

## `GET /api/email/oauth/google/callback`
- handler: `google_oauth_callback` — `routes/email/email_routes.py:7834`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/email/odysseus/reminders`
- handler: `delete_odysseus_reminder_emails` — `routes/email/email_routes.py:5459`
- **JS callers:**
  - `static/js/emailLibrary/index.js:2776` → `/api/email/odysseus/reminders?permanent=1`

## `GET /api/email/pending`
- handler: `list_pending_agent_drafts` — `routes/email/email_routes.py:6041`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/email/pending/{sid}`
- handler: `cancel_agent_draft` — `routes/email/email_routes.py:6084`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/pending/{sid}/approve`
- handler: `approve_agent_draft` — `routes/email/email_routes.py:6060`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/read/{uid}`
- handler: `read_email_by_uid` — `routes/email/email_routes.py:3985`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/resolve-contact`
- handler: `resolve_contact` — `routes/email/email_routes.py:6105`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/schedule`
- handler: `schedule_email` — `routes/email/email_routes.py:5928`
- **JS callers:**
  - `static/js/document.js:7011` → `/api/email/schedule`

## `GET /api/email/scheduled`
- handler: `list_scheduled` — `routes/email/email_routes.py:5994`
- **JS callers:**
  - `static/js/emailLibrary/index.js:5191` → `/api/email/scheduled`

## `DELETE /api/email/scheduled/{sid}`
- handler: `cancel_scheduled` — `routes/email/email_routes.py:6017`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/search`
- handler: `search_emails` — `routes/email/email_routes.py:3540`
- **JS callers:**
  - `static/js/emailLibrary/index.js:4550` → `/api/email/search?`

## `POST /api/email/send`
- handler: `send_email` — `routes/email/email_routes.py:6153`
- **JS callers:**
  - `static/js/document.js:6389` → `/api/email/send`

## `GET /api/email/style`
- handler: `get_writing_style` — `routes/email/email_routes.py:7212`
- **JS callers:**
  - `static/js/document.js:11367` → `/api/email/style`
  - `static/js/emailLibrary/settingsPage.js:273` → `/api/email/style`
  - `static/js/emailLibrary/settingsPage.js:799` → `/api/email/style`
  - `static/js/settings.js:2756` → `/api/email/style`
  - `static/js/settings.js:2900` → `/api/email/style`

## `PUT /api/email/style`
- handler: `update_writing_style` — `routes/email/email_routes.py:7223`
- **JS callers:**
  - `static/js/document.js:11367` → `/api/email/style`
  - `static/js/emailLibrary/settingsPage.js:273` → `/api/email/style`
  - `static/js/emailLibrary/settingsPage.js:799` → `/api/email/style`
  - `static/js/settings.js:2756` → `/api/email/style`
  - `static/js/settings.js:2900` → `/api/email/style`

## `POST /api/email/summarize`
- handler: `summarize_email` — `routes/email/email_routes.py:6585`
- **JS callers:**
  - `static/js/emailLibrary/reader.js:635` → `/api/email/summarize`

## `POST /api/email/translate`
- handler: `translate_email` — `routes/email/email_routes.py:6703`
- **JS callers:**
  - `static/js/emailLibrary/index.js:6312` → `/api/email/translate`

## `GET /api/email/unread-state`
- handler: `unread_state` — `routes/email/email_routes.py:3030`
- **JS callers:**
  - `static/js/emailInbox.js:337` → `/api/email/unread-state`
  - `static/js/emailInbox.js:384` → `/api/email/unread-state`
  - `static/js/emailLibrary/index.js:3282` → `/api/email/unread-state`
  - `static/js/emailLibrary/index.js:4993` → `/api/email/unread-state`

## `POST /api/email/unsubscribe/cleanup`
- handler: `cleanup_unsubscribe_candidates` — `routes/email/email_routes.py:3404`
- **JS callers:**
  - `static/js/emailLibrary/unsubscribe.js:555` → `/api/email/unsubscribe/cleanup`
  - `static/js/emailLibrary/unsubscribe.js:611` → `/api/email/unsubscribe/cleanup`

## `POST /api/email/unsubscribe/execute`
- handler: `execute_unsubscribe` — `routes/email/email_routes.py:3309`
- **JS callers:**
  - `static/js/emailLibrary/unsubscribe.js:1027` → `/api/email/unsubscribe/execute`
  - `static/js/emailLibrary/unsubscribe.js:1179` → `/api/email/unsubscribe/execute`

## `GET /api/email/unsubscribe/scan`
- handler: `scan_unsubscribe_candidates` — `routes/email/email_routes.py:3290`
- **JS callers:**
  - `static/js/emailLibrary/unsubscribe.js:852` → `/api/email/unsubscribe/scan`

## `GET /api/email/urgency-state`
- handler: `get_email_urgency_state` — `routes/email/email_routes.py:7362`
- **JS callers:**
  - `static/js/emailInbox.js:338` → `/api/email/urgency-state`

## `POST /api/email/{uid}/unflag-spam`
- handler: `unflag_spam` — `routes/email/email_routes.py:3104`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/embeddings/endpoint`
- handler: `clear_endpoint` — `routes/embedding_routes.py:336`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/embeddings/endpoint`
- handler: `get_endpoint` — `routes/embedding_routes.py:245`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/embeddings/endpoint`
- handler: `set_endpoint` — `routes/embedding_routes.py:256`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/embeddings/models`
- handler: `list_models` — `routes/embedding_routes.py:116`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/embeddings/models/{model_name:path}`
- handler: `delete_model` — `routes/embedding_routes.py:212`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/embeddings/models/{model_name:path}/download`
- handler: `download_model` — `routes/embedding_routes.py:155`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/embeddings/models/{model_name:path}/status`
- handler: `download_status` — `routes/embedding_routes.py:191`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/emoji/{code}.svg`
- handler: `emoji_svg` — `routes/emoji_routes.py:76`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/export`
- handler: `export_data` — `routes/backup_routes.py:20`
- **JS callers:**
  - `static/js/admin.js:3714` → `/api/export`

## `GET /api/fonts/custom`
- handler: `list_custom_fonts` — `routes/font_routes.py:38`
- **JS callers:**
  - `static/js/theme.js:1343` → `/api/fonts/custom`

## `POST /api/gallery/ai-tag-batch`
- handler: `ai_tag_batch` — `routes/gallery/gallery_routes.py:1408`
- **JS callers:**
  - `static/js/gallery.js:2732` → `/api/gallery/ai-tag-batch?`

## `POST /api/gallery/ai-upscale`
- handler: `gallery_ai_upscale` — `routes/gallery/gallery_routes.py:1067`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/gallery/albums`
- handler: `list_albums` — `routes/gallery/gallery_routes.py:1323`
- **JS callers:**
  - `static/js/gallery.js:246` → `/api/gallery/albums`
  - `static/js/gallery.js:413` → `/api/gallery/albums`
  - `static/js/gallery.js:895` → `/api/gallery/albums`
  - `static/js/gallery.js:930` → `/api/gallery/albums`

## `POST /api/gallery/albums`
- handler: `create_album` — `routes/gallery/gallery_routes.py:1361`
- **JS callers:**
  - `static/js/gallery.js:246` → `/api/gallery/albums`
  - `static/js/gallery.js:413` → `/api/gallery/albums`
  - `static/js/gallery.js:895` → `/api/gallery/albums`
  - `static/js/gallery.js:930` → `/api/gallery/albums`

## `DELETE /api/gallery/albums/{album_id}`
- handler: `delete_album` — `routes/gallery/gallery_routes.py:3044`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PUT /api/gallery/albums/{album_id}`
- handler: `update_album` — `routes/gallery/gallery_routes.py:3015`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/albums/{album_id}/add`
- handler: `add_to_album` — `routes/gallery/gallery_routes.py:3060`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/albums/{album_id}/remove`
- handler: `remove_from_album` — `routes/gallery/gallery_routes.py:3077`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/clear-ai-tags`
- handler: `clear_gallery_ai_tags` — `routes/gallery/gallery_routes.py:1584`
- **JS callers:**
  - `static/js/gallery.js:1906` → `/api/gallery/clear-ai-tags?image_id=`
  - `static/js/gallery.js:2822` → `/api/gallery/clear-ai-tags`

## `POST /api/gallery/clear-user-tags`
- handler: `clear_gallery_user_tags` — `routes/gallery/gallery_routes.py:1559`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/dedupe-tags`
- handler: `dedupe_gallery_tags` — `routes/gallery/gallery_routes.py:1611`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/download-zip`
- handler: `gallery_download_zip` — `routes/gallery/gallery_routes.py:1504`
- **JS callers:**
  - `static/js/gallery.js:3097` → `/api/gallery/download-zip`

## `GET /api/gallery/library`
- handler: `gallery_library` — `routes/gallery/gallery_routes.py:1180`
- **JS callers:**
  - `static/js/document.js:5400` → `/api/gallery/library?`
  - `static/js/document.js:5572` → `/api/gallery/library?sort=recent&limit=30`
  - `static/js/editor/wire-import.js:198` → `/api/gallery/library?limit=50`
  - `static/js/gallery.js:215` → `/api/gallery/library?`

## `GET /api/gallery/stats`
- handler: `gallery_stats` — `routes/gallery/gallery_routes.py:1382`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/style-transfer`
- handler: `gallery_style_transfer` — `routes/gallery/gallery_routes.py:1111`
- **JS callers:**
  - `static/js/editor/ai-tools-misc.js:183` → `/api/gallery/style-transfer`

## `GET /api/gallery/tags`
- handler: `gallery_tags` — `routes/gallery/gallery_routes.py:1158`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/upload`
- handler: `gallery_upload` — `routes/gallery/gallery_routes.py:859`
- **JS callers:**
  - `static/js/gallery.js:327` → `/api/gallery/upload`
  - `static/js/galleryEditor.js:13240` → `/api/gallery/upload`

## `DELETE /api/gallery/{image_id}`
- handler: `delete_gallery_image` — `routes/gallery/gallery_routes.py:1647`
- **JS callers:**
  - `static/js/chatRenderer.js:2195` → `/api/gallery/${encodeURIComponent(imageId)}`
  - `static/js/document.js:5400` → `/api/gallery/library?`
  - `static/js/document.js:5572` → `/api/gallery/library?sort=recent&limit=30`
  - `static/js/editor/ai-tools-misc.js:183` → `/api/gallery/style-transfer`
  - `static/js/editor/wire-import.js:198` → `/api/gallery/library?limit=50`
  - `static/js/gallery.js:215` → `/api/gallery/library?`
  - `static/js/gallery.js:246` → `/api/gallery/albums`
  - `static/js/gallery.js:327` → `/api/gallery/upload`
  - `static/js/gallery.js:413` → `/api/gallery/albums`
  - `static/js/gallery.js:895` → `/api/gallery/albums`
  - `static/js/gallery.js:930` → `/api/gallery/albums`
  - `static/js/gallery.js:1906` → `/api/gallery/clear-ai-tags?image_id=`
  - `static/js/gallery.js:2732` → `/api/gallery/ai-tag-batch?`
  - `static/js/gallery.js:2822` → `/api/gallery/clear-ai-tags`
  - `static/js/gallery.js:3097` → `/api/gallery/download-zip`
  - `static/js/galleryEditor.js:13240` → `/api/gallery/upload`

## `GET /api/gallery/{image_id}`
- handler: `get_gallery_image` — `routes/gallery/gallery_routes.py:1431`
- **JS callers:**
  - `static/js/chatRenderer.js:2195` → `/api/gallery/${encodeURIComponent(imageId)}`
  - `static/js/document.js:5400` → `/api/gallery/library?`
  - `static/js/document.js:5572` → `/api/gallery/library?sort=recent&limit=30`
  - `static/js/editor/ai-tools-misc.js:183` → `/api/gallery/style-transfer`
  - `static/js/editor/wire-import.js:198` → `/api/gallery/library?limit=50`
  - `static/js/gallery.js:215` → `/api/gallery/library?`
  - `static/js/gallery.js:246` → `/api/gallery/albums`
  - `static/js/gallery.js:327` → `/api/gallery/upload`
  - `static/js/gallery.js:413` → `/api/gallery/albums`
  - `static/js/gallery.js:895` → `/api/gallery/albums`
  - `static/js/gallery.js:930` → `/api/gallery/albums`
  - `static/js/gallery.js:1906` → `/api/gallery/clear-ai-tags?image_id=`
  - `static/js/gallery.js:2732` → `/api/gallery/ai-tag-batch?`
  - `static/js/gallery.js:2822` → `/api/gallery/clear-ai-tags`
  - `static/js/gallery.js:3097` → `/api/gallery/download-zip`
  - `static/js/galleryEditor.js:13240` → `/api/gallery/upload`

## `PATCH /api/gallery/{image_id}`
- handler: `patch_gallery_image` — `routes/gallery/gallery_routes.py:1452`
- **JS callers:**
  - `static/js/chatRenderer.js:2195` → `/api/gallery/${encodeURIComponent(imageId)}`
  - `static/js/document.js:5400` → `/api/gallery/library?`
  - `static/js/document.js:5572` → `/api/gallery/library?sort=recent&limit=30`
  - `static/js/editor/ai-tools-misc.js:183` → `/api/gallery/style-transfer`
  - `static/js/editor/wire-import.js:198` → `/api/gallery/library?limit=50`
  - `static/js/gallery.js:215` → `/api/gallery/library?`
  - `static/js/gallery.js:246` → `/api/gallery/albums`
  - `static/js/gallery.js:327` → `/api/gallery/upload`
  - `static/js/gallery.js:413` → `/api/gallery/albums`
  - `static/js/gallery.js:895` → `/api/gallery/albums`
  - `static/js/gallery.js:930` → `/api/gallery/albums`
  - `static/js/gallery.js:1906` → `/api/gallery/clear-ai-tags?image_id=`
  - `static/js/gallery.js:2732` → `/api/gallery/ai-tag-batch?`
  - `static/js/gallery.js:2822` → `/api/gallery/clear-ai-tags`
  - `static/js/gallery.js:3097` → `/api/gallery/download-zip`
  - `static/js/galleryEditor.js:13240` → `/api/gallery/upload`

## `POST /api/gallery/{image_id}/ai-tag`
- handler: `ai_tag_image` — `routes/gallery/gallery_routes.py:3111`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/{image_id}/favorite`
- handler: `toggle_favorite` — `routes/gallery/gallery_routes.py:3097`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/{image_id}/rename`
- handler: `gallery_rename` — `routes/gallery/gallery_routes.py:984`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/{image_id}/replace`
- handler: `gallery_replace` — `routes/gallery/gallery_routes.py:941`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/{image_id}/rotate`
- handler: `gallery_rotate` — `routes/gallery/gallery_routes.py:1010`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/generated-image/{filename}`
- handler: `serve_generated_image` — `app.py:554`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/health`
- handler: `health_check` — `app.py:1055`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/history/{session_id}`
- handler: `get_session_history` — `routes/history/history_routes.py:416`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/history/{session_id}`
- handler: `history` — `tests/test_codex_chat_history.py:36`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/hwfit/image-models`
- handler: `get_image_models` — `routes/hwfit_routes.py:439`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:887` → `/api/hwfit/image-models?`

## `GET /api/hwfit/models`
- handler: `get_models` — `routes/hwfit_routes.py:217`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:887` → `/api/hwfit/models?`
  - `static/js/cookbook-hwfit.js:909` → `/api/hwfit/models?`

## `GET /api/hwfit/profiles`
- handler: `get_serve_profiles` — `routes/hwfit_routes.py:345`
- **JS callers:**
  - `static/js/cookbookServe.js:2052` → `/api/hwfit/profiles?`

## `GET /api/hwfit/system`
- handler: `get_system` — `routes/hwfit_routes.py:209`
- **JS callers:**
  - `static/js/cookbook.js:2777` → `/api/hwfit/system?`

## `POST /api/image/denoise`
- handler: `denoise_image` — `routes/gallery/gallery_routes.py:2523`
- **JS callers:**
  - `static/js/galleryEditor.js:1988` → `/api/image/denoise`

## `GET /api/image/edit-progress`
- handler: `edit_progress` — `routes/gallery/gallery_routes.py:2223`
- **JS callers:**
  - `static/js/galleryEditor.js:876` → `/api/image/edit-progress?request_id=${encodeURIComponent(requestId)}`
  - `static/js/galleryEditor.js:876` → `/api/image/edit-progress?request_id=`

## `POST /api/image/enhance-face`
- handler: `enhance_face` — `routes/gallery/gallery_routes.py:2930`
- **JS callers:**
  - `static/js/galleryEditor.js:2036` → `/api/image/enhance-face`

## `POST /api/image/extend`
- handler: `outpaint_extend` — `routes/gallery/gallery_routes.py:2218`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/image/generate`
- handler: `generate_image` — `routes/gallery/gallery_routes.py:2624`
- **JS callers:**
  - `static/js/editor/image-generation.js:32` → `/api/image/generate`

## `POST /api/image/harmonize`
- handler: `harmonize_image` — `routes/gallery/gallery_routes.py:2299`
- **JS callers:**
  - `static/js/editor/ai-tools-misc.js:74` → `/api/image/harmonize`
  - `static/js/galleryEditor.js:12623` → `/api/image/harmonize`

## `POST /api/image/inpaint`
- handler: `inpaint_proxy` — `routes/gallery/gallery_routes.py:1768`
- **JS callers:**
  - `static/js/editor/ai-inpaint.js:160` → `/api/image/inpaint`
  - `static/js/galleryEditor.js:12201` → `/api/image/inpaint`
  - `static/js/galleryEditor.js:12315` → `/api/image/inpaint`
  - `static/js/galleryEditor.js:12626` → `/api/image/inpaint`

## `POST /api/image/mask`
- handler: `smart_mask` — `routes/gallery/gallery_routes.py:2697`
- **JS callers:**
  - `static/js/galleryEditor.js:7575` → `/api/image/mask`

## `POST /api/image/outpaint`
- handler: `outpaint` — `routes/gallery/gallery_routes.py:2196`
- **JS callers:**
  - `static/js/galleryEditor.js:12338` → `/api/image/outpaint`

## `POST /api/image/remove-bg`
- handler: `remove_background` — `routes/gallery/gallery_routes.py:2829`
- **JS callers:**
  - `static/js/editor/ai-rembg.js:67` → `/api/image/remove-bg`
  - `static/js/editor/ai-tool-runner.js:79` → `/api/image/remove-bg`
  - `static/js/editor/wire-selection-controls.js:337` → `/api/image/remove-bg`
  - `static/js/galleryEditor.js:12617` → `/api/image/remove-bg`

## `POST /api/image/replace-background`
- handler: `replace_background` — `routes/gallery/gallery_routes.py:2173`
- **JS callers:**
  - `static/js/galleryEditor.js:12322` → `/api/image/replace-background`

## `POST /api/image/sharpen`
- handler: `sharpen_image` — `routes/gallery/gallery_routes.py:2499`
- **JS callers:**
  - `static/js/editor/ai-rembg.js:53` → `/api/image/sharpen`

## `POST /api/image/upscale-local`
- handler: `upscale_image_local` — `routes/gallery/gallery_routes.py:2576`
- **JS callers:**
  - `static/js/editor/ai-tools-misc.js:122` → `/api/image/upscale-local`
  - `static/js/galleryEditor.js:12624` → `/api/image/upscale-local`

## `POST /api/import`
- handler: `import_data` — `routes/backup_routes.py:64`
- **JS callers:**
  - `static/js/admin.js:3746` → `/api/import`

## `POST /api/inject_context/{session_id}`
- handler: `inject_context` — `routes/chat_routes.py:5621`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/mcp/oauth/authorize/{server_id}`
- handler: `oauth_authorize` — `routes/mcp/mcp_routes.py:454`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/mcp/oauth/callback`
- handler: `oauth_callback` — `routes/mcp/mcp_routes.py:508`
- **JS callers:**
  - `static/js/settings.js:4646` → `/api/mcp/oauth/callback?code=...`

## `POST /api/mcp/oauth/exchange/{server_id}`
- handler: `oauth_exchange` — `routes/mcp/mcp_routes.py:535`
- **JS callers:**
  - `static/js/settings.js:4655` → `/api/mcp/oauth/exchange/${id}`

## `GET /api/mcp/servers`
- handler: `list_servers` — `routes/mcp/mcp_routes.py:134`
- **JS callers:**
  - `static/js/admin.js:2939` → `/api/mcp/servers`
  - `static/js/admin.js:3257` → `/api/mcp/servers`
  - `static/js/settings.js:3232` → `/api/mcp/servers`
  - `static/js/settings.js:4673` → `/api/mcp/servers`
  - `static/js/settings.js:4699` → `/api/mcp/servers`
  - `static/js/settings.js:4820` → `/api/mcp/servers`
  - `static/js/slashCommands.js:1554` → `/api/mcp/servers`

## `POST /api/mcp/servers`
- handler: `add_server` — `routes/mcp/mcp_routes.py:172`
- **JS callers:**
  - `static/js/admin.js:2939` → `/api/mcp/servers`
  - `static/js/admin.js:3257` → `/api/mcp/servers`
  - `static/js/settings.js:3232` → `/api/mcp/servers`
  - `static/js/settings.js:4673` → `/api/mcp/servers`
  - `static/js/settings.js:4699` → `/api/mcp/servers`
  - `static/js/settings.js:4820` → `/api/mcp/servers`
  - `static/js/slashCommands.js:1554` → `/api/mcp/servers`

## `DELETE /api/mcp/servers/{server_id}`
- handler: `delete_server` — `routes/mcp/mcp_routes.py:377`
- **JS callers:**
  - `static/js/admin.js:2980` → `/api/mcp/servers/${btn.dataset.admMcpToggle}`
  - `static/js/admin.js:2987` → `/api/mcp/servers/${btn.dataset.admMcpDelete}`
  - `static/js/settings.js:3367` → `/api/mcp/servers/${id}`
  - `static/js/settings.js:4737` → `/api/mcp/servers/${srv.id}`

## `PATCH /api/mcp/servers/{server_id}`
- handler: `toggle_server` — `routes/mcp/mcp_routes.py:344`
- **JS callers:**
  - `static/js/admin.js:2980` → `/api/mcp/servers/${btn.dataset.admMcpToggle}`
  - `static/js/admin.js:2987` → `/api/mcp/servers/${btn.dataset.admMcpDelete}`
  - `static/js/settings.js:3367` → `/api/mcp/servers/${id}`
  - `static/js/settings.js:4737` → `/api/mcp/servers/${srv.id}`

## `POST /api/mcp/servers/{server_id}/reconnect`
- handler: `reconnect_server` — `routes/mcp/mcp_routes.py:308`
- **JS callers:**
  - `static/js/admin.js:2969` → `/api/mcp/servers/${btn.dataset.admMcpReconnect}/reconnect`
  - `static/js/settings.js:4727` → `/api/mcp/servers/${srv.id}/reconnect`

## `GET /api/mcp/servers/{server_id}/tools`
- handler: `list_server_tools` — `routes/mcp/mcp_routes.py:402`
- **JS callers:**
  - `static/js/admin.js:3013` → `/api/mcp/servers/${sid}/tools`
  - `static/js/admin.js:3057` → `/api/mcp/servers/${serverId}/tools`
  - `static/js/settings.js:4746` → `/api/mcp/servers/${srv.id}/tools`
  - `static/js/settings.js:4754` → `/api/mcp/servers/${srv.id}/tools`

## `PATCH /api/mcp/servers/{server_id}/tools`
- handler: `update_disabled_tools` — `routes/mcp/mcp_routes.py:422`
- **JS callers:**
  - `static/js/admin.js:3013` → `/api/mcp/servers/${sid}/tools`
  - `static/js/admin.js:3057` → `/api/mcp/servers/${serverId}/tools`
  - `static/js/settings.js:4746` → `/api/mcp/servers/${srv.id}/tools`
  - `static/js/settings.js:4754` → `/api/mcp/servers/${srv.id}/tools`

## `GET /api/mcp/tools`
- handler: `list_tools` — `routes/mcp/mcp_routes.py:395`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/memory/add`
- handler: `api_add_memory` — `routes/memory/memory_routes.py:101`
- **JS callers:**
  - `static/js/memory.js:1255` → `/api/memory/add`
  - `static/js/memory.js:1384` → `/api/memory/add`
  - `static/js/memory.js:1512` → `/api/memory/add`
  - `static/js/memory.js:1554` → `/api/memory/add`
  - `static/js/presets.js:1041` → `/api/memory/add`
  - `static/js/slashCommands.js:1590` → `/api/memory/add`

## `POST /api/memory/audit`
- handler: `api_audit_memories` — `routes/memory/memory_routes.py:292`
- **JS callers:**
  - `static/js/memory.js:631` → `/api/memory/audit`

## `GET /api/memory/by-session/{session_id}`
- handler: `get_memory_by_session` — `routes/memory/memory_routes.py:209`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/memory/debug`
- handler: `debug_memory_relevance` — `routes/memory/memory_routes.py:86`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/memory/extract`
- handler: `extract_memory` — `routes/memory/memory_routes.py:239`
- **JS callers:**
  - `static/js/memory.js:1333` → `/api/memory/extract`

## `POST /api/memory/import`
- handler: `import_memories_from_file` — `routes/memory/memory_routes.py:343`
- **JS callers:**
  - `static/js/memory.js:1452` → `/api/memory/import`

## `POST /api/memory/search`
- handler: `search_memories` — `routes/memory/memory_routes.py:155`
- **JS callers:**
  - `static/js/slashCommands.js:1643` → `/api/memory/search`

## `GET /api/memory/timeline`
- handler: `memory_timeline` — `routes/memory/memory_routes.py:171`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/memory/{memory_id}`
- handler: `delete_memory` — `routes/memory/memory_routes.py:557`
- **JS callers:**
  - `static/js/memory.js:631` → `/api/memory/audit`
  - `static/js/memory.js:1255` → `/api/memory/add`
  - `static/js/memory.js:1333` → `/api/memory/extract`
  - `static/js/memory.js:1384` → `/api/memory/add`
  - `static/js/memory.js:1452` → `/api/memory/import`
  - `static/js/memory.js:1512` → `/api/memory/add`
  - `static/js/memory.js:1554` → `/api/memory/add`
  - `static/js/presets.js:1041` → `/api/memory/add`
  - `static/js/slashCommands.js:1590` → `/api/memory/add`
  - `static/js/slashCommands.js:1643` → `/api/memory/search`

## `GET /api/memory/{memory_id}`
- handler: `get_memory_item` — `routes/memory/memory_routes.py:524`
- **JS callers:**
  - `static/js/memory.js:631` → `/api/memory/audit`
  - `static/js/memory.js:1255` → `/api/memory/add`
  - `static/js/memory.js:1333` → `/api/memory/extract`
  - `static/js/memory.js:1384` → `/api/memory/add`
  - `static/js/memory.js:1452` → `/api/memory/import`
  - `static/js/memory.js:1512` → `/api/memory/add`
  - `static/js/memory.js:1554` → `/api/memory/add`
  - `static/js/presets.js:1041` → `/api/memory/add`
  - `static/js/slashCommands.js:1590` → `/api/memory/add`
  - `static/js/slashCommands.js:1643` → `/api/memory/search`

## `PUT /api/memory/{memory_id}`
- handler: `update_memory` — `routes/memory/memory_routes.py:535`
- **JS callers:**
  - `static/js/memory.js:631` → `/api/memory/audit`
  - `static/js/memory.js:1255` → `/api/memory/add`
  - `static/js/memory.js:1333` → `/api/memory/extract`
  - `static/js/memory.js:1384` → `/api/memory/add`
  - `static/js/memory.js:1452` → `/api/memory/import`
  - `static/js/memory.js:1512` → `/api/memory/add`
  - `static/js/memory.js:1554` → `/api/memory/add`
  - `static/js/presets.js:1041` → `/api/memory/add`
  - `static/js/slashCommands.js:1590` → `/api/memory/add`
  - `static/js/slashCommands.js:1643` → `/api/memory/search`

## `POST /api/memory/{memory_id}/pin`
- handler: `pin_memory` — `routes/memory/memory_routes.py:510`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/model-endpoints`
- handler: `list_model_endpoints` — `routes/model_routes.py:2083`
- **JS callers:**
  - `static/js/admin.js:312` → `/api/model-endpoints`
  - `static/js/admin.js:1024` → `/api/model-endpoints`
  - `static/js/admin.js:2017` → `/api/model-endpoints`
  - `static/js/admin.js:2311` → `/api/model-endpoints`
  - `static/js/admin.js:2499` → `/api/model-endpoints`
  - `static/js/admin.js:2592` → `/api/model-endpoints`
  - `static/js/assistant.js:134` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:536` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:2713` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:2732` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3020` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3686` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3719` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3908` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:4171` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:4374` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:4400` → `/api/model-endpoints`
  - `static/js/markdown.js:1860` → `/api/model-endpoints`
  - `static/js/markdown.js:1887` → `/api/model-endpoints`
  - `static/js/research/panel.js:809` → `/api/model-endpoints`
  - … +7 more

## `POST /api/model-endpoints`
- handler: `create_model_endpoint` — `routes/model_routes.py:2145`
- **JS callers:**
  - `static/js/admin.js:312` → `/api/model-endpoints`
  - `static/js/admin.js:1024` → `/api/model-endpoints`
  - `static/js/admin.js:2017` → `/api/model-endpoints`
  - `static/js/admin.js:2311` → `/api/model-endpoints`
  - `static/js/admin.js:2499` → `/api/model-endpoints`
  - `static/js/admin.js:2592` → `/api/model-endpoints`
  - `static/js/assistant.js:134` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:536` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:2713` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:2732` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3020` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3686` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3719` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3908` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:4171` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:4374` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:4400` → `/api/model-endpoints`
  - `static/js/markdown.js:1860` → `/api/model-endpoints`
  - `static/js/markdown.js:1887` → `/api/model-endpoints`
  - `static/js/research/panel.js:809` → `/api/model-endpoints`
  - … +7 more

## `GET /api/model-endpoints/probe-local`
- handler: `probe_local_endpoints` — `routes/model_routes.py:1825`
- **JS callers:**
  - `static/js/admin.js:2341` → `/api/model-endpoints/probe-local`
  - `static/js/chat.js:2049` → `/api/model-endpoints/probe-local`
  - `static/js/cookbookRunning.js:3909` → `/api/model-endpoints/probe-local`
  - `static/js/modelPicker.js:270` → `/api/model-endpoints/probe-local`

## `POST /api/model-endpoints/test`
- handler: `test_model_endpoint` — `routes/model_routes.py:2412`
- **JS callers:**
  - `static/js/admin.js:1956` → `/api/model-endpoints/test`
  - `static/js/admin.js:2467` → `/api/model-endpoints/test`

## `DELETE /api/model-endpoints/{ep_id}`
- handler: `delete_model_endpoint` — `routes/model_routes.py:3049`
- **JS callers:**
  - `static/js/admin.js:600` → `/api/model-endpoints/${encodeURIComponent(id)}`
  - `static/js/admin.js:1203` → `/api/model-endpoints/${btn.dataset.admToggleEp}`
  - `static/js/admin.js:1247` → `/api/model-endpoints/${encodeURIComponent(epId)}`
  - `static/js/admin.js:1956` → `/api/model-endpoints/test`
  - `static/js/admin.js:2341` → `/api/model-endpoints/probe-local`
  - `static/js/admin.js:2467` → `/api/model-endpoints/test`
  - `static/js/chat.js:2049` → `/api/model-endpoints/probe-local`
  - `static/js/cookbookRunning.js:3909` → `/api/model-endpoints/probe-local`
  - `static/js/modelPicker.js:270` → `/api/model-endpoints/probe-local`

## `PATCH /api/model-endpoints/{ep_id}`
- handler: `toggle_model_endpoint` — `routes/model_routes.py:2864`
- **JS callers:**
  - `static/js/admin.js:600` → `/api/model-endpoints/${encodeURIComponent(id)}`
  - `static/js/admin.js:1203` → `/api/model-endpoints/${btn.dataset.admToggleEp}`
  - `static/js/admin.js:1247` → `/api/model-endpoints/${encodeURIComponent(epId)}`
  - `static/js/admin.js:1956` → `/api/model-endpoints/test`
  - `static/js/admin.js:2341` → `/api/model-endpoints/probe-local`
  - `static/js/admin.js:2467` → `/api/model-endpoints/test`
  - `static/js/chat.js:2049` → `/api/model-endpoints/probe-local`
  - `static/js/cookbookRunning.js:3909` → `/api/model-endpoints/probe-local`
  - `static/js/modelPicker.js:270` → `/api/model-endpoints/probe-local`

## `GET /api/model-endpoints/{ep_id}/catalog-search`
- handler: `search_endpoint_catalog` — `routes/model_routes.py:2637`
- **JS callers:**
  - `static/js/admin.js:903` → `/api/model-endpoints/${epId}/catalog-search?q=${encodeURIComponent(q)}&page=1&per_page=50`
  - `static/js/admin.js:935` → `/api/model-endpoints/${epId}/catalog-search?q=${encodeURIComponent(currentQuery)}&page=${currentPage}&per_page=50`

## `GET /api/model-endpoints/{ep_id}/dependents`
- handler: `get_endpoint_dependents` — `routes/model_routes.py:3043`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/model-endpoints/{ep_id}/models`
- handler: `list_endpoint_models` — `routes/model_routes.py:2508`
- **JS callers:**
  - `static/js/admin.js:733` → `/api/model-endpoints/${epId}/models`
  - `static/js/admin.js:1391` → `/api/model-endpoints/${epId}/models?refresh=true&refresh_timeout=60`
  - `static/js/admin.js:1480` → `/api/model-endpoints/${epId}/models`
  - `static/js/admin.js:1518` → `/api/model-endpoints/${epId}/models`

## `PATCH /api/model-endpoints/{ep_id}/models`
- handler: `update_hidden_models` — `routes/model_routes.py:2565`
- **JS callers:**
  - `static/js/admin.js:733` → `/api/model-endpoints/${epId}/models`
  - `static/js/admin.js:1391` → `/api/model-endpoints/${epId}/models?refresh=true&refresh_timeout=60`
  - `static/js/admin.js:1480` → `/api/model-endpoints/${epId}/models`
  - `static/js/admin.js:1518` → `/api/model-endpoints/${epId}/models`

## `GET /api/model-endpoints/{ep_id}/probe`
- handler: `probe_endpoint_models` — `routes/model_routes.py:2458`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/model/cached`
- handler: `model_cached` — `routes/cookbook_routes.py:1281`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:807` → `/api/model/cached?`
  - `static/js/cookbookServe.js:4355` → `/api/model/cached`

## `POST /api/model/download`
- handler: `model_download` — `routes/cookbook_routes.py:939`
- **JS callers:**
  - `static/js/cookbookDownload.js:638` → `/api/model/download`
  - `static/js/cookbookRunning.js:703` → `/api/model/download`
  - `static/js/cookbookRunning.js:1541` → `/api/model/download`
  - `static/js/cookbookRunning.js:3463` → `/api/model/download`

## `POST /api/model/serve`
- handler: `model_serve` — `routes/cookbook_routes.py:1871`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:2027` → `/api/model/serve`
  - `static/js/cookbook.js:1486` → `/api/model/serve`
  - `static/js/cookbook.js:1562` → `/api/model/serve`
  - `static/js/cookbook.js:1775` → `/api/model/serve`
  - `static/js/cookbookRunning.js:2051` → `/api/model/serve`

## `GET /api/models`
- handler: `api_models` — `routes/model_routes.py:1758`
- **JS callers:**
  - `static/app.js:3608` → `/api/models`
  - `static/js/chat.js:2041` → `/api/models`
  - `static/js/compare/models.js:57` → `/api/models`
  - `static/js/group.js:45` → `/api/models`
  - `static/js/group.js:458` → `/api/models`
  - `static/js/models.js:202` → `/api/models`
  - `static/js/settings.js:448` → `/api/models`
  - `static/js/settings.js:703` → `/api/models`
  - `static/js/skills.js:1739` → `/api/models`
  - `static/js/slashCommands.js:267` → `/api/models`
  - `static/js/slashCommands.js:987` → `/api/models`
  - `static/js/slashCommands.js:1527` → `/api/models`
  - `static/js/tasks.js:1685` → `/api/models`

## `POST /api/notes/fire-reminder`
- handler: `fire_reminder` — `routes/note/note_routes.py:853`
- **JS callers:**
  - `static/js/calendar/reminders.js:77` → `/api/notes/fire-reminder`
  - `static/js/features/notes/infrastructure/http.js:24` → `/api/notes/fire-reminder`
  - `static/js/settings.js:2370` → `/api/notes/fire-reminder`

## `POST /api/notes/reorder`
- handler: `reorder_notes` — `routes/note/note_routes.py:911`
- **JS callers:**
  - `static/js/features/notes/infrastructure/http.js:21` → `/api/notes/reorder`

## `DELETE /api/notes/{note_id}`
- handler: `delete_note` — `routes/note/note_routes.py:770`
- **JS callers:**
  - `static/js/calendar/reminders.js:77` → `/api/notes/fire-reminder`
  - `static/js/features/notes/infrastructure/http.js:21` → `/api/notes/reorder`
  - `static/js/features/notes/infrastructure/http.js:24` → `/api/notes/fire-reminder`
  - `static/js/settings.js:2370` → `/api/notes/fire-reminder`

## `GET /api/notes/{note_id}`
- handler: `get_note` — `routes/note/note_routes.py:693`
- **JS callers:**
  - `static/js/calendar/reminders.js:77` → `/api/notes/fire-reminder`
  - `static/js/features/notes/infrastructure/http.js:21` → `/api/notes/reorder`
  - `static/js/features/notes/infrastructure/http.js:24` → `/api/notes/fire-reminder`
  - `static/js/settings.js:2370` → `/api/notes/fire-reminder`

## `PUT /api/notes/{note_id}`
- handler: `update_note` — `routes/note/note_routes.py:710`
- **JS callers:**
  - `static/js/calendar/reminders.js:77` → `/api/notes/fire-reminder`
  - `static/js/features/notes/infrastructure/http.js:21` → `/api/notes/reorder`
  - `static/js/features/notes/infrastructure/http.js:24` → `/api/notes/fire-reminder`
  - `static/js/settings.js:2370` → `/api/notes/fire-reminder`

## `POST /api/notes/{note_id}/archive`
- handler: `toggle_archive` — `routes/note/note_routes.py:808`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/notes/{note_id}/items/{index}/toggle`
- handler: `toggle_item` — `routes/note/note_routes.py:827`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/notes/{note_id}/pin`
- handler: `toggle_pin` — `routes/note/note_routes.py:789`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/personal/add_directory`
- handler: `add_directory_to_rag` — `routes/personal_routes.py:187`
- **JS callers:**
  - `static/js/admin.js:3365` → `/api/personal/add_directory`
  - `static/js/slashCommands.js:1914` → `/api/personal/add_directory`

## `DELETE /api/personal/file`
- handler: `delete_file_from_rag` — `routes/personal_routes.py:397`
- **JS callers:**
  - `static/js/admin.js:3317` → `/api/personal/file?filepath=`
  - `static/js/rag.js:93` → `/api/personal/file?filepath=`

## `POST /api/personal/reload`
- handler: `api_personal_reload` — `routes/personal_routes.py:178`
- **JS callers:**
  - `static/js/admin.js:3376` → `/api/personal/reload`

## `DELETE /api/personal/remove_directory`
- handler: `remove_directory_from_rag` — `routes/personal_routes.py:256`
- **JS callers:**
  - `static/js/admin.js:3297` → `/api/personal/remove_directory?directory=`
  - `static/js/slashCommands.js:1944` → `/api/personal/remove_directory?directory=`
  - `static/js/slashCommands.js:1953` → `/api/personal/remove_directory?directory=`

## `POST /api/personal/upload`
- handler: `upload_files_to_rag` — `routes/personal_routes.py:308`
- **JS callers:**
  - `static/js/admin.js:3344` → `/api/personal/upload`
  - `static/js/rag.js:120` → `/api/personal/upload`

## `GET /api/ping`
- handler: `ping_endpoints` — `routes/model_routes.py:1905`
- **JS callers:**
  - `static/js/slashCommands.js:5581` → `/api/ping`

## `GET /api/prefs/{key}`
- handler: `get_pref` — `routes/prefs_routes.py:112`
- **JS callers:**
  - `static/js/settings/imagePreferences.js:46` → `/api/prefs/${encodeURIComponent(key)}`
  - `static/js/settings/imagePreferences.js:64` → `/api/prefs/${encodeURIComponent(key)}`
  - `static/js/theme.js:159` → `/api/prefs/custom-themes`
  - `static/js/theme.js:692` → `/api/prefs/theme`
  - `static/js/theme.js:703` → `/api/prefs/theme`
  - `static/js/theme.js:2458` → `/api/prefs/custom-themes`

## `PUT /api/prefs/{key}`
- handler: `set_pref` — `routes/prefs_routes.py:118`
- **JS callers:**
  - `static/js/settings/imagePreferences.js:46` → `/api/prefs/${encodeURIComponent(key)}`
  - `static/js/settings/imagePreferences.js:64` → `/api/prefs/${encodeURIComponent(key)}`
  - `static/js/theme.js:159` → `/api/prefs/custom-themes`
  - `static/js/theme.js:692` → `/api/prefs/theme`
  - `static/js/theme.js:703` → `/api/prefs/theme`
  - `static/js/theme.js:2458` → `/api/prefs/custom-themes`

## `GET /api/presets`
- handler: `get_presets` — `routes/preset_routes.py:32`
- **JS callers:**
  - `static/js/assistant.js:281` → `/api/presets`
  - `static/js/presets.js:522` → `/api/presets`

## `POST /api/presets/custom`
- handler: `update_custom_preset` — `routes/preset_routes.py:36`
- **JS callers:**
  - `static/js/presets.js:710` → `/api/presets/custom`
  - `static/js/presets.js:840` → `/api/presets/custom`
  - `static/js/presets.js:1116` → `/api/presets/custom`

## `POST /api/presets/expand`
- handler: `expand_character_prompt` — `routes/preset_routes.py:80`
- **JS callers:**
  - `static/js/presets.js:136` → `/api/presets/expand`

## `GET /api/presets/groups`
- handler: `get_group_presets` — `routes/preset_routes.py:121`
- **JS callers:**
  - `static/js/group.js:183` → `/api/presets/groups`
  - `static/js/group.js:190` → `/api/presets/groups`
  - `static/js/group.js:267` → `/api/presets/groups`
  - `static/js/group.js:293` → `/api/presets/groups`
  - `static/js/group.js:321` → `/api/presets/groups`

## `POST /api/presets/groups`
- handler: `save_group_presets` — `routes/preset_routes.py:126`
- **JS callers:**
  - `static/js/group.js:183` → `/api/presets/groups`
  - `static/js/group.js:190` → `/api/presets/groups`
  - `static/js/group.js:267` → `/api/presets/groups`
  - `static/js/group.js:293` → `/api/presets/groups`
  - `static/js/group.js:321` → `/api/presets/groups`

## `GET /api/presets/templates`
- handler: `get_user_templates` — `routes/preset_routes.py:59`
- **JS callers:**
  - `static/js/assistant.js:282` → `/api/presets/templates`
  - `static/js/group.js:351` → `/api/presets/templates`
  - `static/js/presets.js:390` → `/api/presets/templates`
  - `static/js/presets.js:493` → `/api/presets/templates`
  - `static/js/presets.js:894` → `/api/presets/templates`

## `POST /api/presets/templates`
- handler: `save_user_template` — `routes/preset_routes.py:63`
- **JS callers:**
  - `static/js/assistant.js:282` → `/api/presets/templates`
  - `static/js/group.js:351` → `/api/presets/templates`
  - `static/js/presets.js:390` → `/api/presets/templates`
  - `static/js/presets.js:493` → `/api/presets/templates`
  - `static/js/presets.js:894` → `/api/presets/templates`

## `DELETE /api/presets/templates/{template_id}`
- handler: `delete_user_template` — `routes/preset_routes.py:73`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/probe`
- handler: `probe_models` — `routes/model_routes.py:1990`
- **JS callers:**
  - `static/js/slashCommands.js:5613` → `/api/probe`

## `POST /api/probe-selected`
- handler: `probe_selected` — `routes/model_routes.py:1945`
- **JS callers:**
  - `static/js/compare/probe.js:45` → `/api/probe-selected`
  - `static/js/compare/selector.js:1092` → `/api/probe-selected`

## `GET /api/providers`
- handler: `providers` — `routes/model_routes.py:2063`
- **JS callers:**
  - `static/js/models.js:615` → `/api/providers`

## `GET /api/rag/stats`
- handler: `get_rag_stats` — `routes/diagnostics_routes.py:67`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/ready`
- handler: `readiness_check` — `app.py:1087`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/research/active`
- handler: `research_active` — `routes/research/research_routes.py:262`
- **JS callers:**
  - `static/js/research/jobs.js:105` → `/api/research/active`

## `POST /api/research/cancel/{session_id}`
- handler: `research_cancel` — `routes/research/research_routes.py:322`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/research/chat-jobs/{chat_id}`
- handler: `chat_research_jobs` — `routes/research/research_routes.py:654`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/research/detail/{session_id}`
- handler: `research_detail` — `routes/research/research_routes.py:474`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/research/library`
- handler: `research_library` — `routes/research/research_routes.py:417`
- **JS callers:**
  - `static/js/documentLibrary.js:2592` → `/api/research/library?archived=true`
  - `static/js/documentLibrary.js:2963` → `/api/research/library`
  - `static/js/research/jobs.js:144` → `/api/research/library?sort=recent&limit=20`
  - `static/js/research/panel.js:181` → `/api/research/library?limit=1`
  - `static/js/sessions.js:3993` → `/api/research/library?`

## `GET /api/research/report/{session_id}`
- handler: `research_report` — `routes/research/research_routes.py:374`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/research/result-peek/{session_id}`
- handler: `research_result_peek` — `routes/research/research_routes.py:715`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/research/result/{session_id}`
- handler: `research_result` — `routes/research/research_routes.py:331`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/research/spinoff/{session_id}`
- handler: `research_spinoff` — `routes/research/research_routes.py:758`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/research/start`
- handler: `research_start` — `routes/research/research_routes.py:546`
- **JS callers:**
  - `static/js/research/jobs.js:331` → `/api/research/start`

## `GET /api/research/status/{session_id}`
- handler: `research_status` — `routes/research/research_routes.py:287`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/research/stream/{session_id}`
- handler: `research_stream` — `routes/research/research_routes.py:660`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/research/{session_id}`
- handler: `research_delete` — `routes/research/research_routes.py:508`
- **JS callers:**
  - `static/js/documentLibrary.js:2592` → `/api/research/library?archived=true`
  - `static/js/documentLibrary.js:2963` → `/api/research/library`
  - `static/js/research/jobs.js:105` → `/api/research/active`
  - `static/js/research/jobs.js:144` → `/api/research/library?sort=recent&limit=20`
  - `static/js/research/jobs.js:331` → `/api/research/start`
  - `static/js/research/panel.js:181` → `/api/research/library?limit=1`
  - `static/js/sessions.js:3993` → `/api/research/library?`

## `POST /api/research/{session_id}/archive`
- handler: `research_archive` — `routes/research/research_routes.py:490`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/research/{session_id}/hide-image`
- handler: `research_hide_image` — `routes/research/research_routes.py:394`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/research/{session_id}/unhide-images`
- handler: `research_unhide_images` — `routes/research/research_routes.py:406`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/rewrite`
- handler: `rewrite_message` — `routes/chat_routes.py:5706`
- **JS callers:**
  - `static/js/chat.js:9238` → `/api/rewrite`

## `GET /api/runtime`
- handler: `runtime_info` — `app.py:1098`
- **JS callers:**
  - `static/js/admin.js:1892` → `/api/runtime`

## `GET /api/search`
- handler: `search_messages` — `routes/chat_routes.py:5636`
- **JS callers:**
  - `static/js/compare/index.js:1061` → `/api/search`
  - `static/js/search-chat.js:194` → `/api/search?q=`
  - `static/js/slashCommands.js:1980` → `/api/search?q=`

## `POST /api/search`
- handler: `do_web_search` — `routes/search/search_routes.py:148`
- **JS callers:**
  - `static/js/compare/index.js:1061` → `/api/search`
  - `static/js/compare/index.js:1061` → `/api/search`
  - `static/js/search-chat.js:194` → `/api/search?q=`
  - `static/js/search-chat.js:194` → `/api/search?q=`
  - `static/js/slashCommands.js:1980` → `/api/search?q=`
  - `static/js/slashCommands.js:1980` → `/api/search?q=`

## `POST /api/search`
- handler: `_stub_search` — `tests/test_codeql_python_residual_closure.py:520`
- **JS callers:**
  - `static/js/compare/index.js:1061` → `/api/search`
  - `static/js/compare/index.js:1061` → `/api/search`
  - `static/js/search-chat.js:194` → `/api/search?q=`
  - `static/js/search-chat.js:194` → `/api/search?q=`
  - `static/js/slashCommands.js:1980` → `/api/search?q=`
  - `static/js/slashCommands.js:1980` → `/api/search?q=`

## `GET /api/search/config`
- handler: `get_search_settings` — `routes/search/search_routes.py:144`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/search/providers`
- handler: `list_search_providers` — `routes/search/search_routes.py:170`
- **JS callers:**
  - `static/js/compare/selector.js:636` → `/api/search/providers`
  - `static/js/compare/selector.js:747` → `/api/search/providers`

## `POST /api/search/query`
- handler: `search_with_provider` — `routes/search/search_routes.py:189`
- **JS callers:**
  - `static/js/compare/index.js:827` → `/api/search/query`
  - `static/js/compare/panes.js:468` → `/api/search/query`
  - `static/js/compare/selector.js:1305` → `/api/search/query`
  - `static/js/settings.js:1124` → `/api/search/query`

## `POST /api/session`
- handler: `create_session` — `routes/session_routes.py:553`
- **JS callers:**
  - `static/js/chat.js:9421` → `/api/session`
  - `static/js/compare/index.js:311` → `/api/session`
  - `static/js/compare/panes.js:740` → `/api/session`
  - `static/js/compare/panes.js:936` → `/api/session`
  - `static/js/compare/stream.js:290` → `/api/session`
  - `static/js/document.js:12340` → `/api/session`
  - `static/js/emailInbox.js:1451` → `/api/session`
  - `static/js/features/notes/infrastructure/http.js:26` → `/api/session`
  - `static/js/group.js:607` → `/api/session`
  - `static/js/group.js:630` → `/api/session`
  - `static/js/keyboard-shortcuts.js:237` → `/api/session`
  - `static/js/presets.js:432` → `/api/session`
  - `static/js/sessions.js:2763` → `/api/session`
  - `static/js/slashCommands.js:1010` → `/api/session`
  - `static/js/tasks.js:2705` → `/api/session`

## `POST /api/session/openai`
- handler: `create_session_openai` — `routes/session_routes.py:1267`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/compact`
- handler: `compact_session` — `routes/history/history_routes.py:1485`
- **JS callers:**
  - `static/js/chat.js:1154` → `/api/session/${encodeURIComponent(sid)}/compact`
  - `static/js/chat.js:1154` → `/api/session/${encodeURIComponent(sid)}/compact`

## `POST /api/session/{session_id}/compact`
- handler: `compact_session` — `routes/session_routes.py:1331`
- **JS callers:**
  - `static/js/chat.js:1154` → `/api/session/${encodeURIComponent(sid)}/compact`
  - `static/js/chat.js:1154` → `/api/session/${encodeURIComponent(sid)}/compact`

## `GET /api/session/{session_id}/context`
- handler: `get_session_context_usage` — `routes/history/history_routes.py:1192`
- **JS callers:**
  - `static/js/chat.js:1184` → `/api/session/${encodeURIComponent(sid)}/context`

## `GET /api/session/{session_id}/context_info`
- handler: `get_context_info` — `routes/session_routes.py:1699`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/delete-messages`
- handler: `delete_messages` — `routes/history/history_routes.py:681`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/edit-message`
- handler: `edit_message` — `routes/history/history_routes.py:769`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/fork`
- handler: `fork_session` — `routes/history/history_routes.py:1051`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/generation-settings`
- handler: `set_session_generation_settings` — `routes/history/history_routes.py:1366`
- **JS callers:**
  - `static/js/chat.js:1133` → `/api/session/${encodeURIComponent(sid)}/generation-settings`

## `POST /api/session/{session_id}/important`
- handler: `mark_session_important` — `routes/session_routes.py:1294`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/mark-stopped`
- handler: `mark_stopped` — `routes/history/history_routes.py:824`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/memory-extraction`
- handler: `set_session_memory_extraction` — `routes/history/history_routes.py:1254`
- **JS callers:**
  - `static/js/chat.js:1028` → `/api/session/${encodeURIComponent(sid)}/memory-extraction`

## `POST /api/session/{session_id}/memory-injection`
- handler: `set_session_memory_injection` — `routes/history/history_routes.py:1329`
- **JS callers:**
  - `static/js/chat.js:1102` → `/api/session/${encodeURIComponent(sid)}/memory-injection`

## `POST /api/session/{session_id}/merge-last-assistant`
- handler: `merge_last_assistant` — `routes/history/history_routes.py:930`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/message`
- handler: `add_message` — `routes/history/history_routes.py:657`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/skill-injection`
- handler: `set_session_skill_injection` — `routes/history/history_routes.py:1290`
- **JS callers:**
  - `static/js/chat.js:1066` → `/api/session/${encodeURIComponent(sid)}/skill-injection`

## `POST /api/session/{session_id}/truncate`
- handler: `truncate_session` — `routes/history/history_routes.py:566`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/uncompact`
- handler: `uncompact_session` — `routes/history/history_routes.py:1422`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/update-last-meta`
- handler: `update_last_meta` — `routes/history/history_routes.py:879`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/session/{sid}`
- handler: `delete_session` — `routes/session_routes.py:963`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PATCH /api/session/{sid}`
- handler: `rename_session` — `routes/session_routes.py:694`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{sid}/archive`
- handler: `archive_session` — `routes/session_routes.py:1056`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{sid}/delete`
- handler: `delete_session_beacon` — `routes/session_routes.py:916`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/session/{sid}/deletion-info`
- handler: `session_deletion_info` — `routes/session_routes.py:952`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/session/{sid}/export`
- handler: `export_session` — `routes/session_routes.py:1169`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{sid}/inject_messages`
- handler: `inject_messages` — `routes/session_routes.py:880`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{sid}/retitle`
- handler: `retitle_session` — `routes/session_routes.py:800`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{sid}/unarchive`
- handler: `unarchive_session` — `routes/session_routes.py:1094`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/sessions`
- handler: `list_sessions` — `routes/session_routes.py:420`
- **JS callers:**
  - `static/js/documentLibrary.js:2154` → `/api/sessions`
  - `static/js/sessions.js:2112` → `/api/sessions`
  - `static/js/slashCommands.js:2023` → `/api/sessions`

## `DELETE /api/sessions/all`
- handler: `delete_all_sessions` — `routes/session_routes.py:1000`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/sessions/archived`
- handler: `list_archived_sessions` — `routes/session_routes.py:1124`
- **JS callers:**
  - `static/js/documentLibrary.js:2590` → `/api/sessions/archived?limit=100&sort=recent`
  - `static/js/sessions.js:3571` → `/api/sessions/archived?`
  - `static/js/sessions.js:3924` → `/api/sessions/archived?`

## `POST /api/sessions/auto-sort`
- handler: `auto_sort_sessions` — `routes/session_routes.py:1441`
- **JS callers:**
  - `static/app.js:1477` → `/api/sessions/auto-sort`
  - `static/js/documentLibrary.js:2552` → `/api/sessions/auto-sort`
  - `static/js/slashCommands.js:1163` → `/api/sessions/auto-sort`

## `POST /api/sessions/bulk-delete`
- handler: `bulk_delete_sessions` — `routes/session_routes.py:921`
- **JS callers:**
  - `static/js/compare/index.js:64` → `/api/sessions/bulk-delete`

## `POST /api/sessions/save`
- handler: `sessions_save_now` — `routes/session_routes.py:1259`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/shell/exec`
- handler: `shell_exec` — `routes/shell_routes.py:1195`
- **JS callers:**
  - `static/js/codeRunner.js:335` → `/api/shell/exec`
  - `static/js/cookbook-diagnosis.js:1074` → `/api/shell/exec`
  - `static/js/cookbook-hwfit.js:1821` → `/api/shell/exec`
  - `static/js/cookbook-hwfit.js:1875` → `/api/shell/exec`
  - `static/js/cookbookDownload.js:289` → `/api/shell/exec`
  - `static/js/cookbookDownload.js:595` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1513` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1615` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1678` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1720` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1753` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1976` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1998` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:2579` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:2944` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:2953` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:2975` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:2984` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:2995` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:3114` → `/api/shell/exec`
  - … +10 more

## `POST /api/shell/stream`
- handler: `shell_stream` — `routes/shell_routes.py:1213`
- **JS callers:**
  - `static/js/cookbookDownload.js:393` → `/api/shell/stream`

## `GET /api/signatures`
- handler: `list_signatures` — `routes/signature_routes.py:87`
- **JS callers:**
  - `static/js/document.js:2193` → `/api/signatures`
  - `static/js/document.js:2482` → `/api/signatures`
  - `static/js/signature.js:329` → `/api/signatures`
  - `static/js/signature.js:336` → `/api/signatures`

## `POST /api/signatures`
- handler: `create_signature` — `routes/signature_routes.py:102`
- **JS callers:**
  - `static/js/document.js:2193` → `/api/signatures`
  - `static/js/document.js:2482` → `/api/signatures`
  - `static/js/signature.js:329` → `/api/signatures`
  - `static/js/signature.js:336` → `/api/signatures`

## `DELETE /api/signatures/{sig_id}`
- handler: `delete_signature` — `routes/signature_routes.py:131`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/skills/add`
- handler: `add_skill` — `routes/skills_routes.py:490`
- **JS callers:**
  - `static/js/skills.js:2274` → `/api/skills/add`

## `POST /api/skills/audit-all`
- handler: `audit_all_skills` — `routes/skills_routes.py:727`
- **JS callers:**
  - `static/js/skills.js:1811` → `/api/skills/audit-all`

## `POST /api/skills/audit-all/cancel`
- handler: `audit_cancel` — `routes/skills_routes.py:771`
- **JS callers:**
  - `static/js/skills.js:1964` → `/api/skills/audit-all/cancel`

## `GET /api/skills/audit-all/status`
- handler: `audit_status` — `routes/skills_routes.py:766`
- **JS callers:**
  - `static/js/skills.js:1918` → `/api/skills/audit-all/status`

## `GET /api/skills/builtin`
- handler: `list_builtin_skills` — `routes/skills_routes.py:360`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/skills/builtin/{name}`
- handler: `reset_builtin_override` — `routes/skills_routes.py:447`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/skills/builtin/{name}`
- handler: `get_builtin_skill` — `routes/skills_routes.py:397`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PUT /api/skills/builtin/{name}`
- handler: `set_builtin_override` — `routes/skills_routes.py:421`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/skills/import-from-url`
- handler: `import_skill_from_url` — `routes/skills_routes.py:460`
- **JS callers:**
  - `static/js/skills.js:2233` → `/api/skills/import-from-url`

## `GET /api/skills/index`
- handler: `get_index` — `routes/skills_routes.py:322`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/skills/search`
- handler: `search_skills` — `routes/skills_routes.py:865`
- **JS callers:**
  - `static/js/slashCommands.js:1676` → `/api/skills/search`

## `GET /api/skills/slash-catalog`
- handler: `get_slash_catalog` — `routes/skills_routes.py:331`
- **JS callers:**
  - `static/js/slashAutocomplete.js:86` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:347` → `/api/skills/slash-catalog`

## `DELETE /api/skills/{skill_id}`
- handler: `delete_skill` — `routes/skills_routes.py:852`
- **JS callers:**
  - `static/js/skills.js:1811` → `/api/skills/audit-all`
  - `static/js/skills.js:2233` → `/api/skills/import-from-url`
  - `static/js/skills.js:2274` → `/api/skills/add`
  - `static/js/slashAutocomplete.js:86` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:347` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:1676` → `/api/skills/search`

## `GET /api/skills/{skill_id}`
- handler: `get_skill` — `routes/skills_routes.py:564`
- **JS callers:**
  - `static/js/skills.js:1811` → `/api/skills/audit-all`
  - `static/js/skills.js:2233` → `/api/skills/import-from-url`
  - `static/js/skills.js:2274` → `/api/skills/add`
  - `static/js/slashAutocomplete.js:86` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:347` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:1676` → `/api/skills/search`

## `PUT /api/skills/{skill_id}`
- handler: `update_skill` — `routes/skills_routes.py:829`
- **JS callers:**
  - `static/js/skills.js:1811` → `/api/skills/audit-all`
  - `static/js/skills.js:2233` → `/api/skills/import-from-url`
  - `static/js/skills.js:2274` → `/api/skills/add`
  - `static/js/slashAutocomplete.js:86` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:347` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:1676` → `/api/skills/search`

## `POST /api/skills/{skill_id}/invoke`
- handler: `invoke_skill` — `routes/skills_routes.py:523`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/skills/{skill_id}/markdown`
- handler: `get_skill_markdown` — `routes/skills_routes.py:573`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/skills/{skill_id}/markdown`
- handler: `save_skill_markdown` — `routes/skills_routes.py:776`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/skills/{skill_id}/test`
- handler: `test_skill` — `routes/skills_routes.py:592`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/skills/{skill_id}/test-approval`
- handler: `approve_skill_test_action` — `routes/skills_routes.py:660`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/skills/{skill_id}/test-status`
- handler: `test_skill_status` — `routes/skills_routes.py:718`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/stt/stats`
- handler: `get_stt_stats` — `routes/stt_routes.py:17`
- **JS callers:**
  - `static/js/voiceRecorder.js:31` → `/api/stt/stats`

## `POST /api/stt/transcribe`
- handler: `transcribe_audio` — `routes/stt_routes.py:26`
- **JS callers:**
  - `static/js/voiceRecorder.js:115` → `/api/stt/transcribe`

## `GET /api/tasks/meta/actions`
- handler: `list_actions` — `routes/task/task_routes.py:1093`
- **JS callers:**
  - `static/js/tasks.js:216` → `/api/tasks/meta/actions`

## `GET /api/tasks/meta/events`
- handler: `list_events` — `routes/task/task_routes.py:1104`
- **JS callers:**
  - `static/js/tasks.js:344` → `/api/tasks/meta/events`

## `GET /api/tasks/meta/output-targets`
- handler: `list_output_targets` — `routes/task/task_routes.py:1055`
- **JS callers:**
  - `static/js/tasks.js:203` → `/api/tasks/meta/output-targets`

## `GET /api/tasks/notification-logs`
- handler: `get_notification_logs` — `routes/task/task_routes.py:587`
- **JS callers:**
  - `static/js/admin.js:4058` → `/api/tasks/notification-logs?limit=500`
  - `static/js/ui.js:377` → `/api/tasks/notification-logs`
  - `static/js/ui.js:516` → `/api/tasks/notification-logs`

## `POST /api/tasks/notification-logs`
- handler: `create_notification_log` — `routes/task/task_routes.py:615`
- **JS callers:**
  - `static/js/admin.js:4058` → `/api/tasks/notification-logs?limit=500`
  - `static/js/ui.js:377` → `/api/tasks/notification-logs`
  - `static/js/ui.js:516` → `/api/tasks/notification-logs`

## `GET /api/tasks/notifications`
- handler: `get_notifications` — `routes/task/task_routes.py:576`
- **JS callers:**
  - `static/js/tasks.js:3366` → `/api/tasks/notifications`

## `GET /api/tasks/onboarding`
- handler: `get_tasks_onboarding` — `routes/task/task_routes.py:383`
- **JS callers:**
  - `static/js/tasks.js:64` → `/api/tasks/onboarding`
  - `static/js/tasks.js:69` → `/api/tasks/onboarding`

## `POST /api/tasks/onboarding`
- handler: `update_tasks_onboarding` — `routes/task/task_routes.py:392`
- **JS callers:**
  - `static/js/tasks.js:64` → `/api/tasks/onboarding`
  - `static/js/tasks.js:69` → `/api/tasks/onboarding`

## `POST /api/tasks/parse`
- handler: `parse_task` — `routes/task/task_routes.py:1162`
- **JS callers:**
  - `static/js/tasks.js:2988` → `/api/tasks/parse`

## `GET /api/tasks/runs/recent`
- handler: `list_recent_runs` — `routes/task/task_routes.py:965`
- **JS callers:**
  - `static/js/tasks.js:2172` → `/api/tasks/runs/recent?limit=`
  - `static/js/tasks.js:2338` → `/api/tasks/runs/recent?limit=`

## `DELETE /api/tasks/{task_id}`
- handler: `delete_task` — `routes/task/task_routes.py:829`
- **JS callers:**
  - `static/js/admin.js:4058` → `/api/tasks/notification-logs?limit=500`
  - `static/js/tasks.js:64` → `/api/tasks/onboarding`
  - `static/js/tasks.js:69` → `/api/tasks/onboarding`
  - `static/js/tasks.js:2988` → `/api/tasks/parse`
  - `static/js/tasks.js:3366` → `/api/tasks/notifications`
  - `static/js/ui.js:377` → `/api/tasks/notification-logs`
  - `static/js/ui.js:516` → `/api/tasks/notification-logs`

## `GET /api/tasks/{task_id}`
- handler: `get_task` — `routes/task/task_routes.py:718`
- **JS callers:**
  - `static/js/admin.js:4058` → `/api/tasks/notification-logs?limit=500`
  - `static/js/tasks.js:64` → `/api/tasks/onboarding`
  - `static/js/tasks.js:69` → `/api/tasks/onboarding`
  - `static/js/tasks.js:2988` → `/api/tasks/parse`
  - `static/js/tasks.js:3366` → `/api/tasks/notifications`
  - `static/js/ui.js:377` → `/api/tasks/notification-logs`
  - `static/js/ui.js:516` → `/api/tasks/notification-logs`

## `PUT /api/tasks/{task_id}`
- handler: `update_task` — `routes/task/task_routes.py:732`
- **JS callers:**
  - `static/js/admin.js:4058` → `/api/tasks/notification-logs?limit=500`
  - `static/js/tasks.js:64` → `/api/tasks/onboarding`
  - `static/js/tasks.js:69` → `/api/tasks/onboarding`
  - `static/js/tasks.js:2988` → `/api/tasks/parse`
  - `static/js/tasks.js:3366` → `/api/tasks/notifications`
  - `static/js/ui.js:377` → `/api/tasks/notification-logs`
  - `static/js/ui.js:516` → `/api/tasks/notification-logs`

## `POST /api/tasks/{task_id}/clear-cache`
- handler: `clear_task_cache` — `routes/task/task_routes.py:638`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/pause`
- handler: `pause_task` — `routes/task/task_routes.py:851`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/resume`
- handler: `resume_task` — `routes/task/task_routes.py:867`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/revert`
- handler: `revert_task` — `routes/task/task_routes.py:890`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/run`
- handler: `run_task_now` — `routes/task/task_routes.py:930`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/tasks/{task_id}/runs`
- handler: `list_runs` — `routes/task/task_routes.py:1037`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/stop`
- handler: `stop_task_now` — `routes/task/task_routes.py:948`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/webhook-regenerate`
- handler: `regenerate_webhook` — `routes/task/task_routes.py:1145`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/webhook/{token}`
- handler: `webhook_trigger` — `routes/task/task_routes.py:1118`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/test-research`
- handler: `test_research` — `routes/diagnostics_routes.py:95`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/test/youtube`
- handler: `test_youtube` — `routes/diagnostics_routes.py:74`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/tokens`
- handler: `list_tokens` — `routes/api_token_routes.py:80`
- **JS callers:**
  - `static/js/admin.js:3428` → `/api/tokens`
  - `static/js/admin.js:3527` → `/api/tokens`
  - `static/js/settings.js:3234` → `/api/tokens`
  - `static/js/settings.js:4848` → `/api/tokens`
  - `static/js/settings.js:5134` → `/api/tokens`

## `POST /api/tokens`
- handler: `create_token` — `routes/api_token_routes.py:116`
- **JS callers:**
  - `static/js/admin.js:3428` → `/api/tokens`
  - `static/js/admin.js:3527` → `/api/tokens`
  - `static/js/settings.js:3234` → `/api/tokens`
  - `static/js/settings.js:4848` → `/api/tokens`
  - `static/js/settings.js:5134` → `/api/tokens`

## `GET /api/tokens/profiles`
- handler: `token_profiles` — `routes/api_token_routes.py:108`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/tokens/{token_id}`
- handler: `delete_token` — `routes/api_token_routes.py:196`
- **JS callers:**
  - `static/js/admin.js:3453` → `/api/tokens/${btn.dataset.admDelToken}`
  - `static/js/admin.js:3476` → `/api/tokens/${input.dataset.tokenId}`
  - `static/js/admin.js:3496` → `/api/tokens/${tokenId}`
  - `static/js/settings.js:3368` → `/api/tokens/${id}`
  - `static/js/settings.js:4998` → `/api/tokens/${renameInput.dataset.tokenId}`
  - `static/js/settings.js:5017` → `/api/tokens/${cb.dataset.tokenId}`
  - `static/js/settings.js:5058` → `/api/tokens/${tokenId}`
  - `static/js/settings.js:5084` → `/api/tokens/${tokenId}`
  - `static/js/settings.js:5260` → `/api/tokens/${tokenId}`

## `PATCH /api/tokens/{token_id}`
- handler: `update_token` — `routes/api_token_routes.py:156`
- **JS callers:**
  - `static/js/admin.js:3453` → `/api/tokens/${btn.dataset.admDelToken}`
  - `static/js/admin.js:3476` → `/api/tokens/${input.dataset.tokenId}`
  - `static/js/admin.js:3496` → `/api/tokens/${tokenId}`
  - `static/js/settings.js:3368` → `/api/tokens/${id}`
  - `static/js/settings.js:4998` → `/api/tokens/${renameInput.dataset.tokenId}`
  - `static/js/settings.js:5017` → `/api/tokens/${cb.dataset.tokenId}`
  - `static/js/settings.js:5058` → `/api/tokens/${tokenId}`
  - `static/js/settings.js:5084` → `/api/tokens/${tokenId}`
  - `static/js/settings.js:5260` → `/api/tokens/${tokenId}`

## `GET /api/tools`
- handler: `list_tools` — `routes/model_routes.py:3105`
- **JS callers:**
  - `static/js/admin.js:2873` → `/api/tools`
  - `static/js/appConfig.js:33` → `/api/tools`

## `POST /api/tools`
- handler: `update_tools` — `routes/model_routes.py:3119`
- **JS callers:**
  - `static/js/admin.js:2873` → `/api/tools`
  - `static/js/appConfig.js:33` → `/api/tools`

## `POST /api/tts/clear-cache`
- handler: `clear_tts_cache` — `routes/tts_routes.py:78`
- **JS callers:**
  - `static/js/settings/speech.js:82` → `/api/tts/clear-cache`

## `GET /api/tts/stats`
- handler: `get_tts_stats` — `routes/tts_routes.py:22`
- **JS callers:**
  - `static/js/tts-ai.js:47` → `/api/tts/stats`

## `POST /api/tts/synthesize`
- handler: `synthesize_speech` — `routes/tts_routes.py:31`
- **JS callers:**
  - `static/js/settings/speech.js:140` → `/api/tts/synthesize`
  - `static/js/slashCommands.js:2099` → `/api/tts/synthesize`
  - `static/js/tts-ai.js:135` → `/api/tts/synthesize`

## `POST /api/upload/cleanup`
- handler: `manual_cleanup` — `routes/upload_routes.py:424`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/upload/stats`
- handler: `upload_stats` — `routes/upload_routes.py:447`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `API_ROUTE /api/upload/{file_id}`
- handler: `download_file` — `routes/upload_routes.py:457`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/upload/{file_id}/vision`
- handler: `get_vision_text` — `routes/upload_routes.py:576`
- **JS callers:**
  - `static/js/chatRenderer.js:726` → `/api/upload/${att.id}/vision`
  - `static/js/chatRenderer.js:790` → `/api/upload/${att.id}/vision`

## `PUT /api/upload/{file_id}/vision`
- handler: `put_vision_text` — `routes/upload_routes.py:615`
- **JS callers:**
  - `static/js/chatRenderer.js:726` → `/api/upload/${att.id}/vision`
  - `static/js/chatRenderer.js:790` → `/api/upload/${att.id}/vision`

## `POST /api/v1/chat`
- handler: `sync_chat` — `routes/webhook/webhook_routes.py:238`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/vault/config`
- handler: `get_config` — `routes/vault/vault_routes.py:144`
- **JS callers:**
  - `static/js/settings.js:3233` → `/api/vault/config`
  - `static/js/settings.js:4538` → `/api/vault/config`
  - `static/js/settings.js:4561` → `/api/vault/config`

## `POST /api/vault/config`
- handler: `save_config` — `routes/vault/vault_routes.py:157`
- **JS callers:**
  - `static/js/settings.js:3233` → `/api/vault/config`
  - `static/js/settings.js:4538` → `/api/vault/config`
  - `static/js/settings.js:4561` → `/api/vault/config`

## `POST /api/vault/lock`
- handler: `lock` — `routes/vault/vault_routes.py:221`
- **JS callers:**
  - `static/js/settings.js:4614` → `/api/vault/lock`

## `POST /api/vault/login`
- handler: `login` — `routes/vault/vault_routes.py:174`
- **JS callers:**
  - `static/js/settings.js:4578` → `/api/vault/login`

## `POST /api/vault/logout`
- handler: `logout` — `routes/vault/vault_routes.py:233`
- **JS callers:**
  - `static/js/settings.js:3369` → `/api/vault/logout`
  - `static/js/settings.js:4624` → `/api/vault/logout`

## `POST /api/vault/unlock`
- handler: `unlock` — `routes/vault/vault_routes.py:199`
- **JS callers:**
  - `static/js/settings.js:4597` → `/api/vault/unlock`

## `GET /api/version`
- handler: `get_version` — `app.py:1036`
- **JS callers:**
  - `static/js/sessions.js:107` → `/api/version`
  - `static/js/settings/sidebar.js:191` → `/api/version`

## `GET /api/webhooks`
- handler: `list_webhooks` — `routes/webhook/webhook_routes.py:72`
- **JS callers:**
  - `static/js/admin.js:3561` → `/api/webhooks`
  - `static/js/admin.js:3623` → `/api/webhooks`

## `POST /api/webhooks`
- handler: `create_webhook` — `routes/webhook/webhook_routes.py:96`
- **JS callers:**
  - `static/js/admin.js:3561` → `/api/webhooks`
  - `static/js/admin.js:3623` → `/api/webhooks`

## `DELETE /api/webhooks/{webhook_id}`
- handler: `delete_webhook` — `routes/webhook/webhook_routes.py:171`
- **JS callers:**
  - `static/js/admin.js:3598` → `/api/webhooks/${btn.dataset.admWhToggle}`
  - `static/js/admin.js:3603` → `/api/webhooks/${btn.dataset.admWhDelete}`
  - `static/js/settings.js:3533` → `/api/webhooks/...`

## `PATCH /api/webhooks/{webhook_id}`
- handler: `toggle_webhook` — `routes/webhook/webhook_routes.py:157`
- **JS callers:**
  - `static/js/admin.js:3598` → `/api/webhooks/${btn.dataset.admWhToggle}`
  - `static/js/admin.js:3603` → `/api/webhooks/${btn.dataset.admWhDelete}`
  - `static/js/settings.js:3533` → `/api/webhooks/...`

## `POST /api/webhooks/{webhook_id}/test`
- handler: `test_webhook` — `routes/webhook/webhook_routes.py:142`
- **JS callers:**
  - `static/js/admin.js:3591` → `/api/webhooks/${btn.dataset.admWhTest}/test`

## `GET /api/workspace/browse`
- handler: `browse` — `routes/workspace_routes.py:18`
- **JS callers:**
  - `static/js/workspace.js:110` → `/api/workspace/browse`

## `GET /api/workspace/default`
- handler: `default_workspace` — `routes/workspace_routes.py:86`
- **JS callers:**
  - `static/js/workspace.js:90` → `/api/workspace/default`

## `GET /api/workspace/vet`
- handler: `vet` — `routes/workspace_routes.py:69`
- **JS callers:**
  - `static/js/workspace.js:75` → `/api/workspace/vet?path=`

## `GET /backgrounds`
- handler: `serve_backgrounds` — `app.py:1025`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /calendar`
- handler: `serve_calendar` — `app.py:993`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /cookbook`
- handler: `serve_cookbook` — `app.py:1001`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /csp-control`
- handler: `_control` — `tests/test_codeql_python_residual_closure.py:524`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /device/cancel`
- handler: `device_cancel` — `routes/device_flow.py:188`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /device/poll`
- handler: `device_poll` — `routes/device_flow.py:160`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /device/start`
- handler: `device_start` — `routes/device_flow.py:148`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /email`
- handler: `serve_email` — `app.py:1005`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /gallery`
- handler: `serve_gallery` — `app.py:1013`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /health`
- handler: `health` — `scripts/diffusion_server.py:1462`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /library`
- handler: `serve_library` — `app.py:1021`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /login`
- handler: `serve_login` — `app.py:1030`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /loop-thread`
- handler: `loop_thread_probe` — `tests/test_add_directory_event_loop.py:101`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /memory`
- handler: `serve_memory` — `app.py:1009`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /notes`
- handler: `serve_notes` — `app.py:989`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /plain`
- handler: `plain` — `tests/test_security_headers_pdf_preview.py:13`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /probe`
- handler: `_delete_probe` — `tests/test_review_20260923_fixes.py:494`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /probe`
- handler: `_get_probe` — `tests/test_review_20260923_fixes.py:490`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /probe`
- handler: `_post_probe` — `tests/test_review_20260923_fixes.py:498`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /search/web`
- handler: `web_search_page` — `routes/search/search_routes.py:46`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /tasks`
- handler: `serve_tasks` — `app.py:1017`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /v1/images/edits`
- handler: `edit_image` — `scripts/diffusion_server.py:763`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /v1/images/edits`
- handler: `edit_image` — `scripts/mlx_image_server.py:392`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /v1/images/generations`
- handler: `generate_image` — `scripts/diffusion_server.py:691`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /v1/images/generations`
- handler: `generate` — `scripts/mlx_image_server.py:329`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /v1/images/harmonize`
- handler: `harmonize_image` — `scripts/diffusion_server.py:1308`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /v1/images/harmonize`
- handler: `harmonize_image` — `scripts/mlx_image_server.py:426`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /v1/images/inpaint`
- handler: `inpaint_image` — `scripts/diffusion_server.py:975`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /v1/images/progress/{request_id}`
- handler: `image_progress` — `scripts/diffusion_server.py:755`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /v1/models`
- handler: `list_models` — `scripts/diffusion_server.py:678`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /v1/models`
- handler: `list_models` — `scripts/mlx_image_server.py:324`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

# Unmatched JS fetch URLs (dynamic or non-API)
- `static/app.js:208` → `/api/auth/`
- `static/app.js:648` → `/api/session/`
- `static/app.js:1631` → `/api/ai/name`
- `static/app.js:1691` → `/api/session/`
- `static/app.js:3517` → `/api/session/`
- `static/js/admin.js:178` → `/api/auth/users/`
- `static/js/admin.js:201` → `/api/auth/users/`
- `static/js/admin.js:227` → `/api/auth/users/`
- `static/js/admin.js:275` → `/api/auth/users/`
- `static/js/admin.js:365` → `/api/auth/users/`
- `static/js/admin.js:600` → `/api/model-endpoints/`
- `static/js/admin.js:733` → `/api/model-endpoints/`
- `static/js/admin.js:903` → `/api/model-endpoints/`
- `static/js/admin.js:935` → `/api/model-endpoints/`
- `static/js/admin.js:1203` → `/api/model-endpoints/`
- `static/js/admin.js:1247` → `/api/model-endpoints/`
- `static/js/admin.js:1298` → `/api/model-endpoints/`
- `static/js/admin.js:1311` → `/api/model-endpoints/`
- `static/js/admin.js:1391` → `/api/model-endpoints/`
- `static/js/admin.js:1480` → `/api/model-endpoints/`
- `static/js/admin.js:1518` → `/api/model-endpoints/`
- `static/js/admin.js:1595` → `/api/chatgpt-subscription/accounts/`
- `static/js/admin.js:2352` → `/api/model-endpoints/`
- `static/js/admin.js:2415` → `/api/model-endpoints/`
- `static/js/admin.js:2955` → `/api/mcp/oauth/authorize/`
- `static/js/admin.js:2969` → `/api/mcp/servers/`
- `static/js/admin.js:2980` → `/api/mcp/servers/`
- `static/js/admin.js:2987` → `/api/mcp/servers/`
- `static/js/admin.js:3013` → `/api/mcp/servers/`
- `static/js/admin.js:3057` → `/api/mcp/servers/`
- `static/js/admin.js:3264` → `/api/mcp/oauth/authorize/`
- `static/js/admin.js:3285` → `/api/personal`
- `static/js/admin.js:3453` → `/api/tokens/`
- `static/js/admin.js:3476` → `/api/tokens/`
- `static/js/admin.js:3496` → `/api/tokens/`
- `static/js/admin.js:3591` → `/api/webhooks/`
- `static/js/admin.js:3598` → `/api/webhooks/`
- `static/js/admin.js:3603` → `/api/webhooks/`
- `static/js/admin.js:3795` → `/api/admin/wipe/`
- `static/js/admin.js:3815` → `/api/admin/wipe/`
- `static/js/appConfig.js:14` → `/api/...`
- `static/js/assistant.js:12` → `/api/assistant`
- `static/js/assistant.js:252` → `/api/model-endpoints/`
- `static/js/backgroundToolJobs.js:109` → `/api/research/chat-jobs/`
- `static/js/calendar.js:38` → `/api/upload`
- `static/js/calendar.js:42` → `/api/upload/`
- `static/js/calendar.js:295` → `/api/calendar/events/`
- `static/js/calendar.js:345` → `/api/calendar/events/`
- `static/js/calendar.js:517` → `/api/calendar/events/`
- `static/js/calendar.js:688` → `/api/notes`
- `static/js/calendar.js:3266` → `/api/calendar/calendars/`
- `static/js/calendar.js:3297` → `/api/calendar/calendars/`
- `static/js/calendar.js:3341` → `/api/calendar/export/`
- `static/js/calendar/reminders.js:5` → `/api/notes?label=calendar`
- `static/js/calendar/reminders.js:59` → `/api/notes?label=calendar`
- `static/js/chat.js:215` → `/api/upload/`
- `static/js/chat.js:229` → `/api/upload/`
- `static/js/chat.js:291` → `/api/gallery/`
- `static/js/chat.js:304` → `/api/upload/`
- `static/js/chat.js:1028` → `/api/session/`
- `static/js/chat.js:1066` → `/api/session/`
- `static/js/chat.js:1102` → `/api/session/`
- `static/js/chat.js:1133` → `/api/session/`
- `static/js/chat.js:1154` → `/api/session/`
- `static/js/chat.js:1184` → `/api/session/`
- `static/js/chat.js:1701` → `/api/chat/stream_status/`
- `static/js/chat.js:1744` → `/api/chat/stream_status/`
- `static/js/chat.js:1919` → `/api/chat/stop/`
- `static/js/chat.js:2529` → `/api/research/cancel/`
- `static/js/chat.js:2633` → `/api/session/`
- `static/js/chat.js:3657` → `/api/chat/finish/`
- `static/js/chat.js:3728` → `/api/history/`
- `static/js/chat.js:5331` → `/api/upload/`
- `static/js/chat.js:5333` → `/api/upload/`
- `static/js/chat.js:5355` → `/api/upload/`
- `static/js/chat.js:6393` → `/api/session/`
- `static/js/chat.js:6626` → `/api/session/`
- `static/js/chat.js:6665` → `/api/chat/stream_status/`
- `static/js/chat.js:7000` → `/api/chat/stream_status/`
- `static/js/chat.js:7063` → `/api/chat/stream_status/`
- `static/js/chat.js:7138` → `/api/session/`
- `static/js/chat.js:7252` → `/api/chat/resume/`
- `static/js/chat.js:7623` → `/api/history/`
- `static/js/chat.js:8203` → `/api/session/`
- `static/js/chat.js:8270` → `/api/session/`
- `static/js/chat.js:8367` → `/api/session/`
- `static/js/chat.js:8562` → `/api/session/`
- `static/js/chat.js:8639` → `/api/session/`
- `static/js/chat.js:8737` → `/api/session/`
- `static/js/chat.js:8770` → `/api/research/status/`
- `static/js/chat.js:8781` → `/api/research/result/`
- `static/js/chat.js:8929` → `/api/research/status/`
- `static/js/chat.js:8955` → `/api/research/result/`
- `static/js/chat.js:9091` → `/api/session/`
- `static/js/chat.js:9164` → `/api/session/`
- `static/js/chat.js:9331` → `/api/session/`
- `static/js/chat.js:9386` → `/api/upload/`
- `static/js/chatRenderer.js:548` → `/api/upload/`
- `static/js/chatRenderer.js:601` → `/api/upload/`
- `static/js/chatRenderer.js:647` → `/api/upload/`
- `static/js/chatRenderer.js:657` → `/api/upload/`
- `static/js/chatRenderer.js:726` → `/api/upload/`
- `static/js/chatRenderer.js:790` → `/api/upload/`
- `static/js/chatRenderer.js:869` → `/api/tools fetch failed; live exec-fence stripping disabled until reload`
- `static/js/chatRenderer.js:1168` → `/api/session/`
- `static/js/chatRenderer.js:1709` → `/api/research/report/`
- `static/js/chatRenderer.js:1725` → `/api/research/spinoff/`
- `static/js/chatRenderer.js:2195` → `/api/gallery/`
- `static/js/chatRenderer.js:2852` → `/api/session/`
- `static/js/compare/index.js:222` → `/api/session/`
- `static/js/compare/index.js:274` → `/api/session/`
- `static/js/compare/panes.js:85` → `/api/session/`
- `static/js/compare/panes.js:820` → `/api/session/`
- `static/js/compare/panes.js:956` → `/api/session/`
- `static/js/compare/stream.js:341` → `/api/session/`
- `static/js/cookbookRunning.js:543` → `/api/model-endpoints/`
- `static/js/cookbookRunning.js:1158` → `/api/generate`
- `static/js/cookbookRunning.js:2062` → `/api/model/serve failed`
- `static/js/cookbookRunning.js:3024` → `/api/model-endpoints/`
- `static/js/cookbookRunning.js:4168` → `/api/model-endpoints/`
- `static/js/cookbookSchedule.js:292` → `/api/tasks`
- `static/js/cookbookSchedule.js:368` → `/api/tasks/`
- `static/js/document.js:1534` → `/api/document/`
- `static/js/document.js:1574` → `/api/document/`
- `static/js/document.js:1618` → `/api/document/`
- `static/js/document.js:1814` → `/api/document/`
- `static/js/document.js:1972` → `/api/document/`
- `static/js/document.js:2110` → `/api/document/`
- `static/js/document.js:2155` → `/api/document/`
- `static/js/document.js:2832` → `/api/document/`
- `static/js/document.js:2867` → `/api/document/`
- `static/js/document.js:2987` → `/api/document/`
- `static/js/document.js:5012` → `/api/email/attachment-as-doc/`
- `static/js/document.js:5018` → `/api/email/attachment/`
- `static/js/document.js:5039` → `/api/email/attachment/`
- `static/js/document.js:5199` → `/api/email/compose-from-attachment/`
- `static/js/document.js:5716` → `/api/upload/`
- `static/js/document.js:5743` → `/api/upload/`
- `static/js/document.js:5937` → `/api/upload`
- `static/js/document.js:5987` → `/api/email/compose-upload/`
- `static/js/document.js:6478` → `/api/email/mark-answered/`
- `static/js/document.js:6484` → `/api/document/`
- `static/js/document.js:6594` → `/api/document/`
- `static/js/document.js:7045` → `/api/email/mark-unread/`
- `static/js/document.js:7087` → `/api/document/`
- `static/js/document.js:7144` → `/api/document/`
- `static/js/document.js:7150` → `/api/document/`
- `static/js/document.js:7245` → `/api/document/`
- `static/js/document.js:8728` → `/api/document/`
- `static/js/document.js:11367` → `/api/email/style${suffix}`
- `static/js/document.js:12277` → `/api/document/`
- `static/js/document.js:12375` → `/api/documents/`
- `static/js/document.js:14684` → `/api/document/`
- `static/js/document.js:14898` → `/api/document/`
- `static/js/document.js:15014` → `/api/document/`
- `static/js/document.js:15207` → `/api/document/`
- `static/js/document.js:15416` → `/api/document/`
- `static/js/document.js:15448` → `/api/document/`
- `static/js/document.js:15995` → `/api/document/`
- `static/js/document.js:16028` → `/api/document/`
- `static/js/document.js:16056` → `/api/document/`
- `static/js/document.js:16076` → `/api/document/`
- `static/js/document.js:16244` → `/api/document/`
- `static/js/document.js:16272` → `/api/document/`
- `static/js/document.js:17355` → `/api/document/`
- `static/js/document.js:17407` → `/api/document/`
- `static/js/document.js:17421` → `/api/document/`
- `static/js/document.js:17449` → `/api/document/`
- `static/js/document.js:17516` → `/api/document/`
- `static/js/documentLibrary.js:241` → `/api/history/`
- `static/js/documentLibrary.js:858` → `/api/document/`
- `static/js/documentLibrary.js:892` → `/api/document/`
- `static/js/documentLibrary.js:1014` → `/api/document/`
- `static/js/documentLibrary.js:1149` → `/api/document/`
- `static/js/documentLibrary.js:1163` → `/api/document/`
- `static/js/documentLibrary.js:1289` → `/api/document/`
- `static/js/documentLibrary.js:1418` → `/api/document/`
- `static/js/documentLibrary.js:1454` → `/api/document/`
- `static/js/documentLibrary.js:1488` → `/api/document/`
- `static/js/documentLibrary.js:1564` → `/api/document/`
- `static/js/documentLibrary.js:2198` → `/api/history/`
- `static/js/documentLibrary.js:2289` → `/api/session/`
- `static/js/documentLibrary.js:2298` → `/api/session/`
- `static/js/documentLibrary.js:2310` → `/api/session/`
- `static/js/documentLibrary.js:2383` → `/api/session/`
- `static/js/documentLibrary.js:2386` → `/api/session/`
- `static/js/documentLibrary.js:2467` → `/api/session/`
- `static/js/documentLibrary.js:2511` → `/api/session/`
- `static/js/documentLibrary.js:2637` → `/api/document/`
- `static/js/documentLibrary.js:2660` → `/api/document/`
- `static/js/documentLibrary.js:2665` → `/api/document/`
- `static/js/documentLibrary.js:2747` → `/api/session/`
- `static/js/documentLibrary.js:2750` → `/api/session/`
- `static/js/documentLibrary.js:2795` → `/api/document/`
- `static/js/documentLibrary.js:2796` → `/api/document/`
- `static/js/documentLibrary.js:2833` → `/api/research/report/`
- `static/js/documentLibrary.js:2834` → `/api/research/`
- `static/js/documentLibrary.js:2835` → `/api/research/`
- `static/js/documentLibrary.js:2904` → `/api/document/`
- `static/js/documentLibrary.js:2905` → `/api/research/`
- `static/js/documentLibrary.js:2906` → `/api/session/`
- `static/js/documentLibrary.js:2910` → `/api/document/`
- `static/js/documentLibrary.js:2911` → `/api/research/`
- `static/js/documentLibrary.js:2912` → `/api/session/`
- `static/js/documentLibrary.js:3012` → `/api/research/detail/`
- `static/js/documentLibrary.js:3066` → `/api/research/spinoff/`
- `static/js/documentLibrary.js:3084` → `/api/research/report/`
- `static/js/documentLibrary.js:3099` → `/api/research/`
- `static/js/documentLibrary.js:3119` → `/api/research/`
- `static/js/documentLibrary.js:3232` → `/api/research/report/`
- `static/js/documentLibrary.js:3243` → `/api/research/`
- `static/js/documentLibrary.js:3258` → `/api/research/`
- `static/js/documentLibrary.js:3326` → `/api/research/detail/`
- `static/js/documentLibrary.js:3340` → `/api/research/`
- `static/js/documentLibrary.js:3391` → `/api/research/`
- `static/js/documentLibrary.js:3415` → `/api/research/`
- `static/js/emailInbox.js:691` → `/api/email/`
- `static/js/emailInbox.js:815` → `/api/email/read/`
- `static/js/emailInbox.js:1116` → `/api/document failed`
- `static/js/emailInbox.js:1297` → `/api/notes`
- `static/js/emailInbox.js:1318` → `/api/email/archive/`
- `static/js/emailInbox.js:1328` → `/api/email/move/`
- `static/js/emailInbox.js:1351` → `/api/email/delete/`
- `static/js/emailInbox.js:1403` → `/api/email/mark-answered/`
- `static/js/emailInbox.js:1404` → `/api/email/mark-read/`
- `static/js/emailInbox.js:1406` → `/api/email/clear-answered/`
- `static/js/emailLibrary/aiReply.js:430` → `/api/notes`
- `static/js/emailLibrary/attachments.js:57` → `/api/email/attachments-download/`
- `static/js/emailLibrary/attachments.js:107` → `/api/email/attachment/`
- `static/js/emailLibrary/attachments.js:165` → `/api/email/attachment-as-doc/`
- `static/js/emailLibrary/attachments.js:255` → `/api/email/attachment/`
- `static/js/emailLibrary/attachments.js:407` → `/api/email/attachments/`
- `static/js/emailLibrary/bodyRender.js:264` → `/api/email/inline-image/`
- `static/js/emailLibrary/bodyRender.js:409` → `/api/email/inline-image/`
- `static/js/emailLibrary/index.js:1009` → `/api/email/delete/`
- `static/js/emailLibrary/index.js:1138` → `/api/email/read/`
- `static/js/emailLibrary/index.js:1329` → `/api/email/`
- `static/js/emailLibrary/index.js:3345` → `/api/email/accounts/`
- `static/js/emailLibrary/index.js:5246` → `/api/email/scheduled/`
- `static/js/emailLibrary/index.js:5621` → `/api/email/mark-answered/`
- `static/js/emailLibrary/index.js:5622` → `/api/email/mark-read/`
- `static/js/emailLibrary/index.js:5624` → `/api/email/clear-answered/`
- `static/js/emailLibrary/index.js:5653` → `/api/email/flag/`
- `static/js/emailLibrary/index.js:5830` → `/api/email/read/`
- `static/js/emailLibrary/index.js:5871` → `/api/email/read/`
- `static/js/emailLibrary/index.js:6014` → `/api/email/read/`
- `static/js/emailLibrary/menus.js:146` → `/api/email/mark-read/`
- `static/js/emailLibrary/menus.js:148` → `/api/email/mark-unread/`
- `static/js/emailLibrary/menus.js:166` → `/api/email/flag/`
- `static/js/emailLibrary/menus.js:187` → `/api/email/mark-answered/`
- `static/js/emailLibrary/menus.js:188` → `/api/email/mark-read/`
- `static/js/emailLibrary/menus.js:190` → `/api/email/clear-answered/`
- `static/js/emailLibrary/menus.js:201` → `/api/email/archive/`
- `static/js/emailLibrary/menus.js:242` → `/api/email/move/`
- `static/js/emailLibrary/menus.js:254` → `/api/email/delete/`
- `static/js/emailLibrary/menus.js:280` → `/api/email/delete-permanent/`
- `static/js/emailLibrary/menus.js:422` → `/api/email/mark-answered/`
- `static/js/emailLibrary/menus.js:423` → `/api/email/mark-read/`
- `static/js/emailLibrary/menus.js:425` → `/api/email/clear-answered/`
- `static/js/emailLibrary/menus.js:445` → `/api/email/flag/`
- `static/js/emailLibrary/menus.js:457` → `/api/email/archive/`
- `static/js/emailLibrary/menus.js:473` → `/api/email/flag/`
- `static/js/emailLibrary/menus.js:485` → `/api/email/archive/`
- `static/js/emailLibrary/menus.js:520` → `/api/email/delete/`
- `static/js/emailLibrary/menus.js:779` → `/api/email/archive/`
- `static/js/emailLibrary/menus.js:786` → `/api/email/delete-permanent/`
- `static/js/emailLibrary/menus.js:800` → `/api/email/mark-answered/`
- `static/js/emailLibrary/menus.js:801` → `/api/email/mark-read/`
- `static/js/emailLibrary/menus.js:805` → `/api/email/`
- `static/js/emailLibrary/reader.js:301` → `/api/email/read/`
- `static/js/emailLibrary/reader.js:449` → `/api/email/read/`
- `static/js/emailLibrary/settingsPage.js:196` → `/api/calendar/events/`
- `static/js/emailLibrary/settingsPage.js:209` → `/api/calendar/events/`
- `static/js/emailLibrary/settingsPage.js:601` → `/api/email/accounts/`
- `static/js/features/notes/infrastructure/http.js:5` → `/api/notes/`
- `static/js/features/notes/infrastructure/http.js:5` → `/api/notes`
- `static/js/features/notes/infrastructure/http.js:10` → `/api/notes/`
- `static/js/features/notes/infrastructure/http.js:15` → `/api/notes/`
- `static/js/features/notes/infrastructure/http.js:20` → `/api/notes`
- `static/js/features/notes/infrastructure/http.js:22` → `/api/upload`
- `static/js/features/notes/infrastructure/http.js:23` → `/api/upload/`
- `static/js/fileHandler.js:349` → `/api/upload`
- `static/js/gallery.js:260` → `/api/gallery/`
- `static/js/gallery.js:279` → `/api/gallery/`
- `static/js/gallery.js:854` → `/api/gallery/albums/`
- `static/js/gallery.js:875` → `/api/gallery/albums/`
- `static/js/gallery.js:962` → `/api/gallery/albums/`
- `static/js/gallery.js:1135` → `/api/editor-drafts/`
- `static/js/gallery.js:1218` → `/api/editor-drafts/`
- `static/js/gallery.js:1543` → `/api/gallery/`
- `static/js/gallery.js:1862` → `/api/gallery/`
- `static/js/gallery.js:1907` → `/api/gallery/`
- `static/js/gallery.js:2057` → `/api/gallery/`
- `static/js/gallery.js:2090` → `/api/gallery/albums/`
- `static/js/gallery.js:2132` → `/api/gallery/`
- `static/js/gallery.js:2767` → `/api/gallery/`
- `static/js/gallery.js:3301` → `/api/gallery/`
- `static/js/galleryEditor.js:4717` → `/api/editor-drafts/`
- `static/js/galleryEditor.js:4801` → `/api/editor-drafts/`
- `static/js/galleryEditor.js:4830` → `/api/editor-drafts/`
- `static/js/galleryEditor.js:11280` → `/api/gallery/`
- `static/js/group.js:666` → `/api/session/`
- `static/js/group.js:716` → `/api/session/`
- `static/js/group.js:798` → `/api/session/`
- `static/js/group.js:826` → `/api/session/`
- `static/js/group.js:967` → `/api/session/`
- `static/js/keyboard-shortcuts.js:189` → `/api/session/`
- `static/js/keyboard-shortcuts.js:208` → `/api/session/`
- `static/js/markdown.js:816` → `/api/emoji/`
- `static/js/memory.js:360` → `/api/prefs/`
- `static/js/memory.js:380` → `/api/prefs/`
- `static/js/memory.js:408` → `/api/prefs/`
- `static/js/memory.js:422` → `/api/prefs/`
- `static/js/memory.js:441` → `/api/prefs/`
- `static/js/memory.js:455` → `/api/prefs/`
- `static/js/memory.js:484` → `/api/memory`
- `static/js/memory.js:591` → `/api/memory/`
- `static/js/memory.js:649` → `/api/memory`
- `static/js/memory.js:1197` → `/api/memory/`
- `static/js/memory.js:1293` → `/api/memory/`
- `static/js/memory.js:1316` → `/api/memory/`
- `static/js/modelPicker.js:732` → `/api/session/`
- `static/js/modelPicker.js:1095` → `/api/session/`
- `static/js/modelPicker.js:1154` → `/api/session/`
- `static/js/presets.js:250` → `/api/presets/templates/`
- `static/js/presets.js:440` → `/api/session/`
- `static/js/presets.js:1036` → `/api/memory`
- `static/js/providerDeviceFlow.js:6` → `/api/copilot/device/start`
- `static/js/providerDeviceFlow.js:7` → `/api/copilot/device/poll`
- `static/js/providerDeviceFlow.js:14` → `/api/chatgpt-subscription/device/start`
- `static/js/providerDeviceFlow.js:15` → `/api/chatgpt-subscription/device/poll`
- `static/js/rag.js:36` → `/api/personal`
- `static/js/research/jobs.js:263` → `/api/research/cancel/`
- `static/js/research/jobs.js:367` → `/api/research/stream/`
- `static/js/research/jobs.js:401` → `/api/research/status/`
- `static/js/research/jobs.js:441` → `/api/research/result-peek/`
- `static/js/research/panel.js:945` → `/api/research/`
- `static/js/research/panel.js:1289` → `/api/research/report/`
- `static/js/research/panel.js:1306` → `/api/research/report/`
- `static/js/research/panel.js:1653` → `/api/research/result-peek/`
- `static/js/research/panel.js:1786` → `/api/research/spinoff/`
- `static/js/sessions.js:283` → `/api/history/`
- `static/js/sessions.js:615` → `/api/session/`
- `static/js/sessions.js:834` → `/api/session/`
- `static/js/sessions.js:894` → `/api/session/`
- `static/js/sessions.js:1090` → `/api/session/`
- `static/js/sessions.js:1128` → `/api/session/`
- `static/js/sessions.js:1143` → `/api/history/`
- `static/js/sessions.js:1286` → `/api/session/`
- `static/js/sessions.js:1345` → `/api/session/`
- `static/js/sessions.js:2055` → `/api/session/`
- `static/js/sessions.js:2786` → `/api/session/`
- `static/js/sessions.js:2897` → `/api/session/`
- `static/js/sessions.js:2924` → `/api/session/`
- `static/js/sessions.js:3095` → `/api/research/status/`
- `static/js/sessions.js:3224` → `/api/chat/stream_status/`
- `static/js/sessions.js:3288` → `/api/chat/stream_status/`
- `static/js/sessions.js:3439` → `/api/history/`
- `static/js/sessions.js:3482` → `/api/session/`
- `static/js/sessions.js:3514` → `/api/session/`
- `static/js/sessions.js:3824` → `/api/session/`
- `static/js/sessions.js:3827` → `/api/session/`
- `static/js/sessions.js:3848` → `/api/document/`
- `static/js/sessions.js:3850` → `/api/research/`
- `static/js/sessions.js:3910` → `/api/session/`
- `static/js/sessions.js:3940` → `/api/session/`
- `static/js/sessions.js:3979` → `/api/document/`
- `static/js/sessions.js:4018` → `/api/research/report/`
- `static/js/sessions.js:4025` → `/api/research/report/`
- `static/js/sessions.js:4035` → `/api/research/`
- `static/js/settings.js:799` → `/api/`
- `static/js/settings.js:2504` → `/api/email/accounts/`
- `static/js/settings.js:2514` → `/api/email/accounts/`
- `static/js/settings.js:2653` → `/api/email/accounts/`
- `static/js/settings.js:2705` → `/api/email/accounts/`
- `static/js/settings.js:2756` → `/api/email/style${emailAccountSuffix()}`
- `static/js/settings.js:2872` → `/api/email/extract-style${emailAccountSuffix()}`
- `static/js/settings.js:2900` → `/api/email/style${emailAccountSuffix()}`
- `static/js/settings.js:3071` → `/api/auth/integrations/`
- `static/js/settings.js:3097` → `/api/auth/integrations/`
- `static/js/settings.js:3111` → `/api/auth/integrations/`
- `static/js/settings.js:3183` → `/api/claude/plugin.zip`
- `static/js/settings.js:3188` → `/api/claude/plugin.zip`
- `static/js/settings.js:3358` → `/api/auth/integrations/`
- `static/js/settings.js:3359` → `/api/calendar/config/accounts/`
- `static/js/settings.js:3366` → `/api/email/accounts/`
- `static/js/settings.js:3367` → `/api/mcp/servers/`
- `static/js/settings.js:3368` → `/api/tokens/`
- `static/js/settings.js:3560` → `/api/auth/integrations/`
- `static/js/settings.js:3579` → `/api/auth/integrations/`
- `static/js/settings.js:3676` → `/api/calendar/config/accounts/`
- `static/js/settings.js:3974` → `/api/contacts/`
- `static/js/settings.js:3984` → `/api/contacts/`
- `static/js/settings.js:4291` → `/api/email/accounts/`
- `static/js/settings.js:4474` → `/api/email/accounts/`
- `static/js/settings.js:4655` → `/api/mcp/oauth/exchange/`
- `static/js/settings.js:4716` → `/api/mcp/oauth/authorize/`
- `static/js/settings.js:4727` → `/api/mcp/servers/`
- `static/js/settings.js:4737` → `/api/mcp/servers/`
- `static/js/settings.js:4746` → `/api/mcp/servers/`
- `static/js/settings.js:4754` → `/api/mcp/servers/`
- `static/js/settings.js:4998` → `/api/tokens/`
- `static/js/settings.js:5017` → `/api/tokens/`
- `static/js/settings.js:5058` → `/api/tokens/`
- `static/js/settings.js:5084` → `/api/tokens/`
- `static/js/settings.js:5260` → `/api/tokens/`
- `static/js/settings/imagePreferences.js:7` → `/api/prefs`
- `static/js/settings/imagePreferences.js:46` → `/api/prefs/`
- `static/js/settings/imagePreferences.js:64` → `/api/prefs/`
- `static/js/signature.js:349` → `/api/signatures/`
- `static/js/skills.js:54` → `/api/skills/`
- `static/js/skills.js:107` → `/api/skills`
- `static/js/skills.js:706` → `/api/skills/builtin/`
- `static/js/skills.js:740` → `/api/skills/builtin/`
- `static/js/skills.js:755` → `/api/skills/builtin/`
- `static/js/skills.js:1336` → `/api/skills/`
- `static/js/skills.js:1361` → `/api/skills/`
- `static/js/skills.js:1377` → `/api/skills/`
- `static/js/skills.js:1391` → `/api/skills/`
- `static/js/skills.js:1438` → `/api/skills/`
- `static/js/skills.js:1502` → `/api/skills/`
- `static/js/skills.js:2053` → `/api/skills/`
- `static/js/skills.js:2076` → `/api/prefs`
- `static/js/skills.js:2115` → `/api/skills/`
- `static/js/skills.js:2143` → `/api/skills/`
- `static/js/skills.js:2169` → `/api/skills/`
- `static/js/skills.js:2208` → `/api/skills/`
- `static/js/slashCommands.js:43` → `/api/v1`
- `static/js/slashCommands.js:53` → `/api/v1`
- `static/js/slashCommands.js:302` → `/api/session/`
- `static/js/slashCommands.js:373` → `/api/skills/`
- `static/js/slashCommands.js:1035` → `/api/session/`
- `static/js/slashCommands.js:1052` → `/api/session/`
- `static/js/slashCommands.js:1069` → `/api/session/`
- `static/js/slashCommands.js:1079` → `/api/session/`
- `static/js/slashCommands.js:1087` → `/api/session/`
- `static/js/slashCommands.js:1094` → `/api/session/`
- `static/js/slashCommands.js:1106` → `/api/session/`
- `static/js/slashCommands.js:1124` → `/api/session/`
- `static/js/slashCommands.js:1215` → `/api/session/`
- `static/js/slashCommands.js:1577` → `/api/memory`
- `static/js/slashCommands.js:1606` → `/api/memory`
- `static/js/slashCommands.js:1616` → `/api/memory/`
- `static/js/slashCommands.js:1628` → `/api/memory`
- `static/js/slashCommands.js:1633` → `/api/memory/`
- `static/js/slashCommands.js:1696` → `/api/skills/`
- `static/js/slashCommands.js:1724` → `/api/notes`
- `static/js/slashCommands.js:1818` → `/api/notes?note_type=note`
- `static/js/slashCommands.js:1830` → `/api/notes`
- `static/js/slashCommands.js:1895` → `/api/personal`
- `static/js/slashCommands.js:1932` → `/api/personal`
- `static/js/slashCommands.js:2071` → `/api/session/`
- `static/js/slashCommands.js:5187` → `/api/memory`
- `static/js/tasks.js:52` → `/api/tasks?include_last_run=true`
- `static/js/tasks.js:81` → `/api/tasks`
- `static/js/tasks.js:92` → `/api/tasks/`
- `static/js/tasks.js:103` → `/api/tasks/`
- `static/js/tasks.js:144` → `/api/tasks/`
- `static/js/tasks.js:151` → `/api/tasks/`
- `static/js/tasks.js:158` → `/api/tasks/`
- `static/js/tasks.js:176` → `/api/tasks/`
- `static/js/tasks.js:191` → `/api/tasks/`
- `static/js/tasks.js:1587` → `/api/tasks/`
- `static/js/tasks.js:2011` → `/api/tasks/`
- `static/js/tasks.js:2025` → `/api/tasks/`
- `static/js/tasks.js:2507` → `/api/research/report/`
- `static/js/tasks.js:2622` → `/api/research/report/`
- `static/js/tasks.js:2712` → `/api/session/`
- `static/sw.js:395` → `/api/`
