# `scripts/diffusion_server.py` — definitions & call sites

41 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `lifespan` — function (async), line 52
- decorator: `asynccontextmanager`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_compute_allowed_hosts` — function, line 68
- **called from:**
- `scripts/diffusion_server.py:1499`

## `_compute_cors_origins` — function, line 80
- **called from:**
- `scripts/diffusion_server.py:1500`

## `_configure_security_middleware` — function, line 92
- **called from:**
- `scripts/diffusion_server.py:114`
- `scripts/diffusion_server.py:1501`

## `_start_progress` — function, line 117
- **called from:**
- `scripts/diffusion_server.py:697`
- `scripts/diffusion_server.py:787`

## `_update_progress` — function, line 133
- **called from:**
- `scripts/diffusion_server.py:169`
- `scripts/diffusion_server.py:173`
- `scripts/diffusion_server.py:740`
- `scripts/diffusion_server.py:865`

## `_finish_progress` — function, line 150
- **called from:**
- `scripts/diffusion_server.py:744`
- `scripts/diffusion_server.py:749`
- `scripts/diffusion_server.py:863`
- `scripts/diffusion_server.py:870`

## `_run_pipeline_with_progress` — function, line 167
- **called from:**
- `scripts/diffusion_server.py:734`
- `scripts/diffusion_server.py:830`
- `scripts/diffusion_server.py:856`

## `step_end_callback` — function, line 168
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `legacy_callback` — function, line 172
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ImageRequest` — class, line 188
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_parse_size` — function, line 198
- **called from:**
- `scripts/diffusion_server.py:695`
- `scripts/diffusion_server.py:785`

## `_quality_steps` — function, line 206
- **called from:**
- `scripts/diffusion_server.py:696`
- `scripts/diffusion_server.py:786`

## `_guidance_scale` — function, line 212
- **called from:**
- `scripts/diffusion_server.py:722`
- `scripts/diffusion_server.py:730`
- `scripts/diffusion_server.py:809`
- `scripts/diffusion_server.py:842`

## `_default_negative_prompt` — function, line 216
- **called from:**
- `scripts/diffusion_server.py:709`
- `scripts/diffusion_server.py:801`
- `scripts/diffusion_server.py:827`
- `scripts/diffusion_server.py:844`
- `scripts/diffusion_server.py:853`

## `_pipeline_accepts_arg` — function, line 221
- **called from:**
- `scripts/diffusion_server.py:709`
- `scripts/diffusion_server.py:775`
- `scripts/diffusion_server.py:776`

## `_pipeline_call_kwargs` — function, line 230
- **called from:**
- `scripts/diffusion_server.py:802`
- `scripts/diffusion_server.py:819`
- `scripts/diffusion_server.py:838`
- `scripts/diffusion_server.py:848`

## `_image_response` — function, line 249
- **called from:**
- `scripts/diffusion_server.py:751`
- `scripts/diffusion_server.py:871`

## `_fix_meta_tensors` — function, line 258
- **called from:**
- `scripts/diffusion_server.py:447`
- `scripts/diffusion_server.py:481`
- `scripts/diffusion_server.py:497`
- `scripts/diffusion_server.py:623`

## `_target_device` — function, line 279
- **called from:**
- `scripts/diffusion_server.py:351`
- `scripts/diffusion_server.py:942`

## `_can_cpu_offload` — function, line 294
- **called from:**
- `scripts/diffusion_server.py:328`
- `scripts/diffusion_server.py:449`
- `scripts/diffusion_server.py:624`
- `scripts/diffusion_server.py:961`

## `_load_omnigen2_pipeline` — function, line 300
- **called from:**
- `scripts/diffusion_server.py:413`

## `load_model` — function, line 342
- **called from:**
- `scripts/diffusion_server.py:53`

## `_cleanup` — function, line 403
- **called from:**
- `scripts/diffusion_server.py:439`
- `scripts/diffusion_server.py:443`
- `scripts/diffusion_server.py:457`
- `scripts/diffusion_server.py:468`
- `scripts/diffusion_server.py:488`
- `scripts/diffusion_server.py:504`
- `scripts/diffusion_server.py:635`
- `src/agent_runtime/effect_adapters.py:353`
- `tests/test_process_lifecycle.py:248`
- `tests/test_process_lifecycle.py:269`
- `tests/test_process_lifecycle.py:295`
- `static/js/compare/index.js:1524`
- `static/js/cookbookRunning.js:2840`
- `static/js/cookbookRunning.js:2874`
- `static/js/cookbookRunning.js:2880`
- `static/js/document.js:13672`
- `static/js/document.js:14367`
- `static/js/document.js:14439`
- `static/js/emailInbox.js:1261`
- `static/js/emailInbox.js:1269`
- `static/js/emailInbox.js:1274`

## `_load_pipe` — function, line 415
- **called from:**
- `scripts/diffusion_server.py:510`
- `scripts/diffusion_server.py:520`

## `_ensure_config_local` — function, line 576
- **called from:**
- `scripts/diffusion_server.py:617`

## `list_models` — function, line 678
- **route:** `GET /v1/models`
- decorator: `app.get("/v1/models")`
- **called from:**
- `scripts/add_hwfit_models.py:457`
- `src/agent_tools/model_interaction_tools.py:271`
- `tests/test_chatgpt_subscription_routes.py:509`
- `tests/test_list_models_hardware_fit.py:32`

## `generate_image` — function, line 691
- **route:** `POST /v1/images/generations`
- decorator: `app.post("/v1/images/generations")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `image_progress` — function, line 755
- **route:** `GET /v1/images/progress/{request_id}`
- decorator: `app.get("/v1/images/progress/{request_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `edit_image` — function (async), line 763
- **route:** `POST /v1/images/edits`
- decorator: `app.post("/v1/images/edits")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `InpaintRequest` — class, line 874
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_get_inpaint_pipe` — function, line 888
- **called from:**
- `scripts/diffusion_server.py:1003`
- `scripts/diffusion_server.py:1369`
- `scripts/diffusion_server.py:1429`

## `inpaint_image` — function, line 975
- **route:** `POST /v1/images/inpaint`
- decorator: `app.post("/v1/images/inpaint")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `HarmonizeRequest` — class, line 1188
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_rgb_to_lalphabeta` — function, line 1208
- **called from:**
- `scripts/diffusion_server.py:1271`

## `_lalphabeta_to_rgb` — function, line 1231
- **called from:**
- `scripts/diffusion_server.py:1280`

## `_reinhard_color_transfer` — function, line 1250
- **called from:**
- `scripts/diffusion_server.py:1359`

## `_decode_mask_b64` — function, line 1289
- **called from:**
- `scripts/diffusion_server.py:1341`
- `scripts/diffusion_server.py:1342`

## `harmonize_image` — function, line 1308
- **route:** `POST /v1/images/harmonize`
- decorator: `app.post("/v1/images/harmonize")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_legacy_whole_image_harmonize` — function, line 1414
- **called from:**
- `scripts/diffusion_server.py:1348`

## `health` — function, line 1462
- **route:** `GET /health`
- decorator: `app.get("/health")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
