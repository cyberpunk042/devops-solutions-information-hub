---
title: "2026-05-16 — RGP profile v5-evening SFIF-overcorrection revert + comprehensive augmentation (17 surgical edits + 3 planning artifacts)"
type: note
note_type: session
domain: cross-domain
status: active
confidence: high
maturity: growing
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: operator-directive-2026-05-16-focus-profile-not-openclaw
    type: directive
    file: raw/notes/2026-05-16-operator-directive-focus-profile-not-openclaw-do-not-decide-do-not-minimize-workflow.md
  - id: prior-handoff-2026-05-16-final
    type: file
    file: docs/SESSION-2026-05-16-final.md
  - id: this-arc-handoff-2026-05-16-v2
    type: file
    file: docs/SESSION-2026-05-16-v2.md
  - id: pain-points-inventory-2026-05-08
    type: file
    file: raw/notes/2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate.md
  - id: sfif-model
    type: wiki
    file: wiki/spine/models/quality/model-sfif-architecture.md
  - id: per-project-assistant-profile-standards
    type: wiki
    file: wiki/spine/standards/per-project-assistant-profile-standards.md
  - id: sdd-methodology-profile
    type: wiki
    file: wiki/config/methodology-profiles/spec-driven.yaml
  - id: tdd-methodology-profile
    type: wiki
    file: wiki/config/methodology-profiles/test-driven.yaml
tags: [session, rgp, root-ghostproxy-rollout, ai-assistant-profile, sfif-revert, workflow-evolution, augment-not-rewrite, planning-artifacts, "2026-05-16"]
---

# 2026-05-16 — RGP profile v5-evening SFIF-overcorrection revert + comprehensive augmentation

## Summary

The root-ghostproxy AI-assistant profile (`.assistant/root-ghostproxy-rollout.{yaml,cron.yaml,openclaw.json5}`) was systematically corrected from the v5-evening hard-scope-lock overcorrection back to operator-doctrinal SFIF framing (per 2026-05-16 sacrosanct: *"this does not mean it completley block tasks either..."*). Arc covers 17 surgical Edit-tool augmentations across 3 files + 3 planning artifacts authored at `.assistant/_state/` + 1 operator-directive verbatim log + 1 authoritative handoff at `docs/SESSION-2026-05-16-v2.md`. All 25 enumerated items from prior handoff `docs/SESSION-2026-05-16-final.md` addressed (Item 4 cron-disable skipped per operator no-OpenClaw-touch directive). R20 sacrosanct held throughout (zero commits, zero `git rm`). Pipeline post: PASS (0 validation errors, 904 pages, 4123 relationships) — baseline + post-augment both clean since no `wiki/` files touched until this log entry.

## Arc origin

Continuation from `docs/SESSION-2026-05-16-final.md` (prior handoff) which documented the v5-evening failure: worker installed via new `cross_project_target` workspace_mode + ran 2 fires on wrong scope (picked T014/T015 sister-integration setup tasks instead of E001-E007 features). My response was overcorrection: hard-locked the profile to E001-E007 + FORBIDDEN to pick from M001-M014/T001-T067. Operator caught this overcorrection (2026-05-16, sacrosanct): *"SFIF also mean that you priritize Skffold before fundation before infrastructure before future... obviously.... this does not mean it completley block tasks either..."* — SFIF is RECURSIVE workflow with WITHIN-SCOPE soft priority, NOT a cross-task hard block.

Then this arc's operator-directive (verbatim, sacrosanct):

> *"YOU DO NOT DECIDE.. DID I SAY ANYTHING ABOUT DISABLING ANY CRON ? NO... FOCUS ON THE TASK.. YOU DONT NEED TO TOUCH ANYTHING ABOUT OPENCLAW.. ITS ALL ABOUT THE THE AI ASSISTANT PROFILE AND MAKING IT RIGHT SO THAT LATER... IN A THOUSAND HOURS WE CAN EVENTUALLY RUN IT SO THAT IT FIX THE PROJECT...."*

