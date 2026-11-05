# `static/js/features/notes/application/reminders.js` — definitions & call sites

12 definitions (regex-based, best-effort).
**Exports:** `createNotesReminders`

## `createNotesReminders` — function, line 3
- **called from:**
- `static/js/features/notes/application/reminders.js:3`
- `static/js/features/notes/index.js:66`

## `_checkReminders` — function, line 28
- **called from:**
- `static/js/features/notes/application/reminders.js:28`
- `static/js/features/notes/application/reminders.js:128`

## `_fireReminder` — function, line 72
- **called from:**
- `static/js/features/notes/application/reminders.js:40`
- `static/js/features/notes/application/reminders.js:72`

## `showLocal` — arrow, line 98
- **called from:**
- `static/js/features/notes/application/reminders.js:104`
- `static/js/features/notes/application/reminders.js:113`
- `static/js/features/notes/application/reminders.js:117`

## `_startReminderLoop` — function, line 125
- **called from:**
- `static/js/features/notes/application/reminders.js:125`
- `static/js/features/notes/application/reminders.js:174`
- `static/js/features/notes/index.js:114`
- `static/js/features/notes/index.js:114`
- `static/js/features/notes/ui/panel.js:313`
- `static/js/features/notes/ui/panel.js:316`

## `_countDueReminders` — function, line 131
- **called from:**
- `static/js/features/notes/application/reminders.js:131`

## `_countFiredReminders` — function, line 135
- **called from:**
- `static/js/features/notes/application/reminders.js:135`
- `static/js/features/notes/index.js:116`
- `static/js/features/notes/index.js:116`
- `static/js/features/notes/ui/reminderDisplay.js:77`

## `dismissFiredReminderDot` — function, line 148
- **called from:**
- `static/js/features/notes/application/reminders.js:148`

## `refreshDueBadge` — function, line 154
- **called from:**
- `static/app.js:1151`
- `static/app.js:1152`
- `static/js/features/notes/application/reminders.js:154`

## `_initReminders` — function, line 168
- **called from:**
- `static/js/features/notes/application/reminders.js:168`

## `start` — function, line 179
- **called from:**
- `app.py:1410`
- `launcher.py:73`
- `launcher.py:145`
- `launcher.py:147`
- `mcp_servers/email_server.py:2023`
- `routes/auth_routes.py:895`
- `routes/chat_helpers.py:94`
- `routes/chat_helpers.py:94`
- `routes/chat_helpers.py:1714`
- `routes/chat_helpers.py:1777`
- `routes/chat_helpers.py:1778`
- `routes/chat_helpers.py:1779`
- `routes/chat_routes.py:5522`
- `routes/cookbook_routes.py:3584`
- `routes/email/email_helpers.py:399`
- `routes/email/email_routes.py:1130`
- `routes/email/email_routes.py:1596`
- `routes/email/email_routes.py:1898`
- `routes/model_routes.py:1666`
- `scripts/add_hwfit_models.py:117`
- `scripts/css_snapshot.py:211`
- `services/hwfit/hf_discovery.py:115`
- `services/search/core.py:411`
- `services/search/core.py:800`
- `services/skills/evaluation.py:463`
- `src/agent_evidence.py:225`
- `src/agent_evidence.py:225`
- `src/agent_evidence.py:245`
- `src/agent_evidence.py:308`
- `src/agent_loop.py:1143`
- `src/agent_loop.py:2639`
- `src/agent_loop.py:2644`
- `src/agent_loop.py:2652`
- `src/agent_loop.py:2653`
- `src/agent_loop.py:3180`
- `src/agent_loop.py:9123`
- `src/agent_loop.py:9123`
- `src/agent_loop.py:9169`
- `src/agent_loop.py:12041`
- `src/agent_loop.py:12044`
- `src/agent_loop.py:14160`
- `src/agent_loop.py:14164`
- `src/agent_runtime/completion.py:90`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:94`
- `src/agent_tools/document_tools.py:240`
- `src/agent_tools/document_tools.py:384`
- `src/agent_tools/document_tools.py:431`
- `src/agent_tools/document_tools.py:729`
- `src/agent_tools/document_tools.py:734`
- `src/agent_tools/document_tools.py:898`
- `src/agent_tools/filesystem_tools.py:1153`
- `src/agent_tools/filesystem_tools.py:1154`
- `src/agent_tools/filesystem_tools.py:1266`
- `src/agent_tools/web_tools.py:954`
- `src/agent_tools/web_tools.py:975`
- `src/agent_tools/web_tools.py:978`
- `src/agent_tools/web_tools_prewave3.py:958`
- … +213 more (grep the name in repo)

## `dispose` — function, line 180
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
