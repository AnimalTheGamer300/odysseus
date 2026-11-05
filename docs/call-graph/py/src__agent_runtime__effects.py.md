# `src/agent_runtime/effects.py` — definitions & call sites

65 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_sha` — function, line 31
- **called from:**
- `src/agent_runtime/effects.py:97`
- `src/agent_runtime/effects.py:154`
- `src/agent_runtime/effects.py:155`
- `src/agent_runtime/effects.py:156`
- `src/agent_runtime/effects.py:161`
- `src/agent_runtime/effects.py:168`
- `src/agent_runtime/effects.py:173`
- `src/agent_runtime/effects.py:177`
- `src/agent_runtime/effects.py:181`
- `src/agent_runtime/effects.py:186`
- `src/agent_runtime/effects.py:224`

## `_text` — function, line 36
- **called from:**
- `src/agent_runtime/effects.py:85`
- `src/agent_runtime/effects.py:86`
- `src/agent_runtime/effects.py:212`
- `src/agent_runtime/effects.py:213`
- `src/agent_runtime/effects.py:214`
- `src/agent_runtime/effects.py:304`
- `src/agent_runtime/effects.py:305`
- `src/agent_runtime/effects.py:405`
- `src/agent_runtime/effects.py:469`
- `src/agent_runtime/effects.py:470`
- `src/agent_runtime/effects.py:552`
- `src/agent_runtime/effects.py:554`
- `src/agent_runtime/resources.py:26`
- `src/agent_runtime/resources.py:192`
- `src/agent_runtime/resources.py:222`
- `src/agent_runtime/resources.py:223`
- `src/agent_runtime/resources.py:256`
- `src/agent_runtime/resources.py:257`
- `src/agent_runtime/resources.py:309`
- `src/agent_runtime/resources.py:461`
- `src/agent_runtime/resources.py:463`
- `src/agent_runtime/resources.py:473`
- `src/agent_runtime/resources.py:550`
- `src/agent_runtime/resources.py:551`
- `src/agent_runtime/resources.py:586`
- `src/agent_runtime/resources.py:587`
- `src/agent_runtime/resources.py:624`
- `src/agent_runtime/resources.py:627`
- `src/agent_runtime/resources.py:641`
- `src/agent_runtime/resources.py:671`
- `src/agent_runtime/resources.py:672`
- `src/agent_runtime/resources.py:673`
- `src/agent_runtime/resources.py:688`
- `src/agent_runtime/resources.py:693`

## `_position` — function, line 42
- **called from:**
- `src/agent_runtime/effects.py:306`
- `src/agent_runtime/effects.py:471`
- `src/agent_runtime/effects.py:555`
- `src/agent_runtime/effects.py:819`
- `static/js/chat.js:7865`
- `static/js/chat.js:7874`
- `static/js/chat.js:7897`
- `static/js/chat.js:7898`
- `static/js/modalSnap.js:1077`
- `static/js/modalSnap.js:1116`
- `static/js/slashAutocomplete.js:141`
- `static/js/slashAutocomplete.js:211`
- `static/js/slashAutocomplete.js:299`

## `ResourceKind` — class, line 54
- **called from:**
- `src/agent_runtime/effects.py:135`

## `ResourceRef` — class, line 65
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/effects.py:156`
- `src/agent_runtime/effects.py:161`
- `src/agent_runtime/effects.py:167`
- `src/agent_runtime/effects.py:172`
- `src/agent_runtime/effects.py:177`
- `src/agent_runtime/effects.py:181`
- `src/agent_runtime/effects.py:185`

## `ResourceRef.__post_init__` — method, line 82
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResourceRef.location_key` — method, line 96
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResourceRef.same_location` — method, line 99
- **called from:**
- `src/agent_runtime/effects.py:588`
- `src/agent_runtime/effects.py:691`
- `src/agent_runtime/effects.py:757`
- `tests/test_effects_foundation.py:94`
- `tests/test_effects_foundation.py:126`
- `tests/test_effects_foundation.py:132`

## `ResourceRef.overlaps` — method, line 102
- **called from:**
- `src/agent_runtime/effects.py:667`
- `tests/test_effects_foundation.py:113`
- `tests/test_effects_foundation.py:113`
- `tests/test_effects_foundation.py:114`
- `tests/test_effects_foundation.py:119`
- `tests/test_effects_foundation.py:126`

