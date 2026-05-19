---
title: "Synthesis — Claude Opus 4.7 (Anthropic, 2026-04-16 GA): rigor-tuned frontier model with self-verification, 3.75 MP vision, xhigh effort tier, task budgets, file-system memory; narrowly retakes generally-available SOTA over GPT-5.4 and Gemini 3.1 Pro at unchanged $5/$25-per-MTok pricing while Mythos Preview remains restricted under Project Glasswing"
type: source-synthesis
domain: ai-models
status: synthesized
confidence: high
maturity: seed
layer: 1
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: anthropic-newsroom-2026-04-16
    type: article
    url: https://www.anthropic.com/news/claude-opus-4-7
    file: raw/articles/introducing-claude-opus-47-anthropic.md
    description: "Anthropic's own announcement (April 16, 2026) — full benchmark suite, 28 customer testimonials (Intuit, Notion, Replit, Devin/Cognition, Harvey, XBOW, Vercel, Databricks, Ramp, Bolt, Hex, Hebbia, Rakuten, CodeRabbit, Genspark, Warp, Quantium, Factory, Qodo, IGGY/MysteryAI, Cursor, etc.), tokenizer-change disclosure (1.0–1.35×), xhigh/task-budgets/auto-mode/ultrareview detail, safety profile relative to Opus 4.6 and Mythos Preview."
  - id: venturebeat-franzen-2026-04-16
    type: article
    url: https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm
    file: raw/articles/anthropic-releases-claude-opus-47-narrowly-retaking-lead-for-most-powerful-gener.md
    description: "VentureBeat (Carl Franzen, 2026-04-16) — strategic framing: narrow SOTA lead vs GPT-5.4 (1753 vs 1674 GDPVal-AA Elo) and Gemini 3.1 Pro (1314), the Rust-TTS self-verification anecdote, Cyber Verification Program detail, Project Glasswing context, $800B valuation environment, DoW supply-chain-risk litigation, 'AI shrinkflation' user-rebellion backdrop the release is engineered to silence."
  - id: marktechpost-razzaq-2026-04-18
    type: article
    url: https://www.marktechpost.com/2026/04/18/anthropic-releases-claude-opus-4-7-a-major-upgrade-for-agentic-coding-high-resolution-vision-and-long-horizon-autonomous-tasks/
    file: raw/articles/anthropic-releases-claude-opus-47-a-major-upgrade-for-agentic-coding-high-resolu.md
    description: "MarkTechPost (Asif Razzaq, 2026-04-18) — concise developer-facing recap: 13% lift on 93-task coding benchmark, CursorBench 70% vs 58% Opus 4.6, +14% on multi-step workflows at 1/3 tool errors, XBOW 98.5% vs 54.5% visual-acuity benchmark, file-system-memory framing, Claude Code default raised to xhigh effort."
  - id: cnbc-capoot-2026-04-16
    type: article
    url: https://www.cnbc.com/2026/04/16/anthropic-claude-opus-4-7-model-mythos.html
    file: raw/articles/httpswwwcnbccom20260416anthropic-claude-opus-4-7-model-mythoshtml.md
    description: "CNBC (Ashley Capoot, 2026-04-16) — regulatory + strategic positioning: Opus 4.7 as 'less risky than Mythos,' Project Glasswing's high-profile Trump-administration/bank-CEO meetings, Mythos Preview not slated for general availability, Anthropic's reputation as safety-first vs OpenAI rival framing."
  - id: claude-release-notes-2026-04
    type: article
    url: https://support.claude.com/en/articles/12138966-release-notes
    file: raw/articles/httpssupportclaudecomenarticles12138966-release-notes.md
    description: "Anthropic release-notes timeline — confirms 2026-04-16 Opus 4.7 launch + 2026-04-17 Claude Design launch + back-history of Cowork, Sonnet 4.6 (Feb 17 2026), Opus 4.6 (Feb 5 2026), Opus 4.5 (Nov 24 2025), Haiku 4.5 (Oct 15 2025) generational cadence."
