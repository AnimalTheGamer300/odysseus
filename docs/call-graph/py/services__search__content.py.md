# `services/search/content.py` — definitions & call sites

21 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_private_address` — function, line 29
- **called from:**
- `services/search/content.py:30`
- `src/outbound_fetch.py:83`
- `src/outbound_fetch.py:87`
- `src/outbound_fetch.py:106`
- `src/outbound_fetch.py:114`

## `_resolve_hostname_ips` — function, line 33
- **called from:**
- `services/search/content.py:34`
- `src/url_security.py:68`
- `src/webhook_manager.py:106`
- `src/webhook_manager.py:153`

## `_public_http_url` — function, line 37
- **called from:**
- `services/search/content.py:38`
- `tests/test_search_content_url_guards.py:20`
- `tests/test_search_content_url_guards.py:31`
- `tests/test_search_content_url_guards.py:36`
- `tests/test_security_regressions.py:849`
- `tests/test_security_regressions.py:850`
- `tests/test_security_regressions.py:851`
- `tests/test_security_regressions.py:861`
- `tests/test_security_regressions.py:901`
- `tests/test_security_regressions.py:906`
- `tests/test_security_regressions.py:913`
- `tests/test_security_regressions.py:920`

## `_resolve_public_ips` — function, line 41
- **called from:**
- `services/search/content.py:42`
- `src/agent_tools/web_tools.py:1250`
- `src/agent_tools/web_tools_prewave3.py:1254`
- `tests/test_security_regressions.py:1301`

## `_get_public_url` — function, line 51
- **called from:**
- `services/search/content.py:52`
- `services/search/content.py:328`
- `services/search/content.py:368`
- `tests/test_security_regressions.py:964`
- `tests/test_security_regressions.py:1498`

## `_extract_pdf_text` — function, line 75
- **called from:**
- `services/search/content.py:395`

## `_extract_meta` — function, line 116
- **called from:**
- `services/search/content.py:468`

## `_extract_og_image` — function, line 129
- **called from:**
- `services/search/content.py:475`
- `tests/test_og_image_extraction.py:19`
- `tests/test_og_image_extraction.py:24`
- `tests/test_og_image_extraction.py:32`

## `_linked_text` — function, line 151
- **called from:**
- `services/search/content.py:545`
- `tests/test_search_content_extraction_parity.py:63`

## `_page_entries` — function, line 175
- **called from:**
- `services/search/content.py:546`

## `_extract_lists` — function, line 214
- **called from:**
- `services/search/content.py:547`

## `_extract_tables` — function, line 224
- **called from:**
- `services/search/content.py:548`

## `_extract_code_blocks` — function, line 238
- **called from:**
- `services/search/content.py:549`

## `_detect_js_frameworks` — function, line 248
- **called from:**
- `services/search/content.py:476`

## `_empty_result` — function, line 267
- **called from:**
- `services/search/content.py:337`
- `services/search/content.py:340`
- `services/search/content.py:343`
- `services/search/content.py:346`
- `services/search/content.py:382`
- `services/search/content.py:394`
- `services/search/content.py:462`
- `services/search/content.py:535`

## `fetch_webpage_content` — function, line 288
- **called from:**
- `services/search/service.py:98`
- `src/agent_tools/web_tools.py:763`
- `src/agent_tools/web_tools_prewave3.py:767`
- `src/chat_processor.py:500`
- `tests/test_search_content_extraction_parity.py:47`
- `tests/test_search_content_extraction_parity.py:99`
- `tests/test_search_content_extraction_parity.py:109`
- `tests/test_search_content_extraction_parity.py:125`
- `tests/test_search_content_extraction_parity.py:146`
- `tests/test_search_content_extraction_parity.py:177`
- `tests/test_search_content_extraction_parity.py:202`
- `tests/test_search_content_extraction_parity.py:239`
- `tests/test_web_fetch_plaintext.py:47`
- `tests/test_web_fetch_plaintext.py:58`
- `tests/test_web_fetch_plaintext.py:66`
- `tests/test_web_fetch_plaintext.py:76`
- `tests/test_web_fetch_plaintext.py:84`
- `tests/test_web_fetch_plaintext.py:92`
- `tests/test_web_fetch_plaintext.py:99`
- `tests/test_web_fetch_plaintext.py:108`
- `tests/test_web_fetch_size_caps.py:111`
- `tests/test_web_fetch_size_caps.py:122`
- `tests/test_web_fetch_size_caps.py:131`
- `tests/test_web_fetch_size_caps.py:141`
- `tests/test_web_fetch_size_caps.py:151`
- `tests/test_web_fetch_size_caps.py:159`
- `tests/test_web_fetch_size_caps.py:170`
- `tests/test_web_fetch_size_caps.py:179`
- `tests/test_web_fetch_size_caps.py:201`
- `tests/test_web_fetch_size_caps.py:244`
- `tests/test_web_fetch_size_caps.py:262`
- `tests/test_web_fetch_size_caps.py:272`

## `_cache_result` — function, line 563
- **called from:**
- `services/search/content.py:411`
- `services/search/content.py:454`
- `services/search/content.py:463`
- `services/search/content.py:559`

## `extract_key_points` — function, line 578
- **called from:**
- `services/search/core.py:1236`

## `get_tldr` — function, line 590
- **called from:**
- `services/search/core.py:1242`

## `extract_quotes` — function, line 597
- **called from:**
- `services/search/core.py:1247`
- `tests/test_extract_quotes.py:10`
- `tests/test_extract_quotes.py:16`
- `tests/test_extract_quotes.py:24`
- `tests/test_extract_quotes.py:28`

## `extract_statistics` — function, line 604
- **called from:**
- `services/search/core.py:1253`
- `tests/test_extract_statistics.py:12`
- `tests/test_extract_statistics.py:17`
- `tests/test_extract_statistics.py:21`
- `tests/test_extract_statistics.py:25`
