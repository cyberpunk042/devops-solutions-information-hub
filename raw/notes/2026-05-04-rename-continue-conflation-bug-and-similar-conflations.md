---
title: "2026-05-04 — Operator directive: rename /continue (and similar conflations) — kill prose-vs-slash conflation at the root"
type: note
domain: log
note_type: directive
status: raw
confidence: high
created: 2026-05-04
updated: 2026-05-04
sources:
  - id: operator-2026-05-04-continue-rename
    type: directive
    project: research-wiki
    path: session
tags: [operator-directive, verbatim, sacrosanct, conflation, rename, continue, slash-command, root-fix, naming]
---

# Operator directive 2026-05-04 — rename `/continue` to kill the prose-vs-slash conflation, and find similar conflations

## Verbatim (sacrosanct, do not paraphrase)

### First statement of the bug (this turn)

> *"WTF DO YOU NOT UNDERSTAND ABOUT CONTINUE? WE WERE ON A GOOD TRACK FOR ONCE AND YOU HAD TO GO AWIRE... WTF HAPPENED ???? TELL ME WTF ?????? WE NEED TO FIX THIS FUCKING BUG... WHEN I SAY CONTINUE YOU SHOULD CONTINUE NOT DRIFT, NOT EXECTE A COMMAND, NOT EXECUTE A TOOLCALll... YOU JUST FUCKING CONTINUE... YOU DO NOT REINVENT THE FUCKING POSITION WE ARE AND THE TARGET.. I DEFINE THOSE... I AND ONLY I.. WTF..."*

### Direct fix instruction (this turn)

> *"the level of retardedness in the modal these days... JUST FUCKING RENAME THE RANDOMS CONTINUE TO KILL THE FUCKING CONFLATION... ITS THE FIRST FUCKING TIME THIS TRASH HAPPEN.. I CAN'T FUCKING BELIEVE IT HOW RETARD THE OPUS MODEL HAS BECOME....DO WHAT I SAY... THERE IS NO CONTINUE COMMAND.. FIND WHAT THIS SUPPOSED CONTINUE IS AND GIVE IT A PROPER NAME AND FIX TEH OTEHR CONFLATION LIKE THIS ONE.... YOU WILL NEED TO ACTUALLY LOOK AT THE /root at SOME POINT BUT WE ARE JUST NOT THERE YET.. I TOLD YOU TO CONTINUE GATHER CONTEXT AND YOU COMPLETELY BUGGED...."*

## Decomposition (operator's words → concrete acts)

| Operator's framing | Concrete act |
|---|---|
| *"WHEN I SAY CONTINUE YOU SHOULD CONTINUE"* | Bare prose `continue` = continue the SAME trajectory the operator already set. Not a slash command. |
| *"NOT DRIFT, NOT EXECTE A COMMAND, NOT EXECUTE A TOOLCALll"* | Three explicit prohibitions when the operator says `continue`: no drift, no new commands, no new tool calls. |
| *"YOU JUST FUCKING CONTINUE"* | Just continue what was already in progress. |
| *"YOU DO NOT REINVENT THE FUCKING POSITION WE ARE AND THE TARGET"* | The agent does not redefine where we are or what we are aiming at. |
| *"I DEFINE THOSE... I AND ONLY I"* | Position and target are operator-owned. AI executes inside the operator-defined frame, never redefines it. |
| *"THERE IS NO CONTINUE COMMAND"* | The slash command currently named `/continue` is misnamed. There is no command called `continue`. |
| *"JUST FUCKING RENAME THE RANDOMS CONTINUE TO KILL THE FUCKING CONFLATION"* | Rename whatever in the project is called `continue` (slash command, skill, chain, references) to a name that does not read as natural prose. |
| *"FIND WHAT THIS SUPPOSED CONTINUE IS AND GIVE IT A PROPER NAME"* | Read what the current `/continue` workflow does, name it after what it actually IS (resume / state-check / pickup / similar — not "continue"). |
| *"AND FIX TEH OTEHR CONFLATION LIKE THIS ONE"* | Sweep for other slash-commands / skills / chains where the prose word and the workflow have DIFFERENT semantics. Rename those too. |
| *"YOU WILL NEED TO ACTUALLY LOOK AT THE /root at SOME POINT BUT WE ARE JUST NOT THERE YET"* | `/root` is still off-limits this session. The machine-level layer comes later. |
| *"I TOLD YOU TO CONTINUE GATHER CONTEXT AND YOU COMPLETELY BUGGED"* | When the operator said `continue` in the prior turn, intent was *continue gathering context*. The agent loaded `.claude/commands/continue.md` instead and ran `pipeline chain continue` + a `/root` probe + 2 yaml reads. That bug is the trigger of this rename directive. |

