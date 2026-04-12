# DevOps Solutions Research Wiki

A research-grade knowledge synthesis system and second brain. Central intelligence
spine for the devops ecosystem (openfleet, AICP, DSPD, devops-control-plane).

# ---------------------------------------------------------------------------
# SACROSANCT OPERATOR DIRECTIVES
# These override everything. Never paraphrase. Never reinterpret.
# ---------------------------------------------------------------------------

> "not only not dumb raw dump but smart content and then to the full requirements / standards"
> "we need to establish a strong method of work with the Wiki LLM structure and Methodology"
> "we need to establish standards for everything with example of document on top of the standards documents for each artifact type"
> "the AI keep ignoring in certain cases even completely the directives given from the methodology"
> "Its important how we configure the claude file to use the second brain when its present"
> "fix it at the root instead.. its not hard" — solve problems with tooling, not manual work
> "we need ourself to make clear first all those high standards and examples"

# ---------------------------------------------------------------------------
# METHODOLOGY — HARD RULES (enforced, non-negotiable)
# ---------------------------------------------------------------------------

## Stage Gates — You MUST progress in order

| Stage | Readiness | ALLOWED | FORBIDDEN |
|-------|-----------|---------|-----------|
| DOCUMENT | 0→25% | Wiki pages, raw/notes/ logs, research | Implementation code, tool modifications |
| DESIGN | 25→50% | Design docs, decision pages, specs | Implementation code, tool modifications |
| SCAFFOLD | 50→80% | Templates, config files, schema changes, empty stubs | Business logic, real implementations |
| IMPLEMENT | 80→95% | Code, config, wiki pages, tool changes | Test modifications |
| TEST | 95→100% | Test implementations, validation runs | New features, scope changes |

"Continue" means advance within the CURRENT stage. NOT skip to the next stage.
"Get started" means start the CURRENT stage. NOT skip to the end.

## Hard Rules (MANDATORY — numbered, sequential, no exceptions)

1. NEVER skip stages. Document before design. Design before scaffold. Scaffold before implement.
2. NEVER write code during document/design. Understanding first, then building.
3. ALWAYS log directives verbatim in raw/notes/ BEFORE acting. Core methodology. Proactive, not reactive.
4. ALWAYS read full files before synthesizing. `wc -l` first. Offset reads for >200 lines. Page ≥0.25× source length.
5. ALWAYS verify depth. Source DESCRIBES a thing → you MUST read a real INSTANCE. README ≠ understanding.
6. ALWAYS run `pipeline post` after wiki changes. 6-step chain validates everything. Errors block completion.
7. NEVER claim done without evidence. Run the command. Show the output. 0 errors = done.

## Soft Rules (require judgment)

| Rule | Guidance |
|------|---------|
| Research before brainstorming | Check existing wiki pages, ecosystem projects, online sources FIRST |
| Update instead of create | If >70% overlap with existing page, update that page |
| Brainstorm before spec | Brainstorm = questions → approaches → design sections → approval on EACH |
| Solve with tooling not manual work | Blockers must be fixed with tools, not handed back to the operator |

# ---------------------------------------------------------------------------
# METHODOLOGY MODELS — select the right one for the task
# ---------------------------------------------------------------------------

| Task Type | Model | Stages | When |
|-----------|-------|--------|------|
| epic/module/task | feature-development | document → design → scaffold → implement → test | Complex work, solution unknown |
| bug | bug-fix | document → implement → test | Fix broken behavior |
| research/spike | research | document → design | Investigation, no code |
| docs | documentation | document | Single wiki page |
| refactor | refactor | document → scaffold → implement → test | Restructure, same behavior |
| hotfix | hotfix | implement → test | Emergency, solution known |
| integration | integration | scaffold → implement → test | Wire existing modules |
| evolve | knowledge-evolution | document → implement | Distill lessons/patterns/decisions |

Full model definitions with artifact chains: `config/methodology.yaml`
Artifact type details: `config/artifact-types.yaml`

## Per-Scale Artifact Requirements

| Scale | Required Artifacts |
|-------|-------------------|
| Epic | Directive log → research → infrastructure analysis → gap analysis → requirements spec → design → plan → per-module breakdown |
| Module | Design (or section of epic design) → plan → per-task breakdown |
| Task | Task description (from plan) → implement → verify |
| Hotfix | Nothing — fix, test, commit |

Templates for ALL artifacts: `config/templates/` (wiki types) and `config/templates/methodology/` (stage documents)

# ---------------------------------------------------------------------------
# WHAT THIS IS — project structure and schema
# ---------------------------------------------------------------------------

## Project Structure

- `raw/` — Unprocessed source material (transcripts, articles, papers, notes, dumps)
- `wiki/` — Processed knowledge (domains/, sources/, comparisons/, lessons/, patterns/, decisions/, spine/, backlog/, log/, config/, index.md, manifest.json)
- `tools/` — Python utilities (lint, manifest, export, validate, stats)
- `skills/` — Claude skill definitions
- `config/` — Schema, domain registry, export profiles, quality standards, methodology engine, artifact types, domain profiles, templates
- `docs/` — Project documentation and specs

**Start here:** `wiki/spine/model-registry.md` — lists all 15 named models with their
companion standards pages. Models are the primary knowledge containers.

## Page Schema

Every wiki page uses YAML frontmatter with these required fields:

    title, type, domain, status, confidence, created, updated, sources, tags

