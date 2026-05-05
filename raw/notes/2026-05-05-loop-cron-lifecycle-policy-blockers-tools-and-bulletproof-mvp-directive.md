---
title: "2026-05-05 — Operator directive: loop/cron auto-management policy + lifecycle scenarios + blocker-operations tools + bulletproof MVP target"
type: note
domain: cross-domain
status: raw
confidence: high
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-loop-lifecycle-and-blocker-tools
    type: directive
tags: [note, operator-directive, sacrosanct, verbatim, loop-cron-lifecycle, auto-management, hard-ruling, mode-aware, blockers-tools, bulletproof-mvp, methodology-harnessing, second-brain-teaching]
---

# Operator directive — 2026-05-05 loop/cron lifecycle + blockers tools + bulletproof MVP

## Verbatim

> "btw when its really logical to remove or even possibly update  a loop/cron you can but it has to be probably bound to some hard ruling about that it has to make sense in the context and be relative for example to being completely blocked and not even being able to advance some WIKI LLM PM or Spec or Docs data or whatever relevant. obviously we can even add hooks to strenghtens this and it can be a voluntered opt in at the install for the hooks. obviously some loops make no sense to be cancelled as much as they might have other reason to come to and end themselves or not. I used the completely blocked example but that's just one example, we can properly evaluate and think through the scenarios and how it might vary depending on the modes too. another light example is passing from one Epic to the next or one milestone to the next or shifting from resolving blockers or from spec to work and etc... from ready_to_work on 0% to 100% or from work_progress 0 to 100 and so on. we have methodology config for this kind of stuff for example. the second-brain is supposed to teach us to use it and even augment our harnessing with it and adapt it to our needs. some even copy the whole base. (adding to the blocking or looking at it or doing operatoin on it are also the kind of things that can become highly useful tools. all those tools needs to be identified and properly developped.... (like right now there are also moment I am adding information but I do not want you to get sidetracked either. continue and also process this as it complementary and related) lets continue till this feel like a proper bulletproof MVP"

## Decomposition

### A — Loop/cron autonomous management permission (NEW)

- "when its really logical to remove or even possibly update a loop/cron you can"
- Permission granted: agent MAY autonomously stop or update a loop/cron
- BUT bound to hard ruling: must make sense in context

### B — Hard ruling required

- "it has to be probably bound to some hard ruling about that it has to make sense in the context and be relative"
- Need a documented hard rule defining when autonomous cancellation/update is appropriate
- Example given (one of many): "completely blocked and not even being able to advance some WIKI LLM PM or Spec or Docs data or whatever relevant"

### C — Hooks to strengthen

- "obviously we can even add hooks to strenghtens this"
- Hooks could enforce/validate the rule before allowing cancellation
- "voluntered opt in at the install for the hooks" — operator can opt in at install time

### D — Asymmetry: not all loops are cancellable

- "obviously some loops make no sense to be cancelled as much as they might have other reason to come to and end themselves or not"
- Some loops should NOT be cancelled by agent
- Some loops have NATURAL end conditions (self-terminating)
- Some loops have OTHER reasons to end (operator decision, time-based, etc.)

### E — Multi-scenario evaluation needed

- "I used the completely blocked example but that's just one example"
- "we can properly evaluate and think through the scenarios"
- Don't only design for "completely blocked" — many scenarios

### F — Mode-dependent

- "and how it might vary depending on the modes too"
- Different modes (PM Scrum Master / DevOps Architect / Dual Expert) may evaluate cancellation differently
- PM mode: cancel when all blockers resolved + no work in flight?
- Architect mode: cancel when current implementation milestone done?
- Dual mode: cancel when both lenses report idle?

### G — Lifecycle transitions (concrete examples)

Operator names several transitions:
- "passing from one Epic to the next" — epic completion → autopilot may pause/restart
- "or one milestone to the next" — milestone close → autopilot may transition
- "shifting from resolving blockers or from spec to work" — phase shift
- "from ready_to_work on 0% to 100%" — readiness transitions
- "from work_progress 0 to 100" — progress transitions

### H — Methodology config governs this

- "we have methodology config for this kind of stuff for example"
- The methodology engine (`/root/wiki/config/methodology.yaml`) has stage gates + transitions
- The lifecycle awareness should be sourced from methodology config, not invented

### I — Second brain teaches harnessing

- "the second-brain is supposed to teach us to use it and even augment our harnessing with it and adapt it to our needs. some even copy the whole base"
- Second brain provides methodology + teaching pattern
- Project augments via project-specific overlays
- Some projects copy the whole base (fully adopt) vs adapt selectively

### J — Tools for blocker operations (NEW)

- "(adding to the blocking or looking at it or doing operatoin on it are also the kind of things that can become highly useful tools. all those tools needs to be identified and properly developped..."
- Tool surface for blockers needs to grow:
  - **Add a blocker** — `tools.blockers add B### --title ... --priority ... --context ...`
  - **Look at a blocker** — `tools.blockers get B###`
  - **Operate on a blocker** — update status, change priority, add downstream effects, mark resolved

### K — Don't sidetrack

- "like right now there are also moment I am adding information but I do not want you to get sidetracked either. continue and also process this as it complementary and related"
- This directive is COMPLEMENTARY to the in-flight thorough review + bulletproof MVP work
- Don't lose the main thread; integrate as related extension

### L — Bulletproof MVP target

- "lets continue till this feel like a proper bulletproof MVP"
- Goal-state: bulletproof MVP

## Action plan

1. Log this directive verbatim — done (this file).
2. Author rule file `/root/.claude/rules/loop-cron-lifecycle.md` defining hard ruling for autonomous cancellation/update + scenario taxonomy + mode-dependent evaluation.
3. Extend `tools.blockers` with subcommands: `add`, `get`, `update`, `resolve` (in addition to existing list/check).
4. Author `/blocker-add`, `/blocker-update`, `/blocker-resolve` slash commands composing the tools (per "command can use tools" pattern).
5. Update mode brain pieces (pm-scrum-master, devops-architect, dual-expert) to declare per-mode loop-lifecycle scenarios — when each mode's `/cycle` autopilot would self-terminate or pause.
6. Identify remaining bulletproof-MVP gaps; capture in `blockers.md` F-items or address inline.

## No-conflate guard

- "you can" (autonomously remove/update loops) = permission, not directive — the agent USES this when context-logical, not always.
- "voluntered opt in at the install for the hooks" = future feature, NOT current directive to build.
- "all those tools needs to be identified and properly developped" = directive to identify + develop, but at MVP scope (not exhaustive).
- "this directive is complementary" = layer on top of the thorough review, don't displace it.
- "lets continue till this feel like a proper bulletproof MVP" = continue, don't declare done prematurely.
