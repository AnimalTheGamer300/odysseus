# `src/agent_runtime/remote_resources.py` — definitions & call sites

15 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `endpoint_identity` — function, line 19
- **called from:**
- `src/agent_runtime/owned_resources.py:109`
- `src/agent_runtime/remote_resources.py:54`
- `src/agent_runtime/remote_resources.py:78`
- `src/agent_runtime/remote_resources.py:84`
- `src/mcp_manager.py:187`
- `src/tool_execution.py:112`
- `tests/test_local_mcp_capabilities.py:137`
- `tests/test_local_mcp_capabilities.py:418`
- `tests/test_remote_resource_identity.py:56`
- `tests/test_remote_resource_identity.py:98`

## `configuration_incarnation` — function, line 39
- **called from:**
- `routes/chat_routes.py:853`
- `src/agent_runtime/owned_resources.py:110`
- `src/agent_runtime/owned_resources.py:131`
- `src/agent_runtime/owned_resources.py:172`
- `src/agent_runtime/owned_resources.py:213`
- `src/agent_runtime/remote_resources.py:57`
- `src/agent_runtime/remote_resources.py:73`
- `src/agent_runtime/remote_resources.py:85`
- `src/agent_runtime/remote_resources.py:182`
- `src/mcp_manager.py:188`
- `tests/test_local_mcp_capabilities.py:125`
- `tests/test_local_mcp_capabilities.py:138`
- `tests/test_local_mcp_capabilities.py:419`
- `tests/test_remote_resource_identity.py:56`
- `tests/test_remote_resource_identity.py:98`

## `_client_resource` — function, line 44
- **called from:**
- `src/agent_runtime/remote_resources.py:115`

## `http_bridge_resource` — function, line 66
- **called from:**
- `src/agent_runtime/remote_resources.py:112`

## `integration_resource` — function, line 81
- **called from:**
- `src/agent_runtime/remote_resources.py:125`
- `src/integrations.py:522`
- `tests/test_remote_resource_identity.py:212`
- `tests/test_remote_resource_identity.py:388`

## `api_arguments` — function, line 89
- **called from:**
- `src/agent_runtime/remote_resources.py:120`

## `resolve_backend` — function, line 106
- **called from:**
- `src/agent_runtime/remote_resources.py:156`
- `src/agent_runtime/remote_resources.py:185`
- `src/agent_runtime/remote_resources.py:195`
- `src/tool_approvals.py:411`

## `seal_backends` — function, line 147
- **called from:**
- `src/agent_runtime/authority.py:165`
- `src/agent_runtime/authority.py:510`
- `tests/runtime_evidence_helpers.py:43`
- `tests/test_remote_resource_identity.py:263`
- `tests/test_remote_resource_identity.py:279`
- `tests/test_remote_resource_identity.py:346`
- `tests/test_remote_resource_identity.py:364`

## `BoundBackendOperation` — class, line 163
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/remote_resources.py:217`
- `src/tool_approvals.py:415`
- `tests/test_effect_verification_adapters.py:259`
- `tests/test_effect_verification_adapters.py:274`
- `tests/test_effect_verification_adapters.py:419`

## `BoundBackendOperation.__post_init__` — method, line 171
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `BoundBackendOperation.to_dict` — method, line 177
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5624`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28789`
- `src/agent_loop.py:31316`
- `src/agent_loop.py:31789`
- `src/agent_loop.py:32054`
- `src/agent_loop.py:32094`
- `src/agent_loop.py:32125`
- `src/agent_loop.py:32178`
- `src/agent_loop.py:32306`
- `src/agent_loop.py:32638`
- `src/agent_loop.py:34858`
- `src/agent_loop.py:36867`
- `src/agent_loop.py:37190`
- `src/agent_loop.py:37403`
- `src/agent_loop.py:37458`
- `src/agent_loop.py:37515`
- `src/agent_loop.py:37849`
- `src/agent_loop.py:37861`
- `src/agent_loop.py:37967`
- `src/agent_loop.py:38889`
- `src/agent_loop.py:38890`
- `src/agent_loop.py:38895`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:653`
- `src/agent_runtime/authority.py:677`
- `src/agent_runtime/authority.py:677`
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

