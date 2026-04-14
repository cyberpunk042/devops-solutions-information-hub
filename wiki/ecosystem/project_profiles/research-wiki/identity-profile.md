---
title: "Research Wiki — Identity Profile"
aliases:
  - "Research Wiki — Identity Profile"
type: reference
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-13
updated: 2026-04-13
sources:
  - id: wiki-claude-md
    type: file
    file: CLAUDE.md
  - id: wiki-stats
    type: file
    file: wiki/manifest.json
    description: "Wiki statistics: 300 pages, 2003 relationships (from tools.view)"
  - id: domain-chain-python-wiki
    type: wiki
    file: wiki/domains/cross-domain/methodology-artifacts/chains/domain-chain-python-wiki.md
tags: [ecosystem, project-profile, research-wiki, identity, goldilocks, self-referential]
---

# Research Wiki — Identity Profile

## Summary

The second brain's understanding of ITSELF as an ecosystem member. This profile is self-referential: the research wiki IS the second brain, and this page is the brain describing its own identity, role, and contribution to the ecosystem. The wiki is a research-grade knowledge synthesis system and central intelligence spine for the devops ecosystem (OpenFleet, AICP, devops-control-plane). At 300 pages and 2,003 relationships, it is the largest knowledge artifact in the ecosystem. Its primary contribution is the methodology framework itself — all models, standards, artifact chains, quality gates, and the knowledge architecture that the other projects consume.

## Identity (Goldilocks 7 Dimensions)

> [!info] Research Wiki Goldilocks Profile
>
> | Dimension | Value | Evidence |
> |-----------|-------|---------|
> | **Type** | system (framework + instance + second brain) | Both the methodology framework AND a running instance of it |
> | **Execution Mode** | Solo (human + Claude in conversation) | No harness, no loop. Operator directs, Claude executes, pipeline validates. |
> | **Domain** | Knowledge (Python/wiki tools) | Python tooling: pipeline, gateway, validate, lint, stats, view, export, sync |
> | **Phase** | Production | Used daily, 300+ pages, methodology consumed by ecosystem |
> | **Scale** | Medium (300 pages, growing) | 7 domains, 15 named models, 78 artifact types, 6-layer knowledge evolution |
> | **PM Level** | L1 (wiki backlog, CLAUDE.md directives, pipeline tools) | Backlog of epics, CLAUDE.md as routing table, pipeline post as gate |
> | **Trust Tier** | Operator-supervised | Human reviews all produced content |
> | **SDLC Chain** | Default (stage-gated with selected artifacts) | 5 stages, artifact chains, pipeline post validation |

## What Makes This Profile Unique

This is the only self-referential profile in the ecosystem. The research wiki:
- **Defines** the methodology framework (models, stages, chains, standards)
- **Implements** the methodology framework (its own pages follow its own rules)
- **Validates** the methodology framework (pipeline post enforces its own schema)
- **Exports** the methodology framework (other projects consume its CLAUDE.md patterns, methodology.yaml, templates)

The brain is both the map AND a territory on that map. When it describes "how to build a wiki page," it is also describing itself.

## What the Brain Learned FROM Itself

