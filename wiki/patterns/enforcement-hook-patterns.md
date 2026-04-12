---
title: "Enforcement Hook Patterns"
type: pattern
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Model: Skills, Commands, and Hooks"
  - "Model: Methodology"
instances:
  - page: "OpenArms pre-bash hook"
    context: "Blocks git commands from agent — harness owns git"
  - page: "OpenArms pre-write hook"
    context: "Blocks wrong-scope writes per methodology stage"
  - page: "OpenArms post-write hook"
    context: "Tracks files created per stage for artifact verification"
  - page: "OpenArms post-compact hook"
    context: "Rebuilds agent instructions after context compaction"
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: openarms-hooks
    type: file
    file: /home/jfortin/openarms/scripts/methodology/hooks/
  - id: openarms-agents
    type: file
    file: /home/jfortin/openarms/AGENTS.md
tags: [hooks, enforcement, agent-compliance, infrastructure, claude-code]
---

# Enforcement Hook Patterns

## Summary

Reusable hook patterns that enforce methodology compliance through infrastructure rather than instructions. Discovered through OpenArms's evolution from instruction-based enforcement (75% violation rate) to infrastructure enforcement (~90% compliance). Four hook types cover the enforcement surface: pre-tool hooks prevent wrong actions, post-tool hooks track state changes.

> [!info] Hook Pattern Reference Card
>
> | Hook | Type | What It Prevents | Compliance Impact |
> |------|------|-----------------|-------------------|
> | Scope Guard | PreToolUse:Bash | Blocks commands the agent shouldn't run (git, destructive ops) | High — prevents irreversible mistakes |
> | Write Guard | PreToolUse:Write/Edit | Blocks writes to wrong-scope paths per stage | Critical — enforces stage boundaries |
> | Artifact Tracker | PostToolUse:Write/Edit | Logs files created/modified for verification | Medium — enables gate checking |
> | Context Rebuilder | PostToolUse:Compact | Rebuilds instructions after context compaction | High — prevents rule loss |

## Pattern Description

> [!abstract] The Enforcement Hierarchy
>
> | Level | Mechanism | Strength | Coverage |
> |-------|-----------|----------|----------|
> | 1. Instructions | CLAUDE.md prose | Weakest — 25% compliance | Everything (but soft) |
> | 2. Structured instructions | ALLOWED/FORBIDDEN tables | Moderate — 50-60% | Rules that can be enumerated |
> | 3. Advisory hooks | Hook warns but doesn't block | Good — 70% | Actions with clear right/wrong |
> | 4. Blocking hooks | Hook prevents the action | Best — 90%+ | Critical violations only |
>
> Hooks are Level 3-4. Use them for violations that would be expensive to fix after the fact. Don't hook everything — over-hooking creates friction and the agent wastes tokens on denied attempts.

### Pattern 1: Scope Guard (Pre-Bash)

Intercepts shell commands and blocks those the agent shouldn't run.

```bash
#!/bin/bash
# pre-bash.sh — block commands the agent must not execute
COMMAND="$1"

# Block git commands — harness owns git
if echo "$COMMAND" | grep -qE "^\s*git\s+(add|commit|push|revert|reset|clean|checkout)"; then
  echo "BLOCKED: git commands are managed by the harness, not the agent."
  echo "Use /stage-complete to commit stage artifacts."
  exit 1
fi
```

**When to use:** When the agent should never run certain commands (git, rm -rf, deployment commands). The harness or operator owns these operations.

**When NOT to use:** For commands that are sometimes valid — use Write Guard instead for context-dependent blocking.

### Pattern 2: Write Guard (Pre-Write/Edit)

Intercepts file writes and blocks those that violate stage boundaries.

```bash
#!/bin/bash
# pre-write.sh — block writes that violate current stage scope
FILE_PATH="$1"
CURRENT_STAGE=$(cat .methodology/current-stage 2>/dev/null || echo "unknown")

case "$CURRENT_STAGE" in
  document|design)
    # Block source code writes during understanding stages
    if echo "$FILE_PATH" | grep -qE "^src/|\.ts$|\.py$|\.tf$"; then
      echo "BLOCKED: Cannot write source files during $CURRENT_STAGE stage."
      echo "Current stage allows only wiki pages and documentation."
      exit 1
    fi
    ;;
  scaffold)
    # Block test implementation writes during scaffold
    if echo "$FILE_PATH" | grep -qE "\.test\.(ts|py)$" && [ "$CURRENT_STAGE" = "scaffold" ]; then
      # Allow test stubs but not test implementations
      # (stub detection would need content analysis — simplified here)
      :
    fi
    ;;
esac
```

**When to use:** When stage boundaries must be enforced and the cost of violation is rework. This is the highest-value hook — it prevents the most common violation (writing code during document stage).

**Stage file requirement:** Needs a state file (`.methodology/current-stage`) that the harness updates at stage transitions.

