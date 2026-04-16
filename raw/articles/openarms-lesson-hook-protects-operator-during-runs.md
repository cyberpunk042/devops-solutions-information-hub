---
title: "The pre-write hook prevents operator-Claude from racing the running agent on backlog files"
type: lesson
domain: learnings
status: active
confidence: high
maturity: seed
created: 2026-04-15
updated: 2026-04-15
tags:
  [methodology, hooks, operator-claude, defense-in-depth, race-conditions, harness, multi-task-run]
related:
  - wiki/domains/learnings/lesson-five-claude-contexts.md
  - wiki/domains/learnings/lesson-epic-readiness-sparse-children.md
---

# The Pre-Write Hook Protects the Operator from Racing the Running Agent

## Summary

While a `pnpm openarms agent run` is in flight, the `scripts/methodology/hooks/pre-bash.sh` and `scripts/methodology/hooks/pre-write.sh` hooks block writes to task files, epic files, and `_index.md` from ANY context — including operator-Claude (Context A in `lesson-five-claude-contexts.md`). The block message is:

```
BLOCKED: Task/epic frontmatter is managed by the harness.
Use /stage-complete to advance stages and /task-done to complete tasks.
```

I'd been mentally treating operator-Claude as "free to edit anything during runs" because operator-Claude is a separate process from the running agent. The hook taught me otherwise: **the methodology enforcement layer correctly prevents race conditions between the two contexts.**

## Why this matters

The harness writes task frontmatter, epic frontmatter, `_index.md`, `task-history.json`, and other backlog files when stage transitions happen. If operator-Claude edits the same files concurrently, the harness's next write will overwrite operator-Claude's changes (or vice versa, depending on timing). Either way, one set of edits is lost silently. Worse, partial writes could leave the backlog in an internally inconsistent state.

Before discovering this hook protection, the workflow I'd been using was:

- Run an agent
- While it runs, pre-spec the next 2-3 tasks so they're queued for follow-up
- Update lesson files based on observations from the in-flight run
- Edit the index to add the new task entries

**Two of those four operations are unsafe.** The "pre-spec the next tasks" and "edit the index" both write backlog files. The hook correctly blocked them when I tried.

## Evidence (2026-04-14 evening, multi-task run `bwhmsotkr`)

While `pnpm openarms agent run --tasks 3 --filter E013` was running T118 → T119 → T120 in the background, I tried to:

1. Write `wiki/backlog/tasks/T121-wire-status-line-agent-watch-live.md` — **BLOCKED** by `pre-write.sh`
2. Edit `wiki/backlog/tasks/_index.md` to add T121 to the Active section — **BLOCKED** by `pre-write.sh`

Both with the same message: `BLOCKED: Task/epic frontmatter is managed by the harness.`

Lesson and learning files (`wiki/domains/learnings/`, `wiki/log/`) were NOT blocked — those are not under the hook's protection because they don't affect harness state.

## What is safe vs unsafe during an active run

| Surface                          | Safe to edit during active run? | Why                                                                                                         |
| -------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `wiki/backlog/tasks/T*.md`       | ❌ NO                           | Harness writes frontmatter on stage transitions                                                             |
| `wiki/backlog/tasks/_index.md`   | ❌ NO                           | Harness writes when tasks complete                                                                          |
| `wiki/backlog/epics/E*.md`       | ❌ NO                           | Harness writes epic readiness on recompute                                                                  |
| `.openarms/concerns.json`        | ❌ NO                           | Agent writes via `/concern` command                                                                         |
| `.openarms/task-history.json`    | ❌ NO                           | Harness writes on task completion                                                                           |
| `.openarms/state/*`              | ❌ NO                           | Harness owns this directory                                                                                 |
| `wiki/domains/learnings/*.md`    | ✅ YES                          | Lessons are operator territory                                                                              |
| `wiki/log/*.md` (handoff, notes) | ✅ YES                          | Logs are operator territory                                                                                 |
| `wiki/domains/architecture/*.md` | 🟡 MAYBE                        | If the running agent is ALSO writing here (research/design stage artifacts), there's a race; otherwise safe |
| `src/**/*.ts`                    | 🟡 MAYBE                        | If the running agent's current stage is implement/test, the agent will write src files; otherwise safe      |
| `scripts/methodology/*`          | ✅ YES                          | Methodology infrastructure is operator territory and rarely touched by the agent                            |
| `CLAUDE.md`, `AGENTS.md`         | ✅ YES                          | Static directive files; agent doesn't write them                                                            |

