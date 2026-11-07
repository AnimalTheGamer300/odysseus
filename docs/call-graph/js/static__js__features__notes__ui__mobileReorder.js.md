# `static/js/features/notes/ui/mobileReorder.js` — definitions & call sites

11 definitions (regex-based, best-effort).
**Exports:** `createMobileReorder`

## `createMobileReorder` — function, line 2
- **called from:**
- `static/js/features/notes/index.js:450`
- `static/js/features/notes/ui/mobileReorder.js:2`

## `_bindLongPressDrag` — function, line 9
- **called from:**
- `static/js/features/notes/index.js:180`
- `static/js/features/notes/index.js:180`
- `static/js/features/notes/ui/cardInteractions.js:62`
- `static/js/features/notes/ui/mobileReorder.js:9`

## `cancel` — arrow, line 39
- **called from:**
- `app.py:1459`
- `app.py:1470`
- `routes/editor_agent_routes.py:1414`
- `routes/email/email_routes.py:6869`
- `routes/history/history_routes.py:613`
- `routes/shell_routes.py:957`
- `routes/shell_routes.py:1342`
- `services/research/research_handler.py:140`
- `services/research/research_handler.py:143`
- `services/shell/service.py:163`
- `services/skills/job_coordinator.py:215`
- `src/agent_loop.py:26037`
- `src/agent_loop.py:34383`
- `src/agent_runs.py:86`
- `src/agent_runs.py:207`
- `src/agent_runs.py:210`
- `src/agent_runs.py:249`
- `src/agent_runs.py:298`
- `src/agent_runs.py:315`
- `src/ai_interaction.py:1822`
- `src/ai_interaction.py:2094`
- `src/clean_agent_preview.py:5609`
- `src/clean_agent_preview.py:5617`
- `src/containment.py:1172`
- `src/containment.py:1182`
- `src/llm_core.py:141`
- `src/mcp_manager.py:440`
- `src/mcp_oauth.py:63`
- `src/research_handler.py:502`
- `src/research_handler.py:505`
- `src/task_scheduler.py:122`
- `src/task_scheduler.py:733`
- `src/task_scheduler.py:741`
- `src/task_scheduler.py:1063`
- `src/task_scheduler.py:1145`
- `src/task_scheduler.py:2470`
- `src/task_scheduler.py:2495`
- `tests/test_agent_editor_routes.py:1008`
- `tests/test_agent_editor_routes.py:1962`
- `tests/test_agent_editor_routes.py:1971`
- `tests/test_browser_identity_transport.py:39`
- `tests/test_browser_identity_transport.py:75`
- `tests/test_builtin_mcp_bg_tasks.py:101`
- `tests/test_client_tool_routing.py:867`
- `tests/test_compare_stop_disconnect_poll.py:377`
- `tests/test_compare_stop_disconnect_poll.py:434`
- `tests/test_completion_boundary.py:319`
- `tests/test_completion_boundary.py:324`
- `tests/test_containment_enforcement.py:382`
- `tests/test_containment_enforcement.py:384`
- `tests/test_containment_enforcement.py:408`
- `tests/test_containment_enforcement.py:410`
- `tests/test_cookbook_cache_scan_isolation.py:102`
- `tests/test_email_summary_llm.py:192`
- `tests/test_email_urgency_checkpoint.py:457`
- `tests/test_email_urgency_checkpoint.py:592`
- `tests/test_host_shell_polling.py:198`
- `tests/test_nested_invocation_ownership.py:93`
- `tests/test_nested_invocation_ownership.py:96`
- `tests/test_nested_invocation_ownership.py:448`
- … +84 more (grep the name in repo)

## `_enterDragMode` — function, line 52
- **called from:**
- `static/js/features/notes/ui/mobileReorder.js:52`

## `_exitDragMode` — function, line 69
- **called from:**
- `static/js/features/notes/ui/mobileReorder.js:69`

## `_setupDragForCard` — function, line 78
- **called from:**
- `static/js/features/notes/ui/mobileReorder.js:78`