## `ResourceRef.to_dict` — method, line 124
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5624`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28789`
- `src/agent_loop.py:31316`
- `src/agent_loop.py:31789`
- `src/agent_loop.py:32054`
- `src/agent_loop.py:32094`
- `src/agent_loop.py:32125`
- `src/agent_loop.py:32178`
- `src/agent_loop.py:32306`
- `src/agent_loop.py:32638`
- `src/agent_loop.py:34858`
- `src/agent_loop.py:36867`
- `src/agent_loop.py:37190`
- `src/agent_loop.py:37403`
- `src/agent_loop.py:37458`
- `src/agent_loop.py:37515`
- `src/agent_loop.py:37849`
- `src/agent_loop.py:37861`
- `src/agent_loop.py:37967`
- `src/agent_loop.py:38889`
- `src/agent_loop.py:38890`
- `src/agent_loop.py:38895`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:653`
- `src/agent_runtime/authority.py:677`
- `src/agent_runtime/authority.py:677`
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

## `ResourceRef.from_dict` — method, line 129
- decorator: `classmethod`
- **called from:**
- `src/agent_runtime/authority.py:319`
- `src/agent_runtime/authority.py:320`
- `src/agent_runtime/authority.py:321`
- `src/agent_runtime/authority.py:322`
- `src/agent_runtime/authority.py:323`
- `src/agent_runtime/authority.py:324`
- `src/agent_runtime/authority.py:325`
- `src/agent_runtime/authority.py:661`
- `src/agent_runtime/authority.py:683`
- `src/agent_runtime/authority.py:686`
- `src/agent_runtime/effect_log.py:91`
- `src/agent_runtime/effects.py:277`
- `src/agent_runtime/effects.py:340`
- `src/agent_runtime/effects.py:341`
- `src/agent_runtime/effects.py:342`
- `src/agent_runtime/effects.py:343`
- `src/agent_runtime/effects.py:493`
- `src/agent_runtime/effects.py:576`
- `src/agent_runtime/process_resources.py:80`
- `src/agent_runtime/process_resources.py:89`
- `src/agent_runtime/process_resources.py:129`
- `src/agent_runtime/process_resources.py:475`
- `src/agent_runtime/resources.py:238`
- `src/agent_runtime/resources.py:275`
- `src/agent_runtime/resources.py:531`
- `src/agent_runtime/resources.py:570`
- `src/agent_runtime/resources.py:608`
- `src/agent_trace.py:124`
- `src/bg_jobs.py:227`
- `src/containment_worker.py:52`
- `src/containment_worker.py:53`
- `tests/test_background_resource_identity.py:54`
- `tests/test_background_resource_identity.py:65`
- `tests/test_background_resource_identity.py:187`
- `tests/test_background_resource_identity.py:191`
- `tests/test_browser_resource_identity.py:160`
- `tests/test_browser_resource_identity.py:321`
- `tests/test_effect_journal_persistence.py:43`
- `tests/test_effects_foundation.py:139`
- `tests/test_effects_foundation.py:141`
- `tests/test_effects_foundation.py:143`
- `tests/test_effects_foundation.py:160`
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`
- `tests/test_owned_resource_identity.py:180`
- `tests/test_owned_resource_identity.py:322`
- `tests/test_owned_resource_identity.py:327`
- `tests/test_process_resource_identity.py:31`
- `tests/test_process_resource_identity.py:37`
- `tests/test_process_resource_identity.py:41`
- `tests/test_process_resource_identity.py:88`
- `tests/test_remote_resource_identity.py:68`
- `tests/test_remote_resource_identity.py:162`
- `tests/test_request_authority.py:115`
- `tests/test_resource_identity.py:379`
- `tests/test_resource_identity.py:393`
- `tests/test_resource_identity.py:660`
- `tests/test_resource_identity.py:683`
- `tests/test_runtime_resource_integration.py:416`
- `tests/test_wave3_launch_cost_lifecycle.py:102`
- … +1 more (grep the name in repo)

## `resource_ref` — function, line 139
- **called from:**
- `src/agent_runtime/effect_adapters.py:155`
- `src/agent_runtime/effect_adapters.py:217`
- `src/agent_runtime/effect_adapters.py:222`
- `src/agent_runtime/effect_adapters.py:223`
- `src/agent_runtime/effect_adapters.py:224`
- `src/agent_runtime/effect_adapters.py:228`
- `src/agent_runtime/effect_adapters.py:229`
- `src/agent_runtime/effect_adapters.py:246`
- `src/agent_runtime/effect_adapters.py:431`
- `src/agent_runtime/effect_adapters.py:444`
- `src/agent_runtime/effect_adapters.py:454`
- `src/agent_runtime/effect_adapters.py:458`
- `src/agent_runtime/effect_adapters.py:466`
- `src/agent_runtime/effects.py:195`
- `tests/test_effect_journal_persistence.py:22`
- `tests/test_effect_journal_persistence.py:161`
- `tests/test_effect_verification_adapters.py:236`
- `tests/test_effect_verification_adapters.py:264`
- `tests/test_effect_verification_adapters.py:323`
- `tests/test_effect_verification_adapters.py:363`
- `tests/test_effects_foundation.py:30`
- `tests/test_effects_foundation.py:81`
- `tests/test_effects_foundation.py:84`
- `tests/test_effects_foundation.py:119`
- `tests/test_effects_foundation.py:125`
- `tests/test_effects_foundation.py:125`
- `tests/test_effects_foundation.py:130`
- `tests/test_effects_foundation.py:131`
- `tests/test_effects_foundation.py:133`
- `tests/test_effects_foundation.py:234`
- `tests/test_effects_foundation.py:445`
- `tests/test_effects_foundation.py:446`

## `bound_filesystem_refs` — function, line 190
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `OperationRef` — class, line 203
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/effect_adapters.py:77`
- `tests/test_effect_journal_persistence.py:26`
- `tests/test_effect_journal_persistence.py:163`
- `tests/test_effect_verification_adapters.py:365`
- `tests/test_effects_foundation.py:34`

## `OperationRef.__post_init__` — method, line 211
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `OperationRef.from_exact` — method, line 219
- decorator: `classmethod`
- **called from:**
- `src/agent_runtime/effect_adapters.py:73`
- `tests/test_effects_foundation.py:148`
- `tests/test_effects_foundation.py:150`

## `OperationRef.to_dict` — method, line 226
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5624`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28789`
- `src/agent_loop.py:31316`
- `src/agent_loop.py:31789`
- `src/agent_loop.py:32054`
- `src/agent_loop.py:32094`
- `src/agent_loop.py:32125`
- `src/agent_loop.py:32178`
- `src/agent_loop.py:32306`
- `src/agent_loop.py:32638`
- `src/agent_loop.py:34858`
- `src/agent_loop.py:36867`
- `src/agent_loop.py:37190`
- `src/agent_loop.py:37403`
- `src/agent_loop.py:37458`
- `src/agent_loop.py:37515`
- `src/agent_loop.py:37849`
- `src/agent_loop.py:37861`
- `src/agent_loop.py:37967`
- `src/agent_loop.py:38889`
- `src/agent_loop.py:38890`
- `src/agent_loop.py:38895`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:653`
- `src/agent_runtime/authority.py:677`
- `src/agent_runtime/authority.py:677`
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

