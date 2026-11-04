# `core/platform_compat.py` — definitions & call sites

19 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `safe_chmod` — function, line 40
- **called from:**
- `core/database.py:2123`
- `core/database.py:2138`
- `routes/cookbook_routes.py:839`
- `routes/cookbook_routes.py:879`
- `routes/cookbook_routes.py:942`
- `routes/cookbook_routes.py:956`
- `routes/cookbook_routes.py:957`
- `routes/cookbook_routes.py:1325`
- `routes/cookbook_routes.py:2733`
- `routes/vault/vault_routes.py:77`
- `src/api_key_manager.py:23`
- `src/api_key_manager.py:33`
- `src/integrations.py:258`
- `src/secret_storage.py:45`

## `detached_popen_kwargs` — function, line 58
- **called from:**
- `routes/cookbook_routes.py:1048`
- `routes/shell_routes.py:901`
- `src/bg_jobs.py:139`

## `pid_alive` — function, line 75
- **called from:**
- `routes/cookbook_routes.py:3346`
- `routes/cookbook_routes.py:4425`
- `src/bg_jobs.py:78`

## `kill_process_tree` — function, line 112
- **called from:**
- `src/bg_jobs.py:235`

## `_ssh_path_override` — function, line 180
- **called from:**
- `core/platform_compat.py:185`
- `tests/test_platform_compat.py:194`

## `_windows_bash_fallbacks` — function, line 188
- **called from:**
- `core/platform_compat.py:250`

## `_is_windows_bash_stub` — function, line 210
- **called from:**
- `core/platform_compat.py:247`

## `git_bash_path` — function, line 219
- **called from:**
- `routes/shell_routes.py:879`
- `routes/shell_routes.py:880`
- `src/bg_jobs.py:111`
- `tests/test_cookbook_helpers.py:809`

## `find_bash` — function, line 234
- **called from:**
- `core/platform_compat.py:259`
- `core/platform_compat.py:289`
- `routes/cookbook_routes.py:1006`
- `routes/shell_routes.py:568`
- `routes/shell_routes.py:875`
- `src/agent_tools/subprocess_tools.py:31`
- `src/bg_jobs.py:100`
- `src/builtin_actions.py:777`
- `src/builtin_actions.py:793`
- `src/builtin_actions.py:794`
- `src/builtin_actions.py:803`
- `src/builtin_actions.py:804`
- `tests/test_cookbook_helpers.py:807`
- `tests/test_platform_compat.py:33`
- `tests/test_platform_compat.py:47`
- `tests/test_platform_compat.py:61`
- `tests/test_platform_compat.py:77`

## `has_bash` — function, line 258
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `which_tool` — function, line 262
- **called from:**
- `core/platform_compat.py:246`
- `routes/cookbook_routes.py:841`
- `routes/cookbook_routes.py:842`
- `routes/cookbook_routes.py:946`
- `routes/cookbook_routes.py:1453`
- `routes/cookbook_routes.py:1453`
- `routes/cookbook_routes.py:1454`
- `routes/shell_routes.py:1593`
- `routes/vault/vault_routes.py:33`
- `src/builtin_mcp.py:27`
- `src/builtin_mcp.py:40`

## `run_script_argv` — function, line 280
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `is_wsl` — function, line 298
- **called from:**
- `core/platform_compat.py:321`
- `core/platform_compat.py:340`
- `core/platform_compat.py:445`
- `tests/test_platform_compat.py:91`
- `tests/test_platform_compat.py:98`
- `tests/test_platform_compat.py:110`

## `translate_path` — function, line 311
- **called from:**
- `core/platform_compat.py:345`
- `tests/test_platform_compat.py:116`
- `tests/test_platform_compat.py:124`
- `tests/test_platform_compat.py:139`

## `get_wsl_windows_user_profile` — function, line 338
- **called from:**
- `tests/test_platform_compat.py:152`
- `tests/test_platform_compat.py:177`
- `tests/test_platform_compat.py:189`

## `_ssh_exec_argv` — function, line 362
- **called from:**
- `core/platform_compat.py:407`
- `routes/cookbook_helpers.py:1463`
- `tests/test_hwfit_remote_validation.py:63`
- `tests/test_hwfit_remote_validation.py:65`
- `tests/test_platform_compat.py:258`
- `tests/test_platform_compat.py:263`

## `run_ssh_command` — function, line 395
- **called from:**
- `routes/hwfit_routes.py:118`
- `services/hwfit/hardware.py:35`
- `tests/test_platform_compat.py:298`

## `_windows_powershell_argv` — function, line 420
- **called from:**
- `core/platform_compat.py:448`
- `tests/test_platform_compat.py:198`
- `tests/test_platform_compat.py:209`

## `run_wsl_windows_powershell` — function, line 435
- **called from:**
- `core/platform_compat.py:343`
- `tests/test_platform_compat.py:220`
- `tests/test_platform_compat.py:242`
