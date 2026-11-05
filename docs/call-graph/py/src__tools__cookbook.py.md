# `src/tools/cookbook.py` — definitions & call sites

48 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_string_arg` — function, line 29
- **called from:**
- `src/tools/cookbook.py:34`
- `src/tools/cookbook.py:35`
- `src/tools/cookbook.py:1359`
- `src/tools/cookbook.py:1360`
- `src/tools/cookbook.py:1522`
- `src/tools/cookbook.py:1527`
- `src/tools/cookbook.py:1549`
- `src/tools/cookbook.py:1624`

## `_validate_cookbook_ssh_target` — function, line 33
- **called from:**
- `src/tools/cookbook.py:1224`
- `src/tools/cookbook.py:1380`
- `src/tools/cookbook.py:1654`

## `_cookbook_label_key` — function, line 39
- **called from:**
- `src/tools/cookbook.py:181`
- `src/tools/cookbook.py:193`
- `src/tools/cookbook.py:193`

## `_cookbook_is_exact_repo_id` — function, line 43
- **called from:**
- `src/tools/cookbook.py:104`
- `src/tools/cookbook.py:185`
- `src/tools/cookbook.py:1534`

## `_hf_official_author_for_query` — function, line 102
- **called from:**
- `src/tools/cookbook.py:1531`

## `_hf_query_mentions_quant` — function, line 113
- **called from:**
- `src/tools/cookbook.py:1533`

## `_hf_query_terms` — function, line 118
- **called from:**
- `src/tools/cookbook.py:1568`

## `_hf_row_text` — function, line 131
- **called from:**
- `src/tools/cookbook.py:145`
- `src/tools/cookbook.py:150`

## `_hf_model_matches_terms` — function, line 142
- **called from:**
- `src/tools/cookbook.py:1572`

## `_hf_model_is_quant_variant` — function, line 149
- **called from:**
- `src/tools/cookbook.py:1582`
- `src/tools/cookbook.py:1586`

## `_hf_format_model_search_output` — function, line 154
- **called from:**
- `src/tools/cookbook.py:1592`

## `_cookbook_match_saved_preset` — function, line 173
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_cookbook_servers` — function (async), line 216
- **called from:**
- `src/tools/cookbook.py:257`
- `src/tools/cookbook.py:754`
- `src/tools/cookbook.py:820`
- `src/tools/cookbook.py:1779`

## `_resolve_cookbook_host` — function (async), line 246
- **called from:**
- `src/tools/cookbook.py:748`
- `src/tools/cookbook.py:818`
- `src/tools/cookbook.py:2038`

## `_cookbook_env_for_host` — function (async), line 275
- **called from:**
- `src/tools/cookbook.py:769`
- `src/tools/cookbook.py:830`
- `src/tools/cookbook.py:1906`

## `_infer_serve_port` — function, line 341
- **called from:**
- `src/tools/cookbook.py:380`

## `_infer_serve_host` — function, line 362
- **called from:**
- `src/tools/cookbook.py:379`

## `_ensure_served_endpoint` — function (async), line 370
- **called from:**
- `src/tools/cookbook.py:874`
- `src/tools/cookbook.py:1927`

## `_cookbook_register_task` — function (async), line 416
- **called from:**
- `src/tools/cookbook.py:783`
- `src/tools/cookbook.py:877`
- `src/tools/cookbook.py:1930`

## `_cookbook_apply_retry_suggestion` — function, line 515
- **called from:**
- `src/tools/cookbook.py:1002`

## `_cookbook_engine_from_model_info` — function, line 542
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_cookbook_default_launch_cmd` — function, line 578
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_cookbook_hf_model_info` — function (async), line 599
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_cookbook_host_meta` — function, line 651
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_cookbook_find_task` — function, line 660
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_cookbook_phase` — function, line 669
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_scan_running_model_processes` — function, line 675
- **called from:**
- `tests/test_cookbook_stop_without_procfs.py:302`

## `do_download_model` — function (async), line 734
- **called from:**
- `src/tool_execution.py:2421`

## `do_serve_model` — function (async), line 804
- **called from:**
- `src/tool_execution.py:2424`

## `do_list_served_models` — function (async), line 921
- **called from:**
- `src/tool_execution.py:2427`

## `_rank` — function, line 971
- **called from:**
- `src/tools/cookbook.py:978`

