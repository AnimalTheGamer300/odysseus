# `src/tool_parsing.py` — definitions & call sites

50 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_tool_block_re` — function, line 42
- **called from:**
- `src/tool_parsing.py:1812`
- `src/tool_parsing.py:1897`
- `src/tool_parsing.py:2169`

## `_fenced_tool_call` — function, line 73
- **called from:**
- `src/tool_parsing.py:106`
- `src/tool_parsing.py:1814`
- `src/tool_parsing.py:1824`
- `src/tool_parsing.py:1837`
- `src/tool_parsing.py:1898`

## `_strip_executed_fence` — function, line 104
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_contains_explicit_tool_markup` — function, line 271
- **called from:**
- `src/tool_parsing.py:1889`
- `src/tool_parsing.py:2168`

## `_normalize_dsml` — function, line 288
- **called from:**
- `src/tool_parsing.py:1883`
- `src/tool_parsing.py:2162`
- `tests/test_tool_parsing_nonstring.py:12`

## `_parse_misfenced_media_lookup` — function, line 453
- **called from:**
- `src/tool_parsing.py:1993`

## `_iter_plain_ui_open_panel` — function, line 571
- **called from:**
- `src/tool_parsing.py:586`
- `src/tool_parsing.py:2136`

## `_strip_plain_ui_open_panel` — function, line 585
- **called from:**
- `src/tool_parsing.py:2198`

## `_parse_python_like_content` — function, line 602
- **called from:**
- `src/tool_parsing.py:474`
- `src/tool_parsing.py:637`
- `src/tool_parsing.py:704`
- `tests/test_tool_parsing_mixed_formats.py:25`

## `_literal_string` — function, line 609
- **called from:**
- `src/tool_parsing.py:655`
- `src/tool_parsing.py:665`
- `src/tool_parsing.py:714`
- `src/tool_parsing.py:724`

## `_parse_misfenced_web_lookup` — function, line 624
- **called from:**
- `src/tool_parsing.py:1994`

## `_parse_misfenced_read_file_lookup` — function, line 697
- **called from:**
- `src/tool_parsing.py:1995`

## `_coerce_raw_web_query` — function, line 778
- **called from:**
- `src/tool_parsing.py:794`
- `src/tool_parsing.py:796`

## `_raw_web_json_to_tool_block` — function, line 788
- **called from:**
- `src/tool_parsing.py:839`

## `_parse_raw_web_json_lookup` — function, line 815
- **called from:**
- `src/tool_parsing.py:2128`
- `src/tool_parsing.py:2194`

## `_looks_like_openai_tool_call_blob` — function, line 845
- **called from:**
- `src/tool_parsing.py:848`
- `src/tool_parsing.py:1031`

## `_raw_openai_tool_call_to_block` — function, line 857
- **called from:**
- `src/tool_parsing.py:860`
- `src/tool_parsing.py:1003`

## `_parse_raw_openai_tool_call_json` — function, line 994
- **called from:**
- `src/tool_parsing.py:2115`

## `_strip_raw_openai_tool_call_json` — function, line 1009
- **called from:**
- `src/tool_parsing.py:2181`

## `iter_email_addresses` — function, line 1046
- **called from:**
- `src/agent_loop.py:1252`
- `src/agent_loop.py:3667`
- `src/agent_loop.py:3714`
- `src/clean_agent_preview.py:3305`
- `src/clean_agent_preview.py:3306`
- `src/clean_agent_preview.py:3308`
- `tests/test_redos_core_parsers.py:242`

## `_iter_qwen_python_args` — function, line 1066
- **called from:**
- `src/tool_parsing.py:1177`
- `tests/test_redos_core_parsers.py:204`

## `_parse_qwen3_native_text_call` — function, line 1083
- **called from:**
- `src/tool_parsing.py:2122`

## `declared_or_builtin` — function, line 1101
- **called from:**
- `src/tool_parsing.py:1126`
- `src/tool_parsing.py:1145`
- `src/tool_parsing.py:1160`
- `src/tool_parsing.py:1182`

