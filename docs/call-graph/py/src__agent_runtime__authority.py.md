# `src/agent_runtime/authority.py` — definitions & call sites

41 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_owner` — function, line 28
- **called from:**
- `routes/assistant_routes.py:127`
- `routes/assistant_routes.py:140`
- `routes/assistant_routes.py:161`
- `routes/assistant_routes.py:279`
- `routes/assistant_routes.py:303`
- `routes/memory/memory_routes.py:88`
- `routes/memory/memory_routes.py:117`
- `routes/memory/memory_routes.py:151`
- `routes/memory/memory_routes.py:157`
- `routes/memory/memory_routes.py:173`
- `routes/memory/memory_routes.py:211`
- `routes/memory/memory_routes.py:246`
- `routes/memory/memory_routes.py:261`
- `routes/memory/memory_routes.py:274`
- `routes/memory/memory_routes.py:299`
- `routes/memory/memory_routes.py:357`
- `routes/memory/memory_routes.py:398`
- `routes/memory/memory_routes.py:512`
- `routes/memory/memory_routes.py:526`
- `routes/memory/memory_routes.py:537`
- `routes/memory/memory_routes.py:559`
- `routes/note/note_routes.py:632`
- `routes/note/note_routes.py:656`
- `routes/note/note_routes.py:694`
- `routes/note/note_routes.py:711`
- `routes/note/note_routes.py:771`
- `routes/note/note_routes.py:790`
- `routes/note/note_routes.py:809`
- `routes/note/note_routes.py:828`
- `routes/note/note_routes.py:867`
- `routes/note/note_routes.py:913`
- `routes/skills_routes.py:317`
- `routes/skills_routes.py:326`
- `routes/skills_routes.py:337`
- `routes/skills_routes.py:463`
- `routes/skills_routes.py:491`
- `routes/skills_routes.py:529`
- `routes/skills_routes.py:565`
- `routes/skills_routes.py:576`
- `routes/skills_routes.py:605`
- `routes/skills_routes.py:666`
- `routes/skills_routes.py:720`
- `routes/skills_routes.py:736`
- `routes/skills_routes.py:767`
- `routes/skills_routes.py:772`
- `routes/skills_routes.py:779`
- `routes/skills_routes.py:830`
- `routes/skills_routes.py:853`
- `routes/skills_routes.py:870`
- `routes/task/task_routes.py:353`
- `routes/task/task_routes.py:384`
- `routes/task/task_routes.py:393`
- `routes/task/task_routes.py:462`
- `routes/task/task_routes.py:580`
- `routes/task/task_routes.py:589`
- `routes/task/task_routes.py:617`
- `routes/task/task_routes.py:640`
- `routes/task/task_routes.py:719`
- `routes/task/task_routes.py:733`
- `routes/task/task_routes.py:830`
- … +16 more (grep the name in repo)

## `_pairs` — function, line 32
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_invalid_constant` — function, line 41
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_json` — function, line 45
- **called from:**
- `src/agent_runtime/authority.py:69`
- `src/agent_runtime/authority.py:532`
- `src/agent_runtime/authority.py:681`

## `ExactOperation` — class, line 50
- decorator: `dataclass(frozen=True)`
- **called from:**
- `tests/test_resource_identity.py:537`

## `ExactOperation.normalize` — method, line 57
- decorator: `classmethod`
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

## `OperationGrant` — class, line 83
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/authority.py:106`
- `src/agent_runtime/authority.py:316`
- `src/agent_runtime/authority.py:533`
- `src/agent_runtime/authority.py:658`
- `tests/process_resource_helpers.py:16`
- `tests/process_resource_helpers.py:49`
- `tests/process_resource_helpers.py:79`
- `tests/runtime_evidence_helpers.py:28`
- `tests/test_agent_external_tool_schemas.py:372`
- `tests/test_agent_state_dir_confinement.py:178`
- `tests/test_agent_state_dir_confinement.py:206`
- `tests/test_api_token_tool_authority.py:31`
- `tests/test_background_resource_identity.py:118`
- `tests/test_background_resource_identity.py:128`
- `tests/test_bg_job_tools.py:66`
- `tests/test_browser_identity_transport.py:156`
- `tests/test_browser_resource_identity.py:83`
- `tests/test_cookbook_readonly_tools_admin_gate.py:109`
- `tests/test_cookbook_readonly_tools_admin_gate.py:131`
- `tests/test_effect_resource_bindings.py:36`
- `tests/test_effect_resource_bindings.py:456`
- `tests/test_exact_approval_ungranted_process.py:25`
- `tests/test_legacy_browser_authority.py:23`
- `tests/test_local_mcp_capabilities.py:85`
- `tests/test_owned_resource_identity.py:34`
- `tests/test_process_resource_identity.py:83`
- `tests/test_process_resource_identity.py:95`
- `tests/test_process_resource_identity.py:108`
- `tests/test_process_resource_identity.py:118`
- `tests/test_process_resource_identity.py:121`
- `tests/test_remote_resource_identity.py:24`
- `tests/test_remote_resource_identity.py:80`
- `tests/test_remote_resource_identity.py:198`
- `tests/test_request_authority.py:25`
- `tests/test_resource_identity.py:31`
- `tests/test_review_regressions.py:966`
- `tests/test_review_regressions.py:993`
- `tests/test_runtime_resource_integration.py:36`
- `tests/test_runtime_resource_integration.py:84`
- `tests/test_scheduled_remote_ssh_refusal.py:17`
- `tests/test_tool_approvals.py:43`
- `tests/test_wave3_diagnostics.py:17`
- `tests/test_wave3_diagnostics.py:33`
- `tests/test_wave3_diagnostics.py:44`
- `tests/test_wave3_local_control.py:120`
- `tests/test_wave3_local_control.py:161`
- `tests/test_wave3_local_control.py:184`
- `tests/test_wave3_local_control.py:230`

