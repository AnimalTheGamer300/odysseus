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
- `core/atomic_io.py:43`
- `core/atomic_io.py:76`
- `core/atomic_io.py:97`
- `core/database.py:555`
- `routes/calendar_routes.py:331`
- `routes/calendar_routes.py:339`
- `routes/email/email_routes.py:7545`
- `scripts/cook_sft_alex_conversations.py:235`
- `scripts/demo_email/demo_account.py:117`
- `scripts/demo_email/demo_account.py:165`
- `scripts/eval_exact_file_routing.py:158`
- `scripts/eval_odysseus_tool_use.py:658`
- `scripts/eval_odysseus_tool_use.py:661`
- `scripts/migrate_searxng_settings.py:133`
- `scripts/pr_blocker_audit.py:125`
- `scripts/pr_blocker_audit.py:138`
- `scripts/pr_blocker_audit.py:144`
- `scripts/pr_blocker_audit.py:151`
- `scripts/run_sft_environment_expansion.py:517`
- `src/agent_tools/filesystem_tools.py:615`
- `src/api_key_manager.py:94`
- `src/browser_identity.py:254`
- `src/containment_worker.py:80`
- `src/email_thread_parser.py:328`
- `src/email_thread_parser.py:334`
- `src/email_thread_parser.py:371`
- `src/email_thread_parser.py:385`
- `src/llm_core.py:3669`
- `src/llm_core.py:3687`
- `src/llm_core.py:3971`
- `src/llm_core.py:4308`
- `src/task_scheduler.py:2849`
- `src/upload_handler.py:799`
- `tests/smoke/stub_provider.py:136`
- `tests/test_atomic_io.py:101`
- `tests/test_codeql_python_residual_closure.py:140`
- `tests/test_codeql_python_residual_closure.py:149`
- `tests/test_codeql_python_residual_closure.py:155`
- `tests/test_codeql_python_residual_closure.py:157`
- `tests/test_daily_brief_local_calendar.py:56`
- `tests/test_launcher.py:24`
- `static/js/chat.js:4225`
- `static/js/emailLibrary/bodyRender.js:746`
- `static/js/emailLibrary/bodyRender.js:752`
- `static/js/emailLibrary/bodyRender.js:757`
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
- `routes/email/email_routes.py:3933`
- `tests/test_email_thread_parser_nonstring.py:5`
- `tests/test_email_thread_parser_nonstring.py:6`
- `tests/test_email_thread_parser_nonstring.py:10`
- `tests/test_forwarded_message_divider.py:23`
- `tests/test_forwarded_message_divider.py:47`
- `tests/test_forwarded_message_divider.py:57`
