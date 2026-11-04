# `src/tool_approvals.py` — definitions & call sites

21 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_normalized_owner` — function, line 34
- **called from:**
- `src/tool_approvals.py:122`
- `src/tool_approvals.py:452`
- `src/tool_approvals.py:490`

## `_normalized_workspace` — function, line 38
- **called from:**
- `src/tool_approvals.py:127`

## `_normalized_selected_tools` — function, line 49
- **called from:**
- `src/tool_approvals.py:135`

## `_normalized_continuation_query` — function, line 82
- **called from:**
- `src/tool_approvals.py:137`

## `_canonical_digest` — function, line 89
- **called from:**
- `src/tool_approvals.py:274`
- `src/tool_approvals.py:391`

## `document_content_digest` — function, line 99
- **called from:**
- `src/agent_loop.py:6311`
- `src/agent_tools/document_tools.py:108`
- `tests/test_external_context_tool_gate.py:1243`
- `tests/test_foreground_model_routing.py:282`
- `tests/test_tool_approvals.py:135`
- `tests/test_tool_approvals.py:199`
- `tests/test_tool_approvals.py:238`
- `tests/test_tool_approvals.py:301`
- `tests/test_tool_approvals.py:308`

## `_binding_payload` — function, line 104
- **called from:**
- `src/tool_approvals.py:256`
- `src/tool_approvals.py:359`

## `PendingToolApproval` — class, line 144
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/tool_approvals.py:375`

## `PendingToolApproval.public_payload` — method, line 166
- **called from:**
- `src/agent_loop.py:6336`
- `src/teacher_escalation.py:774`
- `tests/test_scheduler_prompt_cache_time.py:87`
- `tests/test_skills_routes_owner_update.py:173`
- `tests/test_tool_approval_task_scope.py:46`
- `tests/test_tool_approval_task_scope.py:113`
- `tests/test_tool_approval_task_scope.py:173`
- `tests/test_tool_approvals.py:138`

## `ExactToolApproval` — class, line 219
- decorator: `dataclass`
- **called from:**
- `src/tool_approvals.py:465`
- `src/tool_approvals.py:470`
- `tests/test_tool_approval_task_scope.py:216`

