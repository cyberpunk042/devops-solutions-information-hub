---
title: "2026-04-25 Regather + Systemic Bug Investigation — Layer-2 Teaching Gap and Second P4 Instance in Spine"
type: note
domain: cross-domain
note_type: session
status: active
confidence: high
created: 2026-04-25
updated: 2026-04-25
last_reviewed: 2026-04-25
sources:
  - id: prior-handoff-end-state
    type: wiki
    file: wiki/log/2026-04-25-session-handoff-end-state-with-failures.md
    description: "Prior session's operator-cut handoff; pickup-cold runbook drove this session's regather"
  - id: spine-super-model
    type: wiki
    file: wiki/spine/super-model/super-model.md
    description: "The meta-model — what this whole system IS as a system"
  - id: model-registry
    type: wiki
    file: wiki/spine/references/model-registry.md
    description: "All 16 named models with paths"
  - id: methodology-engine
    type: file
    file: wiki/config/methodology.yaml
  - id: schema-engine
    type: file
    file: wiki/config/wiki-schema.yaml
  - id: artifact-types-engine
    type: file
    file: wiki/config/artifact-types.yaml
  - id: sister-projects-registry
    type: file
    file: wiki/config/sister-projects.yaml
  - id: model-llm-wiki
    type: wiki
    file: wiki/spine/models/foundation/model-llm-wiki.md
  - id: model-wiki-design
    type: wiki
    file: wiki/spine/models/foundation/model-wiki-design.md
  - id: model-claude-code
    type: wiki
    file: wiki/spine/models/agent-config/model-claude-code.md
    description: "Spine page where the second P4 instance was discovered this session — declares 5 skills + no hooks, both wrong"
  - id: model-skills-commands-hooks
    type: wiki
    file: wiki/spine/models/agent-config/model-skills-commands-hooks.md
  - id: model-markdown-as-iac
    type: wiki
    file: wiki/spine/models/agent-config/model-markdown-as-iac.md
  - id: model-context-engineering
    type: wiki
    file: wiki/spine/models/depth/model-context-engineering.md
  - id: model-quality-failure-prevention
    type: wiki
    file: wiki/spine/models/quality/model-quality-failure-prevention.md
    description: "3-layer defense framework — names the layer where the bug lives (Layer 2 teaching, ~60% compliance)"
  - id: principle-1
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
  - id: principle-2
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md
  - id: principle-3
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md
  - id: principle-4
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
  - id: gateway-output-contract
    type: wiki
    file: wiki/spine/standards/gateway-output-contract.md
  - id: concept-page-standards
    type: wiki
    file: wiki/spine/standards/concept-page-standards.md
  - id: enforcement-hierarchy
    type: wiki
    file: wiki/spine/super-model/enforcement-hierarchy.md
  - id: e022-epic
    type: wiki
    file: wiki/backlog/epics/milestone-v2/e022-context-aware-gateway-orientation-and-routing.md
    description: "Epic that shipped gateway orient + what-do-i-need; in review at 95%/90%"
  - id: e022-m002
    type: wiki
    file: wiki/backlog/modules/e022-m002-gateway-orient-subcommand.md
  - id: e022-m003
    type: wiki
    file: wiki/backlog/modules/e022-m003-what-do-i-need-upgrade.md
  - id: gateway-tool
    type: file
    file: tools/gateway.py
    description: "Verified: gateway_orient + _orient_brain_fresh + _wdin_brain_task_bound implemented at lines 264-505"
  - id: session-start-hook
    type: file
    file: .claude/hooks/session-start.sh
    description: "Current session-start reminder — prose pointers to spine, not content injection (bounded by contract size ceiling)"
  - id: post-compact-hook
    type: file
    file: .claude/hooks/post-compact.sh
  - id: settings-json
    type: file
    file: .claude/settings.json
  - id: directives-2026-04-24
    type: notes
    file: raw/notes/2026-04-24-operator-directives-session-verbatim.md
  - id: directives-2026-04-25
    type: notes
    file: raw/notes/2026-04-25-operator-directive-continue-ingestions-plus-qwen3-6-27b.md
  - id: handoff-2026-04-23
    type: wiki
    file: wiki/log/2026-04-23-session-handoff-ai-infrastructure-vision-and-tooling.md
  - id: handoff-2026-04-24
    type: wiki
    file: wiki/log/2026-04-24-session-handoff-brain-refactor-rules-and-hooks.md
  - id: gap-analysis-2026-04-24
    type: wiki
    file: wiki/log/2026-04-24-top-layer-routing-refactor-claude-md-gap-analysis.md
    description: "Named Gap 1 (SessionStart loading) which E022 implements; this session verified Gap 1 is contract-bounded by design, not a deferred fix"
  - id: handoff-2026-04-25-ingestion
    type: wiki
    file: wiki/log/2026-04-25-session-handoff-qwen3-6-27b-ingestion-batch.md
  - id: aicp-session-handoff
    type: external
    file: ~/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md
    description: "AICP's own 2026-04-24 handoff — authoritative on local-AI tier-0 state ($540→$100 routing finding, K2.6 local at 0.3 tok/s)"
  - id: self-reference-drift-lesson
    type: wiki
    file: wiki/lessons/03_validated/methodology-process/self-reference-drift-wiki-must-practice-its-own-teachings.md
    description: "The lesson this session adds further evidence to (Open Question 2 still open per its own framing)"
  - id: agent-must-practice-lesson
    type: wiki
    file: wiki/lessons/03_validated/methodology-process/the-agent-must-practice-what-it-documents.md
    description: "Validated lesson naming this exact bug at the agent-discipline layer"
