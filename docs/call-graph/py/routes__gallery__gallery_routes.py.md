# `routes/gallery/gallery_routes.py` — definitions & call sites

53 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_b64_to_pil_image` — function, line 36
- **called from:**
- `routes/gallery/gallery_routes.py:1847`

## `_pil_image_to_b64` — function, line 52
- **called from:**
- `routes/gallery/gallery_routes.py:1949`

## `_load_sam_backend` — function, line 58
- **called from:**
- `routes/gallery/gallery_routes.py:1860`

## `_load_grounding_backend` — function, line 94
- **called from:**
- `routes/gallery/gallery_routes.py:153`

## `_model_input_to_device` — function, line 130
- **called from:**
- `routes/gallery/gallery_routes.py:144`

## `_model_inputs_to_device` — function, line 142
- **called from:**
- `routes/gallery/gallery_routes.py:164`
- `routes/gallery/gallery_routes.py:1888`
- `tests/test_gallery_model_input_device.py:24`

## `_ground_text_to_box` — function, line 149
- **called from:**
- `routes/gallery/gallery_routes.py:1854`

## `_current_user_is_admin` — function, line 208
- **called from:**
- `routes/session_routes.py:201`

## `_sanitize_gallery_filename` — function, line 221
- **called from:**
- `routes/gallery/gallery_routes.py:236`
- `tests/test_security_regressions.py:1177`
- `tests/test_security_regressions.py:1188`

## `_gallery_image_path` — function, line 232
- **called from:**
- `routes/email_routes.py:4108`
- `routes/gallery/gallery_routes.py:453`
- `routes/gallery/gallery_routes.py:528`
- `routes/gallery/gallery_routes.py:1020`
- `routes/gallery/gallery_routes.py:1159`
- `routes/gallery/gallery_routes.py:2241`
- `tests/test_gallery_filename_confinement.py:26`
- `tests/test_gallery_filename_confinement.py:41`
- `tests/test_gallery_filename_confinement.py:55`
- `tests/test_gallery_filename_confinement.py:74`

## `_normalize_image_endpoint_base` — function, line 250
- **called from:**
- `routes/gallery/gallery_routes.py:309`
- `routes/gallery/gallery_routes.py:314`
- `tests/test_gallery_endpoint_matching.py:6`
- `tests/test_gallery_endpoint_matching.py:7`

## `_is_openai_api_base` — function, line 257
- **called from:**
- `routes/gallery/gallery_routes.py:1307`
- `routes/gallery/gallery_routes.py:1600`

## `_join_checked_gallery_endpoint` — function, line 279
- **called from:**
- `routes/gallery/gallery_routes.py:1377`
- `routes/gallery/gallery_routes.py:1456`
- `routes/gallery/gallery_routes.py:1496`
- `routes/gallery/gallery_routes.py:1666`

## `_visible_image_endpoint_query` — function, line 290
- **called from:**
- `routes/gallery/gallery_routes.py:300`
- `routes/gallery/gallery_routes.py:313`

## `_first_visible_image_endpoint` — function, line 299
- **called from:**
- `routes/gallery/gallery_routes.py:577`
- `routes/gallery/gallery_routes.py:621`
- `routes/gallery/gallery_routes.py:1283`
- `routes/gallery/gallery_routes.py:1548`
- `tests/test_gallery_image_endpoint_owner_scope.py:82`
- `tests/test_gallery_image_endpoint_owner_scope.py:89`

## `_visible_image_endpoint_for_base` — function, line 308
- **called from:**
- `routes/gallery/gallery_routes.py:1296`
- `routes/gallery/gallery_routes.py:1561`
- `tests/test_gallery_image_endpoint_owner_scope.py:100`
- `tests/test_gallery_image_endpoint_owner_scope.py:111`
- `tests/test_gallery_image_endpoint_owner_scope.py:123`

## `_fetch_result_image_b64` — function (async), line 322
- **called from:**
- `routes/gallery/gallery_routes.py:1389`
- `routes/gallery/gallery_routes.py:1464`
- `routes/gallery/gallery_routes.py:1700`
- `tests/test_gallery_result_image_ssrf.py:56`
- `tests/test_gallery_result_image_ssrf.py:68`

## `setup_gallery_routes` — function, line 348
- **called from:**
- `app.py:776`
- `tests/test_gallery_delete_file_ordering.py:22`
- `tests/test_gallery_filename_confinement.py:118`
- `tests/test_gallery_null_user_routes.py:61`

## `gallery_upload` — function (async), line 353
- **route:** `POST /api/gallery/upload`
- decorator: `router.post("/api/gallery/upload")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_replace` — function (async), line 435
- **route:** `POST /api/gallery/{image_id}/replace`
- decorator: `router.post("/api/gallery/{image_id}/replace")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_rename` — function (async), line 478
- **route:** `POST /api/gallery/{image_id}/rename`
- decorator: `router.post("/api/gallery/{image_id}/rename")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_rotate` — function (async), line 504
- **route:** `POST /api/gallery/{image_id}/rotate`
- decorator: `router.post("/api/gallery/{image_id}/rotate")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_ai_upscale` — function (async), line 561
- **route:** `POST /api/gallery/ai-upscale`
- decorator: `router.post("/api/gallery/ai-upscale")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_style_transfer` — function (async), line 605
- **route:** `POST /api/gallery/style-transfer`
- decorator: `router.post("/api/gallery/style-transfer")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_tags` — function (async), line 652
- **route:** `GET /api/gallery/tags`
- decorator: `router.get("/api/gallery/tags")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_library` — function (async), line 674
- **route:** `GET /api/gallery/library`
- decorator: `router.get("/api/gallery/library")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_albums` — function (async), line 813
- **route:** `GET /api/gallery/albums`
- decorator: `router.get("/api/gallery/albums")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_album` — function (async), line 851
- **route:** `POST /api/gallery/albums`
- decorator: `router.post("/api/gallery/albums")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_stats` — function (async), line 872
- **route:** `GET /api/gallery/stats`
- decorator: `router.get("/api/gallery/stats")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ai_tag_batch` — function (async), line 898
- **route:** `POST /api/gallery/ai-tag-batch`
- decorator: `router.post("/api/gallery/ai-tag-batch")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_gallery_image` — function (async), line 921
- **route:** `GET /api/gallery/{image_id}`
- decorator: `router.get("/api/gallery/{image_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `patch_gallery_image` — function (async), line 942
- **route:** `PATCH /api/gallery/{image_id}`
- decorator: `router.patch("/api/gallery/{image_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gallery_download_zip` — function (async), line 994
- **route:** `POST /api/gallery/download-zip`
- decorator: `router.post("/api/gallery/download-zip")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `clear_gallery_user_tags` — function (async), line 1049
- **route:** `POST /api/gallery/clear-user-tags`
- decorator: `router.post("/api/gallery/clear-user-tags")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `clear_gallery_ai_tags` — function (async), line 1074
- **route:** `POST /api/gallery/clear-ai-tags`
- decorator: `router.post("/api/gallery/clear-ai-tags")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `dedupe_gallery_tags` — function (async), line 1101
- **route:** `POST /api/gallery/dedupe-tags`
- decorator: `router.post("/api/gallery/dedupe-tags")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_gallery_image` — function (async), line 1137
- **route:** `DELETE /api/gallery/{image_id}`
- decorator: `router.delete("/api/gallery/{image_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `inpaint_proxy` — function (async), line 1258
- **route:** `POST /api/image/inpaint`
- decorator: `router.post("/api/image/inpaint")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `harmonize_image` — function (async), line 1516
- **route:** `POST /api/image/harmonize`
- decorator: `router.post("/api/image/harmonize")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `sharpen_image` — function (async), line 1716
- **route:** `POST /api/image/sharpen`
- decorator: `router.post("/api/image/sharpen")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `denoise_image` — function (async), line 1741
- **route:** `POST /api/image/denoise`
- decorator: `router.post("/api/image/denoise")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `upscale_image_local` — function (async), line 1792
- **route:** `POST /api/image/upscale-local`
- decorator: `router.post("/api/image/upscale-local")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `smart_mask` — function (async), line 1838
- **route:** `POST /api/image/mask`
- decorator: `router.post("/api/image/mask")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `remove_background` — function (async), line 1964
- **route:** `POST /api/image/remove-bg`
- decorator: `router.post("/api/image/remove-bg")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `enhance_face` — function (async), line 2057
- **route:** `POST /api/image/enhance-face`
- decorator: `router.post("/api/image/enhance-face")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_get_or_404_album` — function, line 2124
- **called from:**
- `routes/gallery/gallery_routes.py:372`
- `routes/gallery/gallery_routes.py:973`
- `routes/gallery/gallery_routes.py:2146`
- `routes/gallery/gallery_routes.py:2166`
- `routes/gallery/gallery_routes.py:2184`
- `routes/gallery/gallery_routes.py:2202`

## `_get_or_404_image` — function, line 2132
- **called from:**
- `routes/gallery/gallery_routes.py:2154`
- `routes/gallery/gallery_routes.py:2221`
- `routes/gallery/gallery_routes.py:2239`

## `update_album` — function (async), line 2141
- **route:** `PUT /api/gallery/albums/{album_id}`
- decorator: `router.put("/api/gallery/albums/{album_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_album` — function (async), line 2162
- **route:** `DELETE /api/gallery/albums/{album_id}`
- decorator: `router.delete("/api/gallery/albums/{album_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_to_album` — function (async), line 2178
- **route:** `POST /api/gallery/albums/{album_id}/add`
- decorator: `router.post("/api/gallery/albums/{album_id}/add")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `remove_from_album` — function (async), line 2196
- **route:** `POST /api/gallery/albums/{album_id}/remove`
- decorator: `router.post("/api/gallery/albums/{album_id}/remove")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_favorite` — function (async), line 2217
- **route:** `POST /api/gallery/{image_id}/favorite`
- decorator: `router.post("/api/gallery/{image_id}/favorite")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ai_tag_image` — function (async), line 2231
- **route:** `POST /api/gallery/{image_id}/ai-tag`
- decorator: `router.post("/api/gallery/{image_id}/ai-tag")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
