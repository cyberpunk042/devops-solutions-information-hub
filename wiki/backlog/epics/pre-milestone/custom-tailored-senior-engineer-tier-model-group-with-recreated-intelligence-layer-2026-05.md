---
title: "Custom-Tailored Senior-Engineer-Tier Model Group + Recreated Intelligence Layer Pipeline (Operator-Authored 2026-05-04)"
aliases:
  - "Senior-Engineer-Tier Custom Model Group Epic"
  - "Custom Model Group + Intelligence Layer Pipeline"
  - "Operator-Tier Model Mission Epic"
  - "Custom-Tailored Model Mission"
  - "Custom-Tailored Model Group Epic"
  - "Custom-Tailored Senior-Engineer-Tier Model Group Epic"
type: epic
domain: backlog
status: active
priority: P0
task_type: epic
current_stage: design
readiness: 20
progress: 0
stages_completed:
  - "document"
artifacts:
  - "wiki/domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md"
  - "raw/notes/2026-05-04-custom-tailored-model-group-moe-intelligence-layer-and-root-ghostproxy-pain-point.md"
confidence: high
created: 2026-05-04
updated: 2026-05-04
last_reviewed: 2026-05-04
sources:
  - id: operator-directive
    type: file
    file: raw/notes/2026-05-04-custom-tailored-model-group-moe-intelligence-layer-and-root-ghostproxy-pain-point.md
    description: "Operator directive 2026-05-04 — verbatim concept of senior-engineer-tier customized model group + recreated intelligence layer at I/O boundaries + multi-version + information-virus + interfaces + middleware + composition with cypher/decypher + composition with I/O compression. Plus the pain-point trigger (root-ghostproxy bootstrap on Debian 13 non-GUI; even fully-configured systems pay AI alignment overhead repeatedly per session)."
  - id: design-synthesis
    type: wiki
    file: wiki/domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md
    description: "Design ground-truth synthesis — captures operator-authored concept with architecture sketch, phase scope, mission alignment, and 8 open design questions. This epic tracks execution against that synthesis."
  - id: e012-tactical-predecessor
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E012-custom-model-library-unsloth-loras.md
    description: "Existing tactical custom-model epic (P2) — Wiki-Assistant + Wiki-Router + Multi-LoRA. This new epic NESTS E012's deliverables as components (Wiki-Router becomes the input-boundary intelligence-layer router; Wiki-Assistant becomes one of the small-LoRA specialists in the model group). E012 stays P2 tactical; this new epic is P0 strategic-tier."
  - id: second-brain-custom-model-strategy
    type: wiki
    file: wiki/spine/references/second-brain-custom-model-strategy.md
    description: "Existing 5-candidate custom-model strategy doc — provides the candidate-base + LoRA-rank + data-recipe substrate. This epic adds the senior-engineer-tier behavioral-alignment dimension on top."
  - id: trust-layer-epic
    type: wiki
    file: wiki/backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md
    description: "Trust-Layer Epic — composes with this epic via operator-toggle-able L0–L4 opt-ins (operator: 'with and without cypher / decypher with or without I/O Compression')"
  - id: post-anthropic-3-layer-epic
    type: wiki
    file: wiki/backlog/epics/pre-milestone/post-anthropic-stack-3-layer-assembly-multica-aicp-3090.md
    description: "Adjacent epic — orchestrator × harness × provider 3-layer stack. The custom model group becomes a routable provider in this stack via Multica + AICP routing."
  - id: post-anthropic-milestone
    type: wiki
    file: wiki/backlog/milestones/post-anthropic-self-autonomous-stack.md
    description: "Parent milestone — this epic adds custom-model strategic-tier scope to the post-Anthropic mission (operator: 'this will be part of this project... massive project... really long')"
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Mission lesson — this epic delivers candidate Evidence 12 (custom-model-customization substitutable axis OR 5th layer; operator-decision)"
  - id: spec-driven-convergence-lesson
    type: wiki
    file: wiki/lessons/01_drafts/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md
    description: "Convergence lesson — operator's 'like we teach' names this directly; model-creation workflow becomes the 9th instance of the spec-driven convergent pattern"
  - id: rlm-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md
    description: "RLM substrate — `mit-oasys/rlm-qwen3-8b-v0.1` is itself a customization-on-open-weight-base instance; candidate base for v0.1-seed"
  - id: prime-rl-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-prime-intellect-prime-rl-async-rl-training-at-scale.md
    description: "Training framework — Apache 2.0; IPO + Kimi-K2.5 KL default loss; 48 H100 hours / ~$48-100 cloud-rental for the RLM-Qwen3-8B post-train precedent"
  - id: unsloth-synthesis
    type: wiki
    file: wiki/sources/tools-integration/src-unsloth-fast-lora-consumer-hardware.md
    description: "Consumer-hardware fine-tune substrate — LoRA + UD-IQ2 / Q2_K; the realistic training environment on RTX 3090"
  - id: dpo-paper
    type: documentation
    url: https://arxiv.org/abs/2305.18290
    description: "Direct Preference Optimization — preference-data fine-tuning method"
  - id: ipo-paper
    type: documentation
    url: https://arxiv.org/abs/2310.12036
    description: "IPO — DPO refinement; default loss in prime-rl"
  - id: lorahub-paper
    type: documentation
    url: https://arxiv.org/abs/2307.13269
    description: "LoRAHub — composing multiple LoRA modules; substrate for operator's MoE-of-LoRAs framing"
  - id: ties-merging-paper
    type: documentation
    url: https://arxiv.org/abs/2306.01708
    description: "TIES merging — composing fine-tuned models without retraining"
  - id: constitutional-ai
    type: documentation
    url: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
    description: "Constitutional AI — alignment-by-constitution precedent for operator's 'core' as the constitution"
