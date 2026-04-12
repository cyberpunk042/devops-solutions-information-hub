---
title: "Methodology Config Architecture — How the Pieces Fit Together"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: methodology-yaml
    type: file
    file: config/methodology.yaml
  - id: artifact-types-yaml
    type: file
    file: config/artifact-types.yaml
  - id: wiki-schema-yaml
    type: file
    file: config/wiki-schema.yaml
  - id: quality-standards-yaml
    type: file
    file: config/quality-standards.yaml
  - id: taxonomy
    type: wiki
    file: wiki/domains/cross-domain/methodology-artifact-taxonomy.md
tags: [methodology, config, architecture, flexible-model, wiki-config, reasoning]
---

# Methodology Config Architecture — How the Pieces Fit Together

## Summary

A reasoning document examining how the wiki's config files, the methodology system, and the LLM wiki knowledge layer work together as a flexible model. The key insight: configs model what tooling CAN ENFORCE, wiki pages document what humans and agents NEED TO UNDERSTAND, and domain profiles ADAPT the generic system to specific tech stacks. This separation is correct. The issue is depth and connection between layers, not the architecture itself.

## Key Insights

1. **The config stack is correctly layered — the problem is connection depth, not structure.** wiki-schema.yaml (structure) → artifact-types.yaml (enrichment) → methodology.yaml (execution) → domain-profiles (adaptation) → quality-standards.yaml (linting). Each layer has a clear responsibility. The gaps are in how they reference each other, not in what they do.

2. **Configs model what tooling can CHECK. Wiki documents what humans need to UNDERSTAND.** validate.py can check frontmatter fields and section presence. It CANNOT check if TypeScript has business logic or if a requirements spec is binding enough. So configs define the CHECKABLE parts (structure, thresholds, styling). Wiki pages define the UNDERSTANDING parts (what good looks like, when to use each type, domain variations).

3. **The 78-type taxonomy doesn't need to be in configs — but the 3-class distinction does.** Of the 78 artifact types, only ~17 are wiki pages (checkable by our tooling). The other ~61 are code files, test results, deployment packages, etc. — checked by domain-specific gate commands (pnpm tsgo, terraform validate). The configs correctly model wiki types deeply and non-wiki types as generic stage artifact categories. But the 3-class distinction (artifact/document/documentation) SHOULD appear in configs because it drives different quality rules.

4. **"Flexible model" means: configs are configurable, wiki documents all possibilities, projects activate subsets.** Adding a new artifact type = add to configs + create wiki documentation. No code changes. Adding a new domain = create a domain profile. No config schema changes. Adding a new model = add to methodology.yaml models section. This is IaC for methodology — human writes config, machine reads it as binding.

## Deep Analysis

### The 6-Layer Config Stack

> [!info] How the layers resolve
>
> ```
> Layer 1: wiki-schema.yaml
>   ↓ defines page types, required fields, required sections
>   ↓ tools/validate.py reads this for structural validation
>
> Layer 2: artifact-types.yaml
>   ↓ extends Layer 1 with: categories, thresholds, styling, verification
>   ↓ tools/validate.py reads this optionally for enhanced checking
>
> Layer 3: methodology.yaml
>   ↓ defines 9 models with stage sequences + artifact chains
>   ↓ CLAUDE.md references this for agent stage-gate rules
>   ↓ skills read this for per-stage artifact requirements
>
> Layer 4: domain-profiles/*.yaml
>   ↓ resolves generic artifact categories to concrete paths + gate commands
>   ↓ projects select their profile (TypeScript, Python/Wiki, Infrastructure)
>
> Layer 5: quality-standards.yaml
>   ↓ defines linting thresholds, export readiness, duplicate detection
>   ↓ tools/lint.py reads this
>
> Layer 6: config/templates/
>   ↓ 22 templates (16 wiki types + 6 methodology documents)
>   ↓ tools/pipeline.py scaffold reads these
> ```
>
> **Resolution order for "what does THIS artifact look like in THIS domain?":**
> methodology.yaml (which model, which stage) → artifact-types.yaml (which type, which thresholds) → domain-profile (which paths, which gates) → template (which structure)

