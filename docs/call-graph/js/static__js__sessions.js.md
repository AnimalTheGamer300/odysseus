# `static/js/sessions.js` — definitions & call sites

130 definitions (regex-based, best-effort).
**Exports:** `clearResearching`, `clearStreamComplete`, `clearStreaming`, `closeArchive`, `closeLibrary`, `createDirectChat`, `default`, `deleteCurrentSessionFromTopMenu`, `getCurrentEndpointUrl`, `getCurrentModel`, `getCurrentSessionId`, `getPendingChat`, `getSessions`, `getSortMode`, `hasPendingChat`, `initDependencies`, `initDragSort`, `isCurrentSessionIncognito`, `loadSessions`, `markResearching`, `markStreamComplete`, `markStreaming`, `materializePendingSession`, `openArchive`, `openLibrary`, `preMaterializePendingSession`, `renderSessionList`, `selectSession`, `setCurrentSessionId`, `setSessionHasDocs`, `setSortMode`, `updateModelPicker`

## `_mirrorTabTitle` — function, line 28
- **called from:**
- `static/js/sessions.js:28`

## `apply` — arrow, line 31
- **called from:**
- `static/app.js:199`
- `static/js/admin.js:1765`
- `static/js/admin.js:1769`
- `static/js/composerHistoryRecall.js:175`
- `static/js/composerHistoryRecall.js:189`
- `static/js/composerHistoryRecall.js:193`
- `static/js/cookbookSchedule.js:22`
- `static/js/document.js:812`
- `static/js/document.js:821`
- `static/js/document.js:6225`
- `static/js/sessions.js:38`
- `static/js/settings.js:194`
- `static/js/settings.js:213`
- `static/js/skills.js:54`
- `static/js/theme.js:775`
- `static/js/theme.js:780`
- `static/js/ui.js:587`

## `_shouldPreserveStartupComposer` — function, line 57
- **called from:**
- `static/js/sessions.js:57`
- `static/js/sessions.js:65`

## `_clearComposerUnlessStartupTyped` — function, line 63
- **called from:**
- `static/js/sessions.js:63`
- `static/js/sessions.js:2015`
- `static/js/sessions.js:2371`

## `_paintSessionLoading` — function, line 73
- **called from:**
- `static/js/sessions.js:73`
- `static/js/sessions.js:2068`

## `_updateSessionLoading` — function, line 104
- **called from:**
- `static/js/sessions.js:104`
- `static/js/sessions.js:2120`

## `_nextPaint` — function, line 109
- **called from:**
- `static/js/sessions.js:109`
- `static/js/sessions.js:2070`
- `static/js/sessions.js:2121`

## `_displayHistoryContent` — function, line 113
- **called from:**
- `static/js/sessions.js:113`
- `static/js/sessions.js:177`
- `static/js/sessions.js:179`

## `_stripUserVisionBlocks` — function, line 132
- **called from:**
- `static/js/sessions.js:132`
- `static/js/sessions.js:184`

## `_historyPageLimit` — function, line 139
- **called from:**
- `static/js/sessions.js:139`
- `static/js/sessions.js:219`
- `static/js/sessions.js:2073`

## `_historyUrl` — function, line 143
- **called from:**
- `static/js/sessions.js:143`
- `static/js/sessions.js:242`
- `static/js/sessions.js:2073`

## `_addHistoryMessageWithFullRenderer` — function, line 150
- **called from:**
- `static/js/sessions.js:150`
- `static/js/sessions.js:200`

## `_renderHistoryMessage` — function, line 173
- **called from:**
- `static/js/sessions.js:173`
- `static/js/sessions.js:250`
- `static/js/sessions.js:2150`

## `_clearHistoryPager` — function, line 203
- **called from:**
- `static/js/sessions.js:203`
- `static/js/sessions.js:213`
- `static/js/sessions.js:1946`

## `_installHistoryPager` — function, line 211
- **called from:**
- `static/js/sessions.js:211`
- `static/js/sessions.js:2167`

## `loadOlder` — arrow, line 226
- **called from:**
- `static/js/sessions.js:286`
- `static/js/sessions.js:300`

## `_getIncognitoIds` — function, line 306
- **called from:**
- `static/js/sessions.js:306`
- `static/js/sessions.js:310`
- `static/js/sessions.js:313`
- `static/js/sessions.js:315`

## `_markIncognito` — function, line 309
- **called from:**
- `static/js/sessions.js:309`
- `static/js/sessions.js:2431`

## `_isIncognitoSession` — function, line 313
- **called from:**
- `static/js/sessions.js:313`
- `static/js/sessions.js:1174`
- `static/js/sessions.js:1773`
- `static/js/sessions.js:2485`

## `_cleanupIncognitoSessions` — function, line 314
- **called from:**
- `static/js/sessions.js:314`
- `static/js/sessions.js:1763`

## `_deselectCurrentSession` — function, line 337
- **called from:**
- `static/js/sessions.js:337`
- `static/js/sessions.js:376`
- `static/js/sessions.js:979`
- `static/js/sessions.js:1333`
- `static/js/sessions.js:1456`
- `static/js/sessions.js:2539`
- `static/js/sessions.js:2592`

