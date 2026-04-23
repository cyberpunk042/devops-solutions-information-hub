---
title: "Three-layer autocomplete chain validated in production fleet operation"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: medium
maturity: growing
derived_from:
  - "Model — Context Engineering"
  - "Context Engineering Standards — What Good Structured Context Looks Like"
created: 2026-04-17
updated: 2026-04-22
sources: []
tags: [contributed, inbox]
contributed_by: "aicp-self"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: 2026-04-17
contribution_status: accepted
review_note: \"Accepted 2026-04-22 during pickup-cold session — structural review (derived_from wired, claim coherent, evidence sourced). Promoted to contributor's tier ceiling (01_drafts) per contribution-policy.yaml harness-trusted tier.\"
contribution_reason: "Context Engineering Standards has Standards-level open question on autocomplete chain — AICP/openfleet has shipping implementation with empirical evidence"
---

# Three-layer autocomplete chain validated in production fleet operation

## Summary

Context Engineering Standards' 8-step autocomplete chain maps cleanly to a three-layer runtime composition deployed in production: static map (intent-map.yaml + injection-profiles.yaml + cross-references.yaml) + knowledge graph (LightRAG, zero-LLM queries) + per-agent memory (claude-mem). Static layer is deterministic and fast. Graph layer adds semantic relationships with zero-LLM cost (pre-supply hl_keywords + ll_keywords + only_need_context=true). Memory layer carries cross-session per-agent context. End-to-end tested with 31 tests (22 unit + 9 integration) in fleet/core/navigator.py, 26 intents x 4 depth tiers (opus-1m / sonnet-200k / localai-8k / heartbeat).

EVIDENCE (4 measurement sources):

