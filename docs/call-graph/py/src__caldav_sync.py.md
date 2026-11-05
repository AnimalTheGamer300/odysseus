# `src/caldav_sync.py` — definitions & call sites

26 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_private_caldav_allowed` — function, line 51
- **called from:**
- `src/caldav_sync.py:66`

## `_validate_caldav_address` — function, line 55
- **called from:**
- `src/caldav_sync.py:75`
- `src/caldav_sync.py:103`

## `_validate_caldav_ip` — function, line 70
- **called from:**
- `src/caldav_sync.py:127`

## `_resolve_caldav_host_ips` — function, line 78
- **called from:**
- `src/caldav_sync.py:97`

## `_validate_caldav_hostname` — function, line 90
- **called from:**
- `src/caldav_sync.py:128`

## `validate_caldav_url` — function, line 106
- **called from:**
- `routes/calendar_routes.py:1016`
- `routes/calendar_routes.py:1067`
- `routes/calendar_routes.py:1098`
- `routes/calendar_routes.py:1157`
- `src/caldav_sync.py:644`
- `src/caldav_writeback.py:295`
- `tests/test_caldav_url_hardening.py:19`
- `tests/test_caldav_url_hardening.py:39`
- `tests/test_caldav_url_hardening.py:45`
- `tests/test_caldav_url_hardening.py:48`
- `tests/test_caldav_url_hardening.py:60`
- `tests/test_caldav_url_hardening.py:72`
- `tests/test_caldav_url_hardening.py:82`
- `tests/test_caldav_url_hardening.py:92`
- `tests/test_caldav_url_hardening.py:115`
- `tests/test_caldav_url_nonstring.py:19`
- `tests/test_caldav_url_nonstring.py:21`
- `tests/test_caldav_url_nonstring.py:30`

## `_event_etag` — function, line 132
- **called from:**
- `src/caldav_sync.py:434`
- `src/caldav_sync.py:450`

## `_stable_cal_id` — function, line 143
- **called from:**
- `src/caldav_sync.py:317`
- `src/caldav_writeback.py:95`
- `tests/test_caldav_writeback.py:21`

## `_to_utc_naive` — function, line 154
- **called from:**
- `src/caldav_sync.py:386`
- `src/caldav_sync.py:390`
- `src/task_scheduler.py:204`
- `src/task_scheduler.py:210`
- `src/task_scheduler.py:234`
- `src/task_scheduler.py:243`
- `src/task_scheduler.py:270`

## `_find_existing_event` — function, line 166
- **called from:**
- `src/caldav_sync.py:418`
- `tests/test_caldav_sync_uid_scope.py:49`
- `tests/test_caldav_sync_uid_scope.py:51`
- `tests/test_caldav_sync_uid_scope.py:62`
- `tests/test_caldav_sync_uid_scope.py:74`

## `_google_caldav_events_url` — function, line 185
- **called from:**
- `src/caldav_sync.py:227`
- `tests/test_caldav_google_principal_url.py:135`
- `tests/test_caldav_google_principal_url.py:137`
- `tests/test_caldav_google_principal_url.py:139`
- `tests/test_caldav_google_principal_url.py:140`
- `tests/test_caldav_google_principal_url.py:147`
- `tests/test_caldav_google_principal_url.py:148`
- `tests/test_caldav_google_principal_url.py:150`

## `_open_url_as_calendar` — function, line 220
- **called from:**
- `src/caldav_sync.py:297`
- `src/caldav_sync.py:304`

## `_build_dav_client` — function, line 231
- **called from:**
- `src/caldav_sync.py:282`
- `src/caldav_writeback.py:194`
- `tests/test_caldav_redirect_hardening.py:24`
- `tests/test_caldav_redirect_hardening.py:79`

## `_should_prune_window` — function, line 257
- **called from:**
- `src/caldav_sync.py:469`
- `tests/test_caldav_prune_parse_failure.py:19`
- `tests/test_caldav_prune_parse_failure.py:24`
- `tests/test_caldav_prune_parse_failure.py:30`
- `tests/test_caldav_prune_parse_failure.py:37`

## `_sync_blocking` — function, line 271
- **called from:**
- `tests/test_caldav_client_cleanup.py:64`
- `tests/test_caldav_client_cleanup.py:84`
- `tests/test_caldav_client_cleanup.py:143`
- `tests/test_caldav_google_principal_url.py:157`

## `_event_payload` — function, line 495
- **called from:**
- `src/caldav_sync.py:523`

## `_load_event_for_writeback` — function, line 510
- **called from:**
- `src/caldav_sync.py:660`

## `_load_delete_for_writeback` — function, line 528
- **called from:**
- `src/caldav_sync.py:673`

## `_pending_writeback_uids` — function, line 553
- **called from:**
- `src/caldav_sync.py:683`

## `_load_caldav_accounts` — function, line 582
- **called from:**
- `routes/calendar_routes.py:970`
- `src/caldav_sync.py:622`
- `src/caldav_writeback.py:268`

## `sync_caldav` — function (async), line 617
- **called from:**
- `src/caldav_sync.py:710`
- `src/caldav_sync.py:715`
- `tests/test_caldav_url_hardening.py:159`

## `push_event_create` — function (async), line 659
- **called from:**
- `routes/calendar_routes.py:170`
- `src/caldav_sync.py:669`

## `push_event_update` — function (async), line 668
- **called from:**
- `routes/calendar_routes.py:173`
- `src/caldav_sync.py:686`

## `push_event_delete` — function (async), line 672
- **called from:**
- `routes/calendar_routes.py:176`
- `src/caldav_sync.py:696`

## `push_pending_events` — function (async), line 681
- **called from:**
- `src/caldav_sync.py:712`
- `src/caldav_sync.py:714`

## `sync_caldav_direction` — function (async), line 707
- **called from:**
- `routes/calendar_routes.py:1230`
