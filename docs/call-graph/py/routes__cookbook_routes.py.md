# `routes/cookbook_routes.py` — definitions & call sites

91 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_windows_local_pid_record_line` — function, line 76
- **called from:**
- `routes/cookbook_routes.py:1015`
- `tests/test_cookbook_local_serve_pid_winpid.py:38`
- `tests/test_cookbook_local_serve_pid_winpid.py:93`

## `_append_mlx_image_server_script` — function, line 100
- **called from:**
- `routes/cookbook_routes.py:2574`

## `_venv_root_from_serve_cmd` — function, line 117
- **called from:**
- `routes/cookbook_routes.py:137`

## `_append_venv_nvidia_library_path_lines` — function, line 129
- **called from:**
- `routes/cookbook_routes.py:2172`

## `_serve_port_from_cmd` — function, line 146
- **called from:**
- `routes/cookbook_routes.py:152`

## `_append_openai_port_preflight_lines` — function, line 151
- **called from:**
- `routes/cookbook_routes.py:2174`

## `_is_generated_ollama_docker_exec_cmd` — function, line 188
- **called from:**
- `routes/cookbook_routes.py:1982`
- `tests/test_cookbook_docker_access.py:259`
- `tests/test_cookbook_docker_access.py:268`
- `tests/test_cookbook_docker_access.py:271`
- `tests/test_cookbook_docker_access.py:274`
- `tests/test_cookbook_docker_access.py:280`

## `_missing_binary_message` — function, line 223
- **called from:**
- `routes/cookbook_routes.py:1163`
- `routes/cookbook_routes.py:2065`
- `routes/cookbook_routes.py:2076`
- `tests/test_cookbook_docker_access.py:50`

## `_remote_binary_available` — function (async), line 244
- **called from:**
- `routes/cookbook_routes.py:326`

## `_remote_posix_path_prefix` — function, line 276
- **called from:**
- `routes/cookbook_routes.py:291`
- `routes/cookbook_routes.py:308`

## `_remote_tmux_command` — function, line 280
- **called from:**
- `routes/cookbook_routes.py:1687`
- `routes/cookbook_routes.py:3721`
- `routes/cookbook_routes.py:3734`
- `routes/cookbook_routes.py:4394`
- `routes/cookbook_routes.py:4400`

## `_remote_tmux_launch_command` — function, line 294
- **called from:**
- `routes/cookbook_routes.py:1333`
- `routes/cookbook_routes.py:2759`

## `_binary_available` — function (async), line 315
- **called from:**
- `routes/cookbook_routes.py:1160`
- `routes/cookbook_routes.py:2062`
- `routes/cookbook_routes.py:2068`
- `tests/test_cookbook_docker_access.py:40`
- `tests/test_cookbook_docker_access.py:66`
- `tests/test_cookbook_docker_access.py:82`
- `tests/test_cookbook_docker_access.py:104`

## `_local_ollama_docker_fallback_available` — function, line 344
- **called from:**
- `routes/cookbook_routes.py:367`
- `routes/cookbook_routes.py:1140`

## `_local_ollama_docker_access_blocked` — function, line 358
- **called from:**
- `routes/cookbook_routes.py:1141`
- `tests/test_cookbook_docker_access.py:288`
- `tests/test_cookbook_docker_access.py:298`

## `_append_local_ollama_download_command_lines` — function, line 374
- **called from:**
- `routes/cookbook_routes.py:1137`
- `tests/test_cookbook_docker_access.py:308`
- `tests/test_cookbook_docker_access.py:328`

## `setup_cookbook_routes` — function, line 397
- **called from:**
- `app.py:804`
- `tests/test_cookbook_docker_access.py:15`
- `tests/test_cookbook_remote_windows_diffusers.py:12`

## `_mask_secret` — function, line 404
- **called from:**
- `routes/cookbook_routes.py:612`

## `_client_host_platform` — function, line 411
- **called from:**
- `routes/cookbook_routes.py:613`

## `_decrypt_secret` — function, line 414
- **called from:**
- `routes/cookbook_routes.py:609`
- `src/webhook_manager.py:384`
- `src/webhook_manager.py:389`

## `_encrypt_secret` — function, line 420
- **called from:**
- `routes/cookbook_routes.py:625`

## `_strip_task_secrets` — function, line 424
- **called from:**
- `routes/cookbook_routes.py:603`
- `routes/cookbook_routes.py:618`

## `_diagnose_serve_output` — function, line 432
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

## `_state_for_client` — function, line 601
- **called from:**
- `routes/cookbook_routes.py:3384`
- `routes/cookbook_routes.py:3388`
- `routes/cookbook_routes.py:3391`
- `routes/cookbook_routes.py:3510`

## `_state_for_storage` — function, line 616
- **called from:**
- `routes/cookbook_routes.py:3501`

## `_load_stored_hf_token` — function, line 635
- **called from:**
- `routes/cookbook_routes.py:1084`
- `routes/cookbook_routes.py:1977`
- `routes/cookbook_routes.py:3876`

## `_normalize_minimax_m3_vllm_cmd` — function, line 638
- **called from:**
- `routes/cookbook_routes.py:1992`

## `add_env` — function, line 675
- **called from:**
- `routes/cookbook_routes.py:699`
- `routes/cookbook_routes.py:700`
- `routes/cookbook_routes.py:775`

## `has_flag` — function, line 679
- **called from:**
- `routes/cookbook_routes.py:696`
- `routes/cookbook_routes.py:785`
- `routes/cookbook_routes.py:787`
- `routes/cookbook_routes.py:789`

## `set_flag` — function, line 682
- **called from:**
- `routes/cookbook_routes.py:701`
- `routes/cookbook_routes.py:702`
- `routes/cookbook_routes.py:703`
- `routes/cookbook_routes.py:704`
- `routes/cookbook_routes.py:705`
- `routes/cookbook_routes.py:784`
- `routes/cookbook_routes.py:786`
- `routes/cookbook_routes.py:788`
- `routes/cookbook_routes.py:791`

## `add_bool` — function, line 695
- **called from:**
- `routes/cookbook_routes.py:706`
- `routes/cookbook_routes.py:707`
- `routes/cookbook_routes.py:708`

## `_normalize_deepseek_v4_sglang_cmd` — function, line 711
- **called from:**
- `routes/cookbook_routes.py:1993`

## `add_env` — function, line 735
- **called from:**
- `routes/cookbook_routes.py:699`
- `routes/cookbook_routes.py:700`
- `routes/cookbook_routes.py:775`

## `has_flag` — function, line 739
- **called from:**
- `routes/cookbook_routes.py:696`
- `routes/cookbook_routes.py:785`
- `routes/cookbook_routes.py:787`
- `routes/cookbook_routes.py:789`

## `flag_value` — function, line 742
- **called from:**
- `routes/cookbook_routes.py:776`

## `set_flag` — function, line 750
- **called from:**
- `routes/cookbook_routes.py:701`
- `routes/cookbook_routes.py:702`
- `routes/cookbook_routes.py:703`
- `routes/cookbook_routes.py:704`
- `routes/cookbook_routes.py:705`
- `routes/cookbook_routes.py:784`
- `routes/cookbook_routes.py:786`
- `routes/cookbook_routes.py:788`
- `routes/cookbook_routes.py:791`

## `remove_flag` — function, line 763
- **called from:**
- `routes/cookbook_routes.py:790`

## `_cookbook_ssh_dir` — function, line 794
- **called from:**
- `routes/cookbook_routes.py:805`
- `routes/cookbook_routes.py:836`
- `routes/cookbook_routes.py:937`

## `_cookbook_ssh_key_path` — function, line 804
- **called from:**
- `routes/cookbook_routes.py:883`
- `routes/cookbook_routes.py:938`

## `_ssh_known_host_name` — function, line 807
- **called from:**
- `routes/cookbook_routes.py:816`
- `routes/cookbook_routes.py:860`

## `_known_hosts_targets` — function, line 815
- **called from:**
- `routes/cookbook_routes.py:844`

## `_ssh_host_key_changed` — function, line 822
- **called from:**
- `routes/cookbook_routes.py:1467`

## `_repair_cookbook_known_host` — function (async), line 829
- **called from:**
- `routes/cookbook_routes.py:1468`

## `_read_cookbook_public_key` — function, line 882
- **called from:**
- `routes/cookbook_routes.py:928`
- `routes/cookbook_routes.py:958`

## `_server_env_prefix_for_download` — function, line 888
- **called from:**
- `routes/cookbook_routes.py:1087`

## `get_cookbook_ssh_key` — function (async), line 926
- **route:** `GET /api/cookbook/ssh-key`
- decorator: `router.get("/api/cookbook/ssh-key")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `generate_cookbook_ssh_key` — function (async), line 935
- **route:** `POST /api/cookbook/ssh-key`
- decorator: `router.post("/api/cookbook/ssh-key")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CookbookSshTestRequest` — class, line 960
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_cookbook_ssh` — function (async), line 965
- **route:** `POST /api/cookbook/test-ssh`
- decorator: `router.post("/api/cookbook/test-ssh")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_needs_binary` — function, line 989
- **called from:**
- `routes/cookbook_routes.py:2068`

## `_launch_local_detached` — function, line 992
- **called from:**
- `routes/cookbook_routes.py:1373`
- `routes/cookbook_routes.py:2767`

## `model_download` — function (async), line 1065
- **route:** `POST /api/model/download`
- decorator: `router.post("/api/model/download")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `model_cached` — function (async), line 1406
- **route:** `GET /api/model/cached`
- decorator: `router.get("/api/model/cached")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_run_cached_scan_once` — function (async), line 1429
- **called from:**
- `routes/cookbook_routes.py:1464`
- `routes/cookbook_routes.py:1471`

