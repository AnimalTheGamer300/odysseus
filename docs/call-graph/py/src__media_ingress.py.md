# `src/media_ingress.py` — definitions & call sites

23 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `MediaIngressLimits` — class, line 38
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/media_ingress.py:107`
- `src/media_ingress.py:118`
- `tests/test_media_ingress.py:31`
- `tests/test_media_ingress.py:77`
- `tests/test_media_ingress.py:115`
- `tests/test_media_ingress.py:146`

## `LocalMediaAttachment` — class, line 54
- decorator: `dataclass(frozen=True)`
- **called from:**
- `tests/test_media_ingress.py:30`
- `tests/test_media_ingress.py:57`
- `tests/test_media_ingress.py:74`
- `tests/test_media_ingress.py:75`
- `tests/test_media_ingress.py:114`
- `tests/test_media_ingress.py:131`
- `tests/test_media_ingress.py:145`
- `tests/test_media_ingress.py:166`
- `tests/test_media_ingress.py:181`

## `MediaArtifact` — class, line 60
- decorator: `dataclass`
- **called from:**
- `src/media_ingress.py:336`
- `src/media_ingress.py:367`
- `src/media_ingress.py:381`
- `src/media_ingress.py:406`

## `MediaArtifact.to_dict` — method, line 74
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

## `MediaIngressResult` — class, line 79
- decorator: `dataclass`
- **called from:**
- `src/media_ingress.py:290`

## `MediaIngressResult.estimated_visual_tokens` — method, line 85
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `MediaIngressResult.metadata` — method, line 88
- **called from:**
- `routes/chat_routes.py:230`
- `routes/chat_routes.py:5205`
- `routes/chat_routes.py:5249`
- `routes/chat_routes.py:5335`
- `tests/test_agent_render_ownership.py:26`
- `tests/test_agent_render_ownership.py:36`
- `tests/test_agent_render_ownership.py:52`
- `tests/test_agent_render_ownership.py:76`
- `tests/test_agent_render_ownership.py:84`
- `tests/test_media_ingress.py:46`
- `tests/test_media_ingress.py:157`
- `tests/test_nested_invocation_ownership.py:85`
- `tests/test_nested_invocation_ownership.py:86`
- `tests/test_nested_invocation_ownership.py:130`
- `tests/test_nested_invocation_ownership.py:130`
- `tests/test_nested_invocation_ownership.py:292`
- `tests/test_nested_invocation_ownership.py:302`
- `tests/test_nested_invocation_ownership.py:303`
- `tests/test_nested_invocation_ownership.py:304`
- `tests/test_nested_invocation_ownership.py:306`
- `tests/test_nested_invocation_ownership.py:544`
- `static/js/chatRenderer.js:3643`
- `static/js/fileHandler.js:461`

## `is_supported_media_path` — function, line 96
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `is_supported_attachment_path` — function, line 100
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `limits_from_env` — function, line 104
- **called from:**
- `src/media_ingress.py:284`

## `value` — function, line 109
- **called from:**
- `src/media_ingress.py:119`
- `src/media_ingress.py:120`
- `src/media_ingress.py:123`
- `src/media_ingress.py:126`
- `src/media_ingress.py:129`
- `src/media_ingress.py:132`
- `src/media_ingress.py:135`
- `src/media_ingress.py:138`
- `src/media_ingress.py:139`
- `src/media_ingress.py:140`
- `src/media_ingress.py:143`
- `src/media_ingress.py:146`
- `static/js/cookbook-hwfit.js:257`
- `static/js/editor/ai-models.js:18`
- `static/js/galleryEditor.js:358`
- `static/js/galleryEditor.js:8471`
- `static/js/skills.js:588`
- `static/js/tasks.js:1684`

## `_regular_file_size` — function, line 152
- **called from:**
- `src/media_ingress.py:298`

## `_sha256` — function, line 161
- **called from:**
- `src/media_ingress.py:312`
- `tests/test_audit_c5_benchmark_evidence.py:42`
- `tests/test_audit_c5_benchmark_evidence.py:110`
- `tests/test_audit_c5_benchmark_evidence.py:345`
- `tests/test_audit_c5_benchmark_evidence.py:940`
- `tests/test_audit_c5_benchmark_evidence.py:1177`

## `_visual_token_estimate` — function, line 169
- **called from:**
- `src/media_ingress.py:389`
- `src/media_ingress.py:444`

## `_normalize_image` — function, line 175
- **called from:**
- `src/media_ingress.py:377`
- `src/media_ingress.py:420`

## `_data_uri` — function, line 193
- **called from:**
- `src/media_ingress.py:397`
- `src/media_ingress.py:437`

## `_audio_data_uri` — function, line 198
- **called from:**
- `src/media_ingress.py:364`

## `_base64_size` — function, line 205
- **called from:**
- `src/media_ingress.py:349`
- `src/media_ingress.py:378`
- `src/media_ingress.py:421`

## `_timestamp_label` — function, line 209
- **called from:**
- `src/media_ingress.py:433`

## `_probe_video` — function, line 214
- **called from:**
- `src/media_ingress.py:404`

## `_uniform_timestamps` — function, line 240
- **called from:**
- `src/media_ingress.py:405`
- `tests/test_media_ingress.py:86`

## `_extract_video_frame` — function, line 245
- **called from:**
- `src/media_ingress.py:419`

## `build_multimodal_user_content` — function, line 275
- **called from:**
- `tests/test_media_ingress.py:28`
- `tests/test_media_ingress.py:55`
- `tests/test_media_ingress.py:71`
- `tests/test_media_ingress.py:112`
- `tests/test_media_ingress.py:129`
- `tests/test_media_ingress.py:143`
- `tests/test_media_ingress.py:164`
- `tests/test_media_ingress.py:179`
