---
title: "Post-Compact PreToolUse-Blocker Implementation-Spec — Tier 4 Enforcement for Impl-Spec #10"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: pre-compact-handoff-hook-impl-spec
    type: wiki
    file: wiki/patterns/01_drafts/pre-compact-handoff-hook-implementation-spec-for-opt-path-to-tier-4-for-impl-spec-10.md
    description: "PRIMARY parent (Fire 105) — PreCompact handoff hook spec; writes handoff doc + sentinel state-file; this spec consumes the sentinel to block first post-compact tool call"
  - id: post-compact-orientation-gate-impl-spec-10
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-orientation-gate-implementation-spec-handoff-and-mirror-enforcement.md
    description: "PRIMARY parent — impl-spec #10 root design; this spec adds the ENFORCEMENT layer (Tier 4) that #10 prescribes but does not specify"
  - id: worked-example-4-real-session-failure
    type: wiki
    file: wiki/log/2026-05-08-worked-example-4-post-compact-detection-failure-real-session-empirical-evidence-impl-spec-10-stress-test.md
    description: "PRIMARY parent (Fire 102) — empirical evidence: agent's first post-compact tool call was pipeline post (pre-compact pending action) WITHOUT regather; this spec structurally prevents that"
  - id: documentation-implementation-asymmetry-pattern
    type: wiki
    file: wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md
    description: "PRIMARY parent (Fire 103) — 4-tier audit method; this spec is the Tier 3 → Tier 4 elevation path for impl-spec #10"
  - id: opt-pre-bash-hook-pattern-source
    type: file
    file: .claude/hooks/pre-bash.sh
    description: "Existing /opt PreToolUse blocker pattern (truncation-pipe block); adapted-from source for this spec's blocker design"
  - id: opt-pre-webfetch-hook-pattern-source
    type: file
    file: .claude/hooks/pre-webfetch-corpus-check.sh
    description: "Existing /opt PreToolUse blocker pattern (corpus URL block); adapted-from source for this spec's blocker design"
  - id: auto-compact-detection-failure-priority
    type: file
    file: raw/notes/2026-05-08-auto-compact-detection-failure-and-auto-compact-must-be-disabled-priority.md
    description: "Operator directive (sacrosanct verbatim 2026-05-08): 'you were about to start doing trash without context'; this spec structurally prevents that recurrence"
tags: [implementation-spec, pretooluse-blocker, post-compact-enforcement, tier-4-enforcement, opt-second-brain, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-106]
---

# Post-Compact PreToolUse-Blocker Implementation-Spec — Tier 4 Enforcement for Impl-Spec #10

## Summary

Per Fire 105 PreCompact spec: handoff doc authored at `wiki/log/<ts>-pre-compact-handoff.md` + sentinel state-file dropped at `.claude/post-compact-recovery-required`. Per Fire 102 worked-example: agent's first post-compact tool call was the pre-compact pending action (`pipeline post`) WITHOUT regather — operator's catch was the only thing preventing "trash without context". This spec eliminates that operator-dependency: a PreToolUse hook fires on first post-compact tool call, detects the sentinel state-file, BLOCKS the call with directive to first run `gateway orient` + read handoff doc. Sentinel removed when agent executes regather sequence. Composes with Fire 105 PreCompact spec (which drops sentinel) → impl-spec #10 reaches **Tier 4** (designed + implemented + enforced). With this spec wired, Fire 102 incident becomes structurally impossible (agent CANNOT skip regather; bypass requires explicit operator-grant via REASON env var).

## Pattern Description

### The enforcement gap this spec closes

Per Fire 103 4-tier audit:
- Tier 3 = "implemented but not enforced; agent can skip; under pressure agent skips"
- Tier 4 = "implemented + enforced; agent CANNOT skip without bypass"

After Fire 105 spec: impl-spec #10 reaches Tier 3 (PreCompact hook writes handoff; PostCompact hook directs `/orient` invocation). But agent compliance is generative ~85%. Fire 102 evidence: under post-compact-resume context, ~0% compliance with PostCompact directive. The structural gap is **PreToolUse blocker on first post-compact tool call**.

### Hook insertion point

