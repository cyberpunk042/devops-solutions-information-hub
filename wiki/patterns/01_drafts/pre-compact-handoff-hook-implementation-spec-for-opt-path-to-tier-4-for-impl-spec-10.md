---
title: "Pre-Compact Handoff Hook Implementation-Spec for the second-brain — Path to Tier 4 for Impl-Spec #10"
type: pattern
domain: agent-config
status: synthesized
confidence: high
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: post-compact-orientation-gate-impl-spec-10
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-orientation-gate-implementation-spec-handoff-and-mirror-enforcement.md
    description: "PRIMARY parent — impl-spec #10 prescribes bidirectional design (PreCompact + PostCompact); the second-brain only has PostCompact wired; this spec closes the gap"
  - id: worked-example-4-real-session-failure
    type: wiki
    file: wiki/log/2026-05-08-worked-example-4-post-compact-detection-failure-real-session-empirical-evidence-impl-spec-10-stress-test.md
    description: "PRIMARY parent (Fire 102) — empirical evidence that PreCompact hook absence caused real-session failure; this spec is the structural fix"
  - id: documentation-implementation-asymmetry-pattern
    type: wiki
    file: wiki/patterns/01_drafts/documentation-implementation-asymmetry-pattern-4-tier-audit-distinguishes-design-from-enforcement.md
    description: "PRIMARY parent (Fire 103) — 4-tier audit method; impl-spec #10 currently at Tier 2 (PostCompact wired only); this spec moves it to Tier 3"
  - id: opt-post-compact-hook-existing
    type: file
    file: .claude/hooks/post-compact.sh
    description: "Existing companion — the second-brain PostCompact bash hook (re-prints sacrosanct directives + pointers); this spec authors the PreCompact pair"
  - id: opt-post-orient-hook-existing
    type: file
    file: .claude/hooks/post-orient.sh
    description: "Existing companion — the second-brain PostCompact Python hook (additionalContext directs /orient invocation); reads handoff doc per impl-spec #10"
  - id: auto-compact-detection-failure-priority
    type: file
    file: raw/notes/2026-05-08-auto-compact-detection-failure-and-auto-compact-must-be-disabled-priority.md
    description: "Operator directive (sacrosanct verbatim 2026-05-08): auto-compact must be off; PreCompact hook must wire; handoff doc must persist"
  - id: root-pre-compact-hook-pattern
    type: file
    file: /root/.claude/hooks/pre-compact.sh
    description: "/root sister-project pre-compact pattern — adapted-from source for the second-brain's pre-compact hook (per bidirectional inheritance rule)"
tags: [implementation-spec, pre-compact-hook, opt-second-brain, tier-elevation, path-to-tier-4, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-105]
---

# Pre-Compact Handoff Hook Implementation-Spec for the second-brain — Path to Tier 4 for Impl-Spec #10

## Summary

Per Fire 102 worked-example: real-session post-compact failure 2026-05-08 traced to the second-brain's missing PreCompact hook → no handoff doc authored → post-compact agent acted on conversation summary alone (an incomplete substitute). Per Fire 103 4-tier audit: impl-spec #10 sits at Tier 2 (partial — PostCompact wired, PreCompact NOT). Per operator directive (sacrosanct verbatim 2026-05-08, post-compact): *"we had so much to do and a hand-off document and such... we need to find how out how that can happen"* — handoff doc was an operator-expected artifact that never materialized. This spec closes the gap: deterministic Python hook authoring `wiki/log/<ts>-pre-compact-handoff.md` per PreCompact event, capturing 11 sections of state. With this hook wired, impl-spec #10 advances Tier 2 → Tier 3 (implementation complete; enforcement still per agent-compliance ~85%). Path to Tier 4: PreToolUse-blocker hook OR detection-sentinel state-file (deferred to Task #27 → separate spec).

## Pattern Description

### Hook insertion point

