# `src/caldav_writeback.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_stable_cal_id` — function, line 26
- **called from:**
- `src/caldav_sync.py:317`
- `src/caldav_writeback.py:95`
- `tests/test_caldav_writeback.py:21`

## `build_event_ical` — function, line 32
- **called from:**
- `src/caldav_writeback.py:153`
- `tests/test_caldav_bidirectional_sync.py:16`
- `tests/test_caldav_writeback.py:67`
- `tests/test_caldav_writeback.py:77`
- `tests/test_caldav_writeback.py:82`

## `find_remote_calendar` — function, line 88
- **called from:**
- `src/caldav_writeback.py:132`
- `tests/test_caldav_writeback.py:88`
- `tests/test_caldav_writeback.py:90`

## `_resource_href` — function, line 102
- **called from:**
- `src/caldav_writeback.py:149`
- `src/caldav_writeback.py:161`
- `src/caldav_writeback.py:169`

## `_resource_etag` — function, line 109
- **called from:**
- `src/caldav_writeback.py:150`
- `src/caldav_writeback.py:162`
- `src/caldav_writeback.py:170`

## `push_event` — function, line 119
- **called from:**
- `src/caldav_writeback.py:199`
- `tests/test_caldav_writeback.py:95`
- `tests/test_caldav_writeback.py:105`
- `tests/test_caldav_writeback.py:116`
- `tests/test_caldav_writeback.py:122`
- `tests/test_caldav_writeback.py:128`
- `tests/test_caldav_writeback.py:134`

## `_discover_calendars` — function, line 174
- **called from:**
- `src/caldav_writeback.py:196`

## `_writeback_blocking` — function, line 189
- **called from:**
- `tests/test_caldav_client_cleanup.py:98`
- `tests/test_caldav_client_cleanup.py:115`

## `_persist_writeback_result` — function, line 205
- **called from:**
- `src/caldav_writeback.py:303`
- `src/caldav_writeback.py:310`
- `tests/test_caldav_bidirectional_sync.py:140`
- `tests/test_caldav_bidirectional_sync.py:156`

## `writeback_event` — function (async), line 253
- **called from:**
- `src/caldav_sync.py:665`
- `src/caldav_sync.py:678`
- `tests/test_caldav_writeback.py:183`
- `tests/test_caldav_writeback.py:233`
