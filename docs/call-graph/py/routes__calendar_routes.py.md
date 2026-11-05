# `routes/calendar_routes.py` — definitions & call sites

54 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_ics_naive_dtstart` — function, line 24
- **called from:**
- `routes/calendar_routes.py:1642`
- `src/email_calendar_import.py:81`
- `tests/test_ics_import_dedup_tz.py:22`
- `tests/test_ics_import_dedup_tz.py:27`
- `tests/test_ics_import_dedup_tz.py:32`
- `tests/test_ics_import_dedup_tz.py:36`
- `tests/test_ics_import_dedup_tz.py:43`

## `_ensure_positive_duration` — function, line 41
- **called from:**
- `routes/calendar_routes.py:1659`
- `routes/calendar_routes.py:1699`
- `src/caldav_sync.py:399`
- `tests/test_calendar_import_zero_duration.py:45`
- `tests/test_calendar_import_zero_duration.py:50`
- `tests/test_calendar_import_zero_duration.py:53`
- `tests/test_calendar_import_zero_duration.py:59`

## `_require_user` — function, line 69
- **called from:**
- `routes/calendar_routes.py:984`
- `routes/calendar_routes.py:1008`
- `routes/calendar_routes.py:1038`
- `routes/calendar_routes.py:1063`
- `routes/calendar_routes.py:1088`
- `routes/calendar_routes.py:1115`
- `routes/calendar_routes.py:1129`
- `routes/calendar_routes.py:1228`
- `routes/calendar_routes.py:1235`
- `routes/calendar_routes.py:1255`
- `routes/calendar_routes.py:1278`
- `routes/calendar_routes.py:1344`
- `routes/calendar_routes.py:1415`
- `routes/calendar_routes.py:1426`
- `routes/calendar_routes.py:1489`
- `routes/calendar_routes.py:1534`
- `routes/calendar_routes.py:1557`
- `routes/calendar_routes.py:1587`
- `routes/calendar_routes.py:1741`
- `routes/calendar_routes.py:1806`
- `routes/research/research_routes.py:264`
- `routes/research/research_routes.py:288`
- `routes/research/research_routes.py:323`
- `routes/research/research_routes.py:332`
- `routes/research/research_routes.py:376`
- `routes/research/research_routes.py:397`
- `routes/research/research_routes.py:408`
- `routes/research/research_routes.py:424`
- `routes/research/research_routes.py:477`
- `routes/research/research_routes.py:492`
- `routes/research/research_routes.py:510`
- `routes/research/research_routes.py:655`
- `routes/research/research_routes.py:662`
- `routes/research/research_routes.py:717`
- `routes/research/research_routes.py:767`

## `_json_object_body` — function (async), line 83
- **called from:**
- `routes/calendar_routes.py:1009`
- `routes/calendar_routes.py:1064`
- `routes/calendar_routes.py:1089`
- `routes/calendar_routes.py:1130`
- `tests/test_calendar_config_body.py:19`

## `_get_or_404_calendar` — function, line 95
- **called from:**
- `routes/calendar_routes.py:1238`
- `routes/calendar_routes.py:1561`
- `routes/calendar_routes.py:1744`
- `tests/test_null_owner_gates.py:75`
- `tests/test_null_owner_gates.py:85`
- `tests/test_null_owner_gates.py:94`

## `_get_or_404_event` — function, line 109
- **called from:**
- `routes/calendar_routes.py:184`
- `routes/calendar_routes.py:1419`
- `routes/calendar_routes.py:1434`
- `routes/calendar_routes.py:1496`
- `tests/test_null_owner_gates.py:105`
- `tests/test_null_owner_gates.py:116`

## `_ics_escape` — function, line 119
- **called from:**
- `routes/calendar_routes.py:1754`
- `routes/calendar_routes.py:1759`
- `routes/calendar_routes.py:1768`
- `routes/calendar_routes.py:1770`
- `tests/test_ics_export_escaping.py:33`
- `tests/test_ics_export_escaping.py:38`
- `tests/test_ics_export_escaping.py:47`
- `tests/test_ics_export_escaping.py:49`

## `_safe_ics_filename` — function, line 137
- **called from:**
- `routes/calendar_routes.py:1777`

## `_resolve_base_uid` — function, line 146
- **called from:**
- `routes/calendar_routes.py:1418`
- `routes/calendar_routes.py:1429`
- `routes/calendar_routes.py:1491`
- `src/tools/calendar.py:679`
- `src/tools/calendar.py:821`
- `tests/test_calendar_recurrence.py:20`
- `tests/test_calendar_recurrence.py:25`
- `tests/test_calendar_recurrence.py:30`
- `tests/test_calendar_recurrence.py:36`
- `tests/test_calendar_recurrence.py:42`

## `_push_caldav_event_after_commit` — function (async), line 163
- **called from:**
- `routes/calendar_routes.py:1397`
- `routes/calendar_routes.py:1472`
- `routes/calendar_routes.py:1513`
- `routes/calendar_routes.py:1521`
- `src/email_calendar_import.py:148`
- `src/email_calendar_import.py:150`
- `src/email_calendar_import.py:183`
- `src/email_calendar_import.py:185`
- `src/tools/calendar.py:643`
- `src/tools/calendar.py:789`
- `src/tools/calendar.py:837`

## `_record_caldav_delete_tombstone` — function, line 193
- **called from:**
- `routes/calendar_routes.py:1516`
- `src/tools/calendar.py:832`

## `EventCreate` — class, line 212
- **called from:**
- `routes/codex_routes.py:481`
- `tests/test_caldav_writeback_route.py:81`
- `tests/test_caldav_writeback_route.py:91`
- `tests/test_caldav_writeback_route.py:101`
- `tests/test_calendar_default_transaction.py:92`
- `tests/test_calendar_default_transaction.py:107`
- `tests/test_calendar_owner_scope.py:236`
- `tests/test_calendar_owner_scope.py:258`
- `tests/test_upload_handler_cleanup.py:789`

## `EventUpdate` — class, line 225
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_default_calendar_id` — function, line 242
- **called from:**
- `routes/calendar_routes.py:306`
- `tests/test_calendar_default_transaction.py:183`
- `tests/test_calendar_default_transaction.py:192`
- `tests/test_calendar_default_transaction.py:201`
- `tests/test_calendar_default_transaction.py:206`
- `tests/test_calendar_default_transaction.py:207`
- `tests/test_calendar_default_transaction.py:208`
- `tests/test_calendar_default_transaction.py:228`
- `tests/test_calendar_default_transaction.py:270`
- `tests/test_calendar_default_transaction.py:299`
- `tests/test_calendar_default_transaction.py:304`
- `tests/test_calendar_default_transaction.py:325`
- `tests/test_calendar_default_transaction.py:346`
- `tests/test_calendar_default_transaction.py:358`
- `tests/test_calendar_default_transaction.py:406`
- `tests/test_calendar_default_transaction.py:459`
- `tests/test_calendar_default_transaction.py:480`
- `tests/test_calendar_default_transaction.py:502`
- `tests/test_calendar_default_transaction.py:532`
- `tests/test_calendar_default_transaction.py:533`

