# `src/chat_helpers.py` — definitions & call sites

23 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `extract_urls` — function, line 29
- **called from:**
- `src/chat_handler.py:149`
- `src/chat_processor.py:494`
- `tests/test_extract_urls.py:13`
- `tests/test_extract_urls.py:20`
- `tests/test_extract_urls.py:24`
- `tests/test_extract_urls.py:25`
- `tests/test_extract_urls.py:33`
- `tests/test_extract_urls.py:38`

## `is_vision_model` — function, line 90
- **called from:**
- `src/chat_helpers.py:354`
- `src/chat_helpers.py:362`
- `src/chat_helpers.py:377`
- `src/chat_helpers.py:380`
- `src/chat_helpers.py:429`
- `tests/test_vision_inline.py:30`
- `tests/test_vision_inline.py:32`
- `tests/test_vision_inline.py:33`
- `tests/test_vision_inline.py:34`
- `tests/test_vision_model_detection.py:22`
- `tests/test_vision_model_detection.py:27`
- `tests/test_vision_model_detection.py:31`
- `tests/test_vision_model_detection.py:43`
- `tests/test_vision_model_detection.py:49`
- `tests/test_vision_model_detection.py:57`
- `tests/test_vision_model_detection.py:64`

## `_is_ip_safe_local` — function, line 128
- **called from:**
- `src/chat_helpers.py:165`
- `src/chat_helpers.py:184`
- `src/chat_helpers.py:220`
- `tests/test_vision_inline.py:272`
- `tests/test_vision_inline.py:273`
- `tests/test_vision_inline.py:276`
- `tests/test_vision_inline.py:277`
- `tests/test_vision_inline.py:278`
- `tests/test_vision_inline.py:279`
- `tests/test_vision_inline.py:280`
- `tests/test_vision_inline.py:283`
- `tests/test_vision_inline.py:284`
- `tests/test_vision_inline.py:285`
- `tests/test_vision_inline.py:286`
- `tests/test_vision_inline.py:289`
- `tests/test_vision_inline.py:290`
- `tests/test_vision_inline.py:293`
- `tests/test_vision_inline.py:294`
- `tests/test_vision_inline.py:295`

## `_is_safe_local_host` — function, line 152
- **called from:**
- `src/chat_helpers.py:315`
- `src/chat_helpers.py:602`
- `tests/test_vision_inline.py:301`
- `tests/test_vision_inline.py:302`
- `tests/test_vision_inline.py:303`
- `tests/test_vision_inline.py:312`
- `tests/test_vision_inline.py:321`

## `SafeProbeBackend` — class, line 192
- **called from:**
- `src/chat_helpers.py:254`
- `src/chat_helpers.py:271`
- `tests/test_vision_inline.py:343`

## `SafeProbeBackend.connect_tcp` — method, line 200
- **called from:**
- `services/memory/skill_importer.py:143`
- `src/integrations.py:403`
- `src/outbound_fetch.py:134`
- `src/webhook_manager.py:191`
- `tests/test_integration_api_call_ssrf.py:203`
- `tests/test_integration_api_call_ssrf.py:218`
- `tests/test_security_regressions.py:1335`
- `tests/test_skill_importer_dns_pinning.py:41`
- `tests/test_skill_importer_dns_pinning.py:61`
- `tests/test_vision_inline.py:347`
- `tests/test_vision_inline.py:350`

## `_safe_probe_get` — function, line 244
- **called from:**
- `src/chat_helpers.py:291`

## `_safe_probe_post` — function, line 261
- **called from:**
- `src/chat_helpers.py:623`

## `_probe_lmstudio_models` — function, line 278
- **called from:**
- `src/chat_helpers.py:317`
- `tests/test_vision_inline.py:337`
- `tests/test_vision_inline.py:363`

## `lmstudio_supports_vision` — function, line 309
- **called from:**
- `src/chat_helpers.py:403`
- `src/chat_helpers.py:405`
- `src/chat_helpers.py:407`
- `tests/test_lmstudio_vision.py:45`
- `tests/test_lmstudio_vision.py:49`
- `tests/test_lmstudio_vision.py:53`
- `tests/test_lmstudio_vision.py:57`
- `tests/test_lmstudio_vision.py:61`
- `tests/test_lmstudio_vision.py:65`
- `tests/test_lmstudio_vision.py:76`
- `tests/test_vision_inline.py:190`
- `tests/test_vision_inline.py:206`

## `model_supports_vision` — function, line 333
- **called from:**
- `tests/test_lmstudio_vision.py:92`
- `tests/test_lmstudio_vision.py:97`
- `tests/test_lmstudio_vision.py:98`
- `tests/test_lmstudio_vision.py:99`
- `tests/test_lmstudio_vision.py:100`
- `tests/test_lmstudio_vision.py:106`
- `tests/test_lmstudio_vision.py:107`
- `tests/test_lmstudio_vision.py:191`
- `tests/test_lmstudio_vision.py:196`
- `tests/test_lmstudio_vision.py:200`
- `tests/test_lmstudio_vision.py:205`
- `tests/test_lmstudio_vision.py:210`
- `tests/test_vision_inline.py:81`
- `tests/test_vision_inline.py:247`
- `tests/test_vision_inline.py:252`
- `tests/test_vision_inline.py:257`
- `tests/test_vision_inline.py:262`
- `tests/test_vision_inline.py:410`
- `tests/test_vision_inline.py:418`
- `tests/test_vision_inline.py:426`
- `tests/test_vision_inline.py:433`

## `_models_list_url` — function, line 449
- **called from:**
- `src/chat_helpers.py:470`
- `tests/test_lmstudio_vision.py:170`
- `tests/test_lmstudio_vision.py:173`

## `_fetch_models_with_modality` — function, line 459
- **called from:**
- `src/chat_helpers.py:525`

## `_model_entry_supports_vision` — function, line 488
- **called from:**
- `src/chat_helpers.py:539`

## `_entry_matches_model` — function, line 509
- **called from:**
- `src/chat_helpers.py:537`

## `advertised_supports_vision` — function, line 519
- **called from:**
- `src/chat_helpers.py:413`
- `tests/test_lmstudio_vision.py:143`
- `tests/test_lmstudio_vision.py:147`
- `tests/test_lmstudio_vision.py:151`
- `tests/test_lmstudio_vision.py:155`
- `tests/test_lmstudio_vision.py:159`
- `tests/test_lmstudio_vision.py:163`
- `tests/test_lmstudio_vision.py:167`

## `_matches_override_pattern` — function, line 547
- **called from:**
- `src/chat_helpers.py:348`
- `src/chat_helpers.py:350`

## `_vision_probe_enabled` — function, line 576
- **called from:**
- `src/chat_helpers.py:599`

## `_chat_completions_url` — function, line 580
- **called from:**
- `src/chat_helpers.py:624`

## `probe_endpoint_supports_vision` — function, line 587
- **called from:**
- `src/chat_helpers.py:420`
- `src/chat_helpers.py:422`
- `src/chat_helpers.py:424`
- `tests/test_vision_inline.py:51`
- `tests/test_vision_inline.py:53`
- `tests/test_vision_inline.py:66`
- `tests/test_vision_inline.py:73`
- `tests/test_vision_inline.py:189`
- `tests/test_vision_inline.py:205`
- `tests/test_vision_inline.py:368`

## `validate_message` — function, line 644
- **called from:**
- `src/chat_helpers.py:747`

## `validate_file_upload` — function, line 659
- **called from:**
- `tests/test_chat_upload_limit_config.py:49`

## `coerce_message_and_session` — function, line 723
- **called from:**
- `routes/chat_routes.py:2987`
