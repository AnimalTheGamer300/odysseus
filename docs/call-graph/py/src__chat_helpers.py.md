# `src/chat_helpers.py` — definitions & call sites

15 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `extract_urls` — function, line 21
- **called from:**
- `src/chat_handler.py:144`
- `src/chat_processor.py:476`
- `tests/test_extract_urls.py:13`
- `tests/test_extract_urls.py:20`
- `tests/test_extract_urls.py:24`
- `tests/test_extract_urls.py:25`
- `tests/test_extract_urls.py:33`
- `tests/test_extract_urls.py:38`

## `is_vision_model` — function, line 78
- **called from:**
- `src/chat_helpers.py:310`
- `tests/test_vision_model_detection.py:23`
- `tests/test_vision_model_detection.py:28`
- `tests/test_vision_model_detection.py:32`
- `tests/test_vision_model_detection.py:44`
- `tests/test_vision_model_detection.py:50`
- `tests/test_vision_model_detection.py:58`
- `tests/test_vision_model_detection.py:65`

## `_is_local_host` — function, line 96
- **called from:**
- `src/chat_helpers.py:149`

## `_probe_lmstudio_models` — function, line 112
- **called from:**
- `src/chat_helpers.py:151`

## `lmstudio_supports_vision` — function, line 143
- **called from:**
- `src/chat_helpers.py:299`
- `tests/test_lmstudio_vision.py:45`
- `tests/test_lmstudio_vision.py:49`
- `tests/test_lmstudio_vision.py:53`
- `tests/test_lmstudio_vision.py:57`
- `tests/test_lmstudio_vision.py:61`
- `tests/test_lmstudio_vision.py:65`
- `tests/test_lmstudio_vision.py:76`

## `_models_list_url` — function, line 184
- **called from:**
- `src/chat_helpers.py:205`
- `tests/test_lmstudio_vision.py:168`
- `tests/test_lmstudio_vision.py:171`

## `_fetch_models_with_modality` — function, line 194
- **called from:**
- `src/chat_helpers.py:260`

## `_model_entry_supports_vision` — function, line 223
- **called from:**
- `src/chat_helpers.py:274`

## `_entry_matches_model` — function, line 244
- **called from:**
- `src/chat_helpers.py:272`

## `advertised_supports_vision` — function, line 254
- **called from:**
- `src/chat_helpers.py:305`
- `tests/test_lmstudio_vision.py:141`
- `tests/test_lmstudio_vision.py:145`
- `tests/test_lmstudio_vision.py:149`
- `tests/test_lmstudio_vision.py:153`
- `tests/test_lmstudio_vision.py:157`
- `tests/test_lmstudio_vision.py:161`
- `tests/test_lmstudio_vision.py:165`

## `model_supports_vision` — function, line 280
- **called from:**
- `tests/test_lmstudio_vision.py:92`
- `tests/test_lmstudio_vision.py:97`
- `tests/test_lmstudio_vision.py:98`
- `tests/test_lmstudio_vision.py:104`
- `tests/test_lmstudio_vision.py:105`
- `tests/test_lmstudio_vision.py:189`
- `tests/test_lmstudio_vision.py:194`
- `tests/test_lmstudio_vision.py:198`
- `tests/test_lmstudio_vision.py:203`
- `tests/test_lmstudio_vision.py:208`

## `_matches_override_pattern` — function, line 313
- **called from:**
- `src/chat_helpers.py:291`
- `src/chat_helpers.py:293`

## `validate_message` — function, line 332
- **called from:**
- `src/chat_helpers.py:435`

## `validate_file_upload` — function, line 347
- **called from:**
- `tests/test_chat_upload_limit_config.py:49`

## `coerce_message_and_session` — function, line 411
- **called from:**
- `routes/chat_routes.py:1334`
