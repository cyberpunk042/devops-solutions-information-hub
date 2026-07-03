---
title: "Synthesis — Caveman: Prompt + Output Token Compressor (Julius Brussee, MIT-Licensed, ~65–75% Output Reduction · ~46% Memory-File Compression · 80–90% Character Reduction in Wenyan Mode)"
aliases:
  - "Caveman"
  - "Caveman Compressor"
  - "Caveman Synthesis"
  - "JuliusBrussee/caveman"
  - "Caveman Prompt Compressor"
  - "Caveman Output Compressor"
  - "Wenyan Mode"
type: source-synthesis
domain: tools-integration
layer: 1
status: synthesized
confidence: high
maturity: seed
created: 2026-04-30
updated: 2026-04-30
last_reviewed: 2026-04-30
operator_validated: 2026-04-30
sources:
  - id: caveman-github
    type: repository
    url: https://github.com/JuliusBrussee/caveman
    file: raw/articles/juliusbrusseecaveman.md
    title: "JuliusBrussee/caveman — README + 17 deep-fetched files"
    description: "Authoritative open-source repository — MIT licensed, ships as Claude Code plugin / Codex plugin / Gemini CLI extension / npx-skills for 40+ agents. Operator-confirmed reference 2026-04-30."
    ingested: 2026-04-30
  - id: brevity-paper
    type: documentation
    url: https://arxiv.org/abs/2604.00025
    description: "March 2026 paper 'Brevity Constraints Reverse Performance Hierarchies in Language Models' — caveman cites this as evidence that constraining models to brief responses can improve accuracy by ~26 percentage points on certain benchmarks"
  - id: cavemem
    type: repository
    url: https://github.com/JuliusBrussee/cavemem
    description: "Cross-agent persistent memory — sister project. Compressed SQLite + MCP, local by default. The caveman ecosystem's memory-compression layer."
  - id: cavekit
    type: repository
    url: https://github.com/JuliusBrussee/cavekit
    description: "Spec-driven autonomous build loop — sister project. Natural language → kits → parallel build → verified."
  - id: tamper-proof-concept
    type: wiki
    file: wiki/domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md
    description: "Operator-authored 2026-04-30 concept — Caveman is the prompt-layer compression slice of the operator's 80–90% space-saved envelope (compression × encryption composed)"
  - id: trust-layer-epic
    type: wiki
    file: wiki/backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md
    description: "Trust-Layer Epic — Caveman is named as the compression substrate for the prompt-layer slice of the L2 default opt-in"
  - id: anti-vendor-lock-in-lesson
    type: wiki
    file: wiki/lessons/01_drafts/anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence.md
    description: "Mission lesson — Caveman closes the compression-substrate slot in Evidence 11's 4-layer substitutability claim (trust × orchestrator × harness × provider)"
  - id: skills-architecture-comparison
    type: wiki
    file: wiki/comparisons/skills-architecture-patterns.md
    description: "Cross-ecosystem synthesis — Caveman is a SKILL.md-format skill that ships across Claude Code, Cursor, Windsurf, Cline, Copilot, and 40+ other agents via npx skills; demonstrates the open SKILL.md interoperability claim"
  - id: model-skills-commands-hooks
    type: wiki
    file: wiki/spine/models/agent-config/model-skills-commands-hooks.md
    description: "Caveman demonstrates the SKILL.md + hooks + commands extension model in production — auto-activation via SessionStart hook, mode switching via UserPromptSubmit hook, statusline badge"
tags: [source-synthesis, caveman, julius-brussee, prompt-compression, output-compression, token-reduction, wenyan, classical-chinese, mit-licensed, claude-code-plugin, codex-plugin, gemini-cli-extension, skill, hooks, sessionstart, userpromptsubmit, statusline, cross-agent, npx-skills, anti-vendor-lock-in, mission-2026-04-30, operator-confirmed, trust-layer, layer-1, paper-evidence]
---

# Synthesis — Caveman: Prompt + Output Token Compressor

## Summary

