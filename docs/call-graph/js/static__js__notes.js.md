# `static/js/notes.js` — definitions & call sites

209 definitions (regex-based, best-effort).
**Exports:** `closeNotes`, `closePanel`, `default`, `dismissFiredReminderDot`, `isNotesOpen`, `isPanelOpen`, `openNote`, `openNotes`, `openPanel`, `refreshDueBadge`, `togglePanel`

## `_forceCloseNotesPanel` — function, line 52
- **called from:**
- `static/js/notes.js:52`
- `static/js/notes.js:1422`
- `static/js/notes.js:1624`

## `_showNotesFirstOpenHint` — function, line 78
- **called from:**
- `static/js/notes.js:78`
- `static/js/notes.js:1435`

## `place` — arrow, line 97
- **called from:**
- `static/js/chat.js:5556`
- `static/js/editor/state.js:220`
- `static/js/notes.js:110`

## `close` — arrow, line 103
- **called from:**
- `app.py:333`
- `app.py:451`
- `app.py:532`
- `app.py:1050`
- `app.py:1174`
- `app.py:1295`
- `companion/pairing.py:151`
- `companion/routes.py:165`
- `core/database.py:161`
- `core/database.py:923`
- `core/database.py:946`
- `core/database.py:971`
- `core/database.py:994`
- `core/database.py:1017`
- `core/database.py:1048`
- `core/database.py:1073`
- `core/database.py:1097`
- `core/database.py:1125`
- `core/database.py:1148`
- `core/database.py:1171`
- `core/database.py:1194`
- `core/database.py:1217`
- `core/database.py:1249`
- `core/database.py:1272`
- `core/database.py:1295`
- `core/database.py:1319`
- `core/database.py:1343`
- `core/database.py:1377`
- `core/database.py:1406`
- `core/database.py:1479`
- `core/database.py:2068`
- `core/database.py:2301`
- `core/database.py:2363`
- `core/database.py:2479`
- `core/database.py:2506`
- `core/database.py:2532`
- `core/database.py:2557`
- `core/database.py:2584`
- `core/database.py:2606`
- `core/database.py:2619`
- `core/database.py:2635`
- `core/session_manager.py:68`
- `core/session_manager.py:177`
- `core/session_manager.py:428`
- `core/session_manager.py:568`
- `core/session_manager.py:603`
- `core/session_manager.py:651`
- `core/session_manager.py:771`
- `core/session_manager.py:858`
- `core/session_manager.py:885`
- `core/session_manager.py:899`
- `core/session_manager.py:945`
- `core/session_manager.py:989`
- `core/session_manager.py:1013`
- `core/session_manager.py:1033`
- `core/session_manager.py:1054`
- `core/session_manager.py:1140`
- `mcp_servers/email_server.py:220`
- `mcp_servers/email_server.py:815`
- `mcp_servers/email_server.py:1351`
- … +754 more (grep the name in repo)

## `_notesFullscreenSafeRect` — function, line 118
- **called from:**
- `static/js/notes.js:118`
- `static/js/notes.js:172`

## `reserve` — arrow, line 130
- **called from:**
- `static/js/notes.js:138`
- `static/js/notes.js:139`

## `_wireNotesWindow` — function, line 156
- **called from:**
- `static/js/notes.js:156`
- `static/js/notes.js:1241`

## `_clearNotesSnapStyles` — function, line 181
- **called from:**
- `static/js/notes.js:181`
- `static/js/notes.js:200`

## `_restoreNotesSidebarDock` — function, line 198
- **called from:**
- `static/js/notes.js:176`
- `static/js/notes.js:198`
- `static/js/notes.js:1242`

## `_topToolWindowZ` — function, line 206
- **called from:**
- `static/js/notes.js:206`
- `static/js/notes.js:213`

## `_bringNotesToFront` — function, line 210
- **called from:**
- `static/js/notes.js:210`
- `static/js/notes.js:1147`
- `static/js/notes.js:1243`
- `static/js/notes.js:1254`
- `static/js/notes.js:1255`
- `static/js/notes.js:5325`

## `_loadPendingHighlights` — function, line 222
- **called from:**
- `static/js/notes.js:222`
- `static/js/notes.js:272`
- `static/js/notes.js:280`

## `_loadGlowedReminders` — function, line 226
- **called from:**
- `static/js/notes.js:226`
- `static/js/notes.js:281`
- `static/js/notes.js:3675`

## `_saveGlowedReminders` — function, line 230
- **called from:**
- `static/js/notes.js:230`
- `static/js/notes.js:301`
- `static/js/notes.js:3677`

## `_loadActiveHighlights` — function, line 233
- **called from:**
- `static/js/notes.js:233`
- `static/js/notes.js:241`
- `static/js/notes.js:250`
- `static/js/notes.js:1745`

## `_saveActiveHighlights` — function, line 237
- **called from:**
- `static/js/notes.js:237`
- `static/js/notes.js:243`
- `static/js/notes.js:253`

## `_clearViewedReminderGlows` — function, line 240
- **called from:**
- `static/js/notes.js:57`
- `static/js/notes.js:240`
- `static/js/notes.js:1153`
- `static/js/notes.js:1635`

## `_setReminderCardGlow` — function, line 248
- **called from:**
- `static/js/notes.js:248`
- `static/js/notes.js:297`
- `static/js/notes.js:1032`
- `static/js/notes.js:2203`
- `static/js/notes.js:3678`

## `_hasActiveReminder` — function, line 261
- **called from:**
- `static/js/notes.js:261`
- `static/js/notes.js:287`
- `static/js/notes.js:1785`
- `static/js/notes.js:1786`
- `static/js/notes.js:1897`

## `_savePendingHighlights` — function, line 267
- **called from:**
- `static/js/notes.js:267`
- `static/js/notes.js:274`
- `static/js/notes.js:291`

## `_queuePendingHighlight` — function, line 271
- **called from:**
- `static/js/notes.js:271`
- `static/js/notes.js:1038`

## `_flushPendingHighlights` — function, line 276
- **called from:**
- `static/js/notes.js:276`
- `static/js/notes.js:1433`

## `_isBgImage` — function, line 326
- **called from:**
- `static/js/notes.js:326`
- `static/js/notes.js:327`
- `static/js/notes.js:338`
- `static/js/notes.js:344`
- `static/js/notes.js:1883`
- `static/js/notes.js:2291`
- `static/js/notes.js:2929`
- `static/js/notes.js:2930`
- `static/js/notes.js:3133`

## `_bgImageUrl` — function, line 327
- **called from:**
- `static/js/notes.js:327`
- `static/js/notes.js:331`
- `static/js/notes.js:345`

## `_dotBg` — function, line 329
- **called from:**
- `static/js/notes.js:329`
- `static/js/notes.js:1895`
- `static/js/notes.js:2298`
- `static/js/notes.js:2972`
- `static/js/notes.js:3140`

## `_dotIsActive` — function, line 337
- **called from:**
- `static/js/notes.js:337`
- `static/js/notes.js:1895`
- `static/js/notes.js:2297`
- `static/js/notes.js:2972`
- `static/js/notes.js:3139`

## `_customColorStyle` — function, line 343
- **called from:**
- `static/js/notes.js:343`
- `static/js/notes.js:1885`
- `static/js/notes.js:2294`
- `static/js/notes.js:2930`
- `static/js/notes.js:3136`

## `_pickCustomBgImage` — function, line 350
- **called from:**
- `static/js/notes.js:350`
- `static/js/notes.js:2309`
- `static/js/notes.js:3147`

## `finish` — arrow, line 358
- **called from:**
- `src/pdf_forms.py:338`
- `static/js/calendar.js:34`
- `static/js/calendar.js:42`
- `static/js/calendar.js:43`
- `static/js/calendar.js:45`
- `static/js/chat.js:1226`
- `static/js/fileHandler.js:92`
- `static/js/fileHandler.js:129`
- `static/js/fileHandler.js:130`
- `static/js/fileHandler.js:144`
- `static/js/fileHandler.js:147`
- `static/js/gallery.js:2191`
- `static/js/gallery.js:2194`
- `static/js/notes.js:361`
- `static/js/notes.js:369`
- `static/js/notes.js:370`
- `static/js/notes.js:373`
- `static/js/notes.js:2381`
- `static/js/notes.js:2385`

## `_pushUndo` — function, line 396
- **called from:**
- `static/js/notes.js:396`
- `static/js/notes.js:436`
- `static/js/notes.js:2366`

