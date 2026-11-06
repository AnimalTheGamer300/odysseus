# `static/js/ui.js` — definitions & call sites

57 definitions (regex-based, best-effort).
**Exports:** `autoResize`, `captureHistoryScroll`, `copyToClipboard`, `debounce`, `default`, `el`, `emptyStateIcon`, `esc`, `getAutoScroll`, `isAutoScrolling`, `isTouchInsideModal`, `restoreHistoryScroll`, `scrollHistory`, `scrollHistoryInstant`, `setAutoScroll`, `showError`, `showToast`, `styledConfirm`, `styledPrompt`

## `_isTextEditingTarget` — function, line 28
- **called from:**
- `static/js/ui.js:28`
- `static/js/ui.js:216`

## `_targetEl` — function, line 33
- **called from:**
- `static/js/ui.js:33`
- `static/js/ui.js:212`

## `_editorPanelVisible` — function, line 37
- **called from:**
- `static/js/ui.js:37`
- `static/js/ui.js:67`

## `_positionToastForOpenPanel` — function, line 49
- **called from:**
- `static/js/ui.js:49`
- `static/js/ui.js:494`
- `static/js/ui.js:531`

## `_visibleModalForSpace` — function, line 131
- **called from:**
- `static/js/ui.js:131`
- `static/js/ui.js:145`
- `static/js/ui.js:201`

## `_isSpaceVisible` — function, line 137
- **called from:**
- `static/js/ui.js:137`
- `static/js/ui.js:267`

## `_spaceWindowId` — function, line 143
- **called from:**
- `static/js/ui.js:143`
- `static/js/ui.js:196`
- `static/js/ui.js:282`

## `_windowAtPointer` — function, line 151
- **called from:**
- `static/js/ui.js:151`
- `static/js/ui.js:179`

## `_containsPointer` — function, line 171
- **called from:**
- `static/js/ui.js:171`

## `_closeHoveredWindow` — function, line 178
- **called from:**
- `static/js/ui.js:178`
- `static/js/ui.js:1555`

## `_spaceIsBlocked` — function, line 211
- **called from:**
- `static/js/ui.js:211`
- `static/js/ui.js:268`
- `static/js/ui.js:274`
- `static/js/ui.js:284`

## `_activateSpaceCard` — function, line 221
- **called from:**
- `static/js/ui.js:221`
- `static/js/ui.js:270`

## `_initHoverCardSpaceToggle` — function, line 238
- **called from:**
- `static/js/ui.js:238`
- `static/js/ui.js:290`

## `copyToClipboard` — function, line 295
- **called from:**
- `static/app.js:558`
- `static/js/admin.js:1277`
- `static/js/chat.js:7925`
- `static/js/chatRenderer.js:2060`
- `static/js/chatRenderer.js:2325`
- `static/js/chatRenderer.js:2539`
- `static/js/document.js:14577`
- `static/js/documentLibrary.js:257`
- `static/js/gallery.js:1776`
- `static/js/skills.js:956`
- `static/js/skills.js:1691`
- `static/js/slashCommands.js:407`
- `static/js/slashCommands.js:539`
- `static/js/tasks.js:2541`
- `static/js/tasks.js:2643`
- `static/js/ui.js:295`

## `_wireToastSwipe` — function, line 318
- **called from:**
- `static/js/ui.js:318`
- `static/js/ui.js:385`
- `static/js/ui.js:524`

