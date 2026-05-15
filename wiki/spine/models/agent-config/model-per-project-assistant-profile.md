---
title: Model — Per-Project Assistant Profile
aliases:
  - "Model — Per-Project Assistant Profile"
  - "Model: Per-Project Assistant Profile"
  - "Profile Model"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: operator-directive-2026-05-09-turn-1
    type: directive
    file: raw/notes/2026-05-09-operator-directive-per-project-assistant-configs-spawn-openclaw-openarms-hermess-and-anthropic-programmatic-budget-policy-research.md
    title: "2026-05-09 turn 1 directive — repos / projects will have assistants configurations / profiles"
  - id: operator-correction-2026-05-09-turn-4
    type: directive
    file: raw/notes/2026-05-09-operator-correction-multi-decision-do-not-corrupt-redefine-profile-stop-skipping-and-minimizing-research-hermes-and-ocmc-properly.md
    title: "2026-05-09 turn 4 correction — Profile is way more than just setting for one tool; tool-agnosticism constitutive"
  - id: operator-correction-2026-05-09-turn-5
    type: directive
    file: raw/notes/2026-05-09-operator-correction-turn-5-every-project-does-own-profile-opt-difference-is-standards-model-integration-super-models-do-not-lose-yourself.md
    title: "2026-05-09 turn 5 correction — every project does own Profiles; this project has standards + model + integration + super-models"
  - id: operator-correction-2026-05-09-turn-6
    type: directive
    file: raw/notes/2026-05-09-operator-correction-turn-6-profiles-plural-per-project-each-is-one-focused-assistant-job-continuous-research-ingestion-synthesis-stop-conflating.md
    title: "2026-05-09 turn 6 correction — PROFILES plural per project; each = one focused assistant job"
  - id: profile-pattern
    type: wiki
    file: wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md
    title: "Pattern — Per-Project Assistant Profile"
  - id: profile-standards
    type: wiki
    file: wiki/spine/standards/per-project-assistant-profile-standards.md
    title: "Per-Project Assistant Profile Standards"
  - id: profile-continuous-research
    type: wiki
    file: wiki/domains/cross-domain/profile-continuous-research-keep-models-and-tech-vision-current.md
    title: "Profile — this project Continuous Research (canonical example #1)"
  - id: profile-pipeline-synthesis
    type: wiki
    file: wiki/domains/cross-domain/profile-pipeline-synthesis-from-raw-to-wiki-page-still-not-at-end-of-pipeline.md
    title: "Profile — this project Pipeline Synthesis (canonical example #2)"
  - id: spectrum-concept
    type: wiki
    file: wiki/domains/ai-agents/declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools.md
    title: "Concept — Declarative Agent Programming Spectrum (7 layers Profile spans)"
  - id: skills-commands-hooks-model
    type: wiki
    file: wiki/spine/models/agent-config/model-skills-commands-hooks.md
    title: "Model — Skills, Commands, and Hooks (sibling model)"
tags: [model, per-project-assistant-profile, profiles-plural-per-project, focused-assistant-job, tool-agnostic, 24-7-runnable, agent-config, spine, "2026-05-09"]
---

# Model — Per-Project Assistant Profile

## Summary

A **Per-Project Assistant Profile** is the abstract per-project definition of ONE focused AI-assistant job. Profiles are **plural per project** (operator-doctrinal 2026-05-09 turn 6, sacrosanct: *"PROFILES... PROFILES... NOT PROFILE.. I CAN RUN MULTIPLE OPENCLAW ASSISTANT AT THE SAME TIME FOR ONE PROJECT"*) — a project authors one Profile per focused assistant role (e.g., Continuous Research · Pipeline Synthesis · Maturity Promotion · etc.); multiple Profiles can run concurrently as 24/7 agents on the same or different tools. A Profile is **tool-agnostic by definition** (operator-doctrinal 2026-05-09 turn 4: *"A PROFILE IS WAY MORE THAN JUST SETTING FOR ONE TOOL"* + *"support but not vendor lock ourself"*) — it is NOT a config for any specific tool; any tool (Claude Code · Multica · OpenClaw · Hermes Agent · Claude OS · OpenCode · Codex · etc.) consumes it through the tool's native mechanism. The same Profile can be consumed by **NONE, ONE, OR MULTIPLE tools simultaneously** (operator-doctrinal 2026-05-09 turn 6). Each Profile has 6 required sections (Identity · Knowledge Scope · Action Surface · Model Routing · Prompt Templates · Success Criteria) and high-quality definitions and features. ==The Profile is the spec; the spawned assistant instance is the product; the tool is the execution layer that consumes the spec.== Every project authors its OWN Profiles in its OWN repo; this project (the research wiki) authors its own Profiles AND uniquely hosts the meta-layer (this model · the standards · the integration · the super-model update) that the broader ecosystem consumes.

