# `src/search_intent.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `reference_lookup_without_date_window` — function, line 5
- **called from:**
- `src/clean_agent_preview.py:5232`
- `src/search_intent.py:34`
- `tests/test_search_publication_intent.py:28`

## `requested_search_publication_window` — function, line 19
- **called from:**
- `src/clean_agent_preview.py:5236`
- `src/search_intent.py:31`

## `inferred_search_publication_window` — function, line 29
- **called from:**
- `src/agent_tools/web_tools.py:329`
- `src/agent_tools/web_tools_prewave3.py:333`
- `src/clean_agent_preview.py:5245`
- `tests/test_search_publication_intent.py:19`
