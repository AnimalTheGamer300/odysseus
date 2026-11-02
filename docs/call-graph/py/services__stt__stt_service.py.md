# `services/stt/stt_service.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `STTService` — class, line 14
- **called from:**
- `services/stt/stt_service.py:207`
- `tests/test_speech_service_toggles.py:34`
- `tests/test_stt_leak.py:7`

## `STTService.__init__` — method, line 25
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

## `STTService._load_settings` — method, line 30
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

## `STTService.available` — method, line 41
- decorator: `property`
- **called from:**
- `static/js/calendar.js:2181`
- `static/js/chatRenderer.js:1789`
- `static/js/sessions.js:1767`
- `static/js/skills.js:1011`

## `STTService._get_whisper` — method, line 58
- **called from:**
- `services/stt/stt_service.py:51`
- `services/stt/stt_service.py:91`
- `services/stt/stt_service.py:191`

## `STTService._transcribe_local` — method, line 90
- **called from:**
- `services/stt/stt_service.py:168`
- `tests/test_stt_leak.py:20`

## `STTService._transcribe_api` — method, line 119
- **called from:**
- `services/stt/stt_service.py:171`

## `STTService.transcribe` — method, line 156
- **called from:**
- `routes/stt_routes.py:39`
- `services/stt/stt_service.py:105`
- `tests/test_speech_service_toggles.py:56`
- `static/js/voiceRecorder.js:9`
- `static/js/voiceRecorder.js:10`

## `STTService.get_stats` — method, line 176
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

## `get_stt_service` — function, line 204
- **called from:**
- `app.py:760`
