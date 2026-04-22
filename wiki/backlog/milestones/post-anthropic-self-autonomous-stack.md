---
title: "Milestone: Post-Anthropic Self-Autonomous AI Stack"
type: milestone
domain: backlog
status: draft
priority: P0
target_date: 2026-04-27
readiness: 15
progress: 10
epics:
  - "E007"
  - "E008"
  - "E009"
  - "E010"
  - "E011"
  - "E012"
acceptance_criteria:
  - "Claude Code CLI can route through OpenRouter to Kimi K2.6 end-to-end (harness + tool-use)"
  - "Local K2.6 Q2 runs via KTransformers on /dev/sdd (WD_BLACK NVMe) with measured tok/s documented"
  - "OpenCode installed as a second consumer harness against the same wiki/MCP/pipeline stack"
  - "AICP complexity scorer routes K2.6-via-OpenRouter as primary for agentic/coding workloads"
  - "Harness Contract document published at wiki/spine/standards/ — captures invariants any harness must provide"
  - "64 GB RAM installed; /dev/sdd mounted at /mnt/models; disk-speed baselines measured"
  - "Cost tracking shows sustained ~6-7\u00d7 reduction vs Anthropic-direct Opus on the same workloads"
  - "Operator confirms: the 2026-04-27 subscription transition was a non-event"
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: operator-directive
    type: file
    file: raw/notes/2026-04-22-directive-post-anthropic-self-autonomous-plan.md
  - id: src-kimi-k2-6-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-kimi-k2-6-moonshot-agent-swarm.md
    title: "Synthesis — Kimi K2.6"
  - id: 2026-consumer-hardware-stack
    type: wiki
    file: wiki/spine/references/2026-consumer-hardware-ai-stack.md
    title: "The 2026 Consumer-Hardware AI Stack"
  - id: model-local-ai
    type: wiki
    file: wiki/spine/models/depth/model-local-ai.md
    title: "Model — Local AI ($0 Target)"
  - id: second-brain-custom-model-strategy
    type: wiki
    file: wiki/spine/references/second-brain-custom-model-strategy.md
    title: "Second-Brain Custom Model Strategy"
tags: [milestone, self-autonomous, post-anthropic, kimi-k2-6, openrouter, harness-neutral, 5-day-plan, p0]
---

# Milestone: Post-Anthropic Self-Autonomous AI Stack

## Summary

On 2026-04-~19 Anthropic shifted Claude Code behind a $140/month subscription tier that expires for the operator on **2026-04-27** (5 days from directive). This milestone transforms that deadline from a blocker into a **non-event** by building a harness-neutral, vendor-neutral inference stack anchored on **Kimi K2.6** (Moonshot AI, released 2026-04-20 — MIT-licensed, 1T/32B-active MoE, leads Opus 4.6 and GPT-5.4 on agentic + real-world coding benchmarks, ~6-7× cheaper via OpenRouter). The milestone coordinates six epics that together deliver: a cloud-side route to K2.6 usable from Claude Code CLI today, a local-side K2.6 tier for offline / privacy / $0 workloads, harness neutrality so any future harness (OpenCode, whatever comes next) plugs in without rewriting the project, hardware enablement for the 64 GB RAM + NVMe storage that makes all of it performant, AICP routing integration that treats all tiers as peers, and a custom-model library (via Unsloth LoRAs) that specializes small models to the wiki's domain. After this milestone the project **never again depends on Anthropic, Claude, or Opus** for its critical path.

## Operator Directive

> "I WANT THE PLAN TO BE THOROUGH... I DONT WANT TO HAVE TO DEAL WITH ANTHROPIC AND CLAUDE AND OPUS IN THE FUTURE......"

> "So far we have all this and there is no milestone, no EPICS and modules and tasks. Instead of wasting my time with your broken reason start working on the document so that I can actually try to work on them later with a non broken AI."

> "We will personally stay on Claude Code for now but evolve our reasoning to be compatible with OpenCode or other real community service that wont lower quality or service with time."

> "Every .agents or .gemini or .claude can be treated as equivalent to us. Every ecosystem needs one and to us it's the same thing. We don't need to lower ourselves to lower standards — even if we need to inject our sauce to elevate it we will."

