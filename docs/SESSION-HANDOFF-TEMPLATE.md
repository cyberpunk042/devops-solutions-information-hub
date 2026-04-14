# Session Handoff — YYYY-MM-DD

> **Purpose:** Context recovery document. Read this to resume work.
> **NOT a wiki page.** Lives in docs/, not wiki/. Do not ingest.
>
> **Standard:** [[session-handoff-standards|Session Handoff Standards]] (wiki/spine/standards/session-handoff-standards.md)

<!--
  INSTRUCTIONS: Replace this block and the YYYY-MM-DD above.

  Keep ALL invariant sections (below). DELETE this HTML comment when done.

  For EXTENDED sections (Session Context, Operator Voice, Architecture Decisions,
  Mistakes, Reflection, Key Files), the template includes commented-out stubs
  below the invariant sections. Uncomment only the ones this session warrants.

  Length rule: follows content, not prescription. 4KB is fine for a quiet
  session; 40KB is fine for a decision-heavy session. Do not pad. Do not
  truncate.

  Filename convention: SESSION-YYYY-MM-DD[-suffix].md where suffix is only
  used for within-day supersession (-part2, -final, -v2). Do NOT use
  "-handoff" suffix — SESSION-*.md is already unambiguous.
-->

---

## Executive Summary

<!--
  One-screen view. 3-5 sentences + metrics snapshot.

  Answer: What was the scope? What changed? What is the state?

  Metrics MUST come from fresh `python3 -m tools.pipeline status`.
  Estimated metrics are a lie.
-->

[Write 3-5 sentences summarizing the session outcome.]

**Final state (from `pipeline post` at session end):**

- Pages: N
- Relationships: N
- Validation errors: 0
- Lint issues: 0
- Raw files pending: N
- Commits this session: N

---

## What Was Done

<!--
  Choose ONE organizing structure based on session shape:

    Directive-driven  → ## Directive N: <title> with verbatim quotes
    Phase-driven      → ### Phase N — <name> with per-phase outputs
    Decision-driven   → Decisions table, before/after columns
    Focused fix       → Flat list of specific changes with file paths

  Every entry should cite file paths. Prose is worthless.
-->

[Structure the work log per the session shape above.]

---

## Current State

<!--
  Snapshot. Include:
    - Page count, relationship count, validation errors, lint issues
    - Git: current branch, ahead-of-main, uncommitted changes
    - Raw files pending ingestion
    - Open question delta (pages with [!question] callouts)
-->

[Paste fresh `pipeline status` and `git status --short` output.]

---

## What's Next

### Immediate Candidates

<!-- What the next session could pick up. Prioritized. -->

- [Candidate 1]
- [Candidate 2]

### What's Blocked

<!-- Items dependent on operator or external input. State the dependency. -->

- [Blocked item — waiting on X]

### Ready for Human Review

<!-- Items at 99% readiness/progress needing operator sign-off. -->

- [Review item — decision needed on Y]

---

## How to Resume

<!--
  NUMBERED CHECKLIST. Not narrative. Each step either reads a specific file
  or runs a specific command. A fresh agent follows this top-to-bottom.
-->

1. Read `CLAUDE.md` (auto-loaded)
2. Read `AGENTS.md` (auto-loaded)
3. Read this handoff
4. Read `wiki/backlog/operator-decision-queue.md` (see what's resolved vs open)
5. Run `python3 -m tools.pipeline post` — verify 0 errors / 0 lint
6. [Session-specific next step]

---

<!--
  ═══════════════════════════════════════════════════════════════════════
  EXTENDED SECTIONS — uncomment the ones this session warrants.
  ═══════════════════════════════════════════════════════════════════════


## Session Context and Trajectory

### Where We Started

[State at the beginning of the session.]

### The Arc

[The narrative shape of the session — 3-7 phases of what unfolded.]

### The Operator's Voice

> "verbatim quote 1"

> "verbatim quote 2"

<!- - Use VERBATIM quotes. Never paraphrase. The exact vocabulary is
     what future sessions will search for. - ->


## Architecture Decisions Made

| # | Decision | Before | After | Commit |
|---|----------|--------|-------|--------|
| Q## | [Decision title] | [Prior state] | [Resolved state] | commit_hash |


## Mistakes

<!- -
  Include ONLY if the session had mistakes. Omitting is dishonest.
  Each mistake: what happened, verbatim operator correction, what was learned.
- ->

### Mistake 1: [Title]

[What the agent did wrong.]

> "verbatim operator quote correcting it"

**Learned:** [What the agent/system now understands.]


## Reflection

### What Worked

- [Pattern that worked]

### What Could Improve

- [Pattern to avoid next time]


## Key Files and References

### Session-Produced (new)

- `path/to/new-file.md` — [role]

### Session-Modified

- `path/to/modified-file.md:42` — [what changed]

-->
