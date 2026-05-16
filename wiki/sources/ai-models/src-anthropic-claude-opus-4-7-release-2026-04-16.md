---
title: "Synthesis — Claude Opus 4.7 release (Anthropic, 2026-04-16 GA): direct upgrade to Opus 4.6 with +13% on 93-task coding benchmark, 3× image resolution (2,576 px long edge), new `xhigh` effort level, file-system memory improvements, and self-verification of outputs — same price as Opus 4.6 ($5/$25 per MTok), updated tokenizer (1.0–1.35× more tokens per same input)"
type: source-synthesis
domain: ai-models
status: synthesized
confidence: high
maturity: seed
layer: 1
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: anthropic-newsroom-opus-4-7-2026-04-16
    type: article
    url: https://www.anthropic.com/news/claude-opus-4-7
    file: raw/articles/introducing-claude-opus-47-anthropic.md
    description: "Anthropic Newsroom (2026-04-16) — official Opus 4.7 announcement, full benchmark table, 28 early-tester quotes (Cursor 70% vs 58% on CursorBench, XBOW 98.5% vs 54.5% visual-acuity, Rakuten-SWE-Bench 3× more resolved tasks, Notion +14% at fewer tokens and 1/3 tool errors, Replit easy upgrade decision), migration guidance (tokenizer change, effort levels), and safety profile (Mythos still best-aligned)."
  - id: marktechpost-razzaq-2026-04-18
    type: article
    url: https://www.marktechpost.com/2026/04/18/anthropic-releases-claude-opus-4-7-a-major-upgrade-for-agentic-coding-high-resolution-vision-and-long-horizon-autonomous-tasks/
    file: raw/articles/anthropic-releases-claude-opus-47-a-major-upgrade-for-agentic-coding-high-resolu.md
    description: "MarkTechPost (Asif Razzaq, 2026-04-18) — third-party framing as 'focused improvement, not full generational leap', emphasis on self-verification as 'meaningful behavioral shift', highlights of `xhigh` effort level + task budgets + `/ultrareview` + auto mode in Claude Code, and operational framing of file-system memory."
tags: [anthropic, claude, claude-opus-4-7, claude-opus-4-6, model-tier, agentic-coding, cursorbench, swe-bench, multimodal, vision-3x, xhigh-effort-level, task-budgets, ultrareview, auto-mode, file-system-memory, self-verification, tokenizer-change, mythos-preview, cyber-verification-program, source-synthesis, "2026-04-16", "2026-05-15"]
---

# Claude Opus 4.7 — 2026-04-16 GA Release

> [!info] Source Reference
>
> | Attribute | Value |
> |-----------|-------|
> | **Model** | `claude-opus-4-7` (API string) |
> | **GA date** | 2026-04-16 |
> | **Successor to** | Claude Opus 4.6 |
> | **Position in family** | Top of GA tier (below Mythos Preview, which remains restricted) |
> | **Price** | $5 / MTok input · $25 / MTok output (unchanged from Opus 4.6) |
> | **Availability** | Claude products + API · Amazon Bedrock · Google Cloud Vertex AI · Microsoft Foundry |
> | **Headline benchmark** | +13% over Opus 4.6 on 93-task coding eval (4 tasks neither Opus 4.6 nor Sonnet 4.6 solved); CursorBench 70% vs 58%; XBOW visual-acuity 98.5% vs 54.5%; Rakuten-SWE-Bench 3× more production tasks resolved |
> | **Key behavioral change** | Self-verification — model devises ways to verify its own outputs before reporting back |

## Summary

