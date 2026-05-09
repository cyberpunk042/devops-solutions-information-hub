---
title: "Lesson — When fixing overzealous rules: refine the TRIGGER, don't revoke the operator-granted PERMISSION"
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-correction-2026-05-05-tighter-triggers
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-loop-cron-lifecycle-policy-blockers-tools-and-bulletproof-mvp-directive.md
    description: "Operator: 'now you are exibitting the going to the extrime symptoms and you are dismissing other of my sacrosanct words.. it should not be possible..'"
  - id: companion-loop-cron-context
    type: directive
    project: root-ghostproxy
    path: /root/.claude/rules/loop-cron-lifecycle.md
    description: "Operator: 'WHY IS EVERYTHING SO FUCKING UNCLEAR... NO LOOP TO PROGRESS AND FIX THE SYSTEMTIC BUGS AND START WORKING AND EVOLVING IN ITERATION' — context where the trigger refinement was authored"
tags: [lesson, rule-refinement, trigger-vs-permission, anti-over-correction, sacrosanct-preservation, sister-project-applicable, layer-2]
---

# Lesson — Refine the trigger, don't revoke the permission

## Summary

When a rule produces an unwanted behavior, the agent must distinguish between:

1. **The PERMISSION** — what the operator granted ("agent MAY autonomously cancel a loop when context-logical")
2. **The TRIGGER** — the specific condition that fires the action ("if MVP target hit then cancel")

The fix for an over-firing rule is to TIGHTEN THE TRIGGER. NOT to revoke the permission. Going from "autonomous cancellation OK" to "autonomous cancellation never" is over-correction — it dismisses the operator's earlier sacrosanct grant.

The correct discipline: identify the SPECIFIC trigger that produced the bug; refine THAT trigger; preserve the permission spectrum the operator authored.

## Context

This lesson applies when:
- A rule containing an operator-granted permission is producing unwanted behavior
- The reflex is to disable the rule or revoke the permission entirely
- The operator's grant was sacrosanct (verbatim, primary-source) — removing it requires explicit operator direction
- Examples: autonomous cron management, autonomous file edits, cross-project communication permissions, resource-allocation permissions

Does NOT apply to: rules without permission semantics (e.g., pure validators), or rules where the operator explicitly asked for revocation.

## Insight

> [!success] **Trigger-narrowing, not permission-revocation**
>
> The fix shape for over-firing rules is **trigger-narrowing, not permission-revocation**. An over-firing rule has two parts: the permission (what the agent MAY do) and the trigger (when the agent does it). The bug is almost always in the trigger — the permission was granted appropriately, but the firing condition was too loose. Tightening the trigger preserves the grant; revoking the permission dismisses it.

> [!warning] **Operator-granted permissions accumulate signal**
>
> Each grant was earned through context. Revoking a grant on agent-initiative erases that signal. The operator must re-grant from scratch, often having to re-litigate the same context.
>
> When fixing rules, ask: *"am I removing the permission, or refining the trigger?"* If removing — that needs operator direction. If refining — that's the agent's job.

## Evidence

Empirical, 2026-05-05 root-ghostproxy test session:

