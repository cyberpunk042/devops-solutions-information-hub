---
date: 2026-04-17
type: operator-directive
action: ingest-expand
status: in-progress
---

# 2026-04-17 — Directive: Open-Model Landscape + gpt-oss

## Verbatim operator message

> is this limited ? isn't there a fact that the open models are now competing ? about about gpt-oss ?
> continue

## What this says

1. The AirLLM synthesis positioned disk-offload too narrowly — as "batch tier only." Operator is pushing for the broader landscape framing: open models are no longer second tier; they compete.
2. Specifically calls out gpt-oss — OpenAI's open-weight model release (gpt-oss-20b and gpt-oss-120b, Apache 2.0). This is a watershed I did not address.
3. "continue" — don't pause, expand the ingestion.

## What this requires me to address

- **gpt-oss specifically**: research architecture, active-param count, capabilities, hardware requirements, how it fits AirLLM / in-VRAM strategies. This deserves its own source-synthesis.
- **Landscape-level reframing**: the Local AI model has a "Breakthrough Evidence — Small Models Can Win" section but not a "Open Models Now Compete" section. The evidence has accumulated (DeepSeek V3/R1, Qwen3, Llama 4, Mistral Large 3, gpt-oss, Hermes 4). Need to name the landscape shift.
- **MoE + AirLLM math correction**: gpt-oss-120b is ~5B active params per token. Layer-wise streaming math changes for MoE — you do not stream dense 120B worth of weights per token, you stream only the active experts. My AirLLM latency table assumed dense models. Need to add MoE math.
- **Routing implication**: if a 120B MoE with 5B active ≈ same effective bandwidth as a 5B dense stream, then AirLLM + gpt-oss-120b might be interactive-viable, not batch-only. This flips the strategic framing.

## Action plan

1. Fetch gpt-oss sources (OpenAI announcement + GitHub + model card).
2. Fetch/verify open-model landscape data (Hermes 4, DeepSeek V3 current status).
3. Create dedicated gpt-oss source-synthesis page.
4. Evolve Model — Local AI with a "Open Models Compete — 2026 Landscape" section.
5. Update the AirLLM synthesis: add MoE-aware latency math + gpt-oss as first-class test target.
6. Run pipeline post.
