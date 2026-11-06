# `static/js/emailLibrary/index.js` — definitions & call sites

252 definitions (regex-based, best-effort).
**Exports:** `_acct`, `_animateEmailCardRemoval`, `_clearDoneResponseTagsLocal`, `_emailMutationQuery`, `_emailReaderSkeletonHtml`, `_exportSelectedAttachments`, `_exportSelectedEmailPdf`, `_exportSelectedEmails`, `_findSiblingEmailCard`, `_fitEmailDropdown`, `_libCacheWriteBack`, `_loadAccounts`, `_loadEmails`, `_loadEmailsFresh`, `_loadFolders`, `_loadedEmailsHaveVisibleTags`, `_makeDraggable`, `_markEmailReaderActive`, `_maybeAutoTranslateEmail`, `_normalizeEmailStateFlags`, `_notifyNoLoadedEmailTags`, `_openCalendarEventFromEmail`, `_openTasksForEmailTags`, `_prepareEmailWindowForDocument`, `_publishActiveAccount`, `_recipientChipHtml`, `_recipientMetaToggleHtml`, `_refreshUnreadBadge`, `_renderAccountsStrip`, `_renderGrid`, `_requireSuccessfulEmailMutation`, `_resetEmailListForFreshLoad`, `_setSummaryCollapsedPref`, `_showEmailDeleteOverlay`, `_showEmailReaderLoadError`, `_snapEmailModalToLeftSidebar`, `_splitRecipientList`, `_stampReaderContext`, `_summaryCollapsedPref`, `_syncEmailDoneState`, `_syncEmailReadState`, `_toggleCardPreview`, `_translateEmail`, `_wireMetaToggle`, `_wireReaderActionOverflow`, `_wireRecipientChips`, `closeEmailLibrary`, `initEmailLibrary`, `isOpen`, `mountEmailSettings`, `openEmailFromTool`, `openEmailLibrary`, `openEmailLibrarySettings`, `prewarmEmailLibrary`, `prewarmUnreadEmails`, `refreshEmailLibrary`

## `_hasActiveEmailSearchResults` — function, line 85
- **called from:**
- `static/js/emailLibrary/index.js:85`
- `static/js/emailLibrary/index.js:5457`
- `static/js/emailLibrary/index.js:5884`

## `_normalizeEmailStateFlags` — function, line 92
- **called from:**
- `static/js/emailLibrary/index.js:92`
- `static/js/emailLibrary/index.js:5449`
- `static/js/emailLibrary/index.js:5878`
- `static/js/emailLibrary/index.js:6022`
- `static/js/emailLibrary/reader.js:308`
- `static/js/emailLibrary/reader.js:455`

## `_isEmailTypingTarget` — function, line 127
- **called from:**
- `static/js/emailLibrary/index.js:127`
- `static/js/emailLibrary/index.js:576`
- `static/js/emailLibrary/index.js:2987`
- `static/js/emailLibrary/index.js:3026`

## `_selectEmailReaderContents` — function, line 136
- **called from:**
- `static/js/emailLibrary/index.js:136`
- `static/js/emailLibrary/index.js:587`
- `static/js/emailLibrary/index.js:2978`

## `_markEmailReaderActive` — function, line 148
- **called from:**
- `static/js/emailLibrary/index.js:148`
- `static/js/emailLibrary/index.js:178`
- `static/js/emailLibrary/index.js:5998`
- `static/js/emailLibrary/index.js:6097`
- `static/js/emailLibrary/reader.js:293`
- `static/js/emailLibrary/reader.js:348`
- `static/js/emailLibrary/reader.js:479`
- `static/js/emailLibrary/reader.js:506`

## `_emailReaderLoadErrorHtml` — function, line 157
- **called from:**
- `static/js/emailLibrary/index.js:157`
- `static/js/emailLibrary/index.js:171`

## `_showEmailReaderLoadError` — function, line 166
- **called from:**
- `static/js/emailLibrary/index.js:166`
- `static/js/emailLibrary/index.js:6001`
- `static/js/emailLibrary/reader.js:288`

## `_openCalendarEventFromEmail` — function, line 181
- **called from:**
- `static/js/emailInbox.js:50`
- `static/js/emailInbox.js:656`
- `static/js/emailLibrary/attachments.js:122`
- `static/js/emailLibrary/index.js:181`
- `static/js/emailLibrary/index.js:5584`

## `_applyTagFilterFromPill` — function, line 190
- **called from:**
- `static/js/emailLibrary/index.js:190`
- `static/js/emailLibrary/index.js:209`
- `static/js/emailLibrary/index.js:5585`

## `_emailTagPillHtml` — function, line 212
- **called from:**
- `static/js/emailInbox.js:68`
- `static/js/emailInbox.js:83`
- `static/js/emailLibrary/index.js:212`
- `static/js/emailLibrary/index.js:227`

## `_emailTagGroupHtml` — function, line 225
- **called from:**
- `static/js/emailInbox.js:81`
- `static/js/emailInbox.js:632`
- `static/js/emailLibrary/index.js:225`
- `static/js/emailLibrary/index.js:5551`

## `_fitEmailCardTags` — function, line 242
- **called from:**
- `static/js/emailLibrary/index.js:242`
- `static/js/emailLibrary/index.js:257`
- `static/js/emailLibrary/index.js:5582`
- `static/js/emailLibrary/index.js:5677`

## `_visibleEmailTagsForRender` — function, line 263
- **called from:**
- `static/js/emailInbox.js:92`
- `static/js/emailInbox.js:631`
- `static/js/emailLibrary/index.js:263`
- `static/js/emailLibrary/index.js:276`
- `static/js/emailLibrary/index.js:5547`

## `_clearDoneResponseTagsLocal` — function, line 269
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

## `_loadedEmailsHaveVisibleTags` — function, line 274
- **called from:**
- `static/js/emailLibrary/index.js:274`
- `static/js/emailLibrary/settingsPage.js:640`

## `_openTasksForEmailTags` — function, line 280
- **called from:**
- `static/js/emailLibrary/index.js:280`

## `_notifyNoLoadedEmailTags` — function, line 292
- **called from:**
- `static/js/emailLibrary/index.js:292`
- `static/js/emailLibrary/settingsPage.js:640`

## `_stampReaderContext` — function, line 307
- **called from:**
- `static/js/emailLibrary/index.js:307`
- `static/js/emailLibrary/index.js:6036`
- `static/js/emailLibrary/reader.js:312`
- `static/js/emailLibrary/reader.js:478`

## `_getActiveEmailContext` — function, line 322
- **called from:**
- `static/js/emailLibrary/index.js:322`

## `_decodeAttrValue` — function, line 352
- **called from:**
- `static/js/emailLibrary/index.js:352`
- `static/js/emailLibrary/index.js:463`
- `static/js/emailLibrary/index.js:532`
- `static/js/emailLibrary/index.js:564`

## `_emailAddressFromRecipientText` — function, line 358
- **called from:**
- `static/js/emailLibrary/index.js:358`
- `static/js/emailLibrary/index.js:444`
- `static/js/emailLibrary/index.js:464`
- `static/js/emailLibrary/index.js:532`

## `_splitRecipientList` — function, line 366
- **called from:**
- `static/js/emailLibrary/index.js:366`
- `static/js/emailLibrary/index.js:434`
- `static/js/emailLibrary/index.js:6061`
- `static/js/emailLibrary/reader.js:315`
- `static/js/emailLibrary/reader.js:465`

## `_copyTextToClipboard` — function, line 391
- **called from:**
- `static/js/emailLibrary/index.js:391`
- `static/js/emailLibrary/index.js:500`
- `static/js/emailLibrary/index.js:535`

## `_wireMetaToggle` — function, line 417
- **called from:**
- `static/js/emailLibrary/index.js:417`
- `static/js/emailLibrary/index.js:6129`
- `static/js/emailLibrary/reader.js:374`
- `static/js/emailLibrary/reader.js:532`

## `_recipientMetaToggleHtml` — function, line 433
- **called from:**
- `static/js/emailLibrary/index.js:433`
- `static/js/emailLibrary/index.js:6077`
- `static/js/emailLibrary/reader.js:328`
- `static/js/emailLibrary/reader.js:486`

## `_recipientChipHtml` — function, line 442
- **called from:**
- `static/js/emailLibrary/index.js:442`
- `static/js/emailLibrary/index.js:6065`
- `static/js/emailLibrary/index.js:6070`
- `static/js/emailLibrary/reader.js:317`
- `static/js/emailLibrary/reader.js:320`
- `static/js/emailLibrary/reader.js:468`
- `static/js/emailLibrary/reader.js:471`

## `_closeRecipientChipPopover` — function, line 451
- **called from:**
- `static/js/emailLibrary/index.js:451`
- `static/js/emailLibrary/index.js:462`
- `static/js/emailLibrary/index.js:512`
- `static/js/emailLibrary/index.js:516`

## `_showRecipientChipPopover` — function, line 460
- **called from:**
- `static/js/emailLibrary/index.js:460`
- `static/js/emailLibrary/index.js:554`

## `_wireRecipientChips` — function, line 523
- **called from:**
- `static/js/emailLibrary/index.js:523`
- `static/js/emailLibrary/index.js:6213`
- `static/js/emailLibrary/reader.js:350`
- `static/js/emailLibrary/reader.js:507`

## `_emailReaderForSelectAllTarget` — function, line 575
- **called from:**
- `static/js/emailLibrary/index.js:575`
- `static/js/emailLibrary/index.js:586`

## `_emailReadContextKey` — function, line 593
- **called from:**
- `static/js/emailLibrary/index.js:593`
- `static/js/emailLibrary/index.js:5897`

## `_emailReadContextIsCurrent` — function, line 597
- **called from:**
- `static/js/emailLibrary/index.js:597`
- `static/js/emailLibrary/index.js:617`
- `static/js/emailLibrary/index.js:5900`

## `_emailMatchesReadContext` — function, line 606
- **called from:**
- `static/js/emailLibrary/index.js:606`
- `static/js/emailLibrary/index.js:619`
- `static/js/emailLibrary/index.js:661`

