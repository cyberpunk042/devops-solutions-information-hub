---
title: "Decision — Extended Thinking to Adaptive Thinking Migration"
aliases:
  - "Decision — Extended Thinking to Adaptive Thinking Migration"
  - "Extended to Adaptive Migration"
type: decision
domain: cross-domain
layer: 6
status: synthesized
confidence: high
maturity: seed
created: 2026-04-16
updated: 2026-04-16
sources:
  - id: opus-4-7-docs
    type: article
    url: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6
  - id: adaptive-thinking-docs
    type: article
    url: https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking
  - id: research-note
    type: wiki
    file: raw/notes/2026-04-16-research-claude-code-2.1.94-to-2.1.111-and-opus-4.7.md
tags: [decision, thinking, adaptive, extended, migration, opus-4.7, breaking-change]
---

# Decision — Extended Thinking to Adaptive Thinking Migration

## Summary

Opus 4.7 removes extended thinking budgets (`budget_tokens` returns 400 error). Adaptive thinking is the only thinking-on mode and is OFF by default. Any harness code, skill, or API call using `thinking: {type: "enabled", budget_tokens: N}` breaks on 4.7. The migration is mandatory for 4.7 adoption but the TIMELINE is a choice: migrate now (accept behavior changes) or stay on 4.6 (defer until prompts are adjusted).

## Decision

> [!success] **Recommended: Gradual migration with 4.6 as default, 4.7 per-task opt-in**
>
> 1. Keep Opus 4.6 as the default model for all harness tasks
> 2. Audit all code for `budget_tokens` references — replace with `thinking: {type: "adaptive"}` + effort level
> 3. Test individual task types on 4.7 with explicit `effort: "high"` or `effort: "xhigh"`
> 4. Move tasks to 4.7 only when verified (same quality, acceptable cost)
> 5. Keep 4.6 as fallback indefinitely — it's not being removed

## Alternatives

> [!abstract]- **Alternative A: Immediate full migration to 4.7**
>
> Switch all tasks to 4.7 immediately. Accept behavior changes. Fix prompts as issues surface.
>
> **Why rejected:** 4.7's "more literal" behavior means existing prompts may produce worse results. The turnCount bug showed what happens when lifecycle thresholds change unexpectedly. Multi-task cost growth means 35% tokenizer increase compounds across runs. Too many variables changing at once.

> [!abstract]- **Alternative B: Stay on 4.6 indefinitely**
>
> Don't upgrade. 4.6 continues to work. Extended thinking budgets still available.
>
> **Why rejected:** 4.7 has genuine improvements (better memory, task budgets, more reliable literal following). Staying on 4.6 forfeits these. Also: 4.6 will eventually reach end of support, and prompt patterns that only work on 4.6 create technical debt.

> [!abstract]- **Alternative C: Per-project model selection**
>
> OpenArms stays on 4.6 (harness-heavy, prompt-sensitive). The second brain moves to 4.7 (knowledge work, better memory). OpenFleet evaluates independently.
>
> **Why this is the actual recommended approach:** Different projects have different sensitivity to behavior changes. The harness is the most sensitive. The second brain's solo-session work is less prompt-dependent. Per-project evaluation with shared findings is the Goldilocks approach.

## Rationale

The migration is driven by three factors:

1. **4.7 is strictly better for some tasks** — file-based memory, task budgets, literal instruction following. Knowledge work and explicit task specs benefit.
2. **4.7 is different (not worse) for other tasks** — fewer subagents, fewer tool calls, stricter interpretation. Harness tasks calibrated for 4.6's generous inference need prompt updates.
3. **The tokenizer change is a hidden cost multiplier** — 35% more tokens per message means context budgets, compaction triggers, and cost estimates all shift. This is the highest-risk change because it's invisible until you measure.

## Reversibility

> [!info] Easy to reverse
>
> Opus 4.6 remains available. The CLI backup (`~/.claude-code-backups/2.1.94/`) preserves the old version. Running both in parallel (`claude-old` for 4.6, `claude` for 4.7) is supported. The migration can proceed task-by-task and roll back per-task.

## Dependencies

- OpenArms: audit harness code for `budget_tokens` before ANY 4.7 testing
- OpenFleet: fleet dispatch may need model-per-agent routing
- AICP: complexity scorer gains a model-selection output dimension
- Second brain: low risk for solo-session work; can move to 4.7 first

## Migration Checklist

- [ ] Backup current CLI version (DONE — `~/.claude-code-backups/2.1.94/`)
- [ ] Audit all harness code for `budget_tokens` references
- [ ] Audit all harness code for `temperature`/`top_p`/`top_k` (removed in 4.7)
- [ ] Update compaction triggers for 35% token increase
- [ ] Update cost budgets for 35% token increase
- [ ] Test 3 representative task types on 4.7 with explicit effort levels
- [ ] Compare quality metrics: completion rate, manual-fix rate, cost per task
- [ ] Document per-task model recommendation (4.6 vs 4.7)
- [ ] Update `methodology.yaml` or harness config to support model selection per task

## Relationships

- RELATES TO: [[model-claude-code|Model — Claude Code]] — model coexistence routing table
- RELATES TO: [[model-context-engineering|Model — Context Engineering]] — model-specific token budgets
- RELATES TO: [[model-local-ai|Model — Local AI ($0 Target)]] — three-tier cloud routing
- RELATES TO: [[agent-execution-cost-optimization-stack|Cost Optimization Stack]] — effort + model as cost levers
- RELATES TO: [[[[right-size-the-methodology-model-to-the-actual-work-not-the|Right-Size Methodology Model]] — methodology model + Claude model = two optimization dimensions]]

## Backlinks

[[model-claude-code|Model — Claude Code]]
[[model-context-engineering|Model — Context Engineering]]
[[model-local-ai|Model — Local AI ($0 Target)]]
[[agent-execution-cost-optimization-stack|Cost Optimization Stack]]
[[Right-Size Methodology Model]]
