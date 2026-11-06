# `static/js/features/notes/index.js` — definitions & call sites

77 definitions (regex-based, best-effort).
**Exports:** `closeNotes`, `closePanel`, `default`, `dismissFiredReminderDot`, `isNotesOpen`, `isPanelOpen`, `newNote`, `openNote`, `openNotes`, `openPanel`, `refreshDueBadge`, `startNotesBackground`, `togglePanel`

## `_pushUndo` — function, line 95
- **called from:**
- `static/js/features/notes/application/workflows.js:12`
- `static/js/features/notes/application/workflows.js:47`
- `static/js/features/notes/index.js:95`
- `static/js/features/notes/index.js:95`

## `_popAndRunUndo` — function, line 96
- **called from:**
- `static/js/features/notes/application/workflows.js:17`
- `static/js/features/notes/index.js:96`
- `static/js/features/notes/index.js:96`
- `static/js/features/notes/ui/panel.js:275`

## `_undoArchive` — function, line 97
- **called from:**
- `static/js/features/notes/application/workflows.js:23`
- `static/js/features/notes/application/workflows.js:46`
- `static/js/features/notes/index.js:97`
- `static/js/features/notes/index.js:97`

## `_archiveNoteById` — function, line 98
- **called from:**
- `static/js/features/notes/application/workflows.js:37`
- `static/js/features/notes/index.js:98`
- `static/js/features/notes/index.js:98`
- `static/js/features/notes/ui/cardInteractions.js:269`
- `static/js/features/notes/ui/editor.js:406`
- `static/js/features/notes/ui/editor.js:503`

## `_fetchNotes` — function, line 99
- **called from:**
- `static/js/features/notes/application/deletion.js:16`
- `static/js/features/notes/application/deletion.js:31`
- `static/js/features/notes/application/deletion.js:47`
- `static/js/features/notes/application/reminders.js:161`
- `static/js/features/notes/application/workflows.js:58`
- `static/js/features/notes/index.js:73`
- `static/js/features/notes/index.js:99`
- `static/js/features/notes/index.js:99`
- `static/js/features/notes/ui/mobileEditor.js:233`
- `static/js/features/notes/ui/panel.js:312`
- `static/js/features/notes/ui/panel.js:403`
- `static/js/features/notes/ui/panel.js:406`
- `static/js/features/notes/ui/toolbar.js:47`

## `_deleteNoteApi` — function, line 101
- **called from:**
- `static/js/features/notes/application/deletion.js:16`
- `static/js/features/notes/application/deletion.js:30`
- `static/js/features/notes/application/deletion.js:45`
- `static/js/features/notes/application/workflows.js:75`
- `static/js/features/notes/index.js:101`
- `static/js/features/notes/index.js:101`

## `_patchNote` — function, line 102
- **called from:**
- `static/js/features/notes/application/agentActions.js:40`
- `static/js/features/notes/application/reminders.js:46`
- `static/js/features/notes/application/reminders.js:59`
- `static/js/features/notes/application/workflows.js:28`
- `static/js/features/notes/application/workflows.js:48`
- `static/js/features/notes/index.js:102`
- `static/js/features/notes/index.js:102`

## `_uid` — function, line 103
- **called from:**
- `src/fixture_email.py:70`
- `src/fixture_email.py:154`
- `src/fixture_email.py:205`
- `static/js/features/notes/index.js:103`
- `static/js/features/notes/ui/checklist.js:53`
- `static/js/features/notes/ui/checklist.js:136`
- `static/js/features/notes/ui/checklist.js:180`
- `static/js/features/notes/ui/editor.js:36`
- `static/js/features/notes/ui/editor.js:166`
- `static/js/features/notes/ui/editor.js:166`
- `static/js/features/notes/ui/editor.js:168`
- `static/js/features/notes/ui/mobileEditor.js:176`

## `_formatDueDate` — function, line 104
- **called from:**
- `static/js/features/notes/domain/recurrence.js:8`
- `static/js/features/notes/index.js:104`
- `static/js/features/notes/index.js:104`
- `static/js/features/notes/ui/cardRendering.js:98`

## `_isDueOverdue` — function, line 105
- **called from:**
- `static/js/features/notes/domain/recurrence.js:26`
- `static/js/features/notes/index.js:105`
- `static/js/features/notes/index.js:105`
- `static/js/features/notes/ui/cardRendering.js:99`