tags: [anthropic, claude, claude-opus-4-7, claude-mythos-preview, frontier-llm, agentic-coding, swe-bench-pro, gdpval-aa, cursorbench, terminal-bench-2, xhigh-effort, task-budgets, file-system-memory, multimodal-vision, computer-use, ultrareview, auto-mode, claude-code, project-glasswing, cyber-verification-program, tokenizer-change-1-0-to-1-35x, self-verification, rigor, "2026-04-16", source-synthesis, "2026-05-15", frontier-delta-2026-05-15]
---

# Claude Opus 4.7 — Anthropic Frontier GA Release, 2026-04-16

> [!info] Reference Card
>
> | Field | Value |
> |---|---|
> | **GA date** | 2026-04-16 |
> | **Predecessor** | Claude Opus 4.6 (2026-02-05) |
> | **Successor (restricted)** | Claude Mythos Preview (restricted; Project Glasswing only) |
> | **API ID** | `claude-opus-4-7` |
> | **Pricing** | $5 / $25 per million input/output tokens (unchanged from 4.6) |
> | **Tokenizer change** | New tokenizer; same content maps to 1.0–1.35× more tokens |
> | **Effort levels** | low / medium / high / **xhigh (new)** / max — Claude Code defaults raised to xhigh |
> | **Vision** | Up to 2,576 px long-edge (~3.75 MP) — 3× prior Claude limit |
> | **Distribution** | Claude products, API, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry |
> | **Key new product surface** | `/ultrareview` slash command + auto mode extended to Max plan + task budgets (public beta) |
> | **Memory model** | File-system-based memory persisted across multi-session work |
> | **Safety profile vs 4.6** | Roughly comparable; better honesty/prompt-injection resistance; modestly weaker on harm-reduction overdetail; Mythos Preview still lowest misaligned-behavior score |
> | **Cyber posture** | Differentially reduced cyber capabilities + automated blockers; Cyber Verification Program for legitimate security researchers |

## Summary

Claude Opus 4.7 is Anthropic's April-16-2026 frontier-tier flagship — a focused, instruction-literal, rigor-tuned successor to Opus 4.6 that **narrowly retakes the generally-available SOTA spot** over GPT-5.4 (released early March 2026) and Gemini 3.1 Pro (February 2026), particularly on long-horizon agentic coding, GDPVal-AA knowledge work (1753 Elo vs GPT-5.4's 1674 and Gemini 3.1 Pro's 1314), CursorBench (70% vs Opus 4.6's 58%), SWE-bench Pro (64.3% vs 53.4%), arXiv visual reasoning (91.0%), and BigLaw Bench (90.9% at high effort). The model ships with **five behavioral and infrastructural changes that compound**: (1) **self-verification** as a default behavior — the model devises its own verification steps before reporting completion, demonstrated by Sean Ward (IGGY) where Opus 4.7 built a Rust text-to-speech engine then fed its own audio through a speech recognizer to verify against a Python reference; (2) **3× higher multimodal resolution** (up to ~3.75 MP), turning XBOW's visual-acuity benchmark from 54.5% (Opus 4.6) to 98.5% — model-level not API-flag, so it just works; (3) a new **xhigh effort level** between high and max plus **task budgets** in API public beta, giving developers a cost-control lever for long-running agentic runs; (4) **file-system-based memory** that persists across sessions reducing up-front context needs; and (5) Claude-Code-specific `/ultrareview` (senior-engineer-equivalent review pass) and auto-mode extended to Max users. Crucially the model is **literal in instruction following** — legacy prompts engineered to be "loose" with prior models will need retuning. Pricing is unchanged at $5 input / $25 output per M-tokens, but the new tokenizer increases token count for identical inputs by 1.0–1.35×, so real-world cost rises. Strategically Opus 4.7 is paired with **Project Glasswing** — Mythos Preview, a more powerful successor, remains restricted to a small group of enterprise cybersecurity partners with no GA plan; Opus 4.7 serves as the public testbed for new automated cyber safeguards (CyberGym 73.1% vs Mythos Preview's 83.1% vs GPT-5.4's 66.3%). For this project's stored vision, Opus 4.7 **re-baselines the tier-0 candidate** previously occupied by Opus generically + K2.6 comparators in the AI Infrastructure Decision Framework 2026 and the OpenRouter T002 smoke-test list.

