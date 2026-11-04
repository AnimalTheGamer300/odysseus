# `src/session_search.py` — definitions & call sites

16 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `SessionSearchResult` — class, line 23
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/session_search.py:174`
- `tests/test_session_search.py:278`

## `SessionSearchResult.to_dict` — method, line 34
- **called from:**
- `core/models.py:164`
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

## `_iso` — function, line 47
- **called from:**
- `src/session_search.py:56`
- `src/session_search.py:181`

## `_message_to_context` — function, line 51
- **called from:**
- `src/session_search.py:163`
- `src/session_search.py:164`

## `_escape_like` — function, line 60
- **called from:**
- `src/session_search.py:199`

## `_snippet` — function, line 64
- **called from:**
- `src/session_search.py:180`
- `src/session_search.py:214`

## `_sanitize_fts_query` — function, line 79
- **called from:**
- `src/session_search.py:246`

## `_is_sqlite_session` — function, line 108
- **called from:**
- `src/session_search.py:117`

## `_has_fts_table` — function, line 116
- **called from:**
- `src/session_search.py:247`

## `_owner_filter` — function, line 129
- **called from:**
- `routes/gallery/gallery_routes.py:660`
- `routes/gallery/gallery_routes.py:693`
- `routes/gallery/gallery_routes.py:706`
- `routes/gallery/gallery_routes.py:716`
- `routes/gallery/gallery_routes.py:818`
- `routes/gallery/gallery_routes.py:825`
- `routes/gallery/gallery_routes.py:830`
- `routes/gallery/gallery_routes.py:837`
- `routes/gallery/gallery_routes.py:880`
- `routes/gallery/gallery_routes.py:881`
- `routes/gallery/gallery_routes.py:882`
- `routes/gallery/gallery_routes.py:910`
- `routes/gallery/gallery_routes.py:1054`
- `routes/gallery/gallery_routes.py:1079`
- `routes/gallery/gallery_routes.py:1106`
- `src/session_search.py:212`
- `tests/test_gallery_owner_filter_single_user.py:41`
- `tests/test_gallery_owner_filter_single_user.py:51`
- `tests/test_gallery_owner_filter_single_user.py:52`
- `tests/test_gallery_owner_filter_single_user.py:62`
- `tests/test_null_owner_gates.py:150`
- `tests/test_null_owner_gates.py:159`
- `tests/test_null_owner_gates.py:167`

## `_context_for_message` — function, line 137
- **called from:**
- `src/session_search.py:171`

## `_rows_to_results` — function, line 168
- **called from:**
- `src/session_search.py:215`
- `src/session_search.py:297`

## `_search_like` — function, line 189
- **called from:**
- `src/session_search.py:337`
- `src/session_search.py:357`

## `_fetch_messages_by_id` — function, line 218
- **called from:**
- `src/session_search.py:290`
- `tests/test_session_search_batch_fetch.py:44`
- `tests/test_session_search_batch_fetch.py:54`

## `_search_fts` — function, line 236
- **called from:**
- `src/session_search.py:326`

## `search_session_messages` — function, line 300
- **called from:**
- `routes/chat_routes.py:3150`
- `src/tools/search.py:25`
- `tests/test_session_search.py:74`
- `tests/test_session_search.py:94`
- `tests/test_session_search.py:113`
- `tests/test_session_search.py:130`
- `tests/test_session_search.py:152`
- `tests/test_session_search.py:167`
- `tests/test_session_search.py:184`
- `tests/test_session_search.py:201`
- `tests/test_session_search.py:223`
