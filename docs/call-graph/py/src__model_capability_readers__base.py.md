# `src/model_capability_readers/base.py` — definitions & call sites

24 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ModelCapabilityRecord` — class, line 35
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/model_capability_readers/generic_openai.py:36`
- `src/model_capability_readers/google.py:38`
- `src/model_capability_readers/llamacpp.py:266`
- `src/model_capability_readers/llamacpp.py:383`
- `src/model_capability_readers/lmstudio.py:89`
- `src/model_capability_readers/lmstudio.py:152`
- `src/model_capability_readers/ollama.py:145`
- `src/model_capability_readers/ollama.py:169`
- `src/model_capability_readers/openai.py:41`
- `src/model_capability_readers/openrouter.py:178`

## `ModelCapabilityRecord.__post_init__` — method, line 45
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ModelCapabilityRecord.to_dict` — method, line 60
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5646`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28809`
- `src/agent_loop.py:31378`
- `src/agent_loop.py:31851`
- `src/agent_loop.py:32116`
- `src/agent_loop.py:32156`
- `src/agent_loop.py:32187`
- `src/agent_loop.py:32240`
- `src/agent_loop.py:32368`
- `src/agent_loop.py:32700`
- `src/agent_loop.py:34920`
- `src/agent_loop.py:36929`
- `src/agent_loop.py:37252`
- `src/agent_loop.py:37465`
- `src/agent_loop.py:37520`
- `src/agent_loop.py:37577`
- `src/agent_loop.py:37911`
- `src/agent_loop.py:37923`
- `src/agent_loop.py:38029`
- `src/agent_loop.py:38963`
- `src/agent_loop.py:38964`
- `src/agent_loop.py:38969`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:681`
- `src/agent_runtime/authority.py:705`
- `src/agent_runtime/authority.py:705`
- `src/agent_runtime/completion.py:356`
- `src/agent_runtime/completion.py:385`
- `src/agent_runtime/completion.py:388`
- `src/agent_runtime/completion.py:389`
- `src/agent_runtime/completion.py:392`
- `src/agent_runtime/context_resolution.py:78`
- `src/agent_runtime/context_resolution.py:78`
- `src/agent_runtime/context_resolution.py:154`
- `src/agent_runtime/context_resolution.py:155`
- `src/agent_runtime/context_resolution.py:502`
- `src/agent_runtime/context_resolution.py:518`
- `src/agent_runtime/effect_adapters.py:296`
- `src/agent_runtime/effect_log.py:263`
- `src/agent_runtime/effects.py:156`
- `src/agent_runtime/effects.py:161`
- `src/agent_runtime/effects.py:168`
- `src/agent_runtime/effects.py:173`
- `src/agent_runtime/effects.py:177`
- `src/agent_runtime/effects.py:181`
- `src/agent_runtime/effects.py:186`
- … +146 more (grep the name in repo)

