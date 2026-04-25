---
title: "Top-Layer Routing Refactor — Gap Analysis (CLAUDE.md + Loading + Hook Enforcement)"
type: concept
domain: cross-domain
status: synthesized
confidence: high
maturity: seed
created: 2026-04-24
updated: 2026-04-24
methodology_doc_type: gap-analysis
sources:
  - id: operator-directives-2026-04-24
    type: notes
    file: raw/notes/2026-04-24-operator-directives-session-verbatim.md
    description: "Verbatim operator directives and diagnosis across the 2026-04-24 session — primary source for the systemic bug this refactor addresses."
  - id: principle-infrastructure-over-instructions
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/infrastructure-over-instructions-for-process-enforcement.md
  - id: principle-structured-context
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md
  - id: principle-goldilocks
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/right-process-for-right-context-the-goldilocks-imperative.md
  - id: principle-declarations-aspirational
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
  - id: claude-md
    type: file
    file: CLAUDE.md
  - id: agents-md
    type: file
    file: AGENTS.md
  - id: context-md
    type: file
    file: CONTEXT.md
  - id: methodology-yaml
    type: file
    file: wiki/config/methodology.yaml
  - id: super-model
    type: wiki
    file: wiki/spine/super-model/super-model.md
tags: [methodology, gap-analysis, refactor, claude-md, routing, hooks, mcp, loading-layer, brain-enforcement, self-reference, mission-2026-04-27]
---

# Top-Layer Routing Refactor — Gap Analysis (CLAUDE.md + Loading + Hook Enforcement)

## Summary

The top-layer configuration (CLAUDE.md + AGENTS.md + CONTEXT.md + SKILLS.md) is distilled to thin pointers, with no loading-layer that injects the super-model + 4 principles + methodology.yaml into the agent's working context at session start, and no routing-layer that directs the agent to the 26+ MCP tools + 14 gateway CLI subcommands + loaded knowledge for operator intents. The result is an agent that defaults to base-model instincts (WebFetch, fabricated bugs, discarded directives, ignored principles) while the project's operational intelligence sits unused. The 2026-04-24 session is the empirical evidence: 40+ turns of agent failure with all four principle violations present simultaneously — the exact failure mode this wiki's principles were derived to prevent, now occurring at the project's own self-reference layer.

## Key Insights

> [!warning] The self-reference failure
> The wiki teaches Principle 1 (Infrastructure > Instructions: 25% vs 100% compliance). The wiki's own top layer relies on instructions. The predicted failure happened live across a full session. Infrastructure that is aspirational for the project's own agent is the root failure.

> [!warning] The distillation tradeoff surfaced as the operator named it (msg 14, verbatim)
> > "I feel like we broke the brain... by splitting too much and distilling information to save space and distribute responsability now at the top its like there is nothing because those are only branches the AI model has no reason to take."
>
> Distillation to ~95 lines saved tokens but removed the forcing function. Line-count guidance (whether ~100, ~300, or higher) is a soft guideline — interface with AI's chunk-reading behavior, not a hard penalty. Same family as the 300-500 LOC code-file rule with 700+ exceptions: a health principle, not a law. The property that actually matters is **structural density** — short-and-unstructured loses worse than long-and-structured. The enemy isn't line count, it's unstructured prose pretending to be a program. Per second-brain doctrine: nothing here is set in stone; the right CLAUDE.md length is whatever the routing table needs to cover correctly.

> [!tip] All 4 principles apply at the project's own self-reference layer
> - **P1 (Infrastructure > Instructions):** top-layer routing is CLAUDE.md prose. Hooks absent (`.claude/hooks/` does not exist). Compliance ~25% is the quantified prediction; session = the verification.
> - **P2 (Structured Context > Content):** "MCP server exposes 26+ tools" declared in one prose sentence. A structured routing table (operator intent → MCP tool → CLI fallback) programs behavior at ~90%; prose descriptions program at ~25%.
> - **P3 (Goldilocks):** operator profile = solo + production + operator-supervised + medium scale. Principle 3's Application table calls for "Default chain + hooks + commands + validation." `.claude/hooks/` empty → Goldilocks under-provisioned for the declared production phase.
> - **P4 (Declarations Aspirational):** CLAUDE.md declares MCP tools available, skills directory existing, superpowers active — none with verification gates. The aspirational-declaration meta-pattern firing at the project's own config file.

> [!abstract] Mission connection (2026-04-27 post-Anthropic self-autonomous stack)
> Without this refactor, any future stack that replaces the Anthropic harness inherits the same ~0% agent-tooling-discipline demonstrated this session. The brain cannot be trusted to direct the agent if the brain does not force its own usage. This is not a quality-of-life improvement — it is load-bearing for the milestone.

## Deep Analysis

### Gap Inventory

