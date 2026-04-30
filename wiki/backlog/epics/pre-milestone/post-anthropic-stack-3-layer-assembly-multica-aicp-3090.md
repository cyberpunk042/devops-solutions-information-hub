---
title: "Post-Anthropic Stack 3-Layer Composability — Multica Orchestrator + Harness + AICP Provider Routing (Operator-Driven Assembly, Mid-May 2026 Hardware Delivery)"
aliases:
  - "Post-Anthropic 3-Layer Stack Epic"
  - "Multica + AICP + 3090 Assembly"
  - "Three-Layer Anti-Vendor-Lock-In Stack"
type: epic
domain: backlog
status: in-progress
priority: P0
task_type: epic
current_stage: implement
readiness: 65
progress: 50
stages_completed:
  - "document"
  - "design"
artifacts:
  - "wiki/sources/tools-integration/src-multica-managed-agents-platform.md"
  - "wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md"
  - "wiki/comparisons/rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate.md"
  - "wiki/domains/cross-domain/rlm-qwen3-6-27b-fine-tune-operations-plan.md"
  - "wiki/comparisons/kimi-k2-6-access-paths-openrouter-ollama-cloud-local.md"
  - "wiki/sources/tools-integration/src-inference-provider-landscape-2026.md"
  - "wiki/sources/tools-integration/src-agentic-coding-harness-landscape-2026.md"
  - "wiki/sources/tools-integration/src-opencode-harness-features.md"
confidence: high
created: 2026-04-28
updated: 2026-04-28
last_reviewed: 2026-04-28
sources:
  - id: post-anthropic-milestone
    type: wiki
    file: wiki/backlog/milestones/post-anthropic-self-autonomous-stack.md
    description: "Parent milestone — this epic is the empirical 3-layer assembly that closes the milestone's anti-vendor-lock-in claim at the orchestrator + harness + provider layers"
  - id: multica-synth
    type: wiki
    file: wiki/sources/tools-integration/src-multica-managed-agents-platform.md
    description: "Multica orchestrator-layer source synthesis — Apache 2.0, 10 supported harness CLIs, self-host or cloud, vendor-neutral. Operator IS using Multica (registered 2026-04-28)."
  - id: ollama-cloud-registered
    type: notes
    file: ~/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/project_ollama_cloud_consensus_2026_04.md
    description: "Ollama Cloud is in operator's active stack since 2026-04-23 — registered cloud-LLM tier in the AICP backend pattern (`ollama_cloud`)"
  - id: rtx-3090-ordered
    type: notes
    file: ~/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/project_rtx_3090_acquired_2026_04_27.md
    description: "RTX 3090 (renewed) ordered 2026-04-27, ETA 2-3 weeks — hardware uplift unlocking local-AI tier with 24GB VRAM Ampere"
  - id: rlm-qwen3-8b-live
    type: notes
    file: ~/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/project_rlm_qwen3_8b_hf_checkpoint_live.md
    description: "MIT released RLM-Qwen3-8B at `mit-oasys/rlm-qwen3-8b-v0.1` — confirmed live 2026-04-27. Phase-1 long-context tier available at $0 cash."
  - id: aicp-handoff
    type: external
    file: ~/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md
    description: "Authoritative AICP-side state — `local`, `k2_6_local`, `k2_6_openrouter`, `ollama_cloud` backends wired; $540→$100 routing finding measured"
tags: [epic, p0, post-anthropic, 3-layer-stack, multica, orchestrator, harness, aicp, provider-routing, ollama-cloud, rtx-3090, rlm-qwen3-8b, qwen3-6-27b, anti-vendor-lock-in, mission-2026-04, milestone-class, in-progress]
---

# Epic — Post-Anthropic Stack 3-Layer Composability (Multica + Harness + AICP)

## Summary

