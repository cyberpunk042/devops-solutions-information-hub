---
title: Methodology System Map
aliases:
  - "Methodology System Map"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-11
updated: 2026-04-13
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
> - **"Who am I? What do I need?"** → [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
> - **"How much process is right?"** → [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]]
> - **Need to understand methodology?** → Knowledge Layer tables below
> - **Need enforcement patterns?** → Agent Compliance section below (13 pages from solo hooks to fleet immune system)
> - **Need work management?** → Work Management section below (hierarchy, readiness/progress, PM levels)
> - **Need a config file?** → Configuration Layer table
> - **Need to know what tool validates what?** → Tooling Layer table
> - **Need all frontmatter fields?** → [[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]]
> - **Need to add something new?** → "How to Extend the System" section at the bottom
> - **Need a specific page?** → Ctrl+F / search this page — every methodology page is listed here
> - **Need to understand how context files compose across agent types?** → [[context-file-taxonomy|Context File Taxonomy — The 8 Dimensions of Agent Context]]

## Summary

Complete map of the methodology system — every component, where it lives, what it does, and how they connect. Use this page when you need to find something specific in the methodology, understand how pieces relate, or extend the system. This is the lookup table; [[model-methodology|Model — Methodology]] is the explanation.

## Reference Content

### The Four Layers

> [!info] How the Methodology System Is Organized
>
> | Layer | What It Contains | Purpose |
> |-------|-----------------|---------|
> | **Entry** (repo root) | README.md, AGENTS.md, CLAUDE.md + 5 thematic root docs | ORIENTATION — first contact for humans, AI tools, MCP clients |
> | **Knowledge** (wiki pages) | Models, standards, patterns, decisions, learning paths | UNDERSTANDING — teaches how methodology works |
> | **Configuration** (config files) | methodology.yaml, artifact-types.yaml, domain profiles, templates | EXECUTION — machines and agents read these |
> | **Tooling** (tools/) | validate.py, lint.py, pipeline.py scaffolder | ENFORCEMENT — checks compliance automatically |
>
> Entry orients the consumer. Knowledge defines WHAT and WHY. Configuration defines HOW (machine-readable). Tooling enforces COMPLIANCE. All four layers must agree — a rule in a wiki page that isn't in the config isn't enforced; a config rule without a wiki explanation isn't understood; a rule known to the system but absent from root docs isn't discoverable.

### Entry Layer — Root Documentation

> [!abstract] Repository-Level Docs (8 files, 2,714 lines)
>
> | File | What It Contains | Audience |
> |------|-----------------|----------|
> | [[root-documentation-map|Root Documentation Map]] | The spine navigation hub for all root docs | Anyone |
> | `README.md` | Project overview, what this IS, role-based entry | First visitor |
> | `AGENTS.md` | Universal cross-tool context (hard rules, stage gates, page schema) | Any AI tool (Claude, Codex, Copilot, Gemini, Cursor) |
> | `CLAUDE.md` | Claude-specific overrides (references AGENTS.md) | Claude Code |
> | `CONTEXT.md` | Identity profile, current state, active epics, constraints | Anyone understanding scope |
> | `ARCHITECTURE.md` | Data flow, tool topology, page schema, integration points | Anyone modifying structure |
> | `DESIGN.md` | Visual design principles, callout vocabulary, page layouts | Page creators |
> | `TOOLS.md` | Complete CLI reference (pipeline, gateway, view, sync, MCP) | Operators |
> | `SKILLS.md` | Skills catalog, SKILL.md format, extension hierarchy | Skill authors |
>
> These files implement the [[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]] pattern. They serve as the **discoverable front door** — `gateway query --docs` lists them, MCP `wiki_gateway_docs` tool exposes them, and every cross-tool AI starts here.

### Knowledge Layer — Wiki Pages

