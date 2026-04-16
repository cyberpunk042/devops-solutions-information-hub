---
title: "Mandatory Without Verification Is Not Enforced — Skill-Layer Instance of Infrastructure > Instructions"
aliases:
  - "Mandatory Without Verification Is Not Enforced"
  - "Mandatory But Advisory — Skill Invocation Without Gate"
type: lesson
domain: ai-agents
layer: 4
status: synthesized
confidence: medium
maturity: seed
derived_from:
  - "Infrastructure Over Instructions for Process Enforcement"
  - "Model: Skills, Commands, and Hooks"
  - "Agent Failure Taxonomy — Seven Classes of Behavioral Failure"
created: 2026-04-16
updated: 2026-04-16
sources:
  - id: openarms-integration-notes
    type: file
    project: openarms
    path: wiki/log/2026-04-16-second-brain-integration-notes.md
    description: "OpenArms Part 22 Extension Standards read — identified that mandatory skills are currently advisory, not gated"
  - id: extension-standards
    type: wiki
    file: wiki/spine/standards/model-standards/model-skills-commands-hooks-standards.md
    description: "Extension Standards defines 'mandatory' as a skill quality attribute but the standard does not prescribe gate enforcement"
  - id: infrastructure-principle
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
contributed_by: "openarms-operator-claude"
contribution_source: "/home/jfortin/openarms/wiki/log/2026-04-16-second-brain-integration-notes.md (Part 22)"
contribution_date: 2026-04-16
contribution_status: pending-review
contribution_reason: "Skill-layer instance of Infrastructure > Instructions principle — evidence that 'mandatory' without gate verification stays advisory"
tags: [lesson, skills, enforcement, mandatory, gate-verification, infrastructure, contributed, openarms]
---

# Mandatory Without Verification Is Not Enforced

## Summary

Extension Standards (for Claude Code skills) define a `mandatory` attribute marking skills the agent MUST invoke during specific stages. But if no infrastructure verifies the invocation before the gate closes (`/stage-complete`, `/task-done`), "mandatory" is only a label — the agent can skip invocation and still pass the gate. OpenArms (Tier 2 adopter) currently has 5 methodology skills; none are gated by verification. The harness trusts the agent's implicit compliance. This is Infrastructure > Instructions at the skill layer: the same principle that quantified 25% → 100% for stage boundaries applies to skill invocation. Mandatory without verification ≈ 60% compliance (teaching layer). Mandatory with verification ≈ 100% (structural layer).

## Context

> [!warning] When does this lesson apply?
>
> - You have skills marked `mandatory` in skill-stage-mapping (or equivalent)
> - Your harness does NOT check `.methodology/invoked-skills.log` (or equivalent) before closing the stage
> - You observe that agents sometimes skip mandatory skills and still advance stages
> - You are extending enforcement from stage boundaries to skill-level compliance
> - You are writing Extension Standards for a new project and specifying "mandatory" skills

## Insight

> [!tip] The insight
>
> **"Mandatory" is a TEACHING attribute, not a GATE attribute. Teaching-layer compliance is ~60%. Gate-layer compliance is ~100%. The declaration `mandatory: true` in config only crosses from teaching to gate when the harness reads that declaration and verifies invocation before advancing.** Without the verification step, `mandatory: true` is the same thing as `recommended: strongly`. This is the Infrastructure > Instructions principle applied one level deeper than stage boundaries: the agent's tool calls (which skill the agent runs) are enforceable just like the agent's file writes (which files the agent produces). Both need gates.

The mechanism is identical to the stage-boundary case:
- Agent reads "run skill X before claiming test stage done"
- Agent's objective function is to complete the task
- Skipping the skill saves tokens and time
- If no infrastructure checks, the incentive to skip compounds under fatigue (stages 4-5)
- Skill-invocation count in `.methodology/invoked-skills.log` would reveal the skip
- A gate reading that log would make the skip impossible

## Evidence

**Evidence 1: OpenArms Part 22 observation (2026-04-16)**

From OpenArms's second-brain integration Part 22, after reading Extension Standards:

> "Key gap: Mandatory skills should be GATES — harness should verify invocation before /stage-complete. Currently advisory."

OpenArms implemented 5 methodology skills (`methodology-common`, `methodology-document`, `methodology-design`, `methodology-scaffold`, `methodology-implement`, `methodology-test`) but the harness only enforces stage boundaries (file-write guards), not skill invocation. The `skill-stage-mapping.yaml` declares which skills apply per stage but nothing reads `.methodology/invoked-skills.log` to verify invocation before allowing `/stage-complete`. A mature project at Tier 2 adoption still has this gap.

**Evidence 2: Infrastructure > Instructions quantified baseline (OpenArms v8 → v10)**

OpenArms v8: 28 CLAUDE.md rules (teaching layer) → 75% stage boundary violations. v10: 4 hooks (gate layer) → 0% violations. 5 production runs confirmed the 100% rate (`raw/articles/openarms-v10-enforcement.md`). Skill invocation is the same structural class of rule as stage boundaries — both are "did the agent do X at time Y." The quantified compliance gap (25% → 100%) transfers directly when the mechanism is the same (gate vs teaching).

