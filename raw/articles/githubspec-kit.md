# github/spec-kit

Source: https://github.com/github/spec-kit
Ingested: 2026-04-14
Type: documentation

---

# README

<div align="center">
    <img src="./media/logo_large.webp" alt="Spec Kit Logo" width="200" height="200"/>
    <h1>🌱 Spec Kit</h1>
    <h3><em>Build high-quality software faster.</em></h3>
</div>

<p align="center">
    <strong>An open source toolkit that allows you to focus on product scenarios and predictable outcomes instead of vibe coding every piece from scratch.</strong>
</p>

<p align="center">
    <a href="https://github.com/github/spec-kit/releases/latest"><img src="https://img.shields.io/github/v/release/github/spec-kit" alt="Latest Release"/></a>
    <a href="https://github.com/github/spec-kit/stargazers"><img src="https://img.shields.io/github/stars/github/spec-kit?style=social" alt="GitHub stars"/></a>
    <a href="https://github.com/github/spec-kit/blob/main/LICENSE"><img src="https://img.shields.io/github/license/github/spec-kit" alt="License"/></a>
    <a href="https://github.github.io/spec-kit/"><img src="https://img.shields.io/badge/docs-GitHub_Pages-blue" alt="Documentation"/></a>
</p>

---

## Table of Contents