### What Each Layer CAN and CANNOT Do

> [!abstract] Layer Capabilities
>
> | Layer | Can Enforce | Cannot Enforce |
> |-------|-----------|---------------|
> | **wiki-schema** | Field presence, enum values, section existence | Content quality, semantic correctness |
> | **artifact-types** | Word counts, relationship counts, callout presence, derived_from | Evidence quality, insight depth, mechanism explanation |
> | **methodology** | Stage sequence, model selection, allowed/forbidden per stage | Whether agent ACTUALLY followed the stage vs just claiming to |
> | **domain-profiles** | Path patterns, gate commands, forbidden zones | Whether gate commands are the RIGHT ones for the project |
> | **quality-standards** | Thresholds, staleness, similarity | Whether a page is genuinely useful vs technically valid |
> | **templates** | Section structure, frontmatter defaults | Content quality within sections |

### What's Currently CORRECT in the Architecture

> [!success] The architecture IS right — these things work
>
> 1. **Separation of concerns:** Each config has ONE job. No overlap, no contradiction.
> 2. **Extensibility:** Add a type = add to yaml. Add a model = add to yaml. Add a domain = add a profile file. No code changes.
> 3. **Wiki pages as knowledge:** The taxonomy, standards, guides, chains — these are UNDERSTANDING that humans and agents read. They don't need to be in configs because configs can't enforce understanding.
> 4. **Domain profiles as adaptation:** The same methodology model produces TypeScript types in one domain and Terraform variables in another. The profile resolves this without changing the model.
> 5. **Templates as scaffolding:** `pipeline scaffold <type> <title>` creates the right structure instantly. The template IS the scaffold stage for wiki pages.

### What's Currently MISSING or WEAK

> [!warning] Gaps in the current config architecture
>
> | Gap | Impact | Fix Approach |
> |-----|--------|-------------|
> | **No 3-class distinction in configs** | A requirements spec (document) gets the same validation as a concept page (documentation). But documents need stricter checks (are FR items testable? do AC map to Done When?). | Add `artifact_class: document | artifact | documentation` to artifact-types.yaml per type |
> | **methodology.yaml chains don't reference templates** | Stage says "produce wiki-page" but doesn't say "use methodology/requirements-spec.md template." Agent must figure out which template fits. | Add `template_hint` to chain artifact entries |
> | **Domain profiles are thin** | 3 profiles exist but each is ~60 lines. The TypeScript profile should reference OpenArms's 24-artifact chain as the detailed instance. | Deepen profiles with concrete examples, link to domain chain wiki pages |
> | **quality-standards.yaml is too simple** | 20 lines. No per-type thresholds (those moved to artifact-types.yaml). Export readiness is basic. | May merge into artifact-types.yaml or keep as linting-specific thresholds |
> | **No compliance checking** | methodology.yaml defines models but nothing checks if the agent FOLLOWED the model. Stage sequence compliance, artifact chain completeness, readiness accuracy — all unchecked. | Future tooling: tools/compliance.py reading methodology.yaml + git log |

### How the Wiki Knowledge Layer Complements Configs