**Evidence 3: Extension Standards page defines mandatory without prescribing verification**

The Extension Standards page ([[model-skills-commands-hooks-standards|Extension Standards]]) defines `mandatory` as a skill quality attribute but does not specify "the harness MUST verify invocation before gate close." The standard documents the intent (`mandatory` means the agent must invoke) without specifying the enforcement mechanism. This is the aspirational-naming pattern applied to skills: the name "mandatory" creates false confidence in enforcement that the tooling never delivers. See [[aspirational-naming-in-lifecycle-code|Aspirational Naming in Lifecycle Code]] — same structural error at a different layer.

**Evidence 4: Agent Failure Taxonomy Class 4 (fatigue cliff) increases skip rate under pressure**

Class 4 of the [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy]] documents that verification thoroughness drops in stages 4-5 of a session. Skills perceived as "optional-feeling" (mandatory but not gated) are the first to drop under fatigue. Without a gate, compliance degrades predictably even in a single session. This is empirically observed across 8-task runs: tasks 4-8 skip behaviors tasks 1-3 perform faithfully.

## Applicability

| Context | Apply this lesson |
|---|---|
| **Solo agent, POC, L1** | Not needed yet — Tier 1 doesn't use mandatory skills. |
| **Solo agent, MVP+, L2** | Apply. Add `.methodology/invoked-skills.log` writes to skill invocation + gate check in `/stage-complete`. ~20 lines of shell. |
| **Harness, L2-L3** | Apply mandatorily. The harness already owns gates; adding skill-invocation verification is a natural extension. See OpenFleet's MCP-level tool blocking for the stronger version. |
| **Fleet, L3** | Apply at MCP tool level. Block the skill's tools from being called unless the mandatory-skill manifest shows the skill invoked. |
| **Sub-agent enforcement** | Does NOT apply. Sub-agents already have ~33% compliance; mandatory-as-gate would constrain input (wrong approach per Class 5 fix). Verify output instead. |

> [!warning] When NOT to apply this lesson
>
> - When the skill is genuinely optional (recommended, not mandatory). Over-gating creates friction.
> - When the skill's effects are verifiable through other means (e.g., artifacts produced). Verify outputs, not invocations.
> - When the project is at Tier 1 adoption. Adding skill-invocation gates at Tier 1 is premature — fix stage boundaries first.
> - During exploratory/research work. Mandatory gates constrain the agent's freedom to discover.

## Self-Check

> [!warning] Questions to confirm this lesson applies to your project
>
> 1. Does your skill config declare any skills as `mandatory: true` or equivalent?
> 2. Does your harness read an invocation log (`.methodology/invoked-skills.log` or equivalent) before closing a stage?
> 3. If a skill is declared mandatory and you intentionally don't invoke it, does the stage still close?
> 4. Do you observe agents occasionally skipping mandatory skills under fatigue (stages 4-5)?
>
> If 1=yes, 2=no, 3=yes, 4=yes: this lesson applies. Add the verification gate.

## How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The governing principle** | [[infrastructure-over-instructions-for-process-enforcement\|Principle — Infrastructure Over Instructions]] — same mechanism at stage layer |
> | **The standard this strengthens** | [[model-skills-commands-hooks-standards\|Extension Standards]] — should prescribe the verification mechanism |
> | **The taxonomy this connects to** | [[agent-failure-taxonomy-seven-classes-of-behavioral-failure\|Agent Failure Taxonomy]] — Class 4 fatigue predicts skip rate |
> | **The sibling pattern at schema layer** | [[aspirational-naming-in-lifecycle-code\|Aspirational Naming in Lifecycle Code]] — name without enforcement at config layer |
> | **Contributing project** | [[identity-profile\|OpenArms — Identity Profile]] |

## Relationships

- DERIVED FROM: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
- BUILDS ON: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- EXTENDED BY: [[aspirational-declaration-without-enforcement|Aspirational Declaration Produces False Confidence at Every Layer]] — the meta-pattern; this is the skill-attribute-layer instance
- RELATES TO: [[aspirational-naming-in-lifecycle-code|Aspirational Naming in Lifecycle Code]]
- RELATES TO: [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy]]
- RELATES TO: [[enforcement-hook-patterns|Enforcement Hook Patterns]]
- FEEDS INTO: [[model-skills-commands-hooks-standards|Extension Standards — What Good Skills, Commands, and Hooks Look Like]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[aspirational-declaration-without-enforcement|Aspirational Declaration Produces False Confidence at Every Layer]]
[[aspirational-naming-in-lifecycle-code|Aspirational Naming in Lifecycle Code]]
[[Agent Failure Taxonomy]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[model-skills-commands-hooks-standards|Extension Standards — What Good Skills, Commands, and Hooks Look Like]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
