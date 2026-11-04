# HTTP endpoints (FastAPI) ↔ JS fetch() callers

504 route decorators found. JS side: 1008 literal `fetch('/...')` call sites.

Match rule: fetch URL matched against route paths with `{param}` as `[^/]+`.

## `GET /`
- handler: `serve_index` — `app.py:892`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /`
- handler: `root` — `tests/test_diffusion_server_security.py:190`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /`
- handler: `root` — `tests/test_security_headers_middleware.py:26`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/activity/heartbeat`
- handler: `activity_heartbeat` — `app.py:645`
- **JS callers:**
  - `static/app.js:142` → `/api/activity/heartbeat`
  - `static/app.js:145` → `/api/activity/heartbeat`

## `DELETE /api/admin/wipe/{kind}`
- handler: `wipe` — `routes/admin_wipe/admin_wipe_routes.py:72`
- **JS callers:**
  - `static/js/admin.js:2921` → `/api/admin/wipe/${k}`
  - `static/js/admin.js:2941` → `/api/admin/wipe/${kind}`

## `GET /api/assistant/available-timezones`
- handler: `list_timezones` — `routes/assistant_routes.py:318`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/assistant/run-status/{task_id}`
- handler: `run_status` — `routes/assistant_routes.py:293`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/assistant/run/{task_id}`
- handler: `run_check_in_now` — `routes/assistant_routes.py:270`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/assistant/session`
- handler: `get_assistant_session` — `routes/assistant_routes.py:124`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/assistant/settings`
- handler: `get_assistant_settings` — `routes/assistant_routes.py:137`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PATCH /api/assistant/settings`
- handler: `update_assistant_settings` — `routes/assistant_routes.py:158`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/auth/2fa/confirm`
- handler: `totp_confirm` — `routes/auth_routes.py:269`
- **JS callers:**
  - `static/js/settings.js:2135` → `/api/auth/2fa/confirm`

## `POST /api/auth/2fa/disable`
- handler: `totp_disable` — `routes/auth_routes.py:283`
- **JS callers:**
  - `static/js/settings.js:2089` → `/api/auth/2fa/disable`

## `POST /api/auth/2fa/setup`
- handler: `totp_setup` — `routes/auth_routes.py:246`
- **JS callers:**
  - `static/js/settings.js:2109` → `/api/auth/2fa/setup`

## `GET /api/auth/2fa/status`
- handler: `totp_status` — `routes/auth_routes.py:293`
- **JS callers:**
  - `static/js/settings.js:2070` → `/api/auth/2fa/status`

## `POST /api/auth/change-password`
- handler: `change_password` — `routes/auth_routes.py:228`
- **JS callers:**
  - `static/js/settings.js:2045` → `/api/auth/change-password`

## `GET /api/auth/features`
- handler: `get_features` — `routes/auth_routes.py:695`
- **JS callers:**
  - `static/app.js:1510` → `/api/auth/features`
  - `static/js/admin.js:2766` → `/api/auth/features`
  - `static/js/admin.js:2776` → `/api/auth/features`
  - `static/js/censor.js:62` → `/api/auth/features`
  - `static/js/slashCommands.js:889` → `/api/auth/features`
  - `static/js/slashCommands.js:893` → `/api/auth/features`
  - `static/js/slashCommands.js:5188` → `/api/auth/features`

## `POST /api/auth/features`
- handler: `set_features` — `routes/auth_routes.py:700`
- **JS callers:**
  - `static/app.js:1510` → `/api/auth/features`
  - `static/js/admin.js:2766` → `/api/auth/features`
  - `static/js/admin.js:2776` → `/api/auth/features`
  - `static/js/censor.js:62` → `/api/auth/features`
  - `static/js/slashCommands.js:889` → `/api/auth/features`
  - `static/js/slashCommands.js:893` → `/api/auth/features`
  - `static/js/slashCommands.js:5188` → `/api/auth/features`

## `GET /api/auth/integrations`
- handler: `list_integrations_route` — `routes/auth_routes.py:763`
- **JS callers:**
  - `static/js/settings.js:2337` → `/api/auth/integrations`
  - `static/js/settings.js:2364` → `/api/auth/integrations`
  - `static/js/settings.js:2434` → `/api/auth/integrations`
  - `static/js/settings.js:3269` → `/api/auth/integrations`
  - `static/js/settings.js:3302` → `/api/auth/integrations`
  - `static/js/settings.js:3356` → `/api/auth/integrations`
  - `static/js/settings.js:3512` → `/api/auth/integrations`
  - `static/js/settings.js:3799` → `/api/auth/integrations`
  - `static/js/settings.js:3845` → `/api/auth/integrations`

## `POST /api/auth/integrations`
- handler: `create_integration` — `routes/auth_routes.py:779`
- **JS callers:**
  - `static/js/settings.js:2337` → `/api/auth/integrations`
  - `static/js/settings.js:2364` → `/api/auth/integrations`
  - `static/js/settings.js:2434` → `/api/auth/integrations`
  - `static/js/settings.js:3269` → `/api/auth/integrations`
  - `static/js/settings.js:3302` → `/api/auth/integrations`
  - `static/js/settings.js:3356` → `/api/auth/integrations`
  - `static/js/settings.js:3512` → `/api/auth/integrations`
  - `static/js/settings.js:3799` → `/api/auth/integrations`
  - `static/js/settings.js:3845` → `/api/auth/integrations`

## `GET /api/auth/integrations/presets`
- handler: `list_presets` — `routes/auth_routes.py:774`
- **JS callers:**
  - `static/js/settings.js:3242` → `/api/auth/integrations/presets`
  - `static/js/settings.js:3679` → `/api/auth/integrations/presets`

## `DELETE /api/auth/integrations/{integration_id}`
- handler: `delete_integration_route` — `routes/auth_routes.py:801`
- **JS callers:**
  - `static/js/settings.js:3242` → `/api/auth/integrations/presets`
  - `static/js/settings.js:3396` → `/api/auth/integrations/${id}`
  - `static/js/settings.js:3643` → `/api/auth/integrations/${id}`
  - `static/js/settings.js:3679` → `/api/auth/integrations/presets`

## `PUT /api/auth/integrations/{integration_id}`
- handler: `update_integration_route` — `routes/auth_routes.py:789`
- **JS callers:**
  - `static/js/settings.js:3242` → `/api/auth/integrations/presets`
  - `static/js/settings.js:3396` → `/api/auth/integrations/${id}`
  - `static/js/settings.js:3643` → `/api/auth/integrations/${id}`
  - `static/js/settings.js:3679` → `/api/auth/integrations/presets`

## `POST /api/auth/integrations/{integration_id}/test`
- handler: `test_integration_route` — `routes/auth_routes.py:812`
- **JS callers:**
  - `static/js/settings.js:3382` → `/api/auth/integrations/${editingId}/test`
  - `static/js/settings.js:3864` → `/api/auth/integrations/${_editId}/test`

## `POST /api/auth/login`
- handler: `login` — `routes/auth_routes.py:166`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/auth/logout`
- handler: `logout` — `routes/auth_routes.py:198`
- **JS callers:**
  - `static/js/settings.js:2168` → `/api/auth/logout`

## `PUT /api/auth/open-signup`
- handler: `set_signup_enabled` — `routes/auth_routes.py:652`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/auth/policy`
- handler: `auth_policy` — `routes/auth_routes.py:223`
- **JS callers:**
  - `static/js/admin.js:372` → `/api/auth/policy`
  - `static/js/settings.js:2022` → `/api/auth/policy`

## `GET /api/auth/settings`
- handler: `get_settings` — `routes/auth_routes.py:716`
- **JS callers:**
  - `static/js/admin.js:354` → `/api/auth/settings`
  - `static/js/appConfig.js:33` → `/api/auth/settings`
  - `static/js/settings.js:49` → `/api/auth/settings`
  - `static/js/settings.js:404` → `/api/auth/settings`
  - `static/js/settings.js:452` → `/api/auth/settings`
  - `static/js/settings.js:503` → `/api/auth/settings`
  - `static/js/settings.js:509` → `/api/auth/settings`
  - `static/js/settings.js:567` → `/api/auth/settings`
  - `static/js/settings.js:656` → `/api/auth/settings`
  - `static/js/settings.js:720` → `/api/auth/settings`
  - `static/js/settings.js:827` → `/api/auth/settings`
  - `static/js/settings.js:994` → `/api/auth/settings`
  - `static/js/settings.js:1098` → `/api/auth/settings`
  - `static/js/settings.js:1119` → `/api/auth/settings`
  - `static/js/settings.js:1417` → `/api/auth/settings`
  - `static/js/settings.js:1535` → `/api/auth/settings`
  - `static/js/settings.js:1562` → `/api/auth/settings`
  - `static/js/settings.js:1821` → `/api/auth/settings`
  - `static/js/settings.js:2265` → `/api/auth/settings`
  - `static/js/settings.js:2348` → `/api/auth/settings`
  - … +3 more

## `POST /api/auth/settings`
- handler: `set_settings` — `routes/auth_routes.py:727`
- **JS callers:**
  - `static/js/admin.js:354` → `/api/auth/settings`
  - `static/js/appConfig.js:33` → `/api/auth/settings`
  - `static/js/settings.js:49` → `/api/auth/settings`
  - `static/js/settings.js:404` → `/api/auth/settings`
  - `static/js/settings.js:452` → `/api/auth/settings`
  - `static/js/settings.js:503` → `/api/auth/settings`
  - `static/js/settings.js:509` → `/api/auth/settings`
  - `static/js/settings.js:567` → `/api/auth/settings`
  - `static/js/settings.js:656` → `/api/auth/settings`
  - `static/js/settings.js:720` → `/api/auth/settings`
  - `static/js/settings.js:827` → `/api/auth/settings`
  - `static/js/settings.js:994` → `/api/auth/settings`
  - `static/js/settings.js:1098` → `/api/auth/settings`
  - `static/js/settings.js:1119` → `/api/auth/settings`
  - `static/js/settings.js:1417` → `/api/auth/settings`
  - `static/js/settings.js:1535` → `/api/auth/settings`
  - `static/js/settings.js:1562` → `/api/auth/settings`
  - `static/js/settings.js:1821` → `/api/auth/settings`
  - `static/js/settings.js:2265` → `/api/auth/settings`
  - `static/js/settings.js:2348` → `/api/auth/settings`
  - … +3 more

## `POST /api/auth/setup`
- handler: `first_run_setup` — `routes/auth_routes.py:128`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/auth/signup`
- handler: `signup` — `routes/auth_routes.py:146`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/auth/signup-toggle`
- handler: `toggle_signup` — `routes/auth_routes.py:636`
- **JS callers:**
  - `static/js/admin.js:340` → `/api/auth/signup-toggle`

## `GET /api/auth/status`
- handler: `auth_status` — `routes/auth_routes.py:206`
- **JS callers:**
  - `static/app.js:1323` → `/api/auth/status`
  - `static/js/admin.js:334` → `/api/auth/status`
  - `static/js/init.js:45` → `/api/auth/status`
  - `static/js/settings.js:2007` → `/api/auth/status`

## `DELETE /api/auth/users`
- handler: `admin_delete_user` — `routes/auth_routes.py:661`
- **JS callers:**
  - `static/js/admin.js:38` → `/api/auth/users`
  - `static/js/admin.js:199` → `/api/auth/users`
  - `static/js/admin.js:392` → `/api/auth/users`

## `GET /api/auth/users`
- handler: `list_users` — `routes/auth_routes.py:302`
- **JS callers:**
  - `static/js/admin.js:38` → `/api/auth/users`
  - `static/js/admin.js:199` → `/api/auth/users`
  - `static/js/admin.js:392` → `/api/auth/users`

## `POST /api/auth/users`
- handler: `admin_create_user` — `routes/auth_routes.py:309`
- **JS callers:**
  - `static/js/admin.js:38` → `/api/auth/users`
  - `static/js/admin.js:199` → `/api/auth/users`
  - `static/js/admin.js:392` → `/api/auth/users`

## `PUT /api/auth/users/{username}/admin`
- handler: `set_user_admin` — `routes/auth_routes.py:611`
- **JS callers:**
  - `static/js/admin.js:218` → `/api/auth/users/${encodeURIComponent(username)}/admin`

## `PUT /api/auth/users/{username}/privileges`
- handler: `update_user_privileges` — `routes/auth_routes.py:325`
- **JS callers:**
  - `static/js/admin.js:144` → `/api/auth/users/${encodeURIComponent(username)}/privileges`
  - `static/js/admin.js:308` → `/api/auth/users/${encodeURIComponent(username)}/privileges`

## `PUT /api/auth/users/{username}/rename`
- handler: `rename_user` — `routes/auth_routes.py:336`
- **JS callers:**
  - `static/js/admin.js:170` → `/api/auth/users/${encodeURIComponent(oldUsername)}/rename`

## `GET /api/calendar/calendars`
- handler: `list_calendars` — `routes/calendar_routes.py:1117`
- **JS callers:**
  - `static/js/calendar.js:185` → `/api/calendar/calendars`
  - `static/js/calendar.js:2623` → `/api/calendar/calendars?name=`
  - `static/js/cookbookSchedule.js:296` → `/api/calendar/calendars`
  - `static/js/cookbookSchedule.js:300` → `/api/calendar/calendars?name=Cookbook&color=%233b82f6`
  - `static/js/settings.js:3520` → `/api/calendar/calendars`

## `POST /api/calendar/calendars`
- handler: `create_calendar` — `routes/calendar_routes.py:1362`
- **JS callers:**
  - `static/js/calendar.js:185` → `/api/calendar/calendars`
  - `static/js/calendar.js:2623` → `/api/calendar/calendars?name=`
  - `static/js/cookbookSchedule.js:296` → `/api/calendar/calendars`
  - `static/js/cookbookSchedule.js:300` → `/api/calendar/calendars?name=Cookbook&color=%233b82f6`
  - `static/js/settings.js:3520` → `/api/calendar/calendars`

## `DELETE /api/calendar/calendars/{cal_id}`
- handler: `delete_calendar` — `routes/calendar_routes.py:1097`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PUT /api/calendar/calendars/{cal_id}`
- handler: `update_calendar` — `routes/calendar_routes.py:1385`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/calendar/config`
- handler: `get_config` — `routes/calendar_routes.py:833`
- **JS callers:**
  - `static/js/admin.js:2793` → `/api/calendar/config`
  - `static/js/admin.js:2803` → `/api/calendar/config`
  - `static/js/admin.js:2819` → `/api/calendar/config`

## `POST /api/calendar/config`
- handler: `save_config` — `routes/calendar_routes.py:857`
- **JS callers:**
  - `static/js/admin.js:2793` → `/api/calendar/config`
  - `static/js/admin.js:2803` → `/api/calendar/config`
  - `static/js/admin.js:2819` → `/api/calendar/config`

## `GET /api/calendar/config/accounts`
- handler: `list_caldav_accounts` — `routes/calendar_routes.py:890`
- **JS callers:**
  - `static/js/settings.js:3513` → `/api/calendar/config/accounts`
  - `static/js/settings.js:3900` → `/api/calendar/config/accounts`
  - `static/js/settings.js:3955` → `/api/calendar/config/accounts`

## `POST /api/calendar/config/accounts`
- handler: `add_caldav_account` — `routes/calendar_routes.py:914`
- **JS callers:**
  - `static/js/settings.js:3513` → `/api/calendar/config/accounts`
  - `static/js/settings.js:3900` → `/api/calendar/config/accounts`
  - `static/js/settings.js:3955` → `/api/calendar/config/accounts`

## `DELETE /api/calendar/config/accounts/{account_id}`
- handler: `delete_caldav_account` — `routes/calendar_routes.py:973`
- **JS callers:**
  - `static/js/settings.js:3644` → `/api/calendar/config/accounts/${id}`
  - `static/js/settings.js:3961` → `/api/calendar/config/accounts/${editId}`

## `PUT /api/calendar/config/accounts/{account_id}`
- handler: `update_caldav_account` — `routes/calendar_routes.py:943`
- **JS callers:**
  - `static/js/settings.js:3644` → `/api/calendar/config/accounts/${id}`
  - `static/js/settings.js:3961` → `/api/calendar/config/accounts/${editId}`

## `GET /api/calendar/events`
- handler: `list_events` — `routes/calendar_routes.py:1140`
- **JS callers:**
  - `static/js/calendar.js:123` → `/api/calendar/events?start=`
  - `static/js/calendar.js:164` → `/api/calendar/events?start=`
  - `static/js/calendar.js:254` → `/api/calendar/events`
  - `static/js/cookbookSchedule.js:331` → `/api/calendar/events`
  - `static/js/slashCommands.js:1849` → `/api/calendar/events`

## `POST /api/calendar/events`
- handler: `create_event` — `routes/calendar_routes.py:1206`
- **JS callers:**
  - `static/js/calendar.js:123` → `/api/calendar/events?start=`
  - `static/js/calendar.js:164` → `/api/calendar/events?start=`
  - `static/js/calendar.js:254` → `/api/calendar/events`
  - `static/js/cookbookSchedule.js:331` → `/api/calendar/events`
  - `static/js/slashCommands.js:1849` → `/api/calendar/events`

## `DELETE /api/calendar/events/{uid}`
- handler: `delete_event` — `routes/calendar_routes.py:1320`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PUT /api/calendar/events/{uid}`
- handler: `update_event` — `routes/calendar_routes.py:1268`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/calendar/export/{cal_id}`
- handler: `export_ics` — `routes/calendar_routes.py:1562`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/calendar/import`
- handler: `import_ics` — `routes/calendar_routes.py:1412`
- **JS callers:**
  - `static/js/calendar.js:2698` → `/api/calendar/import`

## `POST /api/calendar/quick-parse`
- handler: `quick_parse` — `routes/calendar_routes.py:1620`
- **JS callers:**
  - `static/js/calendar.js:2033` → `/api/calendar/quick-parse`

## `POST /api/calendar/sync`
- handler: `sync_caldav_endpoint` — `routes/calendar_routes.py:1087`
- **JS callers:**
  - `static/js/calendar.js:208` → `/api/calendar/sync`

## `POST /api/calendar/test`
- handler: `test_connection` — `routes/calendar_routes.py:984`
- **JS callers:**
  - `static/js/admin.js:2824` → `/api/calendar/test`
  - `static/js/settings.js:3921` → `/api/calendar/test`

## `POST /api/chat`
- handler: `chat_endpoint` — `routes/chat_routes.py:929`
- **JS callers:**
  - `static/js/slashCommands.js:655` → `/api/chat`

## `GET /api/chat/reasoning-control`
- handler: `reasoning_control` — `routes/chat_routes.py:3163`
- **JS callers:**
  - `static/js/chat.js:6075` → `/api/chat/reasoning-control?model=`

