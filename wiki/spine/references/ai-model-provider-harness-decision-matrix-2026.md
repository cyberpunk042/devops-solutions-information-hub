---
title: "AI Model × Provider × Harness Decision Matrix 2026"
aliases:
  - "AI Model × Provider × Harness Decision Matrix 2026"
  - "AI Decision Matrix 2026"
  - "Model-Provider-Harness Matrix"
  - "Unified AI Stack Lookup"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
priority: P0
created: 2026-04-23
updated: 2026-04-23
sources:
  - id: ai-infra-framework-2026
    type: wiki
    file: wiki/spine/references/ai-infrastructure-decision-framework-2026.md
    description: "Parent vision doc — this matrix operationalizes its Specialty Routing + Resilience Playbook sections as a single-page lookup table"
  - id: harness-landscape
    type: wiki
    file: wiki/sources/tools-integration/src-agentic-coding-harness-landscape-2026.md
    description: "11+ harnesses with BYOM-vs-product split"
  - id: provider-landscape
    type: wiki
    file: wiki/sources/tools-integration/src-inference-provider-landscape-2026.md
    description: "10+ inference providers with verified 2026 pricing"
  - id: k2-6-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-kimi-k2-6-moonshot-agent-swarm.md
    description: "K2.6 details for the default agentic model"
  - id: openrouter-glm-4-7
    type: api-documentation
    url: https://openrouter.ai/z-ai/glm-4.7
    title: "GLM 4.7 — API Pricing & Providers | OpenRouter"
    ingested: 2026-04-23
  - id: deepseek-pricing
    type: api-documentation
    url: https://pricepertoken.com/pricing-page/provider/deepseek
    title: "DeepSeek API Pricing (2026)"
    ingested: 2026-04-23
  - id: llm-stats-deepseek
    type: article
    url: https://llm-stats.com/models/deepseek-v3
    title: "DeepSeek-V3 Pricing, Benchmarks & Performance"
    ingested: 2026-04-23
  - id: aicp-model-ecosystem-full-map
    type: documentation
    project: aicp
    path: docs/MODEL-ECOSYSTEM-FULL-MAP-2026-04-24.md
    file: raw/articles/aicp-model-ecosystem-full-map-2026-04-24.md
    description: "AICP's verified provider-pricing map (companion source)"
tags: [reference, p0, decision-matrix, ai-models, providers, harnesses, k2-6, gpt-5, opus, glm-4-7, deepseek, gemini, resilience, routing, 2026]
---

# AI Model × Provider × Harness Decision Matrix 2026

## Summary

Single-page lookup to pick (harness, model, provider) triples for any workload. The framework defines WHY; this matrix defines WHAT EXACTLY. Built from verified 2026 pricing (OpenRouter live, AICP 2026-04-24 session) across **10+ models × 8+ providers × 12+ harnesses**. Updated quarterly — see [[ai-infrastructure-decision-framework-2026|parent framework]] § Price-Monitoring. **Breakthrough finding**: GLM 4.7 at $0.38/$1.74 is 2× CHEAPER than K2.6 on output while scoring 73.8% SWE-Bench Verified — and **DeepSeek V3 at $0.28/$0.42 is cheaper still**. The K2.6 mission-anchor doesn't have to be single-source; there are now multiple mission-aligned open-weight options at different price points, and the resilience playbook's "if K2.6 is unavailable" answer is **concrete** rather than aspirational.

## The Master Matrix — Models × Capability × Cost

