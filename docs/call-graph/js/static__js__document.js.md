# `static/js/document.js` — definitions & call sites

573 definitions (regex-based, best-effort).
**Exports:** `clearAll`, `closePanel`, `createDocument`, `default`, `ensureDocPanel`, `ensureEmailDraftEnvelope`, `findEmailDocId`, `focusEmailReplyBody`, `generateEmailReply`, `getActiveEmailComposerContext`, `getChatDocumentId`, `getCurrentDocId`, `getSelectionContext`, `handleDocSuggestions`, `handleDocUpdate`, `init`, `injectFreshDoc`, `isPanelOpen`, `loadDocument`, `loadSessionDocs`, `newDocument`, `openEmailDraft`, `openPanel`, `prepareDocumentOpen`, `replaceEmailReplyBody`, `restoreSelectionReference`, `saveDocument`, `streamDocDelta`, `streamDocFinalize`, `streamDocOpen`, `swapSide`

## `_isRenderLang` — arrow, line 77
- **called from:**
- `static/js/document.js:92`
- `static/js/document.js:3149`
- `static/js/document.js:3192`
- `static/js/document.js:3200`
- `static/js/document.js:3228`
- `static/js/document.js:3250`
- `static/js/document.js:8258`
- `static/js/document.js:8569`
- `static/js/document.js:8606`
- `static/js/document.js:14353`
- `static/js/document.js:14540`
- `static/js/document.js:14777`
- `static/js/document.js:14788`
- `static/js/document.js:14864`

## `_isRichTextLang` — arrow, line 78
- **called from:**
- `static/js/document.js:92`
- `static/js/document.js:314`
- `static/js/document.js:320`
- `static/js/document.js:3192`
- `static/js/document.js:3200`
- `static/js/document.js:3230`
- `static/js/document.js:3264`
- `static/js/document.js:3287`
- `static/js/document.js:3291`
- `static/js/document.js:3293`
- `static/js/document.js:3668`
- `static/js/document.js:3699`
- `static/js/document.js:3707`
- `static/js/document.js:4224`
- `static/js/document.js:4347`
- `static/js/document.js:4375`
- `static/js/document.js:4382`
- `static/js/document.js:5608`
- `static/js/document.js:5929`
- `static/js/document.js:5947`
- `static/js/document.js:7177`
- `static/js/document.js:7197`
- `static/js/document.js:7333`
- `static/js/document.js:8205`
- `static/js/document.js:8263`
- `static/js/document.js:8510`
- `static/js/document.js:8517`
- `static/js/document.js:8614`
- `static/js/document.js:12063`
- `static/js/document.js:13466`
- `static/js/document.js:14345`
- `static/js/document.js:15119`
- `static/js/document.js:15288`
- `static/js/document.js:15313`
- `static/js/document.js:15315`
- `static/js/document.js:15392`
- `static/js/document.js:15401`
- `static/js/document.js:15478`
- `static/js/document.js:15507`
- `static/js/document.js:15974`
- `static/js/document.js:16162`
- `static/js/document.js:16192`
- `static/js/document.js:16208`
- `static/js/document.js:17150`

## `_isDocxLang` — arrow, line 79
- **called from:**
- `static/js/document.js:92`
- `static/js/document.js:3192`
- `static/js/document.js:3200`
- `static/js/document.js:3229`
- `static/js/document.js:3258`
- `static/js/document.js:7212`
- `static/js/document.js:8245`
- `static/js/document.js:8610`
- `static/js/document.js:14789`
- `static/js/document.js:14865`
- `static/js/document.js:15294`
- `static/js/document.js:15304`
- `static/js/document.js:15306`
- `static/js/document.js:15307`
- `static/js/document.js:15480`
- `static/js/document.js:16269`
- `static/js/document.js:16277`

## `_hasViewToggle` — arrow, line 84
- **called from:**
- `static/js/document.js:3181`
- `static/js/document.js:3280`
- `static/js/document.js:3335`

## `_getEmailAccountsCached` — function, line 95
- **called from:**
- `static/js/document.js:95`
- `static/js/document.js:118`

## `_accountCanSend` — function, line 110
- **called from:**
- `static/js/document.js:110`
- `static/js/document.js:120`

## `_resolveComposeSendAccountId` — function, line 115
- **called from:**
- `static/js/document.js:115`
- `static/js/document.js:6371`
- `static/js/document.js:7010`

## `_renderDocumentSaveState` — function, line 159
- **called from:**
- `static/js/document.js:159`
- `static/js/document.js:177`
- `static/js/document.js:7098`

## `_setDocumentSaveState` — function, line 172
- **called from:**
- `static/js/document.js:172`
- `static/js/document.js:184`
- `static/js/document.js:15004`
- `static/js/document.js:15053`
- `static/js/document.js:15066`

## `_markDocumentDirty` — function, line 180
- **called from:**
- `static/js/document.js:180`
- `static/js/document.js:3707`
- `static/js/document.js:8783`

## `_syncEditorPlaceholder` — function, line 187
- **called from:**
- `static/js/document.js:187`
- `static/js/document.js:1473`
- `static/js/document.js:8016`
- `static/js/document.js:12051`
- `static/js/document.js:16783`
- `static/js/document.js:17141`

## `_setDocumentHistoryControlState` — function, line 210
- **called from:**
- `static/js/document.js:210`
- `static/js/document.js:228`
- `static/js/document.js:237`
- `static/js/document.js:1467`
- `static/js/document.js:7099`

## `_syncDocumentHistoryControlsNow` — function, line 223
- **called from:**
- `static/js/document.js:223`
- `static/js/document.js:8679`
- `static/js/document.js:8688`
- `static/js/document.js:8701`
- `static/js/document.js:8710`

## `_scheduleDocumentHistoryControls` — function, line 240
- **called from:**
- `static/js/document.js:240`
- `static/js/document.js:4021`
- `static/js/document.js:4232`
- `static/js/document.js:4518`
- `static/js/document.js:8808`
- `static/js/document.js:10194`

## `_normalizeRichStatsText` — function, line 245
- **called from:**
- `static/js/document.js:245`
- `static/js/document.js:255`
- `static/js/document.js:260`

## `_documentStatsSource` — function, line 252
- **called from:**
- `static/js/document.js:252`
- `static/js/document.js:278`

## `_renderDocumentStats` — function, line 274
- **called from:**
- `static/js/document.js:274`
- `static/js/document.js:7777`

## `_scheduleDocumentStats` — function, line 307
- **called from:**
- `static/js/document.js:307`
- `static/js/document.js:4228`
- `static/js/document.js:4545`
- `static/js/document.js:7226`
- `static/js/document.js:8806`
- `static/js/document.js:13414`
- `static/js/document.js:13431`

## `_documentOutlineSupported` — function, line 312
- **called from:**
- `static/js/document.js:312`
- `static/js/document.js:421`
- `static/js/document.js:433`
- `static/js/document.js:3325`

## `_documentOutlineEntries` — function, line 317
- **called from:**
- `static/js/document.js:317`
- `static/js/document.js:390`
- `static/js/document.js:421`
- `static/js/document.js:3325`

## `_flashOutlineTarget` — function, line 348
- **called from:**
- `static/js/document.js:348`
- `static/js/document.js:359`
- `static/js/document.js:384`

## `_jumpToDocumentOutlineEntry` — function, line 356
- **called from:**
- `static/js/document.js:356`
- `static/js/document.js:412`

## `_renderDocumentOutlineMenu` — function, line 387
- **called from:**
- `static/js/document.js:387`
- `static/js/document.js:424`
- `static/js/document.js:451`

## `_refreshDocumentOutline` — function, line 419
- **called from:**
- `static/js/document.js:419`
- `static/js/document.js:4229`
- `static/js/document.js:8807`

## `_closeDocumentOutline` — function, line 427
- **called from:**
- `static/js/document.js:423`
- `static/js/document.js:427`
- `static/js/document.js:435`
- `static/js/document.js:3327`
- `static/js/document.js:7053`
- `static/js/document.js:11855`

## `_openDocumentOutline` — function, line 431
- **called from:**
- `static/js/document.js:431`

## `_hideRichSelectionToolbar` — function, line 496
- **called from:**
- `static/js/document.js:496`
- `static/js/document.js:594`
- `static/js/document.js:604`
- `static/js/document.js:611`
- `static/js/document.js:622`
- `static/js/document.js:627`
- `static/js/document.js:632`
- `static/js/document.js:654`
- `static/js/document.js:4446`
- `static/js/document.js:4548`
- `static/js/document.js:6179`
- `static/js/document.js:7054`
- `static/js/document.js:11549`
- `static/js/document.js:11856`
- `static/js/document.js:14672`

## `_restoreRichSelectionToolbarRange` — function, line 504
- **called from:**
- `static/js/document.js:504`
- `static/js/document.js:598`

## `_richSelectionToolbarButton` — function, line 520
- **called from:**
- `static/js/document.js:520`
- `static/js/document.js:570`
- `static/js/document.js:571`
- `static/js/document.js:572`
- `static/js/document.js:573`
- `static/js/document.js:574`
- `static/js/document.js:575`
- `static/js/document.js:576`
- `static/js/document.js:577`

## `_richSelectionHasFormatting` — function, line 530
- **called from:**
- `static/js/document.js:530`
- `static/js/document.js:676`

## `hasFormattedAncestor` — arrow, line 533
- **called from:**
- `static/js/document.js:542`
- `static/js/document.js:542`

## `_clearRichSelectionFormatting` — function, line 551
- **called from:**
- `static/js/document.js:551`
- `static/js/document.js:10090`

## `_ensureRichSelectionToolbar` — function, line 562
- **called from:**
- `static/js/document.js:562`
- `static/js/document.js:659`

## `preserve` — arrow, line 586
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_renderRichSelectionToolbar` — function, line 619
- **called from:**
- `static/js/document.js:619`
- `static/js/document.js:728`
- `static/js/document.js:735`

## `_scheduleRichSelectionToolbar` — function, line 726
- **called from:**
- `static/js/document.js:609`
- `static/js/document.js:726`
- `static/js/document.js:4230`
- `static/js/document.js:4322`
- `static/js/document.js:4327`
- `static/js/document.js:4329`
- `static/js/document.js:4546`
- `static/js/document.js:4553`
- `static/js/document.js:4557`

## `_followRichSelectionToolbarLayout` — function, line 731
- **called from:**
- `static/js/document.js:731`
- `static/js/document.js:4554`
- `static/js/document.js:4558`

## `follow` — arrow, line 734
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_applyRichBlockInputRule` — function, line 783
- **called from:**
- `static/js/document.js:783`
- `static/js/document.js:4436`

## `_richSlashContext` — function, line 838
- **called from:**
- `static/js/document.js:838`
- `static/js/document.js:960`
- `static/js/document.js:980`
- `static/js/document.js:4419`

## `_richSlashCommands` — function, line 859
- **called from:**
- `static/js/document.js:859`
- `static/js/document.js:908`
- `static/js/document.js:961`

## `_hideRichSlashMenu` — function, line 868
- **called from:**
- `static/js/document.js:868`
- `static/js/document.js:969`
- `static/js/document.js:982`
- `static/js/document.js:4432`
- `static/js/document.js:4550`
- `static/js/document.js:6180`
- `static/js/document.js:7055`
- `static/js/document.js:11857`
- `static/js/document.js:14659`

## `_syncRichSlashActiveOption` — function, line 885
- **called from:**
- `static/js/document.js:885`
- `static/js/document.js:933`
- `static/js/document.js:956`

## `_renderRichSlashMenu` — function, line 905
- **called from:**
- `static/js/document.js:905`
- `static/js/document.js:1022`
- `static/js/document.js:4420`

## `_chooseRichSlashCommand` — function, line 959
- **called from:**
- `static/js/document.js:959`
- `static/js/document.js:999`
- `static/js/document.js:4426`

## `_syncRichSlashMenu` — function, line 979
- **called from:**
- `static/js/document.js:979`
- `static/js/document.js:4231`

## `_docOpenKey` — arrow, line 1025
- **called from:**
- `static/js/document.js:1043`
- `static/js/document.js:1046`
- `static/js/document.js:1049`
- `static/js/document.js:12362`

## `_docMinimizedKey` — arrow, line 1026
- **called from:**
- `static/js/document.js:1044`
- `static/js/document.js:1047`
- `static/js/document.js:1050`
- `static/js/document.js:12363`

## `_docActiveKey` — arrow, line 1027
- **called from:**
- `static/js/document.js:1032`
- `static/js/document.js:1036`
- `static/js/document.js:1037`
- `static/js/document.js:12404`
- `static/js/document.js:12407`

## `_rememberActiveDoc` — function, line 1029
- **called from:**
- `static/js/document.js:1029`
- `static/js/document.js:7095`

## `_forgetActiveDoc` — function, line 1035
- **called from:**
- `static/js/document.js:1035`
- `static/js/document.js:7247`

## `_markDocVisibleState` — function, line 1040
- **called from:**
- `static/js/document.js:1040`
- `static/js/document.js:1058`
- `static/js/document.js:7409`
- `static/js/document.js:11849`
- `static/js/document.js:11885`
- `static/js/document.js:11890`
- `static/js/document.js:11893`
- `static/js/document.js:12260`
- `static/js/document.js:12415`
- `static/js/document.js:12425`

## `prepareDocumentOpen` — function, line 1057
- **called from:**
- `static/js/document.js:1057`

## `init` — function, line 1065
- **called from:**
- `static/app.js:3824`
- `static/app.js:3825`
- `static/app.js:3826`
- `static/app.js:3827`
- `static/app.js:3828`
- `static/app.js:3829`
- `static/app.js:3833`
- `static/app.js:3836`
- `static/app.js:3838`
- `static/app.js:3841`
- `static/app.js:3850`
- `static/app.js:4486`
- `static/app.js:4487`
- `static/js/a11y.js:174`
- `static/js/a11y.js:223`
- `static/js/censor.js:44`
- `static/js/chat.js:2061`
- `static/js/chat.js:2066`
- `static/js/compare/index.js:57`
- `static/js/cookbookDownload.js:10`
- `static/js/cookbookRunning.js:337`
- `static/js/cookbookServe.js:21`
- `static/js/document.js:1065`
- `static/js/emailInbox.js:159`
- `static/js/fileHandler.js:201`
- `static/js/group.js:24`
- `static/js/models.js:27`
- `static/js/presets.js:79`
- `static/js/rag.js:12`
- `static/js/research/jobs.js:66`
- `static/js/research/panel.js:206`
- `static/js/research/panel.js:210`
- `static/js/search-chat.js:204`
- `static/js/search.js:14`
- `static/js/tourAutoplay.js:117`
- `static/js/tourAutoplay.js:129`
- `static/js/tourHints.js:158`
- `static/js/tourHints.js:170`
- `static/js/voiceRecorder.js:268`

## `_syncDocIndicator` — function, line 1100
- **called from:**
- `static/js/document.js:1100`
- `static/js/document.js:6495`
- `static/js/document.js:7089`
- `static/js/document.js:7249`
- `static/js/document.js:12399`
- `static/js/document.js:14707`
- `static/js/document.js:15036`
- `static/js/document.js:15060`
- `static/js/document.js:16757`
- `static/js/document.js:17114`
- `static/js/document.js:17536`
- `static/js/documentLibrary.js:1251`
- `static/js/documentLibrary.js:1328`

## `updateArrowVisibility` — function, line 1119
- **called from:**
- `static/js/document.js:1119`
- `static/js/document.js:1247`
- `static/js/document.js:1248`

## `_wireSwipeDismiss` — function, line 1135
- **called from:**
- `static/js/document.js:1135`
- `static/js/document.js:1252`
- `static/js/document.js:7987`

## `getPane` — arrow, line 1142
- **called from:**
- `static/js/document.js:1147`

## `endSwipe` — arrow, line 1177
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `renderTabs` — function, line 1195
- **called from:**
- `static/js/document.js:1195`
- `static/js/document.js:1390`
- `static/js/document.js:1395`
- `static/js/document.js:1459`
- `static/js/document.js:1479`
- `static/js/document.js:6493`
- `static/js/document.js:6608`
- `static/js/document.js:7224`
- `static/js/document.js:7276`
- `static/js/document.js:9339`
- `static/js/document.js:12388`
- `static/js/document.js:14705`
- `static/js/document.js:15034`
- `static/js/document.js:15059`
- `static/js/document.js:16478`
- `static/js/document.js:16492`
- `static/js/document.js:16729`
- `static/js/document.js:16801`
- `static/js/document.js:17233`
- `static/js/document.js:17456`
- `static/js/document.js:17523`

## `_scrollTabIntoView` — arrow, line 1258
- **called from:**
- `static/js/document.js:1282`
- `static/js/document.js:1285`
- `static/js/document.js:1361`

## `startTitleEdit` — function, line 1366
- **called from:**
- `static/js/document.js:1296`
- `static/js/document.js:1366`

## `commitEdit` — function, line 1380
- **called from:**
- `static/js/document.js:1380`
- `static/js/document.js:1403`

## `cancelEdit` — function, line 1393
- **called from:**
- `static/js/document.js:1393`
- `static/js/document.js:1407`

## `initTabDragReorder` — function, line 1413
- **called from:**
- `static/js/document.js:1337`
- `static/js/document.js:1413`

## `showEmptyState` — function, line 1465
- **called from:**
- `static/js/document.js:1465`
- `static/js/document.js:9343`
- `static/js/document.js:12387`
- `static/js/document.js:12433`

## `_showLoadingOverlay` — function, line 1483
- **called from:**
- `static/js/document.js:1483`
- `static/js/document.js:12275`
- `static/js/document.js:12372`

## `_hideLoadingOverlay` — function, line 1500
- **called from:**
- `static/js/document.js:1477`
- `static/js/document.js:1500`
- `static/js/document.js:7056`
- `static/js/document.js:12283`
- `static/js/document.js:12380`
- `static/js/document.js:12429`

## `_isFormBackedDoc` — function, line 1507
- **called from:**
- `static/js/document.js:1507`
- `static/js/document.js:3099`
- `static/js/document.js:3315`
- `static/js/document.js:3321`
- `static/js/document.js:7134`
- `static/js/document.js:7360`
- `static/js/document.js:8222`
- `static/js/document.js:15275`
- `static/js/document.js:16687`
- `static/js/document.js:17241`

## `_dismissDocKb` — function, line 1516
- **called from:**
- `static/js/document.js:1516`
- `static/js/document.js:1531`
- `static/js/document.js:8680`
- `static/js/document.js:8689`
- `static/js/document.js:8702`
- `static/js/document.js:8711`

## `_downloadFilledPdf` — function, line 1529
- **called from:**
- `static/js/document.js:1529`

## `_slug` — arrow, line 1545
- **called from:**
- `routes/document/document_routes.py:1827`
- `routes/document/document_routes.py:1961`
- `static/js/document.js:1546`
- `static/js/document.js:1830`

