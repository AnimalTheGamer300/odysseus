# `static/js/cookbookRunning.js` — definitions & call sites

148 definitions (regex-based, best-effort).
**Exports:** `_addTask`, `_clearCookbookNotif`, `_launchServeTask`, `_loadTasks`, `_nextAvailablePort`, `_parseServePhase`, `_processQueue`, `_removeTask`, `_renderRunningTab`, `_retryDownload`, `_saveTasks`, `_selfHealStaleTasks`, `_serveAutoFix`, `_serveAutoRetry`, `_serveAutoRetryRemove`, `_serveAutoRetryReplace`, `_startBackgroundMonitor`, `_syncFromServer`, `_taskPort`, `_tmuxCmd`, `_tmuxForceKill`, `_tmuxGracefulKill`, `_tmuxIsAliveCheck`, `initRunning`

## `_statusLabel` — function, line 17
- **called from:**
- `static/js/cookbookRunning.js:17`
- `static/js/cookbookRunning.js:52`
- `static/js/cookbookRunning.js:2866`
- `static/js/cookbookRunning.js:3109`
- `static/js/cookbookRunning.js:3139`
- `static/js/cookbookRunning.js:3185`
- `static/js/cookbookRunning.js:3245`
- `static/js/cookbookRunning.js:3285`
- `static/js/cookbookRunning.js:3298`
- `static/js/cookbookRunning.js:3516`
- `static/js/cookbookRunning.js:3536`
- `static/js/cookbookRunning.js:3879`

## `_downloadBadgeText` — function, line 24
- **called from:**
- `static/js/cookbookRunning.js:24`
- `static/js/cookbookRunning.js:45`
- `static/js/cookbookRunning.js:4365`

## `_taskBadge` — function, line 42
- **called from:**
- `static/js/cookbookRunning.js:42`
- `static/js/cookbookRunning.js:2346`
- `static/js/cookbookRunning.js:2397`

## `_ggufDisplayPartFromPath` — function, line 55
- **called from:**
- `static/js/cookbookRunning.js:55`
- `static/js/cookbookRunning.js:68`
- `static/js/cookbookRunning.js:86`
- `static/js/cookbookRunning.js:96`

## `_downloadDisplayName` — function, line 65
- **called from:**
- `static/js/cookbookRunning.js:65`
- `static/js/cookbookRunning.js:92`

## `_downloadNameFromPayload` — function, line 72
- **called from:**
- `static/js/cookbookRunning.js:72`
- `static/js/cookbookRunning.js:92`
- `static/js/cookbookRunning.js:1515`

## `_taskDisplayName` — function, line 90
- **called from:**
- `static/js/cookbookRunning.js:90`
- `static/js/cookbookRunning.js:2399`

## `_canLaunchDownloadedTask` — function, line 100
- **called from:**
- `static/js/cookbookRunning.js:100`
- `static/js/cookbookRunning.js:2405`

## `_downloadServeFields` — function, line 104
- **called from:**
- `static/js/cookbookRunning.js:104`
- `static/js/cookbookRunning.js:2481`

## `_downloadOutputLooksActive` — function, line 118
- **called from:**
- `static/js/cookbookRunning.js:118`
- `static/js/cookbookRunning.js:136`
- `static/js/cookbookRunning.js:141`
- `static/js/cookbookRunning.js:2094`
- `static/js/cookbookRunning.js:2501`
- `static/js/cookbookRunning.js:3756`

## `_canClearTask` — function, line 129
- **called from:**
- `static/js/cookbookRunning.js:129`
- `static/js/cookbookRunning.js:2241`
- `static/js/cookbookRunning.js:2256`
- `static/js/cookbookRunning.js:2356`
- `static/js/cookbookRunning.js:2405`

## `_clearPillLabel` — function, line 140
- **called from:**
- `static/js/cookbookRunning.js:140`
- `static/js/cookbookRunning.js:2358`
- `static/js/cookbookRunning.js:2405`

## `_venvRootFromPath` — function, line 145
- **called from:**
- `static/js/cookbook.js:647`
- `static/js/cookbook.js:680`
- `static/js/cookbookRunning.js:145`
- `static/js/cookbookRunning.js:1981`

## `_depInstallSucceeded` — function, line 160
- **called from:**
- `static/js/cookbookRunning.js:160`
- `static/js/cookbookRunning.js:3130`
- `static/js/cookbookRunning.js:4192`

## `_shouldOfferCrashReport` — function, line 169
- **called from:**
- `static/js/cookbookRunning.js:169`
- `static/js/cookbookRunning.js:2712`

## `_serveTaskLooksAwqOnLocalBackend` — function, line 175
- **called from:**
- `static/js/cookbookRunning.js:175`
- `static/js/cookbookRunning.js:242`
- `static/js/cookbookRunning.js:3155`
- `static/js/cookbookRunning.js:3160`

## `_serveTaskLooksAwqWithoutUsableAccelerator` — function, line 181
- **called from:**
- `static/js/cookbookRunning.js:181`
- `static/js/cookbookRunning.js:252`

## `_openDownloadForGgufTask` — function, line 188
- **called from:**
- `static/js/cookbookRunning.js:188`
- `static/js/cookbookRunning.js:247`
- `static/js/cookbookRunning.js:257`

## `_terminalServeDiagnosis` — function, line 224
- **called from:**
- `static/js/cookbookRunning.js:224`
- `static/js/cookbookRunning.js:2368`
- `static/js/cookbookRunning.js:2417`

## `_redactCrashReportText` — function, line 273
- **called from:**
- `static/js/cookbookRunning.js:273`
- `static/js/cookbookRunning.js:286`
- `static/js/cookbookRunning.js:306`

## `_lastLines` — function, line 285
- **called from:**
- `static/js/cookbookRunning.js:285`
- `static/js/cookbookRunning.js:329`

## `_codeFence` — function, line 291
- **called from:**
- `static/js/cookbookRunning.js:291`
- `static/js/cookbookRunning.js:327`
- `static/js/cookbookRunning.js:329`

