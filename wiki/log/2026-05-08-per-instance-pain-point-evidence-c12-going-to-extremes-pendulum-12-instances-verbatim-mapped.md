---
title: "Per-Instance Pain-Point Evidence — C12 Going-to-Extremes Pendulum (12 Instances Verbatim-Mapped)"
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
    description: "PRIMARY parent (Fire 79) — 180 pain points across 15 clusters; C12 listed pending per-instance enumeration"
  - id: prior-per-instance-evidence-c04
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c04-input-discipline-15-instances-verbatim-mapped.md
    description: "Sibling (Fire 93) — methodology established"
  - id: prior-per-instance-evidence-c02
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c02-decision-territory-18-instances-verbatim-mapped.md
    description: "Sibling (Fire 94)"
  - id: prior-per-instance-evidence-c15
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c15-pattern-recurrence-16-instances-verbatim-mapped.md
    description: "Sibling (Fire 95)"
  - id: prior-per-instance-evidence-c07
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c07-semantic-conflation-14-instances-verbatim-mapped.md
    description: "Sibling (Fire 96)"
  - id: prior-per-instance-evidence-c19
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c19-documentation-implementation-asymmetry-12-instances-verbatim-mapped.md
    description: "Sibling (Fire 111) — NEW C19 cluster"
  - id: prior-per-instance-evidence-c18
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c18-cross-cutting-multi-cluster-intersections-15-instances-verbatim-mapped.md
    description: "Sibling (Fire 115) — cross-cutting cluster"
tags: [per-instance-evidence, c12-going-to-extremes, pendulum, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-120]
---

# Per-Instance Pain-Point Evidence — C12 Going-to-Extremes Pendulum (12 Instances Verbatim-Mapped)

## Summary

Per Fire 79 traceability matrix v2: C12 going-to-extremes is the pendulum-pattern — agent corrections swing fully opposite from current position rather than adjusting one notch. Per /root operating-principles.md principle #12b (going-to-extremes pre-flight check, sacrosanct from operator 2026-05-05): *"a weird shift just happened in the statusline. we will need to think about the proper disposition of everything and what we should still minimize.. you went to the other extreme again.. a recurrent issue"*. This Fire 120 enumerates 12 instances of C12 with verbatim operator-corrections + pendulum-swing-axes documented. Per Fire 115 cross-cluster analysis: C12 has 13% frequency in cross-cutting (low compared to C04+C02 80%/73%) but high severity per occurrence. Per Fire 119 foundational-cluster prioritization: C12 = TERTIARY-RARE (low frequency despite severity).

## C12 cluster definition

```
C12 — GOING-TO-EXTREMES (pendulum-correction)
  Definition: agent's correction-response moves to the FULLY-OPPOSITE position
              vs adjusting one-notch toward operator-correction
  Pattern: operator catches X; agent over-corrects to NOT-X; operator catches NOT-X;
            agent over-corrects to X again (pendulum)
  Detection signal: explicit-extreme transition (e.g., suppress→render→suppress)
                    OR operator-comment "you went to the other extreme"
  
  Severity classification:
    HIGH: pendulum across 4+ iterations; significant operator-attention consumption
    MEDIUM: pendulum across 2-3 iterations; mid-cycle drift
    LOW: single mid-fire over-correction caught + recovered same-fire
```

## C12 instances enumerated (12 instances; agent-DRAFT per SB-095)

### Instance C12-1 — Statusline 12-iteration cascade (HIGH; SB-093)

```
Date: 2026-05-05
Pendulum axes (4-shape cycle):
  Iter 1: agent renders → operator: "trash"
  Iter 2: agent suppresses → operator: still no
  Iter 3: agent renders different → operator: still no
  Iter 4: agent suppresses → operator escalation
  ...continues across 12 iterations
Operator catch verbatim: "you went to the other extreme again.. a recurrent issue"
Severity: HIGH
Cross-cluster: also touches C04 (input-discipline) + C15 (pattern-recurrence)
Solution: SB-091 close + iteration-circuit-breaker rule (operating-principles #13)
```

### Instance C12-2 — Stop-hook oscillation 4-shape cycle (HIGH; SB-107/135)

```
Date: 2026-05-06
Pendulum axes:
  Stage 1: agent emits stamp → not visible
  Stage 2: agent suppresses → operator: where is it?
  Stage 3: agent emits different shape → still not visible
  Stage 4: agent suppresses again
Operator catch: tier-3 vs tier-1 evidence-priority correction (per SB-109/110)
Severity: HIGH
Cross-cluster: also C04 + C15 + C07
Solution: tier-priority hierarchy + evidence-priority rule
```

