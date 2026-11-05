# `src/upload_handler.py` — definitions & call sites

43 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `secure_filename` — function, line 20
- **called from:**
- `routes/personal_routes.py:26`
- `routes/personal_routes.py:35`
- `routes/upload_routes.py:163`
- `routes/upload_routes.py:463`
- `routes/upload_routes.py:544`
- `src/upload_handler.py:1322`

## `UploadCleanupSafetyError` — class, line 50
- **called from:**
- `src/upload_handler.py:708`
- `src/upload_handler.py:742`
- `src/upload_handler.py:763`

## `_pdf_source_upload_ids` — function, line 84
- **called from:**
- `src/upload_handler.py:174`
- `tests/test_codeql_python_residual_followup.py:50`

## `_attachment_reference_ids` — function, line 110
- **called from:**
- `src/upload_handler.py:175`
- `tests/test_codeql_python_residual_followup.py:65`

## `is_valid_upload_id` — function, line 140
- **called from:**
- `src/pdf_form_doc.py:186`
- `src/upload_handler.py:209`
- `src/upload_handler.py:767`
- `tests/test_upload_id_extension.py:26`
- `tests/test_upload_id_extension.py:36`
- `tests/test_upload_id_validation.py:10`
- `tests/test_upload_id_validation.py:14`
- `tests/test_upload_id_validation.py:18`
- `tests/test_upload_id_validation.py:19`
- `tests/test_upload_id_validation.py:20`
- `tests/test_upload_id_validation.py:21`

## `extract_upload_ids` — function, line 145
- **called from:**
- `routes/upload_routes.py:51`

## `extract_internal_upload_ids` — function, line 152
- **called from:**
- `src/upload_handler.py:163`
- `src/upload_handler.py:168`
- `src/upload_handler.py:194`
- `src/upload_handler.py:232`
- `src/upload_handler.py:238`
- `tests/test_codeql_python_residual_followup.py:78`
- `tests/test_upload_handler_cleanup.py:574`
- `tests/test_upload_handler_cleanup.py:575`
- `tests/test_upload_handler_cleanup.py:576`
- `tests/test_upload_handler_cleanup.py:580`
- `tests/test_upload_handler_cleanup.py:583`
- `tests/test_upload_handler_cleanup.py:587`
- `tests/test_upload_handler_cleanup.py:590`
- `tests/test_upload_handler_cleanup.py:593`

## `reserve_upload_references` — function, line 179
- **called from:**
- `routes/calendar_routes.py:958`
- `routes/document/document_routes.py:88`
- `routes/note/note_routes.py:604`
- `src/agent_tools/document_tools.py:49`
- `src/tools/calendar.py:601`
- `src/tools/calendar.py:700`
- `src/tools/notes.py:377`
- `src/tools/notes.py:449`
- `tests/test_upload_handler_cleanup.py:606`
- `tests/test_upload_handler_cleanup.py:611`

## `reserve_upload_ids` — function, line 198
- **called from:**
- `src/upload_handler.py:195`
- `src/upload_handler.py:246`

## `reserve_message_upload_references` — function, line 225
- **called from:**
- `core/session_manager.py:379`
- `core/session_manager.py:390`
- `core/session_manager.py:545`
- `core/session_manager.py:685`
- `routes/history/history_routes.py:284`
- `routes/session_routes.py:893`
- `tests/test_upload_handler_cleanup.py:622`

## `_build_upload_id` — function, line 249
- **called from:**
- `src/upload_handler.py:1428`
- `tests/test_upload_id_extension.py:25`
- `tests/test_upload_id_extension.py:30`
- `tests/test_upload_id_extension.py:31`
- `tests/test_upload_id_extension.py:35`

## `count_recent_uploads` — function, line 263
- **called from:**
- `routes/upload_routes.py:379`
- `tests/test_upload_multifile.py:37`
- `tests/test_upload_multifile.py:39`
- `tests/test_upload_multifile.py:40`
- `tests/test_upload_multifile.py:41`