## `_popAndRunUndo` — function, line 400
- **called from:**
- `static/js/notes.js:400`
- `static/js/notes.js:1394`

## `_undoArchive` — function, line 406
- **called from:**
- `static/js/notes.js:406`
- `static/js/notes.js:435`
- `static/js/notes.js:2365`

## `_archiveNoteById` — function, line 420
- **called from:**
- `static/js/notes.js:420`
- `static/js/notes.js:2432`
- `static/js/notes.js:3628`
- `static/js/notes.js:3753`

## `undo` — arrow, line 435
- **called from:**
- `tests/test_db_stubs_helper.py:67`
- `tests/test_db_stubs_helper.py:82`
- `tests/test_db_stubs_helper.py:99`
- `tests/test_db_stubs_helper.py:118`
- `tests/test_review_regressions.py:1297`
- `static/js/editor/history-panel.js:29`
- `static/js/editor/keyboard-shortcuts.js:10`
- `static/js/editor/keyboard-shortcuts.js:88`
- `static/js/editor/tools/transform-session.js:9`
- `static/js/editor/tools/transform-session.js:370`
- `static/js/galleryEditor.js:1352`
- `static/js/signature.js:261`
- `static/js/signature.js:429`

## `_fetchNotes` — function, line 447
- **called from:**
- `static/js/notes.js:447`
- `static/js/notes.js:1136`
- `static/js/notes.js:1299`
- `static/js/notes.js:1357`
- `static/js/notes.js:1370`
- `static/js/notes.js:1431`
- `static/js/notes.js:1523`
- `static/js/notes.js:3716`
- `static/js/notes.js:3770`
- `static/js/notes.js:4720`
- `static/js/notes.js:4954`
- `static/js/notes.js:5332`
- `static/js/notes.js:5335`

## `_saveNote` — function, line 463
- **called from:**
- `static/js/notes.js:463`
- `static/js/notes.js:3704`

## `_deleteNoteApi` — function, line 475
- **called from:**
- `static/js/notes.js:475`
- `static/js/notes.js:1368`
- `static/js/notes.js:1522`
- `static/js/notes.js:2414`
- `static/js/notes.js:2468`
- `static/js/notes.js:3768`
- `static/js/notes.js:4720`

## `_patchNote` — function, line 482
- **called from:**
- `static/js/notes.js:411`
- `static/js/notes.js:437`
- `static/js/notes.js:482`
- `static/js/notes.js:943`
- `static/js/notes.js:956`
- `static/js/notes.js:1355`
- `static/js/notes.js:2070`
- `static/js/notes.js:2281`
- `static/js/notes.js:2300`
- `static/js/notes.js:2370`
- `static/js/notes.js:2398`
- `static/js/notes.js:2452`
- `static/js/notes.js:2522`
- `static/js/notes.js:2564`
- `static/js/notes.js:2643`
- `static/js/notes.js:2671`
- `static/js/notes.js:4514`
- `static/js/notes.js:4588`
- `static/js/notes.js:4611`

## `_esc` — function, line 494
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
- `static/js/chat.js:4679`
- `static/js/chat.js:4679`
- `static/js/cookbookServe.js:4003`
- `static/js/cookbookServe.js:4005`
- `static/js/document.js:313`
- `static/js/document.js:314`
- `static/js/document.js:8382`
- `static/js/document.js:8966`
- `static/js/documentLibrary.js:70`
- `static/js/documentLibrary.js:86`
- `static/js/documentLibrary.js:582`
- `static/js/documentLibrary.js:586`
- `static/js/documentLibrary.js:588`
- `static/js/documentLibrary.js:1957`
- `static/js/documentLibrary.js:1962`
- `static/js/documentLibrary.js:2110`
- `static/js/documentLibrary.js:2466`
- `static/js/documentLibrary.js:2510`
- `static/js/documentLibrary.js:2547`
- `static/js/documentLibrary.js:2696`
- `static/js/documentLibrary.js:2737`
- `static/js/documentLibrary.js:2750`
- `static/js/documentLibrary.js:2904`
- `static/js/emailInbox.js:75`
- `static/js/emailInbox.js:75`
- `static/js/emailInbox.js:75`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:524`
- … +188 more (grep the name in repo)

## `_attrEsc` — function, line 495
- **called from:**
- `static/js/emailLibrary/utils.js:52`
- `static/js/emailLibrary/utils.js:83`
- `static/js/emailLibrary/utils.js:85`
- `static/js/notes.js:495`
- `static/js/notes.js:527`
- `static/js/notes.js:1857`
- `static/js/notes.js:1863`
- `static/js/notes.js:1863`
- `static/js/notes.js:1863`

## `_safeImgSrc` — function, line 506
- **called from:**
- `static/js/notes.js:506`
- `static/js/notes.js:1927`
- `static/js/notes.js:1927`
- `static/js/notes.js:2931`
- `static/js/notes.js:3013`
- `static/js/notes.js:3065`
- `static/js/notes.js:3157`
- `static/js/notes.js:4031`

## `_linkify` — function, line 517
- **called from:**
- `static/js/notes.js:517`
- `static/js/notes.js:1820`
- `static/js/notes.js:1862`
- `static/js/notes.js:1880`
- `static/js/notes.js:4917`
- `static/js/notes.js:5162`

## `_uid` — function, line 530
- **called from:**
- `static/js/notes.js:530`
- `static/js/notes.js:2634`
- `static/js/notes.js:2924`
- `static/js/notes.js:3053`
- `static/js/notes.js:3053`
- `static/js/notes.js:3055`
- `static/js/notes.js:3700`
- `static/js/notes.js:3831`
- `static/js/notes.js:3911`
- `static/js/notes.js:3955`
- `static/js/notes.js:4898`

## `_wireNotesSwipeDismiss` — function, line 535
- **called from:**
- `static/js/notes.js:535`
- `static/js/notes.js:1251`
- `static/js/notes.js:1252`

## `endSwipe` — arrow, line 570
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_hasTimeComponent` — function, line 591
- **called from:**
- `static/js/notes.js:287`
- `static/js/notes.js:591`
- `static/js/notes.js:600`
- `static/js/notes.js:617`
- `static/js/notes.js:932`
- `static/js/notes.js:1065`
- `static/js/notes.js:1120`
- `static/js/notes.js:1498`
- `static/js/notes.js:1507`
- `static/js/notes.js:1535`
- `static/js/notes.js:1749`
- `static/js/notes.js:1751`
- `static/js/notes.js:1887`
- `static/js/notes.js:1894`

## `_formatDueDate` — function, line 595
- **called from:**
- `static/js/notes.js:595`
- `static/js/notes.js:1834`

## `_isDueOverdue` — function, line 613
- **called from:**
- `static/js/notes.js:613`
- `static/js/notes.js:1835`

## `_isDueTodayOrOverdue` — function, line 621
- **called from:**
- `static/js/notes.js:621`
- `static/js/notes.js:1049`

## `_isNoteFullyDone` — function, line 630
- **called from:**
- `static/js/notes.js:262`
- `static/js/notes.js:630`
- `static/js/notes.js:1049`
- `static/js/notes.js:1064`
- `static/js/notes.js:1116`

## `_hasItems` — function, line 639
- **called from:**
- `static/js/notes.js:425`
- `static/js/notes.js:631`
- `static/js/notes.js:639`
- `static/js/notes.js:975`
- `static/js/notes.js:1838`
- `static/js/notes.js:1920`
- `static/js/notes.js:1929`
- `static/js/notes.js:1942`

## `_goalProgress` — function, line 645
- **called from:**
- `static/js/notes.js:645`
- `static/js/notes.js:1815`
- `static/js/notes.js:1901`

## `_nextGoalStep` — function, line 652
- **called from:**
- `static/js/notes.js:652`
- `static/js/notes.js:1541`
- `static/js/notes.js:1758`
- `static/js/notes.js:1813`

## `_laterTodayDate` — function, line 662
- **called from:**
- `static/js/notes.js:662`
- `static/js/notes.js:3223`
- `static/js/notes.js:3223`

## `_tomorrowDate` — function, line 669
- **called from:**
- `static/js/notes.js:669`
- `static/js/notes.js:3224`
- `static/js/notes.js:3224`
- `static/js/notes.js:3459`

## `_nextWeekDate` — function, line 675
- **called from:**
- `static/js/notes.js:675`
- `static/js/notes.js:3225`
- `static/js/notes.js:3225`
- `static/js/notes.js:3225`

