---
title: "Observe-Fix-Verify Loop — The Battle-Testing Cycle for Autonomous Agent Infrastructure"
aliases:
  - "Observe-Fix-Verify Loop"
  - "OFV Loop"
  - "Battle-Testing Cycle"
type: pattern
domain: ai-agents
layer: 5
status: synthesized
confidence: medium
maturity: seed
derived_from:
  - "Infrastructure Over Instructions for Process Enforcement"
  - "Model — Methodology"
  - "Agent Failure Taxonomy — Seven Classes of Behavioral Failure"
instances:
  - page: "OpenArms 2026-04-09 autonomous session — v1 → v7 methodology evolution"
    context: "10 iterations in one day. Each cycle: run agent → observe specific failure (stage violation, orphan code, rogue task, lost file) → fix the methodology (schema field, hook, invariant) → verify fix held in next run. Cost $3.50/task (v1) → $1.32/task (v7). Every fix persisted — zero regressions across subsequent runs."
  - page: "OpenArms E016 2026-04-15 spike cluster — 6 behavioral-failure findings"
    context: "After infrastructure solved stage violations (v10), the OFV loop turned to judgment-level failures. T107-T112 each observed one class (env-patching, weakest-checker, fatigue, sub-agent, artifact pollution, done-when), proposed one fix, verified against past run data. Produced six findings docs + recommendation per class. Same loop structure, higher cognitive layer."
  - page: "Research Wiki 2026-04-15 tool-building session — MCP fix + consumption-tracker bugs"
    context: "This wiki's own session. Built sister_project tool, observed it broke on 3 edge cases while using it (hardcoded layout list, unnormalized `..` paths, file-sentinel crashes), fixed each, verified on the next tool invocation. Three OFV cycles in under an hour."
  - page: "OpenFleet immune-system doctor cycle"
    context: "30-second production OFV at runtime scale. Observe (detection functions per agent-task pair) → Fix (TEACH/COMPACT/PRUNE correction actions) → Verify (agent-health profile persists across cycles, repeat offenders escalate). The pattern productionized as a always-on loop."
contribution_status: pending-review
created: 2026-04-15
updated: 2026-04-15
sources:
  - id: openarms-live-ofv-pattern
    type: observation
    project: openarms
    path: wiki/domains/learnings/pattern-observe-fix-verify.md
    description: Live OpenArms pattern file — operator-authored naming + first-principles description of the OFV cycle as observed in the 2026-04-09 autonomous session. Verified 2026-04-15; this pattern page synthesizes from OA's naming + our own three-layer evidence.
  - id: openarms-live-methodology-battle-tested
    type: observation
    project: openarms
    path: wiki/domains/learnings/lesson-methodology-battle-tested.md
    description: Live OpenArms lesson — "stable not because well-designed initially but stress-tested by real operation" — the claim this pattern operationalizes. Verified 2026-04-15.
  - id: openarms-live-integration-tests-insufficient
    type: observation
    project: openarms
    path: wiki/domains/learnings/lesson-integration-tests-insufficient.md
    description: Live OpenArms lesson — closed-verification-loop failure mode (agent writes both impl+tests, 686 passing tests / 0 runtime imports / 2073 lines orphaned). Evidence that the Verify step MUST be external to the agent. Verified 2026-04-15.
tags: [pattern, methodology-process, battle-testing, iteration, ofv, autonomous-agent, observability, correction-cycle]
---

# Observe-Fix-Verify Loop — The Battle-Testing Cycle for Autonomous Agent Infrastructure

## Summary

The **Observe-Fix-Verify loop** (OFV) is the iteration cycle that hardens agent infrastructure through real operation rather than prior design. Run the system → observe what went wrong with specific evidence (stage violation / orphan code / lost file / wrong artifact) → fix the ROOT cause in the methodology or enforcement layer (not the symptom in the run) → verify the fix persists on the next run. The pattern is infrastructure-level analog of Build-Measure-Learn, adapted to agent methodology evolution. **Its invariant is externality of the Verify step**: the agent that produced the observation cannot be the verifier — otherwise the loop closes on itself and produces false confidence (OpenArms's 686-passing-tests / 0-runtime-imports incident). The pattern scales from session-length (v1→v7 in one day) to runtime (OpenFleet doctor cycle every 30s) to sprint-length (E016's six-week behavioral-class investigations).

