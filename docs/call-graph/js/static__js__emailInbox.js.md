# `static/js/emailInbox.js` — definitions & call sites

57 definitions (regex-based, best-effort).
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
- `static/js/emailInbox.js:428`
- `static/js/emailInbox.js:435`
- `static/js/emailInbox.js:453`
- `static/js/emailInbox.js:1318`
- `static/js/emailInbox.js:1328`
- `static/js/emailInbox.js:1351`
- `static/js/emailInbox.js:1403`
- `static/js/emailInbox.js:1404`
- `static/js/emailInbox.js:1406`
- `static/js/emailLibrary/attachments.js:57`
- `static/js/emailLibrary/attachments.js:107`
- `static/js/emailLibrary/attachments.js:165`
- `static/js/emailLibrary/attachments.js:255`
- `static/js/emailLibrary/attachments.js:407`
- `static/js/emailLibrary/index.js:1441`
- `static/js/emailLibrary/index.js:2776`
- `static/js/emailLibrary/index.js:5006`
- `static/js/emailLibrary/index.js:5621`
- `static/js/emailLibrary/index.js:5622`
- `static/js/emailLibrary/index.js:5624`
- `static/js/emailLibrary/index.js:5653`
- `static/js/emailLibrary/index.js:5871`
- `static/js/emailLibrary/menus.js:146`
- `static/js/emailLibrary/menus.js:148`
- `static/js/emailLibrary/menus.js:166`
- `static/js/emailLibrary/menus.js:187`
- `static/js/emailLibrary/menus.js:188`
- `static/js/emailLibrary/menus.js:190`
- `static/js/emailLibrary/menus.js:201`
- `static/js/emailLibrary/menus.js:242`
- `static/js/emailLibrary/menus.js:422`
- `static/js/emailLibrary/menus.js:423`
- `static/js/emailLibrary/menus.js:425`
- `static/js/emailLibrary/menus.js:445`
- `static/js/emailLibrary/menus.js:457`
- `static/js/emailLibrary/menus.js:473`
- `static/js/emailLibrary/menus.js:485`
- `static/js/emailLibrary/menus.js:779`
- `static/js/emailLibrary/menus.js:786`
- `static/js/emailLibrary/menus.js:800`
- `static/js/emailLibrary/menus.js:801`
- `static/js/emailLibrary/menus.js:805`
- `static/js/emailLibrary/reader.js:301`
- `static/js/emailLibrary/reader.js:449`

## `_emailSetupHint` — arrow, line 18
- **called from:**
- `static/js/emailInbox.js:444`

## `_icon` — arrow, line 29
- **called from:**
- `tests/test_lang_icon_null_opts_js.py:33`
- `tests/test_lang_icon_null_opts_js.py:40`
- `static/js/emailInbox.js:1184`
- `static/js/emailLibrary/menus.js:304`
- `static/js/emailLibrary/menus.js:342`
- `static/js/emailLibrary/menus.js:547`
- `static/js/emailLibrary/menus.js:564`
- `static/js/sessions.js:1062`
- `static/js/sessions.js:1066`
- `static/js/sessions.js:1070`
- `static/js/sessions.js:1081`
- `static/js/sessions.js:1088`
- `static/js/sessions.js:1122`
- `static/js/sessions.js:1138`
- `static/js/sessions.js:1181`
- `static/js/sessions.js:1216`

## `_splitEmailAddresses` — function, line 33
- **called from:**
- `static/js/emailInbox.js:33`
- `static/js/emailInbox.js:47`

## `_isMyEmailAddress` — function, line 40
- **called from:**
- `static/js/emailInbox.js:40`
- `static/js/emailInbox.js:47`
- `static/js/emailInbox.js:932`

## `_withoutMyAddresses` — function, line 46
- **called from:**
- `static/js/emailInbox.js:46`
- `static/js/emailInbox.js:933`
- `static/js/emailInbox.js:934`

## `_openCalendarEventFromEmail` — function, line 50
- **called from:**
- `static/js/emailInbox.js:50`
- `static/js/emailInbox.js:656`
- `static/js/emailLibrary/attachments.js:122`
- `static/js/emailLibrary/index.js:181`
- `static/js/emailLibrary/index.js:5584`

## `_openEmailTagFilter` — function, line 59
- **called from:**
- `static/js/emailInbox.js:59`
- `static/js/emailInbox.js:663`

## `_emailTagPillHtml` — function, line 68
- **called from:**
- `static/js/emailInbox.js:68`
- `static/js/emailInbox.js:83`
- `static/js/emailLibrary/index.js:212`
- `static/js/emailLibrary/index.js:227`