## `endSwipe` — arrow, line 345
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `showToast` — function, line 376
- **called from:**
- `static/app.js:557`
- `static/app.js:652`
- `static/app.js:1437`
- `static/app.js:1441`
- `static/app.js:1488`
- `static/app.js:1503`
- `static/app.js:1507`
- `static/app.js:1538`
- `static/app.js:1639`
- `static/app.js:1699`
- `static/app.js:1821`
- `static/app.js:1856`
- `static/app.js:2626`
- `static/app.js:2867`
- `static/app.js:2888`
- `static/app.js:3523`
- `static/app.js:4319`
- `static/app.js:4343`
- `static/app.js:4416`
- `static/js/admin.js:208`
- `static/js/admin.js:615`
- `static/js/admin.js:946`
- `static/js/admin.js:1397`
- `static/js/admin.js:2345`
- `static/js/admin.js:2378`
- `static/js/admin.js:2395`
- `static/js/admin.js:2420`
- `static/js/admin.js:4040`
- `static/js/assistant.js:27`
- `static/js/assistant.js:35`
- `static/js/assistant.js:72`
- `static/js/assistant.js:75`
- `static/js/assistant.js:362`
- `static/js/assistant.js:366`
- `static/js/calendar.js:93`
- `static/js/calendar.js:586`
- `static/js/calendar.js:695`
- `static/js/calendar.js:2809`
- `static/js/calendar.js:3267`
- `static/js/calendar.js:3807`
- `static/js/calendar.js:3843`
- `static/js/calendar.js:3881`
- `static/js/calendar/reminders.js:94`
- `static/js/chat.js:882`
- `static/js/chat.js:944`
- `static/js/chat.js:1022`
- `static/js/chat.js:1044`
- `static/js/chat.js:1060`
- `static/js/chat.js:1083`
- `static/js/chat.js:1096`
- `static/js/chat.js:1118`
- `static/js/chat.js:1150`
- `static/js/chat.js:1156`
- `static/js/chat.js:2284`
- `static/js/chat.js:2437`
- `static/js/chat.js:2455`
- `static/js/chat.js:5189`
- `static/js/chat.js:5226`
- `static/js/chat.js:5372`
- `static/js/chat.js:5380`
- … +508 more (grep the name in repo)

## `showError` — function, line 515
- **called from:**
- `static/app.js:574`
- `static/app.js:1309`
- `static/app.js:1510`
- `static/app.js:1626`
- `static/app.js:1644`
- `static/app.js:1686`
- `static/app.js:1715`
- `static/app.js:3525`
- `static/app.js:3528`
- `static/js/admin.js:183`
- `static/js/admin.js:198`
- `static/js/admin.js:207`
- `static/js/admin.js:209`
- `static/js/admin.js:235`
- `static/js/admin.js:244`
- `static/js/admin.js:258`
- `static/js/admin.js:283`
- `static/js/admin.js:292`
- `static/js/admin.js:1240`
- `static/js/admin.js:1258`
- `static/js/calendar.js:279`
- `static/js/calendar.js:313`
- `static/js/calendar.js:365`
- `static/js/calendar.js:701`
- `static/js/calendar.js:2603`
- `static/js/calendar.js:2636`
- `static/js/calendar.js:3250`
- `static/js/chat.js:252`
- `static/js/chat.js:947`
- `static/js/chat.js:1050`
- `static/js/chat.js:1086`
- `static/js/chat.js:1121`
- `static/js/chat.js:1143`
- `static/js/chat.js:1162`
- `static/js/chat.js:2409`
- `static/js/chat.js:2465`
- `static/js/chat.js:3118`
- `static/js/chat.js:8174`
- `static/js/chat.js:8192`
- `static/js/chat.js:8224`
- `static/js/chat.js:8333`
- `static/js/chat.js:8346`
- `static/js/chat.js:8392`
- `static/js/chat.js:8426`
- `static/js/chat.js:8439`
- `static/js/chat.js:8482`
- `static/js/chat.js:8494`
- `static/js/chat.js:8507`
- `static/js/chat.js:8561`
- `static/js/chat.js:8720`
- `static/js/chat.js:9064`
- `static/js/chat.js:9120`
- `static/js/chat.js:9150`
- `static/js/chat.js:9169`
- `static/js/chat.js:9311`
- `static/js/chat.js:9416`
- `static/js/chatRenderer.js:749`
- `static/js/chatRenderer.js:774`
- `static/js/chatRenderer.js:1740`
- `static/js/chatRenderer.js:3871`
- … +245 more (grep the name in repo)

## `_bindScrollIntent` — function, line 585
- **called from:**
- `static/js/ui.js:585`
- `static/js/ui.js:604`

