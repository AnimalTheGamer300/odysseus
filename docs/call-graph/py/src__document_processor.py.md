# `src/document_processor.py` — definitions & call sites

18 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_text_file` — function, line 25
- **called from:**
- `services/memory/skill_importer.py:421`
- `src/document_processor.py:862`
- `tests/test_nix_upload_text.py:9`

## `_process_text_file` — function, line 33
- **called from:**
- `src/document_processor.py:863`
- `tests/test_nix_upload_text.py:16`

## `_process_pdf` — function, line 118
- **called from:**
- `routes/document/document_routes.py:275`
- `routes/document/document_routes.py:530`
- `routes/memory/memory_routes.py:394`
- `src/document_processor.py:778`
- `src/document_processor.py:861`

## `_truncate_inline` — function, line 165
- **called from:**
- `src/document_processor.py:235`

## `_fit_inline_attachment_text` — function, line 173
- **called from:**
- `src/document_processor.py:873`

## `_process_office_document` — function, line 208
- **called from:**
- `src/document_processor.py:865`

## `strip_pdf_content_marker` — function, line 291
- **called from:**
- `routes/document/document_routes.py:275`
- `routes/document/document_routes.py:530`
- `src/document_processor.py:778`
- `tests/test_document_pdf_marker.py:14`
- `tests/test_document_pdf_marker.py:26`
- `tests/test_document_pdf_marker.py:30`

## `_load_vl_settings` — function, line 303
- **called from:**
- `routes/document/document_routes.py:1276`
- `routes/gallery/gallery_routes.py:2254`
- `src/document_processor.py:343`

## `_resolve_vl_model` — function, line 312
- **called from:**
- `routes/document/document_routes.py:1279`
- `routes/gallery/gallery_routes.py:2259`
- `src/document_processor.py:349`
- `tests/test_vision_owner_scope.py:19`
- `tests/test_vision_owner_scope.py:38`

## `analyze_image_with_vl_result` — function, line 339
- **called from:**
- `src/chat_handler.py:273`
- `src/document_processor.py:435`
- `tests/test_vision_owner_scope.py:73`

## `analyze_image_with_vl` — function, line 433
- **called from:**
- `routes/upload_routes.py:484`
- `src/document_processor.py:142`

## `_gif_sample_config` — function, line 438
- **called from:**
- `src/document_processor.py:478`
- `tests/test_gif_video_frames.py:87`
- `tests/test_gif_video_frames.py:97`
- `tests/test_gif_video_frames.py:99`
- `tests/test_gif_video_frames.py:101`
- `tests/test_gif_video_frames.py:103`

## `_gif_frames_as_jpeg` — function, line 462
- **called from:**
- `src/document_processor.py:359`
- `src/document_processor.py:684`
- `tests/test_gif_video_frames.py:107`
- `tests/test_gif_video_frames.py:114`
- `tests/test_gif_video_frames.py:120`

## `_video_sample_config` — function, line 518
- **called from:**
- `src/document_processor.py:598`
- `tests/test_gif_video_frames.py:124`

## `_probe_video_duration` — function, line 542
- **called from:**
- `src/document_processor.py:600`

## `_split_jpeg_stream` — function, line 560
- **called from:**
- `src/document_processor.py:621`
- `tests/test_gif_video_frames.py:151`

## `_video_frames_as_jpeg` — function, line 584
- **called from:**
- `src/document_processor.py:361`
- `src/document_processor.py:728`
- `tests/test_gif_video_frames.py:131`
- `tests/test_gif_video_frames.py:139`
- `tests/test_gif_video_frames.py:146`

## `build_user_content` — function, line 631
- **called from:**
- `src/chat_handler.py:293`
- `tests/test_build_user_content_pdf_marker.py:43`
- `tests/test_build_user_content_pdf_marker.py:83`
- `tests/test_document_processor_attachment_budget.py:45`
- `tests/test_document_processor_attachment_budget.py:70`
- `tests/test_document_processor_empty_media_subtype.py:46`
- `tests/test_document_processor_empty_media_subtype.py:59`
- `tests/test_document_processor_empty_media_subtype.py:72`
- `tests/test_gif_video_frames.py:177`
- `tests/test_gif_video_frames.py:195`
- `tests/test_security_regressions.py:382`
