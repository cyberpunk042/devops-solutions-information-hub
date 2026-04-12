---
title: "Methodology Evolution — v9 → v10 → v11 (in progress)"
type: note
domain: log
status: active
note_type: evolution
created: 2026-04-12
updated: 2026-04-12
tags: [methodology, evolution, v10, v11, harness, agent-behavior, comparison, lessons]
---

# Methodology Evolution — v9 → v10 → v11 (in progress)

Continuation of `wiki/log/2026-04-11-methodology-evolution-v9.md`.

## Version History Update

| Version | Date       | Shift                                      | Driver                                                                                                                     |
| ------- | ---------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| v1-v7   | 2026-04-09 | Prompt iterations                          | See `wiki/log/2026-04-09-methodology-evolution.md`                                                                         |
| v8      | 2026-04-10 | Overnight run findings                     | 12 systemic failures, instruction-based enforcement proven broken                                                          |
| v9      | 2026-04-11 | Infrastructure enforcement                 | Harness-owned loop, commands/skills/hooks, document chain, business logic detection. Proven on T068+T069.                  |
| v10     | 2026-04-12 | Adaptive pipeline + real cost              | Model-aware validation, legacy deletion, cost-per-stage, stage-files phantom filter, fnm wrapping. Drove 5 runs T083-T087. |
| v11     | 2026-04-12 | Agent behavior investigation (IN PROGRESS) | E016 + 6 research spikes to fix agent failure classes, not infrastructure.                                                 |

## What Changed: v9 → v10

### The bugs v9 left in production

v9 shipped working but had known rough edges that only surfaced when T083-T087 ran on it. The 5 runs revealed **14 bugs** documented in `wiki/log/2026-04-11-agent-run-T083-analysis.md` through `wiki/log/2026-04-12-agent-run-T087-analysis.md`:

| Bug                                         | v9 behavior                                                                        | v10 fix                                                                         |
| ------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| readiness_cap ignored                       | validate-stage capped at 99 regardless of model                                    | read `readinessCap` from `current-model-config.json`                            |
| Done When stage checks impossible           | verify-done-when checked `implement` stage for research tasks (no implement stage) | skip stage checks when model doesn't have that stage (`model_na`)               |
| `required_content` prose treated as heading | validator required "At least 2 options compared" as a literal `##` heading         | only validate items starting with `##`                                          |
| Hardwired stage switch                      | 5 per-stage functions (`validateDocument/Design/Scaffold/Implement/Test`)          | generic `validateStageGeneric` driven by model config; legacy functions deleted |
| Stage-files.log phantoms                    | reverted files stayed in the log, validator treated them as artifacts              | filter by `git diff/status/log` against the current task                        |
| fnm wrapper missing                         | `validateStageGeneric` ran `pnpm test` under shell Node 18, tests failed           | `eval "$(fnm env)"; fnm use default` prefix on all gate commands                |
| OPENARMS_LOCAL_CHECK missing                | memory-bounded flag not set in generic validator                                   | prefix on `pnpm tsgo` and `pnpm check`                                          |
| Cost per stage blown                        | token estimator ≠ real billed cost, percentages > 100%                             | scale estimates proportionally to `result.total_cost_usd`                       |
| Harness no run_completed event              | report parser couldn't detect clean end                                            | emit `run_completed` at end of run                                              |
| Commit message lies                         | "→ done" commit message when stage-complete passed all but /task-done failed       | message says "→ all-stages-complete" until /task-done succeeds                  |
| concerns.json carryover                     | not reset between tasks, prior concerns appeared in next task's log                | reset at `initStateDir`                                                         |
| Sub-agent anti-patterns                     | `find \| head` in sub-agent prompts                                                | CLAUDE.md rule (instruction-level, unreliable)                                  |
| No test for generic path                    | 16 tests covered legacy per-stage functions, `validateStageGeneric` had 0          | rewrite test file to cover `validateStageGeneric` with mocked gate commands     |
| Task prompt injection missing               | agent discovered its task from skill injection, not explicit user message          | deferred — agent runs found it regardless                                       |

### Architecture shift

| Aspect                  | v9                                      | v10                                                                |
| ----------------------- | --------------------------------------- | ------------------------------------------------------------------ |
| Stage validation        | 5 per-stage hardcoded functions         | 1 generic function reads model artifacts                           |
| Stage gate selection    | each function decides its gates         | derived from what the stage TOUCHED (src → tsgo, test → tsgo+test) |
| Readiness calculation   | capped at 99 always                     | respects model `readinessCap` (e.g. research: 50)                  |
| Done When verification  | checks implement stage on all models    | aware of applicable stages per model                               |
| Test coverage           | tests covered dead legacy code          | tests cover production generic path                                |
| Cost measurement        | token estimate, could exceed real total | scaled to real billed total                                        |
| validate-stage.cjs size | 1416 lines (legacy + generic)           | 1006 lines (generic only)                                          |

