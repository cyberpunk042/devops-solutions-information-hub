---
title: "2026-05-16 — Operator directive: why is the RGP AI assistant not working on the 200+ epics/tasks?"
type: note
note_type: directive
domain: log
status: active
confidence: authoritative
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: operator-directive-2026-05-16-rgp-200-epics-not-being-worked
    type: directive
tags: [operator-directive, root-ghostproxy, rgp, ai-assistant-not-working, 200-plus-epics, "2026-05-16"]
---

# Operator directive — why is RGP not working on the 200+ epics/tasks

## Verbatim operator words (sacrosanct, 2026-05-16)

> "TELL WTF IS NOT CLEAR AND WHY IS THE AI ASSISTANT NOT WORKING ON THE 200+ EPICS and tasks that are needed to fix root-ghostproxy ?"

Also (from the trailing remark on the prior `/load-context` directive, same arc):

> "then we will look at the root-ghostproxy-rollout.. its doing nothing and there is like for over a year of work lol"

## Operator-asserted facts

1. There are 200+ epics and tasks that exist and are needed to fix root-ghostproxy.
2. The RGP AI assistant is NOT working on them.
3. RGP is "doing nothing."
4. The workload feels like "over a year of work."

## What I need to determine

1. Where are the 200+ epics/tasks? (`wiki/backlog/`? `wiki/domains/cross-domain/`? RGP profile's own workspace?)
2. Is the RGP profile installed + enabled + cron-firing post-gateway-fix?
3. If cron is firing, what is RGP actually doing in those runs (or not doing)?
4. What's the gap between "RGP fires" and "RGP picks up + acts on the 200+ epics"?

## Status

Logged. Investigation in progress this same turn.
