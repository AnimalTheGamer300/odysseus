# `src/tools/calendar.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `do_manage_calendar` — function (async), line 19
- **called from:**
- `routes/email_pollers.py:965`
- `routes/email_pollers.py:980`
- `routes/email_pollers.py:1062`
- `src/tool_execution.py:1236`
- `src/tools/calendar.py:53`
- `tests/test_calendar_batch_events.py:51`
- `tests/test_calendar_batch_events.py:76`
- `tests/test_calendar_batch_events.py:104`
- `tests/test_calendar_default_transaction.py:117`
- `tests/test_calendar_default_transaction.py:136`
- `tests/test_calendar_default_transaction.py:162`
- `tests/test_calendar_list_range_aliases.py:57`
- `tests/test_calendar_list_range_aliases.py:64`
- `tests/test_calendar_list_range_aliases.py:71`
- `tests/test_calendar_list_range_aliases.py:88`
- `tests/test_calendar_list_range_aliases.py:98`
- `tests/test_calendar_reminder_minutes_parsing.py:48`
- `tests/test_calendar_reminder_minutes_parsing.py:86`
- `tests/test_calendar_rrule.py:43`
- `tests/test_calendar_rrule.py:67`
- `tests/test_calendar_rrule.py:85`
- `tests/test_calendar_rrule.py:93`
- `tests/test_calendar_rrule.py:113`
- `tests/test_calendar_rrule.py:121`
- `tests/test_calendar_rrule.py:142`
- `tests/test_calendar_rrule.py:150`
- `tests/test_calendar_update_event_tz.py:47`
- `tests/test_calendar_update_event_tz.py:63`
- `tests/test_calendar_update_event_tz.py:87`
- `tests/test_calendar_update_event_tz.py:95`
- `tests/test_calendar_update_event_tz.py:108`
- `tests/test_upload_handler_cleanup.py:700`

## `_calendar_query` — function, line 90
- **called from:**
- `src/tools/calendar.py:202`
- `src/tools/calendar.py:316`
- `src/tools/calendar.py:321`
- `src/tools/calendar.py:325`

## `_event_query` — function, line 96
- **called from:**
- `src/tools/calendar.py:244`
- `src/tools/calendar.py:368`
- `src/tools/calendar.py:484`
- `src/tools/calendar.py:545`

## `_reminder_minutes` — function, line 102
- **called from:**
- `src/tools/calendar.py:379`
- `src/tools/calendar.py:414`

## `_event_description` — function, line 133
- **called from:**
- `src/tools/calendar.py:416`

## `_parse_event_dt` — function, line 144
- **called from:**
- `src/tools/calendar.py:333`
- `src/tools/calendar.py:339`
- `src/tools/calendar.py:512`
- `src/tools/calendar.py:515`

## `_first_nonempty_arg` — function, line 148
- **called from:**
- `src/tools/calendar.py:215`
- `src/tools/calendar.py:218`

## `_create_calendar_reminder` — function, line 155
- **called from:**
- `src/tools/calendar.py:381`
- `src/tools/calendar.py:446`