## `OperationRef.from_dict` — method, line 231
- decorator: `classmethod`
- **called from:**
- `src/agent_runtime/authority.py:319`
- `src/agent_runtime/authority.py:320`
- `src/agent_runtime/authority.py:321`
- `src/agent_runtime/authority.py:322`
- `src/agent_runtime/authority.py:323`
- `src/agent_runtime/authority.py:324`
- `src/agent_runtime/authority.py:325`
- `src/agent_runtime/authority.py:661`
- `src/agent_runtime/authority.py:683`
- `src/agent_runtime/authority.py:686`
- `src/agent_runtime/effect_log.py:91`
- `src/agent_runtime/effects.py:277`
- `src/agent_runtime/effects.py:340`
- `src/agent_runtime/effects.py:341`
- `src/agent_runtime/effects.py:342`
- `src/agent_runtime/effects.py:343`
- `src/agent_runtime/effects.py:493`
- `src/agent_runtime/effects.py:576`
- `src/agent_runtime/process_resources.py:80`
- `src/agent_runtime/process_resources.py:89`
- `src/agent_runtime/process_resources.py:129`
- `src/agent_runtime/process_resources.py:475`
- `src/agent_runtime/resources.py:238`
- `src/agent_runtime/resources.py:275`
- `src/agent_runtime/resources.py:531`
- `src/agent_runtime/resources.py:570`
- `src/agent_runtime/resources.py:608`
- `src/agent_trace.py:124`
- `src/bg_jobs.py:227`
- `src/containment_worker.py:52`
- `src/containment_worker.py:53`
- `tests/test_background_resource_identity.py:54`
- `tests/test_background_resource_identity.py:65`
- `tests/test_background_resource_identity.py:187`
- `tests/test_background_resource_identity.py:191`
- `tests/test_browser_resource_identity.py:160`
- `tests/test_browser_resource_identity.py:321`
- `tests/test_effect_journal_persistence.py:43`
- `tests/test_effects_foundation.py:139`
- `tests/test_effects_foundation.py:141`
- `tests/test_effects_foundation.py:143`
- `tests/test_effects_foundation.py:160`
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`
- `tests/test_owned_resource_identity.py:180`
- `tests/test_owned_resource_identity.py:322`
- `tests/test_owned_resource_identity.py:327`
- `tests/test_process_resource_identity.py:31`
- `tests/test_process_resource_identity.py:37`
- `tests/test_process_resource_identity.py:41`
- `tests/test_process_resource_identity.py:88`
- `tests/test_remote_resource_identity.py:68`
- `tests/test_remote_resource_identity.py:162`
- `tests/test_request_authority.py:115`
- `tests/test_resource_identity.py:379`
- `tests/test_resource_identity.py:393`
- `tests/test_resource_identity.py:660`
- `tests/test_resource_identity.py:683`
- `tests/test_runtime_resource_integration.py:416`
- `tests/test_wave3_launch_cost_lifecycle.py:102`
- … +1 more (grep the name in repo)

## `Predicate` — class, line 237
- **called from:**
- `src/agent_runtime/effects.py:277`

## `Postcondition` — class, line 254
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/effect_adapters.py:170`
- `src/agent_runtime/effect_adapters.py:175`
- `src/agent_runtime/effect_adapters.py:182`
- `src/agent_runtime/effect_adapters.py:185`
- `src/agent_runtime/effect_adapters.py:190`
- `tests/test_effect_journal_persistence.py:27`
- `tests/test_effect_verification_adapters.py:366`
- `tests/test_effects_foundation.py:72`
- `tests/test_effects_foundation.py:236`
- `tests/test_effects_foundation.py:345`
- `tests/test_effects_foundation.py:448`

## `Postcondition.__post_init__` — method, line 261
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `Postcondition.to_dict` — method, line 270
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5624`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28789`
- `src/agent_loop.py:31316`
- `src/agent_loop.py:31789`
- `src/agent_loop.py:32054`
- `src/agent_loop.py:32094`
- `src/agent_loop.py:32125`
- `src/agent_loop.py:32178`
- `src/agent_loop.py:32306`
- `src/agent_loop.py:32638`
- `src/agent_loop.py:34858`
- `src/agent_loop.py:36867`
- `src/agent_loop.py:37190`
- `src/agent_loop.py:37403`
- `src/agent_loop.py:37458`
- `src/agent_loop.py:37515`
- `src/agent_loop.py:37849`
- `src/agent_loop.py:37861`
- `src/agent_loop.py:37967`
- `src/agent_loop.py:38889`
- `src/agent_loop.py:38890`
- `src/agent_loop.py:38895`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:653`
- `src/agent_runtime/authority.py:677`
- `src/agent_runtime/authority.py:677`
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

## `Postcondition.from_dict` — method, line 274
- decorator: `classmethod`
- **called from:**
- `src/agent_runtime/authority.py:319`
- `src/agent_runtime/authority.py:320`
- `src/agent_runtime/authority.py:321`
- `src/agent_runtime/authority.py:322`
- `src/agent_runtime/authority.py:323`
- `src/agent_runtime/authority.py:324`
- `src/agent_runtime/authority.py:325`
- `src/agent_runtime/authority.py:661`
- `src/agent_runtime/authority.py:683`
- `src/agent_runtime/authority.py:686`
- `src/agent_runtime/effect_log.py:91`
- `src/agent_runtime/effects.py:277`
- `src/agent_runtime/effects.py:340`
- `src/agent_runtime/effects.py:341`
- `src/agent_runtime/effects.py:342`
- `src/agent_runtime/effects.py:343`
- `src/agent_runtime/effects.py:493`
- `src/agent_runtime/effects.py:576`
- `src/agent_runtime/process_resources.py:80`
- `src/agent_runtime/process_resources.py:89`
- `src/agent_runtime/process_resources.py:129`
- `src/agent_runtime/process_resources.py:475`
- `src/agent_runtime/resources.py:238`
- `src/agent_runtime/resources.py:275`
- `src/agent_runtime/resources.py:531`
- `src/agent_runtime/resources.py:570`
- `src/agent_runtime/resources.py:608`
- `src/agent_trace.py:124`
- `src/bg_jobs.py:227`
- `src/containment_worker.py:52`
- `src/containment_worker.py:53`
- `tests/test_background_resource_identity.py:54`
- `tests/test_background_resource_identity.py:65`
- `tests/test_background_resource_identity.py:187`
- `tests/test_background_resource_identity.py:191`
- `tests/test_browser_resource_identity.py:160`
- `tests/test_browser_resource_identity.py:321`
- `tests/test_effect_journal_persistence.py:43`
- `tests/test_effects_foundation.py:139`
- `tests/test_effects_foundation.py:141`
- `tests/test_effects_foundation.py:143`
- `tests/test_effects_foundation.py:160`
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`
- `tests/test_owned_resource_identity.py:180`
- `tests/test_owned_resource_identity.py:322`
- `tests/test_owned_resource_identity.py:327`
- `tests/test_process_resource_identity.py:31`
- `tests/test_process_resource_identity.py:37`
- `tests/test_process_resource_identity.py:41`
- `tests/test_process_resource_identity.py:88`
- `tests/test_remote_resource_identity.py:68`
- `tests/test_remote_resource_identity.py:162`
- `tests/test_request_authority.py:115`
- `tests/test_resource_identity.py:379`
- `tests/test_resource_identity.py:393`
- `tests/test_resource_identity.py:660`
- `tests/test_resource_identity.py:683`
- `tests/test_runtime_resource_integration.py:416`
- `tests/test_wave3_launch_cost_lifecycle.py:102`
- … +1 more (grep the name in repo)

