# `src/model_pricing.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `match_model_key` — function, line 109
- **called from:**
- `src/model_pricing.py:188`
- `tests/test_cost_tracking.py:28`
- `tests/test_cost_tracking.py:29`
- `tests/test_cost_tracking.py:30`

## `is_local_endpoint` — function, line 119
- **called from:**
- `src/agent_loop.py:15638`
- `src/agent_loop.py:24971`
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

## `is_subscription_endpoint` — function, line 150
- **called from:**
- `src/model_pricing.py:165`
- `tests/test_cost_tracking.py:75`
- `tests/test_cost_tracking.py:76`
- `tests/test_cost_tracking.py:77`

## `is_cost_tracked_endpoint` — function, line 164
- **called from:**
- `src/model_pricing.py:181`
- `tests/test_cost_tracking.py:71`
- `tests/test_cost_tracking.py:78`

## `estimate_cost_usd` — function, line 168
- **called from:**
- `routes/chat_routes.py:1270`
- `src/agent_loop.py:16674`
- `src/agent_loop.py:23034`
- `tests/test_cost_tracking.py:35`
- `tests/test_cost_tracking.py:39`
- `tests/test_cost_tracking.py:40`
- `tests/test_cost_tracking.py:41`
- `tests/test_cost_tracking.py:61`
