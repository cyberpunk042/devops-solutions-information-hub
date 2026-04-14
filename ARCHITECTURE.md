# ARCHITECTURE.md — System Architecture, Data Flow, and Directory Topology

> This file describes HOW the DevOps Solutions Research Wiki is built — its directory structure,
> data pipeline, tool boundaries, and integration points.
> Audience: anyone modifying the project's structure or integrating with it.
> For identity and constraints, see [CONTEXT.md](CONTEXT.md).
> For operator-facing commands, see [TOOLS.md](TOOLS.md).

---

## 1. Directory Topology

```
devops-solutions-research-wiki/
│
├── raw/                        # L0: Unprocessed source material (kept permanently)
│   ├── articles/               # Fetched web articles (.md)
│   ├── transcripts/            # YouTube transcripts (.txt)
│   ├── papers/                 # PDFs, research papers
│   ├── notes/                  # Operator directives, session logs (raw/notes/YYYY-MM-DD-*.md)
│   └── dumps/                  # Pasted content that couldn't be auto-fetched
│
├── wiki/                       # L1–L7: Processed, structured knowledge
│   ├── spine/                  # Strategic architecture — models, standards, navigation
│   │   ├── models/             # 16 named models (foundation/, agent-config/, depth/, quality/, ecosystem/)
│   │   ├── standards/          # 22 per-type + per-model standards pages
│   │   ├── super-model/        # 5 sub-super-models + master super-model.md
│   │   ├── references/         # Model registry, system map, gateway reference, integration chain
│   │   ├── domain-overviews/   # High-level domain summary pages
│   │   ├── learning-paths/     # Guided reading sequences
│   │   ├── evolution-log/      # Wiki's own change history
│   │   └── goldilocks-flow.md  # Identity-to-action navigation entry point
│   │
│   ├── domains/                # Domain-specific concept and synthesis pages
│   │   ├── ai-agents/          # Agent patterns, harnesses, fleet orchestration
│   │   ├── ai-models/          # LLM architecture, capabilities, selection
│   │   ├── automation/         # Pipeline patterns, CI/CD, hooks
│   │   ├── devops/             # Infrastructure, operations, platform engineering
│   │   ├── knowledge-systems/  # PKM theory, second brain patterns, graph structures
│   │   ├── tools-and-platforms/# Claude Code, MCP, gateway tools
│   │   └── cross-domain/       # Methodology artifacts, integration specs, shared concepts
│   │
│   ├── sources/                # L1: Per-source synthesis pages
│   ├── comparisons/            # L3: Evaluated alternatives (A vs B, with recommendations)
│   ├── lessons/                # L4: Convergent evidence from ≥3 sources
│   │   ├── 00_inbox/           # Newly scaffolded, unreviewed
│   │   ├── 01_drafts/          # In progress
│   │   ├── 02_synthesized/     # Cross-referenced, internally consistent
│   │   ├── 03_validated/       # Evidence verified (40+ lessons here)
│   │   └── 04_principles/      # Promoted to governing truths (3 principles)
│   ├── patterns/               # L5: Recurring structural phenomena (≥2 instances)
│   │   └── [same 00–04 structure]
│   ├── decisions/              # L6: Binding choices with alternatives + rationale
│   │   └── [same 00–03 structure]
│   ├── ecosystem/              # Sister-project-facing export pages and profiles
│   ├── backlog/                # Work management
│   │   ├── milestones/         # Milestone definitions (e.g., v2.0)
│   │   ├── epics/              # Epic pages (milestone-v2/, older/)
│   │   └── tasks/              # Atomic task pages
│   ├── log/                    # Session logs, evolution logs
│   ├── config/                 # Wiki schema, methodology engine, profiles, templates
│   │   ├── README.md           # THOROUGH reference documenting every config
│   │   ├── wiki-schema.yaml    # Layer 0: frontmatter schema
│   │   ├── artifact-types.yaml # Layer 0: 78 artifact types with content thresholds
│   │   ├── domains.yaml        # Layer 0: domain registry
│   │   ├── quality-standards.yaml # Layer 0: quality thresholds
│   │   ├── export-profiles.yaml   # Layer 0: export configs (openfleet, aicp)
│   │   ├── methodology.yaml    # Layer 1: 9 methodology models + chains (DEFINITIONS)
│   │   ├── methodology-profiles/  # Layer 2: methodology STYLES (4 profiles)
│   │   │   ├── stage-gated.yaml   # Current default style
│   │   │   ├── spec-driven.yaml   # SDD/spec-kit-inspired
│   │   │   ├── agile-ai.yaml      # BMAD-inspired
│   │   │   └── test-driven.yaml   # TDD
│   │   ├── domain-profiles/    # Layer 3: concrete resolution (paths + gate commands)
│   │   │   ├── typescript.yaml
│   │   │   ├── python-wiki.yaml
│   │   │   ├── infrastructure.yaml
│   │   │   └── knowledge.yaml  # Pure knowledge projects (no code)
│   │   ├── sdlc-profiles/      # Layer 4: project POLICY (simplified/default/full)
│   │   └── templates/          # Per-type page templates (19 types)
│   │       └── methodology/    # Stage document templates (gap-analysis, tech-spec, etc.)
│   ├── manifest.json           # Machine-readable page catalog (auto-generated)
│   └── index.md                # Master wiki index (auto-generated)
│
├── tools/                      # Python utility suite (~9,800 lines total)
│   ├── pipeline.py             # Orchestrator — chains all tools (1,512 lines)
│   ├── gateway.py              # Unified CLI/programmatic/MCP interface (1,451 lines)
│   ├── evolve.py               # Maturity lifecycle engine (1,337 lines)
│   ├── lint.py                 # Health checks — orphans, thin pages, dead links (696 lines)
│   ├── view.py                 # Dashboard + navigation (618 lines)
│   ├── common.py               # Shared utilities (571 lines)
│   ├── mcp_server.py           # FastMCP server — 21 tools exposed (447 lines)
│   ├── sync.py                 # WSL↔Windows vault sync (442 lines)
│   ├── ingest.py               # Source fetching (YouTube, GitHub, web) (402 lines)
│   ├── validate.py             # Frontmatter schema validation (356 lines)
│   ├── obsidian.py             # Wikilink generation + backlinks (331 lines)
│   ├── watcher.py              # File watcher daemon (331 lines)
│   ├── integrations.py         # NotebookLM, status report integrations (312 lines)
│   ├── manifest.py             # Page catalog builder
│   ├── export.py               # Export to sister projects (openfleet/LightRAG, aicp)
│   ├── stats.py                # Coverage and growth reporting
│   └── setup.py                # Environment setup
│
├── skills/                     # Claude Code skill definitions (invokable sub-agents)
│   ├── wiki-agent/             # Full ingestion + query + maintenance
│   ├── evolve/                 # Score, scaffold, review, promote maturity
│   ├── continue/               # Resume mission: diagnostics → state → options
│   ├── model-builder/          # Build, review, or evolve a wiki model
│   └── notebooklm/             # NotebookLM sync operations
│
├── docs/                       # Project documentation and specs
├── scripts/                    # Utility shell scripts
├── services/                   # Service configuration templates
├── tests/                      # Test suite
├── .mcp.json                   # MCP server registration (21 tools auto-discovered)
├── README.md                   # Project overview and entry points
├── AGENTS.md                   # Universal cross-tool agent context
├── CLAUDE.md                   # Claude Code-specific methodology enforcement
├── CONTEXT.md                  # Identity, phase, constraints (this project's state)
└── ARCHITECTURE.md             # This file
```

