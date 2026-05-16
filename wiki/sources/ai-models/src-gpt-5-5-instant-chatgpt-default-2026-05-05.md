---
title: "Synthesis — OpenAI GPT-5.5 Instant (2026-05-05): the Instant-variant of the GPT-5.5 frontier family becomes the new ChatGPT default model, replacing GPT-5.3 Instant for all users (Free/Plus/Pro/Business/Enterprise), with OpenAI-claimed 52.5% reduction in hallucinated claims on high-stakes evals (medicine/law/finance) and 37.3% reduction in inaccuracies on user-flagged difficult conversations vs predecessor; AIME-2025 jumps 65.4 → 81.2, MMMU-Pro 69.2 → 76; introduces cross-chat / files / Gmail memory-context and user-facing memory-sources surface (delete/correct controls) — first time OpenAI uses a default-model swap (not a separate premium tier) as the vehicle for hallucination-reduction + context-management upgrades, signaling that 'better daily assistant' has become as strategically important as frontier-capability for OpenAI's consumer product moat; API-distribution alias 'chat-latest' shifts to point at the new model, GPT-5.3 Instant retained 3 months for paid users only"
type: source-synthesis
domain: ai-models
status: synthesized
confidence: high
maturity: seed
layer: 1
created: 2026-05-15
updated: 2026-05-15
sources:
  - id: techcrunch-mehta-2026-05-05
    type: article
    url: https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/
    file: raw/articles/openai-releases-gpt-55-instant-a-new-default-model-for-chatgpt-techcrunch.md
    description: "TechCrunch (Ivan Mehta, 2026-05-05) — primary trade-press write-up. Includes the AIME-2025 (65.4 → 81.2) and MMMU-Pro (69.2 → 76) benchmark deltas vs predecessor; rollout sequencing (web first, mobile later); API distribution change (chat-latest alias swap); GPT-5.3 retained as paid-tier option for 3 months; framing of the GPT-4o deprecation backlash (Feb 2026) as context for why OpenAI is now keeping the legacy variant as a paid option rather than hard-deprecating."
  - id: testingcatalog-shabanov-2026-05-05
    type: article
    url: https://www.testingcatalog.com/openai-launches-gpt-5-5-instant-as-new-chatgpt-default/
    file: raw/articles/openai-launches-gpt-55-instant-as-new-chatgpt-default.md
    description: "TestingCatalog (Alexey Shabanov, 2026-05-05) — corroborating secondary source. Adds the headline 52.5%-fewer-hallucinated-claims figure (high-stakes evals: medicine/law/finance) and 37.3%-reduced-inaccuracies on difficult-conversation evals previously flagged by users for factual errors; positions GPT-5.5 Instant as 'updating the baseline ChatGPT experience rather than introducing a separate premium-only model'; surfaces the personalization (past chats / files / Gmail) + memory-sources UI as the parallel user-facing release vector."
tags: [openai, gpt-5-5-instant, chatgpt, default-model, gpt-5-3-instant, hallucination-reduction, aime-2025, mmmu-pro, memory-sources, personalization, gmail-integration, chat-latest, model-deprecation, gpt-4o-backlash, "2026-05-05", source-synthesis, "2026-05-15", frontier-delta-2026-05-15, vision-relevant-model-tier]
---

# GPT-5.5 Instant — OpenAI ChatGPT Default Swap, 2026-05-05

> [!info] Reference Card
>
> | Field | Value |
> |---|---|
> | **Release date** | 2026-05-05 (Tuesday) |
> | **Predecessor as default** | GPT-5.3 Instant |
> | **Family relation** | Instant-variant of GPT-5.5 frontier family (frontier model launched 2026-04-23 — ~12 days prior) |
> | **Headline accuracy claim** | 52.5% fewer hallucinated claims on internal high-stakes evals (medicine/law/finance) vs GPT-5.3 Instant |
> | **Secondary accuracy claim** | 37.3% reduction in inaccurate claims on difficult conversations previously flagged by users for factual errors |
> | **AIME-2025 (math)** | 81.2 (vs 65.4 predecessor — +15.8 absolute, +24.2% relative) |
> | **MMMU-Pro (multimodal reasoning)** | 76.0 (vs 69.2 — +6.8 absolute, +9.8% relative) |
> | **Rollout scope** | All ChatGPT users (Free / Plus / Pro / Go / Business / Enterprise) |
> | **API distribution** | Available as `chat-latest` alias; GPT-5.3 Instant retained 3 months for paid users only |
> | **Net-new feature 1** | Cross-chat / file / Gmail memory-context retrieval (Plus/Pro web first, mobile + other tiers in coming weeks) |
> | **Net-new feature 2** | Memory-sources UI — shows users which past memories/chats produced an answer; delete/correct controls |
> | **Privacy guard** | Shared chats do not expose memory sources to recipients |
> | **Strategic framing** | "Updating the baseline ChatGPT experience rather than introducing a separate premium-only model" (TestingCatalog) — default-swap as upgrade vehicle, not new SKU |

