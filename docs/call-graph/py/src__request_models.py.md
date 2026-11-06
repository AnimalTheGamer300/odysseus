# `src/request_models.py` — definitions & call sites

14 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ChatRequest` — class, line 7
- **called from:**
- `tests/test_api_token_tool_authority.py:580`
- `tests/test_foreground_model_routing.py:1242`
- `tests/test_foreground_model_routing.py:1282`
- `tests/test_foreground_model_routing.py:1318`
- `tests/test_foreground_model_routing.py:1396`
- `tests/test_foreground_model_routing.py:1431`
- `tests/test_foreground_model_routing.py:1466`
- `tests/test_foreground_model_routing.py:1501`
- `tests/test_foreground_model_routing.py:1565`
- `tests/test_foreground_model_routing.py:1637`
- `tests/test_foreground_model_routing.py:1676`
- `tests/test_foreground_model_routing.py:1708`
- `tests/test_foreground_model_routing.py:1871`
- `tests/test_history_display_model_hydration.py:527`

## `ChatRequest.validate_reasoning_effort` — method, line 20
- decorator: `field_validator('reasoning_effort')`
- decorator: `classmethod`
- **called from:**
- `routes/chat_routes.py:2471`
- `routes/chat_routes.py:3010`
- `routes/history/history_routes.py:268`
- `src/utility_effort.py:80`
- `src/utility_effort.py:87`
- `src/utility_effort.py:127`
- `tests/test_chatgpt_reasoning_and_grouping.py:137`
- `tests/test_chatgpt_reasoning_and_grouping.py:138`
- `tests/test_chatgpt_reasoning_and_grouping.py:139`
- `tests/test_chatgpt_reasoning_and_grouping.py:140`
- `tests/test_chatgpt_reasoning_and_grouping.py:141`
- `tests/test_chatgpt_reasoning_and_grouping.py:142`
- `tests/test_chatgpt_reasoning_and_grouping.py:143`
- `tests/test_utility_reasoning_effort.py:133`
- `tests/test_utility_reasoning_effort.py:134`
- `tests/test_utility_reasoning_effort.py:135`

## `ChatRequest.clean_message` — method, line 32
- decorator: `field_validator('message')`
- decorator: `classmethod`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ChatRequest.validate_time_filter` — method, line 37
- decorator: `field_validator('time_filter')`
- decorator: `classmethod`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SessionCreateRequest` — class, line 43
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `MemoryAddRequest` — class, line 50
- **called from:**
- `routes/codex_routes.py:452`
- `routes/memory/memory_routes.py:110`
- `tests/test_memory_routes_session_owner.py:177`

## `MemoryAddRequest.validate_category` — method, line 58
- decorator: `field_validator('category')`
- decorator: `classmethod`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `MemoryUpdateRequest` — class, line 64
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `PresetUpdateRequest` — class, line 69
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DirectoryRequest` — class, line 129
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ErrorResponse` — class, line 140
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `UploadResponse` — class, line 146
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SessionResponse` — class, line 156
- **called from:**
- `routes/session_routes.py:685`

## `MemoryResponse` — class, line 165
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
