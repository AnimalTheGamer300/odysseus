# `static/js/editor/effects.js` — definitions & call sites

15 definitions (regex-based, best-effort).
**Exports:** `EFFECT_PRESETS`, `EFFECT_TYPES_LIST`, `defaultEffectParams`, `effectLabel`, `effectPreset`, `effectsWithPreview`, `normalizeEffect`, `renderEffects`, `renderEffectsAsync`

## `effectsWithPreview` — function, line 4
- **called from:**
- `static/js/editor/effects.js:4`

## `clone` — function, line 22
- **called from:**
- `static/js/calendar.js:3319`
- `static/js/editor/adjustment-layer.js:29`
- `static/js/editor/adjustment-layer.js:37`
- `static/js/editor/adjustment-layer.js:37`
- `static/js/editor/adjustment-layer.js:38`
- `static/js/editor/adjustment-layer.js:41`
- `static/js/editor/adjustment-layer.js:45`
- `static/js/editor/adjustment-layer.js:50`
- `static/js/editor/adjustment-layer.js:56`
- `static/js/editor/adjustment-layer.js:60`
- `static/js/editor/adjustment-layer.js:65`
- `static/js/editor/effects.js:22`
- `static/js/editor/effects.js:60`
- `static/js/editor/effects.js:67`
- `static/js/editor/effects.js:109`
- `static/sw.js:408`
- `static/sw.js:422`
- `static/sw.js:437`

## `normalizeEffectMask` — function, line 26
- **called from:**
- `static/js/editor/effects.js:26`
- `static/js/editor/effects.js:117`

## `defaultEffectParams` — function, line 40
- **called from:**
- `static/js/editor/effects.js:40`
- `static/js/editor/effects.js:65`

## `effectPreset` — function, line 58
- **called from:**
- `static/js/editor/effects.js:58`

## `normalizeEffect` — function, line 63
- **called from:**
- `static/js/editor/document-codec.js:622`
- `static/js/editor/effects.js:63`
- `static/js/editor/effects.js:212`
- `static/js/editor/effects.js:347`
- `static/js/editor/layer-panel.js:117`
- `static/js/editor/layer-panel.js:976`
- `static/js/editor/layer-panel.js:1583`
- `static/js/editor/layer-panel.js:1931`

## `effectLabel` — function, line 122
- **called from:**
- `static/js/editor/effects.js:114`
- `static/js/editor/effects.js:122`
- `static/js/editor/layer-panel.js:158`
- `static/js/editor/layer-panel.js:182`
- `static/js/editor/layer-panel.js:187`
- `static/js/editor/layer-panel.js:989`
- `static/js/editor/layer-panel.js:998`
- `static/js/editor/layer-panel.js:1018`
- `static/js/editor/layer-panel.js:1039`
- `static/js/editor/layer-panel.js:1053`
- `static/js/editor/layer-panel.js:1937`
- `static/js/editor/layer-panel.js:1944`
- `static/js/editor/layer-panel.js:1952`
- `static/js/editor/layer-panel.js:1974`
- `static/js/editor/layer-panel.js:1996`
- `static/js/editor/layer-panel.js:2010`
- `static/js/editor/layer-panel.js:2038`
- `static/js/editor/layer-panel.js:2052`

## `copyCanvas` — function, line 138
- **called from:**
- `static/js/editor/effects-worker.js:4`
- `static/js/editor/effects-worker.js:11`
- `static/js/editor/effects-worker.js:54`
- `static/js/editor/effects-worker.js:133`
- `static/js/editor/effects.js:138`
- `static/js/editor/effects.js:179`
- `static/js/editor/effects.js:209`
- `static/js/editor/effects.js:293`
- `static/js/editor/placed-layer.js:81`
- `static/js/editor/placed-layer.js:93`
- `static/js/editor/placed-layer.js:104`
- `static/js/editor/tools/transform-session.js:105`
- `static/js/editor/tools/transform-session.js:130`
- `static/js/editor/tools/transform-session.js:148`
- `static/js/editor/tools/transform-session.js:214`

## `gradientColor` — function, line 146
- **called from:**
- `static/js/editor/effects-worker.js:46`
- `static/js/editor/effects-worker.js:122`
- `static/js/editor/effects.js:146`
- `static/js/editor/effects.js:158`

