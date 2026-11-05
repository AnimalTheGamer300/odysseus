# `services/stt/stt_service.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `STTService` — class, line 14
- **called from:**
- `services/stt/stt_service.py:207`
- `tests/test_speech_service_toggles.py:34`
- `tests/test_stt_leak.py:8`

## `STTService.__init__` — method, line 25
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

## `STTService._load_settings` — method, line 30
- **called from:**
- `routes/auth_routes.py:780`
- `routes/auth_routes.py:795`
- `routes/auth_routes.py:986`
- `routes/contacts/contacts_routes.py:52`
- `routes/contacts/contacts_routes.py:1000`
- `routes/email/email_helpers.py:1240`
- `routes/email/email_pollers.py:504`
- `routes/email/email_pollers.py:526`
- `routes/email/email_pollers.py:640`
- `routes/email/email_pollers.py:1576`
- `routes/email/email_routes.py:6573`
- `routes/email/email_routes.py:6930`
- `routes/email/email_routes.py:7219`
- `routes/email/email_routes.py:7231`
- `routes/email/email_routes.py:7257`
- `routes/email/email_routes.py:7304`
- `routes/model_routes.py:184`
- `routes/model_routes.py:2365`
- `routes/model_routes.py:2799`
- `routes/model_routes.py:2967`
- `routes/model_routes.py:2971`
- `routes/model_routes.py:3108`
- `routes/model_routes.py:3128`
- `services/stt/stt_service.py:42`
- `services/stt/stt_service.py:66`
- `services/stt/stt_service.py:157`
- `services/stt/stt_service.py:177`
- `services/tts/tts_service.py:66`
- `services/tts/tts_service.py:200`
- `services/tts/tts_service.py:254`
- `src/agent_loop.py:14918`
- `src/agent_loop.py:15156`
- `src/builtin_actions.py:3583`
- `tests/test_carddav_password_encryption.py:39`
- `tests/test_carddav_password_encryption.py:145`
- `tests/test_carddav_password_encryption.py:158`
- `tests/test_carddav_password_encryption.py:162`

## `STTService.available` — method, line 41
- decorator: `property`
- **called from:**
- `src/containment.py:633`
- `static/js/calendar.js:2743`
- `static/js/chatRenderer.js:2368`
- `static/js/sessions.js:2105`
- `static/js/skills.js:1251`

## `STTService._get_whisper` — method, line 58
- **called from:**
- `services/stt/stt_service.py:51`
- `services/stt/stt_service.py:91`
- `services/stt/stt_service.py:191`

## `STTService._transcribe_local` — method, line 90
- **called from:**
- `services/stt/stt_service.py:168`
- `tests/test_stt_leak.py:21`

## `STTService._transcribe_api` — method, line 119
- **called from:**
- `services/stt/stt_service.py:171`

## `STTService.transcribe` — method, line 156
- **called from:**
- `routes/stt_routes.py:39`
- `services/stt/stt_service.py:105`
- `src/agent_tools/media_tools.py:2266`
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
- `src/research_handler.py:382`
- `src/research_handler.py:406`
- `src/research_handler.py:1074`
- `src/task_scheduler.py:2275`
- `tests/test_deep_research_action_planning.py:490`
- `tests/test_tts_cache_stats.py:10`
- `tests/test_tts_speed_malformed.py:22`

## `get_stt_service` — function, line 204
- **called from:**
- `app.py:840`
