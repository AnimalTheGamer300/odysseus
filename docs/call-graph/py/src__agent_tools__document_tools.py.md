# `src/agent_tools/document_tools.py` — definitions & call sites

32 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_missing_document_upload` — function, line 12
- **called from:**
- `src/agent_tools/document_tools.py:433`
- `src/agent_tools/document_tools.py:521`
- `src/agent_tools/document_tools.py:615`
- `src/agent_tools/document_tools.py:673`

## `set_active_document` — function, line 24
- **called from:**
- `src/agent_loop.py:2754`
- `src/agent_loop.py:2894`
- `src/agent_tools/document_tools.py:345`
- `src/agent_tools/document_tools.py:462`
- `src/agent_tools/document_tools.py:507`
- `src/agent_tools/document_tools.py:595`
- `src/agent_tools/document_tools.py:885`
- `src/office_doc.py:66`
- `src/pdf_form_doc.py:251`
- `src/pdf_form_doc.py:434`
- `tests/test_active_document_clear.py:16`
- `tests/test_active_document_clear.py:23`
- `tests/test_active_document_clear.py:30`
- `tests/test_active_document_clear.py:36`
- `tests/test_document_close_clears_active_route.py:78`
- `tests/test_document_close_clears_active_route.py:86`
- `tests/test_document_close_clears_active_route.py:95`
- `tests/test_document_tool_owner_scope.py:124`
- `tests/test_document_tool_owner_scope.py:130`
- `tests/test_document_tool_owner_scope.py:140`
- `tests/test_document_tool_owner_scope.py:149`

## `set_active_model` — function, line 30
- **called from:**
- `src/agent_loop.py:2719`

## `get_active_model` — function, line 36
- **called from:**
- `src/agent_loop.py:3470`

## `get_active_document` — function, line 41
- **called from:**
- `routes/chat_routes.py:1656`
- `tests/test_active_document_clear.py:17`
- `tests/test_active_document_clear.py:19`
- `tests/test_active_document_clear.py:26`
- `tests/test_active_document_clear.py:32`
- `tests/test_active_document_clear.py:38`
- `tests/test_document_close_clears_active_route.py:80`
- `tests/test_document_close_clears_active_route.py:88`
- `tests/test_document_close_clears_active_route.py:97`

## `clear_active_document` — function, line 45
- **called from:**
- `routes/document/document_routes.py:722`
- `routes/document/document_routes.py:751`
- `tests/test_active_document_clear.py:18`
- `tests/test_active_document_clear.py:25`
- `tests/test_active_document_clear.py:31`
- `tests/test_active_document_clear.py:37`

## `_owned_document_query` — function, line 63
- **called from:**
- `src/agent_tools/document_tools.py:77`
- `src/agent_tools/document_tools.py:85`
- `src/agent_tools/document_tools.py:806`
- `tests/test_document_tool_owner_scope.py:83`
- `tests/test_document_tool_owner_scope.py:90`
- `tests/test_owned_document_query.py:20`
- `tests/test_owned_document_query.py:30`

## `_get_owned_document` — function, line 73
- **called from:**
- `src/agent_tools/document_tools.py:496`
- `src/agent_tools/document_tools.py:582`
- `src/agent_tools/document_tools.py:736`
- `src/agent_tools/document_tools.py:837`
- `src/agent_tools/document_tools.py:875`

## `_most_recent_owned_document` — function, line 81
- **called from:**
- `src/agent_tools/document_tools.py:504`
- `src/agent_tools/document_tools.py:592`
- `src/agent_tools/document_tools.py:878`

## `_approved_document_version_error` — function, line 89
- **called from:**
- `src/agent_tools/document_tools.py:502`
- `src/agent_tools/document_tools.py:512`
- `src/agent_tools/document_tools.py:588`
- `src/agent_tools/document_tools.py:600`
- `src/agent_tools/document_tools.py:740`
- `tests/test_tool_approvals.py:293`
- `tests/test_tool_approvals.py:297`
- `tests/test_tool_approvals.py:304`
- `tests/test_tool_approvals.py:311`

## `_sniff_doc_language` — function, line 127
- **called from:**
- `routes/document/document_routes.py:130`
- `src/agent_tools/document_tools.py:411`

## `_looks_like_email_document` — function, line 169
- **called from:**
- `routes/document/document_routes.py:133`
- `routes/document/document_routes.py:637`
- `routes/document/document_routes.py:638`
- `src/agent_tools/document_tools.py:137`
- `src/agent_tools/document_tools.py:243`
- `src/agent_tools/document_tools.py:412`
- `src/agent_tools/document_tools.py:516`
- `src/agent_tools/document_tools.py:604`

## `_split_email_header_body` — function, line 179
- **called from:**
- `src/agent_tools/document_tools.py:234`
- `src/agent_tools/document_tools.py:237`

## `_split_email_reply_history` — function, line 185
- **called from:**
- `src/agent_tools/document_tools.py:235`
- `src/agent_tools/document_tools.py:238`
- `src/agent_tools/document_tools.py:256`

## `_merge_email_headers` — function, line 211
- **called from:**
- `src/agent_tools/document_tools.py:241`

## `_coerce_email_document_content` — function, line 228
- **called from:**
- `routes/document/document_routes.py:159`
- `routes/document/document_routes.py:641`
- `src/agent_tools/document_tools.py:517`
- `src/agent_tools/document_tools.py:611`

## `parse_edit_blocks` — function, line 261
- **called from:**
- `src/agent_tools/document_tools.py:574`

## `parse_suggest_blocks` — function, line 269
- **called from:**
- `src/agent_tools/document_tools.py:730`

## `_pdf_source_upload_id` — function, line 292
- **called from:**
- `src/agent_tools/document_tools.py:528`
- `src/agent_tools/document_tools.py:680`

## `_strip_pdf_editor_markers` — function, line 300
- **called from:**
- `src/agent_tools/document_tools.py:319`
- `tests/test_pdf_ai_edit_derivative.py:13`
- `tests/test_pdf_ai_edit_derivative.py:22`

## `_create_pdf_text_derivative` — function, line 315
- **called from:**
- `src/agent_tools/document_tools.py:529`
- `src/agent_tools/document_tools.py:681`

## `CreateDocumentTool` — class, line 357
- **called from:**
- `src/agent_tools/__init__.py:51`

## `CreateDocumentTool.execute` — method (async), line 358
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `UpdateDocumentTool` — class, line 483
- **called from:**
- `src/agent_tools/__init__.py:52`
- `tests/test_tool_approvals.py:343`

## `UpdateDocumentTool.execute` — method (async), line 484
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `EditDocumentTool` — class, line 565
- **called from:**
- `src/agent_tools/__init__.py:53`
- `tests/test_upload_handler_cleanup.py:692`

## `EditDocumentTool.execute` — method (async), line 566
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `SuggestDocumentTool` — class, line 719
- **called from:**
- `src/agent_tools/__init__.py:54`

## `SuggestDocumentTool.execute` — method (async), line 720
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `ManageDocumentTool` — class, line 768
- **called from:**
- `src/agent_tools/__init__.py:55`

## `ManageDocumentTool.execute` — method (async), line 769
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `ManageDocumentTool._rel` — method, line 789
- **called from:**
- `src/agent_tools/document_tools.py:823`
- `src/agent_tools/session_tools.py:146`