## `_removeSessionFromLocalState` — function, line 357
- **called from:**
- `static/js/sessions.js:357`
- `static/js/sessions.js:980`
- `static/js/sessions.js:2540`

## `_normalizeSessionsList` — function, line 379
- **called from:**
- `static/js/sessions.js:379`
- `static/js/sessions.js:1792`

## `initDependencies` — function, line 394
- **called from:**
- `static/app.js:4310`
- `static/js/sessions.js:394`

## `loadFolderState` — function, line 400
- **called from:**
- `static/js/sessions.js:400`
- `static/js/sessions.js:1255`
- `static/js/sessions.js:1349`
- `static/js/sessions.js:1425`
- `static/js/sessions.js:1467`

## `saveFolderState` — function, line 403
- **called from:**
- `static/js/sessions.js:403`
- `static/js/sessions.js:1352`
- `static/js/sessions.js:1469`

## `loadFolderOrder` — function, line 406
- **called from:**
- `static/js/sessions.js:406`
- `static/js/sessions.js:1279`

## `saveFolderOrder` — function, line 409
- **called from:**
- `static/js/sessions.js:409`
- `static/js/sessions.js:2626`

## `getFolderNames` — function, line 414
- **called from:**
- `static/js/sessions.js:414`
- `static/js/sessions.js:433`

## `moveToFolder` — function, line 421
- **called from:**
- `static/js/sessions.js:421`
- `static/js/sessions.js:451`
- `static/js/sessions.js:465`
- `static/js/sessions.js:488`
- `static/js/sessions.js:1366`

## `buildFolderSubmenu` — function, line 432
- **called from:**
- `static/js/sessions.js:432`
- `static/js/sessions.js:875`

## `createSessionItem` — function, line 545
- **called from:**
- `static/js/sessions.js:545`
- `static/js/sessions.js:1147`
- `static/js/sessions.js:1156`

## `commit` — arrow, line 642
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

## `close` — arrow, line 696
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

## `_icon` — arrow, line 731
- **called from:**
- `tests/test_lang_icon_null_opts_js.py:33`
- `tests/test_lang_icon_null_opts_js.py:40`
- `static/js/emailInbox.js:1120`
- `static/js/emailLibrary.js:7898`
- `static/js/emailLibrary.js:7919`
- `static/js/emailLibrary.js:8109`
- `static/js/emailLibrary.js:8126`
- `static/js/sessions.js:739`
- `static/js/sessions.js:743`
- `static/js/sessions.js:747`
- `static/js/sessions.js:758`
- `static/js/sessions.js:765`
- `static/js/sessions.js:799`
- `static/js/sessions.js:815`
- `static/js/sessions.js:857`
- `static/js/sessions.js:892`

## `commit` — arrow, line 943
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

## `_dateBucketLabel` — function, line 1060
- **called from:**
- `static/js/sessions.js:1060`
- `static/js/sessions.js:1140`

## `dayStart` — arrow, line 1064
- **called from:**
- `static/js/emailLibrary.js:4904`
- `static/js/emailLibrary.js:4905`
- `static/js/sessions.js:1065`
- `static/js/sessions.js:1066`

## `_sessionBucketDate` — function, line 1081
- **called from:**
- `static/js/sessions.js:1081`
- `static/js/sessions.js:1140`

## `_loadDateSectionCollapseState` — function, line 1085
- **called from:**
- `static/js/sessions.js:1085`
- `static/js/sessions.js:1100`
- `static/js/sessions.js:1104`

## `_saveDateSectionCollapseState` — function, line 1091
- **called from:**
- `static/js/sessions.js:1091`
- `static/js/sessions.js:1107`

## `_dateSectionKey` — function, line 1095
- **called from:**
- `static/js/sessions.js:1095`
- `static/js/sessions.js:1100`
- `static/js/sessions.js:1105`

## `_isDateSectionCollapsed` — function, line 1099
- **called from:**
- `static/js/sessions.js:1099`
- `static/js/sessions.js:1115`
- `static/js/sessions.js:1143`
- `static/js/sessions.js:1154`

## `_toggleDateSection` — function, line 1103
- **called from:**
- `static/js/sessions.js:1103`
- `static/js/sessions.js:1125`
- `static/js/sessions.js:1131`

## `_createDateSectionHeader` — function, line 1111
- **called from:**
- `static/js/sessions.js:1111`
- `static/js/sessions.js:1142`
- `static/js/sessions.js:1153`

## `_appendSessionItemsWithDateHeaders` — function, line 1136
- **called from:**
- `static/js/sessions.js:1136`
- `static/js/sessions.js:1233`
- `static/js/sessions.js:1386`
- `static/js/sessions.js:1486`

## `_appendFavoriteSessionItems` — function, line 1151
- **called from:**
- `static/js/sessions.js:1151`
- `static/js/sessions.js:1232`

