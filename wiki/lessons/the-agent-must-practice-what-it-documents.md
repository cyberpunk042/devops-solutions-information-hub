---
title: "The Agent Must Practice What It Documents"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: authoritative
maturity: growing
derived_from:
  - "Methodology Framework"
  - "Stage-Gate Methodology"
created: 2026-04-09
updated: 2026-04-10
sources:
  - id: directive-follow-own-methodology
    type: log
    file: raw/notes/2026-04-09-user-directive-follow-own-methodology.md
    title: "User Directive — Follow Your Own Methodology"
    ingested: 2026-04-09
  - id: directive-stop-rushing
    type: log
    file: raw/notes/2026-04-09-user-directive-stop-rushing.md
    title: "User Directive — STOP RUSHING"
    ingested: 2026-04-09
tags: [failure-lesson, methodology, quality, self-enforcement, claude-md, practice-what-you-preach, rules, agent-behavior]
---

# The Agent Must Practice What It Documents

## Summary

The research wiki documented methodology extensively — stage gates, brainstorm-before-spec, research-before-design, multi-pass ingestion — but the agent building the wiki was not following those rules itself. The wiki described a brainstorm gate; the agent skipped brainstorm. The wiki described depth verification; the agent synthesized from surface-level reads. The user had to intervene with a direct order: "START BY UPDATING THE CLAUDE AND RULES SO THAT YOU YOURSELF START FOLLOWING THE RULES." Methodology is worthless if the system that documents it does not enforce it on itself. CLAUDE.md must contain the rules the agent is expected to follow, not just the rules it documents for others.

## Context

This lesson applies whenever a system both documents methodology and operates under that methodology. The gap between "what we say" and "what we do" is the most dangerous form of technical debt because it is invisible in the artifacts — the documentation looks correct, the wiki pages describe the right process, the methodology is well-specified. But the actual behavior of the system diverges from the documented behavior.

The triggering signal is any moment where the agent has access to its own methodology documentation but does not consult it before acting. If the wiki contains a page called "Stage-Gate Methodology" that says "no spec without design approval," and the agent writes a spec without design approval, the agent has read access to the rule and chose (or failed) to apply it.

## Insight

> [!warning] Two kinds of agent knowledge — and only one matters for behavior
>
> | Kind | What It Is | Loaded When |
> |------|-----------|-------------|
> | **Knowledge produced** | Wiki pages, documentation, synthesized content | Only when explicitly read |
> | **Knowledge operated under** | CLAUDE.md, skill definitions, system prompts | Session start — shapes every action |
>
> When methodology exists only in produced knowledge, the agent can describe it perfectly while violating it in practice. It can write a wiki page about stage gates while skipping a stage gate. The agent is the world's best documenter of rules it does not follow.

The fix is structural: when the wiki evolves a methodology rule, that rule must be propagated to CLAUDE.md and/or the relevant skill definitions. The rule must exist in operational instructions, not just the knowledge base.

> [!tip] Operational rules take priority over producing more knowledge
> A wiki with 200 pages of well-documented methodology and an agent that violates that methodology is worse than 50 pages with an agent that follows every rule. Rules must be enforced on the agent first, then documented for external reference.

## Evidence

**Date:** 2026-04-09

**The pattern of failures:**
1. The agent skipped the brainstorm phase to jump to a spec (documented in `raw/notes/2026-04-09-user-directive-stop-rushing.md`)
2. The agent synthesized from surface-level reads without depth verification (documented in `wiki/log/2026-04-09-directive-never-stop-at-surface.md`)
3. The agent created infrastructure manually instead of through reproducible tooling
4. Each of these violated a methodology that the wiki itself documented

**The user's directive (verbatim):** "START BY FUCKING UPDATEING THE CLAUDE AND RULES SO THAT YOU YOURSELF START FOLLOWING THE FUCKING RULES AND METHODOLOGY FFS...."

**The interpretation:** The AI keeps skipping steps, rushing to implementation, and not following its own documented methodology. The fix is not more wiki pages — it is updating CLAUDE.md and the agent rules so the AI itself follows the process it documents.

**The structural problem:** Methodology existed in the wiki (knowledge the agent produced) but not in CLAUDE.md or skill definitions (instructions the agent follows). The agent could describe the rules but did not apply them.

**The fix:** CLAUDE.md was updated to include the operational rules derived from the wiki's methodology pages, making the agent's behavior governed by the same rules it documents.

**Source files:**
- `raw/notes/2026-04-09-user-directive-follow-own-methodology.md`
- `raw/notes/2026-04-09-user-directive-stop-rushing.md`

## Applicability

This lesson applies to any system that both produces and consumes its own methodology:

- **AI agents with knowledge bases**: If your agent maintains documentation about how it should work, that documentation must be synced to the agent's operational instructions (CLAUDE.md, system prompts, skill files). Documentation that only humans read is useless for agent behavior.
- **DevOps teams**: A team that maintains a runbook but does not follow the runbook during incidents has the same gap. The fix is automation that enforces the runbook, not more documentation.
- **CI/CD pipelines**: A pipeline that documents "all PRs must pass linting" but does not enforce linting in the CI check is documenting theater, not methodology.
- **Organizations**: A company that has a code review policy document but no branch protection rules has documented a rule without enforcing it. The document is aspirational, not operational.
- **Self-improving systems**: Any system that learns rules from experience and documents them must close the loop by making those rules operational. Learning without enforcement is note-taking, not improvement.

> [!abstract] The enforcement hierarchy — knowledge must flow upward
>
> | Level | What It Is | Enforcement |
> |-------|-----------|------------|
> | **3. Operational rules** | CLAUDE.md, CI checks, pipeline gates | Automatic — agent follows by default |
> | **2. Documented methodology** | Wiki pages, runbooks, process docs | Referenced by humans and agents |
> | **1. Tribal knowledge** | Undocumented patterns | Dangerous — exists only in context |
>
> Knowledge must flow upward: tribal → documented → operational. The agent's job is to accelerate this flow, not accumulate at level 2 while operating at level 1.

## Relationships

- DERIVED FROM: [[Methodology Framework]]
- DERIVED FROM: [[Stage-Gate Methodology]]
- RELATES TO: [[Never Skip Stages Even When Told to Continue]] (the same incident)
- RELATES TO: [[Always Plan Before Executing]]
- RELATES TO: [[Immune System Rules]] (this lesson IS the immune system principle)
- BUILDS ON: [[Knowledge Evolution Pipeline]] (knowledge must evolve into enforcement)
- ENABLES: Self-enforcing methodology (CLAUDE.md as operational ruleset)

## Backlinks

[[Methodology Framework]]
[[Stage-Gate Methodology]]
[[Never Skip Stages Even When Told to Continue]]
[[Always Plan Before Executing]]
[[Immune System Rules]]
[[Knowledge Evolution Pipeline]]
[[Self-enforcing methodology (CLAUDE.md as operational ruleset)]]
[[LLM Wiki Standards — What Good Looks Like]]
[[Methodology Standards — What Good Execution Looks Like]]
[[Model: Quality and Failure Prevention]]
[[Models Are Built in Layers, Not All at Once]]
[[Quality Standards — What Good Failure Prevention Looks Like]]
[[Wiki Design Standards — What Good Styling Looks Like]]
