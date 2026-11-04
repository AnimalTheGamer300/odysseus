# `routes/document/document_helpers.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `DocumentCreate` — class, line 23
- **called from:**
- `routes/codex_routes.py:350`
- `routes/codex_routes.py:510`
- `tests/test_upload_handler_cleanup.py:823`

## `DocumentUpdate` — class, line 29
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DocumentPatch` — class, line 34
- **called from:**
- `tests/test_document_close_clears_active_route.py:79`
- `tests/test_document_close_clears_active_route.py:96`
- `tests/test_document_session_owner_scope.py:112`

## `_doc_to_dict` — function, line 42
- **called from:**
- `routes/document/document_routes.py:175`
- `routes/document/document_routes.py:210`
- `routes/document/document_routes.py:318`
- `routes/document/document_routes.py:464`
- `routes/document/document_routes.py:478`
- `routes/document/document_routes.py:647`
- `routes/document/document_routes.py:688`
- `routes/document/document_routes.py:727`
- `routes/document/document_routes.py:842`

## `_version_to_dict` — function, line 62
- **called from:**
- `routes/document/document_routes.py:806`

## `_verify_doc_owner` — function, line 74
- **called from:**
- `routes/document/document_routes.py:477`
- `routes/document/document_routes.py:491`
- `routes/document/document_routes.py:518`
- `routes/document/document_routes.py:593`
- `routes/document/document_routes.py:631`
- `routes/document/document_routes.py:706`
- `routes/document/document_routes.py:745`
- `routes/document/document_routes.py:774`
- `routes/document/document_routes.py:799`
- `routes/document/document_routes.py:819`
- `routes/document/document_routes.py:1079`
- `routes/document/document_routes.py:1143`
- `routes/document/document_routes.py:1210`
- `routes/document/document_routes.py:1265`
- `routes/document/document_routes.py:1413`
- `routes/document/document_routes.py:1511`
- `routes/document/document_routes.py:1648`
- `tests/test_auth_disabled_document_access.py:142`
- `tests/test_auth_disabled_document_access.py:207`
- `tests/test_auth_disabled_document_access.py:227`

## `_owner_session_filter` — function, line 98
- **called from:**
- `routes/chat_routes.py:1596`
- `routes/chat_routes.py:1636`
- `routes/chat_routes.py:1644`
- `routes/chat_routes.py:1659`
- `routes/document/document_routes.py:358`
- `routes/document/document_routes.py:368`
- `routes/document/document_routes.py:377`
- `routes/document/document_routes.py:864`
- `routes/document/document_routes.py:947`
- `routes/document/document_routes.py:991`
- `tests/test_auth_disabled_document_access.py:154`
- `tests/test_document_session_owner_scope.py:155`
- `tests/test_null_owner_gates.py:127`
- `tests/test_null_owner_gates.py:137`

## `_slug` — function, line 118
- **called from:**
- `routes/document/document_routes.py:1603`
- `routes/document/document_routes.py:1737`
- `static/js/document.js:633`
- `static/js/document.js:917`

## `_upload_path_inside` — function, line 138
- **called from:**
- `routes/document/document_helpers.py:165`

## `_resolve_user_upload_path` — function, line 147
- **called from:**
- `routes/document/document_helpers.py:184`
- `routes/document/document_helpers.py:202`
- `routes/document/document_routes.py:94`
- `tests/test_resolve_upload_path_nondict.py:17`
- `tests/test_resolve_upload_path_nondict.py:18`
- `tests/test_resolve_upload_path_nondict.py:23`

## `_locate_upload` — function, line 171
- **called from:**
- `tests/test_security_regressions.py:440`
- `tests/test_security_regressions.py:441`

## `_assert_pdf_marker_upload_owned` — function, line 187
- **called from:**
- `routes/document/document_routes.py:137`
- `routes/document/document_routes.py:650`
- `tests/test_security_regressions.py:482`
- `tests/test_security_regressions.py:487`

## `_derive_title` — function, line 209
- **called from:**
- `routes/document/document_routes.py:932`
- `tests/test_derive_title_nonstring.py:8`
- `tests/test_derive_title_nonstring.py:9`
- `tests/test_derive_title_nonstring.py:13`
