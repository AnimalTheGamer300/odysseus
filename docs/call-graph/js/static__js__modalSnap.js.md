# `static/js/modalSnap.js` — definitions & call sites

73 definitions (regex-based, best-effort).
**Exports:** `applyEdgeDock`, `applyRightDock`, `clearDockSide`, `clearRightDock`, `collapseSidebarToRail`, `makeEdgeDockController`, `makeRightDockController`, `resumeDock`, `suspendDock`

## `_positionEdgeDockResizeHandles` — function, line 29
- **called from:**
- `static/js/modalSnap.js:29`
- `static/js/modalSnap.js:59`
- `static/js/modalSnap.js:512`
- `static/js/modalSnap.js:594`
- `static/js/modalSnap.js:668`
- `static/js/modalSnap.js:713`
- `static/js/modalSnap.js:899`
- `static/js/modalSnap.js:983`
- `static/js/modalSnap.js:989`

## `_dockClassForSide` — function, line 33
- **called from:**
- `static/js/modalSnap.js:33`
- `static/js/modalSnap.js:38`
- `static/js/modalSnap.js:359`
- `static/js/modalSnap.js:837`
- `static/js/tileManager.js:32`
- `static/js/tileManager.js:37`

## `_hasOtherDockedWindow` — function, line 37
- **called from:**
- `static/js/modalSnap.js:37`
- `static/js/modalSnap.js:48`
- `static/js/modalSnap.js:48`
- `static/js/modalSnap.js:53`
- `static/js/modalSnap.js:566`
- `static/js/modalSnap.js:618`
- `static/js/modalSnap.js:706`
- `static/js/tileManager.js:36`
- `static/js/tileManager.js:48`

## `_hasAnyOtherDockedWindow` — function, line 47
- **called from:**
- `static/js/modalSnap.js:47`
- `static/js/modalSnap.js:569`
- `static/js/modalSnap.js:628`
- `static/js/modalSnap.js:709`

## `clearDockSide` — function, line 51
- **called from:**
- `static/js/modalSnap.js:51`
- `static/js/modalSnap.js:362`
- `static/js/modalSnap.js:562`
- `static/js/modalSnap.js:563`
- `static/js/modalSnap.js:617`
- `static/js/modalSnap.js:694`
- `static/js/notes.js:186`
- `static/js/notes.js:187`
- `static/js/settings/lifecycle.js:37`
- `static/js/settings/lifecycle.js:38`

## `_defaultDockWidth` — function, line 63
- **called from:**
- `static/js/modalSnap.js:63`
- `static/js/modalSnap.js:127`
- `static/js/modalSnap.js:149`

## `_dockWidthStorageKey` — function, line 67
- **called from:**
- `static/js/modalSnap.js:67`
- `static/js/modalSnap.js:73`
- `static/js/modalSnap.js:84`

## `_storedDockWidth` — function, line 72
- **called from:**
- `static/js/modalSnap.js:72`
- `static/js/modalSnap.js:127`
- `static/js/modalSnap.js:131`

## `_saveDockWidth` — function, line 83
- **called from:**
- `static/js/modalSnap.js:83`
- `static/js/modalSnap.js:967`

## `_minEdgeDockWidth` — function, line 89
- **called from:**
- `static/js/modalSnap.js:89`
- `static/js/modalSnap.js:110`
- `static/js/modalSnap.js:119`

## `_activeDockWidth` — function, line 93
- **called from:**
- `static/js/modalSnap.js:93`
- `static/js/modalSnap.js:112`
- `static/js/modalSnap.js:120`
- `static/js/modalSnap.js:169`

## `_clampDockWidthToSpace` — function, line 103
- **called from:**
- `static/js/modalSnap.js:103`
- `static/js/modalSnap.js:115`
- `static/js/modalSnap.js:123`

## `_clampRightDockWidth` — function, line 109
- **called from:**
- `static/js/modalSnap.js:109`
- `static/js/modalSnap.js:127`
- `static/js/modalSnap.js:872`

## `_clampLeftDockWidth` — function, line 118
- **called from:**
- `static/js/modalSnap.js:118`
- `static/js/modalSnap.js:131`
- `static/js/modalSnap.js:886`

## `_resolveRightDockWidth` — function, line 126
- **called from:**
- `static/js/modalSnap.js:126`
- `static/js/modalSnap.js:498`

## `_resolveLeftDockWidth` — function, line 130
- **called from:**
- `static/js/modalSnap.js:130`
- `static/js/modalSnap.js:282`

## `_isEmailDockOwner` — function, line 134
- **called from:**
- `static/js/modalSnap.js:134`
- `static/js/modalSnap.js:291`

