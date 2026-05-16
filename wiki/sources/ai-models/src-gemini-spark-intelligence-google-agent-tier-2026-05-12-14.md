---
title: "Synthesis — Gemini Intelligence + Gemini Spark (Google, 2026-05-12 Android Show announcement + 2026-05-14 APK Insight leak, pre-I/O 2026-05-19~21): Google formalizes a per-vendor agent-runtime tier inside the Gemini app (two-tab Chat/Agent layout; rebranded from internal codename 'Remy' → 'Gemini Agent' → 'Gemini Spark') alongside a confirmed proactive-AI substrate ('Gemini Intelligence') for Android — multi-step task automation (food/rideshare/shopping/cart-build/inbox-declutter/meeting-briefs/news-digest), Chrome auto-browse, Personal-Intelligence-powered Autofill, Rambler speech-cleanup, and natural-language widget generation — rolling out on Galaxy S26 + Pixel 10 this summer with broader Android (watch/car/glasses/laptop) availability later in 2026; Google explicitly warns Spark is 'experimental' and 'may do things like share your info or make purchases without asking,' confirming Google is intentionally entering the same trust-budget territory as ChatGPT agent mode and Claude Managed Agents but with deeper OS-level integration as the differentiator"
type: source-synthesis
domain: ai-models
status: synthesized
confidence: medium
maturity: seed
layer: 1
created: 2026-05-16
updated: 2026-05-16
sources:
  - id: 9to5google-li-2026-05-14
    type: article
    url: https://9to5google.com/2026/05/14/gemini-spark-insight/
    file: raw/articles/gemini-spark-is-googles-upcoming-ai-agent-in-the-gemini-app.md
    description: "9to5Google (Abner Li, 2026-05-14 — APK Insight teardown of Google app beta 17.23). Primary leak source. Confirms the 'Gemini Agent' → 'Gemini Spark' rebrand, the two-tab Chat/Agent in-app navigation, the Personal-Intelligence + Connected-Apps + skills + chats + tasks + websites-logged-in + location signal-pool the agent draws on, the 'share necessary info with third parties' clause, the 'may do things like share your info or make purchases without asking' experimental warning, and the three example task templates (declutter inbox · meeting briefs · custom news digest). APK-teardown so capabilities are interpreted-from-decompiled-strings, not officially-described."
  - id: google-blog-brooks-2026-05-12
    type: article
    url: https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/
    file: raw/articles/gemini-intelligence-brings-proactive-ai-to-android.md
    description: "Google Keyword blog (Mindy Brooks VP Product Management, 2026-05-12, Android Show 2026 announcement). Confirms the umbrella name 'Gemini Intelligence' for the proactive-AI substrate; multi-step automation tuned on Galaxy S26 + Pixel 10 specifically for food + rideshare apps; the photo-context → Expedia-tour-search pattern (visual context as task input); long-press-power-button as the universal Gemini-action invocation gesture; Chrome auto-browse launching late June 2026 for appointment-booking + parking-reservation; Personal-Intelligence-powered Autofill (opt-in, toggleable); Rambler (speech-cleanup, multilingual, audio-not-stored); Create My Widget (natural-language widget generation backed by Gemini); Material 3 Expressive evolution as the visual design layer."
tags: [google, gemini, gemini-intelligence, gemini-spark, gemini-agent, agent-runtime, vendor-agent-tier, android, pixel-10, galaxy-s26, multi-step-automation, chrome-auto-browse, personal-intelligence, autofill, rambler, create-my-widget, material-3-expressive, "2026-05-12", "2026-05-14", source-synthesis, "2026-05-16", frontier-delta-2026-05-16, vision-relevant-agent-runtime, pre-io-2026, leak-corroborated]
---

# Gemini Intelligence + Gemini Spark — Google Agent-Tier Entry, May 2026 (pre-I/O)