## `GET /api/chat/resume/{session_id}`
- handler: `chat_resume` — `routes/chat_routes.py:3080`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/chat/stop/{session_id}`
- handler: `chat_stop` — `routes/chat_routes.py:3096`
- **JS callers:**
  - `static/js/chat.js:1031` → `/api/chat/stop/${encodeURIComponent(sessionId)}`

## `GET /api/chat/stream_status/{session_id}`
- handler: `chat_stream_status` — `routes/chat_routes.py:3106`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/chat_stream`
- handler: `chat_stream` — `routes/chat_routes.py:1123`
- **JS callers:**
  - `static/js/chat.js:2502` → `/api/chat_stream`
  - `static/js/compare/stream.js:243` → `/api/chat_stream`
  - `static/js/compare/stream.js:409` → `/api/chat_stream`
  - `static/js/group.js:855` → `/api/chat_stream`
  - `static/js/notes.js:4524` → `/api/chat_stream`
  - `static/js/notes.js:4595` → `/api/chat_stream`

## `GET /api/cleanup/preview`
- handler: `cleanup_preview` — `routes/cleanup/cleanup_routes.py:23`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/client-perf`
- handler: `client_perf` — `app.py:960`
- **JS callers:**
  - `static/js/chat.js:371` → `/api/client-perf`
  - `static/js/chat.js:376` → `/api/client-perf`

## `GET /api/codex/calendar/events`
- handler: `codex_calendar_list` — `routes/codex_routes.py:421`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/calendar/events`
- handler: `codex_calendar_create` — `routes/codex_routes.py:428`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/codex/calendar/events/{uid}`
- handler: `codex_calendar_delete` — `routes/codex_routes.py:489`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/capabilities`
- handler: `capabilities` — `routes/codex_routes.py:168`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/cookbook/adopt`
- handler: `codex_cookbook_adopt` — `routes/codex_routes.py:826`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/cookbook/cached`
- handler: `codex_cookbook_cached` — `routes/codex_routes.py:693`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/cookbook/output/{session_id}`
- handler: `codex_cookbook_output` — `routes/codex_routes.py:595`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/cookbook/preset/{name}`
- handler: `codex_cookbook_serve_preset` — `routes/codex_routes.py:776`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/cookbook/presets`
- handler: `codex_cookbook_presets` — `routes/codex_routes.py:755`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/cookbook/serve`
- handler: `codex_cookbook_serve` — `routes/codex_routes.py:637`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/cookbook/servers`
- handler: `codex_cookbook_servers` — `routes/codex_routes.py:576`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/cookbook/stop/{session_id}`
- handler: `codex_cookbook_stop` — `routes/codex_routes.py:676`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/cookbook/tasks`
- handler: `codex_cookbook_tasks` — `routes/codex_routes.py:569`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/documents`
- handler: `codex_documents_library` — `routes/codex_routes.py:443`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/documents`
- handler: `codex_documents_create` — `routes/codex_routes.py:503`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/codex/documents/{doc_id}`
- handler: `codex_documents_delete` — `routes/codex_routes.py:496`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/documents/{doc_id}`
- handler: `codex_documents_get` — `routes/codex_routes.py:469`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/emails`
- handler: `list_emails` — `routes/codex_routes.py:252`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/emails/draft`
- handler: `codex_email_draft` — `routes/codex_routes.py:364`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/emails/draft-document`
- handler: `codex_email_draft_document` — `routes/codex_routes.py:339`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/emails/send`
- handler: `codex_email_send` — `routes/codex_routes.py:377`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/emails/{uid}`
- handler: `read_email` — `routes/codex_routes.py:284`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/memory`
- handler: `codex_memory_list` — `routes/codex_routes.py:392`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/memory`
- handler: `codex_memory_add` — `routes/codex_routes.py:399`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/codex/memory/{memory_id}`
- handler: `codex_memory_delete` — `routes/codex_routes.py:482`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/codex/plugin.zip`
- handler: `plugin_zip` — `routes/codex_routes.py:219`
- **JS callers:**
  - `static/js/settings.js:3430` → `/api/codex/plugin.zip`
  - `static/js/settings.js:3430` → `/api/codex/plugin.zip`
  - `static/js/settings.js:3435` → `/api/codex/plugin.zip`
  - `static/js/settings.js:3435` → `/api/codex/plugin.zip`

## `GET /api/codex/plugin.zip`
- handler: `plugin_zip` — `routes/codex_routes.py:892`
- **JS callers:**
  - `static/js/settings.js:3430` → `/api/codex/plugin.zip`
  - `static/js/settings.js:3430` → `/api/codex/plugin.zip`
  - `static/js/settings.js:3435` → `/api/codex/plugin.zip`
  - `static/js/settings.js:3435` → `/api/codex/plugin.zip`

## `GET /api/codex/todos`
- handler: `list_todos` — `routes/codex_routes.py:235`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/codex/todos`
- handler: `manage_todos` — `routes/codex_routes.py:243`
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
  - `static/js/compare/vote.js:130` → `/api/compare/record`

## `POST /api/compare/start`
- handler: `start_comparison` — `routes/compare/compare_routes.py:71`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/compare/{comp_id}`
- handler: `delete_comparison` — `routes/compare/compare_routes.py:347`
- **JS callers:**
  - `static/js/compare/vote.js:130` → `/api/compare/record`

## `POST /api/compare/{comp_id}/vote`
- handler: `vote_comparison` — `routes/compare/compare_routes.py:238`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/contacts/add`
- handler: `add_contact` — `routes/contacts/contacts_routes.py:766`
- **JS callers:**
  - `static/js/document.js:3960` → `/api/contacts/add`
  - `static/js/emailLibrary.js:7815` → `/api/contacts/add`
  - `static/js/settings.js:4074` → `/api/contacts/add`

## `DELETE /api/contacts/clear`
- handler: `clear_contacts` — `routes/contacts/contacts_routes.py:882`
- **JS callers:**
  - `static/js/settings.js:3646` → `/api/contacts/clear`

## `GET /api/contacts/config`
- handler: `get_config` — `routes/contacts/contacts_routes.py:853`
- **JS callers:**
  - `static/js/settings.js:3067` → `/api/contacts/config`
  - `static/js/settings.js:3116` → `/api/contacts/config`
  - `static/js/settings.js:3514` → `/api/contacts/config`
  - `static/js/settings.js:3649` → `/api/contacts/config`
  - `static/js/settings.js:4031` → `/api/contacts/config`
  - `static/js/settings.js:4044` → `/api/contacts/config`

## `PUT /api/contacts/config`
- handler: `update_config` — `routes/contacts/contacts_routes.py:861`
- **JS callers:**
  - `static/js/settings.js:3067` → `/api/contacts/config`
  - `static/js/settings.js:3116` → `/api/contacts/config`
  - `static/js/settings.js:3514` → `/api/contacts/config`
  - `static/js/settings.js:3649` → `/api/contacts/config`
  - `static/js/settings.js:4031` → `/api/contacts/config`
  - `static/js/settings.js:4044` → `/api/contacts/config`

## `GET /api/contacts/export`
- handler: `export_contacts` — `routes/contacts/contacts_routes.py:832`
- **JS callers:**
  - `static/js/settings.js:4088` → `/api/contacts/export?format=${encodeURIComponent(format)}`
  - `static/js/settings.js:4088` → `/api/contacts/export?format=`

## `POST /api/contacts/import`
- handler: `import_vcf` — `routes/contacts/contacts_routes.py:813`
- **JS callers:**
  - `static/js/settings.js:4129` → `/api/contacts/import`

## `GET /api/contacts/list`
- handler: `list_contacts` — `routes/contacts/contacts_routes.py:742`
- **JS callers:**
  - `static/js/emailLibrary.js:3642` → `/api/contacts/list`
  - `static/js/settings.js:3515` → `/api/contacts/list`
  - `static/js/settings.js:4163` → `/api/contacts/list`

## `GET /api/contacts/search`
- handler: `search_contacts` — `routes/contacts/contacts_routes.py:748`
- **JS callers:**
  - `static/js/document.js:3661` → `/api/contacts/search?q=`

## `DELETE /api/contacts/{uid}`
- handler: `delete_contact` — `routes/contacts/contacts_routes.py:909`
- **JS callers:**
  - `static/js/document.js:3661` → `/api/contacts/search?q=`
  - `static/js/document.js:3960` → `/api/contacts/add`
  - `static/js/emailLibrary.js:3642` → `/api/contacts/list`
  - `static/js/emailLibrary.js:7815` → `/api/contacts/add`
  - `static/js/settings.js:3067` → `/api/contacts/config`
  - `static/js/settings.js:3116` → `/api/contacts/config`
  - `static/js/settings.js:3514` → `/api/contacts/config`
  - `static/js/settings.js:3515` → `/api/contacts/list`
  - `static/js/settings.js:3646` → `/api/contacts/clear`
  - `static/js/settings.js:3649` → `/api/contacts/config`
  - `static/js/settings.js:4031` → `/api/contacts/config`
  - `static/js/settings.js:4044` → `/api/contacts/config`
  - `static/js/settings.js:4074` → `/api/contacts/add`
  - `static/js/settings.js:4088` → `/api/contacts/export?format=${encodeURIComponent(format)}`
  - `static/js/settings.js:4088` → `/api/contacts/export?format=`
  - `static/js/settings.js:4129` → `/api/contacts/import`
  - `static/js/settings.js:4163` → `/api/contacts/list`

## `PUT /api/contacts/{uid}`
- handler: `edit_contact` — `routes/contacts/contacts_routes.py:891`
- **JS callers:**
  - `static/js/document.js:3661` → `/api/contacts/search?q=`
  - `static/js/document.js:3960` → `/api/contacts/add`
  - `static/js/emailLibrary.js:3642` → `/api/contacts/list`
  - `static/js/emailLibrary.js:7815` → `/api/contacts/add`
  - `static/js/settings.js:3067` → `/api/contacts/config`
  - `static/js/settings.js:3116` → `/api/contacts/config`
  - `static/js/settings.js:3514` → `/api/contacts/config`
  - `static/js/settings.js:3515` → `/api/contacts/list`
  - `static/js/settings.js:3646` → `/api/contacts/clear`
  - `static/js/settings.js:3649` → `/api/contacts/config`
  - `static/js/settings.js:4031` → `/api/contacts/config`
  - `static/js/settings.js:4044` → `/api/contacts/config`
  - `static/js/settings.js:4074` → `/api/contacts/add`
  - `static/js/settings.js:4088` → `/api/contacts/export?format=${encodeURIComponent(format)}`
  - `static/js/settings.js:4088` → `/api/contacts/export?format=`
  - `static/js/settings.js:4129` → `/api/contacts/import`
  - `static/js/settings.js:4163` → `/api/contacts/list`

## `GET /api/conversations/topics`
- handler: `get_conversation_topics` — `routes/history/history_routes.py:929`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/cookbook/gpus`
- handler: `list_gpus` — `routes/cookbook_routes.py:3142`
- **JS callers:**
  - `static/js/cookbookRunning.js:1889` → `/api/cookbook/gpus`
  - `static/js/cookbookServe.js:2105` → `/api/cookbook/gpus`
  - `static/js/cookbookServe.js:2935` → `/api/cookbook/gpus`
  - `static/js/cookbookServe.js:3458` → `/api/cookbook/gpus`
  - `static/js/cookbookServe.js:3570` → `/api/cookbook/gpus`

## `GET /api/cookbook/hf-gguf-files`
- handler: `hf_gguf_files` — `routes/cookbook_routes.py:3868`
- **JS callers:**
  - `static/js/cookbook.js:2403` → `/api/cookbook/hf-gguf-files?repo_id=${encodeURIComponent(repo)}`
  - `static/js/cookbook.js:2403` → `/api/cookbook/hf-gguf-files?repo_id=`

## `GET /api/cookbook/hf-latest`
- handler: `hf_latest` — `routes/cookbook_routes.py:3519`
- **JS callers:**
  - `static/js/cookbook.js:2691` → `/api/cookbook/hf-latest?vram_gb=${v}&limit=10`
  - `static/js/cookbook.js:2691` → `/api/cookbook/hf-latest?vram_gb=`

## `POST /api/cookbook/install-system-deps`
- handler: `install_system_deps` — `routes/shell_routes.py:1810`
- **JS callers:**
  - `static/js/cookbook.js:1610` → `/api/cookbook/install-system-deps`

## `POST /api/cookbook/kill-pid`
- handler: `kill_pid` — `routes/cookbook_routes.py:3317`
- **JS callers:**
  - `static/js/cookbookServe.js:2829` → `/api/cookbook/kill-pid`
  - `static/js/cookbookServe.js:3052` → `/api/cookbook/kill-pid`
  - `static/js/cookbookServe.js:3076` → `/api/cookbook/kill-pid`

## `GET /api/cookbook/ollama/library`
- handler: `ollama_library` — `routes/cookbook_routes.py:3934`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:588` → `/api/cookbook/ollama/library`
  - `static/js/cookbook.js:2784` → `/api/cookbook/ollama/library`

## `GET /api/cookbook/packages`
- handler: `list_packages` — `routes/shell_routes.py:1184`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:113` → `/api/cookbook/packages`
  - `static/js/cookbook.js:1125` → `/api/cookbook/packages`
  - `static/js/cookbookServe.js:836` → `/api/cookbook/packages`
  - `static/js/galleryEditor.js:3779` → `/api/cookbook/packages`
  - `static/js/galleryEditor.js:3791` → `/api/cookbook/packages`

## `POST /api/cookbook/packages/install`
- handler: `install_package` — `routes/shell_routes.py:1763`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/cookbook/rebuild-engine`
- handler: `rebuild_engine` — `routes/shell_routes.py:1931`
- **JS callers:**
  - `static/js/cookbook.js:1796` → `/api/cookbook/rebuild-engine`

## `POST /api/cookbook/setup`
- handler: `server_setup` — `routes/cookbook_routes.py:2838`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:2651` → `/api/cookbook/setup`

## `GET /api/cookbook/ssh-key`
- handler: `get_cookbook_ssh_key` — `routes/cookbook_routes.py:926`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:2396` → `/api/cookbook/ssh-key`

## `POST /api/cookbook/ssh-key`
- handler: `generate_cookbook_ssh_key` — `routes/cookbook_routes.py:935`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:2396` → `/api/cookbook/ssh-key`

## `GET /api/cookbook/state`
- handler: `get_cookbook_state` — `routes/cookbook_routes.py:3368`
- **JS callers:**
  - `static/js/cookbookRunning.js:1351` → `/api/cookbook/state`
  - `static/js/cookbookRunning.js:1391` → `/api/cookbook/state`
  - `static/js/cookbookRunning.js:4117` → `/api/cookbook/state`

## `POST /api/cookbook/state`
- handler: `save_cookbook_state` — `routes/cookbook_routes.py:3396`
- **JS callers:**
  - `static/js/cookbookRunning.js:1351` → `/api/cookbook/state`
  - `static/js/cookbookRunning.js:1391` → `/api/cookbook/state`
  - `static/js/cookbookRunning.js:4117` → `/api/cookbook/state`

## `GET /api/cookbook/tasks/status`
- handler: `cookbook_tasks_status` — `routes/cookbook_routes.py:4197`
- **JS callers:**
  - `static/js/cookbookRunning.js:4140` → `/api/cookbook/tasks/status`

## `POST /api/cookbook/test-ssh`
- handler: `test_cookbook_ssh` — `routes/cookbook_routes.py:965`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:2350` → `/api/cookbook/test-ssh`

## `GET /api/cookbook/vllm-recipe`
- handler: `vllm_recipe` — `routes/cookbook_routes.py:4081`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/cookbook/vllm-recipe-manifest`
- handler: `vllm_recipe_manifest` — `routes/cookbook_routes.py:4021`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/db/stats`
- handler: `get_database_stats` — `routes/diagnostics_routes.py:57`
- **JS callers:**
  - `static/js/slashCommands.js:1995` → `/api/db/stats`

## `GET /api/default-chat`
- handler: `get_default_chat` — `routes/model_routes.py:2415`
- **JS callers:**
  - `static/app.js:224` → `/api/default-chat`
  - `static/js/chat.js:1780` → `/api/default-chat`
  - `static/js/emailInbox.js:1357` → `/api/default-chat`
  - `static/js/gallery.js:1538` → `/api/default-chat`
  - `static/js/modelPicker.js:141` → `/api/default-chat`
  - `static/js/notes.js:4493` → `/api/default-chat`
  - `static/js/notes.js:4561` → `/api/default-chat`
  - `static/js/sessions.js:2289` → `/api/default-chat`
  - `static/js/slashCommands.js:967` → `/api/default-chat`
  - `static/js/tasks.js:2540` → `/api/default-chat`

## `GET /api/diagnostics/logs`
- handler: `get_diagnostics_logs` — `routes/diagnostics_routes.py:33`
- **JS callers:**
  - `static/js/admin.js:3039` → `/api/diagnostics/logs?limit=${limit}`
  - `static/js/admin.js:3039` → `/api/diagnostics/logs?limit=`

## `GET /api/diagnostics/services`
- handler: `get_service_health` — `routes/diagnostics_routes.py:25`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/discover`
- handler: `discover_local` — `routes/model_routes.py:1925`
- **JS callers:**
  - `static/js/admin.js:1693` → `/api/discover`

## `POST /api/document`
- handler: `create_document` — `routes/document/document_routes.py:106`
- **JS callers:**
  - `static/app.js:549` → `/api/document`
  - `static/app.js:549` → `/api/document`
  - `static/js/chat.js:2119` → `/api/document`
  - `static/js/chat.js:2119` → `/api/document`
  - `static/js/chat.js:7627` → `/api/document`
  - `static/js/chat.js:7627` → `/api/document`
  - `static/js/document.js:4665` → `/api/document`
  - `static/js/document.js:4665` → `/api/document`
  - `static/js/document.js:7033` → `/api/document`
  - `static/js/document.js:7033` → `/api/document`
  - `static/js/document.js:9361` → `/api/document`
  - `static/js/document.js:9361` → `/api/document`
  - `static/js/document.js:9580` → `/api/document`
  - `static/js/document.js:9580` → `/api/document`
  - `static/js/documentLibrary.js:1091` → `/api/document`
  - `static/js/documentLibrary.js:1091` → `/api/document`
  - `static/js/documentLibrary.js:1541` → `/api/document`
  - `static/js/documentLibrary.js:1541` → `/api/document`
  - `static/js/documentLibrary.js:1551` → `/api/document`
  - `static/js/documentLibrary.js:1551` → `/api/document`
  - … +4 more

## `POST /api/document`
- handler: `create_document` — `tests/test_codex_ssh_host_validation.py:232`
- **JS callers:**
  - `static/app.js:549` → `/api/document`
  - `static/app.js:549` → `/api/document`
  - `static/js/chat.js:2119` → `/api/document`
  - `static/js/chat.js:2119` → `/api/document`
  - `static/js/chat.js:7627` → `/api/document`
  - `static/js/chat.js:7627` → `/api/document`
  - `static/js/document.js:4665` → `/api/document`
  - `static/js/document.js:4665` → `/api/document`
  - `static/js/document.js:7033` → `/api/document`
  - `static/js/document.js:7033` → `/api/document`
  - `static/js/document.js:9361` → `/api/document`
  - `static/js/document.js:9361` → `/api/document`
  - `static/js/document.js:9580` → `/api/document`
  - `static/js/document.js:9580` → `/api/document`
  - `static/js/documentLibrary.js:1091` → `/api/document`
  - `static/js/documentLibrary.js:1091` → `/api/document`
  - `static/js/documentLibrary.js:1541` → `/api/document`
  - `static/js/documentLibrary.js:1541` → `/api/document`
  - `static/js/documentLibrary.js:1551` → `/api/document`
  - `static/js/documentLibrary.js:1551` → `/api/document`
  - … +4 more