## `_begin_sqlite_default_write` — function, line 261
- **called from:**
- `routes/calendar_routes.py:298`

## `_ensure_default_calendar` — function, line 281
- **called from:**
- `routes/calendar_routes.py:1258`
- `routes/calendar_routes.py:1359`
- `src/tools/calendar.py:339`
- `src/tools/calendar.py:472`
- `tests/test_calendar_default_transaction.py:182`
- `tests/test_calendar_default_transaction.py:191`
- `tests/test_calendar_default_transaction.py:200`
- `tests/test_calendar_default_transaction.py:255`
- `tests/test_calendar_default_transaction.py:324`
- `tests/test_calendar_default_transaction.py:357`
- `tests/test_calendar_default_transaction.py:434`
- `tests/test_calendar_default_transaction.py:447`
- `tests/test_calendar_default_transaction.py:477`
- `tests/test_calendar_default_transaction.py:513`

## `parse_due_for_user` — function, line 374
- **called from:**
- `src/tools/calendar.py:264`
- `tests/test_parse_due_time_first.py:37`
- `tests/test_parse_due_time_first.py:43`
- `tests/test_parse_due_time_first.py:49`
- `tests/test_parse_due_time_first.py:55`
- `tests/test_parse_due_time_first.py:62`
- `tests/test_redos_residual_python.py:170`
- `tests/test_redos_residual_python.py:171`
- `tests/test_user_time.py:258`
- `tests/test_user_time.py:279`

## `_parse_time` — function, line 423
- **called from:**
- `routes/calendar_routes.py:443`
- `routes/calendar_routes.py:454`
- `routes/calendar_routes.py:465`
- `routes/calendar_routes.py:571`
- `routes/calendar_routes.py:585`
- `routes/calendar_routes.py:599`
- `routes/calendar_routes.py:616`

## `_parse_dt_pair` — function, line 481
- **called from:**
- `routes/calendar_routes.py:1365`
- `routes/calendar_routes.py:1367`
- `routes/calendar_routes.py:1442`
- `routes/calendar_routes.py:1449`
- `src/tools/calendar.py:264`
- `tests/test_calendar_parse_dt_naive.py:38`

