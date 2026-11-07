# `static/js/memory.js` — definitions & call sites

57 definitions (regex-based, best-effort).
**Exports:** `addNewMemory`, `default`, `deleteMemory`, `editMemory`, `exportMemories`, `extractMemory`, `importMemories`, `loadMemories`, `openMemory`, `openMemoryModal`, `renderMemoryList`, `tidyMemories`, `updateMemoryCount`

## `_memorySortIcon` — function, line 36
- **called from:**
- `static/js/memory.js:36`
- `static/js/memory.js:49`
- `static/js/memory.js:67`

## `_renderMemorySortPickerCurrent` — function, line 40
- **called from:**
- `static/js/memory.js:40`
- `static/js/memory.js:93`
- `static/js/memory.js:99`

## `_initMemorySortPicker` — function, line 53
- **called from:**
- `static/js/memory.js:53`
- `static/js/memory.js:1630`

## `unregister` — arrow, line 72
- **called from:**
- `static/js/document.js:1061`
- `static/js/document.js:7400`
- `static/js/document.js:11850`
- `static/js/document.js:11891`
- `static/js/document.js:12254`
- `static/js/editor/fx/adj-popup.js:264`
- `static/js/editor/fx/adj-popup.js:304`
- `static/js/editor/history-panel.js:74`
- `static/js/features/notes/ui/panel.js:51`
- `static/js/features/notes/ui/panel.js:330`
- `static/js/galleryEditor.js:14176`
- `static/js/galleryEditor.js:14192`
- `static/js/memory.js:76`
- `static/js/modalManager.js:1216`
- `static/js/research/panel.js:1112`
- `static/js/research/panel.js:1429`
- `static/js/research/panel.js:1506`
- `static/js/sessions.js:3401`
- `static/js/tourHintDismiss.js:15`

## `close` — arrow, line 73
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

## `open` — arrow, line 79
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

## `_ensureNewMemoryCategorySelect` — function, line 102
- **called from:**
- `static/js/memory.js:102`
- `static/js/memory.js:116`
- `static/js/memory.js:479`

## `_readNewMemoryCategory` — function, line 115
- **called from:**
- `static/js/memory.js:115`
- `static/js/memory.js:1247`

## `_wireMemoryDrag` — function, line 123
- **called from:**
- `static/js/memory.js:123`
- `static/js/memory.js:1605`

## `relativeTime` — function, line 150
- **called from:**
- `static/js/memory.js:150`
- `static/js/memory.js:899`

## `buildCategoryChips` — function, line 162
- **called from:**
- `static/js/memory.js:162`
- `static/js/memory.js:490`
- `static/js/memory.js:508`
- `static/js/memory.js:515`
- `static/js/memory.js:672`

## `syncToggles` — function, line 201
- **called from:**
- `static/js/memory.js:201`
- `static/js/memory.js:493`
- `static/js/memory.js:520`

## `applyDim` — arrow, line 234
- **called from:**
- `static/js/memory.js:238`

## `_applyMemoryModalMode` — function, line 246
- **called from:**
- `static/js/memory.js:246`
- `static/js/memory.js:267`

## `openMemoryModal` — function, line 263
- **called from:**
- `static/app.js:1730`
- `static/app.js:1743`
- `static/js/memory.js:263`
- `static/js/memory.js:304`
- `static/js/memory.js:1399`
- `static/js/memory.js:1583`

## `_decodeMemoryAnchorId` — function, line 285
- **called from:**
- `static/js/memory.js:285`
- `static/js/memory.js:306`

## `_resetMemoryDeepLinkFilters` — function, line 290
- **called from:**
- `static/js/memory.js:290`
- `static/js/memory.js:303`

## `openMemory` — function, line 302
- **called from:**
- `static/js/memory.js:302`
- `static/js/memory.js:313`

## `reflectMemoryToggleInSidebar` — function, line 321
- **called from:**
- `static/js/memory.js:220`
- `static/js/memory.js:225`
- `static/js/memory.js:321`

