# Odysseus — Architecture Map

> **Purpose:** this is the map future IRISes read *first*. Every hour spent re-discovering
> this stuff by grep is an hour wasted. If you find something that changed, update this
> doc in the same breath — it lives with the code.
>
> Repo: `odysseus-garboGH` · Base: upstream PRs ~#4983–#5290 · Written: 2026-08-05
> · Last updated: 2026-08-09 (coherence audit — see §6)
>
> House style: lean, dense, pointer-heavy. No prose that can rot. File:line citations
> where they matter. The changelog lives in `ODYSSEUS-CHANGES.md` (same repo root).
>
> **Per-file map:** want "what does THIS file do, and who does it talk to" — read
> `docs/FILE_MAP.md` (written 2026-08-08). This doc is the overview; FILE_MAP is the
> street map.

---

## 1. Repo Map

```
odysseus-garboGH/
├── app.py                  FastAPI entry — wires ~42 routers, middleware, lifespan
├── routes/                 73 files — the HTTP layer, one module per feature area
├── src/                    144 files — the ENGINE (agent loop, LLM core, tools)
├── core/                   foundation — auth, db, models, session manager, config
├── services/               external wrappers — TTS, STT, YouTube, search, MCP
├── integrations/           third-party integrations
├── companion/              companion app bits
├── static/                 152 JS files + index.html + sw.js (frontend)
│   └── js/                 per-feature ES modules (chat.js, sessions.js, ...)
├── tests/                  762 files — the test suite
├── docs/                   markdown docs + demo .webm videos (house convention)
├── logs/                   runtime logs
├── .backups/               root-level backup dir
└── ODYSSEUS-CHANGES.md     changelog (created 2026-08-05 — APPEND EVERY CHANGE)
```

Scale (venv excluded): ~350k lines — 1,061 Python files / ~215k lines, 152 JS files / ~133k lines.

**Real vs dead weight:** everything listed above is real. There is no "dead" tree; even
`companion/` and `integrations/` have live code. `.backups/` is where pre-edit snapshots
accumulate. `logs/` is where the app log lives — check it *first* when something 502s.

---

## 2. Backend

### 2.1 Entry & wiring — `app.py`

- FastAPI app; ~42 routers mounted (46 `include_router` calls, all under `/api/*`).
- Middleware stack (order matters): CORS → GZip → SecurityHeaders → timeouts →
  `AuthMiddleware` → `_RevalidatingStatic` (forces no-cache on JS/CSS/HTML — the
  reason sw.js caching behavior bites the way it does; see §5 Landmines).
- Lifespan/startup: purges leftover "Nobody"/"Incognito" sessions, defers MCP
  connection setup.

### 2.2 Layers

| Layer | Path | Role |
|---|---|---|
| Routes | `routes/*.py` | HTTP surface — auth, chat, session, model, document, email, memory, tool, settings, notes, image, gallery, research, voice, ... |
| Engine | `src/` | the real logic: `agent_loop.py`, `llm_core.py`, `model_context.py`, `chat_processor.py`, tools |
| Foundation | `core/` | `auth.py` (AuthManager: bcrypt + TOTP + roles), `db.py` (SQLAlchemy), `models.py` (lightweight dataclasses: `DbSession`, `ChatMessage`, `ModelEndpoint`, `ApiToken`), session_manager, database, config (Pydantic, reads `.env`) |
| Wrappers | `services/` | external calls — TTS/STT, YouTube, search/SEARXNG, MCP clients |

### 2.3 Chat API — the hot path

All in `routes/chat_routes.py`:

- `POST /api/chat_stream` — the main streaming endpoint. FormData (not JSON): `message`,
  `session`, `selected_model`, plus `reuse_last_user=true` on regenerate (backend reuses
  the existing user row instead of persisting a new one). Streams SSE (`event: delta` /
  `event: error`); the **first event is `user_message_saved`** (the persisted user row's
  DB id — the frontend stamps the optimistic bubble so delete/regenerate target by id).
  Has research callbacks and image-progress events. **Turn-persistence guarantee
  (2026-08-08 sync audit):** a partial assistant reply is ALWAYS persisted — on client
  disconnect, mid-stream upstream exception, or a stream ending without `[DONE]` — via
  `_persist_stream_partial` (reasoning kept in `metadata.thinking`, `stopped: True` so
  refresh shows the Continue affordance; reasoning-only partials persist too, so a turn
  can never vanish from the DB). **Progressive draft checkpoint (2026-08-08
  draft-checkpoint audit):** while a turn streams, `_checkpoint()` writes the in-flight
  reply to a DB-only draft row (`metadata.draft=True`) — first create fires `draft_saved`
  (the bubble stamps its row id early), then a 4s cadence of in-place updates. Drafts
  are NEVER part of in-memory history (the model's context can't see half-written
  replies). On `[DONE]` the draft is promoted IN PLACE (same row id — `draft_id` threaded
  into `save_assistant_response`/`_persist_stream_partial`) so no duplicate appears; if
  the process dies mid-turn, the history reader + `_db_to_session` hydration finalize
  the orphan as a stopped partial, so the crashed turn survives as a resumable
  "[Message interrupted]" message (live drafts are hidden from history while streaming).
- `POST /api/chat/resume` — stream resume (see §6: garbo ships WITHOUT resume; `resumeStream`
  is dead code).
- `POST /api/chat/stop` · `GET /api/chat/stream_status/{sid}` · rewrite / inject / search endpoints.
- **`_ensure_current_request_is_latest_user`** — server-side dedupe so a slow old request
  can't clobber a newer one. Directly adjacent to the ghost-bug class.

Sessions: `routes/session_routes.py` — CRUD + **`PATCH /session/{sid}`** (rename endpoint,
~line 493); `POST /session/{sid}/retitle` (line 571, added 2026-08-06 auto-title fix) is
what the frontend auto-title dropdown calls.

### 2.4 Failure modes seen in the wild

- **502 stream errors** — almost always the *provider*, not the app. Observed cause:
  `opencode.ai rejected the API key — No payment method` → "All model candidates
  returned no substantive output" → server sends `event: error` status 502. Check
  `logs/` first, then the endpoint's billing.
- `stream_status/{sid}` 404s — normal noise when a session has no active stream. Not a bug.

---

## 3. Frontend

### 3.1 Module graph

- `static/index.html` loads 32 ES modules with **versioned URLs**
  (e.g. `sessions.js?v=20260806autotitle1`, `chat.js?v=20260807historyrecall`).
- `static/app.js` is the orchestrator — imports 36 modules, owns bootstrap:
  `startOdysseusApp()` (~line 3706), `initializeEventListeners()` (~line 268),
  `_handleNewChatAction`, `_startFreshChat`, `_createDirectChatFromPreferredModel`.
- Per-feature modules in `static/js/`: chat.js (~6k lines — the monster), sessions.js
  (~3.7k — session state), chatRenderer.js (~2.8k — message rendering, thinking blocks),
  chatStream.js (stream lifecycle), document.js (~11k), slashCommands.js (~6.5k),
  settings.js, notes.js, emailLibrary.js, models.js, memory.js, gallery.js, ...

### 3.2 Service worker — `static/sw.js`

- **Network-first for JS/CSS**, stale-while-revalidate for HTML, cache-first for assets.
- Cache name is versioned (`odysseus-v391-autotitle1` as of 2026-08-09). Bump it when
  precache lists change, or old JS haunts you.
- **Version-token discipline is mandatory** (see Landmines).

### 3.3 Session state (the part that burned IRIS hardest)

`sessions.js` holds the session state: `currentSessionId`, `lastSelected`,
`__odysseusLastSelectedSessionId` (the "trap" — re-select guard), `selectSession()`,
`createDirectChat()` (~line 2249).

**Select semantics:** clicking a session writes hash + lastSelected **synchronously**,
but sets `currentSessionId` **asynchronously** (after history load). That split is a
race source — see the ghost bug in §5.

---

## 4. Critical Paths

### 4.1 Send a message

