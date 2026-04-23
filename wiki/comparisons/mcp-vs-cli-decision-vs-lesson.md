---
title: MCP vs CLI — Decision Artifact vs Lesson Artifact
aliases:
  - "MCP vs CLI — Decision Artifact vs Lesson Artifact"
  - "Decision vs Lesson — MCP vs CLI"
type: comparison
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: growing
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: decision-mcp-vs-cli
    type: wiki
    file: wiki/decisions/02_validated/tools/mcp-vs-cli-for-tool-integration.md
    description: "The decision artifact — actionable scenario matrix, alternatives, rationale, reversibility, dependencies"
  - id: lesson-cli-beats-mcp
    type: wiki
    file: wiki/lessons/03_validated/tools-architecture/cli-tools-beat-mcp-for-token-efficiency.md
    description: "The lesson artifact — context, insight, mechanism, evidence, applicability"
tags: [comparison, mcp, cli, skills, tool-integration, token-efficiency, decision, lesson, artifact-type, claude-code]
---

# MCP vs CLI — Decision Artifact vs Lesson Artifact

## Summary

Two wiki pages cover the MCP-vs-CLI-for-tool-integration topic: a **decision** (`Decision — MCP vs CLI for Tool Integration`) that tells you which pattern to pick for a given scenario, and a **lesson** (`CLI Tools Beat MCP for Token Efficiency`) that teaches why the tradeoff exists and when it applies. They are **consistent, not contradictory** — both derive from the same source triad (harness-engineering article, Claude Code accuracy tips, Playwright CLI vs MCP comparison) and converge on the same conclusion direction. The difference is reader intent: the decision answers "what do I DO?"; the lesson answers "what did we LEARN, and why does it hold?" Read the decision when choosing a pattern; read the lesson when teaching someone or validating whether the finding generalizes.

## Comparison Matrix

> [!abstract] Decision Artifact vs Lesson Artifact
>
> | Dimension | Decision — MCP vs CLI for Tool Integration | Lesson — CLI Tools Beat MCP for Token Efficiency |
> |-----------|--------------------------------------------|--------------------------------------------------|
> | **Artifact type** | decision | lesson |
> | **Layer** | 6 (decisions) | 4 (principles/lessons) |
> | **Primary reader intent** | Pick a pattern for a specific scenario | Understand a mechanism and when it applies |
> | **Core structure** | Decision + Alternatives + Rationale + Reversibility + Dependencies | Context + Insight + Evidence + Applicability |
> | **Headline device** | `> [!success]` scenario matrix | `> [!abstract]` loading-profile matrix |
> | **Scenario coverage** | 4 concrete scenarios → integration pattern | 4 domain applications + 4 "when MCP is still right" cases |
> | **Evidence weight** | Rationale section cites mechanisms + numbers | Dedicated Evidence section with 7 named sources |
> | **Mechanism depth** | Summarized (enough to justify the decision) | Foregrounded (the Insight is the mechanism) |
> | **Practitioner signal** | Referenced in rationale | First-class ("2026 practitioner consensus") |
> | **Reversibility treatment** | Full section — what changes if reversed | Implied — "when MCP is still right" |
> | **Dependencies explicit** | Yes — 6 downstream effects listed | Implied in Applicability section |
> | **Profile-aware** | Yes — SDLC profile context box | No |
> | **Self-check callout** | No | Yes — "Am I About to Make This Mistake?" (invariant self-check) |
> | **Source overlap with counterpart** | 3 of 4 derived_from entries shared | 3 of 4 derived_from entries shared |
> | **Maturity** | growing (validated decision tier) | growing (validated lesson tier) |
> | **When to update** | When a new scenario or reversal trigger surfaces | When new evidence or a new applicability domain surfaces |

## Key Insights

> [!abstract] The two pages are not duplicates — they are different artifact types with different jobs
>
> Both cover CLI-vs-MCP tool integration, but their role in the reader's workflow is distinct:
>
> 1. **Decision** = picking a pattern. Scenario matrix + alternatives considered + reversibility + downstream effects. You come here to COMMIT to a choice.
> 2. **Lesson** = teaching a finding. Context where it holds + mechanism explaining why + evidence + self-check for over-generalization. You come here to UNDERSTAND and to judge whether to apply.

> [!tip] They are mutually supporting, not redundant
>
> - The lesson validates that the decision's premise (CLI+Skills is cheaper + more accurate) is not one-off but a cross-source convergent finding with a clear mechanism (context-load timing).
> - The decision operationalizes the lesson by specifying which scenarios the finding applies to and what changes if the default shifts.
> - Removing either would weaken the other. Pure decision → unmotivated. Pure lesson → ungrounded in action.

> [!warning] Consistency holds today; watch for drift
>
> Both pages currently agree: CLI+Skills default for operational tooling, MCP for external services / discovery / exploratory testing. If one page gets updated with new evidence and the other is not, divergence creates a credibility problem. Operators reading just one page make choices the other page would contradict.
>
> Pragmatic check: both pages list "Future 1M context window" as a trigger to revisit. If a future session updates one artifact's revisit note, update the other.

