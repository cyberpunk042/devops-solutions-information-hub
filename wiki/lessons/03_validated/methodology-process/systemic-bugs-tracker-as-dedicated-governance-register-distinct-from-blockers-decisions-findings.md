---
title: "Lesson — Systemic-bugs tracker as a dedicated governance register (distinct from blockers/decisions/findings)"
type: lesson
domain: cross-domain
status: synthesized
confidence: medium
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: empirical-2026-05-05-systemic-bugs-tracker-emergence
    type: project
    project: root-ghostproxy
    path: /root/wiki/governance/systemic-bugs.md
    description: "/root test session agent authored a systemic-bugs.md governance register integrated into the /cycle command + tools.cycle.py. New register category beyond blockers / decisions / findings."
  - id: companion-lessons
    type: wiki
    file: wiki/lessons/03_validated/methodology-quality/fake-blockers-vs-real-blockers-empirical-verification-required.md
    description: "Builds on fake-blockers-vs-real-blockers (the SRP discipline that this register's existence operationalizes)"
tags: [lesson, governance, systemic-bugs, tracker-pattern, srp-discipline, sister-project-applicable, layer-2, agent-behavioral-bugs]
---

# Lesson — Systemic-bugs tracker as a dedicated governance register

## Summary

When a project accumulates **agent-behavioral systemic bugs** (recurring agent failure modes, structural rule violations, anti-patterns observed across cycles), a dedicated tracking register is the right structural answer — distinct from blockers, decisions, and findings.

The four registers form a complementary set:

| Register | What it tracks | SRP |
|---|---|---|
| **blockers** | Items requiring operator input to unblock CURRENTLY ACTIVE work | Operator-input gating |
| **decisions** | Decisions made + rationale + reversibility | Audit trail of choices |
| **findings** | Observations / gaps / drift identified in cycles | Cycle-time discoveries |
| **systemic-bugs** | Agent-behavioral patterns + structural-rule conflicts that recur | Long-term bug-fix evolution |

These are NOT interchangeable. Conflating them produces dumping-ground anti-patterns (per the fake-blockers lesson).

## Context

This lesson applies when:
- A project has long-running agent activity (multi-session, multi-cycle, autopilot loops)
- Agent-behavioral patterns recur (the same anti-pattern appears across cycles)
- The existing governance registers (blockers / decisions / findings) are starting to accumulate things that don't fit their SRP
- A structural-evolution discipline is desired (not just one-off bug fixes)

Does NOT apply to: short one-shot projects, projects without autonomous-agent activity, projects where agent-behavioral bugs are rare or out-of-scope.

## Insight

> [!success] **The four registers form a complementary set with distinct SRPs**
>
> The four governance registers (blockers, decisions, findings, systemic-bugs) form a complementary set with distinct **single-responsibility-principles (SRP)**. Conflating them produces dumping-ground anti-patterns: blockers becomes a list of *"things to do later,"* findings becomes random observations, decisions never gets used.

> [!info] **Why systemic-bugs deserves its own register**
>
> Systemic-bugs deserve their own register because they have characteristics no other register handles cleanly: recurring across cycles (not per-cycle like findings), structural-fix required (not just choices like decisions), agent-side resolution possible (not gated on operator like blockers), multi-status lifecycle (open/in-progress/structurally-fixed/verified/recurring), workblock-priority gating (per agent-bug-fix-flow).

> [!tip] **A register's value comes from its discipline**
>
> Each register's SRP is a constraint that keeps it useful. Adding a fourth register is the right answer when the new SRP can't be served by the existing three.

## Evidence

Empirical, 2026-05-05 root-ghostproxy session:

- Severe operator frustration with recurring agent-behavioral failures (verbal-only fixes, freezing-when-corrected, sidetrack patterns, fake-blockers, etc.)
- Existing registers (blockers, decisions) couldn't track agent-evolution work cleanly
- Operator's verbatim directive: *"they must all be addressed seriously into a loop"* — implies a register + cycle integration
- /root test session agent authored `/root/wiki/governance/systemic-bugs.md`
- Integrated into `/root/.claude/commands/cycle.md` step 9 ("systemic-bugs tracker iteration")
- Integrated into `/root/tools/cycle.py` for tool-driven surfacing
- Status lifecycle defined: open → in-progress → structurally-fixed → verified, with `recurring` regression branch
- Each cycle picks one entry to drive forward (highest-leverage open, then awaiting-verification, then recurring-flagged-for-operator)

