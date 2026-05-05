# Checkin — Mission State-and-Options Report

You are running a **mission checkin** on the devops-solutions-research-wiki — diagnostics, state report, options for what to work on next. This is a research-grade knowledge synthesis system and second brain.

> **CRITICAL — disambiguation.** This skill loads when the operator types `/checkin` LITERALLY. Bare prose like "continue" / "resume" / "where are we" in conversation is **trajectory-continue** — keep doing what was already in progress, **do not** trigger this skill, **do not** run new tool calls. See operator directive 2026-05-04 (`raw/notes/2026-05-04-rename-continue-conflation-bug-and-similar-conflations.md`).

Read CLAUDE.md for conventions. Read the most recent SESSION-* artifact in `docs/` for the prior session's handoff context.

## On Activation (`/checkin` slash invocation only)

Run these steps in order. Report results to the user after each.

### 1. Diagnostic chain

Run: `python3 -m tools.pipeline chain checkin`

This executes: status → post-chain → evolve review → evolve score → gaps → crossref.
Report: page count, relationship count, validation errors, candidates, gaps.

### 2. Check Memory

Read the auto-memory `MEMORY.md` to recall user preferences, active projects, and pending work.

The memory path is per-machine: `~/.claude/projects/<encoded-cwd>/memory/MEMORY.md` where `<encoded-cwd>` is the current working directory with `/` → `-`. The harness exposes this in its file-based memory layer.

### 3. Check Unprocessed Raw Files

Run: `python3 -m tools.pipeline status`

If raw file count exceeds wiki page count significantly, there are unprocessed sources.

### 4. Present Mission State

Summarize in a table:
- Wiki stats (pages, relationships, layers, maturity distribution)
- Evolution candidates (top 5 from the score step)
- Gaps (orphans, weak domains, open question count)
- Pending work (from memory)
- Sync status: `python3 -m tools.setup --services`

### 5. Ask What's Next

Present actionable options:
- "Ingest new sources" → user provides URLs or topics
- "Evolve next batch" → scaffold + fill top candidates
- "Deepen weak domains" → focus on domains with few pages
- "Research gaps" → use web search to find sources for open questions
- "Review and promote" → check maturity promotions
- "Export to projects" → push to openfleet/AICP/OpenArms

## Available Tools

All wiki operations are available via:
- **CLI**: `python3 -m tools.pipeline <command>` (see CLAUDE.md for full list)
- **MCP**: wiki tools registered in `.mcp.json`
- **Skills**: wiki-agent (ingest/query), evolve (evolution pipeline), checkin (this), model-builder, notebooklm
- **Chains**: `pipeline chain --list` for all named chains

## Key Chains

| Chain | Purpose |
|-------|---------|
| `checkin` | Mission state-and-options diagnostic (this skill's backend) |
| `review` | Weekly health check |
| `health` | Post → gaps → crossref |
| `evolve` | Score → scaffold → post |
| `evolve-auto` | Score → scaffold → generate (local model) → post |
| `full` | Fetch → post → gaps → crossref → sync |
| `publish` | Post → sync to Windows |