## `OperationGrant.__post_init__` — method, line 88
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `OperationGrant.permits` — method, line 96
- **called from:**
- `routes/chat_routes.py:4049`
- `src/agent_loop.py:497`
- `src/agent_loop.py:521`
- `src/agent_loop.py:600`
- `src/agent_loop.py:22032`
- `src/agent_loop.py:22033`
- `src/agent_loop.py:22066`
- `src/agent_loop.py:23575`
- `src/agent_loop.py:33125`
- `src/agent_loop.py:33962`
- `src/agent_runtime/authority.py:223`
- `src/agent_runtime/local_model_control.py:58`
- `src/agent_runtime/owned_resources.py:419`
- `src/agent_runtime/process_resources.py:373`
- `src/agent_tools/web_tools.py:421`
- `src/agent_tools/web_tools_prewave3.py:425`
- `src/browser_identity.py:627`
- `src/builtin_actions.py:893`
- `src/clean_agent_preview.py:3265`
- `src/clean_agent_preview.py:3289`
- `src/clean_agent_preview.py:7434`
- `src/clean_agent_preview.py:7803`
- `src/task_scheduler.py:1388`
- `src/task_scheduler.py:2196`
- `src/tool_approvals.py:413`
- `src/tool_approvals.py:450`
- `src/tool_capabilities.py:1029`
- `src/tool_execution.py:1776`
- `src/tool_execution.py:1797`
- `src/tool_execution.py:2121`
- `tests/test_background_resource_identity.py:152`
- `tests/test_chat_route_tool_policy.py:340`
- `tests/test_chat_route_tool_policy.py:362`
- `tests/test_chat_route_tool_policy.py:363`
- `tests/test_chat_route_tool_policy.py:374`
- `tests/test_local_mcp_capabilities.py:889`
- `tests/test_local_mcp_capabilities.py:892`
- `tests/test_local_mcp_capabilities.py:958`
- `tests/test_local_mcp_capabilities.py:959`
- `tests/test_local_mcp_capabilities.py:981`
- `tests/test_local_mcp_capabilities.py:982`
- `tests/test_local_mcp_capabilities.py:988`
- `tests/test_local_mcp_capabilities.py:989`
- `tests/test_local_mcp_capabilities.py:1001`
- `tests/test_local_mcp_capabilities.py:1002`
- `tests/test_nested_invocation_ownership.py:236`
- `tests/test_product_turn_contract_route.py:109`
- `tests/test_product_turn_contract_route.py:115`
- `tests/test_product_turn_contract_route.py:125`
- `tests/test_product_turn_contract_route.py:126`
- `tests/test_product_turn_contract_route.py:129`
- `tests/test_product_turn_contract_route.py:230`
- `tests/test_product_turn_contract_route.py:284`
- `tests/test_product_turn_contract_route.py:383`
- `tests/test_request_authority.py:63`
- `tests/test_request_authority.py:64`
- `tests/test_request_authority.py:69`
- `tests/test_request_authority.py:70`
- `tests/test_request_authority.py:77`
- `tests/test_request_authority.py:82`
- … +81 more (grep the name in repo)

