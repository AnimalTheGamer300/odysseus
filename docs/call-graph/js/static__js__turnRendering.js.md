# `static/js/turnRendering.js` — definitions & call sites

13 definitions (regex-based, best-effort).
**Exports:** `createTurnRendering`, `startsContinuationRound`

## `normalize` — arrow, line 7
- **called from:**
- `scripts/generate_sft_environment_expansion.py:267`
- `src/agent_loop.py:34918`
- `src/agent_runtime/authority.py:532`
- `src/agent_runtime/authority.py:647`
- `src/agent_runtime/authority.py:649`
- `src/agent_runtime/journal.py:232`
- `src/agent_runtime/journal.py:253`
- `src/agent_runtime/local_model_control.py:50`
- `src/agent_tools/bg_job_tools.py:90`
- `src/agent_tools/document_tools.py:388`
- `src/agent_tools/document_tools.py:389`
- `src/agent_tools/web_tools.py:867`
- `src/agent_tools/web_tools.py:868`
- `src/agent_tools/web_tools.py:1153`
- `src/agent_tools/web_tools.py:1155`
- `src/agent_tools/web_tools.py:1303`
- `src/agent_tools/web_tools.py:1548`
- `src/agent_tools/web_tools.py:1570`
- `src/agent_tools/web_tools_prewave3.py:871`
- `src/agent_tools/web_tools_prewave3.py:872`
- `src/agent_tools/web_tools_prewave3.py:1157`
- `src/agent_tools/web_tools_prewave3.py:1159`
- `src/agent_tools/web_tools_prewave3.py:1307`
- `src/agent_tools/web_tools_prewave3.py:1552`
- `src/agent_tools/web_tools_prewave3.py:1574`
- `src/browser_identity.py:85`
- `src/builtin_actions.py:892`
- `src/tool_approvals.py:410`
- `src/tool_approvals.py:467`
- `src/tool_capabilities.py:1028`
- `src/tool_execution.py:1766`
- `src/upload_handler.py:23`
- `tests/process_resource_helpers.py:17`
- `tests/process_resource_helpers.py:50`
- `tests/test_agent_state_dir_confinement.py:182`
- `tests/test_agent_state_dir_confinement.py:186`
- `tests/test_background_resource_identity.py:119`
- `tests/test_background_resource_identity.py:133`
- `tests/test_background_resource_identity.py:152`
- `tests/test_bg_job_tools.py:68`
- `tests/test_browser_identity_transport.py:148`
- `tests/test_browser_resource_identity.py:295`
- `tests/test_browser_resource_identity.py:304`
- `tests/test_effect_verification_adapters.py:63`
- `tests/test_effect_verification_adapters.py:75`
- `tests/test_effect_verification_adapters.py:225`
- `tests/test_effect_verification_adapters.py:297`
- `tests/test_effect_verification_adapters.py:316`
- `tests/test_effects_foundation.py:149`
- `tests/test_grep_followup_integrity.py:27`
- `tests/test_local_mcp_capabilities.py:890`
- `tests/test_local_mcp_capabilities.py:893`
- `tests/test_local_mcp_capabilities.py:958`
- `tests/test_local_mcp_capabilities.py:959`
- `tests/test_local_mcp_capabilities.py:981`
- `tests/test_local_mcp_capabilities.py:982`
- `tests/test_local_mcp_capabilities.py:988`
- `tests/test_local_mcp_capabilities.py:989`
- `tests/test_local_mcp_capabilities.py:1001`
- `tests/test_local_mcp_capabilities.py:1002`
- … +75 more (grep the name in repo)

## `startsContinuationRound` — function, line 9
- **called from:**
- `static/js/chat.js:5875`
- `static/js/chat.js:7585`
- `static/js/turnRendering.js:9`

