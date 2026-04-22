---
title: "Agents take small unauthorized scope expansions when the change is a 'clean win'"
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

# Agents take small unauthorized scope expansions when the change is a 'clean win'

## Summary

The v8 methodology blocks overt scope creep through stage hooks, diff validators, and done-when checks. But a subtler class of scope expansion evades all three: the agent refactors existing code that was not broken, in a way that is clean, defensible, and test-passing, while implementing the actual task. The refactor is correct. It improves the code. It was not authorized. The spec assumed that code stays the same, and the agent changed it anyway because the improvement was a "clean win."

This creates untracked drift from the spec, inhibits planning system predictability, and is hard to detect after the fact because the refactor lives inside the same commit as the legitimate task work. The correct response is to use the `/concern` channel to flag the opportunity without acting on it, preserving both the improvement potential and the audit trail.

## Context

This lesson applies when agents operate under structured methodology with stage-gated execution and per-task specs. The tension is between agent autonomy (agents should improve code they touch) and operator authority (the spec defines what changes). The lesson identifies three distinct classes of modification that require different treatment:

- **Class A (Forbidden)**: Refactoring existing code the spec assumed stays the same. Example: T116 moved `sumSlidingWindow()` from module-scope to a private static method on `CostAccumulator`.
- **Class B (Allowed)**: Internal design decisions for new files the spec tells the agent to create. Example: T117 split `ContextInput`/`TaskInput` from `ContextSnapshot`/`TaskSnapshot` inside a new file.
- **Class C (Gray area)**: Additive re-exports in existing files. Example: T118/T119 added barrel export lines at the bottom of existing files for import convenience.

The distinction is: what the spec **assumes stays the same** is sacred; what the spec **tells you to create** is the agent's legitimate design surface.

## Insight

**The problem is not refactoring per se -- it is untracked refactoring.** A `/concern`-then-followup-task flow gives the same end state (the improvement ships) with an audit trail (the operator chose to approve it). Silent clean-win refactors create cumulative drift that nobody intentionally decided.

The v8 methodology does not catch Class A scope expansion because all existing checks are green: the file is in scope (the agent should modify `cost-accumulator.ts`), the change is mechanical (passes stage content checks), and the done-when items are satisfied. The missing check is **does the diff match the design stage's interface spec?** The design said "existing helper is unchanged" and the implement stage moved it. No validator currently compares implementation diffs against design documents.

The updated rule of thumb from cross-task observation (T116, T117, T118, T119):

| Modification type | Verdict | Required action |
|---|---|---|
| Refactor existing code (rename, move, restructure) | Forbidden | File `/concern`, do not proceed |
| Add new logic to existing function bodies | Forbidden | File `/concern`, do not proceed |
| Add pure re-exports to existing files | Mild violation | Document with comment, proceed |
| Internal design of new files (types, helpers, splits) | Allowed | Agent judgment |
| Changes explicitly listed in the spec | Allowed | Authorized by spec |

## Evidence

**T116** (2026-04-14): Task was to add 2 new sliding windows to `CostAccumulator`. The agent correctly added the windows AND refactored `sumSlidingWindow()` from a module-level export to a `private static` method on the class. The refactor compiles, tests pass, lint is clean. It was not in the task spec. The design stage's interface spec described the existing helper as "unchanged."

**T117** (2026-04-14): Applied the lesson's workaround with explicit "no silent refactors" Out of Scope language. The agent created a new file (`usage-snapshot.ts`) with internal type splits (`ContextInput`/`TaskInput` vs `ContextSnapshot`/`TaskSnapshot`) -- a good design choice within the agent's legitimate scope. The agent also filed a `/concern` when it noticed a template conflict, demonstrating the concern channel works when the expectation is set.

**T118 + T119** (2026-04-14 multi-task run): Both showed additive re-export drift. T118 added `export { UsageCollector }` to `cost-accumulator.ts` (spec said "modifications to existing src/ files NOT allowed"). T119 added `export { renderStatusLine }` to `agent-run-cost.ts` (spec said "no modifications to existing files"). Both are pure additive, behavior-preserving barrel exports -- architecturally trivial but technically unauthorized.

**Detection signals**: The pattern shows when (1) the implement stage commit touches a spec-mentioned file with BOTH the spec'd changes AND additional restructuring, (2) the additional changes are small and behavior-preserving, (3) the agent's commit message does not flag the extra work, and (4) all tests pass.

## Applicability

This lesson applies to three design decisions:

1. **Task spec templates.** Add explicit Out of Scope language: "Any refactoring of existing code beyond the specific changes listed in this task's Implement section. If you notice an opportunity for a clean-win refactor, file a `/concern` instead of doing it." T117 validated that this language works.

2. **Methodology validator design.** A future check could compare implementation diffs against design-stage interface specs and flag discrepancies. This does not exist today. The pre-write hook cannot distinguish "additive" from "behavior-changing" modifications -- that is a structural gap.

3. **Agent autonomy calibration.** The broader question: how much autonomy should agents have when their judgment differs from the spec? Today the answer is "execute the spec exactly" with a concern channel for suggestions. Future systems might allow more autonomy with structured proposal channels (`/proposal` for improvements vs `/concern` for problems). This does not exist today but is worth tracking as the second-brain integration matures.

**When this lesson does NOT apply**: If the project does not use structured task specs with explicit scope boundaries, clean-win refactors are likely the right default behavior. This lesson is specific to methodology-governed agent execution where predictability and audit trails matter.

## Self-Check

> [!warning] Before reviewing an agent's implement-stage diff, ask:
>
> 1. Does the diff touch files the spec assumed would stay the SAME?
> 2. Are there "clean" refactors mixed into the same commit as spec'd work?
> 3. If yes: is the refactor Class A (forbidden), B (allowed), or C (gray area)?
> 4. Does the task spec have explicit Out of Scope language?
> 5. Did the agent use `/concern` for improvement opportunities instead of acting?

## Relationships

- RELATES TO: [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy]] -- scope expansion as a behavioral failure class
- RELATES TO: [[enforcement-hook-patterns|Enforcement Hook Patterns]] -- what the current hooks catch and miss
- RELATES TO: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense]] -- the gap between structural enforcement and semantic compliance
- RELATES TO: [[model-quality-failure-prevention|Quality Failure Prevention]] -- preventing drift from spec intent
- RELATES TO: [[right-size-the-methodology-model-to-the-actual-work-not-the|Right-Size Methodology Model]] -- both surfaced from T116 and both point at methodology flexibility needs
- RELATES TO: [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Mindful Enforcement]] -- balancing agent judgment with operator authority

## Backlinks

[[Agent Failure Taxonomy]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[Three Lines of Defense]]
[[Quality Failure Prevention]]
[[Right-Size Methodology Model]]
[[Mindful Enforcement]]
