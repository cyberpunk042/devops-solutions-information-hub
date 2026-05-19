---
title: "2026-05-16 — RGP profile v5.2 cadence-doctrine: 5m sweet spot + do big chunks + no time-anxiety (worker_cadence_doctrine block + 24 surgical edits)"
type: note
note_type: session
domain: cross-domain
status: active
confidence: high
maturity: growing
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: operator-goal-2026-05-16-evening-2-cadence-doctrine
    type: directive
    file: raw/notes/2026-05-16-operator-goal-5m-sweetspot-no-time-worry-do-big-chunks-confident-synergy.md
    description: "Operator /goal 2026-05-16 evening 2 (sacrosanct, verbatim quoted in the raw note): 5m cron sweet spot + agent not directed to worry about time + do big chunks of work + respect workflow + confidence in triggers/prompts/directives/synergy"
  - id: v5-evening-overcorrection-arc-prior
    type: file
    file: wiki/log/2026-05-16-rgp-profile-v5-evening-overcorrection-revert-and-comprehensive-augmentation.md
  - id: v5-evening-overcorrection-handoff
    type: file
    file: docs/SESSION-2026-05-16-v2.md
  - id: overcorrection-lesson
    type: wiki
    file: wiki/lessons/01_drafts/overcorrection-binary-fix-without-nuance-when-correcting-over-permissive-into-over-restrictive.md
  - id: goldilocks-principle
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md
  - id: spec-driven-evolution-principle
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/spec-driven-evolution-the-project-evolves-its-own-spec-to-fix-bugs-it-exhibits.md
  - id: enforcement-must-be-mindful
    type: wiki
    file: wiki/lessons/03_validated/methodology-process/enforcement-must-be-mindful-hard-blocks-need-justified-bypass.md
tags: [session, rgp, root-ghostproxy-rollout, ai-assistant-profile, cadence-doctrine, 5m-sweetspot, do-big-chunks, no-time-anxiety, lock-handles-overlap, workflow-evolution, spec-evolution, "2026-05-16"]
---

# 2026-05-16 — RGP profile v5.2 cadence-doctrine

## Summary

Second profile-evolution arc of 2026-05-16 — operator /goal directed: 5m cron cadence is the sweet spot for the active worker; agent NOT directed to worry about time; do big chunks of substantive work; respect the workflow; otherwise what could take 1h would take 4-5 hours (time-fragmentation overhead). Per operator: *"lets continue till we fill confident into our triggers, prompts and directives and the synergy."* 24 surgical edits across 3 profile files + new top-level `worker_cadence_doctrine` block in profile YAML + this log entry. NO OpenClaw runtime touches (per session-prior operator directive). R20 sacrosanct held. Pipeline post: PASS expected (will run after this log entry).

## What landed (24 augmentations + 1 new doctrine block)

### Cron YAML (10 edits)

| # | Change | Rationale |
|---|---|---|
| 1 | Header v5 → v5.2 + cadence-philosophy block expanded (check-often-work-deep mental model + 5m sweet spot + lock-handles-overlap) | Operator-doctrine 2026-05-16 this /goal |
| 2 | driven-worker-tick comment block expanded + schedule `every:15m` → `every:5m` | Headline cadence change |
| 3 | driven-worker-tick STEP 1 BRANCH OPERATOR_DIRECTED_SPRINT reframed (sprint = MORE WORK PER LOCK-HOLD, NOT faster cadence) | Sprint-semantics correction |
| 4 | driven-worker-tick STEP 1 lock-stale-window 30 min → 90 min (accommodates substantive deep work without false-stale recovery) | Lock policy update |
| 5 | driven-worker-tick STEP 10 LOOP CONDITIONS: removed `Budget remains (< 12 min used of 15-min tick budget; reserve 3 min for stage + log)`; added explicit "NO PER-FIRE TIME BUDGET CAP" framing | Core time-anxiety removal |
| 6 | driven-worker-tick BUDGET section → SUBSTANTIVE-DEPTH FRAMING (no time caps; substantive 60-90 min fires fine; sprint = more-work-per-acquisition) | Reframe per operator |
| 7 | driven-worker-tick description + timeout_seconds 900 → 5400 (90 min ceiling; matches lock-stale window) | Match doctrine |
| 8 | driven-worker-tick Per-acquisition output + Goldilocks per-tick tiebreaker softened to scope-sizing | Consistent framing |
| 9 | weekly-module-deep STEP 1 lock-stale-window 30 min → 90 min + reframed reason ("substantive deep work on the in-flight fire is the right outcome") | Lock policy update |
| 10 | weekly-module-deep STEP 10 LOOP CONDITIONS + module_incomplete_at_natural_end + SUBSTANTIVE-DEPTH FRAMING + description (no time-budget cap); timeout_seconds 10800 kept (3h ceiling matches deep-mode cadence) | Same doctrine applied to weekly |

