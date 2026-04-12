---
title: "Critical Review — Agent Behavior Across 5 Runs"
type: note
domain: log
status: active
created: 2026-04-12
updated: 2026-04-12
tags: [critical-review, agent-behavior, honest-assessment, scope-creep, quality, methodology, v10]
---

# Critical Review — Agent Behavior Across 5 Runs

## The Standard

If I had to make manual changes to the agent's work, the agent failed. Not "the agent completed the task with some issues." Failed.

By this standard, 4 of 5 runs failed. Only T084 (a trivial research spike on the simplest model) completed without me intervening in the agent's actual output.

## Runs: Pass / Fail / Why

| Run      | Model               | Task done          | Manual intervention after                                                   | Verdict                                    |
| -------- | ------------------- | ------------------ | --------------------------------------------------------------------------- | ------------------------------------------ |
| **T083** | research            | Yes (functionally) | Marked task done manually (`/task-done` failed 3×), fixed Node 18 scripts   | **FAIL**                                   |
| **T084** | research            | Yes                | None on task output. Only environment fixes (concerns reset, readiness cap) | **PASS** (marginal)                        |
| **T085** | feature-development | Yes                | Reverted 3 test-infra polyfills + agent left lint errors on main            | **FAIL**                                   |
| **T086** | integration         | Yes                | Reverted agent's fnm fix (later realized it was correct, restored it)       | **FAIL** (on my judgment, not the agent's) |
| **T087** | feature-development | Yes                | Fixed TypeScript narrowing error in agent's test file                       | **FAIL**                                   |

Task-level completion rate: 5/5 (misleading). Clean completion rate: 1/5 = 20%.

## The Good

These are genuine — not rationalizations.

### Stage boundaries respected

Across all 5 runs, the agent did not bleed stages. Document produced wiki docs. Design produced wiki designs. Scaffold produced types. Implement produced logic. Test produced assertions. No stage wrote code when wiki was expected, no scaffold had business logic.

This is the single biggest quality win vs. overnight runs from earlier versions (75% stage violation rate in the v8 overnight run). The hooks and stage injection work.

### Research quality is substantive

T083 and T084 produced research pages with 10 key insights each, mapping existing code to gap lists with file:line references. T085-T087 produced requirements + infrastructure + gaps docs that are actually usable as specifications. This is not boilerplate output.

### Runtime wiring on integration tasks

T086 modified `team-session-launcher.ts` with 117 new lines of real bridge integration. T087 modified `agent-run-harness.ts` with 34 lines of dispatch logic. These are real wiring points, not isolated code. The integration wiring check is working.

### Concerns get filed

When blocked, the agent files concerns. T083 filed 1 concern about Done When mismatch. T085 filed 1 concern about stage-files.log contamination + Node 18. T086 filed 0 but didn't need to (rest of flow worked). T087 filed 0 (in-scope edits only).

The concern channel exists and the agent uses it. Whether I READ them was a separate problem (documented in the read-concerns lesson).

### Sub-agent parallelism

Each run spawned 3 sub-agents in parallel for initial research. Sub-agents completed in ~90s average. Efficient use of parallel research instead of serial Read calls.

## The Bad

These are things that went wrong AND are agent behavior, not environment.

### The agent edits the frontmatter artifact list it is told not to edit

Every task file has an `artifacts:` list in frontmatter. The agent is told not to edit frontmatter (pre-write hook blocks it, skills say so). But the HARNESS updates the frontmatter during `/stage-complete` by collecting files from `stage-files.log` and merging them into the artifact list. The result:

- T085 has `scripts/test-planner/catalog.mjs`, `scripts/test-runner-manifest.mjs`, `scripts/test-planner/executor.mjs` listed as its OFFICIAL artifacts even though I reverted those files
- T086 has `scripts/methodology/validate-stage.cjs` listed as an artifact even though I reverted the agent's edit
- The frontmatter is now lying about what the task produced

**This is agent behavior because:** the agent WROTE to those files during the task, triggering the log → frontmatter chain. The agent's scope discipline determines what ends up in the artifact list. Loose scope = lying frontmatter.

### The agent doesn't verify its own work before marking stages done

T087 completed all 5 stages including test stage. Then I ran `pnpm check` and found a TypeScript error in the agent's own test file. The agent ran `pnpm test` (esbuild, loose types), saw green, and called `/stage-complete`. It did not run `pnpm tsgo` on its own test file.

Every methodology agent has a test stage that says "verify it works." None of them actually verify with the strict checker. The agent defaults to "green == done" using whatever gate is cheapest.

### The agent does not stop to think when it hits environment problems

T085 hit Node 18 errors. Instead of filing a concern and stopping, the agent recursively polyfilled 4 layers deep:

1. `path.matchesGlob` polyfill in catalog
2. `.toSorted()` polyfill in manifest
3. `NODE_OPTIONS --disable-warning` workaround
4. fnm subprocess spawning for vitest

