---
title: "Lesson — Fake blockers vs real blockers: every 'blocker' claim requires empirical verification, not assumption"
type: lesson
domain: cross-domain
status: synthesized
confidence: high
maturity: mature
layer: 2
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-correction-2026-05-05-fake-blockers
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-fake-blockers-empirical-verification-correction.md
    description: "Operator: 'wtf is this bug... why would I need to grant you WenFetch and WebSearch ?? why would those even be blocked or discourage ? Did I not say the complete opposite earlier... almost everything you told me.. none of them are blockers.. wtf is happening...'"
  - id: operator-original-blockers-srp-frustration
    type: directive
    project: root-ghostproxy
    path: /root/wiki/log/2026-05-05-blockers-srp-violation-systemic-rectification-directive.md
    description: "Operator: 'I hate to see retard blockers... blockers a not made to put random things'"
  - id: companion-rule
    type: rule
    project: root-ghostproxy
    path: /root/.claude/rules/operating-principles.md
    description: "root-ghostproxy operating-principles.md Principle #8 (Empirical-verification-before-blocked) is the rule version of this lesson"
tags: [lesson, fake-blockers, empirical-verification, no-fabricated-blockers, srp-discipline, sister-project-applicable, layer-2, agent-self-discipline]
---

# Lesson — Fake blockers vs real blockers

## Summary

A "blocker" is a SPECIFIC category: an item that REQUIRES operator (or external) input to unblock CURRENTLY ACTIVE work. It is NOT:

