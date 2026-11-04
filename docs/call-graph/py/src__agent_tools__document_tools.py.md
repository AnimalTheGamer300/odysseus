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
- `core/database.py:502`
- `core/database.py:895`
- `core/database.py:898`
- `core/database.py:901`
- `core/database.py:913`
- `core/database.py:936`
- `core/database.py:939`
- `core/database.py:960`
- `core/database.py:963`
- `core/database.py:964`
- `core/database.py:984`
- `core/database.py:987`
- `core/database.py:1007`
- `core/database.py:1010`
- `core/database.py:1037`
- `core/database.py:1040`
- `core/database.py:1041`
- `core/database.py:1062`
- `core/database.py:1065`
- `core/database.py:1066`
- `core/database.py:1087`
- `core/database.py:1090`
- `core/database.py:1110`
- `core/database.py:1113`
- `core/database.py:1115`
- `core/database.py:1117`
- `core/database.py:1119`
- `core/database.py:1138`
- `core/database.py:1141`
- `core/database.py:1161`
- `core/database.py:1164`
- `core/database.py:1185`
- `core/database.py:1188`
- `core/database.py:1207`
- `core/database.py:1210`
- `core/database.py:1230`
- `core/database.py:1233`
- `core/database.py:1235`
- `core/database.py:1237`
- `core/database.py:1239`
- `core/database.py:1241`
- `core/database.py:1243`
- `core/database.py:1262`
- `core/database.py:1265`
- `core/database.py:1285`
- `core/database.py:1288`
- `core/database.py:1308`
- `core/database.py:1311`
- `core/database.py:1312`
- `core/database.py:1332`
- `core/database.py:1335`
- `core/database.py:1336`
- `core/database.py:1368`
- `core/database.py:1370`
- `core/database.py:1396`
- `core/database.py:1398`
- … +332 more (grep the name in repo)

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
- `core/database.py:502`
- `core/database.py:895`
- `core/database.py:898`
- `core/database.py:901`
- `core/database.py:913`
- `core/database.py:936`
- `core/database.py:939`
- `core/database.py:960`
- `core/database.py:963`
- `core/database.py:964`
- `core/database.py:984`
- `core/database.py:987`
- `core/database.py:1007`
- `core/database.py:1010`
- `core/database.py:1037`
- `core/database.py:1040`
- `core/database.py:1041`
- `core/database.py:1062`
- `core/database.py:1065`
- `core/database.py:1066`
- `core/database.py:1087`
- `core/database.py:1090`
- `core/database.py:1110`
- `core/database.py:1113`
- `core/database.py:1115`
- `core/database.py:1117`
- `core/database.py:1119`
- `core/database.py:1138`
- `core/database.py:1141`
- `core/database.py:1161`
- `core/database.py:1164`
- `core/database.py:1185`
- `core/database.py:1188`
- `core/database.py:1207`
- `core/database.py:1210`
- `core/database.py:1230`
- `core/database.py:1233`
- `core/database.py:1235`
- `core/database.py:1237`
- `core/database.py:1239`
- `core/database.py:1241`
- `core/database.py:1243`
- `core/database.py:1262`
- `core/database.py:1265`
- `core/database.py:1285`
- `core/database.py:1288`
- `core/database.py:1308`
- `core/database.py:1311`
- `core/database.py:1312`
- `core/database.py:1332`
- `core/database.py:1335`
- `core/database.py:1336`
- `core/database.py:1368`
- `core/database.py:1370`
- `core/database.py:1396`
- `core/database.py:1398`
- … +332 more (grep the name in repo)

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
- `core/database.py:502`
- `core/database.py:895`
- `core/database.py:898`
- `core/database.py:901`
- `core/database.py:913`
- `core/database.py:936`
- `core/database.py:939`
- `core/database.py:960`
- `core/database.py:963`
- `core/database.py:964`
- `core/database.py:984`
- `core/database.py:987`
- `core/database.py:1007`
- `core/database.py:1010`
- `core/database.py:1037`
- `core/database.py:1040`
- `core/database.py:1041`
- `core/database.py:1062`
- `core/database.py:1065`
- `core/database.py:1066`
- `core/database.py:1087`
- `core/database.py:1090`
- `core/database.py:1110`
- `core/database.py:1113`
- `core/database.py:1115`
- `core/database.py:1117`
- `core/database.py:1119`
- `core/database.py:1138`
- `core/database.py:1141`
- `core/database.py:1161`
- `core/database.py:1164`
- `core/database.py:1185`
- `core/database.py:1188`
- `core/database.py:1207`
- `core/database.py:1210`
- `core/database.py:1230`
- `core/database.py:1233`
- `core/database.py:1235`
- `core/database.py:1237`
- `core/database.py:1239`
- `core/database.py:1241`
- `core/database.py:1243`
- `core/database.py:1262`
- `core/database.py:1265`
- `core/database.py:1285`
- `core/database.py:1288`
- `core/database.py:1308`
- `core/database.py:1311`
- `core/database.py:1312`
- `core/database.py:1332`
- `core/database.py:1335`
- `core/database.py:1336`
- `core/database.py:1368`
- `core/database.py:1370`
- `core/database.py:1396`
- `core/database.py:1398`
- … +332 more (grep the name in repo)

