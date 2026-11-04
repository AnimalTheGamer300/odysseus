# `static/js/chat.js` — definitions & call sites

182 definitions (regex-based, best-effort).
**Exports:** `abortCurrentRequest`, `checkBackgroundStream`, `checkPendingResearch`, `compactCurrentChatContext`, `continueFrom`, `default`, `deleteMessage`, `detachCurrentStream`, `editAIMessage`, `editUserMessage`, `forkFrom`, `handleChatSubmit`, `init`, `initListeners`, `queueStreamingComposerRequest`, `refreshChatContextHeader`, `regenerateFrom`, `resendUserMessage`, `resumeStream`, `rewriteWith`, `setDisplayOverride`, `setHideUserBubble`, `setPendingContinue`

## `_submitToolApprovalWhenIdle` — function, line 67
- **called from:**
- `static/js/chat.js:67`
- `static/js/chat.js:73`
- `static/js/chat.js:93`

## `_fmtContextNumber` — function, line 96
- **called from:**
- `static/js/chat.js:96`
- `static/js/chat.js:199`
- `static/js/chat.js:199`
- `static/js/chat.js:313`
- `static/js/chat.js:313`

## `_contextColorClass` — function, line 101
- **called from:**
- `static/js/chat.js:101`
- `static/js/chat.js:180`
- `static/js/chat.js:315`

## `_contextRingColor` — function, line 108
- **called from:**
- `static/js/chat.js:108`
- `static/js/chat.js:133`
- `static/js/chat.js:142`

## `_contextRingMarkup` — function, line 115
- **called from:**
- `static/js/chat.js:115`
- `static/js/chat.js:134`
- `static/js/chat.js:145`

## `_renderContextHeaderRing` — function, line 131
- **called from:**
- `static/js/chat.js:131`
- `static/js/chat.js:311`

## `_renderCompactMenuContextIcon` — function, line 137
- **called from:**
- `static/js/chat.js:137`
- `static/js/chat.js:312`

## `_liveSessionModule` — function, line 148
- **called from:**
- `static/js/chat.js:148`
- `static/js/chat.js:266`
- `static/js/chat.js:291`
- `static/js/chat.js:307`

## `_closeContextHeaderPopup` — function, line 154
- **called from:**
- `static/js/chat.js:154`
- `static/js/chat.js:175`
- `static/js/chat.js:247`
- `static/js/chat.js:276`
- `static/js/chat.js:297`
- `static/js/chat.js:319`
- `static/js/chat.js:327`

## `_positionContextHeaderPopup` — function, line 160
- **called from:**
- `static/js/chat.js:160`
- `static/js/chat.js:242`

## `_showContextHeaderPopup` — function, line 171
- **called from:**
- `static/js/chat.js:171`
- `static/js/chat.js:261`
- `static/js/chat.js:320`

## `close` — arrow, line 244
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

## `_bindContextHeaderPill` — function, line 253
- **called from:**
- `static/js/chat.js:253`
- `static/js/chat.js:288`

## `compactCurrentChatContext` — function, line 265
- **called from:**
- `static/app.js:506`
- `static/js/chat.js:232`
- `static/js/chat.js:265`

## `refreshChatContextHeader` — function, line 287
- **called from:**
- `static/js/chat.js:278`
- `static/js/chat.js:287`
- `static/js/chat.js:3918`
- `static/js/modelPicker.js:726`
- `static/js/sessions.js:2047`
- `static/js/sessions.js:2359`
- `static/js/sessions.js:2449`

## `_setForegroundChatBusy` — function, line 333
- **called from:**
- `static/js/chat.js:333`
- `static/js/chat.js:1011`
- `static/js/chat.js:1245`
- `static/js/chat.js:1253`
- `static/js/chat.js:1642`

## `_createChatSendPerf` — function, line 344
- **called from:**
- `static/js/chat.js:344`
- `static/js/chat.js:1639`

## `now` — arrow, line 349
- **called from:**
- `app.py:957`
- `app.py:1252`
- `core/database.py:25`
- `core/database.py:216`
- `core/database.py:216`
- `core/session_manager.py:408`
- `core/session_manager.py:548`
- `core/session_manager.py:629`
- `core/session_manager.py:700`
- `core/session_manager.py:893`
- `core/session_manager.py:921`
- `core/session_manager.py:922`
- `core/session_manager.py:1005`
- `core/session_manager.py:1025`
- `core/session_manager.py:1042`
- `routes/backup_routes.py:46`
- `routes/backup_routes.py:56`
- `routes/calendar_routes.py:401`
- `routes/calendar_routes.py:525`
- `routes/document/document_routes.py:657`
- `routes/document/document_routes.py:875`
- `routes/email_routes.py:4314`
- `routes/history/history_routes.py:532`
- `routes/history/history_routes.py:802`
- `routes/history/history_routes.py:1019`
- `routes/history/history_routes.py:1143`
- `routes/history/history_routes.py:1164`
- `routes/history/history_routes.py:1188`
- `routes/note/note_routes.py:192`
- `routes/note/note_routes.py:554`
- `routes/session_routes.py:967`
- `routes/session_routes.py:975`
- `routes/session_routes.py:1026`
- `routes/task/task_routes.py:104`
- `routes/task/task_routes.py:1107`
- `scripts/agent_migration_manifest.py:47`
- `scripts/demo_email/seed_demo_emails.py:100`
- `scripts/demo_email/seed_demo_emails.py:116`
- `scripts/demo_email/seed_demo_emails.py:212`
- `scripts/demo_email/seed_demo_emails.py:212`
- `scripts/demo_email/seed_demo_emails.py:272`
- `scripts/pr_blocker_audit.py:524`
- `services/memory/skill_format.py:483`
- `services/search/cache.py:42`
- `services/search/content.py:202`
- `services/search/content.py:395`
- `services/search/content.py:398`
- `services/search/core.py:155`
- `services/search/core.py:198`
- `services/search/core.py:200`
- `services/search/core.py:206`
- `services/search/ranking.py:17`
- `src/agent_loop.py:5130`
- `src/agent_loop.py:6408`
- `src/agent_tools/document_tools.py:793`
- `src/agent_tools/session_tools.py:127`
- `src/agent_tools/spawn_agent_tools.py:171`
- `src/builtin_actions.py:1792`
- `src/builtin_actions.py:2170`
- `src/cleanup_service.py:15`
- … +301 more (grep the name in repo)

