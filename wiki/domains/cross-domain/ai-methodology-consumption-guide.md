---
title: "How AI Agents Consume the Methodology Wiki"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: methodology-model
    type: wiki
    file: wiki/spine/model-methodology.md
  - id: adoption-guide
    type: wiki
    file: wiki/spine/methodology-adoption-guide.md
  - id: agent-artifacts
    type: wiki
    file: wiki/domains/cross-domain/ai-agent-artifacts.md
  - id: claude-md-patterns
    type: wiki
    file: wiki/patterns/claude-md-structural-patterns.md
tags: [ai-agents, methodology, consumption, integration, second-brain, guide]
---

# How AI Agents Consume the Methodology Wiki

## Summary

This page bridges the gap between the methodology wiki as KNOWLEDGE and the methodology wiki as OPERATIONAL GUIDANCE for AI agents. The wiki contains 237+ pages of methodology knowledge — but an AI agent doesn't read the whole wiki. It enters through specific paths, reads specific pages, and needs to translate what it reads into specific actions. This guide defines those paths, explains what agents should extract from each page type, and shows how the second brain becomes an active thinking partner rather than a passive reference.

## Key Insights

1. **AI agents enter the wiki through 4 different paths — not just CLAUDE.md.** Direct access (reading wiki pages during a conversation), CLAUDE.md reference (their project's CLAUDE.md points to wiki pages), MCP tools (wiki_search, wiki_read_page), and export bundles (methodology.yaml + domain profiles imported into the project). Each path gives different depth.

2. **The wiki is a THINKING PARTNER, not a reference manual.** A reference manual is consulted when you have a specific question. A thinking partner is consulted BEFORE you form the question — it shapes how you think about the problem. An AI that reads the artifact taxonomy BEFORE deciding what to produce will make different (better) choices than one that decides first and checks after.

3. **Every methodology page should answer: "What does the AI reading this DO differently?"** A page about stage gates that says "stages exist" teaches nothing. A page that says "BEFORE you write any code, check: are you in scaffold or implement stage? If scaffold, your code MUST NOT have function bodies > 3 lines" — that changes behavior.

4. **The three consumption modes: LEARN, DECIDE, EXECUTE.** Sometimes the AI needs to LEARN a concept (read the model page). Sometimes it needs to DECIDE which model/type/template to use (read the selection tables). Sometimes it needs to EXECUTE a specific stage (read the domain chain for concrete artifacts). Different pages serve different modes.

## Deep Analysis

### The 4 Entry Paths

> [!abstract] How AI Agents Access the Wiki
>
> | Path | How It Works | Depth | When Used |
> |------|-------------|-------|-----------|
> | **Direct read** | Agent reads wiki pages during conversation (Read tool, view tool) | Full page content | Working ON the wiki project |
> | **CLAUDE.md reference** | Project's CLAUDE.md references wiki pages/configs for methodology rules | Summarized in CLAUDE.md, full if agent reads linked pages | ANY project using the methodology |
> | **MCP tools** | wiki_search, wiki_read_page, wiki_status, wiki_gaps | Structured access via tools | Cross-project knowledge queries |
> | **Export bundle** | methodology.yaml + artifact-types.yaml + domain-profiles + key wiki pages | Config files + selected pages | Project bootstrapping |
>
> **The richest path is direct read.** An agent with the wiki as its working directory has the full 237+ pages available. The thinnest path is export bundle — only configs and selected pages.

### What Agents Should Extract from Each Page Type

> [!info] Page Type → What the AI Does With It
>
> | Page Type | Consumption Mode | What to Extract | Action After Reading |
> |-----------|-----------------|-----------------|---------------------|
> | **Model page** (model-methodology.md) | LEARN | Which models exist, when to use each, stage sequences, ALLOWED/FORBIDDEN per stage | Select the right model for the current task |
> | **Standards page** (model-methodology-standards.md) | LEARN + DECIDE | Gold standards, anti-patterns, checklists | Compare your work against the gold standard BEFORE declaring done |
> | **Per-type standards** (spine/standards/*.md) | EXECUTE | Section-by-section quality bar, exemplar, common failures | Follow the quality bar while writing each section of a page |
> | **Artifact taxonomy** | DECIDE | 78 types, 3 classes, 11 categories | Identify which artifacts you need to produce at this stage |
> | **Domain chain** | EXECUTE | Concrete file paths, gate commands, ALLOWED/FORBIDDEN code | Know EXACTLY what files to create and what validation to run |
> | **Lesson page** | LEARN | Mechanism (WHY), evidence, applicability | Avoid the failure pattern described — apply the insight to current work |
> | **Pattern page** | DECIDE | When to apply, when NOT to, instances | Recognize if the current situation matches — apply or avoid |
> | **Decision page** | EXECUTE | The decision, alternatives rejected, rationale | Follow the decision — don't re-decide what's already decided |
> | **Comparison page** | DECIDE | Matrix, recommendation | Use the matrix to select between alternatives |
> | **Operations plan** | EXECUTE | Sequential steps with validation | Follow steps mechanically — this is a deterministic checklist |

### The Three Consumption Modes

#### LEARN Mode — Building Understanding

> [!tip] When the AI needs to UNDERSTAND a concept before working
>
> **Pages to read:** Model pages, framework page, lesson pages
>
> **What the AI does:**
> 1. Read the page's Key Insights FIRST — they're designed to stand alone
> 2. If Key Insights are enough for the current task, stop reading
> 3. If more depth needed, read Deep Analysis subsections relevant to the task
> 4. Check Open Questions — are any relevant to what you're about to do?
> 5. Follow Relationships to connected pages if the concept has dependencies
>
> **What the AI should NOT do:**
> - Read the entire 600-line model page when only one subsection is relevant
> - Skip Key Insights and dive into Deep Analysis (Key Insights are the summary)
> - Ignore Open Questions (they flag known gaps — your task might hit one)

#### DECIDE Mode — Making a Choice

> [!tip] When the AI needs to SELECT between options
>
> **Pages to read:** Artifact taxonomy, comparison pages, decision pages, model selection tables
>
> **The decision tree for "what model should I use?":**
> 1. What is the task_type? (epic, module, task, bug, spike, docs, refactor, hotfix, integration, evolve)
> 2. Look up the model in the Model Selection table (CLAUDE.md or methodology.yaml)
> 3. Check the model's stage sequence — which stages apply?
> 4. For each stage, check the domain chain — what SPECIFIC artifacts do I produce?
>
> **The decision tree for "what artifact type should I produce?":**
> 1. What stage am I in? (document, design, scaffold, implement, test)
> 2. What class of output? (document = constraining, artifact = by-product, documentation = explaining)
> 3. Check the artifact taxonomy for the specific type
> 4. Check the per-type standards for quality bar
> 5. Check if there's a template: `wiki/config/templates/` or `wiki/config/templates/methodology/`

#### EXECUTE Mode — Producing Output

> [!tip] When the AI is DOING the work — writing pages, producing artifacts
>
> **Pages to read:** Per-type standards, domain chain, operations plans
>
> **The execution checklist (every artifact, every time):**
> 1. Which type am I creating? → Read its standards page in `wiki/spine/standards/`
> 2. Which template? → Scaffold from `wiki/config/templates/`
> 3. Section by section: does my content meet the quality bar from the standards page?
> 4. Does the gold-standard exemplar referenced in the standards page LOOK like what I'm producing?
> 5. Am I in the right stage for this artifact? (check ALLOWED/FORBIDDEN)
> 6. Run gate command: `pipeline post` for wiki, domain-specific for code/infra
> 7. 0 errors = done. Errors = fix before proceeding.

### How the Second Brain Becomes Active (Not Passive)

> [!warning] The difference between passive reference and active thinking partner
>
> **PASSIVE (what most AI agents do):**
> - Receive task from user
> - Start working immediately based on training knowledge
> - Consult wiki ONLY when stuck or explicitly asked
> - Produce output that may or may not match methodology
>
> **ACTIVE (what this methodology demands):**
> - Receive task from user
> - BEFORE working: check methodology model, artifact chain, domain profile
> - BEFORE each artifact: check per-type standards, review exemplar
> - DURING work: search wiki for relevant lessons, patterns, decisions
> - AFTER work: verify against gate commands, check if work revealed new knowledge to feed back
>
> The shift is: **consult BEFORE acting, not after failing.** The wiki has answers to questions the agent hasn't thought to ask yet. An agent that reads the "Coverage Blindness" lesson BEFORE building a type system would know to research the full taxonomy first. An agent that reads it AFTER being corrected has already wasted effort.

### Cross-Project Consumption

When an AI agent in OpenArms, OpenFleet, or AICP needs methodology guidance:

> [!abstract] External AI Agent Consumption Path
>
> 1. **Their CLAUDE.md** references methodology configs (methodology.yaml, domain-profile)
> 2. **Their stage skills** inject per-stage rules from their methodology.yaml
> 3. **When they need deeper understanding:** They can access the wiki via:
>    - MCP tools (if wiki MCP server is running)
>    - Direct file read (if wiki is a sibling directory)
>    - Exported knowledge pages (if methodology bundle was exported)
> 4. **What they should read:** The domain chain for their stack + the model page + relevant standards
>
> The wiki is the AUTHORITATIVE source. The project's CLAUDE.md is a CONFIGURED REFERENCE to the wiki. When methodology evolves in the wiki, projects update their references. See [[Methodology Evolution Protocol]] for how this propagation works.

### What's Missing for Full AI Consumption

> [!warning] Gaps that prevent AI agents from fully leveraging the second brain
>
> | Gap | Impact | Fix |
> |-----|--------|-----|
> | **No "AI quick start" at the top of key pages** | Agent reads 600 lines when it needs 10 lines of guidance | Add `> [!tip] AI Quick Start` callouts at the top of model/standards pages |
> | **Pages optimized for human reading, not AI scanning** | Agents skip to the section they need but section names don't always signal their content to an AI | More descriptive section headers, action-oriented |
> | **No decision trees IN the pages** | Agent reads description of types but must construct its own decision process | Embed "if X then Y" decision trees, especially in taxonomy and model selection |
> | **Lessons don't link to prevention** | An agent reads a lesson about a failure but doesn't know how to CHECK if it's about to make the same mistake | Add "Self-check" section to lessons: "Ask yourself: am I about to..." |
> | **Export bundle doesn't include key wiki pages** | External agents only get configs, not the understanding pages | Expand export to include: model page, standards page, taxonomy, domain chain, top 5 lessons |

## Open Questions

> [!question] Should key methodology pages have a standardized "AI Quick Start" callout block at the top? (5-10 lines telling the AI: what this page is for, when to read it, what to do after reading it)

> [!question] Should the MCP server expose a "methodology guide" tool that returns the right pages based on what the agent is about to do? (e.g., `wiki_methodology_guide --task-type bug --stage document` returns the relevant chain + standards + lessons)

## Relationships

- BUILDS ON: [[Model: Methodology]]
- BUILDS ON: [[Methodology Adoption Guide]]
- BUILDS ON: [[CLAUDE.md Structural Patterns for Agent Compliance]]
- BUILDS ON: [[AI Agent Artifacts — Standards and Guide]]
- RELATES TO: [[Methodology System Map]]
- RELATES TO: [[Methodology Config Architecture — How the Pieces Fit Together]]
- FEEDS INTO: [[Model: Claude Code]]
- FEEDS INTO: [[Methodology Standards — What Good Execution Looks Like]]

## Backlinks

[[Model: Methodology]]
[[Methodology Adoption Guide]]
[[CLAUDE.md Structural Patterns for Agent Compliance]]
[[AI Agent Artifacts — Standards and Guide]]
[[Methodology System Map]]
[[Methodology Config Architecture — How the Pieces Fit Together]]
[[Model: Claude Code]]
[[Methodology Standards — What Good Execution Looks Like]]
