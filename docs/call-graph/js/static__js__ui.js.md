# `static/js/ui.js` — definitions & call sites

50 definitions (regex-based, best-effort).
**Exports:** `autoResize`, `copyToClipboard`, `debounce`, `default`, `el`, `emptyStateIcon`, `esc`, `getAutoScroll`, `isTouchInsideModal`, `scrollHistory`, `scrollHistoryInstant`, `setAutoScroll`, `showError`, `showToast`, `styledConfirm`, `styledPrompt`

## `_isTextEditingTarget` — function, line 25
- **called from:**
- `static/js/ui.js:25`
- `static/js/ui.js:145`

## `_targetEl` — function, line 30
- **called from:**
- `static/js/ui.js:30`
- `static/js/ui.js:143`

## `_visibleModalForSpace` — function, line 62
- **called from:**
- `static/js/ui.js:62`
- `static/js/ui.js:76`
- `static/js/ui.js:132`

## `_isSpaceVisible` — function, line 68
- **called from:**
- `static/js/ui.js:68`
- `static/js/ui.js:192`

## `_spaceWindowId` — function, line 74
- **called from:**
- `static/js/ui.js:74`
- `static/js/ui.js:127`
- `static/js/ui.js:207`

## `_windowAtPointer` — function, line 82
- **called from:**
- `static/js/ui.js:82`
- `static/js/ui.js:110`

## `_containsPointer` — function, line 102
- **called from:**
- `static/js/ui.js:102`

## `_closeHoveredWindow` — function, line 109
- **called from:**
- `static/js/ui.js:109`
- `static/js/ui.js:1287`

## `_spaceIsBlocked` — function, line 142
- **called from:**
- `static/js/ui.js:142`
- `static/js/ui.js:193`
- `static/js/ui.js:199`
- `static/js/ui.js:209`

## `_activateSpaceCard` — function, line 150
- **called from:**
- `static/js/ui.js:150`
- `static/js/ui.js:195`

## `_initHoverCardSpaceToggle` — function, line 167
- **called from:**
- `static/js/ui.js:167`
- `static/js/ui.js:215`

## `copyToClipboard` — function, line 220
- **called from:**
- `static/app.js:495`
- `static/js/admin.js:593`
- `static/js/chat.js:6245`
- `static/js/chatRenderer.js:1482`
- `static/js/chatRenderer.js:1746`
- `static/js/chatRenderer.js:1954`
- `static/js/document.js:9143`
- `static/js/documentLibrary.js:151`
- `static/js/skills.js:1411`
- `static/js/slashCommands.js:407`
- `static/js/slashCommands.js:539`
- `static/js/tasks.js:2423`
- `static/js/tasks.js:2507`
- `static/js/ui.js:220`

## `_wireToastSwipe` — function, line 243
- **called from:**
- `static/js/ui.js:243`
- `static/js/ui.js:304`
- `static/js/ui.js:417`

## `endSwipe` — arrow, line 270
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `showToast` — function, line 300
- **called from:**
- `static/app.js:494`
- `static/app.js:557`
- `static/app.js:619`
- `static/app.js:1396`
- `static/app.js:1400`
- `static/app.js:1447`
- `static/app.js:1462`
- `static/app.js:1466`
- `static/app.js:1497`
- `static/app.js:1598`
- `static/app.js:1658`
- `static/app.js:1765`
- `static/app.js:1800`
- `static/app.js:2570`
- `static/app.js:2791`
- `static/app.js:2812`
- `static/app.js:3423`
- `static/app.js:4203`
- `static/app.js:4227`
- `static/app.js:4300`
- `static/js/admin.js:691`
- `static/js/admin.js:1476`
- `static/js/admin.js:1509`
- `static/js/admin.js:1526`
- `static/js/admin.js:1551`
- `static/js/assistant.js:27`
- `static/js/assistant.js:35`
- `static/js/assistant.js:72`
- `static/js/assistant.js:75`
- `static/js/assistant.js:362`
- `static/js/assistant.js:366`
- `static/js/calendar.js:88`
- `static/js/calendar.js:497`
- `static/js/calendar.js:606`
- `static/js/calendar.js:2234`
- `static/js/calendar.js:2657`
- `static/js/calendar.js:3135`
- `static/js/calendar.js:3171`
- `static/js/calendar.js:3206`
- `static/js/calendar/reminders.js:94`
- `static/js/chat.js:269`
- `static/js/chat.js:275`
- `static/js/chat.js:1418`
- `static/js/chat.js:1435`
- `static/js/chat.js:3674`
- `static/js/chat.js:3711`
- `static/js/chat.js:3857`
- `static/js/chat.js:3865`
- `static/js/chat.js:5838`
- `static/js/chat.js:6563`
- `static/js/chat.js:7023`
- `static/js/chat.js:7407`
- `static/js/chat.js:7423`
- `static/js/chat.js:7534`
- `static/js/chatRenderer.js:346`
- `static/js/chatRenderer.js:371`
- `static/js/chatRenderer.js:1536`
- `static/js/chatRenderer.js:1541`
- `static/js/chatStream.js:231`
- `static/js/codeRunner.js:69`
- … +420 more (grep the name in repo)

