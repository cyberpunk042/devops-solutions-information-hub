---
title: Per-Project Assistant Profile Standards
aliases:
  - "Per-Project Assistant Profile Standards"
  - "Profile Standards"
  - "Assistant Profile Standards"
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
    description: "Operator-stated 2026-05-09: 'repos / projects will have assistants configurations / profiles' + 'have high quality definitions and features' — establishes the need for Profile standards"
  - id: operator-correction-2026-05-09-turn-4
    type: directive
    file: raw/notes/2026-05-09-operator-correction-multi-decision-do-not-corrupt-redefine-profile-stop-skipping-and-minimizing-research-hermes-and-ocmc-properly.md
    description: "Operator correction 2026-05-09 turn 4 (sacrosanct): Profile is the abstract per-project assistant definition; way more than just setting for one tool; tool-agnosticism is constitutive"
  - id: operator-correction-2026-05-09-turn-5
    type: directive
    file: raw/notes/2026-05-09-operator-correction-turn-5-every-project-does-own-profile-opt-difference-is-standards-model-integration-super-models-do-not-lose-yourself.md
    description: "Operator clarification 2026-05-09 turn 5 (sacrosanct, verbatim): 'every project will do their own Profiles... this is per project.. the difference in the second-brain is that we do not only have profiles for AI assistants but we will also have the standards and the model and integration into the knowledge and super-models'. THIS standards page is the this project's (the research wiki) meta-layer artifact — what this project uniquely contributes beyond its own Profile."
  - id: profile-pattern
    type: wiki
    file: wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md
    description: "Parent pattern — the Profile pattern (tool-agnostic after 2026-05-09 refactor) is what these standards govern"
  - id: opt-canonical-profile
    type: wiki
    file: wiki/domains/cross-domain/assistant-profile-the-canonical-tool-agnostic-per-project-assistant-definition.md
    description: "The this project's (the research wiki) own canonical Profile — exemplar of standards application"
  - id: spectrum-concept
    type: wiki
    file: wiki/domains/ai-agents/declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools.md
    description: "Declarative Agent Programming Spectrum (7 layers) — Profile is the abstract anchor spanning the spectrum"
  - id: wiki-schema
    type: file
    file: wiki/config/wiki-schema.yaml
    description: "Schema reference for required frontmatter + relationship verbs (Profile-as-page-type extension proposed but not yet codified)"
tags: [standards, per-project-assistant-profile, page-type-standards, spine-level, quality, exemplar, tool-agnostic, sister-project-consumable, "2026-05-09", cross-domain, synthesized]
---

# Per-Project Assistant Profile Standards

## Summary

Standards for **Per-Project Assistant Profile** artifacts — abstract, tool-agnostic definitions of what a focused AI assistant IS for a specific project. Each Profile = **ONE focused assistant job**; each project has **MULTIPLE Profiles** (plural), one per assistant job. Multiple Profiles per project can run concurrently as 24/7 agents on the same or different tools. Operator-stated 2026-05-09 turn 6 (verbatim, sacrosanct): *"PROFILES... PROFILES... NOT PROFILE.. I CAN RUN MULTIPLE OPENCLAW ASSISTANT AT THE SAME TIME FOR ONE PROJECT... I COULD HAVE TWO 24/7 for just the second-brain"* + named examples: **Continuous Research** + **Synthesize ingested information still not at end of pipeline**. Every project authors its OWN Profiles in its OWN repo; this project (the research wiki) authors its own Profiles AND uniquely hosts this standards page (plus the model, integration, super-model layers) for the broader ecosystem to consume. Each Profile must be tool-agnostic (Profile is NOT a config for any specific tool — Claude Code · Multica · OpenClaw · Hermes Agent · etc. consume it through their native mechanisms; the same Profile can be consumed by 0, 1, or multiple tools simultaneously), must have all 6 required sections (Identity · Knowledge Scope · Action Surface · Model Routing · Prompt Templates · Success Criteria), must be **focused on ONE assistant job** (NOT a lumped multi-role spec), and must have "high quality definitions and features" (operator-doctrinal 2026-05-09) — precision in DEFINITIONS (what the assistant IS) and value in FEATURES (what it actually delivers).

