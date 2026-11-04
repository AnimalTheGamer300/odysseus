# `static/js/emailLibrary/utils.js` — definitions & call sites

16 definitions (regex-based, best-effort).
**Exports:** `_SIG_BLOAT_MIN_CHARS`, `_TALON_FROM`, `_TALON_ORIG_RE`, `_TALON_SENT`, `_TALON_SUBJ`, `_TALON_TO`, `_TALON_WROTE`, `_emailSummaryErrorMessage`, `_esc`, `_escLinkify`, `_extractName`, `_formatBubbleDate`, `_formatRecipients`, `_initials`, `_parseTurnMeta`, `_renderEmailSummaryError`, `_sanitizeHtml`, `_senderColor`

## `_esc` — function, line 27
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

## `_emailSummaryErrorMessage` — function, line 40
- **called from:**
- `static/js/emailLibrary/utils.js:40`
- `static/js/emailLibrary/utils.js:48`

## `_renderEmailSummaryError` — function, line 45
- **called from:**
- `static/js/emailLibrary.js:7529`
- `static/js/emailLibrary.js:7533`
- `static/js/emailLibrary/utils.js:45`

## `_attrEsc` — function, line 52
- **called from:**
- `static/js/emailLibrary/utils.js:52`
- `static/js/emailLibrary/utils.js:83`
- `static/js/emailLibrary/utils.js:85`
- `static/js/notes.js:495`
- `static/js/notes.js:527`
- `static/js/notes.js:1857`
- `static/js/notes.js:1863`
- `static/js/notes.js:1863`
- `static/js/notes.js:1863`

## `_compactUrlSchemeValue` — function, line 61
- **called from:**
- `static/js/emailLibrary/utils.js:61`
- `static/js/emailLibrary/utils.js:66`
- `static/js/emailLibrary/utils.js:216`
- `static/js/markdown.js:207`
- `static/js/markdown.js:212`
- `static/js/markdown.js:239`

## `_isDangerousUrl` — function, line 65
- **called from:**
- `static/js/emailLibrary/utils.js:65`
- `static/js/emailLibrary/utils.js:71`
- `static/js/emailLibrary/utils.js:199`
- `static/js/markdown.js:211`
- `static/js/markdown.js:216`
- `static/js/markdown.js:248`

## `_isDangerousSrcset` — function, line 70
- **called from:**
- `static/js/emailLibrary/utils.js:70`
- `static/js/emailLibrary/utils.js:199`
- `static/js/markdown.js:215`
- `static/js/markdown.js:248`

## `_escLinkify` — function, line 75
- **called from:**
- `static/js/emailLibrary.js:5763`
- `static/js/emailLibrary.js:5805`
- `static/js/emailLibrary.js:5833`
- `static/js/emailLibrary.js:5846`
- `static/js/emailLibrary.js:6402`
- `static/js/emailLibrary/utils.js:75`

## `_extractName` — function, line 90
- **called from:**
- `static/js/emailLibrary.js:5553`
- `static/js/emailLibrary.js:7187`
- `static/js/emailLibrary.js:7335`
- `static/js/emailLibrary.js:8713`
- `static/js/emailLibrary/utils.js:90`

## `_parseTurnMeta` — function, line 99
- **called from:**
- `static/js/emailLibrary.js:6110`
- `static/js/emailLibrary.js:6150`
- `static/js/emailLibrary/utils.js:99`

## `_formatBubbleDate` — function, line 118
- **called from:**
- `static/js/emailLibrary.js:6098`
- `static/js/emailLibrary/utils.js:118`

## `_formatRecipients` — function, line 132
- **called from:**
- `static/js/emailLibrary.js:5084`
- `static/js/emailLibrary/utils.js:132`

## `_senderColor` — function, line 150
- **called from:**
- `static/js/emailInbox.js:583`
- `static/js/emailInbox.js:1447`
- `static/js/emailLibrary.js:899`
- `static/js/emailLibrary.js:5093`
- `static/js/emailLibrary.js:6163`
- `static/js/emailLibrary/utils.js:150`

## `_initials` — function, line 162
- **called from:**
- `static/js/emailLibrary.js:6162`
- `static/js/emailLibrary/utils.js:162`

## `_sanitizeHtmlOnce` — function, line 177
- **called from:**
- `static/js/emailLibrary/utils.js:177`
- `static/js/emailLibrary/utils.js:243`

## `_sanitizeHtml` — function, line 240
- **called from:**
- `static/js/emailLibrary.js:5829`
- `static/js/emailLibrary.js:5847`
- `static/js/emailLibrary.js:6175`
- `static/js/emailLibrary.js:6205`
- `static/js/emailLibrary.js:6213`
- `static/js/emailLibrary.js:6215`
- `static/js/emailLibrary/utils.js:240`
