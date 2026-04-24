---
title: "Synthesis — Inference Provider Landscape 2026 (OpenRouter, Together, Groq, Cerebras, DeepInfra, Ollama Cloud, Direct APIs)"
aliases:
  - "Inference Provider Landscape 2026"
  - "API Provider Alternatives 2026"
  - "Non-Lock-In Inference Matrix"
type: source-synthesis
layer: 1
maturity: growing
domain: tools-and-platforms
status: synthesized
confidence: high
created: 2026-04-23
updated: 2026-04-23
sources:
  - id: openrouter-alternatives
    type: article
    url: https://ofox.ai/blog/openrouter-alternatives-2026/
    title: "7 Best OpenRouter Alternatives in 2026: Pricing, Features, and Migration Guide"
    ingested: 2026-04-23
  - id: infrabase-providers
    type: article
    url: https://infrabase.ai/blog/ai-inference-api-providers-compared
    title: "AI Inference API Providers Compared (2026)"
    ingested: 2026-04-23
  - id: pricepertoken-openrouter-together
    type: article
    url: https://pricepertoken.com/endpoints/compare/openrouter-vs-together
    title: "OpenRouter vs Together AI Pricing 2026 — Model & Cost Comparison"
    ingested: 2026-04-23
  - id: edenai-openrouter-alts
    type: article
    url: https://www.edenai.co/post/best-alternatives-to-openrouter
    title: "Top 7 OpenRouter Alternatives in 2026: Pricing, Routing, and Best Use Cases"
    ingested: 2026-04-23
  - id: awesomeagents-free-apis
    type: article
    url: https://awesomeagents.ai/tools/free-ai-inference-providers-2026/
    title: "Every Free AI API in 2026: Complete Guide to Zero-Cost Inference"
    ingested: 2026-04-23
  - id: premai-openrouter-alts
    type: article
    url: https://blog.premai.io/best-openrouter-alternatives-for-private-production-ai/
    title: "16 Best OpenRouter Alternatives for Private, Production AI (2026)"
    ingested: 2026-04-23
tags: [inference-provider, openrouter, together-ai, groq, cerebras, deepinfra, ollama-cloud, anthropic-direct, openai-direct, moonshot-direct, vendor-lock-in, resilience, free-tier, 2026]
---

# Synthesis — Inference Provider Landscape 2026

## Summary

The operator's mission-critical question isn't "which provider is cheapest today?" — it's "**if my current provider changes price or goes down, can I re-route in hours without rewriting anything?**" This synthesis maps the 2026 inference-provider landscape along three axes: **aggregators vs direct providers**, **speed-optimized vs cost-optimized**, **free-tier vs paid**. The mission-aligned default stack is **OpenRouter (aggregator) + Ollama Cloud (flat-rate open-weight) + Direct APIs when needed + Cerebras/Groq free tiers as experimentation overflow + local K2.6 as sovereignty fallback**. This synthesis lists 10+ providers with verified pricing, throughput, model catalogs, and switch-cost, so the framework's resilience playbook has a factual base. The breakthrough finding: **speed is now a distinct axis from cost** — Groq at 315 tok/s and Cerebras at ~1000 TPS aren't just "fast," they enable agentic workflows that are impractical on OpenAI/Anthropic-tier latency budgets.

## Key Insights

> [!info] Aggregator vs direct: different risk shapes
> **Aggregators** (OpenRouter, Together, Eden) route to multiple backends under one API key — convenient, but add a layer of dependency (OpenRouter 5.5% fee + 100-150ms latency + their uptime). **Direct providers** (Anthropic, OpenAI, Moonshot, Groq, Cerebras) skip the middleman — fewer dependencies, but you manage multiple API keys and switching-costs are higher. **Mission-aligned stack uses both**: OpenRouter as daily convenience; direct-provider accounts kept active (even unused) so substitution is config-only.