## `showError` — function, line 413
- **called from:**
- `static/app.js:508`
- `static/app.js:560`
- `static/app.js:1267`
- `static/app.js:1469`
- `static/app.js:1585`
- `static/app.js:1603`
- `static/app.js:1645`
- `static/app.js:1674`
- `static/app.js:3425`
- `static/app.js:3428`
- `static/js/admin.js:149`
- `static/js/admin.js:178`
- `static/js/admin.js:187`
- `static/js/admin.js:201`
- `static/js/admin.js:226`
- `static/js/admin.js:235`
- `static/js/calendar.js:270`
- `static/js/calendar.js:299`
- `static/js/calendar.js:355`
- `static/js/calendar.js:612`
- `static/js/calendar.js:2042`
- `static/js/calendar.js:2075`
- `static/js/calendar.js:2640`
- `static/js/chat.js:281`
- `static/js/chat.js:1391`
- `static/js/chat.js:1445`
- `static/js/chat.js:2060`
- `static/js/chat.js:2175`
- `static/js/chat.js:2193`
- `static/js/chat.js:6528`
- `static/js/chat.js:6532`
- `static/js/chat.js:6539`
- `static/js/chat.js:6566`
- `static/js/chat.js:6626`
- `static/js/chat.js:6655`
- `static/js/chat.js:6668`
- `static/js/chat.js:6702`
- `static/js/chat.js:6732`
- `static/js/chat.js:6745`
- `static/js/chat.js:6786`
- `static/js/chat.js:6799`
- `static/js/chat.js:6825`
- `static/js/chat.js:6857`
- `static/js/chat.js:7026`
- `static/js/chat.js:7401`
- `static/js/chat.js:7426`
- `static/js/chat.js:7482`
- `static/js/chat.js:7485`
- `static/js/chat.js:7537`
- `static/js/chat.js:7556`
- `static/js/chat.js:7698`
- `static/js/chat.js:7803`
- `static/js/chatRenderer.js:351`
- `static/js/chatRenderer.js:376`
- `static/js/chatRenderer.js:1272`
- `static/js/chatRenderer.js:3131`
- `static/js/compare/index.js:234`
- `static/js/compare/index.js:877`
- `static/js/compare/index.js:1007`
- `static/js/compare/index.js:1434`
- … +218 more (grep the name in repo)

## `_bindScrollIntent` — function, line 465
- **called from:**
- `static/js/ui.js:465`
- `static/js/ui.js:484`