## `UploadHandler` — class, line 275
- **called from:**
- `routes/document/document_helpers.py:179`
- `src/app_initializer.py:94`
- `tests/test_chat_upload_limit_config.py:58`
- `tests/test_gif_video_frames.py:158`
- `tests/test_nix_upload_text.py:6`
- `tests/test_rename_user_owner_sync.py:455`
- `tests/test_replace_messages_upload_reservations.py:194`
- `tests/test_security_regressions.py:370`
- `tests/test_security_regressions.py:381`
- `tests/test_security_regressions.py:406`
- `tests/test_security_regressions.py:439`
- `tests/test_security_regressions.py:463`
- `tests/test_security_regressions.py:498`
- `tests/test_upload_confinement_compatibility.py:135`
- `tests/test_upload_content_detection_magic.py:39`
- `tests/test_upload_handler_atomicity.py:56`
- `tests/test_upload_handler_atomicity.py:282`
- `tests/test_upload_handler_cleanup.py:56`
- `tests/test_upload_handler_rename_owner.py:13`
- `tests/test_upload_head_contract.py:65`
- `tests/test_upload_multifile.py:161`
- `tests/test_upload_multifile.py:190`
- `tests/test_upload_multifile.py:221`
- `tests/test_upload_no_login.py:36`
- `tests/test_upload_no_login.py:409`
- `tests/test_upload_no_login.py:490`
- `tests/test_upload_no_login.py:628`
- `tests/test_upload_no_login.py:727`
- `tests/test_upload_no_login.py:775`
- `tests/test_upload_no_login.py:815`
- `tests/test_upload_no_login.py:848`
- `tests/test_upload_routes_owner_scope.py:80`

## `UploadHandler.__init__` — method, line 276
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email/email_helpers.py:205`
- `routes/email/email_helpers.py:220`
- `routes/email/email_helpers.py:232`
- `routes/email/email_helpers.py:248`
- `routes/email/email_routes.py:1664`
- `scripts/css_snapshot.py:194`
- `scripts/probe_browser_budget.py:56`
- `src/agent_tools/document_tools.py:759`
- `src/agent_tools/filesystem_tools.py:384`
- `src/builtin_actions.py:552`
- `src/chatgpt_subscription.py:495`
- `src/containment.py:170`
- `src/outbound_fetch.py:220`
- `src/path_confinement.py:81`
- `src/process_ownership.py:110`
- `src/report_math.py:31`
- `tests/conftest.py:199`
- `tests/test_admin_routes_auth_disabled.py:16`
- `tests/test_agent_state_dir_confinement.py:799`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_action_planning.py:11`
- `tests/test_deep_research_browser_fallback.py:10`
- `tests/test_deep_research_browser_fallback.py:29`
- `tests/test_deep_research_browser_fallback.py:56`
- `tests/test_deep_research_extraction_controls.py:13`
- `tests/test_deep_research_full_loop_navigation.py:11`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_llm_core_streaming.py:50`
- `tests/test_retired_settings_interfaces.py:31`
- `tests/test_searxng_ca_validation.py:35`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:155`

## `UploadHandler.inside_base_dir` — method, line 319
- **called from:**
- `routes/chat_helpers.py:912`
- `src/document_processor.py:817`
- `tests/test_inside_base_dir_nonstring.py:11`
- `tests/test_inside_base_dir_nonstring.py:12`
- `tests/test_inside_base_dir_nonstring.py:13`
- `tests/test_inside_base_dir_nonstring.py:18`
- `tests/test_inside_base_dir_nonstring.py:19`
- `tests/test_upload_no_login.py:757`
- `tests/test_upload_no_login.py:831`

## `UploadHandler.get_upload_dir` — method, line 323
- **called from:**
- `src/upload_handler.py:1431`

## `UploadHandler.calculate_file_hash` — method, line 330
- **called from:**
- `src/upload_handler.py:1349`

## `UploadHandler.detect_content_type` — method, line 339
- **called from:**
- `src/upload_handler.py:1325`
- `tests/test_upload_content_detection_magic.py:45`

## `UploadHandler.is_image_file` — method, line 357
- **called from:**
- `routes/chat_routes.py:2046`
- `routes/upload_routes.py:264`
- `src/chat_handler.py:236`
- `src/clean_agent_preview.py:4070`
- `src/document_processor.py:825`
- `src/tools/image.py:122`

## `UploadHandler.is_document_file` — method, line 375
- **called from:**
- `src/document_processor.py:895`
- `tests/test_legacy_word_reader.py:59`
- `tests/test_legacy_word_reader.py:60`
- `tests/test_nix_upload_text.py:8`

