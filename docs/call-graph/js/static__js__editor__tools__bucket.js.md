# `static/js/editor/tools/bucket.js` — definitions & call sites

9 definitions (regex-based, best-effort).
**Exports:** `createBucketTool`, `floodFillImageData`, `hexToRgb`

## `hexToRgb` — function, line 12
- **called from:**
- `static/js/color/hex.js:8`
- `static/js/colorPicker.js:21`
- `static/js/colorPicker.js:71`
- `static/js/editor/filters/effects.js:480`
- `static/js/editor/filters/effects.js:495`
- `static/js/editor/filters/effects.js:496`
- `static/js/editor/tools/bucket.js:12`
- `static/js/editor/tools/bucket.js:119`
- `static/js/editor/tools/color-range.js:3`
- `static/js/theme.js:170`
- `static/js/theme.js:2114`
- `static/js/theme.js:2370`

## `matches` — function, line 20
- **called from:**
- `src/agent_loop.py:25951`
- `src/model_capabilities.py:903`
- `src/tool_execution.py:1773`
- `tests/test_calendar_cli_overlap.py:85`
- `tests/test_foreground_model_routing.py:357`
- `tests/test_owned_resource_identity.py:364`
- `tests/test_request_authority.py:291`
- `tests/test_resource_identity.py:579`
- `tests/test_resource_identity.py:693`
- `tests/test_tool_approval_task_scope.py:226`
- `static/js/a11y.js:136`
- `static/js/a11y.js:147`
- `static/js/a11y.js:195`
- `static/js/a11y.js:212`
- `static/js/calendar.js:1502`
- `static/js/document.js:5905`
- `static/js/document.js:7885`
- `static/js/document.js:8401`
- `static/js/document.js:9832`
- `static/js/dragSort.js:50`
- `static/js/dragSort.js:175`
- `static/js/dragSort.js:227`
- `static/js/dragSort.js:289`
- `static/js/editor/control-kit.js:145`
- `static/js/editor/control-kit.js:146`
- `static/js/editor/control-kit.js:147`
- `static/js/editor/control-kit.js:148`
- `static/js/editor/control-kit.js:177`
- `static/js/editor/control-kit.js:186`
- `static/js/editor/layer-panel.js:319`
- `static/js/editor/layer-panel.js:340`
- `static/js/editor/layer-style-menu.js:29`
- `static/js/editor/panel-visibility.js:98`
- `static/js/editor/slider-ux.js:97`
- `static/js/editor/tools/bucket.js:20`
- `static/js/editor/tools/bucket.js:62`
- `static/js/editor/wire-extra-menus.js:45`
- `static/js/editor/wire-topbar-overflow.js:66`
- `static/js/editor/wire-topbar-overflow.js:69`
- `static/js/editor/wire-topbar-overflow.js:80`
- `static/js/emailLibrary/index.js:3911`
- `static/js/galleryEditor.js:6345`
- `static/js/galleryEditor.js:6350`
- `static/js/galleryEditor.js:11015`
- `static/js/galleryEditor.js:11018`
- `static/js/mobileBulkSelect.js:13`
- `static/js/mobileBulkSelect.js:14`
- `static/js/mobileBulkSelect.js:19`
- `static/js/mobileBulkSelect.js:24`
- `static/js/turnRendering.js:81`
- `static/js/turnRendering.js:88`
- `static/js/ui.js:223`

## `floodFillImageData` — function, line 41
- **called from:**
- `static/js/editor/tools/bucket.js:41`
- `static/js/editor/tools/bucket.js:117`

## `eligible` — arrow, line 57
- **called from:**
- `static/js/editor/tools/bucket.js:38`
- `static/js/editor/tools/bucket.js:70`
- `static/js/editor/tools/bucket.js:74`
- `static/js/editor/tools/bucket.js:83`
- `static/js/editor/tools/bucket.js:88`

## `createBucketTool` — function, line 98
- **called from:**
- `static/js/editor/tools/bucket.js:98`
- `static/js/galleryEditor.js:7123`

## `maskFor` — function, line 99
- **called from:**
- `static/js/editor/tools/bucket.js:99`
- `static/js/editor/tools/bucket.js:119`

## `fillAtPoint` — function, line 110
- **called from:**
- `static/js/editor/tools/bucket.js:110`
- `static/js/editor/tools/bucket.js:153`
- `static/js/galleryEditor.js:12643`

## `paintableLayer` — function, line 133
- **called from:**
- `static/js/editor/tools/bucket.js:133`
- `static/js/editor/tools/bucket.js:144`

## `fill` — function, line 143
- **called from:**
- `static/js/compare/index.js:1077`
- `static/js/compare/index.js:1078`
- `static/js/compare/index.js:1079`
- `static/js/compare/panes.js:1141`
- `static/js/cookbookServe.js:1607`
- `static/js/document.js:14006`
- `static/js/editor/ai-rembg.js:203`
- `static/js/editor/filters/edge-feather.js:19`
- `static/js/editor/filters/effects.js:593`
- `static/js/editor/filters/effects.js:593`
- `static/js/editor/filters/effects.js:593`
- `static/js/editor/filters/effects.js:593`
- `static/js/editor/fx/adj-popup.js:1069`
- `static/js/editor/panels/studio-panels.js:104`
- `static/js/editor/select-and-mask.js:148`
- `static/js/editor/selection-mask.js:101`
- `static/js/editor/selection-mask.js:305`
- `static/js/editor/selection-mask.js:306`
- `static/js/editor/shape-layer.js:139`
- `static/js/editor/stroke-pipeline.js:65`
- `static/js/editor/tools/bucket.js:143`
- `static/js/editor/tools/lasso-mask.js:50`
- `static/js/editor/tools/lasso-mask.js:86`
- `static/js/editor/tools/lasso-mask.js:123`
- `static/js/editor/tools/lasso.js:127`
- `static/js/editor/tools/pen-selection.js:33`
- `static/js/editor/tools/pen-selection.js:123`
- `static/js/editor/tools/transform-handles.js:254`
- `static/js/galleryEditor.js:5588`
- `static/js/galleryEditor.js:6825`
- `static/js/galleryEditor.js:7247`
- `static/js/galleryEditor.js:7817`
- `static/js/galleryEditor.js:11982`
- `static/js/galleryEditor.js:12641`
- `static/js/researchSynapse.js:105`
- `static/js/researchSynapse.js:114`
- `static/js/researchSynapse.js:136`
- `static/js/researchSynapse.js:154`
- `static/js/researchSynapse.js:159`
- `static/js/slashCommands.js:6280`
- `static/js/spinner.js:132`
- `static/js/spinner.js:239`
- `static/js/theme.js:476`
- `static/js/theme.js:495`
- `static/js/theme.js:1843`
- `static/js/theme.js:2017`
- `static/js/theme.js:2083`
- `static/js/theme.js:2132`
- `static/js/theme.js:2192`
- `static/js/theme.js:2259`
- `static/js/theme.js:2261`
- `static/js/theme.js:2304`
- `static/js/theme.js:2413`
