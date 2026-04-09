---
title: "Integration sprint learnings"
type: note
domain: log
status: active
created: 2026-04-09
updated: 2026-04-09
tags: [integration, learnings, methodology, session]
---

# Integration Sprint Learnings — 2026-04-09

## Context

After finding that 2,073 lines of production code were orphaned (not imported by any runtime file), we added an integration requirement to the implement stage and created P0 integration tasks (T039-T041) to wire network rules, cost tracking, and hook events into the actual runtime.

## What Worked

### 1. Specific Done When items force real integration

When Done When says "`src/infra/net/fetch-guard.ts` imports and calls `evaluateHostAccess()`", the agent modifies that exact file. Vague items get checked off reflexively.

### 2. The agent creates bridge/adapter modules

Instead of making massive changes to existing files, the agent created thin adapter modules:

- `src/infra/net/network-rules-bridge.ts` — bridges resolver into fetch-guard
- `src/commands/agent-run-cost.ts` — bridges cost accumulator into agent-run
- `src/commands/agent-run-hooks.ts` — bridges hook events into agent-run

This is good architecture — minimal diff to core files, clean separation. Future methodology should recognize this pattern as valid.

### 3. Cost comparable to standalone tasks

$11.77 for 3 integration tasks (~$4/task). Standalone module tasks cost $3-10/task. Integration produces far more product value per dollar.

## What Needs Improvement

### 1. Compliance checker false positives on integration tasks

The `scaffold_business_logic` detector flags `.map()`, `.trim()`, `.split()` in modified existing files. Integration tasks inherently modify existing files that already contain these patterns. Need to:

- Only flag NEW files in scaffold, not edits to existing files
- Or whitelist patterns in files that existed before the task

### 2. implement_modified_tests timing issue

The stage transition detection from frontmatter edits is slightly offset from when files are actually modified. This causes false positives when the agent writes tests near a stage boundary. Need to:

- Track stage transitions by commit messages (more reliable) instead of frontmatter edit timestamps
- Or add a tolerance window around stage transitions

### 3. Cost per stage accuracy

Per-stage costs show >100% total because:

- Pre-stage research (reading code before starting scaffold) isn't attributed
- Sub-agent costs go to the wrong stage
- Stage transitions are detected late (frontmatter edit, not first file write)
  Solution: add a "research" pseudo-stage for pre-work, attribute sub-agent costs separately.

### 4. Task Done When should always name integration points

Every task of type `task` (not docs/spike) should have at least one Done When item naming the specific runtime file that consumes the new code. This should be enforced in the schema or at task creation time.

### 5. Bridge module pattern should be documented

The agent's pattern of creating adapter/bridge modules is good practice. Document it in the methodology as the preferred integration approach: create a thin bridge, import it from the consumer, keep the core module unchanged.

## Metrics

| Metric                 | Standalone (T023-T025) | Integration (T039-T041)           |
| ---------------------- | ---------------------- | --------------------------------- |
| Tasks                  | 3                      | 3                                 |
| Duration               | ~50min total           | 37min                             |
| Cost                   | ~$16 total             | $11.77                            |
| Commits                | 12                     | 9                                 |
| Tests                  | 83+                    | 53                                |
| Runtime files modified | 0                      | 3 (fetch-guard, agent-run, types) |
| Files created          | 8 standalone modules   | 6 (3 bridges + 3 tests)           |
| Product value          | None (orphaned)        | High (features work)              |

## Methodology Updates Needed

1. Document bridge module pattern in methodology
2. Fix compliance checker for integration task context
3. Add integration point requirement to task creation template
4. Track "research" as pseudo-stage for cost attribution
