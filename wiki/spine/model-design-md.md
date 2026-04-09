---
title: "Model: Design.md and IaC"
type: concept
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: growing
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [model, spine, design-md, iac, markdown-config, claude-md, agents-md, soul-md, ai-configuration, infrastructure-as-code]
---

# Model: Design.md and IaC

## Summary

The Design.md and IaC model describes the convergence of Infrastructure as Code with AI agent configuration: markdown files placed at the project root serve as binding specifications that AI agents read and execute. This pattern generalizes from traditional IaC (Terraform, Ansible — human writes spec, machine executes it) into the AI agent domain, producing a companion file ecosystem: CLAUDE.md (agent behavioral constraints), DESIGN.md (visual design system), AGENTS.md (build and architecture instructions), and SOUL.md (agent identity). The 9-section DESIGN.md standard, documented in 58+ production implementations including Claude (Anthropic)'s own 312-line specification, represents the most complete instance of this pattern — a file that contains not just design decisions but a built-in usage manual for the AI agents consuming it.

## Key Insights

- **Markdown files at the project root are now IaC**: CLAUDE.md is not documentation — it is configuration. Claude Code reads it at session start as binding operational instructions. DESIGN.md is not a style guide — it is a constraint set that Gemini/Claude/Cursor reads before generating any UI. The executor might be Terraform, systemctl, or an LLM; the principle is identical: human writes specification, machine reads it as binding constraints.

- **The companion file ecosystem is complete at four files**: CLAUDE.md (how the agent should behave), DESIGN.md (how the UI should look), AGENTS.md (how to build the system), SOUL.md (who the agent is). Together they give any AI agent complete project context across behavioral, visual, architectural, and identity dimensions — without requiring a single bloated context-injection prompt.

