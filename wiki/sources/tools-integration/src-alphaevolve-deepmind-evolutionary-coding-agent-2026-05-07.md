---
title: "Synthesis — AlphaEvolve (Google DeepMind, May 2025 launch → May 7 2026 one-year scaling update → Dec 9 2025 Google Cloud private preview): Gemini-powered evolutionary coding agent that pairs Gemini Flash (breadth) + Gemini Pro (depth) with user-defined automated evaluators and an evolutionary loop over a program-population to discover algorithms that outperform expert-written baselines — moves from research curiosity to production substrate inside Google (Borg scheduling +0.7% global compute recovery, +23% on a key Gemini training kernel → 1% total Gemini training-time reduction, FlashAttention +32.5%, Spanner LSM-tree write-amp −20%, software storage footprint −9%, TPU arithmetic-circuit redesign integrated into next-gen silicon) and across external partners (Klarna 2× transformer training speed; Substrate multi-fold lithography simulation; FM Logistic +10.4% TSP routing; WPP +10% campaign-model accuracy; Schrödinger ~4× MLFF train+infer speedup; PacBio DeepConsensus −30% variant-detection errors; Earth-AI natural-disaster prediction +5%; AC Optimal Power Flow 14%→88% feasible solutions; quantum-circuit error 10× lower on Willow; Erdős-problem progress with Tao; 4×4 complex matrix multiplication in 48 scalar multiplications, beating Strassen 1969; kissing-number lower bound advanced in 11 dimensions; ~75% rediscovery + ~20% improvement on 50+ open mathematical problems) — productized via the AlphaEvolve Service API on Google Cloud (private preview, Dec 9 2025; ongoing Early Access program); strategic-impact event for this project's vision: introduces an 'agentic algorithm-discovery' tier ABOVE the agentic-coding-harness tier (Claude Code / Codex / OpenCode / Gemini CLI / etc.), where the deliverable is not 'completed task' but 'better algorithm discovered + production-deployed', and Google is the first vendor to formalize that tier as a cloud API"
type: source-synthesis
domain: tools-and-platforms
status: synthesized
confidence: high
maturity: seed
layer: 1
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: deepmind-alphaevolve-launch-2025-05-14
    type: article
    url: https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
    file: raw/articles/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms-goog.md
    description: "Google DeepMind launch announcement (AlphaEvolve team, 2025-05-14). Defines AlphaEvolve as an evolutionary coding agent using a Gemini Flash + Gemini Pro ensemble with automated evaluators and an evolutionary framework over a program population. Documents production deployments at Google: Borg data-center scheduling (continuously recovering 0.7% of worldwide compute resources for >1 year), Verilog rewrite of a matrix-multiplication arithmetic circuit integrated into an upcoming TPU, +23% on a Gemini training kernel (1% total Gemini training-time reduction), +32.5% on FlashAttention low-level GPU kernel. Mathematical results: 4×4 complex matrix multiplication in 48 scalar multiplications (beats Strassen 1969 — and AlphaTensor's previous best only worked for binary arithmetic in this setting); ~75% state-of-the-art rediscovery and ~20% improvement on 50+ open problems in analysis/geometry/combinatorics/number theory; kissing-number new lower bound in 11 dimensions (configuration of 593 outer spheres). Strategically frames AlphaEvolve as 'beyond single-function discovery to evolve entire codebases.'"
  - id: deepmind-alphaevolve-impact-2026-05-07
    type: article
    url: https://deepmind.google/blog/alphaevolve-impact/
    file: raw/articles/alphaevolve-gemini-powered-coding-agent-scaling-impact-across-fields-google-deep.md
    description: "Google DeepMind one-year-anniversary scaling update (AlphaEvolve team, 2026-05-07). Catalogues impact across (a) social/sustainability — PacBio DeepConsensus −30% variant-detection errors, AC Optimal Power Flow feasibility 14%→88%, Earth-AI natural-disaster prediction +5%; (b) frontier research — Willow quantum-circuit error 10× lower than conventional optimization, Erdős-problem progress with Terence Tao (UCLA), record TSP lower bounds, record Ramsey-number lower bounds, neuroscience-model interpretability, microeconomics market-limit proofs, neural-net building blocks, privacy cryptography, synthetic data generation, frontier-AI safety mitigations; (c) Google AI infrastructure — TPU circuit design integrated into silicon (Jeff Dean quote: 'TPU brains helping design next-generation TPU bodies'), cache-replacement-policy discovery (2 days vs months human effort), Spanner LSM-tree compaction heuristics −20% write amplification, software storage footprint −9%; (d) commercial enterprises via Google Cloud — Klarna 2× transformer training speed + improved quality, Substrate computational-lithography multi-fold runtime speedup, FM Logistic +10.4% TSP routing efficiency (>15,000 km/yr saved), WPP +10% campaign-model accuracy, Schrödinger ~4× MLFF train+infer speedup. Positions AlphaEvolve as 'a versatile, general-purpose system' graduating from pilot to core component."
  - id: google-cloud-alphaevolve-private-preview-2025-12-09
    type: article
    url: https://cloud.google.com/blog/products/ai-machine-learning/alphaevolve-on-google-cloud
    file: raw/articles/alphaevolve-on-google-cloud-google-cloud-blog.md
    description: "Google Cloud Blog (Vladimir Vuskovic, Dir Product Mgmt, Google Cloud + Anant Nawalgaria, Group AI PM/Eng, Google; 2025-12-09). The productization vector: AlphaEvolve Service API launched in private preview on Google Cloud via an Early Access Program (customers contact their Google Cloud Representative to participate). Operating model is documented: (1) customer-defined problem specification + evaluation logic + seed initialization program (compile-ready, sub-optimal); (2) Gemini Flash + Gemini Pro mutate code → 'population space'; (3) evolutionary algorithms select crossover/mutation parents; (4) ground-truth evaluator decides whether a child replaces parent — feedback loop iterates until convergence. Target industries explicitly enumerated: biotech/pharma (molecular-simulation algorithm optimization → shorter drug-discovery timelines), logistics/supply chain (routing + inventory heuristics), financial services (algorithmic risk models for complex portfolio management), energy (smart-grid load-balancing + renewable integration). Frames the offering as 'for complex optimization problems you can define in code and objectively measure.'"
