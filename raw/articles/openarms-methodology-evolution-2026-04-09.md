---
title: "Methodology evolution — session findings and fixes"
type: note
domain: log
status: active
created: 2026-04-09
updated: 2026-04-09
tags: [methodology, evolution, lessons, session]
---

# Methodology Evolution — 2026-04-09

This document records the methodology bugs found, fixes applied, and lessons learned during the first day of autonomous agent operation. These findings should inform future methodology revisions.

## Bug 1: Tasks Marked Done Without Completing Stages

**Found:** Tasks were binary done/not-done. No stage tracking in frontmatter. Agent could check Done When boxes without verification and skip straight from "active" to "done" after one stage.

**Fix:** Added `task_type`, `current_stage`, `readiness`, `stages_completed`, `artifacts` to task frontmatter. Schema enforces these fields. Reset all 22 tasks to honest status. 6 tasks moved from "done" back to "in-progress."

**Lesson:** Binary status is not enough. Progress must be tracked at the stage level with percentage readiness. Every stage transition must update frontmatter and commit.

## Bug 2: Epic Status Not Computed From Children

**Found:** All 8 epics were "draft" when work was in-progress. Epics could be manually marked "done" when zero children were complete.

**Fix:** Added item hierarchy rules: epics are containers, status/readiness computed from children, max agent-settable status is "review." Added `computed_fields: [readiness, status]` to epic schema.

**Lesson:** Parent items should never be set directly. They derive from children. An epic at 30% for weeks is normal.

## Bug 3: Agent Creates Rogue Tasks

**Found:** Agent ignored existing tasks in the Active section and created its own task files, reusing existing task IDs (T026-T029). Created naming collisions and diverged from the operator's intended backlog.

**Fix:** Added directive Section 7.1: "Pick from existing tasks ONLY. Do NOT create new task files." Added 8.2 Task Management Violations. Report detects `unauthorized_task_creation`.

**Lesson:** Task creation is an operator responsibility, not an agent responsibility. Agent executes, operator directs.

## Bug 4: Files Lost in Shared Workspace

**Found:** Write tool reported success for T024/T025. Files disappeared between creation and `git add -A`. Root cause: a failed `git revert` in the same workspace destroyed untracked files.

**Investigation:** Session log showed files existed (backed up by harness at 17:02:10 UTC), gone by 17:04:41 UTC. Only operation in that window was a failed `git revert`. Files recovered from Claude Code file-history backups.

**Fix:** Added directive rules: "commit immediately after creating files" and "never run destructive git commands without checking git status." Added memory entries for future sessions.

**Lesson:** Untracked files are fragile. Commit immediately. Shared workspaces amplify risk.

## Bug 5: Stage Boundaries Not Respected

**Found:** Scaffold stage produced 135-line env reader with business logic (should be implement). Implement stage was a no-op (just updated frontmatter). Test stage marked done with 1 failing test.

**Fix:** Added explicit ALLOWED/FORBIDDEN lists per stage in directive Section 6. Added scaffold vs implement comparison table. Test stage gate requires `pnpm test --` with 0 failures. Methodology protocols updated with forbidden_artifacts.

**Lesson:** Stage names alone are not enough. Each stage needs explicit boundaries — what you CAN produce, what you CANNOT, and what tools to run as a gate check.

## Bug 6: Orphaned Implementations

**Found:** Agent produced 2,073 lines of production code across network rules, cost tracking, and hook events. None of it was imported by the actual runtime. Code passed tests in isolation but the product didn't use it.

**Fix:** Implement stage now requires "at least one existing runtime file imports the new code." Done When must name the specific consumer file. Report detects `orphaned_implementation` violations.

**Lesson:** "Tests pass" is not "feature works." Implement means wired into the runtime, not standalone. Perfect LEGO pieces must be snapped together.

## Bug 7: Stream-JSON Logs Unreadable

**Found:** Agent run logs were raw JSON (95% stream_event token chunks). Impossible to monitor live or produce post-run reports. Sub-agent work was invisible.

**Fix:** Built `scripts/agent-report.py` (stream aggregation, stage tracking, compliance checking, loop detection, error classification, cost per stage) and `scripts/agent-watch.sh` wrapper. Token chunks aggregated into one line per tool call.

**Lesson:** Observability is not optional. You must be able to see what the agent is doing in real-time and verify after the fact.

## Open Issues

### implement_modified_tests False Positive

The compliance checker detects Edit calls to test files during implement stage. However, the stage transition detection from frontmatter edits may be slightly offset from actual file modifications. Needs investigation — the rule is correct but the timing window may cause false positives.

### Node 18 Compatibility

Environment runs Node 18 but repo requires Node 22+. Agent repeatedly hits `Unsupported engine` warnings and `npx vitest` failures. Workaround: directive specifies `pnpm test --` wrapper. Real fix: upgrade Node.

### Cost Per Stage Accuracy

Per-stage cost in reports is approximate (derived from token counts in stream events). Sub-agent costs are not properly attributed to stages. Total cost from result event is accurate but stage breakdown can exceed 100%.

### Read Spirals

Agent reads 9-10 files consecutively during research phases. Not necessarily a bug — reading code before acting is good methodology. But 10 consecutive reads with no action may indicate the agent is lost. Loop detection threshold may need tuning.

## Methodology Version History

| Version | Date          | Changes                                                                                                                       |
| ------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| v1      | 2026-04-08    | Initial: 5 stages, modes, end conditions                                                                                      |
| v2      | 2026-04-09 AM | Added stage tracking fields, task_type, artifact verification                                                                 |
| v3      | 2026-04-09 PM | Added item hierarchy, computed epic readiness, no-task-creation rule                                                          |
| v4      | 2026-04-09 PM | Added stage ALLOWED/FORBIDDEN lists, scaffold vs implement table                                                              |
| v5      | 2026-04-09 PM | Added integration requirement: implement must wire into runtime                                                               |
| v6      | 2026-04-09 PM | Bridge module pattern, commit-based stage tracking, research cost stage, integration point template, compliance checker fixes |
