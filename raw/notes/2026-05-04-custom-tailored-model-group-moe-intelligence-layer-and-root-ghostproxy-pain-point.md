# 2026-05-04 — Custom-Tailored Model Group (MoE + Intelligence Layer) + root-ghostproxy Triggering Pain Point

> Verbatim operator directive log — Hard Rule #4 + AGENTS.md Hard Rule #3. Logged BEFORE acting.

## Verbatim Operator Directive (Sacrosanct)

> *"continue.. also I realize I really am going to need to find and customize my own model.. I think the models in genral lack a core that bring way more intelligence to the model and make it adapted to a real senior software engineer instead of a newbe and by the same way extract way more power and reliability from it."*

> *"most model try to do both ends at the same time and end up achieing both mediocer ... My goal would be to really tailing it to my need and knowledge and proned ways and high standards and Adding my core to it. An AI that not longer try to hack or rush or quickfix things but naturally WANT to do things right and follow the right methodologies and ways to do things."*

> *"Of course it will have multiple versions. but we want to act potentially like both an information virus if you will and also front and out interfaces and possibly a little of middlewares shaping and integrations."*

> *"this will be part of this project, it will be a massive project and we will need to be ready and it will be really long."*

> *"I was for instant on a new machine (non-GUI) debian 13 and I was trying to start working on a new project and I re-realize how a model like opus 4.x can be so potent and yet so trap and low quality at time..."*

> *"That's it hard to achieve the desired quality and on this machine I have the system level config and so many things including the project(s) itself but as much as I can configure the harness more and ecosystem and the project itself.. it takes time before getting started... there are things that shouldn't have to be so long and hard or repeatitive and hard to make the AI align to."*

> *"THE pain point must be itentified with their root and thus we can find the possible solution at the right place."*

> *"The project is called root-ghostproxy and its a new type of project but its IAC and its basically a IPS sitting in between the Edge firewall (OPNSense) and the first switch / the local network. its  aiming to secure an OS and configure claude code and opencode at the root with all the safety needed. it will do this and it will also offer in the future to for instance we use this machine or another [new] one. So its not just an IPS its a system AI safety setup project and the IPS tools (suricata and [polarproxy]) as modules."*

> *"It made me realize all this but clearly its not a model... we probalby need to find our find Group of MoE models of various sizes and needs and we create an intelligence layer... we recreate intelligence at the layers needed. in and out. and we use python and turn thing into proto-programming or proto proto-programming / structure and hyperstructure and exploiting the latest possibilites and adapting to the requirements of the set configuration and so on."*

> *"Its not as if I was mastering AI model creation yet... nor will I maybe but possibly my own customizations and possibly even more useful and flexible. like we teach."*

> *"with and without cypher / decypher with or without I/O Compression, etc we take our time to think things right."*

> *"continue"*

## Concept Decomposition (operator's words → technical surface)

