# `routes/email_pollers.py` — definitions & call sites

25 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_extract_json_array_from_text` — function, line 60
- **called from:**
- `routes/email_pollers.py:950`

## `_owner_for_email_account` — function, line 89
- **called from:**
- `routes/email_pollers.py:538`
- `routes/email_pollers.py:1433`

## `_email_date_only` — function, line 104
- **called from:**
- `routes/email_pollers.py:157`
- `routes/email_pollers.py:158`

## `_effective_settings_for_email_account` — function, line 129
- **called from:**
- `routes/email_pollers.py:516`

## `_away_reply_active` — function, line 146
- **called from:**
- `routes/email_pollers.py:520`

## `_message_after_away_enabled` — function, line 166
- **called from:**
- `routes/email_pollers.py:722`

## `_away_reply_period_key` — function, line 190
- **called from:**
- `routes/email_pollers.py:265`
- `routes/email_pollers.py:306`

## `_away_reply_cooldown_seconds` — function, line 196
- **called from:**
- `routes/email_pollers.py:263`

## `_ensure_away_reply_table` — function, line 207
- **called from:**
- `routes/email_pollers.py:250`
- `routes/email_pollers.py:291`

## `_sender_is_automated` — function, line 230
- **called from:**
- `routes/email_pollers.py:328`

## `_away_reply_already_sent` — function, line 247
- **called from:**
- `routes/email_pollers.py:330`
- `routes/email_pollers.py:723`

## `_record_away_reply` — function, line 288
- **called from:**
- `routes/email_pollers.py:366`

## `_send_away_reply` — function, line 315
- **called from:**
- `routes/email_pollers.py:740`

## `_emit_progress` — function (async), line 372
- **called from:**
- `routes/email_pollers.py:487`
- `routes/email_pollers.py:543`
- `routes/email_pollers.py:585`
- `routes/email_pollers.py:734`
- `routes/email_pollers.py:829`
- `routes/email_pollers.py:866`
- `routes/email_pollers.py:871`
- `routes/email_pollers.py:1319`

## `_run_auto_summarize_once` — function (async), line 383
- **called from:**
- `src/builtin_actions.py:1010`
- `src/builtin_actions.py:1029`
- `src/builtin_actions.py:1535`

## `_latest_inbox_fallback_uids` — function, line 420
- **called from:**
- `routes/email_pollers.py:576`
- `tests/test_email_fallback_reconnect.py:41`
- `tests/test_email_fallback_reconnect.py:57`
- `tests/test_email_fallback_reconnect.py:67`

## `_auto_summarize_pass` — function (async), line 450
- **called from:**
- `routes/email_pollers.py:404`
- `routes/email_pollers.py:1378`
- `routes/email_routes.py:423`

## `_auto_summarize_pass_single` — function (async), line 509
- **called from:**
- `routes/email_pollers.py:477`
- `routes/email_pollers.py:488`
- `routes/email_pollers.py:500`
- `tests/test_email_polly_imap_leak.py:96`
- `tests/test_email_summary_llm.py:387`

## `_auto_summarize_poller` — function (async), line 1370
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_scheduled_poll_once` — function, line 1383
- **called from:**
- `tests/test_email_owner_scope.py:652`
- `tests/test_scheduled_poll_race.py:98`

## `_scheduled_email_poller` — function (async), line 1498
- **called from:**
- `routes/email_pollers.py:1546`

## `_inprocess_pollers_enabled` — function, line 1516
- **called from:**
- `routes/email_pollers.py:1534`
- `tests/test_security_regressions.py:559`
- `tests/test_security_regressions.py:564`
- `tests/test_security_regressions.py:569`

## `_start_poller` — function, line 1527
- **called from:**
- `routes/email_routes.py:1514`

## `_launch` — function, line 1542
- **called from:**
- `routes/email_pollers.py:1551`
- `routes/email_pollers.py:1562`

## `_deferred_start` — function (async), line 1558
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
