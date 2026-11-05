# `src/user_time.py` — definitions & call sites

19 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `set_user_tz_offset` — function, line 19
- **called from:**
- `routes/calendar_routes.py:1828`
- `routes/chat_routes.py:2313`
- `scripts/eval_odysseus_everyday_live_hard.py:216`
- `scripts/eval_odysseus_live_hard_examples.py:227`
- `src/user_time.py:50`
- `tests/test_calendar_update_event_tz.py:34`
- `tests/test_calendar_update_event_tz.py:38`
- `tests/test_parse_due_time_first.py:27`
- `tests/test_user_time.py:21`
- `tests/test_user_time.py:36`
- `tests/test_user_time.py:49`
- `tests/test_user_time.py:70`
- `tests/test_user_time.py:91`
- `tests/test_user_time.py:147`
- `tests/test_user_time.py:171`
- `tests/test_user_time.py:192`
- `tests/test_user_time.py:254`
- `tests/test_user_time.py:275`

## `get_user_tz_offset` — function, line 32
- **called from:**
- `routes/calendar_routes.py:389`
- `src/user_time.py:95`
- `tests/test_user_time.py:118`
- `tests/test_user_time.py:134`

## `set_user_tz_name` — function, line 37
- **called from:**
- `routes/calendar_routes.py:1830`
- `routes/chat_routes.py:2315`
- `scripts/eval_odysseus_everyday_live_hard.py:215`
- `scripts/eval_odysseus_live_hard_examples.py:226`
- `src/user_time.py:49`
- `tests/test_parse_due_time_first.py:28`
- `tests/test_user_time.py:22`
- `tests/test_user_time.py:37`
- `tests/test_user_time.py:60`
- `tests/test_user_time.py:71`
- `tests/test_user_time.py:82`
- `tests/test_user_time.py:92`
- `tests/test_user_time.py:148`
- `tests/test_user_time.py:172`
- `tests/test_user_time.py:193`
- `tests/test_user_time.py:255`
- `tests/test_user_time.py:276`

## `set_user_timezone` — function, line 47
- **called from:**
- `routes/chat_routes.py:2310`
- `tests/test_tool_policy.py:1370`
- `tests/test_user_time.py:94`

## `get_user_tz_name` — function, line 53
- **called from:**
- `routes/calendar_routes.py:390`
- `src/user_time.py:76`
- `src/user_time.py:126`
- `tests/test_user_time.py:83`
- `tests/test_user_time.py:86`
- `tests/test_user_time.py:117`
- `tests/test_user_time.py:133`

## `clear_user_time_context` — function, line 58
- **called from:**
- `routes/calendar_routes.py:1825`
- `routes/chat_routes.py:2304`
- `tests/test_kv_cache_invalidation_2927.py:131`
- `tests/test_kv_cache_invalidation_2927.py:182`
- `tests/test_kv_cache_invalidation_2927.py:228`
- `tests/test_parse_due_time_first.py:26`
- `tests/test_parse_due_time_first.py:32`
- `tests/test_tool_policy.py:1442`
- `tests/test_user_time.py:16`
- `tests/test_user_time.py:20`
- `tests/test_user_time.py:35`
- `tests/test_user_time.py:48`
- `tests/test_user_time.py:59`
- `tests/test_user_time.py:69`
- `tests/test_user_time.py:81`
- `tests/test_user_time.py:85`
- `tests/test_user_time.py:90`
- `tests/test_user_time.py:111`
- `tests/test_user_time.py:127`
- `tests/test_user_time.py:146`
- `tests/test_user_time.py:170`
- `tests/test_user_time.py:191`
- `tests/test_user_time.py:253`
- `tests/test_user_time.py:274`

## `format_utc_offset` — function, line 64
- **called from:**
- `src/user_time.py:124`
- `src/user_time.py:198`

## `_zoneinfo_from_name` — function, line 74
- **called from:**
- `src/user_time.py:92`
- `src/user_time.py:125`

## `user_timezone` — function, line 86
- **called from:**
- `routes/calendar_routes.py:408`
- `scripts/eval_odysseus_everyday_live_hard.py:462`
- `scripts/eval_odysseus_everyday_live_hard.py:467`
- `src/agent_loop.py:1739`
- `src/agent_loop.py:1829`
- `src/agent_loop.py:5596`
- `src/agent_loop.py:5597`
- `src/agent_loop.py:35746`
- `src/user_time.py:107`

## `now_user_local` — function, line 101
- **called from:**
- `routes/calendar_routes.py:416`
- `routes/calendar_routes.py:1838`
- `scripts/eval_odysseus_everyday_live_hard.py:458`
- `src/agent_loop.py:1471`
- `src/agent_loop.py:1501`
- `src/agent_loop.py:1567`
- `src/agent_loop.py:4132`
- `src/agent_loop.py:5768`
- `src/agent_loop.py:5843`
- `src/agent_loop.py:5984`
- `src/agent_loop.py:6101`
- `src/tools/notes.py:284`
- `src/user_time.py:122`
- `src/user_time.py:139`
- `src/user_time.py:274`

## `_date_label` — function, line 110
- **called from:**
- `src/user_time.py:143`
- `src/user_time.py:146`
- `src/user_time.py:203`
- `src/user_time.py:206`
- `src/user_time.py:276`

## `_clock_label` — function, line 114
- **called from:**
- `src/user_time.py:144`
- `src/user_time.py:204`
- `src/user_time.py:276`

## `timezone_label` — function, line 119
- **called from:**
- `src/user_time.py:144`
- `src/user_time.py:277`

## `current_datetime_prompt` — function, line 130
- **called from:**
- `routes/calendar_routes.py:1843`
- `src/user_time.py:239`
- `tests/test_user_time.py:24`
- `tests/test_user_time.py:39`
- `tests/test_user_time.py:51`
- `tests/test_user_time.py:62`
- `tests/test_user_time.py:73`
- `tests/test_user_time.py:95`

## `current_datetime_context_message_for_tz` — function, line 158
- **called from:**
- `src/task_scheduler.py:1759`
- `tests/test_scheduler_prompt_cache_time.py:173`
- `tests/test_scheduler_prompt_cache_time.py:180`
- `tests/test_scheduler_prompt_cache_time.py:185`

## `current_datetime_context_message` — function, line 221
- **called from:**
- `routes/chat_helpers.py:1502`
- `scripts/eval_odysseus_everyday_live_hard.py:251`
- `scripts/eval_odysseus_live_hard_examples.py:258`
- `src/agent_loop.py:14894`
- `tests/test_kv_cache_invalidation_2927.py:229`
- `tests/test_user_time.py:174`

## `now_iso` — function, line 254
- **called from:**
- `src/agent_loop.py:16395`
- `src/agent_loop.py:16485`
- `src/agent_loop.py:16511`
- `src/llm_core.py:2307`
- `tests/test_temporal_grounding_stamps.py:120`

## `current_datetime_line` — function, line 266
- **called from:**
- `src/agent_loop.py:16484`
- `src/agent_loop.py:16503`
- `src/tool_execution.py:1738`
- `src/tool_execution.py:2594`

## `parse_message_timestamp` — function, line 282
- **called from:**
- `tests/test_temporal_grounding_stamps.py:113`
- `tests/test_temporal_grounding_stamps.py:114`
- `tests/test_temporal_grounding_stamps.py:115`
- `tests/test_temporal_grounding_stamps.py:116`
- `tests/test_temporal_grounding_stamps.py:118`