Page types: concept, source-synthesis, comparison, reference, deep-dive, index,
  lesson, pattern, decision, domain-overview, learning-path, evolution,
  operations-plan, epic, module, task, note

Every type has a template in `config/templates/`. Scaffold via:
`python3 -m tools.pipeline scaffold <type> <title>`

## Page Structure

Every page follows this section order:

    # Title
    ## Summary          ← 2-3 sentences min, used for LightRAG description
    ## Key Insights     ← condensed resolution boundary
    ## Deep Analysis    ← full resolution (concept, comparison, deep-dive types)
    ## Open Questions   ← gaps to fill (optional but encouraged)
    ## Relationships    ← VERB: target format, one per line

Evolved page types (lesson, pattern, decision) have additional required sections.
See `config/templates/` for section structure per type.

## Relationship Conventions

Use ALL_CAPS verbs. One relationship per line. Comma-separated targets allowed.

    BUILDS ON, ENABLES, COMPARES TO, CONTRADICTS, USED BY,
    RELATES TO, FEEDS INTO, DERIVED FROM, SUPERSEDES, IMPLEMENTS, EXTENDS

Format: `- VERB: Target Name (optional context)`

# ---------------------------------------------------------------------------
# QUALITY GATES — every page, every time
# ---------------------------------------------------------------------------

- Complete frontmatter with valid values per `config/wiki-schema.yaml`
- Summary ≥30 words
- ≥1 relationship (unless first in new domain)
- Reachable from domain _index.md
- Source provenance (URL or file reference)
- No >70% concept overlap with existing pages
- title field matches # Heading, domain field matches folder path
- Per-type content thresholds defined in `config/artifact-types.yaml`
- Evolved pages (lesson, pattern, decision) require Obsidian callouts
- Every stage transition: previous stage's artifacts exist

Validation: `python3 -m tools.pipeline post` (runs all 6 steps)

# ---------------------------------------------------------------------------
# TOOLING — commands and skills
# ---------------------------------------------------------------------------

## Pipeline (primary entry point)

- `python3 -m tools.pipeline post` — Full post-ingestion chain (index → manifest → validate → obsidian → lint)
- `python3 -m tools.pipeline fetch URL [URL...]` — Fetch URLs into raw/
- `python3 -m tools.pipeline fetch --batch file.txt` — Batch fetch from URL list
- `python3 -m tools.pipeline fetch --topic "query"` — Queue a research topic
- `python3 -m tools.pipeline scan ../project/` — Scan local project, copy key docs to raw/
- `python3 -m tools.pipeline status` — Show raw files and wiki stats
- `python3 -m tools.pipeline run URL [URL...]` — Parallel fetch + post-chain
- `python3 -m tools.pipeline gaps` — Gap analysis (orphans, thin pages, weak domains)
- `python3 -m tools.pipeline crossref` — Cross-reference analysis
- `python3 -m tools.pipeline scaffold <type> <title>` — Create page from template
- `python3 -m tools.pipeline scaffold methodology/<template> <title>` — Methodology document template
- `python3 -m tools.pipeline evolve --score` — Rank evolution candidates
- `python3 -m tools.pipeline evolve --review` — Review seed page maturity
- `python3 -m tools.pipeline backlog` — Show backlog summary
- `python3 -m tools.pipeline chain <name>` — Run named chain (continue, review, health, evolve, full)
- `python3 -m tools.pipeline chain --list` — List available chains

## Skills

- `wiki-agent` — Ingest sources, query knowledge, maintain quality, export
- `evolve` — Score, scaffold, generate, review maturity, detect staleness
- `continue` — Resume mission: diagnostics → state → options
- `model-builder` — Build, review, or evolve a wiki model

## MCP Server

17 tools registered in `.mcp.json` — auto-discovered by Claude Code.
Manual start: `.venv/bin/python -m tools.mcp_server`

## View Tool

- `python3 -m tools.view` — Dashboard overview (pages, types, domains, maturity)
- `python3 -m tools.view tree` — Full wiki structure as navigable tree
- `python3 -m tools.view model <name>` — Model detail with standards, pages, lessons
- `python3 -m tools.view search <query>` — Fuzzy search across all pages
- `python3 -m tools.view refs <title>` — Outbound + inbound relationships

## Other Tools

- `python3 -m tools.validate` — Schema validation
- `python3 -m tools.lint [--report|--summary|--fix]` — Health checks
- `python3 -m tools.export [openfleet|aicp|methodology]` — Export for sister projects
- `python3 -m tools.stats [--json]` — Coverage & growth reporting
- `python3 -m tools.sync [--watch]` — WSL ↔ Windows sync for Obsidian

## Setup

    python -m tools.setup              # Full setup
    python -m tools.setup --check      # Check environment
    python -m tools.setup --deps       # Install dependencies via uv

# ---------------------------------------------------------------------------
# INGESTION — how to process sources
# ---------------------------------------------------------------------------

Three modes, user specifies or defaults to smart:

- `auto` — Process without stopping. Report summary after.
- `guided` — Show extraction plan. Wait for approval. Review each page.
- `smart` (default) — Auto when confident. Escalate when: new domain,
  contradictions, ambiguity, expert-level complexity, low-quality source.

Accept: files in raw/, URLs (fetch → raw/), pasted content (save → raw/dumps/).

## Conventions

- kebab-case filenames, ASCII-only
- One concept per page
- Update existing pages rather than creating duplicates
- Domains grow organically
- _index.md in every domain folder, auto-maintained
- manifest.json regenerated after every wiki change
- raw/ files kept permanently for provenance
