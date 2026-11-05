# `src/config.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `DataConfig` — class, line 20
- **called from:**
- `src/config.py:125`

## `LLMConfig` — class, line 48
- **called from:**
- `src/config.py:126`

## `SearchConfig` — class, line 65
- **called from:**
- `src/config.py:127`

## `SecurityConfig` — class, line 91
- **called from:**
- `src/config.py:128`

## `AppConfig` — class, line 122
- **called from:**
- `src/config.py:176`

## `AppConfig.set_data_paths` — method, line 135
- decorator: `field_validator("data", mode="before")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_directories` — function, line 179
- **called from:**
- `src/app_initializer.py:74`
- `src/config.py:205`
- `tests/test_agent_state_dir_confinement.py:332`
- `tests/test_agent_state_dir_confinement.py:353`

## `validate_config` — function, line 192
- **called from:**
- `src/browser_identity.py:213`
- `src/browser_identity.py:258`
- `src/browser_identity.py:487`
- `src/config.py:208`
- `tests/test_browser_resource_identity.py:235`