> [!info] Reference Card
>
> | Field | Value |
> |---|---|
> | **Announcement date — Gemini Intelligence** | 2026-05-12 (Android Show, official Google Keyword post by Mindy Brooks, VP Product Management) |
> | **Leak date — Gemini Spark name** | 2026-05-14 (9to5Google APK Insight of Google app beta 17.23) |
> | **Internal codename progression** | 'Remy' (pre-leak) → 'Gemini Agent' (Google app beta 17.22) → 'Gemini Spark' (Google app beta 17.23) |
> | **Imminent confirmation event** | Google I/O 2026 keynote (week of 2026-05-19), expected to formally launch Spark |
> | **Initial device targets** | Samsung Galaxy S26 + Google Pixel 10 (rolling out summer 2026) |
> | **Broader device targets** | Wear OS watches, Android Auto, Android XR glasses, Chromebooks (later in 2026) |
> | **In-app architecture** | Two-tab Chat ↔ Agent split inside Gemini app; "Spark" entry in updated navigation drawer |
> | **Signal pool the agent draws on** | Connected Apps, skills, chats, tasks, websites-logged-into, Personal Intelligence, location |
> | **Trust-budget warning (verbatim from APK)** | "may do things like share your info or make purchases without asking" — Google explicitly tells users to supervise |
> | **Example task templates (visible in APK)** | Declutter inbox (summarize/archive newsletters · unsubscribe) · Meeting briefs · Custom news digest |
> | **Multi-step automation domains tuned at launch** | Food-ordering apps, rideshare apps (Brooks: "we've spent months fine-tuning … on the Galaxy S26 and Pixel 10") |
> | **Net-new automation primitives** | Chrome auto-browse (June 2026) · Personal-Intelligence Autofill · Rambler (speech-cleanup) · Create My Widget (natural-language widget gen) |
> | **Visual-context → task pattern** | Long-press power button over notes → "build shopping cart for delivery"; Photo of brochure → "find a tour like this on Expedia for a group of six" |
> | **Confidence** | Medium — Gemini Intelligence is confirmed; Gemini Spark name + behavior is APK-teardown + confirmed leak, awaiting I/O 2026 keynote confirmation (~5 days from synthesis date) |

## Summary

On 2026-05-12 Google's Android Show announced **Gemini Intelligence** — the umbrella name for a proactive-AI substrate coming to Android, starting on Samsung Galaxy S26 + Google Pixel 10 this summer and rolling to Wear OS, Android Auto, Android XR glasses, and Chromebooks later in 2026. Two days later (2026-05-14), 9to5Google's APK Insight of Google app beta 17.23 surfaced the brand identity of the agent layer within that substrate: **Gemini Spark**, an in-app two-tab Chat-vs-Agent surface that internally evolved from codename 'Remy' → 'Gemini Agent' → 'Gemini Spark' across recent beta builds. The strategic significance for this project's stored vision is that Google is now formally entering the **per-vendor agent-runtime tier** alongside Anthropic's Claude Managed Agents (Dreaming / Outcomes / Multiagent Orchestration, 2026-05-07) and OpenAI's ChatGPT agent mode — but with two distinguishing bets: **OS-level integration** (long-press power button → Gemini action; visual context from screen/camera as task input; Connected Apps + websites-you-are-logged-into as the signal pool) and **explicit trust-budget framing** (the APK string "may do things like share your info or make purchases without asking" tells users they are participating in an experimental autonomous-action loop, not a chatbot). Brooks's confirmed announcement frames the multi-step-automation capability concretely: months of tuning on food + rideshare apps for Galaxy S26 / Pixel 10, with described task patterns including grocery-list-photo → cart-build, brochure-photo → Expedia-tour-search, syllabus-find-and-cart-books, and front-row-bike-booking. The agent's three currently-visible task templates (declutter inbox · meeting briefs · news digest) are conservative compared to the multi-step automation Brooks describes, suggesting Spark at I/O launch will be a constrained-task surface that the multi-step-automation work expands over the summer. Adjacent same-day capabilities — Chrome auto-browse for appointment-booking and parking-reservation (late June 2026), Personal-Intelligence Autofill for complex mobile forms, Rambler for speech-cleanup, and Create My Widget for natural-language widget generation — together complete what Google is positioning as "Android transitioning from operating system into intelligence system" (Brooks's framing). The synthesis must caveat: Spark's name + behavior is **APK-teardown plus leak**, not yet official; the I/O 2026 keynote (~5 days from this synthesis) is the confirmation event. The Gemini Intelligence brand and all device + summer-rollout claims are confirmed by the Google Keyword post.

