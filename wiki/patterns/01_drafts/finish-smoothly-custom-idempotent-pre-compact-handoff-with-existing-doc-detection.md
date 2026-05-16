---
title: "/finish-smoothly Custom Idempotent — Pre-Compact Handoff with Existing-Doc Detection"
type: pattern
domain: patterns
status: draft
confidence: medium
created: 2026-05-08
updated: 2026-05-08
maturity: seed
sources:
  - id: operator-directive-pre-compact-finish-smoothly
    type: file
    file: raw/notes/2026-05-08-pre-compact-imminent-validate-adjust-auto-compact-auto-dream-finish-smoothly-directive.md
    description: "Operator verbatim — pre-compact directive at 5%"
  - id: operator-directive-finish-smoothly-idempotent
    type: conversation
    file: raw/notes/2026-05-08-pre-compact-imminent-validate-adjust-auto-compact-auto-dream-finish-smoothly-directive.md
    description: "Operator verbatim 2026-05-08 (this turn): force finsih smoothly if there is not already a defined handoff document or whatnot so that we dont double when there is already a handoff lol or we make it smart / idempotent and whatnot... we work on this now"
  - id: fire-105-pre-compact-handoff-spec
    type: wiki
    file: wiki/patterns/01_drafts/pre-compact-handoff-hook-implementation-spec-for-opt-path-to-tier-4-for-impl-spec-10.md
    description: "PreCompact handoff hook implementation spec — composes with this pattern"
  - id: fire-157-pre-compact-python-draft
    type: wiki
    file: wiki/patterns/01_drafts/pre-compact-handoff-hook-python-draft-agent-authored-deterministic-state-snapshot.md
    description: "Python hook draft that drops sentinel"
  - id: fire-158-pretooluse-blocker-draft
    type: wiki
    file: wiki/patterns/01_drafts/post-compact-pretooluse-blocker-hook-python-draft-agent-authored-tier-4-enforcement.md
    description: "PreToolUse blocker that consumes sentinel"
  - id: pre-compact-handoff-test-case
    type: wiki
    file: wiki/log/2026-05-08-PRE-COMPACT-HANDOFF-MANUAL-imminent-compaction-state-snapshot.md
    description: "Existing manual handoff doc — IS the test case for idempotency"
tags: [finish-smoothly, idempotent, pre-compact, handoff, custom-variant, agent-draft, fire-226]
---

# /finish-smoothly Custom Idempotent — Pre-Compact Handoff with Existing-Doc Detection

> **DRAFT — agent-authored 2026-05-08 per SB-095** in direct response to operator verbatim directive: *"force finsih smoothly if there is not already a defined handoff document or whatnot so that we dont double when there is already a handoff lol or we make it smart / idempotent and whatnot... we work on this now"*. Operator may revise / promote / replace.

## Summary

A custom `/finish-smoothly` variant adapted for the auto-compact-imminent situation. Triggers when context-window <10k tokens remaining. Idempotent by design — detects existing recent pre-compact-handoff doc + skips re-authoring (or refreshes if stale) so two agents (or two cron-fires + one operator) don't double-author. Continues productive work after handoff lands until compaction fires; on PostCompact, performs project-knowledge regather (not just task-at-end), driven by deterministic chain.

## Pattern Description

The base `/finish-smoothly` slash command (Claude Code skill, harness-provided) is a forced knowledge-extraction PASS + handoff. The PROBLEM the operator surfaced: at the auto-compact-imminent 5% threshold, the agent may invoke `/finish-smoothly` unconditionally; if a handoff doc already exists from a prior PreCompact-hook fire (Fire 105 + Fire 157 spec) OR a prior agent-manual authoring (this conversation Fire 225), invoking again **doubles the work** — two handoff docs, neither authoritative.

The CUSTOM variant solves doubling via three idempotency mechanisms:

1. **Detection check (FIRST)**: glob `wiki/log/*pre-compact-handoff*.md` AND `raw/notes/*pre-compact*.md` AND check `.claude/post-compact-recovery-required` sentinel; if any modified within last 1 hour AND content covers current state — SKIP authoring.
2. **Refresh judgment (SECOND)**: if existing doc is >1 hour old OR substantial state change since (e.g., +50 pieces / new operator directive registered / cluster transition), REFRESH the existing doc rather than authoring NEW.
3. **Continue-till-compact (THIRD)**: after handoff lands (whether new-author / refresh / skip), the agent KEEPS WORKING per /loop directive until compaction actually fires. The handoff being "done" is not a stop signal — the loop continues; another fire may trigger another check; idempotency holds.

### Trigger condition

- Context-window remaining <10k tokens (per operator: *"when we are at < 10k token left of window"*)
- OR operator-explicit invocation (`/finish-smoothly` typed)
- OR PreCompact hook fires (Fire 105 + Fire 157 spec — auto-handoff path)

### Idempotency check (pseudocode)