## `_taskHostLabel` — function, line 295
- **called from:**
- `static/js/cookbookRunning.js:295`
- `static/js/cookbookRunning.js:319`

## `_taskPort` — function, line 300
- **called from:**
- `static/js/cookbook-hwfit.js:1720`
- `static/js/cookbookRunning.js:300`
- `static/js/cookbookRunning.js:323`
- `static/js/cookbookRunning.js:518`
- `static/js/cookbookServe.js:86`
- `static/js/cookbookServe.js:3364`

## `_buildCrashReport` — function, line 304
- **called from:**
- `static/js/cookbookRunning.js:304`
- `static/js/cookbookRunning.js:2715`

## `_taskServerSelection` — function, line 357
- **called from:**
- `static/js/cookbookRunning.js:357`
- `static/js/cookbookRunning.js:397`

## `_serverColorForTaskGroup` — function, line 368
- **called from:**
- `static/js/cookbookRunning.js:368`
- `static/js/cookbookRunning.js:2228`

## `_serverHeaderStyle` — function, line 381
- **called from:**
- `static/js/cookbookRunning.js:381`
- `static/js/cookbookRunning.js:2229`

## `_shouldAutoExpandTaskOutput` — function, line 390
- **called from:**
- `static/js/cookbookRunning.js:390`
- `static/js/cookbookRunning.js:2411`

## `_selectTaskServer` — function, line 396
- **called from:**
- `static/js/cookbookRunning.js:396`
- `static/js/cookbookRunning.js:1612`
- `static/js/cookbookRunning.js:2478`

## `_parseServePhase` — function, line 438
- **called from:**
- `static/js/cookbookRunning.js:438`
- `static/js/cookbookRunning.js:3561`

## `_nextAvailablePort` — function, line 512
- **called from:**
- `static/js/cookbook-hwfit.js:1707`
- `static/js/cookbookRunning.js:512`
- `static/js/cookbookServe.js:1541`

## `_removeEndpointByUrl` — function, line 530
- **called from:**
- `static/js/cookbookRunning.js:530`
- `static/js/cookbookRunning.js:2883`
- `static/js/cookbookRunning.js:2961`

## `_refreshModelsAfterEndpointChange` — function, line 545
- **called from:**
- `static/js/cookbookRunning.js:540`
- `static/js/cookbookRunning.js:545`
- `static/js/cookbookRunning.js:2031`
- `static/js/cookbookRunning.js:2663`
- `static/js/cookbookRunning.js:2681`
- `static/js/cookbookRunning.js:2968`
- `static/js/cookbookRunning.js:3569`

## `_appendCookbookEndpointScope` — function, line 578
- **called from:**
- `static/js/cookbookRunning.js:578`
- `static/js/cookbookRunning.js:2674`
- `static/js/cookbookRunning.js:3660`
- `static/js/cookbookRunning.js:4319`

## `_connectHostFromRemote` — function, line 585
- **called from:**
- `static/js/cookbookRunning.js:585`
- `static/js/cookbookRunning.js:1166`
- `static/js/cookbookRunning.js:2651`
- `static/js/cookbookRunning.js:3616`
- `static/js/cookbookRunning.js:3846`
- `static/js/cookbookRunning.js:4273`

## `_isAnyBindHost` — function, line 591
- **called from:**
- `static/js/cookbookRunning.js:591`
- `static/js/cookbookRunning.js:599`

## `_endpointFromAdvertisedUrl` — function, line 596
- **called from:**
- `static/js/cookbookRunning.js:596`
- `static/js/cookbookRunning.js:3627`
- `static/js/cookbookRunning.js:4281`

## `_serveExpectedModel` — function, line 608
- **called from:**
- `static/js/cookbookRunning.js:608`
- `static/js/cookbookRunning.js:631`
- `static/js/cookbookRunning.js:638`
- `static/js/cookbookRunning.js:651`

## `_modelIdMatchesExpected` — function, line 620
- **called from:**
- `static/js/cookbookRunning.js:620`
- `static/js/cookbookRunning.js:634`

## `_endpointMatchesServe` — function, line 630
- **called from:**
- `static/js/cookbookRunning.js:630`
- `static/js/cookbookRunning.js:3642`
- `static/js/cookbookRunning.js:4304`

## `_markServeEndpointMismatch` — function, line 637
- **called from:**
- `static/js/cookbookRunning.js:637`
- `static/js/cookbookRunning.js:3643`
- `static/js/cookbookRunning.js:4305`

## `_appendPinnedServeModel` — function, line 650
- **called from:**
- `static/js/cookbookRunning.js:650`
- `static/js/cookbookRunning.js:3661`
- `static/js/cookbookRunning.js:4320`

## `_isImageServeTask` — function, line 655
- **called from:**
- `static/js/cookbookRunning.js:655`
- `static/js/cookbookRunning.js:2675`
- `static/js/cookbookRunning.js:3655`
- `static/js/cookbookRunning.js:4284`

## `_processQueue` — function, line 662
- **called from:**
- `static/js/cookbookRunning.js:662`
- `static/js/cookbookRunning.js:3251`
- `static/js/cookbookRunning.js:3305`
- `static/js/cookbookRunning.js:3312`
- `static/js/cookbookRunning.js:3551`
- `static/js/tts-ai.js:259`
- `static/js/tts-ai.js:263`

## `_startQueuedDownload` — function, line 678
- **called from:**
- `static/js/cookbookRunning.js:674`
- `static/js/cookbookRunning.js:678`
- `static/js/cookbookRunning.js:2538`
- `static/js/cookbookRunning.js:2622`

## `_serveOutputLooksReady` — function, line 746
- **called from:**
- `static/js/cookbookRunning.js:131`
- `static/js/cookbookRunning.js:233`
- `static/js/cookbookRunning.js:746`
- `static/js/cookbookRunning.js:776`
- `static/js/cookbookRunning.js:3125`
- `static/js/cookbookRunning.js:4204`

