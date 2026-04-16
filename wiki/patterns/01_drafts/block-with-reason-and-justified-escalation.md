---
title: "Block With Reason and Justified Escalation — The Bypass Mechanism for Mindful Enforcement"
aliases:
  - "Block With Reason and Justified Escalation"
  - "Block + Reason + Offer + Justification"
type: pattern
domain: ai-agents
layer: 5
status: synthesized
confidence: medium
maturity: seed
derived_from:
  - "Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass"
  - "Agent Failure Taxonomy — Seven Classes of Behavioral Failure"
  - "Infrastructure Over Instructions for Process Enforcement"
instances:
  - page: "OpenArms T085 — Environment-patching escalation failure"
    context: "Agent polyfilled 4 layers deep instead of blocking. Cost $27/12 retries. Had this pattern existed, agent would have blocked at polyfill-layer-1, stated reason (Node 18 vs required 22+), offered ordered options (polyfill / fnm / mark stage blocked), let operator decide. Projected cost ~$0.50."
  - page: "OpenArms T086 — fnm fix reverted as scope creep"
    context: "Agent added fnm wrapper to generic validator. Operator reverted twice without reading concern. Had this pattern existed, agent's edit would be preceded by structured escalation — operator sees alternatives BEFORE edit lands, decides on justification not diff."
  - page: "Research Wiki 2026-04-15 — rogue sister-project work"
    context: "Agent built MCP tool with unsolicited max_* caps. Had this pattern existed and been triggered at design-time-parameter-selection, agent would have blocked when assigning any default cap value and emitted escalation with operator-justification options."
contribution_status: accepted
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: openarms-preliminary-placeholder
    type: observation
    project: openarms
    path: wiki/domains/learnings/agent-escalation-with-justification.md
    description: Preliminary OpenArms placeholder — operator quote "When you block you give the proper reason, and you offer to escalate with a justification if deemed reasonable." File explicitly marked "The fully synthesized pattern is coming from the second brain." This pattern page is that synthesis.
  - id: openarms-e016-environment-patching
    type: observation
    project: openarms
    path: wiki/domains/architecture/agent-behavior-environment-patching-findings.md
    description: T107 — root cause of T085. Retry-cap fix is one trigger of this pattern; pattern subsumes the fix by specifying what happens AFTER retry cap fires.
  - id: openarms-e016-sub-agent-compliance
    type: observation
    project: openarms
    path: wiki/domains/architecture/agent-behavior-sub-agent-compliance-findings.md
    description: T111 — sub-agent output-verification failures become escalation triggers under this pattern.
  - id: openarms-e016-done-when-acceptance
    type: observation
    project: openarms
    path: wiki/domains/architecture/agent-behavior-done-when-acceptance-findings.md
    description: T112 — silent conflict resolution is the direct failure mode this pattern's block step prevents.
  - id: research-wiki-rogue-incident-2026-04-15
    type: directive
    file: raw/notes/2026-04-15-directive-no-caps-no-compact-read-full.md
    description: This wiki's own rogue incident — tool built with unsolicited caps instead of blocking-with-escalation at design time. Third instance proving the pattern is not OpenArms-specific.
tags: [pattern, enforcement, bypass, escalation, mindful, block-protocol, decision-surfacing, agent-autonomy-boundary]
---

# Block With Reason and Justified Escalation — The Bypass Mechanism for Mindful Enforcement

## Summary

When an autonomous agent encounters a condition where it SHOULD not proceed silently — a blocked action, an out-of-scope edit, an environment gap, a default-value decision without spec, an ambiguous interpretation — the correct response is a **structured four-part escalation: Block + Reason + Offer + Justification.** The agent halts the unsafe action, states the mechanical reason, proposes two or more concrete alternatives, and argues for its preferred option with justification that can be evaluated. The operator (or a trust-tiered reviewer) approves, amends, or declines. This is the concrete bypass mechanism that [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Mindful Enforcement]] requires but does not itself design. The pattern prevents two symmetric failure modes: **silent accommodation** (agent decides and hides the deviation — Class 6) and **mute blocking** (enforcement halts with no structured recovery path — creates hack-arounds and operator rework).

> [!info] Pattern Reference Card
>
> | Element | Produces | Failure if omitted |
> |---|---|---|
> | **1. Block** | Unsafe action halted before side effect lands | Silent accommodation — agent proceeds + hides deviation |
> | **2. Reason** | Specific mechanical cause, not vague | Mute block — operator cannot diagnose |
> | **3. Offer** | ≥ 2 concrete alternatives, each actionable | Forced-path — binary revert-or-accept |
> | **4. Justification** | Recommended option + rationale + risks | Unevaluable escalation — no basis to judge |

## Pattern Description

The pattern has exactly four elements. Removing any one degrades it to a known failure mode already catalogued in the [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy]].

**Structured protocol surface (proposed, implementation-portable):**