## Key Insights

- **The Profile is the abstract assistant definition, not a tool config.** Tool-agnosticism is constitutive (operator-doctrinal). A Profile with a `runtime_targets: [multica, claude-code]` field is corrupt — the schema embeds vendor-lock. The Profile defines WHAT the assistant IS for the project; tools consume it; the Profile never changes shape to fit any tool.

- **Profiles are PLURAL per project; each is ONE focused job.** A comprehensive Profile lumping "knowledge curation + methodology stewardship + ingestion + distillation" into one is corruption. Each focused assistant job gets its own Profile. Multiple Profiles per project run concurrently — operator example: "two 24/7 for just the second-brain" simultaneously with "one for the root-ghostproxy".

- **The Profile spans the 7-layer [[declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools|Declarative Agent Programming Spectrum]]**. Identity ↔ L0 Agents Brain Files; purpose ↔ L1 SDD-style spec intent; Action Surface ↔ L2 Skills + L3 Commands + L5 Hooks; Knowledge Scope ↔ L4 Context; Model Routing ↔ L6 Harness preferences. The Profile is the project-level anchor that compiles the spectrum's abstractions into a concrete assistant.

- **The same Profile, NONE / ONE / MULTIPLE tools consuming.** Operator-doctrinal 2026-05-09 turn 6: *"MANAGING ACROSS NONE, ONE OR MULTIPLE TOOL"*. A Profile can exist as a definition without a current consumer; or be consumed by one tool (one assistant instance); or be consumed simultaneously by multiple tools (e.g., OpenClaw + Multica both running the Continuous Research role with different cadences). Profile stays stable across consumer count changes.

- **Profile evolves with project needs, not tool changes.** A new Claude Code feature, a Multica CLI addition, an Anthropic billing policy shift — none of these change the Profile. A new project responsibility, a validated lesson, a renegotiated cross-project boundary — these update the Profile.

- **6 required sections form the structural contract**. Identity (what the assistant IS) · Knowledge Scope (what it can know) · Action Surface (what it can/can't do + escalation) · Model Routing (abstract tier preferences) · Prompt Templates (the actual prose, operator-doctrinal language preserved verbatim) · Success Criteria (observable outcomes + telemetry + anti-signals). The schema is the quality floor.

- **High quality DEFINITIONS and FEATURES** (operator-doctrinal 2026-05-09 turn 1). The standard scores BOTH dimensions: precision of the definitions (Identity / Scope / Surface unambiguous + bounded) AND value of the features (Action Surface concrete + Success Criteria observable). A Profile scoring high on one and low on the other fails the standard.

## Deep Analysis

### Why Profiles are plural per project (the load-bearing distinction from earlier corruption)

A naive design says "one Profile per project — it defines THE assistant". This was the framing I initially built; operator corrected sharply at turn 6. The correction makes structural sense:

- An AI assistant for a single project has multiple distinct jobs (research · synthesis · maturity-promotion · validation · cross-reference-maintenance · etc.)
- Each job has different cadence (research = continuous monitoring; synthesis = backlog-driven batch; promotion = event-driven on criteria-met)
- Each job has different success criteria (research = vision-currency; synthesis = backlog-reduction + ratio-compliance; promotion = operator-accept-rate)
- Each job has different Action Surface boundaries
- Lumping them into one Profile produces a mega-spec that fails progressive disclosure, fails focused-prompt-template authoring, fails per-job success metrics

The plural design produces:
- ONE Profile per focused job
- Each runnable independently as a 24/7 agent
- Each with focused prompts + focused success criteria
- Multiple can run concurrently (operator: "two 24/7 for just the second-brain on the same computer")

### Why tool-agnosticism is constitutive

Operator-doctrinal 2026-05-09 turn 4 (sacrosanct): *"DO NOT REDEFINE WHAT PROFILE MEAN.... A PROFILE IS WAY MORE THAN JUST SETTING FOR ONE TOOL"*. The corruption mode is treating Profile as Claude-Code-config or Multica-agent-spec. The constitutive nature is the inverse: Profile defines the assistant; tools come and go around it.

Concrete examples:
- A Profile says "model preference: high-capability for complex synthesis" — the consuming tool decides which actual model (Claude Opus 4.7 / Kimi K2.6 / custom LoRA)
- A Profile says "must have access to the wiki knowledge base" — different tools wire it differently (MCP / file mount / API)
- A Profile says "cost ceiling $30-50/month value-equivalent" — different tools meter differently

This preserves [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|the anti-vendor-lock-in mission]] at the Profile layer.

