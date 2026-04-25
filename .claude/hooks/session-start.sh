#!/usr/bin/env bash
# SessionStart hook — print loaded-knowledge reminder so the agent enters with the
# operational program ambient (not just CLAUDE.md auto-load).
# Exit 0 = allow continuation.
#
# Insertion: SessionStart
# Reason: Agent enters session without the super-model / 4 principles / methodology
#         actively loaded. Reminder ensures the agent invokes `gateway orient` and
#         re-reads the rules files before first work action.
#         .claude/rules/self-reference.md, addresses Gap 1 of the refactor gap-analysis.
# Remediation: print structured reminder pointing at next-step commands.

cat <<'EOF'
═══════════════════════════════════════════════════════════════════════════
RESEARCH WIKI — SESSION-START REMINDER
═══════════════════════════════════════════════════════════════════════════

You are INSIDE the second brain. Behave FROM the project, not OVER it.
The project IS the intelligence. The intelligence comes from USING it.

BEFORE first work action:
  .venv/bin/python -m tools.gateway orient

LOADED-KNOWLEDGE LAYERS (read these on demand by topic):
  CLAUDE.md ........................................ operational program (always loaded)
  AGENTS.md ........................................ universal cross-tool rules
  CONTEXT.md ....................................... identity profile + active epics
  .claude/rules/routing.md ......................... operator intent → tool table + 30-tool MCP catalog
  .claude/rules/methodology.md ..................... 5 stages, 9 models, schema, gates
  .claude/rules/self-reference.md .................. this project IS the second brain
  .claude/rules/learnings.md ....................... failure modes to avoid (incl. 2026-04-24)
  .claude/rules/work-mode.md ....................... solo session, output discipline, PO approval
  .claude/rules/ingestion.md ....................... URL ingestion routing detail
  .claude/rules/hook-architecture.md ............... hook design pattern + determinism levels
  wiki/spine/super-model/super-model.md ............ what this system IS
  wiki/lessons/04_principles/hypothesis/ ........... the 4 governing principles
  wiki/config/methodology.yaml ..................... 9 models, 5 stages, ALLOWED/FORBIDDEN

HARD RULES (every message):
  1. Read command output IN FULL (no | head / | tail without REASON env)
  2. When told to execute, execute (don't probe --help)
  3. Use dedicated tools (Read not cat, Grep not grep, Glob not find, Edit not sed)
  4. Operator words are SACROSANCT — quote verbatim, never paraphrase
  4a. Adding ≠ discarding — new direction layers on prior, never overwrites
  5. Use .venv/bin/python for tools.* invocations
  6. URL ingestion → pipeline fetch / wiki_fetch MCP, NEVER WebFetch on corpus URLs
  7. Status claims must inline verification command output
  8. Behave FROM the project, not OVER it
  9. Don't fabricate — investigate via project tools first
  10. pipeline post after every wiki change (0 errors required)

ACTIVE HOOKS (deterministic enforcement):
  pre-webfetch-corpus-check.sh ..................... blocks WebFetch on corpus URLs
  pre-bash.sh ...................................... blocks reflexive truncation pipes
  session-start.sh ................................. this reminder
  post-compact.sh .................................. restores state after compaction

MECHANISM DETERMINISM (per operator 2026-04-24):
  Commands (.claude/commands/) ..................... 100% deterministic, operator slash-invoked
  Skills (.claude/skills/) ......................... ~70% deterministic, auto-trigger (NOT YET BUILT in this project)
  Hooks (.claude/hooks/) ........................... logical insertion + reason + remediation
  MCP tools (30 available) ......................... programmatic, deferred-load via ToolSearch
  CLI (tools.pipeline / tools.gateway / etc.) ...... programmatic, via Bash

═══════════════════════════════════════════════════════════════════════════
EOF
exit 0
