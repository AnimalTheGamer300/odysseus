# `src/model_context.py` — definitions & call sites

16 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

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
- `src/model_context.py:315`
- `src/model_context.py:472`

## `is_local_endpoint` — function, line 90
- **called from:**
- `src/agent_loop.py:15638`
- `src/agent_loop.py:24991`
- `src/agent_runtime/context_resolution.py:430`
- `src/llm_core.py:35`
- `src/llm_core.py:121`
- `src/llm_core.py:1196`
- `src/llm_core.py:1237`
- `src/llm_core.py:1285`
- `src/llm_core.py:1323`
- `src/llm_core.py:1334`
- `src/model_context.py:316`
- `src/model_context.py:492`
- `src/model_context.py:551`
- `src/model_pricing.py:165`
- `tests/test_cost_tracking.py:59`
- `tests/test_cost_tracking.py:70`
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

## `_context_length_override` — function, line 282
- **called from:**
- `src/model_context.py:311`

## `_get_context_length_cached` — function, line 306
- **called from:**
- `src/model_context.py:342`
- `src/model_context.py:351`

## `get_context_length` — function, line 335
- **called from:**
- `routes/chat_helpers.py:1567`
- `routes/history/history_routes.py:1212`
- `routes/history/history_routes.py:1502`
- `routes/session_routes.py:1387`
- `routes/session_routes.py:1758`
- `scripts/dump_agent_prompt.py:303`
- `src/context_compactor.py:670`
- `src/context_compactor.py:747`
- `src/llm_core.py:3051`
- `src/llm_core.py:5000`
- `tests/test_budget_auto_sentinel.py:82`
- `tests/test_context_cache_per_endpoint.py:24`
- `tests/test_context_cache_per_endpoint.py:26`
- `tests/test_context_cache_per_endpoint.py:32`
- `tests/test_context_cache_per_endpoint.py:33`
- `tests/test_context_cache_per_endpoint.py:38`
- `tests/test_context_cache_per_endpoint.py:39`
- `tests/test_model_context.py:237`
- `tests/test_model_context.py:238`
- `tests/test_model_context.py:256`
- `tests/test_model_context.py:257`
- `tests/test_model_context.py:284`
- `tests/test_model_context.py:303`
- `tests/test_model_context.py:305`
- `tests/test_model_context.py:319`
- `tests/test_model_context.py:331`

## `get_context_length_known` — function, line 345
- **called from:**
- `src/llm_core.py:2677`
- `src/llm_core.py:3148`
- `src/llm_core.py:3420`
- `src/model_context.py:365`
- `tests/test_budget_auto_sentinel.py:74`
- `tests/test_budget_auto_sentinel.py:77`

## `budget_context_for_model` — function, line 354
- **called from:**
- `src/agent_loop.py:24598`
- `tests/test_budget_auto_sentinel.py:93`
- `tests/test_budget_auto_sentinel.py:96`
- `tests/test_budget_auto_sentinel.py:99`
- `tests/test_budget_auto_sentinel.py:102`
- `tests/test_budget_auto_sentinel.py:110`

## `_lookup_known` — function, line 371
- **called from:**
- `src/agent_runtime/context_resolution.py:491`
- `src/model_context.py:470`
- `tests/test_model_context.py:170`
- `tests/test_model_context.py:173`
- `tests/test_model_context.py:176`
- `tests/test_model_context.py:179`
- `tests/test_model_context.py:182`
- `tests/test_model_context.py:185`
- `tests/test_model_context.py:189`
- `tests/test_model_context.py:194`
- `tests/test_model_context.py:199`
- `tests/test_model_context.py:202`
- `tests/test_model_context.py:205`
- `tests/test_model_context.py:208`

## `_model_ctx_from_entry` — function, line 390
- **called from:**
- `src/agent_runtime/context_resolution.py:381`
- `src/model_context.py:448`
- `src/model_context.py:543`

## `_proxy_catalog_context` — function, line 425
- **called from:**
- `src/model_context.py:485`

## `_query_context_length` — function, line 467
- **called from:**
- `src/model_context.py:325`
- `tests/test_llama_server_models_url.py:54`
- `tests/test_llama_server_models_url.py:79`

## `estimate_text_tokens` — function, line 568
- **called from:**
- `src/context_compactor.py:363`
- `src/context_compactor.py:376`
- `src/context_compactor.py:387`
- `src/context_compactor.py:397`
- `src/context_compactor.py:432`
- `src/model_context.py:602`
- `src/model_context.py:606`
- `src/model_context.py:622`
- `src/model_context.py:635`
- `src/model_context.py:639`

## `estimate_tokens` — function, line 585
- **called from:**
- `routes/chat_helpers.py:1576`
- `routes/chat_helpers.py:1580`
- `routes/chat_routes.py:1417`
- `routes/chat_routes.py:1418`
- `routes/chat_routes.py:4648`
- `routes/chat_routes.py:4697`
- `routes/chat_routes.py:4786`
- `routes/history/history_routes.py:1211`
- `routes/history/history_routes.py:1501`
- `routes/history/history_routes.py:1639`
- `scripts/dump_agent_prompt.py:261`
- `scripts/dump_agent_prompt.py:458`
- `scripts/dump_agent_prompt.py:528`
- `src/agent_loop.py:16634`
- `src/agent_loop.py:22124`
- `src/agent_loop.py:22214`
- `src/agent_loop.py:22338`
- `src/agent_loop.py:22374`
- `src/agent_loop.py:22549`
- `src/agent_loop.py:22785`
- `src/agent_loop.py:22999`
- `src/agent_loop.py:23015`
- `src/agent_loop.py:24623`
- `src/agent_loop.py:24713`
- `src/agent_loop.py:25368`
- `src/agent_loop.py:26852`
- `src/agent_loop.py:27132`
- `src/agent_loop.py:27671`
- `src/agent_loop.py:28556`
- `src/agent_loop.py:30705`
- `src/agent_loop.py:32779`
- `src/agent_loop.py:38871`
- `src/context_compactor.py:425`
- `src/context_compactor.py:482`
- `src/context_compactor.py:502`
- `src/context_compactor.py:538`
- `src/context_compactor.py:543`
- `src/context_compactor.py:557`
- `src/context_compactor.py:603`
- `src/context_compactor.py:607`
- `src/context_compactor.py:615`
- `src/context_compactor.py:618`
- `src/context_compactor.py:628`
- `src/context_compactor.py:634`
- `src/context_compactor.py:638`
- `src/context_compactor.py:671`
- `src/context_compactor.py:707`
- `src/context_compactor.py:763`
- `src/context_compactor.py:884`
- `src/generation_budget.py:118`
- `tests/test_compact_truncate_tool_call_args.py:45`
- `tests/test_compact_truncate_tool_call_args.py:45`
- `tests/test_context_compactor.py:90`
- `tests/test_context_compactor.py:116`
- `tests/test_context_compactor.py:791`
- `tests/test_context_resolution.py:480`
- `tests/test_estimate_tokens_tool_calls.py:23`
- `tests/test_estimate_tokens_tool_calls.py:31`
- `tests/test_estimate_tokens_tool_calls.py:41`
- `tests/test_estimate_tokens_tool_calls.py:46`
- … +11 more (grep the name in repo)