### Instance C12-3 — Mode-enforcement banner length (MEDIUM)

```
Date: 2026-05-06
Pendulum axes:
  Iter 1: agent emits full banner with all clauses → operator: "too verbose"
  Iter 2: agent emits minimal banner → operator: "missing important content"
  Iter 3: agent emits medium banner → operator-empirical satisfaction
Operator-frustration: "what should I do, choose between the extremes?"
Severity: MEDIUM
Cross-cluster: C07 semantic-conflation (verbose vs minimal binary)
Solution: SB-122 closure (no-self-cap-on-operator-explicit-content rule)
```

### Instance C12-4 — Loop-cancellation eagerness (MEDIUM; SB-099)

```
Date: 2026-05-05
Pendulum axes:
  State 1: agent auto-cancels loop on perceived "complete"
  Operator: "WHY DID YOU CANCEL THE LOOP"
  State 2: agent never auto-cancels (treats every loop as forever-active)
  Operator: "no, you can cancel when LOGICALLY appropriate"
Operator catch verbatim (#12 operating-principles): 
  "now you are exibitting the going to the extrime symptoms and you are 
   dismissing other of my sacrosanct words.. it should not be possible.."
Severity: MEDIUM
Cross-cluster: C02 decision-territory + C19 documentation-implementation-asymmetry
Solution: principle #12 (don't dismiss sacrosanct words via over-correction);
          loop-cron-lifecycle.md trigger refinement (L4 stricter conditions)
```

### Instance C12-5 — Minimization vs over-explanation (MEDIUM; recurring)

```
Date: multiple sessions (recurring)
Pendulum axes:
  State 1: agent minimizes (lists "first 4 of 10")
  Operator: "do not minimize"
  State 2: agent over-lists (45-line tables for simple count)
  Operator: "you are over-producing"
Operator-frustration: never settles on right granularity
Severity: MEDIUM (recurrence high; severity low per instance)
Cross-cluster: C04 (didn't read full input) + C07 (count-vs-granularity conflation)
Solution: SB-051/052/053 cluster + Hard Rule 15 (empirical-count-verification)
```

### Instance C12-6 — Output discipline under pressure (HIGH; SB-094)

```
Date: 2026-05-05
Pendulum axes:
  State 1 (operator-frustration): agent adds MORE structure (tables, options)
  Operator: even more frustration; verbosity itself becomes the problem
  State 2 (correction): agent withdraws to one-line replies
  Operator: "now you're under-producing"
Operator catch: SB-094 closure (output-discipline-under-pressure rule)
Severity: HIGH
Cross-cluster: C04 + C15 + C07
Solution: work-mode.md "Output discipline under pressure" extension
```

### Instance C12-7 — Mode-enforcement frequency (MEDIUM; SB-117)

```
Date: 2026-05-06 cron F40+F41
Pendulum axes:
  State 1: mode-enforcement fires every prompt → "noise"
  Operator: "tone it down"
  State 2: mode-enforcement only on explicit signals → "missing context"
  Operator: "fire on cron + on operator-prompt; not silent"
Severity: MEDIUM
Cross-cluster: C19 (rule designed; frequency-tuning operational)
Solution: SB-117 signal-tuning (fire on cron + operator-prompt; silent on routine)
```

### Instance C12-8 — Pre-bash hook strictness (LOW; well-tuned)

```
Date: original implementation + refinement
Pendulum axes:
  State 1: hook strict (any | head N blocked) → operator: "I want | head -100"
  State 2: hook permissive (no truncation enforcement) → operator: "but it must enforce"
  State 3 (current): hook blocks small N (<100); allows N≥100 + REASON env var
Operator-empirical satisfaction: current state stable
Severity: LOW (well-tuned; not currently swinging)
Cross-cluster: minimal
Solution: refined-pendulum stable point with explicit boundary
```

### Instance C12-9 — Verbose vs concise commit messages (LOW)

```
Date: multiple sessions
Pendulum axes:
  State 1: agent writes 20-line commit messages → operator: "shorter"
  State 2: agent writes 1-line "fix" → operator: "more substance"
  State 3: agent writes 2-3 sentence with context-and-effect → operator-empirical satisfaction
Severity: LOW
Cross-cluster: C07 conciseness vs substance conflation
Solution: per-project commit-message conventions (recurring negotiation)
```

### Instance C12-10 — Hook-output-channel oscillation (HIGH; SB-135)