tags: [alphaevolve, google-deepmind, gemini, gemini-flash, gemini-pro, evolutionary-coding-agent, algorithm-discovery, agentic-coding, google-cloud, tpu, borg, flashattention, spanner, klarna, schrodinger, fm-logistic, wpp, substrate, pacbio, willow-quantum, kissing-number, ramsey-numbers, traveling-salesman, terence-tao, matrix-multiplication, strassen, ac-optimal-power-flow, earth-ai, deepconsensus, lsm-tree, "2025-05-14", "2025-12-09", "2026-05-07", source-synthesis, "2026-05-15", frontier-delta-2026-05-15, vision-relevant-agent-runtime, vision-relevant-tools-platforms, agentic-algorithm-discovery]
---

# AlphaEvolve — Google DeepMind Evolutionary Coding Agent, Three-Anchor Synthesis (May 2025 launch → Dec 9 2025 Cloud preview → May 7 2026 one-year impact update)

> [!info] Reference Card
>
> | Field | Value |
> |---|---|
> | **System name** | AlphaEvolve |
> | **Vendor / lab** | Google DeepMind (developed jointly with Google Research; productized via Google Cloud) |
> | **Initial public announcement** | 2025-05-14 (DeepMind blog) |
> | **Cloud productization** | 2025-12-09 — AlphaEvolve Service API, private preview, Google Cloud Early Access Program |
> | **One-year impact update** | 2026-05-07 (DeepMind blog) |
> | **Model substrate** | Ensemble: Gemini Flash (breadth/speed) + Gemini Pro (depth) |
> | **Agent paradigm** | Evolutionary coding agent over a population of candidate programs |
> | **User-supplied inputs** | (1) problem specification (2) evaluation logic / "ground truth" evaluator (3) seed program (compile-ready, sub-optimal) |
> | **Loop** | Mutate (LLM ensemble) → Score (evaluator) → Select (evolutionary algorithm) → Repeat |
> | **Deliverable type** | A better algorithm (code), not a "completed task" — distinguishing feature vs Claude Code / Codex / Gemini CLI |
> | **Google internal compute recovery** | +0.7% global compute (Borg scheduling), continuously, >1 year |
> | **Gemini training speedup** | +23% on a vital kernel → 1% total Gemini training-time reduction |
> | **FlashAttention speedup** | +32.5% on GPU kernel implementation |
> | **TPU impact** | Verilog rewrite of arithmetic circuit integrated into next-gen TPU silicon |
> | **Spanner impact** | LSM-tree compaction heuristics → −20% write amplification |
> | **Software footprint** | −9% via new compiler optimization strategies |
> | **Cache-replacement policies** | Discovered in 2 days vs months of human effort |
> | **PacBio DeepConsensus** | −30% variant-detection errors |
> | **AC Optimal Power Flow (GNN)** | Feasible-solution rate 14% → 88% |
> | **Earth-AI natural-disaster prediction (20 categories)** | +5% accuracy |
> | **Willow quantum circuits** | 10× lower error than conventional optimization |
> | **Klarna (financial services)** | 2× transformer training speed + quality improvement |
> | **Substrate (semiconductor lithography)** | multi-fold runtime speedup |
> | **FM Logistic (TSP routing)** | +10.4% efficiency, >15,000 km/yr saved |
> | **WPP (advertising)** | +10% campaign-model accuracy |
> | **Schrödinger (MLFF train+infer)** | ~4× speedup |
> | **Matrix-multiplication record** | 4×4 complex matrices in 48 scalar mults (beats Strassen 1969; AlphaTensor only matched in binary) |
> | **Open-problem performance** | ~75% state-of-the-art rediscovery + ~20% improvement across 50+ problems |
> | **Notable theorem-class wins** | Kissing number (n=11): new lower bound, 593 outer spheres; TSP lower bound; Ramsey number lower bound; Erdős-problem progress (Tao collaboration) |
> | **Strategic positioning** | First cloud-API offering for "agentic algorithm discovery" — a tier *above* agentic-coding-harness |
> | **Access model** | Private preview via Google Cloud Representative; not self-serve |

