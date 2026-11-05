# `core/platform_compat.py` — definitions & call sites

21 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `has_procfs` — function, line 47
- **called from:**
- `src/agent_tools/web_tools.py:2445`
- `src/agent_tools/web_tools_prewave3.py:2454`
- `src/browser_lifecycle.py:96`
- `src/browser_lifecycle.py:280`
- `src/browser_lifecycle.py:459`
- `src/process_lifecycle.py:267`
- `src/process_ownership.py:123`
- `src/process_ownership.py:304`
- `src/tools/cookbook.py:681`
- `tests/test_browser_lifecycle.py:271`
- `tests/test_process_lifecycle.py:182`
- `tests/test_process_lifecycle.py:238`
- `tests/test_process_lifecycle.py:253`

## `safe_chmod` — function, line 53
- **called from:**
- `core/database.py:2429`
- `core/database.py:2444`
- `routes/cookbook_routes.py:713`
- `routes/cookbook_routes.py:753`
- `routes/cookbook_routes.py:816`
- `routes/cookbook_routes.py:830`
- `routes/cookbook_routes.py:831`
- `routes/cookbook_routes.py:1200`
- `routes/cookbook_routes.py:2604`
- `routes/vault/vault_routes.py:78`
- `src/api_key_manager.py:23`
- `src/api_key_manager.py:33`
- `src/integrations.py:258`
- `src/secret_storage.py:45`

## `service_home` — function, line 71
- **called from:**
- `src/agent_tools/web_tools.py:34`
- `tests/test_platform_compat.py:340`
- `tests/test_platform_compat.py:353`
- `tests/test_platform_compat.py:364`

## `detached_popen_kwargs` — function, line 91
- **called from:**
- `routes/cookbook_routes.py:922`
- `routes/shell_routes.py:1135`
- `src/bg_jobs.py:135`

## `pid_alive` — function, line 108
- **called from:**
- `routes/cookbook_routes.py:3225`
- `routes/cookbook_routes.py:4335`
- `routes/shell_routes.py:723`
- `src/agent_tools/web_tools.py:191`
- `src/agent_tools/web_tools_prewave3.py:195`
- `src/bg_jobs.py:78`
- `src/browser_lifecycle.py:281`
- `src/browser_lifecycle.py:460`
- `src/containment.py:1308`
- `src/containment.py:1427`
- `src/containment.py:1524`
- `src/containment.py:1526`
- `src/containment.py:1651`
- `src/process_lifecycle.py:360`
- `src/process_lifecycle.py:657`
- `src/process_lifecycle.py:659`
- `tests/test_containment_process_tree.py:85`
- `tests/test_containment_process_tree.py:88`
- `tests/test_containment_process_tree.py:225`
- `tests/test_containment_process_tree.py:392`
- `tests/test_containment_process_tree.py:393`
- `tests/test_containment_process_tree.py:394`
- `tests/test_containment_process_tree.py:395`
- `tests/test_containment_process_tree.py:396`
- `tests/test_containment_process_tree.py:397`
- `tests/test_containment_process_tree.py:404`
- `tests/test_containment_process_tree.py:415`
- `tests/test_containment_process_tree.py:416`
- `tests/test_containment_process_tree.py:419`
- `tests/test_containment_process_tree.py:420`
- `tests/test_containment_process_tree.py:421`
- `tests/test_containment_process_tree.py:422`
- `tests/test_containment_process_tree.py:430`
- `tests/test_native_execution_containment.py:102`
- `tests/test_shell_routes.py:182`
- `tests/test_shell_routes.py:213`
- `tests/test_shell_routes.py:218`
- `tests/test_shell_routes.py:233`
- `tests/test_shell_routes.py:237`
- `tests/test_shell_routes.py:261`
- `tests/test_shell_routes.py:288`

## `kill_process_tree` — function, line 153
- **called from:**
- `src/bg_jobs.py:191`
- `src/bg_jobs.py:319`
- `tests/test_process_lifecycle.py:291`

## `_ssh_path_override` — function, line 202
- **called from:**
- `core/platform_compat.py:207`
- `tests/test_platform_compat.py:195`

## `_windows_bash_fallbacks` — function, line 210
- **called from:**
- `core/platform_compat.py:272`

## `_is_windows_bash_stub` — function, line 232
- **called from:**
- `core/platform_compat.py:269`

