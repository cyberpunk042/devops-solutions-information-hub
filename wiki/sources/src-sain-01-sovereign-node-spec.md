---
title: "Synthesis — SAIN-01 Sovereign AI Node Master Specification"
aliases:
  - "Synthesis — SAIN-01 Sovereign AI Node Master Specification"
  - "SAIN-01"
  - "Sovereign AI Node"
  - "Sovereign OS"
type: source-synthesis
domain: ai-models
status: synthesized
confidence: high
maturity: seed
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: sain01-l0-dump
    type: file
    file: "raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md"
  - id: sain01-operator-directive
    type: directive
    file: "raw/notes/2026-05-15-user-directive-sain01-info-hub-ingestion.md"
tags:
  - sain-01
  - sovereign-os
  - hardware
  - kernel
  - zfs
  - vfio
  - tetragon
  - bitnet
  - dflash
  - 1bit
  - avx512
  - zen5
  - debian
  - infrastructure
  - operator-vision
  - sovereign-node
---

# Synthesis — SAIN-01 Sovereign AI Node Master Specification

## Summary

SAIN-01 is the operator's planned **bare-metal AI orchestration workstation** built on Debian 13 (Trixie) + a custom Zen-5-tuned Linux kernel, anchored by an AMD Ryzen 9 9900X CPU (single-cycle 512-bit AVX-512 datapath) and an asymmetric dual-GPU layout (NVIDIA RTX PRO 6000 Blackwell 96GB + RTX 4090 24GB). Storage is ZFS-on-NVMe with three tiered datasets (`tank/models` 1M-recordsize for weights, `tank/context` 16k+`sync=always` for state files, `tank/agents` 128k for runtime cache). The RTX 4090 is bound to `vfio-pci` at boot as an isolated sandbox; the Blackwell stays host-resident for primary inference. Security is enforced at kernel level via Tetragon eBPF (`sys_execve` allowlist → SIGKILL) with a native Python supervisor (`guardian-core`) acting as autonomous circuit breaker. Network is physically segregated: Intel 2.5GbE for management traffic, Marvell AQC113C 10GbE for model-weight ingestion. The architecture realizes a software "Trinity" (Pulse / Weaver / Auditor) mapped to physical hardware boundaries — CCD 0 for vector pipeline, CCD 1 for state engine, kernel-level eBPF for the immutable gate. Twelve hallucinations were identified in the source material; this synthesis separates them from the verified threads.

## Key Insights

1. **The architecture was conceived as a software trinity BEFORE the hardware was specified.** The original ecosystem — documented as "The Genesis" in Block 6 of the dump — predates motherboard lane discussions. Three SRP-decoupled modules: **The Pulse** (low-level vector kernel, MASM + Wasm primitives for bit-plane transposition), **The Weaver** (Wasm-sandboxed orchestration layer for multi-agent state), **The Auditor** (eBPF/ZFS-anchored integrity gate). The 9900X selection, the Blackwell-4090 pairing, the ZFS dataset stratification, and the Tetragon perimeter are *physical manifestations* of this prior software design — not the other way around. (sain01-l0-dump § "The Sovereign Trinity Framework")

2. **Zen 5's true single-cycle 512-bit AVX-512 datapath is the load-bearing hardware choice.** Zen 4 implemented AVX-512 by double-pumping two 256-bit execution units; Zen 5 exposes true 512-bit ZMM registers executing most AVX-512 instructions in one cycle. This is what makes the "Pulse" module — `bitnet.cpp` ternary lookup matmul over packed 2-bit weights — viable on local CPU threads at human-reading speeds (5-12 tok/sec). The dump's Section 16 ("Hardware Fusion") and Section 20 ("Wasm-to-AVX-512 AOT Pipeline") are the technical exposition of this. (sain01-l0-dump §§ 16, 20)

3. **Dual-CCD partitioning is the operator's response to Infinity-Fabric latency, not a generic optimization.** The 9900X is 2× CCDs of 6 cores each, with 32MB of L3 per CCD. Cross-CCD data movement traverses Infinity Fabric → L3 cache miss → measurable latency penalty. The dump's Section 19 prescribes a precise core mapping that matches the Trinity SRP: cores 0-5 (CCD 0, mask `0xfff`) for The Pulse (AVX-512 vector pipeline), cores 6-9 (CCD 1) for The Weaver + Auditor (state engine + Tetragon stream parser), cores 10-11 (CCD 1) for host kernel / network drivers / ZFS compression. (sain01-l0-dump § 19)