## `_syncEmailReadState` — function, line 613
- **called from:**
- `static/js/emailLibrary/index.js:613`
- `static/js/emailLibrary/index.js:698`
- `static/js/emailLibrary/index.js:5617`
- `static/js/emailLibrary/index.js:5945`
- `static/js/emailLibrary/index.js:5953`
- `static/js/emailLibrary/index.js:5982`
- `static/js/emailLibrary/menus.js:143`
- `static/js/emailLibrary/menus.js:183`
- `static/js/emailLibrary/menus.js:418`
- `static/js/emailLibrary/menus.js:431`
- `static/js/emailLibrary/menus.js:811`
- `static/js/emailLibrary/reader.js:311`
- `static/js/emailLibrary/reader.js:458`

## `_syncEmailDoneState` — function, line 656
- **called from:**
- `static/js/emailLibrary/index.js:656`
- `static/js/emailLibrary/index.js:697`
- `static/js/emailLibrary/index.js:6024`
- `static/js/emailLibrary/reader.js:310`
- `static/js/emailLibrary/reader.js:457`

## `_toggleUnreadEmails` — function, line 708
- **called from:**
- `static/js/emailLibrary/index.js:708`
- `static/js/emailLibrary/index.js:2600`
- `static/js/emailLibrary/index.js:2609`

## `_syncUnreadTabBadge` — function, line 721
- **called from:**
- `static/js/emailLibrary/index.js:721`
- `static/js/emailLibrary/index.js:5000`
- `static/js/emailLibrary/index.js:5028`

## `_syncCurrentAccountUnreadCount` — function, line 734
- **called from:**
- `static/js/emailLibrary/index.js:734`
- `static/js/emailLibrary/index.js:5001`

## `_syncUnreadWindowGlow` — function, line 746
- **called from:**
- `static/js/emailLibrary/index.js:711`
- `static/js/emailLibrary/index.js:746`
- `static/js/emailLibrary/index.js:770`
- `static/js/emailLibrary/index.js:2694`
- `static/js/emailLibrary/index.js:3546`
- `static/js/emailLibrary/index.js:4008`
- `static/js/emailLibrary/index.js:5122`

## `_syncReminderClearButton` — function, line 750
- **called from:**
- `static/js/emailLibrary/index.js:750`
- `static/js/emailLibrary/index.js:771`
- `static/js/emailLibrary/index.js:780`
- `static/js/emailLibrary/index.js:2695`
- `static/js/emailLibrary/index.js:2793`
- `static/js/emailLibrary/index.js:3547`
- `static/js/emailLibrary/index.js:4009`

## `_syncSearchOptionsMenu` — function, line 754
- **called from:**
- `static/js/emailLibrary/index.js:716`
- `static/js/emailLibrary/index.js:754`
- `static/js/emailLibrary/index.js:773`
- `static/js/emailLibrary/index.js:781`
- `static/js/emailLibrary/index.js:801`
- `static/js/emailLibrary/index.js:2698`
- `static/js/emailLibrary/index.js:2712`
- `static/js/emailLibrary/index.js:2743`
- `static/js/emailLibrary/index.js:2752`
- `static/js/emailLibrary/index.js:2767`
- `static/js/emailLibrary/index.js:2792`
- `static/js/emailLibrary/index.js:3215`
- `static/js/emailLibrary/index.js:4011`
- `static/js/emailLibrary/index.js:4116`
- `static/js/emailLibrary/index.js:4124`
- `static/js/emailLibrary/index.js:4136`
- `static/js/emailLibrary/index.js:5349`

## `_setEmailListFilter` — function, line 766
- **called from:**
- `static/js/emailLibrary/index.js:766`
- `static/js/emailLibrary/index.js:2721`

## `_toggleEmailAttachmentFilter` — function, line 778
- **called from:**
- `static/js/emailLibrary/index.js:778`
- `static/js/emailLibrary/index.js:2720`

## `_renderAccountsLoading` — function, line 786
- **called from:**
- `static/js/emailLibrary/index.js:786`
- `static/js/emailLibrary/index.js:3096`

## `_syncEmailReminderBellVisibility` — function, line 798
- **called from:**
- `static/js/emailLibrary/index.js:798`
- `static/js/emailLibrary/index.js:807`
- `static/js/emailLibrary/index.js:809`
- `static/js/emailLibrary/index.js:816`

## `_loadEmailReminderBellVisibility` — function, line 804
- **called from:**
- `static/js/emailLibrary/index.js:804`
- `static/js/emailLibrary/index.js:3109`

## `_readCssPx` — function, line 819
- **called from:**
- `static/js/emailLibrary/index.js:819`
- `static/js/emailLibrary/index.js:903`

## `_emailSplitLeftEdge` — function, line 825
- **called from:**
- `static/js/emailLibrary/index.js:825`
- `static/js/emailLibrary/index.js:920`
- `static/js/emailLibrary/index.js:920`
- `static/js/emailLibrary/index.js:959`
- `static/js/emailLibrary/index.js:974`
- `static/js/emailLibrary/index.js:3499`

## `_setEmailDocumentSplit` — function, line 829
- **called from:**
- `static/js/emailLibrary/index.js:829`
- `static/js/emailLibrary/index.js:974`
- `static/js/emailLibrary/index.js:3512`

## `_measureEmailDocumentSplit` — function, line 845
- **called from:**
- `static/js/emailLibrary/index.js:845`
- `static/js/emailLibrary/index.js:878`
- `static/js/emailLibrary/index.js:879`
- `static/js/emailLibrary/index.js:881`
- `static/js/emailLibrary/index.js:882`

## `_scheduleEmailDocumentSplitMeasure` — function, line 876
- **called from:**
- `static/js/emailLibrary/index.js:876`
- `static/js/emailLibrary/index.js:975`
- `static/js/emailLibrary/index.js:2831`
- `static/js/emailLibrary/index.js:3513`

## `_clearEmailDocumentSplit` — function, line 885
- **called from:**
- `static/js/emailLibrary/index.js:885`
- `static/js/emailLibrary/index.js:3387`
- `static/js/emailLibrary/index.js:3455`

## `_emailSplitLeftEdgeIfSidebarCollapsed` — function, line 901
- **called from:**
- `static/js/emailLibrary/index.js:901`
- `static/js/emailLibrary/index.js:921`

## `_hasDesktopRoomForEmailAndDocument` — function, line 906
- **called from:**
- `static/js/emailLibrary/index.js:906`
- `static/js/emailLibrary/index.js:935`
- `static/js/emailLibrary/index.js:938`

## `_prepareEmailWindowForDocument` — function, line 925
- **called from:**
- `static/js/emailLibrary/attachments.js:182`
- `static/js/emailLibrary/index.js:925`
- `static/js/emailLibrary/index.js:2826`

## `_wireUnreadTabClick` — function, line 984
- **called from:**
- `static/js/emailLibrary/index.js:984`
- `static/js/emailLibrary/index.js:2592`

## `_deleteEmailAndAdvance` — function, line 994
- **called from:**
- `static/js/emailLibrary/index.js:994`
- `static/js/emailLibrary/index.js:3043`

## `_showEmailDeleteOverlay` — function, line 1037
- **called from:**
- `static/js/emailInbox.js:1348`
- `static/js/emailInbox.js:1361`
- `static/js/emailLibrary/index.js:1001`
- `static/js/emailLibrary/index.js:1037`
- `static/js/emailLibrary/menus.js:251`
- `static/js/emailLibrary/menus.js:277`
- `static/js/emailLibrary/menus.js:517`
- `static/js/emailLibrary/menus.js:768`

## `remove` — method?, line 1052
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

## `_animateEmailCardRemoval` — function, line 1062
- **called from:**
- `static/js/emailLibrary/index.js:1018`
- `static/js/emailLibrary/index.js:1062`
- `static/js/emailLibrary/index.js:2786`
- `static/js/emailLibrary/menus.js:80`
- `static/js/emailLibrary/menus.js:458`
- `static/js/emailLibrary/menus.js:486`
- `static/js/emailLibrary/menus.js:528`
- `static/js/emailLibrary/menus.js:864`
- `static/js/emailLibrary/menus.js:872`

## `_selectedEmailExportPayload` — function, line 1086
- **called from:**
- `static/js/emailLibrary/index.js:1086`
- `static/js/emailLibrary/index.js:1295`

## `_downloadBlob` — function, line 1103
- **called from:**
- `static/js/emailLibrary/index.js:1103`
- `static/js/emailLibrary/index.js:1351`

## `_filenameFromContentDisposition` — function, line 1114
- **called from:**
- `static/js/emailLibrary/index.js:1114`
- `static/js/emailLibrary/index.js:1347`

## `_printSelectedEmails` — function, line 1126
- **called from:**
- `static/js/emailLibrary/index.js:1126`
- `static/js/emailLibrary/index.js:1326`

## `readWorker` — arrow, line 1132
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `esc` — arrow, line 1206
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

## `esc` — arrow, line 1210
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

## `cleanupFrame` — arrow, line 1256
- **called from:**
- `static/js/emailLibrary/index.js:1289`

## `_exportSelectedBundle` — function, line 1294
- **called from:**
- `static/js/emailLibrary/index.js:1294`
- `static/js/emailLibrary/index.js:1378`
- `static/js/emailLibrary/index.js:1382`
- `static/js/emailLibrary/index.js:1386`

## `_exportSelectedEmails` — function, line 1377
- **called from:**
- `static/js/emailLibrary/index.js:1377`

## `_exportSelectedEmailPdf` — function, line 1381
- **called from:**
- `static/js/emailLibrary/index.js:1381`

## `_exportSelectedAttachments` — function, line 1385
- **called from:**
- `static/js/emailLibrary/index.js:1385`
- `static/js/emailLibrary/menus.js:594`

## `_openSettingsTab` — function, line 1394
- **called from:**
- `static/js/emailLibrary/index.js:1394`
- `static/js/emailLibrary/index.js:1413`
- `static/js/emailLibrary/index.js:1436`
- `static/js/emailLibrary/index.js:5388`

