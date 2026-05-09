---
title: "Lesson — Autopilot loop + batch-accumulator log: agent self-iterates, accumulates findings, operator processes in batch. Empirically validated 2026-05-05."
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: root-ghostproxy-test-session-empirical-validation
    type: project
    project: root-ghostproxy
    path: /root/.claude/projects/-root/0487d686-2839-447f-bc7e-354a55a2683a.jsonl
    description: "Test session 2026-05-05 13:34 — operator activated /mode-dual + iteration loop; agent ran 2 cycles surfacing 10 findings"
  - id: root-ghostproxy-iteration-log
    type: project
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-mode-dual-self-improvement-iterations.md
    description: "The batch-accumulator log produced by the autopilot"
  - id: operator-directive-mode-dual-self-improvement
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-mode-dual-self-evaluate-self-test-self-improve-with-loop.md
tags: [lesson, autopilot, loop, batch-accumulator, self-evaluation, self-improvement, mode-dual, empirically-validated, sister-project-applicable, layer-2]
---

# Lesson — Autopilot + batch-accumulator empirically validated

## Summary

A solo-operator + AI configuration achieves substantial parallel productivity when:

1. **Operator activates a mode** (PM/Architect/Dual) with a directive about the work focus
2. **Agent self-arms an autopilot loop** (`/loop /cycle` or fixed-interval cron) per the mode's `/cycle` sequence
3. **Each cycle accumulates findings** in a log file (the "batch accumulator") rather than acting unilaterally
4. **Cycles continue until blocked** (per `loop-cron-lifecycle` scenarios) — agent self-cancels when context-logical
5. **Operator processes accumulated batch** when convenient — multiple findings reviewed at once vs interrupting per-cycle

This pattern enables one operator + one agent to cover both PM and engineering workstreams in parallel, with the agent generating high-density value (audits, drift detection, gap identification) without requiring synchronous operator review.

## Context