## `mark` — method?, line 351
- **called from:**
- `static/js/chat.js:351`
- `static/js/chat.js:1749`
- `static/js/chat.js:1751`
- `static/js/chat.js:1779`
- `static/js/chat.js:1782`
- `static/js/chat.js:1794`
- `static/js/chat.js:1796`
- `static/js/chat.js:1798`
- `static/js/chat.js:2010`
- `static/js/chat.js:2047`
- `static/js/chat.js:2049`
- `static/js/chat.js:2052`
- `static/js/chat.js:2160`
- `static/js/chat.js:2164`
- `static/js/chat.js:2182`
- `static/js/chat.js:2253`
- `static/js/chat.js:2255`
- `static/js/chat.js:2257`
- `static/js/chat.js:2501`
- `static/js/chat.js:2508`
- `static/js/chat.js:2557`

## `report` — method?, line 356
- **called from:**
- `static/js/chat.js:356`
- `static/js/chat.js:2509`
- `static/js/chat.js:2558`

## `_hashSessionCandidate` — function, line 388
- **called from:**
- `static/js/chat.js:388`
- `static/js/chat.js:417`

## `_adoptOpenedSessionBeforeAutoCreate` — function, line 399
- **called from:**
- `static/app.js:845`
- `static/app.js:3332`
- `static/js/chat.js:399`
- `static/js/chat.js:1713`

## `_setRoleModelLabel` — function, line 448
- **called from:**
- `static/js/chat.js:448`
- `static/js/chat.js:3686`
- `static/js/chat.js:3714`
- `static/js/chat.js:3767`
- `static/js/chat.js:4494`
- `static/js/chat.js:5793`
- `static/js/chat.js:5815`

## `_bestKnownStreamModel` — function, line 481
- **called from:**
- `static/js/chat.js:481`
- `static/js/chat.js:2428`

## `_clearResearchTimer` — function, line 508
- **called from:**
- `static/js/chat.js:508`
- `static/js/chat.js:1509`
- `static/js/chat.js:3602`
- `static/js/chat.js:3624`
- `static/js/chat.js:5165`
- `static/js/chat.js:7107`
- `static/js/chat.js:7121`
- `static/js/chat.js:7137`

## `_appendViewReportLink` — function, line 524
- **called from:**
- `static/js/chat.js:524`
- `static/js/chat.js:4702`
- `static/js/chat.js:7004`
- `static/js/chat.js:7156`

## `_stripDocumentFenceForChat` — function, line 529
- **called from:**
- `static/js/chat.js:529`
- `static/js/chat.js:559`

## `_stripIncompleteRawToolJsonForChat` — function, line 542
- **called from:**
- `static/js/chat.js:542`
- `static/js/chat.js:559`

## `_streamDisplayText` — function, line 558
- **called from:**
- `static/js/chat.js:558`
- `static/js/chat.js:740`
- `static/js/chat.js:2767`
- `static/js/chat.js:2775`
- `static/js/chat.js:2976`
- `static/js/chat.js:3027`
- `static/js/chat.js:3087`
- `static/js/chat.js:4547`
- `static/js/chat.js:4644`
- `static/js/chat.js:4648`
- `static/js/chat.js:5697`

## `_showDocumentWritingStatus` — function, line 562
- **called from:**
- `static/js/chat.js:562`
- `static/js/chat.js:3115`
- `static/js/chat.js:5699`

## `_finishDocumentWritingStatus` — function, line 613
- **called from:**
- `static/js/chat.js:613`
- `static/js/chat.js:4542`
- `static/js/chat.js:5853`

## `_tabSyncPost` — function, line 674
- **called from:**
- `static/js/chat.js:674`
- `static/js/chat.js:685`
- `static/js/chat.js:2009`
- `static/js/chat.js:3210`
- `static/js/chat.js:3952`
- `static/js/chat.js:4789`
- `static/js/chat.js:4889`
- `static/js/chat.js:4909`
- `static/js/chat.js:4929`
- `static/js/chat.js:4948`
- `static/js/chat.js:5002`
- `static/js/chat.js:5035`
- `static/js/chat.js:5373`
- `static/js/chat.js:5880`
- `static/js/chat.js:5893`
- `static/js/chat.js:7286`
- `static/js/chat.js:7362`