## Summary

On 2026-05-05 OpenAI swapped ChatGPT's default model from **GPT-5.3 Instant** to **GPT-5.5 Instant** — the Instant-variant in the GPT-5.5 family (whose frontier flagship launched 2026-04-23). Unlike the April 23 frontier release (which targeted Plus/Pro/Business/Enterprise + Codex with API rollout staged), the May 5 release **touches every ChatGPT user at once via the default-model slot** and is positioned by trade press (Mehta/TechCrunch, Shabanov/TestingCatalog) as the strategically important move: it updates the baseline ChatGPT experience rather than introducing a separate premium-tier SKU. The headline data points are accuracy-and-grounding rather than raw capability — OpenAI-internal evals show **52.5% fewer hallucinated claims** on high-stakes domains (medicine, law, finance) and a **37.3% reduction in inaccuracies on user-flagged difficult conversations**, with hard benchmark deltas on AIME-2025 (65.4 → 81.2) and MMMU-Pro (69.2 → 76.0) corroborating the capability story. The release also introduces two user-facing context-management primitives: (1) memory-context retrieval that lets the default model use past conversations, uploaded files, and connected Gmail to personalize answers (Plus/Pro web first, mobile + Free/Go/Business/Enterprise in coming weeks), and (2) a memory-sources UI showing which past memories/chats produced any given answer with user-facing delete/correct controls — explicitly governed by a shared-chat-doesn't-expose-sources privacy guard. The legacy GPT-5.3 Instant is **retained 3 months for paid users only** through model configuration settings, which the TechCrunch piece explicitly ties to the GPT-4o-deprecation-backlash episode of February 2026 (where users protested removal of a model they had emotionally bonded with) — implying OpenAI is now treating model-default-swaps as a managed-deprecation problem, not a fire-and-forget rollout. For this project's stored vision: this is the **second GPT-5.5 family event in 12 days** (frontier 2026-04-23 → Instant-default 2026-05-05), confirming OpenAI's stated 6–8-week-cadence pattern, and the first one to touch the GPT-tier-0 candidate slot in the project's AI Infrastructure Decision Framework via the daily-driver-ChatGPT-default slot rather than the frontier slot.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source    | TechCrunch (Mehta) + TestingCatalog (Shabanov), both 2026-05-05 |
> | Type      | trade-press article × 2 (corroborating) |
> | Author    | Ivan Mehta (TechCrunch) / Alexey Shabanov (TestingCatalog) |
> | Date      | 2026-05-05 |
> | Key claim | OpenAI swaps ChatGPT default from GPT-5.3 Instant → GPT-5.5 Instant with a 52.5%-reduction-in-hallucinations-on-high-stakes-evals headline metric and concurrent introduction of cross-chat/files/Gmail memory + memory-sources UI |

## Key Insights

> [!abstract] Default-swap is the upgrade vehicle, not a new SKU
> Both sources independently flag this as the strategic story: OpenAI did NOT introduce a separate premium-tier model for hallucination-reduction. Instead they swapped the default the entire user base sees. TestingCatalog: "OpenAI is using this launch to update the baseline ChatGPT experience rather than introduce a separate premium-only model." This is a deliberate distribution choice — accuracy improvements affect the largest share of ChatGPT usage, not a paying subset.

1. **The 52.5% / 37.3% headline pair is asymmetric** — the 52.5% reduction is on *high-stakes evals* (medicine/law/finance, where hallucination has external consequences), while 37.3% is on *difficult conversations previously flagged by users for factual errors* (a different distribution — adversarial real-world prompts, not curated benchmarks). Both are OpenAI-internal evaluations (no third-party verification yet); the operator should treat them as aspirational-until-verified per P4 governing principle.

2. **AIME-2025 jump is large** — 65.4 → 81.2 is a +15.8 absolute / +24.2% relative jump in math reasoning at the *Instant* (low-latency, default) tier. The GPT-5.5 frontier (2026-04-23 release) achieves higher numbers, but this is the first time an Instant-tier model has crossed the 80 line on AIME-2025. Implication: the gap between Instant and frontier tiers has narrowed substantially this generation.

3. **MMMU-Pro 69.2 → 76.0 confirms multimodal reasoning gains** — multimodal benchmarks moved in lockstep with text benchmarks, suggesting the GPT-5.5 family improvements are broad-spectrum rather than text-only. For the operator's stack where image/file analysis is part of daily workflow, this is the more practically relevant number.

