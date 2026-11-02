# `services/search/content.py` — definitions & call sites

25 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_private_address` — function, line 33
- **called from:**
- `services/search/content.py:34`
- `src/outbound_fetch.py:83`
- `src/outbound_fetch.py:87`
- `src/outbound_fetch.py:106`
- `src/outbound_fetch.py:114`

## `_resolve_hostname_ips` — function, line 37
- **called from:**
- `services/search/content.py:38`
- `src/url_security.py:68`
- `src/webhook_manager.py:106`
- `src/webhook_manager.py:153`

## `_public_http_url` — function, line 41
- **called from:**
- `services/search/content.py:42`
- `tests/test_search_content_url_guards.py:20`
- `tests/test_search_content_url_guards.py:31`
- `tests/test_search_content_url_guards.py:36`
- `tests/test_security_regressions.py:848`
- `tests/test_security_regressions.py:849`
- `tests/test_security_regressions.py:850`
- `tests/test_security_regressions.py:860`
- `tests/test_security_regressions.py:900`
- `tests/test_security_regressions.py:905`
- `tests/test_security_regressions.py:912`
- `tests/test_security_regressions.py:919`

## `_resolve_public_ips` — function, line 45
- **called from:**
- `services/search/content.py:46`
- `tests/test_security_regressions.py:1299`

## `_get_public_url` — function, line 55
- **called from:**
- `services/search/content.py:56`
- `services/search/content.py:389`
- `tests/test_security_regressions.py:963`
- `tests/test_security_regressions.py:1496`

## `_extract_meta` — function, line 77
- **called from:**
- `services/search/content.py:504`

## `_extract_og_image` — function, line 90
- **called from:**
- `services/search/content.py:505`
- `tests/test_og_image_extraction.py:19`
- `tests/test_og_image_extraction.py:24`
- `tests/test_og_image_extraction.py:32`

## `_extract_lists` — function, line 112
- **called from:**
- `services/search/content.py:575`

## `_extract_tables` — function, line 122
- **called from:**
- `services/search/content.py:576`

## `_extract_code_blocks` — function, line 136
- **called from:**
- `services/search/content.py:577`

## `_detect_js_frameworks` — function, line 146
- **called from:**
- `services/search/content.py:506`

## `_empty_result` — function, line 165
- **called from:**
- `services/search/content.py:398`
- `services/search/content.py:401`
- `services/search/content.py:404`
- `services/search/content.py:407`
- `services/search/content.py:424`
- `services/search/content.py:498`

## `_h1_ancestor_ids` — function, line 207
- **called from:**
- `services/search/content.py:268`
- `services/search/content.py:320`

## `_attr_tokens` — function, line 224
- **called from:**
- `services/search/content.py:255`
- `services/search/content.py:294`
- `services/search/content.py:294`

## `_is_boilerplate` — function, line 234
- **called from:**
- `services/search/content.py:271`
- `services/search/content.py:323`

## `_strip_boilerplate` — function, line 261
- **called from:**
- `services/search/content.py:516`

## `_content_attr_text` — function, line 293
- **called from:**
- `services/search/content.py:316`

## `_extract_main_content` — function, line 297
- **called from:**
- `services/search/content.py:529`

## `fetch_webpage_content` — function, line 346
- **called from:**
- `services/search/service.py:98`
- `src/agent_tools/web_tools.py:124`
- `src/chat_processor.py:482`
- `tests/test_search_content_extraction_parity.py:63`
- `tests/test_search_content_extraction_parity.py:88`
- `tests/test_search_content_extraction_parity.py:125`
- `tests/test_web_fetch_plaintext.py:47`
- `tests/test_web_fetch_plaintext.py:58`
- `tests/test_web_fetch_plaintext.py:66`
- `tests/test_web_fetch_plaintext.py:76`
- `tests/test_web_fetch_plaintext.py:84`
- `tests/test_web_fetch_plaintext.py:92`
- `tests/test_web_fetch_plaintext.py:99`
- `tests/test_web_fetch_plaintext.py:108`
- `tests/test_web_fetch_size_caps.py:111`
- `tests/test_web_fetch_size_caps.py:121`
- `tests/test_web_fetch_size_caps.py:131`
- `tests/test_web_fetch_size_caps.py:141`
- `tests/test_web_fetch_size_caps.py:149`
- `tests/test_web_fetch_size_caps.py:160`
- `tests/test_web_fetch_size_caps.py:169`
- `tests/test_web_fetch_size_caps.py:186`
- `tests/test_web_fetch_size_caps.py:197`

## `_cache_result` — function, line 591
- **called from:**
- `services/search/content.py:455`
- `services/search/content.py:490`
- `services/search/content.py:499`
- `services/search/content.py:587`

## `extract_key_points` — function, line 643
- **called from:**
- `services/search/core.py:438`

## `get_tldr` — function, line 655
- **called from:**
- `services/search/core.py:444`

## `extract_quotes` — function, line 676
- **called from:**
- `services/search/core.py:449`
- `tests/test_extract_quotes.py:10`
- `tests/test_extract_quotes.py:16`
- `tests/test_extract_quotes.py:24`
- `tests/test_extract_quotes.py:28`

## `extract_statistics` — function, line 683
- **called from:**
- `services/search/core.py:455`
- `tests/test_extract_statistics.py:12`
- `tests/test_extract_statistics.py:17`
- `tests/test_extract_statistics.py:21`
- `tests/test_extract_statistics.py:29`
- `tests/test_extract_statistics.py:39`
- `tests/test_extract_statistics.py:47`
- `tests/test_extract_statistics.py:54`

## `_classify` — function, line 709
- **called from:**
- `services/search/content.py:744`
- `src/url_safety.py:103`
- `tests/test_tool_rag_contacts_domain.py:40`
- `tests/test_tool_rag_contacts_domain.py:49`
- `tests/test_tool_rag_contacts_domain.py:69`
- `tests/test_tool_rag_contacts_domain.py:70`
- `tests/test_tool_rag_contacts_domain.py:71`
- `tests/test_tool_rag_contacts_domain.py:72`
