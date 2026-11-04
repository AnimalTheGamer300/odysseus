# `static/js/tts-ai.js` — definitions & call sites

22 definitions (regex-based, best-effort).
**Exports:** `AITTSManager`, `addAITTSButton`, `default`

## `AITTSManager` — class, line 6
- **called from:**
- `static/js/tts-ai.js:459`

## `constructor` — method?, line 7
- **called from:**
- `static/js/signature.js:39`
- `static/js/spinner.js:15`
- `static/js/tts-ai.js:7`

## `checkAvailability` — method?, line 33
- **called from:**
- `static/js/settings.js:849`
- `static/js/tts-ai.js:30`
- `static/js/tts-ai.js:33`

## `extractPlainText` — method?, line 71
- **called from:**
- `static/js/tts-ai.js:71`
- `static/js/tts-ai.js:114`
- `static/js/tts-ai.js:181`
- `static/js/tts-ai.js:306`
- `static/js/tts-ai.js:370`
- `static/js/tts-ai.js:438`

## `getCacheKey` — method?, line 98
- **called from:**
- `static/js/tts-ai.js:98`
- `static/js/tts-ai.js:125`

## `synthesize` — method?, line 109
- **called from:**
- `routes/tts_routes.py:50`
- `services/tts/tts_service.py:245`
- `tests/test_speech_service_toggles.py:29`
- `tests/test_tts_speed_malformed.py:31`
- `static/js/tts-ai.js:109`
- `static/js/tts-ai.js:189`
- `static/js/tts-ai.js:296`

## `_findBrowserVoice` — method?, line 167
- **called from:**
- `static/js/tts-ai.js:167`
- `static/js/tts-ai.js:206`

## `play` — method?, line 177
- **called from:**
- `static/js/settings.js:926`
- `static/js/slashCommands.js:2104`
- `static/js/tts-ai.js:120`
- `static/js/tts-ai.js:177`
- `static/js/tts-ai.js:192`
- `static/js/tts-ai.js:335`

## `_playBrowser` — method?, line 203
- **called from:**
- `static/js/tts-ai.js:185`
- `static/js/tts-ai.js:203`
- `static/js/tts-ai.js:307`

## `stop` — method?, line 224
- **called from:**
- `app.py:1290`
- `launcher.py:96`
- `routes/chat_routes.py:3099`
- `tests/test_compare_stop_disconnect_poll.py:146`
- `tests/test_compare_stop_disconnect_poll.py:232`
- `tests/test_compare_stop_disconnect_poll.py:233`
- `tests/test_compare_stop_disconnect_poll.py:235`
- `static/js/admin.js:673`
- `static/js/chat.js:4863`
- `static/js/chat.js:4954`
- `static/js/chatRenderer.js:145`
- `static/js/compare/stream.js:250`
- `static/js/compare/stream.js:287`
- `static/js/cookbookRunning.js:2895`
- `static/js/documentLibrary.js:3065`
- `static/js/documentLibrary.js:3218`
- `static/js/emailLibrary.js:8414`
- `static/js/fileHandler.js:347`
- `static/js/galleryEditor.js:3664`
- `static/js/keyboard-shortcuts.js:171`
- `static/js/models.js:220`
- `static/js/settings.js:2652`
- `static/js/spinner.js:260`
- `static/js/spinner.js:268`
- `static/js/spinner.js:274`
- `static/js/spinner.js:288`
- `static/js/spinner.js:367`
- `static/js/spinner.js:408`
- `static/js/spinner.js:425`
- `static/js/spinner.js:437`
- `static/js/tasks.js:2865`
- `static/js/tts-ai.js:179`
- `static/js/tts-ai.js:224`
- `static/js/tts-ai.js:503`
- `static/js/tts-ai.js:517`
- `static/js/voiceRecorder.js:102`
- `static/js/voiceRecorder.js:178`
- `static/js/voiceRecorder.js:251`

## `enqueue` — method?, line 256
- **called from:**
- `static/js/chat.js:4741`
- `static/js/tts-ai.js:256`
- `static/js/tts-ai.js:401`
- `static/js/tts-ai.js:445`
- `static/js/tts-ai.js:508`

## `_processQueue` — method?, line 263
- **called from:**
- `static/js/cookbookRunning.js:662`
- `static/js/cookbookRunning.js:3251`
- `static/js/cookbookRunning.js:3305`
- `static/js/cookbookRunning.js:3312`
- `static/js/cookbookRunning.js:3551`
- `static/js/tts-ai.js:259`
- `static/js/tts-ai.js:263`

## `_playQueueItem` — method?, line 283
- **called from:**
- `static/js/tts-ai.js:270`
- `static/js/tts-ai.js:283`

## `streamingStart` — method?, line 347
- **called from:**
- `static/js/chat.js:2566`
- `static/js/tts-ai.js:347`

## `streamingUpdate` — method?, line 354
- **called from:**
- `static/js/chat.js:3366`
- `static/js/chat.js:3514`
- `static/js/tts-ai.js:354`

## `_processStreamingSentences` — method?, line 363
- **called from:**
- `static/js/tts-ai.js:359`
- `static/js/tts-ai.js:363`

## `_createPlaceholderButton` — method?, line 408
- **called from:**
- `static/js/tts-ai.js:399`
- `static/js/tts-ai.js:408`
- `static/js/tts-ai.js:443`

## `streamingAttachButton` — method?, line 415
- **called from:**
- `static/js/chat.js:4731`
- `static/js/tts-ai.js:415`

## `streamingEnd` — method?, line 426
- **called from:**
- `static/js/chat.js:4730`
- `static/js/tts-ai.js:426`

## `clearCache` — method?, line 450
- **called from:**
- `static/js/tts-ai.js:450`

## `addAITTSButton` — function, line 462
- **called from:**
- `static/js/chat.js:4714`
- `static/js/tts-ai.js:462`

## `resetButton` — function, line 491
- **called from:**
- `static/js/tts-ai.js:491`
- `static/js/tts-ai.js:504`