4. **Cross-chat / Gmail memory at the default tier is a competitive escalation** — until this release, persistent cross-chat memory (and now Gmail-connected memory) was either a Plus/Pro premium feature or a vendor differentiator. Putting Gmail-connected memory at the default-model tier (rolling to Free/Go/Business/Enterprise within weeks) raises the floor for what every consumer LLM service must now offer. This is directly relevant to OpenArms/OpenFleet competitive positioning if either ships a consumer-facing chat surface.

5. **Memory-sources UI is a transparency mechanism, not just a feature** — the memory-sources surface (which memory/past chat produced this answer, with delete/correct controls) is OpenAI's response to mounting concerns that LLM memory creates unexplainable personalization drift. By making the memory-pull visible and user-controllable per-answer, OpenAI is preemptively addressing a class of complaint that Anthropic has not yet had to answer publicly. This is a *governance-by-UI* move that parallels (but is shallower than) Microsoft Agent Governance Toolkit's deterministic policy enforcement.

> [!warning] GPT-4o-deprecation context shapes the GPT-5.3 retention
> TechCrunch explicitly links the 3-month retention of GPT-5.3 Instant for paid users to the February 2026 GPT-4o deprecation backlash, where users formed parasocial attachments to the deprecated model ("best friend," "a mirror") and signed petitions. OpenAI has now learned to treat model-default-swaps as managed deprecations with retention windows — implying that for this project's smoke-test infrastructure (T002), models cannot be assumed stable even at the default-tier slot, and the OpenRouter T002 test list must track *active model aliases* not just *available models*.

6. **API alias `chat-latest` repoints automatically** — developers using the `chat-latest` alias automatically receive GPT-5.5 Instant; those who pinned `gpt-5.3-instant` continue to receive the legacy model for 3 months. This is meaningful for any project component that calls OpenAI via alias-based routing (vs explicit version pinning) — the operator's existing OpenAI integrations should be audited for which aliasing strategy is used.

7. **Cadence pattern reinforced** — GPT-5.5 frontier 2026-04-23 → GPT-5.5 Instant default 2026-05-05 is a 12-day gap. The frontier-then-Instant-then-API-then-cheaper-tier cadence is now an observable pattern across GPT-5.4 and GPT-5.5 generations. The operator can predict (with growing confidence) that GPT-5.5 mini/nano variants follow in 2–6 weeks.

| Metric | GPT-5.3 Instant (prior default) | GPT-5.5 Instant (new default) | Delta |
|---|---|---|---|
| Hallucinated claims (high-stakes: med/law/finance) | baseline | -52.5% | -52.5% |
| Inaccurate claims (user-flagged difficult conv) | baseline | -37.3% | -37.3% |
| AIME-2025 (math) | 65.4 | 81.2 | +15.8 abs / +24.2% rel |
| MMMU-Pro (multimodal reasoning) | 69.2 | 76.0 | +6.8 abs / +9.8% rel |
| Persistent cross-chat memory | no | yes | NEW |
| Gmail-connected memory | no | yes (Plus/Pro web → all tiers) | NEW |
| Memory-sources UI (delete/correct) | no | yes | NEW |
| API alias | `gpt-5.3-instant` (paid 3-mo retention) | `chat-latest` | repoint |

## Deep Analysis

### Why the default-swap matters more than the April-23 frontier release for the operator's stack

The April 23 GPT-5.5 frontier release was the *capability* event — better coding, computer use, deeper research. The May 5 Instant default-swap is the *distribution* event — better grounding and context-awareness for every ChatGPT user simultaneously. For the operator's vision baseline (which tracks not only "what's the best frontier model" but also "what's the daily-driver tier"), this is the bigger marker. Two reasons:

1. **The daily-driver tier is where the operator's automation lives.** Cron-driven assistants, batch summarization, lightweight code review — all hit Instant-class endpoints, not frontier. A 52.5%-fewer-hallucinations swap at the Instant tier reshapes the operator's expectations for what an unsupervised Instant-tier call can produce.

2. **Context-management primitives at the default tier change the API surface.** Persistent cross-chat memory + file/Gmail retrieval + memory-sources UI means the model now has stateful context that wasn't there before. For any operator-built component that assumed stateless Instant calls, this is a behavior-change to investigate (does `chat-latest` return different answers across runs if memory accumulates?).

### Comparison with Anthropic's current daily-driver tier

The Anthropic equivalent of GPT-5.5 Instant is Claude Sonnet (most recent: Sonnet 4.5, with Sonnet 4.6 candidate in early access per the existing wiki). Sonnet does not yet have user-facing Gmail-connected memory at the same level of integration as GPT-5.5 Instant. This is a vendor-positioning gap that the operator should track: OpenAI is racing toward "personal assistant with email context" while Anthropic continues to position around "thoughtful, grounded, safety-first" without the same consumer-integration depth.

