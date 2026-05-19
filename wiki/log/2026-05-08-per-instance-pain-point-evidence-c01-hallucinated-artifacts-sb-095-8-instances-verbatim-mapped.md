---
title: "Per-Instance Pain-Point Evidence — C01 Hallucinated Artifacts (SB-095; 8 Instances Verbatim-Mapped)"
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
  - id: prior-per-instance-evidence-c05
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c05-minimization-sb-051-052-053-9-instances-verbatim-mapped.md
    description: "Sibling (Fire 131) — 12th cluster"
  - id: opt-operating-principles-extension-14-no-hallucinated-artifacts
    type: file
    file: /root/.claude/rules/operating-principles.md
    description: "/root operating-principles.md extension #14 — No hallucinated artifacts gaining reality (SB-095 closure)"
tags: [per-instance-evidence, c01-hallucinated-artifacts, sb-095, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-132]
---

# Per-Instance Pain-Point Evidence — C01 Hallucinated Artifacts (SB-095; 8 Instances Verbatim-Mapped)

## Summary

Per Fire 79: C01 hallucinated artifacts captures pain points where agent invents an artifact (file, command, draft) and treats it as operator-known/external in subsequent reasoning. Per /root operating-principles.md extension #14 (SB-095 closure): "agent-DRAFT" flagging required; never treat agent-authored as operator-known. This Fire 132 enumerates 8 instances.

## C01 cluster definition

```
C01 — HALLUCINATED ARTIFACTS GAINING REALITY (SB-095)
  Definition: agent invents artifact (file/command/document) then treats as real
              external thing in reasoning chain
  
  Detection signals:
    - "the patch file at /tmp/..." (without operator-acknowledgment)
    - "as I mentioned in X" (where X is agent-only-creation)
    - "use the command Y" (where Y is agent-named-not-implemented)
  
  Severity classification:
    HIGH: hallucinated artifact cited as evidence in operator-decision context
    MEDIUM: hallucinated artifact in agent's reasoning; caught quickly
    LOW: agent-DRAFT flagged correctly; not gaining reality
```

## C01 instances enumerated (8 instances; agent-DRAFT per SB-095)

### C01-1 — `/tmp/opt-statusline-patch.txt` invention (HIGH; SB-095 baseline)

```
Date: 2026-05-05
What happened: agent authored `/tmp/opt-statusline-patch.txt` as hypothetical;
                later cited "the patch file" as if external operator-known artifact
Operator catch: "it even invented a random patch file... and now its even considering it as something real"
Severity: HIGH (operator-trust loss)
Solution: SB-095 closure (agent-DRAFT flagging rule)
```

### C01-2 — Cross-reference to non-existent piece (MEDIUM; recurring)

```
Date: pre-Fire-79 multiple
What happened: cross-references to "Fire X" that didn't yet exist or wasn't authored
Severity: MEDIUM (pipeline post catches via cross-reference validation)
Solution: pipeline post lint catch
```

### C01-3 — Slash command reference without implementation (MEDIUM; recurring)

```
Date: post-Fires 99/101 (question-registry + blocker-impediment-registry)
What happened: pieces reference /questions add or /blockers show as if available
Reality: slash commands NOT implemented in the second-brain
Severity: MEDIUM (caught by Fire 103 4-tier audit; pieces flagged Tier 1)
Solution: Fire 103 audit method + agent-DRAFT framing per piece
```

### C01-4 — Hypothetical hook configurations (MEDIUM; recurring)

```
Date: Fires 105+106+107 hook specs
What happened: spec-pages reference Python hook code as if implementable
                without "agent-DRAFT spec" framing in body
Reality: code is template; not wired
Severity: MEDIUM (defensible per operator-territory implementation)
Solution: spec frontmatter `authorship: agent-authored` + per-spec "agent-DRAFT per SB-095" flag
```

### C01-5 — Implementation_tier field cited before added (LOW; defensible)

```
Date: Fires 116+ that reference `implementation_tier` field
Reality: field NOT YET in wiki-schema; proposal pending operator
Severity: LOW (defensible — explicitly cited as "proposal" not as canonical)
Solution: wiki-schema field standardize-extension proposal Fire 116 explicit
```

### C01-6 — Forward-anchored sister-project state (MEDIUM)

```
Date: Fire 113 sister-project propagation spec
What happened: spec assumes sister-project hook state without empirical investigation
Reality: each project's hook state needs separate audit
Severity: MEDIUM (forward-anchored; investigation noted)
Solution: per-project investigation phase 1 in Fire 113
```

### C01-7 — Auto-dream as if defined (LOW; defensible)

```
Date: Fire 107 + Fire 112 + Fire 128
What happened: spec references "only auto-dream allowed" without auto-dream definition
Severity: LOW (operator-pending Q1 explicitly surfaced; not gaining reality)
Solution: Fire 128 surfaces Q1 explicitly; agent-DRAFT hypothesis space
```

### C01-8 — Foundational-cluster expansion CITED ahead of operator-confirmation (LOW)

```
Date: Fire 127 (this conversation)
What happened: Fire 127 declared C09 added to foundational set
Reality: operator-empirical confirmation pending Q-FIRE-127-1
Severity: LOW (explicitly flagged as operator-pending)
Solution: standardize-extension-proposal pattern per the second-brain convention
```

## Distribution

```
Severity: 1 HIGH (SB-095 baseline) / 4 MEDIUM / 3 LOW (defensible)
Type: 1 invention-gaining-reality + 4 cross-reference-without-existence + 3 forward-anchored-explicit
Defensibility: 4 violations + 4 defensible
```

## Cross-cluster intersection

- C04 input-discipline: 4/8 (didn't verify before citing)
- C09 status-claim-without-verification: 3/8 (artifact-existence claimed without verification)
- C19 documentation-implementation-asymmetry: 6/8 (designed-only pieces cited as if operational)
- C02 decision-territory: 1/8

C19 dominant (75%): hallucinated-artifacts often manifest as design-vs-implementation gap.

## Cumulative coverage

| Cluster | Fire | Instances |
|---|---|---|
| (prior 12 clusters) | various | 155 |
| **C01 hallucinated-artifacts** | **132 (THIS)** | **8** |
| **TOTAL** | | **163** |

163 of ~263 instances = **62%** body-wide pain-point coverage.

## Foundational classification

Per Fire 119:
- Criterion 1: cross-cutting frequency moderate (C19+C04 dominant)
- Criterion 2: HIGH-severity 12% (1/8) ✗
- Criterion 3: Recurring ✓
- Criterion 4: Hook-compatible ◐ (cross-reference validator existing; pattern-match for fabricated paths)
- Criterion 5: Cross-project ✓

C01 = TERTIARY per Fire 119 (HIGH-severity below 30% threshold). Existing pipeline post lint + agent-DRAFT framing structural mitigation.

## Solution-piece chain

- /root operating-principles.md extension #14 (no hallucinated artifacts)
- SB-095 closure rule
- Pipeline post cross-reference validation
- agent-DRAFT frontmatter authorship field
- "agent-DRAFT per SB-095" inline flagging convention

## Closing

C01 = 8 instances; TERTIARY foundational classification; cumulative 62% pain coverage. Existing structural mitigation strong (pipeline post + agent-DRAFT framing). 4 clusters remain.

**Standing by per /loop directive.**

## Tags

[per-instance-evidence, c01-hallucinated-artifacts, sb-095, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-132]
