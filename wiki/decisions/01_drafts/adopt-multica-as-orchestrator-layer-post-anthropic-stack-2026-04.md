---
title: "Decision: Adopt Multica as Orchestrator Layer in the Post-Anthropic Stack (2026-04-28)"
aliases:
  - "Adopt Multica Decision 2026-04-28"
  - "Multica Orchestrator Adoption"
type: decision
domain: cross-domain
layer: 6
status: synthesized
confidence: high
maturity: seed
derived_from:
  - "Synthesis — Multica: Open-Source Managed-Agents Platform"
  - "Anti-Vendor-Lock-In Lesson Evidence 10"
  - "Post-Anthropic Stack 3-Layer Composability Epic"
reversibility: moderate
created: 2026-04-28
updated: 2026-04-28
sources:
  - id: multica-synth
    type: wiki
    file: wiki/sources/tools-integration/src-multica-managed-agents-platform.md
    description: "Layer-1 source synthesis for Multica — license, architecture, supported harnesses, per-agent shaping dimensions, operator-validated 2026-04-28"
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Mission lesson — Evidence 10 documents the orchestrator-layer empirical substitute"
  - id: epic
    type: wiki
    file: wiki/backlog/epics/pre-milestone/post-anthropic-stack-3-layer-assembly-multica-aicp-3090.md
    description: "Parent epic this decision implements"
  - id: m001-custom-env
    type: wiki
    file: wiki/backlog/modules/post-anthropic-3-layer-m001-multica-per-agent-provider-config.md
    description: "Operator-validated `custom_env` mechanism — the per-agent provider routing made possible by this decision"
  - id: operator-multica-self-host
    type: notes
    file: ~/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/project_multica_self_hosted_2026_04_28.md
    description: "Operator's self-host install at /home/jfortin/.multica/server/, source-level access"
tags: [decision, p0, orchestrator, multica, post-anthropic, anti-vendor-lock-in, 3-layer-stack, mission-2026-04-28, architecture, harness-orchestration, vendor-neutral]
---

# Decision: Adopt Multica as Orchestrator Layer in the Post-Anthropic Stack (2026-04-28)

## Summary