1. Knowledge graph scale — 2,695 entity labels deployed in LightRAG. 1,545 KB entities + 2,295 KB relationships from 220 KB entries (parsed ## Relationships sections, zero LLM). 1,309 entities + 3,667 relationships from 360 source files (Python modules, YAML configs, markdown docs, agent CLAUDE.md, SKILL.md). Reference: openfleet/fleet/core/kb_sync.py.

2. Zero-LLM query path validated — Navigator pre-extracts keywords, passes hl_keywords + ll_keywords + only_need_context=true to LightRAG /query. Returns raw graph context without any LLM call. Tested with 5 query types (WIDE: 27 entities/20 relationships; PRECISE: function-level lookup; SPECIAL: navigator impact analysis; cross-system; agent needs). All return graph context in milliseconds with zero LLM cost. Satisfies Local AI $0 target for knowledge retrieval.

3. Tier budgets behave as Standards predicts — opus 5-8K chars / sonnet 2-5K / localai 50-500 chars. All under 8000-char gateway limit. Drops at section boundaries (never mid-text). Matches Expert/Capable/Lightweight tier definitions in Standards.

4. Compaction-survival behavior matches Standards — file-based context (intent-map.yaml, injection-profiles.yaml, knowledge-context.md per agent per cycle) survives compaction. Navigator's _refresh_agent_contexts() at orchestrator Step 0 rebuilds full state per cycle, implementing Standards' Step 8 (Post-Compact Rebuild) as continuous refresh rather than one-time hook.

MECHANISM:

Three layers compose by addressing different cost/latency profiles. Static map = deterministic, file-based, milliseconds, free. Graph = semantic, retrievable in milliseconds with keyword pre-extraction, free (no LLM). Memory = stateful, per-agent, queried via HTTP. Each layer fills a gap the others can't: static can't answer 'what entities relate to X', graph can't answer 'what did Alpha learn last session', memory can't answer 'what does the canonical methodology table say'. Standards predicts 8 steps; runtime can do them as 3 layers because layers chain (static → graph → memory in priority order, with budget enforcement at each).

APPLICABILITY:

- Any agent ecosystem with >=5 agents and >=100 knowledge artifacts where context injection is the bottleneck.
- Any project pursuing Local AI $0 target where knowledge retrieval cost dominates LLM cost.
- Any system that needs to scale context depth per agent tier (expert vs lightweight).

WHEN THE PATTERN DOES NOT FIT:

- Solo agent with <50 knowledge artifacts — static layer alone suffices.
- Projects without an orchestrator/harness — per-cycle refresh model assumes runtime that can call navigator at Step 0.
- Single-tier deployments — tier budget machinery has no use if all agents have same context budget.

## Context

> [!warning] When does this lesson apply?
>
> - You are designing or evaluating a context-injection chain for an agent ecosystem
> - [[model-context-engineering-standards|Context Engineering Standards]] defines an 8-step autocomplete chain and you want to know if it implements in production
> - Your fleet has ≥5 agents and ≥100 knowledge artifacts, or you are pursuing the [[model-local-ai|Local AI $0 target]] and knowledge-retrieval cost dominates LLM cost
> - You need to scale context depth per agent tier (expert vs lightweight)

## Insight

> [!tip] The three-layer composition
>
> Standards' 8-step autocomplete chain maps to three runtime layers that each address a different **cost / latency / scope** profile. The layers CHAIN in priority order (static → graph → memory), with budget enforcement at each step.
>
> | Layer | What it is | Cost profile | Scope |
> |-------|------------|--------------|-------|
> | **Static map** | `intent-map.yaml` + `injection-profiles.yaml` + `cross-references.yaml` | Deterministic · milliseconds · $0 | Canonical tables, MUST/MUST NOT lists, declared structure |
> | **Knowledge graph** | LightRAG with pre-supplied `hl_keywords` + `ll_keywords` + `only_need_context=true` | Milliseconds · zero-LLM · $0 | Semantic relationships across the full knowledge corpus |
> | **Per-agent memory** | claude-mem, queried via HTTP | HTTP round-trip · per-agent stateful | Cross-session agent context, "what did I learn last time" |
>
> Each layer fills a gap the others cannot. Static can't answer "what entities relate to X." Graph can't answer "what did Alpha learn last session." Memory can't recall the canonical methodology table. Three layers, three distinct scopes.
>
> Standards predicts 8 steps; runtime does them as 3 layers because layers chain priority-ordered with budget enforcement at each step.

## Evidence

> [!abstract] Four independent measurement sources
>
> | # | Evidence | Measurement |
> |---|----------|-------------|
> | 1 | **Knowledge graph scale** (openfleet/fleet/core/kb_sync.py) | 2,695 entity labels deployed in LightRAG; 1,545 KB entities + 2,295 KB relationships from 220 KB entries (parsed ## Relationships sections, zero LLM); 1,309 entities + 3,667 relationships from 360 source files |
> | 2 | **Zero-LLM query path validated** | Navigator pre-extracts keywords, passes `hl_keywords + ll_keywords + only_need_context=true` to LightRAG /query. Tested with 5 query types (WIDE: 27 entities/20 relationships; PRECISE: function-level lookup; SPECIAL: navigator impact analysis; cross-system; agent needs). All return graph context in milliseconds with zero LLM cost. Satisfies [[model-local-ai\|Local AI]] $0 target for knowledge retrieval. |
> | 3 | **Tier budgets behave as Standards predicts** | Opus 5-8K chars / Sonnet 2-5K / localai 50-500 chars. All under 8000-char gateway limit. Drops at section boundaries (never mid-text). Matches Expert/Capable/Lightweight tier definitions in Standards. |
> | 4 | **Compaction survival matches Standards** | File-based context (`intent-map.yaml`, `injection-profiles.yaml`, `knowledge-context.md` per agent per cycle) survives compaction. Navigator's `_refresh_agent_contexts()` at orchestrator Step 0 rebuilds full state per cycle — implementing Standards' Step 8 (Post-Compact Rebuild) as continuous refresh rather than one-time hook. |
>
> **Test coverage**: 31 tests in `fleet/core/navigator.py` (22 unit + 9 integration) × 26 intents × 4 depth tiers (opus-1m / sonnet-200k / localai-8k / heartbeat).

## Applicability

> [!abstract] Applies when
>
> - Agent ecosystem with ≥5 agents and ≥100 knowledge artifacts where context injection is the bottleneck
> - Project pursuing [[model-local-ai\|Local AI $0 target]] where knowledge-retrieval cost dominates LLM cost
> - System that needs tiered context depth (expert vs lightweight agents)
>
> Does NOT apply when
>
> - Solo agent with <50 knowledge artifacts — static layer alone suffices
> - Projects without an orchestrator/harness — per-cycle refresh assumes runtime that can call navigator at Step 0
> - Single-tier deployments — tier budget machinery has no use if all agents have same budget
>
> Contributed from /home/jfortin/devops-expert-local-ai. Applicability assessed during promotion review.

## Relationships

- RELATES TO: [[model-context-engineering|Model — Context Engineering]]
- RELATES TO: [[model-context-engineering-standards|Context Engineering Standards]]
- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]]
- VALIDATES IN PRODUCTION: [[model-context-engineering-standards|Context Engineering Standards]] 8-step autocomplete chain
- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[model-context-engineering|Model — Context Engineering]]
[[Context Engineering Standards]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[model-registry|Model Registry]]