tags: [epic, p0, custom-model, senior-engineer-tier, moe-group, intelligence-layer, behavioral-alignment, preference-data, dpo, ipo, multi-version, information-virus, interfaces, middleware, python-hyperstructure, markdown-as-iac, trust-layer-composition, compression-composition, anti-vendor-lock-in, post-anthropic, mission-2026-05-04, milestone-class, operator-authored, strategic-tier]
---

# Epic — Custom-Tailored Senior-Engineer-Tier Model Group + Recreated Intelligence Layer Pipeline

## Summary

Operator-authored 2026-05-04: build the **senior-engineer-tier customized model group + recreated intelligence layer at I/O boundaries** that extends the post-Anthropic mission with operator-controlled model customization. The pipeline composes: (a) **a group of customizations on open-weight bases** — Mixture-of-LoRAs and/or MoE-base fine-tunes per task class with size variance per latency budget; (b) **operator's behavioral-alignment core** — preference data over hack-vs-right outputs, instruction data, and a constitution-as-Markdown encoding the operator's standards; (c) **a recreated intelligence layer at I/O boundaries** — input-boundary routing/compression/spec-loading/context-selection/tool-use planning + output-boundary schema-gating/self-verification/methodology-compliance/hallucination-detection, expressed as Python-as-programming hyperstructure on top of Markdown-as-IaC; (d) **multi-version release discipline** — per-version manifest, maturity ladder (`v0.1-seed` · `v0.5-growing` · `v1.0-validated`), no auto-promotion; (e) **information-virus propagation** to sister projects (OpenArms · OpenFleet · AICP · devops-control-plane · root-ghostproxy when operator registers it) so methodology spreads by weight not just by prose; (f) **operator-toggle-able composition with the trust + compression layers** — L0–L4 trust opt-ins per workload, with/without I/O compression. The model group runs natively on the operator's incoming RTX 3090 (mid-May 2026 ETA) at L2 default; cloud H100 rental is opt-in for larger-base experiments. **This epic is strategic-tier and milestone-class** — operator framed the scope as *"massive project, really long"* — and **NESTS the existing tactical [E012 Custom Model Library](E012-custom-model-library-unsloth-loras.md)** (P2 LoRA library) without replacing it. The mission claim it delivers: a candidate substitutable axis WITHIN the provider layer (operator-authored vs vendor-supplied) OR a candidate 5th substitutable layer (model-customization / operator-authored-tier) — **operator-design call** captured in the open questions below.