## Key Insights

> [!abstract] Self-verification is now a default behavior, not a prompt pattern
> The Rust-TTS-then-speech-recognizer anecdote (Sean Ward, IGGY) is the load-bearing
> behavioral claim: Opus 4.7 *devises its own verification steps before reporting
> a task complete*. This is the most consequential change for autonomous agentic
> pipelines — it closes the loop that prior frontier models left open, which is
> why Cognition's Scott Wu reports Devin can "work coherently for hours" and why
> Factory Droids (Leo Tchourakov) sees the model "carry work all the way through
> instead of stopping halfway." This is not prompt-engineering work the harness
> author has to do; the model does it.

1. **Narrow SOTA lead, not a clean sweep** — GPT-5.4 still leads in agentic search (89.3% vs 79.3%), multilingual Q&A, and raw terminal-based coding; Opus 4.7's lead is 7-to-4 on directly-comparable benchmarks per VentureBeat. The race is tightening; Opus 4.7 is a *specialized* SOTA optimized for long-horizon autonomy and rigor, not a unilateral victor.

2. **GDPVal-AA Elo 1753 is the single cleanest metric** — third-party economically-valuable-knowledge-work eval, with Opus 4.7 1753 / GPT-5.4 1674 / Gemini 3.1 Pro 1314. This is the metric most directly relevant to the operator's "senior engineer tier model group" vision baseline.

3. **3× vision resolution unblocks a class of computer-use work** — XBOW's autonomous penetration-testing visual-acuity benchmark went 54.5% → 98.5%. Oege de Moor (XBOW CEO): "Our single biggest Opus pain point effectively disappeared." This is model-level (not opt-in flag), so any computer-use agent in production picks it up automatically — at higher token cost for high-res images, which users can downsample to avoid.

4. **xhigh + task budgets = first-class fiscal/operational control for autonomous runs** — xhigh sits between high and max; Claude Code defaults are raised to xhigh; task budgets (API public beta) hard-cap token spend per task. Together these are the agent-cost-control surface developers have been asking for, and signal the maturity of agentic AI as a production line-item rather than a novelty.

5. **File-system-based memory across sessions** — explicitly called out by Anthropic and confirmed by multiple testers: Opus 4.7 "remembers important notes across long, multi-session work, and uses them to move on to new tasks that, as a result, need less up-front context." This is a structural change in how long-running agents accumulate state — relevant to OpenArms/OpenClaw harness architectures.

6. **Instruction literalism is the migration trap** — "where previous models interpreted instructions loosely or skipped parts entirely, Opus 4.7 takes the instructions literally." Anthropic explicitly warns: **legacy prompt libraries must be re-tuned**. This affects every harness in this project's ecosystem that has prompt templates calibrated for 4.6.

7. **Tokenizer change costs 0–35% more tokens for the same input** — pricing per token is unchanged, but the new tokenizer maps the same text to 1.0–1.35× more tokens depending on content type. Combined with more-thinking-at-higher-effort, real-world bills will rise — Anthropic recommends measuring on real traffic, not assuming flat cost migration.

8. **`/ultrareview` + auto mode are Claude Code product changes, not just model changes** — `/ultrareview` is a "senior-engineer-equivalent" code review pass; Pro/Max get 3 free trials. Auto mode (Claude makes decisions without per-step permission prompts) is now extended to Max users, lowering the friction for overnight/long-running tasks while keeping permission-skipping bounded.

