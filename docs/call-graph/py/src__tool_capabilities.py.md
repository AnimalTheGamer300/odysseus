# `src/tool_capabilities.py` — definitions & call sites

25 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ToolEffect` — class, line 23
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResultIntegrity` — class, line 39
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ToolCapabilities` — class, line 46
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/tool_capabilities.py:56`
- `src/tool_capabilities.py:316`
- `src/tool_capabilities.py:697`
- `src/tool_capabilities.py:731`
- `src/tool_capabilities.py:742`
- `src/tool_capabilities.py:756`

## `_capabilities` — function, line 52
- **called from:**
- `src/tool_capabilities.py:67`
- `src/tool_capabilities.py:305`
- `src/tool_capabilities.py:321`
- `src/tool_capabilities.py:340`
- `src/tool_capabilities.py:344`
- `src/tool_capabilities.py:713`
- `src/tool_capabilities.py:748`
- `src/tool_capabilities.py:762`

## `_register` — function, line 62
- **called from:**
- `src/tool_capabilities.py:74`
- `src/tool_capabilities.py:78`
- `src/tool_capabilities.py:93`
- `src/tool_capabilities.py:98`
- `src/tool_capabilities.py:103`
- `src/tool_capabilities.py:108`
- `src/tool_capabilities.py:114`
- `src/tool_capabilities.py:119`
- `src/tool_capabilities.py:124`
- `src/tool_capabilities.py:142`
- `src/tool_capabilities.py:147`
- `src/tool_capabilities.py:154`
- `src/tool_capabilities.py:171`
- `src/tool_capabilities.py:183`
- `src/tool_capabilities.py:191`
- `src/tool_capabilities.py:196`
- `src/tool_capabilities.py:202`
- `src/tool_capabilities.py:207`
- `src/tool_capabilities.py:213`
- `src/tool_capabilities.py:219`
- `src/tool_capabilities.py:225`
- `src/tool_capabilities.py:229`
- `src/tool_capabilities.py:234`
- `src/tool_capabilities.py:241`
- `src/tool_capabilities.py:257`
- `src/tool_capabilities.py:263`
- `src/tool_capabilities.py:269`
- `src/tool_capabilities.py:284`

## `_local_mcp_tools` — function, line 350
- **called from:**
- `src/agent_runtime/authority.py:416`
- `src/agent_runtime/authority.py:416`
- `src/tool_capabilities.py:417`
- `src/tool_capabilities.py:418`
- `src/tool_capabilities.py:427`
- `src/tool_capabilities.py:428`
- `src/tool_capabilities.py:452`
- `src/tool_capabilities.py:453`

## `_current_mcp_manager` — function, line 377
- **called from:**
- `src/tool_capabilities.py:432`
- `src/tool_capabilities.py:457`
- `src/tool_capabilities.py:990`

## `_is_declared_local_mcp_tool` — function, line 394
- **called from:**
- `src/tool_capabilities.py:425`
- `src/tool_capabilities.py:450`
- `src/tool_capabilities.py:979`
- `src/tool_capabilities.py:1045`
- `src/tool_capabilities.py:1097`

## `_is_declared_local_mcp_read_tool` — function, line 422
- **called from:**
- `src/agent_runtime/authority.py:435`
- `src/tool_capabilities.py:487`
- `src/tool_capabilities.py:1063`

## `_is_declared_local_mcp_write_tool` — function, line 447
- **called from:**
- `src/agent_runtime/authority.py:436`
- `src/tool_capabilities.py:489`