## `_auto_register_image_endpoint` — function, line 1521
- **called from:**
- `routes/cookbook_routes.py:2790`

## `_pick_free_port_for_ollama` — function, line 1595
- **called from:**
- `routes/cookbook_routes.py:2048`

## `_serve_crash_watchdog` — function (async), line 1649
- **called from:**
- `routes/cookbook_routes.py:2806`

## `_auto_register_llm_endpoint` — function, line 1759
- **called from:**
- `routes/cookbook_routes.py:2792`

## `model_serve` — function (async), line 1962
- **route:** `POST /api/model/serve`
- decorator: `router.post("/api/model/serve")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SetupRequest` — class, line 2833
- **called from:**
- `tests/test_auth_policy.py:154`
- `tests/test_auth_policy.py:201`
- `tests/test_auth_policy.py:212`

## `server_setup` — function (async), line 2838
- **route:** `POST /api/cookbook/setup`
- decorator: `router.post("/api/cookbook/setup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_run_nvidia_smi` — function (async), line 2928
- **called from:**
- `routes/cookbook_routes.py:3166`
- `routes/cookbook_routes.py:3205`

## `_run_gpu_shell` — function (async), line 2951
- **called from:**
- `routes/cookbook_routes.py:2981`
- `routes/cookbook_routes.py:2994`
- `routes/cookbook_routes.py:3007`
- `routes/cookbook_routes.py:3013`
- `routes/cookbook_routes.py:3022`
- `routes/cookbook_routes.py:3101`

