---
title: "Decision — Qwen3-8B as AICP's Main Reasoning Model (over Hermes-7B, CodeLlama-7B, Gemma-3 4B)"
aliases:
  - "Decision — Qwen3-8B as AICP's Main Reasoning Model (over Hermes-7B, CodeLlama-7B, Gemma-3 4B)"
  - "Decision: Qwen3-8B as Main Reasoning Model"
type: decision
domain: cross-domain
layer: 6
status: synthesized
confidence: high
maturity: growing
reversibility: easy
derived_from:
  - model-local-ai
  - localai-over-ollama-vllm-for-multi-model-orchestration
created: 2026-04-18
updated: 2026-04-22
sources:
  - id: aicp-models-config
    type: file
    file: config/models/qwen3-8b.yaml
    description: "qwen3-8b config — 4.9 GB GGUF, 6 GB+ VRAM, thinking mode, native tool calling (AICP project)"
  - id: aicp-default-profile
    type: file
    file: config/profiles/default.yaml
    description: "Default profile primary backend = qwen3-8b (AICP project)"
  - id: model-evals
    type: directory
    file: docs/kb/models/
    description: "Model evaluation notes (AICP project)"
  - id: model-local-ai
    type: wiki
    file: wiki/spine/models/depth/model-local-ai.md
    description: "Qwen3 family (8B, 4B, 30B MoE) covers most text tasks"
  - id: aicp-contribution-staging
    type: wiki
    file: raw/articles/from-aicp/decisions/01_drafts/qwen3-8b-as-main-reasoning-model.md
    description: "AICP's original submission, 2026-04-18 staged in raw/ before ingestion here"
tags: [decision, qwen3, model, reasoning, aicp, transferable, pattern]
contributed_by: "aicp"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: "2026-04-18"
contribution_status: accepted
---

# Decision — Qwen3-8B as AICP's Main Reasoning Model (over Hermes-7B, CodeLlama-7B, Gemma-3 4B)

## Summary

AICP routes general-purpose reasoning, code analysis, and tool-calling workloads to **Qwen3-8B** by default — set as primary backend in `config/profiles/default.yaml`, configured in `config/models/qwen3-8b.yaml` (4.9 GB GGUF, 6 GB+ VRAM, native tool calling, "thinking mode" for chain-of-reasoning, 119-language coverage). Smaller and weaker models considered (Hermes-2-Pro-Mistral 7B, CodeLlama 7B, Gemma 4 E4B at 5 GB, Phi-2 2.7B for CPU fallback) trade off on different axes; Qwen3-8B wins for AICP because it's the only 7-8B-class model that simultaneously: (a) fits the 8 GB single-GPU baseline, (b) supports thinking mode via a single config flag, (c) ships native tool-calling (no prompt-template hacks), (d) has 119-language coverage. The decision is profile-overridable: `fleet-light` uses Gemma 4 E2B; `dual-gpu` uses Qwen3-30B-A3B MoE; `code-review` pairs Qwen3-8B with low-temperature config. Qwen3-8B is the default; not the only choice.

## Decision

> [!success] Default to Qwen3-8B for general reasoning. Override per profile when workload favors different tradeoffs.
>
> | Workload | Active model (per profile) |
> |----------|----------------------------|
> | General reasoning, code analysis, tool calling | **Qwen3-8B** (default profile) |
> | Heartbeat / fleet-light operations | Gemma 4 E2B (53 tok/s, multimodal, smaller VRAM) |
> | Architecture / security audit | Qwen3-8B + thorough profile |
> | Code review / structured output | Qwen3-8B + code-review profile (low temp, structured output emphasized) |
> | MoE / heavy reasoning | Qwen3-30B-A3B (dual-gpu profile, 19 GB VRAM, runnable since 2026-04-17) |
> | Vision tasks | Gemma 4 E4B (preferred multimodal) or LLaVA 7B (legacy) |
> | CPU fallback (no GPU) | Phi-2 2.7B (last resort) |

Default is `qwen3-8b` config (thinking mode ON). `qwen3-8b-fast` variant (thinking OFF, structured output emphasized) is selected for low-latency workloads.

## Alternatives

### Alternative 1 — Hermes-2-Pro-Mistral 7B as default

Previous legacy AICP default. Well-tuned for instruction following.

> [!warning] Rejected: Hermes-2-Pro is older generation (Mistral 7B base, 2023-2024). Qwen3 (2025) was trained on substantially more data with native tool-calling and thinking-mode config that Hermes lacks. Hermes requires explicit prompt templates for tool-calling AICP's router would assemble; Qwen3-8B's is native and reliable. Hermes is English-strong; Qwen3 handles 119 languages. On AICP's qualitative test set (router complexity scoring + breaker reasoning + skill loading), Qwen3-8B produced more consistent structured outputs. Hermes remains in `config/models/hermes.yaml` as legacy.

### Alternative 2 — CodeLlama 7B for code-heavy workloads

Specialized for code generation.

> [!warning] Rejected as default (kept as specialist): CodeLlama is excellent for code COMPLETION but less general for code REASONING (architecture decisions, debugging hypotheses, refactor analysis). AICP's workload mix is ~30% code generation, ~70% mixed (analysis, planning, document authoring). A code-specialist default would underperform on the 70%. Remains in `config/models/codellama.yaml` for raw code completion.

### Alternative 3 — Gemma 4 E4B as default

Google's 2026 multimodal model. ~5 GB GGUF, 6 GB+ VRAM, vision + audio + text.

> [!warning] Rejected as default (kept as multimodal specialist): Gemma 4 E4B is right when MULTIMODAL inputs are present. For pure text reasoning, Qwen3-8B's thinking mode produces better reasoning chains in informal benchmarks. Gemma's strength is breadth; Qwen's is depth. Default goes to depth; multimodal stays profile-selectable.