## `_normalizeTaskForDisplay` — function, line 754
- **called from:**
- `static/js/cookbookRunning.js:754`

## `_loadTasks` — function, line 782
- **called from:**
- `static/js/cookbook-diagnosis.js:156`
- `static/js/cookbook-diagnosis.js:915`
- `static/js/cookbook-hwfit.js:1715`
- `static/js/cookbook.js:1047`
- `static/js/cookbook.js:1064`
- `static/js/cookbook.js:2064`
- `static/js/cookbookDownload.js:558`
- `static/js/cookbookDownload.js:596`
- `static/js/cookbookDownload.js:613`
- `static/js/cookbookRunning.js:513`
- `static/js/cookbookRunning.js:689`
- `static/js/cookbookRunning.js:720`
- `static/js/cookbookRunning.js:782`
- `static/js/cookbookRunning.js:828`
- `static/js/cookbookRunning.js:915`
- `static/js/cookbookRunning.js:954`
- `static/js/cookbookRunning.js:984`
- `static/js/cookbookRunning.js:1339`
- `static/js/cookbookRunning.js:1396`
- `static/js/cookbookRunning.js:1512`
- `static/js/cookbookRunning.js:1562`
- `static/js/cookbookRunning.js:1626`
- `static/js/cookbookRunning.js:1668`
- `static/js/cookbookRunning.js:1701`
- `static/js/cookbookRunning.js:1928`
- `static/js/cookbookRunning.js:1947`
- `static/js/cookbookRunning.js:2084`
- `static/js/cookbookRunning.js:2240`
- `static/js/cookbookRunning.js:2290`
- `static/js/cookbookRunning.js:2502`
- `static/js/cookbookRunning.js:3267`
- `static/js/cookbookRunning.js:3288`
- `static/js/cookbookRunning.js:3751`
- `static/js/cookbookRunning.js:3830`
- `static/js/cookbookRunning.js:3947`
- `static/js/cookbookRunning.js:3983`
- `static/js/cookbookRunning.js:4013`
- `static/js/cookbookRunning.js:4122`
- `static/js/cookbookRunning.js:4152`
- `static/js/cookbookRunning.js:4270`
- `static/js/cookbookServe.js:80`
- `static/js/cookbookServe.js:3354`

## `_downloadRepoKey` — function, line 787
- **called from:**
- `static/js/cookbookRunning.js:787`
- `static/js/cookbookRunning.js:797`

## `_downloadHostKey` — function, line 791
- **called from:**
- `static/js/cookbookRunning.js:791`
- `static/js/cookbookRunning.js:799`

## `_downloadDedupeKey` — function, line 795
- **called from:**
- `static/js/cookbookRunning.js:718`
- `static/js/cookbookRunning.js:730`
- `static/js/cookbookRunning.js:795`
- `static/js/cookbookRunning.js:807`
- `static/js/cookbookRunning.js:815`
- `static/js/cookbookRunning.js:929`
- `static/js/cookbookRunning.js:932`

## `_pruneQueuedDownloadDuplicates` — function, line 802
- **called from:**
- `static/js/cookbookRunning.js:802`
- `static/js/cookbookRunning.js:829`

## `_loadPrunedTasks` — function, line 827
- **called from:**
- `static/js/cookbookRunning.js:663`
- `static/js/cookbookRunning.js:827`
- `static/js/cookbookRunning.js:2045`

## `_loadTombstones` — function, line 841
- **called from:**
- `static/js/cookbookRunning.js:841`
- `static/js/cookbookRunning.js:862`
- `static/js/cookbookRunning.js:869`
- `static/js/cookbookRunning.js:1340`
- `static/js/cookbookRunning.js:1399`

## `_saveTombstones` — function, line 857
- **called from:**
- `static/js/cookbookRunning.js:857`
- `static/js/cookbookRunning.js:866`
- `static/js/cookbookRunning.js:1404`

## `_tombstoneTask` — function, line 860
- **called from:**
- `static/js/cookbookRunning.js:860`
- `static/js/cookbookRunning.js:983`
- `static/js/cookbookRunning.js:2255`

## `_isTombstoned` — function, line 868
- **called from:**
- `static/js/cookbookRunning.js:868`
- `static/js/cookbookRunning.js:1407`
- `static/js/cookbookRunning.js:1409`
- `static/js/cookbookRunning.js:4127`
- `static/js/cookbookRunning.js:4158`

## `_redactStoredText` — function, line 873
- **called from:**
- `static/js/cookbookRunning.js:873`
- `static/js/cookbookRunning.js:887`
- `static/js/cookbookRunning.js:892`
- `static/js/cookbookRunning.js:893`
- `static/js/cookbookRunning.js:1247`
- `static/js/cookbookRunning.js:1248`

## `_isServeOutputPlaceholder` — function, line 879
- **called from:**
- `static/js/cookbookRunning.js:879`
- `static/js/cookbookRunning.js:4233`

## `_redactTaskForStorage` — function, line 884
- **called from:**
- `static/js/cookbookRunning.js:732`
- `static/js/cookbookRunning.js:884`
- `static/js/cookbookRunning.js:935`
- `static/js/cookbookRunning.js:4163`

## `_stripStateSecrets` — function, line 898
- **called from:**
- `static/js/cookbookRunning.js:898`
- `static/js/cookbookRunning.js:1354`

## `_saveTasks` — function, line 909
- **called from:**
- `static/js/cookbook.js:1047`
- `static/js/cookbook.js:1064`
- `static/js/cookbook.js:2064`
- `static/js/cookbookDownload.js:601`
- `static/js/cookbookDownload.js:615`
- `static/js/cookbookRunning.js:695`
- `static/js/cookbookRunning.js:733`
- `static/js/cookbookRunning.js:830`
- `static/js/cookbookRunning.js:909`
- `static/js/cookbookRunning.js:937`
- `static/js/cookbookRunning.js:958`
- `static/js/cookbookRunning.js:985`
- `static/js/cookbookRunning.js:1523`
- `static/js/cookbookRunning.js:2257`
- `static/js/cookbookRunning.js:2507`
- `static/js/cookbookRunning.js:4019`
- `static/js/cookbookRunning.js:4250`

