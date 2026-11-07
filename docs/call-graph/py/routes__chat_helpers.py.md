# `routes/chat_helpers.py` — definitions & call sites

51 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `youtube_prefetch_sources` — function, line 32
- **called from:**
- `routes/chat_helpers.py:1460`
- `tests/test_youtube_prefetch_provenance.py:5`
- `tests/test_youtube_prefetch_provenance.py:23`

## `_skill_run_is_complex` — function, line 57
- **called from:**
- `routes/chat_helpers.py:2152`
- `tests/test_skill_extraction_gate.py:5`
- `tests/test_skill_extraction_gate.py:9`
- `tests/test_skill_extraction_gate.py:10`
- `tests/test_skill_extraction_gate.py:14`

## `clean_repeated_assistant_content` — function, line 62
- **called from:**
- `routes/chat_helpers.py:1929`
- `routes/chat_routes.py:234`
- `tests/test_chat_helpers.py:15`
- `tests/test_chat_helpers.py:51`
- `tests/test_chat_helpers.py:57`
- `tests/test_redos_residual_python.py:136`

## `_is_casual_low_signal` — function, line 142
- **called from:**
- `routes/chat_helpers.py:1326`
- `src/agent_loop.py:10971`
- `src/agent_loop.py:11147`
- `src/agent_loop.py:12757`
- `src/agent_loop.py:17857`
- `src/agent_loop.py:22453`

## `_truthy_request_flag` — function, line 158
- **called from:**
- `routes/chat_helpers.py:1370`

## `_sft_trace_capture_enabled` — function, line 180
- **called from:**
- `routes/chat_helpers.py:210`
- `routes/chat_helpers.py:253`

## `_json_safe` — function, line 185
- **called from:**
- `routes/chat_helpers.py:229`
- `routes/chat_helpers.py:230`
- `routes/chat_helpers.py:240`

## `_last_user_message_for_trace` — function, line 193
- **called from:**
- `routes/chat_helpers.py:226`

## `_append_sft_trace_record` — function, line 200
- **called from:**
- `routes/chat_helpers.py:1980`
- `routes/chat_helpers.py:1991`
- `tests/test_session_sft_trace_delete.py:39`

## `remove_session_sft_trace_rows` — function, line 251
- **called from:**
- `routes/session_routes.py:945`
- `routes/session_routes.py:983`
- `src/agent_tools/session_tools.py:408`
- `tests/test_session_sft_trace_delete.py:19`

## `_prune_sft_retry_rows_before_append` — function, line 296
- **called from:**
- `routes/chat_helpers.py:244`

## `strip_tui_local_context` — function, line 361
- **called from:**
- `routes/chat_helpers.py:951`
- `routes/history/history_routes.py:299`
- `routes/history/history_routes.py:505`
- `routes/history/history_routes.py:514`

## `_spawn_bg` — function, line 368
- **called from:**
- `routes/chat_helpers.py:2174`
- `routes/chat_helpers.py:2189`
- `src/builtin_mcp.py:198`
- `src/builtin_mcp.py:256`
- `tests/test_builtin_mcp_bg_tasks.py:57`

## `_prune_incognito_contexts` — function, line 376
- **called from:**
- `routes/chat_helpers.py:387`
- `routes/chat_helpers.py:398`

## `_incognito_messages` — function, line 386
- **called from:**
- `routes/chat_helpers.py:1479`

## `_append_incognito_message` — function, line 394
- **called from:**
- `routes/chat_helpers.py:1269`
- `routes/chat_helpers.py:1942`

## `PresetInfo` — class, line 413
- decorator: `dataclass`
- **called from:**
- `routes/chat_helpers.py:841`
- `tests/test_chat_document_owner_context.py:34`
- `tests/test_chat_helpers.py:662`
- `tests/test_chat_helpers.py:775`
- `tests/test_kv_cache_invalidation_2927.py:68`
- `tests/test_review_regressions.py:384`
- `tests/test_review_regressions.py:471`

## `PreprocessedMessage` — class, line 424
- decorator: `dataclass`
- **called from:**
- `routes/chat_helpers.py:866`
- `tests/test_chat_document_owner_context.py:35`
- `tests/test_chat_helpers.py:456`
- `tests/test_chat_helpers.py:653`
- `tests/test_chat_helpers.py:766`
- `tests/test_kv_cache_invalidation_2927.py:59`
- `tests/test_review_regressions.py:375`
- `tests/test_review_regressions.py:459`

