---
title: Model — LLM Wiki
aliases:
  - "Model — LLM Wiki"
  - "Model: LLM Wiki"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: authoritative
maturity: growing
created: 2026-04-09
updated: 2026-04-13
sources:
  - id: src-karpathy-llm-wiki-idea-file
    type: documentation
    file: raw/articles/karpathy-llm-wiki-idea-file.md
    title: Karpathy LLM Wiki Idea File
    ingested: 2026-04-08
  - id: src-llm-wiki-v2-agentmemory
    type: documentation
    file: raw/articles/llm-wiki-v2-extending-karpathys-llm-wiki-pattern-with-lessons-from-building-agen.md
    title: LLM Wiki v2 — Extending Karpathy's Pattern with Agentmemory Lessons
    ingested: 2026-04-08
tags: [llm-wiki, model, knowledge-system, schema, ingestion, evolution, standards, transferable]
---
# Model — LLM Wiki
## Summary

The LLM Wiki model defines a knowledge system where an LLM agent maintains a structured markdown wiki — ingesting sources, synthesizing pages, cross-referencing relationships, evolving insights through density layers, and linting for quality. The model solves the wiki maintenance problem: wikis historically die because humans abandon upkeep. With an LLM handling all mechanical operations, the wiki compounds knowledge instead of decaying. This model is technology-agnostic — it defines structure and rules, not tools.

This is one of 14+ named models that a wiki can contain. The [[methodology-framework|Methodology Framework]] is the super-model that governs HOW work is done. This page defines WHAT the wiki IS. See [[model-methodology|Model — Methodology]] for the work process.

## Key Insights

> [!tip] Maintenance economics: LLMs eliminate the fatal flaw
> Wikis fail from abandoned upkeep, not lack of content. Making the LLM handle ALL bookkeeping — cross-references, indexes, validation, relationship discovery — eliminates this structurally. The cost of maintenance drops to near-zero.

> [!info] Three core operations
>
> | Operation | What It Does | Tooling |
> |-----------|-------------|---------|
> | **Ingest** | Source → structured pages with relationships | `pipeline run`, wiki-agent skill |
> | **Query** | Navigate via indexes + relationships, synthesize answers | MCP wiki_search, skill-guided reads |
> | **Lint** | Validate, detect orphans, flag contradictions, check staleness | `pipeline post`, `tools/lint.py` |

- The schema is the real product — content is regenerable from raw sources; the schema that constrains content encodes irreplaceable operational knowledge.
- Knowledge compounds through density layers — each layer denser and more actionable than the previous.
- A wiki hosts multiple named MODELS. Each model is a coherent system with entry point, pages, and standards. The wiki is the container; models are the organized knowledge within it.
- **Dual-scope operation** — the wiki serves both as a project's local knowledge base (`--wiki-root`) AND as a shared second brain (`--brain`). The gateway unifies both scopes through a single CLI/MCP interface.
- **Progressive distillation reaches principles** — knowledge evolves L0 (raw) → L1 (synthesis) → L2 (concept) → L3 (comparison) → L4 (lesson) → L5 (pattern) → L6 (decision) → Principle. Maturity-based folders (`00_inbox` → `04_principles`) make this physical.

## Deep Analysis

### Core Architecture

An LLM Wiki has three layers:

1. **Raw layer** — unprocessed source material. Never modified after ingestion. Permanent provenance.
2. **Wiki layer** — structured markdown pages with YAML frontmatter, typed relationships, quality gates. Also contains the backlog (project management) and log (operator directives).
3. **Meta layer** — schema, templates, validation rules. Defines how the wiki works.

The distinction between `config/` (meta layer — schema, templates) and `wiki/config/` (wiki layer — methodology, agent directive) is intentional:
- `wiki/config/wiki-schema.yaml` and `wiki/config/templates/` define the wiki's STRUCTURE — page types, fields, validation rules. These rarely change.
- `wiki/config/methodology.yaml` and `wiki/config/agent-directive.md` define the WORK PROCESS — stages, task types, execution modes. These evolve with the project.

### Repository Structure

