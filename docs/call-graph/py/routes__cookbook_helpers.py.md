# `routes/cookbook_helpers.py` — definitions & call sites

48 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_git_bash_path` — function, line 58
- **called from:**
- `routes/cookbook_helpers.py:171`
- `routes/cookbook_helpers.py:1408`

## `_validate_repo_id` — function, line 66
- **called from:**
- `routes/cookbook_routes.py:954`
- `routes/cookbook_routes.py:3778`
- `tests/test_cookbook_helpers.py:266`
- `tests/test_cookbook_helpers.py:268`

## `_validate_serve_model_id` — function, line 72
- **called from:**
- `routes/cookbook_routes.py:950`
- `routes/cookbook_routes.py:1941`
- `tests/test_cookbook_helpers.py:272`
- `tests/test_cookbook_helpers.py:273`
- `tests/test_cookbook_helpers.py:275`

## `_validate_include` — function, line 80
- **called from:**
- `routes/cookbook_routes.py:955`

## `_validate_token` — function, line 88
- **called from:**
- `routes/cookbook_routes.py:494`
- `routes/cookbook_routes.py:960`
- `routes/cookbook_routes.py:1889`

## `load_stored_hf_token` — function, line 96
- **called from:**
- `routes/cookbook_routes.py:506`
- `src/tools/cookbook.py:336`
- `src/tools/cookbook.py:613`
- `tests/test_cookbook_hf_token.py:19`
- `tests/test_cookbook_hf_token.py:20`
- `tests/test_cookbook_hf_token.py:26`
- `tests/test_cookbook_hf_token.py:37`

## `_validate_local_dir` — function, line 114
- **called from:**
- `routes/cookbook_routes.py:958`
- `tests/test_cookbook_helpers.py:179`
- `tests/test_cookbook_helpers.py:180`
- `tests/test_cookbook_helpers.py:188`
- `tests/test_cookbook_helpers.py:189`
- `tests/test_cookbook_helpers.py:190`
- `tests/test_cookbook_helpers.py:202`
- `tests/test_cookbook_helpers.py:213`
- `tests/test_cookbook_helpers.py:226`
- `tests/test_cookbook_helpers.py:241`
- `tests/test_cookbook_helpers.py:256`

## `_validate_gpus` — function, line 133
- **called from:**
- `routes/cookbook_routes.py:1886`
- `tests/test_cookbook_helpers.py:260`
- `tests/test_cookbook_helpers.py:262`

## `_shell_path` — function, line 141
- **called from:**
- `routes/cookbook_routes.py:974`
- `tests/test_cookbook_helpers.py:181`
- `tests/test_cookbook_helpers.py:191`

## `_local_tooling_path_export` — function, line 152
- **called from:**
- `routes/cookbook_routes.py:1005`
- `routes/cookbook_routes.py:2069`
- `tests/test_cookbook_helpers.py:282`
- `tests/test_cookbook_helpers.py:288`
- `tests/test_cookbook_helpers.py:524`

## `_pip_install_no_cache` — function, line 183
- **called from:**
- `routes/cookbook_routes.py:1915`
- `tests/test_cookbook_helpers.py:945`
- `tests/test_cookbook_helpers.py:947`
- `tests/test_cookbook_helpers.py:955`
- `tests/test_cookbook_helpers.py:957`
- `tests/test_cookbook_helpers.py:958`

## `_pip_install_attempt` — function, line 198
- **called from:**
- `routes/cookbook_helpers.py:256`
- `routes/cookbook_helpers.py:257`
- `routes/cookbook_helpers.py:258`
- `tests/test_cookbook_helpers.py:469`
- `tests/test_cookbook_helpers.py:480`
- `tests/test_cookbook_helpers.py:487`
- `tests/test_cookbook_helpers.py:499`
- `tests/test_cookbook_helpers.py:511`

## `_pip_command` — function, line 217
- **called from:**
- `routes/cookbook_helpers.py:255`

## `_pip_break_system_packages_check` — function, line 227
- **called from:**
- `routes/cookbook_helpers.py:259`

## `_pip_install_fallback_chain` — function, line 231
- **called from:**
- `routes/cookbook_routes.py:1019`
- `routes/cookbook_routes.py:1024`
- `routes/cookbook_routes.py:1152`
- `routes/cookbook_routes.py:1165`
- `routes/cookbook_routes.py:2157`
- `tests/test_cookbook_helpers.py:294`
- `tests/test_cookbook_helpers.py:313`
- `tests/test_cookbook_helpers.py:325`
- `tests/test_cookbook_helpers.py:382`
- `tests/test_cookbook_helpers.py:390`

## `_venv_safe_local_pip_install_cmd` — function, line 282
- **called from:**
- `routes/cookbook_routes.py:1905`
- `tests/test_cookbook_helpers.py:438`
- `tests/test_cookbook_helpers.py:441`
- `tests/test_cookbook_helpers.py:442`

## `_pip_install_command_without_break_system_packages` — function, line 310
- **called from:**
- `routes/cookbook_helpers.py:347`
- `routes/cookbook_routes.py:2580`

## `_pip_install_help_check_from_cmd` — function, line 319
- **called from:**
- `routes/cookbook_helpers.py:346`

## `_append_pip_install_runner_lines` — function, line 334
- **called from:**
- `routes/cookbook_routes.py:2581`
- `tests/test_cookbook_helpers.py:447`
- `tests/test_cookbook_helpers.py:461`

## `_user_shell_path_bootstrap` — function, line 359
- **called from:**
- `routes/cookbook_routes.py:989`
- `routes/cookbook_routes.py:1115`
- `routes/cookbook_routes.py:2064`
- `tests/test_cookbook_helpers.py:530`

## `_cached_model_scan_script` — function, line 376
- **called from:**
- `routes/cookbook_routes.py:1298`
- `tests/test_cookbook_helpers.py:838`
- `tests/test_cookbook_helpers.py:868`
- `tests/test_cookbook_helpers.py:894`
- `tests/test_cookbook_helpers.py:925`
- `tests/test_cookbook_helpers.py:971`
- `tests/test_cookbook_stale_cache_markers.py:29`
- `tests/test_cookbook_stale_cache_markers.py:35`

## `_ps_squote` — function, line 588
- **called from:**
- `routes/cookbook_routes.py:1049`
- `routes/cookbook_routes.py:1054`
- `routes/cookbook_routes.py:1062`
- `routes/cookbook_routes.py:2002`

## `_bash_squote` — function, line 595
- **called from:**
- `routes/cookbook_helpers.py:1047`
- `routes/cookbook_helpers.py:1098`
- `routes/cookbook_routes.py:150`
- `routes/cookbook_routes.py:167`
- `routes/cookbook_routes.py:168`
- `routes/cookbook_routes.py:991`
- `routes/cookbook_routes.py:1119`
- `routes/cookbook_routes.py:2076`
- `routes/cookbook_routes.py:2173`
- `routes/cookbook_routes.py:2188`
- `routes/cookbook_routes.py:2217`
- `routes/cookbook_routes.py:2309`
- `routes/cookbook_routes.py:2333`
- `routes/cookbook_routes.py:2444`
- `routes/cookbook_routes.py:2473`
- `routes/cookbook_routes.py:2535`
- `tests/test_ollama_runner_hint.py:51`

## `_ollama_bind_from_cmd` — function, line 676
- **called from:**
- `routes/cookbook_routes.py:2164`
- `tests/test_cookbook_helpers.py:663`
- `tests/test_cookbook_helpers.py:664`
- `tests/test_cookbook_helpers.py:669`
- `tests/test_cookbook_helpers.py:676`
- `tests/test_cookbook_helpers.py:680`
- `tests/test_cookbook_helpers.py:687`
- `tests/test_cookbook_helpers.py:691`

## `_normalize_llama_cpp_python_cache_types` — function, line 705
- **called from:**
- `routes/cookbook_routes.py:1902`
- `tests/test_cookbook_helpers.py:639`
- `tests/test_cookbook_helpers.py:648`

## `repl` — function, line 710
- **called from:**
- `src/text_helpers.py:111`

## `_check_serve_binary` — function, line 721
- **called from:**
- `routes/cookbook_helpers.py:781`
- `routes/cookbook_helpers.py:797`

## `_is_safe_serve_subshell` — function, line 746
- **called from:**
- `routes/cookbook_helpers.py:790`

## `_validate_serve_cmd` — function, line 753
- **called from:**
- `routes/cookbook_routes.py:1901`
- `tests/test_cookbook_docker_access.py:267`
- `tests/test_cookbook_helpers.py:591`
- `tests/test_cookbook_helpers.py:608`
- `tests/test_cookbook_helpers.py:617`
- `tests/test_cookbook_helpers.py:630`
- `tests/test_cookbook_helpers.py:1005`
- `tests/test_cookbook_helpers.py:1014`
- `tests/test_cookbook_helpers.py:1029`
- `tests/test_cookbook_helpers.py:1043`
- `tests/test_cookbook_helpers.py:1054`

## `_replace_safe_subshell` — function, line 788
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_append_serve_preflight_exit_lines` — function, line 801
- **called from:**
- `routes/cookbook_routes.py:2557`
- `routes/cookbook_routes.py:2572`
- `tests/test_cookbook_helpers.py:552`

