---
title: "Lesson — MCP discipline: register only what's referenced and actually used; useless MCPs eat context budget and confuse, never pre-emptive"
aliases:
  - "MCP Discipline Lesson"
  - "Don't Overflow MCPs"
  - "MCP Anti-Pre-Emption"
  - "Referenced-and-Used Rule for MCPs"
type: lesson
domain: cross-domain
layer: 2
status: synthesized
confidence: high
maturity: seed
created: 2026-05-08
updated: 2026-05-08
last_reviewed: 2026-05-08
sources:
  - id: operator-directive-2026-05-05-mcp-discipline
    type: file
    file: raw/notes/2026-05-05-blockers-channel-progress-tracker-decisions-logbook-tools-mcp-discipline.md
    description: "Operator-explicit 2026-05-05 directive (verbatim, sacrosanct): *'MCP we must not overflow especially with things that are useless or confusing or useless or we dont even refer to anywhere so will never be used...'* — note 'useless' repeated; emphasis intentional. Directive E of the governance + tools/MCP discipline directive."
  - id: learnings-rule-5
    type: wiki
    file: .claude/rules/learnings.md
    description: "Hard Rule #5 — Don't conflate skills, commands, and hooks; sister doctrine — MCPs are at a different mechanism layer (programmatic, AI-invoked) but the no-overflow rule applies similarly"
  - id: routing-rules
    type: wiki
    file: .claude/rules/routing.md
    description: "30-tool MCP catalog — defines what MCPs ARE registered + their mapping to operator intents; this lesson governs WHEN to add a new MCP (only when the catalog entry is referenced and actually used)"
  - id: skills-commands-hooks-model
    type: wiki
    file: wiki/spine/models/agent-config/model-skills-commands-hooks.md
    description: "5-mechanism determinism ladder — MCPs are programmatic / AI-invoked / deferred-load via ToolSearch; useless MCPs occupy the catalog without contributing to the determinism ladder"
  - id: structured-context-principle
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md
    description: "P2 — Structured Context Governs Agent Behavior; useless MCPs in the catalog are unstructured noise that contributes nothing to behavior — violates P2's signal-to-noise discipline"
  - id: declarations-aspirational-principle
    type: wiki
    file: wiki/lessons/04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md
    description: "P4 — Declarations Aspirational Until Verified; declaring 'we have MCP X' is aspirational until an actual operator-intent route references X AND the route is actually used"
  - id: feedback-research-not-abstract
    type: notes
    file: ~/.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/feedback_research_not_abstract.md
    description: "Operator memory — research concrete products, don't abstract; sister discipline — register concrete used MCPs, don't pre-author hypothetical ones"
tags: [lesson, mcp, mcp-discipline, no-overflow, no-pre-emptive-registration, referenced-and-used-rule, context-budget, signal-to-noise, sister-project-applicable, layer-2, agent-config-discipline, mission-2026-05-08]
---

# Lesson — MCP discipline: register only what's referenced and actually used

## Summary

Operator-doctrinal directive (2026-05-05, verbatim sacrosanct): *"MCP we must not overflow especially with things that are useless or confusing or useless or we dont even refer to anywhere so will never be used..."* The MCP catalog (currently 28 tools in this project per `.claude/rules/routing.md`) carries a context-budget cost: every registered MCP shows up in deferred-tool listings the agent must reason about, even when not invoked. The operator's anti-overflow rule has three load-bearing predicates: an MCP belongs in the catalog if and only if (1) **referenced** somewhere in the agent-config layers (CLAUDE.md / AGENTS.md / .claude/rules/ / commands / patterns / lessons), (2) **routes to a concrete operator-intent** (operator-says-X → invoke MCP-Y), and (3) **actually used** at non-trivial frequency in operator-driven sessions. MCPs failing all three predicates eat context budget without contributing to behavior, AND introduce confusion (the agent reaches for a no-op tool when a better path exists). **The doctrine generalizes**: every layer of the agent-config (skills / commands / hooks / MCPs / rules / patterns) has a finite signal-to-noise budget; pre-emptive registration of "might be useful eventually" entries violates the budget without earning return. This lesson sits sister to [`learnings.md` Rule #5 (don't conflate skills/commands/hooks)](../../../.claude/rules/learnings.md) and to [Principle 2 (Structured Context Governs Agent Behavior)](../04_principles/hypothesis/structured-context-governs-agent-behavior-more-than-content.md): structured context that the agent doesn't act on is noise; structured context that the agent CAN'T act on (because the MCP route is unreferenced) is worse than noise — it's misleading invitation.

## Context

