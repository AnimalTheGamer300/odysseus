# `src/agent_evidence.py` — definitions & call sites

52 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `workspace_artifact_is_usable` — function, line 15
- **called from:**
- `src/agent_evidence.py:1113`
- `src/clean_agent_preview.py:4731`

## `EvidenceKind` — class, line 54
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CompletionStatus` — class, line 62
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CompletionRequirements` — class, line 73
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_evidence.py:415`
- `src/agent_evidence.py:477`
- `src/agent_evidence.py:633`
- `tests/test_agent_evidence.py:591`
- `tests/test_agent_evidence.py:628`
- `tests/test_agent_evidence.py:680`
- `tests/test_agent_evidence.py:732`
- `tests/test_agent_evidence.py:764`
- `tests/test_agent_evidence.py:794`
- `tests/test_agent_evidence.py:857`
- `tests/test_agent_evidence.py:880`
- `tests/test_agent_evidence.py:900`
- `tests/test_agent_evidence.py:922`
- `tests/test_agent_trace.py:20`
- `tests/test_completion_boundary.py:382`
- `tests/test_effect_resource_bindings.py:67`
- `tests/test_effect_resource_bindings.py:330`
- `tests/test_effect_resource_bindings.py:367`
- `tests/test_effect_resource_bindings.py:417`
- `tests/test_effect_verification_adapters.py:124`
- `tests/test_effect_verification_adapters.py:218`
- `tests/test_effect_verification_adapters.py:432`
- `tests/test_effect_verification_adapters.py:452`
- `tests/test_effect_verification_adapters.py:491`
- `tests/test_effect_verification_adapters.py:503`
- `tests/test_effect_verification_adapters.py:515`
- `tests/test_effect_verification_adapters.py:528`
- `tests/test_effect_verification_adapters.py:530`
- `tests/test_effect_verification_adapters.py:540`
- `tests/test_effect_verification_adapters.py:547`
- `tests/test_runtime_evidence_contract.py:68`
- `tests/test_runtime_evidence_contract.py:121`
- `tests/test_runtime_evidence_contract.py:130`
- `tests/test_runtime_evidence_contract.py:139`
- `tests/test_runtime_evidence_contract.py:149`
- `tests/test_runtime_evidence_contract.py:159`
- `tests/test_runtime_evidence_contract.py:172`
- `tests/test_runtime_evidence_contract.py:297`
- `tests/test_runtime_evidence_contract.py:396`
- `tests/test_runtime_evidence_contract.py:450`
- `tests/test_runtime_evidence_contract.py:470`
- `tests/test_runtime_evidence_contract.py:480`
- `tests/test_runtime_evidence_contract.py:494`
- `tests/test_runtime_evidence_contract.py:510`
- `tests/test_runtime_evidence_contract.py:522`
- `tests/test_workspace_artifact_tool_floor.py:282`

## `CompletionRequirements.to_dict` — method, line 83
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

## `EvidenceEvent` — class, line 91
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_evidence.py:809`

## `EvidenceEvent.to_dict` — method, line 108
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

