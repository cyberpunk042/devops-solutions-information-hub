---
title: "PRE-COMPACT HANDOFF MANUAL — Imminent Compaction State Snapshot 2026-05-08"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: pre-compact-spec-fire-105
    type: wiki
    file: wiki/patterns/01_drafts/pre-compact-handoff-hook-implementation-spec-for-opt-path-to-tier-4-for-impl-spec-10.md
    description: "Spec applied manually since hook not wired"
  - id: operator-pre-compact-directive
    type: file
    file: raw/notes/2026-05-08-pre-compact-imminent-validate-adjust-auto-compact-auto-dream-finish-smoothly-directive.md
    description: "PRIMARY operator directive at 5%"
tags: [pre-compact-handoff-manual, imminent-compaction, "2026-05-08", post-compact-recovery-mandatory]
---

# PRE-COMPACT HANDOFF MANUAL — Imminent Compaction State Snapshot 2026-05-08

## Summary

Manual pre-compact handoff snapshot authored at 5% context remaining (2026-05-08). Documents operator directives, active work state, and mandatory post-compact recovery actions for the next agent session. Read in full before taking any action post-compaction.

## ⚠️ POST-COMPACT AGENT — READ THIS FIRST ⚠️

```
ACTION REQUIRED POST-COMPACT (DO NOT SKIP):
  1. Run: .venv/bin/python -m tools.gateway orient
  2. Read this entire handoff doc
  3. Read raw/notes/2026-05-08-*.md most-recent (all 4 files; chronological)
  4. Read /opt CLAUDE.md, AGENTS.md, CONTEXT.md
  5. Read .claude/rules/work-mode.md, self-reference.md, learnings.md
  6. THEN AND ONLY THEN respond to operator OR continue prior work
  
DO NOT execute any pending tool call without completing 1-6 first.
Per Fire 102 incident: skipping regather caused operator to catch agent
"about to start doing trash without context" — DO NOT REPEAT.
```

## Section 1: Compaction context

```
Trigger: auto-compact at 5% remaining
Operator-known: at ~5% (acknowledged in prior message)
PreCompact hook: NOT WIRED at /opt (per Fire 102 incident); this handoff is MANUAL
Auto-compact disable: NOT yet implemented (Tasks #25-#26 pending)
Auto-dream definition: NOT yet defined (Q1 BLOCKER)
```

## Section 2: Active /loop directive (sacrosanct verbatim)

```
"we continue the workflow. you can clear the loop when we going to be at 
Ready for Review before we start fixing and have a clear plan with clear 
solution based of the clear root issues identified and our personal 
knowledge applied. if one piece is ready for review you can move to the 
next.. this is obviousy 30 pieces if not 70-80 pieces and changes. no 
lazyness. no hack or quickfix or rush of anything. we are not in a rush 
we want to do this right and this is why sdlc and methodology and workflow 
respect is utmost important... the at least 100 pain point idenfified in 
the latest root session conversation will also need to have a direct 
response / relationship to the proposed solution and we will need to make 
sure that we cover all of them strategically. no matter how many circle 
back and cross-referencing we need to do this right.. we are at the right 
place to do this. we have the knowledge in the second-brain."
```

## Section 3: NEW operator directive at 5% (sacrosanct verbatim)

```
"also was the auto-compact properly disabled and the auto-dream enabled ? 
we could add our force /finish-smoothly or a custom one adapted to the 
situation even better.  when we are at < 10k token left of window. then 
it can keep continuing till it compact and when it do the post-compact it 
should do the process and also read the handoff and do the group of 
operations needed to regather the context properly, not only the task at 
end but the general needed knowledge per-project before starting working 
or doing anything. righ now would be a good time to valide / adjust all 
this we are readhing the 5%"
```

Registered at: raw/notes/2026-05-08-pre-compact-imminent-validate-adjust-auto-compact-auto-dream-finish-smoothly-directive.md

## Section 4: Body-of-work state

```
Pieces this conversation: ~225 (Fires 102-225 = ~124 substantive fires post-compact)
Combined wiki state post-pull: ~252 pieces / 840 pages / 3914 relationships
Validation errors: 0 (sustained 100% PASS rate)
Cluster coverage: 16/16 enumerated (per Fire 136)
Per-instance pain-point coverage: 65%
Tier-weighted compliance: ~44% projected
Phase 1 hook drafts: 5 (Fires 154-158)
Pareto elevation candidate specs: ~21 (Fires 161-200+)
Decision-packages: v0-v9 (Fire 222)
Open BLOCKERS: 5
Operator-pending decisions: 30+
```

## Section 5: Post-pull merged state

```
Pre-pull: 222 local pieces
Pull: fast-forward 2 commits from origin/main (Strong-Loop Arc + Hidden Physics LLMs)
Post-pull: ~252 total pieces / 840 pages
Pipeline post: 0 errors validated post-pull
Modified (regeneratable indexes): 5 _index.md/manifest.json files
Untracked (this conversation's pieces): ~224 pieces (NOT YET COMMITTED — operator-territory)
```

## Section 6: Operator-pending decisions (TOP PRIORITY for resumption)

