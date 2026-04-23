---
title: "Artifact Path Verification at Gate Close"
aliases:
  - "Artifact Path Verification at Gate Close"
  - "Verify Declared Artifacts Exist"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: medium
maturity: growing
instances:
  - page: "OpenArms verify-done-when.cjs (2026-04-16)"
    context: "Extended the Done When verifier with an artifact-existence check: for every path declared in task frontmatter's `artifacts:` list, the verifier now runs `fs.existsSync()` before allowing `readiness=100`. Commit `b4ed8349`. Addresses the 'readiness lies' class where agents mark tasks complete without producing the declared outputs."
  - page: "Research Wiki validation gate"
    context: "Pipeline post validates wiki page frontmatter, but does NOT check backlog task `artifacts:` list against filesystem. Gap: an agent could declare `artifacts: [wiki/domains/foo.md]` in task frontmatter without creating the file; validation passes. Candidate infrastructure addition."
derived_from:
  - "Infrastructure Over Instructions for Process Enforcement"
  - "Agent Failure Taxonomy — Seven Classes of Behavioral Failure"
  - "Aspirational Naming in Lifecycle Code"
created: 2026-04-16
updated: 2026-04-22
sources:
  - id: openarms-integration-notes
    type: file
    project: openarms
    path: wiki/log/2026-04-16-second-brain-integration-notes.md
    description: "Parts 17 and 20 — identified that 'readiness is computed, not self-reported' requires verifier to check artifact paths against filesystem"
  - id: openarms-verify-done-when
    type: file
    project: openarms
    path: scripts/methodology/verify-done-when.cjs
    description: "The implementation commit b4ed8349 that wired artifact-path verification into the Done When gate"
tags: [pattern, enforcement, gate-close, artifacts, readiness, verification, infrastructure, openarms]
---

# Artifact Path Verification at Gate Close

## Summary

At the moment a task gate closes (`/stage-complete`, `/task-done`, readiness advancing to 100), the harness must verify that every file path declared in `frontmatter.artifacts` actually exists on disk. Without this check, an agent can declare artifacts it never produced, and the readiness field becomes fiction — a "readiness lie" invisible to any subsequent computation. The check is trivial (a loop of `fs.existsSync()` calls), the cost is microseconds, and the prevention is categorical: you cannot close a gate on a phantom file. This pattern is a close cousin of Write Guard but fires at a different moment — Write Guard blocks wrong-scope writes during stage work; Artifact Path Verification blocks wrong-claims about writes at stage end.

## Pattern Description

The pattern's structural components:

1. **Frontmatter carries artifact declarations.** Task files include `artifacts: [path1, path2, ...]` listing files the task produces. These declarations are authoritative claims.

2. **Gate close reads the declarations.** `/stage-complete`, `/task-done`, or the harness's readiness-computation step reads the artifact list before advancing.

3. **Each declared path is checked against the filesystem.** `fs.existsSync()` (or platform equivalent). Missing path = the claim is false.

4. **Gate close fails when any declared path is absent.** The task does not advance. The agent is told which paths are missing. The agent must produce the files or correct the declaration.

**Why this matters:** the readiness field is computed from `stages_completed` and artifact verification. If the verifier skips the filesystem check, readiness computation treats frontmatter claims as ground truth. An agent that declared `artifacts: [...]` without producing the files advances through stages, and the lie propagates up the hierarchy (epic readiness = average(child readiness) = inflated).

**Why the check lives at gate close, not at write time:** write-time check is a separate pattern (Post-Write tracker) that logs all actual writes. Gate-close check compares DECLARED artifacts against either filesystem OR write log. Both are valuable; this pattern specifically addresses the gate-close question: "does the agent's declaration match reality?"

### The Three Failure Modes This Pattern Prevents

> [!warning] Three distinct failures, all eliminated by path verification
>
> | Failure | Without verification | With verification |
> |---|---|---|
> | **Phantom files** | Agent declares `src/auth/oauth.ts` in artifacts; file doesn't exist. Task closes with readiness=100. | Gate close fails listing missing path. |
> | **Reverted files** | Agent created `src/auth/oauth.ts`, hit errors, reverted, declared as artifact anyway. | Gate close fails — reverted file doesn't exist on disk anymore. |
> | **Typo/rename** | Agent declared `src/auth/oath.ts` (typo); actual file is `src/auth/oauth.ts`. Task closes pointing at the wrong path. | Gate close fails exact-path check. Agent must fix declaration or rename file. |

## Instances

