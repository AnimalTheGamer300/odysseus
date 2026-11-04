# `src/url_safety.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_default_resolver` — function, line 37
- **called from:**
- `services/memory/skill_importer.py:101`
- `src/integrations.py:574`

## `_classify` — function, line 42
- **called from:**
- `services/search/content.py:744`
- `src/url_safety.py:103`
- `tests/test_tool_rag_contacts_domain.py:40`
- `tests/test_tool_rag_contacts_domain.py:49`
- `tests/test_tool_rag_contacts_domain.py:69`
- `tests/test_tool_rag_contacts_domain.py:70`
- `tests/test_tool_rag_contacts_domain.py:71`
- `tests/test_tool_rag_contacts_domain.py:72`

## `check_outbound_url` — function, line 60
- **called from:**
- `routes/contacts/contacts_routes.py:68`
- `routes/embedding_routes.py:267`
- `routes/gallery/gallery_routes.py:335`
- `routes/gallery/gallery_routes.py:1272`
- `routes/gallery/gallery_routes.py:1536`
- `services/memory/skill_importer.py:105`
- `src/ai_interaction.py:1145`
- `src/ai_interaction.py:1427`
- `src/ai_interaction.py:1691`
- `src/integrations.py:578`
- `tests/test_check_outbound_url_nonstring.py:11`
- `tests/test_check_outbound_url_nonstring.py:13`
- `tests/test_gallery_endpoint_ssrf.py:43`
- `tests/test_skill_importer_security.py:126`
- `tests/test_skill_importer_security.py:135`
- `tests/test_skill_importer_security.py:144`
- `tests/test_skill_importer_security.py:153`
- `tests/test_url_safety.py:26`
- `tests/test_url_safety.py:32`
- `tests/test_url_safety.py:33`
- `tests/test_url_safety.py:37`
- `tests/test_url_safety.py:43`
- `tests/test_url_safety.py:49`
- `tests/test_url_safety.py:56`
- `tests/test_url_safety.py:57`
- `tests/test_url_safety.py:61`
- `tests/test_url_safety.py:63`
- `tests/test_url_safety.py:72`
- `tests/test_url_safety.py:83`
- `tests/test_url_safety.py:90`
- `tests/test_url_safety.py:95`
- `tests/test_url_safety.py:101`
- `tests/test_url_safety.py:111`
