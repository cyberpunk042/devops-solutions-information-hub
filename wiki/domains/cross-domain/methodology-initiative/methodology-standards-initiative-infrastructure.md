---
title: Methodology Standards Initiative — Infrastructure Analysis
aliases:
  - "Methodology Standards Initiative — Infrastructure Analysis"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: openarms-methodology
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms methodology.yaml configuration"
  - id: openarms-agents
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms project reference"
  - id: wiki-schema
    type: file
    file: wiki/config/wiki-schema.yaml
  - id: wiki-quality
    type: file
    file: wiki/config/quality-standards.yaml
tags: [methodology, infrastructure-analysis, artifact-system, agent-compliance, epic-planning]
---

# Methodology Standards Initiative — Infrastructure Analysis

## Summary

Complete mapping of the methodology and artifact infrastructure across the research wiki and its most evolved consumer (OpenArms). This analysis inventories every component — schemas, templates, exemplars, enforcement scripts, skills, validation tools — to establish what exists today before designing the target system. The research wiki has strong methodology *knowledge* (40+ pages, 15 spine models) but weak methodology *enforcement* (CLAUDE.md prose only). OpenArms has strong enforcement infrastructure (14 scripts, 4 hooks) but it's hardcoded and non-portable.

## Key Insights

1. **Two systems exist with complementary strengths** — the wiki has deep methodology *theory* (framework definition, model catalog, stage boundaries, quality tiers) while OpenArms has methodology *enforcement* (hooks, scripts, artifact verification, deterministic task dispatch). Neither is complete alone.

2. **Instruction-based enforcement has a 75% failure rate** — OpenArms tried v2-v8 of instruction-only stage boundary enforcement. Agents violated stage boundaries 75% of the time in overnight runs (2026-04-10). Infrastructure enforcement (hooks + scripts) in v9 solved this.

3. **The wiki has 14 page types but only 6 templates and 5 exemplars** — 8 page types (concept, source-synthesis, comparison, reference, deep-dive, epic, task, note) have no template. 9 types have no gold-standard exemplar. Agents creating these types operate without structural guidance.

4. **Artifacts are stage-ordered, model-dependent, and domain-adaptive** — a flat list of artifact types misrepresents the system. The real structure is: model selection → stage sequence → per-stage artifact requirements (multiple per stage) → dependencies on prior stage artifacts → domain-specific variations.

5. **Operations plans and design plans are conflated** — the methodology defines "plan" as an alias for design-only mode, but doesn't distinguish between a sequential operations checklist (deterministic, delegatable to a dumb agent) and a design plan (complex decisions, trade-offs, alternatives analysis). These are fundamentally different documents.

6. **The CLAUDE.md control surface lacks structural enforcement techniques** — OpenArms discovered that dividers, nesting, ALLOWED/FORBIDDEN lists, hard vs soft rule separation, and command-based checkpoints dramatically improve compliance. The wiki's CLAUDE.md is flat prose.

## Deep Analysis

### Existing Infrastructure — Research Wiki

> [!info] Research Wiki Component Inventory
>
> | Component | Count | Location | Quality |
> |-----------|-------|----------|---------|
> | Methodology concept pages | 7 | wiki/domains/devops/, cross-domain/ | Growing maturity, authoritative |
> | Spine models | 15 | wiki/spine/model-*.md | Growing-to-mature |
> | Standards pages | 7 | wiki/spine/model-*-standards.md | Seed-to-growing |
> | Page templates | 6 | wiki/config/templates/ | Skeleton only, no exemplars |
> | Schema definition | 1 | wiki/config/wiki-schema.yaml | Complete for structure |
> | Quality standards | 1 | wiki/config/quality-standards.yaml | Thresholds only |
> | Validation tooling | 1 | tools/validate.py | Page quality, not methodology |
> | Lint checks | 1 | tools/lint.py | Orphans, dead rels, thin pages |
> | Skills | 5 | skills/ | Operational, styling-aware |
> | Evolved pages (lesson/pattern/decision) | 47 | wiki/lessons/, patterns/, decisions/ | Most are exemplar-quality |

#### Schema Coverage

