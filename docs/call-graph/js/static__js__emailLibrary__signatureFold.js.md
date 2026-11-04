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
- `static/js/chat.js:4679`
- `static/js/chat.js:4679`
- `static/js/cookbookServe.js:4003`
- `static/js/cookbookServe.js:4005`
- `static/js/document.js:313`
- `static/js/document.js:314`
- `static/js/document.js:8382`
- `static/js/document.js:8966`
- `static/js/documentLibrary.js:70`
- `static/js/documentLibrary.js:86`
- `static/js/documentLibrary.js:582`
- `static/js/documentLibrary.js:586`
- `static/js/documentLibrary.js:588`
- `static/js/documentLibrary.js:1957`
- `static/js/documentLibrary.js:1962`
- `static/js/documentLibrary.js:2110`
- `static/js/documentLibrary.js:2466`
- `static/js/documentLibrary.js:2510`
- `static/js/documentLibrary.js:2547`
- `static/js/documentLibrary.js:2696`
- `static/js/documentLibrary.js:2737`
- `static/js/documentLibrary.js:2750`
- `static/js/documentLibrary.js:2904`
- `static/js/emailInbox.js:75`
- `static/js/emailInbox.js:75`
- `static/js/emailInbox.js:75`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:77`
- `static/js/emailInbox.js:524`
- … +188 more (grep the name in repo)

## `_looksLikeSignature` — function, line 35
- **called from:**
- `static/js/emailLibrary.js:6297`
- `static/js/emailLibrary/signatureFold.js:35`

## `_harvestAttribution` — function, line 66
- **called from:**
- `static/js/emailLibrary.js:6280`
- `static/js/emailLibrary/signatureFold.js:66`

## `_extractTurnMetaFromBlockquote` — function, line 91
- **called from:**
- `static/js/emailLibrary.js:6288`
- `static/js/emailLibrary/signatureFold.js:91`

## `_foldSummary` — function, line 100
- **called from:**
- `static/js/emailLibrary.js:5809`
- `static/js/emailLibrary.js:5815`
- `static/js/emailLibrary.js:6194`
- `static/js/emailLibrary.js:6300`
- `static/js/emailLibrary.js:6315`
- `static/js/emailLibrary.js:6407`
- `static/js/emailLibrary.js:6475`
- `static/js/emailLibrary.js:6508`
- `static/js/emailLibrary/signatureFold.js:100`
- `static/js/emailLibrary/signatureFold.js:278`
- `static/js/emailLibrary/signatureFold.js:295`
- `static/js/emailLibrary/signatureFold.js:322`

## `_extractQuoteMeta` — function, line 135
- **called from:**
- `static/js/emailLibrary.js:5809`
- `static/js/emailLibrary.js:6288`
- `static/js/emailLibrary.js:6388`
- `static/js/emailLibrary.js:6475`
- `static/js/emailLibrary.js:6508`
- `static/js/emailLibrary/signatureFold.js:84`
- `static/js/emailLibrary/signatureFold.js:93`
- `static/js/emailLibrary/signatureFold.js:135`

## `_peelSigNameLine` — function, line 183
- **called from:**
- `static/js/emailLibrary/signatureFold.js:183`
- `static/js/emailLibrary/signatureFold.js:319`

## `_isBloatedSig` — function, line 214
- **called from:**
- `static/js/emailLibrary.js:5814`
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
- `static/js/emailLibrary.js:5761`
- `static/js/emailLibrary.js:5763`
- `static/js/emailLibrary.js:5770`
- `static/js/emailLibrary.js:5832`
- `static/js/emailLibrary.js:5836`
- `static/js/emailLibrary.js:5837`
- `static/js/emailLibrary/signatureFold.js:285`

## `wrap` — arrow, line 292
- **called from:**
- `static/js/emailLibrary.js:6202`
- `static/js/emailLibrary.js:6209`
- `static/js/emailLibrary.js:6224`
- `static/js/emailLibrary/signatureFold.js:299`
- `static/js/emailLibrary/signatureFold.js:301`
- `static/js/emailLibrary/signatureFold.js:303`
- `static/js/emailLibrary/signatureFold.js:308`
- `static/js/emailLibrary/signatureFold.js:329`
- `static/js/emailLibrary/signatureFold.js:335`
- `static/js/tasks.js:1151`
- `static/js/tasks.js:1152`
- `static/js/tasks.js:1153`
- `static/js/tasks.js:1154`
- `static/js/tasks.js:1155`