## `_append_vllm_linux_preflight_lines` — function, line 819
- **called from:**
- `tests/test_cookbook_helpers.py:425`

## `_append_serve_exit_code_lines` — function, line 834
- **called from:**
- `routes/cookbook_routes.py:2587`
- `routes/cookbook_routes.py:2594`
- `tests/test_cookbook_helpers.py:565`
- `tests/test_cookbook_helpers.py:576`

## `_append_llama_cpp_linux_accel_build_lines` — function, line 855
- **called from:**
- `routes/cookbook_routes.py:2131`
- `tests/test_cookbook_helpers.py:698`
- `tests/test_cookbook_helpers.py:713`
- `tests/test_cookbook_helpers.py:732`
- `tests/test_cookbook_helpers.py:742`
- `tests/test_cookbook_helpers.py:759`
- `tests/test_cookbook_helpers.py:766`

## `_append_llama_server_resolution_definition_lines` — function, line 1045
- **called from:**
- `routes/cookbook_helpers.py:1097`
- `routes/cookbook_helpers.py:1172`
- `routes/cookbook_helpers.py:1190`

## `_append_llama_server_shim_definition_lines` — function, line 1095
- **called from:**
- `routes/cookbook_routes.py:2102`
- `tests/test_cookbook_dependency_completion_regression.py:692`
- `tests/test_cookbook_dependency_completion_regression.py:710`
- `tests/test_cookbook_dependency_completion_regression.py:727`
- `tests/test_cookbook_dependency_completion_regression.py:742`
- `tests/test_cookbook_dependency_completion_regression.py:772`
- `tests/test_cookbook_dependency_completion_regression.py:990`
- `tests/test_cookbook_dependency_completion_regression.py:1008`
- `tests/test_cookbook_dependency_completion_regression.py:1267`