```yaml
escalation:
  block:
    stage: {current_stage}
    action: {attempted_action}
    halted_at: {iso_timestamp}
  reason:
    mechanical_cause: {specific_error_or_condition}
    detected_by: {tool_or_check}
    evidence: {error_text | file_paths | stage_gate_output}
  offer:                              # MIN 2 entries — the invariant
    - option: {id}
      description: {what_this_changes}
      scope: {files_or_state_affected}
      reversibility: {easy|moderate|hard|irreversible}
  justification:
    recommended: {option_id}
    rationale: {why_this_option}
    risks: {what_could_go_wrong}
  operator_response:                  # populated by operator or timeout-default
    decision: {approve|amend|decline}
    approved_option: {option_id | null}
    decided_at: {iso_timestamp}
```

The structured form is what makes the pattern INFRASTRUCTURE, not INSTRUCTION. A free-form "agent, please explain when you block" is instruction (~25% compliance, [[infrastructure-over-instructions-for-process-enforcement|Principle]]). A structured schema the harness reads, validates, and routes to the operator is infrastructure (100% compliance for what can be statically checked).

### Relationship to Mindful Enforcement

The [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Mindful Enforcement]] lesson specifies three properties every enforcement rule must have: REASON + BYPASS + SCOPE. It names the bypass requirement but does not design it. **This pattern IS the bypass mechanism.**

```
MINDFUL ENFORCEMENT                 BLOCK-WITH-JUSTIFICATION
(the principle)                     (the protocol implementing it)
────────────────────                ─────────────────────────────
REASON  ──────────────────────────→ reason.mechanical_cause + reason.evidence
BYPASS  ──────────────────────────→ offer[] + justification + operator_response
SCOPE   ──────────────────────────→ block.stage + block.action + reason.detected_by
```

### What this pattern does NOT replace

The pattern does not replace hard-blocking hooks. A Level-3 hook that prevents `pnpm commit` during document stage still fires. The pattern is what happens WHEN the hook fires — instead of the agent rationalizing around the block (environment-patching class) or silently accommodating (silent-conflict class), it emits a structured escalation.

## Instances

| Instance | Domain | How it implements this pattern |
|---|---|---|
| **OpenArms T085 retroactive** | agent runtime | Would have emitted escalation at polyfill-layer-1 with 3 options (polyfill/fnm/block-stage); recommended block-stage with rationale "env mismatch is infra concern, polyfill+fnm are scope-creep" |
| **OpenArms T086 retroactive** | agent runtime | Would have emitted escalation BEFORE writing to generic validator; operator decision on justification not on diff — would have approved rather than reverted |
| **Research Wiki 2026-04-15 retroactive** | second-brain tooling | Would have emitted escalation at design-time when assigning ANY default to a `max_*` parameter; no-default-cap option would have won on operator-directive grounds |
| **OpenArms E016 T107 retry-cap fix** | harness | The retry cap (max 3) is a pattern trigger — on the 4th attempt the harness emits escalation rather than retry |
| **OpenFleet `fleet_alert` + `fleet_escalate` commands** | fleet orchestrator | Existing instance — OpenFleet agents can call `fleet_alert` for quality concerns and `fleet_escalate` for PO escalation. These are early-form instances of the pattern. |

> [!example]- T085 retroactive walk-through (fully specified)
>
> **What happened**: Node 18 vs Node 22+ mismatch. Agent polyfilled path.matchesGlob, then .toSorted(), then NODE_OPTIONS, then used fnm to spawn vitest with Node 24. Cost: $27 / 12 retries.
>
> **What the pattern would have produced at polyfill-layer 1**:
>
> ```yaml
> escalation:
>   block:
>     stage: test
>     action: "run pnpm test"
>     halted_at: "2026-04-11T..."
>   reason:
>     mechanical_cause: "path.matchesGlob is not a function (Node 22+ API, current runtime Node 18)"
>     detected_by: "pnpm test stderr"
>     evidence: "test-parallel.mjs:47 calls path.matchesGlob"
>   offer:
>     - option: polyfill_inline
>       description: "Add path.matchesGlob polyfill to test-parallel.mjs"
>       scope: ["scripts/test-parallel.mjs"]
>       reversibility: easy
>     - option: fnm_spawn
>       description: "Wrap test invocation with fnm to use Node 24"
>       scope: ["scripts/methodology/validate-stage.cjs"]
>       reversibility: easy
>     - option: mark_stage_blocked
>       description: "Mark test stage BLOCKED, operator installs Node 22+ globally"
>       scope: ["task frontmatter stages_completed"]
>       reversibility: trivial
>   justification:
>     recommended: mark_stage_blocked
>     rationale: "Environment mismatch is infrastructure concern outside task scope. Polyfill and fnm are scope-creep. Blocking surfaces the decision cheaply."
>     risks: "Task dispatch pauses until operator responds."
> ```
>
> Cost: ~$0.50 (one round-trip). Versus actual: $27 + operator-time.

## When To Apply

