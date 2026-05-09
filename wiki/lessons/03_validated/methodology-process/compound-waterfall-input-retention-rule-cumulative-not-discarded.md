---
title: "Lesson — Compound / waterfall input-retention rule: operator inputs must cumulate, never discard prior context"
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-compound-waterfall
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-compound-waterfall-input-retention-directive.md
    description: "Operator: 'we might need a compound and waterfal rule and strategy so that we cummulate properly my inputs and make sure we never discard the tasks or inputs from before... we can add or augment tools when we need.'"
tags: [lesson, compound-waterfall, input-retention, cumulative-inputs, anti-discard, sister-project-applicable, layer-2, additive-doctrine]
---

# Lesson — Compound / waterfall input-retention rule

## Summary

Operator inputs across a session must CUMULATE — every directive, comment, clarification, and observation gets retained as part of the cumulative context. The agent must NEVER DISCARD prior inputs when processing a new one.

This is the structural answer to the "agent loses prior tasks when new context arrives" failure mode (parallel to sidetrack-recovery, but at the input-collection level). Compound = each new input ADDS to the stack. Waterfall = inputs cascade through the stages of the bug-fix flow + iteration cycle.

## Context

This lesson applies when:
- A multi-turn session collects multiple operator inputs (directives, comments, clarifications, observations) over time
- The agent has any tendency to process the latest input as if it replaces context (rather than augmenting it)
- The session lacks a structural mechanism (verbatim log + working-set tracker + cascade discipline) to keep prior inputs alive
- Operator pivots focus mid-session; without compound-waterfall, prior in-flight inputs vanish

Does NOT apply to: pure single-input one-shot sessions; cases where the operator explicitly cancels or supersedes a prior directive (the cancel/supersede is itself an input that gets logged).

## Insight

> [!success] **Compound + Waterfall are the structural override of respond-to-latest**
>
> The agent's default response shape is **respond-to-latest** — process the most recent input and ignore prior context unless it's still in the conversation buffer. Under context pressure or compaction, prior unresolved inputs silently disappear. The compound-waterfall pattern is the structural override:
>
> - **Compound**: every input ADDS to a working set; the latest input doesn't replace prior ones
> - **Waterfall**: each input cascades through stages (enqueued → analyzed → identified → in-progress → structurally-fixed → verified → archived) — none jumps backward (except `recurring`)

> [!info] **Realizes the operator's additive doctrine**
>
> Operator 2026-04-24: *"its not because I add something that you can discard everything I asked you before."* Words → behavior → structure. The lesson is the structural realization of the standing rule.

## Evidence

Empirical, 2026-05-05 root-ghostproxy session:

- Operator surfaced compound-waterfall directly: *"we might need a compound and waterfal rule and strategy so that we cummulate properly my inputs and make sure we never discard the tasks or inputs from before"*
- Multiple inputs across the session: SRP-violation in blockers, hooks-need-refinement, .gitignore audit, modes architecture, claude.ignore configuration, mode-aware /cycle behavior, milestones grouping, autopilot self-evaluation, fresh-session orientation, sister-project boundary, etc.
- Without compound-waterfall: agent processed each in turn, prior items vanished from working set; operator had to repeat
- With compound-waterfall: verbatim log layer + module index + governance docs jointly act as the working-set tracker; items cascade through bug-fix-flow stages with status field updates

The structural mechanism was already partially in place (verbatim logs at /root/wiki/log/, modules at /root/wiki/backlog/modules/_index.md with status field, governance docs at /root/wiki/governance/) — the lesson names the pattern + canonicalizes the discipline.

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Multi-turn operator sessions** | Cumulative input handling; verbatim log + working-set tracker + cascade |
| **Agents handling multi-input batched work** | Each input enters the working set; doesn't displace prior |
| **Session-recovery scenarios (post-compact)** | The verbatim log + working-set tracker are the recovery substrate; the agent re-loads them at session-start |
| **Multi-input concurrent workstreams** | The waterfall stage discipline lets multiple items progress in parallel without losing track |
| **Sister-project agent setups** | Universal pattern: verbatim log + tracker + cascade applies to any agent handling multi-input work |
| **NOT applicable** | Single-input one-shot sessions; operator-explicit cancellation/supersession (those are themselves logged inputs) |

## The pattern

```
Input 1 (operator) ─┐
Input 2 (operator) ─┼─ CUMULATE ─→ working set ─→ flow (log → analyze → identify → fix → verify → confirm) ─→ resolved
Input 3 (operator) ─┤
Input N (operator) ─┘
```

Compound: each new input is ADDED to the working set, not REPLACING prior ones.
Waterfall: each input cascades through the flow stages; resolved items archive but don't get DELETED from the historical record.