### Position in the spine (relationship to other models)

| Sibling spine model | Relationship |
|---|---|
| [[model-skills-commands-hooks\|Model — Skills, Commands, Hooks]] | Skills + Commands + Hooks are the **mechanisms** (L2 + L3 + L5 in the spectrum) — Profile's Action Surface SPECIFIES which skills/commands/hooks the assistant has access to. The mechanisms model is constitutive at the mechanism layer; Profile model is constitutive at the per-project-job layer. |
| [[model-context-engineering\|Model — Context Engineering]] | Context engineering (L4 in spectrum) is what populates the assistant's reasoning. Profile's Knowledge Scope SPECIFIES the assistant's context scope. |
| [[model-markdown-as-iac\|Model — Markdown-as-IaC]] | Profile is a Markdown-as-IaC artifact (declarative YAML/markdown, not imperative code) — instances of the markdown-as-IaC pattern at the assistant-definition layer. |
| [[model-claude-code\|Model — Claude Code]] | Claude Code is one consumer of Profiles (alongside Multica, OpenClaw, Hermes Agent, etc.). The Profile abstracts above any specific consumer. |
| [[model-methodology\|Model — Methodology]] | Methodology defines stages + ALLOWED/FORBIDDEN outputs at the project-work layer; Profile's Action Surface uses methodology-stage knowledge to scope per-job action surfaces. |

### Authoring discipline

