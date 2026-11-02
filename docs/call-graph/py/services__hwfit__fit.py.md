# `services/hwfit/fit.py` — definitions & call sites

20 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_lookup_apple_bandwidth` — function, line 77
- **called from:**
- `services/hwfit/fit.py:122`
- `tests/test_hwfit_apple_bandwidth.py:44`
- `tests/test_hwfit_apple_bandwidth.py:45`

## `_lookup_bandwidth` — function, line 107
- **called from:**
- `services/hwfit/fit.py:198`
- `tests/test_hwfit_amd.py:137`
- `tests/test_hwfit_apple_bandwidth.py:5`
- `tests/test_hwfit_apple_bandwidth.py:6`
- `tests/test_hwfit_apple_bandwidth.py:10`
- `tests/test_hwfit_apple_bandwidth.py:11`
- `tests/test_hwfit_apple_bandwidth.py:15`
- `tests/test_hwfit_apple_bandwidth.py:16`
- `tests/test_hwfit_apple_bandwidth.py:20`
- `tests/test_hwfit_apple_bandwidth.py:21`
- `tests/test_hwfit_apple_bandwidth.py:22`
- `tests/test_hwfit_apple_bandwidth.py:26`
- `tests/test_hwfit_apple_bandwidth.py:27`
- `tests/test_hwfit_apple_bandwidth.py:32`
- `tests/test_hwfit_apple_bandwidth.py:33`
- `tests/test_hwfit_apple_bandwidth.py:34`
- `tests/test_hwfit_apple_bandwidth.py:54`
- `tests/test_hwfit_apple_bandwidth.py:55`
- `tests/test_hwfit_apple_bandwidth.py:56`
- `tests/test_hwfit_apple_bandwidth.py:58`
- `tests/test_hwfit_apple_bandwidth.py:59`
- `tests/test_hwfit_bandwidth_nonstring.py:10`
- `tests/test_hwfit_bandwidth_nonstring.py:11`
- `tests/test_hwfit_bandwidth_nonstring.py:12`
- `tests/test_hwfit_bandwidth_nonstring.py:16`

## `_canonical_cpu_backend` — function, line 133
- **called from:**
- `services/hwfit/fit.py:204`

## `_is_mlx_model` — function, line 171
- **called from:**
- `services/hwfit/fit.py:780`

## `_estimate_speed` — function, line 184
- **called from:**
- `services/hwfit/fit.py:590`
- `tests/test_hwfit_amd.py:149`
- `tests/test_hwfit_amd.py:160`
- `tests/test_hwfit_amd.py:161`
- `tests/test_hwfit_amd.py:162`
- `tests/test_hwfit_cpu_only_fallback.py:72`
- `tests/test_hwfit_cpu_only_fallback.py:73`
- `tests/test_hwfit_cpu_only_fallback.py:81`
- `tests/test_hwfit_cpu_only_fallback.py:82`
- `tests/test_hwfit_cpu_only_fallback.py:91`
- `tests/test_hwfit_cpu_only_fallback.py:92`
- `tests/test_hwfit_cpu_only_fallback.py:105`
- `tests/test_hwfit_cpu_only_fallback.py:106`
- `tests/test_hwfit_cpu_only_fallback.py:114`
- `tests/test_hwfit_cpu_only_fallback.py:115`
- `tests/test_hwfit_cpu_only_fallback.py:124`
- `tests/test_hwfit_cpu_only_fallback.py:129`
- `tests/test_hwfit_cpu_only_fallback.py:130`
- `tests/test_hwfit_cpu_only_fallback.py:137`
- `tests/test_hwfit_cpu_only_fallback.py:138`

## `_architecture_bonus` — function, line 238
- **called from:**
- `services/hwfit/fit.py:288`

## `_quality_score` — function, line 259
- **called from:**
- `services/hwfit/fit.py:592`

## `_speed_score` — function, line 309
- **called from:**
- `services/hwfit/fit.py:593`

## `_fit_score` — function, line 314
- **called from:**
- `services/hwfit/fit.py:594`

## `_is_unified_memory_system` — function, line 329
- **called from:**
- `services/hwfit/fit.py:548`

## `_fit_level_for_budget` — function, line 334
- **called from:**
- `services/hwfit/fit.py:556`
- `services/hwfit/fit.py:570`
- `services/hwfit/fit.py:574`

## `_context_score` — function, line 345
- **called from:**
- `services/hwfit/fit.py:595`

## `_try_quant_at` — function, line 354
- **called from:**
- `services/hwfit/fit.py:515`

## `_quant_bits` — function, line 375
- **called from:**
- `services/hwfit/fit.py:490`
- `services/hwfit/fit.py:490`

## `_native_quant` — function, line 404
- **called from:**
- `services/hwfit/fit.py:175`
- `services/hwfit/fit.py:458`
- `services/hwfit/fit.py:779`
- `tests/test_hwfit_native_quant_labels.py:15`
- `tests/test_hwfit_native_quant_labels.py:21`
- `tests/test_hwfit_native_quant_labels.py:27`
- `tests/test_hwfit_native_quant_labels.py:33`
- `tests/test_hwfit_native_quant_labels.py:40`

## `analyze_model` — function, line 431
- **called from:**
- `services/hwfit/fit.py:848`
- `tests/test_hwfit_quant_formats.py:48`
- `tests/test_hwfit_quant_formats.py:75`

## `_version_key` — function, line 627
- **called from:**
- `services/hwfit/fit.py:662`

## `_search_blob` — function, line 674
- **called from:**
- `services/hwfit/fit.py:685`

## `_matches_search` — function, line 681
- **called from:**
- `services/hwfit/fit.py:829`

## `rank_models` — function, line 708
- **called from:**
- `routes/hwfit_routes.py:312`
- `tests/test_hwfit_amd.py:42`
- `tests/test_hwfit_amd.py:52`
- `tests/test_hwfit_amd.py:59`
- `tests/test_hwfit_amd.py:65`
- `tests/test_hwfit_amd.py:171`
- `tests/test_hwfit_amd.py:190`
- `tests/test_hwfit_gemma4_12b.py:31`
- `tests/test_hwfit_macos.py:49`
- `tests/test_hwfit_macos.py:63`
- `tests/test_hwfit_macos.py:72`
- `tests/test_hwfit_macos.py:99`
- `tests/test_hwfit_manual_backend.py:79`
- `tests/test_hwfit_quant_formats.py:52`
- `tests/test_hwfit_windows.py:43`
- `tests/test_hwfit_windows.py:52`
- `tests/test_hwfit_windows.py:59`
- `tests/test_hwfit_windows.py:66`
- `tests/test_hwfit_windows.py:73`
