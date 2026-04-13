---
title: E003 Artifact Type System — Design Document
aliases:
  - "E003 Artifact Type System — Design Document"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: growing
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: requirements-spec
    type: file
    file: wiki/domains/cross-domain/e003-artifact-type-system-requirements.md
  - id: openarms-artifact-spec
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms project reference"
  - id: openarms-methodology
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms methodology.yaml configuration"
  - id: wiki-schema
    type: file
    file: wiki/config/wiki-schema.yaml
tags: [methodology, design, artifact-types, e003, type-system, architecture]
---

# E003 Artifact Type System — Design Document

## Summary

Design decisions and architecture for the Artifact Type System. Resolves all open questions from the requirements spec with concrete decisions backed by evidence from the openarms implementation and the wiki's own operational experience. Defines the config schema, template architecture, artifact chain structure, domain profile pattern, and the operations plan vs design plan distinction. Every decision includes rationale and reversibility assessment.

## Key Insights

1. **Methodology documents stay as wiki page types — no separate category** — a requirements spec IS a concept page with a methodology-specific template. Adding a parallel document system would split the knowledge graph. The wiki is the single container; templates provide the structural variation.

2. **One new page type only: `operations-plan`** — this is the one type that's structurally incompatible with ANY existing type. A sequential checklist with per-step validation criteria doesn't fit concept, reference, or any other existing type. Everything else maps to existing types with methodology-specific templates.

3. **Domain profiles override at the stage level** — not per-artifact-type, not per-model. A domain profile says: "for stage X, the gate commands are Y, the path patterns are Z, the forbidden zones are W." This is the granularity that worked in openarms and it's the simplest that's useful.

4. **Artifact chains live inside model definitions, not separate files** — a model without its chain is incomplete. Splitting them creates sync problems. The methodology config will be large but coherent. This matches what openarms does and what actually works.

## Deep Analysis

### Decision 1: Where Methodology Documents Live

> [!success] Decision: Methodology documents are wiki pages with methodology-specific templates
>
> | Document Type | Wiki `type:` | Template Location | Rationale |
> |--------------|-------------|-------------------|-----------|
> | Requirements spec | concept | wiki/config/templates/methodology/requirements-spec.md | It IS a concept — the concept of what's required |
> | Infrastructure analysis | concept | wiki/config/templates/methodology/infrastructure-analysis.md | It IS a concept — mapping of what exists |
> | Gap analysis | concept | wiki/config/templates/methodology/gap-analysis.md | It IS a concept — mapping of what's missing |
> | ADR / Design decision | decision | wiki/config/templates/decision.md (existing) | An ADR IS a decision — same schema, same structure |
> | Tech spec | reference | wiki/config/templates/methodology/tech-spec.md | It IS a reference — API tables, interface definitions |
> | Design plan | concept | wiki/config/templates/methodology/design-plan.md | Complex analysis with alternatives — concept structure fits |
> | Operations plan | operations-plan | wiki/config/templates/methodology/operations-plan.md | **NEW TYPE** — structurally incompatible with existing types |
> | Test plan | reference | wiki/config/templates/methodology/test-plan.md | It IS a reference — test ID tables, setup procedures |

**Why not a separate category?** The wiki's power is the knowledge graph. Every page is linked, searchable, validated, exportable. A parallel document system outside the wiki would fragment the graph, require separate validation tooling, and break the "single container" principle. The three pages I created today (infrastructure analysis, gap analysis, requirements spec) are already wiki pages — and they work fine.

**Why one new type (`operations-plan`)?** A sequential checklist with per-step validation criteria, rollback procedures, and completion checkboxes has NO structural overlap with any existing type:
- It's not a concept (no Key Insights, no Deep Analysis)
- It's not a reference (not lookup material)
- It's not a decision (no alternatives analysis)
- It's not a task (a task is a backlog item; an operations plan is a DOCUMENT attached to a task)

> [!warning] Rejected Alternative: Add many new types (requirements-spec, tech-spec, design-plan, etc.)
>
> This would balloon the type enum from 16 to 25+ values. Most of these types share structure with existing types — they just need different templates. Type proliferation makes validation harder, confuses agents about which type to pick, and adds no value over template-based differentiation.