## `_openGlobalEmailSettings` — function, line 1410
- **called from:**
- `static/js/emailLibrary/index.js:1410`
- `static/js/emailLibrary/index.js:2597`
- `static/js/emailLibrary/index.js:2606`
- `static/js/emailLibrary/index.js:2614`
- `static/js/emailLibrary/index.js:2819`

## `_emailSetupHintHtml` — function, line 1424
- **called from:**
- `static/js/emailLibrary/index.js:1424`
- `static/js/emailLibrary/index.js:5182`

## `_wireEmailSetupHint` — function, line 1430
- **called from:**
- `static/js/emailLibrary/index.js:1430`
- `static/js/emailLibrary/index.js:5183`

## `_acct` — function, line 1441
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

## `_emailMutationQuery` — function, line 1445
- **called from:**
- `static/js/emailLibrary/index.js:1009`
- `static/js/emailLibrary/index.js:1445`
- `static/js/emailLibrary/menus.js:254`
- `static/js/emailLibrary/menus.js:280`
- `static/js/emailLibrary/menus.js:520`

## `_requireSuccessfulEmailMutation` — function, line 1454
- **called from:**
- `static/js/emailLibrary/index.js:1010`
- `static/js/emailLibrary/index.js:1454`
- `static/js/emailLibrary/menus.js:255`
- `static/js/emailLibrary/menus.js:281`
- `static/js/emailLibrary/menus.js:521`

## `_rememberedEmailAccountId` — function, line 1463
- **called from:**
- `static/js/emailLibrary/index.js:1463`
- `static/js/emailLibrary/index.js:2121`
- `static/js/emailLibrary/index.js:2400`

## `_libSyncDateFrom` — function, line 1507
- **called from:**
- `static/js/emailLibrary/index.js:1507`
- `static/js/emailLibrary/index.js:1514`
- `static/js/emailLibrary/index.js:1547`

## `_libRelativeTime` — function, line 1513
- **called from:**
- `static/js/emailLibrary/index.js:1513`
- `static/js/emailLibrary/index.js:1530`

## `_renderEmailSyncStatus` — function, line 1526
- **called from:**
- `static/js/emailLibrary/index.js:1526`
- `static/js/emailLibrary/index.js:1563`
- `static/js/emailLibrary/index.js:2556`

## `_setEmailSyncStatus` — function, line 1542
- **called from:**
- `static/js/emailLibrary/index.js:1542`
- `static/js/emailLibrary/index.js:1757`
- `static/js/emailLibrary/index.js:1763`
- `static/js/emailLibrary/index.js:1773`
- `static/js/emailLibrary/index.js:2206`
- `static/js/emailLibrary/index.js:2241`
- `static/js/emailLibrary/index.js:2250`
- `static/js/emailLibrary/index.js:4526`
- `static/js/emailLibrary/index.js:4603`
- `static/js/emailLibrary/index.js:4638`
- `static/js/emailLibrary/index.js:4680`
- `static/js/emailLibrary/index.js:5086`
- `static/js/emailLibrary/index.js:5111`
- `static/js/emailLibrary/index.js:5115`
- `static/js/emailLibrary/index.js:5198`

## `_clearStaleEmailRefetch` — function, line 1570
- **called from:**
- `static/js/emailLibrary/index.js:1570`
- `static/js/emailLibrary/index.js:5093`

## `_scheduleStaleEmailRefetch` — function, line 1578
- **called from:**
- `static/js/emailLibrary/index.js:1578`
- `static/js/emailLibrary/index.js:5092`

## `_libCacheKeyFor` — function, line 1591
- **called from:**
- `static/js/emailLibrary/index.js:1591`
- `static/js/emailLibrary/index.js:1602`
- `static/js/emailLibrary/index.js:2191`
- `static/js/emailLibrary/index.js:2212`

## `_libCacheKey` — function, line 1601
- **called from:**
- `static/js/emailLibrary/index.js:1601`
- `static/js/emailLibrary/index.js:1748`
- `static/js/emailLibrary/index.js:2261`
- `static/js/emailLibrary/index.js:5058`

## `_libSessionCacheKey` — function, line 1609
- **called from:**
- `static/js/emailLibrary/index.js:1609`
- `static/js/emailLibrary/index.js:1617`
- `static/js/emailLibrary/index.js:1621`
- `static/js/emailLibrary/index.js:1646`
- `static/js/emailLibrary/index.js:1692`

## `_libPersistCacheKey` — function, line 1612
- **called from:**
- `static/js/emailLibrary/index.js:1612`
- `static/js/emailLibrary/index.js:1631`
- `static/js/emailLibrary/index.js:1669`
- `static/js/emailLibrary/index.js:1672`
- `static/js/emailLibrary/index.js:1693`

## `_libSessionCacheGet` — function, line 1615
- **called from:**
- `static/js/emailLibrary/index.js:1615`
- `static/js/emailLibrary/index.js:1704`

## `_libPersistCacheGet` — function, line 1629
- **called from:**
- `static/js/emailLibrary/index.js:1629`
- `static/js/emailLibrary/index.js:1704`

## `_libSessionCachePut` — function, line 1644
- **called from:**
- `static/js/emailLibrary/index.js:1644`
- `static/js/emailLibrary/index.js:1723`

## `_libPrunePersistCache` — function, line 1649
- **called from:**
- `static/js/emailLibrary/index.js:1649`
- `static/js/emailLibrary/index.js:1670`

## `_libPersistCachePut` — function, line 1667
- **called from:**
- `static/js/emailLibrary/index.js:1667`
- `static/js/emailLibrary/index.js:1724`

## `_looksLikeFixtureEmailRow` — function, line 1675
- **called from:**
- `static/js/emailLibrary/index.js:1675`

## `_libCacheHasFixtureRows` — function, line 1687
- **called from:**
- `static/js/emailLibrary/index.js:1687`
- `static/js/emailLibrary/index.js:1698`
- `static/js/emailLibrary/index.js:1706`
- `static/js/emailLibrary/index.js:1716`

## `_libDropCacheKey` — function, line 1690
- **called from:**
- `static/js/emailLibrary/index.js:1690`
- `static/js/emailLibrary/index.js:1699`
- `static/js/emailLibrary/index.js:1707`
- `static/js/emailLibrary/index.js:1717`

## `_libCacheGet` — function, line 1695
- **called from:**
- `static/js/emailLibrary/index.js:1695`
- `static/js/emailLibrary/index.js:1749`
- `static/js/emailLibrary/index.js:2213`
- `static/js/emailLibrary/index.js:5059`

## `_libCachePut` — function, line 1715
- **called from:**
- `static/js/emailLibrary/index.js:1715`
- `static/js/emailLibrary/index.js:2191`
- `static/js/emailLibrary/index.js:2235`
- `static/js/emailLibrary/index.js:2263`
- `static/js/emailLibrary/index.js:5095`

## `_resetBulkSelectionForContextChange` — function, line 1731
- **called from:**
- `static/js/emailLibrary/index.js:1731`
- `static/js/emailLibrary/index.js:1744`
- `static/js/emailLibrary/index.js:3996`
- `static/js/emailLibrary/index.js:4096`
- `static/js/emailLibrary/index.js:4145`
- `static/js/emailLibrary/index.js:4180`
- `static/js/emailLibrary/index.js:4358`
- `static/js/emailLibrary/index.js:4500`

## `_resetEmailListForFreshLoad` — function, line 1742
- **called from:**
- `static/js/emailLibrary/index.js:1742`
- `static/js/emailLibrary/index.js:1800`
- `static/js/emailLibrary/settingsPage.js:573`

## `_exitEmailReaderModeForList` — function, line 1776
- **called from:**
- `static/js/emailLibrary/index.js:1743`
- `static/js/emailLibrary/index.js:1776`
- `static/js/emailLibrary/index.js:2656`
- `static/js/emailLibrary/index.js:3013`
- `static/js/emailLibrary/index.js:3018`
- `static/js/emailLibrary/index.js:3086`
- `static/js/emailLibrary/index.js:3914`
- `static/js/emailLibrary/index.js:4499`

## `_loadEmailsFresh` — function, line 1790
- **called from:**
- `static/js/emailLibrary/index.js:718`
- `static/js/emailLibrary/index.js:775`
- `static/js/emailLibrary/index.js:783`
- `static/js/emailLibrary/index.js:1790`
- `static/js/emailLibrary/index.js:1836`
- `static/js/emailLibrary/index.js:2690`
- `static/js/emailLibrary/index.js:2697`
- `static/js/emailLibrary/index.js:2745`
- `static/js/emailLibrary/index.js:2754`
- `static/js/emailLibrary/index.js:2795`
- `static/js/emailLibrary/index.js:3217`
- `static/js/emailLibrary/index.js:4013`
- `static/js/emailLibrary/index.js:4103`
- `static/js/emailLibrary/menus.js:722`

## `_refreshEmailLibraryFromUi` — function, line 1806
- **called from:**
- `static/js/emailLibrary/index.js:1806`
- `static/js/emailLibrary/index.js:1886`
- `static/js/emailLibrary/index.js:2813`

## `refreshEmailLibrary` — function, line 1834
- **called from:**
- `static/js/emailLibrary/index.js:1834`
- `static/js/emailLibrary/unsubscribe.js:530`

## `_initMobileEmailPullRefresh` — function, line 1845
- **called from:**
- `static/js/emailLibrary/index.js:1845`
- `static/js/emailLibrary/index.js:2815`

## `setPull` — function, line 1871
- **called from:**
- `static/app.js:4513`
- `static/app.js:4526`
- `static/app.js:4530`
- `static/app.js:4533`
- `static/app.js:4547`
- `static/app.js:4558`
- `static/app.js:4565`
- `static/app.js:4570`
- `static/app.js:4578`
- `static/app.js:4583`
- `static/js/emailLibrary/index.js:1871`
- `static/js/emailLibrary/index.js:1884`
- `static/js/emailLibrary/index.js:1891`
- `static/js/emailLibrary/index.js:1901`
- `static/js/emailLibrary/index.js:1908`
- `static/js/emailLibrary/index.js:1913`
- `static/js/emailLibrary/index.js:1921`
- `static/js/emailLibrary/index.js:1926`