## `_addTask` — function, line 914
- **called from:**
- `static/js/cookbook-hwfit.js:1953`
- `static/js/cookbook.js:1496`
- `static/js/cookbook.js:1557`
- `static/js/cookbook.js:1771`
- `static/js/cookbookDownload.js:639`
- `static/js/cookbookRunning.js:914`
- `static/js/cookbookRunning.js:1528`
- `static/js/cookbookRunning.js:1531`
- `static/js/cookbookRunning.js:2026`

## `_updateTask` — function, line 953
- **called from:**
- `static/js/cookbookRunning.js:641`
- `static/js/cookbookRunning.js:680`
- `static/js/cookbookRunning.js:706`
- `static/js/cookbookRunning.js:712`
- `static/js/cookbookRunning.js:739`
- `static/js/cookbookRunning.js:953`
- `static/js/cookbookRunning.js:1479`
- `static/js/cookbookRunning.js:1502`
- `static/js/cookbookRunning.js:1508`
- `static/js/cookbookRunning.js:1536`
- `static/js/cookbookRunning.js:2295`
- `static/js/cookbookRunning.js:2662`
- `static/js/cookbookRunning.js:2679`
- `static/js/cookbookRunning.js:2863`
- `static/js/cookbookRunning.js:2879`
- `static/js/cookbookRunning.js:3106`
- `static/js/cookbookRunning.js:3136`
- `static/js/cookbookRunning.js:3182`
- `static/js/cookbookRunning.js:3242`
- `static/js/cookbookRunning.js:3264`
- `static/js/cookbookRunning.js:3280`
- `static/js/cookbookRunning.js:3292`
- `static/js/cookbookRunning.js:3384`
- `static/js/cookbookRunning.js:3414`
- `static/js/cookbookRunning.js:3518`
- `static/js/cookbookRunning.js:3542`
- `static/js/cookbookRunning.js:3564`
- `static/js/cookbookRunning.js:3582`
- `static/js/cookbookRunning.js:3590`
- `static/js/cookbookRunning.js:3592`
- `static/js/cookbookRunning.js:3647`
- `static/js/cookbookRunning.js:3669`
- `static/js/cookbookRunning.js:3710`
- `static/js/cookbookRunning.js:3723`
- `static/js/cookbookRunning.js:3728`
- `static/js/cookbookRunning.js:3861`
- `static/js/cookbookRunning.js:3866`
- `static/js/cookbookRunning.js:4286`
- `static/js/cookbookRunning.js:4308`
- `static/js/cookbookRunning.js:4327`
- `static/js/tasks.js:84`
- `static/js/tasks.js:1781`

## `_refreshDepsAfterInstall` — function, line 975
- **called from:**
- `static/js/cookbookRunning.js:975`
- `static/js/cookbookRunning.js:3249`
- `static/js/cookbookRunning.js:3303`
- `static/js/cookbookRunning.js:3545`
- `static/js/cookbookRunning.js:4258`

## `_removeTask` — function, line 982
- **called from:**
- `static/js/cookbookRunning.js:982`
- `static/js/cookbookRunning.js:992`
- `static/js/cookbookRunning.js:997`
- `static/js/cookbookRunning.js:1475`
- `static/js/cookbookRunning.js:1935`
- `static/js/cookbookRunning.js:1958`
- `static/js/cookbookRunning.js:3510`

## `_animateOutThenRemove` — function, line 991
- **called from:**
- `static/js/cookbookRunning.js:991`
- `static/js/cookbookRunning.js:1576`
- `static/js/cookbookRunning.js:1639`
- `static/js/cookbookRunning.js:1681`
- `static/js/cookbookRunning.js:1714`
- `static/js/cookbookRunning.js:2484`
- `static/js/cookbookRunning.js:2530`
- `static/js/cookbookRunning.js:2905`
- `static/js/cookbookRunning.js:2972`
- `static/js/research/panel.js:419`
- `static/js/research/panel.js:1046`
- `static/js/research/panel.js:1050`

## `_taskRemoteHost` — function, line 1002
- **called from:**
- `static/js/cookbookRunning.js:1002`
- `static/js/cookbookRunning.js:1014`
- `static/js/cookbookRunning.js:1022`
- `static/js/cookbookRunning.js:1054`
- `static/js/cookbookRunning.js:1060`
- `static/js/cookbookRunning.js:1074`
- `static/js/cookbookRunning.js:1101`
- `static/js/cookbookRunning.js:1118`
- `static/js/cookbookRunning.js:1155`
- `static/js/cookbookRunning.js:1166`

## `_remoteTmuxPrefix` — function, line 1006
- **called from:**
- `static/js/cookbookRunning.js:1006`
- `static/js/cookbookRunning.js:1016`
- `static/js/cookbookRunning.js:1049`
- `static/js/cookbookRunning.js:1076`
- `static/js/cookbookRunning.js:1103`
- `static/js/cookbookRunning.js:1120`

## `_tmuxCmd` — function, line 1010
- **called from:**
- `static/js/cookbookRunning.js:1010`
- `static/js/cookbookRunning.js:1567`
- `static/js/cookbookRunning.js:1635`
- `static/js/cookbookRunning.js:1677`
- `static/js/cookbookRunning.js:1710`
- `static/js/cookbookRunning.js:2527`
- `static/js/cookbookRunning.js:2942`
- `static/js/cookbookRunning.js:3061`
- `static/js/cookbookRunning.js:3075`
- `static/js/cookbookRunning.js:3274`
- `static/js/cookbookRunning.js:3392`
- `static/js/cookbookRunning.js:3507`
- `static/js/cookbookRunning.js:3549`
- `static/js/cookbookRunning.js:4008`