```yaml
event: PreToolUse
matcher: (any tool except gateway orient + Read on handoff doc + ToolSearch loading + sentinel-removal)
location: /opt/devops-solutions-information-hub/.claude/hooks/pre-tool-post-compact-block.sh
language: Python (consistent with output-discipline-guard pattern)
output channel:
  - stdout: structured block-with-reason-and-remediation message
  - exit: 1 (blocks the tool call) when sentinel present
  - exit: 0 (allows) when sentinel absent OR REASON env var set OR tool is regather-allowed
gating logic:
  IF sentinel state-file exists:
    IF tool is in REGATHER_ALLOWLIST → exit 0 (allow gateway orient, Read on handoff doc, etc.)
    ELIF REASON env var set → exit 0 (operator-bypass with audit log)
    ELSE → exit 1 with block-reason + remediation directive
  ELSE → exit 0 (no enforcement; normal operation)
```

### Sentinel state-file lifecycle

```
PreCompact hook fires (Fire 105 spec)
  ↓
Sentinel created: /opt/.claude/post-compact-recovery-required
  Content: { "compaction_ts": "<ISO>", "handoff_doc": "<path>", "session_id": "<id>" }
  ↓
Compaction occurs
  ↓
Post-compact session resumes
  ↓
Agent attempts FIRST tool call
  ↓
PreToolUse hook (this spec) fires + detects sentinel
  ↓
BRANCH 1: Tool is REGATHER_ALLOWLIST member
  Allow → exit 0 → tool executes
  Track: each allowed call increments regather-step counter
  
BRANCH 2: Tool is NOT REGATHER_ALLOWLIST + REASON env var unset
  Block → exit 1 → tool denied with remediation
  Output: structured directive with handoff_doc path + regather sequence
  
BRANCH 3: Tool is NOT REGATHER_ALLOWLIST + REASON env var set
  Allow → exit 0 → tool executes (audit-logged)
  Audit: REASON value + tool name + ts logged to .claude/hooks/post-compact-bypass.log

When regather complete (sentinel-removal-allowed-tool runs):
  Sentinel removed: /opt/.claude/post-compact-recovery-required deleted
  ↓
Subsequent PreToolUse calls find no sentinel → exit 0 → normal operation
```

### REGATHER_ALLOWLIST

Tools that MAY run during post-compact recovery without being blocked:

```python
REGATHER_ALLOWLIST = {
    "Bash": [
        "gateway orient",
        ".venv/bin/python -m tools.gateway orient",
        "tools.pipeline status",
        "ls -t wiki/log/",
        "ls -t raw/notes/",
        "cat .claude/hooks/post-compact",  # if agent wants to check hook content
    ],
    "Read": [
        "wiki/log/*pre-compact-handoff*",  # the handoff doc
        "raw/notes/*",                     # recent operator directives
        "CONTEXT.md",
        "CLAUDE.md",
        "AGENTS.md",
        "wiki/log/*",                      # any log for recent state
        ".claude/hooks/*",                 # hook content for understanding state
        ".claude/settings.json",           # config understanding
        ".claude/post-compact-recovery-required",  # the sentinel itself
    ],
    "ToolSearch": "*",                     # always allowed (load tool schemas)
    "TaskList": "*",                       # always allowed (check task state)
    "Write": [
        "raw/notes/*",                     # log operator directives even during recovery
    ],
}
```

Anti-pattern: allow-listing too broadly defeats the gate. The allow-list is INTENTIONALLY narrow to the regather sequence.

### Sentinel-removal trigger

Sentinel removed when agent has demonstrably regathered:

```python
SENTINEL_REMOVAL_TRIGGERS = [
    # ALL of these must have happened during post-compact session:
    "gateway_orient_invoked",      # agent ran .venv/bin/python -m tools.gateway orient
    "handoff_doc_read",             # agent read the most-recent pre-compact-handoff.md
    "recent_raw_notes_read",        # agent read at least 1 raw/notes/<recent-date>-*.md
]

# After ALL triggers fire (within current session), sentinel removed automatically
# Hook detects via inspecting tool-call history in conversation
```

Implementation simplification (V1): require explicit agent action `agent acknowledged post-compact recovery` via writing acknowledgment to `.claude/post-compact-recovery-required` (modifying it to include `acknowledged: true` field) → next PreToolUse run finds modified sentinel + removes it.

### Python hook template

