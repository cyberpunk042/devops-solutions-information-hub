---
title: E015 — Gateway Tools Completion — All Requirements Implemented with MCP Integration
aliases:
  - "E015 — Gateway Tools Completion — All Requirements Implemented with MCP Integration"
  - "E015 — Gateway Tools Completion: All Requirements Implemented with MCP Integration"
type: epic
domain: backlog
status: active
priority: P1
task_type: epic
current_stage: implement
readiness: 70
progress: 65
stages_completed:
  - "scaffold"
artifacts:
  - "tools/gateway.py"
  - "wiki/backlog/epics/wiki-gateway-tools-unified-knowledge-interface.md"
confidence: high
created: 2026-04-12
updated: 2026-04-13
sources:
  - id: milestone
    type: file
    file: wiki/backlog/milestones/second-brain-complete-system-v2-0.md
  - id: mega-vision
    type: directive
    file: raw/notes/2026-04-12-mega-vision-directive.md
tags: [epic, gateway, tools, mcp, api, v2, milestone-v2]
---

# E015 — Gateway Tools Completion — All Requirements Implemented with MCP Integration
## Summary

Complete ALL 44 functional requirements for the gateway tools — the unified Python interface that serves humans (CLI), AI agents (programmatic), and MCP connections (tool calls) through ONE engine. Currently gateway.py has 10 commands + status + navigate + what-do-i-need. Missing: operational queries (backlog, logs, lessons), factory reset, full reference update on move, MCP server integration, auto-detect warnings, wiki documentation page. The gateway must work in BOTH directions: toward the second brain (querying methodology) AND toward the project's own wiki (applying, contributing).

## Operator Directive

> "we are going to need to add python script to make the Wiki LLM for internal and for external (other project to second-brain)"

> "It has to be something a human can use and an AI can use and we can connect other tools and MCPs to it."

> "the wiki tools should allow not only to work on the information-hub / second-brain but also on the projects internal wiki themselves when calling the second-brain tools"

> "auto-set on the most logical config from perspective of call by default unless specify and always warned about when auto-detected."

## Goals

- All FR-A1 through FR-A6 requirements fully implemented (see requirements spec)
- MCP server extended with gateway operations (17 existing tools + new gateway tools)
- Auto-detection with honest warnings for what can vs can't be detected
- Dual-scope fully working: `--wiki-root` for project wiki, `--brain` for second brain, auto-detect for both
- Gateway has its own wiki documentation page (reference type, in spine)
- Every command has `--help` that is genuinely helpful (not just argparse defaults)
- Smart defaults: `status` and `what-do-i-need` require ZERO flags

## Done When

