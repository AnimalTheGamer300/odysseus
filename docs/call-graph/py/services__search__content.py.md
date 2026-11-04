# `services/search/content.py` — definitions & call sites

18 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_private_address` — function, line 28
- **called from:**
- `services/search/content.py:29`
- `src/outbound_fetch.py:83`
- `src/outbound_fetch.py:87`
- `src/outbound_fetch.py:106`
- `src/outbound_fetch.py:114`

## `_resolve_hostname_ips` — function, line 32
- **called from:**
- `services/search/content.py:33`
- `src/url_security.py:68`
- `src/webhook_manager.py:106`
- `src/webhook_manager.py:153`

## `_public_http_url` — function, line 36
- **called from:**
- `services/search/content.py:37`
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

## `_resolve_public_ips` — function, line 40
- **called from:**
- `services/search/content.py:41`
- `tests/test_security_regressions.py:1299`

## `_get_public_url` — function, line 50
- **called from:**
- `services/search/content.py:51`
- `services/search/content.py:224`
- `tests/test_security_regressions.py:963`
- `tests/test_security_regressions.py:1496`

## `_extract_meta` — function, line 72
- **called from:**
- `services/search/content.py:339`

## `_extract_og_image` — function, line 85
- **called from:**
- `services/search/content.py:340`
- `tests/test_og_image_extraction.py:19`
- `tests/test_og_image_extraction.py:24`
- `tests/test_og_image_extraction.py:32`

## `_extract_lists` — function, line 107
- **called from:**
- `services/search/content.py:376`

## `_extract_tables` — function, line 117
- **called from:**
- `services/search/content.py:377`

## `_extract_code_blocks` — function, line 131
- **called from:**
- `services/search/content.py:378`

## `_detect_js_frameworks` — function, line 141
- **called from:**
- `services/search/content.py:341`

## `_empty_result` — function, line 160
- **called from:**
- `services/search/content.py:233`
- `services/search/content.py:236`
- `services/search/content.py:239`
- `services/search/content.py:242`
- `services/search/content.py:259`
- `services/search/content.py:333`

## `fetch_webpage_content` — function, line 181
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

## `_cache_result` — function, line 392
- **called from:**
- `services/search/content.py:290`
- `services/search/content.py:325`
- `services/search/content.py:334`
- `services/search/content.py:388`

## `extract_key_points` — function, line 407
- **called from:**
- `services/search/core.py:438`

## `get_tldr` — function, line 419
- **called from:**
- `services/search/core.py:444`

## `extract_quotes` — function, line 426
- **called from:**
- `services/search/core.py:449`
- `tests/test_extract_quotes.py:10`
- `tests/test_extract_quotes.py:16`
- `tests/test_extract_quotes.py:24`
- `tests/test_extract_quotes.py:28`

## `extract_statistics` — function, line 433
- **called from:**
- `services/search/core.py:455`
- `tests/test_extract_statistics.py:12`
- `tests/test_extract_statistics.py:17`
- `tests/test_extract_statistics.py:21`
- `tests/test_extract_statistics.py:25`