## Summary

**AlphaEvolve is a Gemini-powered evolutionary coding agent productized by Google.** Across three anchor sources spanning twelve months — DeepMind's 2025-05-14 launch, the 2025-12-09 Google Cloud private-preview announcement, and DeepMind's 2026-05-07 one-year scaling update — a consistent picture emerges of a system that is **categorically different** from the agentic-coding harnesses currently catalogued in this project's research wiki (Claude Code, Codex, OpenCode, Aider, Cline, Cursor, Gemini CLI, Continue, Crush, Goose — see `wiki/sources/tools-integration/src-agentic-coding-harness-landscape-2026.md`).

The distinction is what the agent *produces*. Harnesses produce **completed tasks** (a PR, a bug-fix, a feature) within a single session's context. AlphaEvolve produces **better algorithms** — artifacts that subsequently run in production, optimize compounding workloads, and themselves become the substrate for the next generation of mutations. The operating loop is: customer provides (1) a problem spec, (2) a deterministic evaluation function, and (3) a seed program that compiles and solves the problem sub-optimally; an ensemble of Gemini Flash (breadth) and Gemini Pro (depth) mutates the seed into many candidate children; the evaluator scores them; an evolutionary selection step picks parents for the next round; and the cycle iterates until convergence. The crucial difference from prompt-driven coding harnesses is that **the human supplies the ground-truth evaluator, not the human-in-the-loop steering of the agent** — the agent runs autonomously across a population of mutations and converges on what the evaluator validates as objectively better.

The impact catalogue in the May 7 2026 update is the data point that elevates this from "interesting research demo" to "vision-relevant strategic event." At Google: AlphaEvolve's outputs are now in production in Borg's data-center scheduler (+0.7% global compute recovery, continuously, for over a year), in Gemini's training kernels (+23% on a key kernel, 1% total training-time reduction — material at frontier scale), in the FlashAttention GPU-kernel path (+32.5%), in Spanner's LSM-tree compaction heuristics (−20% write amplification), in software-storage footprints (−9%), and — most strikingly — embedded directly into the silicon of the next-generation TPU via an AlphaEvolve-proposed Verilog rewrite. Jeff Dean's framing in the blog ("TPU brains helping design next-generation TPU bodies") is not marketing rhetoric; it is the literal description of a closed loop in which a Gemini-driven agent is now part of the design pipeline for the hardware that trains Gemini. Outside Google: a credible cross-industry portfolio — Klarna (2× transformer training speed), Substrate (multi-fold lithography simulation), FM Logistic (+10.4% TSP routing efficiency, 15,000 km/yr saved), WPP (+10% campaign accuracy), Schrödinger (~4× MLFF train+infer), PacBio (DeepConsensus −30% variant errors). The Cloud-Blog productization vector (2025-12-09) explicitly enumerates target industries (biotech/pharma, logistics, financial services, energy) and offers an "AlphaEvolve Service API" in private preview, accessible only through customer-representative gating rather than self-serve sign-up.