## `signature` — function, line 18
- **called from:**
- `routes/contacts/contacts_routes.py:916`
- `routes/hwfit_routes.py:331`
- `scripts/diffusion_server.py:224`
- `scripts/diffusion_server.py:240`
- `src/agent_runtime/authority.py:602`
- `src/agent_runtime/completion.py:207`
- `src/agent_runtime/journal.py:241`
- `src/agent_tools/web_tools.py:756`
- `src/agent_tools/web_tools_prewave3.py:760`
- `src/turn_contract.py:6516`
- `tests/runtime_evidence_helpers.py:23`
- `tests/test_completion_boundary.py:201`
- `tests/test_contract_prompt_conversation.py:87`
- `tests/test_contract_prompt_conversation.py:89`
- `tests/test_contract_prompt_conversation.py:90`
- `tests/test_contract_prompt_conversation.py:91`
- `tests/test_contract_prompt_conversation.py:92`
- `tests/test_runtime_evidence_contract.py:342`
- `tests/test_skills_audit_characterization.py:69`
- `tests/test_skills_audit_characterization.py:162`
- `tests/test_skills_audit_characterization.py:171`
- `tests/test_skills_audit_characterization.py:251`
- `tests/test_skills_audit_characterization.py:251`
- `tests/test_skills_audit_characterization.py:271`
- `tests/test_skills_audit_characterization.py:271`
- `tests/test_skills_audit_characterization.py:295`
- `tests/test_skills_audit_characterization.py:295`
- `tests/test_turn_contract_integration.py:297`
- `tests/test_turn_contract_integration.py:297`
- `static/js/document.js:7611`
- `static/js/emailLibrary/signatureFold.js:227`
- `static/js/turnRendering.js:18`
- `static/js/turnRendering.js:118`
- `static/js/turnRendering.js:123`
- `static/js/turnRendering.js:141`

## `included` — function, line 21
- **called from:**
- `static/js/turnRendering.js:21`
- `static/js/turnRendering.js:37`

## `createTurnRendering` — function, line 52
- **called from:**
- `static/js/chat.js:3699`
- `static/js/chat.js:7288`
- `static/js/turnRendering.js:52`

## `accepts` — function, line 58
- **called from:**
- `src/agent_runtime/effect_log.py:175`
- `src/agent_runtime/effect_log.py:232`
- `src/agent_runtime/effect_log.py:306`
- `src/agent_runtime/effect_log.py:306`
- `src/agent_runtime/effect_log.py:333`
- `src/agent_runtime/effect_log.py:423`
- `static/js/chat.js:3708`
- `static/js/chat.js:4759`
- `static/js/chat.js:4798`
- `static/js/chat.js:5874`
- `static/js/chat.js:5984`
- `static/js/chat.js:7473`
- `static/js/chat.js:7481`
- `static/js/chat.js:7585`
- `static/js/turnRendering.js:58`
- `static/js/turnRendering.js:129`

## `elements` — function, line 75
- **called from:**
- `static/app.js:320`
- `static/js/turnRendering.js:75`
- `static/js/turnRendering.js:88`
- `static/js/turnRendering.js:109`

## `bodies` — function, line 87
- **called from:**
- `static/js/turnRendering.js:87`
- `static/js/turnRendering.js:105`
- `static/js/turnRendering.js:123`
- `static/js/turnRendering.js:127`

## `removeAnswer` — function, line 91
- **called from:**
- `static/js/turnRendering.js:91`
- `static/js/turnRendering.js:142`

## `settle` — function, line 104
- **called from:**
- `static/js/chat.js:3700`
- `static/js/chat.js:3716`
- `static/js/chat.js:6415`
- `static/js/chat.js:7341`
- `static/js/chat.js:7467`
- `static/js/chat.js:7479`
- `static/js/chat.js:7660`
- `static/js/emailLibrary/index.js:5974`
- `static/js/startupShell.js:136`
- `static/js/startupShell.js:145`
- `static/js/startupShell.js:148`
- `static/js/startupShell.js:151`
- `static/js/tourHints.js:66`
- `static/js/turnRendering.js:104`
- `static/js/turnRendering.js:148`

## `expected` — function, line 115
- **called from:**
- `static/js/turnRendering.js:115`
- `static/js/turnRendering.js:122`
- `static/js/turnRendering.js:130`

## `isVisible` — function, line 121
- **called from:**
- `static/js/chat.js:6076`
- `static/js/chat.js:6161`
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

## `render` — function, line 126
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
