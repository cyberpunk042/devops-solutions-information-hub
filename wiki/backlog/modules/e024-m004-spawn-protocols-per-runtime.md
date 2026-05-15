---
title: "E024-M004 — Spawn Protocols per Runtime (the bridge layer: Profile → running Assistant on Multica / OpenClaw / Hermes / Claude Code CLI / generic Agent SDK)"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: document
readiness: 35
progress: 0
stages_completed: []
artifacts:
  - wiki/patterns/01_drafts/spawn-protocol-multica-the-runtime-agnostic-bridge-from-per-project-profile-to-multicas-10-cli-daemon.md
epic: "E024"
depends_on:
  - E024-M002                            # need Profile schema before spawn protocols can map sections to runtime primitives
confidence: high
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: parent-epic
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn.md
    description: "Parent Epic E024"
  - id: spectrum-foundation
    type: wiki
    file: wiki/domains/ai-agents/declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools.md
    description: "The L5 row of the integration matrix names the runtimes this module produces spawn protocols for"
  - id: frontier-comparison
    type: wiki
    file: wiki/comparisons/assistant-platforms-and-frameworks-frontier-comparison-claude-os-obsidian-pm-multica-openclaw-command-center-2026-05-09.md
    description: "Frontier comparison identifying Multica as T3 frontier + operator-adopted; informs spawn priority"
  - id: spawn-protocol-multica
    type: wiki
    file: wiki/patterns/01_drafts/spawn-protocol-multica-the-runtime-agnostic-bridge-from-per-project-profile-to-multicas-10-cli-daemon.md
    description: "First concrete spawn protocol (already authored 2026-05-09) — Multica is operator-adopted runtime"
tags: [module, "E024-M004", spawn-protocols, runtime-bridge, multica, openclaw, hermes, claude-code-cli-p, generic-agent-sdk, "2026-05-09", "draft"]
---

# E024-M004 — Spawn Protocols per Runtime

## Summary

The bridge layer of E024: authors one **spawn protocol** per runtime that the Per-Project Assistant Profile can target. Each protocol is a deterministic mapping: read Profile YAML → render runtime-specific primitives → register the running Assistant → verify behavior matches the Profile. Multica is the priority because operator already adopted it self-hosted (`/home/jfortin/.multica/server/`); spawn-protocol-multica is already authored (2026-05-09). The remaining protocols (OpenClaw, Hermes, Claude Code `-p` CLI, generic Agent SDK) follow. Cross-cutting deliverable: each protocol document references the **declarative agent programming spectrum** to clarify which spectrum layer (L5 Harness) it compiles the Profile into.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T078 | Author spawn-protocol-generic-agent-sdk | 25% | 0% | draft |
| T079 | Author spawn-protocol-openclaw | 25% | 0% | draft |
| T080 | Author spawn-protocol-claude-code-cli-p (the `claude -p` direct-CLI path) | 30% | 0% | draft |
| T081 | Author spawn-protocol-hermes (depends on Hermes CLI investigation D7) | 20% | 0% | draft |
| T082 | Promote spawn-protocol-multica `01_drafts` → `02_synthesized` after operator review | 50% | 0% | draft |
| T083 | Author spawn-protocols-comparison page (which protocol when?) | 20% | 0% | draft |

## Dependencies

- [[e024-m002-per-project-assistant-profile-pattern-and-schema|E024-M002]] — Profile schema must be locked before spawn protocols can map sections precisely
- D7 (Hermes CLI investigation) — blocks T081 specifically; other protocols not blocked

## Done When

- [ ] All 6 child tasks at status: done (per task gates)
- [ ] At least 3 spawn protocol patterns exist in `wiki/patterns/01_drafts/` (Multica done; generic + at-least-one-direct-CLI)
- [ ] Each protocol explicitly maps the 6 Profile sections (Identity, Knowledge Scope, Action Surface, Model Routing, Prompt Templates, Success Criteria) to the runtime's primitives
- [ ] Each protocol includes a smoke-test sequence verifying spawn → behavior matches Profile
- [ ] Spawn-protocols-comparison page (T083) provides the decision heuristic: which protocol when
- [ ] `.venv/bin/python -m tools.pipeline post` returns 0 errors

## Impediments

- D7 (Hermes CLI investigation) blocks T081 — would need to either WebFetch Hermes docs or defer T081 until operator surfaces Hermes information

## The Multica-First Sequencing

Per the [[assistant-platforms-and-frameworks-frontier-comparison-claude-os-obsidian-pm-multica-openclaw-command-center-2026-05-09|frontier comparison]] + the [[declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools|spectrum]]:

- **Multica is a meta-harness** — its daemon auto-detects Claude Code · Codex · OpenClaw · OpenCode · Hermes · Gemini · Pi · Cursor Agent · Kimi · Kiro CLI
- **Implication**: spawn-protocol-multica is the single highest-leverage protocol — covers 10+ CLIs via one bridge
- **Direct-CLI protocols** (openclaw, claude-code-cli-p, hermes) are needed ONLY for use cases that bypass Multica (e.g., one-shot scripts, low-overhead automations)

This shapes priority: Multica first (done) · generic + claude-code-cli-p second (covers `claude -p` programmatic credit consumption) · OpenClaw + Hermes third (only if direct-CLI use case surfaces).

## Relationships

- PART OF: [[e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn|E024 — Per-Project Assistant Configurations]]
- DEPENDS ON: [[e024-m002-per-project-assistant-profile-pattern-and-schema|E024-M002 — Profile Pattern + Schema]]
- BUILDS ON: [[declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools|Concept — Declarative Agent Programming Spectrum]] — L5 Harness row
- IMPLEMENTS: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]] for multiple concrete runtimes
- ENABLES: [[e024-m003-assistant-profile-canonical-example|E024-M003 this project Profile]] to actually spawn an Assistant instance
- DELIVERS: [[spawn-protocol-multica-the-runtime-agnostic-bridge-from-per-project-profile-to-multicas-10-cli-daemon|Pattern — spawn-protocol-multica]] (already authored)

## Backlinks

[[E024 — Per-Project Assistant Configurations]]
[[E024-M002 — Profile Pattern + Schema]]
[[Concept — Declarative Agent Programming Spectrum]]
[[Pattern — Per-Project Assistant Profile]]
[[E024-M003 this project Profile]]
[[Pattern — spawn-protocol-multica]]