## `_saveActiveDocBeforeExport` — function, line 1557
- **called from:**
- `static/js/document.js:1532`
- `static/js/document.js:1557`
- `static/js/document.js:1587`
- `static/js/document.js:15415`
- `static/js/document.js:15447`

## `_openExportPdfModal` — function, line 1585
- **called from:**
- `static/js/document.js:1585`

## `close` — arrow, line 1611
- **called from:**
- `app.py:374`
- `app.py:492`
- `app.py:609`
- `app.py:1214`
- `app.py:1358`
- `app.py:1482`
- `companion/pairing.py:151`
- `companion/routes.py:165`
- `core/database.py:161`
- `core/database.py:982`
- `core/database.py:1004`
- `core/database.py:1026`
- `core/database.py:1048`
- `core/database.py:1074`
- `core/database.py:1095`
- `core/database.py:1120`
- `core/database.py:1143`
- `core/database.py:1166`
- `core/database.py:1197`
- `core/database.py:1222`
- `core/database.py:1246`
- `core/database.py:1274`
- `core/database.py:1297`
- `core/database.py:1320`
- `core/database.py:1344`
- `core/database.py:1367`
- `core/database.py:1390`
- `core/database.py:1442`
- `core/database.py:1465`
- `core/database.py:1488`
- `core/database.py:1511`
- `core/database.py:1548`
- `core/database.py:1571`
- `core/database.py:1595`
- `core/database.py:1629`
- `core/database.py:1658`
- `core/database.py:1731`
- `core/database.py:2365`
- `core/database.py:2635`
- `core/database.py:2697`
- `core/database.py:2813`
- `core/database.py:2840`
- `core/database.py:2866`
- `core/database.py:2891`
- `core/database.py:2918`
- `core/database.py:2940`
- `core/database.py:2962`
- `core/database.py:2974`
- `core/database.py:2990`
- `core/session_manager.py:68`
- `core/session_manager.py:177`
- `core/session_manager.py:444`
- `core/session_manager.py:584`
- `core/session_manager.py:619`
- `core/session_manager.py:667`
- `core/session_manager.py:787`
- `core/session_manager.py:876`
- `core/session_manager.py:903`
- `core/session_manager.py:917`
- `core/session_manager.py:973`
- … +1048 more (grep the name in repo)

## `apply` — arrow, line 1708
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

## `clear` — arrow, line 1715
- **called from:**
- `mcp_servers/email_server.py:117`
- `routes/admin_wipe/admin_wipe_routes.py:84`
- `routes/admin_wipe/admin_wipe_routes.py:101`
- `routes/email/email_routes.py:1936`
- `routes/email/email_routes.py:1937`
- `routes/gallery/gallery_routes.py:109`
- `routes/gallery/gallery_routes.py:110`
- `routes/model_routes.py:1506`
- `routes/session_routes.py:1045`
- `routes/shell_routes.py:2077`
- `routes/shell_routes.py:2204`
- `scripts/diffusion_server.py:101`
- `scripts/odysseus_related_flow_audit.py:651`
- `services/search/core.py:986`
- `services/skills/agent_runner.py:52`
- `src/agent_jobs.py:108`
- `src/agent_jobs.py:119`
- `src/agent_jobs.py:120`
- `src/agent_runtime/context_resolution.py:235`
- `src/agent_tools/filesystem_tools.py:645`
- `src/agent_tools/web_tools.py:2711`
- `src/chatgpt_subscription.py:734`
- `src/email_thread_parser.py:318`
- `src/llm_core.py:4555`
- `src/llm_core.py:4556`
- `src/llm_core.py:4754`
- `src/llm_core.py:5114`
- `src/shutdown.py:34`
- `src/skill_index.py:116`
- `src/task_scheduler.py:581`
- `src/tool_index.py:881`
- `tests/cli/test_gallery_cli_tag_filters.py:37`
- `tests/conftest.py:400`
- `tests/smoke/stub_provider.py:69`
- `tests/test_admin_routes_auth_disabled.py:330`
- `tests/test_agent_editor_routes.py:606`
- `tests/test_agent_editor_routes.py:620`
- `tests/test_agent_editor_routes.py:1357`
- `tests/test_agent_state_dir_confinement.py:283`
- `tests/test_api_token_routes.py:160`
- `tests/test_background_tool_jobs.py:38`
- `tests/test_background_tool_jobs.py:87`
- `tests/test_browser_identity_transport.py:85`
- `tests/test_browser_identity_transport.py:85`
- `tests/test_browser_identity_transport.py:109`
- `tests/test_browser_identity_transport.py:120`
- `tests/test_browser_resource_identity.py:92`
- `tests/test_browser_resource_identity.py:92`
- `tests/test_browser_resource_identity.py:112`
- `tests/test_browser_resource_identity.py:113`
- `tests/test_browser_resource_identity.py:271`
- `tests/test_browser_resource_identity.py:271`
- `tests/test_budget_auto_sentinel.py:72`
- `tests/test_budget_auto_sentinel.py:75`
- `tests/test_budget_auto_sentinel.py:80`
- `tests/test_caldav_writeback_route.py:104`
- `tests/test_companion_pairing.py:28`
- `tests/test_context_cache_per_endpoint.py:17`
- `tests/test_context_resolution_route.py:90`
- `tests/test_editor_generation_model_routing.py:242`
- … +197 more (grep the name in repo)

## `_slug` — arrow, line 1829
- **called from:**
- `routes/document/document_routes.py:1827`
- `routes/document/document_routes.py:1961`
- `static/js/document.js:1546`
- `static/js/document.js:1830`

## `_annotationRegexGlobal` — function, line 1859
- **called from:**
- `static/js/document.js:1859`
- `static/js/document.js:1875`
- `static/js/document.js:1907`

## `_escapeAnnotationValue` — function, line 1866
- **called from:**
- `static/js/document.js:1866`
- `static/js/document.js:1899`

## `_unescapeAnnotationValue` — function, line 1869
- **called from:**
- `static/js/document.js:1869`
- `static/js/document.js:1878`

## `_parseAnnotations` — function, line 1873
- **called from:**
- `static/js/document.js:1873`
- `static/js/document.js:2128`
- `static/js/document.js:2850`

## `_annotationLine` — function, line 1895
- **called from:**
- `static/js/document.js:1895`
- `static/js/document.js:1913`

## `_writeAnnotations` — function, line 1906
- **called from:**
- `static/js/document.js:1906`
- `static/js/document.js:1925`
- `static/js/document.js:2863`
- `static/js/document.js:2960`

## `_newAnnotationId` — function, line 1917
- **called from:**
- `static/js/document.js:1917`
- `static/js/document.js:2325`
- `static/js/document.js:2854`

## `_pdfMarkdownFromLive` — function, line 1921
- **called from:**
- `static/js/document.js:1921`
- `static/js/document.js:1946`

## `_pushPdfUndoSnapshot` — function, line 1945
- **called from:**
- `static/js/document.js:1945`
- `static/js/document.js:2335`
- `static/js/document.js:2502`
- `static/js/document.js:2557`
- `static/js/document.js:2570`
- `static/js/document.js:2591`
- `static/js/document.js:2599`
- `static/js/document.js:2634`
- `static/js/document.js:2695`
- `static/js/document.js:2723`
- `static/js/document.js:2749`

## `_undoPdfPaneAction` — function, line 1955
- **called from:**
- `static/js/document.js:1955`
- `static/js/document.js:8672`

## `_setPdfAnnotationDragging` — function, line 1991
- **called from:**
- `static/js/document.js:1991`
- `static/js/document.js:2601`
- `static/js/document.js:2621`
- `static/js/document.js:2636`
- `static/js/document.js:2655`

## `_wirePdfAnnotationMenuDismiss` — function, line 2006
- **called from:**
- `static/js/document.js:2006`
- `static/js/document.js:2788`

## `_setPdfDropMode` — function, line 2024
- **called from:**
- `static/js/document.js:2024`
- `static/js/document.js:8761`
- `static/js/document.js:8762`
- `static/js/document.js:8763`

## `_encodeFieldName` — function, line 2044
- **called from:**
- `static/js/document.js:2044`
- `static/js/document.js:2930`

## `_wirePdfPaneProximity` — function, line 2061
- **called from:**
- `static/js/document.js:2061`
- `static/js/document.js:2099`

## `_pdfResponseErrorMessage` — function, line 2086
- **called from:**
- `static/js/document.js:2086`
- `static/js/document.js:2111`

## `_renderPdfPane` — function, line 2096
- **called from:**
- `static/js/document.js:1979`
- `static/js/document.js:2096`
- `static/js/document.js:2878`
- `static/js/document.js:3026`
- `static/js/document.js:3038`
- `static/js/document.js:3136`
- `static/js/document.js:8764`

## `renderSigUI` — arrow, line 2184
- **called from:**
- `static/js/document.js:2205`
- `static/js/document.js:2222`
- `static/js/document.js:2226`

## `isBlankPageTarget` — arrow, line 2295
- **called from:**
- `static/js/document.js:2299`
- `static/js/document.js:2304`

## `_buildAnnotation` — function, line 2358
- **called from:**
- `static/js/document.js:2288`
- `static/js/document.js:2336`
- `static/js/document.js:2358`

## `_setHandlesVisible` — arrow, line 2437
- **called from:**
- `static/js/document.js:2076`
- `static/js/document.js:2082`
- `static/js/document.js:2447`
- `static/js/document.js:2452`
- `static/js/document.js:2458`
- `static/js/document.js:2462`
- `static/js/document.js:2622`
- `static/js/document.js:2656`

## `_renderSig` — arrow, line 2468
- **called from:**
- `static/js/document.js:2495`
- `static/js/document.js:2504`
- `static/js/document.js:2510`

## `_autoGrow` — arrow, line 2516
- **called from:**
- `static/js/document.js:2561`
- `static/js/document.js:2566`
- `static/js/document.js:2709`
- `static/js/document.js:2732`
- `static/js/document.js:2761`

## `onMove` — arrow, line 2609
- **called from:**
- `static/js/calendar.js:2042`
- `static/js/modalSnap.js:773`
- `static/js/modalSnap.js:797`
- `static/js/windowDrag.js:213`
- `static/js/windowDrag.js:218`
- `static/js/windowDrag.js:223`
- `static/js/windowDrag.js:224`
- `static/js/windowDrag.js:233`
- `static/js/windowDrag.js:241`
- `static/js/windowDrag.js:262`
- `static/js/windowDrag.js:263`

## `onUp` — arrow, line 2617
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `onMove` — arrow, line 2643
- **called from:**
- `static/js/calendar.js:2042`
- `static/js/modalSnap.js:773`
- `static/js/modalSnap.js:797`
- `static/js/windowDrag.js:213`
- `static/js/windowDrag.js:218`
- `static/js/windowDrag.js:223`
- `static/js/windowDrag.js:224`
- `static/js/windowDrag.js:233`
- `static/js/windowDrag.js:241`
- `static/js/windowDrag.js:262`
- `static/js/windowDrag.js:263`

