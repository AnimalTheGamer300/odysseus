# `src/document_processor.py` — definitions & call sites

22 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_text_file` — function, line 26
- **called from:**
- `services/memory/skill_importer.py:421`
- `src/document_processor.py:388`
- `src/document_processor.py:996`
- `tests/test_nix_upload_text.py:9`

## `_process_text_file` — function, line 36
- **called from:**
- `src/document_processor.py:389`
- `src/document_processor.py:997`
- `tests/test_nix_upload_text.py:16`

## `_process_pdf` — function, line 121
- **called from:**
- `routes/document/document_routes.py:280`
- `routes/document/document_routes.py:746`
- `routes/memory/memory_routes.py:398`
- `src/document_processor.py:383`
- `src/document_processor.py:910`
- `src/document_processor.py:993`
- `tests/test_pdf_cmyk_image_analysis.py:55`
- `tests/test_pdf_cmyk_image_analysis.py:75`
- `tests/test_pdf_cmyk_image_analysis.py:97`

## `_truncate_inline` — function, line 176
- **called from:**
- `src/document_processor.py:246`
- `src/document_processor.py:351`

## `_fit_inline_attachment_text` — function, line 184
- **called from:**
- `src/document_processor.py:1007`

## `_process_office_document` — function, line 219
- **called from:**
- `src/document_processor.py:390`
- `src/document_processor.py:999`

## `_process_legacy_word_document` — function, line 309
- **called from:**
- `src/document_processor.py:381`
- `src/document_processor.py:995`
- `src/personal_docs.py:39`

## `extract_local_document` — function, line 364
- **called from:**
- `src/agent_tools/filesystem_tools.py:305`
- `src/media_ingress.py:317`
- `tests/test_document_pdf_marker.py:49`
- `tests/test_document_processor_text_formats.py:28`
- `tests/test_document_processor_text_formats.py:55`
- `tests/test_legacy_word_reader.py:25`
- `tests/test_legacy_word_reader.py:50`
- `tests/test_pdf_cmyk_image_analysis.py:85`

## `strip_pdf_content_marker` — function, line 397
- **called from:**
- `routes/document/document_routes.py:280`
- `routes/document/document_routes.py:746`
- `src/document_processor.py:910`
- `tests/test_document_pdf_marker.py:15`
- `tests/test_document_pdf_marker.py:27`
- `tests/test_document_pdf_marker.py:31`

## `_load_vl_settings` — function, line 409
- **called from:**
- `routes/document/document_routes.py:1500`
- `routes/gallery/gallery_routes.py:3134`
- `src/document_processor.py:449`

## `_resolve_vl_model` — function, line 418
- **called from:**
- `routes/document/document_routes.py:1503`
- `routes/gallery/gallery_routes.py:3139`
- `src/document_processor.py:455`
- `tests/test_vision_owner_scope.py:19`
- `tests/test_vision_owner_scope.py:38`

## `analyze_image_with_vl_result` — function, line 445
- **called from:**
- `src/chat_handler.py:283`
- `src/document_processor.py:541`
- `tests/test_vision_owner_scope.py:73`

## `analyze_image_with_vl` — function, line 539
- **called from:**
- `routes/upload_routes.py:602`
- `src/document_processor.py:153`

## `_vision_max_side` — function, line 544
- **called from:**
- `src/document_processor.py:561`

## `encode_image_data_url` — function, line 553
- **called from:**
- `src/document_processor.py:845`
- `tests/test_vision_inline.py:89`
- `tests/test_vision_inline.py:102`

## `_gif_sample_config` — function, line 587
- **called from:**
- `src/document_processor.py:627`
- `tests/test_gif_video_frames.py:87`
- `tests/test_gif_video_frames.py:97`
- `tests/test_gif_video_frames.py:99`
- `tests/test_gif_video_frames.py:101`
- `tests/test_gif_video_frames.py:103`

## `_gif_frames_as_jpeg` — function, line 611
- **called from:**
- `src/document_processor.py:465`
- `src/document_processor.py:837`
- `tests/test_gif_video_frames.py:107`
- `tests/test_gif_video_frames.py:114`
- `tests/test_gif_video_frames.py:120`

## `_video_sample_config` — function, line 667
- **called from:**
- `src/document_processor.py:747`
- `tests/test_gif_video_frames.py:124`

## `_probe_video_duration` — function, line 691
- **called from:**
- `src/document_processor.py:749`

## `_split_jpeg_stream` — function, line 709
- **called from:**
- `src/document_processor.py:770`
- `tests/test_gif_video_frames.py:151`

## `_video_frames_as_jpeg` — function, line 733
- **called from:**
- `src/document_processor.py:467`
- `src/document_processor.py:860`
- `tests/test_gif_video_frames.py:131`
- `tests/test_gif_video_frames.py:139`
- `tests/test_gif_video_frames.py:146`

## `build_user_content` — function, line 781
- **called from:**
- `src/chat_handler.py:309`
- `tests/test_build_user_content_pdf_marker.py:43`
- `tests/test_build_user_content_pdf_marker.py:83`
- `tests/test_document_processor_attachment_budget.py:45`
- `tests/test_document_processor_attachment_budget.py:70`
- `tests/test_document_processor_empty_media_subtype.py:46`
- `tests/test_document_processor_empty_media_subtype.py:59`
- `tests/test_document_processor_empty_media_subtype.py:72`
- `tests/test_gif_video_frames.py:177`
- `tests/test_gif_video_frames.py:195`
- `tests/test_security_regressions.py:383`
