---
title: "Consumer Integration Roadmap — OpenArms Exemplar (First Full Plan)"
aliases:
  - "Consumer Integration Roadmap — OpenArms Exemplar"
  - "Consumer Integration Roadmap"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: medium
maturity: growing
created: 2026-04-16
updated: 2026-04-16
sources:
  - id: openarms-integration-plan
    type: file
    project: openarms
    path: wiki/log/2026-04-16-second-brain-integration-notes.md
    description: "Parts 6 and 14-19 — OpenArms's own 5-milestone integration plan produced during first consumer integration. ~27-30 epics, ~150-200 tasks, 800-1200 hours."
  - id: integration-chain
    type: wiki
    file: wiki/spine/references/second-brain-integration-chain.md
  - id: adoption-guide
    type: wiki
    file: wiki/spine/references/methodology-adoption-guide.md
tags: [reference, integration, roadmap, milestones, adoption, consumer, exemplar, openarms]
---

# Consumer Integration Roadmap — OpenArms Exemplar (First Full Plan)

## Summary

The first concrete milestone-level plan for a consumer project integrating with the second brain. OpenArms produced this roadmap during its 2026-04-16 first consumer integration session after absorbing 16 models + standards + principles and identifying gaps against its existing methodology infrastructure. The plan decomposes full Tier 1 → Tier 4 adoption into 5 milestones totaling ~27-30 epics / 125-200 tasks / 800-1200 hours of sustained work. This page exists as an EXEMPLAR — what real scale looks like — not a prescription every consumer must follow. Each adopter will produce its own plan shaped by its phase, scale, and prior methodology investment. What transfers is the STRUCTURE: milestones as adoption tiers, epics as integration workstreams, tasks as specific knowledge absorption or code changes.

## Why This Page Exists

Before OpenArms's first integration, the adoption guide described four tiers abstractly: "Tier 1 is 1 hour, Tier 4 is 2-3 days." The guide implied graduated effort but never quantified it. OpenArms discovered the real scale: Tier 0 → Tier 2 in one session (partial), full Tier 1→4 adoption = **23-30 epics across months**. The gap between "one weekend" and "months" is too large to leave unstated. This exemplar fills that gap.

## The Exemplar — OpenArms 5-Milestone Plan

> [!abstract] Milestone → Epic → Task decomposition (OpenArms, 2026-04-16)
>
> | Milestone | Epics | Tasks (est.) | Prerequisite to |
> |---|---|---|---|
> | **M0: Foundation Alignment** | 4 | 15-25 | Everything — blocker for deeper integration |
> | **M1: Methodology Deepening** | 5 | 20-30 | Enforcement evolution, wiki evolution |
> | **M2: Enforcement Evolution** | 5 | 25-35 | Evolution pipeline (Tier 3) |
> | **M3: Wiki Evolution** | 5 | 30-40 | Hub integration (Tier 4) |
> | **M4: Knowledge Evolution Pipeline** | 4 | 20-30 | Hub integration |
> | **M5: Hub Integration** | 4 | 15-25 | None — terminal state |
> | **TOTAL** | **27** | **125-185** | **800-1200 hours** |

### M0 — Foundation Alignment (prerequisite to everything)

Fix the gaps between the consumer's current state and Tier 1+2 expectations. None of the deeper milestones can succeed until this is clean.

| Epic | Scope | What it produces |
|---|---|---|
| E-M0.1 | Fix schema compliance (validation violations against own schema) | Aligned required_sections OR aligned pages |
| E-M0.2 | CLAUDE.md/AGENTS.md restructure (<200 line target) | Lean routing file + companion rule files |
| E-M0.3 | Adopt task page standards (specific Done When, frontmatter completeness) | Updated task template, specific Done When in all new tasks |
| E-M0.4 | Adopt lesson page standards (for new lessons going forward) | Lesson template + contribution-format bridge verified |

**OpenArms M0 status as of 2026-04-16:** partial. Schema fixed (required_sections restructured). AGENTS.md restructured (471→124→144). Identity Profile declared. Lesson template not yet fully adopted (existing 16 lessons in old format; new ones going forward adopt).

### M1 — Methodology Deepening

Absorb the richer operational rules from the second brain's methodology into local configuration.

| Epic | Scope | What it produces |
|---|---|---|
| E-M1.1 | Adopt quality dimension (Skyscraper/Pyramid/Mountain explicit per task) | `quality_tier` field on tasks, selection guidance |
| E-M1.2 | Adopt model composition rules (sequential, nested, conditional, parallel) | Updated methodology.yaml with composition declarations |
| E-M1.3 | Adopt domain-specific artifact chains (e.g., TypeScript chain with 24 artifacts) | Enriched local chain config with stage-level required/forbidden |
| E-M1.4 | Adopt 8-class failure taxonomy (per-class tracking in post-run reports) | Post-run report template with 8-class metrics |
| E-M1.5 | Enrich methodology.yaml with ALLOWED/FORBIDDEN + gate commands | Stage rules queryable by harness |

