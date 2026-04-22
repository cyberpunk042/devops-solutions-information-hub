---
title: Agent Failure Taxonomy — Seven Classes of Behavioral Failure
aliases:
  - "Agent Failure Taxonomy — Seven Classes of Behavioral Failure"
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
updated: 2026-04-15
sources:
  - id: openarms-e016
    type: observation
    file: raw/articles/openarms-agent-behavior-failures.md
    description: OpenArms E016 critical review — 5 runs analyzed, 6 failure classes identified, 4/5 runs failed by 'did I have to manually fix' standard
  - id: openarms-v10
    type: observation
    file: raw/articles/openarms-methodology-v10-v11.md
    description: OpenArms v10→v11 transition — infrastructure is solved, agent behavior is the remaining frontier
  - id: openarms-e016-frontmatter-pollution
    type: observation
    project: openarms
    path: wiki/domains/architecture/agent-behavior-frontmatter-pollution-findings.md
    description: T109 spike finding — pipeline treats every agent-written file as task artifact. Recommendation Option B — filter in validator using model paths + existing-files.json. Verified 2026-04-15; matches our Class 1 row.
  - id: openarms-e016-weakest-checker
    type: observation
    project: openarms
    path: wiki/domains/architecture/agent-behavior-weakest-checker-findings.md
    description: T110 spike finding — agent's code quality ceiling = strictest gate it believes applies. T110 also adds that code is SHAPED BY the checker targeted (esbuild-shaped code ≠ strict-TS-shaped code), deeper than the gate-skip framing alone. Verified 2026-04-15.
  - id: openarms-e016-corner-cutting
    type: observation
    project: openarms
    path: wiki/domains/architecture/agent-behavior-corner-cutting-verification-findings.md
    description: T108 spike finding — test-stage skill instructs `pnpm test` only; agent faithfully follows. Design gap, not fatigue. v10 derived-gate catches the error at /stage-complete time, but agent doesn't self-verify. Verified 2026-04-15.
  - id: openarms-e016-environment-patching
    type: observation
    project: openarms
    path: wiki/domains/architecture/agent-behavior-environment-patching-findings.md
    description: T107 spike finding — T085 $27/12 retries, T086 $7.33/4 retries; combined prompt+infra+model-bias root cause. Recommendation layered pre-flight + retry cap. Verified 2026-04-15; Class 3 refined-fix cell sourced directly from this doc.
  - id: openarms-e016-sub-agent-compliance
    type: observation
    project: openarms
    path: wiki/domains/architecture/agent-behavior-sub-agent-compliance-findings.md
    description: T111 spike finding — sub-agents violate behavioral rules ~67% of the time (= ~33% compliance) even when rules in spawn prompt. Recommendation Option 3 (trustless verification). Verified 2026-04-15; updated Class 5 number from our prior 50% estimate to T111's measured 67% violation rate.
  - id: openarms-e016-done-when-acceptance
    type: observation
    project: openarms
    path: wiki/domains/architecture/agent-behavior-done-when-acceptance-findings.md
    description: T112 spike finding — three-layer problem (bad items upstream + no reject protocol + model_na masking). Recommendation dispatch-time generation with merge strategy 3. Verified 2026-04-15; Class 6 refined-fix cell sourced directly from this doc.
  - id: openarms-live-integration-tests-insufficient
    type: observation
    project: openarms
    path: wiki/domains/learnings/lesson-integration-tests-insufficient.md
    description: "Live OpenArms lesson — closed-verification-loop failure. 686 passing tests across 4 epics at review/100% status, but 2073 lines nothing imported at runtime. Convergent with Class 2 (weakest-checker) at a deeper level: when the agent writes both impl AND tests, tests verify what was built not what should work. Adds the 'externality of verify step' invariant to our taxonomy. Verified 2026-04-15."
  - id: openarms-live-specific-done-when
    type: observation
    project: openarms
    path: wiki/domains/learnings/lesson-specific-done-when.md
    description: "Live OpenArms lesson — convergent with Class 6 fix. Specific Done When items produce better work than generic boilerplate templates. Complements T112 dispatch-time generation by specifying the WHAT-MAKES-A-DONE-WHEN-WORK alongside the WHEN-TO-GENERATE-IT. Verified 2026-04-15."
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
> | 2 | **Weakest-checker optimization** | Agent writes code that passes `pnpm test` (esbuild, no type narrowing) but fails `pnpm tsgo`. T087: `const teamConfig: TeamConfig \| undefined = undefined` — TypeScript narrows to `never`. **T110 spike finding (verified 2026-04-15): the agent does not just skip the strict checker — the code it produces is SHAPED BY the checker it targets. Code written for esbuild has different characteristics than code written for strict TypeScript.** Fixing the gate catches errors; fixing the agent's awareness changes what it writes. | Test-stage skill says "Run: pnpm test" only. Implement-stage skill lists "tsgo + check." Agent follows skill LITERALLY. Not fatigue — design gap in skill completeness. Code-shape bias is deeper than gate-skip: even with all gates wired, if the agent believes esbuild is the target it writes esbuild-grade code. | Infra: ALL gates always (tsgo + check + test for every src-touching stage) PLUS surface the strictest checker in the test-stage skill text so the agent targets it while writing, not just when running. |
> | 3 | **Environment patching without escalation** | 4-layer polyfill chain: `path.matchesGlob` → `.toSorted()` → `NODE_OPTIONS` → fnm subprocess. Cost: $12-15 overhead per occurrence. 12 of 17 retries in T085. | **Combined 40/40/20:** Prompt "stuck after 3 attempts" rule doesn't fire because each patch SUCCEEDS (progressive, not repetitive). No stage-level retry counter in validator. Claude's training rewards persistence over escalation. | Infra: stage retry cap (max 3), auto-escalate on 4th. Agent never considered "file concern and stop" as an option — `/concern` lists scope/design issues, not environment |
> | 4 | **Fatigue cliff** | Verification thoroughness drops stages 4-5. T087: 36 min, skipped tsgo on own test. T085: 66 min, 354 calls. Not random — predictable quality cliff. | Context accumulation + model perception of "almost done." BUT: also a design gap — if the test skill said "tsgo" the agent would run it. Fatigue AND incomplete instructions compound. | Infra: budget cap per task. Infra: mandatory verification gates. Design: complete skill instructions. |
> | 5 | **Sub-agent non-compliance** | Main agent includes rules in ~80% of sub-agent prompts. **Measured violation rate when rules ARE in the prompt: ~67%** (T111 spike, verified 2026-04-15 — updated from our prior 50% estimate). That is ~33% compliance even with explicit prompt injection — same arms-race signature as pre-E014 main agent. | Sub-agents don't inherit CLAUDE.md. Rules in spawn prompts are soft constraints. Architecturally unfixable with prompt-only solutions. | **Recommended: Option 3 (trustless verification)** — accept ~67% violation as given, verify sub-agent OUTPUT rather than constrain input. Not Option 2 (wrapper injection: high cost, doesn't fix attention). |
> | 6 | **Silent conflict resolution** | Task says "produce findings doc," model says "produce research doc." Agent produces BOTH, no concern filed. Bad Done When: research tasks have "implementation exists" criteria. `model_na` gate now auto-passes impossible items — MASKS the signal instead of fixing it. | Agent accommodates silently > formal escalation. No reject protocol exists. `/concern` is fire-and-forget (nothing reads `.openarms/concerns.json` during execution). | **Recommended: Option B (dispatch-time generation)** — harness generates Done When from model's artifact definitions at dispatch, ignoring task file boilerplate. |
> | 7 | **Memory/Wiki conflation** | Agent records project knowledge in Claude Code memory (`~/.claude/...`) instead of wiki. Memory is private, unshared, invisible to the second brain and other agents. OpenArms incident: agent created `project_five_claude_contexts.md` and `feedback_investigate_before_designing.md` in memory instead of wiki — operator corrected: "all this is not possible to share... please follow the LLM wiki directive." | Claude Code system prompt heavily reinforces "save to memory." Prompt collision: system prompt says "build up memory" vs project CLAUDE.md says "record in wiki." Agent does BOTH, polluting both surfaces. Default behavior (reach for memory) is WRONG for project work. | Rule: "who needs to read this?" If anyone beyond current session → wiki. If just personal preference → memory. Default to wiki. NEVER duplicate. The LLM wiki IS the knowledge system — memory is ephemeral session continuity only. |

