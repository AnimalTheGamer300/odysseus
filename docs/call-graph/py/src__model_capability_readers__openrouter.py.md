# `src/model_capability_readers/openrouter.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_capabilities_from_supported_parameters` — function, line 48
- **called from:**
- `src/model_capability_readers/openrouter.py:152`

## `_limits_from_model` — function, line 58
- **called from:**
- `src/model_capability_readers/lmstudio.py:150`
- `src/model_capability_readers/openrouter.py:176`

## `_has_supported_voices` — function, line 80
- **called from:**
- `src/model_capability_readers/openrouter.py:103`

## `_capabilities_from_modalities` — function, line 84
- **called from:**
- `src/model_capability_readers/openrouter.py:154`

## `_default_parameter_controls` — function, line 114
- **called from:**
- `src/model_capability_readers/openrouter.py:123`

## `_deterministic_controls_from_model` — function, line 119
- **called from:**
- `src/model_capability_readers/openrouter.py:184`

## `record_from_model` — function, line 128
- **called from:**
- `src/model_capability_readers/generic_openai.py:55`
- `src/model_capability_readers/google.py:57`
- `src/model_capability_readers/llamacpp.py:299`
- `src/model_capability_readers/lmstudio.py:133`
- `src/model_capability_readers/openai.py:62`
- `src/model_capability_readers/openrouter.py:163`
- `src/model_capability_readers/openrouter.py:197`

## `records_from_payload` — function, line 189
- **called from:**
- `src/model_capability_readers/__init__.py:66`
- `src/model_capability_readers/__init__.py:72`
- `tests/test_model_capability_readers.py:43`
- `tests/test_model_capability_readers.py:75`
- `tests/test_model_capability_readers.py:84`
- `tests/test_model_capability_readers.py:111`
- `tests/test_model_capability_readers.py:126`
- `tests/test_model_capability_readers.py:238`
- `tests/test_model_capability_readers.py:286`
- `tests/test_model_capability_readers.py:329`
- `tests/test_model_capability_readers.py:412`
- `tests/test_model_capability_readers.py:458`
- `tests/test_model_capability_readers.py:492`
- `tests/test_model_capability_readers.py:511`
- `tests/test_model_capability_readers.py:618`
- `tests/test_model_capability_readers.py:638`