## `runRefresh` — function, line 1881
- **called from:**
- `static/app.js:4523`
- `static/app.js:4577`
- `static/js/emailLibrary/index.js:1881`
- `static/js/emailLibrary/index.js:1920`

## `_isChatInteractionBusy` — function, line 1930
- **called from:**
- `static/js/emailLibrary/index.js:1930`
- `static/js/emailLibrary/index.js:1943`
- `static/js/emailLibrary/index.js:1949`
- `static/js/emailLibrary/index.js:2029`

## `_canRunEmailPrewarm` — function, line 1940
- **called from:**
- `static/js/emailLibrary/index.js:1940`
- `static/js/emailLibrary/index.js:1955`
- `static/js/emailLibrary/index.js:2024`
- `static/js/emailLibrary/index.js:2065`

## `_isEmailPrewarmTemporarilyBlocked` — function, line 1946
- **called from:**
- `static/js/emailLibrary/index.js:1946`
- `static/js/emailLibrary/index.js:2066`

## `_isEmailPrewarmCurrent` — function, line 1952
- **called from:**
- `static/js/emailLibrary/index.js:1952`
- `static/js/emailLibrary/index.js:2132`
- `static/js/emailLibrary/index.js:2140`
- `static/js/emailLibrary/index.js:2143`
- `static/js/emailLibrary/index.js:2155`
- `static/js/emailLibrary/index.js:2168`
- `static/js/emailLibrary/index.js:2170`
- `static/js/emailLibrary/index.js:2186`
- `static/js/emailLibrary/index.js:2188`
- `static/js/emailLibrary/index.js:2205`
- `static/js/emailLibrary/index.js:2211`
- `static/js/emailLibrary/index.js:2230`
- `static/js/emailLibrary/index.js:2232`

## `_settleEmailPrewarm` — function, line 1958
- **called from:**
- `static/js/emailLibrary/index.js:1958`
- `static/js/emailLibrary/index.js:2069`
- `static/js/emailLibrary/index.js:2078`
- `static/js/emailLibrary/index.js:2089`
- `static/js/emailLibrary/index.js:2093`
- `static/js/emailLibrary/index.js:2102`

## `_cancelEmailPrewarm` — function, line 1972
- **called from:**
- `static/js/emailLibrary/index.js:1972`
- `static/js/emailLibrary/index.js:2344`
- `static/js/emailLibrary/index.js:3380`

## `_scheduleEmailPrewarm` — function, line 1993
- **called from:**
- `static/js/emailLibrary/index.js:1993`
- `static/js/emailLibrary/index.js:2116`
- `static/js/emailLibrary/index.js:2161`

## `clearScheduledAttempt` — function, line 2005
- **called from:**
- `static/js/emailLibrary/index.js:2005`
- `static/js/emailLibrary/index.js:2034`

## `scheduleIdleRetry` — function, line 2014
- **called from:**
- `static/js/emailLibrary/index.js:2014`
- `static/js/emailLibrary/index.js:2025`
- `static/js/emailLibrary/index.js:2041`
- `static/js/emailLibrary/index.js:2067`
- `static/js/emailLibrary/index.js:2074`
- `static/js/emailLibrary/index.js:2098`

## `handlePriorityChange` — function, line 2022
- **called from:**
- `static/js/emailLibrary/index.js:2022`

## `requestIdle` — function, line 2052
- **called from:**
- `static/js/emailLibrary/index.js:2052`
- `static/js/emailLibrary/index.js:2108`

## `prewarmEmailLibrary` — function, line 2112
- **called from:**
- `static/js/emailInbox.js:198`
- `static/js/emailLibrary/index.js:2112`

## `_chooseEmailPrewarmAccountId` — function, line 2119
- **called from:**
- `static/js/emailLibrary/index.js:2119`
- `static/js/emailLibrary/index.js:2154`

## `_ensureEmailAccountsForPrewarm` — function, line 2131
- **called from:**
- `static/js/emailLibrary/index.js:2131`
- `static/js/emailLibrary/index.js:2169`
- `static/js/emailLibrary/index.js:2210`

## `prewarmUnreadEmails` — function, line 2160
- **called from:**
- `static/js/emailInbox.js:358`
- `static/js/emailLibrary/index.js:2160`

## `_prewarmUnreadEmailsNow` — function, line 2167
- **called from:**
- `static/js/emailLibrary/index.js:2162`
- `static/js/emailLibrary/index.js:2167`

## `_prewarmEmailViews` — function, line 2204
- **called from:**
- `static/js/emailLibrary/index.js:2204`

## `_libCacheWriteBack` — function, line 2253
- **called from:**
- `static/js/emailLibrary/index.js:1023`
- `static/js/emailLibrary/index.js:2253`
- `static/js/emailLibrary/index.js:5656`
- `static/js/emailLibrary/menus.js:83`
- `static/js/emailLibrary/menus.js:461`
- `static/js/emailLibrary/menus.js:489`
- `static/js/emailLibrary/menus.js:531`
- `static/js/emailLibrary/menus.js:708`
- `static/js/emailLibrary/menus.js:906`
- `static/js/emailLibrary/unsubscribe.js:467`
- `static/js/emailLibrary/unsubscribe.js:572`
- `static/js/emailLibrary/unsubscribe.js:641`

## `_publishActiveAccount` — function, line 2276
- **called from:**
- `static/js/emailLibrary/index.js:2276`
- `static/js/emailLibrary/index.js:2398`
- `static/js/emailLibrary/index.js:2403`
- `static/js/emailLibrary/index.js:3123`
- `static/js/emailLibrary/index.js:3148`
- `static/js/emailLibrary/index.js:3212`
- `static/js/emailLibrary/index.js:3270`
- `static/js/emailLibrary/index.js:3363`
- `static/js/emailLibrary/settingsPage.js:570`

## `initEmailLibrary` — function, line 2301
- **called from:**
- `static/js/emailInbox.js:167`
- `static/js/emailLibrary/index.js:2301`

## `isOpen` — function, line 2324
- **called from:**
- `static/app.js:722`
- `static/app.js:895`
- `static/js/admin.js:2219`
- `static/js/admin.js:2228`
- `static/js/admin.js:2236`
- `static/js/editor/shortcuts-popover.js:148`
- `static/js/emailLibrary/index.js:2324`
- `static/js/features/notes/ui/layout.js:49`
- `static/js/galleryEditor.js:9957`
- `static/js/galleryEditor.js:11749`
- `static/js/galleryEditor.js:14101`
- `static/js/keyboard-shortcuts.js:158`
- `static/js/research/panel.js:221`
- `static/js/search-chat.js:64`
- `static/js/search-chat.js:160`

## `openEmailFromTool` — function, line 2326
- **called from:**
- `static/js/chat.js:5850`
- `static/js/emailLibrary/index.js:2326`

## `openEmailLibrary` — function, line 2340
- **called from:**
- `static/js/emailInbox.js:62`
- `static/js/emailInbox.js:284`
- `static/js/emailInbox.js:315`
- `static/js/emailLibrary/index.js:2337`
- `static/js/emailLibrary/index.js:2340`
- `static/js/emailLibrary/index.js:3375`
- `static/js/emailLibrary/index.js:4479`

## `openAutoReplySettings` — arrow, line 2612
- **called from:**
- `static/js/emailLibrary/index.js:2620`

## `_composeNew` — arrow, line 2823
- **called from:**
- `static/js/emailInbox.js:191`
- `static/js/emailInbox.js:294`
- `static/js/emailInbox.js:1470`

## `_positionFab` — function, line 2856
- **called from:**
- `static/js/emailLibrary/index.js:2848`
- `static/js/emailLibrary/index.js:2856`
- `static/js/emailLibrary/index.js:2884`
- `static/js/emailLibrary/index.js:2889`

## `_revealFab` — arrow, line 2881
- **called from:**
- `static/js/emailLibrary/index.js:2905`
- `static/js/emailLibrary/index.js:2908`
- `static/js/emailLibrary/index.js:2912`

## `pop` — arrow, line 2889
- **called from:**
- `core/auth.py:345`
- `core/auth.py:369`
- `core/auth.py:498`
- `core/auth.py:569`
- `core/auth.py:607`
- `core/auth.py:608`
- `core/auth.py:609`
- `core/auth.py:659`
- `core/auth.py:667`
- `core/auth.py:685`
- `core/auth.py:691`
- `core/auth.py:701`
- `core/auth.py:714`
- `core/session_manager.py:231`
- `core/session_manager.py:349`
- `core/session_manager.py:357`
- `core/session_manager.py:375`
- `core/session_manager.py:466`
- `core/session_manager.py:529`
- `core/session_manager.py:609`
- `core/session_manager.py:1005`
- `mcp_servers/email_server.py:1580`
- `mcp_servers/email_server.py:4041`
- `mcp_servers/email_server.py:4042`
- `routes/auth_routes.py:518`
- `routes/calendar_routes.py:976`
- `routes/chat_helpers.py:383`
- `routes/chat_routes.py:206`
- `routes/chat_routes.py:4266`
- `routes/chat_routes.py:4338`
- `routes/chat_routes.py:4411`
- `routes/chat_routes.py:4416`
- `routes/chat_routes.py:4499`
- `routes/chat_routes.py:4960`
- `routes/chat_routes.py:5503`
- `routes/chat_routes.py:5514`
- `routes/codex_routes.py:696`
- `routes/codex_routes.py:698`
- `routes/cookbook_routes.py:468`
- `routes/cookbook_routes.py:480`
- `routes/cookbook_routes.py:499`
- `routes/cookbook_routes.py:500`
- `routes/cookbook_routes.py:501`
- `routes/cookbook_routes.py:502`
- `routes/device_flow.py:74`
- `routes/device_flow.py:119`
- `routes/device_flow.py:171`
- `routes/device_flow.py:175`
- `routes/device_flow.py:178`
- `routes/device_flow.py:190`
- `routes/editor_agent_routes.py:1378`
- `routes/editor_agent_routes.py:1390`
- `routes/editor_agent_routes.py:1412`
- `routes/editor_agent_routes.py:1419`
- `routes/editor_agent_routes.py:1638`
- `routes/editor_agent_routes.py:1882`
- `routes/editor_agent_routes.py:1890`
- `routes/editor_agent_routes.py:2059`
- `routes/email/email_pollers.py:529`
- `routes/email/email_routes.py:206`
- … +685 more (grep the name in repo)

