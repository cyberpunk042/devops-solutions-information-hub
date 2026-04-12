---
title: "Methodology Adoption Guide"
type: reference
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: methodology-config
    type: file
    file: config/methodology.yaml
  - id: domain-profiles
    type: file
    file: config/domain-profiles/
  - id: artifact-types
    type: file
    file: config/artifact-types.yaml
  - id: openarms-evidence
    type: file
    file: /home/jfortin/openarms/wiki/config/methodology.yaml
tags: [methodology, adoption, guide, onboarding, ecosystem]
---

# Methodology Adoption Guide

## Summary

Step-by-step guide for any project to adopt the research wiki's methodology. Covers the four adoption tiers — from reading the wiki models to running full infrastructure enforcement. Includes concrete configuration examples for TypeScript, Python/wiki, and infrastructure projects. The wiki produces the methodology; projects consume it at whatever depth matches their needs.

## Reference Content

### Adoption Tiers

> [!info] Four Tiers of Adoption
>
> | Tier | What You Get | Effort | Prerequisites |
> |------|-------------|--------|---------------|
> | **1. Read** | Read models + standards pages, follow manually | Minutes | None — just read the wiki |
> | **2. Configure** | Copy methodology.yaml + domain profile, reference in CLAUDE.md | Hours | Access to wiki config/ |
> | **3. Validate** | Add artifact-type checks to your validation pipeline | Days | Tier 2 + validation tooling |
> | **4. Enforce** | Add hooks, stage skills, deterministic dispatch | Weeks | Tier 3 + harness infrastructure |

> [!tip] Start at Tier 1, climb when you feel the pain
>
> Most projects should start by reading the models and following them manually. When agents start skipping stages or producing wrong artifacts, move to Tier 2. When you can't tell if methodology was followed, add Tier 3. When you run autonomous agents overnight, you need Tier 4.

### Tier 1: Read the Models

No configuration needed. Just read these wiki pages:

1. **Start here:** [[Model: Methodology]] — the 9 named models and when to use each
2. **Understand stages:** [[Stage-Gate Methodology]] — the 5 stages and their boundaries
3. **Know the artifacts:** [[Artifact Chains by Methodology Model]] — what each stage produces
4. **Quality tiers:** [[Skyscraper, Pyramid, and Mountain]] — choose your quality level explicitly

Then in your CLAUDE.md, add a reference:

```markdown
## Methodology

This project follows the methodology defined in the devops-solutions-research-wiki.
See: wiki/spine/model-methodology.md for models, wiki/spine/model-methodology-standards.md for quality bar.

Stage gates: Document → Design → Scaffold → Implement → Test
Never skip stages. "Continue" means advance within the current stage, not skip ahead.
```

### Tier 2: Configure

Copy the methodology config and declare your domain profile.

**Step 1: Copy the methodology config**

```bash
# From the research wiki
cp config/methodology.yaml /your-project/config/methodology.yaml
```

Or reference it directly if your project has access to the wiki repo.

**Step 2: Select your domain profile**

```bash
# Choose the profile matching your stack
cp config/domain-profiles/typescript.yaml /your-project/config/domain-profile.yaml
# or: python-wiki.yaml, infrastructure.yaml
```

**Step 3: Add project-specific overrides**

Create a project override file layered on top:

```yaml
# /your-project/config/methodology-overrides.yaml
# Extends the generic methodology.yaml with project-specific details

project: my-project
domain_profile: typescript  # or python-wiki, infrastructure

overrides:
  # Add project-specific gate commands
  stages:
    implement:
      gate_commands:
        - "pnpm tsgo"
        - "pnpm check"
        - "pnpm my-project-specific-check"

  # Restrict models if your project only needs a subset
  enabled_models:
    - feature-development
    - bug-fix
    - hotfix
    - documentation

  # Project-specific forbidden zones
  forbidden_zones:
    document: ["src/", "tests/"]
    design: ["src/", "tests/"]
```

**Step 4: Reference in CLAUDE.md**

```markdown
## Methodology

This project uses the research wiki methodology engine.
Config: config/methodology.yaml (generic) + config/methodology-overrides.yaml (project)
Domain profile: typescript

### Stage Gates (enforced)
- Document (0-25%): Wiki pages only. No src/ writes.
- Design (25-50%): Design docs only. No src/ writes.
- Scaffold (50-80%): Types and stubs only. No business logic.
- Implement (80-95%): Business logic. Must wire into existing runtime.
- Test (95-100%): Real assertions. 0 failures.

### Model Selection
- epic/module/task → feature-development (5 stages)
- bug → bug-fix (3 stages: document, implement, test)
- hotfix → hotfix (2 stages: implement, test)
- docs → documentation (1 stage: document)
```

### Tier 3: Validate

Extend your project's validation to check methodology compliance.

**Option A: Use artifact-types.yaml for per-type validation**

```bash
cp config/artifact-types.yaml /your-project/config/artifact-types.yaml
```

