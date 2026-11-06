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

## `_emailSummaryErrorMessage` — function, line 40
- **called from:**
- `static/js/emailLibrary/utils.js:40`
- `static/js/emailLibrary/utils.js:48`

## `_renderEmailSummaryError` — function, line 45
- **called from:**
- `static/js/emailLibrary/reader.js:661`
- `static/js/emailLibrary/reader.js:665`
- `static/js/emailLibrary/utils.js:45`

## `_attrEsc` — function, line 52
- **called from:**
- `static/js/emailLibrary/utils.js:52`
- `static/js/emailLibrary/utils.js:89`
- `static/js/features/notes/ui/text.js:7`
- `static/js/features/notes/ui/text.js:34`

## `_compactUrlSchemeValue` — function, line 61
- **called from:**
- `static/js/emailLibrary/utils.js:61`
- `static/js/emailLibrary/utils.js:66`
- `static/js/emailLibrary/utils.js:224`
- `static/js/markdown.js:391`
- `static/js/markdown.js:396`
- `static/js/markdown.js:423`

## `_isDangerousUrl` — function, line 65
- **called from:**
- `static/js/emailLibrary/utils.js:65`
- `static/js/emailLibrary/utils.js:71`
- `static/js/emailLibrary/utils.js:207`
- `static/js/markdown.js:395`
- `static/js/markdown.js:400`
- `static/js/markdown.js:432`

## `_isDangerousSrcset` — function, line 70
- **called from:**
- `static/js/emailLibrary/utils.js:70`
- `static/js/emailLibrary/utils.js:207`
- `static/js/markdown.js:399`
- `static/js/markdown.js:432`

## `_escLinkify` — function, line 75
- **called from:**
- `static/js/emailLibrary/bodyRender.js:92`
- `static/js/emailLibrary/bodyRender.js:150`
- `static/js/emailLibrary/bodyRender.js:178`
- `static/js/emailLibrary/bodyRender.js:191`
- `static/js/emailLibrary/bodyRender.js:761`
- `static/js/emailLibrary/utils.js:75`

## `_extractName` — function, line 98
- **called from:**
- `static/js/emailLibrary/aiReply.js:407`
- `static/js/emailLibrary/index.js:6064`
- `static/js/emailLibrary/reader.js:316`
- `static/js/emailLibrary/reader.js:467`
- `static/js/emailLibrary/utils.js:98`

## `_parseTurnMeta` — function, line 107
- **called from:**
- `static/js/emailLibrary/bodyRender.js:469`
- `static/js/emailLibrary/bodyRender.js:509`
- `static/js/emailLibrary/utils.js:107`

## `_formatBubbleDate` — function, line 126
- **called from:**
- `static/js/emailLibrary/bodyRender.js:457`
- `static/js/emailLibrary/utils.js:126`

## `_formatRecipients` — function, line 140
- **called from:**
- `static/js/emailLibrary/index.js:5487`
- `static/js/emailLibrary/utils.js:140`

## `_senderColor` — function, line 158
- **called from:**
- `static/js/emailInbox.js:600`
- `static/js/emailInbox.js:1527`
- `static/js/emailLibrary/bodyRender.js:522`
- `static/js/emailLibrary/index.js:647`
- `static/js/emailLibrary/index.js:5496`
- `static/js/emailLibrary/utils.js:158`

## `_initials` — function, line 170
- **called from:**
- `static/js/emailLibrary/bodyRender.js:521`
- `static/js/emailLibrary/utils.js:170`

## `_sanitizeHtmlOnce` — function, line 185
- **called from:**
- `static/js/emailLibrary/utils.js:185`
- `static/js/emailLibrary/utils.js:251`

## `_sanitizeHtml` — function, line 248
- **called from:**
- `static/js/emailLibrary/bodyRender.js:174`
- `static/js/emailLibrary/bodyRender.js:192`
- `static/js/emailLibrary/bodyRender.js:534`
- `static/js/emailLibrary/bodyRender.js:564`
- `static/js/emailLibrary/bodyRender.js:572`
- `static/js/emailLibrary/bodyRender.js:574`
- `static/js/emailLibrary/utils.js:248`
