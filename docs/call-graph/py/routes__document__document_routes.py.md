# `routes/document/document_routes.py` — definitions & call sites

39 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_get_session_or_404` — function, line 25
- **called from:**
- `routes/document/document_routes.py:126`
- `routes/document/document_routes.py:257`
- `routes/document/document_routes.py:348`
- `routes/document/document_routes.py:647`
- `routes/document/document_routes.py:938`

## `_aggregate_language_facets` — function, line 34
- **called from:**
- `routes/document/document_routes.py:549`
- `tests/test_document_library_language_facet.py:15`
- `tests/test_document_library_language_facet.py:19`
- `tests/test_document_library_language_facet.py:24`
- `tests/test_document_library_language_facet.py:28`
- `tests/test_document_library_pdf_metadata.py:39`

## `_library_language_for_document` — function, line 49
- **called from:**
- `routes/document/document_routes.py:615`
- `tests/test_document_library_pdf_metadata.py:12`
- `tests/test_document_library_pdf_metadata.py:24`
- `tests/test_document_library_pdf_metadata.py:28`
- `tests/test_document_library_pdf_metadata.py:31`

## `_email_source_key` — function, line 63
- **called from:**
- `routes/document/document_routes.py:149`
- `routes/document/document_routes.py:161`

## `setup_document_routes` — function, line 84
- **called from:**
- `app.py:847`
- `tests/test_auth_disabled_document_access.py:58`
- `tests/test_document_close_clears_active_route.py:51`
- `tests/test_document_export_zip_filenames.py:29`
- `tests/test_document_export_zip_ids.py:27`
- `tests/test_document_library_literal_search.py:44`
- `tests/test_document_library_literal_search.py:68`
- `tests/test_document_render_pdf_iframe.py:148`
- `tests/test_document_session_owner_scope.py:40`
- `tests/test_review_document_conversion.py:27`
- `tests/test_review_document_conversion.py:106`
- `tests/test_upload_handler_cleanup.py:812`

## `_reserve_document_uploads` — function, line 87
- **called from:**
- `routes/document/document_routes.py:141`
- `routes/document/document_routes.py:873`

## `_locate_current_user_upload` — function, line 95
- **called from:**
- `routes/document/document_routes.py:274`
- `routes/document/document_routes.py:364`
- `routes/document/document_routes.py:416`
- `routes/document/document_routes.py:469`
- `routes/document/document_routes.py:741`
- `routes/document/document_routes.py:1309`
- `routes/document/document_routes.py:1371`
- `routes/document/document_routes.py:1438`
- `routes/document/document_routes.py:1493`
- `routes/document/document_routes.py:1641`
- `routes/document/document_routes.py:1741`
- `routes/document/document_routes.py:1881`

## `_load_pdf_viewer_fitz` — function, line 101
- **called from:**
- `routes/document/document_routes.py:1375`
- `routes/document/document_routes.py:1444`
- `routes/document/document_routes.py:1649`

## `create_document` — function (async), line 111
- **route:** `POST /api/document`
- decorator: `router.post("/api/document")`
- **called from:**
- `tests/test_upload_handler_cleanup.py:821`

## `import_pdf` — function (async), line 227
- **route:** `POST /api/documents/import-pdf`
- decorator: `router.post("/api/documents/import-pdf")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `import_docx` — function (async), line 329
- **route:** `POST /api/documents/import-docx`
- decorator: `router.post("/api/documents/import-docx")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `render_docx` — function (async), line 402
- **route:** `GET /api/document/{doc_id}/render-docx`
- decorator: `router.get("/api/document/{doc_id}/render-docx")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `convert_original_document` — function (async), line 432
- **route:** `GET /api/document/{doc_id}/convert-original/{target}`
- decorator: `router.get("/api/document/{doc_id}/convert-original/{target}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `convert` — function, line 483
- **called from:**
- `routes/gallery/gallery_routes.py:303`
- `routes/gallery/gallery_routes.py:359`
- `routes/gallery/gallery_routes.py:362`
- `routes/gallery/gallery_routes.py:391`
- `routes/gallery/gallery_routes.py:1855`
- `routes/gallery/gallery_routes.py:1856`
- `routes/gallery/gallery_routes.py:1980`
- `routes/gallery/gallery_routes.py:2861`
- `routes/gallery/gallery_routes.py:2894`
- `routes/gallery/gallery_routes.py:2909`
- `routes/upload_routes.py:523`
- `scripts/diffusion_server.py:789`
- `scripts/diffusion_server.py:985`
- `scripts/diffusion_server.py:986`
- `scripts/diffusion_server.py:1296`
- `scripts/diffusion_server.py:1329`
- `scripts/mlx_image_server.py:180`
- `scripts/mlx_image_server.py:199`
- `src/agent_tools/editor_tools.py:263`
- `src/agent_tools/editor_tools.py:281`
- `src/agent_tools/media_tools.py:381`
- `src/agent_tools/media_tools.py:493`
- `src/agent_tools/media_tools.py:849`
- `src/agent_tools/media_tools.py:1002`
- `src/agent_tools/media_tools.py:1504`
- `src/agent_tools/media_tools.py:1534`
- `src/agent_tools/media_tools.py:1715`
- `src/agent_tools/media_tools.py:1844`
- `src/clean_agent_preview.py:5439`
- `src/document_processor.py:151`
- `src/document_processor.py:491`
- `src/document_processor.py:565`
- `src/document_processor.py:658`
- `src/markitdown_runtime.py:99`
- `src/media_ingress.py:183`
- `src/tools/image.py:168`
- `tests/test_clean_v3_native_workspace.py:115`
- `tests/test_gallery_cloud_inpaint.py:271`
- `tests/test_inspect_media_tool.py:123`

## `documents_library` — function (async), line 513
- **route:** `GET /api/documents/library`
- decorator: `router.get("/api/documents/library")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_documents` — function (async), line 636
- **route:** `GET /api/documents/{session_id}`
- decorator: `router.get("/api/documents/{session_id}")`
- **called from:**
- `tests/test_document_session_owner_scope.py:132`

## `get_document` — function (async), line 660
- **route:** `GET /api/document/{doc_id}`
- decorator: `router.get("/api/document/{doc_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `document_visual_report` — function (async), line 674
- **route:** `GET /api/document/{doc_id}/visual-report`
- decorator: `router.get("/api/document/{doc_id}/visual-report", response_class=HTMLResponse)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `archive_document` — function (async), line 700
- **route:** `POST /api/document/{doc_id}/archive`
- decorator: `router.post("/api/document/{doc_id}/archive")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `extract_pdf_text` — function (async), line 716
- **route:** `POST /api/document/{doc_id}/extract-pdf-text`
- decorator: `router.post("/api/document/{doc_id}/extract-pdf-text")`
- **called from:**
- `routes/email/email_helpers.py:1642`
- `routes/personal_routes.py:346`
- `src/personal_docs.py:127`
- `src/rag_vector.py:522`

## `documents_export_zip` — function (async), line 776
- **route:** `POST /api/documents/export-zip`
- decorator: `router.post("/api/documents/export-zip")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_document` — function (async), line 848
- **route:** `PUT /api/document/{doc_id}`
- decorator: `router.put("/api/document/{doc_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `patch_document` — function (async), line 923
- **route:** `PATCH /api/document/{doc_id}`
- decorator: `router.patch("/api/document/{doc_id}")`
- **called from:**
- `tests/test_document_close_clears_active_route.py:79`
- `tests/test_document_close_clears_active_route.py:96`
- `tests/test_document_session_owner_scope.py:107`

## `delete_document` — function (async), line 962
- **route:** `DELETE /api/document/{doc_id}`
- decorator: `router.delete("/api/document/{doc_id}")`
- **called from:**
- `tests/test_document_close_clears_active_route.py:87`

## `list_versions` — function (async), line 990
- **route:** `GET /api/document/{doc_id}/versions`
- decorator: `router.get("/api/document/{doc_id}/versions")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_version` — function (async), line 1015
- **route:** `GET /api/document/{doc_id}/version/{num}`
- decorator: `router.get("/api/document/{doc_id}/version/{num}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `restore_version` — function (async), line 1036
- **route:** `POST /api/document/{doc_id}/restore/{num}`
- decorator: `router.post("/api/document/{doc_id}/restore/{num}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `tidy_documents` — function (async), line 1077
- **route:** `POST /api/documents/tidy`
- decorator: `router.post("/api/documents/tidy")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_is_filler` — function, line 1136
- **called from:**
- `routes/document/document_routes.py:1142`

## `ai_tidy_documents` — function (async), line 1192
- **route:** `POST /api/documents/ai-tidy`
- decorator: `router.post("/api/documents/ai-tidy")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `export_pdf_preview` — function (async), line 1289
- **route:** `POST /api/document/{doc_id}/export-pdf/preview`
- decorator: `router.post("/api/document/{doc_id}/export-pdf/preview")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `render_pages` — function (async), line 1351
- **route:** `GET /api/document/{doc_id}/render-pages`
- decorator: `router.get("/api/document/{doc_id}/render-pages")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `render_page_png` — function (async), line 1422
- **route:** `GET /api/document/{doc_id}/page/{page_no}.png`
- decorator: `router.get("/api/document/{doc_id}/page/{page_no}.png")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ai_fill_annotations` — function (async), line 1463
- **route:** `POST /api/document/{doc_id}/ai-fill-annotations`
- decorator: `router.post("/api/document/{doc_id}/ai-fill-annotations")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `render_pdf` — function (async), line 1603
- **route:** `GET /api/document/{doc_id}/render-pdf`
- decorator: `router.get("/api/document/{doc_id}/render-pdf")`
- **called from:**
- `tests/test_document_render_pdf_iframe.py:203`
- `tests/test_document_render_pdf_iframe.py:236`

## `_cleanup_temps` — function, line 1622
- **called from:**
- `routes/document/document_routes.py:1658`
- `routes/document/document_routes.py:1781`

## `export_pdf` — function (async), line 1703
- **route:** `GET /api/document/{doc_id}/export-pdf`
- decorator: `router.get("/api/document/{doc_id}/export-pdf")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_cleanup_temps` — function, line 1720
- **called from:**
- `routes/document/document_routes.py:1658`
- `routes/document/document_routes.py:1781`

## `prepare_signed_reply` — function (async), line 1839
- **route:** `POST /api/document/{doc_id}/prepare-signed-reply`
- decorator: `router.post("/api/document/{doc_id}/prepare-signed-reply")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
