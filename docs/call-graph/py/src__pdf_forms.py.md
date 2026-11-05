# `src/pdf_forms.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_require_fitz` — function, line 29
- **called from:**
- `src/pdf_forms.py:72`
- `src/pdf_forms.py:148`
- `src/pdf_forms.py:236`
- `src/pdf_forms.py:273`
- `src/pdf_forms.py:374`

## `_widget_type_names` — function, line 36
- **called from:**
- `src/pdf_forms.py:149`

## `has_form_fields` — function, line 55
- **called from:**
- `routes/document/document_routes.py:286`
- `routes/email/email_routes.py:5025`
- `src/document_processor.py:916`

## `_infer_label` — function, line 91
- **called from:**
- `src/pdf_forms.py:171`

## `_join_nearest` — function, line 114
- **called from:**
- `src/pdf_forms.py:125`
- `src/pdf_forms.py:128`

## `_widget_on_state` — function, line 131
- **called from:**
- `src/pdf_forms.py:173`
- `src/pdf_forms.py:385`

## `extract_fields` — function, line 138
- **called from:**
- `routes/document/document_routes.py:291`
- `routes/email/email_routes.py:5030`
- `src/document_processor.py:938`

## `stamp_signatures` — function, line 219
- **called from:**
- `routes/document/document_routes.py:1789`
- `routes/document/document_routes.py:1923`

## `stamp_annotations` — function, line 259
- **called from:**
- `routes/document/document_routes.py:1687`
- `routes/document/document_routes.py:1822`
- `routes/document/document_routes.py:1954`

## `fill_fields` — function, line 368
- **called from:**
- `routes/document/document_routes.py:1655`
- `routes/document/document_routes.py:1778`
- `routes/document/document_routes.py:1917`