> [!tip] Key Lessons — Self-Generated
>
> | Lesson | What the Wiki Proved |
> |--------|---------------------|
> | [[schema-is-the-real-product|Schema Is the Real Product]] | YAML frontmatter + validation pipeline + manifest.json = the actual system. Pages are instances of the schema. |
> | [[models-are-systems-not-documents|Models Are Systems Not Documents]] | A model is a wiki page + standards page + companion pages + domain overviews + real evidence. Not a single document. |
> | [[standards-must-preach-by-example|Standards Must Preach By Example]] | A standards page that doesn't show a REAL instance of what "good" looks like teaches nothing. |
> | [[automated-knowledge-validation-prevents-wiki-decay|Automated Knowledge Validation Prevents Wiki Decay]] | pipeline post runs 6 steps: index → manifest → validate → obsidian → lint. Without automation, quality drifts. |
> | [[llm-maintained-wikis-outperform-static-documentation|LLM-Maintained Wikis Outperform Static Documentation]] | Cross-referencing, gap detection, evolution scoring — LLM capabilities that static docs can never have. |
> | [[multi-stage-ingestion-beats-single-pass|Multi-Stage Ingestion Beats Single-Pass]] | extract → cross-ref → gaps → deepen. Single-pass produces thin pages with missed connections. |
> | [[shallow-ingestion-is-systemic-not-isolated|Shallow Ingestion Is Systemic Not Isolated]] | When one page is thin, ALL pages from that session are thin. Fix the process, not the page. |
> | [[new-content-must-integrate-into-existing-pages|New Content Must Integrate Into Existing Pages]] | A new page with 0 inbound links is an orphan. Integration = relationships + backlinks + domain index. |
> | [[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks]] | Config with specific values is not a framework. Teach the meta-level. |
> | [[methodology-is-a-framework-not-a-fixed-pipeline|Methodology Is a Framework Not a Fixed Pipeline]] | 9 models, 3 SDLC chains, domain-specific artifact overrides. Not one-size-fits-all. |
> | [[three-classes-of-methodology-output|Three Classes of Methodology Output]] | Documents (constraining) vs Artifacts (by-products) vs Documentation (explaining). Each class has different quality bars. |
> | [[universal-stages-domain-specific-artifacts|Universal Stages, Domain-Specific Artifacts]] | Stages are the same everywhere. Artifacts differ by domain: TypeScript produces .ts types, Python produces YAML configs. |

> [!tip] Key Patterns — Self-Generated
>
> | Pattern | How the Wiki Implements It |
> |---------|--------------------------|
> | [[progressive-distillation|Progressive Distillation]] | L0 raw → L1 synthesis → L2 concept → L3 comparison → L4 lesson → L5 pattern → L6 decision. 6 layers. |
> | [[claude-md-structural-patterns|CLAUDE.md Structural Patterns]] | This wiki's own CLAUDE.md is the most evolved instance: identity profile, hard rules, methodology models, tooling, quality gates |
> | [[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop]] | Wiki learns from projects → distills to patterns → exports to projects → projects produce evidence → wiki learns |
> | [[plan-execute-review-cycle|Plan Execute Review Cycle]] | Every wiki change: understand → plan → execute → validate (pipeline post) → review |
> | [[context-aware-tool-loading|Context-Aware Tool Loading]] | Gateway queries adapt output based on --full, --domain, --chain flags |

## Artifact Chain (Project-Specific)

The wiki uses a 20-artifact Python/Wiki chain for Feature Development at the Default SDLC level.

> [!abstract] Research Wiki Feature Development Chain (Default SDLC)
>
> | Stage | Key Artifacts | Gate |
> |-------|---------------|------|
> | Document | Requirements spec, research notes (raw/notes/), gap analysis | Understanding before building |
> | Design | Design doc, decision page, spec | Approach approved |
> | Scaffold | YAML config additions, template .md files, empty stubs | `pipeline post` passes, no logic |
> | Implement | Python tool code, wiki pages with content, pipeline.py wiring | `pipeline post` 0 errors + `validate` 0 errors |
> | Test | pipeline post full run, lint check, manual review | 0 errors = done |

**Toolchain:** Python 3.12, YAML configs, Markdown wiki pages, pipeline/gateway/validate/lint/stats/view/export/sync tools

> [!warning] Chain Needs Refactoring
>
> The [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]] currently describes this chain but is tightly coupled to the research wiki's specific tooling. It needs refactoring to be generic enough for ANY Python/wiki project, with the research wiki as one specific instance. This is acknowledged technical debt.

See [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]] for the full chain and [[artifact-chains-by-model|Artifact Chains by Methodology Model]] for the generic framework.

## Methodology Adaptations

> [!info] How the Research Wiki Configures Its Own Methodology
>
> | Aspect | Framework Default | Research Wiki Instance |
> |--------|-------------------|----------------------|
> | Stage names | document→design→scaffold→implement→test | Same (the wiki DEFINES these names) |
> | Enforcement | Advisory or enforced | Pipeline post as universal gate — structural enforcement |
> | Evolved knowledge | Optional | Core feature: lessons/, patterns/, decisions/ with maturity folders (00_inbox → 04_principles) |
> | Knowledge layers | N/A | L0-L6 progressive distillation — unique to knowledge domain |
> | Models | 9 methodology models | All 9 defined here, plus 6 non-methodology models (15 total) |
> | SDLC chains | 3 (Simplified/Default/Full) | Operates at Default, defines all 3 |
> | Ingestion modes | N/A | auto/guided/smart — unique to knowledge operations |

