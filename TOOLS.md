# TOOLS.md — Research Wiki Command Reference

Complete command reference. All commands run from the project root.
Audience: human operators and AI agents.

**Quick orientation:**
- `pipeline` — primary entry point: fetch, validate, scaffold, analyze, chain
- `gateway` — unified knowledge interface: query methodology, move/archive pages, Goldilocks flow
- `view` — browse and search the wiki tree
- `sync` — WSL ↔ Windows (Obsidian) sync daemon
- `validate`, `lint`, `stats` — quality and health checks
- `export` — push pages to sister projects
- `evolve` — knowledge evolution pipeline (L0 raw → L6 decisions)
- `setup` — environment bootstrap

---

## 1. Pipeline (`tools.pipeline`)

```
python3 -m tools.pipeline <command> [args] [flags]
```

### Global Flags

| Flag | Short | What It Does |
|------|-------|--------------|
| `--json` | | JSON output |
| `--quiet` | `-q` | Minimal output |
| `--parallel N` | `-p N` | Max parallel workers (default: 4) |
| `--batch FILE` | | File of URLs, one per line (`fetch`, `run`) |
| `--topic QUERY` | | Research topic to queue (`fetch`) |
| `--epic ID` | | Show one epic's detail (`backlog`) |
| `--list` | | List available chains (`chain`) |

---

### `pipeline post`

Run the full post-ingestion validation chain.

```bash
python3 -m tools.pipeline post
```

**6 steps:** rebuild domain indexes → regenerate manifest.json → validate pages → regenerate wikilinks → run lint → report summary.

Run after every wiki change. Required before declaring work complete. Zero errors = done.

---

### `pipeline fetch`

Fetch URLs into `raw/`. Auto-classifies source type (article, YouTube, GitHub deep-fetch).

```bash
python3 -m tools.pipeline fetch https://example.com/article
python3 -m tools.pipeline fetch URL1 URL2 URL3
python3 -m tools.pipeline fetch --batch urls.txt          # one URL per line
python3 -m tools.pipeline fetch --topic "LLM inference"  # queue research topic
```

---

### `pipeline scan`

Scan a local project and copy key documents (CLAUDE.md, README, architecture docs) into `raw/`.

```bash
python3 -m tools.pipeline scan ../openfleet/
python3 -m tools.pipeline scan /home/jfortin/devops-control-plane/
```

---

### `pipeline status`

Show **pipeline's internal plumbing state** — raw files by category (awaiting ingestion) and wiki page count. This is the WRITE-side tool's own inventory.

For **project-level status** (identity, SDLC profile, models, etc.), use `gateway status` — that's the READ-side dashboard for the project as a whole.

```bash
python3 -m tools.pipeline status       # pipeline state: raw/ inventory + wiki page count
python3 -m tools.gateway status        # project dashboard: identity + profile + models + navigation
```

| Concern | Command | Why |
|---------|---------|-----|
| How many unprocessed sources in raw/? | `pipeline status` | Pipeline's inbox |
| Who am I? What profile am I on? | `gateway status` | Project identity |

---

### `pipeline run`

Parallel fetch + full post-chain in one command.

```bash
python3 -m tools.pipeline run https://example.com/article
python3 -m tools.pipeline run URL1 URL2 URL3
python3 -m tools.pipeline run --batch urls.txt
```

---

### `pipeline gaps`

Gap analysis: orphaned link targets, thin pages, weak domains, open questions, disconnected pages.

```bash
python3 -m tools.pipeline gaps
```

---

### `pipeline crossref`

Cross-reference analysis: pages that should link to each other but don't, potential comparison candidates.

```bash
python3 -m tools.pipeline crossref
```

---

### `pipeline scaffold`

Create a new wiki page from template. Scaffolds to the correct inbox/draft folder.

