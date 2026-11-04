# `src/upload_handler.py` — definitions & call sites

41 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `secure_filename` — function, line 19
- **called from:**
- `routes/personal_routes.py:25`
- `routes/personal_routes.py:37`
- `src/upload_handler.py:1268`

## `UploadCleanupSafetyError` — class, line 49
- **called from:**
- `src/upload_handler.py:649`
- `src/upload_handler.py:683`
- `src/upload_handler.py:704`

## `is_valid_upload_id` — function, line 78
- **called from:**
- `src/pdf_form_doc.py:183`
- `src/upload_handler.py:147`
- `src/upload_handler.py:708`
- `tests/test_upload_id_extension.py:26`
- `tests/test_upload_id_extension.py:36`
- `tests/test_upload_id_validation.py:10`
- `tests/test_upload_id_validation.py:14`
- `tests/test_upload_id_validation.py:18`
- `tests/test_upload_id_validation.py:19`
- `tests/test_upload_id_validation.py:20`
- `tests/test_upload_id_validation.py:21`

## `extract_upload_ids` — function, line 83
- **called from:**
- `routes/upload_routes.py:46`

## `extract_internal_upload_ids` — function, line 90
- **called from:**
- `src/upload_handler.py:101`
- `src/upload_handler.py:106`
- `src/upload_handler.py:132`
- `src/upload_handler.py:170`
- `src/upload_handler.py:176`
- `tests/test_upload_handler_cleanup.py:574`
- `tests/test_upload_handler_cleanup.py:575`
- `tests/test_upload_handler_cleanup.py:576`
- `tests/test_upload_handler_cleanup.py:580`
- `tests/test_upload_handler_cleanup.py:583`
- `tests/test_upload_handler_cleanup.py:587`
- `tests/test_upload_handler_cleanup.py:590`
- `tests/test_upload_handler_cleanup.py:593`

## `reserve_upload_references` — function, line 117
- **called from:**
- `routes/calendar_routes.py:809`
- `routes/document/document_routes.py:83`
- `routes/note/note_routes.py:601`
- `src/agent_tools/document_tools.py:14`
- `src/tools/calendar.py:418`
- `src/tools/calendar.py:487`
- `src/tools/notes.py:203`
- `src/tools/notes.py:252`
- `tests/test_upload_handler_cleanup.py:606`
- `tests/test_upload_handler_cleanup.py:611`

## `reserve_upload_ids` — function, line 136
- **called from:**
- `src/upload_handler.py:133`
- `src/upload_handler.py:184`

## `reserve_message_upload_references` — function, line 163
- **called from:**
- `core/session_manager.py:363`
- `core/session_manager.py:374`
- `core/session_manager.py:529`
- `core/session_manager.py:669`
- `routes/history/history_routes.py:136`
- `routes/session_routes.py:699`
- `tests/test_upload_handler_cleanup.py:622`

## `_build_upload_id` — function, line 187
- **called from:**
- `src/upload_handler.py:1374`
- `tests/test_upload_id_extension.py:25`
- `tests/test_upload_id_extension.py:30`
- `tests/test_upload_id_extension.py:31`
- `tests/test_upload_id_extension.py:35`

## `count_recent_uploads` — function, line 201
- **called from:**
- `routes/upload_routes.py:278`
- `tests/test_upload_multifile.py:37`
- `tests/test_upload_multifile.py:39`
- `tests/test_upload_multifile.py:40`
- `tests/test_upload_multifile.py:41`

## `UploadHandler` — class, line 213
- **called from:**
- `routes/document/document_helpers.py:183`
- `src/app_initializer.py:94`
- `tests/test_chat_upload_limit_config.py:58`
- `tests/test_gif_video_frames.py:158`
- `tests/test_nix_upload_text.py:6`
- `tests/test_rename_user_owner_sync.py:455`
- `tests/test_replace_messages_upload_reservations.py:194`
- `tests/test_security_regressions.py:369`
- `tests/test_security_regressions.py:380`
- `tests/test_security_regressions.py:405`
- `tests/test_security_regressions.py:438`
- `tests/test_security_regressions.py:462`
- `tests/test_security_regressions.py:497`
- `tests/test_upload_content_detection_magic.py:39`
- `tests/test_upload_handler_atomicity.py:56`
- `tests/test_upload_handler_atomicity.py:282`
- `tests/test_upload_handler_cleanup.py:56`
- `tests/test_upload_handler_rename_owner.py:13`
- `tests/test_upload_multifile.py:161`
- `tests/test_upload_multifile.py:190`
- `tests/test_upload_multifile.py:221`
- `tests/test_upload_routes_owner_scope.py:80`