## `_tabSyncPostDelta` — function, line 681
- **called from:**
- `static/js/chat.js:681`
- `static/js/chat.js:3328`
- `static/js/chat.js:5765`

## `_tabSyncCurrentSession` — function, line 689
- **called from:**
- `static/js/chat.js:689`
- `static/js/chat.js:795`
- `static/js/chat.js:815`
- `static/js/chat.js:828`
- `static/js/chat.js:859`
- `static/js/chat.js:867`
- `static/js/chat.js:932`
- `static/js/chat.js:951`
- `static/js/chat.js:956`
- `static/js/chat.js:961`
- `static/js/chat.js:966`
- `static/js/chat.js:971`
- `static/js/chat.js:976`

## `_tabSyncEnsureBubble` — function, line 695
- **called from:**
- `static/js/chat.js:695`
- `static/js/chat.js:751`
- `static/js/chat.js:947`

## `_tabSyncRenderDelta` — function, line 728
- **called from:**
- `static/js/chat.js:728`
- `static/js/chat.js:760`

## `_tabSyncQueueDelta` — function, line 750
- **called from:**
- `static/js/chat.js:750`
- `static/js/chat.js:952`

## `_tabSyncClearMirror` — function, line 764
- **called from:**
- `static/js/chat.js:764`
- `static/js/chat.js:783`
- `static/js/chat.js:834`
- `static/js/chat.js:939`

## `_tabSyncReloadSession` — function, line 782
- **called from:**
- `static/js/chat.js:782`
- `static/js/chat.js:797`
- `static/js/chat.js:839`
- `static/js/chat.js:872`

## `_tabSyncScheduleReload` — function, line 791
- **called from:**
- `static/js/chat.js:791`
- `static/js/chat.js:957`
- `static/js/chat.js:977`

## `_tabSyncScheduleTakeover` — function, line 804
- **called from:**
- `static/js/chat.js:804`
- `static/js/chat.js:962`

## `_tabSyncTakeover` — function, line 814
- **called from:**
- `static/js/chat.js:809`
- `static/js/chat.js:814`
- `static/js/chat.js:870`

## `_tabSyncStaleSweep` — function, line 849
- **called from:**
- `static/js/chat.js:849`

## `_tabSyncStampUserBubble` — function, line 883
- **called from:**
- `static/js/chat.js:883`
- `static/js/chat.js:972`

## `_tabSyncApplyDelete` — function, line 892
- **called from:**
- `static/js/chat.js:892`
- `static/js/chat.js:967`

## `_initTabSync` — function, line 920
- **called from:**
- `static/js/chat.js:920`
- `static/js/chat.js:1167`

## `hasActiveStream` — function, line 992
- **called from:**
- `static/js/chat.js:796`
- `static/js/chat.js:816`
- `static/js/chat.js:829`
- `static/js/chat.js:854`
- `static/js/chat.js:868`
- `static/js/chat.js:932`
- `static/js/chat.js:951`
- `static/js/chat.js:956`
- `static/js/chat.js:961`
- `static/js/chat.js:976`
- `static/js/chat.js:992`
- `static/js/chat.js:5407`
- `static/js/chat.js:5593`
- `static/js/sessions.js:2803`

## `_getForegroundStreamState` — function, line 997
- **called from:**
- `static/js/chat.js:997`
- `static/js/chat.js:1007`
- `static/js/chat.js:1168`
- `static/js/chat.js:1557`
- `static/js/chat.js:5246`
- `static/js/chat.js:5337`
- `static/js/chat.js:5349`
- `static/js/chat.js:5506`
- `static/js/chat.js:6313`
- `static/js/chat.js:6326`

## `_syncForegroundStreamGlobals` — function, line 1006
- **called from:**
- `static/js/chat.js:1006`
- `static/js/chat.js:1650`
- `static/js/chat.js:2425`
- `static/js/chat.js:5119`
- `static/js/chat.js:5359`
- `static/js/chat.js:5370`
- `static/js/chat.js:5541`
- `static/js/chat.js:6342`

## `_touchStreamActivity` — function, line 1015
- **called from:**
- `static/js/chat.js:1015`
- `static/js/chat.js:1879`
- `static/js/chat.js:3140`

## `_metricsCostRecordId` — function, line 1024
- **called from:**
- `static/js/chat.js:1024`
- `static/js/chat.js:3868`
- `static/js/chat.js:3902`
- `static/js/chat.js:5781`
- `static/js/chat.js:5835`

## `_postExactStop` — function, line 1030
- **called from:**
- `static/js/chat.js:1030`
- `static/js/chat.js:1053`
- `static/js/chat.js:1070`

## `_stopExactRun` — function, line 1039
- **called from:**
- `static/js/chat.js:1039`
- `static/js/chat.js:2381`
- `static/js/chat.js:2382`
- `static/js/chat.js:5258`

## `_rememberStreamRunId` — function, line 1057
- **called from:**
- `static/js/chat.js:1057`
- `static/js/chat.js:2549`

## `_appendGeneratedImageBubble` — function, line 1088
- **called from:**
- `static/js/chat.js:1088`
- `static/js/chat.js:3269`
- `static/js/chat.js:4155`
- `static/js/chat.js:4698`

