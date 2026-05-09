---
title: "Per-Instance Pain-Point Evidence — C13 Evidence-Priority Misordered (10 Instances Verbatim-Mapped)"
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
    description: "PRIMARY parent (Fire 79) — 180 pain points across 15 clusters; C13 listed pending per-instance enumeration"
  - id: prior-per-instance-evidence-c09
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c09-status-claim-without-verification-p4-axis-12-instances-verbatim-mapped.md
    description: "Sibling (Fire 126) — most recent per-instance enumeration; 9th cluster"
  - id: opt-operating-principles-extension-5-evidence-priority-hierarchy
    type: file
    file: /root/.claude/rules/operating-principles.md
    description: "/root operating-principles.md extension #5 — Evidence-priority hierarchy (operator-empirical > diag-log > subagent-research > agent-inference); SB-109 closure"
tags: [per-instance-evidence, c13-evidence-priority-misordered, sb-109-110-cluster, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-129]
---

# Per-Instance Pain-Point Evidence — C13 Evidence-Priority Misordered (10 Instances Verbatim-Mapped)

## Summary

Per Fire 79: C13 evidence-priority-misordered captures pain points where agent trusts LOWER-priority evidence (subagent research, agent-inference) over HIGHER-priority evidence (operator-empirical, diag-log) when sources conflict. Per /root operating-principles.md extension #5 (SB-109 closure): 4-tier evidence hierarchy. This Fire 129 enumerates 10 instances. Per Fire 119 + 127 foundational-cluster set: C13 likely SECONDARY — close to foundational but C04+C02+C09 cover most-cross-cutting cases.

## C13 cluster definition

```
C13 — EVIDENCE-PRIORITY MISORDERED
  Definition: agent trusts LOWER-tier evidence over HIGHER-tier when sources conflict
  
  Tier hierarchy (per /root operating-principles.md #5):
    TIER 1 (highest): operator-empirical (direct observation, "I had it working")
    TIER 2: diag-log of real session (passive capture of actual behavior)
    TIER 3: subagent research / external docs / vendor specs
    TIER 4 (lowest): agent inference (derived models, "platform must work this way")
  
  Detection signal: agent acts on tier-3/4 evidence DESPITE tier-1 contradicting
  
  Severity classification:
    HIGH: tier-1 explicit + agent overrides → operator-trust loss
    MEDIUM: tier-1 implicit + agent doesn't seek → drift
    LOW: agent-inference accepted in absence of higher-tier
```

## C13 instances enumerated (10 instances; agent-DRAFT per SB-095)

### Instance C13-1 — Stop hook tier-3 over tier-1 (HIGH; SB-109)

```
Date: 2026-05-06
Conflict: operator-empirical "I had it working before" (tier-1) vs claude-code-guide subagent
          "Stop hook has no user-visible channel" (tier-3)
What happened: agent accepted tier-3; oscillated through 4 wrong output shapes
Operator catch: SB-109 closure rule
Severity: HIGH (12-iter cascade-shape)
Solution: SB-109 evidence-priority-hierarchy rule
```

### Instance C13-2 — Platform-limitation framing (MEDIUM; SB-110)

```
Date: 2026-05-06 stamp-bug aftermath
What happened: agent attributed render-failure to "platform behaves this way" (tier-4 inference)
Reality: actually wrong-agent-output-shape (tier-4 error not platform)
Operator catch: SB-110 closure rule
Severity: MEDIUM
Solution: tier-evidence-attribution required for "platform" claims
```

### Instance C13-3 — Mental-model verification skip (HIGH; SB-097)

```
Date: 2026-05-05 statusline cascade
What happened: agent built fixes on assumed mental model (tier-4) without verifying against
                Claude Code architecture (tier-3) or operator (tier-1)
Severity: HIGH
Solution: SB-097 mental-model-verification rule extension
```

### Instance C13-4 — Synthetic-test as real verification (HIGH; SB-091; cousin to C09-3)

```
Date: 2026-05-05
What happened: agent's synthetic test (tier-3 self-crafted) accepted as verification
                vs real-session diag-log (tier-2)
Severity: HIGH
Solution: SB-091 synthetic-test-not-real-verification rule
```

### Instance C13-5 — Documentation over operator-empirical (MEDIUM)

```
Date: pre-Fire-79 multiple
What happened: agent cites Claude Code official docs (tier-3) over operator's empirical observation
                ("docs say X but I'm seeing Y")
Severity: MEDIUM
Solution: tier-1 always trumps tier-3 per SB-109
```

