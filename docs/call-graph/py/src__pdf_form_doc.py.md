# `src/pdf_form_doc.py` — definitions & call sites

16 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_unescape_annotation_value` — function, line 37
- **called from:**
- `src/pdf_form_doc.py:73`

## `parse_markdown_annotations` — function, line 59
- **called from:**
- `routes/document/document_routes.py:1661`
- `routes/document/document_routes.py:1795`
- `routes/document/document_routes.py:1928`
- `tests/test_pdf_annotation_text_controls.py:10`
- `tests/test_pdf_annotation_text_controls.py:23`

## `_encode_name` — function, line 112
- **called from:**
- `src/pdf_form_doc.py:329`

## `_decode_name` — function, line 128
- **called from:**
- `src/pdf_form_doc.py:280`

## `sidecar_path` — function, line 144
- **called from:**
- `src/pdf_form_doc.py:151`
- `src/pdf_form_doc.py:162`

## `save_field_sidecar` — function, line 149
- **called from:**
- `routes/document/document_routes.py:292`
- `routes/email/email_routes.py:5031`
- `src/document_processor.py:939`

## `load_field_sidecar` — function, line 160
- **called from:**
- `routes/document/document_routes.py:1313`
- `routes/document/document_routes.py:1376`
- `routes/document/document_routes.py:1745`
- `routes/document/document_routes.py:1885`

## `find_source_upload_id` — function, line 173
- **called from:**
- `routes/document/document_helpers.py:194`
- `routes/document/document_routes.py:58`
- `routes/document/document_routes.py:463`
- `routes/document/document_routes.py:737`
- `routes/document/document_routes.py:1305`
- `routes/document/document_routes.py:1368`
- `routes/document/document_routes.py:1435`
- `routes/document/document_routes.py:1490`
- `routes/document/document_routes.py:1638`
- `routes/document/document_routes.py:1737`
- `routes/document/document_routes.py:1878`
- `src/agent_loop.py:14953`
- `src/agent_tools/document_tools.py:445`
- `tests/test_security_regressions.py:450`

## `render_plain_pdf_markdown` — function, line 192
- **called from:**
- `src/pdf_form_doc.py:227`

## `create_plain_pdf_document` — function, line 212
- **called from:**
- `routes/document/document_routes.py:301`
- `routes/email/email_routes.py:5040`
- `src/document_processor.py:958`

## `parse_markdown_to_values` — function, line 264
- **called from:**
- `routes/document/document_routes.py:1317`
- `routes/document/document_routes.py:1377`
- `routes/document/document_routes.py:1651`
- `routes/document/document_routes.py:1748`
- `routes/document/document_routes.py:1887`
- `tests/test_form_markdown_roundtrip.py:26`
- `tests/test_form_markdown_roundtrip.py:40`
- `tests/test_form_markdown_roundtrip.py:55`
- `tests/test_form_markdown_roundtrip.py:66`
- `tests/test_form_markdown_roundtrip.py:77`

## `_checkbox_marker` — function, line 305
- **called from:**
- `src/pdf_form_doc.py:334`

## `_flatten` — function, line 309
- **called from:**
- `src/pdf_form_doc.py:328`
- `src/pdf_form_doc.py:331`
- `static/js/slashAutocomplete.js:26`
- `static/js/slashAutocomplete.js:195`

## `_format_field_bullet` — function, line 316
- **called from:**
- `src/pdf_form_doc.py:381`

## `render_form_as_markdown` — function, line 350
- **called from:**
- `src/pdf_form_doc.py:410`
- `tests/test_form_markdown_roundtrip.py:25`
- `tests/test_form_markdown_roundtrip.py:39`
- `tests/test_form_markdown_roundtrip.py:52`
- `tests/test_form_markdown_roundtrip.py:75`

## `create_form_markdown_document` — function, line 394
- **called from:**
- `routes/document/document_routes.py:293`
- `routes/email/email_routes.py:5032`
- `src/document_processor.py:940`
