# `src/tool_parsing.py` — definitions & call sites

33 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_fenced_tool_call` — function, line 52
- **called from:**
- `src/tool_parsing.py:85`
- `src/tool_parsing.py:1350`

## `_strip_executed_fence` — function, line 83
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_normalize_dsml` — function, line 221
- **called from:**
- `src/tool_parsing.py:1322`
- `src/tool_parsing.py:1528`
- `tests/test_tool_parsing_nonstring.py:12`

## `_literal_string` — function, line 370
- **called from:**
- `src/tool_parsing.py:416`
- `src/tool_parsing.py:426`
- `src/tool_parsing.py:475`
- `src/tool_parsing.py:485`

## `_parse_misfenced_web_lookup` — function, line 385
- **called from:**
- `src/tool_parsing.py:1378`

## `_parse_misfenced_read_file_lookup` — function, line 458
- **called from:**
- `src/tool_parsing.py:1379`

## `_coerce_raw_web_query` — function, line 539
- **called from:**
- `src/tool_parsing.py:555`
- `src/tool_parsing.py:557`

## `_raw_web_json_to_tool_block` — function, line 549
- **called from:**
- `src/tool_parsing.py:600`

## `_parse_raw_web_json_lookup` — function, line 576
- **called from:**
- `src/tool_parsing.py:1498`
- `src/tool_parsing.py:1547`

## `_looks_like_openai_tool_call_blob` — function, line 606
- **called from:**
- `src/tool_parsing.py:609`
- `src/tool_parsing.py:793`

## `_raw_openai_tool_call_to_block` — function, line 618
- **called from:**
- `src/tool_parsing.py:621`
- `src/tool_parsing.py:765`

## `_parse_raw_openai_tool_call_json` — function, line 756
- **called from:**
- `src/tool_parsing.py:1492`

## `_strip_raw_openai_tool_call_json` — function, line 771
- **called from:**
- `src/tool_parsing.py:1543`

## `_parse_tool_call_block` — function, line 808
- **called from:**
- `src/tool_parsing.py:1393`
- `tests/test_redos_xml_tool_parsers.py:106`

## `_parse_xml_invoke` — function, line 877
- **called from:**
- `src/tool_parsing.py:1369`
- `src/tool_parsing.py:1422`
- `src/tool_parsing.py:1443`
- `src/tool_parsing.py:1458`

## `_parse_xml_direct_tool` — function, line 902
- **called from:**
- `src/tool_parsing.py:1427`
- `src/tool_parsing.py:1449`

## `_looks_like_json_body` — function, line 942
- **called from:**
- `src/tool_parsing.py:1415`
- `src/tool_parsing.py:1435`

## `_parse_json_tool_call_body` — function, line 947
- **called from:**
- `src/tool_parsing.py:1417`
- `src/tool_parsing.py:1438`

## `_iter_stepfun_tool_calls` — function, line 982
- **called from:**
- `src/tool_parsing.py:1399`

## `_strip_stepfun_tool_markup` — function, line 1003
- **called from:**
- `src/tool_parsing.py:1537`

## `_strip_bare_invoke_markup` — function, line 1022
- **called from:**
- `src/tool_parsing.py:1553`

## `_parse_stepfun_tool_call` — function, line 1044
- **called from:**
- `src/tool_parsing.py:1400`

## `_parse_tool_code_block` — function, line 1074
- **called from:**
- `src/tool_parsing.py:1467`

## `_parse_gemma_tool_call` — function, line 1132
- **called from:**
- `src/tool_parsing.py:1476`

## `_parse_function_model_call` — function, line 1167
- **called from:**
- `src/tool_parsing.py:1485`

## `_iter_delimited` — function, line 1185
- **called from:**
- `src/tool_parsing.py:1174`
- `src/tool_parsing.py:1219`
- `src/tool_parsing.py:1390`
- `src/tool_parsing.py:1411`
- `src/tool_parsing.py:1464`
- `src/tool_parsing.py:1482`

## `_strip_delimited` — function, line 1215
- **called from:**
- `src/tool_parsing.py:1536`
- `src/tool_parsing.py:1538`
- `src/tool_parsing.py:1540`
- `src/tool_parsing.py:1542`

## `_iter_named_blocks` — function, line 1231
- **called from:**
- `src/tool_parsing.py:895`
- `src/tool_parsing.py:1251`

## `_iter_xml_invoke` — function, line 1249
- **called from:**
- `src/tool_parsing.py:1368`
- `src/tool_parsing.py:1421`
- `src/tool_parsing.py:1442`
- `src/tool_parsing.py:1457`

## `_iter_backref_blocks` — function, line 1254
- **called from:**
- `src/tool_parsing.py:1097`
- `src/tool_parsing.py:1291`

## `_iter_xml_direct` — function, line 1288
- **called from:**
- `src/tool_parsing.py:1426`
- `src/tool_parsing.py:1448`