## `SuggestDocumentTool` — class, line 719
- **called from:**
- `src/agent_tools/__init__.py:54`

## `SuggestDocumentTool.execute` — method (async), line 720
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:502`
- `core/database.py:895`
- `core/database.py:898`
- `core/database.py:901`
- `core/database.py:913`
- `core/database.py:936`
- `core/database.py:939`
- `core/database.py:960`
- `core/database.py:963`
- `core/database.py:964`
- `core/database.py:984`
- `core/database.py:987`
- `core/database.py:1007`
- `core/database.py:1010`
- `core/database.py:1037`
- `core/database.py:1040`
- `core/database.py:1041`
- `core/database.py:1062`
- `core/database.py:1065`
- `core/database.py:1066`
- `core/database.py:1087`
- `core/database.py:1090`
- `core/database.py:1110`
- `core/database.py:1113`
- `core/database.py:1115`
- `core/database.py:1117`
- `core/database.py:1119`
- `core/database.py:1138`
- `core/database.py:1141`
- `core/database.py:1161`
- `core/database.py:1164`
- `core/database.py:1185`
- `core/database.py:1188`
- `core/database.py:1207`
- `core/database.py:1210`
- `core/database.py:1230`
- `core/database.py:1233`
- `core/database.py:1235`
- `core/database.py:1237`
- `core/database.py:1239`
- `core/database.py:1241`
- `core/database.py:1243`
- `core/database.py:1262`
- `core/database.py:1265`
- `core/database.py:1285`
- `core/database.py:1288`
- `core/database.py:1308`
- `core/database.py:1311`
- `core/database.py:1312`
- `core/database.py:1332`
- `core/database.py:1335`
- `core/database.py:1336`
- `core/database.py:1368`
- `core/database.py:1370`
- `core/database.py:1396`
- `core/database.py:1398`
- … +332 more (grep the name in repo)

## `ManageDocumentTool` — class, line 768
- **called from:**
- `src/agent_tools/__init__.py:55`

## `ManageDocumentTool.execute` — method (async), line 769
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:502`
- `core/database.py:895`
- `core/database.py:898`
- `core/database.py:901`
- `core/database.py:913`
- `core/database.py:936`
- `core/database.py:939`
- `core/database.py:960`
- `core/database.py:963`
- `core/database.py:964`
- `core/database.py:984`
- `core/database.py:987`
- `core/database.py:1007`
- `core/database.py:1010`
- `core/database.py:1037`
- `core/database.py:1040`
- `core/database.py:1041`
- `core/database.py:1062`
- `core/database.py:1065`
- `core/database.py:1066`
- `core/database.py:1087`
- `core/database.py:1090`
- `core/database.py:1110`
- `core/database.py:1113`
- `core/database.py:1115`
- `core/database.py:1117`
- `core/database.py:1119`
- `core/database.py:1138`
- `core/database.py:1141`
- `core/database.py:1161`
- `core/database.py:1164`
- `core/database.py:1185`
- `core/database.py:1188`
- `core/database.py:1207`
- `core/database.py:1210`
- `core/database.py:1230`
- `core/database.py:1233`
- `core/database.py:1235`
- `core/database.py:1237`
- `core/database.py:1239`
- `core/database.py:1241`
- `core/database.py:1243`
- `core/database.py:1262`
- `core/database.py:1265`
- `core/database.py:1285`
- `core/database.py:1288`
- `core/database.py:1308`
- `core/database.py:1311`
- `core/database.py:1312`
- `core/database.py:1332`
- `core/database.py:1335`
- `core/database.py:1336`
- `core/database.py:1368`
- `core/database.py:1370`
- `core/database.py:1396`
- `core/database.py:1398`
- … +332 more (grep the name in repo)

## `ManageDocumentTool._rel` — method, line 789
- **called from:**
- `src/agent_tools/document_tools.py:823`
- `src/agent_tools/session_tools.py:146`