## `onEnd` — arrow, line 2894
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_setSelectBtnState` — arrow, line 2923
- **called from:**
- `static/js/emailLibrary/index.js:2932`
- `static/js/emailLibrary/index.js:2952`
- `static/js/emailLibrary/index.js:3006`
- `static/js/emailLibrary/index.js:3076`

## `selectExpandedEmailText` — arrow, line 2975
- **called from:**
- `static/js/emailLibrary/index.js:2988`

## `_loadAccounts` — function, line 3116
- **called from:**
- `static/js/emailLibrary/index.js:3106`
- `static/js/emailLibrary/index.js:3116`
- `static/js/emailLibrary/index.js:3311`
- `static/js/emailLibrary/settingsPage.js:545`

## `_renderAccountsStrip` — function, line 3155
- **called from:**
- `static/js/emailLibrary/index.js:743`
- `static/js/emailLibrary/index.js:3094`
- `static/js/emailLibrary/index.js:3126`
- `static/js/emailLibrary/index.js:3151`
- `static/js/emailLibrary/index.js:3155`
- `static/js/emailLibrary/index.js:3213`
- `static/js/emailLibrary/index.js:3296`
- `static/js/emailLibrary/index.js:3351`
- `static/js/emailLibrary/index.js:3364`
- `static/js/emailLibrary/index.js:4981`
- `static/js/emailLibrary/settingsPage.js:565`
- `static/js/emailLibrary/settingsPage.js:572`
- `static/js/emailLibrary/settingsPage.js:588`
- `static/js/emailLibrary/settingsPage.js:607`
- `static/js/emailLibrary/settingsPage.js:752`
- `static/js/emailLibrary/settingsPage.js:782`

## `esc` — arrow, line 3159
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

## `_refreshAccountUnreadHighlights` — function, line 3273
- **called from:**
- `static/js/emailLibrary/index.js:3152`
- `static/js/emailLibrary/index.js:3220`
- `static/js/emailLibrary/index.js:3273`
- `static/js/emailLibrary/index.js:5172`

## `mountEmailSettings` — function, line 3299
- **called from:**
- `static/js/emailLibrary/index.js:3299`
- `static/js/settings.js:2438`

## `render` — arrow, line 3308
- **called from:**
- `scripts/generate_env_reference.py:1219`
- `src/agent_tools/media_tools.py:493`
- `src/agent_tools/media_tools.py:1002`
- `tests/test_audit_c5_benchmark_evidence.py:2875`
- `tests/test_audit_c5_benchmark_evidence.py:2882`
- `tests/test_audit_c5_benchmark_evidence.py:2892`
- `tests/test_audit_c5_benchmark_evidence.py:2906`
- `tests/test_audit_c5_benchmark_evidence.py:2925`
- `tests/test_audit_c5_benchmark_evidence.py:2933`
- `tests/test_audit_c5_benchmark_evidence.py:2935`
- `tests/test_audit_c5_benchmark_evidence.py:2978`
- `tests/test_audit_c5_benchmark_evidence.py:3001`
- `tests/test_audit_c5_benchmark_evidence.py:3006`
- `tests/test_env_reference.py:168`
- `tests/test_env_reference.py:179`
- `static/js/calendar.js:1664`
- `static/js/calendar.js:2653`
- `static/js/chat.js:3712`
- `static/js/chat.js:4812`
- `static/js/chat.js:5173`
- `static/js/chat.js:6073`
- `static/js/chat.js:6217`
- `static/js/chat.js:7371`
- `static/js/documentLibrary.js:108`
- `static/js/documentLibrary.js:124`
- `static/js/editor/adjustments-worker.js:5`
- `static/js/editor/adjustments-worker.js:20`
- `static/js/editor/build/command-palette.js:22`
- `static/js/editor/build/command-palette.js:56`
- `static/js/editor/build/command-palette.js:64`
- `static/js/editor/build/command-palette.js:67`
- `static/js/editor/build/command-palette.js:68`
- `static/js/editor/layer-panel.js:186`
- `static/js/editor/layer-panel.js:302`
- `static/js/editor/layer-panel.js:440`
- `static/js/editor/layer-panel.js:490`
- `static/js/editor/layer-panel.js:581`
- `static/js/editor/layer-panel.js:613`
- `static/js/editor/layer-panel.js:672`
- `static/js/editor/layer-panel.js:711`
- `static/js/editor/layer-panel.js:725`
- `static/js/editor/layer-panel.js:739`
- `static/js/editor/layer-panel.js:751`
- `static/js/editor/layer-panel.js:795`
- `static/js/editor/layer-panel.js:807`
- `static/js/editor/layer-panel.js:839`
- `static/js/editor/layer-panel.js:918`
- `static/js/editor/layer-panel.js:929`
- `static/js/editor/layer-panel.js:942`
- `static/js/editor/layer-panel.js:962`
- `static/js/editor/layer-panel.js:992`
- `static/js/editor/layer-panel.js:1042`
- `static/js/editor/layer-panel.js:1056`
- `static/js/editor/layer-panel.js:1079`
- `static/js/editor/layer-panel.js:1101`
- `static/js/editor/layer-panel.js:1118`
- `static/js/editor/layer-panel.js:1132`
- `static/js/editor/layer-panel.js:1139`
- `static/js/editor/layer-panel.js:1315`
- `static/js/editor/layer-panel.js:1342`
- … +104 more (grep the name in repo)

## `openEmailLibrarySettings` — function, line 3374
- **called from:**
- `static/js/emailLibrary/index.js:3374`

## `closeEmailLibrary` — function, line 3379
- **called from:**
- `static/js/emailInbox.js:176`
- `static/js/emailLibrary/index.js:2659`
- `static/js/emailLibrary/index.js:2827`
- `static/js/emailLibrary/index.js:3021`
- `static/js/emailLibrary/index.js:3379`

## `_makeDraggable` — function, line 3409
- **called from:**
- `static/js/emailLibrary/index.js:2683`
- `static/js/emailLibrary/index.js:3409`
- `static/js/emailLibrary/reader.js:437`
- `static/js/galleryEditor.js:13543`

## `enterFullscreen` — arrow, line 3417
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `exitFullscreen` — arrow, line 3432
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_snapEmailModalToLeftSidebar` — function, line 3479
- **called from:**
- `static/js/emailLibrary/aiReply.js:40`
- `static/js/emailLibrary/index.js:980`
- `static/js/emailLibrary/index.js:3479`
- `static/js/emailLibrary/index.js:6108`
- `static/js/emailLibrary/index.js:6113`
- `static/js/emailLibrary/reader.js:357`
- `static/js/emailLibrary/reader.js:362`
- `static/js/emailLibrary/reader.js:515`
- `static/js/emailLibrary/reader.js:520`

## `_loadFolders` — function, line 3517
- **called from:**
- `static/js/emailLibrary/index.js:3108`
- `static/js/emailLibrary/index.js:3218`
- `static/js/emailLibrary/index.js:3517`
- `static/js/emailLibrary/settingsPage.js:575`

## `_crossFolderCandidates` — function, line 3598
- **called from:**
- `static/js/emailLibrary/index.js:3598`

## `pick` — arrow, line 3601
- **called from:**
- `static/js/document.js:1724`
- `static/js/document.js:2219`
- `static/js/document.js:2500`
- `static/js/editor/tools/eyedropper.js:73`
- `static/js/emailLibrary/index.js:3610`
- `static/js/emailLibrary/index.js:3611`
- `static/js/emailLibrary/index.js:3612`
- `static/js/galleryEditor.js:5549`
- `static/js/galleryEditor.js:5571`
- `static/js/researchSynapse.js:22`
- `static/js/signature.js:5`
- `static/js/signature.js:460`
- `static/js/slashCommands.js:1261`

## `_findEmailFolder` — function, line 3617
- **called from:**
- `static/js/emailLibrary/index.js:3617`
- `static/js/emailLibrary/index.js:3632`
- `static/js/emailLibrary/index.js:3635`
- `static/js/emailLibrary/index.js:3638`
- `static/js/emailLibrary/index.js:3641`
- `static/js/emailLibrary/index.js:3644`
- `static/js/emailLibrary/index.js:3647`
- `static/js/emailLibrary/index.js:3653`

## `_resolveEmailFolderAlias` — function, line 3627
- **called from:**
- `static/js/emailLibrary/index.js:1793`
- `static/js/emailLibrary/index.js:2686`
- `static/js/emailLibrary/index.js:3530`
- `static/js/emailLibrary/index.js:3627`

## `_sentFolderName` — function, line 3652
- **called from:**
- `static/js/emailLibrary/index.js:3652`
- `static/js/emailLibrary/index.js:3678`

## `_deriveSearchScope` — function, line 3656
- **called from:**
- `static/js/emailLibrary/index.js:3656`
- `static/js/emailLibrary/index.js:4502`
- `static/js/emailLibrary/index.js:4533`
- `static/js/emailLibrary/index.js:4535`

## `_buildSuggestionSource` — function, line 3708
- **called from:**
- `static/js/emailLibrary/index.js:3708`
- `static/js/emailLibrary/index.js:4323`

## `_add` — arrow, line 3713
- **called from:**
- `companion/pairing.py:147`
- `companion/pairing.py:155`
- `mcp_servers/email_server.py:3079`
- `mcp_servers/email_server.py:3083`
- `mcp_servers/email_server.py:3091`
- `routes/email/email_routes.py:6761`
- `routes/email/email_routes.py:6765`
- `routes/email/email_routes.py:6769`
- `routes/email/email_routes.py:7089`
- `routes/email/email_routes.py:7094`
- `routes/email/email_routes.py:7100`
- `routes/email/email_routes.py:7105`
- `tests/test_manage_mcp_command_allowlist.py:125`
- `tests/test_manage_mcp_command_allowlist.py:143`
- `tests/test_manage_mcp_command_allowlist.py:160`
- `tests/test_notes_reminder_temporal_redos.py:47`
- `tests/test_notes_reminder_temporal_redos.py:53`
- `static/js/emailLibrary/index.js:3723`
- `static/js/emailLibrary/index.js:3726`
- `static/js/emailLibrary/index.js:3738`

