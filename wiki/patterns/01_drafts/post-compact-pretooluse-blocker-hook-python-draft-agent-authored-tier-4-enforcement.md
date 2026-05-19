---
title: "Post-Compact PreToolUse-Blocker Hook Python Draft (Agent-Authored) — Tier 4 Enforcement"
type: pattern
domain: agent-config
status: synthesized
confidence: medium
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: post-compact-pretooluse-blocker-spec-fire-106
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-pretooluse-blocker-implementation-spec-tier-4-enforcement-for-impl-spec-10.md
    description: "PRIMARY parent (Fire 106) — PreToolUse-blocker spec"
  - id: pre-compact-handoff-hook-draft-fire-157
    type: wiki
    file: wiki/patterns/01_drafts/pre-compact-handoff-hook-python-draft-agent-authored-deterministic-state-snapshot.md
    description: "Sibling (Fire 157) — PreCompact handoff hook draft (sentinel producer)"
tags: [post-compact-pretooluse-blocker-hook-draft, python-implementation, agent-authored, tier-4-enforcement, day-arc-2026-05-08, fire-158]
---

# Post-Compact PreToolUse-Blocker Hook Python Draft (Agent-Authored) — Tier 4 Enforcement

## Summary

Per Fire 106 PreToolUse-blocker spec + Fire 157 PreCompact handoff draft (sentinel producer): this Fire 158 authors the SENTINEL CONSUMER hook draft. Together with Fire 157, completes auto-compact triplet hook drafts. Tier 4 enforcement: agent CANNOT execute pre-compact pending tool call without first running gateway orient + reading handoff.

## Pattern Description

PreToolUse hook checks for sentinel `.claude/post-compact-recovery-required`. If present + tool is not in REGATHER_ALLOWLIST + REASON unset → BLOCK. Sentinel removed when agent acknowledges (modifies sentinel JSON adding `acknowledged: true`).

## When To Apply

- Fire 157 PreCompact handoff hook wired (sentinel producer)
- Task #27 authorized
- Real-session post-compact failure evidence exists (per Fire 102)

## When Not To

- Fire 157 not wired (no sentinel = no enforcement target)
- Operator-explicit "advisory only"

## Instances

**Instance 1: This the second-brain (M-AC3 task per Fire 108)**
**Instance 2: Sister-projects (forward-anchored)**

## Hook implementation draft (Python; agent-DRAFT)

