---
title: Gateway Tools Reference — Complete Command Documentation
aliases:
  - "Gateway Tools Reference — Complete Command Documentation"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: gateway-code
    type: file
    file: tools/gateway.py
tags: [reference, gateway, tools, cli, api, documentation]
---

# Gateway Tools Reference — Complete Command Documentation

> [!tip] Quick Start
>
> - **First time?** Just run `python3 -m tools.gateway` — guided entry shows common paths
> - **Know what you need?** See command table below
> - **From another project?** Add `--wiki-root /path/to/brain` to any command
> - **Want auto-recommendations?** `python3 -m tools.gateway what-do-i-need`

## Summary

Complete reference for the wiki gateway — the unified Python interface serving humans (CLI), AI agents (programmatic), and MCP connections (tool calls). 17 commands across 4 categories: discovery, queries, operations, and navigation. Works in dual-scope: targets the local wiki by default, or a remote second brain via `--wiki-root`.

## Reference Content

### Command Overview

> [!info] All Gateway Commands
>
> | Command | Category | What It Does |
> |---------|----------|-------------|
> | (no args) | Discovery | Guided entry with common paths per user type |
> | `what-do-i-need` | Discovery | Auto-detect identity → recommend chain → show first steps |
> | `status` | Discovery | Full project dashboard: identity + chain + models + navigation |
> | `navigate` | Navigation | Full knowledge tree with CLI commands at each branch |
> | `query --identity` | Query | Show project identity profile from CLAUDE.md |
> | `query --models` | Query | List all 9 methodology models with stages |
> | `query --model X --full-chain` | Query | Full artifact chain for a model |
> | `query --stage X [--domain Y]` | Query | Stage requirements + domain overrides. Auto-detects domain. |
> | `query --profiles` | Query | List all SDLC profiles (simplified/default/full) |
> | `query --profile X` | Query | Profile details: stages, models, readiness gate, enforcement |
> | `query --field X` | Query | Explain a frontmatter field (meaning, valid values, automation) |
> | `query --backlog` | Query | Backlog status: epics with readiness/progress, impediments |
> | `query --lessons` | Query | Lessons grouped by maturity folder (inbox through principles) |
> | `query --logs` | Query | Recent log entries |
> | `query --page "Title"` | Query | Page metadata + summary + relationship count |
> | `query --mapping` | Query | Location mapping for archived/moved pages |
> | `template X` | Operation | Get a page template by type |
> | `config X.Y` | Operation | Render a config section as markdown (e.g., methodology.models) |
> | `flow` | Navigation | Goldilocks flow — 8-step routing from identity to action |
> | `flow --step N` | Navigation | Detailed view of one Goldilocks step (1-8) |
> | `move "Title" --to dir/` | Operation | Move page + update ALL wikilink references across wiki |
> | `archive "Title"` | Operation | Archive page with location mapping |
> | `backup --target /path/` | Operation | Full wiki backup (timestamped) |
> | `factory-reset` | Operation | Reset wiki to clean template state (DRY RUN by default) |
> | `factory-reset --confirm` | Operation | Actually execute factory reset (creates backup first) |
> | `contribute --type X --title Y --content Z` | Operation | Agent write-back: lesson, remark, or correction |

### Global Flags

> [!info] Flags for Any Command
>
> | Flag | What It Does |
> |------|-------------|
> | `--wiki-root /path/` | Target a different project's wiki |
> | `--brain /path/` | Point to the second brain (auto-detected from sibling dirs if not specified) |
> | `--json` | JSON output (for query commands) |

### Auto-Detection

The gateway auto-detects what it CAN from the filesystem:

> [!abstract] What's Detectable vs What Must Be Declared
>
> | Dimension | Auto-Detectable? | How | Override |
> |-----------|-----------------|-----|---------|
> | Domain | Yes | package.json, pyproject.toml, main.tf, wiki/config/ | `--domain` flag or CLAUDE.md |
> | Scale | Yes | Source file count (excluding vendored deps) | Declare in CLAUDE.md |
> | Phase | Partially | CI + tests + Docker markers → heuristic | Declare in CLAUDE.md |
> | Second brain | Yes | Sibling dirs, wiki/config/methodology.yaml presence | `--brain` flag |
> | Execution mode | **No** | The harness decides its own version at runtime | Declare in CLAUDE.md |
> | PM level | **No** | Infrastructure may exist but not be active | Declare in CLAUDE.md |
> | Trust tier | **No** | Requires operational data or operator judgment | Declare in CLAUDE.md |

### Dual-Scope: How Two Perspectives Work

> [!abstract] Local vs Remote
>
> | Mode | When | How |
> |------|------|-----|
> | **Local (default)** | Working on the second brain itself | Just run `gateway` — auto-detects |
> | **Remote project → brain** | From another project, querying the brain | `gateway --wiki-root ~/brain query --models` |
> | **Remote brain → project** | From the brain, targeting a project | Not typical — use the project's own gateway |

The `--wiki-root` flag determines which wiki's pages you browse/modify.
The `--brain` flag determines where methodology configs, chains, templates come from.
When running ON the second brain, both are the same (auto-detected).

### MCP Server Integration

The gateway is also accessible via MCP tools registered in `.mcp.json`. These are task-oriented aggregations of CLI commands.

> [!info] Gateway MCP Tools
>
> | MCP Tool | What It Does | CLI Equivalent |
> |----------|-------------|---------------|
> | `wiki_gateway_query` | Query methodology, models, chains, stages, fields, backlog, lessons, logs, pages | `gateway query --{type} [value]` |
> | `wiki_gateway_template` | Get a page template by type | `gateway template <type>` |
> | `wiki_gateway_contribute` | Write back to the wiki (lesson, remark, correction) | `gateway contribute --type X ...` |
> | `wiki_gateway_flow` | Goldilocks flow step-by-step routing | `gateway flow [--step N]` |
>
> **Parameters for `wiki_gateway_query`:**
> - `query_type`: identity, models, chains, model, chain, stage, field, backlog, lessons, logs, page
> - `value`: required for model, chain, stage, field, page; optional otherwise
>
> These complement the 17 existing MCP tools (wiki_status, wiki_search, wiki_read_page, etc.) that cover pipeline operations. The gateway tools cover methodology and navigation.

### Auto-Detect Warnings

Every auto-detected value now includes a warning so agents and humans know what might be wrong:

```
DETECTED IDENTITY:
  domain:         knowledge  ⚠ Auto-detected. Override with --domain if wrong.
  phase:          mvp  ⚠ Auto-detected from CI/tests/Docker. Override in CLAUDE.md.
  scale:          micro (26 files)  ⚠ Auto-detected from file count.
  execution mode: solo
                  (no harness code found → solo is certain)
```

Auto-detection is a STARTING POINT, not an authority. The declared identity in CLAUDE.md always takes precedence. The warnings ensure agents don't silently use wrong defaults.

### How This Connects — Navigate From Here

> [!abstract] From This Reference → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The flow the gateway implements** | [[goldilocks-flow|Goldilocks Flow — From Identity to Action]] |
> | **The identity protocol** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **The integration chain** | [[second-brain-integration-chain|Operations Plan — Second Brain Integration Chain — Complete Walkthrough]] |
> | **The sub-super-model** | [[integration-ecosystem|Sub-Model — Integration and Ecosystem — Dual-Perspective and Feedback]] |
> | **The principle behind structure** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] |

## Relationships

- PART OF: [[integration-ecosystem|Sub-Model — Integration and Ecosystem — Dual-Perspective and Feedback]]
- IMPLEMENTS: [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
- RELATES TO: [[goldilocks-flow|Goldilocks Flow — From Identity to Action]]
- RELATES TO: [[methodology-system-map|Methodology System Map]]

## Backlinks

[[integration-ecosystem|Sub-Model — Integration and Ecosystem — Dual-Perspective and Feedback]]
[[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
[[goldilocks-flow|Goldilocks Flow — From Identity to Action]]
[[methodology-system-map|Methodology System Map]]