Adopt **Multica** ([multica-ai/multica](https://github.com/multica-ai/multica), Apache 2.0) as the orchestrator layer above the harness layer in the post-Anthropic AI stack. The decision is grounded in Multica's auto-detection of 10 harness CLIs (Claude Code · Codex · OpenClaw · OpenCode · Hermes · Gemini · Pi · Cursor Agent · Kimi · Kiro CLI), per-agent provider routing via `custom_env` field (operator-validated 2026-04-28), self-host capability (operator runs at `/home/jfortin/.multica/server/`), and Apache 2.0 license. Multica adds a third independently-substitutable substitution layer to the wiki's anti-vendor-lock-in evidence chain, completing **3-layer composability**: orchestrator (Multica) × harness (10 supported) × provider (10+ via AICP routing). No single vendor controls more than one of the three layers.

## Decision

> [!success] **Multica is the orchestrator layer for the post-Anthropic stack.**
>
> | Scenario | Use Multica? |
> |----------|--------------|
> | Solo operator, single harness, single provider | ❌ No — direct CLI use; orchestrator overhead exceeds benefit |
> | Solo operator, multiple harnesses (e.g., Claude Code + OpenCode) | ✅ Yes — unified board UX + skill reuse + multi-runtime monitoring |
> | Solo operator, multi-runtime (laptop + cloud GPU + workstation) | ✅ Yes — auto-detection + WebSocket streaming designed for this case |
> | Solo operator wanting per-agent provider routing (AICP / Ollama Cloud / direct) | ✅ Yes — `custom_env` field is the mechanism (operator-validated 2026-04-28) |
> | Team-of-humans + agents | ✅ Yes — built-in human + agent collaboration UX |
> | Heavy governance / approvals / budgets | ❌ No — Multica is lightweight management; Paperclip suits this case |
> | High data-sovereignty needs | ✅ Yes via self-host — operator owns DB, machine, daemon |
>
> **For the operator's specific stack**: yes — already runs Claude Code + OpenCode, plans multi-runtime (laptop now + cloud-occasional + RTX 4090 mid-May 2026), needs per-agent provider routing for AICP / Ollama Cloud / Anthropic-direct. **Multica is the right orchestrator layer.**

## Alternatives

### Alternative 1: No orchestrator (direct CLI use)

Continue using Claude Code, OpenCode, etc. directly without an orchestration layer. Operator drives each harness individually; AICP handles provider routing under each harness.

> [!warning] Rejected: No unified team-collaboration UX, no skill reuse across harnesses, no multi-runtime visibility, no per-agent provider abstraction. Operator already runs 2 harnesses; the orchestrator layer becomes mission-aligned once multi-harness use is concrete (which it is). Direct CLI use was correct *before* multi-harness adoption; with Claude Code + OpenCode both in active use and 4090-incoming multi-runtime, the orchestrator layer has earned its place.

### Alternative 2: Operator-built orchestrator

Build a custom orchestrator on top of AICP that wraps harness invocation + task tracking + activity timelines.

> [!warning] Rejected: Significant engineering cost, parallel reimplementation of what Multica already provides under Apache 2.0. Operator's mission framing is anti-vendor-lock-in (specialty routing), not anti-third-party-tool. Multica is open-source + self-host capable, so the lock-in concern that would justify in-house build doesn't apply. Build effort would be weeks of work for parity that Multica delivers today.

### Alternative 3: Paperclip (per Multica's own README comparison table)

Paperclip simulates a solo AI agent company with org-chart + approvals + budgets governance. Different abstraction layer.

> [!warning] Rejected for current operator state: heavy governance is mismatched to operator's solo-engineer mission. Paperclip suits an operator simulating an org structure. The operator's stack is harness × provider × orchestrator composability — Multica's lightweight Issues/Projects/Labels matches this better. Re-evaluate if operator's needs shift toward governance simulation.

### Alternative 4: Use a different open-source orchestrator (claude-code-router as orchestrator)

Treat [claude-code-router](https://github.com/musistudio/claude-code-router) as a lightweight orchestrator-equivalent for Claude Code agents.

> [!warning] Rejected: claude-code-router is a *provider proxy* (sits below the harness, intercepts Claude Code's API calls), not an orchestrator. It complements Multica (could be used as the harness-level provider router) but doesn't replace Multica's task-management + multi-harness + multi-runtime + skills + activity-timeline functionality. Different layer, different scope.

## Rationale

Multica's adoption is grounded in five concrete properties verified against Multica's documentation + operator's live UI inspection:

1. **Apache 2.0 license** — verified from `.goreleaser.yml` in the source tree. Operator can fork, patch, or extend without licensing concerns. Mission-aligned (anti-vendor-lock-in via open-source).

2. **10 harness CLIs auto-detected** — `claude`, `codex`, `openclaw`, `opencode`, `hermes`, `gemini`, `pi`, `cursor-agent`, `kimi`, `kiro-cli`. Covers the operator's current toolset (Claude Code + OpenCode) plus 8 additional options as the operator's stack evolves. Per [agentic-coding-harness-landscape-2026](../sources/tools-integration/src-agentic-coding-harness-landscape-2026.md), Multica supports 10 of the 11+ wiki-tracked harnesses.

3. **Per-agent provider routing via `custom_env`** — operator-validated 2026-04-28: *"Injected into the agent process at launch (e.g. ANTHROPIC_API_KEY, ANTHROPIC_BASE_URL)"*. This is the mechanism that makes AICP / Ollama Cloud / Anthropic-direct routing per-agent rather than per-process-tree. Plus `custom_args` for CLI flag tuning + `skills` for capability composition + `mcp_config` for MCP integration (Claude Code only) = **7 per-agent shaping dimensions**.

4. **Self-host capability + operator's source-level access** — operator runs at `/home/jfortin/.multica/server/`, built from source, with `.env` operator-written. Plaintext-DB caveat from Multica's docs is mitigated for self-host (operator owns the filesystem). If a future use case requires extending Multica itself, operator can patch the daemon directly rather than waiting on upstream.

5. **3-layer composability achieved** — per [anti-vendor-lock-in lesson Evidence 10](../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md): Multica × harness × provider gives three independently-substitutable layers. Per [Principle 4 (Declarations Aspirational Until Verified)](../lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md), the substitution claim at each layer is verified by operator-validated working integration, not just declared.

## Reversibility

**Moderate** to reverse. If Multica becomes unsuitable (license change · upstream stagnation · acquisition by misaligned vendor · Multica daemon proves too brittle in operator's workflow):

- **What's preserved**: harness configurations (Claude Code + OpenCode + AICP routing remain unchanged) · skills written for Multica COULD be portable to claude-code-router or operator-built orchestrator with translation work · agent prompts/instructions are documented (via `instructions` field) and operator-owned.
- **What requires migration**: Multica's database (issue history, agent definitions, skill bundles, activity timelines) — this becomes operator's data even when Multica is self-hosted, but the schema is Multica-specific. Migration to a different orchestrator means re-creating agents, re-attaching skills, re-defining workflows.
- **What's lost**: the multi-runtime auto-detection convention; the agent-as-teammate UX in board view; integrated WebSocket progress streaming. These are Multica-specific abstractions.

**Mitigation for reversibility**: keep agent definitions documented externally (in this wiki, e.g., per-agent recipes per [M001](../backlog/modules/post-anthropic-3-layer-m001-multica-per-agent-provider-config.md)) so reconstruction is mechanical. Skills SHOULD be authored as portable bundles (SKILL.md + config + templates) that can move between orchestrators. Don't depend on Multica-specific features that have no equivalent elsewhere.

## Dependencies

This decision affects:

- **[Post-Anthropic Stack 3-Layer Composability Epic](../backlog/epics/pre-milestone/post-anthropic-stack-3-layer-assembly-multica-aicp-3090.md)** — this decision IS the epic's foundational architectural choice
- **[Anti-Vendor-Lock-In Lesson](../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md)** Evidence 10 — empirical content
- **[AI Model × Provider × Harness Decision Matrix 2026](../spine/references/ai-model-provider-harness-decision-matrix-2026.md)** — orchestrator dimension added 2026-04-28
- **[K2.6 Access Paths Comparison](../comparisons/kimi-k2-6-access-paths-openrouter-ollama-cloud-local.md)** — composes through Multica's per-agent `custom_env` for K2.6-specific routing
- **AICP integration** (operator's repo at `~/devops-expert-local-ai/`) — AICP's backend pattern remains unchanged; Multica orchestrates harnesses that talk to AICP. AICP-side does NOT need to change to accommodate Multica.
- **Future M002 / M003 / M004** modules — implementation modules under the parent epic implement this decision concretely.

## How This Connects — Navigate From Here

> [!abstract] From this decision → related knowledge
>
> | Direction | Go To |
> |---|---|
> | **The Multica synthesis** (Layer-1 source) | [[src-multica-managed-agents-platform\|Multica Synthesis]] |
> | **The parent epic** (operational implementation) | [[post-anthropic-stack-3-layer-assembly-multica-aicp-3090\|Post-Anthropic 3-Layer Stack Epic]] |
> | **The mechanism that enables this decision** (operator-validated 2026-04-28) | [[post-anthropic-3-layer-m001-multica-per-agent-provider-config\|M001 — Multica `custom_env` Mechanism]] |
> | **The smoke-test runbook** (operator validation gate) | [[post-anthropic-3-layer-m003-multica-aicp-ollama-cloud-smoke-test-runbook\|M003 — Smoke-Test Runbook]] |
> | **The mission lesson the decision supports** | [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence\|Anti-Vendor-Lock-In Lesson]] |
> | **The principle this decision verifies** | [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle 4]] |

## EXTENDED 2026-04-30 — Multica Sits Below the Trust Layer (4-Layer Composition)

> [!info] **The decision composes with the 4th-layer extension**
>
> Per the [Trust-Layer Epic](../../backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md) authored 2026-04-30, the operator's tamper-proof-inference design adds a fourth substitutable layer — trust / confidential-compute — on top of orchestrator × harness × provider. **Multica's role does not change**: it remains the orchestrator-layer choice. The trust layer's cypher + decypher + compression pipeline runs *underneath* Multica's orchestration, regardless of which harness and provider are selected. The decision's reversibility analysis is unaffected — Multica swap remains moderate cost, the trust layer is independent.
>
> Composability picture:
>
> ```
> TRUST  L2/L3 (compressed + encrypted + GPU-decypher; attestation if L3)
>   ↓
> Multica (orchestrator — this decision)
>   ├─ Claude Code  ─→  AICP routing  ─→  local (RTX 4090 with L2)
>   ├─ OpenCode     ─→  AICP routing  ─→  Ollama Cloud | OpenRouter | local
>   └─ Kimi CLI     ─→  AICP routing  ─→  Moonshot direct | OpenRouter
> ```
>
> See [anti-vendor-lock-in lesson Evidence 11](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) for the 4-layer empirical claim, and the [Trust-Layer Learning Path](../../spine/learning-paths/trust-layer-tamper-proof-inference-2026-04-30.md) for the curated reading order.

## Relationships

- DERIVED FROM: [[src-multica-managed-agents-platform|Multica Synthesis]] (the Layer-1 source for the orchestrator-layer empirical evidence)
- DERIVED FROM: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] § Evidence 10
- DERIVED FROM: [[post-anthropic-stack-3-layer-assembly-multica-aicp-3090|Post-Anthropic 3-Layer Stack Epic]]
- IMPLEMENTS: [[post-anthropic-self-autonomous-stack|Milestone — Post-Anthropic Self-Autonomous Stack]]
- EXTENDED BY: [[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic (2026-04-30)]] — Multica's orchestrator role composes underneath the trust layer; 4-layer mission claim added 2026-04-30
- BUILDS ON: [[ai-model-provider-harness-decision-matrix-2026|AI Decision Matrix 2026]] (orchestrator dimension)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] (verified by operator's `custom_env` validation, not just declared)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (Multica's daemon = infrastructure; per-agent `custom_env` = infrastructure not instructions)
- COMPARES TO: [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]] (different layer of the stack — that decision is provider-side; this decision is orchestrator-side)
- FEEDS INTO: [[post-anthropic-3-layer-m001-multica-per-agent-provider-config|M001]] (recipe for adoption)
- FEEDS INTO: [[post-anthropic-3-layer-m003-multica-aicp-ollama-cloud-smoke-test-runbook|M003]] (verification runbook)

## Backlinks

[[src-multica-managed-agents-platform|Multica Synthesis]]
[[Anti-Vendor-Lock-In Lesson]]
[[post-anthropic-stack-3-layer-assembly-multica-aicp-3090|Post-Anthropic 3-Layer Stack Epic]]
[[Milestone — Post-Anthropic Self-Autonomous Stack]]
[[Trust-Layer Epic (2026-04-30)]]
[[ai-model-provider-harness-decision-matrix-2026|AI Decision Matrix 2026]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
[[M001]]
[[M003]]
