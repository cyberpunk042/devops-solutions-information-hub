---
title: Decision — Extension System Operational Decisions
aliases:
  - "Decision — Extension System Operational Decisions"
  - "Decision: Extension System Operational Decisions"
type: decision
domain: ai-agents
layer: 6
status: synthesized
confidence: medium
maturity: growing
derived_from:
  - "Claude Code Skills"
  - "Hooks Lifecycle Architecture"
  - "Harness Engineering"
reversibility: easy
created: 2026-04-10
updated: 2026-04-13
sources: []
tags: [skills, hooks, versioning, composition, harness, python-hooks, design-decisions]
---

# Decision — Extension System Operational Decisions
## Summary

Four open questions about the Claude Code extension system — skill versioning, skill composition, and whether this ecosystem should implement harness-style Python hooks. Cross-referencing the Skills Architecture Patterns comparison, the Hooks Lifecycle Architecture, and the Harness Engineering guardrail rule catalog.

> [!success] Resolved decisions
>
> | Question | Decision | Confidence |
> |----------|----------|------------|
> | Skill versioning mechanism | No formal versioning yet. Convention: CHANGELOG section in SKILL.md. | Medium — ecosystem too small for semver overhead |
> | Skill-to-skill composition | Not formally supported. De facto composition via shared CLIs. Sufficient for now. | High — validated across 3 ecosystems |
> | Should this ecosystem implement R01-R04 as Python hooks? | Yes — start with R01 (block rm -rf, force push) and R04 (require review before merge). | High — highest-leverage, lowest-effort |
> | CLAUDE.md compliance threshold | Not measurable as a percentage. Compliance is binary per rule, probabilistic per session. | Medium — reframe from threshold to rule-count |

## Decision

**Skill versioning: CHANGELOG section, not semver.** At the current ecosystem scale (4 projects, ~10 skills), full semver is overhead without value. A `## Changelog` section in each SKILL.md documents what changed and when. When the ecosystem grows to 20+ skills shared across 10+ projects, revisit with package-manager-style versioning. The agentskills.io specification may provide this — wait for the ecosystem to converge rather than inventing a wiki-specific solution.

**Skill composition: shared CLIs, not formal references.** The Skills Architecture Patterns comparison confirms: "Composition (skills referencing skills) remains largely unsolved across all ecosystems." The de facto pattern — higher-level skills invoke the same CLI tools that lower-level skills use — achieves composition without formal skill-to-skill references. The wiki's own skills demonstrate this: `wiki-agent` and `evolve` both invoke `tools/pipeline.py` commands. They compose through shared tooling, not through skill-to-skill imports.

> [!tip] Start with 2 Python hooks from Harness Engineering
> R01 (block dangerous operations: `rm -rf`, `git push --force`, `git reset --hard`) and R04 (require review step completed before merge/release) are the highest-leverage, lowest-effort hooks to implement. Both are `command` handler type — a Python script that reads the tool call JSON, checks against a blocklist or state file, and returns `{"decision": "block"}` if violated. Implementation: `~/.claude/hooks/safety.py` for R01, `~/.claude/hooks/review-gate.py` for R04.

**CLAUDE.md compliance is binary per rule, not a percentage.** The question "is there a measurable compliance threshold?" is reframed: each CLAUDE.md rule is either followed or not in a given instance. Across a session, compliance is probabilistic — the model may follow 95% of rules 100% of the time and 5% of rules 60% of the time. The correct metric is not "overall compliance %" but "which specific rules have low compliance?" Those rules should graduate from CLAUDE.md (Level 0, ~60% compliance) to hooks (Level 2, ~98% compliance).

## Alternatives

### Alternative: Formal skill package manager

> [!warning] Deferred — ecosystem too small
> A skill registry with dependency resolution, version locking, and update notifications would be valuable at scale. The agentskills.io ecosystem may provide this. At 4 projects and ~10 skills, the overhead exceeds the benefit. Revisit at 20+ skills.

## Rationale

All decisions favor waiting for ecosystem convergence over building custom solutions. Skill versioning: wait for agentskills.io. Composition: the CLI-sharing pattern works. Hooks: start with the two highest-leverage rules. Compliance: reframe the question to identify which rules need stronger enforcement.

## Reversibility

All easy. CHANGELOG sections are additive. CLI-based composition doesn't preclude formal composition later. Python hooks can be added or removed per-project. Compliance metrics can be refined as data accumulates.

## Dependencies

- [[claude-code-skills|Claude Code Skills]] — resolves 2 of its open questions
- [[harness-engineering|Harness Engineering]] — resolves 2 of its open questions
- [[claude-code-best-practices|Claude Code Best Practices]] — resolves the compliance threshold question

> [!info] SDLC Chain Context
> This decision was calibrated for a 4-project ecosystem with ~10 skills and no formal skill registry. At different chain levels:
> - **Simplified chain:** Skills and hooks are unnecessary — the operator runs commands directly. CLAUDE.md compliance is the only enforcement layer, and versioning is not a concern with a single project.
> - **Full chain:** Skill versioning needs semver with automated compatibility checks across 20+ projects. Skill composition needs formal dependency graphs. All R01-R13 guardrail rules should be Python hooks with blocking enforcement, not just R01 and R04.
> See [[sdlc-customization-framework|SDLC Customization Framework]] for chain details.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What skills architecture does this reference?** | [[claude-code-skills|Claude Code Skills]] |
> | **What hooks architecture does this build on?** | [[hooks-lifecycle-architecture|Hooks Lifecycle Architecture]] |
> | **Related decision: hooks design** | [[hooks-design-decisions|Decision — Hooks Design Decisions]] |
> | **What guardrail rules apply?** | [[harness-engineering|Harness Engineering]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[claude-code-skills|Claude Code Skills]]
- DERIVED FROM: [[harness-engineering|Harness Engineering]]
- BUILDS ON: [[hooks-lifecycle-architecture|Hooks Lifecycle Architecture]]
- RELATES TO: [[claude-code-best-practices|Claude Code Best Practices]]
- RELATES TO: [[skills-architecture-patterns|Skills Architecture Patterns]]
- RELATES TO: [[hooks-design-decisions|Decision — Hooks Design Decisions]]

## Backlinks

[[claude-code-skills|Claude Code Skills]]
[[harness-engineering|Harness Engineering]]
[[hooks-lifecycle-architecture|Hooks Lifecycle Architecture]]
[[claude-code-best-practices|Claude Code Best Practices]]
[[skills-architecture-patterns|Skills Architecture Patterns]]
[[hooks-design-decisions|Decision — Hooks Design Decisions]]
