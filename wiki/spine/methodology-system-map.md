---
title: "Methodology System Map"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-11
updated: 2026-04-12
sources:
  - id: methodology-config
    type: file
    file: wiki/config/methodology.yaml
  - id: artifact-types
    type: file
    file: wiki/config/artifact-types.yaml
tags: [methodology, system-map, reference, navigation, framework]
---

# Methodology System Map

> [!tip] AI Quick Start — This Is Your Navigation Hub
>
> - **Need to understand methodology?** → Knowledge Layer tables below
> - **Need a config file?** → Configuration Layer table
> - **Need to know what tool validates what?** → Tooling Layer table
> - **Need to add something new?** → "How to Extend the System" section at the bottom
> - **Need a specific page?** → Ctrl+F / search this page — every methodology page is listed here

## Summary

Complete map of the methodology system — every component, where it lives, what it does, and how they connect. Use this page when you need to find something specific in the methodology, understand how pieces relate, or extend the system. This is the lookup table; [[Model: Methodology]] is the explanation.

## Reference Content

### The Three Layers

> [!info] How the Methodology System Is Organized
>
> | Layer | What It Contains | Purpose |
> |-------|-----------------|---------|
> | **Knowledge** (wiki pages) | Models, standards, patterns, decisions, learning paths | UNDERSTANDING — teaches how methodology works |
> | **Configuration** (config files) | methodology.yaml, artifact-types.yaml, domain profiles, templates | EXECUTION — machines and agents read these |
> | **Tooling** (tools/) | validate.py, lint.py, pipeline.py scaffolder | ENFORCEMENT — checks compliance automatically |
>
> Knowledge defines WHAT and WHY. Configuration defines HOW (machine-readable). Tooling enforces COMPLIANCE. All three layers must agree — a rule in a wiki page that isn't in the config isn't enforced; a config rule without a wiki explanation isn't understood.

### Knowledge Layer — Wiki Pages

> [!abstract] Core Model Pages
>
> | Page | Lines | What It Explains |
> |------|-------|-----------------|
> | [[Model: Methodology]] | 600+ | The 9 models, stage gates, composition, quality tiers, adoption, compliance |
> | [[Methodology Framework]] | 400+ | The META — what a model IS, selection, composition, adaptation, recursion |
> | [[Methodology Standards — What Good Execution Looks Like]] | 440+ | Gold standards for execution with real examples and anti-patterns |

> [!abstract] Supporting Concept Pages
>
> | Page | What It Explains |
> |------|-----------------|
> | [[Stage-Gate Methodology]] | The 5 universal stages with ALLOWED/FORBIDDEN |
> | [[Task Type Artifact Matrix]] | Task type → model mapping |
> | [[Execution Modes and End Conditions]] | 8 modes, 5 end conditions, 14-step work loop |
> | [[Backlog Hierarchy Rules]] | Epic → Module → Task hierarchy, 8 rules |
> | [[Skyscraper, Pyramid, and Mountain]] | Quality tier selection |

> [!abstract] Methodology Extension Pages
>
> | Page | What It Explains |
> |------|-----------------|
> | [[Artifact Chains by Methodology Model]] | Full artifact chain for every model |
> | [[Model Composition Rules]] | Sequential, nested, conditional, parallel composition |
> | [[Methodology Adoption Guide]] | 4-tier adoption from read to enforce |
> | [[Methodology Evolution Protocol]] | Evidence-driven versioned improvement |

> [!abstract] Artifact Taxonomy & Per-Category Standards
>
> | Page | What It Explains |
> |------|-----------------|
> | [[Synthesis: Methodology Artifact Taxonomy — Full Spectrum Research]] | Online research: 78 types from 10 sources |
> | [[Methodology Artifact Taxonomy]] | Complete 78-type reference across 11 categories |
> | [[Initiation and Planning Artifacts — Standards and Guide]] | 15 types: charters, WBS, risk, planning |
> | [[Requirements and Design Artifacts — Standards and Guide]] | 17 types: BRD/FRD/SRS, ADR, tech spec, interface spec, test plan |
> | [[Construction and Testing Artifacts — Standards and Guide]] | 15 types: per-domain scaffold/implement/test |
> | [[Deployment, Closure, and Monitoring Artifacts — Standards and Guide]] | 17 types: operations, lessons, compliance |
> | [[AI Agent Artifacts — Standards and Guide]] | 6 types: personas, skills, hooks, compliance |

