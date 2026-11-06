# `src/agent_tools/document_tools.py` — definitions & call sites

42 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_document_search_tokens` — function, line 21
- **called from:**
- `src/agent_tools/document_tools.py:31`
- `src/agent_tools/document_tools.py:38`

## `_rank_document_search` — function, line 28
- **called from:**
- `src/agent_tools/document_tools.py:1142`

## `_missing_document_upload` — function, line 47
- **called from:**
- `src/agent_tools/document_tools.py:583`
- `src/agent_tools/document_tools.py:679`
- `src/agent_tools/document_tools.py:843`
- `src/agent_tools/document_tools.py:937`

## `set_active_document` — function, line 59
- **called from:**
- `mcp_servers/email_server.py:2863`
- `mcp_servers/email_server.py:2910`
- `src/agent_loop.py:14913`
- `src/agent_loop.py:15053`
- `src/agent_tools/document_tools.py:495`
- `src/agent_tools/document_tools.py:612`
- `src/agent_tools/document_tools.py:659`
- `src/agent_tools/document_tools.py:823`
- `src/agent_tools/document_tools.py:1172`
- `src/agent_tools/document_tools.py:1232`
- `src/office_doc.py:71`
- `src/pdf_form_doc.py:254`
- `src/pdf_form_doc.py:437`
- `tests/test_active_document_clear.py:16`
- `tests/test_active_document_clear.py:23`
- `tests/test_active_document_clear.py:30`
- `tests/test_active_document_clear.py:36`
- `tests/test_chat_document_owner_context.py:106`
- `tests/test_document_close_clears_active_route.py:78`
- `tests/test_document_close_clears_active_route.py:86`
- `tests/test_document_close_clears_active_route.py:95`
- `tests/test_document_followup_integrity.py:23`
- `tests/test_document_followup_integrity.py:31`
- `tests/test_document_followup_integrity.py:74`
- `tests/test_document_followup_integrity.py:93`
- `tests/test_document_read_pagination.py:28`
- `tests/test_document_tool_owner_scope.py:155`
- `tests/test_document_tool_owner_scope.py:161`
- `tests/test_document_tool_owner_scope.py:175`
- `tests/test_document_tool_owner_scope.py:181`
- `tests/test_document_tool_owner_scope.py:194`
- `tests/test_document_tool_owner_scope.py:201`
- `tests/test_document_tool_owner_scope.py:212`
- `tests/test_document_tool_owner_scope.py:221`
- `tests/test_document_tool_owner_scope.py:254`
- `tests/test_document_tool_owner_scope.py:260`
- `tests/test_owned_resource_identity.py:112`

## `set_active_model` — function, line 65
- **called from:**
- `src/agent_loop.py:14877`

## `get_active_model` — function, line 71
- **called from:**
- `src/agent_loop.py:4897`

## `get_active_document` — function, line 76
- **called from:**
- `routes/chat_routes.py:3435`
- `tests/test_active_document_clear.py:17`
- `tests/test_active_document_clear.py:19`
- `tests/test_active_document_clear.py:26`
- `tests/test_active_document_clear.py:32`
- `tests/test_active_document_clear.py:38`
- `tests/test_document_close_clears_active_route.py:80`
- `tests/test_document_close_clears_active_route.py:88`
- `tests/test_document_close_clears_active_route.py:97`
- `tests/test_document_followup_integrity.py:22`
- `tests/test_document_read_pagination.py:22`

## `clear_active_document` — function, line 80
- **called from:**
- `routes/document/document_routes.py:946`
- `routes/document/document_routes.py:975`
- `tests/test_active_document_clear.py:18`
- `tests/test_active_document_clear.py:25`
- `tests/test_active_document_clear.py:31`
- `tests/test_active_document_clear.py:37`

## `_owned_document_query` — function, line 98
- **called from:**
- `src/agent_tools/document_tools.py:112`
- `src/agent_tools/document_tools.py:120`
- `src/agent_tools/document_tools.py:1117`
- `tests/test_document_tool_owner_scope.py:85`
- `tests/test_document_tool_owner_scope.py:92`
- `tests/test_owned_document_query.py:20`
- `tests/test_owned_document_query.py:30`

## `_get_owned_document` — function, line 108
- **called from:**
- `src/agent_tools/document_tools.py:646`
- `src/agent_tools/document_tools.py:808`
- `src/agent_tools/document_tools.py:1011`
- `src/agent_tools/document_tools.py:1169`
- `src/agent_tools/document_tools.py:1217`

## `_most_recent_owned_document` — function, line 116
- **called from:**
- `src/agent_tools/document_tools.py:656`
- `src/agent_tools/document_tools.py:820`
- `src/agent_tools/document_tools.py:1222`

## `_approved_document_version_error` — function, line 124
- **called from:**
- `src/agent_tools/document_tools.py:652`
- `src/agent_tools/document_tools.py:664`
- `src/agent_tools/document_tools.py:814`
- `src/agent_tools/document_tools.py:828`
- `src/agent_tools/document_tools.py:1015`
- `src/agent_tools/document_tools.py:1225`
- `tests/test_tool_approvals.py:329`
- `tests/test_tool_approvals.py:333`
- `tests/test_tool_approvals.py:340`
- `tests/test_tool_approvals.py:347`

## `_sniff_doc_language` — function, line 162
- **called from:**
- `routes/document/document_routes.py:135`
- `src/agent_tools/document_tools.py:561`

## `_looks_like_email_document` — function, line 204
- **called from:**
- `routes/document/document_routes.py:138`
- `routes/document/document_routes.py:861`
- `routes/document/document_routes.py:862`
- `src/agent_tools/document_tools.py:172`
- `src/agent_tools/document_tools.py:278`
- `src/agent_tools/document_tools.py:562`
- `src/agent_tools/document_tools.py:668`
- `src/agent_tools/document_tools.py:832`

## `_split_email_header_body` — function, line 214
- **called from:**
- `src/agent_tools/document_tools.py:269`
- `src/agent_tools/document_tools.py:272`

## `_split_email_reply_history` — function, line 220
- **called from:**
- `src/agent_tools/document_tools.py:270`
- `src/agent_tools/document_tools.py:273`
- `src/agent_tools/document_tools.py:291`

## `_merge_email_headers` — function, line 246
- **called from:**
- `src/agent_tools/document_tools.py:276`

## `_coerce_email_document_content` — function, line 263
- **called from:**
- `routes/document/document_routes.py:164`
- `routes/document/document_routes.py:865`
- `src/agent_tools/document_tools.py:669`
- `src/agent_tools/document_tools.py:839`

## `parse_edit_blocks` — function, line 296
- **called from:**
- `src/agent_tools/document_tools.py:800`

## `parse_suggest_blocks` — function, line 323
- **called from:**
- `src/agent_tools/document_tools.py:1005`
- `tests/test_document_tool_owner_scope.py:231`

## `_stable_suggestion_id` — function, line 346
- **called from:**
- `src/agent_tools/document_tools.py:1046`
- `tests/test_document_tool_owner_scope.py:244`
- `tests/test_document_tool_owner_scope.py:244`
- `tests/test_document_tool_owner_scope.py:245`
- `tests/test_document_tool_owner_scope.py:245`
- `tests/test_document_tool_owner_scope.py:246`
- `tests/test_document_tool_owner_scope.py:246`

## `_visible_text_match_source` — function, line 355
- **called from:**
- `src/agent_tools/document_tools.py:1027`

## `_pdf_source_upload_id` — function, line 442
- **called from:**
- `src/agent_tools/document_tools.py:686`
- `src/agent_tools/document_tools.py:944`

## `_strip_pdf_editor_markers` — function, line 450
- **called from:**
- `src/agent_tools/document_tools.py:469`
- `tests/test_pdf_ai_edit_derivative.py:13`
- `tests/test_pdf_ai_edit_derivative.py:22`

## `_create_pdf_text_derivative` — function, line 465
- **called from:**
- `src/agent_tools/document_tools.py:687`
- `src/agent_tools/document_tools.py:945`

## `CreateDocumentTool` — class, line 507
- **called from:**
- `src/agent_tools/__init__.py:60`

## `CreateDocumentTool.execute` — method (async), line 508
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:539`
- `core/database.py:954`
- `core/database.py:957`
- `core/database.py:960`
- `core/database.py:972`
- `core/database.py:995`
- `core/database.py:997`
- `core/database.py:1017`
- `core/database.py:1019`
- `core/database.py:1039`
- `core/database.py:1041`
- `core/database.py:1060`
- `core/database.py:1068`
- `core/database.py:1085`
- `core/database.py:1088`
- `core/database.py:1109`
- `core/database.py:1112`
- `core/database.py:1113`
- `core/database.py:1133`
- `core/database.py:1136`
- `core/database.py:1156`
- `core/database.py:1159`
- `core/database.py:1186`
- `core/database.py:1189`
- `core/database.py:1190`
- `core/database.py:1211`
- `core/database.py:1214`
- `core/database.py:1215`
- `core/database.py:1236`
- `core/database.py:1239`
- `core/database.py:1259`
- `core/database.py:1262`
- `core/database.py:1264`
- `core/database.py:1266`
- `core/database.py:1268`
- `core/database.py:1287`
- `core/database.py:1290`
- `core/database.py:1310`
- `core/database.py:1313`
- `core/database.py:1334`
- `core/database.py:1337`
- `core/database.py:1358`
- `core/database.py:1361`
- `core/database.py:1380`
- `core/database.py:1383`
- `core/database.py:1406`
- `core/database.py:1423`
- `core/database.py:1426`
- `core/database.py:1428`
- `core/database.py:1430`
- `core/database.py:1432`
- `core/database.py:1434`
- `core/database.py:1436`
- `core/database.py:1455`
- `core/database.py:1458`
- `core/database.py:1478`
- … +725 more (grep the name in repo)

