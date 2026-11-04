# `routes/chat_helpers.py` — definitions & call sites

36 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_casual_low_signal` — function, line 56
- **called from:**
- `routes/chat_helpers.py:774`
- `src/agent_loop.py:1575`
- `src/agent_loop.py:4110`

## `_spawn_bg` — function, line 83
- **called from:**
- `routes/chat_helpers.py:1475`
- `routes/chat_helpers.py:1490`
- `src/builtin_mcp.py:197`
- `src/builtin_mcp.py:254`
- `tests/test_builtin_mcp_bg_tasks.py:57`

## `_prune_incognito_contexts` — function, line 91
- **called from:**
- `routes/chat_helpers.py:102`
- `routes/chat_helpers.py:113`

## `_incognito_messages` — function, line 101
- **called from:**
- `routes/chat_helpers.py:887`

## `_append_incognito_message` — function, line 109
- **called from:**
- `routes/chat_helpers.py:724`
- `routes/chat_helpers.py:1287`

## `PresetInfo` — class, line 128
- decorator: `dataclass`
- **called from:**
- `routes/chat_helpers.py:375`
- `tests/test_chat_helpers.py:485`
- `tests/test_kv_cache_invalidation_2927.py:68`
- `tests/test_review_regressions.py:382`
- `tests/test_review_regressions.py:464`

## `PreprocessedMessage` — class, line 137
- decorator: `dataclass`
- **called from:**
- `routes/chat_helpers.py:398`
- `tests/test_chat_helpers.py:364`
- `tests/test_chat_helpers.py:476`
- `tests/test_kv_cache_invalidation_2927.py:59`
- `tests/test_review_regressions.py:373`
- `tests/test_review_regressions.py:452`

## `ChatContext` — class, line 147
- decorator: `dataclass`
- **called from:**
- `routes/chat_helpers.py:1004`

## `_allowed_models_from_privileges` — function, line 187
- **called from:**
- `routes/chat_helpers.py:209`
- `routes/chat_helpers.py:240`

## `_allowed_models_for_request` — function, line 196
- **called from:**
- `routes/chat_routes.py:984`
- `routes/chat_routes.py:1546`

## `_enforce_chat_privileges` — function, line 211
- **called from:**
- `routes/chat_routes.py:970`
- `routes/chat_routes.py:1497`
- `tests/test_chat_helpers.py:49`
- `tests/test_chat_helpers.py:59`
- `tests/test_chat_helpers.py:75`
- `tests/test_chat_helpers.py:80`
- `tests/test_chat_helpers.py:90`
- `tests/test_chat_helpers.py:91`
- `tests/test_chat_helpers.py:102`
- `tests/test_chat_helpers.py:104`
- `tests/test_chat_helpers.py:118`
- `tests/test_chat_helpers.py:122`
- `tests/test_chat_helpers.py:140`
- `tests/test_chat_helpers.py:141`

## `needs_auto_name` — function, line 266
- **called from:**
- `routes/chat_helpers.py:1489`
- `tests/test_chat_helpers.py:301`

## `auto_name_session` — function (async), line 278
- **called from:**
- `routes/chat_helpers.py:1490`
- `tests/test_chat_helpers.py:428`

## `extract_preset` — function, line 370
- **called from:**
- `routes/chat_helpers.py:705`

## `preprocess` — function (async), line 383
- **called from:**
- `routes/chat_helpers.py:712`

## `build_uploaded_file_manifest` — function, line 407
- **called from:**
- `routes/chat_helpers.py:764`
- `tests/test_chat_helpers.py:229`
- `tests/test_chat_helpers.py:270`

## `_read_file_can_open` — function, line 419
- **called from:**
- `routes/chat_helpers.py:445`

## `add_user_message` — function, line 463
- **called from:**
- `routes/chat_helpers.py:745`
- `routes/chat_helpers.py:750`
- `tests/test_chat_helpers.py:372`

## `fire_message_event` — function, line 474
- **called from:**
- `routes/chat_helpers.py:758`

## `_session_url_matches_endpoint` — function, line 485
- **called from:**
- `routes/chat_helpers.py:535`
- `routes/chat_routes.py:597`
- `routes/chat_routes.py:664`
- `routes/chat_routes.py:731`
- `routes/chat_routes.py:849`

## `_has_auth_keys` — function, line 502
- **called from:**
- `routes/chat_helpers.py:516`
- `routes/chat_helpers.py:555`

## `resolve_session_auth` — function, line 509
- **called from:**
- `routes/chat_routes.py:1500`
- `tests/test_resolve_session_auth_chatgpt.py:58`
- `tests/test_resolve_session_auth_chatgpt.py:108`
- `tests/test_resolve_session_auth_chatgpt.py:154`

## `_match_cached_model_id` — function, line 574
- **called from:**
- `routes/chat_helpers.py:625`

## `_normalize_model_id_from_cache` — function, line 588
- **called from:**
- `routes/chat_helpers.py:876`

## `_session_is_research_spinoff` — function, line 636
- **called from:**
- `routes/chat_helpers.py:800`
- `tests/test_chat_helpers.py:388`
- `tests/test_chat_helpers.py:447`
- `tests/test_chat_helpers.py:455`
- `tests/test_chat_helpers.py:460`
- `tests/test_chat_helpers.py:464`
- `tests/test_chat_helpers.py:465`

## `build_chat_context` — function (async), line 659
- **called from:**
- `routes/chat_routes.py:988`
- `routes/chat_routes.py:1550`
- `tests/test_chat_helpers.py:535`
- `tests/test_kv_cache_invalidation_2927.py:139`
- `tests/test_kv_cache_invalidation_2927.py:151`
- `tests/test_kv_cache_invalidation_2927.py:191`
- `tests/test_kv_cache_invalidation_2927.py:209`
- `tests/test_review_regressions.py:417`
- `tests/test_review_regressions.py:479`

## `_tail_insert` — function, line 889
- **called from:**
- `routes/chat_helpers.py:911`
- `routes/chat_helpers.py:951`
- `routes/chat_helpers.py:959`

## `accumulate_token_usage` — function, line 1028
- **called from:**
- `routes/chat_helpers.py:1479`
- `routes/chat_routes.py:2453`
- `routes/chat_routes.py:2852`

## `_normalize_thinking` — function, line 1047
- **called from:**
- `routes/chat_helpers.py:1195`
- `tests/test_review_regressions.py:341`

## `_extract_thinking_meta` — function, line 1165
- **called from:**
- `routes/chat_helpers.py:1213`
- `routes/chat_helpers.py:1277`

## `clean_thinking_for_save` — function, line 1210
- **called from:**
- `routes/chat_routes.py:305`
- `routes/chat_routes.py:1072`
- `routes/chat_routes.py:1903`
- `tests/test_chat_helpers.py:305`
- `tests/test_chat_helpers.py:316`
- `tests/test_chat_helpers.py:326`
- `tests/test_chat_helpers.py:336`

## `save_assistant_response` — function, line 1223
- **called from:**
- `routes/chat_routes.py:2443`
- `routes/chat_routes.py:2514`
- `routes/chat_routes.py:2562`
- `routes/chat_routes.py:2839`
- `routes/chat_routes.py:2890`
- `routes/chat_routes.py:2943`
- `tests/test_chat_helpers.py:348`

## `_model_value` — function, line 1248
- **called from:**
- `routes/chat_helpers.py:1255`
- `routes/chat_helpers.py:1256`

## `_is_session_stream_active` — function, line 1331
- **called from:**
- `routes/chat_helpers.py:1362`
- `routes/chat_helpers.py:1370`

## `_run_extraction_jobs_sequentially` — function (async), line 1344
- **called from:**
- `routes/chat_helpers.py:1475`
- `tests/test_kv_cache_invalidation_2927.py:261`

## `run_post_response_tasks` — function, line 1379
- **called from:**
- `routes/chat_routes.py:1101`
- `routes/chat_routes.py:2528`
- `routes/chat_routes.py:2902`
- `tests/test_kv_cache_invalidation_2927.py:325`
