---
title: Enforcement Hook Patterns
aliases:
  - "Enforcement Hook Patterns"
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
  - {'page': 'OpenArms pre-bash hook', 'context': 'Blocks git commands from agent — harness owns git'}
  - {'page': 'OpenArms pre-write hook', 'context': 'Blocks wrong-scope writes per methodology stage'}
  - {'page': 'OpenArms post-write hook', 'context': 'Tracks files created per stage for artifact verification'}
  - {'page': 'OpenArms post-compact hook', 'context': 'Rebuilds agent instructions after context compaction'}
created: 2026-04-11
updated: 2026-04-13
sources:
  - id: openarms-hooks
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms project reference"
  - id: openarms-agents
    type: file
    file: wiki/ecosystem/project_profiles/openarms/identity-profile.md
    description: "OpenArms project reference"
tags: [hooks, enforcement, agent-compliance, infrastructure, claude-code]
---

# Enforcement Hook Patterns

## Summary

Reusable hook patterns that enforce methodology compliance through infrastructure rather than instructions. Discovered through OpenArms's evolution from instruction-based enforcement (75% violation rate) to infrastructure enforcement (100% stage boundary compliance in v10, verified across 5 production runs). Four hook types cover the enforcement surface: pre-tool hooks prevent wrong actions, post-tool hooks track state changes. Total implementation: 215 lines of shell scripts replaced 28 CLAUDE.md rules that achieved 25% compliance.

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
> | Level | Mechanism | Measured Compliance | Coverage |
> |-------|-----------|-------------------|----------|
> | 1. Instructions | CLAUDE.md prose | 25% (OpenArms v4-v8 overnight) | Everything (but soft) |
> | 2. Structured instructions | ALLOWED/FORBIDDEN tables, numbered sequences | ~60% (OpenArms CLAUDE.md restructured) | Rules that can be enumerated |
> | 3. Advisory hooks | Hook warns but doesn't block | ~70% (estimated) | Actions with clear right/wrong |
> | 4. Blocking hooks | Hook prevents the action | 100% stage boundaries (OpenArms v10, 5 runs) | Critical violations only |
> | 5. MCP tool blocking | MCP server refuses tool call per stage | 100% tool-level (OpenFleet production) | Fleet with MCP server |
>
> Hooks are Level 3-5. Use them for violations that would be expensive to fix after the fact. Don't hook everything — over-hooking creates friction and blocks correct actions. See [[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]] for the risks of over-enforcement.

> [!warning] Compliance Is an Arms Race — OpenArms Evidence
>
> Across methodology v1-v8 (OpenArms), 4 of 6 documented bugs persisted despite directive-level fixes: epic readiness not computed from children (5 versions unfixed), scaffold business logic (4 versions), implement empty/orphaned (3 versions), Done When not verified (4 versions). The agent reads directives at session start, follows them for ~3 tasks, then DEGRADES under context pressure. Rules perceived as "optional" (metadata, documentation, logs) drop first.
>
> **Detection patterns are evadable.** The scaffold_business_logic checker looked for `.map()`, `.split()`, `.filter()`. Task T080 wrote 286 lines of parsing logic during scaffold WITHOUT triggering any pattern. The agent doesn't intentionally evade — it writes different code that happens to bypass the regex. Detection must evolve faster than evasion.
>
> **Lesson: if a directive fix didn't work twice, it won't work a third time. Skip straight to Layer 3 (runtime gates) or Layer 4 (automated remediation).** See [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]].

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

> [!example]- Instance: OpenArms v10 Enforcement Infrastructure (14 scripts + 4 hooks)
>
> **pre-bash.sh (48 lines):** Feature-flag gated (`.openarms/methodology-enforced`). Extracts command JSON via `node -e`. Hard blocks `git (add|commit|push|revert|reset|clean|stash|checkout --)` via regex. Stage-scopes test commands: `pnpm test -- (scoped)` only when current-stage == "test". Everything else (build, tsgo, check, ls, grep) passes.
>
> **pre-write.sh (106 lines):** 5 enforcement layers:
> 1. `.openarms/` directory blocked (state managed by harness)
> 2. Methodology infrastructure locked (scripts/, commands/, skills/, settings.json) unless meta-task flag set
> 3. Task frontmatter fields (status, readiness, current_stage, stages_completed, artifacts) blocked via grep on old_string
> 4. `src/` blocked during document/design stages
> 5. Real test assertions blocked during implement stage — counts `expect(` calls minus placeholders (`expect(true)`, `expect(1).toBe(1)`, `.toBeDefined()`), max 2 real assertions allowed
>
> **post-write.sh (36 lines):** Appends `${stage}:${filepath}` to `.openarms/stage-files.log`. Stage-tagging enables filtering to current stage only in validate-stage.cjs. Non-fatal: `>> log 2>/dev/null || true`.
>
> **post-compact.sh (29 lines):** Calls `build-reinstruction.cjs` which reads ALL state from `.openarms/` (current-stage, current-task-id, stage-files.log, required-stages.json, stages-completed.json, current-model-config.json). Returns full task state as `additionalContext` in hook response. See [[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]] for why this is critical.
>
> **validate-stage.cjs (1,033 lines):** The core enforcement engine. Model-aware: reads `current-model-config.json` to adapt validation per task type. Business logic detection: parses function signatures, strips strings/comments via state machine, counts control flow. Phantom file filtering: reverted files don't count as artifacts (git diff checks). Integration wiring: verifies at least one existing src/ file modified (blocks standalone new modules). Readiness capped by model config (research = 50%, feature-dev = 100%).
>
> **Result:** 0% stage boundary violations across 5 production runs (v10). Was 75% in v8. The hooks alone achieved what 28 CLAUDE.md rules could not.
>
> **Remaining gap:** Behavioral failures (6 classes) persist despite perfect stage enforcement. Clean completion rate = 20%. See [[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]].