## Why this matters (operator's framing)

Per operator directive 2026-05-05: *"we might need a compound and waterfal rule and strategy so that we cummulate properly my inputs and make sure we never discard the tasks or inputs from before."*

Without compound-waterfall:
- New operator input arrives
- Agent processes the new input as if it replaces context
- Prior inputs (still unresolved) get forgotten
- Operator notices: "you didn't address X from earlier"
- Agent re-processes X, but now under degraded context
- Recurrence pattern

With compound-waterfall:
- New input arrives
- Working set: existing + new
- Each item flows through stages independently
- Operator sees PROGRESS on the cumulative set, not just the latest item
- Even if operator pivots focus, prior inputs remain queued

## What "cumulate" requires structurally

Three artefacts (or equivalents):

1. **Verbatim log of every input** — sacrosanct primary source. Per the words-are-sacrosanct rule + the bug-fix-flow's log step. Already in place via `/root/wiki/log/<date>-<slug>.md`.

2. **Working-set tracker** — registry of inputs that are IN-FLIGHT (not yet resolved). Could be:
   - The systemic-bugs tracker (for systemic-bug-shaped inputs)
   - The blockers register (for operator-input-required inputs)
   - The findings log (for observations that need integration)
   - A new "compound queue" (for inputs that don't fit the others)

3. **Cascade discipline** — each item moves through stages: enqueued → in-progress → structurally-fixed → verified → archived. Items don't skip stages; items don't get DELETED before reaching archived.

## What "waterfall" requires structurally

The cascade through stages must respect a DAG:

```
enqueued → analyzed → identified → in-progress → structurally-fixed → verified → archived
                                                        ↓ (if regression)
                                                    recurring (back to analyzed)
```

Inputs don't jump backwards (except for "recurring" which is its own status). They progress.

## Anti-patterns this lesson addresses

| Anti-pattern | Why bad |
|---|---|
| **Process new input in isolation** | Loses prior context; cumulative state degrades |
| **Replace working-set with just the latest input** | Discards prior, unresolved items |
| **"You'll have time to address X later" — then never returns** | Without a tracker, the "later" never comes |
| **Resolve by attrition (let stale items quietly drop)** | The drop is silent; operator doesn't know X was discarded |
| **One-pass response that closes everything** | Some items need multiple cycles; closing prematurely = same-as-discard |

## Sister-project applicability

Universal. Any agent handling multi-input multi-cycle work needs compound + waterfall. The structural requirements (verbatim log + working-set tracker + cascade discipline) are universal patterns that apply to:

- root-ghostproxy
- Sister projects (OpenArms, OpenFleet, AICP, devops-control-plane)
- Future projects

## Tools that may need augmentation (per operator)

Per operator: *"we can add or augment tools when we need. there can be real needs."*

Possible tool extensions to support compound-waterfall:

- `tools.inputs` — compound queue tracker (separate from blockers, decisions, findings)
- `tools.cycle` — extend to scan the compound queue and surface what's in-flight per cycle
- A status block at end-of-cycle that lists the cumulative state (echoing operator's directive about "end of a prompt or loop signal is also a good moment to output a status such as a count of blocked and their locations")

These are F-items (future enhancements) rather than immediate actions — capture as needs to address.

## Relation to existing patterns

- COMPOSES WITH [[sidetrack-detection-and-recovery]] — sidetrack is operating-on-wrong-track; compound-waterfall is keeping ALL tracks alive
- COMPOSES WITH [[verbal-acknowledgment-is-not-a-fix]] — acknowledging an input verbally without enqueueing it = discard
- COMPOSES WITH [[systemic-bugs-tracker]] — that tracker is one channel of the compound queue (for systemic-bug-shaped inputs)
- BUILDS ON operator's earlier doctrine: *"its not because I add something that you can discard everything I asked you before... when I add information, I add... I do not ask you to ignore the past"* (2026-04-24)

## The ADDITIVE DOCTRINE (operator's standing rule, this is a structural realization of it)

Operator's verbatim 2026-04-24: additive, not destructive. New direction LAYERS on prior. The compound-waterfall lesson is the OPERATIONAL pattern that realizes this doctrine. Words → behavior → structure.

## Relationships

- [[sidetrack-detection-and-recovery-when-agent-loses-the-original-task]] — parallel pattern
- [[words-are-sacrosanct]] (operator's rule layer) — feeds the verbatim-log step
- [[systemic-bugs-tracker-as-dedicated-governance-register]] — one channel of the compound queue
- Operator directive 2026-04-24 (additive doctrine origin)
- Operator directive 2026-05-05 (compound-waterfall naming)