> "In 5 days everything will most likely be happening on this computer with the 19GB VRAM and the 1TB NVME SSD for AirLLM and so on... we will make this workstation self-autonomous and also integrate the OpenRouter like the rest."

See the verbatim directive log at `raw/notes/2026-04-22-directive-post-anthropic-self-autonomous-plan.md` for full context including hardware corrections and model landscape.

## Delivery Target

> [!info] Milestone Parameters
>
> | Parameter | Value |
> |-----------|-------|
> | **Target date (critical path)** | **2026-04-27** — Claude Code subscription transition day |
> | **Target date (full completion)** | 2026-05-10 (2 weeks after critical-path) |
> | **Phase** | Production (operator's daily workstation) |
> | **Chain** | Default (stage-gated with selected artifacts) |
> | **Total epics** | 6 (E007 through E012) |
> | **Estimated total modules** | ~24 |
> | **Estimated total tasks** | ~60-80 |
> | **Budget** | $20 initial OpenRouter credit + existing hardware (no new purchases required on critical path) |

## Epic Composition

| Epic | Contributes | Current Readiness | Status |
|------|------------|-------------------|--------|
| [[E007-openrouter-deadline-de-risk]] | Cloud route to K2.6 — Claude Code CLI → OpenRouter → K2.6 — proven by 2026-04-27 | 45% | in-progress |
| [[E008-local-k2-6-offline-frontier-tier]] | Offline tier — K2.6 Q2 on /dev/sdd via KTransformers at measured tok/s | 20% | draft |
| [[E009-harness-neutrality-and-openCode-parity]] | Second consumer harness — OpenCode reaches parity on top skills + MCP + pipeline | 15% | draft |
| [[E010-storage-and-hardware-enablement]] | 64 GB RAM installed, /dev/sdd ext4 mounted, storage tiering documented | 10% | draft |
| [[E011-routing-integration-aicp-tiers]] | AICP complexity scorer routes across K2.6 online, K2.6 local, local small models, Opus edge-case | 10% | draft |
| [[E012-custom-model-library-unsloth-loras]] | Wiki-Assistant + Wiki-Router + Multi-LoRA adapter library on a small base | 5% | draft |

## Acceptance Criteria

- [ ] **Claude Code CLI → OpenRouter → Kimi K2.6 end-to-end working** — both smoke test (HTTP, DONE 2026-04-22) and interactive harness test (operator-run in fresh terminal, tool-use + multi-step + scaffold proven)
- [ ] **Local K2.6 Q2 runs on /dev/sdd via KTransformers** — cold-start documented, sustained tok/s measured and recorded in wiki log
- [ ] **OpenCode installed, configured, and producing equivalent output** on at least 3 of operator's top skills compared to Claude Code
- [ ] **MCP servers work under both harnesses** — research-wiki + claude-mem + plannotator validated end-to-end
- [ ] **64 GB RAM installed and detected** (`free -g` shows ~62 GiB)
- [ ] **/dev/sdd mounted at /mnt/models** with ext4, persistent via /etc/fstab; K2.6 Q2 GGUF stored there
- [ ] **AICP complexity scorer includes K2.6-OpenRouter as primary routing tier** for agentic/coding work (config committed, routing-split metric measured)
- [ ] **Harness Contract document authored** at `wiki/spine/standards/harness-contract.md` — lists the invariants any harness must provide
- [ ] **Post-deadline retrospective log** entry in `wiki/log/` dated 2026-04-28 confirming the transition happened without capability loss
- [ ] **All 6 epics at status: done (or deferred with justification)**; operator confirms quality
- [ ] **Pipeline post returns 0 validation errors** after all epic work commits
- [ ] **Cost baseline documented** — 1-week post-deadline spend captured vs projected Opus-direct spend; ratio ~6-7× verified or corrected

## Dependencies

- **Hardware arrival (2026-04-23)**: 64 GB RAM dependency for E008 local K2.6 (Q2 mmap cache benefits from extra RAM); E011 AICP routing also benefits. If delayed, E008 slips but E007 critical-path deadline still met via OpenRouter.
- **OpenRouter service availability**: E007 critical path depends on OpenRouter's Anthropic Skin remaining functional and K2.6 remaining listed. Mitigation: provider pinning + direct Moonshot API documented as fallback in E007.
- **Claude Code 2.1.94 CLI env-var honoring**: If a CLI update breaks the env-var override path, fall back to `claude-code-router` proxy (musistudio/claude-code-router) or migrate to OpenCode earlier (accelerates E009).
- **Kimi K2.6 availability on OpenRouter**: Alternative OpenRouter model ids (`moonshotai/kimi-k2.5`, `moonshotai/kimi-k2-thinking`, `moonshotai/kimi-k2-0711`) remain available as fallbacks if K2.6 becomes unavailable.

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| Interactive harness test (Tests 1-4) pending operator execution | clarification | 2026-04-22 | no | Operator to run `or-claude` in fresh terminal; report back |
| 64 GB RAM not yet installed | environment | 2026-04-22 | no | Arrives 2026-04-23 per operator |
| /dev/sdd mount requires sudo | environment | 2026-04-22 | no | Mount procedure staged; operator executes when ready |
| K2.6 quality parity vs Opus on operator's actual workloads | quality | 2026-04-22 | no | Resolved via A/B run inside E007 M007.3 |

## Post-Milestone Trajectory (Week 2+)

This milestone delivers the *deadline-absorbed* state. The next natural phase targets **full stack evolution** — not critical path for 2026-04-27, but the direction this milestone commits to:

1. **Self-evolving second brain** — K2.6 powers the long-horizon wiki evolution workloads (gap analysis, cross-ref maintenance, lesson synthesis) at ~$0.00X per pass.
2. **Fine-tuned local specialization** — Wiki-Assistant, Wiki-Router, and task-specific LoRAs deployed per AICP tier.
3. **Ecosystem spread** — OpenArms, OpenFleet, devops-control-plane, AICP itself all migrate to the same routing model.
4. **Second-brain as portable artifact** — a fresh workstation (new human, new AI) can clone the wiki, read AGENTS.md, install a harness, and operate. The project *is* the second brain; the harness is replaceable.

## Relationships

- CONTAINS: [[E007-openrouter-deadline-de-risk|E007-openrouter-deadline-de-risk]]
- CONTAINS: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
- CONTAINS: [[E009-harness-neutrality-and-openCode-parity]]
- CONTAINS: [[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
- CONTAINS: [[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
- CONTAINS: [[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
- BUILDS ON: [[src-kimi-k2-6-moonshot-agent-swarm|Synthesis — Kimi K2.6]]
- BUILDS ON: [[2026-consumer-hardware-ai-stack|The 2026 Consumer-Hardware AI Stack]]
- BUILDS ON: [[model-local-ai|Model — Local AI ($0 Target)]]
- BUILDS ON: [[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]]
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]

## Backlinks

[[E007-openrouter-deadline-de-risk|E007-openrouter-deadline-de-risk]]
[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
[[E009-harness-neutrality-and-openCode-parity]]
[[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
[[E011-routing-integration-aicp-tiers|E011-routing-integration-aicp-tiers]]
[[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
[[Synthesis — Kimi K2.6]]
[[The 2026 Consumer-Hardware AI Stack]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]]
[[Principle 4 — Declarations Aspirational Until Verified]]
[[E007-openrouter-deadline-de-risk|E007 — OpenRouter Deadline De-Risk (Claude Code CLI → K2.6)]]
[[E008-local-k2-6-offline-frontier-tier|E008 — Local K2.6 Offline Frontier Tier (KTransformers on /dev/sdd)]]
[[E009-harness-neutrality-and-opencode-parity|E009 — Harness Neutrality (OpenCode as Second Consumer)]]
[[E010-storage-and-hardware-enablement|E010 — Storage and Hardware Enablement (64 GB RAM + /dev/sdd + tiering)]]
[[E011-routing-integration-aicp-tiers|E011 — Routing Integration (AICP Tiers Updated for K2.6 + Local Stack)]]
[[E012-custom-model-library-unsloth-loras|E012 — Custom Model Library (Unsloth LoRAs on Wiki Corpus)]]
