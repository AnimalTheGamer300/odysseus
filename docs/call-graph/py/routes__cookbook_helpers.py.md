# `routes/cookbook_helpers.py` — definitions & call sites

44 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_git_bash_path` — function, line 57
- **called from:**
- `routes/cookbook_helpers.py:170`
- `routes/cookbook_helpers.py:1235`

## `_validate_repo_id` — function, line 65
- **called from:**
- `routes/cookbook_routes.py:1079`
- `routes/cookbook_routes.py:3872`
- `tests/test_cookbook_helpers.py:265`
- `tests/test_cookbook_helpers.py:267`

## `_validate_serve_model_id` — function, line 71
- **called from:**
- `routes/cookbook_routes.py:1075`
- `routes/cookbook_routes.py:2030`
- `tests/test_cookbook_helpers.py:271`
- `tests/test_cookbook_helpers.py:272`
- `tests/test_cookbook_helpers.py:274`

## `_validate_include` — function, line 79
- **called from:**
- `routes/cookbook_routes.py:1080`

## `_validate_token` — function, line 87
- **called from:**
- `routes/cookbook_routes.py:624`
- `routes/cookbook_routes.py:1085`
- `routes/cookbook_routes.py:1978`

## `load_stored_hf_token` — function, line 95
- **called from:**
- `routes/cookbook_routes.py:636`
- `src/tools/cookbook.py:207`
- `src/tools/cookbook.py:484`
- `tests/test_cookbook_hf_token.py:19`
- `tests/test_cookbook_hf_token.py:20`
- `tests/test_cookbook_hf_token.py:26`
- `tests/test_cookbook_hf_token.py:37`

## `_validate_local_dir` — function, line 113
- **called from:**
- `routes/cookbook_routes.py:1083`
- `tests/test_cookbook_helpers.py:178`
- `tests/test_cookbook_helpers.py:179`
- `tests/test_cookbook_helpers.py:187`
- `tests/test_cookbook_helpers.py:188`
- `tests/test_cookbook_helpers.py:189`
- `tests/test_cookbook_helpers.py:201`
- `tests/test_cookbook_helpers.py:212`
- `tests/test_cookbook_helpers.py:225`
- `tests/test_cookbook_helpers.py:240`
- `tests/test_cookbook_helpers.py:255`

## `_validate_gpus` — function, line 132
- **called from:**
- `routes/cookbook_routes.py:1976`
- `tests/test_cookbook_helpers.py:259`
- `tests/test_cookbook_helpers.py:261`

## `_shell_path` — function, line 140
- **called from:**
- `routes/cookbook_routes.py:1099`
- `tests/test_cookbook_helpers.py:180`
- `tests/test_cookbook_helpers.py:190`

## `_local_tooling_path_export` — function, line 151
- **called from:**
- `routes/cookbook_routes.py:1130`
- `routes/cookbook_routes.py:2158`
- `tests/test_cookbook_helpers.py:281`
- `tests/test_cookbook_helpers.py:287`
- `tests/test_cookbook_helpers.py:523`

## `_pip_install_no_cache` — function, line 182
- **called from:**
- `routes/cookbook_routes.py:2004`
- `tests/test_cookbook_helpers.py:944`
- `tests/test_cookbook_helpers.py:946`
- `tests/test_cookbook_helpers.py:954`
- `tests/test_cookbook_helpers.py:956`
- `tests/test_cookbook_helpers.py:957`

## `_pip_install_attempt` — function, line 197
- **called from:**
- `routes/cookbook_helpers.py:255`
- `routes/cookbook_helpers.py:256`
- `routes/cookbook_helpers.py:257`
- `tests/test_cookbook_helpers.py:468`
- `tests/test_cookbook_helpers.py:479`
- `tests/test_cookbook_helpers.py:486`
- `tests/test_cookbook_helpers.py:498`
- `tests/test_cookbook_helpers.py:510`

## `_pip_command` — function, line 216
- **called from:**
- `routes/cookbook_helpers.py:254`

## `_pip_break_system_packages_check` — function, line 226
- **called from:**
- `routes/cookbook_helpers.py:258`

## `_pip_install_fallback_chain` — function, line 230
- **called from:**
- `routes/cookbook_routes.py:1144`
- `routes/cookbook_routes.py:1149`
- `routes/cookbook_routes.py:1277`
- `routes/cookbook_routes.py:1290`
- `routes/cookbook_routes.py:2286`
- `tests/test_cookbook_helpers.py:293`
- `tests/test_cookbook_helpers.py:312`
- `tests/test_cookbook_helpers.py:324`
- `tests/test_cookbook_helpers.py:381`
- `tests/test_cookbook_helpers.py:389`

## `_venv_safe_local_pip_install_cmd` — function, line 281
- **called from:**
- `routes/cookbook_routes.py:1994`
- `tests/test_cookbook_helpers.py:437`
- `tests/test_cookbook_helpers.py:440`
- `tests/test_cookbook_helpers.py:441`

## `_pip_install_command_without_break_system_packages` — function, line 309
- **called from:**
- `routes/cookbook_helpers.py:346`
- `routes/cookbook_routes.py:2709`

## `_pip_install_help_check_from_cmd` — function, line 318
- **called from:**
- `routes/cookbook_helpers.py:345`

## `_append_pip_install_runner_lines` — function, line 333
- **called from:**
- `routes/cookbook_routes.py:2710`
- `tests/test_cookbook_helpers.py:446`
- `tests/test_cookbook_helpers.py:460`

## `_user_shell_path_bootstrap` — function, line 358
- **called from:**
- `routes/cookbook_routes.py:1114`
- `routes/cookbook_routes.py:1240`
- `routes/cookbook_routes.py:2153`
- `tests/test_cookbook_helpers.py:529`

## `_cached_model_scan_script` — function, line 375
- **called from:**
- `routes/cookbook_routes.py:1424`
- `tests/test_cookbook_helpers.py:837`
- `tests/test_cookbook_helpers.py:867`
- `tests/test_cookbook_helpers.py:893`
- `tests/test_cookbook_helpers.py:924`
- `tests/test_cookbook_helpers.py:970`

## `_ps_squote` — function, line 584
- **called from:**
- `routes/cookbook_routes.py:1174`
- `routes/cookbook_routes.py:1179`
- `routes/cookbook_routes.py:1187`
- `routes/cookbook_routes.py:2091`

## `_bash_squote` — function, line 591
- **called from:**
- `routes/cookbook_routes.py:138`
- `routes/cookbook_routes.py:155`
- `routes/cookbook_routes.py:156`
- `routes/cookbook_routes.py:1116`
- `routes/cookbook_routes.py:1244`
- `routes/cookbook_routes.py:2165`
- `routes/cookbook_routes.py:2305`
- `routes/cookbook_routes.py:2320`
- `routes/cookbook_routes.py:2349`
- `routes/cookbook_routes.py:2441`
- `routes/cookbook_routes.py:2465`
- `routes/cookbook_routes.py:2576`
- `routes/cookbook_routes.py:2664`
- `tests/test_ollama_runner_hint.py:51`

## `_ollama_bind_from_cmd` — function, line 672
- **called from:**
- `routes/cookbook_routes.py:2296`
- `tests/test_cookbook_helpers.py:662`
- `tests/test_cookbook_helpers.py:663`
- `tests/test_cookbook_helpers.py:668`
- `tests/test_cookbook_helpers.py:675`
- `tests/test_cookbook_helpers.py:679`
- `tests/test_cookbook_helpers.py:686`
- `tests/test_cookbook_helpers.py:690`

## `_normalize_llama_cpp_python_cache_types` — function, line 701
- **called from:**
- `routes/cookbook_routes.py:1991`
- `tests/test_cookbook_helpers.py:638`
- `tests/test_cookbook_helpers.py:647`

## `repl` — function, line 706
- **called from:**
- `src/text_helpers.py:111`

## `_check_serve_binary` — function, line 717
- **called from:**
- `routes/cookbook_helpers.py:772`
- `routes/cookbook_helpers.py:788`

## `_is_safe_serve_subshell` — function, line 737
- **called from:**
- `routes/cookbook_helpers.py:781`

## `_validate_serve_cmd` — function, line 744
- **called from:**
- `routes/cookbook_routes.py:1990`
- `tests/test_cookbook_docker_access.py:262`
- `tests/test_cookbook_helpers.py:590`
- `tests/test_cookbook_helpers.py:607`
- `tests/test_cookbook_helpers.py:616`
- `tests/test_cookbook_helpers.py:629`
- `tests/test_cookbook_helpers.py:1004`
- `tests/test_cookbook_helpers.py:1013`
- `tests/test_cookbook_helpers.py:1028`

## `_replace_safe_subshell` — function, line 779
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_append_serve_preflight_exit_lines` — function, line 792
- **called from:**
- `routes/cookbook_routes.py:2686`
- `routes/cookbook_routes.py:2701`
- `tests/test_cookbook_helpers.py:551`