```yaml
event: PreCompact
matcher: (any) — fires before any compaction event (auto OR manual)
location: $HOME/devops-solutions-information-hub/.claude/hooks/pre-compact.sh
language: Python (consistent with post-orient.sh) — NOT bash (richer state-capture)
output channels:
  - stdout: brief operator-visible message ("PreCompact handoff written to <path>")
  - side-effect: writes wiki/log/<ts>-pre-compact-handoff.md
  - additionalContext (optional): directs agent's last pre-compact action
exit: 0 (always — never block compaction; handoff is for AFTER, not gate)
```

### Hook responsibilities (the 11 sections)

The handoff doc MUST capture (per impl-spec #10 + Fire 102 lessons):

```
SECTION 1: Compaction event metadata
  - timestamp (ISO 8601 + epoch)
  - trigger type (auto-threshold, manual-/compact, harness-default)
  - context-remaining percent at trigger (per Fire 102: 5% incident)
  - session id (Claude Code session id from env)

SECTION 2: Active /loop directive (sacrosanct verbatim)
  - Full text of most-recent /loop directive
  - Source (operator-typed-message vs cron-fire)
  - Cron job id if active (e.g., e19f4787)

SECTION 3: Sacrosanct verbatim refresh (last-N operator directives)
  - Top 5-7 most-recent raw/notes/<date>-*.md primary sources
  - Verbatim quote per directive (sacrosanct rule applies)

SECTION 4: In-flight pieces (pre-compact pending state)
  - Last piece authored (path + name)
  - Pipeline-post status of last piece (validated? pending?)
  - Next-fire-pick (if planned)

SECTION 5: Body-of-work state snapshot
  - Total pieces count
  - Total wiki pages count
  - Current decision-package version (e.g., v4)
  - Tier-distribution shape (per Fire 103 audit)
  - Phases active (e.g., 10+)

SECTION 6: Active operator-pending decisions
  - List of operator-pending decisions per most-recent decision-package
  - Status per decision (still-pending vs newly-decided)

SECTION 7: Live tasks (the second-brain task tracker)
  - All pending tasks with subject + status
  - All in-progress tasks
  - Recently-completed tasks (last 5)

SECTION 8: Pipeline status snapshot
  - Total pages, validation errors, lint issues
  - Last `tools.pipeline post` exit code + timestamp

SECTION 9: Active mode + active focus + active impediment (if state-files exist)
  - ~/.claude/active-mode value
  - ~/.claude/active-focus value
  - ~/.claude/active-impediment value (per Fire 101 convention)
  - Per-mode primary brain pieces loaded

SECTION 10: Cron / scheduled-task state
  - Active CronCreate jobs (id + cadence + prompt-summary)
  - Active ScheduleWakeup deadlines
  - Loop-state (continuing, paused, cleared)

SECTION 11: Post-compact recovery directives
  - Explicit "FIRST ACTION POST-COMPACT MUST BE: gateway orient + read this handoff"
  - Cross-reference to post-orient.sh hook output
  - Forward-anchored: PreToolUse-blocker hook (Tier 4 enforcement; deferred)
```

### Python hook template

```python
#!/usr/bin/env python3
"""PreCompact hook — author deterministic handoff doc to wiki/log/.

Insertion: PreCompact (auto OR manual /compact)
Reason: Compaction destroys conversation context including in-flight state,
        sacrosanct directives, and recent work. Without persistent handoff,
        post-compact agent operates on conversation summary alone — incomplete
        substitute (per Fire 102 real-session failure 2026-05-08).
Remediation: write wiki/log/<ts>-pre-compact-handoff.md capturing 11 sections;
             post-compact agent reads it as deterministic state recovery.
Bypass: NONE — handoff is non-blocking + always-write. If handoff write fails,
        log error to .claude/hooks/pre-compact-errors.log + continue.
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", "$HOME/devops-solutions-information-hub"))
LOG_DIR = PROJECT_ROOT / "wiki" / "log"
RAW_NOTES_DIR = PROJECT_ROOT / "raw" / "notes"
ACTIVE_MODE_FILE = Path.home() / ".claude" / "active-mode"
ACTIVE_FOCUS_FILE = Path.home() / ".claude" / "active-focus"
ACTIVE_IMPEDIMENT_FILE = Path.home() / ".claude" / "active-impediment"

def read_state_file(path: Path) -> str:
    try:
        return path.read_text().strip() if path.exists() else "(unset)"
    except Exception as e:
        return f"(error: {e})"

def get_recent_raw_notes(n: int = 7) -> list[Path]:
    if not RAW_NOTES_DIR.exists():
        return []
    return sorted(RAW_NOTES_DIR.glob("2026-*.md"), key=lambda p: p.stat().st_mtime, reverse=True)[:n]

def get_pipeline_status() -> str:
    try:
        result = subprocess.run(
            [str(PROJECT_ROOT / ".venv" / "bin" / "python"), "-m", "tools.pipeline", "status"],
            capture_output=True, text=True, timeout=10, cwd=PROJECT_ROOT
        )
        return result.stdout.strip()
    except Exception as e:
        return f"(error invoking pipeline status: {e})"

def get_input_metadata() -> dict:
    try:
        return json.loads(sys.stdin.read())
    except Exception:
        return {}

def write_handoff_doc() -> Path:
    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y-%m-%d-%H%M%S")
    doc_path = LOG_DIR / f"{ts}-pre-compact-handoff.md"
    
    metadata = get_input_metadata()
    recent_raws = get_recent_raw_notes()
    pipeline_status = get_pipeline_status()
    
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
    description: "PreCompact hook fired at {now.isoformat()} — deterministic state snapshot"
tags: [pre-compact-handoff, auto-generated, post-compact-recovery]
---

# Pre-Compact Handoff — {ts}

## Section 1: Compaction event metadata
- Timestamp (ISO): {now.isoformat()}
- Timestamp (epoch): {int(now.timestamp())}
- Trigger type: {metadata.get("trigger", "unknown")}
- Session id: {metadata.get("session_id", "unknown")}

## Section 2: Active /loop directive (sacrosanct verbatim)
[CAPTURED FROM SESSION CONTEXT — agent should populate from most-recent /loop prompt prior to compaction]

## Section 3: Sacrosanct verbatim refresh (last-N operator directives)
{chr(10).join(f"- {p.name}" for p in recent_raws)}

## Section 4: In-flight pieces (pre-compact pending state)
[CAPTURED FROM AGENT CONTEXT — last piece authored + pipeline-post status]

## Section 5: Body-of-work state snapshot
{pipeline_status}

## Section 6: Active operator-pending decisions
[CAPTURED FROM AGENT CONTEXT — current decision-package operator-territory items]

## Section 7: Live tasks (the second-brain task tracker)
[CAPTURED FROM AGENT CONTEXT — TaskList output]

## Section 8: Pipeline status snapshot (already in Section 5)

## Section 9: Active mode + focus + impediment
- Active mode: {read_state_file(ACTIVE_MODE_FILE)}
- Active focus: {read_state_file(ACTIVE_FOCUS_FILE)}
- Active impediment: {read_state_file(ACTIVE_IMPEDIMENT_FILE)}

## Section 10: Cron / scheduled-task state
[CAPTURED FROM AGENT CONTEXT — active CronCreate jobs + ScheduleWakeup deadlines]

## Section 11: Post-compact recovery directives
- FIRST ACTION POST-COMPACT MUST BE: `.venv/bin/python -m tools.gateway orient`
- THEN: read this handoff doc (path: {doc_path})
- THEN: read most-recent raw/notes/2026-*.md verbatim
- THEN: re-establish /loop continuation OR resume per pre-compact pending state (Section 4)
- DO NOT execute pre-compact pending tool call before completing recovery procedure
"""
    
    doc_path.write_text(content)
    return doc_path

def main():
    try:
        doc_path = write_handoff_doc()
        directive = (
            f"PreCompact handoff written to: {doc_path.relative_to(PROJECT_ROOT)}\n"
            "After compaction, post-compact agent MUST read this doc + run gateway orient "
            "before any pre-compact-pending tool call."
        )
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreCompact",
                "additionalContext": directive
            }
        }))
        sys.exit(0)
    except Exception as e:
        # Never block compaction; log + continue
        log_path = PROJECT_ROOT / ".claude" / "hooks" / "pre-compact-errors.log"
        try:
            with log_path.open("a") as f:
                f.write(f"{datetime.now(timezone.utc).isoformat()} ERROR: {e}\n")
        except Exception:
            pass
        sys.exit(0)

if __name__ == "__main__":
    main()
```

### Settings.json wiring

Add to `.claude/settings.json` `hooks` block:

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

Note: 15-second timeout (vs 10s elsewhere) to accommodate the `pipeline status` invocation.

### Limitations of this hook (operator-empirical to confirm)

| Limitation | Mitigation |
|---|---|
| Sections 2, 4, 6, 7, 10 require agent-context (not available to subprocess) | Hook stubs these with [CAPTURED FROM AGENT CONTEXT] markers; per impl-spec #10, agent's last-action-before-compact populates them |
| `pipeline status` invocation may be slow (~5-10s) | Timeout 15s; if exceeds, snapshot includes "(timed out)" stub |
| Auto-compact on harness-default may fire BEFORE PreCompact hook | Confirmed open issue per Task #25 investigation; handoff captures partial state regardless |
| Hook cannot prevent compaction (always exit 0) | By design — handoff is for AFTER not BEFORE; combine with Task #26 (auto-compact disable) for full coverage |

### Composability with the second-brain body

| Component | Composability |
|---|---|
| Impl-spec #10 (post-compact orientation gate) | This spec closes the bidirectional pair → Tier 3 |
| post-compact.sh + post-orient.sh | Already wired; this spec adds PreCompact partner; `post-orient.sh` reads handoff doc |
| 4-tier asymmetry pattern (Fire 103) | Authoring this spec moves impl-spec #10 from Tier 2 → Tier 3 (Tier 4 requires PreToolUse blocker) |
| Worked-example #4 (Fire 102) | Empirical-evidence motivation; this spec is the structural fix |
| Task #28 | Operationalizes Task #28 with concrete code template |
| Decision-package v4 (Fire 104) | Option E first-step (highest-leverage single-point fix) |
| Sister-project /root pre-compact.sh | Adapted-from source per bidirectional inheritance rule (operational tooling: $HOME source-of-truth → the second-brain inherits with adaptations for second-brain conventions) |

### Anti-patterns this spec avoids

| Anti-pattern | Why bad |
|---|---|
| Bash hook (insufficient state-capture) | Sections 5, 9 require Python subprocess + Path conventions |
| Blocking compaction (exit 1) | Operator-expectation: handoff is non-blocking; if write fails, compaction proceeds + hooks log error |
| Captured by stdout (no additionalContext) | additionalContext directs agent's last-pre-compact action; stdout alone insufficient (per Fire 102 evidence: agent missed PostCompact stdout output) |
| Single-section handoff (insufficient state) | Multi-section captures discrete state-classes; partial recovery per section possible |
| Static template (not pipeline-status integrated) | Real-time pipeline status critical (per Fire 102 incident: state was 707 pages pre-compact; agent didn't know this without invoking pipeline status post-compact) |

## When To Apply

Apply this PreCompact handoff hook spec when:
- Project has substantive in-flight state across compaction events
- Body of work or codebase exceeds operator's working-memory capacity
- Real-session post-compact failure events have occurred (per Fire 102)
- Composite-compliance metric requires post-compact recovery verification (per Fire 85)
- Sister-project bidirectional inheritance applies (/root has working pattern; the second-brain inherits)

## Instances

**Instance 1: This the second-brain second-brain (Task #28 target)**
- Current state: PostCompact wired; PreCompact missing
- Apply: author pre-compact.sh per this template; wire in settings.json
- Verify: trigger manual /compact; check wiki/log/<ts>-pre-compact-handoff.md exists with 11 sections
- Tier-elevation: impl-spec #10 from Tier 2 → Tier 3

**Instance 2: /root root-ghostproxy (existing pattern reference)**
- Current state: pre-compact.sh exists per /root .claude/hooks/
- Pattern source: this the second-brain spec is adapted-from /root pattern per bidirectional inheritance
- Cross-reference: validate the second-brain's adaptation honors /root's design while accommodating the second-brain's second-brain conventions

**Instance 3: Sister projects (forward-anchored)**
- OpenArms / OpenFleet / AICP / devops-control-plane
- Each may need its own PreCompact hook adapted per project conventions
- Per propagation-pattern (Fire 76+): the second-brain + /root patterns inherit-from / inform-source for sister projects post-tier-3

## When Not To

- Project has no compaction events (e.g., short-session-only operation)
- All in-flight state is already in operator's primary memory (low body-of-work)
- Hooks layer not supported by harness (rare)
- Compaction event-handling deferred to operator-only manual recovery (operator-explicit override)

## Empirical Evidence

Per Fire 102 worked-example: 2026-05-08 compaction event triggered at 5% remaining (operator-surprise); the second-brain has no PreCompact hook; handoff doc never authored; post-compact agent acted on conversation summary alone; about-to-execute pre-compact pending pipeline-post call without regathering context. Operator caught + intervened. Without this spec's structural fix: recurrence highly likely (per Fire 95 pattern-recurrence cluster).

Per Fire 103 4-tier audit: impl-spec #10 currently at Tier 2 (50% — PostCompact only). Authoring this spec ALONE doesn't elevate to Tier 3 (still designed-only); IMPLEMENTING per the template + WIRING in settings.json IS the Tier 2 → Tier 3 transition.

Per the second-brain's bidirectional inheritance rule: /root has working pre-compact.sh; the second-brain should inherit pattern with adaptations. This spec captures the adaptation.

## Required Gates (per hook-architecture proposal #2 4th component)

```yaml
required_gates:
  empirically_passed:
    - synthetic_handoff_doc_schema: passed via mock 11-section template
    - python_hook_template_syntax: passed via Python AST parse (this fire's authoring)
  pending:
    - real_session_pre_compact_event: pending — depends on hook implementation + wiring + manual /compact trigger
    - real_session_post_compact_handoff_read: pending — depends on PostCompact agent reading the handoff doc
    - timeout_compliance_15s: pending — measure pipeline-status invocation duration
    - sister_project_inheritance_validation: pending — compare the second-brain adaptation against /root original
    - operator_empirical_section_coverage: pending — operator confirms 11 sections capture all relevant state
  composite_compliance: pre-compact-handoff-axis stress-test 0% (forward-anchored; M1+ implementation per Task #28)
```

## Path-to-Tier-4 (per Fire 103 4-tier audit method)

```
TIER 1 (designed only): COMPLETE — this spec is the design
  ↓ (operator confirms; agent or operator wires hook + settings.json)
TIER 2 (partial implementation): N/A — this spec is full bidirectional, not partial
  ↓ (skip — full implementation per template + settings.json)
TIER 3 (implemented but not enforced): TARGET — Task #28 completion
  At this state: hook fires per PreCompact; handoff doc authored; agent ~85% compliance reading it
  ↓ (PreToolUse blocker hook OR detection-sentinel state-file)
TIER 4 (designed + implemented + enforced): FORWARD-ANCHORED — separate spec (Task #27)
  At this state: agent CANNOT execute pre-compact pending tool call without first running gateway orient + reading handoff doc
```

## Relationships


## Tags

[implementation-spec, pre-compact-hook, opt-second-brain, tier-elevation, path-to-tier-4, day-arc-2026-05-08, multi-day-pain-point-resolution, fire-105]
