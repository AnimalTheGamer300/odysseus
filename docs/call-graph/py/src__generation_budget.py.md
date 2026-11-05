# `src/generation_budget.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ContextErrorDetails` — class, line 50
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/generation_budget.py:181`

## `ContextRecoveryPlan` — class, line 57
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/generation_budget.py:217`
- `src/generation_budget.py:232`
- `src/generation_budget.py:262`

## `context_safety_margin` — function, line 63
- **called from:**
- `src/clean_agent_preview.py:5548`
- `src/generation_budget.py:151`
- `src/llm_core.py:4625`
- `src/llm_core.py:4706`
- `tests/test_generation_budget.py:18`

## `estimate_tool_schema_tokens` — function, line 78
- **called from:**
- `src/clean_agent_preview.py:5544`
- `src/generation_budget.py:120`
- `src/generation_budget.py:148`
- `src/llm_core.py:4613`
- `src/llm_core.py:4677`
- `tests/test_generation_budget.py:34`

## `estimate_multimodal_image_tokens` — function, line 90
- **called from:**
- `src/clean_agent_preview.py:5545`
- `src/generation_budget.py:119`
- `src/llm_core.py:4618`
- `src/llm_core.py:4697`
- `tests/test_generation_budget.py:52`
- `tests/test_generation_budget.py:279`

## `estimate_request_tokens` — function, line 116
- **called from:**
- `src/generation_budget.py:150`

## `fit_output_token_budget` — function, line 124
- **called from:**
- `src/agent_loop.py:26948`
- `src/agent_loop.py:27044`
- `src/agent_loop.py:28517`
- `src/agent_loop.py:30650`
- `src/agent_loop.py:32692`
- `src/generation_budget.py:248`
- `src/llm_core.py:3033`
- `src/llm_core.py:4982`
- `tests/test_generation_budget.py:32`
- `tests/test_generation_budget.py:50`
- `tests/test_generation_budget.py:66`

## `parse_context_error` — function, line 155
- **called from:**
- `src/generation_budget.py:196`
- `tests/test_generation_budget.py:78`
- `tests/test_generation_budget.py:89`
- `tests/test_generation_budget.py:99`
- `tests/test_generation_budget.py:142`

## `_first` — function, line 163
- **called from:**
- `src/generation_budget.py:182`
- `src/generation_budget.py:183`

## `plan_context_recovery` — function, line 188
- **called from:**
- `src/clean_agent_preview.py:5567`
- `src/llm_core.py:4661`
- `tests/test_generation_budget.py:111`
- `tests/test_generation_budget.py:123`
- `tests/test_generation_budget.py:143`
- `tests/test_generation_budget.py:156`