## `OperationGrant.intersect` — method, line 101
- **called from:**
- `src/agent_runtime/authority.py:243`
- `src/agent_runtime/authority.py:247`
- `src/agent_runtime/authority.py:577`
- `src/agent_runtime/authority.py:671`
- `src/tool_execution.py:1764`
- `tests/test_background_resource_identity.py:130`
- `tests/test_background_resource_identity.py:135`
- `tests/test_browser_identity_transport.py:131`
- `tests/test_browser_resource_identity.py:293`
- `tests/test_browser_resource_identity.py:298`
- `tests/test_owned_resource_identity.py:163`
- `tests/test_owned_resource_identity.py:381`
- `tests/test_process_resource_identity.py:78`
- `tests/test_process_resource_identity.py:111`
- `tests/test_process_resource_identity.py:112`
- `tests/test_process_resource_identity.py:123`
- `tests/test_remote_resource_identity.py:374`
- `tests/test_resource_identity.py:313`
- `tests/test_resource_identity.py:313`
- `tests/test_resource_identity.py:318`
- `tests/test_resource_identity.py:319`
- `tests/test_resource_identity.py:329`
- `tests/test_resource_identity.py:346`
- `tests/test_resource_identity.py:366`
- `tests/test_resource_identity.py:703`
- `static/js/editor/document-geometry.js:169`

## `OperationGrant.limits` — method, line 104
- **called from:**
- `src/agent_runtime/authority.py:106`
- `src/agent_runtime/authority.py:107`
- `src/agent_runtime/authority.py:316`
- `src/agent_runtime/authority.py:316`
- `src/agent_runtime/authority.py:317`

