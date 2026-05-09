---
title: "C02 Decision-Territory Hook Python Draft (Agent-Authored) — PreToolUse Pattern-Match Detection"
type: pattern
domain: agent-config
status: synthesized
confidence: medium
maturity: seed
authorship: agent-authored
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: c02-per-instance-evidence-fire-94
    type: wiki
    file: wiki/log/2026-05-08-per-instance-pain-point-evidence-c02-decision-territory-18-instances-verbatim-mapped.md
    description: "PRIMARY parent (Fire 94) — C02 baseline (18 instances)"
  - id: foundational-cluster-prioritization-fire-119
    type: wiki
    file: wiki/patterns/01_drafts/foundational-cluster-prioritized-enforcement-layer-pattern-c04-c02-coverage-maximizes-cross-cutting-prevention.md
    description: "PRIMARY parent (Fire 119)"
  - id: foundational-triplet-fire-137
    type: wiki
    file: wiki/log/2026-05-08-foundational-triplet-solution-piece-chain-c04-c02-c09-phase-1-implementation-forward-anchor.md
    description: "PRIMARY parent (Fire 137)"
  - id: c09-hook-draft-fire-154
    type: wiki
    file: wiki/patterns/01_drafts/c09-status-claim-hook-python-draft-agent-authored-pre-tool-use-pattern-match-detection.md
    description: "Sibling (Fire 154)"
  - id: c04-hook-draft-fire-155
    type: wiki
    file: wiki/patterns/01_drafts/c04-input-discipline-hook-python-draft-agent-authored-state-file-sentinel-pattern.md
    description: "Sibling (Fire 155)"
tags: [c02-hook-draft, python-implementation, agent-authored, decision-territory, day-arc-2026-05-08, fire-156]
---

# C02 Decision-Territory Hook Python Draft (Agent-Authored) — PreToolUse Pattern-Match Detection

## Summary

Per Fires 94 + 119 + 137: C02 decision-territory enforcement-layer per Phase 1 spec. This Fire 156 authors C02 hook draft using pattern-match approach (similar to C09; different vocabulary). Completes foundational-triplet hook drafts (C04 + C02 + C09).

## Pattern Description

C02 hook detects when agent's tool-input contains decision-words ("I'll choose / let me pick / the right approach is") that may overstep operator-territory. Pattern-match approach; cross-references with operator-pending-decisions (per task tracker). Block if decision is operator-territory + REASON unset.

## When To Apply

- Phase 1 enforcement-layer authorization
- C02 decision-territory cluster identified as foundational (per Fire 119)

## When Not To

- Project has no operator-territory boundary
- Operator-explicit "agent-decides everything" trust-tier

## Instances

**Instance 1: This /opt (M-C02 task per Fire 137)**
**Instance 2: Sister-projects (forward-anchored)**

## Hook implementation draft (Python; agent-DRAFT)

