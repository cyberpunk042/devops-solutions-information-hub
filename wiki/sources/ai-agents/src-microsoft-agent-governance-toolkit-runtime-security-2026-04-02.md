---
title: "Synthesis — Microsoft Agent Governance Toolkit (AGT, MIT-licensed, GA-tracking v3.5.0 2026-05-07; first public preview 2026-04-02): the first open-source toolkit to claim 10/10 coverage of the OWASP Agentic AI Top 10 (Dec 2025 taxonomy) via deterministic sub-millisecond (<0.1 ms p99) application-layer policy enforcement, calibrated against a measured 26.67% prompt-only violation rate vs 0.00% with deterministic enforcement; framework-agnostic with adapters for Microsoft Agent Framework / Semantic Kernel / AutoGen / LangGraph / LangChain / CrewAI / OpenAI Agents SDK / Google ADK / LlamaIndex / Haystack / Dify / pi-mono; 5-language SDKs (Python/TS/.NET/Rust/Go); 13,000+ tests; positions agent runtime governance as 'kernel-like infrastructure' the way OS kernels solved untrusted-program isolation — strategic landmark for the operator's OpenClaw/OpenArms/OpenFleet agent-runtime stack and a hard data point against pure prompt-based safety"
type: source-synthesis
domain: ai-agents
status: synthesized
confidence: high
maturity: seed
layer: 1
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: microsoft-opensource-blog-agt-launch-2026-04-02
    type: article
    url: https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/
    file: raw/articles/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-age.md
    description: "Microsoft Open Source Blog launch announcement (Imran Siddique, Principal Group Engineering Manager and Agentic AI Architect at Microsoft, 2026-04-02, 6-min read). Primary launch source. Names the 7 core packages (Agent OS, Agent Mesh, Agent Runtime, Agent SRE, Agent Compliance, Agent Marketplace, Agent Lightning), the 10 OWASP risk mappings, the sub-millisecond <0.1 ms p99 latency claim, the 9,500-tests-at-launch figure (now 13,000+ per README), the cross-language SDK roster (Python/TypeScript/Rust/Go/.NET), the regulatory framings (EU AI Act high-risk Aug 2026, Colorado AI Act June 2026), and the explicit foundation-aspiration ('move it into a foundation home where it can be governed by the broader community ... actively engaging with the OWASP agentic AI community and foundation leaders'). Key quoted philosophy: 'multiple untrusted programs sharing resources, making decisions, and interacting with the outside world, with limited mediation of their actions ... Operating systems solved a similar problem decades ago.'"
  - id: github-microsoft-agt-readme-v3-5-0-2026-05-07
    type: documentation
    url: https://github.com/microsoft/agent-governance-toolkit
    file: raw/articles/microsoftagent-governance-toolkit.md
    description: "GitHub repository README + 30 fetched files for the microsoft/agent-governance-toolkit project (state at 2026-05-15 — latest stable v3.5.0 released 2026-05-07, marked 'Public Preview — Microsoft-signed, production-quality releases. May have breaking changes before GA'). Primary technical reference. Includes: the framework integration matrix (12+ frameworks), the OWASP ASI-01 through ASI-10 coverage table, the published performance numbers (0.012 ms p50 single-rule policy eval, 0.029 ms 100-rule, 72K ops/sec throughput, 35,481 ops/sec concurrent across 50 agents), the comparative claim of '26.67% policy violation rate' for prompt-based safety vs '0.00%' for deterministic application-layer enforcement, the 4-tier privilege rings + saga orchestration + kill switch model, Ed25519 + ML-DSA-65 (NIST post-quantum) credential schemes, SPIFFE/SVID identity, 9 named adopters across production/pilot/research tiers, 6 maintainers from 4 organizations, OpenSSF Best Practices 100%, and the explicit security disclosure that AGT is 'application-level governance (Python middleware), not OS kernel-level isolation. The policy engine and agents run in the same process — the same trust boundary as every Python agent framework.'"
tags: [microsoft, agent-governance-toolkit, agt, owasp-agentic-top-10, runtime-security, agent-runtime, policy-as-code, opa-rego, cedar, ed25519, ml-dsa-65, spiffe-svid, zero-trust-identity, deterministic-enforcement, sub-millisecond-latency, defense-in-depth, mit-license, foundation-aspiration, eu-ai-act, colorado-ai-act, nist-ai-rmf, framework-agnostic, microsoft-agent-framework, semantic-kernel, autogen, langgraph, langchain, crewai, openai-agents-sdk, google-adk, llamaindex, haystack, dify, kernel-analogy, service-mesh-analogy, sre-for-agents, openclaw-relevant, openarms-relevant, openfleet-relevant, "2026-04-02", "2026-05-07", source-synthesis, "2026-05-15", frontier-delta-2026-05-15]
---

