# `src/process_lifecycle.py` — definitions & call sites

36 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `TerminationOutcome` — class, line 80
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/process_lifecycle.py:631`
- `src/process_lifecycle.py:645`
- `src/process_lifecycle.py:649`
- `src/process_lifecycle.py:659`
- `src/process_lifecycle.py:669`
- `tests/test_process_lifecycle.py:299`

## `TerminationOutcome.to_dict` — method, line 95
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5646`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28809`
- `src/agent_loop.py:31378`
- `src/agent_loop.py:31851`
- `src/agent_loop.py:32116`
- `src/agent_loop.py:32156`
- `src/agent_loop.py:32187`
- `src/agent_loop.py:32240`
- `src/agent_loop.py:32368`
- `src/agent_loop.py:32700`
- `src/agent_loop.py:34920`
- `src/agent_loop.py:36929`
- `src/agent_loop.py:37252`
- `src/agent_loop.py:37465`
- `src/agent_loop.py:37520`
- `src/agent_loop.py:37577`
- `src/agent_loop.py:37911`
- `src/agent_loop.py:37923`
- `src/agent_loop.py:38029`
- `src/agent_loop.py:38963`
- `src/agent_loop.py:38964`
- `src/agent_loop.py:38969`
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

## `ProcessIdentity` — class, line 107
- decorator: `dataclass(frozen=True)`
- **called from:**
- `routes/shell_routes.py:743`
- `src/agent_runtime/process_resources.py:517`
- `src/agent_runtime/resources.py:212`
- `src/agent_runtime/resources.py:492`
- `src/bg_jobs.py:166`
- `src/browser_lifecycle.py:160`
- `src/process_lifecycle.py:211`
- `src/process_lifecycle.py:260`
- `src/tools/cookbook.py:1130`
- `tests/process_resource_helpers.py:54`
- `tests/test_browser_resource_identity.py:41`
- `tests/test_effect_verification_adapters.py:72`
- `tests/test_effect_verification_adapters.py:290`
- `tests/test_effects_foundation.py:123`
- `tests/test_effects_foundation.py:124`
- `tests/test_private_browser_tool.py:178`
- `tests/test_private_browser_tool.py:194`
- `tests/test_private_browser_tool.py:219`
- `tests/test_process_lifecycle.py:164`
- `tests/test_process_lifecycle.py:169`
- `tests/test_process_lifecycle.py:178`
- `tests/test_process_lifecycle.py:209`
- `tests/test_process_lifecycle.py:210`
- `tests/test_process_lifecycle.py:211`
- `tests/test_process_lifecycle.py:230`
- `tests/test_process_lifecycle.py:321`
- `tests/test_process_resource_identity.py:16`
- `tests/test_resource_identity.py:724`
- `tests/test_resource_identity.py:730`
- `tests/test_runtime_resource_integration.py:505`
- `tests/test_shell_routes.py:145`

## `ProcessIdentity.capture` — method, line 120
- decorator: `classmethod`
- **called from:**
- `routes/shell_routes.py:739`
- `scripts/css_snapshot.py:258`
- `scripts/run_sft_environment_expansion.py:695`
- `scripts/verify_notes_browser_runtime.py:74`
- `src/agent_tools/web_tools.py:115`
- `src/agent_tools/web_tools_prewave3.py:119`
- `src/bg_jobs.py:162`
- `src/containment.py:475`
- `src/containment.py:1096`
- `src/containment.py:1127`
- `src/containment.py:1254`
- `src/process_lifecycle.py:122`
- `tests/test_ai_interaction_owner_scope.py:52`
- `tests/test_ai_interaction_owner_scope.py:57`
- `tests/test_css_computed_style_snapshot.py:94`
- `tests/test_css_computed_style_snapshot.py:103`
- `tests/test_css_computed_style_snapshot.py:152`
- `tests/test_css_computed_style_snapshot.py:153`
- `tests/test_css_computed_style_snapshot.py:166`
- `tests/test_css_computed_style_snapshot.py:183`
- `tests/test_css_computed_style_snapshot.py:186`
- `tests/test_notes_native_cleanup.py:24`
- `tests/test_notes_native_cleanup.py:28`
- `tests/test_process_lifecycle.py:185`
- `tests/test_process_lifecycle.py:242`
- `tests/test_process_ownership.py:103`
- `tests/test_process_ownership.py:152`
- `static/js/signature.js:4`
- `static/js/signature.js:379`
- `static/js/signature.js:517`

## `ProcessIdentity.from_record` — method, line 126
- decorator: `classmethod`
- **called from:**
- `src/process_reaper.py:77`
- `src/process_reaper.py:84`
- `tests/test_process_lifecycle.py:158`
- `tests/test_process_lifecycle.py:159`
- `tests/test_process_lifecycle.py:160`

## `ProcessIdentity.verdict` — method, line 144
- **called from:**
- `routes/shell_routes.py:741`
- `routes/shell_routes.py:784`
- `routes/shell_routes.py:794`
- `scripts/verify_notes_browser_runtime.py:28`
- `scripts/verify_notes_browser_runtime.py:30`
- `src/process_lifecycle.py:148`
- `src/process_lifecycle.py:158`
- `src/process_lifecycle.py:556`
- `src/process_lifecycle.py:580`
- `src/process_lifecycle.py:597`
- `tests/test_process_lifecycle.py:170`
- `tests/test_process_lifecycle.py:191`
- `tests/test_process_lifecycle.py:342`
- `tests/test_runtime_resource_integration.py:506`

## `ProcessIdentity.owned` — method, line 147
- **called from:**
- `src/agent_runtime/resources.py:476`
- `src/browser_identity.py:289`
- `src/browser_identity.py:463`
- `src/browser_identity.py:485`
- `src/process_reaper.py:79`
- `src/process_reaper.py:86`
- `tests/test_process_lifecycle.py:171`

## `ProcessIdentity.exited` — method, line 150
- **called from:**
- `src/agent_runtime/resources.py:476`
- `src/process_lifecycle.py:581`
- `src/process_lifecycle.py:584`
- `src/process_lifecycle.py:591`
- `src/process_lifecycle.py:595`
- `tests/test_notes_native_cleanup.py:32`
- `tests/test_process_lifecycle.py:171`
- `tests/test_process_lifecycle.py:179`
- `tests/test_process_lifecycle.py:192`

## `ProcessIdentity.to_record` — method, line 163
- **called from:**
- `src/agent_runtime/resources.py:202`
- `src/agent_runtime/resources.py:481`
- `src/browser_identity.py:432`

## `Observation` — class, line 168
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/effect_log.py:353`
- `src/process_lifecycle.py:211`
- `src/process_lifecycle.py:260`
- `tests/test_effects_foundation.py:61`
- `tests/test_effects_foundation.py:194`
- `tests/test_effects_foundation.py:463`
- `tests/test_effects_foundation.py:465`