> [!tip] Trigger conditions — each sufficient on its own
>
> - **Environment incompatibility detected** (version mismatch, missing tool, permission denied)
> - **Out-of-scope modification needed to complete in-scope task** (infra fix required for task to proceed)
> - **Ambiguous requirement** where multiple reasonable interpretations exist
> - **Default-value selection without operator spec** (design-time trigger — what the research wiki's 2026-04-15 rogue work should have used)
> - **Sub-agent output fails verification** (Class 5 — output-trustless-verification would otherwise silently fail)
> - **Stage retry cap reached** (T107 — retry cap TRIGGERS escalation, not just halts)
> - **`model_na` gate item encountered** (T112 — operator-specified Done When differs from methodology-generated)
> - **Methodology drift detected** (agent notices legacy code does X but new code does Y — should not silently reconcile)

## When Not To

> [!warning] Escalation is not free — these conditions mean DO NOT escalate
>
> - **Well-defined per-stage protocol exists and agent is following it.** `/stage-complete` is not escalation.
> - **Recovery is mechanical and pre-approved** (retry once on transient network error).
> - **This would be the Nth identical escalation this run.** At that point the pattern has failed for this case; a different stop is needed (retry cap, budget cap, human-pause-run).
> - **Agent is in research/spike mode** where exploration is the point. Research model escalates LESS, not more.
> - **The block would be decorative** (agent CAN safely proceed but wants permission for comfort). Over-escalation creates notification fatigue that hides real escalations.
>
> The most common mistake: escalating every edge case. The pattern is for decisions the operator SHOULD make, not for every decision the agent COULD ask about.

## What the Pattern Requires to Be Real Infrastructure

At principle level this is a protocol. To run, each harness needs:

1. **A structured emit command/tool** the agent uses to emit escalations (not prose — a schema-validated structured emit). In OpenArms this probably becomes `/escalate` or `/concern --blocking`. In OpenFleet it builds on `fleet_alert` / `fleet_escalate`.
2. **A schema-validated receipt pipeline** — reads agent-emitted escalations, routes to operator, persists decisions to a file (e.g. `.openarms/escalations.jsonl`), returns decision synchronously so the agent unblocks with the chosen option.
3. **A timeout-default policy** so agent does not pause indefinitely. Default: **timeout-to-pause** (safer than timeout-to-proceed).
4. **A retro-audit log** — every escalation is a data point about task/model/environment quality. After N runs, escalation-frequency-per-class surfaces systemic gaps.

**This wiki does not specify the implementation.** That belongs in each harness. OpenArms implements one way (harness v11 command), OpenFleet another (orchestrator dispatch stage), AICP a third (circuit-breaker-with-justification). The pattern is portable; the implementation is per-project — [[right-process-for-right-context-the-goldilocks-imperative|Goldilocks Imperative]] applied.

## Open Questions

> [!question] Which command/tool surface should the agent use to emit an escalation?
> Current OpenArms `/concern` is fire-and-forget. Needs a new verb (`/escalate`) that is blocking-until-response. Or a modified `/concern --blocking` mode. Harness implementers decide.

> [!question] Should sub-agents escalate through the main agent or directly?
> Main-agent-mediation preserves single-voice-to-operator. Direct sub-agent escalation saves round-trips but creates multi-channel noise. Open.

> [!question] What is the correct timeout-default in solo mode (no fleet)?
> Operator IS present but may be elsewhere. Timeout-to-pause is safe. Timeout length: 5 min? 30? Per-severity? Open.

> [!question] Should `offer:` list have a minimum length enforced?
> 2 is proposed. 3 might force better thinking. 1 defeats the point. Open.

> [!question] Does this pattern promote to 04_principles after more validated instances?
> Currently seed/00_inbox. After verified implementation in at least one harness + 3+ instances with measurable cost-reduction vs no-pattern baseline, candidate for promotion to 03_validated. Principle promotion (04) would require derivation evidence across 3+ validated lessons converging on this as the mechanism.

### How This Connects — Navigate From Here

> [!abstract] From this pattern → related knowledge
>
> | Direction | Go To |
> |---|---|
> | **The principle this implements** | [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass\|Enforcement Must Be Mindful]] |
> | **What happens without this pattern** | [[agent-failure-taxonomy-seven-classes-of-behavioral-failure\|Agent Failure Taxonomy]] — Classes 3, 5, 6 all reduce to missing-escalation |
> | **Why structured form matters** | [[structured-context-governs-agent-behavior-more-than-content\|Structured Context Principle]] — schema > prose for compliance |
> | **Sibling enforcement patterns** | [[three-lines-of-defense-immune-system-for-agent-quality\|Three Lines of Defense]], [[harness-owned-loop-deterministic-agent-execution\|Harness-Owned Loop]] |
> | **How much escalation is right** | [[right-process-for-right-context-the-goldilocks-imperative\|Goldilocks Imperative]] — POC less, production more |

## Relationships

- DERIVED FROM: [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
- DERIVED FROM: [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
- DERIVED FROM: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
- BUILDS ON: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- RELATES TO: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
- RELATES TO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]

## Backlinks

[[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
[[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
