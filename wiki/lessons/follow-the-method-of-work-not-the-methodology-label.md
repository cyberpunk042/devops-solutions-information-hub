---
title: "Follow the Method of Work Not the Methodology Label"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: high
maturity: growing
derived_from:
  - "Model: Methodology"
  - "Never Skip Stages Even When Told to Continue"
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: session-loop
    type: observation
    file: docs/SESSION-2026-04-12-handoff.md
    description: "Agent looped between research and production because 'follow the methodology' was interpreted differently by operator and agent"
  - id: operator-method
    type: directive
    file: raw/notes/2026-04-12-restart-from-scratch.md
    description: "Operator gave explicit 5-step method: record requirements → research → synthesize → investigate code → suggest solutions"
tags: [methodology, agent-failure, execution, circular-failure, method-of-work, lesson-learned]
---

# Follow the Method of Work Not the Methodology Label

## Summary

When told to "follow the methodology," an agent can enter a destructive loop: interpret "methodology" as "do the Document stage" (research), start researching, get told to "just do it," start producing, get told "follow the methodology," go back to research. The loop burns context and trust. The fix is an explicit method of work — concrete sequential steps that both operator and agent agree on — not a label that maps to different mental models.

## Context

> [!warning] When does this lesson apply?
>
> - The operator says "follow the methodology" or "do it properly" without specifying steps
> - You find yourself alternating between research and production without converging
> - The operator's frustration is escalating across multiple cycles
> - You've been told both "do the research" and "stop researching, just do it" in the same session

## Insight

> [!tip] The Ambiguity Trap
>
> "Follow the methodology" maps to different things:
>
> | Who | What they mean |
> |-----|---------------|
> | **Agent** | "Enter Document stage: read sources, produce wiki pages, validate" |
> | **Operator** | "Stop doing random things and work SYSTEMATICALLY toward the goal" |
>
> These are both valid interpretations. The methodology defines stages. The operator wants systematic progress. But they collide: the agent enters Document stage (research), the operator sees more research and no output, says "just do it," the agent jumps to Implement, the operator says "you're not following methodology," and the loop restarts.

The resolution is a **method of work** — an explicit, numbered, sequential protocol that both parties agree on. Not "follow the methodology" (a label) but "do these 5 things in this order" (a procedure):

1. Record the requirements
2. Research upon them (online research)
3. Synthesize after analysis
4. Investigate the codebase
5. Suggest solutions with a recommended path

This is different from a methodology stage gate. Stage gates define WHAT is allowed and forbidden. The method of work defines HOW you progress through a specific task. You can be in "Document stage" AND following the 5-step method — the method is the procedure WITHIN the stage.

## Evidence

> [!bug]- The Research-Produce Loop (2026-04-12)
>
> **Pattern observed:**
> 1. Operator: "follow the methodology"
> 2. Agent: launches research subagent, writes meta-document
> 3. Operator: "stop researching, DO it"
> 4. Agent: starts producing files rapidly
> 5. Operator: "you're not following methodology"
> 6. Agent: goes back to research
> 7. Repeat 3+ times
>
> **Context burned:** Significant portion of session context consumed by the loop. Operator trust dropped with each cycle.
>
> **Root cause:** "Follow the methodology" is ambiguous. The agent mapped it to "enter Document stage." The operator meant "work systematically." Neither was wrong; both were incomplete.

> [!success] The Method of Work Resolution
>
> The loop broke when the operator provided an explicit method:
>
> "we start in order and we do our ONLINE research right... recording the requirement and researching uppon them and synthenising after analysis and then investigation of our code and then suggestions of solution(s) with a recommended path."
>
> After this, production became coherent. Each step had a clear deliverable. No ambiguity about what "next" meant.

## Applicability

> [!abstract] When to Request an Explicit Method
>
> | Signal | Action |
> |--------|--------|
> | Operator says "follow the methodology" generically | Ask for or propose a specific numbered procedure |
> | You've cycled between research and production 2+ times | STOP and propose: "Here is my method of work for this task: 1... 2... 3..." |
> | Operator frustration is escalating | The ambiguity is the cause — resolve it with specificity, not effort |
> | Task is novel (no prior instance to follow) | The methodology model says WHAT stages to follow; the method of work says HOW to progress within them |

> [!warning] Self-Check — Am I In a Loop?
>
> 1. Have I alternated between research and production more than once this session?
> 2. Has the operator said both "research more" and "produce already" in different cycles?
> 3. Do I have a NUMBERED, SEQUENTIAL procedure I'm following, or just a stage label?
> 4. Could I tell someone exactly which step I'm on and what the next step is?

## Relationships

- DERIVED FROM: [[Model: Methodology]]
- DERIVED FROM: [[Never Skip Stages Even When Told to Continue]]
- RELATES TO: [[Always Plan Before Executing]]
- RELATES TO: [[Hardcoded Instances Fail — Build Frameworks Not Solutions]]
- RELATES TO: [[Execution Modes and End Conditions]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Model: Methodology]]
[[Never Skip Stages Even When Told to Continue]]
[[Always Plan Before Executing]]
[[Hardcoded Instances Fail — Build Frameworks Not Solutions]]
[[Execution Modes and End Conditions]]
[[Methodology Standards — What Good Execution Looks Like]]
