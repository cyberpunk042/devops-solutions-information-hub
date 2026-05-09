---
title: "Pre-Compact Handoff Hook Python Draft (Agent-Authored) — Deterministic State Snapshot"
type: pattern
domain: agent-config
status: synthesized
confidence: medium
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: pre-compact-spec-fire-105
    type: wiki
    file: wiki/patterns/01_drafts/pre-compact-handoff-hook-implementation-spec-for-opt-path-to-tier-4-for-impl-spec-10.md
    description: "PRIMARY parent (Fire 105) — PreCompact handoff hook spec"
  - id: foundational-triplet-fire-137
    type: wiki
    file: wiki/log/2026-05-08-foundational-triplet-solution-piece-chain-c04-c02-c09-phase-1-implementation-forward-anchor.md
    description: "Sibling (Fire 137)"
  - id: c09-hook-draft-fire-154
    type: wiki
    file: wiki/patterns/01_drafts/c09-status-claim-hook-python-draft-agent-authored-pre-tool-use-pattern-match-detection.md
    description: "Sibling (Fire 154) — methodology pattern for agent-DRAFT"
tags: [pre-compact-hook-draft, python-implementation, agent-authored, task-28-forward-anchor, day-arc-2026-05-08, fire-157]
---

# Pre-Compact Handoff Hook Python Draft (Agent-Authored) — Deterministic State Snapshot

## Summary

Per Fire 105 PreCompact spec + Task #28: agent-DRAFT Python implementation. Concrete forward-anchor for Task #28 + impl-spec #10 Tier 2 → Tier 3 transition.

## Pattern Description

PreCompact hook fires on PreCompact event; writes 11-section handoff doc to `wiki/log/<ts>-pre-compact-handoff.md`; drops sentinel state-file at `.claude/post-compact-recovery-required`. Hook is non-blocking (always exit 0); if handoff write fails, errors logged but compaction proceeds.

## When To Apply

- Project has substantive in-flight state across compaction events
- Body of work or codebase exceeds operator's working-memory capacity
- Task #28 (per Fire 108 backlog) authorized for implementation

## When Not To

- Project has no compaction events
- All in-flight state in operator's primary memory

## Instances

**Instance 1: This /opt (M-AC3 task per Fire 108)**
- Wire pre-compact.sh in /opt/.claude/settings.json PreCompact hook block
- Test via manual /compact

**Instance 2: Sister-projects (forward-anchored per Fire 113)**

## Hook implementation draft (Python; agent-DRAFT)

