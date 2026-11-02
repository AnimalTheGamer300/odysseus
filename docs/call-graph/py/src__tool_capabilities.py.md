# `src/tool_capabilities.py` — definitions & call sites

17 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ToolEffect` — class, line 21
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResultIntegrity` — class, line 37
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ToolCapabilities` — class, line 44
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/tool_capabilities.py:54`
- `src/tool_capabilities.py:279`
- `src/tool_capabilities.py:467`
- `src/tool_capabilities.py:481`

## `_capabilities` — function, line 50
- **called from:**
- `src/tool_capabilities.py:65`
- `src/tool_capabilities.py:268`
- `src/tool_capabilities.py:284`
- `src/tool_capabilities.py:473`
- `src/tool_capabilities.py:487`

## `_register` — function, line 60
- **called from:**
- `src/tool_capabilities.py:72`
- `src/tool_capabilities.py:76`
- `src/tool_capabilities.py:91`
- `src/tool_capabilities.py:96`
- `src/tool_capabilities.py:101`
- `src/tool_capabilities.py:106`
- `src/tool_capabilities.py:112`
- `src/tool_capabilities.py:129`
- `src/tool_capabilities.py:134`
- `src/tool_capabilities.py:141`
- `src/tool_capabilities.py:158`
- `src/tool_capabilities.py:170`
- `src/tool_capabilities.py:178`
- `src/tool_capabilities.py:183`
- `src/tool_capabilities.py:189`
- `src/tool_capabilities.py:194`
- `src/tool_capabilities.py:200`
- `src/tool_capabilities.py:206`
- `src/tool_capabilities.py:220`
- `src/tool_capabilities.py:226`
- `src/tool_capabilities.py:232`
- `src/tool_capabilities.py:247`

## `capabilities_for_tool` — function, line 298
- **called from:**
- `src/tool_capabilities.py:458`
- `tests/test_external_context_tool_gate.py:131`
- `tests/test_external_context_tool_gate.py:251`
- `tests/test_external_context_tool_gate.py:300`
- `tests/test_external_context_tool_gate.py:326`
- `tests/test_external_context_tool_gate.py:343`
- `tests/test_external_context_tool_gate.py:522`
- `tests/test_external_context_tool_gate.py:537`

## `_action_from_content` — function, line 412
- **called from:**
- `src/tool_capabilities.py:462`

## `capabilities_for_action` — function, line 456
- **called from:**
- `src/agent_loop.py:3576`
- `src/agent_loop.py:6326`
- `src/teacher_escalation.py:772`
- `src/tool_approvals.py:248`
- `src/tool_capabilities.py:527`
- `src/tool_capabilities.py:670`
- `tests/test_external_context_tool_gate.py:564`
- `tests/test_external_context_tool_gate.py:589`
- `tests/test_external_context_tool_gate.py:619`
- `tests/test_external_context_tool_gate.py:647`
- `tests/test_external_context_tool_gate.py:653`
- `tests/test_foreground_model_routing.py:284`
- `tests/test_foreground_model_routing.py:327`
- `tests/test_foreground_model_routing.py:360`
- `tests/test_foreground_model_routing.py:397`
- `tests/test_foreground_model_routing.py:429`
- `tests/test_scheduler_prompt_cache_time.py:85`
- `tests/test_skills_routes_owner_update.py:166`
- `tests/test_tool_approval_single_action_scope.py:25`
- `tests/test_tool_approval_task_scope.py:36`
- `tests/test_tool_approvals.py:24`
- `tests/test_tool_approvals.py:200`
- `tests/test_tool_approvals.py:252`

## `tool_result_is_successful` — function, line 494
- **called from:**
- `src/agent_loop.py:5133`
- `src/agent_loop.py:6484`
- `src/tool_capabilities.py:530`

