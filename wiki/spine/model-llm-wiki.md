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

The LLM Wiki model defines a knowledge system where an LLM agent maintains a structured markdown wiki — ingesting sources, synthesizing pages, cross-referencing relationships, evolving insights through density layers, and linting for quality. The model solves the wiki maintenance problem: wikis historically die because humans abandon upkeep. With an LLM handling all mechanical operations, the wiki compounds knowledge instead of decaying. This document is the complete, lossless human-readable specification of the model. Everything in the schema files is here.

## Key Insights

- Maintenance economics: wikis fail from abandoned upkeep, not lack of content. Making the LLM handle ALL bookkeeping eliminates this structurally.
- Three operations: **Ingest** (source → structured pages), **Query** (navigate via indexes + relationships), **Lint** (validate, detect orphans, flag contradictions).
- The schema is the real product — content is regenerable from raw sources; the schema that constrains content encodes irreplaceable operational knowledge.
- Knowledge compounds through density layers — each layer denser and more actionable than the previous.
- This model is technology-agnostic. It defines WHAT and HOW, not which tools.

## Deep Analysis

### Core Architecture

An LLM Wiki has three layers:

1. **Raw layer** — unprocessed source material. Never modified after ingestion. Permanent provenance.
2. **Wiki layer** — structured markdown pages with YAML frontmatter, typed relationships, quality gates.
3. **Meta layer** — schema, templates, validation rules. Defines how the wiki works.

### Repository Structure

```
{project-root}/
├── raw/                          # Raw layer
│   ├── articles/                 # Web content, READMEs, docs
│   ├── transcripts/              # Video/audio transcripts
│   └── notes/                    # Legacy notes
├── wiki/                         # Wiki layer
│   ├── domains/{domain}/         # L2 concept pages by domain
│   ├── sources/                  # L1 source-synthesis pages
│   ├── comparisons/              # L3 comparison pages
│   ├── lessons/                  # L4 codified experience
│   ├── patterns/                 # L5 recurring structures
│   ├── decisions/                # L6 choice frameworks
│   ├── spine/                    # Navigation: model guides, overviews
│   ├── backlog/                  # PM: epics/modules/tasks
│   ├── log/                      # Operator directives, session logs
│   └── config/                   # Methodology files
├── config/                       # Meta layer
│   ├── wiki-schema.yaml          # Page validation schema
│   └── templates/                # Scaffolding templates per type
└── {project-specific}/           # Whatever else the project needs
```

### Knowledge Layers

| Layer | Directory | Type | Purpose | Created by |
|-------|-----------|------|---------|-----------|
| L0 | raw/ | — | Unprocessed evidence | Fetch / drop |
| L1 | wiki/sources/ | source-synthesis | One synthesis per source | Ingestion |
| L2 | wiki/domains/ | concept | One concept per page | Ingestion + manual |
| L3 | wiki/comparisons/ | comparison | Structured comparisons | Cross-reference |
| L4 | wiki/lessons/ | lesson | Codified experience | Evolution |
| L5 | wiki/patterns/ | pattern | Recurring structures (2+ instances) | Evolution |
| L6 | wiki/decisions/ | decision | Choice frameworks with alternatives | Evolution |
| Spine | wiki/spine/ | various | Navigation, model guides | Curation |

This IS [[Progressive Distillation]]: raw → synthesis → concept → lesson → pattern → decision.

### Complete Page Type Catalog

16 page types, each with a specific purpose and required sections:

