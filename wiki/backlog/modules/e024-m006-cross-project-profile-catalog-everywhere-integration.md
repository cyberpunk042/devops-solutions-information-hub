---
title: "E024-M006 — this-project Meta-Layer for Per-Project Profiles (standards · model · integration · super-model) — the unique this project contribution; sister projects author their OWN Profiles consuming this meta-layer"
type: module
domain: backlog
status: draft
priority: P1
task_type: module
current_stage: document
readiness: 30
progress: 0
stages_completed: []
artifacts:
  - wiki/spine/standards/per-project-assistant-profile-standards.md
epic: "E024"
depends_on: []
confidence: high
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: parent-epic
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn.md
    description: "Parent Epic E024"
  - id: operator-correction-2026-05-09-turn-5
    type: directive
    file: raw/notes/2026-05-09-operator-correction-turn-5-every-project-does-own-profile-opt-difference-is-standards-model-integration-super-models-do-not-lose-yourself.md
    description: "Operator clarification 2026-05-09 turn 5 (sacrosanct, verbatim): 'every project will do their own Profiles... this is per project.. the difference in the second-brain is that we do not only have profiles for AI assistants but we will also have the standards and the model and integration into the knowledge and super-models'. This module was originally wrongly scoped as 'this project authors sister profiles' — refactored 2026-05-09 to its correct scope: this project's unique meta-layer contribution."
  - id: profile-standards-artifact
    type: wiki
    file: wiki/spine/standards/per-project-assistant-profile-standards.md
    description: "First deliverable of this module — Profile Standards (the what-good-looks-like spec sister projects consume)"
tags: [module, "E024-M006", per-project-assistant-meta-layer, profile-standards, profile-model, profile-integration, profile-super-model, "2026-05-09", "refactored-from-cross-project-catalog", "draft"]
---

# E024-M006 — this-project Meta-Layer for Per-Project Profiles

> [!warning] **2026-05-09 refactor**: This module was originally scoped as "this project authors sister-project Profile catalog" — operator correction 2026-05-09 turn 5 (sacrosanct): *"every project will do their own Profiles... this is per project"*. this project does NOT author sister-project Profiles; that's each project's own work. this project uniquely contributes the **meta-layer** (standards · model · integration · super-model). This module is now scoped correctly.

## Summary

Author this project's (the research wiki) **unique meta-layer contribution** to the Per-Project Assistant Profile ecosystem — the **standards**, **model**, **integration into the knowledge**, and **super-model update** that ALL sister projects consume to author their own Profiles. Each project (OpenArms · OpenFleet · AICP · devops-control-plane · OpenClaw · root-ghostproxy · others) authors its OWN Profile in its OWN repo using these this-project artifacts. this project does NOT author sister-project Profiles — that would be a cross-project boundary violation. this project authors:
1. **Profile Standards** — what good Profile looks like; quality gates (✅ done)
2. **Profile Model** — the named model in the 16-model spine registry (pending operator-approval for promotion)
3. **Profile-Knowledge Integration** — how Profile integrates with existing wiki layers (lessons, patterns, decisions, super-model)
4. **Super-Model Update** — add Profile to the spine super-model

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T084 | Author Per-Project Assistant Profile Standards (`wiki/spine/standards/`) | 100% | 100% | ✅ done |
| T085 | Author Per-Project Assistant Profile Model (`wiki/spine/models/agent-config/`) | 30% | 0% | draft |
| T086 | Author Profile-Knowledge Integration concept (cross-reference topology with existing wiki) | 25% | 0% | draft |
| T087 | Update Spine Super-Model to include Profile as foundational | 20% | 0% | draft |
| T088 | (optional) Author Per-Project Assistant Profile Template at `wiki/config/templates/` for sister-project scaffolding | 15% | 0% | draft |
| T089 | (optional) Extend `wiki/config/wiki-schema.yaml` + `wiki/config/artifact-types.yaml` to codify `assistant-profile` as a recognized page type (operator-approval) | 10% | 0% | draft |

## Dependencies

- [[e024-m002-per-project-assistant-profile-pattern-and-schema|E024-M002]] — Profile pattern (the design these meta-layer artifacts standardize)
- [[e024-m003-assistant-profile-canonical-example|E024-M003]] — this project's own Profile (the exemplar applying the standards)

## Done When

- [ ] Profile Standards page exists at `wiki/spine/standards/` ✅ done
- [ ] Profile Model page exists at `wiki/spine/models/agent-config/`
- [ ] Profile-Knowledge Integration concept exists (cross-reference topology documented)
- [ ] Spine Super-Model updated to include Profile (operator-approval — touches a spine-canonical artifact)
- [ ] Optional Profile Template at `wiki/config/templates/` for sister-project scaffolding (operator-decision)
- [ ] Optional schema codification of `assistant-profile` page type (operator-approval)
- [ ] Operator confirms this project's meta-layer scope is complete and ready for sister-project consumption

## Out of Scope (explicit boundary)

- [ ] **Authoring sister-project Profiles at this project** — operator-corrected 2026-05-09: each project authors its OWN Profile. this project does not. Cross-project boundary holds.
- [ ] **Maintaining sister-project Profiles** — same. Sister projects own their own Profile lifecycle.
- [ ] **Auditing sister-project Profile content** — operator-territory, not this-project content scope.

## Relationships

- PART OF: [[e024-per-project-assistant-configurations-to-capture-programmatic-credit-and-enable-ecosystem-spawn|E024 — Per-Project Assistant Configurations]]
- DEPENDS ON: [[e024-m002-per-project-assistant-profile-pattern-and-schema|E024-M002]] (the Profile pattern this standards-layer governs)
- DEPENDS ON: [[e024-m003-assistant-profile-canonical-example|E024-M003]] (this project's canonical Profile = exemplar)
- DELIVERS: [[per-project-assistant-profile-standards|Per-Project Assistant Profile Standards]] (this module's first deliverable)
- DEMONSTRATES: [[the-agent-must-practice-what-it-documents|Lesson — The agent must practice what it documents]] — this project provides the meta-layer + uses it for this project's own Profile

## Backlinks

[[E024 — Per-Project Assistant Configurations]]
[[E024-M002]]
[[E024-M003]]
[[per-project-assistant-profile-standards|Per-Project Assistant Profile Standards]]
[[Lesson — The agent must practice what it documents]]
