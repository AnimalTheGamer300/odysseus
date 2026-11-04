# `src/auth_helpers.py` — definitions & call sites

12 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `get_current_user` — function, line 10
- **called from:**
- `app.py:522`
- `companion/routes.py:41`
- `companion/routes.py:207`
- `routes/api_token_routes.py:126`
- `routes/api_token_routes.py:158`
- `routes/api_token_routes.py:198`
- `routes/assistant_routes.py:84`
- `routes/backup_routes.py:23`
- `routes/backup_routes.py:67`
- `routes/chat_routes.py:525`
- `routes/chat_routes.py:554`
- `routes/chat_routes.py:1295`
- `routes/chatgpt_subscription_routes.py:124`
- `routes/cleanup/cleanup_routes.py:30`
- `routes/cleanup/cleanup_routes.py:48`
- `routes/compare/compare_routes.py:244`
- `routes/compare/compare_routes.py:286`
- `routes/compare/compare_routes.py:323`
- `routes/compare/compare_routes.py:349`
- `routes/cookbook_routes.py:1394`
- `routes/cookbook_routes.py:2818`
- `routes/copilot_routes.py:127`
- `routes/document/document_routes.py:333`
- `routes/document/document_routes.py:447`
- `routes/document/document_routes.py:471`
- `routes/document/document_routes.py:485`
- `routes/document/document_routes.py:512`
- `routes/document/document_routes.py:564`
- `routes/document/document_routes.py:625`
- `routes/document/document_routes.py:700`
- `routes/document/document_routes.py:739`
- `routes/document/document_routes.py:767`
- `routes/document/document_routes.py:792`
- `routes/document/document_routes.py:813`
- `routes/document/document_routes.py:855`
- `routes/document/document_routes.py:975`
- `routes/document/document_routes.py:1073`
- `routes/document/document_routes.py:1137`
- `routes/document/document_routes.py:1204`
- `routes/document/document_routes.py:1259`
- `routes/document/document_routes.py:1407`
- `routes/document/document_routes.py:1505`
- `routes/document/document_routes.py:1642`
- `routes/editor_draft_routes.py:83`
- `routes/editor_draft_routes.py:96`
- `routes/editor_draft_routes.py:113`
- `routes/editor_draft_routes.py:139`
- `routes/editor_draft_routes.py:171`
- `routes/email_helpers.py:423`
- `routes/gallery/gallery_routes.py:363`
- `routes/gallery/gallery_routes.py:437`
- `routes/gallery/gallery_routes.py:482`
- `routes/gallery/gallery_routes.py:519`
- `routes/gallery/gallery_routes.py:654`
- `routes/gallery/gallery_routes.py:686`
- `routes/gallery/gallery_routes.py:814`
- `routes/gallery/gallery_routes.py:853`
- `routes/gallery/gallery_routes.py:873`
- `routes/gallery/gallery_routes.py:903`
- `routes/gallery/gallery_routes.py:922`
- … +28 more (grep the name in repo)

## `effective_user` — function, line 15
- **called from:**
- `routes/calendar_routes.py:811`
- `routes/chat_helpers.py:200`
- `routes/chat_helpers.py:222`
- `routes/chat_helpers.py:481`
- `routes/chat_helpers.py:762`
- `routes/chat_routes.py:952`
- `routes/chat_routes.py:1348`
- `routes/chat_routes.py:1500`
- `routes/chat_routes.py:1528`
- `routes/chat_routes.py:3147`
- `routes/history/history_routes.py:138`
- `routes/history/history_routes.py:1053`
- `routes/model_routes.py:1631`
- `routes/preset_routes.py:105`
- `routes/session_routes.py:145`
- `routes/session_routes.py:284`
- `routes/session_routes.py:403`
- `routes/session_routes.py:493`
- `routes/session_routes.py:557`
- `routes/session_routes.py:696`
- `routes/session_routes.py:913`
- `routes/session_routes.py:1046`
- `routes/session_routes.py:1064`
- `routes/session_routes.py:1148`
- `routes/session_routes.py:1220`
- `routes/upload_routes.py:290`
- `routes/upload_routes.py:372`
- `routes/upload_routes.py:461`
- `routes/upload_routes.py:507`
- `src/auth_helpers.py:92`
- `src/auth_helpers.py:110`
- `tests/test_session_owner_attribution.py:78`
- `tests/test_session_owner_attribution.py:83`
- `tests/test_session_owner_attribution.py:88`

## `_is_api_token_request` — function, line 39
- **called from:**
- `src/auth_helpers.py:57`
- `src/auth_helpers.py:67`
- `src/auth_helpers.py:91`
- `src/auth_helpers.py:132`