| Type | Purpose | Required sections |
|------|---------|------------------|
| **concept** | Core knowledge — one idea per page | Summary, Key Insights, Deep Analysis, Relationships |
| **source-synthesis** | Extraction from one source | Summary, Key Insights, Relationships |
| **comparison** | Structured comparison with matrix | Summary, Comparison Matrix, Key Insights, Deep Analysis, Relationships |
| **reference** | Quick-reference page | Summary, Relationships |
| **deep-dive** | Extended analysis | Summary, Key Insights, Deep Analysis, Relationships |
| **index** | Navigation page | (none required) |
| **lesson** | Codified experience (L4) | Summary, Context, Insight, Evidence, Applicability, Relationships |
| **pattern** | Recurring structure (L5) | Summary, Pattern Description, Instances, When To Apply, When Not To, Relationships |
| **decision** | Choice framework (L6) | Summary, Decision, Alternatives, Rationale, Reversibility, Dependencies, Relationships |
| **domain-overview** | Domain state summary | Summary, State of Knowledge, Maturity Map, Gaps, Priorities, Key Pages, Relationships |
| **learning-path** | Ordered reading guide | Summary, Prerequisites, Sequence, Outcomes, Relationships |
| **evolution** | How a concept changed over time | Summary, Timeline, Key Shifts, Current State, Relationships |
| **epic** | Backlog: large initiative | Summary, Goals, Done When, Relationships |
| **module** | Backlog: scoped deliverable | (same as epic) |
| **task** | Backlog: atomic work unit | Summary, Done When |
| **note** | Log entry (directive/session) | Summary |

### Examples — What Each Type Looks Like

#### Concept example: [[Methodology Framework]]

```yaml
---
title: "Methodology Framework"
type: concept
domain: cross-domain
layer: 2
maturity: growing
status: synthesized
confidence: authoritative
---
```

Sections: Summary → Key Insights (8 bullets on composable models) → Deep Analysis (8 subsections: model definition, selection, composition, adaptation, recursion, multi-track, quality dimension, transferability) → Open Questions → Relationships. 347 lines. The deepest concept page demonstrates the full depth expected.

#### Lesson example: [[Context Management Is the Primary LLM Productivity Lever]]

```yaml
---
title: "Context Management Is the Primary LLM Productivity Lever"
type: lesson
domain: ai-agents
layer: 4
maturity: growing
derived_from:
  - "Claude Code Best Practices"
  - "Synthesis: Claude Code Accuracy Tips"
  - "Synthesis: Claude Code Harness Engineering"
---
```

Sections: Summary → Context (when this lesson applies) → Insight (the core learning — context is the variable you control, not model capability) → Evidence (4 independent sources converging: Boris Cherny's 95% confidence rule, degradation curve quantification, harness engineering guardrails, shanraisshan's CLAUDE.md architecture) → Applicability → Relationships. 102 lines. Evidence section references specific data points from multiple sources.

#### Pattern example: [[Scaffold → Foundation → Infrastructure → Features]]

```yaml
---
title: "Scaffold → Foundation → Infrastructure → Features"
type: pattern
domain: cross-domain
layer: 5
maturity: growing
derived_from:
  - "Four-Project Ecosystem"
  - "Progressive Distillation"
instances:
  - page: "Research Wiki"
    context: "Scaffold (CLAUDE.md, dirs) → Foundation (tools/common.py, schema) → Infrastructure (pipeline.py, MCP) → Features (evolve, sync)"
  - page: "OpenFleet"
    context: "Scaffold (monorepo) → Foundation (orchestrator, agent model) → Infrastructure (board sync, doctor.py) → Features (10 agents)"
  - page: "AICP"
    context: "Scaffold (venv, profiles) → Foundation (router, circuit breaker) → Infrastructure (MCP, guardrails) → Features (routing, voice)"
---
```

Sections: Summary → Pattern Description (what it is, how to recognize it, exit criteria per stage) → Instances (4 detailed examples with per-stage breakdown) → When To Apply → When Not To → Relationships. 176 lines. The `instances` frontmatter field lists concrete occurrences with context.

#### Decision example: [[Decision: MCP vs CLI for Tool Integration]]

