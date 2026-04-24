---
title: "Synthesis — Agentic Coding Harness Landscape 2026 (Claude Code, Codex, OpenCode, Aider, Cline, Cursor, Gemini CLI, Continue, Crush, Goose)"
aliases:
  - "Agentic Coding Harness Landscape 2026"
  - "Harness Alternatives 2026"
  - "Coding CLI Landscape"
type: source-synthesis
layer: 1
maturity: growing
domain: tools-and-platforms
status: synthesized
confidence: high
created: 2026-04-23
updated: 2026-04-23
sources:
  - id: artificialanalysis-agents-coding
    type: article
    url: https://artificialanalysis.ai/agents/coding
    title: "Coding Agents Comparison — Artificial Analysis"
    ingested: 2026-04-23
  - id: tembo-cli-tools-2026
    type: article
    url: https://www.tembo.io/blog/coding-cli-tools-comparison
    title: "The 2026 Guide to Coding CLI Tools: 15 AI Agents Compared — Tembo"
    ingested: 2026-04-23
  - id: morphllm-best-agents-2026
    type: article
    url: https://www.morphllm.com/best-ai-coding-agents-2026
    title: "14 Best AI Coding Agents in 2026: Ranked by Benchmarks and Real Usage"
    ingested: 2026-04-23
  - id: morphllm-alternatives
    type: article
    url: https://www.morphllm.com/comparisons/claude-code-alternatives
    title: "Claude Code Alternatives (2026): 11 Tested, 3 That Beat It for Under $20/mo"
    ingested: 2026-04-23
  - id: jock-harness-comparison
    type: article
    url: https://thoughts.jock.pl/p/ai-coding-harness-agents-2026
    title: "Claude Code vs Codex CLI vs Aider vs OpenCode vs Pi vs Cursor"
    ingested: 2026-04-23
  - id: aimultiple-agentic-cli
    type: article
    url: https://aimultiple.com/agentic-cli
    title: "Agentic CLI Tools Compared"
    ingested: 2026-04-23
tags: [harness, cli, agentic-coding, claude-code, codex, opencode, aider, cline, cursor, gemini-cli, continue, crush, goose, vendor-lock-in, resilience, 2026]
---

# Synthesis — Agentic Coding Harness Landscape 2026

## Summary

The agentic coding harness market in April 2026 has ~15 serious contenders. The operator's primary is **Claude Code**; the session now also has documented access to **Codex** via the plugin. But mission-resilience requires knowing the full landscape — **if Claude Code changes terms, pricing, or availability tomorrow, what replaces it**. This synthesis captures 10+ harnesses with their specific architectures (BYOM vs fixed-model, open-source vs commercial, CLI vs IDE vs cloud VM), pricing models, benchmark standings, and what each is uniquely best at. Not "here's a list" — here's **what to switch to under what trigger**. Mission posture: **Claude Code + Codex Plugin daily, OpenCode as immediate fallback (BYOM + Go + 75+ providers), Aider as efficient-tokens specialist, Cline for VS-Code-native work, Cursor for cloud-VM isolation, Gemini CLI for free-tier overflow**. None of these lock the operator in; every backend model the framework already documents works against at least 3 of these harnesses.

## Key Insights

> [!info] The harness layer is NOT coupled to the model layer
> Claude Code uses `ANTHROPIC_BASE_URL` to route to ANY Anthropic-compatible endpoint. OpenCode supports 75+ LLM providers natively. Aider is provider-agnostic. Cline is BYOM. The mission's "no vendor lock-in" applies at **both** layers: the harness you use AND the model you run inside it. Changing either is a config edit, not a migration.

> [!tip] The six BYOM harnesses (bring your own model) are the mission-resilient set
> **OpenCode, Aider, Cline, Kilo Code, Crush, Goose** are all free, open-source, and provider-agnostic. They run against Claude, GPT, K2.6, local Ollama, or anything OpenAI-API-compatible. If any single provider's pricing changes, you change the config — not the harness. If your subscription harness (Claude Code, Cursor) changes terms, you have immediate substitutes.