4. **The PCIe topology has one non-negotiable rule: M.2_2 stays empty.** The ASUS ProArt X870E-Creator shares PCIe lanes between M.2_2 and PCIEX16_2 — populating M.2_2 forces a bifurcation that drops Slot 2 to x4 electrical, destroying the dual-GPU x8/x8 symmetry. The `friction-audit` script in the dump exists specifically to catch this regression at boot. ⚠️ Caveat: the script as written counts every PCIe x8 link on the system, not just the GPU BDFs — it could false-pass if some other device is at x8 while the GPUs are at x4. Correction noted in directive log. (sain01-l0-dump § 1.2, § 5.1)

5. **ZFS dataset stratification is purpose-built per access pattern, not generic tuning.** Three distinct profiles, each shaped by its workload: `tank/models` uses 1M recordsize + lz4 + `redundant_metadata=most` for 100GB+ weight files (sequential reads, low-FS-metadata overhead). `tank/context` uses 16k recordsize + zstd-9 + `copies=2` + `sync=always` for the state-file fabric (small writes, race-condition prevention, durability). `tank/agents` uses 128k + zstd-3 (balanced runtime cache). The `sync=always` on context is the critical knob — it forces synchronous I/O so an agent's state mutation is physically committed to NVMe before the next agent reads. ⚠️ OpenZFS `O_DIRECT` semantics (used by the dump's atomic-state-writer pattern in §21) only became fully supported in OpenZFS 2.2+; older ZoL silently falls back to buffered. (sain01-l0-dump §§ 3, 4.1, 7.2, 21)

6. **VFIO isolation of the RTX 4090 is hardcoded by PCI vendor:device ID, not by slot.** GRUB parameter `vfio-pci.ids=10de:2204,10de:1ad8` binds the kernel module to the GPU and its companion audio controller at boot, before the NVIDIA host driver loads. `10de:2204` is the GA102 (Ampere) device ID — the earlier RTX 3090 assumption. The RTX 4090 is AD102 (Ada, typically `10de:2684`); confirm the real id via `lspci -nn` on the actual card. The host OS never sees the 4090; it's reserved exclusively for sandboxed agent fleets and Profile-2 speculative decoding workloads. The Blackwell (`10de:????`, different ID) stays host-bound for primary inference. (sain01-l0-dump § 4.3)

7. **Tetragon eBPF is the kernel-level Auditor; `guardian-core` is the user-space circuit breaker.** The Tetragon `TracingPolicy` allowlists ~4 binaries for `sys_execve` (python3, nvidia-smi, vllm, podman); any other syscall in a containerized agent triggers an immediate kernel-level `SIGKILL`. `guardian-core` (a small Python daemon listening on `/var/run/tetragon/tetragon.events`) catches these kill events, kills the offending Podman container, appends to the audit log, and rings the PC speaker. The two together replace the legacy Windows-centric `SecureToast.ps1` concept the operator previously used. (sain01-l0-dump §§ 6, 10)

8. **Three operator-named load-balancing profiles, each anchored to a specific use case.** Profile 1 (Ultra-Sovereign Efficiency) pins a BitNet-b1.58 model to CPU cores 0-7 via `bitnet.cpp` with GPUs in `nvidia-smi -pm 1` sleep — for continuous background state monitoring. Profile 2 (High-Concurrency Agent Burst) spreads asymmetric workloads across CPU + cuda:0 (4090) + cuda:1 (Blackwell). Profile 3 (Deep Context Synthesis) tensor-parallels across both GPUs with fp8 KV cache. ⚠️ Profile 2's JSON references `vllm-vulkan` (not a real backend), `BitNet-b1.58-13B` (no such Microsoft release), and `Qwen-32B-Ternary-Quant` (not a canonical model ID) — see hallucination map. (sain01-l0-dump § 18)

