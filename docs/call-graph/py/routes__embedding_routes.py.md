# `routes/embedding_routes.py` — definitions & call sites

16 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_cache_dir` — function, line 32
- **called from:**
- `routes/embedding_routes.py:49`
- `routes/embedding_routes.py:178`

## `_model_cache_name` — function, line 42
- **called from:**
- `routes/embedding_routes.py:50`

## `_model_cache_path` — function, line 47
- **called from:**
- `routes/embedding_routes.py:64`
- `routes/embedding_routes.py:134`
- `routes/embedding_routes.py:234`
- `tests/test_embedding_cache_confinement.py:33`
- `tests/test_embedding_cache_confinement.py:51`

## `_is_downloaded` — function, line 61
- **called from:**
- `routes/embedding_routes.py:129`
- `routes/embedding_routes.py:168`
- `routes/embedding_routes.py:203`
- `tests/test_embedding_cache_confinement.py:52`

## `_active_model` — function, line 78
- **called from:**
- `routes/embedding_routes.py:123`
- `routes/embedding_routes.py:214`

## `_dir_size_mb` — function, line 83
- **called from:**
- `routes/embedding_routes.py:134`

## `_load_custom_endpoint` — function, line 96
- **called from:**
- `routes/embedding_routes.py:247`
- `tests/test_embedding_endpoint_config.py:11`
- `tests/test_embedding_endpoint_config.py:22`

## `_save_custom_endpoint` — function, line 107
- **called from:**
- `routes/embedding_routes.py:295`

## `setup_embedding_routes` — function, line 112
- **called from:**
- `app.py:740`
- `tests/test_embedding_cache_confinement.py:23`

## `list_models` — function, line 116
- **route:** `GET /models`
- decorator: `router.get("/models")`
- **called from:**
- `scripts/add_hwfit_models.py:375`
- `src/agent_tools/model_interaction_tools.py:215`

## `download_model` — function (async), line 155
- **route:** `POST /models/{model_name:path}/download`
- decorator: `router.post("/models/{model_name:path}/download")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `download_status` — function, line 191
- **route:** `GET /models/{model_name:path}/status`
- decorator: `router.get("/models/{model_name:path}/status")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_model` — function, line 212
- **route:** `DELETE /models/{model_name:path}`
- decorator: `router.delete("/models/{model_name:path}")`
- **called from:**
- `tests/test_embedding_cache_confinement.py:72`

## `get_endpoint` — function, line 245
- **route:** `GET /endpoint`
- decorator: `router.get("/endpoint")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_endpoint` — function, line 256
- **route:** `POST /endpoint`
- decorator: `router.post("/endpoint")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `clear_endpoint` — function, line 336
- **route:** `DELETE /endpoint`
- decorator: `router.delete("/endpoint")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
