---
title: Claude Code Context Management
aliases:
  - "Claude Code Context Management"
type: concept
layer: 2
maturity: growing
domain: ai-agents
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-10
sources:
  - id: src-shanraisshan-claude-code-best-practice
    type: documentation
    url: https://github.com/shanraisshan/claude-code-best-practice
    file: raw/articles/shanraisshanclaude-code-best-practice.md
    title: shanraisshan/claude-code-best-practice
    ingested: 2026-04-08
  - id: src-token-hacks-claude-code
    type: youtube-transcript
    url: https://www.youtube.com/watch?v=49V-5Ock8LU
    file: raw/transcripts/18-claude-code-token-hacks-in-18-minutes.txt
    title: 18 Claude Code Token Hacks in 18 Minutes
    ingested: 2026-04-08
tags: [claude-code, context-window, token-management, CLAUDE-md, compact, prompt-caching, MCP-overhead, cost-optimization, memory, context-engineering]
---

# Claude Code Context Management

## Summary

Context management in Claude Code is the discipline of controlling what occupies the model's limited context window to maximize both output quality and session longevity. Every message re-reads the entire conversation history, CLAUDE.md files, MCP server definitions, system prompts, skills, and referenced files — making costs compound geometrically, not linearly. A developer tracking a 100+ message session found 98.5% of tokens were spent re-reading old history. The discipline spans three concerns: reducing invisible overhead (lean CLAUDE.md, disconnecting unused MCPs, controlling command output), managing session lifecycle (fresh conversations, manual compaction at 60%, strategic clearing before breaks), and making costs visible (/context, /cost, status line). The "lost in the middle" phenomenon — where models attend most strongly to beginning and end of context — means bloated context degrades quality in addition to increasing cost.