## `_emailTagGroupHtml` — function, line 81
- **called from:**
- `static/js/emailInbox.js:81`
- `static/js/emailInbox.js:632`
- `static/js/emailLibrary/index.js:225`
- `static/js/emailLibrary/index.js:5551`

## `_visibleEmailTagsForRender` — function, line 92
- **called from:**
- `static/js/emailInbox.js:92`
- `static/js/emailInbox.js:631`
- `static/js/emailLibrary/index.js:263`
- `static/js/emailLibrary/index.js:276`
- `static/js/emailLibrary/index.js:5547`

## `_clearDoneResponseTagsLocal` — function, line 98
- **called from:**
- `static/js/emailInbox.js:98`
- `static/js/emailInbox.js:136`
- `static/js/emailInbox.js:1392`
- `static/js/emailLibrary/index.js:269`
- `static/js/emailLibrary/index.js:695`
- `static/js/emailLibrary/index.js:5615`
- `static/js/emailLibrary/menus.js:182`
- `static/js/emailLibrary/menus.js:417`
- `static/js/emailLibrary/menus.js:798`

## `_cleanAiReplyText` — function, line 103
- **called from:**
- `static/js/emailInbox.js:103`
- `static/js/emailInbox.js:858`
- `static/js/emailInbox.js:899`

## `init` — function, line 159
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

## `openReplyDraft` — function, line 202
- **called from:**
- `static/js/emailInbox.js:202`

## `_bringEmailReplyDraftToFrontOnMobile` — function, line 213
- **called from:**
- `static/js/emailInbox.js:213`
- `static/js/emailInbox.js:1070`
- `static/js/emailInbox.js:1142`

## `_focusMobileReplyBody` — function, line 230
- **called from:**
- `static/js/emailInbox.js:230`
- `static/js/emailInbox.js:1071`
- `static/js/emailInbox.js:1143`

## `_watchDocOpenToReDockEmail` — function, line 246
- **called from:**
- `static/js/emailInbox.js:199`
- `static/js/emailInbox.js:246`

## `_bindEvents` — function, line 275
- **called from:**
- `static/js/emailInbox.js:161`
- `static/js/emailInbox.js:275`

## `_maybeOpenFromHash` — function, line 309
- **called from:**
- `static/js/emailInbox.js:305`
- `static/js/emailInbox.js:309`

## `_urgencyColor` — function, line 322
- **called from:**
- `static/js/emailInbox.js:322`
- `static/js/emailInbox.js:367`

## `_refreshUnreadCount` — function, line 328
- **called from:**
- `static/js/emailInbox.js:328`

## `markInboxAsSeen` — function, line 380
- **called from:**
- `static/js/emailInbox.js:285`
- `static/js/emailInbox.js:380`

## `loadEmails` — function, line 398
- **called from:**
- `static/js/emailInbox.js:398`
- `static/js/emailInbox.js:568`
- `static/js/emailInbox.js:575`

## `applyListData` — arrow, line 416
- **called from:**
- `static/js/emailInbox.js:431`
- `static/js/emailInbox.js:438`

## `loadFolders` — function, line 451
- **called from:**
- `static/js/emailInbox.js:451`

## `sortedFolders` — function, line 464
- **called from:**
- `static/js/emailInbox.js:464`
- `static/js/emailInbox.js:507`
- `static/js/emailLibrary/index.js:3554`

## `roleOf` — arrow, line 465
- **called from:**
- `static/js/emailInbox.js:480`

## `folderDisplayName` — function, line 490
- **called from:**
- `static/js/emailInbox.js:490`
- `static/js/emailInbox.js:512`
- `static/js/emailInbox.js:527`
- `static/js/emailLibrary/index.js:3558`
- `static/js/emailLibrary/index.js:3565`
- `static/js/emailLibrary/index.js:4031`
- `static/js/emailLibrary/index.js:4751`
- `static/js/emailLibrary/index.js:4765`
- `static/js/emailLibrary/index.js:5716`

## `_populateFolderSelect` — function, line 505
- **called from:**
- `static/js/emailInbox.js:458`
- `static/js/emailInbox.js:505`

## `_renderList` — function, line 533
- **called from:**
- `static/js/emailInbox.js:164`
- `static/js/emailInbox.js:421`
- `static/js/emailInbox.js:533`
- `static/js/emailInbox.js:1320`
- `static/js/emailInbox.js:1332`
- `static/js/emailInbox.js:1354`
- `static/js/tasks.js:682`
- `static/js/tasks.js:692`
- `static/js/tasks.js:700`
- `static/js/tasks.js:707`
- `static/js/tasks.js:810`
- `static/js/tasks.js:860`
- `static/js/tasks.js:3112`
- `static/js/tasks.js:3115`
- `static/js/tasks.js:3136`
- `static/js/tasks.js:3142`
- `static/js/tasks.js:3161`
- `static/js/tasks.js:3282`

