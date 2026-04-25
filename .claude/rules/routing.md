# .claude/rules/routing.md — Operator Intent → Tool Routing

> Loaded on demand when work involves operator intent dispatch. CLAUDE.md has the summary; this file has the full table + the 30-tool MCP catalog + the CLI catalog + the mechanism-selection guide.

## Mechanism Selection (commands vs skills vs MCP vs CLI vs hooks)

| Mechanism | Determinism | Trigger | Use when |
|---|---|---|---|
| **Hook** | Logical (block + reason + remediation) | Tool-call lifecycle event | Structural enforcement: rule MUST hold at this point. Examples: corpus URL must route through pipeline, truncation must have a reason. |
| **Command** | **100% deterministic** | Operator types `/<name>` | Workflow with predictable steps, operator-driven, no auto-trigger needed. Examples: `/ingest`, `/continue`, `/log`. |
| **Skill** | **~70% deterministic** | Auto-triggered by description-match on operator prose | Workflow where auto-trigger is desirable but not load-bearing. Description quality determines trigger reliability. |
| **MCP tool** | Programmatic | AI invokes during reasoning | Discrete operations: search, fetch, read, post, contribute. Deferred load via ToolSearch. |
| **CLI** | Programmatic | AI runs via Bash | Shell-mediated operations, especially when chaining or piping needed. |

**Order of preference for the same operation:**
1. **MCP if available** — typed contract, no shell escaping, structured response
2. **CLI fallback** — when MCP missing, when chaining, when output piping needed
3. **Command/Skill** — for higher-level workflows that compose MCP/CLI calls
4. **Hook** — to enforce that 1-3 happen, not as primary mechanism

## Operator-Intent Routing Table (24 rows)

| # | Operator says... | First action | Primary tool | CLI fallback | Notes |
|---|---|---|---|---|---|
| 1 | `"ingest <url>"` / `"new ingestions:"` / URL list | Pipeline fetch → read raws full → author synthesis → pipeline post → crossref | `wiki_fetch` MCP | `.venv/bin/python -m tools.pipeline fetch <urls>` | Pipeline routes YouTube → transcript API, GitHub → README scrape, PDF → arxiv-aware. Hook denies WebFetch on corpus URLs. |
| 2 | `"continue"` / `"resume"` / `"where are we"` | Orient + state | `wiki_continue` MCP | `.venv/bin/python -m tools.gateway orient` | After compaction or fresh start. |
| 3 | `"status"` / `"what's next"` | State report | `wiki_status` MCP | `.venv/bin/python -m tools.pipeline status` | Plus stats and services. |
| 4 | `"log <directive>"` / verbatim quote | Log verbatim BEFORE acting | `wiki_log` MCP | Write `raw/notes/YYYY-MM-DD-<slug>.md` | AGENTS.md Hard Rule #3. |
| 5 | `"gaps"` / `"what's missing"` | Gap analysis | `wiki_gaps` MCP | `.venv/bin/python -m tools.pipeline gaps` | |
| 6 | `"search wiki for X"` | Wiki search | `wiki_search` MCP | `.venv/bin/python -m tools.view search "X"` | |
| 7 | `"show me <page>"` / `"read X"` | Read specific page | `wiki_read_page` MCP | Read tool on `wiki/` path | |
| 8 | `"promote"` / `"evolve"` / `"what's ready"` | Evolution pipeline | `wiki_evolve` MCP | `.venv/bin/python -m tools.pipeline evolve --score` | |
| 9 | `"scan project X"` | Sister-project scan | `wiki_scan_project` MCP | `.venv/bin/python -m tools.pipeline scan <path>` | |
| 10 | `"build a model"` / `"review model"` | Model workflow | — | Read `.claude/commands/build-model.md` | Operator-invoked slash command. |
| 11 | `"health check"` | Health score | `wiki_gateway_health` MCP | `.venv/bin/python -m tools.gateway health` | |
| 12 | `"validate"` / wiki change committed | Run post-chain (MANDATORY after wiki changes) | `wiki_post` MCP | `.venv/bin/python -m tools.pipeline post` | AGENTS.md Hard Rule #6. |
| 13 | `"find connections"` / `"crossref"` | Cross-reference | `wiki_crossref` MCP | `.venv/bin/python -m tools.pipeline crossref` | |
| 14 | `"contribute lesson"` / `"remark"` / `"correction"` | Contribute back | `wiki_gateway_contribute` MCP | `.venv/bin/python -m tools.gateway contribute --type ... --title ... --content ...` | Lands in 00_inbox or log/. |
| 15 | `"show backlog"` / `"tasks"` | Backlog state | `wiki_backlog` MCP | `.venv/bin/python -m tools.pipeline backlog` | |
| 16 | `"flow"` / `"guide me"` | Goldilocks step-by-step | `wiki_gateway_flow` MCP | `.venv/bin/python -m tools.gateway flow [--step N]` | |
| 17 | `"compliance check"` | Adoption tier + gaps | `wiki_gateway_compliance` MCP | `.venv/bin/python -m tools.gateway compliance` | |
| 18 | `"timeline"` / `"recent activity"` | Cross-project temporal | `wiki_gateway_timeline` MCP | `.venv/bin/python -m tools.gateway timeline` | |
| 19 | `"template for X"` | Page template | `wiki_gateway_template` MCP | `.venv/bin/python -m tools.gateway template <type>` | |
| 20 | `"docs lookup"` (README/AGENTS/CLAUDE/TOOLS) | Root docs | `wiki_gateway_docs` MCP | — | |
| 21 | `"sync"` | Obsidian sync | `wiki_sync` MCP | `.venv/bin/python -m tools.sync` | |
| 22 | `"mirror to NotebookLM"` | NotebookLM | `wiki_mirror_to_notebooklm` MCP | — | |
| 23 | `"methodology guidance"` / `"what process"` | Methodology | `wiki_methodology_guide` MCP | `.venv/bin/python -m tools.gateway query --model <name>` | |
| 24 | `"check provider pricing"` | Pricing snapshot | — | `.venv/bin/python -m tools.pipeline provider-check` | |
| 25 | `"scaffold a page of type X"` | Template scaffold | `wiki_gateway_template` MCP | `.venv/bin/python -m tools.pipeline scaffold <type> "<title>"` | |