> [!abstract] Core Model Pages
>
> | Page | Lines | What It Explains |
> |------|-------|-----------------|
> | [[model-methodology|Model — Methodology]] | 850+ | The 9 models, stage gates, composition, quality tiers, adoption, compliance |
> | [[model-registry|Model Registry]] | 100+ | All 16 named models with status, standards, and maturity |
> | [[methodology-framework|Methodology Framework]] | 400+ | The META — what a model IS, selection, composition, adaptation, recursion |
> | [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]] | 440+ | Gold standards for execution with real examples and anti-patterns |

> [!abstract] Supporting Concept Pages
>
> | Page | What It Explains |
> |------|-----------------|
> | [[stage-gate-methodology|Stage-Gate Methodology]] | The 5 universal stages with ALLOWED/FORBIDDEN |
> | [[task-type-artifact-matrix|Task Type Artifact Matrix]] | Task type → model mapping |
> | [[execution-modes-and-end-conditions|Execution Modes and End Conditions]] | 8 modes, 5 end conditions, 14-step work loop |
> | [[backlog-hierarchy-rules|Backlog Hierarchy Rules]] | Epic → Module → Task hierarchy, 8 rules |
> | [[skyscraper-pyramid-mountain|Skyscraper, Pyramid, Mountain]] | Quality tier selection |

> [!abstract] Methodology Extension Pages
>
> | Page | What It Explains |
> |------|-----------------|
> | [[artifact-chains-by-model|Artifact Chains by Methodology Model]] | Full artifact chain for every model |
> | [[model-composition-rules|Model Composition Rules]] | Sequential, nested, conditional, parallel composition |
> | [[methodology-adoption-guide|Methodology Adoption Guide]] | 4-tier adoption from read to enforce |
> | [[methodology-evolution-protocol|Methodology Evolution Protocol]] | Evidence-driven versioned improvement |

> [!abstract] Artifact Taxonomy & Per-Category Standards
>
> | Page | What It Explains |
> |------|-----------------|
> | [[methodology-artifact-taxonomy-research|Synthesis — Methodology Artifact Taxonomy — Full Spectrum Research]] | Online research: 78 types from 10 sources |
> | [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]] | Complete 78-type reference across 11 categories |
> | [[initiation-and-planning-artifacts|Initiation and Planning Artifacts — Standards and Guide]] | 15 types: charters, WBS, risk, planning |
> | [[requirements-and-design-artifacts|Requirements and Design Artifacts — Standards and Guide]] | 17 types: BRD/FRD/SRS, ADR, tech spec, interface spec, test plan |
> | [[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]] | 15 types: per-domain scaffold/implement/test |
> | [[deployment-closure-monitoring-artifacts|Deployment, Closure, and Monitoring Artifacts — Standards and Guide]] | 17 types: operations, lessons, compliance |
> | [[ai-agent-artifacts|AI Agent Artifacts — Standards and Guide]] | 6 types: personas, skills, hooks, compliance |

> [!abstract] Per-Domain Artifact Chains
>
> | Page | Domain |
> |------|--------|
> | [[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]] | OpenArms, OpenFleet — pnpm, vitest, Zod |
> | [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]] | Research wiki — pipeline post, YAML configs |
> | [[domain-chain-infrastructure|Artifact Chain — Infrastructure-IaC Domain]] | devops-control-plane — Terraform, Docker |
> | [[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]] | Wiki evolution — L0-L6 progressive distillation |

