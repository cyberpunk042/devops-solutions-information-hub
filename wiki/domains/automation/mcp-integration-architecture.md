---
title: MCP Integration Architecture
aliases:
  - "MCP Integration Architecture"
type: concept
layer: 2
maturity: growing
domain: automation
status: synthesized
confidence: medium
created: 2026-04-08
updated: 2026-04-13
sources:
  - id: src-user-directive-integration
    type: notes
    file: raw/notes/2026-04-08-user-directive-integration-vision.md
    title: User Directive — Integration Vision & Service Architecture
    ingested: 2026-04-08
  - id: src-user-directive-ecosystem
    type: notes
    file: raw/notes/2026-04-08-user-directive-ecosystem-connections.md
    title: User Directive — Ecosystem Connections & Automation Vision
    ingested: 2026-04-08
tags: [mcp, model-context-protocol, integration, services, daemon, watcher, rsync, bidirectional-sync, claude-replaceable]
---

# MCP Integration Architecture

## Summary

The MCP Integration Architecture is the evolutionary target for the research wiki system — moving from CLI tools invoked by Claude Code to MCP servers that expose wiki operations as native tools in any Claude Code conversation. The user directive states: "By the end of all this you will do only what you absolutely need to be doing and you will even eventually be replaceable easily if needed." This means the system's intelligence lives in the tools, services, and MCP servers — not in Claude. Three MCP servers (wiki operations, NotebookLM, Obsidian), two service daemons (wiki watcher, WSL↔Windows rsync), and bidirectional sync with external systems. Claude focuses on reasoning, connections, questions, and standards — the mechanical work is offloaded to infrastructure.

> [!info] Integration Architecture Status
>
> | Component | Status | Tools/Details |
> |-----------|--------|--------------|
> | **Wiki MCP Server** | IMPLEMENTED | 17 tools: wiki_status, wiki_search, wiki_read_page, wiki_post, wiki_fetch, wiki_gaps, wiki_crossref, wiki_evolve, etc. |
> | **Wiki Watcher** | IMPLEMENTED | `python -m tools.watcher` — change detection + auto post-chain |
> | **WSL↔Windows Sync** | IMPLEMENTED | `python -m tools.sync` — bidirectional with Obsidian vault |
> | **NotebookLM MCP** | PLANNED | Wraps notebooklm-py: create notebooks, add sources, query, generate |
> | **Obsidian MCP** | PLANNED | Wraps Obsidian CLI: search, read, create, backlinks, sync |

## Key Insights

> [!warning] "Claude becomes replaceable" — the architectural north star
> The persistent intelligence is the wiki, tools, services, and MCP servers — not Claude. Any LLM that can call MCP tools can operate the system. Claude's unique value is reasoning quality, but the operational mechanics are LLM-agnostic. The user directive: "By the end of all this you will do only what you absolutely need to be doing and you will even eventually be replaceable easily if needed."

**Bidirectional sync vision.** Detect user adds note in NotebookLM → ingest. Detect user edits in Obsidian → process. Detect wiki changes → sync to Obsidian + notify. The system reacts to changes from any entry point.

**MCP tool composition in conversations.** "Ingest these 5 URLs, then cross-reference, then export to openfleet" becomes a sequence of MCP tool calls. Group calls run in parallel (subagents each calling MCP tools). Tree operations branch and merge.

**Entry point evolution.** Current: MCP servers + CLI tools + Claude Code conversation + service daemons. Target: add webhooks (external triggers) and scheduled tasks (cron-based research runs) for full autonomous operation.

## Deep Analysis

### MCP Server Designs

**Wiki MCP Server** (highest priority):
```
Tools:
  wiki_ingest(url_or_path, mode="smart")    → trigger ingestion pipeline
  wiki_query(question)                       → search wiki, return cited answer
  wiki_lint()                                → run lint, return report
  wiki_validate()                            → run validation, return errors
  wiki_stats()                               → return current wiki statistics
  wiki_export(target="openfleet")            → export to sister project
  wiki_gaps()                                → identify research priorities
  wiki_manifest()                            → regenerate and return manifest
```

**NotebookLM MCP Server** (wraps notebooklm-py):
```
Tools:
  nlm_create_notebook(title)                 → create NotebookLM notebook
  nlm_add_source(notebook_id, url_or_path)   → add source to notebook
  nlm_ask(notebook_id, question)             → query sources
  nlm_generate(notebook_id, type="audio")    → generate artifact
  nlm_download(notebook_id, type, path)      → download artifact
  nlm_research(notebook_id, query)           → trigger web research
```

**Obsidian MCP Server** (wraps Obsidian CLI):
```
Tools:
  obs_search(query)                          → search vault
  obs_read(file)                             → read note
  obs_create(name, content, template)        → create note
  obs_backlinks(file)                        → get backlinks
  obs_orphans()                              → find orphan pages
  obs_properties(file, format="json")        → read/set frontmatter
  obs_sync()                                 → trigger rsync to Windows
```

### Service Architecture