**Reversibility:** Easy. If we later need a distinct type for requirements specs, we add it. Template-based differentiation doesn't prevent future type additions.

---

### Decision 2: Operations Plan Structure

> [!success] Decision: Operations plan is a new page type with step-based structure
>
> | Aspect | Operations Plan | Design Plan (concept) |
> |--------|----------------|----------------------|
> | Purpose | Execute a known sequence | Analyze an unknown problem |
> | Structure | Ordered steps with validation | Sections with analysis |
> | Judgment required | None — mechanical execution | High — trade-offs, alternatives |
> | Delegatable | Yes — dumb agent can follow | No — requires expertise |
> | Sections | Summary, Prerequisites, Steps, Rollback, Completion Criteria | Summary, Key Insights, Deep Analysis, Open Questions |
> | Step structure | Action → Expected output → Validation → Rollback on failure | N/A |

**Schema addition to wiki-schema.yaml:**

```yaml
# In enums.type:
  - operations-plan

# In required_sections:
  operations-plan:
    - Summary
    - Prerequisites
    - Steps
    - Rollback
    - Completion Criteria
    - Relationships
```

**Template structure:**

```yaml
# Steps section format:
## Steps

### Step 1: {{action_title}}
- **Action:** {{what to do}}
- **Expected output:** {{what success looks like}}
- **Validation:** {{how to verify}}
- **Rollback:** {{what to do if it fails}}

### Step 2: ...
```

This is the "deterministic checklist" the operator described — clear, sequential, mechanically executable, with validation at each step.

---

### Decision 3: Template Architecture

> [!success] Decision: Two template directories — wiki pages and methodology documents
>
> ```
> wiki/config/templates/
> ├── concept.md              ← NEW (wiki page type)
> ├── source-synthesis.md     ← NEW (wiki page type)
> ├── comparison.md           ← NEW (wiki page type)
> ├── reference.md            ← NEW (wiki page type)
> ├── deep-dive.md            ← NEW (wiki page type)
> ├── lesson.md               ← EXISTS
> ├── pattern.md              ← EXISTS
> ├── decision.md             ← EXISTS
> ├── domain-overview.md      ← EXISTS
> ├── evolution.md            ← EXISTS
> ├── learning-path.md        ← EXISTS
> ├── operations-plan.md      ← NEW (new page type)
> ├── epic.md                 ← NEW (backlog type)
> ├── task.md                 ← NEW (backlog type)
> └── methodology/            ← NEW (methodology-specific templates)
>     ├── requirements-spec.md
>     ├── infrastructure-analysis.md
>     ├── gap-analysis.md
>     ├── design-plan.md
>     ├── tech-spec.md
>     └── test-plan.md
> ```

**Why two directories?** Wiki page templates map 1:1 to the `type:` enum — the scaffolder uses the type to select the template. Methodology document templates are type-qualified subtypes — they use an existing wiki type (concept, reference, decision) but with methodology-specific structure. The subdirectory makes this clear.

**Template contract:** Every template includes:
1. Complete frontmatter with `{{variables}}` for the scaffolder
2. Sensible defaults for type-specific fields (layer, maturity, status, confidence)
3. All required sections per wiki-schema.yaml in correct order
4. Inline `<!-- STYLING: ... -->` comments directing callout usage
5. Inline `<!-- MIN N words. Guidance on what to write. -->` content guidance
6. A Relationships section pre-populated with `- DERIVED FROM:` or appropriate default verb

---

### Decision 4: Artifact Type Config Schema

> [!success] Decision: New `wiki/config/artifact-types.yaml` that EXTENDS wiki-schema.yaml
>
> wiki-schema.yaml keeps: frontmatter field definitions, enums, required_sections (for backwards compatibility).
> artifact-types.yaml adds: per-type detail (content thresholds, styling requirements, verification methods, template references, category organization).

**Schema structure:**

