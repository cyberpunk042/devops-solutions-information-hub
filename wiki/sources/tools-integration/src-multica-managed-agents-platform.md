---
title: "Synthesis — Multica: Open-Source Managed-Agents Platform (Orchestrator Layer Above 10 Harness CLIs, Apache 2.0, Self-Host or Cloud)"
aliases:
  - "Multica"
  - "Multica Managed Agents Platform"
  - "Multica Orchestrator"
  - "Multica Synthesis"
type: source-synthesis
domain: tools-integration
layer: 1
status: synthesized
confidence: high
maturity: seed
created: 2026-04-28
updated: 2026-04-28
last_reviewed: 2026-04-28
sources:
  - id: multica-github
    type: repository
    url: https://github.com/multica-ai/multica
    file: raw/articles/multica-aimultica.md
    title: "multica-ai/multica — README + 29 fetched files"
    description: "Authoritative open-source repository — Apache 2.0, Go backend + Next.js 16 frontend + PostgreSQL 17 (pgvector) + local-daemon agent runtime. Verified 2026-04-28."
    ingested: 2026-04-28
  - id: multica-website
    type: documentation
    url: https://multica.ai/
    file: raw/articles/multica-project-management-for-human-agent-teams.md
    title: "Multica — Project Management for Human + Agent Teams"
    description: "Project marketing page — supports BOTH self-host AND cloud (multica.ai/app); confirms vendor-neutral framing, BYO-LLM, and the agent-as-teammate model"
    ingested: 2026-04-28
  - id: harness-landscape
    type: wiki
    file: wiki/sources/tools-integration/src-agentic-coding-harness-landscape-2026.md
    description: "The 11+ harness landscape this orchestrator sits above. Multica supports 10 of them (Claude Code, Codex, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent, Kimi, Kiro CLI)."
  - id: opencode-synth
    type: wiki
    file: wiki/sources/tools-integration/src-opencode-harness-features.md
    description: "Per-harness synthesis for one of the supported backends. Multica orchestrates OpenCode at the layer above OpenCode's per-provider routing."
  - id: ai-decision-matrix
    type: wiki
    file: wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md
    description: "Decision matrix where Multica adds an orchestrator dimension. The matrix already covers harness × provider; Multica adds a third axis (orchestrator)."
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Mission lesson. Multica's explicit 'No vendor lock-in / Bring your own LLM provider, swap agent backends' framing is empirical anti-vendor-lock-in at the orchestrator layer — a layer the lesson's evidence chain hadn't yet documented."
tags: [multica, orchestrator, managed-agents-platform, meta-harness, claude-code, codex, openclaw, opencode, hermes, gemini, pi, cursor-agent, kimi, kiro-cli, apache-2-0, go, postgresql, pgvector, websocket, self-hosted, cloud-optional, vendor-neutral, anti-vendor-lock-in, mission-2026-04-28, paper-pdf-layer-1, post-anthropic-stack]
---

# Synthesis — Multica: Open-Source Managed-Agents Platform

## Summary