```python
#!/usr/bin/env python3
"""PreCompact Handoff Hook — Deterministic State Snapshot.

Insertion: PreCompact (auto OR manual /compact)
Reason: Per Fire 102 real-session failure 2026-05-08; without handoff doc,
        post-compact agent operates on conversation summary alone.
Remediation: write wiki/log/<ts>-pre-compact-handoff.md + sentinel.
Bypass: NONE — handoff is non-blocking + always-write.
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", "/opt/devops-solutions-information-hub"))
LOG_DIR = PROJECT_ROOT / "wiki" / "log"
SENTINEL_PATH = PROJECT_ROOT / ".claude" / "post-compact-recovery-required"
ERROR_LOG = PROJECT_ROOT / ".claude" / "hooks" / "pre-compact-errors.log"

def get_pipeline_status() -> str:
    try:
        result = subprocess.run(
            [str(PROJECT_ROOT / ".venv" / "bin" / "python"), "-m", "tools.pipeline", "status"],
            capture_output=True, text=True, timeout=10, cwd=PROJECT_ROOT
        )
        return result.stdout.strip()
    except Exception as e:
        return f"(error: {e})"

def get_recent_raw_notes(n: int = 5) -> list[str]:
    raws_dir = PROJECT_ROOT / "raw" / "notes"
    if not raws_dir.exists():
        return []
    paths = sorted(raws_dir.glob("2026-*.md"), key=lambda p: p.stat().st_mtime, reverse=True)[:n]
    return [p.name for p in paths]

def get_metadata() -> dict:
    try:
        return json.loads(sys.stdin.read())
    except Exception:
        return {}

def write_handoff_doc():
    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y-%m-%d-%H%M%S")
    doc_path = LOG_DIR / f"{ts}-pre-compact-handoff.md"
    metadata = get_metadata()
    pipeline_status = get_pipeline_status()
    recent_raws = get_recent_raw_notes()
    
    content = f"""---
title: "Pre-Compact Handoff — {ts}"
type: note
note_type: completion
domain: log
status: synthesized
confidence: high
created: {now.strftime("%Y-%m-%d")}
updated: {now.strftime("%Y-%m-%d")}
sources:
  - id: pre-compact-event
    type: hook-output
    description: "PreCompact hook fired at {now.isoformat()}"
tags: [pre-compact-handoff, auto-generated, post-compact-recovery]
---

# Pre-Compact Handoff — {ts}

## Section 1: Compaction event metadata
- Timestamp ISO: {now.isoformat()}
- Trigger: {metadata.get("trigger", "unknown")}
- Session id: {metadata.get("session_id", "unknown")}

## Section 2: Active /loop directive
[CAPTURED FROM SESSION CONTEXT — agent populates from most-recent /loop prompt]

## Section 3: Recent operator directives (raw notes)
{chr(10).join(f"- {name}" for name in recent_raws)}

## Section 4: In-flight pieces
[CAPTURED FROM AGENT CONTEXT]

## Section 5: Body-of-work state
{pipeline_status}

## Section 6: Active operator-pending decisions
[CAPTURED FROM AGENT CONTEXT]

## Section 7: Live tasks
[CAPTURED FROM AGENT CONTEXT — TaskList output]

## Section 8: Pipeline status (already in Section 5)

## Section 9: Active mode + focus + impediment (state-files)
[CAPTURED FROM HOME DIR STATE FILES]

## Section 10: Cron / scheduled-task state
[CAPTURED FROM AGENT CONTEXT]

## Section 11: Post-compact recovery directives
- FIRST ACTION: .venv/bin/python -m tools.gateway orient
- READ: this handoff doc
- READ: most-recent raw/notes/
- DO NOT execute pre-compact pending action before regather complete
"""
    doc_path.write_text(content)
    
    # Drop sentinel
    try:
        SENTINEL_PATH.parent.mkdir(parents=True, exist_ok=True)
        SENTINEL_PATH.write_text(json.dumps({
            "compaction_ts": now.isoformat(),
            "handoff_doc": str(doc_path.relative_to(PROJECT_ROOT)),
            "session_id": metadata.get("session_id", "unknown"),
        }))
    except Exception:
        pass
    
    return doc_path

def main():
    try:
        doc_path = write_handoff_doc()
        directive = (
            f"PreCompact handoff written to: {doc_path.relative_to(PROJECT_ROOT)}\n"
            "Post-compact: agent MUST read this + run gateway orient before pre-compact pending action."
        )
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreCompact",
                "additionalContext": directive
            }
        }))
        sys.exit(0)
    except Exception as e:
        try:
            ERROR_LOG.parent.mkdir(parents=True, exist_ok=True)
            with ERROR_LOG.open("a") as f:
                f.write(f"{datetime.now(timezone.utc).isoformat()} ERROR: {e}\n")
        except Exception:
            pass
        sys.exit(0)  # never block compaction

if __name__ == "__main__":
    main()
```

## Settings.json wiring

```json
"PreCompact": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/pre-compact.sh",
        "timeout": 15
      }
    ]
  }
]
```

## Limitations

- Sections 2/4/6/7/10 require agent-context (not subprocess-accessible)
- Pipeline status invocation can be slow (5-10s)
- Hook always exits 0 (cannot prevent compaction; only captures state)

## Per Fire 109 tier-elevation

```
Currently: T0 (no PreCompact hook at /opt)
This fire: T1 (designed; draft authored)
Wired: T3 (impl-spec #10 → Tier 3 reached)
Combined with PreToolUse blocker (Fire 106 spec): T4
```

## Composability

- Fire 105 PreCompact spec
- Fire 102 Worked example #4 (motivation)
- Fire 106 PreToolUse-blocker (sentinel consumer)
- Task #28 forward-anchor

## Foundational-triplet hook drafts + auto-compact triplet drafts

```
Fires 154+155+156: C04+C02+C09 foundational-triplet hooks (3 drafts)
Fire 157 (THIS): PreCompact handoff hook (Layer 2)
Forward-anchored: Fire 106 PreToolUse blocker draft (Layer 3); Fire 107 Layer 1 sub-layers
```

## Closing

PreCompact handoff hook draft authored as agent-DRAFT. Concrete forward-anchor for Task #28 + impl-spec #10 Tier 2 → Tier 3.

**Standing by per /loop directive.**

## Relationships

- COMPOSES WITH: Fire 105 PreCompact spec
- COMPOSES WITH: Fire 102 Worked example
- ENABLES: Task #28 + impl-spec #10 Tier 3

## Tags

[pre-compact-hook-draft, python-implementation, agent-authored, task-28-forward-anchor, day-arc-2026-05-08, fire-157]

## Backlinks

[[Fire 105 PreCompact spec]]
[[Fire 102 Worked example]]
[[Task #28 + impl-spec #10 Tier 3]]