## Operator Directive (verbatim, sacrosanct)

> *"continue.. also I realize I really am going to need to find and customize my own model.. I think the models in genral lack a core that bring way more intelligence to the model and make it adapted to a real senior software engineer instead of a newbe and by the same way extract way more power and reliability from it."*

> *"most model try to do both ends at the same time and end up achieing both mediocer ... My goal would be to really tailing it to my need and knowledge and proned ways and high standards and Adding my core to it. An AI that not longer try to hack or rush or quickfix things but naturally WANT to do things right and follow the right methodologies and ways to do things."*

> *"Of course it will have multiple versions. but we want to act potentially like both an information virus if you will and also front and out interfaces and possibly a little of middlewares shaping and integrations."*

> *"this will be part of this project, it will be a massive project and we will need to be ready and it will be really long."*

> *"It made me realize all this but clearly its not a model... we probalby need to find our find Group of MoE models of various sizes and needs and we create an intelligence layer... we recreate intelligence at the layers needed. in and out. and we use python and turn thing into proto-programming or proto proto-programming / structure and hyperstructure and exploiting the latest possibilites and adapting to the requirements of the set configuration and so on."*

> *"Its not as if I was mastering AI model creation yet... nor will I maybe but possibly my own customizations and possibly even more useful and flexible. like we teach."*

> *"with and without cypher / decypher with or without I/O Compression, etc we take our time to think things right."*

### Pain-Point Anchor (the trigger)

> *"on this machine I have the system level config and so many things including the project(s) itself but as much as I can configure the harness more and ecosystem and the project itself.. it takes time before getting started... there are things that shouldn't have to be so long and hard or repeatitive and hard to make the AI align to. THE pain point must be itentified with their root and thus we can find the possible solution at the right place."*

The root, named: alignment overhead is paid repeatedly at fresh-environment session starts because the alignment substrate (CLAUDE.md + AGENTS.md + .claude/rules/ + harness + ecosystem config) is *external to the model*. Baking operator's standards into the weights via preference fine-tune + curated instruction data + behavioral constitution is the **solution at the right place** — pay alignment cost once at training, not per session at every fresh environment.

## Goals

- **Operator-tier behavioral alignment in the weights** — the model *naturally wants* to follow methodology over hack-and-rush, validated by held-out hack-vs-right behavior tests
- **Senior-engineer-tier specialization** — empirically defensible per [Anti-Vendor-Lock-In Evidence 1](../../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) (Qwen3.6-27B-Dense beats some 397B MoE on agentic coding) and [Evidence 8](../../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) (RLM-Qwen3-8B approaches frontier on 3/4 long-context tasks at 48 H100 hours / ~$48–100 budget)
- **Model group with size variance per task class** — Mixture-of-LoRAs per senior-engineer task surface (coding · methodology-reasoning · spec-authoring · validation-checking · refactor-planning · debug-analysis); composed via task-routing at inference time
- **Recreated intelligence layer at I/O boundaries** — input boundary (routing + Caveman compression + context selection + spec loading + tool-use planning) and output boundary (schema gate + self-verification + methodology compliance + hallucination detection) as Python hyperstructure
- **Multi-version release discipline** — per-version manifest of base + LoRA + preference data + instruction data + constitution + composition; maturity ladder (`v0.1-seed` → `v0.5-growing` → `v1.0-validated`); no auto-promotion (operator review required)
- **Information-virus ecosystem propagation** — sister-project consumers (OpenArms · OpenFleet · AICP · devops-control-plane · root-ghostproxy when registered) inherit operator's standards by weight; per-consumer integration documented
- **Composition with trust + compression layers** — operator-toggle-able L0–L4 opt-ins (per [Trust-Layer Epic](secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md)); default L2 on RTX 3090 (compressed-encrypted weights + on-GPU decypher via Triton + Caveman input-prompt compression); operator-decision per workload
- **Pain-point reduction empirically measured** — fresh-environment session-start time-to-first-quality-output reduced vs Opus 4.x baseline; the *"shouldn't have to be so long and hard or repetitive"* property validated, not just declared
- **Mission-claim extension** — Anti-vendor-lock-in lesson Evidence 12 (operator-decision: substitutable axis WITHIN provider layer OR 5th substitutable layer) propagated through the wiki's mission-claim chain
- **E012 nesting clean** — Wiki-Router (E012 D) becomes the input-boundary intelligence-layer router; Wiki-Assistant (E012 A) becomes one of the small-LoRA specialists; E012 stays P2 tactical; this epic stays P0 strategic; no duplicate work

