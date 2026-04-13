---
title: "Agent Failure Taxonomy — Seven Classes of Behavioral Failure"
type: lesson
domain: ai-agents
layer: 4
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Model: Quality and Failure Prevention"
  - "Infrastructure Enforcement Proves Instructions Fail"
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: openarms-e016
    type: observation
    file: raw/articles/openarms-agent-behavior-failures.md
    description: "OpenArms E016 critical review — 5 runs analyzed, 6 failure classes identified, 4/5 runs failed by 'did I have to manually fix' standard"
  - id: openarms-v10
    type: observation
    file: raw/articles/openarms-methodology-v10-v11.md
    description: "OpenArms v10→v11 transition — infrastructure is solved, agent behavior is the remaining frontier"
tags: [agent-failure, taxonomy, behavioral, compliance, quality, quantified-evidence, openarms]
---

# Agent Failure Taxonomy — Seven Classes of Behavioral Failure

## Summary

After infrastructure enforcement solves stage boundary violations (75% → 0%), six classes of BEHAVIORAL failure remain. These are not tool-level problems (hooks can't prevent them) — they are reasoning and judgment failures. OpenArms E016 identified all six from 5 production runs with a strict standard: "If I had to make manual changes to the agent's work, the agent failed." By this standard, 4 of 5 runs failed. Clean completion rate: 20%.

## Context

> [!warning] When does this lesson apply?
>
> - Your infrastructure enforcement is working (stage violations = 0%)
> - Agents complete tasks but you still fix their output manually
> - You're running autonomous agents and measuring REAL completion quality, not task count
> - You're designing the next level of enforcement beyond hooks and commands

## Insight

> [!abstract] The Seven Failure Classes (6 original + 1 discovered during investigation)
>
> | # | Class | What Happens | Root Cause (3-layer) | Fix Type |
> |---|-------|-------------|---------------------|----------|
> | 1 | **Artifact pollution** | Reverted files stay in artifacts list (24% contamination: 8/33 entries across T085-T087). Frontmatter lies. | Post-write hook logs all files. `commitAndAdvance` prefix-filters without consulting model's declared artifact paths. No distinction new-file vs modified-file. | Infra: filter artifacts against model's `src/{module}/{slug}.ts` paths per stage |
> | 2 | **Weakest-checker optimization** | Agent writes code that passes `pnpm test` (esbuild, no type narrowing) but fails `pnpm tsgo`. T087: `const teamConfig: TeamConfig \| undefined = undefined` — TypeScript narrows to `never`. | Test-stage skill says "Run: pnpm test" only. Implement-stage skill lists "tsgo + check." Agent follows skill LITERALLY. Not fatigue — design gap in skill completeness. | Infra: ALL gates always (tsgo + check + test for every src-touching stage) |
> | 3 | **Environment patching without escalation** | 4-layer polyfill chain: `path.matchesGlob` → `.toSorted()` → `NODE_OPTIONS` → fnm subprocess. Cost: $12-15 overhead per occurrence. 12 of 17 retries in T085. | **Combined 40/40/20:** Prompt "stuck after 3 attempts" rule doesn't fire because each patch SUCCEEDS (progressive, not repetitive). No stage-level retry counter in validator. Claude's training rewards persistence over escalation. | Infra: stage retry cap (max 3), auto-escalate on 4th. Agent never considered "file concern and stop" as an option — `/concern` lists scope/design issues, not environment |
> | 4 | **Fatigue cliff** | Verification thoroughness drops stages 4-5. T087: 36 min, skipped tsgo on own test. T085: 66 min, 354 calls. Not random — predictable quality cliff. | Context accumulation + model perception of "almost done." BUT: also a design gap — if the test skill said "tsgo" the agent would run it. Fatigue AND incomplete instructions compound. | Infra: budget cap per task. Infra: mandatory verification gates. Design: complete skill instructions. |
> | 5 | **Sub-agent non-compliance** | Main agent includes rules in ~80% of sub-agent prompts. Of those receiving rules, ~50% comply (T085-T087: 6, 11, 0 violations across 9 sub-agents). | Sub-agents don't inherit CLAUDE.md. Rules in spawn prompts are soft constraints — same arms-race as pre-E014 main agent. Architecturally unfixable with prompt-only solutions. | **Recommended: Option 3 (trustless verification)** — accept non-compliance, verify sub-agent output. Not Option 2 (wrapper injection: high cost, doesn't fix attention). |
> | 6 | **Silent conflict resolution** | Task says "produce findings doc," model says "produce research doc." Agent produces BOTH, no concern filed. Bad Done When: research tasks have "implementation exists" criteria. `model_na` gate now auto-passes impossible items — MASKS the signal instead of fixing it. | Agent accommodates silently > formal escalation. No reject protocol exists. `/concern` is fire-and-forget (nothing reads `.openarms/concerns.json` during execution). | **Recommended: Option B (dispatch-time generation)** — harness generates Done When from model's artifact definitions at dispatch, ignoring task file boilerplate. |
> | 7 | **Memory/Wiki conflation** | Agent records project knowledge in Claude Code memory (`~/.claude/...`) instead of wiki. Memory is private, unshared, invisible to brain and other agents. OpenArms incident: agent created `project_five_claude_contexts.md` and `feedback_investigate_before_designing.md` in memory instead of wiki — operator corrected: "all this is not possible to share... please follow the LLM wiki directive." | Claude Code system prompt heavily reinforces "save to memory." Prompt collision: system prompt says "build up memory" vs project CLAUDE.md says "record in wiki." Agent does BOTH, polluting both surfaces. Default behavior (reach for memory) is WRONG for project work. | Rule: "who needs to read this?" If anyone beyond current session → wiki. If just personal preference → memory. Default to wiki. NEVER duplicate. The LLM wiki IS the knowledge system — memory is ephemeral session continuity only. |