> [!warning] Cyber safeguards may block legitimate security workflows
> Opus 4.7 ships with automated detection-and-blocking of requests that "indicate
> prohibited or high-risk cybersecurity uses." Anthropic launched the **Cyber
> Verification Program** as the escape valve — vulnerability researchers,
> pentesters, and red-teamers can apply for verified access to use Opus 4.7
> defensively. This is a structural shift: the most capable AI features are no
> longer universally available, but gated behind professional credentials.
> CyberGym shows Opus 4.7 at 73.1% (vs Mythos Preview 83.1%, GPT-5.4 66.3%) —
> still strong but deliberately restrained.

9. **Mythos Preview is the strategic indicator, not a deployable model** — Anthropic explicitly states no GA plans for Mythos. It exists as a cybersecurity research artifact under Project Glasswing for enterprise partners + an alignment-benchmark anchor (lowest misaligned-behavior score of any Anthropic model). For this project's vision, Mythos is a **tracked-but-unverified frontier-tier indicator**, not a current candidate model.

10. **The customer-testimonial pattern is "reliability, not novelty"** — across 28 quoted testimonials, the recurring phrase is "I can rely on the output" / "feels like a true teammate" / "carries work to completion." This is the discourse shift from "impressed by the tech" to "depending on the output" — the operator's vision baseline ("senior engineer tier") matches this exact frame.

11. **The release exists inside three external pressure systems** — (a) US Department of War "supply chain risk" designation (Anthropic refused mass-surveillance + autonomous-lethal-weapons use; federal appeals court denied stay); (b) the $800B valuation environment (vs $380B Series G in February 2026; $30B run-rate); (c) the GitHub/X "AI shrinkflation" power-user revolt against Opus 4.6 + Claude Code quality regressions. Opus 4.7 is engineered to address the third directly via rigor + reliability + cost controls.

12. **Distribution is unchanged-and-broad** — Anthropic API + Amazon Bedrock + Google Cloud Vertex AI + Microsoft Foundry, all on day one. The OpenRouter T002 smoke-test list should add `anthropic/claude-opus-4-7` and re-rank against the existing candidates.

## Deep Analysis

### Benchmark table (from Anthropic + VentureBeat + MarkTechPost)

| Benchmark | Opus 4.7 | Opus 4.6 | GPT-5.4 | Gemini 3.1 Pro | Mythos Preview |
|---|---|---|---|---|---|
| **GDPVal-AA (Elo)** | **1753** | — | 1674 | 1314 | — |
| **SWE-bench Pro** | **64.3%** | 53.4% | — | — | — |
| **CursorBench** | **70%** | 58% | — | — | — |
| **GPQA Diamond** | **94.2%** | — | parity | parity | — |
| **arXiv visual reasoning (w/ tools)** | **91.0%** | 84.7% | — | — | — |
| **XBOW visual-acuity** | **98.5%** | 54.5% | — | — | — |
| **BigLaw Bench (high effort)** | **90.9%** | — | — | — | — |
| **OfficeQA Pro** | 21% fewer errors than 4.6 (Databricks) | baseline | — | — | — |
| **Rakuten-SWE-Bench** | 3× resolution of 4.6 (Rakuten) | baseline | — | — | — |
| **CyberGym** | 73.1% | 73.8% (revised) | 66.3% | — | **83.1%** |
| **Agentic search** | 79.3% | — | **89.3%** | — | — |
| **Internal research-agent (6 modules avg)** | **0.715** (tied for top) | — | — | — | — |
| **General Finance module** | **0.813** | 0.767 | — | — | — |
| **Misaligned behavior (lower=better)** | improvement over 4.6 | baseline | — | — | **lowest** |

### What changes for this project's stored vision

1. **`wiki/spine/references/ai-infrastructure-decision-framework-2026.md`** — the capability-tier reference should be updated to name `claude-opus-4-7` explicitly as the current generally-available SOTA, with GDPVal-AA 1753 as the headline. Mythos Preview tracked separately as "restricted-tier indicator, not deployable." Flag for operator-decision-queue.

2. **`wiki/backlog/tasks/T002-run-openrouter-smoke-tests.md`** — model list should include `anthropic/claude-opus-4-7` and likely retire `anthropic/claude-opus-4-6` as the primary tier-0 Anthropic candidate. K2.6 comparator unchanged. Flag for operator-decision-queue.

