# Research Wiki — System Design Specification

**Date:** 2026-04-08
**Status:** Draft
**Author:** jfortin + Claude Code

---

## 1. Overview

### 1.1 What This Is

A research-grade knowledge synthesis system and second brain. It ingests sources of any type (articles, transcripts, papers, notes, URLs, pastes), breaks them down into structured interlinked wiki pages, and serves as the central intelligence spine for the devops ecosystem.

### 1.2 What This Is NOT

- Not a content creation pipeline (no slides, podcasts, videos)
- Not a RAG system (though it's designed to feed them)
- Not a NotebookLM wrapper
- Not a simplified Karpathy clone

### 1.3 Goals

- High-quality synthesis and breakdown of online sources
- Deep understanding expressed as interlinked, multi-resolution wiki pages
- Long-term second brain that compounds knowledge over time
- Hub for research and documentation across all domains
- RAG-ready structure for downstream consumption by sister projects
- Massive scale — designed to grow to hundreds then thousands of pages

### 1.4 Sister Projects (Consumers)

| Project | Path | What It Needs | Integration |
|---------|------|---------------|-------------|
| openfleet | `../openfleet` | LightRAG-compatible KB entries with `## Relationships` | Export with frontmatter transform (YAML → markdown headers) |
| AICP (devops-expert-local-ai) | `../devops-expert-local-ai` | `docs/kb/` entries for LocalAI Collections | Export with type/status mapping |
| DSPD (devops-solution-product-dev) | `../devops-solution-product-development` | Future | TBD |
| devops-control-plane | `../devops-control-plane` | Future | TBD |

### 1.5 Compatibility Constraints

- **openfleet `kb_sync.py`**: Relationship lines must match regex `^([A-Z][A-Z /\-]+?):\s*(.+)$`. Verb in ALL_CAPS, comma-separated targets, parenthetical context allowed.
- **openfleet TYPE_MAP**: Exported pages need a recognized `**Type:**` markdown header. Research wiki pages export as `Research` or `Research Synthesis` type.
- **openfleet entity normalization**: Names uppercased, `/` → `::`, `.` → `:` during sync. Our page titles should avoid these characters.
- **AICP `docs/kb/` convention**: Markdown headers (not YAML frontmatter), `**Type:**`, `**Date:**`, `**Status:**` with values like `RESEARCHED`, `VERIFIED`, `IMPLEMENTED`, `OUTDATED`. kebab-case filenames.
- **AICP `sync-kb-to-localai.sh`**: Picks up all `.md` files recursively. Files must be self-contained (no external references needed for chunking).

---

## 2. Architecture

### 2.1 Three-Layer Design

```
┌──────────────────────────────────────────────────────────────────┐
│                     RESEARCH WIKI MONOREPO                        │
│                                                                    │
│  ┌──────────┐    ┌───────────────┐    ┌────────────────────────┐ │
│  │  INTAKE   │───>│  PROCESSING   │───>│    KNOWLEDGE STORE     │ │
│  │           │    │               │    │                          │ │
│  │ raw/      │    │ Claude Code   │    │ wiki/                   │ │
│  │   files   │    │ + wiki-agent  │    │   domains/{domain}/     │ │
│  │   URLs    │    │   skill with  │    │     {topic}.md          │ │
│  │   pastes  │    │   3 ingestion │    │   sources/              │ │
│  │           │    │   modes       │    │     src-{slug}.md       │ │
│  └──────────┘    └───────────────┘    │   comparisons/          │ │
│                                        │     {topic}.md          │ │
│                                        │   index.md              │ │
│                                        │   manifest.json         │ │
│                                        └───────────┬────────────┘ │
│                                                     │              │
│  ┌──────────────────────────────────────────────────┘              │
│  │  INTEGRATION SURFACE                                            │
│  │                                                                 │
│  │  - RAG-ready YAML frontmatter + ## Relationships                │
│  │  - manifest.json (machine-readable full graph)                  │
│  │  - Compatible with openfleet kb_sync.py patterns                │
│  │  - Compatible with AICP docs/kb/ conventions                    │
│  │  - tools/ for linting, export, validation                       │
│  └─────────────────────────────────────────────────────────────────┘
│       │              │                │                │            │
│       ▼              ▼                ▼                ▼            │
│   openfleet       AICP            DSPD         control-plane       │
│   LightRAG     LocalAI KB       (future)         (future)         │
└──────────────────────────────────────────────────────────────────┘
```

### 2.2 Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| YAML frontmatter (not markdown headers) | Richer, machine-parseable, supports arrays/nested structures. Transformed to markdown headers on export for openfleet/AICP compatibility. |
| `## Relationships` with ALL_CAPS verbs | Directly compatible with openfleet `kb_sync.py` regex. No transform needed for LightRAG sync. |
| Domain-organized wiki (not flat) | Supports massive scale. Sub-indexes per domain enable efficient navigation without reading everything. |
| Source provenance on every page | Every claim traces back to a source. Enables confidence assessment and freshness tracking. |
| Multi-resolution content via section markers | Matches openfleet `injection-profiles.yaml` tiers (full/condensed/minimal) and AICP `content_tiers`. No separate files — reader stops at the right heading. |
| manifest.json as integration bridge | Machine-readable graph that any external tool can consume without parsing markdown. |
| Separate sources/ from domains/ | Source synthesis (breakdown of one article) is different from concept pages (synthesized understanding across sources). Keeps concepts clean. |

---

## 3. Page Schema

### 3.1 Frontmatter

```yaml
---
title: "Container Orchestration Patterns"
type: concept
domain: infrastructure
subdomain: containerization              # optional
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-08
sources:
  - id: src-kubernetes-patterns-2026
    type: article
    url: "https://..."
    title: "Kubernetes Patterns 2026"
    ingested: 2026-04-08
  - id: src-karpathy-orchestration-talk
    type: youtube-transcript
    url: "https://..."
    title: "Karpathy on Orchestration"
    ingested: 2026-04-07
tags: [kubernetes, docker, orchestration, scaling, microservices]
aliases: [container-patterns, k8s-orchestration]
complexity: advanced
resolution:
  full: true
  condensed: true
  minimal: true
---
```

### 3.2 Required Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | yes | Human-readable title, must match `# Heading` |
| `type` | enum | yes | `concept`, `source-synthesis`, `comparison`, `reference`, `deep-dive`, `index` |
| `domain` | string | yes | Top-level domain (must exist in `config/domains.yaml` or be created) |
| `subdomain` | string | no | Finer grain within domain |
| `status` | enum | yes | `raw`, `processing`, `synthesized`, `verified`, `stale` |
| `confidence` | enum | yes | `low`, `medium`, `high`, `authoritative` |
| `created` | date | yes | ISO 8601 date |
| `updated` | date | yes | ISO 8601 date |
| `sources` | array | yes | At least one source with `id`, `type`, and `url` or file reference |
| `tags` | array | yes | At least one tag |
| `aliases` | array | no | Alternative names for cross-referencing |
| `complexity` | enum | no | `beginner`, `intermediate`, `advanced`, `expert` |
| `resolution` | object | no | Which resolution tiers are present (auto-detected from sections) |

### 3.3 Page Types

| Type | Purpose | Required Sections | Example |
|------|---------|-------------------|---------|
| `concept` | Synthesized understanding of a topic | Summary, Key Insights, Deep Analysis, Relationships | "Container Orchestration Patterns" |
| `source-synthesis` | Breakdown of a single source | Summary, Key Insights, Relationships | "Synthesis: Karpathy LLM Wiki Post" |
| `comparison` | Side-by-side analysis | Summary, Key Insights, Deep Analysis, Relationships | "RAG vs LLM Wiki vs Knowledge Graph" |
| `reference` | Factual lookup, specs, configs | Summary, Relationships | "LocalAI v4 API Reference" |
| `deep-dive` | Extended analysis with original thinking | Summary, Key Insights, Deep Analysis, Open Questions, Relationships | "Why Deterministic Orchestration Beats LLM Routing" |
| `index` | Domain or topic index page | (structural, no schema enforcement) | "Infrastructure Domain Index" |

### 3.4 Status Lifecycle

```
raw ──> processing ──> synthesized ──> verified
                            │               │
                            └──> stale <─────┘
                                   │
                                   └──> synthesized (after re-review)
```

- **raw** — source dropped in, not yet processed
- **processing** — Claude is actively working on it
- **synthesized** — processed, quality gates passed, ready for use
- **verified** — human-reviewed and confirmed accurate
- **stale** — older than 30 days without review, or superseded by newer info

### 3.5 Page Structure

```markdown
---
(frontmatter)
---

# Title

## Summary
<!-- 2-3 sentences minimum. Becomes "minimal" resolution content. -->
<!-- Used as LightRAG entity description on export. -->

## Key Insights
<!-- Bullet points or short paragraphs. "Condensed" resolution boundary. -->
<!-- Condensed readers stop here. -->

## Deep Analysis
<!-- Full breakdown: comparisons, diagrams, examples, nuance. -->
<!-- Only required for concept, comparison, deep-dive types. -->

## Open Questions
<!-- Gaps identified, things to research further. -->
<!-- Optional but encouraged. Drives gap analysis. -->

## Relationships
- BUILDS ON: Topic A, Topic B
- ENABLES: Topic C (in specific context)
- COMPARES TO: Topic D (different trade-offs)
- DERIVED FROM: src-source-slug
```

### 3.6 Relationship Verbs

| Verb | Semantics | Example |
|------|-----------|---------|
| `BUILDS ON` | Prerequisite knowledge | `BUILDS ON: Docker Fundamentals, Linux Namespaces` |
| `ENABLES` | What this knowledge unlocks | `ENABLES: Microservice Architecture` |
| `COMPARES TO` | Alternatives with different trade-offs | `COMPARES TO: Serverless Patterns` |
| `CONTRADICTS` | Conflicting approaches or findings | `CONTRADICTS: Monolith-First Approach (at scale)` |
| `USED BY` | Which projects/agents consume this | `USED BY: openfleet Infrastructure` |
| `RELATES TO` | General association | `RELATES TO: CI/CD Pipelines` |
| `FEEDS INTO` | Downstream dependency | `FEEDS INTO: AICP Routing Decisions` |
| `DERIVED FROM` | Source attribution | `DERIVED FROM: src-karpathy-llm-wiki` |
| `SUPERSEDES` | Replaces older knowledge | `SUPERSEDES: Old Container Patterns (pre-2025)` |
| `IMPLEMENTS` | Practical application of a concept | `IMPLEMENTS: 12-Factor App Principles` |
| `EXTENDS` | Builds upon with additions | `EXTENDS: Base Orchestration Patterns` |

### 3.7 Resolution System

Maps to openfleet `injection-profiles.yaml` tiers and AICP `content_tiers`:

| Resolution | Sections Included | Use Case |
|------------|-------------------|----------|
| **minimal** | Summary only | localai-8k contexts, quick lookup, manifest descriptions |
| **condensed** | Summary + Key Insights | sonnet-200k contexts, AICP export |
| **full** | All sections | opus-1m contexts, openfleet export, human reading |

Section headings ARE the resolution boundaries. No separate files needed.

---

## 4. Folder Structure

```
devops-solutions-research-wiki/
├── CLAUDE.md                              # System schema, conventions, ingestion modes
├── .claude/
│   └── settings.json                      # Project-level permissions & hooks
│
├── raw/                                   # INTAKE — unprocessed source material
│   ├── transcripts/                       #   YouTube/podcast transcripts
│   ├── articles/                          #   Web clips, blog posts, docs
│   ├── papers/                            #   PDFs, research papers
│   ├── notes/                             #   Personal notes, observations
│   └── dumps/                             #   Anything else
│
├── wiki/                                  # KNOWLEDGE STORE — processed, interlinked
│   ├── index.md                           #   Master index (auto-maintained)
│   ├── manifest.json                      #   Machine-readable graph
│   ├── domains/                           #   Domain-organized knowledge
│   │   ├── _index.md                      #   Domain registry
│   │   ├── ai-agents/
│   │   │   ├── _index.md                  #   Domain index with topic map
│   │   │   ├── llm-wiki-pattern.md
│   │   │   └── multi-agent-orchestration.md
│   │   ├── infrastructure/
│   │   │   ├── _index.md
│   │   │   └── container-orchestration.md
│   │   ├── devops/
│   │   ├── ai-models/
│   │   ├── security/
│   │   └── ...                            #   Domains grow organically
│   ├── sources/                           #   Source synthesis (1:1 with raw sources)
│   │   ├── src-karpathy-llm-wiki.md
│   │   └── src-claude-notebooklm.md
│   └── comparisons/                       #   Cross-cutting analysis
│       └── rag-vs-wiki-vs-graph.md
│
├── tools/                                 # TOOLING — Python utilities
���   ├── validate.py                        #   Frontmatter schema validation
│   ├── manifest.py                        #   Regenerate manifest.json
│   ├── lint.py                            #   Wiki health checks
│   ├── export.py                          #   Export for sister projects
│   └── stats.py                           #   Coverage & growth reporting
│
├── skills/                                # CLAUDE SKILLS
│   └── wiki-agent/
│       └── skill.md                       #   Master skill for all wiki operations
│
├── config/                                # CONFIGURATION
│   ├── domains.yaml                       #   Domain registry with descriptions
│   ├── schema.yaml                        #   Frontmatter schema definition
│   ├── export-profiles.yaml               #   Per-project export transforms
│   └── quality-standards.yaml             #   Linting & validation thresholds
│
└── docs/                                  # PROJECT DOCUMENTATION
    └── superpowers/
        └── specs/
            └── 2026-04-08-research-wiki-design.md  # This document
```

### 4.1 Folder Conventions

- **`_index.md`** in every domain folder — auto-maintained by Claude, lists all pages with one-line descriptions, tag cloud, relationship summary
- **`raw/` is permanent** — raw files stay for provenance, never deleted after processing
- **`wiki/sources/`** holds source-synthesis pages (prefix `src-`), separate from concept pages in `domains/`
- **`wiki/comparisons/`** holds cross-cutting analysis that spans multiple domains
- **Domains grow organically** — Claude creates new domain folders as topics emerge, updates `domains/_index.md` and `config/domains.yaml`
- **kebab-case** for all filenames
- **manifest.json** regenerated after every wiki change

---

## 5. Ingestion Pipeline

### 5.1 Pipeline Stages

```
SOURCE IN ──> EXTRACT ──> ANALYZE ──> SYNTHESIZE ──> WRITE ──> INTEGRATE
   │            │            │            │             │           │
   │         raw text     identify     generate      write to   update
   │         from any     domains,     wiki pages    wiki/      indexes,
   │         format       concepts,    with full     with       manifest,
   │                      gaps,        schema        frontmatter validate
   │                      relations
   │
   ├── Drop file in raw/{subfolder}/
   ├── Give Claude a URL (fetched → saved to raw/)
   └── Paste content directly (saved to raw/notes/)
```

### 5.2 Stage Details

**EXTRACT**
- Read raw source content
- Classify source type (article, transcript, paper, notes, paste)
- Normalize formatting (strip HTML, fix encoding, handle PDF extraction)
- Save to appropriate `raw/` subfolder if not already there (URL fetches, pastes)

**ANALYZE**
- Identify key concepts, claims, arguments, data points
- Determine which domain(s) the source maps to
- Check existing wiki for related/overlapping pages
- Map relationships to existing pages
- Assess source quality and confidence level
- Detect if new domain creation is needed

**SYNTHESIZE**
- Generate source-synthesis page (`wiki/sources/src-{slug}.md`)
- Generate or update concept pages in `wiki/domains/{domain}/`
- Write full frontmatter with all required fields
- Write all required sections per page type
- Write `## Relationships` connecting to existing pages and source page
- Avoid >70% concept overlap with existing pages (update instead of create)

**WRITE**
- Save all pages to wiki/
- Ensure filenames are kebab-case
- Ensure `# Title` matches frontmatter `title`
- Ensure domain folder exists (create if needed)

**INTEGRATE**
- Update affected `_index.md` files (domain indexes, master index)
- Regenerate `manifest.json`
- Run `tools/validate.py` — any errors block completion
- Flag stale pages that may need updating based on new information
- Report summary of changes

### 5.3 Ingestion Modes

#### Mode 1: Autonomous (`auto`)

Claude processes without stopping. Best for bulk ingestion or low-stakes sources.

```
User: "Ingest everything in raw/transcripts/ — auto mode"

Claude: processes all files, reports summary when done
  "Ingested 3 transcripts → 2 source pages, 14 concept pages,
   3 new domains created, 47 relationships mapped"
```

#### Mode 2: Guided (`guided`)

Claude shows the full plan, waits for approval at each stage.

```
User: "Ingest raw/papers/attention-paper.pdf — guided mode"

Claude: analyzes source, presents plan:
  "Source page: src-attention-is-all-you-need
   Concept pages to create (7): [list with domains]
   Concept pages to update (3): [list with changes]
   New domains needed: none
   Proceed?"

User: approves/modifies
Claude: executes, can pause for review after each page
```

#### Mode 3: Smart (`smart`) — Default

Claude decides autonomously when confident, escalates when not.

```
Decision logic:

  IF source maps cleanly to existing domains
     AND no contradictions with existing wiki pages
     AND confidence > medium on all extractions
  THEN → auto (process, report after)

  IF new domain would need to be created
     OR source contradicts existing knowledge
     OR source is ambiguous / multi-interpretation
     OR complexity is expert-level
  THEN → guided (show plan, ask)

  IF source is low-quality or off-topic
  THEN → flag ("This source seems low quality because X. Skip or force?")
```

### 5.4 Source Type Handling

| Source Type | Intake Method | Processing Notes |
|-------------|---------------|------------------|
| Web article | URL → WebFetch → `raw/articles/` | Strip nav/ads, extract main content |
| YouTube transcript | Drop `.txt` in `raw/transcripts/` | Handle timestamp removal, speaker detection |
| PDF / research paper | Drop in `raw/papers/` | Extract text, handle figures/tables as descriptions |
| Personal notes | Drop in `raw/notes/` or paste | Lighter synthesis, more personal context |
| Documentation | URL or file → `raw/articles/` | Preserve code blocks, API signatures |
| Paste | Direct paste in chat | Save to `raw/dumps/{auto-slug}.md` with user-provided context |

### 5.5 Quality Gates

Every wiki page must pass before being written:

| Gate | Criteria | Blocking? |
|------|----------|-----------|
| Frontmatter complete | All required fields present, valid enum values | Yes |
| Summary exists | Minimum 30 words | Yes |
| Relationships exist | Minimum 1 relationship (unless first page in new domain) | Yes |
| Reachable | Page listed in its domain `_index.md` | Yes |
| Source provenance | At least one source with URL or file reference | Yes |
| No duplication | No existing page with >70% concept overlap (Claude uses judgment during ingestion; `tools/lint.py` uses TF-IDF for batch detection) | Yes (update instead) |
| Title consistency | `title` field matches `# Heading` | Yes |
| Domain consistency | `domain` field matches folder path | Yes |

---

## 6. CLAUDE.md Specification

The project `CLAUDE.md` teaches every Claude Code session how to operate the wiki. Full content defined below.

```markdown
# DevOps Solutions Research Wiki

A research-grade knowledge synthesis system and second brain. Central intelligence
spine for the devops ecosystem (openfleet, AICP, DSPD, devops-control-plane).

## What This Is

A monorepo containing:
- An interlinked wiki of synthesized knowledge across domains
- An ingestion pipeline that processes any source type into structured wiki pages
- Tooling for validation, linting, export, and integration with sister projects
- A skill that teaches Claude how to operate the entire system

## Project Structure

- `raw/` — Unprocessed source material (transcripts, articles, papers, notes, dumps)
- `wiki/` — Processed knowledge (domains/, sources/, comparisons/, index.md, manifest.json)
- `tools/` — Python utilities (lint, manifest, export, validate, stats)
- `skills/` — Claude skill definitions
- `config/` — Schema, domain registry, export profiles, quality standards
- `docs/` — Project documentation and specs

## Page Schema

Every wiki page uses YAML frontmatter with these required fields:

  title, type, domain, status, confidence, created, updated, sources, tags

Page types: concept, source-synthesis, comparison, reference, deep-dive, index

Status lifecycle: raw → processing → synthesized → verified → stale

Confidence levels: low, medium, high, authoritative

## Page Structure

Every page follows this section order:

  # Title
  ## Summary          ← minimal resolution (2-3 sentences min, used for LightRAG description)
  ## Key Insights     ← condensed resolution boundary
  ## Deep Analysis    ← full resolution (concept, comparison, deep-dive types)
  ## Open Questions   ← gaps to fill (optional but encouraged)
  ## Relationships    ← VERB: target format, one per line

## Relationship Conventions

Use ALL_CAPS verbs. One relationship per line. Comma-separated targets allowed.

  BUILDS ON, ENABLES, COMPARES TO, CONTRADICTS, USED BY,
  RELATES TO, FEEDS INTO, DERIVED FROM, SUPERSEDES, IMPLEMENTS, EXTENDS

Format: `- VERB: Target Name (optional context)`

Compatible with openfleet kb_sync.py regex: ^([A-Z][A-Z /\-]+?):\s*(.+)$

## Ingestion Modes

Three modes, user specifies or defaults to smart:

- `auto` — Process without stopping. Report summary after.
- `guided` — Show extraction plan. Wait for approval. Review each page.
- `smart` (default) — Auto when confident. Escalate when: new domain,
  contradictions, ambiguity, expert-level complexity, low-quality source.

## Ingestion Sources

Accept any of:
- Files dropped in raw/ (any subfolder)
- URLs (fetch via WebFetch, save to raw/, then process)
- Pasted content (save to raw/dumps/, then process)

## Quality Gates

Every page must have:
- Complete frontmatter with valid values per config/schema.yaml
- Summary (min 30 words)
- At least 1 relationship (unless first in new domain)
- Reachable from domain _index.md
- Source provenance (URL or file reference)
- No >70% concept overlap with existing pages (update instead of create)
- title field matches # Heading
- domain field matches folder path

## Post-Ingestion

After every ingestion:
1. Update affected _index.md files
2. Regenerate manifest.json via tools/manifest.py
3. Run tools/validate.py — errors block completion
4. Flag stale pages affected by new information
5. Report summary of changes

## Integration

This wiki feeds sister projects via file-based export:
- openfleet — LightRAG graph via ## Relationships (kb_sync.py compatible)
- AICP — docs/kb/ via export (tools/export.py)
- DSPD, control-plane — future

Export profiles defined in config/export-profiles.yaml.
Export transforms YAML frontmatter to markdown headers for compatibility.

## Tooling

- `python3 tools/validate.py` — Schema validation (exit 0 = clean, 1 = errors)
- `python3 tools/manifest.py` — Regenerate wiki/manifest.json
- `python3 tools/lint.py [--report|--summary|--fix]` — Health checks
- `python3 tools/export.py [openfleet|aicp]` — Export for sister projects
- `python3 tools/stats.py [--json]` — Coverage & growth reporting

## Conventions

- kebab-case filenames
- One concept per page
- Update existing pages rather than creating duplicates
- Domains grow organically — create new domain folders as needed
- _index.md in every domain folder, auto-maintained
- manifest.json regenerated after every wiki change
- raw/ files kept permanently for provenance
- Sources prefixed with src- in wiki/sources/
```

---

## 7. Wiki-Agent Skill

Located at `skills/wiki-agent/skill.md`. This is the operational manual Claude follows for all wiki operations.

```markdown
# Wiki Agent — Research Wiki Operator

You are operating the devops-solutions-research-wiki. You ingest sources,
query knowledge, maintain quality, and export for sister projects.

Read CLAUDE.md for schema and conventions. Read config/schema.yaml for
validation rules. Read config/domains.yaml for the domain registry.

## Operations

### Ingest

Trigger: user says "ingest", provides a URL, drops a file, or pastes content.
Mode: auto | guided | smart (default: smart)

Pipeline:
1. EXTRACT — read raw source, classify type, normalize formatting
2. ANALYZE — identify domains, concepts, claims, relationships to existing pages
3. SYNTHESIZE — generate wiki pages with full frontmatter and all sections
4. WRITE — save pages to wiki/ (source-synthesis in sources/, concepts in domains/)
5. INTEGRATE — update _index.md files, rebuild manifest.json, validate

For guided mode: present the full extraction plan between ANALYZE and SYNTHESIZE.
Include: source page name, concept pages to create (with domains), concept pages
to update (with what changes), new domains needed, estimated relationship count.
Wait for user approval before proceeding.

For smart mode: decide based on these escalation triggers:
- New domain creation needed → guided
- Contradictions with existing knowledge → guided
- Source is ambiguous or multi-interpretation → guided
- Complexity is expert-level → guided
- Source is low-quality or off-topic → flag and ask
- Everything else → auto

Quality gates (every page):
- Complete frontmatter per config/schema.yaml
- Summary >= 30 words
- At least 1 relationship (unless first in new domain)
- Page listed in domain _index.md
- Source provenance present
- No >70% concept overlap with existing page (update instead)
- title matches # Heading, domain matches folder

Post-ingestion (every time):
1. Update affected _index.md files
2. Run: python3 tools/manifest.py
3. Run: python3 tools/validate.py
4. Flag stale pages needing review
5. Report summary: sources processed, pages created/updated, domains affected,
   relationships added, any warnings

### Query

Trigger: user asks a question about wiki content.

Process:
1. Read wiki/index.md for domain overview
2. Identify relevant domain(s)
3. Read domain _index.md for topic inventory
4. Read relevant pages
5. Synthesize answer
6. Cite which wiki pages informed the answer with file paths

If the answer requires information not in the wiki, say so and offer to research
and ingest new sources.

### Lint

Trigger: user says "lint", "health check", or "check wiki".

Run: python3 tools/lint.py --report

Checks:
- Orphan pages (exist in wiki/ but not in any _index.md)
- Dead relationships (targets that don't resolve to any page)
- Stale pages (updated > 30 days ago, status != stale)
- Thin pages (< 100 words in Deep Analysis for concept/deep-dive types)
- Duplicate detection (>70% Summary overlap between pages)
- Domain balance (domains with < 3 pages flagged as underdeveloped)
- Open Questions density (Open Questions > Deep Analysis word count)
- Isolated clusters (domains with no cross-domain relationships)

Report findings. Offer to fix autonomously or in guided mode.

### Gap Analysis

Trigger: user says "gaps", "what's missing", or "research priorities".

Process:
1. Parse manifest.json for the full relationship graph
2. Find relationship targets that don't have their own wiki page
3. Find domains with few pages or low relationship density
4. Aggregate Open Questions sections across all pages
5. Identify domains with no cross-domain connections

Output: prioritized list of research opportunities with suggested sources.

### Export

Trigger: user says "export for {target}" where target is openfleet, aicp, etc.

Process:
1. Read config/export-profiles.yaml for target configuration
2. Filter pages by min_confidence, min_status, domain filters
3. Transform frontmatter per profile (YAML → markdown headers, type mapping)
4. Copy to target output_dir
5. Report: pages exported, pages skipped (with reasons)

### Stats

Trigger: user says "stats", "status", or "dashboard".

Run: python3 tools/stats.py

Report:
- Total pages by type, domain, status, confidence
- Relationship density (edges per page, most/least connected pages)
- Tag cloud (top 20 tags)
- Freshness (pages by last-updated bucket: <7d, <30d, <90d, >90d)
- Growth over time (pages added per week, from git history)
- Gap score per domain (orphaned refs / total refs ratio)
- Export readiness (% of pages passing each export profile's filters)
```

---

## 8. Tooling

### 8.1 `tools/validate.py`

Schema enforcement against `config/schema.yaml`.

**Validates:**
- YAML frontmatter parses correctly
- All required fields present with valid enum values
- `sources[]` entries have `id`, `type`, and at least `url` or file reference
- `## Relationships` verbs are from the allowed set in `config/schema.yaml`
- Relationship targets either resolve to wiki pages or are flagged as external
- Required sections present per page type
- `title` matches `# Heading`, `domain` matches folder path

**Output:** JSON report with `errors` (blocking) and `warnings` (advisory)
**Exit code:** 0 if clean, 1 if errors

### 8.2 `tools/manifest.py`

Builds machine-readable graph from wiki content.

**Scans:** All `wiki/**/*.md` files
**Parses:** Frontmatter + `## Relationships` from each page
**Produces:** `wiki/manifest.json` containing:
- Full page index with all metadata
- Relationship graph (edges with verbs, source, target)
- Tag index (tag → pages)
- Domain index (domain → pages with counts)
- Orphaned references (relationship targets that don't resolve)
- Stats summary

### 8.3 `tools/lint.py`

Structural and content quality checks beyond schema validation.

**Checks:**
- Orphan pages (in wiki/ but not in any `_index.md`)
- Dead relationships (targets that don't resolve)
- Stale pages (old, not marked stale)
- Thin pages (insufficient content for page type)
- Duplicate detection (TF-IDF cosine similarity on Summary sections)
- Domain balance (underdeveloped domains)
- Open Questions density
- Isolated domain clusters (no cross-domain relationships)

**Modes:** `--report` (JSON), `--summary` (human-readable), `--fix` (auto-fix where possible)

### 8.4 `tools/export.py`

Transforms and copies wiki pages for sister project consumption.

**Driven by:** `config/export-profiles.yaml`
**Per profile:** filters (confidence, status, domains), transforms (frontmatter format, type mapping, metadata injection), resolution level, output directory

**Export targets:**
- `openfleet` — strips YAML frontmatter → markdown headers, maps types to `Research`, preserves `## Relationships`, outputs to `../openfleet/docs/knowledge-map/kb/research-wiki/`
- `aicp` — converts to AICP `**Key:** Value` format, maps to `Research Finding` / `Infrastructure Reference`, condensed resolution, outputs to `../devops-expert-local-ai/docs/kb/research-wiki/`

### 8.5 `tools/stats.py`

Coverage and growth reporting.

**Reads:** `manifest.json` + git history
**Reports:** page counts by dimension, relationship density, tag cloud, freshness distribution, growth trends, gap scores, export readiness percentages

---

## 9. Configuration

### 9.1 `config/schema.yaml`

Source of truth for valid page structure. Defines required fields, enum values, required sections per page type, and allowed relationship verbs.

### 9.2 `config/domains.yaml`

Domain registry with descriptions. New domains added here when created. Drives `wiki/domains/_index.md` generation and validation.

```yaml
domains:
  ai-agents:
    description: "Multi-agent systems, orchestration, fleet management, agent memory"
  ai-models:
    description: "LLMs, embeddings, training, fine-tuning, model evaluation"
  infrastructure:
    description: "Containers, networking, cloud, databases, storage"
  devops:
    description: "CI/CD, deployment, monitoring, IaC, SRE"
  security:
    description: "AppSec, infrastructure security, threat modeling, compliance"
  knowledge-systems:
    description: "RAG, knowledge graphs, wikis, embeddings, search"
  # ... grows organically
```

### 9.3 `config/export-profiles.yaml`

Per-project export configuration. Defines transforms, filters, and output paths. Full specification in Section 8.4.

### 9.4 `config/quality-standards.yaml`

Thresholds for linting and export decisions.

```yaml
page_quality:
  min_summary_words: 30
  min_deep_analysis_words: 100
  min_relationships: 1
  max_open_questions_ratio: 0.5
  stale_threshold_days: 30

domain_health:
  min_pages: 3
  min_cross_domain_relationships: 2

export_readiness:
  min_confidence: medium
  min_status: synthesized
  require_source_provenance: true

duplicate_detection:
  similarity_threshold: 0.70
```

---

## 10. Integration Details

### 10.1 openfleet Compatibility

**Target:** openfleet's `kb_sync.py` which parses `## Relationships` sections and syncs to LightRAG.

**What's compatible out of the box:**
- `## Relationships` section format with `VERB: target` lines
- ALL_CAPS verbs
- Comma-separated targets with parenthetical context

**What needs transformation on export:**
- YAML frontmatter → markdown `**Key:** Value` headers
- Page type → openfleet `TYPE_MAP` value (all map to `research`)
- Add `**Type:** Research` and `**Source Project:** devops-solutions-research-wiki`

**Entity name compatibility:**
- Page titles should avoid `/` and `.` characters (these get mangled by kb_sync.py normalization)
- Relationship targets must match page titles exactly (case-insensitive after normalization)

### 10.2 AICP Compatibility

**Target:** AICP's `docs/kb/` directory, synced to LocalAI Collections via `sync-kb-to-localai.sh`.

**What's compatible out of the box:**
- kebab-case filenames
- One topic per file
- Markdown content with clear sections

**What needs transformation on export:**
- YAML frontmatter → AICP's `**Type:**`, `**Date:**`, `**Status:**`, `**Sources:**` markdown headers
- Status mapping: `synthesized` → `RESEARCHED`, `verified` → `VERIFIED`, `stale` → `OUTDATED`
- Type mapping: `concept`/`source-synthesis`/`comparison`/`deep-dive` → `Research Finding`, `reference` → `Infrastructure Reference`
- Resolution: condensed (Summary + Key Insights only) — AICP has tighter context budgets

### 10.3 manifest.json as Universal Bridge

Any tool or project can consume `wiki/manifest.json` without parsing markdown:

```json
{
  "generated": "2026-04-08T12:00:00Z",
  "stats": {
    "pages": 47,
    "domains": 8,
    "sources": 12,
    "comparisons": 3,
    "relationships": 312,
    "tags_unique": 89
  },
  "pages": [
    {
      "path": "wiki/domains/ai-agents/llm-wiki-pattern.md",
      "title": "LLM Wiki Pattern",
      "type": "concept",
      "domain": "ai-agents",
      "subdomain": null,
      "status": "synthesized",
      "confidence": "high",
      "created": "2026-04-08",
      "updated": "2026-04-08",
      "tags": ["karpathy", "knowledge-base", "markdown"],
      "complexity": "intermediate",
      "source_ids": ["src-karpathy-llm-wiki"],
      "relationships": [
        {"verb": "COMPARES TO", "target": "RAG vs Wiki vs Graph"},
        {"verb": "DERIVED FROM", "target": "src-karpathy-llm-wiki"},
        {"verb": "ENABLES", "target": "Agent Memory Systems"}
      ]
    }
  ],
  "domains": {
    "ai-agents": {"page_count": 12, "relationship_count": 45},
    "infrastructure": {"page_count": 8, "relationship_count": 31}
  },
  "tags": {
    "kubernetes": ["container-orchestration", "deployment-strategies"],
    "karpathy": ["llm-wiki-pattern"]
  },
  "orphaned_refs": [
    {"target": "Service Mesh Architecture", "referenced_by": ["container-orchestration"]}
  ]
}
```

---

## 11. Open Decisions

These are decisions explicitly deferred, not gaps:

| Item | Status | Rationale |
|------|--------|-----------|
| MCP server for wiki queries | Deferred | Build the wiki first, add API later if needed |
| Automated scheduled ingestion | Deferred | Manual/on-demand first, schedule when patterns emerge |
| NotebookLM integration | Out of scope | Not a content creation pipeline |
| LightRAG direct write | Deferred | Export via files first, direct API integration if needed |
| Web UI for browsing | Deferred | Obsidian graph view sufficient initially |
| Multi-user collaboration | Not planned | Single-user second brain |
