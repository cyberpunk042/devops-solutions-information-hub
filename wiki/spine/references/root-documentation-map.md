---
title: Root Documentation Map — Repository-Level Files
aliases:
  - "Root Documentation Map — Repository-Level Files"
  - "Root Documentation Map"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: three-layer-pattern
    type: wiki
    file: wiki/patterns/01_drafts/three-layer-agent-context-architecture.md
    description: The three-layer agent context architecture pattern
  - id: three-layer-synthesis
    type: wiki
    file: wiki/sources/src-skillmd-claudemd-agentsmd-three-layer-context.md
    description: ETH Zurich research + three-layer architecture evidence
tags: [reference, documentation, root, readme, agents, claude, architecture, design, tools, skills, context]
---

# Root Documentation Map — Repository-Level Files

> [!tip] Quick Orient
>
> This wiki has 8 root-level markdown files in addition to the wiki/ tree. Each serves ONE concern. Together they implement the [[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]] pattern: AGENTS.md (universal) + CLAUDE.md (Claude-specific) + Skills (conditional).

## Summary

The repository root contains 8 documentation files (2,714 total lines) that serve as the entry point for humans, AI tools, and external integrators. Each file has ONE responsibility and references the others bidirectionally. This implements the three-layer agent context pattern (per ETH Zurich Feb 2026 research: oversized CLAUDE.md files reduce task success by ~3%) and provides consistent entry paths regardless of the consumer — human, Claude Code, Codex CLI, Copilot, Gemini, Cursor, or MCP client from another project.

## Reference Content

### The 8 Root-Level Files

> [!abstract] Documentation Map — Each File, One Concern
>
> | File | Lines | Audience | Responsibility |
> |------|-------|----------|---------------|
> | **README.md** | 200 | First visitor (human/AI) | Project overview, what it IS, entry points by role |
> | **AGENTS.md** | 159 | Any AI tool | Universal cross-tool context. 60k+ repo standard. |
> | **CLAUDE.md** | 107 | Claude Code specifically | Claude-specific overrides. References AGENTS.md. |
> | **CONTEXT.md** | 227 | Anyone understanding scope | Identity profile, current state, active epics, constraints |
> | **ARCHITECTURE.md** | 585 | Anyone modifying structure | Data flow, tool topology, page schema, integration points |
> | **DESIGN.md** | 355 | Page creators | Callout vocabulary, layouts, styling, graceful degradation |
> | **TOOLS.md** | 806 | Operators | Complete CLI reference (pipeline, gateway, view, sync, MCP) |
> | **SKILLS.md** | 275 | Skill users/authors | Skills catalog, SKILL.md format, extension hierarchy |

### The Three-Layer Architecture (Implemented)

> [!info] How These Files Implement the Pattern
>
> | Layer | File | Size Target | Our State | Status |
> |-------|------|------------|-----------|--------|
> | **Layer 1 — Universal** | AGENTS.md | <100 lines | 159 lines | Slightly over (pragmatic — this is a complex system) |
> | **Layer 2 — Tool-specific** | CLAUDE.md | <100 lines | 107 lines | Meets target (was 315L before slim) |
> | **Layer 3 — Conditional** | `.claude/skills/*` | <500 lines each | Compliant | See [[SKILLS.md]] for catalog |
>
> **ETH Zurich research (Feb 2026):** AI-generated context files reduce task success by ~3%. Oversized CLAUDE.md files are structurally harmful. Our slim matches the recommendation.

### Loading Flow Per Consumer

> [!info] Who Reads What, and When
>
> | Consumer | Files Loaded | When |
> |----------|-------------|------|
> | **Human first visitor** | README.md | First — orients them to everything |
> | **Claude Code (solo session)** | AGENTS.md + CLAUDE.md | Auto-loaded at session start |
> | **Codex CLI / Copilot / Gemini / Cursor** | AGENTS.md | Auto-loaded (Linux Foundation Agentic AI standard) |
> | **Sub-agent dispatched from Claude** | AGENTS.md inheritance only (uncertain) | Include critical rules in spawn prompt |
> | **MCP client from another project** | AGENTS.md | Via gateway integration |
> | **Harness-managed agent (future)** | Stage skill + AGENTS.md | CLAUDE.md de-emphasized |
> | **Human operator running tools** | TOOLS.md | On-demand reference |
> | **Human creating wiki pages** | DESIGN.md | On-demand reference |

### The Documentation Graph

> [!abstract] How Root Files Link to Each Other
>
> ```
>  ┌──────────┐
>  │README.md │ ◄── first visitor entry
>  │          │
>  │ links to │
>  │ all docs │
>  └────┬─────┘
>       │
>       ├──→ AGENTS.md ──► universal rules (also read by other tools)
>       │         │
>       │         └──► CLAUDE.md (Claude-specific overrides)
>       │
>       ├──→ CONTEXT.md ──► identity, phase, constraints
>       ├──→ ARCHITECTURE.md ──► data flow, tool topology
>       ├──→ DESIGN.md ──► page design patterns
>       ├──→ TOOLS.md ──► CLI reference
>       └──→ SKILLS.md ──► skills catalog
>                │
>                └──► .claude/skills/ (actual skill files)
> ```
>
> Every file references at least one other. README.md is the hub. AGENTS.md is the universal base. CLAUDE.md extends AGENTS.md. Thematic files (CONTEXT, ARCHITECTURE, DESIGN, TOOLS, SKILLS) provide depth per concern.