## `_laterTodayDate` — function, line 107
- **called from:**
- `static/js/features/notes/domain/recurrence.js:43`
- `static/js/features/notes/index.js:107`
- `static/js/features/notes/index.js:107`
- `static/js/features/notes/ui/reminderPicker.js:53`
- `static/js/features/notes/ui/reminderPicker.js:53`

## `_tomorrowDate` — function, line 108
- **called from:**
- `static/js/features/notes/domain/recurrence.js:51`
- `static/js/features/notes/index.js:108`
- `static/js/features/notes/index.js:108`
- `static/js/features/notes/ui/reminderPicker.js:54`
- `static/js/features/notes/ui/reminderPicker.js:54`
- `static/js/features/notes/ui/reminderPicker.js:289`

## `_nextWeekDate` — function, line 109
- **called from:**
- `static/js/features/notes/domain/recurrence.js:58`
- `static/js/features/notes/index.js:109`
- `static/js/features/notes/index.js:109`
- `static/js/features/notes/ui/reminderPicker.js:55`
- `static/js/features/notes/ui/reminderPicker.js:55`
- `static/js/features/notes/ui/reminderPicker.js:55`

## `_formatReminderTag` — function, line 110
- **called from:**
- `static/js/features/notes/domain/recurrence.js:72`
- `static/js/features/notes/index.js:110`
- `static/js/features/notes/index.js:110`
- `static/js/features/notes/ui/cardRendering.js:146`
- `static/js/features/notes/ui/reminderPicker.js:27`

## `_snapToRepeat` — function, line 111
- **called from:**
- `static/js/features/notes/domain/recurrence.js:114`
- `static/js/features/notes/index.js:111`
- `static/js/features/notes/index.js:111`
- `static/js/features/notes/ui/reminderPicker.js:87`

## `_ensureNotificationPermission` — function, line 112
- **called from:**
- `static/js/features/notes/index.js:112`
- `static/js/features/notes/ui/reminderPicker.js:281`

## `_startReminderLoop` — function, line 114
- **called from:**
- `static/js/features/notes/application/reminders.js:125`
- `static/js/features/notes/application/reminders.js:174`
- `static/js/features/notes/index.js:114`
- `static/js/features/notes/index.js:114`
- `static/js/features/notes/ui/panel.js:313`
- `static/js/features/notes/ui/panel.js:316`

## `_countFiredReminders` — function, line 116
- **called from:**
- `static/js/features/notes/application/reminders.js:135`
- `static/js/features/notes/index.js:116`
- `static/js/features/notes/index.js:116`
- `static/js/features/notes/ui/reminderDisplay.js:77`

## `_hasActiveReminder` — function, line 118
- **called from:**
- `static/js/features/notes/application/queries.js:48`
- `static/js/features/notes/application/queries.js:49`
- `static/js/features/notes/domain/noteRules.js:7`
- `static/js/features/notes/index.js:118`
- `static/js/features/notes/index.js:118`
- `static/js/features/notes/ui/cardRendering.js:153`
- `static/js/features/notes/ui/reminderDisplay.js:53`

## `_isPastReminder` — function, line 121
- **called from:**
- `static/js/features/notes/application/deletion.js:21`
- `static/js/features/notes/domain/noteRules.js:50`
- `static/js/features/notes/index.js:121`
- `static/js/features/notes/index.js:121`
- `static/js/features/notes/ui/filters.js:29`