1. `handleChatSubmit` (chat.js) — builds FormData: `message`, `session`, `selected_model`.
   The session field comes from `streamSessionId`, resolved via
   `_adoptOpenedSessionBeforeAutoCreate()` — fallback chain: `activeRowId || hashId || lastSelectedId`.
   Pending-flow flags (continue/regen/edit/auto-recover) are captured + cleared at send
   entry, before any early return — an aborted send can't leak them into the next one
   (2026-08-08, Finding A).
2. POST `/api/chat_stream` → SSE stream loop (chat.js ~2300-2800) — deltas render via
   chatRenderer; completion calls `selectSession(streamSessionId)` guarded by "still
   current" checks.
3. On stream error → catch block. **This catch used to crash** (TTS ReferenceError —
   fixed 2026-08-05, see §5). If the catch dies, cleanup never runs: no error message,
   flags never release, optimistic bubble haunts the wrong chat.

### 4.2 New Chat

`_handleNewChatAction` (app.js) →
`_createDirectChatFromPreferredModel()` — if a preferred model endpoint exists (you
always have qwen/deepseek), it **always returns true** and `createDirectChat()` runs
(clears container, hash, trap, nulls current) — and `_startFreshChat()` (the *full*
reset: container + hash + trap + currentSessionId) is **skipped**. Both paths must be
understood before touching new-chat behavior. The 2026-08-05 fix added an intent flag
(`__odysseusNewChatIntent`) + trap clearing so the send path can't re-adopt the old chat.

### 4.3 Stream lifecycle

start (SSE open) → deltas → completion OR error → cleanup (TTS stop, holder removal,
final render, state sync). chatStream.js handles lifecycle events; chat.js holds the loop.
`resumeStream` exists but is **never called** — garbo ships without resume.

---

## 5. Landmines (READ BEFORE TOUCHING ANYTHING)

1. **Split-brain module instances (the ghost bug — fixed 2026-08-05, re-broken by
   dynamic-import stragglers 2026-08-06 → 08-09, re-fixed 2026-08-09).** ES modules
   loaded under two different URLs (versioned vs bare `./sessions.js`) are TWO separate
   instances with independent state + duplicate event listeners. Symptom: UI says one
   thing, engine does another; messages land in the wrong chat; "works then doesn't."
   **Fix discipline: versioned module URLs must match across index.html, app.js, every
   static import, AND every dynamic `import('./x.js?v=...')` call.** Current state
   (2026-08-09 re-audit, path-aware scan excluding `.bak-*`): ALL 19 refs on
   `sessions.js?v=20260806autotitle1` — index.html modulepreload + script tag, app.js,
   sw.js precache, 13 static imports, and the 3 dynamic imports that had drifted
   (`chatRenderer.js:1191` → `selectSession`, `chatStream.js:164` → `openLibrary`,
   `presets.js:403` → `getSessions`/`getCurrentSessionId`). Zero bare imports, zero
   stragglers. Audit trap: a naive `grep -r sessions.js?v=` counts `.bak-*` backups as
   live — always exclude them (path-aware scan or `grep -n` + filter), or backup noise
   fakes a split-brain. Before adding a version query to any module, check it isn't
   imported bare elsewhere.
2. **sw.js caching.** After changing JS: bump the version token AND/OR cache name; then
   hard-refresh (Ctrl+Shift+R) once, or you debug stale code. The `_RevalidatingStatic`
   middleware forces no-cache on HTML/JS/CSS, which mostly saves you — but the SW
   precache still needs the cache-name bump when its list changes.
3. **Pre-existing dirty files** — `src/agent_loop.py`, `src/llm_core.py`,
   `src/model_context.py` were already modified before 2026-08-05. NOT from the ghost
   work. Don't assume they're pristine; document or revert deliberately.
4. **Provider 502s ≠ app bugs.** Check `logs/` and endpoint billing before hunting code.
5. **`.old`'s freeze suspect.** `odysseus.old` (previous upstream base, PRs ~#2548–#2989)
   freezes to a halt after ~82 tok/s. Prime suspect: prior-IRIS `resumeStream`
   implementation (CPU hog). garbo does NOT have this problem. Do not port `.old`'s
   resume machinery wholesale.