## `RequestAuthority` — class, line 111
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/authority.py:534`
- `tests/process_resource_helpers.py:16`
- `tests/process_resource_helpers.py:49`
- `tests/process_resource_helpers.py:79`
- `tests/runtime_evidence_helpers.py:38`
- `tests/test_agent_external_tool_schemas.py:371`
- `tests/test_agent_state_dir_confinement.py:178`
- `tests/test_agent_state_dir_confinement.py:206`
- `tests/test_api_token_tool_authority.py:29`
- `tests/test_background_resource_identity.py:118`
- `tests/test_background_resource_identity.py:128`
- `tests/test_bg_job_tools.py:66`
- `tests/test_browser_identity_transport.py:156`
- `tests/test_browser_resource_identity.py:83`
- `tests/test_cookbook_readonly_tools_admin_gate.py:108`
- `tests/test_cookbook_readonly_tools_admin_gate.py:130`
- `tests/test_effect_resource_bindings.py:35`
- `tests/test_effect_resource_bindings.py:456`
- `tests/test_exact_approval_ungranted_process.py:24`
- `tests/test_legacy_browser_authority.py:23`
- `tests/test_local_mcp_capabilities.py:80`
- `tests/test_owned_resource_identity.py:33`
- `tests/test_process_resource_identity.py:57`
- `tests/test_process_resource_identity.py:59`
- `tests/test_process_resource_identity.py:76`
- `tests/test_process_resource_identity.py:83`
- `tests/test_process_resource_identity.py:95`
- `tests/test_process_resource_identity.py:108`
- `tests/test_process_resource_identity.py:118`
- `tests/test_process_resource_identity.py:121`
- `tests/test_remote_resource_identity.py:23`
- `tests/test_remote_resource_identity.py:198`
- `tests/test_request_authority.py:24`
- `tests/test_resource_identity.py:30`
- `tests/test_review_regressions.py:966`
- `tests/test_review_regressions.py:993`
- `tests/test_runtime_resource_integration.py:36`
- `tests/test_scheduled_remote_ssh_refusal.py:17`
- `tests/test_tool_approvals.py:42`
- `tests/test_wave3_diagnostics.py:17`
- `tests/test_wave3_diagnostics.py:33`
- `tests/test_wave3_diagnostics.py:44`
- `tests/test_wave3_local_control.py:120`
- `tests/test_wave3_local_control.py:161`
- `tests/test_wave3_local_control.py:184`
- `tests/test_wave3_local_control.py:230`

## `RequestAuthority.__post_init__` — method, line 132
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `RequestAuthority.empty` — method, line 209
- decorator: `classmethod`
- **called from:**
- `routes/chat_routes.py:3824`
- `routes/shell_routes.py:1223`
- `routes/skills_routes.py:610`
- `services/skills/agent_runner.py:65`
- `services/skills/agent_runner.py:213`
- `src/agent_runtime/authority.py:265`
- `src/agent_runtime/authority.py:567`
- `src/agent_runtime/authority.py:615`
- `src/agent_runtime/authority.py:620`
- `src/agent_runtime/authority.py:669`
- `src/agent_runtime/authority.py:691`
- `src/agent_runtime/authority.py:722`
- `src/bg_monitor.py:80`
- `tests/test_resource_identity.py:642`
- `tests/test_skills_audit_services.py:198`
- `static/js/chatRenderer.js:2250`
- `static/js/cookbook-hwfit.js:2425`
- `static/js/cookbookRunning.js:2329`
- `static/js/document.js:3340`
- `static/js/documentLibrary.js:3302`
- `static/js/editor/ai-inpaint.js:24`
- `static/js/editor/ai-inpaint.js:336`
- `static/js/editor/build/controls.js:702`
- `static/js/emailInbox.js:1005`
- `static/js/galleryEditor.js:13996`
- `static/js/modalManager.js:247`
- `static/js/modalManager.js:306`

## `RequestAuthority.bound_to` — method, line 213
- **called from:**
- `src/tool_execution.py:1767`
- `tests/test_request_authority.py:465`

## `RequestAuthority.restricted` — method, line 217
- **called from:**
- `src/agent_runtime/authority.py:223`
- `src/tool_execution.py:1772`
- `src/tool_execution.py:1788`

## `RequestAuthority.permits` — method, line 222
- **called from:**
- `routes/chat_routes.py:4049`
- `src/agent_loop.py:497`
- `src/agent_loop.py:521`
- `src/agent_loop.py:600`
- `src/agent_loop.py:22032`
- `src/agent_loop.py:22033`
- `src/agent_loop.py:22066`
- `src/agent_loop.py:23575`
- `src/agent_loop.py:33125`
- `src/agent_loop.py:33962`
- `src/agent_runtime/authority.py:223`
- `src/agent_runtime/local_model_control.py:58`
- `src/agent_runtime/owned_resources.py:419`
- `src/agent_runtime/process_resources.py:373`
- `src/agent_tools/web_tools.py:421`
- `src/agent_tools/web_tools_prewave3.py:425`
- `src/browser_identity.py:627`
- `src/builtin_actions.py:893`
- `src/clean_agent_preview.py:3265`
- `src/clean_agent_preview.py:3289`
- `src/clean_agent_preview.py:7434`
- `src/clean_agent_preview.py:7803`
- `src/task_scheduler.py:1388`
- `src/task_scheduler.py:2196`
- `src/tool_approvals.py:413`
- `src/tool_approvals.py:450`
- `src/tool_capabilities.py:1029`
- `src/tool_execution.py:1776`
- `src/tool_execution.py:1797`
- `src/tool_execution.py:2121`
- `tests/test_background_resource_identity.py:152`
- `tests/test_chat_route_tool_policy.py:340`
- `tests/test_chat_route_tool_policy.py:362`
- `tests/test_chat_route_tool_policy.py:363`
- `tests/test_chat_route_tool_policy.py:374`
- `tests/test_local_mcp_capabilities.py:889`
- `tests/test_local_mcp_capabilities.py:892`
- `tests/test_local_mcp_capabilities.py:958`
- `tests/test_local_mcp_capabilities.py:959`
- `tests/test_local_mcp_capabilities.py:981`
- `tests/test_local_mcp_capabilities.py:982`
- `tests/test_local_mcp_capabilities.py:988`
- `tests/test_local_mcp_capabilities.py:989`
- `tests/test_local_mcp_capabilities.py:1001`
- `tests/test_local_mcp_capabilities.py:1002`
- `tests/test_nested_invocation_ownership.py:236`
- `tests/test_product_turn_contract_route.py:109`
- `tests/test_product_turn_contract_route.py:115`
- `tests/test_product_turn_contract_route.py:125`
- `tests/test_product_turn_contract_route.py:126`
- `tests/test_product_turn_contract_route.py:129`
- `tests/test_product_turn_contract_route.py:230`
- `tests/test_product_turn_contract_route.py:284`
- `tests/test_product_turn_contract_route.py:383`
- `tests/test_request_authority.py:63`
- `tests/test_request_authority.py:64`
- `tests/test_request_authority.py:69`
- `tests/test_request_authority.py:70`
- `tests/test_request_authority.py:77`
- `tests/test_request_authority.py:82`
- … +81 more (grep the name in repo)

## `RequestAuthority.restrict` — method, line 225
- **called from:**
- `routes/chat_routes.py:3822`
- `routes/chat_routes.py:3959`
- `src/agent_runtime/authority.py:540`
- `src/agent_runtime/authority.py:567`
- `src/agent_runtime/authority.py:633`
- `src/bg_monitor.py:185`
- `src/task_scheduler.py:1386`
- `src/task_scheduler.py:2195`
- `src/tool_execution.py:1770`
- `tests/test_request_authority.py:141`
- `tests/test_request_authority.py:143`
- `tests/test_request_authority.py:226`

## `RequestAuthority.intersect` — method, line 232
- **called from:**
- `src/agent_runtime/authority.py:243`
- `src/agent_runtime/authority.py:247`
- `src/agent_runtime/authority.py:577`
- `src/agent_runtime/authority.py:671`
- `src/tool_execution.py:1764`
- `tests/test_background_resource_identity.py:130`
- `tests/test_background_resource_identity.py:135`
- `tests/test_browser_identity_transport.py:131`
- `tests/test_browser_resource_identity.py:293`
- `tests/test_browser_resource_identity.py:298`
- `tests/test_owned_resource_identity.py:163`
- `tests/test_owned_resource_identity.py:381`
- `tests/test_process_resource_identity.py:78`
- `tests/test_process_resource_identity.py:111`
- `tests/test_process_resource_identity.py:112`
- `tests/test_process_resource_identity.py:123`
- `tests/test_remote_resource_identity.py:374`
- `tests/test_resource_identity.py:313`
- `tests/test_resource_identity.py:313`
- `tests/test_resource_identity.py:318`
- `tests/test_resource_identity.py:319`
- `tests/test_resource_identity.py:329`
- `tests/test_resource_identity.py:346`
- `tests/test_resource_identity.py:366`
- `tests/test_resource_identity.py:703`
- `static/js/editor/document-geometry.js:169`

## `RequestAuthority.continuation` — method, line 262
- **called from:**
- `src/agent_runtime/authority.py:689`
- `src/agent_runtime/authority.py:720`

## `RequestAuthority.to_dict` — method, line 274
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5646`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28809`
- `src/agent_loop.py:31378`
- `src/agent_loop.py:31851`
- `src/agent_loop.py:32116`
- `src/agent_loop.py:32156`
- `src/agent_loop.py:32187`
- `src/agent_loop.py:32240`
- `src/agent_loop.py:32368`
- `src/agent_loop.py:32700`
- `src/agent_loop.py:34920`
- `src/agent_loop.py:36929`
- `src/agent_loop.py:37252`
- `src/agent_loop.py:37465`
- `src/agent_loop.py:37520`
- `src/agent_loop.py:37577`
- `src/agent_loop.py:37911`
- `src/agent_loop.py:37923`
- `src/agent_loop.py:38029`
- `src/agent_loop.py:38963`
- `src/agent_loop.py:38964`
- `src/agent_loop.py:38969`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:681`
- `src/agent_runtime/authority.py:705`
- `src/agent_runtime/authority.py:705`
- `src/agent_runtime/completion.py:356`
- `src/agent_runtime/completion.py:385`
- `src/agent_runtime/completion.py:388`
- `src/agent_runtime/completion.py:389`
- `src/agent_runtime/completion.py:392`
- `src/agent_runtime/context_resolution.py:78`
- `src/agent_runtime/context_resolution.py:78`
- `src/agent_runtime/context_resolution.py:154`
- `src/agent_runtime/context_resolution.py:155`
- `src/agent_runtime/context_resolution.py:502`
- `src/agent_runtime/context_resolution.py:518`
- `src/agent_runtime/effect_adapters.py:296`
- `src/agent_runtime/effect_log.py:263`
- `src/agent_runtime/effects.py:156`
- `src/agent_runtime/effects.py:161`
- `src/agent_runtime/effects.py:168`
- `src/agent_runtime/effects.py:173`
- `src/agent_runtime/effects.py:177`
- `src/agent_runtime/effects.py:181`
- `src/agent_runtime/effects.py:186`
- … +146 more (grep the name in repo)

