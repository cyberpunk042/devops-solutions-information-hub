---
title: Decision — Artifact System Design Decisions
aliases:
  - "Decision — Artifact System Design Decisions"
  - "Decision: Artifact System Design Decisions"
type: decision
domain: cross-domain
layer: 6
status: synthesized
confidence: high
maturity: growing
reversibility: moderate
derived_from:
  - "Methodology Artifact Taxonomy"
  - "Requirements and Design Artifacts — Standards and Guide"
  - "Construction and Testing Artifacts — Standards and Guide"
  - "Deployment, Closure, and Monitoring Artifacts — Standards and Guide"
created: 2026-04-12
updated: 2026-04-13
sources: []
tags: [methodology, decision, artifacts, templates, bridge-pattern, compliance, design]
---

# Decision — Artifact System Design Decisions
## Summary

Resolves 6 structural design questions about the methodology artifact system: requirements spec variants, interface spec separation, bridge pattern enforcement, scaffold self-checks, compliance automation, and completion log requirements. Each decision follows the principle: simplest mechanism at current scale with clear upgrade triggers.

## Decision

> [!success] 6 Decisions
>
> | # | Question | Decision | Trigger to Upgrade |
> |---|---------|----------|-------------------|
> | 1 | Requirements Spec variants (BRD/FRD/SRS)? | ONE template with scale-aware guidance sections | When regulated/compliance work requires formal SRS |
> | 2 | Interface Spec separate or in Tech Spec? | Section in Tech Spec by default, separate for complex epics | When interface exceeds 100 lines in the Tech Spec section |
> | 3 | Bridge pattern required or recommended? | RECOMMENDED for integration tasks, REQUIRED when interface mismatch detected | When integration violation rate exceeds 20% |
> | 4 | Scaffold self-check before /stage-complete? | YES — agent runs self-check BEFORE calling gate. Advisory, not blocking. | When harness exists, make it blocking |
> | 5 | Compliance reports automated? | YES — extend pipeline with basic compliance check (stage sequence + artifact existence) | When fleet operations need detailed compliance metrics |
> | 6 | Completion logs required or advisory? | REQUIRED for epic/module completions, ADVISORY for individual tasks | When harness automates them, make required for all |

## Alternatives

### Alt 1: Multiple Requirements Templates

> [!warning] Rejected: Too much overhead at current scale
>
> Creating separate BRD, FRD, and SRS templates would triple template maintenance. At current scale (solo operator, 2-3 active epics), one template with guidance comments ("For epics: include business context. For tasks: focus on FR/AC only.") achieves the same result with less friction. An SRS template becomes worthwhile when regulated or safety-critical work demands IEEE 830 compliance — that's not now.

### Alt 2: Always Separate Interface Spec

> [!warning] Rejected: Overhead for small tasks
>
> OpenArms separates Interface Spec from Tech Spec for every task. For a 20-line type definition, a separate document is overhead. The Interface Spec section in Tech Spec works for tasks and modules. For epics with 100+ lines of types across multiple modules, a separate document prevents the Tech Spec from becoming unwieldy. The 100-line threshold is the natural split point.

### Alt 3: Bridge Pattern Always Required

> [!warning] Rejected: Unnecessary when interfaces already match
>
> If the new module's interface already matches what the consumer expects, a bridge adds an unnecessary indirection layer. The bridge pattern solves interface MISMATCH — new module exports X but consumer needs Y. When X = Y, no bridge needed. Making it required would force a pass-through bridge that adds LOC without adding value.

### Alt 4: Compliance Reports as Manual Process

> [!warning] Rejected: Manual processes don't survive agent operation
>
> OpenArms learned this: "instruction-based enforcement has 75% failure rate." Manual compliance checks have the same problem — they depend on someone remembering to do them. Automated compliance checking, even basic (did the stage sequence match the model? do the required artifacts exist?), catches violations that manual review misses.

## Rationale

All 6 decisions follow the same principle: **simplest mechanism that solves the current problem, with documented trigger to upgrade.** This is the Pyramid quality tier applied to decisions — not the full Skyscraper where every possible variant and edge case is handled upfront, but deliberate compression with clear markers for when to expand.

Evidence:
- **Requirements Spec**: This wiki has produced requirements specs as concept pages for E003. One template worked. The scale-aware guidance comments were sufficient.
- **Interface Spec**: OpenArms's 24-artifact chain separates them for every task. But OpenArms tasks are larger (average L-XL). Wiki tasks are often S-M. Different scales, different separation needs.
- **Bridge pattern**: 5 instances in OpenArms integration sprint (T039-T047). All 5 were cases where the interface DIDN'T match. In 3 other integration tasks, no bridge was needed because interfaces aligned.
- **Scaffold self-check**: Reduces the "fix after gate fails" loop. Agent catches its own business-logic-in-scaffold BEFORE the gate command runs.
- **Compliance**: The 75% violation rate in OpenArms was only discovered by manual git log analysis. Automated detection would have caught it per-session.
- **Completion logs**: Epic/module completions aggregate knowledge that feeds lessons and patterns. Task-level completion logs for a 33-line task add more overhead than value — until a harness automates them.

## Reversibility

Moderate. Each decision can be reversed independently:
- Template split: add new templates, update scaffolder, migrate existing pages
- Spec separation: create new files, update references
- Bridge enforcement: change from recommended to required in CLAUDE.md
- Self-check: make advisory → blocking when harness exists
- Compliance: extend pipeline tool incrementally
- Completion logs: change from advisory → required in methodology config

No decision creates a one-way door.

## Dependencies

- Decisions 4-6 depend on tooling work (pipeline extensions, compliance checker, harness integration)
- Decisions 1-3 can be implemented immediately with template/CLAUDE.md changes only

> [!info] SDLC Chain Context
> This decision was calibrated for a solo operator with 2-3 active epics and no harness enforcement. At different chain levels:
> - **Simplified chain:** Decisions 4-6 (self-check, compliance, completion logs) are irrelevant — a simplified chain has no automated gates or compliance reporting. Only decisions 1-3 (templates, spec separation, bridge pattern) apply.
> - **Full chain:** All 6 decisions shift toward REQUIRED: separate templates per formality level, always-separate interface specs, mandatory bridge pattern, blocking self-checks, automated compliance reports, and required completion logs at every level.
> See [[sdlc-customization-framework|SDLC Customization Framework]] for chain details.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What taxonomy defines the artifacts?** | [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]] |
> | **What model does this inform?** | [[model-methodology|Model — Methodology]] |
> | **What standards does this feed?** | [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]] |
> | **Related decision: stage extensions** | [[methodology-stage-extension-decisions|Decision — Methodology Stage Extension Decisions]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
- DERIVED FROM: [[requirements-and-design-artifacts|Requirements and Design Artifacts — Standards and Guide]]
- DERIVED FROM: [[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
- DERIVED FROM: [[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[requirements-and-design-artifacts|Requirements and Design Artifacts — Standards and Guide]]
[[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
[[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]]
[[model-methodology|Model — Methodology]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