## `reflectSkillsToggleInSidebar` — function, line 331
- **called from:**
- `static/js/memory.js:236`
- `static/js/memory.js:331`

## `syncToggleDim` — function, line 338
- **called from:**
- `static/js/memory.js:338`
- `static/js/memory.js:449`
- `static/js/memory.js:453`
- `static/js/memory.js:463`
- `static/js/memory.js:471`

## `syncPrefSlider` — function, line 353
- **called from:**
- `static/js/memory.js:212`
- `static/js/memory.js:353`

## `fmt` — arrow, line 358
- **called from:**
- `static/js/emailLibrary/bodyRender.js:151`
- `static/js/emailLibrary/bodyRender.js:155`
- `static/js/emailLibrary/bodyRender.js:158`
- `static/js/emailLibrary/bodyRender.js:777`
- `static/js/emailLibrary/bodyRender.js:785`
- `static/js/emailLibrary/bodyRender.js:787`
- `static/js/memory.js:372`
- `static/js/memory.js:375`

## `syncPrefNumber` — function, line 396
- **called from:**
- `static/js/memory.js:213`
- `static/js/memory.js:396`

## `clamp` — arrow, line 399
- **called from:**
- `static/js/colorPicker.js:19`
- `static/js/colorPicker.js:31`
- `static/js/colorPicker.js:100`
- `static/js/colorPicker.js:366`
- `static/js/colorPicker.js:367`
- `static/js/colorPicker.js:374`
- `static/js/editor/canvas-context-menu.js:228`
- `static/js/editor/canvas-context-menu.js:229`
- `static/js/editor/canvas-context-menu.js:250`
- `static/js/editor/canvas-context-menu.js:259`
- `static/js/editor/filters/dehaze.js:23`
- `static/js/editor/filters/dehaze.js:120`
- `static/js/editor/filters/dehaze.js:122`
- `static/js/editor/filters/dehaze.js:127`
- `static/js/editor/filters/dehaze.js:200`
- `static/js/editor/filters/dehaze.js:206`
- `static/js/editor/filters/dehaze.js:232`
- `static/js/editor/filters/dehaze.js:233`
- `static/js/editor/filters/dehaze.js:234`
- `static/js/editor/tools/perspective-crop.js:11`
- `static/js/editor/tools/perspective-crop.js:32`
- `static/js/editor/tools/perspective-crop.js:33`
- `static/js/editor/transform-frame-geometry.js:223`
- `static/js/editor/transform-frame-geometry.js:225`
- `static/js/editor/transform-frame-geometry.js:268`
- `static/js/editor/transform-frame-geometry.js:268`
- `static/js/galleryEditor.js:7986`
- `static/js/galleryEditor.js:7987`
- `static/js/galleryEditor.js:7988`
- `static/js/galleryEditor.js:7989`
- `static/js/galleryEditor.js:7996`
- `static/js/memory.js:411`
- `static/js/memory.js:419`

## `syncPrefToggle` — function, line 437
- **called from:**
- `static/js/memory.js:204`
- `static/js/memory.js:208`
- `static/js/memory.js:209`
- `static/js/memory.js:210`
- `static/js/memory.js:211`
- `static/js/memory.js:437`

## `loadMemories` — function, line 478
- **called from:**
- `static/app.js:4483`
- `static/js/memory.js:282`
- `static/js/memory.js:478`
- `static/js/memory.js:603`
- `static/js/memory.js:1203`
- `static/js/memory.js:1268`
- `static/js/memory.js:1322`
- `static/js/memory.js:1523`
- `static/js/memory.js:1669`
- `static/js/sessions.js:2614`

## `enterSelectMode` — function, line 528
- **called from:**
- `static/js/memory.js:528`
- `static/js/memory.js:959`
- `static/js/memory.js:1638`

