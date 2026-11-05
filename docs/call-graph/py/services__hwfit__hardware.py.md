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
- `services/search/providers.py:268`
- `services/search/providers.py:281`
- `services/search/providers.py:290`
- `services/search/providers.py:298`
- `src/research_handler.py:421`
- `tests/test_agent_evidence_loop.py:128`
- `tests/test_agent_evidence_loop.py:140`
- `tests/test_agent_evidence_loop.py:152`
- `tests/test_agent_evidence_loop.py:163`
- `tests/test_agent_evidence_loop.py:189`
- `tests/test_agent_evidence_loop.py:222`
- `tests/test_agent_evidence_loop.py:262`
- `tests/test_agent_evidence_loop.py:304`
- `tests/test_agent_evidence_loop.py:356`
- `tests/test_agent_evidence_loop.py:399`
- `tests/test_agent_evidence_loop.py:439`
- `tests/test_agent_evidence_loop.py:461`
- `tests/test_agent_evidence_loop.py:627`
- `tests/test_agent_evidence_loop.py:649`
- `tests/test_agent_evidence_loop.py:677`
- `tests/test_agent_evidence_loop.py:715`
- `tests/test_agent_rounds_exhausted.py:24`
- `tests/test_agent_runtime_context.py:28`
- `tests/test_app_config_shared_fetch_js.py:89`
- `tests/test_app_config_shared_fetch_js.py:107`
- `tests/test_app_config_shared_fetch_js.py:125`
- `tests/test_app_config_shared_fetch_js.py:144`
- `tests/test_app_config_shared_fetch_js.py:163`
- `tests/test_app_config_shared_fetch_js.py:188`
- `tests/test_app_config_shared_fetch_js.py:277`
- … +208 more (grep the name in repo)

## `_group_gpus` — function, line 53
- **called from:**
- `services/hwfit/hardware.py:159`
- `services/hwfit/hardware.py:166`
- `services/hwfit/hardware.py:272`
- `services/hwfit/hardware.py:407`

## `_detect_nvidia` — function, line 84
- **called from:**
- `services/hwfit/hardware.py:867`
- `tests/test_hwfit_unified_nvidia.py:27`
- `tests/test_hwfit_unified_nvidia.py:54`
- `tests/test_hwfit_unified_nvidia.py:64`
- `tests/test_hwfit_unified_nvidia.py:73`

## `classify_amd_gfx` — function, line 178
- **called from:**
- `services/hwfit/hardware.py:239`
- `tests/test_hwfit_amd.py:92`

## `_detect_amd` — function, line 205
- **called from:**
- `services/hwfit/hardware.py:867`
- `tests/test_hwfit_amd.py:126`

## `_read` — function, line 209
- **called from:**
- `services/hwfit/hardware.py:246`
- `services/hwfit/hardware.py:253`
- `services/hwfit/hardware.py:254`
- `services/hwfit/hardware.py:255`
- `services/hwfit/hardware.py:266`
- `tests/test_compare_mobile_tabs_static.py:13`
- `tests/test_compare_mobile_tabs_static.py:14`
- `tests/test_compare_mobile_tabs_static.py:27`
- `tests/test_compare_mobile_tabs_static.py:47`
- `tests/test_compare_mobile_tabs_static.py:69`
- `tests/test_compare_shuffle_visual_static.py:14`
- `tests/test_compare_shuffle_visual_static.py:25`
- `tests/test_compare_shuffle_visual_static.py:26`
- `tests/test_compare_shuffle_visual_static.py:43`
- `tests/test_compare_shuffle_visual_static.py:44`
- `tests/test_compare_shuffle_visual_static.py:56`
- `tests/test_compare_shuffle_visual_static.py:63`
- `tests/test_compare_shuffle_visual_static.py:64`
- `tests/test_compare_shuffle_visual_static.py:65`
- `tests/test_compare_shuffle_visual_static.py:77`
- `tests/test_cookbook_dependency_completion_regression.py:24`
- `tests/test_cookbook_dependency_completion_regression.py:32`
- `tests/test_cookbook_dependency_completion_regression.py:46`
- `tests/test_cookbook_dependency_completion_regression.py:61`
- `tests/test_cookbook_dependency_completion_regression.py:72`
- `tests/test_cookbook_dependency_completion_regression.py:90`
- `tests/test_cookbook_dependency_completion_regression.py:104`
- `tests/test_cookbook_dependency_completion_regression.py:114`
- `tests/test_cookbook_dependency_completion_regression.py:123`
- `tests/test_cookbook_dependency_completion_regression.py:130`
- `tests/test_cookbook_dependency_completion_regression.py:139`
- `tests/test_cookbook_dependency_completion_regression.py:148`
- `tests/test_cookbook_dependency_completion_regression.py:158`
- `tests/test_cookbook_dependency_completion_regression.py:167`
- `tests/test_cookbook_dependency_completion_regression.py:180`
- `tests/test_cookbook_dependency_completion_regression.py:188`
- `tests/test_cookbook_dependency_completion_regression.py:197`
- `tests/test_cookbook_dependency_completion_regression.py:206`
- `tests/test_cookbook_dependency_completion_regression.py:216`
- `tests/test_cookbook_dependency_completion_regression.py:229`
- `tests/test_cookbook_dependency_completion_regression.py:230`
- `tests/test_cookbook_dependency_completion_regression.py:240`
- `tests/test_cookbook_dependency_completion_regression.py:241`
- `tests/test_cookbook_dependency_completion_regression.py:251`
- `tests/test_cookbook_dependency_completion_regression.py:262`
- `tests/test_cookbook_dependency_completion_regression.py:263`
- `tests/test_cookbook_dependency_completion_regression.py:264`
- `tests/test_cookbook_dependency_completion_regression.py:273`
- `tests/test_cookbook_dependency_completion_regression.py:283`
- `tests/test_cookbook_dependency_completion_regression.py:291`
- `tests/test_cookbook_dependency_completion_regression.py:299`
- `tests/test_cookbook_dependency_completion_regression.py:308`
- `tests/test_cookbook_dependency_completion_regression.py:315`
- `tests/test_cookbook_dependency_completion_regression.py:316`
- `tests/test_cookbook_dependency_completion_regression.py:328`
- `tests/test_cookbook_dependency_completion_regression.py:345`
- `tests/test_cookbook_dependency_completion_regression.py:358`
- `tests/test_cookbook_dependency_completion_regression.py:359`
- `tests/test_cookbook_dependency_completion_regression.py:370`
- `tests/test_cookbook_dependency_completion_regression.py:371`
- … +171 more (grep the name in repo)