## `onUp` — arrow, line 2651
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_applyLh` — arrow, line 2692
- **called from:**
- `static/js/document.js:2718`
- `static/js/document.js:2719`

## `_applyFs` — arrow, line 2720
- **called from:**
- `static/js/document.js:2735`
- `static/js/document.js:2736`

## `_removeAnnotation` — function, line 2803
- **called from:**
- `static/js/document.js:2592`
- `static/js/document.js:2803`

## `_aiFillAnnotations` — function, line 2817
- **called from:**
- `static/js/document.js:2817`

## `_schedulePdfPaneSave` — function, line 2887
- **called from:**
- `static/js/document.js:2223`
- `static/js/document.js:2280`
- `static/js/document.js:2345`
- `static/js/document.js:2506`
- `static/js/document.js:2562`
- `static/js/document.js:2567`
- `static/js/document.js:2623`
- `static/js/document.js:2657`
- `static/js/document.js:2716`
- `static/js/document.js:2733`
- `static/js/document.js:2762`
- `static/js/document.js:2810`
- `static/js/document.js:2887`

## `_setPdfSaveStatus` — function, line 2893
- **called from:**
- `static/js/document.js:1970`
- `static/js/document.js:1978`
- `static/js/document.js:1982`
- `static/js/document.js:2828`
- `static/js/document.js:2844`
- `static/js/document.js:2876`
- `static/js/document.js:2881`
- `static/js/document.js:2888`
- `static/js/document.js:2893`
- `static/js/document.js:2910`
- `static/js/document.js:2979`
- `static/js/document.js:2985`
- `static/js/document.js:2995`
- `static/js/document.js:2999`
- `static/js/document.js:3002`

## `_savePdfPaneToMarkdown` — function, line 2915
- **called from:**
- `static/js/document.js:1566`
- `static/js/document.js:2890`
- `static/js/document.js:2915`
- `static/js/document.js:3012`
- `static/js/document.js:3024`
- `static/js/document.js:3044`

## `_refreshPdfPreviewIframe` — function, line 3016
- **called from:**
- `static/js/document.js:3016`
- `static/js/document.js:17243`

## `_setPdfViewActive` — function, line 3029
- **called from:**
- `static/js/document.js:3029`
- `static/js/document.js:8223`
- `static/js/document.js:8755`

## `_syncHeaderBarVisibility` — function, line 3065
- **called from:**
- `static/js/document.js:3065`
- `static/js/document.js:3341`
- `static/js/document.js:7720`

## `vis` — arrow, line 3071
- **called from:**
- `static/js/document.js:3083`
- `static/js/document.js:3084`
- `static/js/document.js:3085`
- `static/js/document.js:3086`

## `_syncHeaderActions` — function, line 3090
- **called from:**
- `static/js/document.js:3090`
- `static/js/document.js:7225`
- `static/js/document.js:8277`
- `static/js/document.js:8384`
- `static/js/document.js:8579`
- `static/js/document.js:8590`
- `static/js/document.js:8628`
- `static/js/document.js:12885`
- `static/js/document.js:12898`
- `static/js/document.js:12920`
- `static/js/document.js:16211`
- `static/js/document.js:16237`
- `static/js/document.js:16258`
- `static/js/document.js:16443`
- `static/js/document.js:16702`
- `static/js/document.js:17239`

## `_unfoldEmailHeaderLines` — function, line 3346
- **called from:**
- `static/js/document.js:3346`
- `static/js/document.js:3366`

## `_parseEmailHeader` — function, line 3358
- **called from:**
- `static/js/document.js:3358`
- `static/js/document.js:3431`
- `static/js/document.js:3432`
- `static/js/document.js:3441`
- `static/js/document.js:3677`
- `static/js/document.js:4952`
- `static/js/document.js:5116`
- `static/js/document.js:8210`
- `static/js/document.js:12094`
- `static/js/document.js:12118`
- `static/js/document.js:12181`
- `static/js/document.js:12182`
- `static/js/document.js:16926`
- `static/js/document.js:17014`
- `static/js/document.js:17022`
- `static/js/document.js:17069`
- `static/js/document.js:17070`
- `static/js/document.js:17172`
- `static/js/document.js:17198`
- `static/js/document.js:17577`
- `static/js/document.js:17595`

## `_buildEmailContent` — function, line 3390
- **called from:**
- `static/js/document.js:3390`
- `static/js/document.js:3678`
- `static/js/document.js:7353`
- `static/js/document.js:11992`
- `static/js/document.js:12139`
- `static/js/document.js:17081`

## `_looksLikeWrappedEmailContent` — function, line 3402
- **called from:**
- `static/js/document.js:3402`
- `static/js/document.js:3421`
- `static/js/document.js:3432`

## `_decodeBase64EmailWrapper` — function, line 3407
- **called from:**
- `static/js/document.js:3407`
- `static/js/document.js:3430`
- `static/js/document.js:3438`

## `_sanitizeOutgoingEmailBody` — function, line 3427
- **called from:**
- `static/js/document.js:3427`
- `static/js/document.js:3448`
- `static/js/document.js:3501`
- `static/js/document.js:6335`
- `static/js/document.js:6528`
- `static/js/document.js:6906`

## `_emailLocalDraftKey` — function, line 3457
- **called from:**
- `static/js/document.js:3457`
- `static/js/document.js:3466`
- `static/js/document.js:3511`
- `static/js/document.js:3537`

## `_loadEmailLocalDraft` — function, line 3465
- **called from:**
- `static/js/document.js:3465`
- `static/js/document.js:3485`

## `_emailFieldsWithLocalDraft` — function, line 3484
- **called from:**
- `static/js/document.js:3484`
- `static/js/document.js:4953`

## `keepRealField` — arrow, line 3487
- **called from:**
- `static/js/document.js:3493`
- `static/js/document.js:3494`
- `static/js/document.js:3495`
- `static/js/document.js:3496`
- `static/js/document.js:3497`
- `static/js/document.js:3498`
- `static/js/document.js:3499`
- `static/js/document.js:3500`

## `_persistEmailLocalDraftNow` — function, line 3505
- **called from:**
- `static/js/document.js:3505`

## `_persistEmailLocalDraftSoon` — function, line 3531
- **called from:**
- `static/js/document.js:3531`
- `static/js/document.js:3708`
- `static/js/document.js:4787`
- `static/js/document.js:4802`
- `static/js/document.js:7354`
- `static/js/document.js:8468`
- `static/js/document.js:8805`

## `_clearEmailLocalDraft` — function, line 3536
- **called from:**
- `static/js/document.js:3536`
- `static/js/document.js:3543`
- `static/js/document.js:6475`
- `static/js/document.js:12095`
- `static/js/document.js:17173`
- `static/js/document.js:17199`

## `_clearCurrentEmailLocalDraft` — function, line 3542
- **called from:**
- `static/js/document.js:3542`
- `static/js/document.js:7027`

## `_emailPlainTextToHtml` — function, line 3551
- **called from:**
- `static/js/document.js:3551`
- `static/js/document.js:3606`
- `static/js/document.js:3624`
- `static/js/document.js:3629`
- `static/js/document.js:3640`
- `static/js/document.js:3659`

## `_emailHtmlToPlainText` — function, line 3557
- **called from:**
- `static/js/document.js:3557`
- `static/js/document.js:3646`

## `_sanitizedRichTextHtml` — function, line 3564
- **called from:**
- `static/js/document.js:3564`
- `static/js/document.js:3669`
- `static/js/document.js:7336`

## `_richTextContentToHtml` — function, line 3597
- **called from:**
- `static/js/document.js:3597`
- `static/js/document.js:4587`
- `static/js/document.js:12064`
- `static/js/document.js:15913`

## `_emailQuoteMarkerMatch` — function, line 3609
- **called from:**
- `static/js/document.js:3609`
- `static/js/document.js:3634`

## `_emailBodyFragmentToHtml` — function, line 3615
- **called from:**
- `static/js/document.js:3615`
- `static/js/document.js:3642`
- `static/js/document.js:3651`

## `_emailBodyToHtml` — function, line 3632
- **called from:**
- `static/js/document.js:3632`
- `static/js/document.js:4659`
- `static/js/document.js:4786`
- `static/js/document.js:4801`
- `static/js/document.js:5083`
- `static/js/document.js:6337`
- `static/js/document.js:6530`
- `static/js/document.js:12133`

## `_syncEmailRichbody` — function, line 3664
- **called from:**
- `static/js/document.js:810`
- `static/js/document.js:971`
- `static/js/document.js:3664`
- `static/js/document.js:3929`
- `static/js/document.js:3986`
- `static/js/document.js:4019`
- `static/js/document.js:4204`
- `static/js/document.js:4215`
- `static/js/document.js:4369`
- `static/js/document.js:4516`
- `static/js/document.js:4592`
- `static/js/document.js:5542`
- `static/js/document.js:5767`
- `static/js/document.js:6332`
- `static/js/document.js:6525`
- `static/js/document.js:6901`
- `static/js/document.js:8207`
- `static/js/document.js:8677`
- `static/js/document.js:8699`
- `static/js/document.js:9099`
- `static/js/document.js:9135`
- `static/js/document.js:9514`
- `static/js/document.js:9554`
- `static/js/document.js:9566`
- `static/js/document.js:9587`
- `static/js/document.js:9670`
- `static/js/document.js:9711`
- `static/js/document.js:10081`
- `static/js/document.js:10091`
- `static/js/document.js:10102`
- `static/js/document.js:10192`
- `static/js/document.js:12065`

## `_syncRichEmptyImport` — function, line 3692
- **called from:**
- `static/js/document.js:3672`
- `static/js/document.js:3692`
- `static/js/document.js:4593`
- `static/js/document.js:7218`
- `static/js/document.js:8275`
- `static/js/document.js:16204`

## `_scheduleEmailRichbodySave` — function, line 3705
- **called from:**
- `static/js/document.js:811`
- `static/js/document.js:972`
- `static/js/document.js:3705`
- `static/js/document.js:3930`
- `static/js/document.js:3987`
- `static/js/document.js:4020`
- `static/js/document.js:4216`
- `static/js/document.js:4370`
- `static/js/document.js:4517`
- `static/js/document.js:5543`
- `static/js/document.js:5768`
- `static/js/document.js:8678`
- `static/js/document.js:8700`
- `static/js/document.js:9100`
- `static/js/document.js:9136`
- `static/js/document.js:9515`
- `static/js/document.js:9555`
- `static/js/document.js:9567`
- `static/js/document.js:9588`
- `static/js/document.js:9671`
- `static/js/document.js:9712`
- `static/js/document.js:10082`
- `static/js/document.js:10092`
- `static/js/document.js:10103`
- `static/js/document.js:10193`

## `_richSelectionElement` — function, line 3713
- **called from:**
- `static/js/document.js:3713`
- `static/js/document.js:3723`
- `static/js/document.js:4029`
- `static/js/document.js:5858`

## `_richSelectionListItem` — function, line 3722
- **called from:**
- `static/js/document.js:3722`
- `static/js/document.js:3728`
- `static/js/document.js:3935`
- `static/js/document.js:3961`

## `_richSelectionChecklistItem` — function, line 3727
- **called from:**
- `static/js/document.js:832`
- `static/js/document.js:3727`
- `static/js/document.js:3970`
- `static/js/document.js:3975`
- `static/js/document.js:4462`
- `static/js/document.js:10665`

## `_richChecklistItems` — function, line 3732
- **called from:**
- `static/js/document.js:3732`
- `static/js/document.js:3741`
- `static/js/document.js:3914`
- `static/js/document.js:3920`
- `static/js/document.js:3924`
- `static/js/document.js:3937`
- `static/js/document.js:3943`
- `static/js/document.js:3954`

## `_normalizeRichChecklists` — function, line 3736
- **called from:**
- `static/js/document.js:806`
- `static/js/document.js:3736`
- `static/js/document.js:3913`
- `static/js/document.js:3955`
- `static/js/document.js:3965`
- `static/js/document.js:3985`
- `static/js/document.js:4213`
- `static/js/document.js:4589`

## `_richTextOffsetWithin` — function, line 3749
- **called from:**
- `static/js/document.js:3749`
- `static/js/document.js:3922`
- `static/js/document.js:3938`

## `_richSelectionTextOffsets` — function, line 3760
- **called from:**
- `static/js/document.js:3760`
- `static/js/document.js:3848`

## `_richTextPointAtOffset` — function, line 3774
- **called from:**
- `static/js/document.js:3774`
- `static/js/document.js:3791`
- `static/js/document.js:3792`

## `_restoreRichSelectionTextOffsets` — function, line 3789
- **called from:**
- `static/js/document.js:3789`
- `static/js/document.js:3870`

## `_richSpacingBlocks` — function, line 3801
- **called from:**
- `static/js/document.js:3801`
- `static/js/document.js:3819`
- `static/js/document.js:3851`
- `static/js/document.js:4292`
- `static/js/document.js:10687`

## `_richClosestSpacingBlock` — function, line 3805
- **called from:**
- `static/js/document.js:3805`
- `static/js/document.js:3825`
- `static/js/document.js:3832`

## `_richSelectedSpacingBlockIndexes` — function, line 3814
- **called from:**
- `static/js/document.js:3814`
- `static/js/document.js:3847`
- `static/js/document.js:4293`
- `static/js/document.js:10688`

## `addBlockForNode` — arrow, line 3831
- **called from:**
- `static/js/document.js:3836`
- `static/js/document.js:3837`
- `static/js/document.js:3841`

## `_applyRichLineSpacing` — function, line 3846
- **called from:**
- `static/js/document.js:3846`
- `static/js/document.js:10152`

## `_focusRichTextOffset` — function, line 3874
- **called from:**
- `static/js/document.js:3874`
- `static/js/document.js:3915`

## `_replaceRichChecklist` — function, line 3901
- **called from:**
- `static/js/document.js:3901`
- `static/js/document.js:3928`
- `static/js/document.js:3947`
- `static/js/document.js:3956`

## `_setRichChecklistItemChecked` — function, line 3918
- **called from:**
- `static/js/document.js:833`
- `static/js/document.js:3918`
- `static/js/document.js:4404`
- `static/js/document.js:4465`

## `_toggleRichChecklist` — function, line 3934
- **called from:**
- `static/js/document.js:3934`
- `static/js/document.js:10146`

## `_handleRichChecklistEnter` — function, line 3969
- **called from:**
- `static/js/document.js:3969`
- `static/js/document.js:4469`

## `_handleRichHeadingEnter` — function, line 3992
- **called from:**
- `static/js/document.js:3992`
- `static/js/document.js:4474`

## `_richSelectionInlineCode` — function, line 4028
- **called from:**
- `static/js/document.js:4028`
- `static/js/document.js:4054`
- `static/js/document.js:4082`
- `static/js/document.js:4285`
- `static/js/document.js:10663`

## `_isRichInlineCodeMarker` — function, line 4035
- **called from:**
- `static/js/document.js:3584`
- `static/js/document.js:4031`
- `static/js/document.js:4035`
- `static/js/document.js:4042`

## `_normalizeRichInlineCode` — function, line 4040
- **called from:**
- `static/js/document.js:4040`
- `static/js/document.js:4214`
- `static/js/document.js:4590`

## `_toggleRichInlineCode` — function, line 4047
- **called from:**
- `static/js/document.js:4047`
- `static/js/document.js:10183`

## `_smartRichPasteUrl` — function, line 4091
- **called from:**
- `static/js/document.js:4091`
- `static/js/document.js:4117`

## `_insertSmartRichPasteLink` — function, line 4116
- **called from:**
- `static/js/document.js:4116`
- `static/js/document.js:4365`

## `selectionBlock` — arrow, line 4124
- **called from:**
- `static/js/document.js:4128`
- `static/js/document.js:4128`

## `_cleanRichTextPasteHtml` — function, line 4155
- **called from:**
- `static/js/document.js:4155`
- `static/js/document.js:4367`

## `_wireEmailRichbody` — function, line 4203
- **called from:**
- `static/js/document.js:4203`
- `static/js/document.js:4591`
- `static/js/document.js:5084`

## `syncActiveNow` — arrow, line 4239
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set` — arrow, line 4247
- **called from:**
- `app.py:1330`
- `app.py:1399`
- `companion/routes.py:149`
- `companion/routes.py:149`
- `companion/routes.py:151`
- `core/auth.py:225`
- `core/database.py:67`
- `core/database.py:2262`
- `core/platform_compat.py:221`
- `core/session_manager.py:710`
- `mcp_servers/email_server.py:61`
- `mcp_servers/email_server.py:572`
- `mcp_servers/email_server.py:1020`
- `mcp_servers/email_server.py:1255`
- `mcp_servers/email_server.py:1966`
- `mcp_servers/email_server.py:2029`
- `mcp_servers/email_server.py:2204`
- `mcp_servers/email_server.py:3069`
- `mcp_servers/email_server.py:3431`
- `mcp_servers/email_server.py:3501`
- `mcp_servers/email_server.py:4043`
- `mcp_servers/email_server.py:4044`
- `routes/calendar_routes.py:899`
- `routes/calendar_routes.py:1461`
- `routes/chat_helpers.py:171`
- `routes/chat_routes.py:928`
- `routes/chat_routes.py:928`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:3574`
- `routes/chat_routes.py:3753`
- `routes/chat_routes.py:3797`
- `routes/chat_routes.py:3799`
- `routes/chat_routes.py:3843`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3861`
- `routes/chat_routes.py:3863`
- `routes/chat_routes.py:3879`
- `routes/chat_routes.py:3887`
- `routes/chat_routes.py:3906`
- `routes/chat_routes.py:3907`
- `routes/chat_routes.py:4983`
- `routes/chat_routes.py:4985`
- `routes/chat_routes.py:4987`
- `routes/chat_routes.py:4997`
- `routes/chat_routes.py:5000`
- `routes/chat_routes.py:5004`
- `routes/chat_routes.py:5015`
- `routes/chat_routes.py:5017`
- `routes/chat_routes.py:5059`
- `routes/chatgpt_subscription_routes.py:82`
- `routes/codex_routes.py:89`
- `routes/codex_routes.py:103`
- `routes/codex_routes.py:143`
- `routes/codex_routes.py:183`
- `routes/codex_routes.py:714`
- `routes/codex_routes.py:786`
- `routes/codex_routes.py:864`
- `routes/cookbook_routes.py:2877`
- `routes/cookbook_routes.py:3326`
- `routes/cookbook_routes.py:3872`
- … +2020 more (grep the name in repo)

## `dropdownActive` — arrow, line 4299
- **called from:**
- `static/js/document.js:4306`
- `static/js/document.js:4307`
- `static/js/document.js:4308`
- `static/js/document.js:4309`

## `syncActive` — arrow, line 4311
- **called from:**
- `static/js/document.js:4544`
- `static/js/editor/build/toolbar.js:310`

## `_emailRichbodyActive` — function, line 4562
- **called from:**
- `static/js/document.js:4562`
- `static/js/document.js:4598`
- `static/js/document.js:4623`
- `static/js/document.js:4785`
- `static/js/document.js:4796`
- `static/js/document.js:4809`
- `static/js/document.js:4844`
- `static/js/document.js:5548`
- `static/js/document.js:5733`
- `static/js/document.js:5928`
- `static/js/document.js:6331`
- `static/js/document.js:6524`
- `static/js/document.js:6779`
- `static/js/document.js:6900`
- `static/js/document.js:8206`
- `static/js/document.js:8209`
- `static/js/document.js:8287`
- `static/js/document.js:8673`
- `static/js/document.js:8695`
- `static/js/document.js:9028`
- `static/js/document.js:9059`
- `static/js/document.js:9087`
- `static/js/document.js:9116`
- `static/js/document.js:9155`
- `static/js/document.js:10054`
- `static/js/document.js:10852`
- `static/js/document.js:11264`
- `static/js/document.js:11495`
- `static/js/document.js:12062`
- `static/js/document.js:12072`
- `static/js/document.js:12130`
- `static/js/document.js:13170`
- `static/js/document.js:13228`
- `static/js/document.js:13402`
- `static/js/document.js:13422`
- `static/js/document.js:13466`
- `static/js/document.js:14663`

## `_showRichTextEditor` — function, line 4567
- **called from:**
- `static/js/document.js:4567`
- `static/js/document.js:7208`
- `static/js/document.js:8268`
- `static/js/document.js:14346`
- `static/js/document.js:17158`

## `_captureEmailBodyFocusState` — function, line 4597
- **called from:**
- `static/js/document.js:4597`
- `static/js/document.js:8453`

## `_restoreEmailBodyFocusState` — function, line 4619
- **called from:**
- `static/js/document.js:4619`
- `static/js/document.js:8457`

## `_renderStreamingEmailBody` — function, line 4644
- **called from:**
- `static/js/document.js:4644`
- `static/js/document.js:5146`
- `static/js/document.js:16927`

## `applyBody` — arrow, line 4654
- **called from:**
- `static/js/document.js:4667`
- `static/js/document.js:4685`

## `tick` — arrow, line 4677
- **called from:**
- `src/background_tool_jobs.py:190`
- `tests/test_background_tool_jobs.py:35`
- `tests/test_background_tool_jobs.py:39`
- `tests/test_background_tool_jobs.py:40`
- `tests/test_background_tool_jobs.py:51`
- `tests/test_background_tool_jobs.py:85`
- `tests/test_background_tool_jobs.py:88`
- `tests/test_background_tool_jobs.py:113`
- `tests/test_background_tool_jobs.py:204`
- `tests/test_background_tool_jobs.py:219`
- `static/js/backgroundToolJobs.js:125`
- `static/js/backgroundToolJobs.js:127`
- `static/js/document.js:16847`
- `static/js/editor/build/transform-popup.js:152`
- `static/js/editor/build/transform-popup.js:156`
- `static/js/editor/build/transform-popup.js:159`
- `static/js/escMenuStack.js:101`
- `static/js/galleryEditor.js:891`
- `static/js/galleryEditor.js:14278`
- `static/js/slashCommands.js:2802`

## `_emailQuoteStartIndex` — function, line 4691
- **called from:**
- `static/js/document.js:4691`
- `static/js/document.js:4765`

## `_emailQuoteStartOffset` — function, line 4714
- **called from:**
- `static/js/document.js:4714`
- `static/js/document.js:4758`

## `_splitEmailReplyQuote` — function, line 4746
- **called from:**
- `static/js/document.js:4746`
- `static/js/document.js:4773`
- `static/js/document.js:6763`
- `static/js/document.js:12119`
- `static/js/document.js:12194`
- `static/js/document.js:12195`
- `static/js/document.js:17077`
- `static/js/document.js:17079`

## `_stripEmailReplyQuoteText` — function, line 4772
- **called from:**
- `static/js/document.js:4772`
- `static/js/document.js:4778`

## `_emailReplyOwnText` — function, line 4777
- **called from:**
- `static/js/document.js:4777`
- `static/js/document.js:6231`
- `static/js/document.js:6344`
- `static/js/document.js:6914`
- `static/js/document.js:12121`

## `_setEmailBodyText` — function, line 4781
- **called from:**
- `static/js/document.js:4781`
- `static/js/document.js:4805`
- `static/js/document.js:6844`
- `static/js/document.js:6871`
- `static/js/document.js:6876`
- `static/js/document.js:6884`
- `static/js/document.js:12152`

## `_streamEmailBodyText` — function, line 4790
- **called from:**
- `static/js/document.js:4790`

## `_focusEmailBodyEnd` — function, line 4808
- **called from:**
- `static/js/document.js:4808`
- `static/js/document.js:4965`
- `static/js/document.js:5088`

## `focusEmailReplyBody` — function, line 4842
- **called from:**
- `static/js/document.js:4842`
- `static/js/emailInbox.js:236`

## `_syncEmailHeaderSummary` — function, line 4862
- **called from:**
- `static/js/document.js:4862`
- `static/js/document.js:4898`
- `static/js/document.js:5110`
- `static/js/document.js:5148`
- `static/js/document.js:8466`
- `static/js/document.js:8532`
- `static/js/document.js:8550`

## `_setEmailHeaderInputValue` — function, line 4876
- **called from:**
- `static/js/document.js:4876`
- `static/js/document.js:4957`
- `static/js/document.js:4958`
- `static/js/document.js:4969`
- `static/js/document.js:4970`
- `static/js/document.js:4971`
- `static/js/document.js:4972`
- `static/js/document.js:5099`
- `static/js/document.js:5100`
- `static/js/document.js:5125`
- `static/js/document.js:5126`
- `static/js/document.js:5127`
- `static/js/document.js:5128`
- `static/js/document.js:5129`
- `static/js/document.js:5130`
- `static/js/document.js:5131`
- `static/js/document.js:5132`

## `_setEmailHeaderCollapsed` — function, line 4885
- **called from:**
- `static/js/document.js:4885`
- `static/js/document.js:4910`
- `static/js/document.js:4959`
- `static/js/document.js:8456`
- `static/js/document.js:8472`
- `static/js/document.js:8526`

## `_shouldAutoCollapseEmailHeader` — function, line 4901
- **called from:**
- `static/js/document.js:4901`
- `static/js/document.js:4910`

## `_maybeAutoCollapseEmailHeader` — function, line 4905
- **called from:**
- `static/js/document.js:4905`

## `_showEmailFields` — function, line 4913
- **called from:**
- `static/js/document.js:4913`
- `static/js/document.js:5121`
- `static/js/document.js:7203`
- `static/js/document.js:8262`
- `static/js/document.js:12235`
- `static/js/document.js:14348`
- `static/js/document.js:16726`
- `static/js/document.js:16794`
- `static/js/document.js:17175`
- `static/js/document.js:17200`

## `_withSpinner` — arrow, line 4987
- **called from:**
- `static/js/cookbookServe.js:3109`
- `static/js/cookbookServe.js:3121`
- `static/js/cookbookServe.js:3812`
- `static/js/document.js:5009`
- `static/js/document.js:5036`

## `_syncStreamingEmailFields` — function, line 5114
- **called from:**
- `static/js/document.js:5114`
- `static/js/document.js:16892`

## `_uploadComposeFiles` — function, line 5151
- **called from:**
- `static/js/document.js:5151`
- `static/js/document.js:5228`
- `static/js/document.js:9318`

## `_stageForwardedSourceAttachments` — function, line 5184
- **called from:**
- `static/js/document.js:5111`
- `static/js/document.js:5184`

## `_handleAttachUpload` — function, line 5225
- **called from:**
- `static/js/document.js:5225`

## `_closeOdysseusAttachMenu` — function, line 5233
- **called from:**
- `static/js/document.js:5233`
- `static/js/document.js:5243`
- `static/js/document.js:5248`
- `static/js/document.js:5325`
- `static/js/document.js:5374`
- `static/js/document.js:5616`
- `static/js/document.js:5651`

## `_attachMenuOutsideClick` — function, line 5242
- **called from:**
- `static/js/document.js:5242`

## `_attachMenuEscape` — function, line 5246
- **called from:**
- `static/js/document.js:5246`

## `_positionOdysseusAttachMenu` — function, line 5251
- **called from:**
- `static/js/document.js:5251`
- `static/js/document.js:5649`