## `exitSelectMode` — function, line 539
- **called from:**
- `static/js/memory.js:539`
- `static/js/memory.js:602`
- `static/js/memory.js:804`
- `static/js/memory.js:1637`

## `toggleSelectItem` — function, line 551
- **called from:**
- `static/js/memory.js:551`
- `static/js/memory.js:845`

## `updateBulkCount` — function, line 560
- **called from:**
- `static/js/memory.js:535`
- `static/js/memory.js:557`
- `static/js/memory.js:560`
- `static/js/memory.js:578`
- `static/js/memory.js:961`

## `toggleSelectAll` — function, line 567
- **called from:**
- `static/js/memory.js:567`

## `bulkDelete` — function, line 582
- **called from:**
- `static/js/memory.js:582`

## `tidyMemories` — function, line 609
- **called from:**
- `static/js/memory.js:609`

## `sleep` — function, line 691
- **called from:**
- `app.py:1320`
- `app.py:1324`
- `app.py:1422`
- `app.py:1427`
- `core/session_manager.py:66`
- `launcher.py:121`
- `routes/chat_helpers.py:821`
- `routes/chat_helpers.py:825`
- `routes/chat_helpers.py:2033`
- `routes/chat_helpers.py:2041`
- `routes/chat_routes.py:4254`
- `routes/cookbook_routes.py:1593`
- `routes/email/email_pollers.py:1514`
- `routes/email/email_pollers.py:1577`
- `routes/email/email_pollers.py:1707`
- `routes/email/email_routes.py:4073`
- `routes/email/email_routes.py:4086`
- `routes/research/research_routes.py:706`
- `routes/session_routes.py:351`
- `routes/shell_routes.py:1067`
- `routes/shell_routes.py:1084`
- `routes/shell_routes.py:1163`
- `routes/shell_routes.py:1181`
- `routes/upload_routes.py:642`
- `scripts/audit_email_sft_with_deepseek.py:270`
- `scripts/audit_email_sft_with_deepseek.py:281`
- `scripts/audit_sft_corpus_with_deepseek.py:304`
- `scripts/backfill_model_release_dates.py:112`
- `scripts/dump_agent_prompt.py:414`
- `scripts/eval_followup_domain_continuity.py:156`
- `scripts/eval_followup_domain_continuity.py:173`
- `scripts/generate_sft_environment_expansion.py:199`
- `scripts/generate_sft_flow_variants_with_kimi.py:101`
- `scripts/import_from_vllm_recipes.py:299`
- `scripts/import_from_vllm_recipes.py:327`
- `scripts/odysseus_conversation_qa.py:388`
- `scripts/odysseus_conversation_qa.py:732`
- `scripts/odysseus_related_flow_audit.py:568`
- `scripts/repair_email_sft_with_kimi.py:230`
- `scripts/repair_sft_corpus_with_kimi.py:209`
- `scripts/run_odysseus_search_teacher_pipeline.py:170`
- `scripts/run_sft_overnight_fixture_flows.py:796`
- `scripts/verify_notes_browser_runtime.py:87`
- `services/memory/skill_importer.py:162`
- `services/youtube/youtube_handler.py:156`
- `src/agent_jobs.py:355`
- `src/agent_runs.py:90`
- `src/agent_tools/subprocess_tools.py:756`
- `src/ai_interaction.py:1767`
- `src/ai_interaction.py:2085`
- `src/background_tool_jobs.py:193`
- `src/bg_monitor.py:237`
- `src/builtin_mcp.py:205`
- `src/clean_agent_preview.py:5591`
- `src/containment.py:1156`
- `src/containment.py:1242`
- `src/containment.py:1525`
- `src/cookbook_serve_lifecycle.py:193`
- `src/cookbook_serve_lifecycle.py:199`
- `src/email_calendar_import.py:47`
- … +148 more (grep the name in repo)

## `animateMemoryRemoval` — function, line 695
- **called from:**
- `static/js/memory.js:601`
- `static/js/memory.js:695`
- `static/js/memory.js:1321`