## `_gpu_read_file` — function (async), line 2980
- **called from:**
- `routes/cookbook_routes.py:3040`
- `routes/cookbook_routes.py:3043`
- `routes/cookbook_routes.py:3044`
- `routes/cookbook_routes.py:3045`
- `routes/cookbook_routes.py:3058`
- `routes/cookbook_routes.py:3060`
- `routes/cookbook_routes.py:3062`
- `routes/cookbook_routes.py:3071`

## `_probe_gpu_device_processes` — function (async), line 2986
- **called from:**
- `routes/cookbook_routes.py:3082`
- `routes/cookbook_routes.py:3292`

## `_probe_amd_sysfs` — function (async), line 3012
- **called from:**
- `routes/cookbook_routes.py:3276`

## `_probe_apple_unified_memory` — function (async), line 3088
- **called from:**
- `routes/cookbook_routes.py:3270`

## `list_gpus` — function (async), line 3142
- **route:** `GET /api/cookbook/gpus`
- decorator: `router.get("/api/cookbook/gpus")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `KillPidRequest` — class, line 3310
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `kill_pid` — function (async), line 3317
- **route:** `POST /api/cookbook/kill-pid`
- decorator: `router.post("/api/cookbook/kill-pid")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_cookbook_state` — function (async), line 3368
- **route:** `GET /api/cookbook/state`
- decorator: `router.get("/api/cookbook/state")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `save_cookbook_state` — function (async), line 3396
- **route:** `POST /api/cookbook/state`
- decorator: `router.post("/api/cookbook/state")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `hf_latest` — function (async), line 3519
- **route:** `GET /api/cookbook/hf-latest`
- decorator: `router.get("/api/cookbook/hf-latest")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_est_vram_fp16` — function, line 3546
- **called from:**
- `routes/cookbook_routes.py:3605`

## `_quant_factor` — function, line 3554
- **called from:**
- `routes/cookbook_routes.py:3606`

## `_is_excluded` — function, line 3579
- **called from:**
- `routes/cookbook_routes.py:3602`

## `_maybe_sweep_orphans` — function, line 3642
- **called from:**
- `routes/cookbook_routes.py:4326`

## `_run_sweep` — function, line 3670
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_sync_sweep_orphans` — function, line 3684
- **called from:**
- `routes/cookbook_routes.py:3672`

## `hf_gguf_files` — function (async), line 3868
- **route:** `GET /api/cookbook/hf-gguf-files`
- decorator: `router.get("/api/cookbook/hf-gguf-files")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ollama_library` — function (async), line 3934
- **route:** `GET /api/cookbook/ollama/library`
- decorator: `router.get("/api/cookbook/ollama/library")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `vllm_recipe_manifest` — function (async), line 4021
- **route:** `GET /api/cookbook/vllm-recipe-manifest`
- decorator: `router.get("/api/cookbook/vllm-recipe-manifest")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_fetch_sync` — function, line 4038
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `vllm_recipe` — function (async), line 4081
- **route:** `GET /api/cookbook/vllm-recipe`
- decorator: `router.get("/api/cookbook/vllm-recipe")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_fetch_sync` — function, line 4104
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cookbook_tasks_status` — function (async), line 4197
- **route:** `GET /api/cookbook/tasks/status`
- decorator: `router.get("/api/cookbook/tasks/status")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_compute` — function (async), line 4213
- **called from:**
- `routes/cookbook_routes.py:4218`

## `_cookbook_tasks_status_sync` — function, line 4226
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_pick_download_progress` — function, line 4229
- **called from:**
- `routes/cookbook_routes.py:4432`
- `routes/cookbook_routes.py:4471`

## `_download_cache_complete` — function, line 4251
- **called from:**
- `routes/cookbook_routes.py:4542`

## `_download_cache_incomplete` — function, line 4278
- **called from:**
- `routes/cookbook_routes.py:4489`
