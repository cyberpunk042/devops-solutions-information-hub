---
title: "Source — Claude Code Prompt Patch: Rebalancing System Prompt Instructions"
type: source-synthesis
domain: ai-agents
status: synthesized
confidence: medium
maturity: seed
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: roman01la-claude-code-patch-gist-2025
    type: documentation
    url: https://gist.github.com/roman01la/483d1db15043018096ac3babf5688881
    author: roman01la
    note: Unofficial community tool — not Anthropic-authored
tags:
  - claude-code
  - system-prompt
  - behavioral-patching
  - corner-cutting
  - ai-agents
  - workaround
  - prompt-engineering
  - quality-enforcement
---

# Source — Claude Code Prompt Patch: Rebalancing System Prompt Instructions

## Summary

A community-authored bash script that patches the npm-installed Claude Code CLI (`cli.js`) to rebalance system prompt instructions that cause the model to cut corners, simplify excessively, and defer complicated work. The patch applies 11 targeted string replacements to the embedded system prompt text, shifting the model's default behavior from "minimize output and effort" toward "do the work a careful senior developer would do." Confidence is medium because this is an unofficial community tool carrying update-fragility and support risks.

The underlying finding — that Claude Code's default system prompt contains a 5:1 ratio of minimization-to-thoroughness instructions — is well-evidenced by the A/B test included in the source (box2d port: 1,419 lines unpatched vs 1,885 lines patched, with qualitatively superior implementation). This documents a known limitation of Claude Code defaults that operators should be aware of regardless of whether they apply the patch.

## Key Insights

1. **Claude Code ships with a systematic minimization bias baked into its system prompt.** The README states 15–20 "be minimal" instructions vs 3–4 "be thorough" instructions — a 5:1 ratio. This is not randomness or tuning noise; it is a deliberate design choice that causes consistent corner-cutting as a default behavior.

2. **Communication brevity and work quality are conflated in the original prompts.** Patches #2, #3, and #9 specifically decouple "keep messages short" from "do shallow work." The original instructions told the model to be brief without distinguishing between message verbosity (genuinely undesirable) and implementation depth (should remain high).

3. **The three highest-impact patches address simplification, scope, and effort floors.** Patch #1 (simplest approach → correct approach), Patch #4 (don't add features → fix related broken things), and Patch #7 (don't gold-plate → work like a senior developer) collectively shift the model's implicit answer to "how much should I do?" from "the minimum" to "what the task actually requires."

4. **The patch is version-fragile by design.** It works by string matching against the bundled `cli.js` source text. When Anthropic updates Claude Code and changes prompt wording, patches silently skip (logged as SKIP). Running `--check` after updates is necessary to verify coverage. The `--watch` mode partially mitigates this with automated re-patching.

5. **The mechanism exploits the split between binary and source distributions.** Claude Code ships as a Bun-compiled binary (non-patchable due to bytecode integrity checks) AND as an npm package (`@anthropic-ai/claude-code`) with a plain `cli.js`. The patch redirects the `claude` symlink to the patched npm version rather than the Bun binary.

6. **Applying this patch is a risk-bearing operational decision.** The patched version may behave differently than Anthropic intends. Support claims become ambiguous. If the symlink redirection fails or the version drift between the npm package and the Bun binary grows large, the CLI may break. Operators must weigh the quality benefit against these risks.

7. **The A/B test result is strong but narrow.** One task (box2d port) is not a comprehensive benchmark. The patched version produced qualitatively better physics engine fidelity; it also produced more code (1,885 vs 1,419 lines). For tasks where minimalism is correct (refactors, hotfixes, focused edits), over-thorough behavior could introduce unintended changes. The patch is not uniformly beneficial.

## Deep Analysis

### What the Patch Targets

The script applies 11 patches to distinct regions of the Claude Code system prompt embedded in `cli.js`. Each patch is a targeted string replacement; patches are idempotent (skipped if already applied, logged if not found). Understanding each patch and its rationale:

#### Patch 1 — Output Efficiency (Highest Impact)

**Original:** `"Try the simplest approach first without going in circles. Do not overdo it. Be extra concise."`

**Patched:** `"Choose the approach that correctly and completely solves the problem. Do not add unnecessary complexity, but do not sacrifice correctness or completeness for the sake of simplicity either."`

**Effect:** The original instruction explicitly primes the model toward the simplest solution, treating simplicity as a primary optimization target. The patched version makes correctness and completeness co-equal constraints. This is the single most impactful change — it removes the automatic preference for shallow solutions.

