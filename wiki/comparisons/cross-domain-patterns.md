---
title: Cross-Domain Patterns
aliases:
  - "Cross-Domain Patterns"
type: comparison
layer: 3
maturity: growing
domain: cross-domain
status: synthesized
confidence: high
created: 2026-04-08
updated: 2026-04-10
sources:
  - id: src-openfleet-local
    type: documentation
    file: ../openfleet/CLAUDE.md
    title: OpenFleet — Local Project Documentation
    ingested: 2026-04-08
  - id: src-harness-engineering-article
    type: article
    url: https://levelup.gitconnected.com/building-claude-code-with-harness-engineering-d2e8c0da85f0
    title: Building Claude Code with Harness Engineering
    ingested: 2026-04-08
  - id: src-claude-code-accuracy-tips
    type: youtube-transcript
    url: https://www.youtube.com/watch?v=D5bRTv6GhXk
    title: Claude Code Works Better When You Do This
    ingested: 2026-04-08
tags: [cross-domain, patterns, meta-analysis, plan-execute-review, progressive-distillation, deferred-loading, context-aware, orchestration, knowledge-systems, ai-agents]
---

# Cross-Domain Patterns

## Summary

Certain structural patterns recur independently across multiple domains in this wiki — in AI agent orchestration, knowledge management systems, browser automation tools, and research pipelines — without shared design lineage. Their recurrence across independent systems in different domains is evidence that these patterns respond to fundamental constraints (bounded context windows, compound error costs, information retrieval tradeoffs) rather than domain-specific requirements. This page indexes the cross-domain patterns observed in this wiki, documents their instances, and identifies the underlying constraint each pattern responds to.

## Comparison Matrix

### Pattern Inventory

| Pattern | Domains | Instances | Underlying Constraint |
|---------|---------|-----------|----------------------|
| Plan-Execute-Review Cycle | ai-agents, knowledge-systems, automation | OpenFleet orchestrator, Harness Engineering 5-verb workflow, Wiki ingestion pipeline, Research Pipeline | Bounded context + compound error cost |
| Context-Aware Tool Loading | ai-agents, tools-and-platforms | Skills vs MCP, Playwright CLI vs MCP, NotebookLM, Context7 | Fixed context window degrades accuracy as it fills |
| Progressive Distillation | knowledge-systems, ai-agents | Zettelkasten note types, PARA progressive summarization, Wiki maturity evolution, LLM summary layers | Signal degrades without explicit distillation layers |
| Deterministic Shell + LLM Core | ai-agents, automation | OpenFleet orchestrator, Harness guardrails, Wiki post-chain validation | LLM reasoning is unreliable for deterministic operations |
| Gateway-Centric Routing | tools-and-platforms, ai-agents | OpenArms gateway, OpenClaw gateway, Wiki MCP server | Single control plane prevents N-independent-deployment drift |
| Atomic Units + Typed Links | knowledge-systems, ai-agents | Zettelkasten notes, Wiki pages, OpenFleet task graph, LightRAG KB entries | Coarse-grained units resist linking; untyped links resist querying |

## Key Insights

> [!warning] Every pattern responds to the same root challenge
> Unbounded LLM behavior needs structural constraints to produce reliable results. The six patterns reduce to three first-principle constraints:
>
> | Constraint | Patterns It Drives |
> |-----------|-------------------|
> | Bounded context window | Context-Aware Tool Loading, Progressive Distillation |
> | LLM reasoning is probabilistic | Deterministic Shell + LLM Core, Plan-Execute-Review |
> | N independent deployments drift | Gateway-Centric Routing, Atomic Units + Typed Links |

**Battle-tested = 4+ independent instances.** Plan-Execute-Review and Context-Aware Loading have the most cross-domain instances. Framework-level enforcement survives model upgrades; model-level enforcement breaks.