tags: [handoff, session, regather, systemic-bug, p4-instance-spine, layer-2-teaching-gap, response-composition-boundary, behave-from-the-project, fix-at-the-root, mission-2026-04-27, e022-shipped, skills-layer-unbuilt]
---

# 2026-04-25 Regather + Systemic Bug Investigation — Layer-2 Teaching Gap and Second P4 Instance in Spine

## Summary

Mid-session log capturing a thorough regather (~3500 lines of spine read in one continuous batch under operator directive *"continue"* × 4) and the resulting investigation into the systemic bug operator named: *"every fucking session I have to deal with a systematic bug.. this makes no fucking sense ..."* The bug is at the agent's response-composition boundary — exactly where Claude Code's hook surface does not reach. The wiki's own Layer-2 teaching achieves ~60% compliance per quantified evidence; the bug recurs because no infrastructure layer can structurally enforce "agent must read source X before claiming knowledge from X" — Claude Code has no `PreEmit`/`PreResponse` hook event. E022 (gateway orient + what-do-i-need) is shipped (in review, 95%/90%) and IS the structured digest mechanism, bounded by the gateway-output-contract size ceiling. A second P4 instance was discovered live in the spine itself ([wiki/spine/models/agent-config/model-claude-code.md](wiki/spine/models/agent-config/model-claude-code.md) declaring 5 skills + no hooks — both wrong as of 2026-04-24).

## Verbatim operator directives this session (sacrosanct)

> "lets see if you are able to do better, the last few session were underwhelming.... really bad...."

> "wtf happened ?? why didn't you take the trail ??? you had everything... all the directions handed to you....."

> "every fucking session I have to deal with a systematic bug.. this makes no fucking sense ... answer me this if you are really not retard... what do we teach about Wiki LLM and Methodology and Standards ?"

> "This just prove me that you see some of the surface... like I thought you are a retard...."