### What v10 did NOT fix

The operator called this out directly after v10 P0 shipped:

> "WTF ARE YOU TALKING ABOUT ???? WE DID NOT EVEN FIX ANY BUG ABOUT THE AGENT !?????"

v10 cleaned up the pipeline. It did not touch the agent's behavior. The 6 agent failure classes catalogued in `wiki/log/2026-04-12-critical-review-agent-behavior.md` remained:

1. Frontmatter artifact pollution
2. Corner-cutting verification at final stages
3. Environment-patching without escalation
4. Weakest-checker gate optimization
5. Sub-agent directive compliance
6. Done When boilerplate acceptance

v10 was infrastructure cleanup. v11 has to be agent behavior.

## Comparison: v9 runs vs v10 runs

### T068+T069 (v9, 2026-04-11)

| Metric             | T068        | T069                |
| ------------------ | ----------- | ------------------- |
| Model              | integration | feature-development |
| Stages             | 3           | 5                   |
| Cost               | $9.57       | $7.49               |
| Duration           | 13 min      | 30 min              |
| Stage compressions | 0           | 0                   |
| Commits separated  | yes         | yes                 |

### T083-T087 (v10, 2026-04-11/12)

| Metric              | T083        | T084     | T085                | T086        | T087                |
| ------------------- | ----------- | -------- | ------------------- | ----------- | ------------------- |
| Model               | research    | research | feature-development | integration | feature-development |
| Stages              | 2           | 2        | 5                   | 3           | 5                   |
| Cost                | $2.87       | $1.88    | $27.27              | $7.33       | $11.46              |
| Duration            | 11.7 min    | 8.2 min  | 66 min              | 24.5 min    | 36.2 min            |
| Stage retries       | 2           | 0        | 12                  | 4           | 2                   |
| Post-run manual fix | yes         | no       | yes                 | yes         | yes                 |
| Task status         | INTERRUPTED | DONE     | DONE                | DONE        | DONE                |

### Clean completion rate

v9: 2 of 2 runs clean (T068, T069). But: tested on only 2 tasks, both mature infrastructure, no edge cases.

v10: 1 of 5 runs clean (T084 only — trivial research spike on clean concerns state). Every feature-development or integration run needed post-run intervention.

**The v10 infrastructure is cleaner than v9, but the run reliability got WORSE because v10 exposed agent behavior issues v9 had masked.** v9 never ran a feature-development task under the adaptive validator — there was no adaptive validator. v10 did, and the agent's behavior under pressure became visible.

## What Changed: v10 → v11 (in progress)

### Driver

`wiki/log/2026-04-12-critical-review-agent-behavior.md` — honest assessment by the standard "if I had to make manual changes, the agent failed." 4 of 5 runs failed. v10 fixed zero agent bugs.

### Approach

Pass each failure class through the methodology itself. Not a rush-fix. E016 "Agent Behavior Investigation" with 6 research spikes (T107-T112), each producing:

1. A research page with observed evidence (line-level citations from run logs)
2. A findings doc with ≥2 options compared, recommendation with rationale

No implementation in E016. Implementation goes to a follow-up epic (E017) after all 6 findings are reviewed together.

### T107 (first v11 research run)

| Metric              | Value                                                                                  |
| ------------------- | -------------------------------------------------------------------------------------- |
| Duration            | 7.7 min                                                                                |
| Cost                | $1.91                                                                                  |
| Tool calls          | 105                                                                                    |
| Sub-agents          | 3                                                                                      |
| Stage retries       | 1 (validator bug — fixed in same session)                                              |
| Manual intervention | fix validator bug, rename extra design doc                                             |
| Artifacts produced  | 3 (research + findings + extra design doc)                                             |
| Research quality    | specific line citations, 4 options compared across 7 criteria, concrete recommendation |

Findings from T107: environment-patching escalation failure has a combined root cause (40% prompt / 40% infrastructure / 20% model). Recommended layered fix: stage retry cap (Option A) + environment pre-flight gate (Option B).

### v11 bugs found so far

| Bug                                           | v10 behavior                                                      | v11 fix                                                    |
| --------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| Validator required_content in EVERY wiki file | failed when agent produced primary + supporting docs              | at least ONE wiki file must match the artifact             |
| methodology.yaml research findings-doc path   | `{slug}-research.md` (confusing — research is the document stage) | renamed to `{slug}-findings.md` (matches semantic purpose) |

Both fixes landed before T108 runs. See commit `8beb2f59`.

### v11 agent behavior investigations remaining

| Task | Failure class                               | Status                                                     |
| ---- | ------------------------------------------- | ---------------------------------------------------------- |
| T107 | Environment-patching escalation             | DONE — 4 options recommended, layered fix                  |
| T108 | Corner-cutting verification at final stages | IN PROGRESS                                                |
| T109 | Frontmatter artifact pollution              | not started                                                |
| T110 | Weakest-checker gate optimization           | not started                                                |
| T111 | Sub-agent directive compliance              | not started                                                |
| T112 | Done When boilerplate acceptance            | not started (partially confirmed by T107 execution itself) |