**OpenArms M1 status:** minimal. Methodology v11.0 adds `progress` + `impediment_type` + Rule 8 warning — foundational but not the deeper rule absorption.

### M2 — Enforcement Evolution

Extend the prevention layer (Line 1 of Three Lines of Defense) from current breadth to second-brain-standard breadth.

| Epic | Scope | What it produces |
|---|---|---|
| E-M2.1 | Adopt R01-R13 guardrail hook patterns (expand from 4 hooks to 13 rules) | Expanded pre-bash + pre-write hooks covering 13 guardrail rules |
| E-M2.2 | Adopt Claude Code Standards (CLAUDE.md structure, skill quality bar, hook patterns) | Standards-compliant skills and hook organization |
| E-M2.3 | Implement Plannotator pattern (command+hook composition) | `/<command>` triggers skill + PreToolUse hook enforces constraints |
| E-M2.4 | Adopt context autocomplete chain (8-step context build from CLAUDE.md through post-compact) | Harness implements the full chain |
| E-M2.5 | Implement tier-based context depth in skill injection | Skills inject Expert/Capable/Lightweight context per task properties |

Tied to two contributed lessons: [[mandatory-without-verification-is-not-enforced|mandatory-as-gate]] and [[context-depth-must-vary-per-task-type-not-per-project|tier per task]]. Both extend Infrastructure > Instructions to subtler layers.

### M3 — Wiki Evolution

Bring the consumer's own wiki up to second-brain quality standards. This is the Tier 3 piece: evolution pipeline + maturity lifecycle.

