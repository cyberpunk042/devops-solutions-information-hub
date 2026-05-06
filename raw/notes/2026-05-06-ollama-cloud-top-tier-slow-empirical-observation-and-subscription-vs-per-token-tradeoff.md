# 2026-05-06 — Ollama Cloud Top-Tier Slow Empirical Observation + Subscription vs Per-Token Billing Tradeoff (Operator-Stated, Sacrosanct)

## Verbatim Operator Directive (Sacrosanct)

> *"btw I tested the top tier model on ollama cloud and effectively currently they are very slow... properly overused and low priority requests and/or such.. doesn't mean it might not unlock or maybe the higher tier at 100 unlock a bit of speed but its a clear reality that all the best model I wanted to try were very very slow.. almost as if they were running on my machine.. \"kidding...\"... so yeah that was something to valide. we will need to validate the progress of this over time, it will probably fix itself at some point... I hope.. and otherwise there are other features."*

> *"OpenRouter wasn't giving me this kind of slow performance.. but clearly its hard to have a proper budget with a per token billing... subsription is way more practical... like the claude code I still cannot separate myself from even though now at least I can go on opencode and such other options."*

> *"otherwise continue"*

## Operational Findings (operator-asserted, registered)

### Finding 1 — Ollama Cloud top-tier models slow as of 2026-05-06

| Property | Operator's framing |
|---|---|
| Tested by operator | Top-tier models on Ollama Cloud |
| Empirical state 2026-05-06 | *"very slow... properly overused and low priority requests and/or such"* |
| Comparison framing (joking but indicative) | *"almost as if they were running on my machine"* |
| Suspected cause | Overuse + low-priority request handling on Ollama Cloud's current top-tier free/lower-paid tiers |
| Possible mitigation | Higher tier ($100/mo plan?) might unlock speed — *not yet validated* |
| Disposition | Track over time — operator hopes it fixes itself; otherwise other features |
| Operator stance | Track-and-watch, not pivot away yet |

### Finding 2 — Subscription vs per-token billing tradeoff (operator-stated framing)

| Provider model | Speed | Cost predictability | Operator's framing |
|---|---|---|---|
| **OpenRouter (per-token)** | Fast (no slow performance observed) | Hard to budget — *"its hard to have a proper budget with a per token billing"* | Speed-positive; budget-negative |
| **Ollama Cloud Pro ($20/mo flat)** | Slow at top-tier (this observation) | Predictable flat rate | Budget-positive; speed-negative-at-top-tier |
| **Claude Code subscription** | (operator-confirmed working, prior memory) | Predictable; *"way more practical"* | Operator-stated *"I still cannot separate myself from even though now at least I can go on opencode and such other options"* |
| **OpenCode subscription** | (operator-confirmed available alternative) | Predictable | Now available as Claude-Code substitute |

**Operator's structural framing**: subscription tiers (predictable cost) are practical for budget; per-token (faster perf) is hard to budget. Goldilocks Protocol applied to provider economics — operator picks per workload class.

## Concept Decomposition (operator's words → wiki state updates)

| Operator framing | Wiki integration target |
|---|---|
| Ollama Cloud top-tier slow as of 2026-05-06 | Update `project_ollama_cloud_consensus_2026_04.md` memory file with empirical caveat |
| Track over time, may fix itself | Memory format includes "as of X date" — tracks reality changes |
| Higher tier may unlock speed (untested) | Track-watch flag in memory; operator may test later |
| Per-token vs subscription tradeoff | Update Anti-Vendor-Lock-In Lesson with provider-economics substitutability observation |
| Claude Code subscription "cannot separate myself from" | Operator-stack fact; aligns with prior memory `project_activated_stack_2026_04_23.md` |
| OpenCode as Claude Code alternative | Already registered in active-stack memory |
| "Otherwise continue" | Authorize forward research/synthesis without further decision |

## Cross-references (already in this wiki)

- [[project_ollama_cloud_consensus_2026_04|Memory — Ollama Cloud Active Stack]] — operator-stated 2026-04 fact; needs 2026-05-06 empirical caveat
- [[project_activated_stack_2026_04_23|Memory — Active AI Stack 2026-04-23]] — Ollama Cloud Pro + OpenCode as registered active stack
- [[second-brain-custom-model-strategy|Second-Brain Custom Model Strategy]] — references Ollama Cloud Pro $20/mo as primary; needs 2026-05-06 caveat
- [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — provider × billing-model substitutability is a substitutability axis
- [[ai-model-provider-harness-decision-matrix-2026|AI Decision Matrix 2026]] — provider × billing tier matrix; needs 2026-05-06 row
- [[goldilocks-protocol|Goldilocks Protocol]] — operator's "pick per workload class" framing applied to provider economics

## Provenance

- Operator session 2026-05-06 — empirical validation of Ollama Cloud top-tier performance
- Continuation arc: post the multi-level-progression sweep (5 syntheses + Layer-4 lesson + propagations + Cloudflare ingestion arc completion)
- Mission alignment: registers operator-stack fact per `feedback_register_dont_research_when_operator_states_a_fact.md`
- Future tracking: operator will revalidate Ollama Cloud top-tier speed over time; track in memory

## Posture

- Don't pivot away from Ollama Cloud — operator says "track over time, may fix itself"
- Register the slow-top-tier observation as empirical fact
- Continue forward per operator's "otherwise continue" — reasonable next move is provider-economics-relevant research (Cloudflare AI Platform unified inference layer ingestion was already on the surfaced-options list)
