# `src/agent_runtime/owned_resources.py` — definitions & call sites

24 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_args` — function, line 18
- **called from:**
- `src/agent_runtime/owned_resources.py:247`
- `src/agent_runtime/owned_resources.py:281`
- `src/agent_runtime/owned_resources.py:330`

## `_selector` — function, line 28
- **called from:**
- `src/agent_runtime/owned_resources.py:294`
- `src/agent_runtime/owned_resources.py:338`
- `src/agent_runtime/owned_resources.py:355`
- `src/agent_runtime/owned_resources.py:363`
- `src/agent_runtime/owned_resources.py:402`

## `_revision` — function, line 38
- **called from:**
- `src/agent_runtime/owned_resources.py:54`

## `_record` — function, line 49
- **called from:**
- `src/agent_loop.py:10999`
- `src/agent_loop.py:11001`
- `src/agent_runtime/owned_resources.py:236`
- `src/agent_runtime/owned_resources.py:312`
- `src/agent_runtime/owned_resources.py:342`
- `src/agent_runtime/owned_resources.py:371`
- `src/model_capability_readers/llamacpp.py:306`
- `src/model_capability_readers/llamacpp.py:328`

## `_row` — function, line 57
- **called from:**
- `src/agent_runtime/owned_resources.py:237`
- `src/agent_runtime/owned_resources.py:311`
- `src/agent_runtime/owned_resources.py:341`
- `src/agent_runtime/owned_resources.py:370`
- `src/agent_tools/bg_job_tools.py:100`
- `src/fixture_email.py:133`
- `src/fixture_email.py:182`
- `tests/test_token_cache_atomic_swap.py:59`
- `tests/test_token_cache_atomic_swap.py:67`
- `tests/test_token_cache_atomic_swap.py:68`
- `tests/test_token_cache_atomic_swap.py:69`
- `tests/test_token_cache_atomic_swap.py:89`
- `tests/test_token_cache_atomic_swap.py:96`
- `tests/test_token_cache_atomic_swap.py:107`
- `tests/test_token_cache_atomic_swap.py:146`
- `tests/test_token_cache_atomic_swap.py:163`
- `tests/test_token_cache_atomic_swap.py:164`
- `tests/test_token_cache_atomic_swap.py:167`
- `tests/test_token_cache_atomic_swap.py:208`
- `tests/test_token_cache_atomic_swap.py:216`
- `tests/test_token_cache_atomic_swap.py:227`
- `tests/test_token_cache_atomic_swap.py:229`

## `AttachmentResource` — class, line 72
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/owned_resources.py:99`

## `AttachmentResource.__post_init__` — method, line 76
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AttachmentResource.to_dict` — method, line 80
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

## `_attachment` — function, line 84
- **called from:**
- `src/agent_runtime/owned_resources.py:227`
- `src/agent_runtime/owned_resources.py:381`

## `_vault_revision` — function, line 105
- **called from:**
- `src/agent_runtime/owned_resources.py:118`
- `src/agent_runtime/owned_resources.py:119`
- `src/agent_runtime/owned_resources.py:138`
- `src/agent_runtime/owned_resources.py:149`

## `observe_vault_records` — function, line 113
- **called from:**
- `src/tools/vault.py:73`
- `tests/test_owned_resource_identity.py:267`
- `tests/test_owned_resource_identity.py:408`
- `tests/test_owned_resource_identity.py:422`
- `tests/test_owned_resource_identity.py:426`
- `tests/test_owned_resource_identity.py:427`

## `_vault_resource` — function, line 136
- **called from:**
- `src/agent_runtime/owned_resources.py:222`
- `src/agent_runtime/owned_resources.py:231`
- `src/agent_runtime/owned_resources.py:405`

## `_vault_selector` — function, line 147
- **called from:**
- `src/agent_runtime/owned_resources.py:402`

## `_memory_record` — function, line 160
- **called from:**
- `src/agent_runtime/owned_resources.py:234`
- `src/agent_runtime/owned_resources.py:393`

## `BoundOwnedOperation` — class, line 177
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/owned_resources.py:406`
- `tests/test_effect_verification_adapters.py:226`

## `BoundOwnedOperation.__post_init__` — method, line 189
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `BoundOwnedOperation.to_dict` — method, line 209
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

## `BoundOwnedOperation.validate` — method, line 219
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

## `needs_owned_binding` — function, line 241
- **called from:**
- `src/tool_approvals.py:445`
- `src/tool_execution.py:1856`
- `tests/test_runtime_resource_integration.py:342`

## `resolve_owned_operation` — function, line 275
- **called from:**
- `src/agent_runtime/owned_resources.py:413`
- `src/tool_approvals.py:446`
- `tests/test_owned_resource_identity.py:197`
- `tests/test_owned_resource_identity.py:201`
- `tests/test_owned_resource_identity.py:207`
- `tests/test_owned_resource_identity.py:210`
- `tests/test_owned_resource_identity.py:228`
- `tests/test_owned_resource_identity.py:253`
- `tests/test_owned_resource_identity.py:269`
- `tests/test_owned_resource_identity.py:280`
- `tests/test_owned_resource_identity.py:282`
- `tests/test_owned_resource_identity.py:370`
- `tests/test_owned_resource_identity.py:376`
- `tests/test_owned_resource_identity.py:414`
- `tests/test_owned_resource_identity.py:423`

## `admit_owned_operation` — function, line 412
- **called from:**
- `src/tool_execution.py:1859`
- `tests/test_owned_resource_identity.py:289`

## `active_owned_operation` — function, line 429
- **called from:**
- `src/agent_runtime/effect_adapters.py:59`
- `src/agent_runtime/owned_resources.py:447`
- `src/ai_interaction.py:403`
- `src/tool_execution.py:1633`
- `src/tool_execution.py:1646`
- `src/tool_execution.py:1671`
- `src/tool_execution.py:2160`
- `src/tools/notes.py:81`
- `src/tools/vault.py:72`
- `tests/test_owned_resource_identity.py:97`
- `tests/test_owned_resource_identity.py:105`
- `tests/test_owned_resource_identity.py:291`
- `tests/test_owned_resource_identity.py:303`
- `tests/test_owned_resource_identity.py:305`

## `bind_owned_operation` — function, line 434
- decorator: `contextmanager`
- **called from:**
- `src/tool_execution.py:1997`
- `tests/test_owned_resource_identity.py:229`
- `tests/test_owned_resource_identity.py:297`

## `bound_attachment_path` — function, line 446
- **called from:**
- `src/agent_tools/media_tools.py:452`
- `tests/test_owned_resource_identity.py:230`
- `tests/test_owned_resource_identity.py:232`