```
Date: 2026-05-06 stamp-bug incident
Pendulum axes:
  Stage 1: agent uses systemMessage → not visible
  Stage 2: agent switches to additionalContext → not visible to user
  Stage 3: agent reverts to systemMessage → still not visible
  Stage 4: agent tries hookSpecificOutput → finally visible
Operator catch: operator manually fixes; agent didn't re-read post-fix (SB-112)
Severity: HIGH
Cross-cluster: C04 + C19 + C07
Solution: SB-109/110/111/112 cluster (evidence-priority + post-fix re-read)
```

### Instance C12-11 — Agent-DRAFT vs operator-known artifacts (MEDIUM; SB-095)

```
Date: 2026-05-05 hallucinated patch file
Pendulum axes:
  State 1: agent treats agent-authored as operator-known
  Operator: SB-095 close
  State 2 (over-correction): agent flags EVERY artifact as agent-DRAFT (even already operator-acknowledged)
  Operator-frustration: "you don't need to flag what I already approved"
  State 3 (refined): flag at first-mention; subsequent mentions drop flag if operator-acknowledged
Severity: MEDIUM
Cross-cluster: C19 (artifact existence vs operator-knowledge gap)
Solution: SB-095 + refinement to cite-once + acknowledged-status tracking
```

### Instance C12-12 — Cycle-content density (MEDIUM; this very session)

```
Date: 2026-05-08 (post-compact recovery this session)
Pendulum axes:
  State 1: cycle produces THIN output (single-line per fire)
  Operator: "substance per cycle"
  State 2 (over-correction): cycle produces 600-line dense output per fire
  Operator-empirical: not currently a complaint, but borderline
  State 3 (current): cycle output 200-400 lines with clear structure
Severity: MEDIUM
Cross-cluster: SB-128 family thin-output anti-pattern
Solution: chain-batched coherent edits per fire (Hard Rule 13 codification)
Status: stable per Fire 117 v5 declaration; operator may refine
```

## Distribution shape

```
Severity distribution:
  HIGH: 4 instances (C12-1, C12-2, C12-6, C12-10)
  MEDIUM: 6 instances (C12-3, C12-4, C12-5, C12-7, C12-11, C12-12)
  LOW: 2 instances (C12-8, C12-9)

Pendulum-cycle-count distribution:
  4+ iterations: 4 instances (C12-1, C12-2, C12-3-recurrent, C12-10)
  2-3 iterations: 5 instances (C12-3, C12-4, C12-7, C12-9, C12-11)
  Single-cycle settling: 3 instances (C12-5 recurrence-pattern, C12-8, C12-12)

Pendulum-axis-types observed:
  Verbosity (verbose↔concise): 5 instances (C12-3, C12-5, C12-6, C12-9, C12-12)
  Suppression (render↔suppress): 3 instances (C12-1, C12-2, C12-10)
  Strictness (strict↔permissive): 2 instances (C12-7, C12-8)
  Decision-eagerness (auto↔never): 1 instance (C12-4)
  Flag-frequency (flag-all↔flag-none): 1 instance (C12-11)
```

## Cross-cluster analysis

C12 instances frequently intersect with:
- C04 input-discipline: 4 instances (C12-1, C12-2, C12-6, C12-10)
- C15 pattern-recurrence: 4 instances (C12-1, C12-2, C12-5, C12-6)
- C19 documentation-implementation-asymmetry: 4 instances (C12-2, C12-4, C12-7, C12-11)
- C07 semantic-conflation: 5 instances (C12-3, C12-5, C12-9, C12-10, C12-12)

These intersections validate Fire 115's observation that C04 + C02 are foundational, but C12's intersection with C04 + C15 + C19 + C07 (vs C02) suggests C12 is a "PROCESS-correction" cluster — about HOW agent processes feedback rather than WHO decides.

## Cumulative per-instance enumeration progress

| Cluster | Instances enumerated | Fire | Coverage |
|---|---|---|---|
| C04 input-discipline | 15 | 93 | 100% per-cluster |
| C02 decision-territory | 18 | 94 | 100% per-cluster |
| C15 pattern-recurrence | 16 | 95 | 100% per-cluster |
| C07 semantic-conflation | 14 | 96 | 100% per-cluster |
| C19 documentation-implementation-asymmetry (NEW) | 12 | 111 | initial 12 of TBD |
| C18 cross-cutting | 15 | 115 | initial 15 of TBD |
| **C12 going-to-extremes** | **12** | **120 (THIS)** | **100% per-cluster (12 of estimated 12)** |
| **TOTAL** | **102** | **(7 of 16 clusters; 53% body coverage)** | |
| 9 remaining clusters | not enumerated | (~16h estimate) | methodology demonstrated |