## `observe` — function, line 175
- **called from:**
- `src/agent_runtime/effect_adapters.py:371`
- `src/agent_runtime/process_resources.py:63`
- `src/agent_runtime/resources.py:321`
- `src/agent_runtime/resources.py:325`
- `src/agent_runtime/resources.py:400`
- `src/agent_runtime/resources.py:406`
- `src/agent_runtime/resources.py:519`
- `src/agent_tools/web_tools.py:2457`
- `src/agent_tools/web_tools.py:2500`
- `src/agent_tools/web_tools_prewave3.py:2466`
- `src/agent_tools/web_tools_prewave3.py:2509`
- `src/browser_identity.py:288`
- `src/browser_lifecycle.py:155`
- `src/clean_agent_preview.py:7902`
- `tests/test_browser_progress.py:14`
- `tests/test_browser_progress.py:16`
- `tests/test_browser_progress.py:17`
- `tests/test_browser_progress.py:18`
- `tests/test_browser_progress.py:25`
- `tests/test_browser_progress.py:31`
- `tests/test_browser_progress.py:32`
- `tests/test_browser_progress.py:33`
- `tests/test_browser_progress.py:34`
- `tests/test_browser_progress.py:35`
- `tests/test_browser_progress.py:46`
- `tests/test_effect_journal_persistence.py:75`
- `tests/test_effect_journal_persistence.py:140`
- `tests/test_effect_verification_adapters.py:368`
- `tests/test_effects_foundation.py:216`
- `tests/test_effects_foundation.py:229`
- `tests/test_effects_foundation.py:238`
- `tests/test_effects_foundation.py:240`
- `tests/test_effects_foundation.py:247`
- `tests/test_effects_foundation.py:257`
- `tests/test_effects_foundation.py:268`
- `tests/test_effects_foundation.py:283`
- `tests/test_effects_foundation.py:293`
- `tests/test_effects_foundation.py:304`
- `tests/test_effects_foundation.py:316`
- `tests/test_effects_foundation.py:327`
- `tests/test_effects_foundation.py:330`
- `tests/test_effects_foundation.py:341`
- `tests/test_effects_foundation.py:342`
- `tests/test_effects_foundation.py:349`
- `tests/test_effects_foundation.py:358`
- `tests/test_effects_foundation.py:360`
- `tests/test_effects_foundation.py:369`
- `tests/test_effects_foundation.py:380`
- `tests/test_effects_foundation.py:393`
- `tests/test_effects_foundation.py:411`
- `tests/test_effects_foundation.py:422`
- `tests/test_effects_foundation.py:427`
- `tests/test_effects_foundation.py:450`
- `tests/test_effects_foundation.py:451`
- `tests/test_process_lifecycle.py:320`
- `tests/test_process_lifecycle.py:326`
- `tests/test_process_lifecycle.py:331`
- `tests/test_process_lifecycle.py:340`
- `tests/test_resource_identity.py:62`
- `static/app.js:336`
- … +99 more (grep the name in repo)