## `capabilities_for_tool` — function, line 473
- **called from:**
- `src/agent_runtime/authority.py:439`
- `src/tool_capabilities.py:662`
- `src/tool_capabilities.py:1047`
- `tests/test_clean_agent_preview.py:17`
- `tests/test_clean_agent_preview.py:26`
- `tests/test_clean_agent_preview.py:35`
- `tests/test_external_context_tool_gate.py:200`
- `tests/test_external_context_tool_gate.py:320`
- `tests/test_external_context_tool_gate.py:369`
- `tests/test_external_context_tool_gate.py:395`
- `tests/test_external_context_tool_gate.py:428`
- `tests/test_external_context_tool_gate.py:607`
- `tests/test_external_context_tool_gate.py:622`
- `tests/test_local_mcp_capabilities.py:153`
- `tests/test_local_mcp_capabilities.py:175`
- `tests/test_local_mcp_capabilities.py:200`
- `tests/test_local_mcp_capabilities.py:208`
- `tests/test_local_mcp_capabilities.py:576`
- `tests/test_local_mcp_capabilities.py:580`
- `tests/test_local_mcp_capabilities.py:584`
- `tests/test_local_mcp_capabilities.py:587`
- `tests/test_local_mcp_capabilities.py:607`
- `tests/test_local_mcp_capabilities.py:646`
- `tests/test_local_mcp_capabilities.py:647`
- `tests/test_local_mcp_capabilities.py:650`
- `tests/test_local_mcp_capabilities.py:651`
- `tests/test_local_mcp_capabilities.py:654`
- `tests/test_local_mcp_capabilities.py:655`
- `tests/test_local_mcp_capabilities.py:658`
- `tests/test_local_mcp_capabilities.py:659`

## `_action_from_content` — function, line 616
- **called from:**
- `src/agent_runtime/authority.py:73`
- `src/tool_capabilities.py:737`

## `capabilities_for_action` — function, line 660
- **called from:**
- `src/agent_loop.py:481`
- `src/agent_loop.py:530`
- `src/agent_loop.py:16452`
- `src/agent_loop.py:34224`
- `src/agent_runtime/effect_adapters.py:239`
- `src/clean_agent_preview.py:3780`
- `src/clean_agent_preview.py:3820`
- `src/clean_agent_preview.py:4036`
- `src/clean_agent_preview.py:7932`
- `src/teacher_escalation.py:845`
- `src/tool_approvals.py:278`
- `src/tool_capabilities.py:802`
- `src/tool_capabilities.py:924`
- `src/tool_capabilities.py:982`
- `src/tool_capabilities.py:1179`
- `tests/test_agent_rounds_exhausted.py:3776`
- `tests/test_exact_approval_ungranted_process.py:32`
- `tests/test_external_context_tool_gate.py:129`
- `tests/test_external_context_tool_gate.py:133`
- `tests/test_external_context_tool_gate.py:410`
- `tests/test_external_context_tool_gate.py:413`
- `tests/test_external_context_tool_gate.py:649`
- `tests/test_external_context_tool_gate.py:674`
- `tests/test_external_context_tool_gate.py:704`
- `tests/test_external_context_tool_gate.py:732`
- `tests/test_external_context_tool_gate.py:745`
- `tests/test_external_context_tool_gate.py:750`
- `tests/test_foreground_model_routing.py:338`
- `tests/test_foreground_model_routing.py:381`
- `tests/test_foreground_model_routing.py:414`
- `tests/test_foreground_model_routing.py:451`
- `tests/test_foreground_model_routing.py:483`
- `tests/test_local_mcp_capabilities.py:526`
- `tests/test_owned_resource_identity.py:48`
- `tests/test_remote_resource_identity.py:38`
- `tests/test_request_authority.py:269`
- `tests/test_request_authority.py:289`
- `tests/test_request_authority.py:302`
- `tests/test_resource_identity.py:547`
- `tests/test_runtime_resource_integration.py:43`
- `tests/test_scheduler_prompt_cache_time.py:90`
- `tests/test_skills_audit_services.py:327`
- `tests/test_skills_routes_owner_update.py:166`
- `tests/test_tool_approval_single_action_scope.py:33`
- `tests/test_tool_approval_task_scope.py:45`
- `tests/test_tool_approvals.py:32`
- `tests/test_tool_approvals.py:236`
- `tests/test_tool_approvals.py:288`
- `tests/test_turn_contract_integration.py:223`