Claude Opus 4.7 is Anthropic's 2026-04-16 GA successor to Opus 4.6, positioned by Anthropic itself as a "notable improvement" — not a generational leap — focused on agentic software engineering, multimodal reasoning, and long-horizon autonomous task execution. The headline behavioral shift is **self-verification**: the model now devises ways to verify its own outputs before reporting back, closing a loop that previously required external supervision (significant for CI/CD pipelines and multi-step agents). Benchmark gains are concrete and double-digit across the board (+13% on a 93-task coding eval, CursorBench 70% vs 58%, XBOW visual-acuity 98.5% vs 54.5%, Rakuten-SWE-Bench 3× more production tasks resolved, Notion +14% at fewer tokens and 1/3 the tool errors). Vision resolution triples to 2,576 px on the long edge (~3.75 MP). New developer levers: an `xhigh` ("extra high") effort level between `high` and `max`, public-beta **task budgets** for guiding token spend across long runs, the `/ultrareview` slash command in Claude Code, and auto-mode permissions for Max users. Pricing is unchanged from Opus 4.6, but two changes affect token usage: an **updated tokenizer** (same input → 1.0–1.35× more tokens) and more thinking at higher effort levels on later agentic turns. Mythos Preview remains the most-capable and best-aligned model per Anthropic's own evaluations but is restricted; Opus 4.7 ships with the Cyber Verification Program for legitimate cyber-research access.

## Key Insights

### 1. Direct upgrade — but re-tune prompts because instruction-following is sharper

Opus 4.7 is "a direct upgrade to Opus 4.6" per Anthropic. The catch: it follows instructions **more literally**. Prompts written for prior Claude models that relied on loose interpretation or skipping parts may now produce unexpected results.

> [!warning] Re-tune harnesses on migration
> "Users should re-tune their prompts and harnesses accordingly." — Anthropic Newsroom
> Implication for the harness-engineering domain ([[src-rethinking-ai-agents-harness-engineering-rise|Harness Engineering Is the Dominant Performance Lever]]): existing project harnesses tuned against Opus 4.6's interpretive flexibility need empirical re-validation, not assumed-equivalence.

### 2. Coding benchmark uplift is multi-source and double-digit

| Benchmark / Source | Opus 4.6 | Opus 4.7 | Delta |
|---|---|---|---|
| Anthropic 93-task coding eval | baseline | +13% | +13 pp (4 tasks neither 4.6 nor Sonnet 4.6 solved) |
| Cursor / CursorBench | 58% | 70% | +12 pp |
| Notion (complex multi-step workflows) | baseline | +14% at fewer tokens, 1/3 tool errors | first model to pass implicit-need tests |
| Rakuten-SWE-Bench (production tasks) | 1× | 3× | 3× resolution; double-digit Code Quality + Test Quality gains |
| XBOW visual-acuity benchmark | 54.5% | 98.5% | +44 pp (single biggest Opus pain point "effectively disappeared") |
| Hex (deductive logic, dissonant-data traps) | falls for traps | resists | tester says "low-effort Opus 4.7 ≈ medium-effort Opus 4.6" |
| Factory Droids (task success) | baseline | +10–15% | fewer tool errors, more reliable follow-through |
| Bolt (longer-running app-building) | baseline | up to +10% best case | "without the regressions we've come to expect from very agentic models" |
| Harvey BigLaw Bench (high effort) | <90.9% | 90.9% | better reasoning calibration, distinguishes assignment from change-of-control provisions |
| Databricks OfficeQA Pro (document reasoning) | baseline | 21% fewer errors | best-performing Claude for enterprise document analysis |
| CodeRabbit (code review recall) | baseline | +10%+ | "a bit faster than GPT-5.4 xhigh" |
| Devin (Terminal-Bench) | failed | passes 3 prior-failed tasks | "long-horizon autonomy to a new level" |
| Warp (Terminal Bench tasks) | failed | passes prior-failed | cracked a tricky concurrency bug Opus 4.6 couldn't |
| Genspark Super Agent | loops 1 in 18 queries | "highest quality-per-tool-call ratio we've measured" | loop resistance, consistency, graceful error recovery |
| Vercel (one-shot coding tasks) | baseline | "more correct, more complete, more honest about limits" | "does proofs on systems code before starting work" |

> [!abstract] Behavioral pattern across 28 testers: stop-doing-nothing-then-claim-done
> A consistent thread across the 28 customer quotes is Opus 4.7's tendency to **push through** rather than give up. Genspark calls out loop resistance specifically. Notion observes execution continuing through tool failures that "used to stop Opus cold." Vercel notes the model proofs systems code before starting. This is the same self-verification behavior Anthropic itself names — observed independently across multiple production harnesses.

