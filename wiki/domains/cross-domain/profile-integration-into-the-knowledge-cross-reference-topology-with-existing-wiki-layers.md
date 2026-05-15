---
title: "Concept — Profile Integration into the Knowledge: cross-reference topology between Per-Project Assistant Profiles and existing /opt wiki layers (lessons · patterns · decisions · models · standards · super-model)"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: operator-correction-2026-05-09-turn-5
    type: directive
    file: raw/notes/2026-05-09-operator-correction-turn-5-every-project-does-own-profile-opt-difference-is-standards-model-integration-super-models-do-not-lose-yourself.md
    title: "Operator turn 5 — /opt's difference: standards + model + integration into the knowledge + super-models"
  - id: operator-correction-2026-05-09-turn-6
    type: directive
    file: raw/notes/2026-05-09-operator-correction-turn-6-profiles-plural-per-project-each-is-one-focused-assistant-job-continuous-research-ingestion-synthesis-stop-conflating.md
    title: "Operator turn 6 — Profiles plural per project; each is one focused job"
  - id: profile-model
    type: wiki
    file: wiki/spine/models/agent-config/model-per-project-assistant-profile.md
    title: "Model — Per-Project Assistant Profile (spine)"
  - id: profile-standards
    type: wiki
    file: wiki/spine/standards/per-project-assistant-profile-standards.md
    title: "Per-Project Assistant Profile Standards (spine)"
  - id: profile-pattern
    type: wiki
    file: wiki/patterns/01_drafts/per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes.md
    title: "Pattern — Per-Project Assistant Profile"
  - id: spectrum
    type: wiki
    file: wiki/domains/ai-agents/declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools.md
    title: "Concept — Declarative Agent Programming Spectrum (7 layers)"
  - id: wiki-schema
    type: file
    file: wiki/config/wiki-schema.yaml
    title: "Schema — 17 relationship verbs + 9 frontmatter fields + page types"
  - id: super-model
    type: wiki
    file: wiki/spine/super-model/super-model.md
    title: "Spine Super-Model (target of T087 update)"
tags: [concept, profile-knowledge-integration, cross-reference-topology, navigation-substrate, gateway-discoverability, wiki-graph, /opt-meta-layer, "2026-05-09", e024-m006, cross-domain, synthesized]
---

# Concept — Profile Integration into the Knowledge

> [!info] **Third of /opt's four meta-layer artifacts** (operator-doctrinal 2026-05-09 turn 5: *"standards and the model and integration into the knowledge and super-models"*). Standards ✅. Model ✅. **Integration (this page).** Super-model update — pending operator-approval.

## Summary

How Per-Project Assistant Profiles integrate into the existing /opt knowledge graph — the **cross-reference topology** that connects Profile artifacts (the abstract assistant definitions) with the rest of the wiki (lessons · patterns · decisions · models · standards · super-model). Profiles are not isolated artifacts — they CONSUME knowledge from existing layers (a Profile's Knowledge Scope cites methodology.yaml + lessons + standards; its Action Surface respects existing rules; its Prompt Templates preserve operator-doctrinal language verbatim) AND CONTRIBUTE BACK (Profile evolution feeds new lessons about what works; Profile success/failure becomes evidence for principles). This page documents the bidirectional cross-reference topology, the navigation substrate (how /opt's gateway · wiki_search MCP · view CLI · obsidian sync surface Profile-related content), and the discipline of keeping Profile-layer ↔ existing-layer connections healthy. The integration is what makes Profiles **first-class navigable knowledge** rather than orphan configuration files.

## Key Insights

- **Profiles consume the knowledge graph; they don't replace it.** A Profile's Knowledge Scope cites paths in `wiki/spine/` + `wiki/lessons/` + `wiki/config/` + raw/notes/. Its Prompt Templates preserve operator-doctrinal language (verbatim quotes from raw/notes/). Its Success Criteria reference existing principles (P1-P4). Profiles are KNOWLEDGE CONSUMERS at authoring time.

