---
title: Global Standards Adherence — Engineering Principles the Wiki Follows
aliases:
  - "Global Standards Adherence — Engineering Principles the Wiki Follows"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: operator-directive
    type: directive
    file: raw/notes/2026-04-12-goldilocks-higher-ground-directive.md
    description: "Operator: 'adhering as much as global norms a bit like the cloudevents principle, openAPI and stuff like this'"
tags: [standards, global-norms, engineering-principles, design-patterns, ddd, sfif, srp, oop, openapi, cloudevents]
---

# Global Standards Adherence — Engineering Principles the Wiki Follows

## Summary

The wiki and its methodology framework adhere to recognized engineering standards — not by copying them wholesale, but by applying their principles to the AI agent domain. CloudEvents principles for structured events. OpenAPI principles for machine-readable interfaces. Domain-Driven Design for bounded contexts. SFIF for build lifecycle. Onion Architecture for layer isolation. SRP for component responsibility. OOP design patterns for behavioral composition. Every component in the framework can trace its design to one or more recognized standard. Projects consuming the wiki inherit these standards through the configs, templates, and patterns they adopt.

## Key Insights

1. **Standards are applied, not adopted verbatim.** CloudEvents defines structured event attributes (type, source, id). We don't use CloudEvents directly — we apply the PRINCIPLE (typed, structured, machine-parseable) to frontmatter fields, hook responses, and context injections. The standard teaches the principle; we implement the principle in our domain.

2. **Each wiki component maps to at least one recognized standard.**

> [!abstract] Standards Mapping
>
> | Wiki Component | Standard Applied | How |
> |---------------|-----------------|-----|
> | **Frontmatter fields** | CloudEvents (typed structured attributes) | Every field has: name, type, valid values, what automation reads it. Machine-parseable. |
> | **Gateway tools API** | OpenAPI (machine-readable interface specification) | Gateway operations should be documented as structured interface specs. Any tool/MCP/human can consume them. |
> | **Domain folders** | DDD bounded contexts | Each domain (ai-agents, devops, knowledge-systems) is a bounded context with its own vocabulary and ownership. Cross-domain is the shared kernel. |
> | **Enforcement layers** | Onion Architecture | Inner layers (agent) don't know about outer layers (hooks, doctor). Each layer has one dependency direction: inward. |
> | **Maturity folders** | Progressive maturity / CMMI levels | 00_inbox → 01_drafts → 02_synthesized → 03_validated → 04_principles. Each level has specific promotion criteria. |
> | **Build lifecycle** | SFIF (Scaffold→Foundation→Infrastructure→Features) | Projects build enforcement in stages. Product lifecycle maps: POC=Scaffold, MVP=Foundation, Staging=Infrastructure, Production=Features. |
> | **Component design** | SRP (Single Responsibility Principle) | Validators validate. Hooks block. Commands transition state. Each tool does ONE thing. |
> | **Methodology selection** | Strategy Pattern (OOP) | Identity profile → SDLC profile selection → model selection. Same interface, different implementations based on runtime context. |
> | **Context injection** | Template Method Pattern (OOP) | Same structural skeleton, different content. Validation matrix: 29 scenarios, one template, content varies per condition. |
> | **Enforcement escalation** | Chain of Responsibility (OOP) | Instructions → hooks → commands → harness → immune system → human. Each level handles what it can, passes to the next. |
> | **Immune system correction** | Observer Pattern (OOP) | Doctor observes agent behavior every 30s. Agents don't know they're observed. Detection triggers correction. |
> | **Template scaffolding** | Factory Pattern (OOP) | `pipeline scaffold <type> "Title"` creates pages from templates. Type determines template. One creation interface, many output types. |
> | **Knowledge evolution** | Progressive Distillation (wiki pattern) + CMMI continuous improvement | L0→L6 knowledge layers. Each layer distills from the previous. Continuous improvement through the evolution pipeline. |

3. **Dual perspective: second brain AND project wiki.** Every standard applies in BOTH directions. When a project queries the second brain for methodology, the response follows OpenAPI principles (structured, typed, machine-readable). When a project applies methodology to its own wiki, it follows the same DDD bounded contexts, the same SFIF build stages, the same SRP tool design. The standards transfer because they're PRINCIPLES, not project-specific implementations.

4. **Custom patterns are documented alongside global standards.** The wiki has patterns that don't map to a named global standard but follow the SAME design principles. These custom patterns (Goldilocks identity protocol, readiness vs progress, contribution gating) are documented with the same rigor as the standard-aligned ones — because they may BECOME standards for the AI agent domain.

## Deep Analysis

### How Standards Apply from a PROJECT's Perspective

A project connecting to the second brain interacts with standards at two levels:

> [!abstract] From the Project's Perspective
>
> | What the Project Does | Standard in Play | Second Brain Side | Project Wiki Side |
> |----------------------|-----------------|-------------------|-------------------|
> | **Declares identity** | CloudEvents (structured attributes) | Profile stored as typed YAML | Profile in project's CLAUDE.md |
> | **Queries methodology** | OpenAPI (structured interface) | Gateway returns typed response | Project applies response to its own methodology.yaml |
> | **Organizes knowledge** | DDD (bounded contexts) | Domains in wiki/domains/ | Project organizes its own wiki by domain |
> | **Enforces process** | Onion Architecture (layer isolation) | Enforcement patterns documented | Project implements hooks/harness appropriate to its PM level |
> | **Builds incrementally** | SFIF (staged build) | Framework describes the stages | Project follows stages for its own features |
> | **Tracks work** | CMMI (maturity progression) | Chain selection by maturity level | Project uses appropriate chain for its phase/scale |
> | **Designs tools** | SRP (single responsibility) | Each wiki tool does one thing | Project tools follow the same principle |

### How Standards Apply to the Wiki Itself

The wiki is BOTH the framework AND an instance. It must adhere to the standards it teaches:

> [!info] Self-Adherence Checklist
>
> | Standard | How the Wiki Follows It | Evidence |
> |----------|------------------------|---------|
> | CloudEvents | Frontmatter fields are typed, documented, machine-parseable | [[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]] — every field documented |
> | DDD | 7 domains as bounded contexts, cross-domain as shared kernel | wiki/domains/ folder structure, _index.md per domain |
> | Onion Architecture | Pipeline tools don't know about CLAUDE.md rules. CLAUDE.md doesn't know about pipeline internals. | tools/ and CLAUDE.md are independent layers |
> | SFIF | Wiki built in stages: scaffold (templates) → foundation (schema) → infrastructure (tools) → features (content) | The wiki's own evolution history follows SFIF |
> | SRP | validate.py validates. lint.py lints. pipeline.py chains. export.py exports. | Each tool file has one responsibility |
> | CMMI | Maturity folders (00_inbox→04_principles) mirror CMMI levels 1→5 | Lessons promote through evidence accumulation |

### Recognized Standards We Should Formally Adopt

> [!warning] Standards We Reference But Don't Yet Formally Implement
>
> | Standard | Current State | What Formal Adoption Means |
> |----------|-------------|--------------------------|
> | **OpenAPI** | Gateway tools planned but not built. No formal API spec. | Gateway operations documented as OpenAPI spec. Any tool can consume. |
> | **CloudEvents** | Frontmatter fields are structured but not CloudEvents-formatted events. | Hook responses and pipeline events could follow CloudEvents spec for interoperability. |
> | **Conventional Commits** | OpenFleet enforces. OpenArms partially. Wiki doesn't. | Commit messages follow `type(scope): description` format consistently. |
> | **Semantic Versioning** | Super-model uses v1.3. methodology.yaml doesn't version. | Config files should have version fields. Breaking changes increment major version. |

### How This Connects — Navigate From Here

> [!abstract] From Global Standards → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **How does identity use structured attributes?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] — 7 typed dimensions |
> | **Where is the DDD domain structure?** | wiki/domains/ — 7 bounded contexts |
> | **Where is the Onion enforcement?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] — layers don't know about outer layers |
> | **Where is the SFIF lifecycle?** | [[model-sfif-architecture|Model — SFIF and Architecture]] — 4-stage build with quality tiers |
> | **Where is the SRP tool design?** | tools/ — each file has one job. [[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]] — fields enable specific automation |
> | **Where are the design patterns?** | Strategy (model selection), Template Method (validation matrix), Chain of Responsibility (enforcement), Observer (immune system), Factory (scaffolding) |
> | **What's the gateway tools plan?** | [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]] — should be OpenAPI-documented |

## Open Questions

> [!question] ~~Should the gateway tools produce an actual OpenAPI spec?~~
> **RESOLVED:** When gateway becomes HTTP API, not before. Currently a CLI tool — premature spec.
> If the gateway is meant to serve humans, agents, AND MCP connections, an OpenAPI spec would make it self-documenting for machine consumers. Cost: spec maintenance. Benefit: any tool can discover and use the API.

> [!question] ~~Should hook responses follow CloudEvents format?~~
> **RESOLVED:** Not now. Hooks are local shell scripts, not distributed events. CloudEvents applies when hooks emit to external systems.
> Pre/PostToolUse hooks return JSON. If that JSON followed CloudEvents (type, source, time, data), hooks from different projects would be interoperable. Worth the overhead?

> [!question] ~~Which custom patterns are candidates for formal standardization?~~
> **RESOLVED:** Goldilocks identity protocol, SDLC profile selection, stage-gate enforcement. These are the most reused patterns across the ecosystem.
> The Goldilocks identity protocol, the three-profile SDLC model, the readiness/progress two-field tracking — these are custom to this ecosystem but may generalize. Should we propose them as standards?

## Relationships

- BUILDS ON: [[model-sfif-architecture|Model — SFIF and Architecture]]
- BUILDS ON: [[model-llm-wiki|Model — LLM Wiki]]
- RELATES TO: [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
- RELATES TO: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
- RELATES TO: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- RELATES TO: [[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]]
- FEEDS INTO: [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[model-sfif-architecture|Model — SFIF and Architecture]]
[[model-llm-wiki|Model — LLM Wiki]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]]
[[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