## `BoundBackendOperation.validate` — method, line 184
- **called from:**
- `scripts/eval_ajax_basic_tools.py:59`
- `scripts/test_clean_tool_loop.py:118`
- `src/agent_runtime/authority.py:250`
- `src/agent_runtime/effect_adapters.py:392`
- `src/agent_runtime/effect_adapters.py:397`
- `src/agent_runtime/effect_adapters.py:408`
- `src/agent_runtime/owned_resources.py:229`
- `src/agent_runtime/owned_resources.py:408`
- `src/agent_runtime/owned_resources.py:422`
- `src/agent_runtime/owned_resources.py:438`
- `src/agent_runtime/owned_resources.py:450`
- `src/agent_runtime/process_resources.py:69`
- `src/agent_runtime/process_resources.py:153`
- `src/agent_runtime/process_resources.py:191`
- `src/agent_runtime/process_resources.py:198`
- `src/agent_runtime/process_resources.py:208`
- `src/agent_runtime/process_resources.py:266`
- `src/agent_runtime/process_resources.py:272`
- `src/agent_runtime/process_resources.py:326`
- `src/agent_runtime/process_resources.py:339`
- `src/agent_runtime/process_resources.py:357`
- `src/agent_runtime/process_resources.py:412`
- `src/agent_runtime/remote_resources.py:219`
- `src/agent_runtime/resource_binding.py:66`
- `src/agent_runtime/resource_binding.py:81`
- `src/agent_runtime/resource_binding.py:87`
- `src/agent_runtime/resource_binding.py:197`
- `src/agent_runtime/resource_binding.py:213`
- `src/agent_runtime/resources.py:380`
- `src/agent_runtime/resources.py:432`
- `src/agent_runtime/resources.py:433`
- `src/agent_runtime/resources.py:517`
- `src/agent_runtime/resources.py:560`
- `src/agent_tools/bg_job_tools.py:95`
- `src/agent_tools/filesystem_tools.py:1001`
- `src/ai_interaction.py:405`
- `src/bg_jobs.py:168`
- `src/browser_identity.py:134`
- `src/browser_identity.py:202`
- `src/browser_identity.py:491`
- `src/browser_identity.py:502`
- `src/browser_identity.py:511`
- `src/browser_identity.py:537`
- `src/browser_identity.py:541`
- `src/browser_identity.py:572`
- `src/browser_identity.py:583`
- `src/browser_identity.py:595`
- `src/browser_identity.py:604`
- `src/browser_identity.py:632`
- `src/browser_identity.py:636`
- `src/clean_agent_preview.py:7436`
- `src/clean_agent_preview.py:7809`
- `src/containment_worker.py:54`
- `src/containment_worker.py:57`
- `src/tool_execution.py:1251`
- `src/tool_execution.py:1635`
- `src/tool_execution.py:1673`
- `src/tool_execution.py:1989`
- `src/tool_execution.py:2159`
- `src/tool_execution.py:2162`
- … +28 more (grep the name in repo)

## `bind_backend_for_operation` — function, line 194
- **called from:**
- `src/tool_execution.py:1832`
- `tests/test_remote_resource_identity.py:172`
- `tests/test_remote_resource_identity.py:242`
- `tests/test_wave3_local_control.py:163`
- `tests/test_wave3_local_control.py:185`

## `active_backend_operation` — function, line 226
- **called from:**
- `src/agent_runtime/effect_adapters.py:60`
- `src/agent_runtime/local_model_control.py:51`
- `src/integrations.py:521`
- `src/mcp_manager.py:588`
- `src/tool_execution.py:1485`
- `src/tool_execution.py:2157`
- `src/tools/system.py:730`
- `tests/test_owned_resource_identity.py:292`
- `tests/test_owned_resource_identity.py:304`
- `tests/test_remote_resource_identity.py:82`
- `tests/test_remote_resource_identity.py:234`
- `tests/test_remote_resource_identity.py:249`
- `tests/test_remote_resource_identity.py:250`

## `bind_backend_operation` — function, line 231
- decorator: `contextmanager`
- **called from:**
- `src/tool_execution.py:1997`
- `tests/test_remote_resource_identity.py:176`
- `tests/test_remote_resource_identity.py:243`
- `tests/test_wave3_local_control.py:165`
- `tests/test_wave3_local_control.py:187`