> [!example]- Instance 1: OpenArms verify-done-when.cjs (commit b4ed8349, 2026-04-16)
>
> **Before:** The `verify-done-when.cjs` validator checked that each Done When item had a passing command (introduced in T088 `command_passes` check) but did not verify declared `artifacts:` existed on disk.
>
> **After:** Added artifact-existence check before allowing `readiness=100` assignment. Implementation shape:
>
> ```javascript
> // verify-done-when.cjs (simplified)
> const frontmatter = parseTaskFrontmatter(taskPath);
> const declaredArtifacts = frontmatter.artifacts || [];
>
> const missing = declaredArtifacts.filter(a => !fs.existsSync(path.resolve(repoRoot, a)));
>
> if (missing.length > 0) {
>   console.error(`BLOCKED: Task declares ${declaredArtifacts.length} artifact(s) but ${missing.length} are missing from disk:`);
>   missing.forEach(a => console.error(`  - ${a}`));
>   process.exit(1);
> }
> ```
>
> **Same commit** also added `progress=100` assignment at task completion (Rule 4 of [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]) and a progress-cap-at-100 bug fix (progress could exceed 100 when stages_completed > model's required stages).
>
> **Observed effect:** tasks that would have silently advanced with phantom artifacts now block at the gate. The agent's next action is either to produce the file or to remove the incorrect declaration. Either way, the frontmatter tells the truth by the time the gate closes.

> [!example]- Instance 2: Research Wiki (gap — not yet implemented)
>
> The wiki's `pipeline post` chain validates page frontmatter, wikilinks, and lint. It does NOT check backlog task `artifacts:` list against filesystem. An agent working on a wiki task could declare `artifacts: [wiki/domains/foo.md]` without creating the file and the pipeline would pass.
>
> **Risk:** small today (operator-supervised, solo mode) but real. Would grow with automation. Pattern adoption estimate: ~30 lines of Python added to `tools/validate.py` that reads task frontmatter and checks filesystem.

## When To Apply

- **When your task frontmatter includes `artifacts:` (or equivalent)** — no declaration means nothing to verify
- **When you have gate-close automation** — `/stage-complete`, `/task-done`, or a validator that advances readiness to 100
- **When you observe "readiness lies"** — completed tasks whose declared outputs don't exist, discovered via post-run audit
- **When you have ≥1 run where artifacts were declared without production** — the pattern addresses a real failure you've seen

## When Not To

- When your project doesn't declare artifacts in frontmatter (nothing to verify)
- When the agent is human-supervised in real-time (the human is the verifier — don't duplicate)
- When artifact paths are dynamic (templated, parameterized) and the validator can't resolve them — either make paths static or solve the resolution first
- When the cost of a false-positive block (valid artifact misread as missing) is higher than the cost of a false-negative claim (phantom artifact accepted) — rare, but possible in exploratory research

## Self-Check

> [!warning] Before adopting, confirm:
>
> 1. Does your task frontmatter include declared artifacts?
> 2. Does your gate-close automation advance readiness based on those declarations?
> 3. Have you observed ≥1 task where the declared artifact didn't exist?
> 4. Would a missing-path message be actionable for the agent (can it produce the file or correct the declaration)?
>
> If 1=yes, 2=yes, 3=yes, 4=yes: adopt. Implementation is typically ~20-50 lines in the gate validator.

## Structural Properties

| Property | Description |
|---|---|
| **Cost** | Very low — microseconds per check, ~30 lines of code to implement |
| **Coverage** | Narrow — catches phantom/reverted/typo artifacts, not bad content in real files |
| **Composes with** | Post-Write tracker (log all writes) for cross-check. Stage scope guard (Pattern 2 of Enforcement Hook Patterns) for stage-appropriate writes. |
| **Reversibility** | Trivial — single `fs.existsSync` call can be wrapped in a feature flag |
| **Detection strength** | Binary — file exists or it doesn't |

## Relationship to Readiness Computation

This pattern closes a specific gap in the readiness-computed-not-claimed invariant. The invariant says: readiness is derived from stages_completed + artifacts, never manually set. But the derivation quality depends on the inputs. If `artifacts` is accepted as declared without verification, the derivation is GIGO — garbage in, garbage out. Artifact path verification makes the input verified-at-gate-close, which makes the derivation trustworthy.

## How This Connects — Navigate From Here

> [!abstract] From This Pattern → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The principle this implements** | [[infrastructure-over-instructions-for-process-enforcement\|Infrastructure > Instructions]] — verification at gate time, not trust |
> | **The failure class this addresses** | [[agent-failure-taxonomy-seven-classes-of-behavioral-failure\|Agent Failure Taxonomy]] — Class 1 (Artifact Pollution) variant |
> | **The naming pattern this avoids** | [[aspirational-naming-in-lifecycle-code\|Aspirational Naming]] — `artifacts:` field that is never verified is aspirational |
> | **The tracking model** | [[readiness-vs-progress\|Readiness vs Progress]] — readiness trust depends on artifact verification |
> | **The backlog rule** | [[backlog-hierarchy-rules\|Backlog Hierarchy Rules]] — Rules 4, 5 assume verified inputs |
> | **Composing enforcement layer** | [[enforcement-hook-patterns\|Enforcement Hook Patterns]] — Pattern 3 (Artifact Tracker) logs writes; this pattern verifies claims |

## Relationships

- DERIVED FROM: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
- DERIVED FROM: [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy]]
- BUILDS ON: [[aspirational-naming-in-lifecycle-code|Aspirational Naming in Lifecycle Code]]
- RELATES TO: [[enforcement-hook-patterns|Enforcement Hook Patterns]]
- RELATES TO: [[readiness-vs-progress|Readiness vs Progress]]
- RELATES TO: [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
- FEEDS INTO: [[model-methodology|Model — Methodology]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[Agent Failure Taxonomy]]
[[aspirational-naming-in-lifecycle-code|Aspirational Naming in Lifecycle Code]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[Readiness vs Progress]]
[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[model-methodology|Model — Methodology]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[aspirational-declaration-without-enforcement|Aspirational Declaration Produces False Confidence at Every Layer]]
