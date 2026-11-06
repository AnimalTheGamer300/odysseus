# `src/text_scanning.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `iter_prefixed_token_matches` — function, line 15
- **called from:**
- `src/clean_agent_preview.py:4692`
- `src/text_scanning.py:50`
- `tests/test_codeql_induced_redos.py:141`

## `has_prefixed_token_match` — function, line 42
- **called from:**
- `src/agent_loop.py:7512`
- `src/agent_loop.py:7521`
- `src/turn_contract.py:67`
- `src/turn_contract.py:76`

## `contains_search_engine_navigation` — function, line 71
- **called from:**
- `src/clean_agent_preview.py:8224`
- `tests/test_redos_core_parsers.py:262`
- `tests/test_redos_core_parsers.py:510`

## `contains_detailed_sequence_request` — function, line 103
- **called from:**
- `src/agent_loop.py:31117`
- `src/clean_agent_preview.py:7276`
- `tests/test_redos_core_parsers.py:311`
- `tests/test_redos_core_parsers.py:312`

## `iter_angle_contents` — function, line 130
- **called from:**
- `src/agent_loop.py:12099`
- `src/agent_loop.py:12421`
- `src/agent_loop.py:12477`
- `src/agent_loop.py:12578`
- `tests/test_redos_core_parsers.py:400`

## `iter_markdown_links` — function, line 144
- **called from:**
- `src/agent_loop.py:3009`
- `src/agent_loop.py:3186`
- `src/agent_loop.py:4726`
- `src/agent_loop.py:6536`
- `src/agent_loop.py:12824`
- `src/text_scanning.py:177`
- `tests/test_redos_core_parsers.py:389`

## `replace_markdown_links_with_labels` — function, line 175
- **called from:**
- `src/agent_loop.py:13363`
- `tests/test_redos_core_parsers.py:396`

## `first_tag_content` — function, line 189
- **called from:**
- `src/agent_loop.py:30732`
- `tests/test_redos_core_parsers.py:467`

## `space_delimited_fields` — function, line 213
- **called from:**
- `src/agent_loop.py:2674`
- `src/agent_loop.py:2821`

## `terminal_dot_field` — function, line 256
- **called from:**
- `src/agent_loop.py:2621`
- `src/agent_loop.py:2819`
