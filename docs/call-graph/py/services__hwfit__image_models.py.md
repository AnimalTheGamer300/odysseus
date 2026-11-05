# `services/hwfit/image_models.py` — definitions & call sites

17 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_repo_display_name` — function, line 43
- **called from:**
- `services/hwfit/image_models.py:155`

## `_provider_from_repo` — function, line 48
- **called from:**
- `services/hwfit/image_models.py:156`

## `_infer_capabilities` — function, line 59
- **called from:**
- `services/hwfit/image_models.py:146`

## `_estimate_image_model` — function, line 78
- **called from:**
- `services/hwfit/image_models.py:134`

## `_params_b_from_item` — function, line 99
- **called from:**
- `services/hwfit/image_models.py:135`

## `_mlx_quantize_estimate` — function, line 106
- **called from:**
- `services/hwfit/image_models.py:145`

## `_collection_item_to_model` — function, line 127
- **called from:**
- `services/hwfit/image_models.py:212`
- `tests/test_image_models_nonstring_search.py:124`

## `_fetch_hf_image_collection_models` — function, line 181
- **called from:**
- `services/hwfit/image_models.py:347`

## `_hf_model_search` — function, line 235
- **called from:**
- `services/hwfit/image_models.py:284`

## `_variant_score` — function, line 254
- **called from:**
- `services/hwfit/image_models.py:292`

## `_best_variant_repo` — function, line 282
- **called from:**
- `services/hwfit/image_models.py:312`
- `services/hwfit/image_models.py:316`

## `_should_discover_variants` — function, line 299
- **called from:**
- `services/hwfit/image_models.py:331`

## `_discover_quant_repos` — function, line 303
- **called from:**
- `services/hwfit/image_models.py:332`

## `_merge_quant_repos` — function, line 327
- **called from:**
- `services/hwfit/image_models.py:345`
- `services/hwfit/image_models.py:350`

## `get_image_models` — function, line 343
- **called from:**
- `services/hwfit/image_models.py:384`

## `_is_apple_image_system` — function, line 355
- **called from:**
- `services/hwfit/image_models.py:381`

## `rank_image_models` — function, line 369
- **called from:**
- `routes/hwfit_routes.py:479`
- `services/hwfit/fit.py:726`
- `tests/test_image_models_nondict_system.py:13`
- `tests/test_image_models_nondict_system.py:14`
- `tests/test_image_models_nonstring_search.py:18`
- `tests/test_image_models_nonstring_search.py:24`
- `tests/test_image_models_nonstring_search.py:47`
- `tests/test_image_models_nonstring_search.py:48`
- `tests/test_image_models_nonstring_search.py:81`
- `tests/test_image_models_nonstring_search.py:82`
- `tests/test_image_models_nonstring_search.py:110`
- `tests/test_image_models_nonstring_search.py:114`
- `tests/test_image_models_nonstring_search.py:132`
- `tests/test_image_models_nonstring_search.py:136`
