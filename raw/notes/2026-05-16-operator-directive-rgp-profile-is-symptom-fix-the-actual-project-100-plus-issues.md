---
title: "2026-05-16 — Operator directive: RGP-profile is symptom; fix the actual root-ghostproxy project based on 100+ reported issues/bugs/glitches"
type: note
note_type: directive
domain: log
status: active
confidence: authoritative
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: operator-directive-2026-05-16-rgp-profile-is-symptom
    type: directive
tags: [operator-directive, root-ghostproxy, rgp-profile-is-symptom, 100-plus-issues, systemic-bugs, fix-the-actual-project, "2026-05-16"]
---

# Operator directive — RGP profile is symptom; fix the actual project (100+ reported issues)

## Verbatim operator words (sacrosanct, 2026-05-16, in order)

> "TELL WTF IS NOT CLEAR AND WHY IS THE AI ASSISTANT NOT WORKING ON THE 200+ EPICS and tasks that are needed to fix root-ghostproxy ?"

Then (clarifying immediately):

> "THE ONLY REASON THERE IS A ROOT-GHOSTPROXY PROFILE IN THE SECOND-bRAIN IS BECAUSE ITS BROKEN AND IT COULD NOT WORK.. WE NEED TO FIX THE WHOLE PROJECT.. BASED ON EVERY OF THE 100+ REPORTED ISSUES AND SYSTEMIC BUGS AND GLITCH AND ETC..."

## What this re-frames

The RGP profile in `~/.openclaw/agents/root-ghostproxy-rollout/` is **not the deliverable**. It is a **symptom-fix scaffolding** that exists only because the actual root-ghostproxy project is broken and cannot work on its own.

The deliverable is: **fix root-ghostproxy itself**, based on the 100+ reported issues / systemic bugs / glitches.

Implications:
1. RGP profile's current behavior (observe + surface multi-vision cascade-candidates in `wiki/`) is NOT progress on the actual project.
2. The cross-project boundary that says "RGP cannot edit root-ghostproxy repo content" is the PROBLEM, not the rule — that boundary is why nothing concrete is being shipped.
3. The 100+ reported issues are the real backlog. Need to locate them and start working through them.
4. "Over a year of work" framing implies a large concrete bug-list, not the 10 SFIF modules in wiki/backlog/ (which describe the rollout *of* root-ghostproxy as a second-brain sister, not the *fix-the-100+-bugs* work).

## What I need to determine next

1. WHERE are the 100+ reported issues? Candidates:
   - `/root/BUGS.md` or `/root/ISSUES/` directory
   - GitHub issues on the upstream repo (`cyberpunk042/root-ghostproxy`)
   - Operator directive notes (`raw/notes/`) — particularly the 2026-05-08 pain-points-inventory note ("pain-points-inventory-from-root-failed-conversation-master-aggregate")
   - `wiki/log/2026-05-08-sister-project-investigation-kickoff-spec-root-ghostproxy-foundational-triplet-adaptation.md`
   - The RGP profile workspace's own observation logs
2. Is the actual project source tree accessible from here? (likely `/root/` — need to verify permission)
3. What's the OBSERVATION mode RGP should be in vs the EXECUTION mode it needs to be in?

## Status

Logged. Investigation continuing.