## `scrollHistory` — function, line 479
- **called from:**
- `static/app.js:1946`
- `static/js/chat.js:723`
- `static/js/chat.js:748`
- `static/js/chat.js:1112`
- `static/js/chat.js:1370`
- `static/js/chat.js:1616`
- `static/js/chat.js:2487`
- `static/js/chat.js:2702`
- `static/js/chat.js:2801`
- `static/js/chat.js:3084`
- `static/js/chat.js:3113`
- `static/js/chat.js:3124`
- `static/js/chat.js:3133`
- `static/js/chat.js:3770`
- `static/js/chat.js:4053`
- `static/js/chat.js:4100`
- `static/js/chat.js:4158`
- `static/js/chat.js:4231`
- `static/js/chat.js:4367`
- `static/js/chat.js:4415`
- `static/js/chat.js:4425`
- `static/js/chat.js:4436`
- `static/js/chat.js:4447`
- `static/js/chat.js:4686`
- `static/js/chat.js:5017`
- `static/js/chat.js:5089`
- `static/js/chat.js:5203`
- `static/js/chat.js:5336`
- `static/js/chat.js:5629`
- `static/js/chat.js:5700`
- `static/js/chat.js:5904`
- `static/js/chat.js:5917`
- `static/js/chat.js:5989`
- `static/js/chat.js:7089`
- `static/js/chat.js:7691`
- `static/js/chatRenderer.js:2323`
- `static/js/chatStream.js:294`
- `static/js/group.js:754`
- `static/js/group.js:785`
- `static/js/group.js:887`
- `static/js/group.js:903`
- `static/js/sessions.js:2843`
- `static/js/sessions.js:3045`
- `static/js/slashCommands.js:336`
- `static/js/slashCommands.js:442`
- `static/js/slashCommands.js:447`
- `static/js/slashCommands.js:455`
- `static/js/slashCommands.js:484`
- `static/js/slashCommands.js:580`
- `static/js/slashCommands.js:600`
- `static/js/slashCommands.js:675`
- `static/js/slashCommands.js:5266`
- `static/js/slashCommands.js:5331`
- `static/js/slashCommands.js:5352`
- `static/js/slashCommands.js:5482`
- `static/js/slashCommands.js:5660`
- `static/js/slashCommands.js:5676`
- `static/js/ui.js:479`

## `_smoothScrollStep` — function, line 496
- **called from:**
- `static/js/ui.js:496`

## `scrollHistoryInstant` — function, line 525
- **called from:**
- `static/js/chat.js:1956`
- `static/js/sessions.js:2168`
- `static/js/ui.js:525`

## `setAutoScroll` — function, line 537
- **called from:**
- `static/app.js:333`
- `static/app.js:343`
- `static/app.js:349`
- `static/js/chat.js:1955`
- `static/js/ui.js:537`

## `getAutoScroll` — function, line 544
- **called from:**
- `static/js/ui.js:544`

## `autoResize` — function, line 551
- **called from:**
- `static/app.js:3438`
- `static/app.js:3458`
- `static/app.js:3462`
- `static/js/chat.js:1387`
- `static/js/chat.js:1451`
- `static/js/chat.js:1674`
- `static/js/chat.js:1702`
- `static/js/chat.js:1801`
- `static/js/chat.js:1812`
- `static/js/composerArrowUpRecall.js:127`
- `static/js/composerArrowUpRecall.js:140`
- `static/js/composerArrowUpRecall.js:165`
- `static/js/composerHistoryRecall.js:113`
- `static/js/sessions.js:67`
- `static/js/sessions.js:2021`
- `static/js/ui.js:551`

## `debounce` — function, line 582
- **called from:**
- `static/app.js:330`
- `static/app.js:4120`
- `static/js/ui.js:582`

## `later` — arrow, line 585
- **called from:**
- `static/js/tourAutoplay.js:97`