```yaml
# wiki/config/artifact-types.yaml

categories:
  knowledge-pages:
    description: "Wiki pages containing synthesized understanding"
    layer_range: [1, 3]
    types: [concept, source-synthesis, comparison, reference, deep-dive]

  evolved-pages:
    description: "Wiki pages distilled from other pages"
    layer_range: [4, 6]
    requires_derived_from: true
    types: [lesson, pattern, decision]

  navigation-pages:
    description: "Pages that organize and curate other pages"
    layer: spine
    types: [domain-overview, evolution, learning-path, index]

  backlog-pages:
    description: "Pages tracking planned work"
    types: [epic, module, task, note]

  methodology-documents:
    description: "Documents produced during stage-gated work"
    stage_bound: true  # these are produced at specific stages
    types: [operations-plan]
    # Other methodology docs use existing types with methodology/ templates

types:
  concept:
    category: knowledge-pages
    template: wiki/config/templates/concept.md
    # required_sections inherited from wiki-schema.yaml
    content_thresholds:
      summary_min_words: 30
      deep_analysis_min_words: 100
      min_relationships: 1
    styling:
      callouts_required: false   # concepts CAN use callouts but aren't required to
      callouts_recommended: true  # lint advisory if >80 lines and no callouts
    verification:
      gate: pipeline-post

  source-synthesis:
    category: knowledge-pages
    template: wiki/config/templates/source-synthesis.md
    content_thresholds:
      summary_min_words: 30
      min_relationships: 1
      source_ratio: 0.25  # page length must be ≥25% of raw source length
    styling:
      callouts_required: false
      callouts_recommended: true
      reference_card: true  # should have > [!info] source reference card
    verification:
      gate: pipeline-post
      custom: source-ratio-check

  comparison:
    category: knowledge-pages
    template: wiki/config/templates/comparison.md
    content_thresholds:
      summary_min_words: 30
      deep_analysis_min_words: 100
      min_relationships: 2  # must compare TO something
    styling:
      callouts_required: true  # comparison matrix should be in > [!abstract]
    verification:
      gate: pipeline-post

  reference:
    category: knowledge-pages
    template: wiki/config/templates/reference.md
    content_thresholds:
      summary_min_words: 30
      min_relationships: 1
    styling:
      callouts_required: false
    verification:
      gate: pipeline-post

  deep-dive:
    category: knowledge-pages
    template: wiki/config/templates/deep-dive.md
    content_thresholds:
      summary_min_words: 30
      deep_analysis_min_words: 200  # higher bar — this IS the analysis
      min_relationships: 2
    styling:
      callouts_required: true  # deep-dives must structure with callouts
    verification:
      gate: pipeline-post

  lesson:
    category: evolved-pages
    template: wiki/config/templates/lesson.md
    content_thresholds:
      summary_min_words: 30
      insight_min_words: 50
      min_relationships: 2  # at least DERIVED FROM + one other
      min_evidence_items: 3  # ≥3 independent data points
    styling:
      callouts_required: true
      callout_map:
        Insight: "[!warning] or [!tip]"
        Evidence: "[!bug]- for failures, [!success] for validated"
        Applicability: "table, optionally in [!abstract]"
    verification:
      gate: pipeline-post

  pattern:
    category: evolved-pages
    template: wiki/config/templates/pattern.md
    content_thresholds:
      summary_min_words: 30
      pattern_description_min_words: 100
      min_relationships: 2
      min_instances: 2  # ≥2 concrete instances (not hypothetical)
    styling:
      callouts_required: true
      callout_map:
        Instances: "[!example]- foldable per instance"
        When To Apply: "[!tip]"
        When Not To: "[!warning]"
    verification:
      gate: pipeline-post

  decision:
    category: evolved-pages
    template: wiki/config/templates/decision.md
    content_thresholds:
      summary_min_words: 30
      rationale_min_words: 100
      min_relationships: 2
      min_alternatives: 2  # ≥2 alternatives with rejection rationale
    styling:
      callouts_required: true
      callout_map:
        Decision: "[!success] with scenario-action table"
        Alternatives: "[!warning] per rejected alternative"
    verification:
      gate: pipeline-post
    required_frontmatter:
      - reversibility  # forces cost-of-wrong assessment

  domain-overview:
    category: navigation-pages
    template: wiki/config/templates/domain-overview.md
    content_thresholds:
      summary_min_words: 30
      min_relationships: 3
    verification:
      gate: pipeline-post

  evolution:
    category: navigation-pages
    template: wiki/config/templates/evolution.md
    content_thresholds:
      summary_min_words: 30
    verification:
      gate: pipeline-post

  learning-path:
    category: navigation-pages
    template: wiki/config/templates/learning-path.md
    content_thresholds:
      summary_min_words: 30
      min_sequence_items: 3  # at least 3 pages in sequence
    verification:
      gate: pipeline-post

  operations-plan:
    category: methodology-documents
    template: wiki/config/templates/operations-plan.md
    content_thresholds:
      summary_min_words: 30
      min_steps: 3  # at least 3 steps
    styling:
      callouts_required: false  # checklists don't need callouts
    verification:
      gate: pipeline-post
    # required_sections defined in wiki-schema.yaml

  epic:
    category: backlog-pages
    template: wiki/config/templates/epic.md
    required_frontmatter:
      - priority
      - task_type
      - current_stage
      - readiness
    verification:
      gate: pipeline-post

  task:
    category: backlog-pages
    template: wiki/config/templates/task.md
    required_frontmatter:
      - priority
      - task_type
      - current_stage
      - readiness
      - epic  # must belong to an epic
    verification:
      gate: pipeline-post

  note:
    category: backlog-pages
    template: wiki/config/templates/note.md
    content_thresholds:
      summary_min_words: 10  # notes are short
    verification:
      gate: pipeline-post
```

