# User Directive — 2026-05-15 — SAIN-01 Sovereign Node Ingestion via Info-Hub Workflow

## Verbatim

### Initial framing (2026-05-15, session opening)

> I am now going to give you information from another conversation about our future and 1-bit models. lets start with the start though, I will dumb all this. Its important data but keep in mind its AI and contain piece of hallucination and clear ignorance of this context but at the same time there are reality and important points like the future custom OS and the new build / hardware of this machine and then later other things and 1-bit notion and 512bit advantages and ideas
>
> I just pushed the latest information-hub, we can do the ingestion through it and follow the proper workflow and when we are ready we will transpose into the selfdef and the new Development and Epics and Modules and Tasks needed to get there and all the Spec files and requirements and clear vision.

### Topic add — DFlash + HF model candidates (mid-dump, 2026-05-15)

> And there is also Dflash I recently learned about that somehow with code task on model that fit in memory like any functional model in general it can work 3 times faster, does not work on creative tasks in general but interesting topic and place of introspection and knowledge

> There is also those I think will be good candidate in general for the rtx pro 6000 96gb amongs other we will add to the list:
> https://huggingface.co/inclusionAI/Ling-2.6-flash
> https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16

### Execution authorization (after the agent proposed Path A / B / C, 2026-05-15)

> Go for it. DO not minimize, do not reduze, do not conflate, do not hack or try to take shortcuts. we do this right all the way

### Continuation signal (2026-05-15)

> continue

## Interpretation

### Distinct Topics Identified

#### 1. Transposition workflow: another-conversation → info-hub → selfdef

The operator has dumped content from a prior Claude conversation about a project they call **SAIN-01** (Sovereign AI Node). The workflow is two-stage:

1. **Stage 1 — Ingestion via info-hub**: the dump lands in this wiki's L0 raw layer; progressive synthesis through L1 (sources) → L2 (concepts) → L3 (comparisons) → L4 (lessons) → L6 (decisions). Follows the existing wiki's "proper workflow" — `python3 -m tools.pipeline post`, `python3 -m tools.gateway`, stage gates, schema compliance.

2. **Stage 2 — Transposition into selfdef**: once SAIN-01 lives in info-hub at L1-L6 maturity, the parts that affect the `cyberpunk042/selfdef` daemon (deployment on the Sovereign OS, Tetragon policy integration, state-fabric placement on `tank/context`, etc.) become new Epics / Modules / Tasks / Specs in selfdef's existing audit programme.

#### 2. Quality of the source material — caveats acknowledged

