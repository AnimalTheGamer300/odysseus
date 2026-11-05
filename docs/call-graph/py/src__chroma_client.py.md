# `src/chroma_client.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_port_open` — function, line 22
- **called from:**
- `src/chroma_client.py:52`
- `tests/test_chroma_client.py:25`
- `tests/test_chroma_client.py:36`

## `get_chroma_client` — function, line 31
- **called from:**
- `scripts/migrate_faiss_to_chroma.py:92`
- `scripts/migrate_faiss_to_chroma.py:145`
- `src/embedding_lanes.py:256`
- `src/embedding_lanes.py:283`
- `src/memory_vector.py:93`
- `src/memory_vector.py:196`
- `src/rag_vector.py:163`
- `src/rag_vector.py:448`
- `tests/test_chroma_client.py:47`

## `reset_client` — function, line 70
- **called from:**
- `routes/embedding_routes.py:328`
- `routes/embedding_routes.py:369`
- `tests/test_chroma_client.py:43`
