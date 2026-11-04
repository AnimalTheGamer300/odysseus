# `services/hwfit/models.py` — definitions & call sites

14 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `infer_quantization_from_name` — function, line 88
- **called from:**
- `services/hwfit/models.py:132`
- `tests/test_hwfit_quant_formats.py:33`

## `_normalize_model_entry` — function, line 129
- **called from:**
- `services/hwfit/models.py:325`
- `services/hwfit/models.py:334`

## `is_prequantized` — function, line 138
- **called from:**
- `services/hwfit/fit.py:459`
- `services/hwfit/fit.py:792`
- `services/hwfit/models.py:215`
- `services/hwfit/profiles.py:138`
- `tests/test_hwfit_gemma4_12b.py:44`
- `tests/test_hwfit_gemma4_12b.py:45`
- `tests/test_hwfit_models_nonstring_fields.py:25`
- `tests/test_hwfit_models_nonstring_fields.py:26`
- `tests/test_hwfit_models_nonstring_fields.py:30`
- `tests/test_hwfit_models_nonstring_fields.py:31`
- `tests/test_hwfit_quant_formats.py:41`

## `params_b` — function, line 152
- **called from:**
- `services/hwfit/fit.py:260`
- `services/hwfit/fit.py:432`
- `services/hwfit/fit.py:699`
- `services/hwfit/models.py:196`
- `services/hwfit/models.py:207`
- `services/hwfit/profiles.py:41`
- `services/hwfit/profiles.py:57`
- `tests/test_hwfit_models_nonstring_fields.py:15`
- `tests/test_hwfit_models_nonstring_fields.py:16`
- `tests/test_hwfit_models_nonstring_fields.py:20`
- `tests/test_hwfit_models_nonstring_fields.py:21`
- `tests/test_hwfit_params_b_malformed.py:13`
- `tests/test_hwfit_params_b_malformed.py:14`
- `tests/test_hwfit_params_b_malformed.py:18`
- `tests/test_hwfit_params_b_malformed.py:19`
- `tests/test_hwfit_params_b_malformed.py:20`
- `tests/test_hwfit_params_b_malformed.py:24`

## `estimate_memory_gb` — function, line 192
- **called from:**
- `services/hwfit/fit.py:356`
- `services/hwfit/fit.py:366`
- `services/hwfit/fit.py:524`
- `services/hwfit/models.py:217`
- `services/hwfit/models.py:223`
- `services/hwfit/models.py:231`
- `services/hwfit/models.py:238`

## `_active_params_b` — function, line 202
- **called from:**
- `services/hwfit/fit.py:196`
- `services/hwfit/models.py:198`
- `services/hwfit/profiles.py:46`

## `best_quant_for_budget` — function, line 210
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `infer_use_case` — function, line 246
- **called from:**
- `services/hwfit/fit.py:291`
- `services/hwfit/fit.py:436`
- `services/hwfit/fit.py:853`

## `_load_model_file` — function, line 270
- **called from:**
- `services/hwfit/models.py:327`
- `services/hwfit/models.py:337`

## `reset_model_cache` — function, line 278
- **called from:**
- `services/hwfit/models.py:297`

## `refresh_dynamic_catalogs` — function, line 282
- **called from:**
- `routes/hwfit_routes.py:211`

## `get_models` — function, line 300
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

## `_append_models` — function, line 317
- **called from:**
- `services/hwfit/models.py:335`
- `services/hwfit/models.py:336`
- `services/hwfit/models.py:337`

## `model_catalog_path` — function, line 342
- **called from:**
- `routes/hwfit_routes.py:218`
