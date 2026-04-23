---
title: Model — Ecosystem Architecture vs Four-Project Ecosystem
aliases:
  - "Model — Ecosystem Architecture vs Four-Project Ecosystem"
  - "Ecosystem Model vs Instance"
type: comparison
domain: cross-domain
layer: 5
status: synthesized
confidence: high
maturity: growing
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: model-ecosystem
    type: wiki
    file: wiki/spine/models/ecosystem/model-ecosystem.md
    description: "The generalized ecosystem model — patterns, topologies, and universal invariants for any multi-project system"
  - id: four-project-ecosystem
    type: wiki
    file: wiki/domains/devops/four-project-ecosystem.md
    description: "The concrete instance — project-by-project tables, repos, integration diagram, and ecosystem-specific details"
tags: [comparison, ecosystem, model, openfleet, aicp, openarms, devops-control-plane, multi-project, integration, spine, architecture]
---

# Model — Ecosystem Architecture vs Four-Project Ecosystem

## Summary

Both pages describe the same 5-project ecosystem, but they serve different reader intents. `Model — Ecosystem Architecture` is the **generalized theory** (hub-and-spoke / peer-to-peer / federated topologies, universal invariants that hold at any scale); `Four-Project Ecosystem` is the **concrete instance** (repos, integration points, ASCII integration diagram, current project states). The model teaches how to design any multi-project system; the instance documents what this specific system actually is. Read the instance first if you're working inside THIS ecosystem, the model first if you're adopting ecosystem patterns elsewhere.

## Comparison Matrix