## `_esc` — function, line 122
- **called from:**
- `tests/test_ics_escape.py:12`
- `tests/test_ics_escape.py:16`
- `tests/test_ics_escape.py:20`
- `tests/test_ics_escape.py:24`
- `tests/test_ics_escape.py:25`
- `static/js/assistant.js:115`
- `static/js/assistant.js:144`
- `static/js/assistant.js:144`
- `static/js/assistant.js:147`
- `static/js/assistant.js:150`
- `static/js/assistant.js:151`
- `static/js/assistant.js:154`
- `static/js/assistant.js:156`
- `static/js/assistant.js:157`
- `static/js/assistant.js:165`
- `static/js/assistant.js:169`
- `static/js/assistant.js:169`
- `static/js/assistant.js:178`
- `static/js/assistant.js:186`
- `static/js/assistant.js:207`
- `static/js/assistant.js:207`
- `static/js/assistant.js:241`
- `static/js/assistant.js:241`
- `static/js/assistant.js:257`
- `static/js/assistant.js:257`
- `static/js/assistant.js:302`
- `static/js/assistant.js:302`
- `static/js/assistant.js:311`
- `static/js/assistant.js:311`
- `static/js/chat.js:6293`
- `static/js/chat.js:6293`
- `static/js/cookbookServe.js:4108`
- `static/js/cookbookServe.js:4110`
- `static/js/document.js:1225`
- `static/js/document.js:1226`
- `static/js/document.js:13760`
- `static/js/document.js:14380`
- `static/js/document.js:15402`
- `static/js/documentLibrary.js:169`
- `static/js/documentLibrary.js:185`
- `static/js/documentLibrary.js:705`
- `static/js/documentLibrary.js:709`
- `static/js/documentLibrary.js:711`
- `static/js/documentLibrary.js:2218`
- `static/js/documentLibrary.js:2223`
- `static/js/documentLibrary.js:2371`
- `static/js/documentLibrary.js:2735`
- `static/js/documentLibrary.js:2780`
- `static/js/documentLibrary.js:2818`
- `static/js/documentLibrary.js:2968`
- `static/js/documentLibrary.js:3017`
- `static/js/documentLibrary.js:3030`
- `static/js/documentLibrary.js:3184`
- `static/js/emailInbox.js:76`
- `static/js/emailInbox.js:76`
- `static/js/emailInbox.js:76`
- `static/js/emailInbox.js:78`
- `static/js/emailInbox.js:78`
- `static/js/emailInbox.js:78`
- `static/js/emailInbox.js:78`
- … +226 more (grep the name in repo)

## `_safeImgSrc` — function, line 124
- **called from:**
- `static/js/features/notes/index.js:124`
- `static/js/features/notes/index.js:124`
- `static/js/features/notes/ui/cardRendering.js:184`
- `static/js/features/notes/ui/cardRendering.js:184`
- `static/js/features/notes/ui/drawing.js:100`
- `static/js/features/notes/ui/editor.js:44`
- `static/js/features/notes/ui/editor.js:126`
- `static/js/features/notes/ui/editor.js:178`
- `static/js/features/notes/ui/editor.js:247`
- `static/js/features/notes/ui/text.js:16`

## `_linkify` — function, line 125
- **called from:**
- `static/js/features/notes/index.js:125`
- `static/js/features/notes/index.js:125`
- `static/js/features/notes/ui/cardRendering.js:84`
- `static/js/features/notes/ui/cardRendering.js:119`
- `static/js/features/notes/ui/cardRendering.js:134`
- `static/js/features/notes/ui/mobileEditor.js:195`
- `static/js/features/notes/ui/mobileEditor.js:245`
- `static/js/features/notes/ui/text.js:24`

## `_isBgImage` — function, line 126
- **called from:**
- `static/js/features/notes/index.js:126`
- `static/js/features/notes/index.js:126`
- `static/js/features/notes/ui/cardInteractions.js:157`
- `static/js/features/notes/ui/cardRendering.js:137`
- `static/js/features/notes/ui/colors.js:29`
- `static/js/features/notes/ui/colors.js:31`
- `static/js/features/notes/ui/colors.js:42`
- `static/js/features/notes/ui/colors.js:47`
- `static/js/features/notes/ui/colors.js:86`
- `static/js/features/notes/ui/editor.js:42`
- `static/js/features/notes/ui/editor.js:43`

## `_dotBg` — function, line 128
- **called from:**
- `static/js/features/notes/index.js:128`
- `static/js/features/notes/index.js:128`
- `static/js/features/notes/ui/cardInteractions.js:164`
- `static/js/features/notes/ui/cardRendering.js:151`
- `static/js/features/notes/ui/colors.js:33`
- `static/js/features/notes/ui/colors.js:93`
- `static/js/features/notes/ui/editor.js:85`

## `_dotIsActive` — function, line 129
- **called from:**
- `static/js/features/notes/index.js:129`
- `static/js/features/notes/index.js:129`
- `static/js/features/notes/ui/cardInteractions.js:163`
- `static/js/features/notes/ui/cardRendering.js:151`
- `static/js/features/notes/ui/colors.js:41`
- `static/js/features/notes/ui/colors.js:92`
- `static/js/features/notes/ui/editor.js:85`

## `_customColorStyle` — function, line 130
- **called from:**
- `static/js/features/notes/index.js:130`
- `static/js/features/notes/index.js:130`
- `static/js/features/notes/ui/cardInteractions.js:160`
- `static/js/features/notes/ui/cardRendering.js:139`
- `static/js/features/notes/ui/colors.js:46`
- `static/js/features/notes/ui/colors.js:89`
- `static/js/features/notes/ui/editor.js:43`

