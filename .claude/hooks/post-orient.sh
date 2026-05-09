#!/usr/bin/env python3
# PostCompact hook (second of two on this event) — direct the agent to re-invoke
# /orient after compaction to restore behavioral state.
#
# Insertion: PostCompact
# Reason: Compaction loses behavioral corrections, sacrosanct directives, Hard Rules,
#         and current project intel. The plain-text post-compact.sh re-prints rules;
#         this companion directs the agent to re-load fresh state via /orient.
# Output channel: systemMessage. PostCompact does NOT accept
#         hookSpecificOutput.additionalContext (only SessionStart / UserPromptSubmit /
#         PreToolUse / PostToolUse / PostToolBatch / SubagentStart accept that).
#         See: wiki/lessons/01_drafts/claude-code-hook-additionalcontext-is-event-specific-not-all-events-accept-it.md
# Remediation: agent re-invokes /orient → re-reads brain, recent directives,
#              maturity flow, pipeline health, sister-project pulse → emits fresh
#              ORIENT REPORT.

import json
import sys

DIRECTIVE = """═══════════════════════════════════════════════════════════════════════════
POST-COMPACTION — RE-ORIENT THE SECOND BRAIN
═══════════════════════════════════════════════════════════════════════════

Compaction just occurred. Behavioral state is degraded:
  • Sacrosanct operator directives are lost
  • Recent session work is lost
  • Current methodology / maturity / ingestion state is lost
  • Hard Rules (output discipline, no-fabrication, sacrosanct verbatim) need
    re-internalization

The plain-text post-compact.sh has already printed Hard Rules + sacrosanct
directives. THIS hook directs you to RE-LOAD fresh project state.

INVOKE /orient NOW (re-orientation, not first-orientation).

  /orient at .claude/commands/orient.md will:
  • Re-verify methodology engine health
  • Re-read recent operator directives (raw/notes/ last 5-7 entries)
  • Re-read recent session work (wiki/log/ last 3 entries)
  • Re-survey maturity-tier flow + pipeline health + pending ingestions
  • Emit a fresh ORIENT REPORT

This is the mirror of the SessionStart orient pattern. Compaction = reset
event; same recovery mechanism.

═══════════════════════════════════════════════════════════════════════════
"""

print(json.dumps({
    "systemMessage": DIRECTIVE
}))
sys.exit(0)