## `UploadHandler.is_audio_file` — method, line 407
- **called from:**
- `src/document_processor.py:879`

## `UploadHandler.is_video_file` — method, line 425
- **called from:**
- `src/chat_handler.py:231`
- `src/document_processor.py:858`
- `src/upload_handler.py:1338`
- `tests/test_gif_video_frames.py:159`
- `tests/test_gif_video_frames.py:160`
- `tests/test_gif_video_frames.py:161`
- `tests/test_gif_video_frames.py:162`
- `tests/test_gif_video_frames.py:163`
- `tests/test_gif_video_frames.py:164`

## `UploadHandler.is_safe_file_type` — method, line 452
- **called from:**
- `src/upload_handler.py:1328`

## `UploadHandler._parse_upload_timestamp` — method, line 476
- decorator: `staticmethod`
- **called from:**
- `src/upload_handler.py:491`
- `src/upload_handler.py:566`
- `src/upload_handler.py:1034`

## `UploadHandler._upload_metadata_is_recent` — method, line 488
- decorator: `classmethod`
- **called from:**
- `src/upload_handler.py:678`

## `UploadHandler._upload_index_keys_for_file` — method, line 499
- decorator: `classmethod`
- **called from:**
- `src/upload_handler.py:654`

## `UploadHandler.cleanup_old_uploads` — method, line 587
- **called from:**
- `routes/upload_routes.py:147`
- `tests/test_upload_handler_cleanup.py:248`
- `tests/test_upload_handler_cleanup.py:276`
- `tests/test_upload_handler_cleanup.py:409`
- `tests/test_upload_handler_cleanup.py:466`

## `UploadHandler.validate_upload_id` — method, line 765
- **called from:**
- `routes/upload_routes.py:461`
- `routes/upload_routes.py:580`
- `routes/upload_routes.py:618`
- `src/upload_handler.py:644`
- `src/upload_handler.py:938`
- `src/upload_handler.py:959`
- `src/upload_handler.py:1174`

## `UploadHandler._inside_upload_dir` — method, line 769
- **called from:**
- `routes/chat_helpers.py:910`
- `src/document_processor.py:814`
- `src/upload_handler.py:627`
- `src/upload_handler.py:648`
- `src/upload_handler.py:1017`
- `src/upload_handler.py:1031`
- `src/upload_handler.py:1179`
- `src/upload_handler.py:1192`
- `src/upload_handler.py:1365`

## `UploadHandler._atomic_write_json` — method, line 773
- **called from:**
- `core/auth.py:175`
- `core/auth.py:240`
- `src/upload_handler.py:691`
- `src/upload_handler.py:698`
- `src/upload_handler.py:732`
- `src/upload_handler.py:1050`
- `src/upload_handler.py:1057`
- `src/upload_handler.py:1169`
- `src/upload_handler.py:1374`
- `src/upload_handler.py:1404`
- `src/upload_handler.py:1477`
- `tests/test_rename_user_owner_sync.py:456`
- `tests/test_upload_handler_atomicity.py:108`
- `tests/test_upload_handler_atomicity.py:254`
- `tests/test_upload_handler_atomicity.py:255`
- `tests/test_upload_handler_atomicity.py:278`
- `tests/test_upload_handler_atomicity.py:279`
- `tests/test_upload_handler_atomicity.py:294`
- `tests/test_upload_handler_atomicity.py:310`
- `tests/test_upload_handler_atomicity.py:457`
- `tests/test_upload_handler_atomicity.py:461`
- `tests/test_upload_handler_rename_owner.py:50`
- `tests/test_upload_handler_rename_owner.py:82`

## `UploadHandler._replace_json` — method, line 790
- **called from:**
- `src/upload_handler.py:810`
- `src/upload_handler.py:817`

## `UploadHandler._upload_index_signature` — method, line 826
- decorator: `staticmethod`
- **called from:**
- `src/upload_handler.py:821`
- `src/upload_handler.py:867`
- `src/upload_handler.py:903`
- `src/upload_handler.py:917`
- `src/upload_handler.py:933`

