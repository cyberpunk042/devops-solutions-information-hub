---
title: Frontmatter Field Reference — Complete Parameter Documentation
aliases:
  - "Frontmatter Field Reference — Complete Parameter Documentation"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: wiki-schema
    type: file
    file: wiki/config/wiki-schema.yaml
  - id: artifact-types
    type: file
    file: wiki/config/artifact-types.yaml
  - id: operator-directive
    type: directive
    file: raw/notes/2026-04-12-readiness-progress-pm-levels-directive.md
    description: "Operator: 'its important that we have and explain all the field that is needed / suggested and enable advanced features and automations and control and observability'"
tags: [frontmatter, fields, reference, metadata, schema, parameters, documentation]
---

# Frontmatter Field Reference — Complete Parameter Documentation

> [!tip] AI Quick Start — Using This Reference
>
> 1. **Creating a page?** → Check Required Fields table below — all 9 must be present
> 2. **Creating a work item?** → Check Backlog Fields table — readiness + progress are TWO separate fields
> 3. **Page seems wrong?** → Check Enum Values — wrong type/status/maturity will fail validation
> 4. **Need advanced tracking?** → Check Optional Fields — impediment_type, blocked_by, depends_on enable automation
> 5. **What enables what?** → Every field has a "What It Enables" column — this is how automation hooks in

## Summary

Complete reference for every YAML frontmatter field used in the wiki. Every field is documented with: what it means, which page types require it, what values are valid, and what features or automations it enables. Frontmatter is not just metadata — it is the PROGRAMMATIC INTERFACE through which tools, agents, MCP servers, and the immune system read and act on page state. A field that exists but isn't documented is a field nobody will use correctly.

## Reference Content

### Required Fields (all page types)

> [!info] 9 Required Fields — Every Page Must Have These
>
> | Field | Type | Purpose | What It Enables |
> |-------|------|---------|----------------|
> | `title` | string | Human-readable page title. Must match `# Heading`. | Search, manifest index, wikilink resolution, display |
> | `type` | enum | Page classification. Determines template, required sections, quality thresholds. | Validation rules per type, scaffolder template selection, artifact-types.yaml lookups |
> | `domain` | string | Knowledge domain (ai-agents, devops, cross-domain, etc.). Must match folder path. | Domain index generation, domain health tracking, cross-domain relationship analysis |
> | `status` | enum | Lifecycle state. Different lifecycles for knowledge pages vs backlog items. | Status propagation (Rule 5), board state, dispatch eligibility, staleness detection |
> | `confidence` | enum | How reliable is this content? low→medium→high→authoritative. | Agents weight content by confidence. Low = "treat with skepticism." Authoritative = "trust as ground truth." |
> | `created` | date | ISO date (YYYY-MM-DD) when the page was first created. | Provenance tracking, age calculations |
> | `updated` | date | ISO date (YYYY-MM-DD) when the page was last meaningfully modified. | Staleness detection (lint checks pages not updated in 30 days), evolution scoring |
> | `sources` | list | Where the content came from. Each entry: id, type, file/url, description. | Provenance chain, depth verification, source-synthesis ratio checks |
> | `tags` | list | Freeform keywords for categorization and search. | Tag co-occurrence analysis, comparison candidate detection, search relevance |

### Knowledge Page Fields (optional, enhance quality tracking)

> [!info] Fields for Knowledge Pages (concept, source-synthesis, comparison, lesson, pattern, decision, etc.)
>
> | Field | Type | Used By | Purpose | What It Enables |
> |-------|------|---------|---------|----------------|
> | `layer` | int (1-6) | All knowledge pages | Knowledge evolution layer (L1 source → L6 decision) | Evolution pipeline scoring, layer gap detection |
> | `maturity` | enum | All knowledge pages | seed→growing→mature→canonical. How evolved is this? | Promotion eligibility, stale detection, dashboard maturity distribution |
> | `derived_from` | list | Evolved pages (lesson, pattern, decision) | Which pages was this distilled from? | Provenance chain, ensures lessons trace to evidence, evolution pipeline context |
> | `instances` | list | Patterns only | Concrete pages showing this pattern in action. ≥2 required. | Pattern validation (not a hypothesis if ≥2 instances), exemplar linking |
> | `reversibility` | enum | Decisions only | easy→moderate→hard→irreversible. How hard to undo? | Risk assessment, downstream impact analysis |
> | `complexity` | enum | Any | beginner→intermediate→advanced→expert. Content depth. | Learning path ordering, agent context filtering |
> | `subdomain` | string | Domain concepts | Sub-category within the domain. | Finer-grained organization within large domains |
> | `aliases` | list | Any | Alternative titles this page is known by. | Wikilink resolution for variant names, search |
> | `note_type` | enum | Notes only | directive→session→completion. Determines note structure. | Note template selection, log filtering |

### Backlog Fields (work items: milestone, epic, module, task)