The rule of thumb: **anything the harness or agent might write during the active stage is unsafe for operator-Claude to touch.** When unsure, wait for the run to finish.

## The corrective workflow

When operator-Claude wants to make progress while a run is in flight, only do work that:

1. **Reads code/files** (no writes)
2. **Writes to `wiki/domains/learnings/`** (lesson files)
3. **Writes to `wiki/log/`** (notes, handoff drafts)
4. **Drafts the next task spec in a temporary file or scratch buffer** that won't be committed until the run completes

Specifically, do NOT:

- Edit `_index.md` (even to add notes)
- Edit any task file even if it looks orphaned
- Edit any epic file
- Run `select-task` and rely on the result for backlog state (the state changes mid-run)
- Run `git commit` against backlog files

After the run completes and the harness exits cleanly, all of these become safe again.

## Why the hook is correct

This is defense-in-depth working as designed. The methodology infrastructure (`E014` work) added these hooks specifically to prevent class-of-bug failures where operator and agent both edit the same files. Today's incident was the FIRST time I personally hit the protection, which means:

- Either I'd been getting lucky for many sessions of mixed operator + agent work (unlikely — I'd been editing during runs frequently)
- OR the hook only fires under specific conditions (e.g. when `methodology-enforced` flag is set, which the harness sets at dispatch time)
- OR I was hitting the protection before but not noticing because the failure mode was "silent revert by harness recompute"

The third possibility is the most concerning. **Some of my earlier session's "wait, did the harness overwrite my edit?" moments may have been the same failure mode without the protective hook firing.** The fact that the hook DID fire on 2026-04-14 evening suggests recent E014 work tightened the protection, and that's good.

## Connection to other lessons

- **`lesson-five-claude-contexts.md`** — the operator-Claude context (A) and the solo-agent context (B) are distinct and should not race on shared state. The hook enforces this at the file-write layer.
- **`lesson-epic-readiness-sparse-children.md`** — that lesson predicted "manual override is temporary, harness will overwrite." The hook lesson is the complementary observation: even before the harness gets to overwrite, the hook blocks the manual write in the first place.
- **`lesson-investigate-before-designing.md`** — the impulse "I'll just edit the index quickly" before checking what the running agent will touch is the same impulse as "I'll just design from my mental model" before grepping the codebase. Same family.

## Open questions

- **Does the hook also block the agent's own writes during certain stages?** I think yes (the document stage forbids src/ writes, the scaffold stage forbids business logic, etc.) — but I haven't traced the exact rules.
- **Is there a way to query "what surfaces are currently locked" without trying to write to them?** A `pnpm openarms harness status` or similar that reports "T118 is in scaffold stage, locked: cost-accumulator.ts, usage-collector.ts, \_index.md" would let operator-Claude plan edits more safely.
- **What's the exact mechanism that turns the protection on/off?** Is it the `.openarms/methodology-enforced` flag the harness writes at dispatch? If so, what clears it? Reading `pre-write.sh` would answer this.

These are non-blocking — flagging for future investigation when relevant.

## The distilled rule

**During an active `agent run`, operator-Claude reads but does not write to the backlog.** Lessons, logs, scratch notes, and code reading are fine. Anything in `wiki/backlog/` or `.openarms/` waits until the run completes.

When the next operator-Claude session starts during a multi-task run and wants to "make use of the wait time productively," route the productive work to lesson refinement, log writing, or architecture reading. Do not pre-spec next tasks or edit the index. The hook will catch you, but better not to need it.

## Relationships

- PRODUCED_BY: 2026-04-14 multi-task run `bwhmsotkr` (T118 + T119 + T120) — operator-Claude tried to write T121 spec mid-run and was blocked
- EVIDENCE: `scripts/methodology/hooks/pre-write.sh` (the blocking hook), `scripts/methodology/hooks/pre-bash.sh` (the bash-side equivalent)
- INFORMS: future operator-Claude workflow during active runs
- RELATES_TO: `wiki/domains/learnings/lesson-five-claude-contexts.md`
- RELATES_TO: `wiki/domains/learnings/lesson-epic-readiness-sparse-children.md`
- RELATES_TO: `wiki/domains/learnings/lesson-investigate-before-designing.md`