### Profile YAML (13 edits)

| # | Change | Rationale |
|---|---|---|
| 1 | Profile YAML header v5 → v5.2 + arc-narrative augmented | Version reconciliation |
| 2 | prompt_templates.system principle 5 (Goldilocks per-tick) reframed: Goldilocks scope-sizing + substantive depth + 5m + lock + sprint=more-work-per-acquisition | System prompt 17-principles update |
| 3 | workflow.canonical_pipeline step_10 purpose reframed (no per-fire time-budget cap) | Workflow-step consistency |
| 4 | step_10.per_fire_summary.next_plans reframed (no "if budget were unlimited" caveat) | Per-fire summary consistency |
| 5 | requirements_mapping R13_anti_pollution reframed (substantive depth per acquisition; not count-per-fire) | 21-requirements alignment |
| 6 | anti_patterns.cron_cadence_spam reframed for 5m sweet spot + lock-aware (detector + response + why all updated) | Anti-pattern update |
| 7 | model_routing.principles "Goldilocks per-tick" reframed | Routing principles consistency |
| 8 | sfif_binding.pick_filter level 5 Goldilocks per-tick tiebreaker reframed | Pick-filter consistency |
| 9 | workflow.canonical_pipeline step 2 within-scope tiebreaker Goldilocks per-tick reframed | Workflow-step consistency |
| 10 | OPERATOR_DIRECTED_SPRINT branch description: "cap raised, multi-task per tick" → "MORE WORK PER ACQUISITION (chain substantive tasks within one lock-hold), NOT faster cadence" | Sprint-semantics |
| 11 | STEADY_WORK branch description: "loop until budget exhausted" → "do it FULLY (no per-fire time-budget cap), then loop while LOOP CONDITIONS hold" | Doctrine consistency |
| 12 | pm_scrum_facilitator subagent style: Sprint-mode detection reframed (more-work-per-acquisition) | Subagent style update |
| 13 | All 10 subagent budgets `budget: "X-Y minutes"` → `scope_tier: "verification\|substantive\|bounded\|light (characterization)"` with no time numbers; NOTE block added explaining scope_tier doctrine | Subagent budget reframe |
| 14 | NEW top-level `worker_cadence_doctrine` block (~70 lines) consolidating: cadence (5m driven + Tue weekly + first-fire bootstrap) + mental_model (CHECK OFTEN, WORK DEEP ONCE ACTIVE) + do_big_chunks_directive (operator-verbatim + encoded_in list) + sprint_semantics (NOT faster cadence; IS more-work-per-acquisition) + lock_stale_window 90 min + timeout_seconds per variant + synergy_check (triggers × prompts × directives × workflow matrix) | NEW navigable home for cadence semantics |

### openclaw.json5 (2 edits)

| # | Change | Rationale |
|---|---|---|
| 1 | systemPromptOverride principle 6 reframed: Goldilocks scope-sizing + substantive depth + check-often-work-deep mental model + lock + sprint=more-work-per-acquisition | JSON-encoded system prompt update |
| 2 | systemPromptOverride WORKFLOW CONTRACT line: "Step 10 loop within budget or declare end-of-tick" → "Step 10 loop while LOOP CONDITIONS hold; NO per-fire time-budget cap; release lock at natural completion" | Workflow contract consistency |

## Core mental model change

**Before (v5):** worker fires every 15 min with per-tick BUDGET (8-12 min for steady, reserve 3 min for stage/log, exit if substantive task exceeds 12 min). Implicit time-anxiety: fragment substantive work to fit tick budget.

**After (v5.2):** worker fires every 5 min as a CHECK-OFTEN-WORK-DEEP pattern. Lock-aware: if lock held + PID alive + age < 90 min → defer this fire (in-flight substantive work continues). If lock acquired → do the substantive work AS LONG AS IT NATURALLY TAKES (no per-tick time-budget cap; TDD red→green→refactor through completion; substantive 60-90 min fires are FINE). Release lock at natural completion; next 5m tick picks up next work. Sprint = MORE WORK PER ACQUISITION (chain substantive tasks within one lock-hold), NOT faster cadence.

Operator framing of why: *"otherwise what could take 1h would take 4-5 hours"* — artificially fragmenting a 1-hour task into 4-5 fifteen-minute chunks adds overhead (context-rebuild + re-orient + lock-acquire-cycle + stage-and-restage) AND defeats SDD+TDD natural cycle. Doctrinal answer: TRUST the lock + 5m cadence to handle overlap; DON'T try to make the agent worry about time.

## Synergy verification (per operator: "till we feel confident into our triggers, prompts and directives and the synergy")

Per the new `worker_cadence_doctrine.synergy_check` block in profile YAML:

| Layer | v5.2 encoding |
|---|---|
| **Triggers** | cron schedule `every:5m` (driven) + Tue 09:00 (weekly) + first-fire (bootstrap) · mutual-exclusion lock with 90-min stale-window · bootstrap-marker idempotency-gate |
| **Prompts** | 3 cron prompts (bootstrap + driven + weekly) all reference 4-level priority_order + lock-aware STEP 1 + SUBSTANTIVE-DEPTH FRAMING at STEP 10 · systemPromptOverride 17 principles include cadence + lock + do-big-chunks doctrine (principle 5+11) · workflow.canonical_pipeline 10 steps with augment-not-rewrite + audit-anchored + R20 throughout |
| **Directives** | raw/notes/2026-05-16-* verbatim · wiki/log/2026-05-16-* arc tracking (2 entries now) · wiki/lessons/01_drafts/overcorrection-* meta-lesson · worker_cadence_doctrine block (one navigable home) |
| **Synergy** | triggers acquire/defer via lock → prompts direct deep substantive work → directives anchor the why → workflow.canonical_pipeline executes the how |

Diagnostic: when this synergy holds, a fire that acquires lock does big-chunk-substantive-work and the next 5m tick defers correctly. When synergy fails, fires fragment work OR overlap on git stage OR miss operator-directives. Each failure mode has a specific anti-pattern + remediation encoded in the profile.

## P5 spec-driven evolution cycle (this is the 3rd cycle of 2026-05-16)

Per [[spec-driven-evolution-the-project-evolves-its-own-spec-to-fix-bugs-it-exhibits|Principle 5]] — the project evolves its own spec to fix bugs it exhibits.

- **Cycle 1 (morning):** v5-evening overcorrection. Worker picked wrong scope (T014/T015 setup tasks) → I overcorrected with hard scope lock → operator caught the overcorrection.
- **Cycle 2 (evening 1):** SFIF revert arc. 17 surgical edits + 3 planning artifacts + handoff `docs/SESSION-2026-05-16-v2.md` + log `wiki/log/2026-05-16-rgp-profile-v5-evening-overcorrection-revert-and-comprehensive-augmentation.md` + lesson `wiki/lessons/01_drafts/overcorrection-binary-fix-*.md`.
- **Cycle 3 (evening 2, THIS):** Operator surfaced new improvement direction — cadence + time-anxiety. 24 surgical edits + 1 new doctrine block + this log entry. The PRIOR arc's profile augmentations are the SUBSTRATE this cycle builds on (not rewritten).

Each cycle = operator-observed-bug → spec-evolution → tracked-artifact → next-cycle-builds-on. The P5 doctrine operates at this CONVERSATION layer (operator-correction cycles within session) just as it operates at the larger PROJECT layer.

## R20 + cross-cutting discipline held

- Zero `git commit` (R20 sacrosanct — operator commits)
- Zero `git rm` on tracked files
- Zero OpenClaw runtime / cron / agent-registration operations (per session-prior operator no-OpenClaw-touch directive)
- Only `.assistant/` (profile artifacts) + `wiki/log/` (this entry) touched
- All operator-words quoted verbatim across profile YAML + cron + json5 + this log + worker_cadence_doctrine block
- Augment-not-rewrite preserved: every change used Edit tool surgical old_string/new_string; Write tool only for this new log entry

## Operational implications (when operator chooses to re-install + enable cron)

Per worker_cadence_doctrine.cadence:
- driven-worker-tick fires every 5 min
- Each fire checks lock first: held → defer; free → acquire + do substantive work AS LONG AS IT NATURALLY TAKES
- A 60-min substantive task = 1 fire holds lock for 60 min + 12 subsequent 5m ticks defer (correct lock behavior)
- Sprint mode (operator-invoked) = chain multiple substantive tasks within one lock-hold (until LOOP CONDITIONS go false OR 90-min lock-stale-window approaches)
- Weekly Tue 09:00 fire does 1-3h deep work on one module (10800s timeout); subsequent weekly fires (next Tue) defer via lock if needed (unlikely given weekly cadence)
- All 10 subagents have scope_tier characterizations (no time-minute budgets); each does its work to completion within the parent fire's natural duration

## Relationships

- IMPLEMENTS: [[right-process-for-right-context-the-goldilocks-imperative|Principle 3 Goldilocks]] (5m cadence + do-big-chunks IS the right process for the worker context — calibrated to scope, not over-fragmented)
- DEMONSTRATES: [[spec-driven-evolution-the-project-evolves-its-own-spec-to-fix-bugs-it-exhibits|Principle 5 P5]] (3rd cycle of 2026-05-16 P5 evolution)

## Backlinks

[[Principle 3 Goldilocks]]
[[Principle 5 P5]]