## `_parse` — arrow, line 3724
- **called from:**
- `src/agent_runtime/effect_log.py:229`
- `src/agent_runtime/effect_log.py:420`
- `src/agent_tools/editor_tools.py:364`
- `src/agent_tools/editor_tools.py:392`
- `src/agent_tools/editor_tools.py:442`
- `src/agent_tools/editor_tools.py:468`
- `src/agent_tools/editor_tools.py:644`
- `src/copilot.py:207`
- `tests/test_calendar_config_body.py:23`
- `tests/test_calendar_config_body.py:28`
- `tests/test_calendar_config_body.py:34`
- `static/js/cookbook-hwfit.js:1653`
- `static/js/cookbook-hwfit.js:1653`
- `static/js/emailLibrary/index.js:3728`
- `static/js/emailLibrary/index.js:3729`

## `_scoreSuggestion` — function, line 3745
- **called from:**
- `static/js/emailLibrary/index.js:3745`
- `static/js/emailLibrary/index.js:3822`

## `_formatEmailSuggestionDate` — function, line 3754
- **called from:**
- `static/js/emailLibrary/index.js:3754`
- `static/js/emailLibrary/index.js:3842`
- `static/js/emailLibrary/index.js:3894`

## `_libFilterIconFor` — function, line 3793
- **called from:**
- `static/js/emailLibrary/index.js:3793`
- `static/js/emailLibrary/index.js:3818`
- `static/js/emailLibrary/index.js:3865`
- `static/js/emailLibrary/index.js:4041`

## `_scoreFilterOption` — function, line 3801
- **called from:**
- `static/js/emailLibrary/index.js:3801`
- `static/js/emailLibrary/index.js:3818`

## `_filterSuggestions` — function, line 3811
- **called from:**
- `static/js/emailLibrary/index.js:3811`
- `static/js/emailLibrary/index.js:4335`

## `_exactTypedFilterSuggestion` — function, line 3855
- **called from:**
- `static/js/emailLibrary/index.js:3855`
- `static/js/emailLibrary/index.js:4425`

## `_emailMatchesPill` — function, line 3869
- **called from:**
- `static/js/emailLibrary/index.js:3869`
- `static/js/emailLibrary/index.js:3955`

## `_matchesQuery` — function, line 3892
- **called from:**
- `static/js/emailLibrary/index.js:3889`
- `static/js/emailLibrary/index.js:3892`

## `_applyPillFilter` — function, line 3913
- **called from:**
- `static/js/emailLibrary/index.js:3913`
- `static/js/emailLibrary/index.js:3962`
- `static/js/emailLibrary/index.js:4166`
- `static/js/emailLibrary/index.js:4225`
- `static/js/emailLibrary/index.js:4283`
- `static/js/emailLibrary/index.js:4308`
- `static/js/emailLibrary/index.js:4625`
- `static/js/emailLibrary/index.js:5079`

## `_localSearchFilter` — function, line 3960
- **called from:**
- `static/js/emailLibrary/index.js:3960`

## `_emailFilterLabelFor` — function, line 3967
- **called from:**
- `static/js/emailLibrary/index.js:3967`
- `static/js/emailLibrary/index.js:3980`
- `static/js/emailLibrary/index.js:3984`

## `_activeEmailFilterPills` — function, line 3977
- **called from:**
- `static/js/emailLibrary/index.js:3977`
- `static/js/emailLibrary/index.js:4024`

## `_clearActiveEmailFilterPill` — function, line 3995
- **called from:**
- `static/js/emailLibrary/index.js:3995`
- `static/js/emailLibrary/index.js:4090`

## `_renderSearchPills` — function, line 4016
- **called from:**
- `static/js/emailLibrary/index.js:717`
- `static/js/emailLibrary/index.js:774`
- `static/js/emailLibrary/index.js:782`
- `static/js/emailLibrary/index.js:2689`
- `static/js/emailLibrary/index.js:2696`
- `static/js/emailLibrary/index.js:2744`
- `static/js/emailLibrary/index.js:2753`
- `static/js/emailLibrary/index.js:2794`
- `static/js/emailLibrary/index.js:3216`
- `static/js/emailLibrary/index.js:4012`
- `static/js/emailLibrary/index.js:4016`
- `static/js/emailLibrary/index.js:4102`
- `static/js/emailLibrary/index.js:4161`
- `static/js/emailLibrary/index.js:4165`
- `static/js/emailLibrary/index.js:4184`
- `static/js/emailLibrary/index.js:4318`

## `esc` — arrow, line 4030
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

## `_applyFilterPillSideEffect` — function, line 4108
- **called from:**
- `static/js/emailLibrary/index.js:4108`
- `static/js/emailLibrary/index.js:4160`

## `_clearFilterPillSideEffect` — function, line 4132
- **called from:**
- `static/js/emailLibrary/index.js:4132`
- `static/js/emailLibrary/index.js:4183`

## `_addSearchPill` — function, line 4143
- **called from:**
- `static/js/emailLibrary/index.js:201`
- `static/js/emailLibrary/index.js:4143`
- `static/js/emailLibrary/index.js:4277`
- `static/js/emailLibrary/index.js:4294`
- `static/js/emailLibrary/index.js:4430`
- `static/js/emailLibrary/index.js:4480`
- `static/js/emailLibrary/index.js:4493`

## `_searchQueryFromPills` — function, line 4169
- **called from:**
- `static/js/emailLibrary/index.js:4169`
- `static/js/emailLibrary/index.js:4205`

## `_removeSearchPillAt` — function, line 4178
- **called from:**
- `static/js/emailLibrary/index.js:198`
- `static/js/emailLibrary/index.js:4084`
- `static/js/emailLibrary/index.js:4178`
- `static/js/emailLibrary/index.js:4388`

## `_renderSearchSuggestions` — function, line 4230
- **called from:**
- `static/js/emailLibrary/index.js:4230`
- `static/js/emailLibrary/index.js:4340`
- `static/js/emailLibrary/index.js:4396`
- `static/js/emailLibrary/index.js:4404`

## `esc` — arrow, line 4234
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

## `_hideSearchSuggestions` — function, line 4268
- **called from:**
- `static/js/emailLibrary/index.js:4268`
- `static/js/emailLibrary/index.js:4282`
- `static/js/emailLibrary/index.js:4307`
- `static/js/emailLibrary/index.js:4433`
- `static/js/emailLibrary/index.js:4451`

## `_acceptSuggestion` — function, line 4274
- **called from:**
- `static/js/emailLibrary/index.js:4263`
- `static/js/emailLibrary/index.js:4274`
- `static/js/emailLibrary/index.js:4412`
- `static/js/emailLibrary/index.js:4420`
- `static/js/emailLibrary/index.js:4427`

## `_initEmailSearchChipBar` — function, line 4312
- **called from:**
- `static/js/emailLibrary/index.js:2810`
- `static/js/emailLibrary/index.js:4312`

## `_ensureSuggestionCache` — arrow, line 4321
- **called from:**
- `static/js/emailLibrary/index.js:4334`

## `_refreshSuggestions` — arrow, line 4333
- **called from:**
- `static/js/emailLibrary/index.js:4360`

## `_doSearch` — function, line 4498
- **called from:**
- `static/js/emailLibrary/index.js:4211`
- `static/js/emailLibrary/index.js:4302`
- `static/js/emailLibrary/index.js:4368`
- `static/js/emailLibrary/index.js:4441`
- `static/js/emailLibrary/index.js:4498`

## `stillCurrent` — arrow, line 4531
- **called from:**
- `static/js/emailLibrary/index.js:4592`
- `static/js/emailLibrary/index.js:4651`
- `static/js/emailLibrary/index.js:4664`
- `static/js/emailLibrary/index.js:4669`
- `static/js/emailLibrary/index.js:4673`

## `searchUrl` — arrow, line 4541
- **called from:**
- `static/js/emailLibrary/index.js:4660`
- `static/js/emailLibrary/index.js:4661`

## `folderListUrl` — arrow, line 4552
- **called from:**
- `static/js/emailLibrary/index.js:4649`

## `mergeSearchResults` — arrow, line 4562
- **called from:**
- `static/js/emailLibrary/index.js:4596`

