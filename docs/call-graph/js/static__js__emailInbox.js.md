# `static/js/emailInbox.js` — definitions & call sites

55 definitions (regex-based, best-effort).
**Exports:** `folderDisplayName`, `init`, `loadEmails`, `markInboxAsSeen`, `openReplyDraft`, `sortedFolders`

## `_acct` — arrow, line 16
- **called from:**
- `tests/test_service_health_email.py:26`
- `tests/test_service_health_email.py:26`
- `tests/test_service_health_email.py:36`
- `tests/test_service_health_email.py:36`
- `tests/test_service_health_email.py:41`
- `tests/test_service_health_email.py:46`
- `tests/test_service_health_email.py:51`
- `tests/test_service_health_email.py:58`
- `tests/test_service_health_email.py:73`
- `tests/test_service_health_email.py:73`
- `static/js/emailInbox.js:415`
- `static/js/emailInbox.js:422`
- `static/js/emailInbox.js:440`
- `static/js/emailInbox.js:1254`
- `static/js/emailInbox.js:1271`
- `static/js/emailInbox.js:1323`
- `static/js/emailInbox.js:1324`
- `static/js/emailInbox.js:1326`
- `static/js/emailLibrary.js:1199`
- `static/js/emailLibrary.js:1313`
- `static/js/emailLibrary.js:2839`
- `static/js/emailLibrary.js:4662`
- `static/js/emailLibrary.js:5189`
- `static/js/emailLibrary.js:5190`
- `static/js/emailLibrary.js:5192`
- `static/js/emailLibrary.js:5369`
- `static/js/emailLibrary.js:6599`
- `static/js/emailLibrary.js:6658`
- `static/js/emailLibrary.js:6727`
- `static/js/emailLibrary.js:6866`
- `static/js/emailLibrary.js:7175`
- `static/js/emailLibrary.js:7320`
- `static/js/emailLibrary.js:7742`
- `static/js/emailLibrary.js:7744`
- `static/js/emailLibrary.js:7762`
- `static/js/emailLibrary.js:7783`
- `static/js/emailLibrary.js:7784`
- `static/js/emailLibrary.js:7786`
- `static/js/emailLibrary.js:7797`
- `static/js/emailLibrary.js:7838`
- `static/js/emailLibrary.js:7850`
- `static/js/emailLibrary.js:7875`
- `static/js/emailLibrary.js:7993`
- `static/js/emailLibrary.js:7994`
- `static/js/emailLibrary.js:7996`
- `static/js/emailLibrary.js:8016`
- `static/js/emailLibrary.js:8028`
- `static/js/emailLibrary.js:8044`
- `static/js/emailLibrary.js:8056`
- `static/js/emailLibrary.js:8091`
- `static/js/emailLibrary.js:8270`
- `static/js/emailLibrary.js:8272`
- `static/js/emailLibrary.js:8284`
- `static/js/emailLibrary.js:8285`
- `static/js/emailLibrary.js:8289`

## `_emailSetupHint` — arrow, line 18
- **called from:**
- `static/js/emailInbox.js:431`

## `_icon` — arrow, line 28
- **called from:**
- `tests/test_lang_icon_null_opts_js.py:33`
- `tests/test_lang_icon_null_opts_js.py:40`
- `static/js/emailInbox.js:1120`
- `static/js/emailLibrary.js:7898`
- `static/js/emailLibrary.js:7919`
- `static/js/emailLibrary.js:8109`
- `static/js/emailLibrary.js:8126`
- `static/js/sessions.js:741`
- `static/js/sessions.js:745`
- `static/js/sessions.js:749`
- `static/js/sessions.js:760`
- `static/js/sessions.js:767`
- `static/js/sessions.js:801`
- `static/js/sessions.js:817`
- `static/js/sessions.js:859`
- `static/js/sessions.js:894`

## `_splitEmailAddresses` — function, line 32
- **called from:**
- `static/js/emailInbox.js:32`
- `static/js/emailInbox.js:46`

## `_isMyEmailAddress` — function, line 39
- **called from:**
- `static/js/emailInbox.js:39`
- `static/js/emailInbox.js:46`
- `static/js/emailInbox.js:897`

## `_withoutMyAddresses` — function, line 45
- **called from:**
- `static/js/emailInbox.js:45`
- `static/js/emailInbox.js:898`
- `static/js/emailInbox.js:899`

## `_openCalendarEventFromEmail` — function, line 49
- **called from:**
- `static/js/emailInbox.js:49`
- `static/js/emailInbox.js:639`
- `static/js/emailLibrary.js:498`
- `static/js/emailLibrary.js:5152`

