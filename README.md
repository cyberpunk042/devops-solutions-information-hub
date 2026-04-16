# DevOps Solutions Research Wiki

> **The second brain.** A shared knowledge system that holds methodology, standards, validated lessons, patterns, and decisions across a multi-project DevOps ecosystem. AI-maintained, graph-structured, queryable from any connected project via CLI or MCP.

## What This Is

This is a **continuously evolving knowledge base** maintained by an LLM agent. 339+ structured markdown pages organized by domain, type, and maturity layer. Raw sources (articles, transcripts, repos) enter at layer 0 and progressively distill through synthesis, concepts, lessons, patterns, decisions, and principles.

It is **a production system**, not a prototype — used daily, blocking real decisions, validated by a 6-step pipeline that enforces 0 errors on every change.

## Critical Distinction: Brain vs Second Brain

Every project in this ecosystem has its own **brain** — the files that constitute its agent:
- CLAUDE.md, AGENTS.md, DESIGN.md, SOUL.md
- Skills, hooks, commands, settings
- Project-specific configuration and rules

The **second brain** is THIS wiki — a separate, shared knowledge system that all projects consume from and contribute to. Projects query it for methodology and standards. Projects contribute operational learnings back to it. The second brain evolves from those contributions.

**Do not confuse the two.** Your project's brain governs YOUR agent. The second brain is a shared resource you connect to.

## The 5-Project Ecosystem

| Project | Role | Relationship to the Second Brain |
|---------|------|----------------------------------|
| **Research Wiki** (this) | Knowledge synthesis and curation | IS the second brain |
| **OpenArms** | Personal AI assistant, harness engineering | Feeds operational lessons back; consumes methodology |
| **OpenFleet** | Agent fleet orchestrator (10 agents, 30s cycle) | Consumes wiki as LightRAG knowledge source; feeds fleet lessons back |
| **AICP** | Local-AI inference routing ($0 target) | Implements patterns documented here; consumes routing decisions |
| **devops-control-plane** | Infrastructure governance | 16 post-mortems became OpenFleet's immune system rules; uses wiki methodology |

Knowledge flows **bidirectionally**: the second brain spreads methodology outward, projects contribute learnings inward.

## Start Here

