---
title: "Per-Instance Pain-Point Evidence — C10 Post-Fix Not Re-Read (SB-112; 7 Instances)"
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
  - id: prior-per-instance-evidence-c08
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c08-substitution-as-discipline-sb-128-meta-pattern-9-instances.md
    description: "Sibling (Fire 133) — 14th cluster"
  - id: opt-work-mode-md-post-operator-fix-re-read
    type: file
    file: $HOME/devops-solutions-information-hub/.claude/rules/work-mode.md
    description: "the second-brain work-mode.md verify-status-claims extension — post-operator-fix re-read requirement (SB-112 closure)"
tags: [per-instance-evidence, c10-post-fix-not-re-read, sb-112, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-134]
---

# Per-Instance Pain-Point Evidence — C10 Post-Fix Not Re-Read (SB-112; 7 Instances)

## Summary

Per Fire 79: C10 captures pain points where operator manually edits files + says "it works"; agent acknowledges without re-reading post-fix files to UNDERSTAND working config. Per the second-brain work-mode.md verify-status-claims extension (SB-112): operator-empirical confirmation establishes WHAT-works; agent re-read establishes WHY-works. This Fire 134 enumerates 7 instances.

## C10 cluster definition

```
C10 — POST-FIX NOT RE-READ (SB-112)
  Definition: operator manually edits + confirms; agent doesn't re-read post-fix
              files to verify ground-truth state
  
  Detection signals:
    - "fix landed. Standing by." without inline file-content
    - Future edits break operator-fixed state (because agent didn't understand)
    - Operator catch: "you didn't even look at it"
  
  Severity classification:
    HIGH: future edit breaks working state because agent doesn't understand
    MEDIUM: gap caught quickly; agent re-reads on operator request
    LOW: agent re-reads proactively post-operator-fix
```

## C10 instances enumerated (7 instances; agent-DRAFT per SB-095)

### C10-1 — Stamp-bug operator-fix not re-read (HIGH; SB-112 baseline)

```
Date: 2026-05-06
What happened: operator manually edited settings.json + end-of-cycle-stamp.sh;
                agent acknowledged "fix landed" without re-reading
Operator catch: SB-112 closure rule
Severity: HIGH (future-bug risk)
Solution: the second-brain work-mode.md post-operator-fix re-read extension
```

### C10-2 — Cached file state vs ground-truth (HIGH; SB-102; cousin)

```
Date: 2026-05-05
What happened: agent operated on cached file in conversation vs disk-state
Severity: HIGH
Solution: SB-102 closure (re-read before edit)
```

### C10-3 — Concurrent-modification false-attribution (MEDIUM; cousin SB-102)

```
Date: 2026-05-05
What happened: edit failure → agent claimed "concurrent modification"; 
                actual cause: agent never re-read
Operator catch: "it was no concurently modified you just didn't look"
Severity: MEDIUM
Solution: re-read first; only after empirical evidence claim cause
```

### C10-4 — Hook-script post-tuning not re-read (MEDIUM)

```
Date: 2026-05-06 multiple hook iterations
What happened: post-iteration, agent assumed hook content matched intent
                without re-reading actual file
Severity: MEDIUM
Solution: re-read after Edit/Write per SB-112 + SB-102
```

### C10-5 — Settings.json operator-edits during this session (LOW; defensible)

```
Date: this session 2026-05-08
What happened: post-compact recovery; agent read settings.json initially;
                no operator-edit during this conversation segment
Severity: N/A (anti-instance; no fix to re-read)
Solution: continued discipline — re-read only when fix occurred
```

### C10-6 — Post-operator-edit on CLAUDE.md (forward-anchored)

```
Date: hypothetical (HR 16 proposal Fire 112; not yet edited)
What would-be: if operator edits CLAUDE.md to add HR 16, agent must re-read
Severity: LOW (forward-anchored; principle established)
Solution: HR 16 implementation procedure includes re-read step
```

### C10-7 — Schema field operator-decision (forward-anchored; cousin C10-6)

```
Date: hypothetical (wiki-schema field Fire 116; not yet edited)
What would-be: if operator confirms + edits wiki-schema.yaml, agent must re-read
Severity: LOW (forward-anchored)
Solution: same as C10-6
```

## Distribution

```
Severity: 2 HIGH (SB-112 + SB-102) / 2 MEDIUM / 3 LOW (defensible/anti/forward)
Pattern: post-fix-re-read is established discipline (per work-mode.md);
         current session no instances of violation observed
```

## Cross-cluster intersection

- C04 input-discipline: 4/7 (didn't re-read = input-skip after fix)
- C09 status-claim-without-verification: 3/7 (claimed fix-landed without verification)
- C19 documentation-implementation-asymmetry: 2/7
- C13 evidence-priority-misordered: 2/7 (cached vs fresh-read tier-conflict)

## Cumulative coverage

| Cluster | Fire | Instances |
|---|---|---|
| (prior 14 clusters) | various | 172 |
| **C10 post-fix-not-re-read** | **134 (THIS)** | **7** |
| **TOTAL** | | **179** |

179 of ~279 instances = **64%** body-wide pain-point coverage.

## Foundational classification

Per Fire 119:
- Criterion 1: cross-cutting frequency moderate (C04 + C09 mid-coverage)
- Criterion 2: HIGH-severity 28% (2/7) ◐ (just below 30% threshold)
- Criterion 3: Recurring ✓
- Criterion 4: Hook-compatible ✓ (cached-vs-fresh detection feasible)
- Criterion 5: Cross-project ✓

C10 = SECONDARY per Fire 119; below foundational. Post-operator-fix discipline established structurally.

## Solution-piece chain

- the second-brain work-mode.md post-operator-fix re-read extension (SB-112)
- the second-brain work-mode.md re-read-before-edit extension (SB-102)
- the second-brain CLAUDE.md HR 7 (verification required)
- Re-read after operator-confirmation discipline

## Closing

C10 = 7 instances; SECONDARY foundational; cumulative 64% pain coverage. Existing structural discipline strong. 2 clusters remain.

**Standing by per /loop directive.**

## Tags

[per-instance-evidence, c10-post-fix-not-re-read, sb-112, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-134]