## `_pickCustomBgImage` — function, line 131
- **called from:**
- `static/js/features/notes/index.js:131`
- `static/js/features/notes/index.js:131`
- `static/js/features/notes/ui/cardInteractions.js:174`
- `static/js/features/notes/ui/colors.js:52`
- `static/js/features/notes/ui/colors.js:100`

## `_wireFormColors` — function, line 132
- **called from:**
- `static/js/features/notes/index.js:132`
- `static/js/features/notes/index.js:132`
- `static/js/features/notes/ui/colors.js:80`
- `static/js/features/notes/ui/editor.js:242`

## `openPanel` — function, line 134
- **called from:**
- `static/app.js:1221`
- `static/js/chat.js:9369`
- `static/js/chat.js:9410`
- `static/js/document.js:7387`
- `static/js/document.js:11837`
- `static/js/document.js:12046`
- `static/js/document.js:12099`
- `static/js/document.js:12101`
- `static/js/document.js:12244`
- `static/js/document.js:12258`
- `static/js/document.js:12312`
- `static/js/document.js:12386`
- `static/js/document.js:12426`
- `static/js/document.js:12432`
- `static/js/document.js:13605`
- `static/js/document.js:14703`
- `static/js/document.js:16759`
- `static/js/document.js:17119`
- `static/js/emailInbox.js:1057`
- `static/js/emailInbox.js:1128`
- `static/js/features/notes/index.js:65`
- `static/js/features/notes/index.js:134`
- `static/js/features/notes/index.js:134`
- `static/js/features/notes/infrastructure/notifications.js:14`
- `static/js/features/notes/ui/panel.js:99`
- `static/js/features/notes/ui/panel.js:104`
- `static/js/features/notes/ui/panel.js:382`
- `static/js/features/notes/ui/panel.js:394`
- `static/js/features/notes/ui/panel.js:406`
- `static/js/features/notes/ui/quickAdd.js:109`
- `static/js/research/panel.js:234`
- `static/js/research/panel.js:238`
- `static/js/settings.js:1913`
- `static/js/settings/search.js:75`

## `_smoothScrollToNoteCard` — function, line 136
- **called from:**
- `static/js/features/notes/index.js:136`
- `static/js/features/notes/index.js:136`
- `static/js/features/notes/ui/cardInteractions.js:71`
- `static/js/features/notes/ui/panel.js:414`
- `static/js/features/notes/ui/panel.js:488`
- `static/js/features/notes/ui/reminderDisplay.js:71`

## `_clearViewedReminderGlows` — function, line 137
- **called from:**
- `static/js/features/notes/index.js:137`
- `static/js/features/notes/index.js:137`
- `static/js/features/notes/ui/panel.js:38`
- `static/js/features/notes/ui/panel.js:120`
- `static/js/features/notes/ui/panel.js:325`
- `static/js/features/notes/ui/reminderDisplay.js:16`

## `_setReminderCardGlow` — function, line 138
- **called from:**
- `static/js/features/notes/index.js:78`
- `static/js/features/notes/index.js:138`
- `static/js/features/notes/index.js:138`
- `static/js/features/notes/index.js:495`
- `static/js/features/notes/ui/cardInteractions.js:65`
- `static/js/features/notes/ui/reminderDisplay.js:25`
- `static/js/features/notes/ui/reminderDisplay.js:63`

## `_queuePendingHighlight` — function, line 139
- **called from:**
- `static/js/features/notes/index.js:81`
- `static/js/features/notes/index.js:139`
- `static/js/features/notes/index.js:139`
- `static/js/features/notes/ui/reminderDisplay.js:36`

## `_flushPendingHighlights` — function, line 140
- **called from:**
- `static/js/features/notes/index.js:140`
- `static/js/features/notes/index.js:140`
- `static/js/features/notes/ui/panel.js:315`
- `static/js/features/notes/ui/reminderDisplay.js:42`

## `_updateRailBadge` — function, line 141
- **called from:**
- `static/js/features/notes/application/reminders.js:69`
- `static/js/features/notes/application/reminders.js:151`
- `static/js/features/notes/application/reminders.js:165`
- `static/js/features/notes/index.js:77`
- `static/js/features/notes/index.js:141`
- `static/js/features/notes/index.js:141`
- `static/js/features/notes/ui/cardRendering.js:50`
- `static/js/features/notes/ui/reminderDisplay.js:76`