## `_odysseusAttachLabel` — function, line 5264
- **called from:**
- `static/js/document.js:5264`
- `static/js/document.js:5415`

## `_stageOdysseusAttachment` — function, line 5271
- **called from:**
- `static/js/document.js:5271`
- `static/js/document.js:5322`
- `static/js/document.js:5369`

## `_stageOdysseusZip` — function, line 5292
- **called from:**
- `static/js/document.js:5292`
- `static/js/document.js:5365`

## `_afterOdysseusAttachmentsAdded` — function, line 5313
- **called from:**
- `static/js/document.js:5313`
- `static/js/document.js:5324`
- `static/js/document.js:5373`

## `_attachOdysseusItem` — function, line 5320
- **called from:**
- `static/js/document.js:5320`
- `static/js/document.js:5451`

## `_selectedOdysseusAttachRows` — function, line 5332
- **called from:**
- `static/js/document.js:5332`
- `static/js/document.js:5337`
- `static/js/document.js:5347`

## `_syncOdysseusAttachSelection` — function, line 5336
- **called from:**
- `static/js/document.js:5336`
- `static/js/document.js:5410`
- `static/js/document.js:5449`
- `static/js/document.js:5454`

## `_attachSelectedOdysseusItems` — function, line 5346
- **called from:**
- `static/js/document.js:5346`
- `static/js/document.js:5664`

## `_loadOdysseusAttachItems` — function, line 5387
- **called from:**
- `static/js/document.js:5387`
- `static/js/document.js:5655`
- `static/js/document.js:5661`
- `static/js/document.js:5669`

## `_hideRichImageToolbar` — function, line 5465
- **called from:**
- `static/js/document.js:5465`
- `static/js/document.js:5484`
- `static/js/document.js:5806`

## `_ensureRichImageToolbar` — function, line 5470
- **called from:**
- `static/js/document.js:5470`
- `static/js/document.js:5838`

## `position` — arrow, line 5483
- **called from:**
- `static/js/colorPicker.js:387`
- `static/js/colorPicker.js:446`
- `static/js/editor/text-edit-overlay.js:17`
- `static/js/editor/text-edit-overlay.js:50`
- `static/js/editor/text-edit-overlay.js:144`
- `static/js/editor/wire-topbar-overflow.js:68`
- `static/js/modalManager.js:166`
- `static/js/tileManager.js:187`

## `_insertRichGalleryImage` — function, line 5517
- **called from:**
- `static/js/document.js:5517`
- `static/js/document.js:5586`

## `_showRichImageSourceMenu` — function, line 5546
- **called from:**
- `static/js/document.js:603`
- `static/js/document.js:5546`
- `static/js/document.js:5609`
- `static/js/document.js:8511`
- `static/js/document.js:8518`

## `close` — arrow, line 5596
- **called from:**
- `app.py:374`
- `app.py:492`
- `app.py:609`
- `app.py:1214`
- `app.py:1358`
- `app.py:1482`
- `companion/pairing.py:151`
- `companion/routes.py:165`
- `core/database.py:161`
- `core/database.py:982`
- `core/database.py:1004`
- `core/database.py:1026`
- `core/database.py:1048`
- `core/database.py:1074`
- `core/database.py:1095`
- `core/database.py:1120`
- `core/database.py:1143`
- `core/database.py:1166`
- `core/database.py:1197`
- `core/database.py:1222`
- `core/database.py:1246`
- `core/database.py:1274`
- `core/database.py:1297`
- `core/database.py:1320`
- `core/database.py:1344`
- `core/database.py:1367`
- `core/database.py:1390`
- `core/database.py:1442`
- `core/database.py:1465`
- `core/database.py:1488`
- `core/database.py:1511`
- `core/database.py:1548`
- `core/database.py:1571`
- `core/database.py:1595`
- `core/database.py:1629`
- `core/database.py:1658`
- `core/database.py:1731`
- `core/database.py:2365`
- `core/database.py:2635`
- `core/database.py:2697`
- `core/database.py:2813`
- `core/database.py:2840`
- `core/database.py:2866`
- `core/database.py:2891`
- `core/database.py:2918`
- `core/database.py:2940`
- `core/database.py:2962`
- `core/database.py:2974`
- `core/database.py:2990`
- `core/session_manager.py:68`
- `core/session_manager.py:177`
- `core/session_manager.py:444`
- `core/session_manager.py:584`
- `core/session_manager.py:619`
- `core/session_manager.py:667`
- `core/session_manager.py:787`
- `core/session_manager.py:876`
- `core/session_manager.py:903`
- `core/session_manager.py:917`
- `core/session_manager.py:973`
- … +1048 more (grep the name in repo)

## `_showComposeAttachMenu` — function, line 5606
- **called from:**
- `static/js/document.js:5606`
- `static/js/document.js:8505`
- `static/js/document.js:8509`

## `_isMarkdownImageFile` — function, line 5672
- **called from:**
- `static/js/document.js:5672`

## `_markdownImageAlt` — function, line 5678
- **called from:**
- `static/js/document.js:5523`
- `static/js/document.js:5678`
- `static/js/document.js:5715`
- `static/js/document.js:5744`

## `_activeDocLanguage` — function, line 5683
- **called from:**
- `static/js/document.js:313`
- `static/js/document.js:5607`
- `static/js/document.js:5683`
- `static/js/document.js:5927`
- `static/js/document.js:8508`
- `static/js/document.js:8510`
- `static/js/document.js:8517`
- `static/js/document.js:8517`
- `static/js/document.js:8815`
- `static/js/document.js:8823`
- `static/js/document.js:8829`

## `_scheduleMarkdownImageAutosave` — function, line 5688
- **called from:**
- `static/js/document.js:5688`
- `static/js/document.js:5728`

## `_insertMarkdownImages` — function, line 5703
- **called from:**
- `static/js/document.js:5703`
- `static/js/document.js:5948`

## `_insertRichTextImages` — function, line 5732
- **called from:**
- `static/js/document.js:5732`
- `static/js/document.js:5947`

## `_normalizeRichTextImages` — function, line 5771
- **called from:**
- `static/js/document.js:4212`
- `static/js/document.js:4588`
- `static/js/document.js:5771`

## `_clearRichImageSelection` — function, line 5805
- **called from:**
- `static/js/document.js:4211`
- `static/js/document.js:4398`
- `static/js/document.js:4456`
- `static/js/document.js:4573`
- `static/js/document.js:5805`
- `static/js/document.js:5825`
- `static/js/document.js:5828`
- `static/js/document.js:5917`

## `_selectRichImage` — function, line 5823
- **called from:**
- `static/js/document.js:4395`
- `static/js/document.js:5539`
- `static/js/document.js:5764`
- `static/js/document.js:5823`
- `static/js/document.js:5884`
- `static/js/document.js:5906`

## `_selectedRichImage` — function, line 5854
- **called from:**
- `static/js/document.js:4283`
- `static/js/document.js:5854`
- `static/js/document.js:9504`
- `static/js/document.js:9519`
- `static/js/document.js:9559`
- `static/js/document.js:10854`

## `_replaceRichImage` — function, line 5863
- **called from:**
- `static/js/document.js:5863`
- `static/js/document.js:9513`
- `static/js/document.js:9586`

## `_replaceRichImageFigure` — function, line 5888
- **called from:**
- `static/js/document.js:5870`
- `static/js/document.js:5888`
- `static/js/document.js:9553`

## `_deleteRichImage` — function, line 5910
- **called from:**
- `static/js/document.js:5509`
- `static/js/document.js:5910`
- `static/js/document.js:9565`

## `_uploadMarkdownImages` — function, line 5921
- **called from:**
- `static/js/document.js:4356`
- `static/js/document.js:4389`
- `static/js/document.js:5921`
- `static/js/document.js:5959`
- `static/js/document.js:8820`
- `static/js/document.js:8834`

## `_handleMarkdownImageUpload` — function, line 5956
- **called from:**
- `static/js/document.js:5956`

## `_renderComposeAttachments` — function, line 5962
- **called from:**
- `static/js/document.js:5094`
- `static/js/document.js:5181`
- `static/js/document.js:5219`
- `static/js/document.js:5314`
- `static/js/document.js:5378`
- `static/js/document.js:5962`
- `static/js/document.js:5991`
- `static/js/document.js:14923`
- `static/js/document.js:14986`

## `_splitRecipientsAndFragment` — function, line 6001
- **called from:**
- `static/js/document.js:6001`
- `static/js/document.js:6015`
- `static/js/document.js:6042`
- `static/js/document.js:6050`
- `static/js/document.js:6095`
- `static/js/document.js:6155`

## `_commitRecipient` — function, line 6013
- **called from:**
- `static/js/document.js:6013`
- `static/js/document.js:6086`
- `static/js/document.js:6087`
- `static/js/document.js:6153`
- `static/js/document.js:6158`
- `static/js/document.js:6164`
- `static/js/document.js:6172`

## `_showContactSearchStatus` — function, line 6030
- **called from:**
- `static/js/document.js:6030`
- `static/js/document.js:6045`
- `static/js/document.js:6053`
- `static/js/document.js:6096`

## `_searchContacts` — function, line 6040
- **called from:**
- `static/js/document.js:6040`
- `static/js/document.js:6109`

## `_wireRecipientAutocomplete` — function, line 6102
- **called from:**
- `static/js/document.js:6102`
- `static/js/document.js:8560`
- `static/js/document.js:8561`
- `static/js/document.js:8562`

## `setActive` — arrow, line 6119
- **called from:**
- `static/app.js:2610`
- `static/js/document.js:6138`
- `static/js/document.js:6144`
- `static/js/group.js:161`
- `static/js/group.js:378`

## `_hideEmailFields` — function, line 6178
- **called from:**
- `static/js/document.js:6178`
- `static/js/document.js:7205`
- `static/js/document.js:8264`
- `static/js/document.js:8273`
- `static/js/document.js:16796`

## `so` — class, line 6218
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_bodyMentionsAttachment` — function, line 6226
- **called from:**
- `static/js/document.js:6226`
- `static/js/document.js:6349`
- `static/js/document.js:6918`

## `_clearMissingAttachmentWarnings` — function, line 6234
- **called from:**
- `static/js/document.js:6234`
- `static/js/document.js:6240`
- `static/js/document.js:6260`
- `static/js/document.js:6352`
- `static/js/document.js:6419`
- `static/js/document.js:6921`
- `static/js/document.js:7025`

## `_confirmMissingAttachment` — function, line 6238
- **called from:**
- `static/js/document.js:6238`
- `static/js/document.js:6350`
- `static/js/document.js:6919`

## `cleanup` — arrow, line 6257
- **called from:**
- `tests/test_browser_producer_live_contract.py:41`
- `tests/test_ca_trust.py:43`
- `static/js/calendar.js:3194`
- `static/js/calendar.js:3202`
- `static/js/calendar.js:3239`
- `static/js/calendar.js:3369`
- `static/js/calendar.js:3378`
- `static/js/chat.js:7613`
- `static/js/chat.js:9104`
- `static/js/chat.js:9112`
- `static/js/chat.js:9118`
- `static/js/chat.js:9121`
- `static/js/chat.js:9124`
- `static/js/chat.js:9147`
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

## `_saveEmailDraftForRecovery` — function, line 6270
- **called from:**
- `static/js/document.js:6270`
- `static/js/document.js:6375`

## `_sendEmail` — function, line 6314
- **called from:**
- `static/js/document.js:6314`
- `static/js/document.js:8306`
- `static/js/document.js:8365`

## `_saveDraft` — function, line 6517
- **called from:**
- `static/js/document.js:6517`
- `static/js/document.js:8429`

## `_discardEmail` — function, line 6575
- **called from:**
- `static/js/document.js:6575`
- `static/js/document.js:7048`

## `_visibleDocIdsForCurrentSession` — function, line 6581
- **called from:**
- `static/js/document.js:6489`
- `static/js/document.js:6581`

## `_closeWithoutDeleting` — function, line 6591
- **called from:**
- `static/js/document.js:6578`
- `static/js/document.js:6591`
- `static/js/document.js:7030`

## `_docAiReplyContextKey` — function, line 6616
- **called from:**
- `static/js/document.js:6616`
- `static/js/document.js:6701`
- `static/js/document.js:6872`

## `_loadDocAiReplyContext` — function, line 6635
- **called from:**
- `static/js/document.js:6635`
- `static/js/document.js:6703`

## `_saveDocAiReplyContext` — function, line 6639
- **called from:**
- `static/js/document.js:6639`
- `static/js/document.js:6705`
- `static/js/document.js:6725`

## `_clearDocAiReplyContext` — function, line 6647
- **called from:**
- `static/js/document.js:6647`
- `static/js/document.js:6872`

## `_closeDocAiReplyChoice` — function, line 6651
- **called from:**
- `static/js/document.js:6651`
- `static/js/document.js:6661`

## `_showDocAiReplyChoice` — function, line 6660
- **called from:**
- `static/js/document.js:6660`
- `static/js/document.js:8444`

## `generateEmailReply` — function, line 6731
- **called from:**
- `static/js/document.js:6731`
- `static/js/emailInbox.js:853`

## `_aiReply` — function, line 6735
- **called from:**
- `static/js/document.js:6727`
- `static/js/document.js:6732`
- `static/js/document.js:6735`

## `cleanAiReplyText` — arrow, line 6746
- **called from:**
- `static/js/document.js:6857`

## `richDraftSnapshot` — arrow, line 6780
- **called from:**
- `static/js/document.js:6789`
- `static/js/document.js:6799`
- `static/js/document.js:6846`

## `markEdited` — arrow, line 6791
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `draftStillUnchanged` — arrow, line 6794
- **called from:**
- `static/js/document.js:6842`
- `static/js/document.js:6853`
- `static/js/document.js:6867`
- `static/js/document.js:6876`
- `static/js/document.js:6884`

## `_scheduleSend` — function, line 6893
- **called from:**
- `static/js/document.js:6893`
- `static/js/document.js:8439`

## `pad` — arrow, line 6975
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

## `escHandler` — arrow, line 6978
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cleanup` — arrow, line 6979
- **called from:**
- `tests/test_browser_producer_live_contract.py:41`
- `tests/test_ca_trust.py:43`
- `static/js/calendar.js:3194`
- `static/js/calendar.js:3202`
- `static/js/calendar.js:3239`
- `static/js/calendar.js:3369`
- `static/js/calendar.js:3378`
- `static/js/chat.js:7613`
- `static/js/chat.js:9104`
- `static/js/chat.js:9112`
- `static/js/chat.js:9118`
- `static/js/chat.js:9121`
- `static/js/chat.js:9124`
- `static/js/chat.js:9147`
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

## `_markUnreadAndClose` — function, line 7040
- **called from:**
- `static/js/document.js:7040`
- `static/js/document.js:8434`

## `switchToDoc` — function, line 7051
- **called from:**
- `static/js/document.js:1282`
- `static/js/document.js:1284`
- `static/js/document.js:1308`
- `static/js/document.js:1316`
- `static/js/document.js:6490`
- `static/js/document.js:6604`
- `static/js/document.js:7051`
- `static/js/document.js:7274`
- `static/js/document.js:7309`
- `static/js/document.js:11839`
- `static/js/document.js:12056`
- `static/js/document.js:12110`
- `static/js/document.js:12269`
- `static/js/document.js:12281`
- `static/js/document.js:12418`
- `static/js/document.js:12427`
- `static/js/document.js:13608`
- `static/js/document.js:13613`
- `static/js/document.js:14702`
- `static/js/document.js:14750`
- `static/js/document.js:15211`
- `static/js/document.js:15215`
- `static/js/document.js:16059`
- `static/js/document.js:16085`
- `static/js/document.js:16286`
- `static/js/document.js:16990`

## `_detachDocFromSession` — function, line 7238
- **called from:**
- `static/js/document.js:7238`
- `static/js/document.js:7258`
- `static/js/document.js:11829`

## `closeTab` — function, line 7252
- **called from:**
- `static/js/document.js:1332`
- `static/js/document.js:7252`
- `static/js/document.js:7992`
- `static/js/document.js:8006`
- `static/js/document.js:14875`

## `_autoCreateFromInput` — function, line 7287
- **called from:**
- `static/js/document.js:7287`
- `static/js/document.js:8780`

## `saveCurrentToMap` — function, line 7324
- **called from:**
- `static/js/document.js:6597`
- `static/js/document.js:7080`
- `static/js/document.js:7254`
- `static/js/document.js:7324`
- `static/js/document.js:8467`
- `static/js/document.js:8551`
- `static/js/document.js:11877`
- `static/js/document.js:14330`
- `static/js/document.js:14997`

## `_minimizeNotesForDocumentOpen` — function, line 7368
- **called from:**
- `static/js/document.js:7368`
- `static/js/document.js:7388`
- `static/js/document.js:12265`

## `openPanel` — function, line 7387
- **called from:**
- `static/app.js:1221`
- `static/js/chat.js:9370`
- `static/js/chat.js:9411`
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

## `reveal` — arrow, line 7840
- **called from:**
- `static/js/documentLibrary.js:157`

## `scheduleReveal` — arrow, line 7862
- **called from:**
- `static/js/document.js:7864`

## `_scheduleHandleIdle` — arrow, line 7882
- **called from:**
- `static/js/document.js:7892`
- `static/js/document.js:7899`

## `_showDividerHandle` — arrow, line 7890
- **called from:**
- `static/js/document.js:7905`

## `_applyMode` — arrow, line 7912
- **called from:**
- `static/js/document.js:7936`
- `static/js/document.js:7939`

## `_onMove` — arrow, line 7936
- **called from:**
- `static/js/signature.js:69`
- `static/js/signature.js:97`
- `static/js/windowDrag.js:305`
- `static/js/windowDrag.js:337`

## `_endDrag` — arrow, line 7967
- **called from:**
- `static/js/features/notes/ui/cardReorder.js:129`
- `static/js/features/notes/ui/cardReorder.js:175`
- `static/js/features/notes/ui/cardReorder.js:176`

## `_syncLangIcon` — arrow, line 8012
- **called from:**
- `static/js/document.js:8028`
- `static/js/document.js:8030`
- `static/js/document.js:8215`

## `_interceptLangSelectValue` — function, line 8020
- **called from:**
- `static/js/document.js:8020`

## `_syncLangPicker` — arrow, line 8039
- **called from:**
- `static/js/document.js:8028`
- `static/js/document.js:8193`
- `static/js/document.js:8216`

## `_initLangPicker` — function, line 8040
- **called from:**
- `static/js/document.js:8040`

## `_buildMenu` — arrow, line 8060
- **called from:**
- `static/js/document.js:8115`

## `_close` — arrow, line 8133
- **called from:**
- `static/js/chat.js:7876`
- `static/js/chat.js:7884`
- `static/js/chat.js:7892`
- `static/js/chat.js:7895`
- `static/js/chatRenderer.js:659`
- `static/js/document.js:8109`
- `static/js/document.js:8140`
- `static/js/document.js:8147`
- `static/js/document.js:8153`
- `static/js/modelPicker.js:210`
- `static/js/modelPicker.js:233`
- `static/js/modelPicker.js:698`
- `static/js/modelPicker.js:826`
- `static/js/modelPicker.js:864`
- `static/js/settings.js:3493`
- `static/js/settings.js:3502`

