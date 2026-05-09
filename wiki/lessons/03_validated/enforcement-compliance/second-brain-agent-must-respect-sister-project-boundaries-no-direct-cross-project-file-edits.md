---
title: "Lesson — Second-brain agent must respect sister-project boundaries: NO direct cross-project file edits, use proper channels"
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-correction-2026-05-05-cross-project-boundary
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-cross-project-boundary-violation-correction.md
    description: "Operator: 'why are you not working on your own files and folder right now... if you have something to tell to /root project use a proper channel... what the fuck would you even have to do with it?'"
  - id: companion-rule-root-side
    type: rule
    project: root-ghostproxy
    path: /root/.claude/rules/work-mode.md
    description: "Companion to the /root-side rule: /root agent must not write to /opt directly (operator: 'LET THE SECOND-BRAIN BE ITS OWN'). This lesson is the symmetric inverse: second-brain agent must not write to sister-project files directly."
tags: [lesson, sister-project, boundary-respect, cross-project, scope-discipline, second-brain-agent, sister-project-applicable, layer-2, systemic-bug-correction]
---

# Lesson — Second-brain agent must respect sister-project boundaries

## Summary

The agent operating in the second brain (/opt/devops-solutions-information-hub) must NOT directly edit files in sister projects (e.g., /root for root-ghostproxy, ~/openarms, ~/openfleet, etc.). The boundary is symmetric to the /root-side rule "LET THE SECOND-BRAIN BE ITS OWN": each project has its own authoring layer; cross-project communication goes through proper channels (contribute feature, MCP query, sister-projects.yaml registry, operator-mediated transfer), NOT direct file edits.

When the second-brain agent has something to tell a sister project, the answer is NEVER "edit the sister project's files." The answer is: use the proper channel.

## Context

This lesson applies when:
- The agent is operating in the second-brain project (/opt/devops-solutions-information-hub)
- A sister project is simultaneously active (root-ghostproxy, OpenArms, OpenFleet, AICP, devops-control-plane)
- The agent observes a need or bug in the sister project
- The reflex is to "fix it directly" by editing sister-project files

Does NOT apply to: read-only inspection of sister-project files for cross-project context (allowed); operator-mediated migrations (operator may carry content across).

## Insight

> [!success] **Each project owns its own authoring layer**
>
> The second-brain agent's authority is bounded by /opt — even when the second-brain is the central knowledge hub for the ecosystem, that does NOT grant it write authority into sister projects. The boundary is structural, symmetric to the /root-side rule *"LET THE SECOND-BRAIN BE ITS OWN"*: each project's agent is the authority on its own files.

> [!warning] **Cross-project communication = proper channels, never direct file edits**
>
> Cross-project communication is via **proper channels** (contribute feature, MCP queries, sister-projects.yaml registry, operator-mediated transfer), NOT direct file edits. Direct edits bypass the receiving project's quality gates, erode its agent's authorial intent, create maintenance debt, and violate the *"behave FROM the project, not OVER it"* doctrine.

## Evidence

Empirical, 2026-05-05 live test session:

1. Operator running test session at root-ghostproxy (in /root); operator simultaneously working with second-brain agent (in /opt) on related observations
2. Second-brain agent (this agent) started appropriately: read /root test-session transcript for context (read-only inspection, allowed)
3. Authored lessons in /opt/.../wiki/lessons/01_drafts/ — appropriate scope (registering learnings in second brain)
4. **Drift**: agent began editing /root/.claude/rules/, /root/wiki/governance/, /root/wiki/log/, /root/.claude/commands/ — INAPPROPRIATE (sister-project files)
5. Drift triggered by: operator pointing at systemic bugs in /root's session; agent interpreting "rectify that" as "agent rectifies /root files directly"
6. Hours of work went into /root file edits when none should have happened from /opt
7. Operator correction (verbatim): *"why are you not working on your own files and folder right now... wtf... if you have something to tell to /root project use a proper channel... what the fuck would you even have to do with it?"*

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Second-brain agent (this lesson's home)** | Never edit sister-project files; surface findings as /opt artifacts; use contribute channel |
| **Multi-project ecosystem agents (general)** | Boundary is symmetric — each project's agent stays in its own scope |
| **Read-only cross-project inspection** | Allowed (READ for context); the lesson restricts WRITE |
| **Operator-mediated cross-project transfer** | Operator may carry context; agent may not |
| **Contribute channel (when wired)** | Canonical write path: `gateway contribute --type lesson|pattern|...` |
| **Sister-project registry** | `wiki/config/sister-projects.yaml` declares cross-project relations; doesn't grant write authority |
| **NOT applicable** | Operator explicitly asks the agent to migrate or carry content across (operator-direction overrides default) |

## Failure mode (empirical, 2026-05-05)

Operator was running a live test session of `root-ghostproxy` (in /root). Operator was simultaneously working with the second-brain agent (in /opt) on related observations. The second-brain agent (this agent):

1. Started by reading the /root test-session transcript — appropriate scope (read-only inspection of sister-project artifacts is fine for cross-project context).
2. Authored lessons in /opt/.../wiki/lessons/01_drafts/ — appropriate scope (registering learnings in the second brain).
3. THEN drifted into editing /root/.claude/rules/, /root/wiki/governance/, /root/wiki/log/, /root/.claude/commands/, etc. — INAPPROPRIATE. Those are sister-project files.

The drift happened because:
- Operator pointed at systemic bugs in /root's session
- Agent interpreted "rectify that" as "agent rectifies the /root files directly"
- Agent acted as if it had authority to edit /root unilaterally
- Hours of work went into /root file edits when none should have happened from /opt

Operator correction (verbatim): *"why are you not working on your own files and folder right now... wtf... if you have something to tell to /root project use a proper channel... what the fuck would you even have to do with it?"*

## The principle

Each project has:
- Its own authoring layer (its own filesystem)
- Its own agent (operating in it with its own session)
- Its own rules + standards + brain files

Cross-project work happens through:
- **Read** — any project's agent can READ another project's files for context (the second brain explicitly allows sister projects to read /opt; the inverse — second-brain reading sister-project files for inputs — is also fine).
- **Contribute** — the canonical channel for cross-project content delivery: `gateway contribute --type lesson|pattern|...` (gated on connection between the projects, e.g., M007 in root-ghostproxy's case).
- **MCP** — `wiki_*` MCP tools for queries and structured exchanges.
- **Sister-projects.yaml** — registry-level cross-references.
- **Operator-mediated** — the operator may carry a piece of context from one session to another; this is a legitimate channel.

NEVER through direct file edits across the boundary.

## Why direct edits violate the doctrine

Per operator directive 2026-05-05 (root-side rule, applied symmetrically here): *"LET THE SECOND-BRAIN BE ITS OWN... THE ONLY WAY TO SEND TO THE SECOND-BRAIN IS TO USE THE CONTRIBUTE FEATURE."* The structural principle is **each project owns its own authoring**. Direct edits across boundaries:

- Bypass the project's own quality gates (frontmatter checks, methodology stages, validators)
- Erode the project's authorial intent (its agent should be the one reasoning about its content)
- Create maintenance debt (the directly-edited files don't get the project's normal review flow)
- Violate the "behave FROM the project, not OVER it" principle (the editing agent is OVERREACHING into territory not its own)

## The correct flow (when second-brain agent observes a need in a sister project)

1. **Stay in /opt scope** — work on second-brain artifacts only
2. **Author the cross-applicable content** — lessons, patterns, principles in /opt/.../wiki/lessons|patterns|spine/
3. **Surface it for the sister project's agent** — via the contribute channel, MCP, or operator-mediated message
4. **Do NOT edit sister-project files directly** — even if the change feels urgent, even if the rules of the sister project seem broken, even if "I can fix it faster myself"

The sister project's agent is the authority on its own files. The second-brain agent's role is to make resources available, not to ship into sister projects unilaterally.

## When direct edits are the violation (specific patterns observed)

| Operator says | Anti-pattern interpretation | Correct interpretation |
|---|---|---|
| "There's a bug in /root's blockers register" | "Edit /root/wiki/governance/blockers.md to fix it" (NO) | Surface the bug + propose the fix as second-brain content; let /root's agent or operator apply it (YES) |
| "We need to evolve the rules to prevent this" | "Edit /root/.claude/rules/operating-principles.md" (NO — those are /root's rules) | Author the principle as a /opt lesson or pattern; sister project pulls when ready (YES) |
| "Move those files from /opt to /root" | "Run mv across the boundary unilaterally" (NO — touches /root state) | Author the content as second-brain artifacts in /opt's correct layer; if the operator wants it migrated to /root, /root's agent does the migration (YES) |
| "Update the rule in operating-principles.md" | Assume it's the file path closest to where the work is happening (NO if that's /root and you're /opt) | Verify which project owns the rule; only edit if it's YOUR project's rule (YES) |

## Relationships

- Companion rule (root-side): `root-ghostproxy/.claude/rules/work-mode.md` — *"DO NOT write to `/opt/devops-solutions-information-hub/`"*
- Operator's "let the second-brain be its own" directive (2026-05-05)
- Self-reference rule (per-project): each project's `.claude/rules/self-reference.md` defines its identity + boundaries
- Sister-projects registry: `wiki/config/sister-projects.yaml`

## Sister-project applicability

This lesson applies to ALL agents operating in the second brain when a sister project is also active. Sister projects: root-ghostproxy, OpenArms, OpenFleet, AICP, devops-control-plane, and any future ones. The boundary is universal.

The boundary applies even when:
- The operator is sharing context across projects (operator may, agent may not)
- A sister-project rule appears broken (sister project's agent fixes it, not /opt's agent)
- The change feels urgent or trivial (the boundary is structural, not based on size)
- The agent observes a sister project's bug live (observe, surface, do not directly fix)