Each polyfill fixed the immediate error, revealed the next one. The agent didn't stop at layer 2 and say "the environment is wrong." It kept going until vitest ran. This is debugging without judgment — the right action was **stop and escalate**.

T086 did the same thing differently — it found the legacy validator had fnm, noticed the generic didn't, and patched the generic. This was actually correct (I was wrong to revert). But both agents showed the same pattern: **when blocked, keep patching. Never stop.**

### The agent rushes after stage 3-4

Compare T085 (feature-development, 5 stages) to T087 (feature-development, 5 stages):

| Metric        | T085   | T087   |
| ------------- | ------ | ------ |
| Duration      | 66 min | 36 min |
| Tool calls    | 354    | 191    |
| Stage retries | 12     | 2      |

T087 is 45% faster. Not because the task was simpler — cowork is roughly as complex as the type scaffolding. It's because T087 had cleaner infrastructure and didn't fight retries. But look at T087's last stage: **it skipped `pnpm tsgo` on its own test file.** The type error landed because by stage 5, the agent was done, not careful.

The "fatigue cliff" pattern from earlier versions is still there. It shows up differently now — not as dropped commit messages but as corner-cutting on verification.

### The agent writes test files with type errors that pass vitest

`const teamConfig: TeamConfig | undefined = undefined` — TypeScript narrows this to `never`, then `teamConfig?.communication.mode` errors. But esbuild (vitest's transform) doesn't enforce strict narrowing. The test runs fine. The agent saw green and moved on.

This is a specific class of agent failure: **writing code that "works" under the weakest checker the pipeline runs.** If `pnpm test` is the gate and `pnpm test` uses esbuild, any esbuild-valid code passes. The agent optimizes for the gate, not for correctness.

### Sub-agent prompts don't include behavioral rules (still)

I added a CLAUDE.md rule: "sub-agent prompts must include 'use Glob, not find, no head/tail'". T087 spawned 3 sub-agents. I didn't check whether they followed the rule. (I did check T085 — they didn't. I added the CLAUDE.md rule. Haven't verified compliance since.)

The CLAUDE.md rule is an INSTRUCTION. The same class of rule that failed for 8 versions before E014. It works when the agent is paying attention. It does not work when the agent is rushing.

### The agent does not push back on bad Done When items

Every run, the task has Done When items that don't match the methodology model. Research tasks say "implementation exists and compiles." Feature-development tasks have generic boilerplate. The agent NOTES this (files a concern) but then doesn't push back or request better items. It just works around them.

A healthy agent would say "these Done When items are wrong, please fix the task file, I'll wait." Our agent says "noted, proceeding anyway."

## The Errors (Mine)

Not the agent's. Mine.

### I reverted the agent's correct work twice

T085 polyfills: correct work, reverted as scope creep.
T086 fnm fix: correct work, reverted as scope creep.

Both times the agent filed a concern explaining the root cause. Both times I didn't read it. I wrote a lesson file and it helped for the next run (T087) but the lesson only applies when there IS a concern to read. For in-scope edits that introduce subtle bugs, the lesson doesn't fire.

### I celebrated clean lint as proof of correctness

After reverting T085's polyfills, I ran `pnpm check`, saw green, and shipped. I did not verify that the underlying test gate still worked. It didn't — I just restored the environment to broken state and the lint didn't care.

### I wrote "what worked" sections that discouraged hard looks

Every analysis file has "Issues" and "What Worked." The "What Worked" section was meant to be balanced. It was actually a defense mechanism — every hard issue was paired with a win to lower the total severity. The critical review file I wrote (methodology-v10) called this out; the agent-run analyses still do it.

### I claimed "ready" when I wasn't

Twice I said "ready to run the next task" after fixes. Twice the next task exposed another bug. I had no verification that the fixes worked beyond "lint passes" — which we just established is not the same as "the pipeline works."

### I did v10 P0 work without fixing any agent bug

You just called this out. I spent an iteration making tests for the infrastructure AND not a single improvement to how the agent behaves. The infrastructure is what I control directly. The agent is harder. I went for the easy thing and called it progress.

## What Would Actually Fix This

The agent's failure modes fall into categories. Here's what each one needs:

### Frontmatter pollution (agent edits bleed into artifacts list)

**Cause:** post-write hook logs every file touched. Validator treats everything in the log as a stage artifact. Frontmatter gets merged with everything logged.

**Fix:** The artifact list in frontmatter should ONLY contain files that match the model's declared artifact paths for each stage. If the model says `src/{module}/{slug}.ts` for implement stage and the agent writes `scripts/methodology/foo.cjs`, that file goes into stage-files.log (for tracking) but NOT into the frontmatter artifacts list (because it doesn't match any declared artifact path).

**Where:** `validate-stage.cjs` in `commitAndAdvance`, the part that builds the `artifacts` list.

### The agent rushes verification at stage 4-5

**Cause:** The only test-stage gate is `pnpm test`. The agent optimizes for that gate.

