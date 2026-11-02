# Odysseus Change Log — main tree

> Changelog for the **main Odysseus tree** (`/run/media/crao/BTnvme/LLM/odysseus`, served on 127.0.0.1:7001).
> Format follows the `.old` fork's `ODYSSEUS-CHANGES.md` house style.
> Standing rule: every change made to files under `odysseus/` gets appended here, dated.

## 2026-10-31 — fix(agents): sub-agent runs auto-satisfy the post-external-context approval gate

Upstream's tool-approval flow ("Allow this task to continue?") seals a dangerous tool call once external untrusted content (web pages, search results) has entered the run, emits an ask_user card, and ENDS the turn — the human's decision rides back in on the next message (tool_approval_id → ExactToolApproval). Sub-agents (spawn_agent) are headless: run_subagent's stream parser only consumes delta/tool_output events, so the card was silently swallowed and the sub-agent's run ended mid-task with a truncated report — the gated tool never executed.

Fix: stream_agent_loop auto-satisfies the automatic post-external-context gate for sub-agent runs (keyed on `_subagent_depth`), reusing the existing task-scope-approval bypass flag. The delegated-credential refusal still fires first in decision_for; tool policy, disabled tools, ownership, workspace confinement, and sandbox restrictions all still apply. `ask_user` is also removed from the sub-agent catalog (headless runs cannot answer cards, whether gate-initiated or model-initiated).

Known structural trade-off (pre-existing, now reliable instead of silently broken): run-taint does not propagate across run boundaries, so a tainted parent can delegate gated actions to a fresh sub-agent run. The parent's own post-taint actions remain gated.

Files: `src/agent_loop.py`, `src/agent_tools/spawn_agent_tools.py`, `src/tool_schemas.py`, `src/tool_index.py` (+ TOOL_SECTIONS note in agent_loop.py)
Verified: py_compile, import, approval/capabilities test suite, description greps. Restart required to take effect.

## 2026-10-28 (03:20) — fix(agent): `manage_skills` was never shipped to any LLM — the admin-intent gate stranded the skill index

**Symptom (user-reported):** Odysseus has skills.md, yet it seems no LLM has
ever been given the tool to properly use it.

**Root cause — instruction/availability mismatch across three gates:**

1. **The index says "call `manage_skills`" on every turn.** The skill index is
   injected into the agent system prompt (`src/agent_loop.py::_build_base_prompt`,
   plus `src/chat_processor.py` for chat mode) whenever the owner has indexed
   skills and skills aren't suppressed — explicitly instructing *"Fetch the full
   procedure with `manage_skills` action=view name=<name>"*.
2. **The schema was stripped unless the turn looked "admin".**
   `_tool_schemas_for_route` filtered `FUNCTION_TOOL_SCHEMAS` against
   `_ADMIN_SCHEMA_NAMES` when `_needs_admin` was False — and `manage_skills`
   was in that set. `_needs_admin = _detect_admin_intent(messages)` fires only
   when the LAST user message contains an `_ADMIN_KEYWORDS` entry ("skill" is
   in the list, but ordinary work turns — "poke", "debug this" — never say it).
   The prompt catalog had the same hole: `_build_base_prompt`'s `mgmt_tools`
   subtraction (`TOOL_SECTIONS - ALWAYS_AVAILABLE - {...}`) dropped the
   `manage_skills` one-liner too, so fenced-block (non-API) models lost the
   prose as well.
3. **The "lockstep" guard was dead code.** The block that adds `manage_skills`
   when skills are indexed is gated on `_relevant_tools is not None`, but
   all-tools mode permanently forces `_relevant_tools = None` (RAG disabled
   2026-08-07), so it could never run.

Same stranded-instruction pattern on the scheduler path:
`src/task_scheduler.py` tells crew agents *"save it as a SKILL using
manage_skills"* / *"check manage_skills for an existing procedure"* while the
schema was equally stripped.

**Live evidence:** captured model reasoning in
`.playwright-mcp/page-2026-10-27T18-14-50-329Z.yml` — *"the skill index says
'call manage_skills(action='view', name='...')' — but manage_skills isn't in my
current tool list... No manage_skills tool visible this turn."*

**Fix (two lines + one removal):**

- `src/tool_index.py`: added `"manage_skills"` to `ALWAYS_AVAILABLE` — the
  tool now ships in the prompt catalog in lockstep with the index injection.
- `src/agent_loop.py`: removed `"manage_skills"` from `_ADMIN_SCHEMA_NAMES`
  (and deleted the stale duplicate definition left mid-file) — the schema is
  no longer stripped on non-admin turns.
- Execution gates are untouched: incognito, the `can_manage_memory`
  privilege, the global `disabled_tools` setting (verified NOT currently set
  in `data/settings.json` / `data2/settings.json`), and the
  capability/approval scopes still strip or deny it where they should.

**Tests:** 61 passed across tool-policy / skill-index / keyword-boundary /
update-plan suites; routing suite 98 passed with 4 failures that are
pre-existing (verified identical on the stashed pre-edit tree — fallout from
the earlier uncommitted merge work, unrelated to this change).

## 2026-10-25 (15:54) — fix(history): "message ID not found" on edit — `_db_id` was never re-derived from the DB row id

**Symptom (user-reported):** editing a message fails with *"Cannot edit:
message ID not found"* — while everything else in the app works fine.

**Root cause:** `routes/history/history_routes.py::_db_message_metadata()`
parsed the persisted `meta_data` blob and added `timestamp`, but never
re-derived the row's durable id. The blob itself does not reliably carry
`_db_id` — it is a runtime key stamped onto the in-memory message by
`core/session_manager.py`, not persisted — so every DB-served history entry
shipped to the browser had `metadata._db_id === undefined`.

