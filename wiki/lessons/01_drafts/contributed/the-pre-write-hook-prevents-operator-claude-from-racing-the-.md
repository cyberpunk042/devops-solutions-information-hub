---
title: "The pre-write hook prevents operator-Claude from racing the running agent on backlog files"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: medium
maturity: seed
derived_from: []
created: 2026-04-16
updated: 2026-04-16
sources: []
tags: [contributed, inbox]
contributed_by: "openarms-harness-v10"
contribution_source: "/home/jfortin/openarms"
contribution_date: 2026-04-16
contribution_status: accepted
contribution_reason: "First bidirectional contribution test — F9 from first consumer integration feedback"
---

# The pre-write hook prevents operator-Claude from racing the running agent on backlog files

## Summary

During an active `pnpm openarms agent run`, the methodology enforcement hooks (`pre-bash.sh`, `pre-write.sh`) block writes to task files, epic files, and `_index.md` from all contexts -- including operator-Claude running in a separate session. This is defense-in-depth working correctly: the harness writes these files during stage transitions, and concurrent operator edits would create race conditions where one set of changes is silently lost. The operator's productive parallel work during an active run must be confined to reading, lesson writing, log entries, and scratch drafts -- not backlog modifications.

## Context

This lesson applies whenever an operator runs a parallel Claude Code session while an autonomous agent run is in flight. The natural impulse is to use the wait time productively by pre-speccing the next tasks, updating the backlog index, or editing epic files. The hooks correctly prevent this because the harness owns those files during active runs.

The broader context is the "five Claude contexts" model where operator-Claude (Context A) and the solo-agent (Context B) are distinct processes that share a filesystem. Without file-level write protection, the two contexts race on shared state. The hook layer enforces the separation that the context model describes in theory.

## Insight

**File-level write hooks are the correct enforcement layer for preventing race conditions between operator and agent contexts.** The operator's mental model ("I'm a separate process, I can edit anything") is wrong -- the harness owns certain files during active runs and will overwrite or conflict with concurrent edits. The hook teaches this lesson at the moment of violation rather than after silent data loss.

The corrective workflow during active runs:

| Safe | Unsafe |
|---|---|
| Read code and files | Edit `wiki/backlog/tasks/T*.md` |
| Write to `wiki/lessons/` | Edit `wiki/backlog/tasks/_index.md` |
| Write to `wiki/log/` | Edit `wiki/backlog/epics/E*.md` |
| Draft next task in scratch buffer | Edit `.openarms/` state files |
| Edit `CLAUDE.md` / `AGENTS.md` | Run `git commit` on backlog files |
| Edit `scripts/methodology/` | Run `select-task` (state changes mid-run) |

The rule of thumb: anything the harness or agent might write during the active stage is unsafe for operator-Claude. When in doubt, wait for the run to complete.

## Evidence

**2026-04-14 evening, multi-task run `bwhmsotkr`** (T118, T119, T120 in flight):

1. Attempted to write `wiki/backlog/tasks/T121-wire-status-line-agent-watch-live.md` -- **BLOCKED** by `pre-write.sh` with message: `BLOCKED: Task/epic frontmatter is managed by the harness. Use /stage-complete to advance stages and /task-done to complete tasks.`

2. Attempted to edit `wiki/backlog/tasks/_index.md` to add T121 -- **BLOCKED** with the same message.

3. Writing to `wiki/domains/learnings/` and `wiki/log/` -- **NOT BLOCKED** (these are operator territory, not managed by the harness).

The hook correctly discriminates between harness-managed surfaces (backlog, state files) and operator-territory surfaces (lessons, logs, directives). This discrimination is the key design insight -- a blanket "no writes during runs" would be too restrictive.

**Historical context**: Before the E014 methodology infrastructure work tightened the hooks, the failure mode was likely "silent revert by harness recompute" rather than an explicit block. Some earlier "did the harness overwrite my edit?" moments may have been the same race condition without the protective hook firing. The explicit block is strictly better than silent data loss.

## Applicability

This lesson applies to three scenarios:

1. **Operator workflow during autonomous runs.** Route productive wait-time work to lesson refinement, log writing, architecture reading, or scratch drafts. Do not pre-spec tasks or edit the backlog index until the run completes and the harness exits cleanly.

2. **Designing write-protection hooks for multi-context agent systems.** The pattern generalizes: any system where multiple AI contexts (or AI + human) share a filesystem needs file-level write guards on the surfaces owned by the orchestrator. The guard should emit a clear diagnostic message (not just fail silently) and should discriminate between orchestrator-owned and operator-owned surfaces.

3. **Debugging "lost edit" symptoms in harness-managed projects.** If an operator's edit disappears after an agent run, the most likely cause is a race condition where the harness recompute overwrote the edit. The hook prevents this going forward, but prior instances without the hook are silent data loss.

**Open questions for future investigation:**
- Does the hook also block the agent's own writes during certain stages (e.g., document stage forbidding `src/` writes)?
- Is there a way to query "what surfaces are currently locked" without attempting a write?
- What is the exact mechanism that turns protection on/off (the `.openarms/methodology-enforced` flag)?

## Relationships

- RELATES TO: [[enforcement-hook-patterns|Enforcement Hook Patterns]] -- the hook mechanism and defense-in-depth pattern
- RELATES TO: [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement]] -- why hooks succeed where instructions fail
- RELATES TO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]] -- the harness owns the dispatch loop and the files it manages
- RELATES TO: [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy]] -- race conditions as a class of multi-context failure
- RELATES TO: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense]] -- hooks as the infrastructure enforcement layer
- RELATES TO: [[block-with-reason-and-justified-escalation|Block with Reason]] -- the hook emits a diagnostic rather than silently failing

## Backlinks

[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[Infrastructure Enforcement]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]]
[[Agent Failure Taxonomy]]
[[Three Lines of Defense]]
[[Block with Reason]]