## Done When

- [ ] Phase 0 toolchain wired on RTX 3090 — Unsloth + prime-rl + Triton reproducible training environment
- [ ] Phase 1 data discipline shipped — `data/preferences/v0.1.jsonl` + `data/instructions/v0.1.jsonl` + `constitution-v0.1.md` (operator-authored)
- [ ] First operator-tier specialist LoRA `v0.1-seed` deployed — operator picks base; deployable via Ollama; AICP-routable
- [ ] Mixture-of-LoRAs group expanded — at least 3 specialist LoRAs (coding · methodology-reasoning · validation-checking) operator-graded on held-out tests
- [ ] Recreated intelligence layer operational — input-boundary routing + Caveman compression + spec loading + output-boundary schema gate + self-verification + methodology compliance, all Python-implemented
- [ ] Behavioral preference fine-tune — DPO/IPO over operator-curated hack-vs-right pairs; the *"naturally WANT to do things right"* property empirically validated on held-out tests (operator-graded; ≥80% behavior-test pass rate target — operator confirms threshold)
- [ ] Trust + compression composition wired — L2 default on RTX 3090 per [Trust-Layer Epic M001](secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md); operator-toggle for L0/L3/L4 verified
- [ ] Multi-version manifest + release discipline operational — `v0.1-seed` shipped with full manifest (base + LoRAs + preference data + instruction data + constitution + composition); maturity-ladder review process documented
- [ ] Information-virus propagation to ≥2 sister-project consumers documented — operator picks (likely AICP routing tier + one of OpenArms/OpenFleet/devops-control-plane/root-ghostproxy)
- [ ] Pain-point reduction measured — fresh-environment time-to-first-quality-output baseline (Opus 4.x) vs custom model group (`v0.5-growing` or later) on at least 3 representative task classes
- [ ] [Anti-Vendor-Lock-In Lesson](../../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) Evidence chain extended (Evidence 12 — operator-decision: 5th layer or provider-axis)
- [ ] [Post-Anthropic Milestone](../../milestones/post-anthropic-self-autonomous-stack.md) acceptance criteria amended (EXTENDED 2026-05-04)
- [ ] E012 nesting documented — Wiki-Router routes to this group; Wiki-Assistant nests as a specialist
- [ ] `python3 -m tools.pipeline post` returns 0 validation errors across all epic-related artifacts

## Scale and Model