**The system practices what it documents.** Progressive Distillation is both a knowledge management pattern AND this wiki's operating principle. This is not accidental — it is evidence that the pattern responds to a real constraint.

## Deep Analysis

### Pattern 1: Plan-Execute-Review Cycle

**Constraint it addresses**: LLM agents executing without planning accumulate incorrect assumptions that are expensive to revert. Execution without review produces silent failures that compound.

**Cross-domain instances**:

| System | Plan phase | Execute phase | Review phase | Enforcement mechanism |
|--------|-----------|--------------|-------------|----------------------|
| OpenFleet orchestrator | Steps 1-6 (assessment, security scan, doctor run) | Steps 9-10 (dispatch, directives) | Steps 7, 11-12 (approval gate, parent evaluation, health check) | Deterministic Python; LLM cannot bypass |
| Harness Engineering | Setup + Plan verbs + Planner/Critic | Work verb | Review + Release verbs | TypeScript guardrail rules R01-R13 |
| Wiki ingestion (guided) | Extraction plan shown, awaiting approval | Page creation | post-chain: validate → manifest → lint → index | Exit code 1 blocks completion |
| Research Pipeline | EXTRACT + ANALYZE | SYNTHESIZE + WRITE | INTEGRATE (post-chain) | Automated validation gates |

**The pattern's differentiator**: enforcement strength. Systems where review is advisory degrade; systems where review is a hard blocker remain stable under autonomous operation. See: Plan Execute Review Cycle.

### Pattern 2: Context-Aware Tool Loading

**Constraint it addresses**: Fixed context window capacity means every pre-loaded token competes with task-relevant tokens. Accuracy degrades measurably as context fills.

**Cross-domain instances**:

| System | Eager approach (avoided) | Deferred approach (implemented) | Token differential |
|--------|--------------------------|-------------------------------|-------------------|
| MCP servers | All tool schemas loaded at session start | Skills: load only when invoked | Up to 12x |
| Playwright | Full accessibility tree injected after every navigation | CLI: write YAML to disk, read on demand | 12x in 10-step QA tests |
| NotebookLM | All 250+ research sources in context | notebooklm-py: query on demand, targeted answers | 250+ source payloads → 2-3 sentence answers |
| Context7 | Library docs pre-loaded at session start | Post-implementation fact-check fetch | N/A — qualitative accuracy improvement |

**The pattern's generalization**: any information source used on fewer than ~80% of turns should be deferred. The deferred access mechanism — CLI, skill, file read, API query — is secondary to the principle of not pre-loading. See: Context-Aware Tool Loading.

### Pattern 3: Progressive Distillation

**Constraint it addresses**: Raw captured information is too voluminous and low-density to be directly actionable. Without explicit distillation layers, knowledge accumulates without becoming usable.

**Cross-domain instances**:

| System | Layer 0 (raw) | Layer 1 (synthesis) | Layer 2 (insight) | Layer 3 (canonical) |
|--------|--------------|--------------------|--------------------|---------------------|
| Zettelkasten | Fleeting notes | Literature notes | Permanent notes | — |
| PARA + CODE | Captured resources | Organized + highlighted | Distilled (progressive summarization) | Expressed output |
| This wiki | raw/ (transcripts, articles) | wiki/sources/ (source synthesis) | wiki/domains/ (concept pages) | lessons/ + patterns/ + decisions/ |
| Wiki evolution pipeline | seed maturity | growing maturity | mature maturity | canonical maturity |
| Wiki page sections | (raw source in raw/) | ## Summary | ## Key Insights | ## Deep Analysis |

**The pattern's differentiator**: the distillation layers are enforced structurally (as file system layout, as frontmatter fields, as required page sections), not just recommended. If distillation is optional, it is skipped. See: Knowledge Evolution Pipeline, Zettelkasten Methodology, PARA Methodology.

### Pattern 4: Deterministic Shell + LLM Core