```
{project-root}/
├── raw/                          # Raw layer — immutable source provenance
│   ├── articles/                 # Web content, READMEs, docs
│   ├── transcripts/              # Video/audio transcripts
│   └── notes/                    # Legacy notes
│
├── wiki/                         # Wiki layer — living knowledge + PM + log
│   ├── domains/{domain}/         # L2 concept pages by domain
│   ├── sources/                  # L1 source-synthesis pages
│   ├── comparisons/              # L3 comparison pages
│   ├── lessons/                  # L4 codified experience
│   ├── patterns/                 # L5 recurring structures
│   ├── decisions/                # L6 choice frameworks
│   ├── spine/                    # Navigation: model guides, overviews, adoption guide
│   ├── backlog/                  # Project management: epics/, modules/, tasks/
│   │   ├── epics/               # E001-name.md, E002-name.md, ...
│   │   ├── modules/             # M001-name.md, M002-name.md, ...
│   │   └── tasks/               # T001-name.md, T002-name.md, ...
│   ├── log/                      # Operator directives, session logs, completion notes
│   └── config/                   # Work process definition
│       ├── methodology.yaml      # Stage gates, task types, execution modes
│       └── agent-directive.md    # Work loop, rules, quality gates
│
├── config/                       # Meta layer — wiki structure definition
│   ├── wiki-schema.yaml          # Page validation schema (types, fields, sections)
│   └── templates/                # Scaffolding templates per page type
│
└── {project-specific}/           # Whatever else the project needs (tools/, src/, etc.)
```

### Naming Conventions

- **Filenames**: kebab-case always (`claude-code-best-practices.md`, not `ClaudeCodeBestPractices.md`)
- **Source pages**: prefixed with `src-` (`src-karpathy-claude-code-10x.md`)
- **Backlog IDs**: sequential numbering (`E001-name.md` for epics, `M001-name.md` for modules, `T001-name.md` for tasks)
- **Domain folders**: kebab-case, grow organically as needed
- **Index files**: `_index.md` in every directory, auto-maintained
- **One concept per page**: never combine unrelated topics. If a page covers two concepts, split it.

### Domain Growth Rules

Domains are knowledge categories. They grow organically:

- **When to create a new domain**: when 3+ pages cluster around a topic not covered by existing domains. Don't create a domain for one page.
- **Domain naming**: kebab-case, broad enough for 5-15 pages. `ai-agents` not `claude-code-specific`.
- **Domain field must match folder path**: a page in `wiki/domains/ai-agents/` has `domain: ai-agents`.
- **Every domain gets an `_index.md`**: auto-generated, lists all pages with summaries.
- **Domain overviews** (in `wiki/spine/domain-overviews/`): curated summary per domain — what's known, what's thin, priorities, FAQ.

### Knowledge and Operational Layers

| Layer | Directory | Purpose | Content type |
|-------|-----------|---------|-------------|
| L0 | raw/ | Unprocessed evidence | Fetched articles, transcripts, notes |
| L1 | wiki/sources/ | Source synthesis | One synthesis per source |
| L2 | wiki/domains/ | Core knowledge | One concept per page, by domain |
| L3 | wiki/comparisons/ | Structured comparisons | Matrix tables comparing alternatives |
| L4 | wiki/lessons/ | Codified experience | Distilled from L1-L3 with evidence |
| L5 | wiki/patterns/ | Recurring structures | 2+ instances across contexts |
| L6 | wiki/decisions/ | Choice frameworks | Alternatives + rationale |
| Spine | wiki/spine/ | Navigation | Model guides, overviews, adoption guide |
| Backlog | wiki/backlog/ | Project management | Epics, modules, tasks with stage gates |
| Log | wiki/log/ | Operator voice | Directives (verbatim), session logs |
| Config | wiki/config/ | Work process | methodology.yaml, agent-directive.md |

Knowledge layers (L0-L6) implement [[progressive-distillation|Progressive Distillation]]: raw → synthesis → concept → lesson → pattern → decision.

### Complete Page Type Catalog

16 page types. Each has a purpose, required sections, and guidance:

**Knowledge page types:**