> [!tip] Configs enforce. Wiki explains. Both are needed.
>
> | What agents/humans need | Where they find it |
> |------------------------|--------------------|
> | "What page type should I use?" | artifact-types.yaml categories + wiki-schema.yaml enums |
> | "What sections does this type need?" | wiki-schema.yaml required_sections + template |
> | "What does GOOD look like for this type?" | wiki/spine/standards/{type}-page-standards.md |
> | "What model should I use for this task?" | methodology.yaml model_selection |
> | "What artifacts do I produce at this stage?" | methodology.yaml chains + domain-profile resolution |
> | "What are ALL the artifact types that exist?" | [[Methodology Artifact Taxonomy]] (78 types, 11 categories) |
> | "How does this work for MY domain?" | [[Artifact Chain: TypeScript/Node Domain]] (or Python/Wiki, Infrastructure, Knowledge) |
> | "What are the structural patterns that help agents comply?" | [[CLAUDE.md Structural Patterns for Agent Compliance]] |
> | "What went wrong when methodology was ignored?" | [[Methodology Standards — What Good Execution Looks Like]] anti-pattern gallery |
>
> The configs answer STRUCTURAL questions (what type? what sections? what gate?). The wiki answers UNDERSTANDING questions (what does good look like? when should I use this? what went wrong before?). Neither can replace the other.

### The Flexible Model in Practice

> [!abstract] How projects adopt at different levels
>
> | Adoption Level | What They Configure | What They Read |
> |---------------|-------------------|---------------|
> | **Minimal (Tier 1)** | Nothing — just read wiki pages | Model: Methodology, Standards pages, Taxonomy |
> | **Configured (Tier 2)** | Copy methodology.yaml, select domain profile, update CLAUDE.md | Same + per-domain chain page |
> | **Validating (Tier 3)** | Add artifact-types.yaml, extend validation pipeline | Same + per-type standards docs |
> | **Enforcing (Tier 4)** | Add hooks, stage skills, harness | Same + compliance patterns, enforcement hooks |
>
> Each tier ADDS config complexity without REMOVING what was there. A Tier 4 project still has Tier 1's wiki pages as knowledge. The configs get deeper; the knowledge stays the same. This is the "flexible model" — the same methodology system works at every adoption depth because the configs are layered, not monolithic.

### What Would Break the Architecture

> [!warning] Anti-patterns that would damage the flexible model
>
> 1. **Putting wiki knowledge INTO configs** — if artifact-types.yaml tried to contain the full 78-type taxonomy with descriptions, examples, and quality bars, it would be 5,000+ lines and unmaintainable. Configs contain CHECKABLE rules. Wiki contains UNDERSTANDING.
> 2. **Making configs domain-specific** — if methodology.yaml contained TypeScript-specific artifact types (it currently does in the chain section — this is a known gap), then Python and Infrastructure projects can't use it. Domain specifics go in domain-profiles ONLY.
> 3. **Removing the wiki knowledge layer** — if someone said "just use the configs, the wiki is redundant," agents would have rules without understanding. They'd know WHAT to produce but not WHY or WHAT GOOD LOOKS LIKE. The 75% violation rate in OpenArms was from agents that had configs but no understanding.
> 4. **Making the system rigid** — requiring ALL 78 types for ALL projects. The flexible model means: the taxonomy DEFINES all possibilities, each project SELECTS what applies. Adding required-everywhere types kills adoption.

## Open Questions

> [!question] Should artifact_class (document/artifact/documentation) be added to artifact-types.yaml? This would enable class-specific validation rules. (Recommendation: yes — small change, high value.)

> [!question] Should methodology.yaml chain entries include template_hint to guide which template to use? (Recommendation: yes — reduces agent guessing about which template fits the stage.)

## Relationships

- BUILDS ON: [[Methodology Artifact Taxonomy]]
- BUILDS ON: [[Three Classes of Methodology Output]]
- BUILDS ON: [[Coverage Blindness — Modeling Only What You Know]]
- RELATES TO: [[Model: Methodology]]
- RELATES TO: [[Methodology Framework]]
- RELATES TO: [[Methodology System Map]]
- RELATES TO: [[Methodology Adoption Guide]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Methodology Artifact Taxonomy]]
[[Three Classes of Methodology Output]]
[[Coverage Blindness — Modeling Only What You Know]]
[[Model: Methodology]]
[[Methodology Framework]]
[[Methodology System Map]]
[[Methodology Adoption Guide]]
[[Methodology Standards — What Good Execution Looks Like]]
[[How AI Agents Consume the Methodology Wiki]]
