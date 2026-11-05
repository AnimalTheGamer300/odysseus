# `src/containment_worker.py` — definitions & call sites

2 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `supervise` — function (async), line 25
- **called from:**
- `src/containment_worker.py:120`

## `capture` — function, line 78
- **called from:**
- `routes/shell_routes.py:739`
- `scripts/css_snapshot.py:258`
- `scripts/run_sft_environment_expansion.py:695`
- `scripts/verify_notes_browser_runtime.py:74`
- `src/agent_tools/web_tools.py:115`
- `src/agent_tools/web_tools_prewave3.py:119`
- `src/bg_jobs.py:162`
- `src/containment.py:475`
- `src/containment.py:1096`
- `src/containment.py:1127`
- `src/containment.py:1254`
- `src/process_lifecycle.py:122`
- `tests/test_ai_interaction_owner_scope.py:52`
- `tests/test_ai_interaction_owner_scope.py:57`
- `tests/test_css_computed_style_snapshot.py:94`
- `tests/test_css_computed_style_snapshot.py:103`
- `tests/test_css_computed_style_snapshot.py:152`
- `tests/test_css_computed_style_snapshot.py:153`
- `tests/test_css_computed_style_snapshot.py:166`
- `tests/test_css_computed_style_snapshot.py:183`
- `tests/test_css_computed_style_snapshot.py:186`
- `tests/test_notes_native_cleanup.py:24`
- `tests/test_notes_native_cleanup.py:28`
- `tests/test_process_lifecycle.py:185`
- `tests/test_process_lifecycle.py:242`
- `tests/test_process_ownership.py:103`
- `tests/test_process_ownership.py:152`
- `static/js/signature.js:4`
- `static/js/signature.js:379`
- `static/js/signature.js:517`