> [!tip] The three fastest providers (speed is its own axis in 2026)
> - **Cerebras**: ~1000 TPS on smaller models (Llama 3.3 70B-class). 1M tokens/day **free**. Best sustained throughput on open-weight.
> - **Groq**: 315 TPS on Llama 3.3 70B. Best first-token latency. **Free tier** (rate-limited).
> - **Together AI**: H100/H200/B200 own clusters, 175 models, competitive per-token. Not speed-record but reliable high-quality throughput.
>
> Speed unlocks interactive agentic workflows (rapid tool-call chains) that OpenAI/Anthropic latency budgets make painful. Not a "nice to have" — a different capability class.

> [!warning] OpenRouter's hidden costs
> OpenRouter charges a **5.5% fee on credit purchases** (non-crypto) and adds **100-150ms latency**. OpenRouter is cheaper on 41 of 86 shared models vs Together; Together cheaper on 34. For the operator's K2.6 daily use, OpenRouter is fine. For speed-critical or high-volume workloads, direct provider accounts save the 5.5% + latency.

> [!abstract] The 2026 free-tier landscape — real capacity, not demo-only
>
> | Provider | Free allowance | Usable for |
> |---|---|---|
> | **Cerebras** | 1M tokens/day | Real work — substantial agentic task batches |
> | **Groq** | Rate-limited free tier | Fast experimentation, small batches |
> | **Gemini API** | Most generous among commercial | Daily interactive use if Gemini suits the task |
> | **Hugging Face Inference API** | Community-model rate-limited free | Experimentation on open-weight |
> | **DeepSeek API** | Free tier (terms vary) | Coding-specialty experimentation |
>
> **Operator tactic**: route experimentation and prototyping through free tiers; reserve paid tiers for production-impact workloads. Real $10s-$100s/month savings at operator's volume.

## Deep Analysis

### The ten providers that matter in 2026

| Provider | Type | Model catalog | Pricing shape | Speed | Unique strength | Mission fit |
|---|---|---|---|---|---|---|
| **OpenRouter** | Aggregator | 313 models | Pay-per-token + 5.5% fee | +100-150ms added latency | One API key for dozens of models; A/B testing; provider-pin option | ✅ Current default; no lock-in to a single upstream |
| **Together AI** | Direct (own GPUs) | 175 models | Pay-per-token; also dedicated clusters (H100 $3.99/hr, H200 $5.49/hr, B200 $9.95/hr) | H100/H200/B200 class | No middleman; dedicated options; competitive open-weight pricing | ✅ Open-weight focus; good OR alternative |
| **Groq** | Direct (custom LPU) | Llama family, Moonshot, GPT-OSS, DeepSeek | Pay-per-token; free tier | **315 TPS** Llama 3.3 70B | Best first-token latency; LPU chip advantage | ✅ Speed differentiator |
| **Cerebras** | Direct (wafer-scale) | Llama, specialty open-weight | Pay-per-token; **1M tokens/day free** | **~1000 TPS** on smaller models | Highest sustained throughput; substantial free tier | ✅ Speed + free |
| **DeepInfra** | Direct | Open-weight catalog | **Lowest cost per token** in the space | Standard | Cost floor for open-weight | ✅ High-volume budget option |
| **Ollama Cloud** | Direct (Ollama-managed) | K2.6, GLM 4.7, other open-weight (**no GPT, no Claude**) | **$20/mo flat** (Pro) or ~$100/mo (Max) | Managed pool | Only mission-aligned flat-rate | ✅ Personal-work daily default |
| **Anthropic direct** | Direct (Claude) | Opus, Sonnet, Haiku | Per-token (~$15/$75 Opus); or subscription (Max $100-$200) | Standard | Opus-tier capability | Specialty only (tone, Claude Code harness) |
| **OpenAI direct** | Direct (GPT/Codex) | GPT-5.x family, Codex variants, o-series | Per-token ($0.25/$2 codex-mini → $30/$180 gpt-5.4-pro); or ChatGPT sub ($20-$200) | Standard | Codex specialty, 1.05M context, pure-math | Specialty only (codex, context, math) |
| **Moonshot direct** | Direct (Kimi) | K2.6 and family | Per-token (similar to OpenRouter routing) | Standard | Native K2.6 access with full agent-swarm API | ✅ Removes OpenRouter layer for K2.6 |
| **Google Gemini API** | Direct | Gemini 3.1 Pro family | **Most generous free tier** | Standard | Multimodal SOTA; 1M+ context; free | Specialty (multimodal, free overflow) |
| **Eden AI** | Aggregator (enterprise-focused) | Cross-provider | Routing + enrichment | Aggregator-tier | Enterprise features (SLA, compliance) | Only if enterprise-contract requirements kick in |
| **Hugging Face Inference API** | Aggregator/direct | Community + commercial | Per-token; free community tier | Varies | Widest open-weight catalog including niche models | Experimentation overflow |