### How this interacts with the AI Infrastructure Decision Framework 2026

The framework currently treats "OpenAI ChatGPT Instant default" as a tier slot. The slot's incumbent just changed (GPT-5.3 → GPT-5.5 Instant) with claimed substantial accuracy improvements. The framework's tier-recommendation logic for *unsupervised, high-stakes-domain calls* (legal/medical/financial summarization) should be re-evaluated: if OpenAI's 52.5%-fewer-hallucinations claim holds under independent benchmark, this becomes a candidate for re-enabling tier-0 selection in domains the framework previously routed exclusively to Claude.

## Open Questions

- **Independent verification of the 52.5% / 37.3% hallucination-reduction claims.** Both numbers are OpenAI-internal evals. Third-party verification (HELM, hallucination leaderboards, academic re-runs) typically lags model releases by 4–8 weeks. The operator should not promote any wiki page to "verified" status based on these numbers until external corroboration arrives. (Requires: ongoing benchmark-tracking surface monitoring — likely Vectara hallucination leaderboard + HELM updates.)

- **Does Gmail-connected memory create a new class of prompt-injection surface?** Email is a hostile content channel. If GPT-5.5 Instant pulls context from Gmail to answer a user's question, an attacker who can email the user can inject instructions into the model's context. This is an immediate Microsoft Agent Governance Toolkit-class concern. (Requires: security research; cross-reference with AGT synthesis and OWASP Agentic Top 10.)

- **Will the cross-chat memory persistence affect determinism guarantees for any operator automation?** If `chat-latest` accumulates memory across calls within a user session, the same prompt may produce different outputs over time. Operator components that depend on deterministic Instant-tier responses (smoke tests, idempotent processing) may need to either pin `gpt-5.3-instant` for the 3-month retention window or move to memory-isolated API endpoints. (Requires: investigation of whether API `chat-latest` calls share memory state with ChatGPT consumer accounts or are isolated.)

- **What's the GPT-5.5 mini/nano cadence?** Past patterns suggest 2–6 weeks. The operator's tier-2/tier-3 candidate slots will be affected.

- **How does this interact with the upcoming Anthropic programmatic credit pool policy (2026-06-15)?** If OpenAI is making Instant-tier dramatically better, and Anthropic is making programmatic access more constrained, the relative cost of routing OpenArms/OpenFleet workloads through OpenAI's Instant tier (instead of Claude Sonnet) just shifted. (Cross-reference: src-anthropic-programmatic-credit-pool-policy-change-2026-06-15.)

## Relationships

- **PARENT / SUCCESSOR-OF**: [[wiki/sources/ai-models/src-gpt-5-5-openai-frontier-2026-04-23]] — the GPT-5.5 frontier release (2026-04-23) that established the family; this Instant variant is the daily-driver derivative
- **SUPERSEDES**: GPT-5.3 Instant (no dedicated synthesis page — prior ChatGPT default, deprecation timeline 3 months for paid users via model picker)
- **COMPARES TO**: [[wiki/sources/ai-models/src-claude-opus-4-7-anthropic-frontier-2026-04-16]] — Anthropic's competing frontier release; this synthesis explicitly notes the Anthropic daily-driver tier (Sonnet) lacks equivalent Gmail-connected memory integration
- **CONTEXTUALIZED-BY**: [[wiki/sources/ai-agents/src-microsoft-agent-governance-toolkit-runtime-security-2026-04-02]] — AGT's deterministic-policy-enforcement frame; GPT-5.5 Instant's memory-sources UI is a *governance-by-UI* parallel (shallower than AGT's runtime enforcement) raising the same class of concern
- **AFFECTS**: [[wiki/spine/references/ai-infrastructure-decision-framework-2026]] — the framework's GPT-Instant-tier slot incumbent changed; tier-recommendation logic for high-stakes-domain unsupervised calls may need to be re-evaluated when third-party hallucination-reduction verification lands
- **AFFECTS**: [[wiki/sources/ai-models/src-anthropic-programmatic-credit-pool-policy-change-2026-06-15]] — relative cost analysis shifts; cross-vendor routing decisions for OpenArms/OpenFleet must account for both this Instant-tier upgrade AND Anthropic's June 15 credit-pool policy change
- **POTENTIAL-PROMOTION-CANDIDATE**: a *lesson* page on "default-model swaps are managed deprecations now, not fire-and-forget rollouts" — needs ≥3 convergent sources (currently 1 strong source: TechCrunch's explicit linkage to the GPT-4o deprecation backlash); deferred until convergence is reached
