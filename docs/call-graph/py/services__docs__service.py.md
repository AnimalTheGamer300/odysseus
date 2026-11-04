# `services/docs/service.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `DocChunk` — class, line 12
- decorator: `dataclass`
- **called from:**
- `services/docs/service.py:84`

## `IndexResult` — class, line 21
- decorator: `dataclass`
- **called from:**
- `services/docs/service.py:105`

## `DocsService` — class, line 28
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DocsService.__init__` — method, line 38
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

## `DocsService.query` — method (async), line 41
- **called from:**
- `app.py:320`
- `app.py:446`
- `app.py:526`
- `app.py:1042`
- `app.py:1044`
- `app.py:1168`
- `companion/routes.py:135`
- `core/auth.py:309`
- `core/database.py:534`
- `core/database.py:2699`
- `core/database.py:2713`
- `core/database.py:2714`
- `core/database.py:2715`
- `core/database.py:2716`
- `core/database.py:2717`
- `core/database.py:2742`
- `core/database.py:2757`
- `core/database.py:2770`
- `core/database.py:2779`
- `core/database.py:2791`
- `core/database.py:2810`
- `core/session_manager.py:137`
- `core/session_manager.py:150`
- `core/session_manager.py:264`
- `core/session_manager.py:368`
- `core/session_manager.py:462`
- `core/session_manager.py:496`
- `core/session_manager.py:525`
- `core/session_manager.py:530`
- `core/session_manager.py:615`
- `core/session_manager.py:623`
- `core/session_manager.py:630`
- `core/session_manager.py:667`
- `core/session_manager.py:702`
- `core/session_manager.py:732`
- `core/session_manager.py:767`
- `core/session_manager.py:799`
- `core/session_manager.py:936`
- `core/session_manager.py:964`
- `core/session_manager.py:990`
- `core/session_manager.py:1020`
- `core/session_manager.py:1087`
- `core/session_manager.py:1092`
- `core/session_manager.py:1095`
- `core/session_manager.py:1133`
- `core/session_manager.py:1156`
- `core/session_manager.py:1187`
- `core/session_manager.py:1222`
- `core/session_manager.py:1242`
- `core/session_manager.py:1259`
- `core/session_manager.py:1329`
- `mcp_servers/email_server.py:1645`
- `routes/admin_wipe/admin_wipe_routes.py:79`
- `routes/admin_wipe/admin_wipe_routes.py:80`
- `routes/admin_wipe/admin_wipe_routes.py:81`
- `routes/admin_wipe/admin_wipe_routes.py:90`
- `routes/admin_wipe/admin_wipe_routes.py:91`
- `routes/admin_wipe/admin_wipe_routes.py:127`
- `routes/admin_wipe/admin_wipe_routes.py:128`
- `routes/admin_wipe/admin_wipe_routes.py:134`
- … +623 more (grep the name in repo)

## `DocsService.index` — method (async), line 94
- **called from:**
- `routes/api_token_routes.py:63`
- `routes/calendar_routes.py:579`
- `routes/cookbook_helpers.py:324`
- `routes/cookbook_routes.py:660`
- `routes/history/history_routes.py:443`
- `services/hwfit/profiles.py:155`
- `services/youtube/youtube_handler.py:198`
- `src/builtin_mcp.py:265`
- `src/llm_core.py:1609`
- `src/webhook_manager.py:292`
- `tests/test_active_email_reply_guard.py:6`
- `tests/test_active_email_reply_guard.py:7`
- `tests/test_admin_device_flow_static.py:12`
- `tests/test_admin_device_flow_static.py:13`
- `tests/test_agent_thread_dot_alignment_css.py:35`
- `tests/test_approved_replay_message_shape.py:76`
- `tests/test_approved_replay_message_shape.py:76`
- `tests/test_approved_replay_message_shape.py:77`
- `tests/test_approved_replay_message_shape.py:77`
- `tests/test_chat_stream_scope.py:7`
- `tests/test_chat_stream_scope.py:8`
- `tests/test_compare_ask_user_routing.py:57`
- `tests/test_compare_ask_user_routing.py:58`
- `tests/test_compare_stop_disconnect_poll.py:456`
- `tests/test_compare_stop_disconnect_poll.py:457`
- `tests/test_compare_stop_disconnect_poll.py:458`
- `tests/test_cookbook_helpers.py:579`
- `tests/test_cookbook_helpers.py:579`
- `tests/test_cookbook_helpers.py:658`
- `tests/test_cookbook_helpers.py:658`
- `tests/test_cookbook_helpers.py:701`
- `tests/test_cookbook_helpers.py:701`
- `tests/test_cookbook_helpers.py:705`
- `tests/test_cookbook_helpers.py:705`
- `tests/test_cookbook_helpers.py:725`
- `tests/test_cookbook_helpers.py:725`
- `tests/test_cookbook_helpers.py:753`
- `tests/test_cookbook_helpers.py:753`
- `tests/test_cookbook_local_serve_pid_winpid.py:162`
- `tests/test_cookbook_local_serve_pid_winpid.py:163`
- `tests/test_cookbook_local_serve_pid_winpid.py:172`
- `tests/test_cookbook_local_serve_pid_winpid.py:175`
- `tests/test_cookbook_same_host_server_profiles_js.py:54`
- `tests/test_cookbook_same_host_server_profiles_js.py:54`
- `tests/test_cookbook_windows_stop_tree_js.py:10`
- `tests/test_cookbook_windows_stop_tree_js.py:11`
- `tests/test_copy_message_strips_thinking_js.py:158`
- `tests/test_delete_message_after_refresh.py:309`
- `tests/test_delete_message_no_session.py:19`
- `tests/test_deleted_session_sidebar_regression.py:10`
- `tests/test_deleted_session_sidebar_regression.py:11`
- `tests/test_doc_library_open_orphaned.py:44`
- `tests/test_doc_library_open_orphaned.py:45`
- `tests/test_docker_devops_hardening.py:85`
- `tests/test_docker_devops_hardening.py:86`
- `tests/test_docker_devops_hardening.py:89`
- `tests/test_docker_devops_hardening.py:92`
- `tests/test_docker_devops_hardening.py:93`
- `tests/test_docker_devops_hardening.py:94`
- `tests/test_docker_devops_hardening.py:95`
- … +133 more (grep the name in repo)

## `DocsService.add_document` — method (async), line 111
- **called from:**
- `routes/personal_routes.py:381`
- `services/docs/service.py:113`
- `src/rag_manager.py:66`
- `src/rag_vector.py:540`
- `tests/test_embedding_lanes_rag.py:26`

## `DocsService.get_stats` — method, line 115
- **called from:**
- `routes/diagnostics_routes.py:70`
- `routes/stt_routes.py:20`
- `routes/tts_routes.py:25`
- `scripts/index_documents.py:103`
- `services/docs/service.py:117`
- `services/research/research_handler.py:281`
- `src/rag_manager.py:62`
- `src/research_handler.py:364`
- `src/research_handler.py:388`
- `src/research_handler.py:845`
- `src/task_scheduler.py:2081`
- `tests/test_tts_cache_stats.py:10`
- `tests/test_tts_speed_malformed.py:22`

## `DocsService.rebuild_index` — method, line 119
- **called from:**
- `services/docs/service.py:121`
- `src/rag_manager.py:58`
- `tests/test_embedding_lanes_rag.py:106`
