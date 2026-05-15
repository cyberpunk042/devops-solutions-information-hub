---
title: "E024-M006 — Cross-Project Profile Catalog (the 'everywhere' integration: one Profile per sister project + catalog page enabling operator navigation across the 7-project ecosystem)"
type: module
domain: backlog
status: draft
priority: P2
task_type: module
current_stage: document
readiness: 25
progress: 0
stages_completed: []
artifacts: []
epic: "E024"
depends_on:
  - E024-M002                            # need Profile schema
  - E024-M003                            # need /opt canonical example to mirror
confidence: high
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: parent-epic
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn.md
    description: "Parent Epic E024 — the 'everywhere' requirement from operator directive 2026-05-09 turn 3"
  - id: operator-directive-2026-05-09-turn-3
    type: directive
    file: raw/notes/2026-05-09-operator-directive-sdd-skills-context-hooks-harness-overlap-need-clear-view-and-vision-integrate-everywhere-wiki-llm-pm-claude-os-multica-openclaw-claude-code-opencode.md
    description: "Operator: 'Both need to be possible to use / integrate properly everywhere, Wiki LLM, PM management tools, etc.... Through whatever tool'"
  - id: spectrum
    type: wiki
    file: wiki/domains/ai-agents/declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools.md
    description: "Spectrum's tool-agnostic abstraction makes per-project Profile portable across all 7 sister projects + tool variations"
  - id: sister-projects-config
    type: file
    file: wiki/config/sister-projects.yaml
    description: "Operator-confirmed sister-projects registry — 6 projects (openarms, openfleet, aicp, devops-control-plane, openclaw, root-ghostproxy); Hermes operator-confirmed 2026-05-09 (may or may not be in this file yet)"
tags: [module, "E024-M006", cross-project, profile-catalog, sister-projects, everywhere-integration, navigation, openarms, openfleet, aicp, devops-control-plane, openclaw, root-ghostproxy, hermes, "2026-05-09", "draft"]
---

# E024-M006 — Cross-Project Profile Catalog

## Summary

Author one Per-Project Assistant Profile per sister project (OpenArms · OpenFleet · AICP · devops-control-plane · OpenClaw · root-ghostproxy · Hermes-the-project-if-it-exists) plus a catalog page enabling operator-level navigation across the entire ecosystem. Operator-stated 2026-05-09 turn 3: *"Both need to be possible to use / integrate properly everywhere, Wiki LLM, PM management tools, etc.... Through whatever tool Claude OS, Multica, OpenClaw, Claude Code, OpenCode..."* — this is the "everywhere" requirement. The /opt canonical Profile (M003) provides the structural reference; this module replicates that structure tailored to each project's needs. The catalog page is the navigation hub: operator opens it, sees all 7 profiles + their target runtimes + their value-output telemetry at a glance.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T084 | Author OpenArms Profile (fleet-agent runtime engineering, harness compliance, methodology enforcement) | 25% | 0% | draft |
| T085 | Author OpenFleet Profile (fleet orchestration, LightRAG consumption, task dispatch) | 25% | 0% | draft |
| T086 | Author AICP Profile (local-AI inference, complexity routing, $0 target enforcement) | 25% | 0% | draft |
| T087 | Author devops-control-plane Profile (infrastructure governance, decision tracking) | 25% | 0% | draft |
| T088 | Author OpenClaw Profile (autonomous agentic workflows runtime) | 25% | 0% | draft |
| T089 | Author root-ghostproxy Profile (OS-root harness propagation, IPS modules, global config) | 25% | 0% | draft |
| T090 | Author Hermes-the-project Profile (TBD — depends on whether Hermes-the-project exists separately from Hermes-the-CLI) | 15% | 0% | draft |
| T091 | Author the Cross-Project Profile Catalog page (the navigation hub) | 20% | 0% | draft |

## Dependencies

- [[e024-m002-per-project-assistant-profile-pattern-and-schema|E024-M002]] — Profile schema must be locked
- [[e024-m003-opt-second-brain-assistant-profile-canonical-example|E024-M003]] — /opt canonical example provides the template all 7 mirror

## Done When