## `RequestAuthority.from_dict` — method, line 292
- decorator: `classmethod`
- **called from:**
- `src/agent_runtime/authority.py:319`
- `src/agent_runtime/authority.py:320`
- `src/agent_runtime/authority.py:321`
- `src/agent_runtime/authority.py:322`
- `src/agent_runtime/authority.py:323`
- `src/agent_runtime/authority.py:324`
- `src/agent_runtime/authority.py:325`
- `src/agent_runtime/authority.py:689`
- `src/agent_runtime/authority.py:711`
- `src/agent_runtime/authority.py:714`
- `src/agent_runtime/effect_log.py:91`
- `src/agent_runtime/effects.py:277`
- `src/agent_runtime/effects.py:340`
- `src/agent_runtime/effects.py:341`
- `src/agent_runtime/effects.py:342`
- `src/agent_runtime/effects.py:343`
- `src/agent_runtime/effects.py:493`
- `src/agent_runtime/effects.py:576`
- `src/agent_runtime/process_resources.py:80`
- `src/agent_runtime/process_resources.py:89`
- `src/agent_runtime/process_resources.py:129`
- `src/agent_runtime/process_resources.py:477`
- `src/agent_runtime/resources.py:238`
- `src/agent_runtime/resources.py:275`
- `src/agent_runtime/resources.py:531`
- `src/agent_runtime/resources.py:570`
- `src/agent_runtime/resources.py:608`
- `src/agent_trace.py:124`
- `src/bg_jobs.py:227`
- `src/containment_worker.py:52`
- `src/containment_worker.py:53`
- `tests/test_background_resource_identity.py:54`
- `tests/test_background_resource_identity.py:65`
- `tests/test_background_resource_identity.py:187`
- `tests/test_background_resource_identity.py:191`
- `tests/test_browser_resource_identity.py:160`
- `tests/test_browser_resource_identity.py:321`
- `tests/test_effect_journal_persistence.py:43`
- `tests/test_effects_foundation.py:139`
- `tests/test_effects_foundation.py:141`
- `tests/test_effects_foundation.py:143`
- `tests/test_effects_foundation.py:160`
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`
- `tests/test_owned_resource_identity.py:180`
- `tests/test_owned_resource_identity.py:322`
- `tests/test_owned_resource_identity.py:327`
- `tests/test_process_resource_identity.py:31`
- `tests/test_process_resource_identity.py:37`
- `tests/test_process_resource_identity.py:41`
- `tests/test_process_resource_identity.py:88`
- `tests/test_remote_resource_identity.py:68`
- `tests/test_remote_resource_identity.py:162`
- `tests/test_request_authority.py:115`
- `tests/test_resource_identity.py:379`
- `tests/test_resource_identity.py:393`
- `tests/test_resource_identity.py:660`
- `tests/test_resource_identity.py:683`
- `tests/test_runtime_resource_integration.py:416`
- `tests/test_wave3_launch_cost_lifecycle.py:84`
- … +1 more (grep the name in repo)

## `RequestAuthority.limits` — method, line 296
- **called from:**
- `src/agent_runtime/authority.py:106`
- `src/agent_runtime/authority.py:107`
- `src/agent_runtime/authority.py:316`
- `src/agent_runtime/authority.py:316`
- `src/agent_runtime/authority.py:317`

## `SemanticIntent` — class, line 333
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/authority.py:370`
- `src/agent_runtime/authority.py:371`