## `ChatContext` — class, line 434
- decorator: `dataclass`
- **called from:**
- `routes/chat_helpers.py:1604`
- `tests/test_chat_document_owner_context.py:30`

## `_allowed_models_from_privileges` — function, line 474
- **called from:**
- `routes/chat_helpers.py:496`
- `routes/chat_helpers.py:527`

## `_allowed_models_for_request` — function, line 483
- **called from:**
- `routes/chat_routes.py:2510`
- `routes/chat_routes.py:3282`

## `_enforce_chat_privileges` — function, line 498
- **called from:**
- `routes/chat_routes.py:2496`
- `routes/chat_routes.py:3233`
- `tests/test_chat_helpers.py:95`
- `tests/test_chat_helpers.py:105`
- `tests/test_chat_helpers.py:121`
- `tests/test_chat_helpers.py:126`
- `tests/test_chat_helpers.py:136`
- `tests/test_chat_helpers.py:137`
- `tests/test_chat_helpers.py:148`
- `tests/test_chat_helpers.py:150`
- `tests/test_chat_helpers.py:164`
- `tests/test_chat_helpers.py:168`
- `tests/test_chat_helpers.py:186`
- `tests/test_chat_helpers.py:187`

## `needs_auto_name` — function, line 553
- **called from:**
- `routes/chat_helpers.py:2188`
- `tests/test_chat_helpers.py:347`

## `fallback_session_title` — function, line 565
- **called from:**
- `routes/chat_helpers.py:637`
- `routes/chat_helpers.py:691`
- `routes/chat_helpers.py:700`
- `routes/chat_helpers.py:708`
- `routes/chat_helpers.py:752`
- `routes/chat_helpers.py:799`
- `tests/test_chat_helpers.py:377`

## `auto_name_session` — function (async), line 573
- **called from:**
- `routes/chat_helpers.py:830`
- `tests/test_chat_helpers.py:532`
- `tests/test_chat_helpers.py:574`
- `tests/test_chat_helpers.py:611`
- `tests/test_utility_reasoning_effort.py:342`
- `tests/test_utility_reasoning_effort.py:362`
- `tests/test_utility_reasoning_effort.py:371`
- `tests/test_utility_reasoning_effort.py:383`
- `tests/test_utility_reasoning_effort.py:392`

## `auto_name_session_after_stream` — function (async), line 816
- **called from:**
- `routes/chat_helpers.py:2189`
- `tests/test_chat_helpers.py:370`

## `extract_preset` — function, line 836
- **called from:**
- `routes/chat_helpers.py:1244`

## `preprocess` — function (async), line 851
- **called from:**
- `routes/chat_helpers.py:1251`

## `build_uploaded_file_manifest` — function, line 875
- **called from:**
- `routes/chat_helpers.py:1316`
- `tests/test_chat_helpers.py:275`
- `tests/test_chat_helpers.py:316`

## `_read_file_can_open` — function, line 887
- **called from:**
- `routes/chat_helpers.py:913`

## `add_user_message` — function, line 931
- **called from:**
- `routes/chat_helpers.py:1290`
- `routes/chat_helpers.py:1295`
- `tests/test_chat_helpers.py:464`

## `fire_message_event` — function, line 956
- **called from:**
- `routes/chat_helpers.py:1310`

## `_session_url_matches_endpoint` — function, line 967
- **called from:**
- `routes/chat_helpers.py:1004`
- `routes/chat_routes.py:1943`
- `routes/chat_routes.py:2019`
- `routes/chat_routes.py:2097`
- `routes/chat_routes.py:2102`
- `routes/chat_routes.py:2220`
- `routes/chat_routes.py:2232`