> [!abstract] Agent Compliance Pages
>
> | Page | What It Explains |
> |------|-----------------|
> | [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]] | 8 formatting patterns that improve compliance (25%→60%) |
> | [[enforcement-hook-patterns|Enforcement Hook Patterns]] | 5-level enforcement hierarchy with OpenArms v10 + OpenFleet real implementation data |
> | [[stage-aware-skill-injection|Stage-Aware Skill Injection]] | Per-stage skill recommendations, mandatory, blocked |
> | [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]] | Quantified: instructions=25%, hooks=100%. 215 lines > 28 rules. |
> | [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]] | 6 behavioral classes that persist after infrastructure (20% clean rate) |
> | [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]] | Prevention → Detection → Correction. OpenFleet 3-line immune system. |
> | [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]] | Agent never controls loop, git, or backlog. OpenArms + OpenFleet instances. |
> | [[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]] | Cross-agent inputs collected BEFORE work — prevents rework |
> | [[tier-based-context-depth-trust-earned-through-approval-rates|Tier-Based Context Depth — Trust Earned Through Approval Rates]] | Trust earned through data, not configured. Controls context depth per tier. |
> | [[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]] | 29 scenarios testing structured context — unit testing for prompt engineering |
> | [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]] | All corrections lost after compaction — must rebuild via hooks |
> | [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]] | Every block needs a reason and a bypass mechanism |
> | [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]] | Markdown is the programming language of AI. Structure > content for compliance. |

> [!abstract] Principles (distilled from validated lessons — highest knowledge layer)
>
> | Principle | What It Governs |
> |-----------|----------------|
> | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] | HOW to enforce: infrastructure > instructions. Quantified from 5 converging lessons. |
> | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] | WHY it works: structure > content. Form programs behavior; prose requires parsing. |
> | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] | WHEN to apply: right process = f(identity, phase, scale, PM level). Adaptation, not dogma. |

> [!abstract] SDLC Framework
>
> | Page | What It Explains |
> |------|-----------------|
> | [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]] | Three dimensions: project phase (POC→Production), codebase scale (10k→15M), chain type (simplified/default/full) |
> | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] | 7 identity questions that determine chain, enforcement, and context depth |

> [!abstract] Per-Type Standards (15 docs in wiki/spine/standards/)
>
> | Type | Standards Doc |
> |------|--------------|
> | concept | [[concept-page-standards|Concept Page Standards]] |
> | source-synthesis | [[source-synthesis-page-standards|Source-Synthesis Page Standards]] |
> | comparison | [[comparison-page-standards|Comparison Page Standards]] |
> | reference | [[reference-page-standards|Reference Page Standards]] |
> | deep-dive | [[deep-dive-page-standards|Deep-Dive Page Standards]] |
> | lesson | [[lesson-page-standards|Lesson Page Standards]] |
> | pattern | [[pattern-page-standards|Pattern Page Standards]] |
> | decision | [[decision-page-standards|Decision Page Standards]] |
> | domain-overview | [[domain-overview-page-standards|Domain Overview Page Standards]] |
> | evolution | [[evolution-page-standards|Evolution Page Standards]] |
> | learning-path | [[learning-path-page-standards|Learning Path Page Standards]] |
> | operations-plan | [[operations-plan-page-standards|Operations Plan Page Standards]] |
> | epic | [[epic-page-standards|Epic Page Standards]] |
> | task | [[task-page-standards|Task Page Standards]] |
> | note | [[note-page-standards|Note Page Standards]] |
> | session-handoff (non-wiki genre) | [[session-handoff-standards|Session Handoff Standards]] |

> [!abstract] AI Agent Consumption & Elevation
>
> | Page | What It Explains |
> |------|-----------------|
> | [[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]] | 4 entry paths, 3 consumption modes, active vs passive, cross-project |
> | [[methodology-config-architecture|Methodology Config Architecture — How the Pieces Fit Together]] | 6-layer config stack reasoning, what each layer CAN/CANNOT enforce |
>
> **16 pages have AI Quick Start callouts** — 5-line actionable guides at the top of each methodology page
> **7 lessons have Self-Check sections** — 4 questions to ask BEFORE acting, preventing known failures

