# `src/request_models.py` — definitions & call sites

14 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ChatRequest` — class, line 7
- **called from:**
- `tests/test_api_token_tool_authority.py:217`
- `tests/test_foreground_model_routing.py:1188`
- `tests/test_foreground_model_routing.py:1228`
- `tests/test_foreground_model_routing.py:1264`
- `tests/test_foreground_model_routing.py:1342`
- `tests/test_foreground_model_routing.py:1377`
- `tests/test_foreground_model_routing.py:1412`
- `tests/test_foreground_model_routing.py:1447`
- `tests/test_foreground_model_routing.py:1511`
- `tests/test_foreground_model_routing.py:1583`
- `tests/test_foreground_model_routing.py:1622`
- `tests/test_foreground_model_routing.py:1654`
- `tests/test_foreground_model_routing.py:1787`
- `tests/test_history_display_model_hydration.py:523`

## `ChatRequest.clean_message` — method, line 20
- decorator: `field_validator('message')`
- decorator: `classmethod`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ChatRequest.validate_reasoning_effort` — method, line 25
- decorator: `field_validator('reasoning_effort')`
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
- `routes/codex_routes.py:406`
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

## `DirectoryRequest` — class, line 109
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ErrorResponse` — class, line 120
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `UploadResponse` — class, line 126
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SessionResponse` — class, line 136
- **called from:**
- `routes/session_routes.py:520`

## `MemoryResponse` — class, line 144
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
