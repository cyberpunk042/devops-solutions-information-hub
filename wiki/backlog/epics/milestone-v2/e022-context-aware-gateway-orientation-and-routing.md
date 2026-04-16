---
title: E022 — Context-Aware Gateway Orientation and Task Routing
aliases:
  - "E022 — Context-Aware Gateway Orientation and Task Routing"
  - "E022 — Context-Aware Gateway Orientation and Routing"
type: epic
domain: backlog
status: active
priority: P1
task_type: epic
current_stage: implement
readiness: 80
progress: 75
stages_completed:
  - "document"
  - "design"
  - "scaffold"
artifacts:
  - "raw/notes/2026-04-15-directive-knowledge-project-methodology-rework.md"
  - "wiki/spine/standards/gateway-output-contract.md"
  - "wiki/backlog/epics/milestone-v2/e023-gateway-wide-output-contract-audit.md"
  - "wiki/backlog/modules/e022-m002-gateway-orient-subcommand.md"
  - "wiki/backlog/modules/e022-m003-what-do-i-need-upgrade.md"
  - "tools/common.py"
  - "tools/gateway.py"
  - "tools/mcp_server.py"
  - "CLAUDE.md"
confidence: high
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: milestone
    type: file
    file: wiki/backlog/milestones/second-brain-complete-system-v2-0.md
  - id: operator-directive-rework
    type: directive
    file: raw/notes/2026-04-15-directive-knowledge-project-methodology-rework.md
  - id: output-contract
    type: wiki
    file: wiki/spine/standards/gateway-output-contract.md
tags: [epic, gateway, orientation, context-aware, knowledge-project, v2, milestone-v2, p1, srp, proto-programming]
---

# E022 — Context-Aware Gateway Orientation and Task Routing

## Summary

Fix the post-compaction onboarding gap: the current gateway is app-project-shaped, and a fresh agent inside the brain (the knowledge project itself) gets routed to task-picking output when it needs orientation first. This epic adds a new `gateway orient` subcommand for orientation-before-routing, upgrades `gateway what-do-i-need` to be context-aware (brain / sister / external + fresh / task-bound / returning), codifies the [[gateway-output-contract|Gateway Output Contract]] as a spine standard every subcommand inherits, and exposes both subcommands as MCP tools. The broader gateway audit (applying the contract to remaining subcommands) is deferred to a follow-on epic (E023).

## Operator Directive

> "Why was it not clearer after the context compaction the way we work in this project? we are going to have to rework this. maybe we have mainly a path for the app projects and not made for the knowledge project and even then, maybe its only a skaffold what we have for app projects right now and we need to evolve it all."

> "Yes you do it smart, if you are from second-brain its logical that the second-brain is default select but somtimes you can have mutliple entrypoint to make sure to respect SRP. because remember maybe I did not just ask +1 but + 1 * 2... so maybe orient is not the same as what-do-i-need? orient showing you something else that might lead you to what-do-i-need amongs other things and what-do-i-need for the second-brain show something appropriate, and never too large and making sure the AI know to read it whole."

Full verbatim: `raw/notes/2026-04-15-directive-knowledge-project-methodology-rework.md`

## Goals

- `gateway orient` ships as a new subcommand answering "who are you, where, what must you internalize" — with three context modes (brain / sister / external) and a freshness overlay
- `gateway what-do-i-need` upgraded to branch on context instead of returning one-size-fits-all task routing — brain-self mode returns knowledge-verb task types, not app-dev models
- Both subcommands honor the [[gateway-output-contract|Gateway Output Contract]] (5 rules: SRP, context-aware, size ceiling, read-whole marker, closing next-move)
- MCP exposure: `wiki_gateway_orient` tool; `wiki_gateway_what_do_i_need` kept but context-aware internally
- Contract becomes the standard subsequent subcommands are validated against (follow-on E023 audits the rest)

## Done When