---

## 2. Data Flow — Raw Sources to Validated Principles

```
                    INGESTION PIPELINE
                    ──────────────────

  URL / file / paste
        │
        ▼
  tools/ingest.py ──────────────────────────────────────────────────────┐
  (auto-classifies: YouTube → transcript extract                        │
                    GitHub → README + up to 30 key files               │
                    Web → main content extraction)                      │
        │                                                               │
        ▼                                                               │
  raw/articles/    raw/transcripts/    raw/notes/    raw/dumps/        │
  (L0 — kept permanently for provenance)                               │
        │                                                               │
        ▼                                                               │
  [Human + Claude read source in full]                                  │
  HARD RULE: wc -l first, offset reads for >200 lines                  │
  HARD RULE: README ≠ understanding — read a real INSTANCE             │
        │                                                               │
        ▼                                                               │
  wiki/sources/    (L1 — source-synthesis page per source)             │
  wiki/domains/*/  (L2 — concept pages: what a thing IS)               │
  wiki/comparisons/(L3 — A vs B evaluations with recommendations)       │
        │                                                               │
        └──────────────────────────────────────────────────────────────┘
                    VALIDATION CHAIN (tools/pipeline.py post)
                    ─────────────────────────────────────────

  Step 1: rebuild_all_indexes    — regenerate all domain _index.md
  Step 2: build_manifest         — rebuild wiki/manifest.json catalog
  Step 3: validate_all           — frontmatter schema, required sections, verbs
  Step 4: obsidian fix-rels      — resolve bare title refs → [[slug|title]] wikilinks
  Step 5: obsidian backlinks      — generate ## Backlinks sections for graph view
  Step 6: lint_wiki              — orphans, thin pages, dead relationships, stale pages

  Result: 0 errors required. Any error blocks completion.
```