## `tool_result_is_successful` — function, line 769
- **called from:**
- `src/agent_loop.py:595`
- `src/agent_loop.py:1971`
- `src/agent_loop.py:1996`
- `src/agent_loop.py:2112`
- `src/agent_loop.py:4744`
- `src/agent_loop.py:5101`
- `src/agent_loop.py:6484`
- `src/agent_loop.py:6559`
- `src/agent_loop.py:6596`
- `src/agent_loop.py:6621`
- `src/agent_loop.py:6834`
- `src/agent_loop.py:6945`
- `src/agent_loop.py:6955`
- `src/agent_loop.py:14103`
- `src/agent_loop.py:14189`
- `src/agent_loop.py:14488`
- `src/agent_loop.py:17471`
- `src/agent_loop.py:19406`
- `src/agent_loop.py:20083`
- `src/agent_loop.py:20120`
- `src/agent_loop.py:22623`
- `src/agent_loop.py:26151`
- `src/agent_loop.py:26170`
- `src/agent_loop.py:26190`
- `src/agent_loop.py:26205`
- `src/agent_loop.py:26254`
- `src/agent_loop.py:26314`
- `src/agent_loop.py:26435`
- `src/agent_loop.py:26456`
- `src/agent_loop.py:28048`
- `src/agent_loop.py:34355`
- `src/agent_loop.py:34422`
- `src/agent_loop.py:34470`
- `src/agent_loop.py:34752`
- `src/agent_loop.py:35465`
- `src/agent_loop.py:35696`
- `src/agent_loop.py:35866`
- `src/agent_loop.py:35897`
- `src/agent_loop.py:35982`
- `src/agent_loop.py:36001`
- `src/agent_loop.py:36172`
- `src/agent_loop.py:36184`
- `src/agent_loop.py:36220`
- `src/agent_loop.py:36258`
- `src/agent_loop.py:36293`
- `src/agent_loop.py:36326`
- `src/agent_loop.py:36372`
- `src/agent_loop.py:36393`
- `src/agent_loop.py:36452`
- `src/agent_loop.py:36469`
- `src/agent_loop.py:36478`
- `src/agent_loop.py:36496`
- `src/agent_loop.py:36504`
- `src/agent_loop.py:36532`
- `src/agent_loop.py:36549`
- `src/agent_loop.py:36572`
- `src/agent_loop.py:36590`
- `src/agent_loop.py:36598`
- `src/agent_loop.py:36610`
- `src/agent_loop.py:36628`
- … +24 more (grep the name in repo)

## `tool_result_should_arm_gate` — function, line 781
- **called from:**
- `src/agent_loop.py:16453`
- `src/agent_loop.py:16522`
- `src/tool_capabilities.py:1218`
- `tests/test_external_context_tool_gate.py:246`
- `tests/test_external_context_tool_gate.py:274`
- `tests/test_external_context_tool_gate.py:294`
- `tests/test_external_context_tool_gate.py:305`
- `tests/test_external_context_tool_gate.py:323`
- `tests/test_local_mcp_capabilities.py:161`
- `tests/test_local_mcp_capabilities.py:177`
- `tests/test_local_mcp_capabilities.py:210`