## MCP Tool Catalog (30 tools, deferred — load via ToolSearch when needed)

### Gateway (9)
- `wiki_gateway_query` — query methodology, stages, models, fields, chains
- `wiki_gateway_orient` — context-aware orientation (who/where/what to internalize)
- `wiki_gateway_flow` — Goldilocks step-by-step routing from identity to action
- `wiki_gateway_health` — composite methodology+quality health score
- `wiki_gateway_compliance` — super-model adoption tier + gaps
- `wiki_gateway_template` — get a page template
- `wiki_gateway_timeline` — cross-project temporal view
- `wiki_gateway_contribute` — contribute lesson/remark/correction back to second brain
- `wiki_gateway_docs` — root-level docs lookup (README, AGENTS, CLAUDE, etc.)

### Ingestion (4)
- `wiki_fetch` — fetch a URL into raw/ (handles YouTube transcripts, GitHub READMEs, PDFs, web)
- `wiki_fetch_topic` — search-and-fetch by topic
- `wiki_post` — run post-ingestion 6-step chain (index → manifest → validate → wikilinks → lint)
- `wiki_crossref` — find new connections across pages

### Knowledge (8)
- `wiki_search` — search wiki content
- `wiki_read_page` — read a specific page by title or path
- `wiki_list_pages` — enumerate pages by domain/type
- `wiki_pages` — pages metadata
- `wiki_backlog` — backlog status (epics, modules, tasks, readiness)
- `wiki_gaps` — gap analysis with recommendations
- `wiki_log` — add log entry to wiki/log/ (verbatim directives, session logs, completion notes)
- `wiki_continue` — resume mission (diagnostics → state → options)

### Maintenance (6)
- `wiki_evolve` — knowledge evolution pipeline (score → scaffold → generate → review)
- `wiki_scan_project` — scan a sister project for ingestible content
- `wiki_sister_project` — sister-project ops
- `wiki_mirror_to_notebooklm` — NotebookLM source sync
- `wiki_integrations` — integrations management
- `wiki_sync` — Obsidian sync ops

### Status / meta (3)
- `wiki_status` — wiki stats
- `wiki_methodology_guide` — methodology guidance
- `wiki_root` — wiki root info

## CLI Catalog (canonical: `.venv/bin/python -m <module>`)

### `tools.pipeline` (orchestration)
`post` (6-step validation chain — MANDATORY after wiki changes) · `fetch URL [URL...]` · `fetch --batch FILE` · `fetch --topic QUERY` · `scan PATH` · `status` · `run URL [URL...]` (fetch + post-chain) · `chain <name>` · `chain --list` · `gaps` · `crossref` · `scaffold <type> <title>` · `evolve --score / --scaffold / --review / --auto / --stale` · `backlog` · `provider-check` · `provider-check --health`

### `tools.gateway` (knowledge interface)
`orient` (--orient-as / --fresh / --format) · `what-do-i-need` · `flow` (--step N) · `query` (--stage / --model / --field / --chain / --profile / --identity / --backlog / --logs / --page / --docs) · `template <type>` · `health` (--verbose) · `compliance` · `status` · `navigate` · `timeline` (--scope / --since / --until / --type / --group-by / --epic / --path) · `contribute --type --title --content` · `move <title> --to <dir>` · `archive <title>` · `backup --target <dir>`

### Other modules
- `tools.view` — dashboard / spine / model / search / refs / domains
- `tools.stats` — detailed stats (types, domains, layers, maturity)
- `tools.setup` — `--services` / `--deps` / `--connect <project>`
- `tools.lint` — lint checks (--report)
- `tools.validate` — schema validation
- `tools.evolve` — evolution operations
- `tools.export` — export profiles
- `tools.manifest` — manifest regen
- `tools.provider_check` — provider pricing health

## Cross-references

- Hook architecture (deterministic enforcement of routing): [.claude/rules/hook-architecture.md](.claude/rules/hook-architecture.md)
- Ingestion-specific routing detail: [.claude/rules/ingestion.md](.claude/rules/ingestion.md)
- Methodology stage/model selection: [.claude/rules/methodology.md](.claude/rules/methodology.md)
- This project IS the second brain (self-reference): [.claude/rules/self-reference.md](.claude/rules/self-reference.md)
- Operator-invoked commands: `.claude/commands/`
- Full gateway reference: [wiki/spine/references/gateway-tools-reference.md](wiki/spine/references/gateway-tools-reference.md)