```
                    EVOLUTION PIPELINE
                    ──────────────────

  wiki/sources/ + wiki/domains/ + wiki/comparisons/
        │
        ▼
  tools/evolve.py --score
  (6 scoring signals: cross-source convergence, relationship hub density,
   age since last update, mention count, type distribution, domain gaps)
        │
        ▼
  Candidates ranked by score
        │
        ▼
  tools/pipeline.py scaffold lesson/pattern/decision "<Title>"
  → creates wiki/lessons/00_inbox/<slug>.md
     wiki/patterns/00_inbox/<slug>.md
     wiki/decisions/00_inbox/<slug>.md
        │
        ▼
  [Claude fills content using cross-referenced sources]
        │
        ▼
  Maturity promotion (operator-gated at each step):
  00_inbox → 01_drafts → 02_synthesized → 03_validated → 04_principles

  Promotion criteria:
    00 → 01: Draft exists with summary and ≥1 evidence item
    01 → 02: Cross-referenced with related pages, relationships filled
    02 → 03: ≥3 independent evidence sources, Obsidian callouts present
    03 → 04: Operator confirms; ≥3 lessons supporting the principle

  99→100% on readiness OR progress: ALWAYS requires human review
```

```
  Knowledge Layer Summary:

  L0  raw/              Verbatim sources (never synthesized here)
  L1  sources/          Per-source synthesis (key insights, cross-refs, relationships)
  L2  domains/*/        Concept pages (what a thing IS — authoritative definitions)
  L3  comparisons/      Evaluated alternatives (A vs B, with concrete recommendations)
  L4  lessons/          Convergent evidence from ≥3 sources (maturity: inbox→validated)
  L5  patterns/         Recurring structural phenomena with ≥2 named instances
  L6  decisions/        Binding choices: alternatives considered + rationale documented
  L7  principles/       Governing truths derived from ≥3 validated lessons (04_principles)
```

---

## 3. Tool Topology

### Pipeline vs Gateway: Audience-Based Separation

Two tools, two audiences, two concerns. The division is deliberate.