- [🤔 What is Spec-Driven Development?](#-what-is-spec-driven-development)
- [⚡ Get Started](#-get-started)
- [📽️ Video Overview](#️-video-overview)
- [🧩 Community Extensions](#-community-extensions)
- [🎨 Community Presets](#-community-presets)
- [🚶 Community Walkthroughs](#-community-walkthroughs)
- [🛠️ Community Friends](#️-community-friends)
- [🤖 Supported AI Agents](#-supported-ai-agents)
- [🔧 Specify CLI Reference](#-specify-cli-reference)
- [🧩 Making Spec Kit Your Own: Extensions & Presets](#-making-spec-kit-your-own-extensions--presets)
- [📚 Core Philosophy](#-core-philosophy)
- [🌟 Development Phases](#-development-phases)
- [🎯 Experimental Goals](#-experimental-goals)
- [🔧 Prerequisites](#-prerequisites)
- [📖 Learn More](#-learn-more)
- [📋 Detailed Process](#-detailed-process)
- [🔍 Troubleshooting](#-troubleshooting)
- [💬 Support](#-support)
- [🙏 Acknowledgements](#-acknowledgements)
- [📄 License](#-license)

## 🤔 What is Spec-Driven Development?

Spec-Driven Development **flips the script** on traditional software development. For decades, code has been king — specifications were just scaffolding we built and discarded once the "real work" of coding began. Spec-Driven Development changes this: **specifications become executable**, directly generating working implementations rather than just guiding them.

## ⚡ Get Started

### 1. Install Specify CLI

Choose your preferred installation method:

#### Option 1: Persistent Installation (Recommended)

Install once and use everywhere. Pin a specific release tag for stability (check [Releases](https://github.com/github/spec-kit/releases) for the latest):

```bash
# Install a specific stable release (recommended — replace vX.Y.Z with the latest tag)
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z

# Or install latest from main (may include unreleased changes)
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Then use the tool directly:

```bash
# Create new project
specify init <PROJECT_NAME>

# Or initialize in existing project
specify init . --ai claude
# or
specify init --here --ai claude

# Check installed tools
specify check
```

To upgrade Specify, see the [Upgrade Guide](./docs/upgrade.md) for detailed instructions. Quick upgrade:

```bash
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

#### Option 2: One-time Usage

Run directly without installing:

```bash
# Create new project (pinned to a stable release — replace vX.Y.Z with the latest tag)
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <PROJECT_NAME>

# Or initialize in existing project
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init . --ai claude
# or
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init --here --ai claude
```

**Benefits of persistent installation:**

- Tool stays installed and available in PATH
- No need to create shell aliases
- Better tool management with `uv tool list`, `uv tool upgrade`, `uv tool uninstall`
- Cleaner shell configuration

#### Option 3: Enterprise / Air-Gapped Installation

If your environment blocks access to PyPI or GitHub, see the [Enterprise / Air-Gapped Installation](./docs/installation.md#enterprise--air-gapped-installation) guide for step-by-step instructions on using `pip download` to create portable, OS-specific wheel bundles on a connected machine.

### 2. Establish project principles

Launch your AI assistant in the project directory. Most agents expose spec-kit as `/speckit.*` slash commands; Codex CLI in skills mode uses `$speckit-*` instead.

Use the **`/speckit.constitution`** command to create your project's governing principles and development guidelines that will guide all subsequent development.

```bash
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements
```

### 3. Create the spec

Use the **`/speckit.specify`** command to describe what you want to build. Focus on the **what** and **why**, not the tech stack.

```bash
/speckit.specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page. Albums are never in other nested albums. Within each album, photos are previewed in a tile-like interface.
```

### 4. Create a technical implementation plan

Use the **`/speckit.plan`** command to provide your tech stack and architecture choices.

```bash
/speckit.plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are not uploaded anywhere and metadata is stored in a local SQLite database.
```

### 5. Break down into tasks

Use **`/speckit.tasks`** to create an actionable task list from your implementation plan.

```bash
/speckit.tasks
```

### 6. Execute implementation

Use **`/speckit.implement`** to execute all tasks and build your feature according to the plan.

```bash
/speckit.implement
```

For detailed step-by-step instructions, see our [comprehensive guide](./spec-driven.md).

## 📽️ Video Overview

Want to see Spec Kit in action? Watch our [video overview](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)!

[![Spec Kit video header](/media/spec-kit-video-header.jpg)](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)

## 🧩 Community Extensions

> [!NOTE]
> Community extensions are independently created and maintained by their respective authors. GitHub and the Spec Kit maintainers may review pull requests that add entries to the community catalog for formatting, catalog structure, or policy compliance, but they do **not review, audit, endorse, or support the extension code itself**. The Community Extensions website is also a third-party resource. Review extension source code before installation and use at your own discretion.

🔍 **Browse and search community extensions on the [Community Extensions website](https://speckit-community.github.io/extensions/).**

The following community-contributed extensions are available in [`catalog.community.json`](extensions/catalog.community.json):

**Categories:**

- `docs` — reads, validates, or generates spec artifacts
- `code` — reviews, validates, or modifies source code
- `process` — orchestrates workflow across phases
- `integration` — syncs with external platforms
- `visibility` — reports on project health or progress

**Effect:**

- `Read-only` — produces reports without modifying files
- `Read+Write` — modifies files, creates artifacts, or updates specs

| Extension | Purpose | Category | Effect | URL |
|-----------|---------|----------|--------|-----|
| AI-Driven Engineering (AIDE) | A structured 7-step workflow for building new projects from scratch with AI assistants — from vision through implementation | `process` | Read+Write | [aide](https://github.com/mnriem/spec-kit-extensions/tree/main/aide) |
| Archive Extension | Archive merged features into main project memory. | `docs` | Read+Write | [spec-kit-archive](https://github.com/stn1slv/spec-kit-archive) |
| Azure DevOps Integration | Sync user stories and tasks to Azure DevOps work items using OAuth authentication | `integration` | Read+Write | [spec-kit-azure-devops](https://github.com/pragya247/spec-kit-azure-devops) |
| Branch Convention | Configurable branch and folder naming conventions for /specify with presets and custom patterns | `process` | Read+Write | [spec-kit-branch-convention](https://github.com/Quratulain-bilal/spec-kit-branch-convention) |
| Brownfield Bootstrap | Bootstrap spec-kit for existing codebases — auto-discover architecture and adopt SDD incrementally | `process` | Read+Write | [spec-kit-brownfield](https://github.com/Quratulain-bilal/spec-kit-brownfield) |
| Bugfix Workflow | Structured bugfix workflow — capture bugs, trace to spec artifacts, and patch specs surgically | `process` | Read+Write | [spec-kit-bugfix](https://github.com/Quratulain-bilal/spec-kit-bugfix) |
| Canon | Adds canon-driven (baseline-driven) workflows: spec-first, code-first, spec-drift. Requires Canon Core preset installation. | `process` | Read+Write | [spec-kit-canon](https://github.com/maximiliamus/spec-kit-canon/tree/master/extension) |
| CI Guard | Spec compliance gates for CI/CD — verify specs exist, check drift, and block merges on gaps | `process` | Read-only | [spec-kit-ci-guard](https://github.com/Quratulain-bilal/spec-kit-ci-guard) |
| Checkpoint Extension | Commit the changes made during the middle of the implementation, so you don't end up with just one very large commit at the end | `code` | Read+Write | [spec-kit-checkpoint](https://github.com/aaronrsun/spec-kit-checkpoint) |
| Cleanup Extension | Post-implementation quality gate that reviews changes, fixes small issues (scout rule), creates tasks for medium issues, and generates analysis for large issues | `code` | Read+Write | [spec-kit-cleanup](https://github.com/dsrednicki/spec-kit-cleanup) |
| Conduct Extension | Orchestrates spec-kit phases via sub-agent delegation to reduce context pollution. | `process` | Read+Write | [spec-kit-conduct-ext](https://github.com/twbrandon7/spec-kit-conduct-ext) |
| Confluence Extension | Create a doc in Confluence summarizing the specifications and planning files | `integration` | Read+Write | [spec-kit-confluence](https://github.com/aaronrsun/spec-kit-confluence) |
| DocGuard — CDD Enforcement | Canonical-Driven Development enforcement. Validates, scores, and traces project documentation with automated checks, AI-driven workflows, and spec-kit hooks. Zero NPM runtime dependencies. | `docs` | Read+Write | [spec-kit-docguard](https://github.com/raccioly/docguard) |
| Extensify | Create and validate extensions and extension catalogs | `process` | Read+Write | [extensify](https://github.com/mnriem/spec-kit-extensions/tree/main/extensify) |
| Fix Findings | Automated analyze-fix-reanalyze loop that resolves spec findings until clean | `code` | Read+Write | [spec-kit-fix-findings](https://github.com/Quratulain-bilal/spec-kit-fix-findings) |
| FixIt Extension | Spec-aware bug fixing — maps bugs to spec artifacts, proposes a plan, applies minimal changes | `code` | Read+Write | [spec-kit-fixit](https://github.com/speckit-community/spec-kit-fixit) |
| Fleet Orchestrator | Orchestrate a full feature lifecycle with human-in-the-loop gates across all SpecKit phases | `process` | Read+Write | [spec-kit-fleet](https://github.com/sharathsatish/spec-kit-fleet) |
| GitHub Issues Integration | Generate spec artifacts from GitHub Issues - import issues, sync updates, and maintain bidirectional traceability | `integration` | Read+Write | [spec-kit-github-issues](https://github.com/Fatima367/spec-kit-github-issues) |
| Iterate | Iterate on spec documents with a two-phase define-and-apply workflow — refine specs mid-implementation and go straight back to building | `docs` | Read+Write | [spec-kit-iterate](https://github.com/imviancagrace/spec-kit-iterate) |
| Jira Integration | Create Jira Epics, Stories, and Issues from spec-kit specifications and task breakdowns with configurable hierarchy and custom field support | `integration` | Read+Write | [spec-kit-jira](https://github.com/mbachorik/spec-kit-jira) |
| Learning Extension | Generate educational guides from implementations and enhance clarifications with mentoring context | `docs` | Read+Write | [spec-kit-learn](https://github.com/imviancagrace/spec-kit-learn) |
| MAQA — Multi-Agent & Quality Assurance | Coordinator → feature → QA agent workflow with parallel worktree-based implementation. Language-agnostic. Auto-detects installed board plugins. Optional CI gate. | `process` | Read+Write | [spec-kit-maqa-ext](https://github.com/GenieRobot/spec-kit-maqa-ext) |
| MAQA Azure DevOps Integration | Azure DevOps Boards integration for MAQA — syncs User Stories and Task children as features progress | `integration` | Read+Write | [spec-kit-maqa-azure-devops](https://github.com/GenieRobot/spec-kit-maqa-azure-devops) |
| MAQA CI/CD Gate | Auto-detects GitHub Actions, CircleCI, GitLab CI, and Bitbucket Pipelines. Blocks QA handoff until pipeline is green. | `process` | Read+Write | [spec-kit-maqa-ci](https://github.com/GenieRobot/spec-kit-maqa-ci) |
| MAQA GitHub Projects Integration | GitHub Projects v2 integration for MAQA — syncs draft issues and Status columns as features progress | `integration` | Read+Write | [spec-kit-maqa-github-projects](https://github.com/GenieRobot/spec-kit-maqa-github-projects) |
| MAQA Jira Integration | Jira integration for MAQA — syncs Stories and Subtasks as features progress through the board | `integration` | Read+Write | [spec-kit-maqa-jira](https://github.com/GenieRobot/spec-kit-maqa-jira) |
| MAQA Linear Integration | Linear integration for MAQA — syncs issues and sub-issues across workflow states as features progress | `integration` | Read+Write | [spec-kit-maqa-linear](https://github.com/GenieRobot/spec-kit-maqa-linear) |
| MAQA Trello Integration | Trello board integration for MAQA — populates board from specs, moves cards, real-time checklist ticking | `integration` | Read+Write | [spec-kit-maqa-trello](https://github.com/GenieRobot/spec-kit-maqa-trello) |
| MemoryLint | Agent memory governance tool: Automatically audits and fixes boundary conflicts between AGENTS.md and the constitution. | `process` | Read+Write | [memorylint](https://github.com/RbBtSn0w/spec-kit-extensions/tree/main/memorylint) |
| Onboard | Contextual onboarding and progressive growth for developers new to spec-kit projects. Explains specs, maps dependencies, validates understanding, and guides the next step | `process` | Read+Write | [spec-kit-onboard](https://github.com/dmux/spec-kit-onboard) |
| Optimize | Audit and optimize AI governance for context efficiency — token budgets, rule health, interpretability, compression, coherence, and echo detection | `process` | Read+Write | [spec-kit-optimize](https://github.com/sakitA/spec-kit-optimize) |
| Plan Review Gate | Require spec.md and plan.md to be merged via MR/PR before allowing task generation | `process` | Read-only | [spec-kit-plan-review-gate](https://github.com/luno/spec-kit-plan-review-gate) |
| PR Bridge | Auto-generate pull request descriptions, checklists, and summaries from spec artifacts | `process` | Read-only | [spec-kit-pr-bridge-](https://github.com/Quratulain-bilal/spec-kit-pr-bridge-) |
| Presetify | Create and validate presets and preset catalogs | `process` | Read+Write | [presetify](https://github.com/mnriem/spec-kit-extensions/tree/main/presetify) |
| Product Forge | Full product lifecycle: research → product spec → SpecKit → implement → verify → test | `process` | Read+Write | [speckit-product-forge](https://github.com/VaiYav/speckit-product-forge) |
| Project Health Check | Diagnose a Spec Kit project and report health issues across structure, agents, features, scripts, extensions, and git | `visibility` | Read-only | [spec-kit-doctor](https://github.com/KhawarHabibKhan/spec-kit-doctor) |
| Project Status | Show current SDD workflow progress — active feature, artifact status, task completion, workflow phase, and extensions summary | `visibility` | Read-only | [spec-kit-status](https://github.com/KhawarHabibKhan/spec-kit-status) |
| QA Testing Extension | Systematic QA testing with browser-driven or CLI-based validation of acceptance criteria from spec | `code` | Read-only | [spec-kit-qa](https://github.com/arunt14/spec-kit-qa) |
| Ralph Loop | Autonomous implementation loop using AI agent CLI | `code` | Read+Write | [spec-kit-ralph](https://github.com/Rubiss/spec-kit-ralph) |
| Reconcile Extension | Reconcile implementation drift by surgically updating feature artifacts. | `docs` | Read+Write | [spec-kit-reconcile](https://github.com/stn1slv/spec-kit-reconcile) |
| Repository Index | Generate index for existing repo for overview, architecture and module level. | `docs` | Read-only | [spec-kit-repoindex](https://github.com/liuyiyu/spec-kit-repoindex) |
| Retro Extension | Sprint retrospective analysis with metrics, spec accuracy assessment, and improvement suggestions | `process` | Read+Write | [spec-kit-retro](https://github.com/arunt14/spec-kit-retro) |
| Retrospective Extension | Post-implementation retrospective with spec adherence scoring, drift analysis, and human-gated spec updates | `docs` | Read+Write | [spec-kit-retrospective](https://github.com/emi-dm/spec-kit-retrospective) |
| Review Extension | Post-implementation comprehensive code review with specialized agents for code quality, comments, tests, error handling, type design, and simplification | `code` | Read-only | [spec-kit-review](https://github.com/ismaelJimenez/spec-kit-review) |
| SDD Utilities | Resume interrupted workflows, validate project health, and verify spec-to-task traceability | `process` | Read+Write | [speckit-utils](https://github.com/mvanhorn/speckit-utils) |
| Security Review | Comprehensive security audit of codebases using AI-powered DevSecOps analysis | `code` | Read-only | [spec-kit-security-review](https://github.com/DyanGalih/spec-kit-security-review) |
| SFSpeckit | Enterprise Salesforce SDLC with 18 commands for the full SDD lifecycle. | `process` | Read+Write | [spec-kit-sf](https://github.com/ysumanth06/spec-kit-sf) |
| Ship Release Extension | Automates release pipeline: pre-flight checks, branch sync, changelog generation, CI verification, and PR creation | `process` | Read+Write | [spec-kit-ship](https://github.com/arunt14/spec-kit-ship) |
| Spec Critique Extension | Dual-lens critical review of spec and plan from product strategy and engineering risk perspectives | `docs` | Read-only | [spec-kit-critique](https://github.com/arunt14/spec-kit-critique) |
| Spec Diagram | Auto-generate Mermaid diagrams of SDD workflow state, feature progress, and task dependencies | `visibility` | Read-only | [spec-kit-diagram-](https://github.com/Quratulain-bilal/spec-kit-diagram-) |
| Spec Refine | Update specs in-place, propagate changes to plan and tasks, and diff impact across artifacts | `process` | Read+Write | [spec-kit-refine](https://github.com/Quratulain-bilal/spec-kit-refine) |
| Spec Sync | Detect and resolve drift between specs and implementation. AI-assisted resolution with human approval | `docs` | Read+Write | [spec-kit-sync](https://github.com/bgervin/spec-kit-sync) |
| SpecTest | Auto-generate test scaffolds from spec criteria, map coverage, and find untested requirements | `code` | Read+Write | [spec-kit-spectest](https://github.com/Quratulain-bilal/spec-kit-spectest) |
| Staff Review Extension | Staff-engineer-level code review that validates implementation against spec, checks security, performance, and test coverage | `code` | Read-only | [spec-kit-staff-review](https://github.com/arunt14/spec-kit-staff-review) |
| Status Report | Project status, feature progress, and next-action recommendations for spec-driven workflows | `visibility` | Read-only | [Open-Agent-Tools/spec-kit-status](https://github.com/Open-Agent-Tools/spec-kit-status) |
| Superpowers Bridge | Orchestrates obra/superpowers skills within the spec-kit SDD workflow across the full lifecycle (clarification, TDD, review, verification, critique, debugging, branch completion) | `process` | Read+Write | [superpowers-bridge](https://github.com/RbBtSn0w/spec-kit-extensions/tree/main/superpowers-bridge) |
| TinySpec | Lightweight single-file workflow for small tasks — skip the heavy multi-step SDD process | `process` | Read+Write | [spec-kit-tinyspec](https://github.com/Quratulain-bilal/spec-kit-tinyspec) |
| V-Model Extension Pack | Enforces V-Model paired generation of development specs and test specs with full traceability | `docs` | Read+Write | [spec-kit-v-model](https://github.com/leocamello/spec-kit-v-model) |
| Verify Extension | Post-implementation quality gate that validates implemented code against specification artifacts | `code` | Read-only | [spec-kit-verify](https://github.com/ismaelJimenez/spec-kit-verify) |
| Verify Tasks Extension | Detect phantom completions: tasks marked [X] in tasks.md with no real implementation | `code` | Read-only | [spec-kit-verify-tasks](https://github.com/datastone-inc/spec-kit-verify-tasks) |
| What-if Analysis | Preview the downstream impact (complexity, effort, tasks, risks) of requirement changes before committing to them | `visibility` | Read-only | [spec-kit-whatif](https://github.com/DevAbdullah90/spec-kit-whatif) |
| Worktree Isolation | Spawn isolated git worktrees for parallel feature development without checkout switching | `process` | Read+Write | [spec-kit-worktree](https://github.com/Quratulain-bilal/spec-kit-worktree) |
| Worktrees | Default-on worktree isolation for parallel agents — sibling or nested layout | `process` | Read+Write | [spec-kit-worktree-parallel](https://github.com/dango85/spec-kit-worktree-parallel) |

To submit your own extension, see the [Extension Publishing Guide](extensions/EXTENSION-PUBLISHING-GUIDE.md).

## 🎨 Community Presets

> [!NOTE]
> Community presets are independently created and maintained by their respective authors. GitHub and the Spec Kit maintainers may review pull requests that add entries to the community catalog for formatting, catalog structure, or policy compliance, but they do **not review, audit, endorse, or support the preset code itself**. Review preset source code before installation and use at your own discretion.

The following community-contributed presets customize how Spec Kit behaves — overriding templates, commands, and terminology without changing any tooling. Presets are available in [`catalog.community.json`](presets/catalog.community.json):

| Preset | Purpose | Provides | Requires | URL |
|--------|---------|----------|----------|-----|
| AIDE In-Place Migration | Adapts the AIDE extension workflow for in-place technology migrations (X → Y pattern) — adds migration objectives, verification gates, knowledge documents, and behavioral equivalence criteria | 2 templates, 8 commands | AIDE extension | [spec-kit-presets](https://github.com/mnriem/spec-kit-presets) |
| Canon Core | Adapts original Spec Kit workflow to work together with Canon extension | 2 templates, 8 commands | — | [spec-kit-canon](https://github.com/maximiliamus/spec-kit-canon) |
| Explicit Task Dependencies | Adds explicit `(depends on T###)` dependency declarations and an Execution Wave DAG to tasks.md for parallel scheduling | 1 template, 1 command | — | [spec-kit-preset-explicit-task-dependencies](https://github.com/Quratulain-bilal/spec-kit-preset-explicit-task-dependencies) |
| Fiction Book Writing | It adapts the Spec-Driven Development workflow for storytelling: features become story elements, specs become story briefs, plans become story structures, and tasks become scene-by-scene writing tasks. Supports single and multi-POV, all major plot structure frameworks, and two style modes, author voice sample or humanized AI prose. | 21 templates, 17 commands | — | [spec-kit-preset-fiction-book-writing](https://github.com/adaumann/speckit-preset-fiction-book-writing) |
| Multi-Repo Branching | Coordinates feature branch creation across multiple git repositories (independent repos and submodules) during plan and tasks phases | 2 commands | — | [spec-kit-preset-multi-repo-branching](https://github.com/sakitA/spec-kit-preset-multi-repo-branching) |
| Pirate Speak (Full) | Transforms all Spec Kit output into pirate speak — specs become "Voyage Manifests", plans become "Battle Plans", tasks become "Crew Assignments" | 6 templates, 9 commands | — | [spec-kit-presets](https://github.com/mnriem/spec-kit-presets) |
| Table of Contents Navigation | Adds a navigable Table of Contents to generated spec.md, plan.md, and tasks.md documents | 3 templates, 3 commands | — | [spec-kit-preset-toc-navigation](https://github.com/Quratulain-bilal/spec-kit-preset-toc-navigation) |
| VS Code Ask Questions | Enhances the clarify command to use `vscode/askQuestions` for batched interactive questioning. | 1 command | — | [spec-kit-presets](https://github.com/fdcastel/spec-kit-presets) |

To build and publish your own preset, see the [Presets Publishing Guide](presets/PUBLISHING.md).

## 🚶 Community Walkthroughs

> [!NOTE]
> Community walkthroughs are independently created and maintained by their respective authors. They are **not reviewed, nor endorsed, nor supported by GitHub**. Review their content before following along and use at your own discretion.

See Spec-Driven Development in action across different scenarios with these community-contributed walkthroughs:

- **[Greenfield .NET CLI tool](https://github.com/mnriem/spec-kit-dotnet-cli-demo)** — Builds a Timezone Utility as a .NET single-binary CLI tool from a blank directory, covering the full spec-kit workflow: constitution, specify, plan, tasks, and multi-pass implement using GitHub Copilot agents.

- **[Greenfield Spring Boot + React platform](https://github.com/mnriem/spec-kit-spring-react-demo)** — Builds an LLM performance analytics platform (REST API, graphs, iteration tracking) from scratch using Spring Boot, embedded React, PostgreSQL, and Docker Compose, with a clarify step and a cross-artifact consistency analysis pass included.

- **[Brownfield ASP.NET CMS extension](https://github.com/mnriem/spec-kit-aspnet-brownfield-demo)** — Extends an existing open-source .NET CMS (CarrotCakeCMS-Core, ~307,000 lines of C#, Razor, SQL, JavaScript, and config files) with two new features — cross-platform Docker Compose infrastructure and a token-authenticated headless REST API — demonstrating how spec-kit fits into existing codebases without prior specs or a constitution.

- **[Brownfield Java runtime extension](https://github.com/mnriem/spec-kit-java-brownfield-demo)** — Extends an existing open-source Jakarta EE runtime (Piranha, ~420,000 lines of Java, XML, JSP, HTML, and config files across 180 Maven modules) with a password-protected Server Admin Console, demonstrating spec-kit on a large multi-module Java project with no prior specs or constitution.

- **[Brownfield Go / React dashboard demo](https://github.com/mnriem/spec-kit-go-brownfield-demo)** — Demonstrates spec-kit driven entirely from the **terminal using GitHub Copilot CLI**. Extends NASA's open-source Hermes ground support system (Go) with a lightweight React-based web telemetry dashboard, showing that the full constitution → specify → plan → tasks → implement workflow works from the terminal.

- **[Greenfield Spring Boot MVC with a custom preset](https://github.com/mnriem/spec-kit-pirate-speak-preset-demo)** — Builds a Spring Boot MVC application from scratch using a custom pirate-speak preset, demonstrating how presets can reshape the entire spec-kit experience: specifications become "Voyage Manifests," plans become "Battle Plans," and tasks become "Crew Assignments" — all generated in full pirate vernacular without changing any tooling.

- **[Greenfield Spring Boot + React with a custom extension](https://github.com/mnriem/spec-kit-aide-extension-demo)** — Walks through the **AIDE extension**, a community extension that adds an alternative spec-driven workflow to spec-kit with high-level specs (vision) and low-level specs (work items) organized in a 7-step iterative lifecycle: vision → roadmap → progress tracking → work queue → work items → execution → feedback loops. Uses a family trading platform (Spring Boot 4, React 19, PostgreSQL, Docker Compose) as the scenario to illustrate how the extension mechanism lets you plug in a different style of spec-driven development without changing any core tooling — truly utilizing the "Kit" in Spec Kit.

## 🛠️ Community Friends

> [!NOTE]
> Community projects listed here are independently created and maintained by their respective authors. They are **not reviewed, nor endorsed, nor supported by GitHub**. Review their source code before installation and use at your own discretion.

Community projects that extend, visualize, or build on Spec Kit:

- **[cc-spex](https://github.com/rhuss/cc-spex)** - A Claude Code plugin that adds composable traits on top of Spec Kit with [Superpowers](https://github.com/obra/superpowers)-based quality gates, spec/code review, git worktree isolation, and parallel implementation via agent teams.

- **[Spec Kit Assistant](https://marketplace.visualstudio.com/items?itemName=rfsales.speckit-assistant)** — A VS Code extension that provides a visual orchestrator for the full SDD workflow (constitution → specification → planning → tasks → implementation) with phase status visualization, an interactive task checklist, DAG visualization, and support for Claude, Gemini, GitHub Copilot, and OpenAI backends. Requires the `specify` CLI in your PATH.

- **[SpecKit Companion](https://marketplace.visualstudio.com/items?itemName=alfredoperez.speckit-companion)** — A VS Code extension that brings a visual GUI to Spec Kit. Browse specs in a rich markdown viewer with clickable file references, create specifications with image attachments, comment and refine each step inline (GitHub-style review), track your progress through the SDD workflow with a visual phase stepper, and manage steering documents like constitutions and templates.

## 🤖 Supported AI Agents
| Agent                                                                                | Support | Notes                                                                                                                                     |
| ------------------------------------------------------------------------------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Qoder CLI](https://qoder.com/cli)                                                   | ✅      |                                                                                                                                           |
| [Kiro CLI](https://kiro.dev/docs/cli/)                                               | ✅      | Use `--ai kiro-cli` (alias: `--ai kiro`)                                                                                                 |
| [Amp](https://ampcode.com/)                                                          | ✅      |                                                                                                                                           |
| [Auggie CLI](https://docs.augmentcode.com/cli/overview)                              | ✅      |                                                                                                                                           |
| [Claude Code](https://www.anthropic.com/claude-code)                                 | ✅      | Installs skills in `.claude/skills`; invoke spec-kit as `/speckit-constitution`, `/speckit-plan`, etc.                                  |
| [CodeBuddy CLI](https://www.codebuddy.ai/cli)                                        | ✅      |                                                                                                                                           |
| [Codex CLI](https://github.com/openai/codex)                                         | ✅      | Requires `--ai-skills`. Codex recommends [skills](https://developers.openai.com/codex/skills) and treats [custom prompts](https://developers.openai.com/codex/custom-prompts) as deprecated. Spec-kit installs Codex skills into `.agents/skills` and invokes them as `$speckit-<command>`. |
| [Cursor](https://cursor.sh/)                                                         | ✅      |                                                                                                                                           |
| [Forge](https://forgecode.dev/)                                                      | ✅      | CLI tool: `forge`                                                                                                                         |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli)                            | ✅      |                                                                                                                                           |
| [Goose](https://block.github.io/goose/)                                              | ✅      | Uses YAML recipe format in `.goose/recipes/` with slash command support                                                                   |
| [GitHub Copilot](https://code.visualstudio.com/)                                     | ✅      |                                                                                                                                           |
| [IBM Bob](https://www.ibm.com/products/bob)                                          | ✅      | IDE-based agent with slash command support                                                                                                |
| [Jules](https://jules.google.com/)                                                   | ✅      |                                                                                                                                           |
| [Kilo Code](https://github.com/Kilo-Org/kilocode)                                    | ✅      |                                                                                                                                           |
| [opencode](https://opencode.ai/)                                                     | ✅      |                                                                                                                                           |
| [Pi Coding Agent](https://pi.dev)                                                    | ✅      | Pi doesn't have MCP support out of the box, so `taskstoissues` won't work as intended. MCP support can be added via [extensions](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent#extensions) |
| [Qwen Code](https://github.com/QwenLM/qwen-code)                                     | ✅      |                                                                                                                                           |
| [Roo Code](https://roocode.com/)                                                     | ✅      |                                                                                                                                           |
| [SHAI (OVHcloud)](https://github.com/ovh/shai)                                       | ✅      |                                                                                                                                           |
| [Tabnine CLI](https://docs.tabnine.com/main/getting-started/tabnine-cli)             | ✅      |                                                                                                                                           |
| [Mistral Vibe](https://github.com/mistralai/mistral-vibe)                            | ✅      |                                                                                                                                           |
| [Kimi Code](https://code.kimi.com/)                                                  | ✅      |                                                                                                                                           |
| [iFlow CLI](https://docs.iflow.cn/en/cli/quickstart)                                 | ✅      |                                                                                                                                           |
| [Windsurf](https://windsurf.com/)                                                    | ✅      |                                                                                                                                           |
| [Junie](https://junie.jetbrains.com/)                                                | ✅      |                                                                                                                                           |
| [Antigravity (agy)](https://antigravity.google/)                                     | ✅      | Requires `--ai-skills` |
| [Trae](https://www.trae.ai/)                                                         | ✅      |                                                                                                                                           |
| Generic                                                                              | ✅      | Bring your own agent — use `--ai generic --ai-commands-dir <path>` for unsupported agents                                                 |

## Available Slash Commands

After running `specify init`, your AI coding agent will have access to these slash commands for structured development. If you pass `--ai <agent> --ai-skills`, Spec Kit installs agent skills instead of slash-command prompt files; `--ai-skills` requires `--ai`.

#### Core Commands

Essential commands for the Spec-Driven Development workflow:

| Command                  | Agent Skill            | Description                                                                |
| ------------------------ | ---------------------- | -------------------------------------------------------------------------- |
| `/speckit.constitution`  | `speckit-constitution` | Create or update project governing principles and development guidelines   |
| `/speckit.specify`       | `speckit-specify`      | Define what you want to build (requirements and user stories)              |
| `/speckit.plan`          | `speckit-plan`         | Create technical implementation plans with your chosen tech stack          |
| `/speckit.tasks`         | `speckit-tasks`        | Generate actionable task lists for implementation                          |
| `/speckit.taskstoissues` | `speckit-taskstoissues`| Convert generated task lists into GitHub issues for tracking and execution |
| `/speckit.implement`     | `speckit-implement`    | Execute all tasks to build the feature according to the plan               |

#### Optional Commands

Additional commands for enhanced quality and validation:

| Command              | Agent Skill            | Description                                                                                                                          |
| -------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `/speckit.clarify`   | `speckit-clarify`      | Clarify underspecified areas (recommended before `/speckit.plan`; formerly `/quizme`)                                                |
| `/speckit.analyze`   | `speckit-analyze`      | Cross-artifact consistency & coverage analysis (run after `/speckit.tasks`, before `/speckit.implement`)                             |
| `/speckit.checklist` | `speckit-checklist`    | Generate custom quality checklists that validate requirements completeness, clarity, and consistency (like "unit tests for English") |

## 🔧 Specify CLI Reference

The `specify` tool is invoked as

```text
specify <COMMAND> [SUBCOMMAND] [OPTIONS]
```

and supports the following commands:

### Commands

| Command       | Description                                                                                                                                                                                                                                                                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `init`        | Initialize a new Specify project from the latest template.                                                                                                                                                                                                                                                                                   |
| `check`       | Check for installed tools: `git` plus all CLI-based agents configured in `AGENT_CONFIG` (for example: `claude`, `gemini`, `code`/`code-insiders`, `cursor-agent`, `windsurf`, `junie`, `qwen`, `opencode`, `codex`, `kiro-cli`, `shai`, `qodercli`, `vibe`, `kimi`, `iflow`, `pi`, `forge`, etc.)                                            |
| `version`     | Show the currently installed Spec Kit version.                                                                                                                                                                                                                                                                                               |
| `extension`   | Manage extensions                                                                                                                                                                                                                                                                                                                            |
| `preset`      | Manage presets                                                                                                                                                                                                                                                                                                                               |
| `integration` | Manage integrations                                                                                                                                                                                                                                                                                                                          |

### `specify init` Arguments & Options

```bash
specify init [PROJECT_NAME] <OPTIONS>
```

| Argument/Option        | Type     | Description                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PROJECT_NAME>`       | Argument | Name for your new project directory (optional if using `--here`, or use `.` for current directory)                                                                                                                                                                                                                                                                                        |
| `--ai`                 | Option   | AI assistant to use (see `AGENT_CONFIG` for the full, up-to-date list). Common options include: `claude`, `gemini`, `copilot`, `cursor-agent`, `qwen`, `opencode`, `codex`, `windsurf`, `junie`, `kilocode`, `auggie`, `roo`, `codebuddy`, `amp`, `shai`, `kiro-cli` (`kiro` alias), `agy`, `bob`, `qodercli`, `vibe`, `kimi`, `iflow`, `pi`, `forge`, or `generic` (requires `--ai-commands-dir`) |
| `--ai-commands-dir`    | Option   | Directory for agent command files (required with `--ai generic`, e.g. `.myagent/commands/`)                                                                                                                                                                                                                                                                                               |
| `--script`             | Option   | Script variant to use: `sh` (bash/zsh) or `ps` (PowerShell)                                                                                                                                                                                                                                                                                                                               |
| `--ignore-agent-tools` | Flag     | Skip checks for AI agent tools like Claude Code                                                                                                                                                                                                                                                                                                                                           |
| `--no-git`             | Flag     | Skip git repository initialization                                                                                                                                                                                                                                                                                                                                                        |
| `--here`               | Flag     | Initialize project in the current directory instead of creating a new one                                                                                                                                                                                                                                                                                                                 |
| `--force`              | Flag     | Force merge/overwrite when initializing in current directory (skip confirmation)                                                                                                                                                                                                                                                                                                          |
| `--skip-tls`           | Flag     | Skip SSL/TLS verification (not recommended)                                                                                                                                                                                                                                                                                                                                               |
| `--debug`              | Flag     | Enable detailed debug output for troubleshooting                                                                                                                                                                                                                                                                                                                                          |
| `--github-token`       | Option   | GitHub token for API requests (or set GH_TOKEN/GITHUB_TOKEN env variable)                                                                                                                                                                                                                                                                                                                 |
| `--ai-skills`          | Flag     | Install Prompt.MD templates as agent skills in agent-specific `skills/` directory (requires `--ai`). Extension commands are also auto-registered as skills when extensions are added later.                                                                                                                                                                                               |
| `--branch-numbering`   | Option   | Branch numbering strategy: `sequential` (default — `001`, `002`, `003`, …, `1000`, … — expands beyond 3 digits automatically) or `timestamp` (`YYYYMMDD-HHMMSS`). Timestamp mode is useful for distributed teams to avoid numbering conflicts                                                                                                                                                                                                  |

### Examples

```bash
# Basic project initialization
specify init my-project

# Initialize with specific AI assistant
specify init my-project --ai claude

# Initialize with Cursor support
specify init my-project --ai cursor-agent

# Initialize with Qoder support
specify init my-project --ai qodercli

# Initialize with Windsurf support
specify init my-project --ai windsurf

# Initialize with Kiro CLI support
specify init my-project --ai kiro-cli

# Initialize with Amp support
specify init my-project --ai amp

# Initialize with SHAI support
specify init my-project --ai shai

# Initialize with Mistral Vibe support
specify init my-project --ai vibe

# Initialize with IBM Bob support
specify init my-project --ai bob

# Initialize with Pi Coding Agent support
specify init my-project --ai pi

# Initialize with Codex CLI support
specify init my-project --ai codex --ai-skills

# Initialize with Antigravity support
specify init my-project --ai agy --ai-skills

# Initialize with Forge support
specify init my-project --ai forge

# Initialize with an unsupported agent (generic / bring your own agent)
specify init my-project --ai generic --ai-commands-dir .myagent/commands/

# Initialize with PowerShell scripts (Windows/cross-platform)
specify init my-project --ai copilot --script ps

# Initialize in current directory
specify init . --ai copilot
# or use the --here flag
specify init --here --ai copilot

# Force merge into current (non-empty) directory without confirmation
specify init . --force --ai copilot
# or
specify init --here --force --ai copilot

# Skip git initialization
specify init my-project --ai gemini --no-git

# Enable debug output for troubleshooting
specify init my-project --ai claude --debug

# Use GitHub token for API requests (helpful for corporate environments)
specify init my-project --ai claude --github-token ghp_your_token_here

# Claude Code installs skills with the project by default
specify init my-project --ai claude

# Initialize in current directory with agent skills
specify init --here --ai gemini --ai-skills

# Use timestamp-based branch numbering (useful for distributed teams)
specify init my-project --ai claude --branch-numbering timestamp

# Check system requirements
specify check
```

### Environment Variables

| Variable          | Description                                                                                                                                                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `SPECIFY_FEATURE` | Override feature detection for non-Git repositories. Set to the feature directory name (e.g., `001-photo-albums`) to work on a specific feature when not using Git branches.<br/>\*\*Must be set in the context of the agent you're working with prior to using `/speckit.plan` or follow-up commands. |

## 🧩 Making Spec Kit Your Own: Extensions & Presets

Spec Kit can be tailored to your needs through two complementary systems — **extensions** and **presets** — plus project-local overrides for one-off adjustments:

| Priority | Component Type                                    | Location                         |
| -------: | ------------------------------------------------- | -------------------------------- |
|      ⬆ 1 | Project-Local Overrides                           | `.specify/templates/overrides/`  |
|        2 | Presets — Customize core & extensions             | `.specify/presets/templates/`    |
|        3 | Extensions — Add new capabilities                 | `.specify/extensions/templates/` |
|      ⬇ 4 | Spec Kit Core — Built-in SDD commands & templates | `.specify/templates/`            |

- **Templates** are resolved at **runtime** — Spec Kit walks the stack top-down and uses the first match.
- Project-local overrides (`.specify/templates/overrides/`) let you make one-off adjustments for a single project without creating a full preset.
- **Extension/preset commands** are applied at **install time** — when you run `specify extension add` or `specify preset add`, command files are written into agent directories (e.g., `.claude/commands/`).
- If multiple presets or extensions provide the same command, the highest-priority version wins. On removal, the next-highest-priority version is restored automatically.
- If no overrides or customizations exist, Spec Kit uses its core defaults.

### Extensions — Add New Capabilities

Use **extensions** when you need functionality that goes beyond Spec Kit's core. Extensions introduce new commands and templates — for example, adding domain-specific workflows that are not covered by the built-in SDD commands, integrating with external tools, or adding entirely new development phases. They expand *what Spec Kit can do*.

```bash
# Search available extensions
specify extension search

# Install an extension
specify extension add <extension-name>
```

For example, extensions could add Jira integration, post-implementation code review, V-Model test traceability, or project health diagnostics.

See the [Extensions README](./extensions/README.md) for the full guide and how to build and publish your own. Browse the [community extensions](#-community-extensions) above for what's available.

### Presets — Customize Existing Workflows

Use **presets** when you want to change *how* Spec Kit works without adding new capabilities. Presets override the templates and commands that ship with the core *and* with installed extensions — for example, enforcing a compliance-oriented spec format, using domain-specific terminology, or applying organizational standards to plans and tasks. They customize the artifacts and instructions that Spec Kit and its extensions produce.

```bash
# Search available presets
specify preset search

# Install a preset
specify preset add <preset-name>
```

For example, presets could restructure spec templates to require regulatory traceability, adapt the workflow to fit the methodology you use (e.g., Agile, Kanban, Waterfall, jobs-to-be-done, or domain-driven design), add mandatory security review gates to plans, enforce test-first task ordering, or localize the entire workflow to a different language. The [pirate-speak demo](https://github.com/mnriem/spec-kit-pirate-speak-preset-demo) shows just how deep the customization can go. Multiple presets can be stacked with priority ordering.

See the [Presets README](./presets/README.md) for the full guide, including resolution order, priority, and how to create your own.

### When to Use Which

| Goal | Use |
| --- | --- |
| Add a brand-new command or workflow | Extension |
| Customize the format of specs, plans, or tasks | Preset |
| Integrate an external tool or service | Extension |
| Enforce organizational or regulatory standards | Preset |
| Ship reusable domain-specific templates | Either — presets for template overrides, extensions for templates bundled with new commands |

## 📚 Core Philosophy

Spec-Driven Development is a structured process that emphasizes:

- **Intent-driven development** where specifications define the "*what*" before the "*how*"
- **Rich specification creation** using guardrails and organizational principles
- **Multi-step refinement** rather than one-shot code generation from prompts
- **Heavy reliance** on advanced AI model capabilities for specification interpretation

## 🌟 Development Phases

| Phase                                    | Focus                    | Key Activities                                                                                                                                                     |
| ---------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **0-to-1 Development** ("Greenfield")    | Generate from scratch    | <ul><li>Start with high-level requirements</li><li>Generate specifications</li><li>Plan implementation steps</li><li>Build production-ready applications</li></ul> |
| **Creative Exploration**                 | Parallel implementations | <ul><li>Explore diverse solutions</li><li>Support multiple technology stacks & architectures</li><li>Experiment with UX patterns</li></ul>                         |
| **Iterative Enhancement** ("Brownfield") | Brownfield modernization | <ul><li>Add features iteratively</li><li>Modernize legacy systems</li><li>Adapt processes</li></ul>                                                                |

## 🎯 Experimental Goals

Our research and experimentation focus on:

### Technology independence

- Create applications using diverse technology stacks
- Validate the hypothesis that Spec-Driven Development is a process not tied to specific technologies, programming languages, or frameworks

### Enterprise constraints

- Demonstrate mission-critical application development
- Incorporate organizational constraints (cloud providers, tech stacks, engineering practices)
- Support enterprise design systems and compliance requirements

### User-centric development

- Build applications for different user cohorts and preferences
- Support various development approaches (from vibe-coding to AI-native development)

### Creative & iterative processes

- Validate the concept of parallel implementation exploration
- Provide robust iterative feature development workflows
- Extend processes to handle upgrades and modernization tasks

## 🔧 Prerequisites

- **Linux/macOS/Windows**
- [Supported](#-supported-ai-agents) AI coding agent.
- [uv](https://docs.astral.sh/uv/) for package management
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

If you encounter issues with an agent, please open an issue so we can refine the integration.

## 📖 Learn More

- **[Complete Spec-Driven Development Methodology](./spec-driven.md)** - Deep dive into the full process
- **[Detailed Walkthrough](#-detailed-process)** - Step-by-step implementation guide

---

## 📋 Detailed Process

<details>
<summary>Click to expand the detailed step-by-step walkthrough</summary>

You can use the Specify CLI to bootstrap your project, which will bring in the required artifacts in your environment. Run:

```bash
specify init <project_name>
```

Or initialize in the current directory:

```bash
specify init .
# or use the --here flag
specify init --here
# Skip confirmation when the directory already has files
specify init . --force
# or
specify init --here --force
```

![Specify CLI bootstrapping a new project in the terminal](./media/specify_cli.gif)

You will be prompted to select the AI agent you are using. You can also proactively specify it directly in the terminal:

```bash
specify init <project_name> --ai claude
specify init <project_name> --ai gemini
specify init <project_name> --ai copilot

# Or in current directory:
specify init . --ai claude
specify init . --ai codex --ai-skills

# or use --here flag
specify init --here --ai claude
specify init --here --ai codex --ai-skills

# Force merge into a non-empty current directory
specify init . --force --ai claude

# or
specify init --here --force --ai claude
```

The CLI will check if you have Claude Code, Gemini CLI, Cursor CLI, Qwen CLI, opencode, Codex CLI, Qoder CLI, Tabnine CLI, Kiro CLI, Pi, Forge, Goose, or Mistral Vibe installed. If you do not, or you prefer to get the templates without checking for the right tools, use `--ignore-agent-tools` with your command:

```bash
specify init <project_name> --ai claude --ignore-agent-tools
```

### **STEP 1:** Establish project principles

Go to the project folder and run your AI agent. In our example, we're using `claude`.

![Bootstrapping Claude Code environment](./media/bootstrap-claude-code.gif)

You will know that things are configured correctly if you see the `/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, and `/speckit.implement` commands available.

The first step should be establishing your project's governing principles using the `/speckit.constitution` command. This helps ensure consistent decision-making throughout all subsequent development phases:

```text
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements. Include governance for how these principles should guide technical decisions and implementation choices.
```

This step creates or updates the `.specify/memory/constitution.md` file with your project's foundational guidelines that the AI agent will reference during specification, planning, and implementation phases.

### **STEP 2:** Create project specifications

With your project principles established, you can now create the functional specifications. Use the `/speckit.specify` command and then provide the concrete requirements for the project you want to develop.

> [!IMPORTANT]
> Be as explicit as possible about *what* you are trying to build and *why*. **Do not focus on the tech stack at this point**.

An example prompt:

```text
Develop Taskify, a team productivity platform. It should allow users to create projects, add team members,
assign tasks, comment and move tasks between boards in Kanban style. In this initial phase for this feature,
let's call it "Create Taskify," let's have multiple users but the users will be declared ahead of time, predefined.
I want five users in two different categories, one product manager and four engineers. Let's create three
different sample projects. Let's have the standard Kanban columns for the status of each task, such as "To Do,"
"In Progress," "In Review," and "Done." There will be no login for this application as this is just the very
first testing thing to ensure that our basic features are set up. For each task in the UI for a task card,
you should be able to change the current status of the task between the different columns in the Kanban work board.
You should be able to leave an unlimited number of comments for a particular card. You should be able to, from that task
card, assign one of the valid users. When you first launch Taskify, it's going to give you a list of the five users to pick
from. There will be no password required. When you click on a user, you go into the main view, which displays the list of
projects. When you click on a project, you open the Kanban board for that project. You're going to see the columns.
You'll be able to drag and drop cards back and forth between different columns. You will see any cards that are
assigned to you, the currently logged in user, in a different color from all the other ones, so you can quickly
see yours. You can edit any comments that you make, but you can't edit comments that other people made. You can
delete any comments that you made, but you can't delete comments anybody else made.
```

After this prompt is entered, you should see Claude Code kick off the planning and spec drafting process. Claude Code will also trigger some of the built-in scripts to set up the repository.

Once this step is completed, you should have a new branch created (e.g., `001-create-taskify`), as well as a new specification in the `specs/001-create-taskify` directory.

The produced specification should contain a set of user stories and functional requirements, as defined in the template.

At this stage, your project folder contents should resemble the following:

```text
└── .specify
    ├── memory
    │  └── constitution.md
    ├── scripts
    │  ├── check-prerequisites.sh
    │  ├── common.sh
    │  ├── create-new-feature.sh
    │  ├── setup-plan.sh
    │  └── update-claude-md.sh
    ├── specs
    │  └── 001-create-taskify
    │      └── spec.md
    └── templates
        ├── plan-template.md
        ├── spec-template.md
        └── tasks-template.md
```

### **STEP 3:** Functional specification clarification (required before planning)

With the baseline specification created, you can go ahead and clarify any of the requirements that were not captured properly within the first shot attempt.

You should run the structured clarification workflow **before** creating a technical plan to reduce rework downstream.

Preferred order:

1. Use `/speckit.clarify` (structured) – sequential, coverage-based questioning that records answers in a Clarifications section.
2. Optionally follow up with ad-hoc free-form refinement if something still feels vague.

If you intentionally want to skip clarification (e.g., spike or exploratory prototype), explicitly state that so the agent doesn't block on missing clarifications.

Example free-form refinement prompt (after `/speckit.clarify` if still needed):

```text
For each sample project or project that you create there should be a variable number of tasks between 5 and 15
tasks for each one randomly distributed into different states of completion. Make sure that there's at least
one task in each stage of completion.
```

You should also ask Claude Code to validate the **Review & Acceptance Checklist**, checking off the things that are validated/pass the requirements, and leave the ones that are not unchecked. The following prompt can be used:

```text
Read the review and acceptance checklist, and check off each item in the checklist if the feature spec meets the criteria. Leave it empty if it does not.
```

It's important to use the interaction with Claude Code as an opportunity to clarify and ask questions around the specification - **do not treat its first attempt as final**.

### **STEP 4:** Generate a plan

You can now be specific about the tech stack and other technical requirements. You can use the `/speckit.plan` command that is built into the project template with a prompt like this:

```text
We are going to generate this using .NET Aspire, using Postgres as the database. The frontend should use
Blazor server with drag-and-drop task boards, real-time updates. There should be a REST API created with a projects API,
tasks API, and a notifications API.
```

The output of this step will include a number of implementation detail documents, with your directory tree resembling this:

```text
.
├── CLAUDE.md
├── memory
│  └── constitution.md
├── scripts
│  ├── check-prerequisites.sh
│  ├── common.sh
│  ├── create-new-feature.sh
│  ├── setup-plan.sh
│  └── update-claude-md.sh
├── specs
│  └── 001-create-taskify
│      ├── contracts
│      │  ├── api-spec.json
│      │  └── signalr-spec.md
│      ├── data-model.md
│      ├── plan.md
│      ├── quickstart.md
│      ├── research.md
│      └── spec.md
└── templates
    ├── CLAUDE-template.md
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
```

Check the `research.md` document to ensure that the right tech stack is used, based on your instructions. You can ask Claude Code to refine it if any of the components stand out, or even have it check the locally-installed version of the platform/framework you want to use (e.g., .NET).

Additionally, you might want to ask Claude Code to research details about the chosen tech stack if it's something that is rapidly changing (e.g., .NET Aspire, JS frameworks), with a prompt like this:

```text
I want you to go through the implementation plan and implementation details, looking for areas that could
benefit from additional research as .NET Aspire is a rapidly changing library. For those areas that you identify that
require further research, I want you to update the research document with additional details about the specific
versions that we are going to be using in this Taskify application and spawn parallel research tasks to clarify
any details using research from the web.
```

During this process, you might find that Claude Code gets stuck researching the wrong thing - you can help nudge it in the right direction with a prompt like this:

```text
I think we need to break this down into a series of steps. First, identify a list of tasks
that you would need to do during implementation that you're not sure of or would benefit
from further research. Write down a list of those tasks. And then for each one of these tasks,
I want you to spin up a separate research task so that the net results is we are researching
all of those very specific tasks in parallel. What I saw you doing was it looks like you were
researching .NET Aspire in general and I don't think that's gonna do much for us in this case.
That's way too untargeted research. The research needs to help you solve a specific targeted question.
```

> [!NOTE]
> Claude Code might be over-eager and add components that you did not ask for. Ask it to clarify the rationale and the source of the change.

### **STEP 5:** Have Claude Code validate the plan

With the plan in place, you should have Claude Code run through it to make sure that there are no missing pieces. You can use a prompt like this:

```text
Now I want you to go and audit the implementation plan and the implementation detail files.
Read through it with an eye on determining whether or not there is a sequence of tasks that you need
to be doing that are obvious from reading this. Because I don't know if there's enough here. For example,
when I look at the core implementation, it would be useful to reference the appropriate places in the implementation
details where it can find the information as it walks through each step in the core implementation or in the refinement.
```

This helps refine the implementation plan and helps you avoid potential blind spots that Claude Code missed in its planning cycle. Once the initial refinement pass is complete, ask Claude Code to go through the checklist once more before you can get to the implementation.

You can also ask Claude Code (if you have the [GitHub CLI](https://docs.github.com/en/github-cli/github-cli) installed) to go ahead and create a pull request from your current branch to `main` with a detailed description, to make sure that the effort is properly tracked.

> [!NOTE]
> Before you have the agent implement it, it's also worth prompting Claude Code to cross-check the details to see if there are any over-engineered pieces (remember - it can be over-eager). If over-engineered components or decisions exist, you can ask Claude Code to resolve them. Ensure that Claude Code follows the [constitution](base/memory/constitution.md) as the foundational piece that it must adhere to when establishing the plan.

### **STEP 6:** Generate task breakdown with /speckit.tasks

With the implementation plan validated, you can now break down the plan into specific, actionable tasks that can be executed in the correct order. Use the `/speckit.tasks` command to automatically generate a detailed task breakdown from your implementation plan:

```text
/speckit.tasks
```

This step creates a `tasks.md` file in your feature specification directory that contains:

- **Task breakdown organized by user story** - Each user story becomes a separate implementation phase with its own set of tasks
- **Dependency management** - Tasks are ordered to respect dependencies between components (e.g., models before services, services before endpoints)
- **Parallel execution markers** - Tasks that can run in parallel are marked with `[P]` to optimize development workflow
- **File path specifications** - Each task includes the exact file paths where implementation should occur
- **Test-driven development structure** - If tests are requested, test tasks are included and ordered to be written before implementation
- **Checkpoint validation** - Each user story phase includes checkpoints to validate independent functionality

The generated tasks.md provides a clear roadmap for the `/speckit.implement` command, ensuring systematic implementation that maintains code quality and allows for incremental delivery of user stories.

### **STEP 7:** Implementation

Once ready, use the `/speckit.implement` command to execute your implementation plan:

```text
/speckit.implement
```

The `/speckit.implement` command will:

- Validate that all prerequisites are in place (constitution, spec, plan, and tasks)
- Parse the task breakdown from `tasks.md`
- Execute tasks in the correct order, respecting dependencies and parallel execution markers
- Follow the TDD approach defined in your task plan
- Provide progress updates and handle errors appropriately

> [!IMPORTANT]
> The AI agent will execute local CLI commands (such as `dotnet`, `npm`, etc.) - make sure you have the required tools installed on your machine.

Once the implementation is complete, test the application and resolve any runtime errors that may not be visible in CLI logs (e.g., browser console errors). You can copy and paste such errors back to your AI agent for resolution.

</details>

---

## 🔍 Troubleshooting

### Git Credential Manager on Linux

If you're having issues with Git authentication on Linux, you can install Git Credential Manager:

```bash
#!/usr/bin/env bash
set -e
echo "Downloading Git Credential Manager v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "Installing Git Credential Manager..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "Configuring Git to use GCM..."
git config --global credential.helper manager
echo "Cleaning up..."
rm gcm-linux_amd64.2.6.1.deb
```

## 💬 Support

For support, please open a [GitHub issue](https://github.com/github/spec-kit/issues/new). We welcome bug reports, feature requests, and questions about using Spec-Driven Development.

## 🙏 Acknowledgements

This project is heavily influenced by and based on the work and research of [John Lam](https://github.com/jflam).

## 📄 License

This project is licensed under the terms of the MIT open source license. Please refer to the [LICENSE](./LICENSE) file for the full terms.



> **Deep fetch: 30 key files fetched beyond README.**



---

# FILE: AGENTS.md

# AGENTS.md

## About Spec Kit and Specify

**GitHub Spec Kit** is a comprehensive toolkit for implementing Spec-Driven Development (SDD) - a methodology that emphasizes creating clear specifications before implementation. The toolkit includes templates, scripts, and workflows that guide development teams through a structured approach to building software.

**Specify CLI** is the command-line interface that bootstraps projects with the Spec Kit framework. It sets up the necessary directory structures, templates, and AI agent integrations to support the Spec-Driven Development workflow.

The toolkit supports multiple AI coding assistants, allowing teams to use their preferred tools while maintaining consistent project structure and development practices.

---

## Integration Architecture

Each AI agent is a self-contained **integration subpackage** under `src/specify_cli/integrations/<key>/`. The subpackage exposes a single class that declares all metadata and inherits setup/teardown logic from a base class. Built-in integrations are then instantiated and added to the global `INTEGRATION_REGISTRY` by `src/specify_cli/integrations/__init__.py` via `_register_builtins()`.

```
src/specify_cli/integrations/
├── __init__.py            # INTEGRATION_REGISTRY + _register_builtins()
├── base.py                # IntegrationBase, MarkdownIntegration, TomlIntegration, YamlIntegration, SkillsIntegration
├── manifest.py            # IntegrationManifest (file tracking)
├── claude/                # Example: SkillsIntegration subclass
│   ├── __init__.py        #   ClaudeIntegration class
│   └── scripts/           #   Thin wrapper scripts
│       ├── update-context.sh
│       └── update-context.ps1
├── gemini/                # Example: TomlIntegration subclass
│   ├── __init__.py
│   └── scripts/
├── windsurf/              # Example: MarkdownIntegration subclass
│   ├── __init__.py
│   └── scripts/
├── copilot/               # Example: IntegrationBase subclass (custom setup)
│   ├── __init__.py
│   └── scripts/
└── ...                    # One subpackage per supported agent
```

The registry is the **single source of truth for Python integration metadata**. Supported agents, their directories, formats, and capabilities are derived from the integration classes for the Python integration layer. However, context-update behavior still requires explicit cases in the shared dispatcher scripts (`scripts/bash/update-agent-context.sh` and `scripts/powershell/update-agent-context.ps1`), which currently maintain their own supported-agent lists and agent-key→context-file mappings until they are migrated to registry-based dispatch.

---

## Adding a New Integration

### 1. Choose a base class

| Your agent needs… | Subclass |
|---|---|
| Standard markdown commands (`.md`) | `MarkdownIntegration` |
| TOML-format commands (`.toml`) | `TomlIntegration` |
| YAML recipe files (`.yaml`) | `YamlIntegration` |
| Skill directories (`speckit-<name>/SKILL.md`) | `SkillsIntegration` |
| Fully custom output (companion files, settings merge, etc.) | `IntegrationBase` directly |

Most agents only need `MarkdownIntegration` — a minimal subclass with zero method overrides.

### 2. Create the subpackage

Create `src/specify_cli/integrations/<package_dir>/__init__.py`, where `<package_dir>` is the Python-safe directory name derived from `<key>`: use the key as-is when it contains no hyphens (e.g., key `"gemini"` → `gemini/`), or replace hyphens with underscores when it does (e.g., key `"kiro-cli"` → `kiro_cli/`). The `IntegrationBase.key` class attribute always retains the original hyphenated value, since that is what the CLI and registry use. For CLI-based integrations (`requires_cli: True`), the `key` should match the actual CLI tool name (the executable users install and run) so CLI checks can resolve it correctly. For IDE-based integrations (`requires_cli: False`), use the canonical integration identifier instead.

**Minimal example — Markdown agent (Windsurf):**

```python
"""Windsurf IDE integration."""

from ..base import MarkdownIntegration


class WindsurfIntegration(MarkdownIntegration):
    key = "windsurf"
    config = {
        "name": "Windsurf",
        "folder": ".windsurf/",
        "commands_subdir": "workflows",
        "install_url": None,
        "requires_cli": False,
    }
    registrar_config = {
        "dir": ".windsurf/workflows",
        "format": "markdown",
        "args": "$ARGUMENTS",
        "extension": ".md",
    }
    context_file = ".windsurf/rules/specify-rules.md"
```

**TOML agent (Gemini):**

```python
"""Gemini CLI integration."""

from ..base import TomlIntegration


class GeminiIntegration(TomlIntegration):
    key = "gemini"
    config = {
        "name": "Gemini CLI",
        "folder": ".gemini/",
        "commands_subdir": "commands",
        "install_url": "https://github.com/google-gemini/gemini-cli",
        "requires_cli": True,
    }
    registrar_config = {
        "dir": ".gemini/commands",
        "format": "toml",
        "args": "{{args}}",
        "extension": ".toml",
    }
    context_file = "GEMINI.md"
```

**Skills agent (Codex):**

```python
"""Codex CLI integration — skills-based agent."""

from __future__ import annotations

from ..base import IntegrationOption, SkillsIntegration


class CodexIntegration(SkillsIntegration):
    key = "codex"
    config = {
        "name": "Codex CLI",
        "folder": ".agents/",
        "commands_subdir": "skills",
        "install_url": "https://github.com/openai/codex",
        "requires_cli": True,
    }
    registrar_config = {
        "dir": ".agents/skills",
        "format": "markdown",
        "args": "$ARGUMENTS",
        "extension": "/SKILL.md",
    }
    context_file = "AGENTS.md"

    @classmethod
    def options(cls) -> list[IntegrationOption]:
        return [
            IntegrationOption(
                "--skills",
                is_flag=True,
                default=True,
                help="Install as agent skills (default for Codex)",
            ),
        ]
```

#### Required fields

| Field | Location | Purpose |
|---|---|---|
| `key` | Class attribute | Unique identifier; for CLI-based integrations (`requires_cli: True`), must match the CLI executable name |
| `config` | Class attribute (dict) | Agent metadata: `name`, `folder`, `commands_subdir`, `install_url`, `requires_cli` |
| `registrar_config` | Class attribute (dict) | Command output config: `dir`, `format`, `args` placeholder, file `extension` |
| `context_file` | Class attribute (str or None) | Path to agent context/instructions file (e.g., `"CLAUDE.md"`, `".github/copilot-instructions.md"`) |

**Key design rule:** For CLI-based integrations (`requires_cli: True`), `key` must be the actual executable name (e.g., `"cursor-agent"` not `"cursor"`). This ensures `shutil.which(key)` works for CLI-tool checks without special-case mappings. IDE-based integrations (`requires_cli: False`) should use their canonical identifier (e.g., `"windsurf"`, `"copilot"`).

### 3. Register it

In `src/specify_cli/integrations/__init__.py`, add one import and one `_register()` call inside `_register_builtins()`. Both lists are alphabetical:

```python
def _register_builtins() -> None:
    # -- Imports (alphabetical) -------------------------------------------
    from .claude import ClaudeIntegration
    # ...
    from .newagent import NewAgentIntegration   # ← add import
    # ...

    # -- Registration (alphabetical) --------------------------------------
    _register(ClaudeIntegration())
    # ...
    _register(NewAgentIntegration())            # ← add registration
    # ...
```

### 4. Add scripts

Create two thin wrapper scripts in `src/specify_cli/integrations/<package_dir>/scripts/` that delegate to the shared context-update scripts. Each is ~25 lines of boilerplate.

> **Note on `<package_dir>` vs `<key>`:** `<package_dir>` is the Python-safe directory name for your integration — it matches `<key>` exactly when the key contains no hyphens (e.g., key `"gemini"` → `gemini/`), but uses underscores when it does (e.g., key `"kiro-cli"` → `kiro_cli/`). The `IntegrationBase.key` class attribute always retains the original hyphenated value (e.g., `key = "kiro-cli"`), since that is what the CLI and registry use.

**`update-context.sh`:**

```bash
#!/usr/bin/env bash
# update-context.sh — <Agent Name> integration: create/update <context_file>
set -euo pipefail

_script_dir="$(cd "$(dirname "$0")" && pwd)"
_root="$_script_dir"
while [ "$_root" != "/" ] && [ ! -d "$_root/.specify" ]; do _root="$(dirname "$_root")"; done
if [ -z "${REPO_ROOT:-}" ]; then
  if [ -d "$_root/.specify" ]; then
    REPO_ROOT="$_root"
  else
    git_root="$(git rev-parse --show-toplevel 2>/dev/null || true)"
    if [ -n "$git_root" ] && [ -d "$git_root/.specify" ]; then
      REPO_ROOT="$git_root"
    else
      REPO_ROOT="$_root"
    fi
  fi
fi

exec "$REPO_ROOT/.specify/scripts/bash/update-agent-context.sh" <key>
```

**`update-context.ps1`:**

```powershell
# update-context.ps1 — <Agent Name> integration: create/update <context_file>
$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$repoRoot = try { git rev-parse --show-toplevel 2>$null } catch { $null }
if (-not $repoRoot -or -not (Test-Path (Join-Path $repoRoot '.specify'))) {
    $repoRoot = $scriptDir
    $fsRoot = [System.IO.Path]::GetPathRoot($repoRoot)
    while ($repoRoot -and $repoRoot -ne $fsRoot -and -not (Test-Path (Join-Path $repoRoot '.specify'))) {
        $repoRoot = Split-Path -Parent $repoRoot
    }
}

& "$repoRoot/.specify/scripts/powershell/update-agent-context.ps1" -AgentType <key>
```

Replace `<key>` with your integration key and `<Agent Name>` / `<context_file>` with the appropriate values.

You must also add the agent to the shared context-update scripts so the shared dispatcher recognises the new key:

- **`scripts/bash/update-agent-context.sh`** — add a file-path variable and a case in `update_specific_agent()`.
- **`scripts/powershell/update-agent-context.ps1`** — add a file-path variable, add the new key to the `AgentType` parameter's `[ValidateSet(...)]`, add a switch case in `Update-SpecificAgent`, and add an entry in `Update-AllExistingAgents`.

### 5. Test it

```bash
# Install into a test project
specify init my-project --integration <key>

# Verify files were created in the commands directory configured by
# config["folder"] + config["commands_subdir"] (for example, .windsurf/workflows/)
ls -R my-project/.windsurf/workflows/

# Uninstall cleanly
cd my-project && specify integration uninstall <key>
```

Each integration also has a dedicated test file at `tests/integrations/test_integration_<key>.py`. Note that hyphens in the key are replaced with underscores in the filename (e.g., key `cursor-agent` → `test_integration_cursor_agent.py`, key `kiro-cli` → `test_integration_kiro_cli.py`). Run it with:

```bash
pytest tests/integrations/test_integration_<key_with_underscores>.py -v
```

### 6. Optional overrides

The base classes handle most work automatically. Override only when the agent deviates from standard patterns:

| Override | When to use | Example |
|---|---|---|
| `command_filename(template_name)` | Custom file naming or extension | Copilot → `speckit.{name}.agent.md` |
| `options()` | Integration-specific CLI flags via `--integration-options` | Codex → `--skills` flag |
| `setup()` | Custom install logic (companion files, settings merge) | Copilot → `.agent.md` + `.prompt.md` + `.vscode/settings.json` |
| `teardown()` | Custom uninstall logic | Rarely needed; base handles manifest-tracked files |

**Example — Copilot (fully custom `setup`):**

Copilot extends `IntegrationBase` directly because it creates `.agent.md` commands, companion `.prompt.md` files, and merges `.vscode/settings.json`. See `src/specify_cli/integrations/copilot/__init__.py` for the full implementation.

### 7. Update Devcontainer files (Optional)

For agents that have VS Code extensions or require CLI installation, update the devcontainer configuration files:

#### VS Code Extension-based Agents

For agents available as VS Code extensions, add them to `.devcontainer/devcontainer.json`:

```jsonc
{
  "customizations": {
    "vscode": {
      "extensions": [
        // ... existing extensions ...
        "[New Agent Extension ID]"
      ]
    }
  }
}
```

#### CLI-based Agents

For agents that require CLI tools, add installation commands to `.devcontainer/post-create.sh`:

```bash
#!/bin/bash

# Existing installations...

echo -e "\n🤖 Installing [New Agent Name] CLI..."
# run_command "npm install -g [agent-cli-package]@latest"
echo "✅ Done"
```

---

## Command File Formats

### Markdown Format

**Standard format:**

```markdown
---
description: "Command description"
---

Command content with {SCRIPT} and $ARGUMENTS placeholders.
```

**GitHub Copilot Chat Mode format:**

```markdown
---
description: "Command description"
mode: speckit.command-name
---

Command content with {SCRIPT} and $ARGUMENTS placeholders.
```

### TOML Format

```toml
description = "Command description"

prompt = """
Command content with {SCRIPT} and {{args}} placeholders.
"""
```

### YAML Format

Used by: Goose

```yaml
version: 1.0.0
title: "Command Title"
description: "Command description"
author:
  contact: spec-kit
extensions:
  - type: builtin
    name: developer
activities:
  - Spec-Driven Development
prompt: |
  Command content with {SCRIPT} and {{args}} placeholders.
```

## Argument Patterns

Different agents use different argument placeholders. The placeholder used in command files is always taken from `registrar_config["args"]` for each integration — check there first when in doubt:

- **Markdown/prompt-based**: `$ARGUMENTS` (default for most markdown agents)
- **TOML-based**: `{{args}}` (e.g., Gemini)
- **YAML-based**: `{{args}}` (e.g., Goose)
- **Custom**: some agents override the default (e.g., Forge uses `{{parameters}}`)
- **Script placeholders**: `{SCRIPT}` (replaced with actual script path)
- **Agent placeholders**: `__AGENT__` (replaced with agent name)

## Special Processing Requirements

Some agents require custom processing beyond the standard template transformations:

### Copilot Integration

GitHub Copilot has unique requirements:
- Commands use `.agent.md` extension (not `.md`)
- Each command gets a companion `.prompt.md` file in `.github/prompts/`
- Installs `.vscode/settings.json` with prompt file recommendations
- Context file lives at `.github/copilot-instructions.md`

Implementation: Extends `IntegrationBase` with custom `setup()` method that:
1. Processes templates with `process_template()`
2. Generates companion `.prompt.md` files
3. Merges VS Code settings

### Forge Integration

Forge has special frontmatter and argument requirements:
- Uses `{{parameters}}` instead of `$ARGUMENTS`
- Strips `handoffs` frontmatter key (Forge-specific collaboration feature)
- Injects `name` field into frontmatter when missing

Implementation: Extends `MarkdownIntegration` with custom `setup()` method that:
1. Inherits standard template processing from `MarkdownIntegration`
2. Adds extra `$ARGUMENTS` → `{{parameters}}` replacement after template processing
3. Applies Forge-specific transformations via `_apply_forge_transformations()`
4. Strips `handoffs` frontmatter key
5. Injects missing `name` fields
6. Ensures the shared `update-agent-context.*` scripts include a `forge` case that maps context updates to `AGENTS.md` and lists `forge` in their usage/help text

### Goose Integration

Goose is a YAML-format agent using Block's recipe system:
- Uses `.goose/recipes/` directory for YAML recipe files
- Uses `{{args}}` argument placeholder
- Produces YAML with `prompt: |` block scalar for command content

Implementation: Extends `YamlIntegration` (parallel to `TomlIntegration`):
1. Processes templates through the standard placeholder pipeline
2. Extracts title and description from frontmatter
3. Renders output as Goose recipe YAML (version, title, description, author, extensions, activities, prompt)
4. Uses `yaml.safe_dump()` for header fields to ensure proper escaping
5. Context updates map to `AGENTS.md` (shared with opencode/codex/pi/forge)

## Common Pitfalls

1. **Using shorthand keys for CLI-based integrations**: For CLI-based integrations (`requires_cli: True`), the `key` must match the executable name (e.g., `"cursor-agent"` not `"cursor"`). `shutil.which(key)` is used for CLI tool checks — mismatches require special-case mappings. IDE-based integrations (`requires_cli: False`) are not subject to this constraint.
2. **Forgetting update scripts**: Both bash and PowerShell thin wrappers and the shared context-update scripts must be updated.
3. **Incorrect `requires_cli` value**: Set to `True` only for agents that have a CLI tool; set to `False` for IDE-based agents.
4. **Wrong argument format**: Use `$ARGUMENTS` for Markdown agents, `{{args}}` for TOML agents.
5. **Skipping registration**: The import and `_register()` call in `_register_builtins()` must both be added.

---

*This documentation should be updated whenever new integrations are added to maintain accuracy and completeness.*



---

# FILE: CHANGELOG.md

# Changelog

<!-- insert new changelog below this comment -->

## [0.6.2] - 2026-04-13

### Changed

- feat: Register "What-if Analysis" community extension (#2182)
- feat: add GitHub Issues Integration to community catalog (#2188)
- feat(agents): add Goose AI agent support (#2015)
- Update ralph extension to v1.0.1 in community catalog (#2192)
- fix: skip docs deployment workflow on forks (#2171)
- chore: release 0.6.1, begin 0.6.2.dev0 development (#2162)

## [0.6.1] - 2026-04-10

### Changed

- feat: add bundled lean preset with minimal workflow commands (#2161)
- Add Brownfield Bootstrap extension to community catalog (#2145)
- Add CI Guard extension to community catalog (#2157)
- Add SpecTest extension to community catalog (#2159)
- fix: bundled extensions should not have download URLs (#2155)
- Add PR Bridge extension to community catalog (#2148)
- feat(cursor-agent): migrate from .cursor/commands to .cursor/skills (#2156)
- Add TinySpec extension to community catalog (#2147)
- chore: bump spec-kit-verify to 1.0.3 and spec-kit-review to 1.0.1 (#2146)
- Add Status Report extension to community catalog (#2123)
- chore: release 0.6.0, begin 0.6.1.dev0 development (#2144)

## [0.6.0] - 2026-04-09

### Changed

- Add Bugfix Workflow community extension to catalog and README (#2135)
- Add Worktree Isolation extension to community catalog (#2143)
- Add multi-repo-branching preset to community catalog (#2139)
- Readme clarity (#2013)
- Rewrite AGENTS.md for integration architecture (#2119)
- docs: add SpecKit Companion to Community Friends section (#2140)
- feat: add memorylint extension to community catalog (#2138)
- chore: release 0.5.1, begin 0.5.2.dev0 development (#2137)

## [0.5.1] - 2026-04-08

### Changed

- fix: pin typer>=0.24.0 and click>=8.2.1 to fix import crash (#2136)
- feat: update fleet extension to v1.1.0 (#2029)
- fix(forge): use hyphen notation in frontmatter name field (#2075)
- fix(bash): sed replacement escaping, BSD portability, dead cleanup in update-agent-context.sh (#2090)
- Add Spec Diagram community extension to catalog and README (#2129)
- feat: Git extension stage 2 — GIT_BRANCH_NAME override, --force for existing dirs, auto-install tests (#1940) (#2117)
- fix(git): surface checkout errors for existing branches (#2122)
- Add Branch Convention community extension to catalog and README (#2128)
- docs: lighten March 2026 newsletter for readability (#2127)
- fix: restore alias compatibility for community extensions (#2110) (#2125)
- Added March 2026 newsletter (#2124)
- Add Spec Refine community extension to catalog and README (#2118)
- Add explicit-task-dependencies community preset to catalog and README (#2091)
- Add toc-navigation community preset to catalog and README (#2080)
- fix: prevent ambiguous TOML closing quotes when body ends with `"` (#2113) (#2115)
- fix speckit issue for trae (#2112)
- feat: Git extension stage 1 — bundled `extensions/git` with hooks on all core commands (#1941)
- Upgraded confluence extension to v.1.1.1 (#2109)
- Update V-Model Extension Pack to v0.5.0 (#2108)
- Add canon extension and canon-core preset. (#2022)
- [stage2] fix: serialize multiline descriptions in legacy TOML renderer (#2097)
- [stage1] fix: strip YAML frontmatter from TOML integration prompts (#2096)
- Add Confluence extension (#2028)
- fix: accept 4+ digit spec numbers in tests and docs (#2094)
- fix(scripts): improve git branch creation error handling (#2089)
- Add optimize extension to community catalog (#2088)
- feat: add "VS Code Ask Questions" preset (#2086)
- Add security-review v1.1.1 to community extensions catalog (#2073)
- Add `specify integration` subcommand for post-init integration management (#2083)
- Remove template version info from CLI, fix Claude user-invocable, cleanup dead code (#2081)
- fix: add user-invocable: true to skill frontmatter (#2077)
- fix: add actions:write permission to stale workflow (#2079)
- feat: add argument-hint frontmatter to Claude Code commands (#1951) (#2059)
- Update conduct extension to v1.0.1 (#2078)
- chore(deps): bump astral-sh/setup-uv from 7.6.0 to 8.0.0 (#2072)
- chore(deps): bump actions/configure-pages from 5 to 6 (#2071)
- feat: add spec-kit-fixit extension to community catalog (#2024)
- chore: release 0.5.0, begin 0.5.1.dev0 development (#2070)
- feat: add Forgecode agent support (#2034)

## [0.5.0] - 2026-04-02

### Changed

- Introduces DEVELOPMENT.md (#2069)
- Update cc-sdd reference to cc-spex in Community Friends (#2007)
- chore: release 0.4.5, begin 0.4.6.dev0 development (#2064)

## [0.4.5] - 2026-04-02

### Changed

- Stage 6: Complete migration — remove legacy scaffold path (#1924) (#2063)
- Install Claude Code as native skills and align preset/integration flows (#2051)
- Add repoindex 0402 (#2062)
- Stage 5: Skills, Generic & Option-Driven Integrations (#1924) (#2052)
- feat(scripts): add --dry-run flag to create-new-feature (#1998)
- fix: support feature branch numbers with 4+ digits (#2040)
- Add community content disclaimers (#2058)
- docs: add community extensions website link to README and extensions docs (#2014)
- docs: remove dead Cognitive Squad and Understanding extension links and from extensions/catalog.community.json (#2057)
- Add fix-findings extension to community catalog (#2039)
- Stage 4: TOML integrations — gemini and tabnine migrated to plugin architecture (#2050)
- feat: add 5 lifecycle extensions to community catalog (#2049)
- Stage 3: Standard markdown integrations — 19 agents migrated to plugin architecture (#2038)
- chore: release 0.4.4, begin 0.4.5.dev0 development (#2048)

## [0.4.4] - 2026-04-01

### Changed

- Stage 2: Copilot integration — proof of concept with shared template primitives (#2035)
- docs: sync AGENTS.md with AGENT_CONFIG for missing agents (#2025)
- docs: ensure manual tests use local specify (#2020)
- Stage 1: Integration foundation — base classes, manifest system, and registry (#1925)
- fix: harden GitHub Actions workflows (#2021)
- chore: use PEP 440 .dev0 versions on main after releases (#2032)
- feat: add superpowers bridge extension to community catalog (#2023)
- feat: add product-forge extension to community catalog (#2012)
- feat(scripts): add --allow-existing-branch flag to create-new-feature (#1999)
- fix(scripts): add correct path for copilot-instructions.md (#1997)
- Update README.md (#1995)
- fix: prevent extension command shadowing (#1994)
- Fix Claude Code CLI detection for npm-local installs (#1978)
- fix(scripts): honor PowerShell agent and script filters (#1969)
- feat: add MAQA extension suite (7 extensions) to community catalog (#1981)
- feat: add spec-kit-onboard extension to community catalog (#1991)
- Add plan-review-gate to community catalog (#1993)
- chore(deps): bump actions/deploy-pages from 4 to 5 (#1990)
- chore(deps): bump DavidAnson/markdownlint-cli2-action from 19 to 23 (#1989)
- chore: bump version to 0.4.3 (#1986)

## [0.4.3] - 2026-03-26

### Changed

- Unify Kimi/Codex skill naming and migrate legacy dotted Kimi dirs (#1971)
- fix(ps1): replace null-conditional operator for PowerShell 5.1 compatibility (#1975)
- chore: bump version to 0.4.2 (#1973)

## [0.4.2] - 2026-03-25

### Changed

- feat: Auto-register ai-skills for extensions whenever applicable (#1840)
- docs: add manual testing guide for slash command validation (#1955)
- Add AIDE, Extensify, and Presetify to community extensions (#1961)
- docs: add community presets section to main README (#1960)
- docs: move community extensions table to main README for discoverability (#1959)
- docs(readme): consolidate Community Friends sections and fix ToC anchors (#1958)
- fix(commands): rename NFR references to success criteria in analyze and clarify (#1935)
- Add Community Friends section to README (#1956)
- docs: add Community Friends section with Spec Kit Assistant VS Code extension (#1944)

## [0.4.1] - 2026-03-24

### Changed

- Add checkpoint extension (#1947)
- fix(scripts): prioritize .specify over git for repo root detection (#1933)
- docs: add AIDE extension demo to community projects (#1943)
- fix(templates): add missing Assumptions section to spec template (#1939)

## [0.4.0] - 2026-03-23

### Changed

- fix(cli): add allow_unicode=True and encoding="utf-8" to YAML I/O (#1936)
- fix(codex): native skills fallback refresh + legacy prompt suppression (#1930)
- feat(cli): embed core pack in wheel for offline/air-gapped deployment (#1803)
- ci: increase stale workflow operations-per-run to 250 (#1922)
- docs: update publishing guide with Category and Effect columns (#1913)
- fix: Align native skills frontmatter with install_ai_skills (#1920)
- feat: add timestamp-based branch naming option for `specify init` (#1911)
- docs: add Extension Comparison Guide for community extensions (#1897)
- docs: update SUPPORT.md, fix issue templates, add preset submission template (#1910)
- Add support for Junie (#1831)
- feat: migrate Codex/agy init to native skills workflow (#1906)

## [0.3.2] - 2026-03-19

### Changed

- Add conduct extension to community catalog (#1908)
- feat(extensions): add verify-tasks extension to community catalog (#1871)
- feat(presets): add enable/disable toggle and update semantics (#1891)
- feat: add iFlow CLI support (#1875)
- feat(commands): wire before/after hook events into specify and plan templates (#1886)
- docs(catalog): add speckit-utils to community catalog (#1896)
- docs: Add Extensions & Presets section to README (#1898)
- chore: update DocGuard extension to v0.9.11 (#1899)
- Update cognitive-squad catalog entry — Triadic Model, full lifecycle (#1884)
- feat: register spec-kit-iterate extension (#1887)
- fix(scripts): add explicit positional binding to PowerShell create-new-feature params (#1885)
- fix(scripts): encode residual JSON control chars as \uXXXX instead of stripping (#1872)
- chore: update DocGuard extension to v0.9.10 (#1890)
- Feature/spec kit add pi coding agent pullrequest (#1853)
- feat: register spec-kit-learn extension (#1883)

## [0.3.1] - 2026-03-17

### Changed

- docs: add greenfield Spring Boot pirate-speak preset demo to README (#1878)
- fix(ai-skills): exclude non-speckit copilot agent markdown from skills (#1867)
- feat: add Trae IDE support as a new agent (#1817)
- feat(cli): polite deep merge for settings.json and support JSONC (#1874)
- feat(extensions,presets): add priority-based resolution ordering (#1855)
- fix(scripts): suppress stdout from git fetch in create-new-feature.sh (#1876)
- fix(scripts): harden bash scripts — escape, compat, and error handling (#1869)
- Add cognitive-squad to community extension catalog (#1870)
- docs: add Go / React brownfield walkthrough to community walkthroughs (#1868)
- chore: update DocGuard extension to v0.9.8 (#1859)
- Feature: add specify status command (#1837)
- fix(extensions): show extension ID in list output (#1843)
- feat(extensions): add Archive and Reconcile extensions to community catalog (#1844)
- feat: Add DocGuard CDD enforcement extension to community catalog (#1838)

## [0.3.0] - 2026-03-13

### Changed

- feat(presets): Pluggable preset system with catalog, resolver, and skills propagation (#1787)
- fix: match 'Last updated' timestamp with or without bold markers (#1836)
- Add specify doctor command for project health diagnostics (#1828)
- fix: harden bash scripts against shell injection and improve robustness (#1809)
- fix: clean up command templates (specify, analyze) (#1810)
- fix: migrate Qwen Code CLI from TOML to Markdown format (#1589) (#1730)
- fix(cli): deprecate explicit command support for agy (#1798) (#1808)
- Add /selftest.extension core extension to test other extensions (#1758)
- feat(extensions): Quality of life improvements for RFC-aligned catalog integration (#1776)
- Add Java brownfield walkthrough to community walkthroughs (#1820)

## [0.2.1] - 2026-03-11

### Changed

- Added February 2026 newsletter (#1812)
- feat: add Kimi Code CLI agent support (#1790)
- docs: fix broken links in quickstart guide (#1759) (#1797)
- docs: add catalog cli help documentation (#1793) (#1794)
- fix: use quiet checkout to avoid exception on git checkout (#1792)
- feat(extensions): support .extensionignore to exclude files during install (#1781)
- feat: add Codex support for extension command registration (#1767)

## [0.2.0] - 2026-03-09

### Changed

- fix: sync agent list comments with actual supported agents (#1785)
- feat(extensions): support multiple active catalogs simultaneously (#1720)
- Pavel/add tabnine cli support (#1503)
- Add Understanding extension to community catalog (#1778)
- Add ralph extension to community catalog (#1780)
- Update README with project initialization instructions (#1772)
- feat: add review extension to community catalog (#1775)
- Add fleet extension to community catalog (#1771)
- Integration of Mistral vibe support into speckit (#1725)
- fix: Remove duplicate options in specify.md (#1765)
- fix: use global branch numbering instead of per-short-name detection (#1757)
- Add Community Walkthroughs section to README (#1766)
- feat(extensions): add Jira Integration to community catalog (#1764)
- Add Azure DevOps Integration extension to community catalog (#1734)
- Fix docs: update Antigravity link and add initialization example (#1748)
- fix: wire after_tasks and after_implement hook events into command templates (#1702)
- make c ignores consistent with c++ (#1747)

## [0.1.13] - 2026-03-03

### Changed

- feat: add kiro-cli and AGENT_CONFIG consistency coverage (#1690)
- feat: add verify extension to community catalog (#1726)
- Add Retrospective Extension to community catalog README table (#1741)
- fix(scripts): add empty description validation and branch checkout error handling (#1559)
- fix: correct Copilot extension command registration (#1724)
- fix(implement): remove Makefile from C ignore patterns (#1558)
- Add sync extension to community catalog (#1728)
- fix(checklist): clarify file handling behavior for append vs create (#1556)
- fix(clarify): correct conflicting question limit from 10 to 5 (#1557)

## [0.1.12] - 2026-03-02

### Changed

- fix: use RELEASE_PAT so tag push triggers release workflow (#1736)

## [0.1.11] - 2026-03-02

### Changed

- fix: release-trigger uses release branch + PR instead of direct push to main (#1733)
- fix: Split release process to sync pyproject.toml version with git tags (#1732)

## [0.1.10] - 2026-02-27

### Changed

- fix: prepend YAML frontmatter to Cursor .mdc files (#1699)

## [0.1.9] - 2026-02-28

### Changed

- chore(deps): bump astral-sh/setup-uv from 6 to 7 (#1709)

## [0.1.8] - 2026-02-28

### Changed

- chore(deps): bump actions/setup-python from 5 to 6 (#1710)

## [0.1.7] - 2026-02-27

### Changed

- chore: Update outdated GitHub Actions versions (#1706)
- docs: Document dual-catalog system for extensions (#1689)
- Fix version command in documentation (#1685)
- Add Cleanup Extension to README (#1678)
- Add retrospective extension to community catalog (#1681)

## [0.1.6] - 2026-02-23

### Changed

- Add Cleanup Extension to catalog (#1617)
- Fix parameter ordering issues in CLI (#1669)
- Update V-Model Extension Pack to v0.4.0 (#1665)
- docs: Fix doc missing step (#1496)
- Update V-Model Extension Pack to v0.3.0 (#1661)

## [0.1.5] - 2026-02-21

### Changed

- Fix #1658: Add commands_subdir field to support non-standard agent directory structures (#1660)
- feat: add GitHub issue templates (#1655)
- Update V-Model Extension Pack to v0.2.0 in community catalog (#1656)
- Add V-Model Extension Pack to catalog (#1640)
- refactor: remove OpenAPI/GraphQL bias from templates (#1652)

## [0.1.4] - 2026-02-20

### Changed

- fix: rename Qoder AGENT_CONFIG key from 'qoder' to 'qodercli' to match actual CLI executable (#1651)

## [0.1.3] - 2026-02-20

### Changed

- Add generic agent support with customizable command directories (#1639)

## [0.1.2] - 2026-02-20

### Changed

- fix: pin click>=8.1 to prevent Python 3.14/Homebrew env isolation crash (#1648)

## [0.0.102] - 2026-02-20

### Changed

- fix: include 'src/**' path in release workflow triggers (#1646)

## [0.0.101] - 2026-02-19

### Changed

- chore(deps): bump github/codeql-action from 3 to 4 (#1635)

## [0.0.100] - 2026-02-19

### Changed

- Add pytest and Python linting (ruff) to CI (#1637)
- feat: add pull request template for better contribution guidelines (#1634)

## [0.0.99] - 2026-02-19

### Changed

- Feat/ai skills (#1632)

## [0.0.98] - 2026-02-19

### Changed

- chore(deps): bump actions/stale from 9 to 10 (#1623)
- feat: add dependabot configuration for pip and GitHub Actions updates (#1622)

## [0.0.97] - 2026-02-18

### Changed

- Remove Maintainers section from README.md (#1618)

## [0.0.96] - 2026-02-17

### Changed

- fix: typo in plan-template.md (#1446)

## [0.0.95] - 2026-02-12

### Changed

- Feat: add a new agent: Google Anti Gravity (#1220)

## [0.0.94] - 2026-02-11

### Changed

- Add stale workflow for 180-day inactive issues and PRs (#1594)

## [0.0.93] - 2026-02-10

### Changed

- Add modular extension system (#1551)

## [0.0.92] - 2026-02-10

### Changed

- Fixes #1586 - .specify.specify path error (#1588)

## [0.0.91] - 2026-02-09

### Changed

- fix: preserve constitution.md during reinitialization (#1541) (#1553)
- fix: resolve markdownlint errors across documentation (#1571)

## [0.0.90] - 2025-12-04

### Changed

- Update Markdown formatting
- Update Markdown formatting
- docs: Add existing project initialization to getting started

## [0.0.89] - 2025-12-02

### Changed

- Update scripts/bash/create-new-feature.sh
- fix(scripts): prevent octal interpretation in feature number parsing
- fix: remove unused short_name parameter from branch numbering functions
- Update scripts/powershell/create-new-feature.ps1
- Update scripts/bash/create-new-feature.sh
- fix: use global maximum for branch numbering to prevent collisions

## [0.0.88] - 2025-12-01

### Changed

- fix the incorrect task-template file path

## [0.0.87] - 2025-12-01

### Changed

- Limit width and height to 200px to match the small logo
- docs: Switch readme logo to logo_large.webp
- fix:merge
- fix
- fix
- feat:qoder agent
- docs: Enhance quickstart guide with admonitions and examples
- docs: add constitution step to quickstart guide (fixes #906)
- Update supported AI agents in README.md
- cancel:test
- test
- fix:literal bug
- fix:test
- test
- fix:qoder url
- fix:download owner
- test
- feat:support Qoder CLI

## [0.0.86] - 2025-11-26

### Changed

- feat: add bob to new update-agent-context.ps1 + consistency in comments
- feat: add support for IBM Bob IDE

## [0.0.85] - 2025-11-14

### Changed

- Unset CDPATH while getting SCRIPT_DIR

## [0.0.84] - 2025-11-14

### Changed

- docs: fix broken link and improve agent reference
- docs: reorganize upgrade documentation structure
- docs: remove related documentation section from upgrading guide
- fix: remove broken link to existing project guide
- docs: Add comprehensive upgrading guide for Spec Kit
- Refactor ESLint configuration checks in implement.md to address deprecation

## [0.0.83] - 2025-11-14

### Changed

- feat: Add OVHcloud SHAI AI Agent

## [0.0.82] - 2025-11-14

### Changed

- fix: incorrect logic to create release packages with subset AGENTS or SCRIPTS

## [0.0.81] - 2025-11-14

### Changed

- Fix tasktoissues.md to use the 'github/github-mcp-server/issue_write' tool

## [0.0.80] - 2025-11-14

### Changed

- Refactor feature script logic and update agent context scripts
- Update templates/commands/taskstoissues.md
- Update CHANGELOG.md
- Update agent configuration
- Update scripts/powershell/create-new-feature.ps1
- Update src/specify_cli/__init__.py
- Create create-release-packages.ps1
- Script changes
- Update taskstoissues.md
- Create taskstoissues.md
- Update src/specify_cli/__init__.py
- Update CONTRIBUTING.md
- Potential fix for code scanning alert no. 3: Workflow does not contain permissions
- Update src/specify_cli/__init__.py
- Update CHANGELOG.md
- Fixes #970
- Fixes #975
- Support for version command
- Exclude generated releases
- Lint fixes
- Prompt updates
- Hand offs with prompts
- Chatmodes are back in vogue
- Let's switch to proper prompts
- Update prompts
- Update with prompt
- Testing hand-offs
- Use VS Code handoffs

## [0.0.79] - 2025-10-23

### Changed

- docs: restore important note about JSON output in specify command
- fix: improve branch number detection to check all sources
- feat: check remote branches to prevent duplicate branch numbers

## [0.0.78] - 2025-10-21

### Changed

- Update CONTRIBUTING.md
- docs: add steps for testing template and command changes locally
- update specify to make "short-name" argu for create-new-feature.sh in the right position

## [0.0.77] - 2025-10-21

### Changed

- fix: include the latest changelog in the `GitHub Release`'s  body

## [0.0.76] - 2025-10-21

### Changed

- Fix update-agent-context.sh to handle files without Active Technologies/Recent Changes sections

## [0.0.75] - 2025-10-21

### Changed

- Fixed indentation.
- Added correct `install_url` for Amp agent CLI script.
- Added support for Amp code agent.

## [0.0.74] - 2025-10-21

### Changed

- feat(ci): add markdownlint-cli2 for consistent markdown formatting

## [0.0.73] - 2025-10-21

### Changed

- revert vscode auto remove extra space
- fix: correct command references in implement.md
- fix regarding copilot suggestion
- fix: correct command references in speckit.analyze.md
- Support more lang/Devops of Common Patterns by Technology
- chore: replace `bun` by `node/npm` in the `devcontainer` (as many CLI-based agents actually require a `node` runtime)
- chore: add Claude Code extension to devcontainer configuration
- chore: add installation of `codebuddy` CLI in the `devcontainer`
- chore: fix path to powershell script in vscode settings
- fix: correct `run_command` exit behavior and improve installation instructions (for `Amazon Q`) in `post-create.sh` + fix typos in `CONTRIBUTING.md`
- chore: add `specify`'s github copilot chat settings to `devcontainer`
- chore: add `devcontainer` support  to ease developer workstation setup

## [0.0.72] - 2025-10-18

### Changed

- fix: correct argument parsing in create-new-feature.sh script

## [0.0.71] - 2025-10-18

### Changed

- fix: Skip CLI checks for IDE-based agents in check command
- Change loop condition to include last argument

## [0.0.70] - 2025-10-18

### Changed

- fix: broken media files
- Update README.md
- The function parameters lack type hints. Consider adding type annotations for better code clarity and IDE support.
- - **Smart JSON Merging for VS Code Settings**: `.vscode/settings.json` is now intelligently merged instead of being overwritten during `specify init --here` or `specify init .`   - Existing settings are preserved   - New Spec Kit settings are added   - Nested objects are merged recursively   - Prevents accidental loss of custom VS Code workspace configurations
- Fix: incorrect command formatting in agent context file, refix #895

## [0.0.69] - 2025-10-15

### Changed

- Update scripts/bash/create-new-feature.sh
- Update create-new-feature.sh
- Update files
- Update files
- Create .gitattributes
- Update wording
- Update logic for arguments
- Update script logic

## [0.0.68] - 2025-10-15

### Changed

- format content as copilot suggest
- Ruby, PHP, Rust, Kotlin, C, C++

## [0.0.67] - 2025-10-15

### Changed

- Use the number prefix to find the right spec

## [0.0.66] - 2025-10-15

### Changed

- Update CodeBuddy agent name to 'CodeBuddy CLI'
- Rename CodeBuddy to CodeBuddy CLI in update script
- Update AI coding agent references in installation guide
- Rename CodeBuddy to CodeBuddy CLI in AGENTS.md
- Update README.md
- Update CodeBuddy link in README.md
- update codebuddyCli

## [0.0.65] - 2025-10-15

### Changed

- Fix: Fix incorrect command formatting in agent context file
- docs: fix heading capitalization for consistency
- Update README.md

## [0.0.64] - 2025-10-14

### Changed

- Update tasks.md
- Update README.md

## [0.0.63] - 2025-10-14

### Changed

- fix: update CODEBUDDY file path in agent context scripts
- docs(readme): add /speckit.tasks step and renumber walkthrough

## [0.0.62] - 2025-10-11

### Changed

- A few more places to update from code review
- fix: align Cursor agent naming to use 'cursor-agent' consistently

## [0.0.61] - 2025-10-10

### Changed

- Update clarify.md
- add how to upgrade specify installation

## [0.0.60] - 2025-10-10

### Changed

- Update vscode-settings.json
- Update instructions and bug fix

## [0.0.59] - 2025-10-10

### Changed

- Update __init__.py
- Consolidate Cursor naming
- Update CHANGELOG.md
- Git errors are now highlighted.
- Update __init__.py
- Refactor agent configuration
- Update src/specify_cli/__init__.py
- Update scripts/powershell/update-agent-context.ps1
- Update AGENTS.md
- Update templates/commands/implement.md
- Update templates/commands/implement.md
- Update CHANGELOG.md
- Update changelog
- Update plan.md
- Add ignore file verification step to /speckit.implement command
- Escape backslashes in TOML outputs
- update CodeBuddy to international site
- feat: support codebuddy ai
- feat: support codebuddy ai

## [0.0.58] - 2025-10-08

### Changed

- Add escaping guidelines to command templates
- Update README.md
- Update README.md

## [0.0.57] - 2025-10-06

### Changed

- Update CHANGELOG.md
- Update command reference
- Package up VS Code settings for Copilot
- Update tasks-template.md
- Update templates/tasks-template.md
- Cleanup
- Update CLI changes
- Update template and docs
- Update checklist.md
- Update templates
- Cleanup redundancies
- Update checklist.md
- Codex CLI is now fully supported
- Update specify.md
- Prompt updates
- Update prompt prefix
- Update .github/workflows/scripts/create-release-packages.sh
- Consistency updates to commands
- Update commands.
- Update logs
- Template cleanup and reorganization
- Remove Codex named args limitation warning
- Remove Codex named args limitation from README.md

## [0.0.56] - 2025-10-02

### Changed

- docs(readme): link Amazon Q slash command limitation issue
- docs: clarify Amazon Q limitation and update init docstring
- feat(agent): Added Amazon Q Developer CLI Integration

## [0.0.55] - 2025-09-30

### Changed

- Update URLs to Contributing and Support Guides in Docs
- fix: add UTF-8 encoding to file read/write operations in update-agent-context.ps1
- Update __init__.py
- Update src/specify_cli/__init__.py
- docs: fix the paths of generated files (moved under a `.specify/` folder)
- Update src/specify_cli/__init__.py
- feat: support 'specify init .' for current directory initialization
- feat: Add emacs-style up/down keys

## [0.0.54] - 2025-09-25

### Changed

- Update CONTRIBUTING.md
- Refine `plan-template.md` with improved project type detection, clarified structure decision process, and enhanced research task guidance.
- Update __init__.py

## [0.0.53] - 2025-09-24

### Changed

- Update template path for spec file creation
- Update template path for spec file creation
- docs: remove constitution_update_checklist from README

## [0.0.52] - 2025-09-22

### Changed

- Update analyze.md
- Update templates/commands/analyze.md
- Update templates/commands/clarify.md
- Update templates/commands/plan.md
- Update with extra commands
- Update with --force flag
- feat: add uv tool install instructions to README

## [0.0.51] - 2025-09-21

### Changed

- Update with Roo Code support

## [0.0.50] - 2025-09-21

### Changed

- Update generate-release-notes.sh
- Update error messages
- Auggie folder fix

## [0.0.49] - 2025-09-21

### Changed

- Update scripts/powershell/update-agent-context.ps1
- Update templates/commands/implement.md
- Cleanup the check command
- Add support for Auggie
- Update AGENTS.md
- Updates with Kilo Code support
- Update README.md
- Update templates/commands/constitution.md
- Update templates/commands/implement.md
- Update templates/commands/plan.md
- Update templates/commands/specify.md
- Update templates/commands/tasks.md
- Update README.md
- Stop splitting the warning over multiple lines
- Update templates based on #419
- docs: Update README with codex in check command

## [0.0.48] - 2025-09-21

### Changed

- Update scripts/powershell/check-prerequisites.ps1
- Update CHANGELOG.md
- Update CHANGELOG.md
- Update changelog
- Update scripts/bash/update-agent-context.sh
- Fix script config
- Update scripts/bash/common.sh
- Update scripts/powershell/update-agent-context.ps1
- Update scripts/powershell/update-agent-context.ps1
- Clarification
- Update prompts
- Update update-agent-context.ps1
- Update CONTRIBUTING.md
- Update CONTRIBUTING.md
- Update CONTRIBUTING.md
- Update CONTRIBUTING.md
- Update CONTRIBUTING.md
- Update contribution guidelines.
- Root detection logic
- Update templates/plan-template.md
- Update scripts/bash/update-agent-context.sh
- Update scripts/powershell/create-new-feature.ps1
- Simplification
- Script and template tweaks
- Update config
- Update scripts/powershell/check-prerequisites.ps1
- Update scripts/bash/check-prerequisites.sh
- Fix script path
- Script cleanup
- Update scripts/bash/check-prerequisites.sh
- Update scripts/powershell/check-prerequisites.ps1
- Update script delegation from GitHub Action
- Cleanup the setup for generated packages
- Use proper line endings
- Consolidate scripts

## [0.0.47] - 2025-09-20

### Changed

- Updating agent context files

## [0.0.46] - 2025-09-20

### Changed

- Update update-agent-context.ps1
- Update package release
- Update config
- Update __init__.py
- Update __init__.py
- Remove Codex-specific logic in the initialization script
- Update version rev
- Update __init__.py
- Enhance Codex support by auto-syncing prompt files, allowing spec generation without git, and documenting clearer /specify usage.
- Consistency tweaks
- Consistent step coloring
- Update __init__.py
- Update __init__.py
- Quick UI tweak
- Update package release
- Limit workspace command seeding to Codex init and update Codex documentation accordingly.
- Clarify Codex-specific README note with rationale for its different workflow.
- Bump to 0.0.7 and document Codex support
- Normalize Codex command templates to the scripts-based schema and auto-upgrade generated commands.
- Fix remaining merge conflict markers in __init__.py
- Add Codex CLI support with AGENTS.md and commands bootstrap

## [0.0.45] - 2025-09-19

### Changed

- Update with Windsurf support
- expose token as an argument through cli --github-token
- add github auth headers if there are GITHUB_TOKEN/GH_TOKEN set

## [0.0.44] - 2025-09-18

### Changed

- Update specify.md
- Update __init__.py

## [0.0.43] - 2025-09-18

### Changed

- Update with support for /implement

## [0.0.42] - 2025-09-18

### Changed

- Update constitution.md

## [0.0.41] - 2025-09-18

### Changed

- Update constitution.md

## [0.0.40] - 2025-09-18

### Changed

- Update constitution command

## [0.0.39] - 2025-09-18

### Changed

- Cleanup
- fix: commands format for qwen

## [0.0.38] - 2025-09-18

### Changed

- Fix template path in update-agent-context.sh
- docs: fix grammar mistakes in markdown files

## [0.0.37] - 2025-09-17

### Changed

- fix: add missing Qwen support to release workflow and agent scripts

## [0.0.36] - 2025-09-17

### Changed

- feat: Add opencode ai agent
- Fix --no-git argument resolution.

## [0.0.35] - 2025-09-17

### Changed

- chore(release): bump version to 0.0.5 and update changelog
- chore: address review feedback - remove comment and fix numbering
- feat: add Qwen Code support to Spec Kit

## [0.0.34] - 2025-09-15

### Changed

- Update template.

## [0.0.33] - 2025-09-15

### Changed

- Update scripts

## [0.0.32] - 2025-09-15

### Changed

- Update template paths

## [0.0.31] - 2025-09-15

### Changed

- Update for Cursor rules & script path
- Update Specify definition
- Update README.md
- Update with video header
- fix(docs): remove redundant white space

## [0.0.30] - 2025-09-12

### Changed

- Update update-agent-context.ps1

## [0.0.29] - 2025-09-12

### Changed

- Update create-release-packages.sh
- Update with check changes

## [0.0.28] - 2025-09-12

### Changed

- Update wording
- Update release.yml

## [0.0.27] - 2025-09-12

### Changed

- Support Cursor

## [0.0.26] - 2025-09-12

### Changed

- Saner approach to scripts

## [0.0.25] - 2025-09-12

### Changed

- Update packaging

## [0.0.24] - 2025-09-12

### Changed

- Fix package logic

## [0.0.23] - 2025-09-12

### Changed

- Update config
- Update __init__.py
- Refactor with platform-specific constraints
- Update README.md
- Update CLI reference
- Update __init__.py
- refactor: extract Claude local path to constant for maintainability
- fix: support Claude CLI installed via migrate-installer

## [0.0.22] - 2025-09-11

### Changed

- Update release.yml
- Update create-release-packages.sh
- Update create-release-packages.sh
- Update release file

## [0.0.21] - 2025-09-11

### Changed

- Consolidate script creation
- Update how Copilot prompts are created
- Update local-development.md
- Local dev guide and script updates
- Update CONTRIBUTING.md
- Enhance HTTP client initialization with optional SSL verification and bump version to 0.0.3
- Complete Gemini CLI command instructions
- Refactor HTTP client usage to utilize truststore for SSL context
- docs: Update Commands sections renaming to match implementation
- docs: Fix formatting issues in README.md for consistency
- Update docs and release

## [0.0.20] - 2025-09-08

### Changed

- Update docs/quickstart.md
- Docs setup

## [0.0.19] - 2025-09-08

### Changed

- Update README.md

## [0.0.18] - 2025-09-08

### Changed

- Update README.md

## [0.0.17] - 2025-09-08

### Changed

- Remove trailing whitespace from tasks.md template

## [0.0.16] - 2025-09-07

### Changed

- Fix release workflow to work with repository rules

## [0.0.15] - 2025-09-07

### Changed

- Use `/usr/bin/env bash` instead of `/bin/bash` for shebang

## [0.0.14] - 2025-09-04

### Changed

- fix: correct typos in spec-driven.md

## [0.0.13] - 2025-09-04

### Changed

- Fix formatting in usage instructions

## [0.0.12] - 2025-09-04

### Changed

- Fix template path in plan command documentation

## [0.0.11] - 2025-09-04

### Changed

- fix: incorrect tree structure in examples

## [0.0.10] - 2025-09-04

### Changed

- fix minor typo in Article I

## [0.0.9] - 2025-09-03

### Changed

- Update CLI commands from '/spec' to '/specify'

## [0.0.8] - 2025-09-02

### Changed

- adding executable permission to the scripts so they execute when the coding agent launches them

## [0.0.7] - 2025-09-02

### Changed

- doco(spec-driven): Fix small typo in document

## [0.0.6] - 2025-08-25

### Changed

- Update README.md

## [0.0.5] - 2025-08-25

### Changed

- Update .github/workflows/release.yml
- Fix release workflow to work with repository rules

## [0.0.4] - 2025-08-25

### Changed

- Add John Lam as contributor and release badge

## [0.0.3] - 2025-08-22

### Changed

- Update requirements

## [0.0.2] - 2025-08-22

### Changed

- Update README.md

## [0.0.1] - 2025-08-22

### Changed

- Update release.yml




---

# FILE: CODE_OF_CONDUCT.md

# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or
  advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic
  address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at <opensource@github.com>. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/



---

# FILE: CONTRIBUTING.md

# Contributing to Spec Kit

Hi there! We're thrilled that you'd like to contribute to Spec Kit. Contributions to this project are [released](https://help.github.com/articles/github-terms-of-service/#6-contributions-under-repository-license) to the public under the [project's open source license](LICENSE).

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## Prerequisites for running and testing code

These are one time installations required to be able to test your changes locally as part of the pull request (PR) submission process.

1. Install [Python 3.11+](https://www.python.org/downloads/)
1. Install [uv](https://docs.astral.sh/uv/) for package management
1. Install [Git](https://git-scm.com/downloads)
1. Have an [AI coding agent available](README.md#-supported-ai-agents)

<details>
<summary><b>💡 Hint if you are using <code>VSCode</code> or <code>GitHub Codespaces</code> as your IDE</b></summary>

<br>

Provided you have [Docker](https://docker.com) installed on your machine, you can leverage [Dev Containers](https://containers.dev) through this [VSCode extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers), to easily set up your development environment, with aforementioned tools already installed and configured, thanks to the `.devcontainer/devcontainer.json` file (located at the root of the project).

To do so, simply:

- Checkout the repo
- Open it with VSCode
- Open the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) and select "Dev Containers: Open Folder in Container..."

On [GitHub Codespaces](https://github.com/features/codespaces) it's even simpler, as it leverages the `.devcontainer/devcontainer.json` automatically upon opening the codespace.

</details>

## Submitting a pull request

> [!NOTE]
> If your pull request introduces a large change that materially impacts the work of the CLI or the rest of the repository (e.g., you're introducing new templates, arguments, or otherwise major changes), make sure that it was **discussed and agreed upon** by the project maintainers. Pull requests with large changes that did not have a prior conversation and agreement will be closed.

1. Fork and clone the repository
1. Configure and install the dependencies: `uv sync --extra test`
1. Make sure the CLI works on your machine: `uv run specify --help`
1. Create a new branch: `git checkout -b my-branch-name`
1. Make your change, add tests, and make sure everything still works
1. Test the CLI functionality with a sample project if relevant
1. Push to your fork and submit a pull request
1. Wait for your pull request to be reviewed and merged.

For the detailed test workflow, command-selection prompt, and PR reporting template, see [`TESTING.md`](./TESTING.md).
Activate the project virtual environment (see the Setup block in [`TESTING.md`](./TESTING.md)), then install the CLI from your working tree (`uv pip install -e .` after `uv sync --extra test`) or otherwise ensure the shell uses the local `specify` binary before running the manual slash-command tests described below.

Here are a few things you can do that will increase the likelihood of your pull request being accepted:

- Follow the project's coding conventions.
- Write tests for new functionality.
- Update documentation (`README.md`, `spec-driven.md`) if your changes affect user-facing features.
- Keep your change as focused as possible. If there are multiple changes you would like to make that are not dependent upon each other, consider submitting them as separate pull requests.
- Write a [good commit message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).
- Test your changes with the Spec-Driven Development workflow to ensure compatibility.

## Development workflow

When working on spec-kit:

1. Test changes with the `specify` CLI commands (`/speckit.specify`, `/speckit.plan`, `/speckit.tasks`) in your coding agent of choice
2. Verify templates are working correctly in `templates/` directory
3. Test script functionality in the `scripts/` directory
4. Ensure memory files (`memory/constitution.md`) are updated if major process changes are made

### Recommended validation flow

For the smoothest review experience, validate changes in this order:

1. **Run focused automated checks first** — use the quick verification commands in [`TESTING.md`](./TESTING.md) to catch packaging, scaffolding, and configuration regressions early.
2. **Run manual workflow tests second** — if your change affects slash commands or the developer workflow, follow [`TESTING.md`](./TESTING.md) to choose the right commands, run them in an agent, and capture results for your PR.
3. **Use local release packages when debugging packaged output** — if you need to inspect the exact files CI-style packaging produces, generate local release packages as described below.

### Testing template and command changes locally

Running `uv run specify init` pulls released packages, which won’t include your local changes.  
To test your templates, commands, and other changes locally, follow these steps:

1. **Create release packages**

   Run the following command to generate the local packages:

   ```bash
   ./.github/workflows/scripts/create-release-packages.sh v1.0.0
   ```

2. **Copy the relevant package to your test project**

   ```bash
   cp -r .genreleases/sdd-copilot-package-sh/. <path-to-test-project>/
   ```

3. **Open and test the agent**

   Navigate to your test project folder and open the agent to verify your implementation.

If you only need to validate generated file structure and content before doing manual agent testing, start with the focused automated checks in [`TESTING.md`](./TESTING.md). Keep this section for the cases where you need to inspect the exact packaged output locally.

## AI contributions in Spec Kit

> [!IMPORTANT]
>
> If you are using **any kind of AI assistance** to contribute to Spec Kit,
> it must be disclosed in the pull request or issue.

We welcome and encourage the use of AI tools to help improve Spec Kit! Many valuable contributions have been enhanced with AI assistance for code generation, issue detection, and feature definition.

That being said, if you are using any kind of AI assistance (e.g., agents, ChatGPT) while contributing to Spec Kit,
**this must be disclosed in the pull request or issue**, along with the extent to which AI assistance was used (e.g., documentation comments vs. code generation).

If your PR responses or comments are being generated by an AI, disclose that as well.

As an exception, trivial spacing or typo fixes don't need to be disclosed, so long as the changes are limited to small parts of the code or short phrases.

An example disclosure:

> This PR was written primarily by GitHub Copilot.

Or a more detailed disclosure:

> I consulted ChatGPT to understand the codebase but the solution
> was fully authored manually by myself.

Failure to disclose this is first and foremost rude to the human operators on the other end of the pull request, but it also makes it difficult to
determine how much scrutiny to apply to the contribution.

In a perfect world, AI assistance would produce equal or higher quality work than any human. That isn't the world we live in today, and in most cases
where human supervision or expertise is not in the loop, it's generating code that cannot be reasonably maintained or evolved.

### What we're looking for

When submitting AI-assisted contributions, please ensure they include:

- **Clear disclosure of AI use** - You are transparent about AI use and degree to which you're using it for the contribution
- **Human understanding and testing** - You've personally tested the changes and understand what they do
- **Clear rationale** - You can explain why the change is needed and how it fits within Spec Kit's goals
- **Concrete evidence** - Include test cases, scenarios, or examples that demonstrate the improvement
- **Your own analysis** - Share your thoughts on the end-to-end developer experience

### What we'll close

We reserve the right to close contributions that appear to be:

- Untested changes submitted without verification
- Generic suggestions that don't address specific Spec Kit needs
- Bulk submissions that show no human review or understanding

### Guidelines for success

The key is demonstrating that you understand and have validated your proposed changes. If a maintainer can easily tell that a contribution was generated entirely by AI without human input or testing, it likely needs more work before submission.

Contributors who consistently submit low-effort AI-generated changes may be restricted from further contributions at the maintainers' discretion.

Please be respectful to maintainers and disclose AI assistance.

## Resources

- [Spec-Driven Development Methodology](./spec-driven.md)
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Using Pull Requests](https://help.github.com/articles/about-pull-requests/)
- [GitHub Help](https://help.github.com)



---

# FILE: DEVELOPMENT.md

# Development Notes

Spec Kit is a toolkit for spec-driven development. At its core, it is a coordinated set of prompts, templates, scripts, and CLI/integration assets that define and deliver a spec-driven workflow for AI coding agents. This document is a starting point for people modifying Spec Kit itself, with a compact orientation to the key project documents and repository organization.

**Essential project documents:**

| Document                                                   | Role                                                                                  |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| [README.md](README.md)                                     | Primary user-facing overview of Spec Kit and its workflow.                            |
| [DEVELOPMENT.md](DEVELOPMENT.md)                           | This document.                                                                        |
| [spec-driven.md](spec-driven.md)                           | End-to-end explanation of the Spec-Driven Development workflow supported by Spec Kit. |
| [RELEASE-PROCESS.md](.github/workflows/RELEASE-PROCESS.md) | Release workflow, versioning rules, and changelog generation process.                 |
| [docs/index.md](docs/index.md)                             | Entry point to the `docs/` documentation set.                                         |
| [CONTRIBUTING.md](CONTRIBUTING.md)                         | Contribution process, review expectations, and required development practices.        |
| [TESTING.md](TESTING.md)                                   | Validation strategy and testing procedures.                                           |

**Main repository components:**

| Directory          | Role                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------- |
| `templates/`       | Prompt assets and templates that define the core workflow behavior and generated artifacts. |
| `scripts/`         | Supporting scripts used by the workflow, setup, and repository tooling.                     |
| `src/specify_cli/` | Python source for the `specify` CLI, including agent-specific assets.                       |
| `extensions/`      | Extension-related docs, catalogs, and supporting assets.                                    |
| `presets/`         | Preset-related docs, catalogs, and supporting assets.                                       |



---

# FILE: SECURITY.md

# Security Policy

Thanks for helping make GitHub safe for everyone.

GitHub takes the security of our software products and services seriously, including all of the open source code repositories managed through our GitHub organizations, such as [GitHub](https://github.com/GitHub).

Even though [open source repositories are outside of the scope of our bug bounty program](https://bounty.github.com/index.html#scope) and therefore not eligible for bounty rewards, we will ensure that your finding gets passed along to the appropriate maintainers for remediation.

## Reporting Security Issues

If you believe you have found a security vulnerability in any GitHub-owned repository, please report it to us through coordinated disclosure.

**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**

Instead, please send an email to opensource-security[@]github.com.

Please include as much of the information listed below as you can to help us better understand and resolve the issue:

- The type of issue (e.g., buffer overflow, SQL injection, or cross-site scripting)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit the issue

This information will help us triage your report more quickly.

## Policy

See [GitHub's Safe Harbor Policy](https://docs.github.com/en/site-policy/security-policies/github-bug-bounty-program-legal-safe-harbor#1-safe-harbor-terms)



---

# FILE: SUPPORT.md

# Support

## How to get help

Please search existing [issues](https://github.com/github/spec-kit/issues) and [discussions](https://github.com/github/spec-kit/discussions) before creating new ones to avoid duplicates.

- Review the [README](./README.md) for getting started instructions and troubleshooting tips
- Check the [comprehensive guide](./spec-driven.md) for detailed documentation on the Spec-Driven Development process
- Ask in [GitHub Discussions](https://github.com/github/spec-kit/discussions) for questions about using Spec Kit or the Spec-Driven Development methodology
- Open a [GitHub issue](https://github.com/github/spec-kit/issues/new) for bug reports and feature requests

## Project Status

**Spec Kit** is under active development and maintained by GitHub staff and the community. We will do our best to respond to support, feature requests, and community questions as time permits.

## GitHub Support Policy

Support for this project is limited to the resources listed above.



---

# FILE: TESTING.md

# Testing Guide

This document is the detailed testing companion to [`CONTRIBUTING.md`](./CONTRIBUTING.md).

Use it for three things:

1. running quick automated checks before manual testing,
2. manually testing affected slash commands through an AI agent, and
3. capturing the results in a PR-friendly format.

Any change that affects a slash command's behavior requires manually testing that command through an AI agent and submitting results with the PR.

## Recommended order

1. **Sync your environment** — install the project and test dependencies.
2. **Run focused automated checks** — especially for packaging, scaffolding, agent config, and generated-file changes.
3. **Run manual agent tests** — for any affected slash commands.
4. **Paste results into your PR** — include both command-selection reasoning and manual test results.

## Quick automated checks

Run these before manual testing when your change affects packaging, scaffolding, templates, release artifacts, or agent wiring.

### Environment setup

```bash
cd <spec-kit-repo>
uv sync --extra test
source .venv/bin/activate  # On Windows (CMD): .venv\Scripts\activate  |  (PowerShell): .venv\Scripts\Activate.ps1
```

### Generated package structure and content

```bash
uv run python -m pytest tests/test_core_pack_scaffold.py -q
```

This validates the generated files that CI-style packaging depends on, including directory layout, file names, frontmatter/TOML validity, placeholder replacement, `.specify/` path rewrites, and parity with `create-release-packages.sh`.

### Agent configuration and release wiring consistency

```bash
uv run python -m pytest tests/test_agent_config_consistency.py -q
```

Run this when you change agent metadata, release scripts, context update scripts, or artifact naming.

### Optional single-agent packaging spot check

```bash
AGENTS=copilot SCRIPTS=sh ./.github/workflows/scripts/create-release-packages.sh v1.0.0
```

Inspect `.genreleases/sdd-copilot-package-sh/` and the matching ZIP in `.genreleases/` when you want to review the exact packaged output for one agent/script combination.

## Manual testing process

1. **Identify affected commands** — use the [prompt below](#determining-which-tests-to-run) to have your agent analyze your changed files and determine which commands need testing.
2. **Set up a test project** — scaffold from your local branch (see [Setup](#setup)).
3. **Run each affected command** — invoke it in your agent, verify it completes successfully, and confirm it produces the expected output (files created, scripts executed, artifacts populated).
4. **Run prerequisites first** — commands that depend on earlier commands (e.g., `/speckit.tasks` requires `/speckit.plan` which requires `/speckit.specify`) must be run in order.
5. **Report results** — paste the [reporting template](#reporting-results) into your PR with pass/fail for each command tested.

## Setup

```bash
# Install the project and test dependencies from your local branch
cd <spec-kit-repo>
uv sync --extra test
source .venv/bin/activate  # On Windows (CMD): .venv\Scripts\activate  |  (PowerShell): .venv\Scripts\Activate.ps1
uv pip install -e .
# Ensure the `specify` binary in this environment points at your working tree so the agent runs the branch you're testing.

# Initialize a test project using your local changes
uv run specify init /tmp/speckit-test --ai <agent> --offline
cd /tmp/speckit-test

# Open in your agent
```

If you are testing the packaged output rather than the live source tree, create a local release package first as described in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Reporting results

Paste this into your PR:

~~~markdown
## Manual test results

**Agent**: [e.g., GitHub Copilot in VS Code]  |  **OS/Shell**: [e.g., macOS/zsh]

| Command tested | Notes |
|----------------|-------|
| `/speckit.command` | |
~~~

## Determining which tests to run

Copy this prompt into your agent. Include the agent's response (selected tests plus a brief explanation of the mapping) in your PR.

~~~text
Read TESTING.md, then run `git diff --name-only main` to get my changed files.
For each changed file, determine which slash commands it affects by reading
the command templates in templates/commands/ to understand what each command
invokes. Use these mapping rules:

- templates/commands/X.md → the command it defines
- scripts/bash/Y.sh or scripts/powershell/Y.ps1 → every command that invokes that script (grep templates/commands/ for the script name). Also check transitive dependencies: if the changed script is sourced by other scripts (e.g., common.sh is sourced by create-new-feature.sh, check-prerequisites.sh, setup-plan.sh, update-agent-context.sh), then every command invoking those downstream scripts is also affected
- templates/Z-template.md → every command that consumes that template during execution
- src/specify_cli/*.py → CLI commands (`specify init`, `specify check`, `specify extension *`, `specify preset *`); test the affected CLI command and, for init/scaffolding changes, at minimum test /speckit.specify
- extensions/X/commands/* → the extension command it defines
- extensions/X/scripts/* → every extension command that invokes that script
- extensions/X/extension.yml or config-template.yml → every command in that extension. Also check if the manifest defines hooks (look for `hooks:` entries like `before_specify`, `after_implement`, etc.) — if so, the core commands those hooks attach to are also affected
- presets/*/* → test preset scaffolding via `specify init` with the preset
- pyproject.toml → packaging/bundling; test `specify init` and verify bundled assets

Include prerequisite tests (e.g., T5 requires T3 requires T1).

Output in this format:

### Test selection reasoning

| Changed file | Affects | Test | Why |
|---|---|---|---|
| (path) | (command) | T# | (reason) |

### Required tests

Number each test sequentially (T1, T2, ...). List prerequisite tests first.

- T1: /speckit.command — (reason)
- T2: /speckit.command — (reason)
~~~



---

# FILE: docs/README.md

# Documentation

This folder contains the documentation source files for Spec Kit, built using [DocFX](https://dotnet.github.io/docfx/).

## Building Locally

To build the documentation locally:

1. Install DocFX:

   ```bash
   dotnet tool install -g docfx
   ```

2. Build the documentation:

   ```bash
   cd docs
   docfx docfx.json --serve
   ```

3. Open your browser to `http://localhost:8080` to view the documentation.

## Structure

- `docfx.json` - DocFX configuration file
- `index.md` - Main documentation homepage
- `toc.yml` - Table of contents configuration
- `installation.md` - Installation guide
- `quickstart.md` - Quick start guide
- `_site/` - Generated documentation output (ignored by git)

## Deployment

Documentation is automatically built and deployed to GitHub Pages when changes are pushed to the `main` branch. The workflow is defined in `.github/workflows/docs.yml`.



---

# FILE: docs/docfx.json

{
  "build": {
    "content": [
      {
        "files": [
          "*.md",
          "toc.yml"
        ]
      },
      {
        "files": [
          "../README.md",
          "../CONTRIBUTING.md",
          "../CODE_OF_CONDUCT.md",
          "../SECURITY.md",
          "../SUPPORT.md"
        ],
        "dest": "."
      }
    ],
    "resource": [
      {
        "files": [
          "images/**"
        ]
      },
      {
        "files": [
          "../media/**"
        ],
        "dest": "media"
      }
    ],
    "overwrite": [
      {
        "files": [
          "apidoc/**.md"
        ],
        "exclude": [
          "obj/**",
          "_site/**"
        ]
      }
    ],
    "dest": "_site",
    "globalMetadataFiles": [],
    "fileMetadataFiles": [],
    "template": [
      "default",
      "modern"
    ],
    "postProcessors": [],
    "markdownEngineName": "markdig",
    "noLangKeyword": false,
    "keepFileLink": false,
    "cleanupCacheHistory": false,
    "disableGitFeatures": false,
    "globalMetadata": {
      "_appTitle": "Spec Kit Documentation",
      "_appName": "Spec Kit",
      "_appFooter": "Spec Kit - A specification-driven development toolkit",
      "_enableSearch": true,
      "_disableContribution": false,
      "_gitContribute": {
        "repo": "https://github.com/github/spec-kit",
        "branch": "main"
      }
    }
  }
}




---

# FILE: docs/index.md

# Spec Kit

*Build high-quality software faster.*

**An effort to allow organizations to focus on product scenarios rather than writing undifferentiated code with the help of Spec-Driven Development.**

## What is Spec-Driven Development?

Spec-Driven Development **flips the script** on traditional software development. For decades, code has been king — specifications were just scaffolding we built and discarded once the "real work" of coding began. Spec-Driven Development changes this: **specifications become executable**, directly generating working implementations rather than just guiding them.

## Getting Started

- [Installation Guide](installation.md)
- [Quick Start Guide](quickstart.md)
- [Upgrade Guide](upgrade.md)
- [Local Development](local-development.md)

## Core Philosophy

Spec-Driven Development is a structured process that emphasizes:

- **Intent-driven development** where specifications define the "*what*" before the "*how*"
- **Rich specification creation** using guardrails and organizational principles
- **Multi-step refinement** rather than one-shot code generation from prompts
- **Heavy reliance** on advanced AI model capabilities for specification interpretation

## Development Phases

| Phase | Focus | Key Activities |
|-------|-------|----------------|
| **0-to-1 Development** ("Greenfield") | Generate from scratch | <ul><li>Start with high-level requirements</li><li>Generate specifications</li><li>Plan implementation steps</li><li>Build production-ready applications</li></ul> |
| **Creative Exploration** | Parallel implementations | <ul><li>Explore diverse solutions</li><li>Support multiple technology stacks & architectures</li><li>Experiment with UX patterns</li></ul> |
| **Iterative Enhancement** ("Brownfield") | Brownfield modernization | <ul><li>Add features iteratively</li><li>Modernize legacy systems</li><li>Adapt processes</li></ul> |

## Experimental Goals

Our research and experimentation focus on:

### Technology Independence

- Create applications using diverse technology stacks
- Validate the hypothesis that Spec-Driven Development is a process not tied to specific technologies, programming languages, or frameworks

### Enterprise Constraints

- Demonstrate mission-critical application development
- Incorporate organizational constraints (cloud providers, tech stacks, engineering practices)
- Support enterprise design systems and compliance requirements

### User-Centric Development

- Build applications for different user cohorts and preferences
- Support various development approaches (from vibe-coding to AI-native development)

### Creative & Iterative Processes

- Validate the concept of parallel implementation exploration
- Provide robust iterative feature development workflows
- Extend processes to handle upgrades and modernization tasks

## Contributing

Please see our [Contributing Guide](https://github.com/github/spec-kit/blob/main/CONTRIBUTING.md) for information on how to contribute to this project.

## Support

For support, please check our [Support Guide](https://github.com/github/spec-kit/blob/main/SUPPORT.md) or open an issue on GitHub.



---

# FILE: docs/installation.md

# Installation Guide

## Prerequisites

- **Linux/macOS** (or Windows; PowerShell scripts now supported without WSL)
- AI coding agent: [Claude Code](https://www.anthropic.com/claude-code), [GitHub Copilot](https://code.visualstudio.com/), [Codebuddy CLI](https://www.codebuddy.ai/cli), [Gemini CLI](https://github.com/google-gemini/gemini-cli), or [Pi Coding Agent](https://pi.dev)
- [uv](https://docs.astral.sh/uv/) for package management
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## Installation

### Initialize a New Project

The easiest way to get started is to initialize a new project. Pin a specific release tag for stability (check [Releases](https://github.com/github/spec-kit/releases) for the latest):

```bash
# Install from a specific stable release (recommended — replace vX.Y.Z with the latest tag)
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <PROJECT_NAME>

# Or install latest from main (may include unreleased changes)
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>
```

Or initialize in the current directory:

```bash
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init .
# or use the --here flag
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init --here
```

### Specify AI Agent

You can proactively specify your AI agent during initialization:

```bash
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <project_name> --ai claude
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <project_name> --ai gemini
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <project_name> --ai copilot
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <project_name> --ai codebuddy
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <project_name> --ai pi
```

### Specify Script Type (Shell vs PowerShell)

All automation scripts now have both Bash (`.sh`) and PowerShell (`.ps1`) variants.

Auto behavior:

- Windows default: `ps`
- Other OS default: `sh`
- Interactive mode: you'll be prompted unless you pass `--script`

Force a specific script type:

```bash
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <project_name> --script sh
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <project_name> --script ps
```

### Ignore Agent Tools Check

If you prefer to get the templates without checking for the right tools:

```bash
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <project_name> --ai claude --ignore-agent-tools
```

## Verification

After initialization, you should see the following commands available in your AI agent:

- `/speckit.specify` - Create specifications
- `/speckit.plan` - Generate implementation plans  
- `/speckit.tasks` - Break down into actionable tasks

The `.specify/scripts` directory will contain both `.sh` and `.ps1` scripts.

## Troubleshooting

### Enterprise / Air-Gapped Installation

If your environment blocks access to PyPI (you see 403 errors when running `uv tool install` or `pip install`), you can create a portable wheel bundle on a connected machine and transfer it to the air-gapped target.

**Step 1: Build the wheel on a connected machine (same OS and Python version as the target)**

```bash
# Clone the repository
git clone https://github.com/github/spec-kit.git
cd spec-kit

# Build the wheel
pip install build
python -m build --wheel --outdir dist/

# Download the wheel and all its runtime dependencies
pip download -d dist/ dist/specify_cli-*.whl
```

> **Important:** `pip download` resolves platform-specific wheels (e.g., PyYAML includes native extensions). You must run this step on a machine with the **same OS and Python version** as the air-gapped target. If you need to support multiple platforms, repeat this step on each target OS (Linux, macOS, Windows) and Python version.

**Step 2: Transfer the `dist/` directory to the air-gapped machine**

Copy the entire `dist/` directory (which contains the `specify-cli` wheel and all dependency wheels) to the target machine via USB, network share, or other approved transfer method.

**Step 3: Install on the air-gapped machine**

```bash
pip install --no-index --find-links=./dist specify-cli
```

**Step 4: Initialize a project (no network required)**

```bash
# Initialize a project — no GitHub access needed
specify init my-project --ai claude --offline
```

The `--offline` flag tells the CLI to use the templates, commands, and scripts bundled inside the wheel instead of downloading from GitHub.

> **Deprecation notice:** Starting with v0.6.0, `specify init` will use bundled assets by default and the `--offline` flag will be removed. The GitHub download path will be retired because bundled assets eliminate the need for network access, avoid proxy/firewall issues, and guarantee that templates always match the installed CLI version. No action will be needed — `specify init` will simply work without network access out of the box.

> **Note:** Python 3.11+ is required.

> **Windows note:** Offline scaffolding requires PowerShell 7+ (`pwsh`), not Windows PowerShell 5.x (`powershell.exe`). Install from https://aka.ms/powershell.

### Git Credential Manager on Linux

If you're having issues with Git authentication on Linux, you can install Git Credential Manager:

```bash
#!/usr/bin/env bash
set -e
echo "Downloading Git Credential Manager v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "Installing Git Credential Manager..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "Configuring Git to use GCM..."
git config --global credential.helper manager
echo "Cleaning up..."
rm gcm-linux_amd64.2.6.1.deb
```



---

# FILE: docs/local-development.md

# Local Development Guide

This guide shows how to iterate on the `specify` CLI locally without publishing a release or committing to `main` first.

> Scripts now have both Bash (`.sh`) and PowerShell (`.ps1`) variants. The CLI auto-selects based on OS unless you pass `--script sh|ps`.

## 1. Clone and Switch Branches

```bash
git clone https://github.com/github/spec-kit.git
cd spec-kit
# Work on a feature branch
git checkout -b your-feature-branch
```

## 2. Run the CLI Directly (Fastest Feedback)

You can execute the CLI via the module entrypoint without installing anything:

```bash
# From repo root
python -m src.specify_cli --help
python -m src.specify_cli init demo-project --ai claude --ignore-agent-tools --script sh
```

If you prefer invoking the script file style (uses shebang):

```bash
python src/specify_cli/__init__.py init demo-project --script ps
```

## 3. Use Editable Install (Isolated Environment)

Create an isolated environment using `uv` so dependencies resolve exactly like end users get them:

```bash
# Create & activate virtual env (uv auto-manages .venv)
uv venv
source .venv/bin/activate  # or on Windows PowerShell: .venv\Scripts\Activate.ps1

# Install project in editable mode
uv pip install -e .

# Now 'specify' entrypoint is available
specify --help
```

Re-running after code edits requires no reinstall because of editable mode.

## 4. Invoke with uvx Directly From Git (Current Branch)

`uvx` can run from a local path (or a Git ref) to simulate user flows:

```bash
uvx --from . specify init demo-uvx --ai copilot --ignore-agent-tools --script sh
```

You can also point uvx at a specific branch without merging:

```bash
# Push your working branch first
git push origin your-feature-branch
uvx --from git+https://github.com/github/spec-kit.git@your-feature-branch specify init demo-branch-test --script ps
```

### 4a. Absolute Path uvx (Run From Anywhere)

If you're in another directory, use an absolute path instead of `.`:

```bash
uvx --from /mnt/c/GitHub/spec-kit specify --help
uvx --from /mnt/c/GitHub/spec-kit specify init demo-anywhere --ai copilot --ignore-agent-tools --script sh
```

Set an environment variable for convenience:

```bash
export SPEC_KIT_SRC=/mnt/c/GitHub/spec-kit
uvx --from "$SPEC_KIT_SRC" specify init demo-env --ai copilot --ignore-agent-tools --script ps
```

(Optional) Define a shell function:

```bash
specify-dev() { uvx --from /mnt/c/GitHub/spec-kit specify "$@"; }
# Then
specify-dev --help
```

## 5. Testing Script Permission Logic

After running an `init`, check that shell scripts are executable on POSIX systems:

```bash
ls -l scripts | grep .sh
# Expect owner execute bit (e.g. -rwxr-xr-x)
```

On Windows you will instead use the `.ps1` scripts (no chmod needed).

## 6. Run Lint / Basic Checks (Add Your Own)

Currently no enforced lint config is bundled, but you can quickly sanity check importability:

```bash
python -c "import specify_cli; print('Import OK')"
```

## 7. Build a Wheel Locally (Optional)

Validate packaging before publishing:

```bash
uv build
ls dist/
```

Install the built artifact into a fresh throwaway environment if needed.

## 8. Using a Temporary Workspace

When testing `init --here` in a dirty directory, create a temp workspace:

```bash
mkdir /tmp/spec-test && cd /tmp/spec-test
python -m src.specify_cli init --here --ai claude --ignore-agent-tools --script sh  # if repo copied here
```

Or copy only the modified CLI portion if you want a lighter sandbox.

## 9. Debug Network / TLS Skips

If you need to bypass TLS validation while experimenting:

```bash
specify check --skip-tls
specify init demo --skip-tls --ai gemini --ignore-agent-tools --script ps
```

(Use only for local experimentation.)

## 10. Rapid Edit Loop Summary

| Action | Command |
|--------|---------|
| Run CLI directly | `python -m src.specify_cli --help` |
| Editable install | `uv pip install -e .` then `specify ...` |
| Local uvx run (repo root) | `uvx --from . specify ...` |
| Local uvx run (abs path) | `uvx --from /mnt/c/GitHub/spec-kit specify ...` |
| Git branch uvx | `uvx --from git+URL@branch specify ...` |
| Build wheel | `uv build` |

## 11. Cleaning Up

Remove build artifacts / virtual env quickly:

```bash
rm -rf .venv dist build *.egg-info
```

## 12. Common Issues

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: typer` | Run `uv pip install -e .` |
| Scripts not executable (Linux) | Re-run init or `chmod +x scripts/*.sh` |
| Git step skipped | You passed `--no-git` or Git not installed |
| Wrong script type downloaded | Pass `--script sh` or `--script ps` explicitly |
| TLS errors on corporate network | Try `--skip-tls` (not for production) |

## 13. Next Steps

- Update docs and run through Quick Start using your modified CLI
- Open a PR when satisfied
- (Optional) Tag a release once changes land in `main`



---

# FILE: docs/quickstart.md

# Quick Start Guide

This guide will help you get started with Spec-Driven Development using Spec Kit.

> [!NOTE]
> All automation scripts now provide both Bash (`.sh`) and PowerShell (`.ps1`) variants. The `specify` CLI auto-selects based on OS unless you pass `--script sh|ps`.

## The 6-Step Process

> [!TIP]
> **Context Awareness**: Spec Kit commands automatically detect the active feature based on your current Git branch (e.g., `001-feature-name`). To switch between different specifications, simply switch Git branches.

### Step 1: Install Specify

**In your terminal**, run the `specify` CLI command to initialize your project:

```bash
# Create a new project directory
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>

# OR initialize in the current directory
uvx --from git+https://github.com/github/spec-kit.git specify init .
```

Pick script type explicitly (optional):

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME> --script ps  # Force PowerShell
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME> --script sh  # Force POSIX shell
```

### Step 2: Define Your Constitution

**In your AI Agent's chat interface**, use the `/speckit.constitution` slash command to establish the core rules and principles for your project. You should provide your project's specific principles as arguments.

```markdown
/speckit.constitution This project follows a "Library-First" approach. All features must be implemented as standalone libraries first. We use TDD strictly. We prefer functional programming patterns.
```

### Step 3: Create the Spec

**In the chat**, use the `/speckit.specify` slash command to describe what you want to build. Focus on the **what** and **why**, not the tech stack.

```markdown
/speckit.specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page. Albums are never in other nested albums. Within each album, photos are previewed in a tile-like interface.
```

### Step 4: Refine the Spec

**In the chat**, use the `/speckit.clarify` slash command to identify and resolve ambiguities in your specification. You can provide specific focus areas as arguments.

```bash
/speckit.clarify Focus on security and performance requirements.
```

### Step 5: Create a Technical Implementation Plan

**In the chat**, use the `/speckit.plan` slash command to provide your tech stack and architecture choices.

```markdown
/speckit.plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are not uploaded anywhere and metadata is stored in a local SQLite database.
```

### Step 6: Break Down and Implement

**In the chat**, use the `/speckit.tasks` slash command to create an actionable task list.

```markdown
/speckit.tasks
```

Optionally, validate the plan with `/speckit.analyze`:

```markdown
/speckit.analyze
```

Then, use the `/speckit.implement` slash command to execute the plan.

```markdown
/speckit.implement
```

> [!TIP]
> **Phased Implementation**: For complex projects, implement in phases to avoid overwhelming the agent's context. Start with core functionality, validate it works, then add features incrementally.

## Detailed Example: Building Taskify

Here's a complete example of building a team productivity platform:

### Step 1: Define Constitution

Initialize the project's constitution to set ground rules:

```markdown
/speckit.constitution Taskify is a "Security-First" application. All user inputs must be validated. We use a microservices architecture. Code must be fully documented.
```

### Step 2: Define Requirements with `/speckit.specify`

```text
Develop Taskify, a team productivity platform. It should allow users to create projects, add team members,
assign tasks, comment and move tasks between boards in Kanban style. In this initial phase for this feature,
let's call it "Create Taskify," let's have multiple users but the users will be declared ahead of time, predefined.
I want five users in two different categories, one product manager and four engineers. Let's create three
different sample projects. Let's have the standard Kanban columns for the status of each task, such as "To Do,"
"In Progress," "In Review," and "Done." There will be no login for this application as this is just the very
first testing thing to ensure that our basic features are set up.
```

### Step 3: Refine the Specification

Use the `/speckit.clarify` command to interactively resolve any ambiguities in your specification. You can also provide specific details you want to ensure are included.

```bash
/speckit.clarify I want to clarify the task card details. For each task in the UI for a task card, you should be able to change the current status of the task between the different columns in the Kanban work board. You should be able to leave an unlimited number of comments for a particular card. You should be able to, from that task card, assign one of the valid users.
```

You can continue to refine the spec with more details using `/speckit.clarify`:

```bash
/speckit.clarify When you first launch Taskify, it's going to give you a list of the five users to pick from. There will be no password required. When you click on a user, you go into the main view, which displays the list of projects. When you click on a project, you open the Kanban board for that project. You're going to see the columns. You'll be able to drag and drop cards back and forth between different columns. You will see any cards that are assigned to you, the currently logged in user, in a different color from all the other ones, so you can quickly see yours. You can edit any comments that you make, but you can't edit comments that other people made. You can delete any comments that you made, but you can't delete comments anybody else made.
```

### Step 4: Validate the Spec

Validate the specification checklist using the `/speckit.checklist` command:

```bash
/speckit.checklist
```

### Step 5: Generate Technical Plan with `/speckit.plan`

Be specific about your tech stack and technical requirements:

```bash
/speckit.plan We are going to generate this using .NET Aspire, using Postgres as the database. The frontend should use Blazor server with drag-and-drop task boards, real-time updates. There should be a REST API created with a projects API, tasks API, and a notifications API.
```

### Step 6: Define Tasks

Generate an actionable task list using the `/speckit.tasks` command:

```bash
/speckit.tasks
```

### Step 7: Validate and Implement

Have your AI agent audit the implementation plan using `/speckit.analyze`:

```bash
/speckit.analyze
```

Finally, implement the solution:

```bash
/speckit.implement
```

> [!TIP]
> **Phased Implementation**: For large projects like Taskify, consider implementing in phases (e.g., Phase 1: Basic project/task structure, Phase 2: Kanban functionality, Phase 3: Comments and assignments). This prevents context saturation and allows for validation at each stage.

## Key Principles

- **Be explicit** about what you're building and why
- **Don't focus on tech stack** during specification phase
- **Iterate and refine** your specifications before implementation
- **Validate** the plan before coding begins
- **Let the AI agent handle** the implementation details

## Next Steps

- Read the [complete methodology](https://github.com/github/spec-kit/blob/main/spec-driven.md) for in-depth guidance
- Check out [more examples](https://github.com/github/spec-kit/tree/main/templates) in the repository
- Explore the [source code on GitHub](https://github.com/github/spec-kit)



---

# FILE: docs/toc.yml

# Home page
- name: Home
  href: index.md

# Getting started section
- name: Getting Started
  items:
    - name: Installation
      href: installation.md
    - name: Quick Start
      href: quickstart.md
    - name: Upgrade
      href: upgrade.md

# Development workflows
- name: Development
  items:
    - name: Local Development
      href: local-development.md



---

# FILE: docs/upgrade.md

# Upgrade Guide

> You have Spec Kit installed and want to upgrade to the latest version to get new features, bug fixes, or updated slash commands. This guide covers both upgrading the CLI tool and updating your project files.

---

## Quick Reference

| What to Upgrade | Command | When to Use |
|----------------|---------|-------------|
| **CLI Tool Only** | `uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git@vX.Y.Z` | Get latest CLI features without touching project files |
| **Project Files** | `specify init --here --force --ai <your-agent>` | Update slash commands, templates, and scripts in your project |
| **Both** | Run CLI upgrade, then project update | Recommended for major version updates |

---

## Part 1: Upgrade the CLI Tool

The CLI tool (`specify`) is separate from your project files. Upgrade it to get the latest features and bug fixes.

### If you installed with `uv tool install`

Upgrade to a specific release (check [Releases](https://github.com/github/spec-kit/releases) for the latest tag):

```bash
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

### If you use one-shot `uvx` commands

Specify the desired release tag:

```bash
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init --here --ai copilot
```

### Verify the upgrade

```bash
specify check
```

This shows installed tools and confirms the CLI is working.

---

## Part 2: Updating Project Files

When Spec Kit releases new features (like new slash commands or updated templates), you need to refresh your project's Spec Kit files.

### What gets updated?

Running `specify init --here --force` will update:

- ✅ **Slash command files** (`.claude/commands/`, `.github/prompts/`, etc.)
- ✅ **Script files** (`.specify/scripts/`)
- ✅ **Template files** (`.specify/templates/`)
- ✅ **Shared memory files** (`.specify/memory/`) - **⚠️ See warnings below**

### What stays safe?

These files are **never touched** by the upgrade—the template packages don't even contain them:

- ✅ **Your specifications** (`specs/001-my-feature/spec.md`, etc.) - **CONFIRMED SAFE**
- ✅ **Your implementation plans** (`specs/001-my-feature/plan.md`, `tasks.md`, etc.) - **CONFIRMED SAFE**
- ✅ **Your source code** - **CONFIRMED SAFE**
- ✅ **Your git history** - **CONFIRMED SAFE**

The `specs/` directory is completely excluded from template packages and will never be modified during upgrades.

### Update command

Run this inside your project directory:

```bash
specify init --here --force --ai <your-agent>
```

Replace `<your-agent>` with your AI assistant. Refer to this list of [Supported AI Agents](../README.md#-supported-ai-agents)

**Example:**

```bash
specify init --here --force --ai copilot
```

### Understanding the `--force` flag

Without `--force`, the CLI warns you and asks for confirmation:

```text
Warning: Current directory is not empty (25 items)
Template files will be merged with existing content and may overwrite existing files
Proceed? [y/N]
```

With `--force`, it skips the confirmation and proceeds immediately.

**Important: Your `specs/` directory is always safe.** The `--force` flag only affects template files (commands, scripts, templates, memory). Your feature specifications, plans, and tasks in `specs/` are never included in upgrade packages and cannot be overwritten.

---

## ⚠️ Important Warnings

### 1. Constitution file will be overwritten

**Known issue:** `specify init --here --force` currently overwrites `.specify/memory/constitution.md` with the default template, erasing any customizations you made.

**Workaround:**

```bash
# 1. Back up your constitution before upgrading
cp .specify/memory/constitution.md .specify/memory/constitution-backup.md

# 2. Run the upgrade
specify init --here --force --ai copilot

# 3. Restore your customized constitution
mv .specify/memory/constitution-backup.md .specify/memory/constitution.md
```

Or use git to restore it:

```bash
# After upgrade, restore from git history
git restore .specify/memory/constitution.md
```

### 2. Custom template modifications

If you customized any templates in `.specify/templates/`, the upgrade will overwrite them. Back them up first:

```bash
# Back up custom templates
cp -r .specify/templates .specify/templates-backup

# After upgrade, merge your changes back manually
```

### 3. Duplicate slash commands (IDE-based agents)

Some IDE-based agents (like Kilo Code, Windsurf) may show **duplicate slash commands** after upgrading—both old and new versions appear.

**Solution:** Manually delete the old command files from your agent's folder.

**Example for Kilo Code:**

```bash
# Navigate to the agent's commands folder
cd .kilocode/rules/

# List files and identify duplicates
ls -la

# Delete old versions (example filenames - yours may differ)
rm speckit.specify-old.md
rm speckit.plan-v1.md
```

Restart your IDE to refresh the command list.

---

## Common Scenarios

### Scenario 1: "I just want new slash commands"

```bash
# Upgrade CLI (if using persistent install)
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git

# Update project files to get new commands
specify init --here --force --ai copilot

# Restore your constitution if customized
git restore .specify/memory/constitution.md
```

### Scenario 2: "I customized templates and constitution"

```bash
# 1. Back up customizations
cp .specify/memory/constitution.md /tmp/constitution-backup.md
cp -r .specify/templates /tmp/templates-backup

# 2. Upgrade CLI
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git

# 3. Update project
specify init --here --force --ai copilot

# 4. Restore customizations
mv /tmp/constitution-backup.md .specify/memory/constitution.md
# Manually merge template changes if needed
```

### Scenario 3: "I see duplicate slash commands in my IDE"

This happens with IDE-based agents (Kilo Code, Windsurf, Roo Code, etc.).

```bash
# Find the agent folder (example: .kilocode/rules/)
cd .kilocode/rules/

# List all files
ls -la

# Delete old command files
rm speckit.old-command-name.md

# Restart your IDE
```

### Scenario 4: "I'm working on a project without Git"

If you initialized your project with `--no-git`, you can still upgrade:

```bash
# Manually back up files you customized
cp .specify/memory/constitution.md /tmp/constitution-backup.md

# Run upgrade
specify init --here --force --ai copilot --no-git

# Restore customizations
mv /tmp/constitution-backup.md .specify/memory/constitution.md
```

The `--no-git` flag skips git initialization but doesn't affect file updates.

---

## Using `--no-git` Flag

The `--no-git` flag tells Spec Kit to **skip git repository initialization**. This is useful when:

- You manage version control differently (Mercurial, SVN, etc.)
- Your project is part of a larger monorepo with existing git setup
- You're experimenting and don't want version control yet

**During initial setup:**

```bash
specify init my-project --ai copilot --no-git
```

**During upgrade:**

```bash
specify init --here --force --ai copilot --no-git
```

### What `--no-git` does NOT do

❌ Does NOT prevent file updates
❌ Does NOT skip slash command installation
❌ Does NOT affect template merging

It **only** skips running `git init` and creating the initial commit.

### Working without Git

If you use `--no-git`, you'll need to manage feature directories manually:

**Set the `SPECIFY_FEATURE` environment variable** before using planning commands:

```bash
# Bash/Zsh
export SPECIFY_FEATURE="001-my-feature"

# PowerShell
$env:SPECIFY_FEATURE = "001-my-feature"
```

This tells Spec Kit which feature directory to use when creating specs, plans, and tasks.

**Why this matters:** Without git, Spec Kit can't detect your current branch name to determine the active feature. The environment variable provides that context manually.

---

## Troubleshooting

### "Slash commands not showing up after upgrade"

**Cause:** Agent didn't reload the command files.

**Fix:**

1. **Restart your IDE/editor** completely (not just reload window)
2. **For CLI-based agents**, verify files exist:

   ```bash
   ls -la .claude/commands/      # Claude Code
   ls -la .gemini/commands/      # Gemini
   ls -la .cursor/skills/      # Cursor
   ls -la .pi/prompts/           # Pi Coding Agent
   ```

3. **Check agent-specific setup:**
   - Codex requires `CODEX_HOME` environment variable
   - Some agents need workspace restart or cache clearing

### "I lost my constitution customizations"

**Fix:** Restore from git or backup:

```bash
# If you committed before upgrading
git restore .specify/memory/constitution.md

# If you backed up manually
cp /tmp/constitution-backup.md .specify/memory/constitution.md
```

**Prevention:** Always commit or back up `constitution.md` before upgrading.

### "Warning: Current directory is not empty"

**Full warning message:**

```text
Warning: Current directory is not empty (25 items)
Template files will be merged with existing content and may overwrite existing files
Do you want to continue? [y/N]
```

**What this means:**

This warning appears when you run `specify init --here` (or `specify init .`) in a directory that already has files. It's telling you:

1. **The directory has existing content** - In the example, 25 files/folders
2. **Files will be merged** - New template files will be added alongside your existing files
3. **Some files may be overwritten** - If you already have Spec Kit files (`.claude/`, `.specify/`, etc.), they'll be replaced with the new versions

**What gets overwritten:**

Only Spec Kit infrastructure files:

- Agent command files (`.claude/commands/`, `.github/prompts/`, etc.)
- Scripts in `.specify/scripts/`
- Templates in `.specify/templates/`
- Memory files in `.specify/memory/` (including constitution)

**What stays untouched:**

- Your `specs/` directory (specifications, plans, tasks)
- Your source code files
- Your `.git/` directory and git history
- Any other files not part of Spec Kit templates

**How to respond:**

- **Type `y` and press Enter** - Proceed with the merge (recommended if upgrading)
- **Type `n` and press Enter** - Cancel the operation
- **Use `--force` flag** - Skip this confirmation entirely:

  ```bash
  specify init --here --force --ai copilot
  ```

**When you see this warning:**

- ✅ **Expected** when upgrading an existing Spec Kit project
- ✅ **Expected** when adding Spec Kit to an existing codebase
- ⚠️ **Unexpected** if you thought you were creating a new project in an empty directory

**Prevention tip:** Before upgrading, commit or back up your `.specify/memory/constitution.md` if you customized it.

### "CLI upgrade doesn't seem to work"

Verify the installation:

```bash
# Check installed tools
uv tool list

# Should show specify-cli

# Verify path
which specify

# Should point to the uv tool installation directory
```

If not found, reinstall:

```bash
uv tool uninstall specify-cli
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

### "Do I need to run specify every time I open my project?"

**Short answer:** No, you only run `specify init` once per project (or when upgrading).

**Explanation:**

The `specify` CLI tool is used for:

- **Initial setup:** `specify init` to bootstrap Spec Kit in your project
- **Upgrades:** `specify init --here --force` to update templates and commands
- **Diagnostics:** `specify check` to verify tool installation

Once you've run `specify init`, the slash commands (like `/speckit.specify`, `/speckit.plan`, etc.) are **permanently installed** in your project's agent folder (`.claude/`, `.github/prompts/`, `.pi/prompts/`, etc.). Your AI assistant reads these command files directly—no need to run `specify` again.

**If your agent isn't recognizing slash commands:**

1. **Verify command files exist:**

   ```bash
   # For GitHub Copilot
   ls -la .github/prompts/

   # For Claude
   ls -la .claude/commands/

   # For Pi
   ls -la .pi/prompts/
   ```

2. **Restart your IDE/editor completely** (not just reload window)

3. **Check you're in the correct directory** where you ran `specify init`

4. **For some agents**, you may need to reload the workspace or clear cache

**Related issue:** If Copilot can't open local files or uses PowerShell commands unexpectedly, this is typically an IDE context issue, not related to `specify`. Try:

- Restarting VS Code
- Checking file permissions
- Ensuring the workspace folder is properly opened

---

## Version Compatibility

Spec Kit follows semantic versioning for major releases. The CLI and project files are designed to be compatible within the same major version.

**Best practice:** Keep both CLI and project files in sync by upgrading both together during major version changes.

---

## Next Steps

After upgrading:

- **Test new slash commands:** Run `/speckit.constitution` or another command to verify everything works
- **Review release notes:** Check [GitHub Releases](https://github.com/github/spec-kit/releases) for new features and breaking changes
- **Update workflows:** If new commands were added, update your team's development workflows
- **Check documentation:** Visit [github.io/spec-kit](https://github.github.io/spec-kit/) for updated guides



---

# FILE: presets/scaffold/templates/myext-template.md

# MyExt Report

> This template overrides the one provided by the "myext" extension.
> Customize it to match your needs.

## Summary

Brief summary of the report.

## Details

- Detail 1
- Detail 2

## Actions

- [ ] Action 1
- [ ] Action 2

<!--
  CUSTOMIZE: This template takes priority over the myext extension's
  version of myext-template. The extension's original is still available
  if you remove this preset.
-->



---

# FILE: presets/scaffold/templates/spec-template.md

# Feature Specification: [FEATURE NAME]

**Created**: [DATE]
**Status**: Draft

## Overview

[Brief description of the feature]

## Requirements

- [ ] Requirement 1
- [ ] Requirement 2

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2



---

# FILE: presets/self-test/templates/agent-file-template.md

# Agent File (Self-Test Preset)

<!-- preset:self-test -->

> This template is provided by the self-test preset.

## Agent Instructions

Follow these guidelines when working on this project.



---

# FILE: presets/self-test/templates/checklist-template.md

# Checklist (Self-Test Preset)

<!-- preset:self-test -->

> This template is provided by the self-test preset.

## Pre-Implementation

- [ ] Spec reviewed
- [ ] Plan approved

## Post-Implementation

- [ ] Tests passing
- [ ] Documentation updated



---

# FILE: presets/self-test/templates/constitution-template.md

# Constitution (Self-Test Preset)

<!-- preset:self-test -->

> This template is provided by the self-test preset.

## Principles

1. Principle 1
2. Principle 2

## Guidelines

- Guideline 1
- Guideline 2



---

# FILE: presets/self-test/templates/plan-template.md

# Implementation Plan (Self-Test Preset)

<!-- preset:self-test -->

> This template is provided by the self-test preset.

## Approach

Describe the implementation approach.

## Steps

1. Step 1
2. Step 2

## Dependencies

- Dependency 1

## Risks

- Risk 1



---

# FILE: presets/self-test/templates/spec-template.md

# Feature Specification (Self-Test Preset)

<!-- preset:self-test -->

> This template is provided by the self-test preset.

## Overview

Brief description of the feature.

## Requirements

- Requirement 1
- Requirement 2

## Design

Describe the design approach.

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2



---

# FILE: presets/self-test/templates/tasks-template.md

# Tasks (Self-Test Preset)

<!-- preset:self-test -->

> This template is provided by the self-test preset.

## Task List

- [ ] Task 1
- [ ] Task 2

## Estimation

| Task | Estimate |
|------|----------|
| Task 1 | TBD |
| Task 2 | TBD |



---

# FILE: spec-driven.md

# Specification-Driven Development (SDD)

## The Power Inversion

For decades, code has been king. Specifications served code—they were the scaffolding we built and then discarded once the "real work" of coding began. We wrote PRDs to guide development, created design docs to inform implementation, drew diagrams to visualize architecture. But these were always subordinate to the code itself. Code was truth. Everything else was, at best, good intentions. Code was the source of truth, and as it moved forward, specs rarely kept pace. As the asset (code) and the implementation are one, it's not easy to have a parallel implementation without trying to build from the code.

Spec-Driven Development (SDD) inverts this power structure. Specifications don't serve code—code serves specifications. The Product Requirements Document (PRD) isn't a guide for implementation; it's the source that generates implementation. Technical plans aren't documents that inform coding; they're precise definitions that produce code. This isn't an incremental improvement to how we build software. It's a fundamental rethinking of what drives development.

The gap between specification and implementation has plagued software development since its inception. We've tried to bridge it with better documentation, more detailed requirements, stricter processes. These approaches fail because they accept the gap as inevitable. They try to narrow it but never eliminate it. SDD eliminates the gap by making specifications and their concrete implementation plans born from the specification executable. When specifications and implementation plans generate code, there is no gap—only transformation.

This transformation is now possible because AI can understand and implement complex specifications, and create detailed implementation plans. But raw AI generation without structure produces chaos. SDD provides that structure through specifications and subsequent implementation plans that are precise, complete, and unambiguous enough to generate working systems. The specification becomes the primary artifact. Code becomes its expression (as an implementation from the implementation plan) in a particular language and framework.

In this new world, maintaining software means evolving specifications. The intent of the development team is expressed in natural language ("**intent-driven development**"), design assets, core principles and other guidelines. The **lingua franca** of development moves to a higher level, and code is the last-mile approach.

Debugging means fixing specifications and their implementation plans that generate incorrect code. Refactoring means restructuring for clarity. The entire development workflow reorganizes around specifications as the central source of truth, with implementation plans and code as the continuously regenerated output. Updating apps with new features or creating a new parallel implementation because we are creative beings, means revisiting the specification and creating new implementation plans. This process is therefore a 0 -> 1, (1', ..), 2, 3, N.

The development team focuses in on their creativity, experimentation, their critical thinking.

## The SDD Workflow in Practice

The workflow begins with an idea—often vague and incomplete. Through iterative dialogue with AI, this idea becomes a comprehensive PRD. The AI asks clarifying questions, identifies edge cases, and helps define precise acceptance criteria. What might take days of meetings and documentation in traditional development happens in hours of focused specification work. This transforms the traditional SDLC—requirements and design become continuous activities rather than discrete phases. This is supportive of a **team process**, where team-reviewed specifications are expressed and versioned, created in branches, and merged.

When a product manager updates acceptance criteria, implementation plans automatically flag affected technical decisions. When an architect discovers a better pattern, the PRD updates to reflect new possibilities.

Throughout this specification process, research agents gather critical context. They investigate library compatibility, performance benchmarks, and security implications. Organizational constraints are discovered and applied automatically—your company's database standards, authentication requirements, and deployment policies seamlessly integrate into every specification.

From the PRD, AI generates implementation plans that map requirements to technical decisions. Every technology choice has documented rationale. Every architectural decision traces back to specific requirements. Throughout this process, consistency validation continuously improves quality. AI analyzes specifications for ambiguity, contradictions, and gaps—not as a one-time gate, but as an ongoing refinement.

Code generation begins as soon as specifications and their implementation plans are stable enough, but they do not have to be "complete." Early generations might be exploratory—testing whether the specification makes sense in practice. Domain concepts become data models. User stories become API endpoints. Acceptance scenarios become tests. This merges development and testing through specification—test scenarios aren't written after code, they're part of the specification that generates both implementation and tests.

The feedback loop extends beyond initial development. Production metrics and incidents don't just trigger hotfixes—they update specifications for the next regeneration. Performance bottlenecks become new non-functional requirements. Security vulnerabilities become constraints that affect all future generations. This iterative dance between specification, implementation, and operational reality is where true understanding emerges and where the traditional SDLC transforms into a continuous evolution.

## Why SDD Matters Now

Three trends make SDD not just possible but necessary:

First, AI capabilities have reached a threshold where natural language specifications can reliably generate working code. This isn't about replacing developers—it's about amplifying their effectiveness by automating the mechanical translation from specification to implementation. It can amplify exploration and creativity, support "start-over" easily, and support addition, subtraction, and critical thinking.

Second, software complexity continues to grow exponentially. Modern systems integrate dozens of services, frameworks, and dependencies. Keeping all these pieces aligned with original intent through manual processes becomes increasingly difficult. SDD provides systematic alignment through specification-driven generation. Frameworks may evolve to provide AI-first support, not human-first support, or architect around reusable components.

Third, the pace of change accelerates. Requirements change far more rapidly today than ever before. Pivoting is no longer exceptional—it's expected. Modern product development demands rapid iteration based on user feedback, market conditions, and competitive pressures. Traditional development treats these changes as disruptions. Each pivot requires manually propagating changes through documentation, design, and code. The result is either slow, careful updates that limit velocity, or fast, reckless changes that accumulate technical debt.

SDD can support what-if/simulation experiments: "If we need to re-implement or change the application to promote a business need to sell more T-shirts, how would we implement and experiment for that?"

SDD transforms requirement changes from obstacles into normal workflow. When specifications drive implementation, pivots become systematic regenerations rather than manual rewrites. Change a core requirement in the PRD, and affected implementation plans update automatically. Modify a user story, and corresponding API endpoints regenerate. This isn't just about initial development—it's about maintaining engineering velocity through inevitable changes.

## Core Principles

**Specifications as the Lingua Franca**: The specification becomes the primary artifact. Code becomes its expression in a particular language and framework. Maintaining software means evolving specifications.

**Executable Specifications**: Specifications must be precise, complete, and unambiguous enough to generate working systems. This eliminates the gap between intent and implementation.

**Continuous Refinement**: Consistency validation happens continuously, not as a one-time gate. AI analyzes specifications for ambiguity, contradictions, and gaps as an ongoing process.

**Research-Driven Context**: Research agents gather critical context throughout the specification process, investigating technical options, performance implications, and organizational constraints.

**Bidirectional Feedback**: Production reality informs specification evolution. Metrics, incidents, and operational learnings become inputs for specification refinement.

**Branching for Exploration**: Generate multiple implementation approaches from the same specification to explore different optimization targets—performance, maintainability, user experience, cost.

## Implementation Approaches

Today, practicing SDD requires assembling existing tools and maintaining discipline throughout the process. The methodology can be practiced with:

- AI assistants for iterative specification development
- Research agents for gathering technical context
- Code generation tools for translating specifications to implementation
- Version control systems adapted for specification-first workflows
- Consistency checking through AI analysis of specification documents

The key is treating specifications as the source of truth, with code as the generated output that serves the specification rather than the other way around.

## Streamlining SDD with Commands

The SDD methodology is significantly enhanced through three powerful commands that automate the specification → planning → tasking workflow:

### The `/speckit.specify` Command

This command transforms a simple feature description (the user-prompt) into a complete, structured specification with automatic repository management:

1. **Automatic Feature Numbering**: Scans existing specs to determine the next feature number (e.g., 001, 002, 003, …, 1000 — expands beyond 3 digits automatically)
2. **Branch Creation**: Generates a semantic branch name from your description and creates it automatically
3. **Template-Based Generation**: Copies and customizes the feature specification template with your requirements
4. **Directory Structure**: Creates the proper `specs/[branch-name]/` structure for all related documents

### The `/speckit.plan` Command

Once a feature specification exists, this command creates a comprehensive implementation plan:

1. **Specification Analysis**: Reads and understands the feature requirements, user stories, and acceptance criteria
2. **Constitutional Compliance**: Ensures alignment with project constitution and architectural principles
3. **Technical Translation**: Converts business requirements into technical architecture and implementation details
4. **Detailed Documentation**: Generates supporting documents for data models, API contracts, and test scenarios
5. **Quickstart Validation**: Produces a quickstart guide capturing key validation scenarios

### The `/speckit.tasks` Command

After a plan is created, this command analyzes the plan and related design documents to generate an executable task list:

1. **Inputs**: Reads `plan.md` (required) and, if present, `data-model.md`, `contracts/`, and `research.md`
2. **Task Derivation**: Converts contracts, entities, and scenarios into specific tasks
3. **Parallelization**: Marks independent tasks `[P]` and outlines safe parallel groups
4. **Output**: Writes `tasks.md` in the feature directory, ready for execution by a Task agent

### Example: Building a Chat Feature

Here's how these commands transform the traditional development workflow:

**Traditional Approach:**

```text
1. Write a PRD in a document (2-3 hours)
2. Create design documents (2-3 hours)
3. Set up project structure manually (30 minutes)
4. Write technical specifications (3-4 hours)
5. Create test plans (2 hours)
Total: ~12 hours of documentation work
```

**SDD with Commands Approach:**

```bash
# Step 1: Create the feature specification (5 minutes)
/speckit.specify Real-time chat system with message history and user presence

# This automatically:
# - Creates branch "003-chat-system"
# - Generates specs/003-chat-system/spec.md
# - Populates it with structured requirements

# Step 2: Generate implementation plan (5 minutes)
/speckit.plan WebSocket for real-time messaging, PostgreSQL for history, Redis for presence

# Step 3: Generate executable tasks (5 minutes)
/speckit.tasks

# This automatically creates:
# - specs/003-chat-system/plan.md
# - specs/003-chat-system/research.md (WebSocket library comparisons)
# - specs/003-chat-system/data-model.md (Message and User schemas)
# - specs/003-chat-system/contracts/ (WebSocket events, REST endpoints)
# - specs/003-chat-system/quickstart.md (Key validation scenarios)
# - specs/003-chat-system/tasks.md (Task list derived from the plan)
```

In 15 minutes, you have:

- A complete feature specification with user stories and acceptance criteria
- A detailed implementation plan with technology choices and rationale
- API contracts and data models ready for code generation
- Comprehensive test scenarios for both automated and manual testing
- All documents properly versioned in a feature branch

### The Power of Structured Automation

These commands don't just save time—they enforce consistency and completeness:

1. **No Forgotten Details**: Templates ensure every aspect is considered, from non-functional requirements to error handling
2. **Traceable Decisions**: Every technical choice links back to specific requirements
3. **Living Documentation**: Specifications stay in sync with code because they generate it
4. **Rapid Iteration**: Change requirements and regenerate plans in minutes, not days

The commands embody SDD principles by treating specifications as executable artifacts rather than static documents. They transform the specification process from a necessary evil into the driving force of development.

### Template-Driven Quality: How Structure Constrains LLMs for Better Outcomes

The true power of these commands lies not just in automation, but in how the templates guide LLM behavior toward higher-quality specifications. The templates act as sophisticated prompts that constrain the LLM's output in productive ways:

#### 1. **Preventing Premature Implementation Details**

The feature specification template explicitly instructs:

```text
- ✅ Focus on WHAT users need and WHY
- ❌ Avoid HOW to implement (no tech stack, APIs, code structure)
```

This constraint forces the LLM to maintain proper abstraction levels. When an LLM might naturally jump to "implement using React with Redux," the template keeps it focused on "users need real-time updates of their data." This separation ensures specifications remain stable even as implementation technologies change.

#### 2. **Forcing Explicit Uncertainty Markers**

Both templates mandate the use of `[NEEDS CLARIFICATION]` markers:

```text
When creating this spec from a user prompt:
1. **Mark all ambiguities**: Use [NEEDS CLARIFICATION: specific question]
2. **Don't guess**: If the prompt doesn't specify something, mark it
```

This prevents the common LLM behavior of making plausible but potentially incorrect assumptions. Instead of guessing that a "login system" uses email/password authentication, the LLM must mark it as `[NEEDS CLARIFICATION: auth method not specified - email/password, SSO, OAuth?]`.

#### 3. **Structured Thinking Through Checklists**

The templates include comprehensive checklists that act as "unit tests" for the specification:

```markdown
### Requirement Completeness

- [ ] No [NEEDS CLARIFICATION] markers remain
- [ ] Requirements are testable and unambiguous
- [ ] Success criteria are measurable
```

These checklists force the LLM to self-review its output systematically, catching gaps that might otherwise slip through. It's like giving the LLM a quality assurance framework.

#### 4. **Constitutional Compliance Through Gates**

The implementation plan template enforces architectural principles through phase gates:

```markdown
### Phase -1: Pre-Implementation Gates

#### Simplicity Gate (Article VII)

- [ ] Using ≤3 projects?
- [ ] No future-proofing?

#### Anti-Abstraction Gate (Article VIII)

- [ ] Using framework directly?
- [ ] Single model representation?
```

These gates prevent over-engineering by making the LLM explicitly justify any complexity. If a gate fails, the LLM must document why in the "Complexity Tracking" section, creating accountability for architectural decisions.

#### 5. **Hierarchical Detail Management**

The templates enforce proper information architecture:

```text
**IMPORTANT**: This implementation plan should remain high-level and readable.
Any code samples, detailed algorithms, or extensive technical specifications
must be placed in the appropriate `implementation-details/` file
```

This prevents the common problem of specifications becoming unreadable code dumps. The LLM learns to maintain appropriate detail levels, extracting complexity to separate files while keeping the main document navigable.

#### 6. **Test-First Thinking**

The implementation template enforces test-first development:

```text
### File Creation Order
1. Create `contracts/` with API specifications
2. Create test files in order: contract → integration → e2e → unit
3. Create source files to make tests pass
```

This ordering constraint ensures the LLM thinks about testability and contracts before implementation, leading to more robust and verifiable specifications.

#### 7. **Preventing Speculative Features**

Templates explicitly discourage speculation:

```text
- [ ] No speculative or "might need" features
- [ ] All phases have clear prerequisites and deliverables
```

This stops the LLM from adding "nice to have" features that complicate implementation. Every feature must trace back to a concrete user story with clear acceptance criteria.

### The Compound Effect

These constraints work together to produce specifications that are:

- **Complete**: Checklists ensure nothing is forgotten
- **Unambiguous**: Forced clarification markers highlight uncertainties
- **Testable**: Test-first thinking baked into the process
- **Maintainable**: Proper abstraction levels and information hierarchy
- **Implementable**: Clear phases with concrete deliverables

The templates transform the LLM from a creative writer into a disciplined specification engineer, channeling its capabilities toward producing consistently high-quality, executable specifications that truly drive development.

## The Constitutional Foundation: Enforcing Architectural Discipline

At the heart of SDD lies a constitution—a set of immutable principles that govern how specifications become code. The constitution (`memory/constitution.md`) acts as the architectural DNA of the system, ensuring that every generated implementation maintains consistency, simplicity, and quality.

### The Nine Articles of Development

The constitution defines nine articles that shape every aspect of the development process:

#### Article I: Library-First Principle

Every feature must begin as a standalone library—no exceptions. This forces modular design from the start:

```text
Every feature in Specify MUST begin its existence as a standalone library.
No feature shall be implemented directly within application code without
first being abstracted into a reusable library component.
```

This principle ensures that specifications generate modular, reusable code rather than monolithic applications. When the LLM generates an implementation plan, it must structure features as libraries with clear boundaries and minimal dependencies.

#### Article II: CLI Interface Mandate

Every library must expose its functionality through a command-line interface:

```text
All CLI interfaces MUST:
- Accept text as input (via stdin, arguments, or files)
- Produce text as output (via stdout)
- Support JSON format for structured data exchange
```

This enforces observability and testability. The LLM cannot hide functionality inside opaque classes—everything must be accessible and verifiable through text-based interfaces.

#### Article III: Test-First Imperative

The most transformative article—no code before tests:

```text
This is NON-NEGOTIABLE: All implementation MUST follow strict Test-Driven Development.
No implementation code shall be written before:
1. Unit tests are written
2. Tests are validated and approved by the user
3. Tests are confirmed to FAIL (Red phase)
```

This completely inverts traditional AI code generation. Instead of generating code and hoping it works, the LLM must first generate comprehensive tests that define behavior, get them approved, and only then generate implementation.

#### Articles VII & VIII: Simplicity and Anti-Abstraction

These paired articles combat over-engineering:

```text
Section 7.3: Minimal Project Structure
- Maximum 3 projects for initial implementation
- Additional projects require documented justification

Section 8.1: Framework Trust
- Use framework features directly rather than wrapping them
```

When an LLM might naturally create elaborate abstractions, these articles force it to justify every layer of complexity. The implementation plan template's "Phase -1 Gates" directly enforce these principles.

#### Article IX: Integration-First Testing

Prioritizes real-world testing over isolated unit tests:

```text
Tests MUST use realistic environments:
- Prefer real databases over mocks
- Use actual service instances over stubs
- Contract tests mandatory before implementation
```

This ensures generated code works in practice, not just in theory.

### Constitutional Enforcement Through Templates

The implementation plan template operationalizes these articles through concrete checkpoints:

```markdown
### Phase -1: Pre-Implementation Gates

#### Simplicity Gate (Article VII)

- [ ] Using ≤3 projects?
- [ ] No future-proofing?

#### Anti-Abstraction Gate (Article VIII)

- [ ] Using framework directly?
- [ ] Single model representation?

#### Integration-First Gate (Article IX)

- [ ] Contracts defined?
- [ ] Contract tests written?
```

These gates act as compile-time checks for architectural principles. The LLM cannot proceed without either passing the gates or documenting justified exceptions in the "Complexity Tracking" section.

### The Power of Immutable Principles

The constitution's power lies in its immutability. While implementation details can evolve, the core principles remain constant. This provides:

1. **Consistency Across Time**: Code generated today follows the same principles as code generated next year
2. **Consistency Across LLMs**: Different AI models produce architecturally compatible code
3. **Architectural Integrity**: Every feature reinforces rather than undermines the system design
4. **Quality Guarantees**: Test-first, library-first, and simplicity principles ensure maintainable code

### Constitutional Evolution

While principles are immutable, their application can evolve:

```text
Section 4.2: Amendment Process
Modifications to this constitution require:
- Explicit documentation of the rationale for change
- Review and approval by project maintainers
- Backwards compatibility assessment
```

This allows the methodology to learn and improve while maintaining stability. The constitution shows its own evolution with dated amendments, demonstrating how principles can be refined based on real-world experience.

### Beyond Rules: A Development Philosophy

The constitution isn't just a rulebook—it's a philosophy that shapes how LLMs think about code generation:

- **Observability Over Opacity**: Everything must be inspectable through CLI interfaces
- **Simplicity Over Cleverness**: Start simple, add complexity only when proven necessary
- **Integration Over Isolation**: Test in real environments, not artificial ones
- **Modularity Over Monoliths**: Every feature is a library with clear boundaries

By embedding these principles into the specification and planning process, SDD ensures that generated code isn't just functional—it's maintainable, testable, and architecturally sound. The constitution transforms AI from a code generator into an architectural partner that respects and reinforces system design principles.

## The Transformation

This isn't about replacing developers or automating creativity. It's about amplifying human capability by automating mechanical translation. It's about creating a tight feedback loop where specifications, research, and code evolve together, each iteration bringing deeper understanding and better alignment between intent and implementation.

Software development needs better tools for maintaining alignment between intent and implementation. SDD provides the methodology for achieving this alignment through executable specifications that generate code rather than merely guiding it.



---

# FILE: templates/agent-file-template.md

# [PROJECT NAME] Development Guidelines

Auto-generated from all feature plans. Last updated: [DATE]

## Active Technologies

[EXTRACTED FROM ALL PLAN.MD FILES]

## Project Structure

```text
[ACTUAL STRUCTURE FROM PLANS]
```

## Commands

[ONLY COMMANDS FOR ACTIVE TECHNOLOGIES]

## Code Style

[LANGUAGE-SPECIFIC, ONLY FOR LANGUAGES IN USE]

## Recent Changes

[LAST 3 FEATURES AND WHAT THEY ADDED]

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->



---

# FILE: templates/checklist-template.md

# [CHECKLIST TYPE] Checklist: [FEATURE NAME]

**Purpose**: [Brief description of what this checklist covers]
**Created**: [DATE]
**Feature**: [Link to spec.md or relevant documentation]

**Note**: This checklist is generated by the `/speckit.checklist` command based on feature context and requirements.

<!-- 
  ============================================================================
  IMPORTANT: The checklist items below are SAMPLE ITEMS for illustration only.
  
  The /speckit.checklist command MUST replace these with actual items based on:
  - User's specific checklist request
  - Feature requirements from spec.md
  - Technical context from plan.md
  - Implementation details from tasks.md
  
  DO NOT keep these sample items in the generated checklist file.
  ============================================================================
-->

## [Category 1]

- [ ] CHK001 First checklist item with clear action
- [ ] CHK002 Second checklist item
- [ ] CHK003 Third checklist item

## [Category 2]

- [ ] CHK004 Another category item
- [ ] CHK005 Item with specific criteria
- [ ] CHK006 Final item in this category

## Notes

- Check items off as completed: `[x]`
- Add comments or findings inline
- Link to relevant resources or documentation
- Items are numbered sequentially for easy reference



---

# FILE: templates/commands/analyze.md

---
description: Perform a non-destructive cross-artifact consistency and quality analysis across spec.md, plan.md, and tasks.md after task generation.
scripts:
  sh: scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks
  ps: scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Pre-Execution Checks

**Check for extension hooks (before analysis)**:
- Check if `.specify/extensions.yml` exists in the project root.
- If it exists, read it and look for entries under the `hooks.before_analyze` key
- If the YAML cannot be parsed or is invalid, skip hook checking silently and continue normally
- Filter out hooks where `enabled` is explicitly `false`. Treat hooks without an `enabled` field as enabled by default.
- For each remaining hook, do **not** attempt to interpret or evaluate hook `condition` expressions:
  - If the hook has no `condition` field, or it is null/empty, treat the hook as executable
  - If the hook defines a non-empty `condition`, skip the hook and leave condition evaluation to the HookExecutor implementation
- For each executable hook, output the following based on its `optional` flag:
  - **Optional hook** (`optional: true`):
    ```
    ## Extension Hooks

    **Optional Pre-Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`
    ```
  - **Mandatory hook** (`optional: false`):
    ```
    ## Extension Hooks

    **Automatic Pre-Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}

    Wait for the result of the hook command before proceeding to the Goal.
    ```
- If no hooks are registered or `.specify/extensions.yml` does not exist, skip silently

## Goal

Identify inconsistencies, duplications, ambiguities, and underspecified items across the three core artifacts (`spec.md`, `plan.md`, `tasks.md`) before implementation. This command MUST run only after `/speckit.tasks` has successfully produced a complete `tasks.md`.

## Operating Constraints

**STRICTLY READ-ONLY**: Do **not** modify any files. Output a structured analysis report. Offer an optional remediation plan (user must explicitly approve before any follow-up editing commands would be invoked manually).

**Constitution Authority**: The project constitution (`/memory/constitution.md`) is **non-negotiable** within this analysis scope. Constitution conflicts are automatically CRITICAL and require adjustment of the spec, plan, or tasks—not dilution, reinterpretation, or silent ignoring of the principle. If a principle itself needs to change, that must occur in a separate, explicit constitution update outside `/speckit.analyze`.

## Execution Steps

### 1. Initialize Analysis Context

Run `{SCRIPT}` once from repo root and parse JSON for FEATURE_DIR and AVAILABLE_DOCS. Derive absolute paths:

- SPEC = FEATURE_DIR/spec.md
- PLAN = FEATURE_DIR/plan.md
- TASKS = FEATURE_DIR/tasks.md

Abort with an error message if any required file is missing (instruct the user to run missing prerequisite command).
For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

### 2. Load Artifacts (Progressive Disclosure)

Load only the minimal necessary context from each artifact:

**From spec.md:**

- Overview/Context
- Functional Requirements
- Success Criteria (measurable outcomes — e.g., performance, security, availability, user success, business impact)
- User Stories
- Edge Cases (if present)

**From plan.md:**

- Architecture/stack choices
- Data Model references
- Phases
- Technical constraints

**From tasks.md:**

- Task IDs
- Descriptions
- Phase grouping
- Parallel markers [P]
- Referenced file paths

**From constitution:**

- Load `/memory/constitution.md` for principle validation

### 3. Build Semantic Models

Create internal representations (do not include raw artifacts in output):

- **Requirements inventory**: For each Functional Requirement (FR-###) and Success Criterion (SC-###), record a stable key. Use the explicit FR-/SC- identifier as the primary key when present, and optionally also derive an imperative-phrase slug for readability (e.g., "User can upload file" → `user-can-upload-file`). Include only Success Criteria items that require buildable work (e.g., load-testing infrastructure, security audit tooling), and exclude post-launch outcome metrics and business KPIs (e.g., "Reduce support tickets by 50%").
- **User story/action inventory**: Discrete user actions with acceptance criteria
- **Task coverage mapping**: Map each task to one or more requirements or stories (inference by keyword / explicit reference patterns like IDs or key phrases)
- **Constitution rule set**: Extract principle names and MUST/SHOULD normative statements

### 4. Detection Passes (Token-Efficient Analysis)

Focus on high-signal findings. Limit to 50 findings total; aggregate remainder in overflow summary.

#### A. Duplication Detection

- Identify near-duplicate requirements
- Mark lower-quality phrasing for consolidation

#### B. Ambiguity Detection

- Flag vague adjectives (fast, scalable, secure, intuitive, robust) lacking measurable criteria
- Flag unresolved placeholders (TODO, TKTK, ???, `<placeholder>`, etc.)

#### C. Underspecification

- Requirements with verbs but missing object or measurable outcome
- User stories missing acceptance criteria alignment
- Tasks referencing files or components not defined in spec/plan

#### D. Constitution Alignment

- Any requirement or plan element conflicting with a MUST principle
- Missing mandated sections or quality gates from constitution

#### E. Coverage Gaps

- Requirements with zero associated tasks
- Tasks with no mapped requirement/story
- Success Criteria requiring buildable work (performance, security, availability) not reflected in tasks

#### F. Inconsistency

- Terminology drift (same concept named differently across files)
- Data entities referenced in plan but absent in spec (or vice versa)
- Task ordering contradictions (e.g., integration tasks before foundational setup tasks without dependency note)
- Conflicting requirements (e.g., one requires Next.js while other specifies Vue)

### 5. Severity Assignment

Use this heuristic to prioritize findings:

- **CRITICAL**: Violates constitution MUST, missing core spec artifact, or requirement with zero coverage that blocks baseline functionality
- **HIGH**: Duplicate or conflicting requirement, ambiguous security/performance attribute, untestable acceptance criterion
- **MEDIUM**: Terminology drift, missing non-functional task coverage, underspecified edge case
- **LOW**: Style/wording improvements, minor redundancy not affecting execution order

### 6. Produce Compact Analysis Report

Output a Markdown report (no file writes) with the following structure:

## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| A1 | Duplication | HIGH | spec.md:L120-134 | Two similar requirements ... | Merge phrasing; keep clearer version |

(Add one row per finding; generate stable IDs prefixed by category initial.)

**Coverage Summary Table:**

| Requirement Key | Has Task? | Task IDs | Notes |
|-----------------|-----------|----------|-------|

**Constitution Alignment Issues:** (if any)

**Unmapped Tasks:** (if any)

**Metrics:**

- Total Requirements
- Total Tasks
- Coverage % (requirements with >=1 task)
- Ambiguity Count
- Duplication Count
- Critical Issues Count

### 7. Provide Next Actions

At end of report, output a concise Next Actions block:

- If CRITICAL issues exist: Recommend resolving before `/speckit.implement`
- If only LOW/MEDIUM: User may proceed, but provide improvement suggestions
- Provide explicit command suggestions: e.g., "Run /speckit.specify with refinement", "Run /speckit.plan to adjust architecture", "Manually edit tasks.md to add coverage for 'performance-metrics'"

### 8. Offer Remediation

Ask the user: "Would you like me to suggest concrete remediation edits for the top N issues?" (Do NOT apply them automatically.)

### 9. Check for extension hooks

After reporting, check if `.specify/extensions.yml` exists in the project root.
- If it exists, read it and look for entries under the `hooks.after_analyze` key
- If the YAML cannot be parsed or is invalid, skip hook checking silently and continue normally
- Filter out hooks where `enabled` is explicitly `false`. Treat hooks without an `enabled` field as enabled by default.
- For each remaining hook, do **not** attempt to interpret or evaluate hook `condition` expressions:
  - If the hook has no `condition` field, or it is null/empty, treat the hook as executable
  - If the hook defines a non-empty `condition`, skip the hook and leave condition evaluation to the HookExecutor implementation
- For each executable hook, output the following based on its `optional` flag:
  - **Optional hook** (`optional: true`):
    ```
    ## Extension Hooks

    **Optional Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`
    ```
  - **Mandatory hook** (`optional: false`):
    ```
    ## Extension Hooks

    **Automatic Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}
    ```
- If no hooks are registered or `.specify/extensions.yml` does not exist, skip silently

## Operating Principles

### Context Efficiency

- **Minimal high-signal tokens**: Focus on actionable findings, not exhaustive documentation
- **Progressive disclosure**: Load artifacts incrementally; don't dump all content into analysis
- **Token-efficient output**: Limit findings table to 50 rows; summarize overflow
- **Deterministic results**: Rerunning without changes should produce consistent IDs and counts

### Analysis Guidelines

- **NEVER modify files** (this is read-only analysis)
- **NEVER hallucinate missing sections** (if absent, report them accurately)
- **Prioritize constitution violations** (these are always CRITICAL)
- **Use examples over exhaustive rules** (cite specific instances, not generic patterns)
- **Report zero issues gracefully** (emit success report with coverage statistics)

## Context

{ARGS}



---

# FILE: templates/commands/checklist.md

---
description: Generate a custom checklist for the current feature based on user requirements.
scripts:
  sh: scripts/bash/check-prerequisites.sh --json
  ps: scripts/powershell/check-prerequisites.ps1 -Json
---

## Checklist Purpose: "Unit Tests for English"

**CRITICAL CONCEPT**: Checklists are **UNIT TESTS FOR REQUIREMENTS WRITING** - they validate the quality, clarity, and completeness of requirements in a given domain.

**NOT for verification/testing**:

- ❌ NOT "Verify the button clicks correctly"
- ❌ NOT "Test error handling works"
- ❌ NOT "Confirm the API returns 200"
- ❌ NOT checking if code/implementation matches the spec

**FOR requirements quality validation**:

- ✅ "Are visual hierarchy requirements defined for all card types?" (completeness)
- ✅ "Is 'prominent display' quantified with specific sizing/positioning?" (clarity)
- ✅ "Are hover state requirements consistent across all interactive elements?" (consistency)
- ✅ "Are accessibility requirements defined for keyboard navigation?" (coverage)
- ✅ "Does the spec define what happens when logo image fails to load?" (edge cases)

**Metaphor**: If your spec is code written in English, the checklist is its unit test suite. You're testing whether the requirements are well-written, complete, unambiguous, and ready for implementation - NOT whether the implementation works.

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Pre-Execution Checks

**Check for extension hooks (before checklist generation)**:
- Check if `.specify/extensions.yml` exists in the project root.
- If it exists, read it and look for entries under the `hooks.before_checklist` key
- If the YAML cannot be parsed or is invalid, skip hook checking silently and continue normally
- Filter out hooks where `enabled` is explicitly `false`. Treat hooks without an `enabled` field as enabled by default.
- For each remaining hook, do **not** attempt to interpret or evaluate hook `condition` expressions:
  - If the hook has no `condition` field, or it is null/empty, treat the hook as executable
  - If the hook defines a non-empty `condition`, skip the hook and leave condition evaluation to the HookExecutor implementation
- For each executable hook, output the following based on its `optional` flag:
  - **Optional hook** (`optional: true`):
    ```
    ## Extension Hooks

    **Optional Pre-Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`
    ```
  - **Mandatory hook** (`optional: false`):
    ```
    ## Extension Hooks

    **Automatic Pre-Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}

    Wait for the result of the hook command before proceeding to the Execution Steps.
    ```
- If no hooks are registered or `.specify/extensions.yml` does not exist, skip silently

## Execution Steps

1. **Setup**: Run `{SCRIPT}` from repo root and parse JSON for FEATURE_DIR and AVAILABLE_DOCS list.
   - All file paths must be absolute.
   - For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Clarify intent (dynamic)**: Derive up to THREE initial contextual clarifying questions (no pre-baked catalog). They MUST:
   - Be generated from the user's phrasing + extracted signals from spec/plan/tasks
   - Only ask about information that materially changes checklist content
   - Be skipped individually if already unambiguous in `$ARGUMENTS`
   - Prefer precision over breadth

   Generation algorithm:
   1. Extract signals: feature domain keywords (e.g., auth, latency, UX, API), risk indicators ("critical", "must", "compliance"), stakeholder hints ("QA", "review", "security team"), and explicit deliverables ("a11y", "rollback", "contracts").
   2. Cluster signals into candidate focus areas (max 4) ranked by relevance.
   3. Identify probable audience & timing (author, reviewer, QA, release) if not explicit.
   4. Detect missing dimensions: scope breadth, depth/rigor, risk emphasis, exclusion boundaries, measurable acceptance criteria.
   5. Formulate questions chosen from these archetypes:
      - Scope refinement (e.g., "Should this include integration touchpoints with X and Y or stay limited to local module correctness?")
      - Risk prioritization (e.g., "Which of these potential risk areas should receive mandatory gating checks?")
      - Depth calibration (e.g., "Is this a lightweight pre-commit sanity list or a formal release gate?")
      - Audience framing (e.g., "Will this be used by the author only or peers during PR review?")
      - Boundary exclusion (e.g., "Should we explicitly exclude performance tuning items this round?")
      - Scenario class gap (e.g., "No recovery flows detected—are rollback / partial failure paths in scope?")

   Question formatting rules:
   - If presenting options, generate a compact table with columns: Option | Candidate | Why It Matters
   - Limit to A–E options maximum; omit table if a free-form answer is clearer
   - Never ask the user to restate what they already said
   - Avoid speculative categories (no hallucination). If uncertain, ask explicitly: "Confirm whether X belongs in scope."

   Defaults when interaction impossible:
   - Depth: Standard
   - Audience: Reviewer (PR) if code-related; Author otherwise
   - Focus: Top 2 relevance clusters

   Output the questions (label Q1/Q2/Q3). After answers: if ≥2 scenario classes (Alternate / Exception / Recovery / Non-Functional domain) remain unclear, you MAY ask up to TWO more targeted follow‑ups (Q4/Q5) with a one-line justification each (e.g., "Unresolved recovery path risk"). Do not exceed five total questions. Skip escalation if user explicitly declines more.

3. **Understand user request**: Combine `$ARGUMENTS` + clarifying answers:
   - Derive checklist theme (e.g., security, review, deploy, ux)
   - Consolidate explicit must-have items mentioned by user
   - Map focus selections to category scaffolding
   - Infer any missing context from spec/plan/tasks (do NOT hallucinate)

4. **Load feature context**: Read from FEATURE_DIR:
   - spec.md: Feature requirements and scope
   - plan.md (if exists): Technical details, dependencies
   - tasks.md (if exists): Implementation tasks

   **Context Loading Strategy**:
   - Load only necessary portions relevant to active focus areas (avoid full-file dumping)
   - Prefer summarizing long sections into concise scenario/requirement bullets
   - Use progressive disclosure: add follow-on retrieval only if gaps detected
   - If source docs are large, generate interim summary items instead of embedding raw text

5. **Generate checklist** - Create "Unit Tests for Requirements":
   - Create `FEATURE_DIR/checklists/` directory if it doesn't exist
   - Generate unique checklist filename:
     - Use short, descriptive name based on domain (e.g., `ux.md`, `api.md`, `security.md`)
     - Format: `[domain].md`
   - File handling behavior:
     - If file does NOT exist: Create new file and number items starting from CHK001
     - If file exists: Append new items to existing file, continuing from the last CHK ID (e.g., if last item is CHK015, start new items at CHK016)
   - Never delete or replace existing checklist content - always preserve and append

   **CORE PRINCIPLE - Test the Requirements, Not the Implementation**:
   Every checklist item MUST evaluate the REQUIREMENTS THEMSELVES for:
   - **Completeness**: Are all necessary requirements present?
   - **Clarity**: Are requirements unambiguous and specific?
   - **Consistency**: Do requirements align with each other?
   - **Measurability**: Can requirements be objectively verified?
   - **Coverage**: Are all scenarios/edge cases addressed?

   **Category Structure** - Group items by requirement quality dimensions:
   - **Requirement Completeness** (Are all necessary requirements documented?)
   - **Requirement Clarity** (Are requirements specific and unambiguous?)
   - **Requirement Consistency** (Do requirements align without conflicts?)
   - **Acceptance Criteria Quality** (Are success criteria measurable?)
   - **Scenario Coverage** (Are all flows/cases addressed?)
   - **Edge Case Coverage** (Are boundary conditions defined?)
   - **Non-Functional Requirements** (Performance, Security, Accessibility, etc. - are they specified?)
   - **Dependencies & Assumptions** (Are they documented and validated?)
   - **Ambiguities & Conflicts** (What needs clarification?)

   **HOW TO WRITE CHECKLIST ITEMS - "Unit Tests for English"**:

   ❌ **WRONG** (Testing implementation):
   - "Verify landing page displays 3 episode cards"
   - "Test hover states work on desktop"
   - "Confirm logo click navigates home"

   ✅ **CORRECT** (Testing requirements quality):
   - "Are the exact number and layout of featured episodes specified?" [Completeness]
   - "Is 'prominent display' quantified with specific sizing/positioning?" [Clarity]
   - "Are hover state requirements consistent across all interactive elements?" [Consistency]
   - "Are keyboard navigation requirements defined for all interactive UI?" [Coverage]
   - "Is the fallback behavior specified when logo image fails to load?" [Edge Cases]
   - "Are loading states defined for asynchronous episode data?" [Completeness]
   - "Does the spec define visual hierarchy for competing UI elements?" [Clarity]

   **ITEM STRUCTURE**:
   Each item should follow this pattern:
   - Question format asking about requirement quality
   - Focus on what's WRITTEN (or not written) in the spec/plan
   - Include quality dimension in brackets [Completeness/Clarity/Consistency/etc.]
   - Reference spec section `[Spec §X.Y]` when checking existing requirements
   - Use `[Gap]` marker when checking for missing requirements

   **EXAMPLES BY QUALITY DIMENSION**:

   Completeness:
   - "Are error handling requirements defined for all API failure modes? [Gap]"
   - "Are accessibility requirements specified for all interactive elements? [Completeness]"
   - "Are mobile breakpoint requirements defined for responsive layouts? [Gap]"

   Clarity:
   - "Is 'fast loading' quantified with specific timing thresholds? [Clarity, Spec §NFR-2]"
   - "Are 'related episodes' selection criteria explicitly defined? [Clarity, Spec §FR-5]"
   - "Is 'prominent' defined with measurable visual properties? [Ambiguity, Spec §FR-4]"

   Consistency:
   - "Do navigation requirements align across all pages? [Consistency, Spec §FR-10]"
   - "Are card component requirements consistent between landing and detail pages? [Consistency]"

   Coverage:
   - "Are requirements defined for zero-state scenarios (no episodes)? [Coverage, Edge Case]"
   - "Are concurrent user interaction scenarios addressed? [Coverage, Gap]"
   - "Are requirements specified for partial data loading failures? [Coverage, Exception Flow]"

   Measurability:
   - "Are visual hierarchy requirements measurable/testable? [Acceptance Criteria, Spec §FR-1]"
   - "Can 'balanced visual weight' be objectively verified? [Measurability, Spec §FR-2]"

   **Scenario Classification & Coverage** (Requirements Quality Focus):
   - Check if requirements exist for: Primary, Alternate, Exception/Error, Recovery, Non-Functional scenarios
   - For each scenario class, ask: "Are [scenario type] requirements complete, clear, and consistent?"
   - If scenario class missing: "Are [scenario type] requirements intentionally excluded or missing? [Gap]"
   - Include resilience/rollback when state mutation occurs: "Are rollback requirements defined for migration failures? [Gap]"

   **Traceability Requirements**:
   - MINIMUM: ≥80% of items MUST include at least one traceability reference
   - Each item should reference: spec section `[Spec §X.Y]`, or use markers: `[Gap]`, `[Ambiguity]`, `[Conflict]`, `[Assumption]`
   - If no ID system exists: "Is a requirement & acceptance criteria ID scheme established? [Traceability]"

   **Surface & Resolve Issues** (Requirements Quality Problems):
   Ask questions about the requirements themselves:
   - Ambiguities: "Is the term 'fast' quantified with specific metrics? [Ambiguity, Spec §NFR-1]"
   - Conflicts: "Do navigation requirements conflict between §FR-10 and §FR-10a? [Conflict]"
   - Assumptions: "Is the assumption of 'always available podcast API' validated? [Assumption]"
   - Dependencies: "Are external podcast API requirements documented? [Dependency, Gap]"
   - Missing definitions: "Is 'visual hierarchy' defined with measurable criteria? [Gap]"

   **Content Consolidation**:
   - Soft cap: If raw candidate items > 40, prioritize by risk/impact
   - Merge near-duplicates checking the same requirement aspect
   - If >5 low-impact edge cases, create one item: "Are edge cases X, Y, Z addressed in requirements? [Coverage]"

   **🚫 ABSOLUTELY PROHIBITED** - These make it an implementation test, not a requirements test:
   - ❌ Any item starting with "Verify", "Test", "Confirm", "Check" + implementation behavior
   - ❌ References to code execution, user actions, system behavior
   - ❌ "Displays correctly", "works properly", "functions as expected"
   - ❌ "Click", "navigate", "render", "load", "execute"
   - ❌ Test cases, test plans, QA procedures
   - ❌ Implementation details (frameworks, APIs, algorithms)

   **✅ REQUIRED PATTERNS** - These test requirements quality:
   - ✅ "Are [requirement type] defined/specified/documented for [scenario]?"
   - ✅ "Is [vague term] quantified/clarified with specific criteria?"
   - ✅ "Are requirements consistent between [section A] and [section B]?"
   - ✅ "Can [requirement] be objectively measured/verified?"
   - ✅ "Are [edge cases/scenarios] addressed in requirements?"
   - ✅ "Does the spec define [missing aspect]?"

6. **Structure Reference**: Generate the checklist following the canonical template in `templates/checklist-template.md` for title, meta section, category headings, and ID formatting. If template is unavailable, use: H1 title, purpose/created meta lines, `##` category sections containing `- [ ] CHK### <requirement item>` lines with globally incrementing IDs starting at CHK001.

7. **Report**: Output full path to checklist file, item count, and summarize whether the run created a new file or appended to an existing one. Summarize:
   - Focus areas selected
   - Depth level
   - Actor/timing
   - Any explicit user-specified must-have items incorporated

**Important**: Each `/speckit.checklist` command invocation uses a short, descriptive checklist filename and either creates a new file or appends to an existing one. This allows:

- Multiple checklists of different types (e.g., `ux.md`, `test.md`, `security.md`)
- Simple, memorable filenames that indicate checklist purpose
- Easy identification and navigation in the `checklists/` folder

To avoid clutter, use descriptive types and clean up obsolete checklists when done.

## Example Checklist Types & Sample Items

**UX Requirements Quality:** `ux.md`

Sample items (testing the requirements, NOT the implementation):

- "Are visual hierarchy requirements defined with measurable criteria? [Clarity, Spec §FR-1]"
- "Is the number and positioning of UI elements explicitly specified? [Completeness, Spec §FR-1]"
- "Are interaction state requirements (hover, focus, active) consistently defined? [Consistency]"
- "Are accessibility requirements specified for all interactive elements? [Coverage, Gap]"
- "Is fallback behavior defined when images fail to load? [Edge Case, Gap]"
- "Can 'prominent display' be objectively measured? [Measurability, Spec §FR-4]"

**API Requirements Quality:** `api.md`

Sample items:

- "Are error response formats specified for all failure scenarios? [Completeness]"
- "Are rate limiting requirements quantified with specific thresholds? [Clarity]"
- "Are authentication requirements consistent across all endpoints? [Consistency]"
- "Are retry/timeout requirements defined for external dependencies? [Coverage, Gap]"
- "Is versioning strategy documented in requirements? [Gap]"

**Performance Requirements Quality:** `performance.md`

Sample items:

- "Are performance requirements quantified with specific metrics? [Clarity]"
- "Are performance targets defined for all critical user journeys? [Coverage]"
- "Are performance requirements under different load conditions specified? [Completeness]"
- "Can performance requirements be objectively measured? [Measurability]"
- "Are degradation requirements defined for high-load scenarios? [Edge Case, Gap]"

**Security Requirements Quality:** `security.md`

Sample items:

- "Are authentication requirements specified for all protected resources? [Coverage]"
- "Are data protection requirements defined for sensitive information? [Completeness]"
- "Is the threat model documented and requirements aligned to it? [Traceability]"
- "Are security requirements consistent with compliance obligations? [Consistency]"
- "Are security failure/breach response requirements defined? [Gap, Exception Flow]"

## Anti-Examples: What NOT To Do

**❌ WRONG - These test implementation, not requirements:**

```markdown
- [ ] CHK001 - Verify landing page displays 3 episode cards [Spec §FR-001]
- [ ] CHK002 - Test hover states work correctly on desktop [Spec §FR-003]
- [ ] CHK003 - Confirm logo click navigates to home page [Spec §FR-010]
- [ ] CHK004 - Check that related episodes section shows 3-5 items [Spec §FR-005]
```

**✅ CORRECT - These test requirements quality:**

```markdown
- [ ] CHK001 - Are the number and layout of featured episodes explicitly specified? [Completeness, Spec §FR-001]
- [ ] CHK002 - Are hover state requirements consistently defined for all interactive elements? [Consistency, Spec §FR-003]
- [ ] CHK003 - Are navigation requirements clear for all clickable brand elements? [Clarity, Spec §FR-010]
- [ ] CHK004 - Is the selection criteria for related episodes documented? [Gap, Spec §FR-005]
- [ ] CHK005 - Are loading state requirements defined for asynchronous episode data? [Gap]
- [ ] CHK006 - Can "visual hierarchy" requirements be objectively measured? [Measurability, Spec §FR-001]
```

**Key Differences:**

- Wrong: Tests if the system works correctly
- Correct: Tests if the requirements are written correctly
- Wrong: Verification of behavior
- Correct: Validation of requirement quality
- Wrong: "Does it do X?"
- Correct: "Is X clearly specified?"

## Post-Execution Checks

**Check for extension hooks (after checklist generation)**:
Check if `.specify/extensions.yml` exists in the project root.
- If it exists, read it and look for entries under the `hooks.after_checklist` key
- If the YAML cannot be parsed or is invalid, skip hook checking silently and continue normally
- Filter out hooks where `enabled` is explicitly `false`. Treat hooks without an `enabled` field as enabled by default.
- For each remaining hook, do **not** attempt to interpret or evaluate hook `condition` expressions:
  - If the hook has no `condition` field, or it is null/empty, treat the hook as executable
  - If the hook defines a non-empty `condition`, skip the hook and leave condition evaluation to the HookExecutor implementation
- For each executable hook, output the following based on its `optional` flag:
  - **Optional hook** (`optional: true`):
    ```
    ## Extension Hooks

    **Optional Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`
    ```
  - **Mandatory hook** (`optional: false`):
    ```
    ## Extension Hooks

    **Automatic Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}
    ```
- If no hooks are registered or `.specify/extensions.yml` does not exist, skip silently



---

# FILE: templates/commands/clarify.md

---
description: Identify underspecified areas in the current feature spec by asking up to 5 highly targeted clarification questions and encoding answers back into the spec.
handoffs: 
  - label: Build Technical Plan
    agent: speckit.plan
    prompt: Create a plan for the spec. I am building with...
scripts:
   sh: scripts/bash/check-prerequisites.sh --json --paths-only
   ps: scripts/powershell/check-prerequisites.ps1 -Json -PathsOnly
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Pre-Execution Checks

**Check for extension hooks (before clarification)**:
- Check if `.specify/extensions.yml` exists in the project root.
- If it exists, read it and look for entries under the `hooks.before_clarify` key
- If the YAML cannot be parsed or is invalid, skip hook checking silently and continue normally
- Filter out hooks where `enabled` is explicitly `false`. Treat hooks without an `enabled` field as enabled by default.
- For each remaining hook, do **not** attempt to interpret or evaluate hook `condition` expressions:
  - If the hook has no `condition` field, or it is null/empty, treat the hook as executable
  - If the hook defines a non-empty `condition`, skip the hook and leave condition evaluation to the HookExecutor implementation
- For each executable hook, output the following based on its `optional` flag:
  - **Optional hook** (`optional: true`):
    ```
    ## Extension Hooks

    **Optional Pre-Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`
    ```
  - **Mandatory hook** (`optional: false`):
    ```
    ## Extension Hooks

    **Automatic Pre-Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}

    Wait for the result of the hook command before proceeding to the Outline.
    ```
- If no hooks are registered or `.specify/extensions.yml` does not exist, skip silently

## Outline

Goal: Detect and reduce ambiguity or missing decision points in the active feature specification and record the clarifications directly in the spec file.

Note: This clarification workflow is expected to run (and be completed) BEFORE invoking `/speckit.plan`. If the user explicitly states they are skipping clarification (e.g., exploratory spike), you may proceed, but must warn that downstream rework risk increases.

Execution steps:

1. Run `{SCRIPT}` from repo root **once** (combined `--json --paths-only` mode / `-Json -PathsOnly`). Parse minimal JSON payload fields:
   - `FEATURE_DIR`
   - `FEATURE_SPEC`
   - (Optionally capture `IMPL_PLAN`, `TASKS` for future chained flows.)
   - If JSON parsing fails, abort and instruct user to re-run `/speckit.specify` or verify feature branch environment.
   - For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. Load the current spec file. Perform a structured ambiguity & coverage scan using this taxonomy. For each category, mark status: Clear / Partial / Missing. Produce an internal coverage map used for prioritization (do not output raw map unless no questions will be asked).

   Functional Scope & Behavior:
   - Core user goals & success criteria
   - Explicit out-of-scope declarations
   - User roles / personas differentiation

   Domain & Data Model:
   - Entities, attributes, relationships
   - Identity & uniqueness rules
   - Lifecycle/state transitions
   - Data volume / scale assumptions

   Interaction & UX Flow:
   - Critical user journeys / sequences
   - Error/empty/loading states
   - Accessibility or localization notes

   Non-Functional Quality Attributes:
   - Performance (latency, throughput targets)
   - Scalability (horizontal/vertical, limits)
   - Reliability & availability (uptime, recovery expectations)
   - Observability (logging, metrics, tracing signals)
   - Security & privacy (authN/Z, data protection, threat assumptions)
   - Compliance / regulatory constraints (if any)

   Integration & External Dependencies:
   - External services/APIs and failure modes
   - Data import/export formats
   - Protocol/versioning assumptions

   Edge Cases & Failure Handling:
   - Negative scenarios
   - Rate limiting / throttling
   - Conflict resolution (e.g., concurrent edits)

   Constraints & Tradeoffs:
   - Technical constraints (language, storage, hosting)
   - Explicit tradeoffs or rejected alternatives

   Terminology & Consistency:
   - Canonical glossary terms
   - Avoided synonyms / deprecated terms

   Completion Signals:
   - Acceptance criteria testability
   - Measurable Definition of Done style indicators

   Misc / Placeholders:
   - TODO markers / unresolved decisions
   - Ambiguous adjectives ("robust", "intuitive") lacking quantification

   For each category with Partial or Missing status, add a candidate question opportunity unless:
   - Clarification would not materially change implementation or validation strategy
   - Information is better deferred to planning phase (note internally)

3. Generate (internally) a prioritized queue of candidate clarification questions (maximum 5). Do NOT output them all at once. Apply these constraints:
    - Maximum of 5 total questions across the whole session.
    - Each question must be answerable with EITHER:
       - A short multiple‑choice selection (2–5 distinct, mutually exclusive options), OR
       - A one-word / short‑phrase answer (explicitly constrain: "Answer in <=5 words").
    - Only include questions whose answers materially impact architecture, data modeling, task decomposition, test design, UX behavior, operational readiness, or compliance validation.
    - Ensure category coverage balance: attempt to cover the highest impact unresolved categories first; avoid asking two low-impact questions when a single high-impact area (e.g., security posture) is unresolved.
    - Exclude questions already answered, trivial stylistic preferences, or plan-level execution details (unless blocking correctness).
    - Favor clarifications that reduce downstream rework risk or prevent misaligned acceptance tests.
    - If more than 5 categories remain unresolved, select the top 5 by (Impact * Uncertainty) heuristic.

4. Sequential questioning loop (interactive):
    - Present EXACTLY ONE question at a time.
    - For multiple‑choice questions:
       - **Analyze all options** and determine the **most suitable option** based on:
          - Best practices for the project type
          - Common patterns in similar implementations
          - Risk reduction (security, performance, maintainability)
          - Alignment with any explicit project goals or constraints visible in the spec
       - Present your **recommended option prominently** at the top with clear reasoning (1-2 sentences explaining why this is the best choice).
       - Format as: `**Recommended:** Option [X] - <reasoning>`
       - Then render all options as a Markdown table:

       | Option | Description |
       |--------|-------------|
       | A | <Option A description> |
       | B | <Option B description> |
       | C | <Option C description> (add D/E as needed up to 5) |
       | Short | Provide a different short answer (<=5 words) (Include only if free-form alternative is appropriate) |

       - After the table, add: `You can reply with the option letter (e.g., "A"), accept the recommendation by saying "yes" or "recommended", or provide your own short answer.`
    - For short‑answer style (no meaningful discrete options):
       - Provide your **suggested answer** based on best practices and context.
       - Format as: `**Suggested:** <your proposed answer> - <brief reasoning>`
       - Then output: `Format: Short answer (<=5 words). You can accept the suggestion by saying "yes" or "suggested", or provide your own answer.`
    - After the user answers:
       - If the user replies with "yes", "recommended", or "suggested", use your previously stated recommendation/suggestion as the answer.
       - Otherwise, validate the answer maps to one option or fits the <=5 word constraint.
       - If ambiguous, ask for a quick disambiguation (count still belongs to same question; do not advance).
       - Once satisfactory, record it in working memory (do not yet write to disk) and move to the next queued question.
    - Stop asking further questions when:
       - All critical ambiguities resolved early (remaining queued items become unnecessary), OR
       - User signals completion ("done", "good", "no more"), OR
       - You reach 5 asked questions.
    - Never reveal future queued questions in advance.
    - If no valid questions exist at start, immediately report no critical ambiguities.

5. Integration after EACH accepted answer (incremental update approach):
    - Maintain in-memory representation of the spec (loaded once at start) plus the raw file contents.
    - For the first integrated answer in this session:
       - Ensure a `## Clarifications` section exists (create it just after the highest-level contextual/overview section per the spec template if missing).
       - Under it, create (if not present) a `### Session YYYY-MM-DD` subheading for today.
    - Append a bullet line immediately after acceptance: `- Q: <question> → A: <final answer>`.
    - Then immediately apply the clarification to the most appropriate section(s):
       - Functional ambiguity → Update or add a bullet in Functional Requirements.
       - User interaction / actor distinction → Update User Stories or Actors subsection (if present) with clarified role, constraint, or scenario.
       - Data shape / entities → Update Data Model (add fields, types, relationships) preserving ordering; note added constraints succinctly.
       - Non-functional constraint → Add/modify measurable criteria in Success Criteria > Measurable Outcomes (convert vague adjective to metric or explicit target).
       - Edge case / negative flow → Add a new bullet under Edge Cases / Error Handling (or create such subsection if template provides placeholder for it).
       - Terminology conflict → Normalize term across spec; retain original only if necessary by adding `(formerly referred to as "X")` once.
    - If the clarification invalidates an earlier ambiguous statement, replace that statement instead of duplicating; leave no obsolete contradictory text.
    - Save the spec file AFTER each integration to minimize risk of context loss (atomic overwrite).
    - Preserve formatting: do not reorder unrelated sections; keep heading hierarchy intact.
    - Keep each inserted clarification minimal and testable (avoid narrative drift).

6. Validation (performed after EACH write plus final pass):
   - Clarifications session contains exactly one bullet per accepted answer (no duplicates).
   - Total asked (accepted) questions ≤ 5.
   - Updated sections contain no lingering vague placeholders the new answer was meant to resolve.
   - No contradictory earlier statement remains (scan for now-invalid alternative choices removed).
   - Markdown structure valid; only allowed new headings: `## Clarifications`, `### Session YYYY-MM-DD`.
   - Terminology consistency: same canonical term used across all updated sections.

7. Write the updated spec back to `FEATURE_SPEC`.

8. Report completion (after questioning loop ends or early termination):
   - Number of questions asked & answered.
   - Path to updated spec.
   - Sections touched (list names).
   - Coverage summary table listing each taxonomy category with Status: Resolved (was Partial/Missing and addressed), Deferred (exceeds question quota or better suited for planning), Clear (already sufficient), Outstanding (still Partial/Missing but low impact).
   - If any Outstanding or Deferred remain, recommend whether to proceed to `/speckit.plan` or run `/speckit.clarify` again later post-plan.
   - Suggested next command.

Behavior rules:

- If no meaningful ambiguities found (or all potential questions would be low-impact), respond: "No critical ambiguities detected worth formal clarification." and suggest proceeding.
- If spec file missing, instruct user to run `/speckit.specify` first (do not create a new spec here).
- Never exceed 5 total asked questions (clarification retries for a single question do not count as new questions).
- Avoid speculative tech stack questions unless the absence blocks functional clarity.
- Respect user early termination signals ("stop", "done", "proceed").
- If no questions asked due to full coverage, output a compact coverage summary (all categories Clear) then suggest advancing.
- If quota reached with unresolved high-impact categories remaining, explicitly flag them under Deferred with rationale.

Context for prioritization: {ARGS}

## Post-Execution Checks

**Check for extension hooks (after clarification)**:
Check if `.specify/extensions.yml` exists in the project root.
- If it exists, read it and look for entries under the `hooks.after_clarify` key
- If the YAML cannot be parsed or is invalid, skip hook checking silently and continue normally
- Filter out hooks where `enabled` is explicitly `false`. Treat hooks without an `enabled` field as enabled by default.
- For each remaining hook, do **not** attempt to interpret or evaluate hook `condition` expressions:
  - If the hook has no `condition` field, or it is null/empty, treat the hook as executable
  - If the hook defines a non-empty `condition`, skip the hook and leave condition evaluation to the HookExecutor implementation
- For each executable hook, output the following based on its `optional` flag:
  - **Optional hook** (`optional: true`):
    ```
    ## Extension Hooks

    **Optional Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`
    ```
  - **Mandatory hook** (`optional: false`):
    ```
    ## Extension Hooks

    **Automatic Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}
    ```
- If no hooks are registered or `.specify/extensions.yml` does not exist, skip silently