Then extend your validation tool to read it (see research wiki's tools/validate.py for the pattern — it reads artifact-types.yaml for content thresholds, styling requirements, and per-type frontmatter checks).

**Option B: Add stage-gate checks to CI**

```yaml
# In your CI config
methodology-check:
  script:
    - python3 scripts/check-stage-gate.py
  rules:
    - "No src/ files in document-stage commits"
    - "No test files in implement-stage commits"
    - "Scaffold commits have no function bodies >3 lines"
```

### Tier 4: Enforce

Full infrastructure enforcement — hooks, stage skills, deterministic dispatch.

> [!warning] Tier 4 Requires a Harness
>
> Infrastructure enforcement means the agent doesn't control git, task selection, or stage advancement. A harness (like OpenArms's agent-run.ts) owns the loop. This is the most effective tier (75% violation reduction) but requires the most investment.

**Components needed:**

| Component | Purpose | Example |
|-----------|---------|---------|
| Pre-bash hook | Block git commands from agent | `scripts/hooks/pre-bash.sh` |
| Pre-write hook | Block wrong-scope writes per stage | `scripts/hooks/pre-write.sh` |
| Post-write hook | Track files created per stage | `scripts/hooks/post-write.sh` |
| Stage validation script | Check artifacts before advancing | `scripts/validate-stage.cjs` |
| Task selection script | Deterministic task dispatch | `scripts/select-task.cjs` |
| Stage skills | Per-stage instructions injected into context | `.claude/skills/methodology-{stage}/` |

> [!tip] OpenArms as Reference Implementation
>
> OpenArms (v9) is the most evolved Tier 4 implementation:
> - 14 enforcement scripts in `scripts/methodology/`
> - 4 hooks in `scripts/methodology/hooks/`
> - 5 stage skills in `.claude/skills/`
> - Harness manages loop, commits, frontmatter updates
>
> Study its `wiki/config/methodology.yaml` and `AGENTS.md` for the enforcement patterns.

### Per-Domain Quick Start

> [!abstract] TypeScript Project Quick Start
>
> 1. Copy: `methodology.yaml`, `domain-profiles/typescript.yaml`, `artifact-types.yaml`
> 2. CLAUDE.md: Add stage gate rules with `pnpm tsgo` / `pnpm check` / `pnpm test` gates
> 3. Hooks (optional): pre-write blocks `src/` during document/design stages
> 4. Verify: agent produces wiki pages before code, types before logic, tests last

> [!abstract] Python/Wiki Project Quick Start
>
> 1. Copy: `methodology.yaml`, `domain-profiles/python-wiki.yaml`, `artifact-types.yaml`
> 2. CLAUDE.md: Add stage gate rules with `pipeline post` / `validate` gates
> 3. Hooks (optional): pre-write blocks `tools/` during document stage
> 4. Verify: agent reads existing pages before writing new ones, runs post-chain after changes

> [!abstract] Infrastructure Project Quick Start
>
> 1. Copy: `methodology.yaml`, `domain-profiles/infrastructure.yaml`, `artifact-types.yaml`
> 2. CLAUDE.md: Add stage gate rules with `terraform validate` / `terraform plan` gates
> 3. Hooks (optional): pre-write blocks `*.tf` during document/design stages
> 4. Verify: agent documents current infrastructure before making changes

### Invariants (All Tiers)

> [!warning] These Rules Apply at Every Tier
>
> 1. **Never skip stages** — "continue" means advance within current stage, not skip ahead
> 2. **Quality tier is explicit** — choose Skyscraper, Pyramid, or Mountain deliberately. Mountain is the anti-pattern.
> 3. **Artifacts are evidence** — stages produce verifiable deliverables, not claims
> 4. **Readiness is computed** — from stage completion, not manually claimed
> 5. **Done When items are specific** — name files, functions, endpoints. Generic boilerplate lets agents cheat.

## Relationships

- BUILDS ON: [[Model: Methodology]]
- BUILDS ON: [[Artifact Chains by Methodology Model]]
- BUILDS ON: [[Model Composition Rules]]
- RELATES TO: [[Model: Methodology Standards — What Good Looks Like]]
- RELATES TO: [[Stage-Gate Methodology]]
- RELATES TO: [[Four-Project Ecosystem]]
- FEEDS INTO: [[Model: Ecosystem]]
- FEEDS INTO: [[Super-Model: Research Wiki as Ecosystem Intelligence Hub]]

## Backlinks

[[Model: Methodology]]
[[Artifact Chains by Methodology Model]]
[[Model Composition Rules]]
[[Model: Methodology Standards — What Good Looks Like]]
[[Stage-Gate Methodology]]
[[Four-Project Ecosystem]]
[[Model: Ecosystem]]
[[Super-Model: Research Wiki as Ecosystem Intelligence Hub]]
[[CLAUDE.md Structural Patterns for Agent Compliance]]
[[Enforcement Hook Patterns]]
[[Learning Path: Methodology Fundamentals]]
[[Methodology Evolution Protocol]]
[[Methodology Framework]]
[[Methodology Standards — What Good Execution Looks Like]]
[[Methodology System Map]]
[[Stage-Aware Skill Injection]]