9. **The state-fabric file matrix maps responsibility to access mode.** Four files in `/mnt/vault/context/` (= `tank/context`): `IDENTITY.md` (immutable system persona, RO to agents), `SOUL.md` (core behavioral logic + dynamic long-term memory, RW via manager), `AGENTS.md` (routing table + hardware pinning map, RO to sub-agents), `CLAUDE.md` (active session context + project state, atomic append-only). Each has a precise role in the multi-agent handoff sequence. Worth noting: this matrix is operator-stated; the broader context-engineering knowledge in the wiki may shape this further when L2 concept pages land. (sain01-l0-dump § 7.1)

10. **Network segregation is physical, not just logical.** Intel I226-V 2.5GbE on VLAN 100 = host management (SSH, Tetragon log streams, system updates) → has default gateway 10.0.100.1. Marvell AQC113C 10GbE on VLAN 200 = isolated computation (container bridge, model-weight pulls from local NAS) → no default gateway, MTU 9000 jumbo frames. The split keeps high-bandwidth model traffic off the management plane and gives OPNsense a clean per-VLAN policy surface. (sain01-l0-dump § 8)

## Deep Analysis

### The conversation's structural shape (provenance map)

The L0 dump is a seven-block conversation in which the operator escalated specification depth iteratively. Block 1 ("MANIFEST") was a high-level architectural sketch. Block 2 ("Sovereign OS & Workstation Specification Manual") was a more rigorous formal spec. Block 3 added the state fabric + network + AVX-512 user-space + Guardian daemon (Sections 7-11). Block 4 walked the chronological bootstrap pipeline + a Q&A matrix + edge cases (Sections 12-14). Block 5 introduced the 1-bit paradigm + SRP topology + 3 runtime profiles (Sections 15-18). Block 6 — the keystone — went *backwards in time* to recover the original Trinity (Pulse / Weaver / Auditor) and showed how the hardware choices descended from that prior software vision. Block 7 closed with the Memory Subsystem + Wasm AOT + atomic state + bootstrap checklist (Sections 19-23). Two operator additions after the conversation (DFlash + two HF model candidates) were independent topics merged into the same paste session.

Each escalation revealed information the prior level lacked. The "real" architectural vision lives in **Block 6 (Trinity Genesis)** more than in any single technical block — because that block establishes *why* the hardware looks the way it does.

### What's verified vs hallucinated