> [!info] Epic Parameters
>
> | Parameter | Value |
> |---|---|
> | **Methodology model** | feature-development (5-stage: document → design → scaffold → implement → test) |
> | **Quality tier** | Skyscraper (full process — strategic-tier + mission-class + multi-version) |
> | **Estimated modules** | 6 (M001–M006) |
> | **Estimated tasks** | 30–40 across all phases |
> | **Critical-path target** | `v0.1-seed` first specialist LoRA within ~6 weeks of RTX 3090 delivery (mid-May → late June 2026) |
> | **`v0.5-growing` target** | Multi-LoRA group + intelligence layer + behavioral preference fine-tune within ~4 months of v0.1-seed |
> | **`v1.0-validated` target** | Operator-decision; not date-bound; depends on held-out evaluation pass rate |
> | **Cash budget (Phases 0–4 on RTX 3090)** | $0 — Unsloth open-source · prime-rl Apache 2.0 · Triton via OpenAI · base models from HuggingFace · all run on RTX 3090 |
> | **Cash budget (Phase 5 behavioral preference fine-tune)** | $0 on RTX 3090 (12–48 hours) OR ~$48–100 cloud-H100-rental per cycle (4–12 H100 hours, per RLM-Qwen3-8B precedent) — operator-decision per cycle |
> | **Cash budget (Phase 6 + 7 trust composition + ecosystem propagation)** | $0 — composes with existing infrastructure |

## Candidate Module Breakdown

> [!info] Candidate breakdown — to be confirmed by operator. Modules are not authored as separate pages until operator confirms scope and ordering. Per the trust-layer-epic precedent.

| Module (candidate) | Delivers | Phase | Est. Tasks |
|---|---|---|---|
| **M001 — Toolchain + Data Discipline + Constitution v0.1** | Phase 0 + Phase 1 combined: Unsloth + prime-rl + Triton on RTX 3090; `data/preferences/v0.1.jsonl` from operator-curated hack-vs-right pairs; `data/instructions/v0.1.jsonl` from wiki corpus + operator-authored; `constitution-v0.1.md` (parallels CLAUDE.md scope; small enough to fit single context window during training) | Phase 1 — post-3090 (mid-May 2026 onward) | 5–6 |
| **M002 — First Specialist LoRA + Group Expansion** | Phase 2 + Phase 3 combined: pick base (operator-decision: Qwen3.6-27B at UD-IQ2 / RLM-Qwen3-8B / Qwen3-Coder / merge); train first specialist LoRA `v0.1-seed`; held-out evaluation; expand to Mixture-of-LoRAs across senior-engineer task surfaces (coding · methodology-reasoning · validation-checking · etc.) | Phase 1 | 6–8 |
| **M003 — Recreated Intelligence Layer at I/O Boundaries** | Phase 4: input boundary (routing + Caveman compression + spec loading + context selection + tool-use planning) + output boundary (schema gate + self-verification + methodology compliance + hallucination detection); Python-as-programming hyperstructure on top of Markdown-as-IaC; AICP integration | Phase 1 — parallelizable with M002 after M001 | 5–7 |
| **M004 — Behavioral Preference Fine-Tune (DPO / IPO)** | Phase 5 — the highest-leverage module: operator-curated preference pairs (hack-vs-right outputs); DPO/IPO loss via prime-rl; `naturally WANT to do things right` property empirically validated; this is what makes the model behaviorally distinct from base | Phase 1 close — depends on M001 + M002 group | 4–6 |
| **M005 — Trust + Compression Composition Wiring** | Phase 6: L2 default on RTX 3090 (compressed-encrypted weights + on-GPU decypher via Triton + Caveman input-prompt compression); operator-toggle for L0/L3/L4 verified; composes per [Trust-Layer Epic M001](secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md) without architectural coupling | Phase 1 close — parallelizable after Trust-Layer M001 | 3–4 |
| **M006 — Multi-Version Release Discipline + Ecosystem Propagation + Mission Update** | Phase 7: per-version manifest; maturity ladder; no-auto-promotion review; sister-project consumer integration (≥2 of: AICP routing tier · OpenArms · OpenFleet · devops-control-plane · root-ghostproxy when registered); pain-point reduction measured; Anti-vendor-lock-in Evidence 12 added; post-Anthropic milestone amended | Phase 2 — after `v0.5-growing` reached | 4–6 |

## Dependencies

