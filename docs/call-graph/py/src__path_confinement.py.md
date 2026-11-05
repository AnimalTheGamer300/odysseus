# `src/path_confinement.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `PathEscape` — class, line 69
- **called from:**
- `src/path_confinement.py:176`
- `src/path_confinement.py:185`
- `src/path_confinement.py:187`

## `PathEscape.__init__` — method, line 77
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

## `_reject_unusable` — function, line 86
- **called from:**
- `src/path_confinement.py:120`
- `src/path_confinement.py:133`

## `canonical_root` — function, line 112
- **called from:**
- `routes/upload_routes.py:157`
- `src/agent_runtime/resource_binding.py:105`
- `src/agent_runtime/resource_binding.py:109`
- `src/agent_runtime/resource_binding.py:187`
- `src/agent_runtime/resources.py:33`
- `src/agent_runtime/resources.py:36`
- `src/agent_runtime/resources.py:74`
- `src/agent_runtime/resources.py:79`
- `src/agent_runtime/resources.py:79`
- `src/agent_runtime/resources.py:80`
- `src/agent_runtime/resources.py:83`
- `src/agent_runtime/resources.py:86`
- `src/agent_runtime/resources.py:98`
- `src/agent_runtime/resources.py:103`
- `src/agent_runtime/resources.py:112`
- `src/agent_runtime/resources.py:116`
- `src/agent_runtime/resources.py:120`
- `src/agent_runtime/resources.py:123`
- `src/agent_runtime/resources.py:124`
- `src/agent_runtime/resources.py:320`
- `src/agent_runtime/resources.py:325`
- `src/agent_runtime/resources.py:519`
- `src/path_confinement.py:170`
- `src/tool_execution.py:1111`
- `tests/test_path_confinement_boundary.py:41`
- `tests/test_path_confinement_boundary.py:54`
- `tests/test_path_confinement_boundary.py:58`
- `tests/test_path_confinement_boundary.py:75`
- `tests/test_path_confinement_boundary.py:90`
- `tests/test_path_confinement_boundary.py:129`
- `tests/test_path_confinement_boundary.py:167`
- `tests/test_path_confinement_boundary.py:168`
- `tests/test_path_confinement_boundary.py:211`

## `_canonical_candidate` — function, line 124
- **called from:**
- `src/path_confinement.py:171`

## `is_inside` — function, line 140
- **called from:**
- `routes/document/document_helpers.py:140`
- `routes/upload_routes.py:160`
- `src/agent_tools/filesystem_tools.py:887`
- `src/app_helpers.py:56`
- `src/tool_execution.py:1093`
- `src/upload_handler.py:321`
- `src/upload_handler.py:771`
- `tests/test_path_confinement_boundary.py:102`
- `tests/test_path_confinement_boundary.py:103`
- `tests/test_path_confinement_boundary.py:155`
- `tests/test_path_confinement_boundary.py:156`
- `tests/test_path_confinement_boundary.py:157`
- `tests/test_path_confinement_boundary.py:194`
- `tests/test_path_confinement_boundary.py:195`
- `tests/test_path_confinement_boundary.py:225`

## `confine` — function, line 160
- **called from:**
- `routes/email/email_routes.py:4841`
- `routes/gallery/gallery_routes.py:581`
- `routes/personal_routes.py:27`
- `routes/personal_routes.py:42`
- `routes/personal_routes.py:166`
- `routes/personal_routes.py:417`
- `routes/upload_routes.py:171`
- `routes/upload_routes.py:182`
- `routes/upload_routes.py:193`
- `routes/upload_routes.py:479`
- `routes/upload_routes.py:492`
- `services/memory/skills.py:671`
- `src/agent_runtime/resource_binding.py:89`
- `src/agent_runtime/resources.py:390`
- `src/generated_images.py:64`
- `src/path_confinement.py:154`
- `src/session_image_cleanup.py:30`
- `src/tool_execution.py:1121`
- `tests/test_path_confinement_boundary.py:41`
- `tests/test_path_confinement_boundary.py:54`
- `tests/test_path_confinement_boundary.py:58`
- `tests/test_path_confinement_boundary.py:64`
- `tests/test_path_confinement_boundary.py:65`
- `tests/test_path_confinement_boundary.py:75`
- `tests/test_path_confinement_boundary.py:77`
- `tests/test_path_confinement_boundary.py:83`
- `tests/test_path_confinement_boundary.py:85`
- `tests/test_path_confinement_boundary.py:90`
- `tests/test_path_confinement_boundary.py:113`
- `tests/test_path_confinement_boundary.py:123`
- `tests/test_path_confinement_boundary.py:129`
- `tests/test_path_confinement_boundary.py:175`
- `tests/test_path_confinement_boundary.py:182`
- `tests/test_path_confinement_boundary.py:187`
- `tests/test_path_confinement_boundary.py:203`
- `tests/test_path_confinement_boundary.py:208`
- `tests/test_personal_dir_symlink_escape.py:71`
- `tests/test_personal_dir_symlink_escape.py:73`
- `tests/test_personal_dir_symlink_escape.py:76`