> [!info] Source Reference
> | Attribute | Value |
> |-----------|-------|
> | Source    | 9to5Google APK Insight (Li, 2026-05-14) + Google Keyword (Brooks, 2026-05-12) |
> | Type      | Teardown article (primary leak) + Official Google product announcement (corroborating context) |
> | Authors   | Abner Li (9to5Google) / Mindy Brooks VP Product Management (Google) |
> | Date      | 2026-05-12 / 2026-05-14 |
> | Key claim | Google is launching a per-vendor agent-runtime tier ('Gemini Spark') inside the Gemini app as part of a broader proactive-AI substrate ('Gemini Intelligence') for Android, with multi-step task automation tuned at Galaxy S26 + Pixel 10 launch, formal I/O 2026 unveiling expected week of 2026-05-19 |

## Key Insights

> [!abstract] Google enters the per-vendor agent-runtime tier — three majors now have one

By I/O 2026 week, all three frontier-LLM vendors have a vendor-branded agent-runtime tier:
1. **Anthropic** — Claude Managed Agents (Dreaming · Outcomes · Multiagent Orchestration, GA 2026-05-07; see `src-claude-managed-agents-dreaming-outcomes-multiagent-2026-05.md`)
2. **OpenAI** — ChatGPT agent mode + Codex
3. **Google** — Gemini Spark inside the Gemini app, OS-integrated on Android

The strategic shape is now legible: vendor-branded agent runtimes are NOT a separate product category; they are the **default consumer surface** for each frontier vendor's most-recent-model. The infrastructure-side coding-harness landscape (Claude Code · Codex · OpenCode · Gemini CLI · Aider · Cline · Cursor — see `src-agentic-coding-harness-landscape-2026.md`) and the per-vendor consumer-agent layer are now distinct tiers in the stack.

> [!abstract] Google's differentiation bet is OS-level depth, not agent-loop sophistication

Where Anthropic's Managed Agents pitches **sophistication of the agent loop** (Dreaming = self-improvement; Outcomes = rubric-eval; Multiagent Orchestration) and OpenAI's ChatGPT agent mode pitches **breadth of consumer reach via the default-model slot** (see `src-gpt-5-5-instant-chatgpt-default-2026-05-05.md`), Google's Spark pitches **OS-level integration depth**: long-press power button as universal invocation, visual context from screen + camera as task input, signal pool that includes websites-you-are-logged-into and location, multi-step automation specifically tuned per-vendor-app (food, rideshare). The competitive implication is that the agent's trust-budget — measured in how much info it can share and how many purchases it can make without asking — is being raised most aggressively by Google because the OS layer gives it the most contextual visibility.

> [!abstract] Explicit "may do things without asking" trust framing is the new pattern

The APK string "while it is designed to ask for your permission before taking sensitive actions, it may do things like share your info or make purchases without asking" is notable because **it admits an action-without-consent failure mode at product-launch time**. Compare to the typical earlier-2026 vendor framing where autonomous-purchase risk is hedged behind opt-in flags and beta gates. Google is explicitly preparing the user for the autonomous-action category as a category, not as an edge case — which suggests the failure cases are frequent enough at this maturity stage that hiding them would be worse than disclosing them. This is consistent with the operator's vision-trajectory tracking around **agent trust budgets** as a first-class stack-tier consideration.

> [!abstract] Gemini Intelligence umbrella binds device-tier to model-tier

The Gemini-Intelligence-on-Galaxy-S26-and-Pixel-10-first rollout is the first time Google is using **device-tier** (premium phone hardware) as the primary gate for the proactive agent surface, with watch / car / glasses / laptop following later. This converges with Apple's earlier-cycle Apple-Intelligence-on-A17-Pro+ pattern. The infrastructure-vision implication: the per-vendor agent layer is being co-marketed with new flagship hardware as the iPhone-moment-for-agent-AI, which both creates a hardware-refresh incentive and creates a measurable two-tier user experience (agent-capable hardware vs. legacy). This is vendor-policy-relevant because it affects which devices the operator's stack can assume an on-device-vendor-agent is present on.

> [!abstract] Visual-context → task is now a first-class invocation modality

Brooks's two concrete examples — long-press power button over a notes-app grocery list → "build a shopping cart with all of these items for delivery"; photo of a hotel-lobby travel brochure → "find a tour like this on Expedia for a group of six" — establish **visual context as task input** as a first-class modality alongside text and voice. This matches the broader 2026 pattern of multimodal agent inputs (Opus 4.7's 3.75 MP vision; see `src-claude-opus-4-7-anthropic-frontier-2026-04-16.md`), but Google's version turns the *device itself* (camera + screen + power button gesture) into the input device for the agent rather than the chat surface.

> [!abstract] Pre-I/O leak cadence shows the marketing playbook