> [!info] Context Budget Reference Card
>
> | Threshold | Value | Source |
> |-----------|-------|--------|
> | Baseline overhead (one dev's setup) | ~51,000 tokens before first message | src-shanraisshan |
> | MCP server per-message cost | up to 18,000 tokens each | src-token-hacks |
> | Message 1 vs message 30 cost | ~500 vs ~15,000 tokens (31x) | src-shanraisshan |
> | 30-message cumulative consumption | ~250,000 tokens | calculated |
> | Manual compaction threshold | 60% context utilization | src-token-hacks |
> | Quality degradation markers | 40%, 60%, 80% (probabilistic) | src-accuracy-tips |
> | Compactions before quality loss | 3–4 consecutive | src-token-hacks |
> | Prompt cache TTL | ~5 minutes (unverified by Anthropic) | src-token-hacks |
> | CLAUDE.md size heuristic | <200 lines (real metric: tokens/message) | src-shanraisshan |
> | Sub-agent overhead multiplier | 7–10x vs single-agent | src-token-hacks |

## Key Insights

### Cost Mechanics — Where Tokens Go

> [!warning] Geometric compounding is the fundamental cost driver
> Every message re-reads all prior messages plus their responses. This is not linear addition — it is geometric growth. Message 1 ≈ 500 tokens. Message 30 ≈ 15,000 tokens (31x more). After 30 messages, cumulative consumption approaches 250,000 tokens. Long conversations are vastly more expensive per-token of useful output than fresh ones.

> [!warning] Invisible overhead consumes context before you start
> Before a single word of conversation, one developer measured ~51,000 tokens consumed by system prompts, tools, agents, skills, and memory files (actual baseline varies by configuration). MCP servers add more — a single server can cost 18,000 tokens per message, loaded invisibly on every turn. The total invisible overhead can represent a significant fraction of the context window before any work begins.

**CLAUDE.md as hot path.** CLAUDE.md is re-read on every message, making it the single most impactful factor in per-message overhead. Keep it under 200 lines. Treat it as an index/router, not an encyclopedia. Use `.claude/rules/` to split infrequent instructions. Wrap critical rules in `<important if="...">` tags. Every line in CLAUDE.md is multiplied by the total number of messages in every session.

**MCP servers compound silently.** Every connected MCP server loads all tool definitions on every message regardless of whether those tools are used. Disconnect unused servers at session start via `/mcp`. Prefer CLIs over MCPs where possible — the emerging consensus in 2026 is that CLI+Skills is cheaper and more accurate for project-internal tooling.

**Command output enters context.** When Claude runs shell commands, the full output (git log with 200 commits, verbose build output) enters the context as tokens. Deny permissions for noisy commands in specific projects. Be intentional about what Claude is allowed to run.

### Session Lifecycle — The Three Phases

> [!tip] A well-managed session has three phases
>
> | Phase | Context % | Action |
> |-------|-----------|--------|
> | **Fresh** | 0–40% | Most productive. Context is clean, attention is distributed. Do your hardest work here. |
> | **Managed** | 40–60% | Strategic compaction. Run `/compact` with specific instructions about what to preserve. |
> | **Transition** | 60%+ or 3–4 compacts | Session handoff. Get a summary, `/clear`, feed summary into fresh session. |

**Manual compaction at 60%, not 95%.** Auto-compact triggers at 95% capacity, by which point context is already degraded from lost-in-the-middle effects. The recommendation is `/compact` at 60% with explicit instructions about what to preserve. After 3–4 consecutive compactions, quality degrades noticeably — transition to a fresh session at that point.

**Prompt cache TTL matters for breaks.** Claude Code caches prompt context to avoid reprocessing, but the cache expires after ~5 minutes of inactivity (unverified by Anthropic). A 4-minute break is cheap; a 6-minute break reprocesses everything from scratch. Either compact before stepping away or plan breaks to be preceded by a context management step.

**Batch prompts to reduce re-reads.** Three separate messages cost roughly 3x what one combined message costs because each triggers a full context re-read. Combine related instructions. If Claude makes a small error, editing the original message and regenerating replaces the bad exchange entirely — a follow-up correction stacks permanently onto history.

### Quality Degradation — Why Context Bloat Is Not Just a Cost Problem

> [!abstract] Lost in the middle: quality degrades, not just cost
> Research shows models attend most strongly to the beginning and end of the context window, with reduced attention to content in the middle. This means a long conversation is not just more expensive — the middle sections actively produce worse output. One practitioner reported rough degradation markers at 40%, 60%, 80% context utilization (probabilistic, not deterministic). Fresh conversations with relevant context always outperform continuing a bloated session.

### Operational Controls

> [!tip] Visibility and cost management
>
> | Tool | What it shows |
> |------|---------------|
> | `/context` | Breakdown by component: history, CLAUDE.md, MCP overhead, loaded files |
> | `/cost` | Actual token usage and estimated spend |
> | Status line | Continuous ambient awareness: model, context %, token count |
> | Usage dashboard | Remaining allocation and reset time |

**Model selection as cost control.** Sonnet for default coding, Haiku for sub-agents and simple formatting, Opus only for deep architectural planning when Sonnet is insufficient (keep under 20% of usage). Sub-agents cost 7–10x more tokens than single-agent sessions because each spawns with its own full context reload.

**Peak hour awareness.** The session window drains faster during peak hours (8 AM – 2 PM Eastern weekdays). Schedule heavy refactors and multi-agent work for off-peak hours.

## Deep Analysis

Context management is the meta-discipline that governs all agent productivity. It is not one skill among many — it is the skill that determines the economics, accuracy, and longevity of every other skill. A developer who practices context hygiene gets 3–5x more useful work per session, not by working harder but by reducing the geometric growth of token consumption.

The deeper insight is that **every Claude Code design decision is implicitly a context management decision.** Choosing MCP vs CLI? Context cost. Writing CLAUDE.md? Per-message overhead. Spawning sub-agents? 7–10x context duplication. Creating skills? Deferred loading profile. Deciding when to compact? Session lifecycle design. The developers who get the most out of Claude Code are the ones who internalize this: context is not a technical constraint to work around — it is the fundamental resource that all other optimizations must be expressed in terms of.

The connection to the LLM Wiki Pattern makes this concrete. The wiki approach — structured markdown with indexes, no vector databases — is itself a context management strategy. By pre-organizing knowledge into navigable structures, the wiki reduces context needed per query compared to dumping raw documents into conversation. CLAUDE.md-as-index is the same pattern applied to the agent's own configuration. This wiki's CLAUDE.md demonstrates the principle: it routes to subsystems rather than documenting them inline, keeping per-message overhead proportional to the routing table rather than the total knowledge base.

The compaction lifecycle reveals something non-obvious: **context management is temporal engineering.** The same content has different value at different points in a session. An initial decision that needs to be referenced throughout should survive compaction. A debugging tangent that resolved 20 messages ago should be compressed. The `/compact` command with specific preservation instructions is not just housekeeping — it is the primary tool for shaping what the model attends to going forward. After 3–4 compactions, even carefully preserved context degrades from successive lossy compression, which is why session handoff (summary → clear → fresh session) is not a failure state but a planned transition.

### This Wiki as Practitioner Instance

> [!example]- How this wiki practices context management
>
> | Practice | Implementation |
> |----------|---------------|
> | CLAUDE.md as router | Routes to subsystems, ~230 lines, structured as table of contents |
> | Deferred loading | Skills (wiki-agent, model-builder, evolve) load on invocation, not at startup |
> | MCP with CLI fallback | 17 MCP tools registered for discoverability; all have CLI equivalents via `tools/pipeline` |
> | Pipeline offloading | Lint, validate, manifest — run as separate processes, not in conversation context |
> | Session artifacts | `docs/SESSION-*.md` files capture state for cross-session handoff |
> | Sub-agent scoping | Parallel sub-agents for independent model elevation; main context stays clean |
> | Batch ingestion | `pipeline chain ingest` sequences sources; 3–5 complex transcripts or 8–12 articles per session before compact |

## Open Questions

> [!question] ~~Can the prompt cache TTL be extended or configured?~~
> **RESOLVED:** No — Anthropic API parameter, not user-configurable. Current TTL is 5 minutes. Design around it.
> Requires: Anthropic API documentation or official Claude Code settings documentation. The 5-minute TTL is reported by one practitioner source, unverified by Anthropic.

> [!question] ~~How do economics change across subscription plans?~~
> **RESOLVED:** Same practices regardless of plan. Budget changes headroom, not technique. Context management equally important at $20 and $200.
> Is context management equally important on the $200/month plan as on the $20/month plan? Requires: Anthropic subscription documentation with per-plan token allocation details.

## Answered Open Questions

> [!example]- Quality degradation curve — sharp knees or gradual decline?
> Cross-referencing `Synthesis: Claude Code Accuracy Tips`: the degradation curve has identifiable thresholds, not a smooth gradient. One practitioner reported rough markers at 40%, 60%, 80% — but degradation is probabilistic, not deterministic. This is a step-function pattern with knees rather than a smooth slope. Practical implication: `/clear` before 50% to stay in the reliable zone. The Context-Aware Tool Loading pattern page confirms: "observed by one practitioner to degrade at higher utilization (rough markers at 40%, 60%, 80% reported — probabilistic, not deterministic)."

> [!example]- Optimal CLAUDE.md size — 200 lines, or something else?
> The real metric is per-message token overhead, not line count. A 200-line CLAUDE.md of dense prose costs more per message than 200 lines of concise bullets. The correct mental model: CLAUDE.md is charged on every message — the question is not "how many lines?" but "how many tokens per message, and does each element earn that cost across the session?" The 200-line heuristic is a practical proxy. The real ceiling is whatever token count keeps overhead below the signal value of having that information available on every turn.

> [!example]- Does compaction fix lost-in-the-middle?
> Yes, partially. `/compact` with specific instructions rewrites the conversation summary to place key facts prominently at the beginning of the condensed history. This means the compacted summary's early portion receives full beginning-of-context attention weight. However, after 3–4 compactions, successive lossy compression degrades even this benefit — which is why the recommendation transitions to fresh-session handoff with a manually authored summary (giving full control over what occupies high-attention positions).

> [!example]- Can you profile per-message token cost by component?
> The `/context` command is the primary breakdown tool — it decomposes active context by component. The status line provides continuous total-context monitoring. To measure individual MCP server overhead: compare `/context` output with vs. without specific servers connected. The Context-Aware Tool Loading pattern documents the wiki's own observation: "three planned MCP servers each with 6-8 tools — the cumulative schema payload consumes meaningful context budget on every single turn."

> [!example]- How does wiki linting interact with context limits?
> Resolution: deferred loading, not broad pre-loading. Linting's broad-read requirement conflicts with context management's narrow-read requirement. The wiki resolves this by treating linting as a pipeline operation (`tools/lint.py` via manifest diffing for incremental runs, separate process or sub-agent) rather than an in-conversation operation. This prevents lint token cost from contaminating the primary task context window.

> [!example]- Optimal batch sizes for wiki ingestion?
> Not a fixed number — it is the number of sources processable before reaching the 60% compaction threshold. Given ~51K baseline overhead (varies by setup) and ~15K per complex source synthesis: roughly 3–5 complex transcripts or 8–12 shorter articles per session before compacting or transitioning. Sub-agents receive fresh context per task, making them the correct architecture for batch processing. The wiki's `pipeline chain ingest` sequences rather than loading all sources into one session.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[src-shanraisshan-claude-code-best-practice|Synthesis — Claude Code Best Practice (shanraisshan)]]
- DERIVED FROM: [[src-token-hacks-claude-code|Synthesis — 18 Claude Code Token Hacks in 18 Minutes]]
- BUILDS ON: [[claude-code-skills|Claude Code Skills]]
- BUILDS ON: [[claude-code-best-practices|Claude Code Best Practices]]
- RELATES TO: [[llm-wiki-pattern|LLM Wiki Pattern]]
- RELATES TO: [[memory-lifecycle-management|Memory Lifecycle Management]]
- RELATES TO: [[wiki-knowledge-graph|Wiki Knowledge Graph]]
- CONSTRAINS: [[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
- CONSTRAINS: [[llm-knowledge-linting|LLM Knowledge Linting]]
- RELATES TO: [[skills-architecture-patterns|Skills Architecture Patterns]]
- EXTENDS: [[claude-code|Claude Code]]

## Backlinks

[[src-shanraisshan-claude-code-best-practice|Synthesis — Claude Code Best Practice (shanraisshan)]]
[[src-token-hacks-claude-code|Synthesis — 18 Claude Code Token Hacks in 18 Minutes]]
[[claude-code-skills|Claude Code Skills]]
[[claude-code-best-practices|Claude Code Best Practices]]
[[llm-wiki-pattern|LLM Wiki Pattern]]
[[memory-lifecycle-management|Memory Lifecycle Management]]
[[wiki-knowledge-graph|Wiki Knowledge Graph]]
[[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
[[llm-knowledge-linting|LLM Knowledge Linting]]
[[skills-architecture-patterns|Skills Architecture Patterns]]
[[claude-code|Claude Code]]
[[agent-orchestration-patterns|Agent Orchestration Patterns]]
[[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
[[context-aware-tool-loading|Context-Aware Tool Loading]]
[[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
[[design-md-pattern|Design.md Pattern]]
[[model-claude-code|Model — Claude Code]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[never-present-speculation-as-fact|Never Present Speculation as Fact]]
[[src-claude-code-accuracy-tips|Synthesis — Claude Code Accuracy Tips]]
[[src-context-mode|Synthesis — Context Mode — MCP Sandbox for Context Saving]]
[[src-playwright-cli-vs-mcp|Synthesis — Playwright CLI vs MCP — Automate QA with Less Tokens]]
[[src-playwright-mcp-visual-testing|Synthesis — Playwright MCP for Visual Development Testing]]