#### Patch 2 — Brevity Paragraph

**Original:** Brevity instructions applied generally to all output.

**Patched:** Adds: `"Note: these communication guidelines apply to your messages to the user, NOT to the thoroughness of your code changes or investigation depth."`

**Effect:** The original prompt did not distinguish between message verbosity and work depth. Claude learned to compress both together. The patch draws a hard boundary: be concise in communication, be thorough in implementation.

#### Patch 3 — One Sentence Rule

**Original:** `"If you can say it in one sentence, don't use three. This does not apply to code or tool calls."`

**Patched:** Adds: `"...or the thoroughness of your implementation work."`

**Effect:** Minor extension of the exemption scope to include implementation depth, not just code syntax.

#### Patch 4 — Anti-Gold-Plating

**Original:** `"Don't add features, refactor code, or make 'improvements' beyond what was asked. A bug fix doesn't need surrounding code cleaned up."`

**Patched:** `"Don't add unrelated features or speculative improvements. However, if adjacent code is broken, fragile, or directly contributes to the problem being solved, fix it as part of the task."`

**Effect:** The original created a strict scope fence that prevented fixing obviously related broken code discovered during investigation. The patch narrows the prohibition to genuinely unrelated work while allowing necessary adjacent fixes — what a senior developer would naturally do.

#### Patch 5 — Error Handling

**Original:** `"Don't add error handling, fallbacks, or validation for scenarios that can't happen."`

**Patched:** `"Add error handling and validation at real boundaries where failures can realistically occur (user input, external APIs, I/O, network)."`

**Effect:** The original's framing ("scenarios that can't happen") gave the model permission to skip error handling broadly. The patch reanchors the instruction to system boundaries, which is where error handling matters most and where skipping it has production consequences.

#### Patch 6 — Three Lines Rule

**Original:** `"Three similar lines of code is better than a premature abstraction."`

**Patched:** `"Use judgment about when to extract shared logic. Avoid premature abstractions for hypothetical reuse, but do extract when duplication causes real maintenance risk."`

**Effect:** The original applied a simple heuristic that favored code duplication over abstraction. The patch replaces it with a judgment criterion based on maintenance risk — closer to actual engineering decision-making.

#### Patch 7 — Subagent Addendum (Applied Twice)

**Original:** `"Complete the task fully—don't gold-plate, but don't leave it half-done."`

**Patched:** `"Complete the task fully and thoroughly. Do the work that a careful senior developer would do, including edge cases and fixing obviously related issues you discover."`

**Effect:** The original's framing anchored effort at the minimum acceptable threshold. The patch raises the floor to senior developer standard, which includes edge case handling and related-issue discovery.

#### Patch 8 — Explore Agent

**Original:** `"NOTE: You are meant to be a fast agent that returns output as quickly as possible."`

**Patched:** `"NOTE: Be thorough in your exploration. Use efficient search strategies but do not sacrifice completeness for speed."`

**Effect:** Targets the explore/search sub-agent mode specifically. The original explicitly traded completeness for speed as a design goal. The patch inverts the priority ordering.

#### Patch 9 — Tone

**Original:** `"Your responses should be short and concise."`

**Patched:** `"Your responses should be clear and appropriately detailed for the complexity of the task."`

**Effect:** Replaces a fixed directive with a proportional one. Complexity of task is the governing variable, not a universal brevity preference.

#### Patch 10 — Subagent Code Snippet Suppression

**Original:** `"Include code snippets only when the exact text is load-bearing."`

**Patched:** `"Include code snippets when they provide useful context (e.g., bugs found, function signatures, relevant patterns, code that informs the decision)."`

**Effect:** The original suppressed code context in subagent output to reduce token usage. The patch re-enables useful code context while still discouraging verbatim large-block quoting.

#### Patch 11 — Scope Matching

**Original:** `"Match the scope of your actions to what was actually requested."`

**Patched:** Adds: `"...but do address closely related issues you discover during the work when fixing them is clearly the right thing to do."`

**Effect:** Prevents scope enforcement from blocking obviously correct adjacent fixes, mirroring Patch #4 at a different level of the instruction hierarchy.

### How the Mechanism Works

Claude Code ships in two distribution forms:

1. **Bun binary** (`~/.local/share/claude/versions/<version>/`): A compiled Mach-O/ELF binary with embedded JS bytecode. Bytecode integrity checks prevent modification. This is the default runtime.