## `_outsideClick` — arrow, line 8139
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_escKey` — arrow, line 8142
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `handleSendIntent` — arrow, line 8291
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggleSendMenu` — arrow, line 8318
- **called from:**
- `static/js/document.js:8345`

## `handleCaretIntent` — arrow, line 8325
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_applyDocFont` — function, line 8638
- **called from:**
- `static/js/document.js:8638`
- `static/js/document.js:8658`
- `static/js/document.js:8662`

## `_clearRichFindHighlights` — function, line 8902
- **called from:**
- `static/js/document.js:8902`
- `static/js/document.js:8966`
- `static/js/document.js:9047`
- `static/js/document.js:9093`
- `static/js/document.js:9127`
- `static/js/document.js:9158`

## `_buildRichFindRanges` — function, line 8914
- **called from:**
- `static/js/document.js:8914`
- `static/js/document.js:9089`
- `static/js/document.js:9120`
- `static/js/document.js:9164`

## `_renderRichFindRanges` — function, line 8965
- **called from:**
- `static/js/document.js:8965`
- `static/js/document.js:9169`
- `static/js/document.js:9182`

## `_setReplaceVisible` — function, line 8997
- **called from:**
- `static/js/document.js:8997`
- `static/js/document.js:9019`
- `static/js/document.js:9237`

## `_openFindBar` — function, line 9015
- **called from:**
- `static/js/document.js:9015`
- `static/js/document.js:9233`
- `static/js/document.js:9267`

## `lets` — class, line 9023
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_closeFindBar` — function, line 9043
- **called from:**
- `static/js/document.js:9043`
- `static/js/document.js:9243`
- `static/js/document.js:9247`

## `_replaceAllLiteral` — function, line 9064
- **called from:**
- `static/js/document.js:9064`
- `static/js/document.js:9139`

## `_replaceFindCurrent` — function, line 9083
- **called from:**
- `static/js/document.js:9083`
- `static/js/document.js:9248`

## `_replaceFindAll` — function, line 9111
- **called from:**
- `static/js/document.js:9111`
- `static/js/document.js:9248`

## `_doFind` — function, line 9149
- **called from:**
- `static/js/document.js:9040`
- `static/js/document.js:9090`
- `static/js/document.js:9102`
- `static/js/document.js:9107`
- `static/js/document.js:9143`
- `static/js/document.js:9149`
- `static/js/document.js:9231`
- `static/js/document.js:9232`
- `static/js/document.js:9241`
- `static/js/document.js:9244`

## `_isEmailDrag` — arrow, line 9288
- **called from:**
- `static/js/document.js:9297`
- `static/js/document.js:9303`
- `static/js/document.js:9308`
- `static/js/document.js:9313`

## `_normalizeRichLinkUrl` — function, line 9351
- **called from:**
- `static/js/document.js:3575`
- `static/js/document.js:4097`
- `static/js/document.js:4101`
- `static/js/document.js:4106`
- `static/js/document.js:4192`
- `static/js/document.js:9351`
- `static/js/document.js:9394`
- `static/js/document.js:9409`
- `static/js/document.js:9676`

## `_promptLink` — function, line 9362
- **called from:**
- `static/js/document.js:9362`
- `static/js/document.js:9642`

## `done` — function, line 9388
- **called from:**
- `routes/chat_routes.py:4425`
- `routes/cookbook_routes.py:4116`
- `routes/editor_agent_routes.py:1413`
- `routes/editor_agent_routes.py:1612`
- `routes/model_routes.py:1839`
- `services/research/research_handler.py:142`
- `services/skills/job_coordinator.py:214`
- `src/agent_jobs.py:361`
- `src/agent_loop.py:26016`
- `src/agent_loop.py:34320`
- `src/agent_runs.py:85`
- `src/agent_runs.py:140`
- `src/agent_runs.py:169`
- `src/agent_runs.py:198`
- `src/agent_runs.py:209`
- `src/agent_runs.py:248`
- `src/agent_runs.py:297`
- `src/agent_runs.py:308`
- `src/bg_monitor.py:243`
- `src/clean_agent_preview.py:5604`
- `src/containment.py:1218`
- `src/llm_core.py:136`
- `src/mcp_manager.py:439`
- `src/mcp_oauth.py:62`
- `src/mcp_oauth.py:83`
- `src/research_handler.py:504`
- `src/task_scheduler.py:1144`
- `src/task_scheduler.py:2466`
- `src/task_scheduler.py:2493`
- `tests/test_agent_editor_routes.py:1960`
- `tests/test_agent_editor_routes.py:1961`
- `tests/test_agent_editor_routes.py:1970`
- `tests/test_compare_stop_disconnect_poll.py:235`
- `tests/test_compare_stop_disconnect_poll.py:269`
- `tests/test_compare_stop_disconnect_poll.py:283`
- `tests/test_completion_boundary.py:323`
- `tests/test_email_summary_llm.py:191`
- `tests/test_mcp_cache_invalidation.py:98`
- `tests/test_nested_invocation_ownership.py:92`
- `tests/test_nested_invocation_ownership.py:452`
- `tests/test_review_document_conversion.py:56`
- `tests/test_task_scheduler_cache.py:77`
- `static/js/document.js:9388`
- `static/js/document.js:9401`
- `static/js/document.js:9404`
- `static/js/document.js:9407`
- `static/js/document.js:9411`
- `static/js/document.js:9413`
- `static/js/document.js:9414`
- `static/js/document.js:9447`
- `static/js/document.js:9452`
- `static/js/document.js:9454`
- `static/js/document.js:9457`
- `static/js/document.js:9458`
- `static/js/document.js:9485`
- `static/js/document.js:9490`
- `static/js/document.js:9492`
- `static/js/document.js:9495`
- `static/js/document.js:9496`
- `static/js/features/notes/ui/cardRendering.js:60`
- … +1 more (grep the name in repo)

## `submit` — function, line 9393
- **called from:**
- `mcp_servers/email_server.py:1997`
- `routes/model_routes.py:1637`
- `scripts/audit_sft_corpus_with_deepseek.py:310`
- `scripts/cook_sft_alex_conversations.py:270`
- `scripts/generate_sft_environment_expansion.py:348`
- `scripts/generate_sft_flow_variants_with_kimi.py:166`
- `scripts/judge_seeded_harness_replay.py:164`
- `scripts/odysseus_conversation_qa.py:1273`
- `scripts/repair_sft_corpus_with_kimi.py:214`
- `services/search/core.py:1169`
- `src/model_discovery.py:233`
- `src/service_health.py:183`
- `tests/test_auth_config_lock_concurrency.py:75`
- `tests/test_auth_config_lock_concurrency.py:94`
- `tests/test_auth_config_lock_concurrency.py:119`
- `tests/test_auth_config_lock_concurrency.py:145`
- `tests/test_auth_config_lock_concurrency.py:240`
- `tests/test_auth_config_lock_concurrency.py:241`
- `tests/test_replace_messages_upload_reservations.py:243`
- `tests/test_replace_messages_upload_reservations.py:245`
- `tests/test_spec_router_request_scope.py:42`
- `tests/test_spec_router_request_scope.py:43`
- `tests/test_upload_handler_atomicity.py:206`
- `tests/test_upload_handler_atomicity.py:209`
- `tests/test_upload_handler_cleanup.py:312`
- `tests/test_upload_handler_cleanup.py:318`
- `tests/test_upload_handler_cleanup.py:346`
- `tests/test_upload_handler_cleanup.py:348`
- `tests/test_worker_runtime.py:108`
- `static/js/chat.js:8955`
- `static/js/chatRenderer.js:3181`
- `static/js/document.js:9393`
- `static/js/document.js:9416`
- `static/js/document.js:9452`
- `static/js/document.js:9459`
- `static/js/document.js:9490`
- `static/js/document.js:9497`

## `onKey` — function, line 9403
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

## `_promptImageAlt` — function, line 9427
- **called from:**
- `static/js/document.js:9427`
- `static/js/document.js:9509`

## `done` — function, line 9447
- **called from:**
- `routes/chat_routes.py:4425`
- `routes/cookbook_routes.py:4116`
- `routes/editor_agent_routes.py:1413`
- `routes/editor_agent_routes.py:1612`
- `routes/model_routes.py:1839`
- `services/research/research_handler.py:142`
- `services/skills/job_coordinator.py:214`
- `src/agent_jobs.py:361`
- `src/agent_loop.py:26016`
- `src/agent_loop.py:34320`
- `src/agent_runs.py:85`
- `src/agent_runs.py:140`
- `src/agent_runs.py:169`
- `src/agent_runs.py:198`
- `src/agent_runs.py:209`
- `src/agent_runs.py:248`
- `src/agent_runs.py:297`
- `src/agent_runs.py:308`
- `src/bg_monitor.py:243`
- `src/clean_agent_preview.py:5604`
- `src/containment.py:1218`
- `src/llm_core.py:136`
- `src/mcp_manager.py:439`
- `src/mcp_oauth.py:62`
- `src/mcp_oauth.py:83`
- `src/research_handler.py:504`
- `src/task_scheduler.py:1144`
- `src/task_scheduler.py:2466`
- `src/task_scheduler.py:2493`
- `tests/test_agent_editor_routes.py:1960`
- `tests/test_agent_editor_routes.py:1961`
- `tests/test_agent_editor_routes.py:1970`
- `tests/test_compare_stop_disconnect_poll.py:235`
- `tests/test_compare_stop_disconnect_poll.py:269`
- `tests/test_compare_stop_disconnect_poll.py:283`
- `tests/test_completion_boundary.py:323`
- `tests/test_email_summary_llm.py:191`
- `tests/test_mcp_cache_invalidation.py:98`
- `tests/test_nested_invocation_ownership.py:92`
- `tests/test_nested_invocation_ownership.py:452`
- `tests/test_review_document_conversion.py:56`
- `tests/test_task_scheduler_cache.py:77`
- `static/js/document.js:9388`
- `static/js/document.js:9401`
- `static/js/document.js:9404`
- `static/js/document.js:9407`
- `static/js/document.js:9411`
- `static/js/document.js:9413`
- `static/js/document.js:9414`
- `static/js/document.js:9447`
- `static/js/document.js:9452`
- `static/js/document.js:9454`
- `static/js/document.js:9457`
- `static/js/document.js:9458`
- `static/js/document.js:9485`
- `static/js/document.js:9490`
- `static/js/document.js:9492`
- `static/js/document.js:9495`
- `static/js/document.js:9496`
- `static/js/features/notes/ui/cardRendering.js:60`
- … +1 more (grep the name in repo)

## `submit` — function, line 9452
- **called from:**
- `mcp_servers/email_server.py:1997`
- `routes/model_routes.py:1637`
- `scripts/audit_sft_corpus_with_deepseek.py:310`
- `scripts/cook_sft_alex_conversations.py:270`
- `scripts/generate_sft_environment_expansion.py:348`
- `scripts/generate_sft_flow_variants_with_kimi.py:166`
- `scripts/judge_seeded_harness_replay.py:164`
- `scripts/odysseus_conversation_qa.py:1273`
- `scripts/repair_sft_corpus_with_kimi.py:214`
- `services/search/core.py:1169`
- `src/model_discovery.py:233`
- `src/service_health.py:183`
- `tests/test_auth_config_lock_concurrency.py:75`
- `tests/test_auth_config_lock_concurrency.py:94`
- `tests/test_auth_config_lock_concurrency.py:119`
- `tests/test_auth_config_lock_concurrency.py:145`
- `tests/test_auth_config_lock_concurrency.py:240`
- `tests/test_auth_config_lock_concurrency.py:241`
- `tests/test_replace_messages_upload_reservations.py:243`
- `tests/test_replace_messages_upload_reservations.py:245`
- `tests/test_spec_router_request_scope.py:42`
- `tests/test_spec_router_request_scope.py:43`
- `tests/test_upload_handler_atomicity.py:206`
- `tests/test_upload_handler_atomicity.py:209`
- `tests/test_upload_handler_cleanup.py:312`
- `tests/test_upload_handler_cleanup.py:318`
- `tests/test_upload_handler_cleanup.py:346`
- `tests/test_upload_handler_cleanup.py:348`
- `tests/test_worker_runtime.py:108`
- `static/js/chat.js:8955`
- `static/js/chatRenderer.js:3181`
- `static/js/document.js:9393`
- `static/js/document.js:9416`
- `static/js/document.js:9452`
- `static/js/document.js:9459`
- `static/js/document.js:9490`
- `static/js/document.js:9497`

## `onKey` — function, line 9453
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

## `_promptImageCaption` — function, line 9465
- **called from:**
- `static/js/document.js:9465`
- `static/js/document.js:9526`

## `done` — function, line 9485
- **called from:**
- `routes/chat_routes.py:4425`
- `routes/cookbook_routes.py:4116`
- `routes/editor_agent_routes.py:1413`
- `routes/editor_agent_routes.py:1612`
- `routes/model_routes.py:1839`
- `services/research/research_handler.py:142`
- `services/skills/job_coordinator.py:214`
- `src/agent_jobs.py:361`
- `src/agent_loop.py:26016`
- `src/agent_loop.py:34320`
- `src/agent_runs.py:85`
- `src/agent_runs.py:140`
- `src/agent_runs.py:169`
- `src/agent_runs.py:198`
- `src/agent_runs.py:209`
- `src/agent_runs.py:248`
- `src/agent_runs.py:297`
- `src/agent_runs.py:308`
- `src/bg_monitor.py:243`
- `src/clean_agent_preview.py:5604`
- `src/containment.py:1218`
- `src/llm_core.py:136`
- `src/mcp_manager.py:439`
- `src/mcp_oauth.py:62`
- `src/mcp_oauth.py:83`
- `src/research_handler.py:504`
- `src/task_scheduler.py:1144`
- `src/task_scheduler.py:2466`
- `src/task_scheduler.py:2493`
- `tests/test_agent_editor_routes.py:1960`
- `tests/test_agent_editor_routes.py:1961`
- `tests/test_agent_editor_routes.py:1970`
- `tests/test_compare_stop_disconnect_poll.py:235`
- `tests/test_compare_stop_disconnect_poll.py:269`
- `tests/test_compare_stop_disconnect_poll.py:283`
- `tests/test_completion_boundary.py:323`
- `tests/test_email_summary_llm.py:191`
- `tests/test_mcp_cache_invalidation.py:98`
- `tests/test_nested_invocation_ownership.py:92`
- `tests/test_nested_invocation_ownership.py:452`
- `tests/test_review_document_conversion.py:56`
- `tests/test_task_scheduler_cache.py:77`
- `static/js/document.js:9388`
- `static/js/document.js:9401`
- `static/js/document.js:9404`
- `static/js/document.js:9407`
- `static/js/document.js:9411`
- `static/js/document.js:9413`
- `static/js/document.js:9414`
- `static/js/document.js:9447`
- `static/js/document.js:9452`
- `static/js/document.js:9454`
- `static/js/document.js:9457`
- `static/js/document.js:9458`
- `static/js/document.js:9485`
- `static/js/document.js:9490`
- `static/js/document.js:9492`
- `static/js/document.js:9495`
- `static/js/document.js:9496`
- `static/js/features/notes/ui/cardRendering.js:60`
- … +1 more (grep the name in repo)

## `submit` — function, line 9490
- **called from:**
- `mcp_servers/email_server.py:1997`
- `routes/model_routes.py:1637`
- `scripts/audit_sft_corpus_with_deepseek.py:310`
- `scripts/cook_sft_alex_conversations.py:270`
- `scripts/generate_sft_environment_expansion.py:348`
- `scripts/generate_sft_flow_variants_with_kimi.py:166`
- `scripts/judge_seeded_harness_replay.py:164`
- `scripts/odysseus_conversation_qa.py:1273`
- `scripts/repair_sft_corpus_with_kimi.py:214`
- `services/search/core.py:1169`
- `src/model_discovery.py:233`
- `src/service_health.py:183`
- `tests/test_auth_config_lock_concurrency.py:75`
- `tests/test_auth_config_lock_concurrency.py:94`
- `tests/test_auth_config_lock_concurrency.py:119`
- `tests/test_auth_config_lock_concurrency.py:145`
- `tests/test_auth_config_lock_concurrency.py:240`
- `tests/test_auth_config_lock_concurrency.py:241`
- `tests/test_replace_messages_upload_reservations.py:243`
- `tests/test_replace_messages_upload_reservations.py:245`
- `tests/test_spec_router_request_scope.py:42`
- `tests/test_spec_router_request_scope.py:43`
- `tests/test_upload_handler_atomicity.py:206`
- `tests/test_upload_handler_atomicity.py:209`
- `tests/test_upload_handler_cleanup.py:312`
- `tests/test_upload_handler_cleanup.py:318`
- `tests/test_upload_handler_cleanup.py:346`
- `tests/test_upload_handler_cleanup.py:348`
- `tests/test_worker_runtime.py:108`
- `static/js/chat.js:8955`
- `static/js/chatRenderer.js:3181`
- `static/js/document.js:9393`
- `static/js/document.js:9416`
- `static/js/document.js:9452`
- `static/js/document.js:9459`
- `static/js/document.js:9490`
- `static/js/document.js:9497`

## `onKey` — function, line 9491
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

## `_editRichImageAlt` — function, line 9503
- **called from:**
- `static/js/document.js:9503`
- `static/js/document.js:10107`

## `_editRichImageCaption` — function, line 9518
- **called from:**
- `static/js/document.js:9518`
- `static/js/document.js:10108`

## `_applyRichImageAction` — function, line 9558
- **called from:**
- `static/js/document.js:4451`
- `static/js/document.js:9558`
- `static/js/document.js:10148`

## `_richLinkAtRange` — function, line 9592
- **called from:**
- `static/js/document.js:674`
- `static/js/document.js:4288`
- `static/js/document.js:9592`
- `static/js/document.js:9634`
- `static/js/document.js:10078`
- `static/js/document.js:10124`

## `closestLink` — arrow, line 9594
- **called from:**
- `static/js/document.js:9599`
- `static/js/document.js:9600`

## `_restoreRichLinkRange` — function, line 9604
- **called from:**
- `static/js/document.js:9604`
- `static/js/document.js:9648`
- `static/js/document.js:9651`
- `static/js/document.js:9677`
- `static/js/document.js:9697`
- `static/js/document.js:10961`
- `static/js/document.js:11008`
- `static/js/document.js:11041`
- `static/js/document.js:11079`

## `_removeRichLink` — function, line 9614
- **called from:**
- `static/js/document.js:9614`
- `static/js/document.js:9669`
- `static/js/document.js:10080`
- `static/js/document.js:10124`

## `_wysiwygInsertLink` — function, line 9627
- **called from:**
- `static/js/document.js:9627`
- `static/js/document.js:10086`