## `DELETE /api/document/{doc_id}`
- handler: `delete_document` — `routes/document/document_routes.py:738`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}`
- handler: `get_document` — `routes/document/document_routes.py:470`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PATCH /api/document/{doc_id}`
- handler: `patch_document` — `routes/document/document_routes.py:699`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PUT /api/document/{doc_id}`
- handler: `update_document` — `routes/document/document_routes.py:624`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/document/{doc_id}/ai-fill-annotations`
- handler: `ai_fill_annotations` — `routes/document/document_routes.py:1239`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/document/{doc_id}/archive`
- handler: `archive_document` — `routes/document/document_routes.py:484`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/export-pdf`
- handler: `export_pdf` — `routes/document/document_routes.py:1479`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/document/{doc_id}/export-pdf/preview`
- handler: `export_pdf_preview` — `routes/document/document_routes.py:1065`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/document/{doc_id}/extract-pdf-text`
- handler: `extract_pdf_text` — `routes/document/document_routes.py:500`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/page/{page_no}.png`
- handler: `render_page_png` — `routes/document/document_routes.py:1198`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/document/{doc_id}/prepare-signed-reply`
- handler: `prepare_signed_reply` — `routes/document/document_routes.py:1615`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/render-pages`
- handler: `render_pages` — `routes/document/document_routes.py:1127`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/render-pdf`
- handler: `render_pdf` — `routes/document/document_routes.py:1379`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/render-pdf`
- handler: `render_pdf` — `tests/test_security_headers_pdf_preview.py:17`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/document/{doc_id}/restore/{num}`
- handler: `restore_version` — `routes/document/document_routes.py:812`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/version/{num}`
- handler: `get_version` — `routes/document/document_routes.py:791`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/document/{doc_id}/versions`
- handler: `list_versions` — `routes/document/document_routes.py:766`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/documents/ai-tidy`
- handler: `ai_tidy_documents` — `routes/document/document_routes.py:968`
- **JS callers:**
  - `static/js/documentLibrary.js:3288` → `/api/documents/ai-tidy`

## `POST /api/documents/export-zip`
- handler: `documents_export_zip` — `routes/document/document_routes.py:560`
- **JS callers:**
  - `static/js/documentLibrary.js:1307` → `/api/documents/export-zip`

## `POST /api/documents/import-pdf`
- handler: `import_pdf` — `routes/document/document_routes.py:222`
- **JS callers:**
  - `static/js/chat.js:7622` → `/api/documents/import-pdf`
  - `static/js/document.js:9565` → `/api/documents/import-pdf`
  - `static/js/documentLibrary.js:1518` → `/api/documents/import-pdf`

## `GET /api/documents/library`
- handler: `documents_library` — `routes/document/document_routes.py:324`
- **JS callers:**
  - `static/js/document.js:3374` → `/api/documents/library?`
  - `static/js/document.js:3374` → `/api/documents/library?`
  - `static/js/documentLibrary.js:332` → `/api/documents/library?`
  - `static/js/documentLibrary.js:332` → `/api/documents/library?`
  - `static/js/documentLibrary.js:2330` → `/api/documents/library?archived=true&limit=50`
  - `static/js/documentLibrary.js:2330` → `/api/documents/library?archived=true&limit=50`
  - `static/js/sessions.js:3522` → `/api/documents/library?`
  - `static/js/sessions.js:3522` → `/api/documents/library?`
  - `static/js/slashCommands.js:4829` → `/api/documents/library?limit=1&sort=recent`
  - `static/js/slashCommands.js:4829` → `/api/documents/library?limit=1&sort=recent`

## `GET /api/documents/library`
- handler: `documents_library` — `tests/test_codex_ssh_host_validation.py:108`
- **JS callers:**
  - `static/js/document.js:3374` → `/api/documents/library?`
  - `static/js/document.js:3374` → `/api/documents/library?`
  - `static/js/documentLibrary.js:332` → `/api/documents/library?`
  - `static/js/documentLibrary.js:332` → `/api/documents/library?`
  - `static/js/documentLibrary.js:2330` → `/api/documents/library?archived=true&limit=50`
  - `static/js/documentLibrary.js:2330` → `/api/documents/library?archived=true&limit=50`
  - `static/js/sessions.js:3522` → `/api/documents/library?`
  - `static/js/sessions.js:3522` → `/api/documents/library?`
  - `static/js/slashCommands.js:4829` → `/api/documents/library?limit=1&sort=recent`
  - `static/js/slashCommands.js:4829` → `/api/documents/library?limit=1&sort=recent`

## `POST /api/documents/tidy`
- handler: `tidy_documents` — `routes/document/document_routes.py:853`
- **JS callers:**
  - `static/js/documentLibrary.js:3277` → `/api/documents/tidy`

## `GET /api/documents/{session_id}`
- handler: `list_documents` — `routes/document/document_routes.py:446`
- **JS callers:**
  - `static/js/chat.js:7622` → `/api/documents/import-pdf`
  - `static/js/document.js:3374` → `/api/documents/library?`
  - `static/js/document.js:9565` → `/api/documents/import-pdf`
  - `static/js/documentLibrary.js:332` → `/api/documents/library?`
  - `static/js/documentLibrary.js:1307` → `/api/documents/export-zip`
  - `static/js/documentLibrary.js:1518` → `/api/documents/import-pdf`
  - `static/js/documentLibrary.js:2330` → `/api/documents/library?archived=true&limit=50`
  - `static/js/documentLibrary.js:3277` → `/api/documents/tidy`
  - `static/js/documentLibrary.js:3288` → `/api/documents/ai-tidy`
  - `static/js/sessions.js:3522` → `/api/documents/library?`
  - `static/js/slashCommands.js:4829` → `/api/documents/library?limit=1&sort=recent`

## `GET /api/editor-drafts`
- handler: `list_drafts` — `routes/editor_draft_routes.py:82`
- **JS callers:**
  - `static/js/gallery.js:931` → `/api/editor-drafts`
  - `static/js/galleryEditor.js:1127` → `/api/editor-drafts`
  - `static/js/galleryEditor.js:1168` → `/api/editor-drafts`

## `POST /api/editor-drafts`
- handler: `create_draft` — `routes/editor_draft_routes.py:112`
- **JS callers:**
  - `static/js/gallery.js:931` → `/api/editor-drafts`
  - `static/js/galleryEditor.js:1127` → `/api/editor-drafts`
  - `static/js/galleryEditor.js:1168` → `/api/editor-drafts`

## `DELETE /api/editor-drafts/{draft_id}`
- handler: `delete_draft` — `routes/editor_draft_routes.py:170`
- **JS callers:**
  - `static/js/galleryEditor.js:1113` → `/api/editor-drafts/${encodeURIComponent(state.draftId)}`
  - `static/js/galleryEditor.js:1153` → `/api/editor-drafts/${encodeURIComponent(draftId)}`
  - `static/js/galleryEditor.js:1182` → `/api/editor-drafts/${encodeURIComponent(draftId)}`

## `GET /api/editor-drafts/{draft_id}`
- handler: `get_draft` — `routes/editor_draft_routes.py:95`
- **JS callers:**
  - `static/js/galleryEditor.js:1113` → `/api/editor-drafts/${encodeURIComponent(state.draftId)}`
  - `static/js/galleryEditor.js:1153` → `/api/editor-drafts/${encodeURIComponent(draftId)}`
  - `static/js/galleryEditor.js:1182` → `/api/editor-drafts/${encodeURIComponent(draftId)}`

## `PUT /api/editor-drafts/{draft_id}`
- handler: `update_draft` — `routes/editor_draft_routes.py:138`
- **JS callers:**
  - `static/js/galleryEditor.js:1113` → `/api/editor-drafts/${encodeURIComponent(state.draftId)}`
  - `static/js/galleryEditor.js:1153` → `/api/editor-drafts/${encodeURIComponent(draftId)}`
  - `static/js/galleryEditor.js:1182` → `/api/editor-drafts/${encodeURIComponent(draftId)}`

## `GET /api/email/accounts`
- handler: `list_email_accounts` — `routes/email_routes.py:5605`
- **JS callers:**
  - `static/js/document.js:88` → `/api/email/accounts`
  - `static/js/emailLibrary.js:2314` → `/api/email/accounts`
  - `static/js/emailLibrary.js:3172` → `/api/email/accounts`
  - `static/js/settings.js:2310` → `/api/email/accounts`
  - `static/js/settings.js:2320` → `/api/email/accounts`
  - `static/js/settings.js:2424` → `/api/email/accounts`
  - `static/js/settings.js:2757` → `/api/email/accounts`
  - `static/js/settings.js:2938` → `/api/email/accounts`
  - `static/js/settings.js:2990` → `/api/email/accounts`
  - `static/js/settings.js:3516` → `/api/email/accounts`
  - `static/js/settings.js:4285` → `/api/email/accounts`
  - `static/js/settings.js:4576` → `/api/email/accounts`
  - `static/js/settings.js:4759` → `/api/email/accounts`
  - `static/js/tasks.js:257` → `/api/email/accounts`

## `POST /api/email/accounts`
- handler: `create_email_account` — `routes/email_routes.py:5649`
- **JS callers:**
  - `static/js/document.js:88` → `/api/email/accounts`
  - `static/js/emailLibrary.js:2314` → `/api/email/accounts`
  - `static/js/emailLibrary.js:3172` → `/api/email/accounts`
  - `static/js/settings.js:2310` → `/api/email/accounts`
  - `static/js/settings.js:2320` → `/api/email/accounts`
  - `static/js/settings.js:2424` → `/api/email/accounts`
  - `static/js/settings.js:2757` → `/api/email/accounts`
  - `static/js/settings.js:2938` → `/api/email/accounts`
  - `static/js/settings.js:2990` → `/api/email/accounts`
  - `static/js/settings.js:3516` → `/api/email/accounts`
  - `static/js/settings.js:4285` → `/api/email/accounts`
  - `static/js/settings.js:4576` → `/api/email/accounts`
  - `static/js/settings.js:4759` → `/api/email/accounts`
  - `static/js/tasks.js:257` → `/api/email/accounts`

## `POST /api/email/accounts/test`
- handler: `test_account_config` — `routes/email_routes.py:5781`
- **JS callers:**
  - `static/js/settings.js:4700` → `/api/email/accounts/test`

## `DELETE /api/email/accounts/{account_id}`
- handler: `delete_email_account` — `routes/email_routes.py:5742`
- **JS callers:**
  - `static/js/settings.js:2799` → `/api/email/accounts/${id}`
  - `static/js/settings.js:3651` → `/api/email/accounts/${id}`
  - `static/js/settings.js:4700` → `/api/email/accounts/test`

## `PUT /api/email/accounts/{account_id}`
- handler: `update_email_account` — `routes/email_routes.py:5704`
- **JS callers:**
  - `static/js/settings.js:2799` → `/api/email/accounts/${id}`
  - `static/js/settings.js:3651` → `/api/email/accounts/${id}`
  - `static/js/settings.js:4700` → `/api/email/accounts/test`

## `POST /api/email/accounts/{account_id}/set-default`
- handler: `set_default_account` — `routes/email_routes.py:5987`
- **JS callers:**
  - `static/js/settings.js:2789` → `/api/email/accounts/${id}/set-default`

## `POST /api/email/ai-reply`
- handler: `ai_reply` — `routes/email_routes.py:5148`
- **JS callers:**
  - `static/js/document.js:4264` → `/api/email/ai-reply`
  - `static/js/emailInbox.js:842` → `/api/email/ai-reply`

## `POST /api/email/archive/{uid}`
- handler: `archive_email` — `routes/email_routes.py:3782`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/attachment-as-doc/{uid}/{index}`
- handler: `attachment_as_doc` — `routes/email_routes.py:3432`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/attachment-path/{uid}/{index}`
- handler: `get_attachment_path` — `routes/email_routes.py:3711`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/attachment/{uid}/{index}`
- handler: `download_attachment` — `routes/email_routes.py:3301`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/attachments-download/{uid}`
- handler: `download_all_attachments` — `routes/email_routes.py:3328`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/attachments/{uid}`
- handler: `list_attachments` — `routes/email_routes.py:3280`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/clear-answered/{uid}`
- handler: `clear_answered` — `routes/email_routes.py:4005`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/compose-from-attachment/{uid}/{index}`
- handler: `compose_from_attachment` — `routes/email_routes.py:4192`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/compose-from-odysseus`
- handler: `compose_from_odysseus` — `routes/email_routes.py:4116`
- **JS callers:**
  - `static/js/document.js:3248` → `/api/email/compose-from-odysseus`

## `POST /api/email/compose-from-odysseus-zip`
- handler: `compose_from_odysseus_zip` — `routes/email_routes.py:4140`
- **JS callers:**
  - `static/js/document.js:3269` → `/api/email/compose-from-odysseus-zip`

## `POST /api/email/compose-upload`
- handler: `compose_upload` — `routes/email_routes.py:4020`
- **JS callers:**
  - `static/js/document.js:3136` → `/api/email/compose-upload`

## `DELETE /api/email/compose-upload/{token}`
- handler: `delete_compose_upload` — `routes/email_routes.py:4232`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/config`
- handler: `get_email_config` — `routes/email_routes.py:5467`
- **JS callers:**
  - `static/js/emailLibrary.js:86` → `/api/email/config`
  - `static/js/emailLibrary.js:332` → `/api/email/config`
  - `static/js/emailLibrary.js:8392` → `/api/email/config`
  - `static/js/settings.js:2309` → `/api/email/config`
  - `static/js/settings.js:3052` → `/api/email/config`
  - `static/js/settings.js:3092` → `/api/email/config`

## `PUT /api/email/config`
- handler: `update_email_config` — `routes/email_routes.py:5510`
- **JS callers:**
  - `static/js/emailLibrary.js:86` → `/api/email/config`
  - `static/js/emailLibrary.js:332` → `/api/email/config`
  - `static/js/emailLibrary.js:8392` → `/api/email/config`
  - `static/js/settings.js:2309` → `/api/email/config`
  - `static/js/settings.js:3052` → `/api/email/config`
  - `static/js/settings.js:3092` → `/api/email/config`

## `GET /api/email/contacts`
- handler: `list_contacts` — `routes/email_routes.py:2725`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/email/delete-permanent/{uid}`
- handler: `delete_email_permanent` — `routes/email_routes.py:3812`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/email/delete/{uid}`
- handler: `delete_email` — `routes/email_routes.py:3797`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/draft`
- handler: `save_draft` — `routes/email_routes.py:4723`
- **JS callers:**
  - `static/js/document.js:4025` → `/api/email/draft`

## `POST /api/email/extract-style`
- handler: `extract_writing_style` — `routes/email_routes.py:4775`
- **JS callers:**
  - `static/js/emailLibrary.js:407` → `/api/email/extract-style`
  - `static/js/settings.js:3157` → `/api/email/extract-style`

## `POST /api/email/flag/{uid}`
- handler: `flag_email` — `routes/email_routes.py:3748`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/folders`
- handler: `list_folders` — `routes/email_routes.py:3918`
- **JS callers:**
  - `static/js/emailInbox.js:441` → `/api/email/folders`
  - `static/js/emailLibrary.js:3472` → `/api/email/folders`

## `GET /api/email/inline-image/{uid}`
- handler: `inline_image` — `routes/email_routes.py:3381`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/list`
- handler: `list_emails` — `routes/email_routes.py:2327`
- **JS callers:**
  - `static/js/emailInbox.js:415` → `/api/email/list?folder=`
  - `static/js/emailInbox.js:422` → `/api/email/list?folder=`
  - `static/js/emailLibrary.js:2358` → `/api/email/list`
  - `static/js/emailLibrary.js:2402` → `/api/email/list`
  - `static/js/emailLibrary.js:4340` → `/api/email/list?`
  - `static/js/emailLibrary.js:4662` → `/api/email/list?folder=`
  - `static/js/emailLibrary.js:4773` → `/api/email/list?folder=`
  - `static/js/emailLibrary.js:4800` → `/api/email/list?folder=`

## `POST /api/email/mark-answered/{uid}`
- handler: `mark_answered` — `routes/email_routes.py:3989`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/mark-read/{uid}`
- handler: `mark_read` — `routes/email_routes.py:3765`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/mark-unread/{uid}`
- handler: `mark_unread` — `routes/email_routes.py:3733`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/move/{uid}`
- handler: `move_email` — `routes/email_routes.py:3903`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/oauth/google/authorize`
- handler: `google_oauth_authorize` — `routes/email_routes.py:6010`
- **JS callers:**
  - `static/js/settings.js:2944` → `/api/email/oauth/google/authorize?account_id=`
  - `static/js/settings.js:4582` → `/api/email/oauth/google/authorize?account_id=`

## `GET /api/email/oauth/google/callback`
- handler: `google_oauth_callback` — `routes/email_routes.py:6034`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/email/odysseus/reminders`
- handler: `delete_odysseus_reminder_emails` — `routes/email_routes.py:3828`
- **JS callers:**
  - `static/js/emailLibrary.js:2839` → `/api/email/odysseus/reminders?permanent=1`

## `GET /api/email/pending`
- handler: `list_pending_agent_drafts` — `routes/email_routes.py:4407`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/email/pending/{sid}`
- handler: `cancel_agent_draft` — `routes/email_routes.py:4450`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/pending/{sid}/approve`
- handler: `approve_agent_draft` — `routes/email_routes.py:4426`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/read/{uid}`
- handler: `read_email_by_uid` — `routes/email_routes.py:3176`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/resolve-contact`
- handler: `resolve_contact` — `routes/email_routes.py:4471`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/email/schedule`
- handler: `schedule_email` — `routes/email_routes.py:4294`
- **JS callers:**
  - `static/js/document.js:4426` → `/api/email/schedule`

## `GET /api/email/scheduled`
- handler: `list_scheduled` — `routes/email_routes.py:4360`
- **JS callers:**
  - `static/js/emailLibrary.js:4830` → `/api/email/scheduled`

## `DELETE /api/email/scheduled/{sid}`
- handler: `cancel_scheduled` — `routes/email_routes.py:4383`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/email/search`
- handler: `search_emails` — `routes/email_routes.py:2773`
- **JS callers:**
  - `static/js/emailLibrary.js:4330` → `/api/email/search?`

## `POST /api/email/send`
- handler: `send_email` — `routes/email_routes.py:4519`
- **JS callers:**
  - `static/js/document.js:3909` → `/api/email/send`

## `GET /api/email/style`
- handler: `get_writing_style` — `routes/email_routes.py:5442`
- **JS callers:**
  - `static/js/emailLibrary.js:94` → `/api/email/style`
  - `static/js/emailLibrary.js:368` → `/api/email/style`
  - `static/js/settings.js:3041` → `/api/email/style`
  - `static/js/settings.js:3185` → `/api/email/style`

## `PUT /api/email/style`
- handler: `update_writing_style` — `routes/email_routes.py:5453`
- **JS callers:**
  - `static/js/emailLibrary.js:94` → `/api/email/style`
  - `static/js/emailLibrary.js:368` → `/api/email/style`
  - `static/js/settings.js:3041` → `/api/email/style`
  - `static/js/settings.js:3185` → `/api/email/style`

