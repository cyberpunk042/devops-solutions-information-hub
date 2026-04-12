---
title: "Evolution: Methodology System"
type: evolution
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: openarms-evolution
    type: file
    file: /home/jfortin/openarms/wiki/config/methodology.yaml
  - id: wiki-methodology
    type: file
    file: wiki/config/methodology.yaml
tags: [evolution, methodology, history, stage-gate, enforcement]
---

# Evolution: Methodology System

## Summary

How the methodology system evolved from prose instructions to infrastructure-enforced stage gates. Tracks the journey from OpenArms v1 (manual rules) through v9 (14 enforcement scripts + 4 hooks) and the research wiki's formalization into a portable methodology engine with artifact chains, domain profiles, and structural compliance patterns.

## Timeline

- **2026-04-01** — OpenArms v1: First CLAUDE.md with stage gate prose. Agents ignore most rules. (Significance: proof that the concept works even if enforcement doesn't)

- **2026-04-04** — OpenArms v2-v4: Iterative instruction refinement. Added ALLOWED/FORBIDDEN wording, readiness percentages, task hierarchy rules. Violation rate remains ~75%. (Significance: proved instruction-based enforcement has a ceiling)

- **2026-04-08** — Research Wiki created. First wiki pages about methodology as a concept rather than a project-specific config. Stage-gate methodology, task-type artifact matrix, execution modes documented as reusable knowledge.

- **2026-04-09** — OpenArms v5-v7: Bridge module pattern discovered during integration sprint (T039-T041). Agent created thin adapters 5 independent times. Pattern documented and recommended. (Significance: agents can discover patterns that should feed back into methodology)

- **2026-04-10** — OpenArms overnight run analysis. 75% stage boundary violation rate measured empirically. Key finding: agents violate scaffold→implement boundary most frequently (business logic in scaffold files). Decision: move enforcement from instructions to infrastructure. (Significance: the tipping point — evidence that instruction-based enforcement doesn't work)

- **2026-04-10** — OpenArms v8-v9: 14 CJS enforcement scripts, 4 hooks (pre-bash, pre-write, post-write, post-compact), 3 commands (/stage-complete, /task-done, /concern). Harness owns git, task selection, stage advancement. Agents see ONE task at a time. (Significance: infrastructure enforcement achieves ~90% compliance)

- **2026-04-11** — Research Wiki Methodology Standards Initiative launched. Four epics (E003-E006): Artifact Type System, Portable Methodology Engine, Agent Compliance Framework, Standards-by-Example. Generalized OpenArms's project-specific methodology into a portable, domain-agnostic system.

- **2026-04-11** — Artifact Type System complete. 17 wiki page types with templates, 10 stage artifact categories, artifact chains for all 9 models, 3 domain profiles (TypeScript, Python/wiki, Infrastructure), operations-plan as new page type, methodology.yaml as portable configuration.

- **2026-04-11** — CLAUDE.md restructured using 8 structural patterns (sacrosanct section, hard/soft rule separation, ALLOWED/FORBIDDEN tables, progressive disclosure, command checkpoints, section dividers, anchor phrases, concrete examples). This is the wiki eating its own cooking.

## Key Shifts

1. **Instructions → Infrastructure** — The most important shift. Telling agents what to do doesn't work at scale. Building systems that prevent violations does. This insight drives everything after v8.

2. **Project-specific → Portable** — OpenArms's methodology.yaml was hardcoded to TypeScript/pnpm. The research wiki generalized it into domain-agnostic models with domain profiles as the customization layer.

3. **Prose → Structured CLAUDE.md** — Flat narrative instructions get lost in context. Structural patterns (tables, ALLOWED/FORBIDDEN lists, dividers) create visual distinctiveness that survives context compaction.

4. **Types → Templates → Exemplars** — The progression from defining WHAT types exist (schema) to defining HOW each type is structured (templates) to showing WHAT good looks like (exemplars). Each layer builds on the previous.

5. **Single project → Ecosystem** — The methodology started as "how OpenArms agents work" and became "how any project's agents should work, configurable per domain."

## Current State

The methodology system is at v1.0 — first complete version with:
- 9 named models with full artifact chains
- 3 domain profiles (TypeScript, Python/wiki, Infrastructure)
- 17 page type templates with styling directives
- 8 CLAUDE.md structural patterns documented
- 4 enforcement hook patterns documented
- Stage-aware skill injection pattern documented
- Portable methodology.yaml exportable to consumer projects
- 4-tier adoption guide (Read → Configure → Validate → Enforce)
- Evolution protocol for versioned, evidence-driven improvement

**Next frontiers:**
- Model-methodology-standards.md elevation (seed → mature)
- Compliance reporting tooling
- Consumer project validation (OpenArms consuming the generic base)
- Additional domain profiles as new project types emerge

## Relationships

- BUILDS ON: [[Model: Methodology]]
- BUILDS ON: [[Stage-Gate Methodology]]
- RELATES TO: [[Methodology Evolution Protocol]]
- RELATES TO: [[Methodology Standards — What Good Execution Looks Like]]
- FEEDS INTO: [[Super-Model: Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[Model: Methodology]]
[[Stage-Gate Methodology]]
[[Methodology Evolution Protocol]]
[[Methodology Standards — What Good Execution Looks Like]]
[[Super-Model: Research Wiki as Ecosystem Intelligence Hub]]
