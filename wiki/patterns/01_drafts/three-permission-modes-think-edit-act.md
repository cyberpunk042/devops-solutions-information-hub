---
title: "Three Permission Modes (Think / Edit / Act) — Operator-Selected AI Authority Tiers"
aliases:
  - "Three Permission Modes (Think / Edit / Act) — Operator-Selected AI Authority Tiers"
  - "Three Permission Modes"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: seed
derived_from:
  - model-quality-failure-prevention
  - model-claude-code
instances:
  - page: "AICP CLAUDE.md + AGENTS.md"
    context: "Three modes named and enforced: Think (read/analyze/plan, no edits, no commands), Edit (modify files in scope, produce patches/diffs), Act (run commands, workflows, tools — highest authority). Selected per-session by operator."
  - page: "AICP profiles `force_cloud_modes`"
    context: "Per-profile setting routing different modes to different backends. Default profile routes Edit + Act to Claude regardless of local-first policy — mode IS a routing dimension."
  - page: "AICP guardrails (aicp/guardrails/)"
    context: "Mode enforced server-side: Think mode rejects Write/Edit tool invocations regardless of model; Edit mode rejects out-of-scope writes; Act mode applies command allowlist."
  - page: "Claude Code's Plan Mode"
    context: "Anthropic's Claude Code has a 'Plan Mode' structurally identical to AICP's Think — analysis without execution. Independent designs landing on the same Think/Edit/Act partition is evidence the pattern reflects a real design constraint."
created: 2026-04-18
updated: 2026-04-18
sources:
  - id: aicp-modes
    type: file
    file: aicp/core/modes.py
    description: "Mode enforcement code (Think/Edit/Act definitions + per-mode tool allowlists) — AICP project"
  - id: aicp-claude-md
    type: file
    file: CLAUDE.md
    description: "AICP CLAUDE.md `## Architecture > Three Permission Modes` — operator-facing description"
  - id: aicp-contribution-staging
    type: wiki
    file: raw/articles/from-aicp/patterns/01_drafts/three-permission-modes-think-edit-act.md
    description: "AICP's original submission, 2026-04-18 staged in raw/ before ingestion here"
tags: [pattern, modes, permission, authority, aicp, transferable, principle]
contributed_by: "aicp"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: "2026-04-18"
contribution_status: accepted
---

# Three Permission Modes (Think / Edit / Act) — Operator-Selected AI Authority Tiers

## Summary

A robust AI orchestration platform exposes **three tiers of authority** the operator selects per session: **Think** (AI may read, analyze, plan — but not edit files or execute commands), **Edit** (AI may modify files in a controlled scope and produce patches/diffs — but not execute commands), **Act** (AI may run commands, workflows, tools — highest power, most controlled). The pattern is operator-controlled, mechanically enforced (not just instructionally), and tier-shifting is an explicit operation. AICP names and enforces these three modes; Claude Code's "Plan Mode" is structurally a Think instance; the broader pattern transfers to any system where AI capability needs to be GATED by authority rather than truly safety-checked per call.

> [!info] Pattern Reference Card
>
> | Mode | What the AI MAY do | What the AI MAY NOT do | Default backend |
> |------|--------------------|------------------------|------------------|
> | **Think** | Read files, search, analyze, plan, propose, summarize, query MCP read-only tools | Modify files, run commands, write to disk, invoke side-effecting tools | local (analysis-dominant, cheap) |
> | **Edit** | All Think + Write/Edit tools in explicit scope, produce diffs | Run shell commands beyond a small allowlist, push to remote, invoke deploy | cloud (configurable per profile — diff quality matters) |
> | **Act** | All Edit + Bash, run scripts, invoke deploy/test workflows | Bypass guardrails (no mode → no enforcement) | cloud (most authority demands strongest model) |

## Pattern Description

The pattern partitions AI authority into three tiers. **Authority is monotonic**: Edit ⊃ Think; Act ⊃ Edit. Tier selection happens BEFORE the AI session begins — the operator chooses based on task intent + how much autonomous authority they're comfortable granting.

The pattern's correctness depends on four properties:

1. **Mechanical enforcement, not instructional.** Telling the AI "you're in Think mode, don't write" achieves the documented ~25% compliance baseline. Enforcing via runtime checks (Think mode REJECTS Write tool calls regardless of AI claim) achieves ~98%. Requires Level 2+ enforcement; instruction-only is insufficient.
2. **Tier transitions are explicit operations.** The operator EXPLICITLY changes mode (`aicp --mode edit`); the AI does not self-promote. An AI in Think mode that asks "should I switch to Edit?" is asking correctly — the answer comes from the operator.
3. **Per-tier backend coupling is a profile choice.** AICP's profiles can route modes to different backends (`force_cloud_modes: [edit, act]` routes Edit+Act to Claude even on local-first profiles). Mode is THE primary routing dimension correlated with cost-of-mistake.
4. **Modes COMPOSE with stage gates.** A task in `document` stage in `Edit` mode still has its `forbidden_zones` (no `aicp/`, `tests/`, `config/profiles/` writes per document stage). Modes = SESSION authority; stages = TASK scope. Both layer.

