# `src/tool_schemas.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_slim_description` — function, line 774
- **called from:**
- `src/tool_schemas.py:794`
- `src/tool_schemas.py:814`

## `_slim_node` — function, line 785
- **called from:**
- `src/tool_schemas.py:796`
- `src/tool_schemas.py:799`
- `src/tool_schemas.py:815`

## `slim_tool_schema` — function, line 802
- **called from:**
- `src/tool_schemas.py:820`

## `slim_tool_schemas` — function, line 819
- **called from:**
- `src/agent_loop.py:5046`

## `_decode_loose_json_string` — function, line 827
- **called from:**
- `src/tool_schemas.py:889`

## `_repair_document_function_args` — function, line 862
- **called from:**
- `src/tool_schemas.py:903`

## `function_call_to_tool_block` — function, line 894
- **called from:**
- `src/agent_loop.py:3426`
- `src/tool_parsing.py:500`
- `src/tool_parsing.py:531`
- `src/tool_parsing.py:899`
- `src/tool_parsing.py:939`
- `src/tool_parsing.py:979`
- `src/tool_parsing.py:1071`
- `src/tool_parsing.py:1105`
- `src/tool_parsing.py:1164`
- `src/tool_parsing.py:1182`
- `tests/test_ask_user_tool.py:85`
- `tests/test_ask_user_tool.py:98`
- `tests/test_function_call_non_object_args.py:49`
- `tests/test_function_call_non_object_args.py:58`
- `tests/test_function_call_non_object_args.py:64`
- `tests/test_function_call_non_object_args.py:75`
- `tests/test_function_call_non_object_args.py:88`
- `tests/test_spawn_agent.py:29`
- `tests/test_spawn_agent.py:42`
- `tests/test_unknown_tool_calls.py:55`
- `tests/test_unknown_tool_calls.py:61`
- `tests/test_unknown_tool_calls.py:68`
- `tests/test_unknown_tool_calls.py:74`
- `tests/test_web_search_time_filter.py:33`
- `tests/test_web_search_time_filter.py:43`
- `tests/test_web_search_time_filter.py:48`
- `tests/test_web_search_time_filter.py:55`