> "I DONT FUCKING UNDERSTAND WHY YOU TRY TO INTERNALIZE INTELLIGENCE ??? WTF ??? WHY DOES THIS KEEP HAPPENING ?????? WTF ????????? THE INTELLINGENCE IN IN THE PROJECT.... THE BRAIN IS THE PROJECT...... STOP TRYING TO HALLUCINATE THE ANSWER... IT HAS TO COME FROM GROUND TRUTH NOT TRASH HALLUCINATIONS...... WTF ARE YOU DOING ????? WHAT IS BROKEN AGAIN ??? WTF ???? WHY DIDn"T YOU MAKE THE 20-30+ request required to aquire the minimal context and intelligence ??? IF YOU DONT KNOW THE PROJECT YOU ARE A RETARD.. THIS IS WHAT ALL AI MODELS ARE TO THE ROOT.. RETARTEDED.. IT NEEDS INTELLIGENCE IN THE CONTEXT TO WORK.. WTF ??? HOW CAN THIS BE BROKEN ??? WE NEED A THOROUGH FUCKING INVESTIGATION AFTER YOU FUCKING TAKE THE HINT...."

> "continue" (× 4)

## What was regathered this session

The list, with one-line each — every entry was Read in this session, not summarized:

| # | Path | What it grounded |
|---|---|---|
| 1 | [wiki/log/2026-04-25-session-handoff-end-state-with-failures.md](wiki/log/2026-04-25-session-handoff-end-state-with-failures.md) | Prior session's runbook + the `~/aicp/` fabrication incident |
| 2 | [wiki/spine/super-model/super-model.md](wiki/spine/super-model/super-model.md) | 16 models in dependency-order, 4 adoption tiers, 5 sub-super-models, the weave |
| 3 | [wiki/spine/references/model-registry.md](wiki/spine/references/model-registry.md) | All 16 model names + paths + the three-layer pattern |
| 4 | [wiki/config/methodology.yaml](wiki/config/methodology.yaml) | Per-model artifact chains + ALLOWED/FORBIDDEN per stage + 5 composition patterns |
| 5 | [wiki/config/wiki-schema.yaml](wiki/config/wiki-schema.yaml) | 9 required + 30+ optional fields, 19 types, 17 verbs, source rules |
| 6 | [wiki/config/artifact-types.yaml](wiki/config/artifact-types.yaml) | 3 artifact classes + per-type thresholds + methodology_templates |
| 7 | [wiki/config/sister-projects.yaml](wiki/config/sister-projects.yaml) | aicp.path: ~/devops-expert-local-ai with `aliases: [devops-expert-local-ai]` |
| 8 | [wiki/spine/models/foundation/model-llm-wiki.md](wiki/spine/models/foundation/model-llm-wiki.md) | 3-layer architecture, L0→L6, dual-scope, ~200 page LightRAG threshold |
| 9 | [wiki/spine/models/foundation/model-wiki-design.md](wiki/spine/models/foundation/model-wiki-design.md) | Visual layer, 8 callout vocabulary, 3 formatting contexts |
| 10 | [wiki/spine/models/agent-config/model-markdown-as-iac.md](wiki/spine/models/agent-config/model-markdown-as-iac.md) | IaC spectrum, companion file ecosystem |
| 11 | [wiki/spine/models/agent-config/model-skills-commands-hooks.md](wiki/spine/models/agent-config/model-skills-commands-hooks.md) | 4-level cost gradient + 26 hook events + Hook Design Pattern |
| 12 | [wiki/spine/models/agent-config/model-claude-code.md](wiki/spine/models/agent-config/model-claude-code.md) | Agent runtime; **second P4 instance discovered in this page (see below)** |
| 13 | [wiki/spine/models/depth/model-context-engineering.md](wiki/spine/models/depth/model-context-engineering.md) | Three-level configuration (prompt/context/structural), OS analogy, three-layer authority |
| 14 | [wiki/spine/models/quality/model-quality-failure-prevention.md](wiki/spine/models/quality/model-quality-failure-prevention.md) | **3-layer defense (structural / teaching / review) — names the layer where the bug lives** |
| 15 | [wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md](wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md) | P1 in full — 25%→100% measured |
| 16 | [wiki/lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md](wiki/lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md) | P2 in full — 25%/60%/90% gradient |
| 17 | [wiki/lessons/04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md](wiki/lessons/04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md) | P3 in full — process must adapt to identity |
| 18 | [wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md](wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md) | P4 in full — 5 cross-layer instances |
| 19 | [wiki/spine/standards/gateway-output-contract.md](wiki/spine/standards/gateway-output-contract.md) | 5 rules: SRP, context-aware, ~60-line ceiling, read-whole marker, closing next-move |
| 20 | [wiki/spine/standards/concept-page-standards.md](wiki/spine/standards/concept-page-standards.md) | Sample of standards corpus — concept page quality bar |
| 21 | [wiki/spine/super-model/enforcement-hierarchy.md](wiki/spine/super-model/enforcement-hierarchy.md) | Sub-super-model navigation hub for enforcement domain |
| 22 | [wiki/backlog/epics/milestone-v2/e022-context-aware-gateway-orientation-and-routing.md](wiki/backlog/epics/milestone-v2/e022-context-aware-gateway-orientation-and-routing.md) | E022 in review; readiness 95%, progress 90%, all 5 stages completed |
| 23 | [wiki/backlog/modules/e022-m002-gateway-orient-subcommand.md](wiki/backlog/modules/e022-m002-gateway-orient-subcommand.md) | M002 design (frontmatter stage:design, code shipped — declaration mismatch) |
| 24 | [wiki/backlog/modules/e022-m003-what-do-i-need-upgrade.md](wiki/backlog/modules/e022-m003-what-do-i-need-upgrade.md) | M003 design (same declaration mismatch with code) |
| 25 | [tools/gateway.py](tools/gateway.py) lines 1-500 | Verified `gateway_orient` + `_orient_brain_fresh` + `_wdin_brain_task_bound` implemented |
| 26 | [.claude/hooks/session-start.sh](.claude/hooks/session-start.sh) | Current reminder is prose pointers, not content injection — bounded by contract size ceiling |
| 27 | [.claude/hooks/post-compact.sh](.claude/hooks/post-compact.sh) | Restores sacrosanct directives + Hard Rules after compaction |
| 28 | [.claude/settings.json](.claude/settings.json) | 4 hooks wired: pre-webfetch, pre-bash, SessionStart, PostCompact |
| 29 | [raw/notes/2026-04-24-operator-directives-session-verbatim.md](raw/notes/2026-04-24-operator-directives-session-verbatim.md) | Verbatim — "behave FROM the project not OVER it", "the project IS intelligent" |
| 30 | [raw/notes/2026-04-25-operator-directive-continue-ingestions-plus-qwen3-6-27b.md](raw/notes/2026-04-25-operator-directive-continue-ingestions-plus-qwen3-6-27b.md) | Verbatim Qwen3.6-27B ingestion directive |
| 31 | [wiki/log/2026-04-23-session-handoff-ai-infrastructure-vision-and-tooling.md](wiki/log/2026-04-23-session-handoff-ai-infrastructure-vision-and-tooling.md) | The mission groundwork — $540→$100 smart-routing finding origin |
| 32 | [wiki/log/2026-04-24-session-handoff-brain-refactor-rules-and-hooks.md](wiki/log/2026-04-24-session-handoff-brain-refactor-rules-and-hooks.md) | The brain refactor session that built the rules + hooks layer |
| 33 | [wiki/log/2026-04-24-top-layer-routing-refactor-claude-md-gap-analysis.md](wiki/log/2026-04-24-top-layer-routing-refactor-claude-md-gap-analysis.md) | The 7-gap analysis Gap 1 of which E022 implements |
| 34 | [wiki/log/2026-04-25-session-handoff-qwen3-6-27b-ingestion-batch.md](wiki/log/2026-04-25-session-handoff-qwen3-6-27b-ingestion-batch.md) | Earlier 2026-04-25 session — 6 ingestions + Qwen3.6-27B spine addendum |
| 35 | ~/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md | AICP's authoritative state — local K2.6 running 0.3 tok/s, smart routing $540→$100 CAD/mo |

