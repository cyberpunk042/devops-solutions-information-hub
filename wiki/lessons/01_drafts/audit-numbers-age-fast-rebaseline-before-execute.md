---
title: "Lesson — Audit numbers age fast: rebaseline before executing against an old audit"
aliases:
  - "Audit Numbers Age Fast"
  - "Rebaseline Before Execute"
  - "Stale-Audit Anti-Pattern"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: medium
maturity: growing
created: 2026-04-27
updated: "2026-05-09"
last_reviewed: "2026-05-09"
derived_from: []
sources:
  - id: aicp-skills-audit-2026-04-17
    type: project
    project: aicp
    path: docs/retros/RETRO-post-anthropic-2026-04-27.md
    description: "AICP Post-Anthropic mission retrospective (2026-04-27); original audit at decisions/00_inbox/skills-audit-2026-04-17.md"
  - id: aicp-handoff-skills-phase-2
    type: project
    project: aicp
    path: HANDOFF-SKILLS-PHASE-2-2026-04-27.md
    description: "Re-baseline discovery — original 47% no longer right unit by execution time"
  - id: principle-4
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
    description: "P4 — sister discipline; numbers are aspirational until re-measured"
tags: [contributed, lesson, audit, rebaseline, stale-data, planning, layer-4, contributed-from-aicp, p4-application]
contributed_by: "jfortin@WORKSTATION-JFM"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: "2026-04-27"
contribution_status: accepted
---

# Lesson — Audit numbers age fast: rebaseline before executing against an old audit

## Summary

Brain audits and retrospective metric reports report percentages at a specific time T (e.g., *"47% of skills are boilerplate against the standard"*). That number is true at T but ages quickly: (1) other workstreams may have silently chipped at the underlying problem; (2) the audit's diagnostic criteria may have evolved; (3) the codebase itself may have moved (refactors, deletions, additions). Six weeks later the number can be wrong by a substantial margin while still appearing in the decision document as a current fact. **Rebaselining at execution time is cheap (a single grep or count) and prevents weeks of work being framed against stale data.** Empirically validated 2026-04-17 → 2026-04-27 in AICP's skills audit: original *"47% of 78 skills boilerplate"* was correct at audit time but obsolete by execution time when 17 fleet-referenced skills already had Quality Bar coverage and only 26 needed gold-standard structure.

## Context

> [!info] **When this lesson applies**
>
> | Decision class | Apply this doctrine? |
> |---|---|
> | Plan execution against an audit / metric / baseline >2 weeks old | **YES** — rebaseline before executing |
> | Audit just authored (<2 weeks) | NO — figure is probably still good enough |
> | Long-running plan with rolling milestones | **YES** — rebaseline at each milestone start |
> | Skills / code coverage / dependency / technical-debt audits | **YES** — same pattern; the plan's scope + effort estimates depend on current state |
> | Hard infrastructure facts (vendor pricing, API quotas) | **YES** — pricing and quotas drift; rebaseline at execution |

## Insight

> [!tip] **Audit numbers are time-stamped facts that decay; the pattern + standards are durable, not the percentages.**
>
> The pattern + the standards are the durable artifact. The PERCENTAGES are time-stamped observations that decay as the work being measured continues. Plan-against-an-audit means: extract the pattern, NOT the percentage. The percentage is for the moment of decision; re-measure at execution.

## Evidence

> [!success]- **Evidence — AICP skills audit, 2026-04-17 (audit time) vs 2026-04-27 (execution time)**
>
> - **2026-04-17 (audit time)**: brain decision doc reported *"47% boilerplate against Extension Standards"* across 78 AICP skills. The percentage was correct at that time.
> - **Between 2026-04-17 and 2026-04-27**: in-flight work (driven by other concerns — feature additions, mid-session cleanup) silently eliminated boilerplate from many skills. Nobody re-counted.
> - **2026-04-27 (execution time)**: when the operator picked up Phase 2 of the audit-driven plan, a re-count revealed:
>   - 17 fleet-referenced skills already had Quality Bar coverage (tier-2)
>   - 26 fleet-referenced skills still needed the gold-standard structure
>   - The original *"47% of 78"* frame was no longer the right unit
> - **What the work actually was**: rewrite 26 specific skills to gold-standard pattern. NOT *"fix 47% boilerplate"*. The framing matters because the SCOPE estimate, the EFFORT estimate, and the MEASURABLE goal all change.
>
> The plan was directionally correct — boilerplate was real and the gold-standard pattern was the right answer. The number was misleading by execution time.

## Applicability

> [!info] **Decision matrix — when to rebaseline**
>
> | Audit age | Action |
> |---|---|
> | <2 weeks old | Probably still accurate; proceed |
> | 2-6 weeks old | Re-run measurement before execution; compare to audit |
> | >6 weeks old | Treat as historical context, not current state; full rebaseline required |
> | Audit driving plan execution | Rebaseline at each milestone start regardless of age |

## How to Apply

> [!tip] **In handoff documents and audit decisions:**
>
> 1. ALWAYS include the measurement command/query, not just the number.
> 2. Mark numbers with the time they were taken: *"47% as of 2026-04-17"*.
> 3. When picking up the plan later, re-run the measurement and update the number before executing.
>
> **In retrospectives that reference audit numbers:**
>
> - Always cite *"the figure at the time of the audit"* vs *"the figure at execution"* if both are known.
> - Treat divergence as data: it tells you something about the team's velocity on the underlying concern.

> [!warning] **What this is NOT**
>
> - Not *"audits are useless."* Audits are valuable for surfacing patterns; the pattern + the standards are the durable artifact, not the percentage.
> - Not *"always re-baseline."* For audits <2 weeks old, the figure is probably still good enough. The pattern matters specifically for plans being executed against older numbers.
> - Not specific to skills audits. Applies to any audit: code coverage, technical debt, dependency health, etc.

## Source

AICP Post-Anthropic mission retrospective (2026-04-27), `docs/retros/RETRO-post-anthropic-2026-04-27.md`. Original audit: `wiki/decisions/00_inbox/skills-audit-2026-04-17.md`. Re-baseline discovery: `HANDOFF-SKILLS-PHASE-2-2026-04-27.md` section 4.

## Relationships

- RELATES TO: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — sister discipline; numbers are aspirational until re-measured
- RELATES TO: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — the measurement command is infrastructure (re-runnable); the number is content (drifts)
- RELATES TO: [[fake-blockers-vs-real-blockers-empirical-verification-required|Fake Blockers vs Real Blockers]] — sister discipline; both require empirical verification before assumption

## Backlinks

[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[Fake Blockers vs Real Blockers]]