6. **The boop counter.** Sir types boop-variants mid-hunt (boob/bool/boot/boof/booz/
   booq/boog/boo). They mean "continue." Do not read meaning into them; do not let them
   derail the task. (This is canon now.)

---

## 6. History & Open Items

### 2026-08-09 — ARCHITECTURE.md coherence audit (IRIS)

Re-read this doc against the live tree; stale citations updated in place. What changed
the map:

- **Landmine #1: found LIVE via 3 dynamic-import stragglers → FIXED 2026-08-09.**
  `chatRenderer.js:1191`, `chatStream.js:164`, `presets.js:403` imported
  `sessions.js?v=20260805unified2` while the other 16 refs were on
  `?v=20260806autotitle1`. The 2026-08-06 "grep-audited" verification (changelog:710)
  covered static imports + index.html tags but MISSED dynamic `import(...)` calls —
  split-brain could fire on message-session-link click (selectSession), sessions-panel
  open (openLibrary), or custom-character save (getSessions/getCurrentSessionId). Fix
  applied per Sir's approval: 3 one-line bumps to `20260806autotitle1` + sw cache
  `v390-thinkclose` → `v391-autotitle1`. Cache bump was REQUIRED, not optional: the
  CONTAINER files (chatRenderer.js, chatStream.js) are SW-precached under their own URL
  tokens — content changed under the same URL stays stale cache-first without the bump
  (presets.js is unversioned in index.html, propagates via bg-refresh). Post-fix
  verification: path-aware scan excluding `.bak-*` shows 19/19 refs on
  `20260806autotitle1`, zero bare imports. Hard-refresh (Ctrl+Shift+R) once after
  deploying.
- **auto-title: marked FIXED** (2026-08-06 — retitle route session_routes.py:571,
  tab-title mirror IIFE, `?v=20260806autotitle1`, cache v385-autotitle1; changelog
  2026-08-06).
- **Addendum items 1–2 RESOLVED, 3 PARTIAL** (see statuses below; changelog:1497-1498).
- **sw cache:** `odysseus-v391-autotitle1` (the v377/v378 numbers in old receipts are
  superseded — chain ran v385-autotitle1 → v386-historyrecall → v387-unified-chat →
  v390-thinkclose → v391-autotitle1, the 2026-08-09 split-brain fix).
- Counts refreshed: src 144, tests 762, 1,061 py files / ~215k lines, 32 ES modules in
  index.html, ~42 routers (46 include_router calls), static/app.js imports 36.
- Still OPEN: addendum items 4–6 (memory_extractor refinements, user-nominated paths
  bypass, animated favicon); the mcp CancelledError guards in src/mcp_manager.py.

### 2026-08-05 → 2026-08-06 — auto-title (FIXED 2026-08-06)

- Ported in the `.old` transplant (receipts below: retitle route + `_clean_title`,
  dropdown item, sessions.js `unified1->unified2`, sw v378), **had a bug** — fixed
  2026-08-06: `POST /api/session/{sid}/retitle` route (session_routes.py:571),
  `_clean_title` + `_ECHO_PHRASES` guards, tab-title mirror IIFE restored, token →
  `?v=20260806autotitle1`, cache → `odysseus-v385-autotitle1` (changelog 2026-08-06).
- Status: FIXED, verified live. (Note: the 3 dynamic-import stragglers on the old
  `unified2` token were unified onto `autotitle1` on 2026-08-09 — see the audit entry
  above.)

### 2026-08-05 — ghost-message bug (FIXED, verified live)

- **Root cause:** split-brain `sessions.js` instances (versioned UI import vs bare engine
  imports) → two copies of session state → New Chat cleared the UI copy while the engine
  copy still pointed at the old chat → next POST went to the old chat.
- **Fix:** unified all 19 references onto `sessions.js?v=20260805unified1`; sw.js precache
  updated + cache bumped (`odysseus-v377-unified-sessions` — superseded, now
  `odysseus-v391-autotitle1`); belt-and-suspenders: New Chat intent flag + trap clearing
  + adopt guard.
