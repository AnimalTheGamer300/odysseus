# `services/memory/skill_format.py` — definitions & call sites

17 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `slugify` — function, line 65
- **called from:**
- `services/memory/skill_format.py:446`
- `services/memory/skills.py:77`
- `services/memory/skills.py:78`
- `services/memory/skills.py:247`
- `services/memory/skills.py:320`
- `services/memory/skills.py:400`
- `services/memory/skills.py:401`
- `services/memory/skills.py:481`
- `src/tools/system.py:170`
- `src/tools/system.py:200`
- `tests/test_skill_save_no_rename.py:29`
- `tests/test_skills_delete_owner.py:15`
- `tests/test_skills_manager_owner_isolation.py:49`
- `tests/test_skills_routes_owner_update.py:20`

## `_parse_scalar` — function, line 87
- **called from:**
- `services/memory/skill_format.py:95`
- `services/memory/skill_format.py:174`
- `services/memory/skill_format.py:182`
- `tests/test_skill_frontmatter_escape_roundtrip.py:129`
- `tests/test_skill_frontmatter_escape_roundtrip.py:150`

## `_split_top_level` — function, line 126
- **called from:**
- `services/memory/skill_format.py:95`

## `parse_frontmatter` — function, line 153
- **called from:**
- `services/memory/skill_format.py:443`
- `tests/test_skill_frontmatter_escape_roundtrip.py:186`

## `_emit_scalar` — function, line 206
- **called from:**
- `services/memory/skill_format.py:214`
- `services/memory/skill_format.py:248`
- `tests/test_skill_frontmatter_escape_roundtrip.py:98`
- `tests/test_skill_frontmatter_escape_roundtrip.py:140`
- `tests/test_skill_frontmatter_escape_roundtrip.py:141`
- `tests/test_skill_frontmatter_escape_roundtrip.py:142`
- `tests/test_skill_frontmatter_escape_roundtrip.py:143`
- `tests/test_skill_frontmatter_escape_roundtrip.py:144`

## `_as_list` — function, line 228
- **called from:**
- `services/memory/skill_format.py:452`
- `services/memory/skill_format.py:453`
- `services/memory/skill_format.py:454`
- `services/memory/skill_format.py:455`

## `_as_float` — function, line 236
- **called from:**
- `services/memory/skill_format.py:457`

## `emit_frontmatter` — function, line 243
- **called from:**
- `services/memory/skill_format.py:471`

## `parse_body` — function, line 272
- **called from:**
- `services/memory/skill_format.py:444`

## `_parse_list_lines` — function, line 313
- **called from:**
- `services/memory/skill_format.py:309`

## `emit_body` — function, line 332
- **called from:**
- `services/memory/skill_format.py:472`

## `Skill` — class, line 359
- decorator: `dataclass`
- **called from:**
- `services/memory/skills.py:360`
- `tests/test_skill_frontmatter_escape_roundtrip.py:61`
- `tests/test_skill_frontmatter_escape_roundtrip.py:73`
- `tests/test_skill_frontmatter_escape_roundtrip.py:89`
- `tests/test_skill_frontmatter_escape_roundtrip.py:154`
- `tests/test_skill_frontmatter_escape_roundtrip.py:179`

## `Skill.to_frontmatter` — method, line 389
- **called from:**
- `services/memory/skill_format.py:471`

## `Skill.to_dict` — method, line 408
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:3149`
- `services/memory/skills.py:226`
- `services/memory/skills.py:382`
- `services/memory/skills.py:430`
- `src/model_capabilities.py:538`
- `src/model_capability_readers/base.py:66`
- `src/model_capability_readers/base.py:67`
- `src/model_capability_readers/base.py:68`
- `tests/test_history_compact_tool_calls.py:90`
- `tests/test_model_capabilities.py:68`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:154`

## `Skill.from_markdown` — method, line 442
- decorator: `classmethod`
- **called from:**
- `routes/skills_routes.py:718`
- `routes/skills_routes.py:1818`
- `services/memory/skills.py:170`
- `services/memory/skills.py:399`
- `src/tools/system.py:167`
- `src/tools/system.py:197`
- `tests/test_skill_frontmatter_escape_roundtrip.py:41`
- `tests/test_skill_frontmatter_escape_roundtrip.py:111`
- `tests/test_skill_frontmatter_escape_roundtrip.py:119`

## `Skill.to_markdown` — method, line 470
- **called from:**
- `services/memory/skills.py:179`
- `services/memory/skills.py:428`
- `tests/test_skill_frontmatter_escape_roundtrip.py:41`
- `tests/test_skill_frontmatter_escape_roundtrip.py:89`
- `tests/test_skill_frontmatter_escape_roundtrip.py:179`

## `_now_iso` — function, line 482
- **called from:**
- `services/memory/skill_format.py:405`
- `services/memory/skill_format.py:461`
- `tests/test_skill_format_timestamp.py:28`
- `tests/test_skill_format_timestamp.py:34`
- `tests/test_skill_format_timestamp.py:48`