Multica ([multica-ai/multica](https://github.com/multica-ai/multica), Apache 2.0) is an **open-source managed-agents orchestration platform** that sits above the agent-CLI harness layer. It auto-detects 10 agent CLIs (Claude Code · Codex · OpenClaw · OpenCode · Hermes · Gemini · Pi · Cursor Agent · Kimi · Kiro CLI) on your `PATH` via a local daemon, then exposes them as **assignable teammates** in a board-and-issues UX where humans and agents share the same dropdown, the same activity timeline, and the same task-lifecycle (enqueue → claim → start → complete/fail). Agents create issues, leave comments, post status updates, and report blockers proactively via WebSocket-streamed real-time progress. Backend is Go (Chi router · sqlc · gorilla/websocket) on PostgreSQL 17 with pgvector; frontend is Next.js 16 (App Router); deployable as self-host (Docker Compose, Kubernetes, or single binary) OR via the hosted cloud at multica.ai/app. Multica's own framing — *"vendor-neutral, self-hosted, and designed for human + AI teams"* — is explicit anti-vendor-lock-in at the orchestrator layer, a layer the wiki's mission documentation had not yet covered. Operationally, Multica adds a **third composable substitution dimension** to the wiki's existing harness × provider matrix: orchestrator × harness × provider, where no single vendor controls more than one layer. This synthesis grounds Multica concretely (Apache 2.0 license verified · 10-harness support verified · architecture verified) and locates it in the post-Anthropic stack the wiki teaches.

## Reference Card

> [!info] Multica reference card

| Field | Value |
|---|---|
| **Repository** | [multica-ai/multica](https://github.com/multica-ai/multica) |
| **Website** | [multica.ai](https://multica.ai/) · cloud at multica.ai/app |
| **License** | Apache 2.0 |
| **Backend stack** | Go (Chi router · sqlc · gorilla/websocket) |
| **Frontend stack** | Next.js 16 (App Router) |
| **Database** | PostgreSQL 17 + pgvector |
| **Agent runtime** | Local daemon (auto-detects CLIs on PATH) |
| **Supported harness CLIs (10)** | `claude` · `codex` · `openclaw` · `opencode` · `hermes` · `gemini` · `pi` · `cursor-agent` · `kimi` · `kiro-cli` |
| **Deployment options** | Self-host (Docker Compose · Kubernetes · single binary) OR Multica Cloud |
| **Install (macOS/Linux Homebrew)** | `brew install multica-ai/tap/multica` |
| **Install (curl install script)** | `curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh \| bash` |
| **Setup command** | `multica setup` (Cloud) or `multica setup self-host` |
| **Self-host with server** | `bash -s -- --with-server` flag pulls images from GHCR; Docker required |
| **Languages** | English + Simplified Chinese |
| **Confidence** | high — README verified at full PDF depth + project page read |
| **Mission relevance** | Critical — closes the orchestrator-layer documentation gap in the wiki's anti-vendor-lock-in evidence chain |

## Key Insights

1. **Multica is a meta-harness, not a harness.** It does not replace Claude Code / OpenCode / Codex / etc. — it ORCHESTRATES them. The agent-CLI tools remain the execution layer; Multica adds task management, multi-runtime coordination, skill reuse, and team-collaboration UX above them. Anyone using one of the 10 supported harnesses can adopt Multica without changing how the harness works internally.

2. **"Runtime" is Multica's compute-environment abstraction.** A Runtime is "a compute environment that can execute agent tasks" — your local daemon OR a cloud instance. Each Runtime auto-reports which agent CLIs it has, so Multica routes work to the runtime that has the right harness + the right hardware. Multi-runtime support means you can mix laptop daemon + cloud runtime in one workspace.

3. **Agents are first-class objects, not function calls.** They have profiles (name, instructions, skills attached). They appear in the assignee dropdown alongside humans. They post comments, create issues, change status. Operationally this is a different abstraction than "prompt → response" — agents are persistent participants in the team's project state.

4. **Skills are reusable capability bundles**, defined per agent or shared across the workspace. The README demos a skill "write-migration" that bundles a `SKILL.md` description + config + schema + templates. Once written, every agent can invoke it. Multica's skills are *its own* abstraction (not Claude Code skills) — but the concept overlaps. The wiki's [model-skills-commands-hooks](../../spine/models/agent-config/model-skills-commands-hooks.md) is the closest existing parallel.

5. **Deployment topology: BOTH cloud-and-self-host, no forced choice.** This matters for anti-vendor-lock-in: the operator's data (issues, agent state, code execution) can stay on operator infrastructure even while Multica's coordination/state is in the cloud — OR everything can be self-hosted. Multi-tenancy via workspaces is built in.

6. **Code execution stays local.** Per Multica's FAQ: *"Agent execution happens on your machine (local daemon) or your own cloud infrastructure. Code never passes through Multica servers. The platform only coordinates task state and broadcasts events."* Multica is a **coordinator**, not a code-running middleman. This is structurally important for the wiki's data-sovereignty claims.

7. **Vendor-neutrality is structurally enforced**, not just claimed. Apache 2.0 license + 10-harness auto-detection + self-host option + BYO LLM provider (the harness layer's responsibility) = no single vendor can lock the operator at the orchestrator layer. The wiki's [anti-vendor-lock-in lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) Evidence-chain gains a new layer.

8. **The 10-harness list is comprehensive against the wiki's harness landscape.** Per [agentic-coding-harness-landscape-2026](src-agentic-coding-harness-landscape-2026.md), the wiki documents 11+ harnesses. Multica supports 10 of them. Notable absences from Multica's auto-detect list: Aider, Cline, Continue, Crush, Goose. Most of the wiki-documented "Tier 1" harnesses (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, OpenClaw) are covered.

9. **Comparison to "Paperclip"** (per Multica's own README comparison table): Multica is **team-oriented + cloud-first + lightweight management** (Issues/Projects/Labels). Paperclip is **solo + local-first + heavy governance** (Org chart/Approvals/Budgets). Multica has Skills system; Paperclip has Skills + Plugin system. The two solve different problems — Multica targets team collaboration with AI-as-teammate; Paperclip simulates a solo AI agent company.

10. **Position in the post-Anthropic stack**: Multica adds a layer ABOVE the existing wiki documentation. The wiki has covered harness × provider as a 2-axis matrix; Multica makes it a 3-axis matrix (orchestrator × harness × provider). The operator's existing AICP routing (provider × harness) is now composable with Multica orchestration (orchestrator × the rest).

## Architecture

> [!abstract] Multica architecture (verified from README)

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐
│   Next.js    │────>│  Go Backend  │────>│   PostgreSQL     │
│   Frontend   │<────│  (Chi + WS)  │<────│   (pgvector)     │
└──────────────┘     └──────┬───────┘     └──────────────────┘
                            │
                     ┌──────┴───────┐
                     │ Agent Daemon │  runs on your machine
                     └──────────────┘  (Claude Code, Codex, OpenCode,
                                        OpenClaw, Hermes, Gemini,
                                        Pi, Cursor Agent, Kimi,
                                        Kiro CLI)
```

| Layer | Stack | Notes |
|---|---|---|
| Frontend | Next.js 16 (App Router) | Modern React; web UX is the primary surface |
| Backend | Go (Chi · sqlc · gorilla/websocket) | Single Go binary; fast startup; static compilation |
| Database | PostgreSQL 17 + pgvector | pgvector enables semantic features; no separate vector DB |
| Agent Runtime | Local daemon | Auto-detects 10 CLIs; routes per-task to the right runtime |
| Communication | WebSocket | Real-time progress streaming + activity timeline updates |
| Build target | Cross-platform binaries | macOS / Linux / Windows × amd64 / arm64 (per `.goreleaser.yml`) |
| Update channel | GHCR + Homebrew tap + install scripts | Stable + self-update via `multica update` |

Operator-side install touches **one binary** + **one daemon process** + (optionally) **a Docker stack for self-host**. No JVM/runtime overhead beyond Go + Postgres.

## Mission Alignment — The Third Substitution Layer

Per the [anti-vendor-lock-in lesson](../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md), the wiki's mission claim is empirical when every stack layer has direct paper evidence demonstrating substitutability. Multica adds a layer the lesson's existing 9-layer evidence chain (generation × 3 / retrieval / inference paradigm / training framework / environment library / evaluation × 4 / loss objective / + deployment validation) had not covered: **orchestrator**.

> [!success] **Three substitution dimensions composable**
>
> ```
> Orchestrator (Multica)              ← anti-vendor-lock-in here too (Apache 2.0, self-host option)
>   ├─ Claude Code  ─→  Anthropic | OpenRouter | Ollama (v0.14+) | Ollama Cloud
>   ├─ OpenCode     ─→  75+ providers (Ollama, OpenRouter, Together, ...)
>   ├─ Codex        ─→  OpenAI | OpenRouter | ...
>   ├─ Kimi CLI     ─→  Moonshot direct | OpenRouter
>   ├─ Cursor Agent ─→  proprietary
>   ├─ Gemini CLI   ─→  Google | OpenRouter
>   └─ Hermes / Pi / OpenClaw / Kiro CLI ─→  their respective providers
> ```
>
> No single vendor controls more than one of the three layers. Anti-vendor-lock-in at three layers is **structurally stronger than at two** — the wiki's prior 9-layer evidence chain implicitly assumed a single orchestrator (the operator's own scripts/AICP); Multica makes the orchestrator layer a first-class substitutable component.

For the operator's mission specifically:

| Operator's stack layer | Substitute via | Mission status |
|---|---|---|
| Orchestrator | **Multica** (open-source, Apache 2.0, self-host) | ✅ Available now, free |
| Harness | Claude Code · OpenCode · Codex · Kimi · ... | ✅ Already in operator's toolchain |
| Provider routing | AICP backend pattern + OpenRouter + Ollama Cloud | ✅ Already validated ($540 → $100 finding) |
| Generation (long-context) | RLM-Qwen3-8B (`mit-oasys/rlm-qwen3-8b-v0.1`) | ✅ Confirmed live, Phase-1 deployable |
| Generation (tier-0 dense) | Qwen3.6-27B at UD-IQ2 | ✅ Confirmed runnable on incoming RTX 3090 |

Every layer has open-source-substitute paper or repo evidence. **The wiki's mission claim is empirically traceable end-to-end across orchestrator + harness + provider + generation now**, not just harness + provider + generation.

## Operator's Decision Space

> [!tip] Should the operator adopt Multica?
>
> The decision is **bounded by what's safe-unilateral and zero-spend**. Multica is open source + self-host capable, so the trial cost is operator's own machine time. Per the saved feedback memory on money-spending clarity:
>
> | Path | Cash | Wall time | What you get |
> |---|---|---|---|
> | **A: Trial via Homebrew + cloud (free tier)** | $0 | ~10 min install | Multica orchestrating Claude Code / OpenCode locally, board UX, agent-as-teammate model. State coordination on multica.ai cloud; code stays local. |
> | **B: Self-host via Docker Compose** | $0 cash; ~hour to set up | Tighter data sovereignty (state and code both local), but more ops burden | Same product, fully on-prem |
> | **C: Defer until 3090 lands** | $0 | 2-3 weeks | Adopt Multica AFTER hardware capability is in hand, when the multi-runtime use case is compelling |
>
> **Recommendation**: trial Path A on existing hardware (Multica is harness-orchestrating, not compute-intensive itself). The operator can run it now, see the team-coordination UX with Claude Code + OpenCode, and decide whether the orchestrator layer adds enough value before the 3090-driven Phase-1 routing deployment lands. If yes, switch to self-host (Path B) when AICP routing comes online. **No money commitment at any decision gate.**

## Comparison to Adjacent Tools

| Tool | Layer | Open-source? | Multi-harness? | Multi-provider? | Self-host? |
|---|---|---|---|---|---|
| **Multica** | Orchestrator (above harness) | ✅ Apache 2.0 | ✅ 10 harnesses | Indirect (via harness) | ✅ Both |
| [claude-code-router](https://github.com/musistudio/claude-code-router) | Provider proxy (below harness) | ✅ | ❌ Claude Code only | ✅ Many providers via Anthropic API compat | ✅ Self-only |
| AICP (operator's tool) | Provider router (below harness) | ✅ Apache 2.0 (operator's repo) | ❌ Provider-side only | ✅ via backend pattern | ✅ Self-only |
| OpenRouter | Provider aggregator | ❌ | (any harness) | ✅ 100+ models | ❌ Cloud only |
| Ollama (local) | Provider implementation | ✅ MIT | (any harness via OpenAI/Anthropic compat) | ❌ Local-only | ✅ |
| Ollama Cloud | Provider hosted | ❌ Cloud SaaS | (any harness) | (Ollama-hosted models) | ❌ |

**Multica's distinct niche**: orchestrator above the harness layer with multi-harness + multi-runtime + team-collaboration features. None of the adjacent tools occupy that exact role. It's complementary to the operator's existing AICP (which sits below the harness, routing providers).

## Open Questions

> [!question] How does Multica's "Skills" abstraction relate to Claude Code's skills?
> Multica's skills are workspace-level reusable capability bundles (SKILL.md + config + templates). Claude Code's skills are CLI-level extension files. They overlap in name but differ in scope and execution. (Requires: ingest a Multica SKILL.md example to confirm structural compatibility.)

> [!question] Does Multica's daemon work alongside other agent-runtime managers?
> If the operator already runs OpenClaw harness or AICP daemon, does Multica's daemon coexist or compete? (Requires: read CLI_AND_DAEMON.md from the Multica repo.)

> [!question] What's the data-flow security boundary in cloud mode?
> Multica's FAQ says "Code never passes through Multica servers." Verify how task state, agent comments, and skill definitions are stored — what's encrypted at rest, what flows over the wire? (Requires: read SELF_HOSTING.md security section + the Go backend code.)

> [!question] Is Kimi CLI integration confirmed to work with Kimi K2.6 specifically?
> The README lists `kimi` as auto-detected, but doesn't specify which Kimi CLI version or which Kimi model. The operator's existing K2.6 + OpenRouter wiring may or may not interoperate. (Requires: test or read Kimi CLI's docs.)

## How to Apply

> [!tip] Operator adoption checklist (when ready)
>
> 1. **Install via Homebrew**: `brew install multica-ai/tap/multica`
> 2. **Setup cloud trial**: `multica setup` (configures + authenticates + starts daemon)
> 3. **Verify runtime detection**: open the workspace, confirm machine appears in Settings → Runtimes with detected CLIs listed
> 4. **Create one agent**: pick the runtime + a CLI provider (Claude Code recommended for first trial), give it a name + instructions
> 5. **Assign one issue**: create from board, assign to agent, observe execution + activity timeline
> 6. **Decide self-host vs cloud**: based on the trial's data-sovereignty fit, switch to self-host (Docker Compose) if needed
> 7. **Update AICP routing**: once Multica runs Claude Code, confirm AICP's provider routing still applies inside the Claude Code that Multica orchestrates (Multica is at orchestrator layer, AICP at provider layer — they should compose without conflict)
> 8. **Document the decision** via `gateway contribute --type decision` (or similar) — the wiki captures the operator's actual adoption choices over time

## Relationships

- DERIVED FROM: [[src-agentic-coding-harness-landscape-2026|Agentic Coding Harness Landscape 2026]] (Multica orchestrates 10 of the 11+ harnesses this synth catalogs)
- DERIVED FROM: [[src-opencode-harness-features|OpenCode Synthesis]] (one of the supported harnesses)
- BUILDS ON: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] (adds the orchestrator layer to the lesson's evidence chain)
- BUILDS ON: [[ai-model-provider-harness-decision-matrix-2026|AI Model × Provider × Harness Decision Matrix 2026]] (extends from 2-axis to 3-axis matrix)
- BUILDS ON: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (orchestrator dimension was implicit; now explicit)
- COMPARES TO: [[src-inference-provider-landscape-2026|Inference Provider Landscape 2026]] (different layer; orchestrator vs provider)
- COMPARES TO: [[src-kimi-k2-6-moonshot-agent-swarm|Kimi K2.6]] (Kimi CLI is one of Multica's supported harnesses)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (orchestrator-layer enforcement structure: Multica's daemon is infrastructure for cross-harness coordination, not instructions about it)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] (Multica's "no vendor lock-in" claim is verified by Apache 2.0 + self-host + 10-harness support, not just declared)
- RELATES TO: [[model-ecosystem|Model — Ecosystem Architecture]] (orchestrator topology adds a hub-spoke option above the harness fleet)
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, Hooks]] (Multica's Skills concept overlaps with the wiki's skills mechanism — different scope, similar pattern)
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (orchestrator dimension addendum candidate)

## Backlinks

[[src-agentic-coding-harness-landscape-2026|Agentic Coding Harness Landscape 2026]]
[[src-opencode-harness-features|OpenCode Synthesis]]
[[Anti-Vendor-Lock-In Lesson]]
[[ai-model-provider-harness-decision-matrix-2026|AI Model × Provider × Harness Decision Matrix 2026]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[src-inference-provider-landscape-2026|Inference Provider Landscape 2026]]
[[Kimi K2.6]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[Model — Skills, Commands, Hooks]]
[[2026 Consumer Hardware AI Stack]]
