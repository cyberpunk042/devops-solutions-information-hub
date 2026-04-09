---
title: "Model: LLM Wiki"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: authoritative
maturity: growing
created: 2026-04-09
updated: 2026-04-09
sources:
  - id: src-karpathy-llm-wiki-idea-file
    type: documentation
    file: raw/articles/karpathy-llm-wiki-idea-file.md
    title: "Karpathy LLM Wiki Idea File"
    ingested: 2026-04-08
  - id: src-llm-wiki-v2-agentmemory
    type: documentation
    file: raw/articles/llm-wiki-v2-extending-karpathys-llm-wiki-pattern-with-lessons-from-building-agen.md
    title: "LLM Wiki v2 — Extending Karpathy's Pattern with Agentmemory Lessons"
    ingested: 2026-04-08
tags: [llm-wiki, model, knowledge-system, schema, ingestion, evolution, standards, transferable]
---

# Model: LLM Wiki

## Summary

The LLM Wiki model defines how to build a knowledge system where an LLM agent maintains a markdown wiki — ingesting sources, synthesizing pages, cross-referencing relationships, evolving insights through density layers, and linting for quality. The model solves the wiki maintenance problem: wikis historically die because humans abandon upkeep. With an LLM agent responsible for all mechanical operations, the wiki compounds knowledge instead of decaying. This model is technology-agnostic — it defines WHAT a wiki must contain and HOW it operates, not which tools implement it.

## Key Insights

- The maintenance economics insight: wikis fail not from lack of content but from maintenance abandonment. Making the LLM handle ALL bookkeeping (indexes, validation, cross-referencing, linting) eliminates this failure mode structurally.
- Three core operations define the system: **Ingest** (source → structured pages), **Query** (navigate via indexes and relationships), **Lint** (validate, detect orphans, flag contradictions).
- The schema is the real product — content is regenerable from raw sources, but the schema that constrains content structure encodes irreplaceable operational knowledge.
- Knowledge compounds through density layers — raw sources become syntheses become concepts become lessons become patterns become decisions. Each layer is denser and more actionable.
- The wiki IS the second brain — not a documentation tool alongside the real work, but the persistent intelligence layer that survives across sessions, agents, and projects.

## Deep Analysis

### The Model (universal — any project can adopt this)

#### Core Architecture

An LLM Wiki has three layers:

1. **Raw layer** — unprocessed source material with permanent provenance. Never deleted, never modified after ingestion. This is the evidence base.
2. **Wiki layer** — structured markdown pages with YAML frontmatter, typed relationships, and quality gates. This is the knowledge base. Pages are organized by domain and connected by explicit relationships.
3. **Meta layer** — schema definition, validation rules, templates, and methodology config. This is the operational brain — it defines how the wiki works and enforces structure on all content.

#### Repository Structure

Any project adopting this model creates these directories:

```
{project-root}/
├── raw/                          # Raw layer — permanent source provenance
│   ├── articles/                 # Web content, READMEs, documentation
│   ├── transcripts/              # Video/audio transcripts
│   └── notes/                    # Legacy notes, operator directives
│
├── wiki/                         # Wiki layer — structured knowledge
│   ├── domains/                  # Concept pages by domain
│   │   └── {domain-name}/       # One folder per knowledge domain
│   │       ├── _index.md        # Auto-maintained domain index
│   │       └── {concept}.md     # One concept per page
│   ├── sources/                  # Source-synthesis pages (L1)
│   ├── comparisons/              # Comparison pages with matrices (L3)
│   ├── lessons/                  # Codified experience (L4)
│   ├── patterns/                 # Recurring cross-domain structures (L5)
│   ├── decisions/                # Choice frameworks with alternatives (L6)
│   ├── spine/                    # Navigation: model guides, overviews
│   ├── backlog/                  # Project management (epics/modules/tasks)
│   ├── log/                      # Operator directives, session logs
│   └── config/                   # Methodology definition files
│
├── config/                       # Meta layer — schema and templates
│   ├── wiki-schema.yaml          # Page validation schema
│   └── templates/                # Page scaffolding templates per type
│
└── {project-specific}/           # Whatever the project needs (tools, src, etc.)
```

The separation matters: `raw/` is immutable evidence. `wiki/` is living knowledge. `config/` is operational rules. A project may have its own `src/`, `tools/`, `docs/` — the wiki directories coexist alongside them.

#### Knowledge Layer Architecture