## `_append_vllm_linux_preflight_lines` — function, line 810
- **called from:**
- `tests/test_cookbook_helpers.py:424`

## `_append_serve_exit_code_lines` — function, line 825
- **called from:**
- `routes/cookbook_routes.py:2716`
- `routes/cookbook_routes.py:2723`
- `tests/test_cookbook_helpers.py:564`
- `tests/test_cookbook_helpers.py:575`

## `_append_llama_cpp_linux_accel_build_lines` — function, line 846
- **called from:**
- `routes/cookbook_routes.py:2218`
- `tests/test_cookbook_helpers.py:697`
- `tests/test_cookbook_helpers.py:712`
- `tests/test_cookbook_helpers.py:731`
- `tests/test_cookbook_helpers.py:741`
- `tests/test_cookbook_helpers.py:758`
- `tests/test_cookbook_helpers.py:765`

## `_llama_cpp_rebuild_cmd` — function, line 1033
- **called from:**
- `routes/shell_routes.py:1951`
- `tests/test_cookbook_helpers.py:773`
- `tests/test_cookbook_helpers.py:811`

## `ModelDownloadRequest` — class, line 1066
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ServeRequest` — class, line 1079
- **called from:**
- `routes/codex_routes.py:659`
- `routes/codex_routes.py:810`
- `tests/test_cookbook_docker_access.py:161`
- `tests/test_cookbook_docker_access.py:225`
- `tests/test_cookbook_remote_windows_diffusers.py:45`

## `_parse_serve_phase` — function, line 1090
- **called from:**
- `routes/cookbook_routes.py:4446`
- `routes/cookbook_routes.py:4553`

## `_ssh` — function, line 1148
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_safe_env_prefix` — function, line 1154
- **called from:**
- `routes/cookbook_routes.py:1184`
- `routes/cookbook_routes.py:1250`
- `routes/cookbook_routes.py:1339`
- `routes/cookbook_routes.py:2095`
- `routes/cookbook_routes.py:2169`
- `tests/test_cookbook_helpers.py:39`
- `tests/test_cookbook_helpers.py:96`
- `tests/test_cookbook_helpers.py:101`
- `tests/test_cookbook_helpers.py:106`
- `tests/test_cookbook_helpers.py:131`

