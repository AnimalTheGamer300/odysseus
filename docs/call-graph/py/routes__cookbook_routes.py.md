# `routes/cookbook_routes.py` — definitions & call sites

94 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_windows_local_pid_record_line` — function, line 78
- **called from:**
- `routes/cookbook_routes.py:889`
- `tests/test_cookbook_local_serve_pid_winpid.py:38`
- `tests/test_cookbook_local_serve_pid_winpid.py:93`

## `_append_mlx_image_server_script` — function, line 102
- **called from:**
- `routes/cookbook_routes.py:2442`

## `_normalize_runtime_adapter` — function, line 119
- **called from:**
- `routes/cookbook_routes.py:1887`

## `_venv_root_from_serve_cmd` — function, line 129
- **called from:**
- `routes/cookbook_routes.py:149`

## `_append_venv_nvidia_library_path_lines` — function, line 141
- **called from:**
- `routes/cookbook_routes.py:2083`

## `_serve_port_from_cmd` — function, line 158
- **called from:**
- `routes/cookbook_routes.py:164`

## `_append_openai_port_preflight_lines` — function, line 163
- **called from:**
- `routes/cookbook_routes.py:2085`

## `_is_generated_ollama_docker_exec_cmd` — function, line 200
- **called from:**
- `routes/cookbook_routes.py:1893`
- `tests/test_cookbook_docker_access.py:264`
- `tests/test_cookbook_docker_access.py:273`
- `tests/test_cookbook_docker_access.py:276`
- `tests/test_cookbook_docker_access.py:279`
- `tests/test_cookbook_docker_access.py:285`

## `_missing_binary_message` — function, line 235
- **called from:**
- `routes/cookbook_routes.py:1038`
- `routes/cookbook_routes.py:1976`
- `routes/cookbook_routes.py:1987`
- `tests/test_cookbook_docker_access.py:58`

## `_remote_binary_available` — function (async), line 256
- **called from:**
- `routes/cookbook_routes.py:338`

## `_remote_posix_path_prefix` — function, line 288
- **called from:**
- `routes/cookbook_routes.py:303`
- `routes/cookbook_routes.py:320`

## `_remote_tmux_command` — function, line 292
- **called from:**
- `routes/cookbook_routes.py:1587`
- `routes/cookbook_routes.py:3627`
- `routes/cookbook_routes.py:3640`
- `routes/cookbook_routes.py:4301`
- `routes/cookbook_routes.py:4309`

## `_remote_tmux_launch_command` — function, line 306
- **called from:**
- `routes/cookbook_routes.py:1208`
- `routes/cookbook_routes.py:2630`

## `_binary_available` — function (async), line 327
- **called from:**
- `routes/cookbook_routes.py:1035`
- `routes/cookbook_routes.py:1973`
- `routes/cookbook_routes.py:1979`
- `tests/test_cookbook_docker_access.py:48`
- `tests/test_cookbook_docker_access.py:73`
- `tests/test_cookbook_docker_access.py:89`
- `tests/test_cookbook_docker_access.py:111`

## `_local_ollama_docker_fallback_available` — function, line 356
- **called from:**
- `routes/cookbook_routes.py:379`
- `routes/cookbook_routes.py:1015`

## `_local_ollama_docker_access_blocked` — function, line 370
- **called from:**
- `routes/cookbook_routes.py:1016`
- `tests/test_cookbook_docker_access.py:293`
- `tests/test_cookbook_docker_access.py:303`

## `_append_local_ollama_download_command_lines` — function, line 386
- **called from:**
- `routes/cookbook_routes.py:1012`
- `tests/test_cookbook_docker_access.py:313`
- `tests/test_cookbook_docker_access.py:333`

## `setup_cookbook_routes` — function, line 409
- **called from:**
- `app.py:888`
- `tests/test_cookbook_cache_scan_isolation.py:19`
- `tests/test_cookbook_cache_scan_isolation.py:56`
- `tests/test_cookbook_cache_scan_isolation.py:71`
- `tests/test_cookbook_dependency_completion_regression.py:1087`
- `tests/test_cookbook_dependency_completion_regression.py:1313`
- `tests/test_cookbook_docker_access.py:21`
- `tests/test_cookbook_endpoint_registration.py:56`
- `tests/test_cookbook_endpoint_registration.py:223`
- `tests/test_cookbook_endpoint_registration.py:457`
- `tests/test_cookbook_hf_gguf_files.py:11`
- `tests/test_cookbook_remote_windows_diffusers.py:12`
- `tests/test_cookbook_serve_lifecycle.py:162`
- `tests/test_runtime_resource_integration.py:332`
- `tests/test_wave3_local_control.py:103`
- `tests/test_wave3_local_control.py:240`

## `protect_native_control` — function (async), line 410
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `protect_local_model_producer` — function, line 432
- **called from:**
- `routes/cookbook_routes.py:943`
- `routes/cookbook_routes.py:1881`

## `_mask_secret` — function, line 443
- **called from:**
- `routes/cookbook_routes.py:482`

## `_client_host_platform` — function, line 450
- **called from:**
- `routes/cookbook_routes.py:483`

## `_decrypt_secret` — function, line 453
- **called from:**
- `routes/cookbook_routes.py:479`
- `src/webhook_manager.py:384`
- `src/webhook_manager.py:389`

## `_encrypt_secret` — function, line 459
- **called from:**
- `routes/cookbook_routes.py:495`

## `_strip_task_secrets` — function, line 463
- **called from:**
- `routes/cookbook_routes.py:473`
- `routes/cookbook_routes.py:488`

## `_state_for_client` — function, line 471
- **called from:**
- `routes/cookbook_routes.py:3263`
- `routes/cookbook_routes.py:3267`
- `routes/cookbook_routes.py:3270`
- `routes/cookbook_routes.py:3389`

## `_state_for_storage` — function, line 486
- **called from:**
- `routes/cookbook_routes.py:3380`

## `_load_stored_hf_token` — function, line 505
- **called from:**
- `routes/cookbook_routes.py:959`
- `routes/cookbook_routes.py:1888`
- `routes/cookbook_routes.py:3782`

## `_normalize_minimax_m3_vllm_cmd` — function, line 508
- **called from:**
- `routes/cookbook_routes.py:1903`

## `add_env` — function, line 549
- **called from:**
- `routes/cookbook_routes.py:573`
- `routes/cookbook_routes.py:574`
- `routes/cookbook_routes.py:649`

## `has_flag` — function, line 553
- **called from:**
- `routes/cookbook_routes.py:570`
- `routes/cookbook_routes.py:659`
- `routes/cookbook_routes.py:661`
- `routes/cookbook_routes.py:663`

## `set_flag` — function, line 556
- **called from:**
- `routes/cookbook_routes.py:575`
- `routes/cookbook_routes.py:576`
- `routes/cookbook_routes.py:577`
- `routes/cookbook_routes.py:578`
- `routes/cookbook_routes.py:579`
- `routes/cookbook_routes.py:658`
- `routes/cookbook_routes.py:660`
- `routes/cookbook_routes.py:662`
- `routes/cookbook_routes.py:665`

## `add_bool` — function, line 569
- **called from:**
- `routes/cookbook_routes.py:580`
- `routes/cookbook_routes.py:581`
- `routes/cookbook_routes.py:582`

## `_normalize_deepseek_v4_sglang_cmd` — function, line 585
- **called from:**
- `routes/cookbook_routes.py:1904`

## `add_env` — function, line 609
- **called from:**
- `routes/cookbook_routes.py:573`
- `routes/cookbook_routes.py:574`
- `routes/cookbook_routes.py:649`

## `has_flag` — function, line 613
- **called from:**
- `routes/cookbook_routes.py:570`
- `routes/cookbook_routes.py:659`
- `routes/cookbook_routes.py:661`
- `routes/cookbook_routes.py:663`

## `flag_value` — function, line 616
- **called from:**
- `routes/cookbook_routes.py:650`

## `set_flag` — function, line 624
- **called from:**
- `routes/cookbook_routes.py:575`
- `routes/cookbook_routes.py:576`
- `routes/cookbook_routes.py:577`
- `routes/cookbook_routes.py:578`
- `routes/cookbook_routes.py:579`
- `routes/cookbook_routes.py:658`
- `routes/cookbook_routes.py:660`
- `routes/cookbook_routes.py:662`
- `routes/cookbook_routes.py:665`

## `remove_flag` — function, line 637
- **called from:**
- `routes/cookbook_routes.py:664`

## `_cookbook_ssh_dir` — function, line 668
- **called from:**
- `routes/cookbook_routes.py:679`
- `routes/cookbook_routes.py:710`
- `routes/cookbook_routes.py:811`

## `_cookbook_ssh_key_path` — function, line 678
- **called from:**
- `routes/cookbook_routes.py:757`
- `routes/cookbook_routes.py:812`

## `_ssh_known_host_name` — function, line 681
- **called from:**
- `routes/cookbook_routes.py:690`
- `routes/cookbook_routes.py:734`

## `_known_hosts_targets` — function, line 689
- **called from:**
- `routes/cookbook_routes.py:718`

## `_ssh_host_key_changed` — function, line 696
- **called from:**
- `routes/cookbook_routes.py:1357`

## `_repair_cookbook_known_host` — function (async), line 703
- **called from:**
- `routes/cookbook_routes.py:1358`

## `_read_cookbook_public_key` — function, line 756
- **called from:**
- `routes/cookbook_routes.py:802`
- `routes/cookbook_routes.py:832`

## `_server_env_prefix_for_download` — function, line 762
- **called from:**
- `routes/cookbook_routes.py:962`

## `get_cookbook_ssh_key` — function (async), line 800
- **route:** `GET /api/cookbook/ssh-key`
- decorator: `router.get("/api/cookbook/ssh-key")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `generate_cookbook_ssh_key` — function (async), line 809
- **route:** `POST /api/cookbook/ssh-key`
- decorator: `router.post("/api/cookbook/ssh-key")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CookbookSshTestRequest` — class, line 834
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_cookbook_ssh` — function (async), line 839
- **route:** `POST /api/cookbook/test-ssh`
- decorator: `router.post("/api/cookbook/test-ssh")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_needs_binary` — function, line 863
- **called from:**
- `routes/cookbook_routes.py:1979`

## `_launch_local_detached` — function, line 866
- **called from:**
- `routes/cookbook_routes.py:1248`
- `routes/cookbook_routes.py:2638`

## `model_download` — function (async), line 939
- **route:** `POST /api/model/download`
- decorator: `router.post("/api/model/download")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `model_cached` — function (async), line 1281
- **route:** `GET /api/model/cached`
- decorator: `router.get("/api/model/cached")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_run_cached_scan_once` — function (async), line 1300
- **called from:**
- `routes/cookbook_routes.py:1354`
- `routes/cookbook_routes.py:1361`

