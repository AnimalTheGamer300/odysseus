# `src/pdf_form_doc.py` — definitions & call sites

16 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_unescape_annotation_value` — function, line 37
- **called from:**
- `src/pdf_form_doc.py:73`

## `parse_markdown_annotations` — function, line 59
- **called from:**
- `routes/document/document_routes.py:1437`
- `routes/document/document_routes.py:1571`
- `routes/document/document_routes.py:1704`

## `_encode_name` — function, line 109
- **called from:**
- `src/pdf_form_doc.py:326`

## `_decode_name` — function, line 125
- **called from:**
- `src/pdf_form_doc.py:277`

## `sidecar_path` — function, line 141
- **called from:**
- `src/pdf_form_doc.py:148`
- `src/pdf_form_doc.py:159`

## `save_field_sidecar` — function, line 146
- **called from:**
- `routes/document/document_routes.py:287`
- `routes/email_routes.py:3603`
- `src/document_processor.py:790`

## `load_field_sidecar` — function, line 157
- **called from:**
- `routes/document/document_routes.py:1089`
- `routes/document/document_routes.py:1152`
- `routes/document/document_routes.py:1521`
- `routes/document/document_routes.py:1661`

## `find_source_upload_id` — function, line 170
- **called from:**
- `routes/document/document_helpers.py:198`
- `routes/document/document_routes.py:53`
- `routes/document/document_routes.py:521`
- `routes/document/document_routes.py:1081`
- `routes/document/document_routes.py:1144`
- `routes/document/document_routes.py:1211`
- `routes/document/document_routes.py:1266`
- `routes/document/document_routes.py:1414`
- `routes/document/document_routes.py:1513`
- `routes/document/document_routes.py:1654`
- `src/agent_loop.py:2794`
- `src/agent_tools/document_tools.py:295`
- `tests/test_security_regressions.py:449`

## `render_plain_pdf_markdown` — function, line 189
- **called from:**
- `src/pdf_form_doc.py:224`

## `create_plain_pdf_document` — function, line 209
- **called from:**
- `routes/document/document_routes.py:296`
- `routes/email_routes.py:3612`
- `src/document_processor.py:809`

## `parse_markdown_to_values` — function, line 261
- **called from:**
- `routes/document/document_routes.py:1093`
- `routes/document/document_routes.py:1153`
- `routes/document/document_routes.py:1427`
- `routes/document/document_routes.py:1524`
- `routes/document/document_routes.py:1663`
- `tests/test_form_markdown_roundtrip.py:24`
- `tests/test_form_markdown_roundtrip.py:38`

## `_checkbox_marker` — function, line 302
- **called from:**
- `src/pdf_form_doc.py:331`

## `_flatten` — function, line 306
- **called from:**
- `src/pdf_form_doc.py:325`
- `src/pdf_form_doc.py:328`
- `static/js/slashAutocomplete.js:26`
- `static/js/slashAutocomplete.js:195`

## `_format_field_bullet` — function, line 313
- **called from:**
- `src/pdf_form_doc.py:378`

## `render_form_as_markdown` — function, line 347
- **called from:**
- `src/pdf_form_doc.py:407`
- `tests/test_form_markdown_roundtrip.py:23`
- `tests/test_form_markdown_roundtrip.py:37`

## `create_form_markdown_document` — function, line 391
- **called from:**
- `routes/document/document_routes.py:288`
- `routes/email_routes.py:3604`
- `src/document_processor.py:791`