## `scrollHistory` — function, line 599
- **called from:**
- `static/app.js:343`
- `static/app.js:2004`
- `static/js/chat.js:1603`
- `static/js/chat.js:1628`
- `static/js/chat.js:2007`
- `static/js/chat.js:2365`
- `static/js/chat.js:2641`
- `static/js/chat.js:3545`
- `static/js/chat.js:4065`
- `static/js/chat.js:4170`
- `static/js/chat.js:4502`
- `static/js/chat.js:4526`
- `static/js/chat.js:4538`
- `static/js/chat.js:4548`
- `static/js/chat.js:4794`
- `static/js/chat.js:5285`
- `static/js/chat.js:5595`
- `static/js/chat.js:5647`
- `static/js/chat.js:5719`
- `static/js/chat.js:5803`
- `static/js/chat.js:5956`
- `static/js/chat.js:6006`
- `static/js/chat.js:6016`
- `static/js/chat.js:6027`
- `static/js/chat.js:6038`
- `static/js/chat.js:6632`
- `static/js/chat.js:6726`
- `static/js/chat.js:6856`
- `static/js/chat.js:6989`
- `static/js/chat.js:7295`
- `static/js/chat.js:7374`
- `static/js/chat.js:7417`
- `static/js/chat.js:7610`
- `static/js/chat.js:8781`
- `static/js/chat.js:9304`
- `static/js/chatRenderer.js:2939`
- `static/js/chatStream.js:329`
- `static/js/group.js:754`
- `static/js/group.js:785`
- `static/js/group.js:889`
- `static/js/group.js:905`
- `static/js/sessions.js:3264`
- `static/js/sessions.js:3466`
- `static/js/slashCommands.js:336`
- `static/js/slashCommands.js:442`
- `static/js/slashCommands.js:447`
- `static/js/slashCommands.js:455`
- `static/js/slashCommands.js:484`
- `static/js/slashCommands.js:580`
- `static/js/slashCommands.js:600`
- `static/js/slashCommands.js:675`
- `static/js/slashCommands.js:5275`
- `static/js/slashCommands.js:5340`
- `static/js/slashCommands.js:5384`
- `static/js/slashCommands.js:5514`
- `static/js/slashCommands.js:5692`
- `static/js/slashCommands.js:5708`
- `static/js/ui.js:599`
- `static/js/ui.js:713`

## `captureHistoryScroll` — function, line 624
- **called from:**
- `static/js/ui.js:624`

## `restoreHistoryScroll` — function, line 635
- **called from:**
- `static/js/ui.js:635`

## `apply` — arrow, line 647
- **called from:**
- `tests/test_review_calendar_invitation.py:52`
- `tests/test_review_calendar_invitation.py:54`
- `tests/test_review_calendar_invitation.py:60`
- `tests/test_review_calendar_invitation.py:61`
- `tests/test_review_calendar_invitation.py:70`
- `tests/test_review_calendar_invitation.py:71`
- `tests/test_review_calendar_invitation.py:78`
- `tests/test_review_calendar_invitation.py:79`
- `tests/test_review_calendar_invitation.py:81`
- `tests/test_review_calendar_invitation.py:89`
- `tests/test_review_calendar_invitation.py:109`
- `tests/test_review_calendar_invitation.py:111`
- `tests/test_review_calendar_invitation.py:173`
- `tests/test_review_calendar_invitation.py:174`
- `tests/test_review_calendar_invitation.py:176`
- `tests/test_review_calendar_invitation.py:184`
- `tests/test_review_calendar_invitation.py:185`
- `tests/test_review_calendar_invitation.py:192`
- `tests/test_review_calendar_invitation.py:201`
- `tests/test_review_calendar_invitation.py:202`
- `tests/test_review_calendar_invitation.py:209`
- `tests/test_review_calendar_invitation.py:210`
- `tests/test_review_calendar_invitation.py:211`
- `static/app.js:207`
- `static/js/admin.js:2634`
- `static/js/admin.js:2638`
- `static/js/calendar.js:1515`
- `static/js/composerHistoryRecall.js:175`
- `static/js/composerHistoryRecall.js:189`
- `static/js/composerHistoryRecall.js:193`
- `static/js/cookbookSchedule.js:22`
- `static/js/document.js:1725`
- `static/js/document.js:1734`
- `static/js/document.js:10179`
- `static/js/editor/fx/cube-lut.js:2`
- `static/js/editor/panel-visibility.js:81`
- `static/js/editor/panel-visibility.js:137`
- `static/js/editor/panel-visibility.js:150`
- `static/js/editor/panel-visibility.js:158`
- `static/js/editor/tools/perspective-crop.js:87`
- `static/js/editor/tools/perspective-crop.js:90`
- `static/js/galleryEditor.js:6770`
- `static/js/galleryEditor.js:10650`
- `static/js/galleryEditor.js:10666`
- `static/js/galleryEditor.js:11478`
- `static/js/sessions.js:40`
- `static/js/settings.js:130`
- `static/js/settings.js:149`
- `static/js/skills.js:69`
- `static/js/theme.js:831`
- `static/js/theme.js:836`
- `static/js/ui.js:653`
- `static/js/ui.js:656`
- `static/js/ui.js:757`