> [!abstract] Per-Domain Artifact Chains
>
> | Page | Domain |
> |------|--------|
> | [[Artifact Chain: TypeScript/Node Domain]] | OpenArms, OpenFleet — pnpm, vitest, Zod |
> | [[Artifact Chain: Python/Wiki Domain]] | Research wiki — pipeline post, YAML configs |
> | [[Artifact Chain: Infrastructure/IaC Domain]] | devops-control-plane — Terraform, Docker |
> | [[Artifact Chain: Knowledge/Evolution Domain]] | Wiki evolution — L0-L6 progressive distillation |

> [!abstract] Agent Compliance Pages
>
> | Page | What It Explains |
> |------|-----------------|
> | [[CLAUDE.md Structural Patterns for Agent Compliance]] | 8 formatting patterns that improve compliance |
> | [[Enforcement Hook Patterns]] | 4 hook types: scope guard, write guard, artifact tracker, context rebuilder |
> | [[Stage-Aware Skill Injection]] | Per-stage skill recommendations, mandatory, blocked |

> [!abstract] Per-Type Standards (15 docs in wiki/spine/standards/)
>
> | Type | Standards Doc |
> |------|--------------|
> | concept | [[Concept Page Standards]] |
> | source-synthesis | [[Source-Synthesis Page Standards]] |
> | comparison | [[Comparison Page Standards]] |
> | reference | [[Reference Page Standards]] |
> | deep-dive | [[Deep-Dive Page Standards]] |
> | lesson | [[Lesson Page Standards]] |
> | pattern | [[Pattern Page Standards]] |
> | decision | [[Decision Page Standards]] |
> | domain-overview | [[Domain Overview Page Standards]] |
> | evolution | [[Evolution Page Standards]] |
> | learning-path | [[Learning Path Page Standards]] |
> | operations-plan | [[Operations Plan Page Standards]] |
> | epic | [[Epic Page Standards]] |
> | task | [[Task Page Standards]] |
> | note | [[Note Page Standards]] |

> [!abstract] AI Agent Consumption & Elevation
>
> | Page | What It Explains |
> |------|-----------------|
> | [[How AI Agents Consume the Methodology Wiki]] | 4 entry paths, 3 consumption modes, active vs passive, cross-project |
> | [[Methodology Config Architecture — How the Pieces Fit Together]] | 6-layer config stack reasoning, what each layer CAN/CANNOT enforce |
>
> **16 pages have AI Quick Start callouts** — 5-line actionable guides at the top of each methodology page
> **7 lessons have Self-Check sections** — 4 questions to ask BEFORE acting, preventing known failures

> [!abstract] Decisions Resolved
>
> | Page | What It Resolves |
> |------|-----------------|
> | [[Decision: Artifact System Design Decisions]] | 6 decisions: templates, interface spec, bridge pattern, scaffold checks, compliance, completion logs |
> | [[Decision: Methodology Stage Extension Decisions]] | 4 decisions: initiation stage, deploy stage, status reports, drift detection |

> [!abstract] Lessons Evolved This Session
>
> | Page | What It Teaches |
> |------|----------------|
> | [[Three Classes of Methodology Output]] | Artifact vs document vs documentation — different quality rules per class |
> | [[Coverage Blindness — Modeling Only What You Know]] | 100% of 20% = invisible incompleteness. Research outside your system. |
> | [[Universal Stages, Domain-Specific Artifacts]] | Doc/design = universal. Scaffold/implement/test = domain-specific. |

> [!abstract] History & Learning
>
> | Page | What It Explains |
> |------|-----------------|
> | [[Evolution: Methodology System]] | How the system evolved from v1 to current |
> | [[Learning Path: Methodology Fundamentals]] | 8-page guided sequence for learning methodology |
> | [[Methodology Standards Initiative — Honest Assessment]] | Gap analysis of what's built vs what was asked for |

### Configuration Layer — Config Files

