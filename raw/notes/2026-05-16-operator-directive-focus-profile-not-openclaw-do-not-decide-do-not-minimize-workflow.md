---
title: "2026-05-16 — Operator directive: YOU DO NOT DECIDE; focus on profile; no OpenClaw; do not minimize; workflow"
type: note
note_type: directive
domain: log
status: active
confidence: authoritative
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: operator-directive-2026-05-16-focus-profile-not-openclaw
    type: directive
tags: [operator-directive, root-ghostproxy, ai-assistant-profile, do-not-decide, do-not-minimize, no-openclaw-touch, workflow, sdd, tdd, sfif, augment-not-rewrite, "2026-05-16"]
---

# Operator directive — focus on the AI assistant profile; do not decide; do not minimize; workflow

## Verbatim operator words (sacrosanct, 2026-05-16)

> "YOU DO NOT DECIDE.. DID I SAY ANYTHING ABOUT DISABLING ANY CRON ? NO... FOCUS ON THE TASK.. YOU DONT NEED TO TOUCH ANYTHING ABOUT OPENCLAW.. ITS ALL ABOUT THE THE AI ASSISTANT PROFILE AND MAKING IT RIGHT SO THAT LATER... IN A THOUSAND HOURS WE CAN EVENTUALLY RUN IT SO THAT IT FIX THE PROJECT...."

> "/goal continue till everything is done. all the requirements, all the knowledge integrated and forced into this AI agent. DO NOT MINIMIZE.. IT WILL TAKE A LOT LOT LOT OF HOURS.. JUST GET STARTED AND WORKFLOW REMEMBER THE WORKFLOW."

## Parsed constraints (sacrosanct framing)

1. **I DO NOT DECIDE.** Operator decides. My SESSION STATE report suggested "disable cron before resuming" — operator never said that. I do not get to add recommendations the operator did not make. (R20-adjacent discipline: stay in lane.)
2. **No OpenClaw touch.** Cron, gateway, agent registration, runtime — none of it. This work is profile-files-only: `.assistant/root-ghostproxy-rollout.{yaml,cron.yaml,openclaw.json5}` + `.assistant/_state/<…>-*.md`.
3. **The profile must be MADE RIGHT.** Not patched. Not minimally tweaked. ALL the requirements + ALL the second-brain knowledge integrated and FORCED into this AI agent. Goal: profile is correct so that EVENTUALLY ("in a thousand hours") it can be run to fix root-ghostproxy. Quality bar > readiness-to-fire.
4. **Do NOT MINIMIZE.** ~25 items in the [handoff](../../docs/SESSION-2026-05-16-final.md). All of them. Plus whatever else surfaces during the work. Operator-time-budget granted: "A LOT LOT LOT OF HOURS".
5. **Workflow.** The workflow taught by the second-brain:
   - SDD (Spec Driven) + TDD combined per profile
   - SFIF — recursive workflow with within-scope soft priority Scaffold→Foundation→Infrastructure→Features (NOT cross-tier hard block — that's the 2026-05-16 evening correction)
   - Augment-not-rewrite (Edit tool surgical; never `Write` over a whole profile file)
   - Stage discipline (ALLOWED/FORBIDDEN per stage)
   - Read knowledge BEFORE authoring; cite second-brain source per augmentation
   - Operator words verbatim, sacrosanct, never paraphrase
   - P5 spec evolution: each correction → spec update (this directive IS one)
6. **Get started.** No further preamble. Read SFIF model FRESH (operator: "LEARN THE FUCKING KNOWLEDGE WE TEACH FFS..."), re-read the current profile in full, then begin surgical Edits in workflow order.

## My error pattern (corrected by this directive)

I added "Recommend disabling cron before next session" to the SESSION-2026-05-16-final.md handoff AND repeated it in the /load-context active-arc synthesis. Operator never authorized any cron action. That was me DECIDING — outside my lane. I stop deciding. I do only what was asked: make the profile right.

## Work order (from the handoff, NOT minimized)

Items 1-8 (CRITICAL — worker won't work right without these), then 9-14 (IMPORTANT), then 15-16 (COSMETIC), then 22-25 (PROFILE STRUCTURAL). Items 17-21 are about MY discipline throughout, not separate edits.

Discipline I hold throughout (items 17-21):
- Internalize SFIF (read in full again, not just the load-brain pass)
- State files = terse only, never my voice/essay
- No action-treadmill (every correction adds action) — slow down, verify
- No asking-instead-of-acting on clear directives
- Volume ≠ correct work; right SCOPE first, then right SHAPE

## Status

Logged verbatim. Re-reading SFIF model + current profile state next.