## `_smoothScrollStep` — function, line 661
- **called from:**
- `static/js/ui.js:661`

## `scrollHistoryInstant` — function, line 690
- **called from:**
- `static/js/chat.js:3009`
- `static/js/sessions.js:2515`
- `static/js/ui.js:690`

## `setAutoScroll` — function, line 702
- **called from:**
- `static/app.js:350`
- `static/app.js:360`
- `static/app.js:366`
- `static/js/chat.js:3008`
- `static/js/ui.js:702`

## `getAutoScroll` — function, line 709
- **called from:**
- `static/js/ui.js:709`

## `isAutoScrolling` — function, line 714
- **called from:**
- `static/js/ui.js:714`

## `autoResize` — function, line 721
- **called from:**
- `static/app.js:3538`
- `static/app.js:3558`
- `static/app.js:3562`
- `static/js/chat.js:2405`
- `static/js/chat.js:2471`
- `static/js/chat.js:2699`
- `static/js/chat.js:2725`
- `static/js/chat.js:2826`
- `static/js/chat.js:2837`
- `static/js/composerArrowUpRecall.js:127`
- `static/js/composerArrowUpRecall.js:140`
- `static/js/composerArrowUpRecall.js:165`
- `static/js/composerHistoryRecall.js:113`
- `static/js/sessions.js:155`
- `static/js/sessions.js:2368`
- `static/js/ui.js:721`

## `debounce` — function, line 752
- **called from:**
- `static/app.js:341`
- `static/app.js:4234`
- `static/js/ui.js:752`

## `later` — arrow, line 755
- **called from:**
- `static/js/editor/control-kit.js:162`
- `static/js/tourAutoplay.js:97`

## `el` — function, line 767
- **called from:**
- `static/app.js:289`
- `static/app.js:291`
- `static/app.js:295`
- `static/app.js:322`
- `static/app.js:323`
- `static/app.js:341`
- `static/app.js:342`
- `static/app.js:353`
- `static/app.js:358`
- `static/app.js:363`
- `static/app.js:371`
- `static/app.js:383`
- `static/app.js:411`
- `static/app.js:415`
- `static/app.js:472`
- `static/app.js:482`
- `static/app.js:486`
- `static/app.js:491`
- `static/app.js:549`
- `static/app.js:563`
- `static/app.js:599`
- `static/app.js:611`
- `static/app.js:623`
- `static/app.js:667`
- `static/app.js:668`
- `static/app.js:669`
- `static/app.js:673`
- `static/app.js:679`
- `static/app.js:788`
- `static/app.js:888`
- `static/app.js:897`
- `static/app.js:901`
- `static/app.js:909`
- `static/app.js:910`
- `static/app.js:911`
- `static/app.js:912`
- `static/app.js:925`
- `static/app.js:926`
- `static/app.js:941`
- `static/app.js:942`
- `static/app.js:943`
- `static/app.js:954`
- `static/app.js:959`
- `static/app.js:970`
- `static/app.js:972`
- `static/app.js:973`
- `static/app.js:990`
- `static/app.js:1012`
- `static/app.js:1032`
- `static/app.js:1042`
- `static/app.js:1052`
- `static/app.js:1060`
- `static/app.js:1074`
- `static/app.js:1089`
- `static/app.js:1102`
- `static/app.js:1105`
- `static/app.js:1105`
- `static/app.js:1118`
- `static/app.js:1133`
- `static/app.js:1141`
- … +1014 more (grep the name in repo)