## `_beginGrab` — function, line 91
- **called from:**
- `static/js/features/notes/ui/mobileReorder.js:65`
- `static/js/features/notes/ui/mobileReorder.js:87`
- `static/js/features/notes/ui/mobileReorder.js:91`

## `_onDocTouchMove` — function, line 124
- **called from:**
- `static/js/features/notes/ui/mobileReorder.js:124`

## `_onDocTouchEnd` — function, line 163
- **called from:**
- `static/js/features/notes/ui/mobileReorder.js:73`
- `static/js/features/notes/ui/mobileReorder.js:163`

## `_commitNoteReorder` — function, line 192
- **called from:**
- `static/js/features/notes/ui/mobileReorder.js:184`
- `static/js/features/notes/ui/mobileReorder.js:192`

## `dispose` — function, line 200
- **called from:**
- `tests/cli/test_gallery_cli_tag_filters.py:43`
- `tests/helpers/database.py:27`
- `tests/test_background_tool_jobs.py:21`
- `tests/test_calendar_default_transaction.py:63`
- `tests/test_calendar_default_transaction.py:212`
- `tests/test_calendar_default_transaction.py:310`
- `tests/test_calendar_default_transaction.py:538`
- `tests/test_calendar_stream_links.py:86`
- `tests/test_chat_image_preservation.py:40`
- `tests/test_chat_image_preservation.py:58`
- `tests/test_chat_tidy_content_preservation.py:38`
- `tests/test_chatgpt_session_binding.py:38`
- `tests/test_chatgpt_session_binding.py:162`
- `tests/test_chatgpt_subscription_usage.py:31`
- `tests/test_cleanup_transcript_preservation.py:31`
- `tests/test_cookbook_endpoint_registration.py:326`
- `tests/test_daily_brief_local_calendar.py:80`
- `tests/test_document_export_zip_filenames.py:39`
- `tests/test_document_followup_integrity.py:32`
- `tests/test_document_read_pagination.py:29`
- `tests/test_document_render_pdf_iframe.py:132`
- `tests/test_email_account_default_serialization.py:42`
- `tests/test_email_account_default_serialization.py:286`
- `tests/test_email_account_default_serialization.py:339`
- `tests/test_failed_call_correction.py:78`
- `tests/test_history_display_model_hydration.py:118`
- `tests/test_history_display_model_hydration.py:168`
- `tests/test_history_display_model_hydration.py:269`
- `tests/test_history_display_model_hydration.py:309`
- `tests/test_history_display_model_hydration.py:345`
- `tests/test_history_display_model_hydration.py:389`
- `tests/test_history_display_model_hydration.py:548`
- `tests/test_manage_tasks_cron.py:20`
- `tests/test_notes_checklist_state.py:27`
- `tests/test_owned_resource_identity.py:78`
- `tests/test_pinned_model_route_selection.py:24`
- `tests/test_replace_messages_upload_reservations.py:34`
- `tests/test_request_authority.py:384`
- `tests/test_request_authority.py:413`
- `tests/test_review_calendar_invitation.py:24`
- `tests/test_review_document_conversion.py:139`
- `tests/test_review_endpoint_credentials.py:86`
- `tests/test_upload_handler_cleanup.py:186`
- `tests/test_upload_handler_cleanup.py:550`
- `tests/test_upload_handler_cleanup.py:734`
- `tests/tools/editor_writing_smoke.py:142`
- `tests/tools/organizer_smoke.py:404`
- `static/js/features/notes/application/reminders.js:180`
- `static/js/features/notes/index.js:217`
- `static/js/features/notes/index.js:217`
- `static/js/features/notes/index.js:217`
- `static/js/features/notes/index.js:217`
- `static/js/features/notes/ui/checklistReorder.js:105`
- `static/js/features/notes/ui/layout.js:118`
- `static/js/features/notes/ui/lifecycle.js:34`
- `static/js/features/notes/ui/mobileReorder.js:200`