## `_toLocalDatetimeStr` — function, line 682
- **called from:**
- `static/js/notes.js:682`
- `static/js/notes.js:922`
- `static/js/notes.js:3223`
- `static/js/notes.js:3224`
- `static/js/notes.js:3225`
- `static/js/notes.js:3259`
- `static/js/notes.js:3459`

## `pad` — arrow, line 684
- **called from:**
- `static/js/calendar.js:3115`
- `static/js/calendar.js:3115`
- `static/js/calendar.js:3115`
- `static/js/calendar.js:3115`
- `static/js/document.js:4391`
- `static/js/document.js:4391`
- `static/js/document.js:4391`
- `static/js/document.js:4391`
- `static/js/document.js:4415`
- `static/js/document.js:4415`
- `static/js/document.js:4415`
- `static/js/document.js:4415`
- `static/js/emailInbox.js:1185`
- `static/js/emailInbox.js:1185`
- `static/js/emailInbox.js:1185`
- `static/js/emailInbox.js:1185`
- `static/js/emailInbox.js:1222`
- `static/js/emailInbox.js:1222`
- `static/js/emailInbox.js:1222`
- `static/js/emailInbox.js:1222`
- `static/js/emailLibrary.js:8646`
- `static/js/emailLibrary.js:8646`
- `static/js/emailLibrary.js:8646`
- `static/js/emailLibrary.js:8646`
- `static/js/emailLibrary.js:8707`
- `static/js/emailLibrary.js:8707`
- `static/js/emailLibrary.js:8707`
- `static/js/emailLibrary.js:8707`
- `static/js/modalManager.js:706`
- `static/js/notes.js:685`
- `static/js/notes.js:685`
- `static/js/notes.js:685`
- `static/js/notes.js:685`

## `_formatReminderTag` — function, line 687
- **called from:**
- `static/js/notes.js:687`
- `static/js/notes.js:1890`
- `static/js/notes.js:3197`

## `_nthWeekdayLabel` — function, line 704
- **called from:**
- `static/js/notes.js:704`

## `_isLastWeekdayOfMonth` — function, line 708
- **called from:**
- `static/js/notes.js:708`

## `_nthWeekdayOfMonth` — function, line 715
- **called from:**
- `static/js/notes.js:715`
- `static/js/notes.js:767`
- `static/js/notes.js:898`

## `_lastWeekdayOfMonth` — function, line 724
- **called from:**
- `static/js/notes.js:724`
- `static/js/notes.js:771`
- `static/js/notes.js:901`

## `_snapToRepeat` — function, line 735
- **called from:**
- `static/js/notes.js:735`
- `static/js/notes.js:3257`

## `_formatRepeatLabel` — function, line 788
- **called from:**
- `static/js/notes.js:788`
- `static/js/notes.js:1890`
- `static/js/notes.js:3198`

## `_loadFiredReminders` — function, line 816
- **called from:**
- `static/js/notes.js:816`
- `static/js/notes.js:928`
- `static/js/notes.js:3672`

## `_saveFiredReminders` — function, line 821
- **called from:**
- `static/js/notes.js:821`
- `static/js/notes.js:964`
- `static/js/notes.js:3674`

## `_ensureNotificationPermission` — function, line 826
- **called from:**
- `static/js/notes.js:826`
- `static/js/notes.js:3451`

## `_normalizeRepeat` — function, line 844
- **called from:**
- `static/js/notes.js:790`
- `static/js/notes.js:844`
- `static/js/notes.js:863`
- `static/js/notes.js:3240`
- `static/js/notes.js:3256`

## `_advanceRecurring` — function, line 858
- **called from:**
- `static/js/notes.js:858`
- `static/js/notes.js:940`
- `static/js/notes.js:953`

## `step` — function, line 866
- **called from:**
- `static/js/notes.js:866`
- `static/js/notes.js:912`
- `static/js/notes.js:919`

## `_checkReminders` — function, line 925
- **called from:**
- `static/js/notes.js:925`
- `static/js/notes.js:1045`

## `_fireReminder` — function, line 969
- **called from:**
- `static/js/notes.js:937`
- `static/js/notes.js:969`

## `showLocal` — arrow, line 995
- **called from:**
- `static/js/notes.js:1009`
- `static/js/notes.js:1023`
- `static/js/notes.js:1027`

## `_startReminderLoop` — function, line 1042
- **called from:**
- `static/js/notes.js:1042`
- `static/js/notes.js:1434`
- `static/js/notes.js:5306`

## `_countDueReminders` — function, line 1048
- **called from:**
- `static/js/notes.js:1048`

## `_firedDotDismissedAt` — arrow, line 1052
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_countFiredReminders` — function, line 1059
- **called from:**
- `static/js/notes.js:1059`
- `static/js/notes.js:1079`

## `dismissFiredReminderDot` — function, line 1072
- **called from:**
- `static/js/notes.js:1072`

## `_updateRailBadge` — function, line 1078
- **called from:**
- `static/js/notes.js:966`
- `static/js/notes.js:1075`
- `static/js/notes.js:1078`
- `static/js/notes.js:1140`
- `static/js/notes.js:1741`

## `refreshDueBadge` — function, line 1129
- **called from:**
- `static/app.js:1110`
- `static/app.js:1111`
- `static/js/notes.js:1129`

## `openPanel` — function, line 1145
- **called from:**
- `static/app.js:1180`
- `static/js/chat.js:7595`
- `static/js/chat.js:7636`
- `static/js/document.js:4757`
- `static/js/document.js:6886`
- `static/js/document.js:7048`
- `static/js/document.js:7095`
- `static/js/document.js:7097`
- `static/js/document.js:7227`
- `static/js/document.js:7232`
- `static/js/document.js:7280`
- `static/js/document.js:7345`
- `static/js/document.js:7376`
- `static/js/document.js:7382`
- `static/js/document.js:8254`
- `static/js/document.js:10362`
- `static/js/document.js:10718`
- `static/js/emailInbox.js:1008`
- `static/js/emailInbox.js:1069`
- `static/js/notes.js:999`
- `static/js/notes.js:1145`
- `static/js/notes.js:1623`
- `static/js/notes.js:1695`
- `static/js/notes.js:5323`
- `static/js/notes.js:5335`
- `static/js/research/panel.js:232`
- `static/js/research/panel.js:236`
- `static/js/settings.js:2201`
- `static/js/settings/search.js:75`

## `syncArchiveBtn` — arrow, line 1277
- **called from:**
- `static/js/notes.js:1287`
- `static/js/notes.js:1291`

## `_setViewLabel` — arrow, line 1313
- **called from:**
- `static/js/notes.js:1317`
- `static/js/notes.js:1323`

## `_renderLoadingSkeleton` — function, line 1439
- **called from:**
- `static/js/notes.js:1427`
- `static/js/notes.js:1439`

## `_enterSelectMode` — function, line 1456
- **called from:**
- `static/js/notes.js:1329`
- `static/js/notes.js:1456`
- `static/js/sessions.js:861`
- `static/js/sessions.js:1600`
- `static/js/sessions.js:1658`
- `static/js/sessions.js:1670`
- `static/js/skills.js:414`
- `static/js/skills.js:1673`
- `static/js/skills.js:2004`

## `_exitSelectMode` — function, line 1467
- **called from:**
- `static/js/gallery.js:2520`
- `static/js/gallery.js:2523`
- `static/js/gallery.js:2652`
- `static/js/gallery.js:2691`
- `static/js/gallery.js:2729`
- `static/js/gallery.js:2757`
- `static/js/gallery.js:2769`
- `static/js/gallery.js:2787`
- `static/js/notes.js:1329`
- `static/js/notes.js:1342`
- `static/js/notes.js:1356`
- `static/js/notes.js:1369`
- `static/js/notes.js:1416`
- `static/js/notes.js:1467`
- `static/js/sessions.js:1631`
- `static/js/sessions.js:1657`
- `static/js/sessions.js:1662`
- `static/js/sessions.js:1677`
- `static/js/sessions.js:1718`
- `static/js/sessions.js:1739`
- `static/js/skills.js:641`
- `static/js/skills.js:1684`
- `static/js/skills.js:1754`
- `static/js/skills.js:1813`
- `static/js/skills.js:1833`
- `static/js/skills.js:1844`
- `static/js/skills.js:2004`

## `_updateBulkBar` — function, line 1479
- **called from:**
- `static/js/emailLibrary.js:1210`
- `static/js/emailLibrary.js:1940`
- `static/js/emailLibrary.js:3028`
- `static/js/emailLibrary.js:3037`
- `static/js/emailLibrary.js:3048`
- `static/js/emailLibrary.js:3103`
- `static/js/emailLibrary.js:5070`
- `static/js/emailLibrary.js:5311`
- `static/js/emailLibrary.js:8077`
- `static/js/emailLibrary.js:8175`
- `static/js/emailLibrary.js:8186`
- `static/js/emailLibrary.js:8366`
- `static/js/notes.js:1350`
- `static/js/notes.js:1464`
- `static/js/notes.js:1479`
- `static/js/notes.js:2259`
- `static/js/skills.js:907`
- `static/js/skills.js:1680`
- `static/js/skills.js:1696`
- `static/js/skills.js:1726`

## `so` — class, line 1489
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_noteTags` — function, line 1495
- **called from:**
- `static/js/notes.js:1495`
- `static/js/notes.js:1503`
- `static/js/notes.js:1747`

