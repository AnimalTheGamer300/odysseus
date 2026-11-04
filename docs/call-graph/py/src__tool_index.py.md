# `src/tool_index.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ToolIndex` — class, line 157
- **called from:**
- `src/tool_index.py:627`
- `tests/test_embedding_lanes_tool_index.py:28`

## `ToolIndex.__init__` — method, line 160
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email_routes.py:1455`
- `src/builtin_actions.py:428`
- `src/outbound_fetch.py:220`
- `tests/test_agent_state_dir_confinement.py:648`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_extraction_controls.py:14`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_retired_settings_interfaces.py:30`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:148`

## `ToolIndex.healthy` — method, line 176
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ToolIndex._embed` — method, line 179
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ToolIndex.index_builtin_tools` — method, line 187
- **called from:**
- `src/tool_index.py:628`
- `tests/test_embedding_lanes_tool_index.py:29`
- `tests/test_embedding_lanes_tool_index.py:65`

## `ToolIndex.index_mcp_tools` — method, line 235
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ToolIndex.retrieve` — method, line 310
- **called from:**
- `src/rag_manager.py:54`
- `src/tool_index.py:534`
- `tests/test_embedding_lanes_tool_index.py:33`
- `tests/test_embedding_lanes_tool_index.py:116`
- `tests/test_embedding_lanes_tool_index.py:178`

## `ToolIndex.get_tools_for_query` — method, line 529
- **called from:**
- `tests/test_tool_index_keyword_boundaries.py:27`
- `tests/test_tool_index_keyword_boundaries.py:36`
- `tests/test_tool_index_keyword_boundaries.py:46`
- `tests/test_tool_index_keyword_boundaries.py:55`
- `tests/test_tool_index_keyword_boundaries.py:56`
- `tests/test_tool_index_keyword_boundaries.py:57`
- `tests/test_tool_index_keyword_boundaries.py:62`
- `tests/test_tool_rag_keyword_hints.py:36`
- `tests/test_tool_rag_keyword_hints.py:47`
- `tests/test_tool_rag_keyword_hints.py:55`
- `tests/test_tool_rag_keyword_hints.py:62`

## `get_tool_index` — function, line 614
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `reset_tool_index` — function, line 636
- **called from:**
- `routes/embedding_routes.py:321`
- `routes/embedding_routes.py:362`