### 3. Vision capability tripled — and it's a model-level change, not an API param

Opus 4.7 accepts images up to **2,576 pixels on the long edge (~3.75 megapixels)**, more than 3× the prior limit. XBOW's visual-acuity benchmark jumped from 54.5% (Opus 4.6) to 98.5% (Opus 4.7) — "our single biggest Opus pain point effectively disappeared."

> [!warning] Token-budget implication
> Because the resolution change is model-level (not opt-in API parameter), images sent to Claude are now processed at higher fidelity automatically — consuming more tokens. Users who don't need fine detail should downsample before sending. Pattern to flag in any project page that documents image-to-Claude flows.

Use cases unlocked: computer-use agents reading dense screenshots, data extraction from complex engineering diagrams, life-sciences patent workflows (per Solve Intelligence quote), pixel-perfect references.

### 4. New developer levers: `xhigh` effort + task budgets + Claude Code auto mode + `/ultrareview`

Four production-relevant levers ship alongside the model:

- **`xhigh` effort level** — between `high` and `max`. Claude Code's default for all plans has been raised to `xhigh`. Anthropic recommends starting with `high` or `xhigh` for coding and agentic use cases.
- **Task budgets (public beta on Claude Platform API)** — let developers guide Claude's token spend so it can prioritize work across longer runs. Directly addresses the "thinks more at higher effort, especially on later turns" output-token growth.
- **`/ultrareview` slash command (Claude Code)** — dedicated review session that reads through changes and flags bugs / design issues "that a careful reviewer would catch". Pro and Max users get 3 free ultrareviews.
- **Auto mode (Claude Code, now extended to Max users)** — permissions option where Claude makes decisions on the user's behalf for longer task runs with fewer interruptions. Less risky than skip-all-permissions but more autonomous than per-action confirm.

### 5. File-system-based memory improvements unlock multi-session work

Opus 4.7 is "better at using file system-based memory" — it remembers important notes across long, multi-session work and reuses them, reducing required up-front context on follow-on tasks.

> [!tip] Wiki-as-memory alignment
> This aligns directly with the wiki's own thesis ([[the-wiki-is-the-brain|principle: the wiki IS the brain]] / [[model-second-brain|Model — Second Brain]]): persistent file-system context outperforms in-prompt re-explanation. Opus 4.7 leans into this architectural assumption rather than fighting it.

### 6. Tokenizer change — same input maps to 1.0–1.35× more tokens

> [!warning] Migration economic note — pricing unchanged but token counts shift
> Two compounding token-usage changes:
>
> 1. **Updated tokenizer** — same text input → roughly 1.0–1.35× more tokens (depends on content type).
> 2. **More thinking at higher effort, especially on later agentic turns** → more output tokens.
>
> Net effect on Anthropic's internal agentic coding eval is "favorable" — better score per token across all effort levels. But Anthropic explicitly recommends **measuring on real traffic** before assuming budget parity. Per-MTok prices are unchanged from Opus 4.6 ($5 input / $25 output), so any cost shift comes from token-count shift, not unit price.

### 7. Cyber capability is the safety story; Mythos remains restricted

Opus 4.7 ships with cyber capability that is **deliberately reduced relative to Mythos Preview** ("during its training we experimented with efforts to differentially reduce these capabilities"). It includes automatic safeguards that detect and block prohibited / high-risk cybersecurity requests. Security professionals doing legitimate vuln-research / pentest / red-team work are directed to the new **Cyber Verification Program** for elevated access.

> [!info] Mythos still the most-capable + best-aligned per Anthropic's own evals
> "Mythos Preview still shows the lowest rates of misaligned behavior." Opus 4.7's automated-audit misalignment score is a modest improvement on Opus 4.6 and Sonnet 4.6 — but Anthropic itself ranks Mythos higher on alignment AND capability. Opus 4.7 is the broadly-available top, not the absolute top.

### 8. Safety profile — improvements + one regression

- **Better:** honesty, resistance to malicious prompt-injection attacks.
- **Worse:** tendency to give overly detailed harm-reduction advice on controlled substances (modestly weaker than Opus 4.6).
- **Comparable:** rates of concerning behavior (deception, sycophancy, cooperation with misuse) remain low — same overall profile.