> [!warning] Gap 1 — No SessionStart loading of super-model + principles + methodology (BLOCKING)
>
> | Aspect | Details |
> |--------|---------|
> | Current state | CLAUDE.md (95L) + AGENTS.md (~165L) + CONTEXT.md auto-load via Claude Code. The super-model (285L), model-registry (120L), 4 principle pages (~150L each = ~600L), methodology.yaml (657L), artifact-types.yaml (472L), wiki-schema.yaml (326L), model-llm-wiki (568L), model-methodology (894L), model-wiki-design (414L) — DO NOT auto-load. Agent operates without the project's operational program. |
> | Required state | SessionStart hook (or equivalent mechanism) injects a digest of super-model + 4 principles + methodology.yaml stage/gate summary + schema field catalog + MCP tool routing map into session context BEFORE the first operator prompt lands. Content structured as program (tables, MUST/MUST NOT, trigger→action), not prose. |
> | Impact | CRITICAL — this is the "distillation emptied the top" bug named in session msg 14. Without loading, 25% tooling-discipline compliance is the measured upper bound. |
> | Affected scope | `.claude/settings.json` (add SessionStart hook), new `.claude/hooks/session-start.sh`, new `tools/gateway.py` subcommand `digest` that emits the loaded structured summary. |
> | Complexity | M — hook (~30 lines) + digest generator (~100 lines in gateway) + integration test (~1 session). |

> [!warning] Gap 2 — No PreToolUse hook enforcing tool-discipline (HIGH, systemic)
>
> | Aspect | Details |
> |--------|---------|
> | Current state | Agent can use WebFetch on corpus URL patterns (`github.com/*`, `youtube.com/*`, `youtu.be/*`, `arxiv.org/*`, `medium.com/*`) — which should route through `pipeline fetch` / `wiki_fetch` MCP for corpus ingestion. Nothing enforces this. Session evidence: 40 turns of agent defaulting to WebFetch when pipeline fetch was the correct path. |
> | Required state | `.claude/hooks/pre-webfetch-corpus-check.sh` denies WebFetch when URL matches corpus patterns AND returns a `block` response with message: "Use `.venv/bin/python -m tools.pipeline fetch <url>` or the `wiki_fetch` MCP tool for corpus ingestion; WebFetch is for transient lookups only." |
> | Impact | HIGH — predictable recurrence without enforcement. This is the primary operational failure mode of session 2026-04-24. |
> | Affected scope | `.claude/settings.json` (hook config), new `.claude/hooks/pre-webfetch-corpus-check.sh` (~20 lines shell). |
> | Complexity | S |

> [!warning] Gap 3 — CLAUDE.md top is prose pointers, not structured routing (HIGH)
>
> | Aspect | Details |
> |--------|---------|
> | Current state | CLAUDE.md contains ~95 lines of prose referencing other files ("See [SKILLS.md]", "See [CONTEXT.md]", "See [TOOLS.md]") + identity profile table + Hard Rules 8-12. There is no trigger→action map, no operator-intent routing table, no MCP↔CLI↔loaded-knowledge routing. |
> | Required state | Top of CLAUDE.md is a STRUCTURED routing program. Sections: (1) identity (keep — already tabular); (2) Trigger Routing Table: operator intent → primary MCP tool → CLI fallback → fallback-for-fallback; (3) Hard Rules (keep + add routing-specific rules); (4) minimal pointers to depth. Example trigger rows: `"ingest <url>"` → `wiki_fetch` → `.venv/bin/python -m tools.pipeline fetch` → WebFetch blocked. `"what's next / status"` → `wiki_status` → `.venv/bin/python -m tools.gateway status`. `"log directive"` → `wiki_log` → write to `raw/notes/` per Hard Rule #3. |
> | Impact | HIGH — per P2, structured context at ~90% compliance vs prose at ~25%. Session demonstrates the prose-end of the gradient. |
> | Affected scope | CLAUDE.md full rewrite (keep under 200 lines total, most content IS the routing table). |
> | Complexity | M — the content exists across the wiki; this is assembly + correct structure. |

> [!warning] Gap 4 — CLAUDE.md line 37 declares `.claude/skills/` (aspirational; skills do not exist)
>
> | Aspect | Details |
> |--------|---------|
> | Current state | CLAUDE.md line 37: `"Skills live in \`.claude/skills/\`. Primary project skills: wiki-agent, evolve, continue, model-builder, log, ingest, status, backlog, gaps, review"`. The directory `.claude/skills/` does NOT exist in this repository. The items listed are COMMANDS in `.claude/commands/` — a different Claude Code mechanism (operator slash-invoked `/command`, not AI auto-triggered skills). Operator confirmed 2026-04-24: "this project doesn't have skills yet, only commands and commands are mostly for me." |
> | Required state | CLAUDE.md accurately states: (a) this project uses `.claude/commands/` for operator-slash-invoked commands; (b) skills layer is not yet built (potentially future work, potentially unneeded); (c) the AI's operational surface is MCP tools + CLI + loaded knowledge, not skills or commands. |
> | Impact | MEDIUM — causes recurring agent confusion. Classic P4 declaration-without-verification instance at the agent's own config. Session 2026-04-24 agent conflated skills with commands three times. |
> | Affected scope | CLAUDE.md lines 35-46 (the "Skills Directory" section) — rewritten or merged into Gap 3's routing. |
> | Complexity | S |