- **Hardware (M001–M005)**: RTX 3090 delivery (~mid-May 2026, ordered 2026-04-27). All training-side modules begin on delivery.
- **Hardware (M004 cloud option)**: Optional H100 cloud rental for larger-base preference fine-tune cycles — operator-decision per cycle, not date-bound.
- **Predecessor epic — composes**: [Trust-Layer Epic](secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md) M001 (L2 reference pipeline); M005 of this epic depends on the L2 substrate.
- **Predecessor epic — composes**: [Post-Anthropic 3-Layer Stack Epic](post-anthropic-stack-3-layer-assembly-multica-aicp-3090.md) — orchestrator (Multica) + harness (Claude Code / OpenCode) + provider (AICP) layers route to the custom model group.
- **Predecessor epic — nests**: [E012 Custom Model Library](E012-custom-model-library-unsloth-loras.md) — Wiki-Router (E012 M003) and Wiki-Assistant (E012 M002) become components of M002/M003 of this epic. E012 stays P2 tactical alongside.
- **External tools (open-source, all wired before epic starts)**: Unsloth (LoRA + UD-IQ2/Q2_K) · prime-rl (Apache 2.0; IPO + custom-loss support) · Triton (OpenAI; on-GPU kernels) · Python `cryptography` (AES-256-GCM via Trust-Layer M005) · base models from HuggingFace (Qwen3.6-27B / RLM-Qwen3-8B / Qwen3-Coder / etc.).
- **Operator-time investment (M001 + M004)**: preference-data curation and constitution authoring are operator-time work, not automatable. The conversation IS the work, per [Spec-Driven Convergence Lesson](../../../lessons/01_drafts/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md).

## Mission Framing — A Candidate Substitutable Axis or 5th Layer

The wiki's [Anti-Vendor-Lock-In Lesson](../../../lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) is empirical at 4 layers (trust × orchestrator × harness × provider). This epic delivers a candidate **5th** layer OR a candidate **substitutable axis WITHIN the provider layer** — operator decides:

- **Option A — Substitutable axis WITHIN provider layer**: operator-authored model joins the provider-layer choice set alongside Qwen3.6-27B / RLM-Qwen3-8B / Kimi K2.6 / AICP routing. Provider layer becomes substitutable on `vendor-supplied vs operator-authored`. Compact lesson.
- **Option B — 5th substitutable layer (model-customization / operator-authored-tier)**: operator-authored is structurally distinct from vendor-supplied because training data + alignment data + behavioral constitution are operator-controlled. Substitutability axes within: open-weight base · fine-tune method (LoRA / full / DPO / IPO / KTO) · preference-data source · constitution authoring · evaluation gate · base-model substitution (Qwen3 / Llama / DeepSeek). Acknowledges the strategic-tier scope.

**Default proposal: Option B**, reflecting the operator's framing of this as *"massive project, really long"*. Operator confirms in M006.

## Open Questions (operator design calls)

> [!question] Single bundled epic, or split into 2–3 sub-epics by phase?
> Phases 0–3 (toolchain → first LoRA → group expansion) could be one epic; Phases 4–5 (intelligence layer + behavioral preference fine-tune) a second; Phases 6–7 (composition + ecosystem) a third. Or single bundled (this proposal). Single is simpler; split allows independent priority/scheduling. Operator-decision.

> [!question] First specialist LoRA — base model choice for `v0.1-seed`?
> Candidates: (a) Qwen3.6-27B at UD-IQ2 (proven senior-engineer-tier; fits 24 GB VRAM); (b) RLM-Qwen3-8B (RLM-substrate-aware; smaller; recursive-paradigm-trained); (c) Qwen3-Coder family (purpose-built for coding); (d) merge of multiple via TIES. Operator picks based on workload class.

> [!question] MoE-as-architecture vs Mixture-of-LoRAs — pick one or both?
> Pattern (1) MoE-architecture: pick existing MoE base (Mixtral · DeepSeek V3 · Qwen3-30B-A3B), fine-tune. Pattern (2) Mixture-of-LoRAs: small specialized LoRAs composed via routing. Pattern (2) is operator-feasible on RTX 3090; Pattern (1) larger-infrastructure. Both can coexist (LoRA over MoE base).