# Synthesis — Microsoft Agent Governance Toolkit (AGT)

> [!info] Reference Card
>
> | Field | Value |
> |---|---|
> | **Project** | `microsoft/agent-governance-toolkit` (AGT) |
> | **Launch announcement** | 2026-04-02 (Microsoft Open Source Blog) |
> | **Latest stable** | v3.5.0 — 2026-05-07 (Public Preview; production-quality but breaking changes possible before GA) |
> | **License** | MIT |
> | **Author** | Imran Siddique, Principal Group Engineering Manager + Agentic AI Architect, Microsoft |
> | **Scope** | Runtime governance for AI agents — deterministic policy enforcement, zero-trust identity, execution sandboxing, SRE for agents |
> | **Position claim** | "First toolkit to address all 10 OWASP agentic AI risks with deterministic, sub-millisecond policy enforcement" |
> | **OWASP coverage** | 10/10 (ASI-01 through ASI-10, per [OWASP Agentic AI Top 10 — Dec 2025](https://owasp.org)) |
> | **Latency** | <0.1 ms p99; 0.012 ms p50 single rule; 35,481 ops/sec concurrent across 50 agents |
> | **Tests** | 13,000+ (was 9,500 at launch — grew 37% in ~5 weeks) |
> | **Languages** | Python (full), TypeScript, .NET, Rust, Go (core) |
> | **Framework adapters** | Microsoft Agent Framework, Semantic Kernel, AutoGen, LangGraph, LangChain, CrewAI, OpenAI Agents SDK, Google ADK, LlamaIndex, Haystack, Dify, pi-mono |
> | **Identity primitives** | Ed25519 + ML-DSA-65 (NIST post-quantum), SPIFFE/SVID, Decentralized Identifiers (DIDs), trust scoring 0–1000 |
> | **Policy languages** | YAML, OPA/Rego, Cedar |
> | **Regulatory mappings** | OWASP Agentic Top 10, EU AI Act (high-risk obligations Aug 2026), Colorado AI Act (enforceable June 2026), NIST AI RMF, SOC 2 |
> | **Architecture analogy** | "OS kernels for AI agents" — privilege rings, service mesh (mTLS-like trust), SRE for agents (SLOs, circuit breakers, chaos eng.) |
> | **Foundation aspiration** | Microsoft explicitly states intent to move project to a foundation home (OWASP agentic AI community / LF AI & Data / CoSAI engagement) |

## Summary

The Microsoft Agent Governance Toolkit (AGT, MIT-licensed, public preview launched 2026-04-02, stable v3.5.0 released 2026-05-07) is the first open-source toolkit to claim 10/10 coverage of the **OWASP Agentic AI Top 10** (the December 2025 taxonomy of agent-specific risks: goal hijacking, tool misuse, identity abuse, memory poisoning, cascading failures, rogue agents, etc.) through **deterministic sub-millisecond application-layer policy enforcement** (<0.1 ms p99). The strategic frame Microsoft chose is explicit and load-bearing: AGT treats AI agents as "multiple untrusted programs sharing resources, making decisions, and interacting with the outside world, with limited mediation of their actions" — and applies the **OS-kernel pattern** (privilege rings, identity, process isolation), the **service-mesh pattern** (mTLS-like cryptographic identity, mediated communication), and the **SRE pattern** (SLOs, error budgets, circuit breakers, chaos engineering) to agent runtimes. The empirical anchor is brutal and quotable: Microsoft reports a measured **26.67% policy-violation rate for prompt-based safety** vs **0.00% for AGT's deterministic enforcement** in red-team testing — direct empirical evidence against pure "please follow the rules" guardrail strategies. AGT is **framework-agnostic by design** — adapters ship for Microsoft Agent Framework, Semantic Kernel, AutoGen, LangGraph, LangChain, CrewAI, OpenAI Agents SDK, Google ADK, LlamaIndex, Haystack, Dify, and pi-mono — and is distributed across **5 language SDKs** (Python full-stack; TypeScript / .NET / Rust / Go core). For this project's stored vision, AGT is a landmark: it converts agent-runtime governance from a research-paper topic into **installable infrastructure** (one `pip install`), validates the operator's bet that agent runtime is the dominant performance and safety lever (per the *Harness Engineering Is the Dominant Performance Lever* lesson), and establishes a credible foundation-track competitor to vendor-controlled runtimes — directly relevant to OpenClaw / OpenArms / OpenFleet's positioning as open agent infrastructure. Microsoft has explicitly stated the intent to **donate AGT to a neutral foundation** (engagement with OWASP agentic AI community, LF AI & Data, CoSAI).

## Key Insights

> [!abstract] AGT's load-bearing thesis — "OS kernels for AI agents"
> The toolkit's framing is the synthesis lever. Microsoft is explicitly arguing
> that the right mental model for agent runtimes is not "smarter prompts" or
> "better evals" but **mediated execution** — every action evaluated against
> policy *before* it happens, the way an OS kernel mediates syscalls. The
> blog post draws three analogies in sequence: OS kernels (untrusted programs),
> service meshes (untrusted services), SRE (unreliable distributed systems).
> Each one solved a problem that agent runtimes now face. AGT is a bet that
> the right move is translation, not invention.

1. **The 26.67% → 0.00% violation-rate gap is the killer empirical claim.** AGT's README cites a measured 26.67% policy violation rate for prompt-based safety ("please don't do X") in red-team testing, against 0.00% for deterministic application-layer enforcement. This is **the empirical landmark the agent-safety field has been missing**: a hard, reproducible comparison between prompt-based and runtime-based enforcement. Every claim of the form "if we just write the system prompt better" now has to answer this. The full methodology is in the project's `BENCHMARKS.md`.

2. **Seven-package monorepo, individually installable** — adoption is **incremental, not all-or-nothing**:
   - **Agent OS** — stateless policy engine (the kernel) — YAML / OPA Rego / Cedar
   - **Agent Mesh** — DIDs + Ed25519 + ML-DSA-65 (NIST post-quantum) + Inter-Agent Trust Protocol (IATP) + dynamic trust scoring (0–1000, five behavioral tiers)
   - **Agent Runtime** — 4-tier privilege rings (CPU-privilege-level analog), saga orchestration for multi-step transactions, **emergency kill switch**
   - **Agent SRE** — SLOs, error budgets, circuit breakers, chaos engineering, progressive delivery (the SRE pattern applied to agent fleets)
   - **Agent Compliance** — automated OWASP Agentic Top 10 evidence collection, EU AI Act + Colorado AI Act + SOC 2 + NIST AI RMF mapping, compliance grading
   - **Agent Marketplace** — Ed25519-signed plugin lifecycle, supply-chain trust gating
   - **Agent Lightning** — RL training governance with policy-enforced runners (zero policy violations during reinforcement learning training)

3. **Sub-millisecond p99 latency is the production-readiness claim** that makes deterministic enforcement defensible: 0.012 ms p50 single-rule evaluation, 0.029 ms p50 for 100-rule policies, **35,481 ops/sec concurrent across 50 agents**. Microsoft positions this as "roughly 10,000× faster than an LLM API call" — i.e., governance overhead is mathematically free at the timescales agents already operate at. This neutralizes the historic objection that runtime mediation "would be too slow."

4. **Framework-agnostic by design — and that is the strategic move.** AGT ships adapters into **every major agent framework**: Microsoft's own (Agent Framework, Semantic Kernel, AutoGen) plus the rest of the ecosystem (LangGraph, LangChain, CrewAI, OpenAI Agents SDK, Google ADK, LlamaIndex, Haystack, Dify, pi-mono). Adoption does NOT require rewriting agent code — governance hooks into native extension points (LangChain callback handlers, CrewAI task decorators, Google ADK plugin system, Microsoft Agent Framework middleware pipeline). This explicitly positions AGT as **infrastructure that all frameworks compose with**, not a competing framework.

5. **Five-language SDK matrix** — Python is full-stack; TypeScript (`@microsoft/agent-governance-sdk`), .NET (`Microsoft.AgentGovernance` on NuGet), Rust (`agent-governance` crate), and Go (`agent-governance-golang`) implement core governance (policy, identity, trust, audit). The `.NET MCP` extension package (`Microsoft.AgentGovernance.Extensions.ModelContextProtocol`) is a separate SKU — **Microsoft is shipping MCP governance as a first-class feature**, validating MCP's strategic durability while imposing runtime controls on it.

6. **Regulatory pre-positioning is explicit and load-bearing.** AGT documents compliance mappings for the **EU AI Act** (high-risk AI obligations take effect August 2026), the **Colorado AI Act** (enforceable June 2026), the **NIST AI RMF**, and **SOC 2**. The launch is timed against a regulatory window: any enterprise touching EU operations needs an audit trail of agent decisions within ~3 months of the AGT launch. This is **regulatory-grade infrastructure positioning** — not a research artifact.

7. **MCP Security Scanner is a built-in capability** — detects tool poisoning, typosquatting, and hidden instructions in MCP definitions. This is the first major-vendor open-source implementation of **MCP supply-chain security tooling**; combined with Ed25519-signed plugins in the Agent Marketplace and the `Microsoft.AgentGovernance.Extensions.ModelContextProtocol` .NET package, AGT is laying claim to "the secure MCP runtime layer."

8. **OWASP Agentic Top 10 (Dec 2025) → AGT control mapping is one-to-one and traceable:**

   | OWASP ID | Risk | AGT Control |
   |---|---|---|
   | ASI-01 | Agent Goal Hijacking | Semantic intent classifier in policy engine |
   | ASI-02 | Excessive Capabilities / Tool Misuse | Capability sandboxing + MCP security gateway |
   | ASI-03 | Identity & Privilege Abuse | DID-based identity + behavioral trust scoring |
   | ASI-04 | Uncontrolled Code Execution | Execution rings + resource limits |
   | ASI-05 | Insecure Output / Supply-Chain Risks | Ed25519 plugin signing + manifest verification + content policies |
   | ASI-06 | Memory Poisoning | Cross-Model Verification Kernel (CMVK) with majority voting; episodic memory integrity checks |
   | ASI-07 | Unsafe Inter-Agent Comms | IATP encryption layer |
   | ASI-08 | Cascading Failures | Circuit breakers + SLO enforcement |
   | ASI-09 | Human-Agent Trust Deficit | Approval workflows with quorum logic; full audit trails; flight recorder |
   | ASI-10 | Rogue Agents | Ring isolation + trust decay + automated kill switch + anomaly detection |

9. **Foundation aspiration is explicit and not Microsoft-bound.** Quoted directly: "We believe agent governance is too important to be controlled by any single vendor. We're releasing this project under Microsoft today, but our aspiration is to move it into a foundation home where it can be governed by the broader community. We're actively engaging with the OWASP agentic AI community and foundation leaders to make this happen." Active engagement is named with the **OWASP Agent Security Initiative, LF AI & Data Foundation, and CoSAI working groups**. This is a structural commitment, not a vague gesture.

10. **Open-source fundamentals are exceptional and worth naming** — 13,000+ tests (was 9,500 at launch, grew 37% in ~5 weeks), continuous fuzzing via ClusterFuzzLite (7 fuzz targets), SLSA-compatible build provenance, OpenSSF Scorecard tracking, OpenSSF Best Practices 100%, CodeQL + Dependabot (13 ecosystems), pinned-with-hash CI dependencies, 20+ step-by-step tutorials, 9 named adopters across production/pilot/research, 6 maintainers from 4 organizations, GOVERNANCE.md + CHARTER.md + MAINTAINERS.md per LF Projects format. This is **release engineering posture more typical of mature CNCF projects than a 6-week-old preview**.

11. **Critical security disclosure — honest about boundaries.** AGT documents explicitly: "This toolkit provides **application-level governance** (Python middleware), not OS kernel-level isolation. The policy engine and agents run in the same process — the same trust boundary as every Python agent framework." Production recommendation: **run each agent in a separate container** for OS-level isolation. This is the kind of honest threat-model disclosure missing from most agent-runtime pitches — and it scopes the AGT promise correctly: deterministic policy enforcement *within* a trust boundary, not isolation *across* trust boundaries.

12. **"Trust is dynamic, not static" — the lessons section embeds a non-obvious design claim.** AGT's trust-scoring model (0–1000, five behavioral tiers, with behavioral decay and dynamic privilege assignment) is explicitly named as a rejection of binary trust models. From the blog post: "A binary trusted/untrusted model doesn't capture reality. Trust scoring with behavioral decay and dynamic privilege assignment turned out to be a much better model for systems where agents are constantly changing." This is a **transferable lesson** for any agent-runtime design (including the operator's OpenClaw/OpenArms/OpenFleet stack).

> [!warning] AGT does NOT solve LLM-level safety
> AGT explicitly disclaims content moderation and prompt guardrail responsibilities.
> "This is not a prompt guardrail or content moderation tool. It governs agent
> *actions*, not LLM inputs/outputs. For model-level safety, see Azure AI Content
> Safety." This is the right scope, but it means **a complete agent safety
> story still needs**: (a) AGT for action governance, (b) a prompt-defense /
> content-safety layer for LLM I/O, (c) OS / container isolation for compute
> sandboxing, (d) model-level alignment evals upstream. AGT is one layer, not
> the whole stack.

## Deep Analysis

### Why this is vision-relevant to this project (per operator's stated technology vision)

This project's stored vision (see `wiki/spine/references/ai-infrastructure-decision-framework-2026.md`, the `Harness Engineering Is the Dominant Performance Lever` lesson, and the OpenClaw / OpenArms / OpenFleet ecosystem syntheses) treats **agent runtime as the dominant performance and safety lever** — i.e., what determines whether an agent ships reliable, governable, audit-friendly behavior is the runtime harness around the LLM, not the LLM itself. AGT is the first major-vendor open-source artifact that **operationalizes that thesis at production scale** with empirical backing (the 26.67% → 0.00% gap), regulatory-grade compliance posture, and explicit foundation aspiration.

Three concrete implications for the operator's stack:

1. **OpenClaw** (agent harness) — AGT's adapter pattern (hook into native extension points without replacing the framework) is **structurally compatible** with OpenClaw's harness model. The strategic question is whether OpenClaw should ship an AGT adapter (composable with rather than replacing AGT) or build a parallel governance layer. The former is almost certainly correct — AGT's 10/10 OWASP coverage is hard to match from scratch, and Microsoft has indicated foundation donation, which would neutralize the vendor concern. **Surfaced for operator decision.**

2. **OpenArms** (agent runtime / mesh) — AGT's `Agent Mesh` package (DIDs + Ed25519 + ML-DSA-65 + IATP + trust scoring) directly overlaps with what OpenArms is building. There are two possible postures: (a) OpenArms adopts AGT primitives wholesale and focuses differentiation upstream; (b) OpenArms competes on the mesh layer and ships AGT-compatible interop. The latter is only justified if OpenArms can articulate a sharp differentiator vs AGT's Mesh package. **Surfaced for operator decision.**

3. **OpenFleet** (fleet-level orchestration) — AGT's `Agent SRE` package (SLOs, error budgets, circuit breakers, chaos eng., progressive delivery) is squarely in the OpenFleet problem space. Same question as #2: adopt as a substrate or compete on the layer. The asymmetry here is that Microsoft's pattern (SRE for agent fleets) is well-validated — adopting AGT-SRE primitives and differentiating on fleet topology / multi-tenant economics is probably the right move. **Surfaced for operator decision.**

### Strategic positioning — what Microsoft is actually doing

The AGT launch is not a research-paper drop. It is a **regulatory-window play with foundation-track infrastructure**: the EU AI Act high-risk obligations take effect August 2026, the Colorado AI Act becomes enforceable June 2026, and OWASP shipped the Agentic Top 10 in December 2025. Microsoft is publishing AGT in April 2026, growing it 37% in tests within 5 weeks, signing a v3.5.0 stable release on 2026-05-07, and announcing foundation-donation intent. This is **structurally equivalent to the OpenTelemetry play** — release as Microsoft, donate to foundation, control the standard, lock in framework compatibility. The integration matrix is the moat: by shipping adapters for Microsoft Agent Framework AND OpenAI Agents SDK AND Google ADK AND LangChain AND CrewAI, AGT positions itself as the **neutral runtime governance layer** every agent framework needs. The five-language SDK roster reinforces this: this is infrastructure, not a Python research project.

### What changes downstream of AGT existing

Three claim-shifts to flag in this project's existing pages:

- **`Harness Engineering Is the Dominant Performance Lever` (lesson)** — AGT provides a hard external empirical anchor (26.67% → 0.00% gap). The lesson should reference this number when it next moves up the maturity ladder. **Flag for follow-up.**
- **`AI Infrastructure Decision Framework 2026` (reference)** — the framework's "agent runtime layer" treatment now has a concrete, MIT-licensed, foundation-track option that didn't exist before April 2026. The reference page's agent-runtime section likely needs an AGT row added. **Flag for follow-up.**
- **`OpenClaw` (concept page) / OpenArms / OpenFleet syntheses** — strategic positioning vs AGT needs a paragraph. **Surface to operator for decision before authoring** (this Profile does not modify operator-territory pages, per `TOOLS.md`).

### Adapters list — the integration matrix as a strategic artifact

AGT's framework integration matrix (from the README):

| Framework | Integration type | Stack signal |
|---|---|---|
| Microsoft Agent Framework | Native Middleware | Microsoft-aligned |
| Semantic Kernel (.NET + Python) | Native | Microsoft-aligned |
| Microsoft AutoGen | Adapter | Microsoft-aligned |
| LangGraph / LangChain | Adapter | Ecosystem standard |
| CrewAI | Adapter | Ecosystem standard |
| OpenAI Agents SDK | Middleware | **Notable — direct competitor** |
| pi-mono (coding-agent) | TypeScript SDK Integration | Emerging |
| Google ADK | Adapter | **Notable — direct competitor** |
| LlamaIndex | Middleware | Ecosystem standard |
| Haystack | Pipeline | Ecosystem standard |
| Dify | Plugin | Ecosystem (already in Dify marketplace) |
| Azure AI Foundry | Deployment Guide | Microsoft-aligned |

The presence of **OpenAI Agents SDK** and **Google ADK** adapters at parity with Microsoft-native integrations is the tell: AGT is not a Microsoft-stack play, it is a **runtime governance standard** positioning move.

## Open Questions

- **What is OpenClaw's posture toward AGT — composable adapter or parallel layer?** Composition is structurally correct; needs operator-level decision and AGENTS.md statement.
- **What does the operator want done with the OpenArms Mesh / AGT Mesh overlap?** This is a direct architectural overlap. Adopt-or-compete is a real decision, not a deferral.
- **Where does AGT land on foundation donation — OWASP, LF AI & Data, or CoSAI?** Each implies different governance constraints. Watch the next 3–6 months.
- **How does the 26.67% → 0.00% claim hold up under independent red-team?** The benchmark methodology is documented in `BENCHMARKS.md` but has not (yet) been replicated by third parties. Watch for independent replications.
- **Will the broader ecosystem adopt the OWASP Agentic Top 10 as the standard taxonomy?** AGT's 10/10 mapping is a structural bet that ASI-01 through ASI-10 become the canonical risk vocabulary. If yes, AGT is positioned as the reference implementation. If no, AGT may need to re-map. So far OWASP momentum looks strong (December 2025 publication, multiple regulator alignments cited in the AGT docs).
- **How does AGT compose with `claude-code-harness` or the operator's harness syntheses (per `Harness Engineering Is the Dominant Performance Lever`)?** Likely complementary — harnesses operate at the workflow / orchestration layer, AGT operates at the per-action policy layer. Worth a dedicated comparison page.

## Relationships

- **EXTENDS:** `wiki/lessons/01_drafts/harness-engineering-is-the-dominant-performance-lever.md` — AGT is the productized form of this lesson with empirical backing.
- **EXTENDS:** `wiki/spine/references/ai-infrastructure-decision-framework-2026.md` — the agent-runtime row needs an AGT entry.
- **RELATES TO:** `wiki/domains/ai-agents/orchestration/openclaw.md` — AGT is structurally composable with OpenClaw; posture decision pending.
- **RELATES TO:** `wiki/sources/ai-agents/src-anthropic-effective-harnesses-long-running-agents.md` — Anthropic's harness guidance is workflow-level; AGT is per-action policy-level; complementary.
- **RELATES TO:** `wiki/sources/ai-agents/src-rethinking-ai-agents-harness-engineering-rise.md` — same complementary positioning.
- **RELATES TO:** `wiki/sources/ai-models/src-anthropic-mythos-preview-frontier-restricted-2026-04-16.md` — Anthropic's safety strategy is *capability gating per use case*; Microsoft's (via AGT) is *runtime mediation across all capabilities*. Two different bets on the same problem.
- **CONTRASTS WITH:** prompt-only safety strategies (system prompts, persona constraints) — AGT's 26.67% → 0.00% empirical claim is the data point against pure-prompt approaches.
- **CONTRASTS WITH:** vendor-controlled agent runtimes — AGT is MIT + foundation-aspirational; positions against any pure-vendor lock.
- **CROSS-PROJECT TOUCHPOINT:** OpenArms (Agent Mesh overlap), OpenFleet (Agent SRE overlap), OpenClaw (harness-adapter composition). **Operator-decision-queue surfaced.**