## `_visibleNoteTags` — function, line 1502
- **called from:**
- `static/js/notes.js:1502`
- `static/js/notes.js:1532`
- `static/js/notes.js:1537`
- `static/js/notes.js:1753`
- `static/js/notes.js:1893`

## `_isPastReminder` — function, line 1506
- **called from:**
- `static/js/notes.js:1506`
- `static/js/notes.js:1513`
- `static/js/notes.js:1536`

## `_clearPastReminders` — function, line 1512
- **called from:**
- `static/js/notes.js:1512`
- `static/js/notes.js:1596`

## `_renderLabels` — function, line 1528
- **called from:**
- `static/js/notes.js:1528`
- `static/js/notes.js:1615`

## `_renderLabelsInto` — function, line 1607
- **called from:**
- `static/js/notes.js:1443`
- `static/js/notes.js:1607`
- `static/js/notes.js:1801`
- `static/js/notes.js:1972`

## `_ensureNotesChipRegistered` — function, line 1618
- **called from:**
- `static/js/notes.js:1618`
- `static/js/notes.js:1638`

## `closePanel` — function, line 1631
- **called from:**
- `static/app.js:764`
- `static/app.js:772`
- `static/app.js:861`
- `static/app.js:862`
- `static/app.js:961`
- `static/app.js:2007`
- `static/js/document.js:222`
- `static/js/document.js:272`
- `static/js/document.js:3985`
- `static/js/document.js:4087`
- `static/js/document.js:4639`
- `static/js/document.js:4808`
- `static/js/document.js:5114`
- `static/js/document.js:5193`
- `static/js/document.js:5196`
- `static/js/document.js:5910`
- `static/js/document.js:6894`
- `static/js/document.js:7369`
- `static/js/document.js:9827`
- `static/js/document.js:11126`
- `static/js/notes.js:534`
- `static/js/notes.js:580`
- `static/js/notes.js:1237`
- `static/js/notes.js:1261`
- `static/js/notes.js:1631`
- `static/js/notes.js:1694`
- `static/js/notes.js:4461`
- `static/js/research/panel.js:230`
- `static/js/research/panel.js:277`
- `static/js/research/panel.js:285`
- `static/js/research/panel.js:328`
- `static/js/research/panel.js:684`
- `static/js/research/panel.js:732`
- `static/js/research/panel.js:792`
- `static/js/research/panel.js:1232`
- `static/js/sessions.js:2232`
- `static/js/sessions.js:2340`
- `static/js/slashCommands.js:1241`

## `_cleanup` — arrow, line 1678
- **called from:**
- `scripts/diffusion_server.py:439`
- `scripts/diffusion_server.py:443`
- `scripts/diffusion_server.py:457`
- `scripts/diffusion_server.py:468`
- `scripts/diffusion_server.py:488`
- `scripts/diffusion_server.py:504`
- `scripts/diffusion_server.py:635`
- `static/js/compare/index.js:1391`
- `static/js/cookbookRunning.js:2784`
- `static/js/cookbookRunning.js:2818`
- `static/js/cookbookRunning.js:2824`
- `static/js/document.js:8306`
- `static/js/document.js:8953`
- `static/js/document.js:9024`
- `static/js/emailInbox.js:1197`
- `static/js/emailInbox.js:1205`
- `static/js/emailInbox.js:1210`

## `togglePanel` — function, line 1693
- **called from:**
- `static/app.js:1104`
- `static/js/notes.js:1693`

## `isPanelOpen` — function, line 1698
- **called from:**
- `static/app.js:766`
- `static/app.js:960`
- `static/app.js:1985`
- `static/app.js:2006`
- `static/app.js:3835`
- `static/js/document.js:6038`
- `static/js/document.js:11130`
- `static/js/emailInbox.js:1008`
- `static/js/emailInbox.js:1068`
- `static/js/notes.js:1698`
- `static/js/notes.js:5317`
- `static/js/sessions.js:2339`
- `static/js/slashCommands.js:1240`

## `_captureCardPositions` — function, line 1703
- **called from:**
- `static/js/notes.js:1703`
- `static/js/notes.js:1744`

## `_animateReflow` — function, line 1714
- **called from:**
- `static/js/notes.js:1714`
- `static/js/notes.js:1982`

## `_renderNotes` — function, line 1740
- **called from:**
- `static/js/notes.js:410`
- `static/js/notes.js:415`
- `static/js/notes.js:434`
- `static/js/notes.js:441`
- `static/js/notes.js:1268`
- `static/js/notes.js:1300`
- `static/js/notes.js:1349`
- `static/js/notes.js:1358`
- `static/js/notes.js:1371`
- `static/js/notes.js:1432`
- `static/js/notes.js:1463`
- `static/js/notes.js:1476`
- `static/js/notes.js:1524`
- `static/js/notes.js:1602`
- `static/js/notes.js:1740`
- `static/js/notes.js:2073`
- `static/js/notes.js:2092`
- `static/js/notes.js:2280`
- `static/js/notes.js:2284`
- `static/js/notes.js:2348`
- `static/js/notes.js:2369`
- `static/js/notes.js:2374`
- `static/js/notes.js:2397`
- `static/js/notes.js:2400`
- `static/js/notes.js:2413`
- `static/js/notes.js:2416`
- `static/js/notes.js:2451`
- `static/js/notes.js:2454`
- `static/js/notes.js:2467`
- `static/js/notes.js:2470`
- `static/js/notes.js:2521`
- `static/js/notes.js:2524`
- `static/js/notes.js:2553`
- `static/js/notes.js:2567`
- `static/js/notes.js:2570`
- `static/js/notes.js:2580`
- `static/js/notes.js:2637`
- `static/js/notes.js:2645`
- `static/js/notes.js:3702`
- `static/js/notes.js:3712`
- `static/js/notes.js:3716`
- `static/js/notes.js:3748`
- `static/js/notes.js:3767`
- `static/js/notes.js:3770`
- `static/js/notes.js:4513`
- `static/js/notes.js:4587`
- `static/js/notes.js:4610`
- `static/js/notes.js:4720`
- `static/js/notes.js:5333`

## `_applyMasonry` — function, line 1994
- **called from:**
- `static/js/notes.js:1318`
- `static/js/notes.js:1324`
- `static/js/notes.js:1983`
- `static/js/notes.js:1994`
- `static/js/notes.js:2157`
- `static/js/notes.js:2158`
- `static/js/notes.js:3017`
- `static/js/notes.js:3019`
- `static/js/notes.js:3020`
- `static/js/notes.js:4685`
- `static/js/notes.js:4686`
- `static/js/notes.js:5141`

## `spanForHeight` — arrow, line 2007
- **called from:**
- `static/js/notes.js:2013`
- `static/js/notes.js:2017`
- `static/js/notes.js:2026`
- `static/js/notes.js:2035`

## `recomputeFullRows` — arrow, line 2008
- **called from:**
- `static/js/notes.js:2037`
- `static/js/notes.js:2048`

## `recompute` — arrow, line 2029
- **called from:**
- `static/js/notes.js:2045`

## `_wireTodayView` — function, line 2058
- **called from:**
- `static/js/notes.js:1828`
- `static/js/notes.js:2058`

## `_renderQuickAdd` — function, line 2098
- **called from:**
- `static/js/notes.js:1444`
- `static/js/notes.js:1802`
- `static/js/notes.js:1973`
- `static/js/notes.js:2098`

## `setType` — arrow, line 2123
- **called from:**
- `static/js/notes.js:2138`