That's 35 substantive reads (well above the operator's "20-30+ request" threshold), each producing actual content in context — not summaries.

## The bug — verified diagnosis from project's own evidence

**Verified location**: the bug lives at Layer 2 of [[model-quality-failure-prevention]]'s 3-layer defense:

| Layer | Mechanism | Compliance | Coverage of THIS bug |
|---|---|---|---|
| 1 — Structural prevention | Hooks at tool-call boundaries | ~98% | NO — hooks fire on tool calls; the bug is in response composition |
| **2 — Teaching** | **CLAUDE.md / .claude/rules / skills** | **~60%** | **← bug lives here. Quantified failure mode of instruction-layer enforcement.** |
| 3 — Review | Human gates at boundaries | 100% when engaged | YES — operator catch-and-correct, working empirically every session |

**Verified mechanism gap**: per [[model-skills-commands-hooks]], Claude Code exposes 26 lifecycle events × 7 categories. The categories are: Session, Tool, Permission, Subagent, Task, System, Compaction. **There is no Response category.** No `PreEmit`/`PreResponse` event. The agent's response-composition step — where "answer from internalized summary" vs "tool-call Read first then answer" gets decided — is unreachable by hooks.

**Verified named lesson**: [wiki/lessons/03_validated/methodology-process/the-agent-must-practice-what-it-documents.md](wiki/lessons/03_validated/methodology-process/the-agent-must-practice-what-it-documents.md) — already validated. The wiki teaches it. The agent doesn't reliably practice it. Recurs because it's at Layer 2.