## `_normalizeEndpointForCompare` — function, line 1119
- **called from:**
- `static/js/chat.js:1119`
- `static/js/chat.js:1143`
- `static/js/chat.js:1149`

## `_probeCurrentEndpointStatus` — function, line 1142
- **called from:**
- `static/js/chat.js:1142`

## `init` — function, line 1165
- **called from:**
- `static/app.js:3723`
- `static/app.js:3724`
- `static/app.js:3725`
- `static/app.js:3726`
- `static/app.js:3727`
- `static/app.js:3728`
- `static/app.js:3730`
- `static/app.js:3733`
- `static/app.js:3735`
- `static/app.js:3738`
- `static/app.js:3747`
- `static/app.js:4369`
- `static/app.js:4370`
- `static/js/a11y.js:121`
- `static/js/a11y.js:163`
- `static/js/censor.js:44`
- `static/js/chat.js:1165`
- `static/js/chat.js:1170`
- `static/js/compare/index.js:55`
- `static/js/cookbookDownload.js:10`
- `static/js/cookbookRunning.js:333`
- `static/js/cookbookServe.js:16`
- `static/js/document.js:154`
- `static/js/emailInbox.js:157`
- `static/js/fileHandler.js:173`
- `static/js/group.js:24`
- `static/js/models.js:27`
- `static/js/presets.js:79`
- `static/js/rag.js:12`
- `static/js/research/jobs.js:35`
- `static/js/research/panel.js:210`
- `static/js/research/panel.js:214`
- `static/js/search-chat.js:198`
- `static/js/search.js:14`
- `static/js/tourAutoplay.js:117`
- `static/js/tourAutoplay.js:129`
- `static/js/tourHints.js:163`
- `static/js/tourHints.js:175`
- `static/js/voiceRecorder.js:268`

## `_wireHistoryRecall` — arrow, line 1184
- **called from:**
- `static/js/chat.js:1195`
- `static/js/chat.js:1197`
- `static/js/chat.js:1198`

## `_wireArrowUpRecall` — arrow, line 1189
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `updateSubmitButton` — function, line 1213
- **called from:**
- `static/js/chat.js:1213`
- `static/js/chat.js:1548`
- `static/js/chat.js:1624`
- `static/js/chat.js:1840`
- `static/js/chat.js:2060`
- `static/js/chat.js:2176`
- `static/js/chat.js:2194`
- `static/js/chat.js:5143`
- `static/js/chat.js:5380`
- `static/js/chat.js:5544`
- `static/js/chat.js:5649`
- `static/js/chat.js:5683`
- `static/js/chat.js:6352`

## `_extractPlanText` — function, line 1283
- **called from:**
- `static/js/chat.js:1283`
- `static/js/chat.js:1303`
- `static/js/chat.js:1323`

## `_getStoredPlan` — function, line 1298
- **called from:**
- `static/js/chat.js:1298`
- `static/js/chat.js:1323`

## `_setStoredPlan` — function, line 1302
- **called from:**
- `static/js/chat.js:1302`
- `static/js/chat.js:4281`
- `static/js/chat.js:4709`

## `_clearStoredPlan` — function, line 1308
- **called from:**
- `static/js/chat.js:1308`
- `static/js/chat.js:1331`

## `_attachPlanActions` — function, line 1312
- **called from:**
- `static/js/chat.js:1312`
- `static/js/chat.js:4710`

## `_escapeQueueText` — function, line 1337
- **called from:**
- `static/js/chat.js:1337`
- `static/js/chat.js:1363`

## `_ensureQueuedBubbleHost` — function, line 1341
- **called from:**
- `static/js/chat.js:1341`
- `static/js/chat.js:1357`

## `_createQueuedBubble` — function, line 1356
- **called from:**
- `static/js/chat.js:1356`
- `static/js/chat.js:1432`

## `_removeQueuedRequest` — function, line 1373
- **called from:**
- `static/js/chat.js:1373`
- `static/js/chat.js:1411`
- `static/js/chat.js:1464`

## `_setComposerAndSend` — function, line 1381
- **called from:**
- `static/js/chat.js:1328`
- `static/js/chat.js:1381`
- `static/js/chat.js:1404`
- `static/js/chat.js:1414`
- `static/js/chat.js:1465`

## `handleChatSubmit` — method?, line 1388
- **called from:**
- `static/js/chat.js:1388`
- `static/js/chat.js:1473`

## `_sendQueuedWhenIdle` — function, line 1396
- **called from:**
- `static/js/chat.js:1396`
- `static/js/chat.js:1425`