## `el` — function, line 597
- **called from:**
- `static/app.js:281`
- `static/app.js:283`
- `static/app.js:287`
- `static/app.js:311`
- `static/app.js:312`
- `static/app.js:330`
- `static/app.js:331`
- `static/app.js:336`
- `static/app.js:341`
- `static/app.js:346`
- `static/app.js:354`
- `static/app.js:365`
- `static/app.js:393`
- `static/app.js:418`
- `static/app.js:428`
- `static/app.js:486`
- `static/app.js:500`
- `static/app.js:514`
- `static/app.js:539`
- `static/app.js:566`
- `static/app.js:578`
- `static/app.js:590`
- `static/app.js:634`
- `static/app.js:635`
- `static/app.js:636`
- `static/app.js:640`
- `static/app.js:646`
- `static/app.js:755`
- `static/app.js:855`
- `static/app.js:864`
- `static/app.js:868`
- `static/app.js:876`
- `static/app.js:877`
- `static/app.js:878`
- `static/app.js:879`
- `static/app.js:892`
- `static/app.js:893`
- `static/app.js:908`
- `static/app.js:909`
- `static/app.js:910`
- `static/app.js:921`
- `static/app.js:926`
- `static/app.js:937`
- `static/app.js:939`
- `static/app.js:940`
- `static/app.js:957`
- `static/app.js:979`
- `static/app.js:999`
- `static/app.js:1009`
- `static/app.js:1019`
- `static/app.js:1027`
- `static/app.js:1041`
- `static/app.js:1056`
- `static/app.js:1069`
- `static/app.js:1072`
- `static/app.js:1072`
- `static/app.js:1085`
- `static/app.js:1100`
- `static/app.js:1248`
- `static/app.js:1258`
- … +888 more (grep the name in repo)

## `styledConfirm` — function, line 607
- **called from:**
- `static/app.js:3411`
- `static/js/admin.js:198`
- `static/js/admin.js:215`
- `static/js/admin.js:622`
- `static/js/admin.js:1534`
- `static/js/admin.js:2117`
- `static/js/admin.js:2420`
- `static/js/admin.js:2440`
- `static/js/admin.js:2578`
- `static/js/admin.js:2728`
- `static/js/admin.js:2907`
- `static/js/admin.js:2908`
- `static/js/calendar.js:493`
- `static/js/calendar.js:2680`
- `static/js/chat.js:1825`
- `static/js/chat.js:7323`
- `static/js/chatRenderer.js:1607`
- `static/js/cookbook-hwfit.js:2622`
- `static/js/cookbook.js:2308`
- `static/js/cookbookRunning.js:2254`
- `static/js/cookbookRunning.js:2292`
- `static/js/cookbookServe.js:2486`
- `static/js/cookbookServe.js:2601`
- `static/js/cookbookServe.js:2901`
- `static/js/cookbookServe.js:3048`
- `static/js/cookbookServe.js:3074`
- `static/js/cookbookServe.js:3369`
- `static/js/cookbookServe.js:3415`
- `static/js/cookbookServe.js:3574`
- `static/js/cookbookServe.js:3620`
- `static/js/cookbookServe.js:3689`
- `static/js/cookbookServe.js:3809`
- `static/js/cookbookServe.js:3918`
- `static/js/document.js:9811`
- `static/js/documentLibrary.js:1188`
- `static/js/documentLibrary.js:1216`
- `static/js/documentLibrary.js:2100`
- `static/js/documentLibrary.js:2108`
- `static/js/documentLibrary.js:2184`
- `static/js/documentLibrary.js:2290`
- `static/js/documentLibrary.js:2450`
- `static/js/documentLibrary.js:2539`
- `static/js/documentLibrary.js:2585`
- `static/js/documentLibrary.js:2623`
- `static/js/documentLibrary.js:2712`
- `static/js/documentLibrary.js:2807`
- `static/js/documentLibrary.js:2869`
- `static/js/documentLibrary.js:2878`
- `static/js/documentLibrary.js:3030`
- `static/js/documentLibrary.js:3184`
- `static/js/documentLibrary.js:3313`
- `static/js/editor/layer-panel.js:359`
- `static/js/emailInbox.js:1265`
- `static/js/emailLibrary.js:1188`
- `static/js/emailLibrary.js:1545`
- `static/js/emailLibrary.js:1671`
- `static/js/emailLibrary.js:1736`
- `static/js/emailLibrary.js:2832`
- `static/js/emailLibrary.js:4882`
- `static/js/emailLibrary.js:7867`
- … +57 more (grep the name in repo)

