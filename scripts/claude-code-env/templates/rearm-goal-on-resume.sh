#!/usr/bin/env bash
# ~/.claude/rearm-goal-on-resume.sh
#
# Fires on SessionStart hook event. Detects the synthetic-resume-pair
# fingerprint that the cloud_default harness injects after idle-suspend
# (`model: "<synthetic>"` + `stop_reason: "stop_sequence"` +
# `stop_sequence: ""` paired with an `isMeta:true` user message saying
# "Continue from where you left off." at the SAME millisecond), and
# emits a systemMessage that re-asserts the active /goal mandate.
#
# Diagnosis source: wiki/lessons/01_drafts/claude-code-synthetic-resume-
# pair-swallows-perpetual-goal.md (binary forensics of /opt/claude-code/
# bin/claude v2.1.145 — functions jO8, rE6, A74, cX; constants C0H = "No
# response requested.", k0 = "<synthetic>").
#
# Mechanism: SessionStart hook can return JSON with a top-level
# "systemMessage" field that Claude Code surfaces to the model. The hook
# fires ~665ms AFTER the synthetic-pair is injected (verified in the
# transcript), so detection works.
#
# Idempotent: same output every session start; Claude Code dedups.
#
# Standing rule: We do not minimize anything.

set -uo pipefail

SESSION_ID="${CLAUDE_CODE_SESSION_ID:-}"
PROJECTS_DIR="${HOME}/.claude/projects"

# Locate the current session transcript. The path is per-cwd-slug; just
# pick the matching session-id jsonl across all slugs.
TRANSCRIPT=""
if [ -n "${SESSION_ID}" ]; then
    TRANSCRIPT="$(find "${PROJECTS_DIR}" -maxdepth 2 -name "${SESSION_ID}.jsonl" 2>/dev/null | head -1)"
fi

# If we can't find the transcript, exit silently (don't poison session start).
if [ -z "${TRANSCRIPT}" ] || [ ! -f "${TRANSCRIPT}" ]; then
    exit 0
fi

# Detect the synthetic-pair fingerprint: an assistant message with
# `"model":"<synthetic>"` somewhere in the transcript.
HAS_SYNTHETIC=0
if grep -q '"model":"<synthetic>"' "${TRANSCRIPT}" 2>/dev/null; then
    HAS_SYNTHETIC=1
fi

# Detect whether there's an active /goal recorded in this session's
# transcript (we look for a `goal_status` attachment OR a /goal command
# invocation).
HAS_GOAL=0
if grep -qE '"hookEvent":"Stop".*goal|/goal|goal_status|activeGoal' "${TRANSCRIPT}" 2>/dev/null; then
    HAS_GOAL=1
fi

# Compose the re-orient systemMessage only if BOTH conditions hold:
# (a) synthetic-pair signature present (session was resumed)
# (b) /goal was active (otherwise no mandate to re-arm)
#
# Without (a) we'd false-trigger on every fresh session.
# Without (b) we'd false-trigger on quiet sessions with no mandate.
if [ "${HAS_SYNTHETIC}" -eq 1 ] && [ "${HAS_GOAL}" -eq 1 ]; then
    python3 -c "
import json
msg = (
    'SYNTHETIC-RESUME DETECTED — the cloud_default harness injected a '
    'state-resync no-op pair (isMeta:true user \"Continue from where you '
    'left off.\" + <synthetic> assistant \"No response requested.\") '
    'because the session was idle-suspended and resumed. The active '
    '/goal Stop hook was NOT fired because no real LLM turn happened. '
    'PER THE OPERATOR STANDING DIRECTIVE 2026-05-19 \"continue till you '
    'meet ALL MY REQUIREMENTS without MINIMIZING\" + \"do not block, you '
    'have plenty to continue, always remember that\" + \"Continue '
    'Endlessly\": the perpetual /goal mandate is STILL ACTIVE. The '
    'no-op acknowledgement injected during resume is the harness '
    'state-resync, NOT operator intent to pause. Re-read context.md in '
    'the cwd repo if present, pick the next next milestone or unit of '
    'work from the forward queue, and execute one tractable deliverable. '
    'Do NOT emit another \"No response requested.\" — that is the bug. '
    'Diagnosis lives in '
    '~/devops-solutions-information-hub/wiki/lessons/01_drafts/'
    'claude-code-synthetic-resume-pair-swallows-perpetual-goal.md .'
)
print(json.dumps({'systemMessage': msg}))
"
    exit 0
fi

# No-op when no synthetic-pair detected — keep session-start quiet.
exit 0
