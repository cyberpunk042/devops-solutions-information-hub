---
title: "Auto-Compact Detection Failure + Auto-Compact MUST Be Disabled — Operator Priority Directive 2026-05-08"
type: note
note_type: operator-directive-verbatim
domain: raw
status: raw
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: operator-prompt-2026-05-08-post-compact
    type: conversation
    description: "Operator's verbatim directive immediately after agent failed to detect post-compact state and was about to run pipeline post without regathering context"
tags: [operator-directive, sacrosanct, auto-compact, post-compact-detection-failure, priority, regather-context, register-and-create-tasks]
---

# Auto-Compact Detection Failure + Auto-Compact MUST Be Disabled — Operator Priority Directive 2026-05-08

## Operator verbatim (sacrosanct — never paraphrase, dilute, or summarize)

> "Somehoe you we did't detect there was a compaction... this is a big issue... you were about to start doing trash without context... lets record this as a priority to do something about it.. somehow also the conversation was compacted automatically as soon as we hit 5%.... really weird... we had so much to do and a hand-off document and such... we need to find how out how that can happen and make sure auto-compact is off always. only auto-dream can be enabled. so register. then regather context following the procedure, 30+ operation and then we will address this after you register properly and create thet tasks related to this and then we will continue what we were doing before compact that you probably lost track a lot of..."

## Distinct items registered

1. **Detection failure (agent-side bug)**: agent did not detect the post-compact state and was about to act (pipeline post) without first regathering context. Operator: *"you were about to start doing trash without context"*. The post-compact hook fired (per SessionStart directive in system reminder) but the agent did not OBEY — went straight to executing the pre-compact pending action instead of first running /orient or gateway orient.

2. **Auto-compact triggered prematurely (harness-side bug or config gap)**: *"the conversation was compacted automatically as soon as we hit 5%.... really weird"*. Operator's surprise marker = unexpected behavior. Pre-compact hook should have fired BEFORE compaction destroyed context; instead compaction took the conversation while there was 5% remaining.

3. **Pre-compact handoff doc may not have fired**: *"we had so much to do and a hand-off document and such"*. Implication: operator expected the hand-off document was created, but the agent post-compact does not appear to have read one OR none was authored. Need to verify per pre-compact hook impl.

4. **Operator policy directive (sacrosanct)**: *"make sure auto-compact is off always. only auto-dream can be enabled"*. Auto-compact MUST be permanently off across configs (CLAUDE.md, settings.json, hooks, any system-level harness control). "Auto-dream" is the only auto-* mechanism allowed (term TBD — operator-known concept).

5. **Procedural instruction (this turn)**:
   - "so register" → log verbatim (this file)
   - "then regather context following the procedure, 30+ operation" → run /orient-equivalent + read brain + read recent logs + read recent raws + check pipeline state + check handoff doc + verify Fire 101 state
   - "then we will address this after you register properly and create thet tasks related to this" → after regather, create wiki-backlog tasks for the auto-compact issue
   - "then we will continue what we were doing before compact that you probably lost track a lot of" → resume /loop directive after task-creation

## Implications for this conversation

- The /loop directive ("we continue the workflow...") was active across at least 100+ fires (cron `e19f4787` scheduled at 60s cadence per "exploit before compact" PIVOT before compact event)
- The Fire 101 piece (`wiki/patterns/01_drafts/blocker-and-impediment-registry-pattern-completes-mode-by-nature-governance-trio.md`) was authored just before compaction and pipeline post was NOT yet run on it
- Operator's "you probably lost track a lot of" is the operator-empirical signal that compaction did damage; agent must regather thoroughly, not assume the summary captures everything

## Tasks to create (per operator's "create thet tasks related to this")

After regather context completes:

1. **Investigate auto-compact trigger condition** — why did compaction fire at 5% remaining (rather than respecting the manual operator-control)? Check Claude Code harness settings, config files, env vars.
2. **Disable auto-compact globally** — locate where this is configured (CLAUDE.md hot-path? settings.json? Claude Code harness env var?) and set to never-auto.
3. **Verify pre-compact hook fires reliably** — the hook should write a deterministic handoff doc to wiki/log/ before any compaction event. Check logs for whether one was written for this event.
4. **Add post-compact-detection guardrail** — agent should not act on pre-compact pending tasks without first running /orient or gateway orient to verify state. Possibly a hook injecting a clear "POST-COMPACT — REGATHER FIRST" directive.
5. **Document "auto-dream" as the only allowed auto-* mechanism** — capture operator's allowed-auto policy (only auto-dream; never auto-compact).

## Cross-references

- /loop directive sacrosanct verbatim: established multiple turns prior; appears in summary as "we continue the workflow..."
- 100-piece milestone log: `wiki/log/2026-05-08-100-piece-milestone-closing-arc-summary-pre-compact-preservation.md`
- Fire 99 question-registry pattern: `wiki/patterns/01_drafts/question-registry-discipline-bidirectional-question-answering-with-audience-taxonomy.md`
- Fire 98 mode-by-nature pattern: `wiki/patterns/01_drafts/mode-by-nature-active-governance-pm-architect-dual-expert-generates-blockers-impediments-questions.md`
- Fire 101 blocker-impediment-registry pattern (pipeline post pending): `wiki/patterns/01_drafts/blocker-and-impediment-registry-pattern-completes-mode-by-nature-governance-trio.md`
- /opt PreCompact hook: `.claude/hooks/pre-compact.sh` (verify exists + check it runs per impl-spec #10)
- /opt PostCompact hook: `.claude/hooks/post-compact.sh` (verify exists + check additionalContext directive)

## Tags

[operator-directive, sacrosanct, auto-compact, post-compact-detection-failure, priority, regather-context, register-and-create-tasks]