## `ToolGateDecision` — class, line 854
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/tool_capabilities.py:1143`
- `src/tool_capabilities.py:1151`
- `src/tool_capabilities.py:1153`
- `src/tool_capabilities.py:1155`
- `src/tool_capabilities.py:1157`
- `src/tool_capabilities.py:1171`
- `src/tool_capabilities.py:1190`
- `src/tool_capabilities.py:1197`
- `src/tool_capabilities.py:1199`
- `src/tool_capabilities.py:1206`
- `src/tool_capabilities.py:1210`
- `tests/test_agent_evidence_loop.py:67`
- `tests/test_agent_rounds_exhausted.py:61`
- `tests/test_fenced_example_not_executed_for_native_models.py:59`
- `tests/test_foreground_model_routing.py:70`
- `tests/test_tool_task_cancelled_on_disconnect.py:56`

## `messages_contain_external_untrusted_context` — function, line 887
- **called from:**
- `src/agent_loop.py:21848`
- `src/tool_capabilities.py:1134`
- `tests/test_external_context_tool_gate.py:479`
- `tests/test_external_context_tool_gate.py:492`
- `tests/test_external_context_tool_gate.py:506`
- `tests/test_external_context_tool_gate.py:508`
- `tests/test_external_context_tool_gate.py:549`
- `tests/test_external_context_tool_gate.py:565`
- `tests/test_external_context_tool_gate.py:585`
- `tests/test_external_context_tool_gate.py:600`
- `tests/test_external_context_tool_gate.py:833`

## `delegated_tool_is_blocked` — function, line 916
- **called from:**
- `src/agent_loop.py:25097`
- `src/agent_loop.py:25778`
- `src/clean_agent_preview.py:5678`
- `src/tool_capabilities.py:1142`
- `src/tool_execution.py:1757`

## `_is_authorized_local_mcp_continuation` — function, line 955
- **called from:**
- `src/tool_capabilities.py:1167`

## `ToolRunSecurityContext` — class, line 1072
- decorator: `dataclass`
- **called from:**
- `src/agent_loop.py:21841`
- `src/clean_agent_preview.py:5867`
- `tests/test_api_token_tool_authority.py:46`
- `tests/test_api_token_tool_authority.py:94`
- `tests/test_api_token_tool_authority.py:98`
- `tests/test_api_token_tool_authority.py:129`
- `tests/test_api_token_tool_authority.py:157`
- `tests/test_api_token_tool_authority.py:175`
- `tests/test_api_token_tool_authority.py:192`
- `tests/test_api_token_tool_authority.py:208`
- `tests/test_api_token_tool_authority.py:215`
- `tests/test_api_token_tool_authority.py:224`
- `tests/test_api_token_tool_authority.py:232`
- `tests/test_api_token_tool_authority.py:264`
- `tests/test_api_token_tool_authority.py:416`
- `tests/test_api_token_tool_authority.py:440`
- `tests/test_api_token_tool_authority.py:471`
- `tests/test_api_token_tool_authority.py:503`
- `tests/test_api_token_tool_authority.py:593`
- `tests/test_api_token_tool_authority.py:603`
- `tests/test_api_token_tool_authority.py:613`
- `tests/test_api_token_tool_authority.py:682`
- `tests/test_api_token_tool_authority.py:686`
- `tests/test_effect_resource_bindings.py:43`
- `tests/test_effect_resource_bindings.py:463`
- `tests/test_exact_approval_ungranted_process.py:42`
- `tests/test_external_context_tool_gate.py:137`
- `tests/test_external_context_tool_gate.py:148`
- `tests/test_external_context_tool_gate.py:157`
- `tests/test_external_context_tool_gate.py:170`
- `tests/test_external_context_tool_gate.py:192`
- `tests/test_external_context_tool_gate.py:221`
- `tests/test_external_context_tool_gate.py:228`
- `tests/test_external_context_tool_gate.py:247`
- `tests/test_external_context_tool_gate.py:254`
- `tests/test_external_context_tool_gate.py:267`
- `tests/test_external_context_tool_gate.py:298`
- `tests/test_external_context_tool_gate.py:324`
- `tests/test_external_context_tool_gate.py:373`
- `tests/test_external_context_tool_gate.py:393`
- `tests/test_external_context_tool_gate.py:404`
- `tests/test_external_context_tool_gate.py:426`
- `tests/test_external_context_tool_gate.py:443`
- `tests/test_external_context_tool_gate.py:452`
- `tests/test_external_context_tool_gate.py:514`
- `tests/test_external_context_tool_gate.py:566`
- `tests/test_external_context_tool_gate.py:605`
- `tests/test_external_context_tool_gate.py:620`
- `tests/test_external_context_tool_gate.py:654`
- `tests/test_external_context_tool_gate.py:847`
- `tests/test_external_context_tool_gate.py:878`
- `tests/test_legacy_browser_authority.py:27`
- `tests/test_local_mcp_capabilities.py:163`
- `tests/test_local_mcp_capabilities.py:179`
- `tests/test_local_mcp_capabilities.py:212`
- `tests/test_local_mcp_capabilities.py:223`
- `tests/test_local_mcp_capabilities.py:255`
- `tests/test_local_mcp_capabilities.py:273`
- `tests/test_local_mcp_capabilities.py:297`
- `tests/test_local_mcp_capabilities.py:312`
- … +59 more (grep the name in repo)

## `ToolRunSecurityContext.__post_init__` — method, line 1093
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ToolRunSecurityContext.observe_messages` — method, line 1104
- **called from:**
- `src/agent_loop.py:25367`
- `src/agent_loop.py:26957`
- `src/clean_agent_preview.py:5874`
- `tests/test_api_token_tool_authority.py:233`
- `tests/test_api_token_tool_authority.py:417`
- `tests/test_api_token_tool_authority.py:441`
- `tests/test_api_token_tool_authority.py:472`
- `tests/test_api_token_tool_authority.py:504`
- `tests/test_api_token_tool_authority.py:683`
- `tests/test_api_token_tool_authority.py:688`
- `tests/test_external_context_tool_gate.py:515`
- `tests/test_external_context_tool_gate.py:567`
- `tests/test_local_mcp_capabilities.py:325`
- `tests/test_tool_approval_task_scope.py:148`
- `tests/test_tool_approval_task_scope.py:166`

