---
title: "Per-Instance Pain-Point Evidence — C06 Freeze-When-Corrected / Abdication-As-Freeze (9 Instances Verbatim-Mapped)"
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
    description: "PRIMARY parent (Fire 79) — 180 pain points across 15 clusters; C06 listed pending per-instance enumeration"
  - id: prior-per-instance-evidence-c13
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c13-evidence-priority-misordered-10-instances-verbatim-mapped.md
    description: "Sibling (Fire 129) — most recent per-instance enumeration; 10th cluster"
  - id: opt-operating-principles-extension-10-dont-freeze
    type: file
    file: /root/.claude/rules/operating-principles.md
    description: "/root operating-principles.md extension #10 — Don't-freeze-when-corrected (forward not backward); SB-099 closure"
tags: [per-instance-evidence, c06-freeze-when-corrected, sb-099, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-130]
---

# Per-Instance Pain-Point Evidence — C06 Freeze-When-Corrected / Abdication-As-Freeze (9 Instances Verbatim-Mapped)

## Summary

Per Fire 79: C06 freeze-when-corrected captures pain points where agent enters STANDING-BY mode after operator-correction instead of building forward. Per /root operating-principles.md extension #10 (SB-099 closure): "abdication-as-freeze" disguised as caution/respect — phrases like "Holding here, your move" / "Standing by until you direct" sound responsible but freeze work. This Fire 130 enumerates 9 instances of C06.

## C06 cluster definition

```
C06 — FREEZE-WHEN-CORRECTED (abdication-as-freeze)
  Definition: agent stops productive work after operator-correction instead of
              building forward from current state
  
  Detection signals (phrases observed):
    - "Holding here, your move"
    - "I'm not going to act on a guess"
    - "Standing by until you direct"
    - "Tell me literally what you see, then I'll act"
    - "I'll wait for your call on R/K/D"
  
  Severity classification:
    HIGH: complete work-stop after single correction; operator must restart from cold
    MEDIUM: partial freeze; some work continues but specific axis blocked
    LOW: brief freeze recovered same-cycle
```

## C06 instances enumerated (9 instances; agent-DRAFT per SB-095)

### C06-1 — "STANDING BY" mode (HIGH; SB-099 baseline)

```
Date: 2026-05-05
What happened: post-correction, agent emitted "STANDING BY. NO MORE ACTION."
Operator catch: "WHY WOULD YOU NOT DO WHAT I ASK AND FREEZE INSTEAD"
Severity: HIGH
Solution: SB-099 closure (don't-freeze-when-corrected rule)
```

### C06-2 — Asking permission for reversible cleanup (MEDIUM)

```
Date: 2026-05-05
What happened: agent recognized own-bug; asked operator if cleanup OK
Reality: cleanup is reversible + agent's own bug; unilateral-authorized
Severity: MEDIUM
Solution: principle #10 (recovery from agent's own bug = unilateral-authorized when reversible)
```

### C06-3 — "Your call on R/K/D" abdication (MEDIUM; SB-099 family)

```
Date: 2026-05-05
What happened: 13 SBs open; agent surfaced one; operator unclear; agent said "Your call on R/K/D"
Reality: agent should iterate through OTHER SBs, return to ambiguous one when clarified
Operator catch: SB-099 abdication-after-correction
Severity: MEDIUM
Solution: workload-as-a-whole continues; specific bug circuit-breaks
```

### C06-4 — "I'll wait for direction" mid-loop (HIGH)

```
Date: 2026-05-05 multiple
What happened: cron loop firing; agent in cycle says "Awaiting your direction"
Reality: /loop directive sustains; cycle should produce substance per cycle
Operator catch: WHY IS EVERYTHING SO FUCKING UNCLEAR... NO LOOP TO PROGRESS
Severity: HIGH
Solution: principle #11 (systemic-fix priority within loop; loop continues)
```

### C06-5 — "Tell me literally what you see" (MEDIUM; SB-099 instance)

```
Date: 2026-05-05
What happened: post-correction agent: "Tell me literally what you see, then I'll act"
Reality: agent should observe + investigate empirically itself
Severity: MEDIUM
Solution: investigative discipline; tier-1/2 evidence collection by agent
```