## Key Insights

1. **Profiles are PLURAL per project; each is ONE focused assistant job.** Operator 2026-05-09 turn 6 (sacrosanct): *"PROFILES... PROFILES... NOT PROFILE.. I CAN RUN MULTIPLE OPENCLAW ASSISTANT AT THE SAME TIME FOR ONE PROJECT"*. A project has MANY Profiles (one per focused assistant job — Continuous Research · Pipeline Synthesis · Maturity Promotion · etc.); multiple run concurrently as 24/7 agents on the same or different tools. Lumping multiple jobs into one comprehensive Profile is corruption.

2. **A Profile is per-project, authored by that project.** this project does NOT author OpenArms's Profiles or OpenFleet's Profiles or AICP's Profiles. Each project authors its own Profiles in its own repo. this project (the research wiki) hosts the **standards** + **model** + **integration** + **super-model** that ALL projects consume. Cross-project Profile-authoring at this project is a boundary violation.

2. **A Profile is way more than just setting for one tool** (operator-doctrinal 2026-05-09, sacrosanct). Tool-agnosticism is **constitutive**, not optional. A Profile that says `runtime_targets: [multica, claude-code]` is corrupt — the schema embeds vendor-lock. The Profile defines the assistant abstractly; tools consume it through THEIR mechanisms.

3. **High quality definitions and features (operator 2026-05-09)** means BOTH dimensions: precision of the **definitions** (identity, scope, surface) + value of the **features** (what the assistant actually delivers). A Profile scoring high on one but low on the other is failing the standard.

4. **The 6 sections are the structural contract.** Identity · Knowledge Scope · Action Surface · Model Routing · Prompt Templates · Success Criteria. These hold across project types (knowledge focus / harness focus / fleet orchestration / local-AI / governance / etc.) because they're abstract enough to accommodate domain variance and concrete enough to be testable.

5. **Cross-project boundaries are encoded in Action Surface.** A Profile's `forbidden_actions` explicitly names actions outside the project's scope — including authoring content in sister projects. Together, the ecosystem's Profiles form a contract topology: each project's Profile declares what it does AND what it does NOT do.

6. **Profile evolves with project needs, NOT tool changes.** When Anthropic ships a feature, when Multica adds a CLI, when a new agent runtime emerges — the Profile is unaffected. When the project gains a new responsibility OR a new principle/lesson is validated — the Profile updates.

## Deep Analysis

### Required Sections (the 6 structural contract)

> [!info] **Every Profile MUST have these 6 sections. Profile quality is gated on their completeness + precision + tool-agnosticism.**