Operator explicitly flagged:
- AI-generated content contains **hallucination** ("piece of hallucination")
- Contains **ignorance of THIS context** (the SAIN-01 conversation didn't know about selfdef / info-hub workflow)
- BUT contains **real points worth keeping**: future custom OS, new hardware build, 1-bit notion, 512-bit advantages, ideas

→ Ingestion must filter: preserve verbatim in L0, identify real vs hallucinated at L1 synthesis, build authoritative concept pages at L2 from the real material only.

#### 3. Explicit topics to surface

Operator explicitly named the following technical threads as important:
- **Future custom OS** — Sovereign OS / SAIN-01
- **New hardware build** — Ryzen 9 9900X + RTX PRO 6000 Blackwell 96GB + RTX 3090 24GB + ASUS ProArt X870E-Creator
- **1-bit notion** — BitNet b1.58 ternary weights, `bitnet.cpp` runtime
- **512-bit advantages** — Zen 5 single-cycle AVX-512 datapath
- **DFlash** — operator-described as "3 times faster on code tasks, does not work on creative tasks." Verified real via arXiv:2602.06036 (Feb 2026, Z-Lab) — operator framing matches the paper's "highest gains on math/code, moderate on conversational"
- **HF model candidates for the Blackwell 96GB**:
  - `inclusionAI/Ling-2.6-flash` — verified real, 107B params, bailing_hybrid architecture, MIT
  - `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16` — verified real, 33B params, multimodal MoE

#### 4. Standard for the work

> "DO not minimize, do not reduze, do not conflate, do not hack or try to take shortcuts. we do this right all the way"

The operator's quality bar is explicit. No compression of the dump. No paraphrasing of operator words. No skipping the stage-gated workflow. The info-hub's own standards apply: 0 errors required from `pipeline post`, page minimums (150 lines / 300 / 500 by type), YAML frontmatter compliance, relationship graph maintained.

### Action Items

1. **DONE in this PR (L0 verbatim provenance — sacrosanct)**:
   - This file (operator-directive log per hard rule "ALWAYS log operator directives verbatim in `raw/notes/` BEFORE acting").
   - `raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md` — verbatim transposed content from the other conversation, in user-stated order.

2. **NEXT (separate PR — L1 source-synthesis)**:
   - `wiki/sources/src-sain-01-sovereign-node-spec.md` — synthesis of the SAIN-01 conversation with hallucination map + verified facts
   - `wiki/sources/src-bitnet-b158-ternary-llm.md` — BitNet b1.58 from primary sources (Microsoft paper + `bitnet.cpp` + T-MAC)
   - `wiki/sources/src-dflash-block-diffusion-spec-dec.md` — DFlash from arXiv:2602.06036 + Z-Lab repo + Baseten/Spheron writeups
   - `wiki/sources/src-zen5-avx512-single-cycle.md` — AMD Zen 5 microarchitecture, VPDPBUSD, VNNI from AMD docs

3. **AFTER (L2 concept pages, multiple PRs)**:
   - `concept-1bit-ternary-weights.md`
   - `concept-speculative-decoding-block-diffusion.md`
   - `concept-zfs-tiered-storage-llm-inference.md`
   - `concept-vfio-gpu-isolation-amd-iommu.md`
   - `concept-srp-trinity-pulse-weaver-auditor.md`
   - `concept-dual-ccd-cache-partitioning-9900x.md`

4. **AFTER (L3 comparison pages)**:
   - `cmp-bitnet-vs-fp16-execution-cost.md`
   - `cmp-dflash-vs-eagle3-vs-medusa.md`
   - `cmp-ling-26-flash-vs-nemotron-3-nano-omni.md`

5. **AFTER (master spec artifact in `wiki/backlog/`)**:
   - `wiki/backlog/milestones/sain-01-sovereign-node.md` — milestone definition
   - `wiki/backlog/epics/milestone-sain01/epic-hardware-foundation.md`
   - `wiki/backlog/epics/milestone-sain01/epic-sovereign-os-build.md`
   - `wiki/backlog/epics/milestone-sain01/epic-zfs-storage-layout.md`
   - `wiki/backlog/epics/milestone-sain01/epic-vfio-isolation.md`
   - `wiki/backlog/epics/milestone-sain01/epic-tetragon-guardian-perimeter.md`
   - `wiki/backlog/epics/milestone-sain01/epic-network-segregation.md`
   - `wiki/backlog/epics/milestone-sain01/epic-pulse-vector-runtime.md`
   - `wiki/backlog/epics/milestone-sain01/epic-weaver-state-fabric.md`
   - `wiki/backlog/epics/milestone-sain01/epic-load-balancing-profiles.md`
   - `wiki/backlog/epics/milestone-sain01/epic-dflash-integration.md`
   - `wiki/backlog/epics/milestone-sain01/epic-model-catalog.md`

6. **EVENTUAL (Stage 2 — transposition into selfdef)** — only after L1-L6 maturity in info-hub:
   - New selfdef Epics for the daemon's role on the SAIN-01 host
   - Tetragon policy cross-link with the existing selfdef `agent-guard` module
   - State-fabric integration (selfdef escalations SQLite resident on `tank/context` with `sync=always`)

### Hallucinations / Wrong Tokens — Flagged for Correction at L1 Synthesis

Identified during pre-ingest review of the dump (will be documented in the L1 source-synthesis page with correction notes — DO NOT silently fix in the L0 dump itself; L0 is sacrosanct):

- `bwarw tools-compiler` — not a real Debian package
- `CONFIG_MNATIVE_AMD` — not a real Linux kernel config symbol
- `CONFIG_AQC111` for Marvell 10GbE — wrong symbol; the AQC113C lives under `CONFIG_ATLANTIC`
- `WASMTIME_COMPARE_OPTIONS` — not a real wasmtime environment variable
- `wasmtime compile --target znver5 -O speed` — `--target` takes a triple (`x86_64-unknown-linux-gnu`), not a CPU codename; CPU tuning is via inner Cranelift settings
- `vllm-vulkan` — not a real vLLM backend (vLLM is CUDA-first; Vulkan backend exists in `llama.cpp` only)
- `BitNet-b1.58-13B` — confirmed hallucination via HF hub search; Microsoft's actual releases are b1.58-2B + research-scale 3B
- `Qwen-32B-Ternary-Quant` — not a canonical model ID
- `DeepSeek-R1-Distill-Llama-70B-FP16` — distill exists but standard packaging is BF16, not FP16
- The `friction-audit` script's "≥ 2 x8 widths" check — counts every PCIe x8 link on the system, not scoped to the GPU BDFs (would false-pass with the GPUs at x4)
- OpenZFS `O_DIRECT` semantics — only properly supported from OpenZFS 2.2+; older ZoL silently falls back to buffered. The atomic-state-writer pattern in the dump's Section 21 needs this caveat at L1.

### Verified Facts (from preliminary lookup before commit)

- **DFlash**: verified real — paper [arXiv:2602.06036](https://arxiv.org/abs/2602.06036), repo [github.com/z-lab/dflash](https://github.com/z-lab/dflash). 6× lossless acceleration, 2.5× over EAGLE-3. Math500: 8.02ms → 1.40ms/token. HumanEval: 3.5×+. **Operator's "doesn't work on creative tasks" framing is paper-accurate** — the paper reports "highest gains in mathematical reasoning, followed by coding, while conversational tasks see a more moderate improvement."
- **inclusionAI/Ling-2.6-flash**: 107,494M params (~107B), `bailing_hybrid` architecture, MIT license. At BF16 = ~214GB raw → does NOT fit on 96GB Blackwell at full precision; needs Q4 or MoE-active-only inference. ⚠️ spec must surface this constraint.
- **nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16**: 33,015M params (~33B), NemotronH_Nano_Omni_Reasoning_V3 architecture, multimodal (any-to-any), license "other" (NVIDIA custom — verify terms). At BF16 = ~66GB → fits comfortably on 96GB Blackwell with KV cache headroom.

## Relationships

- FEEDS INTO: `raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md` (the L0 source this directive authorizes ingestion of)
- ENABLES: future `wiki/sources/src-sain-01-sovereign-node-spec.md` (L1 synthesis target)
- ENABLES: future `wiki/backlog/milestones/sain-01-sovereign-node.md` (eventual milestone landing)
- RELATES TO: existing `cyberpunk042/selfdef` repo (Stage 2 transposition target)
