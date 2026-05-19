Light session-state load for the research wiki / second brain.

> Slash-invoked. Operator types `/load-context` literally. Companion to
> `/load-brain` (permanent intelligence) — this loads SESSION-STATE:
> recent operator directives, recent session work, pending decisions,
> pipeline health, git state.

## Why this command exists

`/load-brain` covers the timeless brain (principles, models, standards,
engine). But the agent also needs SESSION awareness:
- What did the operator say recently? (raw/notes/)
- What landed in recent sessions? (wiki/log/)
- What's pending operator review? (operator-decision-queue.md)
- What's the project's current pulse? (pipeline status, git state)

`/load-context` delivers that quickly — ~10 ops, under a minute.

Pair pattern:
- `/load-brain` (heavy default) for intelligence
- `/load-context` (light default — this) for situational awareness
- Together: fully-warmed agent.

For comprehensive arc reconstruction (multi-day break, post-compaction with
heavy session loss): use `/load-context-deep` instead.

## Argument modes

| Invocation | Behavior |
|---|---|
| `/load-context` (no args) | Light default walk (~10 reads) |
| `/load-context <surface>` | Focus on one situational surface |
| `/load-context <s1> <s2> ...` | Union of multiple surfaces |

### Surface vocabulary

| Surface | Aliases | What it loads |
|---|---|---|
| `handoff` | | Most recent `wiki/log/2026-*handoff*.md` or most recent `wiki/log/` entry |
| `notes` | `directives` | Last 3 `raw/notes/2026-*.md` (operator-verbatim) |
| `log` | `sessions` | Last 2 `wiki/log/2026-*.md` |
| `queue` | `decisions`, `pending` | `wiki/backlog/operator-decision-queue.md` |
| `pipeline` | `status` | `.venv/bin/python -m tools.pipeline status` |
| `git` | | `git log --oneline -5` + `git status --short` |
| `backlog` | | `wiki/backlog/_index.md` + recent epics |
| `ingestion` | `raws` | List recent raws, check sources/ for unsynthesized |
| `sister` | `projects` | `wiki/config/sister-projects.yaml` |
| `mode` | | `.claude/active-mode` (if exists) |

## Discipline

- Read each file in full. Read command output in full. Pre-bash hook blocks
  reflexive truncation pipes — respect it.
- raw/notes/ files are SACROSANCT verbatim per AGENTS.md Hard Rule 3 — never
  paraphrase, quote operator words exactly.
- The output is a SESSION STATE report (format below), not a wiki page.
  Don't ingest the report anywhere.

## The Light Default Walk — ~10 ops

### 1. Recent operator directives (last 3 from raw/notes/)

```bash
ls -t raw/notes/2026-*.md
```

Then `Read` the 3 most recent. These are SACROSANCT primary sources.
Surface in report: file + 1-line summary + verbatim headline quote.

### 2. Recent session work (last 2 from wiki/log/)

```bash
ls -t wiki/log/2026-*.md
```

Then `Read` the 2 most recent. Surface: what was being worked on, what
landed, unresolved threads.

### 3. Operator decision queue

```
Read wiki/backlog/operator-decision-queue.md
```

Surface: pending Q-items requiring operator review (count + headlines).

### 4. Pipeline state

```bash
.venv/bin/python -m tools.pipeline status
```

Read full output. Surface: pages count, raws count, recent additions.

### 5. Git state

```bash
git log --oneline -5
git status --short
```

Surface: recent commits, uncommitted changes (count + summary).

### 6. Active mode (forward-compat)

```bash
cat .claude/active-mode 2>/dev/null || echo "(no mode active)"
```

## Then: apply surface args (if any)

For each surface argument the operator passed, perform the corresponding
load (deeper than the light default). Examples:

- `/load-context handoff` → identify the most recent file in `wiki/log/`
  matching `*handoff*` (or just the most recent log entry); read in full.
- `/load-context notes` → read last 7 (instead of 3) raw/notes/ files.
- `/load-context queue backlog` → operator decision queue + backlog _index +
  the 3 most recently updated epics.
- `/load-context ingestion` → list `raw/articles/`, `raw/transcripts/`,
  `raw/papers/`, `raw/notes/` recent additions; compare against
  `wiki/sources/` to find raws without synthesis pages.

### Resolution rules

- Surface names are case-insensitive
- `and` between surfaces is a separator
- Unknown surface → ask the operator to clarify, do NOT guess

## SESSION STATE report (the structured output)

After the walk, emit this report:

```markdown
# SESSION STATE — <DATE>

## Most recent operator directives (last 3 from raw/notes/)
| Date | File | Headline (verbatim quote, do NOT paraphrase) |
|---|---|---|
<rows>

## Recent session work (last 2 from wiki/log/)
<bullets — what landed, unresolved threads>

## Pending operator decisions
<count + Q-item headlines, or "(none)">

## Pipeline state
- Raw files: <count> (articles / transcripts / notes / papers / dumps)
- Wiki pages: <count>
- Validation errors: <count>
- Recent changes: <summary>

## Git state
- Recent commits: <5 oneline>
- Uncommitted: <count + brief summary, or "clean">

## Active mode
<from .claude/active-mode, or "(no mode active)">

## Active arc (synthesis — if obvious from the above)
<one-line trajectory description, OR "(arc unclear — multiple threads)">

## Status
Session context loaded. Ready for operator direction.
```

## Composition with other commands

| Command | Use when |
|---|---|
| `/load-brain` (full ~76) | Cold-start cold session; maximum mastery; once per major reset |
| `/load-brain-light` (~11) | Quick re-warm of the brain; low context budget |
| `/load-context` (this, ~10) | Session start; re-warm after a break |
| `/load-context-deep` (~30) | Multi-day break; full arc reconstruction; heavy post-compaction recovery |
| `/orient` | Predecessor; mixed identity + state (largely superseded by the load-brain / load-context split) |

Common combos:
- Cold start: `/load-brain` then `/load-context`
- Quick re-engagement: just `/load-context`
- Returning after days: `/load-brain-light` then `/load-context-deep`

## Mechanism

100% deterministic per operator 2026-04-24 doctrine. The walk IS the program.
Surface arguments are documented extension points.

## Cross-references

- [load-brain.md](load-brain.md) — permanent brain (full)
- [load-brain-light.md](load-brain-light.md) — permanent brain (light)
- [load-context-deep.md](load-context-deep.md) — session state (deep)
- AGENTS.md Hard Rule 3 — log operator directives verbatim BEFORE acting