## `cleanup` — function, line 654
- **called from:**
- `static/js/calendar.js:2592`
- `static/js/calendar.js:2629`
- `static/js/calendar.js:2750`
- `static/js/calendar.js:2759`
- `static/js/chat.js:5889`
- `static/js/chat.js:7465`
- `static/js/chat.js:7473`
- `static/js/chat.js:7479`
- `static/js/chat.js:7482`
- `static/js/chat.js:7485`
- `static/js/chat.js:7533`
- `static/js/codeRunner.js:262`
- `static/js/codeRunner.js:283`
- `static/js/compare/selector.js:102`
- `static/js/compare/selector.js:877`
- `static/js/compare/selector.js:910`
- `static/js/compare/selector.js:914`
- `static/js/compare/selector.js:963`
- `static/js/compare/selector.js:1257`
- `static/js/compare/selector.js:1282`
- `static/js/compare/selector.js:1295`
- `static/js/cookbookServe.js:1029`
- `static/js/cookbookServe.js:1040`
- `static/js/cookbookServe.js:1041`
- `static/js/cookbookServe.js:1050`
- `static/js/cookbookServe.js:1052`
- `static/js/cookbookServe.js:1057`
- `static/js/document.js:3847`
- `static/js/document.js:3848`
- `static/js/document.js:3849`
- `static/js/document.js:4393`
- `static/js/document.js:4400`
- `static/js/document.js:4442`
- `static/js/dragSort.js:26`
- `static/js/editor/slider-ux.js:179`
- `static/js/editor/slider-ux.js:188`
- `static/js/gallery.js:1665`
- `static/js/gallery.js:1674`
- `static/js/gallery.js:1818`
- `static/js/gallery.js:1830`
- `static/js/gallery.js:1834`
- `static/js/galleryEditor.js:1863`
- `static/js/galleryEditor.js:1952`
- `static/js/galleryEditor.js:1987`
- `static/js/galleryEditor.js:2663`
- `static/js/galleryEditor.js:2664`
- `static/js/galleryEditor.js:2667`
- `static/js/galleryEditor.js:2668`
- `static/js/galleryEditor.js:2670`
- `static/js/galleryEditor.js:3958`
- `static/js/galleryEditor.js:3969`
- `static/js/galleryEditor.js:3971`
- `static/js/galleryEditor.js:3972`
- `static/js/galleryEditor.js:3975`
- `static/js/settings.js:1928`
- `static/js/settings.js:1938`
- `static/js/settings.js:1969`
- `static/js/skills.js:1454`
- `static/js/skills.js:1463`
- `static/js/skills.js:1464`
- … +21 more (grep the name in repo)

## `onOk` — function, line 665
- **called from:**
- `static/js/galleryEditor.js:3966`
- `static/js/galleryEditor.js:3974`
- `static/js/skills.js:1463`
- `static/js/ui.js:665`
- `static/js/ui.js:764`
- `static/js/ui.js:785`

## `onAlt` — function, line 666
- **called from:**
- `static/js/ui.js:666`

## `onCancel` — function, line 667
- **called from:**
- `static/js/cookbookServe.js:1040`
- `static/js/documentLibrary.js:228`
- `static/js/galleryEditor.js:3971`
- `static/js/skills.js:1464`
- `static/js/skills.js:1465`
- `static/js/ui.js:667`
- `static/js/ui.js:765`

## `onBackdrop` — function, line 668
- **called from:**
- `static/js/cookbookServe.js:1052`
- `static/js/galleryEditor.js:3972`
- `static/js/skills.js:1465`
- `static/js/ui.js:668`
- `static/js/ui.js:766`

## `onKey` — function, line 669
- **called from:**
- `static/js/cookbookServe.js:1053`
- `static/js/document.js:6145`
- `static/js/galleryEditor.js:3973`
- `static/js/settings.js:1933`
- `static/js/skills.js:1466`
- `static/js/ui.js:669`
- `static/js/ui.js:767`

## `styledPrompt` — function, line 704
- **called from:**
- `static/js/admin.js:162`
- `static/js/cookbookServe.js:2490`
- `static/js/gallery.js:795`
- `static/js/gallery.js:2774`
- `static/js/sessions.js:484`
- `static/js/sessions.js:1362`
- `static/js/ui.js:704`

