# User Directive — 2026-04-09 — OpenArms Methodology YAML + Agent Directive (Latest)

## Context

The user shared the latest OpenArms methodology.yaml and agent-directive.md as the reference model for the methodology framework brainstorm. Key distinction: superpowers specs/plans are for WORK EXECUTION (how to build something). The methodology backlog is for PROJECT MANAGEMENT and OBSERVABILITY (tracking what work exists, what stage it's at, what's done). Both coexist — different concerns.

OpenArms is adapted for solo-agent mode but the patterns are transferable.

## Key patterns from the shared content:

### 5-stage methodology with hard boundaries
- document → design → scaffold → implement → test
- Each stage has required_artifacts and a protocol injected into context
- ONE COMMIT PER STAGE (not per task)
- Readiness ranges: 0-25%, 25-50%, 50-80%, 80-95%, 95-100%

### Task types with per-type stage requirements
- epic: all 5 stages
- module: all 5 stages
- task: scaffold, implement, test (skip document/design)
- bug: document, implement, test
- spike: document, design only (research, no code)
- docs: document only
- refactor: document, scaffold, implement, test

### Item hierarchy: EPIC → MODULE → TASK
- Work on TASKS, not epics
- Readiness flows UPWARD (epic readiness = avg of children)
- Status flows UPWARD (any child in-progress → parent in-progress)
- Epics NEVER manually marked "done" — computed from children, max "review"

### Execution modes
- autonomous: works until backlog-empty
- full-autonomous: skips document on tasks
- semi-autonomous: pauses between tasks for review
- document-only / design-only / scaffold-only: partial runs
- custom: per-invocation config

### End conditions
- backlog-empty, stage-reached, time-limit, cost-limit, task-count

### The work loop (14 steps)
1. Read backlog → find highest priority undone task
2-8. Execute stage → produce artifacts → update frontmatter → commit
9-14. Loop stages → mark done → update parent → report to log → check end condition

### Quality gates per stage
- Document: wiki page with summary + gap analysis
- Design: decision doc + config shape + type sketches IN DOCS
- Scaffold: types compile + .env entries + empty test files
- Implement: code compiles + lint passes
- Test: scoped tests pass + no regressions