## `_showSnapHint` — function, line 139
- **called from:**
- `static/js/modalSnap.js:139`
- `static/js/modalSnap.js:770`
- `static/js/modalSnap.js:777`
- `static/js/modalSnap.js:782`
- `static/js/windowDrag.js:239`
- `static/js/windowDrag.js:253`

## `_shouldAutoCollapseSidebar` — function, line 159
- **called from:**
- `static/js/modalSnap.js:159`
- `static/js/modalSnap.js:505`
- `static/js/modalSnap.js:880`

## `_leftNavRight` — function, line 176
- **called from:**
- `static/js/modalSnap.js:111`
- `static/js/modalSnap.js:118`
- `static/js/modalSnap.js:130`
- `static/js/modalSnap.js:176`
- `static/js/modalSnap.js:191`
- `static/js/modalSnap.js:279`
- `static/js/modalSnap.js:745`
- `static/js/modalSnap.js:885`
- `static/js/modalSnap.js:1032`
- `static/js/modalSnap.js:1065`

## `_clampEmailDocSplitWidth` — function, line 191
- **called from:**
- `static/js/modalSnap.js:191`
- `static/js/modalSnap.js:265`
- `static/js/modalSnap.js:1033`

## `_storedEmailDocSplitWidth` — function, line 201
- **called from:**
- `static/js/modalSnap.js:201`
- `static/js/modalSnap.js:264`

## `_saveEmailDocSplitWidth` — function, line 211
- **called from:**
- `static/js/modalSnap.js:211`
- `static/js/modalSnap.js:1066`

## `_disconnectLeftDockObservers` — function, line 215
- **called from:**
- `static/js/modalSnap.js:215`
- `static/js/modalSnap.js:557`
- `static/js/modalSnap.js:623`
- `static/js/modalSnap.js:696`

## `_applyEmailDocSplitGeometry` — function, line 225
- **called from:**
- `static/js/modalSnap.js:225`
- `static/js/modalSnap.js:297`
- `static/js/modalSnap.js:1038`

## `_clearEmailDocSplitGeometry` — function, line 248
- **called from:**
- `static/js/modalSnap.js:248`
- `static/js/modalSnap.js:299`
- `static/js/modalSnap.js:567`
- `static/js/modalSnap.js:619`
- `static/js/modalSnap.js:700`
- `static/js/modalSnap.js:707`

## `_resolveEmailDocSplitWidth` — function, line 261
- **called from:**
- `static/js/modalSnap.js:131`
- `static/js/modalSnap.js:261`
- `static/js/modalSnap.js:281`

## `changes` — class, line 274
- **called from:**
- `static/js/admin.js:134`
- `static/js/calendar.js:3645`
- `static/js/cookbook-hwfit.js:237`
- `static/js/document.js:7897`
- `static/js/settings.js:1323`
- `static/js/tileManager.js:295`

## `_anchorLeftDock` — function, line 277
- **called from:**
- `static/js/modalSnap.js:277`
- `static/js/modalSnap.js:414`
- `static/js/modalSnap.js:430`

## `collapseSidebarToRail` — function, line 305
- **called from:**
- `static/js/emailLibrary.js:1120`
- `static/js/emailLibrary.js:1129`
- `static/js/modalSnap.js:305`

## `_collapseSidebarToRail` — function, line 306
- **called from:**
- `static/app.js:1179`
- `static/app.js:1203`
- `static/js/modalSnap.js:305`
- `static/js/modalSnap.js:306`
- `static/js/modalSnap.js:409`
- `static/js/modalSnap.js:506`
- `static/js/modalSnap.js:881`

## `_resolveDockNodes` — function, line 326
- **called from:**
- `static/js/modalSnap.js:326`
- `static/js/modalSnap.js:346`
- `static/js/modalSnap.js:608`
- `static/js/modalSnap.js:677`
- `static/js/modalSnap.js:722`
- `static/js/modalSnap.js:827`
- `static/js/modalSnap.js:860`
- `static/js/modalSnap.js:867`
- `static/js/modalSnap.js:914`
- `static/js/modalSnap.js:944`

## `applyEdgeDock` — function, line 335
- **called from:**
- `static/js/emailInbox.js:179`
- `static/js/emailInbox.js:245`
- `static/js/emailInbox.js:253`
- `static/js/modalManager.js:57`
- `static/js/modalSnap.js:335`
- `static/js/modalSnap.js:728`
- `static/js/notes.js:202`

## `applyRightDock` — function, line 341
- **called from:**
- `static/js/modalSnap.js:341`

## `_applyDockInternal` — function, line 345
- **called from:**
- `static/js/modalSnap.js:337`
- `static/js/modalSnap.js:342`
- `static/js/modalSnap.js:345`
- `static/js/modalSnap.js:779`