## `UpdateDocumentTool` — class, line 633
- **called from:**
- `src/agent_tools/__init__.py:61`
- `tests/test_tool_approvals.py:385`

## `UpdateDocumentTool.execute` — method (async), line 634
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:539`
- `core/database.py:954`
- `core/database.py:957`
- `core/database.py:960`
- `core/database.py:972`
- `core/database.py:995`
- `core/database.py:997`
- `core/database.py:1017`
- `core/database.py:1019`
- `core/database.py:1039`
- `core/database.py:1041`
- `core/database.py:1060`
- `core/database.py:1068`
- `core/database.py:1085`
- `core/database.py:1088`
- `core/database.py:1109`
- `core/database.py:1112`
- `core/database.py:1113`
- `core/database.py:1133`
- `core/database.py:1136`
- `core/database.py:1156`
- `core/database.py:1159`
- `core/database.py:1186`
- `core/database.py:1189`
- `core/database.py:1190`
- `core/database.py:1211`
- `core/database.py:1214`
- `core/database.py:1215`
- `core/database.py:1236`
- `core/database.py:1239`
- `core/database.py:1259`
- `core/database.py:1262`
- `core/database.py:1264`
- `core/database.py:1266`
- `core/database.py:1268`
- `core/database.py:1287`
- `core/database.py:1290`
- `core/database.py:1310`
- `core/database.py:1313`
- `core/database.py:1334`
- `core/database.py:1337`
- `core/database.py:1358`
- `core/database.py:1361`
- `core/database.py:1380`
- `core/database.py:1383`
- `core/database.py:1406`
- `core/database.py:1423`
- `core/database.py:1426`
- `core/database.py:1428`
- `core/database.py:1430`
- `core/database.py:1432`
- `core/database.py:1434`
- `core/database.py:1436`
- `core/database.py:1455`
- `core/database.py:1458`
- `core/database.py:1478`
- … +725 more (grep the name in repo)

## `_document_find_contexts` — function, line 723
- **called from:**
- `src/agent_tools/document_tools.py:748`
- `src/agent_tools/document_tools.py:1033`

## `_document_find_repair_hint` — function, line 745
- **called from:**
- `src/agent_tools/document_tools.py:924`
- `src/agent_tools/document_tools.py:926`
- `src/agent_tools/document_tools.py:983`
- `src/agent_tools/document_tools.py:1051`
- `tests/test_document_markup_repair.py:7`
- `tests/test_document_markup_repair.py:14`
- `tests/test_document_markup_repair.py:18`

## `SourceTags` — class, line 757
- **called from:**
- `src/agent_tools/document_tools.py:770`

## `SourceTags.__init__` — method, line 758
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

## `SourceTags.handle_starttag` — method, line 762
- **called from:**
- `src/agent_tools/document_tools.py:768`

## `SourceTags.handle_startendtag` — method, line 767
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EditDocumentTool` — class, line 791
- **called from:**
- `src/agent_tools/__init__.py:62`
- `tests/test_upload_handler_cleanup.py:692`