```
┌─────────────────────────────────────────────────────┐
│  Claude Code / Any MCP Client                        │
│  (reasoning, connections, questions, standards)       │
└──────────┬────────────┬────────────┬────────────────┘
           │            │            │
    ┌──────▼──────┐ ┌───▼────┐ ┌────▼─────┐
    │  Wiki MCP   │ │NLM MCP │ │ Obs MCP  │
    │  (port TBD) │ │(port)  │ │ (port)   │
    └──────┬──────┘ └───┬────┘ └────┬─────┘
           │            │            │
    ┌──────▼──────────────────────────▼──────┐
    │  tools/*.py    notebooklm-py  obsidian │
    │  (Python)      (Python/CLI)   (CLI)    │
    └──────┬──────────────────────────┬──────┘
           │                          │
    ┌──────▼──────┐          ┌───────▼───────┐
    │ Wiki Watcher │          │ rsync Daemon  │
    │ (inotify)    │          │ (WSL→Windows) │
    └──────────────┘          └───────────────┘
```

### Implementation Priority

> [!success] Completed
> 1. **Wiki MCP** — 17 tools, registered in `.mcp.json`, auto-discovered by Claude Code
> 2. **rsync daemon** — `tools/sync.py` with `--watch` mode, systemd service via `tools/setup`
> 3. **Wiki watcher** — `tools/watcher.py` with change detection + auto post-chain

> [!info] Remaining MCP Integrations
> 4. **NotebookLM MCP** (unlocks: source mirroring, cross-validation via notebooklm-py)
> 5. **Obsidian MCP** (unlocks: bidirectional vault management via Obsidian CLI)

## Open Questions

- How to handle MCP server authentication for multi-user scenarios? (Requires: external research on MCP auth patterns; not covered in existing wiki pages)
- Can one MCP server expose all three tool sets, or should they be separate servers? (Requires: external research on MCP server multi-namespace patterns; not covered in existing wiki pages)

### Answered Open Questions

> [!example]- What MCP framework to use?
> Python (the existing `tools/mcp_server.py` implementation) is the correct choice — all existing tooling is Python, the wiki MCP server is already implemented and proven with 17 tools. TypeScript MCP SDK only if NotebookLM or Obsidian integrations are TypeScript-native. The Decision: MCP vs CLI page establishes CLI+Skills as default for operational tooling; MCP is for external service bridges and tool discovery.

> [!example]- Watcher: inotify, polling, or git hooks?
> Resolved: polling for WSL2. inotify does not work reliably on /mnt/c paths. `tools/watcher.py` polls wiki/ on the Linux filesystem; `tools/sync.py` separately bridges to Windows. Git hooks only fire on git operations, not on file writes from Claude Code. The two-daemon architecture keeps change detection reliable across the WSL2 boundary.

> [!example]- Service daemon lifecycle on WSL2?
> Deploy as systemd user services via `python -m tools.setup --services wiki-sync` (or `wiki-watcher`). Writes to `~/.config/systemd/user/`, runs `systemctl enable`. Requires `[boot] systemd=true` in `/etc/wsl.conf` + `wsl --shutdown` restart. No manual systemctl commands — only reproducible setup scripts (IaC pattern).

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
- BUILDS ON: [[obsidian-cli|Obsidian CLI]]
- BUILDS ON: [[notebooklm-py-cli|notebooklm-py CLI]]
- BUILDS ON: [[claude-code|Claude Code]]
- ENABLES: [[research-pipeline-orchestration|Research Pipeline Orchestration]]
- RELATES TO: [[openfleet|OpenFleet]]
- RELATES TO: [[aicp|AICP]]
- RELATES TO: [[wiki-event-driven-automation|Wiki Event-Driven Automation]]

## Backlinks

[[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
[[obsidian-cli|Obsidian CLI]]
[[notebooklm-py-cli|notebooklm-py CLI]]
[[claude-code|Claude Code]]
[[research-pipeline-orchestration|Research Pipeline Orchestration]]
[[openfleet|OpenFleet]]
[[aicp|AICP]]
[[wiki-event-driven-automation|Wiki Event-Driven Automation]]
[[agent-orchestration-patterns|Agent Orchestration Patterns]]
[[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
[[context-aware-tool-loading|Context-Aware Tool Loading]]
[[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
[[obsidian-vs-notebooklm-as-knowledge-interface|Decision — Obsidian vs NotebookLM as Knowledge Interface]]
[[design-md-pattern|Design.md Pattern]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[gateway-centric-routing|Gateway-Centric Routing]]
[[harness-engineering|Harness Engineering]]
[[agent-orchestration-is-highest-connected-concept|Lesson — Agent Orchestration Is the Highest-Connected Concept in the Wiki]]
[[automation-is-bridge-between-knowledge-and-action|Lesson — Automation Is the Bridge Between Knowledge and Action]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[multi-channel-ai-agent-access|Multi-Channel AI Agent Access]]
[[openarms|OpenArms]]
[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]]
[[src-context-mode|Synthesis — Context Mode — MCP Sandbox for Context Saving]]
[[src-playwright-mcp-visual-testing|Synthesis — Playwright MCP for Visual Development Testing]]
[[wsl2-development-patterns|WSL2 Development Patterns]]