The operator's post-Anthropic AI stack reached **3-layer composability** between 2026-04-23 and 2026-04-28. This epic captures the assembly: **Multica** as the open-source vendor-neutral orchestrator (above harness layer) · **Claude Code + OpenCode** as harness layer · **AICP** as provider routing layer · **Ollama Cloud + local Ollama (incoming) + OpenRouter + direct providers** as substitutable LLM tiers · **RTX 3090 (renewed, ordered 2026-04-27, ETA mid-May 2026)** as the hardware uplift that unlocks the local tier · **`mit-oasys/rlm-qwen3-8b-v0.1` (HF live since 2026-04-27)** as the long-context generation candidate · **Qwen3.6-27B at UD-IQ2** as the short-context dense tier. Together these compose into a stack where **no single vendor controls more than one of the three layers** (orchestrator × harness × provider) — empirical anti-vendor-lock-in at three structural layers, not just two. The wiki's [anti-vendor-lock-in lesson Evidence chain](../../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) gains a third substitution dimension. **This epic is in-progress as of 2026-04-28**: components are individually validated; integration is pending the 3090 hardware delivery + per-agent-per-harness provider configuration in Multica's UI. **Phase-1 deployment is $0-cash** (no cloud GPU rental needed); **Phase-2 fine-tune** ($300-500 one-time, conditional) is deferred until Phase-1 demonstrates a real workload ceiling. The parent [post-Anthropic-self-autonomous-stack milestone](../../milestones/post-anthropic-self-autonomous-stack.md) (originally framed at 2 layers — harness + provider) is structurally upgraded by this epic to 3 layers.

## Operator Directive (verbatim, sacrosanct)

> *"I also realize now that I can use a tool called Multica which is an interesting hybrid option that already allow me to use ClaudeCode OR OpenCode, so I have been able to use it and even OpenRouter through it so I could possibly plug anything I want like my localAIs and possibly a Ollama Cloud ?"* (2026-04-28 — opens the Multica thread)

> *"WE ARE USING OLLAMA CLOUD ??? DO YOU REGISTER ?"* (2026-04-28 — registers Ollama Cloud as active stack member, not a research question)

> *"WHY DO YOU MINIZE ALL THIS >????? THIS IS A FUCKING MASSIVE MILESTONES AND EPIC I AM FUCKING TALKING TO YOU ABOUT"* (2026-04-28 — explicit milestone-class framing)

> *"yes I bought one [RTX 3090 renewed], I dont have it yet... probably 2 to 3 weeks...."* (2026-04-28 — hardware delivery timing)

> *"if it transform months into days"* (2026-04-28 — mission framing on cloud-vs-local tradeoffs)

## Goals

