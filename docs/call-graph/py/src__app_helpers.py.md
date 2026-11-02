# `src/app_helpers.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `read_if_exists` — function, line 12
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `file_to_data_url` — function, line 20
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `abs_join` — function, line 26
- **called from:**
- `app.py:893`
- `app.py:901`
- `app.py:942`
- `app.py:948`

## `serve_html_with_nonce` — function, line 30
- **called from:**
- `app.py:895`
- `app.py:901`
- `app.py:942`
- `app.py:948`
- `tests/test_serve_html_with_nonce.py:29`
- `tests/test_serve_html_with_nonce.py:41`
- `tests/test_serve_html_with_nonce.py:48`

## `inside_base_dir` — function, line 52
- **called from:**
- `routes/chat_helpers.py:444`
- `src/document_processor.py:667`
- `tests/test_inside_base_dir_nonstring.py:11`
- `tests/test_inside_base_dir_nonstring.py:12`
- `tests/test_inside_base_dir_nonstring.py:13`
- `tests/test_inside_base_dir_nonstring.py:18`
- `tests/test_inside_base_dir_nonstring.py:19`
