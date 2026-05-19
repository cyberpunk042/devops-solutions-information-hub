---
title: "C04 Input-Discipline Hook Python Draft (Agent-Authored) — State-File Sentinel Pattern"
type: pattern
domain: agent-config
status: synthesized
confidence: medium
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c04-per-instance-evidence-fire-93
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c04-input-discipline-15-instances-verbatim-mapped.md
    description: "PRIMARY parent (Fire 93) — C04 baseline"
  - id: foundational-cluster-prioritization-fire-119
    type: wiki
    file: wiki/patterns/01_drafts/foundational-cluster-prioritized-enforcement-layer-pattern-c04-c02-coverage-maximizes-cross-cutting-prevention.md
    description: "PRIMARY parent (Fire 119) — C04 enforcement-layer spec"
  - id: foundational-triplet-fire-137
    type: wiki
    file: wiki/log/2026-05-08-foundational-triplet-solution-piece-chain-c04-c02-c09-phase-1-implementation-forward-anchor.md
    description: "PRIMARY parent (Fire 137) — Phase 1 forward-anchor"
  - id: c09-hook-draft-fire-154
    type: wiki
    file: wiki/patterns/01_drafts/c09-status-claim-hook-python-draft-agent-authored-pre-tool-use-pattern-match-detection.md
    description: "Sibling (Fire 154) — C09 hook draft pattern"
tags: [c04-hook-draft, python-implementation, agent-authored, state-file-sentinel, day-arc-2026-05-08, fire-155]
---

# C04 Input-Discipline Hook Python Draft (Agent-Authored) — State-File Sentinel Pattern

## Summary

Per Fire 93 + Fire 119 + Fire 137: C04 input-discipline enforcement-layer per Phase 1 spec. Per Fire 154 C09 hook pattern: agent-DRAFT Python implementation methodology. This Fire 155 authors C04 hook draft using state-file sentinel approach.

## Pattern Description

C04 hook detects when agent attempts non-read tool action without prerequisite-input load (gateway orient + brain pieces). Mechanism: state-file sentinel `~/.claude/c04-input-loaded` set when agent invokes gateway orient + reads required brain. Sentinel cleared per-cycle. PreToolUse hook checks sentinel; blocks if absent + REASON unset.

## When To Apply

- Phase 1 enforcement-layer authorization
- C04 input-discipline cluster identified as foundational (per Fire 119)
- State-file infrastructure feasible

## When Not To

- Project doesn't have gateway orient analog
- Operator-explicit "advisory only"

## Instances

**Instance 1: This the second-brain (M-C04 task per Fire 137)**
- Wire as PreToolUse for non-read tools
- State-file path: `~/.claude/c04-input-loaded`
- Set on: gateway orient + brain pieces read
- Cleared: per-cycle (cycle start)

**Instance 2: Sister-projects (forward-anchored per Fire 113)**

## Hook implementation draft (Python; agent-DRAFT)