### Pattern 3: Artifact Tracker (Post-Write/Edit)

Logs every file the agent creates or modifies for later verification.

```bash
#!/bin/bash
# post-write.sh — track artifact creation for gate verification
FILE_PATH="$1"
LOG=".methodology/stage-files.log"

echo "$FILE_PATH" >> "$LOG"
```

**When to use:** When the gate checker needs to know which files were produced during a stage. Without tracking, the gate can only check if expected files exist — not whether the agent created them during the right stage.

### Pattern 4: Context Rebuilder (Post-Compact)

Rebuilds critical instructions after context compaction removes them.

```bash
#!/bin/bash
# post-compact.sh — rebuild methodology instructions after compaction
# Reads current stage from state, outputs fresh instructions

CURRENT_STAGE=$(cat .methodology/current-stage 2>/dev/null || echo "unknown")
CURRENT_MODEL=$(cat .methodology/current-model 2>/dev/null || echo "unknown")

echo "=== POST-COMPACTION METHODOLOGY REFRESH ==="
echo "Current stage: $CURRENT_STAGE"
echo "Current model: $CURRENT_MODEL"
echo ""

# Re-inject stage-specific ALLOWED/FORBIDDEN
case "$CURRENT_STAGE" in
  document)
    echo "ALLOWED: Wiki pages, documentation, analysis"
    echo "FORBIDDEN: Source code, test files, config changes"
    ;;
  # ... etc
esac
```

**When to use:** For long-running sessions where context compaction may remove the CLAUDE.md methodology sections. Without this, agents lose their rules after compaction and revert to default behavior.

## Instances

> [!example]- Instance: OpenArms Enforcement Infrastructure (14 scripts + 4 hooks)
>
> **pre-bash.sh:** Blocks git add/commit/push/revert/reset/clean. Agent uses /stage-complete command which triggers harness git operations.
>
> **pre-write.sh:** Blocks src/ writes during document/design stages. Blocks _index.md editing (auto-maintained). Blocks .openarms/ state file editing (harness-owned).
>
> **post-write.sh:** Appends every created/modified file path to `.openarms/stage-files.log`. The validate-stage.cjs script reads this log to check which artifacts were produced.
>
> **post-compact.sh:** Calls `build-reinstruciton.cjs` which reads methodology.yaml + skill-stage-mapping.yaml and outputs fresh stage-specific instructions. This is the most complex hook — it effectively rebuilds the agent's methodology context from scratch after compaction.
>
> **Result:** Combined with 14 enforcement scripts, achieved ~90% stage boundary compliance. The pre-write hook alone eliminated the most common violation (writing code during document stage).

> [!example]- Instance: Research Wiki (No hooks currently)
>
> No enforcement hooks installed. Methodology compliance depends entirely on CLAUDE.md prose instructions. Agents frequently write implementation code before completing document stage. The pipeline post tool validates page quality but not methodology compliance.
>
> **Gap:** The research wiki would benefit from at minimum a Write Guard hook blocking tool modifications during document stage.

## When To Apply

> [!tip] Use Enforcement Hooks When
>
> - Moving to Tier 3+ methodology adoption (validation and enforcement)
> - Running autonomous agents (overnight runs, batch operations)
> - A specific violation keeps recurring despite instruction-level fixes
> - The cost of a violation is high (corrupted state, lost work, wrong architecture)
> - You have a state file system (.methodology/ or similar) tracking current stage

## When Not To

> [!warning] Don't Use Hooks When
>
> - You're at Tier 1-2 adoption (manual or configured — hooks add complexity)
> - The violation is genuinely ambiguous (hooks can't make judgment calls)
> - The agent needs flexibility (exploratory research, brainstorming)
> - You don't have stage tracking infrastructure (hooks without state are blind)
> - Over-hooking would cause >10% of legitimate actions to be blocked (friction kills productivity)

## Relationships

- DERIVED FROM: [[Model: Skills, Commands, and Hooks]]
- DERIVED FROM: [[Model: Methodology]]
- BUILDS ON: [[CLAUDE.md Structural Patterns for Agent Compliance]]
- RELATES TO: [[Stage-Gate Methodology]]
- RELATES TO: [[Model: Claude Code]]
- FEEDS INTO: [[Methodology Adoption Guide]]
- FEEDS INTO: [[Model: Methodology Standards — What Good Looks Like]]

## Backlinks

[[Model: Skills, Commands, and Hooks]]
[[Model: Methodology]]
[[CLAUDE.md Structural Patterns for Agent Compliance]]
[[Stage-Gate Methodology]]
[[Model: Claude Code]]
[[Methodology Adoption Guide]]
[[Model: Methodology Standards — What Good Looks Like]]
[[AI Agent Artifacts — Standards and Guide]]
[[Construction and Testing Artifacts — Standards and Guide]]
[[Methodology Framework]]
[[Methodology Standards — What Good Execution Looks Like]]
[[Stage-Aware Skill Injection]]