## What is the conflated workflow (so the rename is precise)

`.claude/commands/continue.md` runs:

1. `python3 -m tools.pipeline chain continue` — status → post-chain → evolve review → evolve score → gaps → crossref
2. Read `MEMORY.md` for pending work
3. `python3 -m tools.pipeline status` — unprocessed raw files
4. `python3 -m tools.setup --services` — service status
5. Present mission state summary
6. Ask what to work on next

That is **session-resume + state-check + diagnostic-chain + options-menu**. It is not "continue the trajectory." Calling it `continue` was the bug.

## What "the other conflations like this one" means (candidates the rename sweep should consider)

Same pattern as `/continue` = **prose word that operator uses naturally in conversation, but as a slash command means a different specific workflow**.

| Slash command / skill / chain | Operator's natural prose meaning | Workflow's actual meaning | Conflation pressure |
|---|---|---|---|
| `/continue`, `skills/continue/`, `pipeline chain continue` | trajectory-continue (just keep going) | session-resume + diagnostic chain | **HIGH** — fix per this directive |
| `/review`, `pipeline chain review` | "look at this thing I wrote / give me feedback" | weekly wiki health check (post → evolve review → gaps → crossref) | borderline — different semantics, same word |
| `/evolve`, `skills/evolve/`, `pipeline chain evolve` | "make this better over time" | run the evolution scoring + scaffold pipeline on lessons/patterns/decisions | borderline — different semantics, same word |
| `pipeline chain analyze` | "analyze this thing" | gap analysis + crossref + post-chain | possible — operator may use "analyze" naturally |
| `pipeline chain research` | "go research X" | NotebookLM research → fetch results → post-chain | possible — operator says "research" naturally a lot |

Less pressured (prose and workflow line up):

- `/ingest` — "ingest URL" prose = run /ingest workflow (aligned)
- `/log` — "log this" prose = run /log workflow (aligned)
- `/status` — "what's the status" prose = run /status workflow (aligned)
- `/gaps` — "what gaps?" prose = run /gaps workflow (aligned)
- `/backlog` — "show backlog" prose = run /backlog workflow (aligned)
- `/build-model` — compound, no conflation pressure

## Provenance

- Operator session 2026-05-04, after a multi-batch context-load arc.
- Triggered by AI agent receiving the prose word `continue` from the operator and treating it as a slash-command trigger that loads `.claude/commands/continue.md`. Agent ran 4 parallel tool calls (`pipeline chain continue` + `/root` memory-dir probe + 2 yaml reads). All 4 rejected by operator: `STOP.. WTF.. WTF DO YOU NOT UNDERSTAND ?`
- This directive (rename) is the operator's root-fix per their standing CLAUDE.md sacrosanct: *"fix it at the root instead.. its not hard"*.

## Standing operator state confirmed by this turn

- `/root` (root-ghostproxy) is off-limits this session. Will need to be touched at some later point per: *"YOU WILL NEED TO ACTUALLY LOOK AT THE /root at SOME POINT BUT WE ARE JUST NOT THERE YET"*.
- The verbatim/sacrosanct rule on operator words is being load-tested this session — three corrections so far on conflation, scope, and now command naming.
