---
title: "Synthesis — Cavemem: Cross-Agent Persistent Memory for AI Coding Assistants (Julius Brussee, MIT-Licensed, Compressed-at-Rest SQLite + FTS5 + Vector Index + MCP Progressive Disclosure)"
aliases:
  - "Cavemem"
  - "Cavemem Synthesis"
  - "JuliusBrussee/cavemem"
  - "Cross-Agent Memory"
  - "Caveman Ecosystem Memory Layer"
type: source-synthesis
domain: tools-integration
layer: 1
status: synthesized
confidence: high
maturity: seed
created: 2026-05-04
updated: 2026-05-04
last_reviewed: 2026-05-04
sources:
  - id: cavemem-github
    type: repository
    url: https://github.com/JuliusBrussee/cavemem
    file: raw/articles/juliusbrusseecavemem.md
    title: "JuliusBrussee/cavemem — README + 13 deep-fetched files"
    description: "Authoritative open-source repository — MIT licensed, npm-distributed (`npm install -g cavemem`), supports Claude Code · Cursor · Gemini CLI · OpenCode · Codex. Ingested 2026-05-04 per Hard Rule 6 (corpus URL routes through `pipeline fetch`)."
    ingested: 2026-05-04
  - id: caveman-synth
    type: wiki
    file: wiki/sources/tools-integration/src-caveman-prompt-output-compressor-julius-brussee.md
    description: "Sister project — caveman (output token compressor). Same author, same caveman grammar, same intensity levels (lite/full/ultra). Cavemem reuses caveman's compression engine for memory at rest."
  - id: caveman-ecosystem
    type: documentation
    url: https://github.com/JuliusBrussee/cavekit
    description: "Sister project — cavekit (spec-driven autonomous build loop). Three-tool ecosystem composes: cavekit orchestrates the build · caveman compresses what the agent says · cavemem compresses what the agent remembers."
  - id: convergence-lesson
    type: wiki
    file: wiki/lessons/01_drafts/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md
    description: "Adjacent — cavemem operationalizes the cross-agent memory layer of the convergent pattern: persistent compressed memory across the 5 supported IDEs is what the convergent pattern's `progress-tracker.md` does in-tree, but at the agent-runtime layer."
  - id: trust-layer-concept
    type: wiki
    file: wiki/domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md
    description: "Adjacent — cavemem's compression-at-rest with technical-token preservation parallels the operator's trust-layer concept of cypher+decypher with technical-substance preservation. Different layer (memory at rest vs weights/context); same mechanism shape (compress + preserve technical substance + retrieve on demand)."
  - id: model-mcp-cli-integration
    type: wiki
    file: wiki/spine/models/ecosystem/model-mcp-cli-integration.md
    description: "Adjacent — cavemem is a strong empirical instance of MCP progressive disclosure (search/timeline compact → get_observations expanded). Saves ~10× tokens vs fetching full bodies upfront — concrete validation of the wiki's MCP-cli model claims."
  - id: cli-tools-beat-mcp-lesson
    type: wiki
    file: wiki/lessons/03_validated/tools-architecture/cli-tools-beat-mcp-for-token-efficiency.md
    description: "Adjacent validated lesson — cavemem cleverly composes BOTH: a CLI for setup/management AND an MCP server for agent-runtime memory access. Demonstrates the both-and pattern when each interface serves a different consumer."
tags: [source-synthesis, cavemem, julius-brussee, persistent-memory, cross-agent-memory, compression-at-rest, mcp-progressive-disclosure, caveman-ecosystem, sqlite, fts5, vector-search, hybrid-search, local-first, privacy-aware, claude-code, cursor, gemini-cli, opencode, codex, mit-licensed, layer-1, paper-evidence, mission-2026-05-04, operator-named-ecosystem]
---

# Synthesis — Cavemem: Cross-Agent Persistent Memory for AI Coding Assistants

## Summary

