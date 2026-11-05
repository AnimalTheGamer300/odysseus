# `src/tool_replay.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_format_output` — function, line 62
- **called from:**
- `src/tool_replay.py:81`
- `src/tool_replay.py:128`
- `src/tool_replay.py:247`
- `tests/test_tool_replay.py:70`

## `_format_event` — function, line 76
- **called from:**
- `src/tool_replay.py:130`

## `collect_prior_tool_event_groups` — function, line 93
- **called from:**
- `src/tool_replay.py:117`

## `prior_tool_outputs_context_message` — function, line 111
- **called from:**
- `routes/chat_helpers.py:1549`
- `tests/test_tool_replay.py:21`
- `tests/test_tool_replay.py:22`
- `tests/test_tool_replay.py:23`
- `tests/test_tool_replay.py:36`
- `tests/test_tool_replay.py:56`
- `tests/test_tool_replay.py:64`
- `tests/test_tool_replay.py:87`
- `tests/test_tool_replay.py:98`
- `tests/test_tool_replay.py:106`

## `_stable_call_id` — function, line 166
- **called from:**
- `src/tool_replay.py:241`

## `_native_args_for_event` — function, line 177
- **called from:**
- `src/tool_replay.py:245`

## `replay_tool_events_as_native` — function, line 197
- **called from:**
- `routes/chat_helpers.py:1536`
- `tests/test_temporal_grounding_stamps.py:98`

## `inject_continue_separator` — function, line 301
- **called from:**
- `routes/chat_helpers.py:1595`

## `build_continue_separator_event` — function, line 344
- **called from:**
- `routes/chat_routes.py:1545`
