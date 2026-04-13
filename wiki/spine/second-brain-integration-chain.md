---
title: Operations Plan — Second Brain Integration Chain — Complete Walkthrough
aliases:
  - "Operations Plan — Second Brain Integration Chain — Complete Walkthrough"
  - "Operations Plan: Second Brain Integration Chain — Complete Walkthrough"
type: operations-plan
domain: cross-domain
layer: spine
status: synthesized
confidence: high
maturity: seed
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: requirements
    type: file
    file: wiki/domains/cross-domain/second-brain-integration-requirements.md
tags: [operations-plan, integration, chain, second-brain, walkthrough]
---

# Operations Plan — Second Brain Integration Chain — Complete Walkthrough
## Summary

Complete step-by-step chain for integrating ANY project with the second brain. Covers: discovery → identity → chain selection → methodology adoption → standards integration → template usage → work loop → feedback. Each step has a command, expected output, and validation. A project following this chain goes from "I know nothing about the second brain" to "I'm fully integrated and feeding knowledge back."

## Prerequisites

- [ ] Second brain repo accessible (local clone or network path)
- [ ] Python 3.8+ with yaml module available
- [ ] The project has a CLAUDE.md (or willingness to create one)

## Steps

### PHASE 1: DISCOVERY — "What is this and what do I need?"

### Step 1: First Contact

- **Action:** Run the gateway with no arguments
- **Command:** `python3 -m tools.gateway`
- **Expected output:** Guided entry showing common paths per user type
- **Validation:** You see "Start here:" with actionable options
- **If from another project:** `python3 -m tools.gateway --wiki-root ~/devops-solutions-research-wiki`

### Step 2: Auto-Detect Identity