## `expandToForm` — arrow, line 2142
- **called from:**
- `static/js/notes.js:2169`
- `static/js/notes.js:2170`
- `static/js/notes.js:2173`

## `_bindCardEvents` — function, line 2179
- **called from:**
- `static/js/notes.js:1981`
- `static/js/notes.js:2179`

## `tapToEditOrSelect` — arrow, line 2180
- **called from:**
- `static/js/notes.js:2207`
- `static/js/notes.js:2211`
- `static/js/notes.js:2218`
- `static/js/notes.js:2232`
- `static/js/notes.js:2247`

## `_applyCardColor` — arrow, line 2290
- **called from:**
- `static/js/notes.js:2309`
- `static/js/notes.js:2312`

## `undo` — arrow, line 2365
- **called from:**
- `tests/test_db_stubs_helper.py:67`
- `tests/test_db_stubs_helper.py:82`
- `tests/test_db_stubs_helper.py:99`
- `tests/test_db_stubs_helper.py:118`
- `tests/test_review_regressions.py:1297`
- `static/js/editor/history-panel.js:29`
- `static/js/editor/keyboard-shortcuts.js:10`
- `static/js/editor/keyboard-shortcuts.js:88`
- `static/js/editor/tools/transform-session.js:9`
- `static/js/editor/tools/transform-session.js:370`
- `static/js/galleryEditor.js:1352`
- `static/js/signature.js:261`
- `static/js/signature.js:429`

## `finish` — arrow, line 2368
- **called from:**
- `src/pdf_forms.py:338`
- `static/js/calendar.js:34`
- `static/js/calendar.js:42`
- `static/js/calendar.js:43`
- `static/js/calendar.js:45`
- `static/js/chat.js:1226`
- `static/js/fileHandler.js:92`
- `static/js/fileHandler.js:129`
- `static/js/fileHandler.js:130`
- `static/js/fileHandler.js:144`
- `static/js/fileHandler.js:147`
- `static/js/gallery.js:2191`
- `static/js/gallery.js:2194`
- `static/js/notes.js:361`
- `static/js/notes.js:369`
- `static/js/notes.js:370`
- `static/js/notes.js:373`
- `static/js/notes.js:2381`
- `static/js/notes.js:2385`

## `once` — arrow, line 2381
- **called from:**
- `static/js/calendar.js:1269`
- `static/js/calendar.js:3222`
- `static/js/escMenuStack.js:75`
- `static/js/notes.js:3898`

## `finishRemove` — arrow, line 2429
- **called from:**
- `static/js/notes.js:2439`

## `_startChecklistItemEdit` — function, line 2530
- **called from:**
- `static/js/notes.js:2530`
- `static/js/notes.js:2596`

## `save` — arrow, line 2546
- **called from:**
- `companion/pairing.py:224`
- `mcp_servers/memory_server.py:187`
- `mcp_servers/memory_server.py:215`
- `mcp_servers/memory_server.py:243`
- `routes/auth_routes.py:261`
- `routes/backup_routes.py:107`
- `routes/backup_routes.py:191`
- `routes/gallery/gallery_routes.py:54`
- `routes/gallery/gallery_routes.py:548`
- `routes/gallery/gallery_routes.py:1337`
- `routes/gallery/gallery_routes.py:1340`
- `routes/gallery/gallery_routes.py:1410`
- `routes/gallery/gallery_routes.py:1443`
- `routes/gallery/gallery_routes.py:1445`
- `routes/gallery/gallery_routes.py:1733`
- `routes/gallery/gallery_routes.py:1782`
- `routes/gallery/gallery_routes.py:1830`
- `routes/gallery/gallery_routes.py:2052`
- `routes/gallery/gallery_routes.py:2102`
- `routes/gallery/gallery_routes.py:2116`
- `routes/memory/memory_routes.py:137`
- `routes/memory/memory_routes.py:511`
- `routes/memory/memory_routes.py:540`
- `routes/memory/memory_routes.py:562`
- `routes/upload_routes.py:401`
- `scripts/diffusion_server.py:253`
- `scripts/diffusion_server.py:1075`
- `scripts/diffusion_server.py:1170`
- `scripts/diffusion_server.py:1181`
- `scripts/diffusion_server.py:1407`
- `scripts/diffusion_server.py:1454`
- `scripts/mlx_image_server.py:181`
- `scripts/mlx_image_server.py:200`
- `scripts/mlx_image_server.py:318`
- `services/memory/memory_extractor.py:652`
- `services/memory/memory_extractor.py:841`
- `services/memory/service.py:123`
- `src/ai_interaction.py:401`
- `src/ai_interaction.py:440`
- `src/ai_interaction.py:472`
- `src/builtin_actions.py:730`
- `src/caldav_writeback.py:156`
- `src/chat_handler.py:349`
- `src/document_processor.py:141`
- `src/document_processor.py:385`
- `src/document_processor.py:509`
- `src/memory.py:212`
- `src/memory.py:255`
- `src/memory.py:315`
- `src/memory_provider.py:166`
- `src/memory_provider.py:249`
- `src/pdf_forms.py:253`
- `src/pdf_forms.py:362`
- `src/pdf_forms.py:398`
- `src/preset_manager.py:74`
- `src/preset_manager.py:97`
- `src/preset_manager.py:109`
- `src/preset_manager.py:155`
- `src/preset_manager.py:175`
- `src/preset_manager.py:181`
- … +85 more (grep the name in repo)

## `onKeydown` — arrow, line 2573
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_maybeSwap` — function, line 2706
- **called from:**
- `static/js/notes.js:2706`
- `static/js/notes.js:2741`
- `static/js/notes.js:2835`

## `_follow` — arrow, line 2761
- **called from:**
- `static/js/notes.js:2833`
- `static/js/notes.js:2839`

## `_reanchor` — arrow, line 2768
- **called from:**
- `static/js/notes.js:2813`
- `static/js/notes.js:2838`

## `_endDrag` — arrow, line 2779
- **called from:**
- `static/js/notes.js:2843`
- `static/js/notes.js:2844`

## `_draftKey` — function, line 2855
- **called from:**
- `static/js/notes.js:2855`
- `static/js/notes.js:2857`
- `static/js/notes.js:2859`
- `static/js/notes.js:2889`

## `_loadDraft` — function, line 2856
- **called from:**
- `static/js/notes.js:2856`
- `static/js/notes.js:2909`

## `_clearDraft` — function, line 2859
- **called from:**
- `static/js/notes.js:2859`
- `static/js/notes.js:2888`
- `static/js/notes.js:3695`
- `static/js/notes.js:3748`

## `_collectFormDraft` — function, line 2860
- **called from:**
- `static/js/notes.js:2860`
- `static/js/notes.js:2887`
- `static/js/notes.js:2903`

## `_isDraftEmpty` — function, line 2877
- **called from:**
- `static/js/notes.js:2877`
- `static/js/notes.js:2888`
- `static/js/notes.js:2904`
- `static/js/notes.js:2910`

## `_wireDraftAutosave` — function, line 2884
- **called from:**
- `static/js/notes.js:2884`
- `static/js/notes.js:3776`

## `save` — arrow, line 2886
- **called from:**
- `companion/pairing.py:224`
- `mcp_servers/memory_server.py:187`
- `mcp_servers/memory_server.py:215`
- `mcp_servers/memory_server.py:243`
- `routes/auth_routes.py:261`
- `routes/backup_routes.py:107`
- `routes/backup_routes.py:191`
- `routes/gallery/gallery_routes.py:54`
- `routes/gallery/gallery_routes.py:548`
- `routes/gallery/gallery_routes.py:1337`
- `routes/gallery/gallery_routes.py:1340`
- `routes/gallery/gallery_routes.py:1410`
- `routes/gallery/gallery_routes.py:1443`
- `routes/gallery/gallery_routes.py:1445`
- `routes/gallery/gallery_routes.py:1733`
- `routes/gallery/gallery_routes.py:1782`
- `routes/gallery/gallery_routes.py:1830`
- `routes/gallery/gallery_routes.py:2052`
- `routes/gallery/gallery_routes.py:2102`
- `routes/gallery/gallery_routes.py:2116`
- `routes/memory/memory_routes.py:137`
- `routes/memory/memory_routes.py:511`
- `routes/memory/memory_routes.py:540`
- `routes/memory/memory_routes.py:562`
- `routes/upload_routes.py:401`
- `scripts/diffusion_server.py:253`
- `scripts/diffusion_server.py:1075`
- `scripts/diffusion_server.py:1170`
- `scripts/diffusion_server.py:1181`
- `scripts/diffusion_server.py:1407`
- `scripts/diffusion_server.py:1454`
- `scripts/mlx_image_server.py:181`
- `scripts/mlx_image_server.py:200`
- `scripts/mlx_image_server.py:318`
- `services/memory/memory_extractor.py:652`
- `services/memory/memory_extractor.py:841`
- `services/memory/service.py:123`
- `src/ai_interaction.py:401`
- `src/ai_interaction.py:440`
- `src/ai_interaction.py:472`
- `src/builtin_actions.py:730`
- `src/caldav_writeback.py:156`
- `src/chat_handler.py:349`
- `src/document_processor.py:141`
- `src/document_processor.py:385`
- `src/document_processor.py:509`
- `src/memory.py:212`
- `src/memory.py:255`
- `src/memory.py:315`
- `src/memory_provider.py:166`
- `src/memory_provider.py:249`
- `src/pdf_forms.py:253`
- `src/pdf_forms.py:362`
- `src/pdf_forms.py:398`
- `src/preset_manager.py:74`
- `src/preset_manager.py:97`
- `src/preset_manager.py:109`
- `src/preset_manager.py:155`
- `src/preset_manager.py:175`
- `src/preset_manager.py:181`
- … +85 more (grep the name in repo)

## `sched` — arrow, line 2892
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_commitOpenInPlaceEditor` — function, line 2900
- **called from:**
- `static/js/notes.js:55`
- `static/js/notes.js:1664`
- `static/js/notes.js:2900`

