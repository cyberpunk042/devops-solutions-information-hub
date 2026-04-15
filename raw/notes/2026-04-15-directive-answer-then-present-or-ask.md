---
title: "Operator directive — answer questions then present for confirmation, or just ask"
type: note
domain: log
status: active
note_type: directive
created: 2026-04-15
updated: 2026-04-15
tags: [operator-directive, verbatim, process, questions, confirmation, no-floating-questions]
---

# Operator Directive — Answer Then Present, or Just Ask

## Verbatim Operator Message

> "approve all and continue. when you have question, you try to answer and you present to me for confirmation or just ask me."

## The Directive

When I have a question during work, I have two valid responses:

1. **Answer it myself first, then present the answer for operator confirmation.** ("I think X because Y. Confirm?")
2. **Just ask the operator directly.** When I genuinely don't know and can't derive an answer.

**Not valid:**
- Leaving the question floating unresolved in output/notes
- Presenting a question as "open" when I could have answered it
- Defering to the operator by default when I have enough evidence to propose an answer

## How This Applies

- Open Questions in wiki pages — where I have fresh context or can cross-reference, attempt an answer + mark as RESOLVED with reasoning, per wiki convention
- Design decisions mid-work — propose the answer with rationale, then confirm with operator
- Edge cases — think through implications first, bring operator a shaped question with my analysis, not a raw "what should we do?"
- Ambiguous instructions — propose my interpretation + confirm, don't hedge

## Why This Was Logged

Per `feedback_verbatim_always.md` — operator directives logged verbatim in `raw/notes/` BEFORE acting. This is a standing process rule going forward.
