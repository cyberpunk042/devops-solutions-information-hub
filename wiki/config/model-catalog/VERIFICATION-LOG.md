# Model catalog — verification log

Records what has been checked against reality (Hugging Face) and what remains,
so `status` is always traceable to a source, never asserted from memory. Method:
Hugging Face MCP `hub_repo_details` / `hub_repo_search` (outbound HF is gated
behind the proxy, so this is an operator-approved step, not autonomous).

## 2026-07-02 — first pass

**Confirmed REAL** (source + `status: real` set from live HF lookup):

| catalog id | HF repo | note |
|---|---|---|
| microsoft-bitnet-b158-2b | `microsoft/bitnet-b1.58-2B-4T` | added — the canonical released BitNet (850M, arxiv 2504.12285) |
| 1bitllm-bitnet-b158-large | `1bitLLM/bitnet_b1_58-large` | 729M |
| falcon3-10b-158bit-prequantized | `tiiuae/Falcon3-10B-Instruct-1.58bit` | 3181M |
| falcon-e-3b | `tiiuae/Falcon-E-3B-Instruct` | BitNet edge; reported 864M despite "3B" name |
| spectra-trilm-3.9b | `SpectraSuite/TriLM_3.9B_Unpacked` | 3992M ternary |
| openthinking-7b | `open-thoughts/OpenThinker-7B` | real name **OpenThinker**; Qwen2.5-7B finetune — **not ternary** (corrected) |
| hyenadna | `LongSafari/hyenadna-medium-450k-seqlen-hf` | genomics |
| evo-arc-institute | `arcinstitute/evo2_7b` | Arc Institute; `togethercomputer/evo-1-131k-base` is the earlier release |
| esmfold | `facebook/esmfold_v1` | protein folding |
| bge-m3 | `BAAI/bge-m3` | embedding (already sourced) |
| starcoder2-3b | `bigcode/starcoder2-3b` | code (already sourced) |

**Marked ASPIRATIONAL** (evidence-based — looked, not found):
- `bitnet-70b`, `bitnet-70b-132k-context` — no public 70B/120B BitNet on HF;
  the real BitNet is the 2B above. Kept as targets.

**Explicitly left UNVERIFIED** (a lookup refuted the guess):
- `qwen25-coder-72b-158` — `Qwen/Qwen2.5-Coder-72B-Instruct` returned
  *not found* (the real Qwen2.5-Coder line tops out at 32B). Do not mark real.

## Next sweep — candidate targets

The remaining 42 unverified split into two buckets a future approved pass should
resolve differently:

1. **Real base, ternary variant is a quantization target** — verify the BASE
   exists, then treat the `-ternary` entry as "quantize this base":
   `phi-3-mini-ternary` / `security-phi-3-mini` (→ `microsoft/Phi-3-mini-*`),
   `codellama-ternary-34b` (→ `codellama/CodeLlama-34b-*`),
   `deepseek-r1-ternary-8b` (→ `deepseek-ai/DeepSeek-R1-Distill-Llama-8B`),
   `qwen25-32b-trit-uniform` (→ `Qwen/Qwen2.5-32B`),
   `llama3-8b-ternary` (→ `meta-llama/Llama-3.1-8B`),
   `mistral-large-ternary-80b` (→ `mistralai/Mistral-Large-*`),
   `gemma-4-litert-2b` (→ current Gemma), `deepseek-v3-ternary`.
2. **Coined / internal names** — likely `aspirational`; a HF search returning
   nothing is the evidence to set it (e.g. `hive-gate-7b`, `hackerlm-tiny-3b`,
   `nexus-spec-1.1b`, `prism-ml-ternary-bonsai-70b`, `trm-*`, `logic-loop-8b`,
   `tiny-ternary-ui-3b`, `ternalm3-*`, `rlm-code-reasoner-8b`, …).
3. **Research tools, not HF-loadable models** — `rosettafold-all-atom`,
   `alphafold3`, `openfold`, `warp-lang` exist as code/libraries, not HF model
   repos; record their real home (GitHub/DeepMind/NVIDIA) rather than an HF id.

Rule: only ever move a model to `real` with a confirmed `source`, or to
`aspirational` after a lookup finds nothing. Absent a check, it stays
`unverified`.

## 2026-07-02 — second pass (base models for bucket 1)

Verified the real BASE models behind the `-ternary` quantization targets and
recorded each via a new `base_model` field. The variant itself stays
`unverified` (the quantized artifact isn't a published repo), but is now
**actionable** — you know exactly what to quantize.

| catalog id | verified base (HF) | base params |
|---|---|---|
| phi-3-mini-ternary, security-phi-3-mini | `microsoft/Phi-3-mini-4k-instruct` | 3821M |
| codellama-ternary-34b | `codellama/CodeLlama-34b-Instruct-hf` | 33744M |
| deepseek-r1-ternary-8b | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` | 8030M |
| qwen25-32b-trit-uniform | `Qwen/Qwen2.5-32B` | 32764M |
| llama3-8b-ternary | `meta-llama/Llama-3.1-8B` | 8030M (gated) |
| mistral-large-ternary-80b | `mistralai/Mistral-Large-Instruct-2411` | **122610M (123B, not 80B — size corrected)** |

Fleet now: 11 real · 2 aspirational · 42 unverified (**7 of the unverified are
base-backed** — real upstream known, quant is the only open step).

**Still open (bucket 2 — likely aspirational, need a HF search to confirm
absence):** `hive-gate-7b`, `hackerlm-tiny-3b`, `nexus-spec-1.1b`,
`prism-ml-ternary-bonsai-70b`, `trm-logic-validator-2b`, `trm-recursive-reasoner`,
`logic-loop-8b`, `tiny-ternary-ui-3b`, `ternalm3-15b-instruct`, `ternlm-3-8b-instruct`,
`rlm-code-reasoner-8b`, `thinking-machines-interaction-1b`, `document-ternary-3b`,
`recursive-ref-validator-2b`, `bitnet-math-expert-30b`, `linux-kernel-tiny-1.5b`,
`llama-ternary-context-1b`, `bash-tiny-coder-1b`, `flex-prompt-tiny-1b`,
`owasp-ternary-3b`, `ternarylm-132m`, `nexus-spec-1.1b`, `zihan-wang-coe`,
`xinyuan-t-moe-8x7b`, `qwen-coder-ternary`, `llama-3-tiny-3b`, `mistral-tiny-3b`,
`mistral-2b-ternary`, `llama-3-thought-8b`, `gemma-4-litert-2b`, `deepseek-v3-ternary`,
`qwen25-coder-72b-158`.

**Bucket 3 (not HF-loadable models):** `rosettafold-all-atom`, `alphafold3`,
`openfold` (GitHub/DeepMind code), `warp-lang` (NVIDIA Python lib) — record their
real home, not an HF id.
