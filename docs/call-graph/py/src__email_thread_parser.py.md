# `src/email_thread_parser.py` — definitions & call sites

17 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_extract_quote_meta` — function, line 121
- **called from:**
- `src/email_thread_parser.py:373`
- `src/email_thread_parser.py:378`
- `src/email_thread_parser.py:536`
- `src/email_thread_parser.py:580`

## `_strip_mashed_header` — function, line 183
- **called from:**
- `src/email_thread_parser.py:202`

## `_normalize_body` — function, line 195
- **called from:**
- `src/email_thread_parser.py:269`

## `_outlook_header_block_end` — function, line 217
- **called from:**
- `src/email_thread_parser.py:345`
- `src/email_thread_parser.py:361`

## `_parse_plaintext` — function, line 257
- **called from:**
- `src/email_thread_parser.py:613`

## `lookahead_content_base` — function, line 299
- **called from:**
- `src/email_thread_parser.py:370`

## `flush` — function, line 305
- **called from:**
- `core/atomic_io.py:37`
- `core/atomic_io.py:58`
- `core/database.py:525`
- `routes/calendar_routes.py:317`
- `routes/calendar_routes.py:325`
- `routes/email_routes.py:5756`
- `scripts/demo_email/demo_account.py:117`
- `scripts/demo_email/demo_account.py:165`
- `scripts/migrate_searxng_settings.py:133`
- `scripts/pr_blocker_audit.py:125`
- `scripts/pr_blocker_audit.py:138`
- `scripts/pr_blocker_audit.py:144`
- `scripts/pr_blocker_audit.py:151`
- `src/api_key_manager.py:94`
- `src/email_thread_parser.py:328`
- `src/email_thread_parser.py:334`
- `src/email_thread_parser.py:371`
- `src/email_thread_parser.py:385`
- `src/llm_core.py:3241`
- `src/llm_core.py:3259`
- `src/llm_core.py:3518`
- `src/llm_core.py:3760`
- `src/task_scheduler.py:2616`
- `src/upload_handler.py:745`
- `tests/test_atomic_io.py:101`
- `tests/test_launcher.py:24`
- `static/js/chat.js:2840`
- `static/js/emailLibrary.js:6387`
- `static/js/emailLibrary.js:6393`
- `static/js/emailLibrary.js:6398`
- `static/js/liveThinkingThrottle.js:18`
- `static/js/liveThinkingThrottle.js:191`

## `_escape_to_html` — function, line 392
- **called from:**
- `src/email_thread_parser.py:315`

## `_is_quote_container` — function, line 408
- **called from:**
- `src/email_thread_parser.py:451`
- `src/email_thread_parser.py:458`
- `src/email_thread_parser.py:539`
- `src/email_thread_parser.py:544`
- `src/email_thread_parser.py:581`
- `src/email_thread_parser.py:585`

## `_parse_html` — function, line 432
- **called from:**
- `src/email_thread_parser.py:609`

## `has_quote_ancestor` — function, line 455
- **called from:**
- `src/email_thread_parser.py:463`

## `_strip_trailing_attribution` — function, line 496
- **called from:**
- `src/email_thread_parser.py:519`

## `_walk` — function, line 535
- **called from:**
- `src/email_thread_parser.py:576`
- `src/email_thread_parser.py:595`
- `src/email_thread_parser.py:598`

## `has_quote_between` — function, line 541
- **called from:**
- `src/email_thread_parser.py:548`
- `src/email_thread_parser.py:589`

## `_walk_with_meta` — function, line 578
- **called from:**
- `src/email_thread_parser.py:571`

## `has_quote_between` — function, line 582
- **called from:**
- `src/email_thread_parser.py:548`
- `src/email_thread_parser.py:589`

## `parse_thread` — function, line 605
- **called from:**
- `routes/email_routes.py:3123`
- `tests/test_email_thread_parser_nonstring.py:5`
- `tests/test_email_thread_parser_nonstring.py:6`
- `tests/test_email_thread_parser_nonstring.py:10`
- `tests/test_forwarded_message_divider.py:23`
- `tests/test_forwarded_message_divider.py:47`
- `tests/test_forwarded_message_divider.py:57`