```python
#!/usr/bin/env python3
"""Post-Compact PreToolUse-Blocker Hook — Tier 4 Enforcement.

Insertion: PreToolUse (broad matcher; excludes ToolSearch/TaskList/TaskGet)
Reason: Per Fire 102 real-session failure 2026-05-08; agent skipped regather
        post-compact. This hook structurally prevents recurrence.
Mechanism: detect sentinel state-file from Fire 157 PreCompact hook;
           block first non-regather tool call.
Bypass: REASON env var with operator-grant; audit-logged.
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", "$HOME/devops-solutions-information-hub"))
SENTINEL_PATH = PROJECT_ROOT / ".claude" / "post-compact-recovery-required"
AUDIT_LOG = PROJECT_ROOT / ".claude" / "hooks" / "post-compact-bypass.log"

REGATHER_ALLOWED_BASH = [
    "gateway orient",
    "tools.gateway orient",
    "tools.pipeline status",
    "ls",
    "cat",
    "grep",
]

REGATHER_READ_PATHS = [
    "wiki/log/",
    "raw/notes/",
    "CONTEXT.md",
    "CLAUDE.md",
    "AGENTS.md",
    ".claude/hooks/",
    ".claude/settings.json",
    ".claude/post-compact-recovery-required",
]

ALWAYS_ALLOWED = ("ToolSearch", "TaskList", "TaskGet")

def is_regather_allowed(tool_name: str, tool_input: dict) -> bool:
    if tool_name in ALWAYS_ALLOWED:
        return True
    if tool_name == "Bash":
        cmd = tool_input.get("command", "")
        return any(allowed in cmd for allowed in REGATHER_ALLOWED_BASH)
    if tool_name == "Read":
        path = tool_input.get("file_path", "")
        return any(pattern in path for pattern in REGATHER_READ_PATHS)
    if tool_name == "Write":
        path = tool_input.get("file_path", "")
        return "raw/notes/" in path
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
    if not SENTINEL_PATH.exists():
        sys.exit(0)
    
    try:
        sentinel_data = json.loads(SENTINEL_PATH.read_text())
    except Exception:
        sentinel_data = {}
    
    # Acknowledgment removes sentinel
    if sentinel_data.get("acknowledged") is True:
        try:
            SENTINEL_PATH.unlink()
        except Exception:
            pass
        sys.exit(0)
    
    try:
        tool_input_data = json.loads(sys.stdin.read())
    except Exception:
        sys.exit(0)
    
    tool_name = tool_input_data.get("tool_name", "")
    tool_input = tool_input_data.get("tool_input", {})
    
    if is_regather_allowed(tool_name, tool_input):
        sys.exit(0)
    
    reason = os.environ.get("REASON")
    if reason:
        log_bypass(tool_name, reason)
        sys.exit(0)
    
    handoff_doc = sentinel_data.get("handoff_doc", "<not specified>")
    block_msg = f"""═══════════════════════════════════════════════════════════════════════════
BLOCKED: post-compact recovery incomplete (Tier 4 enforcement)
═══════════════════════════════════════════════════════════════════════════

Tool call: {tool_name}

REASON:
  Compaction at {sentinel_data.get('compaction_ts', '<unknown>')}.
  Handoff doc: {handoff_doc}
  Agent has NOT completed regather sequence.

REMEDIATION:
  1. Run: .venv/bin/python -m tools.gateway orient
  2. Read: {handoff_doc}
  3. Read: most-recent raw/notes/2026-*.md
  4. Acknowledge: edit .claude/post-compact-recovery-required → set "acknowledged": true
  5. Retry tool call

BYPASS:
  REASON="<documented-reason>" <your-tool-call>
═══════════════════════════════════════════════════════════════════════════
"""
    print(block_msg, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
```

## Settings.json wiring

```json
"PreToolUse": [
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
]
```

## Limitations

- Acknowledgment requires explicit agent action (modify JSON)
- Sentinel-removal can be manual (delete file directly)
- Operator-bypass via REASON env var

## Per Fire 109 tier-elevation

```
Currently: T0
This fire: T1 (designed)
Wired with Fire 157: T3 (sentinel produced + consumed)
Bypass-monitoring: T4
```

## Composability

- Fire 106 PreToolUse-blocker spec
- Fire 157 PreCompact handoff hook (sentinel producer)
- Fire 102 Worked example #4 (motivation)
- Fires 154+155+156 foundational-triplet drafts (sibling agent-DRAFT methodology)

## Auto-compact triplet hook drafts COMPLETE

```
Fire 157: PreCompact handoff (Layer 2 sentinel producer)
Fire 158 (THIS): PreToolUse blocker (Layer 3 sentinel consumer) 
Fire 107 spec: Layer 1 prevention (sub-layers; not all hook-implementable)

Combined Layer 2 + Layer 3 hook drafts ready for operator-empirical wiring
```

## Closing

Auto-compact triplet hook drafts (Layer 2 + Layer 3) complete. Combined Phase 1 hook-draft set: foundational-triplet (Fires 154+155+156) + auto-compact triplet (Fires 157+158) = **5 concrete hook drafts** ready for operator-empirical implementation.

**Standing by per /loop directive.**

## Relationships

- COMPOSES WITH: Fire 106 PreToolUse-blocker spec
- COMPOSES WITH: Fire 157 PreCompact handoff (sentinel pair)
- COMPOSES WITH: Fire 102 Worked example #4
- COMPOSES WITH: Fires 154-156 foundational-triplet drafts
- DEPENDS ON: Fire 157 wired
- ENABLES: Task #27 + impl-spec #10 Tier 4

## Tags

[post-compact-pretooluse-blocker-hook-draft, python-implementation, agent-authored, tier-4-enforcement, day-arc-2026-05-08, fire-158]

## Backlinks

[[Fire 106 PreToolUse-blocker spec]]
[[Fire 157 PreCompact handoff (sentinel pair)]]
[[Fire 102 Worked example #4]]
[[Fires 154-156 foundational-triplet drafts]]
[[Fire 157 wired]]
[[Task #27 + impl-spec #10 Tier 4]]
