# `services/hwfit/hf_discovery.py` — definitions & call sites

16 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_format_params` — function, line 91
- **called from:**
- `services/hwfit/hf_discovery.py:234`

## `_parse_params_from_name` — function, line 109
- **called from:**
- `services/hwfit/hf_discovery.py:231`

## `_infer_quant` — function, line 127
- **called from:**
- `services/hwfit/hf_discovery.py:238`

## `_quant_bytes_per_param` — function, line 160
- **called from:**
- `services/hwfit/hf_discovery.py:240`

## `_infer_context` — function, line 179
- **called from:**
- `services/hwfit/hf_discovery.py:258`

## `_infer_use_case` — function, line 190
- **called from:**
- `services/hwfit/hf_discovery.py:259`

## `_entry_from_collection_item` — function, line 219
- **called from:**
- `services/hwfit/hf_discovery.py:315`
- `tests/test_hwfit_hf_discovery_moe.py:17`
- `tests/test_hwfit_hf_discovery_moe.py:24`
- `tests/test_hwfit_hf_discovery_moe.py:31`
- `tests/test_hwfit_hf_discovery_pipeline_filter.py:19`
- `tests/test_hwfit_hf_discovery_pipeline_filter.py:31`

## `_next_link` — function, line 285
- **called from:**
- `services/hwfit/hf_discovery.py:305`

## `fetch_collection_models` — function, line 292
- **called from:**
- `services/hwfit/hf_discovery.py:365`
- `services/hwfit/hf_discovery.py:378`

## `_load_cache` — function, line 323
- **called from:**
- `services/hwfit/hf_discovery.py:347`
- `services/hwfit/hf_discovery.py:351`

## `_write_cache` — function, line 333
- **called from:**
- `services/hwfit/hf_discovery.py:366`
- `services/hwfit/hf_discovery.py:390`

## `load_cached_mlx_community_models` — function, line 346
- **called from:**
- `services/hwfit/hf_discovery.py:363`
- `services/hwfit/models.py:310`

## `load_cached_hf_collection_models` — function, line 350
- **called from:**
- `services/hwfit/hf_discovery.py:372`
- `services/hwfit/hf_discovery.py:392`
- `services/hwfit/models.py:311`

## `_cache_fresh` — function, line 354
- **called from:**
- `services/hwfit/hf_discovery.py:362`
- `services/hwfit/hf_discovery.py:371`

## `refresh_mlx_community_cache` — function, line 361
- **called from:**
- `services/hwfit/models.py:294`

## `refresh_hf_collection_models_cache` — function, line 370
- **called from:**
- `services/hwfit/models.py:295`