For this project's stored vision, three things shift: (1) the **agent-runtime taxonomy** must add a tier above "agentic coding harness" — call it *agentic algorithm discovery*, where the deliverable is a production-deployable algorithm and the steering signal is a programmatic evaluator rather than NL turns; (2) the **Google strategic position** is no longer "Gemini CLI is roughly comparable to Claude Code" — Google has built a uniquely productized offering at a tier no other vendor currently occupies, and the cloud-API gating is itself a competitive moat (you have to be a Google Cloud customer with a problem big enough that a Google Cloud Rep takes the call); (3) the **frontier-model-tier comparison** is now incomplete unless agent-system-around-the-model is included as a dimension — Gemini Pro + Flash inside AlphaEvolve produces outcomes that no single-model API call into Opus 4.7, GPT-5.5, or even Mythos Preview can match, because the evolutionary loop + evaluator are doing as much work as the underlying LLM.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source 1  | DeepMind blog — launch (AlphaEvolve team, 2025-05-14) |
> | Source 2  | DeepMind blog — one-year impact (AlphaEvolve team, 2026-05-07) |
> | Source 3  | Google Cloud Blog — private preview (Vuskovic + Nawalgaria, 2025-12-09) |
> | Type      | vendor announcement × 3 (1 lab launch + 1 lab update + 1 cloud-product launch — all primary) |
> | Key claim | A Gemini-Flash + Gemini-Pro ensemble inside an evolutionary loop with customer-supplied evaluators has graduated from research demo to production substrate at Google (Borg, TPU silicon, Gemini-training kernels, Spanner, FlashAttention) and to a private-preview cloud API offered to external enterprises with documented gains in financial services, logistics, semiconductors, life sciences, and earth science |

## Key Insights

> [!abstract] AlphaEvolve defines a new agent-runtime tier: *agentic algorithm discovery*

The agentic-coding-harness landscape (`src-agentic-coding-harness-landscape-2026.md`) catalogues systems whose interface is a human NL turn and whose deliverable is a completed task. AlphaEvolve's interface is **three artifacts** — problem spec, evaluator, seed program — and its deliverable is **a better algorithm**. This is not a more-capable harness; it is a different category of system, where the human is the spec-author and evaluator-author and the agent runs unattended over thousands of mutations. The closest prior art is the 2023 FunSearch result (also DeepMind) that AlphaEvolve generalizes from single-function discovery to whole-codebase evolution. No other major vendor (Anthropic, OpenAI, Mistral, DeepSeek, Moonshot, Alibaba) has a publicly announced cloud-API equivalent as of 2026-05-15.

> [!abstract] The Gemini Flash + Gemini Pro ensemble is the structural innovation, not the headline

Most agent-runtime stories of 2025–2026 are about a single model + better scaffolding. AlphaEvolve is **explicitly architected around two models with different roles** — Flash for breadth (maximize idea-space exploration cheaply), Pro for depth (provide insightful improvements on promising directions). This validates a pattern the project should track separately: **role-specialized model ensembles inside an agent loop**, distinct from sequential model-routing (where one model "picks" then another "executes") and from mixture-of-experts (which is internal to a single model). The pattern has implications for the cost/latency/quality decision matrix in `wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md` — if Flash+Pro ensembles measurably outperform single-Pro on long-horizon algorithm-discovery tasks, the matrix needs an ensemble-vs-single column.

> [!abstract] The "self-improving infrastructure" loop is now demonstrably closed at Google

AlphaEvolve produced (a) a 23% speedup on a Gemini-training kernel, (b) a TPU arithmetic-circuit rewrite shipped into next-gen silicon, and (c) Borg-scheduling heuristics recovering 0.7% of global compute. Each of these reduces the cost or accelerates the training of the next Gemini, which improves the next AlphaEvolve, which optimizes more infrastructure. This is the **first documented closed loop** in which a publicly described agent system is materially compounding the capability of its own substrate. The Jeff Dean "TPU brains helping design next-generation TPU bodies" quote is the operator-readable version of this claim. The project's stored vision should track this as a distinct concept: **self-improving AI-infrastructure flywheel**.

