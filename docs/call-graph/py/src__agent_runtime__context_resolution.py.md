# `src/agent_runtime/context_resolution.py` — definitions & call sites

32 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ContextEvidence` — class, line 54
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ContextObservation` — class, line 63
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/context_resolution.py:135`
- `src/agent_runtime/context_resolution.py:350`
- `src/agent_runtime/context_resolution.py:383`
- `src/agent_runtime/context_resolution.py:488`
- `src/agent_runtime/context_resolution.py:493`
- `tests/test_context_resolution.py:32`
- `tests/test_context_resolution_route.py:282`
- `tests/test_context_resolution_route.py:351`

## `ContextObservation.to_dict` — method, line 68
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

## `ContextConflict` — class, line 73
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/context_resolution.py:184`

## `ContextConflict.to_dict` — method, line 77
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

## `ContextResolution` — class, line 82
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/context_resolution.py:162`
- `src/agent_runtime/context_resolution.py:214`

## `ContextResolution.mismatch` — method, line 100
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ContextResolution.budget_limit` — method, line 104
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ContextResolution.shaping_window` — method, line 109
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ContextResolution.applies_to` — method, line 121
- **called from:**
- `src/clean_agent_preview.py:5911`
- `tests/test_context_resolution.py:619`
- `tests/test_context_resolution_route.py:172`

## `ContextResolution.observe_runtime_limit` — method, line 127
- **called from:**
- `src/clean_agent_preview.py:9002`
- `tests/test_context_resolution.py:224`
- `tests/test_context_resolution.py:229`
- `tests/test_context_resolution.py:230`
- `tests/test_context_resolution_route.py:208`

## `ContextResolution.to_dict` — method, line 148
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

## `_conflicts` — function, line 167
- **called from:**
- `src/agent_runtime/context_resolution.py:211`

## `_strongest` — function, line 188
- **called from:**
- `src/agent_runtime/context_resolution.py:203`
- `src/agent_runtime/context_resolution.py:204`
- `src/agent_runtime/context_resolution.py:206`
- `src/agent_runtime/context_resolution.py:210`

## `combine_observations` — function, line 193
- **called from:**
- `src/agent_runtime/context_resolution.py:138`
- `src/agent_runtime/context_resolution.py:494`
- `tests/test_context_resolution.py:163`
- `tests/test_context_resolution.py:173`
- `tests/test_context_resolution.py:183`
- `tests/test_context_resolution.py:195`
- `tests/test_context_resolution.py:206`
- `tests/test_context_resolution.py:215`
- `tests/test_context_resolution.py:223`
- `tests/test_context_resolution.py:234`
- `tests/test_context_resolution.py:445`
- `tests/test_context_resolution.py:473`
- `tests/test_context_resolution_route.py:281`
- `tests/test_context_resolution_route.py:350`
- `tests/test_context_resolution_route.py:368`

## `_ProbeResult` — class, line 225
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/context_resolution.py:420`

## `clear_probe_cache` — function, line 234
- **called from:**
- `tests/conftest.py:355`
- `tests/conftest.py:360`
- `tests/test_context_resolution.py:130`
- `tests/test_context_resolution.py:138`
- `tests/test_context_resolution.py:556`

## `_origin` — function, line 241
- **called from:**
- `src/agent_runtime/context_resolution.py:270`
- `src/agent_runtime/context_resolution.py:327`
- `src/agent_runtime/context_resolution.py:364`

## `_http_client` — function, line 251
- **called from:**
- `src/agent_runtime/context_resolution.py:328`

## `_provider_urls` — function, line 256
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_probe_headers` — function, line 268
- **called from:**
- `src/agent_runtime/context_resolution.py:332`
- `src/agent_runtime/context_resolution.py:340`
- `src/agent_runtime/context_resolution.py:366`

## `_auth_fingerprint` — function, line 279
- **called from:**
- `src/agent_runtime/context_resolution.py:437`

## `_serving_base` — function, line 290
- **called from:**
- `src/agent_runtime/context_resolution.py:330`

## `_get_json` — function (async), line 295
- **called from:**
- `src/agent_runtime/context_resolution.py:331`
- `src/agent_runtime/context_resolution.py:339`
- `src/agent_runtime/context_resolution.py:365`

## `_positive_int` — function, line 315
- **called from:**
- `src/agent_runtime/context_resolution.py:335`
- `src/agent_runtime/context_resolution.py:344`

## `_probe` — function (async), line 321
- **called from:**
- `src/agent_runtime/context_resolution.py:412`
- `tests/test_service_health_collect.py:270`
- `tests/test_service_health_collect.py:271`
- `tests/test_service_health_collect.py:272`
- `tests/test_service_health_collect.py:273`
- `tests/test_tool_approval_gate_default.py:41`
- `tests/test_tool_approval_gate_default.py:50`

## `probe_provider_context` — function (async), line 392
- **called from:**
- `src/agent_runtime/context_resolution.py:442`

## `_is_local` — function (async), line 423
- **called from:**
- `src/agent_runtime/context_resolution.py:408`
- `src/agent_runtime/context_resolution.py:436`
- `tests/test_local_endpoint_js.py:52`
- `tests/test_local_endpoint_js.py:63`

## `_cached_probe` — function (async), line 435
- **called from:**
- `src/agent_runtime/context_resolution.py:480`

## `declared_context_window` — function, line 452
- **called from:**
- `src/agent_runtime/context_resolution.py:486`

## `resolve_effective_context` — function (async), line 463
- **called from:**
- `routes/chat_routes.py:3312`
- `src/clean_agent_preview.py:5913`
- `tests/test_context_resolution.py:249`
- `tests/test_context_resolution.py:265`
- `tests/test_context_resolution.py:278`
- `tests/test_context_resolution.py:295`
- `tests/test_context_resolution.py:304`
- `tests/test_context_resolution.py:312`
- `tests/test_context_resolution.py:321`
- `tests/test_context_resolution.py:332`
- `tests/test_context_resolution.py:343`
- `tests/test_context_resolution.py:356`
- `tests/test_context_resolution.py:371`
- `tests/test_context_resolution.py:379`
- `tests/test_context_resolution.py:380`
- `tests/test_context_resolution.py:384`
- `tests/test_context_resolution.py:392`
- `tests/test_context_resolution.py:393`
- `tests/test_context_resolution.py:396`
- `tests/test_context_resolution.py:403`
- `tests/test_context_resolution.py:404`
- `tests/test_context_resolution.py:531`
- `tests/test_context_resolution.py:582`
- `tests/test_context_resolution.py:605`
- `tests/test_context_resolution.py:618`
- `tests/test_context_resolution_route.py:305`
- `tests/test_context_resolution_route.py:391`
- `tests/test_context_resolution_route.py:392`

## `context_metrics` — function, line 507
- **called from:**
- `src/clean_agent_preview.py:9007`
- `tests/test_context_resolution.py:219`
- `tests/test_context_resolution.py:235`
- `tests/test_context_resolution.py:608`
