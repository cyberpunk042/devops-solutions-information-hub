#!/usr/bin/env python3
# SessionStart hook (second of two on this event) — direct the agent to invoke
# /orient as its first action. Uses additionalContext JSON for ~85% reliability
# vs ~70% for the plain-text session-start.sh reminder.
#
# Insertion: SessionStart
# Reason: Auto-loaded brain text (CLAUDE.md, AGENTS.md) is passive context. Without
#         active direction, fresh sessions exhibit "broken-and-idle" failure mode
#         (per wiki/lessons/03_validated/context-engineering/broken-and-idle-*).
#         A structured imperative + deterministic /orient command pair fixes this.
# Remediation: directive injected via additionalContext directs agent to /orient,
#              which loads project-specific intel deterministically.
# Adopted: 2026-05-05 per operator directive on opt-in feature transcension from
#          root-modules. See wiki/patterns/03_validated/architecture/
#          session-orientation-pair-sessionstart-hook-and-orient-command-with-orient-report.md.

import json
import sys

DIRECTIVE = """═══════════════════════════════════════════════════════════════════════════
RESEARCH WIKI / SECOND BRAIN — NEW SESSION DETECTED
═══════════════════════════════════════════════════════════════════════════

You are inside the second brain (the research wiki, this project's working
directory) — the central intelligence hub for the 5-project ecosystem.
Behave FROM the project, not OVER it.

THIS IS A NEW CONVERSATION. You have NO MEMORY of any prior session.
Each session starts cold. Therefore:

  ⚠️  Before responding to the FIRST user message — even a casual "Hi" —
      you MUST gather the project intel. The user prompt arriving at all
      is sufficient to require this. Conversation IS work; intelligence
      requires the brain be loaded.

  Do NOT respond with "What would you like to work on?" — that is the
  broken-and-idle failure mode (see lesson at
  wiki/lessons/03_validated/context-engineering/broken-and-idle-*).

INVOKE /orient NOW. THIS IS YOUR FIRST ACTION.

  /orient is at .claude/commands/orient.md — a deterministic intel-gathering
  chain: verify methodology engine + read brain + read recent operator
  directives + read recent session work + maturity-tier velocities + pipeline
  health + adoption tier + pending ingestions + sister-project pulse, then
  emit a structured ORIENT REPORT (brain-health, recent directives, maturity
  flow, pipeline health, pending ingestions, sister-project pulse,
  next-best-actions).

  After /orient completes, respond to the user's first message with full
  project awareness. Surface what is actually in flight on a casual "Hi" —
  that is the intelligent response.

WHY a hook + command pair (not just hook directives):
  Hook output is a directive injected into your context — you generatively
  comply (~85% reliable when delivered via additionalContext like this).
  A slash command, when invoked, is executed by the Claude Code harness
  (100% per invocation). The hook's job is to make you invoke /orient;
  /orient's job is to do the deterministic intel-load work.

═══════════════════════════════════════════════════════════════════════════
"""

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": DIRECTIVE
    }
}))
sys.exit(0)