> [!abstract] Decisions Resolved
>
> | Page | What It Resolves |
> |------|-----------------|
> | [[artifact-system-design-decisions|Decision — Artifact System Design Decisions]] | 6 decisions: templates, interface spec, bridge pattern, scaffold checks, compliance, completion logs |
> | [[methodology-stage-extension-decisions|Decision — Methodology Stage Extension Decisions]] | 4 decisions: initiation stage, deploy stage, status reports, drift detection |

> [!abstract] Lessons Evolved the 2026-04-12 session
>
> | Page | What It Teaches |
> |------|----------------|
> | [[three-classes-of-methodology-output|Three Classes of Methodology Output]] | Artifact vs document vs documentation — different quality rules per class |
> | [[coverage-blindness-modeling-only-what-you-know|Coverage Blindness — Modeling Only What You Know]] | 100% of 20% = invisible incompleteness. Research outside your system. |
> | [[universal-stages-domain-specific-artifacts|Universal Stages, Domain-Specific Artifacts]] | Doc/design = universal. Scaffold/implement/test = domain-specific. |

> [!abstract] Work Management & Hierarchy
>
> | Page | What It Explains |
> |------|-----------------|
> | [[backlog-hierarchy-rules|Backlog Hierarchy Rules]] | 4-level hierarchy: Milestone → Epic → Module → Task. 8 impediment types. When to choose what. |
> | [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] | Readiness (is it defined?) vs Progress (is it built?). Two independent dimensions. 99→100 = human only. |
> | [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]] | L1: Wiki LLM. L2: Fleet/Harness. L3: Plane/DSPD. Each wraps the previous. |
> | [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Profile Selection]] | Three dimensions: project phase (POC→Production), scale (10k→15M), chain (simplified/default/full) |
> | [[task-type-artifact-matrix|Task Type Artifact Matrix]] | Task type → methodology model mapping |
> | [[execution-modes-and-end-conditions|Execution Modes and End Conditions]] | 8 modes, 5 end conditions, 14-step work loop |

> [!abstract] History & Learning
>
> | Page | What It Explains |
> |------|-----------------|
> | [[methodology-evolution-history|Evolution — Methodology System]] | How the system evolved from v1 to current |
> | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] | 24-page guided sequence in 6 parts for learning methodology |
> | [[methodology-standards-initiative-honest-assessment|Methodology Standards Initiative — Honest Assessment]] | Gap analysis of what's built vs what was asked for |

### Configuration Layer — Config Files

See [[wiki/config/README.md]] for the definitive thorough reference. Summary below.

> [!info] The 4 Config Layers (composition order)
>
> | Layer | Files | What It Does |
> |-------|-------|-------------|
> | **0 — Schema/Catalog** | wiki-schema.yaml, artifact-types.yaml, domains.yaml, quality-standards.yaml | Defines the UNIVERSE: valid page types, artifacts, domains, quality bars |
> | **1 — Methodology Definitions** | methodology.yaml | The 9 methodology models with stages + artifact chains (universal, base layer) |
> | **2 — Methodology Profiles** (NEW) | methodology-profiles/stage-gated.yaml, spec-driven.yaml, agile-ai.yaml, test-driven.yaml | Methodology STYLE overrides (emphasis, artifact preferences, signature practices). Where BMAD/SDD/TDD live. |
> | **3 — Domain Profiles** | domain-profiles/typescript.yaml, python-wiki.yaml, infrastructure.yaml, knowledge.yaml | Resolve generic artifacts to concrete paths + gate commands per domain |
> | **4 — SDLC Profiles** | sdlc-profiles/simplified.yaml, default.yaml, full.yaml | Project-level POLICY: which methodology profiles allowed, how strict |

