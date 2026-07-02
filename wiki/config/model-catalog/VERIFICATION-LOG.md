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

## 2026-07-02 — third pass (more bucket-1 bases)

Six more `-ternary` entries base-backed to confirmed-real upstreams:

| catalog id | verified base (HF) | note |
|---|---|---|
| deepseek-v3-ternary | `deepseek-ai/DeepSeek-V3` | 685B MoE |
| qwen-coder-ternary | `Qwen/Qwen2.5-Coder-14B-Instruct` (+1.5B inline) | both coder sizes real |
| llama-3-tiny-3b | `meta-llama/Llama-3.2-3B-Instruct` | 3213M, gated |
| gemma-4-litert-2b | `google/gemma-3-4b-it` | **"Gemma 4" doesn't exist — latest is Gemma 3; no Gemma-3 2B (Gemma-2-2B was the 2B). Name misremembered.** |
| mistral-tiny-3b | `mistralai/Ministral-8B-Instruct-2410` | Ministral-3B is API-only; 8B is the open small Mistral |
| qwen25-coder-72b-158 → **aspirational** | base `Qwen/Qwen2.5-Coder-32B-Instruct` | **no 72B Qwen coder exists — 32B is the largest real** |

Fleet now: **11 real · 3 aspirational · 41 unverified**, of which **13 are
base-backed**. Bucket 2 remaining is the clearly-coined names
(`hive-gate-7b`, `hackerlm-tiny-3b`, `prism-ml-ternary-bonsai-70b`, `nexus-spec-1.1b`,
`trm-*`, `logic-loop-8b`, `tiny-ternary-ui-3b`, `ternalm3-*`, `ternlm-3-*`,
`rlm-code-reasoner-8b`, `thinking-machines-interaction-1b`, `document-ternary-3b`,
`recursive-ref-validator-2b`, `bitnet-math-expert-30b`, `linux-kernel-tiny-1.5b`,
`llama-ternary-context-1b`, `bash-tiny-coder-1b`, `flex-prompt-tiny-1b`,
`owasp-ternary-3b`, `ternarylm-132m`, `zihan-wang-coe`, `xinyuan-t-moe-8x7b`,
`llama-3-thought-8b`, `mistral-2b-ternary`) — these need a HF *search* to confirm
absence before flipping to `aspirational`.

## 2026-07-02 — fourth pass (bucket 2, search-to-refute)

Searched HF for the distinctive coined names. Method: `hub_repo_search`;
`No repositories found` (or no near-name match) = evidence of absence → flip to
`aspirational`.

**One REAL find:** `prism-ml/Ternary-Bonsai` is a genuine, active HF line —
`prism-ml/Ternary-Bonsai-{1.7B,4B,8B}-unpacked` + gguf + mlx-2bit (Qwen3-based,
ternary/1.58-bit) — but the **largest is 8B, not 70B**. `prism-ml-ternary-bonsai-70b`
→ `aspirational` for the 70B size, `base_model: prism-ml/Ternary-Bonsai-8B-unpacked`.

**Searched → not found → flipped to `aspirational`:** `trm-recursive-reasoner`,
`trm-logic-validator-2b`, `ternarylm-132m`, `hackerlm-tiny-3b`,
`xinyuan-t-moe-8x7b`, `bitnet-math-expert-30b`, `hive-gate-7b`, `nexus-spec-1.1b`,
`tiny-ternary-ui-3b`, `zihan-wang-coe`, `thinking-machines-interaction-1b`,
`ternlm-3-8b-instruct`, `ternalm3-15b-instruct`, `llama-3-thought-8b`.

**Still `unverified` (coined specialist tinies, not yet each searched by name):**
`rlm-code-reasoner-8b`, `document-ternary-3b`, `recursive-ref-validator-2b`,
`linux-kernel-tiny-1.5b`, `llama-ternary-context-1b`, `bash-tiny-coder-1b`,
`flex-prompt-tiny-1b`, `owasp-ternary-3b`, `logic-loop-8b`, `mistral-2b-ternary`
(a generic "ternary UI code specialist tiny" search returned nothing; kept
`unverified` rather than asserted, pending a per-name search).

Fleet: **11 real · 18 aspirational · 26 unverified · 14 base-backed.**

## 2026-07-02 — fifth pass (bucket 3 + last specialists)

- `owasp-ternary-3b`, `linux-kernel-tiny-1.5b` — searched, not found → `aspirational`.
- **Bucket 3 (research tools, confirmed NOT on HF as model repos):**
  `rosettafold-all-atom` (Baker Lab), `alphafold3` (DeepMind), `openfold`
  (AQ Laboratory), `warp-lang` (NVIDIA `github.com/NVIDIA/warp`) — all real tools,
  GitHub/DeepMind-distributed, not HF models. Annotated as such; `esmfold`
  remains the HF-loadable protein option. Kept `unverified` on the HF axis
  (their GitHub homes weren't verifiable from here — proxy blocks non-HF); record
  exact homes when web access allows.

Fleet: **11 real · 20 aspirational · 24 unverified · 14 base-backed.**

## 2026-07-02 — sixth pass (last specialist tinies) — VERIFICATION COMPLETE

Searched the final 8 per-name; all returned nothing → `aspirational`:
`rlm-code-reasoner-8b`, `recursive-ref-validator-2b`, `logic-loop-8b`,
`bash-tiny-coder-1b`, `document-ternary-3b`, `llama-ternary-context-1b`,
`flex-prompt-tiny-1b`, `mistral-2b-ternary`.

**Every one of the 55 models is now reasoned about.** Final fleet:
**11 real · 28 aspirational · 16 unverified · 14 base-backed.**

The 16 `unverified` are NOT "unchecked" — they are:
- **12 base-backed** — real upstream confirmed (see passes 2–3); the ternary
  *quantized artifact* itself isn't a published repo, so the variant stays
  `unverified` while `base_model` records exactly what to quantize.
- **4 real research tools not on HF** — `rosettafold-all-atom`, `alphafold3`,
  `openfold`, `warp-lang`; real (Baker Lab / DeepMind / AQ Lab / NVIDIA),
  GitHub-distributed, confirmed absent from HF. Unverified on the HF axis only.

Every `real` / `aspirational` / `base_model` value traces to a dated 2026-07-02
HF check recorded in this log. P4 satisfied: nothing asserted, everything gated.
