# `static/js/editor/render-cancellation.js` — definitions & call sites

3 definitions (regex-based, best-effort).
**Exports:** `createRenderGeneration`

## `createRenderGeneration` — function, line 2
- **called from:**
- `static/js/editor/render-cancellation.js:2`

## `begin` — method?, line 5
- **called from:**
- `core/database.py:1399`
- `core/database.py:1517`
- `core/database.py:2249`
- `core/database.py:2375`
- `tests/test_chatgpt_session_binding.py:151`
- `tests/test_chatgpt_session_binding.py:157`
- `tests/test_cookbook_endpoint_registration.py:303`
- `tests/test_email_account_default_serialization.py:241`
- `tests/test_email_account_default_serialization.py:278`
- `tests/test_request_authority.py:375`
- `static/js/editor/brush-engine.js:62`
- `static/js/editor/direct-manipulation-session.js:24`
- `static/js/editor/render-cancellation.js:5`
- `static/js/editor/stroke-pipeline.js:390`
- `static/js/editor/tools/clone.js:7`
- `static/js/editor/tools/clone.js:25`
- `static/js/editor/tools/crop.js:51`
- `static/js/editor/tools/crop.js:61`
- `static/js/editor/tools/crop.js:72`
- `static/js/editor/tools/gradient.js:58`
- `static/js/editor/tools/lasso.js:84`
- `static/js/editor/tools/liquify.js:141`
- `static/js/editor/tools/marquee.js:51`
- `static/js/editor/tools/marquee.js:61`
- `static/js/editor/tools/marquee.js:80`
- `static/js/editor/tools/move.js:47`
- `static/js/editor/tools/patch.js:6`
- `static/js/editor/tools/pen-path.js:37`
- `static/js/editor/tools/pen-selection.js:50`
- `static/js/editor/tools/stroke.js:16`
- `static/js/editor/tools/transform-drag.js:75`
- `static/js/editor/tools/transform-drag.js:86`
- `static/js/galleryEditor.js:4016`
- `static/js/galleryEditor.js:5572`
- `static/js/galleryEditor.js:5573`
- `static/js/galleryEditor.js:5574`
- `static/js/galleryEditor.js:5575`
- `static/js/galleryEditor.js:5590`
- `static/js/galleryEditor.js:5591`
- `static/js/galleryEditor.js:5592`
- `static/js/galleryEditor.js:5596`
- `static/js/galleryEditor.js:5597`
- `static/js/galleryEditor.js:7164`
- `static/js/windowResize.js:124`
- `static/js/windowResize.js:197`

## `invalidate` — method?, line 13
- **called from:**
- `companion/routes.py:78`
- `routes/chatgpt_subscription_routes.py:212`
- `routes/model_routes.py:706`
- `src/agent_tools/web_tools.py:2710`
- `src/browser_identity.py:415`
- `src/browser_identity.py:469`
- `src/browser_identity.py:479`
- `src/browser_identity.py:597`
- `src/browser_identity.py:646`
- `src/chatgpt_subscription.py:772`
- `static/js/editor/render-cancellation.js:13`
- `static/js/galleryEditor.js:4011`
- `static/js/galleryEditor.js:14218`
