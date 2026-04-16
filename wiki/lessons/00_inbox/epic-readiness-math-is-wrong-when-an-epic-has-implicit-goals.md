---
title: "Epic readiness math is wrong when an epic has implicit goals beyond its current children"
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
contribution_status: pending-review
contribution_reason: "First bidirectional contribution test — F9 from first consumer integration feedback"
---

# Epic readiness math is wrong when an epic has implicit goals beyond its current children

## Summary

The harness computes epic readiness as the average of its child task readiness values. This formula is only correct when the children fully cover the epic's goals. When an epic has implicit goals not yet broken into tasks, the average is a mathematical artifact. The first completed child flips the epic to 100% even when the real work is barely started. On E013, completing a single research spike (T115) flipped the epic from `readiness: 0` to `readiness: 100` and `status: review` -- despite 14 implementation tasks still pending across two tracks.

The bug fires every time all current children are simultaneously at 100% and the child set is sparse. It is most dangerous early in an epic's lifecycle (1-4 children) and becomes benign as the child set grows (5+ children with mixed states produce meaningful averages).

## Context

This lesson applies when using a harness that auto-computes epic readiness from child task completion. The pattern generalizes to any hierarchical project tracker where parent progress is derived from child progress: if the children do not cover the parent's full scope, the derived metric is meaningless.

The deeper principle is the same as the task-level "specific done-when" lesson: **the methodology only knows what is structurally encoded; everything in prose is invisible to it.** At the task level, vague done-when items let agents satisfy criteria trivially. At the epic level, sparse children let the harness compute 100% readiness trivially. Both reduce to the same structural gap.

## Insight

**Epic readiness as `average(child.readiness)` is only valid when children fully cover epic scope.** When they do not, three compounding bugs manifest:

1. **Readiness inflation.** `readiness: 100` when all (few) children are done, regardless of how much implicit work remains. The harness auto-flips `status: review` based on the inflated number.

2. **Stage-name pollution.** The recompute writes `current_stage` and `stages_completed` to epic frontmatter -- but epics do not have stages (stages are per-task). The values are projections of the last child's state, creating a category error (e.g., `current_stage: test` on an epic).

3. **Stale artifact lists.** The epic-level `artifacts` field gets stuck on the first child's outputs and does not aggregate across subsequent children. After T115, T116, and T117 completed, E013's artifacts still listed only T115's 2 research documents -- missing T116's 12 files and T117's 2 files.

After three consecutive runs on E013, **5 out of 5 frontmatter fields below the title were wrong** (status, current_stage, readiness, stages_completed, artifacts). The epic frontmatter was functionally fiction.

**Trust rules for epic readiness:**
- 1-4 children: do not trust readiness, set manually
- 5+ children with mixed states: approximately correct
- 10+ children: reliable
- Any epic with implicit goals beyond current children: never trust, regardless of child count

## Evidence

**T115 completion** (2026-04-14): Single research spike. E013 went from `readiness: 0 / status: draft` to `readiness: 100 / status: review`. The epic body described scope covering a full status line track AND a separate dashboard command -- none of which T115 implemented.

**T116 completion** (2026-04-14 evening): Manual override (`readiness: 15`) was overwritten back to `readiness: 100`. Additionally, `current_stage: test` and `stages_completed: [document]` appeared on the epic -- a category error since epics do not have stages.

**T117 completion** (2026-04-14 evening): Third confirmation. `readiness: 100 / status: review` again. Artifacts field still showed only T115's 2 files, missing T116's 12 and T117's 2. Five out of five frontmatter fields wrong.

**Multi-task run T118-T120** (2026-04-14 evening): Nuance discovered. The harness computed E013 at 83% (5 of 6 children at 100%, 1 in flight). **The bug is benign when at least one child is in-flight**, because the average is meaningfully below 100%. The dangerous window is between the last in-flight child completing and a new child being created.

**State transition trace** (T115):
```
Before: E013.children = [], readiness = 0, status = draft
After T115 created: children = [T115], T115.readiness = 0 -> E013.readiness = 0
After T115 done: T115.readiness = 100 -> E013.readiness = average([100]) = 100
-> harness auto-flips status to review
```

## Applicability

Five structural fixes, in order of cost:

1. **Cheap: Warning on sparse 100%.** When readiness flips to 100% and child count is below a threshold (e.g., 5), emit a warning and do not auto-flip status. ~30 lines of code.

2. **Medium: Epic-level done-when items.** Allow epics to declare their own done-when items independent of child task readiness. Readiness only reaches 100% when both child average AND epic done-when are satisfied.

3. **Medium: Stop writing stage-name fields to epics.** Remove `current_stage` and `stages_completed` from epic frontmatter entirely (or rename to `latest_child_stage` with explicit aggregate semantics). Epics are containers, not stage-bearing entities.

4. **Medium: Aggregate artifacts across all children.** Collect `artifacts` from every completed child task and write the union to the epic. Currently stuck on first child only.

5. **Expensive: Implicit-children awareness.** Allow epics to declare expected scope or child count so the harness can detect when current children do not cover declared scope. Probably overkill for current scale.

**Workaround until fixes land:**
- Manually set epic `status: active` and `readiness:` to a realistic number after creating the first child
- Add a "Status note" section to the epic body explaining actual scope
- Re-check and fix epic frontmatter after every child completion
- Treat the epic body as authoritative over frontmatter when conditions above apply

## Relationships

- RELATES TO: [[model-methodology|Model: Methodology]] -- the readiness computation and epic lifecycle logic
- RELATES TO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]] -- the harness recompute that writes epic frontmatter
- RELATES TO: [[coverage-blindness-modeling-only-what-you-know|Coverage Blindness]] -- the harness models only what is structurally encoded
- RELATES TO: [[systemic-incompleteness-is-invisible-to-validation|Systemic Incompleteness]] -- implicit goals invisible to the validation system
- RELATES TO: [[[[the-harness-turncount-variable-counts-streaming-events,-not-|Harness turnCount Bug]] -- both are methodology-infrastructure bugs surfaced by real multi-task usage]]
- RELATES TO: [[[[right-size-the-methodology-model-to-the-actual-work,-not-the|Right-Size Methodology Model]] -- both surfaced from T115/T116 runs]]

## Backlinks

[[model-methodology|Model: Methodology]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]]
[[Coverage Blindness]]
[[Systemic Incompleteness]]
[[Harness turnCount Bug]]
[[Right-Size Methodology Model]]