This lesson applies when:
- Solo operator + AI configuration (no separate human PM/engineer)
- Project has substantial pre-defined backlog (the autopilot iterates over EXISTING work, doesn't invent new scope)
- Operator wants to step away while agent makes progress on auditable, low-risk work
- Drift detection, gap identification, surface-evaluation are the relevant workstreams
- Mode-aware /cycle infrastructure exists (state file + commands + cycle dispatch)

Does NOT apply to: short-burst work, high-risk operations, active design phases where the spec is changing fast, or scenarios without a coherent /cycle target.

## Insight

> [!success] **The batch accumulator is the load-bearing component**
>
> The pattern's load-bearing component is the **batch accumulator** — the log file where each cycle's findings append. Without it, autopilot becomes either: (a) silent (findings discarded), or (b) spam (each cycle interrupts operator). The accumulator decouples agent's iteration cadence from operator's review cadence.

> [!tip] **3-axis productivity boost: mode + /loop + accumulator**
>
> Combining mode (persona overlay) + /loop (cadence) + batch-accumulator (delayed-review) gives a 3-axis productivity boost. Mode shapes WHAT gets done; /loop shapes WHEN it gets done; accumulator shapes HOW operator processes results. Each axis is operator-controllable.
>
> The pattern also implements **operator-in-the-loop preserved** — agent surfaces and accumulates; operator processes batch when appropriate. The autopilot is autonomous on observation, not on decisions.

## Evidence

Empirical, 2026-05-05 root-ghostproxy test session:

- Operator activated `/mode-dual` with self-evaluation directive
- Agent logged directive verbatim to second-brain raw notes
- **Cycle 1**: 8 findings (4 doc-drifts + 1 parser bug + 1 deferred-by-design + 2 NEW operator-directed Epics)
- Agent armed `/loop /cycle` (dynamic mode, self-paced)
- **Cycle 2**: 2 more findings + 5 verified-clean checks + 3 cycle-1 finding updates
- Lifecycle signal `L1-near` triggered (6 blockers + 40 gated tasks) — dual mode rule correctly held off cancellation because Architect lens still had runway
- All findings captured in `/root/wiki/log/2026-05-05-mode-dual-self-improvement-iterations.md` (8KB structured table per cycle)
- Operator returned, processed accumulated batch in single review

Operator's verbatim canonical directive: *"and self-evualuate and self-test and self-improve. there should be enough already defined work that you can iterate over it and be self-critical and improve and do this in iteration with me but at the same time enabling a loop for when till you are blocked and things can commulate and we can process them in batch when appropriate."*

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Solo operator + AI** | The pattern's core: agent iterates while operator is away; operator processes batches |
| **Pre-defined backlog work** | The pattern needs scope to iterate over; new-scope generation is OUT |
| **Drift / audit workstreams** | Self-evaluation cycles surface drift the agent cataloges; operator decides remediation |
| **Mode-aware projects** | Modes provide the persona overlay; /loop provides cadence; batch-accumulator provides decoupling |
| **PM-style backlog grooming** | PM-mode autopilot can audit blockers, decisions, progress between operator turns |
| **Architect-style design review** | Architect-mode autopilot can audit ARCHITECTURE.md staleness, in-progress task drift, stage gates |
| **NOT applicable** | Short-burst work; high-risk implementation autopilot; design-active phases; projects without a coherent /cycle target |

## Failure mode it solves

Without this pattern:
- Operator must sit in real-time with the agent or accept idle gaps
- Agent's "what should I do next?" question per turn wastes operator attention
- Self-evaluation work doesn't happen because no one schedules it
- Drift between brain files and live state accumulates undetected

With this pattern:
- Operator can step away; agent does substantive auditing
- Findings batch up cleanly (per-cycle structured tables in the log)
- When operator returns: one batch review, multiple decisions made at once
- No "what next?" friction

## Operator's canonical directive (verbatim 2026-05-05)

> "and self-evualuate and self-test and self-improve. there should be enough already defined work that you can iterate over it and be self-critical and improve and do this in iteration with me but at the same time enabling a loop for when till you are blocked and things can commulate and we can process them in batch when appropriate."

Decomposed:
- Triple verb: self-evaluate + self-test + self-improve (each cycle does all three)
- Iterate over EXISTING defined work (don't invent new scope)
- Be self-CRITICAL (honest gaps, not just confirmation)
- Iterate WITH operator (operator-in-the-loop preserved)
- Loop until blocked
- Things ACCUMULATE when blocked (don't lose them)
- Operator processes batch WHEN APPROPRIATE (operator's timing)

## Empirical evidence (2026-05-05 test session)

Test session at root-ghostproxy:
- Operator activated `/mode-dual` with self-evaluation directive
- Agent immediately logged directive verbatim to second-brain raw notes
- Agent ran Cycle 1: 8 findings (4 doc-drifts + 1 parser bug + 1 deferred-by-design + 2 NEW operator-directed Epics)
- Agent armed `/loop /cycle` (dynamic mode, self-paced)
- Cycle 2 fired: 2 more findings + 5 verified-clean checks + 3 cycle-1 finding updates
- Lifecycle signal `L1-near` triggered (6 blockers + 40 gated tasks) — dual mode rule correctly held off cancellation because Architect lens still had runway
- Operator returned later, processed the accumulated batch via re-engagement

All findings captured in `/root/wiki/log/2026-05-05-mode-dual-self-improvement-iterations.md` (8KB structured table per cycle).

## Components required for this pattern

| Component | Where in /root |
|---|---|
| Mode mechanism (state file + brain pieces) | `/root/.claude/active-mode` + `/root/.claude/modes/<mode>.md` |
| Cycle command (per-mode dispatch) | `/root/.claude/commands/cycle.md` |
| Loop skill (interval or self-paced) | Bundled Claude Code skill `/loop` |
| Loop-cron-lifecycle rule | `/root/.claude/rules/loop-cron-lifecycle.md` (scenarios L1-L7) |
| Batch-accumulator log | `/root/wiki/log/<date>-<mode>-iterations.md` (append-per-cycle) |
| Tools for state queries | `/root/tools/{state,blockers,progress,decisions,cycle}.py` |

## Composition with other patterns

- **Three-mode pattern** (modes are the persona overlay this pattern operates within)
- **Hook → command determinism ladder** (autopilot uses commands at 100% determinism for the cycle steps)
- **Three-layer file-handling** (batch-accumulator log is gitignored / context-filtered correctly)
- **Methodology engine** (cycle's stage-gate-check step consults `methodology.yaml`)

## When to apply (sister-project-applicable)

- Solo operator + AI scenarios (no separate human PM/engineer)
- Project has substantial pre-defined backlog (modes need something to iterate over)
- Operator wants to step away while agent makes progress on auditable, low-risk work
- Drift / audit / surface-evaluation workstream applicable

## When NOT to apply

- Project work is short-burst (autopilot adds no value)
- High-risk operations where each step needs operator review (don't autopilot foundation install)
- Active design phase where the spec is changing fast (cycle's audit drift report would be noise)

## Anti-patterns

| Anti-pattern | Why bad |
|---|---|
| Autopilot generates new scope unilaterally | Operator's verbatim: "iterate over already defined work"; new scope needs PO approval |
| Findings ACTED on without operator review | Operator's verbatim: "process them in batch when appropriate"; agent surfaces, operator decides |
| Cycle output too verbose per fire | Burns operator attention when batch arrives; tighten per-cycle scope or move to focused mode |
| Loop runs forever with no auto-cancel | Per loop-cron-lifecycle: scenarios L1-L7 govern auto-cancel; without them, loop becomes spam |

## Relationships