## `interpret_request` — function, line 340
- **called from:**
- `src/agent_runtime/authority.py:475`

## `_trusted_local_mcp_request_tools` — function, line 375
- **called from:**
- `src/agent_runtime/authority.py:491`

## `create_request_authority` — function, line 469
- **called from:**
- `src/agent_runtime/authority.py:569`
- `src/agent_runtime/authority.py:623`
- `src/agent_runtime/authority.py:656`
- `tests/test_agent_external_tool_schemas.py:437`
- `tests/test_edit_file.py:59`
- `tests/test_local_mcp_capabilities.py:884`
- `tests/test_local_mcp_capabilities.py:953`
- `tests/test_local_mcp_capabilities.py:980`
- `tests/test_local_mcp_capabilities.py:987`
- `tests/test_local_mcp_capabilities.py:997`
- `tests/test_request_authority.py:61`
- `tests/test_request_authority.py:68`
- `tests/test_request_authority.py:74`
- `tests/test_request_authority.py:81`
- `tests/test_request_authority.py:88`
- `tests/test_request_authority.py:102`
- `tests/test_request_authority.py:119`
- `tests/test_request_authority.py:477`
- `tests/test_resource_identity.py:717`
- `tests/test_runtime_resource_integration.py:286`

## `active_request_authority` — function, line 547
- **called from:**
- `services/skills/agent_runner.py:213`
- `src/agent_loop.py:34270`
- `src/agent_loop.py:38993`
- `src/agent_runtime/authority.py:608`
- `src/agent_runtime/authority.py:667`
- `src/agent_runtime/local_model_control.py:49`
- `src/agent_runtime/process_resources.py:369`
- `src/agent_tools/subprocess_tools.py:530`
- `src/bg_jobs.py:100`
- `src/browser_identity.py:620`
- `src/builtin_actions.py:886`
- `src/tool_capabilities.py:1022`
- `src/tool_execution.py:1644`
- `src/tool_execution.py:1761`
- `src/tool_execution.py:1762`
- `src/turn_contract.py:6447`
- `tests/process_resource_helpers.py:73`
- `tests/test_request_authority.py:179`
- `tests/test_request_authority.py:189`
- `tests/test_request_authority.py:190`
- `tests/test_request_authority.py:199`
- `tests/test_request_authority.py:200`
- `tests/test_request_authority.py:328`
- `tests/test_request_authority.py:337`
- `tests/test_request_authority.py:348`
- `tests/test_request_authority.py:421`
- `tests/test_request_authority.py:429`
- `tests/test_request_authority.py:581`
- `tests/test_runtime_resource_integration.py:156`