> [!abstract] Model vs Instance Comparison
>
> | Dimension | Model — Ecosystem Architecture | Four-Project Ecosystem |
> |-----------|-------------------------------|------------------------|
> | **Page type** | concept (spine/models/) | concept (domains/devops/) |
> | **Layer** | spine (universal) | 2 (project-level) |
> | **Abstraction level** | Generalized patterns + one instance section | Single specific instance |
> | **Primary reader question** | "How do ecosystems work?" | "What does our ecosystem look like?" |
> | **Topology coverage** | Hub-and-spoke, peer-to-peer, federated | Hub-and-spoke (this ecosystem's choice) |
> | **Scale guidance** | 2 → 3-5 → 5-10 → 10+ project tiers | Five specific projects |
> | **Project enumeration** | Yes (in "Instance — Our Ecosystem" section) | Yes (per-project attribute tables) |
> | **Integration diagram** | Integration map table (textual) | ASCII block diagram + table |
> | **Invariants section** | Yes — five universal invariants | No — implied by instance structure |
> | **Adoption guide** | Yes — "How to Adopt" for replicating the pattern | No — describes existing state |
> | **State of knowledge** | Per-ecosystem dimension (well-covered, thin) | Per-project attributes |
> | **PM-level mapping** | Generic L1-L3 tiers | This ecosystem's specific per-project PM levels |
> | **Backlink count** | 36 | 37 |
> | **Primary audience** | Ecosystem designers (including future adopters) | Current ecosystem operators/agents |
> | **When to update** | When a new ecosystem pattern is validated anywhere | When a specific project's role/integration changes |

## Key Insights

> [!abstract] The Matrix Reveals a Model/Instance Split
>
> The two pages encode the same subject at different abstraction levels — not duplication, but complementary layers. This is the **model/instance pattern** applied to ecosystem architecture itself:
>
> 1. **Model** = the theory. Names the topologies, states the invariants, gives the adoption recipe. Portable across ecosystems.
> 2. **Instance** = the data. Names the projects, their repos, their integration points, their current state. Specific to this ecosystem.

> [!tip] The split prevents two failure modes
>
> - **Model without instance**: abstract but useless. Nobody can see what "hub-and-spoke ecosystem" looks like concretely.
> - **Instance without model**: specific but unportable. A new ecosystem has to re-derive the topology choices from scratch.
>
> Keeping both — with backlinks between them — lets a reader drill from theory to concrete, or generalize from concrete to theory, as needed.

> [!warning] Overlap is real — roughly 30% content duplication in project descriptions
>
> The "Instance — Our Ecosystem" section of the model and the "Project-by-Project Breakdown" of the instance cover similar ground (5 projects, their roles, their integration points). This is deliberate: the model needs at least one concrete instance to be grounded; the instance is the canonical, detail-rich reference. Update drift is possible — if a project's role changes, both pages need the update. The instance should be the source of truth; the model's instance section should stay at summary level.

## Deep Analysis

### Model — Ecosystem Architecture

> [!tip] Read this when
> You're designing a new multi-project system, evaluating whether to split a monolithic project into an ecosystem, or trying to understand why this ecosystem is structured the way it is.

**What it does well:**
- States universal invariants that survive scale (single responsibility, file-based integration, active knowledge loop, deterministic orchestration, governance from failures)
- Provides a scale progression table (2 → 10+ projects) with PM-level expectations at each tier
- Cross-references the "Deterministic Shell + LLM Core" pattern with five specific implementations
- Includes a "How to Adopt" section that names what's invariant vs. what must be adapted per ecosystem
- Explicitly calls out the "Dual-Perspective Principle" (standalone project vs ecosystem-node lenses)

**Weaknesses:**
- The "Instance — Our Ecosystem" section partially duplicates the instance page
- Reader has to scroll past generalization to find specific details (if that's what they wanted)
- Some claims are framework-inferred (the scale breakpoints table is labeled "synthesized framework, not externally validated thresholds")

**Ideal use:** onboarding someone NEW to the concept of multi-project AI ecosystems, or extracting the pattern for adoption in a different ecosystem.

### Four-Project Ecosystem

> [!tip] Read this when
> You're working inside this ecosystem, need to find a specific project's repo/integration details, or want the current ASCII integration diagram.

**What it does well:**
- Five per-project attribute tables (repo, role, core component, integration, stage)
- ASCII integration map that shows data-flow arrows concretely (wiki → OpenFleet, control-plane → OpenFleet, OpenFleet → OpenArms)
- Ecosystem Quick Reference table at the top (skim-friendly)
- Concrete numbers (10 agents, 78 skills, 24 rules, 16 post-mortems, 20+ channels) grounded in specific source paths
- Answered open questions with validated resolutions (vault usage, OpenArms↔OpenFleet path, wiki MCP for OpenArms)

**Weaknesses:**
- Title says "Four-Project" but enumerates five (OpenArms is "the fifth") — a minor naming debt from when the ecosystem was just four
- No explicit ecosystem-design guidance for adopters — you have to infer the pattern
- Layer=2 label means it's domain-level, but content crosses all five projects

**Ideal use:** operator lookup, agent context-loading, onboarding someone to THIS ecosystem specifically.

## Recommendation

> [!success] Read both — in this order — for full comprehension
>
> 1. **Start with [[four-project-ecosystem|Four-Project Ecosystem]]** to ground yourself in concrete reality (what's the name, where does it live, what does it do).
> 2. **Then read [[model-ecosystem|Model — Ecosystem Architecture]]** to abstract the pattern (what's universal, what's this ecosystem's specific choice).
> 3. **If you're ADOPTING the pattern** (building your own multi-project ecosystem), invert the order — read the model first for the invariants, then the instance as a worked example.
>
> Do NOT treat these as duplicates. The overlap in project descriptions is a known feature; the divergence in abstraction level is the reason both exist.

> [!tip] If forced to pick one
> **Operators working here now → instance.** **Designers elsewhere → model.**

## Relationships

- COMPARES TO: [[model-ecosystem|Model — Ecosystem Architecture]]
- COMPARES TO: [[four-project-ecosystem|Four-Project Ecosystem]]
- BUILDS ON: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
- RELATES TO: [[model-mcp-cli-integration|Model — MCP and CLI Integration]]
- RELATES TO: [[model-sfif-architecture|Model — SFIF and Architecture]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[model-ecosystem|Model — Ecosystem Architecture]]
[[four-project-ecosystem|Four-Project Ecosystem]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[model-mcp-cli-integration|Model — MCP and CLI Integration]]
[[model-sfif-architecture|Model — SFIF and Architecture]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