## `UploadHandler.__init__` — method, line 214
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email_routes.py:1455`
- `src/builtin_actions.py:428`
- `src/outbound_fetch.py:220`
- `tests/test_agent_state_dir_confinement.py:648`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_extraction_controls.py:14`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_retired_settings_interfaces.py:30`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:148`

## `UploadHandler.inside_base_dir` — method, line 257
- **called from:**
- `routes/chat_helpers.py:444`
- `src/document_processor.py:667`
- `tests/test_inside_base_dir_nonstring.py:11`
- `tests/test_inside_base_dir_nonstring.py:12`
- `tests/test_inside_base_dir_nonstring.py:13`
- `tests/test_inside_base_dir_nonstring.py:18`
- `tests/test_inside_base_dir_nonstring.py:19`

## `UploadHandler.get_upload_dir` — method, line 266
- **called from:**
- `src/upload_handler.py:1377`

## `UploadHandler.calculate_file_hash` — method, line 273
- **called from:**
- `src/upload_handler.py:1295`

## `UploadHandler.detect_content_type` — method, line 282
- **called from:**
- `src/upload_handler.py:1271`
- `tests/test_upload_content_detection_magic.py:45`

## `UploadHandler.is_image_file` — method, line 300
- **called from:**
- `routes/chat_routes.py:691`
- `routes/upload_routes.py:198`
- `src/chat_handler.py:226`
- `src/document_processor.py:675`

## `UploadHandler.is_document_file` — method, line 318
- **called from:**
- `src/document_processor.py:746`
- `tests/test_nix_upload_text.py:8`

## `UploadHandler.is_audio_file` — method, line 348
- **called from:**
- `src/document_processor.py:730`

## `UploadHandler.is_video_file` — method, line 366
- **called from:**
- `src/chat_handler.py:221`
- `src/document_processor.py:709`
- `src/upload_handler.py:1284`
- `tests/test_gif_video_frames.py:159`
- `tests/test_gif_video_frames.py:160`
- `tests/test_gif_video_frames.py:161`
- `tests/test_gif_video_frames.py:162`
- `tests/test_gif_video_frames.py:163`
- `tests/test_gif_video_frames.py:164`

## `UploadHandler.is_safe_file_type` — method, line 393
- **called from:**
- `src/upload_handler.py:1274`

## `UploadHandler._parse_upload_timestamp` — method, line 417
- decorator: `staticmethod`
- **called from:**
- `src/upload_handler.py:432`
- `src/upload_handler.py:507`
- `src/upload_handler.py:980`

## `UploadHandler._upload_metadata_is_recent` — method, line 429
- decorator: `classmethod`
- **called from:**
- `src/upload_handler.py:619`

## `UploadHandler._upload_index_keys_for_file` — method, line 440
- decorator: `classmethod`
- **called from:**
- `src/upload_handler.py:595`

## `UploadHandler.cleanup_old_uploads` — method, line 528
- **called from:**
- `routes/upload_routes.py:142`
- `tests/test_upload_handler_cleanup.py:248`
- `tests/test_upload_handler_cleanup.py:276`
- `tests/test_upload_handler_cleanup.py:409`
- `tests/test_upload_handler_cleanup.py:466`

## `UploadHandler.validate_upload_id` — method, line 706
- **called from:**
- `routes/upload_routes.py:358`
- `routes/upload_routes.py:456`
- `routes/upload_routes.py:500`
- `src/upload_handler.py:585`
- `src/upload_handler.py:884`
- `src/upload_handler.py:905`
- `src/upload_handler.py:1120`

## `UploadHandler._inside_upload_dir` — method, line 710
- **called from:**
- `routes/chat_helpers.py:442`
- `src/document_processor.py:664`
- `src/upload_handler.py:568`
- `src/upload_handler.py:589`
- `src/upload_handler.py:963`
- `src/upload_handler.py:977`
- `src/upload_handler.py:1125`
- `src/upload_handler.py:1138`
- `src/upload_handler.py:1311`