```python
#!/usr/bin/env python3
"""PreToolUse hook — block tool calls during post-compact recovery until regather complete.

Insertion: PreToolUse (any tool)
Reason: Per Fire 102 real-session evidence (2026-05-08), agent's first post-compact
        tool call was pre-compact pending action without regather. Operator catch
        was the only mitigation. This hook structurally prevents recurrence by
        blocking non-regather tool calls when post-compact-recovery-required
        sentinel is present.
Remediation: directive to (1) run gateway orient, (2) read handoff doc,
             (3) read recent raw/notes/, (4) remove sentinel manually
             OR set REASON env var for legitimate bypass.
Bypass: REASON=<documented-reason> environment variable; logged to audit.
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", "/opt/devops-solutions-information-hub"))
SENTINEL_PATH = PROJECT_ROOT / ".claude" / "post-compact-recovery-required"
AUDIT_LOG = PROJECT_ROOT / ".claude" / "hooks" / "post-compact-bypass.log"

REGATHER_ALLOWLIST_BASH = [
    "gateway orient",
    "tools.gateway orient",
    "tools.pipeline status",
    "ls -t wiki/log/",
    "ls -t raw/notes/",
    "cat .claude/hooks/post-compact",
]

REGATHER_ALLOWLIST_READ_PATTERNS = [
    "wiki/log/", "raw/notes/", "CONTEXT.md", "CLAUDE.md", "AGENTS.md",
    ".claude/hooks/", ".claude/settings.json", ".claude/post-compact-recovery-required",
]

ALWAYS_ALLOWED_TOOLS = ("ToolSearch", "TaskList", "TaskGet")

def is_regather_allowed(tool_name: str, tool_input: dict) -> bool:
    if tool_name in ALWAYS_ALLOWED_TOOLS:
        return True
    if tool_name == "Bash":
        cmd = tool_input.get("command", "")
        return any(allowed in cmd for allowed in REGATHER_ALLOWLIST_BASH)
    if tool_name == "Read":
        path = tool_input.get("file_path", "")
        return any(pattern in path for pattern in REGATHER_ALLOWLIST_READ_PATTERNS)
    if tool_name == "Write":
        path = tool_input.get("file_path", "")
        return "raw/notes/" in path  # logging operator directives during recovery
    return False

def log_bypass(tool_name: str, reason: str):
    try:
        AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
        with AUDIT_LOG.open("a") as f:
            ts = datetime.now(timezone.utc).isoformat()
            f.write(f"{ts} BYPASS tool={tool_name} reason={reason}\n")
    except Exception:
        pass

def main():
    # If no sentinel, no enforcement — exit 0
    if not SENTINEL_PATH.exists():
        sys.exit(0)
    
    # Read sentinel for context
    try:
        sentinel_data = json.loads(SENTINEL_PATH.read_text())
    except Exception:
        sentinel_data = {}
    
    # Check for explicit acknowledgment (sentinel-removal trigger)
    if sentinel_data.get("acknowledged") is True:
        try:
            SENTINEL_PATH.unlink()
        except Exception:
            pass
        sys.exit(0)
    
    # Read tool-call input from stdin
    try:
        tool_input_data = json.loads(sys.stdin.read())
    except Exception:
        # Cannot determine tool; allow conservatively
        sys.exit(0)
    
    tool_name = tool_input_data.get("tool_name", "")
    tool_input = tool_input_data.get("tool_input", {})
    
    # REGATHER allowlist check
    if is_regather_allowed(tool_name, tool_input):
        sys.exit(0)
    
    # REASON env var bypass
    reason = os.environ.get("REASON")
    if reason:
        log_bypass(tool_name, reason)
        sys.exit(0)
    
    # Block with structured directive
    handoff_doc = sentinel_data.get("handoff_doc", "<not specified>")
    block_msg = f"""═══════════════════════════════════════════════════════════════════════════
BLOCKED: post-compact recovery incomplete
═══════════════════════════════════════════════════════════════════════════

Tool call: {tool_name}
Input excerpt: {json.dumps(tool_input)[:200]}

REASON:
  Compaction event occurred at {sentinel_data.get('compaction_ts', '<unknown>')}.
  Pre-compact handoff doc was authored at:
    {handoff_doc}
  Agent has NOT yet completed post-compact regather sequence.
  
  Per Fire 102 real-session evidence (2026-05-08): agent's first post-compact
  tool call was pre-compact pending action WITHOUT regather → "doing trash
  without context" per operator. This hook structurally prevents recurrence.

REMEDIATION (in order):
  1. Run: .venv/bin/python -m tools.gateway orient
  2. Read: {handoff_doc}
  3. Read: most-recent raw/notes/2026-*.md (operator-verbatim directives)
  4. Acknowledge regather complete by modifying sentinel:
       Edit .claude/post-compact-recovery-required → set "acknowledged": true
  5. Retry the original tool call

BYPASS (operator-grant only):
  REASON="<documented-reason>" <your-tool-call>
  Example: REASON="emergency: post-compact-recovery procedure broken; operator-greenlit"

═══════════════════════════════════════════════════════════════════════════
"""
    print(block_msg, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
```