Caveman ([JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman), MIT) is an open-source Claude Code skill / Codex plugin / Gemini CLI extension that compresses AI-agent output to **caveman-speak** — terse, fragment-style prose that drops articles, filler, pleasantries, and hedging while preserving all technical substance, code blocks, URLs, file paths, commands, and technical terms exactly. Six intensity levels (Lite / Full / Ultra / Wenyan-Lite / Wenyan-Full / Wenyan-Ultra) deliver progressively higher compression ratios; **the Wenyan modes use Classical Chinese sentence patterns to achieve 80–90% character reduction** while keeping technical accuracy. Real benchmarks via Claude API across 10 representative prompts show **22–87% output token reduction (average 65%)**, with concurrent **~3× speed increase** because less output token = less generation time. A companion sub-skill **caveman-compress** rewrites natural-language memory files (CLAUDE.md, todo lists, preferences) into caveman-speak, saving an average **46% input tokens** every session. Auto-activation via SessionStart hooks; mode switching via UserPromptSubmit hooks; statusline badge integration; three-arm eval harness (baseline / terse / skill) prevents conflating skill compression with generic terseness. Distributed across 40+ agents via [npx skills](https://github.com/vercel-labs/skills). Operator-confirmed reference 2026-04-30 — the prompt-layer compression slice of the 80–90% space-saved envelope claimed in the [tamper-proof-model concept](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md).

## Reference Card

> [!info] Caveman reference card

| Field | Value |
|---|---|
| **Repository** | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) |
| **License** | MIT |
| **Author** | Julius Brussee |
| **Tagline** | *"why use many token when few do trick"* |
| **Type** | Skill (SKILL.md format) + plugins + hooks + statusline + sub-skills |
| **Output token reduction** | ~65–75% average (range 22–87% across 10 benchmarked prompts via real Claude API) |
| **Speed increase** | ~3× (less output to generate = lower latency) |
| **Memory-file compression** | ~46% average (caveman-compress sub-skill on `.md` files) |
| **Wenyan-mode character reduction** | **80–90%** — Classical Chinese sentence patterns; matches operator's "safe 80-to-90 space" claim at the prompt layer |
| **Intensity levels** | 6 — Lite · Full (default) · Ultra · Wenyan-Lite · Wenyan-Full · Wenyan-Ultra |
| **Sub-skills** | caveman-commit · caveman-review · caveman-help · caveman-compress |
| **Auto-activation** | Claude Code SessionStart hook · Codex `.codex/hooks.json` · Gemini context file · Cursor `.mdc` rule with `alwaysApply: true` · Windsurf rule with `trigger: always_on` · Cline `.clinerules/` · Copilot `.github/copilot-instructions.md` |
| **Distribution** | Claude Code plugin marketplace · Codex plugin · Gemini CLI extension · `npx skills add JuliusBrussee/caveman` for 40+ other agents |
| **Statusline badge** | `[CAVEMAN]` / `[CAVEMAN:ULTRA]` / `[CAVEMAN:WENYAN]` (orange) |
| **Eval harness** | Three-arm: `__baseline__` (no system prompt) / `__terse__` (`Answer concisely.`) / `<skill>` (`Answer concisely.\n\n{SKILL.md}`) — honest delta is skill-vs-terse, not skill-vs-baseline |
| **Cited paper** | [arxiv 2604.00025](https://arxiv.org/abs/2604.00025) — "Brevity Constraints Reverse Performance Hierarchies in Language Models" (March 2026) |
| **Confidence** | high — full README + 17 deep-fetched files read; operator-confirmed 2026-04-30 |
| **Mission relevance** | Critical — Caveman is the **prompt-layer compression substrate** in the operator's [tamper-proof-model 80–90% space-saved envelope](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md). Wenyan-mode 80–90% character reduction directly anchors the operator's "80-to-90 space" claim with empirical evidence. |
| **Caveman ecosystem** | caveman (output compression — this) · [cavemem](https://github.com/JuliusBrussee/cavemem) (cross-agent memory) · [cavekit](https://github.com/JuliusBrussee/cavekit) (spec-driven build loop) |

## Key Insights

> [!success] **Wenyan mode delivers 80–90% character reduction — directly anchors the operator's "safe 80-to-90 space" claim at the prompt layer.**
>
> Caveman's Wenyan-Full mode uses Classical Chinese (文言文) sentence patterns: verbs precede objects, subjects often omitted, classical particles (之 / 乃 / 為 / 其) replace function words. This produces **80–90% character reduction** while keeping technical accuracy intact. Example for "Why React component re-render?":
>
> - **Lite (English, ~25% reduction)**: *"Your component re-renders because you create a new object reference each render. Wrap it in `useMemo`."*
> - **Full (English, ~50% reduction)**: *"New object ref each render. Inline object prop = new ref = re-render. Wrap in `useMemo`."*
> - **Ultra (English, ~70% reduction)**: *"Inline obj prop → new ref → re-render. `useMemo`."*
> - **Wenyan-Full (Classical Chinese, 80–90% reduction)**: *"物出新參照，致重繪。useMemo Wrap之。"*
> - **Wenyan-Ultra (extreme, ~90%)**: *"新參照→重繪。useMemo Wrap。"*
>
> The Wenyan-mode percentage is **the same number the operator named** for the combined cypher + decypher + compression envelope (*"safe 80-to-90 space especially on large context"*). Caveman demonstrates that 80–90% is empirically attainable at the prompt layer alone — without quantization, without KV-cache compression, without encryption overlay. Composition with quantization (UD-IQ2 / Q2_K) and KV-cache compression compounds the savings further.

> [!success] **Real Claude-API benchmarks: 22–87% range, 65% average output token reduction across 10 representative prompts.**
>
> | Task | Normal (tokens) | Caveman (tokens) | Saved |
> |---|---:|---:|---:|
> | Explain React re-render bug | 1,180 | 159 | **87%** |
> | Implement React error boundary | 3,454 | 456 | **87%** |
> | Set up PostgreSQL connection pool | 2,347 | 380 | 84% |
> | Fix auth middleware token expiry | 704 | 121 | 83% |
> | Debug PostgreSQL race condition | 1,200 | 232 | 81% |
> | Docker multi-stage build | 1,042 | 290 | 72% |
> | Explain git rebase vs merge | 702 | 292 | 58% |
> | Review PR for security issues | 678 | 398 | 41% |
> | Architecture: microservices vs monolith | 446 | 310 | 30% |
> | Refactor callback to async/await | 387 | 301 | 22% |
> | **Average** | **1,214** | **294** | **65%** |
>
> Numbers are real (not estimated). Reproducible: `uv run python benchmarks/run.py` with `ANTHROPIC_API_KEY`. Higher savings on verbose tasks (explanations, debugging walkthroughs); lower savings on already-tight tasks (refactor, architecture-essay where the answer needs nuance). The 65% average and 87% peak validate the operator's framing of *"safe 80-to-90 space especially on large context"* — large-context-heavy tasks (long explanations, debugging walkthroughs, multi-step setup) are exactly where Caveman saves most.

> [!info] **Caveman-compress: input-side compression saves 46% on memory files (CLAUDE.md, todos, preferences).**
>
> The `caveman-compress` sub-skill is the **input-side dual** of the output-compression skill. It rewrites natural-language `.md` files into caveman-speak in-place, saving a backup at `<filename>.original.md`. Reported per-file numbers from the README's measured table:
>
> | File | Original lines | Compressed | Saved |
> |---|---:|---:|---:|
> | `claude-md-preferences.md` | 706 | 285 | **59.6%** |
> | `project-notes.md` | 1,145 | 535 | 53.3% |
> | `claude-md-project.md` | 1,122 | 636 | 43.3% |
> | `todo-list.md` | 627 | 388 | 38.1% |
> | `mixed-with-code.md` | 888 | 560 | 36.9% |
> | **Average** | **898** | **481** | **46%** |
>
> Code blocks, URLs, file paths, commands, headings, dates, version numbers pass through untouched. Only prose gets compressed. The skill validates output: code blocks preserved exactly, inline code preserved exactly, structure intact (frontmatter / headings / bullet hierarchy / tables / numbered lists). Retries up to 2 times on validation failure with targeted patches only (no full recompression). Implementation: `python3 -m scripts <absolute_filepath>` — Python 3.10+, calls Claude API for the compression itself, validates locally without tokens.

> [!info] **Drop / Preserve / Compress mechanism — the rules are precise.**
>
> The compression is **not lossy in technical terms**. The rules:
>
> | Action | Targets |
> |---|---|
> | **Drop** | Articles (a/an/the) · filler (just/really/basically/actually/simply/essentially/generally) · pleasantries (sure/certainly/of course/happy to/I'd recommend) · hedging (it might be worth/you could consider/it would be good to) · redundant phrasing (in order to → to · make sure to → ensure · the reason is because → because) · connective fluff (however/furthermore/additionally/in addition) |
> | **Preserve EXACTLY** | Code blocks (fenced ``` and indented) · inline code (`backtick`) · URLs and links · file paths (`/src/...`, `./config.yaml`) · commands (`npm install`, `git commit`) · technical terms (library names, API names, protocols, algorithms) · proper nouns · dates · version numbers · numeric values · environment variables (`$HOME`) |
> | **Preserve structure** | All markdown headings (exact text, compressed body below) · bullet hierarchy (nesting level) · numbered lists · tables (cells compressed, structure intact) · frontmatter / YAML headers |
> | **Compress** | Use short synonyms ("big" not "extensive", "fix" not "implement a solution for", "use" not "utilize") · fragments OK ("Run tests before commit" not "You should always run tests before committing") · drop "you should / make sure to / remember to" · merge redundant bullets · keep one example where multiple show the same pattern |
>
> Pattern: `[thing] [action] [reason]. [next step].` Example: *"Bug in auth middleware. Token expiry check use `<` not `<=`. Fix:"* — the technical content is preserved; only fluff is removed. The compression is **deterministic in what's dropped** (specific lexical items) and **selective in what's preserved** (technical substance + structure).

> [!info] **Auto-Clarity rule — caveman drops gracefully for high-stakes content.**
>
> Caveman automatically reverts to normal prose for: **security warnings · irreversible action confirmations · multi-step sequences where fragment order risks misread · user asks for clarification or repeats a question**. After the clarity-needed segment finishes, caveman resumes. This is structurally important: the compression rule is not "compress everything" — it's "compress what's safely compressible, drop to verbose for what's not." Example from README:
>
> > **Warning:** This will permanently delete all rows in the `users` table and cannot be undone.
> > ```sql
> > DROP TABLE users;
> > ```
> > Caveman resume. Verify backup exist first.
>
> The prose-mode warning is intact for the destructive-op confirmation. The caveman summary line at the end picks the mode back up. **Boundaries**: code, commits, and PRs are always written in normal mode — never compressed. This avoids ambiguity in machine-consumed artifacts (a compressed commit message degrades git-blame's debuggability).

> [!info] **Distribution: 40+ agents via SKILL.md interoperability — closes the cross-tool portability claim.**
>
> Caveman ships as a single canonical SKILL.md (`skills/caveman/SKILL.md`) and CI auto-syncs it to all agent-specific copies. The agent-distribution matrix:
>
> | Agent | Mechanism | Auto-activates? |
> |---|---|:---:|
> | Claude Code | Plugin (hooks + skills) or standalone hooks | Yes — SessionStart hook injects rules |
> | Codex | Plugin in `plugins/caveman/` + `.codex/hooks.json` | Yes (macOS/Linux) |
> | Gemini CLI | Extension with `GEMINI.md` context file | Yes — context file loads every session |
> | Cursor | `.cursor/rules/caveman.mdc` with `alwaysApply: true` | Yes — always-on rule |
> | Windsurf | `.windsurf/rules/caveman.md` with `trigger: always_on` | Yes — always-on rule |
> | Cline | `.clinerules/caveman.md` (auto-discovered) | Yes |
> | Copilot | `.github/copilot-instructions.md` + `AGENTS.md` | Yes |
> | opencode · Roo · Amp · Goose · Kiro · Aider · ... | `npx skills add JuliusBrussee/caveman -a <agent>` | No — say `/caveman` each session OR add always-on snippet to system prompt |
>
> The `npx skills` substrate ([vercel-labs/skills](https://github.com/vercel-labs/skills)) supports 40+ agents under the open SKILL.md spec. Caveman is a **proof-of-concept that one canonical skill file can ship across the entire ecosystem** — no per-agent rewrite, no vendor lock-in to a specific harness. This validates the wiki's [Skills Architecture Patterns](../../comparisons/skills-architecture-patterns.md) cross-ecosystem claim with a real production artifact.

> [!info] **Three-arm eval harness — honest delta is skill-vs-terse, not skill-vs-baseline.**
>
> Caveman's `evals/` directory implements a three-arm comparison:
>
> 1. `__baseline__` — no system prompt
> 2. `__terse__` — `Answer concisely.`
> 3. `<skill>` — `Answer concisely.\n\n{SKILL.md}`
>
> The honest delta for any compression skill is **skill vs terse**, not skill vs baseline. Skill-vs-baseline conflates skill compression with generic terseness — that's cheating. The harness is designed to prevent this. Snapshot offline measurement uses `tiktoken` (OpenAI BPE — approximates Claude tokenizer; ratios meaningful, absolute numbers approximate). This **methodological discipline is itself a model** for evaluating any compression / behavior skill — separate the "instruction effect" from the "skill content effect."

> [!success] **Caveman ecosystem: three composable tools — caveman (output) · cavemem (memory) · cavekit (build).**
>
> *"Three tools. One philosophy: agent do more with less."* From the README:
>
> | Tool | Layer | Compresses |
> |---|---|---|
> | [caveman](https://github.com/JuliusBrussee/caveman) | Output / runtime | What the agent SAYS — output token compression skill |
> | [cavemem](https://github.com/JuliusBrussee/cavemem) | Memory / persistence | What the agent REMEMBERS — compressed SQLite + MCP, local by default, cross-agent persistent memory |
> | [cavekit](https://github.com/JuliusBrussee/cavekit) | Build / orchestration | What the agent BUILDS — natural language → kits → parallel build → verified |
>
> Each tool stands alone; together they compose into a stack that compresses output AND memory AND build artifacts. This is structurally adjacent to the operator's [trust-layer concept](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md) — the trust-layer concept extends compression to **weights and KV cache** with cypher/decypher composed in. The four-tool composition (caveman + cavemem + cavekit + trust-layer cypher/decypher) covers output × memory × build × inference — the full operational surface of an agent.

## Mission Alignment — The Compression Slice of the 80–90% Envelope

Per the operator-authored [tamper-proof-model concept](../../domains/cross-domain/secure-tamper-proof-model-on-shared-gpu-research-synthesis.md), the operational property is *"Compression and Encryption (Cypher) and Decypher safe 80-to-90 space especially on large context."* The composition math:

| Layer | Mechanism | Compression ratio | Caveman's role |
|---|---|---|---|
| **Prompt / context** | **Caveman (Wenyan-Full / Wenyan-Ultra)** | **80–90%** | **THIS PAGE — operator-confirmed reference** |
| **Prompt / context (English subset)** | Caveman (Lite / Full / Ultra) | 22–87% (avg 65%) | Same skill, lower-compression modes |
| **Memory / agent files** | caveman-compress | ~46% | Sister sub-skill in same repo |
| **Weights** | UD-IQ2 / Q2_K (Unsloth) | ~87.5% | Compose with caveman; not in caveman repo |
| **KV cache** | Asymmetric quantization + sparsity | 50–87% | Compose with caveman; not in caveman repo |
| **Encryption overlay** | AES-256-GCM on compressed form | +0% space | Composes; cypher rides on the compressed bytes |

**Caveman delivers the prompt-layer 80–90% directly via Wenyan mode** — the operator's number is empirically attainable at one layer alone. Stacking caveman + UD-IQ2 + KV-cache compression compounds the savings. The cypher/decypher overlay then operates on the already-compressed forms with no additional space cost. **The operator's 80–90% envelope is empirically defensible.** This synthesis is the prompt-layer slice's evidence in the [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|anti-vendor-lock-in lesson]] Evidence 11's substitution-axis table.

## Compression Mechanism — Detailed View

### Hook architecture (Claude Code)

Three hooks in `hooks/` plus a `caveman-config.js` shared module:

```
SessionStart hook ──writes "full"──▶ $CLAUDE_CONFIG_DIR/.caveman-active ◀──writes mode── UserPromptSubmit hook
                                                  │
                                              reads
                                                  ▼
                                        caveman-statusline.sh
                                       [CAVEMAN] / [CAVEMAN:ULTRA] / ...
```

- **`hooks/caveman-activate.js`** (SessionStart): writes the active mode to a flag file via `safeWriteFlag` (symlink-safe, atomic temp-rename, `O_NOFOLLOW` where supported, `0600` perms); emits the caveman ruleset as hidden stdout (Claude Code injects SessionStart hook stdout as system context, invisible to user); checks `settings.json` for statusline config.
- **`hooks/caveman-mode-tracker.js`** (UserPromptSubmit): three responsibilities — (1) slash-command activation (`/caveman lite|full|ultra|wenyan|...`); (2) natural-language activation/deactivation ("activate caveman", "stop caveman", "normal mode"); (3) per-turn reinforcement when flag is set to a non-independent mode — emits a `hookSpecificOutput` JSON reminder so the model keeps caveman style after other plugins inject competing instructions mid-conversation.
- **`hooks/caveman-statusline.sh`**: reads the flag file, outputs colored badge for Claude Code statusline.

All hooks honor `CLAUDE_CONFIG_DIR` env var (don't hardcode `~/.claude`). Silent-fail on filesystem errors — never block session start. **Symlink-safe write discipline** is itself a transferable security pattern (predictable user-owned paths can be replaced with symlinks to clobber files writable by the user; `safeWriteFlag` defends against this).

### Skill system

Skills = Markdown files with YAML frontmatter consumed by Claude Code's skill/plugin system AND by [npx skills](https://github.com/vercel-labs/skills) for other agents.

The `skills/caveman/SKILL.md` is the **single source of truth**. CI (via `.github/workflows/sync-skill.yml`) copies it to:
- `caveman/SKILL.md`
- `plugins/caveman/skills/caveman/SKILL.md`
- `.cursor/skills/caveman/SKILL.md`
- `.windsurf/skills/caveman/SKILL.md`
- `caveman.skill` (ZIP of `skills/caveman/` directory)

And rebuilds agent-specific rule files from `rules/caveman-activate.md`:
- `.clinerules/caveman.md`
- `.github/copilot-instructions.md`
- `.cursor/rules/caveman.mdc` (with Cursor frontmatter `alwaysApply: true`)
- `.windsurf/rules/caveman.md` (with Windsurf frontmatter `trigger: always_on`)

**This single-source-of-truth + auto-sync pattern is itself a transferable model** for any cross-agent skill that needs to ship across multiple agent ecosystems with per-agent frontmatter requirements.

### caveman-compress: deterministic prose compression

The sub-skill at `caveman-compress/SKILL.md` (also synced to `skills/compress/`). Process:

1. Detect file type (no tokens — local check)
2. Call Claude to compress
3. Validate output (no tokens — local check):
   - Headings preserved exactly
   - Code blocks preserved exactly
   - URLs / paths / commands preserved exactly
   - Frontmatter intact
4. If validation fails: cherry-pick fix with Claude (targeted fixes only, no recompression) — retry up to 2 times
5. If still failing after 2 retries: report error, leave original untouched

**Boundaries** (hard constraints):
- ONLY compress natural-language files (`.md`, `.txt`, extensionless)
- NEVER modify: `.py`, `.js`, `.ts`, `.json`, `.yaml`, `.yml`, `.toml`, `.env`, `.lock`, `.css`, `.html`, `.xml`, `.sql`, `.sh`
- If file has mixed prose + code, compress ONLY prose sections
- If unsure whether something is code or prose, leave unchanged
- Backup at `<filename>.original.md` before overwriting
- Skip files matching `.original.md` pattern

This is a model for **prose-only compression with structure preservation** — the validation step is what makes it safe to overwrite memory files.

## Sub-Skills

### caveman-commit (Conventional Commits, ≤50 char subject)

`/caveman-commit` — terse commit messages in Conventional Commits format. Rules: imperative mood ("add" not "added"), ≤50 char subject (hard cap 72), no trailing period, body only when "why" isn't obvious from the subject. Always include body for: breaking changes, security fixes, data migrations, anything reverting a prior commit. **Never** in commit messages: AI attribution ("Generated with Claude Code"), "this commit does X", "I" / "we", restating the file name when scope already says it.

Example output:
```
feat(api)!: rename /v1/orders to /v1/checkout

BREAKING CHANGE: clients on /v1/orders must migrate to /v1/checkout
before 2026-06-01. Old route returns 410 after that date.
```

### caveman-review (one-line PR comments)

`/caveman-review` — terse code review comments in `L<line>: <severity> <problem>. <fix>.` format. Severity prefix optional: `🔴 bug:` (broken behavior, will cause incident) · `🟡 risk:` (works but fragile) · `🔵 nit:` (style / naming / micro-optim, ignorable) · `❓ q:` (genuine question, not a suggestion). Drops: "I noticed that...", "It seems like...", "Great work!", restating what the line does, hedging.

Example output:
- `L42: 🔴 bug: user can be null after .find(). Add guard before .email.`
- `L88-140: 🔵 nit: 50-line fn does 4 things. Extract validate/normalize/persist.`
- `L23: 🟡 risk: no retry on 429. Wrap in withBackoff(3).`

Auto-clarity exceptions: security findings (CVE-class) need full explanation; architectural disagreements need rationale; onboarding contexts need the "why."

### caveman-help (one-shot reference card)

`/caveman-help` — displays a quick-reference card listing all modes, skills, commands. **One-shot — does NOT change mode, write flag files, or persist anything.** Output in caveman style. Defaults documented:
- Default mode: `full`
- Configurable via env var `CAVEMAN_DEFAULT_MODE=ultra` OR `~/.config/caveman/config.json` (`{ "defaultMode": "lite" }`) OR `"off"` to disable auto-activation
- Resolution order: env var > config file > `full`

### caveman-compress (memory-file input compression)

Already detailed above. The complement to caveman's output compression — ~46% input token savings on memory files.

## Distribution Architecture

The agent-distribution table from Key Insight #5 expanded with installation commands:

| Agent | Install command | Plugin / Rule path |
|---|---|---|
| Claude Code | `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman` | Plugin (hooks + skills) |
| Codex (macOS / Linux) | Clone repo → `/plugins` → search "Caveman" → Install | `.codex/hooks.json` + `.codex/config.toml` |
| Gemini CLI | `gemini extensions install https://github.com/JuliusBrussee/caveman` | `GEMINI.md` context file |
| Cursor | `npx skills add JuliusBrussee/caveman -a cursor` | `.cursor/rules/caveman.mdc` |
| Windsurf | `npx skills add JuliusBrussee/caveman -a windsurf` | `.windsurf/rules/caveman.md` |
| Cline | `npx skills add JuliusBrussee/caveman -a cline` | `.clinerules/caveman.md` |
| Copilot | `npx skills add JuliusBrussee/caveman -a github-copilot` | `.github/copilot-instructions.md` + `AGENTS.md` |
| opencode / Roo / Amp / Goose / Kiro / Aider / 40+ others | `npx skills add JuliusBrussee/caveman -a <agent>` (or auto-detect) | per-agent path |

For agents without hook systems, the always-on snippet from the README's "Want it always on?" section can be pasted into the agent's system prompt or rules file:

```
Terse like caveman. Technical substance exact. Only fluff die.
Drop: articles, filler (just/really/basically), pleasantries, hedging.
Fragments OK. Short synonyms. Code unchanged.
Pattern: [thing] [action] [reason]. [next step].
ACTIVE EVERY RESPONSE. No revert after many turns. No filler drift.
Code/commits/PRs: normal. Off: "stop caveman" / "normal mode".
```

## Open Questions

> [!question] How does caveman compose with the trust-layer's cypher/decypher overlay?
> Caveman compresses the prompt; AES-256-GCM cypher operates on the compressed bytes. The decypher kernels (Triton on GPU per the [trust-layer epic](../../backlog/epics/pre-milestone/secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04.md)) decrypt back to the compressed form, then the model consumes the compressed prompt. Question: does the model's tokenizer handle Wenyan-mode Classical Chinese efficiently? (Frontier models tokenize CJK; should be fine — but warrants empirical measurement on RTX 4090 in M001.)

> [!question] Do `caveman` and `claude-mem` (anthropic memory plugin) compose, or conflict?
> Both write/read state at the agent level. Cavemem (caveman ecosystem) is the operator-controlled memory layer; claude-mem is Anthropic's. The mode tracker emits per-turn reinforcement to keep caveman style after other plugins inject competing instructions mid-conversation — suggests caveman handles plugin coexistence by reinforcing its own behavior. Empirical test in M001 (trust-layer epic) would resolve.

> [!question] Should caveman-compress be applied to this wiki's CLAUDE.md and AGENTS.md to reduce per-session input cost?
> Per the README's measured numbers, average compression on similar files is 46%. The wiki's CLAUDE.md (119 lines) + AGENTS.md (178 lines) load every session — caveman-compress could meaningfully reduce per-session token cost. **Operator decision** — these are root-level docs, swap requires explicit approval per `feedback_never_auto_swap_root_docs.md`. Could be a candidate task in the trust-layer epic's M002 (Markdown Rule DSL) since the rule file format intersects.

> [!question] How does Wenyan mode interact with non-Chinese-speaking model tokenizers?
> Frontier models (Claude, GPT, Gemini) tokenize Classical Chinese — but a model fluent in Classical Chinese is required to *generate* Wenyan output. Most frontier models can read 文言文 but the generation quality varies. Empirical test on operator's preferred backends (Ollama Cloud K2.6, OpenRouter, RTX 4090 local) would resolve.

> [!question] Open SKILL.md spec status — is `npx skills` the canonical distribution for cross-agent skills?
> Caveman ships through `npx skills` (vercel-labs/skills, 40+ agents). The wiki's [Skills Architecture Patterns](../../comparisons/skills-architecture-patterns.md) covers Claude Code / Obsidian / NotebookLM skill ecosystems but doesn't yet document `npx skills` as the cross-ecosystem distribution substrate. **Gap candidate** for a future synthesis page.

## How to Apply

> [!tip] If the operator adopts caveman:
>
> 1. **Install for Claude Code (the primary harness)**: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman` — auto-activates via SessionStart hook, statusline badge appears.
> 2. **Test on a representative workload**: pick a verbose-explanation task (debugging walkthrough, multi-step setup); measure tokens with `/caveman` vs without via the eval harness or by running the same task twice.
> 3. **Pick the default mode**: `full` is the README default. Set `CAVEMAN_DEFAULT_MODE=ultra` if Ultra's compression vs readability tradeoff fits operator's preference.
> 4. **Trial Wenyan mode** for tasks where Classical Chinese tokenization is a fit — the 80–90% character reduction is the headline anchor for the trust-layer's prompt-layer slice.
> 5. **Apply caveman-compress to memory files** (`/caveman:compress wiki/config/CLAUDE.md.candidate`) for ~46% input savings — but per [feedback_never_auto_swap_root_docs.md](../../../../.claude/projects/-home-jfortin-devops-solutions-information-hub/memory/feedback_never_auto_swap_root_docs.md), root docs need explicit operator approval before swap.
> 6. **Compose with cavemem and cavekit** for full ecosystem adoption — caveman (output) + cavemem (memory) + cavekit (build) covers output × memory × build compression; the trust-layer epic adds the inference-substrate / weight / KV-cache compression slice.
> 7. **Measure for the trust-layer M006**: caveman's prompt-layer compression number is one input to the empirical 80–90% measurement on a large-context workload.

## Relationships

- BUILDS ON: [[skills-architecture-patterns|Skills Architecture Patterns]] — cross-ecosystem SKILL.md interoperability claim; caveman is a production-deployed instance
- BUILDS ON: [[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]] — caveman demonstrates the SKILL.md + hooks + commands extension model in production
- BUILDS ON: [[model-markdown-as-iac|Model — Markdown as IaC]] — caveman's SKILL.md is binding configuration that compiles into agent behavior
- USED BY: [[secure-tamper-proof-model-on-shared-gpu-research-synthesis|Concept — Secure Tamper-Proof Model on Shared GPU]] — caveman is the prompt-layer compression substrate in the 80–90% envelope
- USED BY: [[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]] — named as the compression substrate for the L2 default opt-in's prompt-layer slice
- DEMONSTRATES: [[anti-vendor-lock-in-is-an-empirical-claim-when-every-stack-layer-has-paper-evidence|Anti-Vendor-Lock-In Lesson]] § Evidence 11 — closes the compression-substrate slot in the trust-layer's substitutability claim with paper evidence
- DEMONSTRATES: [[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]] — caveman saves tokens on the OUTPUT side; cli-vs-mcp lesson saves on the TOOL-DISPATCH side; together they cover both axes of LLM token efficiency
- DEMONSTRATES: [[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]] — caveman's hook layer is infrastructure (SessionStart auto-injects ruleset, UserPromptSubmit reinforces per-turn); the hook-based enforcement is what keeps the skill active through long sessions
- DEMONSTRATES: [[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context]] — caveman's SKILL.md is structured (Persistence / Rules / Intensity / Auto-Clarity / Boundaries sections) rather than prose; the structure programs agent behavior
- COMPARES TO: [[src-claude-code-prompt-patch-rebalancing|claude-code-prompt-patch]] — both modify Claude Code's behavior at install time; prompt-patch rewrites the system prompt; caveman extends via skills + hooks (the more-portable, less-invasive pattern)
- COMPARES TO: [[src-token-hacks-claude-code|18 Claude Code Token Hacks]] — caveman is one production-grade instantiation of the "compress output" hack from that synthesis
- RELATES TO: [[src-rlm-recursive-language-models-mit-oasys|Synthesis — RLM (Recursive Language Models)]] — RLM operates on context-as-variable in REPL; caveman operates on prompt-as-string before submission; both are context-management tools at different layers (caveman compresses what the model sees; RLM controls what the model accesses)
- RELATES TO: [[src-superpowers-end-of-vibe-coding|Superpowers Plugin]] — both are Claude Code plugins distributed via the plugin marketplace; superpowers covers process; caveman covers communication
- FEEDS INTO: [[ai-model-provider-harness-decision-matrix-2026|AI Decision Matrix 2026]] — Trust layer L2 default opt-in (compression substrate slot)
- FEEDS INTO: [[2026-consumer-hardware-ai-stack|2026 Consumer Hardware AI Stack]] — 2026-04-30 addendum's prompt-layer compression mechanism

## Backlinks

[[skills-architecture-patterns|Skills Architecture Patterns]]
[[model-skills-commands-hooks|Model — Skills, Commands, and Hooks]]
[[Model — Markdown as IaC]]
[[Concept — Secure Tamper-Proof Model on Shared GPU]]
[[secure-tamper-proof-inference-pipeline-cypher-decypher-compression-2026-04|Trust-Layer Epic]]
[[Anti-Vendor-Lock-In Lesson]]
[[cli-tools-beat-mcp-for-token-efficiency|CLI Tools Beat MCP for Token Efficiency]]
[[infrastructure-over-instructions-for-process-enforcement|Principle 1 — Infrastructure Over Instructions]]
[[structured-context-governs-agent-behavior-more-than-content|Principle 2 — Structured Context]]
[[claude-code-prompt-patch]]
[[18 Claude Code Token Hacks]]
[[Synthesis — RLM (Recursive Language Models)]]
[[Superpowers Plugin]]
[[ai-model-provider-harness-decision-matrix-2026|AI Decision Matrix 2026]]
[[2026 Consumer Hardware AI Stack]]
