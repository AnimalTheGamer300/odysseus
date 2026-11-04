# `src/markitdown_runtime.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `is_markitdown_format` — function, line 27
- **called from:**
- `src/document_processor.py:229`
- `tests/test_markitdown_format_nonstring.py:9`
- `tests/test_markitdown_format_nonstring.py:10`
- `tests/test_markitdown_format_nonstring.py:11`
- `tests/test_markitdown_format_nonstring.py:15`
- `tests/test_markitdown_format_nonstring.py:16`
- `tests/test_markitdown_runtime.py:51`
- `tests/test_markitdown_runtime.py:52`
- `tests/test_markitdown_runtime.py:53`
- `tests/test_markitdown_runtime.py:54`

## `load_markitdown` — function, line 34
- **called from:**
- `src/document_processor.py:281`
- `src/markitdown_runtime.py:86`
- `tests/test_markitdown_runtime.py:29`

## `_extract_docx_native` — function, line 43
- **called from:**
- `src/markitdown_runtime.py:89`

## `convert_to_markdown` — function, line 75
- **called from:**
- `src/document_processor.py:232`
- `src/personal_docs.py:38`
- `tests/test_markitdown_runtime.py:38`
- `tests/test_markitdown_runtime.py:47`
- `tests/test_markitdown_runtime.py:73`