## `_winSessionCmd` — function, line 1021
- **called from:**
- `static/js/cookbookRunning.js:1012`
- `static/js/cookbookRunning.js:1021`

## `_winPowerShellCmd` — function, line 1052
- **called from:**
- `static/js/cookbookRunning.js:1031`
- `static/js/cookbookRunning.js:1037`
- `static/js/cookbookRunning.js:1041`
- `static/js/cookbookRunning.js:1047`
- `static/js/cookbookRunning.js:1052`
- `static/js/cookbookRunning.js:1072`

## `_winSessionStopTreePs` — function, line 1059
- **called from:**
- `static/js/cookbookRunning.js:1040`
- `static/js/cookbookRunning.js:1059`
- `static/js/cookbookRunning.js:1071`

## `_tmuxGracefulKill` — function, line 1069
- **called from:**
- `static/js/cookbook-hwfit.js:1744`
- `static/js/cookbookRunning.js:1069`
- `static/js/cookbookRunning.js:1089`
- `static/js/cookbookRunning.js:1470`
- `static/js/cookbookRunning.js:1933`
- `static/js/cookbookRunning.js:1955`
- `static/js/cookbookRunning.js:2900`
- `static/js/cookbookRunning.js:2931`
- `static/js/cookbookServe.js:3401`

## `_tmuxForceKill` — function, line 1085
- **called from:**
- `static/js/cookbookRunning.js:1085`

## `_tmuxIsAliveCheck` — function, line 1111
- **called from:**
- `static/js/cookbookRunning.js:1111`

## `_shQuote` — function, line 1125
- **called from:**
- `static/js/cookbookRunning.js:1056`
- `static/js/cookbookRunning.js:1103`
- `static/js/cookbookRunning.js:1120`
- `static/js/cookbookRunning.js:1125`
- `static/js/cookbookRunning.js:1154`
- `static/js/cookbookRunning.js:1154`
- `static/js/cookbookRunning.js:1157`

## `_taskLooksOllama` — function, line 1129
- **called from:**
- `static/js/cookbookRunning.js:1129`
- `static/js/cookbookRunning.js:1149`
- `static/js/cookbookRunning.js:1163`

## `_ollamaBaseUrlForTask` — function, line 1134
- **called from:**
- `static/js/cookbookRunning.js:1134`
- `static/js/cookbookRunning.js:1152`
- `static/js/cookbookRunning.js:1164`

## `_ollamaModelForTask` — function, line 1144
- **called from:**
- `static/js/cookbookRunning.js:1144`
- `static/js/cookbookRunning.js:1150`

## `_ollamaUnloadCommand` — function, line 1148
- **called from:**
- `static/js/cookbookRunning.js:1148`
- `static/js/cookbookRunning.js:2885`
- `static/js/cookbookRunning.js:2916`

## `_endpointUrlForTask` — function, line 1162
- **called from:**
- `static/js/cookbookRunning.js:1162`
- `static/js/cookbookRunning.js:2883`
- `static/js/cookbookRunning.js:2960`

## `_startWaveSync` — function, line 1179
- **called from:**
- `static/js/cookbookRunning.js:1179`
- `static/js/cookbookRunning.js:1191`
- `static/js/cookbookRunning.js:3014`

## `_registerWaveEl` — function, line 1191
- **called from:**
- `static/js/cookbookRunning.js:1191`
- `static/js/cookbookRunning.js:2415`

## `_showCookbookNotif` — function, line 1195
- **called from:**
- `static/js/cookbookRunning.js:1195`
- `static/js/cookbookRunning.js:3110`
- `static/js/cookbookRunning.js:3230`
- `static/js/cookbookRunning.js:3248`
- `static/js/cookbookRunning.js:3302`
- `static/js/cookbookRunning.js:3387`
- `static/js/cookbookRunning.js:3425`
- `static/js/cookbookRunning.js:3530`
- `static/js/cookbookRunning.js:3544`
- `static/js/cookbookRunning.js:3713`
- `static/js/cookbookRunning.js:3885`
- `static/js/cookbookRunning.js:4342`
- `static/js/cookbookRunning.js:4344`
- `static/js/cookbookRunning.js:4346`

## `_clearCookbookNotif` — function, line 1211
- **called from:**
- `static/js/cookbook.js:3415`
- `static/js/cookbookRunning.js:1211`
- `static/js/cookbookRunning.js:2046`
- `static/js/cookbookRunning.js:4348`
- `static/js/cookbookRunning.js:4387`

## `_presetEnvFields` — function, line 1230
- **called from:**
- `static/js/cookbookRunning.js:1230`
- `static/js/cookbookRunning.js:1260`
- `static/js/cookbookRunning.js:1316`

## `_redactPresetForStorage` — function, line 1244
- **called from:**
- `static/js/cookbookRunning.js:1244`
- `static/js/cookbookRunning.js:1260`
- `static/js/cookbookRunning.js:1312`

## `_saveTaskAsPreset` — function, line 1254
- **called from:**
- `static/js/cookbookRunning.js:1254`
- `static/js/cookbookRunning.js:2640`

## `_presetsForModelLocal` — function, line 1267
- **called from:**
- `static/js/cookbookRunning.js:1267`
- `static/js/cookbookRunning.js:1308`

## `_autoConfigLabel` — function, line 1277
- **called from:**
- `static/js/cookbookRunning.js:1277`
- `static/js/cookbookRunning.js:1315`

## `_autoSaveWorkingConfig` — function, line 1293
- **called from:**
- `static/js/cookbookRunning.js:1293`
- `static/js/cookbookRunning.js:3648`
- `static/js/cookbookRunning.js:3670`
- `static/js/cookbookRunning.js:4287`

## `_syncToServer` — function, line 1326
- **called from:**
- `static/js/cookbookRunning.js:911`
- `static/js/cookbookRunning.js:1326`
- `static/js/cookbookRunning.js:1361`
- `static/js/theme.js:631`
- `static/js/theme.js:634`