## `_auto_register_image_endpoint` — function, line 1411
- **called from:**
- `routes/cookbook_routes.py:2661`

## `_pick_free_port_for_ollama` — function, line 1495
- **called from:**
- `routes/cookbook_routes.py:1959`

## `_serve_crash_watchdog` — function (async), line 1549
- **called from:**
- `routes/cookbook_routes.py:2685`

## `_auto_register_llm_endpoint` — function, line 1683
- **called from:**
- `routes/cookbook_routes.py:2667`

## `model_serve` — function (async), line 1871
- **route:** `POST /api/model/serve`
- decorator: `router.post("/api/model/serve")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SetupRequest` — class, line 2712
- **called from:**
- `tests/test_auth_policy.py:154`
- `tests/test_auth_policy.py:201`
- `tests/test_auth_policy.py:212`
- `tests/test_auth_username_policy.py:35`

## `server_setup` — function (async), line 2717
- **route:** `POST /api/cookbook/setup`
- decorator: `router.post("/api/cookbook/setup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_run_nvidia_smi` — function (async), line 2807
- **called from:**
- `routes/cookbook_routes.py:3045`
- `routes/cookbook_routes.py:3084`

## `_run_gpu_shell` — function (async), line 2830
- **called from:**
- `routes/cookbook_routes.py:2860`
- `routes/cookbook_routes.py:2873`
- `routes/cookbook_routes.py:2886`
- `routes/cookbook_routes.py:2892`
- `routes/cookbook_routes.py:2901`
- `routes/cookbook_routes.py:2980`

