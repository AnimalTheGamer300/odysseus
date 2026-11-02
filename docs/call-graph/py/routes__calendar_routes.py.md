# `routes/calendar_routes.py` — definitions & call sites

48 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_ics_naive_dtstart` — function, line 24
- **called from:**
- `routes/calendar_routes.py:1470`
- `tests/test_ics_import_dedup_tz.py:22`
- `tests/test_ics_import_dedup_tz.py:27`
- `tests/test_ics_import_dedup_tz.py:32`
- `tests/test_ics_import_dedup_tz.py:36`
- `tests/test_ics_import_dedup_tz.py:43`

## `_ensure_positive_duration` — function, line 41
- **called from:**
- `routes/calendar_routes.py:1487`
- `routes/calendar_routes.py:1526`
- `src/caldav_sync.py:399`
- `tests/test_calendar_import_zero_duration.py:45`
- `tests/test_calendar_import_zero_duration.py:50`
- `tests/test_calendar_import_zero_duration.py:53`
- `tests/test_calendar_import_zero_duration.py:59`

## `_require_user` — function, line 69
- **called from:**
- `routes/calendar_routes.py:835`
- `routes/calendar_routes.py:859`
- `routes/calendar_routes.py:892`
- `routes/calendar_routes.py:917`
- `routes/calendar_routes.py:945`
- `routes/calendar_routes.py:975`
- `routes/calendar_routes.py:989`
- `routes/calendar_routes.py:1091`
- `routes/calendar_routes.py:1098`
- `routes/calendar_routes.py:1118`
- `routes/calendar_routes.py:1141`
- `routes/calendar_routes.py:1207`
- `routes/calendar_routes.py:1269`
- `routes/calendar_routes.py:1321`
- `routes/calendar_routes.py:1363`
- `routes/calendar_routes.py:1386`
- `routes/calendar_routes.py:1416`
- `routes/calendar_routes.py:1566`
- `routes/calendar_routes.py:1631`
- `routes/research/research_routes.py:262`
- `routes/research/research_routes.py:280`
- `routes/research/research_routes.py:291`
- `routes/research/research_routes.py:300`
- `routes/research/research_routes.py:326`
- `routes/research/research_routes.py:347`
- `routes/research/research_routes.py:358`
- `routes/research/research_routes.py:374`
- `routes/research/research_routes.py:425`
- `routes/research/research_routes.py:440`
- `routes/research/research_routes.py:458`
- `routes/research/research_routes.py:582`
- `routes/research/research_routes.py:616`
- `routes/research/research_routes.py:645`

## `_get_or_404_calendar` — function, line 83
- **called from:**
- `routes/calendar_routes.py:1101`
- `routes/calendar_routes.py:1390`
- `routes/calendar_routes.py:1569`
- `tests/test_null_owner_gates.py:75`
- `tests/test_null_owner_gates.py:85`
- `tests/test_null_owner_gates.py:94`

## `_get_or_404_event` — function, line 97
- **called from:**
- `routes/calendar_routes.py:172`
- `routes/calendar_routes.py:1277`
- `routes/calendar_routes.py:1328`
- `tests/test_null_owner_gates.py:105`
- `tests/test_null_owner_gates.py:116`

## `_ics_escape` — function, line 107
- **called from:**
- `routes/calendar_routes.py:1579`
- `routes/calendar_routes.py:1584`
- `routes/calendar_routes.py:1593`
- `routes/calendar_routes.py:1595`
- `tests/test_ics_export_escaping.py:33`
- `tests/test_ics_export_escaping.py:38`
- `tests/test_ics_export_escaping.py:47`
- `tests/test_ics_export_escaping.py:49`

## `_safe_ics_filename` — function, line 125
- **called from:**
- `routes/calendar_routes.py:1602`

## `_resolve_base_uid` — function, line 134
- **called from:**
- `routes/calendar_routes.py:1272`
- `routes/calendar_routes.py:1323`
- `src/tools/calendar.py:481`
- `src/tools/calendar.py:542`
- `tests/test_calendar_recurrence.py:20`
- `tests/test_calendar_recurrence.py:25`
- `tests/test_calendar_recurrence.py:30`
- `tests/test_calendar_recurrence.py:36`
- `tests/test_calendar_recurrence.py:42`

## `_push_caldav_event_after_commit` — function (async), line 151
- **called from:**
- `routes/calendar_routes.py:1256`
- `routes/calendar_routes.py:1308`
- `routes/calendar_routes.py:1343`
- `routes/calendar_routes.py:1350`
- `src/tools/calendar.py:456`
- `src/tools/calendar.py:534`
- `src/tools/calendar.py:554`

## `_record_caldav_delete_tombstone` — function, line 181
- **called from:**
- `routes/calendar_routes.py:1346`
- `src/tools/calendar.py:550`

## `EventCreate` — class, line 200
- **called from:**
- `routes/codex_routes.py:435`
- `tests/test_caldav_writeback_route.py:81`
- `tests/test_caldav_writeback_route.py:91`
- `tests/test_caldav_writeback_route.py:101`
- `tests/test_calendar_default_transaction.py:92`
- `tests/test_calendar_default_transaction.py:107`
- `tests/test_calendar_owner_scope.py:236`
- `tests/test_calendar_owner_scope.py:258`
- `tests/test_upload_handler_cleanup.py:789`

## `EventUpdate` — class, line 212
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_default_calendar_id` — function, line 228
- **called from:**
- `routes/calendar_routes.py:292`
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

