---
title: "Decision: Per-Role Command Design Decisions"
type: decision
domain: ai-agents
layer: 6
status: synthesized
confidence: medium
maturity: growing
derived_from:
  - "Per-Role Command Architecture"
  - "Claude Code Skills"
  - "Hooks Lifecycle Architecture"
reversibility: easy
created: 2026-04-10
updated: 2026-04-10
sources:
  - id: src-shanraisshan-claude-code-best-practice
    type: documentation
    url: "https://github.com/shanraisshan/claude-code-best-practice"
    title: "shanraisshan/claude-code-best-practice"
tags: [commands, roles, slash-commands, skills, hooks, versioning, scope, design-decisions]
---

# Decision: Per-Role Command Design Decisions

## Summary

Five open questions from the Per-Role Command Architecture page resolved by cross-referencing Claude Code's scope mechanics, the skills architecture, and the hooks lifecycle. The answers establish: project scope overrides personal scope for same-named commands, commands should declare skill dependencies in frontmatter, role granularity should be flat with tags (not hierarchical), and mode-aware behavior is achieved via hooks reading session state — not separate command variants.

> [!success] Resolved decisions
>
> | Question | Decision | Confidence |
> |----------|----------|------------|
> | Scope collision (personal vs project) | Project overrides personal (same as CLAUDE.md hierarchy) | High — matches Claude Code's documented scope precedence |
> | Command-to-skill dependencies | Declare in frontmatter `requires: [skill-name]` | Medium — convention, not yet enforced |
> | Command versioning | Semver in frontmatter `version: 1.0.0`, breaking changes bump major | Medium — no ecosystem enforcement yet |
> | Mode-aware behavior | Hooks read session mode; commands don't branch internally | High — Plannotator pattern validates this |
> | Role granularity | Flat with tags `roles: [developer, frontend]`, not hierarchical | Medium — simplest model, revisit if fails |

## Decision

**Project scope overrides personal scope.** When `~/.claude/commands/review.md` and `.claude/commands/review.md` both exist, the project-level command wins. This matches Claude Code's documented hierarchy: project settings override user settings. The personal command still exists but is shadowed in that project context.

**Commands declare skill dependencies in frontmatter.** A `/review` command that requires the `evolve` skill adds `requires: [evolve]` to its frontmatter. This is currently a convention — Claude Code doesn't enforce it — but it makes the dependency explicit for both humans and future tooling.

**Flat roles with tags, not hierarchical.** `roles: [developer, frontend]` is a tag on command frontmatter, not a role tree. A frontend developer sees commands tagged with `developer` OR `frontend`. This avoids the complexity of role inheritance while providing sufficient filtering. If a project needs sub-role specificity, it adds more tags — no schema change required.

**Mode-aware behavior via hooks, not command branching.** A command doesn't check which mode is active. Instead, hooks enforce mode constraints: in `document-only` mode, a PreToolUse hook blocks `Write`/`Edit` calls to `src/`. The command runs the same way; the hook changes what's permitted. This is the Plannotator pattern: command sets context, hook provides structural enforcement.

## Alternatives

### Alternative: Hierarchical roles (developer → frontend → react)

> [!warning] Rejected — complexity exceeds the problem
> A role hierarchy requires inheritance rules, conflict resolution between parent and child roles, and a schema that every project must adopt. The ecosystem has 4 projects with 3-4 practitioner types each. Flat tags handle this. Hierarchical roles are premature optimization for a problem that doesn't yet exist at the ecosystem's current scale.

### Alternative: Separate command variants per mode

> [!warning] Rejected — violates separation of concerns
> Having `/review-autonomous` and `/review-guided` duplicates the command for every mode. The Hooks Lifecycle Architecture page documents that PreToolUse is the correct enforcement surface for runtime constraints — mode enforcement belongs in hooks, not in commands. Commands define WHAT to do; hooks define WHAT'S ALLOWED.

## Rationale

The decisions follow a consistent principle: **commands stay simple, hooks enforce constraints, skills carry knowledge.** This three-layer separation (command → skill → hook) is already the pattern documented in the Per-Role Command Architecture page and validated by the Plannotator pattern. Each decision applies this principle to a specific question:

- Scope collision → resolved by Claude Code's existing precedence system (no new mechanism needed)
- Dependencies → frontmatter convention (lightweight, no enforcement infrastructure)
- Versioning → semver in frontmatter (matches npm/pip conventions the ecosystem already uses)
- Mode awareness → hooks (existing infrastructure, PreToolUse already supports this)
- Role granularity → tags (simplest model that solves the actual problem)

Cross-referencing the Skills Architecture Patterns comparison: the SKILL.md convergence across 3 ecosystems happened without a central authority. The per-role command design follows the same principle — convention-driven interoperability over enforced standards.

## Reversibility

All decisions are easy to reverse:
- Scope precedence is a Claude Code platform behavior — if it changes, we adapt
- Frontmatter conventions can be changed without breaking existing commands
- Flat-to-hierarchical role migration adds fields without removing any
- Hook-based mode enforcement can be replaced with command-internal branching if hooks prove insufficient

## Dependencies

- [[Per-Role Command Architecture]] — these decisions complete the open questions
- [[Hooks Lifecycle Architecture]] — mode enforcement relies on PreToolUse mechanics
- [[Claude Code Skills]] — command-to-skill dependency model
- [[Claude Code Best Practices]] — scope hierarchy documentation

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[Principle: Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[Principle: Infrastructure Over Instructions for Process Enforcement]] |
> | **What is my identity profile?** | [[Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit?** | [[Methodology System Map]] |

## Relationships

- DERIVED FROM: [[Per-Role Command Architecture]]
- BUILDS ON: [[Hooks Lifecycle Architecture]]
- BUILDS ON: [[Claude Code Skills]]
- RELATES TO: [[Claude Code Best Practices]]
- RELATES TO: [[Plannotator — Interactive Plan & Code Review for AI Agents]]

## Backlinks

[[Per-Role Command Architecture]]
[[Hooks Lifecycle Architecture]]
[[Claude Code Skills]]
[[Claude Code Best Practices]]
[[Plannotator — Interactive Plan & Code Review for AI Agents]]