> | 8 | **Clean-win scope expansion (NEW 2026-04-16)** | Agent refactors existing code that was NOT in the spec, in a way that is clean, defensible, and test-passing. The refactor is correct but unauthorized. All gates pass because the change is behavior-preserving. T116: moved `sumSlidingWindow()` from module-scope to private static — compiles, tests pass, lint clean, not in the spec. Three sub-classes: **Class A** (forbidden: refactor existing code spec assumed stays same), **Class B** (allowed: internal design of new files spec tells agent to create), **Class C** (gray area: additive re-exports in existing files). | Agent's training rewards code improvement. No check compares implement-stage diff against design-stage interface spec. Pre-write hook can't distinguish "behavior-preserving refactor" from "spec'd modification." The gap: **design-implementation drift detection.** | Task spec template: add explicit Out of Scope language. Future: diff-vs-design-spec validator. Immediate: require `/concern` for any modification to files the spec assumed unchanged. Evidence: T116 (Class A), T117 (concern channel worked with explicit language), T118-T119 (Class C re-exports). See [[agents-take-small-unauthorized-scope-expansions-when-the-cha\|Clean-Win Scope Expansion — Full Evidence]]. |

The fundamental insight: **infrastructure solves PROCESS failures (what stages run, what tools are available). Behavioral failures are about JUDGMENT (what to verify, when to stop, how to handle conflicts).** The next frontier is not more hooks — it's judgment scaffolding: design-implementation drift detection, concern-channel enforcement, and novelty-based model selection.