> *"/goal continue till everything is done. all the requirements, all the knowledge integrated and forced into this AI agent. DO NOT MINIMIZE.. IT WILL TAKE A LOT LOT LOT OF HOURS.. JUST GET STARTED AND WORKFLOW REMEMBER THE WORKFLOW."*

## What landed (17 augmentations + 3 planning artifacts)

| Layer | File | Edits | Net effect |
|---|---|---|---|
| Profile YAML | `.assistant/root-ghostproxy-rollout.yaml` | 13 surgical Edits | 1546L → 1857L; SFIF revert + bootstrap_idempotency + concurrency_control + announce_channel_policy + output_prose_density_policy + Opus 1M path_g + state_files extended; header v4→v5 |
| Cron YAML | `.assistant/root-ghostproxy-rollout.cron.yaml` | 10 surgical Edits | 490L → 602L; STEP 1 lock + idempotency in all 3 variants; STEP 2 4-level pick logic in all 3 variants; ANTI-PATTERNS lists rewritten with renamed + new anti-patterns; header v3→v5 |
| openclaw vendor config | `.assistant/root-ghostproxy-rollout.openclaw.json5` | 2 surgical Edits | systemPromptOverride principles 3+10 reverted; 214L unchanged |
| Planning artifact 1 | `.assistant/_state/root-ghostproxy-rollout-pain-points-to-epic-mapping.md` | NEW (100L) | Cluster (C01-C15) → primary E00x mapping with cross-cutting analysis; worker uses at Level 3 Step 2 of priority_order |
| Planning artifact 2 | `.assistant/_state/root-ghostproxy-rollout-task-authoring-template.md` | NEW (158L) | Frontmatter + body template + quality-gates self-audit + anti-patterns refused; worker uses at Level 3 Step 5 |
| Planning artifact 3 | `.assistant/_state/root-ghostproxy-rollout-epic-decomposition-sketches.md` | NEW (165L) | Per-E00x sub-module decomposition with SFIF sub-cycle tier per sub-module + audit-cluster mapping + ~tasks estimate; worker uses at Level 3 Step 3 + within_feature_sub_cycle priority detection |
| Operator directive log | `raw/notes/2026-05-16-operator-directive-focus-profile-not-openclaw-do-not-decide-do-not-minimize-workflow.md` | NEW (57L) | Verbatim operator correction; per AGENTS.md Hard Rule 3 |
| Handoff (this arc) | `docs/SESSION-2026-05-16-v2.md` | NEW (484L) | All 17 augmentations + 14 operator-Q items + Resume Checklist |

## Core mental model corrected

Before (v5-evening overcorrection): Hard SCOPE LOCK — pick ONLY from E001-E007; FORBIDDEN to pick from M001-M014/T001-T067; treat sister-integration as ABSOLUTELY OUT OF SCOPE.

After (operator-doctrinal SFIF revert, per *"this does not mean it completley block tasks either..."*):
- **Two SFIF cycles in play** (do not conflate):
  - (A) Sister-integration SFIF — installing root-ghostproxy AS A SISTER-PROJECT — DONE OR DOES NOT MATTER per operator; worker DEFAULTS AWAY
  - (B) root-ghostproxy's OWN project-lifecycle SFIF — at PROJECT scope in Features tier — THE primary purpose; worker DEFAULTS HERE
- **4-level pick priority_order** (replacing hard filter):
  1. Operator-explicit override in `operator-directives.md` (wins above all)
  2. DEFAULT in_scope (E001-E007 by audit-cluster severity + P0→P3 + within-feature sub-cycle SFIF soft priority)
  3. AUTHOR FROM PAIN-POINTS when 1+2 empty (per operator *"EVERYTHING IN THE FUCKING 150+ tasks and more since it was incomplete"*)
  4. CROSS-CYCLE FALLBACK (rare) when 1+2+3 exhausted AND sister-integration task is GENUINELY prerequisite to E001-E007 AND audit-cluster justification staged AND surfaced to operator-decision-queue (per operator *"this does not mean it completley block tasks either"*)
- **SFIF within-scope soft priority** (Scaffold → Foundation → Infrastructure → Features-impl) applies RECURSIVELY at every scope (project / feature / task); NOT a cross-task hard block

