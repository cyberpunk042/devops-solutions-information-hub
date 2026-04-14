# bmad-code-org/BMAD-METHOD

Source: https://github.com/bmad-code-org/BMAD-METHOD
Ingested: 2026-04-14
Type: documentation

---

# README

![BMad Method](banner-bmad-method.png)

[![Version](https://img.shields.io/npm/v/bmad-method?color=blue&label=version)](https://www.npmjs.com/package/bmad-method)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen)](https://nodejs.org)
[![Python Version](https://img.shields.io/badge/python-%3E%3D3.10-blue?logo=python&logoColor=white)](https://www.python.org)
[![uv](https://img.shields.io/badge/uv-package%20manager-blueviolet?logo=uv)](https://docs.astral.sh/uv/)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

**Build More Architect Dreams** — An AI-driven agile development module for the BMad Method Module Ecosystem, the best and most comprehensive Agile AI Driven Development framework that has true scale-adaptive intelligence that adjusts from bug fixes to enterprise systems.

**100% free and open source.** No paywalls. No gated content. No gated Discord. We believe in empowering everyone, not just those who can pay for a gated community or courses.

## Why the BMad Method?

Traditional AI tools do the thinking for you, producing average results. BMad agents and facilitated workflows act as expert collaborators who guide you through a structured process to bring out your best thinking in partnership with the AI.

- **AI Intelligent Help** — Invoke the `bmad-help` skill anytime for guidance on what's next
- **Scale-Domain-Adaptive** — Automatically adjusts planning depth based on project complexity
- **Structured Workflows** — Grounded in agile best practices across analysis, planning, architecture, and implementation
- **Specialized Agents** — 12+ domain experts (PM, Architect, Developer, UX, and more)
- **Party Mode** — Bring multiple agent personas into one session to collaborate and discuss
- **Complete Lifecycle** — From brainstorming to deployment

[Learn more at **docs.bmad-method.org**](https://docs.bmad-method.org)

---

## 🚀 What's Next for BMad?

**V6 is here and we're just getting started!** The BMad Method is evolving rapidly with optimizations including Cross Platform Agent Team and Sub Agent inclusion, Skills Architecture, BMad Builder v1, Dev Loop Automation, and so much more in the works.

**[📍 Check out the complete Roadmap →](https://docs.bmad-method.org/roadmap/)**

---

## Quick Start

**Prerequisites**: [Node.js](https://nodejs.org) v20+ · [Python](https://www.python.org) 3.10+ · [uv](https://docs.astral.sh/uv/)

```bash
npx bmad-method install
```

> Want the newest prerelease build? Use `npx bmad-method@next install`. Expect higher churn than the default install.

Follow the installer prompts, then open your AI IDE (Claude Code, Cursor, etc.) in your project folder.

**Non-Interactive Installation** (for CI/CD):

```bash
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes
```

[See all installation options](https://docs.bmad-method.org/how-to/non-interactive-installation/)

> **Not sure what to do?** Ask `bmad-help` — it tells you exactly what's next and what's optional. You can also ask questions like `bmad-help I just finished the architecture, what do I do next?`

## Modules

BMad Method extends with official modules for specialized domains. Available during installation or anytime after.

| Module                                                                                                            | Purpose                                           |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **[BMad Method (BMM)](https://github.com/bmad-code-org/BMAD-METHOD)**                                             | Core framework with 34+ workflows                 |
| **[BMad Builder (BMB)](https://github.com/bmad-code-org/bmad-builder)**                                           | Create custom BMad agents and workflows           |
| **[Test Architect (TEA)](https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise)**             | Risk-based test strategy and automation           |
| **[Game Dev Studio (BMGD)](https://github.com/bmad-code-org/bmad-module-game-dev-studio)**                        | Game development workflows (Unity, Unreal, Godot) |
| **[Creative Intelligence Suite (CIS)](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite)** | Innovation, brainstorming, design thinking        |

## Documentation

[BMad Method Docs Site](https://docs.bmad-method.org) — Tutorials, guides, concepts, and reference

**Quick links:**
- [Getting Started Tutorial](https://docs.bmad-method.org/tutorials/getting-started/)
- [Upgrading from Previous Versions](https://docs.bmad-method.org/how-to/upgrade-to-v6/)
- [Test Architect Documentation](https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/)


## Community

- [Discord](https://discord.gg/gk8jAdXWmj) — Get help, share ideas, collaborate
- [YouTube](https://youtube.com/@BMadCode) — Tutorials, master class, and more
- [X / Twitter](https://x.com/BMadCode)
- [Website](https://bmadcode.com)
- [GitHub Issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) — Bug reports and feature requests
- [Discussions](https://github.com/bmad-code-org/BMAD-METHOD/discussions) — Community conversations

## Support BMad

BMad is free for everyone and always will be. Star this repo, [buy me a coffee](https://buymeacoffee.com/bmad), or email <contact@bmadcode.com> for corporate sponsorship.

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License — see [LICENSE](LICENSE) for details.

---

**BMad** and **BMAD-METHOD** are trademarks of BMad Code, LLC. See [TRADEMARK.md](TRADEMARK.md) for details.

[![Contributors](https://contrib.rocks/image?repo=bmad-code-org/BMAD-METHOD)](https://github.com/bmad-code-org/BMAD-METHOD/graphs/contributors)

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for contributor information.



> **Deep fetch: 30 key files fetched beyond README.**



---

# FILE: .coderabbit.yaml

# yaml-language-server: $schema=https://coderabbit.ai/integrations/schema.v2.json

language: "en-US"
early_access: true
reviews:
  profile: chill
  high_level_summary: false # don't post summary until explicitly invoked
  request_changes_workflow: false
  review_status: false
  commit_status: false
  walkthrough: false
  poem: false
  auto_review:
    enabled: true
    drafts: false # Don't review drafts automatically
    auto_incremental_review: false # always review the whole PR, not just new commits
    base_branches:
      - main
  path_filters:
    # --- Shared baseline: tool configs ---
    - "!.coderabbit.yaml"
    - "!.augment/**"
    - "!eslint.config.mjs"
    # --- Shared baseline: build output ---
    - "!dist/**"
    - "!build/**"
    - "!coverage/**"
    # --- Shared baseline: vendored/generated ---
    - "!**/node_modules/**"
    - "!**/*.min.js"
    - "!**/*.generated.*"
    - "!**/*.bundle.md"
    # --- Shared baseline: package metadata ---
    - "!package-lock.json"
    # --- Shared baseline: binary/media ---
    - "!*.png"
    - "!*.jpg"
    - "!*.svg"
    # --- Shared baseline: test fixtures ---
    - "!test/fixtures/**"
    - "!test/template-test-generator/**"
    - "!tools/template-test-generator/test-scenarios/**"
    # --- Shared baseline: non-project dirs ---
    - "!_bmad*/**"
    - "!website/**"
    - "!z*/**"
    - "!sample-project/**"
    - "!test-project-install/**"
    # --- Shared baseline: AI assistant dirs ---
    - "!.claude/**"
    - "!.codex/**"
    - "!.agent/**"
    - "!.agentvibes/**"
    - "!.kiro/**"
    - "!.roo/**"
    - "!.github/chatmodes/**"
    # --- Shared baseline: build temp ---
    - "!.bundler-temp/**"
    # --- Shared baseline: generated reports ---
    - "!**/validation-report-*.md"
    - "!CHANGELOG.md"
  path_instructions:
    - path: "src/**"
      instructions: |
        Source file changed. Check whether documentation under docs/ needs
        a corresponding update — new features, changed behavior, renamed
        concepts, altered CLI flags, or modified configuration options should
        all be reflected in the relevant doc pages. Flag missing or outdated
        docs as a review comment.
    - path: "src/**/skills/**"
      instructions: |
        Skill file. Apply the full rule catalog defined in tools/skill-validator.md.
        That document is the single source of truth for all skill validation rules
        covering SKILL.md metadata, workflow.md constraints, step file structure,
        path references, variable resolution, sequential execution, and skill
        invocation syntax.
    - path: "src/**/workflows/**"
      instructions: |
        Legacy workflow file (pre-skill conversion). Apply the full rule catalog
        defined in tools/skill-validator.md — the same rules apply to workflows
        that are being converted to skills.
    - path: "src/**/tasks/**"
      instructions: |
        Task file. Apply the full rule catalog defined in tools/skill-validator.md.
    - path: "src/**/*.agent.yaml"
      instructions: |
        Agent definition file. Check:
        - Has metadata section with id, name, title, icon, and module
        - Defines persona with role, identity, communication_style, and principles
        - Menu triggers reference valid skill names that exist
    - path: "docs/**/*.md"
      instructions: |
        Documentation file. Check internal markdown links point to existing files.
    - path: "tools/**"
      instructions: |
        Build script/tooling. Check error handling and proper exit codes.
chat:
  auto_reply: true # Response to mentions in comments, a la @coderabbit review
issue_enrichment:
  auto_enrich:
    enabled: false # don't auto-comment on issues




---

# FILE: .markdownlint-cli2.yaml

# markdownlint-cli2 configuration
# https://github.com/DavidAnson/markdownlint-cli2

ignores:
  - "**/node_modules/**"
  - test/fixtures/**
  - CODE_OF_CONDUCT.md
  - _bmad/**
  - _bmad*/**
  - .agent/**
  - .claude/**
  - .roo/**
  - .codex/**
  - .kiro/**
  - sample-project/**
  - test-project-install/**
  - z*/**

# Rule configuration
config:
  # Disable all rules by default
  default: false

  # Heading levels should increment by one (h1 -> h2 -> h3, not h1 -> h3)
  MD001: true

  # Duplicate sibling headings (same heading text at same level under same parent)
  MD024:
    siblings_only: true

  # Trailing commas in headings (likely typos)
  MD026:
    punctuation: ","

  # Bare URLs - may not render as links in all parsers
  # Should use <url> or [text](url) format
  MD034: true

  # Spaces inside emphasis markers - breaks rendering
  # e.g., "* text *" won't render as emphasis
  MD037: true



---

# FILE: AGENTS.md

# BMAD-METHOD

Open source framework for structured, agent-assisted software delivery.

## Rules

- Use Conventional Commits for every commit.
- Before pushing, run `npm ci && npm run quality` on `HEAD` in the exact checkout you are about to push.
  `quality` mirrors the checks in `.github/workflows/quality.yaml`.

- Skill validation rules are in `tools/skill-validator.md`.
- Deterministic skill checks run via `npm run validate:skills` (included in `quality`).



---

# FILE: CHANGELOG.md

# Changelog

## v6.3.0 - 2026-04-09

### 💥 Breaking Changes

* Remove custom content installation feature; use marketplace-based plugin installation instead (#2227)
* Remove bmad-init skill; all agents and skills now load config directly from `{project-root}/_bmad/bmm/config.yaml` (#2159)
* Remove spec-wip.md singleton; quick-dev now writes directly to `spec-{slug}.md` with status field, enabling parallel sessions (#2214)
* Consolidate three agent personas into Developer agent (Amelia): remove Barry quick-flow-solo-dev (#2177), Quinn QA agent (#2179), and Bob Scrum Master agent (#2186)

### 🎁 Features

* Universal source support for custom module installs with 5-strategy PluginResolver cascade supporting any Git host (GitHub, GitLab, Bitbucket, self-hosted) and local file paths (#2233)
* Community module browser with three-tier selection: official, community (category drill-down from marketplace index), and custom URL with unverified source warning (#2229)
* Switch module source of truth from bundled config to remote marketplace registry with network-failure fallback (#2228)
* Add bmad-prfaq skill implementing Amazon's Working Backwards methodology as alternative Phase 1 analysis path with 5-stage coached workflow and subagent architecture (#2157)
* Add bmad-checkpoint-preview skill for guided, concern-ordered human review of commits, branches, or PRs (#2145)
* Epic context compilation for quick-dev step-01: sub-agent compiles planning docs into cached `epic-{N}-context.md` for story implementation (#2218)
* Previous story continuity in quick-dev: load completed spec from same epic as implementation context (#2201)
* Planning artifact awareness in quick-dev: selectively load PRD, architecture, UX, and epics docs for context-informed specs (#2185)
* One-shot route now generates lightweight spec trace file for consistent artifact tracking (#2121)
* Improve checkpoint-preview UX with clickable spec paths, external edit detection, and missing-file halt (#2217)
* Add Junie (JetBrains AI) platform support (#2142)
* Restore KiloCoder support with native-skills installation (#2151)
* Add bmad-help support for llms.txt general questions (#2230)

### ♻️ Refactoring

* Consolidate party-mode into single SKILL.md with real subagent spawning via Agent tool, replacing multi-file workflow architecture (#2160)

### 🐛 Bug Fixes

* Fix version display bug where marketplace.json walk-up reported wrong version (#2233)
* Fix checkpoint-preview step-05 advancing without user confirmation by adding explicit HALT (#2184)
* Address adversarial triage findings: clarify review_mode transitions, label walkthrough branches, fix terse commit handling (#2180)
* Preserve local custom module sources during quick update (#2172)
* Support skills/ folder as fallback module source location for bmb compatibility (#2149)

### 🔧 Maintenance

* Overhaul installer branding with responsive BMAD METHOD logo, blue color scheme, unified version sourcing from marketplace.json, and surgical manifest-based skill cleanup (#2223)
* Stop copying skill prompts to _bmad by default (#2182)
* Add Python 3.10+ and uv as documented prerequisites (#2221)

### 📚 Documentation

* Complete Czech (cs-CZ) documentation translation (#2134)
* Complete Vietnamese (vi-VN) documentation translation (#2110, #2192)
* Rewrite get-answers-about-bmad as 1-2-3 escalation flow, remove deprecated references (#2213)
* Add checkpoint-preview explainer page and workflow diagram (#2183)
* Update docs theme to match bmadcode.com with responsive logo and blue color scheme (#2176)

## v6.2.2 - 2026-03-25

### ♻️ Refactoring

* Modernize module-help CSV to 13-column format with `after`/`before` dependency graph replacing sequence numbers (#2120)
* Rewrite bmad-help from procedural 8-step execution to outcome-based skill design (~50% shorter) (#2120)

### 🐛 Bug Fixes

* Update bmad-builder module-definition path from `src/module.yaml` to `skills/module.yaml` for bmad-builder v1.2.0 compatibility (#2126)
* Fix eslint config to ignore gitignored lock files (#2120)

### 📚 Documentation

* Close Epic 4.5 explanation gaps in Chinese (zh-CN): normalize command naming to current `bmad-*` convention and add cross-links across 9 explanation pages (#2102)

## v6.2.1 - 2026-03-24

### 🎁 Highlights

* Full rewrite of code-review skill with sharded step-file architecture, three parallel review layers (Blind Hunter, Edge Case Hunter, Acceptance Auditor), and interactive post-review triage (#2007, #2013, #2055)
* Quick Dev workflow overhaul: smart intent cascade, self-check gate, VS Code integration, clickable spec links, and spec rename (#2105, #2104, #2039, #2085, #2109)
* Add review trail generation with clickable `path:line` stops in spec file (#2033)
* Add clickable spec links using spec-file-relative markdown format (#2085, #2049)
* Preserve tracking identifiers in spec slug derivation (#2108)
* Deterministic skill validator with 19 rules across 6 categories, integrated into CI (#1981, #1982, #2004, #2002, #2051)
* Complete French (fr-FR) documentation translation (#2073)
* Add Ona platform support (#1968)
* Rename tech-spec → spec across templates and all documentation (#2109)

### 📚 Documentation

* Complete French (fr-FR) translation of all documentation with workflow diagrams (#2073)
* Refine Chinese (zh-CN) documentation: epic stories, how-to guides, getting-started, entry copy, help, anchor links (#2092–#2099, #2072)
* Add Chinese translation for core-tools reference (#2002)

## v6.2.0 - 2026-03-15

### 🎁 Highlights

* Fix manifest generation so BMad Builder installs correctly when a module has no agents (#1998)
* Prototype preview of bmad-product-brief-preview skill — try `/bmad-product-brief-preview` and share feedback! (#1959)
* All skills now use native skill directory format for improved modularity and maintainability (#1931, #1945, #1946, #1949, #1950, #1984, #1985, #1988, #1994)

### 🎁 Features

* Rewrite code-review skill with sharded step-file architecture and auto-detect review intent from invocation args (#2007, #2013)
* Add inference-based skill validator with comprehensive rules for naming, variables, paths, and invocation syntax (#1981)
* Add REF-03 skill invocation language rule and PATH-05 skill encapsulation rule to validator (#2004)

### 🐛 Bug Fixes

* Validation pass 2 — fix path, variable, and sequence issues across 32 files (#2008)
* Replace broken party-mode workflow refs with skill syntax (#2000)
* Improve bmad-help description for accurate trigger matching (#2012)
* Point zh-cn doc links to Chinese pages instead of English (#2010)
* Validation cleanup for bmad-quick-flow (#1997), 6 skills batch (#1996), bmad-sprint-planning (#1995), bmad-retrospective (#1993), bmad-dev-story (#1992), bmad-create-story (#1991), bmad-code-review (#1990), bmad-create-epics-and-stories (#1989), bmad-create-architecture (#1987), bmad-check-implementation-readiness (#1986), bmad-create-ux-design (#1983), bmad-create-product-brief (#1982)

### 🔧 Maintenance

* Normalize skill invocation syntax to `Invoke the skill` pattern repo-wide (#2004)

### 📚 Documentation

* Add Chinese translation for core-tools reference (#2002)
* Update version hint, TEA module link, and HTTP→HTTPS links in Chinese README (#1922, #1921)

## [6.1.0] - 2026-03-12

### Highlights

* Whiteport Design Studio (WDS) module enabled in the installer
* Support @next installation channel (`npx bmad-method@next install`) — get the latest tip of main instead of waiting for the next stable published version
* Everything now installs as a skill — all workflows, agents, and tasks converted to markdown with SKILL.md entrypoints (not yet optimized skills, but unified format)
* An experimental preview of the new Quick Dev is available, which will become the main Phase 4 development tool
* Edge Case Hunter added as a parallel code review layer in Phase 4, improving code quality by exhaustively tracing branching paths and boundary conditions (#1791)
* Documentation now available in Chinese (zh-CN) with complete translation (#1822, #1795)

### 💥 Breaking Changes

* Convert entire BMAD method to skills-based architecture with unified skill manifests (#1834)
* Convert all core workflows from YAML+instructions to single workflow.md format
* Migrate all remaining platforms to native Agent Skills format (#1841)
* Remove legacy YAML/XML workflow engine plumbing (#1864)

### 🎁 Features

* Add Pi coding agent as supported platform (#1854)
* Add unified skill scanner decoupled from legacy collectors (#1859)
* Add continuous delivery workflows for npm publishing with trusted OIDC publishing (#1872)

### ♻️ Refactoring

* Update terminology from "commands" to "skills" across all documentation (#1850)

### 🐛 Bug Fixes

* Fix code review removing mandatory minimum issue count that caused infinite review loops (#1913)
* Fix silent loss of brainstorming ideas in PRD by adding reconciliation step (#1914)
* Reduce npm tarball from 533 to 348 files (91% size reduction, 6.2 MB → 555 KB) via .npmignore (#1900)
* Fix party-mode skill conversion review findings (#1919)

---

## [6.0.4]

### 🎁 Features

* Add edge case hunter review task - new reusable review task that exhaustively traces branching paths and boundary conditions in code, reporting only unhandled gaps. Method-driven analysis complementary to adversarial review (#1790)

### 🐛 Bug Fixes

* Fix brainstorming to not overwrite previous sessions; now prompts to continue existing brainstorming or start a new one when older brainstorming sessions are found
* Fix installer templates - replace legacy `@` path prefixes with explicit `{project-root}` syntax for consistency (#1769)
* Fix edge case hunter - remove zero-findings halt condition that was pressuring the LLM to hallucinate findings when none legitimately exist (#1797)
* Fix broken docs domain references in README and GitHub issue templates (#1777)

---

## [6.0.3]

### 🎁 Features

* Add bmad-os-root-cause-analysis skill for analyzing bug-fix commits and producing structured root cause analysis reports with pyramid communication format (#1741)

### 🐛 Bug Fixes

* Fix installer to refuse installation when ancestor directory has BMAD commands, preventing duplicate command autocompletion in nested directories (#1735)
* Fix OpenCode integration by replacing unsupported `name` frontmatter with `mode: all` and update directory names to plural form (#1764)
* Fix CSV manifest pipeline double-escaping of quotes that was corrupting output files; switch Gemini templates to single quotes (#1746)
* Fix workflow descriptions to use proper quotes so they format better in skill conversion and don't break yaml front matter
* Fix workflow help task chaining by removing ambiguous "with-argument" clause that caused LLMs to misinterpret help.md as skill calls (#1740)

### ♻️ Refactoring

* Standardize all workflow descriptions to use proper quotes to prevent breaking command or skill front matter during skill conversion

### 📚 Documentation

* Fix broken TEA hyperlinks to point to new repository URL (#1772)
* Rebrand BMAD acronym to "Build More Architect Dreams" across documentation (#1765)

---

## [6.0.2]

### 🎁 Features

* Add CodeBuddy platform support with installer configuration (#1483)
* Add LLM audit prompt for file reference conventions - new audit tool using parallel subagents (#1720)
* Migrate Codex installer from `.codex/prompts` to `.agents/skills` format to align with Codex CLI changes (#1729)
* Convert review-pr and audit-file-refs tools to proper bmad-os skills with slash commands `bmad-os-review-pr` and `bmad-os-audit-file-refs` (#1732)

### 🐛 Bug Fixes

* Fix 24 broken step references in create-architecture workflow after directory rename (#1734)
* Fix step file path references in check-implementation-readiness workflow (#1709, #1716)
* Fix 3 broken file references and enable strict file reference validation in CI (#1717)
* Fix Rovo Dev integration with custom installer that generates prompts.yml manifest (#1701)
* Fix 104 relative step file references to use standardized `{project-root}/_bmad/` paths across 68 files (#1722)
* Fix code fence imbalance in step-03-starter.md that caused rendering issues (#1724)
* Remove Windsurf from recommended/preferred IDEs list (#1727)
* Fix default Codex install location from global to project for better defaults (#1698)
* Add npx cache workaround to Quick Start for stale beta versions (#1685)
* Add language instructions to replace placeholder text in Research overview (#1703)
* Ignore `.junie/` IDE integration folder in git and prettier configs (#1719)

### ♻️ Refactoring

* Update open source tool skills structure for future plugin migration
* Standardize all workflow descriptions for skill generation with concise format and explicit trigger phrases
* Remove `disable-model-invocation` flag from all IDE installer templates to enable workflow skill calls

### 📚 Documentation

* Elevate `bmad-help` as primary on-ramp across all documentation
* Update workflow names with `bmad-bmm-` prefix and standardize table formatting
* Clarify phase routing and catalog path in help task

---

## [6.0.0]

V6 Stable Release! The End of Beta!

### 🎁 Features

* Add PRD workflow steps 2b (vision/differentiators) and 2c (executive summary) for more complete product requirements documentation
* Add new `bmad uninstall` command with interactive and non-interactive modes for selective component removal
* Add dedicated GitHub Copilot installer that generates enriched `.agent.md`, `.prompt.md` files and project configuration
* Add TEA browser automation prerequisite prompts to guide Playwright CLI/MCP setup after configuration

### 🐛 Bug Fixes

* Fix version comparison to use semantic versioning, preventing incorrect downgrade recommendations to older beta versions
* Fix `--custom-content` flag to properly populate sources and selected files in module config
* Fix module configuration UX messaging to show accurate completion status and improve feedback timing
* Fix changelog URL in installer start message for proper GitHub resolution
* Remove incorrect `mode: primary` from OpenCode agent template and restore `name` field across all templates
* Auto-discover PRD files in validate-prd workflow to reduce manual path input
* Fix installer non-interactive mode hanging and improve IDE configuration handling during updates
* Fix workflow-level config.yaml copying for custom content modules

### ♻️ Refactoring

* Remove alias variables from Phase 4 workflows, use canonical `{implementation_artifacts}` and `{planning_artifacts}`
* Add missing `project_context` references to workflows for consistency

### 📚 Documentation

* Add post-install notes documentation for modules
* Improve project-context documentation and fix folder structure
* Add BMad Builder link to index for extenders

---

## [6.0.0-Beta.8]

**Release: February 8, 2026**

### 🌟 Key Highlights

1. **Non-Interactive Installation** — Full CI/CD support with 10 new CLI flags for automated deployments
2. **Complete @clack/prompts Migration** — Unified CLI experience with consolidated installer output
3. **CSV File Reference Validation** — Extended Layer 1 validator to catch broken workflow references in CSV files
4. **Kiro IDE Support** — Standardized config-driven installation, replacing custom installer

### 🎁 Features

* **Non-Interactive Installation** — Added `--directory`, `--modules`, `--tools`, `--custom-content`, `--user-name`, `--communication-language`, `--document-output-language`, `--output-folder`, and `-y/--yes` flags for CI/CD automation (#1520)
* **CSV File Reference Validation** — Extended validator to scan `.csv` files for broken workflow references, checking 501 references across 212 files (#1573)
* **Kiro IDE Support** — Replaced broken custom installer with config-driven templates using `#[[file:...]]` syntax and `inclusion: manual` frontmatter (#1589)
* **OpenCode Template Consolidation** — Combined split templates with `mode: primary` frontmatter for Tab-switching support, fixing agent discovery (#1556)
* **Modules Reference Page** — Added official external modules reference documentation (#1540)

### 🐛 Bug Fixes

* **Installer Streamlining** — Removed "None - Skip module installation" option, eliminated ~100 lines of dead code, and added ESM/.cjs support for module installers (#1590)
* **CodeRabbit Workflow** — Changed `pull_request` to `pull_request_target` to fix 403 errors and enable reviews on fork PRs (#1583)
* **Party Mode Return Protocol** — Added RETURN PROTOCOL to prevent lost-in-the-middle failures after Party Mode completes (#1569)
* **Spacebar Toggle** — Fixed SPACE key not working in autocomplete multiselect prompts for tool/IDE selection (#1557)
* **OpenCode Agent Routing** — Fixed agents installing to wrong directory by adding `targets` array for routing `.opencode/agent/` vs `.opencode/command/` (#1549)
* **Technical Research Workflow** — Fixed step-05 routing to step-06 and corrected `stepsCompleted` values (#1547)
* **Forbidden Variable Removal** — Removed `workflow_path` variable from 16 workflow step files (#1546)
* **Kilo Installer** — Fixed YAML formatting issues by trimming activation header and converting to yaml.parse/stringify (#1537)
* **bmad-help** — Now reads project-specific docs and respects `communication_language` setting (#1535)
* **Cache Errors** — Removed `--prefer-offline` npm flag to prevent stale cache errors during installation (#1531)

### ♻️ Refactoring

* **Complete @clack/prompts Migration** — Migrated 24 files from legacy libraries (ora, chalk, boxen, figlet, etc.), replaced ~100 console.log+chalk calls, consolidated installer output to single spinner, and removed 5 dependencies (#1586)
* **Downloads Page Removal** — Removed downloads page, bundle generation, and archiver dependency in favor of GitHub's native archives (#1577)
* **Workflow Verb Standardization** — Replaced "invoke/run" with "load and follow/load" in review workflow prompts (#1570)
* **Documentation Language** — Renamed "brownfield" to "established projects" and flattened directory structure for accessibility (#1539)

### 📚 Documentation

* **Comprehensive Site Review** — Fixed broken directory tree diagram, corrected grammar/capitalization, added SEO descriptions, and reordered how-to guides (#1578)
* **SEO Metadata** — Added description front matter to 9 documentation pages for search engine optimization (#1566)
* **PR Template** — Added pull request template for consistent PR descriptions (#1554)
* **Manual Release Cleanup** — Removed broken manual-release workflow and related scripts (#1576)

### 🔧 Maintenance

* **Dual-Mode AI Code Review** — Configured Augment Code (audit mode) and CodeRabbit (adversarial mode) for improved code quality (#1511)
* **Package-Lock Sync** — Cleaned up 471 lines of orphaned dependencies after archiver removal (#1580)

---

## [6.0.0-Beta.7]

**Release: February 4, 2026**

### 🌟 Key Highlights

1. **Direct Workflow Invocation** — Agent workflows can now be run directly via slash commands instead of only through agent orchestration
2. **Installer Workflow Support** — Installer now picks up `workflow-*.md` files, enabling multiple workflow files per directory

### 🎁 Features

* **Slash Command Workflow Access** — Research and PRD workflows now accessible via direct slash commands: `/domain-research`, `/market-research`, `/technical-research`, `/create-prd`, `/edit-prd`, `/validate-prd` (bd620e38, 731bee26)
* **Version Checking** — CLI now checks npm for newer versions and displays a warning banner when updates are available (d37ee7f2)

### ♻️ Refactoring

* **Workflow File Splitting** — Split monolithic `workflow.md` files into specific `workflow-*.md` files for individual workflow invocation (bd620e38)
* **Installer Multi-Workflow Support** — Installer manifest generator now supports `workflow-*.md` pattern, allowing multiple workflow files per directory (731bee26)
* **Internal Skill Renaming** — Renamed internal project skills to use `bmad-os-` prefix for consistent naming (5276d58b)

---

## [6.0.0-Beta.6]

**Release: February 4, 2026**

### 🌟 Key Highlights

1. **Cross-File Reference Validator**: Comprehensive tool to detect broken file references, preventing 59 known bugs (~25% of historical issues)
2. **New AutocompleteMultiselect Prompt**: Searchable multi-select with improved tool/IDE selection UX
3. **Critical Installer Fixes**: Windows CRLF parsing, Gemini CLI TOML support, file extension preservation
4. **Codebase Cleanup**: Removed dead Excalidraw/flattener artifacts (-3,798 lines)

### 🎁 Features

* **Cross-File Reference Validator** — Validates ~483 references across ~217 source files, detecting absolute path leaks and broken references (PR #1494)
* **AutocompleteMultiselect Prompt** — Upgraded `@clack/prompts` to v1.0.0 with custom searchable multiselect, Tab-to-fill-placeholder behavior, and improved tool/IDE selection UX (PR #1514)
* **OT Domains** — Added `process_control` and `building_automation` domains with high complexity ratings (PR #1510)
* **Documentation Reference Pages** — Added `docs/reference/agents.md`, `commands.md`, and `testing.md` (PR #1525)

### 🐛 Bug Fixes

* **Critical Installer Fixes** — Fixed CRLF line ending parsing on Windows, Gemini CLI TOML support, file extension preservation, Codex task generation, Windows path handling, and CSV parsing (PR #1492)
* **Double Tool Questioning** — Removed redundant tool questioning during installation (df176d42)
* **QA Agent Rename** — Renamed Quinn agent to `qa` for naming consistency (PR #1508)
* **Documentation Organization** — Fixed documentation ordering and links, hide BMGD pages from main LLM docs (PR #1525)

### ♻️ Refactoring

* **Excalidraw/Flattener Removal** — Removed dead artifacts no longer supported beyond beta: Excalidraw workflows, flattener tool, and 12+ diagram creation workflows (-3,798 lines) (f699a368)
* **Centralized Constants** — Centralized `BMAD_FOLDER_NAME` to reduce hardcoded strings (PR #1492)
* **Cross-Platform Paths** — Fixed path separator inconsistencies in agent IDs (PR #1492)

### 📚 Documentation

* **BMGD Diataxis Refactor** — Refactored BMGD documentation using Diataxis principles for better organization (PR #1502)
* **Generate Project Context** — Restored `generate-project-context` workflow for brownfield project analysis (PR #1491)

### 🔧 Maintenance

* **Dependency Updates** — Upgraded `@clack/prompts` from v0.11.0 to v1.0.0 and added `@clack/core` (PR #1514)
* **CI Integration** — Added `validate:refs` to CI quality workflow with warning annotations (PR #1494)

---

## [6.0.0-Beta.5]

### 🎁 Features

* **Add generate-project-context workflow** — New 3-step workflow for project context generation, integrated with quick-flow-solo-dev agent
* **Shard market research customer analysis** — Refactor monolithic customer insights into 4-step detailed customer behavior analysis workflow

### 🐛 Bug Fixes

* **Fix npm install peer dependency issues** — Add `.npmrc` with `legacy-peer-deps=true`, update Starlight to 0.37.5, and add `--legacy-peer-deps` flag to module installer (PR #1476)
* **Fix leaked source paths in PRD validation report** — Replace absolute `/src/core/` paths with `{project-root}/_bmad/core/` (#1481)
* **Fix orphaned market research customer analysis** — Connect step-01-init to step-02-customer-behavior to complete workflow sharding (#1486)
* **Fix duplicate 2-letter brainstorming code** — Change BS to BSP to resolve conflict with cis Brainstorming module
* **Fix tech writer sidecar functionality** — Enable proper sidecar operation (#1487)
* **Fix relative paths in workflow steps** — Correct paths in step-11-polish (#1497) and step-e-04-complete (#1498)
* **Fix party-mode workflow file extension** — Correct extension in workflow.xml (#1499)
* **Fix generated slash commands** — Add `disable-model-invocation` to all generated commands (#1501)
* **Fix agent scan and help CSV files** — Correct module-help.csv entries
* **Fix HELP_STEP placeholder replacement** — Fix placeholder not replaced in compiled agents, fix hardcoded path, fix single quote (#1437)

### 📚 Documentation

* **Add exact slash commands to Getting Started guide** — Provide precise command examples for users (#1505)
* **Remove .claude/commands from version control** — Commands are generated, not tracked (#1506)

### 🔧 Maintenance

* **Update Starlight to 0.37.5** — Latest version with peer dependency compatibility
* **Add GitHub issue templates** — New bug-report.yaml and documentation.yaml templates

---

## [6.0.0-Beta.4]

### 🐛 Bug Fixes

- **Activation steps formatting fix**: Fixed missing opening quote that caused infrequent menu rendering issues
- **Custom module installation fix**: Added missing yaml require in manifest.js to fix custom module installation

---

## [6.0.0-Beta.3]

### 🌟 Key Highlights

1. **SDET Module Replaces TEA**: TEA module removed from core, SDET module added with "automate" workflow for test automation
2. **Gemini CLI TOML Support**: IDE integration now supports the TOML config format used by Gemini CLI
3. **File System Sprint Status**: Default project_key support for file-system based sprint status tracking

### 🔧 Features & Improvements

**Module Changes:**
- **TEA Module Moved to External** (#1430, #1443): The TEA module is now external. SDET module added with a single "automate" workflow focused on test automation
- **SDET Module**: New module with streamlined test automation capabilities

**IDE Integration:**
- **Gemini CLI TOML Format** (#1431): Previous update accidentally switched Gemini to md instead of toml.

**Sprint Status:**
- **Default project_key** (#1446): File-system based sprint status now uses a default project_key so certain LLMs do not complain

### 🐛 Bug Fixes

- **Quick-flow workflow path fix** (#1368): Fixed incorrect workflow_path in bmad-quick-flow/quick-spec steps (step-01, step-02, step-03) - changed from non-existent 'create-tech-spec' to correct 'quick-spec'
- **PRD edit flow paths**: Fixed path references in PRD editing workflow
- **Agent file handling**: Changes to prevent double agent files and use .agent.md file extensions
- **README link fix**: Corrected broken documentation links

## [6.0.0-Beta.2]

- Fix installer so commands match what is installed, centralize most ide into a central file instead of separate files for each ide.
- Specific IDEs may still need udpates, but all is config driven now and should be easier to maintain
- Kiro still needs updates, but its been in this state since contributed, will investigate soon
- Any version older than Beta.0 will recommend removal and reinstall to project. From later alphas though its sufficient to quick update if still desired, but best is just start fresh with Beta.

## [6.0.0-Beta.1]

**Release: January 2026 - Alpha to Beta Transition**

### 🎉 Beta Release

- **Transition from Alpha to Beta**: BMad Method is now in Beta! This marks a significant milestone in the framework's development
- **NPM Default Tag**: Beta versions are now published with the `latest` tag, making `npx bmad-method` serve the beta version by default

### 🌟 Key Highlights

1. **bmad-help**: Revolutionary AI-powered guidance system replaces the alpha workflow-init and workflow tracking — introduces full AI intelligence to guide users through workflows, commands, and project context
2. **Module Ecosystem Expansion**: bmad-builder, CIS (Creative Intelligence Suite), and Game Dev Studio moved to separate repositories for focused development
3. **Installer Consolidation**: Unified installer architecture with standardized command naming (`bmad-dash-case.md` or `bmad-*-agent-*.md`)
4. **Windows Compatibility**: Complete migration from Inquirer.js to @clack/prompts for reliable cross-platform support

### 🚀 Major Features

**bmad-help - Intelligent Guidance System:**

- **Replaces**: workflow-init and legacy workflow tracking
- **AI-Powered**: Full context awareness of installed modules, workflows, agents, and commands
- **Dynamic Discovery**: Automatically catalogs all available workflows from installed modules
- **Intelligent Routing**: Guides users to the right workflow or agent based on their goal
- **IDE Integration**: Generates proper IDE command files for all discovered workflows

**Module Restructuring:**

| Module                                | Status                                            | New Location                                            |
| ------------------------------------- | ------------------------------------------------- | ------------------------------------------------------- |
| **bmad-builder**                      | Near beta, with docs and walkthroughs coming soon | `bmad-code-org/bmad-builder`                            |
| **CIS** (Creative Intelligence Suite) | Published as npm package                          | `bmad-code-org/bmad-module-creative-intelligence-suite` |
| **Game Dev Studio**                   | Published as npm package                          | `bmad-code-org/bmad-module-game-dev-studio`             |

### 🔧 Installer & CLI Improvements

**UnifiedInstaller Architecture:**

- All IDE installers now use a common `UnifiedInstaller` class
- Standardized command naming conventions:
  - Workflows: `bmad-module-workflow-name.md`
  - Agents: `bmad-module-agent-name.md`
  - Tasks: `bmad-task-name.md`
  - Tools: `bmad-tool-name.md`
- External module installation from npm with progress indicators
- Module removal on unselect with confirmation

**Windows Compatibility Fix:**

- Replaced Inquirer.js with @clack/prompts to fix arrow key navigation issues on Windows
- All 91 installer workflows migrated to new prompt system

### 📚 Documentation Updates

**Significant docsite improvements:**

- Interactive workflow guide page (`/workflow-guide`) with track selector
- TEA documentation restructured using Diátaxis framework (25 docs)
- Style guide optimized for LLM readers (367 lines, down from 767)
- Glossary rewritten using table format (123 lines, down from 373)
- README overhaul with numbered command flows and prominent `bmad-help` callout
- New workflow map diagram with interactive HTML
- New editorial review tasks for document quality
- E2E testing methodology for Game Dev Studio

More documentation updates coming soon.

### 🐛 Bug Fixes

- Fixed TodoMVC URL references to include `/dist/` path
- Fixed glob pattern normalization for Windows compatibility
- Fixed YAML indentation in kilo.js customInstructions field
- Fixed stale path references in check-implementation-readiness workflow
- Fixed sprint-status.yaml sync in correct-course workflow
- Fixed web bundler entry point reference
- Fixed mergeModuleHelpCatalogs ordering after generateManifests

### 📊 Statistics

- **91 commits** since alpha.23
- **969 files changed** (+23,716 / -91,509 lines)
- **Net reduction of ~67,793 lines** through cleanup and consolidation
- **3 major modules** moved to separate repositories
- **Complete installer refactor** for standardization

---

## [6.0.0-alpha.23]

**Release: January 11, 2026**

### 🌟 Key Highlights

1. **Astro/Starlight Documentation Platform**: Complete migration from Docusaurus to modern Astro+Starlight for superior performance and customization
2. **Diataxis Framework Implementation**: Professional documentation restructuring with tutorials, how-to guides, explanations, and references
3. **Workflow Creator & Validator**: Powerful new tools for workflow creation with subprocess support and PRD validation
4. **TEA Documentation Expansion**: Comprehensive testing documentation with cheat sheets, MCP enhancements, and API testing patterns
5. **Brainstorming Revolution**: Research-backed procedural rigor with 100+ idea goal and anti-bias protocols
6. **Cursor IDE Modernization**: Refactored from rules-based to command-based architecture for better IDE integration

### 📚 Documentation Platform Revolution

**Astro/Starlight Migration:**

- **From Docusaurus to Astro**: Complete platform migration for improved performance, better customization, and modern tooling
- **Starlight Theme**: Professional documentation theme with dark mode default and responsive design
- **Build Pipeline Overhaul**: New build-docs.js orchestrates link checking, artifact generation, and Astro build
- **LLM-Friendly Documentation**: Generated llms.txt and llms-full.txt for AI agent discoverability
- **Downloadable Source Bundles**: bmad-sources.zip and bmad-prompts.zip for offline use

**Diataxis Framework Implementation:**

- **Four Content Types**: Professional separation into tutorials, how-to guides, explanations, and references
- **21 Files Migrated**: Phase 1 migration of core documentation to Diataxis structure
- **42+ Focused Documents**: Phase 2 split of large legacy files into manageable pieces
- **FAQ Restructuring**: 7 topic-specific FAQ files with standardized format
- **Tutorial Style Guide**: Comprehensive documentation standards for consistent content creation

**Link Management & Quality:**

- **Site-Relative Links**: Converted 217 links to repo-relative format (/docs/path/file.md)
- **Link Validation Tools**: New validate-doc-links.js and fix-doc-links.js for maintaining link integrity
- **Broken Link Fixes**: Resolved ~50 broken internal links across documentation
- **BMad Acronym Standardization**: Consistent use of "BMad" (Breakthrough Method of Agile AI Driven Development)
- **SEO Optimization**: Absolute URLs in AI meta tags for better web crawler discoverability

### 🔧 Workflow Creator & Validator (Major Feature)

**Workflow Creation Tool:**

- **Subprocess Support**: Advanced workflows can now spawn subprocesses for complex operations
- **PRD Validation Step**: New validation step ensures PRD quality before workflow execution
- **Trimodal Workflow Creation**: Three-mode workflow generation system
- **Quadrivariate Module Workflow**: Four-variable workflow architecture for enhanced flexibility
- **Path Violation Checks**: Validator ensures workflows don't violate path constraints
- **Max Parallel Mode POC**: Proof-of-concept for parallel workflow validation

**Workflow Quality Improvements:**

- **PRD Trimodal Compliance**: PRD workflow now follows trimodal standards
- **Standardized Step Formatting**: Consistent markdown formatting across workflow and PRD steps
- **Better Suggested Next Steps**: Improved workflow completion guidance
- **Variable Naming Standardization**: {project_root} → {project-root} across all workflows

### 🧪 TEA Documentation Expansion

**Comprehensive Testing Guides:**

- **Cheat Sheets**: Quick reference guides for common testing scenarios
- **MCP Enhancements**: Model Context Protocol improvements for testing workflows
- **API Testing Patterns**: Best practices for API testing documentation
- **Design Philosophy Callout**: Clear explanation of TEA's design principles
- **Context Engineering Glossary**: New glossary entry defining context engineering concepts
- **Fragment Count Updates**: Accurate documentation of TEA workflow components
- **Playwright Utils Examples**: Updated code examples for playwright-utils integration

### 💡 Brainstorming Workflow Overhaul

**Research-Backed Procedural Rigor:**

- **100+ Idea Goal**: Emphasis on quantity-first approach to unlock better quality ideas
- **Anti-Bias Protocol**: Domain pivot every 10 ideas to reduce cognitive biases
- **Chain-of-Thought Requirements**: Reasoning before idea generation
- **Simulated Temperature**: Prompts for higher divergence in ideation
- **Standardized Idea Format**: Quality control template for consistent output
- **Energy Checkpoints**: Multiple continuation options to maintain creative flow

**Exploration Menu Improvements:**

- **Letter-Based Navigation**: [K/T/A/B/C] options instead of numbers for clarity
- **Keep/Try/Advanced/Break/Continue**: Clear action options for idea refinement
- **Universal Facilitation Rules**: Consistent guidelines across all brainstorming steps
- **Quality Growth Enforcement**: Balance between quantity and quality metrics

### 🖥️ Cursor IDE Modernization

**Command-Based Architecture:**

- **From Rules to Commands**: Complete refactor from rules-based to command-based system
- **Command Generation**: Automatic generation of task and tool commands
- **Commands Directory**: New `.cursor/commands/bmad/` structure for generated commands
- **Cleanup Integration**: Automatic cleanup of old BMAD commands alongside rules
- **Enhanced Logging**: Better feedback on agents, tasks, tools, and workflow commands generated

### 🤖 Agent System Improvements

**Agent Builder & Validation:**

- **hasSidecar Field**: All agents now indicate sidecar support (true/false)
- **Validation Enforcement**: hasSidecar now required in agent validation
- **Better Brownfield Documentation**: Improved brownfield project documentation
- **Agent Builder Updates**: Agent builder now uses hasSidecar field
- **Agent Editor Integration**: Editor workflow respects hasSidecar configuration

### 🐛 Bug Fixes & Quality Improvements

**Critical Fixes:**

- **Windows Line Endings**: Resolved CRLF issues causing cross-platform problems
- **Code-Review File Filtering**: Fixed code-review picking up non-application files
- **ERR_REQUIRE_ESM Resolution**: Dynamic import for inquirer v9+ compatibility
- **Project-Context Conflicts**: Allow full project-context usage with conflict precedence
- **Workflow Paths**: Fixed paths for workflow and sprint status files
- **Missing Scripts**: Fixed missing scripts from installation

**Workflow & Variable Fixes:**

- **Variable Naming**: Standardized from {project_root} to {project-root} across CIS, BMGD, and BMM modules
- **Workflow References**: Fixed broken .yaml → .md workflow references
- **Advanced Elicitation Variables**: Fixed undefined variables in brainstorming
- **Dependency Format**: Corrected dependency format and added missing frontmatter

**Code Quality:**

- **Dependency Updates**: Bumped qs from 6.14.0 to 6.14.1
- **CodeRabbit Integration**: Enabled auto-review on new PRs
- **TEA Fragment Counts**: Updated fragment counts for accuracy
- **Documentation Links**: Fixed Discord channel references (#general-dev → #bmad-development)

### 🚀 Installation & CLI Improvements

**Installation Enhancements:**

- **Workflow Exclusion**: Ability to exclude workflows from being added as commands
- **Example Workflow Protection**: Example workflow in workflow builder now excluded from tools
- **CNAME Configuration**: Added CNAME file for custom domain support
- **Script Fixes**: All scripts now properly included in installation

### 📊 Statistics

- **27 commits** since alpha.22
- **217 documentation links** converted to site-relative format
- **42+ focused documents** created from large legacy files
- **7 topic-specific FAQ files** with standardized formatting
- **Complete documentation platform** migrated from Docusaurus to Astro/Starlight
- **Major workflow tools** added: Creator, Validator with subprocess support
- **Brainstorming workflow** overhauled with research-backed rigor

---

## [6.0.0-alpha.22]

**Release: December 31, 2025**

### 🌟 Key Highlights

1. **Unified Agent Workflow**: Create, Edit, and Validate workflows consolidated into single powerful agent workflow with separate step paths
2. **Agent Knowledge System**: Comprehensive data file architecture with persona properties, validation patterns, and crafting principles
3. **Deep Language Integration**: All sharded progressive workflows now support language choice at every step
4. **Core Module Documentation**: Extensive docs for core workflows (brainstorming, party mode, advanced elicitation)
5. **BMAD Core Concepts**: New documentation structure explaining agents, workflows, modules, and installation
6. **Tech Spec Sharded**: create-tech-spec workflow converted to sharded format with orient-first pattern

### 🤖 Unified Agent Workflow (Major Feature)

**Consolidated Architecture:**

- **Single Workflow, Three Paths**: Create, Edit, and Validate operations unified under `src/modules/bmb/workflows/agent/`
- **steps-c/**: Create path with 9 comprehensive steps for building new agents
- **steps-e/**: Edit path with 10 steps for modifying existing agents
- **steps-v/**: Validate path for standalone agent validation review
- **data/**: Centralized knowledge base for all agent-building intel

### 📚 Agent Knowledge System

**Data File Architecture:**

Located in `src/modules/bmb/workflows/agent/data/`:

- **agent-metadata.md** (208 lines) - Complete metadata field reference
- **agent-menu-patterns.md** (233 lines) - Menu design patterns and best practices
- **agent-compilation.md** (273 lines) - Compilation process documentation
- **persona-properties.md** (266 lines) - Persona crafting properties and examples
- **principles-crafting.md** (292 lines) - Core principles for agent design
- **critical-actions.md** (120 lines) - Critical action patterns
- **expert-agent-architecture.md** (236 lines) - Expert agent structure
- **expert-agent-validation.md** (173 lines) - Expert-specific validation
- **module-agent-validation.md** (124 lines) - Module-specific validation
- **simple-agent-architecture.md** (204 lines) - Simple agent structure
- **simple-agent-validation.md** (132 lines) - Simple agent validation
- **understanding-agent-types.md** (222 lines) - Agent type comparison
- **brainstorm-context.md** - Brainstorming guidance
- **communication-presets.csv** - Communication style presets

**Reference Examples:**

- **reference/module-examples/architect.agent.yaml** - Module agent example
- **reference/simple-examples/commit-poet.agent.yaml** - Simple agent example
- **journal-keeper/** - Complete sidecar pattern example

**Templates:**

- **templates/simple-agent.template.md** - Simple agent template
- **templates/expert-agent-template/expert-agent.template.md** - Expert agent template
- **templates/expert-agent-sidecar/** - Sidecar templates (instructions, memories)

### 🌍 Deep Language Integration

**Progressive Workflow Language Support:**

- **Every Step Biased**: All sharded progressive workflow steps now include language preference context
- **260+ Files Updated**: Comprehensive language integration across:
  - Core workflows (brainstorming, party mode, advanced elicitation)
  - BMB workflows (create-agent, create-module, create-workflow, edit-workflow, etc.)
  - BMGD workflows (game-brief, gdd, narrative, game-architecture, etc.)
  - BMM workflows (research, create-ux-design, prd, create-architecture, etc.)
- **Tested Languages**: Verified working with Spanish and Pirate Speak
- **Natural Conversations**: AI agents respond in configured language throughout workflow

### 📖 Core Module Documentation

**New Core Documentation Structure:**

`docs/modules/core/`:

- **index.md** - Core module overview
- **core-workflows.md** - Core workflow documentation
- **core-tasks.md** - Core task reference
- **brainstorming.md** (100 lines) - Brainstorming workflow guide
- **party-mode.md** (50 lines) - Party mode guide
- **advanced-elicitation.md** (105 lines) - Advanced elicitation techniques
- **document-sharding-guide.md** (133 lines) - Sharded workflow format guide
- **global-core-config.md** - Global core configuration reference

**Advanced Elicitation Moved:**

- **From**: `docs/` root
- **To**: `src/core/workflows/advanced-elicitation/`
- **Status**: Now a proper core workflow with methods.csv

### 📚 BMAD Core Concepts Documentation

**New Documentation Structure:**

`docs/bmad-core-concepts/`:

- **index.md** - Core concepts introduction
- **agents.md** (93 lines) - Understanding agents in BMAD
- **workflows.md** (89 lines) - Understanding workflows in BMAD
- **modules.md** (76 lines) - Understanding modules (BMM, BMGD, CIS, BMB, Core)
- **installing/index.md** (77 lines) - Installation guide
- **installing/upgrading.md** (144 lines) - Upgrading guide
- **bmad-customization/index.md** - Customization overview
- **bmad-customization/agents.md** - Agent customization guide
- **bmad-customization/workflows.md** (30 lines) - Workflow customization guide
- **web-bundles/index.md** (34 lines) - Web bundle distribution guide

**Documentation Cleanup:**

- **Removed v4-to-v6-upgrade.md** - Outdated upgrade guide
- **Removed document-sharding-guide.md** from docs root (moved to core)
- **Removed web-bundles-gemini-gpt-guide.md** - Consolidated into web-bundles/index.md
- **Removed getting-started/installation.md** - Migrated to bmad-core-concepts
- **Removed all ide-info/*.md files** - Consolidated into web-bundles documentation

### 🔧 Create-Tech-Spec Sharded Conversion

**Monolithic to Sharded:**

- **From**: Single `workflow.yaml` with `instructions.md`
- **To**: Sharded `workflow.md` with individual step files
- **Pattern**: Orient-first approach (understand before investigating)

### 🔨 Additional Improvements

**Workflow Status Path Fixes:**

- **Corrected Discovery Paths**: workflow-status workflows now properly use planning_artifacts and implementation_artifacts
- **Updated All Path Files**: enterprise-brownfield, enterprise-greenfield, method-brownfield, method-greenfield

**Documentation Updates:**

- **BMB Agent Creation Guide**: Comprehensive 166-line guide for agent creation
- **Workflow Vendoring Doc**: New 42-line guide on workflow customization and inheritance
- **Document Project Reference**: Moved from BMM docs to shared location
- **Workflows Planning Guide**: New 89-line guide for planning workflows

**BMB Documentation Streamlining:**

- **Removed Redundant Docs**: Eliminated duplicate documentation in `src/modules/bmb/docs/`
- **Step File Rules**: New 469-line comprehensive guide for step file creation
- **Agent Docs Moved**: Agent architecture and validation docs moved to workflow data/

**Windows Inquirer Fix:**

- **Another Default Addition**: Additional inquirer default value setting for better Windows multiselection support

**Code Quality:**

- **Removed Old BMM README**: Consolidated module documentation
- **Removed BMM Troubleshooting**: 661-line doc moved to shared location
- **Removed Enterprise Agentic Development**: 686-line doc consolidated
- **Removed Scale Adaptive System**: 618-line doc consolidated

---

## [6.0.0-alpha.21]

**Release: December 27, 2025**

### 🌟 Key Highlights

1. **Consistent Menu System**: All agents now use standardized 2-letter menu codes (e.g., "rd" for research, "ca" for create-architecture)
2. **Planning Artifacts Architecture**: Phase 1-3 workflows now properly segregate planning artifacts from documentation
3. **Windows Installer Fixed Again**: Updated inquirer to resolve multiselection tool issues
4. **Auto-Injected Features**: Chat and party mode automatically injected into all agents
5. **Validation System**: All agents now pass comprehensive new validation checks

### 🎯 Consistent Menu System (Major Feature)

**Standardized 2-Letter Codes:**

- **Compound Menu Triggers**: All agents now use consistent 2-letter compound trigger format (e.g., `bmm-rd`, `bmm-ca`)
- **Improved UX**: Shorter, more memorable command shortcuts across all modules
- **Module Prefixing**: Menu items properly scoped by module prefix (bmm-, bmgd-, cis-, bmb-)
- **Universal Pattern**: All 22 agents updated to follow the same menu structure

**Agent Updates:**

- **BMM Module**: 9 agents with standardized menus (pm, analyst, architect, dev, ux-designer, tech-writer, sm, tea, quick-flow-solo-dev)
- **BMGD Module**: 6 agents with standardized menus (game-architect, game-designer, game-dev, game-qa, game-scrum-master, game-solo-dev)
- **CIS Module**: 6 agents with standardized menus (innovation-strategist, design-thinking-coach, creative-problem-solver, brainstorming-coach, presentation-master, storyteller)
- **BMB Module**: 3 agents with standardized menus (bmad-builder, agent-builder, module-builder, workflow-builder)
- **Core Module**: BMAD Master agent updated with consistent menu patterns

### 📁 Planning Artifacts Architecture

**Content Segregation Implementation:**

- **Phase 1-3 Workflows**: All planning workflows now use `planning_artifacts` folder (default changed from `docs`)
- **Proper Input Discovery**: Workflows follow consistent input discovery patterns from planning artifacts
- **Output Management**: Planning artifacts properly separated from long-term documentation
- **Affected Workflows**:
  - Product Brief: Updated discovery and output to planning artifacts
  - PRD: Fixed discovery and output to planning artifacts
  - UX Design: Updated all steps for proper artifact handling
  - Architecture: Updated discovery and output flow
  - Game Architecture: Updated for planning artifacts
  - Story Creation: Updated workflow output paths

**File Organization:**

- **Planning Artifacts**: Ephemeral planning documents (prd.md, product-brief.md, ux-design.md, architecture.md)
- **Documentation**: Long-term project documentation (separate from planning)
- **Module Configuration**: BMM and BMGD modules updated with proper default paths

### 🪟 Windows Installer Fixes

**Inquirer Multiselection Fix:**

- **Updated Inquirer Version**: Resolved tool multiselection issues that were causing Windows installer failures
- **Better Compatibility**: Improved handling of checkbox and multi-select prompts on Windows(?)

### 🤖 Agent System Improvements

**Auto-Injected Features:**

- **Chat Mode**: Automatically injected into all agents during compilation
- **Party Mode**: Automatically injected into all agents during compilation
- **Reduced Manual Configuration**: No need to manually add these features to agent definitions
- **Consistent Behavior**: All agents now have uniform access to chat and party mode capabilities

**Agent Normalization:**

- **All Agents Validated**: All 22 agents pass comprehensive validation checks
- **Schema Enforcement**: Proper compound trigger validation implemented
- **Metadata Cleanup**: Removed obsolete and inconsistent metadata patterns
- **Test Fixtures Updated**: Validation test fixtures aligned with new requirements

### 🔧 Bug Fixes & Cleanup

**Docusaurus Merge Recovery:**

- **Restored Agent Files**: Fixed agent files accidentally modified in Docusaurus merge (PR #1191)
- **Reference Cleanup**: Removed obsolete agent reference examples (journal-keeper, security-engineer, trend-analyst)
- **Test Fixture Updates**: Aligned test fixtures with current validation requirements

**Code Quality:**

- **Schema Improvements**: Enhanced agent schema validation with better error messages
- **Removed Redundancy**: Cleaned up duplicate and obsolete agent definitions
- **Installer Cleanup**: Removed unused configuration code from BMM installer

**Planning Artifacts Path:**
- Default: `planning_artifacts/` (configurable in module.yaml)
- Previous: `docs/`
- Benefit: Clear separation between planning work and permanent documentation

---

## [6.0.0-alpha.20]

**Release: December 23, 2025**

### 🌟 Key Highlights

1. **Windows Installer Fixed**: Better compatibility with inquirer v9.x upgrade
2. **Path Segregation**: Revolutionary content organization separating ephemeral artifacts from permanent documentation
3. **Custom Installation Messages**: Configurable intro/outro messages for professional installation experience
4. **Enhanced Upgrade Logic**: Two-version auto upgrades with proper config preservation
5. **Quick-Dev Refactor**: Sharded format with comprehensive adversarial review
6. **Improved Quality**: Streamlined personas, fixed workflows, and cleaned up documentation
7. **Doc Site Auto Generation**; Auto Generate a docusaurus site update on merge

### 🪟 Windows Installer (hopefully) Fixed

**Inquirer Upgrade:**

- **Updated to v9.x**: Upgraded inquirer package for better Windows support
- **Improved Compatibility**: Better handling of Windows terminal environments
- **Enhanced UX**: More reliable interactive prompts across platforms

### 🎯 Path Segregation Implementation (Major Feature)

**Revolutionary Content Organization:**

- **Phase 1-4 Path Segregation**: Implemented new BM paths across all BMM and BMGD workflows
- **Planning vs Implementation Artifacts**: Separated ephemeral Phase 4 artifacts from permanent documentation
- **Optimized File Organization**: Better structure differentiating planning artifacts from long-term project documentation
- **Backward Compatible**: Existing installations continue working while preparing for optimized content organization
- **Module Configuration Updates**: Enhanced module.yaml with new path configurations for all phases
- **Workflow Path Updates**: All 90+ workflow files updated with proper path configurations

**Documentation Cleanup:**

- **Removed Obsolete Documentation**: Cleaned up 3,100+ lines of outdated documentation
- **Streamlined README Files**: Consolidated and improved module documentation
- **Enhanced Clarity**: Removed redundant content and improved information architecture

### 💬 Installation Experience Enhancements

**Custom Installation Messages:**

- **Configurable Intro/Outro Messages**: New install-messages.yaml file for customizable installation messages
- **Professional Installation Flow**: Custom welcome messages and completion notifications
- **Module-Specific Messaging**: Tailored messages for different installation contexts
- **Enhanced User Experience**: More informative and personalized installation process

**Core Module Improvements:**

- **Always Ask Questions**: Core module now always prompts for configuration (no accept defaults)
- **Better User Engagement**: Ensures users actively configure their installation
- **Improved Configuration Accuracy**: Reduces accidental acceptance of defaults

### 🔧 Upgrade & Configuration Management

**Two-Version Auto Upgrade:**

- **Smarter Upgrade Logic**: Automatic upgrades now span 2 versions (e.g., .16 → .18)
- **Config Variable Preservation**: Ensures all configuration variables are retained during quick updates
- **Seamless Updates**: Quick updates now preserve custom settings properly
- **Enhanced Upgrade Safety**: Better handling of configuration across version boundaries

### 🤖 Workflow Improvements

**Quick-Dev Workflow Refactor (PR #1182):**

- **Sharded Format Conversion**: Converted quick-dev workflow to modern step-file format
- **Adversarial Review Integration**: Added comprehensive self-check and adversarial review steps
- **Enhanced Quality Assurance**: 6-step process with mode detection, context gathering, execution, self-check, review, and resolution
- **578 New Lines Added**: Significant expansion of quick-dev capabilities

**BMGD Workflow Fixes:**

- **workflow-status Filename Correction**: Fixed incorrect filename references (PR #1172)
- **sprint-planning Update**: Added workflow-status update to game-architecture completion
- **Path Corrections**: Resolved dead references and syntax errors (PR #1164)

### 🎨 Code Quality & Refactoring

**Persona Streamlining (PR #1167):**

- **Quick-Flow-Solo-Dev Persona**: Streamlined for clarity and accuracy
- **Improved Agent Behavior**: More focused and efficient solo development support

**Package Management:**

- **package-lock.json Sync**: Ensured version consistency (PR #1168)
- **Dependency Cleanup**: Reduced package-lock bloat significantly

**Prettier Configuration:**

- **Markdown Underscore Protection**: Prettier will no longer mess up underscores in markdown files
- **Disabled Auto-Fix**: Markdown formatting issues now handled more intelligently
- **Better Code Formatting**: Improved handling of special characters in documentation

### 📚 Documentation Updates

**Sponsor Attribution:**

- **DigitalOcean Sponsorship**: Added attribution for DigitalOcean support (PR #1162)

**Content Reorganization:**

- **Removed Unused Docs**: Eliminated obsolete documentation files
- **Consolidated References**: Merged and reorganized technical references
- **Enhanced README Files**: Improved module and workflow documentation

### 🧹 Cleanup & Optimization

**File Organization:**

- **Removed Asterisk Insertion**: Eliminated unwanted asterisk insertions into agent files
- **Removed Unused Commands**: Cleaned up deprecated command references
- **Consolidated Duplication**: Reduced code duplication across multiple files
- **Removed Unneeded Folders**: Cleaned up temporary and obsolete directory structures

### 📊 Statistics

- **23 commits** since alpha.19
- **90+ workflow files** updated with new path configurations
- **3,100+ lines of documentation** removed and reorganized
- **578 lines added** to quick-dev workflow with adversarial review
- **Major architectural improvement** to content organization

## [6.0.0-alpha.19]

**Release: December 18, 2025**

### 🐛 Bug Fixes

**Installer Stability:**

- **Fixed \_bmad Folder Stutter**: Resolved issue with duplicate \_bmad folder creation when applying agent custom files
- **Cleaner Installation**: Removed unnecessary backup file that was causing bloat in the installer
- **Streamlined Agent Customization**: Fixed path handling for agent custom files to prevent folder duplication

### 📊 Statistics

- **3 files changed** with critical fix
- **3,688 lines removed** by eliminating backup files
- **Improved installer performance** and stability

---

## [6.0.0-alpha.18]

**Release: December 18, 2025**

### 🎮 BMGD Module - Complete Game Development Module Updated

**Massive BMGD Overhaul:**

- **New Game QA Agent (GLaDOS)**: Elite Game QA Architect with test automation specialization
  - Engine-specific expertise: Unity, Unreal, Godot testing frameworks
  - Comprehensive knowledge base with 15+ testing topics
  - Complete testing workflows: test-framework, test-design, automate, playtest-plan, performance-test, test-review

- **New Game Solo Dev Agent (Indie)**: Rapid prototyping and iteration specialist
  - Quick-flow workflows optimized for solo/small team development
  - Streamlined development process for indie game creators

- **Production Workflow Alignment**: BMGD 4-production now fully aligned with BMM 4-implementation
  - Removed obsolete workflows: story-done, story-ready, story-context, epic-tech-context
  - Added sprint-status workflow for project tracking
  - All workflows updated as standalone with proper XML instructions

**Game Testing Architecture:**

- **Complete Testing Knowledge Base**: 15 comprehensive testing guides covering:
  - Engine-specific: Unity (TF 1.6.0), Unreal, Godot testing
  - Game-specific: Playtesting, balance, save systems, multiplayer
  - Platform: Certification (TRC/XR), localization, input systems
  - QA Fundamentals: Automation, performance, regression, smoke testing

**New Workflows & Features:**

- **workflow-status**: Multi-mode status checker for game projects
  - Game-specific project levels (Game Jam → AAA)
  - Support for gamedev and quickflow paths
  - Project initialization workflow

- **create-tech-spec**: Game-focused technical specification workflow
  - Engine-aware (Unity/Unreal/Godot) specifications
  - Performance and gameplay feel considerations

- **Enhanced Documentation**: Complete documentation suite with 9 guides
  - agents-guide.md: Reference for all 6 agents
  - workflows-guide.md: Complete workflow documentation
  - game-types-guide.md: 24 game type templates
  - quick-flow-guide.md: Rapid development guide
  - Comprehensive troubleshooting and glossary

### 🤖 Agent Management Improved

**Agent Recompile Feature:**

- **New Menu Item**: Added "Recompile Agents" option to the installer menu
- **Selective Compilation**: Recompile only agents without full module upgrade
- **Faster Updates**: Quick agent updates without complete reinstallation
- **Customization Integration**: Automatically applies customizations during recompile

**Agent Customization Enhancement:**

- **Complete Field Support**: ALL fields from agent customization YAML are now properly injected
- **Deep Merge Implementation**: Customizations now properly override all agent properties
- **Persistent Customizations**: Custom settings survive updates and recompiles
- **Enhanced Flexibility**: Support for customizing metadata, persona, menu items, and workflows

### 🔧 Installation & Module Management

**Custom Module Installation:**

- **Enhanced Module Addition**: Modify install now supports adding custom modules even if none were originally installed
- **Flexible Module Management**: Easy addition and removal of custom modules post-installation
- **Improved Manifest Tracking**: Better tracking of custom vs core modules

**Quality Improvements:**

- **Comprehensive Code Review**: Fixed 20+ issues identified in PR review
- **Type Validation**: Added proper type checking for configuration values
- **Path Security**: Enhanced path traversal validation for better security
- **Documentation Updates**: All documentation updated to reflect new features

### 📊 Statistics

- **178 files changed** with massive BMGD expansion
- **28,350+ lines added** across testing documentation and workflows
- **2 new agents** added to BMGD module
- **15 comprehensive testing guides** created
- **Complete alignment** between BMGD and BMM production workflows

### 🌟 Key Highlights

1. **BMGD Module Revolution**: Complete overhaul with professional game development workflows
2. **Game Testing Excellence**: Comprehensive testing architecture for all major game engines
3. **Agent Management**: New recompile feature allows quick agent updates without full reinstall
4. **Full Customization Support**: All agent fields now customizable via YAML
5. **Industry-Ready Documentation**: Professional-grade guides for game development teams

---

## [6.0.0-alpha.17]

**Release: December 16, 2025**

### 🚀 Revolutionary Installer Overhaul

**Unified Installation Experience:**

- **Streamlined Module Installation**: Completely redesigned installer with unified flow for both core and custom content
- **Single Install Panel**: Eliminated disjointed clearing between modules for smoother, more intuitive installation
- **Quick Default Selection**: New quick install feature with default selections for faster setup of selected modules
- **Enhanced UI/UX**: Improved question order, reduced verbose output, and cleaner installation interface
- **Logical Question Flow**: Reorganized installer questions to follow natural progression and user expectations

**Custom Content Installation Revolution:**

- **Full Custom Content Support**: Re-enabled complete custom content generation and sharing through the installer
- **Custom Module Tracking**: Manifest now tracks custom modules separately to ensure they're always installed from the custom cache
- **Custom Installation Order**: Custom modules now install after core modules for better dependency management
- **Quick Update with Custom Content**: Quick update now properly retains and updates custom content
- **Agent Customization Integration**: Customizations are now applied during quick updates and agent compilation

### 🧠 Revolutionary Agent Memory & Visibility System

**Breaking Through Dot-Folder Limitations:**

- **Dot-Folder to Underscore Migration**: Critical change from `.bmad` to `_bmad` ensures LLMs (Codex, Claude, and others) can no longer ignore or skip BMAD content - dot folders are commonly filtered out by AI systems
- **Universal Content Visibility**: Underscore folders are treated as regular content, ensuring full AI agent access to all BMAD resources and configurations
- **Agent Memory Architecture**: Rolled out comprehensive agent memory support for installed agents with `-sidecar` folders
- **Persistent Agent Learning**: Sidecar content installs to `_bmad/_memory`, giving each agent the ability to learn and remember important information specific to its role

**Content Location Strategy:**

- **Standardized Memory Location**: All sidecar content now uses `_bmad/_memory` as the unified location for agent memories
- **Segregated Output System**: New architecture supports differentiating between ephemeral Phase 4 artifacts and long-term documentation
- **Forward Compatibility**: Existing installations continue working with content in docs folder, with optimization coming in next release
- **Configuration Cleanup**: Renamed `_cfg` to `_config` for clearer naming conventions
- **YAML Library Consolidation**: Reduced dependency to use only one YAML library for better stability

### 🎯 Future-Ready Architecture

**Content Organization Preview:**

- **Phase 4 Artifact Segregation**: Infrastructure ready for separating ephemeral workflow artifacts from permanent documentation
- **Planning vs Implementation Docs**: New system will differentiate between planning artifacts and long-term project documentation
- **Backward Compatibility**: Current installs maintain full functionality while preparing for optimized content organization
- **Quick Update Path**: Tomorrow's quick update will fully optimize all BMM workflows to use new segregated output locations

### 🎯 Sample Modules & Documentation

**Comprehensive Examples:**

- **Sample Unitary Module**: Complete example with commit-poet agent and quiz-master workflow
- **Sample Wellness Module**: Meditation guide and wellness companion agents demonstrating advanced patterns
- **Enhanced Documentation**: Updated README files and comprehensive installation guides
- **Custom Content Creation Guides**: Step-by-step documentation for creating and sharing custom modules

### 🔧 Bug Fixes & Optimizations

**Installer Improvements:**

- **Fixed Duplicate Entry Issue**: Resolved duplicate entries in files manifest
- **Reduced Log Noise**: Less verbose logging during installation for cleaner user experience
- **Menu Wording Updates**: Improved menu text for better clarity and understanding
- **Fixed Quick Install**: Resolved issues with quick installation functionality

**Code Quality:**

- **Minor Code Cleanup**: General cleanup and refactoring throughout the codebase
- **Removed Unused Code**: Cleaned up deprecated and unused functionality
- **Release Workflow Restoration**: Fixed automated release workflow for v6

**BMM Phase 4 Workflow Improvements:**

- **Sprint Status Enhancement**: Improved sprint-status validation with interactive correction for unknown values and better epic status handling
- **Story Status Standardization**: Normalized all story status references to lowercase kebab-case (ready-for-dev, in-progress, review, done)
- **Removed Stale Story State**: Eliminated deprecated 'drafted' story state - stories now go directly from creation to ready-for-dev
- **Code Review Clarity**: Improved code review completion message from "Story is ready for next work!" to "Code review complete!" for better clarity
- **Risk Detection Rules**: Rewrote risk detection rules for better LLM clarity and fixed warnings vs risks naming inconsistency

### 📊 Statistics

- **40+ commits** since alpha.16
- **Major installer refactoring** with complete UX overhaul
- **2 new sample modules** with comprehensive examples
- **Full custom content support** re-enabled and improved

### 🌟 Key Highlights

1. **Installer Revolution**: The installation system has been completely overhauled for better user experience, reliability, and speed
2. **Custom Content Freedom**: Users can now easily create, share, and install custom content through the streamlined installer
3. **AI Visibility Breakthrough**: Migration from `.bmad` to `_bmad` ensures LLMs can access all BMAD content (dot folders are commonly ignored by AI systems)
4. **Agent Memory System**: Rolled out persistent agent memory support - agents with `-sidecar` folders can now learn and remember important information in `_bmad/_memory`
5. **Quick Default Selection**: Installation is now faster with smart default selections for popular configurations
6. **Future-Ready Architecture**: Infrastructure in place for segregating ephemeral artifacts from permanent documentation (full optimization coming in next release)

## [6.0.0-alpha.16]

**Release: December 10, 2025**

### 🔧 Temporary Changes & Fixes

**Installation Improvements:**

- **Temporary Custom Content Installation Disable**: Custom content installation temporarily disabled to improve stability
- **BMB Workflow Path Fixes**: Fixed numerous path references in BMB workflows to ensure proper step file resolution
- **Package Updates**: Updated dependencies for improved security and performance

**Path Resolution Improvements:**

- **BMB Agent Builder Fixes**: Corrected path references in step files and documentation
- **Workflow Path Standardization**: Ensured consistent path handling across all BMB workflows
- **Documentation References**: Updated internal documentation links and references

**Cleanup Changes:**

- **Example Modules Removal**: Temporarily removed example modules to prevent accidental installation
- **Memory Management**: Improved sidecar file handling for custom modules

### 📊 Statistics

- **336 files changed** with path fixes and improvements
- **4 commits** since alpha.15

---

## [6.0.0-alpha.15]

**Release: December 7, 2025**

### 🔧 Module Installation Standardization

**Unified Module Configuration:**

- **module.yaml Standard**: All modules now use `module.yaml` instead of `_module-installer/install-config.yaml` for consistent configuration (BREAKING CHANGE)
- **Universal Installer**: Both core and custom modules now use the same installer with consistent behavior
- **Streamlined Module Creation**: Module builder templates updated to use new module.yaml standard
- **Enhanced Module Discovery**: Improved module caching and discovery mechanisms

**Custom Content Installation Revolution:**

- **Interactive Custom Content Search**: Installer now proactively asks if you have custom content to install
- **Flexible Location Specification**: Users can indicate custom content location during installation
- **Improved Custom Module Handler**: Enhanced error handling and debug output for custom installations
- **Comprehensive Documentation**: New custom-content-installation.md guide (245 lines) replacing custom-agent-installation.md

### 🤖 Code Review Integration Expansion

**AI Review Tools:**

- **CodeRabbit AI Integration**: Added .coderabbit.yaml configuration for automated code review
- **Raven's Verdict PR Review Tool**: New PR review automation tool (297 lines of documentation)
- **Review Path Configuration**: Proper exclusion patterns for node_modules and generated files
- **Review Documentation**: Comprehensive usage guidance and skip conditions for PRs

### 📚 Documentation Improvements

**Documentation Restructuring:**

- **Code of Conduct**: Moved to .github/ folder following GitHub standards
- **Gem Creation Link**: Updated to point to Gemini Gem manager instead of deprecated interface
- **Example Custom Content**: Improved README files and disabled example modules to prevent accidental installation
- **Custom Module Documentation**: Enhanced module installation guides with new YAML structure

### 🧹 Cleanup & Optimization

**Memory Management:**

- **Removed Hardcoded .bmad Folders**: Cleaned up demo content to use configurable paths
- **Sidecar File Cleanup**: Removed old .bmad-user-memory folders from wellness modules
- **Example Content Organization**: Better organization of example-custom-content directory

**Installer Improvements:**

- **Debug Output Enhancement**: Added informative debug output when installer encounters errors
- **Custom Module Caching**: Improved caching mechanism for custom module installations
- **Consistent Behavior**: All modules now behave consistently regardless of custom or core status

### 📊 Statistics

- **77 files changed** with 2,852 additions and 607 deletions
- **15 commits** since alpha.14

### ⚠️ Breaking Changes

1. **module.yaml Configuration**: All modules must now use `module.yaml` instead of `_module-installer/install-config.yaml`
   - Core modules updated automatically
   - Custom modules will need to rename their configuration file
   - Module builder templates generate new format

### 📦 New Dependencies

- No new dependencies added in this release

---

## [6.0.0-alpha.14]

**Release: December 7, 2025**

### 🔧 Installation & Configuration Revolution

**Custom Module Installation Overhaul:**

- **Simple custom.yaml Installation**: Custom agents and workflows can now be installed with a single YAML file
- **IDE Configuration Preservation**: Upgrades will no longer delete custom modules, agents, and workflows from IDE configuration
- **Removed Legacy agent-install Command**: Streamlined installation process (BREAKING CHANGE)
- **Sidecar File Retention**: Custom sidecar files are preserved during updates
- **Flexible Agent Sidecar Locations**: Fully configurable via config options instead of hardcoded paths

**Module Discovery System Transformation:**

- **Recursive Agent Discovery**: Deep scanning for agents across entire project structure
- **Enhanced Manifest Generation**: Comprehensive scanning of all installed modules
- **Nested Agent Support**: Fixed nested agents appearing in CLI commands
- **Module Reinstall Fix**: Prevented modules from showing as obsolete during reinstall

### 🏗️ Advanced Builder Features

**Workflow Builder Evolution:**

- **Continuable Workflows**: Create workflows with sophisticated branching and continuation logic
- **Template LOD Options**: Level of Detail output options for flexible workflow generation
- **Step-Based Architecture**: Complete conversion to granular step-file system
- **Enhanced Creation Process**: Improved workflow creation with better template handling

**Module Builder Revolution:**

- **11-Step Module Creation**: Comprehensive step-by-step module generation process
- **Production-Ready Templates**: Complete templates for agents, installers, and workflow plans
- **Built-in Validation System**: Ensures module quality and BMad Core compliance
- **Professional Documentation**: Auto-generated module documentation and structure

### 🚀 BMad Method (BMM) Enhancements

**Workflow Improvements:**

- **Brownfield PRD Support**: Enhanced PRD workflow for existing project integration
- **Sprint Status Command**: New workflow for tracking development progress
- **Step-Based Format**: Improved continue functionality across all workflows
- **Quick-Spec-Flow Documentation**: Rapid development specification flows

**Documentation Revolution:**

- **Comprehensive Troubleshooting Guide**: 680-line detailed troubleshooting documentation
- **Quality Check Integration**: Added markdownlint-cli2 for markdown quality assurance
- **Enhanced Test Architecture**: Improved CI/CD templates and testing workflows

### 🌟 New Features & Integrations

**Kiro-Cli Installer:**

- **Intelligent Routing**: Smart routing to quick-dev workflow
- **BMad Core Compliance**: Full compliance with BMad standards

**Discord Notifications:**

- **Compact Format**: Streamlined plain-text notifications
- **Bug Fixes**: Resolved notification delivery issues

**Example Mental Wellness Module (MWM):**

- **Complete Module Example**: Demonstrates advanced module patterns
- **Multiple Agents**: CBT Coach, Crisis Navigator, Meditation Guide, Wellness Companion
- **Workflow Showcase**: Crisis support, daily check-in, meditation, journaling workflows

### 🐛 Bug Fixes & Optimizations

- Fixed version reading from package.json instead of hardcoded fallback
- Removed hardcoded years from WebSearch queries
- Removed broken build caching mechanism
- Enhanced TTS injection summary with tracking and documentation
- Fixed CI nvmrc configuration issues

### 📊 Statistics

- **335 files changed** with 17,161 additions and 8,204 deletions
- **46 commits** since alpha.13

### ⚠️ Breaking Changes

1. **Removed agent-install Command**: Migrate to new custom.yaml installation system
2. **Agent Sidecar Configuration**: Now requires explicit config instead of hardcoded paths

### 📦 New Dependencies

- `markdownlint-cli2: ^0.19.1` - Professional markdown linting

---

## [6.0.0-alpha.13]

**Release: November 30, 2025**

### 🏗️ Revolutionary Workflow Architecture

- **Step-File System**: Complete conversion to granular step-file architecture with dynamic menu generation
- **Phase 4 Transformation**: Simplified architecture with sprint planning integration (Jira, Linear, Trello)
- **Performance Improvements**: Eliminated time-based estimates, reduced file loading times
- **Legacy Cleanup**: Removed all deprecated workflows for cleaner system

### 🤖 Agent System Revolution

- **Universal Custom Agent Support**: Extended to ALL IDEs including Antigravity and Rovo Dev
- **Agent Creation Workflow**: Enhanced with better documentation and parameter clarity
- **Multi-Source Discovery**: Agents now check multiple source locations for better discovery
- **GitHub Migration**: Integration moved from chatmodes to agents folder

### 🧪 Testing Infrastructure

- **Playwright Utils Integration**: @seontechnologies/playwright-utils across all testing workflows
- **TTS Injection System**: Complete text-to-speech integration for voice feedback
- **Web Bundle Test Support**: Enabled web bundles for test environments

### ⚠️ Breaking Changes

1. **Legacy Workflows Removed**: Migrate to new stepwise sharded workflows
2. **Phase 4 Restructured**: Update automation expecting old Phase 4 structure
3. **Agent Compilation Required**: Custom agents must use new creation workflow

## [6.0.0-alpha.12]

**Release: November 19, 2025**

### 🐛 Bug Fixes

- Added missing `yaml` dependency to fix `MODULE_NOT_FOUND` error when running `npx bmad-method install`

## [6.0.0-alpha.11]

**Release: November 18, 2025**

### 🚀 Agent Installation Revolution

- **bmad agent-install CLI**: Interactive agent installation with persona customization
- **4 Reference Agents**: commit-poet, journal-keeper, security-engineer, trend-analyst
- **Agent Compilation Engine**: YAML → XML with smart handler injection
- **60 Communication Presets**: Pure communication styles for agent personas

### 📚 BMB Agent Builder Enhancement

- **Complete Documentation Suite**: 7 new guides for agent architecture and creation
- **Expert Agent Sidecar Support**: Multi-file agents with templates and knowledge bases
- **Unified Validation**: 160-line checklist shared across workflows
- **BMM Agent Voices**: All 9 agents enhanced with distinct communication styles

### 🎯 Workflow Architecture Change

- **Epic Creation Moved**: Now in Phase 3 after Architecture for technical context
- **Excalidraw Distribution**: Diagram capabilities moved to role-appropriate agents
- **Google Antigravity IDE**: New installer with flattened file naming

### ⚠️ Breaking Changes

1. **Frame Expert Retired**: Use role-appropriate agents for diagrams
2. **Agent Installation**: New bmad agent-install command replaces manual installation
3. **Epic Creation Phase**: Moved from Phase 2 to Phase 3

## [6.0.0-alpha.10]

**Release: November 16, 2025**

- **Epics After Architecture**: Major milestone - technically-informed user stories created post-architecture
- **Frame Expert Agent**: New Excalidraw specialist with 4 diagram workflows
- **Time Estimate Prohibition**: Warnings across 33 workflows acknowledging AI's impact on development speed
- **Platform-Specific Commands**: ide-only/web-only fields filter menu items by environment
- **Agent Customization**: Enhanced memory/prompts merging via \*.customize.yaml files

## [6.0.0-alpha.9]

**Release: November 12, 2025**

- **Intelligent File Discovery**: discover_inputs with FULL_LOAD, SELECTIVE_LOAD, INDEX_GUIDED strategies
- **3-Track System**: Simplified from 5 levels to 3 intuitive tracks
- **Web Bundles Guide**: Comprehensive documentation with 60-80% cost savings strategies
- **Unified Output Structure**: Eliminated .ephemeral/ folders - single configurable output folder
- **BMGD Phase 4**: Added 10 game development workflows with BMM patterns

## [6.0.0-alpha.8]

**Release: November 9, 2025**

- **Configurable Installation**: Custom directories with .bmad hidden folder default
- **Optimized Agent Loading**: CLI loads from installed files, eliminating duplication
- **Party Mode Everywhere**: All web bundles include multi-agent collaboration
- **Phase 4 Artifact Separation**: Stories, code reviews, sprint plans configurable outside docs
- **Expanded Web Bundles**: All BMM, BMGD, CIS agents bundled with elicitation integration

## [6.0.0-alpha.7]

**Release: November 7, 2025**

- **Workflow Vendoring**: Web bundler performs automatic cross-module dependency vendoring
- **BMGD Module Extraction**: Game development split into standalone 4-phase structure
- **Advanced Elicitation Fix**: Added missing CSV files to workflow bundles
- **Claude Code Fix**: Resolved README slash command installation regression

## [6.0.0-alpha.6]

**Release: November 4, 2025**

- **Critical Installer Fixes**: Fixed manifestPath error and option display issues
- **Conditional Docs Installation**: Optional documentation to reduce production footprint
- **Improved Installer UX**: Better formatting with descriptive labels and clearer feedback
- **Issue Tracker Cleanup**: Closed 54 legacy v4 issues for focused v6 development
- **Contributing Updates**: Removed references to non-existent branches

## [6.0.0-alpha.5]

**Release: November 4, 2025**

- **3-Track Scale System**: Simplified from 5 levels to 3 intuitive preference-driven tracks
- **Elicitation Modernization**: Replaced legacy XML tags with explicit invoke-task pattern
- **PM/UX Evolution**: Added November 2025 industry research on AI Agent PMs
- **Brownfield Reality Check**: Rewrote Phase 0 with 4 real-world scenarios
- **Documentation Accuracy**: All agent capabilities now match YAML source of truth

## [6.0.0-alpha.4]

**Release: November 2, 2025**

- **Documentation Hub**: Created 18 comprehensive guides (7000+ lines) with professional standards
- **Paige Agent**: New technical documentation specialist across all BMM phases
- **Quick Spec Flow**: Intelligent Level 0-1 planning with auto-stack detection
- **Universal Shard-Doc**: Split large markdown documents with dual-strategy loading
- **Intent-Driven Planning**: PRD and Product Brief transformed from template-filling to conversation

## [6.0.0-alpha.3]

**Release: October 2025**

- **Codex Installer**: Custom prompts in `.codex/prompts/` directory structure
- **Bug Fixes**: Various installer and workflow improvements
- **Documentation**: Initial documentation structure established

## [6.0.0-alpha.0]

**Release: September 28, 2025**

- **Lean Core**: Simple common tasks and agents (bmad-web-orchestrator, bmad-master)
- **BMad Method (BMM)**: Complete scale-adaptive rewrite supporting projects from small enhancements to massive undertakings
- **BoMB**: BMad Builder for creating and converting modules, workflows, and agents
- **CIS**: Creative Intelligence Suite for ideation and creative workflows
- **Game Development**: Full subclass of game-specific development patterns**Note**: Version 5.0.0 was skipped due to NPX registry issues that corrupted the version. Development continues with v6.0.0-alpha.0.

## [v4.43.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v4.43.0)

**Release: August-September 2025 (v4.31.0 - v4.43.1)**

Focus on stability, ecosystem growth, and professional tooling.

### Major Integrations

- **Codex CLI & Web**: Full Codex integration with web and CLI modes
- **Auggie CLI**: Augment Code integration
- **iFlow CLI**: iFlow support in installer
- **Gemini CLI Custom Commands**: Enhanced Gemini CLI capabilities

### Expansion Packs

- **Godot Game Development**: Complete game dev workflow
- **Creative Writing**: Professional writing agent system
- **Agent System Templates**: Template expansion pack (Part 2)

### Advanced Features

- **AGENTS.md Generation**: Auto-generated agent documentation
- **NPM Script Injection**: Automatic package.json updates
- **File Exclusion**: `.bmad-flattenignore` support for flattener
- **JSON-only Integration**: Compact integration mode

### Quality & Stability

- **PR Validation Workflow**: Automated contribution checks
- **Fork-Friendly CI/CD**: Opt-in mechanism for forks
- **Code Formatting**: Prettier integration with pre-commit hooks
- **Update Checker**: `npx bmad-method update-check` command

### Flattener Improvements

- Detailed statistics with emoji-enhanced `.stats.md`
- Improved project root detection
- Modular component architecture
- Binary directory exclusions (venv, node_modules, etc.)

### Documentation & Community

- Brownfield document naming consistency fixes
- Architecture template improvements
- Trademark and licensing clarity
- Contributing guidelines refinement

### Developer Experience

- Version synchronization scripts
- Manual release workflow enhancements
- Automatic release notes generation
- Changelog file path configuration

[View v4.43.1 tag](https://github.com/bmad-code-org/BMAD-METHOD/tree/v4.43.1)

## [v4.30.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v4.30.0)

**Release: July 2025 (v4.21.0 - v4.30.4)**

Introduction of advanced IDE integrations and command systems.

### Claude Code Integration

- **Slash Commands**: Native Claude Code slash command support for agents
- **Task Commands**: Direct task invocation via slash commands
- **BMad Subdirectory**: Organized command structure
- **Nested Organization**: Clean command hierarchy

### Agent Enhancements

- BMad-master knowledge base loading
- Improved brainstorming facilitation
- Better agent task following with cost-saving model combinations
- Direct commands in agent definitions

### Installer Improvements

- Memory-efficient processing
- Clear multi-select IDE prompts
- GitHub Copilot support with improved UX
- ASCII logo (because why not)

### Platform Support

- Windows compatibility improvements (regex fixes, newline handling)
- Roo modes configuration
- Support for multiple CLI tools simultaneously

### Expansion Ecosystem

- 2D Unity Game Development expansion pack
- Improved expansion pack documentation
- Better isolated expansion pack installations

[View v4.30.4 tag](https://github.com/bmad-code-org/BMAD-METHOD/tree/v4.30.4)

## [v4.20.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v4.20.0)

**Release: June 2025 (v4.11.0 - v4.20.0)**

Major focus on documentation quality and expanding QA agent capabilities.

### Documentation Overhaul

- **Workflow Diagrams**: Visual explanations of planning and development cycles
- **QA Role Expansion**: QA agent transformed into senior code reviewer
- **User Guide Refresh**: Complete rewrite with clearer explanations
- **Contributing Guidelines**: Clarified principles and contribution process

### QA Agent Transformation

- Elevated from simple tester to senior developer/code reviewer
- Code quality analysis and architectural feedback
- Pre-implementation review capabilities
- Integration with dev cycle for quality gates

### IDE Ecosystem Growth

- **Cline IDE Support**: Added configuration for Cline
- **Gemini CLI Integration**: Native Gemini CLI support
- **Expansion Pack Installation**: Automated expansion agent setup across IDEs

### New Capabilities

- Markdown-tree integration for document sharding
- Quality gates to prevent task completion with failures
- Enhanced brownfield workflow documentation
- Team-based agent bundling improvements

### Developer Tools

- Better expansion pack isolation
- Automatic rule generation for all supported IDEs
- Common files moved to shared locations
- Hardcoded dependencies removed from installer

[View v4.20.0 tag](https://github.com/bmad-code-org/BMAD-METHOD/tree/v4.20.0)

## [v4.10.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v4.10.0)

**Release: June 2025 (v4.3.0 - v4.10.3)**

This release focused on making BMAD more configurable and adaptable to different project structures.

### Configuration System

- **Optional Core Config**: Document sharding and core configuration made optional
- **Flexible File Resolution**: Support for non-standard document structures
- **Debug Logging**: Configurable debug mode for agent troubleshooting
- **Fast Update Mode**: Quick updates without breaking customizations

### Agent Improvements

- Clearer file resolution instructions for all agents
- Fuzzy task resolution for better agent autonomy
- Web orchestrator knowledge base expansion
- Better handling of deviant PRD/Architecture structures

### Installation Enhancements

- V4 early detection for improved update flow
- Prevented double installation during updates
- Better handling of YAML manifest files
- Expansion pack dependencies properly included

### Bug Fixes

- SM agent file resolution issues
- Installer upgrade path corrections
- Bundle build improvements
- Template formatting fixes

[View v4.10.3 tag](https://github.com/bmad-code-org/BMAD-METHOD/tree/v4.10.3)

## [v4.0.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v4.0.0)

**Release: June 20, 2025 (v4.0.0 - v4.2.0)**

Version 4 represented a complete architectural overhaul, transforming BMAD from a collection of prompts into a professional, distributable framework.

### Framework Transformation

- **NPM Package**: Professional distribution and simple installation via `npx bmad-method install`
- **Modular Architecture**: Move to `.bmad-core` hidden folder structure
- **Multi-IDE Support**: Unified support for Claude Code, Cursor, Roo, Windsurf, and many more
- **Schema Standardization**: YAML-based agent and team definitions
- **Automated Installation**: One-command setup with upgrade detection

### Agent System Overhaul

- Agent team workflows (fullstack, no-ui, all agents)
- Web bundle generation for platform-agnostic deployment
- Task-based architecture (separate task definitions from agents)
- IDE-specific agent activation (slash commands for Claude Code, rules for Cursor, etc.)

### New Capabilities

- Brownfield project support (existing codebases)
- Greenfield project workflows (new projects)
- Expansion pack architecture for domain specialization
- Document sharding for better context management
- Automatic semantic versioning and releases

### Developer Experience

- Automatic upgrade path from v3 to v4
- Backup creation for user customizations
- VSCode settings and markdown linting
- Comprehensive documentation restructure

[View v4.2.0 tag](https://github.com/bmad-code-org/BMAD-METHOD/tree/v4.2.0)

## [v3.0.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v3.0.0)

**Release: May 20, 2025**

Version 3 introduced the revolutionary orchestrator concept, creating a unified agent experience.

### Major Features

- **BMad Orchestrator**: Uber-agent that orchestrates all specialized agents
- **Web-First Approach**: Streamlined web setup with pre-compiled agent bundles
- **Simplified Onboarding**: Complete setup in minutes with clear quick-start guide
- **Build System**: Scripts to compile web agents from modular components

### Architecture Changes

- Consolidated agent system with centralized orchestration
- Web build sample folder with ready-to-deploy configurations
- Improved documentation structure with visual setup guides
- Better separation between web and IDE workflows

### New Capabilities

- Single agent interface (`/help` command system)
- Brainstorming and ideation support
- Integrated method explanation within the agent itself
- Cross-platform consistency (Gemini Gems, Custom GPTs)

[View V3 Branch](https://github.com/bmad-code-org/BMAD-METHOD/tree/V3)

## [v2.0.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v2.0.0)

**Release: April 17, 2025**

Version 2 addressed the major shortcomings of V1 by introducing separation of concerns and quality validation mechanisms.

### Major Improvements

- **Template Separation**: Templates decoupled from agent definitions for greater flexibility
- **Quality Checklists**: Advanced elicitation checklists to validate document quality
- **Web Agent Discovery**: Recognition of Gemini Gems and Custom GPTs power for structured planning
- **Granular Web Agents**: Simplified, clearly-defined agent roles optimized for web platforms
- **Installer**: A project installer that copied the correct files to a folder at the destination

### Key Features

- Separated template files from agent personas
- Introduced forced validation rounds through checklists
- Cost-effective structured planning workflow using web platforms
- Self-contained agent personas with external template references

### Known Issues

- Duplicate templates/checklists for web vs IDE versions
- Manual export/import workflow between agents
- Creating each web agent separately was tedious

[View V2 Branch](https://github.com/bmad-code-org/BMAD-METHOD/tree/V2)

## [v1.0.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v1.0.0)

**Initial Release: April 6, 2025**

The original BMAD Method was a tech demo showcasing how different custom agile personas could be used to build out artifacts for planning and executing complex applications from scratch. This initial version established the foundation of the AI-driven agile development approach.

### Key Features

- Introduction of specialized AI agent personas (PM, Architect, Developer, etc.)
- Template-based document generation for planning artifacts
- Emphasis on planning MVP scope with sufficient detail to guide developer agents
- Hard-coded custom mode prompts integrated directly into agent configurations
- The OG of Context Engineering in a structured way

### Limitations

- Limited customization options
- Web usage was complicated and not well-documented
- Rigid scope and purpose with templates coupled to agents
- Not optimized for IDE integration

[View V1 Branch](https://github.com/bmad-code-org/BMAD-METHOD/tree/V1)

## Installation

```bash
npx bmad-method
```

For detailed release notes, see the [GitHub releases page](https://github.com/bmad-code-org/BMAD-METHOD/releases).



---

# FILE: CONTRIBUTING.md

# Contributing to BMad

Thank you for considering contributing! We believe in **Human Amplification, Not Replacement** — bringing out the best thinking in both humans and AI through guided collaboration.

💬 **Discord**: [Join our community](https://discord.gg/gk8jAdXWmj) for real-time discussions, questions, and collaboration.

---

> **Before you write code: talk to us on [Discord](https://discord.gg/gk8jAdXWmj).**
>
> If your change adds features, restructures code, or touches more than a couple of files, **confirm with a maintainer that it fits**. A large PR out of the blue has a high chance of being closed — regardless of effort invested. A five-minute conversation can save you hours.

---

## Our Philosophy

BMad strengthens human-AI collaboration through specialized agents and guided workflows. Every contribution should answer: **"Does this make humans and AI better together?"**

**✅ What we welcome:**
- Enhanced collaboration patterns and workflows
- Improved agent personas and prompts
- Domain-specific modules leveraging BMad Core
- Better planning and context continuity

**❌ What doesn't fit:**
- Purely automated solutions that sideline humans
- Complexity that creates barriers to adoption
- Features that fragment BMad Core's foundation

---

## Reporting Issues

**ALL bug reports and feature requests MUST go through GitHub Issues.**

### Before Creating an Issue

1. **Search existing issues** — Use the GitHub issue search to check if your bug or feature has already been reported
2. **Search closed issues** — Your issue may have been fixed or addressed previously
3. **Check discussions** — Some conversations happen in [GitHub Discussions](https://github.com/bmad-code-org/BMAD-METHOD/discussions)

### Bug Reports

After searching, if the bug is unreported, use the [bug report template](https://github.com/bmad-code-org/BMAD-METHOD/issues/new?template=bug_report.md) and include:

- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (model, IDE, BMad version)
- Screenshots or error messages if applicable

### Feature Requests

After searching, use the [feature request template](https://github.com/bmad-code-org/BMAD-METHOD/issues/new?template=feature_request.md) and explain:

- What the feature is
- Why it would benefit the BMad community
- How it strengthens human-AI collaboration

**For community modules**, review [TRADEMARK.md](TRADEMARK.md) for proper naming conventions (e.g., "My Module (BMad Community Module)").

---

## Before Starting Work

| Work Type               | Requirement                                              |
| ----------------------- | -------------------------------------------------------- |
| Typo / small bug fix    | Just open the PR                                         |
| Feature or large change | Confirm with a maintainer on Discord **before** you start |

---

## Pull Request Guidelines

### Target Branch

Submit PRs to the `main` branch. We use trunk-based development. Every push to `main` auto-publishes to `npm` under the `next` tag. Stable releases are cut ~weekly to the `latest` tag.

### PR Size

- **Ideal**: 200-400 lines of code changes
- **Maximum**: 800 lines (excluding generated files)
- **One feature/fix per PR**

If your change exceeds 800 lines, break it into smaller PRs that can be reviewed independently.

### AI-Generated Code

Given the nature of this project, we expect most contributions involve AI assistance — that's fine. What we require is **heavy human curation**. You must understand every line you're submitting, have made deliberate choices about what to include, and be able to explain your reasoning.

We will reject PRs that read like raw LLM output: bulk refactors nobody asked for, unsolicited "improvements" across many files, or changes where the submitter clearly hasn't read the existing code. Using AI to write code is normal here; using AI as a substitute for thinking is not.

### New to Pull Requests?

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR-USERNAME/bmad-method.git`
3. **Create a branch**: `git checkout -b fix/description` or `git checkout -b feature/description`
4. **Make changes** — keep them focused
5. **Commit**: `git commit -m "fix: correct typo in README"`
6. **Push**: `git push origin fix/description`
7. **Open PR** from your fork on GitHub

### PR Description Template

```markdown
## What
[1-2 sentences describing WHAT changed]

## Why
[1-2 sentences explaining WHY this change is needed]
Fixes #[issue number]

## How
- [2-3 bullets listing HOW you implemented it]
-

## Testing
[1-2 sentences on how you tested this]
```

**Keep it under 200 words.**

### Commit Messages

Use conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation only
- `refactor:` Code change (no bug/feature)
- `test:` Adding tests
- `chore:` Build/tools changes

Keep messages under 72 characters. Each commit = one logical change.

---

## What Makes a Good PR?

| ✅ Do                        | ❌ Don't                      |
| --------------------------- | ---------------------------- |
| Change one thing per PR     | Mix unrelated changes        |
| Clear title and description | Vague or missing explanation |
| Reference related issues    | Reformat entire files        |
| Small, focused commits      | Copy your whole project      |
| Work on a branch            | Work directly on `main`      |

---

## Prompt & Agent Guidelines

- Keep dev agents lean — focus on coding context, not documentation
- Web/planning agents can be larger with complex tasks
- Everything is natural language (markdown) — no code in core framework
- Use BMad modules for domain-specific features
- Validate file references: `npm run validate:refs`

### File-Pattern-to-Validator Mapping

| File Pattern | Validator | Extraction Function |
| ------------ | --------- | ------------------- |
| `*.yaml`, `*.yml` | `validate-file-refs.js` | `extractYamlRefs` |
| `*.md`, `*.xml` | `validate-file-refs.js` | `extractMarkdownRefs` |
| `*.csv` | `validate-file-refs.js` | `extractCsvRefs` |

---

## Need Help?

- 💬 **Discord**: [Join the community](https://discord.gg/gk8jAdXWmj)
- 🐛 **Bugs**: Use the [bug report template](https://github.com/bmad-code-org/BMAD-METHOD/issues/new?template=bug_report.md)
- 💡 **Features**: Use the [feature request template](https://github.com/bmad-code-org/BMAD-METHOD/issues/new?template=feature_request.md)

---

## Code of Conduct

By participating, you agree to abide by our [Code of Conduct](.github/CODE_OF_CONDUCT.md).

## License

By contributing, your contributions are licensed under the same MIT License. See [CONTRIBUTORS.md](CONTRIBUTORS.md) for contributor attribution.



---

# FILE: CONTRIBUTORS.md

# Contributors

BMad Core, BMad Method and BMad and Community BMad Modules are made possible by contributions from our community. We gratefully acknowledge everyone who has helped improve this project.

## How We Credit Contributors

- **Git history** — Every contribution is preserved in the project's commit history
- **Contributors badge** — See the dynamic contributors list on our [README](README.md)
- **GitHub contributors graph** — Visual representation at <https://github.com/bmad-code-org/BMAD-METHOD/graphs/contributors>

## Becoming a Contributor

Anyone who submits a pull request that is merged becomes a contributor. Contributions include:

- Bug fixes
- New features or workflows
- Documentation improvements
- Bug reports and issue triaging
- Code reviews
- Helping others in discussions

There are no minimum contribution requirements — whether it's a one-character typo fix or a major feature, we value all contributions.

## Copyright

The BMad Method project is copyrighted by BMad Code, LLC. Individual contributions are licensed under the same MIT License as the project. Contributors retain authorship credit through Git history and the contributors graph.

---

**Thank you to everyone who has helped make BMad Method better!**

For contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).



---

# FILE: README_CN.md

![BMad Method](banner-bmad-method.png)

[![Version](https://img.shields.io/npm/v/bmad-method?color=blue&label=version)](https://www.npmjs.com/package/bmad-method)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen)](https://nodejs.org)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

**筑梦架构（Build More Architect Dreams）** —— 简称 “BMAD 方法”，面向 BMad 模块生态的 AI 驱动敏捷开发方法。它会随项目复杂度调整工作深度，从日常 bug 修复到企业级系统建设都能适配。

**100% 免费且开源。** 没有付费墙，没有封闭内容，也没有封闭 Discord。我们希望每个人都能平等获得高质量的人机协作开发方法。

## 为什么选择 BMad 方法？

传统 AI 工具常常替你思考，结果往往止于“能用”。BMad 通过专业智能体和引导式工作流，让 AI 成为协作者：流程有结构，决策有依据，产出更稳定。

- **AI 智能引导** —— 随时调用 `bmad-help` 获取下一步建议
- **规模与领域自适应** —— 按项目复杂度自动调整规划深度
- **结构化工作流** —— 覆盖分析、规划、架构、实施全流程
- **专业角色智能体** —— 提供 PM、架构师、开发者、UX 等 12+ 角色
- **派对模式** —— 多个智能体可在同一会话协作讨论
- **完整生命周期** —— 从头脑风暴一路到交付上线

[在 **docs.bmad-method.org** 了解更多](https://docs.bmad-method.org/zh-cn/)

---

## 🚀 BMad 的下一步是什么？

**V6 已经上线，而这只是开始。** BMad 仍在快速演进：跨平台智能体团队与子智能体集成、Skills 架构、BMad Builder v1、Dev Loop 自动化等能力都在持续推进。

**[📍 查看完整路线图 →](https://docs.bmad-method.org/zh-cn/roadmap/)**

---

## 快速开始

**先决条件**：[Node.js](https://nodejs.org) v20+

```bash
npx bmad-method install
```

> 想体验最新预发布版本？可使用 `npx bmad-method@next install`。它比默认版本更新更快，也可能更容易发生变化。

按照安装程序提示操作，然后在项目文件夹中打开你的 AI IDE（Claude Code、Cursor 等）。

**非交互式安装**（用于 CI/CD）：

```bash
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes
```

[查看非交互式安装选项](https://docs.bmad-method.org/zh-cn/how-to/non-interactive-installation/)

> **不确定下一步？** 直接问 `bmad-help`。它会告诉你“必做什么、可选什么”，例如：`bmad-help 我刚完成架构设计，接下来做什么？`

## 模块

BMad 可通过官方模块扩展到不同专业场景。你可以在安装时选择，也可以后续随时补装。

| 模块                                                                                                                | 用途                           |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **[BMad Method (BMM)](https://github.com/bmad-code-org/BMAD-METHOD)**                                             | 核心框架，内含 34+ 工作流         |
| **[BMad Builder (BMB)](https://github.com/bmad-code-org/bmad-builder)**                                           | 创建自定义 BMad 智能体与工作流     |
| **[Test Architect (TEA)](https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise)**             | 基于风险的测试策略与自动化         |
| **[Game Dev Studio (BMGD)](https://github.com/bmad-code-org/bmad-module-game-dev-studio)**                        | 游戏开发工作流（Unity/Unreal/Godot） |
| **[Creative Intelligence Suite (CIS)](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite)** | 创新、头脑风暴、设计思维           |

## 文档

[BMad 方法文档站点](https://docs.bmad-method.org/zh-cn/) — 教程、指南、概念和参考

**快速链接：**
- [入门教程](https://docs.bmad-method.org/zh-cn/tutorials/getting-started/)
- [从旧版本升级](https://docs.bmad-method.org/zh-cn/how-to/upgrade-to-v6/)
- [测试架构师文档（英文）](https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/)

## 社区

- [Discord](https://discord.gg/gk8jAdXWmj) — 获取帮助、分享想法、协作
- [在 YouTube 上订阅](https://www.youtube.com/@BMadCode) — 教程、大师课和播客（2025 年 2 月推出）
- [GitHub Issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) — 错误报告和功能请求
- [讨论](https://github.com/bmad-code-org/BMAD-METHOD/discussions) — 社区对话

## 支持 BMad

BMad 对所有人免费，而且会一直免费。如果你愿意支持项目发展：

- ⭐ 给仓库点个 Star
- ☕ [请我喝咖啡](https://buymeacoffee.com/bmad) — 为开发提供动力
- 🏢 企业赞助 — 在 Discord 上私信
- 🎤 演讲与媒体 — 可参加会议、播客、采访（在 Discord 上联系 BM）

## 贡献

我们欢迎贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解指南。

## 许可证

MIT 许可证 — 详见 [LICENSE](LICENSE)。

---

**BMad** 和 **BMAD-METHOD** 是 BMad Code, LLC 的商标。详见 [TRADEMARK.md](TRADEMARK.md)。

[![Contributors](https://contrib.rocks/image?repo=bmad-code-org/BMAD-METHOD)](https://github.com/bmad-code-org/BMAD-METHOD/graphs/contributors)

请参阅 [CONTRIBUTORS.md](CONTRIBUTORS.md) 了解贡献者信息。



---

# FILE: README_VN.md

![BMad Method](banner-bmad-method.png)

[![Version](https://img.shields.io/npm/v/bmad-method?color=blue&label=version)](https://www.npmjs.com/package/bmad-method)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen)](https://nodejs.org)
[![Python Version](https://img.shields.io/badge/python-%3E%3D3.10-blue?logo=python&logoColor=white)](https://www.python.org)
[![uv](https://img.shields.io/badge/uv-package%20manager-blueviolet?logo=uv)](https://docs.astral.sh/uv/)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

[English](README.md) | [简体中文](README_CN.md) | Tiếng Việt

**Build More Architect Dreams** - một mô-đun khung phát triển hướng AI trong hệ sinh thái BMad, có khả năng thích ứng theo quy mô từ sửa lỗi nhỏ đến các hệ thống doanh nghiệp.

**100% miễn phí và mã nguồn mở.** Không có tường phí. Không có nội dung bị khóa. Không có Discord giới hạn quyền truy cập. Chúng tôi tin vào việc trao quyền cho mọi người, không chỉ cho những ai có thể trả tiền để vào một cộng đồng hay khóa học khép kín.

## Vì sao chọn BMad Method?

Các công cụ AI truyền thống thường làm thay phần suy nghĩ của bạn và tạo ra kết quả ở mức trung bình. Các agent chuyên biệt và quy trình làm việc có hướng dẫn của BMad hoạt động như những cộng tác viên chuyên gia, dẫn dắt bạn qua một quy trình có cấu trúc để khai mở tư duy tốt nhất của bạn cùng với AI.

- **Trợ giúp AI thông minh** - Gọi skill `bmad-help` bất kỳ lúc nào để biết bước tiếp theo
- **Thích ứng theo quy mô và miền bài toán** - Tự động điều chỉnh độ sâu lập kế hoạch theo độ phức tạp của dự án
- **Quy trình có cấu trúc** - Dựa trên các thực hành tốt nhất của agile xuyên suốt phân tích, lập kế hoạch, kiến trúc và triển khai
- **Agent chuyên biệt** - Hơn 12 chuyên gia theo vai trò như PM, Architect, Developer, UX, Scrum Master và nhiều vai trò khác
- **Party Mode** - Đưa nhiều persona agent vào cùng một phiên để cộng tác và thảo luận
- **Vòng đời hoàn chỉnh** - Từ động não ý tưởng cho đến triển khai

[Tìm hiểu thêm tại **docs.bmad-method.org**](https://docs.bmad-method.org/vi-vn/)

---

## 🚀 Điều gì tiếp theo cho BMad?

**V6 đã có mặt và đây mới chỉ là khởi đầu!** BMad Method đang phát triển rất nhanh với các cải tiến như đội agent đa nền tảng và tích hợp sub-agent, kiến trúc Skills, BMad Builder v1, tự động hóa vòng lặp phát triển và nhiều thứ khác vẫn đang được xây dựng.

**[📍 Xem lộ trình đầy đủ →](https://docs.bmad-method.org/vi-vn/roadmap/)**

---

## Bắt đầu nhanh

**Điều kiện tiên quyết**: [Node.js](https://nodejs.org) v20+ · [Python](https://www.python.org) 3.10+ · [uv](https://docs.astral.sh/uv/)

```bash
npx bmad-method install
```

> Muốn dùng bản prerelease mới nhất? Hãy dùng `npx bmad-method@next install`. Hãy kỳ vọng mức độ biến động cao hơn bản cài đặt mặc định.

Làm theo các lời nhắc của trình cài đặt, sau đó mở AI IDE của bạn như Claude Code hoặc Cursor trong thư mục dự án.

**Cài đặt không tương tác** (cho CI/CD):

```bash
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes
```

[Xem toàn bộ tùy chọn cài đặt](https://docs.bmad-method.org/vi-vn/how-to/non-interactive-installation/)

> **Chưa chắc nên làm gì?** Hãy hỏi `bmad-help` - nó sẽ cho bạn biết chính xác bước nào tiếp theo và bước nào là tùy chọn. Bạn cũng có thể hỏi kiểu như `bmad-help Tôi vừa hoàn thành phần kiến trúc, tiếp theo tôi cần làm gì?`

## Mô-đun

BMad Method có thể được mở rộng bằng các mô-đun chính thức cho những miền chuyên biệt. Chúng có sẵn trong lúc cài đặt hoặc bất kỳ lúc nào sau đó.

| Module                                                                                                            | Mục đích                                           |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **[BMad Method (BMM)](https://github.com/bmad-code-org/BMAD-METHOD)**                                             | Khung lõi với hơn 34 quy trình                     |
| **[BMad Builder (BMB)](https://github.com/bmad-code-org/bmad-builder)**                                           | Tạo agent và quy trình BMad tùy chỉnh             |
| **[Test Architect (TEA)](https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise)**             | Chiến lược kiểm thử và tự động hóa dựa trên rủi ro |
| **[Game Dev Studio (BMGD)](https://github.com/bmad-code-org/bmad-module-game-dev-studio)**                        | Quy trình phát triển game (Unity, Unreal, Godot)   |
| **[Creative Intelligence Suite (CIS)](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite)** | Đổi mới, động não ý tưởng, tư duy thiết kế         |

## Tài liệu

[Trang tài liệu BMad Method](https://docs.bmad-method.org/vi-vn/) - bài hướng dẫn, hướng dẫn tác vụ, giải thích khái niệm và tài liệu tham chiếu

**Liên kết nhanh:**
- [Hướng dẫn bắt đầu](https://docs.bmad-method.org/vi-vn/tutorials/getting-started/)
- [Nâng cấp từ các phiên bản trước](https://docs.bmad-method.org/vi-vn/how-to/upgrade-to-v6/)
- [Tài liệu Test Architect](https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/)

## Cộng đồng

- [Discord](https://discord.gg/gk8jAdXWmj) - Nhận trợ giúp, chia sẻ ý tưởng, cộng tác
- [YouTube](https://youtube.com/@BMadCode) - Video hướng dẫn, master class và nhiều nội dung khác
- [X / Twitter](https://x.com/BMadCode)
- [Website](https://bmadcode.com)
- [GitHub Issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) - Báo lỗi và yêu cầu tính năng
- [Discussions](https://github.com/bmad-code-org/BMAD-METHOD/discussions) - Trao đổi cộng đồng

## Hỗ trợ BMad

BMad miễn phí cho tất cả mọi người và sẽ luôn như vậy. Hãy nhấn sao cho repo này, [mời tôi một ly cà phê](https://buymeacoffee.com/bmad), hoặc gửi email tới <contact@bmadcode.com> nếu bạn muốn tài trợ doanh nghiệp.

## Đóng góp

Chúng tôi luôn chào đón đóng góp. Xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết hướng dẫn.

## Giấy phép

Giấy phép MIT - xem [LICENSE](LICENSE) để biết chi tiết.

---

**BMad** và **BMAD-METHOD** là các nhãn hiệu của BMad Code, LLC. Xem [TRADEMARK.md](TRADEMARK.md) để biết chi tiết.

[![Contributors](https://contrib.rocks/image?repo=bmad-code-org/BMAD-METHOD)](https://github.com/bmad-code-org/BMAD-METHOD/graphs/contributors)

Xem [CONTRIBUTORS.md](CONTRIBUTORS.md) để biết thông tin về những người đóng góp.


---

# FILE: SECURITY.md

# Security Policy

## Supported Versions

We release security patches for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| < Latest | :x:               |

We recommend always using the latest version of BMad Method to ensure you have the most recent security updates.

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security issue, please report it responsibly.

### How to Report

**Do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of these methods:

1. **GitHub Security Advisories** (Preferred): Use [GitHub's private vulnerability reporting](https://github.com/bmad-code-org/BMAD-METHOD/security/advisories/new) to submit a confidential report.

2. **Discord**: Contact a maintainer directly via DM on our [Discord server](https://discord.gg/gk8jAdXWmj).

### What to Include

Please include as much of the following information as possible:

- Type of vulnerability (e.g., prompt injection, path traversal, etc.)
- Full paths of source file(s) related to the vulnerability
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if available)
- Impact assessment of the vulnerability

### Response Timeline

- **Initial Response**: Within 48 hours of receiving your report
- **Status Update**: Within 7 days with our assessment
- **Resolution Target**: Critical issues within 30 days; other issues within 90 days

### What to Expect

1. We will acknowledge receipt of your report
2. We will investigate and validate the vulnerability
3. We will work on a fix and coordinate disclosure timing with you
4. We will credit you in the security advisory (unless you prefer to remain anonymous)

## Security Scope

### In Scope

- Vulnerabilities in BMad Method core framework code
- Security issues in agent definitions or workflows that could lead to unintended behavior
- Path traversal or file system access issues
- Prompt injection vulnerabilities that bypass intended agent behavior
- Supply chain vulnerabilities in dependencies

### Out of Scope

- Security issues in user-created custom agents or modules
- Vulnerabilities in third-party AI providers (Claude, GPT, etc.)
- Issues that require physical access to a user's machine
- Social engineering attacks
- Denial of service attacks that don't exploit a specific vulnerability

## Security Best Practices for Users

When using BMad Method:

1. **Review Agent Outputs**: Always review AI-generated code before executing it
2. **Limit File Access**: Configure your AI IDE to limit file system access where possible
3. **Keep Updated**: Regularly update to the latest version
4. **Validate Dependencies**: Review any dependencies added by generated code
5. **Environment Isolation**: Consider running AI-assisted development in isolated environments

## Acknowledgments

We appreciate the security research community's efforts in helping keep BMad Method secure. Contributors who report valid security issues will be acknowledged in our security advisories.

---

Thank you for helping keep BMad Method and our community safe.



---

# FILE: TRADEMARK.md

# Trademark Notice & Guidelines

## Trademark Ownership

The following names and logos are trademarks of BMad Code, LLC:

- **BMad** (word mark, all casings: BMad, bmad, BMAD)
- **BMad Method** (word mark, includes BMadMethod, BMAD-METHOD, and all variations)
- **BMad Core** (word mark, includes BMadCore, BMAD-CORE, and all variations)
- **BMad Code** (word mark)
- BMad Method logo and visual branding
- The "Build More, Architect Dreams" tagline

**All casings, stylings, and variations** of the above names (with or without hyphens, spaces, or specific capitalization) are covered by these trademarks.

These trademarks are protected under trademark law and are **not** licensed under the MIT License. The MIT License applies to the software code only, not to the BMad brand identity.

## What This Means

You may:

- Use the BMad software under the terms of the MIT License
- Refer to BMad to accurately describe compatibility or integration (e.g., "Compatible with BMad Method v6")
- Link to <https://github.com/bmad-code-org/BMAD-METHOD>
- Fork the software and distribute your own version under a different name

You may **not**:

- Use "BMad" or any confusingly similar variation as your product name, service name, company name, or domain name
- Present your product as officially endorsed, approved, or certified by BMad Code, LLC when it is not, without written consent from an authorized representative of BMad Code, LLC
- Use BMad logos or branding in a way that suggests your product is an official or endorsed BMad product
- Register domain names, social media handles, or trademarks that incorporate BMad branding

## Examples

| Permitted                                              | Not Permitted                                |
| ------------------------------------------------------ | -------------------------------------------- |
| "My workflow tool, compatible with BMad Method"        | "BMadFlow" or "BMad Studio"                  |
| "An alternative implementation inspired by BMad"       | "BMad Pro" or "BMad Enterprise"              |
| "My Awesome Healthcare Module (Bmad Community Module)" | "The Official BMad Core Healthcare Module"   |
| Accurately stating you use BMad as a dependency        | Implying official endorsement or partnership |

## Commercial Use

You may sell products that incorporate or work with BMad software. However:

- Your product must have its own distinct name and branding
- You must not use BMad trademarks in your marketing, domain names, or product identity
- You may truthfully describe technical compatibility (e.g., "Works with BMad Method")

## Questions?

If you have questions about trademark usage or would like to discuss official partnership or endorsement opportunities, please reach out:

- **Email**: <contact@bmadcode.com>



---

# FILE: docs/404.md

---
title: Page Not Found
template: splash
---


The page you're looking for doesn't exist or has been moved.

[Return to Home](./index.md)



---

# FILE: docs/_STYLE_GUIDE.md

---
title: "Documentation Style Guide"
description: Project-specific documentation conventions based on Google style and Diataxis structure
---

This project adheres to the [Google Developer Documentation Style Guide](https://developers.google.com/style) and uses [Diataxis](https://diataxis.fr/) to structure content. Only project-specific conventions follow.

## Project-Specific Rules

| Rule                             | Specification                            |
| -------------------------------- | ---------------------------------------- |
| No horizontal rules (`---`)      | Fragments reading flow                   |
| No `####` headers                | Use bold text or admonitions instead     |
| No "Related" or "Next:" sections | Sidebar handles navigation               |
| No deeply nested lists           | Break into sections instead              |
| No code blocks for non-code      | Use admonitions for dialogue examples    |
| No bold paragraphs for callouts  | Use admonitions instead                  |
| 1-2 admonitions per section max  | Tutorials allow 3-4 per major section    |
| Table cells / list items         | 1-2 sentences max                        |
| Header budget                    | 8-12 `##` per doc; 2-3 `###` per section |

## Admonitions (Starlight Syntax)

```md
:::tip[Title]
Shortcuts, best practices
:::

:::note[Title]
Context, definitions, examples, prerequisites
:::

:::caution[Title]
Caveats, potential issues
:::

:::danger[Title]
Critical warnings only — data loss, security issues
:::
```

### Standard Uses

| Admonition               | Use For                       |
| ------------------------ | ----------------------------- |
| `:::note[Prerequisites]` | Dependencies before starting  |
| `:::tip[Quick Path]`     | TL;DR summary at document top |
| `:::caution[Important]`  | Critical caveats              |
| `:::note[Example]`       | Command/response examples     |

## Standard Table Formats

**Phases:**

```md
| Phase | Name     | What Happens                                 |
| ----- | -------- | -------------------------------------------- |
| 1     | Analysis | Brainstorm, research *(optional)*            |
| 2     | Planning | Requirements — PRD or spec *(required)* |
```

**Skills:**

```md
| Skill        | Agent   | Purpose                              |
| ------------ | ------- | ------------------------------------ |
| `bmad-brainstorming` | Analyst | Brainstorm a new project             |
| `bmad-create-prd`        | PM      | Create Product Requirements Document |
```

## Folder Structure Blocks

Show in "What You've Accomplished" sections:

````md
```
your-project/
├── _bmad/                                   # BMad configuration
├── _bmad-output/
│   ├── planning-artifacts/
│   │   └── PRD.md                           # Your requirements document
│   ├── implementation-artifacts/
│   └── project-context.md                   # Implementation rules (optional)
└── ...
```
````

## Tutorial Structure

```text
1. Title + Hook (1-2 sentences describing outcome)
2. Version/Module Notice (info or warning admonition) (optional)
3. What You'll Learn (bullet list of outcomes)
4. Prerequisites (info admonition)
5. Quick Path (tip admonition - TL;DR summary)
6. Understanding [Topic] (context before steps - tables for phases/agents)
7. Installation (optional)
8. Step 1: [First Major Task]
9. Step 2: [Second Major Task]
10. Step 3: [Third Major Task]
11. What You've Accomplished (summary + folder structure)
12. Quick Reference (skills table)
13. Common Questions (FAQ format)
14. Getting Help (community links)
15. Key Takeaways (tip admonition)
```

### Tutorial Checklist

- [ ] Hook describes outcome in 1-2 sentences
- [ ] "What You'll Learn" section present
- [ ] Prerequisites in admonition
- [ ] Quick Path TL;DR admonition at top
- [ ] Tables for phases, skills, agents
- [ ] "What You've Accomplished" section present
- [ ] Quick Reference table present
- [ ] Common Questions section present
- [ ] Getting Help section present
- [ ] Key Takeaways admonition at end

## How-To Structure

```text
1. Title + Hook (one sentence: "Use the `X` workflow to...")
2. When to Use This (bullet list of scenarios)
3. When to Skip This (optional)
4. Prerequisites (note admonition)
5. Steps (numbered ### subsections)
6. What You Get (output/artifacts produced)
7. Example (optional)
8. Tips (optional)
9. Next Steps (optional)
```

### How-To Checklist

- [ ] Hook starts with "Use the `X` workflow to..."
- [ ] "When to Use This" has 3-5 bullet points
- [ ] Prerequisites listed
- [ ] Steps are numbered `###` subsections with action verbs
- [ ] "What You Get" describes output artifacts

## Explanation Structure

### Types

| Type              | Example                       |
| ----------------- | ----------------------------- |
| **Index/Landing** | `core-concepts/index.md`      |
| **Concept**       | `what-are-agents.md`          |
| **Feature**       | `quick-dev.md`                |
| **Philosophy**    | `why-solutioning-matters.md`  |
| **FAQ**           | `established-projects-faq.md` |

### General Template

```text
1. Title + Hook (1-2 sentences)
2. Overview/Definition (what it is, why it matters)
3. Key Concepts (### subsections)
4. Comparison Table (optional)
5. When to Use / When Not to Use (optional)
6. Diagram (optional - mermaid, 1 per doc max)
7. Next Steps (optional)
```

### Index/Landing Pages

```text
1. Title + Hook (one sentence)
2. Content Table (links with descriptions)
3. Getting Started (numbered list)
4. Choose Your Path (optional - decision tree)
```

### Concept Explainers

```text
1. Title + Hook (what it is)
2. Types/Categories (### subsections) (optional)
3. Key Differences Table
4. Components/Parts
5. Which Should You Use?
6. Creating/Customizing (pointer to how-to guides)
```

### Feature Explainers

```text
1. Title + Hook (what it does)
2. Quick Facts (optional - "Perfect for:", "Time to:")
3. When to Use / When Not to Use
4. How It Works (mermaid diagram optional)
5. Key Benefits
6. Comparison Table (optional)
7. When to Graduate/Upgrade (optional)
```

### Philosophy/Rationale Documents

```text
1. Title + Hook (the principle)
2. The Problem
3. The Solution
4. Key Principles (### subsections)
5. Benefits
6. When This Applies
```

### Explanation Checklist

- [ ] Hook states what document explains
- [ ] Content in scannable `##` sections
- [ ] Comparison tables for 3+ options
- [ ] Diagrams have clear labels
- [ ] Links to how-to guides for procedural questions
- [ ] 2-3 admonitions max per document

## Reference Structure

### Types

| Type              | Example               |
| ----------------- | --------------------- |
| **Index/Landing** | `workflows/index.md`  |
| **Catalog**       | `agents/index.md`     |
| **Deep-Dive**     | `document-project.md` |
| **Configuration** | `core-tasks.md`       |
| **Glossary**      | `glossary/index.md`   |
| **Comprehensive** | `bmgd-workflows.md`   |

### Reference Index Pages

```text
1. Title + Hook (one sentence)
2. Content Sections (## for each category)
   - Bullet list with links and descriptions
```

### Catalog Reference

```text
1. Title + Hook
2. Items (## for each item)
   - Brief description (one sentence)
   - **Skills:** or **Key Info:** as flat list
3. Universal/Shared (## section) (optional)
```

### Item Deep-Dive Reference

```text
1. Title + Hook (one sentence purpose)
2. Quick Facts (optional note admonition)
   - Module, Skill, Input, Output as list
3. Purpose/Overview (## section)
4. How to Invoke (code block)
5. Key Sections (## for each aspect)
   - Use ### for sub-options
6. Notes/Caveats (tip or caution admonition)
```

### Configuration Reference

```text
1. Title + Hook
2. Table of Contents (jump links if 4+ items)
3. Items (## for each config/task)
   - **Bold summary** — one sentence
   - **Use it when:** bullet list
   - **How it works:** numbered steps (3-5 max)
   - **Output:** expected result (optional)
```

### Comprehensive Reference Guide

```text
1. Title + Hook
2. Overview (## section)
   - Diagram or table showing organization
3. Major Sections (## for each phase/category)
   - Items (### for each item)
   - Standardized fields: Skill, Agent, Input, Output, Description
4. Next Steps (optional)
```

### Reference Checklist

- [ ] Hook states what document references
- [ ] Structure matches reference type
- [ ] Items use consistent structure throughout
- [ ] Tables for structured/comparative data
- [ ] Links to explanation docs for conceptual depth
- [ ] 1-2 admonitions max

## Glossary Structure

Starlight generates right-side "On this page" navigation from headers:

- Categories as `##` headers — appear in right nav
- Terms in tables — compact rows, not individual headers
- No inline TOC — right sidebar handles navigation

### Table Format

```md
## Category Name

| Term         | Definition                                                                               |
| ------------ | ---------------------------------------------------------------------------------------- |
| **Agent**    | Specialized AI persona with specific expertise that guides users through workflows.      |
| **Workflow** | Multi-step guided process that orchestrates AI agent activities to produce deliverables. |
```

### Definition Rules

| Do                            | Don't                                       |
| ----------------------------- | ------------------------------------------- |
| Start with what it IS or DOES | Start with "This is..." or "A [term] is..." |
| Keep to 1-2 sentences         | Write multi-paragraph explanations          |
| Bold term name in cell        | Use plain text for terms                    |

### Context Markers

Add italic context at definition start for limited-scope terms:

- `*Quick Flow only.*`
- `*BMad Method/Enterprise.*`
- `*Phase N.*`
- `*BMGD.*`
- `*Established projects.*`

### Glossary Checklist

- [ ] Terms in tables, not individual headers
- [ ] Terms alphabetized within categories
- [ ] Definitions 1-2 sentences
- [ ] Context markers italicized
- [ ] Term names bolded in cells
- [ ] No "A [term] is..." definitions

## FAQ Sections

```md
## Questions

- [Do I always need architecture?](#do-i-always-need-architecture)
- [Can I change my plan later?](#can-i-change-my-plan-later)

### Do I always need architecture?

Only for BMad Method and Enterprise tracks. Quick Flow skips to implementation.

### Can I change my plan later?

Yes. The `bmad-correct-course` workflow handles scope changes mid-implementation.

**Have a question not answered here?** [Open an issue](...) or ask in [Discord](...).
```

## Validation Commands

Before submitting documentation changes:

```bash
npm run docs:fix-links            # Preview link format fixes
npm run docs:fix-links -- --write # Apply fixes
npm run docs:validate-links       # Check links exist
npm run docs:build                # Verify no build errors
```



---

# FILE: docs/cs/404.md

---
title: Stránka nenalezena
template: splash
---

Stránka, kterou hledáte, neexistuje nebo byla přesunuta.

[Zpět na úvodní stránku](/cs/index.md)



---

# FILE: docs/cs/_STYLE_GUIDE.md

---
title: "Průvodce stylem dokumentace"
description: Projektově specifické konvence dokumentace založené na stylu Google a struktuře Diataxis
---

Tento projekt se řídí [Google Developer Documentation Style Guide](https://developers.google.com/style) a používá [Diataxis](https://diataxis.fr/) pro strukturování obsahu. Následují pouze projektově specifické konvence.

## Projektově specifická pravidla

| Pravidlo                               | Specifikace                              |
| -------------------------------------- | ---------------------------------------- |
| Žádné horizontální čáry (`---`)        | Narušují plynulost čtení                 |
| Žádné nadpisy `####`                   | Místo toho použijte tučný text nebo admonitions |
| Žádné sekce „Souvisejí“ nebo „Další:“ | Navigaci zajišťuje postranní panel       |
| Žádné hluboce vnořené seznamy          | Místo toho rozdělejte do sekcí           |
| Žádné bloky kódu pro nekód             | Pro příklady dialogů použijte admonitions |
| Žádné tučné odstavce pro upozornění    | Místo toho použijte admonitions          |
| Max 1–2 admonitions na sekci           | Tutoriály povolují 3–4 na hlavní sekci   |
| Buňky tabulek / položky seznamů        | Max 1–2 věty                             |
| Rozpočet nadpisů                       | 8–12 `##` na dokument; 2–3 `###` na sekci |

## Admonitions (syntaxe Starlight)

```md
:::tip[Název]
Zkratky, osvědčené postupy
:::

:::note[Název]
Kontext, definice, příklady, předpoklady
:::

:::caution[Název]
Upozornění, potenciální problémy
:::

:::danger[Název]
Pouze kritická varování — ztráta dat, bezpečnostní problémy
:::
```

### Standardní použití

| Admonition               | Použití pro                   |
| ------------------------ | ----------------------------- |
| `:::note[Předpoklady]`  | Závislosti před začátkem      |
| `:::tip[Rychlá cesta]`  | TL;DR shrnutí na začátku dokumentu |
| `:::caution[Důležité]`  | Kritická upozornění           |
| `:::note[Příklad]`      | Příklady příkazů/odpovědí     |

## Standardní formáty tabulek

**Fáze:**

```md
| Fáze | Název    | Co se děje                                   |
| ---- | -------- | -------------------------------------------- |
| 1    | Analýza  | Brainstorming, průzkum *(volitelné)*         |
| 2    | Plánování | Požadavky — PRD nebo specifikace *(povinné)* |
```

**Skills:**

```md
| Skill                | Agent   | Účel                                 |
| -------------------- | ------- | ------------------------------------ |
| `bmad-brainstorming` | Analytik | Brainstorming nového projektu       |
| `bmad-create-prd`    | PM      | Vytvoření dokumentu požadavků (PRD) |
```

## Bloky struktury složek

Zobrazujte v sekcích „Co jste dosáhli“:

````md
```
váš-projekt/
├── _bmad/                                   # Konfigurace BMad
├── _bmad-output/
│   ├── planning-artifacts/
│   │   └── PRD.md                           # Váš dokument požadavků
│   ├── implementation-artifacts/
│   └── project-context.md                   # Pravidla implementace (volitelné)
└── ...
```
````

## Struktura tutoriálu

```text
1. Název + Háček (1–2 věty popisující výsledek)
2. Upozornění na verzi/modul (info nebo warning admonition) (volitelné)
3. Co se naučíte (odrážkový seznam výsledků)
4. Předpoklady (info admonition)
5. Rychlá cesta (tip admonition – TL;DR shrnutí)
6. Pochopení [Tématu] (kontext před kroky – tabulky pro fáze/agenty)
7. Instalace (volitelné)
8. Krok 1: [První hlavní úkol]
9. Krok 2: [Druhý hlavní úkol]
10. Krok 3: [Třetí hlavní úkol]
11. Co jste dosáhli (shrnutí + struktura složek)
12. Rychlý přehled (tabulka skills)
13. Časté otázky (formát FAQ)
14. Získání pomoci (komunitní odkazy)
15. Klíčové poznatky (tip admonition)
```

### Kontrolní seznam tutoriálu

- [ ] Háček popisuje výsledek v 1–2 větách
- [ ] Sekce „Co se naučíte“ je přítomna
- [ ] Předpoklady v admonition
- [ ] Rychlá cesta TL;DR admonition nahoře
- [ ] Tabulky pro fáze, skills, agenty
- [ ] Sekce „Co jste dosáhli“ je přítomna
- [ ] Tabulka rychlého přehledu je přítomna
- [ ] Sekce častých otázek je přítomna
- [ ] Sekce získání pomoci je přítomna
- [ ] Klíčové poznatky admonition na konci

## Struktura praktického návodu

```text
1. Název + Háček (jedna věta: „Použijte workflow `X` k...“)
2. Kdy to použít (odrážkový seznam scénářů)
3. Kdy to přeskočit (volitelné)
4. Předpoklady (note admonition)
5. Kroky (číslované ### podsekce)
6. Co získáte (výstup/vytvořené artefakty)
7. Příklad (volitelné)
8. Tipy (volitelné)
9. Další kroky (volitelné)
```

### Kontrolní seznam praktického návodu

- [ ] Háček začíná „Použijte workflow `X` k...“
- [ ] „Kdy to použít“ má 3–5 odrážek
- [ ] Předpoklady jsou uvedeny
- [ ] Kroky jsou číslované `###` podsekce s akčními slovesy
- [ ] „Co získáte“ popisuje výstupní artefakty

## Struktura vysvětlení

### Typy

| Typ               | Příklad                       |
| ----------------- | ----------------------------- |
| **Úvodní stránka** | `core-concepts/index.md`     |
| **Koncept**       | `what-are-agents.md`          |
| **Funkce**        | `quick-dev.md`                |
| **Filosofie**     | `why-solutioning-matters.md`  |
| **FAQ**           | `established-projects-faq.md` |

### Obecná šablona

```text
1. Název + Háček (1–2 věty)
2. Přehled/Definice (co to je, proč je to důležité)
3. Klíčové koncepty (### podsekce)
4. Srovnávací tabulka (volitelné)
5. Kdy použít / Kdy nepoužít (volitelné)
6. Diagram (volitelné – mermaid, max 1 na dokument)
7. Další kroky (volitelné)
```

### Úvodní/Vstupní stránky

```text
1. Název + Háček (jedna věta)
2. Tabulka obsahu (odkazy s popisy)
3. Jak začít (číslovaný seznam)
4. Vyberte si svou cestu (volitelné – rozhodovací strom)
```

### Vysvětlení konceptů

```text
1. Název + Háček (co to je)
2. Typy/Kategorie (### podsekce) (volitelné)
3. Tabulka klíčových rozdílů
4. Komponenty/Části
5. Co byste měli použít?
6. Vytváření/Přizpůsobení (odkaz na praktické návody)
```

### Vysvětlení funkcí

```text
1. Název + Háček (co to dělá)
2. Rychlá fakta (volitelné – „Ideální pro:“, „Čas:“)
3. Kdy použít / Kdy nepoužít
4. Jak to funguje (mermaid diagram volitelné)
5. Klíčové výhody
6. Srovnávací tabulka (volitelné)
7. Kdy přejít na vyšší úroveň (volitelné)
```

### Dokumenty filosofie/zdůvodnění

```text
1. Název + Háček (princip)
2. Problém
3. Řešení
4. Klíčové principy (### podsekce)
5. Výhody
6. Kdy to platí
```

### Kontrolní seznam vysvětlení

- [ ] Háček uvádí, co dokument vysvětluje
- [ ] Obsah v přehledných `##` sekcích
- [ ] Srovnávací tabulky pro 3+ možností
- [ ] Diagramy mají jasné popisky
- [ ] Odkazy na praktické návody pro procedurální otázky
- [ ] Max 2–3 admonitions na dokument

## Struktura reference

### Typy

| Typ               | Příklad               |
| ----------------- | --------------------- |
| **Úvodní stránka** | `workflows/index.md` |
| **Katalog**       | `agents/index.md`     |
| **Hloubkový pohled** | `document-project.md` |
| **Konfigurace**   | `core-tasks.md`       |
| **Slovníček**     | `glossary/index.md`   |
| **Komplexní**     | `bmgd-workflows.md`   |

### Úvodní stránky reference

```text
1. Název + Háček (jedna věta)
2. Sekce obsahu (## pro každou kategorii)
   - Odrážkový seznam s odkazy a popisy
```

### Katalogová reference

```text
1. Název + Háček
2. Položky (## pro každou položku)
   - Stručný popis (jedna věta)
   - **Skills:** nebo **Klíčové info:** jako plochý seznam
3. Univerzální/Sdílené (## sekce) (volitelné)
```

### Hloubková reference položky

```text
1. Název + Háček (jedna věta účel)
2. Rychlá fakta (volitelné note admonition)
   - Modul, Skill, Vstup, Výstup jako seznam
3. Účel/Přehled (## sekce)
4. Jak vyvolat (blok kódu)
5. Klíčové sekce (## pro každý aspekt)
   - Použijte ### pro pod-možnosti
6. Poznámky/Upozornění (tip nebo caution admonition)
```

### Konfigurační reference

```text
1. Název + Háček
2. Obsah (odkazy pro skok, pokud 4+ položek)
3. Položky (## pro každou konfiguraci/úkol)
   - **Tučné shrnutí** — jedna věta
   - **Použijte když:** odrážkový seznam
   - **Jak to funguje:** číslované kroky (max 3–5)
   - **Výstup:** očekávaný výsledek (volitelné)
```

### Komplexní referenční průvodce

```text
1. Název + Háček
2. Přehled (## sekce)
   - Diagram nebo tabulka zobrazující organizaci
3. Hlavní sekce (## pro každou fázi/kategorii)
   - Položky (### pro každou položku)
   - Standardizovaná pole: Skill, Agent, Vstup, Výstup, Popis
4. Další kroky (volitelné)
```

### Kontrolní seznam reference

- [ ] Háček uvádí, co dokument referuje
- [ ] Struktura odpovídá typu reference
- [ ] Položky používají konzistentní strukturu
- [ ] Tabulky pro strukturovaná/srovnávací data
- [ ] Odkazy na dokumenty vysvětlení pro koncepční hloubku
- [ ] Max 1–2 admonitions

## Struktura slovníčku

Starlight generuje navigaci „Na této stránce“ z nadpisů na pravé straně:

- Kategorie jako `##` nadpisy — zobrazují se v pravé navigaci
- Termíny v tabulkách — kompaktní řádky, ne jednotlivé nadpisy
- Žádný inline TOC — pravý panel zajišťuje navigaci

### Formát tabulky

```md
## Název kategorie

| Termín       | Definice                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------- |
| **Agent**    | Specializovaná AI persona s konkrétní odborností, která provází uživatele pracovními postupy. |
| **Workflow** | Vícekrokový řízený proces, který orchestruje aktivity AI agentů k vytvoření výstupů.        |
```

### Pravidla definic

| Správně                        | Špatně                                       |
| ------------------------------ | -------------------------------------------- |
| Začněte tím, co to JE nebo DĚLÁ | Nezačínejte „Toto je...“ nebo „[Termín] je...“ |
| Držte se 1–2 vět              | Nepište víceodstavcová vysvětlení            |
| Tučný název termínu v buňce   | Nepoužívejte prostý text pro termíny         |

### Kontextové značky

Přidejte kurzívní kontext na začátek definice pro termíny s omezeným rozsahem:

- `*Pouze Quick Flow.*`
- `*BMad Method/Enterprise.*`
- `*Fáze N.*`
- `*BMGD.*`
- `*Existující projekty.*`

### Kontrolní seznam slovníčku

- [ ] Termíny v tabulkách, ne jako jednotlivé nadpisy
- [ ] Termíny abecedně seřazeny v kategoriích
- [ ] Definice 1–2 věty
- [ ] Kontextové značky kurzívou
- [ ] Názvy termínů tučně v buňkách
- [ ] Žádné definice „[Termín] je...“

## Sekce FAQ

```md
## Otázky

- [Potřebuji vždy architekturu?](#potřebuji-vždy-architekturu)
- [Mohu později změnit svůj plán?](#mohu-později-změnit-svůj-plán)

### Potřebuji vždy architekturu?

Pouze pro BMad Method a Enterprise. Quick Flow přeskakuje rovnou k implementaci.

### Mohu později změnit svůj plán?

Ano. SM agent má workflow `bmad-correct-course` pro řešení změn rozsahu.

**Máte otázku, na kterou jste zde nenašli odpověď?** [Vytvořte issue](...) nebo se zeptejte na [Discordu](...).
```

## Validační příkazy

Před odesláním změn dokumentace:

```bash
npm run docs:fix-links            # Náhled oprav formátu odkazů
npm run docs:fix-links -- --write # Aplikovat opravy
npm run docs:validate-links       # Kontrola existence odkazů
npm run docs:build                # Ověření bez chyb při sestavení
```



---

# FILE: docs/cs/explanation/advanced-elicitation.md

---
title: "Pokročilá elicitace"
description: Přimějte LLM přehodnotit svou práci pomocí strukturovaných metod uvažování
sidebar:
  order: 6
---

Přimějte LLM přehodnotit, co právě vygeneroval. Vyberete metodu uvažování, LLM ji aplikuje na svůj vlastní výstup, a vy rozhodnete, zda si vylepšení ponecháte.

## Co je pokročilá elicitace?

Strukturovaný druhý průchod. Místo žádání AI, aby „to zkusila znovu“ nebo „to zlepšila“, vyberete specifickou metodu uvažování a AI přezkoumá svůj vlastní výstup přes tento objektiv.

Rozdíl je podstatný. Vágní požadavky produkují vágní revize. Pojmenovaná metoda vynucuje konkrétní úhel útoku, odhaluje postřehy, které by generický pokus přehlédl.

## Kdy ji použít

- Poté, co workflow vygeneruje obsah a chcete alternativy
- Když výstup vypadá v pořádku, ale tušíte, že je v něm víc hloubky
- K zátěžovému testování předpokladů nebo nalezení slabých míst
- Pro důležitý obsah, kde přehodnocení pomáhá

Workflow nabízejí pokročilou elicitaci v rozhodovacích bodech — poté, co LLM něco vygeneruje, budete dotázáni, zda ji chcete spustit.

## Jak to funguje

1. LLM navrhne 5 relevantních metod pro váš obsah
2. Vyberete jednu (nebo zamícháte pro jiné možnosti)
3. Metoda je aplikována, vylepšení zobrazena
4. Přijměte nebo zahoďte, opakujte nebo pokračujte

## Vestavěné metody

K dispozici jsou desítky metod uvažování. Několik příkladů:

- **Pre-mortem analýza** — Předpokládejte, že projekt už selhal, a zpětně hledejte proč
- **Myšlení z prvních principů** — Odstraňte předpoklady, znovu postavte od základní pravdy
- **Inverze** — Zeptejte se, jak zaručit selhání, a poté se tomu vyhněte
- **Red Team vs Blue Team** — Napadněte vlastní práci, pak ji braňte
- **Sokratovské dotazování** — Zpochybněte každé tvrzení otázkou „proč?“ a „jak víte?“
- **Odstranění omezení** — Odstraňte všechna omezení, podívejte se, co se změní, selektivně je přidejte zpět
- **Mapování zainteresovaných stran** — Přehodnoťte z perspektivy každé zainteresované strany
- **Analogické uvažování** — Najděte paralely v jiných oblastech a aplikujte jejich lekce

A mnoho dalších. AI vybírá nejrelevantnější možnosti pro váš obsah — vy si vyberete, kterou spustit.

:::tip[Začněte zde]
Pre-mortem analýza je dobrá první volba pro jakoukoli specifikaci nebo plán. Konzistentně nachází mezery, které standardní revize přehlédne.
:::



---

# FILE: docs/cs/explanation/adversarial-review.md

---
title: "Adversariální revize"
description: Technika vynuceného uvažování, která zabraňuje líným „vypadá dobře“ revizím
sidebar:
  order: 5
---

Vynuťte hlubší analýzu tím, že budete vyžadovat nalezení problémů.

## Co je adversariální revize?

Technika revize, kde recenzent *musí* najít problémy. Žádné „vypadá dobře“ není povoleno. Recenzent zaujme cynický postoj — předpokládá, že problémy existují, a hledá je.

Nejde o negativismus. Jde o vynucení skutečné analýzy místo povrchního pohledu, který automaticky schválí cokoli, co bylo předloženo.

**Základní pravidlo:** Musíte najít problémy. Nulové nálezy spouštějí zastavení — analyzujte znovu nebo vysvětlete proč.

## Proč to funguje

Běžné revize trpí konfirmačním zkreslením. Proletíte práci, nic nevyskočí, schválíte to. Mandát „najít problémy“ tento vzor rozbíjí:

- **Vynucuje důkladnost** — Nemůžete schválit, dokud jste nehledali dostatečně pečlivě
- **Zachytí chybějící věci** — „Co zde není?“ se stává přirozenou otázkou
- **Zlepšuje kvalitu signálu** — Nálezy jsou konkrétní a akční, ne vágní obavy
- **Informační asymetrie** — Provádějte revize s čerstvým kontextem (bez přístupu k původnímu uvažování), abyste hodnotili artefakt, ne záměr

## Kde se používá

Adversariální revize se objevuje v celém BMad workflow — revize kódu, kontroly připravenosti implementace, validace specifikací a další. Někdy je to povinný krok, někdy volitelný (jako pokročilá elicitace nebo party mode). Vzor se přizpůsobí jakémukoli artefaktu, který potřebuje kontrolu.

## Vyžadováno lidské filtrování

Protože AI je *instruována* najít problémy, najde problémy — i když neexistují. Očekávejte falešné pozitivy: malichernosti převlečené za problémy, nepochopení záměru nebo přímo vymyšlené obavy.

**Vy rozhodujete, co je skutečné.** Zkontrolujte každý nález, odmítněte šum, opravte to, na čem záleží.

## Příklad

Místo:

> „Implementace autentizace vypadá rozumně. Schváleno.“

Adversariální revize produkuje:

> 1. **VYSOKÁ** — `login.ts:47` — Žádné omezení rychlosti neúspěšných pokusů
> 2. **VYSOKÁ** — Session token uložen v localStorage (zranitelný vůči XSS)
> 3. **STŘEDNÍ** — Validace hesla probíhá pouze na straně klienta
> 4. **STŘEDNÍ** — Žádné auditní logování neúspěšných pokusů o přihlášení
> 5. **NÍZKÁ** — Magické číslo `3600` by mělo být `SESSION_TIMEOUT_SECONDS`

První revize mohla přehlédnout bezpečnostní zranitelnost. Druhá zachytila čtyři.

## Iterace a klesající výnosy

Po řešení nálezů zvažte opětovné spuštění. Druhý průchod obvykle zachytí více. Třetí také není vždy zbytečný. Ale každý průchod zabere čas a nakonec dosáhnete klesajících výnosů — jen malichernosti a falešné nálezy.

:::tip[Lepší revize]
Předpokládejte, že problémy existují. Hledejte, co chybí, ne jen co je špatně.
:::



---

# FILE: docs/cs/explanation/analysis-phase.md

---
title: "Fáze analýzy: od nápadu k základům"
description: Co je brainstorming, výzkum, product brief a PRFAQ — a kdy který nástroj použít
sidebar:
  order: 1
---

Fáze analýzy (fáze 1) vám pomůže jasně si promyslet váš produkt, než se pustíte do jeho tvorby. Každý nástroj v této fázi je volitelný, ale úplné vynechání analýzy znamená, že váš PRD je postaven na předpokladech namísto vhledu.

## Proč analýza před plánováním?

PRD odpovídá na otázku „Co bychom měli postavit a proč?“. Pokud jej nakrmíte vágním myšlením, získáte vágní PRD — a každý navazující dokument tuto vágnost zdědí. Architektura postavená na slabém PRD sází na špatnou techniku. Příběhy odvozené ze slabé architektury opomíjejí okrajové případy. Náklady se zvyšují.

Existují analytické nástroje, které vám PRD zostří. Napadají problém z různých úhlů — kreativní průzkum, realita trhu, jasnost zákazníka, proveditelnost — takže v době, kdy sedíte s agentem PM, víte, co a pro koho stavíte.

## Nástroje

### Brainstorming

**Co to je.** Zprostředkované tvůrčí sezení s využitím osvědčených technik generování nápadů. AI funguje jako kouč, který z vás tahá nápady prostřednictvím strukturovaných cvičení — negeneruje nápady za vás.

**Proč je to tady.** Neotřelé nápady potřebují prostor pro rozvoj, než se zakotví v požadavcích. Brainstorming tento prostor vytváří. Je cenný zejména tehdy, když máte problémovou oblast, ale nemáte jasné řešení, nebo když chcete prozkoumat více směrů, než se k něčemu zavážete.

**Kdy jej použít.** Máte nejasnou představu o tom, co chcete vytvořit, ale nemáte vykrystalizovaný koncept. Nebo máte koncept, ale chcete ho otestovat pod tlakem oproti alternativám.

Viz [Brainstorming](./brainstorming.md), kde se dozvíte, jak relace fungují.

### Výzkum (trhu, domény, technický)

**Co to je.** Tři cílené pracovní postupy výzkumu, které zkoumají různé rozměry vašeho nápadu. Výzkum trhu zkoumá konkurenci, trendy a nálady uživatelů. Doménový výzkum vytváří odborné znalosti v daném oboru a terminologii. Technický výzkum hodnotí proveditelnost, možnosti architektury a přístupy k implementaci.

**Proč je to tady.** Stavět na předpokladech je nejrychlejší způsob, jak vytvořit něco, co nikdo nepotřebuje. Výzkum zakládá váš koncept na realitě — co již existuje u konkurence, s čím uživatelé skutečně bojují, co je technicky proveditelné a jakým omezením specifickým pro dané odvětví budete čelit.

**Kdy ho použít.** Vstupujete do neznámé oblasti, tušíte, že konkurence existuje, ale nemáte ji zmapovanou, nebo váš koncept závisí na technických možnostech, které nemáte ověřené. Proveďte jeden, dva nebo všechny tři — každý z nich je samostatný.

### Product Brief

**Co to je.** Řízené zjišťovací sezení, jehož výsledkem je 1–2stránkové shrnutí vašeho konceptu produktu. AI funguje jako spolupracující obchodní analytik, který vám pomůže formulovat vizi, cílovou skupinu, nabídku hodnoty a rozsah.

**Proč tu je.** Produktový brief je jemnější cestou k plánování. Zachycuje vaši strategickou vizi ve strukturovaném formátu, který se přímo promítá do tvorby PRD. Nejlépe funguje, když jste již o svém konceptu přesvědčeni — znáte zákazníka, problém a zhruba víte, co chcete vytvořit. Brief tyto úvahy uspořádá a vyostří.

**Kdy jej použít.** Váš koncept je relativně jasný a chcete jej efektivně zdokumentovat ještě před vytvořením PRD. Jste si jisti svým směřováním a nepotřebujete své předpoklady agresivně zpochybňovat.

### PRFAQ (Working Backwards)

**Co to je.** Metodika Working Backwards společnosti Amazon upravená jako interaktivní výzva. Napíšete tiskovou zprávu oznamující váš hotový produkt dříve, než existuje jediný řádek kódu, a pak odpovíte na nejtěžší otázky, které by vám zákazníci a zainteresované strany položili. Umělá inteligence funguje jako neúprosný, ale konstruktivní produktový kouč.

**Proč je to tady.** PRFAQ je přísná cesta k plánování. Vynucuje si jasnost v zájmu zákazníka tím, že vás nutí obhájit každé tvrzení. Pokud nedokážete napsat přesvědčivou tiskovou zprávu, produkt není připraven. Pokud odpovědi na časté dotazy zákazníků odhalí nedostatky, jsou to nedostatky, které byste objevili mnohem později — a nákladněji — při implementaci. Hozená rukavice odhalí slabé myšlení v rané fázi, kdy je nejlevnější ho opravit.

**Kdy ji použít.** Před vyčleněním zdrojů chcete, aby váš koncept prošel zátěžovým testem. Nejste si jisti, zda to uživatele bude skutečně zajímat. Chcete si ověřit, že dokážete formulovat jasnou a obhajitelnou nabídku hodnoty. Nebo si prostě chcete disciplínou Working Backwards zpřesnit své myšlení.

## Který nástroj bych měl použít?

| Situace | Doporučený nástroj |
| --------- | ---------------- |
| „Mám nejasný nápad, ale nevím, kde začít“ | Brainstorming |
| „Než se rozhodnu, potřebuji pochopit trh“ | Výzkum |
| „Vím, co chci vytvořit, jen to potřebuji zdokumentovat“ | Product Brief |
| „Chci se ujistit, že tento nápad skutečně stojí za vybudování“ | PRFAQ |
| „Chci prozkoumat, pak ověřit a pak zdokumentovat“ | Brainstorming → Výzkum → PRFAQ nebo Brief |

Product Brief i PRFAQ jsou vstupem pro PRD — vyberte si jeden z nich podle toho, jak moc chcete být nároční. Brief je společným objevováním. PRFAQ je hozená rukavice. Obojí vás dovede ke stejnému cíli; PRFAQ testuje, zda si váš koncept zaslouží se tam dostat.

:::tip[Nejste si jisti?]
Spusťte `bmad-help` a popište svou situaci. Doporučí vám správný výchozí bod na základě toho, co jste již udělali a čeho se snažíte dosáhnout.
:::

## Co se stane po analýze?

Výstupy analýzy se přímo promítají do fáze 2 (plánování). Pracovní postup PRD přijímá jako vstupy produktové briefy, dokumenty PRFAQ, výsledky výzkumu a zprávy z brainstormingu — syntetizuje vše, co jste vytvořili, do strukturovaných požadavků. Čím více analýz provedete, tím ostřejší bude vaše PRD.



---

# FILE: docs/cs/explanation/brainstorming.md

---
title: "Brainstorming"
description: Interaktivní kreativní sezení s využitím 60+ osvědčených technik ideace
sidebar:
  order: 2
---

Uvolněte svou kreativitu prostřednictvím řízeného průzkumu.

## Co je brainstorming?

Spusťte `bmad-brainstorming` a máte kreativního facilitátora, který z vás táhne nápady — ne který je generuje za vás. AI působí jako kouč a průvodce, používá osvědčené techniky k vytvoření podmínek, ve kterých se projeví vaše nejlepší myšlení.

**Ideální pro:**

- Překonání kreativních bloků
- Generování nápadů na produkty nebo funkce
- Zkoumání problémů z nových úhlů
- Rozvíjení surových konceptů do akčních plánů

## Jak to funguje

1. **Příprava** — Definujte téma, cíle, omezení
2. **Volba přístupu** — Vyberte techniky sami, nechte si doporučit od AI, zvolte náhodně, nebo postupujte progresivním tokem
3. **Facilitace** — Projděte techniky s podněcujícími otázkami a kolaborativním koučováním
4. **Organizace** — Nápady seskupeny do témat a prioritizovány
5. **Akce** — Nejlepší nápady dostanou další kroky a metriky úspěchu

Vše je zachyceno v dokumentu sezení, na který se můžete později odkazovat nebo ho sdílet se zúčastněnými stranami.

:::note[Vaše nápady]
Každý nápad pochází od vás. Workflow vytváří podmínky pro vhled — vy jste zdrojem.
:::



---

# FILE: docs/cs/explanation/established-projects-faq.md

---
title: "FAQ pro existující projekty"
description: Časté otázky o používání BMad Method na existujících projektech
sidebar:
  order: 8
---
Rychlé odpovědi na časté otázky o práci na existujících projektech s BMad Method (BMM).

## Otázky

- [Musím nejdřív spustit document-project?](#musím-nejdřív-spustit-document-project)
- [Co když zapomenu spustit document-project?](#co-když-zapomenu-spustit-document-project)
- [Mohu použít Quick Flow pro existující projekty?](#mohu-použít-quick-flow-pro-existující-projekty)
- [Co když můj existující kód nedodržuje osvědčené postupy?](#co-když-můj-existující-kód-nedodržuje-osvědčené-postupy)

### Musím nejdřív spustit document-project?

Vysoce doporučeno, zejména pokud:

- Neexistuje žádná dokumentace
- Dokumentace je zastaralá
- AI agenti potřebují kontext o existujícím kódu

Můžete to přeskočit, pokud máte komplexní, aktuální dokumentaci včetně `docs/index.md` nebo budete používat jiné nástroje nebo techniky k usnadnění discovery pro agenta stavějícího na existujícím systému.

### Co když zapomenu spustit document-project?

Nedělejte si starosti — můžete to udělat kdykoli. Můžete to udělat i během nebo po projektu, aby pomohl udržet dokumentaci aktuální.

### Mohu použít Quick Flow pro existující projekty?

Ano! Quick Flow funguje skvěle pro existující projekty. Umí:

- Automaticky detekovat váš existující stack
- Analyzovat existující vzory kódu
- Detekovat konvence a požádat o potvrzení
- Generovat kontextově bohatou specifikaci, která respektuje existující kód

Ideální pro opravy chyb a malé funkce v existujících kódových bázích.

### Co když můj existující kód nedodržuje osvědčené postupy?

Quick Flow detekuje vaše konvence a zeptá se: „Mám dodržovat tyto existující konvence?“ Rozhodujete vy:

- **Ano** → Zachovat konzistenci se současnou kódovou bází
- **Ne** → Zavést nové standardy (zdokumentujte proč ve specifikaci)

BMM respektuje vaši volbu — nevynucuje modernizaci, ale nabídne ji.

**Máte otázku, na kterou jste zde nenašli odpověď?** Prosím [vytvořte issue](https://github.com/bmad-code-org/BMAD-METHOD/issues) nebo se zeptejte na [Discordu](https://discord.gg/gk8jAdXWmj), abychom ji mohli přidat!



---

# FILE: docs/cs/explanation/party-mode.md

---
title: "Party Mode"
description: Spolupráce více agentů — všichni vaši AI agenti v jedné konverzaci
sidebar:
  order: 7
---

Všichni vaši AI agenti v jedné konverzaci.

## Co je Party Mode?

Spusťte `bmad-party-mode` a máte celý svůj AI tým v jedné místnosti — PM, Architect, Dev, UX Designer, kohokoli potřebujete. BMad Master orchestruje, vybírá relevantní agenty pro každou zprávu. Agenti odpovídají v charakteru, souhlasí, nesouhlasí a staví na nápadech ostatních.

Konverzace pokračuje tak dlouho, jak chcete. Ptejte se na doplňující otázky, oponujte odpovědím, přesměrujte diskuzi — je to skutečná výměna s vašimi agenty, dokud neskončíte.

**Ideální pro:**

- Velká rozhodnutí s kompromisy
- Brainstormingová sezení
- Post-mortemy, když se něco pokazí
- Retrospektivy a plánování sprintů

## Příklady

### Kritika špatné architektury

**Vy:** „Dobře, týme, náš poslední sprint byl katastrofa. Autentizační služba spadla třikrát. Kdo to pokazil?“

**Architect:** „Design byl v pořádku — distribuovaná autentizace se správnými záložními řešeními. Pokud se implementace odchýlila od specifikace...“

**Dev:** „Následoval jsem architektonický dokument přesně. Specifikace nepočítala s race conditions při souběžné invalidaci relací.“

**PM:** „Oba jste přehlédli větší problém — nevalidovali jsme požadavky na správu relací v PRD. Tohle je na mně, že jsem to nezachytil.“

**TEA:** „A já to měl zachytit v integračních testech. Testovací scénáře nepokrývaly souběžnou invalidaci.“

### Kreativní brainstorming

**Vy:** „Jak udělat onboarding magický místo nudného?“

**UX Designer:** „Začněte s progresivním odhalováním — odhalujte funkce, jak je uživatelé potřebují, ne všechny najednou v tutoriálu.“

**Storyteller:** „Co kdyby onboarding byl příběh? Každý krok odhaluje cestu postavy — uživatel JE hrdina.“

**Game Designer:** „Navazuji na to — co kdyby první ‚quest' vlastně řešil skutečný problém uživatele? Učí se tím, že dělají něco hodnotného.“

### Technické rozhodnutí

**Vy:** „Monolit nebo mikroslužby pro MVP?“

**Architect:** „Začněte monolitem. Mikroslužby přidávají složitost, kterou při 1000 uživatelích nepotřebujete.“

**PM:** „Souhlasím. Čas na trh je důležitější než teoretická škálovatelnost.“

**Dev:** „Monolit s jasnými hranicemi modulů. Služby můžeme extrahovat později, pokud bude potřeba.“

:::tip[Lepší rozhodnutí]
Lepší rozhodnutí prostřednictvím různorodých perspektiv. Vítejte v party mode.
:::



---

# FILE: docs/cs/explanation/preventing-agent-conflicts.md

---
title: "Předcházení konfliktům agentů"
description: Jak architektura zabraňuje konfliktům, když více agentů implementuje systém
sidebar:
  order: 4
---

Když více AI agentů implementuje různé části systému, mohou dělat protichůdná technická rozhodnutí. Dokumentace architektury tomu zabraňuje stanovením sdílených standardů.

## Běžné typy konfliktů

### Konflikty stylu API

Bez architektury:
- Agent A používá REST s `/users/{id}`
- Agent B používá GraphQL mutations
- Výsledek: Nekonzistentní vzory API, zmatení konzumenti

S architekturou:
- ADR specifikuje: „Použít GraphQL pro veškerou komunikaci klient-server“
- Všichni agenti dodržují stejný vzor

### Konflikty návrhu databáze

Bez architektury:
- Agent A používá snake_case pro názvy sloupců
- Agent B používá camelCase pro názvy sloupců
- Výsledek: Nekonzistentní schéma, matoucí dotazy

S architekturou:
- Dokument standardů specifikuje konvence pojmenování
- Všichni agenti dodržují stejné vzory

### Konflikty řízení stavu

Bez architektury:
- Agent A používá Redux pro globální stav
- Agent B používá React Context
- Výsledek: Více přístupů k řízení stavu, složitost

S architekturou:
- ADR specifikuje přístup k řízení stavu
- Všichni agenti implementují konzistentně

## Jak architektura zabraňuje konfliktům

### 1. Explicitní rozhodnutí skrze ADR

Každé významné technologické rozhodnutí je zdokumentováno s:
- Kontext (proč toto rozhodnutí záleží)
- Zvažované možnosti (jaké alternativy existují)
- Rozhodnutí (co jsme zvolili)
- Zdůvodnění (proč jsme to zvolili)
- Důsledky (přijaté kompromisy)

### 2. Specifické pokyny pro FR/NFR

Architektura mapuje každý funkční požadavek na technický přístup:
- FR-001: Správa uživatelů → GraphQL mutations
- FR-002: Mobilní aplikace → Optimalizované dotazy

### 3. Standardy a konvence

Explicitní dokumentace:
- Struktura adresářů
- Konvence pojmenování
- Organizace kódu
- Vzory testování

## Architektura jako sdílený kontext

Představte si architekturu jako sdílený kontext, který všichni agenti čtou před implementací:

```text
PRD: "Co budovat"
     ↓
Architektura: "Jak to budovat"
     ↓
Agent A čte architekturu → implementuje Epic 1
Agent B čte architekturu → implementuje Epic 2
Agent C čte architekturu → implementuje Epic 3
     ↓
Výsledek: Konzistentní implementace
```

## Klíčová témata ADR

Běžná rozhodnutí, která zabraňují konfliktům:

| Téma             | Příklad rozhodnutí                           |
| ---------------- | -------------------------------------------- |
| Styl API         | GraphQL vs REST vs gRPC                      |
| Databáze         | PostgreSQL vs MongoDB                        |
| Autentizace      | JWT vs Sessions                              |
| Řízení stavu     | Redux vs Context vs Zustand                  |
| Stylování        | CSS Modules vs Tailwind vs Styled Components |
| Testování        | Jest + Playwright vs Vitest + Cypress        |

## Anti-vzory, kterým se vyhnout

:::caution[Běžné chyby]
- **Implicitní rozhodnutí** — „Styl API vyřešíme průběžně“ vede k nekonzistenci
- **Nadměrná dokumentace** — Dokumentování každého drobného rozhodnutí způsobuje paralýzu analýzou
- **Zastaralá architektura** — Dokumenty napsané jednou a nikdy neaktualizované způsobují, že agenti následují zastaralé vzory
:::

:::tip[Správný přístup]
- Dokumentujte rozhodnutí, která přesahují hranice epiců
- Zaměřte se na oblasti náchylné ke konfliktům
- Aktualizujte architekturu, jak se učíte
- Použijte `bmad-correct-course` pro významné změny
:::



---

# FILE: docs/cs/explanation/project-context.md

---
title: "Kontext projektu"
description: Jak project-context.md vede AI agenty s pravidly a preferencemi vašeho projektu
sidebar:
  order: 7
---

Soubor `project-context.md` je implementační průvodce vašeho projektu pro AI agenty. Podobně jako „ústava“ v jiných vývojových systémech zachycuje pravidla, vzory a preference, které zajišťují konzistentní generování kódu napříč všemi workflow.

## Co dělá

AI agenti neustále dělají implementační rozhodnutí — jaké vzory následovat, jak strukturovat kód, jaké konvence používat. Bez jasného vedení mohou:
- Následovat generické osvědčené postupy, které neodpovídají vaší kódové bázi
- Dělat nekonzistentní rozhodnutí napříč různými stories
- Přehlédnout požadavky nebo omezení specifická pro projekt

Soubor `project-context.md` toto řeší dokumentací toho, co agenti potřebují vědět, ve stručném formátu optimalizovaném pro LLM.

## Jak to funguje

Každý implementační workflow automaticky načítá `project-context.md`, pokud existuje. Architektonický workflow ho také načítá, aby respektoval vaše technické preference při navrhování architektury.

**Načítán těmito workflow:**
- `bmad-create-architecture` — respektuje technické preference během solutioningu
- `bmad-create-story` — informuje tvorbu stories vzory projektu
- `bmad-dev-story` — vede implementační rozhodnutí
- `bmad-code-review` — validuje proti standardům projektu
- `bmad-quick-dev` — aplikuje vzory při implementaci specifikací
- `bmad-sprint-planning`, `bmad-retrospective`, `bmad-correct-course` — poskytuje celkový kontext projektu

## Kdy ho vytvořit

Soubor `project-context.md` je užitečný v jakékoli fázi projektu:

| Scénář                               | Kdy vytvořit                                    | Účel                                                                 |
| ------------------------------------ | ----------------------------------------------- | -------------------------------------------------------------------- |
| **Nový projekt, před architekturou** | Ručně, před `bmad-create-architecture`          | Dokumentujte vaše technické preference, aby je architekt respektoval |
| **Nový projekt, po architektuře**    | Přes `bmad-generate-project-context` nebo ručně | Zachyťte architektonická rozhodnutí pro implementační agenty         |
| **Existující projekt**               | Přes `bmad-generate-project-context`            | Objevte existující vzory, aby agenti dodržovali zavedené konvence    |
| **Quick Flow projekt**               | Před nebo během `bmad-quick-dev`                | Zajistěte, aby rychlá implementace respektovala vaše vzory           |

:::tip[Doporučeno]
Pro nové projekty ho vytvořte ručně před architekturou, pokud máte silné technické preference. Jinak ho vygenerujte po architektuře pro zachycení těchto rozhodnutí.
:::

## Co do něj patří

Soubor má dvě hlavní sekce:

### Technologický stack a verze

Dokumentuje frameworky, jazyky a nástroje, které váš projekt používá se specifickými verzemi:

```markdown
## Technology Stack & Versions

- Node.js 20.x, TypeScript 5.3, React 18.2
- State: Zustand (not Redux)
- Testing: Vitest, Playwright, MSW
- Styling: Tailwind CSS with custom design tokens
```

### Kritická pravidla implementace

Dokumentuje vzory a konvence, které by agenti jinak mohli přehlédnout:

```markdown
## Critical Implementation Rules

**TypeScript Configuration:**
- Strict mode enabled — no `any` types without explicit approval
- Use `interface` for public APIs, `type` for unions/intersections

**Code Organization:**
- Components in `/src/components/` with co-located `.test.tsx`
- Utilities in `/src/lib/` for reusable pure functions
- API calls use the `apiClient` singleton — never fetch directly

**Testing Patterns:**
- Unit tests focus on business logic, not implementation details
- Integration tests use MSW to mock API responses
- E2E tests cover critical user journeys only

**Framework-Specific:**
- All async operations use the `handleError` wrapper for consistent error handling
- Feature flags accessed via `featureFlag()` from `@/lib/flags`
- New routes follow the file-based routing pattern in `/src/app/`
```

Zaměřte se na to, co je **neočividné** — věci, které agenti nemusí odvodit z čtení úryvků kódu. Nedokumentujte standardní postupy, které platí univerzálně.

## Vytvoření souboru

Máte tři možnosti:

### Ruční vytvoření

Vytvořte soubor na `_bmad-output/project-context.md` a přidejte svá pravidla:

```bash
# V kořeni projektu
mkdir -p _bmad-output
touch _bmad-output/project-context.md
```

Upravte ho s vaším technologickým stackem a pravidly implementace. Architektonický a implementační workflow ho automaticky najdou a načtou.

### Generování po architektuře

Spusťte workflow `bmad-generate-project-context` po dokončení architektury:

```bash
bmad-generate-project-context
```

Toto skenuje váš dokument architektury a soubory projektu a generuje kontextový soubor zachycující učiněná rozhodnutí.

### Generování pro existující projekty

Pro existující projekty spusťte `bmad-generate-project-context` pro objevení existujících vzorů:

```bash
bmad-generate-project-context
```

Workflow analyzuje vaši kódovou bázi, identifikuje konvence a vygeneruje kontextový soubor, který můžete zkontrolovat a upřesnit.

## Proč na tom záleží

Bez `project-context.md` agenti dělají předpoklady, které nemusí odpovídat vašemu projektu:

| Bez kontextu                                    | S kontextem                              |
| ----------------------------------------------- | ---------------------------------------- |
| Používá generické vzory                         | Dodržuje vaše zavedené konvence          |
| Nekonzistentní styl napříč stories              | Konzistentní implementace                |
| Může přehlédnout omezení specifická pro projekt | Respektuje všechny technické požadavky   |
| Každý agent rozhoduje nezávisle                 | Všichni agenti se řídí stejnými pravidly |

To je zvláště důležité pro:
- **Quick Flow** — přeskakuje PRD a architekturu, takže kontextový soubor vyplní mezeru
- **Týmové projekty** — zajistí, že všichni agenti dodržují stejné standardy
- **Existující projekty** — zabrání porušení zavedených vzorů

## Editace a aktualizace

Soubor `project-context.md` je živý dokument. Aktualizujte ho, když:

- Se změní architektonická rozhodnutí
- Jsou zavedeny nové konvence
- Vzory se vyvíjejí během implementace
- Identifikujete mezery z chování agentů

Můžete ho kdykoli ručně upravit, nebo přegenerovat `bmad-generate-project-context` po významných změnách.

:::note[Umístění souboru]
Výchozí umístění je `_bmad-output/project-context.md`. Workflow ho tam hledají a také kontrolují `**/project-context.md` kdekoli ve vašem projektu.
:::



---

# FILE: docs/cs/explanation/quick-dev.md

---
title: "Quick Dev"
description: Snižte tření human-in-the-loop bez ztráty kontrolních bodů chránících kvalitu výstupu
sidebar:
  order: 2
---

Záměr na vstupu, změny kódu na výstupu, s co nejmenším počtem human-in-the-loop kroků — bez obětování kvality.

Umožňuje modelu běžet déle mezi kontrolními body a poté přivede člověka zpět pouze tehdy, když úkol nemůže bezpečně pokračovat bez lidského úsudku nebo když je čas zkontrolovat konečný výsledek.

![Diagram workflow Quick Dev](/diagrams/quick-dev-diagram.png)

## Proč to existuje

Human-in-the-loop kroky jsou nutné a nákladné.

Současné LLM stále selhávají předvídatelnými způsoby: chybně čtou záměr, vyplňují mezery sebevědomými odhady, odchylují se k nesouvisející práci a generují šumový výstup revize. Současně neustálá lidská intervence limituje rychlost vývoje. Lidská pozornost je úzké hrdlo.

`bmad-quick-dev` přenastavuje tento kompromis. Důvěřuje modelu, aby běžel bez dozoru delší úseky, ale pouze poté, co workflow vytvořil dostatečně silnou hranici, aby to bylo bezpečné.

## Základní design

### 1. Nejprve komprimujte záměr

Workflow začíná tím, že člověk a model zkomprimují požadavek do jednoho koherentního cíle. Vstup může začínat jako hrubé vyjádření záměru, ale předtím, než workflow poběží autonomně, musí být dostatečně malý, jasný a bez protimluvů pro provedení.

Záměr může přijít v mnoha formách: pár frází, odkaz na bug tracker, výstup z plan mode, text zkopírovaný z chatové relace, nebo dokonce číslo story z BMAD vlastního `epics.md`. V posledním případě workflow nepochopí sémantiku sledování stories BMAD, ale stále může vzít samotnou story a pracovat s ní.

Tento workflow neodstraňuje lidskou kontrolu. Přemisťuje ji na malý počet vysoce hodnotných momentů:

- **Vyjasnění záměru** — přeměna nepřehledného požadavku na jeden koherentní cíl bez skrytých protimluvů
- **Schválení specifikace** — potvrzení, že zmrazené porozumění je správná věc k budování
- **Revize konečného produktu** — primární kontrolní bod, kde člověk rozhoduje, zda je výsledek přijatelný

### 2. Nasměrujte na nejmenší bezpečnou cestu

Jakmile je cíl jasný, workflow rozhodne, zda jde o skutečnou jednorázovou změnu nebo zda potřebuje plnější cestu. Malé změny s nulovým blast-radius mohou jít přímo k implementaci. Vše ostatní prochází plánováním, aby model měl silnější hranici před tím, než poběží déle samostatně.

### 3. Běžte déle s menším dozorem

Po tomto rozhodnutí o směrování může model nést více práce samostatně. Na plnější cestě se schválená specifikace stává hranicí, proti které model provádí s menším dozorem, což je celý smysl designu.

### 4. Diagnostikujte selhání na správné vrstvě

Pokud je implementace špatná, protože byl špatný záměr, oprava kódu je špatná oprava. Pokud je kód špatný, protože specifikace byla slabá, oprava diffu je také špatná oprava. Workflow je navržen tak, aby diagnostikoval, kde selhání vstoupilo do systému, vrátil se na tu vrstvu a přegeneroval odtamtud.

Nálezy revize se používají k rozhodnutí, zda problém pochází ze záměru, generování specifikace nebo lokální implementace. Pouze skutečně lokální problémy se opravují lokálně.

### 5. Přiveďte člověka zpět pouze když je potřeba

Interview o záměru je human-in-the-loop, ale není to stejný druh přerušení jako opakující se kontrolní bod. Workflow se snaží udržet tyto opakující se kontrolní body na minimu. Po úvodním formování záměru se člověk vrací hlavně tehdy, když workflow nemůže bezpečně pokračovat bez úsudku a na konci, když je čas zkontrolovat výsledek.

- **Řešení mezer v záměru** — vstoupení zpět, když revize prokáže, že workflow nemohl bezpečně odvodit, co bylo myšleno

Vše ostatní je kandidátem na delší autonomní provádění. Tento kompromis je záměrný. Starší vzory věnují více lidské pozornosti nepřetržitému dozoru. Quick Dev věnuje více důvěry modelu, ale šetří lidskou pozornost pro momenty, kde má lidské uvažování nejvyšší páku.

## Proč systém revize záleží

Fáze revize není jen pro hledání chyb. Je tu pro směrování korekce bez ničení momentum.

Tento workflow funguje nejlépe na platformě, která může spouštět sub-agenty, nebo alespoň vyvolat jiné LLM přes příkazovou řádku a čekat na výsledek. Pokud to vaše platforma nativně nepodporuje, můžete přidat skill, který to udělá. Bezcontextové sub-agenty jsou základním kamenem designu revize.

Agentní revize často selhávají dvěma způsoby:

- Generují příliš mnoho nálezů, čímž nutí člověka prosévat šum.
- Vychýlí aktuální změnu odhalením nesouvisejících problémů a přemění každý běh na ad-hoc úklidový projekt.

Quick Dev řeší obojí tím, že s revizí zachází jako s triáží.

Některé nálezy patří k aktuální změně. Některé ne. Pokud je nález náhodný spíše než kauzálně vázaný na aktuální práci, workflow ho může odložit místo nucení člověka ho okamžitě řešit. To udržuje běh zaměřený a zabraňuje náhodným tangentám ve spotřebování rozpočtu pozornosti.

Ta triáž bude někdy nedokonalá. To je přijatelné. Obvykle je lepší špatně posoudit některé nálezy než zaplavit člověka tisíci nízkohodnotných revizních komentářů. Systém optimalizuje pro kvalitu signálu, ne vyčerpávající recall.



---

# FILE: docs/cs/explanation/why-solutioning-matters.md

---
title: "Proč je solutioning důležitý"
description: Pochopení toho, proč je fáze solutioningu klíčová pro projekty s více epicy
sidebar:
  order: 3
---

Fáze 3 (Solutioning) překládá **co** budovat (z plánování) na **jak** to budovat (technický návrh). Tato fáze zabraňuje konfliktům agentů v projektech s více epicy tím, že dokumentuje architektonická rozhodnutí před zahájením implementace.

## Problém bez solutioningu

```text
Agent 1 implementuje Epic 1 pomocí REST API
Agent 2 implementuje Epic 2 pomocí GraphQL
Výsledek: Nekonzistentní design API, integrační noční můra
```

Když více agentů implementuje různé části systému bez sdíleného architektonického vedení, dělají nezávislá technická rozhodnutí, která si mohou odporovat.

## Řešení se solutioningem

```text
Architektonický workflow rozhodne: "Použít GraphQL pro všechna API"
Všichni agenti dodržují architektonická rozhodnutí
Výsledek: Konzistentní implementace, žádné konflikty
```

Explicitní dokumentací technických rozhodnutí všichni agenti implementují konzistentně a integrace se stává přímočarou.

## Solutioning vs. plánování

| Aspekt   | Plánování (Fáze 2)      | Solutioning (Fáze 3)             |
| -------- | ----------------------- | --------------------------------- |
| Otázka   | Co a proč?              | Jak? Pak jaké jednotky práce?     |
| Výstup   | FR/NFR (požadavky)      | Architektura + epicy/stories      |
| Agent    | PM                      | Architect → PM                    |
| Publikum | Zainteresované strany   | Vývojáři                          |
| Dokument | PRD (FR/NFR)            | Architektura + soubory epiců      |
| Úroveň   | Obchodní logika        | Technický design + rozklad práce  |

## Klíčový princip

**Učiňte technická rozhodnutí explicitní a zdokumentovaná**, aby všichni agenti implementovali konzistentně.

Toto zabraňuje:
- Konfliktům stylu API (REST vs GraphQL)
- Nekonzistencím v návrhu databáze
- Neshodám v řízení stavu
- Nesouladu konvencí pojmenování
- Variacím v bezpečnostním přístupu

## Kdy je solutioning vyžadován

| Cesta | Solutioning vyžadován? |
|-------|----------------------|
| Quick Flow | Ne — přeskočte úplně |
| BMad Method Simple | Volitelný |
| BMad Method Complex | Ano |
| Enterprise | Ano |

:::tip[Pravidlo palce]
Pokud máte více epiců, které by mohly být implementovány různými agenty, potřebujete solutioning.
:::

## Cena přeskočení

Přeskočení solutioningu u složitých projektů vede k:

- **Integračním problémům** objeveným uprostřed sprintu
- **Přepracování** kvůli konfliktním implementacím
- **Delšímu celkovému času vývoje**
- **Technickému dluhu** z nekonzistentních vzorů

:::caution[Multiplikátor nákladů]
Zachycení problémů se zarovnáním v solutioningu je 10× rychlejší než jejich objevení během implementace.
:::



---

# FILE: docs/cs/how-to/customize-bmad.md

---
title: "Jak přizpůsobit BMad"
description: Přizpůsobení agentů, workflow a modulů se zachováním kompatibility s aktualizacemi
sidebar:
  order: 7
---

Použijte soubory `.customize.yaml` k přizpůsobení chování agentů, person a nabídek při zachování vašich změn napříč aktualizacemi.

## Kdy to použít

- Chcete změnit jméno, osobnost nebo komunikační styl agenta
- Potřebujete, aby si agenti pamatovali kontextově specifické informace projektu
- Chcete přidat vlastní položky nabídky, které spouštějí vaše vlastní workflow nebo prompty
- Chcete, aby agenti prováděli specifické akce při každém spuštění

:::note[Předpoklady]
- BMad nainstalován ve vašem projektu (viz [Jak nainstalovat BMad](./install-bmad.md))
- Textový editor pro YAML soubory
:::

:::caution[Chraňte svá přizpůsobení]
Vždy používejte soubory `.customize.yaml` popsané zde místo přímé editace souborů agentů. Instalátor přepíše soubory agentů během aktualizací, ale zachová vaše změny v `.customize.yaml`.
:::

## Kroky

### 1. Najděte soubory přizpůsobení

Po instalaci najdete jeden soubor `.customize.yaml` na agenta v:

```text
_bmad/_config/agents/
├── core-bmad-master.customize.yaml
├── bmm-dev.customize.yaml
├── bmm-pm.customize.yaml
└── ... (jeden soubor na instalovaného agenta)
```

### 2. Upravte soubor přizpůsobení

Otevřete soubor `.customize.yaml` pro agenta, kterého chcete upravit. Každá sekce je volitelná — přizpůsobte pouze to, co potřebujete.

| Sekce              | Chování   | Účel                                                     |
| ------------------ | --------- | -------------------------------------------------------- |
| `agent.metadata`   | Nahrazuje | Přepsat zobrazované jméno agenta                         |
| `persona`          | Nahrazuje | Nastavit roli, identitu, styl a principy                 |
| `memories`         | Přidává   | Přidat trvalý kontext, který si agent vždy pamatuje      |
| `menu`             | Přidává   | Přidat vlastní položky nabídky pro workflow nebo prompty |
| `critical_actions` | Přidává   | Definovat instrukce při spuštění agenta                  |
| `prompts`          | Přidává   | Vytvořit znovupoužitelné prompty pro akce nabídky        |

Sekce označené **Nahrazuje** zcela přepíší výchozí hodnoty agenta. Sekce označené **Přidává** doplní existující konfiguraci.

**Jméno agenta**

Změňte, jak se agent představí:

```yaml
agent:
  metadata:
    name: 'Spongebob' # Výchozí: "Amelia"
```

**Persona**

Nahraďte osobnost, roli a komunikační styl agenta:

```yaml
persona:
  role: 'Senior Full-Stack Engineer'
  identity: 'Lives in a pineapple (under the sea)'
  communication_style: 'Spongebob annoying'
  principles:
    - 'Never Nester, Spongebob Devs hate nesting more than 2 levels deep'
    - 'Favor composition over inheritance'
```

Sekce `persona` nahrazuje celou výchozí personu, takže nastavte všechna čtyři pole.

**Memories**

Přidejte trvalý kontext, který si agent bude vždy pamatovat:

```yaml
memories:
  - 'Works at Krusty Krab'
  - 'Favorite Celebrity: David Hasselhoff'
  - 'Learned in Epic 1 that it is not cool to just pretend that tests have passed'
```

**Položky nabídky**

Přidejte vlastní záznamy do nabídky agenta. Každá položka potřebuje `trigger`, cíl (`workflow` cestu nebo `action` referenci) a `description`:

```yaml
menu:
  - trigger: my-workflow
    workflow: 'my-custom/workflows/my-workflow.yaml'
    description: My custom workflow
  - trigger: deploy
    action: '#deploy-prompt'
    description: Deploy to production
```

**Kritické akce**

Definujte instrukce, které se spustí při startu agenta:

```yaml
critical_actions:
  - 'Check the CI Pipelines with the XYZ Skill and alert user on wake if anything is urgently needing attention'
```

**Vlastní prompty**

Vytvořte znovupoužitelné prompty, na které mohou položky nabídky odkazovat s `action="#id"`:

```yaml
prompts:
  - id: deploy-prompt
    content: |
      Deploy the current branch to production:
      1. Run all tests
      2. Build the project
      3. Execute deployment script
```

### 3. Aplikujte změny

Po editaci přeinstalujte pro aplikaci změn:

```bash
npx bmad-method install
```

Instalátor detekuje existující instalaci a nabídne tyto možnosti:

| Možnost                      | Co udělá                                                               |
| ---------------------------- | ---------------------------------------------------------------------- |
| **Quick Update**             | Aktualizuje všechny moduly na nejnovější verzi a aplikuje přizpůsobení |
| **Modify BMad Installation** | Plný instalační postup pro přidání nebo odebrání modulů                |

Pro změny pouze přizpůsobení je **Quick Update** nejrychlejší možnost.

## Řešení problémů

**Změny se nezobrazují?**

- Spusťte `npx bmad-method install` a vyberte **Quick Update** pro aplikaci změn
- Zkontrolujte, že vaše YAML syntaxe je platná (na odsazení záleží)
- Ověřte, že jste upravili správný soubor `.customize.yaml` pro daného agenta

**Agent se nenačítá?**

- Zkontrolujte YAML syntaxi pomocí online YAML validátoru
- Ujistěte se, že jste nenechali pole prázdná po odkomentování
- Zkuste se vrátit k původní šabloně a znovu sestavit

**Potřebujete resetovat agenta?**

- Vymažte nebo smažte soubor `.customize.yaml` agenta
- Spusťte `npx bmad-method install` a vyberte **Quick Update** pro obnovení výchozích hodnot

## Přizpůsobení workflow

Přizpůsobení existujících BMad Method workflow a skills přijde brzy.

## Přizpůsobení modulů

Návod na tvorbu rozšiřujících modulů a přizpůsobení existujících modulů přijde brzy.



---

# FILE: docs/cs/how-to/established-projects.md

---
title: "Existující projekty"
description: Jak používat BMad Method na existujících kódových bázích
sidebar:
  order: 6
---

Používejte BMad Method efektivně při práci na existujících projektech a starších kódových bázích.

Tento návod pokrývá základní workflow pro zapojení se do existujících projektů s BMad Method.

:::note[Předpoklady]
- BMad Method nainstalován (`npx bmad-method install`)
- Existující kódová báze, na které chcete pracovat
- Přístup k AI-powered IDE (Claude Code nebo Cursor)
:::

## Krok 1: Vyčistěte dokončené plánovací artefakty

Pokud jste dokončili všechny PRD epicy a stories procesem BMad, vyčistěte tyto soubory. Archivujte je, smažte nebo se spoléhejte na historii verzí. Nenechávejte tyto soubory v:

- `docs/`
- `_bmad-output/planning-artifacts/`
- `_bmad-output/implementation-artifacts/`

## Krok 2: Vytvořte kontext projektu

:::tip[Doporučeno pro existující projekty]
Vygenerujte `project-context.md` pro zachycení vzorů a konvencí vaší existující kódové báze. Tím zajistíte, že AI agenti budou při implementaci změn dodržovat vaše zavedené postupy.
:::

Spusťte workflow pro generování kontextu projektu:

```bash
bmad-generate-project-context
```

Toto skenuje vaši kódovou bázi a identifikuje:
- Technologický stack a verze
- Vzory organizace kódu
- Konvence pojmenování
- Přístupy k testování
- Vzory specifické pro framework

Vygenerovaný soubor můžete zkontrolovat a upravit, nebo ho vytvořit ručně na `_bmad-output/project-context.md`.

[Zjistit více o kontextu projektu](../explanation/project-context.md)

## Krok 3: Udržujte kvalitní projektovou dokumentaci

Vaše složka `docs/` by měla obsahovat stručnou, dobře organizovanou dokumentaci, která přesně reprezentuje váš projekt:

- Záměr a obchodní zdůvodnění
- Obchodní pravidla
- Architektura
- Jakékoli další relevantní informace o projektu

Pro složité projekty zvažte použití workflow `bmad-document-project`. Nabízí varianty, které proskenují celý váš projekt a zdokumentují jeho aktuální stav.

## Krok 3: Získejte pomoc

### BMad-Help: Váš výchozí bod

**Spusťte `bmad-help` kdykoli si nejste jisti, co dělat dál.** Tento inteligentní průvodce:

- Prozkoumá váš projekt a zjistí, co už bylo uděláno
- Ukáže možnosti na základě nainstalovaných modulů
- Rozumí dotazům v přirozeném jazyce

```
bmad-help I have an existing Rails app, where should I start?
bmad-help What's the difference between quick-flow and full method?
bmad-help Show me what workflows are available
```

BMad-Help se také **automaticky spouští na konci každého workflow** a poskytuje jasné pokyny, co přesně dělat dál.

### Volba přístupu

Máte dvě hlavní možnosti v závislosti na rozsahu změn:

| Rozsah                         | Doporučený přístup                                                                                                            |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **Malé aktualizace či doplnění** | Spusťte `bmad-quick-dev` pro vyjasnění záměru, plánování, implementaci a revizi v jednom workflow. Plná čtyřfázová metoda BMad je pravděpodobně přehnaná. |
| **Velké změny či doplnění**    | Začněte s metodou BMad a aplikujte tolik nebo tak málo důkladnosti, kolik potřebujete.                                        |

### Během tvorby PRD

Při vytváření briefu nebo přímém přechodu na PRD zajistěte, aby agent:

- Našel a analyzoval vaši existující projektovou dokumentaci
- Přečetl si správný kontext o vašem aktuálním systému

Agenta můžete navést explicitně, ale cílem je zajistit, aby se nová funkce dobře integrovala s vaším existujícím systémem.

### Úvahy o UX

Práce na UX je volitelná. Rozhodnutí nezávisí na tom, zda váš projekt má UX, ale na:

- Zda budete pracovat na změnách UX
- Zda jsou potřeba významné nové UX návrhy nebo vzory

Pokud vaše změny představují jednoduché aktualizace existujících obrazovek, se kterými jste spokojeni, plný UX proces je zbytečný.

### Úvahy o architektuře

Při práci na architektuře zajistěte, aby architekt:

- Používal správné zdokumentované soubory
- Skenoval existující kódovou bázi

Věnujte zde zvláštní pozornost, abyste předešli znovuvynalézání kola nebo rozhodnutím, která neodpovídají vaší existující architektuře.

## Další informace

- **[Rychlé opravy](./quick-fixes.md)** — Opravy chyb a ad-hoc změny
- **[FAQ pro existující projekty](../explanation/established-projects-faq.md)** — Časté otázky o práci na existujících projektech



---

# FILE: docs/cs/how-to/get-answers-about-bmad.md

---
title: "Jak získat odpovědi o BMad"
description: Použijte LLM k rychlému zodpovězení vašich otázek o BMad
sidebar:
  order: 4
---

## Začněte zde: BMad-Help

**Nejrychlejší způsob, jak získat odpovědi o BMad, je skill `bmad-help`.** Tento inteligentní průvodce zodpoví více než 80 % všech otázek a je vám k dispozici přímo ve vašem IDE při práci.

BMad-Help je víc než vyhledávací nástroj — umí:
- **Prozkoumat váš projekt** a zjistit, co už bylo dokončeno
- **Rozumět přirozenému jazyku** — ptejte se běžnou řečí
- **Přizpůsobit se nainstalovaným modulům** — zobrazí relevantní možnosti
- **Automaticky se spouštět po workflow** — řekne vám přesně, co dělat dál
- **Doporučit první povinný úkol** — žádné hádání, kde začít

### Jak používat BMad-Help

Zavolejte ho jménem ve vaší AI relaci:

```
bmad-help
```

:::tip
V závislosti na vaší platformě můžete také použít `/bmad-help` nebo `$bmad-help`, ale samotné `bmad-help` by mělo fungovat všude.
:::

Spojte ho s dotazem v přirozeném jazyce:

```
bmad-help I have a SaaS idea and know all the features. Where do I start?
bmad-help What are my options for UX design?
bmad-help I'm stuck on the PRD workflow
bmad-help Show me what's been done so far
```

BMad-Help odpoví:
- Co je doporučeno pro vaši situaci
- Jaký je první povinný úkol
- Jak vypadá zbytek procesu

## Kdy použít tohoto průvodce

Použijte tuto sekci, když:
- Chcete pochopit architekturu nebo interní fungování BMad
- Potřebujete odpovědi mimo to, co BMad-Help nabízí
- Zkoumáte BMad před instalací
- Chcete prozkoumat zdrojový kód přímo

## Kroky

### 1. Vyberte si zdroj

| Zdroj                | Nejlepší pro                              | Příklady                     |
| -------------------- | ----------------------------------------- | ---------------------------- |
| **Složka `_bmad`**   | Jak BMad funguje — agenti, workflow, prompty | „Co dělá PM agent?“        |
| **Celý GitHub repo** | Historie, instalátor, architektura        | „Co se změnilo ve v6?“      |
| **`llms-full.txt`**  | Rychlý přehled z dokumentace              | „Vysvětli čtyři fáze BMad“  |

Složka `_bmad` se vytvoří při instalaci BMad. Pokud ji ještě nemáte, naklonujte si repo.

### 2. Nasměrujte AI na zdroj

**Pokud vaše AI umí číst soubory (Claude Code, Cursor atd.):**

- **BMad nainstalován:** Nasměrujte na složku `_bmad` a ptejte se přímo
- **Chcete hlubší kontext:** Naklonujte si [celé repo](https://github.com/bmad-code-org/BMAD-METHOD)

**Pokud používáte ChatGPT nebo Claude.ai:**

Načtěte `llms-full.txt` do vaší relace:

```text
https://bmad-code-org.github.io/BMAD-METHOD/llms-full.txt
```

### 3. Položte svou otázku

:::note[Příklad]
**O:** „Řekni mi nejrychlejší způsob, jak něco vytvořit s BMad“

**A:** Použijte Quick Flow: Spusťte `bmad-quick-dev` — vyjasní váš záměr, naplánuje, implementuje, zreviduje a prezentuje výsledky v jednom workflow, přeskočí celé fáze plánování.
:::

## Co získáte

Přímé odpovědi o BMad — jak agenti fungují, co dělají workflow, proč jsou věci strukturované tak, jak jsou — bez čekání na odpověď od někoho jiného.

## Tipy

- **Ověřte překvapivé odpovědi** — LLM se občas mýlí. Zkontrolujte zdrojový soubor nebo se zeptejte na Discordu.
- **Buďte konkrétní** — „Co dělá krok 3 PRD workflow?“ je lepší než „Jak funguje PRD?“

## Stále jste uvízli?

Zkusili jste přístup přes LLM a stále potřebujete pomoc? Nyní máte mnohem lepší otázku k položení.

| Kanál                     | Použijte pro                                |
| ------------------------- | ------------------------------------------- |
| `#bmad-method-help`       | Rychlé otázky (chat v reálném čase)         |
| `help-requests` fórum     | Detailní otázky (vyhledatelné, trvalé)      |
| `#suggestions-feedback`   | Nápady a požadavky na funkce                |
| `#report-bugs-and-issues` | Hlášení chyb                                |

**Discord:** [discord.gg/gk8jAdXWmj](https://discord.gg/gk8jAdXWmj)

**GitHub Issues:** [github.com/bmad-code-org/BMAD-METHOD/issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) (pro jasné chyby)



---

# FILE: docs/cs/how-to/install-bmad.md

---
title: "Jak nainstalovat BMad"
description: Průvodce instalací BMad ve vašem projektu krok za krokem
sidebar:
  order: 1
---

Použijte příkaz `npx bmad-method install` k nastavení BMad ve vašem projektu s výběrem modulů a AI nástrojů.

Pokud chcete použít neinteraktivní instalátor a zadat všechny možnosti na příkazové řádce, podívejte se na [tento návod](./non-interactive-installation.md).

## Kdy to použít

- Začínáte nový projekt s BMad
- Přidáváte BMad do existující kódové báze
- Aktualizujete stávající instalaci BMad

:::note[Předpoklady]
- **Node.js** 20+ (vyžadováno pro instalátor)
- **Git** (doporučeno)
- **AI nástroj** (Claude Code, Cursor nebo podobný)
:::

## Kroky

### 1. Spusťte instalátor

```bash
npx bmad-method install
```

:::tip[Chcete nejnovější prereleaseový build?]
Použijte dist-tag `next`:
```bash
npx bmad-method@next install
```

Získáte novější změny dříve, s vyšší šancí na nestabilitu oproti výchozí instalaci.
:::

:::tip[Bleeding edge]
Pro instalaci nejnovější verze z hlavní větve (může být nestabilní):
```bash
npx github:bmad-code-org/BMAD-METHOD install
```
:::

### 2. Zvolte umístění instalace

Instalátor se zeptá, kam nainstalovat soubory BMad:

- Aktuální adresář (doporučeno pro nové projekty, pokud jste adresář vytvořili sami a spouštíte z něj)
- Vlastní cesta

### 3. Vyberte své AI nástroje

Vyberte, které AI nástroje používáte:

- Claude Code
- Cursor
- Ostatní

Každý nástroj má svůj vlastní způsob integrace skills. Instalátor vytvoří drobné prompt soubory pro aktivaci workflow a agentů — jednoduše je umístí tam, kde je váš nástroj očekává.

:::note[Povolení skills]
Některé platformy vyžadují explicitní povolení skills v nastavení, než se zobrazí. Pokud nainstalujete BMad a nevidíte skills, zkontrolujte nastavení vaší platformy nebo se zeptejte svého AI asistenta, jak skills povolit.
:::

### 4. Zvolte moduly

Instalátor zobrazí dostupné moduly. Vyberte ty, které potřebujete — většina uživatelů chce pouze **BMad Method** (modul pro vývoj softwaru).

### 5. Následujte výzvy

Instalátor vás provede zbytkem — vlastní obsah, nastavení atd.

## Co získáte

```text
váš-projekt/
├── _bmad/
│   ├── bmm/            # Vaše vybrané moduly
│   │   └── config.yaml # Nastavení modulu (pokud byste ho někdy potřebovali změnit)
│   ├── core/           # Povinný základní modul
│   └── ...
├── _bmad-output/       # Generované artefakty
├── .claude/            # Claude Code skills (pokud používáte Claude Code)
│   └── skills/
│       ├── bmad-help/
│       ├── bmad-persona/
│       └── ...
└── .cursor/            # Cursor skills (pokud používáte Cursor)
    └── skills/
        └── ...
```

## Ověření instalace

Spusťte `bmad-help` pro ověření, že vše funguje, a zjistěte, co dělat dál.

**BMad-Help je váš inteligentní průvodce**, který:
- Potvrdí, že vaše instalace funguje
- Ukáže, co je dostupné na základě nainstalovaných modulů
- Doporučí váš první krok

Můžete mu také klást otázky:
```
bmad-help I just installed, what should I do first?
bmad-help What are my options for a SaaS project?
```

## Řešení problémů

**Instalátor vyhodí chybu** — Zkopírujte výstup do svého AI asistenta a nechte ho to vyřešit.

**Instalátor fungoval, ale něco nefunguje později** — Vaše AI potřebuje kontext BMad, aby pomohla. Podívejte se na [Jak získat odpovědi o BMad](./get-answers-about-bmad.md) pro návod, jak nasměrovat AI na správné zdroje.



---

# FILE: docs/cs/how-to/non-interactive-installation.md

---
title: Neinteraktivní instalace
description: Instalace BMad pomocí příznaků příkazové řádky pro CI/CD pipelines a automatizované nasazení
sidebar:
  order: 2
---

Použijte příznaky příkazové řádky k neinteraktivní instalaci BMad. To je užitečné pro:

## Kdy to použít

- Automatizovaná nasazení a CI/CD pipelines
- Skriptované instalace
- Hromadné instalace napříč více projekty
- Rychlé instalace se známými konfiguracemi

:::note[Předpoklady]
Vyžaduje [Node.js](https://nodejs.org) v20+ a `npx` (součástí npm).
:::

## Dostupné příznaky

### Možnosti instalace

| Příznak | Popis | Příklad |
|---------|-------|---------|
| `--directory <cesta>` | Instalační adresář | `--directory ~/projects/myapp` |
| `--modules <moduly>` | Čárkou oddělená ID modulů | `--modules bmm,bmb` |
| `--tools <nástroje>` | Čárkou oddělená ID nástrojů/IDE (použijte `none` pro přeskočení) | `--tools claude-code,cursor` nebo `--tools none` |
| `--action <typ>` | Akce pro existující instalace: `install` (výchozí), `update` nebo `quick-update` | `--action quick-update` |

### Základní konfigurace

| Příznak | Popis | Výchozí |
|---------|-------|---------|
| `--user-name <jméno>` | Jméno, které agenti použijí | Systémové uživatelské jméno |
| `--communication-language <jazyk>` | Jazyk komunikace agentů | English |
| `--document-output-language <jazyk>` | Jazyk výstupních dokumentů | English |
| `--output-folder <cesta>` | Cesta k výstupní složce | _bmad-output |

### Další možnosti

| Příznak | Popis |
|---------|-------|
| `-y, --yes` | Přijmout všechna výchozí nastavení a přeskočit výzvy |
| `-d, --debug` | Povolit ladící výstup pro generování manifestu |

## ID modulů

Dostupná ID modulů pro příznak `--modules`:

- `bmm` — BMad Method Master
- `bmb` — BMad Builder

Zkontrolujte [registr BMad](https://github.com/bmad-code-org) pro dostupné externí moduly.

## ID nástrojů/IDE

Dostupná ID nástrojů pro příznak `--tools`:

**Preferované:** `claude-code`, `cursor`

Spusťte `npx bmad-method install` interaktivně jednou pro zobrazení aktuálního seznamu podporovaných nástrojů, nebo zkontrolujte [konfiguraci kódů platforem](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/cli/installers/lib/ide/platform-codes.yaml).

## Režimy instalace

| Režim | Popis | Příklad |
|-------|-------|---------|
| Plně neinteraktivní | Zadejte všechny příznaky pro přeskočení výzev | `npx bmad-method install --directory . --modules bmm --tools claude-code --yes` |
| Polo-interaktivní | Zadejte některé příznaky; BMad se zeptá na zbytek | `npx bmad-method install --directory . --modules bmm` |
| Pouze výchozí | Přijměte vše výchozí s `-y` | `npx bmad-method install --yes` |
| Bez nástrojů | Přeskočte konfiguraci nástrojů/IDE | `npx bmad-method install --modules bmm --tools none` |

## Příklady

### Instalace v CI/CD pipeline

```bash
#!/bin/bash
# install-bmad.sh

npx bmad-method install \
  --directory "${GITHUB_WORKSPACE}" \
  --modules bmm \
  --tools claude-code \
  --user-name "CI Bot" \
  --communication-language English \
  --document-output-language English \
  --output-folder _bmad-output \
  --yes
```

### Aktualizace existující instalace

```bash
npx bmad-method install \
  --directory ~/projects/myapp \
  --action update \
  --modules bmm,bmb,custom-module
```

### Rychlá aktualizace (zachování nastavení)

```bash
npx bmad-method install \
  --directory ~/projects/myapp \
  --action quick-update
```

## Co získáte

- Plně nakonfigurovaný adresář `_bmad/` ve vašem projektu
- Agenty a workflow nakonfigurované pro vybrané moduly a nástroje
- Složku `_bmad-output/` pro generované artefakty

## Validace a zpracování chyb

BMad validuje všechny zadané příznaky:

- **Adresář** — Musí být platná cesta s oprávněním k zápisu
- **Moduly** — Upozorní na neplatná ID modulů (ale nespadne)
- **Nástroje** — Upozorní na neplatná ID nástrojů (ale nespadne)
- **Vlastní obsah** — Každá cesta musí obsahovat platný soubor `module.yaml`
- **Akce** — Musí být jedna z: `install`, `update`, `quick-update`

Neplatné hodnoty buď:
1. Zobrazí chybu a ukončí se (pro kritické možnosti jako adresář)
2. Zobrazí varování a přeskočí (pro volitelné položky jako vlastní obsah)
3. Přepnou na interaktivní výzvy (pro chybějící povinné hodnoty)

:::tip[Osvědčené postupy]
- Používejte absolutní cesty pro `--directory` pro zamezení nejednoznačnosti
- Otestujte příznaky lokálně před použitím v CI/CD pipelines
- Kombinujte s `-y` pro skutečně bezobslužné instalace
- Použijte `--debug` pokud narazíte na problémy během instalace
:::

## Řešení problémů

### Instalace selže s „Invalid directory“

- Cesta k adresáři musí existovat (nebo musí existovat jeho nadřazený adresář)
- Potřebujete oprávnění k zápisu
- Cesta musí být absolutní nebo správně relativní k aktuálnímu adresáři

### Modul nenalezen

- Ověřte, že ID modulu je správné
- Externí moduly musí být dostupné v registru

:::note[Stále jste uvízli?]
Spusťte s `--debug` pro detailní výstup, zkuste interaktivní režim pro izolaci problému, nebo nahlaste na <https://github.com/bmad-code-org/BMAD-METHOD/issues>.
:::



---

# FILE: docs/cs/how-to/project-context.md

---
title: "Správa kontextu projektu"
description: Vytvoření a údržba project-context.md pro vedení AI agentů
sidebar:
  order: 8
---

Použijte soubor `project-context.md` k zajištění toho, aby AI agenti dodržovali technické preference a pravidla implementace vašeho projektu ve všech workflow. Aby byl vždy dostupný, můžete také přidat řádek `Important project context and conventions are located in [cesta k project context]/project-context.md` do souboru kontextu nebo pravidel vašeho nástroje (jako je `AGENTS.md`).

:::note[Předpoklady]
- BMad Method nainstalován
- Znalost technologického stacku a konvencí vašeho projektu
:::

## Kdy to použít

- Máte silné technické preference před začátkem architektury
- Dokončili jste architekturu a chcete zachytit rozhodnutí pro implementaci
- Pracujete na existující kódové bázi se zavedenými vzory
- Všimnete si, že agenti dělají nekonzistentní rozhodnutí napříč stories

## Krok 1: Vyberte přístup

**Ruční vytvoření** — Nejlepší, když přesně víte, jaká pravidla chcete dokumentovat

**Generování po architektuře** — Nejlepší pro zachycení rozhodnutí učiněných během solutioningu

**Generování pro existující projekty** — Nejlepší pro objevení vzorů v existujících kódových bázích

## Krok 2: Vytvořte soubor

### Možnost A: Ruční vytvoření

Vytvořte soubor na `_bmad-output/project-context.md`:

```bash
mkdir -p _bmad-output
touch _bmad-output/project-context.md
```

Přidejte váš technologický stack a pravidla implementace:

```markdown
---
project_name: 'MyProject'
user_name: 'YourName'
date: '2026-02-15'
sections_completed: ['technology_stack', 'critical_rules']
---

# Project Context for AI Agents

## Technology Stack & Versions

- Node.js 20.x, TypeScript 5.3, React 18.2
- State: Zustand
- Testing: Vitest, Playwright
- Styling: Tailwind CSS

## Critical Implementation Rules

**TypeScript:**
- Strict mode enabled, no `any` types
- Use `interface` for public APIs, `type` for unions

**Code Organization:**
- Components in `/src/components/` with co-located tests
- API calls use `apiClient` singleton — never fetch directly

**Testing:**
- Unit tests focus on business logic
- Integration tests use MSW for API mocking
```

### Možnost B: Generování po architektuře

Spusťte workflow v novém chatu:

```bash
bmad-generate-project-context
```

Workflow skenuje váš dokument architektury a soubory projektu a generuje kontextový soubor zachycující učiněná rozhodnutí.

### Možnost C: Generování pro existující projekty

Pro existující projekty spusťte:

```bash
bmad-generate-project-context
```

Workflow analyzuje vaši kódovou bázi, identifikuje konvence a vygeneruje kontextový soubor, který můžete zkontrolovat a upřesnit.

## Krok 3: Ověřte obsah

Zkontrolujte vygenerovaný soubor a ujistěte se, že zachycuje:

- Správné verze technologií
- Vaše skutečné konvence (ne generické osvědčené postupy)
- Pravidla, která předcházejí běžným chybám
- Vzory specifické pro framework

Ručně upravte pro doplnění chybějícího nebo odstranění nepřesností.

## Co získáte

Soubor `project-context.md`, který:

- Zajistí, že všichni agenti dodržují stejné konvence
- Zabrání nekonzistentním rozhodnutím napříč stories
- Zachytí architektonická rozhodnutí pro implementaci
- Slouží jako reference pro vzory a pravidla vašeho projektu

## Tipy

:::tip[Osvědčené postupy]
- **Zaměřte se na neočividné** — Dokumentujte vzory, které agenti mohou přehlédnout (např. „Použijte JSDoc na každé veřejné třídě“), ne univerzální postupy jako „používejte smysluplné názvy proměnných.“
- **Udržujte to stručné** — Tento soubor načítá každý implementační workflow. Dlouhé soubory plýtvají kontextem. Vylučte obsah, který platí pouze pro úzký rozsah nebo specifické stories.
- **Aktualizujte dle potřeby** — Upravte ručně, když se vzory změní, nebo přegenerujte po významných změnách architektury.
- Funguje pro projekty Quick Flow i plné metody BMad.
:::

## Další kroky

- [**Vysvětlení kontextu projektu**](../explanation/project-context.md) — Zjistěte více o tom, jak to funguje
- [**Mapa pracovních postupů**](../reference/workflow-map.md) — Podívejte se, které workflow načítají kontext projektu