## `_parse_tool_call_block` — function, line 1194
- **called from:**
- `src/tool_parsing.py:2009`
- `tests/test_redos_xml_tool_parsers.py:106`

## `_parse_xml_invoke` — function, line 1263
- **called from:**
- `src/tool_parsing.py:1984`
- `src/tool_parsing.py:2038`
- `src/tool_parsing.py:2059`
- `src/tool_parsing.py:2074`

## `_parse_xml_direct_tool` — function, line 1288
- **called from:**
- `src/tool_parsing.py:2043`
- `src/tool_parsing.py:2065`

## `_looks_like_json_body` — function, line 1328
- **called from:**
- `src/tool_parsing.py:2031`
- `src/tool_parsing.py:2051`

## `_parse_json_tool_call_body` — function, line 1333
- **called from:**
- `src/tool_parsing.py:2033`
- `src/tool_parsing.py:2054`

## `_iter_stepfun_tool_calls` — function, line 1368
- **called from:**
- `src/tool_parsing.py:2015`

## `_strip_stepfun_tool_markup` — function, line 1389
- **called from:**
- `src/tool_parsing.py:2175`

## `_strip_bare_invoke_markup` — function, line 1408
- **called from:**
- `src/tool_parsing.py:2200`

## `_parse_stepfun_tool_call` — function, line 1430
- **called from:**
- `src/tool_parsing.py:2016`

## `_parse_tool_code_block` — function, line 1460
- **called from:**
- `src/tool_parsing.py:2090`

## `_iter_gemma_fallback_items` — function, line 1523
- **called from:**
- `src/tool_parsing.py:1581`
- `tests/test_codeql_induced_redos.py:68`

## `_parse_gemma_tool_call` — function, line 1557
- **called from:**
- `src/tool_parsing.py:2099`
- `tests/test_codeql_induced_redos.py:69`

## `_parse_function_model_call` — function, line 1587
- **called from:**
- `src/tool_parsing.py:2108`

## `_iter_delimited` — function, line 1605
- **called from:**
- `src/tool_parsing.py:1594`
- `src/tool_parsing.py:1639`
- `src/tool_parsing.py:2006`
- `src/tool_parsing.py:2027`
- `src/tool_parsing.py:2087`
- `src/tool_parsing.py:2105`

## `_strip_delimited` — function, line 1635
- **called from:**
- `src/tool_parsing.py:1660`
- `src/tool_parsing.py:2174`
- `src/tool_parsing.py:2176`
- `src/tool_parsing.py:2178`
- `src/tool_parsing.py:2179`
- `src/tool_parsing.py:2180`
- `tests/test_redos_core_parsers.py:176`

## `strip_angle_tags` — function, line 1652
- **called from:**
- `src/agent_loop.py:6867`
- `src/agent_loop.py:30760`
- `src/agent_loop.py:33518`
- `src/clean_agent_preview.py:4482`
- `src/clean_agent_preview.py:4507`
- `src/clean_agent_preview.py:4508`
- `tests/test_redos_core_parsers.py:226`

## `_iter_named_blocks` — function, line 1663
- **called from:**
- `src/tool_parsing.py:1109`
- `src/tool_parsing.py:1115`
- `src/tool_parsing.py:1281`
- `src/tool_parsing.py:1683`
- `src/tool_parsing.py:2096`
- `tests/test_redos_core_parsers.py:172`
- `tests/test_redos_core_parsers.py:193`

## `_iter_xml_invoke` — function, line 1681
- **called from:**
- `src/tool_parsing.py:1983`
- `src/tool_parsing.py:2037`
- `src/tool_parsing.py:2058`
- `src/tool_parsing.py:2073`

## `_iter_backref_block_spans` — function, line 1686
- **called from:**
- `src/tool_parsing.py:1721`
- `src/tool_parsing.py:1784`

