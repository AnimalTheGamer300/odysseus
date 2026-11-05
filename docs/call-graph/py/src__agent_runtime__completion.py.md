# `src/agent_runtime/completion.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_ledger` — function, line 27
- **called from:**
- `src/agent_runtime/completion.py:283`
- `src/agent_runtime/completion.py:332`
- `tests/test_effect_resource_bindings.py:67`
- `tests/test_effect_resource_bindings.py:330`
- `tests/test_effect_resource_bindings.py:367`
- `tests/test_effect_resource_bindings.py:417`
- `tests/test_effect_verification_adapters.py:125`
- `tests/test_effect_verification_adapters.py:129`
- `tests/test_effect_verification_adapters.py:219`
- `tests/test_effect_verification_adapters.py:452`
- `tests/test_effect_verification_adapters.py:472`
- `tests/test_effect_verification_adapters.py:474`
- `tests/test_effect_verification_adapters.py:491`
- `tests/test_effect_verification_adapters.py:503`
- `tests/test_effect_verification_adapters.py:515`
- `tests/test_effect_verification_adapters.py:528`
- `tests/test_effect_verification_adapters.py:530`
- `tests/test_effect_verification_adapters.py:540`
- `tests/test_effect_verification_adapters.py:547`

## `_current_run_claims` — function, line 68
- **called from:**
- `src/agent_runtime/completion.py:116`

## `_supported_prose` — function, line 106
- **called from:**
- `src/agent_runtime/completion.py:173`
- `src/agent_runtime/completion.py:412`

## `completion_answer` — function, line 143
- **called from:**
- `src/agent_runtime/completion.py:284`
- `src/agent_runtime/completion.py:347`
- `src/agent_runtime/completion.py:350`
- `src/agent_runtime/completion.py:372`
- `src/agent_runtime/completion.py:415`
- `tests/test_completion_boundary.py:348`
- `tests/test_completion_boundary.py:383`
- `tests/test_completion_boundary.py:397`
- `tests/test_effect_resource_bindings.py:173`
- `tests/test_effect_verification_adapters.py:453`
- `tests/test_effect_verification_adapters.py:479`
- `tests/test_effect_verification_adapters.py:494`
- `tests/test_effect_verification_adapters.py:504`
- `tests/test_effect_verification_adapters.py:518`
- `tests/test_runtime_evidence_contract.py:140`
- `tests/test_runtime_evidence_contract.py:150`
- `tests/test_runtime_evidence_contract.py:161`
- `tests/test_runtime_evidence_contract.py:173`
- `tests/test_runtime_evidence_contract.py:430`
- `tests/test_runtime_evidence_contract.py:440`
- `tests/test_runtime_evidence_contract.py:451`
- `tests/test_runtime_evidence_contract.py:461`
- `tests/test_runtime_evidence_contract.py:471`
- `tests/test_runtime_evidence_contract.py:482`
- `tests/test_runtime_evidence_contract.py:496`

## `_disclose` — function, line 156
- **called from:**
- `src/agent_runtime/completion.py:153`
- `src/agent_runtime/completion.py:341`

## `_disclosure` — function, line 162
- **called from:**
- `src/agent_runtime/completion.py:158`
- `src/agent_runtime/completion.py:360`

## `_completion_answer` — function, line 170
- **called from:**
- `src/agent_runtime/completion.py:152`
- `src/agent_runtime/completion.py:340`

## `_event` — function, line 202
- **called from:**
- `scripts/eval_exact_file_routing.py:104`
- `scripts/eval_exact_file_routing.py:122`
- `src/agent_runtime/completion.py:287`
- `src/agent_runtime/completion.py:356`
- `src/agent_runtime/completion.py:377`
- `src/agent_runtime/completion.py:378`
- `src/agent_runtime/completion.py:381`
- `src/agent_runtime/completion.py:383`
- `src/agent_runtime/completion.py:385`
- `src/agent_runtime/completion.py:419`
- `tests/test_agent_unknown_context_budget.py:44`
- `tests/test_calendar_owner_scope.py:274`
- `tests/test_calendar_owner_scope.py:275`
- `tests/test_calendar_owner_scope.py:276`
- `tests/test_completion_boundary.py:25`
- `tests/test_completion_boundary.py:26`
- `tests/test_completion_boundary.py:27`
- `tests/test_completion_boundary.py:42`
- `tests/test_completion_boundary.py:43`
- `tests/test_completion_boundary.py:55`
- `tests/test_completion_boundary.py:56`
- `tests/test_completion_boundary.py:68`
- `tests/test_completion_boundary.py:69`
- `tests/test_completion_boundary.py:70`
- `tests/test_completion_boundary.py:134`
- `tests/test_completion_boundary.py:136`
- `tests/test_completion_boundary.py:138`
- `tests/test_completion_boundary.py:171`
- `tests/test_completion_boundary.py:172`
- `tests/test_completion_boundary.py:174`
- `tests/test_completion_boundary.py:194`
- `tests/test_completion_boundary.py:212`
- `tests/test_completion_boundary.py:214`
- `tests/test_completion_boundary.py:241`
- `tests/test_completion_boundary.py:242`
- `tests/test_completion_boundary.py:244`
- `tests/test_completion_boundary.py:274`
- `tests/test_completion_boundary.py:276`
- `tests/test_completion_boundary.py:302`
- `tests/test_completion_boundary.py:305`
- `tests/test_completion_boundary.py:313`
- `tests/test_completion_boundary.py:407`
- `tests/test_completion_boundary.py:428`
- `tests/test_completion_boundary.py:429`
- `tests/test_completion_boundary.py:449`
- `tests/test_headless_completion_consumers.py:48`
- `tests/test_headless_completion_consumers.py:49`
- `tests/test_headless_completion_consumers.py:106`
- `tests/test_headless_completion_consumers.py:107`
- `tests/test_headless_completion_consumers.py:108`
- `tests/test_headless_completion_consumers.py:139`
- `tests/test_headless_completion_consumers.py:141`
- `tests/test_headless_completion_consumers.py:148`
- `tests/test_headless_completion_consumers.py:149`

## `with_completion_gate` — function, line 206
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `wrapped` — function (async), line 210
- decorator: `wraps(func)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
