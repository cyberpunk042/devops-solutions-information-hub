---
title: "Directive — 2026-04-22 — Post-Anthropic Self-Autonomous Stack Plan (Thorough)"
date: 2026-04-22
type: directive
tags: [directive, milestone, epics, self-autonomous, kimi-k2-6, openrouter, openrouter-anthropic-skin, harness-neutral, post-anthropic, verbatim]
---

# Directive — 2026-04-22 — Post-Anthropic Self-Autonomous Stack Plan

## Verbatim (operator, 2026-04-22)

> "So far we have all this and there is no milestone, no EPICS and modules and tasks
> Instead of wasting my time with your broken reason start working on the document so that I can actually try to work on them later with a non broken AI....
>
> YOU NEED TO NOT FUCKING A SINGLE THING I SAID AND WHAT I MADE YOU INGEST... I WANT THE PLAN TO BE THOROUGH... I DONT WANT TO HAVE TO DEAL WITH ANTHROPIC AND CLAUDE AND OPUS IN THE FUTURE......"

> "What about the fucking disk… SSDs in RAID 0, NOT NVMe."
>
> "I will be at 64RAM (1 day) and we can have at least the same amount as swap on my RAID 0 NVME ssds" *(operator has a separate NVMe RAID 0 plan distinct from the 1.9 TB Intel SATA RAID 0 already on the machine)*

> "Lets also start exploring the custom models / custom training I could do such as a model for the information hub / second-brain for example."

> "/loop 15m continue monitoring their progress and their inputs and evolving"

> "This is not negotiable... I want it thorough... I want to work on this later with a non-broken AI."

## Intent

Operator's Claude Code subscription transitions **2026-04-27** (5 days from directive time). The operator is explicitly committing to:

1. **Stay on Claude Code for now** — no hurried harness migration.
2. **Build a harness-neutral stack** — so future harness switches are low-friction.
3. **No dependence on Anthropic / Claude / Opus going forward** — K2.6 and open-weight alternatives become primary.
4. **Thorough planning artifact** — operator will work through the plan with a different AI later; plan must be self-contained, hierarchical (milestone → epics → modules → tasks), and carry all the ingested context so a fresh agent can pick it up cold.

This directive authorizes the creation of:

- Master **milestone** page (target 2026-04-27 and beyond)
- 6 EPICs covering: deadline de-risk, local K2.6 tier, harness neutrality, storage/hardware enablement, routing integration, custom model library
- Module and task pages for the critical-path work (enough to start executing)
- Verbatim directive log (this file)

## Context captured from session (2026-04-22)

### Hardware (factual, corrected)

- **VRAM**: 19 GB (actual, since 2026-04-17 upgrade)
- **RAM**: 32 GB → **64 GB arriving 2026-04-23**
- **Windows Disk 0**: WD_BLACK SN770 931 GB, Gen4 NVMe, single drive. Hosts the WSL dynamic VHDX (`/dev/sdd`, 1 TB capacity, ext4 recoverable). Native bandwidth ~5-7 GB/s when accessed as a block device in WSL.
- **Windows Disk 1**: Intel RAID 0 "Raid0SSDStorage", 1.9 TB — **2× SATA SSDs in RAID 0**, NOT NVMe. Real-world bandwidth ~0.8-1.0 GB/s. **Slower than /dev/sdd.** Not the preferred home for model weights.
- **Windows Disk 2**: Intel RAID 0 "Volume1" 466 GB — Windows OS. Off-limits.
- **Windows Disk 3**: Sabrent 4 TB, USB-attached. Speed depends on USB bus (1-4 GB/s).
- **Windows Disk 4**: Generic PCIE 233 GB — Docker. Off-limits.
- **Operator mentioned separately**: plans for RAID 0 NVMe SSDs distinct from the Intel SATA RAID 0 above. Not currently visible in Get-Disk output. Future hardware addition; not in scope for the immediate 5-day plan.
- `/mnt/d` on Windows side maps via 9P filesystem; caps at 1-2 GB/s regardless of underlying drive. Do not use for hot model weights.