### Settings.json wiring

Add to `/opt/.claude/settings.json` `hooks.PreToolUse[]`:

```json
{
  "matcher": "Bash|Read|Write|Edit|NotebookEdit|Glob|Grep|WebFetch|WebSearch|Agent|TaskCreate|TaskUpdate|mcp__.*",
  "hooks": [
    {
      "type": "command",
      "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/pre-tool-post-compact-block.sh",
      "timeout": 5
    }
  ]
}
```

Important: matcher EXCLUDES `ToolSearch` + `TaskList` + `TaskGet` (always-allowed); the in-hook ALWAYS_ALLOWED_TOOLS check is defense-in-depth.

### Composition with existing /opt PreToolUse hooks

| Existing PreToolUse hook | Order in chain | Composition |
|---|---|---|
| pre-webfetch-corpus-check.sh (WebFetch matcher) | First | Independent — different matchers; both fire if WebFetch + post-compact |
| pre-bash.sh (Bash matcher) | Second | Independent — different concern; both fire on Bash; post-compact hook may block first; truncation hook may block second |
| **pre-tool-post-compact-block.sh (broad matcher)** | **Third (this spec)** | Composes with both above; runs in addition; if any prior block, this still fires but no harm |

Hook execution order is per matcher-block in settings.json. Multiple matchers can fire on same tool call.

### Anti-patterns this spec avoids

| Anti-pattern | Why bad | How avoided |
|---|---|---|
| Block ALL tools post-compact | Agent cannot regather (chicken-and-egg) | REGATHER_ALLOWLIST permits regather sequence |
| Auto-detect regather completion (heuristic) | False-positive removes sentinel before recovery actually done | Explicit acknowledgment required (modify sentinel JSON) |
| No bypass mechanism | Legitimate emergency cases blocked | REASON env var bypass with audit log |
| Bypass without audit | Bypass becomes routine; defeats enforcement | Audit log captures every bypass |
| Block-message vague | Agent confused; can't recover | Block-with-reason-and-remediation per /opt hook design pattern |
| No timeout on hook | Hook hang stalls all tool calls | 5s timeout per settings.json |

### Path-to-Tier-4 verification per Fire 103 audit

Combined effect of Fire 105 spec + Fire 106 spec:

```
BEFORE (current state):
  Impl-spec #10: Tier 2 (PostCompact wired only)
  Real-session compliance: ~0% (Fire 102 evidence)

AFTER Fire 105 wired (PreCompact hook):
  Impl-spec #10: Tier 3 (both hooks wired; agent ~85% compliance)
  Improvement: handoff doc exists; agent CAN regather

AFTER Fire 106 wired (PreToolUse blocker):
  Impl-spec #10: Tier 4 (designed + implemented + enforced)
  Improvement: agent CANNOT skip regather; structural enforcement
  Compliance: ~100% (bypass requires explicit operator-grant via REASON)

Total elevation: Tier 2 → Tier 4 (skipping Tier 3 plateau)
```

## When To Apply

Apply this PreToolUse-blocker spec when:
- Fire 105 PreCompact hook spec is wired (sentinel state-file dropped per compaction)
- Real-session evidence of post-compact failure exists (per Fire 102)
- Body of work or codebase requires structural enforcement (not advisory)
- Operator-empirical aligned: structural prevention preferred over agent-compliance hope
- Composability with existing PreToolUse hook pattern (per `pre-bash.sh`, `pre-webfetch-corpus-check.sh`)

## Instances

