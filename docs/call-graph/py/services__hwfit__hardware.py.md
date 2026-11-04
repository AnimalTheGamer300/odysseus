# `services/hwfit/hardware.py` — definitions & call sites

28 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_run` — function, line 27
- **called from:**
- `services/hwfit/hardware.py:87`
- `services/hwfit/hardware.py:94`
- `services/hwfit/hardware.py:108`
- `services/hwfit/hardware.py:110`
- `services/hwfit/hardware.py:211`
- `services/hwfit/hardware.py:221`
- `services/hwfit/hardware.py:237`
- `services/hwfit/hardware.py:237`
- `services/hwfit/hardware.py:293`
- `services/hwfit/hardware.py:293`
- `services/hwfit/hardware.py:294`
- `services/hwfit/hardware.py:323`
- `services/hwfit/hardware.py:325`
- `services/hwfit/hardware.py:338`
- `services/hwfit/hardware.py:341`
- `services/hwfit/hardware.py:376`
- `services/hwfit/hardware.py:378`
- `services/hwfit/hardware.py:393`
- `services/hwfit/hardware.py:422`
- `services/hwfit/hardware.py:466`
- `services/hwfit/hardware.py:491`
- `services/hwfit/hardware.py:503`
- `services/hwfit/hardware.py:503`
- `services/hwfit/hardware.py:531`
- `services/hwfit/hardware.py:549`
- `services/hwfit/hardware.py:554`
- `services/hwfit/hardware.py:557`
- `services/hwfit/hardware.py:562`
- `services/hwfit/hardware.py:635`
- `services/research/research_handler.py:102`
- `services/search/providers.py:198`
- `services/search/providers.py:217`
- `services/search/providers.py:226`
- `services/search/providers.py:234`
- `src/research_handler.py:403`
- `tests/test_agent_rounds_exhausted.py:18`
- `tests/test_app_config_shared_fetch_js.py:89`
- `tests/test_app_config_shared_fetch_js.py:107`
- `tests/test_app_config_shared_fetch_js.py:125`
- `tests/test_app_config_shared_fetch_js.py:144`
- `tests/test_app_config_shared_fetch_js.py:163`
- `tests/test_app_config_shared_fetch_js.py:188`
- `tests/test_app_config_shared_fetch_js.py:277`
- `tests/test_app_config_shared_fetch_js.py:322`
- `tests/test_ask_user_persistence.py:22`
- `tests/test_ask_user_tool.py:31`
- `tests/test_ask_user_tool.py:48`
- `tests/test_ask_user_tool.py:55`
- `tests/test_ask_user_tool.py:65`
- `tests/test_ask_user_tool.py:71`
- `tests/test_ask_user_tool.py:78`
- `tests/test_bg_job_tools.py:90`
- `tests/test_bg_job_tools.py:96`
- `tests/test_bg_job_tools.py:102`
- `tests/test_bg_job_tools.py:108`
- `tests/test_bg_job_tools.py:114`
- `tests/test_bg_job_tools.py:122`
- `tests/test_bg_job_tools.py:128`
- `tests/test_bg_job_tools.py:132`
- `tests/test_bg_job_tools.py:138`
- … +122 more (grep the name in repo)

## `_group_gpus` — function, line 53
- **called from:**
- `services/hwfit/hardware.py:159`
- `services/hwfit/hardware.py:166`
- `services/hwfit/hardware.py:272`
- `services/hwfit/hardware.py:407`

## `_detect_nvidia` — function, line 84
- **called from:**
- `services/hwfit/hardware.py:862`
- `tests/test_hwfit_unified_nvidia.py:27`
- `tests/test_hwfit_unified_nvidia.py:54`
- `tests/test_hwfit_unified_nvidia.py:64`
- `tests/test_hwfit_unified_nvidia.py:73`

## `classify_amd_gfx` — function, line 178
- **called from:**
- `services/hwfit/hardware.py:239`
- `tests/test_hwfit_amd.py:86`

## `_detect_amd` — function, line 205
- **called from:**
- `services/hwfit/hardware.py:862`
- `tests/test_hwfit_amd.py:120`

## `_read` — function, line 209
- **called from:**
- `services/hwfit/hardware.py:246`
- `services/hwfit/hardware.py:253`
- `services/hwfit/hardware.py:254`
- `services/hwfit/hardware.py:255`
- `services/hwfit/hardware.py:266`
- `tests/test_cookbook_dependency_completion_regression.py:12`
- `tests/test_cookbook_dependency_completion_regression.py:20`
- `tests/test_cookbook_dependency_completion_regression.py:34`
- `tests/test_cookbook_dependency_completion_regression.py:49`
- `tests/test_cookbook_dependency_completion_regression.py:60`
- `tests/test_cookbook_dependency_completion_regression.py:78`
- `tests/test_cookbook_dependency_completion_regression.py:92`
- `tests/test_cookbook_dependency_completion_regression.py:102`
- `tests/test_cookbook_dependency_completion_regression.py:108`

## `_list_drm_cards` — function, line 219
- **called from:**
- `services/hwfit/hardware.py:244`

## `_amd_arch` — function, line 230
- **called from:**
- `services/hwfit/hardware.py:273`

## `_detect_apple_silicon` — function, line 309
- **called from:**
- `services/hwfit/hardware.py:862`
- `tests/test_hwfit_macos.py:114`
- `tests/test_hwfit_macos.py:134`
- `tests/test_hwfit_macos.py:145`
- `tests/test_hwfit_macos.py:156`
- `tests/test_hwfit_macos.py:165`
- `tests/test_hwfit_macos.py:174`

## `_parse_apple_gpu_cores` — function, line 349
- **called from:**
- `services/hwfit/hardware.py:376`
- `services/hwfit/hardware.py:378`

## `_read_file` — function, line 419
- **called from:**
- `services/hwfit/hardware.py:432`
- `services/hwfit/hardware.py:483`
- `services/hwfit/hardware.py:510`

## `_parse_meminfo` — function, line 430
- **called from:**
- `services/hwfit/hardware.py:449`
- `services/hwfit/hardware.py:476`

## `_get_ram_gb` — function, line 448
- **called from:**
- `services/hwfit/hardware.py:152`
- `services/hwfit/hardware.py:479`
- `services/hwfit/hardware.py:849`

## `_get_available_ram_gb` — function, line 475
- **called from:**
- `services/hwfit/hardware.py:857`

## `_get_cpu_name` — function, line 482
- **called from:**
- `services/hwfit/hardware.py:859`

## `_get_cpu_count` — function, line 500
- **called from:**
- `services/hwfit/hardware.py:858`

## `_canonical_cpu_arch` — function, line 516
- **called from:**
- `services/hwfit/hardware.py:333`
- `services/hwfit/hardware.py:531`
- `services/hwfit/hardware.py:532`
- `services/hwfit/hardware.py:657`

## `_get_cpu_arch` — function, line 529
- **called from:**
- `services/hwfit/hardware.py:860`

## `_powershell_exe` — function, line 535
- **called from:**
- `services/hwfit/hardware.py:635`

## `_powershell_encoded_for_ssh` — function, line 541
- **called from:**
- `services/hwfit/hardware.py:630`

## `_probe_remote_platform` — function, line 552
- **called from:**
- `services/hwfit/hardware.py:804`
- `tests/test_hwfit_windows.py:107`
- `tests/test_hwfit_windows.py:121`

## `_detect_windows` — function, line 568
- **called from:**
- `services/hwfit/hardware.py:821`
- `services/hwfit/hardware.py:840`
- `tests/test_hwfit_windows.py:95`

## `_as_int` — function, line 644
- **called from:**
- `services/hwfit/hardware.py:655`
- `services/hwfit/hardware.py:661`

## `_cache_key` — function, line 692
- **called from:**
- `services/hwfit/hardware.py:808`
- `services/tts/tts_service.py:215`
- `services/tts/tts_service.py:238`

## `_is_containerized` — function, line 705
- **called from:**
- `services/hwfit/hardware.py:778`

## `_hardware_visibility_warning` — function, line 721
- **called from:**
- `services/hwfit/hardware.py:783`

## `_attach_probe_context` — function, line 772
- **called from:**
- `services/hwfit/hardware.py:823`
- `services/hwfit/hardware.py:842`
- `services/hwfit/hardware.py:903`
- `tests/test_hwfit_container_visibility_warning.py:27`
- `tests/test_hwfit_container_visibility_warning.py:54`
- `tests/test_hwfit_container_visibility_warning.py:80`
- `tests/test_hwfit_container_visibility_warning.py:106`

## `detect_system` — function, line 792
- **called from:**
- `routes/cookbook_routes.py:3238`
- `routes/hwfit_routes.py:191`
- `routes/hwfit_routes.py:205`
- `routes/hwfit_routes.py:332`
- `routes/hwfit_routes.py:418`
- `tests/test_hwfit_cpu_arch_detection.py:41`
- `tests/test_hwfit_cpu_arch_detection.py:52`
- `tests/test_hwfit_macos.py:190`
- `tests/test_hwfit_remote_validation.py:82`
- `tests/test_hwfit_unified_nvidia.py:45`
- `tests/test_hwfit_unified_nvidia.py:115`
- `tests/test_hwfit_unified_nvidia.py:116`
- `tests/test_hwfit_unified_nvidia.py:117`
- `tests/test_hwfit_unified_nvidia.py:144`
- `tests/test_hwfit_unified_nvidia.py:145`
- `tests/test_hwfit_unified_nvidia.py:146`
- `tests/test_hwfit_unified_nvidia.py:147`
- `static/js/cookbook-hwfit.js:1048`