## `_openEmailTagFilter` — function, line 58
- **called from:**
- `static/js/emailInbox.js:58`
- `static/js/emailInbox.js:646`

## `_emailTagPillHtml` — function, line 67
- **called from:**
- `static/js/emailInbox.js:67`
- `static/js/emailInbox.js:82`
- `static/js/emailLibrary.js:529`
- `static/js/emailLibrary.js:544`

## `_emailTagGroupHtml` — function, line 80
- **called from:**
- `static/js/emailInbox.js:80`
- `static/js/emailInbox.js:615`
- `static/js/emailLibrary.js:542`
- `static/js/emailLibrary.js:5138`

## `_visibleEmailTagsForRender` — function, line 90
- **called from:**
- `static/js/emailInbox.js:90`
- `static/js/emailInbox.js:614`
- `static/js/emailLibrary.js:554`
- `static/js/emailLibrary.js:5134`

## `_clearDoneResponseTagsLocal` — function, line 96
- **called from:**
- `static/js/emailInbox.js:96`
- `static/js/emailInbox.js:134`
- `static/js/emailInbox.js:1312`
- `static/js/emailLibrary.js:560`
- `static/js/emailLibrary.js:918`
- `static/js/emailLibrary.js:5183`
- `static/js/emailLibrary.js:7778`
- `static/js/emailLibrary.js:7988`
- `static/js/emailLibrary.js:8282`

## `_cleanAiReplyText` — function, line 101
- **called from:**
- `static/js/emailInbox.js:101`
- `static/js/emailInbox.js:829`
- `static/js/emailInbox.js:863`

## `init` — function, line 157
- **called from:**
- `static/app.js:3724`
- `static/app.js:3725`
- `static/app.js:3726`
- `static/app.js:3727`
- `static/app.js:3728`
- `static/app.js:3729`
- `static/app.js:3731`
- `static/app.js:3734`
- `static/app.js:3736`
- `static/app.js:3739`
- `static/app.js:3748`
- `static/app.js:4370`
- `static/app.js:4371`
- `static/js/a11y.js:121`
- `static/js/a11y.js:163`
- `static/js/censor.js:44`
- `static/js/chat.js:1166`
- `static/js/chat.js:1171`
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

## `openReplyDraft` — function, line 199
- **called from:**
- `static/js/emailInbox.js:199`

## `_bringEmailReplyDraftToFrontOnMobile` — function, line 210
- **called from:**
- `static/js/emailInbox.js:210`
- `static/js/emailInbox.js:1021`
- `static/js/emailInbox.js:1082`

## `_watchDocOpenToReDockEmail` — function, line 233
- **called from:**
- `static/js/emailInbox.js:196`
- `static/js/emailInbox.js:233`

## `_bindEvents` — function, line 262
- **called from:**
- `static/js/emailInbox.js:159`
- `static/js/emailInbox.js:262`

## `_maybeOpenFromHash` — function, line 296
- **called from:**
- `static/js/emailInbox.js:292`
- `static/js/emailInbox.js:296`

## `_urgencyColor` — function, line 309
- **called from:**
- `static/js/emailInbox.js:309`
- `static/js/emailInbox.js:354`

## `_refreshUnreadCount` — function, line 315
- **called from:**
- `static/js/emailInbox.js:315`

## `markInboxAsSeen` — function, line 367
- **called from:**
- `static/js/emailInbox.js:272`
- `static/js/emailInbox.js:367`

## `loadEmails` — function, line 385
- **called from:**
- `static/js/emailInbox.js:385`
- `static/js/emailInbox.js:551`
- `static/js/emailInbox.js:558`

## `applyListData` — arrow, line 403
- **called from:**
- `static/js/emailInbox.js:418`
- `static/js/emailInbox.js:425`

## `loadFolders` — function, line 438
- **called from:**
- `static/js/emailInbox.js:438`

## `sortedFolders` — function, line 451
- **called from:**
- `static/js/emailInbox.js:451`
- `static/js/emailInbox.js:490`
- `static/js/emailLibrary.js:3497`

## `roleOf` — arrow, line 452
- **called from:**
- `static/js/emailInbox.js:467`

## `folderDisplayName` — function, line 474
- **called from:**
- `static/js/emailInbox.js:474`
- `static/js/emailInbox.js:495`
- `static/js/emailInbox.js:510`
- `static/js/emailLibrary.js:3501`
- `static/js/emailLibrary.js:3514`
- `static/js/emailLibrary.js:5249`

## `_populateFolderSelect` — function, line 488
- **called from:**
- `static/js/emailInbox.js:445`
- `static/js/emailInbox.js:488`

