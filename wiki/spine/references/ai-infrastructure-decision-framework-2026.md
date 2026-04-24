---
title: "AI Infrastructure Decision Framework 2026 — Full Landscape × Cost × Capability × Privacy"
aliases:
  - "AI Infrastructure Decision Framework 2026"
  - "AI Infrastructure Reality Check 2026"
  - "Vision — AI Infrastructure 2026"
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
  - id: aicp-perspective-2026-04-24
    type: documentation
    project: aicp
    path: docs/PERSPECTIVE-AI-INFRASTRUCTURE-DECISION-2026-04-24.md
    file: raw/articles/aicp-perspective-ai-infrastructure-decision-2026-04-24.md
    description: "AICP's strategic decision document — the operator-reviewed disillusion artifact. Source of the four-phase framework, the capability-vs-cost question, and the anti-patterns below."
  - id: aicp-postmortem-k26-local
    type: documentation
    project: aicp
    path: docs/POSTMORTEM-2026-04-24-k26-local-wrong-path.md
    file: raw/articles/aicp-postmortem-2026-04-24-k26-local-wrong-path.md
    description: "The postmortem grounding why local K2.6 was the wrong primary path — two days, multiple tool-pivots, ending at 0.3 tok/s. Evidence for `local viability ≠ local practicality` claim."
  - id: aicp-model-ecosystem-map
    type: documentation
    project: aicp
    path: docs/MODEL-ECOSYSTEM-FULL-MAP-2026-04-24.md
    file: raw/articles/aicp-model-ecosystem-full-map-2026-04-24.md
    description: "Verified pricing matrix — Anthropic, OpenAI (GPT-5.x including codex variants), Moonshot, Google, DeepSeek, Z-AI, Qwen, Ollama Cloud. Source of the full-landscape numbers in this doc."
  - id: aicp-cloud-spend
    type: documentation
    project: aicp
    path: docs/CLOUD-SPEND-SCENARIOS-2026-04-24.md
    file: raw/articles/aicp-cloud-spend-scenarios-2026-04-24.md
    description: "Cloud economics — OpenRouter vs Ollama Cloud vs Local, breakeven math, scenario-by-scenario monthly spend projections (CAD)."
  - id: aicp-hardware-build
    type: documentation
    project: aicp
    path: docs/HARDWARE-BUILD-SCENARIOS-2026-04-24.md
    file: raw/articles/aicp-hardware-build-scenarios-2026-04-24.md
    description: "Three hardware tiers with CAD pricing ($15-19k / $32k / $65-80k), what each buys, upgrade paths, savings variants."
  - id: aicp-scaling-projection
    type: documentation
    project: aicp
    path: docs/SCALING-PROJECTION-5YR-2026-04-24.md
    file: raw/articles/aicp-scaling-projection-5yr-2026-04-24.md
    description: "5-year token-volume projection for operator's specific workload pattern (2-3 personal sessions + 1-2 fleets of 10 agents)."
  - id: aicp-session-24-handoff
    type: documentation
    project: aicp
    path: docs/SESSION-2026-04-24-HANDOFF.md
    file: raw/articles/aicp-session-2026-04-24-handoff.md
    description: "Operator's own framing of the 2026-04-24 session outcome, corrections, and open decisions."
tags: [reference, p0, ai-infrastructure, decision-framework, cost, capability, privacy, sovereignty, claude, gpt, codex, kimi, k2-6, openrouter, ollama-cloud, subscription, hardware-tier, mission, post-anthropic, 2026]
---

# AI Infrastructure Decision Framework 2026

## Summary

The 2026 AI-infrastructure landscape has one dominant empirical finding: **cost-optimization and sovereignty-insurance are different decisions**, and almost every wrong choice happens when an operator conflates them. AICP's two-day 2026-04-22 through 2026-04-24 analysis — which got local K2.6 Q2 technically running on the operator's workstation at 0.3 tok/s and then **postmortemed the effort as the wrong primary path** — produced the verified numbers this framework rests on. This document ingests those findings, extends them across the full provider landscape (Anthropic + OpenAI/Codex + Moonshot + Google + open-weight), and produces one reference the operator can consult at every infrastructure-spending decision.

> [!success] The one-line vision
> **Smart-routed cloud is the default. Hardware is capability insurance priced on non-economic grounds. Subscriptions beat per-token only above verified sustained volume AND only when the provider's model policy matches the mission. The $540/mo pre-mission baseline was 2-3× what the actual workload costs at any scale in 2026.**