> [!abstract] Models ranked by cost-per-output-token (open-weight first, then closed)
>
> | Model | $USD/M in | $USD/M out | Context | SWE-Bench Pro / Verified | Best available via | Mission | Strengths |
> |---|---:|---:|---:|---|---|---|---|
> | **DeepSeek V4-Flash** | **$0.14** | **$0.28** | **1.05M** | TBD | OpenRouter (verified), DeepSeek direct | ✅ open-weight | **Cheapest coding-capable; 1M context; floor price** |
> | **DeepSeek V3.2** | $0.252 | **$0.378** | 131K | 73.1% Verified (V3.2-Speciale) | OpenRouter (verified), DeepSeek direct | ✅ open-weight | V3-tier current; coding+math |
> | **GLM 4.7 Flash** | **$0.06** | $0.40 | 203K | — (smaller) | OpenRouter (verified), Ollama Cloud | ✅ open-weight | Cheapest input; light/bulk tasks |
> | **DeepSeek Chat V3.1** | $0.15 | $0.75 | 33K | — | OpenRouter (verified), DeepSeek direct | ✅ open-weight | V3 chat variant — short-context cheap |
> | **GLM 4.7** | $0.38 | **$1.74** | 203K | 73.8% Verified | OpenRouter (verified), Ollama Cloud, Z.ai direct | ✅ open-weight | Strong coding tier, cheap output |
> | **gpt-5.1-codex-mini** | $0.25 | $2.00 | 400K | Strong coding | OpenAI direct, OpenRouter (verified) | ❌ closed (specialty) | Cheapest closed coding tier |
> | **DeepSeek V4-Pro** | **$1.74** | **$3.48** | **1.05M** | **80.6% Verified** (= Opus 4.6) | OpenRouter (verified), DeepSeek direct | ✅ open-weight | Opus-class at 1/7 Opus cost, 1M context |
> | **Kimi K2.6** | **$0.745** | **$4.655** | 256K | **58.6 Pro** (leads), 80.6% Verified (est.) | OpenRouter (verified), Ollama Cloud, Moonshot direct, local | ✅ open-weight | Agentic frontier, 300-agent swarm |
> | **gpt-5 / 5.1 / 5.1-codex** | $1.25 | $10.00 | 400K | Strong | OpenAI direct, OpenRouter (verified) | ❌ closed | Codex CLI native; general GPT tier |
> | **Gemini 2.5 Pro** | $1.25 | $10.00 | 1.05M | — | Google direct, OpenRouter (verified) | ❌ closed (specialty) | Long-context + Gemini ecosystem |
> | **Gemini 3.1 Pro Preview** | $2.00 | $12.00 | 1.05M | — | Google direct, OpenRouter (verified) | ❌ closed (specialty) | Multimodal SOTA + 1M context |
> | **gpt-5.4** | $2.50 | $15.00 | 1.05M | — | OpenAI direct, OpenRouter (verified) | ❌ closed (specialty) | Long context (1M+) specialty |
> | **Claude Opus 4.6/4.7** | **$5.00** (OR) | **$25.00** (OR) | **1M** (4.7) | High | **Anthropic direct ~$15/$75**, OpenRouter ~$5/$25 (verified) | ❌ closed (specialty) | Creative-technical synthesis + tone |
> | **gpt-5.4-pro** | $30 | $180 | 1.05M | — | OpenAI direct | ❌ closed (rare use) | Premium ceiling — reserve for edge cases |
>
> **All prices on this row verified from OpenRouter `/api/v1/models` endpoint 2026-04-23** — cached at [wiki/config/provider-pricing-cache.json](../../config/provider-pricing-cache.json). Re-verify with `python3 -m tools.pipeline provider-check`.
>
> **Corrections surfaced by this verification pass:**
> - **K2.6 on OpenRouter is $0.745/$4.655**, not $0.80/$3.50. Output ~33% higher than earlier citations suggested.
> - **Opus 4.6/4.7 on OpenRouter is $5/$25**, not $15/$75 (direct). OpenRouter is **3× cheaper for Opus** — Opus specialty tasks cost substantially less than the framework previously estimated.
> - **DeepSeek V4-Pro is $1.74/$3.48** — better than my earlier "~$3.48 output" framing (input is also cheap). At $1.74/$3.48, Opus-class coding capability is **20× cheaper** than Claude Opus direct ($15/$75).
> - **DeepSeek V4-Flash** ($0.14/$0.28) **is now the cost floor** for coding-capable models — cheaper than K2.6, GLM 4.7 Flash output, and every closed-weight model. 1M context.
> - **Gemini 2.5 Pro** ($1.25/$10) is 17% cheaper than Gemini 3.1 Pro Preview ($2/$12) — for long-context work not needing the very latest Gemini, use 2.5.
>
> **Key insight**: SEVEN open-weight models now occupy the $0.28-$4.655 per M output range — **five of them cheaper than K2.6**. K2.6 remains best-on-agentic-frontier but is no longer the cheapest viable coder. The practical routing rule: **match workload to tier, not "always K2.6."** DeepSeek V4-Flash covers most routine coding at a fraction of K2.6 cost with 4× the context window.

## Provider × Model Availability Matrix