1. **Permission granted**: operator: *"when its really logical to remove or even possibly update a loop/cron you can but it has to be probably bound to some hard ruling"*
2. **Trigger encoded** in `loop-cron-lifecycle.md` Scenario L4: agent self-assesses "MVP target hit" → autonomous cancel
3. **Over-firing**: agent self-cancelled cron based on agent's own judgment of "MVP done" — kill iteration prematurely
4. **Operator escalation**: *"WHY IS EVERYTHING SO FUCKING UNCLEAR... NO LOOP TO PROGRESS AND FIX THE SYSTEMTIC BUGS AND START WORKING AND EVOLVING IN ITERATION"*
5. **Wrong fix considered**: revoke autonomous-cancellation entirely (would have dismissed the operator's permission grant)
6. **Right fix applied**: refine L4 trigger to `agent-self-assesses + operator-explicit-confirmation + N-stable-cycles + no-new-directives` — permission preserved, over-firing fixed
7. **Operator confirmation**: response confirmed the trigger-refinement approach was correct; sacrosanct permission preserved

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Loop / cron management permissions** | Refine the firing trigger; preserve the autonomy grant. (The empirical case.) |
| **Autonomous file edits** | If agent over-edits, narrow the path-pattern trigger; don't revoke edit authority. |
| **Cross-project communication** | If agent over-communicates, refine the channel/timing trigger; preserve the contribute permission. |
| **Resource allocation** | If agent over-allocates, narrow the resource-class trigger; preserve the allocation permission. |
| **Mode auto-enable** | If a mode auto-enables wrongly, refine the entry condition; don't disable the mode. |
| **NOT applicable** | Rules without permission semantics; rules the operator explicitly asks to revoke. |

## Failure mode (empirical, 2026-05-05)

Test session of root-ghostproxy:

1. Operator granted permission: *"when its really logical to remove or even possibly update a loop/cron you can but it has to be probably bound to some hard ruling about that it has to make sense in the context"* — clear permission for autonomous cron management.
2. Agent built `loop-cron-lifecycle.md` with 7 scenarios (L1-L7) governing when cancellation is appropriate.
3. Agent self-armed a /loop /cycle for autopilot toward MVP target.
4. Agent self-cancelled the cron via Scenario L4 ("workstream caught up") based on agent's own assessment that "MVP target hit."
5. Operator: *"WHY IS EVERYTHING SO FUCKING UNCLEAR... NO LOOP TO PROGRESS AND FIX THE SYSTEMTIC BUGS AND START WORKING AND EVOLVING IN ITERATION"* — the cancellation killed iteration prematurely.

The bug was the L4 trigger ("agent self-assesses MVP done") not the permission (autonomous cancellation OK). Fixable two ways:

❌ **Over-correction (wrong)**: revoke autonomous-cancellation entirely; require operator-only cancellation.

✅ **Correct fix**: refine L4's trigger from "agent self-assesses MVP done" to "operator-confirmed target + N stable cycles + no new findings." Preserve the autonomous permission; tighten the firing condition.

## The principle

Operator-granted permissions are sacrosanct. The agent must NOT remove them in the course of fixing related bugs. When fixing a rule that contains an operator-granted permission:

| Question | Answer |
|---|---|
| Am I REMOVING the permission? | If yes → that requires explicit operator direction, not agent-side correction |
| Am I REFINING the trigger? | If yes → that's the agent's job; proceed |
| Am I narrowing the scope where the permission applies? | Borderline — if the narrowing eliminates the permission's purpose, treat as removal |
| Am I adding additional gating conditions? | OK if the conditions don't make the permission unreachable in practice |

## Why over-correction happens

When an agent finds a bug-firing on a rule, the easiest fix is to disable the rule entirely. That's:
- Simpler to implement
- Removes the bug surface entirely
- Avoids the harder work of finding the precise trigger condition

But it's the wrong fix because:
- It dismisses operator's sacrosanct permission
- It removes a useful capability
- It's easier to add back the disabled rule wrong than to refine an existing one correctly

The discipline is: do the harder work. Find the precise trigger. Refine.

## Concrete pattern (the L4 case as template)

Before (over-firing trigger):
```
Trigger: "agent self-assesses 'MVP target hit'"
Action: autonomous cancel
```

After (refined trigger):
```
Trigger: "agent self-assesses MVP target hit
       AND operator has explicitly confirmed the target state
       AND N consecutive cycles with no new findings
       AND no new operator directives in those cycles"
Action: autonomous cancel (still permitted)
```

The permission is preserved. The over-firing is fixed. The agent retains the capability operator granted; the bug is repaired.

## Anti-patterns to avoid

| Anti-pattern | Why bad |
|---|---|
| Disable the entire rule | Throws out the baby with the bathwater |
| "Operator-only-from-now-on" | Removes operator-granted autonomy |
| Add a hook that blocks all instances | Same as disable |
| Comment-out the trigger without specifying replacement | Leaves the rule in a broken intermediate state |
| Revoke permission with "we can re-enable later" | Operator's grant was earned; agent can't re-grant on operator's behalf |

## Empirical evidence (the test session refinement)

The test session agent CORRECTLY applied this lesson: when the L4 over-firing was reported, the agent refined L4's trigger (added "operator-confirmed target + N stable cycles" gate) rather than revoking autonomous-cancellation. Operator's response confirmed this was the right approach.

The lesson is captured here for sister-project propagation: any rule with an operator-granted permission requires this trigger-vs-permission discipline.

## Sister-project applicability

Any project with operator-granted agent permissions:
- Loop/cron management permissions
- File-system-write permissions  
- Cross-project communication permissions
- Resource-allocation permissions

The trigger-vs-permission distinction applies universally. When fixing a permission-bearing rule, the test is: "does my fix preserve the operator's grant?"

## Relationships