## `_normalizeState` — function, line 1368
- **called from:**
- `static/js/cookbookRunning.js:1368`
- `static/js/cookbookRunning.js:1393`

## `_syncFromServer` — function, line 1389
- **called from:**
- `static/js/cookbook.js:1948`
- `static/js/cookbook.js:3385`
- `static/js/cookbook.js:3548`
- `static/js/cookbookRunning.js:1389`
- `static/js/cookbookRunning.js:4428`

## `_retryTask` — function, line 1462
- **called from:**
- `static/js/cookbookRunning.js:1462`
- `static/js/cookbookRunning.js:2976`
- `static/js/cookbookRunning.js:3208`
- `static/js/cookbookRunning.js:3216`
- `static/js/cookbookRunning.js:3380`

## `_retryDownload` — function, line 1489
- **called from:**
- `static/js/cookbook.js:2556`
- `static/js/cookbookRunning.js:1484`
- `static/js/cookbookRunning.js:1489`
- `static/js/cookbookRunning.js:3511`
- `static/js/cookbookServe.js:3960`

## `_guardServeRetry` — function, line 1547
- **called from:**
- `static/js/cookbookRunning.js:1547`
- `static/js/cookbookRunning.js:1565`
- `static/js/cookbookRunning.js:1629`
- `static/js/cookbookRunning.js:1671`
- `static/js/cookbookRunning.js:1704`

## `_serveAutoFix` — function, line 1558
- **called from:**
- `static/js/cookbook-diagnosis.js:595`
- `static/js/cookbookRunning.js:1558`

## `_openServeEditForTask` — function, line 1597
- **called from:**
- `static/js/cookbookRunning.js:248`
- `static/js/cookbookRunning.js:258`
- `static/js/cookbookRunning.js:269`
- `static/js/cookbookRunning.js:1597`
- `static/js/cookbookRunning.js:2462`
- `static/js/cookbookRunning.js:2465`
- `static/js/cookbookRunning.js:3165`

## `_serveAutoRetryReplace` — function, line 1622
- **called from:**
- `static/js/cookbook-diagnosis.js:288`
- `static/js/cookbook-diagnosis.js:289`
- `static/js/cookbook-diagnosis.js:290`
- `static/js/cookbook-diagnosis.js:297`
- `static/js/cookbook-diagnosis.js:307`
- `static/js/cookbook-diagnosis.js:308`
- `static/js/cookbook-diagnosis.js:330`
- `static/js/cookbook-diagnosis.js:331`
- `static/js/cookbook-diagnosis.js:339`
- `static/js/cookbook-diagnosis.js:340`
- `static/js/cookbook-diagnosis.js:341`
- `static/js/cookbook-diagnosis.js:342`
- `static/js/cookbook-diagnosis.js:351`
- `static/js/cookbook-diagnosis.js:352`
- `static/js/cookbook-diagnosis.js:372`
- `static/js/cookbook-diagnosis.js:373`
- `static/js/cookbook-diagnosis.js:374`
- `static/js/cookbook-diagnosis.js:382`
- `static/js/cookbook-diagnosis.js:787`
- `static/js/cookbookRunning.js:1622`

## `_serveAutoRetryRemove` — function, line 1664
- **called from:**
- `static/js/cookbook-diagnosis.js:381`
- `static/js/cookbook-diagnosis.js:389`
- `static/js/cookbook-diagnosis.js:397`
- `static/js/cookbookRunning.js:1664`

## `_serveAutoRetry` — function, line 1697
- **called from:**
- `static/js/cookbook-diagnosis.js:298`
- `static/js/cookbook-diagnosis.js:299`
- `static/js/cookbook-diagnosis.js:343`
- `static/js/cookbook-diagnosis.js:612`
- `static/js/cookbook-diagnosis.js:613`
- `static/js/cookbook-diagnosis.js:629`
- `static/js/cookbook-diagnosis.js:636`
- `static/js/cookbook-diagnosis.js:643`
- `static/js/cookbookRunning.js:1697`

## `_promptEditServeCmd` — function, line 1734
- **called from:**
- `static/js/cookbookRunning.js:1734`

## `close` — arrow, line 1752
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
- `core/database.py:930`
- `core/database.py:961`
- `core/database.py:984`
- `core/database.py:1009`
- `core/database.py:1032`
- `core/database.py:1055`
- `core/database.py:1086`
- `core/database.py:1111`
- `core/database.py:1135`
- `core/database.py:1163`
- `core/database.py:1186`
- `core/database.py:1209`
- `core/database.py:1232`
- `core/database.py:1255`
- `core/database.py:1287`
- `core/database.py:1310`
- `core/database.py:1333`
- `core/database.py:1357`
- `core/database.py:1381`
- `core/database.py:1415`
- `core/database.py:1444`
- `core/database.py:1517`
- `core/database.py:2106`
- `core/database.py:2340`
- `core/database.py:2402`
- `core/database.py:2518`
- `core/database.py:2545`
- `core/database.py:2571`
- `core/database.py:2596`
- `core/database.py:2623`
- `core/database.py:2645`
- `core/database.py:2658`
- `core/database.py:2674`
- `core/session_manager.py:68`
- `core/session_manager.py:178`
- `core/session_manager.py:442`
- `core/session_manager.py:582`
- `core/session_manager.py:654`
- `core/session_manager.py:689`
- `core/session_manager.py:760`
- `core/session_manager.py:880`
- `core/session_manager.py:984`
- `core/session_manager.py:1014`
- `core/session_manager.py:1028`
- `core/session_manager.py:1074`
- `core/session_manager.py:1118`
- `core/session_manager.py:1149`
- `core/session_manager.py:1173`
- `core/session_manager.py:1209`
- `core/session_manager.py:1233`
- `core/session_manager.py:1253`
- … +763 more (grep the name in repo)

## `onKey` — arrow, line 1757
- **called from:**
- `static/js/cookbookServe.js:1053`
- `static/js/document.js:6145`
- `static/js/galleryEditor.js:3973`
- `static/js/settings.js:1933`
- `static/js/skills.js:1466`
- `static/js/ui.js:669`
- `static/js/ui.js:767`

