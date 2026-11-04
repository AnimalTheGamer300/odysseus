# `src/attachment_refs.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `strip_inline_data_urls` — function, line 30
- **called from:**
- `src/attachment_refs.py:99`
- `src/attachment_refs.py:107`
- `src/attachment_refs.py:117`
- `src/attachment_refs.py:143`
- `src/attachment_refs.py:145`
- `src/attachment_refs.py:147`
- `src/attachment_refs.py:161`

## `attachment_ref` — function, line 37
- **called from:**
- `routes/chat_helpers.py:450`
- `src/attachment_refs.py:72`
- `tests/test_attachment_refs.py:58`

## `attachment_refs_from_metadata` — function, line 64
- **called from:**
- `routes/upload_routes.py:73`
- `src/attachment_refs.py:137`
- `src/upload_handler.py:181`

## `_ref_line` — function, line 78
- **called from:**
- `src/attachment_refs.py:109`
- `src/attachment_refs.py:138`

## `_text_from_blocks` — function, line 94
- **called from:**
- `src/attachment_refs.py:136`
- `src/attachment_refs.py:160`
- `src/attachment_refs.py:163`

## `persistable_message_content` — function, line 124
- **called from:**
- `core/session_manager.py:407`
- `core/session_manager.py:474`
- `core/session_manager.py:502`
- `core/session_manager.py:557`
- `core/session_manager.py:645`
- `core/session_manager.py:852`
- `src/attachment_refs.py:164`
- `tests/test_attachment_refs.py:32`

## `search_index_text` — function, line 150
- **called from:**
- `core/database.py:2370`
- `tests/test_attachment_refs.py:52`