## `UploadHandler._atomic_write_json` — method, line 719
- **called from:**
- `core/auth.py:157`
- `core/auth.py:222`
- `src/upload_handler.py:632`
- `src/upload_handler.py:639`
- `src/upload_handler.py:673`
- `src/upload_handler.py:996`
- `src/upload_handler.py:1003`
- `src/upload_handler.py:1115`
- `src/upload_handler.py:1320`
- `src/upload_handler.py:1350`
- `src/upload_handler.py:1423`
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

## `UploadHandler._replace_json` — method, line 736
- **called from:**
- `src/upload_handler.py:756`
- `src/upload_handler.py:763`

## `UploadHandler._upload_index_signature` — method, line 772
- decorator: `staticmethod`
- **called from:**
- `src/upload_handler.py:767`
- `src/upload_handler.py:813`
- `src/upload_handler.py:849`
- `src/upload_handler.py:863`
- `src/upload_handler.py:879`

## `UploadHandler._load_upload_index` — method, line 803
- **called from:**
- `routes/upload_routes.py:366`
- `routes/upload_routes.py:417`
- `src/upload_handler.py:556`
- `src/upload_handler.py:886`
- `src/upload_handler.py:915`
- `src/upload_handler.py:1082`
- `src/upload_handler.py:1213`
- `src/upload_handler.py:1306`
- `src/upload_handler.py:1330`
- `src/upload_handler.py:1420`
- `tests/test_upload_handler_atomicity.py:262`
- `tests/test_upload_handler_atomicity.py:287`
- `tests/test_upload_handler_atomicity.py:301`
- `tests/test_upload_handler_atomicity.py:330`

## `UploadHandler.get_upload_info` — method, line 882
- **called from:**
- `tests/test_upload_handler_atomicity.py:380`
- `tests/test_upload_handler_atomicity.py:467`
- `tests/test_upload_handler_cleanup.py:195`
- `tests/test_upload_handler_cleanup.py:199`
- `tests/test_upload_handler_cleanup.py:202`
- `tests/test_upload_handler_cleanup.py:223`
- `tests/test_upload_handler_cleanup.py:386`
- `tests/test_upload_handler_cleanup.py:411`

## `UploadHandler.reserve_upload` — method, line 891
- **called from:**
- `src/upload_handler.py:151`
- `src/upload_handler.py:1165`
- `tests/test_upload_handler_cleanup.py:616`

## `UploadHandler._renamed_upload_index_key` — method, line 1029
- **called from:**
- `src/upload_handler.py:1096`

## `UploadHandler._unique_upload_index_key` — method, line 1049
- **called from:**
- `src/upload_handler.py:1097`

## `UploadHandler.rename_owner` — method, line 1066
- **called from:**
- `routes/auth_routes.py:483`
- `routes/auth_routes.py:529`
- `routes/personal_routes.py:115`
- `tests/test_rag_vector_rename_owner.py:66`
- `tests/test_rename_user_owner_sync.py:323`
- `tests/test_rename_user_owner_sync.py:337`
- `tests/test_upload_handler_rename_owner.py:58`
- `tests/test_upload_handler_rename_owner.py:91`

## `UploadHandler._find_upload_path` — method, line 1118
- **called from:**
- `src/upload_handler.py:976`

## `UploadHandler.resolve_upload` — method, line 1150
- **called from:**
- `routes/chat_helpers.py:430`
- `routes/chat_routes.py:682`
- `routes/document/document_helpers.py:156`
- `src/chat_handler.py:182`
- `src/document_processor.py:655`
- `tests/test_rename_user_owner_sync.py:486`
- `tests/test_rename_user_owner_sync.py:487`
- `tests/test_replace_messages_upload_reservations.py:256`
- `tests/test_security_regressions.py:371`
- `tests/test_security_regressions.py:372`
- `tests/test_security_regressions.py:506`
- `tests/test_security_regressions.py:507`
- `tests/test_upload_handler_cleanup.py:197`
- `tests/test_upload_handler_cleanup.py:203`
- `tests/test_upload_handler_rename_owner.py:71`
- `tests/test_upload_handler_rename_owner.py:72`

## `UploadHandler.cleanup_rate_limits` — method, line 1172
- **called from:**
- `routes/upload_routes.py:531`
- `src/upload_handler.py:1255`

## `UploadHandler.get_upload_stats` — method, line 1206
- **called from:**
- `routes/upload_routes.py:348`

## `UploadHandler.save_upload` — method, line 1232
- **called from:**
- `routes/document/document_routes.py:261`
- `routes/upload_routes.py:291`
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
