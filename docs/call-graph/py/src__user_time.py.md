# `src/user_time.py` — definitions & call sites

18 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `set_user_tz_offset` — function, line 19
- **called from:**
- `routes/calendar_routes.py:1653`
- `routes/chat_routes.py:902`
- `tests/test_calendar_update_event_tz.py:34`
- `tests/test_calendar_update_event_tz.py:38`
- `tests/test_parse_due_time_first.py:27`
- `tests/test_user_time.py:19`
- `tests/test_user_time.py:34`
- `tests/test_user_time.py:47`
- `tests/test_user_time.py:68`
- `tests/test_user_time.py:97`
- `tests/test_user_time.py:121`
- `tests/test_user_time.py:142`
- `tests/test_user_time.py:204`
- `tests/test_user_time.py:225`

## `get_user_tz_offset` — function, line 32
- **called from:**
- `routes/calendar_routes.py:375`
- `src/user_time.py:89`

## `set_user_tz_name` — function, line 37
- **called from:**
- `routes/calendar_routes.py:1655`
- `routes/chat_routes.py:904`
- `tests/test_parse_due_time_first.py:28`
- `tests/test_user_time.py:20`
- `tests/test_user_time.py:35`
- `tests/test_user_time.py:58`
- `tests/test_user_time.py:69`
- `tests/test_user_time.py:80`
- `tests/test_user_time.py:98`
- `tests/test_user_time.py:122`
- `tests/test_user_time.py:143`
- `tests/test_user_time.py:205`
- `tests/test_user_time.py:226`

## `get_user_tz_name` — function, line 47
- **called from:**
- `routes/calendar_routes.py:376`
- `src/user_time.py:70`
- `src/user_time.py:120`
- `tests/test_user_time.py:81`
- `tests/test_user_time.py:84`

## `clear_user_time_context` — function, line 52
- **called from:**
- `routes/calendar_routes.py:1650`
- `routes/chat_routes.py:900`
- `tests/test_kv_cache_invalidation_2927.py:131`
- `tests/test_kv_cache_invalidation_2927.py:182`
- `tests/test_kv_cache_invalidation_2927.py:228`
- `tests/test_parse_due_time_first.py:26`
- `tests/test_parse_due_time_first.py:32`
- `tests/test_user_time.py:14`
- `tests/test_user_time.py:18`
- `tests/test_user_time.py:33`
- `tests/test_user_time.py:46`
- `tests/test_user_time.py:57`
- `tests/test_user_time.py:67`
- `tests/test_user_time.py:79`
- `tests/test_user_time.py:83`
- `tests/test_user_time.py:96`
- `tests/test_user_time.py:120`
- `tests/test_user_time.py:141`
- `tests/test_user_time.py:203`
- `tests/test_user_time.py:224`

## `format_utc_offset` — function, line 58
- **called from:**
- `src/user_time.py:118`
- `src/user_time.py:192`

## `_zoneinfo_from_name` — function, line 68
- **called from:**
- `src/user_time.py:86`
- `src/user_time.py:119`

## `user_timezone` — function, line 80
- **called from:**
- `routes/calendar_routes.py:394`
- `src/user_time.py:101`

## `now_user_local` — function, line 95
- **called from:**
- `routes/calendar_routes.py:402`
- `routes/calendar_routes.py:1663`
- `src/user_time.py:116`
- `src/user_time.py:133`
- `src/user_time.py:268`

## `_date_label` — function, line 104
- **called from:**
- `src/user_time.py:137`
- `src/user_time.py:140`
- `src/user_time.py:197`
- `src/user_time.py:200`
- `src/user_time.py:270`

## `_clock_label` — function, line 108
- **called from:**
- `src/user_time.py:138`
- `src/user_time.py:198`
- `src/user_time.py:270`

## `timezone_label` — function, line 113
- **called from:**
- `src/user_time.py:138`
- `src/user_time.py:271`

## `current_datetime_prompt` — function, line 124
- **called from:**
- `routes/calendar_routes.py:1668`
- `src/user_time.py:233`
- `tests/test_user_time.py:22`
- `tests/test_user_time.py:37`
- `tests/test_user_time.py:49`
- `tests/test_user_time.py:60`
- `tests/test_user_time.py:71`

## `current_datetime_context_message_for_tz` — function, line 152
- **called from:**
- `src/task_scheduler.py:1599`
- `tests/test_scheduler_prompt_cache_time.py:168`
- `tests/test_scheduler_prompt_cache_time.py:175`
- `tests/test_scheduler_prompt_cache_time.py:180`

## `current_datetime_context_message` — function, line 215
- **called from:**
- `routes/chat_helpers.py:910`
- `src/agent_loop.py:2736`
- `tests/test_kv_cache_invalidation_2927.py:229`
- `tests/test_user_time.py:124`

## `now_iso` — function, line 248
- **called from:**
- `src/agent_loop.py:3528`
- `src/agent_loop.py:3609`
- `src/agent_loop.py:3625`
- `tests/test_temporal_grounding_stamps.py:120`

## `current_datetime_line` — function, line 260
- **called from:**
- `src/agent_loop.py:3608`
- `src/agent_loop.py:3617`
- `src/tool_execution.py:1387`

## `parse_message_timestamp` — function, line 276
- **called from:**
- `tests/test_temporal_grounding_stamps.py:113`
- `tests/test_temporal_grounding_stamps.py:114`
- `tests/test_temporal_grounding_stamps.py:115`
- `tests/test_temporal_grounding_stamps.py:116`
- `tests/test_temporal_grounding_stamps.py:118`