- **Action:** Let the gateway analyze your project
- **Command:** `python3 -m tools.gateway what-do-i-need`
- **Expected output:** Detected identity (domain, scale, phase) + recommended chain + first steps
- **Validation:** Domain and scale match your project. Execution mode says "unknown — declare" (correct — the gateway can't know your runtime mode).
- **Note:** The gateway auto-detects what it CAN (domain from package.json, scale from file count) and honestly says "unknown" for what it CAN'T (execution mode, PM level, trust tier — these are runtime/operational properties, not filesystem properties).

### Step 3: Browse the Knowledge Tree

- **Action:** See the full structure of what's available
- **Command:** `python3 -m tools.gateway navigate`
- **Expected output:** Tree showing: Identity → SDLC Chains → Methodology Models → Stages → Enforcement → Principles → Tracking → Hierarchy → PM Levels → Tools
- **Validation:** Every branch shows a command to drill deeper

---

### PHASE 2: IDENTITY — "Who am I and what's right for me?"

### Step 4: Declare Your Identity Profile

- **Action:** Add identity profile to your CLAUDE.md
- **Template:**
```yaml
## Identity Profile (Goldilocks)

| Dimension | Value |
|-----------|-------|
| **Type** | {{system / project / library}} |
| **Execution Mode** | {{solo / harness v1 / harness v2 / harness v3 / full system}} |
| **Domain** | {{typescript / python / infrastructure / knowledge}} |
| **Phase** | {{poc / mvp / staging / production}} |
| **Scale** | {{micro / small / medium / large / massive}} |
| **PM Level** | {{L1 / L2 / L3}} |
| **Trust Tier** | {{operator-supervised / trainee / standard / expert}} |
| **SDLC Chain** | {{simplified / default / full}} |
| **Second Brain** | {{self / connected / none}} |
```
- **Validation:** `python3 -m tools.gateway query --identity` shows your declared profile
- **Guidance:** See [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] for what each dimension means and how to choose

### Step 5: Select Your SDLC Chain

- **Action:** Review chains and pick the right one
- **Command:** `python3 -m tools.gateway query --chains` then `python3 -m tools.gateway query --chain default`
- **Expected output:** Chain details: stages, models, readiness gate, enforcement level, upgrade triggers
- **Validation:** Your declared chain in CLAUDE.md matches your phase × scale
- **Decision guide:**
  - POC + micro/small → simplified
  - MVP→Staging + small→medium → default (most projects)
  - Production + medium→massive → full

---

### PHASE 3: METHODOLOGY — "How does work proceed?"

### Step 6: Understand Your Methodology Models

- **Action:** See what models are available for your chain
- **Command:** `python3 -m tools.gateway query --models`
- **Expected output:** List of models with stage sequences
- **Validation:** Your chain's models are a subset of the full 9 (simplified has 4, default has 8, full has 9)

### Step 7: Learn the Stages for Your Task Type

- **Action:** Query stage requirements for a specific task
- **Command:** `python3 -m tools.gateway query --model feature-development --full-chain`
- **Expected output:** Full artifact chain: document → design → scaffold → implement → test with required/forbidden artifacts per stage
- **Validation:** Each stage shows: required artifacts, templates to use, forbidden outputs

### Step 8: Get Stage Details for Your Domain

- **Action:** Query domain-specific stage requirements
- **Command:** `python3 -m tools.gateway query --stage document --domain typescript`
- **Expected output:** Stage rules + domain overrides (forbidden zones, path patterns, gate commands)
- **Validation:** Domain overrides match your project's tech stack

---

### PHASE 4: STANDARDS — "What does 'good' look like?"

### Step 9: Review Quality Standards for Your Page Types

- **Action:** Read the per-type standards for the pages you'll produce
- **Wiki pages:** `wiki/spine/standards/{type}-page-standards.md` (15 types)
- **Validation:** Each standards page has: required sections, content thresholds, exemplar reference, common failures

### Step 10: Get Templates

- **Action:** Get the template for the artifact you need to produce
- **Command:** `python3 -m tools.gateway template lesson` (or: concept, pattern, decision, epic, methodology/requirements-spec, etc.)
- **Expected output:** Full template with inline guidance callouts
- **Validation:** Template has sections matching the standards page

### Step 11: Review Frontmatter Fields

- **Action:** Understand what fields your pages need
- **Command:** `python3 -m tools.gateway query --field readiness` (or: type, status, maturity, impediment_type, etc.)
- **Expected output:** Field definition with: required?, valid values, what automation reads it
- **Validation:** Your frontmatter matches the schema
- **Full reference:** [[frontmatter-field-reference|Frontmatter Field Reference — Complete Parameter Documentation]]

---

### PHASE 5: WORK LOOP — "How do I execute?"

### Step 12: Follow the Stage Sequence

- **For each task:**
  1. Select model based on task type: `gateway query --model <type>`
  2. Follow stages in order: document → design → scaffold → implement → test
  3. At each stage, produce the required artifacts (query the chain for what's needed)
  4. Validate: `pipeline post` (or project-specific gate commands)
  5. Do NOT advance until the current stage's artifacts exist and pass validation

### Step 13: Track Readiness and Progress

- **Readiness** (definition completeness): advances through document/design stages
- **Progress** (execution completeness): advances through scaffold/implement/test stages
- Both are 0-100. Both flow upward in the hierarchy (task → module → epic → milestone).
- 99→100 = human review only. Always.

### Step 14: Handle Impediments

- If blocked: set `impediment_type` in frontmatter (technical, dependency, decision, environment, clarification, scope, external, quality)
- Each type has a different response — see [[backlog-hierarchy-rules|Backlog Hierarchy Rules]]

---

### PHASE 6: FEEDBACK — "How do I contribute back?"

### Step 15: Contribute Learnings

- **Action:** When you learn something the second brain doesn't know
- **Command:** `python3 -m tools.gateway contribute --type lesson --title "What I Learned" --content "Description of the learning"`
- **Expected output:** New lesson created in wiki/lessons/00_inbox/
- **Validation:** `pipeline post` passes, lesson appears in inbox

### Step 16: Scan Your Project for the Brain

- **Action:** Feed your project's operational knowledge back
- **Command:** `python3 -m tools.pipeline scan ../your-project/`
- **Expected output:** Key files copied to raw/ for ingestion
- **Validation:** Raw files appear in raw/articles/

---

### PHASE 7: LOCAL vs REMOTE MODE

### Step 17: Choose Your Mode

| Mode | When | How |
|------|------|-----|
| **Local** | Second brain is cloned next to your project | `python3 -m tools.gateway` (auto-detects) |
| **Remote via --wiki-root** | Second brain is elsewhere on the filesystem | `python3 -m tools.gateway --wiki-root /path/to/brain` |
| **Remote via MCP** | Second brain runs as MCP server | Use MCP tools (wiki_status, wiki_search, wiki_read_page) |
| **Self** | You ARE the second brain | `python3 -m tools.gateway` (auto-detects: second_brain=self) |

The gateway auto-detects the second brain location. If it can't find it, it falls back to local wiki. Override with `--brain /path/to/brain`.

## Rollback

Each step is independent. To undo:
- Remove the Identity Profile from CLAUDE.md (Step 4)
- Delete any created pages (Step 15)
- No other steps modify your project

## Completion Criteria

- [ ] Identity profile declared in CLAUDE.md
- [ ] SDLC chain selected and understood
- [ ] At least one task completed following the stage sequence
- [ ] At least one contribution back to the second brain
- [ ] `gateway what-do-i-need` shows your declared identity (not "unknown")

## Relationships

- IMPLEMENTS: [[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
- BUILDS ON: [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
- BUILDS ON: [[methodology-adoption-guide|Methodology Adoption Guide]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
- RELATES TO: [[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]

## Backlinks

[[second-brain-integration-requirements|Second Brain Integration System — Full Chain Requirements]]
[[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[model-methodology|Model — Methodology]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[wiki-gateway-tools-unified-knowledge-interface|Wiki Gateway Tools — Unified Knowledge Interface]]
[[e016-integration-chain-proof-end-to-end-with-openarms|E016 — Integration Chain Proof — End to End with OpenArms]]
[[goldilocks-flow|Goldilocks Flow — From Identity to Action]]