> [!question] "Information virus" propagation channel — distribution mechanism?
> Options: (a) bundled with each sister project's `setup --connect`; (b) Multica-deployable artifact (any harness routes to it); (c) HuggingFace publish (`cyberpunk042/operator-tier-coding-v0.1` etc.); (d) operator-internal only. Operator-decision per workload class and openness preference.

> [!question] Behavioral constitution — single document or per-domain split?
> Operator's *"core"* could be one document (parallels CLAUDE.md scope) or split per domain (coding-tier · methodology-tier · debugging-tier). Wiki uses layered split. Constitution-as-Markdown follows precedent.

> [!question] Behavior-test pass-rate threshold for `v0.5-growing` and `v1.0-validated`?
> Operator-decision. Suggested: ≥80% on held-out hack-vs-right pairs for `v0.5-growing`; ≥95% + multi-week stability + sister-project consumer satisfaction for `v1.0-validated`. Operator confirms.

> [!question] Pain-point reduction metric — what counts as "shouldn't be so long and hard or repetitive"?
> Candidates: time-to-first-quality-output on fresh-environment session start (Opus 4.x baseline vs custom model group); per-session repeated-correction count; alignment-recovery turn count after deviation. Operator picks the canonical metric in M006.

> [!question] root-ghostproxy as the first non-wiki integration consumer?
> The triggering project (operator: *"trying to start working on a new project... root-ghostproxy"*) is a natural first consumer. Validates the "information virus" propagation in a concrete deployment. Operator-decision; depends on root-ghostproxy registration in `sister-projects.yaml` (operator-decision separately).

> [!question] Mission claim — Option A (substitutable axis) or Option B (5th layer)?
> See Mission Framing section above. Default proposal: Option B. Operator confirms in M006.

## Relationships

