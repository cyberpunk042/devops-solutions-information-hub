# Readiness vs Progress + Three PM Levels Directive — 2026-04-12

## Operator Directive (verbatim)

### Readiness vs Progress

> "I am pretty sure we also need to clarrify readiness vs progress on a task an epic a milestone and a module and a task and whatnot, so that its clear all the requirement of which and what mean what.."

> "Like readiness is one side of the sdlc and the progress is the other where after the information and definitions was ready to start working on / from. I dont know if I explained that well... but basically openfleet already does this and gate on task_readiness and then the task_progress can advance as after finished definition an Epic for example can start to be worked on iteratively to make advanced the progress after the readiness as already reached a certain stage that free / unblock the possibility to start doing work, and they evolving in paralelel till its more tightly coupled toward the last percentages."

> "99 to 100 can only be done by a human and a task must always be reviewed adverserially before being delivered. and systems or harnesses must know their responsabilities and when to delegate to the upper when present and for what is appropriate."

> "It all traceability and allow to enforce better the methodologies."

### Three Levels of PM

> "Lets remember they are also at least three level of PM. there the project level wiki LLM, there is the potential openfleet system (Mission control / Ops / Kanban Board) wrapping itself over it and the openarms arness and there is the dspd / Plane / The fulll project management tool with full SCRUM and agile capabilities and a real surfae not only for currenlty working on work but for all project and all levels and recorded in time and enable advanced integrations that complete tool chains and goup calls."

> "Openarms harness in standalone will only wotk with the Wiki LLM in the repo and the second brain / information-hub, and again barely,, you can enforte to some degree with the directives in the Claude file and such but its not bulletproof, if you enable the harness-v2 now at least you have a chance to at least adhere properly to the sdlc and methodologies and usage of LLM wiki and what it teaches (and what the second brain teaches -and instaured as a good source / ref). (maybe not sdlc yet in openarms through but eventually with the harness v3, it should, we will explain why and when to use and help with proper use of v1 vs v2 vs v3)"

> "So yeah through level of PM management that will interconnect and offer different degree and levels of capabilities / power / usable potential / scalability."

> "its important that we have and explain all the field that is 'needed' / suggested and enable advanced features and automations and control and observability"

## Requirements Extracted

### Readiness vs Progress — Two-Dimensional Tracking

1. **Readiness** = definition completeness (SDLC left side: requirements, design, planning). Measures: is this READY to be worked on?
2. **Progress** = execution completeness (SDLC right side: implementation, testing, delivery). Measures: how far along is the WORK?
3. They evolve in PARALLEL — readiness advances first, unblocks progress, then they converge toward 100%
4. Tightly coupled toward the end — last percentages require both readiness and progress to converge
5. 99→100 = HUMAN ONLY. Adversarial review required before delivery.
6. Systems/harnesses must know when to delegate upward

### Three PM Levels

1. **Level 1: Wiki LLM** (project-level, in-repo) — CLAUDE.md directives, wiki backlog, methodology.yaml. Solo agent with directives. Barely enforced. Harness v1.
2. **Level 2: Fleet System** (Mission Control / Ops / Kanban) — OpenFleet orchestrator, immune system, contribution gating, MCP tool blocking. Multi-agent. Harness v2 (can adhere to SDLC properly).
3. **Level 3: Full PM Tool** (DSPD / Plane) — Full SCRUM/agile, all projects visible, time tracking, advanced integrations, group calls, complete tool chains. Harness v3 (full SDLC).

### Harness Version Progression
- **v1** = standalone, Wiki LLM + second brain only, CLAUDE.md enforcement, barely bulletproof
- **v2** = harness with SDLC adherence, proper methodology + wiki usage enforcement
- **v3** = full SDLC integration, Plane/DSPD integration, complete traceability

### Frontmatter Fields Needed
- All fields should be documented: what they mean, when required, what they enable
- Fields enable: automation, control, observability, advanced features
- Distinction between "needed" and "suggested" fields
