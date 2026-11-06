# `routes/shell_routes.py` — definitions & call sites

49 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_require_admin` — function, line 60
- **called from:**
- `routes/codex_routes.py:132`
- `routes/cookbook_routes.py:418`
- `routes/cookbook_routes.py:429`
- `routes/cookbook_routes.py:437`
- `routes/shell_routes.py:1197`
- `routes/shell_routes.py:1215`
- `routes/shell_routes.py:1435`
- `routes/shell_routes.py:2037`
- `routes/shell_routes.py:2093`
- `routes/shell_routes.py:2223`
- `routes/webhook/webhook_routes.py:73`
- `routes/webhook/webhook_routes.py:103`
- `routes/webhook/webhook_routes.py:143`
- `routes/webhook/webhook_routes.py:158`
- `routes/webhook/webhook_routes.py:172`
- `tests/test_runtime_resource_integration.py:298`
- `tests/test_runtime_resource_integration.py:310`
- `tests/test_runtime_resource_integration.py:319`
- `tests/test_wave3_local_control.py:49`
- `tests/test_wave3_local_control.py:52`
- `tests/test_wave3_local_control.py:60`
- `tests/test_wave3_local_control.py:63`

## `_reject_cross_site` — function, line 85
- **called from:**
- `routes/shell_routes.py:1436`
- `tests/test_shell_routes.py:894`
- `tests/test_shell_routes.py:899`
- `tests/test_shell_routes.py:902`

## `_ssh_base_argv` — function, line 102
- **called from:**
- `routes/shell_routes.py:1710`
- `routes/shell_routes.py:1741`
- `routes/shell_routes.py:1782`
- `routes/shell_routes.py:1949`
- `routes/shell_routes.py:2179`
- `routes/shell_routes.py:2236`
- `tests/test_shell_routes.py:824`
- `tests/test_shell_routes.py:834`
- `tests/test_shell_routes.py:835`
- `tests/test_shell_routes.py:836`
- `tests/test_shell_routes.py:839`
- `tests/test_shell_routes.py:844`
- `tests/test_shell_routes.py:848`
- `tests/test_shell_routes.py:853`

## `_venv_activate_prefix` — function, line 116
- **called from:**
- `routes/shell_routes.py:1708`
- `routes/shell_routes.py:1940`
- `tests/test_shell_routes.py:858`
- `tests/test_shell_routes.py:859`
- `tests/test_shell_routes.py:862`
- `tests/test_shell_routes.py:866`
- `tests/test_shell_routes.py:882`

## `_docker_row_status` — function, line 138
- **called from:**
- `routes/shell_routes.py:2016`
- `tests/test_shell_routes.py:581`
- `tests/test_shell_routes.py:591`
- `tests/test_shell_routes.py:601`
- `tests/test_shell_routes.py:612`
- `tests/test_shell_routes.py:622`
- `tests/test_shell_routes.py:632`

## `_pip_dist_name` — function, line 147
- **called from:**
- `routes/shell_routes.py:1882`
- `routes/shell_routes.py:1893`
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

## `_import_optional_dependency_for_status` — function, line 165
- **called from:**
- `routes/shell_routes.py:1892`
- `tests/test_shell_routes.py:816`

## `_package_installed_from_probe` — function, line 170
- **called from:**
- `routes/shell_routes.py:279`
- `routes/shell_routes.py:283`
- `routes/shell_routes.py:287`
- `routes/shell_routes.py:291`
- `routes/shell_routes.py:299`
- `routes/shell_routes.py:303`
- `routes/shell_routes.py:313`
- `routes/shell_routes.py:317`
- `routes/shell_routes.py:328`
- `routes/shell_routes.py:332`
- `routes/shell_routes.py:342`
- `routes/shell_routes.py:1724`
- `tests/test_shell_routes.py:705`
- `tests/test_shell_routes.py:716`
- `tests/test_shell_routes.py:732`
- `tests/test_shell_routes.py:743`
- `tests/test_shell_routes.py:778`
- `tests/test_shell_routes.py:779`

## `_package_status_note` — function, line 248
- **called from:**
- `routes/shell_routes.py:1846`
- `routes/shell_routes.py:1889`
- `tests/test_shell_routes.py:706`
- `tests/test_shell_routes.py:707`
- `tests/test_shell_routes.py:717`
- `tests/test_shell_routes.py:744`

## `_package_pip_update_status` — function, line 356
- **called from:**
- `routes/shell_routes.py:2010`
- `tests/test_shell_routes.py:719`
- `tests/test_shell_routes.py:730`
- `tests/test_shell_routes.py:745`
- `tests/test_shell_routes.py:752`

## `_prepend_user_install_bins_to_path` — function, line 405
- **called from:**
- `routes/shell_routes.py:1454`
- `tests/test_shell_routes.py:787`

## `_package_probe_script` — function, line 433
- **called from:**
- `routes/shell_routes.py:1705`
- `tests/test_shell_routes.py:794`

## `_find_line_break` — function, line 547
- **called from:**
- `routes/shell_routes.py:915`
- `routes/shell_routes.py:937`
- `routes/shell_routes.py:1284`
- `tests/test_shell_routes.py:65`
- `tests/test_shell_routes.py:461`
- `tests/test_shell_routes.py:464`
- `tests/test_shell_routes.py:467`
- `tests/test_shell_routes.py:470`
- `tests/test_shell_routes.py:473`
- `tests/test_shell_routes.py:476`
- `tests/test_shell_routes.py:479`
- `tests/test_shell_routes.py:482`
- `tests/test_shell_routes.py:486`
- `tests/test_shell_routes.py:490`
- `tests/test_shell_routes.py:494`

## `ShellExecRequest` — class, line 583
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_normalize_legacy_remote_tmux_exec` — function, line 595
- **called from:**
- `routes/shell_routes.py:1202`

