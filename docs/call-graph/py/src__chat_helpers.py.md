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

## `is_vision_model` — function, line 76
- **called from:**
- `src/chat_helpers.py:308`
- `tests/test_vision_model_detection.py:21`
- `tests/test_vision_model_detection.py:26`
- `tests/test_vision_model_detection.py:30`
- `tests/test_vision_model_detection.py:42`
- `tests/test_vision_model_detection.py:48`
- `tests/test_vision_model_detection.py:56`
- `tests/test_vision_model_detection.py:63`

## `_is_local_host` — function, line 94
- **called from:**
- `src/chat_helpers.py:147`

## `_probe_lmstudio_models` — function, line 110
- **called from:**
- `src/chat_helpers.py:149`

## `lmstudio_supports_vision` — function, line 141
- **called from:**
- `src/chat_helpers.py:297`
- `tests/test_lmstudio_vision.py:45`
- `tests/test_lmstudio_vision.py:49`
- `tests/test_lmstudio_vision.py:53`
- `tests/test_lmstudio_vision.py:57`
- `tests/test_lmstudio_vision.py:61`
- `tests/test_lmstudio_vision.py:65`
- `tests/test_lmstudio_vision.py:76`

## `_models_list_url` — function, line 182
- **called from:**
- `src/chat_helpers.py:203`
- `tests/test_lmstudio_vision.py:168`
- `tests/test_lmstudio_vision.py:171`

## `_fetch_models_with_modality` — function, line 192
- **called from:**
- `src/chat_helpers.py:258`

## `_model_entry_supports_vision` — function, line 221
- **called from:**
- `src/chat_helpers.py:272`

## `_entry_matches_model` — function, line 242
- **called from:**
- `src/chat_helpers.py:270`

## `advertised_supports_vision` — function, line 252
- **called from:**
- `src/chat_helpers.py:303`
- `tests/test_lmstudio_vision.py:141`
- `tests/test_lmstudio_vision.py:145`
- `tests/test_lmstudio_vision.py:149`
- `tests/test_lmstudio_vision.py:153`
- `tests/test_lmstudio_vision.py:157`
- `tests/test_lmstudio_vision.py:161`
- `tests/test_lmstudio_vision.py:165`

## `model_supports_vision` — function, line 278
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

## `_matches_override_pattern` — function, line 311
- **called from:**
- `src/chat_helpers.py:289`
- `src/chat_helpers.py:291`

## `validate_message` — function, line 330
- **called from:**
- `src/chat_helpers.py:433`

## `validate_file_upload` — function, line 345
- **called from:**
- `tests/test_chat_upload_limit_config.py:49`

## `coerce_message_and_session` — function, line 409
- **called from:**
- `routes/chat_routes.py:1334`