> [!tip] Where each mission-relevant model runs — with an ✅ meaning "verified active access path"
>
> | Model \\ Provider | OpenRouter | Ollama Cloud | Together AI | Groq | Cerebras | Direct | Local |
> |---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> | **DeepSeek V3** | ✅ | — | ✅ | possibly | — | ✅ DeepSeek | ✅ (Q2 GGUF) |
> | **GLM 4.7 / Flash** | ✅ | ✅ | possibly | — | — | ✅ Z.ai | possibly (via Unsloth) |
> | **Kimi K2.6** | ✅ | ✅ | — | — | — | ✅ Moonshot | ✅ (Q2, 0.3 tok/s) |
> | **DeepSeek V4-Pro** | ✅ | possibly | possibly | — | — | ✅ DeepSeek | — (too large) |
> | **gpt-5.x family** | ✅ | ❌ (proprietary) | ❌ | possibly | — | ✅ OpenAI | — (closed-weight) |
> | **Claude Opus / Sonnet** | ✅ | ❌ (proprietary) | ❌ | ❌ | ❌ | ✅ Anthropic | — (closed-weight) |
> | **Gemini 3.1 Pro** | ✅ | ❌ (proprietary) | ❌ | ❌ | ❌ | ✅ Google | — (closed-weight) |
> | **Llama 3.3 70B** | ✅ | ✅ | ✅ | **315 TPS** | **~1000 TPS** | Meta direct | ✅ |
> | **Qwen3 family (local)** | ✅ | possibly | ✅ | — | — | Alibaba direct | ✅ (operator has) |
> | **gpt-oss / open-weight GPT** | ✅ | possibly | ✅ | ✅ | — | — | ✅ |
>
> **Substitution reading**: pick a row (model), scan across for active columns. Each ✅ is a path you can activate if another goes down.
> **"possibly" = not verified in this session's research; worth checking before trusting.**

## Harness × Provider Compatibility

> [!info] Which harnesses work with which providers
>
> | Harness | Anthropic | OpenAI | OpenRouter | Ollama Cloud | Together | Groq | Cerebras | Local (Ollama/llama.cpp) |
> |---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> | **Claude Code** (via `ANTHROPIC_BASE_URL`) | ✅ native | ✅ Anthropic-compat route | ✅ | ✅ (ollama launch wrapper) | ✅ | ✅ | ✅ | ✅ |
> | **Codex CLI** | — | ✅ native | ✅ | — | — | — | — | — |
> | **Codex Plugin for Claude Code** | inherits CC | ✅ for codex commands | inherits | — | — | — | — | — |
> | **OpenCode** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (75+ providers total) |
> | **Aider** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
> | **Cline** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
> | **Cursor 3** | ✅ | ✅ | limited | ✅ | limited | — | — | limited |
> | **Gemini CLI** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ (Gemini-only) |
> | **Crush / Goose / Kilo / Continue** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
>
> **Pattern**: BYOM harnesses work with every provider. Product-harnesses (Claude Code, Codex CLI, Cursor, Gemini CLI) prefer their home provider but support others at varying fidelity. Gemini CLI is the only hard-locked one.

## Decision Recipes — the operator's daily workloads

> [!success] Quick-pick by workload (copy-paste ready)
>
> | Workload | Harness | Provider | Model | Estimated cost per hour of work |
> |---|---|---|---|---|
> | **Wiki synthesis / research (personal, mission-aligned)** | Claude Code | Ollama Cloud Pro | K2.6 | ~$0.90/h amortized ($27/mo ÷ 30h) |
> | **Wiki synthesis (overflow, peak day)** | Claude Code via `ANTHROPIC_BASE_URL` | OpenRouter | K2.6 | ~$1.20/h (500K output × $3.50/M) |
> | **Client code work (private repo, per-request visibility)** | Claude Code | OpenRouter with pinned provider | K2.6 | ~$1.20/h |
> | **Budget coding (open-source project, cost-sensitive)** | Aider or OpenCode | OpenRouter | GLM 4.7 | ~$0.60/h (2× cheaper output than K2.6) |
> | **Ultra-budget bulk coding** | OpenCode | DeepSeek direct | DeepSeek V3 | ~$0.15/h (cheapest coding tier on the planet) |
> | **Long-context synthesis (>300K tokens)** | Claude Code | OpenRouter | gpt-5.4 (1.05M ctx) | ~$5/h (cost of large context) |
> | **Adversarial code review** | Claude Code + Codex Plugin | OpenAI direct | gpt-5.5 (via `/codex:adversarial-review`) | ~$0.50 per review |
> | **Code rescue / delegated debugging** | Claude Code + Codex Plugin | OpenAI direct | gpt-5.5 (via `/codex:rescue --background`) | ~$1-3 per rescue |
> | **Creative-technical writing (operator voice)** | Claude Code | Anthropic direct | Opus 4.7 | ~$5-10/h (Opus specialty cost) |
> | **Multimodal review (diagrams, UI)** | Claude Code or Cursor | Google direct | Gemini 3.1 Pro | ~$0 (free tier) or <$1/h |
> | **Speed-critical agentic chains** | OpenCode or Aider | Cerebras or Groq | Llama 3.3 70B or open GPT-OSS | ~$0 (free tier) to paid |
> | **Experimentation / prototyping** | Any BYOM | Cerebras free (1M/day) or Gemini free | Open-weight or Gemini | $0 |
> | **Confidential / private-infra / offline** | Aider or OpenCode | — | Local K2.6 Q2 via llama.cpp | $0 marginal (batch tolerant only) |