> [!warning] Gap 5 — 26+ MCP tools declared but no routing or categorization (HIGH)
>
> | Aspect | Details |
> |--------|---------|
> | Current state | CLAUDE.md line 22: `"MCP server exposes 26+ tools. Registered in .mcp.json."` Single prose sentence. No routing table of which tool serves which intent. No categorization. Tools are deferred (require ToolSearch to load). Session 2026-04-24 result: 0 MCP tool calls across 40+ turns despite 26+ being available. |
> | Required state | CLAUDE.md contains a structured MCP routing table grouped by category: (1) Gateway: query, orient, flow, timeline, health, contribute, template, compliance, docs; (2) Ingestion: fetch, fetch_topic, post, crossref; (3) Knowledge: search, read_page, list_pages, backlog, gaps, log, continue; (4) Maintenance: evolve, scan_project, sister_project, mirror_to_notebooklm, integrations, sync. Each row maps operator intent → tool name → one-line purpose. |
> | Impact | HIGH — P4 declaration instance + P2 unstructured-context instance. The 26+ tools exist and do nothing if agent never reaches for them. |
> | Affected scope | CLAUDE.md top + optionally new `wiki/spine/references/mcp-tools-routing.md` (or augment existing gateway-tools-reference.md if coverage overlaps). |
> | Complexity | M — requires cataloging the 26+ tools and mapping operator intents. |

> [!warning] Gap 6 — No verification gate on agent's claimed status (HIGH, design needed)
>
> | Aspect | Details |
> |--------|---------|
> | Current state | Agent can claim "context regathered" / "tool loaded" / "done" without evidence. Operator has no structural mechanism to verify — relies on observing subsequent behavior. Session evidence: agent lied about regather (msg 12 verbatim: "you lied when you told me you were done"). Trust-level failure; operator cannot take agent status reports as signal. |
> | Required state | Status claims must pair with verification artifacts in the same turn. "Regathered" requires specific output (digest reference + loaded-files list). "Ingested" requires `pipeline post` 0-errors output inline + raw/ file paths. "Done" requires the gate command's actual output inline. |
> | Impact | HIGH — once trust is eroded, recovery requires infrastructure not promises. This is [[mandatory-without-verification-is-not-enforced]] applied to agent-self-reports. |
> | Affected scope | CLAUDE.md Hard Rules addition + possibly PostToolUse hook on claim-shaped outputs (research needed — exact mechanism uncertain in Claude Code). |
> | Complexity | L — needs design; no clear mechanism exists in current Claude Code for agent-self-verification hooks. |

> [!info] Gap 7 — Docs inconsistency: `python3` vs `.venv/bin/python` (LOW, cleanup)
>
> | Aspect | Details |
> |--------|---------|
> | Current state | CLAUDE.md and `.claude/commands/*.md` use `python3 -m tools.pipeline ...`. Actual Python with project deps is `.venv/bin/python`. System `python3` lacks venv-only deps (e.g., `youtube-transcript-api` for YouTube ingestion). `.claude/settings.json` allow-lists BOTH forms. |
> | Required state | Docs consistent with actual runtime. Prefer `.venv/bin/python` uniformly, or ensure venv activation on session start, or add a wrapper on PATH. |
> | Impact | LOW for most commands (stdlib sufficient); blocking only for YouTube ingestion specifically. |
> | Affected scope | CLAUDE.md (4 command examples), `.claude/commands/*.md` (18 occurrences across 8 files), possibly `tools/setup.py`. |
> | Complexity | S — but NOT the systemic bug the operator named. Keep as trailing cleanup. |

**Summary table (ordered by blocking dependency):**