> [!warning] The disillusion this document encodes
> Multiple illusions did not survive the 2026-04-22/24 empirical test:
>
> 1. **"Local hardware pays back over 5 years."** *It does not*, at any realistic operator workload up to 2-fleet scale. Hardware ROI only exists on sovereignty/privacy grounds, not cost.
> 2. **"Local K2.6 on current hardware is a usable tier."** *It is not*: 0.3 tok/s measured reality. Local is a sovereignty fallback, not a primary path, until hardware changes or a smaller-footprint K-class model lands.
> 3. **"Claude Max / Anthropic subscriptions are the sensible high-volume default."** *Not for a mission-aligned stack* — the mission exists precisely because Claude is no longer the unique right answer. Ollama Cloud Pro ($27 CAD/mo) flat-rate on open-weight models is 5-7× cheaper for the same agentic quality tier.
> 4. **"Flat-rate always beats per-token."** *Only above the breakeven.* Ollama Cloud Pro = $27/mo = ~5.6M output tokens/mo breakeven vs OpenRouter K2.6. Below that breakeven, per-token is cheaper and has per-request cost visibility.
> 5. **"More providers is always better."** *Only when each one maps to a distinct workload shape.* OpenAI GPT-5.4 at $2.50/$15 is 2× more expensive than K2.6 at $0.80/$3.50 on output — useless unless a specific capability (coding? creative writing? math?) actually warrants it.

## Key Insights

> [!info] Four dimensions, not one, govern every infrastructure decision
>
> 1. **Cost** — $/M tokens, $/month, $/hardware amortized. Measurable, comparable.
> 2. **Capability** — agentic benchmark, coding quality, tool-use reliability, long-context, multimodal, swarm orchestration.
> 3. **Privacy / Sovereignty** — where does inference run, under whose TOS, shared pool or dedicated, can it leave the machine at all.
> 4. **Mission** — independence from any single provider, $0-target, post-Anthropic by 2026-04-27.
>
> **Cost + Capability answer is usually "smart-routed cloud."**
> **Privacy + Mission answer is usually "hardware when sustained volume justifies."**
> Conflating the two leads to the wrong answer in both directions — buying hardware for cost, or paying premium subscriptions against the mission.

> [!tip] The question to ask at every decision point
> *"Am I buying this because it's cheaper, or because I want the capability regardless of cost?"* (AICP PERSPECTIVE 2026-04-24.)
>
> - If cheaper → do the token-volume math. Smart routing almost always wins.
> - If capability-insurance → the math is secondary. Decide on sovereignty-weight and the hardware-relevance horizon (next-gen GPUs in 2026-2027 may shift the whole calculus).

> [!warning] What "mission-aligned" actually means (clarified 2026-04-23)
> **Mission = no single-provider dependency.** NOT "never use closed-weight." NOT "never pay Anthropic or OpenAI." Those are Puritan readings that lead to worse outcomes.
>
> **Closed-weight models are specialty tools.** Each provider has genuine strengths: Claude Code's harness + Opus's tone-fidelity for creative-technical writing, GPT's codex family for adversarial code review + long-context (1.05M on gpt-5.4), Gemini for multimodal understanding. Using all of them AS SPECIALISTS is MORE mission-aligned than using one of them as a default, because it prevents the lock-in the mission exists to avoid.
>
> **The mission-violating pattern is subscription-tier lock-in to ONE provider as the default.** Paying Anthropic $200/mo to use Opus for everything reinstalls the dependency the mission was built to break. Paying Anthropic API rates for Opus on a specific load-bearing task is fine — it's a specialty routing decision with a review trigger.

## Specialty Routing — Each Provider's Unique Strengths

Closed-weight providers are not "off-limits" — they are specialty vendors with distinct comparative advantages. The mission-aligned stack uses them FOR THEIR SPECIALTIES, not as defaults.