> [!abstract] Page Types vs Templates vs Exemplars
>
> | Page Type | Schema Sections | Template | Exemplar | Gap |
> |-----------|----------------|----------|----------|-----|
> | concept | Summary, Key Insights, Deep Analysis, Relationships | NO | YES (Methodology Framework) | Template missing |
> | source-synthesis | Summary, Key Insights, Relationships | NO | YES (Context Mode synthesis) | Template missing |
> | comparison | Summary, Comparison Matrix, Key Insights, Deep Analysis, Relationships | NO | NO | Both missing |
> | reference | Summary, Relationships | NO | NO | Both missing |
> | deep-dive | Summary, Key Insights, Deep Analysis, Relationships | NO | NO | Both missing |
> | lesson | Summary, Context, Insight, Evidence, Applicability, Relationships | YES | YES (CLI Tools Beat MCP) | Complete |
> | pattern | Summary, Pattern Description, Instances, When To Apply, When Not To, Relationships | YES | YES (SFIF) | Complete |
> | decision | Summary, Decision, Alternatives, Rationale, Reversibility, Dependencies, Relationships | YES | YES (MCP vs CLI) | Complete |
> | domain-overview | Summary, State of Knowledge, Maturity Map, Gaps, Priorities, Key Pages, Relationships | YES | NO | Exemplar missing |
> | evolution | Summary, Timeline, Key Shifts, Current State, Relationships | YES | NO | Exemplar missing |
> | learning-path | Summary, Prerequisites, Sequence, Outcomes, Relationships | YES | NO | Exemplar missing |
> | epic | Summary, Goals, Done When, Relationships | NO | NO | Both missing |
> | task | Summary, Done When | NO | NO | Both missing |
> | note | Summary | NO | NO | Both missing |
> | index | (none) | NO | NO | N/A — structural |

#### Methodology Pages (7 core)

All at "growing" maturity, "authoritative" confidence:

1. **model-methodology.md** (~2,000 words) — 9 named models, ALLOWED/FORBIDDEN lists, 7 real bugs traced. Missing: selection algorithm formalization, recovery procedures.
2. **model-methodology-standards.md** (~1,500 words) — Gold standard execution examples, anti-pattern gallery, checklists. Seed maturity — thinnest standards page.
3. **methodology-framework.md** (~1,500 words) — Meta-system: what a methodology model IS. Defines Model = Name + Stages + Gates + Protocols + Parameters. Missing: selection algorithm pseudo-code.
4. **stage-gate-methodology.md** (~1,000 words) — 5-stage system, universality beyond code, enforcement comparison. Missing: gate failure recovery.
5. **task-type-artifact-matrix.md** (~800 words) — 7 task types mapped to stages. Missing: decision tree for ambiguous types, 2 unresolved open questions.
6. **execution-modes-and-end-conditions.md** (~2,000 words) — 8 modes, 5 end conditions, 14-step work loop. Missing: end-to-end loop example, gate failure recovery.
7. **backlog-hierarchy-rules.md** (~1,000 words) — Epic/Module/Task hierarchy, 8 rules, anti-patterns. Missing: weighted readiness, status propagation algorithm.

### Existing Infrastructure — OpenArms (Most Evolved Consumer)

> [!info] OpenArms Enforcement Infrastructure
>
> | Component | Count | Purpose |
> |-----------|-------|---------|
> | methodology.yaml | 753 lines | 9 models, per-stage artifacts, protocols, harness config |
> | Enforcement scripts | 14 CJS | select-task, validate-stage, verify-done-when, recalculate-epic, etc. |
> | Hooks | 4 | pre-bash (block git), pre-write (block wrong-scope writes), post-write (track files), post-compact (rebuild instructions) |
> | Commands | 3 | /stage-complete, /task-done, /concern |
> | Stage skills | 5 | methodology-{document,design,scaffold,implement,test} |
> | Agent directives | 2 | Short form (83 lines), Long form (467 lines) |
> | Skill-stage mapping | 1 | 299-line YAML: 3 layers (generic, role, plugin) with restrictions |
> | Schema | 1 | 143 lines: page types, frontmatter, status lifecycle |
> | Modes config | 1 | 8 execution modes, 5 end conditions, ephemeral overrides |
> | Artifact spec | 1 | 705 lines: typed artifacts with verifiable properties |
> | Operational lessons | 20 | Embedded in AGENTS.md, each traced to a specific bug or date |