## `_local_windows_bash_env_prefix` — function, line 1207
- **called from:**
- `routes/cookbook_routes.py:1339`
- `routes/cookbook_routes.py:2169`
- `tests/test_cookbook_helpers.py:128`
- `tests/test_cookbook_helpers.py:146`
- `tests/test_cookbook_helpers.py:152`

## `_ssh_ps` — function, line 1242
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_diagnose_serve_output` — function, line 1252
- **called from:**
- `routes/cookbook_routes.py:4557`
- `tests/test_cookbook_diagnosis.py:10`
- `tests/test_cookbook_diagnosis.py:29`
- `tests/test_cookbook_error_feedback.py:6`
- `tests/test_cookbook_error_feedback.py:14`
- `tests/test_cookbook_error_feedback.py:22`
- `tests/test_cookbook_error_feedback.py:30`
- `tests/test_cookbook_error_feedback.py:37`
- `tests/test_cookbook_error_feedback.py:47`
- `tests/test_cookbook_error_feedback.py:53`
- `tests/test_cookbook_error_feedback.py:57`
- `tests/test_cookbook_error_feedback.py:58`
- `tests/test_cookbook_error_feedback.py:63`
- `tests/test_cookbook_error_feedback.py:70`

## `run_ssh_command_async` — function (async), line 1448
- **called from:**
- `routes/cookbook_routes.py:971`
- `tests/test_cookbook_helpers.py:64`