> [!info] Pattern Reference Card
>
> | Step | Who | What | Failure if wrong |
> |---|---|---|---|
> | **1. Observe** | Runtime telemetry, post-run analysis, immune system, operator review | Specific failure with quantified evidence (cost, error, artifact path) | Vague "agent is bad" → no actionable fix |
> | **2. Fix** | Methodology/infra layer, not the running agent | Root cause addressed in schema, hook, command, validator, or stage rule | Symptom patched → recurs next run |
> | **3. Verify** | **EXTERNAL** to the cause of the observation | Next run shows fix held without new regression | Same agent verifies own fix → false confidence |

## Pattern Description

The OFV loop is the mechanism by which methodology becomes battle-tested. Most methodology frameworks are designed in theory and then observed to fail in practice. The OFV pattern inverts that: the methodology is EXPECTED to fail, and the loop captures each failure as a design input before the next cycle. Version increments (v1 → v2 → … → vN) are the traceable record of the loop's output.

**Three invariants the loop must preserve:**

1. **The Observe step must produce quantified evidence.** Not "agent skipped stage" but "T087 test-stage skipped tsgo; code shape was esbuild-grade at 36 min / 191 calls." Without quantification, the Fix cannot be targeted and the Verify cannot be judged.
2. **The Fix step must address the ROOT cause, in the methodology/infra layer.** Patching the symptom in the running agent (adding a one-off instruction) is NOT a fix; it is a correction that will not persist. The fix belongs in the schema (new field), the hook (new check), the validator (new rule), or the command surface (new protocol).
3. **The Verify step must be external to the Observe context.** The classic failure case is agent-tests-agent: the agent writes the implementation AND the tests, they pass, the agent declares done. Integration tests run by an independent process (CI, harness, doctor cycle) are necessary. OA's 686-passing-tests-0-imports incident is the canonical anti-instance.

### Why the loop runs at three timescales

| Scale | Instance | Cycle length | Observation surface | Fix location |
|---|---|---|---|---|
| **Session** | OpenArms v1→v7 2026-04-09 | ~1 hour per cycle, 10 per day | Agent-report.py streams, operator review | methodology.yaml schema, hooks |
| **Runtime** | OpenFleet doctor cycle | 30 seconds | Detection functions per agent-task pair | Correction actions (TEACH/COMPACT/PRUNE) |
| **Sprint** | OpenArms E016 T107-T112 | ~1 week per spike | Past-run evidence + external research | methodology.yaml rules, harness commands |

Same loop, different temporal granularity. The pattern is scale-free — it works because at every level, the observation/fix/verify structure is what makes the next state better than the current state given feedback.

### The integration-tests-insufficient corollary

The pattern has a sharp edge case: **when the agent produces both the implementation AND the verification, the loop is closed.** OpenArms's 2026-04-09 session produced 686 passing tests across 4 epics that reached review/100% status — but nothing in the runtime imported 2073 lines of the code. The tests verified what was written, not what worked. This is NOT a failure of OFV; it is a failure of Verify-externality.

The repair: **the Verify step must cross an authority boundary.** Options in order of strength:
1. Human operator review (strongest; expensive; required at 99→100 transitions)
2. Independent automated process (CI, harness-owned gate, doctor cycle) — the authority is structural
3. Cross-agent verification (agent A writes, agent B verifies) — weaker than structural but better than self-test
4. Agent self-verification — NOT sufficient alone, but acceptable WITH an external gate downstream

## Instances

| Instance | Scale | Observe evidence | Fix location | Verify authority |
|---|---|---|---|---|
| **OpenArms v1→v7 (2026-04-09)** | 10 cycles / 1 day | Agent-report streams, per-run stage-violation counts | methodology.yaml invariants, CLAUDE.md hooks, new schema fields | Operator review + next-run compliance measurement |
| **OpenArms E016 T107-T112 (2026-03→04)** | 6 cycles / 6 weeks | Past-run logs for 5 production tasks T085-T087 | Per-class fix recommendation in findings docs | Cross-check against independent evidence + operator review |
| **Research Wiki tool-building (2026-04-15)** | 3 cycles / <1 hour | Tool-error tracebacks during real use | tools/sister_project.py + sister-projects.yaml | Next tool invocation on same inputs |
| **OpenFleet immune system (continuous)** | ∞ cycles / 30s each | Doctor detection functions on live agents | gateway-injected corrections | Agent-health profile persistence across cycles |