## `_parseServeCmdToFields` — function, line 1773
- **called from:**
- `static/js/cookbookRunning.js:1603`
- `static/js/cookbookRunning.js:1604`
- `static/js/cookbookRunning.js:1773`

## `ex` — arrow, line 1775
- **called from:**
- `static/js/cookbookRunning.js:1783`
- `static/js/cookbookRunning.js:1784`
- `static/js/cookbookRunning.js:1785`
- `static/js/cookbookRunning.js:1785`
- `static/js/cookbookRunning.js:1785`
- `static/js/cookbookRunning.js:1785`
- `static/js/cookbookRunning.js:1785`
- `static/js/cookbookRunning.js:1786`
- `static/js/cookbookRunning.js:1787`
- `static/js/cookbookRunning.js:1788`
- `static/js/cookbookRunning.js:1789`
- `static/js/cookbookRunning.js:1790`
- `static/js/cookbookRunning.js:1791`
- `static/js/cookbookRunning.js:1792`
- `static/js/cookbookRunning.js:1793`
- `static/js/cookbookRunning.js:1794`
- `static/js/cookbookRunning.js:1795`
- `static/js/cookbookRunning.js:1796`
- `static/js/cookbookRunning.js:1797`
- `static/js/cookbookRunning.js:1798`
- `static/js/cookbookRunning.js:1799`
- `static/js/cookbookRunning.js:1800`

## `_serveCmdNeedsGpuPreflight` — function, line 1817
- **called from:**
- `static/js/cookbookRunning.js:1817`
- `static/js/cookbookRunning.js:1884`

## `_selectedGpuIndexes` — function, line 1824
- **called from:**
- `static/js/cookbookRunning.js:1824`
- `static/js/cookbookRunning.js:1895`

## `_gbFromMb` — function, line 1843
- **called from:**
- `static/js/cookbookRunning.js:1843`
- `static/js/cookbookRunning.js:1861`
- `static/js/cookbookRunning.js:1873`
- `static/js/cookbookRunning.js:1873`
- `static/js/cookbookRunning.js:1875`
- `static/js/cookbookRunning.js:1875`

## `_gpuPreflightIssues` — function, line 1849
- **called from:**
- `static/js/cookbookRunning.js:1849`
- `static/js/cookbookRunning.js:1896`

## `_confirmGpuPreflight` — function, line 1883
- **called from:**
- `static/js/cookbookRunning.js:1883`
- `static/js/cookbookRunning.js:2000`

## `_launchServeTask` — function, line 1911
- **called from:**
- `static/js/cookbook-diagnosis.js:187`
- `static/js/cookbook-diagnosis.js:203`
- `static/js/cookbook-diagnosis.js:649`
- `static/js/cookbook-diagnosis.js:660`
- `static/js/cookbook-diagnosis.js:747`
- `static/js/cookbook-diagnosis.js:772`
- `static/js/cookbook-diagnosis.js:794`
- `static/js/cookbook-diagnosis.js:813`
- `static/js/cookbook-diagnosis.js:818`
- `static/js/cookbook.js:2238`
- `static/js/cookbookRunning.js:1476`
- `static/js/cookbookRunning.js:1585`
- `static/js/cookbookRunning.js:1658`
- `static/js/cookbookRunning.js:1691`
- `static/js/cookbookRunning.js:1725`
- `static/js/cookbookRunning.js:1911`
- `static/js/cookbookRunning.js:3114`
- `static/js/cookbookServe.js:3712`

## `_renderRunningTab` — function, line 2039
- **called from:**
- `static/js/cookbook-hwfit.js:1954`
- `static/js/cookbook.js:3355`
- `static/js/cookbook.js:3382`
- `static/js/cookbook.js:3416`
- `static/js/cookbook.js:3554`
- `static/js/cookbook.js:3575`
- `static/js/cookbookDownload.js:567`
- `static/js/cookbookDownload.js:603`
- `static/js/cookbookDownload.js:616`
- `static/js/cookbookRunning.js:681`
- `static/js/cookbookRunning.js:707`
- `static/js/cookbookRunning.js:713`
- `static/js/cookbookRunning.js:734`
- `static/js/cookbookRunning.js:737`
- `static/js/cookbookRunning.js:740`
- `static/js/cookbookRunning.js:940`
- `static/js/cookbookRunning.js:986`
- `static/js/cookbookRunning.js:1525`
- `static/js/cookbookRunning.js:2039`
- `static/js/cookbookRunning.js:2114`
- `static/js/cookbookRunning.js:2278`
- `static/js/cookbookRunning.js:2518`
- `static/js/cookbookRunning.js:2623`
- `static/js/cookbookRunning.js:2642`
- `static/js/cookbookRunning.js:3250`
- `static/js/cookbookRunning.js:3304`
- `static/js/cookbookRunning.js:3311`
- `static/js/cookbookRunning.js:3726`
- `static/js/cookbookRunning.js:4037`
- `static/js/cookbookRunning.js:4134`
- `static/js/cookbookRunning.js:4251`

## `_ensureSection` — function, line 2159
- **called from:**
- `static/js/cookbookRunning.js:2159`
- `static/js/cookbookRunning.js:2221`

## `_taskServerKey` — arrow, line 2175
- **called from:**
- `static/js/cookbookRunning.js:2192`
- `static/js/cookbookRunning.js:2241`
- `static/js/cookbookRunning.js:2246`
- `static/js/cookbookRunning.js:2256`
- `static/js/cookbookRunning.js:2290`
- `static/js/cookbookRunning.js:2996`

## `_serverName` — arrow, line 2176
- **called from:**
- `static/js/cookbookRunning.js:2193`
- `static/js/cookbookRunning.js:2248`
- `static/js/cookbookRunning.js:2249`
- `static/js/cookbookRunning.js:2254`
- `static/js/cookbookRunning.js:2291`
- `static/js/cookbookRunning.js:2292`
- `static/js/cookbookRunning.js:2302`

