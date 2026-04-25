---
title: "Boilerplate skill anti-pattern at scale: 47% of AICP's 78 skills are identical instruction dumps"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: medium
maturity: growing
derived_from:
  - "Model — Skills, Commands, and Hooks"
  - "Extension Standards — What Good Skills, Commands, and Hooks Look Like"
  - "Schema aspirationalism — defining required sections you never validate produces false confidence"
created: 2026-04-17
updated: 2026-04-22
sources: []
tags: [contributed, inbox]
contributed_by: "aicp-self"
contribution_source: "/home/jfortin/devops-expert-local-ai"
contribution_date: 2026-04-17
contribution_status: accepted
review_note: \"Accepted 2026-04-22 during pickup-cold session — structural review (derived_from wired, claim coherent, evidence sourced). Promoted to contributor's tier ceiling (01_drafts) per contribution-policy.yaml harness-trusted tier.\"
contribution_reason: "Extension Standards has Open Question 'Should skills have a validation schema?' AICP just provided concrete evidence that skill libraries at scale (78 skills) decay to 47% boilerplate without validation — a quantitative argument for the schema."
---

# Boilerplate skill anti-pattern at scale: 47% of AICP's 78 skills are identical instruction dumps

## Summary

AICP's .claude/skills/ inventory contains 78 skills. Audit against Extension Standards (model-skills-commands-hooks-standards.md) shows 37/78 (47%) share the IDENTICAL generic Process boilerplate, and 0/78 satisfy ANY of the 5 required structural elements (trigger phrases, named operations, quality bar, gotchas, multiple ops). The boilerplate is verbatim:

'1. Read the project context: architecture, current state, relevant code
 2. Analyze what needs to be done for this specific operation
 3. Plan the changes with the user
 4. Execute: create/modify files, run commands as needed
 5. Verify: tests pass, no regressions, output is correct
 6. Update project state (.aicp/state.yaml) with what was accomplished'

EVIDENCE:

1. Quantitative — grep over .claude/skills/*/SKILL.md: 78 total skills; 37 have the boilerplate Process section verbatim; 0 have Trigger/Quality/Gotchas headings; 0 have multiple named Operations sections. Affected skills: config-deploy, config-env, config-feature-flags, config-migrations, config-secrets, evolve-api-version through evolve-scale (6 skills), feature-document through feature-test (6 skills), infra-api through infra-storage (8 skills), quality-accessibility through quality-performance (6 skills), refactor-architecture through refactor-split (6 skills).

2. Anti-pattern match — Extension Standards lines ~85-90 explicitly name this: 'A skill that is a wall of text... No trigger phrases — the agent doesn't know WHEN to load it. No operations — the agent doesn't know WHAT it does. No quality bar — the agent doesn't know WHEN it's done.'

3. Worst case — 37 different skill NAMES point to the SAME instructions. An agent loading 'quality-coverage' gets the same Process as 'feature-implement'. The skill name is a lie about its specificity.

4. Consumer impact — fleet's config/agent-tooling.yaml references 18 of these skills as required for agent operation. Fleet agents are loading boilerplate while expecting domain-specific guidance.

MECHANISM:

The boilerplate likely came from a generation script that scaffolded N skills from one template without filling in skill-specific content. The naming convention (verb-noun like 'config-deploy', 'evolve-migrate') suggests these were programmatically created. Without rewriting, every additional 'verb-noun' skill increases the dilution: skill names multiply but operational variety doesn't.

APPLICABILITY:

- Any project that scaffolded N skills from one template — audit immediately, do not assume scaffolded skills are functional.
- Any consumer (fleet, harness, MCP client) loading these skills — they're getting noise where they expect signal.
- Any project considering skill libraries at scale — must validate skill-specific content, not just skill count.

WHEN THE AUDIT METHOD DOES NOT FIT:

- Projects with <10 skills — manual review per skill is faster than grep heuristics.
- Projects whose skill template intentionally inherits a base process — the boilerplate may be by design (then exemplar skills should still customize). Even then: the 0/78 trigger/quality/gotchas score is a real gap.

DELIVERABLE:

Audit document at AICP wiki/decisions/00_inbox/skills-audit-2026-04-17.md with phased rewrite plan: Phase 1 (this audit, immediate); Phase 2 (rewrite 18 fleet-referenced skills, weeks); Phase 3 (rewrite remaining 19 boilerplate skills as called for, months); Phase 4 (skill validation schema in tools/lint.py when count of properly-authored skills exceeds 50).

## Context

> [!warning] When does this lesson apply?
>
> - You have or are designing a skill library with >20 skills generated from a shared scaffold
> - [[model-skills-commands-hooks-standards|Extension Standards]] defines 5 required structural elements (trigger phrases, named operations, quality bar, gotchas, multiple ops) and you haven't audited compliance
> - Consumers (fleet, harness, MCP client) reference a subset of your skills as required — skill quality is their signal source
> - Skills are named with a regular pattern (verb-noun like `config-deploy`, `evolve-migrate`) suggesting programmatic generation

## Insight

> [!tip] The scaling failure mode of scaffolded skill libraries
>
> Boilerplate dilution is a predictable failure mode when N skills are generated from one template without per-skill customization. The skill NAME differentiates but the BODY does not — consumers loading `quality-coverage` receive the same Process text as consumers loading `feature-implement`. **The name becomes a lie about the skill's specificity.**
>
> The quantitative signature:
>
> | Metric | AICP Evidence | Healthy threshold |
> |--------|---------------|-------------------|
> | Identical boilerplate across skills | **37/78 (47%)** | <5% (one-of-many shared-base case) |
> | Skills with trigger phrases | **0/78** | >80% (agent needs to know WHEN to load) |
> | Skills with named operations | **0/78** | >80% (agent needs to know WHAT it does) |
> | Skills with quality bar | **0/78** | >80% (agent needs to know WHEN it's done) |
> | Skills with gotchas | **0/78** | >60% (hard-won knowledge, rarely-documented) |
> | Consumer-required skills passing all 5 | **0/18 (fleet-referenced)** | 100% |
>
> **Why 0/78 instead of partial adoption**: a generated scaffold either produces the required structural elements or it doesn't. If it doesn't, NONE of the generated skills have them. The number is always 0 or N — never fractional — until manual rewrites begin.

## Evidence

> [!abstract] Quantitative audit (AICP, 2026-04-17)
>
> **The identical boilerplate** (verbatim across 37/78 skills):
>
> ```
> 1. Read the project context: architecture, current state, relevant code
> 2. Analyze what needs to be done for this specific operation
> 3. Plan the changes with the user
> 4. Execute: create/modify files, run commands as needed
> 5. Verify: tests pass, no regressions, output is correct
> 6. Update project state (.aicp/state.yaml) with what was accomplished
> ```
>
> **Affected skill families** (AICP `.claude/skills/*/SKILL.md`):
>
> | Family | Affected / Total | Notes |
> |--------|-----------------|-------|
> | config-* | 5 | config-deploy, config-env, config-feature-flags, config-migrations, config-secrets |
> | evolve-* | 6 | evolve-api-version through evolve-scale |
> | feature-* | 6 | feature-document through feature-test |
> | infra-* | 8 | infra-api through infra-storage |
> | quality-* | 6 | quality-accessibility through quality-performance |
> | refactor-* | 6 | refactor-architecture through refactor-split |
>
> **Anti-pattern match — Extension Standards lines ~85-90 explicitly name this**: *"A skill that is a wall of text... No trigger phrases — the agent doesn't know WHEN to load it. No operations — the agent doesn't know WHAT it does. No quality bar — the agent doesn't know WHEN it's done."*
>
> **Consumer impact**: OpenFleet's `config/agent-tooling.yaml` references 18 of these boilerplate skills as required for agent operation. Fleet agents load these expecting domain-specific guidance; they get identical generic Process text. This propagates to Principle 4 territory: the skill library DECLARES coverage that operations don't VERIFY.

## Applicability

> [!abstract] Applies when
>
> - Any project that scaffolded N skills from one template — audit immediately, do not assume scaffolded skills are functional
> - Any consumer (fleet, harness, MCP client) loading these skills — they're getting noise where they expect signal
> - Any project considering skill libraries at scale — must validate skill-specific content, not just skill count
> - **Extension Standards open question — does skill library need a validation schema?** — AICP's evidence argues YES. A schema lint would block the generated-boilerplate pattern at authoring time.
>
> Does NOT apply when
>
> - Projects with <10 skills — manual review per skill is faster than grep heuristics
> - Projects whose skill template intentionally inherits a base process — boilerplate may be by design. Even then: the 0/N trigger/quality/gotchas score remains a real gap
>
> Contributed from /home/jfortin/devops-expert-local-ai. Applicability assessed during promotion review.

## Deliverable (AICP's Phased Rewrite Plan)

> [!info] AICP's response — 4-phase rewrite
>
> | Phase | Scope | Timeline |
> |-------|-------|----------|
> | 1. Audit | This document + inventory (complete) | Immediate |
> | 2. Rewrite fleet-referenced | 18 fleet-referenced skills rewritten per Extension Standards | Weeks |
> | 3. Rewrite remaining boilerplate | Remaining 19 boilerplate skills as called for | Months |
> | 4. Schema enforcement | Skill validation schema in `tools/lint.py` once >50 skills are properly authored | Post-Phase-3 |
>
> AICP's own audit document: `wiki/decisions/00_inbox/skills-audit-2026-04-17.md` (AICP-internal).

## Relationships

- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- RELATES TO: [[model-skills-commands-hooks-standards|Extension Standards]] (the standards page whose Open Question this evidence addresses)
- RELATES TO: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Aspirational Until Verified]] (skill library declares coverage; operations don't verify)
- RELATES TO: [[profile-as-coordination-bundle|Profile as Coordination Bundle]] (skill selection is per-task; profile selection is per-deployment — both are per-context-config patterns, different scope)
- RELATES TO: [[model-registry|Model Registry]]

## Backlinks

[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[Extension Standards]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Aspirational Until Verified]]
[[profile-as-coordination-bundle|Profile as Coordination Bundle]]
[[model-registry|Model Registry]]