## `renderSessionList` — function, line 1161
- **called from:**
- `static/js/keyboard-shortcuts.js:190`
- `static/js/sessions.js:428`
- `static/js/sessions.js:612`
- `static/js/sessions.js:652`
- `static/js/sessions.js:658`
- `static/js/sessions.js:774`
- `static/js/sessions.js:808`
- `static/js/sessions.js:953`
- `static/js/sessions.js:959`
- `static/js/sessions.js:1108`
- `static/js/sessions.js:1161`
- `static/js/sessions.js:1243`
- `static/js/sessions.js:1353`
- `static/js/sessions.js:1396`
- `static/js/sessions.js:1470`
- `static/js/sessions.js:1498`
- `static/js/sessions.js:1793`
- `static/js/sessions.js:3745`
- `static/js/sessions.js:3752`

## `_renderSessionListImpl` — function, line 1167
- **called from:**
- `static/js/sessions.js:1167`

## `starPartition` — arrow, line 1269
- **called from:**
- `static/js/sessions.js:1275`
- `static/js/sessions.js:1276`

## `_postRenderSessionList` — function, line 1511
- **called from:**
- `static/js/sessions.js:1250`
- `static/js/sessions.js:1507`
- `static/js/sessions.js:1511`

## `_initKeyboardNav` — function, line 1526
- **called from:**
- `static/js/sessions.js:1520`
- `static/js/sessions.js:1526`

## `_initSwipeToDelete` — function, line 1537
- **called from:**
- `static/js/sessions.js:1521`
- `static/js/sessions.js:1537`

## `_showSwipeHint` — function, line 1541
- **called from:**
- `static/js/sessions.js:1523`
- `static/js/sessions.js:1541`

## `_forceSidebarOpen` — function, line 1558
- **called from:**
- `static/js/sessions.js:651`
- `static/js/sessions.js:658`
- `static/js/sessions.js:929`
- `static/js/sessions.js:952`
- `static/js/sessions.js:959`
- `static/js/sessions.js:971`
- `static/js/sessions.js:994`
- `static/js/sessions.js:1005`
- `static/js/sessions.js:1012`
- `static/js/sessions.js:1558`

## `_guardSidebarDuringRename` — function, line 1579
- **called from:**
- `static/js/sessions.js:641`
- `static/js/sessions.js:942`
- `static/js/sessions.js:1579`

## `_enterSelectMode` — function, line 1600
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

## `_exitSelectMode` — function, line 1631
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

## `_updateBulkCount` — function, line 1644
- **called from:**
- `static/js/cookbook.js:2272`
- `static/js/cookbook.js:2283`
- `static/js/cookbook.js:2287`
- `static/js/gallery.js:2488`
- `static/js/gallery.js:2517`
- `static/js/gallery.js:2529`
- `static/js/gallery.js:2538`
- `static/js/gallery.js:2568`
- `static/js/sessions.js:863`
- `static/js/sessions.js:1624`
- `static/js/sessions.js:1628`
- `static/js/sessions.js:1644`
- `static/js/sessions.js:1701`

## `_initBulkSelect` — function, line 1652
- **called from:**
- `static/js/sessions.js:1652`
- `static/js/sessions.js:2905`

