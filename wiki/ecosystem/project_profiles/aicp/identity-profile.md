---
title: "AICP — Identity Profile"
aliases:
  - "AICP — Identity Profile"
type: reference
domain: cross-domain
status: synthesized
confidence: medium
maturity: growing
created: 2026-04-13
updated: 2026-04-13
sources:
  - id: aicp-concept
    type: wiki
    file: wiki/domains/tools-and-platforms/aicp.md
tags: [ecosystem, project-profile, aicp, identity, goldilocks]
---

# AICP — Identity Profile

## Summary

The second brain's understanding of AICP (AI Control Platform) as an ecosystem member. AICP is a Python backend platform that orchestrates local and cloud AI backends under user control. Its core thesis: "You -> AICP -> (LocalAI | Claude Code) -> Your Project." It provides backend routing with complexity scoring, 78 skills, circuit breaker patterns, guardrails, and 9 operational profiles. The brain's knowledge of AICP is thinner than OpenFleet or OpenArms — much of its internals have not been deeply synthesized beyond its concept page and integration points.

## Identity (Goldilocks — Stable + State Fields Only)

> [!info] AICP Identity Profile
>
> Per [[execution-mode-is-consumer-property-not-project-property|Consumer-Property Doctrine]] (2026-04-15), this table lists only **stable project identity** and **phase/scale state**. Consumer/task properties (execution mode, SDLC profile, methodology model, current stage) are declared by the consumer at connection time, not hard-coded to the project. Defaults are noted below the table.
>
> | Dimension | Layer | Value | Evidence |
> |-----------|-------|-------|----------|
> | **Type** | Stable | product (backend AI platform) | CLI + backend routing + MCP server + guardrails |
> | **Domain** | Stable | backend-ai-platform (Python) | 61 modules, 94 test files, 1,758 tests, 78 skills, 9 profiles, 14 model configs |
> | **Second-brain relationship** | Stable | connected | tools/gateway.py forwarder installed; Tier 4/4 structural compliance (operational tier ~2+) |
> | **Phase** | State | production | Stage 2 routing operational (4-tier router + circuit breakers + DLQ + warmup); Stage 3 hardware unlocked 2026-04-17 (19 GB VRAM dual-GPU: RTX 2080 8GB + RTX 2080 Ti 11GB) |
> | **Scale** | State | medium | 61 modules, 94 test files, 1,758 tests, 78 skills, 9 profiles, 14 model configs |
>
> > [!tip] Consumer/task properties — NOT project-bound
> >
> > | Property | Default (consumer may override) | Rationale |
> > |----------|--------------------------------|-----------|
> > | Execution Mode | solo | Solo is the universal default; harness/fleet would declare at MCP connect |
> > | SDLC Profile | default (Goldilocks) | Production + medium scale ⇒ default per [[sdlc-customization-framework\|SDLC Customization Framework]]; simplified reserved for POC/micro |
> > | Methodology Model | task-dependent | bug-fix, feature-development, research — each task picks its own model |
> > | PM Level / Trust Tier | L1 / operator-supervised (current single-operator workflow) | Changes if AICP is later embedded in a fleet or harness runtime |

## What the Brain Learned FROM AICP

> [!warning] Knowledge Depth Caveat
>
> The second brain's understanding of AICP is based primarily on its concept page, the ecosystem overview, and its integration surface with OpenFleet. Deep internal architecture (routing engine internals, circuit breaker implementation details, skill authoring patterns) has NOT been synthesized from source code. The lessons below are drawn from what the brain observes at the integration boundary.

> [!tip] Key Lessons Contributed
>
> | Lesson | What AICP Proved |
> |--------|-----------------|
> | [[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]] | 78 skills in .claude/skills/ — the largest skill collection in the ecosystem. 18 referenced in fleet's agent-tooling.yaml. |
> | [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] | AICP exposes 11 MCP tools AND a CLI — the routing decision itself is an MCP tool (`route`), proving MCP can wrap complex decisions |
> | [[deterministic-shell-llm-core|Deterministic Shell, LLM Core]] | Router's complexity scoring + circuit breaker + profile thresholds are deterministic; only the final inference call is LLM |

> [!tip] Key Patterns Observed
>
> | Pattern | How AICP Implements It |
> |---------|----------------------|
> | [[gateway-centric-routing|Gateway-Centric Routing]] | Auto mode: score complexity → check circuit breaker → apply profile thresholds → select backend → failover chain |
> | [[deterministic-shell-llm-core|Deterministic Shell, LLM Core]] | Router is pure logic; LLM calls happen after routing decision |

## Artifact Chain (Project-Specific)

The second brain has limited visibility into AICP's artifact chain. Known artifacts:

> [!abstract] AICP Known Artifacts
>
> | Category | Artifacts | Notes |
> |----------|-----------|-------|
> | Skills | 78 in .claude/skills/ | Largest skill library in ecosystem |
> | Profiles | 9 operational presets in YAML | default, fast, offline, thorough, code-review, fleet-light, reliable, dual-gpu, benchmark |
> | MCP tools | 11 registered | chat, vision, transcribe, speak, voice pipeline, route, deep health, profile, kb search, task status, DLQ status |
> | Tests | 1,631 tests | High coverage relative to module count |
> | Guardrails | Path protection + response filtering | Deterministic, not LLM-based |

**Toolchain:** Python, LocalAI (9 models), circuit breaker, YAML profiles, MCP server

The generic Python domain chain at [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]] applies here, though AICP's chain has not been specifically resolved to AICP's own artifact patterns.

## Methodology Adaptations

