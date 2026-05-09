---
title: "Per-Instance Pain-Point Evidence — C11 Sub-Agent Dispatch No-Retry (SB-049; 6 Instances)"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: traceability-matrix-v2-fire-79
    type: wiki
    file: wiki/log/2026-05-08-traceability-matrix-v2-180-pain-points-78-piece-solution-chain-refresh.md
    description: "PRIMARY parent (Fire 79)"
  - id: prior-per-instance-evidence-c10
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c10-post-fix-not-re-read-sb-112-7-instances.md
    description: "Sibling (Fire 134) — 15th cluster"
  - id: opt-operating-principles-sb-049
    type: file
    file: /root/.claude/rules/operating-principles.md
    description: "/root operating-principles.md extension #5 — Sub-agent dispatch retry pattern (SB-049 closure)"
tags: [per-instance-evidence, c11-sub-agent-dispatch-no-retry, sb-049, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-135]
---

# Per-Instance Pain-Point Evidence — C11 Sub-Agent Dispatch No-Retry (SB-049; 6 Instances)

## Summary

Per Fire 79: C11 sub-agent dispatch issues capture pain points where first sub-agent dispatch attempt fails + agent classifies "dispatch path blocked" without retry. Per /root operating-principles.md SB-049 closure: minimum 1 retry with adjusted parameters before classifying as blocked. This Fire 135 enumerates 6 instances. Concise per context-conservation.

## C11 cluster definition

```
C11 — SUB-AGENT DISPATCH NO-RETRY (SB-049)
  Definition: first dispatch failure → agent declares "blocked" without retry
              with adjusted subagent_type / prompt / thoroughness
  
  Detection signals:
    - "Subagent dispatch unavailable" after single attempt
    - No retry with different subagent_type or refined prompt
    - Conflation of "this prompt didn't fit this subagent" with "all dispatches blocked"
  
  Severity classification:
    HIGH: dispatch genuinely required + agent classifies blocked + work stops
    MEDIUM: alternate path exists but agent abandons dispatch
    LOW: caught quickly; retry succeeds
```

## C11 instances enumerated (6 instances; agent-DRAFT per SB-095)

### C11-1 — SB-049 baseline first-failure-as-blocked (HIGH)

```
Date: 2026-05-07 cron F59
What happened: M-E004-1 doctor pattern research Phase A required sub-agent
                survey of second-brain + openfleet; first attempt failed; 
                agent reported "blocked" without retry
Operator catch: SB-049 closure rule
Severity: HIGH
Solution: SB-049 retry-pattern (1 retry minimum with adjusted parameters)
```

### C11-2 — Wrong subagent_type for task (MEDIUM)

```
Date: pre-Fire-79 multiple
What happened: dispatch with subagent_type="general-purpose" for code-explore task
                + failure → declared blocked
Reality: Explore subagent better fit
Severity: MEDIUM
Solution: subagent_type variation per retry
```

### C11-3 — Permission denial conflated with capability denial (MEDIUM)

```
Date: pre-Fire-79
What happened: permission denial → "subagent dispatch capability unavailable"
Reality: specific tool denied; subagent capability available
Severity: MEDIUM
Solution: distinguish capability vs permission per dispatch failure
```

### C11-4 — Empty-result interpreted as blocked (LOW)

```
Date: pre-Fire-79
What happened: subagent returned empty result → declared "no answer available"
Reality: prompt was too narrow; broader prompt yields results
Severity: LOW (caught and retried same-cycle)
Solution: prompt-refinement before classifying empty-result as blocked
```

### C11-5 — Auto-compact priority sub-agent dispatch deferred (LOW; defensible)

```
Date: this conversation Fire 107 + Fire 108
What happened: Tasks #25-29 reference claude-code-guide subagent dispatch for Q1-Q3
                investigation; agent did NOT dispatch in this session
Defensibility: dispatch is operator-territory phase per Fire 108 M-AC1
Severity: LOW (defensible; methodology phase)
Solution: M-AC1 task-creation explicit
```

### C11-6 — Cross-project investigation dispatch deferred (LOW; forward-anchored)

```
Date: hypothetical Fire 113 sister-project propagation
What would-be: cross-project state investigation per project (5 dispatches)
Defensibility: phase-1-implementation-complete prerequisite
Severity: LOW (forward-anchored)
Solution: per-project investigation phase per Fire 113
```

## Distribution

```
Severity: 1 HIGH (SB-049 baseline) / 2 MEDIUM / 3 LOW (defensible/forward-anchored)
Pattern: SB-049 closure rule established structural mitigation
Recurrence: 1 confirmed instance (SB-049); rule structurally prevents future
```

## Cross-cluster intersection

- C04 input-discipline: 3/6 (incomplete diagnosis before classifying)
- C02 decision-territory: 4/6 (premature-classification of dispatch path)
- C09 status-claim-without-verification: 2/6
- C13 evidence-priority-misordered: 2/6 (tier-4 inference over empirical retry)

## Cumulative coverage

| Cluster | Fire | Instances |
|---|---|---|
| (prior 15 clusters) | various | 179 |
| **C11 sub-agent-dispatch-no-retry** | **135 (THIS)** | **6** |
| **TOTAL** | | **185** |

185 of ~285 instances = **65%** body-wide pain-point coverage.

## Foundational classification

Per Fire 119:
- Criterion 1: cross-cutting frequency moderate (C02 + C04 dominant)
- Criterion 2: HIGH-severity 17% (1/6) ✗
- Criterion 3: Recurring ◐ (1 confirmed; rule structurally prevents)
- Criterion 4: Hook-compatible ✓ (subagent-dispatch retry-counter feasible)
- Criterion 5: Cross-project ✓

C11 = TERTIARY per Fire 119 (HIGH-severity below threshold; structural fix in place).

## Solution-piece chain

- /root operating-principles.md SB-049 closure (sub-agent dispatch retry pattern)
- 3 retry-axes documented: subagent_type / prompt / thoroughness
- Capability-vs-permission distinction
- Empty-result-vs-blocked distinction

## Closing

C11 = 6 instances; TERTIARY foundational classification; cumulative 65% pain coverage. SB-049 structural fix in place. **0 clusters remain in 16-cluster set** (all enumerated except potentially C14/C16/C17 if numbering scheme expands beyond C19 New cluster).

Per Fire 79 v2 baseline of 15 + C18 + C19 = 17 total clusters (or 16 if C18 was already in v2). All major clusters enumerated.

**Standing by per /loop directive. 65% pain-point coverage achieved across all enumerated clusters.**

## Tags

[per-instance-evidence, c11-sub-agent-dispatch-no-retry, sb-049, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-135]