- **Profiles contribute BACK to the knowledge graph.** When a Profile-instance runs (as an OpenClaw / Multica / etc. agent), its successes + failures + surfaced findings become evidence for new lessons + patterns + decisions. The Profile's Success Criteria + anti_signals_to_watch are themselves a data source.

- **Bidirectional cross-references make the topology navigable.** A Profile page links to the lessons it implements. The lessons link back to the Profiles that demonstrate them. Gateway · wiki_search · view CLI all surface this bidirectional connection. Without the back-links, Profiles are read-only consumers; with them, Profiles are participants in the knowledge graph.

- **The 17 relationship verbs codify how Profiles connect.** Profile→knowledge uses BUILDS ON · IMPLEMENTS · BUILDS ON · COMPLEMENTS · DEMONSTRATES. Knowledge→Profile uses INSTANCES · DEMONSTRATED BY · ENABLES · USED BY. The verbs are part of the integration discipline, not decorative.

- **Profiles are surfaceable via existing gateway tools.** No new MCP tool needed — wiki_search finds Profile pages by query; wiki_read_page reads them; wiki_list_pages enumerates them by type=concept + domain filter; gateway query surfaces them per existing query semantics. Profile integrates by USING existing surfacing primitives.

- **Each focused Profile = one anchor in the knowledge graph.** Plural-per-project (per turn 6) means multiple anchor points per project — not one mega-Profile that's hard to navigate. Each Profile is discoverable independently; together they form the project's assistant-substrate.

## Deep Analysis

### The Bidirectional Cross-Reference Topology

```
                      ┌─────────────────────────────────┐
                      │   PROFILE (e.g., Continuous     │
                      │   Research, Pipeline Synthesis) │
                      └────────────┬────────────────────┘
                                   │
            BUILDS ON / IMPLEMENTS / COMPLEMENTS / DEMONSTRATES
                                   ▼
       ┌───────────────────────────────────────────────────────┐
       │                                                       │
       ▼                                                       ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   Lessons    │  │   Patterns   │  │  Decisions   │  │ Models +     │
│ (operational │  │ (architectural│  │ (operator-   │  │  Standards   │
│  knowledge)  │  │  patterns)   │  │  territory)  │  │  (spine)     │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │                 │
       └─ DEMONSTRATED BY / INSTANCES / ENABLES / USED BY ────┘
                                   ▲
                                   │
                      ┌─────────────────────────────────┐
                      │   PROFILE (bidirectional —      │
                      │   knowledge graph links back)   │
                      └─────────────────────────────────┘
```

### Outgoing References (Profile → existing wiki)

A Profile page MUST reference, in its Relationships section, the existing wiki content it consumes / depends on. Verbs in use:

| Relationship | Used when | Example |
|---|---|---|
| **BUILDS ON** | Profile builds on a principle, model, or foundational artifact | "BUILDS ON [[Model — Per-Project Assistant Profile]]" |
| **IMPLEMENTS** | Profile implements an operator-stated directive or a documented pattern | "IMPLEMENTS [[operator-directive-2026-05-09-turn-6]]" |
| **COMPLEMENTS** | Profile complements a sibling Profile or pattern within the same project | "COMPLEMENTS [[/opt Pipeline Synthesis Profile]]" |
| **DEMONSTRATES** | Profile demonstrates a principle in practice | "DEMONSTRATES [[Principle 4 — Declarations Aspirational Until Verified]]" |
| **DEPENDS ON** | Profile depends on upstream artifacts (config files, schemas, templates) | "DEPENDS ON [[wiki/config/artifact-types.yaml]]" |
| **RELATES TO** | Profile relates to but doesn't directly consume | "RELATES TO [[anti-vendor-lock-in-...]] mission lesson" |

### Incoming References (existing wiki → Profile)

The reverse direction — existing wiki pages link BACK to Profiles where applicable:

| Relationship | Used when | Example |
|---|---|---|
| **INSTANCES** | A model lists Profiles as instances | "INSTANCES: [[/opt Continuous Research]] · [[/opt Pipeline Synthesis]]" |
| **DEMONSTRATED BY** | A lesson is demonstrated by a Profile in practice | "DEMONSTRATED BY: [[/opt Continuous Research Profile]] — keeps anti-vendor-lock-in mission alive via monitoring breadth" |
| **ENABLES** | An artifact enables Profiles to be authored | "ENABLES: every focused Profile authored against this Standards" |
| **USED BY** | Schema / template is used by Profile authoring | "USED BY: every /opt focused Profile" |
| **PART OF** | Profile is part of a larger structure | "PART OF: /opt's plural-Profiles ecosystem" |

### How Existing Pages Need Updates (the integration discipline)

To make the topology bidirectional, existing pages need INCOMING reference additions:

| Existing page | Add backlinks for | Status |
|---|---|---|
| [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence\|Lesson — Anti-Vendor-Lock-In]] | DEMONSTRATED BY → /opt Continuous Research Profile · /opt Pipeline Synthesis Profile · Profile Standards · Profile Model | Pending (operator-territory: don't auto-edit lessons) |
| [[declarations-are-aspirational-until-infrastructure-verifies-them\|Principle 4]] | DEMONSTRATED BY → /opt Profiles (Success Criteria are verifiable) | Pending |
| [[infrastructure-over-instructions-for-process-enforcement\|Principle 1]] | DEMONSTRATED BY → Profile Standards (structural quality enforcement) | Pending |
| [[model-skills-commands-hooks\|Model — Skills, Commands, Hooks]] | COMPLEMENTS → Profile Model (Profile Action Surface specifies which skills/commands/hooks the assistant accesses) | Pending |
| [[model-context-engineering\|Model — Context Engineering]] | COMPLEMENTS → Profile Model (Profile Knowledge Scope scopes context engineering's input) | Pending |
| [[never-synthesize-from-descriptions-alone\|Lesson — Never synthesize from descriptions alone]] | DEMONSTRATED BY → /opt Pipeline Synthesis Profile (Action Surface explicitly forbids) | Pending |

These backlinks are operator-territory in many cases (touching validated lessons / spine principles). Auto-editing is forbidden; surfacing as a punch-list for operator review IS in scope.

### Navigation Substrate: How Profile-Related Content Surfaces

> [!info] **No new MCP tool needed. Existing gateway + wiki_search + view + pipeline tools surface Profile content using existing semantics.**

| How to find Profile content | Tool / command |
|---|---|
| Find all Profile pages | `wiki_list_pages --type=concept --domain=cross-domain --tag=per-project-assistant-profile` OR `view search "Profile"` |
| Find a specific Profile | `wiki_read_page "Continuous Research"` OR `wiki_search "Profile continuous research"` |
| Find Profiles that DEMONSTRATE a principle | Read principle page → check INSTANCES / DEMONSTRATED BY backlinks |
| Find lessons a Profile builds on | Read Profile page → check BUILDS ON / DEMONSTRATES outgoing |
| Find /opt's plural Profiles vs sister-project Profiles | `view domains` filtered on tag=profiles-plural-per-project (/opt only — sister projects host their own in their own repos) |
| Find Profile Standards / Model | `view spine` → standards / models / agent-config |
| 5-channel RRF semantic search | `wiki_search` MCP with 5-channel RRF (covers exact-fact-key, FTS, vector, HyDE, raw body) |

### Schema-Level Integration (operator-approval territory)

Currently the Profile is `type: concept` (the most flexible page type that supports the 6-section structural contract). Future option (operator-approval at /opt): codify `type: per-project-assistant-profile` as a recognized page type in `wiki/config/wiki-schema.yaml` + `wiki/config/artifact-types.yaml`. This would:
- Enable per-type validation rules (e.g., enforce the 6 required sections via `pipeline post`)
- Enable per-type templates at `wiki/config/templates/per-project-assistant-profile.md`
- Enable per-type scaffolding via `pipeline scaffold per-project-assistant-profile "<name>"`

Status: PROPOSED. Operator-decision: codify now (when 2 examples exist) or wait (until more examples surface drift patterns).

### Super-Model Integration (T087 — operator-approval territory)

The spine super-model at [[super-model|wiki/spine/super-model/super-model.md]] currently lists 16 models. Adding "Per-Project Assistant Profile" makes it 17. The super-model is operator-canonical; this update is operator-approval territory at /opt. **NOT auto-applied here**. Surfacing the candidate change is in-scope; applying is not.

### Anti-Patterns This Integration Concept Rejects

| Anti-pattern | Why bad |
|---|---|
| Profile page with NO Relationships section | Profile floats in the graph; isn't discoverable; isn't navigable from neighboring pages |
| Outgoing references only (no backlinks added to existing pages) | One-way topology = poor discoverability from neighboring pages; gateway query / wiki_search find fewer paths |
| Auto-editing operator-territory pages to add backlinks | Boundary violation; backlinks to validated lessons / spine principles are operator-territory |
| Inventing new relationship verbs for Profiles | The 17 existing verbs cover Profile integration; inventing is unnecessary + dilutes schema |
| New MCP tool for "find Profiles" | Existing tools already find Profiles via tag/domain/type filtering; new tool is over-engineering |
| Profile in a folder that breaks domain-folder match (Hard Rule 11) | Profile lives where its domain says it lives; cross-domain Profile → wiki/domains/cross-domain/ |

## The Three /opt-Layer Meta-Artifacts In One Picture

```
┌──────────────────────────────────────────────────────────────┐
│                    /opt SECOND-BRAIN                          │
│  (the unique meta-layer contribution to the Profile ecosystem)│
└──────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌──────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  STANDARDS   │  │     MODEL       │  │  INTEGRATION    │
│ (T084 ✅)    │  │  (T085 ✅)      │  │  (T086 — this   │
│              │  │                 │  │   page ✅)      │
│ What good    │  │ Named model in  │  │ Cross-reference │
│ Profile      │  │ the 16-model    │  │ topology with   │
│ looks like + │  │ spine registry  │  │ existing wiki   │
│ quality gates│  │                 │  │ layers          │
└──────────────┘  └─────────────────┘  └─────────────────┘
                            │
                            ▼
                  ┌─────────────────┐
                  │  SUPER-MODEL    │
                  │  UPDATE (T087)  │
                  │  pending        │
                  │  operator-      │
                  │  approval       │
                  └─────────────────┘
```

Each layer reinforces the others. Standards says HOW; Model names + positions; Integration connects to the graph; Super-model elevates to foundational status.

## Relationships

- BUILDS ON: [[model-per-project-assistant-profile|Model — Per-Project Assistant Profile]] (the named model this integration concept connects to the rest of the graph)
- BUILDS ON: [[per-project-assistant-profile-standards|Per-Project Assistant Profile Standards]]
- BUILDS ON: [[per-project-assistant-profile-pattern-tailored-config-to-spawn-ecosystem-runtimes|Pattern — Per-Project Assistant Profile]]
- COMPLEMENTS: [[declarative-agent-programming-spectrum-five-layers-spec-skill-context-hook-harness-unified-and-integration-matrix-across-tools|Concept — Declarative Agent Programming Spectrum]] (Profile spans the 7-layer spectrum; this integration concept connects Profile to the wider /opt knowledge)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — integration topology is structural (verbs + page types), not prose advice
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]] — relationship verbs are programmatic schema, not English
- INSTANCES (as the integration topology applied):
  - [[opt-profile-continuous-research-keep-models-and-tech-vision-current|/opt Continuous Research]] — fully integrated (BUILDS ON · IMPLEMENTS · DEMONSTRATES · USED BY all populated)
  - [[opt-profile-pipeline-synthesis-from-raw-to-wiki-page-still-not-at-end-of-pipeline|/opt Pipeline Synthesis]] — fully integrated

## Backlinks

[[model-per-project-assistant-profile|Model — Per-Project Assistant Profile]]
[[per-project-assistant-profile-standards|Per-Project Assistant Profile Standards]]
[[Pattern — Per-Project Assistant Profile]]
[[Concept — Declarative Agent Programming Spectrum]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