## `_renderList` — function, line 516
- **called from:**
- `static/js/emailInbox.js:162`
- `static/js/emailInbox.js:408`
- `static/js/emailInbox.js:516`
- `static/js/emailInbox.js:1256`
- `static/js/emailInbox.js:1274`
- `static/js/tasks.js:675`
- `static/js/tasks.js:683`
- `static/js/tasks.js:690`
- `static/js/tasks.js:781`
- `static/js/tasks.js:801`
- `static/js/tasks.js:2908`
- `static/js/tasks.js:2911`
- `static/js/tasks.js:2923`
- `static/js/tasks.js:2929`
- `static/js/tasks.js:2947`
- `static/js/tasks.js:3060`

## `_setSenderFilter` — function, line 547
- **called from:**
- `static/js/emailInbox.js:547`
- `static/js/emailInbox.js:664`

## `_clearSenderFilter` — function, line 554
- **called from:**
- `static/js/emailInbox.js:525`
- `static/js/emailInbox.js:554`

## `_createEmailItem` — function, line 561
- **called from:**
- `static/js/emailInbox.js:538`
- `static/js/emailInbox.js:561`

## `_openEmail` — function, line 755
- **called from:**
- `static/js/emailInbox.js:191`
- `static/js/emailInbox.js:204`
- `static/js/emailInbox.js:688`
- `static/js/emailInbox.js:755`
- `static/js/emailInbox.js:1110`

## `isCurrentOpen` — arrow, line 766
- **called from:**
- `static/js/emailInbox.js:801`
- `static/js/emailInbox.js:861`
- `static/js/emailInbox.js:875`
- `static/js/emailInbox.js:883`
- `static/js/emailInbox.js:1010`
- `static/js/emailInbox.js:1012`
- `static/js/emailInbox.js:1015`
- `static/js/emailInbox.js:1019`
- `static/js/emailInbox.js:1023`
- `static/js/emailInbox.js:1025`
- `static/js/emailInbox.js:1043`
- `static/js/emailInbox.js:1046`
- `static/js/emailInbox.js:1048`
- `static/js/emailInbox.js:1051`
- `static/js/emailInbox.js:1056`
- `static/js/emailInbox.js:1066`
- `static/js/emailInbox.js:1071`
- `static/js/emailInbox.js:1080`
- `static/js/emailInbox.js:1087`
- `static/js/emailLibrary.js:5511`
- `static/js/emailLibrary.js:5524`
- `static/js/emailLibrary.js:5707`

## `_fallback` — arrow, line 809
- **called from:**
- `src/research_handler.py:137`
- `src/research_handler.py:171`
- `static/js/emailInbox.js:818`
- `static/js/emailInbox.js:819`
- `static/js/emailInbox.js:820`
- `static/js/emailInbox.js:821`
- `static/js/emailInbox.js:822`
- `static/js/emailInbox.js:823`
- `static/js/emailInbox.js:824`

## `createReplyDoc` — arrow, line 1032
- **called from:**
- `static/js/emailInbox.js:1042`
- `static/js/emailInbox.js:1050`

## `_showEmailMenu` — function, line 1103
- **called from:**
- `static/js/emailInbox.js:1103`

## `_showRemindSubmenu` — function, line 1140
- **called from:**
- `static/js/emailInbox.js:1124`
- `static/js/emailInbox.js:1140`

## `pad` — arrow, line 1184
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

## `_cleanup` — arrow, line 1192
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

## `_onKey` — arrow, line 1197
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_onDocClick` — arrow, line 1205
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_createReplyReminder` — function, line 1220
- **called from:**
- `static/js/emailInbox.js:1171`
- `static/js/emailInbox.js:1208`
- `static/js/emailInbox.js:1220`

## `pad` — arrow, line 1221
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

## `_archiveEmail` — function, line 1252
- **called from:**
- `static/js/emailInbox.js:734`
- `static/js/emailInbox.js:1112`
- `static/js/emailInbox.js:1252`

## `_deleteEmail` — function, line 1262
- **called from:**
- `static/js/emailInbox.js:1113`
- `static/js/emailInbox.js:1262`

## `_showEmailDeleteOverlay` — function, line 1281
- **called from:**
- `static/js/emailInbox.js:1268`
- `static/js/emailInbox.js:1281`
- `static/js/emailLibrary.js:1191`
- `static/js/emailLibrary.js:1226`
- `static/js/emailLibrary.js:7847`
- `static/js/emailLibrary.js:7872`
- `static/js/emailLibrary.js:8088`
- `static/js/emailLibrary.js:8259`

