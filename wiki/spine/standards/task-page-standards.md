---
title: Task Page Standards
aliases:
  - "Task Page Standards"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-11
updated: 2026-04-11
sources:
  - id: artifact-types
    type: file
    file: wiki/config/artifact-types.yaml
tags: [standards, task, page-type, quality, exemplar, backlog]
---

# Task Page Standards

## Summary

Standards for task pages — the atomic work unit. Tasks are SHORT. Summary + Done When, that's it. If it needs more than 50 lines, it's probably a module or epic. Done When items must name SPECIFIC files, functions, or outputs — generic boilerplate lets agents cheat.

## Key Insights

1. **Tasks are atomic.** One task = one focused deliverable. If it touches 3 subsystems, break it into 3 tasks.

2. **Done When must name specific outputs.** "Generated page passes `pipeline post` validation" is verifiable. "Make it work well" is not. For code tasks: name the runtime file that must import the new code.

3. **Brevity is a feature.** A 200-line task description means the work wasn't broken down enough. Tasks are 20-50 lines.

## Deep Analysis

### Required Sections

| Section | Purpose | Minimum |
|---------|---------|---------|
| **Summary** | What this task produces | 1-2 sentences, name the deliverable |
| **Done When** | Verifiable completion checkboxes | ≥1 item naming a specific file or output |

### Required Frontmatter

| Field | Value | Why |
|-------|-------|-----|
| `type` | task | — |
| `priority` | P0-P3 | Scheduling within epic |
| `task_type` | task/bug/docs/refactor/hotfix/integration/evolve | Determines methodology model |
| `current_stage` | document/design/scaffold/implement/test | Where work stands now |
| `readiness` | 0-100 | Computed from stages_completed |
| `stages_completed` | list | Audit trail — which stages are done |
| `estimate` | XS/S/M/L/XL | Effort sizing |
| `epic` | epic ID | Parent container |
| `depends_on` | list | Blocking dependencies |

### Section-by-Section Quality Bar

#### Summary

- ONE focused deliverable per task. If it produces 3 things, it's 3 tasks.
- Name what will EXIST after the task is done, not what you'll DO.

**Good:** "Per-type content threshold validation reading from artifact-types.yaml."

**Bad:** "Work on improving validation." (vague, no deliverable named)

#### Done When

- Every item is a checkbox: `- [ ] statement`
- At least one item names a SPECIFIC file, command, or output
- For code tasks: name the runtime file that must import the new code
- For wiki tasks: name the page that must pass validation
- For tool tasks: name the command that must succeed

**Good:**
```markdown
- [ ] `tools/validate.py` reads `wiki/config/artifact-types.yaml` for per-type thresholds
- [ ] `python3 -m tools.pipeline post` passes with 0 errors
- [ ] Thin decision page triggers `rationale_below_threshold` warning
```

**Bad:**
```markdown
- [ ] Validation works correctly
- [ ] Tests pass
```

> [!warning] Generic Done When lets agents cheat
>
> OpenArms Bug 6: 2,073 lines of code "done" but nobody imported it. "Code exists" was treated as "code works." Specific Done When items naming consumer files would have caught this. Every Done When should be verifiable by a DIFFERENT agent running a command.

### The Gold-Standard Exemplar

> [!success] [[T001-test-openai-backend|Test OpenAI backend with LocalAI]] — 33 lines
>
> - Short and focused — one deliverable
> - Done When items verifiable with commands
> - Full frontmatter: status, priority, epic, task_type, stage, readiness, estimate
> - Belongs to parent epic via `epic:` field

### Common Failures

| Failure | What It Looks Like | The Fix |
|---------|-------------------|---------|
| **Task as essay** | 200+ lines of description | If it needs that much text, it's a module or epic |
| **Multiple deliverables** | "Build X, integrate Y, test Z" in one task | Break into 3 tasks |
| **Generic Done When** | "It works" / "Tests pass" | Name specific files, commands, outputs |
| **Missing epic** | Task exists without parent | Every task belongs to an epic |
| **Readiness inflation** | `readiness: 100` with `stages_completed: [document]` | Readiness must match stage completion |

### Content Thresholds

| Threshold | Value |
|-----------|-------|
| Max lines | ~50 (if longer, probably should be a module) |
| Min Done When items | 1 |
| Required frontmatter | priority, task_type, current_stage, readiness, epic |

### Annotated Exemplar: Well-defined task standards

> [!example]- What makes a good task page
>
> **Short and focused:** Tasks are ATOMIC — 20-50 lines. If it needs design decisions, it's a module not a task.
> **Done When names FILES:** "- [ ] `wiki/lessons/new-lesson.md` passes pipeline post" — not "lesson is written." The file name IS the verification.
> **Frontmatter audit trail:** current_stage, readiness, progress, stages_completed, artifacts — the HISTORY of execution is in the frontmatter, not in prose.
> **Specific Done When prevents cheating:** "src/hooks/event-firing.ts imports workspace-coordinator" tells the agent WHERE and WHAT. "Wired into runtime" lets the agent satisfy it cheaply under fatigue.

### Template

`wiki/config/templates/task.md` — scaffold via `python3 -m tools.pipeline scaffold task "Title"`

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **Model these standards serve** | [[model-methodology|Model — Methodology]] |
> | **Methodology standards** | [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]] |
> | **Template for this type** | `wiki/config/templates/task.md` |
> | **System map** | [[methodology-system-map|Methodology System Map]] |
> | **Learning path** | [[methodology-fundamentals|Learning Path — Methodology Fundamentals]] |

## Relationships

- BUILDS ON: [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
- FEEDS INTO: [[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[backlog-hierarchy-rules|Backlog Hierarchy Rules]]
[[model-methodology-standards|Methodology Standards — What Good Execution Looks Like]]