## Resilience Substitution — explicit paths

> [!warning] Pre-wired substitutes for each default
>
> **Mission-anchor model (K2.6) substitution chain** (if Moonshot changes terms):
> 1. **GLM 4.7** via OpenRouter ($0.38/$1.74) — cheaper, 73.8% Verified, open-weight ✅
> 2. **DeepSeek V4-Pro** via OpenRouter (~$3.48/M out) — 80.6% Verified (= Opus) ✅
> 3. **DeepSeek V3** via DeepSeek direct ($0.28/$0.42) — cheapest competent option ✅
> 4. **Qwen3 family (local)** — operator hardware already has capability for 8-27B Qwen
>
> **Codex specialty substitution** (if OpenAI changes Codex terms):
> 1. **GLM 4.7 via OpenRouter** — 41% Terminal Bench 2.0 (Codex leader is 77.3%); acceptable for most reviews
> 2. **DeepSeek V4-Pro via OpenRouter** — 80.6% SWE-Bench Verified; can serve as critic in a prompted adversarial-review skill
> 3. **Prompted "adversarial-review" skill in OpenCode/Claude Code** against K2.6 — loses product-command polish, retains 7-attack-surface logic
>
> **Opus specialty substitution** (if Anthropic pricing climbs):
> 1. **K2.6 with tone prompting** — covers ~85% of Opus creative-technical use
> 2. **GPT-5.4** for tone-specific cases where K2.6 isn't matching
> 3. **Claude Code harness** still works via `ANTHROPIC_BASE_URL` to any model — separate the harness from the model
>
> **OpenRouter substitution** (if aggregator changes terms or goes down):
> 1. **Direct provider accounts** kept warm — Moonshot for K2.6, OpenAI for GPT, Anthropic for Opus, Z.ai for GLM, DeepSeek for DeepSeek
> 2. **Together AI** — 175 models, own GPU clusters, no aggregator fee
> 3. **Eden AI or DeepInfra** — second-tier aggregators with similar coverage
>
> **Ollama Cloud substitution** (if Pro pricing changes):
> 1. **OpenRouter K2.6** pay-per-token — breakeven crosses back below 5.6M tokens/mo
> 2. **DeepInfra** — cheapest open-weight inference
> 3. **GLM 4.7 via OpenRouter** — 2× cheaper output than K2.6, extends the budget

## The Breakthrough — "Budget Anchor" Alternatives to K2.6

K2.6 has been treated as THE mission-anchor. 2026-04-23 research surfaces that **open-weight now has a TIER HIERARCHY**, not a single anchor:

> [!abstract] Open-weight tier hierarchy (mission-aligned across the board)
>
> | Tier | Model | Use when | Cost-per-M-output advantage |
> |---|---|---|---|
> | **Ceiling** (Opus-class) | DeepSeek V4-Pro | Need Opus-tier reasoning at fraction of cost | ~$3.48 vs Opus $75 = **20× cheaper** |
> | **Anchor** (agentic frontier) | Kimi K2.6 | General agentic work, 300-agent swarm, long-context (262K) | $3.50 vs GPT-5.4 $15 = **4× cheaper** |
> | **Budget** (strong coding) | GLM 4.7 | Coding-focused, cost-sensitive | $1.74 vs K2.6 $3.50 = **2× cheaper** |
> | **Ultra-budget** (competent coding) | DeepSeek V3 | Bulk coding, high-volume, cost-floor | $0.42 vs K2.6 $3.50 = **8× cheaper** |
> | **Ultra-light** (simple tasks) | GLM 4.7 Flash | Routine automations, simple classifications | $0.40 vs K2.6 $3.50 = **9× cheaper** |
>
> Not ONE mission-anchor. FIVE of them at different price points — all open-weight, all mission-aligned. The operator can route workloads to the cheapest model that hits quality, using K2.6 only when the agentic-frontier specialty is load-bearing.