## `add` — arrow, line 4565
- **called from:**
- `companion/pairing.py:196`
- `core/database.py:554`
- `core/database.py:2269`
- `core/platform_compat.py:227`
- `core/session_manager.py:418`
- `core/session_manager.py:480`
- `core/session_manager.py:714`
- `core/session_manager.py:763`
- `core/session_manager.py:950`
- `mcp_servers/email_server.py:65`
- `mcp_servers/email_server.py:582`
- `mcp_servers/email_server.py:1027`
- `mcp_servers/email_server.py:1261`
- `mcp_servers/email_server.py:1345`
- `mcp_servers/email_server.py:2037`
- `mcp_servers/email_server.py:2224`
- `mcp_servers/email_server.py:2859`
- `mcp_servers/email_server.py:2905`
- `mcp_servers/email_server.py:2906`
- `mcp_servers/email_server.py:3075`
- `mcp_servers/email_server.py:3435`
- `mcp_servers/email_server.py:3441`
- `mcp_servers/email_server.py:3502`
- `mcp_servers/image_gen_server.py:144`
- `mcp_servers/memory_server.py:190`
- `mcp_servers/memory_server.py:219`
- `routes/api_token_routes.py:135`
- `routes/api_token_routes.py:179`
- `routes/backup_routes.py:105`
- `routes/backup_routes.py:176`
- `routes/backup_routes.py:178`
- `routes/backup_routes.py:179`
- `routes/calendar_routes.py:202`
- `routes/calendar_routes.py:330`
- `routes/calendar_routes.py:338`
- `routes/calendar_routes.py:760`
- `routes/calendar_routes.py:1390`
- `routes/calendar_routes.py:1545`
- `routes/calendar_routes.py:1612`
- `routes/calendar_routes.py:1713`
- `routes/chat_helpers.py:371`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:3606`
- `routes/chat_routes.py:3707`
- `routes/chat_routes.py:3943`
- `routes/chatgpt_subscription_routes.py:91`
- `routes/chatgpt_subscription_routes.py:155`
- `routes/chatgpt_subscription_routes.py:185`
- `routes/compare/compare_routes.py:218`
- `routes/compare/compare_routes.py:313`
- `routes/contacts/contacts_routes.py:590`
- `routes/contacts/contacts_routes.py:718`
- `routes/cookbook_routes.py:1479`
- `routes/cookbook_routes.py:1837`
- `routes/cookbook_routes.py:2885`
- `routes/cookbook_routes.py:3694`
- `routes/cookbook_routes.py:3761`
- `routes/cookbook_routes.py:3877`
- `routes/cookbook_routes.py:3964`
- `routes/copilot_routes.py:77`
- … +2020 more (grep the name in repo)

## `addIncoming` — arrow, line 4574
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `paintSearchData` — arrow, line 4591
- **called from:**
- `static/js/emailLibrary/index.js:4652`
- `static/js/emailLibrary/index.js:4666`
- `static/js/emailLibrary/index.js:4674`

## `_filterIcon` — function, line 4711
- **called from:**
- `static/js/emailLibrary/index.js:4711`
- `static/js/emailLibrary/index.js:4821`
- `static/js/emailLibrary/index.js:4850`

## `_folderIcon` — function, line 4715
- **called from:**
- `static/js/emailLibrary/index.js:4715`
- `static/js/emailLibrary/index.js:4754`
- `static/js/emailLibrary/index.js:4764`

## `_renderFolderPicker` — function, line 4744
- **called from:**
- `static/js/emailLibrary/index.js:1798`
- `static/js/emailLibrary/index.js:2688`
- `static/js/emailLibrary/index.js:3594`
- `static/js/emailLibrary/index.js:4101`
- `static/js/emailLibrary/index.js:4744`
- `static/js/emailLibrary/index.js:4790`
- `static/js/emailLibrary/index.js:4809`

## `esc` — arrow, line 4756
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

## `_initFolderPicker` — function, line 4771
- **called from:**
- `static/js/emailLibrary/index.js:2703`
- `static/js/emailLibrary/index.js:4771`

## `dismiss` — arrow, line 4778
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

## `finishClose` — arrow, line 4779
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `open` — arrow, line 4784
- **called from:**
- `app.py:1102`
- `app.py:1168`
- `app.py:1334`
- `app.py:1389`
- `companion/pairing.py:167`
- `core/atomic_io.py:38`
- `core/atomic_io.py:74`
- `core/atomic_io.py:95`
- `core/auth.py:135`
- `core/auth.py:158`
- `core/database.py:1681`
- `core/database.py:1739`
- `core/database.py:1747`
- `core/database.py:1757`
- `core/database.py:1779`
- `core/platform_compat.py:325`
- `launcher.py:92`
- `launcher.py:131`
- `mcp_servers/email_server.py:2400`
- `routes/admin_wipe/admin_wipe_routes.py:48`
- `routes/auth_routes.py:559`
- `routes/chat_helpers.py:245`
- `routes/chat_helpers.py:264`
- `routes/chat_helpers.py:282`
- `routes/chat_helpers.py:286`
- `routes/chat_helpers.py:311`
- `routes/chat_helpers.py:346`
- `routes/chat_helpers.py:349`
- `routes/chat_helpers.py:1425`
- `routes/cookbook_routes.py:749`
- `routes/diagnostics_routes.py:42`
- `routes/document/document_routes.py:1385`
- `routes/document/document_routes.py:1445`
- `routes/document/document_routes.py:1520`
- `routes/email/email_helpers.py:661`
- `routes/email/email_helpers.py:1766`
- `routes/email/email_routes.py:4974`
- `routes/email/email_routes.py:4998`
- `routes/email/email_routes.py:5005`
- `routes/email/email_routes.py:5662`
- `routes/email/email_routes.py:5686`
- `routes/gallery/gallery_helpers.py:35`
- `routes/gallery/gallery_routes.py:62`
- `routes/gallery/gallery_routes.py:303`
- `routes/gallery/gallery_routes.py:359`
- `routes/gallery/gallery_routes.py:362`
- `routes/gallery/gallery_routes.py:391`
- `routes/gallery/gallery_routes.py:967`
- `routes/gallery/gallery_routes.py:1040`
- `routes/gallery/gallery_routes.py:1855`
- `routes/gallery/gallery_routes.py:1856`
- `routes/gallery/gallery_routes.py:1980`
- `routes/gallery/gallery_routes.py:2861`
- `routes/history/history_routes.py:62`
- `routes/history/history_routes.py:88`
- `routes/history/history_routes.py:93`
- `routes/mcp/mcp_routes.py:249`
- `routes/mcp/mcp_routes.py:470`
- `routes/mcp/mcp_routes.py:586`
- `routes/mcp/mcp_routes.py:616`
- … +499 more (grep the name in repo)

## `_renderFilterPickerCurrent` — function, line 4812
- **called from:**
- `static/js/emailLibrary/index.js:772`
- `static/js/emailLibrary/index.js:2700`
- `static/js/emailLibrary/index.js:2791`
- `static/js/emailLibrary/index.js:3214`
- `static/js/emailLibrary/index.js:4010`
- `static/js/emailLibrary/index.js:4812`
- `static/js/emailLibrary/index.js:4885`

## `_initFilterPicker` — function, line 4825
- **called from:**
- `static/js/emailLibrary/index.js:2702`
- `static/js/emailLibrary/index.js:4825`

## `dismiss` — arrow, line 4855
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

## `finishClose` — arrow, line 4856
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `open` — arrow, line 4861
- **called from:**
- `app.py:1102`
- `app.py:1168`
- `app.py:1334`
- `app.py:1389`
- `companion/pairing.py:167`
- `core/atomic_io.py:38`
- `core/atomic_io.py:74`
- `core/atomic_io.py:95`
- `core/auth.py:135`
- `core/auth.py:158`
- `core/database.py:1681`
- `core/database.py:1739`
- `core/database.py:1747`
- `core/database.py:1757`
- `core/database.py:1779`
- `core/platform_compat.py:325`
- `launcher.py:92`
- `launcher.py:131`
- `mcp_servers/email_server.py:2400`
- `routes/admin_wipe/admin_wipe_routes.py:48`
- `routes/auth_routes.py:559`
- `routes/chat_helpers.py:245`
- `routes/chat_helpers.py:264`
- `routes/chat_helpers.py:282`
- `routes/chat_helpers.py:286`
- `routes/chat_helpers.py:311`
- `routes/chat_helpers.py:346`
- `routes/chat_helpers.py:349`
- `routes/chat_helpers.py:1425`
- `routes/cookbook_routes.py:749`
- `routes/diagnostics_routes.py:42`
- `routes/document/document_routes.py:1385`
- `routes/document/document_routes.py:1445`
- `routes/document/document_routes.py:1520`
- `routes/email/email_helpers.py:661`
- `routes/email/email_helpers.py:1766`
- `routes/email/email_routes.py:4974`
- `routes/email/email_routes.py:4998`
- `routes/email/email_routes.py:5005`
- `routes/email/email_routes.py:5662`
- `routes/email/email_routes.py:5686`
- `routes/gallery/gallery_helpers.py:35`
- `routes/gallery/gallery_routes.py:62`
- `routes/gallery/gallery_routes.py:303`
- `routes/gallery/gallery_routes.py:359`
- `routes/gallery/gallery_routes.py:362`
- `routes/gallery/gallery_routes.py:391`
- `routes/gallery/gallery_routes.py:967`
- `routes/gallery/gallery_routes.py:1040`
- `routes/gallery/gallery_routes.py:1855`
- `routes/gallery/gallery_routes.py:1856`
- `routes/gallery/gallery_routes.py:1980`
- `routes/gallery/gallery_routes.py:2861`
- `routes/history/history_routes.py:62`
- `routes/history/history_routes.py:88`
- `routes/history/history_routes.py:93`
- `routes/mcp/mcp_routes.py:249`
- `routes/mcp/mcp_routes.py:470`
- `routes/mcp/mcp_routes.py:586`
- `routes/mcp/mcp_routes.py:616`
- … +499 more (grep the name in repo)

## `_renderEmailLoading` — function, line 4888
- **called from:**
- `static/js/emailLibrary/index.js:1770`
- `static/js/emailLibrary/index.js:3092`
- `static/js/emailLibrary/index.js:4888`
- `static/js/emailLibrary/index.js:5118`
- `static/js/emailLibrary/index.js:5362`

## `_emailReaderSkeletonHtml` — function, line 4908
- **called from:**
- `static/js/emailLibrary/index.js:4908`
- `static/js/emailLibrary/index.js:5996`
- `static/js/emailLibrary/reader.js:298`
- `static/js/emailLibrary/reader.js:447`

## `_appendEmailSearchProgressRow` — function, line 4941
- **called from:**
- `static/js/emailLibrary/index.js:4941`
- `static/js/emailLibrary/index.js:5429`

## `_refreshUnreadBadge` — function, line 4958
- **called from:**
- `static/js/emailLibrary/index.js:2553`
- `static/js/emailLibrary/index.js:3107`
- `static/js/emailLibrary/index.js:3219`
- `static/js/emailLibrary/index.js:4958`
- `static/js/emailLibrary/index.js:5169`
- `static/js/emailLibrary/index.js:5171`
- `static/js/emailLibrary/settingsPage.js:753`

## `_loadEmails` — function, line 5031
- **called from:**
- `static/js/emailLibrary/index.js:1587`
- `static/js/emailLibrary/index.js:1801`
- `static/js/emailLibrary/index.js:1814`
- `static/js/emailLibrary/index.js:3100`
- `static/js/emailLibrary/index.js:3111`
- `static/js/emailLibrary/index.js:4202`
- `static/js/emailLibrary/index.js:4222`
- `static/js/emailLibrary/index.js:4380`
- `static/js/emailLibrary/index.js:4510`
- `static/js/emailLibrary/index.js:5031`
- `static/js/emailLibrary/index.js:5247`
- `static/js/emailLibrary/settingsPage.js:574`

## `paintData` — arrow, line 5069
- **called from:**
- `static/js/emailLibrary/index.js:5109`
- `static/js/emailLibrary/index.js:5146`
- `static/js/emailLibrary/index.js:5167`

## `_loadScheduled` — function, line 5190
- **called from:**
- `static/js/emailLibrary/index.js:5124`
- `static/js/emailLibrary/index.js:5190`

## `_emailDateBucketLabel` — function, line 5259
- **called from:**
- `static/js/emailLibrary/index.js:5259`
- `static/js/emailLibrary/index.js:5321`
- `static/js/emailLibrary/index.js:5415`

## `dayStart` — arrow, line 5263
- **called from:**
- `static/js/emailLibrary/index.js:5265`
- `static/js/emailLibrary/index.js:5266`
- `static/js/sessions.js:1411`
- `static/js/sessions.js:1412`

## `_createEmailDateHeader` — function, line 5281
- **called from:**
- `static/js/emailLibrary/index.js:5281`
- `static/js/emailLibrary/index.js:5422`

## `_emailTimelineGapThreshold` — function, line 5291
- **called from:**
- `static/js/emailLibrary/index.js:5291`
- `static/js/emailLibrary/index.js:5412`

## `_dateGroupEmailsWithPinned` — function, line 5305
- **called from:**
- `static/js/emailLibrary/index.js:5305`
- `static/js/emailLibrary/index.js:5353`

## `priority` — arrow, line 5309
- **called from:**
- `static/js/emailLibrary/index.js:5316`
- `static/js/emailLibrary/index.js:5316`

## `flushGroup` — arrow, line 5313
- **called from:**
- `static/js/emailLibrary/index.js:5323`
- `static/js/emailLibrary/index.js:5328`

## `_renderGrid` — function, line 5332
- **called from:**
- `static/js/emailLibrary/index.js:1022`
- `static/js/emailLibrary/index.js:1738`
- `static/js/emailLibrary/index.js:1754`
- `static/js/emailLibrary/index.js:1762`
- `static/js/emailLibrary/index.js:2934`
- `static/js/emailLibrary/index.js:2943`
- `static/js/emailLibrary/index.js:2954`
- `static/js/emailLibrary/index.js:3008`
- `static/js/emailLibrary/index.js:3078`
- `static/js/emailLibrary/index.js:3933`
- `static/js/emailLibrary/index.js:3957`
- `static/js/emailLibrary/index.js:4513`
- `static/js/emailLibrary/index.js:4529`
- `static/js/emailLibrary/index.js:4628`
- `static/js/emailLibrary/index.js:5081`
- `static/js/emailLibrary/index.js:5114`
- `static/js/emailLibrary/index.js:5332`
- `static/js/emailLibrary/index.js:5651`
- `static/js/emailLibrary/index.js:5662`
- `static/js/emailLibrary/menus.js:82`
- `static/js/emailLibrary/menus.js:151`
- `static/js/emailLibrary/menus.js:158`
- `static/js/emailLibrary/menus.js:164`
- `static/js/emailLibrary/menus.js:170`
- `static/js/emailLibrary/menus.js:193`
- `static/js/emailLibrary/menus.js:443`
- `static/js/emailLibrary/menus.js:448`
- `static/js/emailLibrary/menus.js:460`
- `static/js/emailLibrary/menus.js:471`
- `static/js/emailLibrary/menus.js:476`
- `static/js/emailLibrary/menus.js:488`
- `static/js/emailLibrary/menus.js:507`
- `static/js/emailLibrary/menus.js:530`
- `static/js/emailLibrary/menus.js:656`
- `static/js/emailLibrary/menus.js:707`
- `static/js/emailLibrary/menus.js:897`
- `static/js/emailLibrary/settingsPage.js:638`
- `static/js/emailLibrary/unsubscribe.js:468`
- `static/js/emailLibrary/unsubscribe.js:573`
- `static/js/emailLibrary/unsubscribe.js:642`
- `static/js/gallery.js:234`
- `static/js/gallery.js:1403`
- `static/js/gallery.js:2117`
- `static/js/gallery.js:3087`
- `static/js/gallery.js:3152`
- `static/js/gallery.js:3249`

## `after` — class, line 5406
- **called from:**
- `launcher.py:127`
- `static/js/cookbook-diagnosis.js:924`
- `static/js/document.js:7739`
- `static/js/document.js:7741`
- `static/js/document.js:7822`
- `static/js/document.js:7823`
- `static/js/document.js:9877`
- `static/js/document.js:11959`
- `static/js/document.js:11960`
- `static/js/document.js:14530`
- `static/js/document.js:16366`
- `static/js/editor/build/right-panel.js:103`
- `static/js/features/notes/ui/editor.js:304`
- `static/js/skills.js:1328`
- `static/js/slashCommands.js:4313`

## `_createCard` — function, line 5448
- **called from:**
- `static/js/emailLibrary/index.js:5425`
- `static/js/emailLibrary/index.js:5448`

## `_toggleDone` — arrow, line 5597
- **called from:**
- `static/js/emailInbox.js:1386`

## `as` — class, line 5599
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_cancelHold` — arrow, line 5748
- **called from:**
- `static/js/emailLibrary/index.js:5772`