| Layer | Purpose | Content type | How it's created |
|-------|---------|-------------|-----------------|
| L0 | Raw evidence | Unprocessed sources | Fetched or dropped into raw/ |
| L1 | Source synthesis | One synthesis per source | Ingestion — read source, extract insights |
| L2 | Concepts | One concept per page, by domain | Ingestion + manual creation |
| L3 | Comparisons | Structured comparison with matrix | Cross-reference analysis |
| L4 | Lessons | Codified experience with evidence | Evolution — distilled from L1-L3 |
| L5 | Patterns | Recurring structure with 2+ instances | Evolution — observed across L2-L4 |
| L6 | Decisions | Choice framework with alternatives | Evolution — actionable from L4-L5 |
| Spine | Navigation | Model guides, domain overviews | Manual curation |

This IS the [[Progressive Distillation]] pattern: each layer is denser and more actionable than the previous. Raw → synthesis → concept → lesson → pattern → decision.

#### Page Schema

Every wiki page uses YAML frontmatter. The schema defines required and optional fields:

**Required fields** (every page):
```yaml
title: "Page Title"           # Must match the # Heading
type: concept                  # The page type (see types below)
domain: ai-agents              # Knowledge domain (matches folder)
status: synthesized            # Lifecycle: raw → processing → synthesized → verified → stale
confidence: high               # low | medium | high | authoritative
created: 2026-04-09
updated: 2026-04-09
sources: []                    # Provenance chain — where knowledge came from
tags: []                       # For discovery and cross-referencing
```

**Evolution fields** (for L4-L6 pages):
```yaml
layer: 4                       # Knowledge layer number
maturity: growing              # seed → growing → mature → canonical
derived_from: [list]           # Source pages this was distilled from
```

**Page types**: concept, source-synthesis, comparison, lesson, pattern, decision, domain-overview, learning-path, evolution, epic, module, task, note

Each type has required sections defined in the schema. For example, a `lesson` requires: Summary, Context, Insight, Evidence, Applicability, Relationships. A `decision` requires: Summary, Decision, Alternatives, Rationale, Reversibility, Dependencies, Relationships.

The schema file (`config/wiki-schema.yaml`) is the single source of truth for validation.

#### Page Structure

Every page follows a section order:

```markdown
# Title

## Summary          ← 2-3 sentences, the page's elevator pitch
## Key Insights     ← Condensed takeaways (bullet points)
## Deep Analysis    ← Full depth (for concepts, comparisons)
## Open Questions   ← Gaps to fill, tagged with (Requires: ...)
## Relationships    ← Typed links using ALL_CAPS verbs + [[wikilinks]]
## Backlinks        ← Auto-generated incoming links
```

Evolved page types (lesson, pattern, decision) have different required sections — see templates.

#### Relationship System

Relationships are explicit, typed, and bidirectional via backlinks:

```markdown
## Relationships

- BUILDS ON: [[LLM Wiki Pattern]]
- ENABLES: [[Knowledge Evolution Pipeline]]
- CONTRADICTS: [[some assumption]]
- DERIVED FROM: [[Source Page Title]]
```

Supported verbs: BUILDS ON, ENABLES, COMPARES TO, CONTRADICTS, USED BY, RELATES TO, FEEDS INTO, DERIVED FROM, SUPERSEDES, IMPLEMENTS, EXTENDS, PARALLELS, SYNTHESIZES

This is what makes the wiki a knowledge GRAPH, not just a folder of files. In Obsidian, these render as a navigable graph. In LightRAG, they become queryable edges.

#### Quality Gates

Every page must pass:
1. Valid frontmatter per the schema
2. Summary ≥ 30 words
3. At least 1 relationship (unless first in a new domain)
4. Title field matches # Heading
5. Domain field matches folder path
6. Source provenance (URL or file reference)
7. No > 70% concept overlap with existing pages (update instead of create)

#### Three Core Operations

**Ingest**: Source arrives → save to raw/ → read FULL source (multiple reads for large files, verify depth by examining real instances not just descriptions) → create source-synthesis page → create/update concept pages → validate.

**Query**: Navigate via domain indexes and relationship links. The LLM reads the index, follows links to relevant pages, reads content. No vector database needed below ~200 pages.

**Lint**: Validate all pages against schema. Detect orphaned references. Flag stale content (source updated after derived page). Surface contradictions. Report gaps (weak domains, thin pages, unanswered questions).

#### Evolution Pipeline

The wiki doesn't just store knowledge — it evolves it:

1. **Score** — analyze existing pages to identify evolution candidates (cross-source convergence, relationship hubs, domain gaps, open question density)
2. **Scaffold** — create page stubs from templates
3. **Generate** — fill pages from source material (LLM session, local model, or API)
4. **Validate** — run quality gates
5. **Review** — maturity promotion (seed → growing → mature → canonical)

The maturity lifecycle prevents premature promotion: seed (exists but unvalidated) → growing (reviewed, real derived_from) → mature (cross-referenced, stable 30+ days) → canonical (authoritative, marked manually).