**Verified that E022 is the named fix for Gap 1**, but Gap 1's structural-injection ambition is bounded by the gateway-output-contract Rule 3 size ceiling (~60 lines). The contract was authored 2026-04-15 with the explicit constraint that gateway outputs cannot be exhaustive. E022's `gateway orient` is contract-compliant — it injects identity + 4 principles + 10 verbs + 7 hard rules + pointers to spine, all in ~50 lines. It cannot inject the 286L super-model + 600L of principle pages + 1500L of foundation models. By design.

## Second P4 instance discovered live in the spine

[wiki/spine/models/agent-config/model-claude-code.md](wiki/spine/models/agent-config/model-claude-code.md) at the "How to Adopt → Real instance: this research wiki's harness" callout (line ~509-514) declares:

> - **5 skills** — wiki-agent, evolve, continue, model-builder, notebooklm. Each a folder with `skill.md`.
> - **9 commands** — `/continue`, `/evolve`, `/ingest`, `/review`, `/gaps`, `/status`, `/backlog`, `/log`, `/build-model`.
> - **No hooks yet** — operating at levels 0-1.

Both the skills claim and the hooks claim are wrong:
- **Skills**: [CLAUDE.md](CLAUDE.md) and [.claude/rules/learnings.md](.claude/rules/learnings.md) #5 explicitly state skills are not yet built; `.claude/skills/` does not exist; the names listed (wiki-agent, evolve, continue, model-builder, notebooklm) are commands, not skills. The 2026-04-24 gap-analysis Gap 4 already documented the parallel CLAUDE.md aspirational-declaration about skills.
- **Hooks**: 4 hooks were built 2026-04-24 (`pre-webfetch-corpus-check.sh`, `pre-bash.sh`, `session-start.sh`, `post-compact.sh`) and wired in [.claude/settings.json](.claude/settings.json). The hook layer is live. The pre-bash hook caught a truncation pipe earlier in this very session.

This is a P4 instance at the **spine model layer** — distinct from the 5 instances P4 already documents. The wiki page that teaches what Claude Code IS contains aspirational declarations about its own home project's adoption state.

The fix path per P4 itself: pair every declaration with a verification gate, OR rename/demote the declaration to match reality. Concretely: either build the 5 named skills (porting from commands), OR update model-claude-code.md to say "9 commands at .claude/commands/, skills layer unbuilt, 4 hooks live" — making the spine page reflect verified reality.

## Forward options (durable from prior turn, refreshed)

