# `routes/shell_routes.py` — definitions & call sites

40 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_require_admin` — function, line 53
- **called from:**
- `routes/shell_routes.py:963`
- `routes/shell_routes.py:981`
- `routes/shell_routes.py:1200`
- `routes/shell_routes.py:1765`
- `routes/shell_routes.py:1820`
- `routes/shell_routes.py:1941`
- `routes/webhook/webhook_routes.py:73`
- `routes/webhook/webhook_routes.py:103`
- `routes/webhook/webhook_routes.py:143`
- `routes/webhook/webhook_routes.py:158`
- `routes/webhook/webhook_routes.py:172`

## `_reject_cross_site` — function, line 72
- **called from:**
- `routes/shell_routes.py:1201`
- `tests/test_shell_routes.py:530`
- `tests/test_shell_routes.py:535`
- `tests/test_shell_routes.py:538`

## `_ssh_base_argv` — function, line 82
- **called from:**
- `routes/shell_routes.py:1451`
- `routes/shell_routes.py:1482`
- `routes/shell_routes.py:1523`
- `routes/shell_routes.py:1682`
- `routes/shell_routes.py:1898`
- `routes/shell_routes.py:1954`
- `tests/test_shell_routes.py:460`
- `tests/test_shell_routes.py:470`
- `tests/test_shell_routes.py:471`
- `tests/test_shell_routes.py:472`
- `tests/test_shell_routes.py:475`
- `tests/test_shell_routes.py:480`
- `tests/test_shell_routes.py:484`
- `tests/test_shell_routes.py:489`

## `_venv_activate_prefix` — function, line 96
- **called from:**
- `routes/shell_routes.py:1449`
- `routes/shell_routes.py:1673`
- `tests/test_shell_routes.py:494`
- `tests/test_shell_routes.py:495`
- `tests/test_shell_routes.py:498`
- `tests/test_shell_routes.py:502`
- `tests/test_shell_routes.py:518`

## `_docker_row_status` — function, line 118
- **called from:**
- `routes/shell_routes.py:1749`
- `tests/test_shell_routes.py:212`
- `tests/test_shell_routes.py:222`
- `tests/test_shell_routes.py:232`
- `tests/test_shell_routes.py:243`
- `tests/test_shell_routes.py:253`
- `tests/test_shell_routes.py:263`

## `_pip_dist_name` — function, line 127
- **called from:**
- `routes/shell_routes.py:1615`
- `routes/shell_routes.py:1626`
- `tests/test_cookbook_package_detection.py:19`
- `tests/test_cookbook_package_detection.py:21`
- `tests/test_cookbook_package_detection.py:25`
- `tests/test_cookbook_package_detection.py:26`
- `tests/test_cookbook_package_detection.py:27`
- `tests/test_cookbook_package_detection.py:28`
- `tests/test_cookbook_package_detection.py:29`
- `tests/test_cookbook_package_detection.py:30`
- `tests/test_cookbook_package_detection.py:34`
- `tests/test_cookbook_package_detection.py:35`
- `tests/test_cookbook_package_detection.py:36`
- `tests/test_cookbook_package_detection.py:41`
- `tests/test_cookbook_package_detection.py:42`

## `_import_optional_dependency_for_status` — function, line 145
- **called from:**
- `routes/shell_routes.py:1625`
- `tests/test_shell_routes.py:452`

## `_package_installed_from_probe` — function, line 150
- **called from:**
- `routes/shell_routes.py:246`
- `routes/shell_routes.py:250`
- `routes/shell_routes.py:254`
- `routes/shell_routes.py:258`
- `routes/shell_routes.py:262`
- `routes/shell_routes.py:273`
- `routes/shell_routes.py:277`
- `routes/shell_routes.py:287`
- `routes/shell_routes.py:1465`
- `tests/test_shell_routes.py:341`
- `tests/test_shell_routes.py:352`
- `tests/test_shell_routes.py:368`
- `tests/test_shell_routes.py:379`
- `tests/test_shell_routes.py:414`
- `tests/test_shell_routes.py:415`

## `_package_status_note` — function, line 215
- **called from:**
- `routes/shell_routes.py:1587`
- `routes/shell_routes.py:1622`
- `tests/test_shell_routes.py:342`
- `tests/test_shell_routes.py:343`
- `tests/test_shell_routes.py:353`
- `tests/test_shell_routes.py:380`

## `_package_pip_update_status` — function, line 301
- **called from:**
- `routes/shell_routes.py:1743`
- `tests/test_shell_routes.py:355`
- `tests/test_shell_routes.py:366`
- `tests/test_shell_routes.py:381`
- `tests/test_shell_routes.py:388`

## `_prepend_user_install_bins_to_path` — function, line 350
- **called from:**
- `routes/shell_routes.py:1216`
- `tests/test_shell_routes.py:423`

## `_package_probe_script` — function, line 378
- **called from:**
- `routes/shell_routes.py:1446`
- `tests/test_shell_routes.py:430`

## `_find_line_break` — function, line 480
- **called from:**
- `routes/shell_routes.py:677`
- `routes/shell_routes.py:699`
- `routes/shell_routes.py:1050`
- `tests/test_shell_routes.py:60`
- `tests/test_shell_routes.py:92`
- `tests/test_shell_routes.py:95`
- `tests/test_shell_routes.py:98`
- `tests/test_shell_routes.py:101`
- `tests/test_shell_routes.py:104`
- `tests/test_shell_routes.py:107`
- `tests/test_shell_routes.py:110`
- `tests/test_shell_routes.py:113`
- `tests/test_shell_routes.py:117`
- `tests/test_shell_routes.py:121`
- `tests/test_shell_routes.py:125`

## `ShellExecRequest` — class, line 502
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_normalize_legacy_remote_tmux_exec` — function, line 514
- **called from:**
- `routes/shell_routes.py:968`