## `_setSenderFilter` — function, line 564
- **called from:**
- `static/js/emailInbox.js:564`
- `static/js/emailInbox.js:681`

## `_clearSenderFilter` — function, line 571
- **called from:**
- `static/js/emailInbox.js:542`
- `static/js/emailInbox.js:571`

## `_createEmailItem` — function, line 578
- **called from:**
- `static/js/emailInbox.js:555`
- `static/js/emailInbox.js:578`

## `_openEmail` — function, line 772
- **called from:**
- `static/js/emailInbox.js:193`
- `static/js/emailInbox.js:207`
- `static/js/emailInbox.js:705`
- `static/js/emailInbox.js:772`
- `static/js/emailInbox.js:851`
- `static/js/emailInbox.js:1173`

## `isCurrentOpen` — arrow, line 783
- **called from:**
- `static/js/emailInbox.js:818`
- `static/js/emailInbox.js:897`
- `static/js/emailInbox.js:910`
- `static/js/emailInbox.js:918`
- `static/js/emailInbox.js:1059`
- `static/js/emailInbox.js:1061`
- `static/js/emailInbox.js:1064`
- `static/js/emailInbox.js:1068`
- `static/js/emailInbox.js:1074`
- `static/js/emailInbox.js:1084`
- `static/js/emailInbox.js:1102`
- `static/js/emailInbox.js:1105`
- `static/js/emailInbox.js:1107`
- `static/js/emailInbox.js:1110`
- `static/js/emailInbox.js:1115`
- `static/js/emailInbox.js:1125`
- `static/js/emailInbox.js:1130`
- `static/js/emailInbox.js:1137`
- `static/js/emailInbox.js:1140`
- `static/js/emailInbox.js:1150`
- `static/js/emailLibrary/index.js:6019`
- `static/js/emailLibrary/index.js:6035`
- `static/js/emailLibrary/index.js:6218`

## `_fallback` — arrow, line 827
- **called from:**
- `src/research_handler.py:153`
- `src/research_handler.py:187`
- `static/js/emailInbox.js:836`
- `static/js/emailInbox.js:837`
- `static/js/emailInbox.js:838`
- `static/js/emailInbox.js:839`
- `static/js/emailInbox.js:840`
- `static/js/emailInbox.js:841`
- `static/js/emailInbox.js:842`

## `createReplyDoc` — arrow, line 1091
- **called from:**
- `static/js/emailInbox.js:1101`
- `static/js/emailInbox.js:1109`

## `_showEmailMenu` — function, line 1166
- **called from:**
- `static/js/emailInbox.js:1166`

## `_showRemindSubmenu` — function, line 1204
- **called from:**
- `static/js/emailInbox.js:1188`
- `static/js/emailInbox.js:1204`

## `pad` — arrow, line 1248
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

## `_cleanup` — arrow, line 1256
- **called from:**
- `scripts/diffusion_server.py:439`
- `scripts/diffusion_server.py:443`
- `scripts/diffusion_server.py:457`
- `scripts/diffusion_server.py:468`
- `scripts/diffusion_server.py:488`
- `scripts/diffusion_server.py:504`
- `scripts/diffusion_server.py:635`
- `src/agent_runtime/effect_adapters.py:353`
- `tests/test_process_lifecycle.py:248`
- `tests/test_process_lifecycle.py:269`
- `tests/test_process_lifecycle.py:295`
- `static/js/compare/index.js:1524`
- `static/js/cookbookRunning.js:2840`
- `static/js/cookbookRunning.js:2874`
- `static/js/cookbookRunning.js:2880`
- `static/js/document.js:13672`
- `static/js/document.js:14367`
- `static/js/document.js:14439`
- `static/js/emailInbox.js:1261`
- `static/js/emailInbox.js:1269`
- `static/js/emailInbox.js:1274`

## `_onKey` — arrow, line 1261
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_onDocClick` — arrow, line 1269
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_createReplyReminder` — function, line 1284
- **called from:**
- `static/js/emailInbox.js:1235`
- `static/js/emailInbox.js:1272`
- `static/js/emailInbox.js:1284`

## `pad` — arrow, line 1285
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

## `_archiveEmail` — function, line 1316
- **called from:**
- `static/js/emailInbox.js:751`
- `static/js/emailInbox.js:1176`
- `static/js/emailInbox.js:1316`

## `_spamEmail` — function, line 1326
- **called from:**
- `static/js/emailInbox.js:1175`
- `static/js/emailInbox.js:1326`