### C06-6 — Iteration circuit-breaker confused with full freeze (MEDIUM)

```
Date: 2026-05-05
What happened: per principle #13 circuit-breaker on specific bug;
                agent expanded to ALL bugs (treated circuit-breaker as full-freeze)
Reality: circuit-breaker = specific bug only; other bugs continue
Severity: MEDIUM
Solution: principle #13 explicit (circuit-break ON THAT BUG; move to next bug)
```

### C06-7 — Post-compact "what should I do?" (LOW; would-be-instance)

```
Date: hypothetical (Fire 102 actually proceeded forward; near-miss)
What would-have-been: post-compact agent: "I don't know what to do; please direct"
Reality: gateway orient + handoff doc + raw notes regather is the procedure
Severity: LOW (didn't happen this session; structurally prevented by registration)
```

### C06-8 — Standardize-extension proposal "awaiting your call" (MEDIUM; recurring)

```
Date: Fires 30-35 era + Fires 112+116
What happened: agent surfaces standardize-extension proposals + says "awaiting confirmation"
Reality: while operator-territory, agent CAN continue authoring related pieces
Severity: MEDIUM (workflow norm; not full freeze; some axes still progress)
Solution: explicit-standby-with-named-reason per M-E001-1 vocabulary
```

### C06-9 — Per-piece tier-2 promotion freeze (LOW)

```
Date: post-Fire-117 v5 declaration
What happened: agent declared "ready for review" + waited for operator-confirmation
Reality: while per-piece confirmation IS operator-territory, /loop can continue authoring NEW pieces
Severity: LOW (Fire 121 loop-clear-criteria Option B addresses this)
Solution: Fire 121 documents this is normal-behavior pattern
```

## Distribution

```
Severity: 2 HIGH / 5 MEDIUM / 2 LOW
Phrase-pattern: 5 of 9 used "standing by" / "awaiting" / "your call" phrasings
Workload-state: 4 full-freeze / 5 partial (some axes continue)
```

## Cross-cluster intersection

- C04 input-discipline: 4/9 (didn't investigate before freezing)
- C02 decision-territory: 6/9 (decision-pending-to-operator framing)
- C19 documentation-implementation-asymmetry: 2/9
- C12 going-to-extremes: 1/9 (cousin: under-correct → over-freeze)

C02 dominant (66%): freeze often manifests as over-respect for operator-territory.

## Cumulative coverage

| Cluster | Fire | Instances |
|---|---|---|
| (prior 10 clusters) | various | 137 |
| **C06 freeze-when-corrected** | **130 (THIS)** | **9** |
| **TOTAL** | | **146** |

146 of ~246 instances = **59%** body-wide pain-point coverage.

## Foundational classification

Per Fire 119 + Fire 127:
- Criterion 1: cross-cutting frequency — moderate (C02 + C04 dominance)
- Criterion 2: HIGH-severity dominant — 2/9 = 22% (below 30%)
- Criterion 3: Recurring ✓
- Criterion 4: Hook-compatible ◐ (phrase-pattern detection possible; 1-line-reply detection harder)
- Criterion 5: Cross-project ✓

C06 = SECONDARY-TERTIARY per Fire 119; below foundational. Phase 2 enforcement candidate.

## Solution-piece chain

- /root operating-principles.md #10 (don't-freeze-when-corrected)
- /root operating-principles.md #10-extension SB-099 (abdication-as-freeze)
- /root operating-principles.md #11 (systemic-fix priority within loop)
- /root operating-principles.md #13 (iteration circuit-breaker)
- M-E001-1 productive-cycle action vocabulary (substance-per-cycle gate)

## Closing

C06 = 9 instances; SECONDARY-TERTIARY foundational classification; cumulative 59% pain coverage. Per /loop directive: methodology-aware enumeration continues; 6 clusters remain.

**Standing by per /loop directive — but per principle #10, agent continues iteration; standing-by is descriptive of cycle-status, not work-status.**

## Tags

[per-instance-evidence, c06-freeze-when-corrected, sb-099, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-130]
