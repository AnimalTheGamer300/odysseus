# `src/agent_tools/ocr_engine.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `query_requests_ocr` — function, line 12
- **called from:**
- `src/agent_tools/media_tools.py:916`

## `query_requests_numbers` — function, line 15
- **called from:**
- `src/agent_tools/media_tools.py:917`

## `_engine` — function, line 19
- decorator: `lru_cache(maxsize=1)`
- **called from:**
- `src/agent_tools/ocr_engine.py:28`

## `extract_image_text` — function, line 26
- **called from:**
- `src/agent_tools/media_tools.py:497`
- `tests/test_extract_text_tool.py:52`
