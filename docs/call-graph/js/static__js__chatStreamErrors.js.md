# `static/js/chatStreamErrors.js` — definitions & call sites

3 definitions (regex-based, best-effort).
**Exports:** `createTerminalStreamError`, `isRecoverableStreamError`

## `createTerminalStreamError` — function, line 2
- **called from:**
- `static/js/chat.js:4709`
- `static/js/chat.js:6059`
- `static/js/chat.js:7469`
- `static/js/chatStreamErrors.js:2`

## `stream` — class, line 16
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:255`
- `scripts/eval_odysseus_contextual_tool_use.py:687`
- `scripts/eval_odysseus_crud.py:218`
- `scripts/eval_odysseus_tool_use.py:1068`
- `scripts/odysseus_conversation_qa.py:748`
- `scripts/odysseus_domain_audit.py:301`
- `scripts/run_sft_environment_expansion.py:279`
- `scripts/run_sft_overnight_fixture_flows.py:236`
- `scripts/sft_email_overseer.py:533`
- `src/clean_agent_preview.py:5556`
- `src/llm_core.py:3503`
- `src/llm_core.py:3624`
- `src/llm_core.py:3723`
- `src/llm_core.py:3931`
- `src/outbound_fetch.py:296`
- `tests/smoke/test_chat_smoke.py:37`
- `tests/smoke/test_compare_smoke.py:21`
- `tests/test_agent_runs_terminal_order.py:17`
- `tests/test_agent_runs_terminal_order.py:42`
- `tests/test_compare_stop_disconnect_poll.py:201`
- `tests/test_compare_stop_disconnect_poll.py:207`
- `tests/test_completion_boundary.py:30`
- `tests/test_completion_boundary.py:46`
- `tests/test_completion_boundary.py:59`
- `tests/test_completion_boundary.py:74`
- `tests/test_completion_boundary.py:123`
- `tests/test_completion_boundary.py:146`
- `tests/test_completion_boundary.py:176`
- `tests/test_completion_boundary.py:198`
- `tests/test_completion_boundary.py:219`
- `tests/test_completion_boundary.py:251`
- `tests/test_completion_boundary.py:278`
- `tests/test_completion_boundary.py:311`
- `tests/test_completion_boundary.py:412`
- `tests/test_completion_boundary.py:432`
- `tests/test_completion_boundary.py:452`
- `tests/test_effect_verification_adapters.py:457`
- `tests/test_runtime_evidence_contract.py:113`
- `tests/test_runtime_evidence_contract.py:189`
- `tests/test_runtime_evidence_contract.py:204`
- `tests/test_runtime_evidence_contract.py:219`
- `tests/test_runtime_evidence_contract.py:237`
- `tests/test_runtime_evidence_contract.py:261`
- `tests/test_runtime_evidence_contract.py:320`
- `tests/test_runtime_evidence_contract.py:337`
- `tests/test_runtime_evidence_contract.py:356`
- `tests/test_shell_service.py:52`
- `tests/test_web_fetch_size_caps.py:56`
- `tests/test_web_fetch_size_caps.py:63`
- `static/js/chat.js:1222`
- `static/js/sessions.js:2564`
- `static/js/sessions.js:3209`

## `isRecoverableStreamError` — function, line 17
- **called from:**
- `static/js/chat.js:6658`
- `static/js/chatStreamErrors.js:17`