- [ ] `gateway query --backlog` — shows backlog status (epics, tasks, readiness, impediments)
- [ ] `gateway query --lessons` — shows lessons by maturity level (inbox/synthesized/validated/principles)
- [ ] `gateway query --logs` — shows recent log entries
- [ ] `gateway move "Title" --to dir/` — moves page AND updates ALL wikilink references across wiki
- [ ] `gateway factory-reset --target dir/` — resets a wiki to clean template state (with confirmation prompt)
- [ ] MCP server exposes: `wiki_gateway_query`, `wiki_gateway_template`, `wiki_gateway_contribute`, `wiki_gateway_status`
- [ ] Every auto-detection includes warning: "Auto-detected: X. Override with --Y if wrong."
- [ ] `wiki/spine/references/gateway-tools-reference.md` — complete documentation page in wiki (reference type)
- [ ] `--brain` auto-detects second brain location from sibling directories
- [ ] `gateway --help` shows the guided entry (common paths), not raw argparse
- [ ] All 44 FR requirements from the requirements spec have status=done or documented-deferral

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | feature-development |
> | **Quality tier** | Skyscraper |
> | **Estimated modules** | 4 (missing queries, operations, MCP integration, documentation) |
> | **Estimated tasks** | 15-20 |
> | **Dependencies** | E014 (Goldilocks flow — gateway implements the flow's CLI side) |

## Module Breakdown

### M1: Missing Query Commands

| Task | Command | What It Returns |
|------|---------|----------------|
| T-E015-01 | `query --backlog` | Epic list with readiness/progress, task count, impediments |
| T-E015-02 | `query --lessons` | Lesson list grouped by maturity folder (00_inbox through 04_principles) |
| T-E015-03 | `query --logs` | Recent log entries (last N, filterable by note_type) |
| T-E015-04 | `query --page "Title"` | Full page metadata + summary + relationships (without reading the whole file) |

### M2: Missing Operations

| Task | Operation | What It Does |
|------|-----------|-------------|
| T-E015-05 | `move` — full ref update | After moving file, grep ALL wiki pages for old path/title and update references |
| T-E015-06 | `factory-reset` | Reset wiki to clean state: delete all content, keep templates + configs, rebuild indexes |
| T-E015-07 | Auto-detect warnings | Every auto-detected value includes warning message with override flag |
| T-E015-08 | `--brain` auto-detect | Search sibling dirs, parent dirs, common paths for second brain location |

### M3: MCP Server Integration

| Task | What |
|------|------|
| T-E015-09 | Add `wiki_gateway_query` MCP tool — wraps gateway query commands |
| T-E015-10 | Add `wiki_gateway_template` MCP tool — returns template by type |
| T-E015-11 | Add `wiki_gateway_contribute` MCP tool — wraps contribute command |
| T-E015-12 | Add `wiki_gateway_status` MCP tool — wraps status command |
| T-E015-13 | Add `wiki_gateway_flow` MCP tool — wraps Goldilocks flow (from E014) |
| T-E015-14 | Update `.mcp.json` with new tool registrations |

### M4: Documentation

| Task | What |
|------|------|
| T-E015-15 | Create `wiki/spine/references/gateway-tools-reference.md` — complete reference page for all gateway commands |
| T-E015-16 | Update CLAUDE.md gateway section with all new commands |
| T-E015-17 | Update methodology system map with gateway tools section |

## Dependencies

- **E014 (Goldilocks):** Gateway's `flow` command implements the Goldilocks flow. E014 designs the flow; E015 implements it in CLI.
- **Current gateway:** tools/gateway.py exists (800+ lines, 13 commands). This epic COMPLETES it.
- **MCP server:** tools/mcp_server.py exists (17 tools). This epic EXTENDS it.

## Open Questions

> [!question] ~~Should `factory-reset` be dangerous or safe?~~
> **RESOLVED:** Dangerous with explicit --confirm flag. Prints what will be deleted before acting.
> Dangerous: deletes all content immediately. Safe: requires `--confirm "I understand"` flag + creates backup first. Recommendation: safe — backup first, require confirmation, log the reset.

> [!question] ~~Should MCP tools be 1:1 with CLI commands or aggregated?~~
> **RESOLVED:** Aggregated by task. MCP tools are task-oriented (wiki_search, wiki_status). Already implemented with 17 tools.
> 1:1: each CLI command = one MCP tool (many tools). Aggregated: one `wiki_gateway` tool with action parameter (fewer tools, more complex schema). Recommendation: aggregated — one MCP tool per category (query, operate, contribute).

## Handoff Context

> [!info] For anyone picking this up in a fresh context:
>
> **What this epic does:** Completes the gateway tools to cover all 44 requirements from the FR spec, extends the MCP server, and creates documentation.
>
> **Current state:** tools/gateway.py has 800+ lines, 13 commands (query with 8 sub-options, template, config, move, archive, backup, contribute, status, navigate, what-do-i-need). Auto-detection works for domain/scale but doesn't warn. MCP server has 17 tools but none from gateway. No wiki documentation page.
>
> **Key files:**
> - `tools/gateway.py` — the gateway
> - `tools/mcp_server.py` — the MCP server to extend
> - `wiki/domains/cross-domain/second-brain-integration-requirements.md` — the 44 requirements with status
> - `wiki/backlog/epics/wiki-gateway-tools-unified-knowledge-interface.md` — the original gateway epic (predecessor)

## Relationships

- PART OF: [[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
- IMPLEMENTS: [[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]] (FR-A1 through FR-A6)
- DEPENDS ON: [[e014-goldilocks-navigable-system-identity-to-action-in-continuous-flow|E014 — Goldilocks Navigable System — Identity to Action in Continuous Flow]]
- BUILDS ON: [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
- FEEDS INTO: [[e016-integration-chain-proof-end-to-end-with-openarms|E016 — Integration Chain Proof — End to End with OpenArms]] (E016)
- FEEDS INTO: [[e018-global-standards-implementation-actual-adherence-not-just-reference|E018 — Global Standards Implementation — Actual Adherence Not Just Reference]] (E018)

## Backlinks

[[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
[[e014-goldilocks-navigable-system-identity-to-action-in-continuous-flow|E014 — Goldilocks Navigable System — Identity to Action in Continuous Flow]]
[[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
[[e016-integration-chain-proof-end-to-end-with-openarms|E016 — Integration Chain Proof — End to End with OpenArms]]
[[e018-global-standards-implementation-actual-adherence-not-just-reference|E018 — Global Standards Implementation — Actual Adherence Not Just Reference]]
[[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Task Routing]]