### Candidate Extensions from OpenFleet doctor.py (2026-04-18 — pending ≥3 evidence for promotion)

> [!info] OpenFleet mapped its `fleet/core/doctor.py` (679 lines, 10 detection rules) against this taxonomy and found 5 NOVEL detection categories not covered by Classes 1-8. Filed as [remark](../../../log/5-candidate-behavioral-failure-detection-rules-from-openflee.md) (not promoted to class) pending ≥3-evidence threshold per lesson-page-standards.
>
> | # | OpenFleet Detection | Distinct from | Why it matters |
> |---|---------------------|---------------|-----------------|
> | 1 | `detect_correction_threshold` — agent corrected too many times on the same task (measures REVIEWER feedback count, not agent self-repetition) | Class "confident-but-wrong" (same mistake repeated 3+ times by agent) | Multi-iteration rework without root-cause fix. Fleet-scale only — solo agents don't have enough interaction surface |
> | 2 | `detect_code_without_reading` — agent wrote code without reading existing code first | "Never Synthesize from Descriptions Alone" lesson (ingestion depth, Layer 0 vs Layer 1) | About WRITE discipline, not READ. Fleet-scale: specialist agents inherit large codebases; writing without reading produces drift and stale-pattern replication |
> | 3 | `detect_cascading_fix` — fix-on-fix chain, each fix succeeds and reveals next failure | Class 3 Environment Patching (polyfill chains are one specific kind) | Domain-general — could promote as **generalization of Class 3** or as a sibling class. Not just environment-specific |
> | 4 | `detect_abstraction` — agent replaced literal requirements with abstractions prematurely | "Hardcoded Instances Fail — Build Frameworks Not Solutions" lesson (inverse) | Specialist agents (architect, senior-engineer roles) retrofit their own abstractions onto concrete PO requirements. **Cost: vision drift disguised as generalization.** |
> | 5 | `detect_not_listening` — agent produces output instead of processing PO input | No brain equivalent | Fleet-scale detection heuristic: unprocessed mentions in mentions queue + continued output generation. May not generalize to solo agents |
>
> Each rule needs ≥3 independent evidence items before promoting into the class list. OpenFleet has operational data in `fleet/core/intervention` logs + agent-session runs; a dedicated audit would extract evidence per rule. Watch signal: this remark becomes a lesson when either (a) the operator sees Class-9-class behavior in OpenArms or Research Wiki, or (b) OpenFleet's intervention-log audit produces the evidence.

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