- IMPLEMENTS: [[post-anthropic-self-autonomous-stack|Milestone — Post-Anthropic Self-Autonomous Stack]] — extends mission with custom-model strategic-tier scope
- BUILDS ON: [[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Concept — Custom-Tailored Senior-Engineer-Tier Model Group + Recreated Intelligence Layer]] — design ground truth
- BUILDS ON: [[[[E012-custom-model-library-unsloth-loras|E012 — Custom Model Library (Unsloth LoRAs)]] — nests E012's tactical deliverables as components]]
- BUILDS ON: [[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]] — adds senior-engineer-tier + behavioral-alignment + intelligence-layer dimensions
- BUILDS ON: [[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]] — composes via L0–L4 opt-ins
- BUILDS ON: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — adds candidate Evidence 12
- BUILDS ON: [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Convergence Lesson]] — model-creation workflow as the 9th instance
- BUILDS ON: [[model-markdown-as-iac|Model — Markdown as IaC]] — extended to Python-as-programming hyperstructure
- BUILDS ON: [[src-rlm-recursive-language-models-mit-oasys|RLM Synthesis]] — `mit-oasys/rlm-qwen3-8b-v0.1` is a customization-on-open-weight-base instance
- BUILDS ON: [[src-prime-intellect-prime-rl-async-rl-training-at-scale|prime-rl Synthesis]] — Apache 2.0 training framework
- BUILDS ON: [[src-unsloth-fast-lora-consumer-hardware|Unsloth Synthesis]] — consumer-hardware fine-tune substrate
- BUILDS ON: [[src-qwopus-claude-opus-reasoning-distilled-qwen-27b|Qwopus Synthesis]] — distillation precedent
- BUILDS ON: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] — RTX 3090 incoming hardware reality
- DEPENDS ON: [[post-anthropic-stack-3-layer-assembly-multica-aicp-3090|Epic — Post-Anthropic 3-Layer Stack Assembly]] — provides orchestrator × harness × provider layers
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — behavioral alignment in the weights is infrastructure
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]] — constitution + preference data + per-LoRA SPECs are structured context
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — every behavioral claim aspirational until held-out evaluation confirms it
- DEMONSTRATES: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] — wiki methodology applied to model-creation workflow
- FEEDS INTO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] — adds custom-model dimension as a structural decision axis
- RELATES TO: [[adopt-multica-as-orchestrator-layer-post-anthropic-stack-2026-04|Decision — Adopt Multica]] — Multica routes to the custom model group
- BUILDS ON: [[end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers|Multi-Layer Compression Lesson]] — 14 mechanisms across 6 layers; M005 (Trust + Compression Composition) realizes the multi-layer compounding empirically
- BUILDS ON: [[quality-per-position-compounds-quantity-per-position-diminishes-convergent-pattern|Quality-per-Position Lesson]] — M004 (Behavioral Preference Fine-Tune) operator strategy is the 6th instance of this convergent pattern; better preference-pair quality > larger base-model parameter count
- BUILDS ON: [[mcp-discipline-register-only-what-is-referenced-and-actually-used-not-pre-emptive|MCP Discipline Lesson]] — M003 (Recreated Intelligence Layer) MCP catalog must satisfy 3-predicate test; pre-emptive MCP registration violates the discipline
- BUILDS ON: [[path-versatility-doctrine-metadata-driven-indirection-not-hardcoded-absolute-paths|Path-Versatility Doctrine Lesson]] — M001 (Toolchain) configs must use env-indirection; cross-machine portability for the model-customization workflow
- RELATES TO: [[src-google-tpu-dflash-diffusion-style-speculative-decoding-3x-speedup-2026-05-04|DFlash TPU Synthesis]] — M003 inference-speed substrate option (when NVIDIA torchax port lands)
- RELATES TO: [[src-philschmid-four-subagents-patterns-2026-inline-fanout-pool-teams|Phil Schmid Subagent Patterns Synthesis]] — M003 orchestration-pattern substitutability quartet (P1 → P4)
- RELATES TO: [[src-claude-code-skill-chaining-fork-files-commands-85-percent-less-context|Claude Code Skill Chaining Synthesis]] — production-validated implementation of Pattern 1 (Inline Tool with isolated context)
- RELATES TO: [[src-quantization-280gb-model-on-laptop-outliers-as-central-villain-and-five-algorithms|Quantization Synthesis]] — M002 specialist LoRA algorithmic foundation

## Backlinks

[[Milestone — Post-Anthropic Self-Autonomous Stack]]
[[custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis|Concept — Custom-Tailored Senior-Engineer-Tier Model Group + Recreated Intelligence Layer]]
[[E012 — Custom Model Library (Unsloth LoRAs)]]
[[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]]
[[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]]
[[Anti-Vendor-Lock-In Lesson]]
[[Spec-Driven Convergence Lesson]]
[[Model — Markdown as IaC]]
[[RLM Synthesis]]
[[prime-rl Synthesis]]
[[Unsloth Synthesis]]
[[Qwopus Synthesis]]
[[2026 Consumer Hardware AI Stack]]
[[Epic — Post-Anthropic 3-Layer Stack Assembly]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[Decision — Adopt Multica]]
[[Multi-Layer Compression Lesson]]
[[Quality-per-Position Lesson]]
[[mcp-discipline-register-only-what-is-referenced-and-actually-used-not-pre-emptive|MCP Discipline Lesson]]
[[Path-Versatility Doctrine Lesson]]
[[src-google-tpu-dflash-diffusion-style-speculative-decoding-3x-speedup-2026-05-04|DFlash TPU Synthesis]]
[[src-philschmid-four-subagents-patterns-2026-inline-fanout-pool-teams|Phil Schmid Subagent Patterns Synthesis]]
[[src-claude-code-skill-chaining-fork-files-commands-85-percent-less-context|Claude Code Skill Chaining Synthesis]]
[[Quantization Synthesis]]