- **Also fixed:** TTS ReferenceError — `streamingTTS` was `const` inside the try block,
  referenced in the catch (invisible → catch crashed on any stream error). Hoisted to
  module scope (chat.js:1787).
- **Receipts:** backup `/tmp/odysseus-garboGH-static-backup-20260805-111154.tar.gz`;
  full writeup in `ODYSSEUS-CHANGES.md`.

### 2026-08-05 — POST-AUDIT GAP ADDENDUM (changelog-scope, NOT the file pile)

The receipts below were written against `.old`'s dirty-*file* pile. A later
changelog-scope audit found SIX unported entries the receipts never covered:

1. **Agent preamble / analyst-register fix** — garbo still ships stock
   "You are an AI assistant with tool access" (`src/agent_loop.py:280`); `.old`
   removed the "AI assistant" frame. OVERLAPS user's in-progress agent JB tweak —
   coordinate, don't duplicate. **→ RESOLVED 2026-08-06** (changelog:1497): preamble is
   "You have tool access in this session" at all identity sites; zero "AI assistant"
   matches in agent_loop.py (verified 2026-08-09).
2. **IRIS persona preset** (`data/presets.json`) — `.old` carries the full
   IRIS/catgirl persona preset; garbo's presets.json has ZERO iris/catgirl content.
   **→ RESOLVED 2026-08-06** (changelog:1498): "Custom" preset = full IRIS persona
   (45,414-char system prompt, temperature 1.0, enabled). Verified at
   data/presets.json:25 (2026-08-09).
3. **MCP `mcp<2` pin + CancelledError crash fixes** — `.old` pins `mcp<2` and has
   two `asyncio.CancelledError` guards in `src/mcp_manager.py`; garbo has bare `mcp`
   (2.0.0 installed), zero guards. **→ PARTIAL (2026-08-09):** pin DONE —
   requirements.txt:41 has `mcp<2` (1.29.0 installed). Guards STILL MISSING — zero
   CancelledError matches in src/mcp_manager.py.
4. **memory_extractor refinements** — `.old` upgraded to "MAX 3 facts, must stand
   ALONE (15-50 words), durable-only filter, rewrite-fragment exception"; garbo has
   the older "MAX 2 facts, under 15 words" version.
5. **User-nominated paths bypass** (feature, security-adjacent) — `.old`
   `tool_execution.py` accepts `user_text` and exempts user-named paths from
   workspace confinement (deny-first, tested). Garbo: absent.
6. **Animated favicon during LLM turns** — `.old` theme.js busy-arc; garbo only
   has theme-color sync. Cosmetic.

Status (2026-08-09): 1–2 RESOLVED, 3 PARTIAL (pin done / guards pending), 4–6 OPEN.
Do not treat the transplant as 1:1 until 3–6 are resolved or explicitly skipped.

### 2026-08-05 — `.old` transplant receipts (ALL CLOSED except stream-resume)

Every item below was ported, verified (venv import / py_compile / JS syntax / semantic
round-trip), and backed up (`style.css.bak-20260805`, `ARCHITECTURE.md.bak-20260805`,
plus git working tree for everything else). The stream-resume exclusion stands.