## `_gpu_read_file` — function (async), line 2859
- **called from:**
- `routes/cookbook_routes.py:2919`
- `routes/cookbook_routes.py:2922`
- `routes/cookbook_routes.py:2923`
- `routes/cookbook_routes.py:2924`
- `routes/cookbook_routes.py:2937`
- `routes/cookbook_routes.py:2939`
- `routes/cookbook_routes.py:2941`
- `routes/cookbook_routes.py:2950`

## `_probe_gpu_device_processes` — function (async), line 2865
- **called from:**
- `routes/cookbook_routes.py:2961`
- `routes/cookbook_routes.py:3171`

## `_probe_amd_sysfs` — function (async), line 2891
- **called from:**
- `routes/cookbook_routes.py:3155`

## `_probe_apple_unified_memory` — function (async), line 2967
- **called from:**
- `routes/cookbook_routes.py:3149`

## `list_gpus` — function (async), line 3021
- **route:** `GET /api/cookbook/gpus`
- decorator: `router.get("/api/cookbook/gpus")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `KillPidRequest` — class, line 3189
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `kill_pid` — function (async), line 3196
- **route:** `POST /api/cookbook/kill-pid`
- decorator: `router.post("/api/cookbook/kill-pid")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_cookbook_state` — function (async), line 3247
- **route:** `GET /api/cookbook/state`
- decorator: `router.get("/api/cookbook/state")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `save_cookbook_state` — function (async), line 3275
- **route:** `POST /api/cookbook/state`
- decorator: `router.post("/api/cookbook/state")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `hf_latest` — function (async), line 3398
- **route:** `GET /api/cookbook/hf-latest`
- decorator: `router.get("/api/cookbook/hf-latest")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_est_vram_fp16` — function, line 3432
- **called from:**
- `routes/cookbook_routes.py:3507`

## `_quant_factor` — function, line 3440
- **called from:**
- `routes/cookbook_routes.py:3508`

## `_is_excluded` — function, line 3465
- **called from:**
- `routes/cookbook_routes.py:3502`

## `_is_official` — function, line 3485
- **called from:**
- `routes/cookbook_routes.py:3504`

## `_maybe_sweep_orphans` — function, line 3548
- **called from:**
- `routes/cookbook_routes.py:4233`

## `_run_sweep` — function, line 3576
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_sync_sweep_orphans` — function, line 3590
- **called from:**
- `routes/cookbook_routes.py:3578`