> [!info] Fields for Work Management — Two-Dimensional Tracking
>
> | Field | Type | Used By | Purpose | What It Enables |
> |-------|------|---------|---------|----------------|
> | `readiness` | int (0-100) | All work items | **Definition completeness.** Is this READY to work on? Derived for containers. | Dispatch gating (can't start work until readiness threshold), honest progress reporting |
> | `progress` | int (0-100) | All work items | **Execution completeness.** How far is the WORK? Derived for containers. | Completion tracking, burndown, velocity calculation |
> | `priority` | enum | All work items | P0 (critical) → P3 (low). Determines dispatch order. | Task selection ordering, sprint planning, resource allocation |
> | `task_type` | enum | Tasks | epic/module/task/research/evolve/docs/bug/refactor. Determines methodology model. | Methodology model selection, stage sequence, artifact requirements |
> | `current_stage` | enum | Tasks | document→design→scaffold→implement→test. Where is this task in its stages? | Stage-gate enforcement, ALLOWED/FORBIDDEN rules, skill injection |
> | `stages_completed` | list | Tasks | List of completed stage names. | Readiness computation, stage ordering verification, artifact audit trail |
> | `artifacts` | list | Tasks | File paths produced per stage. | Traceability, artifact verification by validator, completion evidence |
> | `estimate` | enum | Tasks, Modules | XS→S→M→L→XL. Rough sizing. | Sprint planning, velocity tracking, decomposition guidance (XL = probably a module) |
> | `epic` | string | Modules, Tasks | Parent epic ID (e.g., "E003"). | Hierarchy linkage, readiness roll-up to parent |
> | `module` | string | Tasks | Parent module ID. | Hierarchy linkage |
> | `depends_on` | list | Any work item | IDs of items that must complete before this one. | Dependency tracking, dispatch ordering, blocked detection |

### Milestone Fields

> [!info] Fields Specific to Milestones
>
> | Field | Type | Purpose | What It Enables |
> |-------|------|---------|----------------|
> | `target_date` | date | When this milestone should be delivered. | Deadline tracking, overdue detection, timeline visualization |
> | `epics` | list | Epic IDs included in this milestone. | Milestone composition, readiness/progress derivation from children |
> | `acceptance_criteria` | list | Verifiable statements defining "done." | Human review gate, completion verification |

### Impediment Fields (any work item when blocked)

> [!info] Fields for Tracking Blockers
>
> | Field | Type | Values | Purpose | What It Enables |
> |-------|------|--------|---------|----------------|
> | `impediment_type` | enum | technical, dependency, decision, environment, clarification, scope, external, quality | What KIND of blocker is this? | Self-diagnosis (agent knows the response per type), pattern detection, escalation rules |
> | `blocked_by` | string | Task/issue ID | What specific item blocks this? | Dependency graph visualization, automatic unblock detection |
> | `blocked_since` | date | ISO date | When did the block start? | Duration tracking, escalation thresholds (e.g., 3 days → auto-escalate) |
> | `escalated` | bool | true/false | Has this been raised to a human? | Prevents duplicate escalation, tracks resolution ownership |
> | `resolution` | string | Free text | How was the impediment resolved? | Post-mortem patterns, impediment type effectiveness analysis |

### Enum Values Reference

> [!abstract] All Valid Enum Values
>
> | Enum | Values |
> |------|--------|
> | `type` | concept, source-synthesis, comparison, reference, deep-dive, index, lesson, pattern, decision, domain-overview, learning-path, evolution, operations-plan, milestone, epic, module, task, note |
> | `status` (knowledge) | raw → processing → synthesized → verified → stale |
> | `status` (backlog) | draft → active → in-progress → review → done → archived → blocked |
> | `confidence` | low → medium → high → authoritative |
> | `maturity` | seed → growing → mature → canonical |
> | `priority` | P0 → P1 → P2 → P3 |
> | `task_type` | epic, module, task, research, evolve, docs, bug, refactor |
> | `stage` | document → design → scaffold → implement → test |
> | `estimate` | XS → S → M → L → XL |
> | `note_type` | directive, session, completion |
> | `impediment_type` | technical, dependency, decision, environment, clarification, scope, external, quality |
> | `reversibility` | easy → moderate → hard → irreversible |
> | `complexity` | beginner → intermediate → advanced → expert |

### How Fields Connect to Automation

> [!warning] Fields Are Not Just Documentation — They Drive Behavior
>
> | Automation | Reads These Fields | What It Does |
> |-----------|-------------------|-------------|
> | `validate.py` | type, status, confidence, sources, all required fields | Rejects pages with missing or invalid fields |
> | `lint.py` | maturity, updated, relationships, summary length | Flags stale pages, thin pages, orphans |
> | `pipeline post` | type (for per-type thresholds), domain (for index), tags | Rebuilds indexes, validates, generates wikilinks |
> | `evolve --score` | maturity, derived_from, relationships, domain, layer | Scores evolution candidates by 6 signals |
> | Harness dispatch | readiness, progress, priority, depends_on, current_stage | Determines which task to dispatch next |
> | Immune system | current_stage, status, artifacts, readiness | Detects protocol violations, laziness, stuck tasks |
> | Readiness roll-up | readiness, progress (children → parent) | Computes container readiness from descendants |
> | Status propagation | status (children → parent) | Any child in-progress → parent in-progress |

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Principles** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] · [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] · [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **Identity** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[model-llm-wiki|Model — LLM Wiki]]
- BUILDS ON: [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
- RELATES TO: [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
- RELATES TO: [[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
- RELATES TO: [[methodology-system-map|Methodology System Map]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[model-llm-wiki|Model — LLM Wiki]]
[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]]
[[three-pm-levels|Three PM Levels — Wiki to Fleet to Full Tool]]
[[methodology-system-map|Methodology System Map]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[global-standards-adherence|Global Standards Adherence — Engineering Principles the Wiki Follows]]