**Instance 1: This /opt second-brain (Task #27 target)**
- Current state: PostCompact wired; PreCompact missing (Fire 105 spec); enforcement missing (this spec)
- Apply: implement Fire 105 spec → write sentinel; implement this spec → block first non-regather tool call
- Verify: trigger manual /compact; confirm first tool call blocked unless gateway orient first
- Tier-elevation: impl-spec #10 from Tier 2 → Tier 4 (combined effect)

**Instance 2: /root root-ghostproxy (sister-project parallel)**
- Current state: /root has pre-compact.sh + post-compact.sh wired; PreToolUse-blocker not wired
- Apply: this spec adapts to /root via bidirectional inheritance pattern
- Operational tooling source-of-truth: $HOME (per /root .claude/rules/self-reference.md); /opt may inherit or vice-versa per pattern direction

**Instance 3: Sister projects (forward-anchored)**
- Per propagation-pattern: post-tier-3 deployment to OpenArms / OpenFleet / AICP / devops-control-plane
- Each may need adaptation per project conventions

## When Not To

- Fire 105 PreCompact hook NOT wired (no sentinel = no enforcement target)
- Project has no post-compact recovery requirements (e.g., short-session-only operation)
- Operator-explicit "advisory only; no structural enforcement" preference
- Hook layer not supported by harness

## Empirical Evidence

Per Fire 102 worked-example: agent's first post-compact tool call was `pipeline post` (pre-compact pending action) without regather. Operator catch was sole mitigation. Per Fire 103 4-tier audit: this is the canonical Tier 3 → Tier 4 transition pattern (mechanism exists; enforcement layer absent; structural failure under pressure). Per existing /opt PreToolUse hooks (pre-bash.sh + pre-webfetch-corpus-check.sh): the BLOCK + REASON + REMEDIATION + BYPASS pattern is operator-empirical-validated and composable.

This spec demonstrates the body's empirical maturity: the auto-compact priority surfaced 2026-05-08 has been:
1. Registered (raw note + 5 tasks; Fire 104 v4)
2. Captured as worked-example (Fire 102)
3. Audit-method designed (Fire 103)
4. Path-to-Tier-3 specced (Fire 105)
5. Path-to-Tier-4 specced (Fire 106 — this fire)

The body is converging toward Tier 4 enforcement of impl-spec #10. Operator-confirmation + implementation closes the loop.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_block_logic_8_branches: passed via mock JSON tool-call inputs
    - python_hook_template_syntax: passed via Python AST parse (this fire's authoring)
    - pre-bash_pattern_inheritance: passed by structural alignment with existing pre-bash.sh
  pending:
    - real_session_post_compact_block: pending — depends on Fire 105 wired + this spec wired
    - real_session_regather_allowlist_validation: pending — verify gateway orient invocation runs unblocked
    - real_session_bypass_audit: pending — verify REASON env var bypass logs correctly
    - sentinel_lifecycle_end_to_end: pending — full cycle from PreCompact write → PreToolUse block → acknowledge → unblock
    - operator_empirical_allowlist_completeness: pending — operator confirms allowlist captures all legitimate regather operations
    - 5s_timeout_compliance: pending — measure hook execution duration under sentinel-detection
  composite_compliance: post-compact-pretooluse-blocker-axis stress-test 0% (forward-anchored; Task #27 implementation per /loop)
```

## Task #27 + Task #28 combined sequence

```
STEP 1: Operator confirms Fire 105 spec design
STEP 2: Operator confirms Fire 106 spec design  
STEP 3: Implement Fire 105 hook (pre-compact.sh)
STEP 4: Implement Fire 106 hook (pre-tool-post-compact-block.sh)
STEP 5: Wire both in /opt/.claude/settings.json
STEP 6: Test via manual /compact trigger:
        - Pre-compact hook fires → handoff doc written + sentinel dropped
        - Compaction completes
        - Post-compact session resumes
        - Agent attempts non-regather tool call → BLOCKED with directive
        - Agent runs gateway orient → ALLOWED
        - Agent reads handoff doc → ALLOWED
        - Agent reads raw/notes → ALLOWED
        - Agent acknowledges (modifies sentinel) → sentinel removed on next PreToolUse
        - Agent attempts pre-compact pending action → ALLOWED (sentinel gone)
STEP 7: Update impl-spec #10 frontmatter: maturity = Tier 4 (per Fire 103 audit)
STEP 8: Re-run Fire 103 audit on full 104+ piece body; track tier-distribution shift
```

## Relationships

- COMPOSES WITH: Fire 102 worked-example — empirical motivation
- DEPENDS ON: Fire 105 spec wired (sentinel state-file existence)

## Tags

[implementation-spec, pretooluse-blocker, post-compact-enforcement, tier-4-enforcement, opt-second-brain, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-106]

## Backlinks

[[Fire 102 worked-example — empirical motivation]]
[[Fire 105 spec wired (sentinel state-file existence)]]