## The Methodology Framework — What the Wiki Exports

The research wiki's primary export to the ecosystem is the methodology framework itself:

> [!abstract] Framework Components
>
> | Component | Location | What It Provides |
> |-----------|----------|-----------------|
> | 9 methodology models | wiki/config/methodology.yaml | Stage sequences, artifact chains, gates per task type |
> | 78 artifact types | wiki/config/artifact-types.yaml | Type definitions across 11 categories |
> | 3 SDLC chains | wiki/config/methodology.yaml | Simplified/Default/Full with readiness thresholds |
> | Page schema | wiki/config/wiki-schema.yaml | Frontmatter fields, valid values, validation rules |
> | Templates | wiki/config/templates/ | Per-type page scaffolds |
> | Domain chains | wiki/domains/cross-domain/methodology-artifacts/chains/ | Per-domain artifact resolution (TypeScript, Python/Wiki, Infrastructure, Knowledge) |
> | Standards | wiki/spine/standards/ | Per-type quality bars with section-by-section requirements |
> | 15 named models | wiki/spine/models/ | Research synthesis organized as navigable knowledge systems |
> | Gateway | tools/gateway.py | Unified query interface: identity, models, stages, chains, fields, mappings |

## Integration with Second Brain

> [!abstract] Adoption Status (Self-Integration)
>
> | Component | Status |
> |-----------|--------|
> | Three-layer root docs (AGENTS.md + CLAUDE.md + Skills) | Adopted 2026-04-14 — see [[root-documentation-map|Root Documentation Map]] |
> | CLAUDE.md as routing table | Adopted (107 lines, slimmed from 315) — references AGENTS.md |
> | 5 thematic root docs (CONTEXT/ARCHITECTURE/DESIGN/TOOLS/SKILLS) | Adopted 2026-04-14 — separation of concerns, discoverable via `gateway query --docs` |
> | methodology.yaml | Adopted (defines AND uses it) |
> | Stage enforcement | Adopted (pipeline post as universal gate) |
> | Wiki knowledge base | IS the knowledge base (317 pages, 2080 relationships) |
> | Export to other projects | Active (E002 defines interfaces; three-layer pattern now documented for ecosystem adoption) |
> | Feed-back FROM projects | Active (OpenArms: 22 lessons, OpenFleet: 5 patterns, devops-control-plane: 24 rules) |

### How This Connects — Navigate From Here

> [!abstract] From This Profile → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Ecosystem overview** | [[four-project-ecosystem|Four-Project Ecosystem]] |
> | **Super-model (brain overview)** | [[super-model|Research Wiki as Ecosystem Intelligence Hub]] |
> | **Model registry (all 16 models)** | [[model-registry|Model Registry]] |
> | **Methodology model** | [[model-methodology|Model — Methodology]] |
> | **Second brain model** | [[model-second-brain|Model — Second Brain]] |
> | **Ecosystem model** | [[model-ecosystem|Model — Ecosystem Architecture]] |
> | **Python/Wiki artifact chain** | [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]] |
> | **Generic artifact framework** | [[artifact-chains-by-model|Artifact Chains by Methodology Model]] |
> | **Methodology system map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- PART OF: [[four-project-ecosystem|Four-Project Ecosystem]]
- IMPLEMENTS: [[model-methodology|Model — Methodology]]
- RELATES TO: [[model-ecosystem|Model — Ecosystem Architecture]]
- RELATES TO: [[model-second-brain|Model — Second Brain]]
- RELATES TO: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
- RELATES TO: [[methodology-system-map|Methodology System Map]]
- FEEDS INTO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- FEEDS INTO: [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]]
- ENABLES: [[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]

## Backlinks

[[four-project-ecosystem|Four-Project Ecosystem]]
[[model-methodology|Model — Methodology]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[model-second-brain|Model — Second Brain]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[methodology-system-map|Methodology System Map]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]]
[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