| Type | Purpose | Required sections | When to use |
|------|---------|------------------|-------------|
| **concept** | Core knowledge — one idea per page | Summary, Key Insights, Deep Analysis, Relationships | Most pages. Any topic needing structured explanation. |
| **source-synthesis** | Extraction from one source | Summary, Key Insights, Relationships | After ingesting a URL, transcript, or doc. One per source. |
| **comparison** | Structured comparison with matrix | Summary, Comparison Matrix, Key Insights, Deep Analysis, Relationships | When 2+ alternatives need side-by-side evaluation. Matrix is a TABLE. |
| **reference** | Quick-reference page | Summary, Relationships | Cheat sheets, lookup tables. Minimal depth, maximum utility. |
| **deep-dive** | Extended analysis | Summary, Key Insights, Deep Analysis, Relationships | When a topic needs more depth than a concept page. |
| **index** | Navigation page | (none required) | `_index.md` files. Auto-generated. Don't create manually. |
| **lesson** | Codified experience (L4) | Summary, Context, Insight, Evidence, Applicability, Relationships | When sources converge on an insight or a failure teaches something. Requires evidence. |
| **pattern** | Recurring structure (L5) | Summary, Pattern Description, Instances, When To Apply, When Not To, Relationships | When the same structure appears in 2+ independent contexts. Must have concrete instances. |
| **decision** | Choice framework (L6) | Summary, Decision, Alternatives, Rationale, Reversibility, Dependencies, Relationships | When a choice needs evidence-backed documentation. |
| **domain-overview** | Domain state summary | Summary, State of Knowledge, Maturity Map, Gaps, Priorities, Key Pages, Relationships | One per domain. Curated assessment of domain health. |
| **learning-path** | Ordered reading guide | Summary, Prerequisites, Sequence, Outcomes, Relationships | For guiding someone through a topic in order. Model entry points use this. |
| **evolution** | How a concept changed over time | Summary, Timeline, Key Shifts, Current State, Relationships | For tracking how understanding evolved across sessions. |

**Backlog and log page types:**

| Type | Purpose | Required sections | When to use |
|------|---------|------------------|-------------|
| **epic** | Large initiative | Summary, Goals, Done When, Relationships | Work spanning weeks with multiple deliverables. |
| **module** | Scoped deliverable | (same as epic) | Coherent component within an epic. |
| **task** | Atomic work unit | Summary, Done When | Single focused piece, completable in one session. |
| **note** | Log entry | Summary | Directives (verbatim), session summaries, completion notes. |

### Required Frontmatter Fields

Every page must have these 9 fields:

| Field | Type | What it defines |
|-------|------|----------------|
| `title` | string | Must match the `# Heading`. The page's identity. |
| `type` | enum | One of the 16 types. Determines required sections. |
| `domain` | string | Knowledge domain. Must match folder path. |
| `status` | enum | Lifecycle stage (see Status Lifecycle below). |
| `confidence` | enum | `low` (speculation), `medium` (partially sourced), `high` (well-sourced), `authoritative` (primary source / direct experience). |
| `created` | date | When created (YYYY-MM-DD). |
| `updated` | date | When last modified. Used for staleness detection. |
| `sources` | list | Provenance chain. Each entry: `{id, type, url|file}`. |
| `tags` | list | For discovery and cross-referencing. Kebab-case. |

### Optional Frontmatter Fields

| Field | Used by | What it defines |
|-------|---------|----------------|
| `layer` | Knowledge pages | Layer number (1-6) or `spine`. |
| `maturity` | Knowledge pages | `seed` → `growing` → `mature` → `canonical`. |
| `derived_from` | L4-L6 pages | Page titles this was distilled from. Evolution provenance. |
| `instances` | Patterns (L5) | `{page, context}` entries — concrete occurrences. |
| `reversibility` | Decisions (L6) | `easy`, `moderate`, `hard`, `irreversible`. |
| `complexity` | Any page | Reader skill level: `beginner`/`intermediate`/`advanced`/`expert`. Helps sequence learning paths. |
| `subdomain` | Concepts | Finer categorization when a domain grows large. |
| `aliases` | Any page | Alternative names (e.g., "SFIF" for "Scaffold-Foundation-Infrastructure-Features"). |
| `priority` | Backlog | `P0` (critical) / `P1` (high) / `P2` (medium) / `P3` (low). |
| `task_type` | Backlog | Determines required stages. See [[stage-gate-methodology|Stage-Gate Methodology]]. |
| `current_stage` | Backlog | `document` / `design` / `scaffold` / `implement` / `test`. |
| `readiness` | Backlog | 0-100%. Computed from stages completed vs required. |
| `stages_completed` | Backlog | List of finished stages with verified artifacts. |
| `artifacts` | Backlog | File paths produced as evidence. |
| `estimate` | Backlog | `XS` (minutes) / `S` (hour) / `M` (half-day) / `L` (day) / `XL` (multi-day). |
| `epic` | Modules/tasks | Parent epic ID (e.g., `E001`). |
| `module` | Tasks | Parent module ID (e.g., `M001`). |
| `depends_on` | Tasks | Task IDs that must complete first. |
| `note_type` | Log entries | `directive` / `session` / `completion`. |