> [!info] Config File Stack
>
> | File | Lines | What It Defines | Read By |
> |------|-------|----------------|---------|
> | `wiki/config/methodology.yaml` | ~520 | 9 models with artifact chains + template hints, stages, modes, end conditions, quality tiers | Skills, agents, documentation |
> | `wiki/config/artifact-types.yaml` | ~390 | 17 page types + 3 artifact classes + categories, content thresholds, styling, verification | validate.py, lint.py |
> | `wiki/config/domain-profiles/typescript.yaml` | ~60 | TypeScript/Node overrides: pnpm gates, src/ paths, test patterns | Projects adopting methodology |
> | `wiki/config/domain-profiles/python-wiki.yaml` | ~135 | Python/wiki overrides: pipeline post gates, wiki/ paths, knowledge operations, real example | This wiki |
> | `wiki/config/domain-profiles/infrastructure.yaml` | ~60 | IaC overrides: terraform gates, .tf paths | Infra projects |
> | `wiki/config/wiki-schema.yaml` | ~240 | Frontmatter fields, enums, required sections per type, relationship verbs | validate.py, pipeline.py |
> | `wiki/config/quality-standards.yaml` | ~20 | Linting thresholds, export readiness, duplicate detection | lint.py |
> | `wiki/config/export-profiles.yaml` | ~90 | Export transforms for openfleet, AICP, methodology bundle | export.py |
>
> **Resolution order:** methodology.yaml → artifact-types.yaml → domain profile → wiki-schema.yaml

> [!info] Template Files (22 total)
>
> | Directory | Count | Types |
> |-----------|-------|-------|
> | `wiki/config/templates/` | 16 | All wiki page types (concept through operations-plan) |
> | `wiki/config/templates/methodology/` | 6 | Stage documents (requirements-spec, infra-analysis, gap-analysis, design-plan, tech-spec, test-plan) |
>
> Scaffold any template: `python3 -m tools.pipeline scaffold <type> "Title"`
> Scaffold methodology templates: `python3 -m tools.pipeline scaffold methodology/<name> "Title"`

### Tooling Layer — Validation & Enforcement

> [!info] What the Tools Check
>
> | Tool | What It Validates | Reads From |
> |------|------------------|-----------|
> | `tools/validate.py` | Frontmatter fields, enums, required sections, per-type content thresholds, styling requirements | wiki-schema.yaml + artifact-types.yaml |
> | `tools/lint.py` | Orphans, dead relationships, thin pages, stale pages, unstyled pages, filename hygiene, standards self-validation | quality-standards.yaml |
> | `tools/pipeline.py post` | Runs validate + lint + index rebuild + manifest + wikilinks | All config files |
> | `tools/pipeline.py scaffold` | Creates pages from templates | wiki/config/templates/ |

### How to Extend the System

> [!tip] Adding a New Methodology Model
>
> 1. Define the model in `wiki/config/methodology.yaml` under `models:` — name, stages, chain (required/forbidden/gate per stage)
> 2. Add model selection rule in `model_selection.by_task_type` or `overrides`
> 3. Document in [[Model: Methodology]] under "The Model Catalog"
> 4. Add artifact chain to [[Artifact Chains by Methodology Model]]

> [!tip] Adding a New Page Type
>
> 1. Add to `enums.type` in `wiki/config/wiki-schema.yaml`
> 2. Add `required_sections` in `wiki/config/wiki-schema.yaml`
> 3. Add type definition in `wiki/config/artifact-types.yaml`
> 4. Create template in `wiki/config/templates/<type>.md`
> 5. Create standards doc in `wiki/spine/standards/<type>-page-standards.md`
> 6. Add to scaffolder type_dirs in `tools/pipeline.py`
> 7. Update Per-Type Standards table in spine _index.md

> [!tip] Adding a New Domain Profile
>
> 1. Create `wiki/config/domain-profiles/<domain>.yaml` with stage_overrides
> 2. Define gate_commands, path_patterns, forbidden_zones per stage
> 3. Add to Methodology Adoption Guide per-domain quick start
> 4. Add to Domain Profile Resolution table in Artifact Chains page

## Relationships

- BUILDS ON: [[Model: Methodology]]
- BUILDS ON: [[Methodology Framework]]
- RELATES TO: [[Methodology Adoption Guide]]
- RELATES TO: [[LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Model: Methodology]]
[[Methodology Framework]]
[[Methodology Adoption Guide]]
[[LLM Wiki Standards — What Good Looks Like]]
[[Methodology Standards — What Good Execution Looks Like]]
[[How AI Agents Consume the Methodology Wiki]]
[[Methodology Config Architecture — How the Pieces Fit Together]]