#### Scale Boundary

Below ~200 pages: index-driven navigation is cheaper and more accurate than vector search. The LLM reads indexes, follows links, reads pages directly.

Above ~200 pages: add a graph-enhanced retrieval layer (e.g., LightRAG) as an ADDITIVE layer. The wiki stays the same — the retrieval layer indexes it. See [[Decision: Wiki-First with LightRAG Upgrade Path]].

### How to Adopt This Model

1. Create the repository structure above in your project
2. Define your schema in `config/wiki-schema.yaml` — start with the reference schema and adapt types/fields for your domain
3. Create page templates in `config/templates/` — one per page type with placeholder structure
4. Write your agent instructions (CLAUDE.md or equivalent) with the schema, conventions, and quality gates
5. Start ingesting sources — the wiki grows from there
6. After each change, validate all pages against the schema
7. Periodically run evolution: score candidates, scaffold, generate, review maturity

Full guide: [[Adoption Guide — How to Use This Wiki's Standards]]

### Reference Implementation

This research wiki is the reference implementation of the LLM Wiki model. It demonstrates:
- 146 pages across 10 domains with 1,086 relationships
- 6 knowledge layers populated (L1-L6 + spine)
- Evolution pipeline with 6 scoring signals and 3 LLM backends
- Maturity lifecycle applied to all pages (130 growing, 5 seed)
- Quality gates enforced via Python validation tooling
- 14 named models with entry points in wiki/spine/

Project-specific implementation details (pipeline commands, /commands, MCP tools, sync services) are documented in the project's CLAUDE.md and are NOT part of the universal model.

### Key Pages in This Model

| Page | What it covers |
|------|---------------|
| [[LLM Wiki Pattern]] | Karpathy's original design — the foundational pattern |
| [[Wiki Ingestion Pipeline]] | How sources become pages (multi-stage) |
| [[Wiki Knowledge Graph]] | How relationships create a queryable graph |
| [[LLM Knowledge Linting]] | How quality is maintained automatically |
| [[Knowledge Evolution Pipeline]] | How pages evolve through density layers |
| [[Progressive Distillation]] | The pattern: raw → synthesis → lesson → pattern → decision |
| [[LLM Wiki vs RAG]] | When wiki navigation beats vector search |
| [[Decision: Wiki-First with LightRAG Upgrade Path]] | The scale decision |
| [[Second Brain Architecture]] | PKM theory mapped to the wiki model |
| [[Wiki Backlog Pattern]] | How the wiki tracks its own work |

### Lessons Learned

These lessons came from BUILDING a wiki with this model — they are validated experience, not theory:

| Lesson | What we learned |
|--------|----------------|
| [[LLM-Maintained Wikis Outperform Static Documentation]] | Maintenance economics is the differentiator |
| [[Lesson: Schema Is the Real Product — Not the Content]] | The schema survives; content is regenerable |
| [[Multi-Stage Ingestion Beats Single-Pass Processing]] | Each pass discovers what the previous missed |
| [[The Wiki Maintenance Problem Is Solved by LLM Automation]] | The 80-year gap from Memex to working implementation |
| [[Never Synthesize from Descriptions Alone]] | Read the THING, not the description of the thing |
| [[Shallow Ingestion Is Systemic, Not Isolated]] | One defect = audit ALL similar artifacts |
| [[Automated Knowledge Validation Prevents Silent Wiki Decay]] | Without linting, wikis decay silently |

## Open Questions

- What is the optimal schema complexity for a new project adopting this model? (Start minimal and grow, or start comprehensive?)
- How should the wiki model interact with existing documentation systems (Confluence, Notion, Google Docs) in an organization?
- What is the minimum viable wiki — the smallest set of pages and structure that demonstrates value?
- How does multi-author wiki editing work when multiple agents or humans contribute? (Conflict resolution, merge strategy)

## Relationships

- FEEDS INTO: [[Model: Second Brain]]
- FEEDS INTO: [[Model Guide: Ecosystem Architecture]]
- ENABLES: [[Model Guide: Claude Code]]
- BUILDS ON: [[LLM Wiki Pattern]]
- BUILDS ON: [[Wiki Ingestion Pipeline]]
- BUILDS ON: [[Knowledge Evolution Pipeline]]
- RELATES TO: [[Model Guide: Methodology]]
- RELATES TO: [[Model: Knowledge Evolution]]

## Backlinks

[[Model: Second Brain]]
[[Model Guide: Ecosystem Architecture]]
[[Model Guide: Claude Code]]
[[LLM Wiki Pattern]]
[[Wiki Ingestion Pipeline]]
[[Knowledge Evolution Pipeline]]
[[Model Guide: Methodology]]
[[Model: Knowledge Evolution]]
