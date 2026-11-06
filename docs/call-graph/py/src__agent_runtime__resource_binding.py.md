# `src/agent_runtime/resource_binding.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ResourceBinding` — class, line 25
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/resource_binding.py:145`
- `tests/test_resource_identity.py:535`
- `tests/test_resource_identity.py:536`

## `ResourceBinding.__post_init__` — method, line 29
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `BoundFilesystemOperation` — class, line 35
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/resource_binding.py:196`
- `tests/test_resource_identity.py:539`
- `tests/test_resource_identity.py:540`

## `BoundFilesystemOperation.__post_init__` — method, line 42
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `BoundFilesystemOperation.write_intent` — method, line 57
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `BoundFilesystemOperation.validate` — method, line 64
- **called from:**
- `scripts/eval_ajax_basic_tools.py:59`
- `scripts/test_clean_tool_loop.py:118`
- `src/agent_runtime/authority.py:250`
- `src/agent_runtime/effect_adapters.py:392`
- `src/agent_runtime/effect_adapters.py:397`
- `src/agent_runtime/effect_adapters.py:408`
- `src/agent_runtime/owned_resources.py:229`
- `src/agent_runtime/owned_resources.py:408`
- `src/agent_runtime/owned_resources.py:422`
- `src/agent_runtime/owned_resources.py:438`
- `src/agent_runtime/owned_resources.py:450`
- `src/agent_runtime/process_resources.py:69`
- `src/agent_runtime/process_resources.py:153`
- `src/agent_runtime/process_resources.py:191`
- `src/agent_runtime/process_resources.py:198`
- `src/agent_runtime/process_resources.py:208`
- `src/agent_runtime/process_resources.py:266`
- `src/agent_runtime/process_resources.py:272`
- `src/agent_runtime/process_resources.py:326`
- `src/agent_runtime/process_resources.py:339`
- `src/agent_runtime/process_resources.py:357`
- `src/agent_runtime/process_resources.py:412`
- `src/agent_runtime/remote_resources.py:219`
- `src/agent_runtime/resource_binding.py:66`
- `src/agent_runtime/resource_binding.py:81`
- `src/agent_runtime/resource_binding.py:87`
- `src/agent_runtime/resource_binding.py:197`
- `src/agent_runtime/resource_binding.py:213`
- `src/agent_runtime/resources.py:380`
- `src/agent_runtime/resources.py:432`
- `src/agent_runtime/resources.py:433`
- `src/agent_runtime/resources.py:517`
- `src/agent_runtime/resources.py:560`
- `src/agent_tools/bg_job_tools.py:95`
- `src/agent_tools/filesystem_tools.py:1001`
- `src/ai_interaction.py:405`
- `src/bg_jobs.py:168`
- `src/browser_identity.py:134`
- `src/browser_identity.py:202`
- `src/browser_identity.py:491`
- `src/browser_identity.py:502`
- `src/browser_identity.py:511`
- `src/browser_identity.py:537`
- `src/browser_identity.py:541`
- `src/browser_identity.py:572`
- `src/browser_identity.py:583`
- `src/browser_identity.py:595`
- `src/browser_identity.py:604`
- `src/browser_identity.py:632`
- `src/browser_identity.py:636`
- `src/clean_agent_preview.py:7436`
- `src/clean_agent_preview.py:7809`
- `src/containment_worker.py:54`
- `src/containment_worker.py:57`
- `src/tool_execution.py:1251`
- `src/tool_execution.py:1635`
- `src/tool_execution.py:1673`
- `src/tool_execution.py:1989`
- `src/tool_execution.py:2159`
- `src/tool_execution.py:2162`
- … +28 more (grep the name in repo)