## `renderGradient` — function, line 153
- **called from:**
- `static/js/editor/effects.js:153`
- `static/js/editor/effects.js:287`

## `applyEffectMask` — function, line 165
- **called from:**
- `static/js/editor/effects.js:165`
- `static/js/editor/effects.js:291`

## `sharpenCanvas` — function, line 178
- **called from:**
- `static/js/editor/effects-worker.js:10`
- `static/js/editor/effects-worker.js:67`
- `static/js/editor/effects.js:178`
- `static/js/editor/effects.js:225`

## `renderEffects` — function, line 207
- **called from:**
- `static/js/editor/effects-worker.js:53`
- `static/js/editor/effects-worker.js:147`
- `static/js/editor/effects.js:207`
- `static/js/editor/effects.js:311`
- `static/js/editor/effects.js:331`
- `static/js/editor/effects.js:344`
- `static/js/editor/effects.js:364`
- `static/js/editor/effects.js:376`
- `static/js/editor/layer-groups.js:387`

## `renderEffectsAsync` — function, line 308
- **called from:**
- `static/js/editor/effects.js:308`
- `static/js/editor/layer-groups.js:496`

## `finish` — arrow, line 352
- **called from:**
- `src/agent_loop.py:33038`
- `src/agent_loop.py:33051`
- `src/agent_loop.py:33059`
- `src/agent_loop.py:34919`
- `src/agent_runtime/journal.py:267`
- `src/agent_runtime/journal.py:269`
- `src/containment.py:1512`
- `src/containment.py:1518`
- `src/containment.py:1527`
- `src/containment.py:1542`
- `src/containment.py:1545`
- `src/pdf_forms.py:338`
- `tests/test_effect_verification_adapters.py:55`
- `tests/test_effect_verification_adapters.py:121`
- `tests/test_effect_verification_adapters.py:215`
- `tests/test_effect_verification_adapters.py:431`
- `static/js/calendar.js:34`
- `static/js/calendar.js:42`
- `static/js/calendar.js:43`
- `static/js/calendar.js:45`
- `static/js/chat.js:2122`
- `static/js/colorPicker.js:237`
- `static/js/colorPicker.js:243`
- `static/js/editor/adjustment-layer.js:205`
- `static/js/editor/adjustment-layer.js:211`
- `static/js/editor/adjustment-layer.js:215`
- `static/js/editor/ai-inpaint.js:280`
- `static/js/editor/ai-operation.js:19`
- `static/js/editor/ai-tool-runner.js:164`
- `static/js/editor/ai-tools-misc.js:157`
- `static/js/editor/ai-tools-misc.js:206`
- `static/js/editor/effects.js:364`
- `static/js/editor/effects.js:372`
- `static/js/editor/effects.js:376`
- `static/js/editor/layer-panel.js:1424`
- `static/js/editor/layer-panel.js:1426`
- `static/js/editor/layer-panel.js:1431`
- `static/js/editor/precision-guides.js:210`
- `static/js/editor/precision-guides.js:229`
- `static/js/editor/tools/pen-path.js:39`
- `static/js/editor/tools/pen-path.js:46`
- `static/js/features/notes/ui/cardInteractions.js:234`
- `static/js/features/notes/ui/cardInteractions.js:238`
- `static/js/features/notes/ui/colors.js:63`
- `static/js/features/notes/ui/colors.js:71`
- `static/js/features/notes/ui/colors.js:72`
- `static/js/features/notes/ui/colors.js:75`
- `static/js/fileHandler.js:96`
- `static/js/fileHandler.js:134`
- `static/js/fileHandler.js:135`
- `static/js/fileHandler.js:172`
- `static/js/fileHandler.js:175`
- `static/js/gallery.js:2484`
- `static/js/gallery.js:2487`
- `static/js/galleryEditor.js:430`
- `static/js/galleryEditor.js:4572`
- `static/js/galleryEditor.js:4573`
- `static/js/galleryEditor.js:4575`
- `static/js/galleryEditor.js:4655`
- `static/js/galleryEditor.js:4659`
- … +4 more (grep the name in repo)