| Question | Answer |
|---|---|
| Who authors project X's Profiles? | Project X (in project X's own repo) |
| How many Profiles per project? | **Plural** — one per focused assistant job |
| Can this project author sister-project Profiles? | NO — boundary violation. Each project authors its own. |
| Who authors the standards / model / integration / super-model? | **this project (the research wiki) uniquely** (this is this project's contribution beyond its own Profiles) |
| Where do focused Profiles live? | At the project's repo: typically `.assistant/<profile-name>.yaml` per Profile, or equivalent path convention |
| How many tools can consume one Profile? | NONE, ONE, or MULTIPLE — operator-doctrinal flexibility |

### Canonical examples (instances of this model)

| Profile | Where it lives | Focused job |
|---|---|---|
| [[profile-continuous-research-keep-models-and-tech-vision-current\|Continuous Research]] | wiki/domains/cross-domain/ | Keep models + technology-vision current (operator-named example #1) |
| [[profile-pipeline-synthesis-from-raw-to-wiki-page-still-not-at-end-of-pipeline\|Pipeline Synthesis]] | wiki/domains/cross-domain/ | Synthesize ingested information still not at end of pipeline (operator-named example #2) |
| (more this project Profiles per operator-naming, with "things like this...") | wiki/domains/cross-domain/ | TBD |
| Per-sister-project Profiles (OpenArms · OpenFleet · AICP · OpenClaw · root-ghostproxy · etc.) | Each project's OWN repo | NOT this project's authoring scope |

### Profile lifecycle

```
Profile authored (project owner)
   ↓
Profile referenced from this project (standards + model + integration applied)
   ↓
Tool A consumes Profile → spawns assistant instance A (e.g., OpenClaw 24/7)
Tool B consumes Profile → spawns assistant instance B (e.g., Multica scheduled)
Tool C may also consume (or not consume — NONE is valid)
   ↓
Assistant instances produce telemetry per Profile.success_criteria
   ↓
Operator audits telemetry vs Profile's stated outcomes
   ↓
Profile updates when project NEEDS change (NOT when tools change)
```

### Anti-patterns this model rejects

| Anti-pattern | Why bad |
|---|---|
| One comprehensive Profile per project | Plural-per-project doctrine violation (turn 6) |
| `runtime_targets:` field in Profile schema | Tool-coupling corruption (turn 4) |
| this project authoring sister-project Profiles | Cross-project boundary violation (turn 5) |
| "Profile-as-source-of-truth vs distributed-config" framing | Redefines Profile as a tool-config-superset (turn 4 corruption) |
| Asking confirm-questions in the Profile | The Profile asserts; doesn't ask |
| Lumping multiple jobs ("knowledge curation + methodology stewardship + ...") | Plural-per-project doctrine violation |
| Tool-specific section names (e.g., "Multica wiring") | Tool-coupling corruption |

### Why this Model is at this project and not in sister projects

Operator-doctrinal 2026-05-09 turn 5 (sacrosanct): *"the difference in the second-brain is that we do not only have profiles for AI assistants but we will also have the standards and the model and integration into the knowledge and super-models"*. The Profile **model** (this page) is one of four this-project-unique meta-layer artifacts; sister projects consume from this project, don't host these artifacts. This is this project's contribution to the ecosystem.

## Relationships

- BUILDS ON: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]] — the pattern is the design; this model is the named-concept-in-spine-registry
- BUILDS ON: [[per-project-assistant-profile-standards|Per-Project Assistant Profile Standards]] — standards are the quality contract; this model is the conceptual home
- BUILDS ON: [[declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools|Concept — Declarative Agent Programming Spectrum]] — the 7-layer spectrum that Profile spans
- COMPLEMENTS: [[model-skills-commands-hooks|Model — Skills, Commands, Hooks]] — mechanism-level sibling model; Profile's Action Surface specifies which mechanisms the assistant has access to
- COMPLEMENTS: [[model-context-engineering|Model — Context Engineering]] — context-layer sibling; Profile's Knowledge Scope scopes the assistant's context
- COMPLEMENTS: [[model-markdown-as-iac|Model — Markdown-as-IaC]] — Profile is a markdown-as-IaC instance at the per-project-job layer
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Lesson — Anti-Vendor-Lock-In]] — tool-agnosticism is constitutive to the model
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — Profile is a structural artifact governing assistant behavior
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]] — 6-section YAML structure programs behavior
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — Success Criteria + telemetry make Profile claims falsifiable
- INSTANCES: [[profile-continuous-research-keep-models-and-tech-vision-current|Continuous Research]] · [[profile-pipeline-synthesis-from-raw-to-wiki-page-still-not-at-end-of-pipeline|Pipeline Synthesis]]

## Backlinks

[[Pattern — Per-Project Assistant Profile]]
[[per-project-assistant-profile-standards|Per-Project Assistant Profile Standards]]
[[Concept — Declarative Agent Programming Spectrum]]
[[Model — Skills, Commands, Hooks]]
[[model-context-engineering|Model — Context Engineering]]
[[Model — Markdown-as-IaC]]
[[Lesson — Anti-Vendor-Lock-In]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[Continuous Research]]
[[profile-integration-into-the-knowledge-cross-reference-topology-with-existing-wiki-layers|Concept — Profile Integration into the Knowledge: cross-reference topology between Per-Project Assistant Profiles and existing this project wiki layers (lessons · patterns · decisions · models · standards · super-model)]]
