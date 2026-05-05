---
title: "2026-05-05 — Operator directive: rules files at /root + ccstatusline module before Suricata/PolarProxy"
type: note
domain: cross-domain
status: raw
confidence: high
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-rules-and-ccstatusline
    type: directive
tags: [note, operator-directive, sacrosanct, verbatim, rules-files, ccstatusline, module-ordering, claude-code-statusline]
---

# Operator directive — 2026-05-05 mid-readiness-loop

## Verbatim

> "have we done the rules files too ? normally its part of the process. what is there is propably only scafold files in /root. and the hooks an the cross project vision. we are also going to have a simpler module for ccstatusline custom widget so my claude code interface is better and we can even load different profile such as one that allow to see the selected-task, progress, stage and etc... + the obvious normal stuff  I need such as context and context usage and billing usage, 5h windows, 7d + tokens and etc... I am not saying do it now. I am saying this is one of the modules and it will be before suricata and polarproxy. continue. if you need to update the loop now you can too."

## Decomposition (operator's substance, not paraphrased)

1. **Question** — "have we done the rules files too ?" — about `/root/.claude/rules/` files. Operator notes "normally its part of the process."

2. **Observation** — "what is there is propably only scafold files in /root. and the hooks an the cross project vision." Operator confirms current /root state is scaffold + hooks + cross-project vision.

3. **Directive (new module addition)** — "we are also going to have a simpler module for ccstatusline custom widget so my claude code interface is better and we can even load different profile such as one that allow to see the selected-task, progress, stage and etc... + the obvious normal stuff  I need such as context and context usage and billing usage, 5h windows, 7d + tokens and etc..."

4. **Ordering** — "I am not saying do it now. I am saying this is one of the modules and it will be before suricata and polarproxy."

5. **Permission/instruction** — "continue. if you need to update the loop now you can too."

## What the new module covers (operator's words)

- "ccstatusline custom widget" so Claude Code interface is better
- Profile-loadable widgets:
  - selected-task
  - progress
  - stage
  - "and etc..."
- "obvious normal stuff" — context, context usage, billing usage, 5h windows, 7d, tokens, "and etc..."

## Ordering constraint

Before M005 (the current "First specialized feature module" — Suricata/PolarProxy). Operator reaffirms it's a module, not the immediate work.

## Action plan (this readiness pass)

1. Log this directive verbatim — done (this file).
2. Port rules files from second brain to `/root/.claude/rules/` (currently only `words-are-sacrosanct.md` exists there; the rest of the second brain set is missing).
3. Add a new module page in `/root/wiki/backlog/modules/` for the ccstatusline module.
4. Place it in the SFIF Features stream BEFORE the current M005.
5. Update `/root/CONTEXT.md` and the relevant index pages to reflect the new module + the ordering note.
6. Do NOT implement the ccstatusline functionality this iteration — operator's words: *"I am not saying do it now."*

## No-conflate guard

- This is NOT a rejection of any prior work.
- This is NOT a redirect away from "100% session work readiness."
- This IS additive: layered onto the existing readiness work.
- The "rules files" question is a flagged-gap to close, not a complaint.
- The ccstatusline module is a new backlog entry, not an immediate implementation task.