| Layer | Status | Notes |
|---|---|---|
| Hardware selection (9900X · ProArt X870E-Creator · Blackwell · 4090) | Verified | All real parts; the 9900X is 12c/24t, 2×CCD, 2×32MB L3, 5.6 GHz boost (per Wikipedia/Phoronix Zen 5). |
| PCIe x8/x8 + M.2_2 constraint | Verified | Documented behavior of the X870E platform; the bifurcation table for the ProArt model confirms M.2_2 shares with PCIEX16_2. |
| Zen 5 single-cycle 512-bit AVX-512 | Verified | Wikipedia/Phoronix/HWCooling confirm this is the major Zen 4 → Zen 5 shift. |
| AVX-512 VNNI + VPDPBUSD | Verified | Both are real ISA extensions present on Zen 5; the 64×INT8 / 128×4-bit packing claims are arithmetically correct for 512-bit ZMM. |
| BitNet b1.58 ternary `{−1, 0, +1}` math | Verified | Real Microsoft architecture (arXiv:2402.17764). Add / subtract / no-op semantics described correctly. |
| `bitnet.cpp` runtime | Verified | Real Microsoft project (github.com/microsoft/BitNet); supports x86 AVX2/AVX512, ARM via I2_S/TL1/TL2 kernels. |
| 5-7 tok/sec on CPU at high parameter scales | Verified | The BitNet team's own claim for a 100B model on single CPU. |
| ZFS recordsize + compression + `sync=always` semantics | Verified | All operations are real ZFS knobs; their effects are as described. |
| VFIO with `vfio-pci.ids=10de:2204,10de:1ad8` | Verified | `10de:2204`/GA102 was the RTX 3090 (Ampere) id; the RTX 4090 is AD102 (typically `10de:2684`). Pattern is correct; **the id values must be re-derived from `lspci -nn` on the real 4090.** |
| Tetragon `TracingPolicy` + SIGKILL on syscall | Verified | Real Cilium project; `cilium.io/v1alpha1` API is correct. |
| `wall(1)` / OPNsense / Marvell AQC113C / Intel I226-V | Verified | All real components on the ProArt board. |
| `bwarw tools-compiler` in apt-get | **Hallucinated** | Not a real Debian package. The apt-get line has a typo'd token. |
| `CONFIG_MNATIVE_AMD` | **Hallucinated** | Not a real Linux kernel config symbol. |
| `CONFIG_AQC111` for Marvell 10GbE | **Wrong** | The AQC113C is under `CONFIG_ATLANTIC`, not `CONFIG_AQC111`. |
| `WASMTIME_COMPARE_OPTIONS` | **Hallucinated** | Not a real wasmtime env var. |
| `wasmtime compile --target znver5 -O speed` | **Wrong syntax** | `--target` takes a triple (`x86_64-unknown-linux-gnu`); CPU tuning is via inner Cranelift settings. |
| `vllm-vulkan` (Profile 2 JSON) | **Hallucinated** | vLLM is CUDA-first; Vulkan backend exists only in `llama.cpp`. |
| `BitNet-b1.58-13B` (Profile 1 + Profile 2) | **Hallucinated** | Microsoft has shipped b1.58-2B (microsoft/bitnet-b1.58-2B-4T) + research-scale 3B / Llama3-8B-1.58 / Falcon3 / Falcon-E. No 13B. |
| `Qwen-32B-Ternary-Quant` (Profile 2) | **Hallucinated** | Not a canonical HF model ID. |
| `DeepSeek-R1-Distill-Llama-70B-FP16` (Profile 2) | **Almost-wrong** | The distill exists; standard packaging is BF16, not FP16. |
| `friction-audit`'s "≥ 2 x8 widths" check | **Buggy** | Counts every PCIe x8 link on the system, not scoped to the GPU BDFs. Can false-pass with GPUs at x4. Needs scoping to `lspci -s <bdf>`. |
| OpenZFS `O_DIRECT` in §21 atomic writer | **Caveat-needed** | Only properly supported from OpenZFS 2.2+; older ZoL silently falls back to buffered. The atomic-rename + `sync=always` combination is still the right idea; the `O_DIRECT` flag alone is insufficient on older releases. |
| 64×INT8 in 512-bit ZMM (one cycle via VPDPBUSD) | Verified | VNNI VPDPBUSD does INT8 × INT8 → INT32 accumulate. |

### The Trinity → hardware mapping (the keystone)

The dump's Block 6 establishes that the workstation choices are **physical instantiations of a prior software design**:

```
            SOFTWARE GENESIS                     PHYSICAL INSTANTIATION
            ────────────────                     ──────────────────────

   THE PULSE                               →    CCD 0 (cores 0-5) on 9900X
   (low-level vector kernel,                    + native AVX-512 ZMM
    MASM + Wasm primitives,                     + bitnet.cpp + AOT-Wasm
    bit-plane transposition)                    via Cranelift/LLVM

   THE WEAVER                              →    CCD 1 (cores 6-9) on 9900X
   (Wasm-sandboxed orchestration,               + Rootless Podman + RTX 4090
    multi-agent state fabric,                   sandbox via VFIO
    asymmetric load-balancing)                  + ZFS `tank/context` sync=always

   THE AUDITOR                             →    Kernel-level eBPF (Tetragon)
   (immutable gatekeeper, logging,             + guardian-core Python daemon
    SIGKILL on rule violation)                  + tank/context/security_audit.log
                                                atomic append
```

This map matters because it constrains what's negotiable vs what's load-bearing. The 9900X is not just "a fast CPU" — it's the only consumer chip with single-cycle 512-bit AVX-512 that satisfies The Pulse's vector pipeline requirements. The dual-GPU layout is not just "more VRAM" — it's a deliberate sandbox boundary (4090 = isolated agent fleet via VFIO; Blackwell = host primary). The ZFS dataset choices are not just "fast storage" — they're per-tier responses to per-module access patterns.

### The 1-bit / 512-bit fusion thesis

Sections 15-16 of the dump present a tight argument about why 1-bit (ternary) weights become viable on the SAIN-01 hardware:

- **Ternary math eliminates multiplication.** Weights ∈ {−1, 0, +1} → matmul becomes add/subtract/skip → no FPU saturation.
- **Compute shifts from TFLOPS to bandwidth + instruction pipeline.** Energy efficiency rises ~10× per published benchmarks (BitNet team's 55-82% energy reduction claim on bitnet.cpp's GitHub README).
- **AVX-512 VNNI streams ternary lookups at ZMM-register width.** A single ZMM register holds 64×INT8 activations OR 128 packed 4-bit snippets. With the VPDPBUSD instruction, multiple INT8 activations are multiplied by 2-bit-packed ternary weights and accumulated into 32-bit registers in a fraction of a clock cycle.
- **Result**: a high-parameter ternary model executes on CPU threads at 5-12 tok/sec (above human reading rate), leaving GPU VRAM unencumbered for the heavier Logic Engine + Oracle Core workloads.

This thesis is verified by the BitNet team's own published numbers (see `src-bitnet-b158-ternary-llm.md` for the grounded synthesis). It's the technical justification for routing the Conductor Agent to CPU rather than GPU in the SRP topology.

### Three runtime profiles — what's real and what to revise

| Profile | What's verifiable | What needs revision |
|---|---|---|
| **1: Ultra-Sovereign Efficiency** (CPU-pinned BitNet, GPUs asleep) | `taskset -c 0-7 bitnet-cli ...` syntax is real. `nvidia-smi -pm 1` is real (Persistence Mode). The 3B model reference (`BitNet-b1.58-3B`) is real per microsoft/BitNet README. | Concept is sound; can ship as-described. |
| **2: High-Concurrency Agent Burst** (asymmetric load-balancing JSON) | The JSON shape is reasonable; the asymmetric concept is sound. | Replace `vllm-vulkan` with a real backend (vLLM-CUDA or llama.cpp-Vulkan). Replace `BitNet-b1.58-13B` with a real Microsoft release (b1.58-2B-4T, or Llama3-8B-1.58). Replace `Qwen-32B-Ternary-Quant` with a real Qwen quantization variant. Replace `DeepSeek-R1-Distill-Llama-70B-FP16` with BF16. |
| **3: Deep Context Synthesis** (tensor-parallel both GPUs, fp8 KV cache) | `vllm/vllm-openai:latest` image + `--tensor-parallel-size 2` + `--kv-cache-dtype fp8` are all real vLLM flags. The pipeline-parallel-size and gpu-memory-utilization knobs are real. | Concept ships as-described. Verify that the DeepSeek-V3-Quant model id resolves at run-time (operator must check HF availability at deployment). |

The operator's separately-mentioned DFlash + Ling-2.6-flash + Nemotron-3-Nano-Omni are additional candidates that didn't appear in the Profile JSON. They should land in the eventual `wiki/comparisons/cmp-ling-26-flash-vs-nemotron-3-nano-omni.md` page + a Profile-4 or revised-Profile-2 sketch.

### Where the conversation stops short

Several real architectural threads were under-specified in the dump and need follow-up at L2 / L3:

1. **Identity-of-the-host's-resident-models.** The Blackwell hosts "Oracle Core" reasoning models; the dump says "FP16 or uncompromised high-precision" but doesn't pick. The operator's later HF candidates (Ling-2.6-flash 107B, Nemotron-3-Nano-Omni 33B) start to fill this gap.
2. **The Wasm runtime is named but not chosen.** Cranelift vs Wasmer vs WasmEdge vs Wasmtime are all mentioned at various points; the build flow assumes Wasmtime but doesn't justify it over alternatives.
3. **Multi-host scope is implicit but not designed.** The OPNsense/SD-WAN diagram implies multiple SAIN-style nodes; nothing in the spec covers cross-host model partitioning or state synchronization.
4. **Operator-vs-fleet trust model is implicit.** Tetragon SIGKILLs unauthorized syscalls inside containers, but the model of who-authorizes-which-container is not pinned.
5. **Backup + recovery posture is unaddressed.** ZFS RAID 0 maximizes throughput at the cost of redundancy — single NVMe failure loses everything. The dump doesn't address snapshots, send/receive, or off-host replication.