## `is_internal_tool_request` — function, line 551
- **called from:**
- `routes/chat_routes.py:2525`
- `routes/chat_routes.py:2527`
- `routes/chat_routes.py:3348`
- `routes/chat_routes.py:3354`
- `routes/codex_routes.py:128`
- `routes/shell_routes.py:68`
- `routes/task/task_routes.py:33`
- `src/agent_runtime/authority.py:559`
- `src/agent_runtime/authority.py:566`
- `tests/test_request_authority.py:449`

## `require_user_approval_request` — function, line 558
- **called from:**
- `routes/chat_routes.py:3048`
- `routes/skills_routes.py:664`
- `tests/test_request_authority.py:451`
- `tests/test_request_authority.py:454`

## `request_authority_for_http` — function, line 564
- **called from:**
- `routes/chat_routes.py:3809`
- `routes/skills_routes.py:609`
- `tests/test_request_authority.py:463`

## `bind_request_authority` — function, line 573
- decorator: `contextmanager`
- **called from:**
- `src/agent_runtime/authority.py:634`
- `src/task_scheduler.py:1416`
- `src/task_scheduler.py:2271`
- `src/tool_execution.py:1966`
- `src/tool_execution.py:1996`
- `tests/process_resource_helpers.py:18`
- `tests/test_bg_job_tools.py:69`
- `tests/test_effect_resource_bindings.py:459`
- `tests/test_local_mcp_capabilities.py:102`
- `tests/test_local_mcp_capabilities.py:910`
- `tests/test_local_mcp_capabilities.py:939`
- `tests/test_local_mcp_capabilities.py:943`
- `tests/test_local_mcp_capabilities.py:964`
- `tests/test_owned_resource_identity.py:168`
- `tests/test_remote_resource_identity.py:147`
- `tests/test_request_authority.py:182`
- `tests/test_request_authority.py:207`
- `tests/test_request_authority.py:306`
- `tests/test_request_authority.py:331`
- `tests/test_request_authority.py:422`
- `tests/test_request_authority.py:545`
- `tests/test_resource_identity.py:348`
- `tests/test_resource_identity.py:348`
- `tests/test_resource_identity.py:351`
- `tests/test_resource_identity.py:405`
- `tests/test_resource_identity.py:604`
- `tests/test_resource_identity.py:604`
- `tests/test_runtime_resource_integration.py:75`
- `tests/test_runtime_resource_integration.py:85`
- `tests/test_scheduled_remote_ssh_refusal.py:18`
- `tests/test_skills_audit_services.py:209`
- `tests/test_wave3_launch_cost_lifecycle.py:64`
- `tests/test_wave3_local_control.py:133`
- `tests/test_wave3_local_control.py:137`
- `tests/test_wave3_local_control.py:165`
- `tests/test_wave3_local_control.py:187`