### What Each File Contains (Detail)

#### README.md
- Project overview paragraph (what this IS — a second brain, 5-project ecosystem hub)
- Role-based entry table ("You are... → Read this first")
- Knowledge layer structure (L0 → L7)
- Operational layers (raw/, wiki/, tools/, .claude/, wiki/config/)
- Core principles (3 principles from convergent evidence)
- Quick Start (human operator commands)
- Ecosystem diagram (ASCII)
- Status metrics (pages, relationships, models, standards)
- Documentation map table

#### AGENTS.md
- Sacrosanct operator directives (verbatim quotes)
- 7 numbered hard rules (MANDATORY)
- Stage gates table (ALLOWED/FORBIDDEN per stage)
- Methodology models table (task type → model → stages)
- Page schema (required frontmatter + section order)
- Relationship conventions (ALL_CAPS verbs, [[slug|title]] format)
- Quality gates (what `pipeline post` enforces)
- Navigation entry points to other docs

#### CLAUDE.md
- Identity Profile (Goldilocks 9 dimensions)
- Claude-specific behaviors (skills, MCP, TodoWrite, plan mode)
- Skills directory summary (links to SKILLS.md)
- Essential commands table
- Ingestion modes (auto/guided/smart)
- 5 Claude-specific hard rules (extend AGENTS.md)
- Flow per mode table
- Adoption direction (7 Levels positioning)

#### CONTEXT.md
- Identity Profile (9 dimensions with "why it matters")
- Current state metrics
- Active epic portfolio (in-progress + draft)
- Operator context (5-project ecosystem, hardware, preferences)
- Constraints (hard constraints callout + quality thresholds)
- Phase trajectory (past → current → next)
- What this is NOT (5 anti-patterns)

#### ARCHITECTURE.md
- Directory topology (full tree with purposes)
- Data flow (L0 → L7 with promotion criteria)
- Tool topology (13 tools, roles, line counts)
- Wiki page schema (YAML fields, types, maturity folders)
- Integration points (dual-scope, MCP, export, sync)
- Methodology engine (config files, artifact classes)
- Stage gate enforcement flow
- Key architectural decisions

#### DESIGN.md
- Design philosophy (3 compliance tiers: 25/60/90%)
- Callout vocabulary (8 types with semantic purpose)
- 6-level emphasis hierarchy
- Tables vs prose decision guide
- Per-type page layouts
- YAML frontmatter as programmatic interface
- Maturity folder structure
- Before/after styling transformations
- Graceful degradation table (4 rendering contexts)

#### TOOLS.md
- Pipeline (13 subcommands + 14 named chains)
- Gateway (12 subcommands, dual-scope)
- View (9 commands)
- Sync (WSL ↔ Windows)
- MCP Server (21 tools)
- Quality tools (validate, lint, stats)
- Export (openfleet, aicp, methodology)
- Setup (including systemd services)
- Evolution pipeline (6 scoring signals)
- Common workflows (8 recipes)

#### SKILLS.md
- What skills are (conditional vs always-loaded)
- Skill vs CLAUDE.md vs AGENTS.md (three-layer table)
- Skill catalog (9 project skills + 11 superpowers)
- SKILL.md format (YAML frontmatter, body structure)
- Skill authoring guidelines
- Skills vs commands vs hooks (extension hierarchy)
- Skill distribution (agentskills.io portability)

### Cross-References from Wiki Pages

The following wiki pages link to or reference these root-level docs:

| Wiki Page | Root Doc Referenced |
|-----------|--------------------|
| [[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]] | This project's implementation of the pattern |
| [[src-skillmd-claudemd-agentsmd-three-layer-context|Three-Layer Context Synthesis]] | ETH Zurich evidence + rationale |
| [[model-claude-code|Model — Claude Code]] | CLAUDE.md discussed as extension layer |
| [[model-markdown-as-iac|Model — Markdown as IaC]] | These files ARE IaC for agent behavior |
| [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] | SKILLS.md is the skill catalog entry |
| [[adoption-guide|Adoption Guide]] | References these files as the entry point |
| [[super-model|Super-Model]] | References this file as the root-docs map |

### How This Connects — Navigate From Here

> [!abstract] From This Reference → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The pattern this implements** | [[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]] |
> | **Why CLAUDE.md should be slim** | [[src-skillmd-claudemd-agentsmd-three-layer-context|ETH Zurich Research + Three-Layer]] |
> | **Markdown files as IaC** | [[model-markdown-as-iac|Model — Markdown as IaC]] |
> | **Agent context model** | [[model-claude-code|Model — Claude Code]] |
> | **Skills subsystem** | [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] |
> | **Overall system map** | [[super-model|Super-Model]] |
> | **Methodology overview** | [[model-methodology|Model — Methodology]] |

## Relationships

- IMPLEMENTS: [[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]]
- BUILDS ON: [[src-skillmd-claudemd-agentsmd-three-layer-context|Synthesis — SKILL.md vs CLAUDE.md vs AGENTS.md]]
- RELATES TO: [[model-claude-code|Model — Claude Code]]
- RELATES TO: [[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- PART OF: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[three-layer-agent-context-architecture|Three-Layer Agent Context Architecture]]
[[Synthesis — SKILL.md vs CLAUDE.md vs AGENTS.md]]
[[model-claude-code|Model — Claude Code]]
[[model-markdown-as-iac|Model — Markdown as IaC — Design.md and Agent Configuration]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