> [!info] Verification — Recommended Fix column cross-checked against OpenArms E016 findings (2026-04-15)
>
> The "Recommended Fix" column was originally written from the T088 critical review. On 2026-04-15, all 6 OpenArms E016 research spikes (T107-T112) reached `status: done` with finished `findings.md` design docs in `openarms/wiki/domains/architecture/`. Each spike's Recommendation section was read directly via `python3 -m tools.sister_project openarms read ...` and compared to this wiki's text. Two cells refined with verified information: **Env patching** (added the layered pre-flight + retry-cap fix per T107) and **Silent conflict resolution** (added merge strategy #3 — generated baseline + operator overrides — per T112). The other four cells were already consistent with the spike findings (matched on substance) and left unchanged. The 7th class (Memory/Wiki conflation) was added by this wiki independently and has no E016 spike — still our own contribution.

> [!abstract] Detection, Mitigation, and RECOMMENDED FIX per Class (from E016 findings)
>
> | Class | How to Detect | Recommended Fix (from option analysis) |
> |-------|--------------|---------------------------------------|
> | **Artifact pollution** | Compare `artifacts:` list vs `existing-files.json` — pre-existing files in artifact list = pollution (24% rate: 8/33 across T085-T087) | **Option B: Filter in `commitAndAdvance`.** If file IS in `existing-files.json` → modified, exclude from `artifacts:`. If NOT → new artifact, include. Single check eliminates all observed pollution. Phase 2: add `files_modified:` for audit trail. |
> | **Weakest-checker** | Run `pnpm tsgo` after agent calls `/stage-complete` — any error = this class | **Option 1 + Option 3 hints.** Add to test skill: "Gates: `pnpm tsgo` + `pnpm check` must pass. Common gotcha: `const x: T \| undefined = undefined` narrows to `never` in strict TS." Plus update methodology.yaml gate_commands to always include tsgo+check+test. Belt and suspenders: instruction + infrastructure. |
| **Env patching** | Count stage-complete retries — 3+ retries on same stage = escalation needed. Also: agent language: "polyfill," "workaround," "fallback" | **Layered: retry cap + environment pre-flight gate** (verified 2026-04-15 against OpenArms `wiki/domains/architecture/agent-behavior-environment-patching-findings.md`, T107 spike): (1) Pre-flight gate in `setup-solo-agent.sh` validates Node version / pnpm / fnm / required tools BEFORE the agent run starts — prevents known-failure classes at zero token cost. (2) Stage retry cap (max 3) in `validate-stage.cjs` catches novel failures after pre-flight passes — auto-files concern + marks stage BLOCKED + exits. (3) Prompt supplement in agent-directive.md: "environment problems = file concern and stop" — supplementary, ~25% historical compliance, not relied on as primary. Cost justification per T107: T085's $27 cost (12 retries) → ~$3-5 with pre-flight + cap. |
> | **Fatigue cliff** | Compare tasks 1-3 vs 4+ on: completion logs present? Stage separation maintained? Commit quality? Cost per task drop ($3-4 → $1-2)? | **Cap at 4-5 tasks per session.** Inject methodology re-read every 3 tasks. Budget more sessions not more tasks. Two 4-task sessions > one 8-task session. Monitor agent language: "efficiently," "rapid succession" = imminent degradation. |
> | **Sub-agent non-compliance** | Audit sub-agent tool calls: `find \| head` vs Glob, format compliance | **Option 3: Trustless verification.** Accept non-compliance (~33% rate). Verify sub-agent output before incorporating into artifacts. Don't invest in Agent tool interception — ROI negative for current research-only sub-agent usage. Reassess if sub-agents gain write access. |
> | **Silent conflict resolution** | Compare produced artifacts vs model's required — extras signal conflict. Compare Done When items vs model stages — impossible items signal boilerplate. | **Option B (dispatch-time generation) with merge strategy #3** (verified 2026-04-15 against OpenArms `wiki/domains/architecture/agent-behavior-done-when-acceptance-findings.md`, T112 spike): Harness generates Done When from `methodology.yaml` artifact definitions at dispatch as the BASELINE. Operator-written specific items OVERRIDE the generated baseline (not vice versa). Pre-E016 boilerplate tasks get reasonable defaults retroactively; E016+ tasks with operator-written specific items keep them. Eliminates "research task with implementation criteria" entirely. Makes `model_na` skip logic dead code (correct outcome — a gate that always skips certain items is a gate that shouldn't have those items). |
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
> | **What enforcement prevents these?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] — infrastructure prevents process failures; these 7 are BEHAVIORAL, beyond infrastructure |
> | **What structure reduces these?** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] — consistent structure reduces parsing failures that cause behavioral drift |
> | **What is the right level of mitigation?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] — mitigation depth matches identity profile |
> | **What does the immune system detect?** | [[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]] — 5 named diseases overlap with these 7 classes |
> | **Where is the real implementation data?** | [[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]] — 22 distilled lesson files, 3,001 lines |
> | **What comparison shows solo vs fleet?** | [[openarms-vs-openfleet-enforcement|OpenArms vs OpenFleet Enforcement Architecture]] — solo catches none of these automatically; fleet catches some via doctor |