## `_richSelectionCell` — function, line 9716
- **called from:**
- `static/js/document.js:4281`
- `static/js/document.js:9716`
- `static/js/document.js:9890`
- `static/js/document.js:10853`

## `_focusRichTableCell` — function, line 9727
- **called from:**
- `static/js/document.js:9727`
- `static/js/document.js:9786`
- `static/js/document.js:9823`
- `static/js/document.js:10959`

## `_replaceRichTableCellTag` — function, line 9738
- **called from:**
- `static/js/document.js:9738`
- `static/js/document.js:9761`

## `_richTableHeaderModes` — function, line 9749
- **called from:**
- `static/js/document.js:9749`
- `static/js/document.js:9793`
- `static/js/document.js:9897`

## `_applyRichTableHeaderModes` — function, line 9757
- **called from:**
- `static/js/document.js:9757`
- `static/js/document.js:9800`
- `static/js/document.js:9968`

## `_replaceRichTable` — function, line 9766
- **called from:**
- `static/js/document.js:9766`
- `static/js/document.js:9801`
- `static/js/document.js:9944`
- `static/js/document.js:9954`
- `static/js/document.js:9962`
- `static/js/document.js:9969`

## `_appendRichTableRow` — function, line 9790
- **called from:**
- `static/js/document.js:4515`
- `static/js/document.js:9790`

## `_insertRichTable` — function, line 9804
- **called from:**
- `static/js/document.js:9804`
- `static/js/document.js:9886`

## `_richTableCellHasContent` — function, line 9826
- **called from:**
- `static/js/document.js:9826`
- `static/js/document.js:9842`
- `static/js/document.js:9843`
- `static/js/document.js:9870`
- `static/js/document.js:9876`

## `_richTableCanMergeRight` — function, line 9830
- **called from:**
- `static/js/document.js:9830`
- `static/js/document.js:9840`
- `static/js/document.js:10901`

## `_richTableCanSplitCell` — function, line 9835
- **called from:**
- `static/js/document.js:9835`
- `static/js/document.js:9854`
- `static/js/document.js:10902`

## `_mergeRichTableCellRight` — function, line 9839
- **called from:**
- `static/js/document.js:9839`
- `static/js/document.js:9921`

## `_splitRichTableCell` — function, line 9853
- **called from:**
- `static/js/document.js:9853`
- `static/js/document.js:9924`

## `_applyRichTableAction` — function, line 9883
- **called from:**
- `static/js/document.js:9883`
- `static/js/document.js:10150`

## `_insertRichPageBreak` — function, line 9972
- **called from:**
- `static/js/document.js:9972`
- `static/js/document.js:10174`

## `_applyRichPixelFontSize` — function, line 9995
- **called from:**
- `static/js/document.js:9995`
- `static/js/document.js:10098`
- `static/js/document.js:10143`

## `_applyRichFontFamily` — function, line 10013
- **called from:**
- `static/js/document.js:10013`
- `static/js/document.js:10140`

## `applyMdFormat` — function, line 10042
- **called from:**
- `static/js/document.js:607`
- `static/js/document.js:830`
- `static/js/document.js:976`
- `static/js/document.js:4501`
- `static/js/document.js:4536`
- `static/js/document.js:8888`
- `static/js/document.js:8889`
- `static/js/document.js:8890`
- `static/js/document.js:10042`
- `static/js/document.js:10963`
- `static/js/document.js:11009`
- `static/js/document.js:11042`
- `static/js/document.js:11080`
- `static/js/document.js:11556`

## `_replaceRange` — function, line 10304
- **called from:**
- `static/js/document.js:5723`
- `static/js/document.js:9105`
- `static/js/document.js:9141`
- `static/js/document.js:10276`
- `static/js/document.js:10277`
- `static/js/document.js:10298`
- `static/js/document.js:10304`
- `static/js/document.js:10330`
- `static/js/document.js:10338`
- `static/js/document.js:10348`
- `static/js/document.js:10390`
- `static/js/document.js:10410`
- `static/js/document.js:10419`
- `static/js/document.js:10422`
- `static/js/document.js:10440`
- `static/js/document.js:10447`
- `static/js/document.js:10453`

## `_applyWrapToggle` — function, line 10324
- **called from:**
- `static/js/document.js:10216`
- `static/js/document.js:10324`

## `_currentBlockTag` — function, line 10357
- **called from:**
- `static/js/document.js:4261`
- `static/js/document.js:10180`
- `static/js/document.js:10185`
- `static/js/document.js:10188`
- `static/js/document.js:10357`
- `static/js/document.js:10657`

## `_applyHeadingToggle` — function, line 10373
- **called from:**
- `static/js/document.js:10229`
- `static/js/document.js:10373`

## `_applyLinePrefixToggle` — function, line 10397
- **called from:**
- `static/js/document.js:10238`
- `static/js/document.js:10397`

## `_applyOrderedList` — function, line 10428
- **called from:**
- `static/js/document.js:10222`
- `static/js/document.js:10428`

## `_richColorMenuItems` — function, line 10494
- **called from:**
- `static/js/document.js:10494`
- `static/js/document.js:10819`
- `static/js/document.js:10820`

## `_normalizedRichMenuColor` — function, line 10506
- **called from:**
- `static/js/document.js:10506`
- `static/js/document.js:10513`
- `static/js/document.js:10693`
- `static/js/document.js:10694`
- `static/js/document.js:10702`

## `_richMenuColorHex` — function, line 10512
- **called from:**
- `static/js/document.js:10512`
- `static/js/document.js:10524`
- `static/js/document.js:11062`
- `static/js/document.js:11065`

## `_richContrastTextColor` — function, line 10523
- **called from:**
- `static/js/document.js:10523`
- `static/js/document.js:10547`
- `static/js/document.js:10576`
- `static/js/document.js:10585`

## `_applyRichHighlight` — function, line 10534
- **called from:**
- `static/js/document.js:10136`
- `static/js/document.js:10534`

## `applyNativeHighlight` — arrow, line 10581
- **called from:**
- `static/js/document.js:10606`
- `static/js/document.js:10610`

## `_applyRichDefaultTextColor` — function, line 10619
- **called from:**
- `static/js/document.js:10132`
- `static/js/document.js:10619`

## `_richDropdownCurrentActions` — function, line 10654
- **called from:**
- `static/js/document.js:4271`
- `static/js/document.js:4302`
- `static/js/document.js:10654`
- `static/js/document.js:10855`

## `_showMdDropdown` — function, line 10727
- **called from:**
- `static/js/document.js:5496`
- `static/js/document.js:10727`
- `static/js/document.js:11550`
- `static/js/document.js:11564`

## `ensurePaletteGroup` — arrow, line 10865
- **called from:**
- `static/js/document.js:10968`

## `applyDropdownAction` — arrow, line 10957
- **called from:**
- `static/js/document.js:10966`

## `applySliderSize` — arrow, line 11004
- **called from:**
- `static/js/document.js:11032`

## `applyTypedSize` — arrow, line 11035
- **called from:**
- `static/js/document.js:11052`

## `dismiss` — arrow, line 11100
- **called from:**
- `static/js/document.js:6653`
- `static/js/document.js:7986`
- `static/js/document.js:11128`
- `static/js/document.js:11131`
- `static/js/document.js:11154`
- `static/js/documentLibrary.js:380`
- `static/js/emailLibrary/index.js:4797`
- `static/js/emailLibrary/index.js:4804`
- `static/js/emailLibrary/index.js:4807`
- `static/js/emailLibrary/index.js:4873`
- `static/js/emailLibrary/index.js:4880`
- `static/js/emailLibrary/index.js:4883`
- `static/js/features/notes/ui/panel.js:219`
- `static/js/ui.js:1145`

## `enabledItems` — arrow, line 11113
- **called from:**
- `static/js/document.js:11117`
- `static/js/document.js:11164`

## `close` — arrow, line 11140
- **called from:**
- `app.py:374`
- `app.py:492`
- `app.py:609`
- `app.py:1214`
- `app.py:1358`
- `app.py:1482`
- `companion/pairing.py:151`
- `companion/routes.py:165`
- `core/database.py:161`
- `core/database.py:982`
- `core/database.py:1004`
- `core/database.py:1026`
- `core/database.py:1048`
- `core/database.py:1074`
- `core/database.py:1095`
- `core/database.py:1120`
- `core/database.py:1143`
- `core/database.py:1166`
- `core/database.py:1197`
- `core/database.py:1222`
- `core/database.py:1246`
- `core/database.py:1274`
- `core/database.py:1297`
- `core/database.py:1320`
- `core/database.py:1344`
- `core/database.py:1367`
- `core/database.py:1390`
- `core/database.py:1442`
- `core/database.py:1465`
- `core/database.py:1488`
- `core/database.py:1511`
- `core/database.py:1548`
- `core/database.py:1571`
- `core/database.py:1595`
- `core/database.py:1629`
- `core/database.py:1658`
- `core/database.py:1731`
- `core/database.py:2365`
- `core/database.py:2635`
- `core/database.py:2697`
- `core/database.py:2813`
- `core/database.py:2840`
- `core/database.py:2866`
- `core/database.py:2891`
- `core/database.py:2918`
- `core/database.py:2940`
- `core/database.py:2962`
- `core/database.py:2974`
- `core/database.py:2990`
- `core/session_manager.py:68`
- `core/session_manager.py:177`
- `core/session_manager.py:444`
- `core/session_manager.py:584`
- `core/session_manager.py:619`
- `core/session_manager.py:667`
- `core/session_manager.py:787`
- `core/session_manager.py:876`
- `core/session_manager.py:903`
- `core/session_manager.py:917`
- `core/session_manager.py:973`
- … +1048 more (grep the name in repo)

## `_aiWritingSelectionText` — function, line 11263
- **called from:**
- `static/js/document.js:11263`
- `static/js/document.js:11309`
- `static/js/document.js:11396`

## `_setAiWritingLoading` — function, line 11278
- **called from:**
- `static/js/document.js:11278`
- `static/js/document.js:11419`
- `static/js/document.js:11426`

## `_closeAiWritingMenu` — function, line 11296
- **called from:**
- `static/js/document.js:11296`
- `static/js/document.js:11306`
- `static/js/document.js:11331`
- `static/js/document.js:11338`
- `static/js/document.js:11352`

## `_showAiWritingMenu` — function, line 11305
- **called from:**
- `static/js/document.js:11305`
- `static/js/document.js:11542`

## `dismiss` — arrow, line 11329
- **called from:**
- `static/js/document.js:6653`
- `static/js/document.js:7986`
- `static/js/document.js:11128`
- `static/js/document.js:11131`
- `static/js/document.js:11154`
- `static/js/documentLibrary.js:380`
- `static/js/emailLibrary/index.js:4797`
- `static/js/emailLibrary/index.js:4804`
- `static/js/emailLibrary/index.js:4807`
- `static/js/emailLibrary/index.js:4873`
- `static/js/emailLibrary/index.js:4880`
- `static/js/emailLibrary/index.js:4883`
- `static/js/features/notes/ui/panel.js:219`
- `static/js/ui.js:1145`

## `onKeydown` — arrow, line 11335
- **called from:**
- `static/js/editor/select-and-mask.js:182`

## `here` — class, line 11405
- **called from:**
- `static/js/cookbook-hwfit.js:201`
- `static/js/editor/clipboard-and-drop.js:74`
- `static/js/emailLibrary/signatureFold.js:23`
- `static/js/galleryEditor.js:1686`
- `static/js/galleryEditor.js:1810`
- `static/js/galleryEditor.js:11454`
- `static/js/init.js:419`
- `static/js/settings.js:2210`
- `static/js/slashCommands.js:3509`