## `_enterSelectMode` — function, line 142
- **called from:**
- `static/js/features/notes/index.js:142`
- `static/js/features/notes/index.js:142`
- `static/js/features/notes/ui/mobileReorder.js:28`
- `static/js/features/notes/ui/panel.js:237`
- `static/js/features/notes/ui/selection.js:8`
- `static/js/sessions.js:1185`
- `static/js/sessions.js:1940`
- `static/js/sessions.js:1998`
- `static/js/sessions.js:2010`
- `static/js/skills.js:561`
- `static/js/skills.js:1984`
- `static/js/skills.js:2340`

## `_exitSelectMode` — function, line 143
- **called from:**
- `static/js/features/notes/index.js:143`
- `static/js/features/notes/index.js:143`
- `static/js/features/notes/ui/panel.js:237`
- `static/js/features/notes/ui/panel.js:250`
- `static/js/features/notes/ui/panel.js:297`
- `static/js/features/notes/ui/selection.js:20`
- `static/js/gallery.js:2880`
- `static/js/gallery.js:2886`
- `static/js/gallery.js:2903`
- `static/js/gallery.js:3032`
- `static/js/gallery.js:3074`
- `static/js/gallery.js:3112`
- `static/js/gallery.js:3140`
- `static/js/gallery.js:3152`
- `static/js/gallery.js:3170`
- `static/js/sessions.js:1971`
- `static/js/sessions.js:1997`
- `static/js/sessions.js:2002`
- `static/js/sessions.js:2017`
- `static/js/sessions.js:2058`
- `static/js/sessions.js:2079`
- `static/js/skills.js:857`
- `static/js/skills.js:1995`
- `static/js/skills.js:2069`
- `static/js/skills.js:2131`
- `static/js/skills.js:2151`
- `static/js/skills.js:2162`
- `static/js/skills.js:2340`

## `_updateBulkBar` — function, line 144
- **called from:**
- `static/js/emailLibrary/index.js:1021`
- `static/js/emailLibrary/index.js:1373`
- `static/js/emailLibrary/index.js:1737`
- `static/js/emailLibrary/index.js:2933`
- `static/js/emailLibrary/index.js:2942`
- `static/js/emailLibrary/index.js:2953`
- `static/js/emailLibrary/index.js:3007`
- `static/js/emailLibrary/index.js:3077`
- `static/js/emailLibrary/index.js:5474`
- `static/js/emailLibrary/index.js:5787`
- `static/js/emailLibrary/menus.js:506`
- `static/js/emailLibrary/menus.js:655`
- `static/js/emailLibrary/menus.js:666`
- `static/js/emailLibrary/menus.js:706`
- `static/js/emailLibrary/menus.js:896`
- `static/js/features/notes/index.js:144`
- `static/js/features/notes/index.js:144`
- `static/js/features/notes/ui/cardInteractions.js:144`
- `static/js/features/notes/ui/selection.js:17`
- `static/js/features/notes/ui/selection.js:32`
- `static/js/features/notes/ui/selection.js:53`
- `static/js/skills.js:1145`
- `static/js/skills.js:1991`
- `static/js/skills.js:2007`
- `static/js/skills.js:2037`

## `_renderLabelsInto` — function, line 146
- **called from:**
- `static/js/features/notes/index.js:146`
- `static/js/features/notes/index.js:146`
- `static/js/features/notes/ui/cardRendering.js:36`
- `static/js/features/notes/ui/cardRendering.js:65`
- `static/js/features/notes/ui/cardRendering.js:229`
- `static/js/features/notes/ui/filters.js:107`

## `_renderLoadingSkeleton` — function, line 147
- **called from:**
- `static/js/features/notes/index.js:147`
- `static/js/features/notes/index.js:147`
- `static/js/features/notes/ui/cardRendering.js:32`
- `static/js/features/notes/ui/panel.js:308`

