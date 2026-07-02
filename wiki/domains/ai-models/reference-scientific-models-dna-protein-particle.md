---
title: Scientific Models — DNA / Protein / Particle (non-LLM)
aliases:
  - "Scientific Models Catalog"
  - "DNA Protein Particle Models"
type: reference
layer: 2
maturity: seed
domain: ai-models
status: processing
confidence: high
created: 2026-07-02
updated: 2026-07-02
sources:
  - id: note-operator-model-routing-catalog-2026-07-02
    type: note
    file: raw/notes/2026-07-02-operator-model-routing-catalog-handwritten-verbatim.md
    title: Operator handwritten model-routing catalog (verbatim)
    ingested: 2026-07-02
tags: [ai-models, scientific-models, dna, genomics, protein-folding, structure-prediction, physics-sim, non-llm, hardware-tier, evolving]
---

# Scientific Models — DNA / Protein / Particle (non-LLM)

> [!note] Why this lives in the wiki, not the sovereign-os model catalog
> These are the **science models** from the operator's 2026-07-02 handwritten
> catalog (DNA / Protéine / Particules sections). They are **not LLMs**, so they
> don't fit `sovereign-os/models/catalog.yaml`'s `class` enum
> (llm/slm/rlm/ternary-lm/embed/vision/multimodal/code/mixture/speculative/
> reranker/lora-adapter) — no protein-folding / genomics / physics-sim bucket.
> Per operator direction (2026-07-02: *"just document them in the wiki for the
> science stuff"*), they are captured here as knowledge instead. Homes verified
> on HF where a loadable checkpoint exists; the rest are GitHub/DeepMind tools.

## Summary

The operator's handwritten catalog names scientific models across three domains —
**DNA/genomics, protein structure prediction, and particle/physics simulation** —
routed by hardware tier (RTX 4090 vs RTX Pro), alongside the LLM fleet. These are
specialist scientific tools (some on Hugging Face as loadable checkpoints, some
distributed as GitHub/DeepMind code), captured here because they fall outside the
LLM model catalog's taxonomy while remaining part of the operator's model landscape.

## Catalog (task × hardware tier)

| Domain | Model | Tier (per notes) | Real home | On HF? |
|---|---|---|---|---|
| **DNA / genomics** | Evo (Arc Institute) | RTX 4090 | `arcinstitute/evo2_7b` (Evo 2); `togethercomputer/evo-1-131k-base` (Evo 1, stripedhyena) | ✅ verified 2026-07-02 |
| **DNA / genomics** | HyenaDNA | RTX 4090 | `LongSafari/hyenadna-medium-450k-seqlen-hf` | ✅ verified 2026-07-02 |
| **DNA / genomics** | RoseTTAFold All-Atom (RFAA) | RTX Pro | Baker Lab — GitHub `baker-laboratory/RoseTTAFold-All-Atom` | ❌ code/weights, not an HF model repo |
| **Protein folding** | AlphaFold3 | RTX Pro / 4090 | DeepMind — GitHub `google-deepmind/alphafold3` (weights on request) | ❌ DeepMind-distributed |
| **Protein folding** | ESMFold | RTX 4090 | `facebook/esmfold_v1` | ✅ verified 2026-07-02 |
| **Protein folding** | OpenFold | RTX 4090 | AQ Laboratory — GitHub `aqlaboratory/openfold` | ❌ code/weights, not an HF model repo |
| **Particle / physics sim** | Warp-Lang (NVIDIA) | RTX 4090 / RTX Pro | NVIDIA — GitHub `NVIDIA/warp` (Python/CUDA differentiable-sim library) | ❌ a library, not a model |

## Key Insights

- **Three of seven are HF-loadable** (Evo, HyenaDNA, ESMFold) — verified live on
  HF 2026-07-02. The other four (RoseTTAFold-All-Atom, AlphaFold3, OpenFold,
  Warp) are real but distributed as GitHub/DeepMind code + weights, not HF model
  repos; do not expect a `pull.sh` / `hf_repo_id` path for them.
- **They intentionally sit outside the LLM catalog.** `sovereign-os/models/
  catalog.yaml` models the Genesis-Trinity LLM fleet; forcing a protein-folding
  model into its `class` enum would be dishonest. If the operator later wants
  them hosted by sovereign-os, that needs a schema extension (new `class`
  values: e.g. `structure-prediction`, `genomics`, `sim`) — an explicit call.
- **Hardware-tier routing still applies** — the notes place the heavy
  all-atom/structure models (RoseTTAFold-All-Atom, AlphaFold3) on RTX Pro and
  the lighter sequence models (Evo, HyenaDNA, ESMFold) on the 4090.

## Relationships

- RELATES TO [[reference-local-model-routing-catalog|Local Model Routing Catalog]] — the LLM half of the same operator handwritten catalog; these are its science half.
- BUILDS ON [[concept-1bit-ternary-weights]] — contrast: the LLM fleet is ternary-weighted for local hosting; these science models run at native precision.