```yaml
---
title: "Decision: MCP vs CLI for Tool Integration"
type: decision
domain: tools-and-platforms
layer: 6
maturity: growing
derived_from:
  - "Synthesis: Claude Code Harness Engineering"
  - "Synthesis: Claude Code Accuracy Tips"
  - "MCP Integration Architecture"
reversibility: easy
---
```

Sections: Summary → Decision (clear statement: "CLI+Skills for project-internal tooling, MCP for external service bridges") → Alternatives (3 rejected alternatives with reasons) → Rationale (evidence-backed: 12x cost differential, Playwright proof video, Google Trends signal) → Reversibility → Dependencies → Relationships. 121 lines. The `reversibility` field is unique to decisions.

#### Source-synthesis example: [[Synthesis: Context Mode — MCP Sandbox for Context Saving]]

```yaml
---
title: "Synthesis: Context Mode — MCP Sandbox for Context Saving"
type: source-synthesis
domain: ai-agents
layer: 1
maturity: growing
sources:
  - id: src-context-mode
    type: documentation
    url: "https://github.com/mksglu/context-mode"
    file: raw/articles/mksglucontext-mode.md
    title: "mksglu/context-mode"
---
```

Sections: Summary → Key Insights (11 subsections covering sandbox tools, FTS5/BM25 knowledge base, session continuity, 12-platform matrix, benchmarks, Think in Code paradigm) → Open Questions → Relationships. 254 lines. This is what a DEEP source synthesis looks like — the raw file was 1,057 lines and the actual context-mode DESIGN.md was examined (Layer 1 depth verification).

#### Comparison example: [[Cross-Domain Patterns]]

```yaml
---
title: "Cross-Domain Patterns"
type: comparison
domain: cross-domain
layer: 3
maturity: growing
---
```

Sections: Summary → Comparison Matrix (6-row table: pattern name, domains it appears in, instances, underlying constraint) → Key Insights → Deep Analysis (per-pattern deep dives with instance tables) → Open Questions → Relationships. 189 lines. The `Comparison Matrix` section is a structured table — not prose.

#### Epic example: [[Local Inference Engine (Subsystem 3)]]

```yaml
---
title: "Local Inference Engine (Subsystem 3)"
type: epic
domain: backlog
status: draft
priority: P1
task_type: epic
current_stage: document
readiness: 10
stages_completed: [document]
artifacts:
  - wiki/domains/tools-and-platforms/aicp.md
  - wiki/decisions/local-model-vs-cloud-api-for-routine-operations.md
---
```

Sections: Summary → Goals (bulleted list of what the epic achieves) → Done When (checkbox list — unchecked = not done) → Blocked (if applicable) → Relationships. The epic tracks readiness (10% = document stage done), lists artifacts produced so far, and has a `task_type: epic` field that determines which stages are required (all 5: document, design, scaffold, implement, test). Epics are NEVER marked "done" directly — their readiness is computed from child tasks.

#### Task example: [[Test OpenAI backend with LocalAI]]

```yaml
---
title: "Test OpenAI backend with LocalAI"
type: task
domain: backlog
status: blocked
priority: P1
epic: E001
task_type: task
current_stage: scaffold
readiness: 0
stages_completed: []
artifacts: []
depends_on: []
estimate: M
---
```

Sections: Summary → Done When (checkbox list). Tasks are the atomic work unit — they go through stages (for `task_type: task`, the required stages are scaffold, implement, test). The `epic: E001` field links to the parent. `estimate: M` indicates medium effort. `status: blocked` with `readiness: 0` and empty `stages_completed` means work hasn't started. Each stage completion gets its own git commit.

#### Note (directive) example: [[Never Stop at Surface — Depth Verification Rule]]

```yaml
---
title: "Never Stop at Surface — Depth Verification Rule"
type: note
domain: log
note_type: directive
status: active
---
```

Sections: Summary → Operator Directive (verbatim quote) → Interpretation. Notes in wiki/log/ are the operator's voice — directives are logged verbatim and never paraphrased. The `note_type` field distinguishes between `directive` (operator instruction), `session` (work summary), and `completion` (task done report). Log entries are chronological and append-only.