- [ ] All 8 child tasks at status: done
- [ ] 7 Profile artifacts at `wiki/concepts/sister-project-profiles/<project>-assistant-profile.md` (or per-repo `.assistant/profile.yaml`)
- [ ] Catalog page at `wiki/concepts/sister-project-profiles/_index.md` (or similar) lists all 7 with runtime targets + value-output expectations
- [ ] Each Profile validates against the schema (T071 output)
- [ ] Each Profile maps the project's actual needs (not template-clone)
- [ ] Operator confirms 7-project coverage reflects intent
- [ ] `.venv/bin/python -m tools.pipeline post` returns 0 errors

## Impediments

- D1 (Hermes identity) was resolved — Hermes is real (per Multica's daemon CLI list). But: does Hermes-the-CLI come with its own SISTER PROJECT (repo), or is it just a CLI we target? T090 depends on this distinction.
- The 7-project list assumes Hermes-the-project exists. If it doesn't, T090 becomes "skip" rather than "author".

## The "Everywhere" Requirement (operator-stated)

Per [[2026-05-09-operator-directive-sdd-skills-context-hooks-harness-overlap-need-clear-view-and-vision-integrate-everywhere-wiki-llm-pm-claude-os-multica-openclaw-claude-code-opencode|operator directive turn 3]]: *"Both need to be possible to use / integrate properly everywhere, Wiki LLM, PM management tools, etc.... Through whatever tool"*.

Realized in this module by:

- **One Profile per project** = "everywhere" at the project axis
- **Multiple runtime targets per Profile** (Claude Code · Multica · OpenClaw · Hermes-CLI · OpenCode · Claude OS) = "everywhere" at the tool axis
- **Catalog page** = navigation primitive across both axes
- **Multica integration** (per [[spawn-protocol-multica-the-runtime-agnostic-bridge-from-per-project-profile-to-multicas-10-cli-daemon|spawn-protocol-multica]]) = "everywhere" via the meta-harness (10+ CLIs)
- **Destination integration** (Wiki LLM + PM tools per the spectrum's destination table) = "everywhere" at the consumption axis

## The Per-Project Profile Sketches

Per [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]] Sister-Project Applicability section:

| Project | Profile name | Primary focus |
|---|---|---|
| **/opt second-brain** (anchor — M003) | `opt-second-brain-assistant` | Knowledge curation, methodology stewardship, source ingestion, lesson distillation |
| **OpenArms** | `openarms-assistant` | Fleet-agent runtime engineering, harness compliance, methodology enforcement |
| **OpenFleet** | `openfleet-assistant` | Fleet orchestration, LightRAG knowledge consumption, task dispatch |
| **AICP** | `aicp-assistant` | Local-AI inference, complexity routing, $0 target enforcement |
| **devops-control-plane** | `dcp-assistant` | Infrastructure governance, decision tracking |
| **OpenClaw** | `openclaw-assistant` | Autonomous agentic workflows runtime |
| **root-ghostproxy** | `root-ghostproxy-assistant` | OS-root harness propagation, IPS modules, global config |
| **Hermes-the-project** (TBD) | `hermes-assistant` (if project exists) | TBD |

## Relationships

- PART OF: [[e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn|E024 — Per-Project Assistant Configurations]]
- DEPENDS ON: [[e024-m002-per-project-assistant-profile-pattern-and-schema|E024-M002 — Profile Schema]]
- DEPENDS ON: [[e024-m003-opt-second-brain-assistant-profile-canonical-example|E024-M003 — /opt canonical example]]
- BUILDS ON: [[declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools|Concept — Declarative Agent Programming Spectrum]] — provides the tool-agnostic abstraction enabling cross-project portability
- IMPLEMENTS: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]] across the 7-project ecosystem
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Lesson — Anti-Vendor-Lock-In]] — Profiles preserve runtime-agnosticism across all 7 projects

## Backlinks

[[E024 — Per-Project Assistant Configurations]]
[[E024-M002 — Profile Schema]]
[[E024-M003 — /opt canonical example]]
[[Concept — Declarative Agent Programming Spectrum]]
[[Pattern — Per-Project Assistant Profile]]
[[Lesson — Anti-Vendor-Lock-In]]