## `UploadHandler._load_upload_index` — method, line 857
- **called from:**
- `routes/upload_routes.py:470`
- `routes/upload_routes.py:540`
- `src/upload_handler.py:615`
- `src/upload_handler.py:940`
- `src/upload_handler.py:969`
- `src/upload_handler.py:1136`
- `src/upload_handler.py:1267`
- `src/upload_handler.py:1360`
- `src/upload_handler.py:1384`
- `src/upload_handler.py:1474`
- `tests/test_upload_handler_atomicity.py:262`
- `tests/test_upload_handler_atomicity.py:287`
- `tests/test_upload_handler_atomicity.py:301`
- `tests/test_upload_handler_atomicity.py:330`
- `tests/test_upload_no_login.py:663`
- `tests/test_upload_no_login.py:675`
- `tests/test_upload_no_login.py:750`
- `tests/test_upload_no_login.py:828`

## `UploadHandler.get_upload_info` — method, line 936
- **called from:**
- `tests/test_upload_handler_atomicity.py:380`
- `tests/test_upload_handler_atomicity.py:467`
- `tests/test_upload_handler_cleanup.py:195`
- `tests/test_upload_handler_cleanup.py:199`
- `tests/test_upload_handler_cleanup.py:202`
- `tests/test_upload_handler_cleanup.py:223`
- `tests/test_upload_handler_cleanup.py:386`
- `tests/test_upload_handler_cleanup.py:411`

## `UploadHandler.reserve_upload` — method, line 945
- **called from:**
- `src/upload_handler.py:213`
- `src/upload_handler.py:1219`
- `tests/test_upload_handler_cleanup.py:616`

## `UploadHandler._renamed_upload_index_key` — method, line 1083
- **called from:**
- `src/upload_handler.py:1150`

## `UploadHandler._unique_upload_index_key` — method, line 1103
- **called from:**
- `src/upload_handler.py:1151`

## `UploadHandler.rename_owner` — method, line 1120
- **called from:**
- `routes/auth_routes.py:533`
- `routes/auth_routes.py:579`
- `routes/personal_routes.py:110`
- `tests/test_rag_vector_rename_owner.py:66`
- `tests/test_rename_user_owner_sync.py:323`
- `tests/test_rename_user_owner_sync.py:337`
- `tests/test_upload_handler_rename_owner.py:58`
- `tests/test_upload_handler_rename_owner.py:91`

## `UploadHandler._find_upload_path` — method, line 1172
- **called from:**
- `src/upload_handler.py:1030`

## `UploadHandler.resolve_upload` — method, line 1204
- **called from:**
- `routes/chat_helpers.py:898`
- `routes/chat_routes.py:2037`
- `routes/document/document_helpers.py:152`
- `src/agent_runtime/owned_resources.py:89`
- `src/agent_tools/media_tools.py:454`
- `src/chat_handler.py:187`
- `src/clean_agent_preview.py:4062`
- `src/document_processor.py:805`
- `src/tools/image.py:121`
- `tests/test_rename_user_owner_sync.py:486`
- `tests/test_rename_user_owner_sync.py:487`
- `tests/test_replace_messages_upload_reservations.py:256`
- `tests/test_security_regressions.py:372`
- `tests/test_security_regressions.py:373`
- `tests/test_security_regressions.py:507`
- `tests/test_security_regressions.py:508`
- `tests/test_upload_handler_cleanup.py:197`
- `tests/test_upload_handler_cleanup.py:203`
- `tests/test_upload_handler_rename_owner.py:71`
- `tests/test_upload_handler_rename_owner.py:72`

## `UploadHandler.cleanup_rate_limits` — method, line 1226
- **called from:**
- `routes/upload_routes.py:643`
- `src/upload_handler.py:1309`

## `UploadHandler.get_upload_stats` — method, line 1260
- **called from:**
- `routes/upload_routes.py:451`

## `UploadHandler.save_upload` — method, line 1286
- **called from:**
- `routes/document/document_routes.py:266`
- `routes/document/document_routes.py:356`
- `routes/upload_routes.py:394`
- `tests/test_chat_upload_limit_config.py:61`
- `tests/test_upload_handler_atomicity.py:138`
- `tests/test_upload_handler_atomicity.py:192`
- `tests/test_upload_handler_atomicity.py:373`
- `tests/test_upload_handler_atomicity.py:394`
- `tests/test_upload_handler_atomicity.py:399`
- `tests/test_upload_handler_atomicity.py:420`
- `tests/test_upload_handler_atomicity.py:427`
- `tests/test_upload_handler_atomicity.py:451`
- `tests/test_upload_multifile.py:169`
