---
title: Wiki Gateway Tools — Unified Knowledge Interface
aliases:
  - "Wiki Gateway Tools — Unified Knowledge Interface"
type: epic
domain: backlog
status: draft
priority: P0
task_type: epic
current_stage: document
readiness: 5
stages_completed:
artifacts:
confidence: high
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: operator-directive
    type: file
    file: raw/notes/2026-04-12-mega-vision-directive.md
tags: [gateway, tools, api, mcp, unified-interface, second-brain, operations]
---

# Wiki Gateway Tools — Unified Knowledge Interface

## Summary

Build a unified Python interface that serves humans, AI agents, and MCP connections as a single gateway into the wiki knowledge system. The gateway supports both internal operations (archive, move, update references, backup, factory reset) and external queries (stage requirements, domain chains, artifact templates, methodology configs). Every project in the ecosystem can use this interface instead of browsing the wiki directly. Agents can participate by writing remarks, lessons, and corrections back to the second brain.

## Operator Directive

> "we are gong to need to add python script to make the Wiki LLM for internal and for external (other project to second-brain) and we are going to allow those to cleanup the Wiki LLM, to run certain operation like archiving documents, moving things to other folders and updating all the references and stuff like this."

> "Then operations / commands for getting the right information automatically with the right input, not even having to search, an agent or another tools or a MCP can just use this interface instead of browsing the second-brain"

> "It has to be something a human can use and an AI can use and we can connect other tools and MCPs to it."

> "We are going to allow the AI agent to even participe to the second-brain via this gateway or manually in order to leave a remark or a learning or a lesson or something learned"

## Goals

- Human CLI, AI agent, and MCP server all use the SAME Python interface — three frontends, one engine
- Internal operations: archive pages, move pages (update all refs), backup wiki, factory reset (targeted or full)
- Location mapping memory: automatic bridge when things move, trace provenance always
- Methodology queries: get all artifacts for a stage, all stages for a domain, full chain for a task type
- Template access: get any template with rich examples, not empty skeletons
- Config visualization: render methodology.yaml sections as markdown or yaml on demand
- Agent participation: structured write-back (remarks, lessons, corrections) with provenance tracking
- Operational views: backlog status, log entries, lessons by category, config sections
- Documentation: complete manual for every tool, integrated into the Wiki LLM

## Done When

- [ ] `python3 -m tools.gateway --help` shows all available operations
- [ ] `python3 -m tools.gateway query --stage document --domain typescript` returns correct artifacts
- [ ] `python3 -m tools.gateway move "Old Title" --to "domains/new-domain/"` updates all references
- [ ] `python3 -m tools.gateway archive "Page Title"` moves to archive with mapping memory
- [ ] `python3 -m tools.gateway backup --target /path/` creates restorable backup
- [ ] `python3 -m tools.gateway contribute --type lesson --title "..." --content "..."` creates structured write-back
- [ ] MCP server exposes gateway operations as tools (extends existing 17 tools)
- [ ] `python3 -m tools.gateway template lesson` returns rich template with inline example content
- [ ] `python3 -m tools.gateway config methodology.models` renders models section as markdown
- [ ] `python3 -m tools.gateway chain feature-development --domain typescript` returns full chain with branches
- [ ] Documentation page exists in wiki for every gateway operation
- [ ] Pipeline post returns 0 errors after all changes
- [ ] Operator confirms deliverables are findable (discoverability test)

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | feature-development |
> | **Quality tier** | Skyscraper |
> | **Estimated modules** | 6 |
> | **Estimated tasks** | 25-35 |
> | **Dependencies** | E003 (Artifact Type System) partially — needs stable artifact definitions |

## Stage Artifacts (per methodology model)

> [!abstract] Stage → Artifact Map
>
> | Stage | Required Artifacts | Template |
> |-------|--------------------|----------|
> | Document | Directive log (done), research on existing tools, gap analysis vs current pipeline | wiki/config/templates/methodology/gap-analysis.md |
> | Design | Requirements spec (FR/NFR), API design (command interface), architecture decisions | wiki/config/templates/methodology/requirements-spec.md |
> | Scaffold | Python module structure, CLI argument parser, MCP tool registration stubs | N/A |
> | Implement | gateway.py engine, CLI frontend, MCP frontend, operations, queries, write-back | N/A |
> | Test | Integration tests, MCP tool tests, pipeline post validation | N/A |