## `is_delegated_credential` — function, line 44
- **called from:**
- `routes/chat_routes.py:110`
- `routes/chat_routes.py:1679`
- `routes/session_routes.py:173`
- `routes/session_routes.py:212`
- `routes/session_routes.py:1059`

## `require_api_token_scope` — function, line 60
- **called from:**
- `routes/chat_routes.py:930`
- `routes/chat_routes.py:1124`
- `src/auth_helpers.py:80`

## `require_chat_api_token_scope` — function, line 78
- **called from:**
- `tests/test_api_token_tool_authority.py:177`
- `tests/test_api_token_tool_authority.py:188`

## `require_authenticated_request` — function, line 83
- **called from:**
- `routes/codex_routes.py:220`
- `routes/codex_routes.py:893`
- `tests/test_api_token_user_route_gate.py:41`

## `_auth_disabled` — function, line 96
- **called from:**
- `companion/routes.py:130`
- `routes/document/document_helpers.py:83`
- `routes/document/document_helpers.py:111`
- `routes/document/document_routes.py:451`
- `routes/email_helpers.py:426`
- `routes/gallery/gallery_helpers.py:134`
- `routes/model_routes.py:1636`
- `routes/research/research_routes.py:219`
- `routes/session_routes.py:146`
- `routes/session_routes.py:1221`
- `src/auth_helpers.py:144`
- `src/task_action_policy.py:20`
- `src/tool_security.py:253`

## `storage_owner_for_request` — function, line 103
- **called from:**
- `tests/test_owner_identity.py:37`
- `tests/test_owner_identity.py:53`
- `tests/test_owner_identity.py:63`

## `require_user` — function, line 113
- **called from:**
- `routes/calendar_routes.py:75`
- `routes/codex_routes.py:96`
- `routes/codex_routes.py:110`
- `routes/history/history_routes.py:931`
- `routes/memory/memory_routes.py:241`
- `routes/note/note_routes.py:598`
- `routes/note/note_routes.py:852`
- `src/auth_helpers.py:93`
- `src/auth_helpers.py:172`
- `tests/test_api_token_user_route_gate.py:32`
- `tests/test_api_token_user_route_gate.py:51`
- `tests/test_security_regressions.py:544`
- `tests/test_security_regressions.py:598`
- `tests/test_security_regressions.py:631`
- `tests/test_security_regressions.py:663`
- `tests/test_security_regressions.py:695`

## `require_privilege` — function, line 163
- **called from:**
- `routes/document/document_routes.py:108`
- `routes/document/document_routes.py:244`
- `routes/gallery/gallery_routes.py:565`
- `routes/gallery/gallery_routes.py:609`
- `routes/gallery/gallery_routes.py:1263`
- `routes/gallery/gallery_routes.py:1522`
- `routes/gallery/gallery_routes.py:1718`
- `routes/gallery/gallery_routes.py:1742`
- `routes/gallery/gallery_routes.py:1793`
- `routes/gallery/gallery_routes.py:1845`
- `routes/gallery/gallery_routes.py:1977`
- `routes/gallery/gallery_routes.py:2059`
- `routes/memory/memory_routes.py:107`
- `routes/memory/memory_routes.py:347`
- `routes/personal_routes.py:324`
- `routes/research/research_routes.py:496`
- `tests/test_auth_require_privilege_nondict.py:29`
- `tests/test_auth_require_privilege_nondict.py:36`

## `owner_filter` — function, line 191
- **called from:**
- `routes/chat_helpers.py:533`
- `routes/chat_helpers.py:608`
- `routes/chat_routes.py:594`
- `routes/chat_routes.py:659`
- `routes/chat_routes.py:728`
- `routes/chat_routes.py:843`
- `routes/compare/compare_routes.py:39`
- `routes/compare/compare_routes.py:57`
- `routes/gallery/gallery_routes.py:296`
- `routes/model_routes.py:1560`
- `routes/model_routes.py:2470`
- `routes/model_routes.py:2480`
- `routes/research/research_routes.py:174`
- `routes/session_routes.py:334`
- `routes/session_routes.py:354`
- `routes/session_routes.py:363`
- `routes/session_routes.py:423`
- `routes/session_routes.py:572`
- `routes/webhook/webhook_routes.py:40`
- `src/agent_loop.py:1075`
- `src/agent_tools/model_interaction_tools.py:140`
- `src/agent_tools/spawn_agent_tools.py:88`
- `src/ai_interaction.py:128`
- `src/ai_interaction.py:999`
- `src/builtin_actions.py:1811`
- `src/builtin_actions.py:1816`
- `src/builtin_actions.py:2165`
- `src/endpoint_resolver.py:403`
- `src/endpoint_resolver.py:459`
- `src/endpoint_resolver.py:548`
- `src/llm_core.py:2149`
- `src/task_scheduler.py:1877`
- `src/task_scheduler.py:2053`