## `_create_shell` — function (async), line 552
- **called from:**
- `routes/shell_routes.py:578`
- `routes/shell_routes.py:1024`

## `_exec_shell` — function (async), line 574
- **called from:**
- `routes/shell_routes.py:973`

## `_generate_pty` — function (async), line 604
- **called from:**
- `routes/shell_routes.py:1014`
- `tests/test_shell_routes.py:75`

## `_wait_proc` — function (async), line 635
- **called from:**
- `routes/shell_routes.py:639`

## `_pty_read` — function, line 730
- **called from:**
- `routes/shell_routes.py:688`

## `_generate_tmux` — function (async), line 745
- **called from:**
- `routes/shell_routes.py:1008`

## `_generate_win_detached` — function (async), line 861
- **called from:**
- `routes/shell_routes.py:1006`

## `setup_shell_routes` — function, line 957
- **called from:**
- `app.py:800`

## `shell_exec` — function (async), line 961
- **route:** `POST /api/shell/exec`
- decorator: `router.post("/api/shell/exec")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `shell_stream` — function (async), line 979
- **route:** `POST /api/shell/stream`
- decorator: `router.post("/api/shell/stream")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `empty` — function (async), line 985
- **called from:**
- `routes/shell_routes.py:989`
- `static/js/chatRenderer.js:1672`
- `static/js/cookbook-hwfit.js:2315`
- `static/js/cookbookRunning.js:2273`
- `static/js/document.js:2243`
- `static/js/documentLibrary.js:3021`
- `static/js/editor/ai-inpaint.js:24`
- `static/js/editor/ai-inpaint.js:299`
- `static/js/editor/build/controls.js:201`
- `static/js/emailInbox.js:960`
- `static/js/galleryEditor.js:4207`
- `static/js/modalManager.js:247`
- `static/js/modalManager.js:306`

## `generate` — function (async), line 1020
- **called from:**
- `routes/shell_routes.py:1110`
- `scripts/mlx_image_server.py:311`

## `_reader` — function (async), line 1033
- **called from:**
- `routes/shell_routes.py:1061`
- `routes/shell_routes.py:1062`
- `services/shell/service.py:124`
- `services/shell/service.py:125`
- `src/agent_tools/subprocess_tools.py:246`
- `src/agent_tools/subprocess_tools.py:247`

## `_os_id_from_release` — function, line 1112
- **called from:**
- `routes/shell_routes.py:1541`
- `routes/shell_routes.py:1554`

## `_install_cmd_for_target` — function, line 1163
- **called from:**
- `routes/shell_routes.py:1730`

## `list_packages` — function (async), line 1184
- **route:** `GET /api/cookbook/packages`
- decorator: `router.get("/api/cookbook/packages")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `install_package` — function (async), line 1763
- **route:** `POST /api/cookbook/packages/install`
- decorator: `router.post("/api/cookbook/packages/install")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `install_system_deps` — function (async), line 1810
- **route:** `POST /api/cookbook/install-system-deps`
- decorator: `router.post("/api/cookbook/install-system-deps")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_apt` — function, line 1833
- **called from:**
- `routes/shell_routes.py:1861`

## `_pacman` — function, line 1834
- **called from:**
- `routes/shell_routes.py:1862`

## `_dnf` — function, line 1836
- **called from:**
- `routes/shell_routes.py:1863`

## `_apk` — function, line 1843
- **called from:**
- `routes/shell_routes.py:1864`

## `_zypper` — function, line 1849
- **called from:**
- `routes/shell_routes.py:1865`

## `_brew` — function, line 1856
- **called from:**
- `routes/shell_routes.py:1866`

## `rebuild_engine` — function (async), line 1931
- **route:** `POST /api/cookbook/rebuild-engine`
- decorator: `router.post("/api/cookbook/rebuild-engine")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