## `EffectClaim` — class, line 281
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/effect_log.py:345`
- `tests/test_effects_foundation.py:48`
- `tests/test_effects_foundation.py:158`
- `tests/test_effects_foundation.py:159`
- `tests/test_effects_foundation.py:161`

## `EffectClaim.__post_init__` — method, line 302
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EffectClaim.unknown_scope` — method, line 321
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EffectClaim.to_dict` — method, line 324
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5624`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28789`
- `src/agent_loop.py:31316`
- `src/agent_loop.py:31789`
- `src/agent_loop.py:32054`
- `src/agent_loop.py:32094`
- `src/agent_loop.py:32125`
- `src/agent_loop.py:32178`
- `src/agent_loop.py:32306`
- `src/agent_loop.py:32638`
- `src/agent_loop.py:34858`
- `src/agent_loop.py:36867`
- `src/agent_loop.py:37190`
- `src/agent_loop.py:37403`
- `src/agent_loop.py:37458`
- `src/agent_loop.py:37515`
- `src/agent_loop.py:37849`
- `src/agent_loop.py:37861`
- `src/agent_loop.py:37967`
- `src/agent_loop.py:38889`
- `src/agent_loop.py:38890`
- `src/agent_loop.py:38895`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:653`
- `src/agent_runtime/authority.py:677`
- `src/agent_runtime/authority.py:677`
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

## `EffectClaim.from_dict` — method, line 333
- decorator: `classmethod`
- **called from:**
- `src/agent_runtime/authority.py:319`
- `src/agent_runtime/authority.py:320`
- `src/agent_runtime/authority.py:321`
- `src/agent_runtime/authority.py:322`
- `src/agent_runtime/authority.py:323`
- `src/agent_runtime/authority.py:324`
- `src/agent_runtime/authority.py:325`
- `src/agent_runtime/authority.py:661`
- `src/agent_runtime/authority.py:683`
- `src/agent_runtime/authority.py:686`
- `src/agent_runtime/effect_log.py:91`
- `src/agent_runtime/effects.py:277`
- `src/agent_runtime/effects.py:340`
- `src/agent_runtime/effects.py:341`
- `src/agent_runtime/effects.py:342`
- `src/agent_runtime/effects.py:343`
- `src/agent_runtime/effects.py:493`
- `src/agent_runtime/effects.py:576`
- `src/agent_runtime/process_resources.py:80`
- `src/agent_runtime/process_resources.py:89`
- `src/agent_runtime/process_resources.py:129`
- `src/agent_runtime/process_resources.py:475`
- `src/agent_runtime/resources.py:238`
- `src/agent_runtime/resources.py:275`
- `src/agent_runtime/resources.py:531`
- `src/agent_runtime/resources.py:570`
- `src/agent_runtime/resources.py:608`
- `src/agent_trace.py:124`
- `src/bg_jobs.py:227`
- `src/containment_worker.py:52`
- `src/containment_worker.py:53`
- `tests/test_background_resource_identity.py:54`
- `tests/test_background_resource_identity.py:65`
- `tests/test_background_resource_identity.py:187`
- `tests/test_background_resource_identity.py:191`
- `tests/test_browser_resource_identity.py:160`
- `tests/test_browser_resource_identity.py:321`
- `tests/test_effect_journal_persistence.py:43`
- `tests/test_effects_foundation.py:139`
- `tests/test_effects_foundation.py:141`
- `tests/test_effects_foundation.py:143`
- `tests/test_effects_foundation.py:160`
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`
- `tests/test_owned_resource_identity.py:180`
- `tests/test_owned_resource_identity.py:322`
- `tests/test_owned_resource_identity.py:327`
- `tests/test_process_resource_identity.py:31`
- `tests/test_process_resource_identity.py:37`
- `tests/test_process_resource_identity.py:41`
- `tests/test_process_resource_identity.py:88`
- `tests/test_remote_resource_identity.py:68`
- `tests/test_remote_resource_identity.py:162`
- `tests/test_request_authority.py:115`
- `tests/test_resource_identity.py:379`
- `tests/test_resource_identity.py:393`
- `tests/test_resource_identity.py:660`
- `tests/test_resource_identity.py:683`
- `tests/test_runtime_resource_integration.py:416`
- `tests/test_wave3_launch_cost_lifecycle.py:102`
- … +1 more (grep the name in repo)

## `ExecutionOutcome` — class, line 351
- **called from:**
- `src/agent_runtime/effects.py:492`

## `Impact` — class, line 362
- **called from:**
- `src/agent_runtime/effects.py:493`

## `CleanupState` — class, line 368
- **called from:**
- `src/agent_runtime/effects.py:494`

## `ProducerFacts` — class, line 380
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/effect_adapters.py:294`
- `src/agent_runtime/effect_adapters.py:296`
- `src/agent_runtime/effect_adapters.py:350`
- `src/agent_runtime/effect_adapters.py:532`
- `src/agent_runtime/effects.py:434`
- `src/agent_runtime/effects.py:439`
- `src/agent_runtime/effects.py:463`
- `tests/test_effect_resource_bindings.py:443`
- `tests/test_effect_verification_adapters.py:404`
- `tests/test_effects_foundation.py:180`
- `tests/test_effects_foundation.py:181`
- `tests/test_effects_foundation.py:237`
- `tests/test_effects_foundation.py:401`
- `tests/test_effects_foundation.py:421`