## `hf_gguf_files` — function (async), line 3774
- **route:** `GET /api/cookbook/hf-gguf-files`
- decorator: `router.get("/api/cookbook/hf-gguf-files")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ollama_library` — function (async), line 3840
- **route:** `GET /api/cookbook/ollama/library`
- decorator: `router.get("/api/cookbook/ollama/library")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `vllm_recipe_manifest` — function (async), line 3927
- **route:** `GET /api/cookbook/vllm-recipe-manifest`
- decorator: `router.get("/api/cookbook/vllm-recipe-manifest")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_fetch_sync` — function, line 3944
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `vllm_recipe` — function (async), line 3987
- **route:** `GET /api/cookbook/vllm-recipe`
- decorator: `router.get("/api/cookbook/vllm-recipe")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_fetch_sync` — function, line 4010
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cookbook_tasks_status` — function (async), line 4103
- **route:** `GET /api/cookbook/tasks/status`
- decorator: `router.get("/api/cookbook/tasks/status")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_compute` — function (async), line 4119
- **called from:**
- `routes/cookbook_routes.py:4124`

## `_cookbook_tasks_status_sync` — function, line 4132
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_pick_download_progress` — function, line 4135
- **called from:**
- `routes/cookbook_routes.py:4342`
- `routes/cookbook_routes.py:4382`

## `_download_cache_complete` — function, line 4157
- **called from:**
- `routes/cookbook_routes.py:4456`

## `_download_cache_incomplete` — function, line 4184
- **called from:**
- `routes/cookbook_routes.py:4400`