Note: `resolution` is reserved for future use (depth of coverage) but not yet formally defined.

### Status Lifecycle

Two separate lifecycles:

**Knowledge pages**: `raw` → `processing` → `synthesized` → `verified` → `stale`
- `raw`: just created, unreviewed
- `processing`: being worked on
- `synthesized`: complete, passes quality gates
- `verified`: human-confirmed accurate
- `stale`: sources updated since this page was last revised

**Backlog items**: `draft` → `active` → `in-progress` → `review` → `done` → `archived`
- `draft`: planned, not started
- `active`: ready to pick up
- `in-progress`: someone working on it
- `review`: work done, awaiting human review
- `done`: confirmed complete
- `archived`: no longer relevant
- `blocked`: cannot proceed (dependency or external blocker)

### Maturity Lifecycle

| Level | Meaning | How you get there |
|-------|---------|-------------------|
| `seed` | Exists but unvalidated | Auto-generated or scaffolded |
| `growing` | Reviewed, real derived_from, passes quality gates | Human review confirms |
| `mature` | Cross-referenced by others, stable 30+ days | Time + inbound references |
| `canonical` | Authoritative reference for its domain | Marked manually |

No auto-promotion. The system SUGGESTS promotions; a human confirms.

### Source Provenance

Every `sources` entry requires:
- `id` — unique identifier (e.g., `src-karpathy-claude-code-10x`)
- `type` — one of: `article`, `youtube-transcript`, `paper`, `documentation`, `notes`, `paste`, `book`, `podcast-transcript`
- At least one of: `url` (web source) or `file` (local path)

Optional: `title`, `ingested` (date).

### Relationship System

Relationships are explicit, typed, bidirectional via auto-generated backlinks:

```markdown
## Relationships

- BUILDS ON: `[[Page Title]]`
- ENABLES: `[[Another Page]]`
- CONTRADICTS: `[[Some Assumption]]`
```

**17 relationship verbs:**

| Verb | Meaning |
|------|---------|
| BUILDS ON | Extends or depends on the target |
| ENABLES | Makes the target possible |
| COMPARES TO | Direct comparison exists |
| CONTRADICTS | Disagrees with the target |
| USED BY | Target consumes this page's knowledge |
| RELATES TO | General connection (prefer specific verbs) |
| FEEDS INTO | Output flows into the target |
| DERIVED FROM | Synthesized from the target (evolution provenance) |
| SUPERSEDES | Replaces the target |
| IMPLEMENTS | Concrete implementation of the target |
| EXTENDS | Adds to the target |
| CONSTRAINS | Limits the target |
| CONSTRAINED BY | Limited by the target |
| PARALLELS | Similar structure or approach |
| SYNTHESIZES | Combines multiple targets |
| ENABLED BY | Inverse of ENABLES |
| CONTRASTS WITH | Different approach to same problem |

Format: `- VERB: `[[Target]]`` — one per line. Regex: `^([A-Z][A-Z /\-]+?):\s*(.+)$`

### Page Templates

Templates in `wiki/config/templates/` use `{{placeholder}}` variables for scaffolding. Six templates exist:

| Template | Layer | Key structure |
|----------|-------|--------------|
| lesson.md | L4 | Summary → Context → Insight (min 50 words) → Evidence → Applicability → Relationships |
| pattern.md | L5 | Summary → Pattern Description (min 100 words) → Instances (2+) → When To Apply → When Not To → Relationships |
| decision.md | L6 | Summary → Decision → Alternatives (min 2) → Rationale (min 100 words) → Reversibility → Dependencies → Relationships |
| domain-overview.md | Spine | Summary → State of Knowledge → Maturity Map → Gaps → Priorities → Key Pages → FAQ → Relationships |
| learning-path.md | Spine | Summary → Prerequisites → Sequence → Outcomes → Relationships |
| evolution.md | Spine | Summary → Timeline → Key Shifts → Current State → Relationships |