## `_create_shell` — function (async), line 633
- **called from:**
- `routes/shell_routes.py:659`
- `routes/shell_routes.py:1258`

## `_exec_shell` — function (async), line 655
- **called from:**
- `routes/shell_routes.py:1207`

## `_session_pgid` — function, line 685
- **called from:**
- `routes/shell_routes.py:740`
- `tests/test_shell_routes.py:371`

## `_signal_session` — function, line 700
- **called from:**
- `routes/shell_routes.py:797`
- `routes/shell_routes.py:799`
- `routes/shell_routes.py:802`

## `_session_alive` — function, line 711
- **called from:**
- `routes/shell_routes.py:790`
- `tests/test_shell_routes.py:429`
- `tests/test_shell_routes.py:435`

## `_bind_pty_spawn_identity` — function, line 726
- **called from:**
- `routes/shell_routes.py:865`
- `tests/test_shell_routes.py:132`
- `tests/test_shell_routes.py:372`
- `tests/test_shell_routes.py:400`

## `_terminate_pty_session` — function (async), line 747
- **called from:**
- `routes/shell_routes.py:829`
- `routes/shell_routes.py:881`
- `tests/test_shell_routes.py:215`
- `tests/test_shell_routes.py:220`
- `tests/test_shell_routes.py:235`
- `tests/test_shell_routes.py:239`
- `tests/test_shell_routes.py:304`
- `tests/test_shell_routes.py:321`
- `tests/test_shell_routes.py:377`
- `tests/test_shell_routes.py:411`
- `tests/test_shell_routes.py:454`

## `_gone` — function, line 783
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_send` — function, line 793
- **called from:**
- `src/browser_identity.py:349`
- `src/browser_identity.py:367`

## `_reap_leader` — function (async), line 805
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_terminate_pty_session_quietly` — function (async), line 820
- **called from:**
- `routes/shell_routes.py:891`
- `routes/shell_routes.py:953`

## `_generate_pty` — function (async), line 840
- **called from:**
- `routes/shell_routes.py:1248`
- `tests/test_shell_routes.py:103`
- `tests/test_shell_routes.py:254`
- `tests/test_shell_routes.py:283`
- `tests/test_shell_routes.py:346`

