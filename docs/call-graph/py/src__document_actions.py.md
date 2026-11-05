# `src/document_actions.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_norm_title` — function, line 23
- **called from:**
- `src/document_actions.py:152`
- `tests/test_document_actions_nonstring.py:11`
- `tests/test_document_actions_nonstring.py:17`

## `_content_fingerprint` — function, line 29
- **called from:**
- `src/document_actions.py:152`
- `tests/test_document_actions_nonstring.py:12`

## `_real_len` — function, line 44
- **called from:**
- `src/document_actions.py:170`
- `tests/test_document_actions_nonstring.py:13`
- `tests/test_document_actions_nonstring.py:18`

## `run_document_tidy` — function (async), line 53
- **called from:**
- `src/agent_tools/document_tools.py:1237`
- `src/builtin_actions.py:581`
- `tests/test_document_tidy_null_timestamp.py:60`

## `_updated` — function, line 160
- **called from:**
- `src/document_actions.py:171`
- `src/document_actions.py:172`