> [!info] Config File Stack
>
> | File | Lines | What It Defines | Read By |
> |------|-------|----------------|---------|
> | `wiki/config/README.md` | ~830 | Thorough documentation of every config file + composition | Humans, agents starting fresh |
> | `wiki/config/methodology.yaml` | ~520 | 9 models with artifact chains + template hints, stages, modes, end conditions, quality tiers | Skills, agents, gateway, validators |
> | `wiki/config/methodology-profiles/stage-gated.yaml` | ~110 | Current default style (explicit) | Layer 2 runtime overlay |
> | `wiki/config/methodology-profiles/spec-driven.yaml` | ~130 | SDD/spec-kit style — specs as source of truth | Layer 2 runtime overlay |
> | `wiki/config/methodology-profiles/agile-ai.yaml` | ~155 | BMAD style — personas, party mode, brainstorming-first | Layer 2 runtime overlay |
> | `wiki/config/methodology-profiles/test-driven.yaml` | ~145 | TDD style — tests precede implementation | Layer 2 runtime overlay |
> | `wiki/config/artifact-types.yaml` | ~400 | 18 page types + 3 artifact classes, content thresholds, verification | validate.py, lint.py |
> | `wiki/config/domain-profiles/typescript.yaml` | ~60 | TypeScript/Node overrides: pnpm gates, src/ paths | Projects with TS codebases |
> | `wiki/config/domain-profiles/python-wiki.yaml` | ~135 | Python/wiki overrides: pipeline post gates, wiki/ paths | This wiki + similar |
> | `wiki/config/domain-profiles/infrastructure.yaml` | ~60 | IaC overrides: terraform gates, .tf paths | Infra projects |
> | `wiki/config/domain-profiles/knowledge.yaml` | ~100 | Pure knowledge projects (no code, only markdown) | Doc-only repos |
> | `wiki/config/sdlc-profiles/simplified.yaml` | ~75 | POC/micro policy — light enforcement | Policy layer |
> | `wiki/config/sdlc-profiles/default.yaml` | ~95 | MVP→Staging policy — stage gates enforced | Policy layer |
> | `wiki/config/sdlc-profiles/full.yaml` | ~110 | Production policy — full enforcement + immune system | Policy layer |
> | `wiki/config/wiki-schema.yaml` | ~240 | Frontmatter fields, enums, required sections, relationship verbs | validate.py, pipeline.py |
> | `wiki/config/quality-standards.yaml` | ~20 | Linting thresholds, export readiness, duplicate detection | lint.py |
> | `wiki/config/export-profiles.yaml` | ~90 | Export transforms for openfleet, AICP, methodology bundle | export.py |
> | `wiki/config/domains.yaml` | ~30 | Domain registry (names, folder paths) | All tools |
>
> **Composition order:** schema → methodology.yaml → methodology profile → domain profile → sdlc profile → project-local CLAUDE.md (highest precedence)

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
> 3. Document in [[model-methodology|Model — Methodology]] under "The Model Catalog"
> 4. Add artifact chain to [[artifact-chains-by-model|Artifact Chains by Methodology Model]]

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

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Principles** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] · [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] · [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **Identity** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[model-methodology|Model — Methodology]]
- BUILDS ON: [[methodology-framework|Methodology Framework]]
- RELATES TO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- RELATES TO: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[model-methodology|Model — Methodology]]
[[methodology-framework|Methodology Framework]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]]
[[gateway-tools-reference|Gateway Tools Reference — Complete Command Documentation]]
[[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]]
[[methodology-config-architecture|Methodology Config Architecture — How the Pieces Fit Together]]
[[identity-profile|Research Wiki — Identity Profile]]
[[session-handoff-standards|Session Handoff Standards]]
[[enforcement-hierarchy|Sub-Model — Enforcement Hierarchy — From Instructions to Immune System]]
[[goldilocks-protocol|Sub-Model — Goldilocks Protocol — Identity and Adaptation]]
[[integration-ecosystem|Sub-Model — Integration and Ecosystem — Dual-Perspective and Feedback]]
[[knowledge-architecture|Sub-Model — Knowledge Architecture — Layers, Maturity, and Evolution]]
[[work-management|Sub-Model — Work Management — Hierarchy, Tracking, and PM Levels]]
