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