## `styledConfirm` — function, line 777
- **called from:**
- `static/app.js:3415`
- `static/app.js:3511`
- `static/js/admin.js:255`
- `static/js/admin.js:272`
- `static/js/admin.js:588`
- `static/js/admin.js:1306`
- `static/js/admin.js:2403`
- `static/js/admin.js:2986`
- `static/js/admin.js:3294`
- `static/js/admin.js:3314`
- `static/js/admin.js:3452`
- `static/js/admin.js:3602`
- `static/js/admin.js:3781`
- `static/js/admin.js:3782`
- `static/js/calendar.js:582`
- `static/js/calendar.js:3296`
- `static/js/chat.js:2850`
- `static/js/chat.js:8252`
- `static/js/chat.js:8976`
- `static/js/chatRenderer.js:2185`
- `static/js/cookbook-hwfit.js:2734`
- `static/js/cookbook.js:2396`
- `static/js/cookbookRunning.js:2305`
- `static/js/cookbookRunning.js:2348`
- `static/js/cookbookServe.js:2558`
- `static/js/cookbookServe.js:2673`
- `static/js/cookbookServe.js:2986`
- `static/js/cookbookServe.js:3134`
- `static/js/cookbookServe.js:3160`
- `static/js/cookbookServe.js:3473`
- `static/js/cookbookServe.js:3519`
- `static/js/cookbookServe.js:3678`
- `static/js/cookbookServe.js:3724`
- `static/js/cookbookServe.js:3793`
- `static/js/cookbookServe.js:3913`
- `static/js/cookbookServe.js:4023`
- `static/js/document.js:16072`
- `static/js/documentLibrary.js:1412`
- `static/js/documentLibrary.js:1440`
- `static/js/documentLibrary.js:2309`
- `static/js/documentLibrary.js:2385`
- `static/js/documentLibrary.js:2491`
- `static/js/documentLibrary.js:2659`
- `static/js/documentLibrary.js:2749`
- `static/js/documentLibrary.js:2796`
- `static/js/documentLibrary.js:2835`
- `static/js/documentLibrary.js:2924`
- `static/js/documentLibrary.js:3095`
- `static/js/documentLibrary.js:3250`
- `static/js/documentLibrary.js:3379`
- `static/js/editor/layer-panel.js:593`
- `static/js/emailInbox.js:1345`
- `static/js/emailLibrary/index.js:998`
- `static/js/emailLibrary/index.js:2769`
- `static/js/emailLibrary/index.js:5243`
- `static/js/emailLibrary/menus.js:272`
- `static/js/emailLibrary/menus.js:514`
- `static/js/emailLibrary/menus.js:694`
- `static/js/emailLibrary/unsubscribe.js:685`
- `static/js/emailLibrary/unsubscribe.js:693`
- … +55 more (grep the name in repo)

## `btnLabel` — arrow, line 812
- **called from:**
- `static/js/ui.js:814`
- `static/js/ui.js:820`

