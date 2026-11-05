# `src/email_calendar_import.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_invitation_lock` — function (async), line 16
- decorator: `asynccontextmanager`
- **called from:**
- `src/email_calendar_import.py:54`
- `tests/test_review_calendar_invitation.py:129`
- `tests/test_review_calendar_invitation.py:139`
- `tests/test_review_calendar_invitation.py:163`

## `apply_invitation` — function (async), line 53
- **called from:**
- `routes/email/email_pollers.py:157`

## `_apply_invitation` — function (async), line 58
- **called from:**
- `src/email_calendar_import.py:55`

## `exclude_occurrence` — function, line 117
- **called from:**
- `src/email_calendar_import.py:126`
- `src/email_calendar_import.py:170`