## `cleanup` — function, line 753
- **called from:**
- `static/js/calendar.js:2592`
- `static/js/calendar.js:2629`
- `static/js/calendar.js:2750`
- `static/js/calendar.js:2759`
- `static/js/chat.js:5889`
- `static/js/chat.js:7465`
- `static/js/chat.js:7473`
- `static/js/chat.js:7479`
- `static/js/chat.js:7482`
- `static/js/chat.js:7485`
- `static/js/chat.js:7533`
- `static/js/codeRunner.js:262`
- `static/js/codeRunner.js:283`
- `static/js/compare/selector.js:102`
- `static/js/compare/selector.js:877`
- `static/js/compare/selector.js:910`
- `static/js/compare/selector.js:914`
- `static/js/compare/selector.js:963`
- `static/js/compare/selector.js:1257`
- `static/js/compare/selector.js:1282`
- `static/js/compare/selector.js:1295`
- `static/js/cookbookServe.js:1029`
- `static/js/cookbookServe.js:1040`
- `static/js/cookbookServe.js:1041`
- `static/js/cookbookServe.js:1050`
- `static/js/cookbookServe.js:1052`
- `static/js/cookbookServe.js:1057`
- `static/js/document.js:3847`
- `static/js/document.js:3848`
- `static/js/document.js:3849`
- `static/js/document.js:4393`
- `static/js/document.js:4400`
- `static/js/document.js:4442`
- `static/js/dragSort.js:26`
- `static/js/editor/slider-ux.js:179`
- `static/js/editor/slider-ux.js:188`
- `static/js/gallery.js:1665`
- `static/js/gallery.js:1674`
- `static/js/gallery.js:1818`
- `static/js/gallery.js:1830`
- `static/js/gallery.js:1834`
- `static/js/galleryEditor.js:1863`
- `static/js/galleryEditor.js:1952`
- `static/js/galleryEditor.js:1987`
- `static/js/galleryEditor.js:2663`
- `static/js/galleryEditor.js:2664`
- `static/js/galleryEditor.js:2667`
- `static/js/galleryEditor.js:2668`
- `static/js/galleryEditor.js:2670`
- `static/js/galleryEditor.js:3958`
- `static/js/galleryEditor.js:3969`
- `static/js/galleryEditor.js:3971`
- `static/js/galleryEditor.js:3972`
- `static/js/galleryEditor.js:3975`
- `static/js/settings.js:1928`
- `static/js/settings.js:1938`
- `static/js/settings.js:1969`
- `static/js/skills.js:1454`
- `static/js/skills.js:1463`
- `static/js/skills.js:1464`
- … +21 more (grep the name in repo)

## `onOk` — function, line 764
- **called from:**
- `static/js/galleryEditor.js:3966`
- `static/js/galleryEditor.js:3974`
- `static/js/skills.js:1463`
- `static/js/ui.js:665`
- `static/js/ui.js:764`
- `static/js/ui.js:785`

## `onCancel` — function, line 765
- **called from:**
- `static/js/cookbookServe.js:1040`
- `static/js/documentLibrary.js:228`
- `static/js/galleryEditor.js:3971`
- `static/js/skills.js:1464`
- `static/js/skills.js:1465`
- `static/js/ui.js:667`
- `static/js/ui.js:765`

## `onBackdrop` — function, line 766
- **called from:**
- `static/js/cookbookServe.js:1052`
- `static/js/galleryEditor.js:3972`
- `static/js/skills.js:1465`
- `static/js/ui.js:668`
- `static/js/ui.js:766`

## `onKey` — function, line 767
- **called from:**
- `static/js/cookbookServe.js:1053`
- `static/js/document.js:6145`
- `static/js/galleryEditor.js:3973`
- `static/js/settings.js:1933`
- `static/js/skills.js:1466`
- `static/js/ui.js:669`
- `static/js/ui.js:767`

## `onInputKey` — function, line 782
- **called from:**
- `static/js/ui.js:782`