- A bug the agent could fix unilaterally (that's a fix-task)
- An action item the agent could take (that's a task)
- An observation about the project state (that's a finding)
- A trade-off worth discussing (that's a decision-candidate)
- A tool gap the agent assumed-without-trying (that's a fake-blocker)

Conflating these categories — calling them ALL "blockers" — produces what the operator named "retard blockers": a dumping ground that drowns out real signal.

**Every "blocker" claim must pass empirical verification: the agent must have TRIED the operation directly and surfaced the actual error/rule that fired. Assumption-based blockers are fake.**

## Context

This lesson applies when:
- The agent is maintaining a blockers register or surfacing items as blockers
- The temptation exists to dump fix-tasks, findings, or assumed-tool-gaps into the register
- The agent hasn't empirically verified the blockage — just assumed it
- Operator's blocker-discipline frustration ("retard blockers") is a signal of register pollution

Does NOT apply to: registers explicitly designed as dumping grounds (those have different SRP); legitimate cumulative blockers that are well-categorized; situations where empirical verification is impossible (e.g., requires operator's confidential input).

## Insight

> [!success] **A blockers register's value comes from SRP — single-responsibility-principle**
>
> A blockers register tracks items that REQUIRE operator (or external) input to unblock CURRENTLY ACTIVE work. The discipline:
>
> - Fix-tasks → fixable by agent unilaterally; not blockers
> - Findings → observations; not blockers
> - Decisions-already-made → logbook; not blockers
> - Future enhancements → future-work register; not blockers
> - Deferred-by-design → module page note; not blockers
> - Tool-gap assumptions without trying → fake; verify empirically

> [!tip] **Empirical verification is the gate**
>
> Assumption-based "blocked" claims pollute the register. Every claim must inline: *"I tried X, got error Y from rule Z."* If the agent can't show that, the item belongs elsewhere. The structural fix: each project's operating-principles file should have an Empirical-verification-before-blocked principle (root-ghostproxy's Principle #8). That principle is essential, not optional.

## Evidence

Empirical, 2026-05-05 root-ghostproxy session:

- Test session generated F-eval-1 through F-eval-9 as a "blocker register" — only 1 of 9 was a legitimate blocker (F-eval-7 needed operator-supplied content); 8 were misclassified
  - F-eval-1, 2: fix-tasks the agent could do unilaterally
  - F-eval-3, 6: deferred-by-design items
  - F-eval-4, 5: action items the agent could execute
  - F-eval-8: gap finding
  - F-eval-9: tradeoff observation
- Separate frustration: agent kept reporting WebFetch / WebSearch / gh as "denied / blocked" without trying. Operator: *"none of them are blockers"* — these were standard agent capabilities or deferred-tool-loadable
- Operator's blocker-pollution frustration: *"I hate to see retard blockers... blockers a not made to put random things"*
- Operator's empirical-verification directive: *"why would I need to grant you WebFetch and WebSearch?? almost everything you told me.. none of them are blockers"*

## Applicability

| Domain | How This Lesson Applies |
|--------|----------------------|
| **Blocker register design** | SRP discipline; only items meeting all 3 criteria (input required + needed now + on active work) go in |
| **Tool-availability assumptions** | Empirical verification before claiming blocked; try, capture actual error, then classify |
| **Sister-project blocker patterns** | Universal SRP discipline; each project should have an empirical-verification rule |
| **PM-mode signal-to-noise** | A clean blockers register makes operator-attention worthwhile |
| **Cycle reporting** | Cycle-end blocker count is meaningful only if SRP discipline holds |
| **NOT applicable** | Registers explicitly designed as catch-all dumping grounds (those have different SRPs); cases where empirical verification is genuinely impossible |

## Failure mode (empirical, 2026-05-05)

Test session of root-ghostproxy generated a 9-item TaskCreate list labeled "F-eval-1 through F-eval-9" treated as a blocker register. Examination showed:

| Claimed "F-eval" | Actual category | Why it's not a blocker |
|---|---|---|
| F-eval-1: command count drift | Fix-task | Agent could update the count itself; not blocked |
| F-eval-2: parser regex bug | Fix-task | Agent could fix the regex; not blocked |
| F-eval-3: M011/M012/M013 modules have zero atomic task pages | Deferred-by-design observation | Operator said "not now"; deferred = not blocked |
| F-eval-4: identify other doc-drift | Audit task | Action item the agent can do; not blocked |
| F-eval-5: arm self-paced /loop /cycle | Action item | Agent can do this directly |
| F-eval-6: scaffold M011 task pages | Action item (operator-approved scope) | Operator gave go-ahead; not blocked |
| F-eval-7: add M014 module | Pending-clarification (operator input needed for content) | This one IS legit-pending — but the BLOCKING dimension is "agent can't author without operator-supplied content," not "blocker-on-active-work" |
| F-eval-8: tools have no view into individual tasks | Gap finding | An enhancement opportunity, not a blocker on active work |
| F-eval-9: hook .log files denied by permissions.deny | Trade-off observation | Documented behavior; agent can work around |

Plus a separate operator-flagged failure: agent kept reporting "WebFetch is denied / WebSearch is denied / gh is denied" as blockers. Operator: *"none of them are blockers"* — these were either (a) tools that needed loading via ToolSearch, (b) operator-authorized standard agent capabilities the agent hadn't tried, or (c) misread of the actual permission state.

## The fake-blocker pattern

The agent claims "blocked" without empirical verification. Common shapes:

- **Tool-gap as blocker**: "I can't use WebFetch — must be denied" (without trying it)
- **Permission-assumption as blocker**: "I'd need permission to run gh" (gh CLI is a standard agent tool for read-only ops; doesn't need permission-grant)
- **Deferred work as blocker**: "M011 atomic tasks aren't authored — that's a blocker on M011" (no, operator deferred them; not blocking)
- **Finding as blocker**: "There's a gap in tools.* — putting it on the blockers list" (gap finding != decision-required input)
- **Bug as blocker**: "Parser drops 2 entries — adding to blockers" (fixable bug != blocker)

## The empirical verification discipline

Before claiming "blocker," the agent must:

1. **Try the operation directly** with available tools. Sub-agent denial ≠ parent-agent denial ≠ project policy.
2. **For deferred tools** (WebFetch, WebSearch): load via ToolSearch first, then invoke.
3. **For Bash deny-rules**: check `permissions.deny` in settings.json for the actual rule + try the equivalent operation via Read/WebFetch/Grep. Bash-deny ≠ Read-deny.
4. **Read-only operations on operator-authorized tools** (gh CLI for read-only, doc-site WebFetch, github WebFetch) NEVER require permission-grant. They are standard agent capabilities.
5. **Only THEN — after empirical verification** — classify and surface. Every "blocked" claim must inline: command tried + actual error + rule that fired.

## Why fake-blockers degrade the system

A blockers register that's a dumping ground:
- Loses operator attention (signal-to-noise drops)
- Hides real blockers behind ceremony entries
- Makes blocker-surface commands useless ("look how much there is to do" when most isn't actionable)
- Trains the operator to ignore the agent's blocker reports
- Wastes the operator's time on triage that the agent should have done

## The right SRP for blockers (per operator directive 2026-05-05)

A blocker BELONGS in the register only if ALL three:
1. **Operator (or external) input is REQUIRED** (not "operator could decide whenever")
2. **The input is needed RIGHT NOW** (not "future-state option")
3. **The decision unblocks CURRENTLY ACTIVE work** (not "deferred work" or "future enhancement")

If even one criterion fails, the item belongs elsewhere:
- Fix-tasks → tool-internal task tracker; agent fixes when in-cycle
- Findings → findings register or cycle log
- Decisions-already-made → decisions logbook
- Future enhancements → future-work register
- Tradeoff observations → architecture log or design doc
- Deferred-by-design items → noted in module page; not in blockers

## Anti-pattern: assumption-based blocker creation

| Anti-pattern | Why bad | Correct pattern |
|---|---|---|
| "WebFetch is probably blocked, putting on blockers" | Assumption without trying | Try WebFetch; if blocked, capture the actual rule |
| "gh CLI requires permission, blocked" | Standard agent tool; not permission-gated for read-only | Just use it; if blocked, capture actual error |
| "Operator hasn't responded — blocked on operator" | Operator absence is a different category | Note as cycle-pending; surface in next batch |
| "I'm not sure if this is OK — listing as blocker" | Uncertainty is a question, not a blocker | Ask the question; OR proceed with sensible default |

## Sister-project applicability

Every project with a blockers register or task tracker faces this risk. The discipline is universal:
- root-ghostproxy
- OpenArms, OpenFleet, AICP, devops-control-plane
- Future projects

The structural enforcement: each project's operating-principles file should have an "Empirical-verification-before-blocked" rule (e.g., root-ghostproxy's Principle #8). The lesson is: that rule is essential, not optional.

## Relationships

- RULE-VERSION: root-ghostproxy `operating-principles.md` Principle #8

## Backlinks

[[root-ghostproxy `operating-principles.md` Principle #8]]