| | **`tools/pipeline.py`** | **`tools/gateway.py`** |
|---|------------------------|-----------------------|
| **Primary audience** | Internal operator + automation (hooks, cron, watcher) | **External consumers** (other projects, MCP clients, agents) AND operator |
| **Concern** | WRITE operations — ingest, validate, maintain | READ interface + selected write-back (contribute, move) |
| **Mental model** | "The wiki's internal plumbing" | "The wiki's public API" |
| **Entry from outside** | Not typical | Canonical via `--wiki-root` or MCP |
| **Operates on** | This wiki only | This wiki OR any project's wiki (dual-scope) |

**Rule**: pipeline stuff in pipeline, gateway stuff in gateway. Don't blur the boundary.

### `tools/pipeline.py` — The Orchestrator (1,512 lines)

Chains write-side tools into automated pipelines. Supports three execution modes: `chain` (sequential), `group` (parallel with `ThreadPoolExecutor`), and `tree` (branch/merge). Named chains live in `wiki/config/`.

Key commands:
- `post` — 6-step validation chain (always run after wiki changes)
- `fetch` — delegates to `ingest.py` (YouTube/GitHub/web auto-detection)
- `scaffold` — creates typed pages from `wiki/config/templates/`
- `evolve` — delegates to `evolve.py` (score, scaffold, review)
- `gaps`, `crossref` — analysis pipelines
- `chain <name>` — runs a named pipeline chain (continue, review, health, evolve, full)
- `status` — pipeline's own plumbing state: raw files inventory + wiki page count

Deprecated (use gateway):
- `backlog` — knowledge query, not pipeline state. Use `gateway query --backlog`.

### `tools/gateway.py` — Unified Knowledge Interface (1,638 lines)

Dual-scope knowledge interface. Operates on the local second brain OR a target project's wiki via `--wiki-root`. Used by external consumers (MCP clients, sister-project agents) AND the operator.

Auto-detects project identity from filesystem signals (domain markers, scale proxy, execution mode signals). Identity detection distinguishes solo mode from harness v1/v2/v3/fleet — having `.claude/settings.json` does NOT make it a harness.

Key commands:
- `status` — project dashboard (identity + SDLC profile + models + navigation)
- `query` — unified query (identity, models, chains, profiles, stages, fields, backlog, lessons, logs, pages, docs)
- `flow` — Goldilocks 8-step routing
- `template` — get a template for scaffolding
- `move`, `archive`, `backup`, `factory-reset` — knowledge operations
- `contribute` — agent write-back (lesson, remark, correction)
- `what-do-i-need` — auto-detect + recommend SDLC profile

### Why both `status` commands exist

They serve different audiences:

| Audience | Question | Command |
|----------|----------|---------|
| Pipeline operator | "What's in my inbox? How many pages processed?" | `pipeline status` |
| Anyone (external or operator) | "Who is this project? What profile? Which models?" | `gateway status` |

Same verb, different concern. Not duplicates.

Key command groups:
- `query` — methodology, models, stages, chains, fields, identity
- `flow` — step-by-step Goldilocks flow navigation
- `template` — return page templates
- `config` — render config sections as markdown
- `move`, `archive` — structural operations with ref updates
- `backup` — full wiki snapshot
- `contribute` — agent write-back (creates `lessons/00_inbox/` entries)

### `tools/evolve.py` — Maturity Lifecycle Engine (1,337 lines)

Scores pages across 6 signals to identify evolution candidates. Generates scaffold prompts for lesson/pattern/decision promotion. Supports `--auto` mode (LLM-delegated generation), `--review` (maturity assessment), and `--stale` (age detection).

### `tools/ingest.py` — Source Fetching (402 lines)

Auto-classifies URLs:
- **YouTube** → `yt-dlp` transcript extraction → `raw/transcripts/<slug>.txt`
- **GitHub repos** → README + up to 30 key files via GitHub API → `raw/articles/<slug>.md`
- **GitHub gists** → gist content
- **Web pages** → main content extraction → `raw/articles/<slug>.md`

