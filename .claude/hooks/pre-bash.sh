#!/usr/bin/env bash
# PreToolUse hook on Bash — output hygiene: blocks reflexive truncation.
# Exit 0 = allow, exit 2 = block.
#
# Insertion: PreToolUse, matcher=Bash
# Reason: Internal-tool output (gateway, view, pipeline, lint, validate) is curated;
#         defaulting to | head/tail with N<100 silently loses critical information.
#         CLAUDE.md Hard Rule 1, .claude/rules/work-mode.md.
# Remediation: run without truncation; or state REASON=<why> before the command.
# Bypass: REASON env var with non-empty value bypasses; OR head/tail N >= 100 (substantial).
#
# Pattern borrowed from ~/openarms/scripts/methodology/hooks/pre-bash.sh.

set -euo pipefail

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    print(d.get('tool_input', {}).get('command', ''))
except Exception:
    print('')
" 2>/dev/null || echo "")

if [ -z "$COMMAND" ]; then
  exit 0
fi

# Bypass: legitimate truncation can set REASON env var
if [ -n "${REASON:-}" ]; then
  exit 0
fi

FIRST_LINE=$(echo "$COMMAND" | sed -n '1p')

# Only check for piped head/tail (space before pipe = shell piping, not flag arg)
if echo "$FIRST_LINE" | grep -qP '\s\|\s*(head|tail)\s'; then
  # Extract the N argument — handles `head 200`, `head -200`, `head -n 200` forms
  NUM=$(echo "$FIRST_LINE" | grep -oP '\|\s*(head|tail)\b[^0-9]*\K\d+' || echo "")

  # If N >= 100, allow — reading substantial content is legitimate
  if [ -n "$NUM" ] && [ "$NUM" -ge 100 ] 2>/dev/null; then
    exit 0
  fi

  cat <<EOF >&2
═══════════════════════════════════════════════════════════════════════════
BLOCKED: reflexive truncation pipe
═══════════════════════════════════════════════════════════════════════════

Command: $FIRST_LINE

REASON:
  Internal tools (gateway, view, pipeline post, lint, validate, stats) produce
  curated output meant to be read in full. Defaulting to | head / | tail with
  N<100 silently loses critical information.

  Rule: CLAUDE.md Hard Rule 1 + .claude/rules/work-mode.md (Output Discipline).

REMEDIATION:
  Run the command without the truncation pipe and read the full output.

  If you genuinely need only head/tail, use N >= 100 (reading substantial
  content is legitimate; reflexive small N is the illness).

BYPASS (if you have a stated reason):
  REASON="<why>" <your-bash-command>

  Example:
    REASON="checking last 5 commits only" git log --oneline | head -5
═══════════════════════════════════════════════════════════════════════════
EOF
  exit 2
fi

# No truncation pipe detected — allow
exit 0
