# DevOps Solutions Research Wiki

> **The second brain.** A research-grade knowledge synthesis system that serves as the central intelligence hub for a multi-project DevOps ecosystem. AI-maintained, graph-structured, ready for query from humans, agents, and MCP clients.

## What This Is

This is a **continuously evolving knowledge base** — not static documentation. An LLM agent maintains 316+ structured markdown pages organized by domain, type, and maturity layer. Raw sources (articles, transcripts, repos) enter at layer 0 and progressively distill through synthesis → concepts → lessons → patterns → decisions → principles.

It is **the central intelligence hub** for a 5-project ecosystem:
- **Research Wiki** (this project) — where knowledge is synthesized and curated
- **OpenArms** — harness engineering; produces operational lessons back into the wiki
- **OpenFleet** — agent fleet orchestrator; consumes wiki as LightRAG knowledge source
- **AICP** — local-AI complexity-routed inference; implements the $0 target patterns documented here
- **devops-control-plane** — infrastructure governance; uses wiki's methodology

It is **a production system**, not a prototype. The wiki has 313+ pages, 2074+ relationships, 22 standards pages with annotated exemplars, 16 named models with companion standards, and a complete evolution pipeline from raw sources to validated principles.

## Start Here

Pick your entry by role:

| You are... | Read this first |
|-----------|----------------|
| A human exploring the project | This README → [ARCHITECTURE.md](ARCHITECTURE.md) → [wiki/spine/super-model/super-model.md](wiki/spine/super-model/super-model.md) |
| Claude Code (this project's primary AI) | [CLAUDE.md](CLAUDE.md) (auto-loaded) → follows methodology stage gates |
| Any other AI coding tool (Codex, Copilot, Gemini, Cursor) | [AGENTS.md](AGENTS.md) (universal, cross-tool) |
| An agent from another project querying the second brain | MCP server: `.mcp.json` exposes 21 tools. Start with `wiki_status`. |
| A human building/reviewing a wiki model | [wiki/spine/references/model-registry.md](wiki/spine/references/model-registry.md) — all 16 models with standards |
| A human operator running the tools | [TOOLS.md](TOOLS.md) — complete CLI reference |
| A human creating wiki pages | [DESIGN.md](DESIGN.md) — styling + callout vocabulary |
| A skill/command author | [SKILLS.md](SKILLS.md) — skills directory + conventions |
| An integrator from another project | [CONTEXT.md](CONTEXT.md) — identity, phase, constraints |

## What's Inside

### The Spine — Strategic Architecture

- **[Super-Model](wiki/spine/super-model/super-model.md)** — packages all 16 models, 22 standards pages, 5 sub-super-models into a consumable system
- **[Model Registry](wiki/spine/references/model-registry.md)** — all 16 named models with status and standards links
- **16 Models** in `wiki/spine/models/` (e.g. Methodology, LLM Wiki, Claude Code, Context Engineering, Quality, Local AI)
- **22 Standards pages** in `wiki/spine/standards/` — per-type + per-model standards with annotated exemplars
- **5 Sub-super-models** in `wiki/spine/super-model/` — Goldilocks Protocol, Enforcement Hierarchy, Knowledge Architecture, Work Management, Integration & Ecosystem

### Knowledge Layers (Progressive Distillation)

```
L0 raw/           → sources captured verbatim (articles, transcripts, repos, notes)
L1 sources/       → synthesis pages per source (deep read, key insights, cross-references)
L2 concepts/      → domain concept pages (what a thing IS)
L3 comparisons/   → evaluations across alternatives (with recommendations)
L4 lessons/       → convergent evidence from ≥3 sources (00_inbox → 04_principles)
L5 patterns/      → recurring structural phenomena with ≥2 instances
L6 decisions/     → binding choices with alternatives + rationale
L7 principles/    → governing truths derived from ≥3 lessons (04_principles folder)
```

### Work Hierarchy

```
Milestone → Epic → Module → Task
```

Live in `wiki/backlog/`. Every task tracks `readiness` (definition completeness) AND `progress` (execution completeness) independently. 99→100 on either dimension requires human review.

### Operational Layers

- **`raw/`** — unprocessed sources (articles, transcripts, papers, notes, dumps) — kept permanently for provenance
- **`wiki/`** — processed knowledge (domains/, sources/, comparisons/, lessons/, patterns/, decisions/, spine/, backlog/, log/, config/)
- **`tools/`** — Python utilities (pipeline, gateway, validate, lint, obsidian, sync, ingest, mcp_server, ...)
- **`.claude/skills/`** — Claude Code skill definitions
- **`wiki/config/`** — schema, chains, templates, methodology engine, artifact types

## Core Principles

The wiki operates on three principles distilled from convergent evidence:

1. **Infrastructure Over Instructions** — hooks and validators achieve 100% compliance; CLAUDE.md rules alone achieve ~25%. Enforce through tooling, not prose.
2. **Structured Context Governs Agent Behavior More Than Content** — markdown structure (headers, tables, callouts, YAML) programs agent behavior. Same rules as tables: ~60% compliance. As prose: ~25%.
3. **Right Process for Right Context (Goldilocks)** — methodology depth adapts to phase × scale × trust. POC + micro = simplified chain. Production + large + fleet = full chain with immune system.

## Key Features

- **Graph-structured knowledge** — 2074+ relationships across 316 pages. Dense enough to serve as a LightRAG knowledge source.
- **Dual-scope gateway** — CLI tool operates on this wiki (`--brain`) OR another project's wiki (`--wiki-root`). Works as human CLI, agent programmatic interface, or MCP server.
- **Deep GitHub fetch** — ingest pipeline pulls README + up to 30 key files from any GitHub repo. Used to ingest OpenSpec, spec-kit, BMAD-METHOD at 5,000+ line depth.
- **Auto-fix relationships** — pipeline post automatically resolves bare title references to `[[slug|title]]` wikilinks using manifest lookup.
- **Stage-gated methodology** — Document → Design → Scaffold → Implement → Test, enforced by CLAUDE.md ALLOWED/FORBIDDEN tables.
- **Evolution pipeline** — `pipeline evolve --score` ranks pages for promotion based on 6 signals (cross-source convergence, relationship hub, age, etc.)
- **Validation chain** — `pipeline post` runs 6 steps: index → manifest → validate → fix-relationships → backlinks → lint. 0 errors required for any commit.

## Quick Start (Human Operator)

```bash
# Check wiki state
python3 -m tools.pipeline status

# Ingest a URL (auto-classified: YouTube/GitHub/web)
python3 -m tools.pipeline fetch "https://example.com/article"

# Run full post-ingestion chain (validation)
python3 -m tools.pipeline post

# Score evolution candidates
python3 -m tools.pipeline evolve --score

# Query the wiki via gateway
python3 -m tools.gateway query --identity
python3 -m tools.gateway query --models
python3 -m tools.gateway flow --step 1

# Open in Obsidian (Windows vault auto-syncs)
python3 -m tools.sync --watch
```

See [TOOLS.md](TOOLS.md) for the complete command reference.

## How It Connects to the Ecosystem

```
┌─────────────────────────────────────────────────────────────────┐
│  Research Wiki (this project) — the central intelligence hub    │
│                                                                 │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────────┐    │
│  │  Sources    │→ │  Synthesis   │→ │  Models / Standards │    │
│  │  (L0 raw)   │  │  (L1-L3)     │  │  (spine)            │    │
│  └─────────────┘  └──────────────┘  └─────────────────────┘    │
│         │                                     │                 │
│         ↓                                     ↓                 │
│  ┌──────────────────────────────┐  ┌─────────────────────┐    │
│  │  Evolution Pipeline          │  │  Gateway (CLI/MCP)  │    │
│  │  L4 lessons → L5 patterns    │  │                     │    │
│  │  → L6 decisions → principles │  │  Humans / Agents    │    │
│  └──────────────────────────────┘  └─────────────────────┘    │
└──────────────────────┬──────────────────────────┬──────────────┘
                       │                          │
         Lessons feed  │                          │  Knowledge queries
         back in       ↓                          ↓  (read + write-back)
              ┌────────────────┐         ┌─────────────────┐
              │  OpenArms      │         │  OpenFleet      │
              │  (harness)     │         │  (fleet orch.)  │
              └────────────────┘         └─────────────────┘
                       │                          │
                       └──────┐          ┌────────┘
                              ↓          ↓
                       ┌────────────────────┐
                       │  AICP              │
                       │  (local inference) │
                       └────────────────────┘
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full data flow.

## Status

| Metric | Value |
|--------|-------|
| **Pages** | 316 |
| **Relationships** | 2074 |
| **Validation errors** | 0 |
| **Lint issues** | 0 |
| **Models** | 16 (+ 9 methodology models) |
| **Standards** | 22 (all with annotated exemplars) |
| **Sub-super-models** | 5 |
| **Ecosystem project profiles** | 5 |
| **Validated lessons** | 40+ |
| **Validated patterns** | 16+ |
| **Validated decisions** | 16+ |
| **Principles** | 3 |

**Phase:** Production (used daily). **Scale:** Medium (316 pages, growing). **Execution Mode:** Solo (human + Claude, no harness yet). **PM Level:** L1 (wiki backlog + CLAUDE.md directives).

See [CONTEXT.md](CONTEXT.md) for the full identity profile and [wiki/backlog/milestones/second-brain-complete-system-v2-0.md](wiki/backlog/milestones/second-brain-complete-system-v2-0.md) for current milestone status.

## Documentation Map

| File | What You'll Find |
|------|-----------------|
| **README.md** (this file) | Project overview, what it IS, entry points |
| **[AGENTS.md](AGENTS.md)** | Universal cross-tool agent context (Codex, Copilot, Gemini, Cursor, Claude) |
| **[CLAUDE.md](CLAUDE.md)** | Claude Code-specific overrides (Claude Code loads this automatically) |
| **[CONTEXT.md](CONTEXT.md)** | Identity profile, phase, scale, constraints, operator preferences |
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | Data flow, directory topology, module boundaries |
| **[DESIGN.md](DESIGN.md)** | Visual design principles, callout vocabulary, page layout patterns |
| **[TOOLS.md](TOOLS.md)** | Complete CLI reference: pipeline, gateway, view, sync, MCP server |
| **[SKILLS.md](SKILLS.md)** | Skills directory guide, conventions, when to use each |

Each serves ONE concern. Together they form the three-layer agent context architecture (AGENTS.md + CLAUDE.md + Skills) as documented in [[wiki/patterns/01_drafts/three-layer-agent-context-architecture.md]].

## License

MIT. See wiki pages for individual source attributions and licenses.

## Contributing

This is a personal research wiki maintained by the operator with AI assistance. External contributions via:
- Raw sources (URLs, articles, transcripts) — drop in `raw/` subdirectories
- Wiki page corrections — via `gateway contribute --type correction`
- Lessons from your own operational experience — via `gateway contribute --type lesson`

See [CLAUDE.md](CLAUDE.md) for the stage-gated methodology that governs changes.
