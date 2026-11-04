# `services/tts/tts_service.py` — definitions & call sites

21 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_safe_speed` — function, line 18
- **called from:**
- `services/tts/tts_service.py:206`
- `services/tts/tts_service.py:268`

## `TTSService` — class, line 30
- **called from:**
- `services/tts/tts_service.py:349`
- `tests/test_speech_service_toggles.py:6`
- `tests/test_tts_available_nonstring_provider.py:9`
- `tests/test_tts_cache_stats.py:5`
- `tests/test_tts_service_enforce_cache_limit.py:15`
- `tests/test_tts_service_enforce_cache_limit.py:29`
- `tests/test_tts_service_enforce_cache_limit.py:63`
- `tests/test_tts_service_enforce_cache_limit.py:77`
- `tests/test_tts_speed_malformed.py:20`
- `tests/test_tts_speed_malformed.py:27`

## `TTSService.__init__` — method, line 41
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

## `TTSService._load_settings` — method, line 53
- **called from:**
- `routes/auth_routes.py:721`
- `routes/auth_routes.py:733`
- `routes/auth_routes.py:840`
- `routes/contacts/contacts_routes.py:49`
- `routes/contacts/contacts_routes.py:862`
- `routes/email_helpers.py:1100`
- `routes/email_pollers.py:392`
- `routes/email_pollers.py:411`
- `routes/email_pollers.py:516`
- `routes/email_pollers.py:1376`
- `routes/email_routes.py:4872`
- `routes/email_routes.py:5194`
- `routes/email_routes.py:5449`
- `routes/email_routes.py:5461`
- `routes/email_routes.py:5487`
- `routes/email_routes.py:5527`
- `routes/model_routes.py:165`
- `routes/model_routes.py:2182`
- `routes/model_routes.py:2434`
- `routes/model_routes.py:2587`
- `routes/model_routes.py:2591`
- `routes/model_routes.py:2700`
- `routes/model_routes.py:2714`
- `services/stt/stt_service.py:42`
- `services/stt/stt_service.py:66`
- `services/stt/stt_service.py:157`
- `services/stt/stt_service.py:177`
- `services/tts/tts_service.py:66`
- `services/tts/tts_service.py:200`
- `services/tts/tts_service.py:254`
- `src/agent_loop.py:2759`
- `src/agent_loop.py:2993`
- `src/builtin_actions.py:3298`
- `tests/test_carddav_password_encryption.py:39`
- `tests/test_carddav_password_encryption.py:145`
- `tests/test_carddav_password_encryption.py:158`
- `tests/test_carddav_password_encryption.py:162`

## `TTSService.available` — method, line 65
- decorator: `property`
- **called from:**
- `static/js/calendar.js:2181`
- `static/js/chatRenderer.js:1789`
- `static/js/sessions.js:1767`
- `static/js/skills.js:1011`

## `TTSService._cache_key` — method, line 83
- **called from:**
- `services/hwfit/hardware.py:808`
- `services/tts/tts_service.py:215`
- `services/tts/tts_service.py:238`

## `TTSService._get_cached` — method, line 87
- **called from:**
- `services/tts/tts_service.py:216`

## `TTSService._put_cache` — method, line 94
- **called from:**
- `services/tts/tts_service.py:239`
- `tests/test_tts_cache_stats.py:8`
- `tests/test_tts_service_enforce_cache_limit.py:18`
- `tests/test_tts_service_enforce_cache_limit.py:46`
- `tests/test_tts_service_enforce_cache_limit.py:66`
- `tests/test_tts_service_enforce_cache_limit.py:67`
- `tests/test_tts_service_enforce_cache_limit.py:68`
- `tests/test_tts_service_enforce_cache_limit.py:92`

## `TTSService._enforce_cache_limit` — method, line 100
- **called from:**
- `services/tts/tts_service.py:98`

## `TTSService.clear_cache` — method, line 145
- **called from:**
- `routes/tts_routes.py:81`
- `tests/test_email_owner_scope.py:438`

## `TTSService._get_kokoro` — method, line 154
- **called from:**
- `services/tts/tts_service.py:75`
- `services/tts/tts_service.py:224`
- `services/tts/tts_service.py:274`

## `TTSService._synthesize_api` — method, line 161
- **called from:**
- `services/tts/tts_service.py:232`

## `TTSService.synthesize` — method, line 199
- **called from:**
- `routes/tts_routes.py:50`
- `services/tts/tts_service.py:245`
- `tests/test_speech_service_toggles.py:29`
- `tests/test_tts_speed_malformed.py:31`
- `static/js/tts-ai.js:109`
- `static/js/tts-ai.js:189`
- `static/js/tts-ai.js:296`

## `TTSService.synthesize_to_base64` — method, line 243
- **called from:**
- `routes/tts_routes.py:41`

## `TTSService.set_voice` — method, line 250
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TTSService.get_stats` — method, line 253
- **called from:**
- `routes/diagnostics_routes.py:70`
- `routes/stt_routes.py:20`
- `routes/tts_routes.py:25`
- `scripts/index_documents.py:103`
- `services/docs/service.py:117`
- `services/research/research_handler.py:281`
- `src/rag_manager.py:62`
- `src/research_handler.py:364`
- `src/research_handler.py:388`
- `src/research_handler.py:845`
- `src/task_scheduler.py:2081`
- `tests/test_tts_cache_stats.py:10`
- `tests/test_tts_speed_malformed.py:22`

## `_KokoroPipeline` — class, line 284
- **called from:**
- `services/tts/tts_service.py:156`

## `_KokoroPipeline.__init__` — method, line 287
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

## `_KokoroPipeline._init` — method, line 293
- **called from:**
- `services/tts/tts_service.py:291`

## `_KokoroPipeline.synthesize_raw` — method, line 315
- **called from:**
- `services/tts/tts_service.py:226`

## `get_tts_service` — function, line 346
- **called from:**
- `app.py:612`
