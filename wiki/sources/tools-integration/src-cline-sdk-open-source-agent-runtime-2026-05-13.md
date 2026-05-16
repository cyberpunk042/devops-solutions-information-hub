---
title: "Synthesis — Cline SDK (@cline/sdk) — Open-Source Agent Runtime Extracted from Cline 2.0, Outperforms Claude Code on Terminal Bench 2.0 (2026-05-13)"
aliases:
  - "Cline SDK Release 2026-05-13"
  - "@cline/sdk Open-Source Agent Runtime"
  - "Cline 2.0 Harness Extraction"
type: source-synthesis
layer: 1
maturity: growing
domain: tools-and-platforms
status: synthesized
confidence: high
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: cline-blog-introducing-sdk
    type: vendor-announcement
    url: https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime
    file: raw/articles/introducing-cline-sdk-the-upgraded-agent-runtime-and-we-rebuilt-cline-upon-it-cl.md
    title: "Introducing Cline SDK: the upgraded agent runtime, and we rebuilt Cline upon it"
    author: Renee Huang
    published: 2026-05-13
    ingested: 2026-05-16
  - id: marktechpost-cline-sdk
    type: trade-press
    url: https://www.marktechpost.com/2026/05/14/cline-releases-cline-sdk-an-open-source-agent-runtime-now-powering-its-cli-and-kanban-with-ide-extensions-being-migrated/
    file: raw/articles/cline-releases-cline-sdk-an-open-source-agent-runtime-now-powering-its-cli-and-k.md
    title: "Cline Releases Cline SDK: An Open-Source Agent Runtime Now Powering Its CLI and Kanban"
    author: Asif Razzaq
    published: 2026-05-14
    ingested: 2026-05-16
  - id: testingcatalog-cline-sdk
    type: trade-press
    url: https://www.testingcatalog.com/cline-releases-open-source-agent-runtime-sdk-for-coding-agents/
    file: raw/articles/cline-releases-open-source-agent-runtime-sdk.md
    title: "Cline releases open-source agent runtime SDK for coding agents"
    author: Nero Soares
    published: 2026-05-13
    ingested: 2026-05-16
tags: [cline, cline-sdk, agent-runtime, agent-harness, open-source, typescript, terminal-bench-2-0, claude-opus-4-7, claude-code, opencode, codex, droid, multi-provider, subagents, plugins, mcp, apache-2-0, npm, layered-architecture, browser-compatible]
---

# Synthesis — Cline SDK (@cline/sdk) — Open-Source Agent Runtime Extracted from Cline 2.0, Outperforms Claude Code on Terminal Bench 2.0 (2026-05-13)

## Summary

On 2026-05-13, Cline announced **@cline/sdk** — its core agent harness extracted from the Cline VS Code extension into a standalone, open-source, four-layer TypeScript SDK now powering Cline's CLI, Kanban, VS Code extension (in migration), and JetBrains extension (in migration). The release is Apache-2.0 licensed, requires Node.js 22+, and is published to npm as `@cline/sdk` (which re-exports `@cline/core` over `@cline/agents` over `@cline/llms` over `@cline/shared`). Cline accompanied the release with **Terminal Benchmark 2.0** (tbench.ai) numbers: Cline CLI scores **74.2% on claude-opus-4.7** vs Anthropic's published **69.4% for Claude Code** on the same model (+4.8 pp delta, harness-attributable since model is constant); 71.9% vs 65.4% on claude-opus-4.6; **55.1% on kimi-k2.6** vs OpenCode 37.1% (+18 pp) and Pi-Code 45.5% (+9.6 pp). This is a structural sibling event to the [[src-cline-agentic-coding-ide-extension|prior 2026-04-15 Cline IDE-extension synthesis]] — same product line, but the harness is now an **independent, embeddable artifact** rather than an implementation detail of the extension. Strategically: a public, MIT/Apache-licensed, benchmark-validated alternative to Claude Code's harness exists; harness-engineering as the dominant performance lever is empirically reinforced again (constant-model harness swap = +4.8 pp on Opus 4.7); and operator-stack-direct because Claude Code is the daily harness while Cline SDK is now a credible swap-in (or composable substrate) at the runtime layer.

