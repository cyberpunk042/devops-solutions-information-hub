# Fission-AI/OpenSpec

Source: https://github.com/Fission-AI/OpenSpec
Ingested: 2026-04-14
Type: documentation

---

# README

<p align="center">
  <a href="https://github.com/Fission-AI/OpenSpec">
    <picture>
      <source srcset="assets/openspec_bg.png">
      <img src="assets/openspec_bg.png" alt="OpenSpec logo">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://github.com/Fission-AI/OpenSpec/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/Fission-AI/OpenSpec/actions/workflows/ci.yml/badge.svg" /></a>
  <a href="https://www.npmjs.com/package/@fission-ai/openspec"><img alt="npm version" src="https://img.shields.io/npm/v/@fission-ai/openspec?style=flat-square" /></a>
  <a href="./LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" /></a>
  <a href="https://discord.gg/YctCnvvshC"><img alt="Discord" src="https://img.shields.io/discord/1411657095639601154?style=flat-square&logo=discord&logoColor=white&label=Discord&suffix=%20online" /></a>
</p>

<details>
<summary><strong>The most loved spec framework.</strong></summary>

[![Stars](https://img.shields.io/github/stars/Fission-AI/OpenSpec?style=flat-square&label=Stars)](https://github.com/Fission-AI/OpenSpec/stargazers)
[![Downloads](https://img.shields.io/npm/dm/@fission-ai/openspec?style=flat-square&label=Downloads/mo)](https://www.npmjs.com/package/@fission-ai/openspec)
[![Contributors](https://img.shields.io/github/contributors/Fission-AI/OpenSpec?style=flat-square&label=Contributors)](https://github.com/Fission-AI/OpenSpec/graphs/contributors)

</details>
<p></p>
Our philosophy:

```text
→ fluid not rigid
→ iterative not waterfall
→ easy not complex
→ built for brownfield not just greenfield
→ scalable from personal projects to enterprises
```

> [!TIP]
> **New workflow now available!** We've rebuilt OpenSpec with a new artifact-guided workflow.
>
> Run `/opsx:propose "your idea"` to get started. → [Learn more here](docs/opsx.md)

<p align="center">
  Follow <a href="https://x.com/0xTab">@0xTab on X</a> for updates · Join the <a href="https://discord.gg/YctCnvvshC">OpenSpec Discord</a> for help and questions.
</p>

### Teams

Using OpenSpec in a team? [Email here](mailto:teams@openspec.dev) for access to our Slack channel.

<!-- TODO: Add GIF demo of /opsx:propose → /opsx:archive workflow -->

## See it in action

```text
You: /opsx:propose add-dark-mode
AI:  Created openspec/changes/add-dark-mode/
     ✓ proposal.md — why we're doing this, what's changing
     ✓ specs/       — requirements and scenarios
     ✓ design.md    — technical approach
     ✓ tasks.md     — implementation checklist
     Ready for implementation!

You: /opsx:apply
AI:  Implementing tasks...
     ✓ 1.1 Add theme context provider
     ✓ 1.2 Create toggle component
     ✓ 2.1 Add CSS variables
     ✓ 2.2 Wire up localStorage
     All tasks complete!

You: /opsx:archive
AI:  Archived to openspec/changes/archive/2025-01-23-add-dark-mode/
     Specs updated. Ready for the next feature.
```

<details>
<summary><strong>OpenSpec Dashboard</strong></summary>

<p align="center">
  <img src="assets/openspec_dashboard.png" alt="OpenSpec dashboard preview" width="90%">
</p>

</details>

## Quick Start

**Requires Node.js 20.19.0 or higher.**

Install OpenSpec globally:

```bash
npm install -g @fission-ai/openspec@latest
```

Then navigate to your project directory and initialize:

```bash
cd your-project
openspec init
```

Now tell your AI: `/opsx:propose <what-you-want-to-build>`

If you want the expanded workflow (`/opsx:new`, `/opsx:continue`, `/opsx:ff`, `/opsx:verify`, `/opsx:sync`, `/opsx:bulk-archive`, `/opsx:onboard`), select it with `openspec config profile` and apply with `openspec update`.

> [!NOTE]
> Not sure if your tool is supported? [View the full list](docs/supported-tools.md) – we support 25+ tools and growing.
>
> Also works with pnpm, yarn, bun, and nix. [See installation options](docs/installation.md).

## Docs

→ **[Getting Started](docs/getting-started.md)**: first steps<br>
→ **[Workflows](docs/workflows.md)**: combos and patterns<br>
→ **[Commands](docs/commands.md)**: slash commands & skills<br>
→ **[CLI](docs/cli.md)**: terminal reference<br>
→ **[Supported Tools](docs/supported-tools.md)**: tool integrations & install paths<br>
→ **[Concepts](docs/concepts.md)**: how it all fits<br>
→ **[Multi-Language](docs/multi-language.md)**: multi-language support<br>
→ **[Customization](docs/customization.md)**: make it yours


## Why OpenSpec?

AI coding assistants are powerful but unpredictable when requirements live only in chat history. OpenSpec adds a lightweight spec layer so you agree on what to build before any code is written.

- **Agree before you build** — human and AI align on specs before code gets written
- **Stay organized** — each change gets its own folder with proposal, specs, design, and tasks
- **Work fluidly** — update any artifact anytime, no rigid phase gates
- **Use your tools** — works with 20+ AI assistants via slash commands

### How we compare

**vs. [Spec Kit](https://github.com/github/spec-kit)** (GitHub) — Thorough but heavyweight. Rigid phase gates, lots of Markdown, Python setup. OpenSpec is lighter and lets you iterate freely.

**vs. [Kiro](https://kiro.dev)** (AWS) — Powerful but you're locked into their IDE and limited to Claude models. OpenSpec works with the tools you already use.

**vs. nothing** — AI coding without specs means vague prompts and unpredictable results. OpenSpec brings predictability without the ceremony.

## Updating OpenSpec

**Upgrade the package**

```bash
npm install -g @fission-ai/openspec@latest
```

**Refresh agent instructions**

Run this inside each project to regenerate AI guidance and ensure the latest slash commands are active:

```bash
openspec update
```

## Usage Notes

**Model selection**: OpenSpec works best with high-reasoning models. We recommend Opus 4.5 and GPT 5.2 for both planning and implementation.

**Context hygiene**: OpenSpec benefits from a clean context window. Clear your context before starting implementation and maintain good context hygiene throughout your session.

## Contributing

**Small fixes** — Bug fixes, typo corrections, and minor improvements can be submitted directly as PRs.

**Larger changes** — For new features, significant refactors, or architectural changes, please submit an OpenSpec change proposal first so we can align on intent and goals before implementation begins.

When writing proposals, keep the OpenSpec philosophy in mind: we serve a wide variety of users across different coding agents, models, and use cases. Changes should work well for everyone.

**AI-generated code is welcome** — as long as it's been tested and verified. PRs containing AI-generated code should mention the coding agent and model used (e.g., "Generated with Claude Code using claude-opus-4-5-20251101").

### Development

- Install dependencies: `pnpm install`
- Build: `pnpm run build`
- Test: `pnpm test`
- Develop CLI locally: `pnpm run dev` or `pnpm run dev:cli`
- Conventional commits (one-line): `type(scope): subject`

## Other

<details>
<summary><strong>Telemetry</strong></summary>

OpenSpec collects anonymous usage stats.

We collect only command names and version to understand usage patterns. No arguments, paths, content, or PII. Automatically disabled in CI.

**Opt-out:** `export OPENSPEC_TELEMETRY=0` or `export DO_NOT_TRACK=1`

</details>

<details>
<summary><strong>Maintainers & Advisors</strong></summary>

See [MAINTAINERS.md](MAINTAINERS.md) for the list of core maintainers and advisors who help guide the project.

</details>



## License

MIT



> **Deep fetch: 30 key files fetched beyond README.**



---

# FILE: .coderabbit.yaml

# yaml-language-server: $schema=https://coderabbit.ai/integrations/schema.v2.json
# Minimal configuration for getting started
language: "en-US"
reviews:
  profile: "chill"
  high_level_summary: true
  auto_review:
    enabled: true
    drafts: false
    base_branches:
      - ".*"


---

# FILE: AGENTS.md




---

# FILE: CHANGELOG.md

# @fission-ai/openspec

## 1.3.0

### Minor Changes

- [#952](https://github.com/Fission-AI/OpenSpec/pull/952) [`cce787e`](https://github.com/Fission-AI/OpenSpec/commit/cce787ec4083da2b27781f6786f5ce0002909a7b) Thanks [@TabishB](https://github.com/TabishB)! - ### New Features

  - **Junie support** — Added tool and command generation for JetBrains Junie
  - **Lingma IDE support** — Added configuration support for Lingma IDE
  - **ForgeCode support** — Added tool support for ForgeCode
  - **IBM Bob support** — Added support for IBM Bob coding assistant

  ### Bug Fixes

  - **Shell completions opt-in** — Completion install is now opt-in, fixing PowerShell encoding corruption
  - **Copilot auto-detection** — Prevented false GitHub Copilot detection from a bare `.github/` directory
  - **pi.dev command generation** — Fixed command reference transforms and template argument passing

### Patch Changes

- [#760](https://github.com/Fission-AI/OpenSpec/pull/760) [`61eb999`](https://github.com/Fission-AI/OpenSpec/commit/61eb999f7c6c0fc98d2e7f3678756fce6a3f4378) Thanks [@fsilvaortiz](https://github.com/fsilvaortiz)! - fix: OpenCode adapter now uses `.opencode/commands/` (plural) to match OpenCode's official directory convention. Fixes #748.

- [#759](https://github.com/Fission-AI/OpenSpec/pull/759) [`afdca0d`](https://github.com/Fission-AI/OpenSpec/commit/afdca0d5dab1aa109cfd8848b2512333ccad60c3) Thanks [@fsilvaortiz](https://github.com/fsilvaortiz)! - fix: `openspec status` now exits gracefully when no changes exist instead of throwing a fatal error. Fixes #714.

## 1.2.0

### Minor Changes

- [#747](https://github.com/Fission-AI/OpenSpec/pull/747) [`1e94443`](https://github.com/Fission-AI/OpenSpec/commit/1e94443a3551b228eecbc89e95d96d3b9600a192) Thanks [@TabishB](https://github.com/TabishB)! - ### New Features

  - **Profile system** — Choose between `core` (4 essential workflows) and `custom` (pick any subset) profiles to control which skills get installed. Manage profiles with the new `openspec config profile` command
  - **Propose workflow** — New one-step workflow creates a complete change proposal with design, specs, and tasks from a single request — no need to run `new` then `ff` separately
  - **AI tool auto-detection** — `openspec init` now scans your project for existing tool directories (`.claude/`, `.cursor/`, etc.) and pre-selects detected tools
  - **Pi (pi.dev) support** — Pi coding agent is now a supported tool with prompt and skill generation
  - **Kiro support** — AWS Kiro IDE is now a supported tool with prompt and skill generation
  - **Sync prunes deselected workflows** — `openspec update` now removes command files and skill directories for workflows you've deselected, keeping your project clean
  - **Config drift warning** — `openspec config list` warns when global config is out of sync with the current project

  ### Bug Fixes

  - Fixed onboard preflight giving a false "not initialized" error on freshly initialized projects
  - Fixed archive workflow stopping mid-way when syncing — it now properly resumes after sync completes
  - Added Windows PowerShell alternatives for onboard shell commands

## 1.1.1

### Patch Changes

- [#627](https://github.com/Fission-AI/OpenSpec/pull/627) [`afb73cf`](https://github.com/Fission-AI/OpenSpec/commit/afb73cf9ec59c6f8b26d0c538c0218c203ba3c56) Thanks [@TabishB](https://github.com/TabishB)! - ### Bug Fixes

  - **OpenCode command references** — Command references in generated files now use the correct `/opsx-` hyphen format instead of `/opsx:` colon format, ensuring commands work properly in OpenCode

## 1.1.0

### Minor Changes

- [#625](https://github.com/Fission-AI/OpenSpec/pull/625) [`53081fb`](https://github.com/Fission-AI/OpenSpec/commit/53081fb2a26ec66d2950ae0474b9a56cbc5b5a76) Thanks [@TabishB](https://github.com/TabishB)! - ### Bug Fixes

  - **Codex global path support** — Codex adapter now resolves global paths correctly, fixing workflow file generation when run outside the project directory (#622)
  - **Archive operations on cross-device or restricted paths** — Archive now falls back to copy+remove when rename fails with EPERM or EXDEV errors, fixing failures on networked/external drives (#605)
  - **Slash command hints in workflow messages** — Workflow completion messages now display helpful slash command hints for next steps (#603)
  - **Windsurf workflow file path** — Updated Windsurf adapter to use the correct `workflows` directory instead of the legacy `commands` path (#610)

### Patch Changes

- [#550](https://github.com/Fission-AI/OpenSpec/pull/550) [`86d2e04`](https://github.com/Fission-AI/OpenSpec/commit/86d2e04cae76a999dbd1b4571f52fa720036be0c) Thanks [@jerome-benoit](https://github.com/jerome-benoit)! - ### Improvements

  - **Nix flake maintenance** — Version now read dynamically from package.json, reducing manual sync issues
  - **Nix build optimization** — Source filtering excludes node_modules and artifacts, improving build times
  - **update-flake.sh script** — Detects when hash is already correct, skipping unnecessary rebuilds

  ### Other

  - Updated Nix CI actions to latest versions (nix-installer v21, magic-nix-cache v13)

## 1.0.2

### Patch Changes

- [#596](https://github.com/Fission-AI/OpenSpec/pull/596) [`e91568d`](https://github.com/Fission-AI/OpenSpec/commit/e91568deb948073f3e9d9bb2d2ab5bf8080d6cf4) Thanks [@TabishB](https://github.com/TabishB)! - ### Bug Fixes

  - Clarified spec naming convention — Specs should be named after capabilities (`specs/<capability>/spec.md`), not changes
  - Fixed task checkbox format guidance — Tasks now clearly require `- [ ]` checkbox format for apply phase tracking

## 1.0.1

### Patch Changes

- [#587](https://github.com/Fission-AI/OpenSpec/pull/587) [`943e0d4`](https://github.com/Fission-AI/OpenSpec/commit/943e0d41026d034de66b9442d1276c01b293eb2b) Thanks [@TabishB](https://github.com/TabishB)! - ### Bug Fixes

  - Fixed incorrect archive path in onboarding documentation — the template now shows the correct path `openspec/changes/archive/YYYY-MM-DD-<name>/` instead of the incorrect `openspec/archive/YYYY-MM-DD--<name>/`

## 1.0.0

### Major Changes

- [#578](https://github.com/Fission-AI/OpenSpec/pull/578) [`0cc9d90`](https://github.com/Fission-AI/OpenSpec/commit/0cc9d9025af367faa1688a7b2606a2549053cd3f) Thanks [@TabishB](https://github.com/TabishB)! - ## OpenSpec 1.0 — The OPSX Release

  The workflow has been rebuilt from the ground up. OPSX replaces the old phase-locked `/openspec:*` commands with an action-based system where AI understands what artifacts exist, what's ready to create, and what each action unlocks.

  ### Breaking Changes

  - **Old commands removed** — `/openspec:proposal`, `/openspec:apply`, and `/openspec:archive` no longer exist
  - **Config files removed** — Tool-specific instruction files (`CLAUDE.md`, `.cursorrules`, `AGENTS.md`, `project.md`) are no longer generated
  - **Migration** — Run `openspec init` to upgrade. Legacy artifacts are detected and cleaned up with confirmation.

  ### From Static Prompts to Dynamic Instructions

  **Before:** AI received the same static instructions every time, regardless of project state.

  **Now:** Instructions are dynamically assembled from three layers:

  1. **Context** — Project background from `config.yaml` (tech stack, conventions)
  2. **Rules** — Artifact-specific constraints (e.g., "propose spike tasks for unknowns")
  3. **Template** — The actual structure for the output file

  AI queries the CLI for real-time state: which artifacts exist, what's ready to create, what dependencies are satisfied, and what each action unlocks.

  ### From Phase-Locked to Action-Based

  **Before:** Linear workflow — proposal → apply → archive. Couldn't easily go back or iterate.

  **Now:** Flexible actions on a change. Edit any artifact anytime. The artifact graph tracks state automatically.

  | Command              | What it does                                         |
  | -------------------- | ---------------------------------------------------- |
  | `/opsx:explore`      | Think through ideas before committing to a change    |
  | `/opsx:new`          | Start a new change                                   |
  | `/opsx:continue`     | Create one artifact at a time (step-through)         |
  | `/opsx:ff`           | Create all planning artifacts at once (fast-forward) |
  | `/opsx:apply`        | Implement tasks                                      |
  | `/opsx:verify`       | Validate implementation matches artifacts            |
  | `/opsx:sync`         | Sync delta specs to main specs                       |
  | `/opsx:archive`      | Archive completed change                             |
  | `/opsx:bulk-archive` | Archive multiple changes with conflict detection     |
  | `/opsx:onboard`      | Guided 15-minute walkthrough of complete workflow    |

  ### From Text Merging to Semantic Spec Syncing

  **Before:** Spec updates required manual merging or wholesale file replacement.

  **Now:** Delta specs use semantic markers that AI understands:

  - `## ADDED Requirements` — New requirements to add
  - `## MODIFIED Requirements` — Partial updates (add scenario without copying existing ones)
  - `## REMOVED Requirements` — Delete with reason and migration notes
  - `## RENAMED Requirements` — Rename preserving content

  Archive parses these at the requirement level, not brittle header matching.

  ### From Scattered Files to Agent Skills

  **Before:** 8+ config files at project root + slash commands scattered across 21 tool-specific locations with different formats.

  **Now:** Single `.claude/skills/` directory with YAML-fronted markdown files. Auto-detected by Claude Code, Cursor, Windsurf. Cross-editor compatible.

  ### New Features

  - **Onboarding skill** — `/opsx:onboard` walks new users through their first complete change with codebase-aware task suggestions and step-by-step narration (11 phases, ~15 minutes)

  - **21 AI tools supported** — Claude Code, Cursor, Windsurf, Continue, Gemini CLI, GitHub Copilot, Amazon Q, Cline, RooCode, Kilo Code, Auggie, CodeBuddy, Qoder, Qwen, CoStrict, Crush, Factory, OpenCode, Antigravity, iFlow, and Codex

  - **Interactive setup** — `openspec init` shows animated welcome screen and searchable multi-select for choosing tools. Pre-selects already-configured tools for easy refresh.

  - **Customizable schemas** — Define custom artifact workflows in `openspec/schemas/` without touching package code. Teams can share workflows via version control.

  ### Bug Fixes

  - Fixed Claude Code YAML parsing failure when command names contained colons
  - Fixed task file parsing to handle trailing whitespace on checkbox lines
  - Fixed JSON instruction output to separate context/rules from template — AI was copying constraint blocks into artifact files

  ### Documentation

  - New getting-started guide, CLI reference, concepts documentation
  - Removed misleading "edit mid-flight and continue" claims that weren't implemented
  - Added migration guide for upgrading from pre-OPSX versions

## 0.23.0

### Minor Changes

- [#540](https://github.com/Fission-AI/OpenSpec/pull/540) [`c4cfdc7`](https://github.com/Fission-AI/OpenSpec/commit/c4cfdc7c499daef30d8a218f5f59b8d9e5adb754) Thanks [@TabishB](https://github.com/TabishB)! - ### New Features

  - **Bulk archive skill** — Archive multiple completed changes in a single operation with `/opsx:bulk-archive`. Includes batch validation, spec conflict detection, and consolidated confirmation

  ### Other

  - **Simplified setup** — Config creation now uses sensible defaults with helpful comments instead of interactive prompts

## 0.22.0

### Minor Changes

- [#530](https://github.com/Fission-AI/OpenSpec/pull/530) [`33466b1`](https://github.com/Fission-AI/OpenSpec/commit/33466b1e2a6798bdd6d0e19149173585b0612e6f) Thanks [@TabishB](https://github.com/TabishB)! - Add project-level configuration, project-local schemas, and schema management commands

  **New Features**

  - **Project-level configuration** — Configure OpenSpec behavior per-project via `openspec/config.yaml`, including custom rules injection, context files, and schema resolution settings
  - **Project-local schemas** — Define custom artifact schemas within your project's `openspec/schemas/` directory for project-specific workflows
  - **Schema management commands** — New `openspec schema` commands (`list`, `show`, `export`, `validate`) for inspecting and managing artifact schemas (experimental)

  **Bug Fixes**

  - Fixed config loading to handle null `rules` field in project configuration

## 0.21.0

### Minor Changes

- [#516](https://github.com/Fission-AI/OpenSpec/pull/516) [`b5a8847`](https://github.com/Fission-AI/OpenSpec/commit/b5a884748be6156a7bb140b4941cfec4f20a9fc8) Thanks [@TabishB](https://github.com/TabishB)! - Add feedback command and Nix flake support

  **New Features**

  - **Feedback command** — Submit feedback directly from the CLI with `openspec feedback`, which creates GitHub Issues with automatic metadata inclusion and graceful fallback for manual submission
  - **Nix flake support** — Install and develop openspec using Nix with the new `flake.nix`, including automated flake maintenance and CI validation

  **Bug Fixes**

  - **Explore mode guardrails** — Explore mode now explicitly prevents implementation, keeping the focus on thinking and discovery while still allowing artifact creation

  **Other**

  - Improved change inference in `opsx apply` — automatically detects the target change from conversation context or prompts when ambiguous
  - Streamlined archive sync assessment with clearer delta spec location guidance

## 0.20.0

### Minor Changes

- [#502](https://github.com/Fission-AI/OpenSpec/pull/502) [`9db74aa`](https://github.com/Fission-AI/OpenSpec/commit/9db74aa5ac6547efadaed795217cfa17444f2004) Thanks [@TabishB](https://github.com/TabishB)! - Add `/opsx:verify` command and fix vitest process storms

  **New Features**

  - **`/opsx:verify` command** — Validate that change implementations match their specifications

  **Bug Fixes**

  - Fixed vitest process storms by capping worker parallelism
  - Fixed agent workflows to use non-interactive mode for validation commands
  - Fixed PowerShell completions generator to remove trailing commas

## 0.19.0

### Minor Changes

- eb152eb: Add Continue IDE support, shell completions, and `/opsx:explore` command

  **New Features**

  - **Continue IDE support** – OpenSpec now generates slash commands for [Continue](https://continue.dev/), expanding editor integration options alongside Cursor, Windsurf, Claude Code, and others
  - **Shell completions for Bash, Fish, and PowerShell** – Run `openspec completion install` to set up tab completion in your preferred shell
  - **`/opsx:explore` command** – A new thinking partner mode for exploring ideas and investigating problems before committing to changes
  - **Codebuddy slash command improvements** – Updated frontmatter format for better compatibility

  **Bug Fixes**

  - Shell completions now correctly offer parent-level flags (like `--help`) when a command has subcommands
  - Fixed Windows compatibility issues in tests

  **Other**

  - Added optional anonymous usage statistics to help understand how OpenSpec is used. This is **opt-out** by default – set `OPENSPEC_TELEMETRY=0` or `DO_NOT_TRACK=1` to disable. Only command names and version are collected; no arguments, file paths, or content. Automatically disabled in CI environments.

## 0.18.0

### Minor Changes

- 8dfd824: Add OPSX experimental workflow commands and enhanced artifact system

  **New Commands:**

  - `/opsx:ff` - Fast-forward through artifact creation, generating all needed artifacts in one go
  - `/opsx:sync` - Sync delta specs from a change to main specs
  - `/opsx:archive` - Archive completed changes with smart sync check

  **Artifact Workflow Enhancements:**

  - Schema-aware apply instructions with inline guidance and XML output
  - Agent schema selection for experimental artifact workflow
  - Per-change schema metadata via `.openspec.yaml` files
  - Agent Skills for experimental artifact workflow
  - Instruction loader for template loading and change context
  - Restructured schemas as directories with templates

  **Improvements:**

  - Enhanced list command with last modified timestamps and sorting
  - Change creation utilities for better workflow support

  **Fixes:**

  - Normalize paths for cross-platform glob compatibility
  - Allow REMOVED requirements when creating new spec files

## 0.17.2

### Patch Changes

- 455c65f: Fix `--no-interactive` flag in validate command to properly disable spinner, preventing hangs in pre-commit hooks and CI environments

## 0.17.1

### Patch Changes

- a2757e7: Fix pre-commit hook hang issue in config command by using dynamic import for @inquirer/prompts

  The config command was causing pre-commit hooks to hang indefinitely due to stdin event listeners being registered at module load time. This fix converts the static import to a dynamic import that only loads inquirer when the `config reset` command is actually used interactively.

  Also adds ESLint with a rule to prevent static @inquirer imports, avoiding future regressions.

## 0.17.0

### Minor Changes

- 2e71835: Add `openspec config` command and Oh-my-zsh completions

  **New Features**

  - Add `openspec config` command for managing global configuration settings
  - Implement global config directory with XDG Base Directory specification support
  - Add Oh-my-zsh shell completions support for enhanced CLI experience

  **Bug Fixes**

  - Fix hang in pre-commit hooks by using dynamic imports
  - Respect XDG_CONFIG_HOME environment variable on all platforms
  - Resolve Windows compatibility issues in zsh-installer tests
  - Align cli-completion spec with implementation
  - Remove hardcoded agent field from slash commands

  **Documentation**

  - Alphabetize AI tools list in README and make it collapsible

## 0.16.0

### Minor Changes

- c08fbc1: Add new AI tool integrations and enhancements:

  - **feat(iflow-cli)**: Add iFlow-cli integration with slash command support and documentation
  - **feat(init)**: Add IDE restart instruction after init to inform users about slash command availability
    **feat(antigravity)**: Add Antigravity slash command support
  - **fix**: Generate TOML commands for Qwen Code (fixes #293)
  - Clarify scaffold proposal documentation and enhance proposal guidelines
  - Update proposal guidelines to emphasize design-first approach before implementation

## Unreleased

### Minor Changes

- Add Continue slash command support so `openspec init` can generate `.continue/prompts/openspec-*.prompt` files with MARKDOWN frontmatter and `$ARGUMENTS` placeholder, and refresh them on `openspec update`.

- Add Antigravity slash command support so `openspec init` can generate `.agent/workflows/openspec-*.md` files with description-only frontmatter and `openspec update` refreshes existing workflows alongside Windsurf.

## 0.15.0

### Minor Changes

- 4758c5c: Add support for new AI tools with native slash command integration

  - **Gemini CLI**: Add native TOML-based slash command support for Gemini CLI with `.gemini/commands/openspec/` integration
  - **RooCode**: Add RooCode integration with configurator, slash commands, and templates
  - **Cline**: Fix Cline to use workflows instead of rules for slash commands (`.clinerules/workflows/` paths)
  - **Documentation**: Update documentation to reflect new integrations and workflow changes

## 0.14.0

### Minor Changes

- 8386b91: Add support for new AI assistants and configuration improvements

  - feat: add Qwen Code support with slash command integration
  - feat: add $ARGUMENTS support to apply slash command for dynamic variable passing
  - feat: add Qoder CLI support to configuration and documentation
  - feat: add CoStrict AI assistant support
  - fix: recreate missing openspec template files in extend mode
  - fix: prevent false 'already configured' detection for tools
  - fix: use change-id as fallback title instead of "Untitled Change"
  - docs: add guidance for populating project-level context
  - docs: add Crush to supported AI tools in README

## 0.13.0

### Minor Changes

- 668a125: Add support for multiple AI assistants and improve validation

  This release adds support for several new AI coding assistants:

  - CodeBuddy Code - AI-powered coding assistant
  - CodeRabbit - AI code review assistant
  - Cline - Claude-powered CLI assistant
  - Crush AI - AI assistant platform
  - Auggie (Augment CLI) - Code augmentation tool

  New features:

  - Archive slash command now supports arguments for more flexible workflows

  Bug fixes:

  - Delta spec validation now handles case-insensitive headers and properly detects empty sections
  - Archive validation now correctly honors --no-validate flag and ignores metadata

  Documentation improvements:

  - Added VS Code dev container configuration for easier development setup
  - Updated AGENTS.md with explicit change-id notation
  - Enhanced slash commands documentation with restart notes

## 0.12.0

### Minor Changes

- 082abb4: Add factory function support for slash commands and non-interactive init options

  This release includes two new features:

  - **Factory function support for slash commands**: Slash commands can now be defined as functions that return command objects, enabling dynamic command configuration
  - **Non-interactive init options**: Added `--tools`, `--all-tools`, and `--skip-tools` CLI flags to `openspec init` for automated initialization in CI/CD pipelines while maintaining backward compatibility with interactive mode

## 0.11.0

### Minor Changes

- 312e1d6: Add Amazon Q Developer CLI integration. OpenSpec now supports Amazon Q Developer with automatic prompt generation in `.amazonq/prompts/` directory, allowing you to use OpenSpec slash commands with Amazon Q's @-syntax.

## 0.10.0

### Minor Changes

- d7e0ce8: Improve init wizard Enter key behavior to allow proceeding through prompts more naturally

## 0.9.2

### Patch Changes

- 2ae0484: Fix cross-platform path handling issues. This release includes fixes for joinPath behavior and slash command path resolution to ensure OpenSpec works correctly across all platforms.

## 0.9.1

### Patch Changes

- 8210970: Fix OpenSpec not working on Windows when Codex integration is selected. This release includes fixes for cross-platform path handling and normalization to ensure OpenSpec works correctly on Windows systems.

## 0.9.0

### Minor Changes

- efbbf3b: Add support for Codex and GitHub Copilot slash commands with YAML frontmatter and $ARGUMENTS

## Unreleased

### Minor Changes

- Add GitHub Copilot slash command support. OpenSpec now writes prompts to `.github/prompts/openspec-{proposal,apply,archive}.prompt.md` with YAML frontmatter and `$ARGUMENTS` placeholder, and refreshes them on `openspec update`.

## 0.8.1

### Patch Changes

- d070d08: Fix CLI version mismatch and add a release guard that validates the packed tarball prints the same version as package.json via `openspec --version`.

## 0.8.0

### Minor Changes

- c29b06d: Add Windsurf support.
- Add Codex slash command support. OpenSpec now writes prompts directly to Codex's global directory (`~/.codex/prompts` or `$CODEX_HOME/prompts`) and refreshes them on `openspec update`.

## 0.7.0

### Minor Changes

- Add native Kilo Code workflow integration so `openspec init` and `openspec update` manage `.kilocode/workflows/openspec-*.md` files.
- Always scaffold the managed root `AGENTS.md` hand-off stub and regroup the AI tool prompts during init/update to keep instructions consistent.

## 0.6.0

### Minor Changes

- Slim the generated root agent instructions down to a managed hand-off stub and update the init/update flows to refresh it safely.

## 0.5.0

### Minor Changes

- feat: implement Phase 1 E2E testing with cross-platform CI matrix

  - Add shared runCLI helper in test/helpers/run-cli.ts for spawn testing
  - Create test/cli-e2e/basic.test.ts covering help, version, validate flows
  - Migrate existing CLI exec tests to use runCLI helper
  - Extend CI matrix to bash (Linux/macOS) and pwsh (Windows)
  - Split PR and main workflows for optimized feedback

### Patch Changes

- Make apply instructions more specific

  Improve agent templates and slash command templates with more specific and actionable apply instructions.

- docs: improve documentation and cleanup

  - Document non-interactive flag for archive command
  - Replace discord badge in README
  - Archive completed changes for better organization

## 0.4.0

### Minor Changes

- Add OpenSpec change proposals for CLI improvements and enhanced user experience
- Add Opencode slash commands support for AI-driven development workflows

### Patch Changes

- Add documentation improvements including --yes flag for archive command template and Discord badge
- Fix normalize line endings in markdown parser to handle CRLF files properly

## 0.3.0

### Minor Changes

- Enhance `openspec init` with extend mode, multi-tool selection, and an interactive `AGENTS.md` configurator.

## 0.2.0

### Minor Changes

- ce5cead: - Add an `openspec view` dashboard that rolls up spec counts and change progress at a glance
  - Generate and update AI slash commands alongside the renamed `openspec/AGENTS.md` instructions file
  - Remove the deprecated `openspec diff` command and direct users to `openspec show`

## 0.1.0

### Minor Changes

- 24b4866: Initial release



---

# FILE: MAINTAINERS.md

# Maintainers

People who maintain and guide OpenSpec.

## Core Maintainers

| Name | GitHub | Role |
|------|--------|------|
| Tabish Bidiwale | [@TabishB](https://github.com/TabishB) | Lead maintainer |

## Advisors

Advisors help shape technical direction and provide guidance to the project.

| Name | GitHub | Focus |
|------|--------|-------|
| Hari Krishnan | [@harikrishnan83](https://github.com/harikrishnan83) | Technical direction |



---

# FILE: README_OLD.md

<p align="center">
  <a href="https://github.com/Fission-AI/OpenSpec">
    <picture>
      <source srcset="assets/openspec_pixel_dark.svg" media="(prefers-color-scheme: dark)">
      <source srcset="assets/openspec_pixel_light.svg" media="(prefers-color-scheme: light)">
      <img src="assets/openspec_pixel_light.svg" alt="OpenSpec logo" height="64">
    </picture>
  </a>
  
</p>
<p align="center">Spec-driven development for AI coding assistants.</p>
<p align="center">
  <a href="https://github.com/Fission-AI/OpenSpec/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/Fission-AI/OpenSpec/actions/workflows/ci.yml/badge.svg" /></a>
  <a href="https://www.npmjs.com/package/@fission-ai/openspec"><img alt="npm version" src="https://img.shields.io/npm/v/@fission-ai/openspec?style=flat-square" /></a>
  <a href="https://nodejs.org/"><img alt="node version" src="https://img.shields.io/node/v/@fission-ai/openspec?style=flat-square" /></a>
  <a href="./LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" /></a>
  <a href="https://conventionalcommits.org"><img alt="Conventional Commits" src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square" /></a>
  <a href="https://discord.gg/YctCnvvshC"><img alt="Discord" src="https://img.shields.io/badge/Discord-Join%20the%20community-5865F2?logo=discord&logoColor=white&style=flat-square" /></a>
</p>

<p align="center">
  <img src="assets/openspec_dashboard.png" alt="OpenSpec dashboard preview" width="90%">
</p>

<p align="center">
  Follow <a href="https://x.com/0xTab">@0xTab on X</a> for updates · Join the <a href="https://discord.gg/YctCnvvshC">OpenSpec Discord</a> for help and questions.
</p>

<p align="center">
  <sub>🧪 <strong>New:</strong> <a href="docs/opsx.md">OPSX Workflow</a> — schema-driven, hackable, fluid. Iterate on workflows without code changes.</sub>
</p>

# OpenSpec

OpenSpec aligns humans and AI coding assistants with spec-driven development so you agree on what to build before any code is written. **No API keys required.**

## Why OpenSpec?

AI coding assistants are powerful but unpredictable when requirements live in chat history. OpenSpec adds a lightweight specification workflow that locks intent before implementation, giving you deterministic, reviewable outputs.

Key outcomes:
- Human and AI stakeholders agree on specs before work begins.
- Structured change folders (proposals, tasks, and spec updates) keep scope explicit and auditable.
- Shared visibility into what's proposed, active, or archived.
- Works with the AI tools you already use: custom slash commands where supported, context rules everywhere else.

## How OpenSpec compares (at a glance)

- **Lightweight**: simple workflow, no API keys, minimal setup.
- **Brownfield-first**: works great beyond 0→1. OpenSpec separates the source of truth from proposals: `openspec/specs/` (current truth) and `openspec/changes/` (proposed updates). This keeps diffs explicit and manageable across features.
- **Change tracking**: proposals, tasks, and spec deltas live together; archiving merges the approved updates back into specs.
- **Compared to spec-kit & Kiro**: those shine for brand-new features (0→1). OpenSpec also excels when modifying existing behavior (1→n), especially when updates span multiple specs.

See the full comparison in [How OpenSpec Compares](#how-openspec-compares).

## How It Works

```
┌────────────────────┐
│ Draft Change       │
│ Proposal           │
└────────┬───────────┘
         │ share intent with your AI
         ▼
┌────────────────────┐
│ Review & Align     │
│ (edit specs/tasks) │◀──── feedback loop ──────┐
└────────┬───────────┘                          │
         │ approved plan                        │
         ▼                                      │
┌────────────────────┐                          │
│ Implement Tasks    │──────────────────────────┘
│ (AI writes code)   │
└────────┬───────────┘
         │ ship the change
         ▼
┌────────────────────┐
│ Archive & Update   │
│ Specs (source)     │
└────────────────────┘

1. Draft a change proposal that captures the spec updates you want.
2. Review the proposal with your AI assistant until everyone agrees.
3. Implement tasks that reference the agreed specs.
4. Archive the change to merge the approved updates back into the source-of-truth specs.
```

## Getting Started

### Supported AI Tools

<details>
<summary><strong>Native Slash Commands</strong> (click to expand)</summary>

These tools have built-in OpenSpec commands. Select the OpenSpec integration when prompted.

| Tool | Commands |
|------|----------|
| **Amazon Q Developer** | `@openspec-proposal`, `@openspec-apply`, `@openspec-archive` (`.amazonq/prompts/`) |
| **Antigravity** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` (`.agent/workflows/`) |
| **Auggie (Augment CLI)** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` (`.augment/commands/`) |
| **Claude Code** | `/openspec:proposal`, `/openspec:apply`, `/openspec:archive` |
| **Cline** | Workflows in `.clinerules/workflows/` directory (`.clinerules/workflows/openspec-*.md`) |
| **CodeBuddy Code (CLI)** | `/openspec:proposal`, `/openspec:apply`, `/openspec:archive` (`.codebuddy/commands/`) — see [docs](https://www.codebuddy.ai/cli) |
| **Codex** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` (global: `~/.codex/prompts`, auto-installed) |
| **Continue** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` (`.continue/prompts/`) |
| **CoStrict** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` (`.cospec/openspec/commands/`) — see [docs](https://costrict.ai)|
| **Crush** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` (`.crush/commands/openspec/`) |
| **Cursor** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` |
| **Factory Droid** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` (`.factory/commands/`) |
| **Gemini CLI** | `/openspec:proposal`, `/openspec:apply`, `/openspec:archive` (`.gemini/commands/openspec/`) |
| **GitHub Copilot** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` (`.github/prompts/`) |
| **iFlow (iflow-cli)** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` (`.iflow/commands/`) |
| **Kilo Code** | `/openspec-proposal.md`, `/openspec-apply.md`, `/openspec-archive.md` (`.kilocode/workflows/`) |
| **OpenCode** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` |
| **Qoder** | `/openspec:proposal`, `/openspec:apply`, `/openspec:archive` (`.qoder/commands/openspec/`) — see [docs](https://qoder.com) |
| **Qwen Code** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` (`.qwen/commands/`) |
| **RooCode** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` (`.roo/commands/`) |
| **Windsurf** | `/openspec-proposal`, `/openspec-apply`, `/openspec-archive` (`.windsurf/workflows/`) |

Kilo Code discovers team workflows automatically. Save the generated files under `.kilocode/workflows/` and trigger them from the command palette with `/openspec-proposal.md`, `/openspec-apply.md`, or `/openspec-archive.md`.

</details>

<details>
<summary><strong>AGENTS.md Compatible</strong> (click to expand)</summary>

These tools automatically read workflow instructions from `openspec/AGENTS.md`. Ask them to follow the OpenSpec workflow if they need a reminder. Learn more about the [AGENTS.md convention](https://agents.md/).

| Tools |
|-------|
| Amp • Jules • Others |

</details>

### Install & Initialize

#### Prerequisites
- **Node.js >= 20.19.0** - Check your version with `node --version`

#### Step 1: Install the CLI globally

**Option A: Using npm**

```bash
npm install -g @fission-ai/openspec@latest
```

Verify installation:
```bash
openspec --version
```

**Option B: Using Nix (NixOS and Nix package manager)**

Run OpenSpec directly without installation:
```bash
nix run github:Fission-AI/OpenSpec -- init
```

Or install to your profile:
```bash
nix profile install github:Fission-AI/OpenSpec
```

Or add to your development environment in `flake.nix`:
```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    openspec.url = "github:Fission-AI/OpenSpec";
  };

  outputs = { nixpkgs, openspec, ... }: {
    devShells.x86_64-linux.default = nixpkgs.legacyPackages.x86_64-linux.mkShell {
      buildInputs = [ openspec.packages.x86_64-linux.default ];
    };
  };
}
```

Verify installation:
```bash
openspec --version
```

#### Step 2: Initialize OpenSpec in your project

Navigate to your project directory:
```bash
cd my-project
```

Run the initialization:
```bash
openspec init
```

**What happens during initialization:**
- You'll be prompted to pick any natively supported AI tools (Claude Code, CodeBuddy, Cursor, OpenCode, Qoder,etc.); other assistants always rely on the shared `AGENTS.md` stub
- OpenSpec automatically configures slash commands for the tools you choose and always writes a managed `AGENTS.md` hand-off at the project root
- A new `openspec/` directory structure is created in your project

**After setup:**
- Primary AI tools can trigger `/openspec` workflows without additional configuration
- Run `openspec list` to verify the setup and view any active changes
- If your coding assistant doesn't surface the new slash commands right away, restart it. Slash commands are loaded at startup,
  so a fresh launch ensures they appear

### Optional: Populate Project Context

After `openspec init` completes, you'll receive a suggested prompt to help populate your project context:

```text
Populate your project context:
"Please read openspec/project.md and help me fill it out with details about my project, tech stack, and conventions"
```

Use `openspec/project.md` to define project-level conventions, standards, architectural patterns, and other guidelines that should be followed across all changes.

### Create Your First Change

Here's a real example showing the complete OpenSpec workflow. This works with any AI tool. Those with native slash commands will recognize the shortcuts automatically.

#### 1. Draft the Proposal
Start by asking your AI to create a change proposal:

```text
You: Create an OpenSpec change proposal for adding profile search filters by role and team
     (Shortcut for tools with slash commands: /openspec:proposal Add profile search filters)

AI:  I'll create an OpenSpec change proposal for profile filters.
     *Scaffolds openspec/changes/add-profile-filters/ with proposal.md, tasks.md, spec deltas.*
```

#### 2. Verify & Review
Check that the change was created correctly and review the proposal:

```bash
$ openspec list                             # Confirm the change folder exists
$ openspec validate add-profile-filters     # Validate spec formatting
$ openspec show add-profile-filters         # Review proposal, tasks, and spec delta
```

#### 3. Refine the Specs
Iterate on the specifications until they match your needs:

```text
You: Can you add acceptance criteria for the role and team filters?

AI:  I'll update the spec delta with scenarios for role and team filters.
     *Edits openspec/changes/add-profile-filters/specs/profile/spec.md and tasks.md.*
```

#### 4. Implement the Change
Once specs look good, start implementation:

```text
You: The specs look good. Let's implement this change.
     (Shortcut for tools with slash commands: /openspec:apply add-profile-filters)

AI:  I'll work through the tasks in the add-profile-filters change.
     *Implements tasks from openspec/changes/add-profile-filters/tasks.md*
     *Marks tasks complete: Task 1.1 ✓, Task 1.2 ✓, Task 2.1 ✓...*
```

#### 5. Archive the Completed Change
After implementation is complete, archive the change:

```text
AI:  All tasks are complete. The implementation is ready.

You: Please archive the change
     (Shortcut for tools with slash commands: /openspec:archive add-profile-filters)

AI:  I'll archive the add-profile-filters change.
    *Runs: openspec archive add-profile-filters --yes*
     ✓ Change archived successfully. Specs updated. Ready for the next feature!
```

Or run the command yourself in terminal:
```bash
$ openspec archive add-profile-filters --yes  # Archive the completed change without prompts
```

**Note:** Tools with native slash commands (Claude Code, CodeBuddy, Cursor, Codex, Qoder, RooCode) can use the shortcuts shown. All other tools work with natural language requests to "create an OpenSpec proposal", "apply the OpenSpec change", or "archive the change".

## Command Reference

```bash
openspec list               # View active change folders
openspec view               # Interactive dashboard of specs and changes
openspec show <change>      # Display change details (proposal, tasks, spec updates)
openspec validate <change>  # Check spec formatting and structure
openspec archive <change> [--yes|-y]   # Move a completed change into archive/ (non-interactive with --yes)
```

## Example: How AI Creates OpenSpec Files

When you ask your AI assistant to "add two-factor authentication", it creates:

```
openspec/
├── specs/
│   └── auth/
│       └── spec.md           # Current auth spec (if exists)
└── changes/
    └── add-2fa/              # AI creates this entire structure
        ├── proposal.md       # Why and what changes
        ├── tasks.md          # Implementation checklist
        ├── design.md         # Technical decisions (optional)
        └── specs/
            └── auth/
                └── spec.md   # Delta showing additions
```

### AI-Generated Spec (created in `openspec/specs/auth/spec.md`):

```markdown
# Auth Specification

## Purpose
Authentication and session management.

## Requirements
### Requirement: User Authentication
The system SHALL issue a JWT on successful login.

#### Scenario: Valid credentials
- WHEN a user submits valid credentials
- THEN a JWT is returned
```

### AI-Generated Change Delta (created in `openspec/changes/add-2fa/specs/auth/spec.md`):

```markdown
# Delta for Auth

## ADDED Requirements
### Requirement: Two-Factor Authentication
The system MUST require a second factor during login.

#### Scenario: OTP required
- WHEN a user submits valid credentials
- THEN an OTP challenge is required
```

### AI-Generated Tasks (created in `openspec/changes/add-2fa/tasks.md`):

```markdown
## 1. Database Setup
- [ ] 1.1 Add OTP secret column to users table
- [ ] 1.2 Create OTP verification logs table

## 2. Backend Implementation  
- [ ] 2.1 Add OTP generation endpoint
- [ ] 2.2 Modify login flow to require OTP
- [ ] 2.3 Add OTP verification endpoint

## 3. Frontend Updates
- [ ] 3.1 Create OTP input component
- [ ] 3.2 Update login flow UI
```

**Important:** You don't create these files manually. Your AI assistant generates them based on your requirements and the existing codebase.

## Understanding OpenSpec Files

### Delta Format

Deltas are "patches" that show how specs change:

- **`## ADDED Requirements`** - New capabilities
- **`## MODIFIED Requirements`** - Changed behavior (include complete updated text)
- **`## REMOVED Requirements`** - Deprecated features

**Format requirements:**
- Use `### Requirement: <name>` for headers
- Every requirement needs at least one `#### Scenario:` block
- Use SHALL/MUST in requirement text

## How OpenSpec Compares

### vs. spec-kit
OpenSpec’s two-folder model (`openspec/specs/` for the current truth, `openspec/changes/` for proposed updates) keeps state and diffs separate. This scales when you modify existing features or touch multiple specs. spec-kit is strong for greenfield/0→1 but provides less structure for cross-spec updates and evolving features.

### vs. Kiro.dev
OpenSpec groups every change for a feature in one folder (`openspec/changes/feature-name/`), making it easy to track related specs, tasks, and designs together. Kiro spreads updates across multiple spec folders, which can make feature tracking harder.

### vs. No Specs
Without specs, AI coding assistants generate code from vague prompts, often missing requirements or adding unwanted features. OpenSpec brings predictability by agreeing on the desired behavior before any code is written.

## Team Adoption

1. **Initialize OpenSpec** – Run `openspec init` in your repo.
2. **Start with new features** – Ask your AI to capture upcoming work as change proposals.
3. **Grow incrementally** – Each change archives into living specs that document your system.
4. **Stay flexible** – Different teammates can use Claude Code, CodeBuddy, Cursor, or any AGENTS.md-compatible tool while sharing the same specs.

Run `openspec update` whenever someone switches tools so your agents pick up the latest instructions and slash-command bindings.

## Updating OpenSpec

1. **Upgrade the package**
   ```bash
   npm install -g @fission-ai/openspec@latest
   ```
2. **Refresh agent instructions**
   - Run `openspec update` inside each project to regenerate AI guidance and ensure the latest slash commands are active.

## Experimental Features

<details>
<summary><strong>🧪 OPSX: Fluid, Iterative Workflow</strong> (Claude Code only)</summary>

**Why this exists:**
- Standard workflow is locked down — you can't tweak instructions or customize
- When AI output is bad, you can't improve the prompts yourself
- Same workflow for everyone, no way to match how your team works

**What's different:**
- **Hackable** — edit templates and schemas yourself, test immediately, no rebuild
- **Granular** — each artifact has its own instructions, test and tweak individually
- **Customizable** — define your own workflows, artifacts, and dependencies
- **Fluid** — no phase gates, update any artifact anytime

```
You can always go back:

  proposal ──→ specs ──→ design ──→ tasks ──→ implement
     ▲           ▲          ▲                    │
     └───────────┴──────────┴────────────────────┘
```

| Command | What it does |
|---------|--------------|
| `/opsx:new` | Start a new change |
| `/opsx:continue` | Create the next artifact (based on what's ready) |
| `/opsx:ff` | Fast-forward (all planning artifacts at once) |
| `/opsx:apply` | Implement tasks, updating artifacts as needed |
| `/opsx:archive` | Archive when done |

**Setup:** `openspec experimental`

[Full documentation →](docs/opsx.md)

</details>

<details>
<summary><strong>Telemetry</strong> – OpenSpec collects anonymous usage stats (opt-out: <code>OPENSPEC_TELEMETRY=0</code>)</summary>

We collect only command names and version to understand usage patterns. No arguments, paths, content, or PII. Automatically disabled in CI.

**Opt-out:** `export OPENSPEC_TELEMETRY=0` or `export DO_NOT_TRACK=1`

</details>

## Contributing

- Install dependencies: `pnpm install`
- Build: `pnpm run build`
- Test: `pnpm test`
- Develop CLI locally: `pnpm run dev` or `pnpm run dev:cli`
- Conventional commits (one-line): `type(scope): subject`

<details>
<summary><strong>Maintainers & Advisors</strong></summary>

See [MAINTAINERS.md](MAINTAINERS.md) for the list of core maintainers and advisors who help guide the project.

</details>

## License

MIT



---

# FILE: docs/cli.md

# CLI Reference

The OpenSpec CLI (`openspec`) provides terminal commands for project setup, validation, status inspection, and management. These commands complement the AI slash commands (like `/opsx:propose`) documented in [Commands](commands.md).

## Summary

| Category | Commands | Purpose |
|----------|----------|---------|
| **Setup** | `init`, `update` | Initialize and update OpenSpec in your project |
| **Browsing** | `list`, `view`, `show` | Explore changes and specs |
| **Validation** | `validate` | Check changes and specs for issues |
| **Lifecycle** | `archive` | Finalize completed changes |
| **Workflow** | `status`, `instructions`, `templates`, `schemas` | Artifact-driven workflow support |
| **Schemas** | `schema init`, `schema fork`, `schema validate`, `schema which` | Create and manage custom workflows |
| **Config** | `config` | View and modify settings |
| **Utility** | `feedback`, `completion` | Feedback and shell integration |

---

## Human vs Agent Commands

Most CLI commands are designed for **human use** in a terminal. Some commands also support **agent/script use** via JSON output.

### Human-Only Commands

These commands are interactive and designed for terminal use:

| Command | Purpose |
|---------|---------|
| `openspec init` | Initialize project (interactive prompts) |
| `openspec view` | Interactive dashboard |
| `openspec config edit` | Open config in editor |
| `openspec feedback` | Submit feedback via GitHub |
| `openspec completion install` | Install shell completions |

### Agent-Compatible Commands

These commands support `--json` output for programmatic use by AI agents and scripts:

| Command | Human Use | Agent Use |
|---------|-----------|-----------|
| `openspec list` | Browse changes/specs | `--json` for structured data |
| `openspec show <item>` | Read content | `--json` for parsing |
| `openspec validate` | Check for issues | `--all --json` for bulk validation |
| `openspec status` | See artifact progress | `--json` for structured status |
| `openspec instructions` | Get next steps | `--json` for agent instructions |
| `openspec templates` | Find template paths | `--json` for path resolution |
| `openspec schemas` | List available schemas | `--json` for schema discovery |

---

## Global Options

These options work with all commands:

| Option | Description |
|--------|-------------|
| `--version`, `-V` | Show version number |
| `--no-color` | Disable color output |
| `--help`, `-h` | Display help for command |

---

## Setup Commands

### `openspec init`

Initialize OpenSpec in your project. Creates the folder structure and configures AI tool integrations.

Default behavior uses global config defaults: profile `core`, delivery `both`, workflows `propose, explore, apply, archive`.

```
openspec init [path] [options]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `path` | No | Target directory (default: current directory) |

**Options:**

| Option | Description |
|--------|-------------|
| `--tools <list>` | Configure AI tools non-interactively. Use `all`, `none`, or comma-separated list |
| `--force` | Auto-cleanup legacy files without prompting |
| `--profile <profile>` | Override global profile for this init run (`core` or `custom`) |

`--profile custom` uses whatever workflows are currently selected in global config (`openspec config profile`).

**Supported tool IDs (`--tools`):** `amazon-q`, `antigravity`, `auggie`, `claude`, `cline`, `codex`, `codebuddy`, `continue`, `costrict`, `crush`, `cursor`, `factory`, `gemini`, `github-copilot`, `iflow`, `kilocode`, `kiro`, `opencode`, `pi`, `qoder`, `qwen`, `roocode`, `trae`, `windsurf`

**Examples:**

```bash
# Interactive initialization
openspec init

# Initialize in a specific directory
openspec init ./my-project

# Non-interactive: configure for Claude and Cursor
openspec init --tools claude,cursor

# Configure for all supported tools
openspec init --tools all

# Override profile for this run
openspec init --profile core

# Skip prompts and auto-cleanup legacy files
openspec init --force
```

**What it creates:**

```
openspec/
├── specs/              # Your specifications (source of truth)
├── changes/            # Proposed changes
└── config.yaml         # Project configuration

.claude/skills/         # Claude Code skills (if claude selected)
.cursor/skills/         # Cursor skills (if cursor selected)
.cursor/commands/       # Cursor OPSX commands (if delivery includes commands)
... (other tool configs)
```

---

### `openspec update`

Update OpenSpec instruction files after upgrading the CLI. Re-generates AI tool configuration files using your current global profile, selected workflows, and delivery mode.

```
openspec update [path] [options]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `path` | No | Target directory (default: current directory) |

**Options:**

| Option | Description |
|--------|-------------|
| `--force` | Force update even when files are up to date |

**Example:**

```bash
# Update instruction files after npm upgrade
npm update @fission-ai/openspec
openspec update
```

---

## Browsing Commands

### `openspec list`

List changes or specs in your project.

```
openspec list [options]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--specs` | List specs instead of changes |
| `--changes` | List changes (default) |
| `--sort <order>` | Sort by `recent` (default) or `name` |
| `--json` | Output as JSON |

**Examples:**

```bash
# List all active changes
openspec list

# List all specs
openspec list --specs

# JSON output for scripts
openspec list --json
```

**Output (text):**

```
Active changes:
  add-dark-mode     UI theme switching support
  fix-login-bug     Session timeout handling
```

---

### `openspec view`

Display an interactive dashboard for exploring specs and changes.

```
openspec view
```

Opens a terminal-based interface for navigating your project's specifications and changes.

---

### `openspec show`

Display details of a change or spec.

```
openspec show [item-name] [options]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `item-name` | No | Name of change or spec (prompts if omitted) |

**Options:**

| Option | Description |
|--------|-------------|
| `--type <type>` | Specify type: `change` or `spec` (auto-detected if unambiguous) |
| `--json` | Output as JSON |
| `--no-interactive` | Disable prompts |

**Change-specific options:**

| Option | Description |
|--------|-------------|
| `--deltas-only` | Show only delta specs (JSON mode) |

**Spec-specific options:**

| Option | Description |
|--------|-------------|
| `--requirements` | Show only requirements, exclude scenarios (JSON mode) |
| `--no-scenarios` | Exclude scenario content (JSON mode) |
| `-r, --requirement <id>` | Show specific requirement by 1-based index (JSON mode) |

**Examples:**

```bash
# Interactive selection
openspec show

# Show a specific change
openspec show add-dark-mode

# Show a specific spec
openspec show auth --type spec

# JSON output for parsing
openspec show add-dark-mode --json
```

---

## Validation Commands

### `openspec validate`

Validate changes and specs for structural issues.

```
openspec validate [item-name] [options]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `item-name` | No | Specific item to validate (prompts if omitted) |

**Options:**

| Option | Description |
|--------|-------------|
| `--all` | Validate all changes and specs |
| `--changes` | Validate all changes |
| `--specs` | Validate all specs |
| `--type <type>` | Specify type when name is ambiguous: `change` or `spec` |
| `--strict` | Enable strict validation mode |
| `--json` | Output as JSON |
| `--concurrency <n>` | Max parallel validations (default: 6, or `OPENSPEC_CONCURRENCY` env) |
| `--no-interactive` | Disable prompts |

**Examples:**

```bash
# Interactive validation
openspec validate

# Validate a specific change
openspec validate add-dark-mode

# Validate all changes
openspec validate --changes

# Validate everything with JSON output (for CI/scripts)
openspec validate --all --json

# Strict validation with increased parallelism
openspec validate --all --strict --concurrency 12
```

**Output (text):**

```
Validating add-dark-mode...
  ✓ proposal.md valid
  ✓ specs/ui/spec.md valid
  ⚠ design.md: missing "Technical Approach" section

1 warning found
```

**Output (JSON):**

```json
{
  "version": "1.0.0",
  "results": {
    "changes": [
      {
        "name": "add-dark-mode",
        "valid": true,
        "warnings": ["design.md: missing 'Technical Approach' section"]
      }
    ]
  },
  "summary": {
    "total": 1,
    "valid": 1,
    "invalid": 0
  }
}
```

---

## Lifecycle Commands

### `openspec archive`

Archive a completed change and merge delta specs into main specs.

```
openspec archive [change-name] [options]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | No | Change to archive (prompts if omitted) |

**Options:**

| Option | Description |
|--------|-------------|
| `-y, --yes` | Skip confirmation prompts |
| `--skip-specs` | Skip spec updates (for infrastructure/tooling/doc-only changes) |
| `--no-validate` | Skip validation (requires confirmation) |

**Examples:**

```bash
# Interactive archive
openspec archive

# Archive specific change
openspec archive add-dark-mode

# Archive without prompts (CI/scripts)
openspec archive add-dark-mode --yes

# Archive a tooling change that doesn't affect specs
openspec archive update-ci-config --skip-specs
```

**What it does:**

1. Validates the change (unless `--no-validate`)
2. Prompts for confirmation (unless `--yes`)
3. Merges delta specs into `openspec/specs/`
4. Moves change folder to `openspec/changes/archive/YYYY-MM-DD-<name>/`

---

## Workflow Commands

These commands support the artifact-driven OPSX workflow. They're useful for both humans checking progress and agents determining next steps.

### `openspec status`

Display artifact completion status for a change.

```
openspec status [options]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--change <id>` | Change name (prompts if omitted) |
| `--schema <name>` | Schema override (auto-detected from change's config) |
| `--json` | Output as JSON |

**Examples:**

```bash
# Interactive status check
openspec status

# Status for specific change
openspec status --change add-dark-mode

# JSON for agent use
openspec status --change add-dark-mode --json
```

**Output (text):**

```
Change: add-dark-mode
Schema: spec-driven
Progress: 2/4 artifacts complete

[x] proposal
[ ] design
[x] specs
[-] tasks (blocked by: design)
```

**Output (JSON):**

```json
{
  "changeName": "add-dark-mode",
  "schemaName": "spec-driven",
  "isComplete": false,
  "applyRequires": ["tasks"],
  "artifacts": [
    {"id": "proposal", "outputPath": "proposal.md", "status": "done"},
    {"id": "design", "outputPath": "design.md", "status": "ready"},
    {"id": "specs", "outputPath": "specs/**/*.md", "status": "done"},
    {"id": "tasks", "outputPath": "tasks.md", "status": "blocked", "missingDeps": ["design"]}
  ]
}
```

---

### `openspec instructions`

Get enriched instructions for creating an artifact or applying tasks. Used by AI agents to understand what to create next.

```
openspec instructions [artifact] [options]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `artifact` | No | Artifact ID: `proposal`, `specs`, `design`, `tasks`, or `apply` |

**Options:**

| Option | Description |
|--------|-------------|
| `--change <id>` | Change name (required in non-interactive mode) |
| `--schema <name>` | Schema override |
| `--json` | Output as JSON |

**Special case:** Use `apply` as the artifact to get task implementation instructions.

**Examples:**

```bash
# Get instructions for next artifact
openspec instructions --change add-dark-mode

# Get specific artifact instructions
openspec instructions design --change add-dark-mode

# Get apply/implementation instructions
openspec instructions apply --change add-dark-mode

# JSON for agent consumption
openspec instructions design --change add-dark-mode --json
```

**Output includes:**

- Template content for the artifact
- Project context from config
- Content from dependency artifacts
- Per-artifact rules from config

---

### `openspec templates`

Show resolved template paths for all artifacts in a schema.

```
openspec templates [options]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--schema <name>` | Schema to inspect (default: `spec-driven`) |
| `--json` | Output as JSON |

**Examples:**

```bash
# Show template paths for default schema
openspec templates

# Show templates for custom schema
openspec templates --schema my-workflow

# JSON for programmatic use
openspec templates --json
```

**Output (text):**

```
Schema: spec-driven

Templates:
  proposal  → ~/.openspec/schemas/spec-driven/templates/proposal.md
  specs     → ~/.openspec/schemas/spec-driven/templates/specs.md
  design    → ~/.openspec/schemas/spec-driven/templates/design.md
  tasks     → ~/.openspec/schemas/spec-driven/templates/tasks.md
```

---

### `openspec schemas`

List available workflow schemas with their descriptions and artifact flows.

```
openspec schemas [options]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--json` | Output as JSON |

**Example:**

```bash
openspec schemas
```

**Output:**

```
Available schemas:

  spec-driven (package)
    The default spec-driven development workflow
    Flow: proposal → specs → design → tasks

  my-custom (project)
    Custom workflow for this project
    Flow: research → proposal → tasks
```

---

## Schema Commands

Commands for creating and managing custom workflow schemas.

### `openspec schema init`

Create a new project-local schema.

```
openspec schema init <name> [options]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `name` | Yes | Schema name (kebab-case) |

**Options:**

| Option | Description |
|--------|-------------|
| `--description <text>` | Schema description |
| `--artifacts <list>` | Comma-separated artifact IDs (default: `proposal,specs,design,tasks`) |
| `--default` | Set as project default schema |
| `--no-default` | Don't prompt to set as default |
| `--force` | Overwrite existing schema |
| `--json` | Output as JSON |

**Examples:**

```bash
# Interactive schema creation
openspec schema init research-first

# Non-interactive with specific artifacts
openspec schema init rapid \
  --description "Rapid iteration workflow" \
  --artifacts "proposal,tasks" \
  --default
```

**What it creates:**

```
openspec/schemas/<name>/
├── schema.yaml           # Schema definition
└── templates/
    ├── proposal.md       # Template for each artifact
    ├── specs.md
    ├── design.md
    └── tasks.md
```

---

### `openspec schema fork`

Copy an existing schema to your project for customization.

```
openspec schema fork <source> [name] [options]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `source` | Yes | Schema to copy |
| `name` | No | New schema name (default: `<source>-custom`) |

**Options:**

| Option | Description |
|--------|-------------|
| `--force` | Overwrite existing destination |
| `--json` | Output as JSON |

**Example:**

```bash
# Fork the built-in spec-driven schema
openspec schema fork spec-driven my-workflow
```

---

### `openspec schema validate`

Validate a schema's structure and templates.

```
openspec schema validate [name] [options]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `name` | No | Schema to validate (validates all if omitted) |

**Options:**

| Option | Description |
|--------|-------------|
| `--verbose` | Show detailed validation steps |
| `--json` | Output as JSON |

**Example:**

```bash
# Validate a specific schema
openspec schema validate my-workflow

# Validate all schemas
openspec schema validate
```

---

### `openspec schema which`

Show where a schema resolves from (useful for debugging precedence).

```
openspec schema which [name] [options]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `name` | No | Schema name |

**Options:**

| Option | Description |
|--------|-------------|
| `--all` | List all schemas with their sources |
| `--json` | Output as JSON |

**Example:**

```bash
# Check where a schema comes from
openspec schema which spec-driven
```

**Output:**

```
spec-driven resolves from: package
  Source: /usr/local/lib/node_modules/@fission-ai/openspec/schemas/spec-driven
```

**Schema precedence:**

1. Project: `openspec/schemas/<name>/`
2. User: `~/.local/share/openspec/schemas/<name>/`
3. Package: Built-in schemas

---

## Configuration Commands

### `openspec config`

View and modify global OpenSpec configuration.

```
openspec config <subcommand> [options]
```

**Subcommands:**

| Subcommand | Description |
|------------|-------------|
| `path` | Show config file location |
| `list` | Show all current settings |
| `get <key>` | Get a specific value |
| `set <key> <value>` | Set a value |
| `unset <key>` | Remove a key |
| `reset` | Reset to defaults |
| `edit` | Open in `$EDITOR` |
| `profile [preset]` | Configure workflow profile interactively or via preset |

**Examples:**

```bash
# Show config file path
openspec config path

# List all settings
openspec config list

# Get a specific value
openspec config get telemetry.enabled

# Set a value
openspec config set telemetry.enabled false

# Set a string value explicitly
openspec config set user.name "My Name" --string

# Remove a custom setting
openspec config unset user.name

# Reset all configuration
openspec config reset --all --yes

# Edit config in your editor
openspec config edit

# Configure profile with action-based wizard
openspec config profile

# Fast preset: switch workflows to core (keeps delivery mode)
openspec config profile core
```

`openspec config profile` starts with a current-state summary, then lets you choose:
- Change delivery + workflows
- Change delivery only
- Change workflows only
- Keep current settings (exit)

If you keep current settings, no changes are written and no update prompt is shown.
If there are no config changes but the current project files are out of sync with your global profile/delivery, OpenSpec will show a warning and suggest running `openspec update`.
Pressing `Ctrl+C` also cancels the flow cleanly (no stack trace) and exits with code `130`.
In the workflow checklist, `[x]` means the workflow is selected in global config. To apply those selections to project files, run `openspec update` (or choose `Apply changes to this project now?` when prompted inside a project).

**Interactive examples:**

```bash
# Delivery-only update
openspec config profile
# choose: Change delivery only
# choose delivery: Skills only

# Workflows-only update
openspec config profile
# choose: Change workflows only
# toggle workflows in the checklist, then confirm
```

---

## Utility Commands

### `openspec feedback`

Submit feedback about OpenSpec. Creates a GitHub issue.

```
openspec feedback <message> [options]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `message` | Yes | Feedback message |

**Options:**

| Option | Description |
|--------|-------------|
| `--body <text>` | Detailed description |

**Requirements:** GitHub CLI (`gh`) must be installed and authenticated.

**Example:**

```bash
openspec feedback "Add support for custom artifact types" \
  --body "I'd like to define my own artifact types beyond the built-in ones."
```

---

### `openspec completion`

Manage shell completions for the OpenSpec CLI.

```
openspec completion <subcommand> [shell]
```

**Subcommands:**

| Subcommand | Description |
|------------|-------------|
| `generate [shell]` | Output completion script to stdout |
| `install [shell]` | Install completion for your shell |
| `uninstall [shell]` | Remove installed completions |

**Supported shells:** `bash`, `zsh`, `fish`, `powershell`

**Examples:**

```bash
# Install completions (auto-detects shell)
openspec completion install

# Install for specific shell
openspec completion install zsh

# Generate script for manual installation
openspec completion generate bash > ~/.bash_completion.d/openspec

# Uninstall
openspec completion uninstall
```

---

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | Error (validation failure, missing files, etc.) |

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENSPEC_TELEMETRY` | Set to `0` to disable telemetry |
| `DO_NOT_TRACK` | Set to `1` to disable telemetry (standard DNT signal) |
| `OPENSPEC_CONCURRENCY` | Default concurrency for bulk validation (default: 6) |
| `EDITOR` or `VISUAL` | Editor for `openspec config edit` |
| `NO_COLOR` | Disable color output when set |

---

## Related Documentation

- [Commands](commands.md) - AI slash commands (`/opsx:propose`, `/opsx:apply`, etc.)
- [Workflows](workflows.md) - Common patterns and when to use each command
- [Customization](customization.md) - Create custom schemas and templates
- [Getting Started](getting-started.md) - First-time setup guide



---

# FILE: docs/commands.md

# Commands

This is the reference for OpenSpec's slash commands. These commands are invoked in your AI coding assistant's chat interface (e.g., Claude Code, Cursor, Windsurf).

For workflow patterns and when to use each command, see [Workflows](workflows.md). For CLI commands, see [CLI](cli.md).

## Quick Reference

### Default Quick Path (`core` profile)

| Command | Purpose |
|---------|---------|
| `/opsx:propose` | Create a change and generate planning artifacts in one step |
| `/opsx:explore` | Think through ideas before committing to a change |
| `/opsx:apply` | Implement tasks from the change |
| `/opsx:archive` | Archive a completed change |

### Expanded Workflow Commands (custom workflow selection)

| Command | Purpose |
|---------|---------|
| `/opsx:new` | Start a new change scaffold |
| `/opsx:continue` | Create the next artifact based on dependencies |
| `/opsx:ff` | Fast-forward: create all planning artifacts at once |
| `/opsx:verify` | Validate implementation matches artifacts |
| `/opsx:sync` | Merge delta specs into main specs |
| `/opsx:bulk-archive` | Archive multiple changes at once |
| `/opsx:onboard` | Guided tutorial through the complete workflow |

The default global profile is `core`. To enable expanded workflow commands, run `openspec config profile`, select workflows, then run `openspec update` in your project.

---

## Command Reference

### `/opsx:propose`

Create a new change and generate planning artifacts in one step. This is the default start command in the `core` profile.

**Syntax:**
```text
/opsx:propose [change-name-or-description]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name-or-description` | No | Kebab-case name or plain-language change description |

**What it does:**
- Creates `openspec/changes/<change-name>/`
- Generates artifacts needed before implementation (for `spec-driven`: proposal, specs, design, tasks)
- Stops when the change is ready for `/opsx:apply`

**Example:**
```text
You: /opsx:propose add-dark-mode

AI:  Created openspec/changes/add-dark-mode/
     ✓ proposal.md
     ✓ specs/ui/spec.md
     ✓ design.md
     ✓ tasks.md
     Ready for implementation. Run /opsx:apply.
```

**Tips:**
- Use this for the fastest end-to-end path
- If you want step-by-step artifact control, enable expanded workflows and use `/opsx:new` + `/opsx:continue`

---

### `/opsx:explore`

Think through ideas, investigate problems, and clarify requirements before committing to a change.

**Syntax:**
```
/opsx:explore [topic]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `topic` | No | What you want to explore or investigate |

**What it does:**
- Opens an exploratory conversation with no structure required
- Investigates the codebase to answer questions
- Compares options and approaches
- Creates visual diagrams to clarify thinking
- Can transition to `/opsx:propose` (default) or `/opsx:new` (expanded workflow) when insights crystallize

**Example:**
```text
You: /opsx:explore

AI:  What would you like to explore?

You: How should we handle authentication for the mobile app?

AI:  Let me investigate your current auth setup...
     [Analyzes codebase]

     I see you're using session-based auth for the web app.
     For mobile, we have three main options:

     1. JWT tokens (stateless, works offline)
     2. OAuth2 (if you need third-party login)
     3. Extend current sessions (simpler, but requires connectivity)

     Your API already has CORS configured. Which direction interests you?

You: Let's go with JWT. Can we start a change for that?

AI:  Ready when you are. Run /opsx:propose add-jwt-auth to begin.
```

**Tips:**
- Use when requirements are unclear or you need to investigate
- No artifacts are created during exploration
- Good for comparing multiple approaches before deciding
- Can read files and search the codebase

---

### `/opsx:new`

Start a new change scaffold. Creates the change folder and waits for you to generate artifacts with `/opsx:continue` or `/opsx:ff`.

This command is part of the expanded workflow set (not included in the default `core` profile).

**Syntax:**
```
/opsx:new [change-name] [--schema <schema-name>]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | No | Name for the change folder (prompted if not provided) |
| `--schema` | No | Workflow schema to use (default: from config or `spec-driven`) |

**What it does:**
- Creates `openspec/changes/<change-name>/` directory
- Creates `.openspec.yaml` metadata file in the change folder
- Shows the first artifact template ready for creation
- Prompts for change name and schema if not provided

**What it creates:**
```
openspec/changes/<change-name>/
└── .openspec.yaml    # Change metadata (schema, created date)
```

**Example:**
```
You: /opsx:new add-dark-mode

AI:  Created openspec/changes/add-dark-mode/
     Schema: spec-driven

     Ready to create: proposal
     Use /opsx:continue to create it, or /opsx:ff to create all artifacts.
```

**Tips:**
- Use descriptive names: `add-feature`, `fix-bug`, `refactor-module`
- Avoid generic names like `update`, `changes`, `wip`
- Schema can also be set in project config (`openspec/config.yaml`)

---

### `/opsx:continue`

Create the next artifact in the dependency chain. Creates one artifact at a time for incremental progress.

**Syntax:**
```
/opsx:continue [change-name]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | No | Which change to continue (inferred from context if not provided) |

**What it does:**
- Queries the artifact dependency graph
- Shows which artifacts are ready vs blocked
- Creates the first ready artifact
- Reads dependency files for context
- Shows what becomes available after creation

**Example:**
```
You: /opsx:continue

AI:  Change: add-dark-mode

     Artifact status:
     ✓ proposal    (done)
     ◆ specs       (ready)
     ◆ design      (ready)
     ○ tasks       (blocked - needs: specs)

     Creating specs...

     [Reads proposal.md, creates specs based on requirements]

     ✓ Created openspec/changes/add-dark-mode/specs/ui/spec.md

     Now available: tasks
     Run /opsx:continue to create the next artifact.
```

**Tips:**
- Use when you want to review each artifact before proceeding
- Good for complex changes where you want control
- Multiple artifacts may become ready simultaneously
- You can edit created artifacts before continuing

---

### `/opsx:ff`

Fast-forward through artifact creation. Creates all planning artifacts at once.

**Syntax:**
```
/opsx:ff [change-name]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | No | Which change to fast-forward (inferred from context if not provided) |

**What it does:**
- Creates all artifacts in dependency order
- Tracks progress via todo list
- Stops when all `apply-required` artifacts are complete
- Reads each dependency before creating the next artifact

**Example:**
```
You: /opsx:ff add-dark-mode

AI:  Fast-forwarding add-dark-mode...

     ✓ Creating proposal.md
     ✓ Creating specs/ui/spec.md
     ✓ Creating design.md
     ✓ Creating tasks.md

     All planning artifacts complete!
     Ready for implementation. Run /opsx:apply to begin.
```

**Tips:**
- Use when you have a clear picture of what you're building
- Faster than `/opsx:continue` for straightforward changes
- You can still edit artifacts afterward
- Good for small to medium features

---

### `/opsx:apply`

Implement tasks from the change. Works through the task list, writing code and checking off items.

**Syntax:**
```
/opsx:apply [change-name]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | No | Which change to implement (inferred from context if not provided) |

**What it does:**
- Reads `tasks.md` and identifies incomplete tasks
- Works through tasks one by one
- Writes code, creates files, runs tests as needed
- Marks tasks complete with checkboxes `[x]`

**Example:**
```
You: /opsx:apply

AI:  Implementing add-dark-mode...

     Reading tasks.md:
     - [ ] 1.1 Create ThemeContext
     - [ ] 1.2 Add CSS custom properties
     - [ ] 1.3 Implement localStorage persistence

     Working on 1.1: Create ThemeContext...
     [Creates src/context/ThemeContext.tsx]

     ✓ 1.1 Complete

     Working on 1.2: Add CSS custom properties...
     [Updates src/styles/globals.css]

     ✓ 1.2 Complete
     ...
```

**Tips:**
- Can resume where you left off if interrupted
- Use for parallel changes by specifying the change name
- Completion state is tracked in `tasks.md` checkboxes

---

### `/opsx:verify`

Validate that implementation matches your change artifacts. Checks completeness, correctness, and coherence.

**Syntax:**
```
/opsx:verify [change-name]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | No | Which change to verify (inferred from context if not provided) |

**What it does:**
- Checks three dimensions of implementation quality
- Searches codebase for implementation evidence
- Reports issues categorized as CRITICAL, WARNING, or SUGGESTION
- Does not block archive, but surfaces issues

**Verification dimensions:**

| Dimension | What it validates |
|-----------|-------------------|
| **Completeness** | All tasks done, all requirements implemented, scenarios covered |
| **Correctness** | Implementation matches spec intent, edge cases handled |
| **Coherence** | Design decisions reflected in code, patterns consistent |

**Example:**
```
You: /opsx:verify

AI:  Verifying add-dark-mode...

     COMPLETENESS
     ✓ All 8 tasks in tasks.md are checked
     ✓ All requirements in specs have corresponding code
     ⚠ Scenario "System preference detection" has no test coverage

     CORRECTNESS
     ✓ Implementation matches spec intent
     ✓ Edge cases from scenarios are handled
     ✓ Error states match spec definitions

     COHERENCE
     ✓ Design decisions reflected in code structure
     ✓ Naming conventions consistent with design.md
     ⚠ Design mentions "CSS variables" but implementation uses Tailwind classes

     SUMMARY
     ─────────────────────────────
     Critical issues: 0
     Warnings: 2
     Ready to archive: Yes (with warnings)

     Recommendations:
     1. Add test for system preference detection
     2. Update design.md to reflect Tailwind usage, or refactor to use CSS variables
```

**Tips:**
- Run before archiving to catch mismatches early
- Warnings don't block archive but indicate potential issues
- Good for reviewing AI's work before committing
- Can reveal drift between artifacts and implementation

---

### `/opsx:sync`

**Optional command.** Merge delta specs from a change into main specs. Archive will prompt to sync if needed, so you typically don't need to run this manually.

**Syntax:**
```
/opsx:sync [change-name]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | No | Which change to sync (inferred from context if not provided) |

**What it does:**
- Reads delta specs from change folder
- Parses ADDED/MODIFIED/REMOVED/RENAMED sections
- Merges changes into main `openspec/specs/` directory
- Preserves existing content not mentioned in delta
- Does not archive the change (remains active)

**Example:**
```text
You: /opsx:sync

AI:  Syncing add-dark-mode delta specs...

     Reading: openspec/changes/add-dark-mode/specs/ui/spec.md
     Target:  openspec/specs/ui/spec.md

     Changes to apply:
     ✓ ADDED: Theme Selection requirement (2 scenarios)
     ✓ ADDED: Accessibility requirement (1 scenario)

     Merging...
     ✓ openspec/specs/ui/spec.md updated

     Change remains active. Run /opsx:archive when ready to complete.
```

**When to use manually:**

| Scenario | Use sync? |
|----------|-----------|
| Long-running change, want specs in main before archiving | Yes |
| Multiple parallel changes need the updated base specs | Yes |
| Want to preview/review the merge separately | Yes |
| Quick change, going straight to archive | No (archive handles it) |

**Tips:**
- Sync is intelligent, not copy-paste
- Can add scenarios to existing requirements without duplicating
- Change stays active after sync (not archived)
- Most users will never need to call this directly—archive prompts if needed

---

### `/opsx:archive`

Archive a completed change. Finalizes the change and moves it to the archive folder.

**Syntax:**
```
/opsx:archive [change-name]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | No | Which change to archive (inferred from context if not provided) |

**What it does:**
- Checks artifact completion status
- Checks task completion (warns if incomplete)
- Offers to sync delta specs if not already synced
- Moves change folder to `openspec/changes/archive/YYYY-MM-DD-<name>/`
- Preserves all artifacts for audit trail

**Example:**
```text
You: /opsx:archive

AI:  Archiving add-dark-mode...

     Artifact status:
     ✓ proposal.md exists
     ✓ specs/ exists
     ✓ design.md exists
     ✓ tasks.md exists (8/8 tasks complete)

     Delta specs: Not yet synced
     → Sync now? (recommended)

You: Yes

AI:  ✓ Synced specs to openspec/specs/ui/spec.md
     ✓ Moved to openspec/changes/archive/2025-01-24-add-dark-mode/

     Change archived successfully.
```

**Tips:**
- Archive won't block on incomplete tasks, but will warn
- Delta specs can be synced during archive or beforehand
- Archived changes are preserved for history
- Use `/opsx:verify` first to catch issues

---

### `/opsx:bulk-archive`

Archive multiple completed changes at once. Handles spec conflicts between changes.

**Syntax:**
```
/opsx:bulk-archive [change-names...]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-names` | No | Specific changes to archive (prompts to select if not provided) |

**What it does:**
- Lists all completed changes
- Validates each change before archiving
- Detects spec conflicts across changes
- Resolves conflicts by checking what's actually implemented
- Archives in chronological order

**Example:**
```
You: /opsx:bulk-archive

AI:  Found 3 completed changes:
     - add-dark-mode (8/8 tasks complete)
     - fix-login-bug (3/3 tasks complete)
     - update-footer (2/2 tasks complete)

     Checking for spec conflicts...
     ⚠ add-dark-mode and update-footer both touch specs/ui/

     Inspecting codebase to resolve...
     Both changes are implemented. Will merge in chronological order:
     1. add-dark-mode (created Jan 20)
     2. update-footer (created Jan 22)

     Archive all 3 changes?

You: Yes

AI:  ✓ Archived add-dark-mode
     ✓ Archived fix-login-bug
     ✓ Archived update-footer
     Specs merged: add-dark-mode → update-footer
```

**Tips:**
- Good for parallel work streams
- Conflict resolution is agentic (checks codebase)
- Changes are archived in order of creation
- Prompts before overwriting spec content

---

### `/opsx:onboard`

Guided onboarding through the complete OpenSpec workflow. An interactive tutorial using your actual codebase.

**Syntax:**
```
/opsx:onboard
```

**What it does:**
- Walks through a complete workflow cycle with narration
- Scans your codebase for real improvement opportunities
- Creates an actual change with real artifacts
- Implements actual work (small, safe changes)
- Archives the completed change
- Explains each step as it happens

**Phases:**
1. Welcome and codebase analysis
2. Finding an improvement opportunity
3. Creating a change (`/opsx:new`)
4. Writing the proposal
5. Creating specs
6. Writing the design
7. Creating tasks
8. Implementing tasks (`/opsx:apply`)
9. Verifying implementation
10. Archiving the change
11. Summary and next steps

**Example:**
```
You: /opsx:onboard

AI:  Welcome to OpenSpec!

     I'll walk you through the complete workflow using your actual codebase.
     We'll find something small to improve, create a proper change for it,
     implement it, and archive it.

     Let me scan your codebase for opportunities...

     [Analyzes codebase]

     I found a few things we could work on:
     1. Add input validation to the contact form
     2. Improve error messages in the auth flow
     3. Add loading states to async buttons

     Which interests you? (or suggest something else)
```

**Tips:**
- Best for new users learning the workflow
- Uses real code, not toy examples
- Creates a real change you can keep or discard
- Takes 15-30 minutes to complete

---

## Command Syntax by AI Tool

Different AI tools use slightly different command syntax. Use the format that matches your tool:

| Tool | Syntax Example |
|------|----------------|
| Claude Code | `/opsx:propose`, `/opsx:apply` |
| Cursor | `/opsx-propose`, `/opsx-apply` |
| Windsurf | `/opsx-propose`, `/opsx-apply` |
| Copilot (IDE) | `/opsx-propose`, `/opsx-apply` |
| Trae | Skill-based invocations such as `/openspec-propose`, `/openspec-apply-change` (no generated `opsx-*` command files) |

The intent is the same across tools, but how commands are surfaced can differ by integration.

> **Note:** GitHub Copilot commands (`.github/prompts/*.prompt.md`) are only available in IDE extensions (VS Code, JetBrains, Visual Studio). GitHub Copilot CLI does not currently support custom prompt files — see [Supported Tools](supported-tools.md) for details and workarounds.

---

## Legacy Commands

These commands use the older "all-at-once" workflow. They still work but OPSX commands are recommended.

| Command | What it does |
|---------|--------------|
| `/openspec:proposal` | Create all artifacts at once (proposal, specs, design, tasks) |
| `/openspec:apply` | Implement the change |
| `/openspec:archive` | Archive the change |

**When to use legacy commands:**
- Existing projects using the old workflow
- Simple changes where you don't need incremental artifact creation
- Preference for the all-or-nothing approach

**Migrating to OPSX:**
Legacy changes can be continued with OPSX commands. The artifact structure is compatible.

---

## Troubleshooting

### "Change not found"

The command couldn't identify which change to work on.

**Solutions:**
- Specify the change name explicitly: `/opsx:apply add-dark-mode`
- Check that the change folder exists: `openspec list`
- Verify you're in the right project directory

### "No artifacts ready"

All artifacts are either complete or blocked by missing dependencies.

**Solutions:**
- Run `openspec status --change <name>` to see what's blocking
- Check if required artifacts exist
- Create missing dependency artifacts first

### "Schema not found"

The specified schema doesn't exist.

**Solutions:**
- List available schemas: `openspec schemas`
- Check spelling of schema name
- Create the schema if it's custom: `openspec schema init <name>`

### Commands not recognized

The AI tool doesn't recognize OpenSpec commands.

**Solutions:**
- Ensure OpenSpec is initialized: `openspec init`
- Regenerate skills: `openspec update`
- Check that `.claude/skills/` directory exists (for Claude Code)
- Restart your AI tool to pick up new skills

### Artifacts not generating properly

The AI creates incomplete or incorrect artifacts.

**Solutions:**
- Add project context in `openspec/config.yaml`
- Add per-artifact rules for specific guidance
- Provide more detail in your change description
- Use `/opsx:continue` instead of `/opsx:ff` for more control

---

## Next Steps

- [Workflows](workflows.md) - Common patterns and when to use each command
- [CLI](cli.md) - Terminal commands for management and validation
- [Customization](customization.md) - Create custom schemas and workflows



---

# FILE: docs/concepts.md

# Concepts

This guide explains the core ideas behind OpenSpec and how they fit together. For practical usage, see [Getting Started](getting-started.md) and [Workflows](workflows.md).

## Philosophy

OpenSpec is built around four principles:

```
fluid not rigid         — no phase gates, work on what makes sense
iterative not waterfall — learn as you build, refine as you go
easy not complex        — lightweight setup, minimal ceremony
brownfield-first        — works with existing codebases, not just greenfield
```

### Why These Principles Matter

**Fluid not rigid.** Traditional spec systems lock you into phases: first you plan, then you implement, then you're done. OpenSpec is more flexible — you can create artifacts in any order that makes sense for your work.

**Iterative not waterfall.** Requirements change. Understanding deepens. What seemed like a good approach at the start might not hold up after you see the codebase. OpenSpec embraces this reality.

**Easy not complex.** Some spec frameworks require extensive setup, rigid formats, or heavyweight processes. OpenSpec stays out of your way. Initialize in seconds, start working immediately, customize only if you need to.

**Brownfield-first.** Most software work isn't building from scratch — it's modifying existing systems. OpenSpec's delta-based approach makes it easy to specify changes to existing behavior, not just describe new systems.

## The Big Picture

OpenSpec organizes your work into two main areas:

```
┌────────────────────────────────────────────────────────────────────┐
│                        openspec/                                   │
│                                                                    │
│   ┌─────────────────────┐      ┌───────────────────────────────┐   │
│   │       specs/        │      │         changes/              │   │
│   │                     │      │                               │   │
│   │  Source of truth    │◄─────│  Proposed modifications       │   │
│   │  How your system    │ merge│  Each change = one folder     │   │
│   │  currently works    │      │  Contains artifacts + deltas  │   │
│   │                     │      │                               │   │
│   └─────────────────────┘      └───────────────────────────────┘   │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

**Specs** are the source of truth — they describe how your system currently behaves.

**Changes** are proposed modifications — they live in separate folders until you're ready to merge them.

This separation is key. You can work on multiple changes in parallel without conflicts. You can review a change before it affects the main specs. And when you archive a change, its deltas merge cleanly into the source of truth.

## Specs

Specs describe your system's behavior using structured requirements and scenarios.

### Structure

```
openspec/specs/
├── auth/
│   └── spec.md           # Authentication behavior
├── payments/
│   └── spec.md           # Payment processing
├── notifications/
│   └── spec.md           # Notification system
└── ui/
    └── spec.md           # UI behavior and themes
```

Organize specs by domain — logical groupings that make sense for your system. Common patterns:

- **By feature area**: `auth/`, `payments/`, `search/`
- **By component**: `api/`, `frontend/`, `workers/`
- **By bounded context**: `ordering/`, `fulfillment/`, `inventory/`

### Spec Format

A spec contains requirements, and each requirement has scenarios:

```markdown
# Auth Specification

## Purpose
Authentication and session management for the application.

## Requirements

### Requirement: User Authentication
The system SHALL issue a JWT token upon successful login.

#### Scenario: Valid credentials
- GIVEN a user with valid credentials
- WHEN the user submits login form
- THEN a JWT token is returned
- AND the user is redirected to dashboard

#### Scenario: Invalid credentials
- GIVEN invalid credentials
- WHEN the user submits login form
- THEN an error message is displayed
- AND no token is issued

### Requirement: Session Expiration
The system MUST expire sessions after 30 minutes of inactivity.

#### Scenario: Idle timeout
- GIVEN an authenticated session
- WHEN 30 minutes pass without activity
- THEN the session is invalidated
- AND the user must re-authenticate
```

**Key elements:**

| Element | Purpose |
|---------|---------|
| `## Purpose` | High-level description of this spec's domain |
| `### Requirement:` | A specific behavior the system must have |
| `#### Scenario:` | A concrete example of the requirement in action |
| SHALL/MUST/SHOULD | RFC 2119 keywords indicating requirement strength |

### Why Structure Specs This Way

**Requirements are the "what"** — they state what the system should do without specifying implementation.

**Scenarios are the "when"** — they provide concrete examples that can be verified. Good scenarios:
- Are testable (you could write an automated test for them)
- Cover both happy path and edge cases
- Use Given/When/Then or similar structured format

**RFC 2119 keywords** (SHALL, MUST, SHOULD, MAY) communicate intent:
- **MUST/SHALL** — absolute requirement
- **SHOULD** — recommended, but exceptions exist
- **MAY** — optional

### What a Spec Is (and Is Not)

A spec is a **behavior contract**, not an implementation plan.

Good spec content:
- Observable behavior users or downstream systems rely on
- Inputs, outputs, and error conditions
- External constraints (security, privacy, reliability, compatibility)
- Scenarios that can be tested or explicitly validated

Avoid in specs:
- Internal class/function names
- Library or framework choices
- Step-by-step implementation details
- Detailed execution plans (those belong in `design.md` or `tasks.md`)

Quick test:
- If implementation can change without changing externally visible behavior, it likely does not belong in the spec.

### Keep It Lightweight: Progressive Rigor

OpenSpec aims to avoid bureaucracy. Use the lightest level that still makes the change verifiable.

**Lite spec (default):**
- Short behavior-first requirements
- Clear scope and non-goals
- A few concrete acceptance checks

**Full spec (for higher risk):**
- Cross-team or cross-repo changes
- API/contract changes, migrations, security/privacy concerns
- Changes where ambiguity is likely to cause expensive rework

Most changes should stay in Lite mode.

### Human + Agent Collaboration

In many teams, humans explore and agents draft artifacts. The intended loop is:

1. Human provides intent, context, and constraints.
2. Agent converts this into behavior-first requirements and scenarios.
3. Agent keeps implementation detail in `design.md` and `tasks.md`, not `spec.md`.
4. Validation confirms structure and clarity before implementation.

This keeps specs readable for humans and consistent for agents.

## Changes

A change is a proposed modification to your system, packaged as a folder with everything needed to understand and implement it.

### Change Structure

```
openspec/changes/add-dark-mode/
├── proposal.md           # Why and what
├── design.md             # How (technical approach)
├── tasks.md              # Implementation checklist
├── .openspec.yaml        # Change metadata (optional)
└── specs/                # Delta specs
    └── ui/
        └── spec.md       # What's changing in ui/spec.md
```

Each change is self-contained. It has:
- **Artifacts** — documents that capture intent, design, and tasks
- **Delta specs** — specifications for what's being added, modified, or removed
- **Metadata** — optional configuration for this specific change

### Why Changes Are Folders

Packaging a change as a folder has several benefits:

1. **Everything together.** Proposal, design, tasks, and specs live in one place. No hunting through different locations.

2. **Parallel work.** Multiple changes can exist simultaneously without conflicting. Work on `add-dark-mode` while `fix-auth-bug` is also in progress.

3. **Clean history.** When archived, changes move to `changes/archive/` with their full context preserved. You can look back and understand not just what changed, but why.

4. **Review-friendly.** A change folder is easy to review — open it, read the proposal, check the design, see the spec deltas.

## Artifacts

Artifacts are the documents within a change that guide the work.

### The Artifact Flow

```
proposal ──────► specs ──────► design ──────► tasks ──────► implement
    │               │             │              │
   why            what           how          steps
 + scope        changes       approach      to take
```

Artifacts build on each other. Each artifact provides context for the next.

### Artifact Types

#### Proposal (`proposal.md`)

The proposal captures **intent**, **scope**, and **approach** at a high level.

```markdown
# Proposal: Add Dark Mode

## Intent
Users have requested a dark mode option to reduce eye strain
during nighttime usage and match system preferences.

## Scope
In scope:
- Theme toggle in settings
- System preference detection
- Persist preference in localStorage

Out of scope:
- Custom color themes (future work)
- Per-page theme overrides

## Approach
Use CSS custom properties for theming with a React context
for state management. Detect system preference on first load,
allow manual override.
```

**When to update the proposal:**
- Scope changes (narrowing or expanding)
- Intent clarifies (better understanding of the problem)
- Approach fundamentally shifts

#### Specs (delta specs in `specs/`)

Delta specs describe **what's changing** relative to the current specs. See [Delta Specs](#delta-specs) below.

#### Design (`design.md`)

The design captures **technical approach** and **architecture decisions**.

````markdown
# Design: Add Dark Mode

## Technical Approach
Theme state managed via React Context to avoid prop drilling.
CSS custom properties enable runtime switching without class toggling.

## Architecture Decisions

### Decision: Context over Redux
Using React Context for theme state because:
- Simple binary state (light/dark)
- No complex state transitions
- Avoids adding Redux dependency

### Decision: CSS Custom Properties
Using CSS variables instead of CSS-in-JS because:
- Works with existing stylesheet
- No runtime overhead
- Browser-native solution

## Data Flow
```
ThemeProvider (context)
       │
       ▼
ThemeToggle ◄──► localStorage
       │
       ▼
CSS Variables (applied to :root)
```

## File Changes
- `src/contexts/ThemeContext.tsx` (new)
- `src/components/ThemeToggle.tsx` (new)
- `src/styles/globals.css` (modified)
````

**When to update the design:**
- Implementation reveals the approach won't work
- Better solution discovered
- Dependencies or constraints change

#### Tasks (`tasks.md`)

Tasks are the **implementation checklist** — concrete steps with checkboxes.

```markdown
# Tasks

## 1. Theme Infrastructure
- [ ] 1.1 Create ThemeContext with light/dark state
- [ ] 1.2 Add CSS custom properties for colors
- [ ] 1.3 Implement localStorage persistence
- [ ] 1.4 Add system preference detection

## 2. UI Components
- [ ] 2.1 Create ThemeToggle component
- [ ] 2.2 Add toggle to settings page
- [ ] 2.3 Update Header to include quick toggle

## 3. Styling
- [ ] 3.1 Define dark theme color palette
- [ ] 3.2 Update components to use CSS variables
- [ ] 3.3 Test contrast ratios for accessibility
```

**Task best practices:**
- Group related tasks under headings
- Use hierarchical numbering (1.1, 1.2, etc.)
- Keep tasks small enough to complete in one session
- Check tasks off as you complete them

## Delta Specs

Delta specs are the key concept that makes OpenSpec work for brownfield development. They describe **what's changing** rather than restating the entire spec.

### The Format

```markdown
# Delta for Auth

## ADDED Requirements

### Requirement: Two-Factor Authentication
The system MUST support TOTP-based two-factor authentication.

#### Scenario: 2FA enrollment
- GIVEN a user without 2FA enabled
- WHEN the user enables 2FA in settings
- THEN a QR code is displayed for authenticator app setup
- AND the user must verify with a code before activation

#### Scenario: 2FA login
- GIVEN a user with 2FA enabled
- WHEN the user submits valid credentials
- THEN an OTP challenge is presented
- AND login completes only after valid OTP

## MODIFIED Requirements

### Requirement: Session Expiration
The system MUST expire sessions after 15 minutes of inactivity.
(Previously: 30 minutes)

#### Scenario: Idle timeout
- GIVEN an authenticated session
- WHEN 15 minutes pass without activity
- THEN the session is invalidated

## REMOVED Requirements

### Requirement: Remember Me
(Deprecated in favor of 2FA. Users should re-authenticate each session.)
```

### Delta Sections

| Section | Meaning | What Happens on Archive |
|---------|---------|------------------------|
| `## ADDED Requirements` | New behavior | Appended to main spec |
| `## MODIFIED Requirements` | Changed behavior | Replaces existing requirement |
| `## REMOVED Requirements` | Deprecated behavior | Deleted from main spec |

### Why Deltas Instead of Full Specs

**Clarity.** A delta shows exactly what's changing. Reading a full spec, you'd have to diff it mentally against the current version.

**Conflict avoidance.** Two changes can touch the same spec file without conflicting, as long as they modify different requirements.

**Review efficiency.** Reviewers see the change, not the unchanged context. Focus on what matters.

**Brownfield fit.** Most work modifies existing behavior. Deltas make modifications first-class, not an afterthought.

## Schemas

Schemas define the artifact types and their dependencies for a workflow.

### How Schemas Work

```yaml
# openspec/schemas/spec-driven/schema.yaml
name: spec-driven
artifacts:
  - id: proposal
    generates: proposal.md
    requires: []              # No dependencies, can create first

  - id: specs
    generates: specs/**/*.md
    requires: [proposal]      # Needs proposal before creating

  - id: design
    generates: design.md
    requires: [proposal]      # Can create in parallel with specs

  - id: tasks
    generates: tasks.md
    requires: [specs, design] # Needs both specs and design first
```

**Artifacts form a dependency graph:**

```
                    proposal
                   (root node)
                       │
         ┌─────────────┴─────────────┐
         │                           │
         ▼                           ▼
      specs                       design
   (requires:                  (requires:
    proposal)                   proposal)
         │                           │
         └─────────────┬─────────────┘
                       │
                       ▼
                    tasks
                (requires:
                specs, design)
```

**Dependencies are enablers, not gates.** They show what's possible to create, not what you must create next. You can skip design if you don't need it. You can create specs before or after design — both depend only on proposal.

### Built-in Schemas

**spec-driven** (default)

The standard workflow for spec-driven development:

```
proposal → specs → design → tasks → implement
```

Best for: Most feature work where you want to agree on specs before implementation.

### Custom Schemas

Create custom schemas for your team's workflow:

```bash
# Create from scratch
openspec schema init research-first

# Or fork an existing one
openspec schema fork spec-driven research-first
```

**Example custom schema:**

```yaml
# openspec/schemas/research-first/schema.yaml
name: research-first
artifacts:
  - id: research
    generates: research.md
    requires: []           # Do research first

  - id: proposal
    generates: proposal.md
    requires: [research]   # Proposal informed by research

  - id: tasks
    generates: tasks.md
    requires: [proposal]   # Skip specs/design, go straight to tasks
```

See [Customization](customization.md) for full details on creating and using custom schemas.

## Archive

Archiving completes a change by merging its delta specs into the main specs and preserving the change for history.

### What Happens When You Archive

```
Before archive:

openspec/
├── specs/
│   └── auth/
│       └── spec.md ◄────────────────┐
└── changes/                         │
    └── add-2fa/                     │
        ├── proposal.md              │
        ├── design.md                │ merge
        ├── tasks.md                 │
        └── specs/                   │
            └── auth/                │
                └── spec.md ─────────┘


After archive:

openspec/
├── specs/
│   └── auth/
│       └── spec.md        # Now includes 2FA requirements
└── changes/
    └── archive/
        └── 2025-01-24-add-2fa/    # Preserved for history
            ├── proposal.md
            ├── design.md
            ├── tasks.md
            └── specs/
                └── auth/
                    └── spec.md
```

### The Archive Process

1. **Merge deltas.** Each delta spec section (ADDED/MODIFIED/REMOVED) is applied to the corresponding main spec.

2. **Move to archive.** The change folder moves to `changes/archive/` with a date prefix for chronological ordering.

3. **Preserve context.** All artifacts remain intact in the archive. You can always look back to understand why a change was made.

### Why Archive Matters

**Clean state.** Active changes (`changes/`) shows only work in progress. Completed work moves out of the way.

**Audit trail.** The archive preserves the full context of every change — not just what changed, but the proposal explaining why, the design explaining how, and the tasks showing the work done.

**Spec evolution.** Specs grow organically as changes are archived. Each archive merges its deltas, building up a comprehensive specification over time.

## How It All Fits Together

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                              OPENSPEC FLOW                                   │
│                                                                              │
│   ┌────────────────┐                                                         │
│   │  1. START      │  /opsx:propose (core) or /opsx:new (expanded)           │
│   │     CHANGE     │                                                         │
│   └───────┬────────┘                                                         │
│           │                                                                  │
│           ▼                                                                  │
│   ┌────────────────┐                                                         │
│   │  2. CREATE     │  /opsx:ff or /opsx:continue (expanded workflow)         │
│   │     ARTIFACTS  │  Creates proposal → specs → design → tasks              │
│   │                │  (based on schema dependencies)                         │
│   └───────┬────────┘                                                         │
│           │                                                                  │
│           ▼                                                                  │
│   ┌────────────────┐                                                         │
│   │  3. IMPLEMENT  │  /opsx:apply                                            │
│   │     TASKS      │  Work through tasks, checking them off                  │
│   │                │◄──── Update artifacts as you learn                      │
│   └───────┬────────┘                                                         │
│           │                                                                  │
│           ▼                                                                  │
│   ┌────────────────┐                                                         │
│   │  4. VERIFY     │  /opsx:verify (optional)                                │
│   │     WORK       │  Check implementation matches specs                     │
│   └───────┬────────┘                                                         │
│           │                                                                  │
│           ▼                                                                  │
│   ┌────────────────┐     ┌──────────────────────────────────────────────┐    │
│   │  5. ARCHIVE    │────►│  Delta specs merge into main specs           │    │
│   │     CHANGE     │     │  Change folder moves to archive/             │    │
│   └────────────────┘     │  Specs are now the updated source of truth   │    │
│                          └──────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**The virtuous cycle:**

1. Specs describe current behavior
2. Changes propose modifications (as deltas)
3. Implementation makes the changes real
4. Archive merges deltas into specs
5. Specs now describe the new behavior
6. Next change builds on updated specs

## Glossary

| Term | Definition |
|------|------------|
| **Artifact** | A document within a change (proposal, design, tasks, or delta specs) |
| **Archive** | The process of completing a change and merging its deltas into main specs |
| **Change** | A proposed modification to the system, packaged as a folder with artifacts |
| **Delta spec** | A spec that describes changes (ADDED/MODIFIED/REMOVED) relative to current specs |
| **Domain** | A logical grouping for specs (e.g., `auth/`, `payments/`) |
| **Requirement** | A specific behavior the system must have |
| **Scenario** | A concrete example of a requirement, typically in Given/When/Then format |
| **Schema** | A definition of artifact types and their dependencies |
| **Spec** | A specification describing system behavior, containing requirements and scenarios |
| **Source of truth** | The `openspec/specs/` directory, containing the current agreed-upon behavior |

## Next Steps

- [Getting Started](getting-started.md) - Practical first steps
- [Workflows](workflows.md) - Common patterns and when to use each
- [Commands](commands.md) - Full command reference
- [Customization](customization.md) - Create custom schemas and configure your project



---

# FILE: docs/customization.md

# Customization

OpenSpec provides three levels of customization:

| Level | What it does | Best for |
|-------|--------------|----------|
| **Project Config** | Set defaults, inject context/rules | Most teams |
| **Custom Schemas** | Define your own workflow artifacts | Teams with unique processes |
| **Global Overrides** | Share schemas across all projects | Power users |

---

## Project Configuration

The `openspec/config.yaml` file is the easiest way to customize OpenSpec for your team. It lets you:

- **Set a default schema** - Skip `--schema` on every command
- **Inject project context** - AI sees your tech stack, conventions, etc.
- **Add per-artifact rules** - Custom rules for specific artifacts

### Quick Setup

```bash
openspec init
```

This walks you through creating a config interactively. Or create one manually:

```yaml
# openspec/config.yaml
schema: spec-driven

context: |
  Tech stack: TypeScript, React, Node.js, PostgreSQL
  API style: RESTful, documented in docs/api.md
  Testing: Jest + React Testing Library
  We value backwards compatibility for all public APIs

rules:
  proposal:
    - Include rollback plan
    - Identify affected teams
  specs:
    - Use Given/When/Then format
    - Reference existing patterns before inventing new ones
```

### How It Works

**Default schema:**

```bash
# Without config
openspec new change my-feature --schema spec-driven

# With config - schema is automatic
openspec new change my-feature
```

**Context and rules injection:**

When generating any artifact, your context and rules are injected into the AI prompt:

```xml
<context>
Tech stack: TypeScript, React, Node.js, PostgreSQL
...
</context>

<rules>
- Include rollback plan
- Identify affected teams
</rules>

<template>
[Schema's built-in template]
</template>
```

- **Context** appears in ALL artifacts
- **Rules** ONLY appear for the matching artifact

### Schema Resolution Order

When OpenSpec needs a schema, it checks in this order:

1. CLI flag: `--schema <name>`
2. Change metadata (`.openspec.yaml` in the change folder)
3. Project config (`openspec/config.yaml`)
4. Default (`spec-driven`)

---

## Custom Schemas

When project config isn't enough, create your own schema with a completely custom workflow. Custom schemas live in your project's `openspec/schemas/` directory and are version-controlled with your code.

```text
your-project/
├── openspec/
│   ├── config.yaml        # Project config
│   ├── schemas/           # Custom schemas live here
│   │   └── my-workflow/
│   │       ├── schema.yaml
│   │       └── templates/
│   └── changes/           # Your changes
└── src/
```

### Fork an Existing Schema

The fastest way to customize is to fork a built-in schema:

```bash
openspec schema fork spec-driven my-workflow
```

This copies the entire `spec-driven` schema to `openspec/schemas/my-workflow/` where you can edit it freely.

**What you get:**

```text
openspec/schemas/my-workflow/
├── schema.yaml           # Workflow definition
└── templates/
    ├── proposal.md       # Template for proposal artifact
    ├── spec.md           # Template for specs
    ├── design.md         # Template for design
    └── tasks.md          # Template for tasks
```

Now edit `schema.yaml` to change the workflow, or edit templates to change what AI generates.

### Create a Schema from Scratch

For a completely fresh workflow:

```bash
# Interactive
openspec schema init research-first

# Non-interactive
openspec schema init rapid \
  --description "Rapid iteration workflow" \
  --artifacts "proposal,tasks" \
  --default
```

### Schema Structure

A schema defines the artifacts in your workflow and how they depend on each other:

```yaml
# openspec/schemas/my-workflow/schema.yaml
name: my-workflow
version: 1
description: My team's custom workflow

artifacts:
  - id: proposal
    generates: proposal.md
    description: Initial proposal document
    template: proposal.md
    instruction: |
      Create a proposal that explains WHY this change is needed.
      Focus on the problem, not the solution.
    requires: []

  - id: design
    generates: design.md
    description: Technical design
    template: design.md
    instruction: |
      Create a design document explaining HOW to implement.
    requires:
      - proposal    # Can't create design until proposal exists

  - id: tasks
    generates: tasks.md
    description: Implementation checklist
    template: tasks.md
    requires:
      - design

apply:
  requires: [tasks]
  tracks: tasks.md
```

**Key fields:**

| Field | Purpose |
|-------|---------|
| `id` | Unique identifier, used in commands and rules |
| `generates` | Output filename (supports globs like `specs/**/*.md`) |
| `template` | Template file in `templates/` directory |
| `instruction` | AI instructions for creating this artifact |
| `requires` | Dependencies - which artifacts must exist first |

### Templates

Templates are markdown files that guide the AI. They're injected into the prompt when creating that artifact.

```markdown
<!-- templates/proposal.md -->
## Why

<!-- Explain the motivation for this change. What problem does this solve? -->

## What Changes

<!-- Describe what will change. Be specific about new capabilities or modifications. -->

## Impact

<!-- Affected code, APIs, dependencies, systems -->
```

Templates can include:
- Section headers the AI should fill in
- HTML comments with guidance for the AI
- Example formats showing expected structure

### Validate Your Schema

Before using a custom schema, validate it:

```bash
openspec schema validate my-workflow
```

This checks:
- `schema.yaml` syntax is correct
- All referenced templates exist
- No circular dependencies
- Artifact IDs are valid

### Use Your Custom Schema

Once created, use your schema with:

```bash
# Specify on command
openspec new change feature --schema my-workflow

# Or set as default in config.yaml
schema: my-workflow
```

### Debug Schema Resolution

Not sure which schema is being used? Check with:

```bash
# See where a specific schema resolves from
openspec schema which my-workflow

# List all available schemas
openspec schema which --all
```

Output shows whether it's from your project, user directory, or the package:

```text
Schema: my-workflow
Source: project
Path: /path/to/project/openspec/schemas/my-workflow
```

---

> **Note:** OpenSpec also supports user-level schemas at `~/.local/share/openspec/schemas/` for sharing across projects, but project-level schemas in `openspec/schemas/` are recommended since they're version-controlled with your code.

---

## Examples

### Rapid Iteration Workflow

A minimal workflow for quick iterations:

```yaml
# openspec/schemas/rapid/schema.yaml
name: rapid
version: 1
description: Fast iteration with minimal overhead

artifacts:
  - id: proposal
    generates: proposal.md
    description: Quick proposal
    template: proposal.md
    instruction: |
      Create a brief proposal for this change.
      Focus on what and why, skip detailed specs.
    requires: []

  - id: tasks
    generates: tasks.md
    description: Implementation checklist
    template: tasks.md
    requires: [proposal]

apply:
  requires: [tasks]
  tracks: tasks.md
```

### Adding a Review Artifact

Fork the default and add a review step:

```bash
openspec schema fork spec-driven with-review
```

Then edit `schema.yaml` to add:

```yaml
  - id: review
    generates: review.md
    description: Pre-implementation review checklist
    template: review.md
    instruction: |
      Create a review checklist based on the design.
      Include security, performance, and testing considerations.
    requires:
      - design

  - id: tasks
    # ... existing tasks config ...
    requires:
      - specs
      - design
      - review    # Now tasks require review too
```

---

## See Also

- [CLI Reference: Schema Commands](cli.md#schema-commands) - Full command documentation



---

# FILE: docs/getting-started.md

# Getting Started

This guide explains how OpenSpec works after you've installed and initialized it. For installation instructions, see the [main README](../README.md#quick-start).

## How It Works

OpenSpec helps you and your AI coding assistant agree on what to build before any code is written.

**Default quick path (core profile):**

```text
/opsx:propose ──► /opsx:apply ──► /opsx:archive
```

**Expanded path (custom workflow selection):**

```text
/opsx:new ──► /opsx:ff or /opsx:continue ──► /opsx:apply ──► /opsx:verify ──► /opsx:archive
```

The default global profile is `core`, which includes `propose`, `explore`, `apply`, and `archive`. You can enable the expanded workflow commands with `openspec config profile` and then `openspec update`.

## What OpenSpec Creates

After running `openspec init`, your project has this structure:

```
openspec/
├── specs/              # Source of truth (your system's behavior)
│   └── <domain>/
│       └── spec.md
├── changes/            # Proposed updates (one folder per change)
│   └── <change-name>/
│       ├── proposal.md
│       ├── design.md
│       ├── tasks.md
│       └── specs/      # Delta specs (what's changing)
│           └── <domain>/
│               └── spec.md
└── config.yaml         # Project configuration (optional)
```

**Two key directories:**

- **`specs/`** - The source of truth. These specs describe how your system currently behaves. Organized by domain (e.g., `specs/auth/`, `specs/payments/`).

- **`changes/`** - Proposed modifications. Each change gets its own folder with all related artifacts. When a change is complete, its specs merge into the main `specs/` directory.

## Understanding Artifacts

Each change folder contains artifacts that guide the work:

| Artifact | Purpose |
|----------|---------|
| `proposal.md` | The "why" and "what" - captures intent, scope, and approach |
| `specs/` | Delta specs showing ADDED/MODIFIED/REMOVED requirements |
| `design.md` | The "how" - technical approach and architecture decisions |
| `tasks.md` | Implementation checklist with checkboxes |

**Artifacts build on each other:**

```
proposal ──► specs ──► design ──► tasks ──► implement
   ▲           ▲          ▲                    │
   └───────────┴──────────┴────────────────────┘
            update as you learn
```

You can always go back and refine earlier artifacts as you learn more during implementation.

## How Delta Specs Work

Delta specs are the key concept in OpenSpec. They show what's changing relative to your current specs.

### The Format

Delta specs use sections to indicate the type of change:

```markdown
# Delta for Auth

## ADDED Requirements

### Requirement: Two-Factor Authentication
The system MUST require a second factor during login.

#### Scenario: OTP required
- GIVEN a user with 2FA enabled
- WHEN the user submits valid credentials
- THEN an OTP challenge is presented

## MODIFIED Requirements

### Requirement: Session Timeout
The system SHALL expire sessions after 30 minutes of inactivity.
(Previously: 60 minutes)

#### Scenario: Idle timeout
- GIVEN an authenticated session
- WHEN 30 minutes pass without activity
- THEN the session is invalidated

## REMOVED Requirements

### Requirement: Remember Me
(Deprecated in favor of 2FA)
```

### What Happens on Archive

When you archive a change:

1. **ADDED** requirements are appended to the main spec
2. **MODIFIED** requirements replace the existing version
3. **REMOVED** requirements are deleted from the main spec

The change folder moves to `openspec/changes/archive/` for audit history.

## Example: Your First Change

Let's walk through adding dark mode to an application.

### 1. Start the Change (Default)

```text
You: /opsx:propose add-dark-mode

AI:  Created openspec/changes/add-dark-mode/
     ✓ proposal.md — why we're doing this, what's changing
     ✓ specs/       — requirements and scenarios
     ✓ design.md    — technical approach
     ✓ tasks.md     — implementation checklist
     Ready for implementation!
```

If you've enabled the expanded workflow profile, you can also do this as two steps: `/opsx:new` then `/opsx:ff` (or `/opsx:continue` incrementally).

### 2. What Gets Created

**proposal.md** - Captures the intent:

```markdown
# Proposal: Add Dark Mode

## Intent
Users have requested a dark mode option to reduce eye strain
during nighttime usage.

## Scope
- Add theme toggle in settings
- Support system preference detection
- Persist preference in localStorage

## Approach
Use CSS custom properties for theming with a React context
for state management.
```

**specs/ui/spec.md** - Delta showing new requirements:

```markdown
# Delta for UI

## ADDED Requirements

### Requirement: Theme Selection
The system SHALL allow users to choose between light and dark themes.

#### Scenario: Manual toggle
- GIVEN a user on any page
- WHEN the user clicks the theme toggle
- THEN the theme switches immediately
- AND the preference persists across sessions

#### Scenario: System preference
- GIVEN a user with no saved preference
- WHEN the application loads
- THEN the system's preferred color scheme is used
```

**tasks.md** - Implementation checklist:

```markdown
# Tasks

## 1. Theme Infrastructure
- [ ] 1.1 Create ThemeContext with light/dark state
- [ ] 1.2 Add CSS custom properties for colors
- [ ] 1.3 Implement localStorage persistence

## 2. UI Components
- [ ] 2.1 Create ThemeToggle component
- [ ] 2.2 Add toggle to settings page
- [ ] 2.3 Update Header to include quick toggle

## 3. Styling
- [ ] 3.1 Define dark theme color palette
- [ ] 3.2 Update components to use CSS variables
```

### 3. Implement

```
You: /opsx:apply

AI:  Working through tasks...
     ✓ 1.1 Created ThemeContext with light/dark state
     ✓ 1.2 Added CSS custom properties to globals.css
     ✓ 1.3 Implemented localStorage persistence
     ✓ 2.1 Created ThemeToggle component
     ...
     All tasks complete!
```

During implementation, if you discover the design needs adjustment, just update the artifact and continue.

### 4. Archive

```
You: /opsx:archive

AI:  Archiving add-dark-mode...
     ✓ Merged specs into openspec/specs/ui/spec.md
     ✓ Moved to openspec/changes/archive/2025-01-24-add-dark-mode/
     Done! Ready for the next feature.
```

Your delta specs are now part of the main specs, documenting how your system works.

## Verifying and Reviewing

Use the CLI to check on your changes:

```bash
# List active changes
openspec list

# View change details
openspec show add-dark-mode

# Validate spec formatting
openspec validate add-dark-mode

# Interactive dashboard
openspec view
```

## Next Steps

- [Workflows](workflows.md) - Common patterns and when to use each command
- [Commands](commands.md) - Full reference for all slash commands
- [Concepts](concepts.md) - Deeper understanding of specs, changes, and schemas
- [Customization](customization.md) - Make OpenSpec work your way



---

# FILE: docs/installation.md

# Installation

## Prerequisites

- **Node.js 20.19.0 or higher** — Check your version: `node --version`

## Package Managers

### npm

```bash
npm install -g @fission-ai/openspec@latest
```

### pnpm

```bash
pnpm add -g @fission-ai/openspec@latest
```

### yarn

```bash
yarn global add @fission-ai/openspec@latest
```

### bun

```bash
bun add -g @fission-ai/openspec@latest
```

## Nix

Run OpenSpec directly without installation:

```bash
nix run github:Fission-AI/OpenSpec -- init
```

Or install to your profile:

```bash
nix profile install github:Fission-AI/OpenSpec
```

Or add to your development environment in `flake.nix`:

```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    openspec.url = "github:Fission-AI/OpenSpec";
  };

  outputs = { nixpkgs, openspec, ... }: {
    devShells.x86_64-linux.default = nixpkgs.legacyPackages.x86_64-linux.mkShell {
      buildInputs = [ openspec.packages.x86_64-linux.default ];
    };
  };
}
```

## Verify Installation

```bash
openspec --version
```

## Next Steps

After installing, initialize OpenSpec in your project:

```bash
cd your-project
openspec init
```

See [Getting Started](getting-started.md) for a full walkthrough.



---

# FILE: docs/migration-guide.md

# Migrating to OPSX

This guide helps you transition from the legacy OpenSpec workflow to OPSX. The migration is designed to be smooth—your existing work is preserved, and the new system offers more flexibility.

## What's Changing?

OPSX replaces the old phase-locked workflow with a fluid, action-based approach. Here's the key shift:

| Aspect | Legacy | OPSX |
|--------|--------|------|
| **Commands** | `/openspec:proposal`, `/openspec:apply`, `/openspec:archive` | Default: `/opsx:propose`, `/opsx:apply`, `/opsx:archive` (expanded workflow commands optional) |
| **Workflow** | Create all artifacts at once | Create incrementally or all at once—your choice |
| **Going back** | Awkward phase gates | Natural—update any artifact anytime |
| **Customization** | Fixed structure | Schema-driven, fully hackable |
| **Configuration** | `CLAUDE.md` with markers + `project.md` | Clean config in `openspec/config.yaml` |

**The philosophy change:** Work isn't linear. OPSX stops pretending it is.

---

## Before You Begin

### Your Existing Work Is Safe

The migration process is designed with preservation in mind:

- **Active changes in `openspec/changes/`** — Completely preserved. You can continue them with OPSX commands.
- **Archived changes** — Untouched. Your history remains intact.
- **Main specs in `openspec/specs/`** — Untouched. These are your source of truth.
- **Your content in CLAUDE.md, AGENTS.md, etc.** — Preserved. Only the OpenSpec marker blocks are removed; everything you wrote stays.

### What Gets Removed

Only OpenSpec-managed files that are being replaced:

| What | Why |
|------|-----|
| Legacy slash command directories/files | Replaced by the new skills system |
| `openspec/AGENTS.md` | Obsolete workflow trigger |
| OpenSpec markers in `CLAUDE.md`, `AGENTS.md`, etc. | No longer needed |

**Legacy command locations by tool** (examples—your tool may vary):

- Claude Code: `.claude/commands/openspec/`
- Cursor: `.cursor/commands/openspec-*.md`
- Windsurf: `.windsurf/workflows/openspec-*.md`
- Cline: `.clinerules/workflows/openspec-*.md`
- Roo: `.roo/commands/openspec-*.md`
- GitHub Copilot: `.github/prompts/openspec-*.prompt.md` (IDE extensions only; not supported in Copilot CLI)
- And others (Augment, Continue, Amazon Q, etc.)

The migration detects whichever tools you have configured and cleans up their legacy files.

The removal list may seem long, but these are all files that OpenSpec originally created. Your own content is never deleted.

### What Needs Your Attention

One file requires manual migration:

**`openspec/project.md`** — This file isn't deleted automatically because it may contain project context you've written. You'll need to:

1. Review its contents
2. Move useful context to `openspec/config.yaml` (see guidance below)
3. Delete the file when ready

**Why we made this change:**

The old `project.md` was passive—agents might read it, might not, might forget what they read. We found reliability was inconsistent.

The new `config.yaml` context is **actively injected into every OpenSpec planning request**. This means your project conventions, tech stack, and rules are always present when the AI is creating artifacts. Higher reliability.

**The tradeoff:**

Because context is injected into every request, you'll want to be concise. Focus on what really matters:
- Tech stack and key conventions
- Non-obvious constraints the AI needs to know
- Rules that frequently got ignored before

Don't worry about getting it perfect. We're still learning what works best here, and we'll be improving how context injection works as we experiment.

---

## Running the Migration

Both `openspec init` and `openspec update` detect legacy files and guide you through the same cleanup process. Use whichever fits your situation:

- New installs default to profile `core` (`propose`, `explore`, `apply`, `archive`).
- Migrated installs preserve your previously installed workflows by writing a `custom` profile when needed.

### Using `openspec init`

Run this if you want to add new tools or reconfigure which tools are set up:

```bash
openspec init
```

The init command detects legacy files and guides you through cleanup:

```
Upgrading to the new OpenSpec

OpenSpec now uses agent skills, the emerging standard across coding
agents. This simplifies your setup while keeping everything working
as before.

Files to remove
No user content to preserve:
  • .claude/commands/openspec/
  • openspec/AGENTS.md

Files to update
OpenSpec markers will be removed, your content preserved:
  • CLAUDE.md
  • AGENTS.md

Needs your attention
  • openspec/project.md
    We won't delete this file. It may contain useful project context.

    The new openspec/config.yaml has a "context:" section for planning
    context. This is included in every OpenSpec request and works more
    reliably than the old project.md approach.

    Review project.md, move any useful content to config.yaml's context
    section, then delete the file when ready.

? Upgrade and clean up legacy files? (Y/n)
```

**What happens when you say yes:**

1. Legacy slash command directories are removed
2. OpenSpec markers are stripped from `CLAUDE.md`, `AGENTS.md`, etc. (your content stays)
3. `openspec/AGENTS.md` is deleted
4. New skills are installed in `.claude/skills/`
5. `openspec/config.yaml` is created with a default schema

### Using `openspec update`

Run this if you just want to migrate and refresh your existing tools to the latest version:

```bash
openspec update
```

The update command also detects and cleans up legacy artifacts, then refreshes generated skills/commands to match your current profile and delivery settings.

### Non-Interactive / CI Environments

For scripted migrations:

```bash
openspec init --force --tools claude
```

The `--force` flag skips prompts and auto-accepts cleanup.

---

## Migrating project.md to config.yaml

The old `openspec/project.md` was a freeform markdown file for project context. The new `openspec/config.yaml` is structured and—critically—**injected into every planning request** so your conventions are always present when the AI works.

### Before (project.md)

```markdown
# Project Context

This is a TypeScript monorepo using React and Node.js.
We use Jest for testing and follow strict ESLint rules.
Our API is RESTful and documented in docs/api.md.

## Conventions

- All public APIs must maintain backwards compatibility
- New features should include tests
- Use Given/When/Then format for specifications
```

### After (config.yaml)

```yaml
schema: spec-driven

context: |
  Tech stack: TypeScript, React, Node.js
  Testing: Jest with React Testing Library
  API: RESTful, documented in docs/api.md
  We maintain backwards compatibility for all public APIs

rules:
  proposal:
    - Include rollback plan for risky changes
  specs:
    - Use Given/When/Then format for scenarios
    - Reference existing patterns before inventing new ones
  design:
    - Include sequence diagrams for complex flows
```

### Key Differences

| project.md | config.yaml |
|------------|-------------|
| Freeform markdown | Structured YAML |
| One blob of text | Separate context and per-artifact rules |
| Unclear when it's used | Context appears in ALL artifacts; rules appear in matching artifacts only |
| No schema selection | Explicit `schema:` field sets default workflow |

### What to Keep, What to Drop

When migrating, be selective. Ask yourself: "Does the AI need this for *every* planning request?"

**Good candidates for `context:`**
- Tech stack (languages, frameworks, databases)
- Key architectural patterns (monorepo, microservices, etc.)
- Non-obvious constraints ("we can't use library X because...")
- Critical conventions that often get ignored

**Move to `rules:` instead**
- Artifact-specific formatting ("use Given/When/Then in specs")
- Review criteria ("proposals must include rollback plans")
- These only appear for the matching artifact, keeping other requests lighter

**Leave out entirely**
- General best practices the AI already knows
- Verbose explanations that could be summarized
- Historical context that doesn't affect current work

### Migration Steps

1. **Create config.yaml** (if not already created by init):
   ```yaml
   schema: spec-driven
   ```

2. **Add your context** (be concise—this goes into every request):
   ```yaml
   context: |
     Your project background goes here.
     Focus on what the AI genuinely needs to know.
   ```

3. **Add per-artifact rules** (optional):
   ```yaml
   rules:
     proposal:
       - Your proposal-specific guidance
     specs:
       - Your spec-writing rules
   ```

4. **Delete project.md** once you've moved everything useful.

**Don't overthink it.** Start with the essentials and iterate. If you notice the AI missing something important, add it. If context feels bloated, trim it. This is a living document.

### Need Help? Use This Prompt

If you're unsure how to distill your project.md, ask your AI assistant:

```
I'm migrating from OpenSpec's old project.md to the new config.yaml format.

Here's my current project.md:
[paste your project.md content]

Please help me create a config.yaml with:
1. A concise `context:` section (this gets injected into every planning request, so keep it tight—focus on tech stack, key constraints, and conventions that often get ignored)
2. `rules:` for specific artifacts if any content is artifact-specific (e.g., "use Given/When/Then" belongs in specs rules, not global context)

Leave out anything generic that AI models already know. Be ruthless about brevity.
```

The AI will help you identify what's essential vs. what can be trimmed.

---

## The New Commands

Command availability is profile-dependent:

**Default (`core` profile):**

| Command | Purpose |
|---------|---------|
| `/opsx:propose` | Create a change and generate planning artifacts in one step |
| `/opsx:explore` | Think through ideas with no structure |
| `/opsx:apply` | Implement tasks from tasks.md |
| `/opsx:archive` | Finalize and archive the change |

**Expanded workflow (custom selection):**

| Command | Purpose |
|---------|---------|
| `/opsx:new` | Start a new change scaffold |
| `/opsx:continue` | Create the next artifact (one at a time) |
| `/opsx:ff` | Fast-forward—create planning artifacts at once |
| `/opsx:verify` | Validate implementation matches specs |
| `/opsx:sync` | Preview/spec-merge without archiving |
| `/opsx:bulk-archive` | Archive multiple changes at once |
| `/opsx:onboard` | Guided end-to-end onboarding workflow |

Enable expanded commands with `openspec config profile`, then run `openspec update`.

### Command Mapping from Legacy

| Legacy | OPSX Equivalent |
|--------|-----------------|
| `/openspec:proposal` | `/opsx:propose` (default) or `/opsx:new` then `/opsx:ff` (expanded) |
| `/openspec:apply` | `/opsx:apply` |
| `/openspec:archive` | `/opsx:archive` |

### New Capabilities

These capabilities are part of the expanded workflow command set.

**Granular artifact creation:**
```
/opsx:continue
```
Creates one artifact at a time based on dependencies. Use this when you want to review each step.

**Exploration mode:**
```
/opsx:explore
```
Think through ideas with a partner before committing to a change.

---

## Understanding the New Architecture

### From Phase-Locked to Fluid

The legacy workflow forced linear progression:

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│   PLANNING   │ ───► │ IMPLEMENTING │ ───► │   ARCHIVING  │
│    PHASE     │      │    PHASE     │      │    PHASE     │
└──────────────┘      └──────────────┘      └──────────────┘

If you're in implementation and realize the design is wrong?
Too bad. Phase gates don't let you go back easily.
```

OPSX uses actions, not phases:

```
         ┌───────────────────────────────────────────────┐
         │           ACTIONS (not phases)                │
         │                                               │
         │     new ◄──► continue ◄──► apply ◄──► archive │
         │      │          │           │             │   │
         │      └──────────┴───────────┴─────────────┘   │
         │                    any order                  │
         └───────────────────────────────────────────────┘
```

### Dependency Graph

Artifacts form a directed graph. Dependencies are enablers, not gates:

```
                        proposal
                       (root node)
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
           specs                       design
        (requires:                  (requires:
         proposal)                   proposal)
              │                           │
              └─────────────┬─────────────┘
                            │
                            ▼
                         tasks
                     (requires:
                     specs, design)
```

When you run `/opsx:continue`, it checks what's ready and offers the next artifact. You can also create multiple ready artifacts in any order.

### Skills vs Commands

The legacy system used tool-specific command files:

```
.claude/commands/openspec/
├── proposal.md
├── apply.md
└── archive.md
```

OPSX uses the emerging **skills** standard:

```
.claude/skills/
├── openspec-explore/SKILL.md
├── openspec-new-change/SKILL.md
├── openspec-continue-change/SKILL.md
├── openspec-apply-change/SKILL.md
└── ...
```

Skills are recognized across multiple AI coding tools and provide richer metadata.

---

## Continuing Existing Changes

Your in-progress changes work seamlessly with OPSX commands.

**Have an active change from the legacy workflow?**

```
/opsx:apply add-my-feature
```

OPSX reads the existing artifacts and continues from where you left off.

**Want to add more artifacts to an existing change?**

```
/opsx:continue add-my-feature
```

Shows what's ready to create based on what already exists.

**Need to see status?**

```bash
openspec status --change add-my-feature
```

---

## The New Config System

### config.yaml Structure

```yaml
# Required: Default schema for new changes
schema: spec-driven

# Optional: Project context (max 50KB)
# Injected into ALL artifact instructions
context: |
  Your project background, tech stack,
  conventions, and constraints.

# Optional: Per-artifact rules
# Only injected into matching artifacts
rules:
  proposal:
    - Include rollback plan
  specs:
    - Use Given/When/Then format
  design:
    - Document fallback strategies
  tasks:
    - Break into 2-hour maximum chunks
```

### Schema Resolution

When determining which schema to use, OPSX checks in order:

1. **CLI flag**: `--schema <name>` (highest priority)
2. **Change metadata**: `.openspec.yaml` in the change directory
3. **Project config**: `openspec/config.yaml`
4. **Default**: `spec-driven`

### Available Schemas

| Schema | Artifacts | Best For |
|--------|-----------|----------|
| `spec-driven` | proposal → specs → design → tasks | Most projects |

List all available schemas:

```bash
openspec schemas
```

### Custom Schemas

Create your own workflow:

```bash
openspec schema init my-workflow
```

Or fork an existing one:

```bash
openspec schema fork spec-driven my-workflow
```

See [Customization](customization.md) for details.

---

## Troubleshooting

### "Legacy files detected in non-interactive mode"

You're running in a CI or non-interactive environment. Use:

```bash
openspec init --force
```

### Commands not appearing after migration

Restart your IDE. Skills are detected at startup.

### "Unknown artifact ID in rules"

Check that your `rules:` keys match your schema's artifact IDs:

- **spec-driven**: `proposal`, `specs`, `design`, `tasks`

Run this to see valid artifact IDs:

```bash
openspec schemas --json
```

### Config not being applied

1. Ensure the file is at `openspec/config.yaml` (not `.yml`)
2. Validate YAML syntax
3. Config changes take effect immediately—no restart needed

### project.md not migrated

The system intentionally preserves `project.md` because it may contain your custom content. Review it manually, move useful parts to `config.yaml`, then delete it.

### Want to see what would be cleaned up?

Run init and decline the cleanup prompt—you'll see the full detection summary without any changes being made.

---

## Quick Reference

### Files After Migration

```
project/
├── openspec/
│   ├── specs/                    # Unchanged
│   ├── changes/                  # Unchanged
│   │   └── archive/              # Unchanged
│   └── config.yaml               # NEW: Project configuration
├── .claude/
│   └── skills/                   # NEW: OPSX skills
│       ├── openspec-propose/     # default core profile
│       ├── openspec-explore/
│       ├── openspec-apply-change/
│       └── ...                   # expanded profile adds new/continue/ff/etc.
├── CLAUDE.md                     # OpenSpec markers removed, your content preserved
└── AGENTS.md                     # OpenSpec markers removed, your content preserved
```

### What's Gone

- `.claude/commands/openspec/` — replaced by `.claude/skills/`
- `openspec/AGENTS.md` — obsolete
- `openspec/project.md` — migrate to `config.yaml`, then delete
- OpenSpec marker blocks in `CLAUDE.md`, `AGENTS.md`, etc.

### Command Cheatsheet

```text
/opsx:propose      Start quickly (default core profile)
/opsx:apply        Implement tasks
/opsx:archive      Finish and archive

# Expanded workflow (if enabled):
/opsx:new          Scaffold a change
/opsx:continue     Create next artifact
/opsx:ff           Create planning artifacts
```

---

## Getting Help

- **Discord**: [discord.gg/YctCnvvshC](https://discord.gg/YctCnvvshC)
- **GitHub Issues**: [github.com/Fission-AI/OpenSpec/issues](https://github.com/Fission-AI/OpenSpec/issues)
- **Documentation**: [docs/opsx.md](opsx.md) for the full OPSX reference



---

# FILE: docs/multi-language.md

# Multi-Language Guide

Configure OpenSpec to generate artifacts in languages other than English.

## Quick Setup

Add a language instruction to your `openspec/config.yaml`:

```yaml
schema: spec-driven

context: |
  Language: Portuguese (pt-BR)
  All artifacts must be written in Brazilian Portuguese.

  # Your other project context below...
  Tech stack: TypeScript, React, Node.js
```

That's it. All generated artifacts will now be in Portuguese.

## Language Examples

### Portuguese (Brazil)

```yaml
context: |
  Language: Portuguese (pt-BR)
  All artifacts must be written in Brazilian Portuguese.
```

### Spanish

```yaml
context: |
  Idioma: Español
  Todos los artefactos deben escribirse en español.
```

### Chinese (Simplified)

```yaml
context: |
  语言：中文（简体）
  所有产出物必须用简体中文撰写。
```

### Japanese

```yaml
context: |
  言語：日本語
  すべての成果物は日本語で作成してください。
```

### French

```yaml
context: |
  Langue : Français
  Tous les artefacts doivent être rédigés en français.
```

### German

```yaml
context: |
  Sprache: Deutsch
  Alle Artefakte müssen auf Deutsch verfasst werden.
```

## Tips

### Handle Technical Terms

Decide how to handle technical terminology:

```yaml
context: |
  Language: Japanese
  Write in Japanese, but:
  - Keep technical terms like "API", "REST", "GraphQL" in English
  - Code examples and file paths remain in English
```

### Combine with Other Context

Language settings work alongside your other project context:

```yaml
schema: spec-driven

context: |
  Language: Portuguese (pt-BR)
  All artifacts must be written in Brazilian Portuguese.

  Tech stack: TypeScript, React 18, Node.js 20
  Database: PostgreSQL with Prisma ORM
```

## Verification

To verify your language config is working:

```bash
# Check the instructions - should show your language context
openspec instructions proposal --change my-change

# Output will include your language context
```

## Related Documentation

- [Customization Guide](./customization.md) - Project configuration options
- [Workflows Guide](./workflows.md) - Full workflow documentation



---

# FILE: docs/opsx.md

# OPSX Workflow

> Feedback welcome on [Discord](https://discord.gg/YctCnvvshC).

## What Is It?

OPSX is now the standard workflow for OpenSpec.

It's a **fluid, iterative workflow** for OpenSpec changes. No more rigid phases — just actions you can take anytime.

## Why This Exists

The legacy OpenSpec workflow works, but it's **locked down**:

- **Instructions are hardcoded** — buried in TypeScript, you can't change them
- **All-or-nothing** — one big command creates everything, can't test individual pieces
- **Fixed structure** — same workflow for everyone, no customization
- **Black box** — when AI output is bad, you can't tweak the prompts

**OPSX opens it up.** Now anyone can:

1. **Experiment with instructions** — edit a template, see if the AI does better
2. **Test granularly** — validate each artifact's instructions independently
3. **Customize workflows** — define your own artifacts and dependencies
4. **Iterate quickly** — change a template, test immediately, no rebuild

```
Legacy workflow:                      OPSX:
┌────────────────────────┐           ┌────────────────────────┐
│  Hardcoded in package  │           │  schema.yaml           │◄── You edit this
│  (can't change)        │           │  templates/*.md        │◄── Or this
│        ↓               │           │        ↓               │
│  Wait for new release  │           │  Instant effect        │
│        ↓               │           │        ↓               │
│  Hope it's better      │           │  Test it yourself      │
└────────────────────────┘           └────────────────────────┘
```

**This is for everyone:**
- **Teams** — create workflows that match how you actually work
- **Power users** — tweak prompts to get better AI outputs for your codebase
- **OpenSpec contributors** — experiment with new approaches without releases

We're all still learning what works best. OPSX lets us learn together.

## The User Experience

**The problem with linear workflows:**
You're "in planning phase", then "in implementation phase", then "done". But real work doesn't work that way. You implement something, realize your design was wrong, need to update specs, continue implementing. Linear phases fight against how work actually happens.

**OPSX approach:**
- **Actions, not phases** — create, implement, update, archive — do any of them anytime
- **Dependencies are enablers** — they show what's possible, not what's required next

```
  proposal ──→ specs ──→ design ──→ tasks ──→ implement
```

## Setup

```bash
# Make sure you have openspec installed — skills are automatically generated
openspec init
```

This creates skills in `.claude/skills/` (or equivalent) that AI coding assistants auto-detect.

By default, OpenSpec uses the `core` workflow profile (`propose`, `explore`, `apply`, `archive`). If you want the expanded workflow commands (`new`, `continue`, `ff`, `verify`, `sync`, `bulk-archive`, `onboard`), configure them with `openspec config profile` and apply with `openspec update`.

During setup, you'll be prompted to create a **project config** (`openspec/config.yaml`). This is optional but recommended.

## Project Configuration

Project config lets you set defaults and inject project-specific context into all artifacts.

### Creating Config

Config is created during `openspec init`, or manually:

```yaml
# openspec/config.yaml
schema: spec-driven

context: |
  Tech stack: TypeScript, React, Node.js
  API conventions: RESTful, JSON responses
  Testing: Vitest for unit tests, Playwright for e2e
  Style: ESLint with Prettier, strict TypeScript

rules:
  proposal:
    - Include rollback plan
    - Identify affected teams
  specs:
    - Use Given/When/Then format for scenarios
  design:
    - Include sequence diagrams for complex flows
```

### Config Fields

| Field | Type | Description |
|-------|------|-------------|
| `schema` | string | Default schema for new changes (e.g., `spec-driven`) |
| `context` | string | Project context injected into all artifact instructions |
| `rules` | object | Per-artifact rules, keyed by artifact ID |

### How It Works

**Schema precedence** (highest to lowest):
1. CLI flag (`--schema <name>`)
2. Change metadata (`.openspec.yaml` in change directory)
3. Project config (`openspec/config.yaml`)
4. Default (`spec-driven`)

**Context injection:**
- Context is prepended to every artifact's instructions
- Wrapped in `<context>...</context>` tags
- Helps AI understand your project's conventions

**Rules injection:**
- Rules are only injected for matching artifacts
- Wrapped in `<rules>...</rules>` tags
- Appear after context, before the template

### Artifact IDs by Schema

**spec-driven** (default):
- `proposal` — Change proposal
- `specs` — Specifications
- `design` — Technical design
- `tasks` — Implementation tasks

### Config Validation

- Unknown artifact IDs in `rules` generate warnings
- Schema names are validated against available schemas
- Context has a 50KB size limit
- Invalid YAML is reported with line numbers

### Troubleshooting

**"Unknown artifact ID in rules: X"**
- Check artifact IDs match your schema (see list above)
- Run `openspec schemas --json` to see artifact IDs for each schema

**Config not being applied:**
- Ensure file is at `openspec/config.yaml` (not `.yml`)
- Check YAML syntax with a validator
- Config changes take effect immediately (no restart needed)

**Context too large:**
- Context is limited to 50KB
- Summarize or link to external docs instead

## Commands

| Command | What it does |
|---------|--------------|
| `/opsx:propose` | Create a change and generate planning artifacts in one step (default quick path) |
| `/opsx:explore` | Think through ideas, investigate problems, clarify requirements |
| `/opsx:new` | Start a new change scaffold (expanded workflow) |
| `/opsx:continue` | Create the next artifact (expanded workflow) |
| `/opsx:ff` | Fast-forward planning artifacts (expanded workflow) |
| `/opsx:apply` | Implement tasks, updating artifacts as needed |
| `/opsx:verify` | Validate implementation against artifacts (expanded workflow) |
| `/opsx:sync` | Sync delta specs to main (expanded workflow, optional) |
| `/opsx:archive` | Archive when done |
| `/opsx:bulk-archive` | Archive multiple completed changes (expanded workflow) |
| `/opsx:onboard` | Guided walkthrough of an end-to-end change (expanded workflow) |

## Usage

### Explore an idea
```
/opsx:explore
```
Think through ideas, investigate problems, compare options. No structure required - just a thinking partner. When insights crystallize, transition to `/opsx:propose` (default) or `/opsx:new`/`/opsx:ff` (expanded).

### Start a new change
```
/opsx:propose
```
Creates the change and generates planning artifacts needed before implementation.

If you've enabled expanded workflows, you can instead use:

```text
/opsx:new        # scaffold only
/opsx:continue   # create one artifact at a time
/opsx:ff         # create all planning artifacts at once
```

### Create artifacts
```
/opsx:continue
```
Shows what's ready to create based on dependencies, then creates one artifact. Use repeatedly to build up your change incrementally.

```
/opsx:ff add-dark-mode
```
Creates all planning artifacts at once. Use when you have a clear picture of what you're building.

### Implement (the fluid part)
```
/opsx:apply
```
Works through tasks, checking them off as you go. If you're juggling multiple changes, you can run `/opsx:apply <name>`; otherwise it should infer from the conversation and prompt you to choose if it can't tell.

### Finish up
```
/opsx:archive   # Move to archive when done (prompts to sync specs if needed)
```

## When to Update vs. Start Fresh

You can always edit your proposal or specs before implementation. But when does refining become "this is different work"?

### What a Proposal Captures

A proposal defines three things:
1. **Intent** — What problem are you solving?
2. **Scope** — What's in/out of bounds?
3. **Approach** — How will you solve it?

The question is: which changed, and by how much?

### Update the Existing Change When:

**Same intent, refined execution**
- You discover edge cases you didn't consider
- The approach needs tweaking but the goal is unchanged
- Implementation reveals the design was slightly off

**Scope narrows**
- You realize full scope is too big, want to ship MVP first
- "Add dark mode" → "Add dark mode toggle (system preference in v2)"

**Learning-driven corrections**
- Codebase isn't structured how you thought
- A dependency doesn't work as expected
- "Use CSS variables" → "Use Tailwind's dark: prefix instead"

### Start a New Change When:

**Intent fundamentally changed**
- The problem itself is different now
- "Add dark mode" → "Add comprehensive theme system with custom colors, fonts, spacing"

**Scope exploded**
- Change grew so much it's essentially different work
- Original proposal would be unrecognizable after updates
- "Fix login bug" → "Rewrite auth system"

**Original is completable**
- The original change can be marked "done"
- New work stands alone, not a refinement
- Complete "Add dark mode MVP" → Archive → New change "Enhance dark mode"

### The Heuristics

```
                        ┌─────────────────────────────────────┐
                        │     Is this the same work?          │
                        └──────────────┬──────────────────────┘
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                  │
                    ▼                  ▼                  ▼
             Same intent?      >50% overlap?      Can original
             Same problem?     Same scope?        be "done" without
                    │                  │          these changes?
                    │                  │                  │
          ┌────────┴────────┐  ┌──────┴──────┐   ┌───────┴───────┐
          │                 │  │             │   │               │
         YES               NO YES           NO  NO              YES
          │                 │  │             │   │               │
          ▼                 ▼  ▼             ▼   ▼               ▼
       UPDATE            NEW  UPDATE       NEW  UPDATE          NEW
```

| Test | Update | New Change |
|------|--------|------------|
| **Identity** | "Same thing, refined" | "Different work" |
| **Scope overlap** | >50% overlaps | <50% overlaps |
| **Completion** | Can't be "done" without changes | Can finish original, new work stands alone |
| **Story** | Update chain tells coherent story | Patches would confuse more than clarify |

### The Principle

> **Update preserves context. New change provides clarity.**
>
> Choose update when the history of your thinking is valuable.
> Choose new when starting fresh would be clearer than patching.

Think of it like git branches:
- Keep committing while working on the same feature
- Start a new branch when it's genuinely new work
- Sometimes merge a partial feature and start fresh for phase 2

## What's Different?

| | Legacy (`/openspec:proposal`) | OPSX (`/opsx:*`) |
|---|---|---|
| **Structure** | One big proposal document | Discrete artifacts with dependencies |
| **Workflow** | Linear phases: plan → implement → archive | Fluid actions — do anything anytime |
| **Iteration** | Awkward to go back | Update artifacts as you learn |
| **Customization** | Fixed structure | Schema-driven (define your own artifacts) |

**The key insight:** work isn't linear. OPSX stops pretending it is.

## Architecture Deep Dive

This section explains how OPSX works under the hood and how it compares to the legacy workflow.
Examples in this section use the expanded command set (`new`, `continue`, etc.); default `core` users can map the same flow to `propose → apply → archive`.

### Philosophy: Phases vs Actions

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         LEGACY WORKFLOW                                      │
│                    (Phase-Locked, All-or-Nothing)                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌──────────────┐      ┌──────────────┐      ┌──────────────┐             │
│   │   PLANNING   │ ───► │ IMPLEMENTING │ ───► │   ARCHIVING  │             │
│   │    PHASE     │      │    PHASE     │      │    PHASE     │             │
│   └──────────────┘      └──────────────┘      └──────────────┘             │
│         │                     │                     │                       │
│         ▼                     ▼                     ▼                       │
│   /openspec:proposal   /openspec:apply      /openspec:archive              │
│                                                                             │
│   • Creates ALL artifacts at once                                          │
│   • Can't go back to update specs during implementation                    │
│   • Phase gates enforce linear progression                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│                            OPSX WORKFLOW                                     │
│                      (Fluid Actions, Iterative)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│              ┌────────────────────────────────────────────┐                 │
│              │           ACTIONS (not phases)             │                 │
│              │                                            │                 │
│              │   new ◄──► continue ◄──► apply ◄──► archive │                 │
│              │    │          │           │           │    │                 │
│              │    └──────────┴───────────┴───────────┘    │                 │
│              │              any order                     │                 │
│              └────────────────────────────────────────────┘                 │
│                                                                             │
│   • Create artifacts one at a time OR fast-forward                         │
│   • Update specs/design/tasks during implementation                        │
│   • Dependencies enable progress, phases don't exist                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Component Architecture

**Legacy workflow** uses hardcoded templates in TypeScript:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LEGACY WORKFLOW COMPONENTS                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Hardcoded Templates (TypeScript strings)                                  │
│                    │                                                        │
│                    ▼                                                        │
│   Tool-specific configurators/adapters                                      │
│                    │                                                        │
│                    ▼                                                        │
│   Generated Command Files (.claude/commands/openspec/*.md)                  │
│                                                                             │
│   • Fixed structure, no artifact awareness                                  │
│   • Change requires code modification + rebuild                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**OPSX** uses external schemas and a dependency graph engine:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         OPSX COMPONENTS                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Schema Definitions (YAML)                                                 │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  name: spec-driven                                                  │   │
│   │  artifacts:                                                         │   │
│   │    - id: proposal                                                   │   │
│   │      generates: proposal.md                                         │   │
│   │      requires: []              ◄── Dependencies                     │   │
│   │    - id: specs                                                      │   │
│   │      generates: specs/**/*.md  ◄── Glob patterns                    │   │
│   │      requires: [proposal]      ◄── Enables after proposal           │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                    │                                                        │
│                    ▼                                                        │
│   Artifact Graph Engine                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  • Topological sort (dependency ordering)                           │   │
│   │  • State detection (filesystem existence)                           │   │
│   │  • Rich instruction generation (templates + context)                │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                    │                                                        │
│                    ▼                                                        │
│   Skill Files (.claude/skills/openspec-*/SKILL.md)                          │
│                                                                             │
│   • Cross-editor compatible (Claude Code, Cursor, Windsurf)                 │
│   • Skills query CLI for structured data                                    │
│   • Fully customizable via schema files                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Dependency Graph Model

Artifacts form a directed acyclic graph (DAG). Dependencies are **enablers**, not gates:

```
                              proposal
                             (root node)
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
                 specs                       design
              (requires:                  (requires:
               proposal)                   proposal)
                    │                           │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                               tasks
                           (requires:
                           specs, design)
                                  │
                                  ▼
                          ┌──────────────┐
                          │ APPLY PHASE  │
                          │ (requires:   │
                          │  tasks)      │
                          └──────────────┘
```

**State transitions:**

```
   BLOCKED ────────────────► READY ────────────────► DONE
      │                        │                       │
   Missing                  All deps               File exists
   dependencies             are DONE               on filesystem
```

### Information Flow

**Legacy workflow** — agent receives static instructions:

```
  User: "/openspec:proposal"
           │
           ▼
  ┌─────────────────────────────────────────┐
  │  Static instructions:                   │
  │  • Create proposal.md                   │
  │  • Create tasks.md                      │
  │  • Create design.md                     │
  │  • Create specs/<capability>/spec.md    │
  │                                         │
  │  No awareness of what exists or         │
  │  dependencies between artifacts         │
  └─────────────────────────────────────────┘
           │
           ▼
  Agent creates ALL artifacts in one go
```

**OPSX** — agent queries for rich context:

```
  User: "/opsx:continue"
           │
           ▼
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  Step 1: Query current state                                             │
  │  ┌────────────────────────────────────────────────────────────────────┐  │
  │  │  $ openspec status --change "add-auth" --json                      │  │
  │  │                                                                    │  │
  │  │  {                                                                 │  │
  │  │    "artifacts": [                                                  │  │
  │  │      {"id": "proposal", "status": "done"},                         │  │
  │  │      {"id": "specs", "status": "ready"},      ◄── First ready      │  │
  │  │      {"id": "design", "status": "ready"},                          │  │
  │  │      {"id": "tasks", "status": "blocked", "missingDeps": ["specs"]}│  │
  │  │    ]                                                               │  │
  │  │  }                                                                 │  │
  │  └────────────────────────────────────────────────────────────────────┘  │
  │                                                                          │
  │  Step 2: Get rich instructions for ready artifact                        │
  │  ┌────────────────────────────────────────────────────────────────────┐  │
  │  │  $ openspec instructions specs --change "add-auth" --json          │  │
  │  │                                                                    │  │
  │  │  {                                                                 │  │
  │  │    "template": "# Specification\n\n## ADDED Requirements...",      │  │
  │  │    "dependencies": [{"id": "proposal", "path": "...", "done": true}│  │
  │  │    "unlocks": ["tasks"]                                            │  │
  │  │  }                                                                 │  │
  │  └────────────────────────────────────────────────────────────────────┘  │
  │                                                                          │
  │  Step 3: Read dependencies → Create ONE artifact → Show what's unlocked  │
  └──────────────────────────────────────────────────────────────────────────┘
```

### Iteration Model

**Legacy workflow** — awkward to iterate:

```
  ┌─────────┐     ┌─────────┐     ┌─────────┐
  │/proposal│ ──► │ /apply  │ ──► │/archive │
  └─────────┘     └─────────┘     └─────────┘
       │               │
       │               ├── "Wait, the design is wrong"
       │               │
       │               ├── Options:
       │               │   • Edit files manually (breaks context)
       │               │   • Abandon and start over
       │               │   • Push through and fix later
       │               │
       │               └── No official "go back" mechanism
       │
       └── Creates ALL artifacts at once
```

**OPSX** — natural iteration:

```
  /opsx:new ───► /opsx:continue ───► /opsx:apply ───► /opsx:archive
      │                │                  │
      │                │                  ├── "The design is wrong"
      │                │                  │
      │                │                  ▼
      │                │            Just edit design.md
      │                │            and continue!
      │                │                  │
      │                │                  ▼
      │                │         /opsx:apply picks up
      │                │         where you left off
      │                │
      │                └── Creates ONE artifact, shows what's unlocked
      │
      └── Scaffolds change, waits for direction
```

### Custom Schemas

Create custom workflows using the schema management commands:

```bash
# Create a new schema from scratch (interactive)
openspec schema init my-workflow

# Or fork an existing schema as a starting point
openspec schema fork spec-driven my-workflow

# Validate your schema structure
openspec schema validate my-workflow

# See where a schema resolves from (useful for debugging)
openspec schema which my-workflow
```

Schemas are stored in `openspec/schemas/` (project-local, version controlled) or `~/.local/share/openspec/schemas/` (user global).

**Schema structure:**
```
openspec/schemas/research-first/
├── schema.yaml
└── templates/
    ├── research.md
    ├── proposal.md
    └── tasks.md
```

**Example schema.yaml:**
```yaml
name: research-first
artifacts:
  - id: research        # Added before proposal
    generates: research.md
    requires: []

  - id: proposal
    generates: proposal.md
    requires: [research]  # Now depends on research

  - id: tasks
    generates: tasks.md
    requires: [proposal]
```

**Dependency Graph:**
```
   research ──► proposal ──► tasks
```

### Summary

| Aspect | Legacy | OPSX |
|--------|----------|------|
| **Templates** | Hardcoded TypeScript | External YAML + Markdown |
| **Dependencies** | None (all at once) | DAG with topological sort |
| **State** | Phase-based mental model | Filesystem existence |
| **Customization** | Edit source, rebuild | Create schema.yaml |
| **Iteration** | Phase-locked | Fluid, edit anything |
| **Editor Support** | Tool-specific configurator/adapters | Single skills directory |

## Schemas

Schemas define what artifacts exist and their dependencies. Currently available:

- **spec-driven** (default): proposal → specs → design → tasks

```bash
# List available schemas
openspec schemas

# See all schemas with their resolution sources
openspec schema which --all

# Create a new schema interactively
openspec schema init my-workflow

# Fork an existing schema for customization
openspec schema fork spec-driven my-workflow

# Validate schema structure before use
openspec schema validate my-workflow
```

## Tips

- Use `/opsx:explore` to think through an idea before committing to a change
- `/opsx:ff` when you know what you want, `/opsx:continue` when exploring
- During `/opsx:apply`, if something's wrong — fix the artifact, then continue
- Tasks track progress via checkboxes in `tasks.md`
- Check status anytime: `openspec status --change "name"`

## Feedback

This is rough. That's intentional — we're learning what works.

Found a bug? Have ideas? Join us on [Discord](https://discord.gg/YctCnvvshC) or open an issue on [GitHub](https://github.com/Fission-AI/openspec/issues).



---

# FILE: docs/supported-tools.md

# Supported Tools

OpenSpec works with many AI coding assistants. When you run `openspec init`, OpenSpec configures selected tools using your active profile/workflow selection and delivery mode.

## How It Works

For each selected tool, OpenSpec can install:

1. **Skills** (if delivery includes skills): `.../skills/openspec-*/SKILL.md`
2. **Commands** (if delivery includes commands): tool-specific `opsx-*` command files

By default, OpenSpec uses the `core` profile, which includes:
- `propose`
- `explore`
- `apply`
- `archive`

You can enable expanded workflows (`new`, `continue`, `ff`, `verify`, `sync`, `bulk-archive`, `onboard`) via `openspec config profile`, then run `openspec update`.

## Tool Directory Reference

| Tool (ID) | Skills path pattern | Command path pattern |
|-----------|---------------------|----------------------|
| Amazon Q Developer (`amazon-q`) | `.amazonq/skills/openspec-*/SKILL.md` | `.amazonq/prompts/opsx-<id>.md` |
| Antigravity (`antigravity`) | `.agent/skills/openspec-*/SKILL.md` | `.agent/workflows/opsx-<id>.md` |
| Auggie (`auggie`) | `.augment/skills/openspec-*/SKILL.md` | `.augment/commands/opsx-<id>.md` |
| IBM Bob Shell (`bob`) | `.bob/skills/openspec-*/SKILL.md` | `.bob/commands/opsx-<id>.md` |
| Claude Code (`claude`) | `.claude/skills/openspec-*/SKILL.md` | `.claude/commands/opsx/<id>.md` |
| Cline (`cline`) | `.cline/skills/openspec-*/SKILL.md` | `.clinerules/workflows/opsx-<id>.md` |
| CodeBuddy (`codebuddy`) | `.codebuddy/skills/openspec-*/SKILL.md` | `.codebuddy/commands/opsx/<id>.md` |
| Codex (`codex`) | `.codex/skills/openspec-*/SKILL.md` | `$CODEX_HOME/prompts/opsx-<id>.md`\* |
| ForgeCode (`forgecode`) | `.forge/skills/openspec-*/SKILL.md` | Not generated (no command adapter; use skill-based `/openspec-*` invocations) |
| Continue (`continue`) | `.continue/skills/openspec-*/SKILL.md` | `.continue/prompts/opsx-<id>.prompt` |
| CoStrict (`costrict`) | `.cospec/skills/openspec-*/SKILL.md` | `.cospec/openspec/commands/opsx-<id>.md` |
| Crush (`crush`) | `.crush/skills/openspec-*/SKILL.md` | `.crush/commands/opsx/<id>.md` |
| Cursor (`cursor`) | `.cursor/skills/openspec-*/SKILL.md` | `.cursor/commands/opsx-<id>.md` |
| Factory Droid (`factory`) | `.factory/skills/openspec-*/SKILL.md` | `.factory/commands/opsx-<id>.md` |
| Gemini CLI (`gemini`) | `.gemini/skills/openspec-*/SKILL.md` | `.gemini/commands/opsx/<id>.toml` |
| GitHub Copilot (`github-copilot`) | `.github/skills/openspec-*/SKILL.md` | `.github/prompts/opsx-<id>.prompt.md`\*\* |
| iFlow (`iflow`) | `.iflow/skills/openspec-*/SKILL.md` | `.iflow/commands/opsx-<id>.md` |
| Junie (`junie`) | `.junie/skills/openspec-*/SKILL.md` | `.junie/commands/opsx-<id>.md` |
| Kilo Code (`kilocode`) | `.kilocode/skills/openspec-*/SKILL.md` | `.kilocode/workflows/opsx-<id>.md` |
| Kiro (`kiro`) | `.kiro/skills/openspec-*/SKILL.md` | `.kiro/prompts/opsx-<id>.prompt.md` |
| OpenCode (`opencode`) | `.opencode/skills/openspec-*/SKILL.md` | `.opencode/commands/opsx-<id>.md` |
| Pi (`pi`) | `.pi/skills/openspec-*/SKILL.md` | `.pi/prompts/opsx-<id>.md` |
| Qoder (`qoder`) | `.qoder/skills/openspec-*/SKILL.md` | `.qoder/commands/opsx/<id>.md` |
| Qwen Code (`qwen`) | `.qwen/skills/openspec-*/SKILL.md` | `.qwen/commands/opsx-<id>.toml` |
| RooCode (`roocode`) | `.roo/skills/openspec-*/SKILL.md` | `.roo/commands/opsx-<id>.md` |
| Trae (`trae`) | `.trae/skills/openspec-*/SKILL.md` | Not generated (no command adapter; use skill-based `/openspec-*` invocations) |
| Windsurf (`windsurf`) | `.windsurf/skills/openspec-*/SKILL.md` | `.windsurf/workflows/opsx-<id>.md` |

\* Codex commands are installed in the global Codex home (`$CODEX_HOME/prompts/` if set, otherwise `~/.codex/prompts/`), not your project directory.

\*\* GitHub Copilot prompt files are recognized as custom slash commands in IDE extensions (VS Code, JetBrains, Visual Studio). Copilot CLI does not currently consume `.github/prompts/*.prompt.md` directly.

## Non-Interactive Setup

For CI/CD or scripted setup, use `--tools` (and optionally `--profile`):

```bash
# Configure specific tools
openspec init --tools claude,cursor

# Configure all supported tools
openspec init --tools all

# Skip tool configuration
openspec init --tools none

# Override profile for this init run
openspec init --profile core
```

**Available tool IDs (`--tools`):** `amazon-q`, `antigravity`, `auggie`, `bob`, `claude`, `cline`, `codex`, `codebuddy`, `continue`, `costrict`, `crush`, `cursor`, `factory`, `forgecode`, `gemini`, `github-copilot`, `iflow`, `junie`, `kilocode`, `kiro`, `opencode`, `pi`, `qoder`, `qwen`, `roocode`, `trae`, `windsurf`

## Workflow-Dependent Installation

OpenSpec installs workflow artifacts based on selected workflows:

- **Core profile (default):** `propose`, `explore`, `apply`, `archive`
- **Custom selection:** any subset of all workflow IDs:
  `propose`, `explore`, `new`, `continue`, `apply`, `ff`, `sync`, `archive`, `bulk-archive`, `verify`, `onboard`

In other words, skill/command counts are profile-dependent and delivery-dependent, not fixed.

## Generated Skill Names

When selected by profile/workflow config, OpenSpec generates these skills:

- `openspec-propose`
- `openspec-explore`
- `openspec-new-change`
- `openspec-continue-change`
- `openspec-apply-change`
- `openspec-ff-change`
- `openspec-sync-specs`
- `openspec-archive-change`
- `openspec-bulk-archive-change`
- `openspec-verify-change`
- `openspec-onboard`

See [Commands](commands.md) for command behavior and [CLI](cli.md) for `init`/`update` options.

## Related

- [CLI Reference](cli.md) — Terminal commands
- [Commands](commands.md) — Slash commands and skills
- [Getting Started](getting-started.md) — First-time setup



---

# FILE: docs/workflows.md

# Workflows

This guide covers common workflow patterns for OpenSpec and when to use each one. For basic setup, see [Getting Started](getting-started.md). For command reference, see [Commands](commands.md).

## Philosophy: Actions, Not Phases

Traditional workflows force you through phases: planning, then implementation, then done. But real work doesn't fit neatly into boxes.

OPSX takes a different approach:

```text
Traditional (phase-locked):

  PLANNING ────────► IMPLEMENTING ────────► DONE
      │                    │
      │   "Can't go back"  │
      └────────────────────┘

OPSX (fluid actions):

  proposal ──► specs ──► design ──► tasks ──► implement
```

**Key principles:**

- **Actions, not phases** - Commands are things you can do, not stages you're stuck in
- **Dependencies are enablers** - They show what's possible, not what's required next

> **Customization:** OPSX workflows are driven by schemas that define artifact sequences. See [Customization](customization.md) for details on creating custom schemas.

## Two Modes

### Default Quick Path (`core` profile)

New installs default to `core`, which provides:
- `/opsx:propose`
- `/opsx:explore`
- `/opsx:apply`
- `/opsx:archive`

Typical flow:

```text
/opsx:propose ──► /opsx:apply ──► /opsx:archive
```

### Expanded/Full Workflow (custom selection)

If you want explicit scaffold-and-build commands (`/opsx:new`, `/opsx:continue`, `/opsx:ff`, `/opsx:verify`, `/opsx:sync`, `/opsx:bulk-archive`, `/opsx:onboard`), enable them with:

```bash
openspec config profile
openspec update
```

## Workflow Patterns (Expanded Mode)

### Quick Feature

When you know what you want to build and just need to execute:

```text
/opsx:new ──► /opsx:ff ──► /opsx:apply ──► /opsx:verify ──► /opsx:archive
```

**Example conversation:**

```text
You: /opsx:new add-logout-button

AI:  Created openspec/changes/add-logout-button/
     Ready to create: proposal

You: /opsx:ff

AI:  Creating all planning artifacts...
     ✓ proposal.md
     ✓ specs/
     ✓ design.md
     ✓ tasks.md
     Ready for implementation!

You: /opsx:apply

AI:  Working through tasks...
     ✓ Added logout button to header
     ✓ Implemented session clearing
     ✓ Added confirmation dialog
     All tasks complete!

You: /opsx:archive

AI:  ✓ Merged specs
     ✓ Archived change
```

**Best for:** Small to medium features, bug fixes, straightforward changes.

### Exploratory

When requirements are unclear or you need to investigate first:

```text
/opsx:explore ──► /opsx:new ──► /opsx:continue ──► ... ──► /opsx:apply
```

**Example conversation:**

```text
You: /opsx:explore

AI:  What would you like to explore?

You: I want to improve page load performance but I'm not sure
     where the bottlenecks are.

AI:  Let me help investigate...
     [Analyzes bundle sizes, identifies slow queries, reviews
     component render patterns]

     I found three main bottlenecks:
     1. Large unoptimized images
     2. Synchronous data fetching in ProductList
     3. Re-renders from context changes

     Which would you like to address first?

You: Let's tackle the data fetching issue.

You: /opsx:new optimize-product-list-fetching

AI:  Created change. Ready to create: proposal

You: /opsx:continue

AI:  Creating proposal based on our exploration...
     [Writes proposal incorporating investigation insights]

     Ready to create: specs, design
     Which would you like next?

You: /opsx:continue

AI:  Creating specs...
```

**Best for:** Performance optimization, debugging, architectural decisions, unclear requirements.

### Parallel Changes

Work on multiple changes at once:

```text
Change A: /opsx:new ──► /opsx:ff ──► /opsx:apply (in progress)
                                         │
                                    context switch
                                         │
Change B: /opsx:new ──► /opsx:ff ──────► /opsx:apply
```

**Example conversation:**

```text
You: I'm working on add-dark-mode but got pulled into a bug fix

You: /opsx:new fix-login-redirect

AI:  Created openspec/changes/fix-login-redirect/

You: /opsx:ff

AI:  ✓ Created planning artifacts

You: /opsx:apply

AI:  Working on fix-login-redirect...
     [Implements the fix]
     All tasks complete!

You: /opsx:archive

AI:  ✓ Archived fix-login-redirect

You: Let's get back to dark mode

You: /opsx:apply add-dark-mode

AI:  Resuming add-dark-mode...
     Picking up at task 2.3: Update Header...
```

**Best for:** Parallel work streams, urgent interrupts, team collaboration.

When you have multiple completed changes, use `/opsx:bulk-archive`:

```text
You: /opsx:bulk-archive

AI:  Found 3 completed changes:
     - add-dark-mode (all tasks done)
     - fix-login-redirect (all tasks done)
     - update-footer (all tasks done)

     Checking for spec conflicts...
     ⚠ add-dark-mode and update-footer both touch specs/ui/

     Inspecting codebase to resolve...
     Both changes are implemented. Will apply in chronological order.

     Archive all 3 changes?

You: Yes

AI:  ✓ Archived add-dark-mode
     ✓ Archived fix-login-redirect
     ✓ Archived update-footer
     Specs merged in order: add-dark-mode → update-footer
```

Bulk archive detects when multiple changes touch the same specs and resolves conflicts by checking what's actually implemented.

### Completing a Change

The recommended completion flow:

```text
/opsx:apply ──► /opsx:verify ──► /opsx:archive
                    │                 │
              validates          prompts to sync
              implementation     if needed
```

#### Verify: Check Your Work

`/opsx:verify` validates implementation against your artifacts across three dimensions:

```text
You: /opsx:verify

AI:  Verifying add-auth...

     COMPLETENESS
     ✓ All 12 tasks in tasks.md are checked
     ✓ All requirements in specs have corresponding code
     ⚠ Scenario "Session timeout after inactivity" not tested

     CORRECTNESS
     ✓ Implementation matches spec intent
     ✓ Edge cases from scenarios are handled
     ✓ Error states match spec definitions

     COHERENCE
     ✓ Design decisions reflected in code structure
     ✓ Naming conventions consistent with design.md
     ⚠ Design mentions "event-driven" but implementation uses polling

     SUMMARY
     ─────────────────────────────
     Critical issues: 0
     Warnings: 2
     Ready to archive: Yes (with warnings)

     Recommendations:
     1. Add test for session timeout scenario
     2. Consider refactoring to event-driven as designed, or update design.md
```

**What verify checks:**

| Dimension | What it validates |
|-----------|------------------|
| Completeness | All tasks done, all requirements implemented, scenarios covered |
| Correctness | Implementation matches spec intent, edge cases handled |
| Coherence | Design decisions reflected in code, patterns consistent |

Verify won't block archive, but it surfaces issues you might want to address first.

#### Archive: Finalize the Change

`/opsx:archive` completes the change and moves it to the archive:

```text
You: /opsx:archive

AI:  Archiving add-auth...

     Artifact status:
     ✓ proposal.md exists
     ✓ specs/ exists
     ✓ design.md exists
     ✓ tasks.md exists (12/12 tasks complete)

     Delta specs: Not yet synced to main
     → Would you like to sync now?

You: Yes

AI:  ✓ Synced specs to openspec/specs/auth/spec.md
     ✓ Moved to openspec/changes/archive/2025-01-24-add-auth/

     Change archived successfully.
```

Archive will prompt if specs aren't synced. It won't block on incomplete tasks, but it will warn you.

## When to Use What

### `/opsx:ff` vs `/opsx:continue`

| Situation | Use |
|-----------|-----|
| Clear requirements, ready to build | `/opsx:ff` |
| Exploring, want to review each step | `/opsx:continue` |
| Want to iterate on proposal before specs | `/opsx:continue` |
| Time pressure, need to move fast | `/opsx:ff` |
| Complex change, want control | `/opsx:continue` |

**Rule of thumb:** If you can describe the full scope upfront, use `/opsx:ff`. If you're figuring it out as you go, use `/opsx:continue`.

### When to Update vs Start Fresh

A common question: when is updating an existing change okay, and when should you start a new one?

**Update the existing change when:**

- Same intent, refined execution
- Scope narrows (MVP first, rest later)
- Learning-driven corrections (codebase isn't what you expected)
- Design tweaks based on implementation discoveries

**Start a new change when:**

- Intent fundamentally changed
- Scope exploded to different work entirely
- Original change can be marked "done" standalone
- Patches would confuse more than clarify

```text
                     ┌─────────────────────────────────────┐
                     │     Is this the same work?          │
                     └──────────────┬──────────────────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 ▼                  ▼                  ▼
          Same intent?      >50% overlap?      Can original
          Same problem?     Same scope?        be "done" without
                 │                  │          these changes?
                 │                  │                  │
       ┌────────┴────────┐  ┌──────┴──────┐   ┌───────┴───────┐
       │                 │  │             │   │               │
      YES               NO YES           NO  NO              YES
       │                 │  │             │   │               │
       ▼                 ▼  ▼             ▼   ▼               ▼
    UPDATE            NEW  UPDATE       NEW  UPDATE          NEW
```

**Example: "Add dark mode"**

- "Need to also support custom themes" → New change (scope exploded)
- "System preference detection is harder than expected" → Update (same intent)
- "Let's ship toggle first, add preferences later" → Update then archive, then new change

## Best Practices

### Keep Changes Focused

One logical unit of work per change. If you're doing "add feature X and also refactor Y", consider two separate changes.

**Why it matters:**
- Easier to review and understand
- Cleaner archive history
- Can ship independently
- Simpler rollback if needed

### Use `/opsx:explore` for Unclear Requirements

Before committing to a change, explore the problem space:

```text
You: /opsx:explore

AI:  What would you like to explore?

You: How should we handle rate limiting for our API?

AI:  Let me investigate your current setup and options...
     [Researches codebase, considers patterns]

     I see three approaches we could take:
     1. Middleware-based (simple, per-endpoint)
     2. Redis-backed (scalable, shared state)
     3. Token bucket per user (fair, complex)

     Your current stack suggests #1 or #2. What's your scale?
```

Exploration clarifies thinking before you create artifacts.

### Verify Before Archiving

Use `/opsx:verify` to check implementation matches artifacts:

```text
You: /opsx:verify

AI:  Verifying add-dark-mode...

     ✓ All tasks in tasks.md are checked
     ✓ Requirements in specs have corresponding code
     ✓ Design decisions are reflected in implementation

     Ready to archive!
```

Catches mismatches before you close out the change.

### Name Changes Clearly

Good names make `openspec list` useful:

```text
Good:                          Avoid:
add-dark-mode                  feature-1
fix-login-redirect             update
optimize-product-query         changes
implement-2fa                  wip
```

## Command Quick Reference

For full command details and options, see [Commands](commands.md).

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/opsx:propose` | Create change + planning artifacts | Fast default path (`core` profile) |
| `/opsx:explore` | Think through ideas | Unclear requirements, investigation |
| `/opsx:new` | Start a change scaffold | Expanded mode, explicit artifact control |
| `/opsx:continue` | Create next artifact | Expanded mode, step-by-step artifact creation |
| `/opsx:ff` | Create all planning artifacts | Expanded mode, clear scope |
| `/opsx:apply` | Implement tasks | Ready to write code |
| `/opsx:verify` | Validate implementation | Expanded mode, before archiving |
| `/opsx:sync` | Merge delta specs | Expanded mode, optional |
| `/opsx:archive` | Complete the change | All work finished |
| `/opsx:bulk-archive` | Archive multiple changes | Expanded mode, parallel work |

## Next Steps

- [Commands](commands.md) - Full command reference with options
- [Concepts](concepts.md) - Deep dive into specs, artifacts, and schemas
- [Customization](customization.md) - Create custom workflows



---

# FILE: openspec-parallel-merge-plan.md

# OpenSpec Parallel Delta Remediation Plan

## Problem Summary
- Active changes apply requirement-level replacements when archiving. When two changes touch the same requirement, the second archive overwrites the first and silently drops scenarios (e.g., Windsurf vs. Kilo Code slash command updates).
- The archive workflow (`src/core/archive.ts:191` and `src/core/archive.ts:501`) rebuilds main specs by replacing entire requirement blocks with the content contained in the change delta. The delta format (`src/core/parsers/requirement-blocks.ts:113`) has no notion of base versions or scenario-level operations.
- The tooling cannot detect divergence between the change author’s starting point and the live spec, so parallel development corrupts the source of truth without warning.

## Observed Failure Mode
- Change A (`add-windsurf-workflows`) adds a Windsurf scenario under `Slash Command Configuration`.
- Change B (`add-kilocode-workflows`) adds a Kilo Code scenario to the same requirement, starting from the pre-Windsurf spec.
- After Change A archives, the main spec contains both scenarios.
- When Change B archives, `buildUpdatedSpec` sees a `MODIFIED` block for `Slash Command Configuration` and replaces the requirement with the four-scenario variant shipped in that change. Because that file never learned about Windsurf, the Windsurf scenario disappears.
- There is no warning, diff, or conflict indicator—the archive completes successfully, and the source-of-truth spec now omits a shipped scenario.

## Root Causes
1. **Replace-only semantics.** `buildUpdatedSpec` performs hash-map substitution of requirement blocks and cannot merge or compare individual scenarios (`src/core/archive.ts:455`-`src/core/archive.ts:526`).
2. **Missing base fingerprint.** Changes do not persist the requirement content they were authored against, so the archive step cannot tell if the live spec diverged.
3. **Single-level granularity.** The delta language only understands requirements. Even if we introduced scenario-level parsing, we would still lose sibling edits without an accompanying merge strategy.
4. **Lack of conflict UX.** The CLI never forces contributors to reconcile parallel updates. There is no equivalent of `git merge`, `git rebase`, or conflict markers.

## Design Objectives
- Preserve every approved scenario regardless of archive order.
- Detect and block speculative archives when the live spec diverges from the author’s base.
- Provide a deterministic, reviewable conflict resolution flow that mirrors source-control best practices.
- Keep the authoring experience ergonomic: deltas should remain human-editable markdown.
- Support incremental adoption so existing repositories can roll forward without breaking active work.

## Proposed Fix: Layered Remediation

### Phase 0 – Stop the Bleeding (Detection & Guardrails)
1. **Persist requirement fingerprints alongside each change.**
   - When scaffolding or validating a change, capture the current requirement body for every `MODIFIED`/`REMOVED`/`RENAMED` entry and write it to `changes/<id>/meta.json`.
   - Store a stable hash (e.g., SHA-256) of the base requirement content and the raw text itself for later merges.
2. **Validate fingerprints during archive.**
   - Before `buildUpdatedSpec` mutates specs, recompute the requirement hash from the live spec.
   - If the hash differs from the stored base, abort and instruct the user to rebase. This makes the destructive path impossible.
3. **Surface intent in CLI output.**
   - Show which requirements are stale, when they diverged, and which change last touched them.
4. **Document interim manual mitigation.**
   - Update `openspec/AGENTS.md` and docs so contributors know to rerun `openspec change sync` (see Phase 1) whenever another change lands.

_Outcome:_ We prevent data loss immediately while we work on a richer merge story.

### Phase 1 – Add a Rebase Workflow (Author-Side Merge)
1. **Introduce `openspec change sync <id>` (or `rebase`).**
   - Reads the stored base snapshot, the current spec, and the author’s delta.
   - Performs a 3-way merge per requirement. A naive diff3 on markdown lines is acceptable initially because we already operate on requirement-sized chunks.
   - If the merge is clean, rewrite the `MODIFIED` block with the merged text and refresh the stored fingerprint.
   - On conflict, write conflict markers inside the change delta (similar to Git) and require the author to hand-edit before re-running validation.
2. **Enrich validator messages.**
   - `openspec validate` should flag unresolved conflict markers or fingerprint mismatches so errors appear early in the workflow.
3. **Optional:** Offer a `--rewrite-scenarios` helper that merges bullet lists of scenarios to reduce manual editing noise.

_Outcome:_ Contributors can safely reconcile their work with the latest spec before archiving, restoring true parallel development.

### Phase 2 – Increase Delta Granularity
1. **Extend the delta language with scenario-level directives.**
   - Allow `## MODIFIED Requirements` + `## ADDED Scenarios` / `## MODIFIED Scenarios` sections nested under the requirement header.
   - Backed by stable scenario identifiers (explicit IDs or generated hashes) stored in `meta.json`. This lets the system reason about individual scenarios.
2. **Teach the parser to understand nested operations.**
   - Update `parseDeltaSpec` to emit scenario-level operations in addition to requirement blocks.
   - Update `buildUpdatedSpec` (or its replacement) to merge scenario lists, preserving order while inserting new entries in a deterministic fashion.
3. **Automate migration.**
   - Provide a one-time command that inspects each existing spec, injects scenario IDs, and rewrites in-flight change deltas into the richer format.
4. **Continue to rely on the Phase 1 rebase flow for conflicts when two changes edit the same scenario body or description.**

_Outcome:_ Most concurrent updates become commutative, drastically reducing the odds of human merges.

### Phase 3 – Structured Spec Graph (Long-Term)
1. **Define stable requirement IDs.**
   - Embed `Requirement ID: <uuid>` markers in specs so renames and moves are trackable.
   - This enables future features like cross-capability references and better diff visualizations.
2. **Model spec edits as operations over an AST.**
   - Build an intermediate representation (IR) for requirements/scenarios/metadata.
   - Use operational transforms or CRDT-like techniques to guarantee merge associativity.
3. **Integrate with Git directly.**
   - Offer optional `openspec branch` scaffolding that aligns spec changes with Git branches, letting teams leverage Git’s conflict editor for the markdown IR.

_Outcome:_ OpenSpec graduates from replace-based updates to a resilient, intent-preserving spec management platform.

## Migration & Product Impacts
- **Backfill metadata:** add hashes for all active changes and the current main specs during the initial rollout.
- **CLI UX:** new commands (`change sync`, enhanced `archive`) require documentation, help text, and release notes.
- **Docs & AGENTS updates:** reinforce the rebase workflow and explain conflict resolution to AI assistants.
- **Testing:** introduce fixtures covering divergent requirement fingerprints and merge resolution logic.
- **Telemetry (optional):** log fingerprint mismatches so we can see how often teams hit conflicts after the rollout.

## Open Questions / Risks
- How should we order scenarios when multiple changes insert at different points? (Consider optional `position` metadata or deterministic alphabetical fallbacks.)
- What is the graceful failure mode if contributors delete the `meta.json` file? (CLI should recreate fingerprints on demand.)
- Do we need to support offline authors who cannot easily re-run the sync command before archiving? (Potential `--accept-outdated` escape hatch for emergencies.)
- How will archived historical changes be handled? We may need a migration script to embed fingerprints retroactively so re-validation succeeds.

## Immediate Next Steps
1. Prototype fingerprint capture during `openspec change validate` and block archive on mismatches.
2. Ship `openspec change sync` with line-based diff3 merging and conflict markers.
3. Update contributor docs and AI instructions to mandate running `sync` before archiving.
4. Plan the scenario-level delta extension and migration path as a follow-up RFC.



---

# FILE: openspec/changes/add-change-stacking-awareness/specs/change-creation/spec.md

## ADDED Requirements

### Requirement: Stack Metadata Scaffolding
Change creation workflows SHALL support optional dependency metadata for new or split changes.

#### Scenario: Create change with stack metadata
- **WHEN** a change is created with stack metadata inputs
- **THEN** creation SHALL persist metadata fields in change configuration
- **AND** persisted metadata SHALL be validated against change metadata schema rules

#### Scenario: Split-generated child metadata
- **WHEN** child changes are generated from a split workflow
- **THEN** each child SHALL include a `parent` link to the source change
- **AND** SHALL include dependency metadata needed for deterministic sequencing




---

# FILE: openspec/changes/add-change-stacking-awareness/specs/change-stacking-workflow/spec.md

## ADDED Requirements

### Requirement: Stack Metadata Model
The system SHALL support optional metadata on active changes to express sequencing and decomposition relationships.

#### Scenario: Optional stack metadata is present
- **WHEN** a change includes stack metadata fields
- **THEN** the system SHALL parse and expose `dependsOn`, `provides`, `requires`, `touches`, and `parent`
- **AND** validation SHALL enforce normalized field shapes and value types (`dependsOn`/`provides`/`requires`/`touches` as string arrays, `parent` as string when present)

#### Scenario: Backward compatibility without stack metadata
- **WHEN** a change does not include stack metadata
- **THEN** existing behavior SHALL continue without migration steps
- **AND** validation SHALL not fail solely because stack metadata is absent

### Requirement: Change Dependency Graph
The system SHALL provide dependency-aware ordering for active changes.

#### Scenario: Build dependency order
- **WHEN** users request stack planning output
- **THEN** the system SHALL compute a dependency graph across active changes
- **AND** SHALL return a deterministic topological order for unblocked changes

#### Scenario: Tie-breaking within the same dependency depth
- **WHEN** multiple unblocked changes share the same topological dependency depth
- **THEN** ordering SHALL break ties lexicographically by change ID
- **AND** repeated runs over the same input SHALL return the same order

#### Scenario: Dependency cycle detection
- **WHEN** active changes contain a dependency cycle
- **THEN** validation SHALL fail with cycle details before archive or sequencing actions proceed
- **AND** output SHALL include actionable guidance to break the cycle

### Requirement: Capability marker and overlap semantics
The system SHALL treat capability markers as validation contracts and `touches` as advisory overlap signals.

#### Scenario: Required capability provided by an active change
- **WHEN** change B declares `requires` marker `X`
- **AND** active change A declares `provides` marker `X`
- **THEN** validation SHALL require B to declare an explicit ordering edge in `dependsOn` to at least one active provider of `X`
- **AND** validation SHALL fail if no explicit dependency is declared

#### Scenario: Requires marker without active provider
- **WHEN** a change declares a `requires` marker
- **AND** no active change declares the corresponding `provides` marker
- **THEN** validation SHALL NOT infer an implicit dependency edge
- **AND** ordering SHALL continue to be determined solely by explicit `dependsOn` relationships

#### Scenario: Requires marker satisfied by archived history
- **WHEN** a change declares a `requires` marker
- **AND** no active change provides that marker
- **AND** at least one archived change in history provides that marker
- **THEN** validation SHALL NOT warn solely about missing provider
- **AND** SHALL continue to use explicit `dependsOn` for active ordering

#### Scenario: Requires marker missing in full history
- **WHEN** a change declares a `requires` marker
- **AND** no active or archived change in history provides that marker
- **THEN** validation SHALL emit a non-blocking warning naming the change and missing marker
- **AND** SHALL NOT infer an implicit dependency edge

#### Scenario: Overlap warning for shared touches
- **WHEN** multiple active changes declare overlapping `touches` values
- **THEN** validation SHALL emit a warning listing the overlapping changes and touched areas
- **AND** validation SHALL NOT fail solely on overlap



---

# FILE: openspec/changes/add-change-stacking-awareness/specs/cli-change/spec.md

## ADDED Requirements

### Requirement: Stack Planning Commands
The change CLI SHALL provide commands for dependency-aware sequencing of active changes.

#### Scenario: Show dependency graph
- **WHEN** a user runs `openspec change graph`
- **THEN** the CLI SHALL display dependency relationships for active changes
- **AND** SHALL include a deterministic recommended order for execution

#### Scenario: Show next unblocked changes
- **WHEN** a user runs `openspec change next`
- **THEN** the CLI SHALL list changes that are not blocked by unresolved dependencies
- **AND** SHALL use deterministic tie-breaking when multiple options are available

### Requirement: Split Large Change Scaffolding
The change CLI SHALL support scaffolding child slices from an existing large change.

#### Scenario: Split command scaffolds child changes
- **WHEN** a user runs `openspec change split <change-id>`
- **THEN** the CLI SHALL create child change directories with proposal/tasks stubs
- **AND** generated metadata SHALL include `parent` and dependency links back to the source change

#### Scenario: Re-running split on an already-split change
- **WHEN** a user runs `openspec change split <change-id>` for a parent whose generated child directories already exist
- **THEN** the CLI SHALL fail with a deterministic, actionable error
- **AND** SHALL NOT mutate existing child change content unless an explicit overwrite mode is requested



---

# FILE: openspec/changes/add-change-stacking-awareness/specs/openspec-conventions/spec.md

## ADDED Requirements

### Requirement: Stack-Aware Change Planning Conventions
OpenSpec conventions SHALL define optional metadata fields for sequencing and decomposition across concurrent changes.

#### Scenario: Declaring change dependencies
- **WHEN** authors need to sequence related changes
- **THEN** conventions SHALL define how to declare dependencies and provided/required capability markers
- **AND** validation guidance SHALL distinguish hard blockers from soft overlap warnings

#### Scenario: Dependency source of truth during migration
- **WHEN** both stack metadata and `openspec/changes/IMPLEMENTATION_ORDER.md` are present
- **THEN** conventions SHALL treat per-change stack metadata as the normative dependency source
- **AND** `IMPLEMENTATION_ORDER.md` SHALL be treated as optional narrative guidance

#### Scenario: Explicit ordering remains required for capability markers
- **WHEN** authors use `provides` and `requires` markers to describe capability contracts
- **THEN** conventions SHALL require explicit `dependsOn` edges for ordering relationships
- **AND** conventions SHALL prohibit treating `requires` as an implicit dependency edge

#### Scenario: Declaring advisory overlap via touches
- **WHEN** a change may affect capability/spec areas shared by concurrent changes without requiring ordering
- **THEN** conventions SHALL allow authors to declare `touches` with advisory area identifiers (for example capability IDs, spec area names, or paths)
- **AND** tooling SHALL treat `touches` as informational only (no implicit dependency edge, non-blocking validation signal)

#### Scenario: Declaring parent-child split structure
- **WHEN** a large change is decomposed into smaller slices
- **THEN** conventions SHALL define parent-child metadata and expected ordering semantics
- **AND** docs SHALL describe when to split versus keep a single change



---

# FILE: openspec/changes/add-global-install-scope/specs/ai-tool-paths/spec.md

## MODIFIED Requirements

### Requirement: AIToolOption skillsDir field
The `AIToolOption` interface SHALL include scope support metadata in addition to path metadata.

#### Scenario: Scope support metadata present
- **WHEN** a tool entry is defined in `AI_TOOLS`
- **THEN** it MAY declare supported install scopes for skills and commands
- **AND** this metadata SHALL be used for effective scope resolution

#### Scenario: Scope support metadata absent
- **WHEN** a tool entry in `AI_TOOLS` omits scope support metadata for a surface
- **THEN** resolver behavior SHALL default that surface to project-only support
- **AND** effective scope resolution SHALL apply normal preferred/fallback rules against that default

### Requirement: Path configuration for supported tools
Path metadata SHALL support both project and global install targets via resolver logic.

#### Scenario: Project scope path
- **WHEN** effective scope is `project` for skills
- **THEN** `skillsDir` SHALL be treated as a tool-specific container path under project root
- **AND** managed skill artifacts SHALL be written under `<projectRoot>/<skillsDir>/skills/`
- **AND** tool definitions SHALL set `skillsDir` accordingly (for example `.openspec` -> `.openspec/skills/`)

#### Scenario: Global scope path
- **WHEN** effective scope is `global` for a supported tool/surface
- **THEN** paths SHALL resolve to tool-specific global directories
- **AND** environment overrides (for example `CODEX_HOME`) SHALL be respected where applicable

#### Scenario: Windows global path resolution for Codex commands
- **WHEN** effective scope is `global`
- **AND** tool is Codex
- **AND** platform is Windows
- **THEN** command targets SHALL resolve to `%CODEX_HOME%\prompts` when `CODEX_HOME` is set
- **AND** SHALL otherwise resolve to `%USERPROFILE%\.codex\prompts`



---

# FILE: openspec/changes/add-global-install-scope/specs/cli-config/spec.md

## ADDED Requirements

### Requirement: Install scope configuration via profile flow
The config profile workflow SHALL allow users to configure install scope preference.

#### Scenario: Interactive profile includes install scope
- **WHEN** user runs `openspec config profile`
- **THEN** the interactive flow SHALL include install scope selection with values `global` and `project`
- **AND** the currently configured value SHALL be pre-selected

#### Scenario: Save install scope
- **WHEN** user confirms config profile changes
- **THEN** selected install scope SHALL be saved to global config

### Requirement: Install scope visibility in config output
The config command SHALL display install scope preference in human-readable output.

#### Scenario: Config list shows install scope
- **WHEN** user runs `openspec config list`
- **THEN** output SHALL include current install scope value
- **AND** indicate whether value is default or explicit



---

# FILE: openspec/changes/add-global-install-scope/specs/cli-init/spec.md

## ADDED Requirements

### Requirement: Init install scope selection
The init command SHALL support install scope selection for generated artifacts.

#### Scenario: Scope defaults to global
- **WHEN** user runs `openspec init` without explicit scope override
- **THEN** init SHALL use global config install scope
- **AND** if unset, SHALL resolve migration-aware default (`global` for newly created configs, `project` for legacy schema-evolved configs)

#### Scenario: Scope override via flag
- **WHEN** user runs `openspec init --scope project`
- **THEN** init SHALL use `project` as preferred scope for that run
- **AND** SHALL NOT mutate persisted global config unless user explicitly changes config

### Requirement: Init uses effective scope resolution
The init command SHALL resolve effective scope per tool surface before generating files.

#### Scenario: Effective scope with fallback
- **WHEN** selected tool/surface does not support preferred scope
- **AND** supports alternate scope
- **THEN** init SHALL generate files at alternate effective scope
- **AND** SHALL display fallback note in summary

#### Scenario: Unsupported scope selection
- **WHEN** selected tool/surface supports neither preferred nor alternate scope
- **THEN** init SHALL fail before writing files
- **AND** SHALL provide clear error guidance



---

# FILE: openspec/changes/add-global-install-scope/specs/cli-update/spec.md

## ADDED Requirements

### Requirement: Update install scope selection
The update command SHALL support install scope selection for sync operations.

#### Scenario: Scope defaults to global config value
- **WHEN** user runs `openspec update` without explicit scope override
- **THEN** update SHALL use configured install scope
- **AND** if unset, SHALL resolve migration-aware default (`global` for newly created configs, `project` for legacy schema-evolved configs)

#### Scenario: Scope override via flag
- **WHEN** user runs `openspec update --scope project`
- **THEN** update SHALL use `project` as preferred scope for that run

### Requirement: Scope-aware sync and drift detection
The update command SHALL evaluate configured state and drift using effective scoped paths.

#### Scenario: Scoped drift detection
- **WHEN** update evaluates whether tools are up-to-date
- **THEN** it SHALL inspect files at effective scoped targets for each tool/surface
- **AND** SHALL compare current resolved scope against last successful effective scope for each tool/surface
- **AND** SHALL treat a difference as sync-required drift

#### Scenario: Scope fallback during update
- **WHEN** preferred scope is unsupported for a configured tool/surface
- **AND** alternate scope is supported
- **THEN** update SHALL apply fallback scope resolution
- **AND** SHALL report fallback in output

#### Scenario: Unsupported scope during update
- **WHEN** configured tool/surface supports neither preferred nor alternate scope
- **THEN** scope support SHALL be validated for all configured tools/surfaces before any write
- **AND** update SHALL fail without performing file writes when incompatibilities are detected
- **AND** SHALL report incompatible tools with remediation steps



---

# FILE: openspec/changes/add-global-install-scope/specs/command-generation/spec.md

## MODIFIED Requirements

### Requirement: ToolCommandAdapter interface
The system SHALL provide install-context-aware command path resolution.

#### Scenario: Adapter interface structure
- **WHEN** implementing a tool adapter
- **THEN** command file path resolution SHALL receive install context (including effective scope and environment context)
- **AND** SHALL return the effective command output path for that context

#### Scenario: Codex global path remains supported
- **WHEN** resolving Codex command paths in global scope
- **THEN** the adapter SHALL target `$CODEX_HOME/prompts` when `CODEX_HOME` is set
- **AND** SHALL otherwise target `~/.codex/prompts`

### Requirement: Command generator function
The command generator SHALL pass install context into adapter path resolution for all generated commands.

#### Scenario: Scoped command generation
- **WHEN** generating commands for a tool with a resolved effective scope
- **THEN** generated command paths SHALL match that effective scope
- **AND** the formatted command body/frontmatter behavior SHALL remain tool-specific and unchanged



---

# FILE: openspec/changes/add-global-install-scope/specs/global-config/spec.md

## ADDED Requirements

### Requirement: Install scope field in global config
The global config schema SHALL include install scope preference.

#### Scenario: Config shape supports install scope
- **WHEN** reading or writing global config
- **THEN** config SHALL support `installScope` with allowed values `global` and `project`

#### Scenario: Schema evolution default
- **WHEN** loading legacy config without `installScope`
- **THEN** the system SHALL preserve schema compatibility without mutating the file
- **AND** effective install scope SHALL resolve to `project` until user explicitly sets `installScope`
- **AND** preserve all other existing fields

#### Scenario: New config default
- **WHEN** creating a new global config
- **THEN** the system SHALL persist `installScope: global` by default
- **AND** users MAY switch to `project` explicitly

#### Scenario: Invalid install scope value
- **WHEN** config validation receives an invalid install scope value
- **THEN** the value SHALL be rejected
- **AND** the system SHALL preserve the existing valid configuration



---

# FILE: openspec/changes/add-global-install-scope/specs/installation-scope/spec.md

## Purpose

Define the install scope model for OpenSpec-generated skills and commands, including scope preference, effective scope resolution, and fallback/error semantics.

## ADDED Requirements

### Requirement: Install scope preference model
The system SHALL support a user-level install scope preference with values `global` and `project`.

#### Scenario: Default install scope
- **WHEN** install scope is not explicitly configured
- **THEN** the system SHALL resolve a migration-aware default:
- **AND** use `global` for newly created configs
- **AND** use `project` for legacy schema-evolved configs until explicit migration

#### Scenario: Explicit install scope
- **WHEN** user configures install scope to `project`
- **THEN** generation and update flows SHALL use `project` as the preferred scope

### Requirement: Effective scope resolution by tool surface
The system SHALL compute effective scope per tool surface (skills, commands) based on preferred scope and tool capability support.

#### Scenario: Preferred scope is supported
- **WHEN** preferred scope is supported for a tool surface
- **THEN** the system SHALL use that scope as the effective scope

#### Scenario: Preferred scope is unsupported but alternate is supported
- **WHEN** preferred scope is not supported for a tool surface
- **AND** the alternate scope is supported
- **THEN** the system SHALL use the alternate scope as effective scope
- **AND** SHALL record a fallback note for user-facing output

#### Scenario: No supported scope
- **WHEN** neither `global` nor `project` is supported for a tool surface
- **THEN** the command SHALL fail before writing files
- **AND** SHALL display actionable remediation

### Requirement: Effective scope reporting
The system SHALL report effective scope decisions in command output when they differ from the preferred scope.

#### Scenario: Fallback reporting
- **WHEN** fallback resolution occurs for any selected/configured tool surface
- **THEN** init/update summaries SHALL include effective scope notes per affected tool

### Requirement: Cross-platform path behavior
Install scope resolution SHALL produce platform-correct target paths.

#### Scenario: Global scope path on Windows
- **WHEN** effective scope is `global`
- **AND** the command runs on Windows
- **THEN** resolved target paths SHALL use Windows path conventions and separators
- **AND** SHALL NOT reuse POSIX-style home-relative defaults directly

### Requirement: Cleanup safety for scope transitions
Scope transitions SHALL update new targets first and clean old managed targets safely.

#### Scenario: Automatic cleanup for managed files on scope change
- **WHEN** update or init applies a scope transition for a configured tool/surface
- **THEN** the system SHALL write new artifacts in the new effective scope before cleanup
- **AND** SHALL automatically remove only OpenSpec-managed files in the previous effective scope

#### Scenario: Cleanup scope boundaries
- **WHEN** cleanup runs after a scope transition
- **THEN** the system SHALL leave non-managed files untouched
- **AND** SHALL limit removal scope to the affected tool/workflow-managed paths

#### Scenario: Cleanup failure after successful writes
- **WHEN** new artifacts were written successfully in the new scope
- **AND** cleanup of old managed targets fails
- **THEN** the command SHALL report failure with leftover cleanup paths
- **AND** SHALL NOT rollback successfully written new-scope artifacts



---

# FILE: openspec/changes/add-qa-smoke-harness/specs/developer-qa-workflow/spec.md

## ADDED Requirements

### Requirement: Makefile QA Entry Point

The repository SHALL provide Makefile targets as the primary developer entrypoint for CLI QA flows.

#### Scenario: Default QA target runs smoke suite

- **WHEN** a developer runs `make qa`
- **THEN** the command SHALL execute the non-interactive smoke suite
- **AND** exit with status code 0 only when all smoke scenarios pass

#### Scenario: Smoke suite target is directly invokable

- **WHEN** a developer runs `make qa-smoke`
- **THEN** the command SHALL execute the same smoke suite used by `make qa`
- **AND** return a non-zero exit code on assertion failure

#### Scenario: Interactive checklist target exists

- **WHEN** a developer runs `make qa-interactive`
- **THEN** the command SHALL provide the manual interactive verification checklist
- **AND** SHALL NOT run interactive prompt automation by default

### Requirement: Sandboxed Smoke Scenario Runner

The smoke suite SHALL run CLI scenarios in isolated sandboxes so tests are repeatable and do not depend on machine-global state.

#### Scenario: Scenario execution is environment-isolated

- **WHEN** a smoke scenario runs
- **THEN** it SHALL use temporary values for `HOME`, `XDG_CONFIG_HOME`, `XDG_DATA_HOME`, and `CODEX_HOME`
- **AND** global config from the host machine SHALL NOT affect scenario outcomes

#### Scenario: Scenario artifacts are captured for review

- **WHEN** a smoke scenario completes
- **THEN** the runner SHALL capture command output and exit status
- **AND** SHALL capture enough filesystem state to inspect before/after behavior

#### Scenario: High-risk workflow coverage exists

- **WHEN** the smoke suite executes
- **THEN** it SHALL include scenarios covering profile/delivery behavior and migration-sensitive flows
- **AND** include at least:
  - non-interactive tool detection
  - migration when profile is unset
  - delivery cleanup (`both -> skills`, `both -> commands`)
  - commands-only update detection



---

# FILE: openspec/changes/add-tool-command-surface-capabilities/specs/cli-init/spec.md

## ADDED Requirements

### Requirement: Command surface capability resolution
The init command SHALL resolve each selected tool's command surface using explicit metadata first, then deterministic inference.

#### Scenario: Explicit command surface override
- **WHEN** a tool declares an explicit command-surface capability
- **THEN** init SHALL use that explicit capability
- **AND** SHALL NOT override it based on adapter presence

#### Scenario: Inferred command surface from adapter presence
- **WHEN** a tool does not declare an explicit command-surface capability
- **AND** a command adapter is registered for the tool
- **THEN** init SHALL infer `adapter` as the command surface

#### Scenario: Inferred command surface for skills-only tool
- **WHEN** a tool does not declare an explicit command-surface capability
- **AND** no command adapter is registered for the tool
- **AND** the tool has a configured `skillsDir`
- **THEN** init SHALL infer `skills-invocable` as the command surface

#### Scenario: Inferred command surface without adapter or skills
- **WHEN** a tool does not declare an explicit command-surface capability
- **AND** no command adapter is registered for the tool
- **AND** the tool has no `skillsDir`
- **THEN** init SHALL infer `none` as the command surface

### Requirement: Delivery compatibility by tool command surface
The init command SHALL apply delivery settings using each tool's command surface capability, not adapter presence alone.

#### Scenario: Both delivery for adapter-backed tool
- **WHEN** user runs `openspec init` with a selected tool that has a command adapter
- **AND** delivery is set to `both`
- **THEN** the system SHALL generate command files for active workflows using that adapter
- **AND** SHALL generate or refresh managed skills when the tool has `skillsDir`

#### Scenario: Both delivery for skills-invocable tool
- **WHEN** user runs `openspec init` with a selected tool whose command surface is `skills-invocable`
- **AND** delivery is set to `both`
- **THEN** the system SHALL generate or refresh managed skill directories when the tool has `skillsDir`
- **AND** SHALL NOT require adapter-generated command files for that tool

#### Scenario: Both delivery for none command surface
- **WHEN** user runs `openspec init` with a selected tool whose command surface is `none`
- **AND** delivery is set to `both`
- **THEN** the system SHALL perform no command-surface artifact action for that tool
- **AND** MAY emit a compatibility note indicating no command surface is available

#### Scenario: Skills delivery for adapter-backed tool
- **WHEN** user runs `openspec init` with a selected tool that has a command adapter
- **AND** delivery is set to `skills`
- **THEN** the system SHALL generate or refresh managed skill directories when the tool has `skillsDir`
- **AND** SHALL remove managed adapter-generated command files for that tool

#### Scenario: Skills delivery for skills-invocable tool
- **WHEN** user runs `openspec init` with a selected tool whose command surface is `skills-invocable`
- **AND** delivery is set to `skills`
- **THEN** the system SHALL generate or refresh managed skill directories when the tool has `skillsDir`
- **AND** SHALL NOT require adapter-generated command files for that tool

#### Scenario: Skills delivery for none command surface
- **WHEN** user runs `openspec init` with a selected tool whose command surface is `none`
- **AND** delivery is set to `skills`
- **THEN** the system SHALL perform no command-surface artifact action for that tool
- **AND** MAY emit a compatibility note indicating no command surface is available

#### Scenario: Commands delivery for adapter-backed tool
- **WHEN** user runs `openspec init` with a selected tool that has a command adapter
- **AND** delivery is set to `commands`
- **THEN** the system SHALL generate command files for active workflows using that adapter
- **AND** the system SHALL remove managed skill directories for that tool

#### Scenario: Commands delivery for skills-invocable tool
- **WHEN** user runs `openspec init` with a selected tool whose command surface is `skills-invocable`
- **AND** delivery is set to `commands`
- **THEN** the system SHALL generate or refresh managed skill directories for active workflows
- **AND** the system SHALL NOT remove those managed skill directories as part of commands-only cleanup
- **AND** the system SHALL NOT require a command adapter for that tool

#### Scenario: Commands delivery for mixed tool selection
- **WHEN** user runs `openspec init` with multiple tools
- **AND** selected tools include both adapter-backed and skills-invocable command surfaces
- **AND** delivery is set to `commands`
- **THEN** the system SHALL apply commands-only behavior per tool capability
- **AND** the resulting install SHALL include command files for adapter-backed tools and skills for skills-invocable tools

#### Scenario: Commands delivery for unsupported command surface
- **WHEN** user runs `openspec init` with a selected tool that has no command surface capability
- **AND** delivery is set to `commands`
- **THEN** the system SHALL fail before generating or deleting artifacts
- **AND** the error SHALL list incompatible tool IDs and explain supported alternatives (`both` or `skills`)

#### Scenario: Interactive handling for unsupported command surface
- **WHEN** user runs `openspec init` interactively
- **AND** delivery is set to `commands`
- **AND** selected tools include one or more tools with command surface `none`
- **THEN** the CLI SHALL show a compatibility error and return to the interactive selection flow for correction
- **AND** SHALL not perform artifact writes until a valid selection is confirmed

### Requirement: Init compatibility signaling
The init command SHALL clearly signal command-surface compatibility outcomes in both interactive and non-interactive flows.

#### Scenario: Interactive compatibility note
- **WHEN** init runs interactively
- **AND** delivery is `commands`
- **AND** selected tools include skills-invocable command surfaces
- **THEN** the system SHALL display a compatibility note before the confirmation prompt indicating those tools will use skills as their command surface

#### Scenario: Non-interactive compatibility summary for skills-invocable tools
- **WHEN** init runs non-interactively (including `--tools` usage)
- **AND** delivery is `commands`
- **AND** selected tools include one or more `skills-invocable` command surfaces
- **THEN** the command SHALL proceed with exit code 0
- **AND** the command SHALL write deterministic compatibility summary lines to stdout indicating those tools will use managed skills as their command surface

#### Scenario: Non-interactive compatibility failure
- **WHEN** init runs non-interactively (including `--tools` usage)
- **AND** delivery is `commands`
- **AND** selected tools include any tool with no command surface capability
- **THEN** the command SHALL exit with code 1
- **AND** the command SHALL write deterministic, actionable guidance for resolving the selection to stderr