## `_begin_sqlite_default_write` — function, line 247
- **called from:**
- `routes/calendar_routes.py:284`

## `_ensure_default_calendar` — function, line 267
- **called from:**
- `routes/calendar_routes.py:1121`
- `routes/calendar_routes.py:1222`
- `src/tools/calendar.py:198`
- `src/tools/calendar.py:329`
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

## `parse_due_for_user` — function, line 360
- **called from:**
- `src/tools/calendar.py:146`
- `tests/test_parse_due_time_first.py:37`
- `tests/test_parse_due_time_first.py:43`
- `tests/test_parse_due_time_first.py:49`
- `tests/test_parse_due_time_first.py:55`
- `tests/test_parse_due_time_first.py:62`
- `tests/test_user_time.py:208`
- `tests/test_user_time.py:229`

## `_parse_time` — function, line 409
- **called from:**
- `routes/calendar_routes.py:429`
- `routes/calendar_routes.py:440`
- `routes/calendar_routes.py:451`
- `routes/calendar_routes.py:557`
- `routes/calendar_routes.py:571`
- `routes/calendar_routes.py:585`
- `routes/calendar_routes.py:602`

## `_parse_dt_pair` — function, line 467
- **called from:**
- `routes/calendar_routes.py:1228`
- `routes/calendar_routes.py:1230`
- `routes/calendar_routes.py:1285`
- `routes/calendar_routes.py:1292`
- `src/tools/calendar.py:146`
- `tests/test_calendar_parse_dt_naive.py:38`

## `_parse_dt` — function, line 491
- **called from:**
- `routes/calendar_routes.py:392`
- `routes/calendar_routes.py:464`
- `routes/calendar_routes.py:488`
- `routes/calendar_routes.py:1143`
- `routes/calendar_routes.py:1144`
- `src/tools/calendar.py:231`
- `src/tools/calendar.py:235`
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

## `_parse_time` — function, line 529
- **called from:**
- `routes/calendar_routes.py:429`
- `routes/calendar_routes.py:440`
- `routes/calendar_routes.py:451`
- `routes/calendar_routes.py:557`
- `routes/calendar_routes.py:571`
- `routes/calendar_routes.py:585`
- `routes/calendar_routes.py:602`

## `_event_to_dict` — function, line 624
- **called from:**
- `routes/calendar_routes.py:705`
- `routes/calendar_routes.py:731`
- `routes/calendar_routes.py:749`

## `_recurrence_exdates` — function, line 664
- **called from:**
- `routes/calendar_routes.py:650`
- `routes/calendar_routes.py:750`
- `routes/calendar_routes.py:1335`

## `_occurrence_exdate_key` — function, line 677
- **called from:**
- `routes/calendar_routes.py:1332`

## `_expand_rrule` — function, line 686
- **called from:**
- `routes/calendar_routes.py:1188`
- `tests/test_calendar_recurrence.py:79`
- `tests/test_calendar_recurrence.py:97`
- `tests/test_calendar_recurrence.py:121`
- `tests/test_calendar_recurrence.py:147`
- `tests/test_calendar_recurrence.py:166`
- `tests/test_calendar_recurrence.py:183`
- `tests/test_calendar_recurrence.py:199`
- `tests/test_calendar_recurrence.py:221`
- `tests/test_calendar_recurrence.py:237`
- `tests/test_calendar_recurrence.py:254`
- `tests/test_calendar_recurrence.py:272`
- `tests/test_calendar_recurrence.py:291`
- `tests/test_calendar_recurrence.py:314`
- `tests/test_calendar_recurrence.py:333`
- `tests/test_calendar_recurrence.py:352`
- `tests/test_calendar_rrule_until_utc.py:61`