Cavemem ([JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem), MIT) is an open-source cross-agent persistent memory system that solves the AI-coding-assistant memory-loss problem with **compressed-at-rest local SQLite + FTS5 + vector index, exposed to agents via 4 MCP tools with progressive disclosure**. Hooks fire at editor session boundaries (Claude Code · Cursor · Gemini CLI · OpenCode · Codex), `<private>...</private>` content is redacted at the write boundary, observations are compressed via the same caveman grammar from [the sister project](src-caveman-prompt-output-compressor-julius-brussee.md) (~75% prose-token reduction with technical tokens — code blocks, URLs, paths, commands, version numbers — preserved byte-for-byte), and written synchronously to local SQLite. Agents query their own history through 4 MCP tools (`search` · `timeline` · `get_observations` · `list_sessions`) with **progressive disclosure**: compact results (IDs + snippets) until the agent asks for full bodies via `get_observations(ids[])` — saving ~10× tokens vs fetching upfront. **Local-by-default**: no network calls, hybrid BM25 (FTS5) + vector ranking, tunable blend via `search.alpha`. Embedding providers: local Transformers.js default, optional Ollama or OpenAI. Web viewer at `127.0.0.1:37777` for human-readable browsing. Performance: hook handlers <150ms p95, search <50ms p95 for ≤50K observations, compression ≥5MB/s on one core. Distribution: `npm install -g cavemem` then `cavemem install --ide <name>`. **In the caveman ecosystem**, cavemem composes: cavekit orchestrates the build · caveman compresses what the agent *says* · cavemem compresses what the agent *remembers*. Operator-named source 2026-05-04 (the second of three caveman-ecosystem tools the operator named on 2026-04-30).

## Reference Card

> [!info] Cavemem reference card

| Field | Value |
|---|---|
| **Repository** | [JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem) |
| **License** | MIT |
| **Author** | Julius Brussee |
| **Tagline** | *"why agent forget when agent can remember"* |
| **Distribution** | `npm install -g cavemem` (npm package) |
| **Type** | CLI + MCP server + hooks + local web viewer + worker daemon |
| **Supported IDEs** | Claude Code · Cursor · Gemini CLI · OpenCode · Codex (one-command install per IDE) |
| **Storage backend** | Local SQLite + FTS5 + vector index (no network, no cloud by default) |
| **Compression engine** | Same caveman grammar as [the sister project](src-caveman-prompt-output-compressor-julius-brussee.md) — lite / full / ultra intensity, technical tokens preserved byte-for-byte, round-trip guaranteed |
| **Memory write path** | Hook fires → redact `<private>` → compress prose → write to SQLite synchronously → embedding computed async via worker |
| **Memory read path (model)** | MCP `search`/`timeline` (compact) → `get_observations(ids[])` (full bodies, expanded by default) |
| **Memory read path (human)** | Web viewer at `http://127.0.0.1:37777` (read-only, expanded text) |
| **MCP tools (4)** | `search(query, limit?)` — BM25 + vector hybrid · `timeline(session_id, around_id?, limit?)` — chronological IDs · `get_observations(ids[], expand?)` — full bodies · `list_sessions(limit?)` — recent sessions |
| **Hybrid search blend** | `search.alpha` config — tunable BM25/cosine blend (default 0.5) |
| **Embedding providers** | local (Transformers.js default) · ollama · openai · none |
| **Privacy** | `<private>...</private>` stripped at write boundary · `privacy.excludePatterns` skips matching paths · worker binds to `127.0.0.1` only |
| **Performance budgets** | Hook handler p95 ≤150ms · `search` MCP p95 ≤50ms (≤50K observations) · compression ≥5MB/s · worker cold start ≤500ms (Node) / ≤100ms (Bun) |
| **Token-savings target** | ≥30% average · ≥40% at `full` · ≥55% at `ultra` (per docs) |
| **Auto-management** | Worker auto-spawns on first hook, self-exits when idle. No daemon on write path; hooks succeed even if worker is down (BM25 keeps working). |
| **Confidence** | high — README + CLAUDE.md + 11 deep-fetched files (architecture · compression spec · MCP contract · development workflow · lexicon JSON) read at L1 depth |
| **Mission relevance** | Critical — cavemem operationalizes the cross-session memory layer of the [2026 spec-driven convergent pattern](../../lessons/01_drafts/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md), and parallels the operator's trust-layer compression-at-rest mechanism at the memory layer (different scale, same shape) |

