# `static/js/features/notes/domain/recurrence.js` — definitions & call sites

19 definitions (regex-based, best-effort).
**Exports:** `_DAYS`, `_ORDINALS`, `_advanceRecurring`, `_formatDueDate`, `_formatReminderTag`, `_formatRepeatLabel`, `_hasTimeComponent`, `_isDueOverdue`, `_isDueTodayOrOverdue`, `_isLastWeekdayOfMonth`, `_lastWeekdayOfMonth`, `_laterTodayDate`, `_nextWeekDate`, `_normalizeRepeat`, `_nthWeekdayLabel`, `_nthWeekdayOfMonth`, `_snapToRepeat`, `_toLocalDatetimeStr`, `_tomorrowDate`

## `_hasTimeComponent` — function, line 4
- **called from:**
- `static/js/features/notes/application/queries.js:12`
- `static/js/features/notes/application/queries.js:14`
- `static/js/features/notes/application/reminders.js:35`
- `static/js/features/notes/application/reminders.js:141`
- `static/js/features/notes/domain/noteRules.js:42`
- `static/js/features/notes/domain/noteRules.js:51`
- `static/js/features/notes/domain/recurrence.js:4`
- `static/js/features/notes/domain/recurrence.js:13`
- `static/js/features/notes/domain/recurrence.js:30`
- `static/js/features/notes/ui/cardRendering.js:143`
- `static/js/features/notes/ui/cardRendering.js:150`
- `static/js/features/notes/ui/filters.js:28`
- `static/js/features/notes/ui/reminderDisplay.js:53`
- `static/js/features/notes/ui/reminderDisplay.js:119`

## `_formatDueDate` — function, line 8
- **called from:**
- `static/js/features/notes/domain/recurrence.js:8`
- `static/js/features/notes/index.js:104`
- `static/js/features/notes/index.js:104`
- `static/js/features/notes/ui/cardRendering.js:98`

## `_isDueOverdue` — function, line 26
- **called from:**
- `static/js/features/notes/domain/recurrence.js:26`
- `static/js/features/notes/index.js:105`
- `static/js/features/notes/index.js:105`
- `static/js/features/notes/ui/cardRendering.js:99`

## `_isDueTodayOrOverdue` — function, line 34
- **called from:**
- `static/js/features/notes/application/reminders.js:132`
- `static/js/features/notes/domain/recurrence.js:34`

## `_laterTodayDate` — function, line 43
- **called from:**
- `static/js/features/notes/domain/recurrence.js:43`
- `static/js/features/notes/index.js:107`
- `static/js/features/notes/index.js:107`
- `static/js/features/notes/ui/reminderPicker.js:53`
- `static/js/features/notes/ui/reminderPicker.js:53`

## `_tomorrowDate` — function, line 51
- **called from:**
- `static/js/features/notes/domain/recurrence.js:51`
- `static/js/features/notes/index.js:108`
- `static/js/features/notes/index.js:108`
- `static/js/features/notes/ui/reminderPicker.js:54`
- `static/js/features/notes/ui/reminderPicker.js:54`
- `static/js/features/notes/ui/reminderPicker.js:289`

## `_nextWeekDate` — function, line 58
- **called from:**
- `static/js/features/notes/domain/recurrence.js:58`
- `static/js/features/notes/index.js:109`
- `static/js/features/notes/index.js:109`
- `static/js/features/notes/ui/reminderPicker.js:55`
- `static/js/features/notes/ui/reminderPicker.js:55`
- `static/js/features/notes/ui/reminderPicker.js:55`

## `_toLocalDatetimeStr` — function, line 66
- **called from:**
- `static/js/features/notes/domain/recurrence.js:66`
- `static/js/features/notes/domain/recurrence.js:268`
- `static/js/features/notes/ui/reminderPicker.js:53`
- `static/js/features/notes/ui/reminderPicker.js:54`
- `static/js/features/notes/ui/reminderPicker.js:55`
- `static/js/features/notes/ui/reminderPicker.js:89`
- `static/js/features/notes/ui/reminderPicker.js:289`

