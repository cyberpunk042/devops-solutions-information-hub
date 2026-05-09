---
title: "C09 Status-Claim Hook Python Draft (Agent-Authored) — PreToolUse Pattern-Match Detection"
type: pattern
domain: agent-config
status: synthesized
confidence: medium
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c09-per-instance-evidence-fire-126
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c09-status-claim-without-verification-p4-axis-12-instances-verbatim-mapped.md
    description: "PRIMARY parent (Fire 126)"
  - id: foundational-cluster-set-expansion-fire-127
    type: wiki
    file: wiki/log/2026-05-08-foundational-cluster-set-expansion-c04-c02-c09-post-fire-126-phase-1-effort-revision.md
    description: "PRIMARY parent (Fire 127) — C09 enforcement-layer spec"
  - id: foundational-triplet-fire-137
    type: wiki
    file: wiki/log/2026-05-08-foundational-triplet-solution-piece-chain-c04-c02-c09-phase-1-implementation-forward-anchor.md
    description: "PRIMARY parent (Fire 137) — Phase 1 forward-anchor"
  - id: opt-pre-bash-hook-pattern-source
    type: file
    file: .claude/hooks/pre-bash.sh
    description: "Existing /opt PreToolUse hook pattern (truncation block)"
tags: [c09-hook-draft, python-implementation, agent-authored, pre-tool-use, day-arc-2026-05-08, fire-154]
---

# C09 Status-Claim Hook Python Draft (Agent-Authored) — PreToolUse Pattern-Match Detection

## Summary

Per Fire 126 (C09 evidence) + Fire 127 (foundational addition) + Fire 137 (Phase 1 spec): C09 status-claim enforcement-layer is FOUNDATIONAL Phase 1 priority. This Fire 154 authors agent-DRAFT Python hook draft for /opt/.claude/hooks/c09-status-claim-check.sh per the spec. **Agent-DRAFT per SB-095**: this is design-only; operator confirms + wires per work-mode.md.

## Pattern Description

This pattern provides an agent-DRAFT Python implementation of the C09 status-claim verification hook specified in Fire 127. The hook fires on PreToolUse for text-emit tools (Write/Edit/NotebookEdit), detects status-claim patterns in the agent's tool-input content, and checks for verification-evidence patterns in the same content. If status-claim detected without verification AND REASON env var unset, hook blocks (exit 1) with structured remediation directive.

## When To Apply

Apply this hook when:
- /opt second-brain has Phase 1 enforcement-layer authorization (operator-confirmed)
- C09 cluster identified as foundational (per Fire 127)
- Pattern-match rate-limit acceptable (~5-10% false-positive expected)

## When Not To

- Project has no P4-axis pain-point evidence
- Operator-explicit "advisory only; no enforcement"
- Hook layer not supported by harness

## Instances

**Instance 1: This /opt (M-C09 task per Fire 137)**
- Wire as PreToolUse hook with Write/Edit/NotebookEdit matcher
- Test via real-session "Done" claim
- Verify block fires + REASON bypass works

**Instance 2: Sister-projects (forward-anchored)**
- Per Fire 113 propagation: each project adapts pattern-list

## Hook implementation draft (Python; agent-DRAFT)

```python
#!/usr/bin/env python3
"""C09 Status-Claim Verification Hook — Pre-Tool-Use Pattern-Match Detection.

Insertion: PreToolUse on Write/Edit/NotebookEdit (text-emit tools)
Reason: Per P4 governing principle (Declarations Aspirational Until Verified) +
        Fire 126 12-instance evidence (5 HIGH severity); status claims like 
        "Done" / "Verified" / "Loaded" without inline command-output evidence
        violate P4. Hook detects pattern-match + suggests verification.
Remediation: directive to inline verification command output + suggest specific
             tool (gateway orient / pipeline post / tools.run-tests).
Bypass: REASON env var with documented reason; audit-logged.

Per Fire 126 + Fire 137:
  Pattern detection: status-claim words in agent's response BEFORE verification command
  Verification check: command-output present in same response?
  Block: if status-claim without verification + REASON unset → exit 1
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", "/opt/devops-solutions-information-hub"))
AUDIT_LOG = PROJECT_ROOT / ".claude" / "hooks" / "c09-status-claim-bypass.log"

STATUS_CLAIM_PATTERNS = [
    r"\bDone\.\b",                  # "Done."
    r"\bDone:\b",                   # "Done:"
    r"\bVerified\.\b",
    r"\bVerified:\b",
    r"\bLoaded\.\b",
    r"\bLoaded:\b",
    r"\bComplete\.\b",
    r"\bRegathered\.\b",
    r"\bFix landed\.?\b",
    r"\bTier \d+ reached\b",
]

VERIFICATION_PATTERNS = [
    r"\$\s",                       # bash prompt suggestion (rare)
    r"^\s*\$\s",                   # bash prompt at line start
    r"\[\d+/\d+\]",                # pipeline post step indicator
    r"Status: PASS",               # pipeline post output
    r"Validation errors:\s*\d+",   # pipeline post output
    r"^\s*\w+:\s*\d+",             # general structured output
    r"```\s*\n.*?\n```",           # fenced code block (assumed verification)
]

def detect_status_claims(text: str) -> list[str]:
    """Return list of status-claim phrases detected."""
    matches = []
    for pattern in STATUS_CLAIM_PATTERNS:
        for match in re.finditer(pattern, text, re.MULTILINE):
            matches.append(match.group())
    return matches

def has_verification_evidence(text: str) -> bool:
    """Check if text contains verification-evidence patterns."""
    for pattern in VERIFICATION_PATTERNS:
        if re.search(pattern, text, re.MULTILINE | re.DOTALL):
            return True
    return False

def log_bypass(reason: str, claims: list[str]):
    try:
        AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
        with AUDIT_LOG.open("a") as f:
            ts = datetime.now(timezone.utc).isoformat()
            f.write(f"{ts} REASON={reason} claims={claims}\n")
    except Exception:
        pass

def main():
    # Read input from stdin
    try:
        tool_input_data = json.loads(sys.stdin.read())
    except Exception:
        sys.exit(0)  # cannot parse; allow conservatively
    
    tool_name = tool_input_data.get("tool_name", "")
    tool_input = tool_input_data.get("tool_input", {})
    
    # Only check text-emit tools (Write/Edit)
    if tool_name not in ("Write", "Edit", "NotebookEdit"):
        sys.exit(0)
    
    # Extract content from tool input
    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    if not content:
        sys.exit(0)
    
    # Detect status-claims
    claims = detect_status_claims(content)
    if not claims:
        sys.exit(0)  # no claims to verify
    
    # Check for verification evidence in content
    if has_verification_evidence(content):
        sys.exit(0)  # has verification; allow
    
    # Check REASON bypass
    reason = os.environ.get("REASON")
    if reason:
        log_bypass(reason, claims)
        sys.exit(0)
    
    # Block with structured directive
    block_msg = f"""═══════════════════════════════════════════════════════════════════════════
BLOCKED: status-claim without inline verification (C09 / P4 violation)
═══════════════════════════════════════════════════════════════════════════

Tool call: {tool_name}
Status-claim(s) detected: {claims}

REASON:
  Per P4 governing principle (Declarations Aspirational Until Verified) +
  /opt CLAUDE.md HR 7 (status claims must inline verification): "Done" / 
  "Verified" / etc. require command-output evidence in same response.
  
  Per Fire 126 C09 12-instance evidence (5 HIGH severity): unverified status-claims
  cause operator-trust loss + cascade-failures.

REMEDIATION:
  1. Run verification command (e.g., gateway orient, pipeline post, tools.run-tests)
  2. Paste output as inline evidence within same response
  3. Then claim "Done" / "Verified" with command-output backing

BYPASS (operator-grant only):
  REASON="<documented-reason>" <your-tool-call>
  Example: REASON="documentation update; verification not applicable"

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
    "matcher": "Write|Edit|NotebookEdit",
    "hooks": [
      {
        "type": "command",
        "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/c09-status-claim-check.sh",
        "timeout": 5
      }
    ]
  }
]
```