> [!example]- Detailed walk-through: Research Wiki's 3-cycle tool-building OFV
>
> **Observe 1**: `wiki_sister_project(openarms, summary)` crashed on `NotADirectoryError` after extending the openarms layout.
> **Fix 1**: Added `is_dir()` guard in consumption_summary loop (sister_project.py).
> **Verify 1**: Same command succeeded on rerun; returned valid JSON.
>
> **Observe 2**: After verify 1, openfleet layout keys were added but summary showed 0/23 consumed for docs.systems even though three files were consumed. Trace showed paths had `wiki/../docs/` string form that didn't match `docs/` in consumed set.
> **Fix 2**: Added `.resolve()` to `_rel_to_project` to normalize `..` segments.
> **Verify 2**: `docs.systems 1/23 consumed (4.3%)` — correctly reflects the one absorbed file.
>
> **Observe 3**: `consumption_summary` had a hardcoded layout-key list — adding docs.* to openfleet yaml didn't show new sections.
> **Fix 3**: Added `_flatten_layout_keys()` that walks the layout dict recursively.
> **Verify 3**: All declared layouts now appear in summary output across all sisters.
>
> Three cycles, three genuine bugs, three structural fixes — not patches. All in one hour. The pattern operationalized.

## When To Apply

> [!tip] Trigger conditions
>
> - You are building agent infrastructure and expecting it to be correct on v1 would be naive
> - You have runtime telemetry (stream events, logs, artifact counts, cost-per-task)
> - You have ≥2 completed runs to compare — the Verify step needs a before/after
> - The fix surface is in YOUR code (methodology.yaml, hooks, validators) — you can change the infrastructure, not just the agent's behavior
> - You are willing to version-bump the methodology and accept non-idempotent state — each fix produces a new vN

## When Not To

> [!warning] Do NOT apply when
>
> - The observation is anecdotal ("agent is slow"). OFV requires QUANTIFIED evidence.
> - The fix would be a one-off instruction to the running agent. That is correction, not fix.
> - You cannot externalize the verify step. Agent-verifies-own-fix is the closed-loop anti-pattern (integration-tests-insufficient).
> - The cycle length exceeds the opportunity window — if you get one run per month, the loop degrades to annual methodology reviews.
> - Multiple failure classes are observed simultaneously and conflated. Attack ONE class per cycle; conflation produces fixes that don't hold.

## Relationship to Other Patterns

- **[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop]]** — OFV is what the harness-owned loop IS optimizing for at runtime. The harness runs the agent (Observe), collects metrics (Observe evidence), enforces stage gates (part of Fix), and terminates/restarts (part of Verify).
- **[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense]]** — OpenFleet's doctor is OFV productionized. Line 2 (Detection) = Observe. Line 3 (Correction) = Fix. Subsequent doctor cycles = Verify.
- **[[if-you-can-verify-you-converge|If You Can Verify, You Converge]]** — OFV is the pattern that creates the verification capability the convergence lesson depends on. You can only converge if you can verify.
- **[[block-with-reason-and-justified-escalation|Block With Reason and Justified Escalation]]** — a well-designed Fix step emits escalations when the agent cannot self-correct; the operator's response becomes the next Observation.

## Open Questions

> [!question] What is the minimum cycle frequency below which the pattern degrades?
> OA ran 10 cycles/day in 2026-04-09; OF runs continuous 30s cycles; E016 ran ~1 cycle/week. Is there a floor (e.g. 1 cycle/month) below which the pattern collapses into ad-hoc patching? Open.

> [!question] Can the Verify step be chained across projects (sister-verifies-sister)?
> If OA observes a failure and fixes it in the methodology that feeds OpenFleet, does OF's subsequent run count as Verify? This would make cross-project OFV explicit. Open — this wiki's consumption-tracker tool is early infrastructure toward this.

> [!question] What makes a Fix a ROOT fix versus a symptom patch?
> Tentative criterion: a root fix is one that, if undone, causes the original failure to recur — regardless of surface details. A symptom patch suppresses one instance. Tightening needed.

## Relationships

- DERIVED FROM: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
- DERIVED FROM: [[model-methodology|Model — Methodology]]
- DERIVED FROM: [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
- BUILDS ON: [[if-you-can-verify-you-converge|If You Can Verify, You Converge]]
- RELATES TO: [[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
- RELATES TO: [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
- RELATES TO: [[block-with-reason-and-justified-escalation|Block With Reason and Justified Escalation]]
- FEEDS INTO: [[methodology-evolution-protocol|Methodology Evolution Protocol]]

## Backlinks

[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[model-methodology|Model — Methodology]]
[[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
[[if-you-can-verify-you-converge|If You Can Verify, You Converge]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[Block With Reason and Justified Escalation]]
[[methodology-evolution-protocol|Methodology Evolution Protocol]]