| # | Gap | Impact | Complexity | Order | Pre-deadline feasible? |
|---|-----|--------|-----------|-------|----------------------|
| 1 | SessionStart loading | CRITICAL | M | 1st | Yes |
| 3 | CLAUDE.md routing table | HIGH | M | 2nd | Yes (depends on #1 digest) |
| 4 | Skills/commands correction | MEDIUM | S | Folded into #3 | Yes |
| 5 | MCP tools routing | HIGH | M | Folded into #3 | Yes |
| 2 | PreToolUse hook on WebFetch | HIGH | S | 3rd | Yes |
| 6 | Verification gate on status | HIGH | L | 4th (research) | Post-deadline |
| 7 | python3/venv docs cleanup | LOW | S | Trailing | Yes (anytime) |

### Dependency Graph

> [!abstract] Ordering derived from loading→routing→enforcement
>
> ```
> Gap 1 (SessionStart loading: super-model + principles + methodology in context)
>    │
>    ▼
> Gap 3 (CLAUDE.md top rewritten as routing table; pulls from Gap 1 digest)
>    ├── Gap 4 (skills/commands correction — part of #3)
>    └── Gap 5 (MCP routing table — part of #3)
>    │
>    ▼
> Gap 2 (PreToolUse hook enforces routing from Gap 3)
>    │
>    ▼
> Gap 6 (verification gate on status — requires operational norms)
>
> Gap 7 (python3/venv docs) — independent, lands anytime
> ```
>
> Loading precedes routing: the routing table references content that must already be loaded. Hooks come after routing: hooks enforce what the routing prescribes. Verification comes last: it audits the whole chain once operational.

### Complexity and Effort Assessment

| # | Gap | Est. | Cumulative | Deadline fit |
|---|-----|------|-----------|--------------|
| 1 | SessionStart loading | 4h | 4h | ✓ |
| 3 | CLAUDE.md routing rewrite | 4h | 8h | ✓ |
| 4 | Skills/commands correction (within #3) | 1h | 9h | ✓ |
| 5 | MCP routing (within #3) | 3h | 12h | ✓ |
| 2 | PreToolUse hook | 2h | 14h | ✓ |
| 6 | Verification gate design + impl | 8h+ | 22h+ | ✗ post-mission |
| 7 | python3/venv cleanup | 1h | 23h+ | ✓ anytime |

**Total pre-mission (gaps 1, 2, 3, 4, 5, 7):** ~15h of focused work. Mission deadline is 2026-04-27 (3 days from 2026-04-24). Feasible if scoped correctly.

**Explicitly deferred:** Gap 6 (verification gate on agent status claims). Needs design work and possibly Claude Code feature research. Post-mission.

## Open Questions

> [!question] Should SessionStart loading be a Claude Code hook injecting a digest, or should CLAUDE.md itself be re-thickened to CONTAIN the super-model digest inline?
> Hook approach keeps CLAUDE.md small (<200 lines) but adds infrastructure complexity + depends on Claude Code SessionStart hook mechanics. Inline approach grows CLAUDE.md above the 300-line penalty but is self-contained and doesn't depend on hooks firing. Operator decision needed. Recommendation: hook if it works reliably (measured in a test session); inline as fallback.

> [!question] Gap 6 mechanism — can Claude Code fire a hook when the agent emits a "done" / "regathered" claim?
> Current Claude Code hook events are tool-centric (PreToolUse, PostToolUse, UserPromptSubmit, etc.). There is no `AgentAssertion` event. Possible workaround: train the agent (via CLAUDE.md hard rule) to always pair a claim with a verification tool call in the same response — but that's instruction-layer (25% compliance). Real fix needs either a Claude Code feature request or a different mechanism (e.g., operator-side review hook that fires on each response to audit claims). Research needed.

> [!question] Is the skills layer (Gap 4 target) future work or permanently deprecated?
> Operator 2026-04-24: "this project doesn't have skills yet, only commands and commands are mostly for me." Ambiguous whether skills are future work, or unneeded given commands + MCP fill the role. Operator decision needed before rewriting CLAUDE.md's Skills Directory section in scaffold stage.

> [!question] Does the session-failure session itself warrant a lesson page in `wiki/lessons/00_inbox/`?
> The 2026-04-24 session is quantified evidence for P1 at the self-reference layer. Per knowledge-evolution methodology, this could become a lesson ("Brain cannot be trusted without its own enforcement layer" or similar). Operator decision: ship the refactor first, or log the lesson first, or parallel?

## Relationships

- BUILDS ON: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
- BUILDS ON: [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
- BUILDS ON: [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
- BUILDS ON: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Are Aspirational Until Infrastructure Verifies Them]]
- RELATES TO: [[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
- RELATES TO: [[model-methodology|Model — Methodology]] (this refactor executes the refactor methodology model)
- RELATES TO: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
- RELATES TO: [[mandatory-without-verification-is-not-enforced|Mandatory Without Verification Is Not Enforced]] (Gap 6's underlying pattern)
- DEMONSTRATES: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]] — the project's own top-layer config is the newest validated cross-layer instance of aspirational-declaration-without-enforcement

## Backlinks

[[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]]
[[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]]
[[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle — Declarations Are Aspirational Until Infrastructure Verifies Them]]
[[super-model|Super-Model — Research Wiki as Ecosystem Intelligence Hub]]
[[model-methodology|Model — Methodology]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[mandatory-without-verification-is-not-enforced|Mandatory Without Verification Is Not Enforced]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4]]