## `cleanup` — function, line 832
- **called from:**
- `tests/test_browser_producer_live_contract.py:41`
- `tests/test_ca_trust.py:43`
- `static/js/calendar.js:3194`
- `static/js/calendar.js:3202`
- `static/js/calendar.js:3239`
- `static/js/calendar.js:3369`
- `static/js/calendar.js:3378`
- `static/js/chat.js:7595`
- `static/js/chat.js:9103`
- `static/js/chat.js:9111`
- `static/js/chat.js:9117`
- `static/js/chat.js:9120`
- `static/js/chat.js:9123`
- `static/js/chat.js:9146`
- `static/js/codeRunner.js:273`
- `static/js/codeRunner.js:294`
- `static/js/compare/selector.js:102`
- `static/js/compare/selector.js:953`
- `static/js/compare/selector.js:986`
- `static/js/compare/selector.js:990`
- `static/js/compare/selector.js:1046`
- `static/js/compare/selector.js:1345`
- `static/js/compare/selector.js:1367`
- `static/js/compare/selector.js:1380`
- `static/js/cookbookServe.js:1058`
- `static/js/cookbookServe.js:1069`
- `static/js/cookbookServe.js:1070`
- `static/js/cookbookServe.js:1079`
- `static/js/cookbookServe.js:1081`
- `static/js/cookbookServe.js:1086`
- `static/js/document.js:6258`
- `static/js/document.js:6263`
- `static/js/document.js:6978`
- `static/js/document.js:6985`
- `static/js/document.js:7028`
- `static/js/document.js:15678`
- `static/js/document.js:15699`
- `static/js/dragSort.js:26`
- `static/js/editor/ai-operation.js:35`
- `static/js/editor/ai-operation.js:41`
- `static/js/editor/ai-operation.js:42`
- `static/js/editor/slider-ux.js:181`
- `static/js/editor/slider-ux.js:190`
- `static/js/editor/wire-topbar-overflow.js:23`
- `static/js/gallery.js:1910`
- `static/js/gallery.js:1919`
- `static/js/gallery.js:2063`
- `static/js/gallery.js:2075`
- `static/js/gallery.js:2079`
- `static/js/galleryEditor.js:7450`
- `static/js/galleryEditor.js:7530`
- `static/js/galleryEditor.js:7565`
- `static/js/galleryEditor.js:8330`
- `static/js/galleryEditor.js:8354`
- `static/js/galleryEditor.js:8357`
- `static/js/galleryEditor.js:8365`
- `static/js/galleryEditor.js:8368`
- `static/js/galleryEditor.js:8372`
- `static/js/galleryEditor.js:8373`
- `static/js/galleryEditor.js:8375`
- … +33 more (grep the name in repo)

## `onOk` — function, line 844
- **called from:**
- `static/js/galleryEditor.js:13606`
- `static/js/galleryEditor.js:13665`
- `static/js/skills.js:1770`
- `static/js/ui.js:844`
- `static/js/ui.js:948`
- `static/js/ui.js:969`

## `onAlt` — function, line 845
- **called from:**
- `static/js/ui.js:845`

## `onCancel` — function, line 846
- **called from:**
- `static/js/cookbookServe.js:1069`
- `static/js/editor/direct-manipulation-session.js:70`
- `static/js/galleryEditor.js:13624`
- `static/js/skills.js:1771`
- `static/js/skills.js:1772`
- `static/js/ui.js:846`
- `static/js/ui.js:949`

## `onBackdrop` — function, line 847
- **called from:**
- `static/js/cookbookServe.js:1081`
- `static/js/galleryEditor.js:13663`
- `static/js/skills.js:1772`
- `static/js/ui.js:847`
- `static/js/ui.js:950`

## `onKey` — function, line 848
- **called from:**
- `static/js/cookbookServe.js:1082`
- `static/js/document.js:9403`
- `static/js/document.js:9453`
- `static/js/document.js:9491`
- `static/js/editor/tools/perspective-crop.js:85`
- `static/js/galleryEditor.js:13664`
- `static/js/settings.js:1644`
- `static/js/skills.js:1773`
- `static/js/ui.js:848`
- `static/js/ui.js:951`

## `styledPrompt` — function, line 884
- **called from:**
- `static/js/admin.js:194`
- `static/js/admin.js:196`
- `static/js/admin.js:219`
- `static/js/cookbookServe.js:2562`
- `static/js/gallery.js:892`
- `static/js/gallery.js:3157`
- `static/js/sessions.js:699`
- `static/js/sessions.js:1711`
- `static/js/ui.js:884`