```python
#!/usr/bin/env python3
"""C02 Decision-Territory Verification Hook — PreToolUse Pattern-Match.

Insertion: PreToolUse on Write/Edit/Bash (decision-emitting tools)
Reason: Per C02 cluster (18 instances Fire 94; 73% in cross-cutting per Fire 115);
        agent over-stepping operator-territory causes operator-trust loss.
Mechanism: pattern-match agent's tool-input for decision-words.
Bypass: REASON env var with operator-grant evidence.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", "/opt/devops-solutions-information-hub"))
AUDIT_LOG = PROJECT_ROOT / ".claude" / "hooks" / "c02-decision-territory-bypass.log"

DECISION_PATTERNS = [
    r"\bI(?:'ll| will) (?:choose|pick|decide|select)\b",
    r"\blet me pick\b",
    r"\bthe right approach is\b",
    r"\bI'll go with\b",
    r"\bI'll commit to\b",
    r"\bdeciding to\b",
    r"\bI choose\b",
]

OPERATOR_GRANT_PATTERNS = [
    r"operator-confirmed",
    r"operator-empirical",
    r"per /loop directive",
    r"per operator's directive",
    r"agent-DRAFT",        # explicitly flagged as agent-only
    r"agent-territory",
]

def detect_decision_words(text: str) -> list[str]:
    matches = []
    for pattern in DECISION_PATTERNS:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            matches.append(m.group())
    return matches

def has_operator_grant(text: str) -> bool:
    for pattern in OPERATOR_GRANT_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

def log_bypass(claims: list[str], reason: str):
    try:
        AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
        with AUDIT_LOG.open("a") as f:
            ts = datetime.now(timezone.utc).isoformat()
            f.write(f"{ts} REASON={reason} claims={claims}\n")
    except Exception:
        pass

def main():
    try:
        tool_input_data = json.loads(sys.stdin.read())
    except Exception:
        sys.exit(0)
    
    tool_name = tool_input_data.get("tool_name", "")
    tool_input = tool_input_data.get("tool_input", {})
    
    if tool_name not in ("Write", "Edit", "NotebookEdit", "Bash"):
        sys.exit(0)
    
    content = (
        tool_input.get("content", "")
        or tool_input.get("new_string", "")
        or tool_input.get("command", "")
    )
    if not content:
        sys.exit(0)
    
    claims = detect_decision_words(content)
    if not claims:
        sys.exit(0)
    
    # If operator-grant pattern present, allow
    if has_operator_grant(content):
        sys.exit(0)
    
    # REASON env var bypass
    reason = os.environ.get("REASON")
    if reason:
        log_bypass(claims, reason)
        sys.exit(0)
    
    block_msg = f"""═══════════════════════════════════════════════════════════════════════════
BLOCKED: decision-territory potential overreach (C02)
═══════════════════════════════════════════════════════════════════════════

Tool call: {tool_name}
Decision-language detected: {claims}

REASON:
  Per C02 cluster (18 instances Fire 94; 73% cross-cutting per Fire 115):
  agent over-stepping operator-territory causes operator-trust loss.

REMEDIATION:
  1. Verify decision is agent-territory (per /opt work-mode.md)
  2. Add operator-grant cite (e.g., "per operator's directive 2026-05-08")
  3. Or flag as "agent-DRAFT per SB-095" (agent-territory authorship)
  4. Or surface as operator-pending decision (per Fire 110 question-registry)

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
    "matcher": "Write|Edit|NotebookEdit|Bash",
    "hooks": [
      {
        "type": "command",
        "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/c02-decision-territory-check.sh",
        "timeout": 5
      }
    ]
  }
]
```

## Limitations

- False-positive: legitimate agent-territory decisions (e.g., authoring standardize-extension proposals)
- False-negative: clever phrasing evading patterns
- Operator-grant pattern list extensible per real-session evidence

## Per Fire 109 tier-elevation: T0 → T1 → T3 → T4

```
Currently: T0
This fire: T1 (designed)
Wired: T3
Bypass-monitoring: T4
```

## Composability

- Fire 94 C02 evidence
- Fire 119 foundational prioritization
- Fire 137 Phase 1
- Fires 154+155 sibling hook drafts (C04 + C09)
- Words-are-sacrosanct.md (premise-confirmation gate sibling)

## Foundational-triplet hook drafts COMPLETE

```
C04 Fire 155: state-file sentinel approach
C02 Fire 156: pattern-match approach (this fire)
C09 Fire 154: pattern-match approach
Combined Phase 1 = 3 hook drafts ready for operator-empirical wiring
```

## Closing

C02 hook draft authored. Foundational-triplet hook drafts (C04 + C02 + C09) now COMPLETE as agent-DRAFTs. Combined Phase 1 forward-anchor: 48-72h operator-territory implementation per Fire 137.

**Standing by per /loop directive. Foundational-triplet hook drafts complete.**

## Relationships

- COMPOSES WITH: Fire 94 C02 evidence
- COMPOSES WITH: Fire 119 foundational prioritization
- COMPOSES WITH: Fire 137 Phase 1 forward-anchor
- COMPOSES WITH: Fires 154+155 (foundational-triplet siblings)
- ENABLES: M-C02 task completion

## Tags

[c02-hook-draft, python-implementation, agent-authored, decision-territory, day-arc-2026-05-08, fire-156]

## Backlinks

[[Fire 94 C02 evidence]]
[[Fire 119 foundational prioritization]]
[[Fire 137 Phase 1 forward-anchor]]
[[Fires 154+155 (foundational-triplet siblings)]]
[[M-C02 task completion]]