#### What OpenArms Proved (Hard Evidence)

> [!warning] Key Findings from OpenArms Autonomous Runs
>
> | Finding | Evidence | Implication |
> |---------|----------|-------------|
> | Instruction-based enforcement fails | 75% stage boundary violation rate, v2-v8 | Must use infrastructure (hooks, scripts) |
> | Agent fatigue is real | Quality cliff after 3-4 tasks (overnight 2026-04-10) | Session management required |
> | Readiness computation can't be instructed | Agents claimed 100% with incomplete work | Must be computed by scripts |
> | One task at a time | Showing 8 tasks causes rushing | Deterministic dispatch, hide backlog |
> | Specific Done When items work | Generic boilerplate lets agents cheat | Integration proof required |
> | Commit immediately after creating files | Bug 4: files lost to git revert | Stage-commit pattern |
> | Orphaned code is invisible | Bug 6: 2,073 lines nobody imports | Integration wiring artifact |

#### What's Hardcoded vs Portable

> [!abstract] Portability Assessment
>
> | OpenArms Component | Hardcoded | Portable Concept |
> |-------------------|-----------|------------------|
> | Stage names (document, design, scaffold, implement, test) | YES — TypeScript project | Stage-gated workflow pattern |
> | Gate commands (pnpm tsgo, pnpm check, pnpm test) | YES — pnpm/TypeScript | Per-stage gate command pattern |
> | File restrictions (src/ during document) | YES — src/ layout | Scope restriction per stage |
> | Artifact types (type_definition, zod_schema) | YES — TypeScript/Zod | Typed, verifiable artifact pattern |
> | Bridge module pattern | YES — integration pattern | Thin adapter pattern |
> | methodology.yaml structure | PARTIALLY — models are generic, artifacts are TS-specific | Model/stage/artifact hierarchy |
> | Skill-stage mapping | PARTIALLY — superpowers plugin specific | Layer-based skill injection |
> | Hook architecture | YES — Claude Code hooks format | Structural enforcement at tool boundaries |
> | Deterministic task selection | Generic | Hide backlog, dispatch one task |
> | Artifact-centric validation | Generic | Check deliverables, not behavior |
> | Hard vs soft rule separation | Generic | Infrastructure enforces hard, instructions guide soft |

### The Artifact Chain — What It Actually Is

The artifact chain is NOT a flat list. It is a **directed acyclic graph** where:

1. **Model selection** determines which stages apply (9 models × different stage subsets)
2. **Each stage** requires specific artifacts (multiple per stage)
3. **Artifacts have dependencies** on artifacts from prior stages
4. **Artifacts vary by domain** (TypeScript project ≠ wiki ≠ infrastructure ≠ research)
5. **Some artifacts are generic** (wiki page, gap analysis) and some are **domain-specific** (Zod schema, Dockerfile, test stub)

> [!abstract] Artifact Chain Structure
>
> ```
> Methodology Model (selected by task_type + conditions)
>   └── Stage Sequence (ordered, gated)
>         └── Per-Stage Artifacts (multiple, typed)
>               ├── Required artifacts (must exist to pass gate)
>               ├── Optional artifacts (exist if conditions met)
>               ├── Forbidden artifacts (must NOT exist — stage boundary)
>               └── Dependencies (prior stage artifacts that feed this one)
> ```

#### Feature Development Model — Full Chain Example

| Stage | Required Artifacts | Dependencies | Domain Variations |
|-------|-------------------|-------------|-------------------|
| Document | Requirements spec, Infrastructure analysis, Gap analysis | None | Wiki: wiki pages. Code: wiki pages about code. Infra: wiki pages about infra. |
| Design | ADR, Tech spec, Interface spec, Config spec, Test plan | All Document artifacts | Wiki: no interface spec. Code: TypeScript types. Infra: Terraform shapes. |
| Scaffold | Type definitions, Schema definitions, Test stubs, Config wiring | Interface spec, Test plan, Config spec | Wiki: template files. Code: .ts stubs. Infra: .tf stubs. |
| Implement | Business logic, Integration wiring, Bridge modules | Scaffold types, Tech spec | Wiki: content pages. Code: .ts functions. Infra: .tf resources. |
| Test | Test implementations, Test results (0 failures) | Test plan, Scaffold stubs | Wiki: pipeline post. Code: pnpm test. Infra: terraform plan. |