| Operator's framing | Technical territory |
|---|---|
| "find and customize my own model" | Model customization — fine-tune / RL / DPO / IPO / continuous pre-training / merge / LoRA / hyper-LoRA |
| "models in general lack a core that bring way more intelligence" | Behavioral core / inductive bias — what the model is *biased toward* (do-things-right vs ship-fast) is shaped by training data + alignment data |
| "real senior software engineer instead of a newbe" | Tier specialization — not a single model serving both ends; senior-engineer-tier as design target |
| "extract way more power and reliability from it" | Both ends fail-mediocre framing — operator's argument is that bimodal training compresses both modes |
| "tailoring it to my need and knowledge and proned ways and high standards and Adding my core to it" | Preference data + instruction data + persona — operator's standards as the alignment signal |
| "naturally WANT to do things right and follow the right methodologies" | Behavioral alignment — DPO/IPO/RLHF with operator-curated preference pairs over hack-vs-right outputs |
| "multiple versions" | Release-line discipline — versioned model artifacts; this wiki's evolution lifecycle applies |
| "information virus" (positive sense) | Methodology propagation mechanism — model carries the wiki's principles + standards + lessons; spreads them when integrated into other projects |
| "front and out interfaces" | UI / CLI / API surface for operator interaction |
| "middlewares shaping and integrations" | Wrapper / orchestrator / integration layer between consumers and the model |
| "this will be part of this project... massive project... really long" | Wiki-internal workstream (not a sister project) — milestone-class scope |
| "Group of MoE models of various sizes and needs" | MoE composition — mixture of experts; expert specialization per task class; size variance per latency/cost target |
| "create an intelligence layer... recreate intelligence at the layers needed. in and out" | Architecture: intelligence at the I/O boundaries, not just at the model — pre-processing / routing / post-validation as layers |
| "python and turn thing into proto-programming or proto proto-programming / structure and hyperstructure" | Markdown-as-IaC extended to Python-as-programming layer; structured/hyper-structured config as the runtime contract |
| "exploiting the latest possibilites and adapting to the requirements of the set configuration" | Goldilocks — model behavior parameterized on identity / phase / scale / trust |
| "Its not as if I was mastering AI model creation yet... but possibly my own customizations and possibly even more useful and flexible. like we teach." | Realistic scope: customizations on existing open-weight models (Qwen3 / RLM-Qwen3-8B / Qwen3-Coder / Llama / etc.); the wiki teaches methodology — apply it to the model-creation workflow itself |
| "with and without cypher / decypher with or without I/O Compression" | Composes with the [Trust-Layer Epic](../../wiki/backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md) — the L0–L4 opt-ins layer onto this model group; cypher / compression are independently togglable |

## Pain-Point Decomposition (the trigger event)

| Operator's framing | Technical territory |
|---|---|
| "new machine (non-GUI) debian 13" | Fresh server-class environment; no IDE GUI; CLI-only AI agent setup |
| "trying to start working on a new project" | Net-new project bootstrap workflow |
| "opus 4.x can be so potent and yet so trap and low quality at time" | Frontier-model dual-mode behavior — high ceiling but inconsistent floor |
| "I have the system level config and so many things including the project(s) itself but as much as I can configure the harness more and ecosystem and the project itself.. it takes time before getting started" | Even with full layered config (system + harness + project), AI alignment time-to-quality remains painful |
| "there are things that shouldn't have to be so long and hard or repeatitive and hard to make the AI align to" | Repetition cost is itself a quality signal — when alignment is repetitive, the alignment substrate is wrong, not the operator's persistence |
| "THE pain point must be itentified with their root and thus we can find the possible solution at the right place" | Operator's standing root-cause discipline — *"fix it at the root instead.. its not hard"* (CLAUDE.md sacrosanct directive) |

## root-ghostproxy (new project — context)

Operator named a new project not yet in `sister-projects.yaml`:

| Dimension | Operator's words / framing |
|---|---|
| Name | `root-ghostproxy` |
| Type | "new type of project but its IAC" — IaC-based |
| Architecture | "IPS sitting in between the Edge firewall (OPNSense) and the first switch / the local network" |
| True purpose | "not just an IPS its a system AI safety setup project" — secure OS + configure Claude Code + OpenCode at root level with all safety needed |
| IPS tools | `suricata` + `[polarproxy]` as **modules** (not the project itself) |
| Scope | Deployable to "this machine or another [new] one" — multi-host capable |

Status: operator-named, not yet a registered sister project in this wiki. Adding to `sister-projects.yaml` is operator-decision, not auto.

## Composition with Existing Mission Layers

The custom-tailored model group composes naturally with the wiki's prior mission claims:

| Existing layer | How custom model composes |
|---|---|
| **Trust** ([Trust-Layer Epic](../../wiki/backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md)) | Custom model can be deployed at any L0–L4 trust opt-in — operator chooses cypher/decypher/compression per workload |
| **Orchestrator** (Multica) | Multica can route to the custom model alongside other providers via `custom_env` |
| **Harness** (Claude Code · OpenCode · Codex · etc.) | The custom model is harness-agnostic — same surface |
| **Provider** (AICP routing across Ollama Cloud / OpenRouter / direct) | The custom model becomes a *provider* in AICP's routing — but distinct in that it's *operator-authored*, not vendor-supplied |

Open question (operator-decision): does custom model add a 5th substitutable layer (e.g., model-customization / operator-authored-tier) to the anti-vendor-lock-in mission claim, OR is it a substitutable axis WITHIN the provider layer (operator's-own-model as one provider option)?

## Connection to Convergent Pattern (8-instance Layer-4 lesson)

The [spec-driven convergence lesson](../../wiki/lessons/01_drafts/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md) names *the wiki itself* as one of the 8+ instances. The model-creation workflow is itself a candidate spec-driven build:
- The model-version specs would be Markdown artifacts (six-file pattern + per-version specs)
- The "core" the operator adds is preference data + instruction data — both are version-controlled artifacts
- Closed-loop sync rule applies: when the model deviates from operator's standards, fix the spec (preference data / instruction data) first, then re-train

Operator's *"like we teach"* names this directly — the wiki's methodology applied to the model-creation workflow.

## Initial Research Direction

### In-project (already known here)

| Source | Why it grounds the operator's design |
|---|---|
| [src-rlm-recursive-language-models-mit-oasys](../../wiki/sources/tools-integration/src-rlm-recursive-language-models-mit-oasys.md) | Script-orientation substrate · `mit-oasys/rlm-qwen3-8b-v0.1` is a customized open-weight checkpoint (post-trained 8B reaches frontier on 3/4 long-context tasks) |
| [src-rlm-paper-deep-dive-table-1-training-recipe-six-observations](../../wiki/sources/tools-integration/src-rlm-paper-deep-dive-table-1-training-recipe-six-observations.md) | Training-recipe deep-dive — *what changes* between base Qwen3-8B and RLM-Qwen3-8B |
| [src-prime-intellect-prime-rl-async-rl-training-at-scale](../../wiki/sources/tools-integration/src-prime-intellect-prime-rl-async-rl-training-at-scale.md) | Training framework — Apache 2.0 · 48 H100 hours (~$48–100 cloud rental) for the RLM-Qwen3-8B post-train · IPO + Kimi-K2.5 KL default loss · custom-loss support via `loss.type=custom` |
| [src-prime-intellect-verifiers-llm-rl-environments](../../wiki/sources/tools-integration/src-prime-intellect-verifiers-llm-rl-environments.md) | Environment library for RL — verifiers + tasksets + RLMEnv |
| [src-qwopus-claude-opus-reasoning-distilled-qwen-27b](../../wiki/sources/tools-integration/src-qwopus-claude-opus-reasoning-distilled-qwen-27b.md) | Distillation precedent — Claude Opus reasoning distilled into Qwen 27B |
| [src-unsloth-fast-lora-consumer-hardware](../../wiki/sources/tools-integration/src-unsloth-fast-lora-consumer-hardware.md) | LoRA + UD-IQ2 / Q2_K — consumer-hardware fine-tune + quantization |
| [src-qwen3-6-27b-dense-beats-397b-moe-agentic-coding](../../wiki/sources/tools-integration/src-qwen3-6-27b-dense-beats-397b-moe-agentic-coding.md) | Senior-engineer-tier evidence — 27B-dense beats some 397B MoE on agentic coding (specialized > general) |
| [src-gpt-oss-architecture-shared-experts-distillation](../../wiki/sources/tools-integration/src-gpt-oss-architecture-shared-experts-distillation.md) | MoE architecture — shared experts + distillation precedent |
| [model-markdown-as-iac](../../wiki/spine/models/agent-config/model-markdown-as-iac.md) | The Markdown-as-IaC pattern operator extends to Python-as-programming hyperstructure |
| [src-cavekit-spec-driven-development-claude-code-julius-brussee](../../wiki/sources/tools-integration/src-cavekit-spec-driven-development-claude-code-julius-brussee.md) | Most-distilled spec-driven instance — minimum viable shape for the model-creation workflow |
| [Trust-Layer Epic](../../wiki/backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md) | Cypher / decypher / compression — composes with custom model |
| [Anti-Vendor-Lock-In Lesson](../../wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md) | Mission framing — custom model adds a candidate substitutable layer / axis |
| [Spec-Driven Convergence Lesson](../../wiki/lessons/01_drafts/spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts.md) | Methodology — model-creation workflow can itself be spec-driven |

### Online (research targets, secondary to in-project)

- MoE routing methods (top-k vs hash · expert imbalance handling · auxiliary loss-free routing)
- Mixture-of-LoRA composition (S-LoRA, LoRAHub, expert-LoRA per task class)
- DPO / IPO / KTO / SLiC / GRPO — preference-data fine-tuning methods (operator's "naturally want to do things right" → preference data)
- Continuous pre-training on operator-authored corpus (the wiki itself is a candidate corpus)
- Constitutional AI / Anthropic's RLAIF — alignment-by-constitution precedent for "core" injection
- Distillation from a strong model (Opus / GPT-5 / Claude) into a smaller open-weight base — operator-controlled distillation pipeline
- Model merging (TIES, DARE, slerp, task-arithmetic) — compose specialized fine-tunes
- Inference-layer intelligence: speculative decoding, contrastive decoding, prompt-time tool routing

## Provenance

- Operator session 2026-05-04 (post-handoff, post-compaction)
- Triggered by operator's experience setting up `root-ghostproxy` on a fresh non-GUI Debian 13 host
- Mission alignment: extends the post-Anthropic 4-layer empirical claim with a candidate 5th layer (model-customization / operator-authored-tier) OR enriches the provider layer with operator-authored substitutability — operator-decision

## Operator Framing Quality (registered, not contested)

Per `feedback_do_not_undermine_operator_design_assertions.md` — when operator names operational properties or asserts a design path, my role is to ground with research, not impose research-found ceilings.

| Operator framing | Stance |
|---|---|
| *"I really am going to need to find and customize my own model"* | Registered — operator owns the design intuition |
| *"models in general lack a core... try to do both ends at the same time and end up achieing both mediocer"* | Registered — operator's diagnosis of frontier-model bimodality is a design hypothesis, not contested |
| *"naturally WANT to do things right"* | Registered — behavioral-alignment goal, achievable via preference fine-tuning + curated instruction data + constitutional steering |
| *"information virus"* | Registered (positive framing) — methodology propagation mechanism, not malware |
| *"Its not as if I was mastering AI model creation yet"* | Registered — operator self-flags scope; customization-tier work, not foundation-model authoring |
| *"like we teach"* | Registered — apply the wiki's own methodology to the model-creation workflow |
| *"we take our time to think things right"* | Registered — exploratory phase, no rush to commit an architecture |

## Cross-references in this wiki

- [[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]] — composes (cypher/compression are operator-toggle-able opt-ins)
- [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — mission framing
- [[spec-driven-agentic-build-is-the-2026-convergent-pattern-prompts-are-first-class-artifacts|Spec-Driven Convergence Lesson]] — methodology applied to model-creation workflow
- [[model-markdown-as-iac|Model — Markdown as IaC]] — extended to Python-as-programming hyperstructure
- [[src-rlm-recursive-language-models-mit-oasys|RLM Synthesis]] — script-orientation substrate; mit-oasys/rlm-qwen3-8b-v0.1 IS an instance of operator-authored customization on open-weight base
- [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] — RTX 3090 incoming (mid-May 2026) is the realistic training-target hardware for L2-tier customizations