## `setup_calendar_routes` — function, line 805
- **called from:**
- `app.py:795`
- `tests/test_caldav_test_connection_ssl.py:41`
- `tests/test_caldav_writeback_route.py:60`
- `tests/test_calendar_default_transaction.py:71`
- `tests/test_calendar_import_zero_duration.py:83`
- `tests/test_calendar_owner_scope.py:192`
- `tests/test_upload_handler_cleanup.py:781`

## `_reserve_calendar_uploads` — function, line 808
- **called from:**
- `routes/calendar_routes.py:1208`
- `routes/calendar_routes.py:1270`
- `routes/calendar_routes.py:1364`
- `routes/calendar_routes.py:1387`

## `_get_caldav_accounts` — function, line 819
- **called from:**
- `routes/calendar_routes.py:836`
- `routes/calendar_routes.py:864`
- `routes/calendar_routes.py:893`
- `routes/calendar_routes.py:937`
- `routes/calendar_routes.py:950`
- `routes/calendar_routes.py:976`
- `routes/calendar_routes.py:999`

## `_save_caldav_accounts` — function, line 823
- **called from:**
- `routes/calendar_routes.py:866`
- `routes/calendar_routes.py:884`
- `routes/calendar_routes.py:939`
- `routes/calendar_routes.py:969`
- `routes/calendar_routes.py:980`

## `get_config` — function (async), line 833
- **route:** `GET /config`
- decorator: `router.get("/config")`
- **called from:**
- `tests/test_email_oauth.py:911`

## `save_config` — function (async), line 857
- **route:** `POST /config`
- decorator: `router.post("/config")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_caldav_accounts` — function (async), line 890
- **route:** `GET /config/accounts`
- decorator: `router.get("/config/accounts")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_caldav_account` — function (async), line 914
- **route:** `POST /config/accounts`
- decorator: `router.post("/config/accounts")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_caldav_account` — function (async), line 943
- **route:** `PUT /config/accounts/{account_id}`
- decorator: `router.put("/config/accounts/{account_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_caldav_account` — function (async), line 973
- **route:** `DELETE /config/accounts/{account_id}`
- decorator: `router.delete("/config/accounts/{account_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_connection` — function (async), line 984
- **route:** `POST /test`
- decorator: `router.post("/test")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `sync_caldav_endpoint` — function (async), line 1087
- **route:** `POST /sync`
- decorator: `router.post("/sync")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_calendar` — function (async), line 1097
- **route:** `DELETE /calendars/{cal_id}`
- decorator: `router.delete("/calendars/{cal_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_calendars` — function (async), line 1117
- **route:** `GET /calendars`
- decorator: `router.get("/calendars")`
- **called from:**
- `tests/test_calendar_default_transaction.py:153`

## `list_events` — function (async), line 1140
- **route:** `GET /events`
- decorator: `router.get("/events")`
- **called from:**
- `tests/test_calendar_owner_scope.py:290`

## `create_event` — function (async), line 1206
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

## `update_event` — function (async), line 1268
- **route:** `PUT /events/{uid}`
- decorator: `router.put("/events/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_event` — function (async), line 1320
- **route:** `DELETE /events/{uid}`
- decorator: `router.delete("/events/{uid}")`
- **called from:**
- `tests/test_caldav_writeback_route.py:105`

## `create_calendar` — function (async), line 1362
- **route:** `POST /calendars`
- decorator: `router.post("/calendars")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_calendar` — function (async), line 1385
- **route:** `PUT /calendars/{cal_id}`
- decorator: `router.put("/calendars/{cal_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `import_ics` — function (async), line 1412
- **route:** `POST /import`
- decorator: `router.post("/import")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `export_ics` — function (async), line 1562
- **route:** `GET /export/{cal_id}`
- decorator: `router.get("/export/{cal_id}")`
- **called from:**
- `tests/test_calendar_owner_scope.py:309`
- `tests/test_calendar_owner_scope.py:323`
- `tests/test_calendar_owner_scope.py:338`

## `quick_parse` — function (async), line 1620
- **route:** `POST /quick-parse`
- decorator: `router.post("/quick-parse")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_strip_tz` — function, line 1737
- **called from:**
- `routes/calendar_routes.py:1747`
- `routes/calendar_routes.py:1748`