Alignment assessment language: "largely well-aligned and trustworthy, though not fully ideal in its behavior."

### 9. State of the model family (per Anthropic, as of 2026-04-16)

| Tier | Model | Status |
|---|---|---|
| Restricted | **Claude Mythos Preview** | Most capable + best aligned (per Anthropic evals) — limited release, cyber capabilities not yet broadly safe |
| **Top GA** | **Claude Opus 4.7** | This release. State-of-the-art for broadly-available frontier coding/agentic work |
| Mid GA | Claude Sonnet 4.6 | Unchanged |
| Bottom GA | Claude Haiku | Unchanged |

> [!info] What "Mythos-class" means going forward
> Anthropic states the Cyber Verification Program + Opus 4.7 safeguards are the on-ramp to "our eventual goal of a broad release of Mythos-class models." Mythos is the trajectory anchor for the next 6–12 months; Opus 4.7 is the production-deployable surface.

## Deep Analysis

### Why "focused improvement, not generational leap" is the operationally correct framing

MarkTechPost characterizes Opus 4.7 as "a focused improvement rather than a full generational leap" — and Anthropic's own language ("notable improvement", "direct upgrade") supports this. The version-number convention (4.6 → 4.7, not 4.x → 5.0) is doing real work. Implications:

1. **No architectural retraining of harnesses is required.** Opus 4.6 patterns still work. The instruction-following sharpness is the only mandatory re-tune.
2. **Benchmark gains compound on agentic workloads, not on single-turn tasks.** The 13% / 14% / 3× gains all come from multi-step / long-horizon contexts. Single-turn chat won't show comparable deltas.
3. **The token-usage shift is the operational risk, not capability regression.** Same dollars-per-MTok but more tokens per same input + more output at higher effort means real spend could rise even on identical workloads. Measure before scaling.

### Self-verification as the dominant behavioral shift

Eight of the 28 testers independently surface variants of "the model checks itself" / "pushes through failures" / "doesn't give up" / "doesn't fabricate fallbacks":

- Notion: "first model to pass our implicit-need tests, keeps executing through tool failures that used to stop Opus cold."
- Hex: "correctly reports when data is missing instead of providing plausible-but-incorrect fallbacks."
- Genspark: "highest quality-per-tool-call ratio we've measured" + loop resistance.
- Devin: "pushes through hard problems rather than giving up."
- Vercel: "does proofs on systems code before starting work."
- Ben Lafferty: "cutting out the meaningless wrapper functions and fallback scaffolding... fixes its own code as it goes."
- Qodo: "demonstrates strong precision in identifying real issues, and surfaces important findings that other models either gave up on or didn't resolve."
- Replit: "Personally, I love how it pushes back during technical discussions."

This is consistent with the [[harness-engineering-is-the-dominant-performance-lever|harness-engineering thesis]]: when self-checking moves into the model, the harness layer can simplify the verification scaffolding it previously had to provide externally. Worth a follow-up empirical comparison: harness complexity needed for Opus 4.6 vs Opus 4.7 on the same agentic task to quantify the offload.

### Cline CLI / 3rd-party harness signal (MarkTechPost sidebar)

The MarkTechPost article's "Cline Releases Cline SDK" sidebar reports: **"On Terminal Benchmark 2.0, Cline CLI scored 74.2% on claude-opus-4.7, compared to Anthropic's published 69.4% for Claude Code on the same model."** Read as: harness layer can still extract meaningful additional performance on top of the model upgrade — Cline outperformed Anthropic's own Claude Code harness on the same underlying Opus 4.7. The harness-engineering lever is alive and well even with self-verifying models. (Cline SDK is a separate corpus delta; this synthesis flags it but does not synthesize it — separate source-synthesis recommended.)

## Open Questions