## `ProducerFacts.__post_init__` — method, line 397
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ProducerFacts.to_dict` — method, line 409
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5624`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28789`
- `src/agent_loop.py:31316`
- `src/agent_loop.py:31789`
- `src/agent_loop.py:32054`
- `src/agent_loop.py:32094`
- `src/agent_loop.py:32125`
- `src/agent_loop.py:32178`
- `src/agent_loop.py:32306`
- `src/agent_loop.py:32638`
- `src/agent_loop.py:34858`
- `src/agent_loop.py:36867`
- `src/agent_loop.py:37190`
- `src/agent_loop.py:37403`
- `src/agent_loop.py:37458`
- `src/agent_loop.py:37515`
- `src/agent_loop.py:37849`
- `src/agent_loop.py:37861`
- `src/agent_loop.py:37967`
- `src/agent_loop.py:38889`
- `src/agent_loop.py:38890`
- `src/agent_loop.py:38895`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:653`
- `src/agent_runtime/authority.py:677`
- `src/agent_runtime/authority.py:677`
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

## `ProducerFacts.from_dict` — method, line 416
- decorator: `classmethod`
- **called from:**
- `src/agent_runtime/authority.py:319`
- `src/agent_runtime/authority.py:320`
- `src/agent_runtime/authority.py:321`
- `src/agent_runtime/authority.py:322`
- `src/agent_runtime/authority.py:323`
- `src/agent_runtime/authority.py:324`
- `src/agent_runtime/authority.py:325`
- `src/agent_runtime/authority.py:661`
- `src/agent_runtime/authority.py:683`
- `src/agent_runtime/authority.py:686`
- `src/agent_runtime/effect_log.py:91`
- `src/agent_runtime/effects.py:277`
- `src/agent_runtime/effects.py:340`
- `src/agent_runtime/effects.py:341`
- `src/agent_runtime/effects.py:342`
- `src/agent_runtime/effects.py:343`
- `src/agent_runtime/effects.py:493`
- `src/agent_runtime/effects.py:576`
- `src/agent_runtime/process_resources.py:80`
- `src/agent_runtime/process_resources.py:89`
- `src/agent_runtime/process_resources.py:129`
- `src/agent_runtime/process_resources.py:475`
- `src/agent_runtime/resources.py:238`
- `src/agent_runtime/resources.py:275`
- `src/agent_runtime/resources.py:531`
- `src/agent_runtime/resources.py:570`
- `src/agent_runtime/resources.py:608`
- `src/agent_trace.py:124`
- `src/bg_jobs.py:227`
- `src/containment_worker.py:52`
- `src/containment_worker.py:53`
- `tests/test_background_resource_identity.py:54`
- `tests/test_background_resource_identity.py:65`
- `tests/test_background_resource_identity.py:187`
- `tests/test_background_resource_identity.py:191`
- `tests/test_browser_resource_identity.py:160`
- `tests/test_browser_resource_identity.py:321`
- `tests/test_effect_journal_persistence.py:43`
- `tests/test_effects_foundation.py:139`
- `tests/test_effects_foundation.py:141`
- `tests/test_effects_foundation.py:143`
- `tests/test_effects_foundation.py:160`
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`
- `tests/test_owned_resource_identity.py:180`
- `tests/test_owned_resource_identity.py:322`
- `tests/test_owned_resource_identity.py:327`
- `tests/test_process_resource_identity.py:31`
- `tests/test_process_resource_identity.py:37`
- `tests/test_process_resource_identity.py:41`
- `tests/test_process_resource_identity.py:88`
- `tests/test_remote_resource_identity.py:68`
- `tests/test_remote_resource_identity.py:162`
- `tests/test_request_authority.py:115`
- `tests/test_resource_identity.py:379`
- `tests/test_resource_identity.py:393`
- `tests/test_resource_identity.py:660`
- `tests/test_resource_identity.py:683`
- `tests/test_runtime_resource_integration.py:416`
- `tests/test_wave3_launch_cost_lifecycle.py:102`
- … +1 more (grep the name in repo)

## `_label` — function, line 422
- **called from:**
- `src/agent_runtime/effects.py:441`
- `src/agent_runtime/effects.py:443`
- `src/agent_runtime/effects.py:444`
- `src/service_health.py:337`
- `src/service_health.py:353`
- `src/service_health.py:379`
- `src/service_health.py:393`

## `producer_facts` — function, line 427
- **called from:**
- `src/agent_runtime/effect_adapters.py:291`
- `tests/test_effects_foundation.py:179`
- `tests/test_effects_foundation.py:181`
- `tests/test_effects_foundation.py:182`

## `EffectOutcome` — class, line 451
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/effect_log.py:350`
- `src/agent_runtime/effect_log.py:508`
- `src/agent_runtime/effects.py:822`
- `tests/test_effect_journal_persistence.py:119`
- `tests/test_effects_foundation.py:54`
- `tests/test_effects_foundation.py:166`
- `tests/test_effects_foundation.py:168`
- `tests/test_effects_foundation.py:170`
- `tests/test_effects_foundation.py:172`
- `tests/test_effects_foundation.py:173`

