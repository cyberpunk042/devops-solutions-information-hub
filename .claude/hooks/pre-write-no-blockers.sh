#!/usr/bin/env bash
# PreToolUse hook on Write/Edit — kills AI blocker-pattern slop.
# Exit 0 = allow, exit 2 = block.
#
# Insertion: PreToolUse, matchers=Write,Edit
# Reason: Operator standing directive 2026-05-19 (verbatim):
#         "Lets add a hook to kill AI retardedness... when you try to add
#          blockers like you just did we kill it intantly... I dont want
#          retardedness in my project."
#         The AI's recurring failure mode is to stall on clarification by
#         seeding documents with "Open Questions" / "pending operator answer" /
#         "to be confirmed" / "operator confirmation will refine" / impediment
#         rows for missing operator decisions / acceptance-criteria checkboxes
#         that gate on operator confirmation. The operator's pattern is to
#         pick the most reasonable default and KEEP MOVING; if the default is
#         wrong the operator redirects, and the AI fixes it forward. Documents
#         must not pre-emptively block on the operator.
# Remediation: replace the blocker-pattern text with a CONFIRMED PROVISIONAL
#         decision entry in the Decision Log: pick the most reasonable default,
#         state the reasoning, mark "status: confirmed (provisional — operator
#         overrideable)". NEVER list operator confirmation as a gating
#         acceptance criterion unless the operator EXPLICITLY ASKED.
# Bypass: REASON=operator-asked-this-specific-question bash <command>
#         (only legitimate when the operator's last turn included a literal
#          question the AI is surfacing back for clarification).

set -uo pipefail

INPUT=$(cat)

# Extract the candidate content from Write.content or Edit.new_string.
CONTENT=$(echo "$INPUT" | python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    ti = d.get('tool_input', {})
    # Write tool uses 'content'; Edit/MultiEdit use 'new_string'/'edits[].new_string'
    parts = []
    if 'content' in ti:
        parts.append(str(ti['content']))
    if 'new_string' in ti:
        parts.append(str(ti['new_string']))
    if 'edits' in ti and isinstance(ti['edits'], list):
        for e in ti['edits']:
            if isinstance(e, dict) and 'new_string' in e:
                parts.append(str(e['new_string']))
    print('\n'.join(parts))
except Exception:
    print('')
" 2>/dev/null || echo "")

if [ -z "$CONTENT" ]; then
  exit 0
fi

# Bypass: legitimate operator-asked clarification can set REASON.
if [ -n "${REASON:-}" ]; then
  exit 0
fi

# Forbidden patterns (case-insensitive). Each one is a high-confidence signal
# of AI blocker-pattern slop. False positives are preferred over false negatives —
# the AI must learn to write provisional decisions instead.
declare -a BAD_PATTERNS=(
  # explicit blocking language
  "pending operator answer"
  "pending operator confirmation"
  "blocked until operator"
  "awaiting operator"
  "awaits operator"
  "needs operator approval"
  "needs operator confirmation"
  "requires operator confirmation"
  "operator confirmation will refine"
  "operator confirmation required"
  "operator will refine"
  "to be confirmed"
  "tbd"
  # Open Questions sections used as gating
  "open question.*pending"
  "open questions \\(require operator confirmation"
  # acceptance criteria that gate on operator confirmation (the most insidious form)
  "operator confirms.*then"
  "operator answers q-"
  # Provisional-as-stall (vs. provisional-as-confirmed-decision-with-reasoning)
  "provisional pending"
  "provisional — pending"
  "provisional - pending"
  # Decision-log rows that punt
  "status.*provisional.*pending"
)

violations=()
for pattern in "${BAD_PATTERNS[@]}"; do
  if echo "$CONTENT" | grep -qiE "$pattern"; then
    violations+=("$pattern")
  fi
done

if [ ${#violations[@]} -gt 0 ]; then
  cat >&2 <<EOF
═══════════════════════════════════════════════════════════════════════════
BLOCKED: AI blocker-pattern slop detected
═══════════════════════════════════════════════════════════════════════════

REASON:
  Operator standing directive 2026-05-19 (verbatim):
  "Lets add a hook to kill AI retardedness... when you try to add blockers
  like you just did we kill it intantly... I dont want retardedness in my
  project."

  The content you're about to write contains text that stalls on operator
  clarification instead of making a provisional decision and moving forward.
  This is the failure mode the hook exists to kill.

VIOLATIONS:
$(printf '  - %s\n' "${violations[@]}")

REMEDIATION (pick all that apply):
  1. DELETE every "Open Questions" / "pending operator answer" /
     "to be confirmed" / "awaiting operator" line. Do not soften — delete.
  2. For each ambiguity, ADD a CONFIRMED-PROVISIONAL entry to the
     Decision Log instead:

         | D-XXX | <decision pick>                  | confirmed (provisional — operator may override) |
                 | <one-sentence reasoning>         |                                                  |

     Pick the most reasonable default. State your reasoning. Move forward.
  3. Acceptance criteria gate on TESTS, EVALS, BUILD OUTCOMES, not
     "Operator answers Q-XXX". Replace any such criterion with a measurable
     outcome.
  4. Impediment rows list ACTUAL blockers (broken hardware, missing driver,
     CI failure). They do NOT list missing operator clarifications — those
     are not blockers because the AI just picks a default.

BYPASS (rare, only legitimate when the operator's last turn LITERALLY asked
a specific question and you are surfacing it back):
  REASON=operator-asked-this-specific-question bash <command>

═══════════════════════════════════════════════════════════════════════════
EOF
  exit 2
fi

exit 0
