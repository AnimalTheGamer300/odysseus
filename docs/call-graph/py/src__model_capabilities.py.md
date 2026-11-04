# `src/model_capabilities.py` — definitions & call sites

41 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_clean_token` — function, line 377
- **called from:**
- `src/model_capabilities.py:382`
- `src/model_capabilities.py:404`
- `src/model_capabilities.py:418`
- `src/model_capabilities.py:424`
- `src/model_capabilities.py:430`
- `src/model_capabilities.py:921`

## `_normalize_choice` — function, line 381
- **called from:**
- `src/model_capabilities.py:388`
- `src/model_capabilities.py:392`
- `src/model_capabilities.py:396`
- `src/model_capabilities.py:400`
- `src/model_capabilities.py:410`
- `src/model_capabilities.py:414`

## `normalize_family` — function, line 387
- **called from:**
- `src/model_capabilities.py:498`

## `normalize_source` — function, line 391
- **called from:**
- `src/model_capabilities.py:512`
- `src/model_capabilities.py:573`
- `src/model_capabilities.py:630`

## `normalize_confidence` — function, line 395
- **called from:**
- `src/model_capabilities.py:513`
- `src/model_capabilities.py:574`
- `src/model_capabilities.py:631`

## `normalize_modality` — function, line 399
- **called from:**
- `src/model_capability_readers/base.py:197`

## `normalize_capability` — function, line 403
- **called from:**
- `src/model_capabilities.py:566`
- `src/model_capabilities.py:690`
- `src/model_capability_readers/llamacpp.py:75`

## `normalize_assertion_status` — function, line 409
- **called from:**
- `src/model_capabilities.py:567`
- `src/model_capabilities.py:624`

## `normalize_probe_status` — function, line 413
- **called from:**
- `src/model_capabilities.py:691`

## `normalize_deterministic_control` — function, line 417
- **called from:**
- `src/model_capabilities.py:623`

## `normalize_reasoning_control_mechanism` — function, line 423
- **called from:**
- `tests/test_model_capabilities.py:227`

## `normalize_reasoning_control_value` — function, line 429
- **called from:**
- `tests/test_model_capabilities.py:241`
- `tests/test_model_capabilities.py:248`

## `_normalize_tokens` — function, line 435
- **called from:**
- `src/model_capabilities.py:464`
- `src/model_capabilities.py:465`
- `src/model_capabilities.py:507`
- `src/model_capabilities.py:798`

## `_normalize_limits` — function, line 450
- **called from:**
- `src/model_capabilities.py:511`
- `src/model_capabilities.py:575`
- `src/model_capabilities.py:632`
- `src/model_capabilities.py:705`

## `Modalities` — class, line 457
- decorator: `dataclass(frozen=True)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `Modalities.from_values` — method, line 462
- decorator: `classmethod`
- **called from:**
- `src/model_capabilities.py:503`

## `Modalities.to_dict` — method, line 468
- **called from:**
- `core/models.py:164`
- `routes/chat_routes.py:3149`
- `services/memory/skills.py:226`
- `services/memory/skills.py:382`
- `services/memory/skills.py:430`
- `src/model_capabilities.py:538`
- `src/model_capability_readers/base.py:66`
- `src/model_capability_readers/base.py:67`
- `src/model_capability_readers/base.py:68`
- `tests/test_history_compact_tool_calls.py:90`
- `tests/test_model_capabilities.py:68`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:154`

## `ModelCapability` — class, line 476
- decorator: `dataclass(frozen=True)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ModelCapability.build` — method, line 486
- decorator: `classmethod`
- **called from:**
- `scripts/dump_agent_prompt.py:424`
- `src/model_capabilities.py:523`
- `src/model_capabilities.py:582`
- `src/model_capabilities.py:583`
- `src/model_capabilities.py:639`
- `src/model_capabilities.py:640`
- `src/model_capabilities.py:711`
- `src/model_capabilities.py:712`
- `src/model_capabilities.py:732`
- `src/model_capabilities.py:774`
- `src/model_capabilities.py:792`
- `src/model_capabilities.py:911`
- `src/model_capabilities.py:923`
- `src/model_capabilities.py:929`
- `src/model_capability_readers/base.py:259`
- `src/model_capability_readers/google_ai_studio_mapping.py:89`
- `src/model_capability_readers/llamacpp.py:172`
- `src/model_capability_readers/llamacpp.py:182`
- `tests/test_model_capabilities.py:85`
- `tests/test_model_capabilities.py:107`
- `tests/test_model_capabilities.py:115`
- `tests/test_model_capabilities.py:116`
- `tests/test_model_capabilities.py:117`
- `tests/test_model_capabilities.py:118`
- `tests/test_model_capabilities.py:122`
- `tests/test_model_capabilities.py:129`
- `tests/test_model_capabilities.py:142`
- `tests/test_model_capabilities.py:165`
- `tests/test_model_capabilities.py:177`

## `ModelCapability.from_dict` — method, line 517
- decorator: `classmethod`
- **called from:**
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`

