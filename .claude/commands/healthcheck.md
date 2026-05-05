Wiki weekly health check (slash-invoked audit).

> **CRITICAL — disambiguation.** This command runs ONLY when the operator types `/healthcheck` LITERALLY. Bare prose `review` / `look at this` / `give me feedback` is NOT a trigger — when the operator uses "review" in conversation it is feedback-language, not a workflow trigger; do not run any chain or new tool calls. The built-in `/review` skill in Claude Code is for PR review (separate scope). See `raw/notes/2026-05-04-rename-continue-conflation-bug-and-similar-conflations.md`.

## On `/healthcheck`

1. Run `python3 -m tools.pipeline chain healthcheck`
2. Report: validation errors, maturity promotions available, stale pages, gaps, crossref opportunities
3. If promotions available, list them and ask which to promote
4. If gaps found, suggest next research targets
5. If comparison candidates found, ask which to create