## `waitForWritingStream` — arrow, line 11423
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_orderDocumentToolbar` — function, line 11438
- **called from:**
- `static/js/document.js:11438`
- `static/js/document.js:11514`

## `_syncDocumentToolbarSeparators` — function, line 11461
- **called from:**
- `static/js/document.js:3311`
- `static/js/document.js:11461`

## `isVisible` — arrow, line 11463
- **called from:**
- `static/js/chat.js:6105`
- `static/js/chat.js:6190`
- `static/js/cookbook.js:3703`
- `static/js/cookbook.js:3746`
- `static/js/cookbook.js:3784`
- `static/js/cookbook.js:3796`
- `static/js/cookbookRunning.js:3826`
- `static/js/document.js:11467`
- `static/js/document.js:11468`
- `static/js/document.js:11471`
- `static/js/document.js:11472`
- `static/js/editor/panel-visibility.js:61`
- `static/js/editor/panel-visibility.js:143`
- `static/js/galleryEditor.js:11470`
- `static/js/galleryEditor.js:11480`
- `static/js/turnRendering.js:121`
- `static/js/turnRendering.js:131`
- `static/js/turnRendering.js:145`

## `_saveFormatSelection` — function, line 11476
- **called from:**
- `static/js/document.js:11476`
- `static/js/document.js:11524`
- `static/js/document.js:11537`

## `initMdToolbar` — function, line 11504
- **called from:**
- `static/js/document.js:8767`
- `static/js/document.js:11504`

## `updateScrollArrows` — function, line 11582
- **called from:**
- `static/js/document.js:11582`
- `static/js/document.js:11602`

## `syncMdOverflow` — function, line 11600
- **called from:**
- `static/js/document.js:11600`

## `closeMdMenu` — function, line 11605
- **called from:**
- `static/js/document.js:11605`
- `static/js/document.js:11628`

## `_getDocRecent` — function, line 11652
- **called from:**
- `static/js/document.js:11652`
- `static/js/document.js:11656`
- `static/js/document.js:11680`

## `_trackDocAction` — function, line 11655
- **called from:**
- `static/js/document.js:11655`
- `static/js/document.js:11725`
- `static/js/document.js:11773`

## `initActionOverflow` — function, line 11662
- **called from:**
- `static/js/document.js:11662`

## `syncOverflow` — function, line 11672
- **called from:**
- `static/js/document.js:11672`
- `static/js/document.js:11736`
- `static/js/editor/wire-topbar-overflow.js:84`
- `static/js/editor/wire-topbar-overflow.js:94`

## `closeMenu` — function, line 11745
- **called from:**
- `static/js/calendar.js:643`
- `static/js/calendar.js:648`
- `static/js/chatRenderer.js:2414`
- `static/js/chatRenderer.js:2592`
- `static/js/compare/panes.js:674`
- `static/js/compare/panes.js:923`
- `static/js/cookbookServe.js:2647`
- `static/js/cookbookServe.js:2776`
- `static/js/cookbookServe.js:2814`
- `static/js/cookbookServe.js:2836`
- `static/js/cookbookServe.js:2866`
- `static/js/document.js:11730`
- `static/js/document.js:11734`
- `static/js/document.js:11745`
- `static/js/document.js:11767`
- `static/js/editor/wire-selection-controls.js:302`
- `static/js/editor/wire-selection-controls.js:305`

## `initDividerDrag` — function, line 11784
- **called from:**
- `static/js/document.js:7871`
- `static/js/document.js:11784`
- `static/js/document.js:11964`

## `_ensureDocChipRegistered` — function, line 11819
- **called from:**
- `static/js/document.js:11819`
- `static/js/document.js:11886`
- `static/js/document.js:12416`

## `closePanel` — function, line 11845
- **called from:**
- `static/app.js:797`
- `static/app.js:805`
- `static/app.js:894`
- `static/app.js:895`
- `static/app.js:994`
- `static/app.js:2065`
- `static/js/document.js:1134`
- `static/js/document.js:1184`
- `static/js/document.js:6409`
- `static/js/document.js:6491`
- `static/js/document.js:6606`
- `static/js/document.js:7270`
- `static/js/document.js:7371`
- `static/js/document.js:7437`
- `static/js/document.js:7909`
- `static/js/document.js:7988`
- `static/js/document.js:7991`
- `static/js/document.js:8878`
- `static/js/document.js:11845`
- `static/js/document.js:12419`
- `static/js/document.js:16088`
- `static/js/document.js:17535`
- `static/js/features/notes/ui/panel.js:114`
- `static/js/features/notes/ui/panel.js:208`
- `static/js/features/notes/ui/panel.js:232`
- `static/js/features/notes/ui/panel.js:321`
- `static/js/features/notes/ui/panel.js:381`
- `static/js/features/notes/ui/panel.js:477`
- `static/js/research/panel.js:232`
- `static/js/research/panel.js:283`
- `static/js/research/panel.js:297`
- `static/js/research/panel.js:344`
- `static/js/research/panel.js:1798`
- `static/js/sessions.js:2582`
- `static/js/sessions.js:2701`
- `static/js/slashCommands.js:1241`

## `_dropKb` — arrow, line 11868
- **called from:**
- `static/js/document.js:11872`

## `_finishClose` — arrow, line 11899
- **called from:**
- `static/js/document.js:11936`

## `swapSide` — function, line 11941
- **called from:**
- `static/js/document.js:11941`
- `static/js/sidebar-layout.js:171`
- `static/js/sidebar-layout.js:210`
- `static/js/sidebar-layout.js:243`

## `newDocument` — function, line 11973
- **called from:**
- `static/app.js:1306`
- `static/js/document.js:1088`
- `static/js/document.js:11973`

## `openEmailDraft` — function, line 11986
- **called from:**
- `static/js/document.js:11986`
- `static/js/emailInbox.js:847`
- `static/js/emailLibrary/index.js:5834`

## `createDocument` — function, line 12023
- **called from:**
- `static/js/document.js:1354`
- `static/js/document.js:11981`
- `static/js/document.js:12023`

## `injectFreshDoc` — function, line 12088
- **called from:**
- `static/js/chat.js:9412`
- `static/js/document.js:12019`
- `static/js/document.js:12088`
- `static/js/emailInbox.js:1136`
- `static/js/emailInbox.js:1511`

## `replaceEmailReplyBody` — function, line 12115
- **called from:**
- `static/js/chatStream.js:257`
- `static/js/document.js:12115`
- `static/js/emailInbox.js:1067`

## `_buildEmailContentFromFields` — function, line 12158
- **called from:**
- `static/js/document.js:12158`
- `static/js/document.js:12233`

## `ensureEmailDraftEnvelope` — function, line 12178
- **called from:**
- `static/js/document.js:12178`
- `static/js/emailInbox.js:1063`

## `_ensureDocPaneMounted` — function, line 12246
- **called from:**
- `static/js/document.js:12099`
- `static/js/document.js:12104`
- `static/js/document.js:12246`
- `static/js/document.js:12268`
- `static/js/document.js:12274`
- `static/js/document.js:13464`

## `loadDocument` — function, line 12264
- **called from:**
- `static/js/chat.js:5816`
- `static/js/chat.js:9371`
- `static/js/chat.js:9413`
- `static/js/chatStream.js:256`
- `static/js/document.js:5015`
- `static/js/document.js:12264`
- `static/js/document.js:12300`
- `static/js/document.js:13461`
- `static/js/document.js:13607`
- `static/js/document.js:14922`
- `static/js/document.js:14985`
- `static/js/emailInbox.js:1060`
- `static/js/emailInbox.js:1139`
- `static/js/emailInbox.js:1513`
- `static/js/slashCommands.js:4849`

## `_maybeOpenDocFromHash` — function, line 12298
- **called from:**
- `static/js/document.js:1095`
- `static/js/document.js:12298`

## `ensureDocPanel` — function, line 12304
- **called from:**
- `static/app.js:2078`
- `static/js/document.js:12304`
- `static/js/slashCommands.js:1250`

## `_autoCreateSession` — function, line 12320
- **called from:**
- `static/js/document.js:1348`
- `static/js/document.js:7294`
- `static/js/document.js:11978`
- `static/js/document.js:11989`
- `static/js/document.js:12309`
- `static/js/document.js:12320`
- `static/js/document.js:14714`
- `static/js/document.js:14730`
- `static/js/document.js:14947`

## `loadSessionDocs` — function, line 12359
- **called from:**
- `static/app.js:2076`
- `static/app.js:3845`
- `static/js/document.js:12316`
- `static/js/document.js:12359`
- `static/js/sessions.js:2580`
- `static/js/sessions.js:3972`
- `static/js/slashCommands.js:1248`

## `addDocToTabs` — function, line 12438
- **called from:**
- `static/js/document.js:7305`
- `static/js/document.js:12045`
- `static/js/document.js:12098`
- `static/js/document.js:12280`
- `static/js/document.js:12397`
- `static/js/document.js:12438`
- `static/js/document.js:14701`
- `static/js/document.js:14971`
- `static/js/document.js:15210`
- `static/js/document.js:15214`
- `static/js/document.js:16058`

## `populateEditor` — function, line 12459
- **called from:**
- `static/js/document.js:12459`
- `static/js/document.js:17425`

## `_postProcessMarkdown` — function, line 12474
- **called from:**
- `static/js/document.js:12474`
- `static/js/document.js:12653`

## `renderFindRects` — function, line 12524
- **called from:**
- `static/js/document.js:8846`
- `static/js/document.js:9058`
- `static/js/document.js:9200`
- `static/js/document.js:9226`
- `static/js/document.js:12524`

## `applyFindMarks` — function, line 12585
- **called from:**
- `static/js/document.js:9056`
- `static/js/document.js:9160`
- `static/js/document.js:9199`
- `static/js/document.js:9222`
- `static/js/document.js:12585`
- `static/js/document.js:12657`

## `syncHighlighting` — function, line 12625
- **called from:**
- `static/js/document.js:1478`
- `static/js/document.js:4784`
- `static/js/document.js:5068`
- `static/js/document.js:7113`
- `static/js/document.js:8231`
- `static/js/document.js:8663`
- `static/js/document.js:11806`
- `static/js/document.js:12067`
- `static/js/document.js:12470`
- `static/js/document.js:12625`
- `static/js/document.js:12884`
- `static/js/document.js:12897`
- `static/js/document.js:12919`
- `static/js/document.js:13883`
- `static/js/document.js:14304`
- `static/js/document.js:14351`
- `static/js/document.js:14392`
- `static/js/document.js:16658`
- `static/js/document.js:16666`
- `static/js/document.js:16799`
- `static/js/document.js:16876`
- `static/js/document.js:16937`
- `static/js/document.js:16975`
- `static/js/document.js:17166`
- `static/js/document.js:17179`
- `static/js/document.js:17309`
- `static/js/document.js:17411`

## `_lineNumberContentEl` — function, line 12675
- **called from:**
- `static/js/document.js:12675`
- `static/js/document.js:12813`
- `static/js/document.js:12842`
- `static/js/document.js:14156`

## `_lineNumberStyleSignature` — function, line 12686
- **called from:**
- `static/js/document.js:12686`
- `static/js/document.js:12816`

## `_textareaTextWidth` — function, line 12701
- **called from:**
- `static/js/document.js:12701`
- `static/js/document.js:12815`

## `_lineHeightPx` — function, line 12707
- **called from:**
- `static/js/document.js:12707`
- `static/js/document.js:12750`

## `_lineNumberMeasureEl` — function, line 12714
- **called from:**
- `static/js/document.js:12714`
- `static/js/document.js:12748`

## `_syncLineNumberMeasureStyle` — function, line 12729
- **called from:**
- `static/js/document.js:12729`
- `static/js/document.js:12749`

## `_measureLineNumberHeights` — function, line 12747
- **called from:**
- `static/js/document.js:12747`
- `static/js/document.js:12829`

## `_renderLineNumberRows` — function, line 12758
- **called from:**
- `static/js/document.js:12758`
- `static/js/document.js:12830`

## `_scheduleLineNumberRerender` — function, line 12775
- **called from:**
- `static/js/document.js:12775`

## `run` — arrow, line 12777
- **called from:**
- `app.py:1228`
- `app.py:1530`
- `core/platform_compat.py:428`
- `core/platform_compat.py:469`
- `launcher.py:114`
- `launcher.py:149`
- `mcp_servers/email_server.py:4704`
- `mcp_servers/email_server.py:4710`
- `mcp_servers/email_server.py:4710`
- `mcp_servers/image_gen_server.py:188`
- `mcp_servers/image_gen_server.py:192`
- `mcp_servers/image_gen_server.py:192`
- `mcp_servers/memory_server.py:281`
- `mcp_servers/memory_server.py:285`
- `mcp_servers/memory_server.py:285`
- `mcp_servers/rag_server.py:156`
- `mcp_servers/rag_server.py:160`
- `mcp_servers/rag_server.py:160`
- `routes/cookbook_routes.py:1527`
- `routes/cookbook_routes.py:3626`
- `routes/cookbook_routes.py:3639`
- `routes/cookbook_routes.py:3650`
- `routes/cookbook_routes.py:3711`
- `routes/cookbook_routes.py:4177`
- `routes/cookbook_routes.py:4179`
- `routes/cookbook_routes.py:4201`
- `routes/cookbook_routes.py:4203`
- `routes/cookbook_routes.py:4368`
- `routes/cookbook_routes.py:4378`
- `routes/document/document_routes.py:489`
- `routes/email/email_routes.py:5062`
- `routes/email/email_routes.py:6861`
- `routes/hwfit_routes.py:147`
- `scripts/build_frontend.py:69`
- `scripts/build_frontend.py:70`
- `scripts/check_brotli.py:39`
- `scripts/css_snapshot.py:92`
- `scripts/css_snapshot.py:131`
- `scripts/diffusion_server.py:1506`
- `scripts/dump_agent_prompt.py:415`
- `scripts/eval_exact_file_routing.py:202`
- `scripts/eval_followup_domain_continuity.py:209`
- `scripts/eval_odysseus_everyday_live_hard.py:586`
- `scripts/eval_odysseus_live_hard_examples.py:464`
- `scripts/eval_qwen_tool_groups_stream.py:276`
- `scripts/mlx_image_server.py:207`
- `scripts/mlx_image_server.py:281`
- `scripts/mlx_image_server.py:379`
- `scripts/mlx_image_server.py:466`
- `scripts/pr_blocker_audit.py:253`
- `scripts/probe_browser_budget.py:112`
- `scripts/probe_empty_search_recovery.py:90`
- `scripts/probe_fixed_search_evidence.py:81`
- `scripts/ref_parity_audit.py:142`
- `scripts/ref_parity_audit.py:232`
- `scripts/review_sft_environment_expansion.py:115`
- `scripts/run_odysseus_cases_chunked.py:107`
- `scripts/run_odysseus_search_teacher_pipeline.py:305`
- `scripts/run_odysseus_search_teacher_pipeline.py:412`
- `scripts/test_clean_tool_loop.py:209`
- … +1417 more (grep the name in repo)

## `_ensureLineNumberResizeObserver` — function, line 12789
- **called from:**
- `static/js/document.js:12789`
- `static/js/document.js:12818`

## `updateLineNumbers` — function, line 12806
- **called from:**
- `static/js/document.js:5689`
- `static/js/document.js:8794`
- `static/js/document.js:11808`
- `static/js/document.js:12667`
- `static/js/document.js:12780`
- `static/js/document.js:12806`
- `static/js/document.js:14305`
- `static/js/document.js:14444`
- `static/js/document.js:16854`
- `static/js/document.js:16867`
- `static/js/document.js:16904`

## `syncGutterScroll` — function, line 12838
- **called from:**
- `static/js/document.js:8841`
- `static/js/document.js:12825`
- `static/js/document.js:12834`
- `static/js/document.js:12838`

## `_looksLikeMarkdown` — function, line 12848
- **called from:**
- `static/js/document.js:12848`
- `static/js/document.js:12891`

## `attemptAutoDetect` — function, line 12864
- **called from:**
- `static/js/document.js:12864`
- `static/js/document.js:16938`
- `static/js/document.js:17148`

## `_richRootText` — function, line 12932
- **called from:**
- `static/js/document.js:12932`
- `static/js/document.js:12979`
- `static/js/document.js:13171`
- `static/js/document.js:13468`

## `_richRangeFromOffsets` — function, line 12939
- **called from:**
- `static/js/document.js:12939`
- `static/js/document.js:13230`
- `static/js/document.js:13523`

## `updateRichSelectionState` — function, line 12965
- **called from:**
- `static/js/document.js:4321`
- `static/js/document.js:4326`
- `static/js/document.js:12965`

## `_scheduleSelRerender` — function, line 13002
- **called from:**
- `static/js/document.js:8664`
- `static/js/document.js:13002`

## `_ensureSelResizeObserver` — function, line 13018
- **called from:**
- `static/js/document.js:13018`
- `static/js/document.js:13034`

## `updateSelectionState` — function, line 13028
- **called from:**
- `static/js/document.js:9326`
- `static/js/document.js:13028`

## `showSelectionBadge` — function, line 13068
- **called from:**
- `static/js/document.js:12989`
- `static/js/document.js:13063`
- `static/js/document.js:13068`
- `static/js/document.js:13261`
- `static/js/document.js:13430`
- `static/js/document.js:13519`

## `_isCodeDoc` — function, line 13134
- **called from:**
- `static/js/document.js:13134`
- `static/js/document.js:13295`

## `_measurePos` — function, line 13146
- **called from:**
- `static/js/document.js:13146`
- `static/js/document.js:13341`
- `static/js/document.js:13342`
- `static/js/document.js:14480`
- `static/js/document.js:14481`

## `_validateSelections` — function, line 13168
- **called from:**
- `static/js/document.js:13168`
- `static/js/document.js:13227`
- `static/js/document.js:13445`

## `renderAllSelectionHighlights` — function, line 13209
- **called from:**
- `static/js/document.js:12990`
- `static/js/document.js:13007`
- `static/js/document.js:13064`
- `static/js/document.js:13209`
- `static/js/document.js:13390`
- `static/js/document.js:13429`
- `static/js/document.js:13520`

## `addRect` — arrow, line 13345
- **called from:**
- `static/js/document.js:13372`
- `static/js/document.js:13375`
- `static/js/document.js:13379`
- `static/js/document.js:13381`
- `static/js/document.js:14496`
- `static/js/document.js:14498`
- `static/js/document.js:14501`
- `static/js/document.js:14502`

## `syncSelectionOverlay` — function, line 13388
- **called from:**
- `static/js/document.js:8842`
- `static/js/document.js:13388`
- `static/js/document.js:13536`

## `clearSelection` — function, line 13394
- **called from:**
- `static/js/document.js:4217`
- `static/js/document.js:7096`
- `static/js/document.js:8775`
- `static/js/document.js:8869`
- `static/js/document.js:9334`
- `static/js/document.js:13125`
- `static/js/document.js:13394`
- `static/js/document.js:13449`
- `static/js/document.js:13454`
- `static/js/document.js:14618`
- `static/js/features/notes/ui/selection.js:10`
- `static/js/features/notes/ui/selection.js:22`
- `static/js/features/notes/ui/selection.js:52`
- `static/js/features/notes/ui/toolbar.js:38`
- `static/js/sessions.js:2294`
- `static/js/sessions.js:2797`

## `clearSelectionAt` — function, line 13417
- **called from:**
- `static/js/document.js:13110`
- `static/js/document.js:13255`
- `static/js/document.js:13332`
- `static/js/document.js:13363`
- `static/js/document.js:13417`

## `getSelectionContext` — function, line 13439
- **called from:**
- `static/js/chat.js:3015`
- `static/js/document.js:13439`

## `restoreSelectionReference` — function, line 13459
- **called from:**
- `static/js/document.js:13459`

## `lineStart` — arrow, line 13493
- **called from:**
- `static/js/document.js:13503`
- `static/js/document.js:13504`

## `_selectSuggestionText` — function, line 13546
- **called from:**
- `static/js/document.js:13546`
- `static/js/document.js:13696`

## `_clearSuggestionTextSelection` — function, line 13555
- **called from:**
- `static/js/document.js:13555`
- `static/js/document.js:13677`
- `static/js/document.js:14436`

## `_saveSuggestionsToStorage` — function, line 13570
- **called from:**
- `static/js/document.js:13570`
- `static/js/document.js:13642`
- `static/js/document.js:14364`
- `static/js/document.js:14434`

## `_restoreSuggestionsFromStorage` — function, line 13581
- **called from:**
- `static/js/document.js:7230`
- `static/js/document.js:13581`

## `handleDocSuggestions` — function, line 13600
- **called from:**
- `static/js/chat.js:5872`
- `static/js/document.js:13600`

## `_showCurrentSuggestion` — function, line 13665
- **called from:**
- `static/js/document.js:13590`
- `static/js/document.js:13649`
- `static/js/document.js:13665`
- `static/js/document.js:13778`
- `static/js/document.js:13786`
- `static/js/document.js:14373`
- `static/js/document.js:14376`

## `_positionCard` — function, line 13701
- **called from:**
- `static/js/document.js:13701`
- `static/js/document.js:13811`
- `static/js/document.js:13814`

## `_reposition` — arrow, line 13814
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_showInlineDiff` — function, line 13829
- **called from:**
- `static/js/document.js:13829`

## `_clearInlineDiff` — function, line 13879
- **called from:**
- `static/js/document.js:13674`
- `static/js/document.js:13879`
- `static/js/document.js:14437`

## `_computeLineDiff` — function, line 13892
- **called from:**
- `static/js/document.js:13892`
- `static/js/document.js:13968`
- `static/js/document.js:14200`
- `static/js/document.js:14257`

## `_buildDiffChunks` — function, line 13927
- **called from:**
- `static/js/document.js:13927`
- `static/js/document.js:13969`

## `enterDiffMode` — function, line 13961
- **called from:**
- `static/js/document.js:8741`
- `static/js/document.js:13961`
- `static/js/document.js:16991`

## `_renderDiffOverlay` — function, line 13994
- **called from:**
- `static/js/document.js:13983`
- `static/js/document.js:13994`

## `_renderDiffToolbar` — function, line 14061
- **called from:**
- `static/js/document.js:13984`
- `static/js/document.js:14061`

## `_renderDiffGutter` — function, line 14093
- **called from:**
- `static/js/document.js:13985`
- `static/js/document.js:14093`

## `_updateDiffStatus` — function, line 14139
- **called from:**
- `static/js/document.js:14072`
- `static/js/document.js:14139`
- `static/js/document.js:14181`

## `_scrollToDiffChunk` — function, line 14146
- **called from:**
- `static/js/document.js:13986`
- `static/js/document.js:14146`
- `static/js/document.js:14191`

## `_resolveChunk` — function, line 14161
- **called from:**
- `static/js/document.js:14120`
- `static/js/document.js:14126`
- `static/js/document.js:14161`

## `_applyResolvedChunksToTextarea` — function, line 14197
- **called from:**
- `static/js/document.js:14184`
- `static/js/document.js:14197`

## `_resolveAllChunks` — function, line 14228
- **called from:**
- `static/js/document.js:14077`
- `static/js/document.js:14082`
- `static/js/document.js:14228`

## `exitDiffMode` — function, line 14240
- **called from:**
- `static/js/document.js:7057`
- `static/js/document.js:8718`
- `static/js/document.js:8861`
- `static/js/document.js:13601`
- `static/js/document.js:13962`
- `static/js/document.js:14188`
- `static/js/document.js:14236`
- `static/js/document.js:14240`
- `static/js/document.js:16712`
- `static/js/document.js:16714`
- `static/js/document.js:16989`
- `static/js/document.js:16992`

## `isDiffModeActive` — function, line 14316
- **called from:**
- `static/js/document.js:14316`

## `_applySuggestions` — function, line 14326
- **called from:**
- `static/js/document.js:13789`
- `static/js/document.js:13800`
- `static/js/document.js:14326`

## `_animateNext` — function, line 14363
- **called from:**
- `static/js/document.js:13791`
- `static/js/document.js:13795`
- `static/js/document.js:13803`
- `static/js/document.js:14363`

## `_esc` — function, line 14380
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
- `static/js/chat.js:6329`
- `static/js/chat.js:6329`
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

## `acceptSuggestion` — function, line 14385
- **called from:**
- `static/js/document.js:14385`

## `dismissSuggestion` — function, line 14413
- **called from:**
- `static/js/document.js:14413`

## `clearAllSuggestions` — function, line 14431
- **called from:**
- `static/js/document.js:14431`

## `_highlightSuggestionText` — function, line 14448
- **called from:**
- `static/js/document.js:13743`
- `static/js/document.js:14448`

## `addRect` — arrow, line 14484
- **called from:**
- `static/js/document.js:13372`
- `static/js/document.js:13375`
- `static/js/document.js:13379`
- `static/js/document.js:13381`
- `static/js/document.js:14496`
- `static/js/document.js:14498`
- `static/js/document.js:14501`
- `static/js/document.js:14502`

## `_clearSuggestionHighlight` — function, line 14509
- **called from:**
- `static/js/document.js:13673`
- `static/js/document.js:13742`
- `static/js/document.js:14403`
- `static/js/document.js:14422`
- `static/js/document.js:14435`
- `static/js/document.js:14449`
- `static/js/document.js:14509`

## `runDocument` — function, line 14515
- **called from:**
- `static/js/document.js:8576`
- `static/js/document.js:14515`
- `static/js/document.js:14860`

## `copyDocument` — function, line 14573
- **called from:**
- `static/js/document.js:8007`
- `static/js/document.js:14573`
- `static/js/document.js:14859`

## `_closeDocTabMenu` — function, line 14590
- **called from:**
- `static/js/document.js:14590`
- `static/js/document.js:14652`
- `static/js/document.js:14742`
- `static/js/document.js:14764`
- `static/js/document.js:14772`
- `static/js/document.js:14856`

## `_moveDocToSession` — function, line 14678
- **called from:**
- `static/js/document.js:14678`
- `static/js/document.js:14716`
- `static/js/document.js:14731`

## `moveActiveDocumentToCurrentChat` — function, line 14711
- **called from:**
- `static/js/document.js:14711`
- `static/js/document.js:14872`

## `moveActiveDocumentToNewChat` — function, line 14724
- **called from:**
- `static/js/document.js:14724`
- `static/js/document.js:14873`