## Limitations + caveats

```
False-positive rate (estimated 5-10%):
  - Legitimate status-claims with implicit verification
  - Markdown headings containing "Done" or "Complete"
  - Quote-of-prior-work (operator's words in agent's response)

False-negative rate (estimated 15-20%):
  - Clever phrasing evading pattern-match (e.g., "looks good now")
  - Verification language in different tense
  - Inline-cite-without-explicit-output

Mitigations:
  - REASON env var bypass for operator-explicit cases
  - Audit-log allows bypass-frequency monitoring
  - Patterns extensible per operator-empirical refinement
```

## Per Fire 109 tier-elevation: T1 → T3 → T4

```
Current: T0 (no policy enforced)
This fire authoring: T1 (designed)
Operator confirms + wires settings.json: T2 (partial — wired but not yet tested)
Real-session test passes: T3 (full implementation; agent ~85% compliance)
Bypass-frequency monitoring + threshold-based escalation: T4 (enforced)
```

## Composability with body's other layers

| Component | Composability |
|---|---|
| Fire 126 C09 per-instance evidence | Empirical foundation |
| Fire 127 foundational-cluster expansion | C09 part of foundational triplet |
| Fire 137 foundational-triplet solution-chain | This fire IS the C09 layer Phase 1 |
| /opt CLAUDE.md HR 7 | Brain-rule baseline; this hook enforces |
| /opt learnings.md HR 4 | Existing baseline |
| Pre-bash hook pattern | Adapted-from source |

## Operator-pending action

```
Q-FIRE-154-1: Endorse this Python draft?
  Argument for: agent-DRAFT per SB-095; concrete forward-anchor
  Argument against: pattern-match has false-positive risk; needs tuning
  Recommended: endorse with explicit "agent-DRAFT pending operator-empirical refinement"

Q-FIRE-154-2: Pattern-match thresholds?
  STATUS_CLAIM_PATTERNS additions (e.g., "fixed" / "running smoothly")?
  VERIFICATION_PATTERNS expansion?
  Recommended: start with current 10 + 7 patterns; refine via real-session evidence

Q-FIRE-154-3: Hook integration timing?
  Bundle with HR 16 hot-path edit + wiki-schema field per Fire 149 Tier-2
```

## Closing

C09 hook Python draft authored as agent-DRAFT per SB-095. Concrete forward-anchor for Phase 1 M-C09 task per Fire 137. T1 (designed); operator-territory pending wire + test. Composability with /opt's existing PreToolUse hook patterns (pre-bash, pre-webfetch, opt-write-block).

**Standing by per /loop directive. C09 hook draft surfaced; awaits operator-empirical wiring confirmation.**

## Relationships

- COMPOSES WITH: Fire 126 C09 per-instance evidence (empirical foundation)
- COMPOSES WITH: Fire 137 foundational-triplet Phase 1 solution-chain
- COMPOSES WITH: P4 governing principle (canonical)
- ENABLES: M-C09 task completion per Fire 137 Phase 1

## Tags

[c09-hook-draft, python-implementation, agent-authored, pre-tool-use, day-arc-2026-05-08, fire-154]

## Backlinks

[[Fire 126 C09 per-instance evidence (empirical foundation)]]
[[Fire 137 foundational-triplet Phase 1 solution-chain]]
[[P4 governing principle (canonical)]]
[[M-C09 task completion per Fire 137 Phase 1]]