**Why extend, not replace?** NFR-1 (backwards compatibility). The validate tool currently reads wiki-schema.yaml. We don't break it. artifact-types.yaml adds detail that the validator CAN read for enhanced checking, but the basic validation still works with wiki-schema.yaml alone. Over time, artifact-types.yaml becomes the primary authority and wiki-schema.yaml becomes the minimal compatibility layer.

---

### Decision 5: Artifact Chain Architecture

> [!success] Decision: Chains live inside model definitions in a single config file
>
> Each methodology model defines its artifact chain as part of its model definition. No separate chain file.

**Why inside, not separate?** A model IS its stages + artifacts. Separating them is like separating a function from its return type — technically possible, but creates sync problems and loses coherence. OpenArms puts everything in one 753-line methodology.yaml and it works. The file is large but you never have to cross-reference.

**Config structure (showing Feature Development as example):**

```yaml
# Inside wiki/config/methodology.yaml (the portable version)

models:
  feature-development:
    description: "Full 5-stage model for complex work. Solution not yet known."
    stages: [document, design, scaffold, implement, test]
    readiness_cap: 100
    chain:
      document:
        required:
          - artifact: wiki-page
            count: "1+"
            purpose: "Requirements, infrastructure mapping, gap analysis"
            # Domain profile resolves path_pattern and gate
        forbidden: [code-file, test-file]
        gate:
          checks: [wiki-page-exists, no-code-files-created]

      design:
        required:
          - artifact: design-document
            count: "1+"
            purpose: "ADR, tech spec, config shape, type sketches (IN DOCS)"
            depends_on: [document.wiki-page]
        forbidden: [code-file, test-file]
        gate:
          checks: [design-doc-exists, no-code-files-created]

      scaffold:
        required:
          - artifact: type-definition
            count: "1+"
            purpose: "Types, schemas, static data"
            depends_on: [design.design-document]
          - artifact: test-stub
            count: "1+"
            purpose: "Empty test files with placeholder assertions"
            depends_on: [design.design-document]
        forbidden: [implementation, test-implementation]
        gate:
          checks: [types-compile, no-business-logic, test-stubs-exist]

      implement:
        required:
          - artifact: implementation
            count: "1+"
            purpose: "Business logic filling scaffold stubs"
            depends_on: [scaffold.type-definition]
          - artifact: integration-wiring
            count: "1+"
            purpose: "Existing file imports and calls new code"
            depends_on: [scaffold.type-definition]
        forbidden: [test-implementation]
        gate:
          checks: [code-compiles, lint-passes, integration-wiring-exists]

      test:
        required:
          - artifact: test-implementation
            count: "1+"
            purpose: "Real assertions replacing scaffold placeholders"
            depends_on: [scaffold.test-stub, implement.implementation]
          - artifact: test-results
            purpose: "Gate output showing 0 failures"
        gate:
          checks: [tests-pass, no-placeholder-assertions]

  research:
    description: "Investigation without implementation. Produces understanding."
    stages: [document, design]
    readiness_cap: 50
    chain:
      document:
        required:
          - artifact: wiki-page
            count: "1+"
            purpose: "Research findings with sources and evidence"
        forbidden: [code-file, test-file]
        gate:
          checks: [wiki-page-exists]
      design:
        required:
          - artifact: design-document
            count: "1+"
            purpose: "Options compared, recommendation, implications"
            depends_on: [document.wiki-page]
        forbidden: [code-file, test-file]
        gate:
          checks: [design-doc-exists, options-compared]

  knowledge-evolution:
    description: "Distill higher-layer pages from existing knowledge."
    stages: [document, implement]
    chain:
      document:
        required:
          - artifact: wiki-page
            count: "1"
            purpose: "Source inventory with convergence identified"
        gate:
          checks: [sources-identified, convergence-stated]
      implement:
        required:
          - artifact: wiki-page
            count: "1"
            purpose: "Evolved page (lesson, pattern, or decision)"
            depends_on: [document.wiki-page]
        gate:
          checks: [evolved-page-valid, evidence-from-sources]

  documentation:
    description: "Single-stage. Done when document passes quality gates."
    stages: [document]
    readiness_cap: 100
    chain:
      document:
        required:
          - artifact: wiki-page
            count: "1+"
            purpose: "Wiki page meeting all quality gates"
        gate:
          checks: [wiki-page-valid]

  bug-fix:
    description: "Restore correct behavior. No design needed."
    stages: [document, implement, test]
    chain:
      document:
        required:
          - artifact: wiki-page
            count: "1"
            purpose: "Bug analysis: description, reproduction, root cause"
        gate:
          checks: [root-cause-identified]
      implement:
        required:
          - artifact: code-fix
            count: "1+"
            purpose: "Code change fixing root cause"
            depends_on: [document.wiki-page]
        forbidden: [new-architecture]
        gate:
          checks: [code-compiles, lint-passes]
      test:
        required:
          - artifact: test-implementation
            count: "1+"
            purpose: "Regression test proving fix"
            depends_on: [implement.code-fix]
        gate:
          checks: [tests-pass]

  refactor:
    description: "Restructure without changing behavior."
    stages: [document, scaffold, implement, test]
    chain:
      document:
        required:
          - artifact: wiki-page
            count: "1"
            purpose: "Current structure mapped, target structure defined"
        gate:
          checks: [current-and-target-documented]
      scaffold:
        required:
          - artifact: type-definition
            count: "1+"
            purpose: "New type definitions for target structure"
            depends_on: [document.wiki-page]
        gate:
          checks: [types-compile]
      implement:
        required:
          - artifact: implementation
            count: "1+"
            purpose: "Code moved to new structure, consumers updated"
            depends_on: [scaffold.type-definition]
        gate:
          checks: [code-compiles, lint-passes, no-broken-imports]
      test:
        required:
          - artifact: test-implementation
            count: "1+"
            purpose: "Tests proving behavior unchanged"
            depends_on: [implement.implementation]
        gate:
          checks: [tests-pass, same-assertions-as-before]

  hotfix:
    description: "Emergency fix. Problem and solution already known."
    stages: [implement, test]
    chain:
      implement:
        required:
          - artifact: code-fix
            count: "1+"
            purpose: "Direct fix"
        gate:
          checks: [code-compiles]
      test:
        required:
          - artifact: test-implementation
            count: "1+"
            purpose: "Proof the fix works"
            depends_on: [implement.code-fix]
        gate:
          checks: [tests-pass]

  integration:
    description: "Wire existing standalone modules into runtime. Bridge pattern."
    stages: [scaffold, implement, test]
    chain:
      scaffold:
        required:
          - artifact: type-definition
            count: "1+"
            purpose: "Bridge adapter interfaces, stub functions"
          - artifact: test-stub
            count: "1+"
        gate:
          checks: [types-compile, no-business-logic]
      implement:
        required:
          - artifact: implementation
            count: "1+"
            purpose: "Bridge logic (<80 LOC)"
          - artifact: integration-wiring
            count: "1+"
            purpose: "Existing consumer imports bridge"
        gate:
          checks: [code-compiles, lint-passes, bridge-under-80-loc]
      test:
        required:
          - artifact: test-implementation
            count: "1+"
            purpose: "Tests proving wiring works"
        gate:
          checks: [tests-pass]

  project-lifecycle:
    description: "Macro SFIF model. Other models run inside its stages."
    stages: [scaffold, foundation, infrastructure, features]
    composition: nested  # inner stages use other models
    chain:
      scaffold:
        required:
          - artifact: wiki-page
            purpose: "Project structure, directory layout, config skeleton"
      foundation:
        required:
          - artifact: wiki-page
            purpose: "Core dependencies, base config, CI setup"
        composition_model: documentation  # inner tasks use documentation model
      infrastructure:
        required:
          - artifact: wiki-page
            purpose: "Tooling, automation, deployment pipeline"
        composition_model: feature-development  # inner tasks use full model
      features:
        composition_model: feature-development  # each feature is a full cycle
```