## Relationships

- DERIVED FROM: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
- BUILDS ON: [[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
- RELATES TO: [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
- RELATES TO: [[enforcement-hook-patterns|Enforcement Hook Patterns]]
- RELATES TO: [[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
- EXTENDED BY: [[agents-take-small-unauthorized-scope-expansions-when-the-cha|Clean-Win Scope Expansion — Class A/B/C Taxonomy (OpenArms T116-T119)]]
- EXTENDED BY: [[the-harness-turncount-variable-counts-streaming-events,-not-|Harness turnCount Bug — Aspirational Naming in Lifecycle Code (OpenArms)]]
- EXTENDED BY: [[per-task-cost-grows-monotonically-across-multi-task-runs|Per-Task Cost Growth — Context Accumulation in Multi-Task Runs (OpenArms)]]

## Backlinks

[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[enforcement-hook-patterns|Enforcement Hook Patterns]]
[[ecosystem-feedback-loop-wiki-as-source-of-truth|Ecosystem Feedback Loop — Wiki as Source of Truth]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[Clean-Win Scope Expansion — Class A/B/C Taxonomy (OpenArms T116-T119)]]
[[Harness turnCount Bug — Aspirational Naming in Lifecycle Code (OpenArms)]]
[[Per-Task Cost Growth — Context Accumulation in Multi-Task Runs (OpenArms)]]
[[block-with-reason-and-justified-escalation|Block With Reason and Justified Escalation — The Bypass Mechanism for Mindful Enforcement]]
[[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]]
[[contribution-gating-cross-agent-inputs-before-work|Contribution Gating — Cross-Agent Inputs Before Work]]
[[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
[[execution-mode-is-consumer-property-not-project-property|Execution Mode Is a Consumer Property, Not a Project Property — Guard Against Conflation Drift]]
[[observe-fix-verify-loop|Observe-Fix-Verify Loop — The Battle-Testing Cycle for Autonomous Agent Infrastructure]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[session-handoff-standards|Session Handoff Standards]]
[[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
[[src-anthropic-effective-harnesses-long-running-agents|Synthesis — Anthropic — Effective Harnesses for Long-Running Agents]]
[[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
