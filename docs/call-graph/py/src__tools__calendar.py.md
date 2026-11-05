# `src/tools/calendar.py` — definitions & call sites

17 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_normalize_local_event_times` — function, line 21
- **called from:**
- `src/tools/calendar.py:117`
- `tests/test_calendar_explicit_timezone.py:45`
- `tests/test_calendar_explicit_timezone.py:50`

## `_saved_event_times` — function, line 47
- **called from:**
- `src/tools/calendar.py:579`
- `src/tools/calendar.py:583`
- `src/tools/calendar.py:655`
- `src/tools/calendar.py:657`
- `src/tools/calendar.py:793`

## `serialize` — function, line 49
- **called from:**
- `src/tools/calendar.py:57`
- `src/tools/calendar.py:58`

## `_explicit_calendar_time` — function, line 64
- **called from:**
- `src/tools/calendar.py:263`
- `tests/test_calendar_explicit_timezone.py:19`
- `tests/test_calendar_explicit_timezone.py:31`

## `do_manage_calendar` — function (async), line 95
- **called from:**
- `routes/email/email_pollers.py:1149`
- `routes/email/email_pollers.py:1168`
- `routes/email/email_pollers.py:1260`
- `src/email_calendar_import.py:159`
- `src/tool_execution.py:2418`
- `src/tools/calendar.py:135`
- `tests/test_calendar_batch_events.py:51`
- `tests/test_calendar_batch_events.py:76`
- `tests/test_calendar_batch_events.py:104`
- `tests/test_calendar_default_transaction.py:117`
- `tests/test_calendar_default_transaction.py:136`
- `tests/test_calendar_default_transaction.py:162`
- `tests/test_calendar_list_range_aliases.py:57`
- `tests/test_calendar_list_range_aliases.py:64`
- `tests/test_calendar_list_range_aliases.py:71`
- `tests/test_calendar_list_range_aliases.py:89`
- `tests/test_calendar_list_range_aliases.py:97`
- `tests/test_calendar_list_range_aliases.py:104`
- `tests/test_calendar_list_range_aliases.py:121`
- `tests/test_calendar_list_range_aliases.py:131`
- `tests/test_calendar_reminder_minutes_parsing.py:48`
- `tests/test_calendar_reminder_minutes_parsing.py:89`
- `tests/test_calendar_reminder_minutes_parsing.py:98`
- `tests/test_calendar_reminder_minutes_parsing.py:105`
- `tests/test_calendar_reminder_minutes_parsing.py:137`
- `tests/test_calendar_reminder_minutes_parsing.py:150`
- `tests/test_calendar_rrule.py:44`
- `tests/test_calendar_rrule.py:146`
- `tests/test_calendar_rrule.py:164`
- `tests/test_calendar_rrule.py:172`
- `tests/test_calendar_rrule.py:192`
- `tests/test_calendar_rrule.py:200`
- `tests/test_calendar_rrule.py:221`
- `tests/test_calendar_rrule.py:229`
- `tests/test_calendar_stream_links.py:28`
- `tests/test_calendar_stream_links.py:71`
- `tests/test_calendar_update_event_tz.py:58`
- `tests/test_calendar_update_event_tz.py:60`
- `tests/test_calendar_update_event_tz.py:62`
- `tests/test_calendar_update_event_tz.py:85`
- `tests/test_calendar_update_event_tz.py:91`
- `tests/test_calendar_update_event_tz.py:109`
- `tests/test_calendar_update_event_tz.py:126`
- `tests/test_calendar_update_event_tz.py:150`
- `tests/test_calendar_update_event_tz.py:158`
- `tests/test_calendar_update_event_tz.py:173`
- `tests/test_calendar_update_event_tz.py:186`
- `tests/test_calendar_update_event_tz.py:195`
- `tests/test_calendar_update_event_tz.py:221`
- `tests/test_calendar_update_event_tz.py:246`
- `tests/test_calendar_update_event_tz.py:254`
- `tests/test_calendar_update_event_tz.py:272`
- `tests/test_calendar_update_event_tz.py:280`
- `tests/test_calendar_update_event_tz.py:293`
- `tests/test_minimal_native_tool_prompt.py:953`
- `tests/test_minimal_native_tool_prompt.py:962`
- `tests/test_upload_handler_cleanup.py:700`
- `tests/tools/organizer_smoke.py:103`
- `tests/tools/organizer_smoke.py:241`

## `_calendar_query` — function, line 172
- **called from:**
- `src/tools/calendar.py:343`
- `src/tools/calendar.py:459`
- `src/tools/calendar.py:464`
- `src/tools/calendar.py:468`

## `_event_query` — function, line 178
- **called from:**
- `src/tools/calendar.py:386`
- `src/tools/calendar.py:519`
- `src/tools/calendar.py:682`
- `src/tools/calendar.py:687`
- `src/tools/calendar.py:808`
- `src/tools/calendar.py:824`

## `_event_uid_candidates` — function, line 184
- **called from:**
- `src/tools/calendar.py:677`
- `src/tools/calendar.py:819`

## `_first_present_arg` — function, line 200
- **called from:**
- `src/tools/calendar.py:218`

## `_has_reminder_request` — function, line 206
- **called from:**
- `src/tools/calendar.py:765`

## `_reminder_minutes` — function, line 217
- **called from:**
- `src/tools/calendar.py:558`
- `src/tools/calendar.py:597`
- `src/tools/calendar.py:767`

## `_event_description` — function, line 249
- **called from:**
- `src/tools/calendar.py:599`

## `_parse_event_dt` — function, line 260
- **called from:**
- `src/tools/calendar.py:277`
- `src/tools/calendar.py:373`
- `src/tools/calendar.py:377`
- `src/tools/calendar.py:479`
- `src/tools/calendar.py:489`
- `src/tools/calendar.py:730`
- `src/tools/calendar.py:740`

## `_parse_all_day_event_dt` — function, line 266
- **called from:**
- `src/tools/calendar.py:477`
- `src/tools/calendar.py:487`

## `_looks_like_timed_dt` — function, line 279
- **called from:**
- `src/tools/calendar.py:727`
- `src/tools/calendar.py:741`

## `_first_nonempty_arg` — function, line 289
- **called from:**
- `src/tools/calendar.py:356`
- `src/tools/calendar.py:359`

## `_create_calendar_reminder` — function, line 296
- **called from:**
- `src/tools/calendar.py:560`
- `src/tools/calendar.py:633`
- `src/tools/calendar.py:771`