## `_deleteEmail` — function, line 1342
- **called from:**
- `static/js/emailInbox.js:1177`
- `static/js/emailInbox.js:1342`

## `_showEmailDeleteOverlay` — function, line 1361
- **called from:**
- `static/js/emailInbox.js:1348`
- `static/js/emailInbox.js:1361`
- `static/js/emailLibrary/index.js:1001`
- `static/js/emailLibrary/index.js:1037`
- `static/js/emailLibrary/menus.js:251`
- `static/js/emailLibrary/menus.js:277`
- `static/js/emailLibrary/menus.js:517`
- `static/js/emailLibrary/menus.js:768`

## `remove` — method?, line 1376
- **called from:**
- `core/auth.py:593`
- `mcp_servers/memory_server.py:218`
- `mcp_servers/memory_server.py:246`
- `routes/admin_wipe/admin_wipe_routes.py:51`
- `routes/admin_wipe/admin_wipe_routes.py:121`
- `routes/editor_agent_routes.py:1388`
- `routes/embedding_routes.py:339`
- `routes/memory/memory_routes.py:550`
- `routes/memory/memory_routes.py:572`
- `routes/personal_routes.py:426`
- `scripts/audit_c5_benchmark_evidence.py:184`
- `scripts/audit_c5_benchmark_evidence.py:241`
- `scripts/sanitize_trace_artifacts.py:296`
- `scripts/select_sft_expansion_seeds.py:128`
- `scripts/test_clean_tool_loop.py:30`
- `services/memory/service.py:125`
- `services/memory/skills.py:604`
- `src/agent_trace.py:367`
- `src/ai_interaction.py:530`
- `src/api_key_manager.py:100`
- `src/clean_agent_preview.py:2660`
- `src/clean_agent_preview.py:3912`
- `src/clean_agent_preview.py:3923`
- `src/clean_agent_preview.py:3940`
- `src/clean_agent_preview.py:3945`
- `src/clean_agent_preview.py:3968`
- `src/clean_agent_preview.py:3973`
- `src/clean_agent_preview.py:3981`
- `src/clean_agent_preview.py:3987`
- `src/clean_agent_preview.py:3998`
- `src/memory_provider.py:251`
- `src/personal_docs.py:322`
- `src/readiness.py:50`
- `src/tools/image.py:188`
- `src/upload_handler.py:719`
- `tests/test_cleanup_transcript_preservation.py:152`
- `tests/test_cleanup_transcript_preservation.py:214`
- `tests/test_cleanup_transcript_preservation.py:297`
- `tests/test_cleanup_transcript_preservation.py:366`
- `tests/test_email_bulk_delete_safety.py:49`
- `tests/test_embedding_lanes_memory.py:165`
- `tests/test_exact_approval_ungranted_process.py:146`
- `tests/test_history_display_model_hydration.py:117`
- `tests/test_memory_store_unreadable_no_wipe.py:94`
- `tests/test_path_confinement_boundary.py:160`
- `tests/test_replace_messages_upload_reservations.py:130`
- `tests/test_replace_messages_upload_reservations.py:172`
- `tests/test_upload_handler_atomicity.py:425`
- `tests/test_web_tools_pwd_optional.py:35`
- `static/app.js:354`
- `static/app.js:395`
- `static/app.js:398`
- `static/app.js:426`
- `static/app.js:437`
- `static/app.js:463`
- `static/app.js:466`
- `static/app.js:553`
- `static/app.js:568`
- `static/app.js:603`
- `static/app.js:615`
- … +1518 more (grep the name in repo)

## `_toggleDone` — function, line 1386
- **called from:**
- `static/js/emailInbox.js:1386`

## `_createEmailChat` — function, line 1413
- **called from:**
- `static/js/emailInbox.js:1082`
- `static/js/emailInbox.js:1106`
- `static/js/emailInbox.js:1413`
- `static/js/emailInbox.js:1478`
- `static/js/emailInbox.js:1497`

## `_composeNew` — function, line 1470
- **called from:**
- `static/js/emailInbox.js:191`
- `static/js/emailInbox.js:294`
- `static/js/emailInbox.js:1470`

## `createComposeDoc` — arrow, line 1484
- **called from:**
- `static/js/emailInbox.js:1494`
- `static/js/emailInbox.js:1498`

## `_esc` — function, line 1521
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

## `_senderColor` — function, line 1527
- **called from:**
- `static/js/emailInbox.js:600`
- `static/js/emailInbox.js:1527`
- `static/js/emailLibrary/bodyRender.js:522`
- `static/js/emailLibrary/index.js:647`
- `static/js/emailLibrary/index.js:5496`
- `static/js/emailLibrary/utils.js:158`