## `POST /api/email/summarize`
- handler: `summarize_email` — `routes/email_routes.py:4884`
- **JS callers:**
  - `static/js/emailLibrary.js:7503` → `/api/email/summarize`

## `POST /api/email/translate`
- handler: `translate_email` — `routes/email_routes.py:5001`
- **JS callers:**
  - `static/js/emailLibrary.js:7587` → `/api/email/translate`

## `GET /api/email/unread-state`
- handler: `unread_state` — `routes/email_routes.py:2410`
- **JS callers:**
  - `static/js/emailInbox.js:324` → `/api/email/unread-state`
  - `static/js/emailInbox.js:371` → `/api/email/unread-state`
  - `static/js/emailLibrary.js:3316` → `/api/email/unread-state`
  - `static/js/emailLibrary.js:4644` → `/api/email/unread-state`

## `POST /api/email/unsubscribe/cleanup`
- handler: `cleanup_unsubscribe_candidates` — `routes/email_routes.py:2678`
- **JS callers:**
  - `static/js/emailLibrary.js:1479` → `/api/email/unsubscribe/cleanup`

## `POST /api/email/unsubscribe/execute`
- handler: `execute_unsubscribe` — `routes/email_routes.py:2605`
- **JS callers:**
  - `static/js/emailLibrary.js:1686` → `/api/email/unsubscribe/execute`
  - `static/js/emailLibrary.js:1744` → `/api/email/unsubscribe/execute`

## `GET /api/email/unsubscribe/scan`
- handler: `scan_unsubscribe_candidates` — `routes/email_routes.py:2586`
- **JS callers:**
  - `static/js/emailLibrary.js:1620` → `/api/email/unsubscribe/scan`

## `GET /api/email/urgency-state`
- handler: `get_email_urgency_state` — `routes/email_routes.py:5583`
- **JS callers:**
  - `static/js/emailInbox.js:325` → `/api/email/urgency-state`

## `POST /api/email/{uid}/unflag-spam`
- handler: `unflag_spam` — `routes/email_routes.py:2484`
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
  - `static/js/admin.js:2840` → `/api/export`

## `GET /api/fonts/custom`
- handler: `list_custom_fonts` — `routes/font_routes.py:37`
- **JS callers:**
  - `static/js/theme.js:1275` → `/api/fonts/custom`

## `POST /api/gallery/ai-tag-batch`
- handler: `ai_tag_batch` — `routes/gallery/gallery_routes.py:898`
- **JS callers:**
  - `static/js/gallery.js:2374` → `/api/gallery/ai-tag-batch?`

## `POST /api/gallery/ai-upscale`
- handler: `gallery_ai_upscale` — `routes/gallery/gallery_routes.py:561`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/gallery/albums`
- handler: `list_albums` — `routes/gallery/gallery_routes.py:813`
- **JS callers:**
  - `static/js/gallery.js:182` → `/api/gallery/albums`
  - `static/js/gallery.js:349` → `/api/gallery/albums`
  - `static/js/gallery.js:798` → `/api/gallery/albums`
  - `static/js/gallery.js:833` → `/api/gallery/albums`

## `POST /api/gallery/albums`
- handler: `create_album` — `routes/gallery/gallery_routes.py:851`
- **JS callers:**
  - `static/js/gallery.js:182` → `/api/gallery/albums`
  - `static/js/gallery.js:349` → `/api/gallery/albums`
  - `static/js/gallery.js:798` → `/api/gallery/albums`
  - `static/js/gallery.js:833` → `/api/gallery/albums`

## `DELETE /api/gallery/albums/{album_id}`
- handler: `delete_album` — `routes/gallery/gallery_routes.py:2162`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PUT /api/gallery/albums/{album_id}`
- handler: `update_album` — `routes/gallery/gallery_routes.py:2141`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/albums/{album_id}/add`
- handler: `add_to_album` — `routes/gallery/gallery_routes.py:2178`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/albums/{album_id}/remove`
- handler: `remove_from_album` — `routes/gallery/gallery_routes.py:2196`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/clear-ai-tags`
- handler: `clear_gallery_ai_tags` — `routes/gallery/gallery_routes.py:1074`
- **JS callers:**
  - `static/js/gallery.js:1661` → `/api/gallery/clear-ai-tags?image_id=`
  - `static/js/gallery.js:2464` → `/api/gallery/clear-ai-tags`

## `POST /api/gallery/clear-user-tags`
- handler: `clear_gallery_user_tags` — `routes/gallery/gallery_routes.py:1049`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/dedupe-tags`
- handler: `dedupe_gallery_tags` — `routes/gallery/gallery_routes.py:1101`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/download-zip`
- handler: `gallery_download_zip` — `routes/gallery/gallery_routes.py:994`
- **JS callers:**
  - `static/js/gallery.js:2714` → `/api/gallery/download-zip`

## `GET /api/gallery/library`
- handler: `gallery_library` — `routes/gallery/gallery_routes.py:674`
- **JS callers:**
  - `static/js/document.js:3373` → `/api/gallery/library?`
  - `static/js/editor/wire-import.js:108` → `/api/gallery/library?limit=50`
  - `static/js/gallery.js:152` → `/api/gallery/library?`

## `GET /api/gallery/stats`
- handler: `gallery_stats` — `routes/gallery/gallery_routes.py:872`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/style-transfer`
- handler: `gallery_style_transfer` — `routes/gallery/gallery_routes.py:605`
- **JS callers:**
  - `static/js/editor/ai-tools-misc.js:176` → `/api/gallery/style-transfer`

## `GET /api/gallery/tags`
- handler: `gallery_tags` — `routes/gallery/gallery_routes.py:652`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/upload`
- handler: `gallery_upload` — `routes/gallery/gallery_routes.py:353`
- **JS callers:**
  - `static/js/gallery.js:263` → `/api/gallery/upload`
  - `static/js/galleryEditor.js:3691` → `/api/gallery/upload`

## `DELETE /api/gallery/{image_id}`
- handler: `delete_gallery_image` — `routes/gallery/gallery_routes.py:1137`
- **JS callers:**
  - `static/js/chatRenderer.js:1617` → `/api/gallery/${encodeURIComponent(imageId)}`
  - `static/js/document.js:3373` → `/api/gallery/library?`
  - `static/js/editor/ai-tools-misc.js:176` → `/api/gallery/style-transfer`
  - `static/js/editor/wire-import.js:108` → `/api/gallery/library?limit=50`
  - `static/js/gallery.js:152` → `/api/gallery/library?`
  - `static/js/gallery.js:182` → `/api/gallery/albums`
  - `static/js/gallery.js:263` → `/api/gallery/upload`
  - `static/js/gallery.js:349` → `/api/gallery/albums`
  - `static/js/gallery.js:798` → `/api/gallery/albums`
  - `static/js/gallery.js:833` → `/api/gallery/albums`
  - `static/js/gallery.js:1661` → `/api/gallery/clear-ai-tags?image_id=`
  - `static/js/gallery.js:2374` → `/api/gallery/ai-tag-batch?`
  - `static/js/gallery.js:2464` → `/api/gallery/clear-ai-tags`
  - `static/js/gallery.js:2714` → `/api/gallery/download-zip`
  - `static/js/galleryEditor.js:3691` → `/api/gallery/upload`

## `GET /api/gallery/{image_id}`
- handler: `get_gallery_image` — `routes/gallery/gallery_routes.py:921`
- **JS callers:**
  - `static/js/chatRenderer.js:1617` → `/api/gallery/${encodeURIComponent(imageId)}`
  - `static/js/document.js:3373` → `/api/gallery/library?`
  - `static/js/editor/ai-tools-misc.js:176` → `/api/gallery/style-transfer`
  - `static/js/editor/wire-import.js:108` → `/api/gallery/library?limit=50`
  - `static/js/gallery.js:152` → `/api/gallery/library?`
  - `static/js/gallery.js:182` → `/api/gallery/albums`
  - `static/js/gallery.js:263` → `/api/gallery/upload`
  - `static/js/gallery.js:349` → `/api/gallery/albums`
  - `static/js/gallery.js:798` → `/api/gallery/albums`
  - `static/js/gallery.js:833` → `/api/gallery/albums`
  - `static/js/gallery.js:1661` → `/api/gallery/clear-ai-tags?image_id=`
  - `static/js/gallery.js:2374` → `/api/gallery/ai-tag-batch?`
  - `static/js/gallery.js:2464` → `/api/gallery/clear-ai-tags`
  - `static/js/gallery.js:2714` → `/api/gallery/download-zip`
  - `static/js/galleryEditor.js:3691` → `/api/gallery/upload`

## `PATCH /api/gallery/{image_id}`
- handler: `patch_gallery_image` — `routes/gallery/gallery_routes.py:942`
- **JS callers:**
  - `static/js/chatRenderer.js:1617` → `/api/gallery/${encodeURIComponent(imageId)}`
  - `static/js/document.js:3373` → `/api/gallery/library?`
  - `static/js/editor/ai-tools-misc.js:176` → `/api/gallery/style-transfer`
  - `static/js/editor/wire-import.js:108` → `/api/gallery/library?limit=50`
  - `static/js/gallery.js:152` → `/api/gallery/library?`
  - `static/js/gallery.js:182` → `/api/gallery/albums`
  - `static/js/gallery.js:263` → `/api/gallery/upload`
  - `static/js/gallery.js:349` → `/api/gallery/albums`
  - `static/js/gallery.js:798` → `/api/gallery/albums`
  - `static/js/gallery.js:833` → `/api/gallery/albums`
  - `static/js/gallery.js:1661` → `/api/gallery/clear-ai-tags?image_id=`
  - `static/js/gallery.js:2374` → `/api/gallery/ai-tag-batch?`
  - `static/js/gallery.js:2464` → `/api/gallery/clear-ai-tags`
  - `static/js/gallery.js:2714` → `/api/gallery/download-zip`
  - `static/js/galleryEditor.js:3691` → `/api/gallery/upload`

## `POST /api/gallery/{image_id}/ai-tag`
- handler: `ai_tag_image` — `routes/gallery/gallery_routes.py:2231`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/{image_id}/favorite`
- handler: `toggle_favorite` — `routes/gallery/gallery_routes.py:2217`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/{image_id}/rename`
- handler: `gallery_rename` — `routes/gallery/gallery_routes.py:478`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/{image_id}/replace`
- handler: `gallery_replace` — `routes/gallery/gallery_routes.py:435`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/gallery/{image_id}/rotate`
- handler: `gallery_rotate` — `routes/gallery/gallery_routes.py:504`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/generated-image/{filename}`
- handler: `serve_generated_image` — `app.py:513`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/health`
- handler: `health_check` — `app.py:956`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/history/{session_id}`
- handler: `get_session_history` — `routes/history/history_routes.py:269`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/hwfit/image-models`
- handler: `get_image_models` — `routes/hwfit_routes.py:413`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:838` → `/api/hwfit/image-models?`

## `GET /api/hwfit/models`
- handler: `get_models` — `routes/hwfit_routes.py:194`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:838` → `/api/hwfit/models?`
  - `static/js/cookbook-hwfit.js:860` → `/api/hwfit/models?${fallbackParams}`
  - `static/js/cookbook-hwfit.js:860` → `/api/hwfit/models?`

## `GET /api/hwfit/profiles`
- handler: `get_serve_profiles` — `routes/hwfit_routes.py:319`
- **JS callers:**
  - `static/js/cookbookServe.js:1993` → `/api/hwfit/profiles?${params}`
  - `static/js/cookbookServe.js:1993` → `/api/hwfit/profiles?`

## `GET /api/hwfit/system`
- handler: `get_system` — `routes/hwfit_routes.py:186`
- **JS callers:**
  - `static/js/cookbook.js:2657` → `/api/hwfit/system?${qp}`
  - `static/js/cookbook.js:2657` → `/api/hwfit/system?`

## `POST /api/image/denoise`
- handler: `denoise_image` — `routes/gallery/gallery_routes.py:1741`
- **JS callers:**
  - `static/js/galleryEditor.js:538` → `/api/image/denoise`

## `POST /api/image/enhance-face`
- handler: `enhance_face` — `routes/gallery/gallery_routes.py:2057`
- **JS callers:**
  - `static/js/galleryEditor.js:544` → `/api/image/enhance-face`

## `POST /api/image/harmonize`
- handler: `harmonize_image` — `routes/gallery/gallery_routes.py:1516`
- **JS callers:**
  - `static/js/editor/ai-tools-misc.js:72` → `/api/image/harmonize`

## `POST /api/image/inpaint`
- handler: `inpaint_proxy` — `routes/gallery/gallery_routes.py:1258`
- **JS callers:**
  - `static/js/editor/ai-inpaint.js:143` → `/api/image/inpaint`

## `POST /api/image/mask`
- handler: `smart_mask` — `routes/gallery/gallery_routes.py:1838`
- **JS callers:**
  - `static/js/galleryEditor.js:1997` → `/api/image/mask`

## `POST /api/image/remove-bg`
- handler: `remove_background` — `routes/gallery/gallery_routes.py:1964`
- **JS callers:**
  - `static/js/editor/ai-rembg.js:71` → `/api/image/remove-bg`
  - `static/js/editor/wire-selection-controls.js:163` → `/api/image/remove-bg`

## `POST /api/image/sharpen`
- handler: `sharpen_image` — `routes/gallery/gallery_routes.py:1716`
- **JS callers:**
  - `static/js/editor/ai-rembg.js:53` → `/api/image/sharpen`

## `POST /api/image/upscale-local`
- handler: `upscale_image_local` — `routes/gallery/gallery_routes.py:1792`
- **JS callers:**
  - `static/js/editor/ai-tools-misc.js:120` → `/api/image/upscale-local`

## `POST /api/import`
- handler: `import_data` — `routes/backup_routes.py:64`
- **JS callers:**
  - `static/js/admin.js:2872` → `/api/import`

## `POST /api/inject_context/{session_id}`
- handler: `inject_context` — `routes/chat_routes.py:3124`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/mcp/oauth/authorize/{server_id}`
- handler: `oauth_authorize` — `routes/mcp/mcp_routes.py:429`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/mcp/oauth/callback`
- handler: `oauth_callback` — `routes/mcp/mcp_routes.py:483`
- **JS callers:**
  - `static/js/settings.js:4931` → `/api/mcp/oauth/callback?code=...`

## `POST /api/mcp/oauth/exchange/{server_id}`
- handler: `oauth_exchange` — `routes/mcp/mcp_routes.py:498`
- **JS callers:**
  - `static/js/settings.js:4940` → `/api/mcp/oauth/exchange/${id}`

## `GET /api/mcp/servers`
- handler: `list_servers` — `routes/mcp/mcp_routes.py:121`
- **JS callers:**
  - `static/js/admin.js:2070` → `/api/mcp/servers`
  - `static/js/admin.js:2387` → `/api/mcp/servers`
  - `static/js/settings.js:3517` → `/api/mcp/servers`
  - `static/js/settings.js:4958` → `/api/mcp/servers`
  - `static/js/settings.js:4984` → `/api/mcp/servers`
  - `static/js/settings.js:5101` → `/api/mcp/servers`
  - `static/js/slashCommands.js:1550` → `/api/mcp/servers`

## `POST /api/mcp/servers`
- handler: `add_server` — `routes/mcp/mcp_routes.py:159`
- **JS callers:**
  - `static/js/admin.js:2070` → `/api/mcp/servers`
  - `static/js/admin.js:2387` → `/api/mcp/servers`
  - `static/js/settings.js:3517` → `/api/mcp/servers`
  - `static/js/settings.js:4958` → `/api/mcp/servers`
  - `static/js/settings.js:4984` → `/api/mcp/servers`
  - `static/js/settings.js:5101` → `/api/mcp/servers`
  - `static/js/slashCommands.js:1550` → `/api/mcp/servers`

## `DELETE /api/mcp/servers/{server_id}`
- handler: `delete_server` — `routes/mcp/mcp_routes.py:357`
- **JS callers:**
  - `static/js/admin.js:2111` → `/api/mcp/servers/${btn.dataset.admMcpToggle}`
  - `static/js/admin.js:2118` → `/api/mcp/servers/${btn.dataset.admMcpDelete}`
  - `static/js/settings.js:3652` → `/api/mcp/servers/${id}`
  - `static/js/settings.js:5022` → `/api/mcp/servers/${srv.id}`

## `PATCH /api/mcp/servers/{server_id}`
- handler: `toggle_server` — `routes/mcp/mcp_routes.py:324`
- **JS callers:**
  - `static/js/admin.js:2111` → `/api/mcp/servers/${btn.dataset.admMcpToggle}`
  - `static/js/admin.js:2118` → `/api/mcp/servers/${btn.dataset.admMcpDelete}`
  - `static/js/settings.js:3652` → `/api/mcp/servers/${id}`
  - `static/js/settings.js:5022` → `/api/mcp/servers/${srv.id}`

## `POST /api/mcp/servers/{server_id}/reconnect`
- handler: `reconnect_server` — `routes/mcp/mcp_routes.py:288`
- **JS callers:**
  - `static/js/admin.js:2100` → `/api/mcp/servers/${btn.dataset.admMcpReconnect}/reconnect`
  - `static/js/settings.js:5012` → `/api/mcp/servers/${srv.id}/reconnect`

## `GET /api/mcp/servers/{server_id}/tools`
- handler: `list_server_tools` — `routes/mcp/mcp_routes.py:382`
- **JS callers:**
  - `static/js/admin.js:2144` → `/api/mcp/servers/${sid}/tools`
  - `static/js/admin.js:2188` → `/api/mcp/servers/${serverId}/tools`
  - `static/js/settings.js:5031` → `/api/mcp/servers/${srv.id}/tools`
  - `static/js/settings.js:5039` → `/api/mcp/servers/${srv.id}/tools`

## `PATCH /api/mcp/servers/{server_id}/tools`
- handler: `update_disabled_tools` — `routes/mcp/mcp_routes.py:402`
- **JS callers:**
  - `static/js/admin.js:2144` → `/api/mcp/servers/${sid}/tools`
  - `static/js/admin.js:2188` → `/api/mcp/servers/${serverId}/tools`
  - `static/js/settings.js:5031` → `/api/mcp/servers/${srv.id}/tools`
  - `static/js/settings.js:5039` → `/api/mcp/servers/${srv.id}/tools`

## `GET /api/mcp/tools`
- handler: `list_tools` — `routes/mcp/mcp_routes.py:375`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/memory/add`
- handler: `api_add_memory` — `routes/memory/memory_routes.py:101`
- **JS callers:**
  - `static/js/memory.js:1117` → `/api/memory/add`
  - `static/js/memory.js:1246` → `/api/memory/add`
  - `static/js/memory.js:1374` → `/api/memory/add`
  - `static/js/memory.js:1416` → `/api/memory/add`
  - `static/js/presets.js:979` → `/api/memory/add`
  - `static/js/slashCommands.js:1586` → `/api/memory/add`

## `POST /api/memory/audit`
- handler: `api_audit_memories` — `routes/memory/memory_routes.py:289`
- **JS callers:**
  - `static/js/memory.js:525` → `/api/memory/audit`