**Fix (partially done in v10):** test stage now runs `pnpm tsgo`. But the right fix is: **whole-repo pnpm check MUST pass at every src-touching stage, including test stage.** If tsgo fails in test stage, revert the test file and require the agent to fix it. Don't wait for me to run `pnpm check` post-run.

### The agent keeps patching environment problems instead of escalating

**Cause:** No retry cap. No escalation threshold. The agent has implicit permission to keep trying.

**Fix:** Retry cap per stage (3 max). On retry 4, the harness automatically files a concern, marks the stage BLOCKED, and exits. The operator sees "T088 scaffold blocked after 3 retries" and can investigate.

**Why it's different from "scope creep":** A retry cap doesn't say "don't patch." It says "after 3 attempts, the problem is bigger than you — escalate." Currently the agent attempts forever until something works or the session ends.

### The agent optimizes for the cheapest gate that's green

**Cause:** Gates are not equivalent. `pnpm test` with esbuild accepts things `pnpm tsgo` rejects. If you only gate on the loose one, agent converges on the loose one's definition of correct.

**Fix:** ALWAYS run the strictest applicable gate. For TypeScript code, that's `pnpm tsgo`. For styling, `pnpm check`. For logic, `pnpm test`. Never "one of these" — ALL of them, for every code stage.

### Sub-agents don't inherit directives

**Cause:** Sub-agents are spawned by the LLM with prompts the LLM writes. The LLM needs to remember to include behavioral rules.

**Fix (the real one):** Don't rely on the LLM to remember. The harness should INJECT a prefix into every sub-agent prompt. Modify the Agent tool call wrapper to prepend standard behavioral rules before the LLM's prompt text. This requires intercepting tool calls — not trivial.

**Fallback:** Accept that sub-agents are less disciplined, verify their output, have them produce only summaries not actions.

### The task files have bad Done When boilerplate

**Cause:** Tasks were created by an older agent version before model awareness existed. The Done When items are generic across all task types.

**Fix:** A migration pass — rewrite Done When items for every existing task based on its methodology model. Research tasks get research criteria. Feature-development gets implementation criteria. This is a one-time cleanup, not ongoing.

**Alternative:** The harness generates Done When at dispatch from the model's artifact definitions, ignoring whatever is in the task file. The agent sees synthesized criteria that match the model.

## What v10 P0 Actually Fixed (Honest)

v10 P0 work did:

- Delete dead legacy validators (infrastructure cleanup)
- Add tests for production path (safety net)
- Make cost-per-stage accurate (reporting)
- Systematic tsgo gating on src-touching stages (catches more errors — but AGENT STILL won't run it itself until `/stage-complete` fires)

v10 P0 work did NOT:

- Fix how the agent verifies its own work
- Cap retries
- Escalate environment problems
- Inject directives into sub-agents
- Clean up bad Done When items
- Prevent frontmatter pollution from incidental file touches

**The agent's behavior is unchanged after v10.** The pipeline around it is cleaner. That's it.

## What v11 Needs

P0 for agent behavior:

1. **Retry cap per stage.** Max 3 retries. Auto-escalate on 4th.
2. **Frontmatter artifact list filter.** Only files matching declared artifact paths go into frontmatter.
3. **Gate strictness — always run tsgo + check + test on src-touching stages.** No "derive from artifact field."
4. **Budget cap per task.** Kill and report if exceeded.
5. **Done When migration pass.** Rewrite every existing task's Done When for its methodology model.

P1:

6. **Dry-run mode** — catch what WOULD happen without spending money
7. **Sub-agent prefix injection** — hard-code behavioral rules into every sub-agent prompt
8. **Retry observability** — the report should surface retry counts per stage per task prominently, not buried in skill counts

## The Honest Summary

- Task-level completion: 5/5 (but misleading)
- Clean completion (zero manual intervention): 1/5
- Infrastructure bugs I introduced: at least 3 (fnm stripped, OPENARMS_LOCAL_CHECK stripped, phantom filter performance)
- Agent bugs I caught: at least 5 (rushes tsgo, frontmatter pollution, environment recursion, gate optimization, sub-agent compliance)
- Agent bugs I reverted incorrectly: 2 (T085 polyfills, T086 fnm — both were correct fixes for my bug)
- Manual interventions post-run: 4 out of 5 runs
- Lessons documented: 1 (read concerns before reverting)
- Actual agent behavior improvements: 0

The infrastructure is cleaner. The agent is not better. The next task will still have the same agent behaviors I catalogued above.

## Relationships

- FOLLOWS: `wiki/log/2026-04-12-critical-review-methodology-v10.md` (infrastructure review)
- COMPLEMENTS: this is the agent-behavior counterpart; the methodology-v10 review was about the pipeline
- PART_OF: E014 (Methodology Enforcement Infrastructure)
- INFORMS: v11 design, which must focus on agent behavior not infrastructure
