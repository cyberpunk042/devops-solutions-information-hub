---
title: "Local Inference Engine (Subsystem 3)"
type: epic
domain: backlog
status: draft
priority: P1
task_type: epic
current_stage: document
readiness: 10
stages_completed: [document]
artifacts:
  - wiki/domains/tools-and-platforms/aicp.md
  - wiki/domains/ai-models/local-llm-quantization.md
  - wiki/decisions/local-model-vs-cloud-api-for-routine-operations.md
  - docs/superpowers/specs/2026-04-08-knowledge-evolution-pipeline-design.md
confidence: high
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [local-inference, aicp, localai, subsystem-3, zero-cost, evolution]
---

# Local Inference Engine (Subsystem 3)

## Summary

Full AICP integration for the wiki evolution pipeline. Route evolution tasks through AICP's complexity scoring — simple tasks (scaffold, lint, manifest) to local models ($0), complex tasks (synthesis, cross-referencing, lesson generation) to Claude. Blocked on hardware upgrade (8GB → 19GB VRAM).

## Goals

- Wire `pipeline evolve --auto --backend openai` to LocalAI via AICP routing
- Test local model quality on evolution tasks (scaffold, summarize, cross-reference)
- Establish quality thresholds — which tasks can go local, which must stay cloud
- Achieve $0 cost for routine operations (manifest, lint, scaffold, simple evolution)
- Document findings as wiki pages (model comparison, quality benchmarks)

## Done When

- [ ] `pipeline evolve --auto --backend openai --top 1` generates a page via local model
- [ ] Generated page passes validation with 0 errors
- [ ] Quality comparison: local vs Claude on same candidate (documented as wiki page)
- [ ] AICP routing profile configured for wiki operations
- [ ] At least 3 evolution tasks completed via local model
- [ ] Cost savings documented (tokens saved, $ avoided)

## Blocked

Waiting for 19GB VRAM hardware upgrade. Current 8GB limits model size to 8B parameters.

## Relationships

- IMPLEMENTS: Decision: Local Model vs Cloud API for Routine Operations
- BUILDS ON: AICP (backend routing, circuit breaker)
- ENABLES: Knowledge Evolution Pipeline ($0 evolution)
- RELATES TO: Local LLM Quantization

## Backlinks

[[Decision: Local Model vs Cloud API for Routine Operations]]
[[AICP (backend routing, circuit breaker)]]
[[Knowledge Evolution Pipeline ($0 evolution)]]
[[Local LLM Quantization]]