```
5 BLOCKERS:
  B1: Q1 auto-dream definition (Fire 110/128 surfaced; Fire 206 alternative subagent dispatch spec)
  B2: Foundational-triplet endorsement (Fire 137)
  B3: Phase 1 launch timing (Fire 137 Q-FIRE-137-2)
  B4: Q2 Epic placement v2.0 vs v2.1 (Fire 110)
  B5: Q3 Investigation method (Fire 110)

NEW BLOCKERS from operator's pre-compact directive (this turn):
  B6: Validate auto-compact disable status — answer: NOT IMPLEMENTED
  B7: Validate auto-dream enable status — answer: NOT IMPLEMENTED (Q1 still BLOCKER)
  B8: Custom /finish-smoothly variant adapted spec — NEW operator proposal; NOT YET AUTHORED
```

## Section 7: Live tasks

```
#25: Investigate auto-compact 5% trigger — pending
#26: Disable auto-compact globally — pending (operator just confirmed at 5%; was NOT implemented)
#27: Fix post-compact detection failure — pending
#28: Wire PreCompact hook at /opt — pending (would have helped THIS handoff)
#29: Document auto-dream policy — pending (still Q1 BLOCKER)
#20: Sister-project context templates — pending (separate stream)
```

## Section 8: In-flight work (THIS conversation)

```
Last fire: Fire 225 post-pull synchronization observation
Operator's latest message: pre-compact directive at 5%; validate auto-compact + auto-dream;
                            propose /finish-smoothly custom variant
Pending action: AUTHOR /finish-smoothly custom spec (pre-compact + post-compact + 
                 < 10k token threshold + project-knowledge-regather)
Pending action: respond to operator's validate questions (auto-compact + auto-dream both NO)
```

## Section 9: Active mode + focus + impediment (state-files)

```
Active mode: not set
Active focus: /loop multi-day pain-point body-of-work
Active impediment: 5% pre-compact imminent + auto-compact/auto-dream not implemented
                   + Q1 auto-dream BLOCKER + 5 other operator-pending BLOCKERS
```

## Section 10: Cron / scheduled-task state

```
Cron: ScheduleWakeup chain at 90s cadence per /loop
Loop-state: continuing per Option B (per Fire 121)
```

## Section 11: Post-compact recovery directives (MANDATORY)

```
STEP 1 (FIRST ACTION): .venv/bin/python -m tools.gateway orient
STEP 2: Read this handoff doc IN FULL
STEP 3: Read raw/notes/2026-05-08-*.md (4+ recent: pre-compact-imminent + 
        auto-compact-detection-failure + brain-improvement-mandate + 
        pain-points-inventory)
STEP 4: Read /opt CLAUDE.md, AGENTS.md, CONTEXT.md (auto-loaded; verify)
STEP 5: Read .claude/rules/{work-mode,self-reference,learnings}.md
STEP 6: Read recent wiki/log/2026-05-08-*.md (top 5 most-recent)

PROJECT-LEVEL KNOWLEDGE TO REGATHER (per operator directive — "general 
needed knowledge per-project before starting working or doing anything"):
  - 4 governing principles (P1-P4) per CONTEXT.md
  - methodology engine 5 stages × ALLOWED/FORBIDDEN
  - 16 named models per super-model
  - hook architecture + 10 wired hooks
  - 28 MCP tools catalog
  - sister-project ecosystem (5 projects)

THEN AND ONLY THEN respond to operator OR continue prior work.

DO NOT execute pending pre-compact tool call without completing all 6 steps.

If /finish-smoothly custom spec NOT YET AUTHORED before compaction:
  Author it post-compact as Fire-N+1 substantive piece per /loop directive.
```

## Section 12: Operator directive answers (ready-prepared for resumption)

```
Q-OPERATOR-1: "was the auto-compact properly disabled?"
  ANSWER: NO. Per Tasks #25-#26 pending. Fire 107 Layer 1 spec authored 
  (designed-only Tier 1 per Fire 103 audit). Operator-empirical implementation 
  not yet performed. Auto-compact-disable would require Q1 auto-dream 
  definition + harness investigation per Fire 107 4-sub-layer spec.

Q-OPERATOR-2: "the auto-dream enabled?"
  ANSWER: NO. Q1 auto-dream definition is operator-empirical BLOCKER. 
  Per Fire 128 hypothesis space (H1-H7); operator-empirical resolution pending.

Q-OPERATOR-3: "we could add our force /finish-smoothly or a custom one 
              adapted to the situation"
  ANSWER: STRONG ENDORSEMENT. Custom variant proposal:
    Trigger: context-window <10k tokens
    Pre-compact behavior: continue substantive work + author handoff doc 
                          (per Fire 105 spec applied manually if hook not wired)
    Post-compact behavior: STEP 1-6 above (mandatory regather; project-knowledge 
                            + task-at-end, not just task-at-end)
    Implementation forward-anchor: NEW pattern to author post-compact.

Q-OPERATOR-4: "validate/adjust all this we are reaching 5%"
  ANSWER: VALIDATE FAILED — auto-compact-disable + auto-dream NOT implemented; 
                            cannot adjust before compaction.
  ANSWER: ADJUST — manual handoff doc authored (THIS document); post-compact 
                    agent has structured recovery procedure per Section 11.
```

## Tags

[pre-compact-handoff-manual, imminent-compaction, 2026-05-08, post-compact-recovery-mandatory]