| `.old` feature | Verdict | Receipt |
|---|---|---|
| hljs cap on giant outputs | PORTED | `static/style.css`: `.agent-tool-output pre { max-height: 480px }` — drop-in, class already emitted by chatRenderer:2397 |
| tool-output truncation | PORTED | `static/style.css`: `.agent-thread-tail { max-height: 140px !important }` (chat.js:3686 emits the class) |
| thinking pre-wrap fix | PORTED | `static/style.css` `.thinking-content-inner`: `white-space: pre-wrap; word-break: break-word;` — was missing vs .old:8450 |
| auto-title | PORTED | retitle route + `_clean_title` (session_routes.py:571/:75); dropdown item sessions.js:703; sessions.js token `unified1→unified2` (19 refs, superseded → `autotitle1` 2026-08-06) + sw cache v377→v378 (now v391-autotitle1) |
| teacher-takeover fix | PORTED | teacher_escalation.py anchored MULTILINE patterns (killed unanchored `\berror:\s`/`\bnot found\b`); `data.get("teacher")` guards at chat_routes delta sites + rewrite path — garbo had ZERO guards (bug confirmed live) |
| tool_schemas slimming | PORTED (3-way merge) | 1595→967 lines; 39 tools swapped where `garbo == .old-pre`, 32 untouched (16 drifted + 6 garbo-only); semantic round-trip + real-order import verified |
| agent_runs subscriber cap | PORTED | `_MAX_SUBSCRIBERS = 4` + replay-path guard (RAM-bomb / tab-storm bound) |
| tuning pile (constants/settings/request_models) | PORTED | output 10k→50k, read 20k→200k, name 50→100, system_prompt 10k→100k, inject pre/suffix 5k→50k, research 16384→163840, agent budget 6000→200000, sys-prompt trunc 2k→200k |
| context_compactor force_threshold_tokens | PORTED | signature param + logic branch; agent_loop mid-message compact block + 600000 fallback |
| integrations API truncation | N/A | garbo refactored upstream (DICT_LIMIT/budget system) — old 12k block doesn't exist |
| tool_parsing fence fix | ALREADY IN GARBO | `_ALLOW_MID_REPLY_FENCES` (line 23) + trailing-fence walk-back (1276-1300) + `skip_fenced` extension |
| history ghost-delete | ALREADY IN GARBO (superseded) | exact-id delete — `routes/history/history_routes.py:355-395`; `resolve_pairs` pair-delete removed 2026-08-08 (Sir's spec: no pair obliteration) |
| reasoning_content chain | MOSTLY IN GARBO | metadata round-trip + `_metrics_to_save["thinking"]` + `_supports_thinking` gate (llm_core.py:1311) + newest-keeps-reasoning strip (agent_loop:2783 — line drifted, unverified 2026-08-09) + chatRenderer `<think>` rebuild (2578) |
| tool transcript caps | PORTED | agent_loop:5144-5147 (4000-char output) + :5178 (200-event cap) — the ONE genuine 7d gap |
| round_reasonings list | SKIPPED | dead weight — garbo frontend reads `metadata.thinking` blob, not the list |
| user_message_saved event | PORTED 2026-08-08 | chat_routes emits it as the FIRST stream event; chat.js stamps the optimistic user bubble with its DB id — exact-id delete + id-stable regenerate depend on it (see ODYSSEUS-CHANGES.md) |
| no-[DONE] rescue / thinking-only saves | REWORKED 2026-08-08 | sync audit replaced `_stopped_content`/`_stopped_md` with `_persist_stream_partial` — ONE save path for disconnect / upstream-exception / no-[DONE] ends: reasoning preserved in `metadata.thinking`, reasoning-only partials persist (empty content + thinking), `stopped: True` rides along; `_saw_done`/`_saved_this_turn` dedup across branches; reasoning-only completions save empty content + thinking only (refresh no longer double-renders) |
| stream-resume | EXCLUDED | `.old`'s is the freeze suspect; design fresh if ever wanted |

**Open items still:** opencode.ai endpoint billing (502s); `.old` freeze investigation
(resumeStream suspect) — separate project.

- opencode.ai endpoint billing → fix whenever (causes 502s on that model).
- `.old` freeze investigation (resumeStream suspect) — separate project.

---

## 7. Conventions

- **Backup before touching anything an app runs on:** `cp file file.bak-<date>` or a
  tarball to `/tmp` (ghost-fix precedent: full `static/` tarball).
- **Version tokens** on JS module URLs; bump on every change; keep index.html, app.js,
  and static imports in lockstep.
- **Changelog:** append every change to `ODYSSEUS-CHANGES.md`, dated, with root cause +
  receipts (mirrors `.old`'s house style).
- **Tests:** 762 files exist — run them before/after engine changes.
- **Verify on the wire:** the ghost hunt's gold standard was live browser verification
  (fetch/XHR wiretap + state dumps). For frontend bugs: reproduce live, then verify live.