> [!warning] Recognition signal — a system exposing "autonomous mode" vs "guided mode" without a middle tier OR without enforcement is approximating but missing key properties.
>
> Common failure modes:
> - Two modes only (Think vs Act) — collapses the diff-producing middle tier; operators want "I'll review the diff before applying" semantics that Edit provides.
> - Three names but no enforcement (mode is just instruction text) — fails Quality Standards' compliance bar.
> - Mode is set IN-SESSION by the AI itself — defeats operator control.
> - Modes don't compose with other authority dimensions (scope, stage, role) — mode becomes the only authority knob, over-loaded.

## Instances

### Instance 1 — AICP CLAUDE.md + AGENTS.md three-mode declaration

CLAUDE.md `## Architecture > Three Permission Modes` defines modes (operator-facing). `aicp/core/modes.py` enforces them (machine-readable). Per CLAUDE.md: "Think — read, analyze, plan. No edits, no commands. Edit — modify files in a controlled scope. Produce patches/diffs. Act — run commands, workflows, tools. Highest power, most controlled."

### Instance 2 — AICP profiles `force_cloud_modes`

`force_cloud_modes: [edit, act]` in the default profile routes Edit + Act requests to Claude regardless of the local-first router policy. Rationale: an Edit session is producing diffs the operator will review; diff QUALITY matters more than per-request cost. Profile authors set this per their cost/quality tradeoff.

### Instance 3 — AICP guardrails (server-side enforcement)

Mode is ENFORCED server-side. Think mode requests with Write/Edit tool calls get rejected by guardrails before reaching the backend. The AI cannot "talk its way out" — check is mechanical, not LLM-mediated.

### Instance 4 — Claude Code's Plan Mode (cross-platform convergence)

Anthropic's Claude Code has a "Plan Mode" structurally identical to AICP's Think. Claude Code doesn't name the Edit/Act tiers explicitly; AICP's Three-Modes is a more explicit articulation. Independent designs landing on the same partition is evidence this reflects a real design constraint, not an AICP idiosyncrasy.

## When To Apply

- AI orchestration platforms where the AI can invoke tools with side effects (Write, Edit, Bash, deploy)
- Multi-tenant or multi-context deployments where some sessions are exploratory (Think suffices) and others are operational (need Edit/Act)
- Cost-sensitive deployments where mode-based routing materially changes per-session cost (Think → cheap local; Act → expensive cloud)
- Compliance/security contexts where authorized actions must be auditable per session (mode IS the auth tier in the audit log)
- Teams with mixed trust profiles: junior contributors get Think-only sessions; trusted operators get Act

## When Not To

- **Single-purpose AI tools** — a chatbot that never writes has no Edit or Act tier; mode partitioning adds no value
- **Fully autonomous agent systems with no human-in-loop** — mode selection assumes an operator; unattended systems need different authority (capability-based auth, signed commands)
- **Read-only assistants** — if the AI never edits or executes, Think is the only mode; naming adds noise
- **Systems with simpler authority models that work** — if binary tool-use toggle suffices, three modes is over-engineering

## Tradeoffs

> [!warning] The three-mode cost
>
> | Cost | Mitigation |
> |------|-----------|
> | Operators must choose mode per session (cognitive overhead) | Default to Think for new sessions; explicit upgrade. Lowest-authority default reduces accidents |
> | In-session mode transitions require restart (or per-tool auth prompts) | Per-tool prompts work but add friction; AICP defaults to per-session mode |
> | Three modes add vocabulary operators must remember | Names map to intuition (Think before Edit before Act); skills reference modes; permission prompts surface the active mode |
> | Mode + stage + role + scope = 4 authority dimensions to compose | Each axis adds enforcement signal; cost bounded; profile system bundles mode-related settings |

## Cross-Cutting Design Principles This Pattern Surfaces

1. **Authority is monotonic and tiered, not binary** — Think ⊂ Edit ⊂ Act. Operators want a middle tier (Edit) for review-before-apply.
2. **Authority must be enforced mechanically** — instructions insufficient (~25% compliance).
3. **Authority transitions are operator operations** — the AI cannot self-promote.
4. **Authority IS a routing dimension** — higher authority correlates with higher cost-of-mistake; justifies stronger backends.
5. **Authority composes with scope** — modes (session) layer with stages (task) layer with paths (file).

## Relationships

- BUILDS ON: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] (enforcement-level evidence)
- BUILDS ON: [[model-claude-code|Model — Claude Code]] (Plan Mode is one Think instance)
- RELATES TO: [[skills-as-primary-extension-pattern|Decision — Skills as Primary Extension Pattern]] (skills load conditionally; modes gate authority — different axes, both compose)
- RELATES TO: [[pretooluse-hooks-layered-approach|Decision — Layered PreToolUse Hooks]] (hooks enforce universal R01-R04; modes enforce per-session authority — both Layer 2 enforcement, complementary)
- RELATES TO: [[4-tier-router-with-profiles-over-hardcoded-routing|Decision — 4-tier Router with Profiles]] (profiles' `force_cloud_modes` is the mechanism making mode a routing dimension)

## Backlinks

[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[model-claude-code|Model — Claude Code]]
[[Decision — Skills as Primary Extension Pattern]]
[[Decision — Layered PreToolUse Hooks]]
[[Decision — 4-tier Router with Profiles]]