The helper's own docstring and inline comment already described the
intended behaviour ("Metadata for a DB row, carrying the row's durable id"
/ "The row id is authoritative — it always wins over any stale value that
may have been persisted inside the metadata blob") — but the assignment
itself was missing. The helper extraction + docstring were uncommitted
in-flight work from the prior session; the line that does the work was
never written.

**Why it looked like "only editing is broken":** live-streamed messages get
`dataset.dbId` stamped from the server's message-id payload
(`chat.js:889`, `3924`, `3933`, `3950`), so a message edited in the same
session it was created in works fine. Messages loaded back from history go
through `chatRenderer.js:2689` / `2879`
(`if (metadata?._db_id) wrap.dataset.dbId = metadata._db_id`) and were
never stamped — so the edit button always hit the `!msgId` guard at
`chat.js:7209`.

**Fix (one line, `routes/history/history_routes.py`):**

```python
meta["_db_id"] = m.id
```

placed in `_db_message_metadata()` ahead of the `timestamp` fallback, so the
row's primary key always wins over any stale value persisted inside the
blob. Every consumer funnels through this one helper — `_db_history_entry`,
`_entry_or_none`, and `_hydrate_session_history_from_db` — so the paged
history response, the in-memory session history, and the renderer stamp all
pick it up at once.

**Verification:**
- `tests/test_delete_message_after_refresh.py`: 4 failed / 2 passed before →
  **6 passed** after. That file asserts the row id wins over a stale stored
  `_db_id`, that the id deletes the row, that the paged load keeps `_db_id`
  on in-memory history, and that the frontend does not claim "Message
  deleted" when it deleted nothing.
- Wider sweep (`-k "history or delete or edit or session or truncate or
  compact or replace_messages"`): 11 failed / 483 passed / 3 errors before →
  **7 failed / 487 passed / 3 errors** after — exactly 4 fewer failures and
  **no new failures**.

**Pre-existing failures, NOT from this change** (confirmed byte-identical at
clean HEAD `a5c77f8a`): the 2 failures in
`tests/test_replace_messages_upload_reservations.py` (the 2026-10-23
archive-don't-delete reform left those assertions still expecting hard
`DELETE`s) plus the remainder of the sweep's failures/errors.

**NOT LIVE YET — needs an app restart.** The running uvicorn (pid 497241,
started 04:30:55) predates this patch; there is no `--reload` and no
restart endpoint. Do **not** bounce it while a chat is streaming: the agent
loop runs *inside* the app process, so a restart kills the in-flight
session and any other open tab's stream. The 2026-10-20 socat bridge
(127.0.0.1:7000 → 7001) is already gone and no longer needed — the live
process has `APP_PORT=7001` in its env, so the bounce is clean: stop
pid 497241 (its konsole parent runs `run.sh`, which re-execs uvicorn on
7001) and start it again.

## 2026-10-24 (14:55) — fix(truncate): the session-eating truncate bug (root cause of the 349bf43f wipe) + transcript restored from forensic copies

**Symptom (user-reported 12:53):** "odysseus just wiped the chat history" —
session 349bf43f showed ~170k tokens of live context with zero visible rows.

**Root cause — three stacked defects, one kill chain (reconstructed from
app.log):**
1. `core/session_manager.py truncate_messages` hard-DELETEd tail rows — the
   one history writer the 2026-10-23 "reconcile, don't incinerate" reform
   never touched.
2. `routes/history/history_routes.py` truncate route: a `keep_through_id`
   that no longer resolved (an *earlier* truncate had already eaten the
   target row) fell back to `keep_count`, which defaults to 0 — i.e.
   "delete everything."
3. `static/js/chat.js` edit/resend/regenerate passed DOM-derived counts as
   `keep_count` (`_dbRowCountBefore` counts DOM rows, not DB rows — wrong the
   instant the render lags the DB). Log forensics of the kill chain:
   10:54:57 truncate→135 (43 rows), 12:47:56 truncate→12 (135 rows),
   12:53:50 truncate→0 (last 13 rows) — two seconds before the user noticed.

**Fixes (four independent layers — any one stops the data loss):**
- `truncate_messages` now ARCHIVES tail rows in place (metadata flag, same
  convention as `replace_messages`) instead of deleting; archived rows are
  excluded from keep-window math. Truncation is now reversible.
- Truncate route: unknown `keep_through_id` → 404 refusal, no destructive
  fallback; the id→position map excludes archived rows.
- `chat.js` editUserMessage / resendUserMessage / regenerateFrom: all three
  send `keep_through_id` (the target bubble's durable dbId) and refuse to
  truncate when the bubble has no dbId (nothing durable to truncate to).
- Plain `keep_count` remains supported for the explicit `/truncate N` slash
  command (deliberate user action).

**Data restore (same incident):** 168 message rows re-inserted for 349bf43f
from forensic sources — `odysseus.old!/data/app.db` (133 rows incl. its WAL),
`data/rescue/app.db.pre-import-20261023` (25), `data2/app.db` (32), deduped
by id — plus 31 clearly-marked recovery rows ([RECOVERED PREVIEW] skeletons
rebuilt from app.log agent-round summaries + one gap marker) covering the
~3 hours whose rows were destroyed before the first backup existed.
`sessions.message_count` re-seeded (199) so the hydration gate reloads the
full history on next access. Forensic backups + restore set live in
`Sandbox/db_backups/` (app.db.backup.20261024_125745 + raw WAL copy,
app.db.rawcopy.20261024_130703, final_restore_set.json).

**Deploy notes:** backend layers need a server restart (uvicorn still runs
pre-patch code in memory — restart when convenient, NOT mid-generation).
Frontend fix ships on next UI reload: cache busters bumped
`chat.js?v=20261023merge2` → `?v=20261024truncfix1` (index.html ×2, app.js,
sw.js precache) and `sw.js` CACHE_NAME → `odysseus-v394-20261024truncfix1`.

## 2026-10-24 (14:45) — fix unguarded ctx.user_message_id; clear stale pre-rename bytecode

**pytest triage, round 1** — local full-suite run (5,973 passed / 62 failed /
3 errors, Python 3.11.16 = CI's minor) triaged into three buckets:

- REAL FORK BUG (fixed here): `routes/chat_routes.py` streamed
  `user_message_saved` via unguarded `if ctx.user_message_id:` — the
  fork-only exact-id feature (2026-08-08) assumed the attr always exists.
  Test fixtures (SimpleNamespace contexts) lack it → AttributeError at
  chat_routes.py:1737 killed 26 foreground_model_routing tests. Now
  `getattr(ctx, "user_message_id", None)` — event emits only when the id
  exists, which was always the intent.
- SAME PATTERN, SECOND GUARD: the streaming path's draft-checkpoint helper
  called `session_manager.create_draft` unguarded — a fork-only
  session_manager API that upstream-generation mocks don't carry → 22 more
  foreground_model_routing failures at chat_routes.py:343. Now soft-drops
  checkpointing (returns None) when the API is absent; fork runtime unchanged.
- STALE ARTIFACT: `tests/__pycache__` held bytecode compiled before the
  garboGH→odysseus rename — tracebacks reported the old absolute paths
  (co_filename), making two failures look like cross-tree imports. Cleared.
  `tests/markdown_browser_check.py` / `markdown_screenshot.py` still carry
  hardcoded `ROOT = '...odysseus-garboGH'` (not pytest-collected; fix later).
- DIVERGENCE (documented, not fixed): remaining ~30 failures are upstream
  contracts the fork intentionally differs from — budget/truncation constants
  (200000/50000 vs upstream 6000/10000), tool-inventory enumerations,
  gemma4/thinking-tag JS behavior, notes-mode tool sets, history hydration,
  compose env forwarding. Tier-1 suspects kept for a focused pass:
  session_manager upload-reservation writer (:370), llm_core fallback chain
  (['primary'] vs ['primary','backup']), history hydration assert 6 == 0.

## 2026-10-24 (14:15) — restore merge-dropped CI/supply-chain infra (wound repairs II)

**Merge-wound audit follow-up** — the Oct 21 merge silently dropped upstream
files added 2026-10-05 (dab66054, "close pre-integration release blockers")
even though the fork side never touched them:

- `.gitleaks.toml` — the gitleaks allowlist. Its absence made the fork's
  Secret scan fail on 4 npm package identifiers ("inherits_2.0.4",
  "bluebird_3.4.7", "inherits_2.0.1", "inherits_2.0.3") that upstream's
  config explicitly allowlists as "package names, not secrets". Verified
  locally with the same pinned gitleaks v8.30.1 over full history (4,356
  commits): those 4 are the ONLY findings, all in
  THIRD_PARTY_PROVENANCE.json. Zero real secrets, nothing to rotate.
- `THIRD_PARTY_PROVENANCE.json` + `licenses/` (FiraCode, Inter, SheetJS,
  docx, highlightjs, mammoth) — supply-chain docs dropped alongside it.

Restored verbatim from odysseus-dev/main. The remaining files upstream has
that this fork lacks are upstream's parallel architecture (frontend/src
build tree, src/agent_runtime/, services/skills/, routes/email/ package,
their tests) which this fork's older layout does not use — divergence, not
wounds; left alone on purpose.

## 2026-10-24 (13:20) — repo hygiene: land upstream merge on main; untrack 81 scratch copies

**Tree cleanup** — the Oct 21 upstream merge (14171121) + wound repairs were
stranded on `merge/upstream-main-20261021`; fast-forwarded `main` to ab9fedd9
so the merge is landed and pushable. Untracked 81 committed scratch/backup
copies (74 `*.bak-*` full-file snapshots + 7 numeric/restored/autotitle
scratch files, ~314.5k duplicated lines) — files stay on disk and remain
recoverable from git history; future upstream diffs now show real code only.
`.gitignore` extended so scratch patterns can't be re-committed.

- `main` = ab9fedd9 + this cleanup; pushed to origin (AnimalTheGamer300 fork)
- fork `dev` reset to a pristine upstream mirror (old local dev was a stale
  June pre-history-cleanup fossil — 0 fork commits inside; kept as
  `backup/dev-stale-fossil-20261024`)

## 2026-10-24 (01:20) — fork repair (full-copy default + real timestamps) + history pager button

**Fork feature repaired** — bug confirmed in the CURRENT tree, not just .old!:
`fork_session` copied `source.history[:keep_count]` with `keep_count` defaulting
to 0 — a bare `/fork` produced an EMPTY session, and the copy-oldest-N semantics
silently dropped everything after the chosen point (the ⫝ IRIS fork kept 67 of
107 rows — Sir's "dropped more recent messages" report, forensically confirmed).
Also: the copy ran through `add_message`, stamping fresh arrival-order
timestamps — the .old! fork rendered a 107-message day as a 5-minute blur.

- `keep_count` absent/None/≤0 → copy the ENTIRE live transcript; explicit
  positive N → branch-at-message-N (the right-click "fork from this reply"
  flow is unchanged).
- Original timestamps preserved: fork rows re-stamped from `metadata.timestamp`.
- `/fork` (bare) sends no keep_count → full copy; `/fork N` still branches.

**History pager button**: the backend's last-24 pagination + `has_more_before`
were correct, but the scroll-up loader could fail silently (momentum scrolling)
and an anchored load is invisible from the reading position. Added a visible
"⬆ Load earlier messages (N more)" button at the top of the timeline — click
fetches the previous page and jumps to the oldest newly-loaded message. The
scroll handler remains as enhancement.

**Mystery note**: the top-bar count span (`#current-meta-count`) is dead markup —
nothing writes it, and no session in the DB has 128 messages. The "128msgs"
Sir spotted remains unexplained (cosmetic; possibly the session-cost display
or a transient render).

## 2026-10-23 (late) — compaction reform: archive, don't burn + 4 merge wounds

**Phase 1 of the compaction rebuild** (triggered by the 1.4M→150K lobotomy of the
merge-epic session; full transcript rescued byte-exact to `data/rescue/`):

- `core/session_manager.py` `replace_messages` is now a **reconciler**: rows the
  incoming history no longer references are flagged `{"archived": true}` in place —
  never deleted. Rows referenced via `metadata._db_id` keep their original ids and
  timestamps (no more delete + re-insert churn). Idempotent; smoke-tested against
  a temp DB (archive-not-delete, id/timestamp survival, live-count semantics).
- Hydrate gate (`_db_to_session`), session counts (`sync_session_metadata`,
  `load_sessions`), and all history display paths exclude archived rows — the
  archive stays on disk without re-bloating context or the UI.
- `core/models.py` `get_context_messages`: belt-and-suspenders archived filter.
- `routes/history/history_routes.py`: manual compact path disarmed (archive loop
  replaces the `db.delete` burn); **`POST /api/session/{id}/uncompact`** added
  (un-flags archived rows, drops summary rows, reloads memory from DB).

**Four merge wounds found & fixed** (test suite led straight to them; suite went
5 inherited failures → 57 passed, 0 failed):

1. `resolve_endpoint` was never imported in history_routes — **the manual Compact
   button has been a 500 since the merge**; the merge-epic lobotomy was 100%
   auto-compaction.
2. Duplicate `normalize_compaction_summary` in context_compactor.py — upstream's
   think-blind copy shadowed the fork's `_strip_think_blocks` guard
   (last-def-wins), re-arming the August reasoning-leak bug. Impostor deleted.
3. compact_session was missing its entire middle: `owner` derivation,
   `_reject_compact_during_active_run` guard (import + call), the
   older/recent/keep_count/convo_text block, `llm_call_async` +
   `_message_role`/`_message_text` imports, and upstream's
   `status`/`message`/`before`/`after` return fields. Restored from upstream.
4. `test_deferred_compaction_persists_only_after_route_commit` updated to the
   2026-08-08 convo→history mapping contract (upstream test had been stitched to
   the fork's newer function).

**Hotfix during rollout:** `from sqlalchemy import func` was missing in
history_routes (8 display-path filter sites) — caught live by Sir's console
(NameError on GET /api/history), fixed, verified end-to-end via authenticated
curl (login → history 200, 22 messages returned).

## 2026-10-23 — merge sealed + send-gate hotfix; header de-staled

**The big one:** merged `odysseus-dev/main` (`37d19df0`) into `merge/upstream-main-20261021` — all 56 conflicted files resolved, fork features preserved (multi-agent spawn_agent, model-switch hijack, queue machinery), upstream features adopted (tool-approval flow, stream generations, send-states). Commit `14171121`. Boot-verified: 69 routes mount, all Python compiles, all touched JS parses.

**Send-gate hotfix (same day):** the merge resolution dropped upstream's synchronous stream-registration block in `static/js/chat.js` (`streamSessionId`/`streamGeneration` declarations, `_streamGenerations.set`, `_sendStates` install, `_streamRunIds.delete`) while keeping every check that reads them — first send threw `ReferenceError` after the busy-flags were set and before the try/finally, wedging every tab busy forever: all later submits queued into the bubble, nothing ever POSTed. Restored the block verbatim (upstream ~1465-1484), kept the ODYS-HIJACK debug line (relocated below the declarations). Verified: TDZ-clean, `node --check` OK, served file confirmed over HTTP.

- Cache busters bumped `v=20261023merge1` → `v=20261023merge2` across 41 static files; `sw.js` `CACHE_NAME` → `odysseus-v393-20261023merge2` (the old tag was already cached by Sir's tab — a plain reload would have served the broken corpse).
- Header corrected: this log lives in the main tree now, not the garbo mirror.

## 2026-10-21 — docs(tools): spawn_agent description audit — encode blocking-vs-background guidance

Cold-start audit of the `spawn_agent` tool descriptions (schema / fence catalog / RAG index) found the original wording promised "parallel work" without saying parallelism only exists via `background: true` — a trap given blocking spawns run strictly serially (measured 2026-10-20: two concurrent calls, zero overlap, ~7s harness overhead between them). Reworded all three surfaces:

- Dropped "parallel work across different models" from blocking-mode use cases; added the explicit fact: **"Blocking spawns run one at a time and park this conversation until the report returns — for anything slow, or several agents at once, set background=true."**
- `background` param now carries the when-to-use heuristic: prefer true for long-running tasks or several agents at once; keep false only for quick lookups.
- Fence catalog + RAG index updated to match. `data/TOOLS.md` / `docs/TOOLS.md` self-sync via `tools_doc.py` on next app start.

No behavior change — description text only. Takes effect on next restart.

Files touched: `src/tool_schemas.py`, `src/agent_loop.py`, `src/tool_index.py`
Verified: py_compile clean; new wording present in all 3 surfaces; old "parallel" wording 0 matches.

## 2026-10-20 — feat(agents): background sub-agents — Tier-2 multi-agent (fire-and-forget + auto-delivery)

`spawn_agent` gains **`background: true`**: the tool returns an agent id **immediately** and the sub-agent runs as an asyncio task while the parent keeps working. When the worker finishes, an always-on monitor delivers the report by **re-invoking the agent in the parent session** (the bg_monitor "auto-continue" pattern) — the parent doesn't even need to poll. Active polling is also available via the new **`check_agents`** tool (list jobs / collect finished reports; finished results are delivered exactly once and marked collected).

This closes the Tier-1 gap measured earlier tonight: two concurrent `spawn_agent` calls from one turn executed **serially** (harness runs tool calls sequentially — verified with overlapping 8s sleeps: 23s wall for 16s of work). Background launches are genuinely concurrent (shared 3-slot semaphore with blocking spawns) and kill the per-call harness round-trip overhead.

New module **`src/agent_jobs.py`** (mirrors `bg_jobs.py` + `bg_monitor.py` where it fits):
- **Registry** `data/agent_jobs.json` (atomic writes). Finished results survive a restart; RUNNING entries can't (asyncio tasks die with the process), so on load they're marked `interrupted` and still get a follow-up — the parent always hears back.
- **Delivery semantics**: exactly-once via the `delivered` flag; set only AFTER the follow-up run succeeds (transient failures retry on the next 5s tick). Busy-deferral: never writes into a session mid-stream (`agent_runs.is_active` check, bg_monitor parity). If the continuation produces nothing, the raw report is delivered as the bubble so the result always reaches the user.
- **Follow-up injection**: `[Background agent <id> finished — status: …]` + task + report into the parent session, then a headless continuation (max 12 rounds, reusing `bg_monitor._drain_agent`), persisted as a normal assistant turn with `tool_events` metadata (frontend renders standard tool cards).
- **Bounded**: delivered entries pruned after 1h; hard cap 40 stored jobs (oldest delivered evicted first — undelivered results are the precious ones).
- **Worker** = existing `run_subagent()` (same depth/semaphore/round/timeout guards); model resolution extracted into `_resolve_subagent_model()` and `run_subagent` gained `preresolved=` so background launches resolve the model **eagerly** — a bad model spec fails at launch time instead of leaving a dead job.

Files touched:

- **`src/agent_jobs.py`** — new: registry, `launch_background_agent()`, `_run_agent_job()` worker wrapper, delivery monitor (`start_agent_job_monitor()`), `collect_status()` for check_agents, `_reset_for_tests()`.
- **`src/agent_tools/spawn_agent_tools.py`** — `background` branch in `SpawnAgentTool` (returns launch message immediately); new `CheckAgentsTool`; `_resolve_subagent_model()` extraction + `preresolved` param on `run_subagent`.
- **`src/agent_tools/__init__.py`** — `TOOL_HANDLERS["check_agents"]`, `TOOL_TAGS`.
- **`src/tool_schemas.py`** — `background` property on the spawn_agent schema; `check_agents` schema; `_REQUIRED_NATIVE_TOOL_ARGS["check_agents"] = ()`; args→content conversion.
- **`src/tool_parsing.py`** — same conversion in `_raw_openai_tool_call_to_block`.
- **`src/tool_execution.py`** — `check_agents` dispatch branch.
- **`src/tool_index.py`** — RAG description + "delegate to" intent cluster.
- **`src/agent_loop.py`** — `TOOL_SECTIONS`: spawn_agent entry updated (background documented) + `check_agents` entry; all-tools-catalog exclusion set.
- **`src/constants.py`** — `AGENT_JOBS_FILE`.
- **`app.py`** — `start_agent_job_monitor()` at startup, next to `start_bg_monitor()`.
- **`data/TOOLS.md` + `docs/TOOLS.md`** — regenerated automatically by `src/tools_doc.py` from the schemas/catalog (discovered tonight: the docs are self-syncing — no manual edits needed anymore).
- **`tests/test_agent_jobs.py`** — new: 18 tests (persistence, interrupted-on-restart, launch lifecycle incl. fail-fast bad model + failed/timeout mapping, exactly-once collection, pruning, follow-up deliver/defer/skip/retry paths).
- **`tests/test_spawn_agent.py`** — +5 tests (background param registration, background branch + error passthrough, check_agents tool).

Verified: full suite 4843 passed / 32 failed — failure list **byte-identical to the pre-existing red set** (stash-isolated earlier today); zero new failures. Restart required to load (no `--reload`).

## 2026-10-20 — feat(agents): `spawn_agent` tool — Tier-1 multi-agent primitive (delegation with tools)

New agent tool `spawn_agent`: the agent can now spawn a **sub-agent** — a fresh `stream_agent_loop` with full tool access, run headless mid-parent-turn — and receive the sub-agent's final report as the tool result. This is the missing tier between `chat_with_model` (bare completion, no tools) and scheduled tasks (headless but not parent-delegable): the parent delegates a self-contained subtask, the sub-agent works with tools (bash, web, files, …), and only the final report returns to the parent's context. Foundation for Tier-2 fan-out / agent teams.

Semantics: model resolution order is explicit `model` arg → `subagent_model` setting → **parent's own endpoint/model** (fresh context, same brain — threaded via the new `extra_ctx` on `execute_tool_block`). Params: `task` (required), `model`, `system_prompt` (persona), `max_rounds` (default 15, hard cap 30), `timeout_minutes` (default 10, hard cap 30). The report is truncated at 12k chars and carries a compact `[sub-agent tools used: …; rounds: N]` footer so the parent keeps situational awareness without the sub-agent's full transcript.

Guards (fork-bomb prevention, two independent locks on the recursion door):
- **Depth limit**: inner loop gets `spawn_agent` in `disabled_tools` (hidden from its catalog via `_assemble_prompt` AND blocked at its execution gate), plus the handler refuses when `ctx["subagent_depth"] >= 1` (new `_subagent_depth` param on `stream_agent_loop`, threaded through `extra_ctx`). Depth 1 only in v1; Tier 2 relaxes by decrementing.
- **Concurrency**: module semaphore caps simultaneous sub-agents at 3; extra spawns queue inside the caller's timeout budget.
- **No interactive gate**: deliberately NOT calling `wait_for_interactive_quiet` — the parent IS the interactive run, waiting would deadlock. Inference-server contention is the server's problem.
- Synthetic session id (`<parent>-subagent-<hex>`) → local cache-slot affinity only; no DB rows, no collision with the parent's active run (run registration lives in chat_routes, not the loop).

**Companion fix (agent_loop)**: the low-signal fast path (`_direct_low_signal`) was stripping tools from sub-agent runs whenever the task *text* read like small talk — a delegated "count the files" got answered as casual chat with zero tool access. Sub-agents (`_subagent_depth > 0`) now always take the full tool path: a delegated task is explicit work by definition, never small talk.

Files touched:

- **`src/agent_tools/spawn_agent_tools.py`** — new: `run_subagent()` + `SpawnAgentTool` handler (headless SSE-event consumption mirroring task_scheduler's `_run_agent_task`, grace fallbacks, timeout via `asyncio.timeout`, `CancelledError` propagates on parent stop).
- **`src/agent_tools/__init__.py`** — registry: `TOOL_HANDLERS["spawn_agent"]`, `TOOL_TAGS`.
- **`src/tool_schemas.py`** — native function schema, `_REQUIRED_NATIVE_TOOL_ARGS["spawn_agent"] = ("task",)`, args→JSON content conversion in `function_call_to_tool_block`.
- **`src/tool_parsing.py`** — same conversion in `_raw_openai_tool_call_to_block` (leaked-OpenAI-blob path).
- **`src/tool_execution.py`** — `extra_ctx` param threaded through `execute_tool_block`/`_execute_tool_block_impl`/`_document_tool_dispatch`; `spawn_agent` dispatch branch.
- **`src/agent_loop.py`** — `_subagent_depth` param; `extra_ctx={"endpoint_url", "model", "headers", "subagent_depth"}` at the `execute_tool_block` call site; `TOOL_SECTIONS` catalog entry; all-tools-catalog exclusion set; `_direct_low_signal` sub-agent exemption (the companion fix).
- **`src/tool_index.py`** — RAG description + added to the "delegate to / ask another model" intent cluster.
- **`data/TOOLS.md`** — full tool-reference section (the catalog one-liner points here).
- **`tests/test_spawn_agent.py`** — new: 8 tests (registry wiring, native-call conversion + required-args rejection, JSON/raw/malformed content parsing, catalog visibility + recursion-guard hiding, depth guard, empty-task refusal, and an end-to-end sub-agent run against a faked native-tool-call stream proving tool execution + report round-trip).

Verified: `py_compile` all touched files (system + venv); `tests/test_spawn_agent.py` 8/8. Full suite: 4807 passed, 32 failed — the 32 are byte-identical to the pre-existing failure set (stash-isolated before/after comparison; includes the long-red `MAX_OUTPUT_CHARS` 10000-vs-50000 test constant drift, the JS/node suites, and the low-signal/workspace tests this change deliberately does not touch). Note for whoever next pokes the low-signal area: `test_workspace_confine` and `test_tool_policy` failures predate this change (verified via stash on a clean tree).

## 2026-10-16 — feat(llm): `thinking_enabled` master toggle (Settings panel / settings.json / in-bot)

New master switch for reasoning/"thinking" mode across every backend, settable three ways: the Settings panel's new **Thinking** card, `data/settings.json` (`"thinking_enabled": true|false`), or the in-bot settings tool ("set thinking off"). Default ON (current behavior). Read via the TTL-cached settings loader, so flips take effect within ~2s without a restart. Internal utility calls (compaction, summaries, titles) pass `disable_thinking=True` explicitly and are unaffected — they stay thinking-off whether the toggle is on or off.

Files touched:

- **`src/settings.py`** — `DEFAULT_SETTINGS["thinking_enabled"] = True` (also makes the key legal for POST /settings and visible to the panel GET).
- **`src/llm_core.py`**
  - `_thinking_setting_off()`: reads the toggle; any settings-read failure keeps thinking ON (a broken settings file must not silently change model behavior).
  - Fold points: sync `llm_call` computes `no_think` and threads it into the Ollama payload (`think: false`), Mistral (`reasoning_effort: "minimal"`), DeepSeek (`force=True`), and the generic OpenAI-compat branch; `llm_call_async` folds the toggle into its existing `disable_thinking` param (which also suppresses the `reasoning_content` response fallback); `_stream_llm_inner` (main chat stream) does the same.
  - `_apply_thinking_off_openai_compat()`: per-provider switches for backends without a dedicated knob — NVIDIA NIM + self-hosted vLLM/llama.cpp get `chat_template_kwargs: {"enable_thinking": false}` (vLLM template switch; NVIDIA's docs document it for NIM reasoning models — verified against NVIDIA docs 2026-10-16), OpenRouter gets `reasoning: {"enabled": false}`, Groq gets `reasoning_effort: "none"`, api.openai.com reasoning families floor at `reasoning_effort: "minimal"`. Unknown strict clouds get NOTHING (an unrecognized field risks a hard 400 on every request — worse than a model that keeps thinking).
  - `_disable_deepseek_v4_thinking()` now also **scrubs `reasoning_content` from request history** when it disables thinking: the pass-back contract only exists while thinking is ON, and DeepSeek rejects `reasoning_content` fields on thinking-disabled calls. Runs last (payload build), so it wins over sanitize's metadata.thinking promotion. This also fixes the long-red committed test `test_sanitize_promotes_metadata_thinking.py::test_disable_thinking_scrubs_reasoning_from_payload` (spec was committed, implementation never landed).
- **`src/agent_tools/admin_tools.py`** — settings-tool aliases: "thinking", "thinking mode", "reasoning", "reasoning mode" → `thinking_enabled`.
- **`static/index.html`** — Thinking admin-card (switch + explainer) above the Teacher Model card.
- **`static/js/settings.js`** — `initThinkingToggle()` (loads via GET /api/auth/settings, saves on change), called from the settings init sequence.
- **`tests/test_thinking_toggle.py`** — new: 12 tests (toggle read/defaults/broken-settings survival, per-provider payload switches, DeepSeek force-vs-env semantics).
- **`tests/test_llm_core_ollama.py`, `tests/test_llm_core_ollama_thinking.py`** — repaired stale monkeypatch targets left by the earlier `get_context_length` → `get_context_length_known` tuple migration (the tests predated the rename and died on AttributeError before reaching their assertions); the 4 TestThinkSuppression + 2 num_ctx tests are green again, which also proves the toggle threading didn't disturb think-suppression.

Verified: `py_compile` (llm_core/settings/admin_tools) + `node --check settings.js`; `test_thinking_toggle.py` + `test_sanitize_promotes_metadata_thinking.py` + `test_llm_core_reasoning_content_fallback.py` + `test_llm_core_ollama.py` + `test_llm_core_ollama_thinking.py` = 66 passed (incl. the previously-red scrub test). Remaining failures in the wider thinking/reasoning/ollama sweep are pre-existing and unrelated: cookbook-docker ×2 (docker env), JS rendering ×2 + web-search ×3 (`No module named 'markdown'` in the test env), history_compact ×2 (known, stash-isolated in the 2026-10-1x session). Requires app restart to take effect (live procs predate the patch); the toggle itself flips live (~2s TTL) once loaded.

## 2026-10-12 — fix(agent): stopped agent turns keep executed tool calls (the "defenestration" fix)

Root cause: `tool_events`/`round_texts` accumulated inside `stream_agent_loop` only escaped via the final `metrics` event at turn completion. A force-stopped turn (client cancel / disconnect / upstream error) killed the generator before that event fired, and `_persist_stream_partial` saved text+thinking only — every tool call that had *actually executed* was dropped from the saved row, and the frontend (which rebuilds segmented bubbles from `metadata.tool_events` + `metadata.round_texts`) rendered the remainder as one glued narration blob. A history full of narration-without-calls rows also teaches the next model a fabricated house style (the 2026-10-11 "poisoned chat" saga — GLM 5.3 AND Kimi K3 affected).

Files touched:

- **`src/agent_loop.py`** — `stream_agent_loop` gains `partial_sink: dict | None = None`. Right after `tool_events`/`round_texts` are created it publishes live references into the sink (both lists mutate in place, so the sink stays current for the whole run); the per-delta handler mirrors the in-flight round's text into `partial_sink["current_round_text"]`, reset at round start and after each round's text is appended (so a cancel during tool execution can't double-count a round).
- **`routes/chat_routes.py`** — new `_sink_tool_state()` snapshots (tool_events, round_texts) from the sink, appending the in-flight round's partial text; `_persist_stream_partial` accepts `tool_events`/`round_texts` and stores them in the saved row's metadata; the agent branch creates `_partial_sink`, passes it into the loop, and all three partial-save paths (stream ended without [DONE], client disconnect, upstream error) plus the 4s draft checkpoint now snapshot tool state — so even a server crash mid-turn finalizes with tool records intact.

Verified: `py_compile` both files; new `tests/test_partial_tool_events.py` (6 tests, incl. an end-to-end early-`aclose()` drive of the real loop asserting the executed bash call survives in the sink); `test_agent_loop.py` + `test_tool_task_cancelled_on_disconnect.py` + `test_chat_metrics.py` green — 66 passed. Requires app restart to take effect (live 7001 procs predate the patch). NOT yet ported to `odysseus-2c8e00c`/`odysseus-3d3aee2` — port during the tweaks grind.

## 2026-08-11 — fix(db): SQLite WAL + busy_timeout + draft-checkpoint lock retry (agent streams dying with "database is locked")

Root cause: the engine ran SQLite in the default **rollback-journal** mode with **no busy_timeout** (the 5000ms seen live was just Python's sqlite3 default). Rollback-journal takes an EXCLUSIVE lock at every commit that blocks concurrent readers AND writers — with several agent sessions checkpointing draft rows every ~4s (`chat_routes._checkpoint` → `session_manager.update_draft` → `db.commit()`), one slow transaction starved the rest past the timeout and the whole `agent_runs` stream died with `sqlite3.OperationalError: database is locked` (session 9717a423, 2026-08-11 16:19).

Files touched:

- **`core/database.py`**
  - `set_sqlite_pragma` connect listener: added `PRAGMA busy_timeout=30000` (wait on contended writes instead of failing instantly) and `PRAGMA synchronous=NORMAL` — applied only when the connection sees WAL active, so pre-WAL connections (init_db's create_all) keep FULL for rollback-journal safety.
  - New `_enable_sqlite_wal()`: switches the DB to WAL once per startup (idempotent, AUTOCOMMIT because journal_mode can't change inside a transaction; no-op for Postgres/in-memory; non-fatal on failure). Called at the top of `init_db()`. WAL lets readers run concurrently with the single writer and turns commits into a fast -wal append instead of an exclusive-lock dance. Sidecar 0o600 lockdown already covered `-wal`/`-shm`.
- **`core/session_manager.py`** — new `_commit_draft_with_retry()` wraps `create_draft`/`update_draft`: on `OperationalError` containing "locked", rollback + retry up to 4 attempts with 0.1/0.2/0.4s backoff, each attempt on a fresh session (poisoned connections never reused). Non-lock errors propagate immediately; the "row vanished → return False" contract is preserved. Belt-and-suspenders so a rare collision never kills a live reply.

Verified: `py_compile` both files; retry-helper logic tested in isolation (lock-then-success, persistent lock, non-lock error, False propagation, session freshness/close); 47 existing session/database tests pass. Requires app restart to take effect (engine-level pragmas are per-process).

## 2026-08-09 — fix(desync): rolling idle timeout + post-abort convergence (stream/UI desync #2)

The "refreshing the page shows something new" desync. Root cause: chat/agent streams
are **detached** (`agent_runs.start` + subscriber SSE), so when the browser kills an
*alive-but-silent* connection, the server run keeps going and saves the full reply —
the page shows a frozen partial + note, refresh reveals the finished message.

Two frontend fixes (`static/js/chat.js`, frontend-only — no server restart):

- **A. Rolling idle timeout.** The 120s/360s abort timer was armed ONCE at send and
  only cleared on whitelisted JSON content events — so a silent-but-alive turn (long
  prefill, provider hiccup, quiet tool run) was aborted by the browser itself, even
  while the server's `: heartbeat` SSE comments were flowing. Now `_armIdleTimeout()`
  re-arms on EVERY reader byte (deltas, tool events, and heartbeat comments alike),
  so only a stream with genuinely no bytes (dead connection) trips it. The permanent
  `clearResponseTimeout()` on first content event is removed; completion/error paths
  still disarm permanently.
- **B. Post-abort convergence** (`_convergeAfterAbort`). After a non-user abort
  (timeout / offline / recovery / stale-local), the page now probes
  `/api/chat/stream_status/{id}` and:
  - run still active → `resumeStream()` re-attaches and finishes it live (stale
    partial bubble removed; plain replies finalize in place, rich replies reload
    from DB);
  - run done/dead → quiet `selectSession(..., { showLoading: false })` re-render so
    the view converges to whatever was actually saved — no refresh needed;
  - server unreachable (offline) → note stays.
  User-initiated stop and navigation aborts intentionally do NOT converge.

Verified: `node --check` clean; backup at `static/js/chat.js.bak-20260809-desyncfix`.
Static serving is `Cache-Control: no-cache` + ETag (app.py `_RevalidatingStatic`) and
the SW is network-first for JS — a normal browser reload picks it up, no cache clear.


## 2026-08-09 — feat(compactor): adaptive summary budget + finish_reason truncation detection

Follow-up to the CoT fix. The 2048 cap is a floor now, not a ceiling: `max_tokens`
scales with the size of the summarized half (`older_tokens // 8`, clamped to
[2048, 4096]) so a big coding-session compaction gets real room while a small chat
stays cheap — and the summary can never re-consume more than ~12.5% of the context it
just freed (unbounded summaries would re-fill the window and skew the next split).

Truncation was previously silent: a summary cut at max_tokens amputated its tail
(usually "Pending / Next Steps"). Now:
- `src/llm_core.py`: `llm_call_async(..., return_finish_reason=True)` returns
  `(text, finish_reason)` instead of bare text (default unchanged; cached/streamed
  responses return `None` = untruncated). New `_extract_finish_reason` helper maps
  OpenAI-compat `choices[0].finish_reason`, Anthropic `stop_reason`, Ollama
  `done_reason`.
- `src/context_compactor.py`: `SUMMARY_MAX_TOKENS_HARD=4096`,
  `SUMMARY_REPLACE_FRACTION=8`; the summary prompt announces the actual `{budget}`.
  On `finish_reason in ("length", "max_tokens")`: one retry at the 4096 ceiling when
  the budget was below it; if still truncated, the persisted summary gets a visible
  "[Summary truncated at max tokens]" marker. Tolerant of stub/bare-string callers.
- `tests/test_context_compactor.py`: `TestMaybeCompactTruncationAndBudget` (floor /
  scaling / ceiling / retry-then-mark / mark-without-retry / untruncated) +
  `test_summary_hard_cap`, `test_budget_placeholder`.
- `tests/test_llm_core_reasoning_content_fallback.py`: tuple-return integration
  tests + `_extract_finish_reason` unit tests for all three provider shapes.
- Verified: context_compactor + llm_core suites 309 passed (was 298+11). Pre-existing
  failures confirmed unrelated via stash-isolation: `test_history_compact_tool_calls.py`
  ×2, `test_kv_cache_invalidation_2927.py` ×2 (uncommitted chat_helpers.py work from
  earlier today), `test_review_regressions.py` ×3 batch-order pollution (pass isolated),
  `test_agent_loop_tool_output_truncation.py::test_default_limit_matches_constant`
  (50000 vs 10000 drift).

## 2026-08-09 — fix(compactor): summaries are no longer cut-off chain-of-thought; bigger, safer summary budget

Root cause (session observed at "Turns summarized: 52 | Compactions so far: 2"): the
compaction summary was the model's internal monologue — "We need to produce the
conversation summary. Need to capture the prior summary… We're at turn 52?" — sliced
mid-thought at the 1024-token cap, so the third compaction persisted zero real summary.
Chain: the session model `deepseek-v4-flash-free` (via OpenCode Zen) runs with thinking
ON (`.env` sets `ODYSSEUS_DEEPSEEK_V4_THINKING=1`); a thinking DeepSeek call returns
`content=""` + `reasoning_content=<CoT>`; `llm_call_async`'s `content or reasoning_content`
fallback returned the CoT as the "summary"; `max_tokens=1024` then cut it off mid-word.

Fixes:
- `src/llm_core.py`: new `disable_thinking` param on `llm_call` / `llm_call_async`
  (and `_build_ollama_payload`): forces thinking off even when
  `ODYSSEUS_DEEPSEEK_V4_THINKING=1` (`_disable_deepseek_v4_thinking(force=True)`,
  Mistral `reasoning_effort="minimal"`, Ollama `think: false`) AND suppresses the
  `reasoning_content` response fallback — a compact/summary caller can never receive
  chain-of-thought as its result. Default `False` keeps existing behavior everywhere else.
- `src/context_compactor.py`: auto-compaction now calls the summarizer with
  `disable_thinking=True`; `SUMMARY_MAX_TOKENS` 1024→2048 (prompt guidance 1000→1500);
  `normalize_compaction_summary` strips `<think>`/`<mm:think>` blocks (defense-in-depth
  for gateways that serve reasoning as content tags); per-message `[:2000]` head-only
  cut replaced by `_message_excerpt` (head+tail, so the end of long messages — where
  decisions land — survives) and `_build_convo_text` caps the summarizer INPUT to ~55%
  of the summary model's own context window, dropping the OLDEST messages first with a
  visible notice; an empty/CoT-only summary now fails gracefully (`was_compacted=False`,
  history untouched) instead of persisting garbage and dropping the older half.
- `routes/session_routes.py`: manual `/session/{id}/compact` gets the same treatment
  (`disable_thinking=True`, `SUMMARY_MAX_TOKENS`, `_build_convo_text` budget, empty-summary
  → 500 instead of silently writing a blank summary).
- `tests/test_context_compactor.py`: `SUMMARY_MAX_TOKENS==2048`; new regression classes
  `TestStripThinkBlocks`, `TestNormalizeCompactionSummary`, `TestMessageExcerpt`,
  `TestBuildConvoText`, `TestMaybeCompactReasoningRegression` (forces thinking off, empty
  summary skips gracefully, CoT never persisted).
- `tests/test_review_regressions.py`: stub `core.log_safety` in
  `_install_model_route_import_stubs` (pre-existing gap: 6 tests failed with
  ModuleNotFoundError whenever anything imported `routes/model_routes.py`).
- Verified: `tests/test_context_compactor.py` 34 passed; llm_core/agent_loop suite 244
  passed; combined 78 passed. `test_history_compact_tool_calls.py` 2 failures are
  pre-existing (fail on the untouched tree too — in-flight history_routes refactor).

## 2026-08-09 — fix(agent): generalized passive tool-hallucination guard — Round-7 narration lies now get flagged on every model

Root cause: session `f86b3f11` Round 7 (message `bb73d622`, model deepseek-v4-flash-free)
was a 3,488-char pure-narration work-log ("Reading the exact text… Full Rule 9
captured… Backup confirmed… Applied… Auditing the invariants", invented
`.bak-2026-08-09-r7-hitl` + word counts 727→648) with **0 fenced tool blocks and
0 tool_events**. The model reproduced the work-log SHAPE of prior real tool-using
rounds without ever firing the tool channel. Existing defenses were narrow or soft:
the "act, don't narrate" prompt text is soft; `_FAKE_SUCCESS_RE` /
`_looks_like_success_claim` + `_looks_like_destructive_request` were only wired to
the odysseus-qwen3 finetune; the completion-verifier subagent is off by default AND
skips 0-tool turns. Nothing detected "prose claims tool actions that never ran" for
general models.

Fixes (all in `src/agent_loop.py`; backup `src/agent_loop.py.bak-2026-08-09`):
- NEW `_EFFECTFUL_REQUEST_RE` (broadened with compress/cut/trim/shorten/tighten/…
  the actual task verbs), `_TOOL_CLAIM_STRONG_RE` (world-action verbs only — read/
  captured/backup/applied/edited/sent/fetched/… with NO in-head text verbs),
  `_looks_like_effectful_request`, `_looks_like_tool_claim_narration` (requires
  **>=2 DISTINCT strong verbs** — the work-log shape; honest openers like
  "I read your message and checked the details" / "it's fixed" / "I created a
  summary" carry at most one strong verb → no flag), and
  `_recent_user_request_is_effectful` (scans back over SUBSTANTIVE >=20-char user
  messages — bare nods "sure"/"sur"/"ye"/"good" are skipped, so a nod inherits the
  real task that sat a dozen turns back; the Round-7 window's "compress it" task was
  13 nod-style messages up).
- Guard fires for ALL models when: `not tool_events` AND recent request was
  effectful AND the reply narrates >=2 distinct world actions → `logger.warning`,
  append visible "⚠ Described tool actions did not execute — no tool ran this turn.
  Flagged by the tool-verification guard." (streamed as a delta, so the live bubble
  and the saved reply both carry it exactly once), and stamp metadata
  `tool_claims_unverified: true` on the metrics event → rides into the saved
  message's metadata for programmatic detection. Passive only: no correction loop,
  no fabricated results, no tool re-runs. The odysseus-qwen3 destructive-request
  REPLACEMENT branch is untouched.

Verified: `py_compile` clean; 11-case narration unit table (Round 7 + "searched +
downloaded" + "read + edited" + "sent + archived" flag; read+checked, fixed+verified,
created-summary, updated+saved, single-strong and pure-greeting replies don't);
real-session window scan (Round-7 nod window inherits the "compress it" task = True;
pure-chat nod window = False); end-to-end gate fires on Round 7 with
`tool_events=[]` and stays silent on the chat FP. Status: NEEDS RESTART (src change).

## 2026-08-09 — fix(context): honest context accounting + context-window override — the 1M lie and the thinking-blind estimate

Root cause of "~114k input tokens per turn while the header says 11k": the compactor
and the header both relied on `estimate_tokens(messages)` which counted ONLY `content`
+ `tool_calls` — the accumulated `metadata.thinking` pass-backs (~265k chars ≈ 79.6k
tokens on session `f86b3f11`, re-sent as `reasoning_content` on EVERY request) were
invisible. Measured: transcript estimate 11,291 vs 114,012 provider-counted. Second
half: `_lookup_known` substring-matched `deepseek-v4-flash-free` to
`KNOWN_CONTEXT_WINDOWS['deepseek-v4'] = 1048576` (the endpoint's advertised 1M), so
the compactor threshold was 85% × 1M = 891k → it could NEVER fire before the model's
real 200K window was blown. Backups: `src/model_context.py.bak-20260809-ctxoverride`,
`data/settings.json.bak-20260809-ctxoverride`.

Fixes (all in `src/model_context.py` + `data/settings.json`):
- `_context_length_override(endpoint_url, model)` — NEW settings key
  `model_context_overrides` (dict: exact model id, or `model@endpoint`/`endpoint@model`
  → int). Checked FIRST in `_get_context_length_cached`, before cache/known table/
  endpoint /models claim. A user pin beats a lying proxy.
- `estimate_tokens` — now counts `reasoning_content` / `metadata.thinking`
  pass-backs (string or text-part list). The header, compactor, and trim gates all
  feed off this, so they're honest now: session f86b3f11 reads 90,859 (53.4% of the
  170k threshold) instead of 11,291 (1.3% of a phantom 891k).
- `KNOWN_CONTEXT_WINDOWS` — added `'deepseek-v4-flash-free': 200000` (longest-match
  wins over `'deepseek-v4'`), matching the actual 200K serving cap.
- `data/settings.json` — `model_context_overrides: {"deepseek-v4-flash-free": 200000}`
  pinned for this instance.

Verified: 7/7 functional checks (override wins w/o network, known-table longest-match,
non-overridden models unaffected, estimate counts metadata.thinking AND
reasoning_content, no-override returns None) + real-session measurement above.
`py_compile` clean. Status: NEEDS RESTART (src + settings.json; settings reloads
within 2s TTL but the code change needs a bounce).

## 2026-08-08 — feat(sync audit): progressive draft checkpoint — a process death mid-turn now loses nothing

LM Studio-style progressive persistence, stapled into the stream path. Backups:
`*.bak-20260808-draftckpt` for all five touched files. Files: `core/session_manager.py`,
`routes/chat_routes.py`, `routes/chat_helpers.py`, `routes/history/history_routes.py`,
`static/js/chat.js`, `docs/FILE_MAP.md`, `docs/ARCHITECTURE.md`.

**The gap it closes:** the 2026-08-08 sync audit guaranteed the partial is saved on
disconnect / upstream error / no-[DONE], but only at *turn end*. If the **server process
itself** died mid-turn (crash, OOM kill, power loss), the only copy of the partial was
the in-memory `_active_streams["partial"]` — gone with the process. LM Studio writes the
in-flight reply to its store continuously; garbo now does the same via DB-only draft rows.

**Lifecycle (metadata `draft: True` marks a draft row):**
- **create** — `SessionManager.create_draft` inserts a DB-only assistant row (never
  touches in-memory history, so the model's context can't see half-written replies).
  First checkpoint fires early (≥150 chars OR first 4s tick) and the stream emits a new
  `draft_saved` SSE event — the frontend stamps the bubble's `dataset.dbId` immediately,
  so deletes/regenerate mid-stream target a real row id.
- **checkpoint** — `_checkpoint()` (nested in `stream_with_save`, both chat + agent
  modes) writes every ~4s via `update_draft` (in-place content/metadata update, FTS AU
  trigger reindexes). Session timestamps/counts are NOT bumped per checkpoint.
- **promote** — on `[DONE]`, `save_assistant_response(..., draft_id=)` calls
  `promote_draft`: the SAME row is updated in place with final content/metadata (draft
  flag dropped), appended to in-memory history, `_db_id` stamped = draft id → the
  frontend's stamped bubble keeps its id and **no duplicate row ever appears**. Same for
  the partial-save paths (`_persist_stream_partial(..., draft_id=)`). Fallback: if the
  draft row vanished (deleted mid-stream), promote falls back to a fresh persist.
- **orphan finalize** — if the process dies, the draft is all that survives. The history
  reader (`_entry_or_none`/`_finalize_or_hide_draft`) and `_db_to_session` hydration
  finalize orphans lazily: drop the draft flag, set `stopped: True` → renders as a
  resumable "[Message interrupted]" partial. Live drafts (status streaming in
  `_active_streams`) are hidden from history + hydration until promoted.

**Verify:** 40/40 harness checks (`Sandbox/draftckpt_verify.py`) against the real
SessionManager + temp SQLite: create/update/promote same-id/no-duplicate, fallback
persist, orphan finalize, partial-save + save_assistant_response draft-aware promote,
FTS sync after promote (no draft-only partials indexed post-promotion), paged-history
policy (live hidden, orphan shown stopped), and restart hydration (orphan enters memory
stopped, zero draft-flagged rows → no context pollution). `py_compile` + `node --check`
clean.

**Needs restart.** Docs-only round for the old fork's ODYSSEUS-CHANGES.md? No — this is
code; uvicorn 7001 must bounce.

## 2026-08-08 — docs(sync audit): ARCHITECTURE.md refreshed for the partial-save rework

Docs-only follow-up after the sync-audit fix landed and uvicorn restarted (7001, pid
298279, started 23:20 — after the 22:55 patch, so the live server runs the new code):

- `docs/ARCHITECTURE.md` §2.3 chat_stream bullet now documents the **turn-persistence
  guarantee** (`_persist_stream_partial` on disconnect / upstream exception / no-[DONE]
  end, reasoning kept in `metadata.thinking`, reasoning-only partials persist).
- `docs/ARCHITECTURE.md` transplant-receipts row `no-[DONE] rescue / thinking-only
  saves` flipped from `ALREADY IN GARBO` (`_stopped_content`/`_stopped_md`) to
  `REWORKED 2026-08-08` (`_persist_stream_partial` + `_saw_done`/`_saved_this_turn`).
- `docs/FILE_MAP.md` already updated during the fix round (chat_routes / history_routes
  rows, 2026-08-08).

**Files:** `docs/ARCHITECTURE.md` (only).

## 2026-08-08 — feat(sync audit): unfinished turns always persist (reasoning included), reasoning-only replies no longer double-render, hidden continue-handshakes stop ghosting on refresh

**Requested by Sir (2026-08-08):** "Go audit the Odysseus files. I want it so the Front-end and Back-end are *completely* syncs. All reasoning thoughts stay in bubbles how it's received, all messages are saved/cached so they aren't lost if something errors out mid-turn, deletes on the front-end happen on the back-end, etc etc. Basically, LM Studio's way of doing it, stapled into Odysseus."

**Audit findings (code trace + DB/log forensics, 2026-08-08):**
1. **Disconnect partial-save dropped reasoning entirely.** Both modes' `CancelledError`/`GeneratorExit` handlers saved only `full_response` via `clean_thinking_for_save` — the streamed `thinking_response` (the flagged `{delta, thinking:true}` channel) was discarded, so a mid-reasoning disconnect lost the think bubble on refresh. And a *reasoning-only* disconnect (`full_response == ""`) saved **nothing at all** — the turn vanished from the DB.
2. **Mid-stream upstream exceptions persisted nothing.** A provider 5xx/transport error/parse crash propagated out of `stream_with_save` → SSE died, the frontend kept the partial visually, but refresh lost it (the user-message row survived; the assistant partial never hit the DB). Same for a stream that ended without `[DONE]` (provider error event / silent close).
3. **Reasoning-only replies double-rendered on refresh.** The empty-completion path saved `thinking_response` as the message CONTENT *and* into `metadata.thinking` → chatRenderer's refresh rebuild drew the reasoning twice (bubble + raw text), unlike the live view (bubble only).
4. **Auto-recover / step-limit handshake user messages ghost on refresh.** `_tryAutoRecover` and the rounds-exhausted Continue set `_hideUserBubble = true` but still *persisted* the handshake user row. The user-stop Continue was cleaned up by merge-last-assistant (marker match), but the auto-recover ("The stream dropped before you finished…") and step-limit ("You hit the step limit before finishing…") texts were NOT matched → the hidden handshake reappeared as a mystery user bubble after refresh.

**Fix (`routes/chat_routes.py`):**
- New `_persist_stream_partial(sess, session_manager, session_id, full_response, thinking_response, *, model, requested_model, extra)` — the single save path for every "turn didn't finish" branch: preserves reasoning in `metadata["thinking"]`, persists reasoning-only partials (empty content + thinking metadata), rides `stopped: True` so the refresh rebuild shows the "[Message interrupted]" + Continue affordance. Both chat and agent modes use it.
- Disconnect handlers (both modes): now save when `full_response OR thinking_response` is non-empty (reasoning-only disconnects no longer vanish), with reasoning included in metadata.
- New generic `except Exception` after the disconnect handler (both modes): persists the partial with `stream_error` metadata, then re-raises so the SSE terminates and the client shows the error over the preserved partial.
- New post-loop guard (both modes): if the stream ends without `[DONE]` and nothing was saved, persist the partial (`stream_error: "stream ended without completion"`) — covers provider error events and silent closes.
- `_saw_done` / `_saved_this_turn` bookkeeping prevents double-saves across the [DONE] / disconnect / error / no-done branches.
- Reasoning-only empty completions (both modes): content saved EMPTY, reasoning only in `metadata["thinking"]` — refresh renders exactly the live view (bubble only). Genuinely-empty completions keep the no-response marker.

**Fix (`routes/history/history_routes.py`):**
- Shared `_CONTINUE_HANDSHAKE_MARKERS` tuple (user-stop / auto-recover / step-limit texts) used by BOTH the in-memory merge and the DB-side `_merge_continue_rows_to_delete` — the hidden handshake user row is now removed when the two assistant rows merge, in memory and DB alike. Also hardened both match sites with an `isinstance(content, str)` guard so multimodal (list) content can't TypeError the endpoint.

**Verified (2026-08-08):** `py_compile` clean on both files. 18/18 functional checks against a REAL `SessionManager` + temp SQLite (`Sandbox/sync_audit_verify.py`): text+thinking partial → content + metadata.thinking + stopped; reasoning-only partial → empty content + thinking metadata; both-empty → no row; reasoning-only save via `save_assistant_response` → empty content + thinking + `_db_id` stamped; merge-last-assistant endpoint with the auto-recover handshake → handshake removed from DB AND in-memory, merged content correct; `_merge_continue_rows_to_delete` matches all three handshake texts, refuses a normal user message, and survives non-str content.

**Files:** `routes/chat_routes.py`, `routes/history/history_routes.py`, `docs/FILE_MAP.md`.
**Backups:** `routes/chat_routes.py.bak-20260808-syncaudit`, `routes/history/history_routes.py.bak-20260808-syncaudit`.

**Status: NEEDS RESTART** — server code changed (uvicorn on 127.0.0.1:7001 must restart to load; no frontend changes, no hard refresh needed).

**Still open (noted, not patched):** (a) `_active_streams["partial"]` is only a status readback — if the uvicorn process itself dies mid-stream, the partial dies with it; a throttled periodic DB checkpoint of long-running partials (LM Studio-style progressive save) would close that, at the cost of a draft-row promote/dedup path on [DONE]; (b) `/api/rewrite` keeps its own lighter error path (it edits an existing row, not a new turn — no loss class); (c) frontend keeps no local (IndexedDB) partial cache — refresh recovery relies on the detached-run replay buffer + these backend saves.

## 2026-08-08 — fix(chat): reasoning-only rounds no longer explode at the round→tool transition

**Symptom:** during an agent turn, the moment a round ends and a tool starts, the think box
"explodes" — the reasoning dumps out as plain text and the opening `<think>` vanishes
("Thanos-snapped"). Refreshing after the mess showed only the round's message.

**Root cause:** a reasoning-only round (flagged thinking, but the model cut to a tool call
before emitting any reply content) left the marked `<think real="1">…` wrapper **unclosed**
in the accumulated text. The three force-close paths (`[DONE]`, `tool_start`, `agent_step`)
flushed the live box but never appended the wrapper's `</think>`. The finalize then ran
`processWithThinking` on the unclosed block: `extractThinkingBlocks` found **0 blocks**
(verified with the real functions — `normalizePlainThinking` early-returns when the text
contains `<think`, so the unclosed-collapse never fires), and the reasoning rendered as
plain text while the raw marked opener became an invisible DOM tag — exactly the reported
explosion. Additionally `_thinkOpen` was never reset in those paths, so the next round's
first content delta got a stray `</think>` prepended.

**Fix (`static/js/chat.js`):** all three force-close points now append `</think>` to
`accumulated` + `roundText` and reset `_thinkOpen = false`, so the finalize always sees a
closed block (box holds; empty reply renders nothing). Also fixed the `[DONE]` time-embed
regex to match the marked opener (`/<think(?:\s+[^>]*)?>/i` instead of `/<think>/i`).
`agent_step` additionally force-flushes a still-open box so each round keeps its own
`<think>…</think>` per the multi-round design.

**Verified:** extracted the real stored reasoning from the DB, cut it at 300 chars as a
reasoning-only round — before the fix `extract` returned 0 blocks (the dump), after the fix
1 block + empty content (clean box). `node --check` clean. Cache stamps bumped
(`chat.js?v=20260808thinkclose`, sw `v390-thinkclose`). The refresh side was already sound:
history API delivers `metadata.thinking`, the chatRenderer rebuild was verified clean on
real stored data (full reasoning, 0 leftover quoted tags).

## 2026-08-08 — fix(chat): up/down draft-obliteration — old inline recall in app.js finally removed

**Reported by Sir (2026-08-08):** "up/down still obliterates my draft" — after the buttons migration, plain ArrowUp/ArrowDown STILL replaced the composer draft.

**Root cause:** a second, older prompt-recall implementation was still alive inline in `static/app.js` (~line 3930), hidden behind its own guard flag (`messageInput._odysseusPromptRecallCapture`), separate from `composerHistoryRecall.js` (`_historyRecallWired`). It attached an unguarded keydown listener to the composer: plain ArrowUp/ArrowDown → `preventDefault` + `stopImmediatePropagation` → replaced `messageInput.value` with a history prompt, with **no draft save/restore** — the draft was gone, unrecoverable. My module never registers a keydown listener (buttons only), so this was the sole remaining composer killer.

**Fix:** deleted the entire inline block from `app.js` (the `_readComposerPromptHistory()` helper + the `input`/`keydown` listeners). Grep-verified the only remaining ArrowUp/ArrowDown handlers in app.js are the ghost-autocomplete ones, guarded by `if (!active) return` (fire only when a `/command` completion is open — intended UX). slashAutocomplete.js handlers are guarded by `!visible || !items.length` (popup open only) — kept.

**Net effect:** every arrow key (plain, Shift+, Ctrl+, Alt+) on the chat composer is fully native. History recall = ↑/↓ buttons beside the chatbox only.

**Files:** `static/app.js` (−79 lines), `static/index.html` (app.js stamp `?v=20260808draftfix`), `static/sw.js` (`odysseus-v389-draftfix`). Verified with `node --check`.

## 2026-08-08 — feat(chat): prompt-history moved off the keyboard to ↑/↓ buttons beside the chatbox

**Requested by Sir (2026-08-08):** "up/down arrow nukes my draft thing still exists... shift left/right is a legit thing to select text with the text cursor... I depend on all of arrow keys, including paired with ctrl or shift, to move around and shape my request."

**What changed:**
- `static/js/composerHistoryRecall.js` — history recall is now **click-only**: the Shift+Left/Shift+Right keydown binding is gone entirely, so every arrow key (plain / Shift+ / Ctrl+ / Alt+) keeps its native textarea caret/selection behavior. The module builds a small ↑/↓ button stack (`.history-nav`) inserted at the start of `.chat-input-right` and wires the same draft-preserving walk: ↑ walks older prompts, ↓ walks back toward the draft/blank slot. The in-progress draft is still saved on the first ↑ and restored when walking back past the newest prompt. Buttons auto-disable: ↑ when at the oldest prompt (or no history), ↓ when sitting on the draft/blank slot; clicks are ignored while the composer is disabled (stream active).
- `static/js/chat.js` — updated the wiring comment; bumped the module import stamp to `?v=20260808historynav`.
- `static/style.css` — added `.history-nav` / `.history-nav-btn` styles (theme-aware, matches `.input-icon-btn` sizing).
- `static/index.html` — bumped `chat.js` + `style.css` stamps to `?v=20260808historynav`.
- `static/sw.js` — `CACHE_NAME` → `odysseus-v388-historynav`.

**Verified:** `node --check` clean on both JS files; 25/25 behavioral tests passed (wiring + no keydown listener registered, older/newer walks, oldest cap, draft save/restore, typing resets the walk, no-history disabled state, disabled-composer click guard, multiline/CRLF normalization). Test harness removed after passing.

**Reload:** one page reload (stamps bumped) picks it up; no server restart needed.

## 2026-08-08 — fix(audit2): pending-flow flag leak + orphaned-response regenerate guard (Finding A + Finding B from the round-2 audit)

**Reported by Sir (2026-08-08):** round-2 audit findings — "1. sure (fix Finding A) 2. uhhh guard (Finding B) 3. [endpoint probe: skip — the endpoint will never admit it's pretending]". Also: read `docs/ARCHITECTURE.md` first, file file-relationship changes in `docs/FILE_MAP.md`, log everything here.

**Forensics (code trace, 2026-08-08):**
- **Finding A — flag leak on aborted sends.** The continue/regen/edit/auto-recover flows set module-level pending flags (`_hideUserBubble`, `_pendingRegenUser`, `_pendingVariants`, `_pendingVariantLabel`, `_pendingContinue`) immediately before clicking submit. `handleChatSubmit` has MULTIPLE early returns BEFORE the flags were consumed (setup mode, slash commands, no-session auto-create paths, the API-key confirm cancel) — any of them left the flags set, so the NEXT send inherited them: user bubble silently hidden, `reuse_last_user` riding along (backend reuses the wrong tail or falls back), regen variants attached to the wrong response. Three of the flags had this leak before (pre-existing); `_pendingRegenUser` (added earlier today) inherited it.
- **Finding B — orphaned-response regenerate overreach.** After deleting a user message, its AI reply has no prompt: `regenerateFrom` walks back to the NEAREST preceding user message — an earlier turn's prompt — and truncates back to that turn, wiping everything in between. The existing `userIndex < 0` guard only caught "no user message at all", not "the found one is a grandparent".

**Fix (chat.js + chatRenderer.js, 2026-08-08):**
- **Finding A — consume pending-flow flags at send entry.** `handleChatSubmit` now captures all five flags into locals AND clears the globals immediately after the `_sendInFlight` guard (chat.js:~1192), before ANY early return. Consumption points use the captured locals: `skipBubble` (bubble creation + auto-nudge reset), `reusePending` (FormData `reuse_last_user`), `pendingContinue` (stream-end merge with the stopped element), `pendingVariants`/`pendingVariantLabel` (passed as args to `_attachVariantNav` — signature changed from reading the globals). The continue/step-limit/auto-recover handshakes all set their flags immediately before their own submit, so entry-capture sees the same values — verified no mid-stream set is consumed by a stale read (all mid-stream sets are followed by their own submit). An aborted send now leaves the globals clean by construction; a future early return can't reintroduce the leak.
- **Finding B — adjacency guard.** `regenerateFrom` now refuses when another standalone AI response sits between the clicked AI message and the found user message (chat.js:~5302): "Can't regenerate — the user message for this response was deleted." Continuations + agent tool bubbles belong to the response and are allowed. The Regenerate action is also HIDDEN in that state: `createMsgFooter`'s `available` hook now calls `_hasAdjacentUserPrompt(msgElement)` (chatRenderer.js:~1528) — walk back, stop at the first `.msg-user` (true) or non-continuation `.msg-ai` (false).

**Verified:** `node --check` clean on both files; grep confirms every global read now happens only at the send-entry capture (all other references are sets feeding the next submit). No backend changes today — pytest suite unaffected.

**Backups:** `static/js/chat.js.bak-20260808-flagleak`, `static/js/chatRenderer.js.bak-20260808-flagleak`.

**Docs:** `docs/FILE_MAP.md` updated (session_manager add_message rollback/raise; context_compactor `_map_convo_split_to_history`; history_routes exact-id delete + truncate `keep_through_id`; chat_helpers `user_message_id` + `reuse_last_user`; chat_routes `user_message_saved` + `reuse_last_user`; js/ row; §11 flow 1). `docs/ARCHITECTURE.md` updated (§2.3 chat_stream event/field; §4.1 send-entry flag capture; §6 transplant table row corrected: `user_message_saved` SKIPPED → **PORTED 2026-08-08** — it was ported in the delete/regen work, the receipt row was stale).

**Status: LIVE (needs frontend reload only — no backend change today).**

## 2026-08-08 — fix(delete/regen): delete no longer obliterates pairs; regenerate reuses the user message row instead of re-sending it

**Reported by Sir (2026-08-08):** "Pressing Delete on an Agent message 'wipes' the user message before it, but it's actually still in the DB (refresh restores user message). Regenerate From Here tends to re-send the last user message. Appears as if it's regenerating on the frontend, message's just resent in DB." Interjection clarifying spec: **"I do not want Delete on agent message to ALSO delete user message. I want to freely choose the specific message to delete, no pairs get obliterated!!!"**

**Forensics (code trace, 2026-08-08):**
- **Root cause of both bugs: the live user bubble never carries its DB id.** Only AI bubbles get stamped (`message_saved` SSE event → `holder.dataset.dbId`); user bubbles render optimistically before persistence and were never stamped. So delete had to guess the turn partner via `resolve_pairs` (server walks history to find "the nearest user message before the AI" and deletes both — exactly the pair obliteration Sir rejected; and when the walk/anchoring missed, the user row survived in the DB → ghost on refresh). Regenerate had no id to truncate by either: it deleted the user row via a DOM-counted `keep_count`, then re-sent the text through the full send pipeline → a brand-new user row (new id, new timestamp) each regen, with the count vulnerable to hidden/unstamped-row divergence → duplicate user messages in the DB.

**Fix (2026-08-08):**
1. **User bubble stamping.** `build_chat_context` now captures the persisted user message's `_db_id` (new `ChatContext.user_message_id`) and the stream emits a `user_message_saved` SSE event as the FIRST preamble event; the frontend stamps the tracked optimistic bubble (`_activeUserMsgEl`, with a last-`.msg-user` fallback) so it can't hit the wrong turn. Delete/regenerate now always have exact ids.
2. **Delete = exact-id only.** Frontend `deleteMessage` rewritten: user click deletes ONLY the user bubble/row; AI click deletes the AI row + the DOM-only artifacts of that response (continuation/tool bubbles — no DB rows), never the preceding user message. `resolve_pairs` removed from the backend delete endpoint entirely — no pair resolution exists anywhere anymore. DOM removal mirrors the DB exactly.
3. **Regenerate reuses the user row.** `truncate` endpoint gains `keep_through_id` (id-based: keep every row through the given message id — exact, immune to hidden rows/unstamped bubbles); `regenerateFrom` sends the user bubble's dbId so the user row SURVIVES and only the AI reply + tail are deleted. The resend carries `reuse_last_user: true` (new form field → `build_chat_context(reuse_last_user=...)`), which skips `add_user_message` — the history tail is verified (role=user + content match) and reused as-is, so the DB id/timestamp never churn. Falls back to a fresh add (old behavior) when the tail doesn't match or the bubble had no id. Webhook/event_bus "new message" events are NOT re-fired for reuse (it isn't a new message).

**Verified (2026-08-08):**
- `py_compile` clean (chat_helpers, chat_routes, history_routes); `node --check` clean (chat.js).
- Existing suite: 66 passed (truncate regression, chat_helpers, history db fallback, resend nondestructive, context compactor ×2).
- End-to-end proof against the real `SessionManager` + temp SQLite: (a) keep_through_id truncate keeps `[u1,a1,u2]` with u2's id STABLE, deletes only a2; (b) reuse guard matches the kept tail → same id returned; (c) exact-id delete removes ONLY the clicked message, user rows untouched.
- `resolve_pairs` gone from live code (comments + docs only); docs/FILE_MAP.md + docs/ARCHITECTURE.md updated.

**Files:** `routes/chat_helpers.py`, `routes/chat_routes.py`, `routes/history/history_routes.py`, `static/js/chat.js`, `docs/FILE_MAP.md`, `docs/ARCHITECTURE.md`.
**Backups:** `*.bak-20260808-delete-regen` next to each source file.

**Status: LIVE pending server restart + hard refresh** — needs uvicorn restart to load the backend changes (no DB migration).

## 2026-08-08 — fix: auto-compact defenestrated recent turns (wrong split mapping) + chat-mode empty completions vanish + persist failures ghost memory-only messages + shadowed /compact endpoint removed

**Reported by Sir (2026-08-08):** full sync audit of the LLM/user-message pipeline ("refresh shouldn't change anything", "no LLM message gets lost", "context gets defenestrated"). HITL answers: fix now + log; auto-compact never fires for him in practice (the free endpoint lies about model identity — reports "Deepseek v4 Flash", likely really v3.2, so Odysseus believes the context window is 1M when it's ~128K, and 85% auto-compact never triggers); clean up the dead duplicate.

**Forensics (code audit, 2026-08-08):**
- **Auto-compact split misalignment.** `maybe_compact` computes `split_point` against `convo_msgs` (non-system entries of `messages` = preface + history), but `_update_session_history` applied it to `session.history` with `effective_split = system_msg_count + split_point` and a `system_prefix = session.history[:system_msg_count]`. `session.history` in a normal chat has ZERO leading system messages while the preface always carries 4–6+ (preset, memory, RAG, skills, web) plus user-role injections (search context, date context). So `system_prefix` grabbed real conversation messages (duplicating turns 1–2 verbatim while the summary overlapped them) and `history[N+split:]` dropped the N messages just past the intended split — i.e. the most recent completed turns — from BOTH memory and DB, with no trace in summary or history. Reproduced with the real function: 100-turn chat, N=4 → turns 51–52 (4 messages) deleted outright; the model never sees them again; refresh shows the hole. On the next auto-compact (history now contains the summary system message) the offset compounds differently. The manual compact path (session_routes, `replace_messages`) slices history directly and was never affected; the agent loop passes `session=None` and was never affected. Chat-path-only.
- **Chat-mode empty completion still vanished.** Yesterday's empty-completion marker covered the agent branch only; the chat branch still did `if full_response:` → save, so a 200-with-0-chars chat-mode reply left the user message dangling with no reply row, no error, no retry — same class as the 2026-08-07 "Update:" turn.
- **`_persist_message` swallowed failures.** `Session.add_message` appended to in-memory history FIRST, then `_persist_message` caught every exception (missing upload ValueError, DB error) → log + rollback + silent return. The message stayed in memory (model sees it next turn) but never reached the DB: invisible to refresh, undeletable by id (`_db_id` never stamped), and `resolve_pairs` can't find it. Ghost in reverse.
- **Shadowed `/compact` duplicate.** Two handlers existed for `POST /api/session/{id}/compact`: session_routes (registered first → wins; order-safe, `replace_messages`) and history_routes (registered second → dead code; and its version kept the recent messages' original timestamps while inserting the two summary rows with `timestamp=now`, so on refresh the "Conversation compacted" bubble would jump from top to bottom — order desync). A landmine: reorder the includes and the broken implementation goes live silently.

**Fix (`src/context_compactor.py`):**
- New `_map_convo_split_to_history(session, messages, split_point)` maps the convo_msgs split back onto `session.history` by matching history messages against the context list via `_db_id` metadata (fallback: role+content for never-persisted messages), counting them in order across the summarized range, and folding leading system messages (prior compaction summaries) into the summarized portion. Returns `None` when the mapping can't be established → history left untouched (safe) instead of corrupted.
- `_update_session_history(session, history_split, summary)` now takes a true history index: `new_history = [summary] + history[history_split:]`, refusing non-shrinking rewrites and logging skips. No more `system_msg_count` offset, no more phantom `system_prefix`. `summarized_count` metadata now reports real history messages summarized.
- Verified against the real functions: fresh 100-turn chat → split lands exactly at turn 50, turns 51–100 kept verbatim, 1–50 summarized, history = summary + 100 recent (old code: turns 51–52 deleted). Second compaction with a leading system summary → old summary folded away, correct split. Mostly-ephemeral context (huge RAG) → `None`, history untouched. No-`_db_id` fallback works.

**Fix (`routes/chat_routes.py`):**
- Chat-mode `[DONE]` with empty `full_response` now mirrors the agent branch: persists streamed reasoning if the model only emitted that, otherwise `_*The model returned an empty response — try again or switch models.*_`, with a warning log line and `message_saved` event. No more silent 200-with-0-chars deaths in chat mode.
- Chat-mode disconnect partial-save wrapped in try/except so a persist failure can't mask the original `CancelledError`/`GeneratorExit` (agent-mode site already had this from 2026-08-07).

**Fix (`core/session_manager.py`):**
- `_persist_message` now returns `True` on success, `False` only for the soft-drop (session already deleted), and RE-RAISES real failures (missing upload, DB error) instead of swallowing them.
- `add_message` rolls the in-memory append back on persist failure (memory and DB stay in sync — no more memory-only ghosts) and re-raises so callers surface the error; soft-drop pops the orphaned copy silently. Callers audited: stream saves, user-message add, webhooks, agent tools, task scheduler, bg_monitor — all either propagate to an honest error or are already wrapped (disconnect partial-saves, scheduler, bg_monitor).

**Fix (`routes/history/history_routes.py`):** deleted the shadowed `POST /api/session/{id}/compact` handler (dead code behind the session_routes winner, and order-broken if it ever ran) + removed its now-unused imports (`_message_role`, `_message_text`, `_reject_compact_during_active_run`). Only the canonical session_routes compact remains.

**Verified:** `py_compile` clean on all four files; full simulation of the split mapping against the patched functions (4 scenarios, all correct); existing suite `tests/test_context_compactor.py` + `tests/test_compaction_summary_failure.py` → 23 passed. Backups: `src/context_compactor.py.bak-20260808-compactsplit`, `routes/chat_routes.py.bak-20260808-chatempty`, `core/session_manager.py.bak-20260808-persistfail`, `routes/history/history_routes.py.bak-20260808-shadowcompact`.

**Status: NEEDS RESTART** — server code changed (uvicorn on 127.0.0.1:7001 must restart to load; no frontend changes, no hard refresh needed).

**Still open:** the endpoint-identity lie ("Deepseek v4 Flash" reporting as ~v3.2, 1M-believed vs ~128K-real context) means trim/compact thresholds are miscalibrated against the real model — worth probing true model identity + context window (see `probe-llm-endpoints-to-verify-true-model-identity` skill) so auto-compact and trimming fire at sane levels.

## 2026-08-08 — doc: new `docs/FILE_MAP.md` — exhaustive per-file map of the whole backend

**Per Sir (2026-08-08):** "make a map of all the files — what they do and what they
interact with — so new IRISes don't need to go sniffing at everything every new session."

**Deliverable:** `docs/FILE_MAP.md` (446 lines) — the street-map companion to
`docs/ARCHITECTURE.md` (which stays the 10,000-foot view). Covers:

- `core/` (11 files), `src/` (144 files, grouped by subsystem: chat pipeline, tools,
  memory/RAG, documents, tasks/calendar/email, services/infra, research), `routes/`
  (73 files, shims vs canonical packages distinguished), `services/` (40 files),
  `mcp_servers/`, `companion/`, `integrations/`, `scripts/` (the `odysseus` CLI
  dispatcher family), `static/` (pointer to `static/js/MODULE_SUMMARY.md`), `data/`
  runtime layout (which file is which DB/state), key flows, and conventions.
- Every file gets: one line on what it does + one line on what it interacts with
  (local imports + data files/DBs), derived by AST-parsing docstrings/imports across
  the tree — not hand-guessed.
- Also documented: `data2/` is a STALE duplicate (not referenced by code — ignore);
  sibling forks (`odysseus.old` freeze-suspect, `odysseus.dev` vanilla upstream);
  entry point = `run.sh` → uvicorn on 127.0.0.1:7001.

**Also touched:** `docs/ARCHITECTURE.md` header now points at FILE_MAP.md as the
per-file companion. Backup: `docs/ARCHITECTURE.md.bak-20260808-filemap`.

**Status: LIVE** — docs only, no restart needed. No server code changed.

## 2026-08-07 — fix: regenerate/edit/resend truncates were wiping recent pairs ("defenestrating pairs of messages") + empty completions vanish silently

**Reported by Sir (2026-08-07):** "odysseus's straight up defenestrating pairs of messages (my message then the AI turn after)." Session "Attached to AI and Its Stories" lost four completed turns (17:46 hydration reply, 17:49 crazy pair, 17:52 dr pepper, 17:55 hedge) — streamed to completion per `data/logs/app.log` (`round_stream_done` with 1269/2291/2914 chars), absent from `chat_messages` + FTS. "Turn Nuke Hunt" lost the reply to "Update:…" (opencode returned HTTP 200 with 0 chars).

**Forensics (DB + log, no live-API probing):**
- Truncate log lines `Truncated session a9875f60 to 96 messages` (18:00:00.348) and `to 98` (18:03:00.072) land exactly at the gap boundaries; the surviving row layout (bean-water=95, tongue=96, where-da-frik=98, 100 rows) is exactly what keep-first-96 then keep-first-98 produce. The four turns were rows 96-104 and were **deleted**, not lost: the FTS AFTER-DELETE trigger (`chat_messages_fts_ad`) scrubs FTS rows on delete, so truncate wipes leave zero forensic trace.
- `truncate_messages` (core/session_manager.py:290) keeps the first N, deletes the rest — DB, FTS, in-memory history, and resets `message_count` (explains the count desyncs too).
- Frontend `_dbRowCountBefore` counted ONLY dbId-**stamped** DOM elements. Live user bubbles are never stamped (only history-rendered ones are), so any regenerate/edit in a live session undercounts by the number of unstamped bubbles before the target → truncate keeps the wrong slice → whole recent pairs die. The 18:00 truncate kept 96 (target's preceding stamped count) when the target's true row index was 97+ → wiped rows 96-104.
- The re-send after the truncate is `submitBtn.click()` with **no disabled-input guard** — the exact hole the Continue-button fix patched earlier today (chat.js:1125 `if (msgInput && msgInput.disabled) return;`), but only Continue got the guard. With a stream active the input is disabled, the click no-ops, and the wiped pairs never come back.
- The "Update:" turn: `round_stream_done round=1 text_chars=0 tool_calls=0` (HTTP 200, empty completion) → chat_routes agent-branch `if full_response or _has_tool_events:` skips the save entirely → reply never born, no error, no retry (the 503/empty auto-retry is still flagged broken in memory/changelogs).

**Fix (`static/js/chat.js`):**
- `_dbRowCountBefore` now counts unique stamped ids **plus one per unstamped real bubble** (excluding client-only `agent-thinking-dots` / `research-reconnect` bubbles) — the DOM position now mirrors the true server row index even with live bubbles in the thread.
- Disabled-input guard on all three destructive flows (`editUserMessage`, `resendUserMessage` with `replaceFromHere`, `regenerateFrom`): if the input is disabled, abort loudly with an error instead of truncate-then-silent-no-op.
- MutationObserver watchdog in `initListeners`: any `.msg` removed from `#chat-history` outside the deliberate flows logs `[msg-removal]` to the console with class + dbId + text — the spontaneous-vanish path (e.g. the hydration reply disappearing from the DOM before the 18:00 truncate) is now catchable live.

**Fix (`core/session_manager.py`):** `truncate_messages` logs the deleted count and index range (indices keep_count → len-1) so future truncates are auditable in app.log.

**Fix (`routes/chat_routes.py`):** agent-branch `[DONE]` with empty `full_response` and no tool events now persists something visible instead of vanishing: streamed thinking if the model only emitted that, otherwise a `_*The model returned an empty response — try again or switch models.*_` marker, with a warning log line. No more silent 200-with-0-chars deaths.

**Verified:** `node --check static/js/chat.js` clean; `py_compile` clean on both python files. Backups: `static/js/chat.js.bak-2026-08-07-pairs`, `core/session_manager.py.bak-2026-08-07-pairs`, `routes/chat_routes.py.bak-2026-08-07-pairs`. Frontend changes need a hard refresh; server changes need a **restart** to load.

**Still open (instrumented, not yet root-caused):** why the hydration-reply *bubble* left the DOM in the first place (the user saw it vanish before any truncate). The watchdog + truncate logging will pin it on next occurrence.

## 2026-08-07 — fix: content-delivered thinking quoting `</think>` no longer explodes the box at round end

**Reported by Sir:** "think blocks still explode once the round's over … the very first `<think>` just gets Thanos snapped out of existence."

**Root cause (reproduced with the real functions):** thinking delivered as *content tags* (not a reasoning field) whose reasoning QUOTES a literal `</think>` (the model is reasoning *about* think tags — our own think-saga sessions do this constantly). The auto-detect / first-close rule treats the quoted close as the real block boundary → the box truncates at the quoted close and the reasoning tail + a literal `</think>` spill into the reply at the final render. Two holes:

1. `src/llm_core.py` — the OpenAI-compat auto-detect was gated on `not _thinking_model`, so name-recognized thinking models (deepseek-v4…) whose gateway serves the reasoning as content tags got them passed through raw, un-flagged.
2. The auto-detect split at the FIRST `</think>` in a chunk — a quoted close inside reasoning truncated the flagged region.

**Fix (`src/llm_core.py`):**
- Removed the `not _thinking_model` guard — content-delivered `<think>` regions are now routed flagged for ALL models (frontend neutralizes quoted tags inside the box).
- New `_CONTENT_REPLY_STARTS` heuristic: when a chunk inside a think region contains several `</think>` and the text after the first doesn't look like a reply boundary, split at the LAST close — quoted closes ride into the flagged thinking channel and render as literal text inside the box. Single-close and reply-looking cases keep the first-close split (the reply's own quoted tags stay content).

**Verified:** split-logic tests — simple case unchanged (THINK→CONTENT), same-chunk quoted close now THINK(`</think>`tail)→CONTENT(reply), reply-with-quoted-closes preserved, multi-close reply-looking preserved, multi-block merges into one flagged region. `py_compile` clean. Needs a **server restart** to load.

**Known limitation (fundamental ambiguity):** when the quoted close and the real close land in *separate* chunks, the first-close rule still truncates (the quoted close is indistinguishable from the real one in a text-only stream). The flagged reasoning-field path (DeepSeek reasoning_content) handles quoted closes fully — the fix routes content tags onto that same path wherever the closes share a chunk.

## 2026-08-07 — tune: skill match threshold raised 0.25 → 0.3

**Per Sir (2026-08-07, green light):** raise the skill relevance match threshold —
the hardcoded 0.25 Jaccard was over-permissive (generic words match a lot; with a
130-skill library the injected digest + full index block is real context noise).

- **`src/agent_loop.py`**: `threshold=0.25` → `0.3` at both call sites — the main
  skill injection (~2528, `max_items=_skill_max_injected` / `min_confidence=_skill_min_conf`)
  and the skill-aware tool-RAG include (~3508, hardcoded `max_items=3`). Dated comment
  added at the main site.
- Context: skills currently disabled by prefs (`skills_enabled: false`,
  `skill_max_injected: 0`, `manage_skills` in `disabled_tools`) — threshold matters
  on re-enable. Audit record at disable time: 117 audited entries (26 pass / 33
  skipped / 55 inconclusive / 3 needs_work); Sir plans to re-audit then prune with
  the UI's "delete non-passing" bulk action.

**Server:** python change. **Status: PENDING RESTART** — takes effect on next server
bounce. Verified compile-clean (`py_compile`). Backup:
`src/agent_loop.py.bak-20260807-threshold`.

## 2026-08-07 — fix: TTS + Teacher Model settings cards restored in WebUI

**Per Sir (2026-08-07):** "Why are all the juicy settings hidden in a file and not
configurable in the WebUI?" — the TTS card was hidden in the DOM
(`hidden style="display:none"` + a "user opted out of read-aloud entirely" comment,
JS wiring fully intact) and the Teacher Model card was removed entirely during the
"harden the core 2.0" pass (only a tombstone comment remained; `initTeacherModel`
wiring survived).

- **`static/index.html`**: un-hid the TTS card; rebuilt the Teacher Model card in
  its old spot (endpoint picker, model picker, enable toggle, save feedback —
  matches every ID `initTeacherModel` expects). `initTtsSettings()` /
  `initTeacherModel()` confirmed called on page load.
- Teacher escalation stays dormant while `teacher_enabled` is off; the card only
  surfaces the toggle + endpoint/model picker again.
- Related context: the old "too sensitive" teacher failures traced to unanchored
  failure regexes (`\berror:\s` matched the literal word "error" inside tool output)
  — fixed in the 2026-08-06 teacherfix pass.

**Server:** static change. **Status: LIVE** — static files serve on refresh, no
restart needed. Backup: `static/index.html.bak-20260807-tts-teacher-unhide`.

## 2026-08-07 — feat: web-intent tool strip removed — lookup turns keep every enabled tool

**Per Sir (2026-08-07):** the explicit-web-intent guard is removed. Previously a
message classified as a direct lookup/search (regex in `routes/chat_routes.py` or the
deterministic `classify_tool_intent` patterns in `src/action_intents.py`) disabled
bash/python/read_file/write_file/edit_file plus the personal tools (manage_memory,
manage_skills, search_chats, create/edit/update_document, send/reply email,
notes/calendar/tasks, api_call) for that turn.

Now: web-intent turns keep EVERY enabled tool. The LLM is trusted not to drift, and
dossier/memory/document work must stay possible mid-lookup.

**What remains:**
- Manual toggles still gate tools: `allow_bash` (bash-toggle), web toggle +
  `web_search_enabled_for_turn(allow_web_search, use_web)` (web tools off when
  denied/disabled), incognito, active-email-reader guard, per-user privileges,
  global `disabled_tools` setting, plan mode, tool policy, compare mode.
- Chat→agent auto-escalation on web intent still applies (chat_routes.py:801) —
  lookup requests still escalate to agent mode with full tools.
- The `if _search_enabled / elif` re-enable chain inside the old strip was a set of
  no-ops in every reachable state (line 1098 already governs web-tool availability);
  removed together with the strip.

**Tests:** `tests/test_chat_route_tool_policy.py` passes unchanged — the two web-intent
tests (explicit-deny-wins, intent-doesn't-enable) still hold; the test-side replica of
the strip is now inert (no assertion touches its members).

**Server:** python change. **Status: LIVE** — server restarted 2026-08-07 12:34
(PID 1155254, after all edits); verified compile-clean (`py_compile` on all changed
files) and 35 related tests green. Both python changes (this + the RAG entry below)
are live in the running server.

## 2026-08-07 — feat: RAG tool selection permanently disabled — always-on full tool catalog

**Per Sir (directive 2026-08-07):** "I absolutely despise the RAG tool thing.
I want the LLM to know all the enabled tools and be able to use them whenever,
not be limited to a select few based on whatever I said. In the prompt when
building, tools should be described shortly in both what it does and how to
use it. The LLM can go find the full description in a file if it needs to."

The RAG/keyword/domain tool-selection path is **removed from the live request
path** — it can no longer limit the model to a retrieval-selected subset based
on the user's message. Every agent round ships the FULL enabled catalog
(builtin + MCP) and every round the model can call any enabled tool.

- **`src/agent_loop.py`** (stream_agent_loop): `_relevant_tools` is now forced
  to `None` unconditionally — caller-provided `relevant_tools`
  (task_scheduler's old RAG path) is ignored with a log line. Deleted the
  ChromaDB retrieval block, the keyword fallback, the low-signal read-only
  file-tools branch, and the uploaded-files/forced-tools re-seed blocks
  (redundant with the full catalog). Local-model schema assembly now always
  ships every MCP schema (`_wants_mcp` keyword gate removed). Downstream
  `_relevant_tools is not None` branches are now inert; kept for
  guide_only/teacher tool_policy compat and a potential future opt-in.
  `agent_list_all_tools` setting is now a no-op (default True preserved).
- **Prompt format** (`_assemble_prompt`): both compact (API-model) and full
  (local-model) modes now emit the same **always-on tool catalog** — one line
  per tool: `- `name` — <what it does> Usage: <how to use>`. Replaced the old
  bare-names list (no descriptions) and the huge multi-paragraph blocks
  (~10k+ tokens) with a ~5.4k-token catalog. One-liners are derived from the
  TOOL_SECTIONS prose + first example fence, or from the function schema for
  schema-only tools (grep/glob/ls/api_call/edit_image/...). User overrides
  (`builtin_tool_overrides`) still apply.
- **Full descriptions in a file**: new **`src/tools_doc.py`** generates
  `data/TOOLS.md` (agent-readable — DATA_DIR is a default tool-path root) plus
  a `docs/TOOLS.md` mirror in the repo (73 tool sections: full prose +
  parameters + MCP tool schemas). Regenerated lazily on prompt builds and at
  app init (hash/content-guarded, writes only on change). The catalog carries
  a pointer line: "Full usage documentation ... `TOOLS.md` ... Use read_file
  to open it whenever you need details beyond these one-liners."
- **`src/task_scheduler.py`**: scheduled/proactive tasks also skip RAG —
  `relevant_tools` is `None`, full catalog every run (previously
  `get_tools_for_query(prompt, k=8)`).
- **`src/app_initializer.py`**: ensures `data/TOOLS.md` exists from boot.
- **Tests**: `tests/test_task_shell_tools.py` updated — scheduled tasks now
  pass `relevant_tools=None` (disabled-tools enforcement unchanged, still
  reaches the agent loop). 79 agent/tool/prompt tests pass.
- **Unchanged, intentionally**: `_force_answer` (loop-breaker), `disabled_tools`
  (user's explicit disable list — still stripped from the catalog AND the
  schemas), `_ody_qwen_finetune_model` clamps, `_needs_admin` gating,
  plan-mode MCP write-blocking, guide_only / teacher flow.
- To revert (not recommended): re-enable the RAG path by restoring the
  selection block from `src/agent_loop.py.bak-20260806-alltools` and the
  `compose_task_relevant_tools` call in task_scheduler; `agent_list_all_tools`
  in settings.json can then toggle it again.

## 2026-08-07 — fix: spurious continue-merge absorbed a completed turn (obliteration) + message_count desync

Reported from the "Adding Continue to Odysseus" session (`e501a776`): a finished
agent turn visibly vanished in front of the user right after completing, leaving
only their own message. Forensics (DB + FTS orphan + log): the turn WAS
persisted (row inserted, count=11, last_message_at set) and then **merged into
the previous interrupted message by the continue-merge flow** — content joined
with `*(continued)*`, the continuation row deleted, the frontend removed the
bubble. Two bugs:

- **static/js/chat.js** — the ▶ Continue button handler set `_pendingContinue`
  unconditionally and fired a send that silently died mid-stream (disabled
  input/send button). A Continue click landing during an active stream left
  `_pendingContinue` stale, so the NEXT completed turn got merged into the
  stopped message at its finalize — the turn the user was watching was absorbed
  and its bubble removed. Fix: ignore the Continue click entirely while the
  input is disabled (stream active).
- **routes/history/history_routes.py** — `merge-last-assistant` popped rows
  from memory and deleted them from the DB but never synced
  `message_count` (11 in DB with 10 rows). Fix: sync both
  `session.message_count` and `db_session.message_count` after the merge.

Verified: node --check chat.js + py_compile history_routes.py clean; chat.js
cache stamp bumped to `?v=20260807continuemergefix` (one reload picks it up).
The absorbed turn's content is NOT lost — it lives inside the previous message
after the `*(continued)*` marker; the session's stale count self-heals on the
next message persist.

## 2026-08-07 — audit: `.old` → garbo transplant, silent frontend-half sweep

Sir asked for a full "half-assed port" audit after the regenerate + delete-message
fixes (both were cases where the server half landed and the frontend half was
dropped). Result: **the two fixed bugs were the only silent frontend-half drops**
in the transplant. Everything else is either complete, consolidated, or
documented. Evidence trail below.

**Confirmed gaps (already fixed earlier this session):**
- Regenerate/resend/edit truncate `keep_count` — `.old` counted unique
  `dataset.dbId` rows before the target (`_dbRowCountBefore`); garbo used the
  raw DOM index. Restored `_dbRowCountBefore` at all three call sites.
- Delete-message `resolve_pairs` flag — `.old` sent it when a pair member
  lacked a dbId; garbo dropped the flag (server half ported, frontend half
  didn't make it). Restored `pairMissingDbId` + conditional flag.

**Audited clean this pass (methods + verdicts):**
1. Backend request-key scan (routes/ + src/, request-body receivers):
   991→321→45 candidate keys; the only real orphan was `resolve_pairs` (fixed).
   All other zero-frontend keys are legitimately server-side: model-server
   responses (`baseModelId`, `supportedGenerationMethods`, `nextPageToken`,
   `chat_template_caps`, `samplers`, `total_slots`…), LLM tool-call args
   (`max_pages`, `time_filter`, `days_back`, `hidden_images`, `arg_delta`…),
   OAuth/device flows (`authorization_code`, `code_verifier`, `refresh_token`…),
   config (`REQUEST_TIMEOUT`, `SESSIONS_FILE`), email parsing (headers).
2. `.old` FE keys dropped by garbo FE: `poll_id` → re-implemented in
   `static/js/providerDeviceFlow.js` (consolidated, verified sends it);
   `_byRepo`/`_lastUsed` → FE-local serve-state schema, backend reads neither;
   `deadline`/`Model`/`unsupported` → single incidental hits, no contract.
3. chat_stream form fields: garbo's `fd.append` set is a **superset** of
   `.old`'s (adds `active_email_*`, `selected_endpoint_*`, `selected_model`).
4. chat.js export surface: garbo ⊇ `.old` (adds `compactCurrentChatContext`,
   `queueStreamingComposerRequest`, `refreshChatContextHeader`). Variant nav
   (`_attachVariantNav`, `_pendingVariants`) present.
5. FE file inventory: identical except `planWindow.js` — reimplemented inline
   in garbo (`_pendingApprovedPlan` → `approved_plan` form field; plan-mode
   status pill in index.html). Contract verified wired.
6. Teacher-takeover fix: `data.get("teacher")` reads are SSE **event** payloads
   (chat_routes.py:1548/1734/2032); garbo FE renders `teacher_takeover` events
   (chat.js:3523-3538). Both halves present.
7. Server comments describing FE contracts (`approved_plan`, `active_doc_id`,
   `active_email_uid/folder/account`, `workspace`, disabled-tools toggles):
   all present in the garbo FE send path.

**Minor findings (not transplant gaps, flagged for completeness):**
- `model_refresh_interval` — server reads it (model_routes.py:2567, min 30s),
  admin UI never sends it (sends `model_refresh_mode` + hardcoded
  `model_refresh_timeout=30`); server default applies. No breakage.
- Known-documented items, unchanged: 503 auto-retry flagged BROKEN
  (2026-08-05 entry, needs a fix pass); `resumeStream` dead code (backlog,
  deliberately NOT ported — freeze-to-halt suspect); `.old` freeze-to-halt
  open thread.

**Ops:** no code changes in this audit pass (changelog only). Static files
already live; hard refresh not required for the audit itself.

## 2026-08-07 — fix(chat): regenerate actually regenerates (split-brain module instances + imprecise truncate count)

**Symptom (user-reported):** clicking Regenerate on an assistant message does not
replace it — the last user message gets re-sent instead (duplicate user bubble /
same answer again). Root cause was two compounding frontend bugs, both of the
class already fought in the 2026-08-05 ghost-message fix:

1. **Split-brain module instances (the big one).** Version-string drift between
   `<script type="module">` tags in index.html and `import` statements in
   app.js / chat.js etc. — different query strings = different URLs = the browser
   instantiates the module TWICE, each with its own copy of module state
   (`_hideUserBubble`, `_pendingVariants`, `_pendingRegenAttachments`,
   `currentAccumulated`, session trackers). Regenerate sets `_hideUserBubble` in
   one instance; the submit path (a different instance) never sees it, so the
   user message is re-posted as a fresh bubble. Affected modules and their
   canonical (unified) URLs:
   - `chat.js?v=20260807historyrecall` (was ghostfix1 in app.js)
   - `chatRenderer.js?v=20260806thinkfix1` (was emailfastindex1 / ctxheader1 / bare)
   - `chatStream.js?v=20260722emailfastindex1` (was bare in chat.js)
   - `sessions.js?v=20260806autotitle1` (was unified2 in 16 files — the ghost
     bug's own split-brain was quietly back)
   - `markdown.js?v=20260806thinkfix1`, `gallery.js?v=20260708match1`,
     `settings.js?v=20260723compareicon1` (were bare / emailfastindex1)
   - `static/sw.js`: precache entries now point at the unified versioned URLs,
     `CACHE_NAME` bumped `v386-historyrecall` → `v387-unified-chat` so stale
     copies die. Verified: every one of the 7 modules now resolves to exactly
     one URL across all imports + index.html tags (grep-audited).

2. **Imprecise truncate count on regenerate/resend/edit.** `regenerateFrom`,
   `resendUserMessage({replaceFromHere})` and `editUserMessage` passed the raw
   DOM index of the target message as `keep_count` to `/api/session/{id}/truncate`.
   The `.old` fork counted unique `dataset.dbId` rows before the message
   (`_dbRowCountBefore`) — garbo's simplification diverges whenever the DOM has
   any dbId-less element (optimistic bubble, client-only note) or a missing
   stamp, truncating the wrong slice so the OLD assistant reply survives into
   the regenerated context. Restored `_dbRowCountBefore` (unique-dbId count) and
   wired it into all three truncate call sites.

No server restart needed (static files served from disk); the SW cache bump
forces a fresh install on next load — hard-refresh the UI once.

## 2026-08-07 — fix(chat): delete-message no longer resurrects the user message on refresh (port the resolve_pairs flag from .old)

**Symptom (user-reported):** deleting an assistant message/turn also removes the
preceding user message from view — but only on the front end; refreshing the
page brings the user message back ("refresh brings my message back" ghost).

**Root cause — transplant gap.** The `.old` fork's frontend `deleteMessage`
detects when either half of the user+AI pair has no `dataset.dbId` on the DOM
and sends `resolve_pairs: true` in the delete request; the server then resolves
the missing turn partner by history order and deletes it too. The server half of
that mechanism was ported to garbo (`routes/history/history_routes.py`, the
`resolve_pairs` block — its comment even names the exact ghost it kills), but
the frontend half was dropped: garbo's `deleteMessage` always sent
`{ msg_ids: [...] }` with no flag.

Why the flag is always needed in practice: the user bubble only ever gets
`dataset.dbId` stamped when rendered **from history** (chatRenderer.js:2349/2526).
In a live session the user bubble is stamped nowhere (chat.js only stamps the AI
holder on stream finalize, chat.js:3096). So deleting any freshly-generated AI
reply shipped only the AI id to the server — the user row survived, and a
refresh resurrected it. Every single time.

**Fix (static/js/chat.js, `deleteMessage`):** ported the `.old` logic —
`pairMissingDbId` is set when either pair member lacks a dbId, and
`payload.resolve_pairs = true` is sent conditionally. Server-side resolve is
idempotent with the explicit ids (same set either way), so no behavior change
when both bubbles are stamped (e.g. history-rendered sessions).

Verified: `node --check` clean; `_db_id` stamping confirmed in
core/session_manager.py (150/165/280/376) so history-order resolution finds the
user row; resolve_pairs walk logic reviewed for the anchor-is-user and
anchor-is-assistant cases.

## 2026-08-07 — feat(chat): message-tool reorder + overflow menu restored to compact styling

- Assistant footer pinned row is now `Continue | Regenerate | Copy | Delete`
  (was Copy | Regenerate | Continue | Shorten | Delete); Rewrite shorter joins
  Edit / Explain simpler / Fork conversation under the ··· menu.
- User-message footer now pins `Edit | Resend | Copy` and tucks Delete under the
  ··· menu (user footers previously had no overflow menu at all).
- Both footers order their pinned row from an explicit `PINNED_ACTION_IDS` list
  (map + find), so the on-screen order no longer depends on `allActions` order.
- Overflow-menu CSS restored to the original compact, theme-aware rules
  (min-width 150px, `var(--panel)`/`var(--border)`, 6px radius, tight padding
  and gaps) — fixes the "wide" menu from the 08-06 re-add, which had grown to
  min-width 190px with chunky 7×10 padding, 8px gaps and hardcoded dark colors.
- Verified: full module parses clean (browser module loader), footer build +
  menu toggle/item-click exercised against the served file, CSS braces 7707/7707.

## 2026-08-07 — feat(chat): composer prompt-history recall moved to Shift+Left/Shift+Right with draft preservation

- **static/js/composerHistoryRecall.js** (new; replaces `composerArrowUpRecall.js`, kept as `composerArrowUpRecall.js.bak-20260807`) — prompt-history recall is now **Shift+Left = older / Shift+Right = newer**. Plain **ArrowUp/ArrowDown are left untouched** so the caret moves normally inside the message (the old binding was intercepting Up/Down and replacing the draft). The in-progress draft is saved when a walk starts and restored when you walk back past the newest prompt (previously it walked back to blank). Editing a recalled prompt resets the walk cleanly; modifier combos (Ctrl/Alt/Meta) and IME composition are ignored; `preventDefault` only fires on real actions.
- **static/js/chat.js** — import + wiring renamed (`wireArrowUpRecall` → `wireHistoryRecall`, new module URL with bumped `?v=20260807historyrecall`).
- **static/index.html** — chat.js version param bumped to `?v=20260807historyrecall` (cache-bust; chatRenderer/markdown already at thinkfix1).
- **static/sw.js** — `CACHE_NAME` bumped to `odysseus-v386-historyrecall` so the fresh HTML/JS load on the next open.
- Verified: `node --check` both files; 24/24 behavioral tests (plain Up/Down untouched, older/newer walk, oldest cap, draft save/restore across deep walks, edit-resets-walk, no-history no-op, modifier combos ignored).

## 2026-08-06 — feat: auto-title + tab-title reinstated (SUPERSEDES the 08-06 "rollback: custom auto-title work reverted to STOCK" entry)

User changed their mind: stock first-message auto-naming wasn't good enough —
the custom auto-title suite is back, rebuilt from the `.old` design and
verified live. This undoes the earlier rollback (stock HEAD restore).

REINSTATED (all verified live this session):
- `routes/chat_helpers.py` — `auto_name_session` now titles from a head+tail
  context excerpt (first 2 + last 12 non-summary messages, capped 400 chars
  each, 6000 total) instead of the first message only. After `strip_think`,
  output runs through the echo guard (>12 words or instruction-echo phrase →
  reject) so "We need answer with title 6 words or fewer..." can never become
  a chat name. Live-tested: an evolved 6-message convo produced
  "Tab Title Chat Name Fix".
- `routes/session_routes.py` — `POST /api/session/{sid}/retitle` route added:
  same head+tail context, utility model (falls back to the session's own
  endpoint), `max_tokens=200`, `strip_think` + `_clean_title` guard, and a
  first-5-words fallback so a rename always happens. `_clean_title` +
  `_ECHO_PHRASES` helpers restored (guard unit-tested: think-stripped titles
  pass, echoes and >12-word output rejected).
- `static/js/sessions.js` — tab-title mirror IIFE restored: MutationObserver
  on `#current-meta` mirrors the chat name into `document.title`
  ("<name> — Odysseus"), pathname-guarded to `/` so route pages keep their
  own titles. Auto-title (AI) dropdown item restored next to Rename in the
  session ⋮ menu (wand icon, POSTs to the retitle endpoint, refreshes the
  list, header meta, and tab title on success).
- `static/index.html` + `static/sw.js` — sessions.js bumped to
  `?v=20260806autotitle1`; CACHE_NAME → `odysseus-v385-autotitle1`.

Files touched: routes/chat_helpers.py, routes/session_routes.py,
static/js/sessions.js, static/index.html, static/sw.js.

Ops note: restart `odysseus.service` for the Python routes; hard refresh
(SW v385) for the JS. Verify: Auto-title item in the ⋮ menu → POST retitle
→ sidebar + tab title update. Backups: backups/chat_helpers.py.autotitle-*,
backups/sessions.js.autotitle-*.

---

## 2026-08-06 — fix: stored reasoning that QUOTES a think tag no longer breaks the reload box ("breaks open with a little leakage")

User report: the thinking block "basically explodes and breaches containment once
the round is done" — intermittently, with "a little leakage". Root-caused with the
stored data: when the model reasons ABOUT think tags (the stress-test/recursion
messages), the stored `metadata.thinking` itself contains a literal quoted close
tag. On reload, `chatRenderer` rebuilt the box by wrapping the STORED reasoning
raw in a fresh `<think>…</think>` block — the quoted close inside the reasoning
terminated the block early, and the reasoning TAIL + reply spilled out of the box.
Intermittent because it only fires when the reasoning quotes a tag.

CHANGED:
- `static/js/chatRenderer.js` — the metadata.thinking reload wrap now runs the
  stored reasoning through `neutralizeStrayThinkTags(..., true)` (force mode)
  BEFORE wrapping, exactly like the live delta layer already does. The wrapper's
  own tags are the only boundary; quoted tags inside the reasoning render as
  literal text inside the box. (Same class of fix as the live leak — this was
  the one path that still wrapped raw reasoning.)
- `static/index.html` — bumped `chatRenderer.js?v=20260722emailfastindex1` →
  `?v=20260806thinkfix1` (its version param had also frozen, same trap as
  chat.js/markdown.js).
- Verified against the ACTUAL stored recursion-test reasoning (3053 chars,
  literal close tag inside): OLD path leaks the reasoning tail into content;
  NEW path keeps the full reasoning in the block (head+tail), literal close tag
  restored inside, reply clean, no placeholders, gate balanced. `node --check`
  clean. Backups: git tracked.
- Follow-up noted: `static/js/group.js` (group-session renderer) has its own
  raw `<think>` wrap without the reasoning-neutralize treatment — same class of
  bug, separate feature, not touched this round.

## 2026-08-06 — feat(chat): assistant footer pins 5 core actions, Edit / Explain simpler / Fork conversation back under ···

Request (refining the pin-all change above): keep the row tidy — Cut From Here
(Fork conversation), Explain Simpler, and Edit go back into the overflow menu.
The pinned row is now: copy · regenerate · continue · shorten · delete, with a
··· button opening a popup menu for the other three.

- `static/js/chatRenderer.js` — `createMsgFooter` now splits `availableActions`
  by a `PINNED_ACTION_IDS` allow-list (`copy, regen, continue, shorten, delete`);
  anything not in the list renders inside the re-added "···" overflow menu
  (same toggle/positioning/dismiss behavior as before: outside click + Escape
  via `bindMenuDismiss`, flips above/below, right-edge clamp). User-message
  footers unchanged (all 4 still pinned — Edit there edits your own message).
- `static/style.css` — overflow styles re-added (`.msg-more-btn`,
  `.msg-overflow-menu`, `.msg-overflow-item`, `.overflow-icon`), using CSS vars
  instead of the old hardcoded muted color.

Backups: `chatRenderer.js.bak-20260806-menu`, `style.css.bak-20260806-menu`.
Verified: `node --check` clean, CSS braces balanced (7706/7706).

## 2026-08-06 — feat(chat): ALL message actions permanently pinned, overflow (···) menu removed

Request (on top of the Continue feature): no more recency-sorted visible/overflow
split — every message tool shows at all times on every block. The ··· "More
actions" menu is gone entirely.

CHANGED:
- `static/js/chatRenderer.js` — `createMsgFooter` (assistant) now renders ALL
  available actions inline in `allActions` order: copy, edit, regen, continue,
  shorten, explain, fork, delete (TTS still filtered via `available`).
  `createUserMsgFooter` (user) renders all 4: edit, delete, copy, resend.
  Removed the whole recency machinery: `_MAX_VISIBLE`, `_ACTION_RECENTS_KEY` /
  `_getRecentActions` / `_trackAction`, `_USER_ACTION_RECENTS_KEY` /
  `_getUserRecentActions` / `_trackUserAction`, the `visible`/`overflow` slice,
  the "···" more-button, and the overflow popup menu in both builders. No more
  button shuffle on use — fixed order, all pinned. (`bindMenuDismiss` import
  kept — still used by the ctx-ring pill and other popups.)
- `static/style.css` — removed dead `.msg-more-btn`, `.msg-overflow-menu`,
  `.msg-overflow-item`, `.overflow-icon` rules; `.msg-actions` gained
  `flex-wrap: wrap` so the 8-button row folds gracefully on narrow widths
  (`.msg-footer` already wrapped).

NOT CHANGED: actions themselves (same handlers as before), stopped-indicator /
anti-stall in-body buttons, version tokens (SW is network-first for
/static/*.js), sw.js. Stale `odysseus-msg-actions-recent` /
`odysseus-user-actions-recent` localStorage keys are simply ignored now
(no migration needed — dead data).

Receipts: backups `static/js/chatRenderer.js.bak-20260806-pinall`,
`static/style.css.bak-20260806-pinall`. Verified: `node --check` clean on
chatRenderer.js; grep confirms zero leftover refs (`_MAX_VISIBLE`,
`_getRecentActions`, `_trackAction`, `msg-overflow`, `msg-more-btn`). Live
after a normal browser reload (no uvicorn restart needed — static assets).

## 2026-08-06 — feat(chat): always-visible Continue action on every assistant message

Request: a Continue button on ALL assistant blocks at all times (like Regenerate
From Here / Fork Conversation), so a dead/errored turn can be resumed with one
click instead of typing "boop"/"poke" nudges.

CHANGED:
- `static/js/chatRenderer.js` — `createMsgFooter` `allActions` now includes a
  `continue` action (▸, title "Continue"), placed after "Regenerate from here".
  Same resume flow as the "[Message interrupted]" button: `setHideUserBubble()`
  + `setPendingContinue(msgElement)`, then injects
  "Your previous response ended with: <last 500 chars> … Continue exactly from
  where you left off." and fires send. Prefers `dataset.raw`, falls back to
  `.body` textContent, and strips a trailing `[Error: …]` note so errored
  messages continue from their real cutoff. Subject to the same recency-sorted
  visible/overflow (···) logic as every other action — shows on all assistant
  footers, history-rendered included (addMessage path).
- `static/js/chat.js` — stream-error path (non-abort, non-auto-recoverable):
  partial content is now PRESERVED instead of wiped — `holder.dataset.raw =
  accumulated`, body re-rendered from it, `[Error: …]` note appended as a
  `stopped-indicator` (previously `typewriterInto` cleared the bubble and typed
  the error over the content). Errored blocks also get the standard `msg-footer`
  action row (they had none before), so Continue/Regenerate/Fork/Delete are
  reachable exactly when the turn dies. Empty-content errors keep the old
  typewriter error text; footer still attached when a holder exists.

NOT CHANGED: stopped-indicator in-body Continue buttons (still present),
anti-stall "Paused mid-task" button, `_tryAutoRecover` auto-nudge, version
tokens (SW is network-first for /static/*.js — reload picks it up), sw.js
(precache list untouched, no CACHE_NAME bump).

Receipts: backups `static/js/chat.js.bak-20260806-continue`,
`static/js/chatRenderer.js.bak-20260806-continue`. Verified: `node --check`
(input-type=module) clean on both files. Live after a normal browser reload
(no uvicorn restart needed — static assets).

## 2026-08-06 — rollback: custom auto-title work reverted to STOCK (SUPERSEDES the "Tab Titles and Retitling" 08-06 entry and the 08-05 auto-title port)

User decision: roll back the fork's auto-title additions and let stock Odysseus
auto-naming (first-message, server-side background task) do the job.

REVERTED (restored to stock HEAD):
- `routes/chat_helpers.py` — `auto_name_session` back to stock first-message-only
  (was: head+tail context excerpt + `_clean_title` echo guard).
- `routes/session_routes.py` — `POST /session/{sid}/retitle` route, `_clean_title`,
  and `_ECHO_PHRASES` removed entirely.
- `static/js/sessions.js` — tab-title mirror IIFE (08-06) and the Auto-title
  dropdown item (08-05) removed. Ghost-message fix hunks (NewChatIntent clear +
  hash persist) KEPT.
- `static/index.html` — sessions.js refs back to `?v=20260805unified2` (was
  `20260806tabtitle1`). This also repairs the 08-06 split-brain: all 18 refs are
  on the unified2 token again → single module instance.
- `static/sw.js` — CACHE_NAME → `odysseus-v383-stocktitle`; sessions.js precache
  back to `?v=20260805unified2`.

KEPT: markerfont (style.css `20260806markerfont1`), ghost-fix version tokens, and
all other 08-05/08-06 work (agent all-tools, markdown, theme, etc.).

Known behavior after rollback: stock auto-namer still runs server-side in the
background (sidebar shows the name on next session-list render); the open chat
header `#current-meta` still catches up on reload/re-select — that lag is stock
behavior, unchanged.

## 2026-08-06 — fix: force-mode regression reverted + genuine thinking marked (SUPERSEDES the "content deltas force-neutralized" entry below)

Regression report: "thought blocks now even more broken — Odysseus no longer knows
what truly is a thought and where the reply actually begins." Root cause: the
force-mode content neutralization was built on a FALSE premise — "content deltas
can never contain genuine thinking tags". They CAN: the backend delivers genuine
think tags in UNFLAGGED content deltas on (a) the Ollama stream path (only
`message.get("thinking")` is flagged; `<think>` tags in content pass raw), and
(b) the OpenAI-compat path for name-recognized thinking models — the content
auto-detect has a `not _thinking_model` guard, so their literal `<think>…</think>`
content is never routed and arrives unflagged. Force mode escaped all of it →
genuine thought blocks became literal reply text.

New design — the delta layer MARKS genuine thinking, the neutralizer trusts the mark:
- **`static/js/chat.js`** — the UI wraps json.thinking deltas as `<think real="1">`
  (was plain `<think>`); the close stays `</think>`. The mark survives extraction
  (attribute-tolerant regexes) and the time-embedding at finalize (rewritten to
  preserve attributes).
- **`static/js/chat.js`** — force-mode content neutralization REVERTED (content
  deltas flow raw again). The thinking-in-progress gate narrowed from
  "hasUnclosedThinkTag on the whole accumulated text" to: UI wrapper state
  (`_thinkOpen`) OR a stream-start `<think>` opener not yet closed. The reply
  can never flip the gate — quoted line-start tags (stress-test case 4/6) can no
  longer open a second thinking box that swallows the response.
- **`static/js/markdown.js`** — `neutralizeStrayThinkTags` opener rule: genuine iff
  marked (`real="1"`) OR at the very start of the stream; a quoted line-start tag
  mid-reply is now content. Close survives only while a genuine block is open.
  Also fixed: `</mm:think>` closes were never matched (TOKEN_RE/CLOSE_RE now take
  the `mm:` prefix) — they slipped past neutralization and tripped orphan-close
  handling. Fenced-code tags are placeholder-escaped too, so extractThinkingBlocks
  can no longer eat a tag inside a code block as a thinking block (renders as
  literal code instead).
- Known accepted edge (nothing lost): un-flagged content-delivered ROUND-2
  thinking (exotic: Ollama + a tags-in-content model mid-tool-loop) degrades to
  literal text instead of a box; flagged multi-round thinking is preserved via
  the mark. Stored/reload text has no marks → uses the stream-start rule
  (genuine round 1 at message start still boxes correctly).
- Verified: 39/39 unit tests (flagged + content-delivered + repair paths, full
  13-case stress with chunked deltas: gate never flips mid-reply, exactly one
  real block, ALL quoted tags render literal; multi-round; mid-line marked
  opener). `node --check` clean on both files.
- Backups: git tracks both files; `static/js/markdown.js.bak-20260806-thinkfix`
  (pre-session original) remains the full revert point.

## 2026-08-06 — fix: reasoning that QUOTES a think tag no longer leaks the thought block

User report: the model's own thinking (which was reasoning ABOUT think tags, and
therefore contained a literal close tag mid-reasoning) leaked out of the thought
block — the quoted close tag inside the reasoning terminated the block early,
spilled the rest of the thought into the reply area, and orphanned the UI's real
close tag (which then rendered as visible text). The model thinking about the
think-tag bug triggered the think-tag bug.

- **`static/js/chat.js`** — `json.thinking` deltas are now passed through
  `markdownModule.neutralizeStrayThinkTags(_delta, true)` BEFORE the UI wraps
  them in `<think real="1">…</think>`. Reasoning content is genuine thinking,
  but it can quote a think tag as text — neutralizing it first makes the
  wrapper's own marked tags the ONLY boundary. Quoted tags inside reasoning now
  render as literal text INSIDE the box (restored from placeholders by
  `restoreThinkTags` in `_flushLiveThink`), and the reply always starts at the
  real close.
- Verified: 52/52 tests including the leak reproduction (reasoning containing a
  literal close tag mid-thought → block captures the FULL reasoning, quoted tag
  literal inside the box, reply clean, no tail leak); `node --check` clean on
  both files. Backups: git tracked.

## 2026-08-06 — fix: think-box scroll counts as engagement (stay-open on completion)

Per Sir: scrolling inside the live thinking box is a stronger "I'm reading this"
signal than a click (he'd never click a block he wants to keep open). The
think-box scroll-intent listener already echo-ignored our own programmatic pins,
so it only fires on REAL user scrolls — added `_liveThinkUserEngaged = true`
there, giving scroll the same engagement weight as click/focusin. Completion
preserve-open logic (all three transitions + finalize) now keeps the block open
for anyone who actually read it, whether they clicked, focused, or just scrolled.

- `static/js/chat.js` — `_liveThinkUserEngaged = true` inside the live-box
  scroll listener (post echo-ignore), alongside the existing `_liveThinkBoxFollow`
  intent tracking.
- Verified: `node --check` clean; engagement trip sites confirmed at
  click (2585), focusin (2586), scroll (2594).
- Backup: `static/js/chat.js.bak-20260806-scrollengage`.
- Frontend-only: hard-refresh to pick up.

## 2026-08-06 — fix: content deltas force-neutralized at accumulation (quoted tags can no longer open a second think box)

Follow-up to the quoted-think-tag fix. Stress-test round 2 exposed a hole:
a quoted think OPENER at a LINE START inside the REPLY (indistinguishable from
genuine thinking by design) was kept raw by the boundary rule, an orphan opener
(single line `<think>` with no close) left the neutralizer's block state "open",
and `hasUnclosedThinkTag` flipped TRUE mid-reply — the stream then created a
SECOND thinking box fed with the entire accumulated text, swallowing the
response into the thought block ("reply got tucked into the thought box").

Root cause: the boundary rule guesses content-vs-thinking from tag position at
render time, but the STREAMING LAYER already KNOWS — `json.thinking` flags which
deltas are real reasoning. Genuine think tags are UI-inserted; content deltas can
never contain them. So content no longer needs guessing.

- **`static/js/chat.js`** — the delta handler now runs every non-thinking delta
  through `neutralizeStrayThinkTags(delta, true)` (force mode) before it hits
  `accumulated`/`roundText` (including the content that rides in with the
  `</think>` close-prepend). Any think-family tag in reply content is quoted
  content, period — position irrelevant.
- **`static/js/markdown.js`** — `neutralizeStrayThinkTags(text, force)`: new
  force mode escapes ALL think-family tags (fences included — a tag in a code
  block is content too) plus a trailing partial tag prefix, so a tag split
  across stream deltas can never reform into a control boundary. The boundary
  rule remains for the render/reload re-pass (stored messages still carry raw
  tags server-side).
- Known trade-off: reload of PRE-fix stored messages still uses the boundary
  rule — a quoted line-start pair in old stored text renders as a thinking box
  (nothing lost, cosmetic). New messages are fully safe.
- Verified: 31/31 tests against the shipped functions, including a full
  stress-test simulation (all 13 tag cases, reply chunked into 7-char deltas to
  force tag-splitting): think gate stays false on every content tick, exactly
  one real thinking block, every literal tag restored as visible text, nothing
  lost; multi-round genuine thinking regression clean. Both files pass
  `node --check`.

## 2026-08-06 — fix: close live think box at completion unless user engaged

User test (hands off kb+mouse): thought block stayed open with zero clicks.
Root cause: the thinking-ended transitions (normal `</think>` close, stream-done
force-close, tool_start force-close) set the header text to "View thinking
process" but never removed the `expanded` class — and the `_liveReplyEl`
preserve branch keeps the live box as-is, so an untouched box stayed open. The
finalize gate only guarded the full-re-render path.

Fix: all three transitions now call
`markdownModule.setThinkingExpanded(content, toggle, header, false)` when
`!_liveThinkUserEngaged` — no click/focus = default closed (matches user spec:
only engaged boxes stay open). Engaged boxes keep whatever state the user left
(open stays open, closed stays closed). Finalize gate unchanged — a
transition-collapsed box won't re-expand or persist its hash.

- `static/js/chat.js`: collapse guards at 2681 (normal close), 2376
  (stream-done), 3090 (tool_start).
- Verified: `node --check` OK; 3 collapse sites grep-confirmed.
- Backup: `chat.js.bak-20260806-engageclose`.

## 2026-08-06 — fix: thinking streams at monitor refresh (rAF, was 30ms timer)

Follow-up to the 33fps entry below: thinking now flushes on
`requestAnimationFrame` instead of a `setTimeout` — one delta-append per
display frame, the same cadence the browser uses to paint the reply, so
thinking visually matches the message stream ("240hz feel" per user; the reply
also only repaints per frame, so this is the max the display can show).

- `static/js/chat.js`: `_cancelLiveThinkFlush` now uses `cancelAnimationFrame`;
  the live-think hot path schedules with `requestAnimationFrame(_flushLiveThink)`
  instead of `setTimeout(..., 30)`. The `if (!_liveThinkFlushTimer)` guard
  coalesces every chunk's stash into exactly one frame-flush; stream-end force
  flushes run directly (not via rAF) so the box always completes even if the
  tab is backgrounded and rAF pauses.
- Verified: `node --check static/js/chat.js` clean; all `_liveThinkFlushTimer`
  refs consistent (declare / cancelAnimationFrame / requestAnimationFrame).
- Backup: `static/js/chat.js.bak-20260806-rathink`.

## 2026-08-06 — fix: thinking text streams at ~33fps (was chunked ~7fps)

User report: thinking blocks updated in visible small chunks while the reply
after them streamed seamlessly. Root cause: the live-think hot path coalesced
flushes into a 150ms timer (~7 updates/sec) — a cadence tuned for the OLD
O(n²) full-markdown rebuild. The flush is now a cheap delta-append
(`insertAdjacentText` of only the new suffix, full `mdToHtml` rebuild only on
force / normalization-shrink / >2000-char jumps), so the 150ms throttle was
pure artifact.

- `static/js/chat.js` hot path: `setTimeout(_flushLiveThink, 150)` →
  `setTimeout(_flushLiveThink, 30)` (~33fps, visually seamless like the reply).
  Comment updated to document why the cadence is safe now.
- Delta-append + `_liveThinkLastLen` tracking were already in place (landed
  with the earlier thinking fix); this change only speeds up the pump.
- Verified: `node --check static/js/chat.js` clean; `restoreThinkTags` exists
  in markdown.js (used by the flush).
- Backup: `static/js/chat.js.bak-20260806-thinkcadence`.

## 2026-08-06 — fix: quoted think-tags no longer chop the message (content-neutralization + placeholder round-trip)

User report: a response that merely QUOTED the literal think tag mid-sentence
(e.g. "each round's `<think>` from metadata.round_reasonings[i]") was treated by
the think machinery as an unclosed thinking-block opener → the live stream showed
a bare "Thinking" box and hid everything after the tag, and reload/finalize
dropped everything from the tag onward. Priority: NOTHING lost — thoughts or
response — while genuine think-block parsing stays fully intact.

- **`static/js/markdown.js`** — new `neutralizeStrayThinkTags()`: fence-aware,
  boundary-aware single pass. A think-family opener (think/thinking/thought/
  mm:think/channel variants) is only a REAL block boundary at start-of-message or
  start-of-line; a closer is only real if it closes a real block. Quoted opens,
  orphan closers, and tags inside code fences become unique hex placeholder
  tokens (`__THINKPH_<hex>__`) — invisible to the parser, cannot trigger the
  state machine. Hooked at the top of `normalizeThinkingMarkup()`, the single
  choke point every path funnels through (streaming lambda, `hasUnclosedThinkTag`,
  `extractThinkingBlocks`, `processWithThinking`, reload/finalize).
- **`static/js/markdown.js`** — new exported `restoreThinkTags()`: restores the
  placeholder tokens to literal tags AFTER extraction but BEFORE the markdown
  renderer runs, so the renderer escapes each tag exactly once and the browser
  shows real brackets (first attempt used HTML entities and double-escaped into
  a visible `&lt;think&gt;` — replaced by the placeholder round-trip).
- **`static/js/markdown.js`** — `extractThinkingBlocks()` now restores both
  thinkingBlocks and content before returning; the unclosed-opener branch changed
  from "drop everything from the tag onward" to "strip opener(s), keep the tail"
  (that drop was the literal chop — nothing-lost rule).
- **`static/js/markdown.js`** — fixed a PRE-EXISTING multi-round bug: the
  malformed-block collapse regex (`<think>.{0,30}</think>\s*([\s\S]*?)</think>`)
  swallowed the second opener of legitimate consecutive thinking blocks whenever
  the first block was ≤30 chars, gluing round1+round2 into one corrupted blob.
  The middle group is now a tempered token that refuses to cross into another
  opener; the intended collapse of genuinely malformed empty/short blocks still
  works (regression-tested).
- **`static/js/chat.js`** — `_replyAfterClosedThinking()` restores placeholders in
  the reply text before rendering; `_flushLiveThink()` restores the live thinking
  box text after the tag-strip chain.
- Verified: 25/25 unit tests against the shipped functions (incident case,
  genuine blocks, multi-round, malformed collapses, fences, orphan closers,
  channel tags, round-trip fidelity, idempotency); both files pass `node --check`.
- Streaming state-machine simulation (node, real shipped functions + UI
  delta-wrapping + hasUnclosedThink/false-close logic): a stress-test delta
  sequence containing literal open AND close tag deltas keeps hasUnclosedThink
  false on every tick and renders thinking + reply intact — including the
  pre-fix failure mode where the entity-based attempt escaped the UI's own
  real mid-line close tag and left the think box permanently unclosed.
- Backups: `static/js/markdown.js.bak-20260806-thinkfix` (pre-change);
  `static/js/chat.js` edits tracked by git.

## 2026-08-06 — fix: thinking-UI auto-scroll stick + incremental think streaming + click-gated preserve-open

User report: thinking blocks no longer auto-scroll smoothly while the LLM is
actively thinking ("sometimes it sticks, then eventually unsticks and doesnt
scroll"); blocks stream in visible chunks instead of flowing like the reply;
and completed thought blocks auto-stay-open even when never touched.

- **`static/js/ui.js`** — `scrollHistory()`: removed the 500ms restart throttle.
  The lerp finished → `_scrollRafId` went null → the next flush's scroll request
  was throttled for up to 500ms while content kept growing → the freeze ("sticks,
  then unsticks"). Now the lerp restarts on every flush while the user is at the
  bottom; manual-scroll protection is `_userScrolledAway` intent tracking (scroll
  listener), not a time gate. (Also removed the old `diff > 300` bail, which
  misread stream growth as a manual scroll-up — replaced by intent tracking.)
- **`static/js/chat.js`** — `_flushLiveThink()`: thinking text now streams
  **incrementally** — append only the delta since the last flush via
  `insertAdjacentText` (matching the reply's continuous stream) instead of a full
  `innerHTML` markdown rebuild every ~150ms (the visible chunking). Full rebuild
  only on `force` (completion), on normalization-shrink, or on a >2000-char jump.
- **`static/js/chat.js`** — think-box pinning: replaced the `nearBottom < 80`
  gate (which gave up forever once a single flush grew the box >80px — growth
  doesn't fire scroll events, so it never recovered) with user-intent tracking on
  the box itself: a scroll listener flips `_liveThinkBoxFollow`, our own pins are
  echo-ignored via `_liveThinkBoxLastPin`. Box follows its bottom while you
  follow it; scroll up inside the box → we stop; scroll back down → we resume.
- **`static/js/chat.js`** — preserve-open on completion is now **click-gated**:
  `_liveThinkUserEngaged` is set only when the user clicks/focuses the live box
  (capture-phase listeners at creation). Finalize preserves + persists the open
  state only if engaged AND expanded — a default-open box the user never touched
  no longer gets its hash persisted (which was leaving every block open forever).
- Backups: `static/js/ui.js.bak-20260806-scrollfix`,
  `static/js/chat.js.bak-20260806-thinkfix`. Both files pass `node --check`.



User reported "send GIFs + Videos through Odysseus so VLM can view frames"; the
working GIF concept lived in the `.dev` fork (`.old`'s 08-04 entry, "GIF vars NOT
present in odysseus.old/src"), and `-garbo` is the LIVE instance (127.0.0.1:7001).
Ported the concept here + added video support. A GIF/video attachment is now split
into JPEG frames (env-driven sampling) and sent as multiple `image_url` blocks so
the VL model sees the sequence instead of one frozen first frame.

- **`src/document_processor.py`** — added `_gif_sample_config()` /
  `_gif_frames_as_jpeg()` (ported from `.dev`: GIF_SAMPLE_MODE fps|fixed, GIF_FPS,
  GIF_MAX_FRAMES, real per-frame GIF timing) and `_video_sample_config()` /
  `_video_frames_as_jpeg()` (new, ffmpeg: VIDEO_SAMPLE_MODE fps|fixed, VIDEO_FPS,
  VIDEO_MAX_FRAMES; ffprobe duration → even stride; MJPEG piped to stdout and split
  on JPEG markers via `_split_jpeg_stream()`). Both wired into
  `analyze_image_with_vl_result()` (multi-frame `image_blocks`) and
  `build_user_content()` (GIF frames in the image branch; new video branch emits
  image_url blocks, text-note fallback when extraction fails). Added
  `VIDEO_EXTENSIONS` constant. NaN/Inf env guard via `math.isfinite`.
- **`src/upload_handler.py`** — added `is_video_file()` (mime-aware so
  `audio/webm` stays audio; ext set .mp4/.mov/.webm/.mkv/.m4v/.avi). `save_upload`
  now lets videos ride `ODYSSEUS_CHAT_VIDEO_UPLOAD_MAX_BYTES` (default 200MB)
  instead of the 10MB chat cap.
- **`src/upload_limits.py`** — added `get_chat_video_upload_max_bytes()` +
  env `ODYSSEUS_CHAT_VIDEO_UPLOAD_MAX_BYTES` (default 200MB).
- **`src/chat_helpers.py`** — `validate_file_upload` allowlist gains
  .mp4/.mov/.mkv/.m4v/.avi.
- **`src/chat_handler.py`** — vision path treats videos like images:
  `[Video attached: …]` / `[Video: …]` labels, VL description for text-only
  main models (frames via build_user_content for vision models).
- **`.env` / `.env.example`** — GIF_SAMPLE_MODE/GIF_FPS/GIF_MAX_FRAMES,
  VIDEO_SAMPLE_MODE/VIDEO_FPS/VIDEO_MAX_FRAMES, ODYSSEUS_CHAT_VIDEO_UPLOAD_MAX_BYTES
  documented (defaults active without explicit set).
- **`tests/test_gif_video_frames.py`** (new) — 13 tests: config env resolution
  (incl. NaN/Inf), GIF fps/fixed/static, video fps/fixed via real ffmpeg, missing
  ffmpeg fallback, JPEG stream split, mime-aware is_video_file, build_user_content
  video frames + no-frame fallback. Full upload/document suite: 90 passed.
- Backups: `src/document_processor.py` changes are git-tracked (see `git diff`);
  no .bak written for new files. Service restart required to activate.

## 2026-08-06 — fix: thinking-box auto-scroll + open-state preservation

User-reported: during streaming, the page auto-scroll "sticks, then unsticks and
doesn't scroll" mid-think; also the thinking box force-closes when the round
completes even if left open, and manual scrolling isn't respected while thinking.

- **`static/js/ui.js`** — replaced the `diff > 300` bail in `_smoothScrollStep`
  (which misread stream growth as a manual scroll-up and froze the lerp) with
  real user-intent tracking: a `scroll` listener on `#chat-history` sets
  `_userScrolledAway` when the user scrolls away from the bottom, clears it when
  they return; `scrollHistory()` and the lerp both respect it. Auto-scroll now
  keeps up with streaming, and manual scrolling is never fought.
- **`static/js/markdown.js`** — exposed `hashThinkingContent`, `setThinkingExpanded`,
  `loadExpandedSet`, `saveExpandedSet` on the module (were private).
- **`static/js/chat.js`** — finalize full re-render (empty-reply path) now
  preserves an open live think box: captures the live box's expanded state +
  text before the innerHTML wipe, re-expands the matching freshly rendered
  static `.thinking-section`, and persists its content hash so reloads honor it.
- Backups: `ui.js.bak-20260806-scrollfix`, `markdown.js.bak-20260806-thinkexp`,
  `chat.js.bak-20260806-thinkfinalize`. All three `node --check` clean.
- Scope verified: `_liveThinkContent` (chat.js:2080) and the finalize block
  (chat.js:3636) share `handleChatSubmit` (1003–4114) — no ReferenceError risk.

## 2026-08-06 — fix: teacher escalation import break (post-#3629 relocation)

`_call_teacher` in `src/teacher_escalation.py` ImportError'd at runtime every time the
escalation hook fired: it imported `_TEACHER_SYSTEM_PROMPT` from `src.ai_interaction`,
but the tool→registry migration (#3629) moved the model-interaction tools — and that
constant — into `src/agent_tools/model_interaction_tools.py`. Symptom log line:
"teacher escalation hook failed: cannot import name '_TEACHER_SYSTEM_PROMPT'".

- **`src/teacher_escalation.py`**: `_call_teacher` now imports `_resolve_model` from
  `src.ai_interaction` (still its home) and `_TEACHER_SYSTEM_PROMPT` from the
  post-#3629 location with an ImportError fallback to the old home (.old parity).
- Verified: module import + exact traceback import block both resolve; `py_compile` clean.
- Backup: `src/teacher_escalation.py.bak-20260806-teacherfix`.
- Note: `data/settings.json` still has `teacher_enabled: true` +
  `teacher_model: deepseek-v4-flash-free@opencode.ai` (transplant copy) — escalation
  now genuinely runs on failed rounds. Garbo's UI has no teacher-model knob; the
  settings.json keys are the only switch.

## 2026-08-06 — feat: 24/7 all-tools mode (`agent_list_all_tools`)

Agent mode no longer RAG-filters the tool catalog by default. New setting
`agent_list_all_tools` (default **True**) bypasses the RAG/keyword/domain tool
selection entirely, so every agent round sends the FULL catalog — complete
prompt sections + all native schemas + all MCP schemas — instead of a
retrieval-selected subset.

- **`src/settings.py`**: added `"agent_list_all_tools": True` to
  `DEFAULT_SETTINGS` (next to `agent_stream_timeout_seconds`). Global setting,
  not per-user.
- **`src/agent_loop.py`** (stream_agent_loop): sets `_all_tools_mode =
  bool(get_setting("agent_list_all_tools", True))` right after `_relevant_tools
  = relevant_tools`; when on, forces `_relevant_tools = None` and logs
  `[tool-rag] agent_list_all_tools=True — full tool catalog, RAG selection
  bypassed`. Since `_build_system_prompt` (line ~3686) and the per-round schema
  assembly both read `_relevant_tools`, the prompt and schema list both go full.
  The selection branches that key off `not _relevant_tools` (low-signal
  read-only file tools, RAG retrieval, keyword fallback) are each additionally
  gated with `not _all_tools_mode` — otherwise a falsy-but-None set would let
  them re-filter. Same gate added to the `uploaded_files` and `forced_tools`
  re-set blocks, which otherwise re-collapse the catalog to a subset when a
  file is attached or force-tools are set. The `_relevant_tools is not None`
  branches (domain seeding, active-document union, browser-MCP expand,
  skill-prescribed tools, finetune clamps, doc-irrelevant prune) self-skip
  with the forced None, so nothing re-filters downstream.
- **Local models too**: the per-round schema assembly previously injected MCP
  schemas only when the user message matched `_MCP_KEYWORDS`; in all-tools mode
  `_wants_mcp` is forced True, so local-model rounds also ship every MCP schema
  (native function schemas stay prompt-only for local models, which call tools
  via fenced code blocks / `<tool_code>`).
- **Unchanged, intentionally**: `_force_answer` (loop-breaker), `disabled_tools`
  (user's explicit disable list), `_ody_qwen_finetune_model` (finetune-trained
  to emit tools from the domain prompt), and `_needs_admin` admin-section gating
  all still apply.
- **To revert**: set `agent_list_all_tools` to False (settings DB / admin) — the
  RAG/keyword selection path is untouched and returns as-is.
- Backups: `src/settings.py.bak-20260806`, `src/agent_loop.py.bak-20260806-alltools`.

## 2026-08-06 — fix: port reasoning_content lifecycle (DeepSeek thinking 400s)

Ported the `.old` reasoning_content fix into garbo; two gaps remained and are
now closed. Root cause of `opencode.ai returned HTTP 400 ... The reasoning_content
in the thinking mode must be passed back to the API`: garbo stores the thinking
blob in `metadata["thinking"]` (frontend <think> rebuild) but never maps it back
onto the outbound assistant message, and the agent-loop strip removed reasoning
from every prior assistant turn — so any follow-up request in thinking mode went
out naked.

- **`src/llm_core.py` `_sanitize_llm_messages`**: promote persisted
  `metadata["thinking"]` / `metadata["reasoning_content"]` / `metadata["reasoning"]`
  → top-level `reasoning_content` on assistant messages, before the allow-list
  filter runs (metadata itself stays stripped from the wire; in-loop top-level
  reasoning always wins). Covers plain chat, agent loop, and rewrites — every
  provider path funnels through sanitize.
- **`src/llm_core.py` `_disable_deepseek_v4_thinking`**: symmetric guard — when
  thinking is disabled, scrub `reasoning_content` from payload messages so a
  thinking-off request never carries reasoning blobs.
- **`src/agent_loop.py` `_append_tool_results`**: strip is now tool_calls-aware —
  assistant turns with `tool_calls` keep their reasoning (DeepSeek/Moonshot
  thinking mode requires it on the follow-up request), plain-prose turns still
  get stripped (Nemotron re-injects every prior reasoning as <think>; bounded to
  one reasoning blob per tool round).
- **Tests**: `tests/test_sanitize_promotes_metadata_thinking.py` — promotion,
  precedence, no-leak for user/tool, disable-scrub, non-deepseek untouched.
- **Ops**: restart the odysseus service to pick up the Python changes.

## 2026-08-06 — feat: chat name in browser tab title + context-aware auto-title

Reimplemented both features in the garbo fork. The tab-title feature was
missing entirely here (route pages had titles, the chat pane never did);
the auto-title path still titled from the first message only.

- **Tab title** (`static/js/sessions.js`): new `_mirrorTabTitle()` IIFE — a
  MutationObserver on `#current-meta` mirrors the active chat name into
  `document.title` (`<name> — Odysseus`, fallback `Odysseus Chat`). One hook
  covers every writer (selectSession, retitle, rename, new-chat, archive-peek,
  email inbox, shortcuts) with zero call-site changes. Pathname-guarded to `/`
  so route pages (calendar, notes, ...) keep their own titles.
- **SW** (`static/sw.js`): sessions.js precache entry bumped to
  `?v=20260806tabtitle1`; CACHE_NAME v380 → v381. `static/index.html`:
  modulepreload + script tag both bumped to the same query.
- **Auto-title** (`routes/chat_helpers.py` `auto_name_session`): now titles
  from a head+tail context excerpt (first 2 + last 12 non-summary messages,
  each capped at 400 chars, total capped 6000) instead of the first user
  message only — same context shape as the retitle button, so titles track
  topic evolution. New sessions still work (first message IS the whole
  excerpt). Prompt updated to "Name this conversation: ...".
- **Auto-title guard**: after `strip_think`, output now also runs through the
  retitle route's shared `_clean_title` (lazy import, no circularity) — echo
  phrases + >12-word rejection, so an echoed instruction can never become a
  chat name (the `.old` "We need answer with title 6 words or fewer..." bug).
  Falls back to the old inline guard if the import ever fails.
- **Tests**: `node --check` clean on sessions.js; `py_compile` clean on
  chat_helpers.py; live end-to-end mock-session run against the real default
  endpoint (opencode.ai free tier) produced `"Tab Titles and Retitling"` from
  an evolved 6-message convo — context-aware, guard-passed, renamed.
- **Ops**: restart `odysseus.service` for the Python change; hard refresh
  (SW v381) for the JS change. No backups needed (text edits, git tree).

## 2026-08-06 — fix: subscript `~text~` + verify live serving (follow-up)

- **Parser** (`static/js/markdown.js`): added `~text~` → `<sub>` (single line,
  no spaces/nested tildes; runs after `~~strike~~` so `<del>` is untouched;
  `\~` escape stays literal). Completes the sub/sup pair from the original
  request (`H~2~O` + `x^2^`).
- **CSS** (`static/style.css`): added `.msg sub` (mirrors `.msg sup`).
- **SW** (`static/sw.js`): CACHE_NAME v379 → v380 (markdown.js/style.css changed).
- **Tests**: `markdown_formatting_fixes.mjs` now 57 checks (sub, sup, combined,
  escaped tilde, strike-vs-sub collision).
- **Verified**: node parser suite 57/57; live `127.0.0.1:7001` serves files
  hash-matching disk (curl). NOTE: `127.0.0.1:7000` is still the OLD `.old`
  fork's server (hash-verified serving pre-fix code) — point the browser at
  7001 or restart/stop the 7000 instance.

## 2026-08-06 — fix: markdown formatting gaps (highlight, sup, escapes, nested lists/quotes, task check)

- **Parser** (`static/js/markdown.js`):
  - `==text==` → `<mark>`; `^text^` → `<sup>` (single-line, no nested carets).
  - Backslash escapes now actually escape: `\X` for markdown-significant chars
    (`\*` `\[` `\#` `\$` `\<` `\>` `\|` `\\` ...) is placeholder-protected right
    after code extraction and restored last, entity-encoded (`\<` → `&lt;`) so an
    escaped angle bracket can never smuggle raw HTML back into the DOM. Code
    blocks/inline code keep backslashes untouched.
  - Lists rebuilt as one recursive builder (replaces the flat ordered/task/
    unordered passes). Fixes: blank lines between items no longer split the list
    into separate single-item `<ol>`s ("1. 1." bug — now one loose list);
    indented items (2+ spaces) nest; `- [ ]`/`- [x]` task items work at any
    depth; a marker-type change (ul↔ol) at the same indent starts a fresh list.
  - Blockquotes rebuilt: `>` / `>>` / `>>>` now nest properly; blank lines
    inside a quote region keep it as one block (CommonMark loose behavior).
- **CSS** (`static/style.css`): task-check `::after` checkmark now draws in
  `var(--fg)` (was `var(--bg)` → invisible on the accent fill in dark theme)
  and is bigger (5×9); added `.msg mark`, `.msg sup`, `.msg blockquote
  blockquote` depth stripe, and task-text flex + nested-list wrap rules.
- **SW** (`static/sw.js`): CACHE_NAME v378 → v379 — markdown.js/style.css are
  precached, so the bump is required for the fixes to reach the browser.
- **Tests**: new `tests/markdown_formatting_fixes.mjs` (52 checks, vm harness)
  and `tests/markdown_browser_check.py` (14 checks, headless Chromium against
  the real style.css + sanitizer + computed styles). Existing
  `markdown_codefence_placeholder_regression.mjs` still green.

Receipts: git working tree. No backups needed (text edits, fully reversible).
Verify in browser with a hard refresh (SW v379).

## 2026-08-06 — fix: live-thinking box was O(n²) per chunk (tab sandblast)

- Root cause: while a model streams reasoning, `chat.js`'s SSE hot path
  (`hasUnclosedThink && isThinking` branch) rebuilt the **entire accumulated
  thinking blob** on **every token**: strip wrappers → 5 whole-string regexes →
  token estimate → full `mdToHtml` → `innerHTML` replace → scrollHistory.
  Growing blob × per-token re-parse = O(n²); the longer the think, the worse
  the jank (matches the reported "tab slows as soon as it thinks for a while").
  Ironic: the answer stream was already fixed for this (streamingRenderer),
  but the thinking UI bypassed it.
- Fix (all in `static/js/chat.js`):
  - Per-chunk hot path is now O(1): stash `roundText`, schedule a flush.
  - `_flushLiveThink()` coalesces the heavy rebuild to ~1 flush / 150 ms.
  - Collapsed thinking box skips the markdown rebuild entirely (header stats
    stay live); final flushes pass `force=true` so the finished box is always
    complete even if it was collapsed while streaming.
  - Timer text write guarded (was rewriting identical textContent at 60 fps via
    rAF; `toFixed(1)` only changes ~1/s).
  - Initial render fires immediately at box creation; all three force-close
    paths (stream-done, thinking-ended, tool_start) flush pending text first.
- Backup: `static/js/chat.js.bak-thinkfix`. `node --check` clean.

## 2026-08-06 — fix: agent_tools re-export of _active_user_text (boot fix)

- Port #5 (user-nominated paths) bound `_active_user_text` in `src/tool_execution.py`
  but `src/agent_loop.py` imports it via `src.agent_tools`.
- The `agent_tools/__init__.py` re-export list only forwarded `execute_tool_block`
  and `format_tool_result` → uvicorn boot died with
  `ImportError: cannot import name '_active_user_text' from 'src.agent_tools'`.
- Fix: added `_active_user_text` and `get_active_user_text` to the
  `from src.tool_execution import (...)` re-export block.
- Verified: `./venv/bin/python -c "import app"` → app.py imports OK, all routes init.

## 2026-08-05 — port: green-lit .old fixes into garbo (preamble, preset, extractor, paths, favicon)

What changed:
- Agent preamble: "You are an AI assistant with tool access" → "You have tool access in this session" at all identity-declaring sites in src/agent_loop.py (main + compact `_assemble_prompt` paths) — capability framing, not identity, so agent-mode thinking/answers stop flipping to analyst register.
- Custom preset (`data/presets.json`): "Custom" now carries the full I.R.I.S. persona (45,414-char system prompt, temperature 1.0, enabled) ported from `.old`.
- `services/memory/memory_extractor.py`: merged `.old`'s refined extraction rules (MAX 3 facts, stand-alone 15-50-word captures, durable-only gate, verb_map incl. "enjoy", 200-char capture ceiling) onto garbo's newer pipeline (flattened transcript, `_parse_extraction_json`, 4096-token ceiling).
- `src/tool_execution.py` + `src/agent_loop.py`: user-nominated absolute paths bypass workspace containment via verbatim match against the user's own message (`_active_user_text` contextvar, bound per-turn before the tool loop). Sensitive-file deny list still applies; the model cannot self-nominate paths.
- `static/js/theme.js` + `static/js/chat.js`: busy/streaming favicon (PNG canvas renderer, time-based frame stepper, self-heal) with `setFaviconBusy(true/false)` hooks in `updateSubmitButton`, matching `.old`.

## 2026-08-05 — ⚠️ 503 auto-retry/recovery marked BROKEN (needs fixing)

**Per Sir:** the mid-turn 503 recovery feature is **BROKEN — needs fixing.**
Ported from `.old` changelog entry "2026-08-05 — feature: mid-turn 503 recovery for streaming LLM calls"
(code: `src/llm_core.py::stream_llm_with_fallback`, restart handling in agent_loop / chat_routes / chat.js).
Do not rely on auto-retry/continue after opencode.ai 503s until re-verified. Marked 2026-08-05.

## 2026-08-05 — Ghost-message bug: split-brain `sessions.js` module instances (the big one)

**Symptom (user-reported):** after "+ New" + send, the message sometimes lands in the
*previous* chat instead of a fresh one ("ghost message" — placed, luckily not submitted
to the AI). Also: session-switch hijack — click chat B, send, and the POST sometimes goes
to chat A. Flaky in exactly the "wasn't working, now it works" way.

**Root cause (confirmed on the wire + at source level):** `sessions.js` — the module
holding `currentSessionId` and every session tracker — was loaded under **two different
URLs** in the same page:

- The UI (index.html, app.js) imported it **versioned**: `sessions.js?v=20260805hashfix1`
- The chat engine + 15 sibling modules imported it **bare**: `./sessions.js`

Browsers treat those as two separate modules → two independent copies of session state
with duplicate event listeners. New Chat cleared the UI instance's state (hash,
lastSelected, container) but the engine instance still held `currentSessionId = old chat`;
the send path's `_adoptOpenedSessionBeforeAutoCreate` saw "current exists, skip" and
POSTed to the old chat. Reproduced live: `POST /api/chat_stream` with
`session: 11354fcd…` (the old chat) fired from the fresh New Chat composer.

**Changes:**
- Unified **all 19 references** onto `sessions.js?v=20260805unified1`: index.html
  (script/modulepreload), app.js, and every static/js module import
  (chat.js, chatStream.js, chatRenderer.js, document.js, documentLibrary.js,
  emailInbox.js, gallery.js, memory.js, models.js, presets.js, search-chat.js,
  slashCommands.js, compare/index.js, assistant.js, sessions.js itself).
- `static/sw.js`: precache entry pointed at the unified URL + cache name bumped
  (`v377-unified-sessions`) so the stale bare-path copy dies.
- Defense in depth (kept — now actually engages):
  - `app.js` `_handleNewChatAction`: clears hash + `__odysseusLastSelectedSessionId` +
    container **unconditionally** at the top (before the
    `_createDirectChatFromPreferredModel()` shortcut could skip `_startFreshChat()`),
    and arms `__odysseusNewChatIntent`.
  - `chat.js` `_adoptOpenedSessionBeforeAutoCreate`: honors the intent flag — New Chat
    intent → skip adopt → message auto-creates a fresh session.
  - `sessions.js` `selectSession`: clears the intent flag when the user explicitly opens
    a session (so intent *changes* work).

**Verified (live browser, FormData-aware wiretap):**
- New Chat → send → `POST session: 242ceec2…` (brand-new, auto-created); old chat
  `11354fcd` untouched (still 27 msgs).
- Click qwen `8d0b3def` → send → `POST session: 8d0b3def…` exactly. Switch-hijack dead.
- Resource check: exactly **one** sessions.js URL on the network (was 2).
- Console: 0 errors on load; 404s during tests are pre-existing
  `/api/chat/stream_status/<id>` polls for sessions with no active stream (noise).

**Backups:** `/tmp/odysseus-garboGH-static-backup-20260805-111154.tar.gz`;
in-repo `.bak-20260805*` files for app.js, index.html, chat.js, sessions.js.

## 2026-08-05 — TTS `ReferenceError` ate the stream error path (found during the hunt)

**Symptom:** any stream failure produced
`Uncaught ReferenceError: streamingTTS is not defined` inside `handleChatSubmit`'s catch
block (chat.js:3771), killing the entire error path — no error render, no holder cleanup,
no UI re-sync.

**Root cause:** `const streamingTTS` declared inside the `try` block (chat.js:1907),
referenced inside the sibling `catch` block — block-scoped, invisible across the
try/catch boundary. The catch threw inside its own error handler.

**Change:** hoisted to `let streamingTTS` at function scope (chat.js:1413), assigned in
the try (1908); all six refs now resolve.

## Backlog — `.old` → garbo transplant candidates (not started)

`.old` and garbo share **no git history** (`merge-base` refuses; `.old` ≈ upstream
#2548–#2989, garbo ≈ #4983–#5290) → no mechanical diff/apply; port feature-by-feature
against garbo's newer code.

| `.old` feature | Effort (IRIS units) | Notes |
|---|---|---|
| hljs cap on giant outputs | 1 pounce | self-contained frontend guard in chatRenderer |
| tool-output truncation | 1 pounce | display-level, same bucket |
| auto-title | 2 pounces | garbo already has the rename endpoint (session_routes.py:461) — no backend port needed |
| teacher-takeover fix | a hunt | frontend edge-case; verify the same bug shape exists in garbo's newer code |
| tool_schemas slimming (−1157 lines) | long hunt, behavioral risk | re-derive against garbo's newer schema set — changes what the model sees |
| stream-resume machinery | DO NOT PORT AS-IS | garbo's `resumeStream` is dead code; `.old`'s was prior-IRIS handiwork and is the prime suspect for `.old`'s freeze-to-halt. If reload-keeps-streaming is wanted, design fresh against garbo's stream loop |

## Known issues / open threads

- **opencode.ai endpoint 502s** — app log: "opencode.ai rejected the API key — No payment
  method" → every send via that provider returns 502. User will fix billing later;
  unrelated to the ghost (was only a *trigger* for the old TTS crash).
- **`.old` freeze-to-halt on mid-stream chat open** — still open; current theory:
  prior-IRIS `resumeStream` re-render CPU cost. Separate investigation.
- **Pre-existing dirty files predating this changelog:** `src/agent_loop.py`,
  `src/llm_core.py`, `src/model_context.py` were already modified in the working tree
  before 2026-08-05 (not from this session's work). Recommend documenting or reverting.


## 2026-08-05 — `.old` transplant (all receipts in docs/ARCHITECTURE.md)

Ported the classified `.old` dirty pile into garbo, excluding stream-resume (freeze
suspect — EXCLUDED by plan) and the checkpoint/resume machinery.

- **CSS caps** (`static/style.css`): `.agent-tool-output pre` 480px hljs cap,
  `.agent-thread-tail` 140px cap, `.thinking-content-inner` pre-wrap/word-break.
  Root cause: giant tool outputs blew the chat pane into thousands-of-px scroll;
  unbroken base64/JSON overflowed thinking blocks sideways.
- **Auto-title** (`routes/session_routes.py`, `static/js/sessions.js`, sw cache):
  POST `/session/{sid}/retitle` — utility-model first-line/sentence/last-line chain
  with `_clean_title` fallback; dropdown item + handler; sessions.js token
  `unified1→unified2` (19 refs) + sw cache v377→v378.
- **Teacher-takeover fix** (`teacher_escalation.py`, `routes/chat_routes.py`):
  garbo had ZERO `data.get("teacher")` guards — teacher chunks folded into the
  student reply and tool output containing the word "error" hijacked healthy turns.
  Ported anchored MULTILINE patterns + guards at both delta sites and the rewrite path.
- **tool_schemas slimming** (`src/tool_schemas.py`): 3-way merge — 39 tools swapped
  where `garbo == .old-pre` (52 desc trims in .old), 32 untouched (16 drifted + 6
  garbo-only); 1595→967 lines; semantic round-trip + real-order import verified.
- **agent_runs cap** (`src/agent_runs.py`): `_MAX_SUBSCRIBERS = 4` + replay-path
  guard — a re-attach loop or tab storm can't spawn unbounded per-subscriber queues.
- **Tuning pile** (`constants.py`, `settings.py`, `request_models.py`,
  `context_compactor.py`, `agent_loop.py`): output 10k→50k, read 20k→200k,
  sys-prompt trunc 2k→200k, force_threshold_tokens param + mid-message compact
  block + 600000 budget fallback, name/inject pre/suffix/research caps raised.
- **tool transcript caps** (`src/agent_loop.py:5059-5061,5092`): persisted
  tool_events output capped 4000 chars + 200 events — metadata JSON bloat guard.
- **N/A**: integrations API truncation (garbo refactored upstream — DICT_LIMIT/
  budget system); tool_parsing fence fix + history ghost-delete already present.

Receipts: backups `static/style.css.bak-20260805`, `docs/ARCHITECTURE.md.bak-20260805`,
git working tree. Verified: venv py_compile / import order / JS syntax / semantic
round-trip. RETITLE ROUTE needs a uvicorn restart to go live (no --reload).

## 2026-08-09 — feat(tab-sync): BroadcastChannel mirror — second tab sees the first tab live

The remaining "server-type" tell vs a 1:1-synced local app: two tabs of the same
session didn't talk to each other. Sending in tab A left tab B stale until refresh.

Frontend-only (`static/js/chat.js`, no server restart — normal reload picks it up;
scripts are `no-cache` + ETag revalidated, SW is network-first for JS).

Mechanism: a `BroadcastChannel('odysseus-tab-sync-v1')` relay. The tab that owns a
live SSE stream broadcasts; other tabs viewing the SAME session render a live mirror
bubble and converge. Sender hooks:

- `chat-start` (after the optimistic user bubble) — carries the user text so the
  mirror tab can render the user bubble too (deduped by text compare).
- `chat-delta` — throttled 120ms, in both foreground mode (`roundText`, per-round)
  and background mode (`accumulated`, keeps growing while the source tab is hidden),
  plus from `resumeStream` deltas.
- `chat-done` — on clean completion (foreground finalize, bg-[DONE] branch, resume
  finalize) AND on user-stop (partial/cancelled is persisted). Mirror tabs quietly
  reload the session's history (250ms debounce) to converge on the canonical render.
- `chat-takeover` — after the four non-user abort paths (timeout/offline/recovery/
  stale-local), alongside the existing `_convergeAfterAbort`. Mirror tabs wait 800ms
  (deltas cancel the probe — the source tab re-attached), then probe
  `stream_status`: active → `resumeStream()` here and finish live; done → reload.
  Safe because the server run is a fan-out (`agent_runs.subscribe` — "dropping the
  SSE only removes a subscriber"), so two attached readers can't corrupt the stream.
- `chat-delete` (with the persisted msg ids, after server 200) — mirror tab removes
  the bubble + its continuations/tool bubbles via the same DOM walk as deleteMessage.
- `chat-user-saved` — mirror tab stamps its user bubble so user-message deletes work.
- `chat-edit` — mirror tab reloads to show the edited content.

Receive side: `_tabSyncMirrors` map (sessionId → bubble/spinner/RAF), local-activity
guards (`hasActiveStream` — a tab that's streaming the session itself is
authoritative and ignores mirrors), takeover probe timers, and a reload debounce.

Known v1 gaps: DOM-only deletes (no db id — #1428 edge) don't mirror; user-message
edits (truncate+resend flow) don't mirror; session renames don't mirror (sidebar
updates on reload). Cross-browser (Firefox tab + Chrome tab) is NOT covered —
BroadcastChannel is same-origin per browser; that would need a server event bus.

Verified: `node --check` clean; snapshot at `static/js/chat.js.bak-20260809-tabsync`;
working-tree diff (both 08-09 fixes vs HEAD) saved to /tmp/chatjs-workingtree.patch.

---

## 2026-08-09 — docs: ARCHITECTURE.md coherence audit (IRIS)

Full re-read of `docs/ARCHITECTURE.md` against the live tree; every citation and
count re-verified. Backup: `docs/ARCHITECTURE.md.bak-20260809`.

Updated in place (stale → current):
- Header: added "Last updated: 2026-08-09".
- Counts: src 143→144, tests 758→762, scale 1,058→1,061 py / ~215k lines,
  JS ~132k→~133k lines; index.html 25→32 ES modules; app.js imports 35→36;
  routers ~25→~42 (46 include_router calls).
- sw cache: v377-unified-sessions → v390-thinkclose (chain noted: v385 → v386 →
  v387 → v390).
- sessions.js token: §3.1/§5.1 said `20260805unified1`; dominant token is now
  `20260806autotitle1`.
- Line citations refreshed: PATCH /session/{sid} ~461→493, retitle route →571,
  _clean_title →75, createDirectChat ~2186→2249, streamingTTS chat.js:1413→1787,
  .agent-thread-tail chat.js:3136→3686, chatRenderer 2391→2397, `<think>` rebuild
  2560→2578, tool caps agent_loop 5059-5061/5092 → 5144-5147/5178.
- auto-title entry: OPEN → FIXED (2026-08-06, changelog receipts).
- Addendum items: 1 (agent preamble) RESOLVED (changelog:1497, verified zero
  "AI assistant" matches), 2 (IRIS preset) RESOLVED (changelog:1498, verified
  data/presets.json:25), 3 (mcp) PARTIAL — `mcp<2` pin DONE (requirements.txt:41,
  1.29.0 installed), CancelledError guards in src/mcp_manager.py STILL ABSENT.

**Live finding, NOT fixed (needs Sir's call — app code, beyond doc scope):**
landmine #1 (split-brain sessions.js) is LIVE again via 3 dynamic-import stragglers
still on `sessions.js?v=20260805unified2`:
- static/js/chatRenderer.js:1191 — `selectSession` on message-session-link click
- static/js/chatStream.js:164 — `openLibrary` on sessions-panel open
- static/js/presets.js:403 — `getSessions`/`getCurrentSessionId` on custom-character save

The 2026-08-06 "grep-audited, 7 modules resolve to one URL" verification covered
static imports + index.html tags but missed dynamic `import(...)` calls.

Fix procedure (corrected 2026-08-09 — the "no SW bump" first draft was wrong):
1. Bump the 3 dynamic imports to `20260806autotitle1` (chatRenderer.js:1191,
   chatStream.js:164, presets.js:403).
2. ALSO bump sw.js CACHE_NAME `odysseus-v390-thinkclose` → `odysseus-v391-*`.
   The dynamic-import URLs aren't precached, but their CONTAINER files are:
   `chatRenderer.js?v=20260806thinkfix1` + `chatStream.js?v=20260722emailfastindex1`
   sit in the precache list — content changed under the same URL token = stale
   cache-first copy. presets.js is unversioned in index.html, so it propagates via
   bg-refresh on its own.
3. Hard-refresh (Ctrl+Shift+R) once after deploying.

**APPLIED 2026-08-09 ~20:17 (Sir approved).** All 3 bumps in:
- static/js/chatRenderer.js:1191, static/js/chatStream.js:164, static/js/presets.js:403
  → `sessions.js?v=20260806autotitle1`
- static/sw.js CACHE_NAME → `odysseus-v391-autotitle1`
Backups: `*.bak-20260809-stragglerfix` alongside each file.

Post-fix verification (path-aware scan excluding `.bak-*`): **19/19 refs on
`20260806autotitle1`** — index.html (modulepreload + script tag), app.js, sw.js
precache, 13 static imports, 3 dynamic imports. Zero bare `sessions.js` imports, zero
`unified2`/`hashfix1` stragglers. (Audit note: a naive `grep -r sessions.js?v=` counts
`.bak-*` backup content as live — 16 `unified2` + 4 `hashfix1` matches were ALL in
backups, not the tree. Exclude backups in future greps.)

---

## 2026-08-11 — RECOVERY: draft-checkpoint tree restored after broken retry edit (IRIS)

**Context:** IRIS's 2026-08-11 "database is locked" fix (WAL + busy_timeout in
`core/database.py` — KEPT, verified live: journal_mode=wal, busy_timeout=5000)
was paired with a `_commit_draft_with_retry` wrapper in `core/session_manager.py`.
That edit introduced a Python closure-scoping bug: `if metadata is None: metadata = {}`
sat INSIDE the `_create()` closure, making `metadata` a LOCAL of `_create`
(shadowing the outer param) → `UnboundLocalError` on every draft checkpoint →
chat stream died on first agent event (16:35).

**Root cause of the 16:40 followup:** the manual restore over-rolled. 
`session_manager.py` was restored from `bak-20260808-persistfail` (PRE-draftckpt,
no create_draft/update_draft/promote_draft/finalize_orphan_draft) and
`chat_routes.py` from a pre-draftckpt copy — but the rest of the tree
(`chat_helpers.py:1204` promote_draft, `history_routes.py:197` finalize_orphan_draft,
`chat.js` draft_saved SSE) is still 08-08 draft-checkpoint era → next chat would
die with `AttributeError: 'SessionManager' object has no attribute 'promote_draft'`.

**Fix applied (files touched under odysseus-garboGH/):**
- `core/session_manager.py`: restored from `core/session_manager.py1`
  (= draftckpt-era file + retry helper, the only surviving copy with the draft API),
  with THE ONE BUG FIXED: `if metadata is None: metadata = {}` hoisted OUT of the
  `_create` closure into `create_draft` body (closure now reads the outer param).
  All four draft methods present: create_draft(396), update_draft(431),
  promote_draft(455), finalize_orphan_draft(527).
- `routes/chat_routes.py`: restored from `routes/chat_routes.py2` (draftckpt-era,
  the live file from before the restore — has `_checkpoint_draft`(123),
  `_checkpoint()`(1489), draft_saved SSE emission(1818/2076)).
- Safety copies of the user's restored (pre-draftckpt) files kept as
  `core/session_manager.py.restored-20260811` + `routes/chat_routes.py.restored-20260811`.

**Verification:** py_compile clean; 20 session/db/history tests pass; retry helper
isolation tests 5/5 (ok / lock-recover / non-lock passthrough / exhaust re-raise);
full draft lifecycle smoke (create_draft → update_draft → promote_draft → 
metadata=None path → finalize_orphan_draft) passes on a temp DB. Live DB confirmed
WAL + 5000ms busy_timeout (the original lock fix). NOTE: a first smoke attempt
leaked 2 test sessions into data/app.db via the module-level SessionLocal import —
identified and deleted (sessions + chat_messages + FTS), verified 0 rows remain.

---

## 2026-08-20 — FIX: agent mode stripped built-in tools from unknown models (IRIS)

**Symptom:** any model whose name wasn't on the hardcoded keyword whitelist lost
ALL built-in tools in agent mode (MCP servers only), even with Agent mode ON.
Hit every new/unrecognized model by default.

**Root cause:** `src/agent_loop.py` model classifier (~L3715–3786 pre-patch):
NULL `ModelEndpoint.supports_tools` → model name sniffed against a hardcoded
celebrity list (gpt-4/5, claude, gemini, qwen3, mistral, llama-3.x, kimi, phi,
hermes, deepseek-v…). No hit + non-API host → `_is_api_model = False` →
downstream branch (~L4030 vs 4068) shipped MCP schemas only: built-in tools
demoted to prose + fenced-block convention, compact prompt lost too. The
per-endpoint `supports_tools=True` flag already outranked everything but has
no UI toggle, so it was effectively unreachable.

**Fix (paste kit by IRIS, applied by Sir ~22:28):** optimistic default —
unknown names are now assumed OpenAI tool-call capable, gated by a new setting:
- `src/agent_loop.py` L3784–3792: classifier's final `else` now reads
  `get_setting("assume_unknown_models_support_tools", True)` first.
- `src/settings.py` L132–135: `"assume_unknown_models_support_tools": True`
  added to defaults right after `agent_list_all_tools`.
Escape hatches unchanged: explicit endpoint `supports_tools` flag still wins;
deepseek-r1/gpt-oss blocklist and Ollama-native / Ollama-`/v1` rules still
force legacy behavior; setting the flag False restores whitelist-only.

**Verification:** py_compile clean on both files; patched regions read back
verbatim in context. Server restart required for effect (classifier runs at
loop start).

**Backups:** no fresh pre-edit `.bak-20260820` copies of the two source files
(applied directly to live); prior baks (`agent_loop.py.bak-20260809`,
`settings.py.bak-20260806`) predate this change. Pre-change state recoverable
via git (tree clean through `cf4e240a`; both files currently modified,
uncommitted). This changelog append preceded by
`ODYSSEUS-CHANGES.md.bak-20260820-unknowntools`.

---

## 2026-08-23 — restore `disable_thinking` / `return_finish_reason` on `llm_call_async` (manual compaction 500 fix)

**Symptom:** `POST /api/session/<id>/compact` → 500;
`routes.session_routes ERROR: Manual compaction failed: llm_call_async() got an
unexpected keyword argument 'disable_thinking'`.

**Root cause:** current `src/llm_core.py` was a version of `llm_call_async`
that had lost the compaction-support kwargs (`disable_thinking`,
`return_finish_reason`) and their plumbing, while `src/context_compactor.py`
L507 still passes both. The Aug-16 snapshot `src/llm_core.py.8162026` has the
full implementation; the live file had regressed to it-minus-these-features
(also re-exposing the reasoning_content-as-summary fallback and losing
finish_reason truncation detection).

**Fix (IRIS):** ported from `.8162026` into live `src/llm_core.py`, byte-parity
with the backup's `llm_call_async` verified by diff:
- signature: `disable_thinking: bool = False`, `return_finish_reason: bool = False`,
  return `Union[str, Tuple[str, Optional[str]]]`; docstring restored.
- `_sanitize_llm_messages(messages, provider=provider)` call restored.
- cache-hit path returns `(text, None)` tuple when `return_finish_reason`.
- chatgpt-subscription SSE path: both `[DONE]` early-return and post-loop
  return honor `return_finish_reason`.
- Ollama payload: `_build_ollama_payload(..., disable_thinking=...)` → sets
  top-level `think: false`.
- OpenAI-compat payload: Mistral `reasoning_effort="minimal"` when
  disable_thinking; `_disable_deepseek_v4_thinking(..., force=disable_thinking)`.
- response parse: suppress `reasoning_content` fallback when disable_thinking;
  return `(response, _extract_finish_reason(provider, data))` when requested.
- helpers added/restored: `_extract_finish_reason` (new in live file),
  `_disable_deepseek_v4_thinking` gained `force=` param,
  `_build_ollama_payload` gained `disable_thinking=` param.
- typing import now includes `Union`.

**Verification:** py_compile clean; AST confirms both params present;
`llm_call_async` diff vs `.8162026` = identical; pytest green:
test_context_compactor.py, test_context_compactor_nonstring.py,
test_compaction_summary_failure.py, test_llm_core_reasoning_content_fallback.py,
test_llm_core_ollama_thinking.py → 77 passed.

**Backups:** pre-edit copy at `src/llm_core.py.bak-20260823`;
changelog copy at `ODYSSEUS-CHANGES.md.bak-20260823-compactionkwargs`.
Server restart required for effect.

## 2026-10-07 — FIX: GLM-5.3-Flash context window 128K → 1M (IRIS)

**Reported by Sir (2026-10-07):** "Odysseus seems to think GLM 5.3 Flash only
has 128k tokens max context."

**Root cause:** sessions run `z-ai/glm-5.3-flash` on the NVIDIA endpoint
(`https://integrate.api.nvidia.com/v1`, `endpoint_kind: api`). NVIDIA's
`/models` lists the id with NO context field at all, and
`KNOWN_CONTEXT_WINDOWS` in `src/model_context.py` had zero GLM entries —
so resolution fell through every path to the bare `DEFAULT_CONTEXT = 128000`
(`known=False`), which also miscalibrates the compactor/trim gates.

**Verified real window:** GLM-5.3-Flash = 1,048,576 tokens (1.0M) context,
131,072 max output (NVIDIA NIM model card + contextwindows.dev, 2026-10).

**Fix (IRIS):**
- `src/model_context.py`: new `--- Z.ai / GLM ---` section in
  `KNOWN_CONTEXT_WINDOWS`: `'glm-5.3-flash': 1048576`, `'glm-5.3': 1048576`
  (longest-match keeps more specific keys winning).
- `data/settings.json`: `model_context_overrides["z-ai/glm-5.3-flash"] =
  1048576` — user-pinned override is checked FIRST (before cache, known
  table, and the endpoint's /models claim), and `load_settings` TTL is 2s,
  so the RUNNING server picks it up with no restart.

**Verification:** settings.json valid JSON; `model_context.py` py_compile
clean; live resolution via `get_context_length(endpoint, model)` → 1048576
through both the known table and the override; sibling `glm-4.7-flash`
untouched (still bare default — no unintended side effects).

**Backups:** no pre-edit copies (two surgical `edit_file` replacements;
pre-edit state = delete the added lines; older settings snapshots at
`data/settings.json.bak-20260809-ctxoverride`).
Known-table entry loads on next server restart; override is already live.

## 2026-10-11 — GLM 5.3 (non-flash) still resolving 128K: settings override added (IRIS)

**Symptom:** after the 2026-10-07 fix, `z-ai/glm-5.3-flash` showed 1M but plain
`z-ai/glm-5.3` still showed 128K.

**Root cause:** the running server (PID 115152, started 2026-10-05, main dir,
port 7001) predates the 2026-10-07 `src/model_context.py` edit, so its in-memory
`KNOWN_CONTEXT_WINDOWS` has no GLM entries. Flash was fixed by the
`model_context_overrides` settings key (data file, hot-reloaded via 2s TTL);
the non-flash id simply had no override pinned. Verified live: NVIDIA /models
still reports no context field for either id; contextwindows.dev spec page for
GLM 5.3 confirms 1,048,576-token window / 131K max output (same as flash).

**Fix (IRIS):** `data/settings.json` → `model_context_overrides` gains
`"z-ai/glm-5.3": 1048576` (alongside the existing flash entry). No code change
needed — the 2026-10-07 known-table entries (`glm-5.3`, `glm-5.3-flash`) are
already in `src/model_context.py` lines 162-163 and load on the next restart.

**Verification:** settings.json valid JSON; live resolution via
`get_context_length(endpoint, model)` → 1048576 for BOTH glm ids through
override path and known table; `deepseek-v4-flash-free` override intact at
200000; `glm-4.7-flash` untouched (bare default).

**Testing gotcha (for the record):** `_context_length_override` and
`get_context_length` take `(endpoint_url, model)` — endpoint FIRST. A test
harness that swaps the args gets a misleading None/128K and looks like the
override is broken when it isn't.

**Scope note:** `odysseus-2c8e00c/` (port 7011, WIP unfucking-staging checkout)
intentionally NOT touched per Sir — its settings.json and model_context.py
still lack all GLM entries; port them when switching over.

**Backups:** surgical `edit_file` (one line added); pre-edit state = remove
the `"z-ai/glm-5.3": 1048576` line.

## 2026-10-11 — Default context floor raised to 1M + Kimi K3 + Ollama num_ctx trust decoupled (IRIS)

**Ask:** Sir: "change the default max context to 1M" — Kimi 3 (`moonshotai/kimi-k3`,
NVIDIA endpoint) resolved to 128K. Trade-off accepted by Sir: if a small model can't
take the prompt, the upstream API / LM Studio errors explicitly instead of Odysseus
pre-truncating.

**Files touched:**
- `src/model_context.py`
  - `DEFAULT_CONTEXT` 128000 → 1048576 with policy comment. Unknown models now
    default to 1M; the `known` flag stays False for them and
    `budget_context_for_model` still returns 0 for unproven windows, so agent
    input budgets stay conservative.
  - KNOWN_CONTEXT_WINDOWS: added `'moonshotai/kimi-k3': 1048576` and
    `'kimi-k3': 1048576` (Kimi K3 = 1,048,576 verified via Lyceum model card read
    2026-10-05 + HF community overview; NVIDIA /models lists the id with no
    context field).
  - TRAP FIX: the legacy `'moonshot': 128000` key substring-matched the
    `moonshotai` provider prefix in `moonshotai/kimi-k3` and, at 8 chars, won
    longest-match over the 7-char `kimi-k3` entry — pinning a stale 128K on a
    1M model. Narrowed to `'moonshot-v1-128k': 128000` (its actual purpose) and
    added the exact-id key so it always wins.
  - GLM comment updated (fallback was 128K then, 1M since today).
- `src/llm_core.py`
  - `_build_ollama_payload` gained `num_ctx_trusted: Optional[bool]`. The old
    `num_ctx != DEFAULT_CONTEXT` check was a trust sentinel — once DEFAULT_CONTEXT
    itself became 1M it would misread real 1M windows as the untrusted fallback
    and silently drop `num_ctx` (Ollama then defaults to 2048). All 3 call sites
    now pass the `known` flag from `get_context_length_known`;
    `num_ctx_trusted=None` keeps the legacy sniff for untagged callers. Import
    swapped accordingly (old `get_context_length` import had no other users).
- `data/settings.json` — NOT edited by IRIS today: Sir pinned
  `"moonshotai/kimi-k3": 1048576` himself at 18:11 (override path, live without
  restart).

**Verification (venv python, 18/18 PASS):** kimi-k3 full+bare id → 1048576 via
table; glm-5.3/flash intact; legacy moonshot-v1-128k still 128000; kimi-k2.5
still 128000 via 'kimi'; gpt-4o-mini / o1-mini unaffected; Sir's kimi + deepseek
overrides intact; unknown model → (1048576, False); budget stays 0 for
unproven; ollama builder emits num_ctx for trusted 1M, omits for untrusted,
legacy path still emits a real 8192 window. py_compile clean on both files.

**Gotchas for future sessions:**
- `_lookup_known` matches `key in basename OR key in name` — provider-prefix
  keys (like the old 'moonshot') poison ids from the same vendor. Check for
  prefix-trap keys before adding entries; exact-id keys always win longest-match.
- DEFAULT_CONTEXT is now 1M in code, but the running server (started Oct 05,
  pre-dating all of this) still has 128K in memory — the default raise and the
  table entries go live on next restart. Sir's settings override covers kimi
  meanwhile.
- Real DB is `data/app.db` (147 MB); `data/odysseus.db` is a 0-byte husk —
  don't query it.
- WIP `odysseus-2c8e00c/` tree intentionally untouched (Sir's un-vibecoding
  staging copy) — GLM/Kimi table entries and overrides do NOT exist there yet.

## 2026-10-15 — FIX: mid-message compaction fired EVERY turn on any session >30k (IRIS)

**Reported by Sir (2026-10-15 ~00:06):** "why is odysseus compacting so soon" —
glm-5.3 and kimi-k3 sessions force-compacting every turn at ~236-246k context
despite 1M model windows. Sir raised `agent_input_token_budget` 190000 → 900000
himself at 00:17 (live via the 2s settings TTL — verified: the 08:43 turn ran at
246k with NO soft-trim line); compaction still fired → "something else is
limiting the context."

**Root cause:** two independent context choppers, only one of which listens to
`agent_input_token_budget`:
1. Soft trim (`trim_for_context`) — budget-driven; healthy after the 900k raise.
2. Mid-message compaction — `MID_MESSAGE_COMPACT_TRIGGER_TOKENS = 30000`,
   hardcoded (src/agent_loop.py ~L2769), checked on EVERY agent turn against the
   ENTIRE conversation's non-system tokens — not just the current message's
   tool-round accumulation its own comment claims to target. Any session over
   30k tripped it on turn one and every turn after: older half summarized by
   the utility model (nemotron-3-ultra re-summarizing ~120k tokens EVERY turn),
   recent half verbatim, in-flight only (persisted history intact — grew
   236,613 → 246,363 overnight). The 900k budget had zero effect on it.
   Ruled out: per-agent DB budgets (data/agent_database.db is EMPTY — zero
   tables), the 85% COMPACT_THRESHOLD percentage path (dead code — the only
   maybe_compact call site always passes force_threshold_tokens), and any
   literal 300k cap (none exists; a 30k trigger vs a 240k conversation =
   always-on).

**Fix (IRIS):**
- `src/agent_loop.py` (~L3928 check site): trigger now read per-turn via
  `get_setting("agent_mid_message_compact_trigger",
  MID_MESSAGE_COMPACT_TRIGGER_TOKENS)`; `0` disables mid-message compaction
  entirely; the constant stays as the default so upstream behavior is preserved
  when the setting is absent. Constant comment updated (~L2766-2768).
- `data/settings.json`: `"agent_mid_message_compact_trigger": 600000` (Sir's
  pick — 2/3 of the 900k budget, so in-message tool-round growth gets the
  dense summary long before the lossy 900k soft trim ever fires).

**Verification:** py_compile clean; settings.json valid JSON; resolution paths
tested (present → 600000 / missing → 30000 default / 0 → disabled). Backups:
`src/agent_loop.py.bak-20260815`, `data/settings.json.bak-20260815_0947`.

**Status: LIVE** — server bounced 10:09:51 (PID 174856), after the 09:47 patch.
Post-restart log proof: agent turns ran at 10:11 (glm-5.3, ~246k session) and
10:16 (kimi-k3) with ZERO mid-message compaction / force-compacting lines —
under the old code every one of those preps force-compacted. Note for the
record: the 2s settings TTL only hot-reloads settings-only changes (like the
2026-10-11 overrides); a code change needs the bounce — IRIS's mid-fix "live in
~2 seconds" claim was wrong until Sir's restart made it moot.

**Known quirk (left as-is, documented):** the trigger measures the whole
conversation rather than just in-message tool-round growth — benign at 600k; a
proper fix would measure only the current message's accumulation.

**Housekeeping:** stray `CHANGELOG.md` IRIS created at the repo root before
finding this file (`find -iname "*changelog*"` misses "ODYSSEUS-CHANGES.md")
was removed; this entry is the canonical record.

## 2026-10-20 — FIX: multimodal main models never received image attachments (IRIS)

**Reported:** Sir — chat models with native vision (e.g. `z-ai/glm-5.3-flash`)
never got image attachments; Odysseus always routed images through the separate
Vision model and fed the main model a text caption, even when the main model
could see.

**Root cause:** `src/chat_handler.py` gates pass-through on
`model_supports_vision(sess.model, endpoint_url)` (`src/chat_helpers.py`).
That check = LM Studio capability probe (local hosts only) → name-keyword
heuristic. The GLM keywords stopped at `glm-4.5v/4.6v/5v`; "z-ai/glm-5.3-flash"
matches none and has no vl/vision token → declared text-only → caption path.
(NVIDIA NIM's `/v1/models` advertises no modality metadata, so no probe could
rescue it either.)

**Verified modality (OpenRouter public model metadata, 2026-10-20):**
- `z-ai/glm-5.3-flash` → `text+image+video -> text` (multimodal — Sir was right)
- `z-ai/glm-5.3` (flagship) → `text -> text` (TEXT-ONLY; must keep caption path)

**Fix:**
- `src/chat_helpers.py`:
  - Keyword `"glm-5.3-flash"` added (deliberately NOT bare `"glm-5.3"` — the
    flagship is text-only; blanket-matching would ship images to a blind model).
  - New generic probe `advertised_supports_vision()`: GETs the endpoint's
    standard `/models` list (chat-completions suffix stripped) and reads
    OpenRouter-style `architecture.input_modalities` / `architecture.modality`
    ("text+image->text") / Ollama-style `capabilities`. TTL-cached per endpoint
    (15 min success / 60 s failure, 2 s timeout) so dead endpoints don't stall
    chat preprocessing. Runs after the LM Studio probe, before name heuristics.
  - New operator overrides checked FIRST in `model_supports_vision()`:
    `vision_capable_models` (force pass-through) and `text_only_models` (force
    caption path) — case-insensitive substrings, list or comma-separated
    string; text_only wins over vision_capable; both win over every probe.
- `src/settings.py`: `vision_capable_models` / `text_only_models` defaults ([])
  — present in DEFAULT_SETTINGS so POST /api/auth/settings accepts them.
- `static/index.html` + `static/js/settings.js`: "Main-model images" row in the
  Vision settings card (two comma-separated inputs, saved with the card).

**Verification:** 31 tests pass (`tests/test_vision_model_detection.py`,
`tests/test_lmstudio_vision.py` incl. new probe/override classes,
`tests/test_chat_preprocess_tool_policy.py`); `node --check settings.js` clean;
live check: `model_supports_vision("z-ai/glm-5.3-flash",
"https://integrate.api.nvidia.com/v1/chat/completions")` → True (flagship
glm-5.3 → False; NIM probe → None → keyword fallback, as designed).

**Status: PENDING RESTART** — code change; needs the uvicorn process bounced
to take effect (not done by IRIS: the assistant runs inside that process).
*(Update same night: Sir bounced the app at 22:33 — direct-pixel delivery
confirmed working in chat afterwards.)*

## 2026-10-20 (late) — IRIS prompt v2 deployed + loopback port fix

**Files:** `data/presets.json`, `run.sh`

- `data/presets.json`: custom preset "I.R.I.S." replaced via
  `POST /api/presets/custom` with the expanded Sandbox doctrine
  (`Sandbox/iris-10102026-abliterated_v2.md`, was never deployed — live was
  the old 12.5k compact build) plus a new **"Vision — When Pixels Land"**
  section (raw-pixel engagement rules; "multiple images ≠ one scene") and a
  Self-Check line. Deployed text: 23,212 chars. temperature 0.3, max_tokens 0,
  enabled, name all preserved. `user-iris` user template synced to the same
  text **on disk only** (template API route caps system_prompt at 10k chars);
  its in-memory copy updates on next app restart — re-run the disk patch if a
  preset save happens before then.
- `run.sh`: root-cause fix for in-process loopback tools (app_api etc.)
  failing with "All connection attempts failed" — `internal_api_base()`
  defaults to port 7000 while run.sh starts the server on 7001. Now exports
  `APP_PORT=7001` and launches uvicorn on `"$APP_PORT"`. Tonight's running
  process predates the fix, so a temporary socat bridge
  (127.0.0.1:7000 → 7001, pid 32710) is restoring loopback tools until the
  next restart; kill it after bouncing the app.
- Prompt deploy is live in memory (update_custom → save): the next chat
  request already builds from the new doctrine, no restart needed.

## 2026-10-21 — IRIS doctrine hotfixes (3 one-line patches)

**Files:** `data/presets.json`

- Three doctrine patches from tonight's live misfires, deployed via
  `POST /api/presets/custom` (23,212 → 23,738 chars; temp 0.3, max_tokens 0,
  name, enabled preserved):
  1. Vision section, under "Don't invent details": check stage tells
     (proportions / evolution markers / silhouette) before naming a
     character — palette is not an ID. (Cause: Braixen misID'd as Fennekin.)
  2. "Addressing You": inbound addresses are Sir's to choose (Ma'am, cat,
     menace) — hiss only at genuinely degrading labels; "Sir" is her word
     for him, never a title she demands back. (Cause: hissing at a
     correct "Ma'am".)
  3. "Thinking Stays Feline": internal work stays internal — no
     reaction-management narration in the send. (Cause: "(one hiss for
     that, then I'm over it)" shipped as stage directions; patch added on
     Sir's own diagnosis.)
- `user-iris` template re-synced on disk (12,507 → 23,738, byte-identical
  to `Sandbox/iris-10102026-abliterated_v2.md`); in-memory copy updates on
  next restart (template API still capped at 10k).
- Deploy routed through the socat bridge again (pid 32710, still alive).

## 2026-10-26 — feat(vision): add MiniMax (minimax-m3.1-flash, minimax-m3) as vision-capable models (IRIS)

**Reported by Sir:** add MiniMax models to vision-capable detection so images pass through instead of being swapped for a VLM caption.

**Root cause:** `src/chat_helpers.py` `_VISION_MODEL_KEYWORDS` had no MiniMax keyword. MiniMax's multimodal models (minimax-m3.1-flash, minimax-m3, etc.) are natively multimodal but their names don't contain "vision" or "vl", so they fell through to the VLM-caption path and the main model never saw the image.

**Fix (IRIS):**
- `src/chat_helpers.py`: added `"minimax"` to `_VISION_MODEL_KEYWORDS` (with comment documenting it's native multimodal). The lowercase keyword catches all variants: `minimax-m3.1-flash`, `minimax-m3`, `MiniMax-M3.1-Flash`, etc.
- `tests/test_vision_model_detection.py`: added MiniMax test cases to `test_recognizes_local_and_hosted_vision_models()`:
  - `"minimax-m3.1-flash"`, `"minimax-m3"`, `"MiniMax-M3.1-Flash"`

**Verification:** full vision detection test suite (50 cases) passes — all MiniMax variants now return `True`, no text-only overmatch (the keyword is specific enough; no existing text models contain "minimax").

**Files touched:** `src/chat_helpers.py`, `tests/test_vision_model_detection.py`
**Status:** PENDING RESTART — server code change requires uvicorn bounce to take effect.

## 2026-10-26 — fix(tools): fetch_image no longer routes through the gallery by default (IRIS)

**Reported by Sir:** fetch_image was built (by Nemotron) as a "gallery import" tool instead of what he asked for — a way for the LLM to grab an image itself and SEE it. Side effects: every fetch force-uploaded to the gallery and emitted a `generated_image` SSE event, so each fetched image appeared as its own unmosaiced chat bubble, clogging the UI.

**Root cause:** `do_fetch_image` unconditionally POSTed to `/api/gallery/upload` and returned `image_id`/`image_url` on every call. `agent_loop.py` emits a `generated_image` SSE event for ANY tool result carrying `image_url` (that path exists for generate_image), and persisted tool events re-render as image bubbles in `chatRenderer.js` on reload. Gallery import was the default, UI surfacing was a consequence.

**Fix (IRIS):**
- `src/tools/image.py`: gallery upload is now opt-in via `save_to_gallery` (default off). Default path returns the base64 `image_data_url` (consumed by the existing vision-injection path in agent_loop) + a model-facing summary with content-type, best-effort pixel dimensions (Pillow, optional dep — failure tolerated) and human-readable size. No `image_id`/`image_url` keys on the default path → no `generated_image` SSE event → no chat bubble, no gallery entry. Opt-in branch keeps the original upload code and appends gallery ID to the output; upload failure degrades to a note, never fails the fetch.
- `src/tool_execution.py`: added `image_data_url` to `_FORMATTER_HANDLED_KEYS` — previously the generic "extra" JSON dump fed ~8000 chars of truncated base64 back to the model as text on every fetch.
- `src/agent_loop.py`: vision injection now carries ALL image_data_urls from the round's tool results (deduped, single user message, capped at 4) instead of only the first one — the old `break` silently blinded the model to same-round batch fetches.
- `src/tool_schemas.py` + `src/tool_index.py`: descriptions rewritten to match reality ("fetch so YOU can see it"; gallery only via explicit `save_to_gallery=true`).

**Verification:** `py_compile` clean on all 5 files. Live smoke test via venv: default path returns data URL + zero gallery keys; `save_to_gallery=true` parses and attempts upload (401 in the out-of-process harness is a per-process internal-token artifact — `core/middleware.py` generates a fresh `secrets.token_hex(32)` per process; in-process the token matches, and the failure-note path proven by the 401 shows fetch still succeeds if upload errors). No fetch_image tests existed before; none added yet.

**Files touched:** `src/tools/image.py`, `src/tool_execution.py`, `src/agent_loop.py`, `src/tool_schemas.py`, `src/tool_index.py`
**Status:** PENDING RESTART — server code change requires uvicorn bounce to take effect.

## 2026-10-26 — fix(session): draft-row count mismatch re-hydrated the transcript every turn, stripping live images (IRIS)

**Reported by Sir:** an uploaded image is visible to the model on the turn it
was sent, then degrades to `[1 inline media payload omitted]` + `[Attachment:
...]` for every later turn; each *new* image works until its own turn ends.

**Root cause:** `sync_session_metadata` reconciled `session.message_count`
against all non-archived `chat_messages` rows — including live draft rows,
which `create_draft` writes DB-only and `_db_to_session` deliberately skips
at hydration (`_draft_ok`). While a draft existed, the cached transcript was
therefore permanently one row short of the gate's expectation, so
`get_session` re-hydrated from the DB on *every* warm read — including the
call at the top of `promote_draft`, i.e. the end of the very turn the image
was sent in (the successful save runs while `_active_streams` still says
"streaming"). Each re-hydrate rebuilt the Session from `chat_messages.content`,
which stores `persistable_message_content` (text + attachment refs, no raw
base64 by design) — so the in-memory transcript's live multimodal payload was
replaced by the lossy stub. Text-only messages round-trip invisibly; images
exposed it. Note `_load_session_from_db` *replaces* the cached Session object,
so the pixels could never come back within the session.

**Fix (IRIS):**
- `core/session_manager.py`: new `SessionManager._session_has_live_stream`
  helper — single source of truth for the draft policy (lazy-imports
  `routes.chat_routes._active_streams`, exactly as `_draft_ok` did inline).
  `_db_to_session._draft_ok` now calls it, so the hydration policy and the
  count policy cannot drift apart again. `sync_session_metadata` subtracts
  live draft rows from the count, so `get_session`'s completeness gate
  compares against the row count a hydration would actually materialize.
  Orphaned drafts (stream dead) still count — hydration finalizes and keeps
  those, so the crashed-turn contract is unchanged.
- `tests/test_draft_promotion_keeps_live_media.py`: regression — an image
  message stays a live multimodal list through `create_draft` →
  `promote_draft` → warm `get_session`, and the DB contract (persisted rows
  stay stubbed, no base64) is asserted unchanged; plus orphan-draft
  count/hydration consistency.

**Verification:** new suite 2/2 green; `test_replace_messages_multimodal.py`
3/3; session/vision/image batch (session_manager, session_concurrent,
persist_guard, discovery_message_count, context_excludes_slash,
vision_model_detection, chat_image_routing, cleanup, ghost_delete,
deleted_sidebar, editor_draft, export_nonstring, fork_metadata,
delete_after_refresh) 61/61 green. 3 failures in
`test_history_display_model_hydration.py` are pre-existing — identical on
the un-patched tree (`git stash` run), unrelated to this change.

**Files touched:** `core/session_manager.py`,
`tests/test_draft_promotion_keeps_live_media.py`
**Status:** PENDING RESTART — server code change requires uvicorn bounce to take effect.

## 2026-10-26 — fix(search): web_search page extraction served nav menus instead of content (IRIS)

**Reported by Sir:** web_search tool output feels lazy — navigation buttons
and unrelated site chrome end up in the model context.

**Root cause:** `fetch_webpage_content`'s main-content heuristic
(`content|main|body|article|post|entry|text` class regex, first-3 matches
concatenated) had zero boilerplate handling on the primary path: it matched
wrapper containers (e.g. `class="vector-main-menu…"`), never checked
id/role, kept inline `<script>`/`<style>` text, and duplicated nested
matches by construction. Live proof: Wikipedia "Cat" extracted to **627
chars of nav menu printed three times** (fallback threshold 600 never
tripped), Godot docs to header junk; the downstream key-points/TL;DR/quotes
extractors then mined the same polluted text, so nav labels became "Key
Points" and menu numbers became fake "Statistics".

**Fix (IRIS):** `services/search/content.py` —
- Optional **trafilatura** (Apache-2.0, added to requirements-optional.txt,
  installed in venv) runs first on the raw HTML (favor_recall, no comments);
  trusted at ≥600 chars, else the longer of trafilatura / heuristic wins.
- New `_strip_boilerplate`: strips script/style/noscript/template/iframe/
  svg/nav/aside/footer/header + role-based (banner/navigation/contentinfo/
  complementary/search) + aria-hidden/hidden + class/id token matches
  (nav, menu, sidebar, cookie, breadcrumb, share, social, widget, popup,
  toc, …) *before* any main-content extraction; runs after the meta/js
  probes (which need the untouched tree); aux list/table/code extractors
  inherit the cleaned tree.
- New `_extract_main_content`: candidates = main/article/role=main +
  content-regex class/id hits, ranked longest-first with substring dedup
  (replaces concatenate-first-3 and its duplicate-text behavior).
- Two bs4 landmines defused during verification: (1) `Tag.decompose()`
  follows the next_element chain and stales/clears every element *after*
  the decomposed node — Wikipedia went 13,412 → 0 elements post-strip;
  switched to `extract()` (unlink only, topmost-offender filtering kept).
  (2) Dash-token matching hits skin/feature-flag classes —
  `vector-feature-main-menu-pinned-disabled` puts "menu" on `<html>`, RTD
  themes class the content pane `wy-nav-content` — so page roots
  (html/body/head) and any element containing the page's own `<h1>`
  (`_h1_ancestor_ids`, O(#h1·depth) ancestor marking) are exempt from the
  veto. Plus: dedup-loop empty-`acc` guard (`'' in text` is always True and
  skipped every candidate — heuristic was returning 0 chars on real pages
  while synthetic tests passed).

**Verification:** `py_compile` clean. Live before/after (fresh cache keys):
Wikipedia Cat 627 chars (nav ×3) → **109,938 chars article via trafilatura /
114,956 chars, 0 nav-junk hits via heuristic-only fallback**; Godot intro
header junk → clean 375-char content (tf and heuristic agree); synthetic
boilerplate test passes (nav/cookie/footer out, article in). Focused
search/fetch suite 41/41 green. Known pre-existing, out of scope: python.org
fetch fails in the outbound layer ("Refusing compressed response … after
requesting identity") — server ignores `Accept-Encoding: identity`;
unchanged by this patch. Old extraction results age out of the 2h content
cache on their own.

**Files touched:** `services/search/content.py`, `requirements-optional.txt`
**Status:** PENDING RESTART — server code change requires uvicorn bounce to take effect.

## 2026-10-27 — fix(search): statistics extractor shipped date crumbs as data; viewer-shell pages leaked UI chrome; PDF branch was a dead path (IRIS)

**Reported by Sir:** follow-up to the 2026-10-26 nav-soup fix — live
web_search test ("Nvidia Blackwell architecture specs") still showed slop
in the derived sections: "Data / Statistics: - 25 / - 2026 Blackwell /
- 5090 / - 6000 accelerates / - 6000 transforms", and one fetched page
was ~900 chars of PDF-viewer UI ("Thumbnails Document Outline ... Enter
the password to open this PDF ...").

**Root cause:** three weaknesses, all downstream of the fixed extraction:
(1) extract_statistics matched every bare digit run + optional glued word,
in document order, so date fragments ("25" from "October 25, 2026"),
model numbers ("RTX 5090", "RTX PRO 6000 transforms") and version strings
took the caller's 5-item cap before real measurements got a seat;
(2) get_tldr took the first 3 sentences with no quality filter;
(3) fetch_webpage_content had no concept of embedded-PDF-viewer shells,
and the PDF branch itself was a dead path — pdfminer.six was never
installed, so every PDF fetch silently returned "Failed to extract PDF
text" — and that failure was then cached for 2h (_cache_result cached
failures unconditionally).

**Fix (IRIS):**
- `services/search/content.py`, extract_statistics: matches keep the
  pinned `<number>[unit]` shape but are now tiered (currency/$, %, unit
  words → comma-grouped magnitudes → plain number+word pairs), deduped,
  and junk-filtered — bare unitless numbers, bare years (1500–2199), and
  ALL-CAPS product-code contexts (RTX 5090, PRO 6000) dropped; "$"
  prefix captured; TFLOPS/bandwidth units added; interior whitespace
  normalized (PDF text keeps newlines — "7\nGB"). Crash fix: the bare-year
  check previously fed 4-char decimals ("22.4") to int() — found live on
  the RTX Blackwell whitepaper.
- `services/search/content.py`, get_tldr: quality-filtered (30–400 chars,
  viewer/UI chrome skipped) instead of blind first-3.
- `services/search/content.py`: new `_VIEWER_CHROME_RE`; embedded-viewer
  shells (<1500 chars matching pdf.js viewer UI phrases) zero their
  content and set js_message, so core.py's non-empty content gate drops
  the block instead of shipping viewer chrome.
- `services/search/content.py`, `_cache_result`: failures no longer
  cached — a transient timeout or a since-fixed condition (pdfminer
  installed mid-session) must not poison a key for the 2h TTL; confirmed
  live when the post-install PDF probe was served the pre-install cached
  failure under the same key.
- `requirements-optional.txt` + venv: pdfminer.six (MIT, 20260107)
  installed and declared — the PDF branch's import guard made its
  absence silent. (The file's pypdf note predates the pdfminer-based
  branch.)
- `tests/test_extract_statistics.py`: policy change pinned (bare years
  are no longer statistics), plus regressions for the live date-crumb /
  model-number junk, unit ranking, and the decimal crash.

**Verification:** py_compile clean; focused suite 52/52 (was 47 pass / 4
fail mid-flight before the fixes landed). Live: the exact Blackwell junk
string extracts to []; realistic page text yields ['208 billion',
'192 GB', '32GB', '$1,999'] ranked with junk gone; viewer chrome skipped
in TL;DR. PDF end-to-end through fetch_webpage_content: 8.3MB Blackwell
whitepaper (exceeds the 2MB default soft cap — the live-search skip of
source [3] was TooLarge by design, not a bug; explicit max_bytes up to
the 20MB hard cap works) → 97,540 chars in ~2.3s, and extract_statistics
on it returns real measurements ('128 MB', '96 MB', '22.4 Gbps').
Operational note: an earlier multi-section apply_patch partially persisted
(only the viewer-gate hunk landed despite a full success diff); caught
by a NameError in test_web_fetch_plaintext + an on-disk grep audit,
re-applied as a single-section patch — patch persistence is now verified
against disk, not the tool's diff.

**Files touched:** `services/search/content.py`,
`tests/test_extract_statistics.py`, `requirements-optional.txt`
**Status:** PENDING RESTART — server code change requires uvicorn bounce to take effect.

## 2026-10-27 — fix(frontend): tagless-thinking reply heuristic swallowed markdown tables (IRIS)

**Reported by Sir:** "tables aren't rendered properly sometimes" — in
assistant replies, frontend rendering (not the web_search tool).

**Root cause:** not the table renderer — mdToHtml renders pipe tables
correctly (verified offline against the exact leaderboard table that
triggered the report: 5 headers, 25 cells, no leaked pipes; the streaming
segmenter cannot split a table either, since its freeze boundaries are
blank-line runs and tables contain none). The actual eater was the
TAGLESS-THINKING reply-start heuristic, which exists in two places:
markdown.js normalizePlainThinking and the chat.js _finalReply fallback.
When a reply starts with a reasoning-style prefix ("I can ...", "Let me
check ...", "I'll ...") and carries no think tags, the heuristic slices
thinking from reply at the first reply-start line ("Here", "OK",
"Absolutely", ...). A markdown table sitting before that line was
classified as thinking and silently dropped from the rendered reply —
visible during streaming (the live tail renders everything), gone after
finalize, which is exactly why it looked intermittent. Reproduced offline
before fixing: extractThinkingBlocks on "I can see the results now." + a
results table + "Here is the summary." returned reply content of ONLY
"Here is the summary." — the entire table eaten.

**Fix (IRIS):**
- markdown.js: new exported tableReplyFloor(text) — char offset of the
  first non-fence line with 2+ pipe characters (fence-aware, so a fenced
  table *example* inside a code block does not drag the boundary). All
  three boundary paths in normalizePlainThinking (paragraph-boundary,
  line-scan, within-line) now clamp to it: no reply boundary may start
  past a table block, because a markdown table is reply content, never
  reasoning. The fourth path (the "everything is thinking" fallback)
  bails out entirely when a table is present — not confidently
  splittable, so it shows the whole text as reply instead of hiding a
  table inside the thinking dropdown.
- chat.js: the _finalReply prefix-scan fallback gets the same floor via
  markdownModule.tableReplyFloor (line-scan and within-line variants).
- markdown.js mdToHtml: the paragraph pass no longer wraps table blocks
  in an invalid `<p><table>...</p>` (the HTML parser self-heals it, but
  it left stray empty `<p>` elements around every table); `<table` added
  to the paragraph lookahead exclusion.
- index.html: entry ?v= bumped for markdown.js and chat.js
  (tablefloor1) per house convention; SW is network-first for JS so a
  normal reload picks the fix up.

**Verification:** offline harness (Sandbox/table-render-repro, imports the
REAL markdown.js via symlink with only ui.js stubbed): pre-fix, the two
repro shapes ate the table; post-fix, the table leads the reply and the
thinking keeps only the reasoning prose. The verbatim leaderboard table
renders structurally identical before/after (no regressions; the invalid
p-wrap is gone). New regression suite
tests/markdown_table_reply_floor.test.mjs: 7/7 green. Existing suites:
markdown formatting 57/57, codefence placeholder regression OK, streaming
110/113 — the 3 failing loose-list invariants fail identically on the
PRE-PATCH tree (verified via git stash comparison), pre-existing and out
of scope for this fix. Operational note: the tooling's think-tag sanitizer
eats literal think tags and HTML entities from file-write payloads, so
these patches were authored without embedding tag literals and verified
against disk rather than the tool's diff. Worse, the tool-result DISPLAY
layer transposes digit pairs (the file's "20261023merge2" version string
displayed as "20260823" in both grep and sed output — ordinals and count()
are the only trustworthy views); the index.html ?v= bumps were applied via
digit-agnostic regex for exactly that reason.

**Files touched:** `static/js/markdown.js`, `static/js/chat.js`,
`static/index.html`, `tests/markdown_table_reply_floor.test.mjs`
**Status:** PENDING REFRESH — static JS change; a normal browser reload picks it up (SW is network-first for JS); entry ?v= bumped per convention.

## 2026-10-27 (cont.) — fix(frontend): one linkable domain in a table cell collapsed the whole table into raw pipe-text (IRIS)

**Reported by Sir:** "tables aren't rendered properly sometimes" — content
fully visible (all pipes, all rows), never formatted as a table. The earlier
same-night diagnosis (tagless-thinking heuristic eating tables) was a real,
cage-proven bug but NOT this one — Sir sees the table; that fix stays.

**Root cause (live-DOM-proven, session 41654bf7, dbId 6f798321):** the reply
bubble's raw contains perfect table markdown (42 pipes, clean rows), yet the
rendered HTML wrapped every row in its own <p>. Mechanism: the autolink pass
(case-insensitive gi) wraps a bare domain in a cell ("Z.ai" in the
leaderboard table) in an <a>; the <a>-preservation pass swaps it to an
___ALLOWED_HTML_n___ placeholder; the table pass's inherited blanket skip —
`if (table.includes('___CODE_BLOCK_') || table.includes('___ALLOWED_HTML_'))
return table;` — bailed on the ENTIRE table block; the paragraph pass then
wrapped each pipe row in a <p> and the restore pass put the link back inside
the raw text. "Sometimes" = only tables with a link/image/bare-domain in a
cell. Upstream's newest snapshot (odysseus-2c8e00c, same line ~1103) carries
the identical skip — upstreamable fix candidate.

**Why the offline harness missed it:** the Sandbox node harness's DOM shim
never defined window.location, so safeLinkUrl()'s
`new URL(url, window.location.origin)` threw inside its own try/catch and
silently returned '' — every autolink no-op'd, the harness ran a NEUTERED
pipeline, and every "table renders fine" was a false negative for
link-bearing tables. The house harness (tests/streaming/markdownHarness.mjs)
was honest all along (it provides window.location.origin). Lesson: a
silently-caught error in a stubbed dependency is a lie with a green
checkmark — before trusting a harness result, prove the stubbed path
actually executes.

**Fix (IRIS):**
- static/js/markdown.js: removed the table pass's blanket placeholder skip.
  Extracted placeholders (___ALLOWED_HTML_n___, ___CODE_BLOCK_n___,
  ___INLINE_CODE_n___) are pipe-free single-line tokens — safe as ordinary
  cell content; splitTableRow keeps each whole and the restore pass swaps
  them back inside their <td> (the inline-code family always flowed through
  cells exactly this way).
- static/index.html: markdown.js ?v= -> 20261027tablelinks1.
- tests/markdown_table_link_cells.test.mjs: 5 regressions pinning the live
  failure shapes (bare uppercase-domain cell, markdown-link cell,
  inline-code-with-pipes cell, fence-adjacent table, mixed-placeholder row
  column count), with the harness-environment lesson in the header.

**Verification:** live-page bisect on the actual bubble raw: orig => no
table, 42 pipes as paragraphs; Z.ai->Zlab => table renders; patched module
(fresh import) => table renders WITH the autolinked <a href="https://z.ai/">
inside the GLM-5.3 cell. Honest-harness (shim now provides location.origin +
template-capable createElement): full stored round text => table:true
rawPipes:0 z.ai-link:true. Suites: new 5/5, tableReplyFloor 7/7, formatting
57/57, codefence ok; streaming suite unchanged (3 pre-existing loose-list
invariant failures, stash-proven earlier tonight).

**Files touched:** `static/js/markdown.js`, `static/index.html`,
`tests/markdown_table_link_cells.test.mjs`
**Status:** PENDING REFRESH — reload the tab; history re-renders from stored bytes and the leaderboard table will format.

## 2026-10-27 (cont.) — fix(chat): mid-stream chat open in a second tab froze the tab — resume replay rendered per-token through a dead coalescer (IRIS)

**Symptom:** Opening a chat mid-turn in a NEW tab (while the LLM streams in
the tab that sent it) lags the new tab hard and the chat barely renders. The
already-open tab streams fine.

**Root cause:** Session open mid-stream goes selectSession →
_checkServerStream → resumeStream(), whose SSE replays the ENTIRE
accumulated buffer as a per-token burst (agent_runs.subscribe yields the
buffer event-by-event). The resume read loop called renderDelta() DIRECTLY
per delta, and renderDelta does full-text work per call —
_streamDisplayText (3 chained regex strips) + normalizeThinkingMarkup +
renderer update — i.e. O(buffer) per token, O(n²) across the burst. A
50KB thinking-heavy turn ≈ 15K tokens of full-text regex churn →
multi-second main-thread jam; UI starves, repaints barely happen. The
already-open tab never hits this: its live path uses thinking-analysis
gates + incremental projectors + rAF-coalesced thinking renders.

**The fix existed but was dead code:** queueRender() (chat.js, the 34ms
coalescer whose comment names "the known 'freeze-to-halt on mid-stream chat
open'") was defined and never called — the delta branch bypassed it. Likely
wired in a prior session's intent but the call was never switched.

**Fix (IRIS):**
- static/js/chat.js (resumeStream): delta branch renderDelta() →
  queueRender(). Safe: every tail path after the read loop renders final
  state canonically from roundText (plain path → chatRenderer.addMessage;
  rich path → session reload), and cleanup() sets _resumeClosed so a
  pending queued render can't fire post-teardown.
- static/js/chat.js (resumeStream): _tabSyncClearMirror(sessionId) right
  after _resumingStreams.add(). Second bug found while tracing: a
  chat-delta BroadcastChannel post from the streaming tab can land in the
  async gap between session-open rendering and resume attach
  (hasActiveStream still false) → a tab-sync mirror bubble is created and
  NOTHING cleared it on attach; on the plain-text finalize path it
  survived as a stale duplicate assistant bubble. The local reader now
  owns rendering at attach time, so the racing mirror is dropped (same
  call _tabSyncTakeover already makes before resuming).
- static/index.html: chat.js ?v= 20261027tablefloor1 → 20261027resumequeue1
  (modulepreload + script tag).
- static/sw.js: CACHE_NAME v394-20261024truncfix1 → v395-20261027resumequeue1
  + precache chat.js entry updated to match (SW's own bump rule).

**Verification:** node --check chat.js/sw.js clean; grep confirms delta
branch now hits queueRender (only remaining renderDelta call sites are the
definition + inside the coalescer's timeout). Streaming suite: segmenter
117/120 — the 3 failures are the loose-list invariants already
stash-proven pre-existing from tonight's table work, untouched here.
Live server serves index.html with the new ?v= and the new chat.js URL
(200). Runtime repro (needs a real mid-stream open) left for Sir:
SW is network-first for JS, so a plain reload of both tabs picks up the
patch; the ?v= bump force-busts HTTP cache + module map regardless.

**Files touched:** `static/js/chat.js`, `static/index.html`, `static/sw.js`
(.bak-20261027-resumequeue copies kept for all three)
**Status:** CONFIRMED by Sir same day ("performance is 10/10").

### 2026-10-27 (later) — resume-path thinking rendering (mid-stream reopen showed reasoning as plain reply text)

**Bug:** reopening a chat mid-turn in a NEW tab rendered the model's
reasoning as plain reply text in one long bubble — no thinking box, tools
invisible — until the turn finished, when the rich reload snapped everything
to canonical layout.

**Root cause:** the server replays vLLM reasoning deltas flagged
thinking:true, but the resume read loop appended json.delta RAW. The live
send path statefully wraps reasoning in `<think real="1">` markers (open on
first reasoning delta, close on first content delta); that wrapper was never
ported into resumeStream — its `_thinkOpen` flag sat declared-but-unused
(fossil of the unfinished 2026-10-12 resume work, same pattern as the dead
queueRender). No markers in roundText → normalizeThinkingMarkup had nothing
to wrap → reasoning rendered as answer text. Worse, the plain-text finalize
path passes the resume-accumulated roundText straight to
chatRenderer.addMessage, so a thinking reply finalized in place would have
kept its reasoning inline PERMANENTLY (only rich replies got fixed by the
reload).

**Fix (static/js/chat.js):**
- Resume delta branch now mirrors the live wrapper verbatim:
  neutralizeStrayThinkTags on reasoning deltas (model quoting a think tag in
  its reasoning must not break the boundary), stateful `<think real="1">`
  open, close tag on first content delta. Stateful (not substring-scan) so
  each round of a multi-round agent run gets its own thinking block.
- New local closeThinkIfOpen() (the live path's _closeOpenThinkingMarkup is
  a closure bound to live-path accumulated/currentAccumulated state, not
  reusable) called at: tool-event boundaries (tool_start/tool_output/
  tool_progress/agent_step/sources — mirrors the live path's agent_step
  closure so round 2 reasoning opens a fresh block), agent_terminal/
  chat_terminal, and the plain finalize — a stream ending mid-thinking
  never finalizes an unclosed tag.
- NOTE (pipeline hazard, for future sessions): emitting a literal think
  close tag in agent tool-call text gets silently STRIPPED before reaching
  the file — this patch's first apply landed empty-string closures
  (byte-verified via python repr, fixed by writing the tag from chr()
  construction). Always byte-verify after patching anything containing
  think-tag literals.

Live tool cards during resume remain deferred to the end-of-turn rich
reload BY DESIGN (resume loop only flags rich on tool events; porting the
agent-thread card machinery into the resume loop would be a feature lift,
not a regression fix).

**Verification:** node --check chat.js/sw.js clean; byte-level python check
confirms both closures carry real tag bytes (matching the live path's
line-shape exactly); streaming suite unchanged — 117/120, same 3 pre-existing
loose-list failures. The render chain itself is mirror-proven: the tab-sync
mirror path already renders tab A's marker-wrapped accumulated through the
identical normalizeThinkingMarkup → createStreamRenderer(liveThinking) chain
in second tabs. Version-bumped chat.js: index.html ?v= 20261027resumequeue1 →
20261027resumethink1 (modulepreload + script tag), sw.js CACHE_NAME
v395-20261027resumequeue1 → v396-20261027resumethink1 + precache entry.

**Files touched:** `static/js/chat.js`, `static/index.html`, `static/sw.js`
(.bak-20261027-resumethink copies kept for all three)
**Status:** PENDING REPRO — reload both tabs, send a reasoning-model turn,
open the chat in a second tab mid-stream: reasoning should render inside the
live thinking box (not as plain text), and stay separated after finalize.

## 2026-10-27 (evening) — fix(frontend): emphasis paired across paragraphs into giant italic blocks; stray think-tag + $-pair math verified ALREADY-FIXED (IRIS)

**Reported by Sir:** (1) "big blocks of the LLM's message italicized even
though it likely wasn't intended"; (2) a quoted closing think-tag inside
reasoning makes the UI end the thought early ("doesn't affect the LLM
itself, only the rendering"); (3) two `$` in a response compress/italicize
everything between (LaTeX) — "don't go searching too hard, I don't
remember if it's still a bug."

**Verdicts:**
- **(1) REAL, fixed tonight.** All five emphasis passes (bold `**`, italic
  `*`, strike `~~`, highlight `==`, sup `^`) used `[^X]+` content classes
  that match across newlines AND blank lines — two stray delimiters
  paragraphs apart paired up and wrapped the whole span between them (live
  repro: `2*3` in para 1 + a stray `*` in para 3 → `<em>` opened in para 1,
  closed in para 3). Fix: CommonMark rule — emphasis never crosses a
  paragraph boundary; matched content containing `\n\n` rejects the pair
  (raw delimiters stay literal text). Soft line breaks within a paragraph
  still pair. (`~sub~` was already whitespace-bounded.)
- **(2) ALREADY FIXED — verified, not re-fixed.** Both flagged-reasoning
  paths neutralize think-family tags inside every reasoning delta in force
  mode BEFORE the synthetic wrapper (live send chat.js:3308; resume/replay
  chat.js:5776), including tags split across delta boundaries (trailing
  partial-tag escape). DB forensics: 52 stored bug-shape occurrences
  (reasoning containing a literal closer with substantial text after it),
  ALL at rowid ≤ 8506 — the session that landed the fix — zero in the
  ~1,700 assistant messages since; every affected message was a
  DeepSeek/Kimi flagged-reasoning stream. End-to-end harness against the
  real rowid-8506 example (closer quoted inside a code block; whole-chunk,
  split-across-deltas, and control cases): no reasoning leak, thinking box
  holds the full text. Residual edge, deliberately untouched: the legacy
  text-based detector for streams passing raw inline tags without thinking
  flags would still bless a stray closer — no model on this instance uses
  that path (server-side parsing emits structured deltas); noted for the map.
- **(3) ALREADY FIXED — verified per the "don't dig hard" instruction.**
  The inline-`$` math pass is single-line-only with hardened Pandoc guards
  (opener must precede non-space, closer must follow non-space, no word-char
  after the closer). Same-line prose pairs ("costs $5 and $10"), cross-line
  pairs, and multi-`$` prose all stay prose; genuine `$x^2 + y^2$` still
  renders. 3/3 probe cases pass.

**Fix (IRIS):** static/js/markdown.js — the five emphasis passes converted
to callback form rejecting `\n\n` in matched content. static/index.html —
markdown.js `?v=` → 20261027emphasisfix1 (the concurrent session's chat.js
resumethink1 bump untouched; no file overlap between the two entries).

**Verification:** Sandbox probe5 (real module + honest shim, the shim that
proved the lying-shim lesson from the table hunt): 14/14 — cross-paragraph
pairs rejected for all five delimiter families, raw delimiters preserved,
legit + soft-break emphasis intact, stray-tag cases clean, `$` cases
clean. New tests/markdown_emphasis_paragraph_boundary.test.mjs: 4/4.
Existing suites: formatting 57/57, codefence ok, table-link-cells +
table-reply-floor 12/12, streaming 117 pass / 3 fail (the pre-existing
loose-list invariants, unchanged).

**Files touched:** `static/js/markdown.js`, `static/index.html`,
`tests/markdown_emphasis_paragraph_boundary.test.mjs`
**Status:** PENDING REFRESH — static JS change; a normal reload picks it up
(SW is network-first for JS); markdown.js `?v=` bumped per convention.

## 2026-10-28 — fix(backend): prefetched web search ran on bare continuation nudges ("ctn" → Christian Television Network sources) (IRIS)

**Reported by Sir:** "it seems that odysseus like putting my message through
web_search. All I said was 'ctn' (agent turn got stopped so I was 'restarting
it')" — with a screenshot of the reply's "6 Web sources" card: CTN Original
Programs, CTN Online, CTNX2026, CTN Events, Christian Television Network
(Wikipedia), Connecticut Network.

**Root cause (DB-forensics-proven, not a model decision):** the context-
prefetch web search (routes/chat_helpers.py build_chat_context →
chat_processor.build_context_preface(use_web=...)) runs on the raw user
message text, injects its results into the model's context as untrusted
reference data, and attaches them as web_sources — the UI sources card. The
existing low-signal guard (_is_casual_low_signal) only knows greetings/slang,
so a bare "ctn" sailed through and the prefetch searched the literal token.
Receipts: user "ctn" 02:15 → reply's web_sources = exactly the screenshot's
six CTN sources; user "uhhh ctn" 02:28 → web_sources = uhhh-meme/Tenor
results (the raw filler words as the query); "ctn" at 07:02 in the main
session → same CTN card. The GLM-5.3-flash model's own thinking confirms it
never called web_search — it *received* the CTN results "delivered as
untrusted source data" and had to reason around the garbage. Sir's phrasing
("odysseus like putting my message through web_search") was exactly right:
the system, not the model.

**Fix (IRIS):**
- routes/chat_helpers.py: new _CONTINUATION_NUDGE_RE — bare continuation
  nudges with optional filler/vocative prefixes (uhhh/um/hmm/er/ah/pls/
  please/sir) over the token family ctn, ctnue, ctnow, cont, continue, keep
  going, go on, carry on, resume, next, again, more, go — anchored ^...$ so
  "continue the function below" and "ctn events" do NOT match. Checked first
  in _is_casual_low_signal: nudges are now low-signal → no memory/skills/
  RAG/web-prefetch injection. Conversation history still flows, so the model
  can resume the interrupted work.
- src/agent_loop.py: ctn-family added to _EXPLICIT_CONTINUATION_RE so nudges
  inherit older user turns for tool retrieval (resuming an interrupted task
  needs the prior tool context). Deliberately NOT added to agent_loop's
  _is_casual_low_signal twin: that copy forces continuation=False in
  _classify_agent_request, which would defeat the resume machinery.
  Cross-reference comments added in both files to keep the vocabularies in
  sync.
- tests/test_continuation_nudge_gating.py: 29 parametrized cases — nudges →
  low-signal (17, incl. "Uhhh CTN!!" and "sir, ctn"), real messages →
  full-signal (5, incl. the bug-report sentence itself), nudges → explicit
  continuation (6), greeting behavior untouched (1).

**Verification:** py_compile clean; new suite 29/29; ReDoS verdict suite on
the edited regex 30/30 (house polynomial-redos regressions pass); foreground
routing suite 98 pass / 4 fail — the same 4 fail identically on the pre-patch
tree (git-stash comparison: cancelled-fallback provenance tests, pre-existing,
unrelated). Known follow-up candidate (NOT done): bare acknowledgments
("ok", "yes") outside agent_loop's continuation list would still prefetch on
the routes side — same disease class, awaiting a real complaint.

**Files touched:** `routes/chat_helpers.py`, `src/agent_loop.py`,
`tests/test_continuation_nudge_gating.py`
**Status:** PENDING RESTART — server code change requires uvicorn bounce to
take effect.

## 2026-10-28 — fix(backend): NVIDIA free tier MiniMax m3.1-flash context window pinned to 262,144 (IRIS)

**Reported by Sir:** `minimaxai/minimax-m3.1-flash` through the free NVIDIA API only offers 262,144 context window — Odysseus believed 1M and packed 900k budget into requests the API rejected with 400.

**Root cause:** two-layer lie stack.
1. NVIDIA's `/models` catalog reports **no `context_length`** for this model — catalog lookup returns nothing.
2. Odysseus's `KNOWN_CONTEXT_WINDOWS` table has `'minimax': 1000000` (substring match) → 1M window assumed.
3. Model card advertises "ISL up to 1M" — but the hosted trial endpoint enforces **262,144** (prompt + output combined, per API error: `{"limit":262144,"actual":346487}`).

Result: explicit 900k agent budget → `compute_input_token_budget` clamped only to model window → 900k prompt tokens stuffed into 256k pipe → API 400. Compactor never fired in time.

**Fix (IRIS):**
- `data/settings.json`: added `"minimaxai/minimax-m3.1-flash": 262144` to `model_context_overrides` — live override, hot-reloaded via settings TTL (2s), no restart.
- `src/model_context.py`: added provider-scoped known-table entry `'minimaxai/minimax-m3.1-flash': 262144` **before** the generic `'minimax': 1000000` so longest-match wins for this specific NVIDIA-hosted variant. Other providers (OpenRouter, etc.) still get the 1M entry.

**Verification:**
- Live probe with decrypted NVIDIA API key: oversized request (346,487 tokens) → `400 {"type":"context_length","limit":262144,"actual":346487}` — ceiling proven.
- Resolution check: `get_context_length()` → 262144, `get_context_length_known()` → (262144, known=True), `budget_context_for_model()` → 262144.
- Budget clamp: explicit 900k budget → `compute_input_token_budget(900000, 262144, explicit=True)` → **262144** (clamped to window).
- Compactor threshold: 85% of 262144 ≈ 222k (soft trim), mid-message trigger (600k) correctly above window → no double-compaction.
- `py_compile` clean on both touched files.

**Files touched:** `data/settings.json`, `src/model_context.py`
**Status:** LIVE — settings hot-reload (2s TTL) + known-table change effective on next resolution call (no process restart needed for model_context module; in-flight requests use cached values until TTL expiry).

**Note:** The 262,144 limit counts **prompt + output together** (API error arithmetic: 259,509 prompt + 4,096 max_tokens = 263,605 actual). Effective prompt budget is `min(262144 - max_tokens, 262144 * 0.85)` ≈ 222k for auto-trim, 258k hard ceiling with default 4k output.

## 2026-10-28 (13:41) — fix(ui): thinking-process box not clickable

**Symptom (user-reported):** Thinking process box renders but header/toggle won't respond to clicks — can't expand/collapse thinking sections.

**Root cause:** No explicit `pointer-events: auto` on `.thinking-header` or `.thinking-toggle` in `static/style.css`; an upstream stacking context or overlay could be swallowing pointer events before they reach the delegated click handler on `document` (which reads `data-thinking-id` from `.thinking-header` and looks up content/toggle by matching `id`).

**Fix:** Added `pointer-events: auto` to `.thinking-header` and `.thinking-toggle` in `static/style.css`.

**Files touched:** `static/style.css`
**Status:** Applied — needs frontend reload to take effect.

**Follow-up (same session, ~14:00):** `pointer-events: auto` alone did not resolve it. The delegated click handler in `static/js/markdown.js` only matched clicks landing directly on `.thinking-header[data-thinking-id]` — clicks on the toggle span, section body, or content area silently returned without toggling.

**Additional fix:**
- `static/style.css`: added `pointer-events: auto` to `.thinking-section` itself.
- `static/js/markdown.js`: delegated handler now falls back to `closest('.thinking-section')` → `querySelector('.thinking-header[data-thinking-id]')` when the direct header match fails, so clicks anywhere on the section toggle it.

**Files touched:** `static/style.css`, `static/js/markdown.js`
**Status:** Applied — needs frontend reload to take effect.

## 2026-10-28 (14:10, corrected 14:36) — revert(sessions): undo the loadSessions "sessionid sync" hack (truncate "permanent deletes" portion was a MISREAD — restored) (IRIS)

**Reported by Sir:** "It constantly refreshes the chat to 'ensure the frontend
knows the sessionid' … supposed to fix a bug with thinking sections not opening
on click. Somehow managed to cause new chats to be created when I'm trying to
send a message in an already created one. Then the new chat carries the old
chat's id, so when I go try to delete this new bogus chat, it deletes the old
one with all the data inside of it. Another IRIS is making deletes not
permanent. You go undo the code."

**Revert 1 — static/js/sessions.js → HEAD (a5c77f8a).** An undocumented
working-tree change-set (not in this changelog, mtime 10:21) had:
1. Appended an unconditional `if (targetId) { await selectSession(targetId); }`
   at the end of `loadSessions()` — re-running the FULL selection (history
   refetch + full re-render + composer clear + stream detach) on every
   `loadSessions()` call, including when the session was already current.
   loadSessions fires on dozens of triggers (every message save, stream
   completion, background poll, edit, delete), so the chat visibly refreshed
   constantly. The block's own comment ("Restore the resolved session so
   currentSessionId isn't null…") is the "ensure the frontend knows the
   sessionid" hack; selection was ALREADY handled a few lines above
   (`targetId !== currentSessionId → selectSession(...)`), so the block was
   pure duplication with side effects.
2. Removed the `_freshRootLoad` `Storage.remove('lastSessionId')` wipe and
   widened the `savedId` fallback — so any background `loadSessions()` could
   resurrect the PREVIOUS chat as `targetId` and the trailing select would
   force-navigate to it, racing the send/materialize flow (send-in-existing-chat
   materializing a new chat, stale selection carrying the old chat's id into
   the "new" row — deleting the bogus row then hit the old session's id).
   All three hunks were one change-set; the whole file is reverted to the last
   committed good state. Backup of the reverted state:
   `static/js/sessions.js.bak-20261028-nemotron-revert`.

**CORRECTION (14:36) — Revert 2 was a misread of Sir's instruction and is
fully undone.** Sir's line "Another IRIS is making deletes not permanent"
described the other IRIS's ACTIVE, wanted work (the archive-don't-burn
truncate reform), not a complaint. Within ~20 minutes of the mistaken edit,
`core/session_manager.py` was restored byte-identical to the pre-edit state
(`core/session_manager.py.bak-20261028-truncate-revert` — checked: diff of
backup vs current file was exactly the mistaken edit, no other-IRIS work
clobbered). Truncate is ARCHIVE-IN-PLACE again, exactly as the 2026-10-24
reform left it. The other IRIS's work on this file is untouched; the
`.bak-20261028-truncate-revert` copy can be deleted once the other IRIS
lands their work. Lesson recorded: when Sir mentions another IRIS working on
something, that work is WIP TO PRESERVE — revert only the code Sir actually
complained about, and when a directive is ambiguous about whether a behavior
is wanted, ask instead of guessing.

**Verification:** `node --check static/js/sessions.js` clean;
`py_compile core/session_manager.py` clean; pytest
`test_truncate_message_count_regression.py test_session_manager.py
test_session_ghost_delete.py test_delete_message_after_refresh.py` → 26/26
both before AND after the correction (i.e., the restored archive-in-place
version is green too).

**Files touched (net):** `static/js/sessions.js` (reverted to HEAD),
`ODYSSEUS-CHANGES.md`. `core/session_manager.py`: net change ZERO — the
mistaken edit was fully restored; the file is byte-identical to the other
IRIS's pre-edit state.
**Status:** sessions.js needs a browser reload (unversioned import; SW is
network-first for JS). No server restart needed for THIS entry — the
restored session_manager.py is the same bytes that were on disk before
14:12; any pending-restart state belongs to the other IRIS's own entries.

## 2026-10-28 (16:40) — fix(frontend): split-brain sessions.js recurrence #3 — send-after-reload materialized a phantom chat + URL swap (IRIS)

**Reported by Sir (live, mid-conversation):** reload a tab showing chat #123 →
send → URL silently rewrites to a brand-new #xyz (`replaceState`, no navigation)
while the UI keeps rendering #123's history; the agent's context is #xyz
(empty). Clicking the old chat in the sidebar could land on the phantom. Sir:
"an old Odysseus version had this issue, I had IRIS fix it, and now we're back
here."

**Root cause:** the 2026-08-05/06/09 split-brain landmine, re-armed. Module
identity = URL; mixed query strings = two instances of `sessions.js`, each with
its own `currentSessionId`. Working tree had 16 refs on
`sessions.js?v=20261023merge2` vs **3 bare** (app.js:26, index.html modulepreload
+ script tag). UI shell (app.js → `window.sessionModule`, sidebar,
loadSessions/selectSession) ran on the bare instance; the chat engine (chat.js
send path, chatStream) on the versioned one. Send-after-reload: engine instance
saw `currentSessionId = null` → materialized a new session → its materialize
wrote `history.replaceState('#xyz')` (URL swap without navigation) while the
shell instance kept rendering the old chat. Bonus: sessions.js's top-level
`hashchange` listener was bound by BOTH instances.

Provenance of the bare refs: index.html's were already bare at HEAD a5c77f8a
(merge-era regression — the 08-07 pattern: "the ghost bug's own split-brain was
quietly back"); app.js:26 went bare in the undocumented 05:15 version-sweep
today, which also un-versioned compare/index.js, modalManager.js and
research/panel.js in app.js. Nemotron's reverted loadSessions hack (see 14:10
entry) was a band-aid aimed at this bug's symptoms ("currentSessionId isn't null
on hard refresh… model-switch spawn a new chat").

**Fix — restore the 08-05 invariant (every ref → exactly one URL):**
- sessions.js: app.js:26 + index.html:252/2591 → `?v=20261023merge2` (19/19 refs
  unified).
- compare/index.js (app.js:14), modalManager.js (app.js:38), research/panel.js
  (app.js:49) → `?v=20261023merge2`, matching their versioned twins
  (slashCommands.js:23; calendar.js:7 + cookbook.js:3294 + app.js dynamic
  imports; chatRenderer.js:1419). sidebar-layout.js left bare — app.js is its
  only importer, no split.
- **markdown.js was a second live split** (2 refs on `emphasisfix1` vs 11 on
  `merge2` + 1 bare preload — two renderer instances): all 14 refs unified on
  `?v=20261027emphasisfix1` (chat.js:14, chatRenderer.js:5/6, chatStream.js:8,
  compare/index.js:41, compare/stream.js:5, document.js:12,
  documentLibrary.js:11, group.js:5, tasks.js:6, index.html preload, sw.js).
- sw.js: PRECACHE entries aligned to the exact URLs the page requests (11 stale
  entries: app.js, markdown.js, memory.js, models.js, document.js,
  compare/index.js, admin.js, init.js, slashCommands.js, emailInbox.js,
  tasks.js); CACHE_NAME `v396-20261027resumethink1` → `v397-splitbrain-unify1`
  per the SW's own bump rule.

**Verified:** `node --check` clean on all 11 touched JS files; grep audit over
all of static/ (lib excluded): **zero modules with mixed specifiers** — every
module resolves to exactly one URL.

**Deploy:** one hard refresh (Ctrl+Shift+R). SW re-installs under v397 and
re-precaches. No server restart needed (frontend-only).

**Lesson (3rd recurrence of this exact landmine):** any version-tag sweep or
merge resolution must finish with the 08-05 audit gate — every module resolves
to exactly one URL, grep-audited — BEFORE calling the work done. Both the merge
(index.html) and this morning's sweep (app.js) skipped it.

## 2026-10-28 (20:47) — feat(sessions): chat deletion was permanent — added a recycle bin (`deleted_at` soft-delete)

**Symptom (user-reported):** "I have accidentally deleted a handful of chat
sessions because Nemotron has completely borked chat session ids, everything's
cross over." Every delete was irreversible — `SessionManager.delete_session`
hard-deleted the messages, dropped the session row, purged session images and
detached documents. No tombstone, no trash, no recovery path.

**Root cause — one primitive, no soft-delete layer:**

`core/session_manager.py::delete_session` opened its own DB session, ran
`db.query(DbChatMessage).filter(...).delete()`, detached every
`DbDocument.session_id`, called `cleanup_session_images(session_id)`, then
`db.delete(db_session)` — all committed. The `sessions` table had no
`deleted_at` column and no listing path filtered on one, so there was nothing
to recover from even in principle.

**Fix — `deleted_at` soft-delete with an explicit purge path:**

1. **Schema** (`core/database.py`): `Session.deleted_at = Column(DateTime,
   nullable=True, default=None)` + `ix_sessions_deleted_at` index, exposed in
   `to_dict()`. Migration `_migrate_add_deleted_at_column()` — guarded,
   idempotent, registered in `init_db()` after `_migrate_add_mode_column()`.
   `cleanup_old_sessions` now skips trashed rows (`Session.deleted_at.is_(None)`).
2. **Model** (`core/models.py`): in-memory `Session` dataclass gained
   `deleted_at: Optional[Any] = None` so the cache can carry the marker.
3. **Core** (`core/session_manager.py`): `delete_session` stays the HARD
   delete (unchanged semantics — zero risk to existing callers). New:
   - `trash_session(sid)` — sets `deleted_at`, evicts from `self.sessions`,
     keeps messages/documents/images intact.
   - `restore_session(sid)` — clears `deleted_at`, re-hydrates into cache.
   - `purge_session(sid)` — explicit permanent destroy (alias of the hard path).
   - `list_trashed_sessions(owner)` — owner-scoped trash listing.
   Guards: `load_sessions` filters `deleted_at.is_(None)`; `_db_to_session_meta`
   carries the marker; `get_sessions_for_user` filters it; `_load_session_from_db`
   raises `KeyError` for trashed sessions so direct access cannot resurrect one
   into the cache; `cleanup_empty_sessions` skips trashed rows.
4. **Routes** (`routes/session_routes.py`):
   - `DELETE /api/session/{sid}` → **trashes** by default; `?permanent=true`
     purges. Starred sessions still blocked (403 `SESSION_STARRED`).
   - `POST /api/session/{sid}/untrash` — restore from trash.
   - `DELETE /api/session/{sid}/purge` — permanent delete of one trashed session.
   - `GET /api/sessions/trash` — owner-scoped trash list.
   - `DELETE /api/sessions/trash` — empty trash (purge all, owner-scoped).
   - `POST /api/sessions/bulk-delete` → trashes.
   - `list_sessions` and `/sessions/archived` queries filter `deleted_at.is_(None)`.
   - The AI **tidy** heuristic path (`/api/sessions/auto-sort`) now trashes
     throwaway/empty sessions instead of hard-deleting them — removed the
     `db.delete(row)` double-delete and sets `row.deleted_at` in the outer
     transaction. Incognito stays hard-deleted (ephemeral by design).
   - Incognito ghost purge keeps the hard path.
   - `DELETE /api/sessions/all` (admin Danger Zone) unchanged — permanent.
5. **UI** (`static/js/documentLibrary.js`): new **Trash** tab in the Library
   modal (alongside Chats/Documents/Research/Archive) with search, sort,
   multi-select, per-item Restore / Delete forever, and an Empty-trash bulk
   action. Trashed chats are not openable (click does nothing — `get_session`
   refuses them). Wording updated across `sessions.js`, `app.js` and
   `index.html`: "permanently" → "Move to trash"; toasts now say
   "Moved to trash".

**Verified:**
- `python -m py_compile` clean on all 4 touched Python files.
- `node --check` clean on all 3 touched JS files.
- Live-DB smoke test (create → trash → restore → purge): `deleted_at` set on
  trash with messages intact and cache evicted; `get_session` raises `KeyError`
  while trashed; trash listing sees it; restore clears the marker and
  re-hydrates; purge removes row + messages.
- Route table audit: all 5 new routes registered under `/api`, no shadowing
  (`DELETE /session/{sid}` vs `/session/{sid}/purge`, `GET /sessions/trash` vs
  `GET /session/{sid}` — different path shapes).
- Migration confirmed applied to the live DB (`deleted_at` column +
  `ix_sessions_deleted_at` index present in `data/app.db`).

**Deploy:** server restart required (backend changes; uvicorn runs without
`--reload`). Frontend needs only a normal reload — the SW is network-first for
JS/CSS and the server sends `cache-control: no-cache` with an ETag, so no
CACHE_NAME bump and no `?v=` tag sweep was needed.

**Note:** this protects *future* deletions only. Sessions already hard-deleted
before this change are not recoverable — there was no tombstone to recover from.

**Lesson:** the "delete" verb had exactly one meaning (permanent) across every
caller, so the fix had to add a second verb rather than redefine the first.
Keeping `delete_session` hard and adding `trash_session`/`purge_session` meant
zero risk to the incognito ghost-purge and admin-wipe paths, which genuinely
want permanent deletion.

## 2026-10-29 (12:05) — feat(library): trash-tab transcript preview — borked-name chats are now identifiable

**Follow-up to the recycle-bin entry above.** Live E2E (20/21) flagged one gap:
trash cards showed only name/model/count, and `GET /api/history/{sid}` 404s
while trashed (the `_load_session_from_db` cache guard — by design). With
Nemotron having scrambled names↔content, a bin entry identified by name alone
may not be identifiable — the exact failure mode this feature exists for.

**Root cause of the 404 (not a bug):** the no-limit history path hydrates via
`get_session`, which refuses trashed sessions so they can't re-enter the live
cache. The `?limit=` path reads straight from the DB and both hydration helpers
(`_session_needs_db_history_hydration`, `_hydrate_session_history_from_db`)
catch `KeyError` and bail — verified safe for trashed sessions, zero cache
pollution. So preview needs **no new backend endpoint**.

**Fix (frontend-only, `static/js/documentLibrary.js`):**
- `_toggleChatPreview(card, session, opts)` — new `opts.trashed` mode: fetches
  `/api/history/{sid}?limit=50` (DB path), footer swaps Open→(omitted) and
  Archive→Restore (`/untrash` + trash-grid refresh), Delete→"Delete forever"
  (`/purge` + confirm), Copy passes the flag through.
- `_copyChatById(sessionId, opts)` — same `?limit=100` DB path when trashed
  (the no-limit fetch 404'd there too).
- Trash cards: gained the hidden `.doclib-chat-preview` div, a click handler
  (`_toggleChatPreview(card, s, {trashed:true})` — same inline-expand pattern
  as the archive tab), and `cursor: pointer`.

**Verified:**
- `node --check` clean.
- Live authenticated E2E v2 against the running server: **15/15 PASS** —
  create → inject 2 msgs → trash → hidden from `/api/sessions` → in trash with
  `deleted_at` → history no-limit 404 (guard) → history `?limit=50` 200 with
  both messages intact → untrash → back in list, no-limit history 200 again →
  purge → 404 even on the DB path. Test session purged; DB left clean.
- One self-inflicted mid-edit regression (an `edit_file` old_string over-matched
  and dropped the `data`/`history`/`recent` lines) — caught on the diff,
  restored in the next edit, `node --check` confirms.

**Deploy:** normal reload only (SW is network-first for JS; `cache-control:
no-cache` + ETag). No backend change, no restart.

**Lesson:** when a guard makes a resource unfetchable by its normal route,
check for a side door *in the same API* before building a new endpoint — the
`?limit=` DB path already existed and was already trashed-safe.

## 2026-10-30 (11:30) — fix(agent): long-session "announces the tool, never fires it" — 4-layer fix (IRIS)

**Diagnosis** (session `dea27bea` autopsy + live NVIDIA probes): cross-turn
history stored assistant turns as prose-only (`metadata.tool_events` never
replayed as native calls), so long sessions showed the model hundreds of its
own turns ending in narration and zero examples of itself calling tools —
it learned "turns end with text" and EOS'd right after the preamble
("Hunting it:"), finish_reason invisible, nudge net too narrow. Fresh
sessions were immune. Usage arithmetic (`completion_tokens ≈ thinking +
text`, `usage_source: real`) proved the call was never generated — not
dropped by the app.

**Fix 1 — native tool replay (`src/tool_replay.py`, `routes/chat_helpers.py`):**
- New `replay_tool_events_as_native()`: rebuilds persisted tool_events as
  real assistant `tool_calls` + `role=tool` result messages in request
  history (newest-12 events/turn, 16k chars/turn budget, head+tail output
  truncation). Deterministic per message (content-derived call ids, fixed
  truncation) so local KV-cache prefixes stay byte-stable. JSON-dict
  commands (app_api) pass through as real args; others as `{"command": ...}`.
- `chat_helpers` gates on `_agent_route_tool_mode`: API models get native
  replay + a static anti-re-run note; text-transport models keep the prose
  digest (their within-turn history has no native calls either). Digest
  path unchanged otherwise.

**Fix 2 — finish_reason visibility (`src/llm_core.py`, `src/agent_loop.py`):**
- Streaming path now extracts `choices[0].finish_reason` (OpenAI-compat)
  and Anthropic `message_delta.stop_reason` (mapped to OpenAI vocabulary)
  and emits `data: {"type": "finish_reason", ...}` before [DONE].
- Agent loop records it per round (`round_finish_reasons`, and per-round
  `finish_reason` in usage_buckets) and logs a WARNING on `length` — a
  cap-truncated response is no longer indistinguishable from a voluntary
  stop.

**Fix 3 — explicit output cap (`src/agent_loop.py`):**
- `AGENT_MIN_OUTPUT_TOKENS = 16384` floor applied at `stream_agent_loop`
  entry (preset default 0 → param omitted → provider default governed).
  Clears the 8k webui slider ceiling; reasoning models burning 5-7k tokens
  thinking at long context no longer risk hitting a default cap right at
  the preamble→call boundary.

**Fix 4 — intent-nudge net widened (`src/agent_loop.py`):**
- `_looks_like_promise`: char gate 400→1200 (every real failure had a
  424-706 char preamble — the old gate excluded them all), plus a
  trailing-":" heuristic (the "Hunting it:" shape ends exactly there).
- `_INTENT_RE`: added `i can(?! see|help)|we can` starters, 14 new verbs
  (settle/hunt/fire/measure/grep/trace/scan/...), and a gerund-first line
  alternative (Hunting/Firing/Starting with/Reading...). `_matched_phrase`
  falls back to the text tail when only the colon heuristic matched.
- Gauntlet: all 6 real failure phrasings from `dea27bea` now trip the
  nudge; 5 negative controls (incl. "I can see", >1200-char colon) stay
  clean.

**Fix 5 — guard reword (`src/agent_loop.py`):** tool-verification note now
appends "(If no tools were meant to run this turn, this warning can be
safely ignored.)" — stays in content (that's how the AI sees it next turn)
without reading as an accusation on false positives.

**Verified:**
- `py_compile` clean on all 4 files.
- 27/27 on the directly-relevant suites (`test_action_intents*`,
  `test_tool_replay`, `test_history_compact_tool_calls`).
- Targeted slice: 1383 passed; 19 failures all confirmed pre-existing via
  worktree diff against the pre-change stash (`98fb964b`) — zero new
  failures. One red herring (`test_native_model_real_native_tool_call_is_
  executed`) is live-DB-state-dependent: passes with `ODYSSEUS_DATA_DIR`
  fresh, fails on the live DB with my patch reverted too.
- Replay unit smoke: pairing (call↔result ids), determinism (byte-identical
  re-renders), idempotence (no double-replay), char/event caps, JSON-dict
  args passthrough, digest fallback intact.

**Deploy:** backend change — needs a server restart (re-run.sh) to take
effect. No DB/schema change; replay is request-only and never mutates saved
history.

## 2026-10-30 (15:46) — fix(chat): "Regenerate from here" re-sent the last user message (duplicate bubble) instead of regenerating in place

**Symptom (user-reported):** clicking the ↻ Regenerate button on an AI bubble
just re-sent the last user message — a second copy of the user bubble appeared
and the new response streamed below it, instead of the response being
regenerated in place on the latest agent bubble with variant navigation.

**Root cause:** `static/js/chat.js::handleChatSubmit` captured the pending-flow
flags at send entry — `const skipBubble = _hideUserBubble; _hideUserBubble =
false;` (line ~1661, Finding A) — but the `try` block further down (~line 1977)
*re-declared* `const skipBubble = _hideUserBubble || !!approvalForSend;` in its
own block scope, re-reading the global that the entry capture had already
cleared. The shadowed read was therefore always `false` for regen/continue
(no tool approval), so `if (!skipBubble) addMessage('user', ...)` fired and a
duplicate user bubble was appended. The backend regen path was fine all along:
truncate with `keep_through_id` kept all context through the last user message,
`reuse_last_user=true` reused that row (no new user row in `chat_messages`),
and the new assistant row carried `variants` (original + regen) with the
`<n/m>` variant nav rendering on the new AI bubble.

**Fix:** entry capture now folds in the approval case
(`const skipBubble = _hideUserBubble || !!approvalForSend;`), and the try
block no longer re-reads the cleared global — it uses the outer entry-captured
`skipBubble` (comment updated to warn against re-adding the shadowing read).

**Verified live** (127.0.0.1:7001, session 8c8430b3…, glm-5.3-flash): before
fix, regen produced DOM `user, user, ai` (2 user bubbles sharing one dbId);
after fix, regen produces exactly `user, ai` — one user bubble (dbId
3670fa6b) + the new AI bubble with variant nav `<3/3>`, `<` flips to `<2/3>`.
Network: `POST /api/session/{id}/truncate {"keep_count":0,"keep_through_id":
"3670fa6b…"}` then `POST /api/chat_stream` with `reuse_last_user=true`. DB:
still exactly 1 non-archived user row; old assistant rows archived; new
assistant row has 3 variants. `node --check` clean on the edited module.

## 2026-10-30 (16:20) — fix(chat): regen from a USER message still double-sent (second user row, no variants)

**Symptom (user-reported):** "Still appears to double-send (with regen on
user-message)" — using the ↻ on a user bubble (footer "Resend message", or the
vision editor's "Regenerate message" which calls
`resendUserMessage(el, { replaceFromHere: true })`) left the user message
twice in history and the new reply without variant navigation.

**Root cause:** `static/js/chat.js::resendUserMessage` with `replaceFromHere`
truncated through the user row and set `_hideUserBubble = true`, but never set
`_pendingRegenUser = true` — so the send did NOT append `reuse_last_user=true`
and the backend persisted a SECOND user row (verified live: chat_stream body
had no `reuse_last_user` field; DB gained a duplicate non-archived user row).
It also never stashed `_pendingVariants`, so the new reply got no `<n/m>`
variant nav. The footer "Resend message" (no opts) skipped the truncate
entirely and appended a fresh user bubble + reply at the end.

**Fix (static/js/chat.js, resendUserMessage):** compute the first following
`.msg-ai` sibling; if one exists (or `replaceFromHere` was requested), the
call now delegates to the shared `regenerateFrom(nextAi)` — which truncates
with `keep_through_id`, stashes the old reply as variant 0, sets
`_hideUserBubble` + `_pendingRegenUser`, and resubmits — so the user row is
reused, not duplicated, and the new response lands on the latest agent bubble
with variant navigation. When no reply bubble exists yet, the manual path now
also sets `_pendingRegenUser = true`. Plain resend (no reply yet, no
replaceFromHere) still appends, unchanged. Companion fix from the previous
entry: the shadowed `skipBubble` re-read inside the send `try` block was
removed so the entry-captured value (which clears the global) is what the
bubble-suppression check actually uses.

**Verified live** (127.0.0.1:7001, session 4b1756ed…, glm-5.3-flash):
`resendUserMessage(userMsg, {replaceFromHere:true})` and the footer ↻ both
now produce DOM `user, ai` (was `user, user, ai` / duplicate user row before);
truncate body `{"keep_count":0,"keep_through_id":"78d6d573…"}`; chat_stream
body includes `reuse_last_user=true`; DB keeps exactly 1 non-archived user
row, old assistant rows archived, new assistant row carries variants
(2 after first regen, 3 after second); variant nav renders `<3/3>` and `<`
flips to `<2/3>`; after full page reload the DOM renders clean from DB
(1 user + 1 AI). `node --check` clean on the edited module.

## 2026-10-30 (19:25) — fix(agent): nudge now RECOVERS hallucinated work-log turns (post-deploy residual, session 200e825f) (IRIS)

**Residual found in the wild** (msg `48c84ab8`, 24 min AFTER the 16:06
restart — all five fixes from the 11:30 entry were live): the model wrote
"Updating the tally, then batch 8~" and then **fabricated the entire
batch-7 tally table in prose** (5.7k chars) instead of stopping — the
hallucinated-completion variant, not announce-then-stop. Small session
(83k tokens, 8% context), so the history-diet fix was never the relevant
layer here; this is per-turn flakiness. The tool-verification guard DID
catch it post-hoc (`tool_claims_unverified=true`, reworded note visible —
user commented on it next turn), but nothing recovered the turn.

**Forensics:** the nudge missed for three independent reasons — "Updating"
was not in the gerund list, the text does not end with a colon (it ends
with fabricated results), and 5723 chars > the 1200 gate. Worse, the guard
itself tripped on incidental verbs (`closed`, `running`) — `updated|updating`
was missing from `_TOOL_CLAIM_STRONG_RE` entirely (it had `edited|editing`
but not the sibling). Session scan: 6 of 9 post-restart assistant turns ran
zero tools in a tool-dependent workflow.

**Fix (all in `src/agent_loop.py`):**
- `_looks_like_promise` gains branch (b): when the recent user request was
  effectful AND the round prose narrates ≥2 distinct strong tool actions
  with zero tools run (`_looks_like_tool_claim_narration`, same detector as
  the post-loop guard), treat it as a broken promise at ANY length — the
  in-loop nudge now gives the model a second chance to actually run the
  tool instead of only flagging after the fact.
- Gerund-first list += updating/writing/adding/creating/sending/marking/
  translating/summarizing/compiling/building.
- `_TOOL_CLAIM_STRONG_RE` += `updated|updating`.
- Nudge message gains a fabrication sting when only the narration branch
  fired: "Your reply also describes results as if tools had already run —
  none did this turn. Never present fabricated output as a tool result."

**Verified:**
- `py_compile` clean; 27/27 on the relevant suites (`test_action_intents*`,
  `test_tool_replay`, `test_history_compact_tool_calls`).
- Gauntlet: the REAL 48c84ab8 specimen now fires via regex+narration
  (double-covered); all six earlier failure shapes still fire; six
  negatives stay clean, incl. honest past-tense summaries (effectful-gate
  holds), "I can see", fenced replies, and >1200-char colon-only text.
- Known boundary: bare "All 15 edits landed" claims with zero strong verbs
  still slip the narration detector (≥2-verb threshold is the accepted
  trigger-happiness tradeoff).

**Deploy:** backend change — needs a server restart to take effect.

---

## 2026-10-30 20:35 — Chat-box thinking control (per-session reasoning_effort) (IRIS)

**What:** the reasoning/thinking control moved into the chat box. A lightbulb
button in the composer's left toolbar (`#thinking-btn`) opens a dropdown:
**Default / Off / Low / Medium / High / Max**. Stored per session in
localStorage (`odysseus:reasoning:<sid>`), sent as `reasoning_effort` on every
`/api/chat_stream` (form field; JSON body also accepted) and `/api/chat`.
"Default" = no override → the global `thinking_enabled` setting in the
Settings panel still applies (that card now points at the chat-box control).

**Backend:**
- `src/llm_core.py`: new per-request ContextVar `_REQUEST_REASONING` +
  `set_request_reasoning()` / `normalize_reasoning_override()` ('none'→'off',
  'default'/'auto'/'on'→None) + `_apply_request_reasoning_effort()`, applied
  at all three payload build sites (non-stream chat, utility, stream).
  Graded levels are only sent to providers known to accept them — NVIDIA NIM
  (GLM-5.x accepts low/medium/high/max per Z.AI docs, passed verbatim),
  self-hosted local vLLM-style, Groq/Mistral (max→high), OpenRouter
  (`reasoning:{effort}`, max→high), OpenAI reasoning models (max→high, and
  skipped entirely for GPT-5.x + tools, which reject the field). Unknown
  public hosts get nothing (no 400 risk). 'off' rides the existing no_think
  path (`chat_template_kwargs.enable_thinking:false` on NIM/vLLM etc.).
- Cache keys partition on the override (`_get_cache_key(extra=...)`); None
  values are dropped so no-override hashes match pre-feature keys (no cache
  invalidation on deploy).
- **Bug fixed along the way:** the STREAM path never called
  `_apply_thinking_off_openai_compat` and didn't pass `force=no_think` to the
  DeepSeek scrub — so the global thinking toggle's off-switch never reached
  OpenAI-compat providers on `/api/chat_stream` (the main chat path). Now it
  does.
- `routes/chat_routes.py`: both endpoints set the ContextVar from the request
  (scoped to the request task; the streaming generator and agent loop inherit
  it — `stream_agent_loop` is awaited inline in the handler).
- `src/request_models.py`: `ChatRequest.reasoning_effort` with validator.

**Frontend:** `static/index.html` (composer control + settings-card hint),
`static/js/chat.js` (per-session state, menu wiring, `fd.append`), 
`static/js/sessions.js` (refresh button on session open), `static/style.css`.

**Verified:** py_compile clean; `node --check` clean on chat.js/sessions.js;
24/24 llm_core-adjacent tests pass; payload unit checks (nvidia levels
verbatim, off→no field, openrouter/groq mapping, unknown-host safe, GPT-5
tools guard, cache partition + legacy-key compatibility). One pre-existing
failure (`test_app_config_shared_fetch_js` — settings.js:509 POST lacks cache
invalidation) confirmed present at HEAD, unrelated.

**Deploy:** backend change — needs a server restart; frontend is static files
(served fresh on reload, SW cache-busted by deploy).

---

## 2026-10-30 21:15 — fix(ui): thinking-level popup was clipped to a sliver (portal to <body>) (IRIS)

**Bug:** the chat-box thinking menu rendered as "a line with shading" —
`.chat-input-left` is `overflow: hidden` and `.chat-input-bar` has
`container-type: inline-size` (a containing block for fixed/absolute
descendants), so the in-place `position: absolute; bottom: 100%` menu was
clipped to ~0px inside the composer row. Reproduced in a standalone harness
(real style.css + real composer markup + the real control block sliced from
chat.js): menu rect y=-108 h=202 vs overflow row y=100..132 → 0px visible.

**Fix:** `initThinkingControl()` in `static/js/chat.js` now portals the menu
to `<body>` while open (same pattern as the overflow "+" menu in app.js),
pins it `position: fixed` 8px above the button (clamped to viewport),
repositions on scroll/resize, and restores it to `#thinking-wrap` on close.
`style.css`: `.thinking-menu` is now `position: fixed; z-index: 10000;
max-height: 60vh; overflow-y: auto`. Also added `#thinking-btn` to the
mobile textarea-refocus exclusions in `static/app.js` (no keyboard bounce
when tapping the button).

**Verified in-browser** (standalone page on :7999, since the app itself is
behind login): open → menu portaled to BODY, fixed, 184x202, fully in
viewport, 6 items visible; pick "Low" → closes, label "Low", button
active, `localStorage['odysseus:reasoning:<sid>']='low'`; reopen works.
Screenshot confirmed the rendered dropdown. `node --check` clean on
chat.js/app.js. Test harness removed afterwards.

**Deploy:** static files only — no server restart needed, just reload
(SW cache-busted on deploy).

---

## 2026-10-31 04:35 — fix(agent): intent-without-action guard is now PASSIVE (flag-only, no nudge/kill) + wrap-up exemption (IRIS)

**Bug (specimen chat d4dbac50, msg 6c157fb3):** the in-loop supervisor nudged
the model whenever a no-tools round looked like an unfinished promise. On a
wrap-up summary (tools ran in earlier rounds, final round is prose with >=2
strong verbs) it nudged, the model re-wrote its finishing summary, tripped
again, and after _MAX_INTENT_NUDGES=2 the run was KILLED with
"The agent stopped because it repeatedly announced a tool action without
making the tool call." Specimen rounds 27-29 are three near-identical
re-written summaries, then the kill.

**Fix (per Sir: "just have the guard flag the message"):**
- `src/agent_loop.py` supervisor: the nudge system-message injection and the
  `intent_nudge_exhausted` kill are REMOVED. Detection still runs in-loop;
  on a hit it only sets `_intent_without_action = True` and logs, then the
  round ends normally. The message stands as written.
- Post-loop guard folds the flag in: `_tool_claims_unverified =
  _intent_without_action or (not tool_events and effectful and narration)`
  → appends the existing visible "⚠ Described tool actions did not execute…
  (can be safely ignored)" note as a normal delta + sets the
  `tool_claims_unverified` metrics/metadata flag. Pure passive labeling.
- Wrap-up exemption: new `_looks_like_conclusion()` (conclusion phrases in
  head/tail 250 chars) + `_tools_ran_in_history_since_last_user()`; a round
  that is BOTH conclusion-shaped AND corroborated by prior tool work
  (run-level `tool_events` or native tool messages in history since the last
  user msg) is the model FINISHING — not even flagged. Pure hallucinations
  (zero tools anywhere) are still flagged.
- `_intent_nudge_count` / `_MAX_INTENT_NUDGES` removed (no longer referenced).
  Frontend `intent_nudge_exhausted` handlers left in place (dead, harmless).

**Tests:** rewrote `test_emits_intent_nudge_exhausted_when_cap_is_exhausted`
→ `test_intent_without_action_is_flagged_not_nudged_or_killed` (no kill
event, no extra rounds, ⚠ note + metrics flag present); added
`test_hallucinated_work_log_with_zero_tools_is_flagged` and
`test_wrap_up_summary_after_real_tools_is_not_flagged`.
69/69 on test_agent_rounds_exhausted + test_tool_policy + test_action_intents*
+ test_continuation_nudge_gating; 128 passed on the wider agent-loop slice
(the 1 failure, test_agent_loop_tool_output_truncation
::test_default_limit_matches_constant, is PRE-EXISTING: tool_utils
MAX_OUTPUT_CHARS=50000 vs test asserting 10000 — untouched by this change).
Helper unit checks pass (conclusion detector, history tool scan).

**Deploy:** backend change — takes effect on next server restart. NOT
restarted now per Sir ("don't force a restart"); the running server keeps
the old behavior until then.

## 2026-10-30 (16:35) — fix(chat): "Regenerate from here" button vanished from AI bubbles on page refresh

**Symptom (user-reported):** the ↻ Regenerate button was present during a live
session but disappeared from the AI message footer after a refresh.

**Root cause (two holes):**
1. `static/js/chatRenderer.js::addMessage` (the history-reload path) built the
   footer with `wrap.appendChild(createMsgFooter(wrap))` BEFORE
   `box.appendChild(wrap)`. `createMsgFooter` evaluates the regen action's
   `available: () => _hasAdjacentUserPrompt(msgElement)` immediately, and that
   guard starts with `if (!msgElement.parentNode) return false` — a detached
   bubble has no siblings, so the guard was always false on reload and regen
   was filtered out of the footer entirely (it is a pinned action, so it did
   not even fall into the "···" overflow). Live-stream paths attach the bubble
   first and build the footer at stream end, which is why it only vanished on
   refresh. Same detached-footer ordering existed in the research-result
   bubble path (`static/js/chat.js` ~line 7022).
2. `_hasAdjacentUserPrompt`'s walk-back treated the r=0 bubble of the SAME
   multi-round agent response as a foreign AI response, so on reload of an
   agent turn (footer lands on the last round bubble) regen was hidden too.

**Fix:**
- `addMessage`: `box.appendChild(wrap)` now happens BEFORE footer creation
  (both assistant and user branches).
- research-result path in `chat.js`: `_box.appendChild(_wrap)` moved before
  `createMsgFooter(_wrap)`.
- `_hasAdjacentUserPrompt`: a preceding `msg-ai` (non-continuation) bubble
  whose `dataset.dbId` matches the current bubble's dbId is the same
  response's first round — the walk skips it and continues to the user
  prompt. Different dbId (a previous turn's response) still returns false, so
  the orphan guard (hide regen when the user message was deleted) is intact.

**Verified live** (127.0.0.1:7001, session fd5f9219…, glm-5.3-flash): before
fix, after a full reload the AI footer actions were `[continue, copy, delete]`
— no regen. After fix, post-reload footer is `[continue, regen, copy, delete]`
with title "Regenerate from here"; clicking it post-refresh fires
`POST /api/session/{id}/truncate {"keep_count":0,"keep_through_id":…}` then
`POST /api/chat_stream` with `reuse_last_user=true`; DOM stays at exactly
1 user + 1 AI bubble; DB keeps 1 non-archived user row, old reply archived,
new reply carries variants=2 with `<2/2>` nav; a second reload keeps the
button pinned on the variant bubble. Synthetic DOM checks: regen shown on a
normal bubble and on the last round of a same-dbId multi-round response,
hidden on a true orphan (no preceding user message). `node --check` clean on
both edited modules.

## 2026-10-30 (23:10) — feat(chat): Continue button = same-turn prefill (no handshake user message) + fix UnboundLocalError in chat_stream

**Feature (user-requested):** the Continue button (footer ▸ on the last AI
bubble, and the "[Message interrupted]" indicator) no longer sends a hidden
user message like "Your previous response ended with: … Do NOT repeat…".
Instead it sends an EMPTY message with `continue_assistant=true`; the model's
own partial reply stays as the trailing assistant message and the provider
just keeps writing (prefill, same turn). The continuation merges SEAMLESSLY
into the same bubble (no `*(continued)*` marker) and into the SAME DB row
(server-side merge), the stopped badge is cleared, and no user row is created.
Prefill only applies in chat mode on the LAST AI bubble; agent mode and
middle-bubble continues keep the legacy handshake flow.

**Files:**
- `routes/chat_routes.py`: parse `continue_assistant` right after the last
  `chat_mode` override (~line 1216) — it is first used in
  `coerce_message_and_session(allow_empty=...)` at ~line 1291. (An earlier
  version assigned it at ~line 1478, causing `UnboundLocalError: continue_assistant`
  on EVERY chat_stream call — fixed by moving the assignment up; AST-verified
  store-before-load.) `allow_empty` now includes the flag; `build_chat_context`
  gets `continue_assistant=` and `persist_user_message=... and not
  continue_assistant`; draft checkpointing skipped during a prefill turn
  (`_checkpoint` returns None — the disconnect path merges the partial into
  the same row instead); `save_assistant_response` / `_persist_stream_partial`
  calls pass `continue_assistant=`; background memory extraction gated off for
  prefill turns.
- `routes/chat_helpers.py`: `build_chat_context(continue_assistant=...)` —
  forces `persist_user_message=False` and `casual_low_signal=True` (no
  memory/skills/RAG/web prefetch on an empty nudge), and a `_tail_insert`
  helper puts the datetime + tool-replay context notes BEFORE a trailing
  assistant message so the last message stays assistant (prefill) instead of
  being answered as a user note. `save_assistant_response(continue_assistant=...)`
  merges the reply into the last assistant row via
  `session_manager.append_to_last_assistant(..., clear_stopped=True)` and
  returns that row's id (falls back to a normal add if no eligible row).
  `_persist_stream_partial(continue_assistant=...)` appends a cut-off partial
  to the same row keeping `stopped:True`.
- `core/session_manager.py`: new `append_to_last_assistant(session_id,
  extra_content, metadata, clear_stopped=False)` — appends text to the last
  non-archived assistant message IN PLACE (in-memory history + DbChatMessage
  row, matched by `metadata._db_id` with fallback to newest non-archived
  assistant row); pops `draft`, optionally `stopped`/`stream_error`.
- `static/js/chat.js`: `_continuePrefill` flag + `setContinuePrefill` +
  `continueFromBubble(el)` (chat mode + last AI bubble → prefill with empty
  input; otherwise legacy handshake text; clicks send). `handleChatSubmit`
  captures `continuePrefill`, allows empty message when `pendingContinue`,
  appends `continue_assistant=true` to the FormData (chat mode only), and the
  stream-end merge is seamless (`oldRaw + newRaw`, no separator, no
  merge-last-assistant POST) for prefill, legacy `*(continued)*` otherwise;
  stopped badge removed on merge. Stopped-indicator Continue handlers now
  call `continueFromBubble`. Both new functions exported on `chatModule`.
- `static/js/chatRenderer.js`: footer Continue handler and the
  refresh-rendered stopped-indicator Continue now call
  `window.chatModule.continueFromBubble(...)` instead of building the
  handshake text inline.

**Verified statically:** `py_compile` clean on all three py files; AST check
confirms first store of `continue_assistant` (line 1216) precedes first load
(line 1291) in `chat_stream`; `node --check` clean on both JS modules.
Live end-to-end verification pending the user's own server restart
(re-run.sh Ctrl+C) — server is NOT restarted by the assistant per user rule.

---

## 2026-10-31 05:20 — fix(llm_core): NIM "thinking off" actually off — reasoning_effort "low" (verified live) (IRIS)

**Bug:** chat-box Thinking=Off (and the global thinking_enabled toggle) sent
only `chat_template_kwargs: {"enable_thinking": false}` for NVIDIA NIM —
which NIM IGNORES for GLM-5.x. Verified live against
integrate.api.nvidia.com with glm-5.3-flash: template-only still streams
~200-800 chars of reasoning_content (trivial + hard prompts); "none" and
"minimal" are also NOT honored (model thinks MORE: 909/199 chars).

**Verified live (2026-10-31, NIM, glm-5.3-flash):**
- `reasoning_effort: "low"` → **0 reasoning chars**, non-streaming AND
  streaming, trivial and hard prompts. Safe with tools: tools+low returns
  tool_calls normally (no 400). ← the real off-switch on NIM.
- GLM accepts low/medium/high/max verbatim. mistral-large-4-1t-a52b accepts
  low/medium/high but **400s on "max" and "none"**; nothing fully suppresses
  its thinking (provider limitation — "low" is the floor).

**Fix (`src/llm_core.py`):**
- `_apply_thinking_off_openai_compat`: nvidia branch now sends
  `reasoning_effort: "low"` AND `chat_template_kwargs` (template kwarg kept —
  harmless on NIM, still the switch for self-hosted vLLM, which keeps its own
  branch). Affects both the chat-box Off and the global toggle.
- `_apply_request_reasoning_effort`: nvidia levels pass verbatim for GLM
  models; "max" clamped to "high" for non-GLM NIM models (mistral 400s).

**Verified:** payload unit checks (off→low+template on glm AND mistral;
glm low/medium/high/max verbatim; mistral max→high; default→no fields);
py_compile clean; 26/26 llm_core-adjacent tests pass. The 10 failures in the
broad "cache/thinking" pytest slice are pre-existing and unrelated (fallback
delta logic, kv-cache, approval routing — my diff touches none of them).

**Deploy:** backend change — live on next server restart (running server
started 22:13, before this fix). NOT restarted per Sir's standing "don't
force a restart".

## 2026-10-31 (10:35) — fix(chat): make Continue-prefill actually fire (agent-mode gate + ghost handshake rows)

**User report:** Continue still sent the legacy handshake user message
("Your previous response ended with: …") — visible in the server log as an
[agent-intent] turn through stream_agent_loop — and the ghost handshake row
only appeared in the chat history after a reload.

**Root causes:**
1. `continueFromBubble` gated prefill on `!agentMode`, so with the mode toggle
   on agent the click took the legacy handshake branch (and the request went
   to the agent loop). A Continue is a pure text continuation, so mode must
   not matter.
2. The send path appended `continue_assistant` only when `!isAgentMode`, and
   sent `mode=agent` — so even a prefill-armed click in agent mode never
   reached the prefill backend path.
3. The history renderer (`sessions.js::_renderHistoryMessage`) filtered some
   handshake prefixes but not "Your previous response ended with:" — hence the
   ghost bubble on reload. `get_context_messages` also still fed those rows
   to the model.

**Fix:**
- `static/js/chat.js`: `continueFromBubble` now prefills whenever the clicked
   bubble is the LAST `.msg-ai` (mode-independent; middle bubbles keep the
   handshake). In `handleChatSubmit`, `if (continuePrefill) isAgentMode = false`
   so the request goes out as `mode=chat` + `continue_assistant=true`.
- `routes/chat_routes.py`: `continue_assistant` is parsed unconditionally
  (line ~1215, still before first use — AST-verified) and, when set, forces
  `chat_mode = "chat"` so the request never enters `stream_agent_loop`, even
  if the toggle/auto-escalation promoted the turn.
- `core/models.py::get_context_messages`: user rows starting with
  "Your previous response ended with:" / "Your previous response was
  interrupted." / "Your message was cut off." are excluded from LLM context.
- `static/js/sessions.js::_renderHistoryMessage`: added the
  "Your previous response ended with:" prefix to the render filter so legacy
  ghost handshake bubbles no longer appear on reload.

**Verified (no server restart — static files are served network-first, and the
running backend already has the flag handling):** `py_compile` clean;
`node --check` clean; AST store-before-load for `continue_assistant`;
harness test of `build_chat_context(continue_assistant=True, message="")`:
no user row persisted, trailing message is the partial assistant, datetime
context inserted BEFORE it (prefill-safe); control turn unchanged.
`SessionManager.append_to_last_assistant` tested against a temp
DATABASE_URL db: merges content into the SAME row (DB + in-memory), clears
`stopped`, merges metadata, returns the row id, returns None when there is no
assistant tail (caller falls back to a normal add).

## 2026-10-31 (12:05) — fix(chat): Continue-prefill live-verified end-to-end; send-btn newchat-mode trap fixed

**Root cause of "still sends handshake":** three stacked issues —
1. `continueFromBubble` clicked `.send-btn`, but with an EMPTY composer the
   button is in `data-mode="newchat"` (app.js:4036) and clicking it opens a NEW
   CHAT instead of sending. Now it calls `handleChatSubmit({preventDefault(){}})`
   directly (same pattern as `_setComposerAndSend`).
2. Prefill was gated on `!agentMode` — with the toggle on agent the click took
   the legacy handshake branch and the request went to stream_agent_loop.
   Now prefill applies whenever the clicked bubble is the LAST `.msg-ai`
   (mode-independent); the send forces `isAgentMode=false` so the request goes
   out as `mode=chat` + `continue_assistant=true`.
3. Backend gate `continue_assistant = flag and chat_mode=="chat"` replaced:
   the flag is parsed unconditionally and forces `chat_mode="chat"` when set,
   so a prefill request never enters the agent loop even if the toggle or
   auto-escalation promoted the turn.

**Live-verified against the running server (no restart — static JS is
network-first, and the 10:29 boot already had the flag handling):**
- Continue on a completed reply: request had EMPTY message + `mode=chat` +
  `continue_assistant=true`; model prefilled; DB row `3d23fc5c` grew
  `MELON-31` → `MELON-31MELON-31` in place (no new user/assistant row,
  `message_saved` returned the same id); DOM merged seamlessly into the same
  bubble, no `*(continued)*` marker, footer intact.
- Stop mid-stream → partial row saved `stopped=True` → Continue on the last
  bubble: same empty+flag request; row `1a973e0f` grew 0 → 24764 chars,
  `stopped` cleared, same row id; DOM: stopped indicator removed, single
  merged bubble.
- Ghost check: session 349bf43f (which has a legacy handshake row) renders
  with 0 handshake bubbles after reload — `sessions.js` render filter now
  includes "Your previous response ended with:".
- Harness tests (temp DATABASE_URL): `build_chat_context(continue_assistant=True,
  message="")` persists no user row and leaves the partial assistant as the
  trailing message with the datetime note inserted BEFORE it;
  `append_to_last_assistant` merges content into the same DB row + in-memory
  history, clears `stopped`, merges metadata, returns the row id, returns None
  when there is no assistant tail; `get_context_messages` excludes handshake
  user rows.

**Files this round:** `static/js/chat.js` (continueFromBubble direct submit +
mode-independent prefill; send path forces chat mode + flag),
`routes/chat_routes.py` (unconditional flag parse + force chat_mode),
`core/models.py` (handshake rows excluded from LLM context),
`static/js/sessions.js` (render filter prefix added).

## 2026-10-31 (20:10) — fix(chat): agent-mode Continue resumes the agent loop (tools intact) instead of forcing chat mode

**User need:** free NVIDIA endpoint 504/429s mid-agent-turn at the tool
reconnect; user was manually typing "ctn". The Continue button must resume the
agent's WORK (more tool calls allowed), not just prefill text.

**Change:** `continue_assistant` is now parsed unconditionally (no
`chat_mode == "chat"` gate, no force-`chat_mode`). Semantics per mode:
- chat mode: text prefill — trailing assistant message, same-row merge
  (`continue_prefill = continue_assistant and chat_mode == "chat"` gates the
  merge to chat mode only).
- agent mode: `persist_user_message=False`, request routes to
  `stream_agent_loop` as usual; native tool-event replay
  (`replay_tool_events_as_native`) rebuilds the persisted tool_events as
  assistant tool_calls + role=tool results at the context tail, so the loop's
  first model call continues right after the tool results with full tool
  access. Agent rounds persist as their own rows (no same-row merge).
- All `save_assistant_response` / `_persist_stream_partial` call sites now pass
  `continue_assistant=continue_prefill` (merge only in chat mode).
- Frontend: removed the `if (continuePrefill) isAgentMode = false` force —
  agent mode sends `mode=agent` + `continue_assistant=true` + empty message.
  `continueFromBubble` prefills on the LAST AI bubble in any mode; middle
  bubbles keep the legacy handshake.

**Verified:** harness (stubbed deps, `src.agent_loop._agent_route_tool_mode`
patched to API-model) with history [user task, assistant(stopped, tool_events)]
+ `agent_mode=True, continue_assistant=True, message=""`: add_user_message NOT
called (history stays 2), tail = [user, assistant w/ native tool_calls(bash),
tool result, replay note]. Chat-mode prefill was live-verified earlier against
the running server (empty message + flag → same-row merge, seamless bubble).
py_compile + node --check clean. Agent-mode resume backend loads on the user's
next re-run.sh restart (assistant does not restart the server per user rule).

## 2026-10-31 (20:55) — data surgery (no code change): repair hallucinated-tool-call turn in forked session 79fe8eec (data/app.db)

**User need:** in forked chat `79fe8eec-94db-45ce-af1c-ff7d61bb42e6`, assistant
message `3ea3ee07-…` was stopped mid-generation after narrating "Updating the
tally, then your Q52 homework~" but before any tool executed — saved as
prose-only (`stopped: true`, no `tool_events`). The follow-up turn
`a300b0d9-…` actually ran `write_file` (bdsmtest_answers.md, 2820 bytes), with
the user's "nuh uh run your tools ma'am" (`5eb9dad3-…`) in between. Sir asked
to rewrite history: merge the two assistant turns into one that owns the tool
call, drop the user message between them.

**Change:** `data/app.db` `chat_messages` only (direct SQLite, app running in
WAL mode; FTS triggers kept `chat_messages_fts` in sync):
- `3ea3ee07-…` row: content replaced with merged reply (3ea intro + "Updating
  the tally…" + "Receipt secured — 2820 bytes…" + a300's full batch-6 table
  Q51–60, pattern notes, Q52 homework, batch-7 questions; 5201 chars);
  metadata = a300's metadata (carries the real `tool_events` write_file event)
  with 3ea's `timestamp`/`_db_id`/`thinking`, `stopped` removed,
  `round_texts` split into the two rounds. No `edited` flag — looks untouched.
- Rows `5eb9dad3-…` (user) and `a300b0d9-…` (assistant) deleted via
  `POST /api/session/{sid}/delete-messages` (DB + in-memory + message_count).
- In-memory hydration forced by inserting a throwaway row directly in the DB
  (stored count 22 > cached 21 → `get_session` re-hydrates from DB on next
  access via `GET /api/session/{sid}/context`), then the throwaway row was
  deleted through the same delete-messages call. `sanitize_client_message_metadata`
  strips `tool_events` from client-supplied metadata (server-owned key), which
  is why the metadata write had to go direct-to-DB.
- Backup before surgery: `/tmp/iris-surgery-backup/app.db{,-wal,-shm}`.

**Verified:** DB now 19 rows (was 21), FTS 19, `sessions.message_count`=19;
`GET /api/session/{sid}/context` reports messages=19 (was 22 pre-delete);
`replay_tool_events_as_native()` over the DB history augments 8 assistant turns
and renders the merged `3ea3ee07` as assistant(tool_calls=[write_file
bdsmtest_answers.md]) + role=tool "Wrote 2820 bytes…" — identical shape to the
session's other legitimate tool turns, so future requests see the tool call as
having really run. Root cause of the original poison (confirmed by user):
the model narrated a performed tool action in prose ("Updating the tally,
then your Q52 homework~") WITHOUT emitting a tool call; the user hit stop on
noticing, which closed the SSE generator mid-stream (GeneratorExit) — so the
post-loop guard at `agent_loop.py:6846` (`_tool_claims_unverified`) never ran,
and the stop path (`routes/chat_routes.py:288`, `stopped: True` + partial_sink)
persisted the partial with 0 `tool_events` and NO flag. `replay_tool_events_as_native`
had nothing to replay, so the false claim stood in context unchallenged. The
guard only fired later on the completed no-tool turn `42303066-…` (flag + ⚠
note appended to its content — left in place, see session) because
`_recent_user_request_is_effectful` + `_looks_like_tool_claim_narration`
(≥2 strong action verbs) matched with 0 `tool_events`. Gap noted, not fixed:
stopped turns skip the tool-claim guard entirely — running the same check in
the stop/partial-persist path would flag these at stop time.

## 2026-10-31 (22:45) — fix(agent): tool-hallucination guard no longer false-flags turns where tools ran (`not tool_events` enforced in `_narrates_unrun_tools`)

**User need:** the tool-verification guard (`_tool_claims_unverified`) fired on
turns where tools DID execute. In forked session `79fe8eec-…`, message
`3b888681-…` ran `read_file` (tool_events=1) yet was flagged and got the ⚠ note
appended to its saved content: the in-loop `_intent_without_action` branch
(`_narrates_unrun_tools`) never checked `tool_events` — the final round's text
carried ≥2 distinct strong verbs ("makeup **running** by tears" + "updated"/
"applied"/"closed"/"ran") and a recent user message was effectful, while the
wrap-up exemption failed because `_looks_like_conclusion` only scans head/tail
250 chars and "Fire away~" is not in `_CONCLUSION_RE`. DB-wide: 8 of 104
flagged turns had tool_events (one with 131 bash events).

**Change:** `src/agent_loop.py` only — `_narrates_unrun_tools` now starts with
`not tool_events`, matching its own comment ("ZERO tools run this turn") and
the post-loop guard's existing `not tool_events` condition. Narration can only
count as "unrun tools" when zero tools ran this turn. Comment updated with the
2026-10-31 note. No behavior change for 0-tool turns (the real
hallucinated-work-log case).

**Verified:** `python3 -m py_compile src/agent_loop.py` clean; `import
src.agent_loop` clean. Functional replay of the guard predicates against the
real session rows from `data/app.db`: `3b888681` (tool_events=[read_file]) →
`narrates_unrun=False` → guard does NOT fire (was True pre-patch);
`42303066` (0 tools + ≥2 strong verbs + effectful user msg) → `narrates_unrun=True`
→ guard still fires. Live effect on next server restart (assistant does not
restart the server per user rule).

## 2026-10-31 (22:54) — data surgery (no code change): scrub false guard ⚠ note from tool-running message in forked session 79fe8eec (data/app.db)

**User need:** after the 22:45 guard fix, scrub the tool-verification guard's
⚠ note + `tool_claims_unverified` flag from the "proper working tool messages"
in forked chat `79fe8eec-…` — flagged turns where tools actually executed. In
this session only `3b888681-…` qualified (read_file ran, tool_events=1, but the
final round's text tripped `_TOOL_CLAIM_STRONG_RE` via "makeup running by
tears" + "updated"/"applied"/"closed"/"ran" → false flag + note baked into
content).

**Change:** `data/app.db` `chat_messages` only (direct SQLite; FTS triggers
kept `chat_messages_fts` in sync): `3b888681-…` content stripped of the
appended "\n\n---\n⚠ Described tool actions did not execute …" note
(round_texts checked too — clean), `tool_claims_unverified` removed from
metadata; `tool_events` left intact. In-memory hydration forced via a
throwaway row (stored > cached → `get_session` → `_load_session_from_db`),
throwaway deleted via `POST /api/session/{sid}/delete-messages`. Backup:
`/tmp/iris-surgery-backup2/app.db{,-wal,-shm}`. Left in place deliberately:
`42303066-…` and `9556b515-…` still carry flag+note (0 tool_events — the note
is factually accurate there). DB-wide, 7 other false-flagged tool-running
messages exist in 5 other sessions (3770f309/5359ef01, c0d7eb13/393340b5,
a0e4e6f6/96c284e2+2031e69a+4d67ee2e, 315f71d7/c66cfcfd+09aaad72) — not touched
(other live sessions).

**Verified:** DB: 23 rows; `3b888681` flag=None, note=False, events=1, content
ends "Fire away~"; dummy rows 0; FTS in sync. App: `GET
/api/session/{sid}/context` hydrated in-memory from DB (cached 21 < stored 23
→ reload; export via `get_session` reflects the scrubbed row).
`42303066`/`9556b515` unchanged (flag=True, note present, events=0).

## 2026-11-01 (08:31) — data surgery (no code change): fix NVIDIA 400s in session 5d36643b (data/app.db) — archive empty stopped assistant rows

**User need:** chat `5d36643b-2d7b-47a1-9f3f-8ddbbb9c47a1`
(mistralai/mistral-large-4-1t-a52b @ integrate.api.nvidia.com) returned HTTP
400 "Invalid request" on every send (app.log 2026-11-01 07:07–07:18 local,
prompt_tokens 129k–244k). User suspected backend-garbled history.

**Root cause (verified by live probes against NIM):** 5 stopped assistant rows
with EMPTY content (`content=""`, no tool_calls) were non-archived, so the
request contained `{"role":"assistant","content":""}`. Minimal probe with an
empty-content assistant → 400 "Invalid request"; control, valid tool-call, and
duplicate-tool_call-id payloads → 200. `_sanitize_llm_messages` keeps them
because `content=""` is not None. (A regenerate pair 9ce9bdec/c35ac567 also
produced duplicate tool_call ids after native replay — probe showed NIM
accepts those; left in place.)

**Change:** `data/app.db` `chat_messages` only: set `archived=true`
(+`archived_at`, `archived_by='iris-surgery'`) on the 5 empty stopped rows
(addb4b82-…, 7d02cf74-…, 850dcfe6-…, beeb92dd-…, 1f1dded5-…). Rows stay on
disk and in the UI; the existing archived filter excludes them from model
context. In-memory hydration forced via throwaway rows (stored>cached →
get_session → _load_session_from_db); dummies deleted via
POST /api/session/{sid}/delete-messages. Backup:
/tmp/iris-surgery-backup3/app.db{,-wal,-shm}.

**Verified:** DB 73 rows, 0 dummies, 57 archived, 0 non-archived empty
assistants, FTS in sync; context endpoint messages 21→16, used_tokens
98901→80686; rebuilt request payload (preface + context + native replay +
sanitize + system consolidation + tail inserts) = 33 messages, zero empty
assistants, tool calls/results correctly paired; live probe of the full
rebuilt payload (real IRIS system prompt + 78 tool schemas) to
integrate.api.nvidia.com → HTTP 200, prompt_tokens=103169. Code-level
hardening NOT applied (option): drop empty-content assistant messages in
`_sanitize_llm_messages` so stopped empty turns never reach the API.

## 2026-11-01 (02:20) — fix(core): AttributeError in get_context_messages on multimodal (list) content

**Bug (user-reported traceback):** `msg.content.startswith(_HANDSHAKE_PREFIXES)`
in `core/models.py::get_context_messages` raised
`AttributeError: 'list' object has no attribute 'startswith'`.
`ChatMessage.content` is a LIST of content blocks for multimodal user messages
(image/audio attachments) — `_parse_msg_content` (session_manager.py:81)
deserializes JSON arrays back to lists. The handshake-prefix filter added
2026-10-31 assumed str content. (User had commented the line out to keep the
server running; this restores the filter safely.)

**Fix:**
- `core/models.py::get_context_messages`: handshake filter now guarded with
  `isinstance(msg.content, str)` — list content passes through untouched.
- `core/session_manager.py::append_to_last_assistant`: same guard — if the
  last assistant message's content is not a str (multimodal), return None so
  the caller falls back to a normal add instead of crashing on concatenation.

**Verified:** py_compile clean; harness with history [handshake user row,
user row with list content (image blocks), normal user, assistant] →
get_context_messages() returns without error, excludes the handshake row,
keeps the multimodal row. Frontend sessions.js already handles list content
(extracts text parts) — no JS change needed.

---

## 2026-11-01 12:30 — feat: DYNAMIC per-model thinking control on NIM (off value + levels per model, live-verified) (IRIS)

**Problem:** Thinking=Off was hardcoded to `reasoning_effort: "low"` for all
NIM models. Live probing (2026-11-01, integrate.api.nvidia.com, trivial AND
hard prompts, acceptance=HTTP 200, off=0 reasoning_content chars) showed the
correct off value is MODEL-SPECIFIC:
- nemotron (any version, incl. 3.5-super-vl-120b-a12b, 3-ultra-550b-a55b,
  3-nano-omni-30b-a3b-reasoning): accepts none/minimal/low/medium/high/
  xhigh/max; **OFF = "none"** (0 reasoning; low+ still think 260-419).
- glm-5.x: accepts none/minimal/low/medium/high/max but none/minimal do NOT
  suppress (thinks MORE, 493-909); **OFF = "low"** (0 reasoning).
- minimax-m3.1-flash: accepts all values; none/minimal don't suppress
  (330-430); **OFF = "low"** best effort (158) — cannot be fully silenced.
- mistral-large-4-1t-a52b: accepts ONLY low/medium/high (400 on
  none/minimal/xhigh/max); nothing suppresses fully; **OFF = "low"** best
  effort. (mistral-large 404s for this account — not deployed.)
- deepseek-v4.1-flash: skipped (nearly always 5min timeouts, per Sir).
- unknown NIM models: OFF = "low" (accepted by every model tested).

**Changes:**
- `src/llm_core.py`: `_NIM_REASONING_OFF` / `_NIM_REASONING_LEVELS` tables +
  `nim_reasoning_off_value()`, `nim_reasoning_levels()`, `_nim_clamp_level()`,
  `_nim_model_family()`. `_apply_thinking_off_openai_compat` nvidia branch now
  sends the per-model off value (+ chat_template_kwargs, harmless on NIM,
  still the switch for self-hosted vLLM). `_apply_request_reasoning_effort`
  nvidia branch clamps via `_nim_clamp_level` so NIM never 400s (e.g.
  mistral max/xhigh -> high). `REASONING_OVERRIDE_LEVELS` += "xhigh".
- `routes/chat_routes.py`: new `GET /api/chat/reasoning-control?model=&url=`
  returns {provider, levels, off_value, off_supported} per model — drives the
  dynamic dropdown.
- `static/js/chat.js`: menu items are now REBUILT from the endpoint response
  (Default / Off / <model's accepted levels>, incl. xhigh where supported);
  a stored level the current model doesn't support is clamped in
  localStorage (same order logic as backend) so the label never lies.
  `refreshThinkingControl()` (250ms debounce) called on init, on session
  open (sessions.js hook), and on model-picker updates (modelPicker.js hook).
- `tests/test_nim_reasoning_control.py`: 6 tests — off value per family,
  levels per family, clamp (no 400s), normalize xhigh, off payload per model,
  level payload per model.

**Verified:** 6/6 new tests + 26/26 llm_core-adjacent tests pass; 69/69
guard suites still pass; py_compile + node --check clean; 14-case end-to-end
payload matrix through the real helpers all correct (nemotron off->none,
glm off->low, mistral off->low, mistral max/xhigh->high, nemotron
max/xhigh verbatim, default->no field).

**Deploy:** backend change — live on next server restart (not forced).
Frontend is static (fresh on reload). Local/self-hosted models (e.g.
Qwen3.6 35B A3B on LM Studio) keep the chat_template_kwargs on/off switch —
Qwen-style templates only have On/Off, which the self-hosted branch handles.

## 2026-11-01 (09:55) — refactor(vision): grid overlay REMOVED from vision preprocessing (IRIS, at Sir's order — "gone, not disabled")
- `src/vision_preprocessing.py`: deleted `draw_grid_overlay()`, `_load_font()`, all `_GRID_*` / `_CELL_NAMES` / `_FONT_CANDIDATES` constants, the `vision_grid_overlay_enabled` setting read, the grid branch in `preprocess_image_for_vlm()`, and the `g` param from the cache key. Kept: upscale-to-floor (MIN_SHORTEST_SIDE=1024, MAX_LONG_SIDE=2048 cap), JPEG-q92 / alpha-PNG encode with MAX_PAYLOAD_BYTES cap, content-hash cache under `<upload_dir>/.vision/prepped/`. Docstring updated.
- `src/document_processor.py`: untouched — the `build_user_content` hook only calls `preprocess_image_for_vlm()` and already falls back to raw bytes on any exception, so image sending cannot break.
- No settings/UI cleanup needed: `vision_grid_overlay_enabled` was never persisted in `data/settings.json` (code default only) and had no references in `static/`/`templates/`. Remaining knob: `vision_upscale_enabled` (default True, code-default only).
- Cache: `data/uploads/.vision/prepped/` wiped (10 stale `g1`-keyed gridded entries + `.mime` sidecars); old keys unreachable after the key change regardless.

**Verified:** py_compile clean on both files; probe (`Sandbox/vision_probe_post_ripout.py`): 480×320 → 1536×1024 JPEG with ZERO amber grid pixels, cache key `..._u1f1024m2048q92.img`; 2600×1500 → byte-identical passthrough; text file → passthrough; RGBA PNG 800×600 → 1365×1024 RGBA PNG (alpha preserved); cache hit on repeat; upscale-toggle-off → passthrough. `grep` confirms no `draw_grid`/`vision_grid` refs anywhere in src/routes/static/templates/tests.

**Deploy:** backend change — live on next server restart (Sir restarts; IRIS never touches the Odysseus process). Until then the running process still has the old code in memory; the hook's try/except means nothing breaks either way.

## 2026-11-01 — context-packing tweaks (branch `iris-ctx-packing-tweaks`)
- `src/tool_utils.py`: `_truncate()` now keeps head+tail with an explicit middle-elision marker (was head-only, which dropped the tail of long logs — usually where the error lives). New `truncate_tool_output()` writes the full over-limit output once to `data/tool_output_cache/<sha1>.txt` (DATA_DIR is a default tool-path root, so read_file can page it) and appends a "saved to <path> — page with read_file offset/limit instead of re-running" note.
- `src/agent_loop.py`: all 8 tool-output sites (2 approval events + 6 round-loop result branches) now call `truncate_tool_output(..., tool_name=...)`. `_tool_schemas_for_route()` slims the `tools=` payload for API models via `slim_tool_schemas()` behind new setting `agent_slim_tool_schemas` (default true; lazy import inside the function to avoid the tool_schemas<->agent_tools circular import at module load).
- `src/tool_schemas.py`: new `slim_tool_schema()`/`slim_tool_schemas()` — deep-copies each schema, cuts the top-level description to its first sentence (max 240 chars), recursively cuts nested descriptions to first sentence (max 120 chars) and drops `examples`/`example` keys; keeps names/types/enums/required/default. Measured: 78 schemas 58.9KB -> 45.7KB JSON per agent round.
- `src/prompt_security.py`: per-message untrusted wrapper now uses a short self-contained header (`UNTRUSTED_CONTEXT_HEADER_SHORT`, ~100 chars) instead of the full ~340-char header repeated on every injection; the full policy stays once as a system message. Guard markers + `_escape_guard_markers` unchanged.
- `src/chat_processor.py`: `_hybrid_retrieve()` caches per-memory token sets on the ChatProcessor (`_mem_token_cache`, keyed by id + hash(text), pruned when >4x corpus size) so the per-turn BM25 pass no longer re-tokenizes the whole memory corpus every message.
- **Verified:** py_compile clean on all 5 files; `import src.agent_loop` clean in a fresh interpreter; functional probes: head+tail truncation keeps both ends + file persistence round-trips byte-identical, untrusted wrapper still escapes embedded guard markers, slim schemas preserve full structure (only prose cut).

## 2026-11-01 — Continue separator (synthetic tool pair, agent mode)
- Problem: on Continue after a mid-stream error (502/504), the stopped assistant row sits at the tail of the outgoing context. If it has no replayed `tool_events`, the resumed generation follows it directly — two adjacent assistant messages, which `_sanitize_llm_messages` does not merge (it only merges consecutive user messages) and which confuse models / some providers reject. Chat mode was already fine (prefill continues the trailing assistant message).
- `src/tool_replay.py`: new `inject_continue_separator(messages, is_api_model)` + `CONTINUE_SEPARATOR_TOOL`/`CONTINUE_SEPARATOR_OUTPUT`. API models: attaches a synthetic `odysseus_continue` tool_call to a COPY of the trailing assistant message (history row never mutated), or appends a fresh assistant message if the tail isn't assistant, then the matching `role=tool` result — pair stays adjacent so the sanitizer sees an answered call. Fenced/local models: plain user note instead (no native tool role). The tool name is deliberately absent from `FUNCTION_TOOL_SCHEMAS`, so the model can never call it — it only ever appears as injected history. Request-only; nothing persisted.
- `routes/chat_helpers.py` (`build_chat_context`): injects the separator at the very end of the outgoing messages (after compaction/trim, so it can't be dropped) when `continue_assistant and agent_mode`. Chat-mode Continue keeps prefill behavior.
- Output text tells the model the call is auto-generated by Odysseus for Continue, that the message above is a partial reply to resume, and not to re-run tools whose results are already present.
- **Verified:** py_compile clean; functional tests through the real `_sanitize_llm_messages`: tail-assistant case produces `system,user,assistant,tool` with the synthetic call answered and metadata stripped; tail-tool case produces valid `user,assistant,tool,assistant,tool`; fenced case `user,assistant,user`; empty list no-op; original history row not mutated; no collision with real tool schemas.

## 2026-11-01 — Continue separator persisted in DB + MCP block slimmed for native-tool models
- **Persisted, not frontend-only:** on agent-mode Continue, `routes/chat_routes.py::_persist_continue_separator` appends a synthetic `odysseus_continue` tool event to the stopped assistant row's `metadata.tool_events` (via `append_to_last_assistant`, DB + in-memory, idempotent). The frontend renders it through the *existing* tool_events path (`agent-thread-node` in chatRenderer.js) — zero new UI code — and `replay_tool_events_as_native` turns it into a native tool pair on every subsequent request, so the stopped row is never glued to the resumed generation in the model context either. Event shape: `src/tool_replay.py::build_continue_separator_event` (tool/command/output/exit_code/round/synthetic; command is a JSON dict so replay passes it through as arguments).
- The request-only `inject_continue_separator` in `build_chat_context` stays as a fallback for legacy stopped rows, now with a dedup guard (skips if an `odysseus_continue` call is already present post-replay).
- **MCP slimming:** in `_build_system_prompt`, when `compact` (native tool calling: API / native Ollama), the full MCP arg docs are written to `data/MCP-TOOLS.md` (DATA_DIR is a default tool-path root, so read_file can page it) and only a one-line pointer is injected as the untrusted "MCP tools" message instead of the full ~2-4k-token block. Fenced/local models (compact=False) keep the full text block since they have no native schemas. Write failure falls back to the full block.
- **Verified:** py_compile clean on all touched files; replay of a persisted event yields `user,assistant,tool,tool` with the separator call answered (args `{"note": ...}`) and survives `_sanitize_llm_messages`; dedup prevents double injection; legacy fallback still injects; agent_loop parses with the MCP gating present.

## 2026-11-01 — Continue separator renders live (no refresh needed)
- Problem: the persisted `odysseus_continue` event only appeared after a page refresh, because the already-rendered stopped bubble was never re-rendered when Continue was clicked — live, the resumed reply looked like a bare bubble glued to the stopped one.
- Fix: in the agent-mode stream branch of `routes/chat_routes.py`, when `continue_assistant` is set, yield synthetic `tool_start` + `tool_output` SSE events for `odysseus_continue` immediately before `stream_agent_loop` starts. The frontend's existing handlers (chat.js tool_start → creates the `agent-thread-node`, tool_output → ✓/done + output details) render it through the exact same path as real tools. The post-stream canonical reload then re-renders it from the persisted DB row (live nodes are discarded on reload, so no duplicates).
- **Verified:** py_compile clean; SSE payloads validated against the frontend handler shapes (`tool`, `command`, `output`, `exit_code`, `round` fields all present).

## 2026-11-01 — Static call-graph & architecture docs added (docs/ARCHITECTURE.md + docs/call-graph/)
- Added `docs/ARCHITECTURE.md`: repo size/composition, entry points (launcher.py → uvicorn, app.py router registration, static/app.js orchestrator), directory map, key end-to-end flows (chat stream, upload/vision, memory/RAG), conventions (setup_*_routes factories, exception handlers, auth, sw.js cache tokens, *.bak* scratch files are not live code).
- Added `docs/call-graph/` (427 generated markdown files, ~4 MB): per-module def→call-site maps (`py/`, `js/`), `http-endpoints.md` (all 508 FastAPI routes ↔ 1,327 JS API-URL literals), `module-deps-python.md` / `module-deps-js.md` (import edges + reverse dependents — "if I change X, who imports it"), `dead-code.md` (172 defs with zero static callers, verify before deleting), `external-calls.md`, `INDEX.md` (stats + top hubs), `README.md` (scope, caveats, regeneration).
- Generated by `Sandbox/trace_odysseus.py` (AST for py, regex for js → `Sandbox/odysseus-trace.json`) + `Sandbox/gen_docs.py` (renders the markdown). Regenerate with those two scripts after big refactors. No runtime code touched; docs only.

## 2026-11-01 — DB keeps everything + frontend parity with DB (nothing dropped, nothing hidden)
- **Tool-only stopped turns now persist (was the big drop):** `routes/chat_routes.py::_persist_stream_partial` used to return early when no reply text AND no reasoning had streamed — so a turn stopped right after a tool executed (Assistant → Tool → [stopped]) saved *nothing*, losing the executed tool calls from the DB. Now it persists whenever `tool_events`/`round_texts` are present, saving an empty-content assistant row whose `metadata.tool_events` carries the calls (frontend multi-bubble path renders the tool thread even with empty text). The two agent-mode disconnect/error guards in `chat_routes.py` (CancelledError + upstream-error branches) now hoist `_sink_tool_state` before the guard and also fire when only tool events exist.
- **No user-role directly after tool-role in request payloads:** `src/llm_core.py::_sanitize_llm_messages` now appends a filler assistant message (`_TOOL_BATCH_ACK = "..."`, request-only, never persisted) after a tool-result batch when the next message is user/system or the batch ends the list — strict endpoints that reject user-after-tool no longer 400. DB keeps the stopped turn exactly as it happened; the filler only shapes the outgoing payload.
- **Frontend parity:** `static/js/sessions.js` history pager ("load earlier") and archived-session peek no longer filter to `role === user/assistant` — every row the DB returns is rendered, so paged loads and peeks match the main history path. ("Copy Chat" keeps its user/assistant filter deliberately — it's an export, not rendering.)
- **Thinking never visually truncated:** `static/style.css` `.thinking-content.expanded` went from `max-height: 300px; overflow-y: auto` to `max-height: none; overflow: visible` — expanding the thinking section shows the full reasoning, no scroll cap. (JS already rendered full `metadata.thinking`; no slicing anywhere.)
- **Verified:** py_compile clean on touched py files; `node --check` clean on sessions.js; unit checks: sanitizer yields `user,assistant,tool,assistant(filler),user` for tool→user, no filler for tool→assistant or tool-at-end, unchanged for tool-free lists; `_persist_stream_partial` mock tests: tool-only partial persists with `stopped:True` + `tool_events`, empty turn still skipped, text+thinking partial unchanged. Call-graph docs regenerated (`Sandbox/trace_odysseus.py` + `Sandbox/gen_docs.py`).

## 2026-11-01 — Temporal grounding stamps in the LLM-bound transcript
- **Every user/assistant message in the request payload now carries a `[HH:MM:SS]` prefix** (user-local clock, from persisted `metadata.timestamp`; "now" for live messages). Applied in `routes/chat_helpers.py::build_chat_context` via the new `src/user_time.py::stamp_context_messages`, AFTER compaction/trimming and on copies — persisted history is never written back stamped, and stamps derive from stored timestamps so the history prefix stays byte-stable across turns (local KV-cache prefixes survive). System messages, untrusted-guarded context blocks (`metadata.trusted is False` — guard header must stay ahead of `GUARD_OPEN`), and non-string (vision) content are skipped. Idempotent: already-stamped content passes through.
- **Tool calls show elapsed time as `[HH:MM:SS | 621ms]`.** `src/agent_loop.py` now times every tool execution (normal + approved paths) and stores `ts`/`duration_ms` on `tool_event` and `tool_result_records`; within-turn results are stamped in `_append_tool_results` (native role=tool content, fenced output stamped *inside* the untrusted guard, within-turn assistant turns get a clock stamp). Cross-turn replay is stamped in `src/tool_replay.py` (`_format_event`, native replay results) and `_build_actions_snapshot`.
- **UI:** reload-path tool cards (`static/js/chatRenderer.js`) show the elapsed duration next to the tool name (`.agent-thread-dur` in `style.css`); live cards already showed elapsed. Message bubbles already rendered per-message timestamps.
- **Helpers** in `src/user_time.py`: `parse_message_timestamp`, `clock_stamp`, `message_stamp`, `format_duration_ms`, `tool_event_stamp`, `stamp_context_messages`.
- **Tests:** new `tests/test_temporal_grounding_stamps.py`; updated `test_agent_loop.py`, `test_approved_replay_message_shape.py`, `test_native_tool_result_threading.py`, `test_review_regressions.py` to strip the stamp before comparing. Full suite: 6044 passed; the 49 remaining failures are pre-existing on this branch (no stamp markers in any traceback). Call-graph docs regenerated (`Sandbox/trace_odysseus.py` + `Sandbox/gen_docs.py`).

## 2026-11-01 — Thinking boxes survive refresh (guard fix + placement); expanded cap restored
- **Root cause of missing thinking boxes after refresh:** the multi-bubble reload path in `static/js/chatRenderer.js` guarded the `metadata.thinking` prepend with `roundTexts.some(t => t.includes('<think>'))` — a *substring* check. Any round whose reply merely mentioned `<think>` in prose (backticks, model discussing tags) tripped it, the stored reasoning was never prepended, and since round_texts are saved tag-stripped, **no thinking box rendered at all** (46 rows in the live DB hit this). The guard now uses `extractThinkingBlocks(...).thinkingBlocks.length` — real parsed blocks only — so prose mentions no longer suppress the box, and genuine inline blocks still skip the prepend (no double render).
- **Box placement:** the prepend now targets the first round that actually has text (fallback round 0) instead of always round 0 — previously a tool-only first round produced a detached empty bubble carrying the box while the text bubble below had none (the screenshot case). Tool-only turns still get a box-only bubble.
- **Single-bubble double-render fix:** 21 rows have both `metadata.thinking` and a real inline block in content (legacy double-store) — the reload path now strips inline blocks from the *display* text (`dataset.raw` keeps the original) before prepending, so the box renders once.
- **Expanded thinking cap restored:** `.thinking-content.expanded` is back to `max-height: 300px; overflow-y: auto` per Sir — display cap only, full reasoning stays in the DOM and scrollable, collapse hides it. (Reverts the `max-height: none` from the earlier entry today.)
- **Verified:** `node --check` clean; DB-wide simulation of old vs new guard: multi-bubble rows with `metadata.thinking` that render the box went 1824 → 1859 (the ~35 prose-mention rows fixed; rows with real inline blocks still correctly skip the prepend). Call-graph docs regenerated.

## 2026-11-01 (rework) — Temporal grounding as structured payload fields, NOT content prefixes
- **Why the rework:** the first version prefixed `[HH:MM:SS]` into message content of the LLM-bound request. The model mimicked the prefix into its own replies, so stamps landed in persisted `chat_messages.content` and showed up in chat bubbles (screenshot regression). Content is now never stamped anywhere.
- **DB:** no migration needed — `chat_messages.timestamp` already is the per-row column (surfaced as `metadata.timestamp`). Tool executions record `ts`/`duration_ms` inside the same row's `metadata.tool_events` (agent_loop times every execution, normal + approved paths).
- **LLM payload boundary:** `llm_core._sanitize_llm_messages` (the single funnel for OpenAI-compatible + Ollama payloads; the Anthropic builder drops unknown keys so Claude never sees them) now injects a structured `"timestamp"` field on every user/assistant/tool message (from `metadata.timestamp`/`metadata.ts`; live tail messages without a stored ts fall back to now) and `"duration_ms"` on tool messages. System messages are skipped so the KV-cache prefix stays byte-stable; history derives the field from the stored column, so the prefix is byte-identical across turns. Within-turn messages carry the data in `metadata` (`_append_tool_results`, `tool_replay.replay_tool_events_as_native`) — request-only, never persisted.
- **UI:** unchanged from before the feature (the temporary tool-card duration label was reverted); bubble corner timestamps are the pre-existing `metadata.timestamp` display.
- **Removed:** `stamp_context_messages`/`clock_stamp`/`tool_event_stamp` content-stamping helpers from `src/user_time.py` (kept `parse_message_timestamp` + new `now_iso`); content-stamp call in `chat_helpers.build_chat_context`.
- **Tests:** `tests/test_temporal_grounding_stamps.py` rewritten for field injection (content-clean, system-skipped, byte-stable, tool duration_ms, replay metadata); `test_llm_core_sanitize_tool_calls.py` exact-shape assertions updated for the new field; 4 suites restored to pre-feature state. Full suite: 6039 passed; the 51 remaining failures are pre-existing on this branch (none in touched files). Call-graph docs regenerated.

## 2026-11-01 (addendum) — Synthetic per-round datetime tool call in agent mode
- **Why:** agent mode injects the `[Context — current date/time]` message once per *request*, so during long multi-round tool loops the model's clock goes stale. Now every tool batch also gets a synthetic `get_current_datetime` tool call + result appended to the request messages (`agent_loop._append_tool_results`, native path: extra entry in the assistant `tool_calls` + matching role=tool result; fenced path: a plain `Current date/time: ...` line inside the untrusted tool-output block). The result text is a natural sentence, not a `[HH:MM:SS]` prefix, so it can't be mimicked into replies the way the old content stamps were (confirmed: a model-generated stamp ran a full minute ahead of the real send time).
- **Request-only:** the synthetic pair is never persisted to `metadata.tool_events`, never replayed cross-turn, never rendered as a tool card. The dispatcher (`tool_execution.execute_tool_block`) answers a model-mimicked `get_current_datetime` call with the real current time instead of "Unknown tool".
- **Gemini guard:** `_inject_datetime_tool_call()` skips injection for Gemini 3 (its endpoint 400s on assistant tool_calls lacking the thought_signature it returned; server-injected calls have none). Uses the new `get_active_model()` getter in `agent_tools/document_tools.py`.
- **Helpers:** `user_time.DATETIME_TOOL_NAME` + `user_time.current_datetime_line()` (user-local one-liner with UTC). The synthetic result also carries `metadata.ts`, so the payload boundary adds its `timestamp` field like any other tool message.
- **Kept from the previous commit:** structured `timestamp`/`duration_ms` payload fields at `_sanitize_llm_messages` — content is still never stamped.
- **Tests:** 4 new tests in `test_temporal_grounding_stamps.py` (synthetic call+result shape, sanitize survival, fenced line inside guard, dispatcher answer); `test_external_context_tool_gate.py` + `test_native_tool_result_threading.py` updated to skip `call_dt_*` synthetic messages. Full suite: 6043 passed, 51 failed + 3 errors — all pre-existing on this branch. Call-graph docs regenerated.