## `_endpoint_created_sort_key` — function, line 984
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_select_session_endpoint` — function, line 993
- **called from:**
- `routes/chat_helpers.py:1074`

## `_has_auth_keys` — function, line 1030
- **called from:**
- `routes/chat_helpers.py:1045`
- `routes/chat_helpers.py:1061`

## `resolve_session_auth` — function, line 1037
- **called from:**
- `routes/chat_routes.py:2492`
- `routes/chat_routes.py:3236`
- `tests/test_chatgpt_session_binding.py:74`
- `tests/test_chatgpt_session_binding.py:90`
- `tests/test_resolve_session_auth_chatgpt.py:58`
- `tests/test_resolve_session_auth_chatgpt.py:108`
- `tests/test_resolve_session_auth_chatgpt.py:154`
- `tests/test_resolve_session_auth_chatgpt.py:212`
- `tests/test_resolve_session_auth_chatgpt.py:241`
- `tests/test_resolve_session_auth_chatgpt.py:257`
- `tests/test_resolve_session_auth_chatgpt.py:280`
- `tests/test_resolve_session_auth_chatgpt.py:300`

## `_match_cached_model_id` — function, line 1106
- **called from:**
- `routes/chat_helpers.py:1157`

## `_normalize_model_id_from_cache` — function, line 1120
- **called from:**
- `routes/chat_helpers.py:1468`

## `_session_is_research_spinoff` — function, line 1168
- **called from:**
- `routes/chat_helpers.py:1361`
- `tests/test_chat_helpers.py:480`
- `tests/test_chat_helpers.py:624`
- `tests/test_chat_helpers.py:632`
- `tests/test_chat_helpers.py:637`
- `tests/test_chat_helpers.py:641`
- `tests/test_chat_helpers.py:642`

## `build_chat_context` — function (async), line 1191
- **called from:**
- `routes/chat_routes.py:2514`
- `routes/chat_routes.py:3318`
- `tests/test_c5_rag_disable.py:63`
- `tests/test_chat_helpers.py:712`
- `tests/test_chat_helpers.py:816`
- `tests/test_context_resolution_route.py:353`
- `tests/test_context_resolution_route.py:366`
- `tests/test_context_resolution_route.py:379`
- `tests/test_kv_cache_invalidation_2927.py:139`
- `tests/test_kv_cache_invalidation_2927.py:151`
- `tests/test_kv_cache_invalidation_2927.py:191`
- `tests/test_kv_cache_invalidation_2927.py:209`
- `tests/test_review_regressions.py:423`
- `tests/test_review_regressions.py:486`

## `_tail_insert` — function, line 1481
- **called from:**
- `routes/chat_helpers.py:1503`
- `routes/chat_helpers.py:1543`
- `routes/chat_helpers.py:1551`

## `accumulate_token_usage` — function, line 1628
- **called from:**
- `routes/chat_helpers.py:2178`
- `routes/chat_routes.py:4754`
- `routes/chat_routes.py:5243`
- `tests/test_cost_tracking.py:155`
- `tests/test_cost_tracking.py:156`
- `tests/test_cost_tracking.py:172`
- `tests/test_cost_tracking.py:173`
- `tests/test_cost_tracking.py:174`

## `_normalize_thinking` — function, line 1656
- **called from:**
- `routes/chat_helpers.py:1823`
- `tests/test_redos_residual_python.py:150`
- `tests/test_review_regressions.py:343`

## `_extract_thinking_meta` — function, line 1793
- **called from:**
- `routes/chat_helpers.py:1841`
- `routes/chat_helpers.py:1932`

## `clean_thinking_for_save` — function, line 1838
- **called from:**
- `routes/chat_routes.py:1501`
- `routes/chat_routes.py:2603`
- `routes/chat_routes.py:4196`
- `tests/test_chat_helpers.py:67`
- `tests/test_chat_helpers.py:385`
- `tests/test_chat_helpers.py:396`
- `tests/test_chat_helpers.py:406`
- `tests/test_chat_helpers.py:416`
- `tests/test_chat_helpers.py:426`

## `save_assistant_response` — function, line 1868
- **called from:**
- `routes/chat_routes.py:4744`
- `routes/chat_routes.py:4832`
- `routes/chat_routes.py:4883`
- `routes/chat_routes.py:5230`
- `routes/chat_routes.py:5292`
- `routes/chat_routes.py:5359`
- `routes/chat_routes.py:5415`
- `tests/test_chat_helpers.py:440`

## `_model_value` — function, line 1893
- **called from:**
- `routes/chat_helpers.py:1900`
- `routes/chat_helpers.py:1901`

## `_is_session_stream_active` — function, line 2001
- **called from:**
- `routes/chat_helpers.py:820`
- `routes/chat_helpers.py:2032`
- `routes/chat_helpers.py:2040`

## `_run_extraction_jobs_sequentially` — function (async), line 2014
- **called from:**
- `routes/chat_helpers.py:2174`
- `tests/test_kv_cache_invalidation_2927.py:261`

## `run_post_response_tasks` — function, line 2049
- **called from:**
- `routes/chat_routes.py:2632`
- `routes/chat_routes.py:4846`
- `routes/chat_routes.py:5307`
- `routes/chat_routes.py:5371`
- `tests/test_kv_cache_invalidation_2927.py:325`