> [!warning] Harness-as-product vs harness-as-tool — two different bets
> Claude Code and Cursor are **product-harnesses**: opinionated UX, Anthropic/Cursor-controlled development cadence, subscription-tier pricing. OpenCode / Aider / Cline are **tool-harnesses**: open-source, config-driven, community cadence. Product-harnesses ship faster and polish the experience; tool-harnesses are resilient to provider decisions. Run both. Don't be surprised when a product-harness deprecates a feature you relied on — that's the product-harness tradeoff.

> [!abstract] Benchmark-leaders by task (2026 Q1-Q2 measurements)
>
> | Benchmark | Leader | Score |
> |---|---|---|
> | SWE-Bench Verified | Claude Code | 80.8% |
> | Terminal-Bench 2.0 | Codex CLI | 77.3% |
> | Runtime efficiency (balanced) | Aider | 52.7% combined, 257s, 126k tokens |
> | Best overall (but expensive) | Codex CLI | 67.7%, 426s, 258k tokens |
> | Most-adopted open-source IDE extension | Cline | 5M VS Code installs |
> | Most-starred open-source CLI | OpenCode | 95K+ GitHub stars |
> | GitHub commits/day written by the harness | Claude Code | ~135K (~4% of all public commits) |
> | Most generous free tier | Gemini CLI | Largest free allowance in the field |

## Deep Analysis

### The full landscape — 11 serious harnesses

| Harness | Type | Open-source? | BYOM? | Pricing | Benchmark standing | Unique strength |
|---|---|---|---|---|---|---|
| **Claude Code** | CLI + IDE (Anthropic) | No | Via `ANTHROPIC_BASE_URL` | $20/mo (Pro), $100/$200 (Max) | SWE-Bench 80.8% leader | Most complete harness; skills+hooks+plugins+subagents |
| **Codex CLI** (OpenAI) | CLI TUI | No | Via OpenAI-compat | OpenAI API rates (gpt-5.5 default) | Terminal-Bench 77.3% leader | Native `/codex:adversarial-review`, cloud tasks |
| **OpenCode** | CLI TUI (Go) | ✅ 95K stars | ✅ 75+ providers | Free (BYOM) | Strong across all | LSP integration, multi-session, session sharing links |
| **Aider** | CLI | ✅ | ✅ | Free (BYOM) | 52.7% balanced, 126k tokens (most efficient) | Token-efficient; best cost-per-task |
| **Cline** | VS Code extension + CLI | ✅ | ✅ | Free (BYOM); 5M installs | Strong for iterative review | Plan+Act dual modes; permission-per-file; parallel terminal agents (2.0) |
| **Continue** | IDE + CI CLI | ✅ | ✅ | Free | — | Pivoted to "AI checks in CI" pipelines |
| **Cursor 3** (April 2026) | IDE (Electron) | No | Limited | $20/mo | Strong, product-polished | Cloud agents on isolated VMs, `/worktree`, parallel Agent Tabs, self-hosted agents |
| **Gemini CLI** | CLI (Google) | No (free tier) | No (Gemini-only) | Most generous free tier | — | Free allowance unmatched |
| **Copilot CLI** (GitHub) | CLI | No | No | Via GitHub Copilot sub | — | Deep GitHub integration |
| **Crush** (Charm) | CLI TUI | ✅ | ✅ | Free | — | Terminal-beautiful UX; Charm ecosystem |
| **Goose** (Block) | CLI | ✅ | ✅ | Free | — | Multi-agent orchestration focus |
| **Amp** (Sourcegraph) | IDE | No | No | Ad-supported free | — | Codebase-wide context via Sourcegraph index |
| **Kilo Code** | VS Code fork | ✅ | ✅ | Free | — | Cline-derivative with its own direction |
| **Pi** (small, emerging) | CLI | ? | ✅ | Free | — | Experimental; worth tracking |