## `ToolRunSecurityContext.decision_for` — method, line 1138
- **called from:**
- `src/agent_loop.py:33899`
- `src/agent_loop.py:33977`
- `src/tool_execution.py:1758`
- `src/tool_execution.py:1967`
- `src/tool_execution.py:1972`
- `tests/test_api_token_tool_authority.py:209`
- `tests/test_api_token_tool_authority.py:211`
- `tests/test_api_token_tool_authority.py:216`
- `tests/test_api_token_tool_authority.py:217`
- `tests/test_api_token_tool_authority.py:228`
- `tests/test_api_token_tool_authority.py:420`
- `tests/test_api_token_tool_authority.py:444`
- `tests/test_api_token_tool_authority.py:506`
- `tests/test_api_token_tool_authority.py:598`
- `tests/test_api_token_tool_authority.py:599`
- `tests/test_api_token_tool_authority.py:609`
- `tests/test_api_token_tool_authority.py:618`
- `tests/test_api_token_tool_authority.py:619`
- `tests/test_api_token_tool_authority.py:684`
- `tests/test_api_token_tool_authority.py:690`
- `tests/test_external_context_tool_gate.py:141`
- `tests/test_external_context_tool_gate.py:152`
- `tests/test_external_context_tool_gate.py:153`
- `tests/test_external_context_tool_gate.py:162`
- `tests/test_external_context_tool_gate.py:163`
- `tests/test_external_context_tool_gate.py:164`
- `tests/test_external_context_tool_gate.py:165`
- `tests/test_external_context_tool_gate.py:166`
- `tests/test_external_context_tool_gate.py:175`
- `tests/test_external_context_tool_gate.py:204`
- `tests/test_external_context_tool_gate.py:224`
- `tests/test_external_context_tool_gate.py:233`
- `tests/test_external_context_tool_gate.py:250`
- `tests/test_external_context_tool_gate.py:278`
- `tests/test_external_context_tool_gate.py:309`
- `tests/test_external_context_tool_gate.py:327`
- `tests/test_external_context_tool_gate.py:380`
- `tests/test_external_context_tool_gate.py:396`
- `tests/test_external_context_tool_gate.py:406`
- `tests/test_external_context_tool_gate.py:429`
- `tests/test_external_context_tool_gate.py:436`
- `tests/test_external_context_tool_gate.py:437`
- `tests/test_external_context_tool_gate.py:445`
- `tests/test_external_context_tool_gate.py:460`
- `tests/test_external_context_tool_gate.py:463`
- `tests/test_external_context_tool_gate.py:464`
- `tests/test_external_context_tool_gate.py:518`
- `tests/test_external_context_tool_gate.py:568`
- `tests/test_external_context_tool_gate.py:615`
- `tests/test_external_context_tool_gate.py:631`
- `tests/test_external_context_tool_gate.py:661`
- `tests/test_local_mcp_capabilities.py:103`
- `tests/test_local_mcp_capabilities.py:181`
- `tests/test_local_mcp_capabilities.py:215`
- `tests/test_local_mcp_capabilities.py:259`
- `tests/test_local_mcp_capabilities.py:263`
- `tests/test_local_mcp_capabilities.py:267`
- `tests/test_local_mcp_capabilities.py:277`
- `tests/test_local_mcp_capabilities.py:278`
- `tests/test_local_mcp_capabilities.py:279`
- … +26 more (grep the name in repo)