## `_toggleAll` — arrow, line 1685
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_animateSessionRowsRemoving` — function, line 1747
- **called from:**
- `static/js/sessions.js:1738`
- `static/js/sessions.js:1747`
- `static/js/sessions.js:3072`
- `static/js/sessions.js:3115`

## `loadSessions` — function, line 1760
- **called from:**
- `static/app.js:620`
- `static/app.js:1464`
- `static/app.js:1669`
- `static/app.js:3418`
- `static/app.js:4327`
- `static/app.js:4423`
- `static/js/chat.js:2516`
- `static/js/chat.js:3637`
- `static/js/chat.js:4180`
- `static/js/chat.js:5051`
- `static/js/chat.js:5220`
- `static/js/chat.js:5892`
- `static/js/chat.js:5976`
- `static/js/chat.js:6941`
- `static/js/chat.js:7610`
- `static/js/chatRenderer.js:1265`
- `static/js/document.js:7316`
- `static/js/documentLibrary.js:2296`
- `static/js/documentLibrary.js:2790`
- `static/js/emailInbox.js:1379`
- `static/js/group.js:692`
- `static/js/keyboard-shortcuts.js:208`
- `static/js/keyboard-shortcuts.js:240`
- `static/js/presets.js:433`
- `static/js/research/panel.js:1230`
- `static/js/sessions.js:1000`
- `static/js/sessions.js:1013`
- `static/js/sessions.js:1338`
- `static/js/sessions.js:1367`
- `static/js/sessions.js:1461`
- `static/js/sessions.js:1720`
- `static/js/sessions.js:1741`
- `static/js/sessions.js:1760`
- `static/js/sessions.js:1834`
- `static/js/sessions.js:2450`
- `static/js/sessions.js:2553`
- `static/js/sessions.js:2593`
- `static/js/sessions.js:3063`
- `static/js/sessions.js:3097`
- `static/js/sessions.js:3407`
- `static/js/sessions.js:3424`
- `static/js/sessions.js:3477`
- `static/js/sessions.js:3478`
- `static/js/sessions.js:3507`
- `static/js/slashCommands.js:1013`
- `static/js/slashCommands.js:1038`
- `static/js/slashCommands.js:1055`
- `static/js/slashCommands.js:1070`
- `static/js/slashCommands.js:1080`
- `static/js/slashCommands.js:1113`
- `static/js/slashCommands.js:1166`
- `static/js/startupShell.js:142`
- `static/js/tasks.js:2587`

## `_isTransient` — arrow, line 1807
- **called from:**
- `static/js/sessions.js:1808`
- `static/js/sessions.js:1824`

## `selectSession` — function, line 1926
- **called from:**
- `static/app.js:360`
- `static/app.js:3420`
- `static/app.js:3788`
- `static/app.js:4421`
- `static/js/assistant.js:5`
- `static/js/assistant.js:30`
- `static/js/chat.js:277`
- `static/js/chat.js:426`
- `static/js/chat.js:786`
- `static/js/chat.js:3635`
- `static/js/chat.js:5049`
- `static/js/chat.js:5431`
- `static/js/chat.js:5891`
- `static/js/chat.js:5974`
- `static/js/chat.js:6395`
- `static/js/chat.js:6942`
- `static/js/chatRenderer.js:1266`
- `static/js/chatRenderer.js:2246`
- `static/js/chatStream.js:265`
- `static/js/chatStream.js:291`
- `static/js/chatStream.js:313`
- `static/js/documentLibrary.js:1007`
- `static/js/documentLibrary.js:1020`
- `static/js/documentLibrary.js:2011`
- `static/js/documentLibrary.js:2120`
- `static/js/documentLibrary.js:2475`
- `static/js/documentLibrary.js:2791`
- `static/js/emailInbox.js:1380`
- `static/js/gallery.js:1529`
- `static/js/group.js:693`
- `static/js/keyboard-shortcuts.js:210`
- `static/js/keyboard-shortcuts.js:241`
- `static/js/notes.js:4461`
- `static/js/presets.js:434`
- `static/js/research/panel.js:1231`
- `static/js/search-chat.js:136`
- `static/js/sessions.js:717`
- `static/js/sessions.js:1883`
- `static/js/sessions.js:1926`
- `static/js/sessions.js:2572`
- `static/js/sessions.js:2601`
- `static/js/sessions.js:2649`
- `static/js/sessions.js:2870`
- `static/js/sessions.js:2876`
- `static/js/sessions.js:3471`
- `static/js/sessions.js:3476`
- `static/js/sessions.js:3538`
- `static/js/sessions.js:3545`
- `static/js/slashCommands.js:1014`
- `static/js/slashCommands.js:1114`
- `static/js/slashCommands.js:1155`
- `static/js/slashCommands.js:2076`
- `static/js/tasks.js:2588`

## `_getPreferredDefaultChat` — function, line 2277
- **called from:**
- `static/js/sessions.js:1906`
- `static/js/sessions.js:2277`

## `createDirectChat` — function, line 2302
- **called from:**
- `static/app.js:245`
- `static/app.js:253`
- `static/app.js:259`
- `static/app.js:266`
- `static/app.js:4060`
- `static/js/chat.js:1795`
- `static/js/cookbookRunning.js:568`
- `static/js/cookbookRunning.js:3688`
- `static/js/documentLibrary.js:1059`
- `static/js/gallery.js:1544`
- `static/js/modelPicker.js:694`
- `static/js/models.js:84`
- `static/js/sessions.js:1908`
- `static/js/sessions.js:2302`
- `static/js/slashCommands.js:709`

## `materializePendingSession` — function, line 2377
- **called from:**
- `static/app.js:610`
- `static/app.js:2014`
- `static/js/chat.js:1750`
- `static/js/chat.js:1761`
- `static/js/chat.js:1797`
- `static/js/document.js:7291`
- `static/js/documentLibrary.js:1048`
- `static/js/documentLibrary.js:1060`
- `static/js/sessions.js:2377`
- `static/js/sessions.js:2472`

## `materializePromise` — arrow, line 2382
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `preMaterializePendingSession` — function, line 2464
- **called from:**
- `static/js/sessions.js:2464`

## `hasPendingChat` — function, line 2477
- **called from:**
- `static/app.js:586`
- `static/app.js:2013`
- `static/js/chat.js:415`
- `static/js/chat.js:1748`
- `static/js/document.js:7290`
- `static/js/documentLibrary.js:1047`
- `static/js/sessions.js:2477`

## `getPendingChat` — function, line 2478
- **called from:**
- `static/app.js:243`
- `static/js/admin.js:427`
- `static/js/chat.js:487`
- `static/js/chat.js:1727`
- `static/js/chat.js:1759`
- `static/js/modelPicker.js:130`
- `static/js/modelPicker.js:147`
- `static/js/modelPicker.js:173`
- `static/js/modelPicker.js:665`
- `static/js/modelPicker.js:736`
- `static/js/modelPicker.js:874`
- `static/js/modelPicker.js:938`
- `static/js/sessions.js:2478`

## `getCurrentSessionId` — function, line 2480
- **called from:**
- `static/app.js:250`
- `static/app.js:519`
- `static/app.js:545`
- `static/app.js:583`
- `static/app.js:610`
- `static/app.js:837`
- `static/app.js:1650`
- `static/app.js:1662`
- `static/app.js:2011`
- `static/app.js:2015`
- `static/app.js:2564`
- `static/app.js:3405`
- `static/app.js:3740`
- `static/app.js:4057`
- `static/app.js:4419`
- `static/js/chat.js:267`
- `static/js/chat.js:292`
- `static/js/chat.js:308`
- `static/js/chat.js:367`
- `static/js/chat.js:400`
- `static/js/chat.js:430`
- `static/js/chat.js:691`
- `static/js/chat.js:999`
- `static/js/chat.js:1481`
- `static/js/chat.js:1505`
- `static/js/chat.js:1611`
- `static/js/chat.js:1752`
- `static/js/chat.js:1755`
- `static/js/chat.js:1762`
- `static/js/chat.js:1767`
- `static/js/chat.js:1799`
- `static/js/chat.js:1851`
- `static/js/chat.js:1959`
- `static/js/chat.js:2048`
- `static/js/chat.js:3162`
- `static/js/chat.js:3527`
- `static/js/chat.js:3604`
- `static/js/chat.js:3634`
- `static/js/chat.js:4479`
- `static/js/chat.js:4481`
- `static/js/chat.js:4777`
- `static/js/chat.js:4811`
- `static/js/chat.js:4991`
- `static/js/chat.js:5048`
- `static/js/chat.js:5138`
- `static/js/chat.js:5196`
- `static/js/chat.js:5236`
- `static/js/chat.js:5238`
- `static/js/chat.js:5288`
- `static/js/chat.js:5340`
- `static/js/chat.js:5342`
- `static/js/chat.js:5405`
- `static/js/chat.js:5476`
- `static/js/chat.js:5648`
- `static/js/chat.js:5682`
- `static/js/chat.js:5739`
- `static/js/chat.js:5857`
- `static/js/chat.js:5955`
- `static/js/chat.js:5973`
- `static/js/chat.js:6098`
- … +65 more (grep the name in repo)

## `isCurrentSessionIncognito` — function, line 2484
- **called from:**
- `static/js/sessions.js:2484`

## `getSessions` — function, line 2488
- **called from:**
- `static/app.js:249`
- `static/app.js:519`
- `static/app.js:547`
- `static/app.js:588`
- `static/app.js:616`
- `static/app.js:1662`
- `static/app.js:3407`
- `static/app.js:4056`
- `static/js/chat.js:700`
- `static/js/chat.js:1482`
- `static/js/chat.js:2623`
- `static/js/chat.js:4330`
- `static/js/chat.js:4481`
- `static/js/chat.js:5617`
- `static/js/chat.js:5939`
- `static/js/chat.js:6991`
- `static/js/chat.js:7027`
- `static/js/chatStream.js:278`
- `static/js/document.js:7297`
- `static/js/documentLibrary.js:1054`
- `static/js/group.js:141`
- `static/js/keyboard-shortcuts.js:183`
- `static/js/keyboard-shortcuts.js:198`
- `static/js/keyboard-shortcuts.js:203`
- `static/js/keyboard-shortcuts.js:227`
- `static/js/modelPicker.js:702`
- `static/js/modelPicker.js:734`
- `static/js/modelPicker.js:873`
- `static/js/presets.js:404`
- `static/js/sessions.js:2488`
- `static/js/slashCommands.js:950`
- `static/js/slashCommands.js:958`
- `static/js/slashCommands.js:1029`
- `static/js/slashCommands.js:1049`
- `static/js/slashCommands.js:1065`
- `static/js/slashCommands.js:1135`
- `static/js/slashCommands.js:1150`
- `static/js/slashCommands.js:1180`
- `static/js/slashCommands.js:1227`
- `static/js/slashCommands.js:2016`

## `getCurrentModel` — function, line 2492
- **called from:**
- `static/js/chat.js:483`
- `static/js/chat.js:1737`
- `static/js/chat.js:6071`
- `static/js/cookbookRunning.js:556`
- `static/js/document.js:4252`
- `static/js/document.js:7296`
- `static/js/documentLibrary.js:1053`
- `static/js/emailInbox.js:839`
- `static/js/sessions.js:2492`
- `static/js/skills.js:1218`
- `static/js/slashCommands.js:1538`

## `getCurrentEndpointUrl` — function, line 2501
- **called from:**
- `static/js/chat.js:1738`
- `static/js/chat.js:6072`
- `static/js/chatRenderer.js:754`
- `static/js/chatRenderer.js:865`
- `static/js/sessions.js:2501`
- `static/js/skills.js:1219`
- `static/js/slashCommands.js:1539`
- `static/js/slashCommands.js:2030`

## `setCurrentSessionId` — function, line 2508
- **called from:**
- `static/app.js:843`
- `static/app.js:2618`
- `static/js/chat.js:428`
- `static/js/document.js:7314`
- `static/js/group.js:163`
- `static/js/group.js:691`
- `static/js/keyboard-shortcuts.js:212`
- `static/js/sessions.js:2508`

## `deleteCurrentSessionFromTopMenu` — function, line 2522
- **called from:**
- `static/app.js:572`
- `static/js/sessions.js:2522`

## `_onSessionListKeydown` — function, line 2558
- **called from:**
- `static/js/sessions.js:2558`

## `initDragSort` — function, line 2607
- **called from:**
- `static/js/sessions.js:1522`
- `static/js/sessions.js:2607`

## `_updateResearchDots` — function, line 2654
- **called from:**
- `static/js/sessions.js:2654`
- `static/js/sessions.js:2692`
- `static/js/sessions.js:2702`
- `static/js/sessions.js:2709`
- `static/js/sessions.js:2715`
- `static/js/sessions.js:2721`
- `static/js/sessions.js:2731`
- `static/js/sessions.js:2741`
- `static/js/sessions.js:2746`
- `static/js/sessions.js:2757`
- `static/js/sessions.js:2891`

## `_startResearchPolling` — function, line 2672
- **called from:**
- `static/js/sessions.js:2672`
- `static/js/sessions.js:2704`

## `markResearching` — function, line 2700
- **called from:**
- `static/js/chat.js:3528`
- `static/js/chat.js:7061`
- `static/js/sessions.js:2700`

## `clearResearching` — function, line 2707
- **called from:**
- `static/js/chat.js:3598`
- `static/js/chat.js:3605`
- `static/js/chat.js:3626`
- `static/js/chat.js:6960`
- `static/js/chat.js:6968`
- `static/js/chat.js:7123`
- `static/js/chat.js:7139`
- `static/js/sessions.js:2707`

## `markStreaming` — function, line 2713
- **called from:**
- `static/js/chat.js:3180`
- `static/js/chat.js:5532`
- `static/js/sessions.js:2713`

## `clearStreaming` — function, line 2719
- **called from:**
- `static/js/chat.js:4825`
- `static/js/chat.js:4853`
- `static/js/chat.js:4858`
- `static/js/chat.js:5534`
- `static/js/sessions.js:2719`

## `_clearRunningState` — function, line 2725
- **called from:**
- `static/js/sessions.js:2725`
- `static/js/sessions.js:2807`
- `static/js/sessions.js:2812`

## `markStreamComplete` — function, line 2736
- **called from:**
- `static/js/chat.js:3205`
- `static/js/notes.js:4531`
- `static/js/notes.js:4601`
- `static/js/sessions.js:2736`

## `setTimeout` — method?, line 2755
- **called from:**
- `static/app.js:288`
- `static/app.js:810`
- `static/app.js:1194`
- `static/app.js:1195`
- `static/app.js:1230`
- `static/app.js:1231`
- `static/app.js:1851`
- `static/app.js:2109`
- `static/app.js:2113`
- `static/app.js:2195`
- `static/app.js:2969`
- `static/app.js:3317`
- `static/app.js:3461`
- `static/app.js:3662`
- `static/app.js:3709`
- `static/app.js:3874`
- `static/app.js:4004`
- `static/app.js:4162`
- `static/app.js:4343`
- `static/app.js:4348`
- `static/app.js:4414`
- `static/app.js:4496`
- `static/js/admin.js:475`
- `static/js/admin.js:599`
- `static/js/admin.js:1232`
- `static/js/admin.js:1429`
- `static/js/admin.js:2262`
- `static/js/admin.js:2461`
- `static/js/admin.js:2629`
- `static/js/admin.js:2674`
- `static/js/admin.js:2719`
- `static/js/admin.js:2812`
- `static/js/admin.js:2829`
- `static/js/assistant.js:396`
- `static/js/calendar.js:45`
- `static/js/calendar.js:496`
- `static/js/calendar.js:824`
- `static/js/calendar.js:865`
- `static/js/calendar.js:869`
- `static/js/calendar.js:2021`
- `static/js/calendar.js:2027`
- `static/js/calendar.js:2216`
- `static/js/calendar.js:2230`
- `static/js/calendar.js:2245`
- `static/js/calendar.js:2247`
- `static/js/calendar.js:2632`
- `static/js/calendar.js:2655`
- `static/js/calendar.js:3127`
- `static/js/censor.js:120`
- `static/js/censor.js:122`
- `static/js/chat.js:73`
- `static/js/chat.js:243`
- `static/js/chat.js:517`
- `static/js/chat.js:794`
- `static/js/chat.js:807`
- `static/js/chat.js:1198`
- `static/js/chat.js:1229`
- `static/js/chat.js:1258`
- `static/js/chat.js:1387`
- `static/js/chat.js:1400`
- … +541 more (grep the name in repo)

## `_updateRailNotifs` — function, line 2764
- **called from:**
- `static/js/research/panel.js:119`
- `static/js/sessions.js:2703`
- `static/js/sessions.js:2710`
- `static/js/sessions.js:2716`
- `static/js/sessions.js:2722`
- `static/js/sessions.js:2732`
- `static/js/sessions.js:2742`
- `static/js/sessions.js:2747`
- `static/js/sessions.js:2764`
- `static/js/sessions.js:2892`

## `_checkServerStream` — function, line 2797
- **called from:**
- `static/js/sessions.js:2215`
- `static/js/sessions.js:2797`

## `clearStreamComplete` — function, line 2884
- **called from:**
- `static/js/chat.js:1959`
- `static/js/sessions.js:2204`
- `static/js/sessions.js:2884`

## `_initAllDropdowns` — function, line 2896
- **called from:**
- `static/js/sessions.js:2896`
- `static/js/sessions.js:2910`

## `_initDropdownDismiss` — function, line 2914
- **called from:**
- `static/js/sessions.js:2904`
- `static/js/sessions.js:2914`

## `_showDropdown` — function, line 2949
- **called from:**
- `static/js/sessions.js:2949`
- `static/js/sessions.js:3242`
- `static/js/sessions.js:3475`
- `static/js/sessions.js:3506`
- `static/js/sessions.js:3544`
- `static/js/sessions.js:3591`

## `close` — function, line 2980
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

## `_arcRelativeTime` — function, line 2993
- **called from:**
- `static/js/sessions.js:2993`
- `static/js/sessions.js:3222`
- `static/js/sessions.js:3622`

## `_arcPeekOpen` — function, line 3010
- **called from:**
- `static/js/sessions.js:3010`
- `static/js/sessions.js:3243`
- `static/js/sessions.js:3257`

## `_checkPeekCleanup` — function, line 3050
- **called from:**
- `static/js/sessions.js:1948`
- `static/js/sessions.js:3050`

## `_arcRestore` — function, line 3056
- **called from:**
- `static/js/sessions.js:3056`
- `static/js/sessions.js:3244`

## `_arcDelete` — function, line 3067
- **called from:**
- `static/js/sessions.js:3067`
- `static/js/sessions.js:3245`

## `_arcRemove` — function, line 3079
- **called from:**
- `static/js/sessions.js:3060`
- `static/js/sessions.js:3073`
- `static/js/sessions.js:3079`
- `static/js/sessions.js:3091`
- `static/js/sessions.js:3111`

## `_arcBulkRestore` — function, line 3085
- **called from:**
- `static/js/sessions.js:3085`

## `_arcBulkDelete` — function, line 3100
- **called from:**
- `static/js/sessions.js:3100`

## `_arcToggleSelectMode` — function, line 3121
- **called from:**
- `static/js/sessions.js:3121`

## `_arcUpdateBulkBar` — function, line 3127
- **called from:**
- `static/js/sessions.js:3127`
- `static/js/sessions.js:3174`
- `static/js/sessions.js:3237`
- `static/js/sessions.js:3255`

## `_arcFetch` — function, line 3141
- **called from:**
- `static/js/sessions.js:3141`
- `static/js/sessions.js:3196`
- `static/js/sessions.js:3706`
- `static/js/sessions.js:3709`
- `static/js/sessions.js:3711`
- `static/js/sessions.js:3722`

## `_arcRefreshUI` — function, line 3169
- **called from:**
- `static/js/sessions.js:3061`
- `static/js/sessions.js:3074`
- `static/js/sessions.js:3095`
- `static/js/sessions.js:3117`
- `static/js/sessions.js:3124`
- `static/js/sessions.js:3161`
- `static/js/sessions.js:3169`
- `static/js/sessions.js:3718`

## `_arcRenderStats` — function, line 3177
- **called from:**
- `static/js/sessions.js:3170`
- `static/js/sessions.js:3177`

## `_arcRenderChips` — function, line 3182
- **called from:**
- `static/js/sessions.js:3171`
- `static/js/sessions.js:3182`

## `mkChip` — arrow, line 3192
- **called from:**
- `static/js/sessions.js:3199`
- `static/js/sessions.js:3200`
- `static/js/tasks.js:784`
- `static/js/tasks.js:785`

## `_arcRenderCard` — function, line 3203
- **called from:**
- `static/js/sessions.js:3203`
- `static/js/sessions.js:3271`

## `_arcRenderGrid` — function, line 3263
- **called from:**
- `static/js/sessions.js:3172`
- `static/js/sessions.js:3263`

## `_arcRenderLoadMore` — function, line 3274
- **called from:**
- `static/js/sessions.js:3173`
- `static/js/sessions.js:3274`

## `openLibrary` — function, line 3285
- **called from:**
- `static/app.js:1049`
- `static/app.js:1236`
- `static/app.js:1251`
- `static/app.js:1277`
- `static/app.js:1284`
- `static/js/document.js:5198`
- `static/js/document.js:9554`
- `static/js/document.js:9658`
- `static/js/documentLibrary.js:1573`
- `static/js/research/panel.js:686`
- `static/js/research/panel.js:734`
- `static/js/research/panel.js:794`
- `static/js/sessions.js:3285`
- `static/js/sessions.js:3288`
- `static/js/sessions.js:3347`
- `static/js/slashCommands.js:4602`

## `_updateLibCount` — function, line 3431
- **called from:**
- `static/js/sessions.js:3392`
- `static/js/sessions.js:3431`
- `static/js/sessions.js:3636`
- `static/js/sessions.js:3643`

## `_renderLibGrid` — function, line 3436
- **called from:**
- `static/js/sessions.js:3364`
- `static/js/sessions.js:3372`
- `static/js/sessions.js:3375`
- `static/js/sessions.js:3383`
- `static/js/sessions.js:3408`
- `static/js/sessions.js:3425`
- `static/js/sessions.js:3428`
- `static/js/sessions.js:3436`
- `static/js/sessions.js:3477`
- `static/js/sessions.js:3478`
- `static/js/sessions.js:3507`
- `static/js/sessions.js:3508`
- `static/js/sessions.js:3546`
- `static/js/sessions.js:3603`

## `_renderLibChats` — function, line 3446
- **called from:**
- `static/js/documentLibrary.js:1879`
- `static/js/documentLibrary.js:1896`
- `static/js/documentLibrary.js:2032`
- `static/js/documentLibrary.js:2053`
- `static/js/documentLibrary.js:2122`
- `static/js/documentLibrary.js:2129`
- `static/js/documentLibrary.js:2225`
- `static/js/documentLibrary.js:2270`
- `static/js/documentLibrary.js:2297`
- `static/js/sessions.js:3440`
- `static/js/sessions.js:3446`

## `_renderLibArchive` — function, line 3485
- **called from:**
- `static/js/documentLibrary.js:1880`
- `static/js/documentLibrary.js:2038`
- `static/js/documentLibrary.js:2053`
- `static/js/documentLibrary.js:2321`
- `static/js/documentLibrary.js:2392`
- `static/js/documentLibrary.js:2397`
- `static/js/documentLibrary.js:2477`
- `static/js/documentLibrary.js:2481`
- `static/js/documentLibrary.js:2524`
- `static/js/documentLibrary.js:2525`
- `static/js/documentLibrary.js:2562`
- `static/js/documentLibrary.js:2563`
- `static/js/documentLibrary.js:2647`
- `static/js/documentLibrary.js:2668`
- `static/js/documentLibrary.js:2822`
- `static/js/documentLibrary.js:2841`
- `static/js/sessions.js:3441`
- `static/js/sessions.js:3485`

## `_renderLibDocuments` — function, line 3516
- **called from:**
- `static/js/sessions.js:3442`
- `static/js/sessions.js:3516`

## `_renderLibResearch` — function, line 3554
- **called from:**
- `static/js/documentLibrary.js:1881`
- `static/js/documentLibrary.js:2678`
- `static/js/documentLibrary.js:3076`
- `static/js/sessions.js:3443`
- `static/js/sessions.js:3554`

## `_buildLibCard` — function, line 3613
- **called from:**
- `static/js/sessions.js:3467`
- `static/js/sessions.js:3499`
- `static/js/sessions.js:3530`
- `static/js/sessions.js:3576`
- `static/js/sessions.js:3613`

## `_toggleLibSelect` — function, line 3641
- **called from:**
- `static/js/sessions.js:3470`
- `static/js/sessions.js:3502`
- `static/js/sessions.js:3534`
- `static/js/sessions.js:3641`

## `closeLibrary` — function, line 3646
- **called from:**
- `static/app.js:1047`
- `static/js/documentLibrary.js:999`
- `static/js/documentLibrary.js:1015`
- `static/js/documentLibrary.js:1105`
- `static/js/documentLibrary.js:2012`
- `static/js/documentLibrary.js:2793`
- `static/js/documentLibrary.js:3237`
- `static/js/documentLibrary.js:3366`
- `static/js/documentLibrary.js:3377`
- `static/js/documentLibrary.js:3391`
- `static/js/sessions.js:3346`
- `static/js/sessions.js:3471`
- `static/js/sessions.js:3476`
- `static/js/sessions.js:3537`
- `static/js/sessions.js:3545`
- `static/js/sessions.js:3646`

## `openArchive` — function, line 3660
- **called from:**
- `static/js/sessions.js:2990`
- `static/js/sessions.js:3660`

## `closeArchive` — function, line 3725
- **called from:**
- `static/js/sessions.js:3013`
- `static/js/sessions.js:3720`
- `static/js/sessions.js:3725`

## `getSortMode` — function, line 3740
- **called from:**
- `static/app.js:1391`
- `static/app.js:1408`
- `static/js/sessions.js:3740`

## `setSortMode` — function, line 3741
- **called from:**
- `static/app.js:1394`
- `static/app.js:1398`
- `static/app.js:1441`
- `static/js/sessions.js:468`
- `static/js/sessions.js:492`
- `static/js/sessions.js:3741`

## `setSessionHasDocs` — function, line 3748
- **called from:**
- `static/js/document.js:201`
- `static/js/sessions.js:3748`