## `trySend` — arrow, line 1398
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_promoteQueuedRequest` — function, line 1410
- **called from:**
- `static/js/chat.js:1366`
- `static/js/chat.js:1410`

## `_queueAgentRequest` — function, line 1428
- **called from:**
- `static/js/chat.js:1428`
- `static/js/chat.js:1447`

## `queueStreamingComposerRequest` — function, line 1438
- **called from:**
- `static/app.js:113`
- `static/app.js:3480`
- `static/app.js:4107`
- `static/js/chat.js:1438`
- `static/js/chat.js:1498`

## `_drainQueuedAgentRequests` — function, line 1456
- **called from:**
- `static/js/chat.js:1456`
- `static/js/chat.js:1552`
- `static/js/chat.js:5223`
- `static/js/chat.js:5383`

## `handleChatSubmit` — function, line 1473
- **called from:**
- `static/js/chat.js:1388`
- `static/js/chat.js:1473`

## `_releaseSendFlag` — arrow, line 1648
- **called from:**
- `static/js/chat.js:1683`
- `static/js/chat.js:1695`
- `static/js/chat.js:1704`
- `static/js/chat.js:1752`
- `static/js/chat.js:1762`
- `static/js/chat.js:1799`
- `static/js/chat.js:1808`
- `static/js/chat.js:1819`
- `static/js/chat.js:1827`
- `static/js/chat.js:2061`
- `static/js/chat.js:2177`
- `static/js/chat.js:2195`

## `selectedRouteForSend` — arrow, line 1716
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_renderStream` — arrow, line 1902
- **called from:**
- `static/js/chat.js:2921`
- `static/js/chat.js:2957`
- `static/js/chat.js:3361`
- `static/js/chat.js:3363`
- `static/js/chat.js:3508`
- `static/js/chat.js:3510`

## `_finalizeRoundRender` — arrow, line 1903
- **called from:**
- `static/js/chat.js:2996`
- `static/js/chat.js:3966`
- `static/js/chat.js:4293`

## `_finalizeInterruptedView` — arrow, line 1904
- **called from:**
- `static/js/chat.js:2423`
- `static/js/chat.js:4829`

## `_cancelThinkingTimer` — arrow, line 1905
- **called from:**
- `static/js/chat.js:3274`
- `static/js/chat.js:3280`
- `static/js/chat.js:3288`
- `static/js/chat.js:3958`
- `static/js/chat.js:4272`
- `static/js/chat.js:4286`
- `static/js/chat.js:4362`
- `static/js/chat.js:4372`
- `static/js/chat.js:4388`
- `static/js/chat.js:4470`
- `static/js/chat.js:4838`

## `_removeThinkingSpinner` — arrow, line 1906
- **called from:**
- `static/js/chat.js:2698`
- `static/js/chat.js:3281`
- `static/js/chat.js:3289`
- `static/js/chat.js:3959`
- `static/js/chat.js:4273`
- `static/js/chat.js:4287`
- `static/js/chat.js:4363`
- `static/js/chat.js:4373`
- `static/js/chat.js:4389`
- `static/js/chat.js:4471`
- `static/js/chat.js:4839`

## `_flushLiveThinking` — arrow, line 1907
- **called from:**
- `static/js/chat.js:2848`
- `static/js/chat.js:3168`

## `_cancelLiveThinkingWork` — arrow, line 1908
- **called from:**
- `static/js/chat.js:2422`
- `static/js/chat.js:2849`
- `static/js/chat.js:2876`
- `static/js/chat.js:3169`
- `static/js/chat.js:3471`
- `static/js/chat.js:4291`
- `static/js/chat.js:4468`
- `static/js/chat.js:4815`
- `static/js/chat.js:5092`

## `_closeOpenThinkingMarkup` — arrow, line 1914
- **called from:**
- `static/js/chat.js:2994`
- `static/js/chat.js:3186`
- `static/js/chat.js:3956`
- `static/js/chat.js:4284`
- `static/js/chat.js:4813`

## `_endThinkingOnTerminalPath` — arrow, line 1915
- **called from:**
- `static/js/chat.js:2995`
- `static/js/chat.js:4833`

## `clearResponseTimeout` — arrow, line 1918
- **called from:**
- `static/js/chat.js:2512`
- `static/js/chat.js:3263`
- `static/js/chat.js:5093`

## `clearFirstTokenWaitTimers` — arrow, line 1920
- **called from:**
- `static/js/chat.js:1925`
- `static/js/chat.js:3135`
- `static/js/chat.js:3265`
- `static/js/chat.js:5095`

## `scheduleFirstTokenWaitMessages` — arrow, line 1924
- **called from:**
- `static/js/chat.js:2470`

## `clearProcessingProbe` — arrow, line 1937
- **called from:**
- `static/js/chat.js:3264`
- `static/js/chat.js:5094`

## `_dropReadonly` — arrow, line 2024
- **called from:**
- `static/js/chat.js:2038`
- `static/js/compare/index.js:622`

## `_idleTimeoutHandler` — arrow, line 2368
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_armIdleTimeout` — arrow, line 2396
- **called from:**
- `static/js/chat.js:2401`
- `static/js/chat.js:3142`

## `enableResearchBtn` — arrow, line 2481
- **called from:**
- `static/js/chat.js:2545`

## `_tzName` — arrow, line 2497
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_rememberGeneratedImage` — function, line 2582
- **called from:**
- `static/js/chat.js:2582`
- `static/js/chat.js:3268`
- `static/js/chat.js:4154`

## `_metricsTargetForTurn` — function, line 2590
- **called from:**
- `static/js/chat.js:2590`
- `static/js/chat.js:3896`
- `static/js/chat.js:3916`
- `static/js/chat.js:4746`

## `_ensureStreamLayout` — function, line 2600
- **called from:**
- `static/js/chat.js:2600`
- `static/js/chat.js:2984`
- `static/js/chat.js:3019`
- `static/js/chat.js:3448`