## `_iter_backref_blocks` — function, line 1720
- **called from:**
- `src/tool_parsing.py:1483`
- `src/tool_parsing.py:1730`

## `_iter_xml_direct` — function, line 1727
- **called from:**
- `src/tool_parsing.py:2042`
- `src/tool_parsing.py:2064`

## `_declared_tool_name_map` — function, line 1733
- **called from:**
- `src/tool_parsing.py:1099`
- `src/tool_parsing.py:1891`
- `src/tool_parsing.py:2081`
- `src/tool_parsing.py:2183`

## `_unique_declared_schema_match` — function, line 1743
- **called from:**
- `src/tool_parsing.py:1942`

## `_parse_declared_direct_xml_calls` — function, line 1775
- **called from:**
- `src/tool_parsing.py:2080`
- `src/tool_parsing.py:2182`

## `_parse_adjacent_declared_tool_fences` — function, line 1803
- **called from:**
- `src/tool_parsing.py:1892`

## `parse_tool_blocks` — function, line 1850
- **called from:**
- `scripts/eval_qwen_tool_groups_stream.py:186`
- `src/agent_loop.py:15791`
- `src/agent_loop.py:38311`
- `src/clean_agent_preview.py:6815`
- `tests/test_agent_external_tool_schemas.py:187`
- `tests/test_agent_external_tool_schemas.py:188`
- `tests/test_agent_external_tool_schemas.py:198`
- `tests/test_agent_external_tool_schemas.py:199`
- `tests/test_agent_external_tool_schemas.py:208`
- `tests/test_agent_external_tool_schemas.py:209`
- `tests/test_agent_external_tool_schemas.py:218`
- `tests/test_agent_external_tool_schemas.py:219`
- `tests/test_agent_external_tool_schemas.py:229`
- `tests/test_agent_external_tool_schemas.py:231`
- `tests/test_agent_external_tool_schemas.py:240`
- `tests/test_agent_external_tool_schemas.py:253`
- `tests/test_agent_external_tool_schemas.py:268`
- `tests/test_agent_external_tool_schemas.py:277`
- `tests/test_agent_external_tool_schemas.py:278`
- `tests/test_fenced_example_not_executed_for_native_models.py:377`
- `tests/test_fenced_example_not_executed_for_native_models.py:391`
- `tests/test_fenced_example_not_executed_for_native_models.py:404`
- `tests/test_fenced_example_not_executed_for_native_models.py:415`
- `tests/test_fenced_example_not_executed_for_native_models.py:430`
- `tests/test_fenced_example_not_executed_for_native_models.py:446`
- `tests/test_fenced_example_not_executed_for_native_models.py:462`
- `tests/test_fenced_example_not_executed_for_native_models.py:471`
- `tests/test_fenced_example_not_executed_for_native_models.py:472`
- `tests/test_fenced_inline_args.py:13`
- `tests/test_fenced_inline_args.py:18`
- `tests/test_fenced_inline_args.py:24`
- `tests/test_fenced_inline_args.py:29`
- `tests/test_fenced_inline_args.py:37`
- `tests/test_fenced_inline_args.py:42`
- `tests/test_fenced_inline_args.py:50`
- `tests/test_fenced_inline_args.py:55`
- `tests/test_fenced_inline_args.py:62`
- `tests/test_fenced_inline_args.py:69`
- `tests/test_fenced_inline_args.py:80`
- `tests/test_fenced_inline_args.py:90`
- `tests/test_fenced_inline_args.py:96`
- `tests/test_fenced_inline_args.py:103`
- `tests/test_fenced_inline_args.py:109`
- `tests/test_fenced_inline_args.py:163`
- `tests/test_fenced_invoke_no_raw_xml.py:10`
- `tests/test_fenced_invoke_no_raw_xml.py:20`
- `tests/test_fenced_invoke_no_raw_xml.py:25`
- `tests/test_fenced_invoke_no_raw_xml.py:32`
- `tests/test_fenced_invoke_no_raw_xml.py:43`
- `tests/test_fenced_invoke_no_raw_xml.py:49`
- `tests/test_fenced_invoke_no_raw_xml.py:55`
- `tests/test_function_model_tool_call.py:13`
- `tests/test_function_model_tool_call.py:28`
- `tests/test_gemma_tool_call_parsing.py:7`
- `tests/test_gemma_tool_call_parsing.py:18`
- `tests/test_gemma_tool_call_parsing.py:28`
- `tests/test_gemma_tool_call_parsing.py:38`
- `tests/test_misfenced_media_tool_call.py:10`
- `tests/test_misfenced_media_tool_call.py:22`
- `tests/test_misfenced_media_tool_call.py:34`
- … +54 more (grep the name in repo)

