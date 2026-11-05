# `routes/document/document_helpers.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `DocumentCreate` — class, line 24
- **called from:**
- `routes/codex_routes.py:396`
- `routes/codex_routes.py:556`
- `tests/test_upload_handler_cleanup.py:823`

## `DocumentUpdate` — class, line 30
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DocumentPatch` — class, line 35
- **called from:**
- `tests/test_document_close_clears_active_route.py:79`
- `tests/test_document_close_clears_active_route.py:96`
- `tests/test_document_session_owner_scope.py:107`

## `_doc_to_dict` — function, line 43
- **called from:**
- `routes/document/document_routes.py:180`
- `routes/document/document_routes.py:215`
- `routes/document/document_routes.py:323`
- `routes/document/document_routes.py:397`
- `routes/document/document_routes.py:654`
- `routes/document/document_routes.py:668`
- `routes/document/document_routes.py:871`
- `routes/document/document_routes.py:912`
- `routes/document/document_routes.py:951`
- `routes/document/document_routes.py:1066`

## `_version_to_dict` — function, line 63
- **called from:**
- `routes/document/document_routes.py:1030`

## `_verify_doc_owner` — function, line 75
- **called from:**
- `routes/document/document_routes.py:412`
- `routes/document/document_routes.py:456`
- `routes/document/document_routes.py:667`
- `routes/document/document_routes.py:682`
- `routes/document/document_routes.py:707`
- `routes/document/document_routes.py:734`
- `routes/document/document_routes.py:811`
- `routes/document/document_routes.py:855`
- `routes/document/document_routes.py:930`
- `routes/document/document_routes.py:969`
- `routes/document/document_routes.py:998`
- `routes/document/document_routes.py:1023`
- `routes/document/document_routes.py:1043`
- `routes/document/document_routes.py:1303`
- `routes/document/document_routes.py:1367`
- `routes/document/document_routes.py:1434`
- `routes/document/document_routes.py:1489`
- `routes/document/document_routes.py:1637`
- `routes/document/document_routes.py:1735`
- `routes/document/document_routes.py:1872`
- `tests/test_auth_disabled_document_access.py:142`
- `tests/test_auth_disabled_document_access.py:207`
- `tests/test_auth_disabled_document_access.py:227`

## `_owner_session_filter` — function, line 99
- **called from:**
- `routes/chat_routes.py:3355`
- `routes/chat_routes.py:3396`
- `routes/chat_routes.py:3404`
- `routes/chat_routes.py:3419`
- `routes/document/document_routes.py:547`
- `routes/document/document_routes.py:557`
- `routes/document/document_routes.py:566`
- `routes/document/document_routes.py:1088`
- `routes/document/document_routes.py:1171`
- `routes/document/document_routes.py:1215`
- `tests/test_auth_disabled_document_access.py:154`
- `tests/test_document_session_owner_scope.py:150`
- `tests/test_null_owner_gates.py:127`
- `tests/test_null_owner_gates.py:137`

## `_slug` — function, line 119
- **called from:**
- `routes/document/document_routes.py:1827`
- `routes/document/document_routes.py:1961`
- `static/js/document.js:1546`
- `static/js/document.js:1830`

## `_upload_path_inside` — function, line 139
- **called from:**
- `routes/document/document_helpers.py:161`

## `_resolve_user_upload_path` — function, line 143
- **called from:**
- `routes/document/document_helpers.py:180`
- `routes/document/document_helpers.py:198`
- `routes/document/document_routes.py:99`
- `tests/test_resolve_upload_path_nondict.py:17`
- `tests/test_resolve_upload_path_nondict.py:18`
- `tests/test_resolve_upload_path_nondict.py:23`

## `_locate_upload` — function, line 167
- **called from:**
- `tests/test_security_regressions.py:441`
- `tests/test_security_regressions.py:442`

## `_assert_pdf_marker_upload_owned` — function, line 183
- **called from:**
- `routes/document/document_routes.py:142`
- `routes/document/document_routes.py:874`
- `tests/test_security_regressions.py:483`
- `tests/test_security_regressions.py:488`

## `_derive_title` — function, line 205
- **called from:**
- `routes/document/document_routes.py:1156`
- `tests/test_derive_title_nonstring.py:8`
- `tests/test_derive_title_nonstring.py:9`
- `tests/test_derive_title_nonstring.py:13`