3. **`wiki/log/2026-04-22-openrouter-k2-6-day-1-setup-procedure.md`** — Opus tier reference should be checked for staleness; if the entry refers to "Opus" generically, it's still correct, but if it pins Opus 4.6 specifically it should be amended.

4. **Custom-tailored senior-engineer tier-model-group research synthesis** (`wiki/domains/cross-domain/custom-tailored-senior-engineer-tier-model-group-with-recreated-intelligence-layer-research-synthesis.md`) — should incorporate self-verification + file-system-memory as confirming evidence for the "recreated intelligence layer" thesis; specifically, Opus 4.7's internal self-verification reduces the harness's burden to enforce verification externally.

5. **Anti-vendor-lock-in lesson** (`wiki/lessons/02_synthesized/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md`) — Opus 4.7 reinforces Anthropic's lead but the *narrow* nature of the lead + GPT-5.4 still winning in agentic-search/multilingual/terminal-coding is empirical evidence for the lesson's framing: there is no single dominant stack, the lead trades positions every ~6 weeks.

### Migration cost for legacy harnesses (from Anthropic + VentureBeat + tester quotes)

| Change | Action required | Risk if ignored |
|---|---|---|
| Instruction literalism | Re-tune loose prompts → explicit prompts | "Unexpected or overly rigid results" (Anthropic warning) |
| Tokenizer 1.0–1.35× | Re-budget token spend on real traffic | Bill rises 0–35% silently |
| xhigh becomes Claude Code default | Decide explicit effort per workflow | More compute, more latency than expected |
| Auto mode extended to Max | Audit which scripts auto-approve | More autonomous decisions running unattended |
| Cyber safeguards may block | Apply to Cyber Verification Program if legitimate security work | Workflow blocked mid-run |

### Strategic claim — Anthropic is "buying" public trust on safety while restricting peak capability

The Project Glasswing + Mythos-restricted + Cyber Verification Program structure is a deliberate **capability-safety-tradeoff bargain**: peak capability is gated behind credentials, public model is publicly safe, the verification program is the bridge. CNBC (Capoot) frames this as Anthropic continuing its "safety-first vs OpenAI" reputational strategy; VentureBeat (Franzen) frames it as fiscal-and-operational maturity matching the $800B-valuation environment. Either framing yields the same conclusion: **the era of "the most capable AI is universally available" is now formally over for the Anthropic stack**, with cyber-capability gating as the first concrete instance.

## Open Questions

- Has anyone independently benchmarked Opus 4.7 + xhigh against GPT-5.5 (released 1 week later, 2026-04-23, per `src-gpt-5-5-openai-frontier-2026-04-23.md`)? The CNBC reporting treats them as parallel-track frontier releases but no head-to-head benchmark surfaced yet.
- What is the empirical cost-delta for migrating a representative this-project harness from Opus 4.6 to Opus 4.7 with the new tokenizer + xhigh-by-default? Needs T002 smoke-test data on real workloads.
- Does file-system-based memory interact safely with this project's `raw/notes/` sacrosanct-verbatim discipline? If Opus 4.7 writes notes to disk autonomously in an agentic harness, the "verbatim operator directive" boundary needs explicit guardrails.
- What does the Cyber Verification Program approval process actually require, and does any legitimate research workflow in this project's scope trip the new blockers? Pen-testing + Suricata-adjacent work in this project's `wiki/domains/cybersecurity/` may be relevant.

## Relationships

- SUPERSEDES (in tier-0 GA candidate slot): Claude Opus 4.6 — predecessor model from February 2026
- RESTRICTED-TIER INDICATOR (not deployable): Claude Mythos Preview — see `src-anthropic-mythos-preview-frontier-restricted-2026-04-16.md`
- PEER COMPETITOR (released ~1 week later): GPT-5.5 — see `src-gpt-5-5-openai-frontier-2026-04-23.md`
- PEER COMPETITOR (older frontier): Google Gemini 3.1 Pro (February 2026)
