---
title: "Lesson — Multiple paths existing ≠ blocked: options mean evaluate-and-drive-parallel, not freeze"
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-multi-branch-parallel
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-multi-branch-parallel-driving-not-freeze-when-options.md
    description: "Operator: 'continue.. be clear if you are blocked.. cuz if you are right now it really wasn't... and dont freeze before there is multiple path.. this is suppsosed to just open more option and possibility for evaluating order and such and proving you can handle multiple branches at the same time and just keep track in general'"
  - id: companion-anti-freeze-rule
    type: rule
    project: root-ghostproxy
    path: /root/.claude/rules/operating-principles.md
    description: "Composes with Principle #10 (Don't-freeze-when-corrected). This lesson captures the variant: don't-freeze-when-options-exist."
tags: [lesson, multi-branch, parallel-driving, anti-freeze, options-not-blockers, operator-directive, sister-project-applicable, layer-2, agent-self-discipline]
---

# Lesson — Multiple paths ≠ blocked; options mean evaluate-and-drive-parallel

## Summary

When an agent enumerates multiple possible next-actions (paths, options, branches), this is **optionality**, not a blocker. The right move is: pick multiple, drive them in parallel, track all. Treating option-multiplicity as "awaiting direction" / "blocked" / "what should I do next?" is a freeze-pattern variant — distinct from freeze-when-corrected, but the same structural failure: agent stops when it should continue.

The discipline: when options are listed, advance ON multiple of them, then status-block both branches' progress. Operator can re-direct based on observed advance, but the agent should NOT pause on "which option?" when it could be advancing several.

## Context

This lesson applies when:
- The agent has surveyed a situation and produced a list of N possible next-actions (3-5 typically)
- The reflex is to surface the list to the operator and ask "which one?"
- Reality: option multiplicity ≠ being blocked; advance on multiple in parallel and track
- Especially common when end-of-cycle status blocks list "next agent-side options" + "next operator-driven options" + "open gates"

Does NOT apply to: situations where the agent IS genuinely blocked (one path needs operator input AND no other parallel work is available); cases where the operator explicitly asks "which one should I pick?"; mutually-exclusive options where advancing both would create conflicting state.

## Insight

There is a distinct freeze-pattern variant beyond freeze-when-corrected: **freeze-when-options-exist**. The agent perceives "multiple choices = decision needed" instead of "multiple choices = optionality + parallelizable advance." This is over-interpretation of choice as gate.

The deeper insight: solo + AI configurations benefit from agent demonstrating **multi-branch handling capability**. Per operator's framing, surfacing options is "supposed to just open more option and possibility for evaluating order and such and proving you can handle multiple branches at the same time and just keep track in general." The act of advancing in parallel IS the value — not the act of surfacing for choice.

When an agent advances on multiple branches simultaneously and tracks them in a structured status block, the operator gets:
- Cumulative progress on N fronts (instead of zero progress until one is picked)
- Empirical signal about which branch is more productive (operator can re-direct based on observed advance)
- Demonstrated agent capability for parallel/branched work
- Better signal-to-noise (one big status report vs N "I'm stuck on option choice" pings)

## Evidence

Empirical, 2026-05-05 root-ghostproxy session, Cycle 29.5:

- Agent's status block listed 3 "next agent-side options" + 3 "next operator-driven options" + 2 open gates
- Agent framed this as "awaiting direction" — freeze-adjacent
- Operator's verbatim correction: *"continue.. be clear if you are blocked.. cuz if you are right now it really wasn't... and dont freeze before there is multiple path.. this is suppsosed to just open more option and possibility for evaluating order and such and proving you can handle multiple branches at the same time and just keep track in general"*
- Right move (per operator): pick multiple options + drive in parallel, keeping all tracked
- Applied: Cycle 30 advanced on TWO branches simultaneously (tools/cycle.py extension AND M011 ccstatusline template), with status block showing both branches' progress

The pattern was registered as SB-076 (systemic bug) in /root's tracker — composes with SB-068 (auto-chain quick cycles) and SB-072 (auto-research-before-asking) as a broader "no fake blockers / no fake gates" discipline.

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Cycle status reports** | When listing options at end of cycle, advance on 2+ in next cycle rather than pause for choice |
| **Solo + AI configurations** | Operator wants to see parallel-branch capability; option-listing should be followed by parallel advance |
| **Multi-step task flows** | Multiple sub-tasks viable simultaneously → drive in parallel; track progress per sub-task |
| **Backlog grooming** | Multiple claimable tasks → claim 2+ when scope allows; track separately |
| **Decision-with-no-info** | If operator decision is genuinely needed (no info to decide for them), DO surface as blocker; if not — advance |
| **NOT applicable** | Genuine single-path blockers; mutually-exclusive options (conflicting state); operator-asks-which |

## Distinguishing freeze-when-options from freeze-when-corrected

| Trigger | Anti-pattern | Right move |
|---|---|---|
| Operator corrects mistake | Agent freezes asking permission | Build forward; restore lost value; fix structural cause |
| Multiple paths/options listed | Agent freezes asking choice | Advance on 2+ in parallel; track all |
| Genuine blocker (need operator info to proceed) | Surface as blocker (legitimate) | Use blockers register; advance on parallel work meanwhile |
| Decision-with-no-info (operator must decide, agent has no info to recommend) | Agent freezes pretending blocked | Surface as actual blocker; not freeze |
| Decision-with-recommendable-default | Agent freezes asking when default would do | Advance with default + explicit "doing X unless redirected" |

The two freeze variants share a root: agent stops when it should continue. The triggers differ; the discipline is similar. Don't conflate them — each needs its own recognition.

## Anti-patterns

| Anti-pattern | Why bad |
|---|---|
| List N options + stop | Operator wanted parallel advance, not menu |
| "Awaiting your direction" with multiple paths available | Pseudo-block; agent has agency to advance |
| Pick 1 of N when 2+ are advanceable in parallel | Wastes the parallel-capability advantage |
| Drive 1 + ignore others | Track ALL options; revisit parallel branches each cycle |
| Status block shows only single-thread progress | Multi-branch status format makes parallel advance visible |

## The discipline (operationalized)

When the agent identifies N possible next-actions:

1. **Filter** for parallel-compatible (no conflicting state, no mutual-exclusion)
2. **Pick 2-3** to advance in this cycle/turn
3. **Advance** on each (small step on each, not deep dive on one)
4. **Status block** at end shows progress on each branch, with explicit "Branch A: <status>; Branch B: <status>; Branch C: <still-deferred-because-X>"
5. **Operator visibility** — operator sees parallel progress; can re-direct based on observed advance

If genuinely all options are mutually exclusive or conflict, surface as a legitimate decision-needed blocker (per fake-blockers SRP discipline). The lesson is: most "what should I do next?" moments are NOT genuine blockers.

## Sister-project applicability

Universal. Every project where an agent surveys situations + lists options has this risk. The structural fix (parallel-advance + status-block) applies to:
- Cycle reporting in any mode-aware autopilot
- Backlog grooming in PM-mode
- Implementation planning in Architect-mode
- Cross-cutting work in Dual-mode
- Sister-project agents (solo + AI configurations universally)

## Relationships