## `animateTidyDiff` — function, line 709
- **called from:**
- `static/js/memory.js:668`
- `static/js/memory.js:709`

## `getFilteredMemories` — function, line 760
- **called from:**
- `static/js/memory.js:573`
- `static/js/memory.js:716`
- `static/js/memory.js:760`
- `static/js/memory.js:798`

## `renderMemoryList` — function, line 791
- **called from:**
- `static/app.js:707`
- `static/app.js:1733`
- `static/app.js:1759`
- `static/js/memory.js:194`
- `static/js/memory.js:270`
- `static/js/memory.js:305`
- `static/js/memory.js:481`
- `static/js/memory.js:491`
- `static/js/memory.js:509`
- `static/js/memory.js:516`
- `static/js/memory.js:536`
- `static/js/memory.js:548`
- `static/js/memory.js:579`
- `static/js/memory.js:673`
- `static/js/memory.js:791`
- `static/js/memory.js:962`
- `static/js/memory.js:1161`
- `static/js/memory.js:1177`
- `static/js/memory.js:1189`
- `static/js/memory.js:1300`
- `static/js/memory.js:1627`
- `static/js/presets.js:1054`

## `_onTS` — arrow, line 1040
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_onTM` — arrow, line 1046
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_onTE` — arrow, line 1057
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_lpCancel` — arrow, line 1084
- **called from:**
- `static/js/cookbookRunning.js:2644`
- `static/js/memory.js:1098`
- `static/js/skills.js:1075`

## `closeDropdown` — arrow, line 1106
- **called from:**
- `static/js/cookbookServe.js:1300`
- `static/js/cookbookServe.js:1348`
- `static/js/memory.js:1111`

## `onOutsideClick` — arrow, line 1110
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `startInlineEdit` — function, line 1124
- **called from:**
- `static/js/memory.js:915`
- `static/js/memory.js:944`
- `static/js/memory.js:1124`

## `saveInlineEdit` — function, line 1182
- **called from:**
- `static/js/memory.js:1156`
- `static/js/memory.js:1173`
- `static/js/memory.js:1182`
- `static/js/memory.js:1288`

## `updateMemoryCount` — function, line 1215
- **called from:**
- `static/app.js:1734`
- `static/app.js:1760`
- `static/js/memory.js:195`
- `static/js/memory.js:271`
- `static/js/memory.js:482`
- `static/js/memory.js:492`
- `static/js/memory.js:510`
- `static/js/memory.js:517`
- `static/js/memory.js:674`
- `static/js/memory.js:1215`
- `static/js/presets.js:1055`

## `addNewMemory` — function, line 1244
- **called from:**
- `static/app.js:1772`
- `static/app.js:1778`
- `static/js/memory.js:1244`

## `editMemory` — function, line 1281
- **called from:**
- `static/js/memory.js:1281`

## `togglePin` — function, line 1291
- **called from:**
- `static/js/features/notes/application/cardOperations.js:10`
- `static/js/features/notes/ui/cardInteractions.js:152`
- `static/js/memory.js:939`
- `static/js/memory.js:1291`

## `deleteMemory` — function, line 1309
- **called from:**
- `static/js/memory.js:949`
- `static/js/memory.js:1309`

## `extractMemory` — function, line 1332
- **called from:**
- `static/js/memory.js:1332`

## `exportMemories` — function, line 1404
- **called from:**
- `static/js/memory.js:1404`

## `importMemories` — function, line 1422
- **called from:**
- `static/js/memory.js:1422`

## `handleImportFile` — function, line 1428
- **called from:**
- `static/js/memory.js:1428`
- `static/js/memory.js:1665`

## `updateHeaderTitle` — arrow, line 1489
- **called from:**
- `static/js/memory.js:1493`
- `static/js/memory.js:1561`
- `static/js/memory.js:1572`
