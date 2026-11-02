# `routes/document/document_routes.py` — definitions & call sites

34 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_get_session_or_404` — function, line 20
- **called from:**
- `routes/document/document_routes.py:121`
- `routes/document/document_routes.py:252`
- `routes/document/document_routes.py:457`
- `routes/document/document_routes.py:714`

## `_aggregate_language_facets` — function, line 29
- **called from:**
- `routes/document/document_routes.py:360`
- `tests/test_document_library_language_facet.py:15`
- `tests/test_document_library_language_facet.py:19`
- `tests/test_document_library_language_facet.py:24`
- `tests/test_document_library_language_facet.py:28`
- `tests/test_document_library_pdf_metadata.py:39`

## `_library_language_for_document` — function, line 44
- **called from:**
- `routes/document/document_routes.py:425`
- `tests/test_document_library_pdf_metadata.py:12`
- `tests/test_document_library_pdf_metadata.py:24`
- `tests/test_document_library_pdf_metadata.py:28`
- `tests/test_document_library_pdf_metadata.py:31`

## `_email_source_key` — function, line 58
- **called from:**
- `routes/document/document_routes.py:144`
- `routes/document/document_routes.py:156`

## `setup_document_routes` — function, line 79
- **called from:**
- `app.py:767`
- `tests/test_auth_disabled_document_access.py:58`
- `tests/test_document_close_clears_active_route.py:51`
- `tests/test_document_render_pdf_iframe.py:148`
- `tests/test_document_session_owner_scope.py:45`
- `tests/test_upload_handler_cleanup.py:812`

## `_reserve_document_uploads` — function, line 82
- **called from:**
- `routes/document/document_routes.py:136`
- `routes/document/document_routes.py:649`

## `_locate_current_user_upload` — function, line 90
- **called from:**
- `routes/document/document_routes.py:269`
- `routes/document/document_routes.py:525`
- `routes/document/document_routes.py:1085`
- `routes/document/document_routes.py:1147`
- `routes/document/document_routes.py:1214`
- `routes/document/document_routes.py:1269`
- `routes/document/document_routes.py:1417`
- `routes/document/document_routes.py:1517`
- `routes/document/document_routes.py:1657`

## `_load_pdf_viewer_fitz` — function, line 96
- **called from:**
- `routes/document/document_routes.py:1151`
- `routes/document/document_routes.py:1220`
- `routes/document/document_routes.py:1425`

## `create_document` — function (async), line 106
- **route:** `POST /api/document`
- decorator: `router.post("/api/document")`
- **called from:**
- `tests/test_upload_handler_cleanup.py:821`

## `import_pdf` — function (async), line 222
- **route:** `POST /api/documents/import-pdf`
- decorator: `router.post("/api/documents/import-pdf")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `documents_library` — function (async), line 324
- **route:** `GET /api/documents/library`
- decorator: `router.get("/api/documents/library")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_documents` — function (async), line 446
- **route:** `GET /api/documents/{session_id}`
- decorator: `router.get("/api/documents/{session_id}")`
- **called from:**
- `tests/test_document_session_owner_scope.py:137`

## `get_document` — function (async), line 470
- **route:** `GET /api/document/{doc_id}`
- decorator: `router.get("/api/document/{doc_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `archive_document` — function (async), line 484
- **route:** `POST /api/document/{doc_id}/archive`
- decorator: `router.post("/api/document/{doc_id}/archive")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `extract_pdf_text` — function (async), line 500
- **route:** `POST /api/document/{doc_id}/extract-pdf-text`
- decorator: `router.post("/api/document/{doc_id}/extract-pdf-text")`
- **called from:**
- `routes/email_helpers.py:1495`
- `routes/personal_routes.py:360`
- `src/personal_docs.py:123`
- `src/rag_vector.py:522`

## `documents_export_zip` — function (async), line 560
- **route:** `POST /api/documents/export-zip`
- decorator: `router.post("/api/documents/export-zip")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_document` — function (async), line 624
- **route:** `PUT /api/document/{doc_id}`
- decorator: `router.put("/api/document/{doc_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `patch_document` — function (async), line 699
- **route:** `PATCH /api/document/{doc_id}`
- decorator: `router.patch("/api/document/{doc_id}")`
- **called from:**
- `tests/test_document_close_clears_active_route.py:79`
- `tests/test_document_close_clears_active_route.py:96`
- `tests/test_document_session_owner_scope.py:112`

## `delete_document` — function (async), line 738
- **route:** `DELETE /api/document/{doc_id}`
- decorator: `router.delete("/api/document/{doc_id}")`
- **called from:**
- `tests/test_document_close_clears_active_route.py:87`

## `list_versions` — function (async), line 766
- **route:** `GET /api/document/{doc_id}/versions`
- decorator: `router.get("/api/document/{doc_id}/versions")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_version` — function (async), line 791
- **route:** `GET /api/document/{doc_id}/version/{num}`
- decorator: `router.get("/api/document/{doc_id}/version/{num}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `restore_version` — function (async), line 812
- **route:** `POST /api/document/{doc_id}/restore/{num}`
- decorator: `router.post("/api/document/{doc_id}/restore/{num}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `tidy_documents` — function (async), line 853
- **route:** `POST /api/documents/tidy`
- decorator: `router.post("/api/documents/tidy")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_is_filler` — function, line 912
- **called from:**
- `routes/document/document_routes.py:918`

## `ai_tidy_documents` — function (async), line 968
- **route:** `POST /api/documents/ai-tidy`
- decorator: `router.post("/api/documents/ai-tidy")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `export_pdf_preview` — function (async), line 1065
- **route:** `POST /api/document/{doc_id}/export-pdf/preview`
- decorator: `router.post("/api/document/{doc_id}/export-pdf/preview")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `render_pages` — function (async), line 1127
- **route:** `GET /api/document/{doc_id}/render-pages`
- decorator: `router.get("/api/document/{doc_id}/render-pages")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `render_page_png` — function (async), line 1198
- **route:** `GET /api/document/{doc_id}/page/{page_no}.png`
- decorator: `router.get("/api/document/{doc_id}/page/{page_no}.png")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ai_fill_annotations` — function (async), line 1239
- **route:** `POST /api/document/{doc_id}/ai-fill-annotations`
- decorator: `router.post("/api/document/{doc_id}/ai-fill-annotations")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `render_pdf` — function (async), line 1379
- **route:** `GET /api/document/{doc_id}/render-pdf`
- decorator: `router.get("/api/document/{doc_id}/render-pdf")`
- **called from:**
- `tests/test_document_render_pdf_iframe.py:203`
- `tests/test_document_render_pdf_iframe.py:236`

## `_cleanup_temps` — function, line 1398
- **called from:**
- `routes/document/document_routes.py:1434`
- `routes/document/document_routes.py:1557`

## `export_pdf` — function (async), line 1479
- **route:** `GET /api/document/{doc_id}/export-pdf`
- decorator: `router.get("/api/document/{doc_id}/export-pdf")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_cleanup_temps` — function, line 1496
- **called from:**
- `routes/document/document_routes.py:1434`
- `routes/document/document_routes.py:1557`

## `prepare_signed_reply` — function (async), line 1615
- **route:** `POST /api/document/{doc_id}/prepare-signed-reply`
- decorator: `router.post("/api/document/{doc_id}/prepare-signed-reply")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