## `EffectOutcome.__post_init__` — method, line 468
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EffectOutcome.to_dict` — method, line 483
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5624`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28789`
- `src/agent_loop.py:31316`
- `src/agent_loop.py:31789`
- `src/agent_loop.py:32054`
- `src/agent_loop.py:32094`
- `src/agent_loop.py:32125`
- `src/agent_loop.py:32178`
- `src/agent_loop.py:32306`
- `src/agent_loop.py:32638`
- `src/agent_loop.py:34858`
- `src/agent_loop.py:36867`
- `src/agent_loop.py:37190`
- `src/agent_loop.py:37403`
- `src/agent_loop.py:37458`
- `src/agent_loop.py:37515`
- `src/agent_loop.py:37849`
- `src/agent_loop.py:37861`
- `src/agent_loop.py:37967`
- `src/agent_loop.py:38889`
- `src/agent_loop.py:38890`
- `src/agent_loop.py:38895`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:653`
- `src/agent_runtime/authority.py:677`
- `src/agent_runtime/authority.py:677`
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

## `EffectOutcome.from_dict` — method, line 489
- decorator: `classmethod`
- **called from:**
- `src/agent_runtime/authority.py:319`
- `src/agent_runtime/authority.py:320`
- `src/agent_runtime/authority.py:321`
- `src/agent_runtime/authority.py:322`
- `src/agent_runtime/authority.py:323`
- `src/agent_runtime/authority.py:324`
- `src/agent_runtime/authority.py:325`
- `src/agent_runtime/authority.py:661`
- `src/agent_runtime/authority.py:683`
- `src/agent_runtime/authority.py:686`
- `src/agent_runtime/effect_log.py:91`
- `src/agent_runtime/effects.py:277`
- `src/agent_runtime/effects.py:340`
- `src/agent_runtime/effects.py:341`
- `src/agent_runtime/effects.py:342`
- `src/agent_runtime/effects.py:343`
- `src/agent_runtime/effects.py:493`
- `src/agent_runtime/effects.py:576`
- `src/agent_runtime/process_resources.py:80`
- `src/agent_runtime/process_resources.py:89`
- `src/agent_runtime/process_resources.py:129`
- `src/agent_runtime/process_resources.py:475`
- `src/agent_runtime/resources.py:238`
- `src/agent_runtime/resources.py:275`
- `src/agent_runtime/resources.py:531`
- `src/agent_runtime/resources.py:570`
- `src/agent_runtime/resources.py:608`
- `src/agent_trace.py:124`
- `src/bg_jobs.py:227`
- `src/containment_worker.py:52`
- `src/containment_worker.py:53`
- `tests/test_background_resource_identity.py:54`
- `tests/test_background_resource_identity.py:65`
- `tests/test_background_resource_identity.py:187`
- `tests/test_background_resource_identity.py:191`
- `tests/test_browser_resource_identity.py:160`
- `tests/test_browser_resource_identity.py:321`
- `tests/test_effect_journal_persistence.py:43`
- `tests/test_effects_foundation.py:139`
- `tests/test_effects_foundation.py:141`
- `tests/test_effects_foundation.py:143`
- `tests/test_effects_foundation.py:160`
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`
- `tests/test_owned_resource_identity.py:180`
- `tests/test_owned_resource_identity.py:322`
- `tests/test_owned_resource_identity.py:327`
- `tests/test_process_resource_identity.py:31`
- `tests/test_process_resource_identity.py:37`
- `tests/test_process_resource_identity.py:41`
- `tests/test_process_resource_identity.py:88`
- `tests/test_remote_resource_identity.py:68`
- `tests/test_remote_resource_identity.py:162`
- `tests/test_request_authority.py:115`
- `tests/test_resource_identity.py:379`
- `tests/test_resource_identity.py:393`
- `tests/test_resource_identity.py:660`
- `tests/test_resource_identity.py:683`
- `tests/test_runtime_resource_integration.py:416`
- `tests/test_wave3_launch_cost_lifecycle.py:102`
- … +1 more (grep the name in repo)

## `ObservationMechanism` — class, line 501
- **called from:**
- `src/agent_runtime/effects.py:577`

## `Coverage` — class, line 513
- **called from:**
- `src/agent_runtime/effects.py:578`

## `Observation` — class, line 531
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/effect_log.py:353`
- `src/process_lifecycle.py:211`
- `src/process_lifecycle.py:260`
- `tests/test_effects_foundation.py:61`
- `tests/test_effects_foundation.py:194`
- `tests/test_effects_foundation.py:463`
- `tests/test_effects_foundation.py:465`