## `_renderNotes` — function, line 148
- **called from:**
- `static/js/features/notes/application/agentActions.js:39`
- `static/js/features/notes/application/deletion.js:16`
- `static/js/features/notes/application/deletion.js:32`
- `static/js/features/notes/application/deletion.js:44`
- `static/js/features/notes/application/deletion.js:47`
- `static/js/features/notes/application/workflows.js:27`
- `static/js/features/notes/application/workflows.js:32`
- `static/js/features/notes/application/workflows.js:45`
- `static/js/features/notes/application/workflows.js:52`
- `static/js/features/notes/index.js:88`
- `static/js/features/notes/index.js:148`
- `static/js/features/notes/index.js:148`
- `static/js/features/notes/ui/cardChecklist.js:52`
- `static/js/features/notes/ui/cardChecklist.js:141`
- `static/js/features/notes/ui/cardInteractions.js:213`
- `static/js/features/notes/ui/cardRendering.js:49`
- `static/js/features/notes/ui/editor.js:498`
- `static/js/features/notes/ui/filters.js:102`
- `static/js/features/notes/ui/filters.js:119`
- `static/js/features/notes/ui/panel.js:314`
- `static/js/features/notes/ui/panel.js:404`
- `static/js/features/notes/ui/selection.js:16`
- `static/js/features/notes/ui/selection.js:29`
- `static/js/features/notes/ui/selection.js:53`
- `static/js/features/notes/ui/toolbar.js:16`
- `static/js/features/notes/ui/toolbar.js:48`

## `_captureCardPositions` — function, line 149
- **called from:**
- `static/js/features/notes/index.js:149`
- `static/js/features/notes/index.js:149`
- `static/js/features/notes/ui/cardRendering.js:53`
- `static/js/features/notes/ui/layout.js:3`

## `_animateReflow` — function, line 150
- **called from:**
- `static/js/features/notes/index.js:150`
- `static/js/features/notes/index.js:150`
- `static/js/features/notes/ui/cardRendering.js:239`
- `static/js/features/notes/ui/layout.js:14`

## `_applyMasonry` — function, line 151
- **called from:**
- `static/js/features/notes/index.js:151`
- `static/js/features/notes/index.js:151`
- `static/js/features/notes/ui/cardRendering.js:240`
- `static/js/features/notes/ui/editor.js:130`
- `static/js/features/notes/ui/editor.js:132`
- `static/js/features/notes/ui/editor.js:133`
- `static/js/features/notes/ui/layout.js:40`
- `static/js/features/notes/ui/mobileReorder.js:183`
- `static/js/features/notes/ui/quickAdd.js:70`
- `static/js/features/notes/ui/quickAdd.js:71`
- `static/js/features/notes/ui/quickAdd.js:139`
- `static/js/features/notes/ui/quickAdd.js:140`
- `static/js/features/notes/ui/toolbar.js:66`
- `static/js/features/notes/ui/toolbar.js:72`

## `_renderQuickAdd` — function, line 152
- **called from:**
- `static/js/features/notes/index.js:152`
- `static/js/features/notes/index.js:152`
- `static/js/features/notes/ui/cardRendering.js:37`
- `static/js/features/notes/ui/cardRendering.js:66`
- `static/js/features/notes/ui/cardRendering.js:230`
- `static/js/features/notes/ui/quickAdd.js:11`

## `_editNote` — function, line 154
- **called from:**
- `static/js/features/notes/index.js:154`
- `static/js/features/notes/index.js:154`
- `static/js/features/notes/ui/cardChecklist.js:142`
- `static/js/features/notes/ui/cardInteractions.js:55`
- `static/js/features/notes/ui/cardInteractions.js:187`
- `static/js/features/notes/ui/quickAdd.js:113`

## `_bindCardEvents` — function, line 155
- **called from:**
- `static/js/features/notes/index.js:155`
- `static/js/features/notes/index.js:155`
- `static/js/features/notes/ui/cardInteractions.js:27`
- `static/js/features/notes/ui/cardRendering.js:238`

## `_wireCardChecklist` — function, line 156
- **called from:**
- `static/js/features/notes/index.js:156`
- `static/js/features/notes/index.js:156`
- `static/js/features/notes/ui/cardChecklist.js:10`
- `static/js/features/notes/ui/cardInteractions.js:331`

## `_wireTodayView` — function, line 157
- **called from:**
- `static/js/features/notes/index.js:157`
- `static/js/features/notes/index.js:157`
- `static/js/features/notes/ui/cardChecklist.js:120`
- `static/js/features/notes/ui/cardRendering.js:92`

## `_wireCardReorder` — function, line 158
- **called from:**
- `static/js/features/notes/index.js:158`
- `static/js/features/notes/index.js:158`
- `static/js/features/notes/ui/cardInteractions.js:332`
- `static/js/features/notes/ui/cardReorder.js:8`

## `_wireDraftAutosave` — function, line 160
- **called from:**
- `static/js/features/notes/index.js:160`
- `static/js/features/notes/index.js:160`
- `static/js/features/notes/ui/draftEditor.js:33`
- `static/js/features/notes/ui/editor.js:512`

