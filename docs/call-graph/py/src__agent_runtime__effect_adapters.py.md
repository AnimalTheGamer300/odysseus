# `src/agent_runtime/effect_adapters.py` — definitions & call sites

22 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `DispatchCapture` — class, line 38
- decorator: `dataclass`
- **called from:**
- `src/agent_runtime/effect_adapters.py:59`
- `tests/test_effect_verification_adapters.py:67`
- `tests/test_effect_verification_adapters.py:76`
- `tests/test_effect_verification_adapters.py:226`
- `tests/test_effect_verification_adapters.py:261`
- `tests/test_effect_verification_adapters.py:276`
- `tests/test_effect_verification_adapters.py:301`
- `tests/test_effect_verification_adapters.py:318`
- `tests/test_effect_verification_adapters.py:344`
- `tests/test_effect_verification_adapters.py:351`
- `tests/test_effect_verification_adapters.py:379`
- `tests/test_effect_verification_adapters.py:398`
- `tests/test_effect_verification_adapters.py:411`
- `tests/test_effect_verification_adapters.py:420`

## `capture_dispatch` — function, line 51
- **called from:**
- `src/agent_runtime/effect_adapters.py:252`

## `_exact_operation` — function, line 63
- **called from:**
- `src/agent_runtime/effect_adapters.py:71`

## `_operation` — function, line 70
- **called from:**
- `src/agent_runtime/effect_adapters.py:264`

## `_write_file_digest` — function, line 81
- **called from:**
- `src/agent_runtime/effect_adapters.py:158`

## `_pre_state_text` — function, line 94
- **called from:**
- `src/agent_runtime/effect_adapters.py:123`
- `src/agent_runtime/effect_adapters.py:134`
- `src/agent_runtime/effect_adapters.py:165`

## `_edit_file_digest` — function, line 110
- **called from:**
- `src/agent_runtime/effect_adapters.py:172`

## `_patch_update_digest` — function, line 130
- **called from:**
- `src/agent_runtime/effect_adapters.py:187`

## `_filesystem_scope` — function, line 144
- **called from:**
- `src/agent_runtime/effect_adapters.py:211`
- `tests/test_write_file_empty_body.py:96`

## `classify` — function, line 194
- **called from:**
- `scripts/build_historical_harness_queue.py:251`
- `src/agent_runtime/effect_adapters.py:255`
- `tests/test_build_historical_harness_queue.py:61`
- `tests/test_build_historical_harness_queue.py:67`
- `tests/test_build_historical_harness_queue.py:73`
- `tests/test_build_historical_harness_queue.py:80`
- `tests/tools/build_oversized_test_split_plan.py:196`

## `begin_effect` — function, line 250
- **called from:**
- `src/agent_runtime/journal.py:184`
- `tests/test_effect_verification_adapters.py:52`

## `_server_producer` — function, line 279
- **called from:**
- `src/agent_runtime/effect_adapters.py:292`

## `_facts` — function, line 289
- **called from:**
- `src/agent_runtime/effect_adapters.py:352`

## `_execution` — function, line 300
- **called from:**
- `src/agent_runtime/effect_adapters.py:353`

## `_cleanup` — function, line 323
- **called from:**
- `scripts/diffusion_server.py:439`
- `scripts/diffusion_server.py:443`
- `scripts/diffusion_server.py:457`
- `scripts/diffusion_server.py:468`
- `scripts/diffusion_server.py:488`
- `scripts/diffusion_server.py:504`
- `scripts/diffusion_server.py:635`
- `src/agent_runtime/effect_adapters.py:353`
- `tests/test_process_lifecycle.py:248`
- `tests/test_process_lifecycle.py:269`
- `tests/test_process_lifecycle.py:295`
- `static/js/compare/index.js:1524`
- `static/js/cookbookRunning.js:2840`
- `static/js/cookbookRunning.js:2874`
- `static/js/cookbookRunning.js:2880`
- `static/js/document.js:13672`
- `static/js/document.js:14367`
- `static/js/document.js:14439`
- `static/js/emailInbox.js:1261`
- `static/js/emailInbox.js:1269`
- `static/js/emailInbox.js:1274`

## `settle_effect` — function, line 340
- **called from:**
- `src/agent_runtime/journal.py:214`
- `tests/test_effect_verification_adapters.py:56`

## `_WholeFileRead` — class, line 379
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/effect_adapters.py:398`
- `src/agent_runtime/effect_adapters.py:399`
- `src/agent_runtime/effect_adapters.py:406`
- `src/agent_runtime/effect_adapters.py:410`
- `src/agent_runtime/effect_adapters.py:411`

## `_read_whole` — function, line 384
- **called from:**
- `src/agent_runtime/effect_adapters.py:101`
- `src/agent_runtime/effect_adapters.py:422`

## `_file_observation` — function, line 414
- **called from:**
- `src/agent_runtime/effect_adapters.py:450`

## `_observations` — function, line 439
- **called from:**
- `src/agent_runtime/effect_adapters.py:369`

## `_settle_background` — function, line 471
- **called from:**
- `src/agent_runtime/effect_adapters.py:358`
- `src/agent_runtime/effect_adapters.py:373`

## `settle_background_job` — function, line 486
- **called from:**
- `src/agent_runtime/effect_adapters.py:483`
- `src/bg_monitor.py:57`