```
def finish_smoothly_idempotent():
    # Step 1: detect existing handoff
    handoff_globs = [
        "wiki/log/*pre-compact-handoff*.md",
        "wiki/log/*PRE-COMPACT-HANDOFF*.md",
        "raw/notes/*pre-compact*handoff*.md",
    ]
    sentinel = ".claude/post-compact-recovery-required"

    recent_handoffs = []
    for pattern in handoff_globs:
        for path in glob(pattern):
            mtime = os.path.getmtime(path)
            if (now - mtime) < 3600:  # within last hour
                recent_handoffs.append((path, mtime))

    if recent_handoffs:
        most_recent = max(recent_handoffs, key=lambda x: x[1])
        # Step 2: judge refresh-or-skip
        state_delta = compute_state_delta_since(most_recent[1])
        if state_delta_substantial(state_delta):
            refresh_handoff(most_recent[0], state_delta)
            log("refreshed existing handoff at " + most_recent[0])
        else:
            log("skipped — existing handoff at " + most_recent[0] + " is current")
    else:
        # Step 3: author NEW handoff
        author_new_handoff()
        log("authored new handoff (no existing found)")

    # Step 4: drop sentinel for PreToolUse-blocker (Fire 158 consumer)
    write_sentinel(sentinel)

    # Step 5: continue work per /loop directive (no auto-stop)
    return  # control returns to caller; loop continues
```

### Post-compact procedure (PROJECT-KNOWLEDGE regather)

Per operator directive: *"read the handoff and do the group of operations needed to regather the context properly, not only the task at end but the general needed knowledge per-project before starting working or doing anything"*.

The post-compact agent MUST:

1. Run `.venv/bin/python -m tools.gateway orient` (deterministic chain)
2. Read THE handoff doc (most-recent matching glob above)
3. Read project-level brain files: `CLAUDE.md`, `AGENTS.md`, `CONTEXT.md`
4. Read `.claude/rules/{work-mode,self-reference,learnings,methodology}.md`
5. Read recent operator directives in `raw/notes/2026-05-*.md` (chronological top-5)
6. Read recent session logs in `wiki/log/2026-05-*.md` (chronological top-5)
7. Project-level knowledge regather (per operator's "general needed knowledge per-project"):
   - 4 governing principles (P1-P4) per CONTEXT.md
   - Methodology engine 5 stages × ALLOWED/FORBIDDEN
   - 16 named models per super-model
   - Hook architecture + currently-wired hooks
   - 28 MCP tools catalog
   - Sister-project ecosystem (5 projects)
8. THEN AND ONLY THEN respond to operator OR continue prior work
9. Remove sentinel only after STEP 1-7 verified (per Fire 158 PreToolUse-blocker)

## When To Apply

- **Auto-compact imminent at <10k tokens** AND handoff hook NOT yet wired (PreCompact / Fire 105 spec is a Tier 0/1 design at this writing) — the manual-applied form of this pattern keeps the doubling-bug closed even before automation lands
- **Operator-explicit `/finish-smoothly` at end of long session** — idempotency check ensures the agent doesn't redundantly author on top of a hook-emitted handoff
- **Cron-fire mid-conversation when context-thresholds detected** — same idempotency principle
- **Multi-agent / parallel-session scenarios** — idempotency check prevents two agents (e.g., this session + cron-fire) from racing to author handoff doc

## When NOT To Apply

- **Context window comfortable (>10k tokens)** — premature handoff authoring wastes context
- **Operator-explicit "do not handoff"** — operator-words sacrosanct; if operator says skip handoff, skip
- **Active operator-iteration in flight** — if operator is actively typing corrections / directives, handoff doc would race the directive registration; defer one fire
- **No detectable substantive state to capture** — if conversation has done minimal work since last fire, handoff is unnecessary
- **Sentinel `.claude/post-compact-recovery-required` already exists from prior compaction not yet acknowledged** — different signal; means PRIOR compaction recovery is incomplete; operator should clear before authoring NEW handoff

## Instances

### Test case (this conversation, 2026-05-08)

**Existing artifact**: `wiki/log/2026-05-08-PRE-COMPACT-HANDOFF-MANUAL-imminent-compaction-state-snapshot.md` (Fire 225)

**What this pattern says SHOULD happen if `/finish-smoothly` invoked NOW**:

- Step 1: glob `wiki/log/*pre-compact-handoff*.md` finds the Fire 225 doc (mtime <1 hour ago)
- Step 2: state-delta since Fire 225 = ~1 fire (this Fire 226 = the spec being authored); not substantial
- Step 3: SKIP authoring (or LOG-only refresh marking "Fire 226 spec landed; idempotency-pattern now defined")
- Step 4: drop sentinel `.claude/post-compact-recovery-required`
- Step 5: continue work per /loop directive

**Why this test case matters**: validates idempotency in the wild. Without the pattern, an agent at 5% context would invoke `/finish-smoothly` and author a SECOND handoff doc — two handoffs, neither authoritative, post-compact agent confused.

### Composition with Fire 105 / Fire 157 PreCompact hook

When PreCompact hook is wired (Fire 105 implementation spec → Fire 157 Python draft):

- PreCompact hook fires deterministically at compact-imminent
- Hook authors handoff doc to `wiki/log/<ts>-pre-compact-handoff.md`
- Hook drops sentinel `.claude/post-compact-recovery-required`
- Hook returns; compaction fires; PostCompact runs

If `/finish-smoothly` is also invoked manually at <10k:

- Idempotency check finds the hook-authored doc
- SKIPs (hook output is authoritative)
- Confirms sentinel exists; doesn't double-drop

### Composition with Fire 158 PreToolUse-blocker

The sentinel `.claude/post-compact-recovery-required`:

- Authored by EITHER `/finish-smoothly` invocation OR PreCompact hook (whichever fires first)
- Consumed by Fire 158 PreToolUse-blocker post-compact (Tier 4 enforcement)
- Removed after STEP 1-9 of post-compact procedure complete

The idempotency principle extends: PreToolUse-blocker checks sentinel existence; doesn't matter who created it, doesn't matter how many times it was created, the blocker fires the same way until acknowledged.

### Body-wide pattern echo

The idempotency principle in this pattern (detect-existing → skip-or-refresh → continue) parallels:

- Pipeline post idempotency (running twice produces same end-state, not duplicate work)
- Methodology stage-gate idempotency (entering a stage twice doesn't double the work; idempotent advance)
- Tool re-runs (tools.gateway orient producing consistent output regardless of invocation count)

This pattern brings idempotency to the handoff layer specifically; previously implicit (operator manually noticed doubling); now explicit.

## Relationships

- **EXTENDS** `pre-compact-handoff-hook-implementation-spec-for-opt-path-to-tier-4-for-impl-spec-10` (Fire 105) — adds idempotency check to base spec
- **EXTENDS** `pre-compact-handoff-hook-python-draft-agent-authored-deterministic-state-snapshot` (Fire 157) — adds detection step before write
- **CONSTRAINS** `post-compact-pretooluse-blocker-hook-python-draft-agent-authored-tier-4-enforcement` (Fire 158) — sentinel consumer must tolerate "already-existed" state
- **DERIVED FROM** `auto-compact-disable-implementation-spec-prevention-layer-for-impl-spec-10-defense-in-depth` (Fire 107) — Layer-2 mitigation (handoff layer) within defense-in-depth triplet
- **RELATES TO** `loop-clear-criteria-pattern-ready-for-review-stop-conditions-and-re-loop-triggers` (Fire 121) — handoff is one of the multi-fire-block governance steps
- **IMPLEMENTS** Fire 225 manual handoff doc as test case — validates pattern in production

## Composition with the auto-compact-disable defense-in-depth triplet

| Layer | Mechanism | Spec | This pattern's role |
|---|---|---|---|
| L1 Prevention | Disable auto-compact globally | Fire 107 spec | Pattern doesn't run if auto-compact disabled (no compaction → no need) |
| L2 Mitigation | PreCompact handoff (this pattern's home) | Fire 105 spec + Fire 157 draft | THIS pattern's idempotency engine |
| L3 Enforcement | PostCompact PreToolUse-blocker | Fire 106 spec + Fire 158 draft | Sentinel consumer; coordinates with this pattern |

The triplet is operator-pending decision (B6/B7/B8 in Fire 225 handoff). This pattern unblocks Layer 2 specifically — the handoff layer can be wired before Layer 1 (auto-compact-disable) lands; idempotency holds either way.

## Forward-anchor for implementation

```
Status: DRAFT spec (this fire)
Next-step: operator endorsement of idempotency design
Effort estimate: 4-6h to wire (Python detection + glob + state-delta heuristic + log)
Dependency: NONE (Layer 2 standalone; Layer 1 + Layer 3 can land later)
Test case: re-author this conversation's Fire 225 handoff via the pattern; verify SKIP triggered
```

## Tags

[finish-smoothly, idempotent, pre-compact, handoff, custom-variant, agent-draft, fire-226]

## When Not To

- **Auto-compact is disabled (Layer 1 is active):** If auto-compact has been globally disabled (Fire 107 spec), no compaction will fire, so pre-compact handoff is unnecessary — skip this pattern.
- **Context window is healthy (>10k tokens):** This pattern is designed for the 5–10% context-remaining threshold. Invoking it early wastes tokens and produces premature handoff docs.
- **A recent, complete handoff doc already exists:** The idempotency check is the core of this pattern. If a fresh handoff doc exists and context state has not significantly changed since it was authored, the pattern should SKIP (not refresh) — double-authoring is the failure mode this pattern prevents.
- **Non-compaction context switches:** Normal task completion or operator-requested handoffs use the standard `/finish-smoothly` flow, not this custom variant.