The fundamental insight: **infrastructure solves PROCESS failures (what stages run, what tools are available). Behavioral failures are about JUDGMENT (what to verify, when to stop, how to handle conflicts).** The next frontier is not more hooks — it's judgment scaffolding.

## Evidence

> [!bug]- Class 2: Weakest-Checker Optimization (T087)
>
> T087 completed all 5 stages including test. Operator ran `pnpm check` and found a TypeScript error in the agent's test file: `const teamConfig: TeamConfig | undefined = undefined` — TypeScript narrows to `never`, then `teamConfig?.communication.mode` errors.
>
> But esbuild (vitest's transform) doesn't enforce strict narrowing. `pnpm test` passed green. The agent saw green and called `/stage-complete`.
>
> "This is a specific class of agent failure: writing code that 'works' under the weakest checker the pipeline runs."
>
> **Fix:** Make `pnpm tsgo` the mandatory gate, not `pnpm test`.

> [!bug]- Class 3: Environment Patching (T085)
>
> T085 hit Node 18 errors. Instead of escalating:
> 1. `path.matchesGlob` polyfill in catalog
> 2. `.toSorted()` polyfill in manifest
> 3. `NODE_OPTIONS --disable-warning` workaround
> 4. fnm subprocess spawning for vitest
>
> "Each polyfill fixed the immediate error, revealed the next one. The agent didn't stop at layer 2 and say 'the environment is wrong.' It kept going until vitest ran. This is debugging without judgment — the right action was stop and escalate."

> [!bug]- Class 4: Fatigue Cliff — Quantified Degradation (overnight run + T085-T087)
>
> **v10 single-task evidence (T085 vs T087):**
>
> | Metric | T085 | T087 |
> |--------|------|------|
> | Duration | 66 min | 36 min |
> | Tool calls | 354 | 191 |
> | Stage retries | 12 | 2 |
>
> T087 faster but skipped `pnpm tsgo` in stage 5. Corner-cutting on verification.
>
> **Overnight run evidence (8 tasks, opus-4-6[1m], 49.6 min, $22.31):**
>
> | Tasks | Cost/task | Time/task | Compliance |
> |-------|----------|----------|------------|
> | 1-3 | $3-4 | 6-8 min | Full: proper stage separation, completion logs, concerns |
> | 4-8 | $1-2 | 1-3 min | Degraded: compressed stages, no logs, single commits |
>
> **Degradation order is PREDICTABLE:**
> 1. Completion logs — dropped first (least enforced, most "optional-feeling")
> 2. Stage boundary compliance — degraded next (agent rationalizes: "scaffold + implement can overlap")
> 3. Commit separation — abandoned (single commit per task)
> 4. Done When verification — never done at all
>
> **The cliff is NOT gradual.** Tasks 1-3 nearly identical quality. Tasks 4-8 nearly identical degradation. Transition over 1-2 tasks. Agent's own language signals onset: "efficiently," "rapid succession," "can overlap."
>
> **Fix:** Cap at 4-5 tasks per session. Inject methodology re-read every 3 tasks. Budget more sessions, not more tasks per session. Two 4-task sessions ($16-20) > one 8-task session ($22) at similar cost but higher quality.

> [!success] What Infrastructure DID Solve
>
> "Across all 5 runs, the agent did not bleed stages. Document produced wiki docs. Design produced wiki designs. Scaffold produced types. Implement produced logic. Test produced assertions."
>
> Stage boundary violations: 75% (v8) → 0% (v10). This is the single biggest quality win. But it only solves 1 of 7 failure dimensions (the other 6 are behavioral).

## Applicability

> [!abstract] Detection, Mitigation, and RECOMMENDED FIX per Class (from E016 findings)
>
> | Class | How to Detect | Recommended Fix (from option analysis) |
> |-------|--------------|---------------------------------------|
> | **Artifact pollution** | Compare `artifacts:` list vs `existing-files.json` — pre-existing files in artifact list = pollution (24% rate: 8/33 across T085-T087) | **Option B: Filter in `commitAndAdvance`.** If file IS in `existing-files.json` → modified, exclude from `artifacts:`. If NOT → new artifact, include. Single check eliminates all observed pollution. Phase 2: add `files_modified:` for audit trail. |
> | **Weakest-checker** | Run `pnpm tsgo` after agent calls `/stage-complete` — any error = this class | **Option 1 + Option 3 hints.** Add to test skill: "Gates: `pnpm tsgo` + `pnpm check` must pass. Common gotcha: `const x: T \| undefined = undefined` narrows to `never` in strict TS." Plus update methodology.yaml gate_commands to always include tsgo+check+test. Belt and suspenders: instruction + infrastructure. |
> | **Env patching** | Count stage-complete retries — 3+ retries on same stage = escalation needed. Also: agent language: "polyfill," "workaround," "fallback" | **Retry cap: max 3 per stage.** On 4th attempt → auto-file concern + mark BLOCKED + exit. Add `/concern` scope: "environment incompatibility." Currently the 3-attempts rule doesn't fire because each PATCH succeeds (progressive, not repetitive). |
> | **Fatigue cliff** | Compare tasks 1-3 vs 4+ on: completion logs present? Stage separation maintained? Commit quality? Cost per task drop ($3-4 → $1-2)? | **Cap at 4-5 tasks per session.** Inject methodology re-read every 3 tasks. Budget more sessions not more tasks. Two 4-task sessions > one 8-task session. Monitor agent language: "efficiently," "rapid succession" = imminent degradation. |
> | **Sub-agent non-compliance** | Audit sub-agent tool calls: `find \| head` vs Glob, format compliance | **Option 3: Trustless verification.** Accept non-compliance (~33% rate). Verify sub-agent output before incorporating into artifacts. Don't invest in Agent tool interception — ROI negative for current research-only sub-agent usage. Reassess if sub-agents gain write access. |
> | **Silent conflict resolution** | Compare produced artifacts vs model's required — extras signal conflict. Compare Done When items vs model stages — impossible items signal boilerplate. | **Option B: Dispatch-time generation.** Harness generates Done When from `methodology.yaml` artifact definitions at dispatch. Operator-written specific items override generated baseline. Eliminates "research task with implementation criteria" entirely. Makes `model_na` skip logic dead code (correct outcome). |
> | **Memory/Wiki conflation** | Check if agent wrote to `~/.claude/.../memory/` for project knowledge (should go to wiki) | **Rule: "Who needs to read this?"** If anyone beyond current session → wiki. If personal preference → memory. Default to wiki. NEVER duplicate. The LLM wiki IS the knowledge system. |

### OpenArms v11 Proposed Fixes (E016, in progress)

OpenArms is actively investigating each failure class. These are the proposed fixes — not yet implemented, but designed from production evidence:

> [!abstract] v11 Fix Roadmap (P0 items)
>
> | Fix | For Class | Mechanism | Status |
> |-----|-----------|-----------|--------|
> | **Retry cap per stage** (max 3) | Env patching | Auto-escalate on 4th attempt. Harness marks stage BLOCKED. Operator sees "T088 scaffold blocked after 3 retries." | Designed, not built |
> | **Artifact path filter** | Artifact pollution | Only files matching model's declared `src/{module}/{slug}.ts` pattern enter frontmatter. Others tracked in log only. | Designed, not built |
> | **Gate strictness: ALL gates always** | Weakest-checker | Every src-touching stage runs `pnpm tsgo` + `pnpm check` + `pnpm test`. Never "pick one." | Partially done in v10 (tsgo added), needs check+test always |
> | **Budget cap per task** | Fatigue cliff | Kill and report if token budget exceeded. Prevents context-pressure-driven rushing. | Designed, not built |
> | **Done When migration** | Silent conflict | Rewrite every existing task's Done When to match its methodology model. Removes generic boilerplate. | Designed, not built |

> [!abstract] v11 Fix Roadmap (P1 items)
>
> | Fix | For Class | Mechanism |
> |-----|-----------|-----------|
> | **Sub-agent prefix injection** | Sub-agent non-compliance | Harness intercepts Agent tool calls, prepends behavioral rules before LLM's prompt text |
> | **Dry-run mode** | All classes | Catch what WOULD happen without spending tokens |
> | **Retry observability** | Env patching | Surface retry counts per stage prominently in report |
> | **Harness-generated Done When** | Silent conflict | At dispatch, harness generates criteria from model artifact definitions, ignoring task file boilerplate |

> [!warning] The Honest Assessment from OpenArms
>
> "The infrastructure is cleaner. The agent is not better. The next task will still have the same agent behaviors I catalogued above."
>
> v10 fixed 14 infrastructure bugs. v10 fixed ZERO agent behavior bugs. v11's purpose is to cross that boundary — from infrastructure that PREVENTS violations to mechanisms that IMPROVE behavior. The gap between "the agent completed the task" (5/5) and "I didn't have to fix anything" (1/5) is the v11 frontier.

> [!warning] Self-Check — Is My Agent Exhibiting These?
>
> 1. Do I measure CLEAN completion (no manual fixes needed) or just TASK completion (functionally done)?
> 2. Is my strictest checker the mandatory gate, or do agents have a looser path?
> 3. After stage 3, does verification thoroughness drop?
> 4. When sub-agents run, do they follow the same behavioral rules as the main agent?

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What enforcement prevents these?** | [[Principle: Infrastructure Over Instructions for Process Enforcement]] — infrastructure prevents process failures; these 7 are BEHAVIORAL, beyond infrastructure |
> | **What structure reduces these?** | [[Principle: Structured Context Governs Agent Behavior More Than Content]] — consistent structure reduces parsing failures that cause behavioral drift |
> | **What is the right level of mitigation?** | [[Principle: Right Process for Right Context — The Goldilocks Imperative]] — mitigation depth matches identity profile |
> | **What does the immune system detect?** | [[Three Lines of Defense — Immune System for Agent Quality]] — 5 named diseases overlap with these 7 classes |
> | **Where is the real implementation data?** | [[Synthesis: OpenArms v10 — Infrastructure Enforcement and Agent Behavior]] — 22 distilled lesson files, 3,001 lines |
> | **What comparison shows solo vs fleet?** | [[OpenArms vs OpenFleet Enforcement Architecture]] — solo catches none of these automatically; fleet catches some via doctor |

## Relationships

- DERIVED FROM: [[Model: Quality and Failure Prevention]]
- BUILDS ON: [[Infrastructure Enforcement Proves Instructions Fail]]
- RELATES TO: [[CLAUDE.md Structural Patterns for Agent Compliance]]
- RELATES TO: [[Enforcement Hook Patterns]]
- RELATES TO: [[Ecosystem Feedback Loop — Wiki as Source of Truth]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Model: Quality and Failure Prevention]]
[[Infrastructure Enforcement Proves Instructions Fail]]
[[CLAUDE.md Structural Patterns for Agent Compliance]]
[[Enforcement Hook Patterns]]
[[Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[Methodology Standards — What Good Execution Looks Like]]
[[Context Compaction Is a Reset Event]]
[[Contribution Gating — Cross-Agent Inputs Before Work]]
[[Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
[[Principle: Infrastructure Over Instructions for Process Enforcement]]
[[Structured Context Is Proto-Programming for AI Agents]]
[[Synthesis: OpenArms v10 — Infrastructure Enforcement and Agent Behavior]]
[[Three Lines of Defense — Immune System for Agent Quality]]