## `EditDocumentTool.execute` — method (async), line 792
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:539`
- `core/database.py:954`
- `core/database.py:957`
- `core/database.py:960`
- `core/database.py:972`
- `core/database.py:995`
- `core/database.py:997`
- `core/database.py:1017`
- `core/database.py:1019`
- `core/database.py:1039`
- `core/database.py:1041`
- `core/database.py:1060`
- `core/database.py:1068`
- `core/database.py:1085`
- `core/database.py:1088`
- `core/database.py:1109`
- `core/database.py:1112`
- `core/database.py:1113`
- `core/database.py:1133`
- `core/database.py:1136`
- `core/database.py:1156`
- `core/database.py:1159`
- `core/database.py:1186`
- `core/database.py:1189`
- `core/database.py:1190`
- `core/database.py:1211`
- `core/database.py:1214`
- `core/database.py:1215`
- `core/database.py:1236`
- `core/database.py:1239`
- `core/database.py:1259`
- `core/database.py:1262`
- `core/database.py:1264`
- `core/database.py:1266`
- `core/database.py:1268`
- `core/database.py:1287`
- `core/database.py:1290`
- `core/database.py:1310`
- `core/database.py:1313`
- `core/database.py:1334`
- `core/database.py:1337`
- `core/database.py:1358`
- `core/database.py:1361`
- `core/database.py:1380`
- `core/database.py:1383`
- `core/database.py:1406`
- `core/database.py:1423`
- `core/database.py:1426`
- `core/database.py:1428`
- `core/database.py:1430`
- `core/database.py:1432`
- `core/database.py:1434`
- `core/database.py:1436`
- `core/database.py:1455`
- `core/database.py:1458`
- `core/database.py:1478`
- … +725 more (grep the name in repo)

## `SuggestDocumentTool` — class, line 994
- **called from:**
- `src/agent_tools/__init__.py:63`

## `SuggestDocumentTool.execute` — method (async), line 995
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:539`
- `core/database.py:954`
- `core/database.py:957`
- `core/database.py:960`
- `core/database.py:972`
- `core/database.py:995`
- `core/database.py:997`
- `core/database.py:1017`
- `core/database.py:1019`
- `core/database.py:1039`
- `core/database.py:1041`
- `core/database.py:1060`
- `core/database.py:1068`
- `core/database.py:1085`
- `core/database.py:1088`
- `core/database.py:1109`
- `core/database.py:1112`
- `core/database.py:1113`
- `core/database.py:1133`
- `core/database.py:1136`
- `core/database.py:1156`
- `core/database.py:1159`
- `core/database.py:1186`
- `core/database.py:1189`
- `core/database.py:1190`
- `core/database.py:1211`
- `core/database.py:1214`
- `core/database.py:1215`
- `core/database.py:1236`
- `core/database.py:1239`
- `core/database.py:1259`
- `core/database.py:1262`
- `core/database.py:1264`
- `core/database.py:1266`
- `core/database.py:1268`
- `core/database.py:1287`
- `core/database.py:1290`
- `core/database.py:1310`
- `core/database.py:1313`
- `core/database.py:1334`
- `core/database.py:1337`
- `core/database.py:1358`
- `core/database.py:1361`
- `core/database.py:1380`
- `core/database.py:1383`
- `core/database.py:1406`
- `core/database.py:1423`
- `core/database.py:1426`
- `core/database.py:1428`
- `core/database.py:1430`
- `core/database.py:1432`
- `core/database.py:1434`
- `core/database.py:1436`
- `core/database.py:1455`
- `core/database.py:1458`
- `core/database.py:1478`
- … +725 more (grep the name in repo)