## Module Breakdown

| Module | Delivers | Est. Tasks |
|--------|----------|-----------|
| M1: Gateway Engine | Core Python interface — the single engine all frontends use | 4-5 |
| M2: Internal Operations | archive, move (with ref update), backup, factory reset, location mapping | 5-6 |
| M3: Methodology Queries | stage artifacts, domain chains, task type chains, template access, config visualization | 5-6 |
| M4: Agent Participation | structured write-back (remarks, lessons, corrections), provenance tracking | 3-4 |
| M5: Operational Views | backlog status, log entries, lessons by category, config rendering | 3-4 |
| M6: Documentation & MCP | Manual pages in wiki, MCP tool extensions, CLI help system | 4-5 |

## Dependencies

- **E003 (Artifact Type System):** Gateway queries need stable artifact definitions. Current state: 40% — enough for M3 to start but may need updates.
- **Existing pipeline.py:** Gateway WRAPS existing pipeline functionality, doesn't replace it. pipeline.py remains the post-ingestion chain.
- **Existing MCP server:** Gateway extends the MCP server with new tools, doesn't replace existing 17.

## Open Questions

> [!question] ~~Should the gateway be a separate Python module or extend pipeline.py?~~
> **RESOLVED:** Separate. Already implemented as tools/gateway.py (1,200+ lines). Different concern from pipeline orchestration.
> pipeline.py is already 800+ lines. A separate tools/gateway.py (or tools/gateway/ package) keeps concerns clean. But it needs access to the same utilities (common.py, manifest, etc.).

> [!question] ~~How does location mapping memory work across git?~~
> **RESOLVED:** Gateway archive/move writes location mappings to JSON file tracked by git. Persists across history. Any consumer looks up where a page went.
> When a page moves, the mapping needs to persist. Options: JSON file in wiki/config/, git-tracked. Or: redirect pages (like HTTP 301). Or: both — mapping for programmatic access, redirect page for human/agent navigation.

> [!question] ~~Should write-back (agent contributions) require approval or auto-merge?~~
> **RESOLVED:** Trust-tier-gated per Goldilocks. Lightweight: auto-merge to raw/notes/. Capable: auto-merge with validation. Expert: auto-merge anywhere. Details TBD.
> Options: auto-merge to raw/notes/ (low risk), require operator approval for wiki/ pages (higher quality gate), or tiered — remarks auto-merge, lessons need review.

> [!question] ~~How do we handle factory reset for projects that aren't the research wiki?~~
> **RESOLVED:** Re-scaffold from brain templates. Delete custom config, re-copy from wiki/config/templates/, re-run pipeline post.
> The operator said "tools for every project, not necessarily the second-brain." The gateway needs to work on any wiki-structured project, not just this one. Config path must be parameterizable.

### How This Connects — Navigate From Here

> [!abstract] From This Epic → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Goldilocks** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- IMPLEMENTS: [[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
- BUILDS ON: [[model-llm-wiki|Model — LLM Wiki]]
- RELATES TO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- RELATES TO: [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
- RELATES TO: [[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]]
- DEPENDS ON: [[E003-artifact-type-system|Artifact Type System]]

## Backlinks

[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[model-llm-wiki|Model — LLM Wiki]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]]
[[E003-artifact-type-system|Artifact Type System]]
[[e014-goldilocks-navigable-system-identity-to-action-in-continuous-flow|E014 — Goldilocks Navigable System — Identity to Action in Continuous Flow]]
[[e015-gateway-tools-completion-all-requirements-implemented-with-mcp-integration|E015 — Gateway Tools Completion — All Requirements Implemented with MCP Integration]]
[[gateway-tools-reference|Gateway Tools Reference — Complete Command Documentation]]
[[global-standards-adherence|Global Standards Adherence — Engineering Principles the Wiki Follows]]
[[goldilocks-flow|Goldilocks Flow — From Identity to Action]]
[[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain — Complete Walkthrough]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
[[the-wiki-is-a-hub-not-a-silo|The Wiki Is a Hub, Not a Silo]]