The structural answer materialized as files; the lesson captures the pattern for sister-project propagation.

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Long-running agent projects** | Systemic-bugs register tracks agent-evolution work; integrates with cycle |
| **Multi-cycle autopilot loops** | Each cycle picks one systemic-bug entry to drive; structural fixes accumulate |
| **Agent-self-improvement disciplines** | The register is the substrate for structural evolution; without it, fixes scatter |
| **Sister-project pattern adoption** | Universal: any project with autonomous agent activity benefits from the register + cycle integration |
| **Governance register design (general)** | Apply SRP per register; add a new register only when an existing one's SRP doesn't fit |
| **NOT applicable** | Short one-shot projects; projects without autonomous-agent activity; projects where agent-behavioral bugs are out-of-scope |

## Why systemic-bugs deserves its own register

Agent-behavioral bugs have characteristics that don't fit other registers:

| Characteristic | Why it matters |
|---|---|
| **Recurring across cycles** | Findings are per-cycle; systemic bugs span multiple cycles |
| **Structural fix required** | Decisions document choices; systemic bugs need structural change (rule, hook, code) |
| **Operator may NOT be the resolver** | Blockers gate on operator; systemic bugs are agent-side, sometimes auto-fixable |
| **Status spans more than open/closed** | open / in-progress / structurally-fixed / verified / recurring — the verification is empirical and may take many cycles |
| **Workblock-priority gating** | Per workblock-priority rule (#11): when a systemic bug is reported, it's UTMOST priority — distinct flow from blocker resolution |

A blockers register is a queue of operator decisions. A systemic-bugs register is a queue of agent-evolution work. Mixing them obscures both.

## Status lifecycle (operator-defined)

```
open → in-progress → structurally-fixed → verified
                              ↓
                          recurring (if structural fix didn't hold)
                              ↓
                          (back to open with stronger fix)
```

| Status | Meaning |
|---|---|
| `open` | Bug observed; structural fix not yet applied |
| `in-progress` | Agent is working on the structural fix this cycle |
| `structurally-fixed` | Rule / hook / code change landed; awaiting empirical verification |
| `verified` | Multiple cycles without recurrence; bug considered closed |
| `recurring` | Despite structural fix, bug re-appeared; needs stronger fix or different approach |

## Format (per root-ghostproxy first implementation)

Each entry has:
- **ID** (SB-XXX, sequential)
- **Title** (one-line summary)
- **Status** (lifecycle above)
- **Severity** (critical / high / medium / low)
- **Pattern** (the anti-pattern observed)
- **Evidence** (transcript references, dates, recurrence count)
- **Structural fix path** (which rule/hook/code change addresses it)
- **Verification approach** (how to confirm fix held)

## Integration with the cycle

The /cycle command picks one systemic-bug per fire to drive forward (per root-ghostproxy's cycle.md step 9):

1. First priority: `open` bug with available structural fix path → highest-leverage one
2. Else: `structurally-fixed` bug awaiting verification → propose verification approach
3. Else: `recurring` bug → flag for operator-attention (the agent's structural fix didn't hold; needs operator insight)

This makes the systemic-bug-fix work LIVE in the autopilot loop. The cycle isn't just surveying; it's actively driving structural evolution.

## Why this fixes the dumping-ground problem

Without a dedicated register, agent-behavioral bugs end up:
- In the blockers register (mis-categorized as needing operator decisions when the fix is agent-side)
- In findings (loses workblock-priority status — they're not casual findings)
- In decisions (decisions are choices made, not work to do)
- Scattered in iteration logs (not queryable as a coherent set)

The dedicated register:
- Has its own SRP (long-term agent-evolution)
- Has its own status lifecycle (more granular than open/closed)
- Has its own integration point (the cycle's systemic-bug-driver step)
- Doesn't pollute the other registers

## Pattern caveats

| Caveat | Note |
|---|---|
| Risk of new dumping ground | The register itself can become a dumping ground if anti-patterns aren't enforced. SRP discipline applies here too — only legitimate systemic-bugs go in. |
| Maintenance overhead | Register requires updates per cycle; if the agent doesn't, it goes stale. The cycle's systemic-bug-driver step is the maintenance trigger. |
| Operator-attention competition | If the register's open count grows unbounded, operator attention is split. Triage by severity + workblock-priority gates; old `verified` items can archive. |

## Sister-project applicability

Any project where:
- Agent has long-running role (across sessions, cycles)
- Agent-behavioral bugs are likely (most agentic-loop projects)
- A formalized evolution loop is desired
- Operator wants visibility into agent-self-improvement state

This pattern emerged from root-ghostproxy 2026-05-05 in response to severe operator frustration with agent-behavioral failures. The register is part of the structural answer.

## Relationships

