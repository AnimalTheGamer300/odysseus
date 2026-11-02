# `src/model_context.py` — definitions & call sites

15 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_in_tailscale_range` — function, line 33
- **called from:**
- `src/model_context.py:99`

## `_is_private_ip_literal` — function, line 40
- **called from:**
- `src/model_context.py:99`

## `_normalize_base_for_compare` — function, line 48
- **called from:**
- `src/model_context.py:58`
- `src/model_context.py:69`

## `_configured_endpoint_kind` — function, line 56
- **called from:**
- `src/model_context.py:92`
- `src/model_context.py:313`
- `src/model_context.py:470`

## `is_local_endpoint` — function, line 90
- **called from:**
- `src/llm_core.py:92`
- `src/llm_core.py:1049`
- `src/llm_core.py:1090`
- `src/model_context.py:314`
- `src/model_context.py:490`
- `src/model_context.py:535`
- `tests/test_model_context.py:59`
- `tests/test_model_context.py:62`
- `tests/test_model_context.py:65`
- `tests/test_model_context.py:68`
- `tests/test_model_context.py:76`
- `tests/test_model_context.py:80`
- `tests/test_model_context.py:92`
- `tests/test_model_context.py:95`
- `tests/test_model_context.py:98`
- `tests/test_model_context.py:101`
- `tests/test_model_context.py:104`

## `_context_length_override` — function, line 280
- **called from:**
- `src/model_context.py:309`

## `_get_context_length_cached` — function, line 304
- **called from:**
- `src/model_context.py:340`
- `src/model_context.py:349`

## `get_context_length` — function, line 333
- **called from:**
- `routes/chat_helpers.py:969`
- `routes/history/history_routes.py:993`
- `routes/history/history_routes.py:1103`
- `routes/session_routes.py:1234`
- `routes/session_routes.py:1577`
- `scripts/dump_agent_prompt.py:303`
- `src/context_compactor.py:433`
- `src/context_compactor.py:478`
- `tests/test_budget_auto_sentinel.py:82`
- `tests/test_context_cache_per_endpoint.py:24`
- `tests/test_context_cache_per_endpoint.py:26`
- `tests/test_context_cache_per_endpoint.py:32`
- `tests/test_context_cache_per_endpoint.py:33`
- `tests/test_context_cache_per_endpoint.py:38`
- `tests/test_context_cache_per_endpoint.py:39`
- `tests/test_model_context.py:220`
- `tests/test_model_context.py:221`
- `tests/test_model_context.py:239`
- `tests/test_model_context.py:240`
- `tests/test_model_context.py:267`
- `tests/test_model_context.py:286`
- `tests/test_model_context.py:288`
- `tests/test_model_context.py:302`
- `tests/test_model_context.py:314`

## `get_context_length_known` — function, line 343
- **called from:**
- `src/llm_core.py:2323`
- `src/llm_core.py:2742`
- `src/llm_core.py:2999`
- `src/model_context.py:363`
- `tests/test_budget_auto_sentinel.py:74`
- `tests/test_budget_auto_sentinel.py:77`

## `budget_context_for_model` — function, line 352
- **called from:**
- `src/agent_loop.py:4723`
- `tests/test_budget_auto_sentinel.py:93`
- `tests/test_budget_auto_sentinel.py:96`
- `tests/test_budget_auto_sentinel.py:99`
- `tests/test_budget_auto_sentinel.py:102`
- `tests/test_budget_auto_sentinel.py:110`

## `_lookup_known` — function, line 369
- **called from:**
- `src/model_context.py:468`
- `tests/test_model_context.py:156`
- `tests/test_model_context.py:159`
- `tests/test_model_context.py:162`
- `tests/test_model_context.py:165`
- `tests/test_model_context.py:168`
- `tests/test_model_context.py:172`
- `tests/test_model_context.py:177`
- `tests/test_model_context.py:182`
- `tests/test_model_context.py:185`
- `tests/test_model_context.py:188`
- `tests/test_model_context.py:191`

## `_model_ctx_from_entry` — function, line 388
- **called from:**
- `src/model_context.py:446`
- `src/model_context.py:527`

## `_proxy_catalog_context` — function, line 423
- **called from:**
- `src/model_context.py:483`

## `_query_context_length` — function, line 465
- **called from:**
- `src/model_context.py:323`
- `tests/test_llama_server_models_url.py:54`

## `estimate_tokens` — function, line 552
- **called from:**
- `routes/chat_helpers.py:976`
- `routes/chat_helpers.py:980`
- `routes/chat_routes.py:221`
- `routes/chat_routes.py:222`
- `routes/chat_routes.py:2348`
- `routes/chat_routes.py:2396`
- `routes/chat_routes.py:2483`
- `routes/history/history_routes.py:992`
- `routes/history/history_routes.py:1102`
- `routes/history/history_routes.py:1232`
- `scripts/dump_agent_prompt.py:261`
- `scripts/dump_agent_prompt.py:458`
- `scripts/dump_agent_prompt.py:528`
- `src/agent_loop.py:3704`
- `src/agent_loop.py:4150`
- `src/agent_loop.py:4231`
- `src/agent_loop.py:4407`
- `src/agent_loop.py:4423`
- `src/agent_loop.py:4732`
- `src/agent_loop.py:4755`
- `src/agent_loop.py:4890`
- `src/agent_loop.py:5456`
- `src/agent_loop.py:5478`
- `src/agent_loop.py:5925`
- `src/agent_loop.py:7026`
- `src/context_compactor.py:266`
- `src/context_compactor.py:323`
- `src/context_compactor.py:343`
- `src/context_compactor.py:360`
- `src/context_compactor.py:365`
- `src/context_compactor.py:379`
- `src/context_compactor.py:393`
- `src/context_compactor.py:398`
- `src/context_compactor.py:403`
- `src/context_compactor.py:405`
- `src/context_compactor.py:409`
- `src/context_compactor.py:434`
- `src/context_compactor.py:493`
- `src/context_compactor.py:610`
- `tests/test_compact_truncate_tool_call_args.py:45`
- `tests/test_compact_truncate_tool_call_args.py:45`
- `tests/test_estimate_tokens_tool_calls.py:23`
- `tests/test_estimate_tokens_tool_calls.py:31`
- `tests/test_estimate_tokens_tool_calls.py:41`
- `tests/test_estimate_tokens_tool_calls.py:46`
- `tests/test_estimate_tokens_tool_calls.py:47`
- `tests/test_model_context.py:109`
- `tests/test_model_context.py:113`
- `tests/test_model_context.py:122`
- `tests/test_model_context.py:137`
- `tests/test_model_context.py:143`
- `tests/test_model_context.py:148`
- `tests/test_model_context.py:150`