## `_findSiblingEmailCard` — function, line 5810
- **called from:**
- `static/js/emailLibrary/index.js:1005`
- `static/js/emailLibrary/index.js:1005`
- `static/js/emailLibrary/index.js:5696`
- `static/js/emailLibrary/index.js:5810`
- `static/js/emailLibrary/index.js:5822`
- `static/js/emailLibrary/index.js:5823`
- `static/js/emailLibrary/menus.js:78`
- `static/js/emailLibrary/menus.js:78`

## `_syncCardNavArrows` — function, line 5819
- **called from:**
- `static/js/emailLibrary/index.js:5819`
- `static/js/emailLibrary/index.js:6132`

## `_openDraftInComposer` — function, line 5826
- **called from:**
- `static/js/emailLibrary/index.js:5797`
- `static/js/emailLibrary/index.js:5826`

## `_prefetchAdjacentEmails` — function, line 5841
- **called from:**
- `static/js/emailLibrary/index.js:5841`

## `_emFold` — arrow, line 5860
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_toggleCardPreview` — function, line 5877
- **called from:**
- `static/js/emailLibrary/index.js:1030`
- `static/js/emailLibrary/index.js:2676`
- `static/js/emailLibrary/index.js:4290`
- `static/js/emailLibrary/index.js:5442`
- `static/js/emailLibrary/index.js:5700`
- `static/js/emailLibrary/index.js:5701`
- `static/js/emailLibrary/index.js:5804`
- `static/js/emailLibrary/index.js:5877`
- `static/js/emailLibrary/index.js:5970`
- `static/js/emailLibrary/index.js:6005`
- `static/js/emailLibrary/menus.js:90`
- `static/js/emailLibrary/menus.js:387`

## `isCurrentOpen` — arrow, line 5898
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

## `restoreUnreadState` — arrow, line 5942
- **called from:**
- `static/js/emailLibrary/index.js:6018`
- `static/js/emailLibrary/index.js:6030`
- `static/js/emailLibrary/index.js:6217`

## `commitReadState` — arrow, line 5947
- **called from:**
- `static/js/emailLibrary/index.js:6033`

## `showFailedReader` — arrow, line 5999
- **called from:**
- `static/js/emailLibrary/index.js:6019`
- `static/js/emailLibrary/index.js:6219`

## `buildRecipients` — arrow, line 6059
- **called from:**
- `static/js/emailLibrary/index.js:6080`
- `static/js/emailLibrary/index.js:6081`

## `findHScroller` — arrow, line 6145
- **called from:**
- `static/js/emailLibrary/index.js:6157`

## `_summaryCollapsedPref` — function, line 6229
- **called from:**
- `static/js/emailLibrary/index.js:6229`
- `static/js/emailLibrary/index.js:6242`
- `static/js/emailLibrary/reader.js:615`

## `_setSummaryCollapsedPref` — function, line 6232
- **called from:**
- `static/js/emailLibrary/index.js:6232`
- `static/js/emailLibrary/index.js:6257`
- `static/js/emailLibrary/reader.js:621`

## `_showCachedSummary` — function, line 6236
- **called from:**
- `static/js/emailLibrary/index.js:6210`
- `static/js/emailLibrary/index.js:6236`

## `_flip` — arrow, line 6255
- **called from:**
- `static/js/emailLibrary/index.js:6260`
- `static/js/emailLibrary/index.js:6262`

## `_translateEmail` — function, line 6273
- **called from:**
- `static/js/emailLibrary/aiReply.js:264`
- `static/js/emailLibrary/aiReply.js:290`
- `static/js/emailLibrary/index.js:6273`

## `flip` — arrow, line 6301
- **called from:**
- `static/js/emailLibrary/index.js:6302`
- `static/js/emailLibrary/index.js:6304`

## `_maybeAutoTranslateEmail` — function, line 6344
- **called from:**
- `static/js/emailLibrary/index.js:6104`
- `static/js/emailLibrary/index.js:6344`
- `static/js/emailLibrary/reader.js:354`
- `static/js/emailLibrary/reader.js:512`

## `_fitEmailDropdown` — function, line 6351
- **called from:**
- `static/js/emailLibrary/index.js:6351`
- `static/js/emailLibrary/menus.js:350`
- `static/js/emailLibrary/menus.js:572`
- `static/js/emailLibrary/menus.js:635`
- `static/js/emailLibrary/menus.js:660`

## `_fitReaderActions` — function, line 6383
- **called from:**
- `static/js/emailLibrary/index.js:6383`
- `static/js/emailLibrary/index.js:6403`
- `static/js/emailLibrary/index.js:6410`

## `_wireReaderActionOverflow` — function, line 6407
- **called from:**
- `static/js/emailLibrary/index.js:6130`
- `static/js/emailLibrary/index.js:6407`
- `static/js/emailLibrary/reader.js:375`
- `static/js/emailLibrary/reader.js:533`