## `CapabilityReader` — class, line 75
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CapabilityReader.records_from_payload` — method, line 78
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

## `as_mapping` — function, line 88
- **called from:**
- `src/model_capability_readers/base.py:172`
- `src/model_capability_readers/llamacpp.py:43`
- `src/model_capability_readers/llamacpp.py:51`
- `src/model_capability_readers/llamacpp.py:55`
- `src/model_capability_readers/llamacpp.py:104`
- `src/model_capability_readers/llamacpp.py:119`
- `src/model_capability_readers/llamacpp.py:119`
- `src/model_capability_readers/llamacpp.py:123`
- `src/model_capability_readers/llamacpp.py:128`
- `src/model_capability_readers/llamacpp.py:142`
- `src/model_capability_readers/llamacpp.py:153`
- `src/model_capability_readers/llamacpp.py:160`
- `src/model_capability_readers/llamacpp.py:162`
- `src/model_capability_readers/llamacpp.py:168`
- `src/model_capability_readers/llamacpp.py:203`
- `src/model_capability_readers/llamacpp.py:296`
- `src/model_capability_readers/llamacpp.py:324`
- `src/model_capability_readers/llamacpp.py:350`
- `src/model_capability_readers/llamacpp.py:351`
- `src/model_capability_readers/llamacpp.py:420`
- `src/model_capability_readers/lmstudio.py:31`
- `src/model_capability_readers/lmstudio.py:32`
- `src/model_capability_readers/lmstudio.py:67`
- `src/model_capability_readers/lmstudio.py:180`
- `src/model_capability_readers/ollama.py:102`
- `src/model_capability_readers/ollama.py:104`
- `src/model_capability_readers/ollama.py:162`
- `src/model_capability_readers/ollama.py:195`
- `src/model_capability_readers/openrouter.py:59`
- `src/model_capability_readers/openrouter.py:60`
- `src/model_capability_readers/openrouter.py:61`
- `src/model_capability_readers/openrouter.py:115`
- `src/model_capability_readers/openrouter.py:138`

## `as_list` — function, line 92
- **called from:**
- `src/model_capability_readers/base.py:176`
- `src/model_capability_readers/base.py:204`
- `src/model_capability_readers/google.py:25`
- `src/model_capability_readers/google_ai_studio_mapping.py:63`
- `src/model_capability_readers/llamacpp.py:47`
- `src/model_capability_readers/llamacpp.py:51`
- `src/model_capability_readers/llamacpp.py:67`
- `src/model_capability_readers/llamacpp.py:82`
- `src/model_capability_readers/llamacpp.py:199`
- `src/model_capability_readers/lmstudio.py:30`
- `src/model_capability_readers/lmstudio.py:180`
- `src/model_capability_readers/ollama.py:42`
- `src/model_capability_readers/ollama.py:51`
- `src/model_capability_readers/ollama.py:162`
- `src/model_capability_readers/openrouter.py:81`
- `src/model_capability_readers/openrouter.py:122`

## `compact_str` — function, line 102
- **called from:**
- `src/model_capability_readers/base.py:107`
- `src/model_capability_readers/base.py:115`
- `src/model_capability_readers/base.py:128`
- `src/model_capability_readers/base.py:138`
- `src/model_capability_readers/base.py:156`
- `src/model_capability_readers/base.py:180`
- `src/model_capability_readers/base.py:214`
- `src/model_capability_readers/base.py:272`
- `src/model_capability_readers/base.py:292`
- `src/model_capability_readers/generic_openai.py:40`
- `src/model_capability_readers/google.py:42`
- `src/model_capability_readers/google_ai_studio_mapping.py:58`
- `src/model_capability_readers/google_ai_studio_mapping.py:58`
- `src/model_capability_readers/google_ai_studio_mapping.py:63`
- `src/model_capability_readers/llamacpp.py:56`
- `src/model_capability_readers/llamacpp.py:59`
- `src/model_capability_readers/llamacpp.py:68`
- `src/model_capability_readers/llamacpp.py:82`
- `src/model_capability_readers/llamacpp.py:96`
- `src/model_capability_readers/llamacpp.py:97`
- `src/model_capability_readers/llamacpp.py:200`
- `src/model_capability_readers/lmstudio.py:58`
- `src/model_capability_readers/lmstudio.py:98`
- `src/model_capability_readers/lmstudio.py:161`
- `src/model_capability_readers/ollama.py:43`
- `src/model_capability_readers/ollama.py:51`
- `src/model_capability_readers/ollama.py:64`
- `src/model_capability_readers/ollama.py:93`
- `src/model_capability_readers/ollama.py:125`
- `src/model_capability_readers/openai.py:45`
- `src/model_capability_readers/openrouter.py:52`
- `src/model_capability_readers/openrouter.py:81`
- `src/model_capability_readers/openrouter.py:182`

## `_identity_part` — function, line 106
- **called from:**
- `src/model_capability_readers/base.py:126`
- `src/model_capability_readers/base.py:127`
- `src/model_capability_readers/base.py:130`

## `_base_url_scope` — function, line 114
- **called from:**
- `src/model_capability_readers/base.py:132`

## `stable_model_id_for` — function, line 125
- **called from:**
- `src/model_capability_readers/base.py:47`
- `src/model_capability_readers/generic_openai.py:39`
- `src/model_capability_readers/google.py:41`
- `src/model_capability_readers/llamacpp.py:269`
- `src/model_capability_readers/llamacpp.py:386`
- `src/model_capability_readers/lmstudio.py:92`
- `src/model_capability_readers/lmstudio.py:155`
- `src/model_capability_readers/ollama.py:148`
- `src/model_capability_readers/ollama.py:172`
- `src/model_capability_readers/openai.py:44`
- `src/model_capability_readers/openrouter.py:181`
- `tests/test_model_capability_readers.py:66`
- `tests/test_model_capability_readers.py:67`
- `tests/test_model_capability_readers.py:67`
- `tests/test_model_capability_readers.py:118`
- `tests/test_model_capability_readers.py:582`

## `model_id_from` — function, line 136
- **called from:**
- `src/model_capability_readers/generic_openai.py:29`
- `src/model_capability_readers/llamacpp.py:95`
- `src/model_capability_readers/llamacpp.py:293`
- `src/model_capability_readers/llamacpp.py:362`
- `src/model_capability_readers/lmstudio.py:113`
- `src/model_capability_readers/ollama.py:125`
- `src/model_capability_readers/ollama.py:165`
- `src/model_capability_readers/ollama.py:199`
- `src/model_capability_readers/openai.py:37`
- `src/model_capability_readers/openrouter.py:134`

## `int_limit` — function, line 144
- **called from:**
- `src/model_capability_readers/google_ai_studio_mapping.py:68`
- `src/model_capability_readers/google_ai_studio_mapping.py:69`
- `src/model_capability_readers/llamacpp.py:106`
- `src/model_capability_readers/llamacpp.py:107`
- `src/model_capability_readers/llamacpp.py:108`
- `src/model_capability_readers/llamacpp.py:125`
- `src/model_capability_readers/llamacpp.py:126`
- `src/model_capability_readers/llamacpp.py:128`
- `src/model_capability_readers/lmstudio.py:33`
- `src/model_capability_readers/lmstudio.py:33`
- `src/model_capability_readers/lmstudio.py:44`
- `src/model_capability_readers/lmstudio.py:47`
- `src/model_capability_readers/lmstudio.py:47`
- `src/model_capability_readers/lmstudio.py:48`
- `src/model_capability_readers/lmstudio.py:48`
- `src/model_capability_readers/ollama.py:88`
- `src/model_capability_readers/ollama.py:95`
- `src/model_capability_readers/openrouter.py:70`
- `src/model_capability_readers/openrouter.py:74`

## `merge_unique` — function, line 152
- **called from:**
- `src/model_capability_readers/llamacpp.py:208`
- `src/model_capability_readers/llamacpp.py:378`
- `src/model_capability_readers/lmstudio.py:79`
- `src/model_capability_readers/ollama.py:142`
- `src/model_capability_readers/openrouter.py:121`
- `src/model_capability_readers/openrouter.py:175`

## `deterministic_controls_from_supported_parameters` — function, line 162
- **called from:**
- `src/model_capability_readers/llamacpp.py:208`
- `src/model_capability_readers/openrouter.py:120`

## `openai_model_items` — function, line 171
- **called from:**
- `src/model_capability_readers/generic_openai.py:54`
- `src/model_capability_readers/llamacpp.py:44`
- `src/model_capability_readers/lmstudio.py:174`
- `src/model_capability_readers/openai.py:61`
- `src/model_capability_readers/openrouter.py:196`

## `normalize_modality_token` — function, line 179
- **called from:**
- `src/model_capability_readers/base.py:207`

## `modalities_from_value` — function, line 200
- **called from:**
- `src/model_capability_readers/base.py:220`
- `src/model_capability_readers/base.py:220`
- `src/model_capability_readers/base.py:221`
- `src/model_capability_readers/openrouter.py:139`
- `src/model_capability_readers/openrouter.py:142`

## `split_modality_arrow` — function, line 213
- **called from:**
- `src/model_capability_readers/openrouter.py:146`

## `family_from_modalities` — function, line 224
- **called from:**
- `src/model_capability_readers/openrouter.py:161`

## `primary_task_for_family` — function, line 239
- **called from:**
- `src/model_capability_readers/base.py:261`

## `build_capability` — function, line 250
- **called from:**
- `src/model_capability_readers/llamacpp.py:219`
- `src/model_capability_readers/llamacpp.py:227`
- `src/model_capability_readers/llamacpp.py:238`
- `src/model_capability_readers/lmstudio.py:145`
- `src/model_capability_readers/ollama.py:138`
- `src/model_capability_readers/openrouter.py:171`

## `detect_vendor` — function, line 271
- **called from:**
- `routes/gallery/gallery_routes.py:1834`
- `src/ai_interaction.py:1389`
- `src/ai_interaction.py:1390`
- `src/ai_interaction.py:1417`
- `src/ai_interaction.py:1628`
- `src/model_capability_readers/__init__.py:62`
- `tests/test_model_capability_readers.py:22`
- `tests/test_model_capability_readers.py:23`
- `tests/test_model_capability_readers.py:24`
- `tests/test_model_capability_readers.py:25`
- `tests/test_model_capability_readers.py:26`
- `tests/test_model_capability_readers.py:27`
- `tests/test_model_capability_readers.py:28`
- `tests/test_model_capability_readers.py:29`
- `tests/test_model_capability_readers.py:30`
- `tests/test_model_capability_readers.py:34`
- `tests/test_model_capability_readers.py:35`
- `tests/test_model_capability_readers.py:36`
- `tests/test_model_capability_readers.py:37`
- `tests/test_model_capability_readers.py:38`
- `tests/test_model_capability_readers.py:39`

## `host_matches` — function, line 296
- **called from:**
- `src/model_capability_readers/base.py:300`
- `src/model_capability_readers/base.py:302`
- `src/model_capability_readers/base.py:304`
- `src/model_capability_readers/base.py:306`
- `src/model_capability_readers/base.py:308`