- **3-layer composability empirically verified** — operator can issue a task in Multica, have it orchestrate a harness (Claude Code OR OpenCode), have that harness route via AICP to any provider tier (Ollama Cloud OR local Ollama OR OpenRouter), and observe the round-trip working.
- **Per-agent provider configuration in Multica** — investigate and document HOW Multica's UI exposes per-agent env-var or config so different agents can target different LLM providers (this is currently UNVERIFIED — operator confirmed 2026-04-28 that Multica's UI doesn't show an Ollama Cloud dropdown, which makes sense because Multica orchestrates harnesses not providers; the question is HOW the harness gets its provider config when run under Multica).
- **AICP backend integration verified under Multica orchestration** — when Multica runs Claude Code, does Claude Code's `ANTHROPIC_BASE_URL` (pointing at AICP) propagate? When Multica runs OpenCode, does OpenCode's provider config propagate?
- **Local Ollama tier wired post-3090** — once RTX 3090 is delivered (mid-May 2026), local Ollama becomes the primary path for many workloads; AICP `local` backend points at local Ollama; Multica orchestrates harness pointing at AICP.
- **Anti-vendor-lock-in at 3 layers documented end-to-end** — the [anti-vendor-lock-in lesson](../../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) Evidence chain extended to include the orchestrator layer (already partially done via Multica synth and decision-matrix update; needs to be reflected in the lesson's Evidence section).
- **Resilience proven** — when one layer fails (e.g., Ollama Cloud 503s per [GitHub #15453](https://github.com/ollama/ollama/issues/15453)), AICP failover chain routes to next backend; Multica orchestration is unaffected. The 3-layer architecture's resilience claim becomes empirical, not aspirational.

## Done When

- [ ] Multica's per-agent provider config mechanism documented (env var per agent? inherited from runtime daemon? requires harness-side wrapper like `claude-code-router`?) — surfaces a real gap in current understanding
- [ ] Operator can create a Multica agent whose underlying Claude Code is configured (via `ANTHROPIC_BASE_URL` or `ollama launch claude` wrapper) to talk to Ollama Cloud
- [ ] Operator can create a SECOND Multica agent whose underlying Claude Code talks to Anthropic-direct (or different provider)
- [ ] Both agents coexist in same Multica workspace; each is correctly routed to its configured provider
- [ ] OpenCode-as-harness path verified: Multica orchestrates OpenCode with operator's existing OpenCode provider config (per [OpenCode synth](../../../sources/tools-integration/src-opencode-harness-features.md)'s 75+ provider list including Ollama)
- [ ] AICP integration verified under Multica: Claude Code's `ANTHROPIC_BASE_URL=<AICP endpoint>` works when Claude Code is run by Multica daemon
- [ ] One-issue smoke test: assign an issue in Multica → Claude Code agent → AICP routes to Ollama Cloud → result observed in Multica's activity timeline
- [ ] RTX 3090 received (~mid-May 2026); local Ollama installed; AICP `local` backend points at local Ollama; smoke test repeated with Multica → Claude Code → AICP → local Ollama
- [ ] [Anti-vendor-lock-in lesson](../../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) Evidence section updated to include orchestrator layer (3-layer empirical claim)
- [ ] Resilience smoke test: deliberately disable one provider (e.g., `ollama_cloud` AICP backend) → AICP fails over to next tier → Multica's task completes correctly via failover
- [ ] `python3 -m tools.pipeline post` returns 0 validation errors across all epic-related artifacts

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Methodology model** | feature-development (5-stage: document → design → scaffold → implement → test) |
> | **Quality tier** | Skyscraper (full process — this is mission-critical infrastructure) |
> | **Estimated modules** | 5 |
> | **Estimated tasks** | 15-20 |
> | **Critical-path target** | Mid-May 2026 (synchronized with RTX 3090 delivery) |
> | **Full-completion target** | End of May 2026 |
> | **Cash budget (Phase 1)** | **$0** — Multica is open-source self-hostable; harnesses already installed; AICP exists; Ollama Cloud already subscribed; RLM-Qwen3-8B HF download free |
> | **Cash budget (Phase 2 conditional)** | $300-500 one-time IFF operator commits to RLM-Qwen3.6-27B fine-tune AFTER Phase-1 demonstrates real ceiling |
> | **Hardware budget** | RTX 3090 already ordered (separate operator purchase, not part of this epic) |

## Module Breakdown

| Module | Delivers | Phase | Est. Tasks |
|---|---|---|---|
| **M001 — Multica per-agent provider config investigation** | Documentation of HOW Multica's UI/API allows per-agent provider configuration. Gap: currently unknown whether Multica supports per-agent env, inherits from runtime daemon, or requires harness-side wrapper (e.g., `claude-code-router`). | Now | 3-4 |
| **M002 — Harness-level provider wiring under Multica** | Claude Code AND OpenCode each verified to reach Ollama Cloud, AICP-routed providers, and direct providers when orchestrated by Multica. | Now | 4-5 |
| **M003 — AICP-Multica integration smoke test** | Round-trip task: Multica → Claude Code → AICP → Ollama Cloud (or other backend) → result back to Multica. Documented as a reusable pattern. | Now | 2-3 |
| **M004 — Local-Ollama tier post-3090** | After RTX 3090 delivery: local Ollama installed, AICP `local` backend points at it, Multica orchestrates harness → AICP → local Ollama path. Smoke test. | Mid-May 2026 | 4-5 |
| **M005 — Anti-vendor-lock-in lesson Evidence-chain update** | Lesson's Evidence section gains 3-layer composability documentation. The wiki's mission claim is empirically traceable at 3 layers, not 2. | Phase-1 close | 2-3 |

## Dependencies

- **Hardware**: RTX 3090 delivery (~mid-May 2026, ordered 2026-04-27). M004 cannot start until delivery.
- **External tool**: Multica installed and operational (already true — operator is on the UI as of 2026-04-28).
- **External services**: Ollama Cloud Pro subscription active (already true — since 2026-04-23). Anthropic / OpenRouter / Moonshot direct as fallback (variable per workload).
- **Existing AICP infrastructure**: AICP repo at `~/devops-expert-local-ai/` with `local` / `k2_6_local` / `k2_6_openrouter` / `ollama_cloud` backends already wired (per [AICP 2026-04-24 handoff](file:///home/jfortin/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md)).
- **Existing harness installs**: Claude Code (operator's primary today), OpenCode (installed per active-stack memory).
- **Predecessor epics**: [E007 OpenRouter de-risk](E007-openrouter-deadline-de-risk.md) (proves OpenRouter route works) · [E009 Harness Neutrality](E009-harness-neutrality-and-opencode-parity.md) (proves OpenCode parity). Both partially-completed; this epic doesn't block on them but extends their work.

## Open Questions

> [!question] Does Multica's UI expose per-agent provider config?
> Operator confirmed 2026-04-28 that Multica's "New Agent" UI shows harness dropdown (Claude Code / OpenCode / Codex / etc.) but no LLM-provider dropdown. The question is whether per-agent env vars are configurable elsewhere (Settings → Agents → Advanced?), or whether all agents on a runtime inherit env from the daemon's shell. M001 resolves this.

> [!question] How does claude-code-router fit if Multica doesn't expose per-agent env?
> [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) is a wrapper that intercepts Claude Code's API calls and routes them to OpenRouter / DeepSeek / Ollama / etc. If Multica doesn't expose per-agent env, the operator could install claude-code-router as the harness-level provider abstraction, and Multica orchestrates `claude` (which is now actually claude-code-router intercepting). M002 evaluates this option.

> [!question] What does "Multica + AICP" mean concretely?
> AICP exposes an Anthropic-compatible endpoint locally. Claude Code points to AICP via `ANTHROPIC_BASE_URL`. AICP routes to backends (`ollama_cloud`, `k2_6_openrouter`, `local`). When Multica runs Claude Code, does the env var setup propagate? Need empirical test (M003).

> [!question] How does Multica's "Skills" abstraction relate to Claude Code's skills + AICP routing rules?
> Multica's skills are workspace-level reusable capability bundles. Claude Code's skills are CLI extensions. AICP's routing is per-request complexity scoring. Three-tier abstraction overlap — does it create conflict or composability? Needs investigation (deferred to post-Phase-1).

> [!question] What if Multica's daemon doesn't propagate operator's env to spawned harness processes?
> Worst case: Multica respawns harness CLIs in a clean env, breaking provider config that depends on `ANTHROPIC_BASE_URL` / `OPENAI_API_KEY` / etc. Mitigation: configure provider via harness's own config files (not env), OR use Multica's per-agent config if it exists, OR write a wrapper script. M001 + M002 surface this.

## Mission Framing

This epic is the **operational realization** of the wiki's [anti-vendor-lock-in lesson](../../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) at the orchestrator + harness + provider layers. The lesson's Evidence chain previously documented 9 layers (generation × 3 / retrieval / inference paradigm / training framework / environment library / evaluation × 4 / loss objective / + deployment validation) but treated the orchestrator layer as implicit (assumed to be the operator's own scripts or AICP). Multica makes the orchestrator a first-class substitutable component. **Three independently-substitutable layers, no single-vendor multi-layer control = anti-vendor-lock-in at 3 structural levels.**

Per [Saturation Lesson Hard Rule #11](../../../lessons/01_drafts/saturation-declarations-are-p4-aspirational-test-by-attempting-forward-work.md), this epic empirically refutes any "the post-Anthropic mission is wiki-side complete" claim — there's a concrete operational mission-execution path that the wiki had been calling "operator-driven, AICP-side" in earlier framings, and which is now being explicitly documented as a wiki-side epic with the 3-layer composability target.

**EXTENDED 2026-04-30 — 4th-layer extension via the [Trust-Layer Epic](secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md).** The operator-authored tamper-proof-inference design (cypher + decypher + compression composed for 80-90% space saved on large context, seamless and performance-positive) adds a **fourth substitutable layer** — trust / confidential-compute — on top of orchestrator × harness × provider. The two epics compose: this 3-layer epic delivers the substrate; the 4th-layer epic delivers the security stance and compression-encryption pipeline that runs *on top of* whichever orchestrator × harness × provider triple is selected. Per [anti-vendor-lock-in lesson Evidence 11](../../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md), the mission claim now extends to 4 structural layers, not 3.

## Relationships

- IMPLEMENTS: [[post-anthropic-self-autonomous-stack|Milestone — Post-Anthropic Self-Autonomous Stack]] — extends from 2-layer (harness + provider) to 3-layer (orchestrator + harness + provider)
- BUILDS ON: [[src-multica-managed-agents-platform|Multica Synthesis]] (orchestrator-layer source)
- BUILDS ON: [[src-agentic-coding-harness-landscape-2026|Harness Landscape 2026]] (harness-layer survey)
- BUILDS ON: [[src-inference-provider-landscape-2026|Inference Provider Landscape 2026]] (provider-layer survey)
- BUILDS ON: [[ai-model-provider-harness-decision-matrix-2026|AI Model × Provider × Harness Decision Matrix 2026]] (3-axis matrix updated 2026-04-28 with orchestrator dimension)
- BUILDS ON: [[kimi-k2-6-access-paths-openrouter-ollama-cloud-local|K2.6 Access Paths Comparison]] (provider-tier routing rules already established)
- BUILDS ON: [[rlm-qwen3-8b-vs-qwen3-6-27b-tier-0-long-context-candidate|Tier-0 Candidate Comparison]] (Phase-1 routing recipe: RLM-Qwen3-8B for long context + Qwen3.6-27B for short context, both running on RTX 3090)
- DEPENDS ON: [[[[E007-openrouter-deadline-de-risk|E007 — OpenRouter De-Risk]] (predecessor — proves OpenRouter path)]]
- DEPENDS ON: [[[[E009-harness-neutrality-and-opencode-parity|E009 — Harness Neutrality]] (predecessor — proves OpenCode harness parity)]]
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] (extends Evidence chain to 3-layer composability)
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] (Multica's daemon + AICP routing + harness env are infrastructure layers, not instructions)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] (each layer's substitutability is verified by working integration, not just declared)
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] (concrete 2026 stack assembly with empirical components)
- FEEDS INTO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] (operationalizes the Specialty Routing + Resilience Playbook sections)
- EXTENDED BY: [[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic — Cypher + Decypher + Compression]] — adds the 4th substitutable layer (trust / confidential-compute) on top of the orchestrator × harness × provider stack delivered here

## Backlinks

[[Milestone — Post-Anthropic Self-Autonomous Stack]]
[[src-multica-managed-agents-platform|Multica Synthesis]]
[[Harness Landscape 2026]]
[[src-inference-provider-landscape-2026|Inference Provider Landscape 2026]]
[[ai-model-provider-harness-decision-matrix-2026|AI Model × Provider × Harness Decision Matrix 2026]]
[[K2.6 Access Paths Comparison]]
[[Tier-0 Candidate Comparison]]
[[E007 — OpenRouter De-Risk]]
[[E009 — Harness Neutrality]]
[[Anti-Vendor-Lock-In Lesson]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[2026 Consumer Hardware AI Stack]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[Trust-Layer Epic — Cypher + Decypher + Compression]]