> [!info] The scenario matrix (decision) and the loading-profile matrix (lesson) encode the same information differently
>
> - Decision's matrix = reader-first: "You want to do X → use pattern Y."
> - Lesson's matrix = mechanism-first: "Property Z differs between MCP and CLI in this way."
>
> Same four scenarios show up on both sides, but the decision page tells you what to do, the lesson page tells you why.

## Deep Analysis

### Decision — MCP vs CLI for Tool Integration

> [!tip] Read this when
> You're choosing an integration pattern for a new tool, evaluating whether to migrate an existing integration, or updating CLAUDE.md / skills to reflect a pattern preference.

**What it does well:**
- Scenario matrix maps concrete use cases (wiki pipeline, external services, cross-conversation discoverability, research workflows) to integration pattern
- Three alternatives explicitly considered (MCP-First, Skills-Only, CLI-Only) and each rejection is reasoned
- Reversibility section names the exact migration path both ways — no orphaned concerns
- Dependencies section lists 6 downstream effects (CLAUDE.md conventions, MCP server scope, skill design, subagent patterns, Context7, future 1M window)
- Profile-aware: SDLC callout says "simplified chain: CLI-only" vs "full chain: MCP more attractive at fleet scale"

**Weaknesses:**
- Rationale references the mechanism (context-load timing) but doesn't foreground it — reader who wants "why" has to dig into paragraphs
- Evidence is scattered throughout Rationale rather than centralized
- No self-check callout — a reader could over-apply the default to scenarios where MCP legitimately wins

**Ideal use:** operator making an integration-pattern choice, CLAUDE.md author, decision-record audit.

### Lesson — CLI Tools Beat MCP for Token Efficiency

> [!tip] Read this when
> You're teaching someone the tradeoff, validating the generalization in a new domain, writing a comparison or a model that cites this finding, or debugging a hallucination pattern that might trace to schema bloat.

**What it does well:**
- Insight is foregrounded: one warning callout states the mechanism, one abstract callout shows the loading profile
- Evidence section has 7 named sources with mechanism-level detail (Playwright injects 10 accessibility trees vs 2-3 YAML snapshots; Microsoft endorses CLI; Google Trends shows CLI overtaking MCP; Claude Code extension comparison table corroborates)
- Applicability names four specific downstream contexts (AI agent design, research wiki architecture, OpenFleet agent design, AICP and devops-control-plane)
- Self-check callout ("Am I About to Make This Mistake?") prompts readers to test their own context before applying
- Distinguishes "when MCP is still right" with four concrete cases

**Weaknesses:**
- Title is absolute ("CLI Tools BEAT MCP") but body qualifies heavily with "when MCP is still right" — title may mislead skimmers
- No reversibility analog — what signals would flip the finding?
- Less profile-aware than the decision — doesn't explicitly address how the tradeoff shifts at different scales

**Ideal use:** teaching material, knowledge-graph nodes cited by other lessons/patterns, self-audit against over-generalization.

## Recommendation

> [!success] Which to read depends on what you're doing right now
>
> | Your task | Read |
> |-----------|------|
> | **Picking an integration pattern for a specific tool** | **Decision** — the scenario matrix answers your question directly |
> | **Teaching someone why CLI default is the right call** | **Lesson** — foregrounds the mechanism and practitioner consensus |
> | **Reviewing whether an existing MCP integration is worth its cost** | **Both** — decision's dependencies list the change scope, lesson's applicability validates whether your case still fits |
> | **Writing a new comparison or model citing this finding** | **Lesson** — it's the knowledge-graph anchor; the decision is downstream |
> | **Auditing: is our MCP-vs-CLI policy consistent across projects?** | **Decision** (primary) + **Lesson** (secondary) — decision is the policy surface, lesson is the evidence anchor |

> [!tip] Maintenance rule
> These pages share 3 of 4 derived_from entries. When one is revised based on new evidence from a shared source, audit the other for consistency before closing the update. They are a tightly-coupled pair.

## Relationships

- COMPARES TO: [[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
- COMPARES TO: [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
- BUILDS ON: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]
- RELATES TO: [[mcp-integration-architecture|MCP Integration Architecture]]
- RELATES TO: [[context-aware-tool-loading|Context-Aware Tool Loading]]
- RELATES TO: [[skills-as-primary-extension-pattern|Decision — Skills as the Primary Extension Pattern]]

## Backlinks

[[mcp-vs-cli-for-tool-integration|Decision — MCP vs CLI for Tool Integration]]
[[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[mcp-integration-architecture|MCP Integration Architecture]]
[[context-aware-tool-loading|Context-Aware Tool Loading]]
[[Decision — Skills as the Primary Extension Pattern]]
