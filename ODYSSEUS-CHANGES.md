# Odysseus Change Log — main tree

> Changelog for the **main Odysseus tree** (`/run/media/crao/BTnvme/LLM/odysseus`, served on 127.0.0.1:7001).
> Format follows the `.old` fork's `ODYSSEUS-CHANGES.md` house style.
> Standing rule: every change made to files under `odysseus/` gets appended here, dated.

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