**Composition rule:** When `composition_model` is set, the outer model's stage defines the SCOPE (what kind of work belongs here), and the inner model defines the PROCESS (how that work is executed). The inner model's full artifact chain applies. This is not flattened — it's runtime nesting.

---

### Decision 6: Domain Profile Architecture

> [!success] Decision: Stage-level overrides, layered over generic definitions
>
> | Override Level | What It Controls | Example |
> |---------------|-----------------|---------|
> | Generic (default) | Artifact categories, verification methods | "wiki-page requires Summary section" |
> | Domain profile | Path patterns, gate commands, forbidden zones | "TypeScript: gate = pnpm tsgo; Python: gate = pipeline post" |
> | Project override | Project-specific tweaks | "OpenArms: bridge module required for integration" |

**Profile schema:**

```yaml
# wiki/config/domain-profiles/typescript.yaml
domain: typescript
description: "TypeScript/Node.js projects (OpenArms, OpenFleet)"
stage_overrides:
  scaffold:
    gate_commands: ["pnpm tsgo"]
    path_patterns:
      type-definition: "src/**/*.ts"
      test-stub: "src/**/*.test.ts"
    forbidden_zones: []
  implement:
    gate_commands: ["pnpm tsgo", "pnpm check"]
    path_patterns:
      implementation: "src/**/*.ts"
    forbidden_zones: ["*.test.ts"]
  test:
    gate_commands: ["pnpm test -- {test_file}"]
    path_patterns:
      test-implementation: "src/**/*.test.ts"

# wiki/config/domain-profiles/python-wiki.yaml
domain: python-wiki
description: "Python projects and knowledge wikis (research-wiki)"
stage_overrides:
  document:
    gate_commands: ["python3 -m tools.pipeline post"]
    path_patterns:
      wiki-page: "wiki/**/*.md"
    forbidden_zones: ["tools/", "src/"]
  implement:
    gate_commands: ["python3 -m tools.pipeline post"]
    path_patterns:
      wiki-page: "wiki/**/*.md"
      implementation: "tools/**/*.py"
  test:
    gate_commands: ["python3 -m tools.pipeline post", "python3 -m tools.validate"]

# wiki/config/domain-profiles/infrastructure.yaml
domain: infrastructure
description: "Infrastructure as Code projects (devops-control-plane)"
stage_overrides:
  scaffold:
    gate_commands: ["terraform validate"]
    path_patterns:
      type-definition: "**/*.tf"
  implement:
    gate_commands: ["terraform plan"]
    path_patterns:
      implementation: "**/*.tf"
  test:
    gate_commands: ["terraform plan", "terraform apply -auto-approve (staging)"]
```