## `strip_tool_blocks` — function, line 2143
- **called from:**
- `routes/chat_helpers.py:1926`
- `src/agent_loop.py:560`
- `src/agent_loop.py:6399`
- `src/agent_loop.py:14495`
- `src/agent_loop.py:17910`
- `src/agent_loop.py:17957`
- `src/agent_loop.py:18177`
- `src/agent_loop.py:19460`
- `src/agent_loop.py:19481`
- `src/agent_loop.py:19499`
- `src/agent_loop.py:19515`
- `src/agent_loop.py:19526`
- `src/agent_loop.py:19938`
- `src/agent_loop.py:20315`
- `src/agent_loop.py:20727`
- `src/agent_loop.py:27999`
- `src/agent_loop.py:28321`
- `src/agent_loop.py:30526`
- `src/agent_loop.py:30629`
- `src/agent_loop.py:30638`
- `src/agent_loop.py:30792`
- `src/agent_loop.py:35430`
- `src/agent_loop.py:35487`
- `src/agent_loop.py:35573`
- `src/agent_loop.py:38122`
- `src/agent_loop.py:38202`
- `src/agent_loop.py:38487`
- `src/agent_loop.py:38570`
- `src/clean_agent_preview.py:2508`
- `src/clean_agent_preview.py:6843`
- `src/clean_agent_preview.py:6904`
- `tests/test_agent_external_tool_schemas.py:192`
- `tests/test_agent_external_tool_schemas.py:223`
- `tests/test_fenced_example_not_executed_for_native_models.py:395`
- `tests/test_fenced_example_not_executed_for_native_models.py:419`
- `tests/test_fenced_example_not_executed_for_native_models.py:434`
- `tests/test_fenced_example_not_executed_for_native_models.py:466`
- `tests/test_fenced_example_not_executed_for_native_models.py:651`
- `tests/test_fenced_example_not_executed_for_native_models.py:658`
- `tests/test_fenced_example_not_executed_for_native_models.py:670`
- `tests/test_fenced_inline_args.py:75`
- `tests/test_fenced_inline_args.py:122`
- `tests/test_fenced_inline_args.py:129`
- `tests/test_fenced_inline_args.py:135`
- `tests/test_fenced_inline_args.py:142`
- `tests/test_fenced_inline_args.py:164`
- `tests/test_function_model_tool_call.py:18`
- `tests/test_function_model_tool_call.py:29`
- `tests/test_gemma_tool_call_parsing.py:12`
- `tests/test_gemma_tool_call_parsing.py:39`
- `tests/test_gemma_tool_call_parsing.py:48`
- `tests/test_gemma_tool_call_parsing.py:59`
- `tests/test_misfenced_media_tool_call.py:122`
- `tests/test_misfenced_read_file_tool_call.py:65`
- `tests/test_plain_ui_control_open_panel.py:48`
- `tests/test_redos_core_parsers.py:179`
- `tests/test_redos_llm_parsers.py:62`
- `tests/test_redos_llm_parsers.py:69`
- `tests/test_redos_llm_parsers.py:73`
- `tests/test_streamed_tool_markup.py:24`
- … +9 more (grep the name in repo)