## `GET /api/memory/by-session/{session_id}`
- handler: `get_memory_by_session` — `routes/memory/memory_routes.py:209`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/memory/debug`
- handler: `debug_memory_relevance` — `routes/memory/memory_routes.py:86`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/memory/extract`
- handler: `extract_memory` — `routes/memory/memory_routes.py:239`
- **JS callers:**
  - `static/js/memory.js:1195` → `/api/memory/extract`

## `POST /api/memory/import`
- handler: `import_memories_from_file` — `routes/memory/memory_routes.py:340`
- **JS callers:**
  - `static/js/memory.js:1314` → `/api/memory/import`

## `POST /api/memory/search`
- handler: `search_memories` — `routes/memory/memory_routes.py:155`
- **JS callers:**
  - `static/js/slashCommands.js:1639` → `/api/memory/search`

## `GET /api/memory/timeline`
- handler: `memory_timeline` — `routes/memory/memory_routes.py:171`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/memory/{memory_id}`
- handler: `delete_memory` — `routes/memory/memory_routes.py:550`
- **JS callers:**
  - `static/js/memory.js:525` → `/api/memory/audit`
  - `static/js/memory.js:1117` → `/api/memory/add`
  - `static/js/memory.js:1195` → `/api/memory/extract`
  - `static/js/memory.js:1246` → `/api/memory/add`
  - `static/js/memory.js:1314` → `/api/memory/import`
  - `static/js/memory.js:1374` → `/api/memory/add`
  - `static/js/memory.js:1416` → `/api/memory/add`
  - `static/js/presets.js:979` → `/api/memory/add`
  - `static/js/slashCommands.js:1586` → `/api/memory/add`
  - `static/js/slashCommands.js:1639` → `/api/memory/search`

## `GET /api/memory/{memory_id}`
- handler: `get_memory_item` — `routes/memory/memory_routes.py:517`
- **JS callers:**
  - `static/js/memory.js:525` → `/api/memory/audit`
  - `static/js/memory.js:1117` → `/api/memory/add`
  - `static/js/memory.js:1195` → `/api/memory/extract`
  - `static/js/memory.js:1246` → `/api/memory/add`
  - `static/js/memory.js:1314` → `/api/memory/import`
  - `static/js/memory.js:1374` → `/api/memory/add`
  - `static/js/memory.js:1416` → `/api/memory/add`
  - `static/js/presets.js:979` → `/api/memory/add`
  - `static/js/slashCommands.js:1586` → `/api/memory/add`
  - `static/js/slashCommands.js:1639` → `/api/memory/search`

## `PUT /api/memory/{memory_id}`
- handler: `update_memory` — `routes/memory/memory_routes.py:528`
- **JS callers:**
  - `static/js/memory.js:525` → `/api/memory/audit`
  - `static/js/memory.js:1117` → `/api/memory/add`
  - `static/js/memory.js:1195` → `/api/memory/extract`
  - `static/js/memory.js:1246` → `/api/memory/add`
  - `static/js/memory.js:1314` → `/api/memory/import`
  - `static/js/memory.js:1374` → `/api/memory/add`
  - `static/js/memory.js:1416` → `/api/memory/add`
  - `static/js/presets.js:979` → `/api/memory/add`
  - `static/js/slashCommands.js:1586` → `/api/memory/add`
  - `static/js/slashCommands.js:1639` → `/api/memory/search`

## `POST /api/memory/{memory_id}/pin`
- handler: `pin_memory` — `routes/memory/memory_routes.py:503`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/model-endpoints`
- handler: `list_model_endpoints` — `routes/model_routes.py:1933`
- **JS callers:**
  - `static/js/admin.js:255` → `/api/model-endpoints`
  - `static/js/admin.js:489` → `/api/model-endpoints`
  - `static/js/admin.js:1124` → `/api/model-endpoints`
  - `static/js/admin.js:1442` → `/api/model-endpoints`
  - `static/js/admin.js:1630` → `/api/model-endpoints`
  - `static/js/admin.js:1723` → `/api/model-endpoints`
  - `static/js/assistant.js:134` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:532` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:2657` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:2676` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:2964` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3630` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3663` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3842` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:4094` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:4297` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:4323` → `/api/model-endpoints`
  - `static/js/editor/ai-models.js:97` → `/api/model-endpoints`
  - `static/js/markdown.js:1453` → `/api/model-endpoints`
  - `static/js/markdown.js:1480` → `/api/model-endpoints`
  - … +6 more

## `POST /api/model-endpoints`
- handler: `create_model_endpoint` — `routes/model_routes.py:1990`
- **JS callers:**
  - `static/js/admin.js:255` → `/api/model-endpoints`
  - `static/js/admin.js:489` → `/api/model-endpoints`
  - `static/js/admin.js:1124` → `/api/model-endpoints`
  - `static/js/admin.js:1442` → `/api/model-endpoints`
  - `static/js/admin.js:1630` → `/api/model-endpoints`
  - `static/js/admin.js:1723` → `/api/model-endpoints`
  - `static/js/assistant.js:134` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:532` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:2657` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:2676` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:2964` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3630` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3663` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:3842` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:4094` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:4297` → `/api/model-endpoints`
  - `static/js/cookbookRunning.js:4323` → `/api/model-endpoints`
  - `static/js/editor/ai-models.js:97` → `/api/model-endpoints`
  - `static/js/markdown.js:1453` → `/api/model-endpoints`
  - `static/js/markdown.js:1480` → `/api/model-endpoints`
  - … +6 more

## `GET /api/model-endpoints/probe-local`
- handler: `probe_local_endpoints` — `routes/model_routes.py:1677`
- **JS callers:**
  - `static/js/admin.js:1472` → `/api/model-endpoints/probe-local`
  - `static/js/chat.js:1153` → `/api/model-endpoints/probe-local`
  - `static/js/cookbookRunning.js:3843` → `/api/model-endpoints/probe-local`
  - `static/js/modelPicker.js:270` → `/api/model-endpoints/probe-local`

## `POST /api/model-endpoints/test`
- handler: `test_model_endpoint` — `routes/model_routes.py:2227`
- **JS callers:**
  - `static/js/admin.js:1063` → `/api/model-endpoints/test`
  - `static/js/admin.js:1598` → `/api/model-endpoints/test`

## `DELETE /api/model-endpoints/{ep_id}`
- handler: `delete_model_endpoint` — `routes/model_routes.py:2665`
- **JS callers:**
  - `static/js/admin.js:583` → `/api/model-endpoints/${btn.dataset.admToggleEp}`
  - `static/js/admin.js:1063` → `/api/model-endpoints/test`
  - `static/js/admin.js:1472` → `/api/model-endpoints/probe-local`
  - `static/js/admin.js:1598` → `/api/model-endpoints/test`
  - `static/js/chat.js:1153` → `/api/model-endpoints/probe-local`
  - `static/js/cookbookRunning.js:539` → `/api/model-endpoints/${ep.id}`
  - `static/js/cookbookRunning.js:2968` → `/api/model-endpoints/${ep.id}`
  - `static/js/cookbookRunning.js:3843` → `/api/model-endpoints/probe-local`
  - `static/js/modelPicker.js:270` → `/api/model-endpoints/probe-local`

## `PATCH /api/model-endpoints/{ep_id}`
- handler: `toggle_model_endpoint` — `routes/model_routes.py:2498`
- **JS callers:**
  - `static/js/admin.js:583` → `/api/model-endpoints/${btn.dataset.admToggleEp}`
  - `static/js/admin.js:1063` → `/api/model-endpoints/test`
  - `static/js/admin.js:1472` → `/api/model-endpoints/probe-local`
  - `static/js/admin.js:1598` → `/api/model-endpoints/test`
  - `static/js/chat.js:1153` → `/api/model-endpoints/probe-local`
  - `static/js/cookbookRunning.js:539` → `/api/model-endpoints/${ep.id}`
  - `static/js/cookbookRunning.js:2968` → `/api/model-endpoints/${ep.id}`
  - `static/js/cookbookRunning.js:3843` → `/api/model-endpoints/probe-local`
  - `static/js/modelPicker.js:270` → `/api/model-endpoints/probe-local`

## `GET /api/model-endpoints/{ep_id}/dependents`
- handler: `get_endpoint_dependents` — `routes/model_routes.py:2659`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/model-endpoints/{ep_id}/models`
- handler: `list_endpoint_models` — `routes/model_routes.py:2308`
- **JS callers:**
  - `static/js/admin.js:685` → `/api/model-endpoints/${epId}/models?refresh=true&refresh_timeout=60`
  - `static/js/admin.js:752` → `/api/model-endpoints/${epId}/models`
  - `static/js/admin.js:779` → `/api/model-endpoints/${epId}/models`

## `PATCH /api/model-endpoints/{ep_id}/models`
- handler: `update_hidden_models` — `routes/model_routes.py:2363`
- **JS callers:**
  - `static/js/admin.js:685` → `/api/model-endpoints/${epId}/models?refresh=true&refresh_timeout=60`
  - `static/js/admin.js:752` → `/api/model-endpoints/${epId}/models`
  - `static/js/admin.js:779` → `/api/model-endpoints/${epId}/models`

## `GET /api/model-endpoints/{ep_id}/probe`
- handler: `probe_endpoint_models` — `routes/model_routes.py:2258`
- **JS callers:**
  - `static/js/cookbookRunning.js:4091` → `/api/model-endpoints/${epId}/probe`

## `GET /api/model/cached`
- handler: `model_cached` — `routes/cookbook_routes.py:1406`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:765` → `/api/model/cached?${_cacheParams}`
  - `static/js/cookbook-hwfit.js:765` → `/api/model/cached?`
  - `static/js/cookbookServe.js:4202` → `/api/model/cached`

## `POST /api/model/download`
- handler: `model_download` — `routes/cookbook_routes.py:1065`
- **JS callers:**
  - `static/js/cookbookDownload.js:622` → `/api/model/download`
  - `static/js/cookbookRunning.js:699` → `/api/model/download`
  - `static/js/cookbookRunning.js:1495` → `/api/model/download`
  - `static/js/cookbookRunning.js:3407` → `/api/model/download`

## `POST /api/model/serve`
- handler: `model_serve` — `routes/cookbook_routes.py:1962`
- **JS callers:**
  - `static/js/cookbook-hwfit.js:1945` → `/api/model/serve`
  - `static/js/cookbook.js:1473` → `/api/model/serve`
  - `static/js/cookbook.js:1549` → `/api/model/serve`
  - `static/js/cookbook.js:1760` → `/api/model/serve`
  - `static/js/cookbookRunning.js:2005` → `/api/model/serve`

## `GET /api/models`
- handler: `api_models` — `routes/model_routes.py:1619`
- **JS callers:**
  - `static/app.js:3507` → `/api/models`
  - `static/js/chat.js:1145` → `/api/models`
  - `static/js/compare/models.js:57` → `/api/models`
  - `static/js/group.js:45` → `/api/models`
  - `static/js/group.js:458` → `/api/models`
  - `static/js/models.js:202` → `/api/models`
  - `static/js/settings.js:629` → `/api/models`
  - `static/js/settings.js:699` → `/api/models`
  - `static/js/slashCommands.js:267` → `/api/models`
  - `static/js/slashCommands.js:987` → `/api/models`
  - `static/js/slashCommands.js:1523` → `/api/models`
  - `static/js/tasks.js:1588` → `/api/models`

## `POST /api/notes/fire-reminder`
- handler: `fire_reminder` — `routes/note/note_routes.py:844`
- **JS callers:**
  - `static/js/calendar/reminders.js:77` → `/api/notes/fire-reminder`
  - `static/js/notes.js:1011` → `/api/notes/fire-reminder`
  - `static/js/settings.js:2657` → `/api/notes/fire-reminder`

## `POST /api/notes/reorder`
- handler: `reorder_notes` — `routes/note/note_routes.py:902`
- **JS callers:**
  - `static/js/notes.js:2698` → `/api/notes/reorder`
  - `static/js/notes.js:2792` → `/api/notes/reorder`
  - `static/js/notes.js:5282` → `/api/notes/reorder`

## `DELETE /api/notes/{note_id}`
- handler: `delete_note` — `routes/note/note_routes.py:761`
- **JS callers:**
  - `static/js/calendar/reminders.js:77` → `/api/notes/fire-reminder`
  - `static/js/notes.js:1011` → `/api/notes/fire-reminder`
  - `static/js/notes.js:2698` → `/api/notes/reorder`
  - `static/js/notes.js:2792` → `/api/notes/reorder`
  - `static/js/notes.js:5282` → `/api/notes/reorder`
  - `static/js/settings.js:2657` → `/api/notes/fire-reminder`

## `GET /api/notes/{note_id}`
- handler: `get_note` — `routes/note/note_routes.py:689`
- **JS callers:**
  - `static/js/calendar/reminders.js:77` → `/api/notes/fire-reminder`
  - `static/js/notes.js:1011` → `/api/notes/fire-reminder`
  - `static/js/notes.js:2698` → `/api/notes/reorder`
  - `static/js/notes.js:2792` → `/api/notes/reorder`
  - `static/js/notes.js:5282` → `/api/notes/reorder`
  - `static/js/settings.js:2657` → `/api/notes/fire-reminder`

## `PUT /api/notes/{note_id}`
- handler: `update_note` — `routes/note/note_routes.py:706`
- **JS callers:**
  - `static/js/calendar/reminders.js:77` → `/api/notes/fire-reminder`
  - `static/js/notes.js:1011` → `/api/notes/fire-reminder`
  - `static/js/notes.js:2698` → `/api/notes/reorder`
  - `static/js/notes.js:2792` → `/api/notes/reorder`
  - `static/js/notes.js:5282` → `/api/notes/reorder`
  - `static/js/settings.js:2657` → `/api/notes/fire-reminder`

## `POST /api/notes/{note_id}/archive`
- handler: `toggle_archive` — `routes/note/note_routes.py:799`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/notes/{note_id}/items/{index}/toggle`
- handler: `toggle_item` — `routes/note/note_routes.py:818`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/notes/{note_id}/pin`
- handler: `toggle_pin` — `routes/note/note_routes.py:780`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/personal/add_directory`
- handler: `add_directory_to_rag` — `routes/personal_routes.py:201`
- **JS callers:**
  - `static/js/admin.js:2491` → `/api/personal/add_directory`
  - `static/js/slashCommands.js:1910` → `/api/personal/add_directory`

## `DELETE /api/personal/file`
- handler: `delete_file_from_rag` — `routes/personal_routes.py:411`
- **JS callers:**
  - `static/js/admin.js:2443` → `/api/personal/file?filepath=`
  - `static/js/rag.js:93` → `/api/personal/file?filepath=`

## `POST /api/personal/reload`
- handler: `api_personal_reload` — `routes/personal_routes.py:192`
- **JS callers:**
  - `static/js/admin.js:2502` → `/api/personal/reload`

## `DELETE /api/personal/remove_directory`
- handler: `remove_directory_from_rag` — `routes/personal_routes.py:270`
- **JS callers:**
  - `static/js/admin.js:2423` → `/api/personal/remove_directory?directory=`
  - `static/js/slashCommands.js:1940` → `/api/personal/remove_directory?directory=`
  - `static/js/slashCommands.js:1949` → `/api/personal/remove_directory?directory=`

## `POST /api/personal/upload`
- handler: `upload_files_to_rag` — `routes/personal_routes.py:322`
- **JS callers:**
  - `static/js/admin.js:2470` → `/api/personal/upload`
  - `static/js/rag.js:120` → `/api/personal/upload`

## `GET /api/ping`
- handler: `ping_endpoints` — `routes/model_routes.py:1757`
- **JS callers:**
  - `static/js/slashCommands.js:5549` → `/api/ping`

## `GET /api/prefs/{key}`
- handler: `get_pref` — `routes/prefs_routes.py:112`
- **JS callers:**
  - `static/js/theme.js:122` → `/api/prefs/custom-themes`
  - `static/js/theme.js:636` → `/api/prefs/theme`
  - `static/js/theme.js:647` → `/api/prefs/theme`
  - `static/js/theme.js:2246` → `/api/prefs/custom-themes`

## `PUT /api/prefs/{key}`
- handler: `set_pref` — `routes/prefs_routes.py:118`
- **JS callers:**
  - `static/js/theme.js:122` → `/api/prefs/custom-themes`
  - `static/js/theme.js:636` → `/api/prefs/theme`
  - `static/js/theme.js:647` → `/api/prefs/theme`
  - `static/js/theme.js:2246` → `/api/prefs/custom-themes`

## `GET /api/presets`
- handler: `get_presets` — `routes/preset_routes.py:30`
- **JS callers:**
  - `static/js/assistant.js:281` → `/api/presets`
  - `static/js/presets.js:503` → `/api/presets`

## `POST /api/presets/custom`
- handler: `update_custom_preset` — `routes/preset_routes.py:34`
- **JS callers:**
  - `static/js/presets.js:676` → `/api/presets/custom`
  - `static/js/presets.js:794` → `/api/presets/custom`
  - `static/js/presets.js:1047` → `/api/presets/custom`

## `POST /api/presets/expand`
- handler: `expand_character_prompt` — `routes/preset_routes.py:74`
- **JS callers:**
  - `static/js/presets.js:136` → `/api/presets/expand`

## `GET /api/presets/groups`
- handler: `get_group_presets` — `routes/preset_routes.py:115`
- **JS callers:**
  - `static/js/group.js:183` → `/api/presets/groups`
  - `static/js/group.js:190` → `/api/presets/groups`
  - `static/js/group.js:267` → `/api/presets/groups`
  - `static/js/group.js:293` → `/api/presets/groups`
  - `static/js/group.js:321` → `/api/presets/groups`

## `POST /api/presets/groups`
- handler: `save_group_presets` — `routes/preset_routes.py:120`
- **JS callers:**
  - `static/js/group.js:183` → `/api/presets/groups`
  - `static/js/group.js:190` → `/api/presets/groups`
  - `static/js/group.js:267` → `/api/presets/groups`
  - `static/js/group.js:293` → `/api/presets/groups`
  - `static/js/group.js:321` → `/api/presets/groups`

## `GET /api/presets/templates`
- handler: `get_user_templates` — `routes/preset_routes.py:53`
- **JS callers:**
  - `static/js/assistant.js:282` → `/api/presets/templates`
  - `static/js/group.js:351` → `/api/presets/templates`
  - `static/js/presets.js:373` → `/api/presets/templates`
  - `static/js/presets.js:474` → `/api/presets/templates`
  - `static/js/presets.js:846` → `/api/presets/templates`

## `POST /api/presets/templates`
- handler: `save_user_template` — `routes/preset_routes.py:57`
- **JS callers:**
  - `static/js/assistant.js:282` → `/api/presets/templates`
  - `static/js/group.js:351` → `/api/presets/templates`
  - `static/js/presets.js:373` → `/api/presets/templates`
  - `static/js/presets.js:474` → `/api/presets/templates`
  - `static/js/presets.js:846` → `/api/presets/templates`