**Resolution order:** Generic artifact definition → Domain profile override → Project-specific override. Projects declare their domain in their config (CLAUDE.md, methodology.yaml, or a project.yaml).

**Why stage-level, not per-artifact-type?** Because the gate commands and forbidden zones are properties of STAGES, not individual artifacts. You run `pnpm tsgo` once per stage, not once per artifact. The path patterns are the only per-artifact override, and they nest cleanly inside the stage block. Per-artifact-type overrides would create a combinatorial explosion (9 artifact types × 5 stages × 3 domains = 135 override points). Stage-level gives us 5 stages × 3 domains = 15 override points — manageable.

---

### Decision 7: Validation Extension Strategy

> [!success] Decision: Extend existing validate.py incrementally, reading artifact-types.yaml as optional enhancement
>
> | Phase | What Changes | Backwards Compatible |
> |-------|-------------|---------------------|
> | Phase 1 | validate.py reads artifact-types.yaml for content_thresholds per type | YES — falls back to wiki-schema.yaml |
> | Phase 2 | validate.py checks styling requirements (callouts_required) per type | YES — advisory warnings, not errors |
> | Phase 3 | validate.py checks methodology chain compliance (if methodology context present) | YES — only runs when .methodology-context exists |

The validator already works. We don't rewrite it. We add layers:
1. If artifact-types.yaml exists → use its thresholds instead of quality-standards.yaml defaults
2. If a page's type has `callouts_required: true` and the page has 0 callouts → advisory warning
3. If a methodology context file exists (.methodology-context or similar) → check that produced artifacts match the model's chain requirements

