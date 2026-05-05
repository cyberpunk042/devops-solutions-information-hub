---
title: "2026-05-05 — Operator directive: modes are for DOING work (not just running cycle surveys); cycle is heartbeat, between-cycle is the work"
type: note
domain: cross-domain
status: raw
confidence: high
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-modes-are-for-doing
    type: directive
  - id: test-session-agent-captured-quote
    type: project
    project: root-ghostproxy
    path: /root/.claude/modes/dual-expert.md
    description: "The test session agent captured this verbatim quote inline in dual-expert.md; this raw note formalizes it as sacrosanct primary source"
tags: [note, operator-directive, sacrosanct, verbatim, modes, doing-work, cycle-vs-between-cycle, surface-without-act-failure-mode]
---

# Operator directive — 2026-05-05 modes are for DOING work, not just surveying

## Verbatim

> "obviously if you are in a mode its to do work lol even when that work stop to defining docs or specs or requirements or preparing tasks or advancing architecture or planning or information about blocker and question and answers and solutions and options and suggestions"

(Captured inline by the test session agent in `/root/.claude/modes/dual-expert.md`'s "Cycle vs between-cycle action" section. Formalized here as the sacrosanct primary source.)

## Decomposition

### A — Modes exist for ACTION, not just survey

- "if you are in a mode its to do work lol"
- The "lol" is rhetorical emphasis — operator is correcting an implicit assumption that modes = read-only cycles.
- Modes are PERSONAS for getting work done.

### B — "Work" includes non-implementation work

Operator names what counts as "work" within a mode (verbatim):
- Defining docs
- Defining specs
- Defining requirements
- Preparing tasks
- Advancing architecture
- Planning
- Information about blockers
- Questions
- Answers
- Solutions
- Options
- Suggestions

These are ALL work. Stages document/design/scaffold all produce these. The mode operates within the methodology stage, but modes ≠ idle survey-only.

### C — Cycle vs between-cycle distinction

The /cycle command is the survey heartbeat (orient + scan + report). The actual work happens BETWEEN cycles:
- Cycle = survey + accumulate findings
- Between-cycle = work the unilateral subset (per `work-mode.md` PO approval boundary)

If agent in dual mode runs cycles but never works between them → progress stalls → "surface-without-act" failure mode.

### D — Failure mode named (F-eval-12 self-critique by test-session agent)

The test session agent surfaced this anti-pattern as F-eval-12 self-critique:
> "Surface-without-act: agent in dual mode runs cycles, surfaces findings, but doesn't act on the unilateral subset → progress stalls → operator asks why nothing is happening."

Correction: each cycle ends with a NEXT-ACTION list (split into operator-batch vs unilateral); agent works the unilateral list immediately, surfaces operator-batch for review.

## Action plan

1. Log this directive verbatim — done (this file).
2. Verify `/root/.claude/modes/dual-expert.md` already captures the doctrine — yes (test session agent did this).
3. Mirror the discipline into `/root/.claude/modes/pm-scrum-master.md` + `/root/.claude/modes/devops-architect.md` cycle-vs-between-cycle sections.
4. Surface the "surface-without-act" failure mode as a registered learning (lesson) in second brain.
5. Update `work-mode.md` PO-approval-boundary table to make the unilateral subset more explicit (what an agent in a mode CAN do without operator review).

## No-conflate guard

- "to do work" = operator wants action, not just reports.
- "even when that work stop to defining docs or specs..." = the kind of work named is BROAD; not just code.
- "lol" = emphasis, not levity; operator is correcting agent behavior.
- The directive does NOT relax the PO approval boundary — large/destructive changes still need operator approval. It DOES relax "agent shouldn't act unilaterally" misreadings — agent should act on the UNILATERAL subset.