### Breakdown by what each is distinctively best at

**Claude Code** — best harness *product* in 2026. Skills + hooks + plugins + subagents + MCP all co-designed. The integration with its own model is tightest, but `ANTHROPIC_BASE_URL` lets the harness run against OpenRouter's endpoints or anything Anthropic-compatible (so you can use the Claude Code experience with K2.6). The mission-risk: Anthropic controls the cadence; if they change subscription tiers or harness features, you're along for the ride.

**Codex CLI + Codex Plugin for Claude Code** — best specialty-review tool. `/codex:adversarial-review` is documented-feature-level capability. The plugin bridges both product-harnesses so the operator doesn't leave Claude Code to invoke Codex commands. Uses OpenAI's gpt-5.5 by default; runs at OpenAI API rates.

**OpenCode** — best BYOM replacement if you had to stop using Claude Code tomorrow. 75+ providers means you can plug K2.6 via OpenRouter, GPT via OpenAI, local Ollama, or anything OpenAI-compat. Go binary (single executable). LSP integration auto-wires language servers. Multi-session support lets parallel agents work on the same repo. Closest-to-feature-parity open-source option to Claude Code/Cursor.

**Aider** — best token-efficiency tool. 257s avg runtime, 126k tokens per task, 52.7% benchmark score — the Pareto-optimal combination when you're billing per-token. Run Aider against K2.6 via OpenRouter for the cheapest real agentic coding per task.

**Cline** — best VS-Code-native experience for developers already in VS Code. 5M installs. Plan+Act explicit-permission model is a real differentiator for operators who want to preview changes. Parallel terminal agents in 2.0.

**Continue** — repositioned as CI-native. Less useful for interactive coding; more useful as a PR-review pipeline step. Niche but real.

**Cursor 3** — best when you want a polished IDE and cloud-isolated execution. $20/mo parallel with Claude Code. `/worktree` for branch isolation. 30% of Cursor's own PRs are agent-made (dog-fooding signal). Mission-risk: Cursor-only product; no BYOM swap.

**Gemini CLI** — best free-tier overflow. Google's generous free allowance means you can route experimental work here at zero marginal cost. Mission-cost: Google lock-in if it becomes primary.

**Copilot CLI** — only consider if you're already paying GitHub Copilot subscription. Otherwise the BYOM harnesses are cheaper and more flexible.

**Crush / Goose / Kilo Code / Pi** — community options worth tracking; Crush especially for its UX polish. None currently differentiate enough for operator-primary use but all are valid fallbacks.

### Resilience substitution matrix

The operator's daily stack (Claude Code + Codex plugin) — if either disappears tomorrow, what slots in?

| If this fails/changes | Immediate substitute | Why it works | Migration cost |
|---|---|---|---|
| Claude Code (Anthropic pricing/terms change) | **OpenCode** with K2.6 via OpenRouter | Go single binary, 75+ providers, closest feature parity, BYOM | ~1h — config the provider, recreate skills as SKILL.md files |
| Claude Code + prefer IDE | **Cursor 3** | Polished IDE product, cloud agents, parallel tabs | ~half day — learn new UX |
| Codex CLI (OpenAI pricing/outage) | **GPT via OpenRouter** or **Aider** with GPT models | Preserves adversarial-review-style work via prompting in a BYOM harness; loses the exact command semantics | Hours — write an "adversarial-review" skill in OpenCode or Claude Code that prompts the same 7 attack surfaces |
| OpenRouter (aggregator outage or pricing) | **Together AI** (175 models, own GPUs), **OpenAI direct**, **Moonshot direct**, **Groq** (speed-critical) | All provide Claude/GPT/K2.6 endpoints separately | Hours per swap |
| K2.6 discontinued by Moonshot | **GLM-4.7** (via Ollama Cloud), **DeepSeek v3** (via OpenRouter) | Both open-weight, comparable tier | Hours — change tier_map entry in AICP |
| All cloud unavailable / sovereignty | Local K2.6 via llama.cpp | 0.3 tok/s batch mode — usable for non-interactive | Already ready (technical milestone reached) |
| Need zero marginal cost experimentation | **Gemini CLI** free tier or **Cerebras** (1M tokens/day free) | Absorb prototyping overflow without provider lock | Free; change BYOM config |

