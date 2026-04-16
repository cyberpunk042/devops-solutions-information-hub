---
title: E023 — Gateway-Wide Output Contract Audit
aliases:
  - "E023 — Gateway-Wide Output Contract Audit"
  - "E023 — Gateway Output Audit"
type: epic
domain: backlog
status: draft
priority: P2
task_type: epic
current_stage: document
readiness: 5
progress: 0
stages_completed: []
artifacts: []
confidence: high
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: milestone
    type: file
    file: wiki/backlog/milestones/second-brain-complete-system-v2-0.md
  - id: e022-predecessor
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e022-context-aware-gateway-orientation-and-routing.md
  - id: output-contract
    type: wiki
    file: wiki/spine/standards/gateway-output-contract.md
tags: [epic, gateway, audit, contract-compliance, v2, milestone-v2, p2, follow-on, stub]
---

# E023 — Gateway-Wide Output Contract Audit

## Summary

Follow-on to E022. E022 ships the [[gateway-output-contract|Gateway Output Contract]] and applies it to two subcommands (`orient` + `what-do-i-need`). E023 audits every remaining gateway subcommand against the contract's 5 rules, produces a compliance matrix, and ships upgrades per subcommand in priority order. This is explicitly a follow-on to preserve E022's scope discipline — smaller modules ship faster. This epic is a **stub**: scope is captured, work begins after E022 lands and real usage data informs priorities.

## Why This Is Follow-On, Not Part of E022

The operator's `+1 × 2` framing scoped E022 to exactly two changes (new `orient` + upgraded `what-do-i-need`) plus the contract. Auditing the full gateway in one epic would have violated the brain's volume-not-quality rule: one scoped epic with complete execution > one sprawling epic with flim traces across many subcommands. E023 exists so the follow-on is not forgotten, not to be activated in parallel.

## Goals

- Complete compliance matrix for every gateway subcommand (current state vs. each of the 5 contract rules)
- Prioritized upgrade list: critical violations (Rule 2 declared-over-detected, Rule 5 closing-next-move) before polish
- Each subcommand either passes all 5 rules OR has a logged documented-deferral with reason
- Validator for the mechanically checkable rules (3, 4, 5) integrated into `pipeline post` if feasible (open question)

## Done When

- [ ] Compliance matrix exists as a wiki page or inline in the gateway reference, listing every current subcommand × each of the 5 rules
- [ ] Upgrades scoped as modules (one per subcommand that needs work)
- [ ] All P2+ subcommands pass contract; P3/rarely-used subcommands may carry documented-deferrals with reason
- [ ] `pipeline post` optionally extended with mechanical-rules validator (Rules 3/4/5) — contingent on M003 design call
- [ ] No regression in E022's two subcommands after the full audit

## Scope — Subcommands to Audit

Provisional list based on current gateway. Confirm by reading `tools/gateway.py` when epic activates.

> [!info] Subcommand audit scope
>
> | Subcommand | Known / suspected violations | Priority |
> |------------|----------------------------|----------|
> | `status` | Probably compliant (short, single-purpose) | P3 |
> | `query` (many flags) | Rule 1 risk — 8+ flags = multiple questions? Rule 3 risk for some dimensions | P2 |
> | `template` | Probably compliant | P3 |
> | `config` | Unknown until audited | P3 |
> | `move` | Probably compliant (single-action) | P3 |
> | `archive` | Probably compliant | P3 |
> | `backup` | Probably compliant | P3 |
> | `contribute` | Rule 5 check — does it close with next-move? | P2 |
> | `navigate` | Rule 3 violation — can flood with full tree, no ceiling | P1 (critical) |
> | `flow` | Rule 2 violation (already documented anti-pattern — heuristic override of declaration) + Rule 5 risk | P1 (critical) |
> | `timeline` | Rule 3 risk — `--scope all` can emit hundreds of events; Rule 4 if large | P2 |
> | `compliance` / `docs` / other | Audit when epic activates | P3 |
>
> **Critical violations** (P1) are candidates for immediate upgrade alongside E022. Everything else can batch.

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Model** | refactor (change behavior of existing subcommands, no new features) |
> | **Quality tier** | Pyramid (audit → fix, not Skyscraper's full SFIF) |
> | **Estimated modules** | 3 (audit, P1 fixes, P2 fixes) |
> | **Estimated tasks** | 8-15 depending on audit findings |
> | **Dependencies** | E022 MUST ship first — the contract and two exemplar subcommands inform what "good" looks like during audit |
> | **Blocker for activation** | Wait for ≥1 real usage cycle of E022's upgraded subcommands — so audit learns from operational feedback, not just spec |

## Module Breakdown (provisional)

### M001 — Audit and Compliance Matrix

Read `tools/gateway.py` full source; for each subcommand, produce a 5-column compliance row. Output: a reference page or updated `gateway-tools-reference.md` section.

### M002 — Critical Fixes (P1)

Upgrade `navigate` (Rule 3 ceiling) and `flow` (Rule 2 declaration honoring, Rule 5 close). May or may not require design stage per subcommand.

### M003 — Secondary Fixes (P2)

Upgrade `query`, `contribute`, `timeline` based on audit findings. Group by related changes to batch testing.

### M004 — Optional Validator Integration

If mechanical rules (3, 4, 5) can be validated programmatically, add to `pipeline post` lint step. Design-stage call.

## Open Questions

> [!question] Should the audit produce a standing compliance dashboard?
> A `pipeline gateway-compliance` or similar command that runs the checkable rules against all subcommands and reports drift over time. Turns the contract from a point-in-time audit into continuous enforcement. Good idea but adds scope.

> [!question] What's the documented-deferral bar?
> Some subcommands (rarely-used, external-facing) may cost more to upgrade than they're worth. A documented-deferral with "reason: <X>, accepted risk: <Y>, revisit trigger: <Z>" preserves optionality without blocking E023 completion.

> [!question] Does the validator touch every invocation or sample?
> If it runs on every gateway call, there's overhead. If it samples, drift can hide. Design call when M004 activates.

## Dependencies

- **E022 (Context-Aware Gateway Orientation and Task Routing):** MUST ship first. The contract and exemplars exist only after E022 lands.
- **Real operational feedback** on E022's two subcommands. Activating E023 before any real usage would audit against theory; waiting lets evidence inform priorities.

## Handoff Context

> [!info] For activation later
>
> **When to activate:** After E022 ships and at least one full session has exercised both `orient` and `what-do-i-need` in real conditions. Lessons from that usage inform which rules need tightening in the contract before auditing the rest.
>
> **Where to start:** Read `tools/gateway.py` in full. For each `add_parser` call, produce a 5-rule compliance row. Output initial matrix in this epic's file or a dedicated reference page.
>
> **What would trigger descoping:** If the contract proves too strict in practice (too many false anti-pattern flags), the audit may reveal rule adjustments rather than subcommand fixes. That's fine — the contract evolves; E023 updates it accordingly.

## Relationships

- PART OF: [[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
- DEPENDS ON: [[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Task Routing]]
- BUILDS ON: [[gateway-output-contract|Gateway Output Contract — What Good Tool Output Looks Like]]
- RELATES TO: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]

## Backlinks

[[second-brain-complete-system-v2-0|Milestone — Second Brain Complete System — v2.0]]
[[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation and Task Routing]]
[[gateway-output-contract|Gateway Output Contract — What Good Tool Output Looks Like]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