#### Backlog hierarchy in practice

```
E001-local-inference-engine (epic, P1, readiness=10%)
  └── T001-test-openai-backend (task, P1, blocked, readiness=0%)

E002-ecosystem-integration (epic, P2, readiness=15%)
  └── (tasks to be created)
```

Work happens on TASKS, not epics. To advance E001, you pick T001 and complete its next stage. Epic readiness = average of child readiness. Status flows upward: any child in-progress → parent in-progress. All children done → parent moves to "review" (not "done" — human confirms).

Task types determine which stages are required:

| task_type | Required stages |
|-----------|----------------|
| epic | document, design, scaffold, implement, test |
| module | document, design, scaffold, implement, test |
| task | scaffold, implement, test |
| research | document, design |
| evolve | document, implement |
| docs | document |
| bug | document, implement, test |
| refactor | document, scaffold, implement, test |

### Required Frontmatter Fields

Every page:

| Field | Type | What it defines |
|-------|------|----------------|
| `title` | string | Must match the `# Heading`. The page's identity. |
| `type` | enum | One of the 16 types above. Determines required sections. |
| `domain` | string | Knowledge domain. Must match the folder path. Domains grow organically. |
| `status` | enum | Lifecycle stage (see below). |
| `confidence` | enum | How certain: `low`, `medium`, `high`, `authoritative`. |
| `created` | date | When the page was created (YYYY-MM-DD). |
| `updated` | date | When last modified. |
| `sources` | list | Provenance chain — where this knowledge came from. |
| `tags` | list | For discovery and cross-referencing. |

### Optional Frontmatter Fields

| Field | Used by | What it defines |
|-------|---------|----------------|
| `layer` | All knowledge pages | Knowledge layer number (1-6, spine) |
| `maturity` | All knowledge pages | Lifecycle: `seed` → `growing` → `mature` → `canonical` |
| `derived_from` | L4-L6 pages | Source pages this was distilled from |
| `instances` | Patterns (L5) | Specific occurrences with page + context |
| `reversibility` | Decisions (L6) | `easy`, `moderate`, `hard`, `irreversible` |
| `complexity` | Any | `beginner`, `intermediate`, `advanced`, `expert` |
| `resolution` | Any | How thoroughly the topic is covered |
| `subdomain` | Concepts | Finer categorization within a domain |
| `aliases` | Any | Alternative names for the concept |
| `priority` | Backlog items | `P0`, `P1`, `P2`, `P3` |
| `task_type` | Backlog items | `epic`, `module`, `task`, `research`, `evolve`, `docs`, `bug`, `refactor` |
| `current_stage` | Backlog items | `document`, `design`, `scaffold`, `implement`, `test` |
| `readiness` | Backlog items | 0-100 percentage |
| `stages_completed` | Backlog items | List of completed stages |
| `artifacts` | Backlog items | Files produced as evidence |
| `estimate` | Backlog items | `XS`, `S`, `M`, `L`, `XL` |
| `epic` | Modules/tasks | Parent epic ID |
| `module` | Tasks | Parent module ID |
| `depends_on` | Tasks | Dependency list |
| `note_type` | Log entries | `directive`, `session`, `completion` |

### Status Lifecycle

Two separate lifecycles coexist:

**Knowledge pages**: `raw` → `processing` → `synthesized` → `verified` → `stale`

**Backlog items**: `draft` → `active` → `in-progress` → `review` → `done` → `archived` (or `blocked`)

### Maturity Lifecycle

| Level | Meaning | How you get there |
|-------|---------|-------------------|
| `seed` | Exists but unvalidated | Auto-generated or scaffolded |
| `growing` | Human-reviewed, real derived_from, passes quality gates | Review confirms quality |
| `mature` | Cross-referenced by others, stable 30+ days | Time + inbound references |
| `canonical` | Authoritative reference for its domain | Marked manually |