**Design principle embedded:** nothing in this matrix requires operator hardware changes or multi-day migrations. Every substitution is a config edit + knowledge portability (skills → SKILL.md, agents → `.claude/agents/` — Agent Skills standard is cross-tool).

### Per-dimension leaders

| Dimension | Winner | Why |
|---|---|---|
| Overall product completeness | Claude Code | Skills + hooks + plugins + subagents + MCP all first-class |
| Open-source mission alignment | OpenCode | 95K stars, 75+ providers, active development |
| Token efficiency | Aider | 126k tokens per task (lowest among competent agents) |
| Speed | Depends on backend model — use Groq (315 tok/s) or Cerebras (~1000 TPS) |
| Free-tier generosity | Gemini CLI + Cerebras (1M tokens/day) |
| Parallel-agent orchestration | Cline 2.0 (parallel terminal agents) + Claude Agent SDK subagents |
| Cloud-VM isolation | Cursor 3 |
| Specialty code review | Codex CLI (`/codex:adversarial-review`) |
| CI pipeline integration | Continue |

## Cross-references

- [[src-claude-code-harness-features|Claude Code Harness Features]] — deep synthesis of the currently-primary harness
- [[src-codex-cli-and-claude-code-plugin|Codex CLI + Codex Plugin]] — specialty-review harness + plugin bridge
- [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] — economic context
- [[src-kimi-k2-6-moonshot-agent-swarm|Kimi K2.6 Synthesis]] — the default model that runs inside most of these harnesses

## State of Knowledge

| Claim | Verified? | Evidence |
|---|---|---|
| 15+ agentic coding tools in market 2026 | ✅ | Tembo + MorphLLM + ArtificialAnalysis |
| OpenCode has 95K+ GitHub stars, 75+ provider support, Go binary | ✅ | Multiple sources |
| Claude Code SWE-Bench Verified 80.8% | ✅ | MorphLLM + ArtificialAnalysis |
| Codex Terminal-Bench 2.0 77.3% | ✅ | MorphLLM 2026 ranking |
| Aider 52.7% combined, 126k tokens/task avg | ✅ | ArtificialAnalysis benchmark |
| Cline 5M VS Code installs + Plan/Act + parallel terminals 2.0 | ✅ | Tembo + AIMultiple |
| Cursor 3 released April 2026 with cloud agents on VMs + `/worktree` + parallel tabs | ✅ | Morph + Tembo |
| Gemini CLI most generous free tier | ✅ | Tembo + AwesomeAgents |
| 135K/day Claude Code commits (~4% of public GitHub) | ✅ | MorphLLM + 2026 data |
| All BYOM harnesses (OpenCode, Aider, Cline, Kilo, Crush, Goose) are free | ✅ | Multiple sources |
| Codex subscription (via ChatGPT) vs BYOM-free | ✅ | Tembo |

## Relationships

- BUILDS ON: [[src-claude-code-harness-features|Synthesis — Claude Code Harness Features]]
- BUILDS ON: [[src-codex-cli-and-claude-code-plugin|Synthesis — Codex CLI + Plugin]]
- FEEDS INTO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] — adds the harness-substitution dimension to the framework's resilience story
- RELATES TO: [[src-kimi-k2-6-moonshot-agent-swarm|Synthesis — Kimi K2.6]] — the default model that most of these harnesses run against
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] — the mission-resilience claim "we are not vendor-locked" is verified by the existence of BYOM substitutes with documented feature sets, not asserted

## Backlinks

[[Synthesis — Claude Code Harness Features]]
[[Synthesis — Codex CLI + Plugin]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[Synthesis — Kimi K2.6]]
[[Principle 4]]