Templates include HTML comment guidance (e.g., `<!-- Min 50 words. State it plainly. -->`). Concept, source-synthesis, comparison, reference, and deep-dive types don't have templates — their structure is defined by the required sections in the schema.

### Quality Gates

Every page must pass:

1. Valid frontmatter per wiki-schema.yaml (all required fields, enums match)
2. All required sections for the page type present
3. Summary ≥ 30 words
4. At least 1 relationship (unless first page in a new domain)
5. Title field matches # Heading exactly
6. Domain field matches folder path
7. Source provenance (at least one source with url or file)
8. No > 70% concept overlap with existing pages (update instead of create)
9. Source-synthesis pages: ≥ 0.25 line ratio to raw file length (a 400-line raw file → wiki page must be ≥ 100 lines)

**When a gate fails**: the page is NOT published/committed. Fix the issue, then re-validate. The methodology's stage-gate system (see [[Stage-Gate Methodology]]) enforces that quality gates pass before advancing to the next stage.

Backlog items additionally: warn if `task_type` missing, warn if `readiness` > 0 but `stages_completed` empty.

### Three Core Operations

**Ingest**:
1. Source arrives (URL, file, paste)
2. Save to raw/ — permanent provenance, never deleted
3. Read the COMPLETE source before synthesizing — all of it, not just the beginning
4. **Depth verification**: if the source DESCRIBES a format, tool, or pattern, examine a real INSTANCE of that thing. A README about DESIGN.md files is Layer 0 (description). An actual DESIGN.md file is Layer 1 (instance). Must reach Layer 1. This is how you avoid synthesizing from surfaces — see [[Never Synthesize from Descriptions Alone]].
5. Create source-synthesis page in wiki/sources/ (prefixed `src-`)
6. Create/update concept pages in wiki/domains/
7. Validate all pages against schema — fail = fix before committing

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

### Backlog and Stage-Gate

The wiki manages its own work through a backlog. The full stage-gate system — task types, required stages per type, stage definitions, quality gates per stage, execution modes, end conditions — is defined in [[Stage-Gate Methodology]] and [[Task Type Artifact Matrix]]. The key rules:

- **Hierarchy**: EPIC → MODULE → TASK. Work on tasks, not epics.
- **Readiness flows upward**: epic readiness = average of children.
- **Status flows upward**: any child in-progress → parent in-progress. All children done → parent moves to "review" (human confirms "done").
- **Stages**: document → design → scaffold → implement → test. Each task type requires a subset. See [[Task Type Artifact Matrix]] for the full matrix.
- **One commit per stage**. Do not advance until the stage's quality gate passes.

Methodology files: `wiki/config/methodology.yaml` (machine-readable) and `wiki/config/agent-directive.md` (human-readable work loop).

### Evolution Pipeline

1. **Score** — 6 deterministic signals: tag co-occurrence, cross-source convergence, relationship hubs, domain layer gaps, open question density, orphaned references
2. **Scaffold** — create page stubs from templates
3. **Generate** — fill pages from source material (any LLM)
4. **Validate** — run quality gates (fail = fix, not skip)
5. **Review** — maturity promotion: seed → growing → mature → canonical (never auto-promoted)

### Maturity-Based Folder Structure

Evolved knowledge pages (lessons, patterns, decisions) organize into maturity-based subfolders that reflect their quality level:

> [!info] Folder Maturity Pipeline
>
> | Folder | What's In It | Promotion Criteria |
> |--------|-------------|-------------------|
> | `00_inbox/` | New contributions, just arrived | Has frontmatter, passes validation |
> | `01_drafts/` | Early content, thin | Needs more evidence or depth |
> | `02_synthesized/` | Has evidence, needs validation | ≥80 lines, evidence present |
> | `03_validated/` | Full evidence, self-check, navigation weave | ≥100 lines, self-check section, navigation section, ≥2 evidence items |
> | `04_principles/` | Distilled from ≥3 validated items | ≥3 validated lessons converge on same mechanism |

The scalability rule: when any folder exceeds ~10 items, add sub-structure (clusters/, related/, unrelated/). This keeps browsing manageable at every level.