## `_ensureVisibleRoundForDelta` — function, line 2612
- **called from:**
- `static/js/chat.js:2612`
- `static/js/chat.js:3331`

## `_thinkingLabel` — function, line 2669
- **called from:**
- `static/js/chat.js:2669`
- `static/js/chat.js:2708`

## `_showThinkingSpinner` — function, line 2682
- **called from:**
- `static/js/chat.js:2682`
- `static/js/chat.js:2699`
- `static/js/chat.js:2708`

## `_replaceThinkingSpinner` — function, line 2697
- **called from:**
- `static/js/chat.js:2697`
- `static/js/chat.js:3275`

## `_scheduleThinkingSpinner` — function, line 2704
- **called from:**
- `static/js/chat.js:2704`
- `static/js/chat.js:2922`
- `static/js/chat.js:3365`
- `static/js/chat.js:3512`
- `static/js/chat.js:4222`

## `_estimateThinkingTokens` — function, line 2741
- **called from:**
- `static/js/chat.js:2741`
- `static/js/chat.js:2785`

## `_formatThinkStats` — function, line 2747
- **called from:**
- `static/js/chat.js:2747`
- `static/js/chat.js:2821`
- `static/js/chat.js:2889`
- `static/js/chat.js:2934`
- `static/js/chat.js:3229`

## `_stripThinkingWrappers` — function, line 2753
- **called from:**
- `static/js/chat.js:2753`
- `static/js/chat.js:2768`
- `static/js/chat.js:2779`

## `_liveThinkingText` — function, line 2766
- **called from:**
- `static/js/chat.js:2766`
- `static/js/chat.js:2780`
- `static/js/chat.js:2799`

## `_closedThinkingText` — function, line 2774
- **called from:**
- `static/js/chat.js:2774`
- `static/js/chat.js:2874`
- `static/js/chat.js:2886`
- `static/js/chat.js:2904`
- `static/js/chat.js:3220`

## `_commitLiveThinkingText` — function, line 2783
- **called from:**
- `static/js/chat.js:2783`

## `_ensureLiveThinkingThrottle` — function, line 2796
- **called from:**
- `static/js/chat.js:2796`
- `static/js/chat.js:2826`

## `_stopLiveThinkTimer` — function, line 2805
- **called from:**
- `static/js/chat.js:2805`
- `static/js/chat.js:2816`
- `static/js/chat.js:2843`

## `_startLiveThinkTimer` — function, line 2810
- **called from:**
- `static/js/chat.js:2810`
- `static/js/chat.js:2827`

## `_queueLiveThinking` — function, line 2825
- **called from:**
- `static/js/chat.js:2825`
- `static/js/chat.js:2831`
- `static/js/chat.js:3355`
- `static/js/chat.js:3472`
- `static/js/chat.js:3498`

## `_finalizeLiveThinking` — function, line 2847
- **called from:**
- `static/js/chat.js:2847`
- `static/js/chat.js:2874`
- `static/js/chat.js:2886`
- `static/js/chat.js:2906`
- `static/js/chat.js:3220`

## `_endLiveThinkingSection` — function, line 2882
- **called from:**
- `static/js/chat.js:2882`
- `static/js/chat.js:3962`
- `static/js/chat.js:4289`

## `_cancelThinkingGrace` — function, line 2893
- **called from:**
- `static/js/chat.js:2649`
- `static/js/chat.js:2844`
- `static/js/chat.js:2893`
- `static/js/chat.js:2903`
- `static/js/chat.js:3432`

## `_finishLiveThinkingTransition` — function, line 2899
- **called from:**
- `static/js/chat.js:2899`
- `static/js/chat.js:2966`
- `static/js/chat.js:3501`

## `_scheduleThinkingGrace` — function, line 2960
- **called from:**
- `static/js/chat.js:2960`
- `static/js/chat.js:3429`
- `static/js/chat.js:3496`

## `_replyAfterClosedThinking` — function, line 3006
- **called from:**
- `static/js/chat.js:3006`
- `static/js/chat.js:3028`

## `markFirstVisibleOutput` — arrow, line 3132
- **called from:**
- `static/js/chat.js:3157`

## `resetFn` — arrow, line 4722
- **called from:**
- `static/js/tts-ai.js:235`
- `static/js/tts-ai.js:341`

## `failures` — class, line 5021
- **called from:**
- `static/js/chat.js:5272`

## `abortCurrentRequest` — function, line 5235
- **called from:**
- `static/app.js:839`
- `static/js/chat.js:1511`
- `static/js/chat.js:5235`
- `static/js/chat.js:5330`
- `static/js/chat.js:5509`
- `static/js/keyboard-shortcuts.js:247`
- `static/js/sessions.js:977`
- `static/js/sessions.js:1990`
- `static/js/sessions.js:1996`
- `static/js/sessions.js:2537`

## `failures` — class, line 5272
- **called from:**
- `static/js/chat.js:5272`

## `_tryAutoRecover` — function, line 5276
- **called from:**
- `static/js/chat.js:5024`
- `static/js/chat.js:5276`

## `_removeStallBanner` — function, line 5298
- **called from:**
- `static/js/chat.js:5298`
- `static/js/chat.js:5319`
- `static/js/chat.js:5330`
- `static/js/chat.js:5440`
- `static/js/chat.js:5445`