> [!abstract] Provider → unique specialty → reach-for-it trigger
>
> | Provider / Model | Unique specialty | Reach for it when | Why not the default |
> |---|---|---|---|
> | **Anthropic Claude Code harness** | The agent-loop product itself (IDE, skills, hooks, MCP) | Any session where the harness is load-bearing, regardless of which model runs inside | Harness is separable from model choice — route via `ANTHROPIC_BASE_URL` |
> | **Claude Opus** (current) | Creative-technical synthesis; tone fidelity; constitutional-AI behavior for sensitive reasoning | Wiki synthesis where tone + structure + reasoning combine; sensitive decision framing | $15/$75 per M vs K2.6's $0.80/$3.50 — reserve for tasks where Opus's specific behavior is load-bearing |
> | **Future Claude** (e.g. Mythos if/when it lands) | Unknown; track and re-evaluate | When it lands and shows a clear capability delta | Don't pre-commit to subscription before measurement |
> | **GPT-5.1-codex family** | Coding-specialized; `codex-mini` at $0.25/$2 is cheapest coding-capable tier | Pure coding tasks with tight cost budget; adversarial code review (GPT as critic vs K2.6 as author) | General agentic work — K2.6 leads on SWE-Bench Pro despite price |
> | **GPT-5.4 / 5.4-pro** | Long context (1.05M vs K2.6's 262K); pure-math reasoning (AIME 96-99 vs K2.6 ~92) | Very-long-context synthesis; math-heavy workloads; adversarial review of an agentic workflow | 4× price of K2.6 on output; don't use for general agentic work |
> | **GPT + K2.6 together** | Adversarial-review pattern: one writes, the other critiques | High-stakes architecture decisions, security reviews, cross-checking synthesis quality | Routine work where single-model output is good enough |
> | **Kimi K2.6** | Agentic frontier; 300-agent swarm; open-weight mission-alignment | General agentic coding, wiki synthesis, research pipelines | Pure-math corners, ultra-long context, certain creative-tone tasks |
> | **Google Gemini 3.1 Pro** | Multimodal understanding (MMMU-Pro 83.0 vs K2.6's 79.4) | Image/video/UI review; diagram extraction; multimodal research | Text-only agentic work — doesn't justify the context-switch |
> | **Local K2.6 Q2** | Sovereignty; offline; zero marginal cost on batch work | Confidential code; offline sessions; regulatory data-residency; long-running batch jobs tolerant of 0.3 tok/s | Interactive sessions — throughput floor is the practicality ceiling |
>
> **The adversarial-review specialty is worth naming explicitly:** pair K2.6 (author) + GPT-5.x (critic) on high-stakes decisions. K2.6 tends toward confident forward motion; GPT tends to surface risks and edge cases. Neither model is "better" — the pair is better than either alone. This is NOT doubled cost per decision; it's ~1.2× cost for substantially higher confidence on the handful of decisions where it matters.

## The Full Provider Landscape

### Pricing matrix (verified 2026-04-24, AICP source)

> [!abstract] Per-million-token cost — ranked, coding-capable tier
>
> | Model | Access | $USD/M in | $USD/M out | Context | Mission-aligned? |
> |---|---|---:|---:|---:|---|
> | Model | Access | $USD/M in | $USD/M out | Context | Role |
> |---|---|---:|---:|---:|---|
> | **gpt-5.1-codex-mini** | OpenAI / OpenRouter | $0.25 | $2.00 | 400K | **Specialist** — cheapest coding tier; adversarial-review critic |
> | **kimi-k2-6** | OpenRouter (MIT open-weight) | $0.80 | $3.50 | 262K | **Default** — agentic frontier, mission-anchor |
> | **gpt-5.1-codex** | OpenAI / OpenRouter | $1.25 | $10.00 | 400K | Specialist — coding + adversarial review |
> | **gpt-5.1-codex-max** | OpenAI / OpenRouter | $1.25 | $10.00 | 400K | Specialist — coding + adversarial review |
> | **gpt-5** / **gpt-5.1** | OpenAI / OpenRouter | $1.25 | $10.00 | 400K | Specialist — long-context fallback |
> | **gpt-5.4** | OpenAI / OpenRouter | $2.50 | $15.00 | 1.05M | Specialist — 1M+ context; math reasoning |
> | **gpt-5.2** | OpenAI / OpenRouter | $1.75 | $14.00 | 400K | Specialist (rare use — 5.1-codex usually preferred) |
> | **claude-opus-4-6** (API est.) | Anthropic direct | ~$15 | ~$75 | 200K | Specialist — creative-technical synthesis; tone fidelity |
> | **gpt-5.4-pro** | OpenAI | $30 | $180 | 1.05M | Rare — only when 1M context + pro-tier reasoning together |
>
> **"Default" vs "Specialist" legend:** Default = the model you route to without a specific reason. Specialist = the model you route to because this specific task needs what it's best at. Using specialists is mission-aligned; using ONLY one provider (default or specialist) is the lock-in the mission exists to prevent.

### Subscription matrix (verified 2026-04-24)

> [!abstract] Flat-rate subscriptions across providers
>
> | Plan | $USD/mo | Models covered | Usage envelope | Privacy posture | Mission-aligned? |
> |---|---:|---|---|---|---|
> | **Ollama Cloud Pro** | $20 | K2.6, GLM 4.7, others open-weight | ~20-30M tokens/mo soft-cap (estimated) | Shared pool — **prototyping only** | ✅ |
> | **Ollama Cloud Max** | ~$100 | Same, higher cap | ~80-120M tokens/mo (estimated) | Shared pool — **prototyping only** | ✅ |
> | **ChatGPT Plus** | $20 | GPT-5.x via ChatGPT UI (not API) | ~50 msgs/3h cap per model tier | OpenAI TOS | Lock-in risk at default use |
> | **ChatGPT Pro** | $200 | GPT-5.x + o-series + pro models | Much higher cap | OpenAI TOS | Lock-in risk at default use |
> | **Claude Max 5×** | $100 | Opus/Sonnet via Claude Code + web | ~700 prompts/week | Anthropic TOS | Lock-in risk at default use |
> | **Claude Max 20×** | $200 | Opus/Sonnet, higher cap | ~1200 prompts/week | Anthropic TOS | Lock-in risk at default use |
>
> **Key asymmetry**: Ollama Cloud is the **only subscription that doesn't increase single-provider lock-in** — because it's the only flat-rate plan that serves open-weight models you could replicate locally if Ollama disappeared tomorrow. Paying Anthropic or OpenAI a monthly subscription for DEFAULT use deepens lock-in (the mission-violating pattern). Paying Anthropic or OpenAI at **API rates for specialty routing** (Opus for specific synthesis, Codex for specific review passes) does not — you retain provider-switch capability because no single vendor is load-bearing for daily operation.

### Hardware tiers (verified 2026-04-24, AICP sources)

> [!abstract] Local inference capability — CAD pricing
>
> | Tier | CAD | Tok/s on K2.6 Q2 | Breakeven vs cloud | Mission fit |
> |---|---:|---:|---|---|
> | **Tier 0** (existing: RTX 2080 Ti + RTX 2080, 64GB DDR4) | $0 | **~0.3 tok/s** (measured 2026-04-24) | Sunk cost | Insufficient for primary |
> | **Tier 1** | $15-19k | ~5-10 tok/s (estimated) | ~$130 CAD/mo sustained cloud | Usable sovereignty fallback |
> | **Tier 2** ("sweet spot") | ~$32k | ~20-30 tok/s (estimated) | ~$440 CAD/mo sustained cloud | Full-time viable; sovereignty primary |
> | **Tier 3** (datacenter-at-home) | $65-80k | ~40-60 tok/s (estimated) | >$900 CAD/mo sustained cloud | Only for multi-client commercial |
>
> **Operator's projected 5-year sustained cloud spend, smart-routed: ~$11,460 CAD.** No hardware tier pays back economically. Tier 2 is cost-neutral-to-positive only if operator's spend sustained the prior $540 CAD/mo level — which the smart-routed stack refutes.

## The Phase Framework (extended from AICP)

> [!success] Four phases, trigger-gated
>
> | Phase | Period | Trigger to advance | Monthly AI spend budget | Primary path |
> |---|---|---|---|---|
> | **1. Ramp-up** | 2026 now | baseline | **$40-70 CAD/mo** | OpenRouter K2.6 (client) + Ollama Pro (personal) + local K2.6 Q2 fallback |
> | **2. Pro → Max** | Q4 2026 - 2027 | sustained >30M output tokens/mo for 2+ months | **$150-220 CAD/mo** | Ollama Max + OpenRouter overflow |
> | **3. Hardware decision point** | 2027-2028 | sustained 50M+ tokens/mo for 6+ months **AND** sovereignty weight crosses threshold | Decide cloud vs hybrid | Either: Tier 2 hw + Max, or Max + OR-heavy |
> | **4. Steady state** | 2029+ | — | $4-6k/yr cloud-only OR $7-8k/yr hybrid | Whatever path Phase 3 chose |
>
> **The phases are not a timeline — they are thresholds.** Advance only on verified sustained volume (not projected, not burst). Regress if volume drops.

## The Anti-Patterns (expanded beyond AICP)

> [!warning] Rules that prevent the known failure modes
>
> 1. **Never buy Tier 3 hardware** unless: AI work is generating measurable revenue for 12+ months, multiple users/clients need local inference, and sovereignty is a *contractual* requirement rather than a preference.
>
> 2. **Never subscribe to Anthropic as a DEFAULT tier** — $200/mo to use Opus for everything reinstalls the lock-in the mission exists to break. Opus via API at specialty-rates ($15/$75) for tasks where its tone/synthesis is load-bearing is fine. Claude Code harness used with a non-Anthropic model via `ANTHROPIC_BASE_URL` is also fine — harness ≠ model choice.
>
> 3. **Never subscribe to OpenAI as a DEFAULT tier** — same lock-in principle. GPT-5.1-codex-mini at $0.25/$2 API is a specialty tool for coding and adversarial review. ChatGPT Pro at $200/mo to use GPT for everything is the pattern to avoid.
>
> 4. **Never route client/employer work through Ollama Cloud** (any tier). Shared pool, opaque providers, author-acknowledged "prototyping only" policy. Use OpenRouter with pinned vetted provider OR local-when-usable.
>
> 5. **Never upgrade cloud tier on a usage spike.** Wait 2+ consecutive months of sustained usage before committing to the next-tier subscription. Bursts lie; trends don't.
>
> 6. **Never buy hardware speculatively.** Only after 6+ months of usage data showing the capacity is needed AND mission-weight justifies the non-economic cost.
>
> 7. **Never conflate cost optimization with independence mission.** They produce different right answers. Pick the question explicitly before running the numbers.
>
> 8. **Never treat "GPT-5.4 > K2.6" as a default truth.** GPT-5.4 at $2.50/$15 is 2× more expensive than K2.6 on output for general agentic work where K2.6 is at or above GPT-5.4 on the benchmarks that matter (SWE-Bench Pro, HLE-with-tools). Reach for GPT only when a specific capability gap matters.
>
> 9. **Never treat "local K2.6 is running" as "local K2.6 is usable."** 0.3 tok/s is technically-working, not practically-usable. Mission milestone is a sovereignty-insurance proof, not an operational tier.
>
> 10. **Never mistake `ollama launch` for `aicp --backend`** — the convenience of `ollama launch claude --model X` makes it easy to accidentally route sensitive sessions through the shared Ollama pool. AICP's `tier_map` is the mission-aligned routing surface; Ollama's `launch` wrapper is an escape hatch, not the default.

## Per-Workload Routing Map

> [!tip] Match each session to the right path at invocation time
>
> | Workload shape | Path | Reason |
> |---|---|---|
> | Wiki synthesis, open-source research, public code analysis | Ollama Cloud Pro (if quota) OR OpenRouter K2.6 | Flat rate for volume; no privacy cost |
> | AICP self-development (operator's own code) | OpenRouter K2.6 | Per-request cost visibility for self-measurement |
> | OpenArms / OpenFleet agent development | OpenRouter K2.6 primary | Mission-aligned, visible cost |
> | Client/employer work, private repos | OpenRouter K2.6 with pinned provider OR local-when-usable | Never Ollama shared pool |
> | Pure coding at small-task scale | OpenRouter `gpt-5.1-codex-mini` ($0.25/$2) | Cheapest coding tier; specialty routing (not default lock-in) |
> | High-stakes decision, architecture review, security review | **K2.6 author + GPT-5.1-codex critic** (adversarial pair) | Two-model review surfaces risks neither would alone; ~1.2× cost for substantially higher confidence |
> | Creative-technical writing where tone + structure + reasoning combine | Opus-tier via Anthropic API | Specialty: Opus's tone fidelity is load-bearing for wiki synthesis and operator-voice material |
> | Multimodal review (diagrams, UI mockups, video) | Gemini 3.1 Pro via OpenRouter | Gemini's MMMU-Pro edge; rare but real use |
> | Long-context research synthesis (>200K tokens) | OpenRouter K2.6 (262K) or `gpt-5.4` (1.05M) | Context-size-driven choice |
> | Creative writing with specific tone | Opus-tier if tone is load-bearing | Rare; justify each time |
> | Offline sessions (travel, outages, legal residency) | Local K2.6 Q2 (batch-tolerant tasks only) | Sovereignty-only tier |
> | Pure-math reasoning | GPT-5.x (AIME 96-99 vs K2.6 ~92) | Specific capability gap |
> | 300-agent swarm orchestration | OpenRouter K2.6 or local | Model-native feature; Ollama Cloud untested |

## The Subscription Decision Flow

> [!info] Subscribe to exactly ONE flat-rate provider at a time, and gate it
>
> 1. **Measure** current sustained monthly output tokens (not projected, not peak).
> 2. **If < 5M tokens/mo**: no subscription. Pure OpenRouter pay-per-token is cheapest.
> 3. **If 5-30M tokens/mo sustained 2+ months**: Ollama Cloud Pro at $20 USD/mo. OpenRouter for client work.
> 4. **If >30M tokens/mo sustained 2+ months**: Ollama Cloud Max at ~$100 USD/mo. Revisit quarterly.
> 5. **If >100M tokens/mo sustained 6+ months AND sovereignty weight justifies**: Phase 3 hardware decision.
>
> **Anthropic Max or ChatGPT Pro enter this flow ONLY if** a specific closed-model capability is load-bearing for 2+ months of real work — and the subscription cost is logged as a mission-exception with a review date.

## The Mission Budget

> [!success] Current state (2026-04-23, per-operator framing)
>
> - **Mission**: post-Anthropic self-autonomous AI stack by 2026-04-27. **Still active.**
> - **Prior baseline**: $540 CAD/mo (2× $240 CAD subs + tax). **Disabled.**
> - **Current spend**: $0 measurable. Local K2.6 running but not usable as primary.
> - **Next action (Phase 1 ramp-up)**: reactivate exactly one subscription — Ollama Cloud Pro at $20 USD (~$27 CAD)/mo. Keep OpenRouter active for client-adjacent work. Local K2.6 stays as sovereignty fallback.
> - **Expected Phase 1 spend**: $40-70 CAD/mo. **1/8 to 1/10 of prior baseline.**
>
> The smart-routed replacement is measurably cheaper than the prior single-provider habit. 5-year savings from the routing change alone: $12-18K CAD. Zero hardware required.

## Training: Local Unsloth/LoRA vs Cloud GPU Rental

The framework above covers **inference** (running models). Training (fine-tuning, LoRA, embedding models, routers) is a separate decision with different economics.

### What fits on operator's Tier-0 hardware (19 GB VRAM + 64 GB RAM)

> [!abstract] Local training feasibility — Unsloth-optimized
>
> | Base model size | LoRA rank 16-64 | Full fine-tune | Practical on Tier 0? |
> |---|---|---|---|
> | ≤1B (routers, classifiers, small embeddings) | Trivial fit | Trivial fit | ✅ Easy — hours to days |
> | 2B-4B (Qwen3-4B, Gemma3 4B) | Comfortable fit (4-bit base + LoRA) | Tight | ✅ Feasible — overnight jobs |
> | 7-8B (Qwen3-8B — AICP main reasoner) | Fits with gradient checkpointing | Impractical locally | ✅ Feasible — 12-24h per epoch |
> | 13B | Tight; needs careful Unsloth config | No | ⚠️ Doable but slow — multi-day |
> | 27B (Qwopus-class) | Possible with aggressive offload | No | ⚠️ Painful — days to week per run |
> | ≥70B | No practical path | No | ❌ Cloud only |
>
> Unsloth's speciality is making LoRA fit in less VRAM than vanilla HF Transformers — 2× less memory, 2× faster on the same hardware. The table reflects Unsloth-optimized numbers, not raw PyTorch.

### Cloud GPU rental economics

> [!abstract] Rental costs for typical LoRA jobs (2026-04 pricing)
>
> | Provider | GPU | USD/hr | Typical 8B LoRA full-run | Typical 27B LoRA full-run |
> |---|---|---:|---:|---:|
> | **Colab Pro+** | A100 40GB | $0.40-1.00 effective | $5-15 (hits quota limits) | $15-40 (may need multiple sessions) |
> | **Lambda Labs** | A100 40GB | $1.10 | $10-20 | $30-60 |
> | **Lambda Labs** | H100 80GB | $2.50-3.50 | $8-15 (2-3× Unsloth speedup) | $20-40 |
> | **RunPod Community** | A100 40GB | $0.80-1.20 | $8-18 | $25-50 |
> | **RunPod Community** | H100 80GB | $1.90-2.50 | $6-12 | $15-30 |
> | **Vast.ai** | RTX 4090 (24GB) | $0.20-0.45 | $4-10 (if fits) | Doesn't fit without multi-GPU |
> | **Vast.ai** | A100 40GB | $0.60-1.00 | $6-12 | $18-35 |

### The split that actually matters

> [!tip] Local training is viable for the operator's actual planned work
> The custom-model strategy ([[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]]) names five candidates. Three of them fit local training cleanly:
>
> | Candidate | Base size | Local training verdict |
> |---|---|---|
> | **A — Wiki-Assistant** | Qwen3-4B + LoRA rank 32 | ✅ Local — Unsloth-optimized, overnight run |
> | **D — Wiki-Router** | ≤1B classifier | ✅ Local — trivial |
> | **E — Multi-LoRA on Qwen3-8B base** | 8B + N adapters | ✅ Local per-adapter — 12-24h each |
> | **B — Wiki-Reasoner** | If 27B+ | ⚠️ Cloud rental ($30-60 on H100) makes more sense per run |
> | **C — Wiki-Opus-Distilled** | 27B with substantial data | ⚠️ Cloud rental ($40-80 on H100) |
>
> **The custom-model work the operator actually plans — wiki alignment LoRAs, tool-call fine-tuning, semantic enhancement, router training — is all in the local-viable column.** Unsloth on the 19 GB VRAM setup handles the Qwen3-4B / 8B base candidates comfortably. There's no economic reason to rent cloud for these.

### When cloud rental IS the right answer

- **27B+ base models** (Qwopus-class distillation, Wiki-Reasoner if scoped above 13B): H100 rental at ~$15-40 per run beats a multi-day local job on operator time-value grounds.
- **Full fine-tuning (not LoRA)** on anything 7B+: memory overhead of full gradient state exceeds 19 GB VRAM with headroom for any real data.
- **Experimentation sweeps** (10+ LoRA configs to compare): parallelize across multiple rented GPUs — days of experimentation done in hours.
- **Production-scale embedding model training** (if the wiki ever needs a domain-specific embedding over 1-10M pages): dedicated training hardware justified by volume.

### The honest cost comparison

> [!info] A realistic annual training budget for operator's planned custom-model work
>
> - 4-6 LoRA runs on Qwen3-4B (Wiki-Assistant iterations) — **local, $0 additional cost**
> - 2-3 LoRA runs on Qwen3-8B (Multi-LoRA adapters, tool-call specialists) — **local, $0 additional cost**
> - 1-2 experimental 27B LoRA runs (if Wiki-Reasoner pursued) — **~$40-100 on H100 rental**
> - Occasional router/embedding retraining — **local, negligible**
>
> **Total: $40-100/year for training**, dominated by one or two 27B cloud rentals. Training cost is a rounding error vs inference cost; the inference framework above is where the real money lives.

### Anti-patterns for training

> [!warning]
> - **Don't buy hardware "for training"** unless you're training multiple-per-week and the workloads are 27B+. Tier-1 hardware payback vs cloud rental is 6-12 months ONLY at heavy sustained volume.
> - **Don't default to full fine-tuning** when LoRA suffices. The operator's use cases (domain alignment, tool-call patterns, semantic routing) are LoRA-shaped — full fine-tuning is for different problems (distillation, architectural changes).
> - **Don't skip Unsloth** for local runs. Vanilla HF Transformers on 19 GB VRAM is a different (much worse) feasibility table.
> - **Don't commit to a custom-model training project before verifying K2.6 via OpenRouter can't already do the task.** Most "we need a fine-tuned model for X" goals are solved by better prompting + K2.6 at $0.80/$3.50.

## Re-Evaluation Triggers

This framework is valid until one of these triggers fires:

1. **Cloud prices rise materially** (e.g., OpenRouter blended cost >$6 CAD/M output, Ollama Cloud Pro >$40 CAD/mo). Historical trend is falling ~30%/yr for open-weight models; reversal = re-run the math.

2. **Regulatory / client contract** mandates data residency (client, employer, jurisdictional). Forces local tier usability regardless of cost.

3. **Next-gen hardware landing** — Blackwell consumer GPUs, unified-memory Apple Silicon at >256GB, ARM-server-class memory bandwidth at consumer prices. Any of these shifts the Tier 1/2/3 pricing and tok/s substantially.

4. **Next-gen model architectures** with materially smaller memory footprint at K2.6-level capability — would make Tier 0 (existing) viable and collapse the hardware-tier argument entirely.

5. **Mission weight change** — operator decides sovereignty is terminal (end in itself), not instrumental. Legitimate; the math doesn't fight the decision. Document the change.

6. **Provider exit** — Moonshot discontinues K2.6 open-weight policy, or Ollama Cloud changes model mix to closed-weight only. Either invalidates the mission-aligned-subscription argument.

## How This Connects — Navigate From Here

> [!abstract] From this framework → related pages
>
> | Direction | Go To |
> |---|---|
> | Full K2.6 architecture + benchmarks | [[src-kimi-k2-6-moonshot-agent-swarm\|Synthesis — Kimi K2.6]] |
> | K2.6 path-picker (OpenRouter vs Ollama Cloud vs Local) | [[kimi-k2-6-access-paths-openrouter-ollama-cloud-local\|K2.6 Access Paths Comparison]] |
> | Consumer-hardware layer model | [[2026-consumer-hardware-ai-stack\|2026 Consumer-Hardware AI Stack]] |
> | Local-AI strategy | [[model-local-ai\|Model — Local AI]] |
> | Custom-model training (K2.6 obsoletes several candidates) | [[second-brain-custom-model-strategy\|Second-Brain Custom Model Strategy]] |
> | Principle this framework depends on | [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle — Declarations Are Aspirational Until Infrastructure Verifies Them]] |
> | MCP vs CLI framing for agent tooling | [[mcp-vs-cli-decision-vs-lesson\|MCP vs CLI — Decision vs Lesson]] |

## State of Knowledge

| Claim | Verified? | Evidence |
|---|---|---|
| Local K2.6 Q2 on operator Tier-0 hw = 0.3 tok/s | ✅ | AICP 2026-04-24 measured with llama.cpp |
| Tier 2 hardware CAD cost = ~$32k | ✅ | AICP HARDWARE-BUILD-SCENARIOS verified quotes |
| Smart-routed 5-year spend ≈ $11,460 CAD | ⚠️ Projected | Assumes AICP's volume ramp model; sensitive to usage growth |
| K2.6 OpenRouter $0.80/$3.50 USD/M | ✅ | OpenRouter API live 2026-04-22/24 |
| Ollama Cloud Pro $20 USD/mo, Max $100 USD/mo | ✅ | ollama.com/turbo live 2026-04-24 |
| GPT-5.1-codex-mini $0.25/$2 USD/M | ✅ | OpenAI API verified via AICP MODEL-ECOSYSTEM-FULL-MAP |
| Ollama Cloud does NOT carry GPT models | ✅ | AICP MODEL-ECOSYSTEM-FULL-MAP explicitly |
| Anthropic Max 5× ~$100/mo, 20× ~$200/mo | ✅ | operator baseline confirmation |
| Breakeven flat-rate vs per-token ≈ 5.6M output tokens/mo | ✅ | AICP CLOUD-SPEND math |
| Operator's prior $540 CAD/mo was 2-3× actual workload | ⚠️ Inferred | From token-volume reverse-engineering in AICP CLOUD-SPEND |
| K2.6 ≥ GPT-5.4 on agentic benchmarks | ✅ | src-kimi-k2-6-moonshot-agent-swarm synthesis |

## Relationships

- BUILDS ON: [[src-kimi-k2-6-moonshot-agent-swarm|Synthesis — Kimi K2.6]]
- BUILDS ON: [[2026-consumer-hardware-ai-stack|2026 Consumer-Hardware AI Stack]]
- BUILDS ON: [[kimi-k2-6-access-paths-openrouter-ollama-cloud-local|K2.6 Access Paths Comparison]]
- DERIVED FROM: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Infrastructure Verifies Them]]
- FEEDS INTO: [[model-local-ai|Model — Local AI]]
- FEEDS INTO: [[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]]
- RELATES TO: [[mcp-vs-cli-decision-vs-lesson|MCP vs CLI — Decision vs Lesson]]
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] — the "local K2.6 pays back in 18 months" and "hardware is cheaper long-term" claims did not survive measurement

## Backlinks

[[Synthesis — Kimi K2.6]]
[[2026 Consumer-Hardware AI Stack]]
[[K2.6 Access Paths Comparison]]
[[Principle 4 — Declarations Aspirational Until Infrastructure Verifies Them]]
[[Model — Local AI]]
[[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]]
[[MCP vs CLI — Decision vs Lesson]]
[[Principle 4]]