- **Semantic color naming is an AI vocabulary design decision**: Every color in a production DESIGN.md gets a NAME (Parchment), a HEX (#f5f4ed), a ROLE (primary background), and RATIONALE ("warm cream with yellow-green tint that feels like aged paper"). The name becomes the agent's working vocabulary. When a prompt says "use Parchment" rather than "use #f5f4ed," the agent can honor the design intent even when the exact hex value changes — semantic naming survives refactors that literal values do not.

- **The Do's and Don'ts section is the guardrail layer**: Without explicit prohibitions, an AI agent generating UI reverts to training-data averages: gradients, bold serifs, cool grays, drop shadows. The Do's and Don'ts section (10 concrete rules each in production implementations) explicitly prohibits these defaults. This is the section that makes DESIGN.md a constraint file, not just a preference file.

- **Always-loaded files consume always-present context budget**: every token in CLAUDE.md and DESIGN.md costs context budget on every turn, not just when the agent uses them. The 40% degradation threshold for Claude Code accuracy means static config files collectively have a hard budget ceiling. The rule of thumb: keep always-loaded markdown under ~200 lines; put detailed workflows in skills loaded on demand.

- **58+ production implementations exist now**: the VoltAgent/awesome-design-md repository contains Design.md files for Claude (Anthropic), Stripe, Vercel, Linear, Figma, Spotify, Tesla, and dozens more. These are immediately usable as project templates. Any project wanting AI-generated consistent UI does not need to author a DESIGN.md from scratch.

## Deep Analysis

### The 9-Section DESIGN.md Standard

The standard structure, with what each section achieves, based on Claude (Anthropic)'s 312-line implementation:

**1. Visual Theme** — Atmospheric prose description of the design intent + 4-6 key characteristic adjectives. This section gives the AI a holistic "feel" for the design before it reads any specific values. It is the design philosophy translated into language the model can use as a prior.

**2. Color Palette** — Named colors with hex + functional role + design rationale. The structure matters: NAME → HEX → ROLE → WHY. The WHY column ("warm cream with yellow-green tint") is what separates DESIGN.md from a Figma tokens export. It captures reasoning, not just values.

**3. Typography** — 16-role hierarchy table. Entries: role name (Display, H1, H2, Body, Caption, etc.) → size → font family → weight → line-height → letter-spacing. The table format gives the AI a lookup structure it can reference mechanically rather than inferring from examples.

**4. Component Styles** — 5+ named button variants with exact padding, border-radius, shadow, and color values as CSS. This is the most specific section: exact implementation values, not design principles. An AI generating a button has no ambiguity about which CSS to produce.

**5. Layout Principles** — Spacing scale (8px base unit), grid system, whitespace philosophy, 7-level border-radius scale. These are the structural rules that govern how components relate to each other and to the page — the invisible constraints that make or break visual consistency.

**6. Depth & Elevation** — 5-level system from flat to inset, with shadow values at each level. This section makes explicit which interactions warrant visual weight and which should stay flat, preventing arbitrary shadow application.

**7. Do's and Don'ts** — 10 concrete rules each. This is the guardrail section. Claude's DESIGN.md prohibits: gradients in backgrounds, mixing font families, using literal hex values in prompts (use semantic names instead), and 7 others. Each Don't directly counteracts a specific AI tendency toward training-data average UI.

**8. Responsive Behavior** — 5 breakpoints with collapse strategy. At what viewport width does the nav collapse? When does the grid switch from 3-column to 2-column to 1-column? These answers cannot be inferred from the color palette; they require explicit specification.

**9. Agent Prompt Guide** — Ready-to-paste component prompts with exact values baked in + 7-rule iteration guide for how to use the file. This section is unique to DESIGN.md: no other design spec format (Figma tokens, Storybook, design tokens JSON) includes a built-in usage manual for AI. Claude's DESIGN.md includes 5 complete component prompts ("Create a hero section on Parchment (#f5f4ed) with a headline at 64px Anthropic Serif weight 500, line-height 1.10...") — the file teaches the AI how to use it.

Full depth and the 312-line Claude example: see [[Design.md Pattern]].

### The Do's and Don'ts Section as Constraint Engineering

The Do's and Don'ts section deserves special attention because it is the section that makes DESIGN.md a constraint file rather than a preference file.

Without explicit prohibitions, AI agents generating UI converge on training-data averages. These averages look like: subtle gradients on surfaces, bold serifs for headings, cool neutral grays for text, drop shadows on every elevated element, blue for all interactive elements. This is not wrong — it is generic. The AI is applying statistical consensus from millions of web pages, not the specific design language of this project.

The Do's section reinforces explicit choices. The Don'ts section prohibits the defaults that would otherwise fill in wherever the Do's leave gaps. Claude's DESIGN.md prohibits: gradients in backgrounds, mixing Anthropic Serif with system fonts in the same element, using literal hex values in prompts (use semantic names so the file remains the single source of truth), applying ring shadows where drop shadows were specified, using cool grays where warm grays are defined.

Each Don't is a documented failure mode — a specific visual decision the AI will make if left unconstrained. The Don'ts section is not pessimistic; it is precise. It identifies exactly the 10 ways the design system will be violated if the specification only says what to do and not what to avoid.

**Practical implication**: when authoring a new DESIGN.md, identify the 10 AI default decisions that would violate your design language and make them explicit Don'ts. This requires knowing how AI agents interpret visual design — an audit of AI-generated UI against a blank context is the fastest way to identify the relevant defaults.

### The Broader IaC Spectrum

The companion file ecosystem sits on a continuous spectrum of specification-driven configuration:

| Spec File | Executor | Domain |
|-----------|----------|--------|
| `main.tf` | Terraform | Cloud infrastructure |
| `docker-compose.yml` | Docker | Container orchestration |
| `CLAUDE.md` | Claude Code | AI agent behavior |
| `DESIGN.md` | Google Stitch / Claude / Cursor | Visual design system |
| `AGENTS.md` | Claude Code | Build and architecture conventions |
| `SOUL.md` | OpenFleet | Agent identity and values |
| `config/schema.yaml` | tools/validate.py | Wiki page schema |
| `stacks/*.yml` | Deployment scripts | Service deployment |
| `.env.example` | setup.py / developers | Environment configuration |
| `services/*.conf` | systemd | Daemon configuration |

The common pattern: a human writes a specification file at a standard location; an executor reads it as binding constraints. The executor's type (infrastructure tool, AI agent, validation script) does not change the pattern. This is why CLAUDE.md is IaC even though it is read by an LLM rather than by Terraform.

See [[Infrastructure as Code Patterns]] for full treatment of the spectrum and the ecosystem's specific IaC instances.

### The Two-Tier Configuration Model

AI agent configuration in this ecosystem uses a two-tier model that maps directly to the [[Context-Aware Tool Loading]] pattern:

**Tier 1 — Static context** (always-loaded, always-present budget consumption):
- `CLAUDE.md` — project-level agent behavioral constraints
- `DESIGN.md` — visual system constraints, loaded when UI generation is the primary task
- `config/schema.yaml` — page schema for validation

**Tier 2 — Dynamic context** (skills, loaded on invocation, zero overhead when not in use):
- `skills/evolve.md`, `skills/wiki-agent.md`, `skills/continue.md`
- Any detailed workflow that is only needed in specific session contexts

The implication: DESIGN.md loaded into every session has a real context cost, even when the session is not generating UI. The correct model is to load DESIGN.md only when the current session is UI-focused — either by keeping it as a separate skill invoked on demand, or by accepting the overhead as worthwhile for sessions where UI generation is the dominant task.

This wiki's `CLAUDE.md` (~250+ lines) is at the upper boundary of the recommended always-loaded size. See [[Claude Code Best Practices]] for the specific accuracy thresholds that govern this constraint.

### How the Companion Files Compose

The four companion files are designed to be read together, with non-overlapping scopes:

**CLAUDE.md** answers: "How should this AI agent behave in this project?" It covers commands to run, coding conventions, quality gates, prohibited actions, and the tools available. It is behavioral configuration — it shapes how the agent works, not what it builds.

**DESIGN.md** answers: "How should this project look?" It covers the visual system — colors, typography, spacing, component patterns, responsive behavior. It is visual configuration — it shapes the output of any UI-generating agent action.

**AGENTS.md** answers: "How should this project be built?" It covers architecture decisions, build conventions, module structure, dependency patterns. It is architectural configuration — it shapes how the agent structures its implementation work.

**SOUL.md** (OpenFleet-specific) answers: "Who is this agent?" It covers the agent's identity, values, expertise domain, decision-making principles, and relationship to the human. It is identity configuration — it shapes the agent's self-model and how it approaches its role.

The four files are separated by scope deliberately: no single file is responsible for behavioral AND visual AND architectural AND identity configuration. This keeps each file readable, maintainable, and at a size appropriate for always-loaded static context. An agent loading all four gains complete project context without any file being oversized.

The context budget implication: each file loads at session start. CLAUDE.md at ~200 lines + DESIGN.md at ~300 lines + AGENTS.md at ~100 lines + SOUL.md at ~150 lines = ~750 lines of always-present context overhead. Against a 190,000 token context window, this is ~4,000 tokens — less than 3% of the budget. The overhead is worthwhile for sessions that need all four.

### Why This Matters for the Ecosystem

The IaC pattern is how the ecosystem maintains coherence across five projects without centralized configuration management. Each project's configuration is self-contained in its root directory:

- OpenFleet's behavioral contract lives in `SOUL.md` templates and `HEARTBEAT.md` files — agent identity as IaC
- AICP's inference policy lives in profile YAML files — routing rules as IaC
- The wiki's quality gates live in `config/schema.yaml` — knowledge structure as IaC
- Each project's AI agent constraints live in its `CLAUDE.md` — session behavior as IaC

When a new engineer (or a new AI agent) needs to understand a project, they read the specification files. The specification files are the ground truth. No external knowledge, onboarding documentation, or tribal memory is required — the specification is the onboarding.

### The awesome-design-md Corpus

The VoltAgent/awesome-design-md repository contains 58+ Design.md files for production design systems: Claude (Anthropic), Stripe, Vercel, Linear, Figma, Spotify, Tesla, GitHub, and dozens more. Each file comes with `preview.html` and `preview-dark.html` for human verification. This corpus provides:

1. **Immediate templates**: drop a Design.md for a known design system into any project and AI agents can match that design system's UI without further configuration
2. **Pattern reference**: real production examples of all 9 sections with concrete values, not toy examples
3. **Coverage evidence**: 58 implementations demonstrates that the format generalizes across extremely different visual design languages

The corpus is at `https://github.com/VoltAgent/awesome-design-md` and is the authoritative source for Design.md section structure. Claude's 312-line implementation is the most complete example of the Agent Prompt Guide section.

## Open Questions

- At what point does the companion file ecosystem (CLAUDE.md + DESIGN.md + AGENTS.md + SOUL.md) tip from "useful configuration" into "context overhead that should be split into skills"? Is there a measurable accuracy threshold, or is the boundary project-specific?
- DESIGN.md is currently tool-agnostic (Google Stitch, Claude, Cursor all read it). As LLMs improve at visual design without explicit constraints, does the value of DESIGN.md decrease, or does the "design reasoning capture" value (WHY columns) remain durable even as constraint-following improves?
- Is there a DESIGN.md equivalent for interaction behavior (animations, state transitions, loading patterns) that the current 9-section structure does not capture?

## Relationships

- BUILDS ON: [[Design.md Pattern]]
- BUILDS ON: [[Infrastructure as Code Patterns]]
- BUILDS ON: [[Context-Aware Tool Loading]]
- RELATES TO: [[Model: SFIF and Architecture]]
- RELATES TO: [[Model: Quality and Failure Prevention]]
- RELATES TO: [[Model: Automation and Pipelines]]
- RELATES TO: [[Model: MCP and CLI Integration]]
- ENABLES: [[Claude Code Best Practices]]

## Backlinks

[[Design.md Pattern]]
[[Infrastructure as Code Patterns]]
[[Context-Aware Tool Loading]]
[[Model: SFIF and Architecture]]
[[Model: Quality and Failure Prevention]]
[[Model: Automation and Pipelines]]
[[Model: MCP and CLI Integration]]
[[Claude Code Best Practices]]
