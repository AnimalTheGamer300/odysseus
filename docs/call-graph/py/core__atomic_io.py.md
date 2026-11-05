# `core/atomic_io.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `store_transaction` — function, line 28
- **called from:**
- `src/agent_runtime/process_resources.py:409`
- `src/agent_runtime/process_resources.py:428`
- `src/agent_runtime/process_resources.py:450`
- `src/agent_runtime/process_resources.py:495`
- `src/bg_jobs.py:81`
- `src/bg_jobs.py:240`
- `src/bg_jobs.py:356`
- `src/bg_jobs.py:373`
- `src/bg_jobs.py:407`
- `src/bg_jobs.py:436`
- `src/containment.py:468`
- `src/containment.py:500`
- `src/containment.py:523`

## `decorate` — function, line 30
- **called from:**
- `static/js/editor/control-kit.js:150`

## `locked` — function, line 32
- decorator: `functools.wraps(function)`
- **called from:**
- `routes/contacts/contacts_routes.py:328`
- `src/llm_core.py:176`

## `atomic_write_json` — function, line 61
- **called from:**
- `routes/auth_routes.py:548`
- `routes/auth_routes.py:568`
- `routes/auth_routes.py:633`
- `routes/codex_routes.py:920`
- `routes/contacts/contacts_routes.py:47`
- `routes/contacts/contacts_routes.py:138`
- `routes/cookbook_routes.py:3383`
- `routes/cookbook_routes.py:3769`
- `routes/email/email_helpers.py:1146`
- `routes/prefs_routes.py:27`
- `scripts/odysseus_conversation_qa.py:1282`
- `scripts/odysseus_conversation_qa.py:1480`
- `scripts/odysseus_conversation_qa.py:1504`
- `services/memory/skills.py:122`
- `src/agent_jobs.py:111`
- `src/agent_runtime/authority.py:677`
- `src/agent_runtime/process_resources.py:423`
- `src/agent_runtime/process_resources.py:519`
- `src/bg_jobs.py:70`
- `src/builtin_actions.py:3662`
- `src/containment.py:450`
- `src/containment_worker.py:114`
- `src/cookbook_serve_lifecycle.py:186`
- `src/integrations.py:257`
- `src/preset_manager.py:124`
- `src/settings.py:291`
- `src/settings.py:391`
- `tests/process_resource_helpers.py:63`
- `tests/test_atomic_io.py:46`
- `tests/test_atomic_io.py:54`
- `tests/test_atomic_io.py:64`
- `tests/test_atomic_io.py:72`
- `tests/test_atomic_io.py:74`
- `tests/test_atomic_io.py:84`
- `tests/test_atomic_io.py:106`
- `tests/test_atomic_io.py:130`
- `tests/test_atomic_io.py:136`
- `tests/test_atomic_io.py:145`
- `tests/test_atomic_io.py:154`
- `tests/test_background_resource_identity.py:92`
- `tests/test_background_resource_identity.py:201`
- `tests/test_background_resource_identity.py:254`
- `tests/test_wave3_launch_cost_lifecycle.py:149`
- `tests/test_wave3_launch_cost_lifecycle.py:165`
- `tests/test_wave3_launch_cost_lifecycle.py:213`

## `atomic_write_text` — function, line 88
- **called from:**
- `routes/auth_routes.py:615`
- `scripts/run_sft_overnight_fixture_flows.py:658`
- `scripts/run_sft_overnight_fixture_flows.py:677`
- `scripts/run_sft_overnight_fixture_flows.py:712`
- `scripts/run_sft_overnight_fixture_flows.py:713`
- `services/memory/skills.py:227`
- `services/memory/skills.py:489`
- `services/memory/skills.py:499`
- `src/containment_worker.py:116`
- `tests/test_atomic_io.py:168`
- `tests/test_atomic_io.py:176`
- `tests/test_atomic_io.py:184`
- `tests/test_atomic_io.py:186`
- `tests/test_atomic_io.py:194`
- `tests/test_atomic_io.py:203`
- `tests/test_atomic_io.py:214`
- `tests/test_atomic_io.py:223`
- `tests/test_atomic_io.py:232`
- `tests/test_atomic_io.py:246`
- `tests/test_sft_overnight_fixture_flows.py:293`