Currently the research wiki has: 40 validated lessons, 15 validated patterns, 3 principles (hypothesis). Zero inbox, zero drafts, zero synthesized — everything was promoted during the 2026-04-12 session. The inbox is ready for new incoming knowledge from source ingestion.

### Dual-Scope: Second Brain AND Project Wiki

The wiki tools work in TWO directions:

> [!abstract] Dual-Scope Operations
>
> | Direction | What Happens | How |
> |-----------|-------------|-----|
> | **Project → Second Brain** | Project queries methodology, standards, chains, templates | `gateway query --stage document --wiki-root ~/brain` or auto-detect |
> | **Second Brain → Project** | Standards applied to project's own wiki pages | Project runs pipeline tools on its own wiki |
> | **Project → Second Brain (feedback)** | Project contributes learnings back | `gateway contribute --type lesson --wiki-root ~/brain` |
> | **Self (second brain = project)** | The wiki operates on itself | Default mode — no --wiki-root needed |

The `--wiki-root` flag targets a project wiki. The `--brain` flag targets the second brain. Auto-detection finds the second brain in sibling directories. When running ON the second brain itself, both are the same.

### Scale Boundary

> [!warning] ~200 pages is the index-navigation ceiling
> Below ~200: index-driven navigation is cheaper and more accurate than vector search. Above ~200: add graph-enhanced retrieval (LightRAG) as an ADDITIVE layer — the wiki stays the same, the retrieval layer indexes it. See [[Decision — Wiki-First with LightRAG Upgrade Path]].

### How to Adopt

1. **Create the repository structure** — raw/, wiki/ (with all subdirectories), config/. The structure above is the reference.
2. **Define your schema** — copy `wiki/config/wiki-schema.yaml`. For a code project: add types like `api-spec` or `architecture`, remove types you won't use. For a research wiki: the default types work well. For a small project: start with `concept`, `source-synthesis`, `lesson`, `decision` — add more as the wiki grows.
3. **Create page templates** — at minimum: lesson, pattern, decision. Templates define section structure + placeholder variables. Copy from `wiki/config/templates/`.
4. **Write agent instructions** — CLAUDE.md (or equivalent) must include: schema conventions, naming rules, quality gates, the three operations. The agent reads this at session start.
5. **Adapt quality gates** — the GATES are universal (frontmatter valid, sections present, summary ≥30 words). The COMMANDS that check them are project-specific (Python validator, TypeScript linter, manual checklist).
6. **Start ingesting** — 5-10 sources build the initial knowledge base. The wiki grows from there.
7. **Evolve periodically** — after 20+ pages, score candidates and generate lessons/patterns/decisions from what exists.

Full guide: [[Adoption Guide — How to Use This Wiki's Standards]]

### Key Examples

Two inline examples showing the most important types. For all 9 type examples with full frontmatter, see the reference implementation's actual pages.

**Lesson example** — [[Context Management Is the Primary LLM Productivity Lever]]:
102 lines. Frontmatter: `type: lesson`, `layer: 4`, `maturity: growing`, `derived_from: ["Claude Code Best Practices", "Synthesis: Claude Code Accuracy Tips", "Synthesis: Claude Code Harness Engineering"]`. Sections: Summary → Context → Insight (context is the variable you control, not model capability) → Evidence (4 independent sources: Boris Cherny's 95% confidence rule, degradation curve, harness guardrails, shanraisshan's architecture) → Applicability → Relationships. Evidence references specific data points, not vague claims.

**Pattern example** — [[Scaffold → Foundation → Infrastructure → Features]]:
176 lines. Frontmatter: `type: pattern`, `layer: 5`, `maturity: growing`, `instances: [{page: "Research Wiki", context: "..."}, {page: "OpenFleet", context: "..."}, {page: "AICP", context: "..."}]`. Sections: Summary → Pattern Description (exit criteria per stage) → Instances (4 detailed) → When To Apply → When Not To → Relationships. The `instances` field is key — a pattern without instances is a hypothesis.

### Reference Implementation

This research wiki is the reference implementation. Project-specific details (Python tooling, CLI commands, MCP tools, sync services, slash commands) are in the project's CLAUDE.md. They are NOT part of the universal model.

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
| [[Decision — Wiki-First with LightRAG Upgrade Path]] | The scale decision |
| [[Second Brain Architecture]] | PKM theory (PARA, Zettelkasten) mapped to this model |
| [[Wiki Backlog Pattern]] | How the wiki tracks its own work |

### Quality Standards

See [[LLM Wiki Standards — What Good Looks Like]] for the gold-standard example of each page type, what makes each one good, and the anti-patterns to avoid. The standards page is the companion to this model — the model defines structure, the standards define quality.

### Frontmatter as Programmatic Interface

Every YAML frontmatter field is not just metadata — it is the interface through which tools, agents, MCP servers, and enforcement systems read and act on page state. A complete reference of every field, what it enables, and what automation reads it is at [[Frontmatter Field Reference — Complete Parameter Documentation]].

Key fields for work management: `readiness` (definition completeness) and `progress` (execution completeness) are TWO independent dimensions tracked at every hierarchy level. See [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]].

### Gateway Vision

The wiki is evolving toward a unified gateway interface (Python CLI + MCP + programmatic API) that serves humans, AI agents, and external tools through one engine. Operations include: query by stage/domain/chain, archive/move with reference updates, agent write-back (remarks, lessons, corrections), config visualization, and template access. See [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]] for the epic.