## `DELETE /api/presets/templates/{template_id}`
- handler: `delete_user_template` — `routes/preset_routes.py:67`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/probe`
- handler: `probe_models` — `routes/model_routes.py:1842`
- **JS callers:**
  - `static/js/slashCommands.js:5581` → `/api/probe`

## `POST /api/probe-selected`
- handler: `probe_selected` — `routes/model_routes.py:1797`
- **JS callers:**
  - `static/js/compare/probe.js:45` → `/api/probe-selected`
  - `static/js/compare/selector.js:1009` → `/api/probe-selected`

## `GET /api/providers`
- handler: `providers` — `routes/model_routes.py:1913`
- **JS callers:**
  - `static/js/models.js:607` → `/api/providers`

## `GET /api/rag/stats`
- handler: `get_rag_stats` — `routes/diagnostics_routes.py:67`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/ready`
- handler: `readiness_check` — `app.py:988`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/research/active`
- handler: `research_active` — `routes/research/research_routes.py:260`
- **JS callers:**
  - `static/js/research/jobs.js:62` → `/api/research/active`

## `POST /api/research/cancel/{session_id}`
- handler: `research_cancel` — `routes/research/research_routes.py:290`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/research/detail/{session_id}`
- handler: `research_detail` — `routes/research/research_routes.py:422`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/research/library`
- handler: `research_library` — `routes/research/research_routes.py:367`
- **JS callers:**
  - `static/js/documentLibrary.js:2331` → `/api/research/library?archived=true`
  - `static/js/documentLibrary.js:2691` → `/api/research/library`
  - `static/js/research/jobs.js:95` → `/api/research/library?sort=recent&limit=20`
  - `static/js/research/panel.js:190` → `/api/research/library?limit=1`
  - `static/js/sessions.js:3560` → `/api/research/library?`

## `GET /api/research/report/{session_id}`
- handler: `research_report` — `routes/research/research_routes.py:324`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/research/result-peek/{session_id}`
- handler: `research_result_peek` — `routes/research/research_routes.py:614`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/research/result/{session_id}`
- handler: `research_result` — `routes/research/research_routes.py:299`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/research/spinoff/{session_id}`
- handler: `research_spinoff` — `routes/research/research_routes.py:636`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/research/start`
- handler: `research_start` — `routes/research/research_routes.py:493`
- **JS callers:**
  - `static/js/research/jobs.js:276` → `/api/research/start`

## `GET /api/research/status/{session_id}`
- handler: `research_status` — `routes/research/research_routes.py:279`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/research/stream/{session_id}`
- handler: `research_stream` — `routes/research/research_routes.py:580`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/research/{session_id}`
- handler: `research_delete` — `routes/research/research_routes.py:456`
- **JS callers:**
  - `static/js/documentLibrary.js:2331` → `/api/research/library?archived=true`
  - `static/js/documentLibrary.js:2691` → `/api/research/library`
  - `static/js/research/jobs.js:62` → `/api/research/active`
  - `static/js/research/jobs.js:95` → `/api/research/library?sort=recent&limit=20`
  - `static/js/research/jobs.js:276` → `/api/research/start`
  - `static/js/research/panel.js:190` → `/api/research/library?limit=1`
  - `static/js/sessions.js:3560` → `/api/research/library?`

## `POST /api/research/{session_id}/archive`
- handler: `research_archive` — `routes/research/research_routes.py:438`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/research/{session_id}/hide-image`
- handler: `research_hide_image` — `routes/research/research_routes.py:344`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/research/{session_id}/unhide-images`
- handler: `research_unhide_images` — `routes/research/research_routes.py:356`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/rewrite`
- handler: `rewrite_message` — `routes/chat_routes.py:3209`
- **JS callers:**
  - `static/js/chat.js:7426` → `/api/rewrite`

## `GET /api/runtime`
- handler: `runtime_info` — `app.py:999`
- **JS callers:**
  - `static/js/admin.js:1005` → `/api/runtime`

## `GET /api/search`
- handler: `search_messages` — `routes/chat_routes.py:3139`
- **JS callers:**
  - `static/js/compare/index.js:948` → `/api/search`
  - `static/js/search-chat.js:188` → `/api/search?q=`
  - `static/js/slashCommands.js:1976` → `/api/search?q=`

## `POST /api/search`
- handler: `do_web_search` — `routes/search/search_routes.py:47`
- **JS callers:**
  - `static/js/compare/index.js:948` → `/api/search`
  - `static/js/search-chat.js:188` → `/api/search?q=`
  - `static/js/slashCommands.js:1976` → `/api/search?q=`

## `GET /api/search/config`
- handler: `get_search_settings` — `routes/search/search_routes.py:43`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/search/providers`
- handler: `list_search_providers` — `routes/search/search_routes.py:69`
- **JS callers:**
  - `static/js/compare/selector.js:573` → `/api/search/providers`
  - `static/js/compare/selector.js:680` → `/api/search/providers`

## `POST /api/search/query`
- handler: `search_with_provider` — `routes/search/search_routes.py:88`
- **JS callers:**
  - `static/js/compare/index.js:714` → `/api/search/query`
  - `static/js/compare/panes.js:125` → `/api/search/query`
  - `static/js/compare/selector.js:1217` → `/api/search/query`
  - `static/js/settings.js:1358` → `/api/search/query`

## `POST /api/session`
- handler: `create_session` — `routes/session_routes.py:392`
- **JS callers:**
  - `static/js/chat.js:7609` → `/api/session`
  - `static/js/compare/index.js:257` → `/api/session`
  - `static/js/compare/panes.js:393` → `/api/session`
  - `static/js/compare/panes.js:597` → `/api/session`
  - `static/js/compare/stream.js:234` → `/api/session`
  - `static/js/document.js:7307` → `/api/session`
  - `static/js/emailInbox.js:1371` → `/api/session`
  - `static/js/group.js:607` → `/api/session`
  - `static/js/group.js:630` → `/api/session`
  - `static/js/keyboard-shortcuts.js:236` → `/api/session`
  - `static/js/notes.js:4505` → `/api/session`
  - `static/js/notes.js:4571` → `/api/session`
  - `static/js/presets.js:415` → `/api/session`
  - `static/js/sessions.js:2402` → `/api/session`
  - `static/js/slashCommands.js:1010` → `/api/session`
  - `static/js/tasks.js:2569` → `/api/session`

## `POST /api/session/openai`
- handler: `create_session_openai` — `routes/session_routes.py:1053`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/compact`
- handler: `compact_session` — `routes/history/history_routes.py:1049`
- **JS callers:**
  - `static/js/chat.js:273` → `/api/session/${encodeURIComponent(sid)}/compact`
  - `static/js/chat.js:273` → `/api/session/${encodeURIComponent(sid)}/compact`

## `POST /api/session/{session_id}/compact`
- handler: `compact_session` — `routes/session_routes.py:1117`
- **JS callers:**
  - `static/js/chat.js:273` → `/api/session/${encodeURIComponent(sid)}/compact`
  - `static/js/chat.js:273` → `/api/session/${encodeURIComponent(sid)}/compact`

## `GET /api/session/{session_id}/context`
- handler: `get_session_context_usage` — `routes/history/history_routes.py:938`
- **JS callers:**
  - `static/js/chat.js:303` → `/api/session/${encodeURIComponent(sid)}/context`

## `GET /api/session/{session_id}/context_info`
- handler: `get_context_info` — `routes/session_routes.py:1497`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/delete-messages`
- handler: `delete_messages` — `routes/history/history_routes.py:474`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/edit-message`
- handler: `edit_message` — `routes/history/history_routes.py:545`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/fork`
- handler: `fork_session` — `routes/history/history_routes.py:816`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/important`
- handler: `mark_session_important` — `routes/session_routes.py:1080`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/mark-stopped`
- handler: `mark_stopped` — `routes/history/history_routes.py:600`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/merge-last-assistant`
- handler: `merge_last_assistant` — `routes/history/history_routes.py:706`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/message`
- handler: `add_message` — `routes/history/history_routes.py:456`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/truncate`
- handler: `truncate_session` — `routes/history/history_routes.py:417`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/uncompact`
- handler: `uncompact_session` — `routes/history/history_routes.py:987`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{session_id}/update-last-meta`
- handler: `update_last_meta` — `routes/history/history_routes.py:655`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/session/{sid}`
- handler: `delete_session` — `routes/session_routes.py:756`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PATCH /api/session/{sid}`
- handler: `rename_session` — `routes/session_routes.py:528`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{sid}/archive`
- handler: `archive_session` — `routes/session_routes.py:843`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{sid}/delete`
- handler: `delete_session_beacon` — `routes/session_routes.py:722`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/session/{sid}/export`
- handler: `export_session` — `routes/session_routes.py:955`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{sid}/inject_messages`
- handler: `inject_messages` — `routes/session_routes.py:686`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{sid}/retitle`
- handler: `retitle_session` — `routes/session_routes.py:606`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/session/{sid}/unarchive`
- handler: `unarchive_session` — `routes/session_routes.py:881`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/sessions`
- handler: `list_sessions` — `routes/session_routes.py:283`
- **JS callers:**
  - `static/js/documentLibrary.js:1901` → `/api/sessions`
  - `static/js/sessions.js:1772` → `/api/sessions`
  - `static/js/slashCommands.js:2019` → `/api/sessions`

## `DELETE /api/sessions/all`
- handler: `delete_all_sessions` — `routes/session_routes.py:790`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/sessions/archived`
- handler: `list_archived_sessions` — `routes/session_routes.py:911`
- **JS callers:**
  - `static/js/documentLibrary.js:2329` → `/api/sessions/archived?limit=100&sort=recent`
  - `static/js/sessions.js:3147` → `/api/sessions/archived?`
  - `static/js/sessions.js:3491` → `/api/sessions/archived?`

## `POST /api/sessions/auto-sort`
- handler: `auto_sort_sessions` — `routes/session_routes.py:1211`
- **JS callers:**
  - `static/app.js:1436` → `/api/sessions/auto-sort`
  - `static/js/documentLibrary.js:2291` → `/api/sessions/auto-sort`
  - `static/js/slashCommands.js:1163` → `/api/sessions/auto-sort`

## `POST /api/sessions/bulk-delete`
- handler: `bulk_delete_sessions` — `routes/session_routes.py:727`
- **JS callers:**
  - `static/js/compare/index.js:62` → `/api/sessions/bulk-delete`

## `POST /api/sessions/save`
- handler: `sessions_save_now` — `routes/session_routes.py:1045`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/shell/exec`
- handler: `shell_exec` — `routes/shell_routes.py:961`
- **JS callers:**
  - `static/js/codeRunner.js:324` → `/api/shell/exec`
  - `static/js/cookbook-diagnosis.js:1059` → `/api/shell/exec`
  - `static/js/cookbook-hwfit.js:1740` → `/api/shell/exec`
  - `static/js/cookbook-hwfit.js:1794` → `/api/shell/exec`
  - `static/js/cookbookDownload.js:282` → `/api/shell/exec`
  - `static/js/cookbookDownload.js:588` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1467` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1569` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1632` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1674` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1707` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1930` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:1952` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:2524` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:2888` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:2897` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:2919` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:2928` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:2939` → `/api/shell/exec`
  - `static/js/cookbookRunning.js:3058` → `/api/shell/exec`
  - … +10 more

## `POST /api/shell/stream`
- handler: `shell_stream` — `routes/shell_routes.py:979`
- **JS callers:**
  - `static/js/cookbookDownload.js:386` → `/api/shell/stream`

## `GET /api/signatures`
- handler: `list_signatures` — `routes/signature_routes.py:87`
- **JS callers:**
  - `static/js/document.js:1234` → `/api/signatures`
  - `static/js/document.js:1509` → `/api/signatures`
  - `static/js/signature.js:329` → `/api/signatures`
  - `static/js/signature.js:336` → `/api/signatures`

## `POST /api/signatures`
- handler: `create_signature` — `routes/signature_routes.py:102`
- **JS callers:**
  - `static/js/document.js:1234` → `/api/signatures`
  - `static/js/document.js:1509` → `/api/signatures`
  - `static/js/signature.js:329` → `/api/signatures`
  - `static/js/signature.js:336` → `/api/signatures`

## `DELETE /api/signatures/{sig_id}`
- handler: `delete_signature` — `routes/signature_routes.py:131`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/skills/add`
- handler: `add_skill` — `routes/skills_routes.py:1381`
- **JS callers:**
  - `static/js/skills.js:1956` → `/api/skills/add`

## `POST /api/skills/audit-all`
- handler: `audit_all_skills` — `routes/skills_routes.py:1702`
- **JS callers:**
  - `static/js/skills.js:1503` → `/api/skills/audit-all`

## `POST /api/skills/audit-all/cancel`
- handler: `audit_cancel` — `routes/skills_routes.py:1791`
- **JS callers:**
  - `static/js/skills.js:1653` → `/api/skills/audit-all/cancel`

## `GET /api/skills/audit-all/status`
- handler: `audit_status` — `routes/skills_routes.py:1777`
- **JS callers:**
  - `static/js/skills.js:1607` → `/api/skills/audit-all/status`

## `GET /api/skills/builtin`
- handler: `list_builtin_skills` — `routes/skills_routes.py:1251`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/skills/builtin/{name}`
- handler: `reset_builtin_override` — `routes/skills_routes.py:1338`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/skills/builtin/{name}`
- handler: `get_builtin_skill` — `routes/skills_routes.py:1288`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `PUT /api/skills/builtin/{name}`
- handler: `set_builtin_override` — `routes/skills_routes.py:1312`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/skills/import-from-url`
- handler: `import_skill_from_url` — `routes/skills_routes.py:1351`
- **JS callers:**
  - `static/js/skills.js:1915` → `/api/skills/import-from-url`

## `GET /api/skills/index`
- handler: `get_index` — `routes/skills_routes.py:1213`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/skills/search`
- handler: `search_skills` — `routes/skills_routes.py:1889`
- **JS callers:**
  - `static/js/slashCommands.js:1672` → `/api/skills/search`

## `GET /api/skills/slash-catalog`
- handler: `get_slash_catalog` — `routes/skills_routes.py:1222`
- **JS callers:**
  - `static/js/slashAutocomplete.js:86` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:347` → `/api/skills/slash-catalog`

## `DELETE /api/skills/{skill_id}`
- handler: `delete_skill` — `routes/skills_routes.py:1876`
- **JS callers:**
  - `static/js/skills.js:1503` → `/api/skills/audit-all`
  - `static/js/skills.js:1915` → `/api/skills/import-from-url`
  - `static/js/skills.js:1956` → `/api/skills/add`
  - `static/js/slashAutocomplete.js:86` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:347` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:1672` → `/api/skills/search`

## `GET /api/skills/{skill_id}`
- handler: `get_skill` — `routes/skills_routes.py:1455`
- **JS callers:**
  - `static/js/skills.js:1503` → `/api/skills/audit-all`
  - `static/js/skills.js:1915` → `/api/skills/import-from-url`
  - `static/js/skills.js:1956` → `/api/skills/add`
  - `static/js/slashAutocomplete.js:86` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:347` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:1672` → `/api/skills/search`

## `PUT /api/skills/{skill_id}`
- handler: `update_skill` — `routes/skills_routes.py:1857`
- **JS callers:**
  - `static/js/skills.js:1503` → `/api/skills/audit-all`
  - `static/js/skills.js:1915` → `/api/skills/import-from-url`
  - `static/js/skills.js:1956` → `/api/skills/add`
  - `static/js/slashAutocomplete.js:86` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:347` → `/api/skills/slash-catalog`
  - `static/js/slashCommands.js:1672` → `/api/skills/search`

## `POST /api/skills/{skill_id}/invoke`
- handler: `invoke_skill` — `routes/skills_routes.py:1414`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/skills/{skill_id}/markdown`
- handler: `get_skill_markdown` — `routes/skills_routes.py:1464`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/skills/{skill_id}/markdown`
- handler: `save_skill_markdown` — `routes/skills_routes.py:1804`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/skills/{skill_id}/test`
- handler: `test_skill` — `routes/skills_routes.py:1479`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/skills/{skill_id}/test-approval`
- handler: `approve_skill_test_action` — `routes/skills_routes.py:1562`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/skills/{skill_id}/test-status`
- handler: `test_skill_status` — `routes/skills_routes.py:1683`
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
- handler: `list_actions` — `routes/task/task_routes.py:1021`
- **JS callers:**
  - `static/js/tasks.js:209` → `/api/tasks/meta/actions`

## `GET /api/tasks/meta/events`
- handler: `list_events` — `routes/task/task_routes.py:1032`
- **JS callers:**
  - `static/js/tasks.js:337` → `/api/tasks/meta/events`

## `GET /api/tasks/meta/output-targets`
- handler: `list_output_targets` — `routes/task/task_routes.py:983`
- **JS callers:**
  - `static/js/tasks.js:196` → `/api/tasks/meta/output-targets`

## `GET /api/tasks/notifications`
- handler: `get_notifications` — `routes/task/task_routes.py:562`
- **JS callers:**
  - `static/js/tasks.js:3127` → `/api/tasks/notifications`

## `GET /api/tasks/onboarding`
- handler: `get_tasks_onboarding` — `routes/task/task_routes.py:374`
- **JS callers:**
  - `static/js/tasks.js:57` → `/api/tasks/onboarding`
  - `static/js/tasks.js:62` → `/api/tasks/onboarding`

## `POST /api/tasks/onboarding`
- handler: `update_tasks_onboarding` — `routes/task/task_routes.py:383`
- **JS callers:**
  - `static/js/tasks.js:57` → `/api/tasks/onboarding`
  - `static/js/tasks.js:62` → `/api/tasks/onboarding`

## `POST /api/tasks/parse`
- handler: `parse_task` — `routes/task/task_routes.py:1090`
- **JS callers:**
  - `static/js/tasks.js:2842` → `/api/tasks/parse`

## `GET /api/tasks/runs/recent`
- handler: `list_recent_runs` — `routes/task/task_routes.py:893`
- **JS callers:**
  - `static/js/tasks.js:2073` → `/api/tasks/runs/recent?limit=`
  - `static/js/tasks.js:2233` → `/api/tasks/runs/recent?limit=`

## `DELETE /api/tasks/{task_id}`
- handler: `delete_task` — `routes/task/task_routes.py:757`
- **JS callers:**
  - `static/js/cookbookSchedule.js:353` → `/api/tasks/${encodeURIComponent(data.id)}`
  - `static/js/tasks.js:57` → `/api/tasks/onboarding`
  - `static/js/tasks.js:62` → `/api/tasks/onboarding`
  - `static/js/tasks.js:2842` → `/api/tasks/parse`
  - `static/js/tasks.js:3127` → `/api/tasks/notifications`

## `GET /api/tasks/{task_id}`
- handler: `get_task` — `routes/task/task_routes.py:653`
- **JS callers:**
  - `static/js/cookbookSchedule.js:353` → `/api/tasks/${encodeURIComponent(data.id)}`
  - `static/js/tasks.js:57` → `/api/tasks/onboarding`
  - `static/js/tasks.js:62` → `/api/tasks/onboarding`
  - `static/js/tasks.js:2842` → `/api/tasks/parse`
  - `static/js/tasks.js:3127` → `/api/tasks/notifications`