## `_request_text` — function, line 585
- **called from:**
- `src/agent_runtime/authority.py:623`

## `with_request_authority` — function, line 600
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `wrapped` — function (async), line 604
- decorator: `wraps(func)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `task_operation` — function, line 643
- **called from:**
- `src/agent_runtime/authority.py:655`
- `src/task_scheduler.py:1387`
- `src/task_scheduler.py:2196`
- `tests/test_request_authority.py:136`
- `tests/test_request_authority.py:137`
- `tests/test_request_authority.py:219`
- `tests/test_request_authority.py:412`

## `seal_task_authority` — function, line 653
- **called from:**
- `routes/task/task_routes.py:34`
- `src/task_scheduler.py:2714`
- `src/tools/system.py:519`
- `src/tools/system.py:596`
- `tests/test_request_authority.py:134`
- `tests/test_request_authority.py:208`
- `tests/test_request_authority.py:217`
- `tests/test_request_authority.py:546`
- `tests/test_resource_identity.py:352`
- `tests/test_resource_identity.py:406`
- `tests/test_task_scheduler_cancel.py:195`
- `tests/test_task_scheduler_endpoint_authority.py:63`
- `tests/test_wave3_local_control.py:131`

## `restore_task_authority` — function, line 684
- **called from:**
- `src/task_scheduler.py:1382`
- `src/task_scheduler.py:2075`
- `src/task_scheduler.py:2192`
- `tests/test_request_authority.py:135`
- `tests/test_request_authority.py:209`
- `tests/test_request_authority.py:212`
- `tests/test_request_authority.py:218`
- `tests/test_request_authority.py:410`
- `tests/test_request_authority.py:437`
- `tests/test_resource_identity.py:353`
- `tests/test_resource_identity.py:407`
- `tests/test_wave3_local_control.py:132`

## `_background_path` — function, line 694
- **called from:**
- `src/agent_runtime/authority.py:705`
- `src/agent_runtime/authority.py:710`

## `save_background_authority` — function, line 701
- **called from:**
- `src/bg_jobs.py:179`
- `tests/process_resource_helpers.py:65`
- `tests/test_request_authority.py:229`
- `tests/test_resource_identity.py:402`

## `restore_background_authority` — function, line 708
- **called from:**
- `src/bg_monitor.py:169`
- `tests/test_background_resource_identity.py:145`
- `tests/test_background_resource_identity.py:150`
- `tests/test_background_resource_identity.py:153`
- `tests/test_request_authority.py:230`
- `tests/test_request_authority.py:233`
- `tests/test_request_authority.py:246`
- `tests/test_resource_identity.py:403`
- `tests/test_resource_identity.py:404`
