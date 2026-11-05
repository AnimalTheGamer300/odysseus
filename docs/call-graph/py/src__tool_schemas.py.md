# `src/tool_schemas.py` — definitions & call sites

15 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_first_nonempty_string` — function, line 52
- **called from:**
- `src/tool_schemas.py:103`
- `src/tool_schemas.py:107`
- `src/tool_schemas.py:116`
- `src/tool_schemas.py:126`

## `_repair_function_arg_aliases` — function, line 60
- **called from:**
- `src/tool_schemas.py:256`

## `_schema_name_for_tool` — function, line 143
- **called from:**
- `src/tool_schemas.py:152`

## `_schema_properties_for_tool` — function, line 151
- **called from:**
- `src/tool_schemas.py:186`

## `_normalize_function_args_for_schema` — function, line 163
- **called from:**
- `src/tool_schemas.py:257`

## `normalize_native_function_args` — function, line 249
- **called from:**
- `src/clean_agent_preview.py:3137`
- `src/clean_agent_preview.py:3167`
- `src/tool_schemas.py:3400`
- `tests/test_tool_schemas.py:120`
- `tests/test_tool_schemas.py:133`
- `tests/test_tool_schemas.py:228`

## `normalized_native_function_argument_error` — function, line 261
- **called from:**
- `src/clean_agent_preview.py:7419`
- `src/clean_agent_preview.py:7596`
- `src/tool_schemas.py:3427`
- `tests/test_clean_agent_preview.py:3634`
- `tests/test_clean_agent_preview.py:3640`
- `tests/test_clean_agent_preview.py:3644`
- `tests/test_tool_schemas.py:236`

## `_slim_description` — function, line 3197
- **called from:**
- `src/tool_schemas.py:3217`
- `src/tool_schemas.py:3237`

## `_slim_node` — function, line 3208
- **called from:**
- `src/tool_schemas.py:3219`
- `src/tool_schemas.py:3222`
- `src/tool_schemas.py:3238`

## `slim_tool_schema` — function, line 3225
- **called from:**
- `src/tool_schemas.py:3243`

## `slim_tool_schemas` — function, line 3242
- **called from:**
- `src/agent_loop.py:25842`

## `_decode_loose_json_string` — function, line 3250
- **called from:**
- `src/tool_schemas.py:3312`

## `_repair_document_function_args` — function, line 3285
- **called from:**
- `src/tool_schemas.py:3378`

## `_repair_truncated_readonly_inspect_args` — function, line 3317
- **called from:**
- `src/tool_schemas.py:3380`

## `function_call_to_tool_block` — function, line 3369
- **called from:**
- `scripts/eval_qwen_tool_groups_stream.py:45`
- `src/agent_loop.py:15745`
- `src/clean_agent_preview.py:7155`
- `src/clean_agent_preview.py:7841`
- `src/tool_parsing.py:739`
- `src/tool_parsing.py:770`
- `src/tool_parsing.py:915`
- `src/tool_parsing.py:1105`
- `src/tool_parsing.py:1189`
- `src/tool_parsing.py:1285`
- `src/tool_parsing.py:1325`
- `src/tool_parsing.py:1365`
- `src/tool_parsing.py:1457`
- `src/tool_parsing.py:1491`
- `src/tool_parsing.py:1584`
- `src/tool_parsing.py:1602`
- `tests/test_ask_user_tool.py:88`
- `tests/test_ask_user_tool.py:101`
- `tests/test_clean_agent_preview.py:3623`
- `tests/test_document_followup_integrity.py:214`
- `tests/test_function_call_non_object_args.py:49`
- `tests/test_function_call_non_object_args.py:58`
- `tests/test_function_call_non_object_args.py:64`
- `tests/test_function_call_non_object_args.py:75`
- `tests/test_function_call_non_object_args.py:84`
- `tests/test_function_call_non_object_args.py:95`
- `tests/test_function_call_non_object_args.py:108`
- `tests/test_generate_image_native_schema.py:21`
- `tests/test_manage_memory_json_contract.py:52`
- `tests/test_manage_memory_json_contract.py:62`
- `tests/test_spawn_agent.py:29`
- `tests/test_spawn_agent.py:42`
- `tests/test_tool_schemas.py:24`
- `tests/test_tool_schemas.py:35`
- `tests/test_tool_schemas.py:44`
- `tests/test_tool_schemas.py:55`
- `tests/test_tool_schemas.py:69`
- `tests/test_tool_schemas.py:80`
- `tests/test_tool_schemas.py:88`
- `tests/test_tool_schemas.py:96`
- `tests/test_tool_schemas.py:153`
- `tests/test_tool_schemas.py:168`
- `tests/test_tool_schemas.py:182`
- `tests/test_tool_schemas.py:190`
- `tests/test_tool_schemas.py:204`
- `tests/test_tool_schemas.py:224`
- `tests/test_ui_control_rag_toggle.py:24`
- `tests/test_ui_control_rag_toggle.py:119`
- `tests/test_unknown_tool_calls.py:55`
- `tests/test_unknown_tool_calls.py:61`
- `tests/test_unknown_tool_calls.py:68`
- `tests/test_unknown_tool_calls.py:74`
- `tests/test_web_fetch_batch.py:102`
- `tests/test_web_fetch_batch.py:111`
- `tests/test_web_fetch_batch.py:127`
- `tests/test_web_fetch_batch.py:141`
- `tests/test_web_search_time_filter.py:14`
- `tests/test_web_search_time_filter.py:24`
- `tests/test_web_search_time_filter.py:29`
- `tests/test_web_search_time_filter.py:36`
- … +9 more (grep the name in repo)