### Missing Document Types

> [!warning] Documents That Don't Exist Yet
>
> | Document Type | What It Is | Why It's Needed |
> |--------------|-----------|----------------|
> | **Operations plan** | Sequential todo list with validation steps. Deterministic. Delegatable to a dumb agent. | Currently conflated with "design plan." A dumb-agent checklist is NOT a design. |
> | **Methodology adaptation guide** | Per-project guide: "here's how to configure methodology.yaml for YOUR stack" | No project can adopt the methodology without manually figuring this out |
> | **Enforcement pattern catalog** | Reusable patterns for hooks, skills, validation scripts | OpenArms built these from scratch; next project would too |
> | **Agent compliance report** | Post-session analysis: which stages were followed, which were violated, which artifacts produced | No way to measure compliance today |
> | **CLAUDE.md structural patterns** | How to structure CLAUDE.md for maximum agent compliance | Discovered empirically, never documented |
> | **Exemplar annotations** | Annotated exemplars showing WHY each section/choice is good | Current exemplars show WHAT good looks like but not WHY |

## Open Questions

> [!question] ~~How do we handle domain-specific artifact variations without creating N copies of every template? (Requires: generic + override pattern desi~~
> **RESOLVED:** Generic template with domain-specific callout sections. One template, domain-aware content inside.gn)

> [!question] ~~What is the minimum viable enforcement infrastructure a new project needs? (Requires: analysis of OpenArms enforcement components — which ar~~
> **RESOLVED:** CLAUDE.md with MUST/MUST NOT + pipeline post as single gate. The simplified chain IS the minimum. Hooks/harness/immune are progressive layers.e essential vs nice-to-have)

> [!question] ~~Should operations plans be a new page type in the schema, or a subtype of an existing type?~~
> **RESOLVED:** Already a page type. operations-plan exists in wiki-schema.yaml with required_sections. (Requires: design decision after analyzing usage patterns)

> [!question] ~~How does the artifact chain handle composition — when a Feature Development task is nested inside an SFIF project lifecycle stage? (Requires~~
> **RESOLVED:** Preserve nesting as tree structure. Outer stage's artifacts include inner task's artifacts. Don't flatten.: recursive composition analysis)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- FEEDS INTO: [[methodology-framework|Methodology Framework]]
- FEEDS INTO: [[model-methodology|Model — Methodology]]
- BUILDS ON: [[stage-gate-methodology|Stage-Gate Methodology]]
- BUILDS ON: [[task-type-artifact-matrix|Task Type Artifact Matrix]]
- BUILDS ON: [[execution-modes-and-end-conditions|Execution Modes and End Conditions]]
- BUILDS ON: [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
- RELATES TO: [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
- RELATES TO: [[plan-execute-review-cycle|Plan Execute Review Cycle]]
- ENABLES: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]]

## Backlinks

[[methodology-framework|Methodology Framework]]
[[model-methodology|Model — Methodology]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[task-type-artifact-matrix|Task Type Artifact Matrix]]
[[execution-modes-and-end-conditions|Execution Modes and End Conditions]]
[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[E005-agent-compliance-framework|Agent Compliance Framework]]
[[E003-artifact-type-system|Artifact Type System]]
[[e003-artifact-type-system-design|E003 Artifact Type System — Design Document]]
[[e003-artifact-type-system-requirements|E003 Artifact Type System — Requirements Spec]]
[[methodology-standards-initiative-gaps|Methodology Standards Initiative — Gap Analysis]]
[[methodology-standards-initiative-honest-assessment|Methodology Standards Initiative — Honest Assessment]]
[[E004-portable-methodology-engine|Portable Methodology Engine]]