## `CompletionDecision` — class, line 118
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_evidence.py:1006`
- `src/agent_evidence.py:1017`
- `src/agent_evidence.py:1023`
- `src/agent_evidence.py:1035`
- `src/agent_evidence.py:1049`
- `src/agent_evidence.py:1053`
- `src/agent_evidence.py:1060`
- `src/agent_evidence.py:1068`
- `src/agent_evidence.py:1075`
- `src/agent_evidence.py:1125`
- `src/agent_evidence.py:1157`
- `src/agent_evidence.py:1191`
- `src/agent_evidence.py:1198`
- `src/agent_evidence.py:1208`
- `src/agent_evidence.py:1223`
- `src/agent_evidence.py:1231`
- `src/agent_evidence.py:1237`
- `src/agent_evidence.py:1244`
- `src/agent_evidence.py:1251`
- `src/agent_evidence.py:1262`
- `src/agent_runtime/completion.py:352`

## `CompletionDecision.to_dict` — method, line 125
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

## `command_is_validation` — function, line 203
- **called from:**
- `src/agent_loop.py:20093`
- `src/agent_loop.py:36400`
- `tests/test_runtime_evidence_contract.py:551`

## `command_is_test` — function, line 209
- **called from:**
- `src/agent_evidence.py:903`
- `src/agent_loop.py:36396`
- `tests/test_runtime_evidence_contract.py:550`

## `_clean_path` — function, line 214
- **called from:**
- `src/agent_evidence.py:219`
- `src/agent_evidence.py:255`
- `src/agent_evidence.py:271`
- `src/agent_evidence.py:351`
- `src/agent_evidence.py:365`
- `src/agent_evidence.py:433`
- `src/agent_evidence.py:441`
- `src/agent_evidence.py:457`
- `src/agent_evidence.py:485`
- `src/agent_evidence.py:495`
- `src/agent_evidence.py:503`
- `src/agent_evidence.py:539`
- `src/agent_evidence.py:547`
- `src/agent_evidence.py:556`
- `src/agent_evidence.py:569`
- `src/agent_evidence.py:585`
- `src/workspace_paths.py:24`
- `src/workspace_paths.py:25`
- `src/workspace_paths.py:29`
- `src/workspace_paths.py:30`

## `_is_prose_abbreviation` — function, line 218
- **called from:**
- `src/agent_evidence.py:358`

## `_artifact_match_is_negated` — function, line 222
- **called from:**
- `src/agent_evidence.py:352`

## `_artifact_match_is_callable` — function, line 229
- **called from:**
- `src/agent_evidence.py:354`

## `_artifact_match_is_email_host` — function, line 242
- **called from:**
- `src/agent_evidence.py:356`

## `_workspace_path_identity` — function, line 252
- **called from:**
- `src/agent_evidence.py:363`
- `src/agent_evidence.py:371`
- `src/agent_evidence.py:460`
- `src/agent_evidence.py:466`

## `_known_input_is_explicit_mutation_target` — function, line 262
- **called from:**
- `src/agent_evidence.py:372`
- `src/agent_evidence.py:467`

## `_unquoted_statements` — function, line 288
- **called from:**
- `src/agent_evidence.py:338`
- `src/agent_runtime/completion.py:114`

## `mask` — function, line 294
- **called from:**
- `static/js/editor/ai-inpaint.js:220`
- `static/js/editor/ai-tools-misc.js:5`
- `static/js/editor/ai-tools-misc.js:54`
- `static/js/editor/ai-tools-misc.js:55`
- `static/js/editor/build/controls.js:691`
- `static/js/editor/layer-panel.js:889`
- `static/js/editor/layer-panel.js:1684`
- `static/js/editor/layer-panel.js:1731`
- `static/js/editor/patch-ops.js:26`
- `static/js/editor/psd.js:340`
- `static/js/editor/retouch.js:163`
- `static/js/galleryEditor.js:565`
- `static/js/galleryEditor.js:1848`
- `static/js/galleryEditor.js:1848`
- `static/js/galleryEditor.js:3438`
- `static/js/galleryEditor.js:7892`
- `static/js/galleryEditor.js:11138`
- `static/js/galleryEditor.js:11144`
- `static/js/galleryEditor.js:12442`
- `static/js/galleryEditor.js:12611`

## `_execution_obligation` — function, line 316
- **called from:**
- `src/agent_runtime/completion.py:109`
- `src/agent_runtime/completion.py:172`
- `src/agent_runtime/completion.py:351`

## `infer_completion_requirements` — function, line 322
- **called from:**
- `src/agent_evidence.py:447`
- `tests/test_agent_evidence.py:14`
- `tests/test_agent_evidence.py:23`
- `tests/test_agent_evidence.py:30`
- `tests/test_agent_evidence.py:49`
- `tests/test_agent_evidence.py:60`
- `tests/test_agent_evidence.py:70`
- `tests/test_agent_evidence.py:81`
- `tests/test_agent_evidence.py:89`
- `tests/test_agent_evidence.py:97`
- `tests/test_agent_evidence.py:105`
- `tests/test_agent_evidence.py:115`
- `tests/test_agent_evidence.py:124`
- `tests/test_agent_evidence.py:132`
- `tests/test_agent_evidence.py:140`
- `tests/test_agent_evidence.py:196`
- `tests/test_agent_evidence.py:226`
- `tests/test_agent_evidence.py:247`
- `tests/test_agent_evidence.py:269`
- `tests/test_agent_evidence.py:297`
- `tests/test_agent_evidence.py:312`
- `tests/test_agent_evidence.py:318`
- `tests/test_agent_evidence.py:344`
- `tests/test_agent_evidence.py:367`
- `tests/test_agent_evidence.py:385`
- `tests/test_agent_evidence.py:422`
- `tests/test_agent_evidence.py:453`
- `tests/test_agent_evidence.py:480`
- `tests/test_agent_evidence.py:507`
- `tests/test_agent_evidence.py:527`
- `tests/test_agent_evidence.py:570`
- `tests/test_agent_evidence.py:663`
- `tests/test_agent_evidence.py:700`
- `tests/test_agent_evidence.py:716`
- `tests/test_agent_evidence.py:817`
- `tests/test_completion_boundary.py:362`
- `tests/test_completion_boundary.py:372`
- `tests/test_email_reader_completion_regression.py:26`

## `requirements_from_runtime_context` — function, line 425
- **called from:**
- `src/agent_loop.py:25376`
- `src/agent_runtime/completion.py:220`
- `src/agent_runtime/completion.py:272`
- `tests/test_agent_evidence.py:148`
- `tests/test_agent_evidence.py:166`

## `_digest` — function, line 489
- **called from:**
- `src/agent_evidence.py:628`
- `src/agent_evidence.py:802`
- `src/agent_evidence.py:803`
- `src/agent_runtime/local_model_control.py:72`
- `src/agent_runtime/local_model_control.py:98`

## `_path_is_mentioned` — function, line 493
- **called from:**
- `src/agent_evidence.py:864`
- `src/agent_evidence.py:921`

## `_artifact_path_matches_required` — function, line 501
- **called from:**
- `src/agent_evidence.py:666`
- `src/agent_evidence.py:677`
- `src/agent_evidence.py:762`
- `src/agent_evidence.py:891`
- `src/agent_evidence.py:949`
- `src/agent_evidence.py:962`
- `src/agent_evidence.py:1088`
- `src/agent_evidence.py:1172`
- `src/agent_evidence.py:1179`
- `src/agent_evidence.py:1219`

## `_explicit_tool_paths` — function, line 509
- **called from:**
- `src/agent_evidence.py:849`

## `_command_text` — function, line 592
- **called from:**
- `src/agent_evidence.py:206`
- `src/agent_evidence.py:211`
- `src/agent_evidence.py:610`
- `src/agent_evidence.py:623`
- `src/agent_evidence.py:903`
- `src/agent_evidence.py:918`

## `_matches_declared_verifier` — function, line 609
- **called from:**
- `src/agent_evidence.py:903`

## `command_has_mutation_effect` — function, line 620
- **called from:**
- `src/agent_evidence.py:855`
- `src/agent_loop.py:20070`
- `src/agent_loop.py:20605`
- `src/agent_loop.py:36309`
- `src/clean_agent_preview.py:4601`
- `tests/test_workspace_artifact_tool_floor.py:1586`
- `tests/test_workspace_artifact_tool_floor.py:1590`

## `_event_id` — function, line 626
- **called from:**
- `src/agent_evidence.py:810`
- `src/agent_evidence.py:824`

## `EvidenceLedger` — class, line 631
- **called from:**
- `tests/test_agent_evidence.py:941`
- `tests/test_completion_boundary.py:347`
- `tests/test_completion_boundary.py:374`
- `tests/test_completion_boundary.py:382`
- `tests/test_completion_boundary.py:396`
- `tests/test_runtime_evidence_contract.py:139`

## `EvidenceLedger.__init__` — method, line 632
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email/email_helpers.py:205`
- `routes/email/email_helpers.py:220`
- `routes/email/email_helpers.py:232`
- `routes/email/email_helpers.py:248`
- `routes/email/email_routes.py:1664`
- `scripts/css_snapshot.py:194`
- `scripts/probe_browser_budget.py:56`
- `src/agent_tools/document_tools.py:759`
- `src/agent_tools/filesystem_tools.py:384`
- `src/builtin_actions.py:552`
- `src/chatgpt_subscription.py:495`
- `src/containment.py:170`
- `src/outbound_fetch.py:220`
- `src/path_confinement.py:81`
- `src/process_ownership.py:110`
- `src/report_math.py:31`
- `tests/conftest.py:199`
- `tests/test_admin_routes_auth_disabled.py:16`
- `tests/test_agent_state_dir_confinement.py:799`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_action_planning.py:11`
- `tests/test_deep_research_browser_fallback.py:10`
- `tests/test_deep_research_browser_fallback.py:29`
- `tests/test_deep_research_browser_fallback.py:56`
- `tests/test_deep_research_extraction_controls.py:13`
- `tests/test_deep_research_full_loop_navigation.py:11`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_llm_core_streaming.py:50`
- `tests/test_retired_settings_interfaces.py:31`
- `tests/test_searxng_ca_validation.py:35`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:155`

## `EvidenceLedger.record_effects` — method, line 645
- **called from:**
- `src/agent_runtime/completion.py:30`

## `EvidenceLedger._last_success_ordinal` — method, line 663
- **called from:**
- `src/agent_evidence.py:671`

## `EvidenceLedger._later_effects` — method, line 669
- **called from:**
- `src/agent_evidence.py:709`

## `EvidenceLedger._entry_unsettled` — method, line 684
- decorator: `staticmethod`
- **called from:**
- `src/agent_evidence.py:709`
- `src/agent_evidence.py:1073`

## `EvidenceLedger._effect_unsettled` — method, line 707
- **called from:**
- `src/agent_evidence.py:970`
- `src/agent_evidence.py:1118`

## `EvidenceLedger._current_effects` — method, line 711
- **called from:**
- `src/agent_evidence.py:724`
- `src/agent_evidence.py:1074`

## `EvidenceLedger._contradicted_target` — method, line 716
- **called from:**
- `src/agent_evidence.py:1066`

## `EvidenceLedger.unverified_external_effects` — method, line 730
- **called from:**
- `src/agent_evidence.py:745`
- `src/agent_evidence.py:957`
- `src/agent_evidence.py:1003`
- `src/agent_runtime/completion.py:111`

## `EvidenceLedger.effect_disclosures` — method, line 741
- **called from:**
- `src/agent_runtime/completion.py:164`

## `EvidenceLedger._effect_contradicted` — method, line 758
- **called from:**
- `src/agent_evidence.py:970`
- `src/agent_evidence.py:1058`

## `EvidenceLedger.from_tool_events` — method, line 770
- decorator: `classmethod`
- **called from:**
- `src/agent_loop.py:20167`
- `src/agent_loop.py:25772`
- `src/agent_loop.py:26529`
- `src/agent_loop.py:26706`
- `src/agent_loop.py:27790`
- `src/agent_loop.py:28473`
- `src/agent_loop.py:28676`
- `src/agent_loop.py:28723`
- `src/agent_loop.py:30467`
- `src/agent_loop.py:31051`
- `src/agent_loop.py:31243`
- `src/agent_loop.py:31746`
- `src/agent_loop.py:31797`
- `src/agent_loop.py:31923`
- `src/agent_loop.py:31974`
- `src/agent_loop.py:32147`
- `src/agent_loop.py:32273`
- `src/agent_loop.py:32437`
- `src/agent_loop.py:36244`
- `src/agent_loop.py:36285`
- `src/agent_loop.py:36834`
- `src/agent_loop.py:37209`
- `src/agent_loop.py:37257`
- `src/agent_loop.py:37298`
- `src/agent_loop.py:37341`
- `src/agent_loop.py:37425`
- `src/agent_loop.py:37483`
- `src/agent_loop.py:37812`
- `src/agent_loop.py:37942`
- `src/agent_loop.py:38871`
- `src/agent_runtime/completion.py:29`
- `src/agent_trace.py:683`
- `tests/test_agent_evidence.py:201`
- `tests/test_agent_evidence.py:227`
- `tests/test_agent_evidence.py:250`
- `tests/test_agent_evidence.py:270`
- `tests/test_agent_evidence.py:298`
- `tests/test_agent_evidence.py:321`
- `tests/test_agent_evidence.py:347`
- `tests/test_agent_evidence.py:368`
- `tests/test_agent_evidence.py:386`
- `tests/test_agent_evidence.py:427`
- `tests/test_agent_evidence.py:454`
- `tests/test_agent_evidence.py:481`
- `tests/test_agent_evidence.py:508`
- `tests/test_agent_evidence.py:551`
- `tests/test_agent_evidence.py:571`
- `tests/test_agent_evidence.py:594`
- `tests/test_agent_evidence.py:632`
- `tests/test_agent_evidence.py:664`
- `tests/test_agent_evidence.py:683`
- `tests/test_agent_evidence.py:701`
- `tests/test_agent_evidence.py:717`
- `tests/test_agent_evidence.py:735`
- `tests/test_agent_evidence.py:770`
- `tests/test_agent_evidence.py:797`
- `tests/test_agent_evidence.py:818`
- `tests/test_agent_evidence.py:838`
- `tests/test_agent_evidence.py:861`
- `tests/test_agent_evidence.py:884`
- … +23 more (grep the name in repo)

## `EvidenceLedger._append` — method, line 781
- **called from:**
- `src/agent_evidence.py:842`
- `src/agent_evidence.py:872`
- `src/agent_evidence.py:894`
- `src/agent_evidence.py:911`
- `src/agent_evidence.py:922`
- `src/agent_evidence.py:986`
- `src/agent_runtime/effect_log.py:345`
- `src/agent_runtime/effect_log.py:350`
- `src/agent_runtime/effect_log.py:353`
- `src/agent_runtime/effect_log.py:509`
- `src/task_endpoint.py:60`
- `src/task_endpoint.py:67`
- `src/task_endpoint.py:68`
- `src/task_endpoint.py:69`
- `src/task_endpoint.py:71`

## `EvidenceLedger.record_tool_event` — method, line 830
- **called from:**
- `src/agent_evidence.py:778`
- `tests/test_agent_evidence.py:407`
- `tests/test_agent_evidence.py:557`

## `EvidenceLedger._supports_verifier_claim` — method, line 930
- **called from:**
- `src/agent_runtime/completion.py:123`
- `src/agent_runtime/completion.py:191`

## `EvidenceLedger._supports_artifact_claim` — method, line 952
- **called from:**
- `src/agent_runtime/completion.py:126`
- `src/agent_runtime/completion.py:180`
- `tests/test_effect_resource_bindings.py:177`

## `EvidenceLedger.record_media_ingress` — method, line 974
- **called from:**
- `src/agent_loop.py:38878`

## `EvidenceLedger.evaluate` — method, line 995
- **called from:**
- `src/agent_loop.py:25772`
- `src/agent_loop.py:26529`
- `src/agent_loop.py:26706`
- `src/agent_loop.py:27790`
- `src/agent_loop.py:28473`
- `src/agent_loop.py:28676`
- `src/agent_loop.py:28723`
- `src/agent_loop.py:30467`
- `src/agent_loop.py:31051`
- `src/agent_loop.py:31247`
- `src/agent_loop.py:31746`
- `src/agent_loop.py:31797`
- `src/agent_loop.py:31923`
- `src/agent_loop.py:31974`
- `src/agent_loop.py:32147`
- `src/agent_loop.py:32273`
- `src/agent_loop.py:32437`
- `src/agent_loop.py:36244`
- `src/agent_loop.py:36285`
- `src/agent_loop.py:36834`
- `src/agent_loop.py:37209`
- `src/agent_loop.py:37257`
- `src/agent_loop.py:37298`
- `src/agent_loop.py:37341`
- `src/agent_loop.py:37425`
- `src/agent_loop.py:37483`
- `src/agent_loop.py:37812`
- `src/agent_loop.py:37942`
- `src/agent_loop.py:38879`
- `src/agent_runtime/completion.py:284`
- `src/agent_runtime/completion.py:333`
- `src/agent_runtime/completion.py:339`
- `src/agent_trace.py:693`
- `tests/markdown_browser_check.py:73`
- `tests/markdown_browser_check.py:76`
- `tests/markdown_browser_check.py:106`
- `tests/markdown_browser_check.py:112`
- `tests/markdown_browser_check.py:120`
- `tests/markdown_browser_check.py:125`
- `tests/markdown_screenshot.py:94`
- `tests/markdown_screenshot.py:95`
- `tests/test_agent_evidence.py:222`
- `tests/test_agent_evidence.py:240`
- `tests/test_agent_evidence.py:263`
- `tests/test_agent_evidence.py:290`
- `tests/test_agent_evidence.py:300`
- `tests/test_agent_evidence.py:338`
- `tests/test_agent_evidence.py:363`
- `tests/test_agent_evidence.py:379`
- `tests/test_agent_evidence.py:406`
- `tests/test_agent_evidence.py:416`
- `tests/test_agent_evidence.py:447`
- `tests/test_agent_evidence.py:474`
- `tests/test_agent_evidence.py:501`
- `tests/test_agent_evidence.py:519`
- `tests/test_agent_evidence.py:553`
- `tests/test_agent_evidence.py:564`
- `tests/test_agent_evidence.py:584`
- `tests/test_agent_evidence.py:619`
- `tests/test_agent_evidence.py:657`
- … +108 more (grep the name in repo)

## `EvidenceLedger._evaluate_obligations` — method, line 1010
- **called from:**
- `src/agent_evidence.py:936`
- `src/agent_evidence.py:1001`

## `EvidenceLedger.to_list` — method, line 1269
- **called from:**
- `src/agent_loop.py:38883`
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