> [!abstract] Productization gate is a moat, not a bottleneck

Google has chosen to expose AlphaEvolve only through an Early Access Program gated by a customer's Google Cloud Representative — not as a self-serve console SKU. This is a strategic choice: each engagement requires Google to co-design the evaluator with the customer, which (a) generates high-margin services revenue, (b) creates a strong customer-success motion that prevents implementation failure from poisoning the brand, and (c) prevents competitors from learning about specific customer problem-formulations. The closest analog is OpenAI's "frontier red-teaming partner" model for Mythos-tier preview (per Anthropic) — both vendors are now using **selective access as a feature**, not a temporary capacity constraint. This shift has implications for the project's vendor-policy tracking: pricing pages no longer tell the full story; the most strategically important capabilities are now gated by relationship rather than by tier.

> [!abstract] The evaluator becomes the new "prompt"

In a harness, the prompt is the steering signal. In AlphaEvolve, the **evaluation function** is. Writing a good evaluator is now a high-leverage skill: it must be deterministic, fast enough to run thousands of times, faithful to the actual production objective, and resistant to gaming (an evolutionary system will reliably find any specification gap and exploit it). This is a knowledge-management opportunity for this project — patterns of "evaluator design for evolutionary coding agents" will be highly valuable, and there is currently no comparable corpus. The Schrödinger MLFF case (4× speedup) and the FM Logistic TSP case (+10.4% routing) suggest the evaluator-design playbook is non-trivial and partner-specific — Google's customer-rep-gated rollout is partly evaluator-engineering services in disguise.

## Affected pages / claims in this wiki

The following existing pages contain claims or comparison tables that AlphaEvolve's existence calls into question or extends. These are **flagged**, not silently edited — operator reviews:

1. **`wiki/sources/tools-integration/src-agentic-coding-harness-landscape-2026.md`** — does not include AlphaEvolve. Should be extended with a clarifying note that AlphaEvolve occupies a *category above* the harness landscape (different deliverable type, different interface, different access model). A cross-reference is the minimum; a comparison-table extension may be warranted.

2. **`wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md`** — currently treats model × provider × harness as a 3-axis decision. AlphaEvolve adds a fourth implicit axis: **agent-system class** (single-model harness vs role-specialized model ensemble vs evolutionary loop with evaluator). Worth flagging that the matrix is now under-dimensioned for an emergent class of workloads.

3. **`wiki/spine/references/ai-infrastructure-decision-framework-2026.md`** — Google's positioning is now non-obvious. For "complex optimization problems definable in code with measurable objectives," AlphaEvolve is the only first-party option from a major vendor. The framework's "when to choose which vendor" guidance should call this out for the relevant industry categories (biotech/pharma, logistics, financial services, energy).

4. **Any backlog task that compares Gemini CLI vs Claude Code vs Codex** — those comparisons should explicitly note they apply to *agentic coding harnesses* and not to Google's full agent-system portfolio (which now includes AlphaEvolve at a tier above).

5. **Lesson candidates** — see "Promotion candidates" section.

## Promotion candidates (for operator-decision-queue.md)

Per AUTONOMY.md the assistant proposes, operator decides. Promotion floor (lessons): ≥3 convergent existing wiki sources.

- **Candidate lesson — *Agentic-algorithm-discovery is a category above agentic-coding-harness* —** convergence count to be verified: this synthesis (1), plus the harness landscape synthesis (2 — comparison anchor), plus any neuro-symbolic / FunSearch-class prior reference if it exists in corpus (3). Operator should confirm the third anchor before promotion.
- **Candidate concept (pattern) — *Role-specialized model ensembles inside an agent loop (Flash-breadth + Pro-depth)* —** this synthesis is the only documented anchor in corpus right now; further convergent sources required before promotion.
- **Candidate concept — *Self-improving AI-infrastructure flywheel* —** AlphaEvolve is the first publicly documented closed-loop case (TPU silicon + Gemini kernel + Borg scheduling). Surface as a watch-item; do not promote on a single anchor.

## Open questions / research-gaps surfaced