### Lessons Learned

From building with this model — validated experience:

| Lesson | What was learned |
|--------|-----------------|
| [[llm-maintained-wikis-outperform-static-documentation|LLM-Maintained Wikis Outperform Static Documentation]] | Maintenance economics is the differentiator |
| [[schema-is-the-real-product|Lesson — Schema Is the Real Product — Not the Content]] | Schema survives; content is regenerable |
| [[multi-stage-ingestion-beats-single-pass|Multi-Stage Ingestion Beats Single-Pass Processing]] | Each pass discovers what the previous missed |
| [[never-synthesize-from-descriptions-alone|Never Synthesize from Descriptions Alone]] | Read the THING, not the description (Layer 0 → Layer 1) |
| [[shallow-ingestion-is-systemic-not-isolated|Shallow Ingestion Is Systemic, Not Isolated]] | One defect = audit ALL similar artifacts |
| [[automated-knowledge-validation-prevents-wiki-decay|Automated Knowledge Validation Prevents Silent Wiki Decay]] | Without linting, wikis decay silently |
| [[new-content-must-integrate-into-existing-pages|New Content Must Integrate Into Existing Pages]] | If entry points don't link to it, it doesn't exist |
| [[hardcoded-instances-fail-build-frameworks-not-solutions|Hardcoded Instances Fail — Build Frameworks Not Solutions]] | Copy values ≠ build framework. Portability test. |
| [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]] | Markdown IS the programming language for AI. Consistent structure > content. |

### State of Knowledge

> [!success] **Well-covered**
> - Complete page type catalog (19 types including milestone + principle added the 2026-04-12 session)
> - Maturity-based folder structure (00_inbox→04_principles) implemented and populated
> - 3 core operations (ingest, query, lint) with real tooling (pipeline, gateway, MCP server)
> - Evolution pipeline running (scores, promotes, detects staleness)
> - Gateway tools with dual-scope (second brain + project wiki)
> - Frontmatter as programmatic interface — every field documented with automation enablement
> - Agent write-back (contribute command) creates structured entries in inbox
> - 9 lessons from building with this model, each backed by specific incidents

> [!warning] **Thin or unverified**
> - Multi-agent wiki co-authoring — untested, potential for merge conflicts
> - Location mapping — implemented but never used in practice (no pages archived yet)
> - Scale beyond 280 pages — approaching the ~200 ceiling where LightRAG becomes needed
> - Enterprise coexistence (Confluence/Notion alongside LLM Wiki)
> - Minimal viable wiki — the simplest structure that works hasn't been tested empirically

## Open Questions

> [!question] ~~What is the minimum viable wiki?~~
> **RESOLVED:** Depends on identity profile. Solo + POC + micro: raw/ + wiki/domains/ + 1 template is enough. The simplified SDLC chain defines the minimal process. See [[goldilocks-flow|Goldilocks Flow — From Identity to Action]] for the full identity-to-chain routing. (Remaining: test empirically on a fresh project — E016)

