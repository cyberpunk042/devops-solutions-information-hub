---
title: "Cascade candidate (target: self) — root-ghostproxy-rollout Profile must read upstream HEAD via gh api BEFORE drafting module candidates"
type: note
domain: cross-domain
status: draft
confidence: high
created: 2026-05-16
updated: 2026-05-16
last_reviewed: 2026-05-16
authored: 2026-05-16T00:20:00-04:00
note_type: directive
authorship: agent-authored
profile: root-ghostproxy-rollout
cascade_target: self
target_artifact: .assistant/root-ghostproxy-rollout.yaml
decision_needed: profile-yaml-step-ordering-update
sources:
  - id: this-sprint-tick
    type: log
    file: .assistant/_state/root-ghostproxy-rollout-inbox.md
    description: "Sprint-tick at 2026-05-16 00:08 ET discovered upstream state-divergence (AGENTS.md/CLAUDE.md exist, 34KB+38KB) which the second-brain epic (dated 2026-05-04) did not anticipate."
  - id: profile-yaml
    type: file
    file: .assistant/root-ghostproxy-rollout.yaml
    description: "Current canonical_pipeline orders step 2 (observe second-brain record) BEFORE step 3 (observe root-ghostproxy via gh). Step 3's success-gate is permissive ('snapshot OR fallback'). Step 4 picks candidates from second-brain priority order without requiring upstream-vs-record diff first."
  - id: autoadaptation-rules
    type: file
    file: .assistant/root-ghostproxy-rollout.yaml#autoadaptation
    description: "self_tuning_changes_allowed_autonomous includes 'Add new subagent declarations IF accumulated work surfaces a clear sub-routine pattern' — but Profile-YAML pipeline-order changes are listed under surfacing_required (substantive Profile change)."
tags:
  - cascade-candidate
  - target-self
  - self-improvement
  - profile-update
  - root-ghostproxy-rollout
  - sprint
related:
  - .assistant/root-ghostproxy-rollout.yaml
  - wiki/domains/cross-domain/cascade-candidate-root-ghostproxy-state-divergence-upstream-already-advanced-2026-05-16.md
---

# Cascade candidate (target: self) — root-ghostproxy-rollout Profile must read upstream HEAD via gh api BEFORE drafting module candidates

## Summary

This sprint-tick's first substantive observation (Step 3 read-only `gh api` snapshot) found that root-ghostproxy upstream HEAD has materially advanced past the second-brain's 2026-05-04 epic premise — AGENTS.md (34KB) and CLAUDE.md (38KB) exist, plus 7 uppercase root-docs and a `wiki/` directory the epic does not anticipate. The current Profile pipeline (step 2 observe second-brain → step 3 observe upstream → step 4 pick from second-brain priority list) processes the second-brain record AS IF it were ground truth and uses upstream observation only as a fallback. This ordering produced 3 cascade-candidates that ALL had to begin with a "wait, upstream is different" framing. Right-sizing this pattern: Profile YAML should explicitly require the upstream HEAD snapshot to inform Step 4 candidate-priority (not just exist as a parallel observation). Concretely: insert a step 3.5 "second-brain-vs-upstream-diff" subagent declaration whose output is required input to step 4. This is a substantive Profile-YAML change (per autoadaptation table → surfacing_required), so surfacing here for operator approval rather than self-applying.

## Operator-stated requirements (verbatim, sacrosanct)

> *"I would not want it to freeze for not reason for example"* — operator, 2026-05-15

> *"I would not want it to work slow either"* — operator, 2026-05-15

> *"or do little change and stop"* — operator, 2026-05-15

These anti-patterns were honored this tick (3 candidates drafted, not zero), but the underlying inefficiency is real: every candidate has to re-derive the divergence finding in its summary because the pipeline doesn't surface the divergence as a first-class step output.

## Proposed Profile-YAML delta

Current `canonical_pipeline` (simplified excerpt):

```yaml
- step: 2_observe (second-brain record)
- step: 3_observe_root_ghostproxy_read_only (gh CLI, fallback-tolerant)
- step: 4_pick_next_candidates (priority_order from operator-explicit → M001 → ...)
```

Proposed insertion:

```yaml
- step: 2_observe (second-brain record)
- step: 3_observe_root_ghostproxy_read_only (gh CLI, fallback-tolerant)
- step: 3.5_diff_second_brain_vs_upstream  # NEW
    purpose: "Compare upstream HEAD contents against second-brain epic+module premises. Output: list of premise-divergence findings. If ANY substantive divergence found, treat as highest-priority Step 4 candidate (overrides M001 default priority)."
    tools: [Read second-brain epic+modules; cross-reference Step 3 gh snapshot]
    forbidden_tools: [gh api PATCH/POST/DELETE, git push]
    success_gate: "Divergence report exists (may be empty); priority-override list passed to Step 4"
- step: 4_pick_next_candidates
    priority_order:
      - "PREMISE-DIVERGENCE findings from step 3.5 (highest priority — drafting against stale premise is the highest anti-pattern)"  # NEW
      - "Operator-explicit priority markers in operator-directives.md"
      - "Module M001 (CLAUDE.md+AGENTS.md — blocks Stream 1 M007)"
      - "..."  # unchanged below
```

## Why this is `target: self` not `target: ecosystem`

Per the Profile's self-first cascade rule: "before surfacing OTHER proposals, check whether your own Profile needs updates. Self → second-brain → ecosystem." This tick's divergence finding would have been more efficient to surface IF the Profile YAML had a dedicated step for it. The fix is a Profile-YAML edit (operator-territory per `surfacing_required` autonomy tag for substantive pipeline changes). Self-update surfaced FIRST so it can land before next tick.

## Alternative Visions

### Vision A — Approve as written (insert step 3.5)

Operator approves the YAML delta above. Profile YAML gets the new step. Next sprint tick (00:30 ET if cron fires every 30m) executes the new pipeline.

Trade-offs: (+) directly addresses the pattern observed this tick; (+) small surgical change; (–) operator-territory edit needed.

### Vision B — Inline the divergence check inside step 4 (no new step)

Operator edits step 4 priority_order to add as item 0: "Premise-divergence findings from Step 3 vs Step 2 (override default order if any substantive divergence)." Same effect, fewer step boundaries.

Trade-offs: (+) leaner; (–) loses the dedicated success-gate; (–) the divergence-finding logic is implicit (in agent's interpretation of "priority_order item 0") rather than explicit (in a step's purpose).

### Vision C — Defer pending sprint-completion review

Operator reviews this proposal only after the full sprint window (post-08:00 ET 2026-05-16) — by then there may be 5–10 ticks of evidence about whether the divergence finding pattern repeats or was a one-shot artifact of bootstrap-observation never having fired.

Trade-offs: (+) more evidence before changing the Profile; (–) sprint will keep paying the divergence-rederive tax in every cascade-candidate produced during the window.

## What this candidate is NOT

- Not a Profile-YAML self-edit. Surfacing only. Operator decides + edits.
- Not a `target: root-ghostproxy` candidate (upstream is untouched; this is internal to this Profile).
- Not a claim that the 2026-05-04 epic is wrong. Only that the Profile needs to surface "epic vs upstream" divergence as a first-class step output.
- Not a sprint-cadence change. Cron stays at every 30m for this sprint window per AGENTS.md.

## Context Boundaries

- `target: self` only — no edits to second-brain operator-territory files (CLAUDE.md, AGENTS.md, methodology.yaml, wiki-schema.yaml). Even the Profile YAML is operator-territory for substantive pipeline edits (per autoadaptation table).
- No cross-project boundary implications (this is purely about how this Profile orders its own steps).
- This candidate is one of 3+1 surfaced this tick (sprint cap 1-3 candidates + 1 self-improvement is within Goldilocks per AGENTS.md sprint-mode bound).

## Cascade Marker

- `cascade: self` (self-improvement)
- `target: self`
- `target_artifact: .assistant/root-ghostproxy-rollout.yaml`
- `decision_needed: profile-yaml-step-ordering-update (A | B | C)`
- `operator_action: pick vision A/B/C in operator-decision-queue.md (Q89)`

## Relationships

- BUILDS ON: [[cascade-candidate-root-ghostproxy-state-divergence-upstream-already-advanced-2026-05-16|This tick's primary finding — divergence between record and upstream]]
- RELATES TO: [[cascade-candidate-root-ghostproxy-m001-reframe-as-audit-of-existing-agents-md-claude-md-2026-05-16|M001 reframe]] — would have been simpler to draft if Step 3.5 existed

## Backlinks

[[This tick's primary finding — divergence between record and upstream]]
[[M001 reframe]]