## `so` — class, line 356
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_doAnchor` — arrow, line 429
- **called from:**
- `static/js/modalSnap.js:434`

## `reanchor` — arrow, line 432
- **called from:**
- `static/js/modalSnap.js:453`

## `_bindDocResizeObs` — arrow, line 469
- **called from:**
- `static/js/modalSnap.js:456`
- `static/js/modalSnap.js:484`

## `onGone` — arrow, line 519
- **called from:**
- `static/js/modalSnap.js:528`
- `static/js/modalSnap.js:534`

## `flip` — class, line 520
- **called from:**
- `static/js/emailLibrary.js:7577`
- `static/js/emailLibrary.js:7579`

## `_isGone` — arrow, line 525
- **called from:**
- `static/js/modalSnap.js:528`

## `_onDockedModalGone` — function, line 548
- **called from:**
- `static/js/modalSnap.js:519`
- `static/js/modalSnap.js:548`

## `_expandSidebarFromRail` — function, line 597
- **called from:**
- `static/js/modalSnap.js:570`
- `static/js/modalSnap.js:597`
- `static/js/modalSnap.js:628`
- `static/js/modalSnap.js:710`

## `clearRightDock` — function, line 607
- **called from:**
- `static/js/modalManager.js:1332`
- `static/js/modalSnap.js:607`
- `static/js/modalSnap.js:762`

## `suspendDock` — function, line 676
- **called from:**
- `static/js/modalManager.js:1243`
- `static/js/modalManager.js:1530`
- `static/js/modalSnap.js:676`
- `static/js/modalSnap.js:718`

## `resumeDock` — function, line 721
- **called from:**
- `static/js/modalManager.js:1276`
- `static/js/modalSnap.js:674`
- `static/js/modalSnap.js:721`

## `makeRightDockController` — function, line 737
- **called from:**
- `static/js/modalSnap.js:737`

## `_leftNavWidth` — function, line 744
- **called from:**
- `static/js/modalSnap.js:744`
- `static/js/modalSnap.js:755`
- `static/js/windowDrag.js:50`
- `static/js/windowDrag.js:186`

## `makeEdgeDockController` — function, line 751
- **called from:**
- `static/js/modalSnap.js:738`
- `static/js/modalSnap.js:751`
- `static/js/windowDrag.js:95`
- `static/js/windowDrag.js:100`

## `_distFromEdge` — arrow, line 754
- **called from:**
- `static/js/modalSnap.js:761`
- `static/js/modalSnap.js:767`

## `onMove` — method?, line 759
- **called from:**
- `static/js/calendar.js:1587`
- `static/js/modalSnap.js:735`
- `static/js/modalSnap.js:759`
- `static/js/windowDrag.js:195`
- `static/js/windowDrag.js:200`
- `static/js/windowDrag.js:205`
- `static/js/windowDrag.js:206`
- `static/js/windowDrag.js:215`
- `static/js/windowDrag.js:223`
- `static/js/windowDrag.js:244`
- `static/js/windowDrag.js:245`

## `hovering` — method?, line 774
- **called from:**
- `static/js/modalSnap.js:734`
- `static/js/modalSnap.js:736`
- `static/js/modalSnap.js:750`
- `static/js/modalSnap.js:774`
- `static/js/windowDrag.js:261`
- `static/js/windowDrag.js:267`

## `side` — method?, line 775
- **called from:**
- `static/app.js:1539`
- `static/js/chat.js:4813`
- `static/js/document.js:6981`
- `static/js/modalSnap.js:350`
- `static/js/modalSnap.js:775`
- `static/js/notes.js:4496`
- `static/js/sidebar-layout.js:588`

## `commit` — method?, line 776
- **called from:**
- `app.py:449`
- `app.py:1047`
- `core/database.py:924`
- `core/database.py:955`
- `core/database.py:978`
- `core/database.py:1003`
- `core/database.py:1026`
- `core/database.py:1049`
- `core/database.py:1080`
- `core/database.py:1105`
- `core/database.py:1129`
- `core/database.py:1158`
- `core/database.py:1180`
- `core/database.py:1203`
- `core/database.py:1227`
- `core/database.py:1249`
- `core/database.py:1282`
- `core/database.py:1304`
- `core/database.py:1327`
- `core/database.py:1351`
- `core/database.py:1375`
- `core/database.py:1409`
- `core/database.py:1438`
- `core/database.py:1512`
- `core/database.py:1591`
- `core/database.py:1606`
- `core/database.py:1632`
- `core/database.py:1704`
- `core/database.py:1723`
- `core/database.py:1735`
- `core/database.py:1747`
- `core/database.py:1764`
- `core/database.py:1784`
- `core/database.py:1805`
- `core/database.py:1817`
- `core/database.py:1830`
- `core/database.py:1835`
- `core/database.py:1847`
- `core/database.py:1851`
- `core/database.py:2098`
- `core/database.py:2251`
- `core/database.py:2335`
- `core/database.py:2396`
- `core/database.py:2425`
- `core/database.py:2457`
- `core/database.py:2491`
- `core/database.py:2512`
- `core/database.py:2539`
- `core/database.py:2565`
- `core/database.py:2595`
- `core/database.py:2618`
- `core/database.py:2640`
- `core/database.py:2669`
- `core/database.py:2745`
- `core/database.py:2813`
- `core/session_manager.py:429`
- `core/session_manager.py:479`
- `core/session_manager.py:504`
- `core/session_manager.py:569`
- `core/session_manager.py:647`
- … +406 more (grep the name in repo)

## `release` — method?, line 781
- **called from:**
- `src/llm_core.py:142`
- `tests/test_task_scheduler_cancel.py:90`
- `static/js/init.js:410`
- `static/js/init.js:418`
- `static/js/modalSnap.js:734`
- `static/js/modalSnap.js:750`
- `static/js/modalSnap.js:781`
- `static/js/windowDrag.js:194`
- `static/js/windowDrag.js:199`
- `static/js/windowDrag.js:208`
- `static/js/windowDrag.js:209`
- `static/js/windowDrag.js:241`
- `static/js/windowDrag.js:242`
- `static/js/windowDrag.js:256`
- `static/js/windowDrag.js:257`
- `static/js/windowDrag.js:262`
- `static/js/windowDrag.js:268`
- `static/js/windowDrag.js:273`
- `static/js/windowDrag.js:274`

## `_initEdgeDockResizeHandles` — function, line 788
- **called from:**
- `static/js/modalSnap.js:788`

## `_setStyle` — arrow, line 799
- **called from:**
- `static/js/modalSnap.js:802`
- `static/js/modalSnap.js:929`
- `static/js/modalSnap.js:930`
- `static/js/modalSnap.js:931`

## `_hideHandle` — arrow, line 802
- **called from:**
- `static/js/modalSnap.js:910`
- `static/js/modalSnap.js:916`
- `static/js/modalSnap.js:920`
- `static/js/modalSnap.js:926`

## `_isUsableDockOwner` — arrow, line 823
- **called from:**
- `static/js/modalSnap.js:840`

## `_activeDockOwner` — arrow, line 836
- **called from:**
- `static/js/modalSnap.js:913`
- `static/js/modalSnap.js:939`

## `_zIndexFor` — arrow, line 845
- **called from:**
- `static/js/modalSnap.js:931`

## `_hasVisibleFloatingModal` — arrow, line 851
- **called from:**
- `static/js/modalSnap.js:919`

## `_setWidth` — arrow, line 866
- **called from:**
- `static/js/modalSnap.js:951`
- `static/js/modalSnap.js:954`

## `onMove` — arrow, line 952
- **called from:**
- `static/js/calendar.js:1587`
- `static/js/modalSnap.js:735`
- `static/js/modalSnap.js:759`
- `static/js/windowDrag.js:195`
- `static/js/windowDrag.js:200`
- `static/js/windowDrag.js:205`
- `static/js/windowDrag.js:206`
- `static/js/windowDrag.js:215`
- `static/js/windowDrag.js:223`
- `static/js/windowDrag.js:244`
- `static/js/windowDrag.js:245`

## `onUp` — arrow, line 956
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `schedulePosition` — arrow, line 979
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_initSplitSeamIndicator` — function, line 992
- **called from:**
- `static/js/modalSnap.js:992`