## `_showStallBanner` — function, line 5303
- **called from:**
- `static/js/chat.js:5303`

## `_probeStaleLocalStream` — function, line 5336
- **called from:**
- `static/js/chat.js:5336`

## `_convergeAfterAbort` — function, line 5402
- **called from:**
- `static/js/chat.js:4890`
- `static/js/chat.js:4910`
- `static/js/chat.js:4930`
- `static/js/chat.js:4949`
- `static/js/chat.js:5036`
- `static/js/chat.js:5402`

## `_startStallWatchdog` — function, line 5436
- **called from:**
- `static/js/chat.js:1247`
- `static/js/chat.js:5436`

## `_stopStallWatchdog` — function, line 5443
- **called from:**
- `static/js/chat.js:1255`
- `static/js/chat.js:5443`

## `_renderCancelledBubble` — function, line 5451
- **called from:**
- `static/js/chat.js:1546`
- `static/js/chat.js:4958`
- `static/js/chat.js:5451`

## `detachCurrentStream` — function, line 5505
- **called from:**
- `static/app.js:838`
- `static/js/chat.js:5505`
- `static/js/sessions.js:1988`
- `static/js/sessions.js:2316`

## `resumeStream` — function, line 5591
- **called from:**
- `static/js/chat.js:643`
- `static/js/chat.js:836`
- `static/js/chat.js:5289`
- `static/js/chat.js:5360`
- `static/js/chat.js:5397`
- `static/js/chat.js:5424`
- `static/js/chat.js:5591`
- `static/js/sessions.js:2822`
- `static/js/sessions.js:2855`

## `cleanup` — arrow, line 5673
- **called from:**
- `static/js/calendar.js:2592`
- `static/js/calendar.js:2629`
- `static/js/calendar.js:2750`
- `static/js/calendar.js:2759`
- `static/js/chat.js:5852`
- `static/js/chat.js:7329`
- `static/js/chat.js:7337`
- `static/js/chat.js:7343`
- `static/js/chat.js:7346`
- `static/js/chat.js:7349`
- `static/js/chat.js:7372`
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

## `renderDelta` — arrow, line 5696
- **called from:**
- `static/js/chat.js:5717`
- `static/js/chat.js:5771`