### Three routing recommendations by workload shape

**Daily agentic coding (personal, research, non-sensitive)**
→ **Ollama Cloud Pro** ($20/mo) or **OpenRouter K2.6** (per-token)
→ Breakeven vs per-token at ~5.6M output tokens/mo — operator's likely volume sits above this for personal+fleet work

**Client-adjacent, private-repo work**
→ **OpenRouter with pinned high-quality provider** OR **Together AI direct** (no middleman)
→ Never Ollama shared pool; never aggregator without provider pin

**Speed-critical interactive agents (rapid tool chains)**
→ **Groq** (first-token latency) or **Cerebras** (sustained throughput)
→ Both free tiers substantial enough for real experimentation; direct API for production

**Experimentation overflow / exploration / prototyping**
→ **Gemini API free tier**, **Cerebras free (1M/day)**, **Groq free**, **Hugging Face free**
→ Cycle through free tiers per-project; keep paid spend on production-impact work

**Specialty: Opus-tone creative synthesis**
→ **Anthropic direct API** at per-token rates ($15/$75) — specialty, not default

**Specialty: Codex adversarial-review or rescue delegation**
→ **OpenAI direct** (gpt-5.5) via Codex CLI — product feature, not just model

**Specialty: pure math or very-long context**
→ **OpenAI direct** (gpt-5.4 at 1.05M context) or **Gemini API** (1M+ context)

**Sovereignty / offline / regulatory**
→ **Local K2.6 Q2** via llama.cpp on operator's hardware (0.3 tok/s batch mode)

### Provider-failure substitution matrix

| If this provider changes terms / goes down | First substitute | Second substitute | Model-layer impact |
|---|---|---|---|
| **OpenRouter** outage or 5.5% fee climbs | Together AI (direct, 175 models) | Direct provider accounts (Moonshot for K2.6, OpenAI for GPT, Anthropic for Claude) | None — same models, different router |
| **Ollama Cloud** pricing change or model-mix shift | OpenRouter pay-per-token on K2.6/GLM | DeepInfra (cheapest open-weight) | None — same open-weight models |
| **Moonshot** discontinues K2.6 open-weight | GLM 4.7 (via Ollama Cloud or OpenRouter) | DeepSeek v3 (via OpenRouter or DeepSeek direct) | Config-only: tier_map entry updates |
| **Anthropic** Opus pricing climbs or API change | Opus via Anthropic direct (specialty only) → if priced out, **K2.6 via OpenRouter** covers 90% of what Opus was used for; tone-specific cases fall back to carefully-prompted K2.6 or GPT-5.4 | | Harness: still Claude Code via `ANTHROPIC_BASE_URL` |
| **OpenAI** pricing climbs (codex, gpt-5.x) | Codex CLI unusable if OpenAI API cost prohibitive → drop to prompted adversarial-review skill in Claude Code/OpenCode against K2.6 | Cerebras + Llama for coding-adjacent | Lose the `/codex:adversarial-review` exact command; keep the capability class |
| **Groq/Cerebras** changes free tier | Each other; Together AI; DeepInfra | | None — same open-weight base |
| **Multiple aggregators fail** (OR + Together both) | All direct provider accounts active (kept warm even if unused) | | Hours-level switching, not days |
| **All cloud unavailable** | Local K2.6 via llama.cpp at 0.3 tok/s for batch work | | Sovereignty milestone already reached |

