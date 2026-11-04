# `services/hwfit/image_models.py` — definitions & call sites

17 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_repo_display_name` — function, line 38
- **called from:**
- `services/hwfit/image_models.py:150`

## `_provider_from_repo` — function, line 43
- **called from:**
- `services/hwfit/image_models.py:151`

## `_infer_capabilities` — function, line 54
- **called from:**
- `services/hwfit/image_models.py:141`

## `_estimate_image_model` — function, line 73
- **called from:**
- `services/hwfit/image_models.py:129`

## `_params_b_from_item` — function, line 94
- **called from:**
- `services/hwfit/image_models.py:130`

## `_mlx_quantize_estimate` — function, line 101
- **called from:**
- `services/hwfit/image_models.py:140`

## `_collection_item_to_model` — function, line 122
- **called from:**
- `services/hwfit/image_models.py:186`
- `tests/test_image_models_nonstring_search.py:124`

## `_fetch_hf_image_collection_models` — function, line 170
- **called from:**
- `services/hwfit/image_models.py:306`

## `_hf_model_search` — function, line 194
- **called from:**
- `services/hwfit/image_models.py:243`

## `_variant_score` — function, line 213
- **called from:**
- `services/hwfit/image_models.py:251`

## `_best_variant_repo` — function, line 241
- **called from:**
- `services/hwfit/image_models.py:271`
- `services/hwfit/image_models.py:275`

## `_should_discover_variants` — function, line 258
- **called from:**
- `services/hwfit/image_models.py:290`

## `_discover_quant_repos` — function, line 262
- **called from:**
- `services/hwfit/image_models.py:291`

## `_merge_quant_repos` — function, line 286
- **called from:**
- `services/hwfit/image_models.py:304`
- `services/hwfit/image_models.py:309`

## `get_image_models` — function, line 302
- **called from:**
- `services/hwfit/image_models.py:343`

## `_is_apple_image_system` — function, line 314
- **called from:**
- `services/hwfit/image_models.py:340`

## `rank_image_models` — function, line 328
- **called from:**
- `routes/hwfit_routes.py:453`
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