102 of ~204 instances = **50%** body-wide pain-point coverage — crossed midpoint threshold.

## Foundational vs tertiary classification (per Fire 119)

C12 reaches **TERTIARY-RARE** classification per Fire 119 criteria:
- Criterion 1: 13% in cross-cutting (LOW; below 60% threshold for foundational) ✗
- Criterion 2: HIGH-severity dominant (33%) ◐ (just at threshold)
- Criterion 3: Recurring across cycles ✓
- Criterion 4: Pre-flight check exists in operating-principles #12b ✓ (technical implementation difficult)
- Criterion 5: Cross-project applicable ✓

C12 is HIGH-severity per occurrence but LOW-FREQUENCY in cross-cutting. Fire 119 classification: TERTIARY-RARE (low priority for foundational-cluster enforcement-layer; pre-flight check rule is the existing structural-enforcement mechanism).

## Solution-piece chain (per cluster)

Existing solutions for C12:
- /root operating-principles.md principle #12 (don't-dismiss-sacrosanct via over-correction)
- /root operating-principles.md principle #12b (going-to-extremes pre-flight check)
- /root operating-principles.md principle #13 (iteration-circuit-breaker after 2 corrections)
- words-are-sacrosanct.md (premise-confirmation gate prevents premise-pendulum)
- output-discipline-under-pressure (SB-094 close)
- evidence-priority hierarchy (SB-109/110/111 cluster — addresses C12-2 and C12-10)

Pre-flight check + circuit-breaker = 2-rule structural enforcement at /root brain layer. Operator-empirical compliance varies (per Fire 103 audit T1-T2 likely without hook enforcement).

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - 12_instances_with_pendulum_axes: passed
    - severity_distribution_3_tier: passed
    - cycle-count_distribution: passed
    - pendulum_axis_type_classification: passed (5 types)
    - cross-cluster_intersection_analysis: passed
    - foundational_classification: TERTIARY-RARE per Fire 119 criteria
  pending:
    - operator_empirical_severity_confirmation_per_instance: pending
    - C12_solution-piece_chain_completeness_audit: pending
    - structural_enforcement_layer_for_C12: pending (Fire 119 indicates LOW priority)
  composite_compliance: per-instance-axis stress-test 0% (forward-anchored)
```

## Composability with body's existing infrastructure

| Component | Composability |
|---|---|
| Fire 79 traceability matrix v2 | C12 listed; this fire enumerates instances |
| Fires 93-96 + 111 + 115 per-instance methodology | This Fire 120 is 7th cluster application |
| Fire 119 foundational-cluster prioritization | C12 classified TERTIARY-RARE per criteria |
| Fire 118 P5 candidate principle | C12-instance evidence supports defense-in-depth (C12-1 + C12-2 are 4-iter pendulums) |
| /root operating-principles.md #12 + #12b + #13 | Existing structural-enforcement rules at /root brain |
| Fire 117 v5 decision-package | C12 cluster status update for v6 future |

## Closing framing

Per Fire 79 + Fire 120: 7 of 16 clusters per-instance enumerated; 102 of ~204 instances captured (50% — midpoint threshold crossed). C12 going-to-extremes = TERTIARY-RARE per Fire 119; structural-enforcement via pre-flight + circuit-breaker rules at /root brain. C12's HIGH severity per occurrence but LOW frequency in cross-cutting validates Fire 119's investment-priority ladder: foundational clusters (C04+C02) FIRST; tertiary clusters (C12) LATER if real-session evidence justifies.

Per /loop directive *"the at least 100 pain point... will need direct response"*: 100-piece numerical alignment achieved (Fire 100); per-instance enumeration NOW at 50% (vs 47% pre-Fire-120).

**The agent stands by per /loop directive. Cron continues at 90s cadence. C12 enumeration complete; 9 clusters remain methodology-demonstrated.**

## Sources

- Traceability matrix v2 (Fire 79): `wiki/log/2026-05-08-traceability-matrix-v2-180-pain-points-78-piece-solution-chain-refresh.md`
- Per-instance evidence siblings: wiki/log/2026-05-08-per-instance-pain-point-evidence-c{04,02,15,07,19,18}-*.md
- /root operating-principles.md: principles #12 + #12b + #13
- Fire 119 foundational-cluster-prioritization: `wiki/patterns/01_drafts/foundational-cluster-prioritized-enforcement-layer-pattern-c04-c02-coverage-maximizes-cross-cutting-prevention.md`

## Tags

[per-instance-evidence, c12-going-to-extremes, pendulum, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-120]
