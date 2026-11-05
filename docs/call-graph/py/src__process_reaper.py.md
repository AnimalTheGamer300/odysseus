# `src/process_reaper.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `reap_containment_grants` — function, line 43
- **called from:**
- `src/process_reaper.py:298`
- `tests/test_agent_tmux_retirement.py:108`
- `tests/test_background_containment.py:121`
- `tests/test_orphan_reaping.py:199`
- `tests/test_orphan_reaping.py:257`
- `tests/test_orphan_reaping.py:271`
- `tests/test_orphan_reaping.py:289`
- `tests/test_orphan_reaping.py:308`
- `tests/test_orphan_reaping.py:324`
- `tests/test_orphan_reaping.py:336`

## `reap_bg_jobs` — function, line 137
- **called from:**
- `src/process_reaper.py:299`

## `reap_legacy_agent_tmux` — function, line 155
- **called from:**
- `src/process_reaper.py:300`
- `tests/test_agent_tmux_retirement.py:62`
- `tests/test_agent_tmux_retirement.py:71`
- `tests/test_agent_tmux_retirement.py:79`
- `tests/test_agent_tmux_retirement.py:88`
- `tests/test_agent_tmux_retirement.py:98`
- `tests/test_agent_tmux_retirement.py:130`
- `tests/test_agent_tmux_retirement.py:152`
- `tests/test_agent_tmux_retirement.py:163`

## `snapshot` — function, line 176
- **called from:**
- `src/process_reaper.py:207`
- `src/process_reaper.py:234`
- `src/process_reaper.py:263`
- `src/process_reaper.py:271`
- `static/js/editor/editor-control.js:50`
- `static/js/editor/editor-control.js:65`
- `static/js/editor/tools/quick-select.js:3`
- `static/js/emailLibrary/index.js:3824`
- `static/js/galleryEditor.js:4243`
- `static/js/galleryEditor.js:4315`

## `launcher_is_ours` — function, line 191
- **called from:**
- `src/process_reaper.py:210`

## `reap_orphans` — function, line 281
- **called from:**
- `tests/test_orphan_reaping.py:438`

## `reap_orphans_at_startup` — function (async), line 312
- **called from:**
- `app.py:1451`