## `bind_descendants` — function, line 214
- **called from:**
- `scripts/verify_notes_browser_runtime.py:27`
- `src/process_reaper.py:228`
- `src/tools/cookbook.py:1093`
- `tests/test_process_lifecycle.py:353`
- `tests/test_process_lifecycle.py:364`

## `is_zombie` — function, line 265
- **called from:**
- `routes/shell_routes.py:791`
- `src/process_lifecycle.py:161`
- `tests/test_process_lifecycle.py:188`

## `own_pgid` — function, line 279
- **called from:**
- `routes/shell_routes.py:695`
- `src/containment.py:1274`
- `src/process_lifecycle.py:306`
- `src/process_lifecycle.py:324`

## `pgid_of` — function, line 286
- **called from:**
- `routes/shell_routes.py:694`
- `routes/shell_routes.py:796`
- `src/containment.py:1280`
- `src/process_lifecycle.py:374`
- `src/process_lifecycle.py:633`

## `group_present` — function, line 296
- **called from:**
- `routes/shell_routes.py:722`
- `src/containment.py:1290`
- `src/process_lifecycle.py:360`
- `src/process_lifecycle.py:644`
- `tests/test_process_lifecycle.py:52`
- `tests/test_process_lifecycle.py:63`
- `tests/test_process_lifecycle.py:69`

## `signal_group` — function, line 317
- **called from:**
- `routes/shell_routes.py:708`
- `src/agent_tools/web_tools.py:2419`
- `src/agent_tools/web_tools_prewave3.py:2428`
- `src/containment.py:1295`
- `src/process_lifecycle.py:662`
- `tests/test_process_lifecycle.py:53`
- `tests/test_process_lifecycle.py:79`

