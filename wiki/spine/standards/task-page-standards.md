---
title: "Task Page Standards"
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
    file: config/artifact-types.yaml
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
| **Summary** | What this task produces | 1-2 sentences |
| **Done When** | Verifiable completion checkboxes | ≥1 item naming a specific file/output |

### The Gold-Standard Exemplar

> [!success] [[Test OpenAI backend with LocalAI]] — 33 lines
>
> - Short and focused — one deliverable
> - Done When items verifiable with commands
> - Full frontmatter: status, priority, epic, task_type, stage, readiness, estimate

### Template

`config/templates/task.md` — scaffold via `python3 -m tools.pipeline scaffold task "Title"`

## Relationships

- BUILDS ON: [[Backlog Hierarchy Rules]]
- FEEDS INTO: [[Model: Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Backlog Hierarchy Rules]]
[[Model: Methodology Standards — What Good Execution Looks Like]]
