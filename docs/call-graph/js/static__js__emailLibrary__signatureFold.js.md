# `static/js/emailLibrary/signatureFold.js` — definitions & call sites

11 definitions (regex-based, best-effort).
**Exports:** `_QUOTE_ICON`, `_SIG_ICON`, `_extractQuoteMeta`, `_extractTurnMetaFromBlockquote`, `_foldSignature`, `_foldSummary`, `_harvestAttribution`, `_isBloatedSig`, `_looksLikeSignature`, `_peelSigNameLine`, `_tryFoldHintSig`

## `_esc` — function, line 25
- **called from:**
- `tests/test_ics_escape.py:12`
- `tests/test_ics_escape.py:16`
- `tests/test_ics_escape.py:20`
- `tests/test_ics_escape.py:24`
- `tests/test_ics_escape.py:25`
- `static/js/assistant.js:115`
- `static/js/assistant.js:144`
- `static/js/assistant.js:144`
- `static/js/assistant.js:147`
- `static/js/assistant.js:150`
- `static/js/assistant.js:151`
- `static/js/assistant.js:154`
- `static/js/assistant.js:156`
- `static/js/assistant.js:157`
- `static/js/assistant.js:165`
- `static/js/assistant.js:169`
- `static/js/assistant.js:169`
- `static/js/assistant.js:178`
- `static/js/assistant.js:186`
- `static/js/assistant.js:207`
- `static/js/assistant.js:207`
- `static/js/assistant.js:241`
- `static/js/assistant.js:241`
- `static/js/assistant.js:257`
- `static/js/assistant.js:257`
- `static/js/assistant.js:302`
- `static/js/assistant.js:302`
- `static/js/assistant.js:311`
- `static/js/assistant.js:311`
- `static/js/chat.js:6293`
- `static/js/chat.js:6293`
- `static/js/cookbookServe.js:4108`
- `static/js/cookbookServe.js:4110`
- `static/js/document.js:1225`
- `static/js/document.js:1226`
- `static/js/document.js:13760`
- `static/js/document.js:14380`
- `static/js/document.js:15402`
- `static/js/documentLibrary.js:169`
- `static/js/documentLibrary.js:185`
- `static/js/documentLibrary.js:705`
- `static/js/documentLibrary.js:709`
- `static/js/documentLibrary.js:711`
- `static/js/documentLibrary.js:2218`
- `static/js/documentLibrary.js:2223`
- `static/js/documentLibrary.js:2371`
- `static/js/documentLibrary.js:2735`
- `static/js/documentLibrary.js:2780`
- `static/js/documentLibrary.js:2818`
- `static/js/documentLibrary.js:2968`
- `static/js/documentLibrary.js:3017`
- `static/js/documentLibrary.js:3030`
- `static/js/documentLibrary.js:3184`
- `static/js/emailInbox.js:76`
- `static/js/emailInbox.js:76`
- `static/js/emailInbox.js:76`
- `static/js/emailInbox.js:78`
- `static/js/emailInbox.js:78`
- `static/js/emailInbox.js:78`
- `static/js/emailInbox.js:78`
- … +226 more (grep the name in repo)

## `_looksLikeSignature` — function, line 35
- **called from:**
- `static/js/emailLibrary/bodyRender.js:656`
- `static/js/emailLibrary/signatureFold.js:35`

## `_harvestAttribution` — function, line 66
- **called from:**
- `static/js/emailLibrary/bodyRender.js:639`
- `static/js/emailLibrary/signatureFold.js:66`

## `_extractTurnMetaFromBlockquote` — function, line 91
- **called from:**
- `static/js/emailLibrary/bodyRender.js:647`
- `static/js/emailLibrary/signatureFold.js:91`

## `_foldSummary` — function, line 100
- **called from:**
- `static/js/emailLibrary/bodyRender.js:154`
- `static/js/emailLibrary/bodyRender.js:160`
- `static/js/emailLibrary/bodyRender.js:553`
- `static/js/emailLibrary/bodyRender.js:659`
- `static/js/emailLibrary/bodyRender.js:674`
- `static/js/emailLibrary/bodyRender.js:766`
- `static/js/emailLibrary/bodyRender.js:834`
- `static/js/emailLibrary/bodyRender.js:867`
- `static/js/emailLibrary/signatureFold.js:100`
- `static/js/emailLibrary/signatureFold.js:278`
- `static/js/emailLibrary/signatureFold.js:295`
- `static/js/emailLibrary/signatureFold.js:322`

## `_extractQuoteMeta` — function, line 135
- **called from:**
- `static/js/emailLibrary/bodyRender.js:154`
- `static/js/emailLibrary/bodyRender.js:647`
- `static/js/emailLibrary/bodyRender.js:747`
- `static/js/emailLibrary/bodyRender.js:834`
- `static/js/emailLibrary/bodyRender.js:867`
- `static/js/emailLibrary/signatureFold.js:84`
- `static/js/emailLibrary/signatureFold.js:93`
- `static/js/emailLibrary/signatureFold.js:135`

## `_peelSigNameLine` — function, line 183
- **called from:**
- `static/js/emailLibrary/signatureFold.js:183`
- `static/js/emailLibrary/signatureFold.js:319`

## `_isBloatedSig` — function, line 214
- **called from:**
- `static/js/emailLibrary/bodyRender.js:159`
- `static/js/emailLibrary/signatureFold.js:214`
- `static/js/emailLibrary/signatureFold.js:276`
- `static/js/emailLibrary/signatureFold.js:293`
- `static/js/emailLibrary/signatureFold.js:320`

## `_tryFoldHintSig` — function, line 231
- **called from:**
- `static/js/emailLibrary/signatureFold.js:231`
- `static/js/emailLibrary/signatureFold.js:289`

## `_foldSignature` — function, line 285
- **called from:**
- `static/js/emailLibrary/bodyRender.js:90`
- `static/js/emailLibrary/bodyRender.js:92`
- `static/js/emailLibrary/bodyRender.js:108`
- `static/js/emailLibrary/bodyRender.js:115`
- `static/js/emailLibrary/bodyRender.js:177`
- `static/js/emailLibrary/bodyRender.js:181`
- `static/js/emailLibrary/bodyRender.js:182`
- `static/js/emailLibrary/signatureFold.js:285`

## `wrap` — arrow, line 292
- **called from:**
- `tests/smoke/areas.py:167`
- `static/js/emailLibrary/bodyRender.js:561`
- `static/js/emailLibrary/bodyRender.js:568`
- `static/js/emailLibrary/bodyRender.js:583`
- `static/js/emailLibrary/signatureFold.js:299`
- `static/js/emailLibrary/signatureFold.js:301`
- `static/js/emailLibrary/signatureFold.js:303`
- `static/js/emailLibrary/signatureFold.js:308`
- `static/js/emailLibrary/signatureFold.js:329`
- `static/js/emailLibrary/signatureFold.js:335`
- `static/js/tasks.js:1248`
- `static/js/tasks.js:1249`
- `static/js/tasks.js:1250`
- `static/js/tasks.js:1251`
- `static/js/tasks.js:1252`