| Epic | Scope | What it produces |
|---|---|---|
| E-M3.1 | Adopt LLM Wiki quality gates (summary length, relationship density, freshness) | Local pipeline post with same gates |
| E-M3.2 | Build wiki validation post-chain (consumer's own `pipeline post` equivalent) | Post-chain script validates pages + lint + indexes |
| E-M3.3 | Adopt wiki design standards (callout vocabulary, styling consistency) | Consistent use of callouts across 400+ pages |
| E-M3.4 | Add relationship density (from avg 1.0 to target 6.0 per page) | Systematic cross-linking pass across all pages |
| E-M3.5 | Adopt progressive distillation as a practice | raw → synthesis → concept → lesson → pattern → decision lifecycle |

### M4 — Knowledge Evolution Pipeline (Tier 3)

New capability — not extending existing infrastructure, building it from scratch. The evolution pipeline that scores, scaffolds, generates, validates, and promotes knowledge.

| Epic | Scope | What it produces |
|---|---|---|
| E-M4.1 | Build evolution scorer (6 signals, deterministic) | Scorer that ranks promotion candidates |
| E-M4.2 | Build maturity lifecycle for wiki pages (seed → growing → mature → canonical) | Maturity field + promotion gates |
| E-M4.3 | Build promotion pipeline with human review gate | `evolve --review` workflow |
| E-M4.4 | Add knowledge layer structure (L1-L6) | Layer field + promotion rules |

### M5 — Hub Integration (Tier 4)

Terminal state — consumer participates fully in the ecosystem.

| Epic | Scope | What it produces |
|---|---|---|
| E-M5.1 | Build export profiles for the second brain | Consumer exports its methodology+lessons+patterns to second brain via declared profile |
| E-M5.2 | Implement `MCP_CLIENT_RUNTIME` declaration | Per-session consumer identity declaration |
| E-M5.3 | Build bidirectional sync (contribute pipeline + import pipeline) | Changes flow automatically in both directions |
| E-M5.4 | Implement contribution gating for multi-agent work | Cross-agent inputs flow through structured contribution protocol |

## What Transfers to Other Consumers

> [!tip] Generalize the STRUCTURE; re-estimate the CONTENT per project
>
> | Element | Transferable | Per-project |
> |---|---|---|
> | Milestone count (5) | ✓ | — |
> | Milestone titles (Foundation → Methodology → Enforcement → Wiki → Evolution → Hub) | ✓ | — |
> | Dependency ordering (M0 is prerequisite to all) | ✓ | — |
> | Epic count per milestone | ~4-5 (rough) | Depends on prior investment |
> | Task count per epic | ~5-7 (rough) | Depends on scope and tech stack |
> | Total hours | ~800-1200 | Halves if project already at Tier 2+; doubles if still at Tier 0 |
> | Specific epic titles | Roughly transferable | Adapt to local tech stack (TypeScript vs Python etc.) |
> | Specific tasks | NOT transferable — always project-specific | — |

## Gate Criteria per Milestone

Each milestone should close only when a specific gate passes. These are the gates OpenArms declared (subject to revision as adoption progresses):

> [!abstract] Adoption Milestone Gates
>
> | Milestone | Gate |
> |---|---|
> | **M0** | `gateway compliance` shows Tier 2/4 with all three T1 and all three T2 items passing. Consumer's own `pipeline post` (if applicable) passes 0 errors. |
> | **M1** | Local methodology.yaml query returns artifact chains matching second brain structurally (content adapts per project). |
> | **M2** | Hooks cover all 13 R01-R13 guardrail patterns. Mandatory skills are GATED (verify invocation before stage close). |
> | **M3** | Consumer wiki health score ≥ target (70+). Average relationship density ≥ 6.0 per knowledge page. |
> | **M4** | At least one page promoted through full seed → growing → mature lifecycle with human review at each transition. |
> | **M5** | Second brain timeline shows bidirectional activity. Consumer exports flow automatically on commit. MCP_CLIENT_RUNTIME declared per session. |

## Key Observations from Exemplar Production

> [!warning] What OpenArms learned while producing this plan
>
> 1. **The plan is a BYPRODUCT of deep absorption, not a prerequisite for it.** OpenArms produced this plan AFTER reading 16 models, not before. Trying to plan adoption before understanding the system produces wrong milestones.
>
> 2. **Prior methodology investment compresses the plan significantly.** OpenArms had 5 months of prior work — M1 is partially done already for them. A greenfield consumer would not have that head start and M1 would take proportionally longer.
>
> 3. **Milestones are NOT sequential.** M3 and M4 can overlap for some epics. M5's `MCP_CLIENT_RUNTIME` can ship before M3 is complete. The milestone structure is a decomposition aid, not a strict ordering.
>
> 4. **Pure-capability milestones (M4) have different cost curves than alignment milestones (M0-M3).** Alignment milestones compress with prior investment. Pure-capability milestones (building a NEW pipeline) have a floor cost regardless of prior state.
>
> 5. **The "800-1200 hours" estimate is a ceiling, not a floor.** With focused effort, OpenArms achieved 15 adoption items in one session. But each one was a small piece of M0-M1. Full M4-M5 at this pace would still take months of sustained work.

## Self-Check for Adopters

> [!tip] Before building your own consumer integration roadmap
>
> 1. **Have you absorbed the second brain?** Read the super-model, the 16 models, the standards. If not, you'll plan wrong milestones.
>
> 2. **What tier are you currently at?** Run `gateway compliance` (with functional-equivalence fix) to know your baseline.
>
> 3. **What prior investment do you have?** A project at Tier 2 with mature methodology.yaml compresses M0-M1 significantly. A greenfield project does not.
>
> 4. **Do you have a harness, or are you solo?** Harness projects can parallelize some epics; solo projects do them serially.
>
> 5. **Do you have the time?** Honest estimate: 800-1200 hours for full Tier 1→4. If you can allocate 5 hours/week, that's 3+ years. If 40 hours/week, ~6 months. Most projects stop at Tier 2-3 and that is fine.

## How This Connects — Navigate From Here

> [!abstract] From This Exemplar → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The abstract adoption guide** | [[methodology-adoption-guide\|Methodology Adoption Guide]] |
> | **The step-by-step walkthrough** | [[second-brain-integration-chain\|Operations Plan — Second Brain Integration Chain]] |
> | **OpenArms's identity profile (full adoption log)** | [[identity-profile\|OpenArms — Identity Profile]] |
> | **The cost-curve lesson** | [[defense-layer-progression-is-expensive\|Defense Layer Progression Is Expensive]] |
> | **The pattern for enriching agent config** | [[progressive-structural-enrichment-in-agent-config\|Progressive Structural Enrichment in Agent Config]] |
> | **The underlying principle** | [[right-process-for-right-context-the-goldilocks-imperative\|Goldilocks]] — not every project needs every milestone |

## Relationships

- BUILDS ON: [[methodology-adoption-guide|Methodology Adoption Guide]]
- BUILDS ON: [[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain]]
- DERIVED FROM: [[identity-profile|OpenArms — Identity Profile]]
- RELATES TO: [[defense-layer-progression-is-expensive|Defense Layer Progression Is Expensive]]
- RELATES TO: [[progressive-structural-enrichment-in-agent-config|Progressive Structural Enrichment in Agent Config]]
- RELATES TO: [[right-process-for-right-context-the-goldilocks-imperative|Principle — Goldilocks]]
- FEEDS INTO: [[super-model|Super-Model]]

## Backlinks

[[methodology-adoption-guide|Methodology Adoption Guide]]
[[Operations Plan — Second Brain Integration Chain]]
[[identity-profile|OpenArms — Identity Profile]]
[[defense-layer-progression-is-expensive|Defense Layer Progression Is Expensive]]
[[progressive-structural-enrichment-in-agent-config|Progressive Structural Enrichment in Agent Config]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle — Goldilocks]]
[[Super-Model]]
