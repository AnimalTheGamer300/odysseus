# `services/memory/skill_format.py` — definitions & call sites

17 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `slugify` — function, line 65
- **called from:**
- `routes/skills_routes.py:841`
- `services/memory/skill_format.py:455`
- `services/memory/skills.py:98`
- `services/memory/skills.py:99`
- `services/memory/skills.py:314`
- `services/memory/skills.py:391`
- `services/memory/skills.py:471`
- `services/memory/skills.py:472`
- `services/memory/skills.py:565`
- `src/tools/system.py:176`
- `src/tools/system.py:208`
- `tests/test_skill_save_no_rename.py:29`
- `tests/test_skills_delete_owner.py:15`
- `tests/test_skills_manager_owner_isolation.py:30`
- `tests/test_skills_routes_owner_update.py:20`

## `_parse_scalar` — function, line 87
- **called from:**
- `services/memory/skill_format.py:99`
- `services/memory/skill_format.py:183`
- `services/memory/skill_format.py:191`
- `tests/test_skill_frontmatter_escape_roundtrip.py:129`
- `tests/test_skill_frontmatter_escape_roundtrip.py:150`

## `_split_top_level` — function, line 130
- **called from:**
- `services/memory/skill_format.py:99`

## `parse_frontmatter` — function, line 162
- **called from:**
- `services/memory/skill_format.py:452`
- `tests/test_skill_frontmatter_escape_roundtrip.py:186`
- `tests/test_skill_frontmatter_list_escapes.py:38`
- `tests/test_skill_frontmatter_list_escapes.py:43`
- `tests/test_skill_frontmatter_list_escapes.py:49`
- `tests/test_skill_version_preservation.py:34`

## `_emit_scalar` — function, line 215
- **called from:**
- `services/memory/skill_format.py:223`
- `services/memory/skill_format.py:257`
- `tests/test_skill_frontmatter_escape_roundtrip.py:98`
- `tests/test_skill_frontmatter_escape_roundtrip.py:140`
- `tests/test_skill_frontmatter_escape_roundtrip.py:141`
- `tests/test_skill_frontmatter_escape_roundtrip.py:142`
- `tests/test_skill_frontmatter_escape_roundtrip.py:143`
- `tests/test_skill_frontmatter_escape_roundtrip.py:144`

## `_as_list` — function, line 237
- **called from:**
- `services/memory/skill_format.py:461`
- `services/memory/skill_format.py:462`
- `services/memory/skill_format.py:463`
- `services/memory/skill_format.py:464`

## `_as_float` — function, line 245
- **called from:**
- `services/memory/skill_format.py:466`

## `emit_frontmatter` — function, line 252
- **called from:**
- `services/memory/skill_format.py:480`
- `tests/test_skill_frontmatter_list_escapes.py:37`
- `tests/test_skill_frontmatter_list_escapes.py:48`

## `parse_body` — function, line 281
- **called from:**
- `services/memory/skill_format.py:453`

## `_parse_list_lines` — function, line 322
- **called from:**
- `services/memory/skill_format.py:318`

## `emit_body` — function, line 341
- **called from:**
- `services/memory/skill_format.py:481`

## `Skill` — class, line 368
- decorator: `dataclass`
- **called from:**
- `services/memory/skills.py:431`
- `tests/test_skill_frontmatter_escape_roundtrip.py:61`
- `tests/test_skill_frontmatter_escape_roundtrip.py:73`
- `tests/test_skill_frontmatter_escape_roundtrip.py:89`
- `tests/test_skill_frontmatter_escape_roundtrip.py:154`
- `tests/test_skill_frontmatter_escape_roundtrip.py:179`
- `tests/test_skill_frontmatter_list_escapes.py:20`
- `tests/test_skill_frontmatter_list_escapes.py:29`

## `Skill.to_frontmatter` — method, line 398
- **called from:**
- `services/memory/skill_format.py:480`

## `Skill.to_dict` — method, line 417
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

## `Skill.from_markdown` — method, line 451
- decorator: `classmethod`
- **called from:**
- `routes/skills_routes.py:790`
- `services/memory/builtin_skills.py:50`
- `services/memory/skills.py:218`
- `services/memory/skills.py:470`
- `services/skills/publication.py:332`
- `src/tools/system.py:173`
- `src/tools/system.py:205`
- `tests/test_skill_frontmatter_escape_roundtrip.py:41`
- `tests/test_skill_frontmatter_escape_roundtrip.py:111`
- `tests/test_skill_frontmatter_escape_roundtrip.py:119`
- `tests/test_skill_frontmatter_list_escapes.py:22`
- `tests/test_skill_frontmatter_list_escapes.py:30`
- `tests/test_skill_version_preservation.py:27`
- `tests/test_skill_version_preservation.py:46`

## `Skill.to_markdown` — method, line 479
- **called from:**
- `services/memory/skills.py:227`
- `services/memory/skills.py:499`
- `tests/test_skill_frontmatter_escape_roundtrip.py:41`
- `tests/test_skill_frontmatter_escape_roundtrip.py:89`
- `tests/test_skill_frontmatter_escape_roundtrip.py:179`
- `tests/test_skill_frontmatter_list_escapes.py:22`
- `tests/test_skill_frontmatter_list_escapes.py:30`
- `tests/test_skill_version_preservation.py:30`

## `_now_iso` — function, line 491
- **called from:**
- `services/memory/skill_format.py:414`
- `services/memory/skill_format.py:470`
- `tests/test_skill_format_timestamp.py:28`
- `tests/test_skill_format_timestamp.py:34`
- `tests/test_skill_format_timestamp.py:48`
