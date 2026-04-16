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

## Identity (Goldilocks 7 Dimensions)

> [!info] AICP Goldilocks Profile
>
> | Dimension | Value | Evidence |
> |-----------|-------|---------|
> | **Type** | product (backend platform) | CLI + backend routing + MCP server + guardrails |
> | **Execution Mode** | Solo | Human + Claude in conversation, no harness, no fleet dispatch |
> | **Domain** | Backend AI Platform (Python) | 60 Python modules, 1,631 tests |
> | **Phase** | Production | Stage 1 (LocalAI functional) complete, Stage 2 (routing) implemented |
> | **Scale** | Medium (~60 modules) | Growing, but less documented in the second brain than OpenFleet/OpenArms |
> | **PM Level** | L1 (CLAUDE.md directives) | No harness or orchestrator — skill-based extension |
> | **Trust Tier** | Operator-supervised | Solo execution, human decides |
> | **SDLC Profile** | Simplified | Lighter process — fewer artifacts per stage |

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

> [!abstract] Adoption Status
>
> | Component | Status |
> |-----------|--------|
> | CLAUDE.md as routing table | Adopted |
> | Three-layer root docs (AGENTS.md + CLAUDE.md + Skills) | Not adopted — candidate upgrade. AICP already has Layer 3 (78 skills); Layer 1 AGENTS.md would enable cross-tool portability. See [[root-documentation-map|Root Documentation Map]] |
> | Skills as extension pattern | Adopted (78 skills) |
> | Wiki knowledge base | Partial (consumes wiki exports in docs/kb/) |
> | Export from second brain | Defined (E002 integration interface) |
> | Feed-back TO second brain | Minimal (concept page + integration patterns) |

## Knowledge Gaps

> [!warning] What the Brain Does NOT Know About AICP
>
> - Internal architecture of the routing engine (scoring algorithm, threshold tuning)
> - Circuit breaker implementation details (state transitions, recovery timing)
> - Skill authoring lifecycle and quality patterns
> - Guardrails pipeline implementation (how path rules and response filters compose)
> - Dual-machine Alpha/Bravo architecture failure modes
> - Actual token cost reduction measurements at Stage 2
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
