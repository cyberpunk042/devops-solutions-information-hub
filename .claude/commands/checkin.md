Mission state-and-options checkin — diagnostic + memory + pending-work report.

> **CRITICAL — disambiguation.** This command runs ONLY when the operator types `/checkin` LITERALLY (slash + name). Bare prose words like "continue", "resume", "where are we" are trajectory-continue, NOT triggers for this command. When the operator says "continue" in conversation, it means *continue the same trajectory we are already on* — do not initiate any new tool calls or commands. See `raw/notes/2026-05-04-rename-continue-conflation-bug-and-similar-conflations.md`.

## On `/checkin`

1. Run `python3 -m tools.pipeline chain checkin` and report the results
2. Read the auto-memory `MEMORY.md` for pending work (path varies per machine; resolve via `~/.claude/projects/<encoded-cwd>/memory/MEMORY.md`)
3. Run `python3 -m tools.pipeline status` to check for unprocessed raw files
4. Run `python3 -m tools.setup --services` to check service status
5. Present a summary table: pages, relationships, validation, candidates, gaps, pending work
6. Ask what to work on next: ingest, evolve, deepen, research gaps, export, or review