## `pad` — arrow, line 68
- **called from:**
- `static/js/calendar.js:3787`
- `static/js/calendar.js:3787`
- `static/js/calendar.js:3787`
- `static/js/calendar.js:3787`
- `static/js/document.js:6976`
- `static/js/document.js:6976`
- `static/js/document.js:6976`
- `static/js/document.js:6976`
- `static/js/document.js:7000`
- `static/js/document.js:7000`
- `static/js/document.js:7000`
- `static/js/document.js:7000`
- `static/js/emailInbox.js:1249`
- `static/js/emailInbox.js:1249`
- `static/js/emailInbox.js:1249`
- `static/js/emailInbox.js:1249`
- `static/js/emailInbox.js:1286`
- `static/js/emailInbox.js:1286`
- `static/js/emailInbox.js:1286`
- `static/js/emailInbox.js:1286`
- `static/js/emailLibrary/aiReply.js:340`
- `static/js/emailLibrary/aiReply.js:340`
- `static/js/emailLibrary/aiReply.js:340`
- `static/js/emailLibrary/aiReply.js:340`
- `static/js/emailLibrary/aiReply.js:401`
- `static/js/emailLibrary/aiReply.js:401`
- `static/js/emailLibrary/aiReply.js:401`
- `static/js/emailLibrary/aiReply.js:401`
- `static/js/emailLibrary/settingsPage.js:116`
- `static/js/emailLibrary/settingsPage.js:116`
- `static/js/emailLibrary/settingsPage.js:144`
- `static/js/emailLibrary/settingsPage.js:144`
- `static/js/features/notes/domain/recurrence.js:69`
- `static/js/features/notes/domain/recurrence.js:69`
- `static/js/features/notes/domain/recurrence.js:69`
- `static/js/features/notes/domain/recurrence.js:69`
- `static/js/modalManager.js:716`

## `_formatReminderTag` — function, line 72
- **called from:**
- `static/js/features/notes/domain/recurrence.js:72`
- `static/js/features/notes/index.js:110`
- `static/js/features/notes/index.js:110`
- `static/js/features/notes/ui/cardRendering.js:146`
- `static/js/features/notes/ui/reminderPicker.js:27`

## `_nthWeekdayLabel` — function, line 87
- **called from:**
- `static/js/features/notes/domain/recurrence.js:87`

## `_isLastWeekdayOfMonth` — function, line 92
- **called from:**
- `static/js/features/notes/domain/recurrence.js:92`

## `_nthWeekdayOfMonth` — function, line 98
- **called from:**
- `static/js/features/notes/domain/recurrence.js:98`
- `static/js/features/notes/domain/recurrence.js:146`
- `static/js/features/notes/domain/recurrence.js:244`

## `_lastWeekdayOfMonth` — function, line 108
- **called from:**
- `static/js/features/notes/domain/recurrence.js:108`
- `static/js/features/notes/domain/recurrence.js:150`
- `static/js/features/notes/domain/recurrence.js:247`

## `_snapToRepeat` — function, line 114
- **called from:**
- `static/js/features/notes/domain/recurrence.js:114`
- `static/js/features/notes/index.js:111`
- `static/js/features/notes/index.js:111`
- `static/js/features/notes/ui/reminderPicker.js:87`

## `_formatRepeatLabel` — function, line 164
- **called from:**
- `static/js/features/notes/domain/recurrence.js:164`
- `static/js/features/notes/ui/cardRendering.js:146`
- `static/js/features/notes/ui/reminderPicker.js:28`

## `_normalizeRepeat` — function, line 190
- **called from:**
- `static/js/features/notes/domain/recurrence.js:166`
- `static/js/features/notes/domain/recurrence.js:190`
- `static/js/features/notes/domain/recurrence.js:209`
- `static/js/features/notes/ui/reminderPicker.js:70`
- `static/js/features/notes/ui/reminderPicker.js:86`

## `_advanceRecurring` — function, line 204
- **called from:**
- `static/js/features/notes/application/reminders.js:43`
- `static/js/features/notes/application/reminders.js:56`
- `static/js/features/notes/domain/recurrence.js:204`

## `step` — function, line 212
- **called from:**
- `static/js/editor/tools/liquify.js:10`
- `static/js/features/notes/domain/recurrence.js:212`
- `static/js/features/notes/domain/recurrence.js:258`
- `static/js/features/notes/domain/recurrence.js:265`
