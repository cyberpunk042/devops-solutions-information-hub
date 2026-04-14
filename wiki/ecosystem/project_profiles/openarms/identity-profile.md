---
title: "OpenArms — Identity Profile"
aliases:
  - "OpenArms — Identity Profile"
type: reference
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-13
updated: 2026-04-13
sources:
  - id: openarms-claude
    type: file
    file: raw/articles/openarms-claude.md
  - id: openarms-v10
    type: wiki
    file: wiki/sources/ecosystem-projects/src-openarms-v10-enforcement.md
tags: [ecosystem, project-profile, openarms, identity, goldilocks]
---

# OpenArms — Identity Profile

## Summary

The second brain's understanding of OpenArms as an ecosystem member. OpenArms is a TypeScript/Node.js agent platform that evolved from a simple CLI tool through 10 methodology versions, proving that infrastructure enforcement works where instruction-based compliance fails. It is the most methodology-evolved project in the ecosystem and the primary source of enforcement lessons.

## Identity (Goldilocks 7 Dimensions)

> [!info] OpenArms Goldilocks Profile
>
> | Dimension | Value | Evidence |
> |-----------|-------|---------|
> | **Type** | product (agent platform) | CLI + agent run + provisioning + fleet dispatch |
> | **Execution Mode** | Harness v2 (enforced) | `agent run` wraps Claude in methodology loop with hooks + validation |
> | **Domain** | Backend API / Agent Platform (TypeScript/Node) | pnpm + tsgo + oxlint + vitest stack |
> | **Phase** | Production | Used daily, 93+ completed tasks |
> | **Scale** | Medium-Large (~50k LOC estimated) | Growing codebase with 8 execution modes |
> | **PM Level** | L2 (Harness) | methodology.yaml + agent-directive + task frontmatter + hooks |
> | **Trust Tier** | Capable (earned through 93 tasks, 9 methodology versions) | Auto-approval on routine operations |
> | **SDLC Profile** | Default → trending Full | Stage-gated with artifact requirements, hooks enforcing boundaries |

## Execution Mode History

> [!abstract] Evolution Path
>
> | Phase | Mode | What Changed |
> |-------|------|-------------|
> | v1-v3 | Solo → Harness v1 | Basic `agent run` loop, no enforcement |
> | v4-v6 | Harness v1 → v2 | Added methodology.yaml, stage validation, hooks |
> | v7-v9 | Harness v2 (maturing) | 4 hooks (pre-commit, pre-tool-use, pre-edit, post-session), MCP tool blocking |
> | v10 | Harness v2 (enforced) | 1033-line validator, 100% stage compliance, 6 behavioral failure classes remain |

## What the Brain Learned FROM OpenArms

These are cross-referenced to the wiki's lesson and pattern pages — the brain's distilled understanding, not OpenArms documentation.

> [!tip] Key Lessons Contributed
>
> | Lesson | What OpenArms Proved |
> |--------|---------------------|
> | [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]] | Instructions: 25% compliance → Hooks: 100% compliance |
> | [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]] | Even at 100% infrastructure enforcement, 6 behavioral failure classes persist (20% clean rate) |
> | [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful]] | T086: agent's correct fnm fix was blocked as "scope creep" — blind enforcement fails too |
> | [[harness-ownership-converges-independently-across-projects|Harness Ownership Converges Independently]] | OpenArms and OpenFleet independently evolved harness-owns-loop pattern |
> | [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]] | After compaction, prose corrections lost — structured state rebuilds from files |

> [!tip] Key Patterns Observed
>
> | Pattern | How OpenArms Implements It |
> |---------|--------------------------|
> | [[enforcement-hook-patterns|Enforcement Hook Patterns]] | 4 hooks: pre-commit (conventional), pre-tool-use (stage blocking), pre-edit (path guard), post-session (state save) |
> | [[stage-aware-skill-injection|Stage-Aware Skill Injection]] | Stage skills injected at each methodology stage with MUST/MUST NOT constraints |
> | [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]] | `agent run` wraps Claude in dispatch→execute→validate→advance loop |

## Artifact Chain (Project-Specific)

OpenArms uses a 24-artifact chain for Feature Development at the Default SDLC level. This is ONE instance of what could be 100+ artifacts at the Full level. See [[artifact-chains-by-model|Artifact Chains by Methodology Model]] for the generic framework.

> [!abstract] OpenArms Feature Development Chain (24 artifacts, Default SDLC)
>
> | Stage | Count | Key Artifacts | Gate |
> |-------|-------|---------------|------|
> | Document | 3 | Requirements spec, infrastructure analysis, gap analysis | FR items have Input/Output/Constraint |
> | Design | 5 | ADR, tech spec, interface spec, config spec, test plan | Types complete, ready for scaffold |
> | Scaffold | 5 | Type definitions (.ts), Zod schemas, test stubs, config wiring, env example | `pnpm tsgo` passes, no control flow |
> | Implement | 4 | Implementation, env reader, bridge module, integration wiring | `pnpm tsgo` + `pnpm check`, existing file modified |
> | Test | 2 | Test implementation, test results gate | `pnpm test` 0 failures |
> | Harness | 5 | Task frontmatter, git commits, epic readiness, completion log, compliance check | All gates passed |

**Toolchain:** pnpm, TypeScript (tsgo), oxlint/oxfmt, vitest, Zod, ESM

## Methodology Adaptations

> [!info] How OpenArms Customizes the Methodology
>
> | Aspect | Standard | OpenArms Override |
> |--------|----------|------------------|
> | Task types | 9 models | 7 models (no evolve, no documentation as standalone) |
> | Execution modes | 8 defined | agent-run, agent-provision, agent-heartbeat, agent-dispatch, interactive, plan, review, migrate |
> | Stage enforcement | Advisory (default profile) | Enforced (hooks block wrong-stage artifacts) |
> | Integration requirement | Not enforced | Every implement MUST modify an existing runtime file (Bug 6 prevention) |
> | Scaffold rules | No control flow | Strict: no if/for/while, max 3-line function bodies |

## Integration with Second Brain

> [!abstract] Adoption Status
>
> | Component | Status |
> |-----------|--------|
> | CLAUDE.md as routing table | Adopted (v10) |
> | Three-layer root docs (AGENTS.md + CLAUDE.md + Skills) | Not adopted — candidate upgrade (see [[root-documentation-map|Root Documentation Map]] for the wiki's implementation, ~400L CLAUDE.md is harmful per ETH Zurich research) |
> | methodology.yaml | Adopted (9 models, 7 task types) |
> | Stage hooks | Adopted (4 hooks) |
> | Wiki structure | Adopted (wiki/ folder with frontmatter) |
> | Export from second brain | Pending (E016 proved the chain) |
> | Feed-back TO second brain | Active (22 lesson files ingested the 2026-04-12 session) |

### How This Connects — Navigate From Here

> [!abstract] From This Profile → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Ecosystem overview** | [[four-project-ecosystem|Four-Project Ecosystem]] |
> | **Enforcement comparison** | [[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]] |
> | **Full synthesis source** | [[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]] |
> | **Generic artifact framework** | [[artifact-chains-by-model|Artifact Chains by Methodology Model]] |
> | **Methodology model** | [[model-methodology|Model — Methodology]] |

## Relationships

- PART OF: [[four-project-ecosystem|Four-Project Ecosystem]]
- DERIVED FROM: [[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]]
- RELATES TO: [[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- FEEDS INTO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]

## Backlinks

[[four-project-ecosystem|Four-Project Ecosystem]]
[[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]]
[[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]]
[[model-methodology|Model — Methodology]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