### Alternative 4 — Always route to Claude — skip local entirely

Forget local; route everything to Claude.

> [!warning] Rejected: contradicts AICP's stated mission ("LocalAI independence — progressive offload from Claude to LocalAI"). The 5-stage roadmap targets ~80% Claude token reduction by Stage 5. Defaulting to Claude means Stage 2 (route simple ops to LocalAI) never happens. Qwen3-8B as default is the operational expression of the mission's local-first commitment.

### Alternative 5 — Smallest sufficient model (Qwen3-4B) as default

Use Qwen3-4B (3.3 GB). Half the VRAM, half the load time.

> [!warning] Rejected as default (kept for fleet-lightweight): Qwen3-4B is useful for fleet heartbeats and structured-format tasks, but for general reasoning the quality drop is meaningful. Thinking-mode chain quality, tool-calling reliability under ambiguous inputs, multi-turn coherence all favor 8B over 4B. Default targets typical operator workload; 4B is deployed where size/quality tradeoff favors size.

## Rationale

> [!info] Evidence-backed reasons
>
> 1. **Thinking mode + tool-calling are config flags, not prompt hacks.** Qwen3-8B enables thinking via `thinking: true`; tool calls are native with structured schemas. AICP's router doesn't template-engineer these; it sets flags. Hermes/CodeLlama require AICP to assemble prompt templates — duplicated logic that drifts.
>
> 2. **8B fits 8 GB → 19 GB hardware comfortably.** Single-active-backend pattern reserves GPU for ONE chat model. Qwen3-8B at 4.9 GB fits 6 GB+ VRAM with margin for KV cache + context. On 19 GB dual-GPU, qwen3-8b shares space with embedders + reranker AND leaves room for occasional swap to qwen3-30b. Larger default (qwen3-14b) would saturate 8 GB baseline.
>
> 3. **119-language coverage is operationally useful.** AICP serves multiple projects (openfleet, second brain, NNRT) and may accept multilingual tasks. Hermes/CodeLlama are English-strong; Qwen3-8B is broadly multilingual.
>
> 4. **`config/models/qwen3-8b.yaml` is operationally proven.** AICP has run qwen3-8b as default since 2026-Q1 transition off Hermes. Model swap, watchdog timeouts, GPU loading, warmup behavior all calibrated for qwen3-8b specifics (4.9 GB load, ~10-30 s cold start, ~1-1.2 s warm). Re-tuning for a different default would be substantial work.
>
> 5. **Fast variant covers latency-sensitive workloads** without changing the default. `qwen3-8b-fast.yaml` disables thinking + emphasizes structured output. For fleet / high-throughput, gives ~2× throughput at qwen3-8b-class quality.
>
> 6. **Profile system makes the choice safely reversible.** Per [[4-tier-router-with-profiles-over-hardcoded-routing|4-tier router decision]], model selection is per-profile. Switching default = one-line edit in `config/profiles/default.yaml`. Other profiles keep their overrides.

## Reversibility

**Easy** — `config/profiles/default.yaml` `backends.local.model: qwen3-8b`. Change name, run `make profile-validate` + `make profile-use PROFILE=default`. Tests pass against any OpenAI-compatible model.

Cost scales with embeddedness:
- Routine swap (→ gemma4-e4b): minutes
- Architectural swap (drop thinking mode entirely): days (router scoring + skill expectations need updating)
- Drop Qwen3 family entirely: hours (delete `config/models/qwen3-*.yaml`, switch dual-gpu away from qwen3-30b-a3b, retune circuit breakers)

## Dependencies

If reversed (switch primary away from Qwen3-8B):

- `config/profiles/default.yaml` `backends.local.model` — the one-line change
- `config/profiles/code-review.yaml` + `thorough.yaml` also reference qwen3-8b — would need updating
- Router complexity scoring (`aicp/core/router.py`) — thresholds calibrated for qwen3-8b's envelope
- Skill model overrides (`.claude/skills/*/SKILL.md` `model:` field) — many reference qwen3-8b
- KB embeddings (nomic-embed CPU) — unaffected by chat model change
- Testing — `make benchmark-qwen3` exists; new benchmark target needed

If extended (add a new model as default candidate):

- `config/models/<new>.yaml` — define
- `make benchmark-<model>` + A/B vs Qwen3-8B
- If wins, edit `config/profiles/default.yaml`
- Consider existing profiles adoption

## Relationships

- BUILDS ON: [[model-local-ai|Model — Local AI ($0 Target)]] (Qwen3 family highlighted as covering "most text tasks")
- RELATES TO: [[localai-over-ollama-vllm-for-multi-model-orchestration|Decision — LocalAI over Ollama/vLLM]] (sibling — the runtime that hosts qwen3-8b)
- RELATES TO: [[4-tier-router-with-profiles-over-hardcoded-routing|Decision — 4-Tier Router with Profiles]] (the router; qwen3-8b is the local tier's default)
- RELATES TO: [[single-active-backend-with-lru-eviction|Single-Active Backend with LRU Eviction]] (runtime pattern determining qwen3-8b's GPU residency vs swap-out)
- RELATES TO: [[asymmetric-kv-cache-quantization-q4-keys-q2-values|Decision — Asymmetric KV Cache Quantization]] (sibling — how to fit this model)

## Backlinks

[[model-local-ai|Model — Local AI ($0 Target)]]
[[Decision — LocalAI over Ollama/vLLM]]
[[Decision — 4-Tier Router with Profiles]]
[[single-active-backend-with-lru-eviction|Single-Active Backend with LRU Eviction]]
[[Decision — Asymmetric KV Cache Quantization]]