## `queueRender` — arrow, line 5711
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_finishToolNode` — arrow, line 5724
- **called from:**
- `static/js/chat.js:5678`

## `checkBackgroundStream` — function, line 5901
- **called from:**
- `static/js/chat.js:5901`
- `static/js/sessions.js:2209`

## `_markCompactPre` — function, line 5986
- **called from:**
- `static/js/chat.js:5986`
- `static/js/chat.js:6012`

## `_scanCompactPres` — function, line 5996
- **called from:**
- `static/js/chat.js:5996`
- `static/js/chat.js:6007`
- `static/js/chat.js:6013`

## `_initCompactPreObserver` — function, line 6004
- **called from:**
- `static/js/chat.js:6004`

## `_reasoningKey` — function, line 6027
- **called from:**
- `static/js/chat.js:6027`
- `static/js/chat.js:6030`
- `static/js/chat.js:6036`
- `static/js/chat.js:6037`

## `getReasoningLevel` — function, line 6028
- **called from:**
- `static/js/chat.js:2227`
- `static/js/chat.js:6028`
- `static/js/chat.js:6042`
- `static/js/chat.js:6099`

## `setReasoningLevel` — function, line 6034
- **called from:**
- `static/js/chat.js:6034`
- `static/js/chat.js:6106`
- `static/js/chat.js:6152`

## `updateThinkingUI` — function, line 6041
- **called from:**
- `static/js/chat.js:6039`
- `static/js/chat.js:6041`
- `static/js/chat.js:6108`
- `static/js/chat.js:6160`
- `static/js/sessions.js:1955`

## `refreshThinkingControl` — function, line 6064
- **called from:**
- `static/js/chat.js:6064`
- `static/js/chat.js:6161`
- `static/js/modelPicker.js:857`
- `static/js/sessions.js:1956`

## `_refreshThinkingControlNow` — function, line 6068
- **called from:**
- `static/js/chat.js:6068`

## `mk` — arrow, line 6082
- **called from:**
- `static/js/chat.js:6093`
- `static/js/chat.js:6094`
- `static/js/chat.js:6095`
- `static/js/cookbookServe.js:2709`
- `static/js/cookbookServe.js:2717`
- `static/js/cookbookServe.js:2722`
- `static/js/cookbookServe.js:2723`
- `static/js/cookbookServe.js:2769`
- `static/js/cookbookServe.js:2770`
- `static/js/documentLibrary.js:2161`
- `static/js/documentLibrary.js:2162`
- `static/js/documentLibrary.js:2593`
- `static/js/documentLibrary.js:2594`
- `static/js/documentLibrary.js:2595`
- `static/js/documentLibrary.js:2596`
- `static/js/skills.js:404`
- `static/js/skills.js:405`
- `static/js/skills.js:420`
- `static/js/skills.js:424`
- `static/js/skills.js:426`
- `static/js/skills.js:427`

## `initThinkingControl` — function, line 6113
- **called from:**
- `static/js/chat.js:6113`
- `static/js/chat.js:6168`

## `_position` — function, line 6126
- **called from:**
- `static/js/chat.js:6126`
- `static/js/chat.js:6135`
- `static/js/chat.js:6158`
- `static/js/chat.js:6159`
- `static/js/modalSnap.js:1039`
- `static/js/modalSnap.js:1078`
- `static/js/slashAutocomplete.js:141`
- `static/js/slashAutocomplete.js:211`
- `static/js/slashAutocomplete.js:299`

## `_open` — function, line 6132
- **called from:**
- `static/js/chat.js:6132`
- `static/js/chat.js:6145`
- `static/js/settings.js:3778`

## `_close` — function, line 6137
- **called from:**
- `static/js/chat.js:6137`
- `static/js/chat.js:6145`
- `static/js/chat.js:6153`
- `static/js/chat.js:6156`
- `static/js/chatRenderer.js:261`
- `static/js/document.js:5281`
- `static/js/document.js:5311`
- `static/js/document.js:5318`
- `static/js/document.js:5324`
- `static/js/modelPicker.js:209`
- `static/js/modelPicker.js:232`
- `static/js/modelPicker.js:677`
- `static/js/modelPicker.js:807`
- `static/js/modelPicker.js:845`
- `static/js/settings.js:3778`
- `static/js/settings.js:3787`

## `initListeners` — function, line 6167
- **called from:**
- `static/app.js:3729`
- `static/js/chat.js:6167`

## `_observeChatHistory` — arrow, line 6189
- **called from:**
- `static/js/chat.js:6194`

## `_dbRowCountBefore` — function, line 6416
- **called from:**
- `static/js/chat.js:6416`
- `static/js/chat.js:6499`
- `static/js/chat.js:6600`
- `static/js/chat.js:6738`

## `editUserMessage` — function, line 6442
- **called from:**
- `static/js/chat.js:6442`
- `static/js/chatRenderer.js:1945`

## `resendUserMessage` — function, line 6539
- **called from:**
- `static/js/chat.js:6539`
- `static/js/chatRenderer.js:369`
- `static/js/chatRenderer.js:1960`

## `regenerateFrom` — function, line 6631
- **called from:**
- `static/js/chat.js:6631`
- `static/js/chatRenderer.js:1761`

## `_attachVariantNav` — function, line 6798
- **called from:**
- `static/js/chat.js:4750`
- `static/js/chat.js:6798`

## `_variantTagText` — function, line 6824
- **called from:**
- `static/js/chat.js:6824`
- `static/js/chat.js:6850`

## `_renderVariantNav` — function, line 6828
- **called from:**
- `static/js/chat.js:6810`
- `static/js/chat.js:6828`
- `static/js/chat.js:6908`
- `static/js/chat.js:7527`

## `_switchVariant` — function, line 6898
- **called from:**
- `static/js/chat.js:6858`
- `static/js/chat.js:6866`
- `static/js/chat.js:6878`
- `static/js/chat.js:6886`
- `static/js/chat.js:6898`

## `forkFrom` — function, line 6921
- **called from:**
- `static/js/chat.js:6921`
- `static/js/chatRenderer.js:1780`

## `checkPendingResearch` — function, line 6955
- **called from:**
- `static/js/chat.js:6955`
- `static/js/sessions.js:2189`

## `updateSpinnerFromProgress` — function, line 7039
- **called from:**
- `static/js/chat.js:7039`
- `static/js/chat.js:7059`
- `static/js/chat.js:7127`

## `setDisplayOverride` — function, line 7176
- **called from:**
- `static/js/chat.js:7176`

## `setHideUserBubble` — function, line 7181
- **called from:**
- `static/js/chat.js:7181`

## `setPendingContinue` — function, line 7186
- **called from:**
- `static/js/chat.js:7186`

## `deleteMessage` — function, line 7200
- **called from:**
- `static/js/chat.js:7200`
- `static/js/chatRenderer.js:1784`
- `static/js/chatRenderer.js:1949`

## `editAIMessage` — function, line 7297
- **called from:**
- `static/js/chat.js:7297`
- `static/js/chatRenderer.js:1752`

## `cleanup` — function, line 7329
- **called from:**
- `static/js/calendar.js:2592`
- `static/js/calendar.js:2629`
- `static/js/calendar.js:2750`
- `static/js/calendar.js:2759`
- `static/js/chat.js:5852`
- `static/js/chat.js:7329`
- `static/js/chat.js:7337`
- `static/js/chat.js:7343`
- `static/js/chat.js:7346`
- `static/js/chat.js:7349`
- `static/js/chat.js:7372`
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

## `rewriteWith` — function, line 7386
- **called from:**
- `static/js/chat.js:7386`
- `static/js/chatRenderer.js:1772`
- `static/js/chatRenderer.js:1776`

## `_killRwSpin` — arrow, line 7423
- **called from:**
- `static/js/chat.js:7469`
- `static/js/chat.js:7534`

## `_stripThink` — arrow, line 7488
- **called from:**
- `static/js/chat.js:7494`

## `continueFrom` — function, line 7544
- **called from:**
- `static/js/chat.js:7544`

## `_attachLang` — function, line 7561
- **called from:**
- `static/js/chat.js:7561`
- `static/js/chat.js:7629`

## `openAttachment` — function, line 7571
- **called from:**
- `static/js/chat.js:7571`
- `static/js/chatRenderer.js:202`