The cadence Android Show (May 12) → APK Insight leak (May 14) → I/O keynote (week of May 19) → broader rollout (summer) is itself the new product-launch shape. Google is no longer keeping major agent features for the I/O keynote surprise — the umbrella brand was already announced 7 days before I/O, and the agent-tier name was already leaked 5 days before I/O. This implies the I/O keynote function is consolidation + developer-API exposure (Agent-to-Agent protocol; see `adamlobo.tv` framing of "A2A" protocol for Gemini 4.0) rather than reveal. For this project's frontier-monitoring posture: **the leak-cadence has moved earlier in the pipeline** and the watch-windows around major vendor events now extend ~2 weeks before the official announcement.

## Relationships

> [!info] Explicit relationships
> | Verb | Target | Why |
> |---|---|---|
> | **complements** | `wiki/sources/ai-models/src-gpt-5-5-instant-chatgpt-default-2026-05-05.md` | Three majors now have a per-vendor consumer-default surface — OpenAI via GPT-5.5 Instant default-swap, Google via Gemini Spark in the Gemini app, Anthropic via Claude Managed Agents in the Claude app |
> | **complements** | `wiki/sources/tools-integration/src-claude-managed-agents-dreaming-outcomes-multiagent-2026-05.md` | Same product tier (per-vendor managed agent runtime), different differentiation bet (Google: OS depth; Anthropic: agent-loop sophistication) |
> | **contrasts-with** | `wiki/sources/tools-integration/src-agentic-coding-harness-landscape-2026.md` | The per-vendor consumer-agent tier (Spark / Managed Agents / ChatGPT agent) is now distinct from the infrastructure-side coding-harness landscape (Claude Code · Codex · OpenCode · Gemini CLI · etc.) — same vendors but different deployment topology and trust-budget |
> | **affects** | `wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md` | Decision matrix now needs a "vendor-agent-runtime" column distinct from raw model-tier; Gemini Spark fills the previously-empty Google cell |
> | **affects** | `wiki/spine/references/ai-infrastructure-decision-framework-2026.md` | Framework should reflect that per-vendor agent runtimes are now the default consumer surface for each frontier vendor, not a separate optional product |
> | **emerges-from** | `wiki/sources/ai-models/src-claude-opus-4-7-anthropic-frontier-2026-04-16.md` | Opus 4.7 establishes vision + memory + task-budget primitives in April; Gemini Spark in May ports the same primitive set (visual context, memory, task list) into Google's OS-integrated form factor — convergent industry direction |
> | **pre-announces** | Google I/O 2026 keynote (week of 2026-05-19) | Spark's official confirmation event; this synthesis should be re-visited within 1 week of I/O for verification + capability deltas |

## Pages potentially affected (operator review required)

The following existing pages may need an addendum reflecting that Google now formally occupies the vendor-agent-runtime tier:

1. **`wiki/spine/references/ai-model-provider-harness-decision-matrix-2026.md`** — add Gemini Spark / Gemini Intelligence row(s) and column(s) for vendor-agent-runtime tier
2. **`wiki/spine/references/ai-infrastructure-decision-framework-2026.md`** — update vendor-tier coverage table to reflect three-vendor parity at the agent-runtime tier
3. **`wiki/sources/tools-integration/src-agentic-coding-harness-landscape-2026.md`** — cross-reference note that the per-vendor agent-runtime layer (Spark / Managed Agents / ChatGPT agent) is now a distinct tier from infrastructure-side coding harnesses (Gemini CLI / Claude Code / Codex), even when same vendor

These are flag-only entries — operator decides whether/how to update. A follow-up `wiki/log/2026-05-16-flagged-pages-gemini-spark.md` will be authored separately.

## Open questions for operator

- Does the operator's stack want to treat per-vendor agent runtimes (Spark · Managed Agents · ChatGPT agent) as a stack-tier the wiki tracks comparatively, or as vendor-specific implementation details that don't merit cross-vendor comparison?
- Post-I/O (week of 2026-05-19), is the Gemini-Spark + I/O-keynote re-visit a separate synthesis or an update to this one? (This page is currently dated 2026-05-16 with `confidence: medium` pending the keynote.)
- Is the **trust-budget framing** ("may do things without asking") a candidate cross-cutting lesson? It now appears in Claude Managed Agents + Gemini Spark + earlier ChatGPT agent mode framings — possibly ≥3 convergent signals.