## `_append_llama_server_shim_reconciliation_lines` — function, line 1156
- **called from:**
- `routes/cookbook_routes.py:2103`
- `tests/test_cookbook_dependency_completion_regression.py:797`
- `tests/test_cookbook_dependency_completion_regression.py:812`
- `tests/test_cookbook_dependency_completion_regression.py:829`
- `tests/test_cookbook_dependency_completion_regression.py:843`
- `tests/test_cookbook_dependency_completion_regression.py:860`
- `tests/test_cookbook_dependency_completion_regression.py:878`
- `tests/test_cookbook_dependency_completion_regression.py:895`
- `tests/test_cookbook_dependency_completion_regression.py:926`
- `tests/test_cookbook_dependency_completion_regression.py:942`
- `tests/test_cookbook_dependency_completion_regression.py:975`
- `tests/test_cookbook_dependency_completion_regression.py:1154`
- `tests/test_cookbook_dependency_completion_regression.py:1188`
- `tests/test_cookbook_dependency_completion_regression.py:1216`
- `tests/test_cookbook_dependency_completion_regression.py:1242`
- `tests/test_cookbook_dependency_completion_regression.py:1268`

## `_append_llama_server_finalization_lines` — function, line 1177
- **called from:**
- `routes/cookbook_routes.py:2111`
- `routes/cookbook_routes.py:2159`
- `tests/test_cookbook_dependency_completion_regression.py:991`
- `tests/test_cookbook_dependency_completion_regression.py:1009`
- `tests/test_cookbook_dependency_completion_regression.py:1269`

## `_llama_cpp_rebuild_cmd` — function, line 1202
- **called from:**
- `routes/shell_routes.py:2233`
- `tests/test_cookbook_helpers.py:774`
- `tests/test_cookbook_helpers.py:812`

## `ModelDownloadRequest` — class, line 1235
- **called from:**
- `tests/test_wave3_local_control.py:245`

## `ServeRequest` — class, line 1248
- **called from:**
- `routes/codex_routes.py:705`
- `routes/codex_routes.py:856`
- `tests/test_cookbook_dependency_completion_regression.py:1107`
- `tests/test_cookbook_dependency_completion_regression.py:1332`
- `tests/test_cookbook_docker_access.py:167`
- `tests/test_cookbook_docker_access.py:230`
- `tests/test_cookbook_endpoint_registration.py:64`
- `tests/test_cookbook_endpoint_registration.py:465`
- `tests/test_cookbook_remote_windows_diffusers.py:45`
- `tests/test_cookbook_serve_lifecycle.py:181`

## `_parse_serve_phase` — function, line 1263
- **called from:**
- `routes/cookbook_routes.py:4356`
- `routes/cookbook_routes.py:4467`

## `_ssh` — function, line 1321
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_safe_env_prefix` — function, line 1327
- **called from:**
- `routes/cookbook_routes.py:1059`
- `routes/cookbook_routes.py:1125`
- `routes/cookbook_routes.py:1214`
- `routes/cookbook_routes.py:2006`
- `routes/cookbook_routes.py:2080`
- `tests/test_cookbook_helpers.py:40`
- `tests/test_cookbook_helpers.py:97`
- `tests/test_cookbook_helpers.py:102`
- `tests/test_cookbook_helpers.py:107`
- `tests/test_cookbook_helpers.py:132`

## `_local_windows_bash_env_prefix` — function, line 1380
- **called from:**
- `routes/cookbook_routes.py:1214`
- `routes/cookbook_routes.py:2080`
- `tests/test_cookbook_helpers.py:129`
- `tests/test_cookbook_helpers.py:147`
- `tests/test_cookbook_helpers.py:153`

## `_ssh_ps` — function, line 1415
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_diagnose_serve_output` — function, line 1425
- **called from:**
- `routes/cookbook_routes.py:4471`
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
- `tests/test_cookbook_error_feedback.py:93`
- `tests/test_cookbook_error_feedback.py:107`
- `tests/test_cookbook_error_feedback.py:120`

## `run_ssh_command_async` — function (async), line 1635
- **called from:**
- `routes/cookbook_routes.py:845`
- `tests/test_cookbook_helpers.py:65`