## `reap_if_child` — function, line 341
- **called from:**
- `src/containment.py:1302`
- `src/process_lifecycle.py:359`

## `tree_gone` — function, line 356
- **called from:**
- `src/process_lifecycle.py:661`

## `group_ownership_verdict` — function, line 363
- **called from:**
- `src/agent_tools/web_tools.py:2416`
- `src/agent_tools/web_tools_prewave3.py:2425`
- `src/containment.py:1353`
- `src/process_lifecycle.py:638`

## `pidfd_supported` — function, line 380
- **called from:**
- `src/process_lifecycle.py:391`

## `open_pidfd` — function, line 384
- **called from:**
- `src/containment.py:1438`

## `pidfd_exited` — function, line 399
- **called from:**
- `src/containment.py:1502`
- `src/containment.py:1649`
- `src/containment.py:1659`

## `pidfd_signal` — function, line 403
- **called from:**
- `src/containment.py:1506`
- `src/containment.py:1667`
- `src/containment.py:1671`

## `close_fd` — function, line 411
- **called from:**
- `src/containment.py:1444`

## `taskkill_tree` — function, line 420
- **called from:**
- `scripts/verify_notes_browser_runtime.py:31`
- `src/containment.py:1522`
- `src/process_lifecycle.py:655`

## `Escalation` — class, line 435
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/process_lifecycle.py:471`
- `src/process_lifecycle.py:477`
- `src/process_lifecycle.py:483`
- `src/process_lifecycle.py:509`
- `src/process_lifecycle.py:515`
- `src/process_lifecycle.py:527`

## `term_kill_steps` — function, line 443
- **called from:**
- `scripts/verify_notes_browser_runtime.py:35`
- `src/containment.py:1538`
- `src/containment.py:1677`
- `src/process_lifecycle.py:663`
- `src/tools/cookbook.py:1132`
- `tests/test_notes_native_cleanup.py:38`
- `tests/test_process_lifecycle.py:244`

## `escalate` — function, line 449
- **called from:**
- `src/containment.py:1537`
- `src/process_lifecycle.py:660`
- `tests/test_process_lifecycle.py:89`
- `tests/test_process_lifecycle.py:95`
- `tests/test_process_lifecycle.py:102`
- `tests/test_process_lifecycle.py:109`
- `tests/test_process_lifecycle.py:124`

## `escalate_async` — function (async), line 486
- **called from:**
- `routes/shell_routes.py:809`
- `src/containment.py:1676`
- `tests/test_process_lifecycle.py:136`
- `tests/test_process_lifecycle.py:150`

## `IdentitySweep` — class, line 532
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/process_lifecycle.py:601`

## `IdentitySweep.dead` — method, line 546
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `signal_identity` — function, line 550
- **called from:**
- `src/process_lifecycle.py:588`
- `tests/test_process_resource_identity.py:69`
- `tests/test_runtime_resource_integration.py:507`

## `terminate_identities` — function, line 565
- **called from:**
- `scripts/verify_notes_browser_runtime.py:33`
- `src/agent_tools/web_tools.py:2461`
- `src/agent_tools/web_tools.py:2513`
- `src/agent_tools/web_tools_prewave3.py:2470`
- `src/agent_tools/web_tools_prewave3.py:2522`
- `src/browser_lifecycle.py:232`
- `src/tools/cookbook.py:1129`
- `tests/test_notes_native_cleanup.py:38`
- `tests/test_process_lifecycle.py:208`
- `tests/test_process_lifecycle.py:229`
- `tests/test_process_lifecycle.py:243`

## `terminate_tree` — function, line 610
- **called from:**
- `core/platform_compat.py:161`
- `tests/test_process_lifecycle.py:257`
- `tests/test_process_lifecycle.py:265`
- `tests/test_process_lifecycle.py:278`

## `refusal` — function, line 635
- **called from:**
- `src/process_lifecycle.py:651`
- `src/process_lifecycle.py:664`