## Source Reference

> [!info] Source card
>
> | Source | Type | URL | Published | Ingested |
> |--------|------|-----|-----------|----------|
> | Cline Blog — Renee Huang | Vendor announcement (primary) | [introducing-cline-sdk-the-upgraded-agent-runtime](https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime) | 2026-05-13 | 2026-05-16 |
> | MarkTechPost — Asif Razzaq | Trade press (independent) | [cline-releases-cline-sdk-...](https://www.marktechpost.com/2026/05/14/cline-releases-cline-sdk-an-open-source-agent-runtime-now-powering-its-cli-and-kanban-with-ide-extensions-being-migrated/) | 2026-05-14 | 2026-05-16 |
> | TestingCatalog — Nero Soares | Trade press (independent) | [cline-releases-open-source-agent-runtime-sdk](https://www.testingcatalog.com/cline-releases-open-source-agent-runtime-sdk-for-coding-agents/) | 2026-05-13 | 2026-05-16 |

## Key Insights

### 1. Architectural shift — harness as shared service, not single-product internal

Vendor-stated: *"the architecture that got us there was not the modular and extensible framework we would choose for what comes next... we abstracted our core agent harness into a plugable agent SDK"* and *"the runtime as a shared service, not just an implementation detail of a single product."* The extension UI, the CLI, and the (future) JetBrains plugin all consume the **same runtime**; the runtime is itself one of several products built on the SDK. This is the harness-extraction pattern visible elsewhere in the ecosystem ([[src-claude-agent-sdk-and-managed-agents|Claude Agent SDK]]; [[src-strands-agents-aws-intent-based-tool-design-96-percent-token-reduction|Strands Agents]]) — vendor product-as-app on top of a separately-evolving runtime, with the runtime made externally consumable.

### 2. Four-layer dependency-strict TypeScript stack

```
@cline/sdk            ← public surface, re-exports @cline/core
  └── @cline/core     ← Node runtime: sessions, storage, built-in tools, transports, scheduling, telemetry, plugin loading
      └── @cline/agents   ← browser-compatible stateless agent loop (iteration, tool orchestration, event emission)
          └── @cline/llms ← provider gateway: Anthropic, OpenAI, Google, AWS Bedrock, Mistral, LiteLLM, OpenAI-compat (vLLM/Together/Fireworks)
              └── @cline/shared ← types, schemas, tool helpers, hook contracts
```

Dependencies flow strictly downward; each layer has a single responsibility. Critical detail for embedding: **`@cline/agents` is browser-compatible** because it does not own session storage, built-in file/shell tools, or Node-specific orchestration. That means an LLM proxy can take just `@cline/llms`; a serverless or in-browser agent can take `@cline/agents + @cline/llms + @cline/shared` without dragging in the full Node runtime.

### 3. Empirical benchmark — harness ≥ +4.8 pp at constant model on Opus 4.7

> [!quote] Cline-published Terminal Bench 2.0 frontier-models table (pass@1)
>
> | Model | Cline CLI | Codex CLI | Droid | Claude Code |
> |---|---|---|---|---|
> | claude-opus-4.7 | **74.2%** | N/A | N/A | 69.4% |
> | claude-opus-4.6 | **71.9%** | N/A | 69.9% | 65.4% |
> | gpt-5.3-codex | 73.0% | 75.1% | 77.3% | N/A |
> | gemini-3.1-pro-preview | 57.3% | N/A | N/A | N/A |
> | gemini-3-flash-preview | 49.4% | N/A | N/A | N/A |
>
> Source: Cline-team runs on tbench.ai as of 2026-05-08. Anthropic's published Claude-Code-on-Opus-4.7 number (69.4%) is the reference point cited in [[src-anthropic-claude-opus-4-7-release-2026-04-16|Opus 4.7 release synthesis]] and [[2026-05-15-research-watch-opus-4-7-source-synthesis-shipped-end-to-end|the Opus 4.7 surfacing log]].

This is the second independent empirical confirmation of the [[harness-engineering-is-the-dominant-performance-lever|harness-engineering-is-dominant lesson]]: the +4.8 pp delta on identical model (claude-opus-4.7) is attributable purely to harness differences — prompts, loop, context management, error handling, tool exposure. Cline's open-weight numbers are even more striking (Cline 55.1% vs OpenCode 37.1% on kimi-k2.6 = +18 pp). **Caveat (P4-aspirational):** these are Cline-team-run pass@1 scores; independent reproduction by third parties is not yet published. Treat as vendor-favorable empirical anchor pending replication.

### 4. Native multi-agent / subagent primitives in core runtime

Subagents and agent teams live in `@cline/core` — not bolted on by a separate orchestration layer like LangGraph or CrewAI. The bundled plugin exposes tools for starting subagents, messaging them, reading status, and storing handoff notes. Each subagent gets its own model, tool set, and system prompt. This matches the [[src-philschmid-four-subagents-patterns-2026-inline-fanout-pool-teams|four-subagents-patterns]] taxonomy at the **teams** end and converges with the [[src-claude-managed-agents-dreaming-outcomes-multiagent-2026-05|Claude Managed Agents v2 dreaming/outcomes/multiagent]] direction Anthropic announced earlier this month. The pattern recurrence (≥3 vendors now ship native subagent primitives in the runtime, not as an external orchestrator) is approaching pattern-tier convergence floor.

### 5. Plugin architecture as harness extension contract

Plugins can register tools, observe lifecycle events, add rules and commands, and shape what the agent sees. They can start as a local `.ts`/`.js` module and graduate to a package directory with a `cline.plugins` manifest. Beyond plugins, the SDK exposes custom tools, MCP connectors, and skills as separate extensibility points. The pattern of **multiple extension contracts at different lifecycle points** (plugins for runtime behavior, MCP for tool/resource composition, skills for procedural knowledge) is now visible across Cline SDK, Claude Code, and Codex CLI ([[src-codex-cli-and-claude-code-plugin|Codex CLI Claude Code plugin]]) — convergent extension-surface taxonomy.

### 6. Provider-layer abstraction as substrate for multi-provider strategy

`@cline/llms` owns the provider gateway: Anthropic, OpenAI, Google, AWS Bedrock, Mistral, LiteLLM, and **any OpenAI-compatible endpoint** (vLLM, Together, Fireworks). Custom providers register via `registerProvider` / `registerModel`. Switching providers is *"a config change, not a code change"* — the agent loop never touches provider-specific code paths. This is the same abstraction shape as [[src-cloudflare-ai-platform-unified-inference-layer-12-providers-automatic-failover-2026-04-16|Cloudflare AI Platform's unified inference layer]] and the [[src-inference-provider-landscape-2026|inference provider landscape]] picture — provider as commodity at the harness/runtime boundary.

### 7. Sessions durable across surfaces — UI restart no longer kills work

Vendor-stated: *"long-running work no longer dies with a UI restart; sessions can move across surfaces."* The agent loop stays stateless (in `@cline/agents`) while the runtime (`@cline/core`) carries session lifecycle, persistence, transports. This is the **stateless-loop + durable-runtime split** — a deliberate separation that makes sessions a first-class portable object rather than UI state. Cron scheduling + checkpointing + web search + MCP connectors are native to `@cline/core`.

### 8. Connector channels — agents reachable via Telegram/WhatsApp/Slack

The new Cline CLI ships experimental connector channels: `cline connect` opens an interactive wizard to surface agents on messaging platforms. This converges with the [[src-openclaw-billing-proxy|OpenClaw multi-channel surface]] direction (Telegram/Signal/WhatsApp/iMessage adapters at the harness layer rather than at app layer) and is a stack-direct adjacency.

## Strategic Implications (this wiki's vision baselines)

### Operator-stack: Claude Code is daily harness; Cline SDK is now a credible peer

The operator stack runs Claude Code as the primary CLI harness. Cline CLI on Opus 4.7 = 74.2% vs Claude Code on Opus 4.7 = 69.4% on Terminal Bench 2.0 (pass@1, vendor-run). This is **harness-swap evidence** — same model, different harness, +4.8 pp. If the gap reproduces independently, it constitutes the strongest published harness-attributable performance delta to date. **Flag for [[ai-infrastructure-decision-framework-2026]] and [[ai-model-provider-harness-decision-matrix-2026]] update**: Cline CLI now warrants a row at parity with Claude Code (or above, on Opus benchmarks).

### Harness-engineering-is-dominant: second post-Cloudflare-style empirical anchor

The [[harness-engineering-is-the-dominant-performance-lever|DRAFT lesson]] cites mostly architectural and qualitative anchors. Cline SDK's published numbers add a **quantitative constant-model delta** to that lesson's evidence section. Combined with the [[src-poetiq-meta-system-automatic-harness-construction|Poetiq Meta-System single-harness-improves-every-model finding]] (per MarkTechPost adjacent article — not yet ingested), the harness-as-multiplier claim now has multiple independent empirical anchors. Pre-promotion floor still applies (≥3 convergent + operator decision).

### Open-source agent runtime tier — Cline SDK joins Claude Agent SDK + AGT mesh as candidates

The [[src-microsoft-agent-governance-toolkit-runtime-security-2026-04-02|Microsoft AGT]] release (governance substrate) and the [[src-claude-agent-sdk-and-managed-agents|Claude Agent SDK]] (Anthropic's runtime API) already exist in this corpus. Cline SDK adds a **third open-source agent-runtime substrate** — fully open under Apache 2.0, vendor-independent (unlike Claude Agent SDK), with native multi-agent primitives (unlike pure-policy AGT). The substrate-candidate question (cf. Q74/Q75/Q76 AGT cascade trio) now has a sibling-shape: *"Does OpenClaw / OpenArms / OpenFleet adopt Cline SDK as the agent-runtime substrate, or build its own?"* This is a candidate Q surface (see [[#promotion-candidates]] below).

### Cline CLI 2.0 as agent-orchestration peer to Claude Code

Cline CLI 2.0 (launched earlier in 2026, now rebuilt on the SDK) has TUI, agent teams, scheduled jobs, connectors. Compare to Claude Code: similar CLI-first agent surface, similar feature set, now better Terminal Bench numbers on Anthropic's own model. **Stack-strategic question**: is Cline CLI on Opus 4.7 now operator-preferable to Claude Code on Opus 4.7 for daily harness use? Not the agent's decision to make — flagged for operator awareness.

## Relationships

- **EXTENDS** [[src-cline-agentic-coding-ide-extension|Synthesis — Cline — Agentic Coding IDE Extension]] (2026-04-15) — same product family; this synthesis covers the 2026-05-13 SDK-extraction architectural shift, the prior covers the v3.55 IDE-extension capability set
- **EXTENDS** [[src-agentic-coding-harness-landscape-2026|Agentic Coding Harness Landscape 2026]] — adds Cline CLI 2.0 + Terminal Bench 2.0 numbers to the landscape table
- **CORROBORATES** [[harness-engineering-is-the-dominant-performance-lever|Lesson — Harness Engineering Is the Dominant Performance Lever]] — provides constant-model harness-swap delta (+4.8 pp Opus 4.7) as quantitative anchor
- **CONTRASTS** [[src-anthropic-claude-opus-4-7-release-2026-04-16|Claude Opus 4.7 release]] — Anthropic's published Claude-Code-on-Opus-4.7 number (69.4%) is the reference Cline CLI surpasses
- **PEERS** [[src-claude-agent-sdk-and-managed-agents|Claude Agent SDK]] — both are open-source-ish agent-runtime SDKs; Cline SDK is fully Apache-2.0 + vendor-independent
- **PEERS** [[src-strands-agents-aws-intent-based-tool-design-96-percent-token-reduction|Strands Agents (AWS)]] — peer agent-runtime SDK in the same release window
- **PEERS** [[src-microsoft-agent-governance-toolkit-runtime-security-2026-04-02|Microsoft Agent Governance Toolkit]] — different layer (governance vs runtime), composable rather than competing
- **RELATES TO** [[src-philschmid-four-subagents-patterns-2026-inline-fanout-pool-teams|Four Subagents Patterns]] — Cline SDK's native subagents land at the "teams" end of the taxonomy
- **RELATES TO** [[src-claude-managed-agents-dreaming-outcomes-multiagent-2026-05|Claude Managed Agents v2]] — converges on the runtime-native multi-agent primitives direction
- **RELATES TO** [[src-cloudflare-ai-platform-unified-inference-layer-12-providers-automatic-failover-2026-04-16|Cloudflare unified inference layer]] — same provider-abstraction pattern at runtime/harness boundary
- **RELATES TO** [[context-file-taxonomy|Context File Taxonomy]] — Cline SDK's plugin/MCP/skills extension surfaces extend the agent-context composition picture
- **RELATES TO** [[ai-infrastructure-decision-framework-2026]] — Cline CLI now warrants explicit consideration in the harness-selection matrix
- **RELATES TO** [[ai-model-provider-harness-decision-matrix-2026]] — Terminal Bench 2.0 + Cline CLI = new row + column candidate

## Open Questions

- **Independent replication of Cline CLI vs Claude Code on Opus 4.7.** Cline's 74.2% vs 69.4% is vendor-run pass@1. Anthropic, third-party benchmark sites (Artificial Analysis), or independent harness comparisons would convert this from "vendor-favorable empirical anchor" to "validated harness-attributable delta." Watch tbench.ai leaderboard for non-Cline runs.
- **Claude Code response.** Anthropic's harness team has visibility into Cline's numbers. Expected: prompt/tool-loop revisions in next Claude Code release. The harness-engineering competitive race is now on-the-record between two named products on the same benchmark.
- **OpenClaw / OpenArms / OpenFleet posture toward Cline SDK as substrate.** AGT cascade trio (Q74/Q75/Q76) decision-shape applies: adopt-as-substrate unless project can name a load-bearing differentiator. Cline SDK's Apache-2.0 + native multi-agent + provider-agnostic shape makes it a candidate substrate for OpenClaw's agent runtime layer.
- **Cline SDK skill (`npx skills add cline/sdk-skill`) interaction with three-layer context architecture.** Cline shipped a "skill" that gives Claude Code, Codex, or Cline itself full context on the SDK's APIs so it can scaffold agents — this is the [[src-skillmd-claudemd-agentsmd-three-layer-context|three-layer skill model]] applied to vendor-package-onboarding. Pattern to watch: vendor-shipped skills as the new "install our SDK" UX.

## Reference card

> [!info] Release card
>
> | Field | Value |
> |---|---|
> | Product | Cline SDK (`@cline/sdk`) |
> | Vendor | Cline Bot Inc. |
> | Author (blog) | Renee Huang |
> | Announced | 2026-05-13 |
> | License | Apache 2.0 |
> | Runtime | Node.js 22+ |
> | Layers (top→bottom) | `@cline/sdk` → `@cline/core` → `@cline/agents` → `@cline/llms` → `@cline/shared` |
> | Providers | Anthropic, OpenAI, Google, AWS Bedrock, Mistral, LiteLLM, any OpenAI-compatible endpoint (vLLM/Together/Fireworks) |
> | Headline benchmark | Cline CLI 74.2% vs Claude Code 69.4% on claude-opus-4.7 (Terminal Bench 2.0, pass@1, Cline-team-run, 2026-05-08) |
> | Open-weight headline | Cline CLI 55.1% on kimi-k2.6 vs OpenCode 37.1% (+18 pp) |
> | Install | `npm install @cline/sdk` · `npm i -g @cline` (CLI) · `npx skills add cline/sdk-skill` |
> | Docs | docs.cline.bot/sdk |
> | User base claim | 7M+ developers across Cline surfaces |

## Sources ingested

- `raw/articles/introducing-cline-sdk-the-upgraded-agent-runtime-and-we-rebuilt-cline-upon-it-cl.md` (Cline blog primary, 2026-05-13)
- `raw/articles/cline-releases-cline-sdk-an-open-source-agent-runtime-now-powering-its-cli-and-k.md` (MarkTechPost, 2026-05-14)
- `raw/articles/cline-releases-open-source-agent-runtime-sdk.md` (TestingCatalog, 2026-05-13)