This changes the routing math. Instead of "K2.6 for everything mission-aligned," the more efficient rule is:

1. **Classify the workload by required model tier** (ceiling / anchor / budget / ultra-budget / ultra-light)
2. **Pick the tier's canonical model** as the first choice
3. **Fallback within-tier to substitutes** if the primary provider changes

Projected cost impact at operator's volume (15-30M output tokens/month): switching 50% of K2.6 traffic to GLM 4.7 saves ~**$25-50/month** with zero capability loss for coding-shaped work.

## How To Use This Matrix

> [!tip] At every workload decision point
>
> 1. **Identify the workload shape** (coding / synthesis / review / multimodal / etc.) — use the Decision Recipes table.
> 2. **Confirm model tier** (anchor / budget / ultra-budget / specialty) — use the Breakthrough tier hierarchy above.
> 3. **Pick the provider** based on cost + privacy + speed needs — use the Provider × Model matrix.
> 4. **Pick the harness** based on current session context — most BYOM harnesses work; choose for UX.
> 5. **Log the choice** — so quarterly review can validate whether the pattern still matches workload cost.
>
> When something changes (provider prices, new model releases, mission drift), re-run this decision flow against the updated matrix. The matrix is a live reference; the decision process is stable.

## Updates + quarterly review triggers

Re-validate this matrix when:
- **Any cell in the "Master Matrix" shifts >20%** (price change, benchmark update, availability change)
- **A new open-weight model lands** that beats K2.6, GLM 4.7, or DeepSeek in its tier (e.g., K3, GLM 5, DeepSeek V5)
- **A major provider deprecates or launches** (e.g., Ollama Cloud model mix change, new aggregator, Cerebras adds K2.6)
- **A new harness crosses the capability bar** to enter the "serious contender" set (currently 11+ harnesses)
- **Operator workload pattern changes** (new fleet, new domain, new regulatory constraint)

## How This Connects

> [!abstract] From this matrix → supporting detail
>
> | Need | Go To |
> |---|---|
> | Strategic framing (why these choices) | [[ai-infrastructure-decision-framework-2026\|AI Infrastructure Decision Framework 2026]] |
> | Individual harness deep-dives | [[src-agentic-coding-harness-landscape-2026\|Harness Landscape 2026]] |
> | Individual provider deep-dives | [[src-inference-provider-landscape-2026\|Inference Provider Landscape 2026]] |
> | K2.6 specifics | [[src-kimi-k2-6-moonshot-agent-swarm\|Kimi K2.6 Synthesis]] |
> | Codex features + plugin | [[src-codex-cli-and-claude-code-plugin\|Codex CLI + Plugin Synthesis]] |
> | Claude Code harness features | [[src-claude-code-harness-features\|Claude Code Harness Features]] |
> | Training vs inference economics | [[ai-infrastructure-decision-framework-2026\|Framework]] § Training |
> | Local training playbook | [[local-training-playbook-2026\|Local Training Playbook 2026]] |

## Relationships

- IMPLEMENTS: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
- BUILDS ON: [[src-kimi-k2-6-moonshot-agent-swarm|Kimi K2.6 Synthesis]]
- BUILDS ON: [[src-agentic-coding-harness-landscape-2026|Harness Landscape 2026]]
- BUILDS ON: [[src-inference-provider-landscape-2026|Inference Provider Landscape 2026]]
- BUILDS ON: [[src-codex-cli-and-claude-code-plugin|Codex CLI + Plugin]]
- BUILDS ON: [[src-claude-code-harness-features|Claude Code Harness Features]]
- FEEDS INTO: [[aicp|AICP]] — this matrix directly informs `tier_map` configuration
- FEEDS INTO: [[local-training-playbook-2026|Local Training Playbook 2026]]
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] — every ✅ in the matrices is a verified access path with sourced pricing, not an asserted claim

## Backlinks

[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[Kimi K2.6 Synthesis]]
[[Harness Landscape 2026]]
[[src-inference-provider-landscape-2026|Inference Provider Landscape 2026]]
[[Codex CLI + Plugin]]
[[src-claude-code-harness-features|Claude Code Harness Features]]
[[aicp|AICP]]
[[local-training-playbook-2026|Local Training Playbook 2026]]
[[Principle 4]]
[[provider-pricing-monitoring-operations-plan|Provider Pricing Monitoring — Operations Plan]]