| You are... | First step |
|-----------|-----------|
| **A human on a new machine** | [Setup](#setup-on-a-new-machine) below |
| **An agent inside the second brain (fresh)** | `python3 -m tools.gateway orient` |
| **An agent in a sister project** | Read your AGENTS.md → see "Second Brain Connection" section → `python3 -m tools.gateway orient` |
| **Claude Code in this project** | [CLAUDE.md](CLAUDE.md) loads automatically → run `gateway orient` if fresh |
| **Any other AI tool (Codex, Copilot, Gemini, Cursor)** | [AGENTS.md](AGENTS.md) — universal cross-tool context |
| **A human browsing the knowledge** | `python3 -m tools.view spine` |
| **A human running tools** | [TOOLS.md](TOOLS.md) — complete CLI reference |

## Setup on a New Machine

### Prerequisites

- **Git** (to clone repos)
- **Python 3.8+** (3.11 recommended)
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** (fast Python package installer — setup uses it to create the venv and install deps)

### Step-by-step

```bash
# 1. Clone the second brain
git clone <repo-url> ~/devops-solutions-information-hub
cd ~/devops-solutions-information-hub

# 2. Full setup (creates .venv, installs deps, configures Obsidian if present)
python3 -m tools.setup

# 3. Generate the machine-specific .mcp.json (REQUIRED after clone on any new machine)
#    .mcp.json is gitignored — each machine regenerates it with its own absolute paths.
python3 -m tools.setup --init

# 4. Verify — should print PASS with 0 errors
python3 -m tools.pipeline post

# 5. Orient — should show the second-brain orientation
python3 -m tools.gateway orient

# 6. Browse — should show all 16 models, standards, sub-models
python3 -m tools.view spine
```

**Why step 3?** MCP protocol requires absolute paths in `command` and `cwd`. Committing those would hardcode one user's home directory. `.mcp.json` is gitignored and regenerated per-machine by `--init`. The committed `.mcp.json.template` shows the expected structure.

### Connecting sister projects

Sister projects need to be cloned first, then connected:

```bash
# Connect one project
python3 -m tools.setup --connect-project ~/openarms

# Or connect ALL projects from the registry (sister-projects.yaml)
python3 -m tools.setup --connect-all

# Disconnect a project
cd ~/openarms && python3 ~/devops-solutions-information-hub/tools/setup.py --disconnect
```

**What `--connect` does** (one command, four things):
1. Writes a `research-wiki` MCP server entry into the sister's `.mcp.json`
2. Creates `tools/gateway.py` forwarder so `python3 -m tools.gateway orient` works from the sister
3. Creates `tools/view.py` forwarder so `python3 -m tools.view spine` works from the sister
4. Adds a `## Second Brain Connection` section to the sister's AGENTS.md (or CLAUDE.md) so agents know the connection exists on first load

**The second brain does NOT push anything.** The sister project decides whether to query, when to query, and what to consume. The connection makes it possible; the sister makes the choice.

### Auto-detection

Gateway commands auto-detect the second brain by searching for `devops-solutions-information-hub` or `devops-solutions-research-wiki` in sibling directories and the home directory. No `--brain` flag needed in most cases. Override with `--brain /path/to/second-brain` if auto-detection fails.

## For Agents in Sister Projects

After `--connect`, a fresh agent in a sister project follows this flow:

```
1. AGENTS.md loads → agent sees "Second Brain Connection" section
2. Agent runs: python3 -m tools.gateway orient
   → detects sister + fresh → shows:
      - YOUR BRAIN IS YOUR OWN (distinction)
      - THE SECOND BRAIN IS SEPARATE (what it holds)
      - THREE PRINCIPLES (the rules)
      - HOW TO CONSUME (6 steps)
      - NEXT: query the second brain

3. Agent browses: python3 -m tools.view spine
   → sees all 16 models, 5 sub-models, standards, paths

4. Agent routes: python3 -m tools.gateway what-do-i-need
   → sees methodology model table:
      Feature/epic → feature-development → document → design → scaffold → implement → test
      Bug fix      → bug-fix            → document → implement → test
      Research     → research           → document → design
      ...etc

5. Agent picks a model, follows stages, produces artifacts

6. Agent contributes: python3 -m tools.gateway contribute --type lesson --title "..."
   → learning lands in 00_inbox for operator review
```

**MCP tools** are also available in Claude Code sessions: `wiki_gateway_orient`, `wiki_gateway_query`, `wiki_search`, `wiki_read_page`, `wiki_gateway_contribute`, `wiki_gateway_timeline`, and 20+ more.

## Browsing the Knowledge (`tools.view`)

The view tool is the **primary interface** for exploring what the second brain knows. Works from any connected project. When called from outside the second brain, the first line shows the root path so all file references are resolvable.

```bash
python3 -m tools.view --help             # list all available commands
```

| Command | What it shows |
|---------|--------------|
| `python3 -m tools.view` | Full wiki tree — pages, relationships, domains (dashboard) |
| `python3 -m tools.view spine` | Super-model + 5 sub-models + all 16 models with summaries and paths |
| `python3 -m tools.view model <name>` | One model in full — summary, key insights, lessons learned, standards, open questions |
| `python3 -m tools.view model methodology` | How work proceeds — 9 models, stage gates, ALLOWED/FORBIDDEN |
| `python3 -m tools.view model llm` | What the wiki IS — schema, operations, quality gates |
| `python3 -m tools.view lessons` | 44 validated lessons grouped by category (failure, evolved, hub, other) |
| `python3 -m tools.view patterns` | 19 validated patterns with summaries and maturity |
| `python3 -m tools.view decisions` | 16+ decision records with summaries |
| `python3 -m tools.view principles` | 3 governing principles (the highest knowledge layer) |
| `python3 -m tools.view standards` | 25 standards pages (per-type + per-model + gateway output contract) |
| `python3 -m tools.view domain <name>` | One domain with all pages and summaries |
| `python3 -m tools.view search "<query>"` | Full-text search across the entire wiki |
| `python3 -m tools.view refs "<title>"` | Trace relationships for a specific page |
| `python3 -m tools.view model <name> --full` | Complete page content (no truncation) |

**This is how you understand what the second brain knows.** The gateway routes you to the right task; the view lets you READ the knowledge.

## Gateway Commands (`tools.gateway`)

The gateway is the **operational interface** — orientation, task routing, queries, timeline, contributions. Works from any connected project.

### Orientation (canonical first step)

```bash
python3 -m tools.gateway orient              # auto-detects context (second-brain / sister / external)
python3 -m tools.gateway orient --fresh      # force fresh mode (e.g. after compaction)
python3 -m tools.gateway orient --format json # structured output for programmatic use
```

`orient` detects WHERE you are (inside the second brain, a sister project, or an external client) and WHETHER you're fresh (first contact) or returning. Shows context-appropriate orientation:
- **Second brain + fresh**: 3 principles, 10 knowledge-verb framework, standing rules, reading path
- **Sister + fresh**: brain vs second brain distinction, consumption guide, 3 principles
- **External**: MCP tool list, one-shot orientation pointers

### Task routing

```bash
python3 -m tools.gateway what-do-i-need     # context-aware task routing
```

Shows the methodology models available for your context:
- **Inside the second brain**: knowledge-project verbs (aggregate, process, evaluate, learn, integrate, modelize, validate, standardize, teach, offer)
- **From a sister project**: app-project methodology models (feature-development, bug-fix, research, hotfix, refactor, documentation, integration) with stage sequences

### Queries, timeline, contributions

```bash
# Query methodology
python3 -m tools.gateway query --models           # all 9 methodology models
python3 -m tools.gateway query --model bug-fix     # one model's stages and artifacts
python3 -m tools.gateway query --identity          # project identity profile
python3 -m tools.gateway query --profiles          # SDLC profiles (simplified/default/full)

# Computed timeline
python3 -m tools.gateway timeline --scope all --since 7d    # cross-project activity
python3 -m tools.gateway timeline --epic E022                # one epic's events

# Contribute learnings
python3 -m tools.gateway contribute --type lesson --title "..." --content "..."
python3 -m tools.gateway contribute --type correction --title "..." --content "..."
```

See [TOOLS.md](TOOLS.md) for the complete command reference.

## What's Inside

### Knowledge Layers (Progressive Distillation)

```
L0 raw/           → sources captured verbatim (articles, transcripts, repos, notes)
L1 sources/       → synthesis pages per source (deep read, key insights, cross-references)
L2 concepts/      → domain concept pages (what a thing IS)
L3 comparisons/   → evaluations across alternatives (with recommendations)
L4 lessons/       → convergent evidence from ≥3 sources (00_inbox → 04_principles)
L5 patterns/      → recurring structural phenomena with ≥2 instances
L6 decisions/     → binding choices with alternatives + rationale
L7 principles/    → governing truths derived from ≥3 validated lessons
```

Each layer is denser and more actionable than the previous. The evolution pipeline (`pipeline evolve --score`) identifies pages ready for promotion based on 6 deterministic signals.

### The Spine (Strategic Architecture)

- **[Super-Model](wiki/spine/super-model/super-model.md)** — packages all 16 models + 5 sub-models into a consumable system
- **[Model Registry](wiki/spine/references/model-registry.md)** — all 16 models with status and standards links
- **16 Models** in `wiki/spine/models/` organized by category:
  - **Foundation**: LLM Wiki (what the wiki IS), Methodology (how work proceeds), Wiki Design (how pages look)
  - **Agent config**: Claude Code (the runtime), Skills/Commands/Hooks (extension system), Markdown as IaC (config files as code)
  - **Quality**: SFIF (build lifecycle), Quality & Failure Prevention (three-layer defense)
  - **Depth**: Knowledge Evolution, Second Brain, Context Engineering, NotebookLM, Local AI
  - **Ecosystem**: Ecosystem Architecture, Automation Pipelines, MCP/CLI Integration
- **25 Standards pages** in `wiki/spine/standards/` — per-type + per-model + gateway output contract, each with annotated exemplars
- **5 Sub-super-models** — Goldilocks Protocol, Enforcement Hierarchy, Knowledge Architecture, Work Management, Integration & Ecosystem

### Work Hierarchy

```
Milestone → Epic → Module → Task
```

Live in `wiki/backlog/`. Every task tracks `readiness` (definition completeness) AND `progress` (execution completeness) independently. 99→100 on either dimension requires human review.

### Directory Structure

```
raw/                    → unprocessed sources (permanent provenance)
wiki/                   → processed knowledge
  domains/              → L2 concept pages by domain
  sources/              → L1 source-synthesis pages
  comparisons/          → L3 comparison pages
  lessons/              → L4 lessons (00_inbox → 04_principles)
  patterns/             → L5 patterns (00_inbox → 03_validated)
  decisions/            → L6 decisions (00_inbox → 03_validated)
  spine/                → strategic architecture (models, standards, references)
  backlog/              → project management (epics, modules, tasks)
  log/                  → operator directives, session logs
  config/               → schema, methodology, templates, profiles
  ecosystem/            → project identity profiles
tools/                  → Python utilities (pipeline, gateway, view, validate, lint, ...)
.claude/skills/         → Claude Code skill definitions
docs/                   → session handoffs, promotion reviews
```

## Core Principles

Three principles distilled from ≥3 converging validated lessons each. They govern all agent behavior and wiki design:

**1. Infrastructure Over Instructions**
If a rule can be checked by a tool, enforce it structurally (hooks, validators, pipeline post), not with prose rules. Measured: CLAUDE.md prose rules achieve ~25% compliance. Hooks achieve 100%. Same rules, different enforcement mechanism, categorical difference. BUT enforcement must be mindful — every block needs a reason and a bypass mechanism.

**2. Structured Context Governs Agent Behavior More Than Content**
Tables, MUST/MUST NOT lists, YAML fields, and callout types program agent behavior more reliably than natural language paragraphs. Design every injection (CLAUDE.md, skills, tool output) as a structured program, not a prose instruction. Same content restructured from paragraphs to tables: 25% → 60% compliance improvement.

**3. Right Process for Right Context (Goldilocks)**
Process must adapt to identity (type, phase, scale, PM level). A POC doesn't need full enforcement. Production does. Don't hardcode one process level for all contexts. The Goldilocks point shifts as the project matures — the framework adapts because it's designed to adapt.

## The Methodology

9 named models. Each defines a different stage sequence for a different kind of work:

| Task type | Model | Stages |
|-----------|-------|--------|
| Feature / epic | feature-development | document → design → scaffold → implement → test |
| Bug fix | bug-fix | document → implement → test |
| Research / spike | research | document → design (caps at 50% readiness) |
| Documentation | documentation | document |
| Refactor | refactor | document → scaffold → implement → test |
| Hotfix (known fix) | hotfix | implement → test |
| Integration | integration | scaffold → implement → test |
| Knowledge evolution | knowledge-evolution | document → implement |
| Project lifecycle (SFIF) | project-lifecycle | scaffold → foundation → infrastructure → features |

Each stage has explicit ALLOWED and FORBIDDEN artifact lists. Methodology is DATA defined in `wiki/config/methodology.yaml`, not hardcoded in logic.

See `python3 -m tools.view model methodology` for the full model with real examples, 7 battle-tested bugs, and the enforcement hierarchy.

## Validation & Quality

Every wiki change must pass the 6-step validation chain:

```bash
python3 -m tools.pipeline post
```

1. **Rebuild indexes** — `_index.md` per domain and layer
2. **Regenerate manifest** — `manifest.json` with all page metadata
3. **Validate** — frontmatter schema, required sections, per-type thresholds (BLOCKS on errors)
4. **Fix relationships** — resolve bare titles to `[[slug|title]]` wikilinks
5. **Lint** — orphans, thin pages, broken relationships, staleness
6. **Rebuild layer indexes** — lessons, patterns, decisions, spine

**0 errors required.** Validation errors block completion. This is not advisory.

## Status

| Metric | Value |
|--------|-------|
| **Pages** | 339 |
| **Relationships** | 2263 |
| **Validation errors** | 0 |
| **MCP tools** | 26+ |
| **Models** | 16 named + 9 methodology models |
| **Standards** | 25 (per-type + per-model + gateway output contract) |
| **Sub-super-models** | 5 |
| **Validated lessons** | 44 |
| **Validated patterns** | 19 |
| **Validated decisions** | 16+ |
| **Principles** | 3 |
| **Ecosystem projects** | 5 (all connectable via `--connect`) |

**Phase:** Production. **Scale:** Medium (339 pages, growing). **Execution Mode:** Solo. **PM Level:** L1.

## How It Connects to the Ecosystem

```
┌─────────────────────────────────────────────────────────────────┐
│  Second Brain (this project)                                    │
│                                                                 │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────────┐    │
│  │  Sources    │→ │  Synthesis   │→ │  Models / Standards │    │
│  │  (L0 raw)   │  │  (L1-L3)     │  │  (spine)            │    │
│  └─────────────┘  └──────────────┘  └─────────────────────┘    │
│         │                                     │                 │
│         ↓                                     ↓                 │
│  ┌──────────────────────────────┐  ┌─────────────────────┐    │
│  │  Evolution Pipeline          │  │  Gateway + View     │    │
│  │  L4 lessons → L5 patterns    │  │  (CLI / MCP)        │    │
│  │  → L6 decisions → principles │  │  Humans / Agents    │    │
│  └──────────────────────────────┘  └─────────────────────┘    │
└──────────────────────┬──────────────────────────┬──────────────┘
                       │                          │
         Lessons feed  │                          │  Knowledge queries
         back in       ↓                          ↓  (read + contribute)
              ┌────────────────┐         ┌─────────────────┐
              │  OpenArms      │         │  OpenFleet      │
              │  (harness)     │         │  (fleet orch.)  │
              └────────────────┘         └─────────────────┘
                       │                          │
                       └──────┐          ┌────────┘
                              ↓          ↓
              ┌──────────────────┐  ┌────────────────────┐
              │  AICP            │  │  control-plane     │
              │  (local AI)      │  │  (governance)      │
              └──────────────────┘  └────────────────────┘
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full data flow.

## Documentation Map

| File | What You'll Find |
|------|-----------------|
| **README.md** (this file) | Project overview, setup, browsing, gateway commands |
| **[AGENTS.md](AGENTS.md)** | Universal cross-tool agent context (hard rules, stage gates, page schema) |
| **[CLAUDE.md](CLAUDE.md)** | Claude Code-specific overrides (auto-loaded by Claude Code) |
| **[CONTEXT.md](CONTEXT.md)** | Identity profile, phase, scale, constraints, active epics |
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | Data flow, directory topology, module boundaries |
| **[DESIGN.md](DESIGN.md)** | Visual design: callout vocabulary, page layouts, styling |
| **[TOOLS.md](TOOLS.md)** | Complete CLI reference: pipeline, gateway, view, sync, MCP |
| **[SKILLS.md](SKILLS.md)** | Skills directory, conventions, when to use each |

Each file serves ONE concern. Together they form the three-layer agent context architecture: AGENTS.md (universal) + CLAUDE.md (tool-specific) + Skills (on-demand).

## Contributing

Contributions flow through the gateway, not through manual file creation:

```bash
# Contribute a lesson from operational experience
python3 -m tools.gateway contribute --type lesson --title "What I learned" --content "..."

# Contribute a correction to existing knowledge
python3 -m tools.gateway contribute --type correction --title "Fix in page X" --content "..."
```

Contributions land in `wiki/lessons/00_inbox/` (lessons) or `wiki/log/` (corrections). Promotion through the maturity ladder (`00_inbox → 01_drafts → 02_synthesized → 03_validated → 04_principles`) requires operator review. The second brain does not auto-promote — trust is earned through evidence.

## License

MIT. See wiki pages for individual source attributions and licenses.
