# Local Git Workflow — Crao's fork

> Local-only doc (2026-11-02), written after the "fricky-wicky incident": a
> destructive `git reset --hard` wiped a full day of uncommitted work.
> Read this before ANY git operation in this repo.

## Remotes — what each one IS

| remote | repo | role |
|---|---|---|
| `origin` | `git@github.com:AnimalTheGamer300/odysseus.git` | **Crao's fork — the public repo page. The ONLY remote we ever push to.** |
| `odysseus-dev` | `https://github.com/odysseus-dev/odysseus.git` | upstream project. **NEVER push.** |
| `pewdiepie-archdaemon` | `github.com/pewdiepie-archdaemon/odysseus.git` | **just a redirect to odysseus-dev** (same repo). Treat as upstream. **NEVER push.** |

The fork is a permanent divergent fork: it carries hardcoded features that
will never be offered upstream. Do not "help" by PRing anything to
odysseus-dev, and do not treat upstream as a merge target unless Sir
explicitly asks for a sync.

SSH auth to `origin` verified working 2026-11-02 (`git ls-remote origin`).
If it ever breaks: `ssh -T git@github.com` to diagnose; fallback is HTTPS +
a GitHub PAT via `git remote set-url origin https://github.com/...`.

## Branch layout

- `dev` — the fork's DEFAULT branch (the front page). It tracks upstream's
  dev (via the pewdiepie-archdaemon redirect) and is ~508 upstream commits
  ahead of the local working line — merging the working line into it is a
  REAL merge with likely conflicts, not a fast-forward. Only do it when Sir
  explicitly asks for a front-page update.
- `main` — tracks `origin/main`, roughly in sync (ahead 1 as of 2026-11-02).
- `iris-*`, `wip-snapshot-*`, `backup/*`, `pre-agent-turn-fixes-*` — local
  working/safety branches. These are the recovery points.

## The rules that keep work alive

1. **Snapshot after every completed unit of work.** Uncommitted changes die
   to any `git checkout` / `git reset --hard`:
   ```bash
   git add -A && git commit -m "wip: snapshot <date> — <what> (IRIS)"
   git branch wip-snapshot-<date>-<topic>   # optional bookmark
   ```
2. **ODYSSEUS-CHANGES.md is git-immune** — untracked + ignored via
   `.git/info/exclude` (commit `d101c70a`, 2026-11-02). Never `git add` it
   back. NEVER run `git clean -x` / `git clean -fdx` in the repo root —
   that deletes ignored files and is the one thing that can still kill the
   changelog.
3. **Never run destructive git commands** (`git checkout -- .`,
   `git reset --hard`, `git clean -fd`, branch switches that discard
   changes) on Sir's working tree without his explicit yes. `git stash`
   shelves; `git clean -fdn` dry-runs; `git branch backup/<name>` before
   big moves.
4. **Never push to `odysseus-dev` or `pewdiepie-archdaemon`.** Fork only.

## Publishing to the fork (what Sir's words mean)

- **"Push to the fork"** → push the current working branch as a branch:
  ```bash
  git push -u origin <branch>        # -u sets tracking on first push
  ```
  It then appears on github.com/AnimalTheGamer300/odysseus under branches.
- **"Put it on the fork's front page"** → the front page shows the default
  branch (`dev`). That requires merging the working line into `dev` and
  pushing:
  ```bash
  git checkout dev && git merge <branch> && git push origin dev
  ```
  WARNING: dev is ~508 upstream commits ahead of the working line — this is
  a real merge, expect conflicts. Do it only on Sir's explicit ask, and
  snapshot first.
- A plain branch push does NOT change the front page. Changing the default
  branch on GitHub (Settings → Branches) is Sir's call, not ours.

## After any destructive git op (recovery order)

1. `git reflog` — HEAD@{n} entries survive almost everything.
2. `git branch -a` — wip-snapshot-* / backup/* branches are recovery points.
3. `git stash list` — stashes survive resets.
4. `ODYSSEUS-CHANGES.md` (on disk, git-immune) documents what was done.