## `_wait_proc` — function (async), line 872
- **called from:**
- `routes/shell_routes.py:876`

## `_pty_read` — function, line 964
- **called from:**
- `routes/shell_routes.py:926`

## `_generate_tmux` — function (async), line 979
- **called from:**
- `routes/shell_routes.py:1242`

## `_generate_win_detached` — function (async), line 1095
- **called from:**
- `routes/shell_routes.py:1240`

## `setup_shell_routes` — function, line 1191
- **called from:**
- `app.py:884`
- `tests/test_wave3_local_control.py:104`

## `shell_exec` — function (async), line 1195
- **route:** `POST /api/shell/exec`
- decorator: `router.post("/api/shell/exec")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `shell_stream` — function (async), line 1213
- **route:** `POST /api/shell/stream`
- decorator: `router.post("/api/shell/stream")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `empty` — function (async), line 1219
- **called from:**
- `routes/chat_routes.py:3824`
- `routes/shell_routes.py:1223`
- `routes/skills_routes.py:610`
- `services/skills/agent_runner.py:65`
- `services/skills/agent_runner.py:213`
- `src/agent_runtime/authority.py:265`
- `src/agent_runtime/authority.py:567`
- `src/agent_runtime/authority.py:615`
- `src/agent_runtime/authority.py:620`
- `src/agent_runtime/authority.py:669`
- `src/agent_runtime/authority.py:691`
- `src/agent_runtime/authority.py:722`
- `src/bg_monitor.py:80`
- `tests/test_resource_identity.py:642`
- `tests/test_skills_audit_services.py:198`
- `static/js/chatRenderer.js:2250`
- `static/js/cookbook-hwfit.js:2425`
- `static/js/cookbookRunning.js:2329`
- `static/js/document.js:3340`
- `static/js/documentLibrary.js:3302`
- `static/js/editor/ai-inpaint.js:24`
- `static/js/editor/ai-inpaint.js:336`
- `static/js/editor/build/controls.js:702`
- `static/js/emailInbox.js:1005`
- `static/js/galleryEditor.js:13996`
- `static/js/modalManager.js:247`
- `static/js/modalManager.js:306`

## `generate` — function (async), line 1254
- **called from:**
- `routes/shell_routes.py:1344`
- `scripts/mlx_image_server.py:311`

## `_reader` — function (async), line 1267
- **called from:**
- `routes/shell_routes.py:1295`
- `routes/shell_routes.py:1296`
- `services/shell/service.py:124`
- `services/shell/service.py:125`

## `_os_id_from_release` — function, line 1346
- **called from:**
- `routes/shell_routes.py:1800`
- `routes/shell_routes.py:1813`

## `_install_cmd_for_target` — function, line 1398
- **called from:**
- `routes/shell_routes.py:1997`

## `list_packages` — function (async), line 1419
- **route:** `GET /api/cookbook/packages`
- decorator: `router.get("/api/cookbook/packages")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `install_package` — function (async), line 2035
- **route:** `POST /api/cookbook/packages/install`
- decorator: `router.post("/api/cookbook/packages/install")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `install_system_deps` — function (async), line 2083
- **route:** `POST /api/cookbook/install-system-deps`
- decorator: `router.post("/api/cookbook/install-system-deps")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_apt` — function, line 2106
- **called from:**
- `routes/shell_routes.py:2142`

## `_pacman` — function, line 2107
- **called from:**
- `routes/shell_routes.py:2143`

## `_dnf` — function, line 2109
- **called from:**
- `routes/shell_routes.py:2144`

## `_apk` — function, line 2116
- **called from:**
- `routes/shell_routes.py:2145`

## `_zypper` — function, line 2122
- **called from:**
- `routes/shell_routes.py:2146`

## `_brew` — function, line 2129
- **called from:**
- `routes/shell_routes.py:2147`

## `rebuild_engine` — function (async), line 2213
- **route:** `POST /api/cookbook/rebuild-engine`
- decorator: `router.post("/api/cookbook/rebuild-engine")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