## Key Insights

> [!success] **Cross-agent persistent memory solves the named failure mode of AI coding assistants.**
>
> Per [JS Mastery's framing](src-jsmastery-six-file-context-system-agentic-build.md): *"The first few hours feel incredible, and then a week later, the agent has forgotten every decision you've made. One new feature breaks three others."* Cavemem's hooks capture observations at session boundaries; the SQLite store keeps them; agents query their own history at the start of new sessions via 4 MCP tools. **The memory persists across sessions AND across IDEs** (Claude Code session today, Cursor session tomorrow, OpenCode next week — same memory, queryable from any). This IS the cross-agent persistence the convergent pattern's `progress-tracker.md` does in-tree, but at the agent-runtime layer.

> [!success] **Compression-at-rest with technical-token preservation parallels the operator's trust-layer concept.**
>
> Cavemem's invariant: *"All persisted prose must pass through `packages/compress` before hitting storage. Writing raw prose to SQLite is a defect."* Code blocks, inline code, URLs, file paths, shell commands, version numbers, dates, numeric literals, and quoted identifiers are **preserved byte-for-byte** through the tokenizer in `packages/compress/src/tokenize.ts`. This is the same shape as the operator's [trust-layer concept](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md): compress + preserve technical substance + retrieve on demand. Cavemem operates at the memory-at-rest layer; the trust-layer concept operates at the weights/context layer; the structural mechanism is identical (compress + preserve + retrieve).

> [!success] **MCP progressive disclosure — concrete empirical evidence of the ~10× token-savings claim.**
>
> Per cavemem's docs/mcp.md: *"Following [the 3-layer pattern of `search` → review IDs → `get_observations`] saves ~10× tokens versus fetching full bodies upfront."* Three patterns make this work:
>
> 1. **Compact-first tools** — `search` and `timeline` return `[{id, score, snippet, session_id, ts}]`, NOT full content
> 2. **Filtered-fetch tool** — `get_observations(ids[])` fetches only what the agent decided it needs
> 3. **Default-expand for model** — full bodies expand to human-readable form by default; `expand: false` returns compressed form for agents that understand the caveman dialect directly
>
> This is concrete empirical validation of the [MCP-CLI model](../../spine/models/ecosystem/model-mcp-cli-integration.md)'s schema-overhead arguments. Progressive disclosure ≠ simply paginating; it's giving the agent the index *first* and the content *only on filtered request*.

> [!success] **Hybrid local-first search: BM25 (FTS5) + vector + tunable blend.**
>
> SQLite FTS5 keyword search runs always (BM25 ranking). Vector index runs when embeddings are available (local Transformers.js by default; remote ollama/openai opt-in). Hybrid ranking is tunable via `search.alpha` (BM25/cosine blend). **If the worker is down, BM25 still works** — the system degrades gracefully, never fails closed. This combines the strengths of [agentic search vs vector search](../../comparisons/agentic-search-vs-vector-search.md) — the false binary the wiki's existing comparison page resolves.

> [!success] **Privacy at the write boundary — not at retrieval.**
>
> Content inside `<private>...</private>` tags is stripped *before* the compressed observation is written. Paths matching `settings.excludePatterns` are never read. The worker binds to `127.0.0.1` only — no network exposure. **Privacy enforcement at write time is structurally stronger than retrieval-time filtering**: nothing private ever exists in the store; nothing can leak through query bugs because there's nothing to leak.

> [!info] **No daemon on write path — write hooks are synchronous, embedding is async.**
>
> Hooks invoke `MemoryStore.addObservation` directly through SQLite; no HTTP boundary, no IPC. Hook handler p95 ≤150ms. The worker (Hono on `127.0.0.1:37777`) is *only* for embedding backfill + read-only viewer. The worker auto-spawns on first hook and self-exits when idle. **Writes succeed even if the worker is down** — only semantic re-ranking degrades; BM25 keeps working. This is a clean architectural decision: the hot path (hook → write) has no shared dependency; the cold path (search re-ranking) is async and replaceable.

> [!info] **The caveman grammar IS the same engine as the sister project.**
>
> cavemem reuses `@cavemem/compress` from the same monorepo. Same intensity levels (`lite` / `full` / `ultra`). Same lexicon (fillers · articles · hedges · pleasantries · abbreviations · expansions). Same technical-token preservation tokenizer. **The caveman ecosystem's three tools (caveman · cavemem · cavekit) share a compression engine** — operationally one less thing to learn for an operator adopting any one of them.

## Architecture (verified from `docs/architecture.md` + `packages/*` layout)

> [!abstract] **Cavemem flow — compression at write, progressive disclosure at read**
>
> ```
> IDE ── hooks ──▶ CLI `hook run`
>                      │
>                      ▼
>               MemoryStore (core)
>             ┌──────────┴──────────┐
>             ▼                     ▼
>        compress (prose)      Storage (SQLite + FTS5 + embeddings)
>                                    ▲
>                                    │
> IDE ── MCP stdio ──▶ mcp-server ───┘
> Browser ── HTTP ──▶ worker (Hono) ─┘
> ```

**Monorepo layout** (pnpm workspaces; strict downward dependency direction):

| Layer | Purpose |
|---|---|
| `apps/cli` | User-facing binary (`cavemem` command) |
| `apps/worker` | Local HTTP daemon — read-only viewer + embedding backfill loop |
| `apps/mcp-server` | stdio MCP server (4 tools) |
| `packages/config` | Settings schema, loader, defaults, settingsDocs() |
| `packages/compress` | Compression engine + lexicon (shared with caveman ecosystem) |
| `packages/storage` | SQLite + FTS5 + vector adapter |
| `packages/core` | Domain models, MemoryStore facade, Embedder interface |
| `packages/embedding` | Provider factory (local · ollama · openai · none) |
| `packages/hooks` | Lifecycle hook handlers + worker auto-spawn |
| `packages/installers` | Per-IDE integration modules (Claude Code · Cursor · Gemini CLI · OpenCode · Codex) |
| `viewer/` | Vite + React read-only UI |
| `hooks-scripts/` | Portable shell stubs that invoke node handlers |
| `evals/` | Token-savings + round-trip harness |

Dependency direction: `config → compress → storage → { core · embedding } → hooks → installers`. No upward or sideways imports. All database I/O goes through `@cavemem/storage`. Settings access goes through `@cavemem/config`. **Every constraint is enforced by the package boundaries** — not by lint rules or convention prose.

## The Caveman Ecosystem — Composition

> [!info] Three tools. One philosophy: **agent do more with less.**

| Tool | What | Layer of operation |
|---|---|---|
| [**caveman**](src-caveman-prompt-output-compressor-julius-brussee.md) | Output compression skill | What the agent **says** (~75% output token reduction) |
| **cavemem** *(this synthesis)* | Cross-agent persistent memory | What the agent **remembers** (cross-session memory, compressed at rest) |
| **cavekit** | Spec-driven autonomous build loop | What the agent **does** (orchestration; spec-driven build) |

**They compose**: cavekit orchestrates the build · caveman compresses what the agent says · cavemem compresses what the agent remembers. Install one, some, or all — each stands alone. The shared `@cavemem/compress` engine means the three tools speak the same caveman grammar at every layer.

For the operator's stack, this matters because:
- The [trust-layer epic](../../backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md)'s 80–90% combined envelope already includes Caveman as the prompt-layer compression substrate. Cavemem extends that envelope to the cross-session memory dimension at no incremental tooling cost.
- The [Six-File Context System](src-jsmastery-six-file-context-system-agentic-build.md)'s `progress-tracker.md` is the in-tree per-project version of what cavemem does at the agent-runtime layer. They compose: the project keeps progress-tracker in version control; cavemem keeps cross-session observations as a runtime memory layer accessible across IDEs.

## Mission Alignment

Cavemem instantiates **multiple wiki principles + concepts simultaneously**:

| Wiki concept | Cavemem instance |
|---|---|
| [Markdown-as-IaC model](../../spine/models/agent-config/model-markdown-as-iac.md) | Settings file (`~/.cavemem/settings.json`) + per-IDE installer-generated config files are the binding configuration |
| [MCP-CLI Integration model](../../spine/models/ecosystem/model-mcp-cli-integration.md) | The both-and pattern: CLI for setup/management AND MCP for agent-runtime access — different consumers, same store |
| [Progressive disclosure](../../comparisons/agentic-search-vs-vector-search.md) | 3-layer search → IDs → fetch pattern; ~10× token savings empirically validated |
| [CLI tools beat MCP for token efficiency lesson](../../lessons/03_validated/tools-architecture/cli-tools-beat-mcp-for-token-efficiency.md) | Compose both: CLI for non-token paths, MCP for agent paths with progressive disclosure |
| [P1 — Infrastructure Over Instructions](../../lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md) | Compression invariant enforced at the package boundary (`MemoryStore.addObservation`), not at the prose-rule layer. Privacy enforced at write boundary, not via prose policy. |
| [P2 — Structured Context Governs Behavior](../../lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md) | The 4 MCP tools are structured context — schemas + return shapes — that the agent's runtime understands programmatically |
| [Spec-Driven Convergence Lesson](../../lessons/01_drafts/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md) | Cavemem's CLAUDE.md is itself a Six-File-style context file: project identity · non-negotiable rules · architectural rules · layout · workflow · gates · extension points |

**Trust-layer alignment** (operator's 2026-04-30 concept): cavemem's compression-at-rest with technical-substance preservation is structurally the same shape as the trust-layer's cypher+decypher with technical-token preservation. Different layer (memory vs weights/context); same mechanism (compress + preserve invariants + retrieve on demand). Both prove the operator's "seamless · blazing-fast · transparent · performance-positive" properties are achievable when the compression layer respects technical substance.

## Open Questions

> [!question] How does cavemem compose with the wiki's existing `wiki/log/` per-session logs?
> The wiki's current pattern: each session produces a verbatim raw note + a wiki/log/ session-log markdown. Cavemem's pattern: hooks compress observations into local SQLite at session boundaries. The two patterns serve adjacent purposes. Could the wiki's session logs be queryable via cavemem's MCP — making prior-session continuity a single MCP query instead of cat-the-handoff-file? Worth empirical evaluation.

> [!question] Cross-IDE memory — empirical operator validation pending.
> The README claims cross-IDE memory works (Claude Code session today, Cursor tomorrow, same memory). Operator's stack includes Claude Code + OpenCode + (potentially) Codex via Multica. Empirical confirmation that cavemem persists cleanly across the operator's actual IDE pattern would close a real gap.

> [!question] Performance budget under operator-actual workload.
> The README cites ≤150ms hook p95, ≤50ms search p95 for ≤50K observations. The operator's likely usage pattern (long sessions across multiple IDEs over weeks) could push observation counts past 50K. Empirical measurement on operator's stack would validate the budget.

> [!question] Privacy + the trust-layer concept.
> Cavemem strips `<private>` content at write boundary. The trust-layer concept operates at weights/context. Could a unified "private content" annotation flow from cavemem's `<private>` markup through the trust-layer's encryption substrate? They share the same operational concern (technical substance preserved, sensitive content protected) at different layers.

> [!question] Cavekit ingestion — completes the operator-named ecosystem.
> The third tool in the caveman ecosystem (cavekit — spec-driven autonomous build loop) remains uningested. Closing it would complete the operator-named ecosystem and surface whether cavekit's "natural language → kits → parallel build → verified" loop is the convergent pattern's authoritative tooling instance from the same author.

## How to Apply

> [!tip] Adoption checklist
>
> 1. **Install** — `npm install -g cavemem` then `cavemem install` (defaults to Claude Code) or `cavemem install --ide cursor|gemini-cli|opencode|codex` per IDE
> 2. **Verify** — `cavemem status` shows wiring + DB counts + embedding backfill + worker pid
> 3. **Open the viewer** — `cavemem viewer` opens `http://127.0.0.1:37777` in browser for human-readable session browsing
> 4. **Tune intensity** — `cavemem config set compression.intensity full` (or `lite` / `ultra`); default is `full`
> 5. **Configure privacy** — `~/.cavemem/settings.json` → `privacy.excludePatterns: [...]` for paths never to capture; use `<private>...</private>` markup inline for content never to persist
> 6. **Choose embedding provider** — `cavemem config set embedding.provider local` (default · Transformers.js · no network) OR `ollama` (local Ollama) OR `openai` (remote, opt-in)
> 7. **Verify cross-IDE persistence** — install in two IDEs (e.g., Claude Code + Cursor), generate observations in each, confirm `cavemem search <query>` returns from both
> 8. **Tune search blend** — `cavemem config set search.alpha 0.5` for hybrid; closer to 1.0 favors BM25, closer to 0.0 favors vector
> 9. **Audit at 7/30/90 days** — token-savings via `evals/` harness · search latency p95 · cross-IDE coverage · privacy boundary verified

## Relationships

- BUILDS ON: [[src-caveman-prompt-output-compressor-julius-brussee|Caveman Synthesis]] (sister project — shared `@cavemem/compress` engine and grammar)
- PARALLELS: [[src-jsmastery-six-file-context-system-agentic-build|JS Mastery Six-File Context System]] (cavemem's runtime memory layer parallels Six-File's `progress-tracker.md` in-tree memory layer; they compose, don't compete)
- BUILDS ON: [[model-mcp-cli-integration|Model — MCP and CLI Integration]] (concrete empirical instance of progressive disclosure with ~10× token savings claim)
- BUILDS ON: [[model-markdown-as-iac|Model — Markdown as IaC]] (settings + per-IDE installer-generated config files are the binding configuration substrate)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] (compression-at-rest invariant enforced at package boundary, not at prose-rule layer; privacy enforced at write boundary)
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Behavior]] (4 MCP tools with typed schemas program agent runtime behavior)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] (every CLAUDE.md invariant is verified by `pnpm typecheck && pnpm lint && pnpm test && pnpm build` — the 4 required gates)
- DEMONSTRATES: [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Convergence Lesson]] (cavemem's CLAUDE.md is itself a structured Six-File-style context file with non-negotiable rules · architectural rules · layout · gates · extension points — the wiki's convergent pattern in cavemem's own development)
- RELATES TO: [[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]] (compression-at-rest with technical-substance preservation parallels cypher+decypher with technical-token preservation at a different layer)
- RELATES TO: [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] (cavemem composes both patterns: CLI for setup, MCP for agent-runtime — each serves a different consumer with the right interface)
- RELATES TO: [[agentic-search-vs-vector-search|Agentic Search vs Vector Search Comparison]] (cavemem's hybrid BM25 + vector + tunable blend resolves the false binary in concrete production form)
- COMPARES TO: [[src-context-mode|Synthesis — Context Mode (MCP Sandbox for Context Saving)]] (adjacent — both solve cross-session continuity at the MCP layer with different design choices)
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (cavemem is a candidate addition to the consumer-stack memory dimension; runs locally on operator's RTX 3090 hardware with no incremental compute cost)

## Backlinks

[[src-caveman-prompt-output-compressor-julius-brussee|Caveman Synthesis]]
[[JS Mastery Six-File Context System]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[Model — Markdown as IaC]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[Principle 2 — Structured Context Governs Behavior]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[Spec-Driven Convergence Lesson]]
[[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]]
[[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
[[Agentic Search vs Vector Search Comparison]]
[[Synthesis — Context Mode (MCP Sandbox for Context Saving)]]
[[2026 Consumer Hardware AI Stack]]