## `parse_tool_blocks` — function, line 1294
- **called from:**
- `src/agent_loop.py:3450`
- `tests/test_fenced_example_not_executed_for_native_models.py:220`
- `tests/test_fenced_example_not_executed_for_native_models.py:234`
- `tests/test_fenced_example_not_executed_for_native_models.py:247`
- `tests/test_fenced_example_not_executed_for_native_models.py:258`
- `tests/test_fenced_example_not_executed_for_native_models.py:273`
- `tests/test_fenced_example_not_executed_for_native_models.py:289`
- `tests/test_fenced_example_not_executed_for_native_models.py:297`
- `tests/test_fenced_example_not_executed_for_native_models.py:298`
- `tests/test_fenced_inline_args.py:28`
- `tests/test_fenced_inline_args.py:33`
- `tests/test_fenced_inline_args.py:39`
- `tests/test_fenced_inline_args.py:44`
- `tests/test_fenced_inline_args.py:52`
- `tests/test_fenced_inline_args.py:57`
- `tests/test_fenced_inline_args.py:65`
- `tests/test_fenced_inline_args.py:70`
- `tests/test_fenced_inline_args.py:77`
- `tests/test_fenced_inline_args.py:84`
- `tests/test_fenced_inline_args.py:95`
- `tests/test_fenced_inline_args.py:105`
- `tests/test_fenced_inline_args.py:111`
- `tests/test_fenced_inline_args.py:118`
- `tests/test_fenced_inline_args.py:124`
- `tests/test_fenced_inline_args.py:178`
- `tests/test_fenced_invoke_no_raw_xml.py:25`
- `tests/test_fenced_invoke_no_raw_xml.py:35`
- `tests/test_fenced_invoke_no_raw_xml.py:40`
- `tests/test_fenced_invoke_no_raw_xml.py:47`
- `tests/test_fenced_invoke_no_raw_xml.py:58`
- `tests/test_fenced_invoke_no_raw_xml.py:64`
- `tests/test_fenced_invoke_no_raw_xml.py:70`
- `tests/test_function_model_tool_call.py:13`
- `tests/test_function_model_tool_call.py:28`
- `tests/test_gemma_tool_call_parsing.py:7`
- `tests/test_gemma_tool_call_parsing.py:18`
- `tests/test_gemma_tool_call_parsing.py:28`
- `tests/test_gemma_tool_call_parsing.py:38`
- `tests/test_misfenced_read_file_tool_call.py:8`
- `tests/test_misfenced_read_file_tool_call.py:16`
- `tests/test_misfenced_read_file_tool_call.py:28`
- `tests/test_misfenced_read_file_tool_call.py:36`
- `tests/test_misfenced_read_file_tool_call.py:48`
- `tests/test_misfenced_read_file_tool_call.py:56`
- `tests/test_odysseus_doc_fence_normalization.py:9`
- `tests/test_odysseus_doc_fence_normalization.py:24`
- `tests/test_odysseus_doc_fence_normalization.py:34`
- `tests/test_plain_ui_control_open_panel.py:6`
- `tests/test_plain_ui_control_open_panel.py:14`
- `tests/test_plain_ui_control_open_panel.py:28`
- `tests/test_plain_ui_control_open_panel.py:29`
- `tests/test_redos_llm_parsers.py:60`
- `tests/test_redos_llm_parsers.py:67`
- `tests/test_redos_xml_tool_parsers.py:48`
- `tests/test_redos_xml_tool_parsers.py:55`
- `tests/test_redos_xml_tool_parsers.py:62`
- `tests/test_redos_xml_tool_parsers.py:67`
- `tests/test_redos_xml_tool_parsers.py:74`
- `tests/test_redos_xml_tool_parsers.py:89`
- `tests/test_redos_xml_tool_parsers.py:99`
- … +16 more (grep the name in repo)

## `strip_tool_blocks` — function, line 1513
- **called from:**
- `src/agent_loop.py:5546`
- `src/agent_loop.py:5894`
- `src/agent_loop.py:5918`
- `src/agent_loop.py:5978`
- `src/agent_loop.py:6657`
- `src/agent_loop.py:6687`
- `src/agent_loop.py:6708`
- `src/agent_loop.py:6934`
- `tests/test_fenced_example_not_executed_for_native_models.py:238`
- `tests/test_fenced_example_not_executed_for_native_models.py:262`
- `tests/test_fenced_example_not_executed_for_native_models.py:277`
- `tests/test_fenced_example_not_executed_for_native_models.py:325`
- `tests/test_fenced_example_not_executed_for_native_models.py:332`
- `tests/test_fenced_example_not_executed_for_native_models.py:344`
- `tests/test_fenced_inline_args.py:90`
- `tests/test_fenced_inline_args.py:137`
- `tests/test_fenced_inline_args.py:144`
- `tests/test_fenced_inline_args.py:150`
- `tests/test_fenced_inline_args.py:157`
- `tests/test_fenced_inline_args.py:179`
- `tests/test_function_model_tool_call.py:18`
- `tests/test_function_model_tool_call.py:29`
- `tests/test_gemma_tool_call_parsing.py:12`
- `tests/test_gemma_tool_call_parsing.py:39`
- `tests/test_gemma_tool_call_parsing.py:48`
- `tests/test_gemma_tool_call_parsing.py:59`
- `tests/test_misfenced_read_file_tool_call.py:65`
- `tests/test_plain_ui_control_open_panel.py:24`
- `tests/test_redos_llm_parsers.py:62`
- `tests/test_redos_llm_parsers.py:69`
- `tests/test_redos_llm_parsers.py:73`
- `tests/test_tool_parsing_bare_end_marker.py:56`
- `tests/test_tool_parsing_bare_end_marker.py:61`
- `tests/test_tool_parsing_bare_end_marker.py:66`
- `tests/test_tool_parsing_hermes_json.py:77`
- `tests/test_tool_parsing_nonstring.py:14`
- `tests/test_tool_parsing_nonstring.py:18`
- `tests/test_web_search_raw_json_tool_call.py:67`