**Design principle**: every first-substitute is a config edit, not a migration. Direct provider accounts kept warm (even without monthly subscription) so substitution activates in minutes.

### The specific breakthrough: speed as a distinct axis

OpenAI and Anthropic-tier latency (typically 20-80 tok/s) makes certain agentic workloads painful:
- Rapid tool-call chains (agent calls 50+ tools in a sequence)
- Real-time iterative coding (think + code + re-think loops at interactive speed)
- Large-batch code review across many files

Cerebras at ~1000 TPS and Groq at 315 TPS make these workloads **practical**, not just faster. A 300-agent swarm orchestration on K2.6 at Cerebras speeds would complete in minutes instead of hours. **This is a new capability class the operator should keep aware of**, not just a cost optimization.

Operator's stance for 2026: **Cerebras and Groq free tiers should be active** (zero cost). When a workload crosses the "painful-at-normal-latency" line, route to speed providers. If sustained, consider paid tier.

### Free-tier strategic use — 2026 reality

Free tiers in 2026 have grown substantially enough to absorb real work:
- **Cerebras 1M tokens/day free** = ~30M tokens/month — more than operator's personal baseline (15M/mo est.)
- **Gemini API** free tier covers light agentic coding use
- **Groq free** = rate-limited but usable for speed experiments
- **Hugging Face** community inference free for open-weight experimentation
- **DeepSeek** free tier for coding specialty

**Operator tactic**: route experimentation + prototyping + non-critical daily use through free tiers. Reserve paid spend for production-impact workloads. Measured savings at operator's volume: **$10-50/month** without changing workload.

## Cross-references

- [[src-kimi-k2-6-moonshot-agent-swarm|Kimi K2.6]] — the agentic-frontier model that most providers above can serve
- [[src-agentic-coding-harness-landscape-2026|Harness Landscape 2026]] — pairs with this; harness × provider = the full configuration
- [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] — economics + mission context
- [[kimi-k2-6-access-paths-openrouter-ollama-cloud-local|K2.6 Access Paths Comparison]] — narrower comparison for K2.6 specifically

## State of Knowledge

| Claim | Verified? | Evidence |
|---|---|---|
| OpenRouter has 313 models, 5.5% credit fee, +100-150ms latency | ✅ | OpenRouter alternatives article |
| Together AI 175 models, own H100/H200/B200 clusters | ✅ | Eden AI + pricepertoken |
| Groq 315 TPS on Llama 3.3 70B | ✅ | Multiple sources |
| Cerebras ~1000 TPS, 1M tokens/day free | ✅ | Multiple sources |
| DeepInfra cheapest cost per token for open-weight | ✅ | Eden AI + pricepertoken |
| Ollama Cloud Pro $20/mo flat, no GPT models | ✅ | AICP MODEL-ECOSYSTEM-FULL-MAP + Ollama turbo page |
| OpenRouter cheaper on 41/86 shared models vs Together; Together cheaper on 34 | ✅ | pricepertoken comparison |
| Together H100 $3.99/hr, H200 $5.49/hr, B200 $9.95/hr dedicated | ✅ | pricepertoken |
| Gemini API has most generous free tier among commercial | ✅ | AwesomeAgents + multiple |

## Relationships

- BUILDS ON: [[src-kimi-k2-6-moonshot-agent-swarm|Synthesis — Kimi K2.6]]
- BUILDS ON: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
- RELATES TO: [[src-agentic-coding-harness-landscape-2026|Harness Landscape 2026]] — provider × harness matrix
- RELATES TO: [[kimi-k2-6-access-paths-openrouter-ollama-cloud-local|K2.6 Access Paths Comparison]]
- FEEDS INTO: [[aicp|AICP]] — the `tier_map` config is where these providers get operationalized
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] — resilience claim "we can respond to provider changes" is verified by documented substitution paths with specific switch-costs, not asserted

## Backlinks

[[Synthesis — Kimi K2.6]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[Harness Landscape 2026]]
[[K2.6 Access Paths Comparison]]
[[aicp|AICP]]
[[Principle 4]]