## `_commitOpenInPlaceEditor` — function, line 161
- **called from:**
- `static/js/features/notes/index.js:161`
- `static/js/features/notes/index.js:161`
- `static/js/features/notes/ui/draftEditor.js:48`
- `static/js/features/notes/ui/panel.js:36`
- `static/js/features/notes/ui/panel.js:351`

## `_applyDraftToNote` — function, line 162
- **called from:**
- `static/js/features/notes/index.js:162`
- `static/js/features/notes/index.js:162`
- `static/js/features/notes/ui/draftEditor.js:56`
- `static/js/features/notes/ui/mobileEditor.js:45`
- `static/js/features/notes/ui/quickAdd.js:97`
- `static/js/features/notes/ui/quickAdd.js:121`

## `_buildForm` — function, line 163
- **called from:**
- `static/js/features/notes/index.js:163`
- `static/js/features/notes/index.js:163`
- `static/js/features/notes/ui/editor.js:32`
- `static/js/features/notes/ui/mobileEditor.js:46`
- `static/js/features/notes/ui/quickAdd.js:57`
- `static/js/features/notes/ui/quickAdd.js:98`
- `static/js/features/notes/ui/quickAdd.js:122`

## `_wireReminderPicker` — function, line 164
- **called from:**
- `static/js/features/notes/index.js:164`
- `static/js/features/notes/index.js:164`
- `static/js/features/notes/ui/editor.js:276`
- `static/js/features/notes/ui/reminderPicker.js:15`

## `_buildGoalHtml` — function, line 165
- **called from:**
- `static/js/features/notes/index.js:165`
- `static/js/features/notes/index.js:165`
- `static/js/features/notes/ui/checklist.js:7`
- `static/js/features/notes/ui/editor.js:61`

## `_wireGoalForm` — function, line 166
- **called from:**
- `static/js/features/notes/index.js:166`
- `static/js/features/notes/index.js:166`
- `static/js/features/notes/ui/checklist.js:17`
- `static/js/features/notes/ui/editor.js:245`

## `_buildChecklistHtml` — function, line 167
- **called from:**
- `static/js/features/notes/index.js:167`
- `static/js/features/notes/index.js:167`
- `static/js/features/notes/ui/checklist.js:12`
- `static/js/features/notes/ui/checklist.js:49`
- `static/js/features/notes/ui/editor.js:62`
- `static/js/features/notes/ui/editor.js:170`

## `_wireRow` — function, line 168
- **called from:**
- `static/js/features/notes/index.js:168`
- `static/js/features/notes/index.js:168`
- `static/js/features/notes/ui/checklist.js:67`
- `static/js/features/notes/ui/checklist.js:141`
- `static/js/features/notes/ui/checklist.js:144`
- `static/js/features/notes/ui/mobileEditor.js:180`

## `_wireChecklist` — function, line 169
- **called from:**
- `static/js/features/notes/index.js:169`
- `static/js/features/notes/index.js:169`
- `static/js/features/notes/ui/checklist.js:46`
- `static/js/features/notes/ui/checklist.js:118`
- `static/js/features/notes/ui/editor.js:171`
- `static/js/features/notes/ui/editor.js:244`

## `_collectItems` — function, line 170
- **called from:**
- `static/js/features/notes/index.js:170`
- `static/js/features/notes/index.js:170`
- `static/js/features/notes/ui/checklist.js:175`
- `static/js/features/notes/ui/draftEditor.js:20`
- `static/js/features/notes/ui/draftEditor.js:21`
- `static/js/features/notes/ui/editor.js:148`
- `static/js/features/notes/ui/editor.js:151`
- `static/js/features/notes/ui/editor.js:445`
- `static/js/features/notes/ui/editor.js:447`

## `_buildDrawHtml` — function, line 171
- **called from:**
- `static/js/features/notes/index.js:171`
- `static/js/features/notes/index.js:171`
- `static/js/features/notes/ui/drawing.js:8`
- `static/js/features/notes/ui/editor.js:59`
- `static/js/features/notes/ui/editor.js:173`

## `_wireCanvas` — function, line 172
- **called from:**
- `static/js/features/notes/index.js:172`
- `static/js/features/notes/index.js:172`
- `static/js/features/notes/ui/drawing.js:42`
- `static/js/features/notes/ui/editor.js:178`
- `static/js/features/notes/ui/editor.js:247`

