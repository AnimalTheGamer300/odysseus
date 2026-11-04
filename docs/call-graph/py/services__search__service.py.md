# `services/search/service.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `SearchResult` — class, line 15
- decorator: `dataclass`
- **called from:**
- `services/search/service.py:83`

## `SearchResponse` — class, line 24
- decorator: `dataclass`
- **called from:**
- `services/search/service.py:90`

## `SearchService` — class, line 32
- **called from:**
- `tests/test_search_service_nondict_rows.py:20`
- `tests/test_searchservice_search_call.py:40`

## `SearchService.__init__` — method, line 43
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

## `SearchService.search` — method (async), line 47
- **called from:**
- `mcp_servers/email_server.py:427`
- `mcp_servers/email_server.py:433`
- `mcp_servers/email_server.py:446`
- `mcp_servers/email_server.py:530`
- `mcp_servers/email_server.py:599`
- `mcp_servers/email_server.py:1529`
- `routes/calendar_routes.py:1706`
- `routes/chat_helpers.py:66`
- `routes/chat_helpers.py:1148`
- `routes/chat_helpers.py:1176`
- `routes/chat_routes.py:493`
- `routes/chat_routes.py:495`
- `routes/chat_routes.py:500`
- `routes/chat_routes.py:502`
- `routes/chat_routes.py:550`
- `routes/chat_routes.py:1205`
- `routes/chat_routes.py:1209`
- `routes/contacts/contacts_routes.py:503`
- `routes/contacts/contacts_routes.py:507`
- `routes/contacts/contacts_routes.py:511`
- `routes/cookbook_helpers.py:680`
- `routes/cookbook_helpers.py:1129`
- `routes/cookbook_helpers.py:1132`
- `routes/cookbook_helpers.py:1436`
- `routes/cookbook_helpers.py:1438`
- `routes/cookbook_helpers.py:1438`
- `routes/cookbook_output.py:56`
- `routes/cookbook_routes.py:124`
- `routes/cookbook_routes.py:147`
- `routes/cookbook_routes.py:590`
- `routes/cookbook_routes.py:592`
- `routes/cookbook_routes.py:592`
- `routes/cookbook_routes.py:918`
- `routes/cookbook_routes.py:990`
- `routes/cookbook_routes.py:1528`
- `routes/cookbook_routes.py:1787`
- `routes/cookbook_routes.py:1788`
- `routes/cookbook_routes.py:1808`
- `routes/cookbook_routes.py:1823`
- `routes/cookbook_routes.py:2046`
- `routes/cookbook_routes.py:2173`
- `routes/cookbook_routes.py:2293`
- `routes/cookbook_routes.py:2684`
- `routes/cookbook_routes.py:3547`
- `routes/cookbook_routes.py:3751`
- `routes/cookbook_routes.py:3753`
- `routes/cookbook_routes.py:3755`
- `routes/cookbook_routes.py:3757`
- `routes/cookbook_routes.py:3763`
- `routes/cookbook_routes.py:3824`
- `routes/cookbook_routes.py:3827`
- `routes/cookbook_routes.py:3829`
- `routes/cookbook_routes.py:3973`
- `routes/cookbook_routes.py:4238`
- `routes/cookbook_routes.py:4488`
- `routes/cookbook_routes.py:4494`
- `routes/cookbook_routes.py:4513`
- `routes/document/document_helpers.py:227`
- `routes/document/document_routes.py:63`
- `routes/document/document_routes.py:64`
- … +326 more (grep the name in repo)

## `SearchService.fetch_content` — method (async), line 96
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SearchService.get_config` — method, line 100
- **called from:**
- `tests/test_email_oauth.py:911`