> [!info] **When this lesson applies**
>
> | Decision class | Apply this doctrine? |
> |---|---|
> | Adding a new MCP server to `.mcp.json` | **YES** — must satisfy the 3-predicate test |
> | Registering a tool inside an existing MCP server | **YES** — same 3-predicate test |
> | Adding a slash command in `.claude/commands/` | **YES** (sister discipline; same predicate logic per the routing matrix in `.claude/rules/routing.md`) |
> | Adding a skill in `.claude/skills/` | **YES** (when skills are built — currently this project doesn't have skills) |
> | Removing an existing MCP that fails the 3-predicate test | **YES** — operator-decision; surface for batch review |
> | One-off transient lookups via WebFetch / Bash | NO — those are operator-driven inline tools, not catalog-registered MCPs |

## Insight

> [!success] **An MCP belongs in the catalog only if it satisfies all 3 predicates: referenced + routes-to-intent + actually-used.**
>
> | # | Predicate | What it means | Verification |
> |---|---|---|---|
> | 1 | **Referenced** | Some agent-config layer (CLAUDE.md / AGENTS.md / .claude/rules/ / commands / patterns / lessons) names this MCP by name or by intent | grep the agent-config layers for the MCP name; if no hit, predicate fails |
> | 2 | **Routes-to-intent** | An operator-intent → MCP route exists (e.g., per the 24-row routing table in [`.claude/rules/routing.md`](../../../.claude/rules/routing.md)) | check the routing table; if the MCP isn't a "primary tool" or "CLI fallback" for any operator-intent row, predicate fails |
> | 3 | **Actually used** | Sessions invoke the MCP at non-trivial frequency (operator-driven workloads exercise it) | observability / OTEL data; if zero invocations across N recent sessions, predicate fails |
>
> **All three required.** A reference without a route is dead documentation. A route without usage is aspirational architecture. Usage without reference + route is rogue tooling that drifts from the agent-config doctrine.

## Evidence

> [!success]- **Evidence 1 — Operator-stated 2026-05-05 (verbatim, sacrosanct)**
>
> > *"MCP we must not overflow especially with things that are useless or confusing or useless or we dont even refer to anywhere so will never be used..."*
>
> Note: "useless" appears twice in the verbatim. Per [feedback_register_dont_research_when_operator_states_a_fact](../../../.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/feedback_register_dont_research_when_operator_states_a_fact.md) and operator's general framing on emphasis, repeated words denote weight. The operator's emphasis is on the anti-overflow rule.

> [!success]- **Evidence 2 — The 28-tool MCP catalog example (this project)**
>
> Per [`.claude/rules/routing.md`](../../../.claude/rules/routing.md): the project registers 28 MCP tools. Each tool is referenced in the routing table (predicate 1 + 2 satisfied). Predicate 3 (actually used) varies: gateway-orient + wiki-search + wiki-fetch + pipeline-post fire frequently; mirror-to-notebooklm + integrations fire rarely. **An MCP that fired zero times across 30 sessions is a candidate for catalog removal pending operator-decision** — but the catalog stays under 30 entries by careful curation. **No pre-emptive additions.**

> [!success]- **Evidence 3 — Phantom-MCP gap closed 2026-04-27 (P4 instance)**
>
> Per [`.claude/rules/routing.md`](../../../.claude/rules/routing.md) verification gate note: an earlier "30 tools" claim included 2 phantom entries (`wiki_pages` + `wiki_root`) that were never implemented. The mismatch was surfaced by `gateway navigate`'s computed-count fix; phantom entries removed; catalog now reflects actual implementation. **This is a [P4](../04_principles/hypothesis/declarations-are-aspirational-until-infrastructure-verifies-them.md) instance — declarations aspirational until verified — applied at the MCP catalog layer.** The verification gate is: count `@server.tool()` decorators in `tools/mcp_server.py` and reconcile with the catalog. If the count differs from the documented number, phantom entries exist.

> [!success]- **Evidence 4 — Useless MCPs ALSO confuse, not just bloat**
>
> Operator-named two distinct failure modes: *"useless or confusing or useless or we dont even refer to anywhere"*. **Confusion** is the agent reaching for a registered MCP that doesn't actually serve the workload — wasting reasoning steps, producing wrong-tool errors, or generating misleading completions. The fix is the same as for bloat (predicate-based curation), but the failure-mode is different (correctness, not just budget).

## Applicability

> [!info] **The 3-predicate test as a decision tool**
>
> | Scenario | Test result | Action |
> |---|---|---|
> | New MCP idea, no agent-config reference yet, no routing entry | All 3 predicates fail | DON'T register; add reference + routing entry FIRST, then evaluate after operator validates intent |
> | New MCP idea, reference exists, no routing entry | Predicate 2 fails | Add routing entry; if no operator-intent fits, predicate 2 still fails — DON'T register |
> | New MCP idea, all 3 predicates pass | Eligible | Register; track usage; review after N sessions |
> | Existing MCP, predicate 3 fails (zero usage in 30+ sessions) | Predicate 3 fails | Surface for operator-decision; remove if operator confirms unused |
> | Existing MCP, predicate 1 or 2 fails (orphaned) | 1 or 2 fails | Surface for operator-decision; either restore reference/routing OR remove |

## How to Apply

> [!tip] **Concrete checklist before adding an MCP**
>
> 1. **Identify the operator-intent** the MCP serves. If you can't name a verbatim operator-intent line ("operator says X → invoke this MCP"), STOP — predicate 2 will fail.
> 2. **Find the agent-config reference.** Update CLAUDE.md / AGENTS.md / .claude/rules/ / a command file / a lesson to name the MCP and explain when to use it. If no natural place exists, predicate 1 fails — STOP.
> 3. **Estimate session-frequency.** Will this fire in operator-driven sessions, or just in hypothetical-workload-X-someday? Predicate 3 evidence comes only after registration; estimate honestly. If frequency estimate is "rare" without operator confirmation of intent, defer.
> 4. **Register, then track.** Add to the MCP catalog. Add observability (per [Claude Code skill chaining synthesis](../../sources/tools-integration/src-claude-code-skill-chaining-fork-files-commands-85-percent-less-context.md): OTEL is easier than ever). Review usage after N sessions.
> 5. **Cull if unused.** If the MCP fires zero times in N sessions and operator hasn't asked for it, surface for removal. **Don't preserve dead entries out of sentimental architecture.**

> [!warning] **Anti-patterns**
>
> - **Pre-emptive MCP registration**: "we might want X someday" — predicate 3 starts at zero and stays there
> - **Generalist MCPs**: "search-everything" / "get-anything" tools that don't map to a specific operator-intent — predicate 2 fails
> - **Convenience-driven additions**: "it would be cool if the agent could do Y" — operator-intent comes from the operator, not from the agent's convenience
> - **Phantom catalog entries**: documented but unimplemented MCPs — P4 violation; surfacing the gap is mandatory
> - **Forgetting to remove**: keeping the catalog bloated because removal is annoying — anti-overflow discipline is also anti-bloat-by-inertia

## Open Questions

> [!question] What's the right cadence for the predicate-3 (usage) review?
> Per-session is too frequent (most MCPs naturally fire intermittently); never is too sparse (dead entries accumulate). **Default proposal**: review at session-handoff time (when the operator commits + compacts), surface zero-usage entries for batch operator-decision. Operator-decision per workload pattern.

> [!question] Does this lesson apply equally to skills (when built) and slash commands?
> YES per the structural pattern — every layer of the agent-config has a signal-to-noise budget. But the predicate-3 evidence is different per layer: skills auto-trigger on prose; commands fire on operator slash; MCPs fire on AI-driven reasoning. **Per-layer instantiation of the same doctrine.**

> [!question] Should removed MCPs be archived or deleted entirely?
> Archive is the safer default (the implementation may have non-trivial code; deletion loses that). **Default proposal**: move to `tools/mcp_server_archived/` with a header documenting removal date + reason; if the implementation never resurfaces in 6 months, delete entirely.

> [!question] How does this lesson compose with the [[end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers|Multi-Layer Compression Lesson]]?
> Compression operates on REGISTERED content (compressed prompts, compressed weights, etc.). MCP discipline operates on CATALOG content (what's registered to be compressible at all). **Sister disciplines**: compression maximizes leverage of what's registered; MCP discipline minimizes pre-emptive registration. Both compound at the structured-context layer.

## Self-Check — Am I About to Make This Mistake?

> [!warning] Before adding an MCP to the catalog, ask:
>
> 1. **Did the operator name the intent?** Or am I anticipating?
> 2. **Is there a verbatim operator-quote tying intent → tool?** Or am I extrapolating?
> 3. **Will this fire in operator's actual workloads?** Or am I imagining hypothetical workloads?
> 4. **If I were debugging an unused MCP six months from now, would I be glad I added this?** Or would I want to revert?
> 5. **Is there a simpler path** (Bash + existing tool, slash command, or just operator-driven prose) that doesn't require catalog registration?

If any answer is "no" or "maybe," DON'T register. Defer until operator validates the intent.

## Relationships

- BUILDS ON: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]] — useless MCPs are noise that violates P2's signal-to-noise discipline
- BUILDS ON: [[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]] — MCP catalog declarations require verification (count + usage)
- RELATES TO: [[end-to-end-compression-across-the-ai-stack-composes-multiplicatively-6-plus-independent-mechanisms-at-6-distinct-layers|Multi-Layer Compression Lesson]] — sister discipline; compression maximizes leverage of registered content, MCP discipline minimizes pre-emptive registration
- RELATES TO: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] — substitutability requires substitutable axes that are actually USED, not just theoretically registered
- DEMONSTRATES: [[goldilocks-protocol|Goldilocks Protocol]] — pick MCP set per workload; not all MCPs apply to all sessions

## Backlinks

[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context Governs Agent Behavior]]
[[declarations-are-aspirational-until-infrastructure-verifies-them|Principle 4 — Declarations Aspirational Until Verified]]
[[Multi-Layer Compression Lesson]]
[[Anti-Vendor-Lock-In Lesson]]
[[Goldilocks Protocol]]