```python
#!/usr/bin/env python3
"""C04 Input-Discipline Verification Hook — State-File Sentinel Pattern.

Insertion: PreToolUse on Write/Edit/Bash (non-read tools)
Reason: Per C04 cluster (15 instances per Fire 93); agent skipping prerequisite-input
        causes cross-cutting failures (per Fire 115 C04 in 80% of C18 instances).
Mechanism: state-file sentinel set when input-load completed; checked per tool call.
Bypass: REASON env var; audit-logged.
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", "$HOME/devops-solutions-information-hub"))
SENTINEL_PATH = Path.home() / ".claude" / "c04-input-loaded"
AUDIT_LOG = PROJECT_ROOT / ".claude" / "hooks" / "c04-bypass.log"

# Tools allowed without input-load sentinel
INPUT_LOAD_ALLOWED_TOOLS = (
    "Read",          # reading is part of input-load
    "Grep",          # searching is part of input-load
    "Glob",          # listing is part of input-load
    "TaskList",      # task tracker check is preliminary
    "TaskGet",
    "ToolSearch",
)

# Bash commands allowed without input-load sentinel
INPUT_LOAD_ALLOWED_BASH = [
    "gateway orient",
    "tools.gateway orient",
    "tools.pipeline status",
    "ls",
    "cat",                    # for input-loading
    "grep",                   # for input-loading
]

def is_input_load_action(tool_name: str, tool_input: dict) -> bool:
    """Check if tool call is itself an input-load action."""
    if tool_name in INPUT_LOAD_ALLOWED_TOOLS:
        return True
    if tool_name == "Bash":
        cmd = tool_input.get("command", "")
        return any(allowed in cmd for allowed in INPUT_LOAD_ALLOWED_BASH)
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
    try:
        tool_input_data = json.loads(sys.stdin.read())
    except Exception:
        sys.exit(0)
    
    tool_name = tool_input_data.get("tool_name", "")
    tool_input = tool_input_data.get("tool_input", {})
    
    # If sentinel exists, allow
    if SENTINEL_PATH.exists():
        sys.exit(0)
    
    # If tool is itself input-load, allow + suggest setting sentinel
    if is_input_load_action(tool_name, tool_input):
        sys.exit(0)
    
    # Check REASON bypass
    reason = os.environ.get("REASON")
    if reason:
        log_bypass(tool_name, reason)
        sys.exit(0)
    
    # Block
    block_msg = f"""═══════════════════════════════════════════════════════════════════════════
BLOCKED: input-discipline violation (C04)
═══════════════════════════════════════════════════════════════════════════

Tool call: {tool_name}
Input-load sentinel NOT SET at: {SENTINEL_PATH}

REASON:
  Per C04 cluster (15 instances Fire 93; 80% in cross-cutting per Fire 115):
  agent skipping prerequisite-input causes cross-cutting failures.

REMEDIATION:
  1. Run: .venv/bin/python -m tools.gateway orient
  2. Read required brain pieces (CONTEXT.md, recent raws, etc.)
  3. Set sentinel: touch {SENTINEL_PATH}
  4. Retry tool call

BYPASS:
  REASON="<documented-reason>" <your-tool-call>
  Or: skip if input-load not applicable (e.g., minor edit)
═══════════════════════════════════════════════════════════════════════════
"""
    print(block_msg, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
```

## Settings.json wiring proposal

```json
"PreToolUse": [
  {
    "matcher": "Write|Edit|Bash|NotebookEdit",
    "hooks": [
      {
        "type": "command",
        "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/c04-input-discipline-check.sh",
        "timeout": 5
      }
    ]
  }
]
```

## Limitations

- Sentinel cleanup discipline (per-cycle reset) requires separate hook OR cron
- False-positive: minor edits don't truly need full input-load
- False-negative: sentinel set but agent didn't actually read

## Per Fire 109 tier-elevation: T0 → T1 → T3 → T4

```
Currently: T0 (no enforcement)
This fire: T1 (designed)
Wired: T3 (full impl, ~85% compliance)
Bypass-monitoring: T4
```

## Composability

- Fire 93 C04 evidence (foundation)
- Fire 119 foundational-cluster prioritization
- Fire 137 Phase 1 forward-anchor
- Fire 154 C09 hook (sibling)
- Pre-bash + Pre-webfetch existing PreToolUse hooks

## Closing

C04 input-discipline hook draft authored. Sentinel-based mechanism vs Fire 154 C09's pattern-match — different approaches per cluster. Combined Phase 1: 3 hook drafts (C04 sentinel + C02 pattern-match + C09 pattern-match).

**Standing by per /loop directive. C04 hook draft surfaced.**

## Relationships

- COMPOSES WITH: Fire 93 + Fire 119 + Fire 137 (C04 lineage)
- COMPOSES WITH: Fire 154 C09 hook draft (Phase 1 sibling)
- ENABLES: M-C04 task completion per Fire 137

## Tags

[c04-hook-draft, python-implementation, agent-authored, state-file-sentinel, day-arc-2026-05-08, fire-155]

## Backlinks

[[Fire 93 + Fire 119 + Fire 137 (C04 lineage)]]
[[Fire 154 C09 hook draft (Phase 1 sibling)]]
[[M-C04 task completion per Fire 137]]