## `_list_drm_cards` — function, line 219
- **called from:**
- `services/hwfit/hardware.py:244`

## `_amd_arch` — function, line 230
- **called from:**
- `services/hwfit/hardware.py:273`

## `_detect_apple_silicon` — function, line 309
- **called from:**
- `services/hwfit/hardware.py:867`
- `tests/test_hwfit_macos.py:121`
- `tests/test_hwfit_macos.py:141`
- `tests/test_hwfit_macos.py:152`
- `tests/test_hwfit_macos.py:163`
- `tests/test_hwfit_macos.py:172`
- `tests/test_hwfit_macos.py:181`

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
- `services/hwfit/hardware.py:853`

## `_get_available_ram_gb` — function, line 475
- **called from:**
- `services/hwfit/hardware.py:862`

## `_get_cpu_name` — function, line 482
- **called from:**
- `services/hwfit/hardware.py:864`

## `_get_cpu_count` — function, line 500
- **called from:**
- `services/hwfit/hardware.py:863`

## `_canonical_cpu_arch` — function, line 516
- **called from:**
- `services/hwfit/hardware.py:333`
- `services/hwfit/hardware.py:531`
- `services/hwfit/hardware.py:532`
- `services/hwfit/hardware.py:657`

## `_get_cpu_arch` — function, line 529
- **called from:**
- `services/hwfit/hardware.py:865`

## `_powershell_exe` — function, line 535
- **called from:**
- `services/hwfit/hardware.py:635`

## `_powershell_encoded_for_ssh` — function, line 541
- **called from:**
- `services/hwfit/hardware.py:630`

## `_probe_remote_platform` — function, line 552
- **called from:**
- `services/hwfit/hardware.py:806`
- `tests/test_hwfit_windows.py:113`
- `tests/test_hwfit_windows.py:127`

## `_detect_windows` — function, line 568
- **called from:**
- `services/hwfit/hardware.py:823`
- `services/hwfit/hardware.py:844`
- `tests/test_hwfit_windows.py:101`

## `_as_int` — function, line 644
- **called from:**
- `services/hwfit/hardware.py:655`
- `services/hwfit/hardware.py:661`

## `_cache_key` — function, line 694
- **called from:**
- `services/hwfit/hardware.py:810`
- `services/tts/tts_service.py:215`
- `services/tts/tts_service.py:238`
- `src/skill_index.py:60`

## `_is_containerized` — function, line 707
- **called from:**
- `services/hwfit/hardware.py:780`

## `_hardware_visibility_warning` — function, line 723
- **called from:**
- `services/hwfit/hardware.py:785`

## `_attach_probe_context` — function, line 774
- **called from:**
- `services/hwfit/hardware.py:825`
- `services/hwfit/hardware.py:846`
- `services/hwfit/hardware.py:911`
- `tests/test_hwfit_container_visibility_warning.py:27`
- `tests/test_hwfit_container_visibility_warning.py:54`
- `tests/test_hwfit_container_visibility_warning.py:80`
- `tests/test_hwfit_container_visibility_warning.py:106`

## `detect_system` — function, line 794
- **called from:**
- `routes/cookbook_routes.py:3117`
- `routes/hwfit_routes.py:214`
- `routes/hwfit_routes.py:228`
- `routes/hwfit_routes.py:358`
- `routes/hwfit_routes.py:444`
- `tests/test_hwfit_cpu_arch_detection.py:41`
- `tests/test_hwfit_cpu_arch_detection.py:52`
- `tests/test_hwfit_macos.py:197`
- `tests/test_hwfit_probe_result_shape.py:32`
- `tests/test_hwfit_probe_result_shape.py:41`
- `tests/test_hwfit_probe_result_shape.py:51`
- `tests/test_hwfit_probe_result_shape.py:74`
- `tests/test_hwfit_remote_validation.py:82`
- `tests/test_hwfit_unified_nvidia.py:45`
- `tests/test_hwfit_unified_nvidia.py:115`
- `tests/test_hwfit_unified_nvidia.py:116`
- `tests/test_hwfit_unified_nvidia.py:117`
- `tests/test_hwfit_unified_nvidia.py:144`
- `tests/test_hwfit_unified_nvidia.py:145`
- `tests/test_hwfit_unified_nvidia.py:146`
- `tests/test_hwfit_unified_nvidia.py:147`
- `static/js/cookbook-hwfit.js:1099`
