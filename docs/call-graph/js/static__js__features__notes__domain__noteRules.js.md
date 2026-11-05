# `static/js/features/notes/domain/noteRules.js` — definitions & call sites

12 definitions (regex-based, best-effort).
**Exports:** `_goalProgress`, `_hasActiveReminder`, `_hasItems`, `_isCalendarReminderNote`, `_isNoteFullyDone`, `_isPastReminder`, `_nextGoalStep`, `_noteTags`, `_noteToAgentPrompt`, `_serializeNoteForCopy`, `_standardVisualVariant`, `_visibleNoteTags`

## `_isCalendarReminderNote` — function, line 3
- **called from:**
- `static/js/features/notes/application/queries.js:62`
- `static/js/features/notes/domain/noteRules.js:3`

## `_hasActiveReminder` — function, line 7
- **called from:**
- `static/js/features/notes/application/queries.js:48`
- `static/js/features/notes/application/queries.js:49`
- `static/js/features/notes/domain/noteRules.js:7`
- `static/js/features/notes/index.js:118`
- `static/js/features/notes/index.js:118`
- `static/js/features/notes/ui/cardRendering.js:153`
- `static/js/features/notes/ui/reminderDisplay.js:53`

## `_isNoteFullyDone` — function, line 14
- **called from:**
- `static/js/features/notes/application/reminders.js:132`
- `static/js/features/notes/application/reminders.js:140`
- `static/js/features/notes/domain/noteRules.js:8`
- `static/js/features/notes/domain/noteRules.js:14`
- `static/js/features/notes/index.js:74`
- `static/js/features/notes/ui/reminderDisplay.js:115`

## `_hasItems` — function, line 21
- **called from:**
- `static/js/features/notes/application/reminders.js:78`
- `static/js/features/notes/domain/noteRules.js:15`
- `static/js/features/notes/domain/noteRules.js:21`
- `static/js/features/notes/index.js:75`
- `static/js/features/notes/index.js:91`
- `static/js/features/notes/ui/cardRendering.js:102`
- `static/js/features/notes/ui/cardRendering.js:177`
- `static/js/features/notes/ui/cardRendering.js:186`
- `static/js/features/notes/ui/cardRendering.js:199`

## `_goalProgress` — function, line 25
- **called from:**
- `static/js/features/notes/domain/noteRules.js:25`
- `static/js/features/notes/ui/cardRendering.js:79`
- `static/js/features/notes/ui/cardRendering.js:157`

## `_nextGoalStep` — function, line 31
- **called from:**
- `static/js/features/notes/application/queries.js:21`
- `static/js/features/notes/domain/noteRules.js:31`
- `static/js/features/notes/ui/cardRendering.js:77`
- `static/js/features/notes/ui/filters.js:34`

## `_noteTags` — function, line 39
- **called from:**
- `static/js/features/notes/application/queries.js:10`
- `static/js/features/notes/domain/noteRules.js:39`
- `static/js/features/notes/domain/noteRules.js:47`

## `_visibleNoteTags` — function, line 46
- **called from:**
- `static/js/features/notes/application/queries.js:16`
- `static/js/features/notes/domain/noteRules.js:46`
- `static/js/features/notes/ui/cardRendering.js:149`
- `static/js/features/notes/ui/filters.js:25`
- `static/js/features/notes/ui/filters.js:30`

## `_isPastReminder` — function, line 50
- **called from:**
- `static/js/features/notes/application/deletion.js:21`
- `static/js/features/notes/domain/noteRules.js:50`
- `static/js/features/notes/index.js:121`
- `static/js/features/notes/index.js:121`
- `static/js/features/notes/ui/filters.js:29`

## `_serializeNoteForCopy` — function, line 56
- **called from:**
- `static/js/features/notes/domain/noteRules.js:56`
- `static/js/features/notes/ui/clipboard.js:47`

## `_noteToAgentPrompt` — function, line 70
- **called from:**
- `static/js/features/notes/application/agentActions.js:16`
- `static/js/features/notes/domain/noteRules.js:70`

## `_standardVisualVariant` — function, line 82
- **called from:**
- `static/js/features/notes/domain/noteRules.js:82`
- `static/js/features/notes/ui/cardRendering.js:141`