## `PUT /api/tasks/{task_id}`
- handler: `update_task` — `routes/task/task_routes.py:667`
- **JS callers:**
  - `static/js/cookbookSchedule.js:353` → `/api/tasks/${encodeURIComponent(data.id)}`
  - `static/js/tasks.js:57` → `/api/tasks/onboarding`
  - `static/js/tasks.js:62` → `/api/tasks/onboarding`
  - `static/js/tasks.js:2842` → `/api/tasks/parse`
  - `static/js/tasks.js:3127` → `/api/tasks/notifications`

## `POST /api/tasks/{task_id}/clear-cache`
- handler: `clear_task_cache` — `routes/task/task_routes.py:573`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/pause`
- handler: `pause_task` — `routes/task/task_routes.py:779`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/resume`
- handler: `resume_task` — `routes/task/task_routes.py:795`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/revert`
- handler: `revert_task` — `routes/task/task_routes.py:818`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/run`
- handler: `run_task_now` — `routes/task/task_routes.py:858`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/tasks/{task_id}/runs`
- handler: `list_runs` — `routes/task/task_routes.py:965`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/stop`
- handler: `stop_task_now` — `routes/task/task_routes.py:876`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/webhook-regenerate`
- handler: `regenerate_webhook` — `routes/task/task_routes.py:1073`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `POST /api/tasks/{task_id}/webhook/{token}`
- handler: `webhook_trigger` — `routes/task/task_routes.py:1046`
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
  - `static/js/admin.js:2554` → `/api/tokens`
  - `static/js/admin.js:2653` → `/api/tokens`
  - `static/js/settings.js:3519` → `/api/tokens`
  - `static/js/settings.js:5124` → `/api/tokens`
  - `static/js/settings.js:5410` → `/api/tokens`

## `POST /api/tokens`
- handler: `create_token` — `routes/api_token_routes.py:116`
- **JS callers:**
  - `static/js/admin.js:2554` → `/api/tokens`
  - `static/js/admin.js:2653` → `/api/tokens`
  - `static/js/settings.js:3519` → `/api/tokens`
  - `static/js/settings.js:5124` → `/api/tokens`
  - `static/js/settings.js:5410` → `/api/tokens`

## `GET /api/tokens/profiles`
- handler: `token_profiles` — `routes/api_token_routes.py:108`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `DELETE /api/tokens/{token_id}`
- handler: `delete_token` — `routes/api_token_routes.py:196`
- **JS callers:**
  - `static/js/admin.js:2579` → `/api/tokens/${btn.dataset.admDelToken}`
  - `static/js/admin.js:2602` → `/api/tokens/${input.dataset.tokenId}`
  - `static/js/admin.js:2622` → `/api/tokens/${tokenId}`
  - `static/js/settings.js:3653` → `/api/tokens/${id}`
  - `static/js/settings.js:5274` → `/api/tokens/${renameInput.dataset.tokenId}`
  - `static/js/settings.js:5293` → `/api/tokens/${cb.dataset.tokenId}`
  - `static/js/settings.js:5334` → `/api/tokens/${tokenId}`
  - `static/js/settings.js:5360` → `/api/tokens/${tokenId}`
  - `static/js/settings.js:5536` → `/api/tokens/${tokenId}`

## `PATCH /api/tokens/{token_id}`
- handler: `update_token` — `routes/api_token_routes.py:156`
- **JS callers:**
  - `static/js/admin.js:2579` → `/api/tokens/${btn.dataset.admDelToken}`
  - `static/js/admin.js:2602` → `/api/tokens/${input.dataset.tokenId}`
  - `static/js/admin.js:2622` → `/api/tokens/${tokenId}`
  - `static/js/settings.js:3653` → `/api/tokens/${id}`
  - `static/js/settings.js:5274` → `/api/tokens/${renameInput.dataset.tokenId}`
  - `static/js/settings.js:5293` → `/api/tokens/${cb.dataset.tokenId}`
  - `static/js/settings.js:5334` → `/api/tokens/${tokenId}`
  - `static/js/settings.js:5360` → `/api/tokens/${tokenId}`
  - `static/js/settings.js:5536` → `/api/tokens/${tokenId}`

## `GET /api/tools`
- handler: `list_tools` — `routes/model_routes.py:2697`
- **JS callers:**
  - `static/js/admin.js:2004` → `/api/tools`
  - `static/js/appConfig.js:33` → `/api/tools`

## `POST /api/tools`
- handler: `update_tools` — `routes/model_routes.py:2711`
- **JS callers:**
  - `static/js/admin.js:2004` → `/api/tools`
  - `static/js/appConfig.js:33` → `/api/tools`

## `POST /api/tts/clear-cache`
- handler: `clear_tts_cache` — `routes/tts_routes.py:78`
- **JS callers:**
  - `static/js/settings.js:855` → `/api/tts/clear-cache`

## `GET /api/tts/stats`
- handler: `get_tts_stats` — `routes/tts_routes.py:22`
- **JS callers:**
  - `static/js/tts-ai.js:47` → `/api/tts/stats`

## `POST /api/tts/synthesize`
- handler: `synthesize_speech` — `routes/tts_routes.py:31`
- **JS callers:**
  - `static/js/settings.js:913` → `/api/tts/synthesize`
  - `static/js/slashCommands.js:2095` → `/api/tts/synthesize`
  - `static/js/tts-ai.js:135` → `/api/tts/synthesize`

## `POST /api/upload/cleanup`
- handler: `manual_cleanup` — `routes/upload_routes.py:321`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/upload/stats`
- handler: `upload_stats` — `routes/upload_routes.py:344`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/upload/{file_id}`
- handler: `download_file` — `routes/upload_routes.py:354`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/upload/{file_id}/vision`
- handler: `get_vision_text` — `routes/upload_routes.py:452`
- **JS callers:**
  - `static/js/chatRenderer.js:328` → `/api/upload/${att.id}/vision`
  - `static/js/chatRenderer.js:392` → `/api/upload/${att.id}/vision`

## `PUT /api/upload/{file_id}/vision`
- handler: `put_vision_text` — `routes/upload_routes.py:497`
- **JS callers:**
  - `static/js/chatRenderer.js:328` → `/api/upload/${att.id}/vision`
  - `static/js/chatRenderer.js:392` → `/api/upload/${att.id}/vision`

## `POST /api/v1/chat`
- handler: `sync_chat` — `routes/webhook/webhook_routes.py:238`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/vault/config`
- handler: `get_config` — `routes/vault/vault_routes.py:130`
- **JS callers:**
  - `static/js/settings.js:3518` → `/api/vault/config`
  - `static/js/settings.js:4823` → `/api/vault/config`
  - `static/js/settings.js:4846` → `/api/vault/config`

## `POST /api/vault/config`
- handler: `save_config` — `routes/vault/vault_routes.py:143`
- **JS callers:**
  - `static/js/settings.js:3518` → `/api/vault/config`
  - `static/js/settings.js:4823` → `/api/vault/config`
  - `static/js/settings.js:4846` → `/api/vault/config`

## `POST /api/vault/lock`
- handler: `lock` — `routes/vault/vault_routes.py:206`
- **JS callers:**
  - `static/js/settings.js:4899` → `/api/vault/lock`

## `POST /api/vault/login`
- handler: `login` — `routes/vault/vault_routes.py:159`
- **JS callers:**
  - `static/js/settings.js:4863` → `/api/vault/login`

## `POST /api/vault/logout`
- handler: `logout` — `routes/vault/vault_routes.py:218`
- **JS callers:**
  - `static/js/settings.js:3654` → `/api/vault/logout`
  - `static/js/settings.js:4909` → `/api/vault/logout`

## `POST /api/vault/unlock`
- handler: `unlock` — `routes/vault/vault_routes.py:184`
- **JS callers:**
  - `static/js/settings.js:4882` → `/api/vault/unlock`

## `GET /api/version`
- handler: `get_version` — `app.py:951`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /api/webhooks`
- handler: `list_webhooks` — `routes/webhook/webhook_routes.py:72`
- **JS callers:**
  - `static/js/admin.js:2687` → `/api/webhooks`
  - `static/js/admin.js:2749` → `/api/webhooks`

## `POST /api/webhooks`
- handler: `create_webhook` — `routes/webhook/webhook_routes.py:96`
- **JS callers:**
  - `static/js/admin.js:2687` → `/api/webhooks`
  - `static/js/admin.js:2749` → `/api/webhooks`

## `DELETE /api/webhooks/{webhook_id}`
- handler: `delete_webhook` — `routes/webhook/webhook_routes.py:171`
- **JS callers:**
  - `static/js/admin.js:2724` → `/api/webhooks/${btn.dataset.admWhToggle}`
  - `static/js/admin.js:2729` → `/api/webhooks/${btn.dataset.admWhDelete}`
  - `static/js/settings.js:3818` → `/api/webhooks/...`

## `PATCH /api/webhooks/{webhook_id}`
- handler: `toggle_webhook` — `routes/webhook/webhook_routes.py:157`
- **JS callers:**
  - `static/js/admin.js:2724` → `/api/webhooks/${btn.dataset.admWhToggle}`
  - `static/js/admin.js:2729` → `/api/webhooks/${btn.dataset.admWhDelete}`
  - `static/js/settings.js:3818` → `/api/webhooks/...`

## `POST /api/webhooks/{webhook_id}/test`
- handler: `test_webhook` — `routes/webhook/webhook_routes.py:142`
- **JS callers:**
  - `static/js/admin.js:2717` → `/api/webhooks/${btn.dataset.admWhTest}/test`

## `GET /api/workspace/browse`
- handler: `browse` — `routes/workspace_routes.py:18`
- **JS callers:**
  - `static/js/workspace.js:93` → `/api/workspace/browse`

## `GET /api/workspace/vet`
- handler: `vet` — `routes/workspace_routes.py:69`
- **JS callers:**
  - `static/js/workspace.js:74` → `/api/workspace/vet?path=`

## `GET /backgrounds`
- handler: `serve_backgrounds` — `app.py:940`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /calendar`
- handler: `serve_calendar` — `app.py:908`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /cookbook`
- handler: `serve_cookbook` — `app.py:916`
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
- handler: `serve_email` — `app.py:920`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /gallery`
- handler: `serve_gallery` — `app.py:928`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /health`
- handler: `health` — `scripts/diffusion_server.py:1462`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /library`
- handler: `serve_library` — `app.py:936`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /login`
- handler: `serve_login` — `app.py:945`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /loop-thread`
- handler: `loop_thread_probe` — `tests/test_add_directory_event_loop.py:101`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /memory`
- handler: `serve_memory` — `app.py:924`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /notes`
- handler: `serve_notes` — `app.py:904`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /plain`
- handler: `plain` — `tests/test_security_headers_pdf_preview.py:13`
- _no literal JS fetch found (dynamic URL, server-side call, or unused)_

