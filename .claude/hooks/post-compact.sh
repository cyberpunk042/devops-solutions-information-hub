#!/usr/bin/env bash
# PostCompact hook — restore behavioral state after context compaction.
# Exit 0 = allow continuation.
#
# Insertion: PostCompact
# Reason: Compaction loses behavioral corrections, sacrosanct directives, and Hard Rules.
#         Per [[context-compaction-is-a-reset-event]] — all illnesses return after compaction.
#         Without restoration, agent reverts to base-model defaults.
# Remediation: re-print sacrosanct directives + Hard Rules + pointer to recent verbatim log.

cat <<'EOF'
═══════════════════════════════════════════════════════════════════════════
POST-COMPACTION STATE RESTORATION — RESEARCH WIKI
═══════════════════════════════════════════════════════════════════════════

Compaction just occurred. Behavioral corrections are LOST. Re-internalize NOW.

OPERATOR DIRECTIVES (sacrosanct — see CLAUDE.md, raw/notes/2026-04-24-*):
  • "do what is asked. not do what you were not asked to do"
  • "behave FROM the project, not OVER it"
  • "the project is intelligent. the intelligence comes from USING the project"
  • "my words are sacrosanct — quote me verbatim all the time"
  • "everything evolves and everything is flexible"
  • "its not because I add something that you can discard everything I asked
     you before... when I add information, I add... I do not ask you to ignore
     the past"
  • "fix it at the root instead.. its not hard"

NEXT STEPS (mandatory after compaction):
  1. Re-read CLAUDE.md (operational program)
  2. Re-read .claude/rules/learnings.md (failure modes — most-recent first)
  3. Read raw/notes/$(date +%Y-%m-%d)-*.md if it exists (today's directives)
  4. Run .venv/bin/python -m tools.gateway orient before first work action

WHAT THE AGENT MUST NOT FORGET:
  • URL ingestion → pipeline fetch / wiki_fetch MCP (NEVER WebFetch on corpus URLs)
  • Status claims need inline verification (P4 — Declarations Aspirational Until Verified)
  • Read internal-tool output IN FULL (no | head / | tail by default)
  • Don't fabricate bugs / declarations / state operator never named
  • Verbatim quoting is the alignment mechanism — don't paraphrase
  • Behave FROM the project (use MCP/CLI/loaded knowledge) not OVER it (improvise)

ACTIVE HOOKS still wired (no need to recreate):
  pre-webfetch-corpus-check.sh / pre-bash.sh / session-start.sh / post-compact.sh

═══════════════════════════════════════════════════════════════════════════
EOF
exit 0