## `tool_result_should_arm_gate` — function, line 506
- **called from:**
- `src/agent_loop.py:3577`
- `src/agent_loop.py:3636`
- `src/tool_capabilities.py:692`
- `tests/test_external_context_tool_gate.py:177`
- `tests/test_external_context_tool_gate.py:205`
- `tests/test_external_context_tool_gate.py:225`
- `tests/test_external_context_tool_gate.py:236`
- `tests/test_external_context_tool_gate.py:254`

## `ToolGateDecision` — class, line 569
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/tool_capabilities.py:659`
- `src/tool_capabilities.py:667`
- `src/tool_capabilities.py:669`
- `src/tool_capabilities.py:673`
- `src/tool_capabilities.py:677`

## `messages_contain_external_untrusted_context` — function, line 586
- **called from:**
- `src/agent_loop.py:4020`
- `src/tool_capabilities.py:639`
- `src/tool_capabilities.py:651`
- `tests/test_external_context_tool_gate.py:394`
- `tests/test_external_context_tool_gate.py:407`
- `tests/test_external_context_tool_gate.py:421`
- `tests/test_external_context_tool_gate.py:423`
- `tests/test_external_context_tool_gate.py:464`
- `tests/test_external_context_tool_gate.py:480`
- `tests/test_external_context_tool_gate.py:500`
- `tests/test_external_context_tool_gate.py:515`
- `tests/test_external_context_tool_gate.py:736`

## `ToolRunSecurityContext` — class, line 616
- decorator: `dataclass`
- **called from:**
- `src/agent_loop.py:4013`
- `tests/test_api_token_tool_authority.py:53`
- `tests/test_api_token_tool_authority.py:77`
- `tests/test_api_token_tool_authority.py:108`
- `tests/test_api_token_tool_authority.py:140`
- `tests/test_api_token_tool_authority.py:230`
- `tests/test_api_token_tool_authority.py:240`
- `tests/test_api_token_tool_authority.py:250`
- `tests/test_api_token_tool_authority.py:319`
- `tests/test_api_token_tool_authority.py:323`
- `tests/test_external_context_tool_gate.py:99`
- `tests/test_external_context_tool_gate.py:123`
- `tests/test_external_context_tool_gate.py:152`
- `tests/test_external_context_tool_gate.py:159`
- `tests/test_external_context_tool_gate.py:178`
- `tests/test_external_context_tool_gate.py:185`
- `tests/test_external_context_tool_gate.py:198`
- `tests/test_external_context_tool_gate.py:229`
- `tests/test_external_context_tool_gate.py:255`
- `tests/test_external_context_tool_gate.py:304`
- `tests/test_external_context_tool_gate.py:324`
- `tests/test_external_context_tool_gate.py:335`
- `tests/test_external_context_tool_gate.py:341`
- `tests/test_external_context_tool_gate.py:358`
- `tests/test_external_context_tool_gate.py:367`
- `tests/test_external_context_tool_gate.py:429`
- `tests/test_external_context_tool_gate.py:481`
- `tests/test_external_context_tool_gate.py:520`
- `tests/test_external_context_tool_gate.py:535`
- `tests/test_external_context_tool_gate.py:569`
- `tests/test_external_context_tool_gate.py:750`
- `tests/test_external_context_tool_gate.py:781`
- `tests/test_tool_approval_single_action_scope.py:46`
- `tests/test_tool_approval_task_scope.py:85`
- `tests/test_tool_approval_task_scope.py:92`
- `tests/test_tool_approval_task_scope.py:138`
- `tests/test_tool_approval_task_scope.py:156`
- `tests/test_tool_approvals.py:176`
- `tests/test_tool_approvals.py:230`
- `tests/test_tool_approvals.py:274`
- `tests/test_tool_approvals.py:381`
- `tests/test_tool_approvals.py:417`
- `tests/test_tool_approvals.py:453`

## `ToolRunSecurityContext.observe_messages` — method, line 631
- **called from:**
- `src/agent_loop.py:4889`
- `src/agent_loop.py:5392`
- `tests/test_api_token_tool_authority.py:54`
- `tests/test_api_token_tool_authority.py:78`
- `tests/test_api_token_tool_authority.py:109`
- `tests/test_api_token_tool_authority.py:141`
- `tests/test_api_token_tool_authority.py:320`
- `tests/test_api_token_tool_authority.py:325`
- `tests/test_external_context_tool_gate.py:430`
- `tests/test_external_context_tool_gate.py:482`
- `tests/test_tool_approval_task_scope.py:139`
- `tests/test_tool_approval_task_scope.py:157`

## `ToolRunSecurityContext.decision_for` — method, line 654
- **called from:**
- `src/agent_loop.py:6215`
- `src/tool_execution.py:940`
- `tests/test_api_token_tool_authority.py:57`
- `tests/test_api_token_tool_authority.py:81`
- `tests/test_api_token_tool_authority.py:143`
- `tests/test_api_token_tool_authority.py:235`
- `tests/test_api_token_tool_authority.py:236`
- `tests/test_api_token_tool_authority.py:246`
- `tests/test_api_token_tool_authority.py:255`
- `tests/test_api_token_tool_authority.py:256`
- `tests/test_api_token_tool_authority.py:321`
- `tests/test_api_token_tool_authority.py:327`
- `tests/test_external_context_tool_gate.py:103`
- `tests/test_external_context_tool_gate.py:135`
- `tests/test_external_context_tool_gate.py:155`
- `tests/test_external_context_tool_gate.py:164`
- `tests/test_external_context_tool_gate.py:181`
- `tests/test_external_context_tool_gate.py:209`
- `tests/test_external_context_tool_gate.py:240`
- `tests/test_external_context_tool_gate.py:258`
- `tests/test_external_context_tool_gate.py:311`
- `tests/test_external_context_tool_gate.py:327`
- `tests/test_external_context_tool_gate.py:337`
- `tests/test_external_context_tool_gate.py:344`
- `tests/test_external_context_tool_gate.py:351`
- `tests/test_external_context_tool_gate.py:352`
- `tests/test_external_context_tool_gate.py:360`
- `tests/test_external_context_tool_gate.py:375`
- `tests/test_external_context_tool_gate.py:378`
- `tests/test_external_context_tool_gate.py:379`
- `tests/test_external_context_tool_gate.py:433`
- `tests/test_external_context_tool_gate.py:483`
- `tests/test_external_context_tool_gate.py:530`
- `tests/test_external_context_tool_gate.py:546`
- `tests/test_external_context_tool_gate.py:576`
- `tests/test_tool_approval_single_action_scope.py:50`
- `tests/test_tool_approval_task_scope.py:89`
- `tests/test_tool_approval_task_scope.py:93`
- `tests/test_tool_approval_task_scope.py:141`
- `tests/test_tool_approval_task_scope.py:158`

## `ToolRunSecurityContext.observe_tool_result` — method, line 686
- **called from:**
- `src/agent_loop.py:6409`
- `src/tool_execution.py:981`
- `tests/test_external_context_tool_gate.py:101`
- `tests/test_external_context_tool_gate.py:125`
- `tests/test_external_context_tool_gate.py:153`
- `tests/test_external_context_tool_gate.py:161`
- `tests/test_external_context_tool_gate.py:179`
- `tests/test_external_context_tool_gate.py:187`
- `tests/test_external_context_tool_gate.py:190`
- `tests/test_external_context_tool_gate.py:206`
- `tests/test_external_context_tool_gate.py:237`
- `tests/test_external_context_tool_gate.py:256`
- `tests/test_external_context_tool_gate.py:305`
- `tests/test_external_context_tool_gate.py:369`
- `tests/test_external_context_tool_gate.py:524`
- `tests/test_external_context_tool_gate.py:539`
- `tests/test_external_context_tool_gate.py:570`

## `blocked_tool_result` — function, line 699
- **called from:**
- `src/tool_execution.py:949`