## `_capture_session_processes` — function (async), line 1040
- **called from:**
- `src/tools/cookbook.py:1245`

## `_snapshot` — function, line 1086
- **called from:**
- `src/browser_lifecycle.py:176`
- `tests/test_cookbook_error_tail_lines.py:19`
- `tests/test_cookbook_error_tail_lines.py:28`
- `tests/test_cookbook_error_tail_lines.py:38`
- `tests/test_cookbook_error_tail_lines.py:51`
- `static/js/features/notes/ui/drawing.js:205`
- `static/js/features/notes/ui/drawing.js:280`

## `_sweep_session_survivors` — function, line 1106
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_unowned_match_note` — function, line 1155
- **called from:**
- `src/tools/cookbook.py:1151`

## `_cookbook_kill_session` — function (async), line 1184
- **called from:**
- `src/tools/cookbook.py:1323`
- `src/tools/cookbook.py:1503`
- `tests/test_runtime_resource_integration.py:353`

## `do_stop_served_model` — function (async), line 1314
- **called from:**
- `src/tool_execution.py:2430`
- `tests/test_cookbook_agent_tool_ssh_validation.py:51`
- `tests/test_cookbook_agent_tool_ssh_validation.py:75`
- `tests/test_cookbook_agent_tool_ssh_validation.py:88`
- `tests/test_cookbook_agent_tool_ssh_validation.py:107`
- `tests/test_cookbook_stop_without_procfs.py:162`
- `tests/test_cookbook_stop_without_procfs.py:194`
- `tests/test_cookbook_stop_without_procfs.py:216`
- `tests/test_cookbook_stop_without_procfs.py:245`
- `tests/test_cookbook_stop_without_procfs.py:281`
- `tests/test_cookbook_stop_without_procfs.py:328`
- `tests/test_cookbook_stop_without_procfs.py:363`

## `do_tail_serve_output` — function (async), line 1331
- **called from:**
- `src/tool_execution.py:2433`
- `tests/test_cookbook_agent_tool_ssh_validation.py:166`
- `tests/test_cookbook_agent_tool_ssh_validation.py:190`

## `do_list_downloads` — function (async), line 1470
- **called from:**
- `src/tool_execution.py:2436`

## `do_cancel_download` — function (async), line 1494
- **called from:**
- `src/tool_execution.py:2439`
- `tests/test_cookbook_agent_tool_ssh_validation.py:129`
- `tests/test_cookbook_agent_tool_ssh_validation.py:153`

## `do_search_hf_models` — function (async), line 1511
- **called from:**
- `src/tool_execution.py:2442`
- `tests/test_search_hf_models_tool.py:66`
- `tests/test_search_hf_models_tool.py:88`
- `tests/test_search_hf_models_tool.py:97`

## `do_adopt_served_model` — function (async), line 1601
- **called from:**
- `src/tool_execution.py:2457`
- `tests/test_cookbook_agent_tool_ssh_validation.py:203`
- `tests/test_cookbook_tool_dry_run.py:32`

## `do_list_cookbook_servers` — function (async), line 1774
- **called from:**
- `src/tool_execution.py:2460`

## `do_list_serve_presets` — function (async), line 1798
- **called from:**
- `src/tool_execution.py:2451`

## `do_serve_preset` — function (async), line 1839
- **called from:**
- `src/tool_execution.py:2454`
- `tests/test_cookbook_tool_dry_run.py:56`

## `do_list_cached_models` — function (async), line 1942
- **called from:**
- `src/tool_execution.py:2445`
- `tests/test_cached_model_scan_failures.py:20`
- `tests/test_cached_model_scan_failures.py:39`
- `tests/test_cached_model_scan_failures.py:57`
- `tests/test_cached_model_scan_failures.py:86`

## `_scan_one` — function (async), line 1959
- **called from:**
- `src/tools/cookbook.py:2046`
- `src/tools/cookbook.py:2059`
- `src/tools/cookbook.py:2067`
- `src/tools/cookbook.py:2075`

## `_dirs_for` — function, line 2019
- **called from:**
- `routes/codex_routes.py:774`
- `src/tools/cookbook.py:2046`
- `src/tools/cookbook.py:2060`
- `src/tools/cookbook.py:2067`
- `src/tools/cookbook.py:2080`