## `GET /tasks`
- handler: `serve_tasks` — `app.py:932`
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
- `static/app.js:200` → `/api/auth/`
- `static/app.js:615` → `/api/session/`
- `static/app.js:1590` → `/api/ai/name`
- `static/app.js:1650` → `/api/session/`
- `static/app.js:3416` → `/api/session/`
- `static/js/admin.js:144` → `/api/auth/users/`
- `static/js/admin.js:170` → `/api/auth/users/`
- `static/js/admin.js:218` → `/api/auth/users/`
- `static/js/admin.js:308` → `/api/auth/users/`
- `static/js/admin.js:583` → `/api/model-endpoints/`
- `static/js/admin.js:614` → `/api/model-endpoints/`
- `static/js/admin.js:627` → `/api/model-endpoints/`
- `static/js/admin.js:685` → `/api/model-endpoints/`
- `static/js/admin.js:752` → `/api/model-endpoints/`
- `static/js/admin.js:779` → `/api/model-endpoints/`
- `static/js/admin.js:1483` → `/api/model-endpoints/`
- `static/js/admin.js:1546` → `/api/model-endpoints/`
- `static/js/admin.js:2086` → `/api/mcp/oauth/authorize/`
- `static/js/admin.js:2100` → `/api/mcp/servers/`
- `static/js/admin.js:2111` → `/api/mcp/servers/`
- `static/js/admin.js:2118` → `/api/mcp/servers/`
- `static/js/admin.js:2144` → `/api/mcp/servers/`
- `static/js/admin.js:2188` → `/api/mcp/servers/`
- `static/js/admin.js:2390` → `/api/mcp/oauth/authorize/`
- `static/js/admin.js:2411` → `/api/personal`
- `static/js/admin.js:2579` → `/api/tokens/`
- `static/js/admin.js:2602` → `/api/tokens/`
- `static/js/admin.js:2622` → `/api/tokens/`
- `static/js/admin.js:2717` → `/api/webhooks/`
- `static/js/admin.js:2724` → `/api/webhooks/`
- `static/js/admin.js:2729` → `/api/webhooks/`
- `static/js/admin.js:2921` → `/api/admin/wipe/`
- `static/js/admin.js:2941` → `/api/admin/wipe/`
- `static/js/appConfig.js:14` → `/api/...`
- `static/js/assistant.js:12` → `/api/assistant`
- `static/js/assistant.js:252` → `/api/model-endpoints/`
- `static/js/calendar.js:38` → `/api/upload`
- `static/js/calendar.js:42` → `/api/upload/`
- `static/js/calendar.js:284` → `/api/calendar/events/`
- `static/js/calendar.js:335` → `/api/calendar/events/`
- `static/js/calendar.js:599` → `/api/notes`
- `static/js/calendar.js:2656` → `/api/calendar/calendars/`
- `static/js/calendar.js:2681` → `/api/calendar/calendars/`
- `static/js/calendar.js:2725` → `/api/calendar/export/`
- `static/js/calendar/reminders.js:5` → `/api/notes?label=calendar`
- `static/js/calendar/reminders.js:59` → `/api/notes?label=calendar`
- `static/js/chat.js:273` → `/api/session/`
- `static/js/chat.js:303` → `/api/session/`
- `static/js/chat.js:820` → `/api/chat/stream_status/`
- `static/js/chat.js:863` → `/api/chat/stream_status/`
- `static/js/chat.js:1031` → `/api/chat/stop/`
- `static/js/chat.js:1507` → `/api/research/cancel/`
- `static/js/chat.js:1612` → `/api/session/`
- `static/js/chat.js:3808` → `/api/upload/`
- `static/js/chat.js:3810` → `/api/upload/`
- `static/js/chat.js:3832` → `/api/upload/`
- `static/js/chat.js:4779` → `/api/session/`
- `static/js/chat.js:4992` → `/api/session/`
- `static/js/chat.js:5030` → `/api/chat/stream_status/`
- `static/js/chat.js:5345` → `/api/chat/stream_status/`
- `static/js/chat.js:5412` → `/api/chat/stream_status/`
- `static/js/chat.js:5487` → `/api/session/`
- `static/js/chat.js:5598` → `/api/chat/resume/`
- `static/js/chat.js:6501` → `/api/session/`
- `static/js/chat.js:6601` → `/api/session/`
- `static/js/chat.js:6749` → `/api/session/`
- `static/js/chat.js:6815` → `/api/session/`
- `static/js/chat.js:6913` → `/api/session/`
- `static/js/chat.js:6933` → `/api/session/`
- `static/js/chat.js:6958` → `/api/research/status/`
- `static/js/chat.js:6969` → `/api/research/result/`
- `static/js/chat.js:7117` → `/api/research/status/`
- `static/js/chat.js:7143` → `/api/research/result/`
- `static/js/chat.js:7279` → `/api/session/`
- `static/js/chat.js:7352` → `/api/session/`
- `static/js/chat.js:7519` → `/api/session/`
- `static/js/chat.js:7574` → `/api/upload/`
- `static/js/chatRenderer.js:150` → `/api/upload/`
- `static/js/chatRenderer.js:203` → `/api/upload/`
- `static/js/chatRenderer.js:249` → `/api/upload/`
- `static/js/chatRenderer.js:259` → `/api/upload/`
- `static/js/chatRenderer.js:328` → `/api/upload/`
- `static/js/chatRenderer.js:392` → `/api/upload/`
- `static/js/chatRenderer.js:471` → `/api/tools fetch failed; live exec-fence stripping disabled until reload`
- `static/js/chatRenderer.js:770` → `/api/session/`
- `static/js/chatRenderer.js:1241` → `/api/research/report/`
- `static/js/chatRenderer.js:1257` → `/api/research/spinoff/`
- `static/js/chatRenderer.js:1617` → `/api/gallery/`
- `static/js/chatRenderer.js:2238` → `/api/session/`
- `static/js/compare/index.js:168` → `/api/session/`
- `static/js/compare/index.js:220` → `/api/session/`
- `static/js/compare/panes.js:476` → `/api/session/`
- `static/js/compare/panes.js:585` → `/api/session/`
- `static/js/compare/stream.js:285` → `/api/session/`
- `static/js/cookbook.js:2784` → `/api/cookbook/ollama/library${refresh ? `
- `static/js/cookbookRunning.js:539` → `/api/model-endpoints/`
- `static/js/cookbookRunning.js:1154` → `/api/generate`
- `static/js/cookbookRunning.js:1889` → `/api/cookbook/gpus${params.toString() ? `
- `static/js/cookbookRunning.js:2016` → `/api/model/serve failed`
- `static/js/cookbookRunning.js:2968` → `/api/model-endpoints/`
- `static/js/cookbookRunning.js:4091` → `/api/model-endpoints/`
- `static/js/cookbookSchedule.js:277` → `/api/tasks`
- `static/js/cookbookSchedule.js:353` → `/api/tasks/`
- `static/js/cookbookServe.js:4202` → `/api/model/cached${params}`
- `static/js/document.js:621` → `/api/document/`
- `static/js/document.js:661` → `/api/document/`
- `static/js/document.js:705` → `/api/document/`
- `static/js/document.js:901` → `/api/document/`
- `static/js/document.js:1056` → `/api/document/`
- `static/js/document.js:1160` → `/api/document/`
- `static/js/document.js:1196` → `/api/document/`
- `static/js/document.js:1796` → `/api/document/`
- `static/js/document.js:1831` → `/api/document/`
- `static/js/document.js:1950` → `/api/document/`
- `static/js/document.js:2989` → `/api/email/attachment-as-doc/`
- `static/js/document.js:2995` → `/api/email/attachment/`
- `static/js/document.js:3016` → `/api/email/attachment/`
- `static/js/document.js:3172` → `/api/email/compose-from-attachment/`
- `static/js/document.js:3534` → `/api/upload/`
- `static/js/document.js:3564` → `/api/upload`
- `static/js/document.js:3613` → `/api/email/compose-upload/`
- `static/js/document.js:3972` → `/api/email/mark-answered/`
- `static/js/document.js:3978` → `/api/document/`
- `static/js/document.js:4075` → `/api/document/`
- `static/js/document.js:4459` → `/api/email/mark-unread/`
- `static/js/document.js:4478` → `/api/document/`
- `static/js/document.js:4531` → `/api/document/`
- `static/js/document.js:4537` → `/api/document/`
- `static/js/document.js:4618` → `/api/document/`
- `static/js/document.js:5779` → `/api/document/`
- `static/js/document.js:7245` → `/api/document/`
- `static/js/document.js:7337` → `/api/documents/`
- `static/js/document.js:9310` → `/api/document/`
- `static/js/document.js:9413` → `/api/document/`
- `static/js/document.js:9594` → `/api/document/`
- `static/js/document.js:9815` → `/api/document/`
- `static/js/document.js:10946` → `/api/document/`
- `static/js/document.js:10998` → `/api/document/`
- `static/js/document.js:11012` → `/api/document/`
- `static/js/document.js:11040` → `/api/document/`
- `static/js/document.js:11107` → `/api/document/`
- `static/js/documentLibrary.js:133` → `/api/history/`
- `static/js/documentLibrary.js:714` → `/api/document/`
- `static/js/documentLibrary.js:741` → `/api/document/`
- `static/js/documentLibrary.js:834` → `/api/document/`
- `static/js/documentLibrary.js:927` → `/api/document/`
- `static/js/documentLibrary.js:941` → `/api/document/`
- `static/js/documentLibrary.js:1028` → `/api/document/`
- `static/js/documentLibrary.js:1071` → `/api/document/`
- `static/js/documentLibrary.js:1192` → `/api/document/`
- `static/js/documentLibrary.js:1228` → `/api/document/`
- `static/js/documentLibrary.js:1262` → `/api/document/`
- `static/js/documentLibrary.js:1338` → `/api/document/`
- `static/js/documentLibrary.js:1937` → `/api/history/`
- `static/js/documentLibrary.js:2028` → `/api/session/`
- `static/js/documentLibrary.js:2037` → `/api/session/`
- `static/js/documentLibrary.js:2049` → `/api/session/`
- `static/js/documentLibrary.js:2122` → `/api/session/`
- `static/js/documentLibrary.js:2125` → `/api/session/`
- `static/js/documentLibrary.js:2206` → `/api/session/`
- `static/js/documentLibrary.js:2250` → `/api/session/`
- `static/js/documentLibrary.js:2368` → `/api/document/`
- `static/js/documentLibrary.js:2391` → `/api/document/`
- `static/js/documentLibrary.js:2396` → `/api/document/`
- `static/js/documentLibrary.js:2477` → `/api/session/`
- `static/js/documentLibrary.js:2480` → `/api/session/`
- `static/js/documentLibrary.js:2524` → `/api/document/`
- `static/js/documentLibrary.js:2525` → `/api/document/`
- `static/js/documentLibrary.js:2561` → `/api/research/report/`
- `static/js/documentLibrary.js:2562` → `/api/research/`
- `static/js/documentLibrary.js:2563` → `/api/research/`
- `static/js/documentLibrary.js:2632` → `/api/document/`
- `static/js/documentLibrary.js:2633` → `/api/research/`
- `static/js/documentLibrary.js:2634` → `/api/session/`
- `static/js/documentLibrary.js:2638` → `/api/document/`
- `static/js/documentLibrary.js:2639` → `/api/research/`
- `static/js/documentLibrary.js:2640` → `/api/session/`
- `static/js/documentLibrary.js:2732` → `/api/research/detail/`
- `static/js/documentLibrary.js:2786` → `/api/research/spinoff/`
- `static/js/documentLibrary.js:2804` → `/api/research/report/`
- `static/js/documentLibrary.js:2819` → `/api/research/`
- `static/js/documentLibrary.js:2839` → `/api/research/`
- `static/js/documentLibrary.js:2951` → `/api/research/report/`
- `static/js/documentLibrary.js:2962` → `/api/research/`
- `static/js/documentLibrary.js:2977` → `/api/research/`
- `static/js/documentLibrary.js:3045` → `/api/research/detail/`
- `static/js/documentLibrary.js:3059` → `/api/research/`
- `static/js/documentLibrary.js:3110` → `/api/research/`
- `static/js/documentLibrary.js:3134` → `/api/research/`
- `static/js/emailInbox.js:674` → `/api/email/`
- `static/js/emailInbox.js:798` → `/api/email/read/`
- `static/js/emailInbox.js:1057` → `/api/document failed`
- `static/js/emailInbox.js:1233` → `/api/notes`
- `static/js/emailInbox.js:1254` → `/api/email/archive/`
- `static/js/emailInbox.js:1271` → `/api/email/delete/`
- `static/js/emailInbox.js:1323` → `/api/email/mark-answered/`
- `static/js/emailInbox.js:1324` → `/api/email/mark-read/`
- `static/js/emailInbox.js:1326` → `/api/email/clear-answered/`
- `static/js/emailLibrary.js:1199` → `/api/email/delete/`
- `static/js/emailLibrary.js:3246` → `/api/email/accounts/`
- `static/js/emailLibrary.js:4885` → `/api/email/scheduled/`
- `static/js/emailLibrary.js:5189` → `/api/email/mark-answered/`
- `static/js/emailLibrary.js:5190` → `/api/email/mark-read/`
- `static/js/emailLibrary.js:5192` → `/api/email/clear-answered/`
- `static/js/emailLibrary.js:5369` → `/api/email/read/`
- `static/js/emailLibrary.js:5506` → `/api/email/read/`
- `static/js/emailLibrary.js:5915` → `/api/email/inline-image/`
- `static/js/emailLibrary.js:6056` → `/api/email/inline-image/`
- `static/js/emailLibrary.js:6599` → `/api/email/attachments-download/`
- `static/js/emailLibrary.js:6658` → `/api/email/attachment-as-doc/`
- `static/js/emailLibrary.js:6727` → `/api/email/attachment/`
- `static/js/emailLibrary.js:6866` → `/api/email/attachments/`
- `static/js/emailLibrary.js:7175` → `/api/email/read/`
- `static/js/emailLibrary.js:7320` → `/api/email/read/`
- `static/js/emailLibrary.js:7742` → `/api/email/mark-read/`
- `static/js/emailLibrary.js:7744` → `/api/email/mark-unread/`
- `static/js/emailLibrary.js:7762` → `/api/email/flag/`
- `static/js/emailLibrary.js:7783` → `/api/email/mark-answered/`
- `static/js/emailLibrary.js:7784` → `/api/email/mark-read/`
- `static/js/emailLibrary.js:7786` → `/api/email/clear-answered/`
- `static/js/emailLibrary.js:7797` → `/api/email/archive/`
- `static/js/emailLibrary.js:7838` → `/api/email/move/`
- `static/js/emailLibrary.js:7850` → `/api/email/delete/`
- `static/js/emailLibrary.js:7875` → `/api/email/delete-permanent/`
- `static/js/emailLibrary.js:7993` → `/api/email/mark-answered/`
- `static/js/emailLibrary.js:7994` → `/api/email/mark-read/`
- `static/js/emailLibrary.js:7996` → `/api/email/clear-answered/`
- `static/js/emailLibrary.js:8016` → `/api/email/flag/`
- `static/js/emailLibrary.js:8028` → `/api/email/archive/`
- `static/js/emailLibrary.js:8044` → `/api/email/flag/`
- `static/js/emailLibrary.js:8056` → `/api/email/archive/`
- `static/js/emailLibrary.js:8091` → `/api/email/delete/`
- `static/js/emailLibrary.js:8270` → `/api/email/archive/`
- `static/js/emailLibrary.js:8272` → `/api/email/delete/`
- `static/js/emailLibrary.js:8284` → `/api/email/mark-answered/`
- `static/js/emailLibrary.js:8285` → `/api/email/mark-read/`
- `static/js/emailLibrary.js:8289` → `/api/email/`
- `static/js/emailLibrary.js:8736` → `/api/notes`
- `static/js/fileHandler.js:307` → `/api/upload`
- `static/js/gallery.js:196` → `/api/gallery/`
- `static/js/gallery.js:215` → `/api/gallery/`
- `static/js/gallery.js:757` → `/api/gallery/albums/`
- `static/js/gallery.js:778` → `/api/gallery/albums/`
- `static/js/gallery.js:865` → `/api/gallery/albums/`
- `static/js/gallery.js:1022` → `/api/editor-drafts/`
- `static/js/gallery.js:1096` → `/api/editor-drafts/`
- `static/js/gallery.js:1352` → `/api/gallery/`
- `static/js/gallery.js:1617` → `/api/gallery/`
- `static/js/gallery.js:1662` → `/api/gallery/`
- `static/js/gallery.js:1812` → `/api/gallery/`
- `static/js/gallery.js:1845` → `/api/gallery/albums/`
- `static/js/gallery.js:1887` → `/api/gallery/`
- `static/js/gallery.js:2409` → `/api/gallery/`
- `static/js/gallery.js:2906` → `/api/gallery/`
- `static/js/galleryEditor.js:1113` → `/api/editor-drafts/`
- `static/js/galleryEditor.js:1153` → `/api/editor-drafts/`
- `static/js/galleryEditor.js:1182` → `/api/editor-drafts/`
- `static/js/galleryEditor.js:3298` → `/api/gallery/`
- `static/js/group.js:666` → `/api/session/`
- `static/js/group.js:716` → `/api/session/`
- `static/js/group.js:798` → `/api/session/`
- `static/js/group.js:825` → `/api/session/`
- `static/js/group.js:965` → `/api/session/`
- `static/js/keyboard-shortcuts.js:188` → `/api/session/`
- `static/js/keyboard-shortcuts.js:207` → `/api/session/`
- `static/js/markdown.js:632` → `/api/emoji/`
- `static/js/memory.js:254` → `/api/prefs/`
- `static/js/memory.js:274` → `/api/prefs/`
- `static/js/memory.js:302` → `/api/prefs/`
- `static/js/memory.js:316` → `/api/prefs/`
- `static/js/memory.js:335` → `/api/prefs/`
- `static/js/memory.js:349` → `/api/prefs/`
- `static/js/memory.js:378` → `/api/memory`
- `static/js/memory.js:485` → `/api/memory/`
- `static/js/memory.js:543` → `/api/memory`
- `static/js/memory.js:1059` → `/api/memory/`
- `static/js/memory.js:1155` → `/api/memory/`
- `static/js/memory.js:1178` → `/api/memory/`
- `static/js/modelPicker.js:711` → `/api/session/`
- `static/js/notes.js:365` → `/api/upload`
- `static/js/notes.js:369` → `/api/upload/`
- `static/js/notes.js:450` → `/api/notes`
- `static/js/notes.js:465` → `/api/notes/`
- `static/js/notes.js:465` → `/api/notes`
- `static/js/notes.js:478` → `/api/notes/`
- `static/js/notes.js:483` → `/api/notes/`
- `static/js/notes.js:3511` → `/api/upload`
- `static/js/notes.js:3515` → `/api/upload/`
- `static/js/notes.js:4349` → `/api/upload`
- `static/js/notes.js:4352` → `/api/upload/`
- `static/js/notes.js:5302` → `/api/notes`
- `static/js/presets.js:245` → `/api/presets/templates/`
- `static/js/presets.js:423` → `/api/session/`
- `static/js/presets.js:974` → `/api/memory`
- `static/js/providerDeviceFlow.js:6` → `/api/copilot/device/start`
- `static/js/providerDeviceFlow.js:7` → `/api/copilot/device/poll`
- `static/js/providerDeviceFlow.js:14` → `/api/chatgpt-subscription/device/start`
- `static/js/providerDeviceFlow.js:15` → `/api/chatgpt-subscription/device/poll`
- `static/js/rag.js:36` → `/api/personal`
- `static/js/research/jobs.js:211` → `/api/research/cancel/`
- `static/js/research/jobs.js:308` → `/api/research/stream/`
- `static/js/research/jobs.js:336` → `/api/research/status/`
- `static/js/research/jobs.js:369` → `/api/research/result-peek/`
- `static/js/research/panel.js:1023` → `/api/research/report/`
- `static/js/research/panel.js:1033` → `/api/research/report/`
- `static/js/research/panel.js:1045` → `/api/research/`
- `static/js/research/panel.js:1143` → `/api/research/result-peek/`
- `static/js/research/panel.js:1220` → `/api/research/spinoff/`
- `static/js/sessions.js:144` → `/api/history/`
- `static/js/sessions.js:323` → `/api/session/`
- `static/js/sessions.js:424` → `/api/session/`
- `static/js/sessions.js:609` → `/api/session/`
- `static/js/sessions.js:647` → `/api/session/`
- `static/js/sessions.js:767` → `/api/session/`
- `static/js/sessions.js:805` → `/api/session/`
- `static/js/sessions.js:820` → `/api/history/`
- `static/js/sessions.js:948` → `/api/session/`
- `static/js/sessions.js:998` → `/api/session/`
- `static/js/sessions.js:1007` → `/api/session/`
- `static/js/sessions.js:1332` → `/api/session/`
- `static/js/sessions.js:1455` → `/api/session/`
- `static/js/sessions.js:1715` → `/api/session/`
- `static/js/sessions.js:1734` → `/api/session/`
- `static/js/sessions.js:2425` → `/api/session/`
- `static/js/sessions.js:2547` → `/api/session/`
- `static/js/sessions.js:2591` → `/api/session/`
- `static/js/sessions.js:2682` → `/api/research/status/`
- `static/js/sessions.js:2805` → `/api/chat/stream_status/`
- `static/js/sessions.js:2864` → `/api/chat/stream_status/`
- `static/js/sessions.js:3015` → `/api/history/`
- `static/js/sessions.js:3058` → `/api/session/`
- `static/js/sessions.js:3070` → `/api/session/`
- `static/js/sessions.js:3090` → `/api/session/`
- `static/js/sessions.js:3108` → `/api/session/`
- `static/js/sessions.js:3398` → `/api/session/`
- `static/js/sessions.js:3401` → `/api/session/`
- `static/js/sessions.js:3415` → `/api/session/`
- `static/js/sessions.js:3417` → `/api/document/`
- `static/js/sessions.js:3419` → `/api/research/`
- `static/js/sessions.js:3477` → `/api/session/`
- `static/js/sessions.js:3478` → `/api/session/`
- `static/js/sessions.js:3507` → `/api/session/`
- `static/js/sessions.js:3508` → `/api/session/`
- `static/js/sessions.js:3546` → `/api/document/`
- `static/js/sessions.js:3585` → `/api/research/report/`
- `static/js/sessions.js:3592` → `/api/research/report/`
- `static/js/sessions.js:3602` → `/api/research/`
- `static/js/settings.js:1033` → `/api/`
- `static/js/settings.js:2789` → `/api/email/accounts/`
- `static/js/settings.js:2799` → `/api/email/accounts/`
- `static/js/settings.js:2938` → `/api/email/accounts/`
- `static/js/settings.js:2990` → `/api/email/accounts/`
- `static/js/settings.js:3041` → `/api/email/style${emailAccountSuffix()}`
- `static/js/settings.js:3157` → `/api/email/extract-style${emailAccountSuffix()}`
- `static/js/settings.js:3185` → `/api/email/style${emailAccountSuffix()}`
- `static/js/settings.js:3356` → `/api/auth/integrations/`
- `static/js/settings.js:3382` → `/api/auth/integrations/`
- `static/js/settings.js:3396` → `/api/auth/integrations/`
- `static/js/settings.js:3468` → `/api/claude/plugin.zip`
- `static/js/settings.js:3473` → `/api/claude/plugin.zip`
- `static/js/settings.js:3643` → `/api/auth/integrations/`
- `static/js/settings.js:3644` → `/api/calendar/config/accounts/`
- `static/js/settings.js:3651` → `/api/email/accounts/`
- `static/js/settings.js:3652` → `/api/mcp/servers/`
- `static/js/settings.js:3653` → `/api/tokens/`
- `static/js/settings.js:3845` → `/api/auth/integrations/`
- `static/js/settings.js:3864` → `/api/auth/integrations/`
- `static/js/settings.js:3961` → `/api/calendar/config/accounts/`
- `static/js/settings.js:4259` → `/api/contacts/`
- `static/js/settings.js:4269` → `/api/contacts/`
- `static/js/settings.js:4576` → `/api/email/accounts/`
- `static/js/settings.js:4759` → `/api/email/accounts/`
- `static/js/settings.js:4940` → `/api/mcp/oauth/exchange/`
- `static/js/settings.js:5001` → `/api/mcp/oauth/authorize/`
- `static/js/settings.js:5012` → `/api/mcp/servers/`
- `static/js/settings.js:5022` → `/api/mcp/servers/`
- `static/js/settings.js:5031` → `/api/mcp/servers/`
- `static/js/settings.js:5039` → `/api/mcp/servers/`
- `static/js/settings.js:5274` → `/api/tokens/`
- `static/js/settings.js:5293` → `/api/tokens/`
- `static/js/settings.js:5334` → `/api/tokens/`
- `static/js/settings.js:5360` → `/api/tokens/`
- `static/js/settings.js:5536` → `/api/tokens/`
- `static/js/signature.js:349` → `/api/signatures/`
- `static/js/skills.js:39` → `/api/skills/`
- `static/js/skills.js:92` → `/api/skills`
- `static/js/skills.js:551` → `/api/skills/builtin/`
- `static/js/skills.js:585` → `/api/skills/builtin/`
- `static/js/skills.js:600` → `/api/skills/builtin/`
- `static/js/skills.js:1062` → `/api/skills/`
- `static/js/skills.js:1087` → `/api/skills/`
- `static/js/skills.js:1103` → `/api/skills/`
- `static/js/skills.js:1117` → `/api/skills/`
- `static/js/skills.js:1164` → `/api/skills/`
- `static/js/skills.js:1222` → `/api/skills/`
- `static/js/skills.js:1742` → `/api/skills/`
- `static/js/skills.js:1761` → `/api/prefs`
- `static/js/skills.js:1800` → `/api/skills/`
- `static/js/skills.js:1825` → `/api/skills/`
- `static/js/skills.js:1851` → `/api/skills/`
- `static/js/skills.js:1890` → `/api/skills/`
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
- `static/js/slashCommands.js:1573` → `/api/memory`
- `static/js/slashCommands.js:1602` → `/api/memory`
- `static/js/slashCommands.js:1612` → `/api/memory/`
- `static/js/slashCommands.js:1624` → `/api/memory`
- `static/js/slashCommands.js:1629` → `/api/memory/`
- `static/js/slashCommands.js:1692` → `/api/skills/`
- `static/js/slashCommands.js:1720` → `/api/notes`
- `static/js/slashCommands.js:1814` → `/api/notes?note_type=note`
- `static/js/slashCommands.js:1826` → `/api/notes`
- `static/js/slashCommands.js:1891` → `/api/personal`
- `static/js/slashCommands.js:1928` → `/api/personal`
- `static/js/slashCommands.js:2067` → `/api/session/`
- `static/js/slashCommands.js:5176` → `/api/memory`
- `static/js/tasks.js:45` → `/api/tasks`
- `static/js/tasks.js:74` → `/api/tasks`
- `static/js/tasks.js:85` → `/api/tasks/`
- `static/js/tasks.js:96` → `/api/tasks/`
- `static/js/tasks.js:137` → `/api/tasks/`
- `static/js/tasks.js:144` → `/api/tasks/`
- `static/js/tasks.js:151` → `/api/tasks/`
- `static/js/tasks.js:169` → `/api/tasks/`
- `static/js/tasks.js:184` → `/api/tasks/`
- `static/js/tasks.js:1490` → `/api/tasks/`
- `static/js/tasks.js:1914` → `/api/tasks/`
- `static/js/tasks.js:1928` → `/api/tasks/`
- `static/js/tasks.js:2389` → `/api/research/report/`
- `static/js/tasks.js:2576` → `/api/session/`
- `static/sw.js:190` → `/api/`