## `esc` — function, line 809
- **called from:**
- `static/js/admin.js:20`
- `static/js/admin.js:20`
- `static/js/admin.js:53`
- `static/js/admin.js:55`
- `static/js/admin.js:60`
- `static/js/admin.js:61`
- `static/js/admin.js:62`
- `static/js/admin.js:80`
- `static/js/admin.js:91`
- `static/js/admin.js:104`
- `static/js/admin.js:105`
- `static/js/admin.js:109`
- `static/js/admin.js:273`
- `static/js/admin.js:274`
- `static/js/admin.js:275`
- `static/js/admin.js:525`
- `static/js/admin.js:532`
- `static/js/admin.js:534`
- `static/js/admin.js:545`
- `static/js/admin.js:545`
- `static/js/admin.js:674`
- `static/js/admin.js:679`
- `static/js/admin.js:719`
- `static/js/admin.js:719`
- `static/js/admin.js:720`
- `static/js/admin.js:722`
- `static/js/admin.js:1022`
- `static/js/admin.js:1200`
- `static/js/admin.js:1203`
- `static/js/admin.js:1206`
- `static/js/admin.js:1933`
- `static/js/admin.js:1948`
- `static/js/admin.js:1949`
- `static/js/admin.js:1951`
- `static/js/admin.js:1953`
- `static/js/admin.js:2081`
- `static/js/admin.js:2156`
- `static/js/admin.js:2157`
- `static/js/admin.js:2158`
- `static/js/admin.js:2158`
- `static/js/admin.js:2390`
- `static/js/admin.js:2417`
- `static/js/admin.js:2417`
- `static/js/admin.js:2417`
- `static/js/admin.js:2436`
- `static/js/admin.js:2436`
- `static/js/admin.js:2436`
- `static/js/admin.js:2542`
- `static/js/admin.js:2543`
- `static/js/admin.js:2544`
- `static/js/admin.js:2545`
- `static/js/admin.js:2545`
- `static/js/admin.js:2558`
- `static/js/admin.js:2561`
- `static/js/admin.js:2561`
- `static/js/admin.js:2562`
- `static/js/admin.js:2563`
- `static/js/admin.js:2566`
- `static/js/admin.js:2567`
- `static/js/admin.js:2569`
- … +443 more (grep the name in repo)

## `isTouchInsideModal` — function, line 833
- **called from:**
- `static/app.js:825`
- `static/js/cookbook.js:3598`
- `static/js/documentLibrary.js:3580`
- `static/js/gallery.js:2792`
- `static/js/sessions.js:3723`
- `static/js/settings.js:2218`
- `static/js/settings/lifecycle.js:106`
- `static/js/tasks.js:3026`
- `static/js/ui.js:833`

## `_initScrollDismiss` — function, line 838
- **called from:**
- `static/js/ui.js:838`
- `static/js/ui.js:853`

## `emptyStateIcon` — function, line 862
- **called from:**
- `static/js/documentLibrary.js:2141`
- `static/js/documentLibrary.js:2504`
- `static/js/documentLibrary.js:2776`
- `static/js/emailLibrary.js:4978`
- `static/js/memory.js:706`
- `static/js/notes.js:1966`
- `static/js/notes.js:1975`
- `static/js/ui.js:862`

## `_closeFloatingDropdownsForSwipe` — function, line 953
- **called from:**
- `static/js/ui.js:953`
- `static/js/ui.js:1061`

## `raiseModalToFront` — arrow, line 1141
- **called from:**
- `static/js/ui.js:1156`

## `_isVisible` — arrow, line 1245
- **called from:**
- `static/js/modalManager.js:1167`
- `static/js/modalManager.js:1169`
- `static/js/tourAutoplay.js:35`
- `static/js/tourAutoplay.js:83`
- `static/js/tourAutoplay.js:109`
- `static/js/tourHints.js:45`
- `static/js/tourHints.js:136`
- `static/js/tourHints.js:146`
- `static/js/ui.js:1247`
- `static/js/ui.js:1334`

## `_promote` — arrow, line 1246
- **called from:**
- `static/js/ui.js:1263`
- `static/js/ui.js:1264`

## `pickTopModal` — arrow, line 1269
- **called from:**
- `static/js/ui.js:1344`

## `directly` — class, line 1285
- **called from:**
- `static/js/document.js:6346`
- `static/js/editor/layer-panel.js:12`
- `static/js/galleryEditor.js:1346`
- `static/js/group.js:348`
- `static/js/sessions.js:679`
- `static/js/startupShell.js:8`