| # | Action | Approval needed | Comment |
|---|---|---|---|
| **A** | Build first skill at `.claude/skills/answer-from-spine/SKILL.md` — description-matches knowledge-question shapes; body MUSTs reading relevant spine page before answering | Yes — adds new mechanism to brain config | Closes ~60-70% of the Layer-2 gap. Operator's verbatim 2026-04-24 ratifies skills as a designed layer ("skills = 70% deterministic"). |
| **B** | Fix the P4 instance in [[model-claude-code]] — update the "Real instance" callout to verified reality (9 commands, 0 skills, 4 hooks) | Yes — spine model page edit | Eliminates one cross-layer P4 instance the wiki currently exhibits in its own teaching. |
| **C** | Strengthen UserPromptSubmit hook to detect knowledge-question keyword shapes and inject pointer to relevant spine page | Yes — settings.json hook addition | More pointed Layer-2 teaching at prompt-arrival time. Doesn't reach 100% but better than ambient session-start reminder. |
| **D** | Add Evidence 6 to [[self-reference-drift-wiki-must-practice-its-own-teachings\|self-reference-drift lesson]] — this session's surface-answer + the second P4 instance found in spine | Borderline — adding evidence to a validated lesson; the lesson explicitly invites further evidence on Open Question 2 | Closes another instance of the lesson's recurring failure mode. Pipeline post required after. |
| **E** | Operate from the regathered context on actual mission/wiki/whatever work you direct | None — your direction sets the work | The session-by-session catch-and-correct is the working Layer-3 mechanism. Discipline is exercised by doing well, not by adding more brain mechanisms. |

## State at log time

- Wiki pages: 490 (per `pipeline status` at session start)
- Validation: not yet re-run after this log; will be after Write
- Working tree before this log: only [wiki/log/2026-04-25-session-handoff-end-state-with-failures.md](wiki/log/2026-04-25-session-handoff-end-state-with-failures.md) untracked (prior session's handoff, still uncommitted)
- After this log: 2 untracked log files (the prior end-state + this regather)

## Mission anchor — T-0

**2026-04-27 is today.** Per [aicp-session-handoff](file:///home/jfortin/devops-expert-local-ai/docs/SESSION-2026-04-24-HANDOFF.md): mission Stage 5 (80%+ Claude reduction) is reachable on smart cloud-tier routing alone — `Ollama Cloud Pro $27 + OpenRouter for client work ~$60 + local sovereignty fallback` — dropping cloud spend $540 → ~$100 CAD/mo (80% reduction) without hardware investment. The wiki's contribution side is in place per the [[2026-04-25-session-handoff-qwen3-6-27b-ingestion-batch|2026-04-25 ingestion handoff]]: Qwen3.6-27B documented as tier-0 candidate at the spine layer; AICP E008-E012 milestone impacts tracked.

## Relationships

- BUILDS ON: [[2026-04-25-session-handoff-end-state-with-failures|2026-04-25 — End-state handoff (operator-cut)]]
- BUILDS ON: [[2026-04-24-session-handoff-brain-refactor-rules-and-hooks|2026-04-24 — Brain Refactor Handoff]]
- BUILDS ON: [[2026-04-24-top-layer-routing-refactor-claude-md-gap-analysis|2026-04-24 Gap Analysis]] — verified Gap 1 is contract-bounded, not deferred
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1]] — Layer-2 teaching's ~60% compliance manifested again this session
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] — second instance found in [[model-claude-code|Model — Claude Code]] spine page
- DEMONSTRATES: [[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]] — the validated lesson this session adds to
- RELATES TO: [[self-reference-drift-wiki-must-practice-its-own-teachings|Self-Reference Drift]] — Open Question 2 still open
- RELATES TO: [[e022-context-aware-gateway-orientation-and-routing|E022 — Context-Aware Gateway Orientation]] — verified shipped in this session

## Backlinks

[[2026-04-25 — End-state handoff (operator-cut)]]
[[2026-04-24 — Brain Refactor Handoff]]
[[2026-04-24 Gap Analysis]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
[[the-agent-must-practice-what-it-documents|The Agent Must Practice What It Documents]]
[[self-reference-drift-wiki-must-practice-its-own-teachings|Self-Reference Drift]]
[[E022 — Context-Aware Gateway Orientation]]