| # | Section | Purpose | Minimum content |
|---|---|---|---|
| **1** | **Identity** | Declares what the assistant IS — abstract definition independent of any tool | profile_version, profile_name, project, project_type, project_role, project_domain, owner, tagline, purpose (multi-line), relationship_to_ecosystem (multi-line) |
| **2** | **Knowledge Scope** | Bounds what the assistant can/should know | brain_files (L0 layer) · project_scope (paths in this project's repo) · second_brain_references (this project's content this Profile references — for consumer projects) · external_references (sister-project cross-links) · forbidden_scope (what NOT to bring into the assistant's knowledge) |
| **3** | **Action Surface** | The MUST / MUST NOT list — programs assistant behavior structurally (P2 Structured Context) | allowed_actions (grouped by category) · forbidden_actions (named + reason) · escalation_triggers (when to STOP + escalate) |
| **4** | **Model Routing** | Abstract tier preferences for which model serves which complexity workload | preferences (per complexity tier: need + tier-description) · cost_ceilings (target + hard-stop in value-equivalent USD) · principles (routing doctrine: frontier-pulling, local-when-possible, etc.) |
| **5** | **Prompt Templates** | The actual prose the assistant inherits — operator-doctrinal language preserved verbatim | system (the primary system prompt) · on_X (per-trigger templates: directive-received, error, ambiguity, corruption, pre-compaction, etc.) |
| **6** | **Success Criteria** | How to know the assistant is delivering value (P4 Declarations-Aspirational-Until-Verified) | observable_outcomes (grouped by layer) · measurable_value_per_month · telemetry (where/what is logged) · anti_signals_to_watch (patterns that signal Profile drift) |

### Tool-Agnosticism Discipline (the constitutive requirement)

> [!warning] **Tool-agnosticism is constitutive — a Profile that embeds a specific tool's schema is corrupt.**
>
> Operator-doctrinal 2026-05-09 (sacrosanct, verbatim): *"DO NOT REDEFINE WHAT PROFILE MEAN.... WHY WOULD A PROFILE BE RELATED TO MULTICA IF I DID NOT SAY IT WAS RELATED TO MULTICA.... THIS WOULD BE DOUMN TO ADD A VENDOR LOCK WHEN I LITTERALLY SAID TO SUPPORT BUT NOT VENDOR LOCK OURSELF... A PROFILE IS WAY MORE THAN JUST SETTING FOR ONE TOOL."*

**The corruption test**: read your Profile and try substituting any specific tool name (Multica → Hermes; Claude Code → Codex; etc.) anywhere it appears. Does the Profile still make sense?
- ✅ If the substitution holds (or the tool is named as **context**, not as **target**) → Profile is tool-agnostic
- ❌ If the substitution breaks (the schema field name presupposes the tool, or content depends on the tool's data shape) → Profile is tool-coupled (corrupt)

**Forbidden Profile patterns**:

| ❌ Anti-pattern | Why it's corrupt | Fix |
|---|---|---|
| `runtime_targets: [multica, claude-code, openclaw]` field | Couples Profile to specific tool list; adding/removing tools requires editing every Profile | Remove field; Profile is consumed by tools, not coupled to them |
| Tool-specific section names ("Multica wiring", "Claude Code hooks") | Schema presupposes tool's data model | Use abstract section names (Knowledge Scope · Action Surface · Model Routing) |
| Cost field in tool-specific units (`claude_credit_usd_per_month`) | Couples Profile to one tool's billing model | Use value-equivalent USD abstractly |
| Identity section enumerates "supported tools" | Defines assistant by tool list rather than by purpose | Identity describes WHAT the assistant IS (its role), not WHAT TOOL it uses |
| Action Surface lists tool-specific API calls | Couples allowed actions to tool's tool list | Use abstract capability names (e.g., "knowledge search" not "wiki_search MCP call") — capabilities map to per-tool implementations via the spawn protocol |
| Profile-source-of-truth framing that says "tool configs duplicate the Profile" | Implies Profile IS a tool config that gets distributed | Profile is the abstract definition; tool configs are separate downstream artifacts |

### Per-Project Authoring Rules (plural Profiles per project)

> [!success] **Authoring discipline (who authors what, where, how many)**

| Question | Answer |
|---|---|
| How many Profiles per project? | **PLURAL.** One per focused assistant job. Examples: a project might have a Continuous Research Profile + a Pipeline Synthesis Profile + a Maturity Promotion Profile + others. Multiple run concurrently as 24/7 agents. |
| Who authors project X's Profiles? | Project X. Authored in project X's own repo. |
| Who authors the Profile schema, standards, model, super-model? | this project (the research wiki) (this project) — uniquely. |
| Can this project author sketches of sister-project Profiles? | NO. That's a cross-project boundary violation. Each project authors its own. |
| Can this project provide a TEMPLATE that sister projects use? | YES. Profile templates live at `wiki/config/templates/` and are operator-shipped. |
| Where do a project's authored Profiles live? | At the project's repo: typically `.assistant/<profile-name>.yaml` per Profile (one file per focused job), or equivalent path convention. |
| Where do this project's own Profiles live? | At this project's wiki: `wiki/domains/cross-domain/profile-<job-name>.md` (one file per focused job — e.g., `profile-continuous-research-...md`, `profile-pipeline-synthesis-...md`). |
| Can a Profile reference this project's content? | YES via Knowledge Scope. Sister projects CONSUME from this project; this project does not CREATE FOR them. |
| How many tools can consume a single Profile? | **NONE, ONE, OR MULTIPLE.** Operator 2026-05-09 turn 6 (sacrosanct): *"managing across NONE, ONE OR MULTIPLE TOOL"*. The Profile is the spec; tool consumption is variable. Same Profile, varying number of consumers. |
| Can one job's Profile lump multiple roles? | NO. Each Profile = ONE focused job. Lumping = corruption. If an assistant has more than one job, that's multiple Profiles. |

### Quality Gates

> [!success] **Profile quality is verifiable via these gates**

| Gate | What to check |
|---|---|
| **Schema-pass** | All 6 sections present with required fields populated; YAML valid |
| **Tool-agnosticism-pass** | No `runtime_targets:` field; no tool-specific schema fields; no embedded tool data model; corruption test (substitution) passes |
| **High-quality-definitions** | Identity precisely describes WHAT the assistant IS (role, purpose, relationship); Knowledge Scope unambiguously bounded; Action Surface forbidden/allowed lists exhaustive |
| **High-quality-features** | Action Surface lists concrete reusable capabilities; Success Criteria are observable (not aspirational); telemetry hooks named |
| **Anti-vendor-lock-in-pass** | No tool-specific field anywhere; Profile remains valid under tool substitution |
| **Cross-project-boundary-pass** | Action Surface's `forbidden_actions` explicitly names cross-project edit boundaries; Knowledge Scope's `forbidden_scope` declares non-project content as out-of-scope |
| **Operator-doctrine-preservation** | Prompt Templates preserve operator-stated rules verbatim (no paraphrasing of sacrosanct directives) |
| **Sister-project-consumability** | Profile structure matches the 6-section contract so it's navigable + comparable alongside other projects' Profiles |

### Anti-Patterns to Avoid (lessons distilled 2026-05-09)

| Anti-pattern | Concrete instance | Fix |
|---|---|---|
| this project authors sister-project Profiles | Authoring "OpenArms Assistant Profile" at this project | Delete. Each project authors its own. this project provides standards + model + integration + super-model. |
| Profile schema includes `runtime_targets:` | Field listing which tools the Profile "supports" | Remove. Profile is consumed by tools, not coupled. |
| Profile-vs-tool-config conflation | "Profile-as-source-of-truth vs distributed-config" decision question | Drop the framing. Profile is the abstract definition; tool configs are separate. |
| Tool-specific cost units | `claude_credit_usd_per_month: 50` | Use value-equivalent: `target_monthly_value_output_usd_equivalent: 50` |
| Spawn protocol coupling in the Profile itself | Profile pattern listing "OpenClaw spawn protocol" as a Profile property | Move to companion patterns; Profile remains independent |
| Deformation of operator's quality assertion | Treating "have high quality definitions and features" as a "define a quality bar" decision | Quality assertion ≠ quality-bar definition. The standard IS high quality in definitions + features. |
| Asking confirm-questions about settled facts | Asking operator to confirm plan tier when they already named it | Don't. State the implication and proceed. |
| Skipping research the operator named | Deferring Hermes CLI research to "later" | Do it. Operator-named research is in-scope by default. |
| Claiming "empty" without auth-verification | Pipeline-fetch returns "No README" → claim repo has no content | Verify via auth-bearing tool (gh CLI) before claiming. |

### How a New Project Adopts the Profile Standard

1. **Read these standards** + read this project's canonical Profile as an exemplar
2. **Create `.assistant/profile.yaml`** in the project repo
3. **Populate all 6 sections** with the project's actual needs (NOT a template clone)
4. **Run the corruption test**: no tool-specific schema fields; abstract content throughout
5. **Validate via quality gates** (above)
6. **Iterate as needs evolve** (Profile changes with project needs, not tool changes)
7. **Optionally cross-reference** from this project (the research wiki) via gateway contribute (lands in 00_inbox)

### How this project Maintains These Standards

1. Operator-stated additions to the contract → update these standards
2. New anti-patterns observed → add to the table
3. New quality gates surfaced → add to the gates table
4. Sister-project feedback → integrate (operator-mediated)
5. Schema codification: if Profile becomes a recognized wiki page type, extend `wiki/config/wiki-schema.yaml` + `wiki/config/artifact-types.yaml` (operator-approval)

## Cross-references to other this-project meta-layer artifacts

The Per-Project Assistant Profile Standards is **one of four** this-project meta-layer artifacts (operator-named 2026-05-09 turn 5: "standards and the model and integration into the knowledge and super-models"). The others (planned):

| Artifact | Status | Purpose |
|---|---|---|
| **Per-Project Assistant Profile Standards** (this page) | ✅ done | What good Profile looks like; quality gates |
| **Model — Per-Project Assistant Profile** (`wiki/spine/models/agent-config/`) | Pending | The named model in the 16-model registry (operator-approval for promotion) |
| **Profile-Knowledge Integration** | Pending | How Profile integrates with existing wiki (lessons, patterns, decisions, super-model) — cross-reference topology |
| **Super-Model update** | Pending | Add Profile to the spine super-model so it's foundational to the system |

These four together comprise this project's unique contribution to the Profile ecosystem. Other projects (OpenArms, OpenFleet, AICP, dcp, OpenClaw, root-ghostproxy) author their own Profiles consuming these standards/model/integration/super-model artifacts.

## Relationships

- IMPLEMENTS: [[2026-05-09-operator-correction-multi-decision-do-not-corrupt-redefine-profile-stop-skipping-and-minimizing-research-hermes-and-ocmc-properly|Operator correction 2026-05-09 turn 4]] (tool-agnosticism doctrine)
- BUILDS ON: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]] (the pattern these standards govern)
- BUILDS ON: [[assistant-profile-the-canonical-tool-agnostic-per-project-assistant-definition|Second-Brain Assistant Profile]] (exemplar of standards application)
- BUILDS ON: [[declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools|Concept — Declarative Agent Programming Spectrum]] (Profile spans the 7-layer spectrum)
- COMPLEMENTS: [[lesson-page-standards|Lesson Page Standards]] / [[decision-page-standards|Decision Page Standards]] / [[pattern-page-standards|Pattern Page Standards]] / etc. — same spine-standards convention applied to Profile artifacts
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Lesson — Anti-Vendor-Lock-In]] — tool-agnosticism standard preserves the mission
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — standards are structural quality enforcement, not prose advice
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]] — 6 required sections are YAML-structured contract
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — quality gates make Profile claims verifiable