### Model landscape (as of 2026-04-22)

- **Kimi K2.6** (Moonshot AI, released 2026-04-20, modified MIT): 1T total / 32B active MoE, 384 experts, MLA attention, 256K context, native INT4 via QAT, Agent Swarm up to 300 sub-agents × 4,000 steps × 12+h autonomous. **Leads Opus 4.6 and GPT-5.4 on HLE-Full (54.0) and SWE-Bench Pro (58.6)**. OpenRouter pricing: **$0.80 input / $3.50 output per M tokens**. GGUFs on HF: Q2=340 GB, Q4=584 GB, Q8=595 GB.
- **Claude Opus 4.6**: via OpenRouter Bedrock route ≈ $5 in / $25 out per M. K2.6 is **~6-7× cheaper** on operator's workloads (not 20× as initial list-price estimates suggested).
- **GPT-5.4**: ~$15 out per M via OpenRouter. Reachable as specialty fallback for pure-math / unique-capability tasks.
- **gpt-oss 20b / 120b**: Apache 2.0, 21B/3.6B-active and 117B/5.1B-active. Already ingested; 20b fits VRAM natively, 120b is MoE-aware offload candidate.
- **Qwopus 27B (v3 GGUF)**: Opus-distilled, Apache 2.0, Q4 fits 19 GB VRAM.
- **Qwen3-8B**: current local default.
- **AirLLM**: layer-wise inference mechanism for oversized models on NVMe.
- **Unsloth**: LoRA fine-tuning toolchain, 2× faster / 70% less VRAM.

### What was proven today (2026-04-22)

- OpenRouter account live; key at `/home/jfortin/devops-expert-local-ai/.env` (73 chars).
- Wrapper script at `tools/claude_openrouter.sh` — functions: `or-claude`, `or-claude-opus`, `or-claude-gpt`, `or-claude-smoke`, `or-claude-status`, `or-claude-clear`.
- Smoke tests PASSED via curl: K2.6 ($0.00047 per test call), Opus 4.6 ($0.000635), GPT-5.4 ($0.00027). K2.6 thinking blocks preserved. OpenRouter Anthropic Skin confirmed functional.
- Claude Code CLI env-var path verified: `ANTHROPIC_BASE_URL=https://openrouter.ai/api` (no /v1), `ANTHROPIC_AUTH_TOKEN=<key>`, `ANTHROPIC_API_KEY=""` (empty), model ids `moonshotai/kimi-k2.6`, `anthropic/claude-opus-4.6`, `openai/gpt-5.4`.
- Interactive harness test (Claude Code CLI session → OpenRouter → K2.6) pending operator-driven execution in a fresh terminal.

### Strategic north-stars

1. **Harness-neutral consumer contract** — Claude Code, OpenCode, and any future harness are all *consumers* of the wiki + MCP + pipeline; the project never depends on a specific harness.
2. **Vendor-neutral inference routing** — K2.6 via OpenRouter primary; Opus reserved for edge cases; local (K2.6 Q2, gpt-oss family, Qwen3) for $0 and privacy.
3. **Consumer-property doctrine respected** — execution mode / SDLC profile / harness are consumer-declared, not project-declared.
4. **Declarations aspirational until verified** — benchmark leadership claims and capability predictions flagged until validated on operator's actual workloads.

## Follow-up actions (authorized by this directive)

1. Master milestone page at `wiki/backlog/milestones/post-anthropic-self-autonomous-stack.md`.
2. Six epic pages at `wiki/backlog/epics/pre-milestone/E007-*.md` through `E012-*.md`.
3. Critical-path module pages for epics in progress or imminent.
4. Initial task pages for Day 1-3 work.
5. Pipeline post validates all new pages (0 validation errors gate).
6. Updates to Model — Local AI / 2026 Consumer-Hardware Stack / Second-Brain Custom Model Strategy already landed pre-directive; those pages will be re-cross-referenced once the milestone+epics exist.
