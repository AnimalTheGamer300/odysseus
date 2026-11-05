# `routes/gallery/gallery_routes.py` — definitions & call sites

80 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_compose_cloud_image_edit` — function, line 41
- **called from:**
- `routes/gallery/gallery_routes.py:1981`
- `tests/test_gallery_cloud_inpaint.py:90`

## `_rss_mb` — function, line 59
- **called from:**
- `routes/gallery/gallery_routes.py:72`
- `tests/test_gallery_heavy_image_ops.py:59`

## `_image_op_log_rss` — function, line 71
- **called from:**
- `routes/gallery/gallery_routes.py:119`
- `routes/gallery/gallery_routes.py:132`
- `routes/gallery/gallery_routes.py:184`
- `routes/gallery/gallery_routes.py:234`
- `routes/gallery/gallery_routes.py:2722`
- `routes/gallery/gallery_routes.py:2819`
- `routes/gallery/gallery_routes.py:2884`
- `routes/gallery/gallery_routes.py:2901`

## `_local_image_models_enabled` — function, line 75
- **called from:**
- `routes/gallery/gallery_routes.py:153`
- `routes/gallery/gallery_routes.py:177`
- `routes/gallery/gallery_routes.py:225`
- `routes/gallery/gallery_routes.py:2946`
- `tests/test_gallery_heavy_image_ops.py:43`
- `tests/test_gallery_heavy_image_ops.py:49`
- `tests/test_gallery_heavy_image_ops.py:55`

## `_remote_image_ops_base` — function, line 88
- **called from:**
- `routes/gallery/gallery_routes.py:130`
- `routes/gallery/gallery_routes.py:175`
- `routes/gallery/gallery_routes.py:223`

## `_outpaint_timeout` — function, line 92
- **called from:**
- `routes/gallery/gallery_routes.py:2214`
- `tests/test_gallery_seneca_image_ops.py:201`
- `tests/test_gallery_seneca_image_ops.py:203`

## `_unload_image_models` — function, line 105
- **called from:**
- `routes/gallery/gallery_routes.py:2820`
- `routes/gallery/gallery_routes.py:2902`

## `_route_heavy_image_op` — function (async), line 122
- **called from:**
- `routes/gallery/gallery_routes.py:2529`
- `routes/gallery/gallery_routes.py:2582`
- `tests/test_gallery_heavy_image_ops.py:64`

## `_xywh_to_xyxy` — function, line 158
- **called from:**
- `routes/gallery/gallery_routes.py:278`

## `_remote_remove_background` — function (async), line 167
- **called from:**
- `routes/gallery/gallery_routes.py:2846`

## `_remote_smart_mask` — function (async), line 215
- **called from:**
- `routes/gallery/gallery_routes.py:2706`

## `_b64_to_pil_image` — function, line 294
- **called from:**
- `routes/gallery/gallery_routes.py:2509`
- `routes/gallery/gallery_routes.py:2544`
- `routes/gallery/gallery_routes.py:2596`
- `routes/gallery/gallery_routes.py:2709`
- `routes/gallery/gallery_routes.py:2853`
- `routes/gallery/gallery_routes.py:2942`

## `_b64_bytes` — function, line 310
- **called from:**
- `routes/gallery/gallery_routes.py:180`
- `routes/gallery/gallery_routes.py:183`
- `routes/gallery/gallery_routes.py:228`
- `routes/gallery/gallery_routes.py:358`
- `routes/gallery/gallery_routes.py:361`
- `routes/gallery/gallery_routes.py:1851`
- `routes/gallery/gallery_routes.py:1854`
- `routes/gallery/gallery_routes.py:2860`
- `tests/test_agent_editor_routes.py:448`
- `tests/test_agent_editor_routes.py:449`
- `tests/test_agent_editor_routes.py:453`

## `_json_object` — function (async), line 327
- **called from:**
- `routes/editor_agent_routes.py:1431`
- `routes/editor_agent_routes.py:1536`
- `routes/editor_agent_routes.py:1604`
- `routes/editor_agent_routes.py:1628`
- `routes/editor_agent_routes.py:1697`
- `routes/editor_agent_routes.py:2088`
- `routes/gallery/gallery_routes.py:338`
- `routes/gallery/gallery_routes.py:3017`

## `_image_ids` — function (async), line 337
- **called from:**
- `routes/gallery/gallery_routes.py:3062`
- `routes/gallery/gallery_routes.py:3079`

## `_pil_image_to_b64` — function, line 344
- **called from:**
- `routes/gallery/gallery_routes.py:2812`

## `_prepare_local_edit` — function, line 350
- **called from:**
- `tests/test_image_op_offload.py:22`
- `tests/test_image_op_offload.py:30`

## `_restore_local_b64` — function, line 384
- **called from:**
- `tests/test_image_op_offload.py:36`
- `tests/test_image_op_offload.py:39`

## `_load_sam_backend` — function, line 400
- **called from:**
- `routes/gallery/gallery_routes.py:2723`

## `_load_grounding_backend` — function, line 436
- **called from:**
- `routes/gallery/gallery_routes.py:495`

## `_model_input_to_device` — function, line 472
- **called from:**
- `routes/gallery/gallery_routes.py:486`

## `_model_inputs_to_device` — function, line 484
- **called from:**
- `routes/gallery/gallery_routes.py:506`
- `routes/gallery/gallery_routes.py:2751`
- `tests/test_gallery_model_input_device.py:24`

## `_ground_text_to_box` — function, line 491
- **called from:**
- `routes/gallery/gallery_routes.py:2716`

## `_current_user_is_admin` — function, line 550
- **called from:**
- `routes/session_routes.py:311`

## `_sanitize_gallery_filename` — function, line 563
- **called from:**
- `routes/gallery/gallery_routes.py:578`
- `tests/test_security_regressions.py:1179`
- `tests/test_security_regressions.py:1190`

## `_gallery_image_path` — function, line 574
- **called from:**
- `routes/email/email_routes.py:5742`
- `routes/gallery/gallery_routes.py:959`
- `routes/gallery/gallery_routes.py:1034`
- `routes/gallery/gallery_routes.py:1530`
- `routes/gallery/gallery_routes.py:1669`
- `routes/gallery/gallery_routes.py:3121`
- `tests/test_gallery_filename_confinement.py:26`
- `tests/test_gallery_filename_confinement.py:41`
- `tests/test_gallery_filename_confinement.py:55`
- `tests/test_gallery_filename_confinement.py:74`

## `_normalize_image_endpoint_base` — function, line 589
- **called from:**
- `routes/gallery/gallery_routes.py:705`
- `routes/gallery/gallery_routes.py:730`
- `tests/test_gallery_endpoint_matching.py:6`
- `tests/test_gallery_endpoint_matching.py:7`

## `_is_openai_api_base` — function, line 596
- **called from:**
- `routes/gallery/gallery_routes.py:1832`
- `routes/gallery/gallery_routes.py:2383`

## `_join_checked_gallery_endpoint` — function, line 620
- **called from:**
- `routes/gallery/gallery_routes.py:1938`
- `routes/gallery/gallery_routes.py:1940`
- `routes/gallery/gallery_routes.py:1942`
- `routes/gallery/gallery_routes.py:2082`
- `routes/gallery/gallery_routes.py:2125`
- `routes/gallery/gallery_routes.py:2449`

## `_visible_image_endpoint_query` — function, line 631
- **called from:**
- `routes/gallery/gallery_routes.py:641`

## `_first_visible_image_endpoint` — function, line 640
- **called from:**
- `routes/gallery/gallery_routes.py:776`
- `routes/gallery/gallery_routes.py:1083`
- `routes/gallery/gallery_routes.py:1127`
- `routes/gallery/gallery_routes.py:1808`
- `routes/gallery/gallery_routes.py:2256`
- `routes/gallery/gallery_routes.py:2331`
- `tests/test_gallery_image_endpoint_fallback.py:83`
- `tests/test_gallery_image_endpoint_fallback.py:93`
- `tests/test_gallery_image_endpoint_fallback.py:103`
- `tests/test_gallery_image_endpoint_owner_scope.py:82`
- `tests/test_gallery_image_endpoint_owner_scope.py:89`

## `_first_mixed_image_endpoint` — function, line 656
- **called from:**
- `routes/gallery/gallery_routes.py:653`

## `_visible_image_endpoint_for_base` — function, line 703
- **called from:**
- `routes/gallery/gallery_routes.py:772`
- `routes/gallery/gallery_routes.py:1821`
- `routes/gallery/gallery_routes.py:2248`
- `routes/gallery/gallery_routes.py:2252`
- `routes/gallery/gallery_routes.py:2344`
- `tests/test_editor_model_discovery.py:172`
- `tests/test_editor_model_discovery.py:176`
- `tests/test_editor_model_discovery.py:180`
- `tests/test_gallery_endpoint_enforcement.py:412`
- `tests/test_gallery_endpoint_enforcement.py:417`
- `tests/test_gallery_endpoint_enforcement.py:442`
- `tests/test_gallery_image_endpoint_owner_scope.py:100`
- `tests/test_gallery_image_endpoint_owner_scope.py:111`
- `tests/test_gallery_image_endpoint_owner_scope.py:123`

## `_fetch_result_image_b64` — function (async), line 739
- **called from:**
- `routes/gallery/gallery_routes.py:838`
- `routes/gallery/gallery_routes.py:1969`
- `routes/gallery/gallery_routes.py:2093`
- `routes/gallery/gallery_routes.py:2483`
- `tests/test_gallery_result_image_ssrf.py:56`
- `tests/test_gallery_result_image_ssrf.py:68`

## `_resolve_image_op_endpoint` — function, line 765
- **called from:**
- `routes/gallery/gallery_routes.py:2166`

## `_forward_seneca_image_op` — function (async), line 785
- **called from:**
- `routes/gallery/gallery_routes.py:2190`
- `routes/gallery/gallery_routes.py:2212`

## `setup_gallery_routes` — function, line 854
- **called from:**
- `app.py:856`
- `tests/test_editor_generation_model_routing.py:111`
- `tests/test_editor_generation_model_routing.py:329`
- `tests/test_editor_generation_model_routing.py:384`
- `tests/test_editor_generation_model_routing.py:437`
- `tests/test_gallery_album_input.py:10`
- `tests/test_gallery_cloud_inpaint.py:72`
- `tests/test_gallery_cloud_inpaint.py:119`
- `tests/test_gallery_cloud_inpaint.py:184`
- `tests/test_gallery_cloud_inpaint.py:292`
- `tests/test_gallery_delete_file_ordering.py:22`
- `tests/test_gallery_edit_progress.py:18`
- `tests/test_gallery_endpoint_enforcement.py:84`
- `tests/test_gallery_endpoint_enforcement.py:125`
- `tests/test_gallery_endpoint_enforcement.py:166`
- `tests/test_gallery_endpoint_enforcement.py:208`
- `tests/test_gallery_endpoint_enforcement.py:254`
- `tests/test_gallery_endpoint_enforcement.py:327`
- `tests/test_gallery_endpoint_enforcement.py:370`
- `tests/test_gallery_filename_confinement.py:118`
- `tests/test_gallery_heavy_image_ops.py:38`
- `tests/test_gallery_heavy_image_ops.py:82`
- `tests/test_gallery_heavy_image_ops.py:117`
- `tests/test_gallery_image_bad_input.py:15`
- `tests/test_gallery_null_user_routes.py:61`
- `tests/test_gallery_search_multiword.py:82`
- `tests/test_gallery_seneca_image_ops.py:22`

## `gallery_upload` — function (async), line 859
- **route:** `POST /api/gallery/upload`
- decorator: `router.post("/api/gallery/upload")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_replace` — function (async), line 941
- **route:** `POST /api/gallery/{image_id}/replace`
- decorator: `router.post("/api/gallery/{image_id}/replace")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_rename` — function (async), line 984
- **route:** `POST /api/gallery/{image_id}/rename`
- decorator: `router.post("/api/gallery/{image_id}/rename")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_rotate` — function (async), line 1010
- **route:** `POST /api/gallery/{image_id}/rotate`
- decorator: `router.post("/api/gallery/{image_id}/rotate")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_ai_upscale` — function (async), line 1067
- **route:** `POST /api/gallery/ai-upscale`
- decorator: `router.post("/api/gallery/ai-upscale")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_style_transfer` — function (async), line 1111
- **route:** `POST /api/gallery/style-transfer`
- decorator: `router.post("/api/gallery/style-transfer")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_tags` — function (async), line 1158
- **route:** `GET /api/gallery/tags`
- decorator: `router.get("/api/gallery/tags")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_library` — function (async), line 1180
- **route:** `GET /api/gallery/library`
- decorator: `router.get("/api/gallery/library")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_albums` — function (async), line 1323
- **route:** `GET /api/gallery/albums`
- decorator: `router.get("/api/gallery/albums")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_album` — function (async), line 1361
- **route:** `POST /api/gallery/albums`
- decorator: `router.post("/api/gallery/albums")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_stats` — function (async), line 1382
- **route:** `GET /api/gallery/stats`
- decorator: `router.get("/api/gallery/stats")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ai_tag_batch` — function (async), line 1408
- **route:** `POST /api/gallery/ai-tag-batch`
- decorator: `router.post("/api/gallery/ai-tag-batch")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_gallery_image` — function (async), line 1431
- **route:** `GET /api/gallery/{image_id}`
- decorator: `router.get("/api/gallery/{image_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `patch_gallery_image` — function (async), line 1452
- **route:** `PATCH /api/gallery/{image_id}`
- decorator: `router.patch("/api/gallery/{image_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_download_zip` — function (async), line 1504
- **route:** `POST /api/gallery/download-zip`
- decorator: `router.post("/api/gallery/download-zip")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `clear_gallery_user_tags` — function (async), line 1559
- **route:** `POST /api/gallery/clear-user-tags`
- decorator: `router.post("/api/gallery/clear-user-tags")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `clear_gallery_ai_tags` — function (async), line 1584
- **route:** `POST /api/gallery/clear-ai-tags`
- decorator: `router.post("/api/gallery/clear-ai-tags")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `dedupe_gallery_tags` — function (async), line 1611
- **route:** `POST /api/gallery/dedupe-tags`
- decorator: `router.post("/api/gallery/dedupe-tags")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_gallery_image` — function (async), line 1647
- **route:** `DELETE /api/gallery/{image_id}`
- decorator: `router.delete("/api/gallery/{image_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `inpaint_proxy` — function (async), line 1768
- **route:** `POST /api/image/inpaint`
- decorator: `router.post("/api/image/inpaint")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_restore_b64` — function (async), line 2048
- **called from:**
- `routes/gallery/gallery_routes.py:2091`
- `routes/gallery/gallery_routes.py:2095`
- `routes/gallery/gallery_routes.py:2097`

## `_finish` — function, line 2067
- **called from:**
- `routes/gallery/gallery_routes.py:2091`
- `routes/gallery/gallery_routes.py:2095`
- `routes/gallery/gallery_routes.py:2097`
- `src/containment.py:1199`

## `_resolve_and_decode` — function (async), line 2148
- **called from:**
- `routes/gallery/gallery_routes.py:2177`
- `routes/gallery/gallery_routes.py:2200`

## `replace_background` — function (async), line 2173
- **route:** `POST /api/image/replace-background`
- decorator: `router.post("/api/image/replace-background")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `outpaint` — function (async), line 2196
- **route:** `POST /api/image/outpaint`
- decorator: `router.post("/api/image/outpaint")`
- **called from:**
- `routes/gallery/gallery_routes.py:2220`

## `outpaint_extend` — function (async), line 2218
- **route:** `POST /api/image/extend`
- decorator: `router.post("/api/image/extend")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `edit_progress` — function (async), line 2223
- **route:** `GET /api/image/edit-progress`
- decorator: `router.get("/api/image/edit-progress")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `harmonize_image` — function (async), line 2299
- **route:** `POST /api/image/harmonize`
- decorator: `router.post("/api/image/harmonize")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `sharpen_image` — function (async), line 2499
- **route:** `POST /api/image/sharpen`
- decorator: `router.post("/api/image/sharpen")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `denoise_image` — function (async), line 2523
- **route:** `POST /api/image/denoise`
- decorator: `router.post("/api/image/denoise")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `upscale_image_local` — function (async), line 2576
- **route:** `POST /api/image/upscale-local`
- decorator: `router.post("/api/image/upscale-local")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `generate_image` — function (async), line 2624
- **route:** `POST /api/image/generate`
- decorator: `router.post("/api/image/generate")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `smart_mask` — function (async), line 2697
- **route:** `POST /api/image/mask`
- decorator: `router.post("/api/image/mask")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `remove_background` — function (async), line 2829
- **route:** `POST /api/image/remove-bg`
- decorator: `router.post("/api/image/remove-bg")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `enhance_face` — function (async), line 2930
- **route:** `POST /api/image/enhance-face`
- decorator: `router.post("/api/image/enhance-face")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_get_or_404_album` — function, line 2998
- **called from:**
- `routes/gallery/gallery_routes.py:878`
- `routes/gallery/gallery_routes.py:1483`
- `routes/gallery/gallery_routes.py:3028`
- `routes/gallery/gallery_routes.py:3048`
- `routes/gallery/gallery_routes.py:3065`
- `routes/gallery/gallery_routes.py:3082`

## `_get_or_404_image` — function, line 3006
- **called from:**
- `routes/gallery/gallery_routes.py:3036`
- `routes/gallery/gallery_routes.py:3101`
- `routes/gallery/gallery_routes.py:3119`

## `update_album` — function (async), line 3015
- **route:** `PUT /api/gallery/albums/{album_id}`
- decorator: `router.put("/api/gallery/albums/{album_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_album` — function (async), line 3044
- **route:** `DELETE /api/gallery/albums/{album_id}`
- decorator: `router.delete("/api/gallery/albums/{album_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_to_album` — function (async), line 3060
- **route:** `POST /api/gallery/albums/{album_id}/add`
- decorator: `router.post("/api/gallery/albums/{album_id}/add")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `remove_from_album` — function (async), line 3077
- **route:** `POST /api/gallery/albums/{album_id}/remove`
- decorator: `router.post("/api/gallery/albums/{album_id}/remove")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_favorite` — function (async), line 3097
- **route:** `POST /api/gallery/{image_id}/favorite`
- decorator: `router.post("/api/gallery/{image_id}/favorite")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ai_tag_image` — function (async), line 3111
- **route:** `POST /api/gallery/{image_id}/ai-tag`
- decorator: `router.post("/api/gallery/{image_id}/ai-tag")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