## `ManageDocumentTool` — class, line 1075
- **called from:**
- `src/agent_tools/__init__.py:64`

## `ManageDocumentTool.execute` — method (async), line 1076
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:539`
- `core/database.py:954`
- `core/database.py:957`
- `core/database.py:960`
- `core/database.py:972`
- `core/database.py:995`
- `core/database.py:997`
- `core/database.py:1017`
- `core/database.py:1019`
- `core/database.py:1039`
- `core/database.py:1041`
- `core/database.py:1060`
- `core/database.py:1068`
- `core/database.py:1085`
- `core/database.py:1088`
- `core/database.py:1109`
- `core/database.py:1112`
- `core/database.py:1113`
- `core/database.py:1133`
- `core/database.py:1136`
- `core/database.py:1156`
- `core/database.py:1159`
- `core/database.py:1186`
- `core/database.py:1189`
- `core/database.py:1190`
- `core/database.py:1211`
- `core/database.py:1214`
- `core/database.py:1215`
- `core/database.py:1236`
- `core/database.py:1239`
- `core/database.py:1259`
- `core/database.py:1262`
- `core/database.py:1264`
- `core/database.py:1266`
- `core/database.py:1268`
- `core/database.py:1287`
- `core/database.py:1290`
- `core/database.py:1310`
- `core/database.py:1313`
- `core/database.py:1334`
- `core/database.py:1337`
- `core/database.py:1358`
- `core/database.py:1361`
- `core/database.py:1380`
- `core/database.py:1383`
- `core/database.py:1406`
- `core/database.py:1423`
- `core/database.py:1426`
- `core/database.py:1428`
- `core/database.py:1430`
- `core/database.py:1432`
- `core/database.py:1434`
- `core/database.py:1436`
- `core/database.py:1455`
- `core/database.py:1458`
- `core/database.py:1478`
- … +725 more (grep the name in repo)

## `ManageDocumentTool._rel` — method, line 1100
- **called from:**
- `src/agent_tools/document_tools.py:1155`
- `src/agent_tools/session_tools.py:160`
