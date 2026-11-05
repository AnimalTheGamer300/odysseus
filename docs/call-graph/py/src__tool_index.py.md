# `src/tool_index.py` — definitions & call sites

18 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ToolIndex` — class, line 214
- **called from:**
- `src/tool_index.py:821`
- `tests/test_embedding_lanes_tool_index.py:28`

## `ToolIndex.__init__` — method, line 217
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email/email_helpers.py:205`
- `routes/email/email_helpers.py:220`
- `routes/email/email_helpers.py:232`
- `routes/email/email_helpers.py:248`
- `routes/email/email_routes.py:1664`
- `scripts/css_snapshot.py:194`
- `scripts/probe_browser_budget.py:56`
- `src/agent_tools/document_tools.py:759`
- `src/agent_tools/filesystem_tools.py:384`
- `src/builtin_actions.py:552`
- `src/chatgpt_subscription.py:495`
- `src/containment.py:170`
- `src/outbound_fetch.py:220`
- `src/path_confinement.py:81`
- `src/process_ownership.py:110`
- `src/report_math.py:31`
- `tests/conftest.py:199`
- `tests/test_admin_routes_auth_disabled.py:16`
- `tests/test_agent_state_dir_confinement.py:799`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_action_planning.py:11`
- `tests/test_deep_research_browser_fallback.py:10`
- `tests/test_deep_research_browser_fallback.py:29`
- `tests/test_deep_research_browser_fallback.py:56`
- `tests/test_deep_research_extraction_controls.py:13`
- `tests/test_deep_research_full_loop_navigation.py:11`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_llm_core_streaming.py:50`
- `tests/test_retired_settings_interfaces.py:31`
- `tests/test_searxng_ca_validation.py:35`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:155`

## `ToolIndex.healthy` — method, line 233
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ToolIndex.embedding_lanes` — method, line 237
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ToolIndex._embed` — method, line 241
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ToolIndex.index_builtin_tools` — method, line 249
- **called from:**
- `src/tool_index.py:822`
- `tests/test_embedding_lanes_tool_index.py:29`
- `tests/test_embedding_lanes_tool_index.py:65`

## `ToolIndex.index_mcp_tools` — method, line 297
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ToolIndex.retrieve` — method, line 372
- **called from:**
- `src/rag_manager.py:54`
- `src/tool_index.py:620`
- `src/tool_index.py:857`
- `tests/test_embedding_lanes_tool_index.py:33`
- `tests/test_embedding_lanes_tool_index.py:116`
- `tests/test_embedding_lanes_tool_index.py:178`

## `ToolIndex.get_tools_for_query` — method, line 615
- **called from:**
- `tests/test_tool_index_keyword_boundaries.py:27`
- `tests/test_tool_index_keyword_boundaries.py:36`
- `tests/test_tool_index_keyword_boundaries.py:46`
- `tests/test_tool_index_keyword_boundaries.py:55`
- `tests/test_tool_index_keyword_boundaries.py:56`
- `tests/test_tool_index_keyword_boundaries.py:57`
- `tests/test_tool_index_keyword_boundaries.py:62`
- `tests/test_tool_index_keyword_boundaries.py:73`
- `tests/test_tool_index_multilingual_literal_hints.py:20`
- `tests/test_tool_index_multilingual_literal_hints.py:25`
- `tests/test_tool_index_multilingual_literal_hints.py:26`
- `tests/test_tool_index_multilingual_literal_hints.py:30`
- `tests/test_tool_rag_keyword_hints.py:36`
- `tests/test_tool_rag_keyword_hints.py:47`
- `tests/test_tool_rag_keyword_hints.py:55`
- `tests/test_tool_rag_keyword_hints.py:62`

## `_utc_now` — function, line 734
- **called from:**
- `src/tool_index.py:814`
- `src/tool_index.py:827`
- `src/tool_index.py:841`
- `src/tool_index.py:865`

## `_set_status` — function, line 738
- **called from:**
- `src/tool_index.py:810`
- `src/tool_index.py:824`
- `src/tool_index.py:838`
- `src/tool_index.py:859`
- `src/tool_index.py:862`

## `_lane_readiness` — function, line 743
- **called from:**
- `src/tool_index.py:831`
- `src/tool_index.py:866`

## `get_tool_index_status` — function, line 763
- **called from:**
- `src/readiness.py:73`
- `src/tool_index.py:808`
- `src/tool_index.py:855`
- `src/tool_index.py:869`
- `tests/test_tool_index_lifecycle.py:94`
- `tests/test_tool_index_lifecycle.py:108`
- `tests/test_tool_index_lifecycle.py:117`
- `tests/test_tool_index_lifecycle.py:156`

## `get_ready_tool_index` — function, line 774
- **called from:**
- `src/skill_index.py:85`
- `tests/test_tool_index_lifecycle.py:82`

## `tool_index_prewarm_enabled` — function, line 784
- **called from:**
- `app.py:1267`
- `src/readiness.py:74`
- `tests/test_tool_index_lifecycle.py:146`

## `get_tool_index` — function, line 791
- **called from:**
- `src/tool_index.py:853`
- `tests/test_tool_index_lifecycle.py:90`
- `tests/test_tool_index_lifecycle.py:107`
- `tests/test_tool_index_lifecycle.py:115`
- `tests/test_tool_index_lifecycle.py:123`

## `prewarm_tool_index` — function, line 851
- **called from:**
- `tests/test_tool_index_lifecycle.py:65`
- `tests/test_tool_index_lifecycle.py:126`
- `tests/test_tool_index_lifecycle.py:152`

## `reset_tool_index` — function, line 874
- **called from:**
- `routes/embedding_routes.py:321`
- `routes/embedding_routes.py:362`
- `tests/test_tool_index_lifecycle.py:28`
- `tests/test_tool_index_lifecycle.py:30`
- `tests/test_tool_index_lifecycle.py:154`