## `_applyDraftToNote` — function, line 2908
- **called from:**
- `static/js/notes.js:2908`
- `static/js/notes.js:4363`
- `static/js/notes.js:4667`
- `static/js/notes.js:4762`

## `_buildForm` — function, line 2920
- **called from:**
- `static/js/notes.js:2144`
- `static/js/notes.js:2920`
- `static/js/notes.js:4364`
- `static/js/notes.js:4668`
- `static/js/notes.js:4763`

## `_refreshFormLayout` — arrow, line 3014
- **called from:**
- `static/js/notes.js:3106`

## `_activateAt` — arrow, line 3117
- **called from:**
- `static/js/notes.js:3123`

## `_applyFormColor` — arrow, line 3130
- **called from:**
- `static/js/notes.js:3147`
- `static/js/notes.js:3150`

## `_grow` — arrow, line 3168
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_renderReminderTag` — function, line 3192
- **called from:**
- `static/js/notes.js:3192`
- `static/js/notes.js:3208`
- `static/js/notes.js:3245`
- `static/js/notes.js:3450`
- `static/js/notes.js:3498`

## `_openReminderMenu` — function, line 3215
- **called from:**
- `static/js/notes.js:3211`
- `static/js/notes.js:3215`
- `static/js/notes.js:3497`

## `getNorm` — function, line 3238
- **called from:**
- `static/js/notes.js:3238`
- `static/js/notes.js:3291`
- `static/js/notes.js:3315`
- `static/js/notes.js:3325`
- `static/js/notes.js:3382`

## `commit` — function, line 3243
- **called from:**
- `app.py:449`
- `app.py:1047`
- `core/database.py:917`
- `core/database.py:940`
- `core/database.py:965`
- `core/database.py:988`
- `core/database.py:1011`
- `core/database.py:1042`
- `core/database.py:1067`
- `core/database.py:1091`
- `core/database.py:1120`
- `core/database.py:1142`
- `core/database.py:1165`
- `core/database.py:1189`
- `core/database.py:1211`
- `core/database.py:1244`
- `core/database.py:1266`
- `core/database.py:1289`
- `core/database.py:1313`
- `core/database.py:1337`
- `core/database.py:1371`
- `core/database.py:1400`
- `core/database.py:1474`
- `core/database.py:1553`
- `core/database.py:1568`
- `core/database.py:1594`
- `core/database.py:1666`
- `core/database.py:1685`
- `core/database.py:1697`
- `core/database.py:1709`
- `core/database.py:1726`
- `core/database.py:1746`
- `core/database.py:1767`
- `core/database.py:1779`
- `core/database.py:1792`
- `core/database.py:1797`
- `core/database.py:1809`
- `core/database.py:1813`
- `core/database.py:2060`
- `core/database.py:2212`
- `core/database.py:2296`
- `core/database.py:2357`
- `core/database.py:2386`
- `core/database.py:2418`
- `core/database.py:2452`
- `core/database.py:2473`
- `core/database.py:2500`
- `core/database.py:2526`
- `core/database.py:2556`
- `core/database.py:2579`
- `core/database.py:2601`
- `core/database.py:2630`
- `core/database.py:2704`
- `core/database.py:2772`
- `core/session_manager.py:415`
- `core/session_manager.py:465`
- `core/session_manager.py:490`
- `core/session_manager.py:555`
- `core/session_manager.py:596`
- `core/session_manager.py:631`
- … +401 more (grep the name in repo)

## `snapAndCommit` — function, line 3253
- **called from:**
- `static/js/notes.js:3253`
- `static/js/notes.js:3376`
- `static/js/notes.js:3394`
- `static/js/notes.js:3403`

## `reposition` — function, line 3266
- **called from:**
- `static/js/notes.js:3266`
- `static/js/notes.js:3362`

## `render` — function, line 3281
- **called from:**
- `static/js/calendar.js:1259`
- `static/js/calendar.js:2092`
- `static/js/chat.js:3650`
- `static/js/chat.js:4474`
- `static/js/chat.js:4602`
- `static/js/editor/layer-panel.js:67`
- `static/js/editor/layer-panel.js:144`
- `static/js/editor/layer-panel.js:157`
- `static/js/editor/layer-panel.js:271`
- `static/js/editor/layer-panel.js:325`
- `static/js/editor/layer-panel.js:342`
- `static/js/editor/layer-panel.js:373`
- `static/js/editor/layer-panel.js:392`
- `static/js/editor/layer-panel.js:413`
- `static/js/editor/layer-panel.js:445`
- `static/js/editor/layer-panel.js:458`
- `static/js/editor/layer-panel.js:499`
- `static/js/editor/layer-panel.js:532`
- `static/js/editor/layer-panel.js:552`
- `static/js/editor/layer-panel.js:566`
- `static/js/emojiPicker.js:227`
- `static/js/emojiPicker.js:265`
- `static/js/emojiPicker.js:267`
- `static/js/galleryEditor.js:3572`
- `static/js/group.js:478`
- `static/js/group.js:515`
- `static/js/group.js:516`
- `static/js/markdown.js:1299`
- `static/js/notes.js:3281`
- `static/js/notes.js:3386`
- `static/js/notes.js:3389`
- `static/js/notes.js:3392`
- `static/js/notes.js:3397`
- `static/js/notes.js:3400`
- `static/js/notes.js:3410`
- `static/js/research/panel.js:721`
- `static/js/settings.js:309`
- `static/js/settings.js:352`
- `static/js/settings.js:367`
- `static/js/settings.js:371`
- `static/js/settings.js:374`
- `static/js/settings.js:1839`
- `static/js/settings.js:1887`
- `static/js/settings.js:1929`
- `static/js/settings.js:1993`
- `static/js/settings.js:1999`
- `static/js/settings/search.js:79`
- `static/js/settings/search.js:129`
- `static/js/skills.js:1071`
- `static/js/streamingRenderer.js:57`
- `static/js/streamingRenderer.js:76`
- `static/js/streamingRenderer.js:136`
- `static/js/streamingSegmenter.js:18`
- `static/js/streamingSegmenter.js:18`
- `static/js/streamingSegmenter.js:18`
- `static/js/streamingSegmenter.js:118`
- `static/js/streamingSegmenter.js:118`
- `static/js/streamingSegmenter.js:118`
- `static/js/streamingSegmenter.js:125`
- `static/js/streamingSegmenter.js:125`
- … +1 more (grep the name in repo)

## `wire` — function, line 3366
- **called from:**
- `static/js/notes.js:3363`
- `static/js/notes.js:3366`

## `close` — arrow, line 3413
- **called from:**
- `app.py:333`
- `app.py:451`
- `app.py:532`
- `app.py:1050`
- `app.py:1174`
- `app.py:1295`
- `companion/pairing.py:151`
- `companion/routes.py:165`
- `core/database.py:161`
- `core/database.py:923`
- `core/database.py:946`
- `core/database.py:971`
- `core/database.py:994`
- `core/database.py:1017`
- `core/database.py:1048`
- `core/database.py:1073`
- `core/database.py:1097`
- `core/database.py:1125`
- `core/database.py:1148`
- `core/database.py:1171`
- `core/database.py:1194`
- `core/database.py:1217`
- `core/database.py:1249`
- `core/database.py:1272`
- `core/database.py:1295`
- `core/database.py:1319`
- `core/database.py:1343`
- `core/database.py:1377`
- `core/database.py:1406`
- `core/database.py:1479`
- `core/database.py:2068`
- `core/database.py:2301`
- `core/database.py:2363`
- `core/database.py:2479`
- `core/database.py:2506`
- `core/database.py:2532`
- `core/database.py:2557`
- `core/database.py:2584`
- `core/database.py:2606`
- `core/database.py:2619`
- `core/database.py:2635`
- `core/session_manager.py:68`
- `core/session_manager.py:177`
- `core/session_manager.py:428`
- `core/session_manager.py:568`
- `core/session_manager.py:603`
- `core/session_manager.py:651`
- `core/session_manager.py:771`
- `core/session_manager.py:858`
- `core/session_manager.py:885`
- `core/session_manager.py:899`
- `core/session_manager.py:945`
- `core/session_manager.py:989`
- `core/session_manager.py:1013`
- `core/session_manager.py:1033`
- `core/session_manager.py:1054`
- `core/session_manager.py:1140`
- `mcp_servers/email_server.py:220`
- `mcp_servers/email_server.py:815`
- `mcp_servers/email_server.py:1351`
- … +754 more (grep the name in repo)

## `_monthlyShortDescriptor` — function, line 3421
- **called from:**
- `static/js/notes.js:3308`
- `static/js/notes.js:3336`
- `static/js/notes.js:3421`

## `_setReminder` — function, line 3436
- **called from:**
- `static/js/notes.js:3223`
- `static/js/notes.js:3224`
- `static/js/notes.js:3225`
- `static/js/notes.js:3436`
- `static/js/notes.js:3492`

## `_pickCustomDate` — function, line 3454
- **called from:**
- `static/js/notes.js:3226`
- `static/js/notes.js:3454`

## `_wireHashtag` — function, line 3555
- **called from:**
- `static/js/notes.js:3072`
- `static/js/notes.js:3555`
- `static/js/notes.js:3576`
- `static/js/notes.js:3577`

## `_enterArchive` — arrow, line 3731
- **called from:**
- `static/js/notes.js:3742`

## `_enterUpdate` — arrow, line 3736
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_buildGoalHtml` — function, line 3785
- **called from:**
- `static/js/notes.js:2948`
- `static/js/notes.js:3785`