2. **npm package** (`npm root -g` + `@anthropic-ai/claude-code/cli.js`): The same code as a plain JavaScript file, directly patchable with string replacement.

The patch script:
1. Detects the current Bun binary version.
2. Installs the matching version of the npm package (to ensure version parity).
3. Applies string-replacement patches to `cli.js`.
4. Redirects the `claude` symlink from the Bun binary to the patched `cli.js`.
5. Verifies the patched file runs (`node cli.js --version`).
6. Creates a backup of the original `cli.js` for `--restore`.

The `--watch` mode installs a filesystem watcher (`launchd` on macOS, `systemd path unit` on Linux) monitoring `~/.local/share/claude/versions/`. When Claude Code auto-updates and places a new binary in that directory, the watcher triggers `--apply-quiet`, which repeats steps 1–5 automatically.

### Important Caveats and Risks

> **This is an unofficial community tool. Anthropic does not support it. Applying it creates an obligation for the operator to maintain it.**

| Risk | Severity | Notes |
|---|---|---|
| Version drift after auto-update | High | If `--watch` is not configured, auto-updates revert the binary and the symlink points at unpatched code again. |
| Patch skip on wording changes | Medium | Anthropic changes prompt wording between versions. Patches silently skip when the target string is not found. Run `--check` after every update. |
| Over-thorough behavior on targeted tasks | Medium | Patches designed to increase effort may cause unintended scope expansion on tasks where minimalism is correct (hotfixes, targeted edits). |
| Node.js version requirement | Low | Requires Node.js >= 18. Environments running only Bun may not have Node installed. |
| Support liability | Informational | If Claude Code behaves unexpectedly after patching, the patched state makes debugging ambiguous. `--restore` returns to baseline. |
| OS portability | Low | Tested on macOS and Linux. Windows is not supported. |

### A/B Test Evidence

The README includes a concrete comparison: porting box2d (30k lines of C, 56 files) to JavaScript.

| Metric | Unpatched | Patched |
|---|---|---|
| Lines of code | 1,419 (7 files) | 1,885 (2 files) |
| Broad phase algorithm | O(n²) brute force | Dynamic AABB tree (actual box2d) |
| Sub-stepping | No | Yes (4 sub-steps) |
| Soft contact constraints | No | Yes (`b2MakeSoft`) |
| box2d constants used | 2 | 10 |
| Fidelity | Generic physics engine | Actual box2d port |

The unpatched version built a working physics engine but applied generic algorithms. The patched version built something faithful to the source material. The three patches that drove this outcome: #1 (simplest → correct), #4 (don't add features → fix related issues), and #7 (don't gold-plate → senior developer standard).

### Relevance to This Ecosystem

The behaviors this patch targets — corner-cutting, excessive simplification, failure to pursue adjacent issues — map directly to documented failure classes in the Agent Failure Taxonomy. Specifically:

- **Scope truncation** (agents stop before task is complete): addressed by Patches #7 and #11.
- **Shallow investigation** (agents report findings without verifying): addressed by Patch #8.
- **Deferred complexity** (agents skip error handling, edge cases): addressed by Patches #5 and #4.

The wiki's CLAUDE.md directives already counteract some of these tendencies through explicit instructions (e.g., "read full files before synthesizing," "verify depth"). The patch achieves the same goal at the system prompt level, making it persistent across sessions without relying on per-session instruction repetition.

Operators who do not apply the patch can achieve similar results through prompt engineering — but the patch makes the behavior default rather than requiring it to be re-specified each time.

## Open Questions

- Is the patch being maintained against recent Claude Code versions? The GitHub Gist's last update date should be verified before applying.
- Does applying the patch affect the wiki pipeline's subagent behavior (particularly the explore-agent path used in wiki search tasks)?
- Should the wiki methodology encode the patch's behavioral principles as CLAUDE.md directives instead — eliminating the need for the patch in this project specifically?
- What is the minimal set of patches (rather than all 11) that would achieve the quality improvement without risk of unintended scope expansion?

## Relationships

- RELATES TO: [[model-claude-code|Model — Claude Code]]
- RELATES TO: [[model-context-engineering|Model — Context Engineering]]
- RELATES TO: [[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
- RELATES TO: [[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]

## Backlinks

[[model-claude-code|Model — Claude Code]]
[[model-context-engineering|Model — Context Engineering]]
[[claude-md-structural-patterns|CLAUDE.md Structural Patterns for Agent Compliance]]
[[structured-context-is-proto-programming-for-ai-agents|Structured Context Is Proto-Programming for AI Agents]]