## `_parse_dt` — function, line 505
- **called from:**
- `routes/calendar_routes.py:406`
- `routes/calendar_routes.py:478`
- `routes/calendar_routes.py:502`
- `routes/calendar_routes.py:1280`
- `routes/calendar_routes.py:1281`
- `tests/test_calendar_parse_dt_naive.py:29`
- `tests/test_calendar_parse_dt_naive.py:44`
- `tests/test_calendar_parse_dt_time_first.py:15`
- `tests/test_calendar_parse_dt_time_first.py:15`
- `tests/test_calendar_parse_dt_time_first.py:19`
- `tests/test_calendar_parse_dt_time_first.py:19`
- `tests/test_calendar_parse_dt_time_first.py:23`
- `tests/test_calendar_parse_dt_time_first.py:23`
- `tests/test_calendar_parse_dt_time_first.py:27`
- `tests/test_calendar_parse_dt_time_first.py:27`
- `tests/test_calendar_parse_dt_time_first.py:31`
- `tests/test_calendar_parse_dt_time_first.py:31`
- `tests/test_calendar_parse_dt_tonight.py:15`
- `tests/test_calendar_parse_dt_tonight.py:16`
- `tests/test_calendar_parse_dt_tonight.py:22`
- `tests/test_calendar_parse_dt_tonight.py:22`
- `tests/test_calendar_parse_dt_tonight.py:26`
- `tests/test_calendar_parse_dt_tonight.py:26`
- `tests/test_redos_residual_python.py:168`

## `_parse_time` — function, line 543
- **called from:**
- `routes/calendar_routes.py:443`
- `routes/calendar_routes.py:454`
- `routes/calendar_routes.py:465`
- `routes/calendar_routes.py:571`
- `routes/calendar_routes.py:585`
- `routes/calendar_routes.py:599`
- `routes/calendar_routes.py:616`

## `_note_due_datetime` — function, line 638
- **called from:**
- `routes/calendar_routes.py:689`

## `_calendar_reminder_for_event` — function, line 653
- **called from:**
- `routes/calendar_routes.py:780`
- `src/tools/calendar.py:795`

## `_delete_calendar_reminders_for_event` — function, line 707
- **called from:**
- `routes/calendar_routes.py:1463`
- `routes/calendar_routes.py:1517`
- `src/email_calendar_import.py:129`
- `src/email_calendar_import.py:144`
- `src/tools/calendar.py:766`
- `src/tools/calendar.py:833`
- `tests/test_calendar_rrule.py:134`

## `_create_calendar_reminder_for_event` — function, line 731
- **called from:**
- `routes/calendar_routes.py:1393`
- `routes/calendar_routes.py:1465`

## `_event_to_dict` — function, line 764
- **called from:**
- `routes/calendar_routes.py:854`
- `routes/calendar_routes.py:880`
- `routes/calendar_routes.py:898`
- `routes/calendar_routes.py:1401`
- `routes/calendar_routes.py:1420`
- `routes/calendar_routes.py:1475`
- `src/tools/calendar.py:410`
- `tests/test_calendar_rrule.py:93`

## `_recurrence_exdates` — function, line 813
- **called from:**
- `routes/calendar_routes.py:791`
- `routes/calendar_routes.py:899`
- `routes/calendar_routes.py:1505`
- `src/email_calendar_import.py:123`
- `src/email_calendar_import.py:177`

## `_occurrence_exdate_key` — function, line 826
- **called from:**
- `routes/calendar_routes.py:1502`

## `_expand_rrule` — function, line 835
- **called from:**
- `routes/calendar_routes.py:1325`
- `tests/test_calendar_recurrence.py:79`
- `tests/test_calendar_recurrence.py:97`
- `tests/test_calendar_recurrence.py:121`
- `tests/test_calendar_recurrence.py:147`
- `tests/test_calendar_recurrence.py:166`
- `tests/test_calendar_recurrence.py:183`
- `tests/test_calendar_recurrence.py:199`
- `tests/test_calendar_recurrence.py:221`
- `tests/test_calendar_recurrence.py:238`
- `tests/test_calendar_recurrence.py:254`
- `tests/test_calendar_recurrence.py:269`
- `tests/test_calendar_recurrence.py:286`
- `tests/test_calendar_recurrence.py:304`
- `tests/test_calendar_recurrence.py:323`
- `tests/test_calendar_recurrence.py:346`
- `tests/test_calendar_recurrence.py:365`
- `tests/test_calendar_recurrence.py:384`
- `tests/test_calendar_rrule_until_utc.py:61`

## `setup_calendar_routes` — function, line 954
- **called from:**
- `app.py:879`
- `tests/test_caldav_test_connection_ssl.py:41`
- `tests/test_caldav_writeback_route.py:60`
- `tests/test_calendar_default_transaction.py:71`
- `tests/test_calendar_import_zero_duration.py:83`
- `tests/test_calendar_owner_scope.py:192`
- `tests/test_upload_handler_cleanup.py:781`