## `git_bash_path` — function, line 241
- **called from:**
- `routes/shell_routes.py:1113`
- `routes/shell_routes.py:1114`
- `tests/test_cookbook_dependency_completion_regression.py:645`
- `tests/test_cookbook_dependency_completion_regression.py:814`
- `tests/test_cookbook_dependency_completion_regression.py:828`
- `tests/test_cookbook_dependency_completion_regression.py:881`
- `tests/test_cookbook_dependency_completion_regression.py:881`
- `tests/test_cookbook_dependency_completion_regression.py:898`
- `tests/test_cookbook_dependency_completion_regression.py:898`
- `tests/test_cookbook_dependency_completion_regression.py:928`
- `tests/test_cookbook_dependency_completion_regression.py:928`
- `tests/test_cookbook_dependency_completion_regression.py:944`
- `tests/test_cookbook_dependency_completion_regression.py:944`
- `tests/test_cookbook_dependency_completion_regression.py:977`
- `tests/test_cookbook_dependency_completion_regression.py:977`
- `tests/test_cookbook_dependency_completion_regression.py:989`
- `tests/test_cookbook_dependency_completion_regression.py:1131`
- `tests/test_cookbook_dependency_completion_regression.py:1131`
- `tests/test_cookbook_dependency_completion_regression.py:1152`
- `tests/test_cookbook_dependency_completion_regression.py:1152`
- `tests/test_cookbook_dependency_completion_regression.py:1162`
- `tests/test_cookbook_dependency_completion_regression.py:1186`
- `tests/test_cookbook_dependency_completion_regression.py:1186`
- `tests/test_cookbook_dependency_completion_regression.py:1189`
- `tests/test_cookbook_dependency_completion_regression.py:1194`
- `tests/test_cookbook_dependency_completion_regression.py:1210`
- `tests/test_cookbook_dependency_completion_regression.py:1214`
- `tests/test_cookbook_dependency_completion_regression.py:1214`
- `tests/test_cookbook_dependency_completion_regression.py:1240`
- `tests/test_cookbook_dependency_completion_regression.py:1240`
- `tests/test_cookbook_dependency_completion_regression.py:1249`
- `tests/test_cookbook_dependency_completion_regression.py:1265`
- `tests/test_cookbook_dependency_completion_regression.py:1265`
- `tests/test_cookbook_dependency_completion_regression.py:1348`
- `tests/test_cookbook_dependency_completion_regression.py:1348`
- `tests/test_cookbook_dependency_completion_regression.py:1348`
- `tests/test_cookbook_helpers.py:810`

## `find_bash` — function, line 256
- **called from:**
- `core/platform_compat.py:281`
- `core/platform_compat.py:311`
- `routes/cookbook_routes.py:880`
- `routes/shell_routes.py:649`
- `routes/shell_routes.py:1109`
- `src/agent_tools/subprocess_tools.py:112`
- `src/builtin_actions.py:911`
- `src/builtin_actions.py:927`
- `src/builtin_actions.py:928`
- `src/builtin_actions.py:937`
- `src/builtin_actions.py:938`
- `src/containment.py:928`
- `tests/test_cookbook_dependency_completion_regression.py:644`
- `tests/test_cookbook_helpers.py:808`
- `tests/test_platform_compat.py:34`
- `tests/test_platform_compat.py:48`
- `tests/test_platform_compat.py:62`
- `tests/test_platform_compat.py:78`

## `has_bash` — function, line 280
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `which_tool` — function, line 284
- **called from:**
- `core/platform_compat.py:268`
- `routes/cookbook_routes.py:715`
- `routes/cookbook_routes.py:716`
- `routes/cookbook_routes.py:820`
- `routes/cookbook_routes.py:1324`
- `routes/cookbook_routes.py:1324`
- `routes/cookbook_routes.py:1325`
- `routes/shell_routes.py:1852`
- `routes/vault/vault_routes.py:34`
- `src/builtin_mcp.py:27`
- `src/builtin_mcp.py:40`

## `run_script_argv` — function, line 302
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `is_wsl` — function, line 320
- **called from:**
- `core/platform_compat.py:343`
- `core/platform_compat.py:362`
- `core/platform_compat.py:467`
- `tests/test_platform_compat.py:92`
- `tests/test_platform_compat.py:99`
- `tests/test_platform_compat.py:111`

## `translate_path` — function, line 333
- **called from:**
- `core/platform_compat.py:367`
- `tests/test_platform_compat.py:117`
- `tests/test_platform_compat.py:125`
- `tests/test_platform_compat.py:140`

## `get_wsl_windows_user_profile` — function, line 360
- **called from:**
- `tests/test_platform_compat.py:153`
- `tests/test_platform_compat.py:178`
- `tests/test_platform_compat.py:190`

## `_ssh_exec_argv` — function, line 384
- **called from:**
- `core/platform_compat.py:429`
- `routes/cookbook_helpers.py:1650`
- `tests/test_hwfit_remote_validation.py:63`
- `tests/test_hwfit_remote_validation.py:65`
- `tests/test_platform_compat.py:259`
- `tests/test_platform_compat.py:264`

## `run_ssh_command` — function, line 417
- **called from:**
- `routes/hwfit_routes.py:137`
- `services/hwfit/hardware.py:35`
- `tests/test_platform_compat.py:299`

## `_windows_powershell_argv` — function, line 442
- **called from:**
- `core/platform_compat.py:470`
- `tests/test_platform_compat.py:199`
- `tests/test_platform_compat.py:210`

## `run_wsl_windows_powershell` — function, line 457
- **called from:**
- `core/platform_compat.py:365`
- `tests/test_platform_compat.py:221`
- `tests/test_platform_compat.py:243`