## `ModelCapability.to_dict` — method, line 534
- **called from:**
- `core/models.py:164`
- `routes/chat_routes.py:3149`
- `services/memory/skills.py:226`
- `services/memory/skills.py:382`
- `services/memory/skills.py:430`
- `src/model_capabilities.py:538`
- `src/model_capability_readers/base.py:66`
- `src/model_capability_readers/base.py:67`
- `src/model_capability_readers/base.py:68`
- `tests/test_history_compact_tool_calls.py:90`
- `tests/test_model_capabilities.py:68`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:154`

## `CapabilityAssertion` — class, line 547
- decorator: `dataclass(frozen=True)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CapabilityAssertion.build` — method, line 556
- decorator: `classmethod`
- **called from:**
- `scripts/dump_agent_prompt.py:424`
- `src/model_capabilities.py:523`
- `src/model_capabilities.py:582`
- `src/model_capabilities.py:583`
- `src/model_capabilities.py:639`
- `src/model_capabilities.py:640`
- `src/model_capabilities.py:711`
- `src/model_capabilities.py:712`
- `src/model_capabilities.py:732`
- `src/model_capabilities.py:774`
- `src/model_capabilities.py:792`
- `src/model_capabilities.py:911`
- `src/model_capabilities.py:923`
- `src/model_capabilities.py:929`
- `src/model_capability_readers/base.py:259`
- `src/model_capability_readers/google_ai_studio_mapping.py:89`
- `src/model_capability_readers/llamacpp.py:172`
- `src/model_capability_readers/llamacpp.py:182`
- `tests/test_model_capabilities.py:85`
- `tests/test_model_capabilities.py:107`
- `tests/test_model_capabilities.py:115`
- `tests/test_model_capabilities.py:116`
- `tests/test_model_capabilities.py:117`
- `tests/test_model_capabilities.py:118`
- `tests/test_model_capabilities.py:122`
- `tests/test_model_capabilities.py:129`
- `tests/test_model_capabilities.py:142`
- `tests/test_model_capabilities.py:165`
- `tests/test_model_capabilities.py:177`

## `CapabilityAssertion.from_dict` — method, line 580
- decorator: `classmethod`
- **called from:**
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`

## `CapabilityAssertion.to_dict` — method, line 592
- **called from:**
- `core/models.py:164`
- `routes/chat_routes.py:3149`
- `services/memory/skills.py:226`
- `services/memory/skills.py:382`
- `services/memory/skills.py:430`
- `src/model_capabilities.py:538`
- `src/model_capability_readers/base.py:66`
- `src/model_capability_readers/base.py:67`
- `src/model_capability_readers/base.py:68`
- `tests/test_history_compact_tool_calls.py:90`
- `tests/test_model_capabilities.py:68`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:154`

## `DeterministicControl` — class, line 604
- decorator: `dataclass(frozen=True)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DeterministicControl.build` — method, line 613
- decorator: `classmethod`
- **called from:**
- `scripts/dump_agent_prompt.py:424`
- `src/model_capabilities.py:523`
- `src/model_capabilities.py:582`
- `src/model_capabilities.py:583`
- `src/model_capabilities.py:639`
- `src/model_capabilities.py:640`
- `src/model_capabilities.py:711`
- `src/model_capabilities.py:712`
- `src/model_capabilities.py:732`
- `src/model_capabilities.py:774`
- `src/model_capabilities.py:792`
- `src/model_capabilities.py:911`
- `src/model_capabilities.py:923`
- `src/model_capabilities.py:929`
- `src/model_capability_readers/base.py:259`
- `src/model_capability_readers/google_ai_studio_mapping.py:89`
- `src/model_capability_readers/llamacpp.py:172`
- `src/model_capability_readers/llamacpp.py:182`
- `tests/test_model_capabilities.py:85`
- `tests/test_model_capabilities.py:107`
- `tests/test_model_capabilities.py:115`
- `tests/test_model_capabilities.py:116`
- `tests/test_model_capabilities.py:117`
- `tests/test_model_capabilities.py:118`
- `tests/test_model_capabilities.py:122`
- `tests/test_model_capabilities.py:129`
- `tests/test_model_capabilities.py:142`
- `tests/test_model_capabilities.py:165`
- `tests/test_model_capabilities.py:177`

## `DeterministicControl.from_dict` — method, line 637
- decorator: `classmethod`
- **called from:**
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`

