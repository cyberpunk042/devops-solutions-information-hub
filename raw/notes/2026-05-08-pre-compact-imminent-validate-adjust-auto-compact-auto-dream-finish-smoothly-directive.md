---
title: "Pre-Compact Imminent — Operator Validate-Adjust Auto-Compact / Auto-Dream / Finish-Smoothly Directive"
type: note
note_type: directive
domain: raw
status: raw
confidence: high
created: 2026-05-08
updated: 2026-05-08
sources:
  - id: operator-prompt-2026-05-08-pre-compact-imminent
    type: conversation
    description: "Operator's verbatim directive at ~5% remaining; asking to validate auto-compact disable + auto-dream enable + propose custom /finish-smoothly variant for post-compact recovery"
tags: [operator-directive, sacrosanct, pre-compact-imminent, auto-compact-validate, auto-dream-validate, finish-smoothly-custom, regather-process, day-arc-2026-05-08]
---

# Pre-Compact Imminent — Operator Validate-Adjust Auto-Compact / Auto-Dream / Finish-Smoothly Directive

## Operator verbatim (sacrosanct — never paraphrase)

> "also was the auto-compact properly disabled and the auto-dream enabled ? we could add our force /finish-smoothly or a custom one adapted to the situation even better.  when we are at < 10k token left of window. then it can keep continuing till it compact and when it do the post-compact it should do the process and also read the handoff and do the group of operations needed to regather the context properly, not only the task at end but the general needed knowledge per-project before starting working or doing anything. righ now would be a good time to valide / adjust all this we are readhing the 5%"

## Distinct items

1. **Q: Was auto-compact disabled?** — NO (Fire 107 spec authored; Tasks #25-#26 pending implementation; harness-default still operative)

2. **Q: Was auto-dream enabled?** — NO (Q1 auto-dream definition still BLOCKER; Task #29 pending; nothing actually enabled)

3. **Proposal: Custom /finish-smoothly variant adapted to situation**
   - Trigger: < 10k tokens left of window
   - Behavior: keep continuing till compact happens
   - Post-compact: read handoff doc + do regather process
   - "general needed knowledge per-project before starting working or doing anything" (NOT just task-at-end)

4. **Validate/adjust NOW** — operator explicit at 5%

5. **Pre-compact recovery procedure (per directive 5)**: post-compact agent should:
   - Read handoff doc
   - Do general project-knowledge regather (not just last task)
   - Per-project regather before starting any work

## Implications for THIS conversation (5% remaining)

- Compaction imminent; no PreCompact hook wired at /opt → handoff must be authored MANUALLY now
- Per Fire 105 + Fire 157 spec: 11-section handoff doc designed
- Author handoff doc + drop sentinel manually as Fire 157 spec describes

## Action required

1. Author manual handoff doc at wiki/log/<ts>-pre-compact-handoff-manual.md
2. Answer operator's validate questions (auto-compact + auto-dream both NOT implemented yet)
3. Surface custom /finish-smoothly variant proposal as new spec
4. Survive compaction; post-compact agent reads handoff per /opt post-compact.sh + post-orient.sh hooks (those ARE wired) + this raw note

## Tags

[operator-directive, sacrosanct, pre-compact-imminent, auto-compact-validate, auto-dream-validate, finish-smoothly-custom, regather-process, day-arc-2026-05-08]