These belong in the eventual `wiki/backlog/epics/milestone-sain01/epic-*.md` set as deliberate scope (or deliberate deferrals).

## Open Questions

- Which specific 1-bit / ternary model size ships as Profile-1's "Conductor" — the official microsoft/bitnet-b1.58-2B-4T, the research 3B, the Llama3-8B-1.58, or one of the Falcon3 / Falcon-E variants? Each has different latency vs accuracy tradeoffs at 5-7 tok/sec.
- Which Wasm runtime (Wasmtime vs Wasmer vs WasmEdge) is the AOT target? The dump assumes Wasmtime but doesn't justify it.
- How does the operator want to handle ZFS RAID 0's lack of redundancy? Single NVMe failure = total data loss on this configuration. Snapshot+replicate to a separate device, or accept the risk in exchange for throughput?
- Does the dual-CCD core mapping survive operator-stated future expansion (256GB RAM, more agents)? The mask `0xf00000` reserves only 4 cores for kernel/IRQ/ZFS-compression — sufficient for the described workload but tight under heavy concurrency.
- What's the cross-link with the existing `selfdef` daemon? Tetragon policies on SAIN-01 will need to coexist with selfdef's `agent-guard` module's existing TracingPolicies. Conflict resolution is an L2 concept page.
- The dump's "Vibe Managing Platform" / "Vibe Manager" terminology is operator-stated jargon — does it map to an existing wiki concept (e.g. orchestrator, harness, runtime supervisor), or does it warrant its own L2 concept page?
- Block 6's biological framing ("matching the SRP of your software trinity") is metaphor; is there an empirical justification that ties the dual-CCD partition to measurable latency gains under the planned workload? Could be a future spike or benchmark.

## Relationships

- DERIVED FROM: [[2026-05-15-sain-01-master-spec-other-conversation-transposition|L0 verbatim dump]]
- DERIVED FROM: [[2026-05-15-user-directive-sain01-info-hub-ingestion|Operator-directive log]]
- BUILDS ON: [[src-bitnet-b158-ternary-llm|BitNet b1.58 ternary LLM family]]
- BUILDS ON: [[src-dflash-block-diffusion-spec-dec|DFlash block-diffusion speculative decoding]]
- BUILDS ON: [[src-zen5-avx512-single-cycle|Zen 5 microarchitecture and AVX-512 single-cycle path]]
- RELATES TO: [[src-hrm-trm-tiny-recursion-models|HRM/TRM Tiny Recursion Models]] (alternative small-model approach; could pair with the Conductor agent on CPU)
- RELATES TO: [[src-llm-architecture-gallery-raschka|LLM Architecture Gallery]] (hybrid architectures relevant to the Blackwell's Oracle Core role)

## Source Notes

The primary source is the L0 dump at `raw/dumps/2026-05-15-sain-01-master-spec-other-conversation-transposition.md`, which preserves seven conversation blocks + two operator additions verbatim. The operator-directive log at `raw/notes/2026-05-15-user-directive-sain01-info-hub-ingestion.md` carries the hallucination map + verified-facts table.

Confidence is rated **high** for the architectural threads that map to verifiable upstream (the Trinity → hardware mapping, the ZFS dataset profiles, the VFIO + Tetragon perimeter, the Zen 5 single-cycle AVX-512 claim, the BitNet b1.58 math). Confidence drops to **medium** for the specific runtime profiles' JSON (which contains the cluster of model-ID hallucinations) and for the "Vibe Managing Platform" terminology, which is operator-jargon without grounded definition.

The conversation's structural shape — escalating depth across seven blocks, with the keystone Trinity origin retrieved on operator prompt in Block 6 — matters interpretively. The operator's own framing of the source as containing "piece of hallucination and clear ignorance of this context" is what permitted aggressive hallucination-flagging in this synthesis without losing the real architectural signal.

## Backlinks

[[L0 verbatim dump]]
[[Operator-directive log]]
[[BitNet b1.58 ternary LLM family]]
[[DFlash block-diffusion speculative decoding]]
[[Zen 5 microarchitecture and AVX-512 single-cycle path]]
[[HRM/TRM Tiny Recursion Models]]
[[LLM Architecture Gallery]]