Deep GitHub fetch: pulls README + key docs (ARCHITECTURE, CLAUDE, AGENTS, DESIGN, TOOLS, etc.) at up to 5,000+ line depth. Used to ingest OpenSpec, spec-kit, BMAD-METHOD.

### `tools/obsidian.py` — Wikilink Bridge (331 lines)

Bridges the `## Relationships` section format (plain text `VERB: Title`) to Obsidian `[[slug|title]]` wikilinks. Two operations:

1. **fix-relationships** (Step 4 of `post`): resolves bare title references → `[[slug|title]]` using manifest lookup
2. **backlinks** (Step 5 of `post`): generates `## Backlinks` sections so graph view shows incoming links

### `tools/validate.py` — Schema Validation (356 lines)

Validates YAML frontmatter against `wiki/config/wiki-schema.yaml`. Checks: required fields, field enums, required sections per page type, relationship verb format. Exit code 1 = errors found.

### `tools/lint.py` — Health Checks (696 lines)

Checks: dead relationships (target page doesn't exist), orphan pages (not reachable from any `_index.md`), thin pages (below content thresholds), stale pages (not updated in N days), domain health. Supports `--fix` for auto-remediation where possible.

### `tools/mcp_server.py` — MCP Tool Exposure (447 lines)

FastMCP server exposing 21 wiki operations as native Claude Code tools. Auto-discovered via `.mcp.json`. Covers: status, search, read, list, post, fetch, gaps, crossref, sync, evolve, backlog, log, gateway query/template/contribute/flow.

Any Claude Code conversation in this project can use MCP tool calls instead of CLI commands.

### `tools/sync.py` — WSL↔Windows Sync (442 lines)

Keeps `wiki/` directory in sync between WSL (where tools run) and Windows (where Obsidian opens the vault). Supports one-shot sync and `--watch` daemon mode. Auto-detects Windows username for default target path. Configurable via `WIKI_SYNC_TARGET` env var.

### `tools/manifest.py` — Page Catalog

Builds `wiki/manifest.json` — machine-readable catalog of all pages with title, slug, type, domain, status, confidence, relationships. Used by `obsidian.py` for slug lookup and by `gateway.py` for identity queries.

### `tools/export.py` — Sister Project Export

Config-driven via `wiki/config/export-profiles.yaml`. Profiles:
- **openfleet**: exports for LightRAG ingestion (knowledge graph source)
- **aicp**: exports for LocalAI Collections (local inference patterns)
- **methodology**: exports methodology artifacts for devops-control-plane

Transform pipeline: filter by confidence/status → map types → inject metadata → resolve sections.

### `tools/view.py` — Dashboard + Navigation (618 lines)

Human-readable wiki exploration:
- `view` — dashboard (page counts, types, domains, maturity distribution)
- `view tree` — full wiki structure as navigable tree
- `view model <name>` — model detail with standards, member pages, lessons
- `view search <query>` — fuzzy search across all pages
- `view refs <title>` — outbound + inbound relationships for a page

---

## 4. Wiki Page Schema Architecture

### Frontmatter as Programmatic Interface

Every wiki page uses YAML frontmatter. The frontmatter is the programmatic interface — `validate.py` enforces it, `manifest.py` indexes it, `evolve.py` scores it, `gateway.py` queries it, `export.py` filters on it.

**Required fields (all pages):**
```yaml
title:      # Must match the # Heading exactly
type:       # One of 19 valid types (see below)
domain:     # Must match the folder path
status:     # raw | processing | synthesized | verified | draft | active | done | ...
confidence: # low | medium | high | authoritative
created:    # YYYY-MM-DD
updated:    # YYYY-MM-DD
sources:    # list of {id, type, url/file} — provenance is mandatory
tags:       # list of strings
```

**Optional fields (type-specific):**
```yaml
maturity:         # for lessons/patterns/decisions
readiness:        # 0-100: definition completeness (work management pages)
progress:         # 0-100: execution completeness (independent from readiness)
current_stage:    # document | design | scaffold | implement | test
stages_completed: # list
priority:         # P0 | P1 | P2 | P3
depends_on:       # list of epic/task IDs
blocked_by:       # impediment page title
```

### Type System (19 Types)

| Type | Layer | Primary Use |
|------|-------|------------|
| `source-synthesis` | L1 | Per-source deep read with insights and cross-refs |
| `concept` | L2 | Authoritative definition of a domain concept |
| `comparison` | L3 | A vs B evaluation with concrete recommendation |
| `lesson` | L4 | Convergent evidence from ≥3 sources |
| `pattern` | L5 | Recurring structural phenomenon with ≥2 instances |
| `decision` | L6 | Binding choice with alternatives + rationale |
| `principle` | L7 | Governing truth derived from ≥3 lessons |
| `reference` | spine | Navigation, registry, index pages |
| `deep-dive` | spine | Extended analysis of a single topic |
| `domain-overview` | domains | High-level domain summary |
| `learning-path` | spine | Guided reading sequence |
| `evolution` | spine | Wiki's own change history entry |
| `note` | misc | Raw notes, session logs |
| `epic` | backlog | Strategic work package |
| `module` | backlog | Coherent subsystem scope |
| `task` | backlog | Atomic work item |
| `milestone` | backlog | Multi-epic delivery target |
| `operations-plan` | ops | Operational runbook |
| `index` | auto | Auto-generated domain index |

### Maturity Folder Structure

Evolved knowledge types use maturity-based folder promotion:

```
wiki/lessons/
    00_inbox/       # Freshly scaffolded — not yet reviewed
    01_drafts/      # Being written — content incomplete
    02_synthesized/ # Cross-referenced — internally consistent
    03_validated/   # Evidence verified (≥3 sources) — 40+ lessons here
    04_principles/  # Operator-promoted governing truths — 3 principles here

wiki/patterns/      # Same 00–04 structure
wiki/decisions/     # 00–03 structure (no 04_principles folder)
```

Rule: >10 items in a folder = add sub-structure.

### Relationship Graph

Relationships are declared in a `## Relationships` section using ALL_CAPS verbs, one per line. The obsidian.py tool converts these to `[[slug|title]]` wikilinks for Obsidian's graph view.

```markdown
## Relationships
- BUILDS ON: [[model-methodology|Model — Methodology]]
- ENABLES: [[model-context-engineering|Model — Context Engineering]]
- COMPARES TO: [[src-openspec|Synthesis: OpenSpec]]
- DERIVED FROM: [[lesson-infrastructure-over-instructions|Infrastructure Over Instructions]]
```

Valid verbs: `BUILDS ON, ENABLES, COMPARES TO, CONTRADICTS, USED BY, RELATES TO, FEEDS INTO, DERIVED FROM, SUPERSEDES, IMPLEMENTS, EXTENDS, CONTAINS, PART OF`

The relationship graph has 2074+ edges across 316 nodes — dense enough to serve as a LightRAG knowledge source.

---

## 5. Integration Points

### Dual-Scope Gateway

`gateway.py` has two modes of operation controlled by scope flags:

```bash
# Operate on this second brain (default)
python3 -m tools.gateway query --models

# Operate on another project's wiki
python3 -m tools.gateway --wiki-root /path/to/openarms query --models

# Operate on this second brain explicitly
python3 -m tools.gateway --brain query --identity
```

This means the same gateway binary serves both the wiki and all sister projects without configuration changes.

### MCP Server (21 Tools)

Registered in `.mcp.json` (stdio transport). Auto-discovered by Claude Code. Any agent in any project can call wiki operations as native tool calls.

Tool categories: status, search, read, list, post, fetch, gaps, crossref, sync, mirror, evolve, backlog, log, gateway_query, gateway_template, gateway_contribute, gateway_flow, integrations, continue, scan_project, fetch_topic.

Start manually: `python -m tools.mcp_server`

### Export Profiles (Sister Projects)

```bash
python3 -m tools.export openfleet   # → LightRAG knowledge source (OpenFleet)
python3 -m tools.export aicp        # → LocalAI Collections (AICP)
python3 -m tools.export methodology # → decision tracking (devops-control-plane)
```

Export filtering: confidence ≥ `high`, status ≥ `synthesized`, transforms type labels, injects project metadata. Defined in `wiki/config/export-profiles.yaml`.

### Bidirectional Sync (WSL ↔ Obsidian)

```bash
python3 -m tools.sync           # One-shot sync to Windows vault
python3 -m tools.sync --watch   # Daemon mode (auto-sync on change)
python3 -m tools.sync --reverse # Sync Windows edits back to WSL
```

Default target: `C:\Users\<WIN_USER>\Documents\obsidian-vault\` (auto-detected from `WIN_USER` env var or Windows username detection).

### Gateway Contribute (Agent Write-Back)

Any agent (from any sister project) can write learned lessons back to the wiki:

```bash
python3 -m tools.gateway contribute \
  --type lesson \
  --title "Learned: Hook Retry Behavior Under Load" \
  --content "..."
```

Creates `wiki/lessons/00_inbox/<slug>.md` — enters the maturity pipeline. The source is permanently recorded in `raw/notes/` for provenance.

---

## 6. Methodology Engine

### Core Config Files

| File | Purpose |
|------|---------|
| `wiki/config/methodology.yaml` | 9 methodology models (feature-development, bug-fix, research, docs, refactor, hotfix, integration, knowledge-evolution) + stage definitions + artifact chains |
| `wiki/config/artifact-types.yaml` | 78 artifact types across 11 categories with content thresholds, required sections, and per-type quality standards |
| `wiki/config/sdlc-profiles/simplified.yaml` | Simplified SDLC profile (POC, micro-scale, low trust) |
| `wiki/config/sdlc-profiles/default.yaml` | Default SDLC profile (production, medium scale, operator-supervised) — THIS PROJECT |
| `wiki/config/sdlc-profiles/full.yaml` | Full SDLC profile (fleet, large scale, high stakes) |
| `wiki/config/wiki-schema.yaml` | Page frontmatter schema (required fields, enums, constraints) |
| `wiki/config/quality-standards.yaml` | Minimum content thresholds by page type |

### Artifact Classes

The methodology distinguishes three distinct artifact classes (NOT interchangeable):

| Class | Role | Examples |
|-------|------|---------|
| **DOCUMENT** | Constraining — defines what must be built | Requirements spec, gap analysis, tech spec |
| **ARTIFACT** | By-product — created as part of doing the work | Source synthesis, concept page, lesson |
| **DOCUMENTATION** | Explaining — describes what was built | README, AGENTS.md, this file |

78 artifact types across 11 categories: `wiki/domains/cross-domain/methodology-artifacts/categories/methodology-artifact-taxonomy.md`

### Domain Artifact Chains

Each domain has a specific chain of artifacts per stage. Check the right chain before producing anything:

- **TypeScript**: `wiki/domains/cross-domain/methodology-artifacts/chains/domain-chain-typescript.md`
- **Python/Wiki**: `wiki/domains/cross-domain/methodology-artifacts/chains/domain-chain-python-wiki.md`
- **Infrastructure**: `wiki/domains/cross-domain/methodology-artifacts/chains/domain-chain-infrastructure.md`
- **Knowledge**: `wiki/domains/cross-domain/methodology-artifacts/chains/domain-chain-knowledge.md`

---

## 7. Stage Gate Enforcement Flow

```
  Operator gives instruction
          │
          ▼
  What stage is this work in?
  (check current_stage in epic/task frontmatter, or ask)
          │
          ▼
  ┌───────────────────────────────────────────────────────────────────┐
  │  DOCUMENT (readiness 0→25%)                                       │
  │  ALLOWED: wiki pages, raw/notes/ logs, research                   │
  │  FORBIDDEN: implementation code, tool modifications               │
  └───────────────────────┬───────────────────────────────────────────┘
                          │ readiness ≥ 25% AND previous artifacts exist
                          ▼
  ┌───────────────────────────────────────────────────────────────────┐
  │  DESIGN (readiness 25→50%)                                        │
  │  ALLOWED: design docs, decision pages, specs                      │
  │  FORBIDDEN: implementation code, tool modifications               │
  └───────────────────────┬───────────────────────────────────────────┘
                          │ readiness ≥ 50% AND previous artifacts exist
                          ▼
  ┌───────────────────────────────────────────────────────────────────┐
  │  SCAFFOLD (readiness 50→80%)                                      │
  │  ALLOWED: templates, config files, schema changes, empty stubs    │
  │  FORBIDDEN: business logic, real implementations                  │
  └───────────────────────┬───────────────────────────────────────────┘
                          │ readiness ≥ 80% AND previous artifacts exist
                          ▼
  ┌───────────────────────────────────────────────────────────────────┐
  │  IMPLEMENT (readiness 80→95%)                                     │
  │  ALLOWED: code, config, wiki pages, tool changes                  │
  │  FORBIDDEN: test modifications                                    │
  └───────────────────────┬───────────────────────────────────────────┘
                          │ readiness ≥ 95% AND previous artifacts exist
                          ▼
  ┌───────────────────────────────────────────────────────────────────┐
  │  TEST (readiness 95→100%)                                         │
  │  ALLOWED: test implementations, validation runs                   │
  │  FORBIDDEN: new features, scope changes                           │
  └───────────────────────┬───────────────────────────────────────────┘
                          │ readiness = 100% AND progress = 100%
                          │ REQUIRES: human review at 99→100 on EITHER dimension
                          ▼
                       DONE ✓
```

### Readiness vs Progress (Two Independent Dimensions)

```
  readiness (0–100): "Is this READY to work on?"
  — Measures definition completeness
  — "Do we know enough to start this stage?"
  — Can be 100% while progress is 0% (fully defined, not started)

  progress (0–100): "How far is the WORK done?"
  — Measures execution completeness
  — "How much of the actual work is finished?"
  — Can be 75% while readiness is 50% (partially done but poorly defined)

  Both must reach 100% for completion.
  99→100 on EITHER dimension requires explicit human review.
```

### Post-Chain as the Enforcement Gate

Every wiki change must pass `pipeline post` before committing:

```bash
python3 -m tools.pipeline post
```

This runs all 6 validation steps. The command exits with code 1 if any step finds errors. "Done" means showing this output with 0 errors — not claiming it.

---

## 8. Key Architectural Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Markdown + YAML frontmatter | vs database | Git-native, Obsidian-compatible, LLM-readable, no schema migrations |
| Single wiki/ directory | vs per-domain repos | Relationships cross domains; centralized manifest enables graph analysis |
| `pipeline post` as commit gate | vs optional validation | 100% compliance requires enforcement; advisory validation achieves ~25% |
| Dual-scope gateway | vs separate tools | Same interface for second brain and all sister projects — DRY |
| Maturity folder structure | vs status field only | Physical location = discoverable maturity; folder > frontmatter for browsing |
| Permanent raw/ retention | vs delete after synthesis | Provenance is non-negotiable; re-reading sources is common |
| Verbatim directive logging | vs paraphrase | Exact wording matters for intent; paraphrasing loses precision |

Decision pages: `wiki/decisions/`

---

*Last updated: 2026-04-14. Tool line counts from `wc -l tools/*.py`. Page counts from `python3 -m tools.pipeline status`.*
