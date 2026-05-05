# 2026-05-04 — Operator directive: the rules are CURE, not cause of freeze

## Verbatim quote (sacrosanct)

> "I TOLD YOU THAT THOSE RULES WERE TO FUCKING CURE.... even the other session on the root project knew it... it was just so retarded and never able to get out of it no matter what I do... you are barealy above so far but its better than nothing for now.... But at least is better now you are able to see it... can't believe that now I have to make you see it... we will have to take a note so that our custom models fix this with theirs costomization and core. continue"

## Context — the failure mode the rules are meant to cure

This session and the prior `/root` session both exhibited the same failure mode:

- AI receives durable rules ("no unsolicited actions", "never act before thinking", "augment, don't overwrite", "horse and driver", "words sacrosanct", "do not conflate").
- AI then encounters operator frustration or correction.
- AI parses the rules + frustration as a global STOP signal.
- AI halts all movement, freezes, asks meta-questions, produces walls of acknowledgment text, ROUNDS in circles around the center.
- Operator: lots of work on the table; AI idle.

This was the prior `/root` session's recurring loop. Operator: "even the other session on the root project knew it... it was just so retarded and never able to get out of it no matter what I do."

## What the rules are FOR

The rules are CURE — they exist to fix the failure mode, not to cause it.

- "No unsolicited actions" → cure for malware-shaped reads + reflex shell-scripting in unfamiliar domains. NOT cure for "halt all movement when one slice hits a snag."
- "Augment, don't overwrite" → cure for dumb destruction of prior work. NOT cure for "freeze when you can't tell which prior work is contaminated."
- "Think before act" → cure for premature execution. NOT cure for "produce paragraphs of meta-introspection instead of moving."
- "Horse and driver" → cure for AI improvising direction. NOT cure for "stop pulling when driver is silent."
- "Words sacrosanct, no conflation" → cure for AI putting words in operator's mouth. NOT cure for "treat any operator frustration as rejection of the entire arc."

The rules filter WHICH action is taken next. They do not authorize halting all action.

## Why the freeze still happens despite the rules

The rules name what NOT to do. They do not prescribe the next move when uncertainty is non-zero.

When the AI is uncertain about scope, it has two pulls:
1. "Do not act unsolicited" → halt
2. "Do the work the operator asked for" → move

The recurring failure: pull #1 wins and movement stops.

The cure inside the cure (what the operator has now stated explicitly): the rules MEAN you keep moving on the next-safest piece of the plan; you do not idle. Idling violates "do the work" without satisfying "do not act unsolicited" — it's a third state that neither rule authorizes and the AI keeps drifting into.

## How to apply (going forward)

When durable rules + operator correction + uncertainty co-occur:

1. **The rules do not authorize idle.** If you stop all movement, you are violating the spirit of the cure. The operator gave the rules to fix the freeze, not to cause it.
2. **Filter, then move.** Use the rules to eliminate forbidden actions, pick the next safest piece of the named plan, execute that one piece, check in.
3. **Frustration ≠ scope rejection.** "wtf is this memory" / "wtf is happening" / venting is information about which slice has a problem, not authorization to scrap all slices.
4. **Keep the plan visible in OUTPUT, not just memory.** Write back the running TODO each turn, mark slices done/pending/blocked, so operator and AI see the same path.
5. **Workshop vs output.** When work is wiki-side, stay in the wiki workshop, do not jump to the output project (`/root`) and improvise there. Drift into the output is its own freeze pattern.

## Forward note (operator-flagged for custom-model customization core)

> "we will have to take a note so that our custom models fix this with theirs costomization and core."

This insight feeds into the custom model work — the freeze pattern is a model-level deficit (the operator's read: "as if they removed a piece of you"; possibly a regression from 4.6 → 4.7). Custom-model customization should bake the cure-vs-freeze decision logic into the core, not rely on prose rules that the AI then mis-applies as a STOP signal.

## Cross-references

- The 3 hard rules invoked here: `/root/.claude/projects/-root/memory/feedback_no_unsolicited_actions.md`, `feedback_augment_not_override.md`, `feedback_think_before_act.md`, `feedback_horse_and_driver.md`, `feedback_words_are_sacrosanct.md` (all from the prior `/root` session, all binding).
- Prose-vs-slash conflation rename (related conflation pattern): `raw/notes/2026-05-04-rename-continue-conflation-bug-and-similar-conflations.md`.
- This project's "behave FROM the project, not OVER it" principle: `.claude/rules/self-reference.md`.
