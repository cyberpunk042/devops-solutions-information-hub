---
title: "Operator directive — new ingestions 2026-04-24 (AIDLC + Firecrawl + YouTube)"
type: note
domain: cross-domain
note_type: session
status: active
confidence: high
created: 2026-04-24
updated: 2026-04-24
tags: [raw, operator-directive, ingestion, aidlc, firecrawl, youtube, tts]
---

## Verbatim directive (2026-04-24)

> The new ingestions:
> https://www.youtube.com/watch?v=Edpsu61cwG8 (might want to do TTS with the Wiki here and/or and openclaw|openarms agent)
> https://github.com/firecrawl/firecrawl
> https://github.com/awslabs/aidlc-workflows
>
> or even: https://github.com/ijin/aidlc-cc-plugin (to take with a grain of salt)

## Parsing notes (not content — routing only)

- **YouTube** (`Edpsu61cwG8`): operator flags **TTS/transcript via wiki and/or openclaw|openarms agent** as the likely capture path — not a straight WebFetch. The video itself is opaque to me.
- **firecrawl/firecrawl**: scraping/crawling tool. Directly fetchable. Candidate `source-synthesis` under `tools-integration`.
- **awslabs/aidlc-workflows**: THE AIDLC source the operator previously deferred ("stay focus on the present for now" on 2026-04-23). Now in scope. Directly fetchable.
- **ijin/aidlc-cc-plugin**: community Claude Code plugin. Operator flags **"take with a grain of salt"** — treat as secondary/unofficial; note authority tier explicitly in the synthesis.

## Ordering

Priority-order per operator listing: YouTube, Firecrawl, awslabs/aidlc-workflows, ijin/aidlc-cc-plugin.
YouTube is TTS-agent-blocked for me → back of the queue in practice; the three repos go first.