## `BoundFilesystemOperation.to_dict` — method, line 68
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5643`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28809`
- `src/agent_loop.py:31336`
- `src/agent_loop.py:31809`
- `src/agent_loop.py:32074`
- `src/agent_loop.py:32114`
- `src/agent_loop.py:32145`
- `src/agent_loop.py:32198`
- `src/agent_loop.py:32326`
- `src/agent_loop.py:32658`
- `src/agent_loop.py:34878`
- `src/agent_loop.py:36887`
- `src/agent_loop.py:37210`
- `src/agent_loop.py:37423`
- `src/agent_loop.py:37478`
- `src/agent_loop.py:37535`
- `src/agent_loop.py:37869`
- `src/agent_loop.py:37881`
- `src/agent_loop.py:37987`
- `src/agent_loop.py:38909`
- `src/agent_loop.py:38910`
- `src/agent_loop.py:38915`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:681`
- `src/agent_runtime/authority.py:705`
- `src/agent_runtime/authority.py:705`
- `src/agent_runtime/completion.py:356`
- `src/agent_runtime/completion.py:385`
- `src/agent_runtime/completion.py:388`
- `src/agent_runtime/completion.py:389`
- `src/agent_runtime/completion.py:392`
- `src/agent_runtime/context_resolution.py:78`
- `src/agent_runtime/context_resolution.py:78`
- `src/agent_runtime/context_resolution.py:154`
- `src/agent_runtime/context_resolution.py:155`
- `src/agent_runtime/context_resolution.py:502`
- `src/agent_runtime/context_resolution.py:518`
- `src/agent_runtime/effect_adapters.py:296`
- `src/agent_runtime/effect_log.py:263`
- `src/agent_runtime/effects.py:156`
- `src/agent_runtime/effects.py:161`
- `src/agent_runtime/effects.py:168`
- `src/agent_runtime/effects.py:173`
- `src/agent_runtime/effects.py:177`
- `src/agent_runtime/effects.py:181`
- `src/agent_runtime/effects.py:186`
- … +146 more (grep the name in repo)

## `BoundFilesystemOperation.resolve_path` — method, line 73
- **called from:**
- `src/agent_tools/filesystem_tools.py:39`
- `src/agent_tools/filesystem_tools.py:1018`
- `src/agent_tools/filesystem_tools.py:1098`
- `src/agent_tools/filesystem_tools.py:1236`
- `src/agent_tools/filesystem_tools.py:1315`
- `src/tool_execution.py:1061`
- `src/tool_execution.py:1291`

## `_resolve` — function, line 96
- **called from:**
- `src/agent_runtime/resource_binding.py:144`
- `src/agent_tools/admin_tools.py:664`
- `src/agent_tools/admin_tools.py:677`
- `src/agent_tools/admin_tools.py:710`
- `tests/cli/test_logs_cli_resolve_nonstring.py:12`
- `tests/cli/test_logs_cli_resolve_nonstring.py:13`
- `tests/test_compare_endpoint_owner_scope.py:80`
- `tests/test_compare_endpoint_owner_scope.py:85`
- `tests/test_compare_endpoint_owner_scope.py:91`
- `tests/test_compare_endpoint_owner_scope.py:97`
- `tests/test_compare_endpoint_owner_scope.py:103`
- `tests/test_research_endpoint_owner_scope.py:98`
- `tests/test_research_endpoint_owner_scope.py:103`
- `tests/test_research_endpoint_owner_scope.py:109`
- `tests/test_research_endpoint_owner_scope.py:115`
- `tests/test_research_endpoint_owner_scope.py:123`
- `tests/test_research_endpoint_owner_scope.py:129`
- `tests/test_research_endpoint_owner_scope.py:136`
- `tests/test_ui_visibility_js.py:86`
- `tests/test_ui_visibility_js.py:95`
- `tests/test_ui_visibility_js.py:102`
- `tests/test_ui_visibility_js.py:109`
- `tests/test_ui_visibility_js.py:114`
- `tests/test_ui_visibility_js.py:123`
- `tests/test_ui_visibility_js.py:128`
- `tests/test_ui_visibility_js.py:134`
- `tests/test_ui_visibility_js.py:139`

## `resolve_filesystem_operation` — function, line 123
- **called from:**
- `src/tool_approvals.py:466`
- `src/tool_execution.py:1882`
- `tests/test_agent_state_dir_confinement.py:181`
- `tests/test_agent_state_dir_confinement.py:185`
- `tests/test_grep_followup_integrity.py:27`
- `tests/test_resource_identity.py:35`
- `tests/test_write_file_empty_body.py:94`

## `bind` — function, line 143
- **called from:**
- `scripts/verify_frontend_runtime.py:55`
- `scripts/verify_notes_browser_runtime.py:55`
- `scripts/verify_notes_browser_runtime.py:57`
- `src/agent_runtime/authority.py:605`
- `src/agent_runtime/completion.py:213`
- `src/agent_runtime/journal.py:245`
- `src/agent_runtime/resource_binding.py:159`
- `src/agent_runtime/resource_binding.py:192`
- `src/agent_tools/web_tools_prewave3.py:2969`
- `src/chat_helpers.py:229`
- `src/turn_contract.py:6508`
- `src/url_safety.py:267`
- `tests/cli/test_dev_cli_isolation.py:95`
- `tests/helpers/unix_sockets.py:42`
- `tests/runtime_evidence_helpers.py:26`
- `tests/test_chroma_client.py:19`
- `tests/test_chroma_client.py:32`
- `tests/test_codeql_python_residual_closure.py:127`
- `tests/test_codeql_python_residual_closure.py:557`
- `tests/test_security_regressions.py:1355`
- `tests/test_skill_importer_dns_pinning.py:163`
- `tests/test_worker_runtime.py:81`
- `static/js/editor/text-layer.js:121`
- `static/js/editor/text-layer.js:121`
- `static/js/editor/wire-extra-menus.js:116`
- `static/js/editor/wire-extra-menus.js:145`
- `static/js/editor/wire-extra-menus.js:172`
- `static/js/editor/wire-extra-menus.js:183`
- `static/js/editor/wire-extra-menus.js:199`
- `static/js/editor/wire-extra-menus.js:220`
- `static/js/editor/wire-extra-menus.js:243`
- `static/js/editor/wire-extra-menus.js:249`
- `static/js/editor/wire-extra-menus.js:255`
- `static/js/features/notes/application/state.js:36`
- `static/js/galleryEditor.js:12846`
- `static/js/providerDeviceFlow.js:77`
- `static/js/slashCommands.js:1273`

## `active_resource_operation` — function, line 204
- **called from:**
- `src/agent_runtime/effect_adapters.py:59`
- `src/agent_tools/filesystem_tools.py:35`
- `src/agent_tools/filesystem_tools.py:416`
- `src/agent_tools/filesystem_tools.py:999`
- `src/tool_execution.py:1059`
- `src/tool_execution.py:1289`
- `src/tool_execution.py:1645`
- `src/tool_execution.py:2166`
- `src/tool_execution.py:2240`
- `src/tool_execution.py:2288`
- `src/tool_execution.py:2290`
- `src/tool_execution.py:2297`
- `tests/test_resource_identity.py:427`
- `tests/test_resource_identity.py:455`
- `tests/test_resource_identity.py:460`
- `tests/test_resource_identity.py:468`
- `tests/test_resource_identity.py:486`
- `tests/test_resource_identity.py:498`
- `tests/test_resource_identity.py:509`
- `tests/test_resource_identity.py:510`

## `bind_resource_operation` — function, line 209
- decorator: `contextmanager`
- **called from:**
- `src/tool_execution.py:1996`
- `tests/test_grep_followup_integrity.py:32`
- `tests/test_resource_identity.py:438`
- `tests/test_resource_identity.py:443`
- `tests/test_resource_identity.py:503`
