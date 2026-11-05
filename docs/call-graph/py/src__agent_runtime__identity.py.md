# `src/agent_runtime/identity.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `digest` — function, line 25
- **called from:**
- `src/agent_runtime/journal.py:41`
- `src/agent_runtime/journal.py:56`
- `src/agent_runtime/process_resources.py:259`
- `src/agent_runtime/process_resources.py:275`
- `src/agent_runtime/process_resources.py:298`
- `src/agent_runtime/process_resources.py:299`
- `src/browser_identity.py:62`
- `src/browser_identity.py:74`
- `src/browser_identity.py:244`
- `src/browser_identity.py:310`
- `src/browser_identity.py:431`

## `artifact_version` — function, line 30
- **called from:**
- `src/agent_evidence.py:1052`
- `src/agent_runtime/journal.py:112`
- `tests/test_runtime_evidence_contract.py:78`
- `tests/test_runtime_evidence_contract.py:79`
- `tests/test_runtime_evidence_contract.py:84`
- `tests/test_runtime_evidence_contract.py:101`

## `artifact_identity` — function, line 71
- **called from:**
- `src/agent_evidence.py:506`
- `src/agent_evidence.py:506`
- `src/agent_evidence.py:823`
- `src/agent_evidence.py:854`
- `src/agent_evidence.py:1044`
- `src/agent_evidence.py:1110`
- `src/agent_runtime/identity.py:32`
- `src/agent_runtime/journal.py:112`
- `tests/test_runtime_evidence_contract.py:56`
- `tests/test_runtime_evidence_contract.py:57`
- `tests/test_runtime_evidence_contract.py:59`
- `tests/test_runtime_evidence_contract.py:60`
- `tests/test_runtime_evidence_contract.py:61`
- `tests/test_runtime_evidence_contract.py:62`

## `executable_words` — function, line 98
- **called from:**
- `src/agent_evidence.py:610`
- `src/agent_evidence.py:616`
- `src/agent_evidence.py:918`
- `src/agent_runtime/identity.py:138`
- `src/agent_runtime/identity.py:158`

## `is_test_command` — function, line 137
- **called from:**
- `src/agent_evidence.py:211`
- `src/agent_runtime/identity.py:162`
- `tests/test_runtime_evidence_contract.py:34`
- `tests/test_runtime_evidence_contract.py:44`
- `tests/test_runtime_evidence_contract.py:538`
- `tests/test_runtime_evidence_contract.py:543`

## `is_validation_command` — function, line 157
- **called from:**
- `src/agent_evidence.py:206`
- `src/agent_evidence.py:919`
- `tests/test_runtime_evidence_contract.py:48`
- `tests/test_runtime_evidence_contract.py:49`
