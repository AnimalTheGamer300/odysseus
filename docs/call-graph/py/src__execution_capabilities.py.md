# `src/execution_capabilities.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `VerifierCapability` — class, line 11
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/execution_capabilities.py:52`

## `VerifierCapability.to_dict` — method, line 16
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5643`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28809`
- `src/agent_loop.py:31336`
- `src/agent_loop.py:31809`
- `src/agent_loop.py:32074`
- `src/agent_loop.py:32114`
- `src/agent_loop.py:32145`
- `src/agent_loop.py:32198`
- `src/agent_loop.py:32326`
- `src/agent_loop.py:32658`
- `src/agent_loop.py:34878`
- `src/agent_loop.py:36887`
- `src/agent_loop.py:37210`
- `src/agent_loop.py:37423`
- `src/agent_loop.py:37478`
- `src/agent_loop.py:37535`
- `src/agent_loop.py:37869`
- `src/agent_loop.py:37881`
- `src/agent_loop.py:37987`
- `src/agent_loop.py:38909`
- `src/agent_loop.py:38910`
- `src/agent_loop.py:38915`
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

## `ExecutionCapabilities` — class, line 21
- decorator: `dataclass(frozen=True)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ExecutionCapabilities.from_probe` — method, line 29
- decorator: `classmethod`
- **called from:**
- `tests/test_execution_capabilities.py:5`
- `tests/test_execution_capabilities.py:33`

## `ExecutionCapabilities.verifier_commands` — method, line 71
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ExecutionCapabilities.to_dict` — method, line 74
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5643`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28809`
- `src/agent_loop.py:31336`
- `src/agent_loop.py:31809`
- `src/agent_loop.py:32074`
- `src/agent_loop.py:32114`
- `src/agent_loop.py:32145`
- `src/agent_loop.py:32198`
- `src/agent_loop.py:32326`
- `src/agent_loop.py:32658`
- `src/agent_loop.py:34878`
- `src/agent_loop.py:36887`
- `src/agent_loop.py:37210`
- `src/agent_loop.py:37423`
- `src/agent_loop.py:37478`
- `src/agent_loop.py:37535`
- `src/agent_loop.py:37869`
- `src/agent_loop.py:37881`
- `src/agent_loop.py:37987`
- `src/agent_loop.py:38909`
- `src/agent_loop.py:38910`
- `src/agent_loop.py:38915`
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

## `_safe_source_path` — function, line 84
- **called from:**
- `src/execution_capabilities.py:48`

## `verifier_prompt` — function, line 91
- **called from:**
- `tests/test_execution_capabilities.py:43`
