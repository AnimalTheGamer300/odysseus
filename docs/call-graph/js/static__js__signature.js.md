# `static/js/signature.js` — definitions & call sites

34 definitions (regex-based, best-effort).
**Exports:** `capture`, `default`, `getLastUsed`, `pick`, `setLastUsed`

## `_esc` — function, line 17
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
- `static/js/chat.js:4679`
- `static/js/chat.js:4679`
- `static/js/cookbookServe.js:4003`
- `static/js/cookbookServe.js:4005`
- `static/js/document.js:313`
- `static/js/document.js:314`
- `static/js/document.js:8382`
- `static/js/document.js:8966`
- `static/js/documentLibrary.js:70`
- `static/js/documentLibrary.js:86`
- `static/js/documentLibrary.js:582`
- `static/js/documentLibrary.js:586`
- `static/js/documentLibrary.js:588`
- `static/js/documentLibrary.js:1957`
- `static/js/documentLibrary.js:1962`
- `static/js/documentLibrary.js:2110`
- `static/js/documentLibrary.js:2466`
- `static/js/documentLibrary.js:2510`
- `static/js/documentLibrary.js:2547`
- `static/js/documentLibrary.js:2696`
- `static/js/documentLibrary.js:2737`
- `static/js/documentLibrary.js:2750`
- `static/js/documentLibrary.js:2904`
- `static/js/emailInbox.js:75`
- `static/js/emailInbox.js:75`
- `static/js/emailInbox.js:75`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:524`
- … +188 more (grep the name in repo)

## `_safeSignatureDataUrl` — function, line 26
- **called from:**
- `static/js/signature.js:26`
- `static/js/signature.js:464`
- `static/js/signature.js:498`

## `getLastUsed` — function, line 35
- **called from:**
- `static/js/document.js:820`
- `static/js/signature.js:35`

## `setLastUsed` — function, line 36
- **called from:**
- `static/js/signature.js:36`
- `static/js/signature.js:449`
- `static/js/signature.js:501`
- `static/js/signature.js:518`

## `SmoothPad` — class, line 38
- **called from:**
- `static/js/signature.js:408`

## `constructor` — method?, line 39
- **called from:**
- `static/js/signature.js:39`
- `static/js/spinner.js:15`
- `static/js/tts-ai.js:7`

## `_wirePointer` — method?, line 65
- **called from:**
- `static/js/signature.js:61`
- `static/js/signature.js:65`

## `_toLocal` — method?, line 75
- **called from:**
- `static/js/signature.js:75`
- `static/js/signature.js:90`
- `static/js/signature.js:100`

## `_onDown` — method?, line 87
- **called from:**
- `static/js/signature.js:68`
- `static/js/signature.js:87`

## `_onMove` — method?, line 97
- **called from:**
- `static/js/signature.js:69`
- `static/js/signature.js:97`
- `static/js/windowDrag.js:287`
- `static/js/windowDrag.js:319`

## `_onUp` — method?, line 125
- **called from:**
- `static/js/signature.js:70`
- `static/js/signature.js:71`
- `static/js/signature.js:72`
- `static/js/signature.js:125`

## `_repaintAll` — method?, line 138
- **called from:**
- `static/js/signature.js:134`
- `static/js/signature.js:138`
- `static/js/signature.js:264`
- `static/js/signature.js:375`

## `_chaikinPass` — method?, line 147
- **called from:**
- `static/js/signature.js:147`
- `static/js/signature.js:179`

## `_drawStrokeSmooth` — method?, line 169
- **called from:**
- `static/js/signature.js:143`
- `static/js/signature.js:169`

## `_widthBetween` — method?, line 209
- **called from:**
- `static/js/signature.js:121`
- `static/js/signature.js:172`
- `static/js/signature.js:200`
- `static/js/signature.js:209`
- `static/js/signature.js:238`

## `_strokeLine` — method?, line 222
- **called from:**
- `static/js/signature.js:121`
- `static/js/signature.js:172`
- `static/js/signature.js:222`

## `_drawSegment` — method?, line 234
- **called from:**
- `static/js/signature.js:118`
- `static/js/signature.js:234`

## `clear` — method?, line 250
- **called from:**
- `app.py:334`
- `routes/admin_wipe/admin_wipe_routes.py:84`
- `routes/admin_wipe/admin_wipe_routes.py:101`
- `routes/email_routes.py:1643`
- `routes/model_routes.py:1394`
- `routes/session_routes.py:832`
- `routes/skills_routes.py:462`
- `scripts/diffusion_server.py:101`
- `services/search/core.py:228`
- `src/agent_jobs.py:108`
- `src/agent_jobs.py:119`
- `src/agent_jobs.py:120`
- `src/email_thread_parser.py:318`
- `src/llm_core.py:126`
- `src/llm_core.py:141`
- `src/llm_core.py:4084`
- `src/task_scheduler.py:441`
- `tests/test_api_token_routes.py:160`
- `tests/test_budget_auto_sentinel.py:72`
- `tests/test_budget_auto_sentinel.py:75`
- `tests/test_budget_auto_sentinel.py:80`
- `tests/test_caldav_writeback_route.py:104`
- `tests/test_companion_pairing.py:28`
- `tests/test_context_cache_per_endpoint.py:17`
- `tests/test_email_urgency_checkpoint.py:854`
- `tests/test_hwfit_cpu_arch_detection.py:10`
- `tests/test_hwfit_cpu_arch_detection.py:15`
- `tests/test_hwfit_remote_validation.py:79`
- `tests/test_hwfit_remote_validation.py:89`
- `tests/test_hwfit_unified_nvidia.py:113`
- `tests/test_hwfit_unified_nvidia.py:142`
- `tests/test_kimi_code_user_agent.py:63`
- `tests/test_kimi_code_user_agent.py:68`
- `tests/test_kimi_code_user_agent.py:79`
- `tests/test_kimi_code_user_agent.py:94`
- `tests/test_kimi_code_user_agent.py:98`
- `tests/test_kimi_code_user_agent.py:132`
- `tests/test_kimi_code_user_agent.py:136`
- `tests/test_kimi_code_user_agent.py:167`
- `tests/test_kimi_code_user_agent.py:171`
- `tests/test_kimi_code_user_agent.py:212`
- `tests/test_llm_core_async_mistral_content.py:36`
- `tests/test_llm_core_fallback.py:503`
- `tests/test_llm_core_fallback.py:537`
- `tests/test_llm_core_fallback.py:787`
- `tests/test_llm_core_fallback.py:788`
- `tests/test_llm_core_fallback.py:824`
- `tests/test_llm_core_fallback.py:825`
- `tests/test_llm_core_ollama.py:91`
- `tests/test_llm_core_temperature_moonshot.py:59`
- `tests/test_llm_core_temperature_reasoning.py:39`
- `tests/test_lmstudio_vision.py:35`
- `tests/test_lmstudio_vision.py:37`
- `tests/test_lmstudio_vision.py:131`
- `tests/test_lmstudio_vision.py:133`
- `tests/test_mcp_email_decode_header_spaces.py:23`
- `tests/test_mcp_email_decode_header_spaces.py:25`
- `tests/test_mcp_email_decode_header_spaces.py:98`
- `tests/test_mcp_email_decode_header_spaces.py:112`
- `tests/test_mcp_email_decode_header_spaces.py:170`
- … +105 more (grep the name in repo)

## `undo` — method?, line 261
- **called from:**
- `tests/test_db_stubs_helper.py:67`
- `tests/test_db_stubs_helper.py:82`
- `tests/test_db_stubs_helper.py:99`
- `tests/test_db_stubs_helper.py:118`
- `tests/test_review_regressions.py:1297`
- `static/js/editor/history-panel.js:29`
- `static/js/editor/keyboard-shortcuts.js:10`
- `static/js/editor/keyboard-shortcuts.js:88`
- `static/js/editor/tools/transform-session.js:9`
- `static/js/editor/tools/transform-session.js:370`
- `static/js/galleryEditor.js:1352`
- `static/js/signature.js:261`
- `static/js/signature.js:429`

## `isEmpty` — method?, line 268
- **called from:**
- `static/js/signature.js:268`
- `static/js/signature.js:420`

## `toTrimmedDataUrl` — method?, line 272
- **called from:**
- `static/js/signature.js:272`
- `static/js/signature.js:435`

## `_modal` — function, line 318
- **called from:**
- `static/js/signature.js:318`
- `static/js/signature.js:382`
- `static/js/signature.js:475`

## `_listSignatures` — function, line 328
- **called from:**
- `static/js/signature.js:328`
- `static/js/signature.js:462`

## `_saveSignature` — function, line 335
- **called from:**
- `static/js/signature.js:335`
- `static/js/signature.js:436`

## `_deleteSignature` — function, line 348
- **called from:**
- `static/js/signature.js:348`
- `static/js/signature.js:511`

## `_loadSmoothness` — function, line 355
- **called from:**
- `static/js/signature.js:355`
- `static/js/signature.js:381`

## `_saveSmoothness` — function, line 359
- **called from:**
- `static/js/signature.js:359`
- `static/js/signature.js:414`

## `_smoothnessToParams` — function, line 362
- **called from:**
- `static/js/signature.js:362`
- `static/js/signature.js:371`
- `static/js/signature.js:408`

## `_applySmoothness` — function, line 370
- **called from:**
- `static/js/signature.js:370`
- `static/js/signature.js:415`

## `capture` — function, line 379
- **called from:**
- `tests/test_ai_interaction_owner_scope.py:52`
- `tests/test_ai_interaction_owner_scope.py:57`
- `static/js/signature.js:4`
- `static/js/signature.js:379`
- `static/js/signature.js:517`

## `refreshSaveBtn` — arrow, line 420
- **called from:**
- `static/js/signature.js:428`
- `static/js/signature.js:429`

## `close` — arrow, line 425
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

## `pick` — function, line 460
- **called from:**
- `static/js/document.js:811`
- `static/js/document.js:1260`
- `static/js/document.js:1527`
- `static/js/emailLibrary.js:3544`
- `static/js/emailLibrary.js:3545`
- `static/js/emailLibrary.js:3546`
- `static/js/researchSynapse.js:21`
- `static/js/signature.js:5`
- `static/js/signature.js:460`
- `static/js/slashCommands.js:1261`

## `close` — arrow, line 488
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
