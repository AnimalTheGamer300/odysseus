# `static/js/features/notes/infrastructure/storage.js` — definitions & call sites

12 definitions (regex-based, best-effort).
**Exports:** `NOTES_FIRST_OPEN_HINT_KEY`, `NOTES_LABELS_COLLAPSED_KEY`, `REMINDER_ACTIVE_HIGHLIGHT_KEY`, `REMINDER_DISMISSED_AT_KEY`, `REMINDER_FIRED_KEY`, `REMINDER_GLOWED_KEY`, `REMINDER_PENDING_HIGHLIGHT_KEY`, `_DRAFT_PREFIX`, `createNotesPersistence`

## `createNotesPersistence` — function, line 11
- **called from:**
- `static/js/features/notes/index.js:54`
- `static/js/features/notes/infrastructure/storage.js:11`

## `_loadPendingHighlights` — function, line 12
- **called from:**
- `static/js/features/notes/infrastructure/storage.js:12`
- `static/js/features/notes/ui/reminderDisplay.js:37`
- `static/js/features/notes/ui/reminderDisplay.js:46`

## `_loadGlowedReminders` — function, line 17
- **called from:**
- `static/js/features/notes/application/submission.js:21`
- `static/js/features/notes/infrastructure/storage.js:17`
- `static/js/features/notes/ui/reminderDisplay.js:47`

## `_saveGlowedReminders` — function, line 22
- **called from:**
- `static/js/features/notes/application/submission.js:23`
- `static/js/features/notes/infrastructure/storage.js:22`
- `static/js/features/notes/ui/reminderDisplay.js:67`

## `_loadActiveHighlights` — function, line 26
- **called from:**
- `static/js/features/notes/infrastructure/storage.js:26`
- `static/js/features/notes/ui/cardRendering.js:54`
- `static/js/features/notes/ui/reminderDisplay.js:17`
- `static/js/features/notes/ui/reminderDisplay.js:27`

## `_saveActiveHighlights` — function, line 31
- **called from:**
- `static/js/features/notes/infrastructure/storage.js:31`
- `static/js/features/notes/ui/reminderDisplay.js:19`
- `static/js/features/notes/ui/reminderDisplay.js:30`

## `_savePendingHighlights` — function, line 35
- **called from:**
- `static/js/features/notes/infrastructure/storage.js:35`
- `static/js/features/notes/ui/reminderDisplay.js:39`
- `static/js/features/notes/ui/reminderDisplay.js:57`

## `_loadFiredReminders` — function, line 40
- **called from:**
- `static/js/features/notes/application/reminders.js:31`
- `static/js/features/notes/application/submission.js:18`
- `static/js/features/notes/infrastructure/storage.js:40`

## `_saveFiredReminders` — function, line 45
- **called from:**
- `static/js/features/notes/application/reminders.js:67`
- `static/js/features/notes/application/submission.js:20`
- `static/js/features/notes/infrastructure/storage.js:45`

## `_draftKey` — function, line 50
- **called from:**
- `static/js/features/notes/application/drafts.js:19`
- `static/js/features/notes/application/drafts.js:36`
- `static/js/features/notes/infrastructure/storage.js:50`
- `static/js/features/notes/infrastructure/storage.js:53`
- `static/js/features/notes/infrastructure/storage.js:56`

## `_loadDraft` — function, line 52
- **called from:**
- `static/js/features/notes/application/submission.js:42`
- `static/js/features/notes/application/submission.js:52`
- `static/js/features/notes/infrastructure/storage.js:52`
- `static/js/features/notes/ui/draftEditor.js:57`

## `_clearDraft` — function, line 56
- **called from:**
- `static/js/features/notes/application/drafts.js:36`
- `static/js/features/notes/application/submission.js:52`
- `static/js/features/notes/infrastructure/storage.js:56`