## `showDocTabMenu` — function, line 14739
- **called from:**
- `static/js/document.js:1325`
- `static/js/document.js:14739`

## `_di` — arrow, line 14791
- **called from:**
- `static/js/cookbookServe.js:1298`
- `static/js/cookbookServe.js:1347`
- `static/js/document.js:14801`
- `static/js/document.js:14802`
- `static/js/document.js:14804`
- `static/js/document.js:14810`
- `static/js/document.js:14812`
- `static/js/document.js:14813`
- `static/js/document.js:14817`
- `static/js/document.js:14820`
- `static/js/document.js:14822`
- `static/js/documentLibrary.js:813`
- `static/js/documentLibrary.js:828`
- `static/js/documentLibrary.js:843`
- `static/js/documentLibrary.js:854`
- `static/js/documentLibrary.js:885`
- `static/js/documentLibrary.js:910`

## `_sendSignedReply` — function, line 14892
- **called from:**
- `static/js/document.js:8000`
- `static/js/document.js:14874`
- `static/js/document.js:14892`

## `saveDocument` — function, line 14991
- **called from:**
- `static/js/chat.js:3222`
- `static/js/chat.js:3293`
- `static/js/document.js:3710`
- `static/js/document.js:5221`
- `static/js/document.js:5316`
- `static/js/document.js:5700`
- `static/js/document.js:6599`
- `static/js/document.js:7242`
- `static/js/document.js:7315`
- `static/js/document.js:8001`
- `static/js/document.js:8270`
- `static/js/document.js:8470`
- `static/js/document.js:8553`
- `static/js/document.js:8803`
- `static/js/document.js:9261`
- `static/js/document.js:11410`
- `static/js/document.js:12069`
- `static/js/document.js:12155`
- `static/js/document.js:12238`
- `static/js/document.js:14185`
- `static/js/document.js:14306`
- `static/js/document.js:14358`
- `static/js/document.js:14393`
- `static/js/document.js:14682`
- `static/js/document.js:14858`
- `static/js/document.js:14991`
- `static/js/document.js:16287`

## `releaseSaveTurn` — arrow, line 15006
- **called from:**
- `static/js/document.js:15074`

## `ensureDocx` — function, line 15080
- **called from:**
- `static/js/document.js:15080`
- `static/js/document.js:15962`

## `_getExportBaseName` — function, line 15093
- **called from:**
- `static/js/document.js:15093`
- `static/js/document.js:15406`
- `static/js/document.js:15426`
- `static/js/document.js:15503`
- `static/js/document.js:15982`
- `static/js/document.js:16009`

## `exportDocument` — function, line 15101
- **called from:**
- `static/js/document.js:15101`

## `_importFromDevice` — function, line 15134
- **called from:**
- `static/js/document.js:7997`
- `static/js/document.js:15134`
- `static/js/document.js:15281`

## `showExportMenu` — function, line 15229
- **called from:**
- `static/js/document.js:8003`
- `static/js/document.js:11731`
- `static/js/document.js:14869`
- `static/js/document.js:15229`

## `_richTextExportCss` — function, line 15347
- **called from:**
- `static/js/document.js:15347`
- `static/js/document.js:15401`
- `static/js/document.js:15509`

## `exportAsHtml` — function, line 15385
- **called from:**
- `static/js/document.js:15385`

## `exportAsVisualReport` — function, line 15412
- **called from:**
- `static/js/document.js:15412`

## `previewVisualReport` — function, line 15437
- **called from:**
- `static/js/document.js:15437`

## `exportAsPdf` — function, line 15466
- **called from:**
- `static/js/document.js:15466`

## `_docxHexColor` — function, line 15542
- **called from:**
- `static/js/document.js:15542`
- `static/js/document.js:15582`
- `static/js/document.js:15584`
- `static/js/document.js:15591`

## `_docxInlineStyle` — function, line 15561
- **called from:**
- `static/js/document.js:15561`
- `static/js/document.js:15745`

## `_docxTextRuns` — function, line 15600
- **called from:**
- `static/js/document.js:15600`
- `static/js/document.js:15732`
- `static/js/document.js:15788`
- `static/js/document.js:15885`

## `_docxImageFallbackRun` — function, line 15621
- **called from:**
- `static/js/document.js:15621`
- `static/js/document.js:15742`

## `_docxImageWidth` — function, line 15630
- **called from:**
- `static/js/document.js:15630`
- `static/js/document.js:15709`

## `_docxImageAlignment` — function, line 15650
- **called from:**
- `static/js/document.js:15650`
- `static/js/document.js:15781`
- `static/js/document.js:15862`
- `static/js/document.js:15868`

## `_docxImagePngData` — function, line 15656
- **called from:**
- `static/js/document.js:15656`
- `static/js/document.js:15708`

## `cleanup` — arrow, line 15663
- **called from:**
- `tests/test_browser_producer_live_contract.py:41`
- `tests/test_ca_trust.py:43`
- `static/js/calendar.js:3194`
- `static/js/calendar.js:3202`
- `static/js/calendar.js:3239`
- `static/js/calendar.js:3369`
- `static/js/calendar.js:3378`
- `static/js/chat.js:7613`
- `static/js/chat.js:9104`
- `static/js/chat.js:9112`
- `static/js/chat.js:9118`
- `static/js/chat.js:9121`
- `static/js/chat.js:9124`
- `static/js/chat.js:9147`
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

## `_docxPrepareImages` — function, line 15703
- **called from:**
- `static/js/document.js:15703`
- `static/js/document.js:15914`

## `_docxInlineChildren` — function, line 15728
- **called from:**
- `static/js/document.js:15728`
- `static/js/document.js:15746`
- `static/js/document.js:15790`
- `static/js/document.js:15795`
- `static/js/document.js:15807`
- `static/js/document.js:15831`
- `static/js/document.js:15863`
- `static/js/document.js:15870`

## `_docxParagraphOptions` — function, line 15756
- **called from:**
- `static/js/document.js:15756`
- `static/js/document.js:15797`

## `_docxParagraphFromElement` — function, line 15785
- **called from:**
- `static/js/document.js:15785`
- `static/js/document.js:15905`

## `_docxListBlocks` — function, line 15800
- **called from:**
- `static/js/document.js:15800`
- `static/js/document.js:15818`
- `static/js/document.js:15891`

## `_docxTableBlock` — function, line 15823
- **called from:**
- `static/js/document.js:15823`
- `static/js/document.js:15895`

## `_docxFigureBlocks` — function, line 15858
- **called from:**
- `static/js/document.js:15858`
- `static/js/document.js:15893`

## `_docxBlocksFromNodes` — function, line 15880
- **called from:**
- `static/js/document.js:15832`
- `static/js/document.js:15880`
- `static/js/document.js:15903`
- `static/js/document.js:15915`

## `_richTextToDocxChildren` — function, line 15911
- **called from:**
- `static/js/document.js:15911`
- `static/js/document.js:15975`

## `_markdownToDocxChildren` — function, line 15918
- **called from:**
- `static/js/document.js:15918`
- `static/js/document.js:15976`

## `_richDocxNumbering` — function, line 15942
- **called from:**
- `static/js/document.js:15942`
- `static/js/document.js:15978`

## `exportAsDocx` — function, line 15957
- **called from:**
- `static/js/document.js:15957`

## `convertOriginalDocument` — function, line 15991
- **called from:**
- `static/js/document.js:15307`
- `static/js/document.js:15311`
- `static/js/document.js:15991`

## `convertOriginalToPdfForSigning` — function, line 16024
- **called from:**
- `static/js/document.js:16024`

## `deleteActiveDocument` — function, line 16067
- **called from:**
- `static/js/document.js:9280`
- `static/js/document.js:14876`
- `static/js/document.js:16067`

## `toggleFullscreen` — function, line 16098
- **called from:**
- `static/js/document.js:7908`
- `static/js/document.js:11408`
- `static/js/document.js:16098`

## `_installMarkdownPreviewEditButton` — function, line 16133
- **called from:**
- `static/js/document.js:16133`
- `static/js/document.js:16180`

## `_setMarkdownPreviewActive` — function, line 16150
- **called from:**
- `static/js/document.js:7199`
- `static/js/document.js:7207`
- `static/js/document.js:7211`
- `static/js/document.js:8243`
- `static/js/document.js:14310`
- `static/js/document.js:16144`
- `static/js/document.js:16150`
- `static/js/document.js:16216`
- `static/js/document.js:16221`
- `static/js/document.js:16963`
- `static/js/document.js:16976`
- `static/js/document.js:17174`
- `static/js/document.js:17230`

## `toggleMarkdownPreview` — function, line 16214
- **called from:**
- `static/js/document.js:8383`
- `static/js/document.js:8567`
- `static/js/document.js:8589`
- `static/js/document.js:14862`
- `static/js/document.js:16214`

## `toggleRichTextPreview` — function, line 16219
- **called from:**
- `static/js/document.js:8617`
- `static/js/document.js:16219`

## `_setDocxPreviewActive` — function, line 16225
- **called from:**
- `static/js/document.js:7213`
- `static/js/document.js:8246`
- `static/js/document.js:8248`
- `static/js/document.js:16225`
- `static/js/document.js:16263`

## `isCurrent` — arrow, line 16228
- **called from:**
- `static/js/chat.js:3726`
- `static/js/chat.js:3731`
- `static/js/chat.js:3733`
- `static/js/document.js:16246`
- `static/js/document.js:16255`
- `static/js/emailLibrary/index.js:2336`
- `static/js/galleryEditor.js:3905`
- `static/js/galleryEditor.js:3908`
- `static/js/galleryEditor.js:4048`
- `static/js/galleryEditor.js:4052`
- `static/js/galleryEditor.js:8330`
- `static/js/galleryEditor.js:8344`
- `static/js/galleryEditor.js:8368`
- `static/js/galleryEditor.js:8427`
- `static/js/galleryEditor.js:8438`

## `toggleDocxPreview` — function, line 16261
- **called from:**
- `static/js/document.js:8613`
- `static/js/document.js:14865`
- `static/js/document.js:16261`

## `_convertDocxToRichText` — function, line 16266
- **called from:**
- `static/js/document.js:16266`

## `parseCSV` — function, line 16295
- **called from:**
- `static/js/document.js:16295`
- `static/js/document.js:16355`

## `csvEscapeField` — function, line 16323
- **called from:**
- `static/js/document.js:16323`
- `static/js/document.js:16337`
- `static/js/document.js:16340`

## `syncTableToTextarea` — function, line 16331
- **called from:**
- `static/js/document.js:16331`
- `static/js/document.js:16393`
- `static/js/document.js:16429`

## `toggleCsvPreview` — function, line 16348
- **called from:**
- `static/js/document.js:7185`
- `static/js/document.js:8568`
- `static/js/document.js:8605`
- `static/js/document.js:14863`
- `static/js/document.js:16348`
- `static/js/document.js:17227`

## `esc` — arrow, line 16372
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

## `so` — class, line 16439
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_themedRenderSrcdoc` — function, line 16447
- **called from:**
- `static/js/document.js:14355`
- `static/js/document.js:16447`
- `static/js/document.js:16474`
- `static/js/document.js:17221`

## `toggleHtmlPreview` — function, line 16462
- **called from:**
- `static/js/document.js:1317`
- `static/js/document.js:8569`
- `static/js/document.js:8609`
- `static/js/document.js:14543`
- `static/js/document.js:14864`
- `static/js/document.js:16462`
- `static/js/document.js:17218`

## `exitHtmlPreview` — function, line 16485
- **called from:**
- `static/js/document.js:7189`
- `static/js/document.js:8258`
- `static/js/document.js:16480`
- `static/js/document.js:16485`
- `static/js/document.js:16761`

## `simpleDiff` — function, line 16503
- **called from:**
- `static/js/document.js:16503`

## `lineDiff` — function, line 16530
- **called from:**
- `static/js/document.js:16530`
- `static/js/document.js:16575`

## `animateDocChange` — function, line 16567
- **called from:**
- `static/js/document.js:16567`

## `_syncStreamDocChrome` — function, line 16683
- **called from:**
- `static/js/document.js:16683`
- `static/js/document.js:16728`
- `static/js/document.js:16800`

## `streamDocOpen` — function, line 16706
- **called from:**
- `static/js/chat.js:5846`
- `static/js/chat.js:7515`
- `static/js/document.js:16706`

## `_animateDocEdit` — function, line 16807
- **called from:**
- `static/js/document.js:16807`

## `tick` — function, line 16847
- **called from:**
- `src/background_tool_jobs.py:190`
- `tests/test_background_tool_jobs.py:35`
- `tests/test_background_tool_jobs.py:39`
- `tests/test_background_tool_jobs.py:40`
- `tests/test_background_tool_jobs.py:51`
- `tests/test_background_tool_jobs.py:85`
- `tests/test_background_tool_jobs.py:88`
- `tests/test_background_tool_jobs.py:113`
- `tests/test_background_tool_jobs.py:204`
- `tests/test_background_tool_jobs.py:219`
- `static/js/backgroundToolJobs.js:125`
- `static/js/backgroundToolJobs.js:127`
- `static/js/document.js:16847`
- `static/js/editor/build/transform-popup.js:152`
- `static/js/editor/build/transform-popup.js:156`
- `static/js/editor/build/transform-popup.js:159`
- `static/js/escMenuStack.js:101`
- `static/js/galleryEditor.js:891`
- `static/js/galleryEditor.js:14278`
- `static/js/slashCommands.js:2802`

## `streamDocDelta` — function, line 16885
- **called from:**
- `static/js/chat.js:5856`
- `static/js/chat.js:7518`
- `static/js/document.js:16885`

## `streamDocFinalize` — function, line 16921
- **called from:**
- `static/js/document.js:16921`
- `static/js/document.js:16982`

## `_isMarkdownPreviewVisible` — function, line 16942
- **called from:**
- `static/js/document.js:16942`
- `static/js/document.js:16948`
- `static/js/document.js:16969`
- `static/js/document.js:17151`

## `_handleMarkdownPreviewClickHint` — function, line 16947
- **called from:**
- `static/js/document.js:16947`

## `_refreshMarkdownPreviewIfVisible` — function, line 16968
- **called from:**
- `static/js/document.js:5729`
- `static/js/document.js:14352`
- `static/js/document.js:16968`
- `static/js/document.js:17162`
- `static/js/document.js:17180`

## `handleDocUpdate` — function, line 16981
- **called from:**
- `static/js/chat.js:5818`
- `static/js/chat.js:5864`
- `static/js/document.js:16981`

## `toggleVersionHistory` — function, line 17251
- **called from:**
- `static/js/document.js:1308`
- `static/js/document.js:17251`

## `_closeVersionPanel` — function, line 17302
- **called from:**
- `static/js/document.js:14627`
- `static/js/document.js:17292`
- `static/js/document.js:17298`
- `static/js/document.js:17302`

## `_buildDiffSummary` — function, line 17319
- **called from:**
- `static/js/document.js:17319`
- `static/js/document.js:17362`

## `_escHtml` — function, line 17344
- **called from:**
- `static/js/document.js:2114`
- `static/js/document.js:4985`
- `static/js/document.js:5426`
- `static/js/document.js:5427`
- `static/js/document.js:5441`
- `static/js/document.js:5442`
- `static/js/document.js:5582`
- `static/js/document.js:5980`
- `static/js/document.js:6077`
- `static/js/document.js:6077`
- `static/js/document.js:16251`
- `static/js/document.js:16256`
- `static/js/document.js:17335`
- `static/js/document.js:17338`
- `static/js/document.js:17344`
- `static/js/tasks.js:331`
- `static/js/tasks.js:331`
- `static/js/tasks.js:1634`
- `static/js/tasks.js:1634`
- `static/js/tasks.js:1645`
- `static/js/tasks.js:2204`
- `static/js/tasks.js:2307`
- `static/js/tasks.js:2355`
- `static/js/tasks.js:2559`
- `static/js/tasks.js:2571`
- `static/js/tasks.js:2573`
- `static/js/tasks.js:2574`
- `static/js/tasks.js:2574`
- `static/js/tasks.js:2821`
- `static/js/tasks.js:2845`
- `static/js/tasks.js:2880`
- `static/js/tasks.js:2916`
- `static/js/tasks.js:2916`
- `static/js/tasks.js:2925`
- `static/js/tasks.js:2929`
- `static/js/tasks.js:2931`
- `static/js/tasks.js:2932`
- `static/js/tasks.js:2932`
- `static/js/tasks.js:2938`
- `static/js/tasks.js:2942`
- `static/js/tasks.js:2957`

## `loadVersionHistory` — function, line 17349
- **called from:**
- `static/js/document.js:17287`
- `static/js/document.js:17349`
- `static/js/document.js:17434`

## `previewVersion` — function, line 17404
- **called from:**
- `static/js/document.js:17395`
- `static/js/document.js:17404`

## `restoreVersion` — function, line 17418
- **called from:**
- `static/js/document.js:17384`
- `static/js/document.js:17418`

## `updateTitle` — function, line 17443
- **called from:**
- `static/js/document.js:1389`
- `static/js/document.js:17443`
- `static/js/document.js:17505`

## `autoTitleFromContent` — function, line 17464
- **called from:**
- `static/js/document.js:4226`
- `static/js/document.js:5698`
- `static/js/document.js:7312`
- `static/js/document.js:8801`
- `static/js/document.js:17117`
- `static/js/document.js:17464`

## `updateLanguage` — function, line 17511
- **called from:**
- `static/js/document.js:8230`
- `static/js/document.js:12883`
- `static/js/document.js:12896`
- `static/js/document.js:12918`
- `static/js/document.js:17511`

## `clearAll` — function, line 17531
- **called from:**
- `static/js/document.js:17531`
- `static/js/research/jobs.js:279`

## `isPanelOpen` — function, line 17539
- **called from:**
- `static/app.js:799`
- `static/app.js:993`
- `static/app.js:2043`
- `static/app.js:2064`
- `static/app.js:3409`
- `static/app.js:3939`
- `static/js/document.js:9276`
- `static/js/document.js:17539`
- `static/js/emailInbox.js:1057`
- `static/js/emailInbox.js:1127`
- `static/js/features/notes/ui/panel.js:385`
- `static/js/features/notes/ui/panel.js:388`
- `static/js/sessions.js:2700`
- `static/js/slashCommands.js:1240`

## `getCurrentDocId` — function, line 17543
- **called from:**
- `static/app.js:3411`
- `static/js/document.js:17543`

## `getChatDocumentId` — function, line 17547
- **called from:**
- `static/js/chat.js:3209`
- `static/js/document.js:14992`
- `static/js/document.js:17547`
- `static/js/document.js:17573`

## `getActiveEmailComposerContext` — function, line 17572
- **called from:**
- `static/js/chat.js:3206`
- `static/js/chatStream.js:245`
- `static/js/document.js:17572`

## `findEmailDocId` — function, line 17589
- **called from:**
- `static/js/chatStream.js:253`
- `static/js/document.js:17589`
- `static/js/emailInbox.js:1054`