> [!question] ~~How do multiple agents co-author a wiki without conflicts?~~
> **RESOLVED:** File-level partitioning + git merge + harness-resolved conflicts. Each agent works different files. OpenFleet contribution gating prevents overlap.
> OpenFleet has 10 agents but they don't write to the wiki simultaneously. The contribution system gates inputs. Real multi-agent co-authoring remains untested. (Requires: multi-agent testing)

> [!question] ~~When does LightRAG become necessary?~~
> **RESOLVED:** When keyword search + relationship traversal can't find cross-domain answers. ~200+ pages with dense relationships. Wiki at 296 pages — approaching threshold.
> The wiki is at ~280 pages — above the ~200 index-navigation ceiling. LightRAG integration is designed but not deployed. (Requires: benchmarking search accuracy with current page count)

### How This All Weaves Together — Navigation from This Page

> [!abstract] From LLM Wiki → Everywhere
>
> | You Want To Know... | Go To |
> |---------------------|-------|
> | **"How does methodology govern wiki work?"** | [[model-methodology|Model — Methodology]] — 9 models, stage gates, the super-model that governs ALL work |
> | **"What level of wiki do I need?"** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] — identity profile determines wiki scope: second brain vs project wiki vs both |
> | **"What fields does every page need?"** | [[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]] — 9 required, 20+ optional, each enables specific automation |
> | **"How do I track work in the wiki?"** | [[backlog-hierarchy-rules|Backlog Hierarchy Rules]] — Milestone→Epic→Module→Task, [[readiness-vs-progress|Readiness vs Progress — Two-Dimensional Work Tracking]] |
> | **"How do agents consume the wiki?"** | [[ai-methodology-consumption-guide|How AI Agents Consume the Methodology Wiki]] — 4 entry paths, 3 consumption modes |
> | **"What does 'good' look like per page type?"** | [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] — gold-standard exemplar per type |
> | **"How do I adopt this for my project?"** | [[methodology-adoption-guide|Methodology Adoption Guide]] — 4 tiers, per-domain quick starts |
> | **"What tools exist for wiki operations?"** | [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]] — planned unified interface for humans, agents, and MCP |
> | **"Where does memory vs wiki content go?"** | Memory = ephemeral per-session. Wiki = shared project knowledge. Default to wiki. See OpenArms lesson on memory/wiki conflation (7th failure class). |
>
> **Dual-scope principle:** Wiki tools work on BOTH the second brain (information hub) AND project-internal wikis. One toolset, two contexts. A project queries the second brain for standards, then applies them to its own wiki.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Quality standards for wiki pages** | [[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]] |
> | **Per-type standards** | `wiki/spine/standards/{type}-page-standards.md` |
> | **Methodology model (how work proceeds)** | [[model-methodology|Model — Methodology]] |
> | **Super-model (all models)** | [[super-model|Super-Model]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Domain chains** | [[domain-chain-typescript|TypeScript]], [[domain-chain-python-wiki|Python-Wiki]], [[domain-chain-infrastructure|Infrastructure]], [[domain-chain-knowledge|Knowledge]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- FEEDS INTO: [[model-second-brain|Model — Second Brain]]
- FEEDS INTO: [[model-ecosystem|Model — Ecosystem Architecture]]
- ENABLES: [[model-claude-code|Model — Claude Code]]
- BUILDS ON: [[llm-wiki-pattern|LLM Wiki Pattern]]
- BUILDS ON: [[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
- BUILDS ON: [[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[model-knowledge-evolution|Model — Knowledge Evolution]]

## Backlinks

[[model-second-brain|Model — Second Brain]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[model-claude-code|Model — Claude Code]]
[[llm-wiki-pattern|LLM Wiki Pattern]]
[[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
[[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
[[model-methodology|Model — Methodology]]
[[model-knowledge-evolution|Model — Knowledge Evolution]]
[[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]]
[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]]
[[global-standards-adherence|Global Standards Adherence — Engineering Principles the Wiki Follows]]
[[model-llm-wiki-standards|LLM Wiki Standards — What Good Looks Like]]
[[model-registry|Model Registry]]
[[model-wiki-design|Model — Wiki Design]]
[[models-are-systems-not-documents|Models Are Systems, Not Documents]]
[[new-content-must-integrate-into-existing-pages|New Content Must Integrate Into Existing Pages]]
[[wiki-post-ingestion-operations-plan|Operations Plan — Wiki Post-Ingestion Validation]]
[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