No auto-promotion. The pipeline SUGGESTS promotions but never changes maturity automatically.

### Source Provenance

Every `sources` entry requires:
- `id` — unique identifier (e.g., `src-karpathy-claude-code-10x`)
- `type` — one of: `article`, `youtube-transcript`, `paper`, `documentation`, `notes`, `paste`, `book`, `podcast-transcript`
- At least one of: `url` (web source) or `file` (local file path)

Optional: `title`, `ingested` (date).

### Relationship System

Relationships are explicit, typed, bidirectional via backlinks:

```markdown
## Relationships

- BUILDS ON: [[Page Title]]
- ENABLES: [[Another Page]]
- CONTRADICTS: [[Some Assumption]]
```

**Complete verb catalog (17 verbs):**

| Verb | Meaning |
|------|---------|
| BUILDS ON | This page extends or depends on the target |
| ENABLES | This page makes the target possible |
| COMPARES TO | Direct comparison exists |
| CONTRADICTS | This page disagrees with the target |
| USED BY | The target consumes this page's knowledge |
| RELATES TO | General connection |
| FEEDS INTO | This page's output flows into the target |
| DERIVED FROM | This page was synthesized from the target |
| SUPERSEDES | This page replaces the target |
| IMPLEMENTS | This page is a concrete implementation of the target |
| EXTENDS | This page adds to the target |
| CONSTRAINS | This page limits the target |
| CONSTRAINED BY | This page is limited by the target |
| PARALLELS | Similar structure or approach |
| SYNTHESIZES | This page combines multiple targets |
| ENABLED BY | Inverse of ENABLES |
| CONTRASTS WITH | Different approach to same problem |

Format: `^([A-Z][A-Z /\-]+?):\s*(.+)$` — compatible with OpenFleet's kb_sync.py regex.

### Page Templates

Templates live in `config/templates/` with `{{placeholder}}` variables. Six templates:

| Template | Layer | Placeholders |
|----------|-------|-------------|
| lesson.md | L4 | `{{title}}`, `{{domain}}`, `{{date}}`, `{{derived_page_1}}` |
| pattern.md | L5 | Same + `{{derived_page_2}}`, `{{instance_1}}`, `{{instance_2}}` |
| decision.md | L6 | Same + default `reversibility: moderate` |
| domain-overview.md | Spine | `{{domain}}`, `{{domain_name}}`, `{{date}}` |
| learning-path.md | Spine | `{{title}}`, `{{date}}` |
| evolution.md | Spine | `{{title}}`, `{{date}}`, `{{concept}}` |

Templates define the section structure with HTML comment guidance:
```markdown
## Insight
<!-- The core learning. Min 50 words. State it plainly. -->
```

### Quality Gates

Every page must pass:

1. Valid frontmatter per wiki-schema.yaml
2. All required sections for the page type present
3. Summary ≥ 30 words
4. At least 1 relationship (unless first in a new domain)
5. Title field matches # Heading
6. Domain field matches folder path
7. Source provenance (at least one source with url or file)
8. No > 70% concept overlap with existing pages
9. Source-synthesis pages ≥ 0.25 line ratio to raw file length

Backlog items additionally: warn if `task_type` missing, warn if `readiness` > 0 but `stages_completed` empty.

### Three Core Operations

**Ingest**:
1. Source arrives (URL, file, paste)
2. Save to raw/ (permanent provenance)
3. Read the FULL source (multiple reads for >200 lines)
4. Verify depth: examine real INSTANCES not just descriptions (Layer 0 → Layer 1)
5. Create source-synthesis page in wiki/sources/
6. Create/update concept pages in wiki/domains/
7. Validate all pages against schema

**Query**:
- Navigate via domain `_index.md` files and relationship links
- The LLM reads the index, follows links, reads content
- No vector database needed below ~200 pages
- Above ~200 pages: add graph-enhanced retrieval as an additive layer