## `_openEdit` — arrow, line 2462
- **called from:**
- `static/js/cookbookRunning.js:2636`

## `_lpStart` — arrow, line 2574
- **called from:**
- `static/js/cookbookRunning.js:2594`

## `_lpCancel` — arrow, line 2583
- **called from:**
- `static/js/cookbookRunning.js:2588`
- `static/js/memory.js:969`
- `static/js/skills.js:837`

## `_lpMove` — arrow, line 2586
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_openTaskMenu` — arrow, line 2600
- **called from:**
- `static/js/cookbookRunning.js:2846`

## `closeHandler` — arrow, line 2816
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `scrollClose` — arrow, line 2824
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_unreg` — arrow, line 2825
- **called from:**
- `static/js/cookbookRunning.js:2827`
- `static/js/documentLibrary.js:247`
- `static/js/documentLibrary.js:287`

## `_cleanup` — arrow, line 2826
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

## `_reconnectTask` — function, line 3040
- **called from:**
- `static/js/cookbookRunning.js:2553`
- `static/js/cookbookRunning.js:2867`
- `static/js/cookbookRunning.js:3010`
- `static/js/cookbookRunning.js:3040`
- `static/js/cookbookRunning.js:3190`
- `static/js/cookbookRunning.js:3288`

## `_trySelectModel` — arrow, line 3679
- **called from:**
- `static/js/cookbookRunning.js:3695`
- `static/js/cookbookRunning.js:3698`

## `_hasLiveTasks` — function, line 3750
- **called from:**
- `static/js/cookbookRunning.js:3750`
- `static/js/cookbookRunning.js:4051`
- `static/js/cookbookRunning.js:4430`

## `_isRunningTabVisible` — function, line 3760
- **called from:**
- `static/js/cookbookRunning.js:3009`
- `static/js/cookbookRunning.js:3043`
- `static/js/cookbookRunning.js:3053`
- `static/js/cookbookRunning.js:3760`
- `static/js/cookbookRunning.js:3823`
- `static/js/cookbookRunning.js:4051`

## `_isCookbookVisible` — function, line 3767
- **called from:**
- `static/js/cookbookRunning.js:3767`
- `static/js/cookbookRunning.js:4078`
- `static/js/cookbookRunning.js:4087`

## `_foregroundChatBusy` — function, line 3777
- **called from:**
- `static/js/cookbook.js:3505`
- `static/js/cookbook.js:3537`
- `static/js/cookbookRunning.js:3777`
- `static/js/cookbookRunning.js:3807`
- `static/js/cookbookRunning.js:3822`
- `static/js/cookbookRunning.js:4078`
- `static/js/cookbookRunning.js:4087`

## `_claimBackgroundLeader` — function, line 3785
- **called from:**
- `static/js/cookbookRunning.js:3785`
- `static/js/cookbookRunning.js:3809`

## `_canBackgroundPoll` — function, line 3806
- **called from:**
- `static/js/cookbookRunning.js:3806`
- `static/js/cookbookRunning.js:4044`
- `static/js/cookbookRunning.js:4055`
- `static/js/cookbookRunning.js:4110`

## `_checkServeReachability` — function, line 3819
- **called from:**
- `static/js/cookbookRunning.js:3819`
- `static/js/cookbookRunning.js:4046`
- `static/js/cookbookRunning.js:4057`

## `_serveTaskFailed` — function, line 3895
- **called from:**
- `static/js/cookbookRunning.js:3895`

## `_setServerDot` — function, line 3900
- **called from:**
- `static/js/cookbookRunning.js:3900`
- `static/js/cookbookRunning.js:3916`
- `static/js/cookbookRunning.js:3924`
- `static/js/cookbookRunning.js:3957`

## `_syncSettingsServerDots` — function, line 3907
- **called from:**
- `static/js/cookbookRunning.js:3907`
- `static/js/cookbookRunning.js:3959`

## `_refreshServerDots` — function, line 3945
- **called from:**
- `static/js/cookbookRunning.js:961`
- `static/js/cookbookRunning.js:3584`
- `static/js/cookbookRunning.js:3887`
- `static/js/cookbookRunning.js:3945`

## `_taskServerKeyForDot` — arrow, line 3949
- **called from:**
- `static/js/cookbookRunning.js:3950`
- `static/js/cookbookRunning.js:3950`

## `_selfHealStaleTasks` — function, line 3970
- **called from:**
- `static/js/cookbook.js:3421`
- `static/js/cookbookRunning.js:3228`
- `static/js/cookbookRunning.js:3970`
- `static/js/cookbookRunning.js:4052`

## `_startBackgroundMonitor` — function, line 4041
- **called from:**
- `static/js/cookbookRunning.js:735`
- `static/js/cookbookRunning.js:943`
- `static/js/cookbookRunning.js:1526`
- `static/js/cookbookRunning.js:4041`
- `static/js/cookbookRunning.js:4430`

## `_stopBackgroundMonitor` — function, line 4061
- **called from:**
- `static/js/cookbookRunning.js:4061`
- `static/js/cookbookRunning.js:4349`

## `_probeEndpointUntilOnline` — function, line 4077
- **called from:**
- `static/js/cookbookRunning.js:2667`
- `static/js/cookbookRunning.js:2685`
- `static/js/cookbookRunning.js:3652`
- `static/js/cookbookRunning.js:3676`
- `static/js/cookbookRunning.js:4077`
- `static/js/cookbookRunning.js:4312`
- `static/js/cookbookRunning.js:4333`

## `_pollBackgroundStatus` — function, line 4109
- **called from:**
- `static/js/cookbookRunning.js:4045`
- `static/js/cookbookRunning.js:4056`
- `static/js/cookbookRunning.js:4109`

## `initRunning` — function, line 4398
- **called from:**
- `static/js/cookbook.js:3641`
- `static/js/cookbookRunning.js:4398`