## `ExactToolApproval.grants_chat_session` — method, line 234
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ExactToolApproval._matches_unlocked` — method, line 237
- **called from:**
- `src/tool_approvals.py:286`
- `src/tool_approvals.py:304`

## `ExactToolApproval.matches` — method, line 276
- **called from:**
- `src/agent_loop.py:5058`
- `src/model_capabilities.py:903`
- `tests/test_calendar_cli_overlap.py:85`
- `tests/test_foreground_model_routing.py:303`
- `tests/test_tool_approval_task_scope.py:217`
- `static/js/a11y.js:105`
- `static/js/a11y.js:116`
- `static/js/a11y.js:135`
- `static/js/a11y.js:152`
- `static/js/dragSort.js:45`
- `static/js/dragSort.js:163`
- `static/js/dragSort.js:194`
- `static/js/editor/slider-ux.js:97`
- `static/js/emailLibrary.js:3806`
- `static/js/ui.js:152`

## `ExactToolApproval.claim` — method, line 294
- **called from:**
- `src/tool_execution.py:921`
- `tests/test_tool_approvals.py:41`
- `tests/test_tool_approvals.py:48`
- `tests/test_tool_approvals.py:55`
- `static/sw.js:182`

## `ToolApprovalStore` — class, line 316
- **called from:**
- `src/tool_approvals.py:513`
- `tests/test_tool_approval_single_action_scope.py:30`
- `tests/test_tool_approval_single_action_scope.py:54`
- `tests/test_tool_approval_single_action_scope.py:70`
- `tests/test_tool_approval_task_scope.py:42`
- `tests/test_tool_approval_task_scope.py:68`
- `tests/test_tool_approval_task_scope.py:97`
- `tests/test_tool_approval_task_scope.py:162`
- `tests/test_tool_approval_task_scope.py:200`
- `tests/test_tool_approvals.py:31`
- `tests/test_tool_approvals.py:65`
- `tests/test_tool_approvals.py:87`
- `tests/test_tool_approvals.py:100`
- `tests/test_tool_approvals.py:109`
- `tests/test_tool_approvals.py:120`
- `tests/test_tool_approvals.py:129`
- `tests/test_tool_approvals.py:152`
- `tests/test_tool_approvals.py:191`
- `tests/test_tool_approvals.py:246`
- `tests/test_tool_approvals.py:359`
- `tests/test_tool_approvals.py:395`
- `tests/test_tool_approvals.py:429`

## `ToolApprovalStore.__init__` — method, line 319
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

## `ToolApprovalStore._purge_expired_locked` — method, line 330
- **called from:**
- `src/tool_approvals.py:398`
- `src/tool_approvals.py:446`
- `src/tool_approvals.py:479`
- `src/tool_approvals.py:495`

## `ToolApprovalStore.create` — method, line 339
- **called from:**
- `routes/chat_routes.py:398`
- `scripts/demo_email/seed_demo_emails.py:318`
- `src/agent_loop.py:6297`
- `src/teacher_escalation.py:764`
- `tests/test_email_account_default_serialization.py:375`
- `tests/test_email_account_port_validation.py:45`
- `tests/test_foreground_model_routing.py:273`
- `tests/test_foreground_model_routing.py:319`
- `tests/test_foreground_model_routing.py:352`
- `tests/test_foreground_model_routing.py:389`
- `tests/test_foreground_model_routing.py:421`
- `tests/test_model_routes.py:1407`
- `tests/test_model_routes.py:1427`
- `tests/test_model_routes.py:1452`
- `tests/test_model_routes.py:1478`
- `tests/test_model_routes.py:1498`
- `tests/test_model_routes.py:1523`
- `tests/test_model_routes.py:1544`
- `tests/test_model_routes.py:1563`
- `tests/test_scheduler_prompt_cache_time.py:77`
- `tests/test_skills_routes_owner_update.py:158`
- `tests/test_tool_approval_single_action_scope.py:17`
- `tests/test_tool_approval_task_scope.py:26`
- `tests/test_tool_approvals.py:27`
- `static/app.js:1429`
- `static/js/chat.js:711`
- `static/js/chat.js:2463`
- `static/js/chat.js:2696`
- `static/js/chat.js:4362`
- `static/js/chat.js:5626`
- `static/js/chat.js:5984`
- `static/js/chat.js:7116`
- `static/js/compare/index.js:696`
- `static/js/compare/index.js:773`
- `static/js/compare/index.js:844`
- `static/js/compare/index.js:920`
- `static/js/compare/panes.js:109`
- `static/js/compare/panes.js:161`
- `static/js/compare/selector.js:387`
- `static/js/compare/stream.js:77`
- `static/js/compare/stream.js:469`
- `static/js/compare/stream.js:529`
- `static/js/cookbook.js:110`
- `static/js/document.js:581`
- `static/js/documentLibrary.js:2344`
- `static/js/documentLibrary.js:3245`
- `static/js/documentLibrary.js:3478`
- `static/js/editor/ai-inpaint.js:104`
- `static/js/editor/ai-tool-runner.js:58`
- `static/js/emailLibrary.js:8245`
- `static/js/fileHandler.js:284`
- `static/js/galleryEditor.js:3655`
- `static/js/galleryEditor.js:4052`
- `static/js/group.js:742`
- `static/js/memory.js:513`
- `static/js/models.js:187`
- `static/js/presets.js:125`
- `static/js/sessions.js:2839`
- `static/js/slashCommands.js:672`
- `static/js/slashCommands.js:2059`
- … +3 more (grep the name in repo)

## `ToolApprovalStore.consume` — method, line 426
- **called from:**
- `routes/chat_routes.py:1376`
- `routes/skills_routes.py:782`
- `routes/skills_routes.py:1534`
- `routes/skills_routes.py:1601`
- `src/task_scheduler.py:1951`
- `tests/test_external_context_tool_gate.py:1244`
- `tests/test_teacher_eval_tier2.py:293`
- `tests/test_tool_approval_single_action_scope.py:33`
- `tests/test_tool_approval_single_action_scope.py:57`
- `tests/test_tool_approval_single_action_scope.py:73`
- `tests/test_tool_approval_task_scope.py:70`
- `tests/test_tool_approval_task_scope.py:99`
- `tests/test_tool_approval_task_scope.py:165`
- `tests/test_tool_approvals.py:33`
- `tests/test_tool_approvals.py:68`
- `tests/test_tool_approvals.py:77`
- `tests/test_tool_approvals.py:91`
- `tests/test_tool_approvals.py:154`
- `tests/test_tool_approvals.py:202`
- `tests/test_tool_approvals.py:254`
- `tests/test_tool_approvals.py:361`
- `tests/test_tool_approvals.py:397`
- `tests/test_tool_approvals.py:431`
- `static/js/cookbookRunning.js:4090`

## `ToolApprovalStore.peek` — method, line 476
- **called from:**
- `routes/chat_routes.py:1351`
- `routes/skills_routes.py:1593`
- `tests/test_external_context_tool_gate.py:1239`
- `tests/test_foreground_model_routing.py:302`
- `tests/test_foreground_model_routing.py:378`
- `tests/test_foreground_model_routing.py:406`
- `tests/test_scheduler_prompt_cache_time.py:114`
- `tests/test_skills_routes_owner_update.py:205`
- `tests/test_teacher_eval_tier2.py:288`
- `tests/test_tool_approval_single_action_scope.py:80`
- `tests/test_tool_approval_task_scope.py:171`
- `tests/test_tool_approvals.py:74`
- `tests/test_tool_approvals.py:83`
- `tests/test_tool_approvals.py:104`
- `tests/test_tool_approvals.py:105`
- `tests/test_tool_approvals.py:113`
- `tests/test_tool_approvals.py:115`
- `tests/test_tool_approvals.py:124`
- `tests/test_tool_approvals.py:125`
- `static/js/editor/build/right-panel.js:147`

## `ToolApprovalStore.retire_for_session` — method, line 482
- **called from:**
- `routes/chat_routes.py:1429`
- `tests/test_tool_approvals.py:112`
- `tests/test_tool_approvals.py:114`
- `tests/test_tool_approvals.py:116`