## `_wireGoalForm` — function, line 3795
- **called from:**
- `static/js/notes.js:3155`
- `static/js/notes.js:3795`

## `was` — class, line 3822
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_buildChecklistHtml` — function, line 3827
- **called from:**
- `static/js/notes.js:2949`
- `static/js/notes.js:3057`
- `static/js/notes.js:3790`
- `static/js/notes.js:3827`

## `_wireRow` — function, line 3845
- **called from:**
- `static/js/notes.js:3845`
- `static/js/notes.js:3916`
- `static/js/notes.js:3919`
- `static/js/notes.js:4902`

## `_wireChecklist` — function, line 3893
- **called from:**
- `static/js/notes.js:3058`
- `static/js/notes.js:3154`
- `static/js/notes.js:3824`
- `static/js/notes.js:3893`

## `_collectItems` — function, line 3950
- **called from:**
- `static/js/notes.js:2873`
- `static/js/notes.js:2874`
- `static/js/notes.js:3035`
- `static/js/notes.js:3038`
- `static/js/notes.js:3663`
- `static/js/notes.js:3665`
- `static/js/notes.js:3950`

## `_buildDrawHtml` — function, line 3966
- **called from:**
- `static/js/notes.js:2946`
- `static/js/notes.js:3060`
- `static/js/notes.js:3966`

## `_wireCanvas` — function, line 4002
- **called from:**
- `static/js/notes.js:3065`
- `static/js/notes.js:3157`
- `static/js/notes.js:4002`

## `_snapshot` — arrow, line 4090
- **called from:**
- `tests/test_cookbook_error_tail_lines.py:19`
- `tests/test_cookbook_error_tail_lines.py:28`
- `tests/test_cookbook_error_tail_lines.py:38`
- `tests/test_cookbook_error_tail_lines.py:51`
- `static/js/notes.js:4127`
- `static/js/notes.js:4202`

## `_undo` — arrow, line 4097
- **called from:**
- `static/js/notes.js:4332`

## `_pos` — arrow, line 4108
- **called from:**
- `static/js/notes.js:4015`
- `static/js/notes.js:4128`
- `static/js/notes.js:4155`
- `static/js/notes.js:4225`

## `_begin` — arrow, line 4118
- **called from:**
- `static/js/notes.js:4268`

## `_openTextInput` — arrow, line 4144
- **called from:**
- `static/js/notes.js:4124`

## `commit` — arrow, line 4194
- **called from:**
- `app.py:449`
- `app.py:1047`
- `core/database.py:917`
- `core/database.py:940`
- `core/database.py:965`
- `core/database.py:988`
- `core/database.py:1011`
- `core/database.py:1042`
- `core/database.py:1067`
- `core/database.py:1091`
- `core/database.py:1120`
- `core/database.py:1142`
- `core/database.py:1165`
- `core/database.py:1189`
- `core/database.py:1211`
- `core/database.py:1244`
- `core/database.py:1266`
- `core/database.py:1289`
- `core/database.py:1313`
- `core/database.py:1337`
- `core/database.py:1371`
- `core/database.py:1400`
- `core/database.py:1474`
- `core/database.py:1553`
- `core/database.py:1568`
- `core/database.py:1594`
- `core/database.py:1666`
- `core/database.py:1685`
- `core/database.py:1697`
- `core/database.py:1709`
- `core/database.py:1726`
- `core/database.py:1746`
- `core/database.py:1767`
- `core/database.py:1779`
- `core/database.py:1792`
- `core/database.py:1797`
- `core/database.py:1809`
- `core/database.py:1813`
- `core/database.py:2060`
- `core/database.py:2212`
- `core/database.py:2296`
- `core/database.py:2357`
- `core/database.py:2386`
- `core/database.py:2418`
- `core/database.py:2452`
- `core/database.py:2473`
- `core/database.py:2500`
- `core/database.py:2526`
- `core/database.py:2556`
- `core/database.py:2579`
- `core/database.py:2601`
- `core/database.py:2630`
- `core/database.py:2704`
- `core/database.py:2772`
- `core/session_manager.py:415`
- `core/session_manager.py:465`
- `core/session_manager.py:490`
- `core/session_manager.py:555`
- `core/session_manager.py:596`
- `core/session_manager.py:631`
- … +401 more (grep the name in repo)

## `_move` — arrow, line 4222
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_end` — arrow, line 4260
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_setMode` — arrow, line 4277
- **called from:**
- `static/js/notes.js:4319`
- `static/js/notes.js:4320`
- `static/js/notes.js:4329`
- `static/js/notes.js:4330`
- `static/js/notes.js:4331`

## `_cycle` — arrow, line 4322
- **called from:**
- `tests/test_skill_frontmatter_escape_roundtrip.py:61`
- `tests/test_skill_frontmatter_escape_roundtrip.py:76`
- `tests/test_skill_frontmatter_escape_roundtrip.py:122`
- `tests/test_skill_frontmatter_escape_roundtrip.py:155`
- `static/js/notes.js:4329`
- `static/js/notes.js:4330`
- `static/js/notes.js:4331`

## `_uploadCanvasAsPng` — function, line 4342
- **called from:**
- `static/js/notes.js:3656`
- `static/js/notes.js:4342`

## `_createNote` — function, line 4358
- **called from:**
- `static/js/notes.js:4358`

## `_serializeNoteForCopy` — function, line 4372
- **called from:**
- `static/js/notes.js:4372`
- `static/js/notes.js:4625`

## `_openNoteCornerMenu` — function, line 4389
- **called from:**
- `static/js/notes.js:2333`
- `static/js/notes.js:4389`

## `_positionNoteMenu` — function, line 4422
- **called from:**
- `static/js/notes.js:4422`
- `static/js/notes.js:4455`

## `close` — arrow, line 4431
- **called from:**
- `app.py:333`
- `app.py:451`
- `app.py:532`
- `app.py:1050`
- `app.py:1174`
- `app.py:1295`
- `companion/pairing.py:151`
- `companion/routes.py:165`
- `core/database.py:161`
- `core/database.py:923`
- `core/database.py:946`
- `core/database.py:971`
- `core/database.py:994`
- `core/database.py:1017`
- `core/database.py:1048`
- `core/database.py:1073`
- `core/database.py:1097`
- `core/database.py:1125`
- `core/database.py:1148`
- `core/database.py:1171`
- `core/database.py:1194`
- `core/database.py:1217`
- `core/database.py:1249`
- `core/database.py:1272`
- `core/database.py:1295`
- `core/database.py:1319`
- `core/database.py:1343`
- `core/database.py:1377`
- `core/database.py:1406`
- `core/database.py:1479`
- `core/database.py:2068`
- `core/database.py:2301`
- `core/database.py:2363`
- `core/database.py:2479`
- `core/database.py:2506`
- `core/database.py:2532`
- `core/database.py:2557`
- `core/database.py:2584`
- `core/database.py:2606`
- `core/database.py:2619`
- `core/database.py:2635`
- `core/session_manager.py:68`
- `core/session_manager.py:177`
- `core/session_manager.py:428`
- `core/session_manager.py:568`
- `core/session_manager.py:603`
- `core/session_manager.py:651`
- `core/session_manager.py:771`
- `core/session_manager.py:858`
- `core/session_manager.py:885`
- `core/session_manager.py:899`
- `core/session_manager.py:945`
- `core/session_manager.py:989`
- `core/session_manager.py:1013`
- `core/session_manager.py:1033`
- `core/session_manager.py:1054`
- `core/session_manager.py:1140`
- `mcp_servers/email_server.py:220`
- `mcp_servers/email_server.py:815`
- `mcp_servers/email_server.py:1351`
- … +754 more (grep the name in repo)

## `_openTodoAgentMenu` — function, line 4439
- **called from:**
- `static/js/notes.js:2617`
- `static/js/notes.js:4439`

## `_noteToAgentPrompt` — function, line 4472
- **called from:**
- `static/js/notes.js:4472`
- `static/js/notes.js:4490`

## `_agentSolveNote` — function, line 4487
- **called from:**
- `static/js/notes.js:4419`
- `static/js/notes.js:4487`

## `_agentSolveTodoItem` — function, line 4547
- **called from:**
- `static/js/notes.js:4466`
- `static/js/notes.js:4547`

## `_copyNote` — function, line 4622
- **called from:**
- `static/js/notes.js:1411`
- `static/js/notes.js:4418`
- `static/js/notes.js:4622`

## `_editNote` — function, line 4659
- **called from:**
- `static/js/notes.js:2093`
- `static/js/notes.js:2193`
- `static/js/notes.js:2322`
- `static/js/notes.js:4659`

## `_focusBest` — arrow, line 4696
- **called from:**
- `static/js/notes.js:4712`

## `_deleteNote` — function, line 4715
- **called from:**
- `static/js/notes.js:4715`

## `_isNotesMobileMode` — function, line 4732
- **called from:**
- `static/js/notes.js:1173`
- `static/js/notes.js:1904`
- `static/js/notes.js:2188`
- `static/js/notes.js:2199`
- `static/js/notes.js:2241`
- `static/js/notes.js:2681`
- `static/js/notes.js:2748`
- `static/js/notes.js:4732`

## `_openMobileFullscreenEdit` — function, line 4740
- **called from:**
- `static/js/notes.js:2191`
- `static/js/notes.js:4740`

## `_closeMobileFullscreenEdit` — function, line 4937
- **called from:**
- `static/js/notes.js:56`
- `static/js/notes.js:1665`
- `static/js/notes.js:4744`
- `static/js/notes.js:4786`
- `static/js/notes.js:4800`
- `static/js/notes.js:4810`
- `static/js/notes.js:4845`
- `static/js/notes.js:4852`
- `static/js/notes.js:4937`

## `_bindLongPressDrag` — function, line 4959
- **called from:**
- `static/js/notes.js:2200`
- `static/js/notes.js:4959`

## `cancel` — arrow, line 4992
- **called from:**
- `app.py:1283`
- `routes/shell_routes.py:723`
- `routes/shell_routes.py:1108`
- `routes/skills_routes.py:1800`
- `services/research/research_handler.py:140`
- `services/research/research_handler.py:143`
- `services/shell/service.py:163`
- `src/agent_loop.py:5124`
- `src/agent_loop.py:6401`
- `src/agent_runs.py:84`
- `src/agent_runs.py:195`
- `src/agent_runs.py:198`
- `src/agent_runs.py:237`
- `src/agent_runs.py:286`
- `src/agent_tools/subprocess_tools.py:273`
- `src/agent_tools/subprocess_tools.py:275`
- `src/agent_tools/subprocess_tools.py:279`
- `src/ai_interaction.py:1379`
- `src/ai_interaction.py:1646`
- `src/llm_core.py:109`
- `src/mcp_manager.py:400`
- `src/mcp_oauth.py:63`
- `src/research_handler.py:456`
- `src/research_handler.py:459`
- `src/task_scheduler.py:100`
- `src/task_scheduler.py:591`
- `src/task_scheduler.py:599`
- `src/task_scheduler.py:917`
- `src/task_scheduler.py:1012`
- `src/task_scheduler.py:2272`
- `src/task_scheduler.py:2296`
- `tests/test_builtin_mcp_bg_tasks.py:101`
- `tests/test_compare_stop_disconnect_poll.py:376`
- `tests/test_compare_stop_disconnect_poll.py:433`
- `tests/test_email_summary_llm.py:192`
- `tests/test_email_urgency_checkpoint.py:419`
- `tests/test_email_urgency_checkpoint.py:554`
- `tests/test_task_scheduler_cache.py:34`
- `tests/test_task_scheduler_cache.py:70`
- `static/js/chat.js:2841`
- `static/js/chat.js:5741`
- `static/js/chat.js:5756`
- `static/js/documentLibrary.js:180`
- `static/js/gallery.js:2576`
- `static/js/gallery.js:2584`
- `static/js/liveThinkingThrottle.js:20`
- `static/js/liveThinkingThrottle.js:22`
- `static/js/liveThinkingThrottle.js:193`
- `static/js/liveThinkingThrottle.js:198`
- `static/js/liveThinkingThrottle.js:199`
- `static/js/settings.js:883`
- `static/js/slashCommands.js:2439`
- `static/js/tasks.js:1076`
- `static/js/tts-ai.js:241`
- `static/js/windowDrag.js:157`

## `_enterDragMode` — function, line 5010
- **called from:**
- `static/js/notes.js:4981`
- `static/js/notes.js:5010`

## `_exitDragMode` — function, line 5027
- **called from:**
- `static/js/notes.js:5027`

## `_setupDragForCard` — function, line 5036
- **called from:**
- `static/js/notes.js:5036`

## `_beginGrab` — function, line 5049
- **called from:**
- `static/js/notes.js:5023`
- `static/js/notes.js:5045`
- `static/js/notes.js:5049`

## `_onDocTouchMove` — function, line 5082
- **called from:**
- `static/js/notes.js:5082`

## `_onDocTouchEnd` — function, line 5121
- **called from:**
- `static/js/notes.js:5031`
- `static/js/notes.js:5121`

## `_addRowReadMode` — function, line 5154
- **called from:**
- `static/js/notes.js:5154`

## `_wireChecklistTouchReorder` — function, line 5183
- **called from:**
- `static/js/notes.js:4817`
- `static/js/notes.js:4904`
- `static/js/notes.js:5183`

## `_beginChecklistGrab` — function, line 5205
- **called from:**
- `static/js/notes.js:5194`
- `static/js/notes.js:5205`

## `_onClTouchMove` — function, line 5229
- **called from:**
- `static/js/notes.js:5229`

## `_onClTouchEnd` — function, line 5258
- **called from:**
- `static/js/notes.js:5258`

## `_commitNoteReorder` — function, line 5276
- **called from:**
- `static/js/notes.js:5142`
- `static/js/notes.js:5276`

## `_initReminders` — function, line 5300
- **called from:**
- `static/js/notes.js:5300`

## `openNote` — function, line 5316
- **called from:**
- `static/js/notes.js:5316`

## `findAndFlash` — arrow, line 5339
- **called from:**
- `static/js/notes.js:5351`

## `tryNext` — arrow, line 5350
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