> [!info] How AICP Customizes the Methodology
>
> | Aspect | Standard (Wiki) | AICP Approach |
> |--------|-----------------|---------------|
> | SDLC profile | Default (5-stage, gated) | Simplified (lighter gates, fewer mandatory artifacts) |
> | Skill authoring | Template-based | 78 skills suggest a mature internal authoring pattern — not yet documented in the second brain |
> | Testing | pipeline post | pytest with 1,631 tests — high coverage culture |
> | Profile system | N/A | 9 profiles controlling backend selection — a methodology-adjacent routing concern |

## Integration with Second Brain

> [!abstract] Adoption Status (updated 2026-04-17)
>
> | Component | Status |
> |-----------|--------|
> | CLAUDE.md as routing table | Adopted; Identity Profile section added 2026-04-17 per doctrine |
> | Three-layer root docs (AGENTS.md + CLAUDE.md + Skills) | Layer 3 adopted (78 skills); Layer 1 AGENTS.md would enable cross-tool portability — candidate upgrade. See [[root-documentation-map\|Root Documentation Map]] |
> | Skills as extension pattern | Adopted (78 skills) |
> | Wiki knowledge base | Consumed (docs/kb/ + gateway forwarder) |
> | Export from second brain | Defined (E002 integration interface) |
> | Feed-back TO second brain | **Active as of 2026-04-17** — 3 contributions filed (Stage-3 hardware unlocked · this identity reconciliation · three-layer autocomplete validation lesson) |
> | Structural compliance | **Tier 4/4** per `gateway compliance` check |
> | Operational compliance | Tier 2+ (honest reporting per [[structural-compliance-is-not-operational-compliance\|Structural Compliance Is Not Operational Compliance]]) |

## 2026-04-17 Update — Stage 5 Trajectory Changed

The 2026-04-17 ingestion wave (AirLLM, gpt-oss, Qwopus v3, Unsloth — synthesized in [[2026-consumer-hardware-ai-stack|2026 Consumer-Hardware AI Stack]]) materially changed AICP's Stage 5 positioning:

> [!info] **AICP Stage Status Before and After 2026-04-17**
>
> | Stage | Goal | Pre-2026-04 | Post-2026-04-17 |
> |-------|------|--------------|-----------------|
> | 1 | LocalAI functional | Complete | Complete |
> | 2 | Route simple ops to LocalAI | Complete | Complete |
> | 3 | Progressive offload | **Hardware-blocked on 19 GB VRAM** | **Unblocked** — 19 GB actual + [[src-gpt-oss-openai-open-weight-moe\|gpt-oss-20b]] fills the reasoning tier |
> | 4 | Circuit breakers + DLQ | Planned | Planned (unchanged) |
> | 5 | 80%+ Claude reduction | Aspirational, distant | **Integration-blocked, not hardware-blocked** — Q2-Q3 2026 objective |

**Four concrete wiring tasks** unlock Stage 5 (from the [[2026-consumer-hardware-ai-stack|Consumer-Hardware Stack Synthesis]]'s AICP-roadmap section):
1. Wire gpt-oss-20b as local-reasoning tier in the complexity scorer
2. Wire gpt-oss-120b via llama.cpp `-ngl` offload as local-batch-reasoning tier
3. Train a wiki-corpus LoRA (Qwen3.5-4B base via [[src-unsloth-fast-lora-consumer-hardware|Unsloth]]) as methodology-maintenance tier
4. Complete Stage 4 circuit breakers + DLQ (already planned)

None of these require hardware beyond what the operator already has. The work is integration effort, not research-lab budget.

**Candidate epic**: E024 — Local-First Routing Integration (Stage 3-5). Measurable outcome: routing-split metric moves from ~40% local to >80% local. Operator-supervised.

## Knowledge Gaps

> [!warning] What the Brain Does NOT Know About AICP
>
> - Internal architecture of the routing engine (scoring algorithm, threshold tuning)
> - Circuit breaker implementation details (state transitions, recovery timing)
> - Skill authoring lifecycle and quality patterns
> - Guardrails pipeline implementation (how path rules and response filters compose)
> - Dual-machine Alpha/Bravo architecture failure modes
> - Actual token cost reduction measurements at Stage 2
> - **Empirical routing split with 19 GB dual-GPU hardware** (Stage 3 hardware just unlocked 2026-04-17; measurements pending — connects to [[model-local-ai\|Model — Local AI]] "Empirical routing split after Stage 3" open question, now answerable in principle)
>
> These gaps are acknowledged, not hidden. Future ingestion of AICP source code would fill them.

### How This Connects — Navigate From Here

> [!abstract] From This Profile → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Ecosystem overview** | [[four-project-ecosystem|Four-Project Ecosystem]] |
> | **Concept page** | [[aicp|AICP]] |
> | **Generic artifact framework** | [[artifact-chains-by-model|Artifact Chains by Methodology Model]] |
> | **Methodology model** | [[model-methodology|Model — Methodology]] |
> | **Ecosystem model** | [[model-ecosystem|Model — Ecosystem Architecture]] |
> | **Local AI model** | [[model-local-ai|Model — Local AI ($0 Target)]] |

## Relationships

- PART OF: [[four-project-ecosystem|Four-Project Ecosystem]]
- DERIVED FROM: [[aicp|AICP]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[model-ecosystem|Model — Ecosystem Architecture]]
- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]]
- FEEDS INTO: [[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]]
- FEEDS INTO: [[gateway-centric-routing|Gateway-Centric Routing]]

## Backlinks

[[four-project-ecosystem|Four-Project Ecosystem]]
[[aicp|AICP]]
[[model-methodology|Model — Methodology]]
[[model-ecosystem|Model — Ecosystem Architecture]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[skills-architecture-is-dominant-extension-pattern|Skills Architecture Is the Dominant LLM Extension Pattern]]
[[gateway-centric-routing|Gateway-Centric Routing]]