## `cleanup` — function, line 936
- **called from:**
- `tests/test_browser_producer_live_contract.py:41`
- `tests/test_ca_trust.py:43`
- `static/js/calendar.js:3194`
- `static/js/calendar.js:3202`
- `static/js/calendar.js:3239`
- `static/js/calendar.js:3369`
- `static/js/calendar.js:3378`
- `static/js/chat.js:7595`
- `static/js/chat.js:9103`
- `static/js/chat.js:9111`
- `static/js/chat.js:9117`
- `static/js/chat.js:9120`
- `static/js/chat.js:9123`
- `static/js/chat.js:9146`
- `static/js/codeRunner.js:273`
- `static/js/codeRunner.js:294`
- `static/js/compare/selector.js:102`
- `static/js/compare/selector.js:953`
- `static/js/compare/selector.js:986`
- `static/js/compare/selector.js:990`
- `static/js/compare/selector.js:1046`
- `static/js/compare/selector.js:1345`
- `static/js/compare/selector.js:1367`
- `static/js/compare/selector.js:1380`
- `static/js/cookbookServe.js:1058`
- `static/js/cookbookServe.js:1069`
- `static/js/cookbookServe.js:1070`
- `static/js/cookbookServe.js:1079`
- `static/js/cookbookServe.js:1081`
- `static/js/cookbookServe.js:1086`
- `static/js/document.js:6258`
- `static/js/document.js:6263`
- `static/js/document.js:6978`
- `static/js/document.js:6985`
- `static/js/document.js:7028`
- `static/js/document.js:15678`
- `static/js/document.js:15699`
- `static/js/dragSort.js:26`
- `static/js/editor/ai-operation.js:35`
- `static/js/editor/ai-operation.js:41`
- `static/js/editor/ai-operation.js:42`
- `static/js/editor/slider-ux.js:181`
- `static/js/editor/slider-ux.js:190`
- `static/js/editor/wire-topbar-overflow.js:23`
- `static/js/gallery.js:1910`
- `static/js/gallery.js:1919`
- `static/js/gallery.js:2063`
- `static/js/gallery.js:2075`
- `static/js/gallery.js:2079`
- `static/js/galleryEditor.js:7450`
- `static/js/galleryEditor.js:7530`
- `static/js/galleryEditor.js:7565`
- `static/js/galleryEditor.js:8330`
- `static/js/galleryEditor.js:8354`
- `static/js/galleryEditor.js:8357`
- `static/js/galleryEditor.js:8365`
- `static/js/galleryEditor.js:8368`
- `static/js/galleryEditor.js:8372`
- `static/js/galleryEditor.js:8373`
- `static/js/galleryEditor.js:8375`
- … +33 more (grep the name in repo)

## `onOk` — function, line 948
- **called from:**
- `static/js/galleryEditor.js:13606`
- `static/js/galleryEditor.js:13665`
- `static/js/skills.js:1770`
- `static/js/ui.js:844`
- `static/js/ui.js:948`
- `static/js/ui.js:969`

## `onCancel` — function, line 949
- **called from:**
- `static/js/cookbookServe.js:1069`
- `static/js/editor/direct-manipulation-session.js:70`
- `static/js/galleryEditor.js:13624`
- `static/js/skills.js:1771`
- `static/js/skills.js:1772`
- `static/js/ui.js:846`
- `static/js/ui.js:949`

## `onBackdrop` — function, line 950
- **called from:**
- `static/js/cookbookServe.js:1081`
- `static/js/galleryEditor.js:13663`
- `static/js/skills.js:1772`
- `static/js/ui.js:847`
- `static/js/ui.js:950`

## `onKey` — function, line 951
- **called from:**
- `static/js/cookbookServe.js:1082`
- `static/js/document.js:9403`
- `static/js/document.js:9453`
- `static/js/document.js:9491`
- `static/js/editor/tools/perspective-crop.js:85`
- `static/js/galleryEditor.js:13664`
- `static/js/settings.js:1644`
- `static/js/skills.js:1773`
- `static/js/ui.js:848`
- `static/js/ui.js:951`

## `onInputKey` — function, line 966
- **called from:**
- `static/js/ui.js:966`