## `_reserve_calendar_uploads` — function, line 957
- **called from:**
- `routes/calendar_routes.py:1345`
- `routes/calendar_routes.py:1427`
- `routes/calendar_routes.py:1535`
- `routes/calendar_routes.py:1558`

## `_get_caldav_accounts` — function, line 968
- **called from:**
- `routes/calendar_routes.py:985`
- `routes/calendar_routes.py:1010`
- `routes/calendar_routes.py:1039`
- `routes/calendar_routes.py:1080`
- `routes/calendar_routes.py:1090`
- `routes/calendar_routes.py:1116`
- `routes/calendar_routes.py:1136`

## `_save_caldav_accounts` — function, line 972
- **called from:**
- `routes/calendar_routes.py:1012`
- `routes/calendar_routes.py:1030`
- `routes/calendar_routes.py:1082`
- `routes/calendar_routes.py:1109`
- `routes/calendar_routes.py:1120`

## `get_config` — function (async), line 982
- **route:** `GET /config`
- decorator: `router.get("/config")`
- **called from:**
- `tests/test_email_oauth.py:911`

## `save_config` — function (async), line 1006
- **route:** `POST /config`
- decorator: `router.post("/config")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_caldav_accounts` — function (async), line 1036
- **route:** `GET /config/accounts`
- decorator: `router.get("/config/accounts")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_caldav_account` — function (async), line 1060
- **route:** `POST /config/accounts`
- decorator: `router.post("/config/accounts")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_caldav_account` — function (async), line 1086
- **route:** `PUT /config/accounts/{account_id}`
- decorator: `router.put("/config/accounts/{account_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_caldav_account` — function (async), line 1113
- **route:** `DELETE /config/accounts/{account_id}`
- decorator: `router.delete("/config/accounts/{account_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_connection` — function (async), line 1124
- **route:** `POST /test`
- decorator: `router.post("/test")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `sync_caldav_endpoint` — function (async), line 1224
- **route:** `POST /sync`
- decorator: `router.post("/sync")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_calendar` — function (async), line 1234
- **route:** `DELETE /calendars/{cal_id}`
- decorator: `router.delete("/calendars/{cal_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_calendars` — function (async), line 1254
- **route:** `GET /calendars`
- decorator: `router.get("/calendars")`
- **called from:**
- `tests/test_calendar_default_transaction.py:153`

## `list_events` — function (async), line 1277
- **route:** `GET /events`
- decorator: `router.get("/events")`
- **called from:**
- `tests/test_calendar_owner_scope.py:292`

## `create_event` — function (async), line 1343
- **route:** `POST /events`
- decorator: `router.post("/events")`
- **called from:**
- `tests/test_caldav_writeback_route.py:81`
- `tests/test_caldav_writeback_route.py:91`
- `tests/test_caldav_writeback_route.py:101`
- `tests/test_calendar_default_transaction.py:90`
- `tests/test_calendar_default_transaction.py:105`
- `tests/test_calendar_owner_scope.py:234`
- `tests/test_calendar_owner_scope.py:256`
- `tests/test_upload_handler_cleanup.py:787`

## `get_event` — function (async), line 1414
- **route:** `GET /events/{uid}`
- decorator: `router.get("/events/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_event` — function (async), line 1425
- **route:** `PUT /events/{uid}`
- decorator: `router.put("/events/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_event` — function (async), line 1488
- **route:** `DELETE /events/{uid}`
- decorator: `router.delete("/events/{uid}")`
- **called from:**
- `tests/test_caldav_writeback_route.py:105`

## `create_calendar` — function (async), line 1533
- **route:** `POST /calendars`
- decorator: `router.post("/calendars")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_calendar` — function (async), line 1556
- **route:** `PUT /calendars/{cal_id}`
- decorator: `router.put("/calendars/{cal_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `import_ics` — function (async), line 1583
- **route:** `POST /import`
- decorator: `router.post("/import")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `export_ics` — function (async), line 1737
- **route:** `GET /export/{cal_id}`
- decorator: `router.get("/export/{cal_id}")`
- **called from:**
- `tests/test_calendar_owner_scope.py:311`
- `tests/test_calendar_owner_scope.py:325`
- `tests/test_calendar_owner_scope.py:340`

## `quick_parse` — function (async), line 1795
- **route:** `POST /quick-parse`
- decorator: `router.post("/quick-parse")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_strip_tz` — function, line 1912
- **called from:**
- `routes/calendar_routes.py:1922`
- `routes/calendar_routes.py:1923`