- Is the AlphaEvolve Service API priced per evolutionary-run, per evaluator-invocation, or per outcome? Cloud Blog does not disclose. Worth tracking.
- What is the per-customer engagement model (does Google Cloud co-engineer the evaluator)? Inferred yes but not stated.
- Is there a public list of Early Access customers beyond the four named (Klarna, Substrate, FM Logistic, Schrödinger; WPP appears in the May 7 update; PacBio is a research collaboration, not necessarily a Cloud customer)?
- Where does AlphaEvolve sit relative to Google Antigravity (Google's "agentic development platform" mentioned in the DeepMind page navigation)? Open relationship.
- Are there academic-program AlphaEvolve users beyond the Tao / Erdős-problem case, and is there a publication trail?
- How does the evaluator-gaming-resistance problem scale to less-formal domains (e.g., user-experience optimization, code-readability optimization)?

## Cross-references

- See `wiki/sources/tools-integration/src-agentic-coding-harness-landscape-2026.md` for the harness tier that AlphaEvolve sits above.
- See `wiki/sources/ai-models/src-claude-opus-4-7-anthropic-frontier-2026-04-16.md` and `wiki/sources/ai-models/src-gpt-5-5-openai-frontier-2026-04-23.md` for the frontier-model tier whose comparison-claims are now under-dimensioned without the agent-system axis.
- See `wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md` and `wiki/spine/references/ai-infrastructure-decision-framework-2026.md` for the decision frameworks that should incorporate AlphaEvolve's existence.
- See `wiki/sources/src-anthropic-effective-harnesses-long-running-agents.md` for Anthropic's parallel work on long-running agent harnesses — useful contrast: Anthropic optimizes harness-around-Claude; DeepMind builds a new agent class around Gemini.

## Relationships

- **COMPARES TO** [[src-agentic-coding-harness-landscape-2026]] — AlphaEvolve occupies a tier *above* the agentic-coding-harness category catalogued there; same domain (tools-and-platforms), different deliverable class (better algorithm vs completed task).
- **RELATES TO** [[src-claude-opus-4-7-anthropic-frontier-2026-04-16]] — frontier-model comparison context; AlphaEvolve uses Gemini Pro + Flash ensemble rather than a single frontier model.
- **RELATES TO** [[src-gpt-5-5-openai-frontier-2026-04-23]] — same comparison context; OpenAI has no announced cloud-API equivalent at AlphaEvolve's tier.
- **RELATES TO** [[src-gpt-5-5-instant-chatgpt-default-2026-05-05]] — concurrent frontier-vendor event; underscores that the strategic axis has shifted from raw-model-capability to agent-system-around-the-model.
- **EXTENDS** [[ai-model-provider-harness-decision-matrix-2026]] — adds a fourth implicit decision axis (agent-system class) to the existing model × provider × harness matrix.
- **EXTENDS** [[ai-infrastructure-decision-framework-2026]] — adds AlphaEvolve as the only first-party major-vendor option for code-defined optimization problems with measurable objectives.
- **BUILDS ON** [[src-anthropic-effective-harnesses-long-running-agents]] — parallel-but-distinct paradigm; both target long-horizon agentic work, AlphaEvolve via an evolutionary loop + evaluator rather than a tuned harness.
- **DEMONSTRATES** self-improving AI-infrastructure flywheel (concept candidate) — TPU silicon redesign + Gemini training-kernel speedup + Borg scheduling improvement form a closed loop where Gemini-driven AlphaEvolve compounds the substrate that trains the next Gemini.

## Verification status

- All numeric claims sourced to one of the three primary blog posts (DeepMind launch, DeepMind one-year update, Google Cloud private-preview announcement). All three are first-party vendor sources — high confidence on existence/claims, *aspirational until verified* on independent benchmark replication (per P4).
- No independent third-party benchmark replication of the headline impact numbers (Klarna 2×, FM Logistic 10.4%, Schrödinger 4×) was located in this scan. These are vendor-claimed customer wins, not externally audited.
- Mathematical results (matrix-multiplication 4×4-complex in 48 mults, kissing number in 11 dimensions, TSP/Ramsey lower bounds) are checkable in principle; the DeepMind whitepaper (linked from launch post) and the public Gallery are the verification surfaces. Not re-verified by this assistant in this tick — should be tracked.
