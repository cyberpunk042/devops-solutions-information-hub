# 2026-05-08 — Operator directive: ingest 5 URLs (subagent patterns 2026 + Google TPU diffusion-style speculative decoding + 3 YouTube videos) and continue

> Verbatim operator directive log — Hard Rule #4 + AGENTS.md Hard Rule #3. Logged BEFORE acting.

## Verbatim (sacrosanct)

> *"ingest:*
>
> *https://www.philschmid.de/subagent-patterns-2026*
>
> *https://www.youtube.com/watch?v=ppCZfjLdSY8*
> *https://www.youtube.com/watch?v=Quj3M5gqxT8*
> *https://www.youtube.com/watch?v=JdqJ2ekWt8M*
>
> *https://developers.googleblog.com/supercharging-llm-inference-on-google-tpus-achieving-3x-speedups-with-diffusion-style-speculative-decoding/*
>
> *and continue"*

## URL routing

| URL | Type | Pipeline destination |
|---|---|---|
| philschmid.de/subagent-patterns-2026 | Article | `raw/articles/<slug>.md` |
| youtube.com/watch?v=ppCZfjLdSY8 | YouTube video | `raw/transcripts/<slug>.txt` (youtube-transcript-api, venv-only) |
| youtube.com/watch?v=Quj3M5gqxT8 | YouTube video | `raw/transcripts/<slug>.txt` |
| youtube.com/watch?v=JdqJ2ekWt8M | YouTube video | `raw/transcripts/<slug>.txt` |
| developers.googleblog.com/supercharging-llm-inference-on-google-tpus-... | Article | `raw/articles/<slug>.md` |

## "and continue"

Forward-motion cadence. After ingestion + synthesis, stay in the active arc — meaning the carry-forward from the prior turn (2 inbox lessons pending operator-decision; 10 cross-source convergence candidates from `evolve --score`; path-versatility lesson at `01_drafts/seed`).

## Plan

1. Log directive verbatim — done (this file)
2. Pipeline fetch all 5 URLs (batch, .venv/bin/python)
3. Read raws in full per AGENTS.md Hard Rule #4 (`wc -l` first; offset reads for >200 lines)
4. Author source-synthesis page per raw at `wiki/sources/tools-integration/src-<slug>.md` (≥0.25 ratio per artifact-types.yaml)
5. Pipeline post (Hard Rule #10 — 0 errors required)
6. Pipeline crossref
7. Report: pages created, relationships added, new connections found