**Constraint it addresses**: LLM inference is probabilistic, expensive, and inconsistent across runs. Control decisions, security checks, and quality gates must be deterministic and auditable.

**Cross-domain instances**:

| System | Deterministic shell | LLM core |
|--------|--------------------|---------| 
| OpenFleet orchestrator | 12-step cycle: state transitions, security scan, doctor run, budget gating (zero LLM calls) | Agent execution layer (L3): task work only |
| Harness Engineering | TypeScript guardrail rules R01-R13 (block/query/security) | Claude Code coding worker |
| Wiki post-chain | validate, manifest, lint, obsidian (Python tools) | Ingestion synthesis (LLM writes pages) |
| kb_sync.py | Regex-based relationship extraction from ## Relationships sections | LightRAG knowledge graph queries |

**The pattern's insight**: the LLM should not decide whether the LLM's own output meets quality standards. Deterministic checks are the correct tool for quality gates; LLM reasoning is the correct tool for content generation. Mixing them produces unreliable quality enforcement. See: Agent Orchestration Patterns, Harness Engineering.

### Pattern 5: Atomic Units + Typed Links

**Constraint it addresses**: Coarse-grained units (monolithic documentation pages, compound task descriptions, multi-concept notes) cannot be linked precisely because they match multiple contexts weakly. Untyped links cannot be queried for relationship type.

**Cross-domain instances**:

| System | Atomic unit | Typed link mechanism |
|--------|------------|---------------------|
| Zettelkasten | Permanent note (one idea) | Note links with descriptive anchor text |
| This wiki | Domain concept page (one concept) | ALL_CAPS relationship verbs in ## Relationships |
| OpenFleet KB | KB entry (one tool/command/concept) | ## Relationships section, parsed by kb_sync.py |
| LightRAG graph | Entity (extracted concept) | Relationship triple (entity → relation → entity) |
| OpenFleet task graph | Task (one deliverable) | Multi-dimensional state axes (lifecycle, execution, progress, readiness, validation, context) |

**The machine-readability advantage**: typed links in this wiki's relationship format (`^([A-Z][A-Z /\-]+?):\s*(.+)$`) are parsed directly into LightRAG graph edges by kb_sync.py without LLM extraction. The semantic type is encoded in the human-readable verb and machine-parseable in the same artifact. This is a zero-cost information density gain. See: Wiki Knowledge Graph, LLM Wiki Pattern.

### Pattern 6: Gateway-Centric Routing

**Constraint it addresses**: N independent deployments (one per channel, one per integration, one per client) produce N-way drift in behavior, configuration, and access control. A single gateway prevents drift by making routing, auth, and configuration changes in one place.

**Cross-domain instances**:

| System | Gateway | What it routes |
|--------|---------|----------------|
| OpenArms | Local WebSocket gateway (ws://127.0.0.1:18789) | 20+ messaging channels → unified agent runtime |
| OpenClaw | Open Gateway (ws://18789) | Agent sessions, heartbeats, tool calls → Mission Control |
| Wiki MCP server | MCP server process | Claude Code conversations → wiki read/write/search operations |
| OpenFleet orchestrator | Deterministic orchestrator | PO directives, task events → agent dispatch decisions |

**The operational benefit**: any change to routing logic, access control, or agent behavior is made once in the gateway rather than N times across channel adapters. OpenArms's DM pairing security model applies to all 20+ channels because it is enforced at the gateway, not per-channel. See: Multi-Channel AI Agent Access, MCP Integration Architecture.

## Open Questions

- Are there additional cross-domain patterns not yet surfaced? The `pipeline crossref` command may identify more as wiki density grows. (Requires: running `pipeline crossref` as wiki density increases; not answerable from current static cross-referencing)
- As the wiki grows, will new patterns emerge that are currently invisible because they require more instances to recognize? (Requires: future wiki state; unanswerable until more instances accumulate)

### Answered Open Questions

> [!example]- Do six patterns imply universal "first principles" for LLM agent design?
> Yes. The six patterns reduce to three first-principle constraints: (1) bounded context window → Context-Aware Loading + Progressive Distillation; (2) LLM reasoning is probabilistic → Deterministic Shell + Plan-Execute-Review; (3) N deployments drift → Gateway Routing + Atomic Units. This is a compact, principled design space — six responses to three constraints, not an arbitrary collection.

> [!example]- Which patterns are domain-specific vs genuinely universal?
> **Universal (3+ domains):** Plan-Execute-Review (4 domains), Progressive Distillation (3+), Atomic Units + Typed Links (3+), Context-Aware Tool Loading (any shared-resource system). **More domain-specific:** Gateway-Centric Routing (strong in distributed systems, weak in knowledge-systems), Deterministic Shell + LLM Core (most native to ai-agents/automation; wiki post-chain is the closest knowledge-systems analog).

### Key Takeaway

> [!success] Applying These Patterns
>
> This page is a survey, not a two-sided comparison — the six patterns are complementary, not competing. The takeaway is how to apply them in combination.
>
> **Adopt all six by default when building LLM-augmented systems.** They address distinct root constraints and do not conflict. A system missing any one of them will exhibit the failure mode that pattern prevents: missing Plan-Execute-Review produces silent failures; missing Deterministic Shell produces unreliable quality gates; missing Context-Aware Tool Loading degrades accuracy as context fills; missing Progressive Distillation lets raw knowledge accumulate without becoming usable; missing Atomic Units + Typed Links prevents precise querying; missing Gateway-Centric Routing produces N-way behavioral drift.
>
> **Priority order when starting from scratch:** (1) [[plan-execute-review-cycle|Plan-Execute-Review]] — prevents compounding errors in any agent workflow. (2) [[context-aware-tool-loading|Context-Aware Tool Loading]] — protects accuracy from context saturation on every session. (3) Deterministic Shell + LLM Core — separates quality enforcement from content generation. The remaining three apply as the system matures.
>
> **When a pattern is impractical:** Gateway-Centric Routing is most relevant in distributed multi-channel systems; a single-agent personal tool can defer it. Progressive Distillation requires a maturity model to enforce — without structural enforcement (file system layers, frontmatter fields), it collapses to optional and gets skipped. If you can only enforce one pattern structurally, make it this one.

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit?** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- RELATES TO: [[plan-execute-review-cycle|Plan Execute Review Cycle]]
- RELATES TO: [[context-aware-tool-loading|Context-Aware Tool Loading]]
- RELATES TO: [[agent-orchestration-patterns|Agent Orchestration Patterns]]
- RELATES TO: [[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
- RELATES TO: [[zettelkasten-methodology|Zettelkasten Methodology]]
- RELATES TO: [[para-methodology|PARA Methodology]]
- RELATES TO: [[llm-wiki-pattern|LLM Wiki Pattern]]
- RELATES TO: [[wiki-knowledge-graph|Wiki Knowledge Graph]]
- BUILDS ON: [[second-brain-architecture|Second Brain Architecture]]
- FEEDS INTO: [[research-pipeline-orchestration|Research Pipeline Orchestration]]

## Backlinks

[[plan-execute-review-cycle|Plan Execute Review Cycle]]
[[context-aware-tool-loading|Context-Aware Tool Loading]]
[[agent-orchestration-patterns|Agent Orchestration Patterns]]
[[knowledge-evolution-pipeline|Knowledge Evolution Pipeline]]
[[zettelkasten-methodology|Zettelkasten Methodology]]
[[para-methodology|PARA Methodology]]
[[llm-wiki-pattern|LLM Wiki Pattern]]
[[wiki-knowledge-graph|Wiki Knowledge Graph]]
[[second-brain-architecture|Second Brain Architecture]]
[[research-pipeline-orchestration|Research Pipeline Orchestration]]