## `Observation.__post_init__` — method, line 551
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `Observation.to_dict` — method, line 565
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5624`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28789`
- `src/agent_loop.py:31316`
- `src/agent_loop.py:31789`
- `src/agent_loop.py:32054`
- `src/agent_loop.py:32094`
- `src/agent_loop.py:32125`
- `src/agent_loop.py:32178`
- `src/agent_loop.py:32306`
- `src/agent_loop.py:32638`
- `src/agent_loop.py:34858`
- `src/agent_loop.py:36867`
- `src/agent_loop.py:37190`
- `src/agent_loop.py:37403`
- `src/agent_loop.py:37458`
- `src/agent_loop.py:37515`
- `src/agent_loop.py:37849`
- `src/agent_loop.py:37861`
- `src/agent_loop.py:37967`
- `src/agent_loop.py:38889`
- `src/agent_loop.py:38890`
- `src/agent_loop.py:38895`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:653`
- `src/agent_runtime/authority.py:677`
- `src/agent_runtime/authority.py:677`
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

## `Observation.from_dict` — method, line 573
- decorator: `classmethod`
- **called from:**
- `src/agent_runtime/authority.py:319`
- `src/agent_runtime/authority.py:320`
- `src/agent_runtime/authority.py:321`
- `src/agent_runtime/authority.py:322`
- `src/agent_runtime/authority.py:323`
- `src/agent_runtime/authority.py:324`
- `src/agent_runtime/authority.py:325`
- `src/agent_runtime/authority.py:661`
- `src/agent_runtime/authority.py:683`
- `src/agent_runtime/authority.py:686`
- `src/agent_runtime/effect_log.py:91`
- `src/agent_runtime/effects.py:277`
- `src/agent_runtime/effects.py:340`
- `src/agent_runtime/effects.py:341`
- `src/agent_runtime/effects.py:342`
- `src/agent_runtime/effects.py:343`
- `src/agent_runtime/effects.py:493`
- `src/agent_runtime/effects.py:576`
- `src/agent_runtime/process_resources.py:80`
- `src/agent_runtime/process_resources.py:89`
- `src/agent_runtime/process_resources.py:129`
- `src/agent_runtime/process_resources.py:475`
- `src/agent_runtime/resources.py:238`
- `src/agent_runtime/resources.py:275`
- `src/agent_runtime/resources.py:531`
- `src/agent_runtime/resources.py:570`
- `src/agent_runtime/resources.py:608`
- `src/agent_trace.py:124`
- `src/bg_jobs.py:227`
- `src/containment_worker.py:52`
- `src/containment_worker.py:53`
- `tests/test_background_resource_identity.py:54`
- `tests/test_background_resource_identity.py:65`
- `tests/test_background_resource_identity.py:187`
- `tests/test_background_resource_identity.py:191`
- `tests/test_browser_resource_identity.py:160`
- `tests/test_browser_resource_identity.py:321`
- `tests/test_effect_journal_persistence.py:43`
- `tests/test_effects_foundation.py:139`
- `tests/test_effects_foundation.py:141`
- `tests/test_effects_foundation.py:143`
- `tests/test_effects_foundation.py:160`
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`
- `tests/test_owned_resource_identity.py:180`
- `tests/test_owned_resource_identity.py:322`
- `tests/test_owned_resource_identity.py:327`
- `tests/test_process_resource_identity.py:31`
- `tests/test_process_resource_identity.py:37`
- `tests/test_process_resource_identity.py:41`
- `tests/test_process_resource_identity.py:88`
- `tests/test_remote_resource_identity.py:68`
- `tests/test_remote_resource_identity.py:162`
- `tests/test_request_authority.py:115`
- `tests/test_resource_identity.py:379`
- `tests/test_resource_identity.py:393`
- `tests/test_resource_identity.py:660`
- `tests/test_resource_identity.py:683`
- `tests/test_runtime_resource_integration.py:416`
- `tests/test_wave3_launch_cost_lifecycle.py:102`
- … +1 more (grep the name in repo)

## `predicate_holds` — function, line 581
- **called from:**
- `src/agent_runtime/effects.py:767`
- `tests/test_effect_resource_bindings.py:250`

## `Freshness` — class, line 609
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EffectHistory` — class, line 616
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/effect_log.py:193`
- `tests/test_effects_foundation.py:68`
- `tests/test_effects_foundation.py:197`
- `tests/test_effects_foundation.py:439`

