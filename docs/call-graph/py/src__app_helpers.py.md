# `src/app_helpers.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `read_if_exists` — function, line 14
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `file_to_data_url` — function, line 22
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `abs_join` — function, line 28
- **called from:**
- `app.py:978`
- `app.py:986`
- `app.py:1027`
- `app.py:1033`

## `serve_html_with_nonce` — function, line 32
- **called from:**
- `app.py:980`
- `app.py:986`
- `app.py:1027`
- `app.py:1033`
- `tests/test_serve_html_with_nonce.py:29`
- `tests/test_serve_html_with_nonce.py:41`
- `tests/test_serve_html_with_nonce.py:48`

## `inside_base_dir` — function, line 54
- **called from:**
- `routes/chat_helpers.py:912`
- `src/document_processor.py:817`
- `tests/test_inside_base_dir_nonstring.py:11`
- `tests/test_inside_base_dir_nonstring.py:12`
- `tests/test_inside_base_dir_nonstring.py:13`
- `tests/test_inside_base_dir_nonstring.py:18`
- `tests/test_inside_base_dir_nonstring.py:19`
- `tests/test_upload_no_login.py:757`
- `tests/test_upload_no_login.py:831`