## `_uploadCanvasAsPng` — function, line 173
- **called from:**
- `static/js/features/notes/index.js:173`
- `static/js/features/notes/index.js:173`
- `static/js/features/notes/ui/drawing.js:423`
- `static/js/features/notes/ui/editor.js:437`

## `_openNoteCornerMenu` — function, line 174
- **called from:**
- `static/js/features/notes/index.js:174`
- `static/js/features/notes/index.js:174`
- `static/js/features/notes/ui/cardInteractions.js:198`
- `static/js/features/notes/ui/clipboard.js:11`

## `_copyNote` — function, line 175
- **called from:**
- `static/js/features/notes/index.js:175`
- `static/js/features/notes/index.js:175`
- `static/js/features/notes/ui/clipboard.js:40`
- `static/js/features/notes/ui/clipboard.js:44`
- `static/js/features/notes/ui/panel.js:292`

## `_isNotesMobileMode` — function, line 176
- **called from:**
- `static/js/features/notes/index.js:176`
- `static/js/features/notes/index.js:176`
- `static/js/features/notes/ui/cardInteractions.js:50`
- `static/js/features/notes/ui/cardInteractions.js:61`
- `static/js/features/notes/ui/cardInteractions.js:126`
- `static/js/features/notes/ui/cardRendering.js:161`
- `static/js/features/notes/ui/cardReorder.js:13`
- `static/js/features/notes/ui/cardReorder.js:80`
- `static/js/features/notes/ui/mobileEditor.js:15`
- `static/js/features/notes/ui/panel.js:140`

## `_openMobileFullscreenEdit` — function, line 177
- **called from:**
- `static/js/features/notes/index.js:177`
- `static/js/features/notes/index.js:177`
- `static/js/features/notes/ui/cardInteractions.js:53`
- `static/js/features/notes/ui/mobileEditor.js:23`

## `_closeMobileFullscreenEdit` — function, line 178
- **called from:**
- `static/js/features/notes/index.js:178`
- `static/js/features/notes/index.js:178`
- `static/js/features/notes/ui/mobileEditor.js:27`
- `static/js/features/notes/ui/mobileEditor.js:69`
- `static/js/features/notes/ui/mobileEditor.js:83`
- `static/js/features/notes/ui/mobileEditor.js:93`
- `static/js/features/notes/ui/mobileEditor.js:123`
- `static/js/features/notes/ui/mobileEditor.js:130`
- `static/js/features/notes/ui/mobileEditor.js:215`
- `static/js/features/notes/ui/panel.js:37`
- `static/js/features/notes/ui/panel.js:352`

## `_bindLongPressDrag` — function, line 180
- **called from:**
- `static/js/features/notes/index.js:180`
- `static/js/features/notes/index.js:180`
- `static/js/features/notes/ui/cardInteractions.js:62`
- `static/js/features/notes/ui/mobileReorder.js:9`

## `_wireChecklistTouchReorder` — function, line 182
- **called from:**
- `static/js/features/notes/index.js:182`
- `static/js/features/notes/index.js:182`
- `static/js/features/notes/ui/checklistReorder.js:10`
- `static/js/features/notes/ui/mobileEditor.js:100`
- `static/js/features/notes/ui/mobileEditor.js:182`

## `_sortedVisibleNotes` — function, line 184
- **called from:**
- `static/js/features/notes/application/queries.js:8`
- `static/js/features/notes/index.js:184`
- `static/js/features/notes/index.js:184`
- `static/js/features/notes/ui/cardRendering.js:56`

## `_userVisibleNotes` — function, line 185
- **called from:**
- `static/js/features/notes/application/queries.js:9`
- `static/js/features/notes/application/queries.js:61`
- `static/js/features/notes/index.js:185`
- `static/js/features/notes/index.js:185`
- `static/js/features/notes/ui/filters.js:23`

## `_agentSolveNote` — function, line 186
- **called from:**
- `static/js/features/notes/application/agentActions.js:13`
- `static/js/features/notes/index.js:186`
- `static/js/features/notes/index.js:186`
- `static/js/features/notes/ui/clipboard.js:41`

## `_clearPastReminders` — function, line 188
- **called from:**
- `static/js/features/notes/application/deletion.js:20`
- `static/js/features/notes/index.js:188`
- `static/js/features/notes/index.js:188`
- `static/js/features/notes/ui/filters.js:96`

## `startNotesBackground` — function, line 486
- **called from:**
- `static/js/features/notes/index.js:486`
- `static/js/notes.js:5`