## `ToolRunSecurityContext.observe_tool_result` — method, line 1212
- **called from:**
- `src/agent_loop.py:27307`
- `src/agent_loop.py:27503`
- `src/agent_loop.py:27625`
- `src/agent_loop.py:34419`
- `src/tool_execution.py:2015`
- `tests/test_external_context_tool_gate.py:139`
- `tests/test_external_context_tool_gate.py:194`
- `tests/test_external_context_tool_gate.py:222`
- `tests/test_external_context_tool_gate.py:230`
- `tests/test_external_context_tool_gate.py:248`
- `tests/test_external_context_tool_gate.py:256`
- `tests/test_external_context_tool_gate.py:259`
- `tests/test_external_context_tool_gate.py:275`
- `tests/test_external_context_tool_gate.py:306`
- `tests/test_external_context_tool_gate.py:325`
- `tests/test_external_context_tool_gate.py:374`
- `tests/test_external_context_tool_gate.py:454`
- `tests/test_external_context_tool_gate.py:609`
- `tests/test_external_context_tool_gate.py:624`
- `tests/test_external_context_tool_gate.py:655`
- `tests/test_local_mcp_capabilities.py:164`
- `tests/test_local_mcp_capabilities.py:180`
- `tests/test_local_mcp_capabilities.py:213`
- `tests/test_local_mcp_capabilities.py:224`
- `tests/test_local_mcp_capabilities.py:256`
- `tests/test_local_mcp_capabilities.py:274`
- `tests/test_local_mcp_capabilities.py:298`
- `tests/test_local_mcp_capabilities.py:313`
- `tests/test_local_mcp_capabilities.py:316`
- `tests/test_local_mcp_capabilities.py:338`
- `tests/test_local_mcp_capabilities.py:346`
- `tests/test_local_mcp_capabilities.py:364`
- `tests/test_local_mcp_capabilities.py:442`
- `tests/test_local_mcp_capabilities.py:491`
- `tests/test_local_mcp_capabilities.py:498`
- `tests/test_local_mcp_capabilities.py:612`
- `tests/test_local_mcp_capabilities.py:671`
- `tests/test_local_mcp_capabilities.py:699`
- `tests/test_local_mcp_capabilities.py:727`
- `tests/test_local_mcp_capabilities.py:752`
- `tests/test_local_mcp_capabilities.py:781`
- `tests/test_local_mcp_capabilities.py:932`
- `tests/test_local_mcp_capabilities.py:974`

## `blocked_tool_result` — function, line 1230
- **called from:**
- `src/tool_execution.py:1759`
- `src/tool_execution.py:1981`
