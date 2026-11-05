# `routes/hwfit_routes.py` — definitions & call sites

12 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_official_model` — function, line 28
- **called from:**
- `routes/hwfit_routes.py:338`
- `routes/hwfit_routes.py:481`

## `_validate_detection_target` — function, line 40
- **called from:**
- `routes/hwfit_routes.py:213`
- `routes/hwfit_routes.py:227`
- `routes/hwfit_routes.py:357`
- `routes/hwfit_routes.py:443`

## `_apply_manual_hardware` — function, line 48
- **called from:**
- `routes/hwfit_routes.py:256`
- `routes/hwfit_routes.py:457`
- `tests/test_hwfit_manual_backend.py:23`
- `tests/test_hwfit_manual_backend.py:24`
- `tests/test_hwfit_manual_backend.py:30`
- `tests/test_hwfit_manual_backend.py:38`
- `tests/test_hwfit_manual_backend.py:54`
- `tests/test_hwfit_manual_backend.py:61`
- `tests/test_hwfit_manual_backend.py:68`
- `tests/test_hwfit_manual_backend.py:79`

## `_run_model_probe` — function, line 134
- **called from:**
- `routes/hwfit_routes.py:166`
- `routes/hwfit_routes.py:171`
- `routes/hwfit_routes.py:189`

## `_inspect_model_path` — function, line 155
- **called from:**
- `routes/hwfit_routes.py:397`

## `setup_hwfit_routes` — function, line 201
- **called from:**
- `app.py:895`
- `tests/test_codeql_python_residual_followup.py:105`
- `tests/test_hwfit_gpu_count_nonnumeric.py:36`
- `tests/test_hwfit_remote_validation.py:9`
- `tests/test_publication_plan_b.py:112`

## `get_system` — function, line 209
- **route:** `GET /system`
- decorator: `router.get("/system")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_models` — function, line 217
- **route:** `GET /models`
- decorator: `router.get("/models")`
- **called from:**
- `routes/hwfit_routes.py:237`
- `routes/hwfit_routes.py:361`
- `services/hwfit/fit.py:716`
- `tests/test_hwfit_amd.py:46`
- `tests/test_hwfit_amd.py:202`
- `tests/test_hwfit_gemma4_12b.py:43`
- `tests/test_hwfit_gemma4_12b.py:74`
- `tests/test_hwfit_macos.py:76`
- `tests/test_hwfit_manual_backend.py:83`
- `tests/test_hwfit_quant_formats.py:43`
- `tests/test_hwfit_quant_formats.py:51`
- `tests/test_hwfit_windows.py:47`
- `tests/test_publication_plan_b.py:88`
- `tests/test_publication_plan_b.py:92`
- `tests/test_publication_plan_b.py:98`
- `tests/test_publication_plan_b.py:102`

## `_apply_group` — function, line 275
- **called from:**
- `routes/hwfit_routes.py:298`
- `routes/hwfit_routes.py:310`

## `get_serve_profiles` — function, line 345
- **route:** `GET /profiles`
- decorator: `router.get("/profiles")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_norm` — function, line 363
- **called from:**
- `routes/hwfit_routes.py:391`
- `routes/hwfit_routes.py:393`
- `static/js/cookbookServe.js:2556`
- `static/js/cookbookServe.js:2556`
- `static/js/theme.js:1065`
- `static/js/theme.js:1065`

## `get_image_models` — function, line 439
- **route:** `GET /image-models`
- decorator: `router.get("/image-models")`
- **called from:**
- `services/hwfit/image_models.py:384`