## `remove` — method?, line 1296
- **called from:**
- `core/auth.py:542`
- `mcp_servers/memory_server.py:218`
- `mcp_servers/memory_server.py:246`
- `routes/admin_wipe/admin_wipe_routes.py:51`
- `routes/admin_wipe/admin_wipe_routes.py:121`
- `routes/embedding_routes.py:339`
- `routes/gallery/gallery_routes.py:2019`
- `routes/memory/memory_routes.py:543`
- `routes/memory/memory_routes.py:565`
- `routes/personal_routes.py:440`
- `services/memory/service.py:125`
- `services/memory/skills.py:517`
- `src/agent_tools/filesystem_tools.py:395`
- `src/ai_interaction.py:477`
- `src/api_key_manager.py:100`
- `src/memory_provider.py:251`
- `src/personal_docs.py:318`
- `src/readiness.py:42`
- `src/upload_handler.py:660`
- `tests/test_embedding_lanes_memory.py:165`
- `tests/test_history_display_model_hydration.py:117`
- `tests/test_memory_store_unreadable_no_wipe.py:94`
- `tests/test_replace_messages_upload_reservations.py:130`
- `tests/test_replace_messages_upload_reservations.py:172`
- `tests/test_upload_handler_atomicity.py:425`
- `static/app.js:337`
- `static/app.js:377`
- `static/app.js:380`
- `static/app.js:398`
- `static/app.js:409`
- `static/app.js:412`
- `static/app.js:490`
- `static/app.js:504`
- `static/app.js:518`
- `static/app.js:543`
- `static/app.js:570`
- `static/app.js:582`
- `static/app.js:685`
- `static/app.js:697`
- `static/app.js:720`
- `static/app.js:797`
- `static/app.js:803`
- `static/app.js:806`
- `static/app.js:812`
- `static/app.js:813`
- `static/app.js:817`
- `static/app.js:818`
- `static/app.js:853`
- `static/app.js:865`
- `static/app.js:897`
- `static/app.js:1143`
- `static/app.js:1157`
- `static/app.js:1292`
- `static/app.js:1564`
- `static/app.js:1689`
- `static/app.js:1987`
- `static/app.js:2008`
- `static/app.js:2165`
- `static/app.js:2166`
- `static/app.js:2192`
- … +1230 more (grep the name in repo)

## `_toggleDone` — function, line 1306
- **called from:**
- `static/js/emailInbox.js:1306`

## `_createEmailChat` — function, line 1333
- **called from:**
- `static/js/emailInbox.js:1024`
- `static/js/emailInbox.js:1047`
- `static/js/emailInbox.js:1333`
- `static/js/emailInbox.js:1398`
- `static/js/emailInbox.js:1417`

## `_composeNew` — function, line 1390
- **called from:**
- `static/js/emailInbox.js:189`
- `static/js/emailInbox.js:281`
- `static/js/emailInbox.js:1390`

## `createComposeDoc` — arrow, line 1404
- **called from:**
- `static/js/emailInbox.js:1414`
- `static/js/emailInbox.js:1418`

## `_esc` — function, line 1441
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
- `static/js/chat.js:4698`
- `static/js/chat.js:4698`
- `static/js/cookbookServe.js:4003`
- `static/js/cookbookServe.js:4005`
- `static/js/document.js:313`
- `static/js/document.js:314`
- `static/js/document.js:8382`
- `static/js/document.js:8966`
- `static/js/documentLibrary.js:70`
- `static/js/documentLibrary.js:86`
- `static/js/documentLibrary.js:584`
- `static/js/documentLibrary.js:588`
- `static/js/documentLibrary.js:590`
- `static/js/documentLibrary.js:1997`
- `static/js/documentLibrary.js:2002`
- `static/js/documentLibrary.js:2170`
- `static/js/documentLibrary.js:2526`
- `static/js/documentLibrary.js:2570`
- `static/js/documentLibrary.js:2607`
- `static/js/documentLibrary.js:2796`
- `static/js/documentLibrary.js:2911`
- `static/js/documentLibrary.js:2952`
- `static/js/documentLibrary.js:2965`
- `static/js/documentLibrary.js:3119`
- `static/js/emailInbox.js:75`
- `static/js/emailInbox.js:75`
- `static/js/emailInbox.js:75`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:77`
- … +189 more (grep the name in repo)

## `_senderColor` — function, line 1447
- **called from:**
- `static/js/emailInbox.js:583`
- `static/js/emailInbox.js:1447`
- `static/js/emailLibrary.js:899`
- `static/js/emailLibrary.js:5093`
- `static/js/emailLibrary.js:6163`
- `static/js/emailLibrary/utils.js:150`
