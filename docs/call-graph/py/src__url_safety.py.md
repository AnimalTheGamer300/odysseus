# `src/url_safety.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_nat64_well_known_embedded_ipv4` — function, line 65
- **called from:**
- `src/url_safety.py:93`

## `_default_resolver` — function, line 80
- **called from:**
- `services/memory/skill_importer.py:101`
- `src/integrations.py:580`

## `_classify` — function, line 85
- **called from:**
- `src/url_safety.py:95`
- `src/url_safety.py:161`
- `src/url_safety.py:196`
- `src/url_safety.py:212`
- `src/url_safety.py:257`
- `tests/test_editor_planner_routing.py:102`
- `tests/test_editor_planner_routing.py:117`
- `tests/test_editor_planner_routing.py:127`
- `tests/test_editor_planner_routing.py:134`
- `tests/test_tool_rag_contacts_domain.py:40`
- `tests/test_tool_rag_contacts_domain.py:49`
- `tests/test_tool_rag_contacts_domain.py:69`
- `tests/test_tool_rag_contacts_domain.py:70`
- `tests/test_tool_rag_contacts_domain.py:71`
- `tests/test_tool_rag_contacts_domain.py:72`

## `check_outbound_url` — function, line 118
- **called from:**
- `routes/contacts/contacts_routes.py:71`
- `routes/embedding_routes.py:267`
- `routes/gallery/gallery_routes.py:752`
- `routes/gallery/gallery_routes.py:1782`
- `routes/gallery/gallery_routes.py:2157`
- `routes/gallery/gallery_routes.py:2265`
- `routes/gallery/gallery_routes.py:2319`
- `routes/model_routes.py:2183`
- `routes/model_routes.py:2430`
- `routes/model_routes.py:2933`
- `services/memory/skill_importer.py:105`
- `services/search/core.py:542`
- `src/agent_tools/admin_tools.py:54`
- `src/ai_interaction.py:1514`
- `src/ai_interaction.py:1875`
- `src/ai_interaction.py:2139`
- `src/integrations.py:584`
- `tests/test_check_outbound_url_nonstring.py:11`
- `tests/test_check_outbound_url_nonstring.py:13`
- `tests/test_gallery_endpoint_ssrf.py:43`
- `tests/test_skill_importer_security.py:126`
- `tests/test_skill_importer_security.py:135`
- `tests/test_skill_importer_security.py:144`
- `tests/test_skill_importer_security.py:153`
- `tests/test_url_safety.py:28`
- `tests/test_url_safety.py:34`
- `tests/test_url_safety.py:35`
- `tests/test_url_safety.py:39`
- `tests/test_url_safety.py:45`
- `tests/test_url_safety.py:51`
- `tests/test_url_safety.py:58`
- `tests/test_url_safety.py:59`
- `tests/test_url_safety.py:63`
- `tests/test_url_safety.py:65`
- `tests/test_url_safety.py:78`
- `tests/test_url_safety.py:94`
- `tests/test_url_safety.py:107`
- `tests/test_url_safety.py:118`
- `tests/test_url_safety.py:125`
- `tests/test_url_safety.py:130`
- `tests/test_url_safety.py:136`
- `tests/test_url_safety.py:146`
- `tests/test_url_safety.py:176`
- `tests/test_url_safety.py:179`
- `tests/test_url_safety.py:188`
- `tests/test_url_safety.py:199`
- `tests/test_url_safety.py:208`
- `tests/test_url_safety.py:219`
- `tests/test_url_safety.py:232`
- `tests/test_url_safety.py:246`
- `tests/test_url_safety.py:255`
- `tests/test_url_safety.py:257`
- `tests/test_url_safety.py:267`
- `tests/test_url_safety.py:269`
- `tests/test_url_safety.py:275`
- `tests/test_url_safety.py:276`
- `tests/test_url_safety.py:283`

## `check_outbound_host` — function, line 170
- **called from:**
- `routes/email/email_routes.py:94`
- `tests/test_email_account_host_ssrf.py:40`
- `tests/test_email_account_host_ssrf.py:42`
- `tests/test_email_account_host_ssrf.py:59`
- `tests/test_email_account_host_ssrf.py:61`
- `tests/test_email_account_host_ssrf.py:67`
- `tests/test_email_account_host_ssrf.py:72`
- `tests/test_email_account_host_ssrf.py:73`
- `tests/test_email_account_host_ssrf.py:77`
- `tests/test_email_account_host_ssrf.py:79`
- `tests/test_email_account_host_ssrf.py:81`
- `tests/test_email_account_host_ssrf.py:83`
- `tests/test_email_account_host_ssrf.py:90`
- `tests/test_email_account_host_ssrf.py:91`
- `tests/test_email_account_host_ssrf.py:470`
- `tests/test_email_account_host_ssrf.py:474`

## `OutboundAddressBlocked` — class, line 222
- **called from:**
- `src/url_safety.py:259`

## `connect_outbound_tcp` — function, line 226
- **called from:**
- `routes/email/email_helpers.py:210`
- `routes/email/email_helpers.py:237`
- `tests/test_codeql_python_residual_closure.py:286`
- `tests/test_codeql_python_residual_closure.py:339`
- `tests/test_codeql_python_residual_closure.py:347`
- `tests/test_codeql_python_residual_closure.py:350`
- `tests/test_codeql_python_residual_closure.py:369`
- `tests/test_codeql_python_residual_closure.py:372`
- `tests/test_codeql_python_residual_closure.py:382`
- `tests/test_email_account_host_ssrf.py:279`
- `tests/test_email_account_host_ssrf.py:290`
- `tests/test_email_account_host_ssrf.py:351`
- `tests/test_email_account_host_ssrf.py:356`
- `tests/test_email_account_host_ssrf.py:447`
- `tests/test_email_account_host_ssrf.py:456`
- `tests/test_email_account_host_ssrf.py:465`
