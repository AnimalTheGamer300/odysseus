# `routes/email/email_pollers.py` — definitions & call sites

28 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_extract_json_array_from_text` — function, line 60
- **called from:**
- `routes/email/email_pollers.py:1134`

## `_calendar_attachment_payloads` — function, line 89
- **called from:**
- `routes/email/email_pollers.py:113`
- `routes/email/email_pollers.py:865`

## `_import_calendar_attachments` — function (async), line 109
- **called from:**
- `routes/email/email_pollers.py:932`
- `tests/test_review_calendar_invitation.py:47`

## `_owner_for_email_account` — function, line 172
- **called from:**
- `routes/email/email_pollers.py:665`
- `routes/email/email_pollers.py:1633`

## `_email_date_only` — function, line 187
- **called from:**
- `routes/email/email_pollers.py:240`
- `routes/email/email_pollers.py:241`

## `_effective_settings_for_email_account` — function, line 212
- **called from:**
- `routes/email/email_pollers.py:640`

## `_away_reply_active` — function, line 229
- **called from:**
- `routes/email/email_pollers.py:644`

## `_message_after_away_enabled` — function, line 249
- **called from:**
- `routes/email/email_pollers.py:861`

## `_away_reply_period_key` — function, line 273
- **called from:**
- `routes/email/email_pollers.py:376`
- `routes/email/email_pollers.py:417`

## `_away_reply_cooldown_seconds` — function, line 279
- **called from:**
- `routes/email/email_pollers.py:374`

## `_ensure_away_reply_table` — function, line 290
- **called from:**
- `routes/email/email_pollers.py:361`
- `routes/email/email_pollers.py:402`

## `_sender_is_automated` — function, line 313
- **called from:**
- `routes/email/email_pollers.py:439`
- `routes/email/email_pollers.py:851`

## `_remove_urgent_tag_from_cache` — function, line 333
- **called from:**
- `routes/email/email_pollers.py:853`

## `_away_reply_already_sent` — function, line 358
- **called from:**
- `routes/email/email_pollers.py:441`
- `routes/email/email_pollers.py:862`

## `_record_away_reply` — function, line 399
- **called from:**
- `routes/email/email_pollers.py:477`

## `_send_away_reply` — function, line 426
- **called from:**
- `routes/email/email_pollers.py:883`

## `_emit_progress` — function (async), line 483
- **called from:**
- `routes/email/email_pollers.py:605`
- `routes/email/email_pollers.py:670`
- `routes/email/email_pollers.py:712`
- `routes/email/email_pollers.py:877`
- `routes/email/email_pollers.py:1012`
- `routes/email/email_pollers.py:1050`
- `routes/email/email_pollers.py:1055`
- `routes/email/email_pollers.py:1519`

## `_run_auto_summarize_once` — function (async), line 494
- **called from:**
- `src/builtin_actions.py:1152`
- `src/builtin_actions.py:1173`
- `src/builtin_actions.py:1708`

## `_latest_inbox_fallback_uids` — function, line 535
- **called from:**
- `routes/email/email_pollers.py:703`
- `tests/test_email_fallback_reconnect.py:41`
- `tests/test_email_fallback_reconnect.py:57`
- `tests/test_email_fallback_reconnect.py:67`

## `_auto_summarize_pass` — function (async), line 565
- **called from:**
- `routes/email/email_pollers.py:516`
- `routes/email/email_pollers.py:1578`
- `routes/email/email_routes.py:467`

## `_auto_summarize_pass_single` — function (async), line 633
- **called from:**
- `routes/email/email_pollers.py:592`
- `routes/email/email_pollers.py:606`
- `routes/email/email_pollers.py:621`
- `tests/test_email_polly_imap_leak.py:96`
- `tests/test_email_summary_llm.py:431`

## `_auto_summarize_poller` — function (async), line 1570
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_scheduled_poll_once` — function, line 1583
- **called from:**
- `tests/test_email_owner_scope.py:652`
- `tests/test_scheduled_poll_race.py:98`

## `_scheduled_email_poller` — function (async), line 1698
- **called from:**
- `routes/email/email_pollers.py:1746`

## `_inprocess_pollers_enabled` — function, line 1716
- **called from:**
- `routes/email/email_pollers.py:1734`
- `tests/test_security_regressions.py:560`
- `tests/test_security_regressions.py:565`
- `tests/test_security_regressions.py:570`

## `_start_poller` — function, line 1727
- **called from:**
- `routes/email/email_routes.py:1723`

## `_launch` — function, line 1742
- **called from:**
- `routes/email/email_pollers.py:1751`
- `routes/email/email_pollers.py:1762`

## `_deferred_start` — function (async), line 1758
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