**Lint**:
- Validate all pages against schema
- Detect orphaned relationship targets
- Flag stale content (source updated after derived page)
- Report gaps: weak domains, thin pages, unanswered questions
- Surface contradictions between pages

### Evolution Pipeline

1. **Score** — 6 deterministic signals: tag co-occurrence, cross-source convergence, relationship hubs, domain layer gaps, open question density, orphaned references
2. **Scaffold** — create page stubs from templates with `{{placeholder}}` variables
3. **Generate** — fill pages from source material (any LLM — session, local model, API)
4. **Validate** — run quality gates
5. **Review** — maturity promotion: seed → growing → mature → canonical (never auto-promoted)

### Scale Boundary

Below ~200 pages: index-driven navigation is cheaper and more accurate than vector search.

Above ~200 pages: add graph-enhanced retrieval (e.g., LightRAG with BM25 + vector + graph traversal) as an ADDITIVE layer. The wiki structure stays the same — the retrieval layer indexes it.

See [[Decision: Wiki-First with LightRAG Upgrade Path]].

### How to Adopt

1. Create the repository structure above
2. Copy and adapt `config/wiki-schema.yaml` for your domain (types, fields, sections)
3. Create page templates in `config/templates/` per page type
4. Write agent instructions (CLAUDE.md) with schema, conventions, quality gates
5. Start ingesting sources — the wiki grows from ingestion
6. After each change, validate against the schema
7. Periodically evolve: score candidates → scaffold → generate → review maturity

Full guide: [[Adoption Guide — How to Use This Wiki's Standards]]

### Reference Implementation

This research wiki is the reference implementation. 146+ pages, 1,086+ relationships, 10 domains, 6 knowledge layers populated. Project-specific implementation details (Python tooling, CLI commands, MCP tools, sync services) are documented in the project's CLAUDE.md. They are NOT part of the universal model.

### Key Pages

| Page | Role in the model |
|------|-------------------|
| [[LLM Wiki Pattern]] | Karpathy's original design — the foundational pattern |
| [[Wiki Ingestion Pipeline]] | How sources become structured pages |
| [[Wiki Knowledge Graph]] | How relationships create a queryable graph |
| [[LLM Knowledge Linting]] | How quality is maintained automatically |
| [[Knowledge Evolution Pipeline]] | How pages evolve through density layers |
| [[Progressive Distillation]] | The pattern: raw → synthesis → lesson → pattern → decision |
| [[LLM Wiki vs RAG]] | When wiki navigation outperforms vector search |
| [[Decision: Wiki-First with LightRAG Upgrade Path]] | The scale decision |
| [[Second Brain Architecture]] | PKM theory mapped to this model |
| [[Wiki Backlog Pattern]] | How the wiki tracks its own work |

### Lessons Learned

From building with this model — validated experience:

| Lesson | What was learned |
|--------|-----------------|
| [[LLM-Maintained Wikis Outperform Static Documentation]] | Maintenance economics is the differentiator |
| [[Lesson: Schema Is the Real Product — Not the Content]] | Schema survives; content is regenerable |
| [[Multi-Stage Ingestion Beats Single-Pass Processing]] | Each pass discovers what the previous missed |
| [[Never Synthesize from Descriptions Alone]] | Read the THING, not the description |
| [[Shallow Ingestion Is Systemic, Not Isolated]] | One defect = audit ALL similar artifacts |
| [[Automated Knowledge Validation Prevents Silent Wiki Decay]] | Without linting, wikis decay silently |

## Open Questions

- What is the minimum viable wiki for a new project? (Smallest structure that demonstrates value)
- How should multi-author editing work? (Conflict resolution when multiple agents contribute)
- What is the optimal schema complexity for a new adopter? (Start minimal and grow, or start comprehensive?)
- How does this model interact with existing documentation systems in organizations?

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
