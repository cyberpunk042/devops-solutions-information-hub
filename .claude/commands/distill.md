Knowledge-distillation pipeline (slash-invoked).

> **CRITICAL — disambiguation.** This command runs ONLY when the operator types `/distill` LITERALLY. Bare prose `evolve` / `promote` / `improve` / `let it grow` is NOT a trigger. The wiki's CONCEPT of "knowledge evolution" / "evolved pages" / "maturity promotion" is unchanged in vocabulary — only the workflow trigger is renamed to kill prose conflation. The CLI subcommand `pipeline evolve --score` is also retained (operator types it explicitly; not a conflation). See `raw/notes/2026-05-04-rename-continue-conflation-bug-and-similar-conflations.md`.

## On `/distill`

1. Run `python3 -m tools.pipeline evolve --score --top 10` to show candidates
2. Present the ranked candidates and ask what to do:
   - "scaffold" → `python3 -m tools.pipeline evolve --scaffold --top N`
   - "generate" → fill scaffolded pages with real content (this session)
   - "review" → `python3 -m tools.pipeline evolve --review` for maturity promotions
   - "stale" → `python3 -m tools.pipeline evolve --stale` for freshness check
3. After any generation, run `python3 -m tools.pipeline post`