## `_activeLeftDockContent` — arrow, line 1008
- **called from:**
- `static/js/modalSnap.js:1030`

## `_position` — arrow, line 1018
- **called from:**
- `static/js/chat.js:6167`
- `static/js/chat.js:6176`
- `static/js/chat.js:6199`
- `static/js/chat.js:6200`
- `static/js/modalSnap.js:1039`
- `static/js/modalSnap.js:1078`
- `static/js/slashAutocomplete.js:141`
- `static/js/slashAutocomplete.js:211`
- `static/js/slashAutocomplete.js:299`

## `_dragTo` — arrow, line 1029
- **called from:**
- `static/js/modalSnap.js:1051`
- `static/js/modalSnap.js:1054`

## `onMove` — arrow, line 1052
- **called from:**
- `static/js/calendar.js:1587`
- `static/js/modalSnap.js:735`
- `static/js/modalSnap.js:759`
- `static/js/windowDrag.js:195`
- `static/js/windowDrag.js:200`
- `static/js/windowDrag.js:205`
- `static/js/windowDrag.js:206`
- `static/js/windowDrag.js:215`
- `static/js/windowDrag.js:223`
- `static/js/windowDrag.js:244`
- `static/js/windowDrag.js:245`

## `onUp` — arrow, line 1056
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
