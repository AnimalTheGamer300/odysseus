# `src/agent_runtime/journal.py` — definitions & call sites

23 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ActionReceipt` — class, line 18
- decorator: `dataclass`
- **called from:**
- `src/agent_runtime/journal.py:121`

## `ActionReceipt.transition` — method, line 34
- **called from:**
- `src/agent_runtime/journal.py:40`
- `src/agent_runtime/journal.py:58`
- `src/agent_runtime/journal.py:128`
- `src/agent_runtime/journal.py:173`
- `src/agent_runtime/journal.py:187`
- `src/agent_runtime/journal.py:191`
- `src/agent_runtime/journal.py:226`
- `src/agent_runtime/journal.py:266`
- `src/agent_runtime/journal.py:276`
- `static/js/chat.js:4275`

## `ActionReceipt.normalize` — method, line 37
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

## `ActionReceipt.finish` — method, line 44
- **called from:**
- `src/agent_loop.py:33038`
- `src/agent_loop.py:33051`
- `src/agent_loop.py:33059`
- `src/agent_loop.py:34919`
- `src/agent_runtime/journal.py:267`
- `src/agent_runtime/journal.py:269`
- `src/containment.py:1512`
- `src/containment.py:1518`
- `src/containment.py:1527`
- `src/containment.py:1542`
- `src/containment.py:1545`
- `src/pdf_forms.py:338`
- `tests/test_effect_verification_adapters.py:55`
- `tests/test_effect_verification_adapters.py:121`
- `tests/test_effect_verification_adapters.py:215`
- `tests/test_effect_verification_adapters.py:431`
- `static/js/calendar.js:34`
- `static/js/calendar.js:42`
- `static/js/calendar.js:43`
- `static/js/calendar.js:45`
- `static/js/chat.js:2122`
- `static/js/colorPicker.js:237`
- `static/js/colorPicker.js:243`
- `static/js/editor/adjustment-layer.js:205`
- `static/js/editor/adjustment-layer.js:211`
- `static/js/editor/adjustment-layer.js:215`
- `static/js/editor/ai-inpaint.js:280`
- `static/js/editor/ai-operation.js:19`
- `static/js/editor/ai-tool-runner.js:164`
- `static/js/editor/ai-tools-misc.js:157`
- `static/js/editor/ai-tools-misc.js:206`
- `static/js/editor/effects.js:364`
- `static/js/editor/effects.js:372`
- `static/js/editor/effects.js:376`
- `static/js/editor/layer-panel.js:1424`
- `static/js/editor/layer-panel.js:1426`
- `static/js/editor/layer-panel.js:1431`
- `static/js/editor/precision-guides.js:210`
- `static/js/editor/precision-guides.js:229`
- `static/js/editor/tools/pen-path.js:39`
- `static/js/editor/tools/pen-path.js:46`
- `static/js/features/notes/ui/cardInteractions.js:234`
- `static/js/features/notes/ui/cardInteractions.js:238`
- `static/js/features/notes/ui/colors.js:63`
- `static/js/features/notes/ui/colors.js:71`
- `static/js/features/notes/ui/colors.js:72`
- `static/js/features/notes/ui/colors.js:75`
- `static/js/fileHandler.js:96`
- `static/js/fileHandler.js:134`
- `static/js/fileHandler.js:135`
- `static/js/fileHandler.js:172`
- `static/js/fileHandler.js:175`
- `static/js/gallery.js:2484`
- `static/js/gallery.js:2487`
- `static/js/galleryEditor.js:430`
- `static/js/galleryEditor.js:4572`
- `static/js/galleryEditor.js:4573`
- `static/js/galleryEditor.js:4575`
- `static/js/galleryEditor.js:4655`
- `static/js/galleryEditor.js:4659`
- … +4 more (grep the name in repo)

## `ActionReceipt.to_dict` — method, line 60
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

## `ActionJournal` — class, line 65
- decorator: `dataclass`
- **called from:**
- `src/agent_runtime/completion.py:227`
- `tests/test_browser_resource_identity.py:114`
- `tests/test_effect_resource_bindings.py:33`
- `tests/test_effect_verification_adapters.py:43`
- `tests/test_image_creation_routing.py:144`
- `tests/test_nested_invocation_ownership.py:141`
- `tests/test_request_authority.py:588`
- `tests/test_runtime_evidence_contract.py:91`
- `tests/test_runtime_evidence_contract.py:270`
- `tests/test_runtime_evidence_contract.py:293`
- `tests/test_runtime_evidence_contract.py:367`
- `tests/test_runtime_evidence_contract.py:388`
- `tests/test_runtime_evidence_contract.py:404`

## `ActionJournal.effect_entries` — method, line 75
- **called from:**
- `src/agent_runtime/completion.py:30`

## `ActionJournal.partial_reads` — method, line 100
- **called from:**
- `src/agent_runtime/completion.py:32`

## `ActionJournal.capture_versions` — method, line 109
- **called from:**
- `src/agent_runtime/journal.py:255`
- `src/agent_runtime/journal.py:261`

## `ActionJournal.propose` — method, line 116
- **called from:**
- `src/agent_runtime/journal.py:167`
- `tests/test_effect_verification_adapters.py:50`
- `tests/test_effect_verification_adapters.py:119`
- `tests/test_effect_verification_adapters.py:213`
- `tests/test_effect_verification_adapters.py:429`
- `tests/test_nested_invocation_ownership.py:142`
- `tests/test_runtime_evidence_contract.py:92`

## `ActionJournal.to_list` — method, line 132
- **called from:**
- `src/agent_loop.py:38957`
- `src/agent_runtime/completion.py:388`
- `src/agent_runtime/completion.py:389`
- `tests/test_agent_evidence.py:850`
- `tests/test_agent_trace.py:45`
- `tests/test_agent_trace.py:45`
- `tests/test_agent_trace.py:215`
- `tests/test_nested_invocation_ownership.py:117`
- `tests/test_nested_invocation_ownership.py:128`
- `tests/test_nested_invocation_ownership.py:132`
- `tests/test_runtime_evidence_contract.py:284`
- `tests/test_runtime_evidence_contract.py:284`

## `ActionJournal.evidence_events` — method, line 135
- **called from:**
- `src/agent_runtime/completion.py:29`
- `tests/test_runtime_evidence_contract.py:282`
- `tests/test_runtime_evidence_contract.py:283`
- `tests/test_runtime_evidence_contract.py:298`
- `tests/test_runtime_evidence_contract.py:300`
- `tests/test_runtime_evidence_contract.py:380`
- `tests/test_runtime_evidence_contract.py:395`

## `bind_journal` — function, line 151
- decorator: `contextmanager`
- **called from:**
- `src/agent_runtime/completion.py:242`
- `tests/test_browser_resource_identity.py:127`
- `tests/test_effect_resource_bindings.py:40`
- `tests/test_effect_resource_bindings.py:459`
- `tests/test_image_creation_routing.py:145`
- `tests/test_nested_invocation_ownership.py:183`
- `tests/test_request_authority.py:589`
- `tests/test_runtime_evidence_contract.py:273`
- `tests/test_runtime_evidence_contract.py:294`
- `tests/test_runtime_evidence_contract.py:368`
- `tests/test_runtime_evidence_contract.py:389`
- `tests/test_runtime_evidence_contract.py:405`

## `current_journal` — function, line 161
- **called from:**
- `src/agent_runtime/completion.py:226`
- `src/agent_runtime/journal.py:250`
- `src/agent_runtime/journal.py:259`
- `src/agent_runtime/journal.py:277`
- `src/teacher_escalation.py:47`
- `tests/test_completion_boundary.py:144`
- `tests/test_completion_boundary.py:159`
- `tests/test_completion_boundary.py:308`
- `tests/test_completion_boundary.py:328`
- `tests/test_effect_verification_adapters.py:449`
- `tests/test_headless_completion_consumers.py:143`
- `tests/test_headless_completion_consumers.py:166`
- `tests/test_nested_invocation_ownership.py:53`
- `tests/test_nested_invocation_ownership.py:59`
- `tests/test_nested_invocation_ownership.py:61`
- `tests/test_nested_invocation_ownership.py:89`
- `tests/test_nested_invocation_ownership.py:107`
- `tests/test_nested_invocation_ownership.py:115`
- `tests/test_nested_invocation_ownership.py:117`
- `tests/test_nested_invocation_ownership.py:119`
- `tests/test_nested_invocation_ownership.py:135`
- `tests/test_nested_invocation_ownership.py:147`
- `tests/test_nested_invocation_ownership.py:166`
- `tests/test_nested_invocation_ownership.py:178`
- `tests/test_nested_invocation_ownership.py:191`
- `tests/test_nested_invocation_ownership.py:233`
- `tests/test_nested_invocation_ownership.py:268`
- `tests/test_nested_invocation_ownership.py:291`
- `tests/test_nested_invocation_ownership.py:316`
- `tests/test_nested_invocation_ownership.py:392`
- `tests/test_nested_invocation_ownership.py:413`
- `tests/test_nested_invocation_ownership.py:432`
- `tests/test_nested_invocation_ownership.py:467`
- `tests/test_nested_invocation_ownership.py:500`
- `tests/test_nested_invocation_ownership.py:521`
- `tests/test_nested_invocation_ownership.py:550`
- `tests/test_nested_invocation_ownership.py:606`
- `tests/test_runtime_evidence_contract.py:109`
- `tests/test_runtime_evidence_contract.py:355`
- `tests/test_runtime_evidence_contract.py:359`

## `propose_action` — function, line 165
- **called from:**
- `src/agent_loop.py:33020`
- `src/agent_runtime/journal.py:247`
- `tests/test_runtime_evidence_contract.py:274`

## `mark_authorized` — function, line 170
- **called from:**
- `src/agent_runtime/journal.py:189`
- `src/tool_execution.py:2201`

## `mark_dispatch` — function, line 176
- **called from:**
- `src/agent_runtime/journal.py:197`
- `src/tool_execution.py:2252`
- `tests/runtime_evidence_helpers.py:53`
- `tests/test_runtime_evidence_contract.py:226`

## `dispatched` — function (async), line 194
- **called from:**
- `src/tool_execution.py:2215`
- `src/tool_execution.py:2242`
- `src/tool_execution.py:2286`
- `src/tool_execution.py:2299`
- `src/tool_execution.py:2309`
- `src/tool_execution.py:2315`
- `src/tool_execution.py:2320`
- `src/tool_execution.py:2331`
- `src/tool_execution.py:2335`
- `src/tool_execution.py:2340`
- `src/tool_execution.py:2345`
- `src/tool_execution.py:2361`
- `src/tool_execution.py:2369`
- `src/tool_execution.py:2393`
- `src/tool_execution.py:2397`
- `src/tool_execution.py:2400`
- `src/tool_execution.py:2403`
- `src/tool_execution.py:2407`
- `src/tool_execution.py:2411`
- `src/tool_execution.py:2415`
- `src/tool_execution.py:2418`
- `src/tool_execution.py:2421`
- `src/tool_execution.py:2424`
- `src/tool_execution.py:2427`
- `src/tool_execution.py:2430`
- `src/tool_execution.py:2433`
- `src/tool_execution.py:2436`
- `src/tool_execution.py:2439`
- `src/tool_execution.py:2442`
- `src/tool_execution.py:2445`
- `src/tool_execution.py:2448`
- `src/tool_execution.py:2451`
- `src/tool_execution.py:2454`
- `src/tool_execution.py:2457`
- `src/tool_execution.py:2460`
- `src/tool_execution.py:2463`
- `src/tool_execution.py:2468`
- `src/tool_execution.py:2470`
- `src/tool_execution.py:2474`
- `src/tool_execution.py:2477`
- `src/tool_execution.py:2480`
- `src/tool_execution.py:2483`
- `src/tool_execution.py:2486`
- `src/tool_execution.py:2489`
- `src/tool_execution.py:2492`
- `src/tool_execution.py:2539`
- `src/tool_execution.py:2562`
- `src/tool_execution.py:2573`

## `_settle` — function, line 206
- **called from:**
- `src/agent_runtime/journal.py:272`
- `src/agent_runtime/journal.py:277`

## `mark_operation_started` — function, line 222
- **called from:**
- `src/containment.py:1099`
- `tests/test_nested_invocation_ownership.py:38`
- `tests/test_nested_invocation_ownership.py:150`
- `tests/test_nested_invocation_ownership.py:180`
- `tests/test_nested_invocation_ownership.py:186`
- `tests/test_nested_invocation_ownership.py:193`

## `execute_action` — function (async), line 229
- **called from:**
- `src/agent_loop.py:34333`
- `tests/test_nested_invocation_ownership.py:184`
- `tests/test_runtime_evidence_contract.py:275`

## `record_action` — function, line 240
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `wrapped` — function (async), line 244
- decorator: `wraps(func)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