## `EffectHistory.__post_init__` — method, line 627
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EffectHistory.claim` — method, line 652
- **called from:**
- `src/agent_runtime/effect_adapters.py:263`
- `src/agent_runtime/journal.py:89`
- `src/agent_runtime/process_resources.py:422`
- `src/tool_execution.py:1946`
- `tests/test_effect_journal_persistence.py:26`
- `tests/test_effect_journal_persistence.py:39`
- `tests/test_effect_journal_persistence.py:53`
- `tests/test_effect_journal_persistence.py:59`
- `tests/test_effect_journal_persistence.py:72`
- `tests/test_effect_journal_persistence.py:77`
- `tests/test_effect_journal_persistence.py:95`
- `tests/test_effect_journal_persistence.py:105`
- `tests/test_effect_journal_persistence.py:118`
- `tests/test_effect_journal_persistence.py:130`
- `tests/test_effect_journal_persistence.py:135`
- `tests/test_effect_journal_persistence.py:163`
- `tests/test_effect_journal_persistence.py:182`
- `tests/test_effect_journal_persistence.py:186`
- `tests/test_effect_journal_persistence.py:193`
- `tests/test_effect_journal_persistence.py:205`
- `tests/test_effect_journal_persistence.py:209`
- `tests/test_effect_journal_persistence.py:220`
- `tests/test_effect_journal_persistence.py:221`
- `tests/test_effect_journal_persistence.py:222`
- `tests/test_effect_journal_persistence.py:237`
- `tests/test_effect_journal_persistence.py:281`
- `tests/test_effect_journal_persistence.py:296`
- `tests/test_effect_journal_persistence.py:353`
- `tests/test_effect_journal_persistence.py:354`
- `tests/test_effect_verification_adapters.py:365`
- `tests/test_effects_foundation.py:189`
- `tests/test_effects_foundation.py:205`
- `tests/test_effects_foundation.py:214`
- `tests/test_effects_foundation.py:227`
- `tests/test_effects_foundation.py:236`
- `tests/test_effects_foundation.py:248`
- `tests/test_effects_foundation.py:256`
- `tests/test_effects_foundation.py:266`
- `tests/test_effects_foundation.py:269`
- `tests/test_effects_foundation.py:280`
- `tests/test_effects_foundation.py:282`
- `tests/test_effects_foundation.py:291`
- `tests/test_effects_foundation.py:294`
- `tests/test_effects_foundation.py:302`
- `tests/test_effects_foundation.py:305`
- `tests/test_effects_foundation.py:314`
- `tests/test_effects_foundation.py:317`
- `tests/test_effects_foundation.py:325`
- `tests/test_effects_foundation.py:339`
- `tests/test_effects_foundation.py:347`
- `tests/test_effects_foundation.py:356`
- `tests/test_effects_foundation.py:367`
- `tests/test_effects_foundation.py:378`
- `tests/test_effects_foundation.py:389`
- `tests/test_effects_foundation.py:400`
- `tests/test_effects_foundation.py:409`
- `tests/test_effects_foundation.py:420`
- `tests/test_effects_foundation.py:434`
- `tests/test_effects_foundation.py:448`
- `tests/test_tool_approvals.py:58`
- … +3 more (grep the name in repo)

## `EffectHistory.latest_outcome` — method, line 655
- **called from:**
- `src/agent_runtime/effect_adapters.py:519`
- `src/agent_runtime/effects.py:662`
- `src/agent_runtime/effects.py:686`
- `src/agent_runtime/effects.py:784`
- `src/agent_runtime/effects.py:821`
- `src/agent_runtime/journal.py:90`
- `tests/test_effect_journal_persistence.py:289`
- `tests/test_effect_journal_persistence.py:290`

## `EffectHistory.execution` — method, line 661
- **called from:**
- `src/agent_runtime/effects.py:702`

## `_claim_touches` — function, line 666
- **called from:**
- `src/agent_runtime/effects.py:684`
- `src/agent_runtime/effects.py:701`

## `invalidated_by` — function, line 670
- **called from:**
- `src/agent_runtime/effects.py:698`
- `tests/test_effects_foundation.py:273`
- `tests/test_effects_foundation.py:296`
- `tests/test_effects_foundation.py:331`
- `tests/test_effects_foundation.py:454`

## `freshness` — function, line 697
- **called from:**
- `src/agent_runtime/effects.py:764`
- `tests/test_effect_verification_adapters.py:251`
- `tests/test_effect_verification_adapters.py:252`
- `tests/test_effect_verification_adapters.py:307`
- `tests/test_effect_verification_adapters.py:339`
- `tests/test_effect_verification_adapters.py:562`
- `tests/test_effects_foundation.py:259`
- `tests/test_effects_foundation.py:333`
- `tests/test_effects_foundation.py:455`

## `EffectVerdict` — class, line 712
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EffectAssessment` — class, line 728
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/effects.py:787`
- `src/agent_runtime/effects.py:792`
- `src/agent_runtime/effects.py:794`
- `src/agent_runtime/effects.py:798`
- `src/agent_runtime/effects.py:804`

## `EffectAssessment.unresolved_impact` — method, line 740
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EffectAssessment.to_dict` — method, line 746
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5624`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28789`
- `src/agent_loop.py:31316`
- `src/agent_loop.py:31789`
- `src/agent_loop.py:32054`
- `src/agent_loop.py:32094`
- `src/agent_loop.py:32125`
- `src/agent_loop.py:32178`
- `src/agent_loop.py:32306`
- `src/agent_loop.py:32638`
- `src/agent_loop.py:34858`
- `src/agent_loop.py:36867`
- `src/agent_loop.py:37190`
- `src/agent_loop.py:37403`
- `src/agent_loop.py:37458`
- `src/agent_loop.py:37515`
- `src/agent_loop.py:37849`
- `src/agent_loop.py:37861`
- `src/agent_loop.py:37967`
- `src/agent_loop.py:38889`
- `src/agent_loop.py:38890`
- `src/agent_loop.py:38895`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:653`
- `src/agent_runtime/authority.py:677`
- `src/agent_runtime/authority.py:677`
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

## `_assess_obligation` — function, line 754
- **called from:**
- `src/agent_runtime/effects.py:799`

## `assess` — function, line 782
- **called from:**
- `src/agent_runtime/effects.py:809`
- `tests/test_effect_journal_persistence.py:63`
- `tests/test_effect_journal_persistence.py:66`
- `tests/test_effect_journal_persistence.py:81`
- `tests/test_effect_journal_persistence.py:85`
- `tests/test_effect_journal_persistence.py:99`
- `tests/test_effect_verification_adapters.py:149`
- `tests/test_effect_verification_adapters.py:157`
- `tests/test_effect_verification_adapters.py:183`
- `tests/test_effects_foundation.py:207`
- `tests/test_effects_foundation.py:217`
- `tests/test_effects_foundation.py:230`
- `tests/test_effects_foundation.py:239`
- `tests/test_effects_foundation.py:241`
- `tests/test_effects_foundation.py:250`
- `tests/test_effects_foundation.py:260`
- `tests/test_effects_foundation.py:274`
- `tests/test_effects_foundation.py:285`
- `tests/test_effects_foundation.py:307`
- `tests/test_effects_foundation.py:308`
- `tests/test_effects_foundation.py:318`
- `tests/test_effects_foundation.py:343`
- `tests/test_effects_foundation.py:350`
- `tests/test_effects_foundation.py:359`
- `tests/test_effects_foundation.py:361`
- `tests/test_effects_foundation.py:370`
- `tests/test_effects_foundation.py:381`
- `tests/test_effects_foundation.py:391`
- `tests/test_effects_foundation.py:394`
- `tests/test_effects_foundation.py:402`
- `tests/test_effects_foundation.py:412`
- `tests/test_effects_foundation.py:423`
- `tests/test_effects_foundation.py:426`
- `tests/test_effects_foundation.py:428`
- `tests/test_effects_foundation.py:435`
- `tests/test_effects_foundation.py:440`
- `tests/test_effects_foundation.py:457`

## `assess_all` — function, line 808
- **called from:**
- `src/agent_runtime/effect_log.py:383`

## `replay_interrupted` — function, line 812
- **called from:**
- `src/agent_runtime/effect_log.py:504`
- `tests/test_effects_foundation.py:436`
- `tests/test_effects_foundation.py:441`