## `esc` — function, line 993
- **called from:**
- `static/js/admin.js:28`
- `static/js/admin.js:28`
- `static/js/admin.js:86`
- `static/js/admin.js:88`
- `static/js/admin.js:93`
- `static/js/admin.js:94`
- `static/js/admin.js:96`
- `static/js/admin.js:114`
- `static/js/admin.js:125`
- `static/js/admin.js:138`
- `static/js/admin.js:139`
- `static/js/admin.js:143`
- `static/js/admin.js:330`
- `static/js/admin.js:331`
- `static/js/admin.js:332`
- `static/js/admin.js:648`
- `static/js/admin.js:651`
- `static/js/admin.js:655`
- `static/js/admin.js:680`
- `static/js/admin.js:769`
- `static/js/admin.js:769`
- `static/js/admin.js:771`
- `static/js/admin.js:773`
- `static/js/admin.js:777`
- `static/js/admin.js:777`
- `static/js/admin.js:836`
- `static/js/admin.js:836`
- `static/js/admin.js:838`
- `static/js/admin.js:840`
- `static/js/admin.js:841`
- `static/js/admin.js:915`
- `static/js/admin.js:1072`
- `static/js/admin.js:1073`
- `static/js/admin.js:1077`
- `static/js/admin.js:1077`
- `static/js/admin.js:1078`
- `static/js/admin.js:1078`
- `static/js/admin.js:1080`
- `static/js/admin.js:1094`
- `static/js/admin.js:1094`
- `static/js/admin.js:1094`
- `static/js/admin.js:1097`
- `static/js/admin.js:1097`
- `static/js/admin.js:1099`
- `static/js/admin.js:1099`
- `static/js/admin.js:1099`
- `static/js/admin.js:1380`
- `static/js/admin.js:1385`
- `static/js/admin.js:1428`
- `static/js/admin.js:1428`
- `static/js/admin.js:1430`
- `static/js/admin.js:1432`
- `static/js/admin.js:1436`
- `static/js/admin.js:1436`
- `static/js/admin.js:1551`
- `static/js/admin.js:1554`
- `static/js/admin.js:1557`
- `static/js/admin.js:1557`
- `static/js/admin.js:1915`
- `static/js/admin.js:2802`
- … +576 more (grep the name in repo)

## `isTouchInsideModal` — function, line 1017
- **called from:**
- `static/app.js:858`
- `static/js/cookbook.js:3809`
- `static/js/documentLibrary.js:3647`
- `static/js/gallery.js:3175`
- `static/js/sessions.js:4153`
- `static/js/settings.js:1930`
- `static/js/settings/lifecycle.js:108`
- `static/js/tasks.js:3246`
- `static/js/ui.js:1017`

## `_initScrollDismiss` — function, line 1022
- **called from:**
- `static/js/ui.js:1022`
- `static/js/ui.js:1037`

## `emptyStateIcon` — function, line 1046
- **called from:**
- `static/js/documentLibrary.js:2342`
- `static/js/documentLibrary.js:2713`
- `static/js/emailLibrary/index.js:5367`
- `static/js/features/notes/ui/cardRendering.js:223`
- `static/js/features/notes/ui/cardRendering.js:232`
- `static/js/memory.js:812`
- `static/js/ui.js:1046`

## `_closeFloatingDropdownsForSwipe` — function, line 1140
- **called from:**
- `static/js/ui.js:1140`
- `static/js/ui.js:1248`

## `raiseModalToFront` — arrow, line 1328
- **called from:**
- `static/js/ui.js:1343`

## `_isVisible` — arrow, line 1432
- **called from:**
- `static/js/modalManager.js:1179`
- `static/js/modalManager.js:1181`
- `static/js/tourAutoplay.js:35`
- `static/js/tourAutoplay.js:83`
- `static/js/tourAutoplay.js:109`
- `static/js/tourHints.js:47`
- `static/js/tourHints.js:131`
- `static/js/tourHints.js:141`
- `static/js/ui.js:1434`
- `static/js/ui.js:1488`
- `static/js/ui.js:1501`
- `static/js/ui.js:1516`
- `static/js/ui.js:1574`

## `_promote` — arrow, line 1433
- **called from:**
- `static/js/ui.js:1450`
- `static/js/ui.js:1451`

## `pickTopModal` — arrow, line 1456
- **called from:**
- `static/js/ui.js:1584`

## `directly` — class, line 1472
- **called from:**
- `static/js/document.js:10313`
- `static/js/editor/layer-panel.js:12`
- `static/js/galleryEditor.js:5328`
- `static/js/group.js:348`
- `static/js/sessions.js:990`
- `static/js/startupShell.js:8`