- [ ] `wiki/spine/standards/gateway-output-contract.md` exists with ≥2 annotated exemplars and ≥3 anti-patterns (M001 — DONE when this epic logs it as artifact)
- [ ] `gateway orient` subcommand implemented in `tools/gateway.py`
- [ ] `gateway orient` output passes all 5 contract rules for brain-self / sister / external × fresh / task-bound (6 contexts)
- [ ] `gateway what-do-i-need` upgraded with context-aware branching — brain-self mode returns knowledge-verb task routing (NOT app-dev models)
- [ ] `gateway what-do-i-need` output passes all 5 contract rules across all contexts
- [ ] Declared > detected: both subcommands use heuristics only as sanity-check signals, never as overrides of declared values (no auto-detected phase/scale override of CLAUDE.md declarations)
- [ ] MCP tool `wiki_gateway_orient` exposed in `tools/mcp_server.py` with complete description
- [ ] MCP tool for upgraded `what-do-i-need` either added or existing tool's description updated to reflect context-aware behavior
- [ ] Session-state detection: fresh vs. task-bound vs. returning inferred from session-state file OR explicit flag (design-stage call in M002)
- [ ] Integration test: run `gateway orient` and `gateway what-do-i-need` in each of the 6 contexts; confirm output shape matches contract per context
- [ ] `wiki/spine/references/gateway-tools-reference.md` updated with both subcommands and contract pointer
- [ ] CLAUDE.md updated to reference `gateway orient` as the canonical first-step for fresh agents
- [ ] `pipeline post` passes with 0 errors, 0 lint issues, 0 orphan relationships
- [ ] Follow-on epic E023 stub created covering gateway-wide audit against the contract (M005)

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | feature-development (full 5 stages) |
> | **Quality tier** | Skyscraper |
> | **Estimated modules** | 5 (contract, orient, what-do-i-need upgrade, MCP exposure, audit-epic stub) |
> | **Estimated tasks** | 12-15 |
> | **Dependencies** | E015 (Gateway Tools Completion — this extends the gateway with new subcommand + contract) · the `methodology-fundamentals` learning path (orient points to it) |
> | **Follow-on** | E023 — Gateway-Wide Output Contract Audit (document-stage only in this epic; full work deferred) |
> | **Related epic (not dependency)** | E024 — Knowledge-Verbs Methodology Model (separate data-layer epic; what-do-i-need brain-mode routes to its verbs once ready) |

## Module Breakdown

### M001 — Gateway Output Contract (spine standard)

| Task | What | Stage |
|------|------|-------|
| T-E022-01 | Draft `wiki/spine/standards/gateway-output-contract.md` with 5 rules, 3 contexts, 2 annotated exemplars, 3 anti-patterns | document (DONE) |
| T-E022-02 | Cross-link contract into methodology-system-map and model-mcp-cli-integration | implement |
| T-E022-03 | Add contract to Per-Type Standards table in `wiki/spine/_index.md` if standards-index references apply | implement |

**Status:** T-E022-01 completed alongside this epic's document-stage authoring (2026-04-15). M001 artifact exists as `wiki/spine/standards/gateway-output-contract.md`.

### M002 — `gateway orient` Subcommand

| Task | What | Stage |
|------|------|-------|
| T-E022-04 | Design context detection function (brain-self / sister / external × fresh / task-bound / returning) with declared > detected priority | design |
| T-E022-05 | Design session-state file format for freshness detection (or reuse existing pattern) | design |
| T-E022-06 | Scaffold `orient` subcommand in `tools/gateway.py` with argparse entry + context detector stub | scaffold |
| T-E022-07 | Implement the six output modes (3 locations × 2 primary freshness states, one path for returning = redirect to what-do-i-need) | implement |
| T-E022-08 | Verify each output mode passes all 5 contract rules via manual audit + integration test | test |

### M003 — `gateway what-do-i-need` Upgrade

| Task | What | Stage |
|------|------|-------|
| T-E022-09 | Design context branching for current what-do-i-need output; separate SRP violations (remove consumer-runtime + default-profile blocks into appropriate subcommands or conditional sections) | design |
| T-E022-10 | Scaffold context branches in what-do-i-need handler | scaffold |
| T-E022-11 | Implement brain-self branch returning knowledge-verb task types (depends on E024 naming or uses concept placeholders) | implement |
| T-E022-12 | Implement sister and external branches | implement |
| T-E022-13 | Honor declared > detected: remove heuristic overrides of CLAUDE.md declarations; heuristics become sanity-check warnings only | implement |
| T-E022-14 | Verify all 6 contexts pass 5 contract rules | test |

### M004 — MCP Exposure

| Task | What | Stage |
|------|------|-------|
| T-E022-15 | Add `wiki_gateway_orient` MCP tool to `tools/mcp_server.py` with complete description for autonomous invocation | implement |
| T-E022-16 | Update the existing MCP tool wrapping `what-do-i-need` (if present) or add one, with description reflecting context-aware behavior | implement |
| T-E022-17 | Update `wiki/spine/references/gateway-tools-reference.md` and `.mcp.json` / tool registration | implement |

### M005 — E023 Follow-on Stub (document-stage only in this epic)