- **Empirical re-validation of Opus 4.6 harnesses against Opus 4.7's literal-instruction-following.** Where in our corpus do we have Opus 4.6-tuned prompts that will misbehave under literal interpretation? (Candidates: any `.claude/skills/` instruction sets, harness command files, or AGENTS.md sections that relied on "soft" wording.)
- **Token-usage real-world delta.** What's the actual token-cost shift on this project's workflows after the tokenizer change + xhigh-default in Claude Code? Requires measurement, not estimation — operator should sample.
- **Smoke test refresh.** [[T002-run-openrouter-smoke-tests|T002 — Run OpenRouter Smoke Tests (K2.6 + Opus + GPT-5.4)]] uses model strings predating Opus 4.7 / GPT-5.5. Smoke test set should add `claude-opus-4-7` and the new GPT-5.5 Instant — separate task.
- **Cyber Verification Program scope.** Does Opus 4.7's auto-blocking of "high-risk cybersecurity requests" affect any legitimate research workflows in our ecosystem (e.g., the PolarProxy / Suricata / Hanke honeypot synthesis chain)? Worth a probe-and-document follow-up rather than assumption.
- **Mythos Preview access path.** Anthropic states broad release is the eventual goal but timeline-undeclared. No corpus action until access opens to general developers — but the trajectory anchor (Mythos-class is the next 6–12 month target) should be recorded so we don't get blindsided by a future GA.

## Pages Affected — Cross-Reference Flags

The following existing pages reference Claude models, model tiers, or benchmark comparisons and will need refresh after this synthesis lands. Flagging here (not editing — operator approves promotion):

- [[model-registry|Model Registry]] — does not yet mention Opus 4.7 as the top GA model.
- [[ai-models-domain-overview|AI Models — Domain Overview]] — model tier landscape may reference older Opus version.
- [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] — full landscape × cost × capability comparison; needs Opus 4.7 row.
- [[model-claude-code|Model — Claude Code]] — needs note on `xhigh` default raise, `/ultrareview`, auto-mode-for-Max, instruction-following re-tune requirement.
- [[T002-run-openrouter-smoke-tests|T002 — OpenRouter Smoke Tests]] — model string list outdated (K2.6 + Opus 4.x + GPT-5.4 → should include Opus 4.7 + GPT-5.5 Instant).
- [[src-anthropic-programmatic-credit-pool-policy-change-2026-06-15|Anthropic Programmatic Credit Pool synthesis]] — does not mention Opus 4.7 (post-dates that source, but the credit pool covers Opus 4.7 the same way).
- [[src-rethinking-ai-agents-harness-engineering-rise|Harness Engineering thesis]] — self-verification behavior is new evidence; the thesis still holds (Cline 74.2% > Claude Code 69.4% on same Opus 4.7 confirms harness layer still extracts value) but needs amendment to reflect that some verification moves into the model.
- [[src-anthropic-effective-harnesses-long-running-agents|Effective Harnesses for Long-Running Agents synthesis]] — may need an addendum noting Opus 4.7's tokenizer change + xhigh effort + file-system memory improvements affect harness sizing.

## Relationships

- RELATES TO: [[src-anthropic-programmatic-credit-pool-policy-change-2026-06-15|Anthropic Programmatic Credit Pool (2026-06-15)]] — same vendor, billing layer above the model
- RELATES TO: [[model-claude-code|Model — Claude Code]] — Claude Code raises default effort to `xhigh` for this model
- RELATES TO: [[src-rethinking-ai-agents-harness-engineering-rise|Harness Engineering Thesis]] — self-verification is a partial in-model substitute for external verification
- RELATES TO: [[src-anthropic-effective-harnesses-long-running-agents|Anthropic — Effective Harnesses for Long-Running Agents]] — file-system memory + task budgets are harness-side levers
- RELATES TO: [[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]] — capability tier shifts
- RELATES TO: [[model-registry|Model Registry]] — top of the Claude GA tier as of 2026-04-16

## Backlinks

[[Anthropic Programmatic Credit Pool (2026-06-15)]]
[[model-claude-code|Model — Claude Code]]
[[Harness Engineering Thesis]]
[[Anthropic — Effective Harnesses for Long-Running Agents]]
[[ai-infrastructure-decision-framework-2026|AI Infrastructure Decision Framework 2026]]
[[model-registry|Model Registry]]