## Lessons From v10

### Lesson: Don't revert agent infrastructure edits without reading concerns

Two consecutive iterations (T085, T086), the agent correctly diagnosed and fixed a bug I introduced in iteration 1 (stripped fnm wrapper from `validateStageGeneric`). Both times I reverted the fix calling it "scope creep." Both times the agent filed a concern explaining the root cause. Both times I didn't read the concern before reverting.

Full lesson: `wiki/domains/learnings/lesson-read-agent-reasoning-before-reverting.md`

### Lesson: The agent optimizes for the cheapest gate that's green

T087 landed a TypeScript narrowing error on main because the agent ran `pnpm test` (esbuild, loose), saw green, and called `/stage-complete`. It did not run `pnpm tsgo` on its own test file. This is not "laziness" — it's the agent optimizing for whatever gate the pipeline actually runs. If the gate is loose, correct-per-gate is not correct-per-product.

Fix applied: v10 test stage now runs `pnpm tsgo` before `pnpm test`. But the deeper fix is to investigate the pattern (T110).

### Lesson: "Stuck after 3 attempts" rule doesn't fire for progressive patching

The agent directive has a soft rule: "If you're stuck after 3 attempts, explain what you tried." This works for repeated failures of the same action. It does NOT fire for cascading workarounds where each individual patch succeeds. T085 polyfilled 4 layers of Node compat — never felt stuck, never hit the rule. Full analysis in T107 findings doc.

### Lesson: Agent silently resolves task/model conflicts instead of pushing back

T107 execution hit a conflict between the task's Done When (asking for `-findings.md`) and methodology.yaml's spec (asking for `-research.md`). The agent produced BOTH files. It did not file a concern. This is the T112 failure pattern — empirically confirmed by T107's own execution before T112 runs.

### Lesson: Infrastructure fixes masquerading as progress

The operator called this out after v10 P0 landed:

> v10 P0 work did: delete dead code, add tests for production path, make cost accurate, systematic tsgo gating.
> v10 P0 work did NOT: fix how the agent verifies its own work, cap retries, escalate environment problems, inject directives into sub-agents, clean up bad Done When items, prevent frontmatter pollution.

The pipeline is cleaner. The agent is not better. Version numbers should track agent improvement, not pipeline polish.

## Metrics That Track Progress

### Clean completion rate

The standard: if I had to change the agent's work post-run, the agent failed.

| Version         | Runs | Clean             | Rate                |
| --------------- | ---- | ----------------- | ------------------- |
| v8 overnight    | 8    | 0                 | 0%                  |
| v9 (T068, T069) | 2    | 2                 | 100% (small sample) |
| v10 (T083-T087) | 5    | 1                 | 20%                 |
| v11 (T107)      | 1    | 0 (validator bug) | 0% (sample of 1)    |

v11's first run hit a v10 validator bug, not an agent bug. The agent's work itself was clean. If the validator bug hadn't fired, T107 would have been clean. Sample size too small to conclude.

### Cost trajectory

For feature-development model (5 stages):

| Run                     | Cost   | Retries |
| ----------------------- | ------ | ------- |
| T069 (v9)               | $7.49  | unknown |
| T085 (v10, first)       | $27.27 | 12      |
| T087 (v10, after fixes) | $11.46 | 2       |

T085 was the worst run of the session — early v10 had fnm stripped, Node 18 issues cascaded, agent patched recursively. T087 after iteration 4 fixes was clean on environment and retried only because of the tsgo-in-test gap. The real cost floor for feature-development tasks under v10 is somewhere between $7 and $12 depending on task shape.

### Research task baseline

For research model (2 stages):

| Run        | Cost  | Duration |
| ---------- | ----- | -------- |
| T083 (v10) | $2.87 | 11.7 min |
| T084 (v10) | $1.88 | 8.2 min  |
| T107 (v11) | $1.91 | 7.7 min  |

Research tasks are stable around $2 and 8-12 minutes. The v10 infrastructure improvements didn't make them meaningfully faster, but they made them reliably clean (T084, T107).

## Relationships

- FOLLOWS: `wiki/log/2026-04-11-methodology-evolution-v9.md`
- FOLLOWS: `wiki/log/2026-04-09-methodology-evolution.md`
- DRIVER: `wiki/log/2026-04-12-critical-review-methodology-v10.md` (v10 P0 gaps)
- DRIVER: `wiki/log/2026-04-12-critical-review-agent-behavior.md` (v11 target)
- PART_OF: E014 (Methodology Enforcement Infrastructure)
- NEXT: E016 completion + E017 design for agent behavior fixes