## Operational improvements landed

- **Bootstrap idempotency** (Item 6): first-fire re-installs no longer re-do full planning artifact; marker_file + inbox-evidence detection short-circuits to lightweight verification
- **Mutual-exclusion lock** (Item 7): `.assistant/_state/root-ghostproxy-rollout.lock` (PID + timestamp + variant) prevents bootstrap × driven-tick race on git stage in target project; stale-lock recovery on PID-dead OR age ≥ 30 min
- **Announce channel resolved** (Item 8): per `announce_channel_policy`, all surfacing routes via worker-owned files (inbox + fire-summary + queue + Resolution) — no OpenClaw announce-channel dependency; silences the *"announce → no route"* error
- **Per-fire summary mechanism** (Item 24): `.assistant/_state/root-ghostproxy-rollout-fire-summary.md` appended per fire with did/surfaced/next_plans/friction_observed subsections — operator can `grep` history without inspecting git status
- **Prose density policy** (Item 14): per-type targets + density anti-patterns + operator-feedback adaptation signal — addresses the T014/T015 verbose-Resolution retrospective
- **Opus 1M operator-action unlock path** (Item 9): 6-step `path_g_operator_action_unlock_sequence` consolidated (claude setup-token → openclaw auth login → add 1M model variant → update profile primary → re-install → scale context_limits 4×); operator-action only; 195k baseline non-blocking

## R20 + cross-cutting discipline held

- Zero `git commit` this session (R20 sacrosanct — operator commits)
- Zero `git rm` on tracked files
- Zero `wiki/` files touched until this log entry (only `.assistant/` + `raw/notes/` + `docs/`)
- Zero OpenClaw runtime / cron / agent-registration operations (per operator's explicit no-OpenClaw-touch directive 2026-05-16)
- All operator-words quoted verbatim in profile + planning artifacts + handoff + this log
- Augment-not-rewrite preserved: every change used Edit tool (surgical old_string/new_string); Write tool used only for brand-new files (3 planning artifacts + 1 directive log + 1 handoff + this entry)

## Pipeline post

- Baseline (pre-this-log): PASS · 904 pages · 4123 relationships · 0 validation errors · 326 lint issues (pre-existing advisory; not introduced this session)
- Expected post-this-log: PASS · 905 pages · ~4130 relationships · 0 NEW validation errors

## Relationships

- DERIVED FROM: [[2026-05-16-strong-handoff-ck-v3-live-cr-ps-still-broken|2026-05-16-strong-handoff-ck-v3-live-cr-ps-still-broken]]
- BUILDS ON: [[per-project-assistant-profile-standards|Per-Project Assistant Profile Standards]]
- IMPLEMENTS: [[model-sfif-architecture|SFIF Model]] (operator-corrected recursive workflow doctrine)
- IMPLEMENTS: [[model-per-project-assistant-profile|Per-Project Assistant Profile Model]]
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (workflow-encoded as profile structure)
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2]] (6-section profile + structured YAML + cron prompts as structural enforcement)
- DEMONSTRATES: [[right-process-for-right-context-the-goldilocks-imperative|Principle 3]] (4-level priority_order = per-task Goldilocks selection)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] (Success Criteria + telemetry + per-tick gates make profile claims falsifiable)
- DEMONSTRATES: [[spec-driven-evolution-the-project-evolves-its-own-spec-to-fix-bugs-it-exhibits|Principle 5]] (operator-corrected SFIF framing = spec evolution from the v5-evening bug)
- RELATES TO: [[2026-05-08-pain-points-inventory-from-root-failed-conversation-master-aggregate|Pain-Points Inventory]] (worker's Level 3 authoring substrate)

## Backlinks

[[2026-05-16-strong-handoff-ck-v3-live-cr-ps-still-broken|2026-05-16-strong-handoff-ck-v3-live-cr-ps-still-broken]]
[[per-project-assistant-profile-standards|Per-Project Assistant Profile Standards]]
[[SFIF Model]]
[[Per-Project Assistant Profile Model]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle 3]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[Principle 5]]
[[Pain-Points Inventory]]