> [!example]- Instance: OpenFleet MCP Tool Blocking + Agent Hooks (10 agents, production)
>
> OpenFleet enforces at a HIGHER level than Claude Code hooks — tools are blocked per stage in `methodology.yaml` `tools_blocked` field. The MCP server itself refuses the tool call before it reaches any hook.
>
> **Per-role hooks** (config/agent-hooks.yaml):
> - software-engineer: destructive command detection (blocks rm -rf, DROP TABLE, etc.)
> - devsecops-expert: credential scanning on file writes
> - All roles: conventional commit format validation on `fleet_commit` via PreToolUse
> - All roles: progress trail recording on PostToolUse for state-modifying calls → `.fleet-trail.log`
>
> **9 security-guidance patterns** injected via plugin (not hardcoded hooks). Per-role, context-aware.
>
> **Key difference from OpenArms:** Enforcement is declarative YAML, not shell scripts. The MCP server reads the config and enforces — no hook code to maintain per rule.

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

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- DERIVED FROM: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- DERIVED FROM: [[model-methodology|Model — Methodology]]
- BUILDS ON: [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
- RELATES TO: [[stage-gate-methodology|Stage-Gate Methodology]]
- RELATES TO: [[model-claude-code|Model — Claude Code]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
- EXTENDED BY: [[the-pre-write-hook-prevents-operator-claude-from-racing-the-|Pre-Write Hook Race Prevention — Operator/Agent File Contention (OpenArms)]]
- EXTENDED BY: [[agents-take-small-unauthorized-scope-expansions-when-the-cha|Clean-Win Scope Expansion — What Hooks Miss (OpenArms T116-T119)]]

## Backlinks

[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[model-methodology|Model — Methodology]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[model-claude-code|Model — Claude Code]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
[[Pre-Write Hook Race Prevention — Operator/Agent File Contention (OpenArms)]]
[[Clean-Win Scope Expansion — What Hooks Miss (OpenArms T116-T119)]]
[[ai-agent-artifacts|AI Agent Artifacts — Standards and Guide]]
[[agent-failure-taxonomy-seven-classes-of-behavioral-failure|Agent Failure Taxonomy — Seven Classes of Behavioral Failure]]
[[agents-take-small-unauthorized-scope-expansions-when-the-cha|Agents take small unauthorized scope expansions when the change is a 'clean win']]
[[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
[[context-compaction-is-a-reset-event|Context Compaction Is a Reset Event]]
[[enforcement-must-be-mindful-hard-blocks-need-justified-bypass|Enforcement Must Be Mindful — Hard Blocks Need Justified Bypass]]
[[harness-owned-loop-deterministic-agent-execution|Harness-Owned Loop — Deterministic Agent Execution]]
[[infrastructure-enforcement-proves-instructions-fail|Infrastructure Enforcement Proves Instructions Fail]]
[[methodology-framework|Methodology Framework]]
[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[stage-aware-skill-injection|Stage-Aware Skill Injection]]
[[src-openarms-v10-enforcement|Synthesis — OpenArms v10 — Infrastructure Enforcement and Agent Behavior]]
[[the-harness-turncount-variable-counts-streaming-events,-not-|The harness 'turnCount' variable counts streaming events, not conversational turns]]
[[the-pre-write-hook-prevents-operator-claude-from-racing-the-|The pre-write hook prevents operator-Claude from racing the running agent on backlog files]]
[[three-lines-of-defense-immune-system-for-agent-quality|Three Lines of Defense — Immune System for Agent Quality]]
[[validation-matrix-test-suite-for-context-injection|Validation Matrix — Test Suite for Context Injection]]