---

### Module Plan (Refined from Requirements Spec)

> [!abstract] Implementation Order
>
> | Order | Module | Scope | Estimate | Depends On |
> |-------|--------|-------|----------|-----------|
> | 1 | M1: artifact-types.yaml | Write the full config file with all types defined | M | Nothing |
> | 2 | M2: Wiki page templates | concept, source-synthesis, comparison, reference, deep-dive | M | M1 (to know what each type requires) |
> | 3 | M3: Backlog + ops-plan templates | epic, module, task, note, operations-plan | S | M1 |
> | 4 | M4: Methodology templates | requirements-spec, infrastructure-analysis, gap-analysis, design-plan, tech-spec, test-plan | M | M1 |
> | 5 | M5: Schema update | Add operations-plan to wiki-schema.yaml, update scaffolder | S | M1, M3 |
> | 6 | M6: Artifact chains | Full chain config for all 9 models + wiki documentation | L | M1 |
> | 7 | M7: Domain profiles | 3 profiles (TypeScript, Python/wiki, Infrastructure) | M | M1, M6 |
> | 8 | M8: Validation extension | Extend validate.py to read artifact-types.yaml | M | M1 |

**M1 is the keystone.** Everything else depends on it. I will scaffold it next.

## Open Questions

> [!question] ~~Should the `module` backlog type get its own required_sections in wiki-schema.yaml? Currently undefined. Recommendation: yes — same as epic ~~
> **RESOLVED:** Yes. Summary, Module Breakdown, Dependencies, Done When. Same pattern as epic but lighter.(Summary, Goals, Done When, Relationships). (Decision: yes, add during M5.)

> [!question] ~~Should methodology templates (wiki/config/templates/methodology/) be accessible via the scaffolder, and if so, with what syntax? Recommendat~~
> **RESOLVED:** Yes. `pipeline scaffold methodology/requirements-spec "Title"`. Already partially implemented.ion: `pipeline scaffold methodology/requirements-spec "Title"` — the `/` in the type triggers the methodology subdirectory lookup. (Decision: yes, implement during M5.)

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- IMPLEMENTS: [[E003-artifact-type-system|Artifact Type System]] (E003)
- BUILDS ON: [[e003-artifact-type-system-requirements|E003 Artifact Type System — Requirements Spec]]
- BUILDS ON: [[methodology-standards-initiative-infrastructure|Methodology Standards Initiative — Infrastructure Analysis]]
- RELATES TO: [[methodology-framework|Methodology Framework]]
- RELATES TO: [[task-type-artifact-matrix|Task Type Artifact Matrix]]
- FEEDS INTO: [[E004-portable-methodology-engine|Portable Methodology Engine]] (E004)
- FEEDS INTO: [[E005-agent-compliance-framework|Agent Compliance Framework]] (E005)

## Backlinks

[[E003-artifact-type-system|Artifact Type System]]
[[e003-artifact-type-system-requirements|E003 Artifact Type System — Requirements Spec]]
[[methodology-standards-initiative-infrastructure|Methodology Standards Initiative — Infrastructure Analysis]]
[[methodology-framework|Methodology Framework]]
[[task-type-artifact-matrix|Task Type Artifact Matrix]]
[[E004-portable-methodology-engine|Portable Methodology Engine]]
[[E005-agent-compliance-framework|Agent Compliance Framework]]
