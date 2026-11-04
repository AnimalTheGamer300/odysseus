# `routes/hwfit_routes.py` — definitions & call sites

11 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_validate_detection_target` — function, line 21
- **called from:**
- `routes/hwfit_routes.py:190`
- `routes/hwfit_routes.py:204`
- `routes/hwfit_routes.py:331`
- `routes/hwfit_routes.py:417`

## `_apply_manual_hardware` — function, line 29
- **called from:**
- `routes/hwfit_routes.py:232`
- `routes/hwfit_routes.py:431`
- `tests/test_hwfit_manual_backend.py:17`
- `tests/test_hwfit_manual_backend.py:18`
- `tests/test_hwfit_manual_backend.py:24`
- `tests/test_hwfit_manual_backend.py:32`
- `tests/test_hwfit_manual_backend.py:48`
- `tests/test_hwfit_manual_backend.py:55`
- `tests/test_hwfit_manual_backend.py:62`
- `tests/test_hwfit_manual_backend.py:73`

## `_run_model_probe` — function, line 115
- **called from:**
- `routes/hwfit_routes.py:147`
- `routes/hwfit_routes.py:152`
- `routes/hwfit_routes.py:170`

## `_inspect_model_path` — function, line 136
- **called from:**
- `routes/hwfit_routes.py:371`

## `setup_hwfit_routes` — function, line 182
- **called from:**
- `app.py:811`
- `tests/test_hwfit_gpu_count_nonnumeric.py:11`
- `tests/test_hwfit_remote_validation.py:9`

## `get_system` — function, line 186
- **route:** `GET /system`
- decorator: `router.get("/system")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_models` — function, line 194
- **route:** `GET /models`
- decorator: `router.get("/models")`
- **called from:**
- `routes/hwfit_routes.py:214`
- `routes/hwfit_routes.py:335`
- `services/hwfit/fit.py:716`
- `tests/test_hwfit_amd.py:40`
- `tests/test_hwfit_amd.py:194`
- `tests/test_hwfit_gemma4_12b.py:18`
- `tests/test_hwfit_gemma4_12b.py:23`
- `tests/test_hwfit_gemma4_12b.py:37`
- `tests/test_hwfit_gemma4_12b.py:43`
- `tests/test_hwfit_gemma4_12b.py:49`
- `tests/test_hwfit_macos.py:70`
- `tests/test_hwfit_macos.py:84`
- `tests/test_hwfit_manual_backend.py:77`
- `tests/test_hwfit_quant_formats.py:37`
- `tests/test_hwfit_quant_formats.py:45`
- `tests/test_hwfit_windows.py:41`

## `_apply_group` — function, line 251
- **called from:**
- `routes/hwfit_routes.py:274`
- `routes/hwfit_routes.py:286`

## `get_serve_profiles` — function, line 319
- **route:** `GET /profiles`
- decorator: `router.get("/profiles")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_norm` — function, line 337
- **called from:**
- `routes/hwfit_routes.py:365`
- `routes/hwfit_routes.py:367`
- `static/js/cookbookServe.js:2484`
- `static/js/cookbookServe.js:2484`
- `static/js/theme.js:1001`
- `static/js/theme.js:1001`

## `get_image_models` — function, line 413
- **route:** `GET /image-models`
- decorator: `router.get("/image-models")`
- **called from:**
- `services/hwfit/image_models.py:343`