```bash
# Wiki page types
python3 -m tools.pipeline scaffold concept "LLM Context Windows"
python3 -m tools.pipeline scaffold lesson "Always Verify Before Done"
python3 -m tools.pipeline scaffold pattern "Idempotent Deployment"
python3 -m tools.pipeline scaffold decision "Use PydanticAI over LangChain"
python3 -m tools.pipeline scaffold source-synthesis "Synthesis — OpenFleet Architecture"
python3 -m tools.pipeline scaffold deep-dive "Claude Code Extension System"
python3 -m tools.pipeline scaffold comparison "PydanticAI vs LangGraph vs DSPy"
python3 -m tools.pipeline scaffold epic "E018 — Local Inference Pipeline"
python3 -m tools.pipeline scaffold task "T002 — Validate VLLM batch endpoint"

# Methodology document templates
python3 -m tools.pipeline scaffold methodology/requirements-spec "Requirements — LLM Gateway"
python3 -m tools.pipeline scaffold methodology/tech-spec "Tech Spec — MCP Server Expansion"
python3 -m tools.pipeline scaffold methodology/design-doc "Design — Knowledge Evolution v2"
python3 -m tools.pipeline scaffold methodology/task-plan "Plan — Ingest New Sources Sprint"
```

**All wiki page types:** concept, source-synthesis, comparison, reference, deep-dive, index, lesson, pattern, decision, principle, domain-overview, learning-path, evolution, operations-plan, milestone, epic, module, task, note

Never create wiki pages by hand — always scaffold first, then fill in content.

---

### `pipeline evolve`

