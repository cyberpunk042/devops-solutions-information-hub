# Directive: Methodology Standards & Agent Compliance Framework
Date: 2026-04-11

## User Directive (verbatim)

"we need to establish a strong method of work with the Wiki LLM structure and Methodology structure and execution and we need to establish standards for everything with example of document on top of the standards documents for each artifact type."

"This way not agent must always meet a model and we can even automatic / validate that the structure and a minimum is meet at least."

"I have the proper that agent are working with the methodlogy and they dont work well, the AI keep ignoring in certain cases even completely the directives given from the methodlogy but its mostly do to comfusion and broadness vs generic and order of thigs and start and ending and format used"

"There are ways of work and even kindda magic tricks that strangely serve a purpose like properly deviding content or imbricating."

"What is certain is that in a fleet or in solo. it requires a fine-tuning to have an agent really fuly use the methodology and the skills and tools . the more compact the harder but also when too large naturally can lead to confusion in some if not many cases."

"There is also a difference between operation / operations plan and design plan.. where the operations its basically jsut a todo list... that could at the very least be a dumber agent maybe, done on the fly in process or clearly state that this highly broken down tiny piece has to be executed exatly like this, like clear todo of sequential operations and validation."

"A real plan in methodlogy is not brainless robotic operations.. its much more complex than this..."

"We need to properly define that. And we need to do it for each documents."

"Ones you dont even know yet. I dont even know if you have the full chain of artifacts or documents."

"If you look there for example you will see some evolution, its not perfect but its a start, you see that through it we define stages per cases with consitions and those have requireds documents and eveything is structured: /home/jfortin/openarms/wiki/config/methodology.yaml"

"(We need to re-use this but do the best solution, clearly this one was a first draft and its full of random or hardcoded specific stuff... we want better....)"

"Its important how we configure the claude file to use the second brain when its present on the machine and how we shape it into adhering to methodologies of work instead of rush or waterfall or mockup mode.."

"We need to think of everything and we need ourself to make clear first all those high standards and examples"

## Key Themes

1. **Agent compliance problem**: Agents ignore methodology — caused by confusion, broadness, ordering, format
2. **Standards + exemplars**: Every artifact type needs a standards doc AND an example doc
3. **Validation**: Automated/structural minimum enforcement
4. **Operations vs Design plans**: Two fundamentally different things, currently conflated
5. **Full artifact chain**: Not yet fully mapped — need complete inventory
6. **CLAUDE.md as control surface**: How to configure agents to USE the second brain
7. **Compact vs verbose tradeoff**: Too compact = hard, too large = confusion — need the sweet spot
8. **"Magic tricks"**: Structural techniques (dividers, nesting, ordering) that improve agent compliance
9. **Cross-ecosystem**: Must work for fleet agents, solo agents, any project consuming the wiki

## Clarifications (verbatim, 2026-04-11 brainstorm)

Q1 (Scope): "BOTH.. REMEMBER WE ARE THE SECOND BRAIN.. NOT ONLY WILL WE SHOW THE WAY, WE WIL SHOW HOW TO HARNESS IT AND HOW TO INFORCE IT AT THE MULTIPLE LEVEL AND VALIDATE AND CHOSE THE GRANULARITY, WE WILL DEFINE EVERYTHING...."

Q2 (Artifact chain): "What you are missing its that its dynamic and that sometimes thsoe are generic and sometimes those are speficics, you are missing that you flattened them as if they where not multiple artifacts or documents required by stages, you ommited the order and dependencies, you wrote this as if it was the final product when I clearly said it was a mediocre example... we will create the information and the access to it and everything revolving around it. (Like what if I am in domain X or Z or B an whatnot... you have to think of this.) We are talking multiple EPICs here."

Q3 (Compliance): "I never said it was not working, I said it was a work in progress and there are failure and we are here to help and solve all the problems before fleet and openarms have to solved them individually. What I mean is that we will have to lean seriously on it and discuss and analyse and research and do it right.... and make it clear."

Q4 (Magic tricks): "That would break you right now..."

## Epic Structure (approved 2026-04-11)

Four epics confirmed. All four get full effort — no compression.

- **Epic A: Artifact Type System** — Define every document/artifact type with: definition, template, exemplar, validation rules. Handle the generic-vs-specific dimension. Map the full chain per methodology model.
- **Epic B: Portable Methodology Engine** — A generic methodology.yaml the wiki produces and projects consume. Not hardcoded to any tech stack. Includes model definitions, stage specs, artifact chains, enforcement patterns.
- **Epic C: Agent Compliance Framework** — CLAUDE.md structural patterns, enforcement hooks, validation tooling, skill injection. The "how to make agents actually follow this."
- **Epic D: Standards-by-Example** — Every standard we define must ship with a gold-standard exemplar that passes its own rules. The wiki eats its own cooking.

User directive (verbatim): "Absolutely all 4 of them and with the most effort and complexity point. do we give them their appropriate room in our level of effort."

## Corrections to My Understanding

1. I FLATTENED the artifact chain — artifacts are stage-ordered, have dependencies, vary by domain/context, and have multiplicity per stage. Not a flat list.
2. I treated the openarms methodology.yaml as the answer — it's a first draft, mediocre. We need better.
3. I framed compliance as broken — it's a work-in-progress. The wiki's job is to solve it HERE so projects don't solve individually.
4. This is MULTIPLE EPICS, not a single task.
5. The wiki is the LABORATORY — prove methodology here, then projects consume it.
6. The "magic tricks" of formatting are real but too complex to explain cold — they emerge from practice.