| Task | What | Stage |
|------|------|-------|
| T-E022-18 | Create `wiki/backlog/epics/milestone-v2/e023-gateway-wide-output-contract-audit.md` stub listing current subcommands and the audit plan against the contract | document |

E023 is NOT implemented here. Only its document-stage scaffold lives in this epic.

## Dependencies

- **E015 (Gateway Tools Completion):** This epic extends the gateway with a new subcommand + the output contract. E015 builds the engine; E022 adds context-awareness as the next capability layer.
- **`methodology-fundamentals` learning path:** `gateway orient` points to this as the canonical brain-self reading path for fresh agents. Must exist (it does).
- **[[consumer-runtime-signaling-via-mcp-config|Consumer Runtime Signaling decision]]:** Declared > detected is the inherited principle. Both subcommands honor `MCP_CLIENT_RUNTIME` as the authoritative consumer declaration.

## Open Questions

> [!question] Should `gateway what-do-i-need` auto-redirect to `orient` when it detects fresh+in-brain, or just emit a pointer?
> **Answer-before-ask leaning:** pointer. Explicit > implicit. Agent asking `what-do-i-need` while fresh gets a single-line "NEXT: gateway orient" at the top, not auto-redirect. Preserves consumer intent ("I chose this command for a reason"). Confirmed in M003 design stage.

> [!question] How is "fresh" reliably detected post-compaction?
> Compaction clears conversation state but not filesystem. A session-state file (updated on each gateway invocation) makes freshness inspectable — absence or staleness = fresh. Design-stage call in M002. Alternative: explicit `--fresh` flag the agent sets when it knows.

> [!question] Does `gateway flow` need similar treatment, or is its use case narrow enough to skip?
> `gateway flow` has the same heuristic-over-declaration violation (Rule 2 anti-pattern in the contract). It belongs in E023 (follow-on audit), not this epic's scope.

## Handoff Context

> [!info] For anyone picking this up in a fresh context
>
> **What this epic does:** Adds context-aware orientation and task routing to the gateway. Fresh agents inside the brain (post-compaction) get oriented before routed. Both subcommands honor a new output contract that every gateway subcommand will eventually inherit.
>
> **What this epic does NOT do:**
> - Audit every existing gateway subcommand against the contract (deferred to E023)
> - Build the knowledge-verbs methodology model that `what-do-i-need` brain-mode routes to (separate epic — E024)
> - Modify `tools/mcp_server.py` core — only adds new tool exposures
>
> **Current state:** Document stage. M001 artifact complete (the contract spine standard). M002-M005 awaiting design / scaffold approval.
>
> **Key files:**
> - `wiki/spine/standards/gateway-output-contract.md` — the contract (M001 artifact, DONE)
> - `tools/gateway.py` — where `orient` subcommand lands (M002)
> - `tools/mcp_server.py` — where MCP tool exposure lands (M004)
> - `raw/notes/2026-04-15-directive-knowledge-project-methodology-rework.md` — operator directive that drove this epic

## Relationships

- PART OF: [[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
- BUILDS ON: [[gateway-output-contract|Gateway Output Contract — What Good Tool Output Looks Like]]
- BUILDS ON: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- BUILDS ON: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
- BUILDS ON: [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
- DEPENDS ON: [[e015-gateway-tools-completion-all-requirements-implemented-with-mcp-integration|E015 — Gateway Tools Completion — All Requirements Implemented with MCP Integration]]
- RELATES TO: [[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]
- RELATES TO: [[consumer-runtime-signaling-via-mcp-config|Decision — Consumer Runtime Signaling via MCP Config]]
- RELATES TO: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]
- RELATES TO: [[model-context-engineering|Model — Context Engineering]]

## Backlinks

[[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
[[gateway-output-contract|Gateway Output Contract — What Good Tool Output Looks Like]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
[[e015-gateway-tools-completion-all-requirements-implemented-with-mcp-integration|E015 — Gateway Tools Completion — All Requirements Implemented with MCP Integration]]
[[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property]]
[[consumer-runtime-signaling-via-mcp-config|Decision — Consumer Runtime Signaling via MCP Config]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[model-context-engineering|Model — Context Engineering]]
[[e022-m002-gateway-orient-subcommand|E022-M002 — Gateway Orient Subcommand (Module Design)]]
[[e022-m003-what-do-i-need-upgrade|E022-M003 — Gateway What-Do-I-Need Upgrade (Module Design)]]
[[e023-gateway-wide-output-contract-audit|E023 — Gateway-Wide Output Contract Audit]]
