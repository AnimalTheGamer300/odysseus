# `src/session_search.py` — definitions & call sites

19 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `SessionSearchResult` — class, line 23
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/session_search.py:202`
- `tests/test_session_search.py:350`

## `SessionSearchResult.to_dict` — method, line 34
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5624`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28789`
- `src/agent_loop.py:31316`
- `src/agent_loop.py:31789`
- `src/agent_loop.py:32054`
- `src/agent_loop.py:32094`
- `src/agent_loop.py:32125`
- `src/agent_loop.py:32178`
- `src/agent_loop.py:32306`
- `src/agent_loop.py:32638`
- `src/agent_loop.py:34858`
- `src/agent_loop.py:36867`
- `src/agent_loop.py:37190`
- `src/agent_loop.py:37403`
- `src/agent_loop.py:37458`
- `src/agent_loop.py:37515`
- `src/agent_loop.py:37849`
- `src/agent_loop.py:37861`
- `src/agent_loop.py:37967`
- `src/agent_loop.py:38889`
- `src/agent_loop.py:38890`
- `src/agent_loop.py:38895`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:653`
- `src/agent_runtime/authority.py:677`
- `src/agent_runtime/authority.py:677`
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

## `_iso` — function, line 47
- **called from:**
- `src/session_search.py:56`
- `src/session_search.py:209`

## `_message_to_context` — function, line 51
- **called from:**
- `src/session_search.py:191`
- `src/session_search.py:192`

## `escape_like_pattern` — function, line 60
- **called from:**
- `routes/gallery/gallery_routes.py:1230`
- `routes/gallery/gallery_routes.py:1246`
- `src/session_search.py:70`

## `_escape_like` — function, line 69
- **called from:**
- `routes/document/document_routes.py:575`
- `src/session_search.py:227`
- `src/session_search.py:273`

## `_snippet` — function, line 73
- **called from:**
- `src/session_search.py:208`
- `src/session_search.py:242`
- `src/session_search.py:293`
- `tests/test_session_search.py:67`
- `tests/test_session_search.py:77`
- `tests/test_session_search.py:85`
- `tests/test_session_search.py:94`
- `tests/test_session_search.py:100`

## `_query_terms` — function, line 96
- **called from:**
- `src/session_search.py:82`

## `_sanitize_fts_query` — function, line 107
- **called from:**
- `src/session_search.py:328`

## `_is_sqlite_session` — function, line 136
- **called from:**
- `src/session_search.py:145`

## `_has_fts_table` — function, line 144
- **called from:**
- `src/session_search.py:329`

## `_owner_filter` — function, line 157
- **called from:**
- `routes/gallery/gallery_routes.py:1166`
- `routes/gallery/gallery_routes.py:1199`
- `routes/gallery/gallery_routes.py:1212`
- `routes/gallery/gallery_routes.py:1222`
- `routes/gallery/gallery_routes.py:1328`
- `routes/gallery/gallery_routes.py:1335`
- `routes/gallery/gallery_routes.py:1340`
- `routes/gallery/gallery_routes.py:1347`
- `routes/gallery/gallery_routes.py:1390`
- `routes/gallery/gallery_routes.py:1391`
- `routes/gallery/gallery_routes.py:1392`
- `routes/gallery/gallery_routes.py:1420`
- `routes/gallery/gallery_routes.py:1564`
- `routes/gallery/gallery_routes.py:1589`
- `routes/gallery/gallery_routes.py:1616`
- `src/session_search.py:240`
- `src/session_search.py:278`
- `tests/test_gallery_owner_filter_single_user.py:41`
- `tests/test_gallery_owner_filter_single_user.py:51`
- `tests/test_gallery_owner_filter_single_user.py:52`
- `tests/test_gallery_owner_filter_single_user.py:62`
- `tests/test_null_owner_gates.py:150`
- `tests/test_null_owner_gates.py:159`
- `tests/test_null_owner_gates.py:167`

## `_context_for_message` — function, line 165
- **called from:**
- `src/session_search.py:199`

## `_rows_to_results` — function, line 196
- **called from:**
- `src/session_search.py:243`
- `src/session_search.py:294`
- `src/session_search.py:379`

## `_search_like` — function, line 217
- **called from:**
- `src/session_search.py:419`
- `src/session_search.py:439`

## `search_session_titles` — function, line 246
- **called from:**
- `src/tools/search.py:36`

## `_fetch_messages_by_id` — function, line 300
- **called from:**
- `src/session_search.py:372`
- `tests/test_session_search_batch_fetch.py:44`
- `tests/test_session_search_batch_fetch.py:54`

## `_search_fts` — function, line 318
- **called from:**
- `src/session_search.py:408`

## `search_session_messages` — function, line 382
- **called from:**
- `routes/chat_routes.py:5625`
- `src/tools/search.py:30`
- `src/tools/search.py:49`
- `tests/test_session_search.py:115`
- `tests/test_session_search.py:135`
- `tests/test_session_search.py:154`
- `tests/test_session_search.py:171`
- `tests/test_session_search.py:193`
- `tests/test_session_search.py:208`
- `tests/test_session_search.py:225`
- `tests/test_session_search.py:242`
- `tests/test_session_search.py:264`