## Backlinks

[[Operator correction 2026-05-09 turn 4]]
[[Pattern — Per-Project Assistant Profile]]
[[Second-Brain Assistant Profile]]
[[Concept — Declarative Agent Programming Spectrum]]
[[lesson-page-standards|Lesson Page Standards]]
[[Lesson — Anti-Vendor-Lock-In]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[profile-integration-into-the-knowledge-cross-reference-topology-with-existing-wiki-layers|Concept — Profile Integration into the Knowledge: cross-reference topology between Per-Project Assistant Profiles and existing this project wiki layers (lessons · patterns · decisions · models · standards · super-model)]]
[[cursor-state-folder-standards-common-cross-project-runtime-state-surface|Cursor State Folder Standards (`.cursor/`) — Common Cross-Project Runtime State Surface for /view · /questions · vision · focus · trace]]
[[e024-m006-cross-project-profile-catalog-everywhere-integration|E024-M006 — this-project Meta-Layer for Per-Project Profiles (standards · model · integration · super-model) — the unique this project contribution; sister projects author their OWN Profiles consuming this meta-layer]]
[[model-per-project-assistant-profile|Model — Per-Project Assistant Profile]]
[[profile-continuous-research-keep-models-and-tech-vision-current|Profile — this project Continuous Research: focused assistant Profile for keeping models + technology-vision current; runnable as a 24/7 OpenClaw (or other tool) agent]]
[[profile-pipeline-synthesis-from-raw-to-wiki-page-still-not-at-end-of-pipeline|Profile — this project Pipeline Synthesis: focused assistant Profile for synthesizing ingested information still not at end of pipeline (raw → wiki page); runnable as a 24/7 OpenClaw (or other tool) agent]]
