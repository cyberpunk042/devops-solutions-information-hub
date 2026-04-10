---
title: "Model: LLM Wiki"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: authoritative
maturity: growing
created: 2026-04-09
updated: 2026-04-10
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

The LLM Wiki model defines a knowledge system where an LLM agent maintains a structured markdown wiki — ingesting sources, synthesizing pages, cross-referencing relationships, evolving insights through density layers, and linting for quality. The model solves the wiki maintenance problem: wikis historically die because humans abandon upkeep. With an LLM handling all mechanical operations, the wiki compounds knowledge instead of decaying. This model is technology-agnostic — it defines structure and rules, not tools.

This is one of 14+ named models that a wiki can contain. The [[Methodology Framework]] is the super-model that governs HOW work is done. This page defines WHAT the wiki IS. See [[Model: Methodology]] for the work process.

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

## Deep Analysis

### Core Architecture

An LLM Wiki has three layers:

1. **Raw layer** — unprocessed source material. Never modified after ingestion. Permanent provenance.
2. **Wiki layer** — structured markdown pages with YAML frontmatter, typed relationships, quality gates. Also contains the backlog (project management) and log (operator directives).
3. **Meta layer** — schema, templates, validation rules. Defines how the wiki works.

The distinction between `config/` (meta layer — schema, templates) and `wiki/config/` (wiki layer — methodology, agent directive) is intentional:
- `config/wiki-schema.yaml` and `config/templates/` define the wiki's STRUCTURE — page types, fields, validation rules. These rarely change.
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

Knowledge layers (L0-L6) implement [[Progressive Distillation]]: raw → synthesis → concept → lesson → pattern → decision.

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
| `task_type` | Backlog | Determines required stages. See [[Stage-Gate Methodology]]. |
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

- BUILDS ON: [[Page Title]]
- ENABLES: [[Another Page]]
- CONTRADICTS: [[Some Assumption]]
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

Format: `- VERB: [[Target]]` — one per line. Regex: `^([A-Z][A-Z /\-]+?):\s*(.+)$`

### Page Templates

Templates in `config/templates/` use `{{placeholder}}` variables for scaffolding. Six templates exist:

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

### Scale Boundary

> [!warning] ~200 pages is the index-navigation ceiling
> Below ~200: index-driven navigation is cheaper and more accurate than vector search. Above ~200: add graph-enhanced retrieval (LightRAG) as an ADDITIVE layer — the wiki stays the same, the retrieval layer indexes it. See [[Decision: Wiki-First with LightRAG Upgrade Path]].

### How to Adopt

1. **Create the repository structure** — raw/, wiki/ (with all subdirectories), config/. The structure above is the reference.
2. **Define your schema** — copy `config/wiki-schema.yaml`. For a code project: add types like `api-spec` or `architecture`, remove types you won't use. For a research wiki: the default types work well. For a small project: start with `concept`, `source-synthesis`, `lesson`, `decision` — add more as the wiki grows.
3. **Create page templates** — at minimum: lesson, pattern, decision. Templates define section structure + placeholder variables. Copy from `config/templates/`.
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
| [[Decision: Wiki-First with LightRAG Upgrade Path]] | The scale decision |
| [[Second Brain Architecture]] | PKM theory (PARA, Zettelkasten) mapped to this model |
| [[Wiki Backlog Pattern]] | How the wiki tracks its own work |

### Quality Standards

See [[LLM Wiki Standards — What Good Looks Like]] for the gold-standard example of each page type, what makes each one good, and the anti-patterns to avoid. The standards page is the companion to this model — the model defines structure, the standards define quality.

### Lessons Learned

From building with this model — validated experience:

| Lesson | What was learned |
|--------|-----------------|
| [[LLM-Maintained Wikis Outperform Static Documentation]] | Maintenance economics is the differentiator |
| [[Lesson: Schema Is the Real Product — Not the Content]] | Schema survives; content is regenerable |
| [[Multi-Stage Ingestion Beats Single-Pass Processing]] | Each pass discovers what the previous missed |
| [[Never Synthesize from Descriptions Alone]] | Read the THING, not the description (Layer 0 → Layer 1) |
| [[Shallow Ingestion Is Systemic, Not Isolated]] | One defect = audit ALL similar artifacts |
| [[Automated Knowledge Validation Prevents Silent Wiki Decay]] | Without linting, wikis decay silently |

## Open Questions

> [!question] What is the minimum viable wiki? Can a project start with just raw/ + wiki/domains/ + config/wiki-schema.yaml and add the other layers later? What's the smallest structure that demonstrates value? (Requires: empirical testing with a fresh project)
- How do multiple agents co-author a wiki without conflicts? The current model assumes one agent + one operator. With OpenFleet's 10-agent architecture, merge conflicts on frontmatter, competing relationship claims, and simultaneous page creation need resolution. (Requires: multi-agent testing)
- Optimal starting schema complexity? A new adopter could start with 5 types (concept, source-synthesis, lesson, decision, note) and grow to 16 — or start comprehensive. Which leads to better adoption? (Requires: 2+ adoption experiences)
- Can the LLM Wiki coexist with Confluence/Notion in an organization? Possible boundary: LLM Wiki for AI-maintained synthesized knowledge, Confluence for human-authored team docs. The wiki ingests FROM Confluence but doesn't replace it. (Requires: enterprise context testing)

## Relationships

- FEEDS INTO: [[Model: Second Brain]]
- FEEDS INTO: [[Model: Ecosystem Architecture]]
- ENABLES: [[Model: Claude Code]]
- BUILDS ON: [[LLM Wiki Pattern]]
- BUILDS ON: [[Wiki Ingestion Pipeline]]
- BUILDS ON: [[Knowledge Evolution Pipeline]]
- RELATES TO: [[Model: Methodology]]
- RELATES TO: [[Model: Knowledge Evolution]]

## Backlinks

[[Model: Second Brain]]
[[Model: Ecosystem Architecture]]
[[Model: Claude Code]]
[[LLM Wiki Pattern]]
[[Wiki Ingestion Pipeline]]
[[Knowledge Evolution Pipeline]]
[[Model: Methodology]]
[[Model: Knowledge Evolution]]
[[LLM Wiki Standards — What Good Looks Like]]
[[Model Registry]]
[[Model: Wiki Design]]
[[Models Are Systems, Not Documents]]