### Instance C13-6 — Subagent research as tier-1 (MEDIUM)

```
Date: 2026-05-07 subagent dispatch
What happened: agent treats claude-code-guide subagent answer as authoritative (effectively tier-1)
Reality: subagent research is tier-3; can be incomplete
Severity: MEDIUM
Solution: tier-3 must be flagged as tier-3 in agent reasoning
```

### Instance C13-7 — Premature blocked-classification (MEDIUM; SB-049)

```
Date: 2026-05-07 cron F59
What happened: first dispatch failure → "dispatch path blocked" (tier-4 inference)
Reality: parameter mismatch; retry possible (would have been tier-2 evidence post-retry)
Severity: MEDIUM
Solution: SB-049 sub-agent-dispatch-retry-pattern (1 retry minimum before tier-4 classification)
```

### Instance C13-8 — Agent-output-vs-real-effect conflation (MEDIUM)

```
Date: hook-tuning iterations
What happened: agent's stdout output (e.g., "Fix landed") taken as evidence of fix
                vs runtime diag-log evidence
Severity: MEDIUM
Solution: tier-2 diag-log required for runtime verification
```

### Instance C13-9 — Cached-state vs fresh-read (HIGH; SB-102)

```
Date: 2026-05-05
What happened: agent operated on cached file state in conversation (tier-4) vs re-reading
                file from disk (tier-2 ground-truth)
Severity: HIGH
Solution: SB-102 closure (re-read before edit; never cached)
```

### Instance C13-10 — Wrong-cause-attribution (MEDIUM; cousin SB-102)

```
Date: 2026-05-05 same incident
What happened: edit failure → agent claimed "concurrent modification" (tier-4 unverified hypothesis)
Reality: agent never re-read; cached anchor stale
Operator catch: "it was no concurently modified you just didn't look at it before"
Severity: MEDIUM
Solution: re-read first; only after empirical evidence claim cause
```

## Distribution

```
Severity:
  HIGH: 4 instances (C13-1, C13-3, C13-4, C13-9)
  MEDIUM: 6 instances (others)
  LOW: 0

Tier-conflict-type:
  tier-3 over tier-1: 3 (C13-1, C13-5, C13-6)
  tier-4 over tier-1/2: 5 (C13-2, C13-3, C13-7, C13-9, C13-10)
  tier-3 self-crafted as tier-2: 2 (C13-4, C13-8)
```

## Cross-cluster intersection

C13 frequently intersects:
- C04 input-discipline: 6/10 (didn't read tier-1/2 source)
- C09 status-claim-without-verification: 4/10
- C19 documentation-implementation-asymmetry: 3/10
- C12 going-to-extremes: 2/10 (cousin: tier-mistake → cascade)

## Cumulative coverage

| Cluster | Fire | Instances |
|---|---|---|
| C04, C02, C15, C07 (originals) | 93-96 | 63 |
| C19 (NEW) | 111 | 12 |
| C18 cross-cutting | 115 | 15 |
| C12 going-to-extremes | 120 | 12 |
| C03 stage-gate-violations | 123 | 13 |
| C09 status-claim-without-verification | 126 | 12 |
| **C13 evidence-priority-misordered** | **129 (THIS)** | **10** |
| **TOTAL** | | **137** |

137 of ~237 instances = **58%** body-wide pain-point coverage.

## Foundational classification

Per Fire 119 + Fire 127 criteria:
- Criterion 1: cross-cutting frequency — C04+C09 intersection 6/10+4/10 = high; cross-cutting frequency estimated ~50% (below 60% threshold)
- Criterion 2: HIGH-severity dominant (4/10 = 40%) ✓
- Criterion 3: Recurring ✓
- Criterion 4: Hook-compatible ◐ (tier-classification harder to detect than C09 patterns)
- Criterion 5: Cross-project ✓

C13 = SECONDARY per Fire 119; below foundational threshold but close. Phase 2 enforcement candidate.

## Solution-piece chain

- /root operating-principles.md extension #5 (evidence-priority-hierarchy)
- SB-091, SB-097, SB-102, SB-109, SB-110, SB-049, SB-112 closures
- Mental-model-verification extension to work-mode.md
- Re-read-before-edit extension

## Closing

C13 = 10 instances; SECONDARY foundational classification; cumulative 58% pain coverage. Per /loop directive: methodology-aware enumeration continues.

**Standing by per /loop directive.**

## Tags

[per-instance-evidence, c13-evidence-priority-misordered, sb-109-110-cluster, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-129]