## `DeterministicControl.to_dict` — method, line 649
- **called from:**
- `core/models.py:164`
- `routes/chat_routes.py:3149`
- `services/memory/skills.py:226`
- `services/memory/skills.py:382`
- `services/memory/skills.py:430`
- `src/model_capabilities.py:538`
- `src/model_capability_readers/base.py:66`
- `src/model_capability_readers/base.py:67`
- `src/model_capability_readers/base.py:68`
- `tests/test_history_compact_tool_calls.py:90`
- `tests/test_model_capabilities.py:68`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:154`

## `CapabilityProbeResult` — class, line 661
- decorator: `dataclass(frozen=True)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CapabilityProbeResult.build` — method, line 675
- decorator: `classmethod`
- **called from:**
- `scripts/dump_agent_prompt.py:424`
- `src/model_capabilities.py:523`
- `src/model_capabilities.py:582`
- `src/model_capabilities.py:583`
- `src/model_capabilities.py:639`
- `src/model_capabilities.py:640`
- `src/model_capabilities.py:711`
- `src/model_capabilities.py:712`
- `src/model_capabilities.py:732`
- `src/model_capabilities.py:774`
- `src/model_capabilities.py:792`
- `src/model_capabilities.py:911`
- `src/model_capabilities.py:923`
- `src/model_capabilities.py:929`
- `src/model_capability_readers/base.py:259`
- `src/model_capability_readers/google_ai_studio_mapping.py:89`
- `src/model_capability_readers/llamacpp.py:172`
- `src/model_capability_readers/llamacpp.py:182`
- `tests/test_model_capabilities.py:85`
- `tests/test_model_capabilities.py:107`
- `tests/test_model_capabilities.py:115`
- `tests/test_model_capabilities.py:116`
- `tests/test_model_capabilities.py:117`
- `tests/test_model_capabilities.py:118`
- `tests/test_model_capabilities.py:122`
- `tests/test_model_capabilities.py:129`
- `tests/test_model_capabilities.py:142`
- `tests/test_model_capabilities.py:165`
- `tests/test_model_capabilities.py:177`

## `CapabilityProbeResult.from_dict` — method, line 709
- decorator: `classmethod`
- **called from:**
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`

## `CapabilityProbeResult.to_assertion` — method, line 726
- **called from:**
- `tests/test_model_capabilities.py:184`
- `tests/test_model_capabilities.py:185`

## `CapabilityProbeResult.to_dict` — method, line 750
- **called from:**
- `core/models.py:164`
- `routes/chat_routes.py:3149`
- `services/memory/skills.py:226`
- `services/memory/skills.py:382`
- `services/memory/skills.py:430`
- `src/model_capabilities.py:538`
- `src/model_capability_readers/base.py:66`
- `src/model_capability_readers/base.py:67`
- `src/model_capability_readers/base.py:68`
- `tests/test_history_compact_tool_calls.py:90`
- `tests/test_model_capabilities.py:68`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:154`

## `capability_assertions_from_capability` — function, line 766
- **called from:**
- `src/model_capability_readers/base.py:52`
- `src/model_capability_readers/llamacpp.py:273`
- `src/model_capability_readers/llamacpp.py:395`

## `deterministic_controls_from_values` — function, line 784
- **called from:**
- `src/model_capability_readers/base.py:163`
- `src/model_capability_readers/google_ai_studio_mapping.py:157`
- `tests/test_model_capabilities.py:201`

## `CapabilityQuery` — class, line 803
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/model_capabilities.py:842`
- `src/model_capabilities.py:848`
- `src/model_capabilities.py:854`
- `src/model_capabilities.py:861`
- `src/model_capabilities.py:867`
- `src/model_capabilities.py:874`
- `src/model_capabilities.py:880`
- `src/model_capabilities.py:886`
- `src/model_capabilities.py:891`
- `src/model_capabilities.py:895`

## `CapabilityQuery.matches` — method, line 815
- **called from:**
- `src/agent_loop.py:5058`
- `src/model_capabilities.py:903`
- `tests/test_calendar_cli_overlap.py:85`
- `tests/test_foreground_model_routing.py:303`
- `tests/test_tool_approval_task_scope.py:217`
- `static/js/a11y.js:105`
- `static/js/a11y.js:116`
- `static/js/a11y.js:135`
- `static/js/a11y.js:152`
- `static/js/dragSort.js:45`
- `static/js/dragSort.js:163`
- `static/js/dragSort.js:194`
- `static/js/editor/slider-ux.js:97`
- `static/js/emailLibrary.js:3806`
- `static/js/ui.js:152`

## `display_surfaces_for` — function, line 902
- **called from:**
- `tests/test_model_capabilities.py:5`
- `tests/test_model_capabilities.py:39`
- `tests/test_model_capabilities.py:102`
- `tests/test_model_capability_readers.py:18`

## `unknown_capability` — function, line 906
- **called from:**
- `src/model_capabilities.py:519`
- `src/model_capabilities.py:934`
- `src/model_capability_readers/generic_openai.py:32`
- `src/model_capability_readers/google_ai_studio_mapping.py:128`
- `src/model_capability_readers/lmstudio.py:99`
- `src/model_capability_readers/ollama.py:132`
- `src/model_capability_readers/ollama.py:179`
- `src/model_capability_readers/openai.py:46`
- `tests/test_model_capabilities.py:83`

## `capability_from_endpoint_type` — function, line 914
- **called from:**
- `tests/test_model_capabilities.py:9`
- `tests/test_model_capabilities.py:21`
- `tests/test_model_capabilities.py:34`