Aliases for `tools.evolve`. See [Section 9](#9-evolution-pipeline-toolsevolve).

```bash
python3 -m tools.pipeline evolve --score   # rank candidates
python3 -m tools.pipeline evolve --review  # review maturity
```

---

### `pipeline backlog` (DEPRECATED)

Backlog is a KNOWLEDGE query, not a pipeline operation. Use `gateway query --backlog` instead — it's the canonical interface and works for external consumers too.

```bash
# DEPRECATED — prints warning, still works
python3 -m tools.pipeline backlog

# CANONICAL
python3 -m tools.gateway query --backlog
```

---

### `pipeline chain`

Run a named multi-step chain.

```bash
python3 -m tools.pipeline chain --list          # list all chains
python3 -m tools.pipeline chain continue        # session entry point
python3 -m tools.pipeline chain health          # minimal wiki health check
python3 -m tools.pipeline chain review          # full weekly review
python3 -m tools.pipeline chain evolve          # score + scaffold + post
```

**All chains:**

| Chain | What It Does | Input? |
|-------|-------------|--------|
| `continue` | Resume mission: status → review → score → gaps | No |
| `health` | Post-chain → gaps → crossref | No |
| `review` | Post-chain → evolve review → gaps → crossref | No |
| `publish` | Post-chain → sync to Windows | No |
| `analyze` | Gap analysis → crossref → post-chain | No |
| `evolve` | Score candidates → scaffold top N → post-chain | No |
| `evolve-auto` | Score → scaffold → generate (local model) → post-chain | No |
| `spine-refresh` | Score domain-overview candidates → generate → post-chain | No |
| `deep` | Gaps → crossref → mirror → sync (full analysis + integration) | No |
| `mirror` | Push wiki source URLs to NotebookLM | No |
| `ingest` | Fetch URLs → post-chain | Yes (URLs) |
| `ingest-local` | Scan local projects → post-chain | Yes (paths) |
| `full` | Fetch → post → gaps → crossref → sync | Yes (URLs) |
| `research` | NotebookLM research → fetch results → post-chain | Yes (topics) |

---

### `pipeline integrations`

Check integration status (Obsidian, NotebookLM).

```bash
python3 -m tools.pipeline integrations
```

---

## 2. Gateway (`tools.gateway`)

Unified knowledge interface for humans, agents, and MCP. Operates on the local wiki by default.

```
python3 -m tools.gateway <command> [args] [flags]
```

### Global Flags

| Flag | What It Does |
|------|-------------|
| `--wiki-root /path/` | Target a different project's wiki |
| `--brain /path/` | Point to second brain (auto-detected if not specified) |

---

### Discovery Commands

```bash
python3 -m tools.gateway                  # guided entry — shows paths per user type
python3 -m tools.gateway what-do-i-need   # auto-detect identity → recommend chain + first steps
python3 -m tools.gateway status           # full dashboard: identity, chain, models, navigation
python3 -m tools.gateway navigate         # full knowledge tree with CLI commands at each branch
```

---

### `gateway flow`

Goldilocks 8-step routing from "who am I?" to "what do I do next?".

```bash
python3 -m tools.gateway flow            # overview of all 8 steps
python3 -m tools.gateway flow --step 3  # detail for one step
```

| Step | Name | Command |
|------|------|---------|
| 1 | DETECT | `gateway what-do-i-need` |
| 2 | DECLARE | `gateway query --identity` |
| 3 | SELECT CHAIN | `gateway query --chains` |
| 4 | SELECT MODEL | `gateway query --models` |
| 5 | ENTER STAGE | `gateway query --stage document` |
| 6 | PRODUCE | `gateway query --model feature-development --full-chain` |
| 7 | TRACK | `gateway query --field readiness` |
| 8 | FEEDBACK | `gateway contribute --type lesson ...` |

---

### `gateway query`

Query the methodology knowledge base.

```bash
python3 -m tools.gateway query --identity                             # project identity from CLAUDE.md
python3 -m tools.gateway query --models                               # all methodology models with stages
python3 -m tools.gateway query --model feature-development            # one model
python3 -m tools.gateway query --model feature-development --full-chain  # model + full artifact chain
python3 -m tools.gateway query --profiles                             # all SDLC profiles
python3 -m tools.gateway query --profile default                        # chain detail: stages, gates, enforcement
python3 -m tools.gateway query --stage document                       # stage requirements
python3 -m tools.gateway query --stage scaffold --domain typescript   # stage + domain overrides
python3 -m tools.gateway query --field readiness                      # explain a frontmatter field
python3 -m tools.gateway query --backlog                              # epics, readiness, impediments
python3 -m tools.gateway query --lessons                              # lessons by maturity folder
python3 -m tools.gateway query --logs                                 # recent log entries
python3 -m tools.gateway query --page "Model Registry"                # page metadata + summary
python3 -m tools.gateway query --mapping                              # all archived/moved page locations
python3 -m tools.gateway query --mapping "Old Title"                  # location for a specific page
python3 -m tools.gateway query --json                                 # JSON output (any query)
```

---

### `gateway template`

Get a page template by type (prints to stdout).

```bash
python3 -m tools.gateway template lesson
python3 -m tools.gateway template pattern
python3 -m tools.gateway template decision
python3 -m tools.gateway template concept
python3 -m tools.gateway template epic
python3 -m tools.gateway template task
python3 -m tools.gateway template methodology/requirements-spec
python3 -m tools.gateway template methodology/tech-spec
python3 -m tools.gateway template methodology/design-doc
```

---

### `gateway config`

Render a config section as markdown (dot-notation paths).

```bash
python3 -m tools.gateway config methodology.models
python3 -m tools.gateway config methodology.stages
python3 -m tools.gateway config chains
```

---

### `gateway move`

Move a wiki page and update ALL wikilink references across the wiki.

```bash
python3 -m tools.gateway move "Old Page Title" --to domains/ai-agents/ --dry-run
python3 -m tools.gateway move "Old Page Title" --to domains/ai-agents/
```

Never move files manually — this command updates all backlinks.

---

### `gateway archive`

Archive a page with a location mapping entry so old links remain resolvable.

```bash
python3 -m tools.gateway archive "Page Title" --dry-run
python3 -m tools.gateway archive "Page Title"
```

---

### `gateway backup`

Full wiki backup to a timestamped directory.

```bash
python3 -m tools.gateway backup --target /path/to/backup/dir/
# Creates: backup-dir/wiki-backup-YYYY-MM-DD/
```

---

### `gateway factory-reset`

Reset wiki to clean template state. Dry-run by default; creates backup before executing.

```bash
python3 -m tools.gateway factory-reset            # dry run (safe)
python3 -m tools.gateway factory-reset --confirm  # execute (creates backup first)
```

---

### `gateway contribute`

Write back to the wiki as an agent — lesson, remark, or correction.

```bash
python3 -m tools.gateway contribute \
  --type lesson \
  --title "Always Verify Output Before Reporting Done" \
  --content "Evidence from three sessions: ..." \
  --domain cross-domain
```

| Flag | Values | Required? |
|------|--------|-----------|
| `--type` | `lesson`, `remark`, `correction` | Yes |
| `--title` | string | Yes |
| `--content` | string | Yes |
| `--domain` | domain name | No (default: `cross-domain`) |

---

### Dual-Scope Usage

```bash
# Query the second brain from a sister project
python3 -m tools.gateway --wiki-root /home/jfortin/devops-solutions-research-wiki query --models

# Use second brain methodology while targeting openfleet's wiki
python3 -m tools.gateway \
  --wiki-root /home/jfortin/openfleet/wiki \
  --brain /home/jfortin/devops-solutions-research-wiki \
  query --stage document --domain typescript
```

---

## 3. View (`tools.view`)

Dashboard, navigation, and search.

```
python3 -m tools.view [command] [argument] [--brief] [--full] [--type TYPE]
```

| Command | What It Does |
|---------|-------------|
| (none) | Full wiki dashboard: tree, counts, relationships, layers |
| `tree` | Full structure as navigable tree |
| `spine` | Spine detail — all 16 models, standards pages, maturity |
| `model <name>` | One model: key insights, member pages, related lessons |
| `domain <name>` | One domain: pages, types, relationship counts |
| `lessons` | All lessons by maturity category |
| `decisions` | All decisions with summaries and file paths |
| `search <query>` | Fuzzy search across all pages — returns title, summary, path |
| `refs "Title"` | Outbound + inbound relationships for a page |

```bash
python3 -m tools.view
python3 -m tools.view tree
python3 -m tools.view spine
python3 -m tools.view model "Claude Code"
python3 -m tools.view domain ai-agents
python3 -m tools.view lessons
python3 -m tools.view decisions
python3 -m tools.view search "context injection"
python3 -m tools.view refs "Model Registry"
```

Use `search` before creating a new page (overlap check). Use `refs` to see what depends on a page before moving or archiving it.

---

## 4. Sync (`tools.sync`)

WSL ↔ Windows sync daemon for Obsidian vault access.

```
python3 -m tools.sync [flags]
```

| Flag | Short | What It Does |
|------|-------|-------------|
| `--watch` | `-w` | Daemon mode: watch for changes, auto-sync |
| `--interval N` | `-i N` | Watch interval in seconds (default: 15) |
| `--reverse` | `-r` | Sync from target back to source |
| `--target PATH` | `-t PATH` | Override sync target path |
| `--status` | `-s` | Show sync config and last sync timestamp |
| `--json` | | JSON output |
| `--quiet` | `-q` | Minimal output |

```bash
python3 -m tools.sync                                    # one-shot: wiki/ → Windows vault
python3 -m tools.sync --watch                            # daemon mode (recommended)
python3 -m tools.sync --watch --interval 10             # faster polling
python3 -m tools.sync --reverse                         # Windows vault → wiki/
python3 -m tools.sync --status                          # check config + last sync
python3 -m tools.sync --target /mnt/c/Users/Name/Obsidian/Wiki/
```

Run `--watch` at the start of any Obsidian editing session. Run `--reverse` after editing in Obsidian directly. Deploy as a persistent service: `python3 -m tools.setup --services wiki-sync`.

---

## 5. MCP Server (`tools.mcp_server`)

21 tools registered in `.mcp.json` and auto-discovered by Claude Code.

Manual start (debugging only):
```bash
.venv/bin/python -m tools.mcp_server
```

### Pipeline Tools (17)

| Tool | What It Does |
|------|-------------|
| `wiki_status` | Page count, raw files, domain breakdown |
| `wiki_search` | Fuzzy search — returns paths + titles |
| `wiki_read_page` | Read a page by path — frontmatter + sections |
| `wiki_list_pages` | List pages, optionally filtered by domain |
| `wiki_post` | Run full post-ingestion chain |
| `wiki_fetch` | Fetch URLs into `raw/` |
| `wiki_fetch_topic` | Queue a research topic |
| `wiki_scan_project` | Scan local project, copy docs to `raw/` |
| `wiki_gaps` | Gap analysis (orphans, thin pages, weak domains) |
| `wiki_crossref` | Cross-reference analysis |
| `wiki_sync` | One-shot wiki → Windows sync |
| `wiki_mirror_to_notebooklm` | Push source URLs to NotebookLM notebook |
| `wiki_integrations` | Check integration status (Obsidian, NotebookLM) |
| `wiki_continue` | Resume mission: status → review → score → gaps |
| `wiki_evolve` | Evolution pipeline (modes: score, scaffold, dry-run, review, stale) |
| `wiki_backlog` | Backlog summary, optionally filtered by epic |
| `wiki_log` | Create a log entry in `wiki/log/` |

### Gateway Tools (4)

| Tool | Parameters | What It Does |
|------|-----------|-------------|
| `wiki_gateway_query` | `query_type`, `value` | Query methodology, models, chains, stages, fields, backlog, lessons, logs, pages |
| `wiki_gateway_template` | `page_type` | Get a page template by type |
| `wiki_gateway_contribute` | `contrib_type`, `title`, `content`, `domain` | Write-back: lesson, remark, or correction |
| `wiki_gateway_flow` | `step` (optional 1-8) | Goldilocks flow — 8-step routing |

**`wiki_gateway_query` — `query_type` values:**

| query_type | value required? | Returns |
|-----------|----------------|---------|
| `identity` | No | Project identity profile |
| `models` | No | All methodology models |
| `profiles` | No | All SDLC profiles |
| `model` | Yes (model name) | Model detail |
| `chain` | Yes (chain name) | Chain detail |
| `stage` | Yes (stage name) | Stage requirements |
| `field` | Yes (field name) | Frontmatter field explanation |
| `backlog` | No | Epic + task status |
| `lessons` | No | Lessons by maturity |
| `logs` | No | Recent log entries |
| `page` | Yes (page title) | Page metadata + summary |

---

## 6. Quality Tools

### Validate (`tools.validate`)

Schema validation: frontmatter fields, required values, type constraints.

```bash
python3 -m tools.validate                          # all wiki pages
python3 -m tools.validate wiki/domains/ai-agents/openfleet.md
python3 -m tools.validate wiki/domains/ai-agents/
python3 -m tools.validate --json
python3 -m tools.validate --schema /path/to/wiki-schema.yaml
```

---

### Lint (`tools.lint`)

Health checks: orphaned pages, missing relationships, empty summaries, broken wikilinks.

```bash
python3 -m tools.lint                          # human-readable summary (default)
python3 -m tools.lint --report                 # full JSON report
python3 -m tools.lint --summary                # summary mode
python3 -m tools.lint --fix                    # auto-fix issues where possible
python3 -m tools.lint /path/to/other/wiki/     # target a specific wiki directory
python3 -m tools.lint --config /path/to/quality-standards.yaml
```

---

### Stats (`tools.stats`)

Coverage and growth report: pages by type, domain, maturity; relationship density.

```bash
python3 -m tools.stats
python3 -m tools.stats --json
python3 -m tools.stats --wiki /path/to/wiki/
```

---

## 7. Export (`tools.export`)

Export filtered wiki pages to a sister project per a named export profile.

```bash
python3 -m tools.export openfleet        # export for openfleet
python3 -m tools.export aicp             # export for AICP
python3 -m tools.export methodology      # export methodology pages
python3 -m tools.export openfleet --dry  # dry run — preview without writing
python3 -m tools.export openfleet --wiki /path/to/wiki/
python3 -m tools.export openfleet --profiles /path/to/export-profiles.yaml
```

Export profiles defined in `wiki/config/export-profiles.yaml`. Each profile specifies domains, types, tags to include, and the output destination.

---

## 8. Setup (`tools.setup`)

Environment bootstrap and cross-platform setup.

```bash
python3 -m tools.setup                         # full setup
python3 -m tools.setup --check                 # check environment (no changes)
python3 -m tools.setup --deps                  # install dependencies via uv only
python3 -m tools.setup --obsidian-config       # configure Obsidian vault settings
python3 -m tools.setup --services              # list available systemd services
python3 -m tools.setup --services wiki-sync    # deploy wiki-sync service
python3 -m tools.setup --services wiki-evolve  # deploy wiki-evolve service
python3 -m tools.setup --services wiki-sync --target /mnt/c/Users/Name/Obsidian/Wiki/
```

---

## 9. Evolution Pipeline (`tools.evolve`)

Score and scaffold the knowledge evolution ladder (L0 raw → L6 decisions).

```
python3 -m tools.evolve [mode] [flags]
```

### Modes

| Mode | What It Does |
|------|-------------|
| `score` (default) | Rank candidates by 6 signals |
| `scaffold` | Scaffold top N candidates as lesson/pattern/decision pages |
| `dry-run` | Show what scaffold would do without writing |
| `auto` | Score → scaffold → generate content via LLM |
| `execute` | Process the scaffold queue |
| `review` | Check maturity state of seed pages |
| `stale` | Find evolved pages whose sources have been updated |

```bash
python3 -m tools.evolve score               # rank top 10
python3 -m tools.evolve score --top 20
python3 -m tools.evolve score --type lesson
python3 -m tools.evolve score --type pattern
python3 -m tools.evolve score --type decision
python3 -m tools.evolve score --domain ai-agents
python3 -m tools.evolve scaffold --top 5
python3 -m tools.evolve dry-run --top 10
python3 -m tools.evolve auto --backend claude-code
python3 -m tools.evolve auto --backend openai --top 5
python3 -m tools.evolve review
python3 -m tools.evolve stale
python3 -m tools.evolve execute --clear
python3 -m tools.evolve score --json
```

### Flags

| Flag | Short | Default | What It Does |
|------|-------|---------|-------------|
| `--top N` | `-n N` | 10 | Number of candidates to show/process |
| `--type TYPE` | `-t TYPE` | all | Filter: `lesson`, `pattern`, `decision` |
| `--domain D` | `-d D` | all | Filter by domain |
| `--backend B` | `-b B` | `claude-code` | LLM backend for auto: `claude-code`, `openai`, `aicp` |
| `--clear` | | False | Clear queue after execute |
| `--quiet` | `-q` | False | Suppress verbose output |
| `--json` | | False | JSON output |

### The 6 Evolution Signals

Score is a weighted sum of: `cross_source_convergence` (same insight in ≥2 independent sources), `directive_alignment` (matches operator directives), `link_density` (many pages reference this concept), `recency` (sources recently updated), `open_questions` (unresolved gaps), `orphan_penalty` (penalizes pages with no inbound links).

### Maturity Folders

New scaffolds land in `00_inbox`. Promote manually as evidence accumulates.

| Layer | Lessons | Patterns | Decisions |
|-------|---------|---------|----------|
| Inbox | `lessons/00_inbox/` | `patterns/00_inbox/` | `decisions/00_inbox/` |
| Drafts | `lessons/01_drafts/` | `patterns/01_drafts/` | `decisions/01_drafts/` |
| Synthesized | `lessons/02_synthesized/` | `patterns/02_synthesized/` | `decisions/02_validated/` |
| Validated | `lessons/03_validated/` | `patterns/03_validated/` | `decisions/03_principles/` |
| Principles | `lessons/04_principles/` | `patterns/04_principles/` | — |

Promote lessons when ≥3 evidence items. Promote patterns when ≥2 instances. Run `pipeline post` after any promotion.

---

## 10. Common Workflows

### Ingest a new source
```bash
python3 -m tools.pipeline run https://example.com/article   # fetch + post in one step
# or separately:
python3 -m tools.pipeline fetch URL && python3 -m tools.pipeline post
```

### Add a new wiki page
```bash
python3 -m tools.pipeline scaffold concept "My New Concept"  # scaffold
# edit the file
python3 -m tools.pipeline post                               # validate + index
```

### Start a session
```bash
python3 -m tools.pipeline chain continue    # status → review → score → gaps
```

### Weekly review
```bash
python3 -m tools.pipeline chain review      # post → evolve review → gaps → crossref
```

### Promote a lesson
```bash
python3 -m tools.evolve review              # check maturity state
# manually move file to next maturity folder, update maturity field
python3 -m tools.pipeline post              # validate
```

### Query the wiki from another project
```bash
python3 -m tools.gateway \
  --wiki-root /home/jfortin/devops-solutions-research-wiki \
  query --stage document --domain typescript
```

### Ingest a GitHub repository
```bash
python3 -m tools.pipeline fetch https://github.com/owner/repo   # deep fetch is automatic
# or scan a local clone:
python3 -m tools.pipeline scan /home/jfortin/owner/repo/
```

### Check for page overlap before creating
```bash
python3 -m tools.view search "your topic"
python3 -m tools.pipeline gaps              # see what's explicitly missing
```

### Sync wiki to Obsidian
```bash
python3 -m tools.sync --watch --interval 15  # continuous sync during editing session
```

### Export to a sister project
```bash
python3 -m tools.export openfleet --dry    # preview
python3 -m tools.export openfleet          # execute
```

---

## 11. Reference: Page Types and Frontmatter

### Page Types (for `scaffold` and `gateway template`)

| Type | Use When |
|------|---------|
| `concept` | Core domain concept (most common) |
| `source-synthesis` | Processed raw source → wiki knowledge |
| `comparison` | Side-by-side analysis of ≥2 things |
| `reference` | Lookup table, command reference, schema |
| `deep-dive` | Exhaustive treatment of one complex topic |
| `lesson` | Distilled insight with ≥3 evidence items |
| `pattern` | Reusable solution with ≥2 instances |
| `decision` | Resolved choice with alternatives + rationale |
| `principle` | Elevated validated lesson |
| `domain-overview` | Entry point for a domain |
| `epic` | Strategic capability (weeks of work) |
| `module` | Coherent subsystem (days of work) |
| `task` | Single-session atomic work item |
| `note` | Log entries, directives, session notes |
| `evolution` | Meta-page about knowledge evolution |
| `learning-path` | Sequenced reading guide |

### Required Frontmatter Fields

```yaml
title:      # Must match the # Heading exactly
type:       # Page type from list above
domain:     # Must match the folder path segment
status:     # draft | in-progress | synthesized | validated
confidence: # low | medium | high
created:    # YYYY-MM-DD
updated:    # YYYY-MM-DD
sources:    # List of source references
tags:       # List of tags
```

Full schema: `wiki/config/wiki-schema.yaml`

---

## 12. Tool Locations

| Tool | Entry Point | Source File |
|------|------------|-------------|
| Pipeline | `python3 -m tools.pipeline` | `tools/pipeline.py` |
| Gateway | `python3 -m tools.gateway` | `tools/gateway.py` |
| View | `python3 -m tools.view` | `tools/view.py` |
| Sync | `python3 -m tools.sync` | `tools/sync.py` |
| Validate | `python3 -m tools.validate` | `tools/validate.py` |
| Lint | `python3 -m tools.lint` | `tools/lint.py` |
| Stats | `python3 -m tools.stats` | `tools/stats.py` |
| Export | `python3 -m tools.export` | `tools/export.py` |
| Evolve | `python3 -m tools.evolve` | `tools/evolve.py` |
| Setup | `python3 -m tools.setup` | `tools/setup.py` |
| Manifest | `python3 -m tools.manifest` | `tools/manifest.py` |
| MCP Server | `.venv/bin/python -m tools.mcp_server` | `tools/mcp_server.py` |

All tools require the project virtualenv. Activate: `source .venv/bin/activate`, or prefix: `.venv/bin/python3 -m tools.X`.

---

## Related Wiki Pages

- `wiki/spine/references/gateway-tools-reference.md` — gateway command details + dual-scope guide
- `wiki/spine/references/model-registry.md` — all 16 models, methodology entry point
- `wiki/spine/references/methodology-system-map.md` — component locations across the wiki
- `wiki/config/wiki-schema.yaml` — full page schema with valid values
- `wiki/config/methodology.yaml` — models, stages, artifact chains
- `wiki/config/export-profiles.yaml` — sister project export definitions
- `wiki/config/quality-standards.yaml` — lint thresholds and health check definitions
