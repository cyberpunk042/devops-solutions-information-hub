# cline/cline

Source: https://github.com/cline/cline
Ingested: 2026-04-15
Type: documentation

---

# README

<div align="center"><sub>
English | <a href="https://github.com/cline/cline/blob/main/locales/es/README.md" target="_blank">Español</a> | <a href="https://github.com/cline/cline/blob/main/locales/de/README.md" target="_blank">Deutsch</a> | <a href="https://github.com/cline/cline/blob/main/locales/ja/README.md" target="_blank">日本語</a> | <a href="https://github.com/cline/cline/blob/main/locales/zh-cn/README.md" target="_blank">简体中文</a> | <a href="https://github.com/cline/cline/blob/main/locales/zh-tw/README.md" target="_blank">繁體中文</a> | <a href="https://github.com/cline/cline/blob/main/locales/ko/README.md" target="_blank">한국어</a>
</sub></div>

# Cline

<p align="center">
  <img src="https://media.githubusercontent.com/media/cline/cline/main/assets/docs/demo.gif" width="100%" />
</p>

<div align="center">
<table>
<tbody>
<td align="center">
<a href="https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev" target="_blank"><strong>Download on VS Marketplace</strong></a>
</td>
<td align="center">
<a href="https://discord.gg/cline" target="_blank"><strong>Discord</strong></a>
</td>
<td align="center">
<a href="https://www.reddit.com/r/cline/" target="_blank"><strong>r/cline</strong></a>
</td>
<td align="center">
<a href="https://github.com/cline/cline/discussions/categories/feature-requests?discussions_q=is%3Aopen+category%3A%22Feature+Requests%22+sort%3Atop" target="_blank"><strong>Feature Requests</strong></a>
</td>
<td align="center">
<a href="https://docs.cline.bot/getting-started/for-new-coders" target="_blank"><strong>Getting Started</strong></a>
</td>
</tbody>
</table>
</div>

Meet Cline, an AI assistant that can use your **CLI** a**N**d **E**ditor.

Thanks to [Claude Sonnet's agentic coding capabilities](https://www.anthropic.com/claude/sonnet), Cline can handle complex software development tasks step-by-step. With tools that let him create & edit files, explore large projects, use the browser, and execute terminal commands (after you grant permission), he can assist you in ways that go beyond code completion or tech support. Cline can even use the Model Context Protocol (MCP) to create new tools and extend his own capabilities. While autonomous AI scripts traditionally run in sandboxed environments, this extension provides a human-in-the-loop GUI to approve every file change and terminal command, providing a safe and accessible way to explore the potential of agentic AI.

1. Enter your task and add images to convert mockups into functional apps or fix bugs with screenshots.
2. Cline starts by analyzing your file structure & source code ASTs, running regex searches, and reading relevant files to get up to speed in existing projects. By carefully managing what information is added to context, Cline can provide valuable assistance even for large, complex projects without overwhelming the context window.
3. Once Cline has the information he needs, he can:
    - Create and edit files + monitor linter/compiler errors along the way, letting him proactively fix issues like missing imports and syntax errors on his own.
    - Execute commands directly in your terminal and monitor their output as he works, letting him e.g., react to dev server issues after editing a file.
    - For web development tasks, Cline can launch the site in a headless browser, click, type, scroll, and capture screenshots + console logs, allowing him to fix runtime errors and visual bugs.
4. When a task is completed, Cline will present the result to you with a terminal command like `open -a "Google Chrome" index.html`, which you run with a click of a button.

> [!TIP]
> Follow [this guide](https://docs.cline.bot/features/customization/opening-cline-in-sidebar) to open Cline on the right side of your editor. This lets you use Cline side-by-side with your file explorer, and see how he changes your workspace more clearly.

---

<img align="right" width="340" src="https://github.com/user-attachments/assets/3cf21e04-7ce9-4d22-a7b9-ba2c595e88a4">

### Use any API and Model

Cline supports API providers like OpenRouter, Anthropic, OpenAI, Google Gemini, AWS Bedrock, Azure, GCP Vertex, Cerebras and Groq. You can also configure any OpenAI compatible API, or use a local model through LM Studio/Ollama. If you're using OpenRouter, the extension fetches their latest model list, allowing you to use the newest models as soon as they're available.

The extension also keeps track of total tokens and API usage cost for the entire task loop and individual requests, keeping you informed of spend every step of the way.

<!-- Transparent pixel to create line break after floating image -->

<img width="2000" height="0" src="https://github.com/user-attachments/assets/ee14e6f7-20b8-4391-9091-8e8e25561929"><br>

<img align="left" width="370" src="https://github.com/user-attachments/assets/81be79a8-1fdb-4028-9129-5fe055e01e76">

### Run Commands in Terminal

Thanks to the new [shell integration updates in VSCode v1.93](https://code.visualstudio.com/updates/v1_93#_terminal-shell-integration-api), Cline can execute commands directly in your terminal and receive the output. This allows him to perform a wide range of tasks, from installing packages and running build scripts to deploying applications, managing databases, and executing tests, all while adapting to your dev environment & toolchain to get the job done right.

For long running processes like dev servers, use the "Proceed While Running" button to let Cline continue in the task while the command runs in the background. As Cline works he’ll be notified of any new terminal output along the way, letting him react to issues that may come up, such as compile-time errors when editing files.

<!-- Transparent pixel to create line break after floating image -->

<img width="2000" height="0" src="https://github.com/user-attachments/assets/ee14e6f7-20b8-4391-9091-8e8e25561929"><br>

<img align="right" width="400" src="https://github.com/user-attachments/assets/c5977833-d9b8-491e-90f9-05f9cd38c588">

### Create and Edit Files

Cline can create and edit files directly in your editor, presenting you a diff view of the changes. You can edit or revert Cline's changes directly in the diff view editor, or provide feedback in chat until you're satisfied with the result. Cline also monitors linter/compiler errors (missing imports, syntax errors, etc.) so he can fix issues that come up along the way on his own.

All changes made by Cline are recorded in your file's Timeline, providing an easy way to track and revert modifications if needed.

<!-- Transparent pixel to create line break after floating image -->

<img width="2000" height="0" src="https://github.com/user-attachments/assets/ee14e6f7-20b8-4391-9091-8e8e25561929"><br>

<img align="left" width="370" src="https://github.com/user-attachments/assets/bc2e85ba-dfeb-4fe6-9942-7cfc4703cbe5">

### Use the Browser

With Claude Sonnet's new [Computer Use](https://www.anthropic.com/news/3-5-models-and-computer-use) capability, Cline can launch a browser, click elements, type text, and scroll, capturing screenshots and console logs at each step. This allows for interactive debugging, end-to-end testing, and even general web use! This gives him autonomy to fixing visual bugs and runtime issues without you needing to handhold and copy-pasting error logs yourself.

Try asking Cline to "test the app", and watch as he runs a command like `npm run dev`, launches your locally running dev server in a browser, and performs a series of tests to confirm that everything works. [See a demo here.](https://x.com/sdrzn/status/1850880547825823989)

<!-- Transparent pixel to create line break after floating image -->

<img width="2000" height="0" src="https://github.com/user-attachments/assets/ee14e6f7-20b8-4391-9091-8e8e25561929"><br>

<img align="right" width="350" src="https://github.com/user-attachments/assets/ac0efa14-5c1f-4c26-a42d-9d7c56f5fadd">

### "add a tool that..."

Thanks to the [Model Context Protocol](https://github.com/modelcontextprotocol), Cline can extend his capabilities through custom tools. While you can use [community-made servers](https://github.com/modelcontextprotocol/servers), Cline can instead create and install tools tailored to your specific workflow. Just ask Cline to "add a tool" and he will handle everything, from creating a new MCP server to installing it into the extension. These custom tools then become part of Cline's toolkit, ready to use in future tasks.

-   "add a tool that fetches Jira tickets": Retrieve ticket ACs and put Cline to work
-   "add a tool that manages AWS EC2s": Check server metrics and scale instances up or down
-   "add a tool that pulls the latest PagerDuty incidents": Fetch details and ask Cline to fix bugs

<!-- Transparent pixel to create line break after floating image -->

<img width="2000" height="0" src="https://github.com/user-attachments/assets/ee14e6f7-20b8-4391-9091-8e8e25561929"><br>

<img align="left" width="360" src="https://github.com/user-attachments/assets/7fdf41e6-281a-4b4b-ac19-020b838b6970">

### Add Context

**`@url`:** Paste in a URL for the extension to fetch and convert to markdown, useful when you want to give Cline the latest docs

**`@problems`:** Add workspace errors and warnings ('Problems' panel) for Cline to fix

**`@file`:** Adds a file's contents so you don't have to waste API requests approving read file (+ type to search files)

**`@folder`:** Adds folder's files all at once to speed up your workflow even more

<!-- Transparent pixel to create line break after floating image -->

<img width="2000" height="0" src="https://github.com/user-attachments/assets/ee14e6f7-20b8-4391-9091-8e8e25561929"><br>

<img align="right" width="350" src="https://github.com/user-attachments/assets/140c8606-d3bf-41b9-9a1f-4dbf0d4c90cb">

### Checkpoints: Compare and Restore

As Cline works through a task, the extension takes a snapshot of your workspace at each step. You can use the 'Compare' button to see a diff between the snapshot and your current workspace, and the 'Restore' button to roll back to that point.

For example, when working with a local web server, you can use 'Restore Workspace Only' to quickly test different versions of your app, then use 'Restore Task and Workspace' when you find the version you want to continue building from. This lets you safely explore different approaches without losing progress.

<!-- Transparent pixel to create line break after floating image -->

<img width="2000" height="0" src="https://github.com/user-attachments/assets/ee14e6f7-20b8-4391-9091-8e8e25561929"><br>

## Contributing

To contribute to the project, start with our [Contributing Guide](CONTRIBUTING.md) to learn the basics. You can also join our [Discord](https://discord.gg/cline) to chat with other contributors in the `#contributors` channel. If you're looking for full-time work, check out our open positions on our [careers page](https://cline.bot/join-us)!

## Enterprise

Get the same Cline experience with enterprise-grade controls: SSO (SAML/OIDC), global policies and configuration, observability with audit trails, private networking (VPC/private link), and self-hosted or on-prem deployments, and enterprise support. Learn more at our [enterprise page](https://cline.bot/enterprise) or [talk to us](https://cline.bot/contact-sales).


## License

[Apache 2.0 © 2026 Cline Bot Inc.](./LICENSE)



> **Deep fetch: 30 key files fetched beyond README.**



---

# FILE: .agents/skills/create-pull-request/SKILL.md

---
name: create-pull-request
description: Create a GitHub pull request following project conventions. Use when the user asks to create a PR, submit changes for review, or open a pull request. Handles commit analysis, branch management, PR template usage, and PR creation using the gh CLI tool.
---

# Create Pull Request

This skill guides you through creating a well-structured GitHub pull request that follows project conventions and best practices.

## Prerequisites Check

Before proceeding, verify the following:

### 1. Check if `gh` CLI is installed

```bash
gh --version
```

If not installed, inform the user:
> The GitHub CLI (`gh`) is required but not installed. Please install it:
> - macOS: `brew install gh`
> - Other: https://cli.github.com/

### 2. Check if authenticated with GitHub

```bash
gh auth status
```

If not authenticated, guide the user to run `gh auth login`.

### 3. Verify clean working directory

```bash
git status
```

If there are uncommitted changes, ask the user whether to:
- Commit them as part of this PR
- Stash them temporarily
- Discard them (with caution)

## Gather Context

### 1. Identify the current branch

```bash
git branch --show-current
```

Ensure you're not on `main` or `master`. If so, ask the user to create or switch to a feature branch.

### 2. Find the base branch

```bash
git remote show origin | grep "HEAD branch"
```

This is typically `main` or `master`.

### 3. Analyze recent commits relevant to this PR

```bash
git log origin/main..HEAD --oneline --no-decorate
```

Review these commits to understand:
- What changes are being introduced
- The scope of the PR (single feature/fix or multiple changes)
- Whether commits should be squashed or reorganized

### 4. Review the diff

```bash
git diff origin/main..HEAD --stat
```

This shows which files changed and helps identify the type of change.

## Information Gathering

Before creating the PR, you need the following information. Check if it can be inferred from:
- Commit messages
- Branch name (e.g., `fix/issue-123`, `feature/new-login`)
- Changed files and their content

If any critical information is missing, use `ask_followup_question` to ask the user:

### Required Information

1. **Related Issue Number**: Look for patterns like `#123`, `fixes #123`, or `closes #123` in commit messages
2. **Description**: What problem does this solve? Why were these changes made?
3. **Type of Change**: Bug fix, new feature, breaking change, refactor, cosmetic, documentation, or workflow
4. **Test Procedure**: How was this tested? What could break?

### Example clarifying question

If the issue number is not found:
> I couldn't find a related issue number in the commit messages or branch name. What GitHub issue does this PR address? (Enter the issue number, e.g., "123" or "N/A" for small fixes)

## Git Best Practices

Before creating the PR, consider these best practices:

### Commit Hygiene

1. **Atomic commits**: Each commit should represent a single logical change
2. **Clear commit messages**: Follow conventional commit format when possible
3. **No merge commits**: Prefer rebasing over merging to keep history clean

### Branch Management

1. **Rebase on latest main** (if needed):
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Squash if appropriate**: If there are many small "WIP" commits, consider interactive rebase:
   ```bash
   git rebase -i origin/main
   ```
   Only suggest this if commits appear messy and the user is comfortable with rebasing.

### Push Changes

Ensure all commits are pushed:
```bash
git push origin HEAD
```

If the branch was rebased, you may need:
```bash
git push origin HEAD --force-with-lease
```

## Create the Pull Request

**IMPORTANT**: Read and use the PR template at `.github/pull_request_template.md`. The PR body format must **strictly match** the template structure. Do not deviate from the template format.

When filling out the template:
- Replace `#XXXX` with the actual issue number, or keep as `#XXXX` if no issue exists (for small fixes)
- Fill in all sections with relevant information gathered from commits and context
- Mark the appropriate "Type of Change" checkbox(es)
- Complete the "Pre-flight Checklist" items that apply

### Create PR with gh CLI

**Use a temporary file for the PR body** to avoid shell escaping issues, newline problems, and other command-line flakiness:

1. Write the PR body to a temporary file:
   ```
   /tmp/pr-body.md
   ```

2. Create the PR using the file:
   ```bash
   gh pr create --title "PR_TITLE" --body-file /tmp/pr-body.md --base main
   ```

3. Clean up the temporary file:
   ```bash
   rm /tmp/pr-body.md
   ```

For draft PRs:
```bash
gh pr create --title "PR_TITLE" --body-file /tmp/pr-body.md --base main --draft
```

**Why use a file?** Passing complex markdown with newlines, special characters, and checkboxes directly via `--body` is error-prone. The `--body-file` flag handles all content reliably.

## Post-Creation

After creating the PR:

1. **Display the PR URL** so the user can review it
2. **Remind about CI checks**: Tests and linting will run automatically
3. **Suggest next steps**:
   - Add reviewers if needed: `gh pr edit --add-reviewer USERNAME`
   - Add labels if needed: `gh pr edit --add-label "bug"`

## Error Handling

### Common Issues

1. **No commits ahead of main**: The branch has no changes to submit
   - Ask if the user meant to work on a different branch

2. **Branch not pushed**: Remote doesn't have the branch
   - Push the branch first: `git push -u origin HEAD`

3. **PR already exists**: A PR for this branch already exists
   - Show the existing PR: `gh pr view`
   - Ask if they want to update it instead

4. **Merge conflicts**: Branch conflicts with base
   - Guide user through resolving conflicts or rebasing

## Summary Checklist

Before finalizing, ensure:
- [ ] `gh` CLI is installed and authenticated
- [ ] Working directory is clean
- [ ] All commits are pushed
- [ ] Branch is up-to-date with base branch
- [ ] Related issue number is identified, or placeholder is used
- [ ] PR description follows the template exactly
- [ ] Appropriate type of change is selected
- [ ] Pre-flight checklist items are addressed


---

# FILE: CHANGELOG.md

# Changelog

## [3.78.0]

### Added

- Add a dedicated "Spend Limit Reached" error UI when spend caps are hit
- Docs updates

### Fixed

- Show actual `read_file` line ranges in chat UI

## [3.77.0]

### Added

- Add "Lazy Teammate Mode" experimental toggle
- `read_file` tool now supports chunked reading for targeted file access

### Fixed

- Exclude `new_task` tool from system prompt in yolo/headless mode
- Fix Kanban demo video formatting

### Changed

- Polish `Notification` hook functionality

## [3.76.0]

### Added

- Add Cline Kanban launch modal in webview; CLI now launches Kanban by default with a migration view
- Add toggle to disable feature tips in chat
- Add repeated tool call loop detection to prevent infinite loops wasting tokens

### Fixed

- Fix CLI Kanban spawn on Windows by enabling shell mode for `npx.cmd`

## [3.75.0]

### Added

- Latency improvements for remote workspaces

### Fixed

- Stabilize flaky hooks tests

### Changed

- Remove example hooks in favor of reading the docs

## [3.74.0]

### Added
- Implement dynamic free model detection for Cline API
- Add file read deduplication cache to prevent repeated reads
- Add feature tips tooltip during thinking state

### Fixed
- Replace error message when not logged in to Cline
- Align ClineRulesToggleModal padding with ServersToggleModal
- Skip WebP for GLM and Devstral models running through llama.cpp
- Respect user-configured context window in LiteLLM getModel()
- Honor explicit model IDs outside static catalog in W&B provider
- Add missing Fireworks serverless models and pricing

## [3.73.0]

### Added

- Added W&B Inference by CoreWeave as a new API provider with 17 models
- Improved parallel tool calling support for OpenRouter and Cline providers

### Fixed

- Claude Code Provider: handle rate limit events, empty content arrays, error results, and unknown content types without crashing
- Tool handlers (`read_file`, `list_files`, `list_code_definition_names`, `search_files`) now return graceful errors instead of crashing

## [3.72.0]

### Added

- Added Anthropic Opus 4.6 fast mode variants

### Fixed

- Resolved native tool placeholder interpolation in prompts
- Gemini: capped Flash output tokens to 8192 across providers
- Fixed Windows unit test path normalization
- Fixed flaky hooks tests on Windows
- Bedrock: handle thinking and redacted_thinking blocks correctly in message conversion and streaming
- Prevent crash when `list_files` or `list_code_definition_names` receives a file path

### Changed

- Updated Jupyter Notebook GIFs
- Markdown image loading now requires user consent
- Added `.github/copilot-instructions.md` for coding agents
- Hooks: reintroduced feature toggle

## [3.71.0]

### Added

- Added GPT-5.4 models for ChatGPT subscription users
- Hooks: Added a `Notification` hook for attention and completion boundaries

### Fixed

- Handle streamable HTTP MCP reconnects more reliably after disconnects

## [3.70.0]

### Added

- New Cline API docs: Getting Started, Auth, Chat Completions, Models, Errors, and SDK Examples
- Hook payloads now include `model.provider` and `model.slug` 
- Token/cost updates now happen immediately as usage chunks arrive, not after tool execution

### Fixed

- Improve subagent context compaction logic
- Subagent stream retry delay increased to reduce noise from transient failures
- State serialization errors are now caught and logged instead of crashing
- Removed incorrect `max_tokens` from OpenRouter requests

### Changed

- Windows test cleanup now retries on locked files and applies per-test timeouts
- Updated hooks docs 


## [3.69.0]

### Added

- Add `User-Agent` header to requests sent to the Cline backend
- Add default auto-tag workflow for publish release flow
- Show Cline SDK docs on the Cline page

### Fixed

- Retry nested git restore and prevent silent `.git_disabled` leftovers in checkpoints
- Prevent Chinese filename escaping in diff view
- Trigger auto-compaction on OpenRouter context overflow errors
- Restore GPT-OSS native file editing on OpenAI-compatible models

### Changed

- Update Cline SDK docs
- Improve hooks support for Windows PowerShell

## [3.68.0]

### Added

- Add dynamic Cline provider model fetching from Cline endpoint
- Add additional Markdown formatting in CLI
- Add focus indicator on action buttons in extension

### Fixed

- Clear all OCA secrets on auth refresh failure to prevent re-auth loops
- Resolve "Could not find the file context" error in Explain Changes
- Use `JSON_SCHEMA` for `yaml.load` to prevent unsafe deserialization
- Fetch model info from API in CLI headless auth for Cline and Vercel providers
- Generate commit message from staged changes only when staging exists
- Update stale `maxTokens` values for Claude 3.7+ models across Anthropic, Bedrock, Vertex, and SAP AI Core
- Use `model.info.maxTokens` for OpenRouter instead of hardcoded `8192`

### Changed

- Increase timeout for a flaky test to reduce short-term test instability

## [3.67.1]

### Added

- Added Cline SDK API interface for programmatic access to Cline features and tools, enabling integration into custom applications.
- Added Codex 5.3 model support

### Fixed

- Fix OpenAI Codex by setting `store` to `false`
- Use `isLocatedInPath()` instead of string matching for path containment checks

## [3.67.0]

### Added

- Add support for skills and optional modelId in subagent configuration
- Add AgentConfigLoader for file-based agent configs
- Add Responses API support for OpenAI native provider
- Preconnect websocket to reduce response latency
- Fetch featured models from backend with local fallback
- Add /q command to quit CLI
- Add MCP enterprise configuration details
- Pull Cline's recommended models from internal endpoint
- Add dynamic flag to adjust banner cache duration

### Fixed

- Fix reasoning delta crash on usage-only stream chunks
- Fix OpenAI tool ID transformation restricted to native provider only
- Fix auth check for ACP mode
- Fix CLI yolo mode to not persist yolo setting to disk
- Fix inline focus-chain slider within its feature row
- Fix Gemini 3.1 Pro compatibility
- Fix Cline auth with ACP flag

### Changed

- Move PR skill to .agents/skills
- SambaNova provider: update models list
- Remove changeset-converter GitHub Action and npm run changeset

## [3.66.0]

### Added

- Gemini-3.1 Pro Preview


## [3.65.0]

### Added

- Add /skills slash command to CLI for viewing and managing installed skills

### Fixed

- Fix aggressive context compaction caused by accidental clicks on the context window progress bar silently setting a very low auto-condense threshold
- Fix infinite retry loop when write_to_file fails with missing content parameter.
- Fixed default claude model

## [3.64.0]

### Added
- Added sonnet 4.6


## [3.63.0]

### Added

- added zai GLM 5 Free promo

### Fixed

- Restore reasoning trace visibility in chat and improve the thinking row UX so reasoning is visible, then collapsible after completion.

## [3.62.0]

### Fixed

- Banners now display immediately when opening the extension instead of requiring user interaction first
- Resolved 17 security vulnerabilities including high-severity DoS issues in dependencies (body-parser, axios, qs, tar, and others)

## [3.61.0]

- UI/UX fixes with minimax model family

## [3.60.0]

- Fixes for Minimax model family

## [3.59.0]

- Added Minimax 2.5 Free Promo
- Fixed Response chaining for OpenAI's Responses API

## [3.58.0]

### Added

- Subagent: replace legacy subagents with the native `use_subagents` tool
- Bundle `endpoints.json` support so packaged distributions can ship required endpoints out-of-the-box
- Amazon Bedrock: support parallel tool calling
- New "double-check completion" experimental feature to verify work before marking tasks complete
- CLI: new task controls/flags including custom `--thinking` token budget and `--max-consecutive-mistakes` for yolo runs
- Remote config: new UI/options (including connection/test buttons) and support for syncing deletion of remotely configured MCP servers
- Vertex / Claude Code: add 1M context model options for Claude Opus 4.6
- ZAI/GLM: add GLM-5

### Fixed

- CLI: handle stdin redirection correctly in CI/headless environments
- CLI: preserve OAuth callback paths during auth redirects
- VS Code Web: generate auth callback URLs via `vscode.env.asExternalUri` (OAuth callback reliability)
- Terminal: surface command exit codes in results and improve long-running `execute_command` timeout behavior
- UI: add loading indicator and fix `api_req_started` rendering
- Task streaming: prevent duplicate streamed text rows after completion
- API: preserve selected Vercel model when model metadata is missing
- Telemetry: route PostHog networking through proxy-aware shared fetch and ensure telemetry flushes on shutdown
- CI: increase Windows E2E test timeout to reduce flakiness

### Changed

- Settings/model UX: move "reasoning effort" into model configuration and expose it in settings
- CLI provider selection: limit provider list to those remotely configured
- UI: consolidate ViewHeader component/styling across views
- Tools: add auto-approval support for `attempt_completion` commands
- Remotely configured MCP server schema now supports custom headers

## [3.57.1]

### Fixed

- Fixed Opus 4.6 for bedrock provider

## [3.57.0]

### Added

- Cline CLI 2.0 now available. Install with `npm install -g cline`
- Anthopic Opus 4.6
- Minimax-2.1 and Kimi-k2.5 now available for free for a limited time promo
- Codex-5.3 through ChatGPT subscription

### Fixed

- Fix read file tool to support reading large files
- Fix decimal input crash in OpenAI Compatible price fields (#8129)
- Fix build complete handlers when updating the api config
- Fixed missing provider from list
- Fixed Favorite Icon / Star from getting clipped in the task history view

### Changed

- Make skills always enabled and remove feature toggle setting

## [3.56.0]

### Added

- **CLI authentication:** Added Vercel AI Gateway and Cline API key provider support for headless CI/automation workflows
- **New model:** Added Kimi-K2.5 model to Moonshot provider (262K context, image support, prompt caching)
- **Prompt variant:** Added Trinity Large prompt variant for improved tool-calling support
- **OpenTelemetry:** Added support for custom headers on metrics and logs endpoints
- **Social links:** Added community icons (X, Discord, GitHub, Reddit, LinkedIn) to the What's New modal

### Fixed

- **LiteLLM:** Fixed thinking configuration not appearing for reasoning-capable models
- **OpenTelemetry:** Fixed endpoint path handling (no longer incorrectly appends `/v1/logs` or `/v1/metrics`) and ensured logs are sent regardless of VSCode telemetry settings
- **CLI auth:** Fixed `cline auth` displaying incorrect provider information after configuration

### Changed

- **Hooks:** Hook scripts now run from the workspace repository root instead of filesystem root
- **Default settings:** Enabled multi-root workspaces, parallel tool calling, and skills by default; disabled strict plan mode by default
- **Settings UI:** Refreshed feature settings section with collapsible design

## [3.55.0]

- Add new model: Arcee Trinity Large Preview
- Add new model: Moonshot Kimi K2.5
- Add MCP prompts support - prompts from connected MCP servers now appear in slash command autocomplete as `/mcp:<server>:<prompt>`

## [3.54.0]

### Added

- Native tool calls support for Ollama provider
- Sonnet 4.5 is now the default Amazon Bedrock model id

### Fixed

- Prevent infinite retry loops when replace_in_file fails repeatedly. The system now detects repeated failures and provides better guidance to break out of retry cycles.
- Skip diff error UI handling during streaming to prevent flickering. Error handling is deferred until streaming completes.
- Strip notebook cell outputs when extracting text content from Jupyter notebooks, significantly reducing context size sent to the LLM.
- Throttle diff view updates during streaming to reduce UI flickering and improve performance.

### Changed

- Removed Mistral's Devstral-2512 free from the free models list
- Removed deprecated zai-glm-4.6 model from Cerebras provider

## [3.53.1]

### Fixed

- Bug in responses API

## [3.53.0]

### Fixed

- Removed grok model from free tier

## [3.52.0]

### Added

- Users with ChatGPT Plus or Pro subscriptions can now use GPT-5 models directly through Cline without needing an API key. Authentication is handled via OAuth through OpenAI's authentication system.
- Grok models are now moving out of free tier and into paid plans.
- Introduces comprehensive Jupyter Notebook support for Cline, enabling AI-assisted editing of `.ipynb` files with full cell-level context awareness.

### Fixed

- Bugs in DiffViewProvider for file editing
- Ollama's recommended models to use correct identifiers

## [3.51.0]

### Added

- Adding OpenAI gpt-5.2-codex model to the model picker

## [3.50.0]

### Added

- Add gpt-5.2-codex OpenAI model support
- Add create-pull-request skill

### Fixed

- Fix the selection of remotely configured providers
- Fix act_mode_respond to prevent consecutive calls
- Fix invalid tool call IDs when switching between model formats

## [3.49.1]

### Added

- Add telemetry to track usage of skills feature
- Add version headers to Cline backend requests
- Phase in Responses API usage instead of defaulting for every supported model

### Fixed

- Fix workflow slash command search to be case-insensitive
- Fix model display in ModelPickerModal when using LiteLLM
- Fix LiteLLM model fetching with default base URL
- Fix crash when OpenAI-compatible APIs send usage chunks with empty or null choices arrays at end of streaming
- Fix model ID for Kat Coder Pro Free model

## [3.49.0]

- Enable configuring an OTEL collector at runtime
- Removing Minimax-2.1 from free model list as the free trial has ended
- Improved image display in MCP responses
- Auto-sync remote MCP servers from remote config to local settings

## [3.48.0]

### Added

- Add Skills system for reusable, on-demand agent instructions
- Add new websearch tooling in Cline provider
- Add zai-glm-4.7 to Cerebras model list
- Add model refresh and improve reasoning support for Vercel AI Gateway

### Fixed

- Revert #8341 due to regressions in diff view/document truncation (see #8423, #8429)
- Fixed extension crash when using context menu selector

## [3.47.0]

### Added

- Added experimental support for Background Edits (allows editing files in background without opening the diff view)
- Updated free model to MiniMax M2.1 (replacing MiniMax M2)
- Added support for Azure based identity authentication in OpenAI Compatible provider and Azure OpenAI
- Add `supportsReasoning` property to Baseten models

### Fixed

- Prevent expired token usage in authenticated requests
- Exclude binary files without extensions from diffs
- Preserve file endings and trailing newlines
- Fix Cerebras rate limiting
- Fix Auto Compact for Claude Code provider
- Make Workspace and Favorites history filters independent
- Fix remote MCP server connection failures (404 response handling)
- Disable native tool calling for Deepseek 3.2 speciale
- Show notification instead of opening sidebar on update
- Fix Baseten model selector

### Refactored

- Modify prompts for parallel tool usage in Claude and Gemini 3 models

## [3.46.1]

### Fixed

- Remove GLM 4.6 from free models

## [3.46.0]

### Added

- Added GLM 4.7 model
- Enhanced background terminal execution with command tracking, log file output, zombie process prevention (10-minute timeout), and clickable log paths in UI
- Apply Patch tool for GPT-5+ models (replacing current diff edit tools)

### Fixed

- Duplicate error messages during streaming for Diff Edit tool when Parallel Tool Calling is not enabled
- Banner carousel styling and dismiss functionality
- Typos in Gemini system prompt overrides
- Model picker favorites ordering, star toggle, and keyboard navigation for OpenRouter and Vercel AI Gateway providers
- Fetch remote config values from the cache

### Refactored

- Anthropic handler to use metadata for reasoning support
- Bedrock provider to use metadata for reasoning support

## [3.45.1]

- Fixed MCP settings race condition where toggling auto-approve or changing timeout settings would cause the UI to flash and revert

## [3.45.0]

- Added Gemini 3 Flash Preview model

## [3.44.2]

- Polished the model picker UI with checkmarks for selected models, tooltips on Plan/Act tabs, and consistent arrow pointers across all popup modals
- Improved WhatsNew modal responsiveness and cleaned up redundant UI elements
- Fixed GLM models outputting garbled text in thinking tags—reasoning is now properly disabled for these models

## [3.44.1]

- Fixed a critical bug where local MCP servers stopped connecting after v3.42.0—all user-configured stdio-based MCP servers should now work again
- Fixed remotely configured API keys not being extracted correctly for enterprise users
- Added support for dynamic tool instructions that adapt based on runtime context, laying groundwork for future context-aware features

## [3.44.0]

## Added

- Updating minor version to show a proper banner for the release

## [3.43.1]

### Patch Changes

- Fix GLM-4.6 Model reference id

## [3.43.0]

### Added

- GLM-4.6
- kat-coder-pro
- Add parsing of env variable patterns to the mcpconfig.json

### Fixed

- TLS Proxy support issues for VSCode
- Add supportsReasoning flag to OpenAI reasoning models
- Fix thinking not available for some models in the OpenAI provider
- Fix invalid signature field issues when switching between Gemini and Anthropic providers
- Extract OpenRouter model filtering into reusable utility and use it in different model pickers
- Fix a11y for auto approve checkbox
- Improve ModelPickerModal provider list layout

### Refactored

- Migrate WhatsNewModal to new shared dialogue component

## [3.42.0]

### Added

- Expose `getAvailableSlashCommands` rpc endpoint to UI clients
- Made slash command menu and context menu accessible and screenreader-friendly
- Made expanding/collapsing UI components accessible

### Fixed

- Devstral OpenRouter model ID and routing issues
- Incorrect pricing display for Devstral model in the extension

## [3.41.0]

### Added

- OpenAI GPT-5.2
- Devstral-2512 (formerly stealth model "Microwave")
- Improvements to chat modal model picker
- Amazon Nova 2 Lite
- DeepSeek 3.2 to native tool calling allow list
- Responses API support for Codex models in OpenAI provider (requires native tool calling)
- Xmas Special Santa Cline
- Welcome screen UI enhancements

### Fixed

- Initial checkpoint commit now non-blocking for improved responsiveness in large repositories
- Gemini Vertex models erroring when thinking parameters are not supported
- Restrictive file permissions for secrets.json
- Ollama streaming requests not aborting when task is cancelled

### Refactored

- OpenAI provider to centralize temperature configuration and include missing GPT-5 model settings
- OpenAI native handler to use metadata for model capabilities
- Vertex provider to use metadata for model capabilities

## [3.40.2]

- Fix logout on network errors during token refresh (e.g., opening laptop while offline)

## [3.40.1]

- Fix cost calculation display for Anthropic API requests

## [3.40.0]

- Fix highlighted text flashing when task header is collapsed
- Add X-Cerebras-3rd-Party-Integration header to Cerebras API requests
- Add microwave family system prompt configuration
- Remove tooltips from auto approve menu
- Fix Standalone, ensure cwd is the install dir to find resources reliably
- Fix a bug where terminal commands with double quotes are broken when "Terminal Execution Mode" is set to "Background Exec"
- Add support for slash commands anywhere in a message, not just at the beginning. This matches the behavior of @ mentions for a more flexible input experience.
- Add bottom padding to the last message to fix last response text getting cut off by auto approve settings bar.
- Add default thinking level for Gemini 3 Pro models in Gemini provider

## [3.39.2]

- Fix for microwave model and thinking settings

## [3.39.1]

- Fix Openrouter and Cline Provider model info

## [3.39.0]

- Add Explain Changes feature
- Add microwave Stealth model
- Add Tabbed Model Picker with Recommended and Free tabs
- Add support to View remote rules and workflows in the editor
- Enable NTC (Native Tool Calling) by default
- Bug fixes and improvements for LiteLLM provider

## [3.38.3]

- Task export feature now opens the task directory, allowing easy access to the full task files
- Add Grok 4.1 and Grok Code to XAI provider
- Enabled native tool calling for Baseten and Kimi K2 models
- Add thinking level to Gemini 3.0 Pro preview
- Expanded Hooks functionality
- Removed Task Timeline from Task Header
- Bug fix for slash commands
- Bug fixes for Vertex provider
- Bug fixes for thinking/reasoning issues across multiple providers when using native tool calling
- Bug fixes for terminal usage on Windows devices

## [3.38.2]

- Add Claude Opus 4.5

## [3.38.1]

### Fixed

- Fixed handling of 'signature' field in sanitizeAnthropicContentBlock to properly preserve it when thinking is enabled, as required by Anthropic's API.

## [3.38.0]

### Added

- Gemini 3 Pro Preview model
- AquaVoice Avalon model for voice-to-text dictation

### Fixed

- Automatic context truncation when AWS Bedrock token usage rate limits are exceeded
- Removed new_task tool from system prompts, updated slash command prompts, and added helper function for native tool calling validation

## [3.37.1]

- Comprehensive changes to better support GPT 5.1 - System prompt, tools, deep-planning, focus chain, etc.
- Add AGENTS.md support
- feat(models): Add free minimax/mimax-m2 model to the model picker

## [3.37.0]

### Added

- GPT-5.1 with model-specific prompting: tailored system prompts, tool usage, focus chain, and deep-planning optimizations
- Nous Research provider with Hermes 4 model family and custom system prompts
- Switched to Aqua Voice's Avalon model in speech to text transcription
- Added Linux support for speech to text
- Model-family breakouts for deep-planning prompting, laying groundwork for enhanced slash commands
- Expanded HTTP proxy support throughout the codebase
- Improved focus chain prompting for frontier models (Anthropic, OpenAI, Gemini, xAI)

### Fixed

- Duplicate tool results prevention through existence checking
- XML entity escaping in model content processor
- Commit message generation in command palette
- OpenAI Compatible provider temperature parameter type conversion

## Documentation

- Added missing proto generation step in CONTRIBUTING.md
- New `npm run dev` script for streamlined terminal workflow (fixes #7335)

## [3.36.1]

- fix: remove native tool calling support from Gemini and XAI provider due to invalid tool names issues
- fix: disable native tool callings for grok code models
- Add MCP tool usage to GLM
- Removes reasoning_details content field from Anthropic providers

## [3.36.0]

- Add: Hooks allow you to inject custom logic into Cline's workflow
- Add: new provider AIhubmix
- Add: Use http_proxy, https_proxy and no_proxy in JetBrains
- Fix: Oca Token Refresh logic
- Fix: issues where assistant message with empty content is added to conversation history
- Fix: bug where the checkbox shows in the model selector dropdown
- Fix: Switch from defaultUserAgentProvider to customUserAgent for Bedrock
- Fix: support for `<think>` tags for better compatibility with open-source models
- Fix: refinements to the GLM-4.6 system prompt

## [3.35.1]

- Add: Hicap API integration as provider
- Fix: enable Add Header button in OpenAICompatibleProvider UI
- Fix: Remove orphaned tool_results after truncation and empty content field issues in native tool call
- Fix: render model description in markdown

## [3.35.0]

- Add native tool calling support with configurable setting.
- Auto-approve is now always-on with a redesigned expanding menu. Settings simplified and notifications moved to General Settings.
- added zai-glm-4.6 as a Cerebras model
- Created GPT5 family specific system prompt template
- Fix: show reasoning budget slider to models with valid thinking config
- Requesty base URL, and API key fixes
- Delete all Auth Tokens when logging out
- Support for <think> tags for models that prefer that over <thinking>

## [3.34.1]

- Added support for MiniMax provider with MiniMax-M2 model
- Remove Cline/code-supernova-1-million model
- Changes to allow users to manually enter model names (eg. presets) when using OpenRouter

## [3.34.0]

- Cline Teams is now free through 2025 for unlimited users. Includes Jetbrains, RBAC, centralized billing and more.
- Use the “exacto” versions of GLM-4.6, Kimi-K2, and Qwen3-Coder in the Cline provider for the best balance of cost, speed, accuracy and tool-calling.

## [3.33.1]

- Fix CLI installation copy text

## [3.33.0]

- Added Cline CLI (Preview)
- Added Subagent support (Experimental)
- Added Multi-Root Workspaces support (Enable in feature settings)
- Add auto-retry with exponential backof for failed API requests

## [3.32.8]

- Add Claude Haiku 4.5 support

## [3.32.7]

- Add JP and Global inference profile options to AWS Bedrock
- Adding Improvements to VSCode multi root workspaces
- Added markdown support to focus chain text, allowing the model to display more interesting focus chains

## [3.32.6]

- Add experimental support for VSCode multi root workspaces
- Add Claude Sonnet 4.5 to Claude Code provider
- Add Glm 4.6 to Z AI provider

## [3.32.5]

- Improve thinking budget slider UI to take up less space
- Fix Vercel provider cost note and sign-up url
- Fix repeated API error 400 in SAP AI Core provider
- Add us-west-1 to Amazon Bedrock regions
- Fix OCA provider refresh logic

## [3.32.4]

- Add 1m context window support to Claude Sonnet 4.5
- Add Claude Sonnet 4.5 to GCP Vertex
- Add prompt caching support for OpenRouter accidental `anthropic/claude-4.5-sonnet` model ID

## [3.32.3]

- Add Claude Sonnet 4.5 to Bedrock provider
- Add Alert banner for new Claude Sonnet 4.5 model

## [3.32.2]

- Add Claude Sonnet 4.5 to Cline/OpenRouter/Anthropic providers
- Add /task deep link handler

## [3.32.1]

- Preserve reasoning traces for Cline/OpenRouter/Anthropic providers to maintain conversation integrity
- Add automatically retry on rate limit errors with SAP AI Core provider
- Fix Cline accounts using stale id token at refresh response
- Minor UI improvements to Settings and Task Header

## [3.32.0]

- Added the new code-supernova-1-million stealth model, available for free and delivering a 1 million token context window
- Changes to inform Cline about commands that are available on your system

## [3.31.1]

- Version bump

## [3.31.0]

- UI Improvements: New task header and focus chain design to take up less space for a cleaner experience
- Voice Mode: Experimental feature that must be enabled in settings for hands-free coding
- YOLO Mode: Enable in settings to let Cline approve all actions and automatically switch between plan/act mode
- Fix Oracle Code Assist provider issues

## [3.30.3]

- Add Oracle Code Assist provider

## [3.30.2]

- Fix UI tests

## [3.30.1]

- Fix model list not being updated in time for user to use shortcut button to update model to stealth model
- Fix flicker issue when switching modes
- Fix Sticky header in settings view overlaping with content on scroll
- Add experimental yolo mode feature that disables all user approvals and automatically executes a task and navigates through plan to act mode until the task is complete

## [3.30.0]

- Add code-supernova stealth model

## [3.29.2]

- Fix: Reverted change that caused formatting issues
- Fix: Moonshot - Pass max_tokens value to provider

## [3.29.1]

- Changeset bump + Announcement banner update

## [3.29.0]

- Updated Baseten provider to fetch models from server
- Fix: Updated insufficient balance URL for easy Cline balance top-ups
- Accessibility: Improvements to screen readers in MCP, Cline Rules, workflows, and history views.

## [3.28.4]

- Fix bug where some Windows machines had API request hanging
- Fix bug where 'Proceed while running' action button would be disabled after running an interactive command
- Fix prompt cache info not being displayed in History

## [3.28.3]

- Fixed issue with start new task button
- Feature to generate commit message for staged changes, with unstaged as fallback

## [3.28.2]

- Fix for focus chain settings

## [3.28.1]

- Requesty: use base URL to get models and API keys
- Removed focus chain feature flag

## [3.28.0]

- Synchronized Task History: Real-time task history synchronization across all Cline instances
- Optimized GPT-5 Integration: Fine-tuned system prompts for improved performance with GPT-5 model family
- Deep Planning Improvements: Optimized prompts for Windows/PowerShell environments and dependency exclusion
- Streamlined UI Experience: ESC key navigation, cleaner approve/reject buttons, and improved editor panel focus
- Smart Provider Search: Improved search functionality in API provider dropdown for faster model selection
- Added per-provider thinking tokens configurability
- Added Ollama custom prompt options
- Enhanced SAP AI Core Provider: Orchestration mode support and improved model visibility
- Added Dify.ai API Integration
- SambaNova Updates: Added DeepSeek-V3.1 model
- Better Gemini rate limit handling
- OpenAI Reasoning Effort: Minimal reasoning effort configuration for OpenAI models
- Fixed LiteLLM Caching: Anthropic caching compatibility when using LiteLLM
- Fixed Ollama default endpoint connections
- Fixed AutoApprove menu overflow
- Fixed extended thinking token issue with Anthropic models
- Fixed issue with slash commands removing text from prompt

## [3.27.2]

- Remove `grok-code-fast-1` promotion deadline

## [3.27.1]

- Add new Kimi K2 model to groq and moonshot providers

## [3.27.0]

- Fix `grok-code-fast-1` model information
- Add call to action for trying free `grok-code-fast-1` in Announcement banner

## [3.26.7]

- Add 200k context window variant for Claude Sonnet 4 to OpenRouter and Cline providers

## [3.26.6]

- Add free Grok Coder model to Cline provider for users looking for a fast, free coding model option
- Fix GPT-5 models not respecting auto-compact setting when enabled, improving context window management
- Fix provider retry attempts not showing proper user feedback during rate limiting scenarios
- Improve markdown and code block styling to automatically adapt when switching VS Code themes

## [3.26.5]

- fix (provider/vercel-ai-gateway): reduce model list load frequency in settings view
- Fix OVSX publish command to resolve deployment failure

## [3.26.4]

- Update nebius ai studio models
- Update sap provider - support reasoning effort for open ai models
- Fix Claude 4 image input in SAP AI Core Provider

## [3.26.3]

- Add compact system prompt option for LM Studio and Ollama models, optimized for smaller context windows (8k or less)
- Add token usage tracking for LM Studio models to better monitor API consumption
- Add "Use compact prompt" checkbox in LM Studio provider settings
- Fix "Unexpected API Response" bug with gpt-5

## [3.26.2]

- Improve OpenRouter model parsing to show reasoning budget sliders for all models that support thinking, not just Claude models
- Fix OpenRouter context window error handling to properly extract error codes from error messages, resolving "Unexpected API Response" errors with GPT-5 on Cline provider
- Fix GPT-5 context window configuration for OpenAI/OpenRouter/Cline providers to use correct 272K limit
- Remove max tokens configuration from Sonic Alpha model
- Add Go language support to deep-planning feature (Thanks @yuvalman!)
- Fix typo in Focus Chain settings page (Thanks @joyceerhl!)

## [3.26.1]

- Add Vercel AI Gateway as a new API provider option (Thanks @joshualipman123!)
- Improve SAP AI Core provider to show deployed and undeployed models in the UI (Thanks @yuvalman!)
- Fix Fireworks provider configuration and functionality (Thanks @ershang-fireworks!)
- Add telemetry tracking for MCP tool usage to help improve the extension
- Improve telemetry tracking for rules and workflow usage analytics
- Set Plan mode to use strict mode by default for better planning results

## [3.26.0]

- Add Z AI as a new API provider with GLM-4.5 and GLM-4.5 Air models, offering competitive performance with cost-effective pricing especially for Chinese language tasks (Thanks @jues!)
- Add Cline Sonic Alpha model - experimental advanced model with 262K context window for complex coding tasks
- Add support for LM Studio local models from v0 API endpoint with configurable max tokens
- Fix Ollama context window configuration not being used in requests

## [3.25.3]

- Fix bug where 'Enable checkpoints' and 'Disable MCP Marketplace' settings would be reset to default on reload
- Move the position of the focus chain edit button when a scrollbar is present. Make the pencil icon bigger and better centered.

## [3.25.2]

- Fix attempt_completion showing twice in chat due to partial logic not being handled correctly
- Fix OpenRouter showing cline credits error after 402 response

## [3.25.1]

- Fix attempt_completion command showing twice in chat view when updating progress checklist
- Fix bug where announcement banner could not be dismissed
- Add GPT-OSS models to AWS Bedrock

## [3.25.0]

- **Focus Chain:** Automatically creates and maintains todo lists as you work with Cline, breaking down complex tasks into manageable steps with real-time progress tracking
- **Auto Compact:** Intelligently manages conversation context to prevent token limit errors by automatically compacting older messages while preserving important context
- **Deep Planning:** New `/deep-planning` slash command for structured 4-step implementation planning that integrates with Focus Chain for automatic progress tracking
- Add support for 200k context window for Claude Sonnet 4 in OpenRouter and Cline providers
- Add option to configure custom base URL for Requesty provider

## [3.24.0]

- Add OpenAI GPT-5 Chat(gpt-5-chat-latest)
- Add custom browser arguments setting to allow passing flags to the Chrome executable for better headless compatibility.
- Add 1m context window model support for claude sonnet 4
- Fis the API Keys URL for Requesty
- Set gpt5 max tokens to 8_192 to fix 'context window exceeded' error
- Fix issue where fallback request to retrieve cost was not using correct auth token
- Add OpenAI context window exceeded error handling
- Calibrate input token counts when using anthropic models of sap ai core provider

## [3.23.0]

- Add caching support for Bedrock inferences using SAP AI Core and minor refactor
- Improve visibility for mode switch background color on different themes
- Fix terminal commands putting webview in blocked state

## [3.22.0]

- Implemented a retry strategy for Cerebras to handle rate limit issues due to its generation speed
- Add support for GPT-5 models to SAP AI Core Provider
- Support sending context to active webview when editor panels are opened.
- Fix bug where running out of credits on Cline accounts would show '402 empty body' response instead of 'buy credits' component
- Fix LiteLLM Proxy Provider Cost Tracking

## [3.21.0]

- Add support for GPT-5 model family including GPT-5, GPT-5 Mini, and GPT-5 Nano with prompt caching support and set GPT-5 as the new default model
- Add "Take a Tour" button for new users to easily access the VSCode walkthrough and improve onboarding experience
- Enhance plan mode response handling with better exploration parameter support

## [3.20.13]

- Fix prompt caching support for Opus 4.1 on OpenRouter/Cline

## [3.20.12]

- Add Claude Opus 4.1 model support to AWS Bedrock provider (Thanks @omercelik!)
- Fix prompt caching and extended thinking support for Claude Opus 4.1 in Anthropic provider

## [3.20.11]

Add gpt-oss-120b as a Cerebras model
Add Opus 4.1 through Claude Code

## [3.20.10]

- Add OpenAI's new open-source models (GPT-OSS-120B and GPT-OSS-20B) to Hugging Face and Groq providers

## [3.20.9]

- Add support for Claude Opus 4.1 model in Anthropic provider
- Add Baseten as a new API provider with support for DeepSeek, Llama, and Kimi K2 models (Thanks @AlexKer!)
- Fix error messages not clearing from UI when retrying failed tasks
- Fix chat input box positioning issues

## [3.20.8]

- Add navbar tooltips on hover

## [3.20.7]

- Fix circular dependency that affect the github workflow Tests / test (pull_request)

## [3.20.6]

- Fix login check on extension restart

## [3.20.5]

- Fix authentication persistence issues that could cause users to be logged out unexpectedly

## [3.20.4]

- Add new Cerebras models
- Update rate limits for existing Cerebras models
- Fix for delete task dialog

## [3.20.3]

- Add Huawei Cloud MaaS Provider (Thanks @ddling!)
- Add Cerebras Qwen 3 235B instruct model (Thanks @kevint-cerebras!)
- Add DeepSeek R1 0528 support under Hugging Face (Thanks @0ne0rZer0!)
- Fix Global Rules directory documentation for Linux/WSL systems
- Fix token counting when using VSCode LM API provider
- Fix input field stealing focus issue by only focusing on visible and active editor panels
- Fix duplicate tool registration for claude4-experimental
- Trim input value for URL fields

## [3.20.2]

- Fixed issue with sap ai core client credentials storage
- Fix Qwen Api option inconsistency between UI and API layer
- Fix credit balance out of sync issue on account switching
- Fix Claude Code CLAUDE_CODE_MAX_OUTPUT_TOKENS
- Fix cursor state after restoring files to be disabled after checked out
- Fix issue where checkpointing blocked UI

## [3.20.1]

- Fix for files being deleted when switching modes or closing tasks

## [3.20.0]

- Add account balance display for all organization members, allowing non-admin users to view their organization's credit balance and add credits

## [3.19.8]

- Add Claude Code support on Windows with improved system prompt handling to fix E2BIG errors (Thanks @BarreiroT!)
- Improve Cerebras provider with updated model selection (Qwen and Llama 3.3 70B only) and increased context window for Qwen 3 32B from 16K to 64K tokens
- Improve Cerebras Qwen model performance by removing thinking tokens from model input
- Add robust checkpoint timeout handling with early warning at 7 seconds and timeout at 15 seconds to prevent hanging on large repositories
- Fix MCP servers incorrectly starting when disabled in configuration (Thanks @mohanraj-r!)
- Refactor Git commit message generation with streaming support and improved module organization
- Fix settings navigation to open correct tab when accessing from checkpoint warnings

## [3.19.7]

- Add Hugging Face as a new API provider with support for their inference API models
- Improve Claude Code error messages with better guidance for common setup issues (Thanks @BarreiroT!)
- Fix authentication sync issues when using multiple VSCode windows

## [3.19.6]

- Improve Kimi K2 model provider routing with additional provider options for better availability and performance
- Fixed terminal bug where Cline failed to capture output of certain fast-running commands
- Fixed bug with increasing auto approved number of requests not resetting the counter mid-task

## [3.19.5]

- Add Groq as a new API provider with support for all Groq models including Kimi-K2
- Add user role display in organization UI for Cline account users
- Fix message dialogs not showing option buttons properly
- Fix authentication issues when using multiple VSCode windows

## [3.19.4]

- Add ability to choose Chinese endpoint for Moonshot provider

## [3.19.3]

- Add Moonshot AI provider

## [3.19.2]

- Show request ID in error messages returned by Cline Accounts API to help debug user reported issues

## [3.19.1]

- Fix documentation

## [3.19.0]

- Add Kimi-K2 as a recommended model in the Cline Provider, and route to Together/Groq for 131k context window and high throughput
- Added API Key support for Bedrock integration

## [3.18.14]

- Fix bug where Cline account users logged in with invalid token would not be shown as logged out in webview presentation layer

## [3.18.13]

- Fix authentication issue where Cline accounts users would keep getting logged out or seeing 'Unexpected API response' errors

## [3.18.12]

- Fix flaky organization switching behavior in Cline provider that caused UI inconsistencies and double loading
- Fix insufficient credits error display to properly show error messages when account balance is too low
- Improve credit balance validation and error handling for Cline provider requests

## [3.18.11]

- Fix authentication issues with Cline provider by ensuring the client always uses the latest auth token

## [3.18.10]

- Update recommended fast & cheap model to Grok 4 in OpenRouter model picker
- Fix Gemini 2.5 Pro thinking budget slider and add support for Gemini 2.5 Flash Lite Preview model (Thanks @arafatkatze!)

## [3.18.9]

- Fix streaming reliability issues with Cline provider that could cause connection problems during long conversations
- Fix authentication error handling for Cline provider to show clearer error messages when not signed in and prevent recursive failed requests
- Remove incorrect pricing display for SAP AI Core provider since it uses non-USD "Capacity Units" that cannot be directly converted (Thanks @ncryptedV1!)

## [3.18.8]

- Update pricing for Grok 3 model because the promotion ended

## [3.18.7]

- Remove promotional "free" messaging for Grok 3 model in UI

## [3.18.6]

- Update request header to include `"ai-client-type": "Cline"` to SAP Api Provider
- Add organization accounts

## [3.18.5]

- Fix Plan/Act mode persistence across sessions and multi-workspace conflicts
- Improve provider switching performance by 18x (from 550ms to 30ms) with batched storage operations
- Improve SAP AI Core provider model organization and fix exception handling (Thanks @schardosin!)

## [3.18.4]

- Add support for Gemini 2.5 Pro and Flash to SAP AI Core Provider
- Fix logging in with Cline account not getting past welcome screen

## [3.18.3]

- Improve Cerebras Qwen model performance by removing thinking tokens from model input (Thanks @kevint-cerebras!)
- Improve Claude Code provider with better error handling and performance optimizations (Thanks @BarreiroT!)

## [3.18.2]

- Fix issue where terminal output would not be captured if shell integration fails by falling back to capturing the terminal content.
- Add confirmation popup when deleting tasks
- Add support for Claude Sonnet 4 and Opus 4 model in SAP AI Core provider (Thanks @lizzzcai!)
- Add support for `litellm_session_id` to group requests in a single session (Thanks @jorgegarciarey!)
- Add "Thinking Budget" customization for Claude Code (Thanks @BarreiroT!)
- Fix issue where the extension would use the user's environment variables for authentication when using Claude Code (Thanks @BarreiroT!)

## [3.18.1]

- Add support for Claude 4 Sonnet in SAP AI Core provider (Thanks @GTxx!)
- Fix ENAMETOOLONG error when using Claude Code provider with long conversation histories (Thanks @BarreiroT!)
- Remove Gemini CLI provider because Google asked us to
- Fix bug with "Delete All Tasks" functionality

## [3.18.0]

- Optimized Cline to work with the Claude 4 family of models, resulting in improved performance, reliability, and new capabilities
- Added a new Gemini CLI provider that allows you to use your local Gemini CLI authentication to access Gemini models for free (Thanks @google-gemini!)
- Optimized Cline to work with the Gemini 2.5 family of models
- Updated the default and recommended model to Claude 4 Sonnet for the best performance
- Fix race condition in Plan/Act mode switching
- Improve robustness of search and replace parsing

## [3.17.16]

- Fix Claude Code provider error handling for incomplete messages during long-running tasks (Thanks @BarreiroT!)
- Add taskId as metadata to LiteLLM API requests for better request tracing (Thanks @jorgegarciarey!)

## [3.17.15]

- Fix LiteLLM provider to properly respect selected model IDs when switching between Plan and Act modes (Thanks @sammcj!)
- Fix chat input being cleared when switching between Plan/Act modes without sending a message (Thanks @BarreiroT!)
- Fix MCP server name display to avoid showing "undefined" for SSE servers, preventing tool/resource invocation failures (Thanks @ramybenaroya!)
- Fix AWS Bedrock provider by removing deprecated custom model encoding (Thanks @watany-dev!)
- Fix timeline tooltips for followup messages and improve color retrieval code (Thanks @char8x!)
- Improve accessibility by making task header buttons properly announced by screen readers (Thanks @yncat!)
- Improve accessibility by adding proper state reporting for Plan/Act mode switch for screen readers (Thanks @yncat!)
- Prevent reading development environment variables from user's environment (Thanks @BarreiroT!)

## [3.17.14]

- Add Claude Code as a new API provider, allowing integration with Anthropic's Claude Code CLI tool and Claude Max Plan (Thanks @BarreiroT!)
- Add SAP AI Core as a new API provider with support for Claude and GPT models (Thanks @schardosin!)
- Add configurable default terminal profile setting, allowing users to specify which terminal Cline should use (Thanks @valinha!)
- Add terminal output size constraint setting to limit how much terminal output is processed
- Add MCP Rich Display settings to the settings page for persistent configuration (Thanks @Vl4diC0de!)
- Improve copy button functionality with refactored reusable components (Thanks @shouhanzen!)
- Improve AWS Bedrock provider by removing deprecated dependency and using standard AWS SDK (Thanks @watany-dev!)
- Fix list_files tool to properly return files when targeting hidden directories
- Fix search and replace edge case that could cause file deletion, making the algorithm more lenient for models using different diff formats
- Fix task restoration issues that could occur when resuming interrupted tasks
- Fix checkpoint saving to properly track all file changes
- Improve file context warnings to reduce diff edit errors when resuming restored tasks
- Clear chat input when switching between Plan/Act modes within a task
- Exclude .clinerules files from checkpoint tracking

## [3.17.13]

- Add Thinking UX for Gemini models, providing visual feedback during model reasoning
- Add support for Notifications MCP integration with Cline
- Add prompt caching indicator for Grok 3 models
- Sort MCP marketplace by newest listings by default for easier discovery of recent servers
- Update O3 model family pricing to reflect latest OpenAI rates
- Remove '-beta' suffix from Grok model identifiers
- Fix AWS Bedrock provider by removing deprecated Anthropic-Bedrock SDK (Thanks @watany-dev!)
- Fix menu display issue for terminal timeout settings
- Improve chat input field styling and behavior

## [3.17.12]

- **Free Grok Model Available!** Access Grok 3 completely free through the Cline provider
- Add collapsible MCP response panels to keep conversations focused on the main AI responses while still allowing access to detailed MCP output (Thanks @valinha!)
- Prioritize active files (open tabs) at the top of the file context menu when using @ mentions (Thanks @abeatrix!)
- Fix context menu to properly default to "File" option instead of incorrectly selecting "Git Commits"
- Fix diff editing to handle out-of-order SEARCH/REPLACE blocks, improving reliability with models that don't follow strict ordering
- Fix telemetry warning popup appearing repeatedly for users who have telemetry disabled

## [3.17.11]

- Add support for Gemini 2.5 Pro Preview 06-05 model to Vertex AI and Google Gemini providers

## [3.17.10]

- Add support for Qwen 3 series models with thinking mode options (Thanks @Jonny-china!)
- Add new AskSage models: Claude 4 Sonnet, Claude 4 Opus, GPT 4.1, Gemini 2.5 Pro (Thanks @swhite24!)
- Add VSCode walkthrough to help new users get started with Cline
- Add support for streamable MCP servers
- Improve Ollama model selection with filterable dropdown instead of radio buttons (Thanks @paulgear!)
- Add setting to disable aggressive terminal reuse to help users experiencing task lockout issues
- Fix settings dialog applying changes even when cancel button is clicked

## [3.17.9]

- Aligning Cline to work with Claude 4 model family (Experimental)
- Add task timeline scrolling feature
- Add support for uploading CSV and XLSX files for data analysis and processing
- Add stable Grok-3 models to xAI provider (grok-3, grok-3-fast, grok-3-mini, grok-3-mini-fast) and update default model from grok-3-beta to grok-3 (Thanks @PeterDaveHello!)
- Add new models to Vertex AI provider
- Add new model to Nebius AI Studio
- Remove hard-coded temperature from LM Studio API requests and add support for reasoning_content in LM Studio responses
- Display delay information when retrying API calls for better user feedback
- Fix AWS Bedrock credential caching issue where externally updated credentials (e.g., by AWS Identity Manager) were not detected, requiring extension restart (Thanks @DaveFres!)
- Fix search tool overloading conversation with massive outputs by setting maximum byte limit for responses
- Fix checkpoints functionality
- Fix token counting for xAI provider
- Fix Ollama provider issues
- Fix window title display for Windows users
- Improve chat box UI

## [3.17.8]

- Fix bug where terminal would get stuck and output "capture failure"

## [3.17.7]

- Fix diff editing reliability for Claude 4 family models by adding constraints to prevent errors with large replacements

## [3.17.6]

- Add Cerebras as a new API provider with 5 high-performance models including reasoning-capable models (Thanks @kevint-cerebras!)
- Add support for uploading various file types (XML, JSON, TXT, LOG, MD, DOCX, IPYNB, PDF) alongside images
- Add improved onboarding experience for new users with guided setup
- Add prompt cache indicator for Gemini 2.5 Flash models
- Update SambaNova provider with new model list and documentation links (Thanks @luisfucros!)
- Fix diff editing support for Claude 4 family of models
- Improve telemetry and analytics for better user experience insights

## [3.17.5]

- Fix issue with Claude 4 models where after several conversation turns, it would start making invalid diff edits

## [3.17.4]

- Fix thinking budget slider for Claude 4

## [3.17.3]

- Fix diff edit errors with Claude 4 models

## [3.17.2]

- Add support for Claude 4 models (Sonnet 4 and Opus 4) in AWS Bedrock and Vertex AI providers
- Add support for global workflows, allowing workflows to be shared across workspaces with local workflows taking precedence
- Fix settings page z-index UI issues that caused display problems
- Fix AWS Bedrock environment variable handling to properly restore process.env after API calls (Thanks @DaveFres!)

## [3.17.1]

- Add prompt caching for Claude 4 models on Cline and OpenRouter providers
- Increase max tokens for Claude Opus 4 from 4096 to 8192

## [3.17.0]

- Add support for Anthropic Claude Sonnet 4 and Claude Opus 4 in both Anthropic and Vertex providers
- Add integration with Nebius AI Studio as a new provider (Thanks @Aktsvigun!)
- Add custom highlight and hotkey suggestion when the assistant prompts to switch to Act mode
- Update settings page design, now split into tabs for easier navigation (Thanks Yellow Bat @dlab-anton, and Roo Team!)
- Fix MCP Server configuration bug
- Fix model listing for Requesty provider
- Move all advanced settings to settings page

## [3.16.3]

- Add devstral-small-2505 to the Mistral model list, a new specialized coding model from Mistral AI (Thanks @BarreiroT!)
- Add documentation links to rules & workflows UI
- Add support for Streameable HTTP Transport for MCPs (Thanks @alejandropta!)
- Improve error handling for Mistral SDK API

## [3.16.2]

- Add support for Gemini 2.5 Flash Preview 05-20 model to Vertex AI provider with massive 1M token context window (Thanks @omercelik!)
- Add keyboard shortcut (Cmd+') to quickly focus Cline from anywhere in VS Code
- Add lightbulb actions for selected text with options to "Add to Cline", "Explain with Cline", and "Improve with Cline"
- Automatically focus Cline window after extension updates

## [3.16.1]

- Add Enable auto approve toggle switch, allowing users to easily turn auto-approve functionality on or off without losing their action settings
- Improve Gemini retry handling with better UI feedback, showing retry progress during API request attempts
- Fix memory leak issue that could occur during long sessions with multiple tasks
- Improve UI for Gemini model retry attempts with clearer status updates
- Fix quick actions functionality in auto-approve settings
- Update UI styling for auto-approve menu items to conserve space

## [3.16.0]

- Add new workflow feature allowing users to create and manage workflow files that can be injected into conversations via slash commands
- Add collapsible recent task list, allowing users to hide their task history when sharing their screen (Thanks @cosmix!)
- Add global endpoint option for Vertex AI users, providing higher availability and reducing 429 errors (Thanks @soniqua!)
- Add detection for new users to display special components and guidance
- Add Tailwind CSS IntelliSense to the recommended extensions list
- Fix eternal loading states when the last message is a checkpoint (Thanks @BarreiroT!)
- Improve settings organization by migrating VSCode Advanced settings to Settings Webview

## [3.15.5]

- Fix inefficient memory management in the task timeline
- Fix Gemini rate limitation response not being handled properly (Thanks @BarreiroT!)

## [3.15.4]

- Add gemini model back to vertex provider
- Add gemini telemetry
- Add filtering for tasks tied to the current workspace

## [3.15.3]

- Add Fireworks API Provider
- Fix minor visual issues with auto-approve menu
- Fix one instance of terminal not getting output
- Fix 'Chrome was launched but debug port is not responding' error

## [3.15.2]

- Added details to auto approve menu and more sensible default controls
- Add detailed configuration options for LiteLLM provider
- Add webview telemetry for users who have opted in to telemetry
- Update Gemini in OpenRouter/Cline providers to use implicit caching
- Fix freezing issues during rendering of large streaming text
- Fix grey screen webview crashes by releasing memory after every diff edit
- Fix breaking out of diff auto-scroll
- Fix IME composition Enter auto‑sending edited message

## [3.15.1]

- Fix bug where PowerShell commands weren't given enough time before giving up and showing an error

## [3.15.0]

- Add Task Timeline visualization to tasks (Thanks eomcaleb!)
- Add cache to ui for OpenAi provider
- Add FeatureFlagProvider service for the Node.js extension side
- Add copy buttons to task header and assistant messages
- Add a more simplified home header was added
- Add ability to favorite a task, allowing it to be kept when clearing all tasks
- Add npm script for issue creation (Thanks DaveFres!)
- Add confirmation dialog to Delete All History button
- Add ability to allow the user to type their next message into the chat while Cline is taking action
- Add ability to generate commit message via cline (Thanks zapp88!)
- Add improvements to caching for gemini models on OpenRouter and Cline providers
- Add improvements to allow scrolling the file being edited.
- Add ui for windsurf and cursor rules
- Add mistral medium-3 model
- Add option to collect events to send them in a bundle to avoid sending too many events
- Add support to quote a previous message in chat
- Add support for Gemini Implicit Caching
- Add support for batch selection and deletion of tasks in history (Thanks danix800!)
- Update change suggested models
- Update fetch cache details from generation endpoint
- Update converted docs to Mintlify
- Update the isOminiModel to include o4-mini model (Thanks PeterDaveHello!)
- Update file size that can be read by Cline, allowing larger files
- Update defaults for bedrock API models (Thanks Watany!)
- Update to extend ReasoningEffort to non-o3-mini reasoning models for all providers (Thanks PeterDaveHello!)
- Update to give error when a user tries to upload an image larger than 7500x7500 pixels
- Update announcement so that previous updates are in a dropdown
- Update UI for auto approve with favorited settings
- Fix bug where certain terminal commands would lock you out of a task
- Fix only initialize posthog in the webview if the user has opted into telemetry
- Fix bug where autocapture was on for front-end telemetry
- Fix for markdown copy excessively escaping characters (Thanks weshoke!)
- Fix an issue where loading never finished when using an application inference profile for the model ID (Thanks WinterYukky!)

## [3.14.1]

- Disables autocaptures when initializing feature flags

## [3.14.0]

- Add support for custom model ID in AWS Bedrock provider, enabling use of Application Inference Profile (Thanks @clicube!)
- Add more robust caching & cache tracking for gemini & vertex providers
- Add support for LaTeX rendering
- Add support for custom API request timeout. Timeouts were 15-30s, but can now be configured via settings for OpenRouter/Cline & Ollama (Thanks @WingsDrafterwork!)
- Add truncation notice when truncating manually
- Add a timeout setting for the terminal connection, allowing users to set a time to wait for terminal startup
- Add copy button to code blocks
- Add copy button to markdown blocks (Thanks @weshoke!)
- Add checkpoints to more messages
- Add slash command to create a new rules file (/newrule)
- Add cache ui for open router and cline provider
- Add Amazon Nova Premier model to Bedrock (Thanks @watany!)
- Add support for cursorrules and windsurfrules
- Add support for batch history deletion (Thanks @danix800!)
- Improve Drag & Drop experience
- Create clinerules folder when creating new rule if it's needed
- Enable pricing calculation for gemini and vertex providers
- Refactor message handling to not show the MCP View of the server modal
- Migrate the addRemoteServer to protobus (Thanks @DaveFres!)
- Update task header to be expanded by default
- Update Gemini cache TTL time to 15 minutes
- Fix race condition in terminal command usage
- Fix to correctly handle `import.meta.url`, avoiding leading slash in pathname for Windows (Thanks @DaveFres!)
- Fix @withRetry() decoration syntax error when running extension locally (Thanks @DaveFres!)
- Fix for git commit mentions in repos with no git commits
- Fix cost calculation (Thanks @BarreiroT!)

## [3.13.3]

- Add download counts to MCP marketplace items
- Add `/compact` command
- Add prompt caching to gemini models in cline / openrouter providers
- Add tooltips to bottom row menu

## [3.13.2]

- Add Gemini 2.5 Flash model to Vertex and Gemini Providers (Thanks monotykamary!)
- Add Caching to gemini provider (Thanks arafatkatze!)
- Add thinking budget support to Gemini Models (Thanks monotykamary!)
- Add !include .file directive support for .clineignore (Thanks watany-dev!)
- Improve slash command functionality
- Improve prompting for new task tool
- Fix o1 temperature being passed to the azure api (Thanks treeleaves30760!)
- Fix to make "add new rule file" button functional
- Fix Ollama provider timeout, allowing for a larger loading time (Thanks suvarchal!)
- Fix Non-UTF-8 File Handling: Improve Encoding Detection to Prevent Garbled Text and Binary Misclassification (Thanks yt3trees!)
- Fix settings to not reset by changing providers
- Fix terminal outputs missing commas
- Fix terminal errors caused by starting non-alphanumeric outputs
- Fix auto approve settings becoming unset
- Fix Mermaid syntax error in documentation (Thanks tuki0918!)
- Remove supportsComputerUse restriction and support browser use through any model that supports images (Thanks arafatkatze!)

## [3.13.1]

- Fix bug where task cancellation during thinking stream would result in error state

## [3.13.0]

- Add Cline rules popover under the chat field, allowing you to easily add, enable & disable workspace level or global rule files
- Add new slash command menu letting you type “/“ to do quick actions like creating new tasks
- Add ability to edit past messages, with options to restore your workspace back to that point
- Allow sending a message when selecting an option provided by the question or plan tool
- Add command to jump to Cline's chat input
- Add support for OpenAI o3 & 4o-mini (Thanks @PeterDaveHello and @arafatkatze!)
- Add baseURL option for Google Gemini provider (Thanks @owengo and @olivierhub!)
- Add support for Azure's DeepSeek model. (Thanks @yt3trees!)
- Add ability for models that support it to receive image responses from MCP servers (Thanks @rikaaa0928!)
- Improve search and replace diff editing by making it more flexible with models that fail to follow structured output instructions. (Thanks @chi-cat!)
- Add detection of Ctrl+C termination in terminal, improving output reading issues
- Fix issue where some commands with large output would cause UI to freeze
- Fix token usage tracking issues with vertex provider (Thanks @mzsima!)
- Fix issue with xAI reasoning content not being parsed (Thanks @mrubens!)

## [3.12.3]

- Add copy button to MermaidBlock component (Thanks @cacosub7!)
- Add the ability to fetch from global cline rules files
- Add icon to indicate when a file outside of the users workspace is edited

## [3.12.2]

- Add gpt-4.1

## [3.12.1]

- Use visual checkpoint indicator to make it clear when checkpoints are created
- Big shoutout to @samuel871211 for numerous code quality improvements, refactoring contributions, and webview performance improvements!
- Use improved context manager

## [3.12.0]

- Add favorite toggles for models when using the Cline & OpenRouter providers
- Add auto-approve options for edits/reads outside of the workspace
- Improve diff editing animation for large files
- Add indicator showing number of diff edits when Cline edits a file
- Add streaming support and reasoning effort option to xAI's Grok 3 Mini
- Add settings button to MCP popover to easily modify installed servers
- Fix bug where browser tool actions would show unparsed results in the chat view
- Fix issue with new checkpoints popover hiding too quickly
- Fix duplicate checkpoints bug
- Improve Ollama provider with retry mechanism, timeout handling, and improved error handling (thanks suvarchal!)

## [3.11.0]

- Redesign checkpoint UI to declutter chat view by using a subtle indicator line that expands to a popover on hover, with a new date indicator for when it was created
- Add support for xAI's provider's Grok 3 models
- Add more robust error tracking for users opted in to telemetry (thank you for helping us make Cline better!)

## [3.10.1]

- Add CMD+' keyboard shortcut to add selected text to Cline
- Cline now auto focuses the text field when using 'Add to Cline' shortcut
- Add new 'Create New Task' tool to let Cline start a new task autonomously!
- Fix Mermaid diagram issues
- Fix Gemini provider cost calculation to take new tiered pricing structure into account

## [3.10.0]

- Add setting to let browser tool use local Chrome via remote debugging, enabling session-based browsing. Replaces sessionless Chromium, unlocking debugging and productivity workflows tied to your real browser state.
- Add new auto-approve option to approve _ALL_ commands (use at your own risk!)
- Add modal in the chat area to more easily enable or disable MCP servers
- Add drag and drop of file/folders into cline chat (Thanks eljapi!)
- Add prompt caching for LiteLLM + Claude (Thanks sammcj!)
- Add Improved context management
- Fix MCP auto approve toggle issues being out of sync with settings

## [3.9.2]

- Add recommended models for Cline provider
- Add ability to detect when user edits files manually so Cline knows to re-read, leading to reduced diff edit errors
- Add improvements to file mention searching for faster searching
- Add scoring logic to file mentions to sort and exclude results based on relevance
- Add Support for Bytedance Doubao (Thanks Tunixer!)
- Fix to prevent duplicate BOM (Thanks bamps53!)

## [3.9.1]

- Add Gemini 2.5 Pro Preview 03-25 to Google Provider

## [3.9.0]

- Add Enable extended thinking for LiteLLM provider (Thanks @jorgegarciarey!)
- Add a tab for configuring local MCP Servers
- Fix issue with DeepSeek API provider token counting + context management
- Fix issues with checkpoints hanging under certain conditions

## [3.8.6]

- Add UI for adding remote servers
- Add Mentions Feature Guide and update related documentation
- Fix bug where menu would open in sidebar and open tab
- Fix issue with Cline accounts not showing user info in popout tabs
- Fix bug where menu buttons wouldn't open view in sidebar

## [3.8.5]

- Add support for remote MCP Servers using SSE
- Add gemini-2.5-pro-exp-03-25 to Vertex AI (thanks @arri-cc!)
- Add access to history, mcp, and new task buttons in popout view
- Add task feedback telemetry (thumbs up/down on task completion)
- Add toggle disabled for remote servers
- Move the MCP Restart and Delete buttons and add an auto-approve all toggle
- Update Requestly UX for model selection (thanks @arafatkatze!)
- Add escape for html content for gemini when running commands
- Improve search and replace edit failure behaviors

## [3.8.4]

- Add Sambanova Deepseek-V3-0324
- Add cost calculation support for LiteLLM provider
- Fix bug where Cline would use plan_mode_response bug without response parameter

## [3.8.3]

- Add support for SambaNova QwQ-32B model
- Add OpenAI "dynamic" model chatgpt-4o-latest
- Add Amazon Nova models to AWS Bedrock
- Improve file handling for NextJS folder naming (fixes issues with parentheses in folder names)
- Add Gemini 2.5 Pro to Google AI Studio available models
- Handle "input too large" errors for Anthropic
- Fix "See more" not showing up for tasks after task un-fold
- Fix gpt-4.5-preview's supportsPromptCache value to true

## [3.8.2]

- Fix bug where switching to plan/act would result in VS Code LM/OpenRouter model being reset

## [3.8.0]

- Add 'Add to Cline' as an option when you right-click in a file or the terminal, making it easier to add context to your current task
- Add 'Fix with Cline' code action - when you see a lightbulb icon in your editor, you can now select 'Fix with Cline' to send the code and associated errors for Cline to fix. (Cursor users can also use the 'Quick Fix (CMD + .)' menu to see this option)
- Add Account view to display billing and usage history for Cline account users. You can now keep track of credits used and transaction history right in the extension!
- Add 'Sort underling provider routing' setting to Cline/OpenRouter allowing you to sort provider used by throughput, price, latency, or the default (combination of price and uptime)
- Improve rich MCP display with dynamic image loading and support for GIFs
- Add 'Documentation' menu item to easily access Cline's docs
- Add OpenRouter's new usage_details feature for more reliable cost reporting
- Display total space Cline takes on disk next to 'Delete all Tasks' button in History view
- Fix 'Context Window Exceeded' error for OpenRouter/Cline Accounts (additional support coming soon)
- Fix bug where OpenRouter model ID would be set to invalid value
- Add button to delete MCP servers in a failure state

## [3.7.1]

- Fix issue with 'See more' button in task header not showing when starting new tasks
- Fix issue with checkpoints using local git commit hooks

## [3.7.0]

- Cline now displays selectable options when asking questions or presenting a plan, saving you from having to type out responses!
- Add support for a `.clinerules/` directory to load multiple files at once (thanks @ryo-ma!)
- Prevent Cline from reading extremely large files into context that would overload context window
- Improve checkpoints loading performance and display warning for large projects not suited for checkpoints
- Add SambaNova API provider (thanks @saad-noodleseed!)
- Add VPC endpoint option for AWS Bedrock profiles (thanks @minorunara!)
- Add DeepSeek-R1 to AWS Bedrock (thanks @watany-dev!)

## [3.6.5]

- Add 'Delete all Task History' button to History view
- Add toggle to disable model switching between Plan/Act modes in Settings (new users default to disabled)
- Add temperature option to OpenAI Compatible
- Add Kotlin support to tree-sitter parser (thanks @fumiya-kume!)

## [3.6.3]

- Improve QwQ support for Alibaba (thanks @meglinge!) and OpenRouter
- Improve diff edit prompting to prevent immediately reverting to write_to_file when a model uses search patterns that don't match anything in the file
- Fix bug where new checkpoints system would revert file changes when switching between tasks
- Fix issue with incorrect token count for some OpenAI compatible providers

## [3.6.0]

- Add Cline API as a provider option, allowing new users to sign up and get started with Cline for free
- Optimize checkpoints with branch-per-task strategy, reducing storage required and first task load times
- Fix problem with Plan/Act toggle keyboard shortcut not working in Windows (thanks @yt3trees!)
- Add new Gemini models to GCP Vertex (thanks @shohei-ihaya!) and Claude models AskSage (thanks @swhite24!)
- Improve OpenRouter/Cline error reporting

## [3.5.1]

- Add timeout option to MCP servers
- Add Gemini Flash models to Vertex provider (thanks @jpaodev!)
- Add prompt caching support for AWS Bedrock provider (thanks @buger!)
- Add AskSage provider (thanks @swhite24!)

## [3.5.0]

- Add 'Enable extended thinking' option for Claude 3.7 Sonnet, with ability to set different budgets for Plan and Act modes
- Add support for rich MCP responses with automatic image previews, website thumbnails, and WolframAlpha visualizations
- Add language preference option in Advanced Settings
- Add xAI Provider Integration with support for all Grok models (thanks @andrewmonostate!)
- Fix issue with Linux XDG pointing to incorrect path for Document folder (thanks @jonatkinson!)

## [3.4.10]

- Add support for GPT-4.5 preview model

## [3.4.9]

- Add toggle to let users opt-in to anonymous telemetry and error reporting

## [3.4.6]

- Add support for Claude 3.7 Sonnet

## [3.4.0]

- Introducing MCP Marketplace! You can now discover and install the best MCP servers right from within the extension, with new servers added regularly
- Add mermaid diagram support in Plan mode! You can now see visual representations of mermaid code blocks in chat, and click on them to see an expanded view
- Use more visual checkpoints indicators after editing files & running commands
- Create a checkpoint at the beginning of each task to easily revert to the initial state
- Add 'Terminal' context mention to reference the active terminal's contents
- Add 'Git Commits' context mention to reference current working changes or specific commits (thanks @mrubens!)
- Send current textfield contents as additional feedback when toggling from Plan to Act Mode, or when hitting 'Approve' button
- Add advanced configuration options for OpenAI Compatible (context window, max output, pricing, etc.)
- Add Alibaba Qwen 2.5 coder models, VL models, and DeepSeek-R1/V3 support
- Improve support for AWS Bedrock Profiles
- Fix Mistral provider support for non-codestral models
- Add advanced setting to disable browser tool
- Add advanced setting to set chromium executable path for browser tool

## [3.3.2]

- Fix bug where OpenRouter requests would periodically not return cost/token stats, leading to context window limit errors
- Make checkpoints more visible and keep track of restored checkpoints

## [3.3.0]

- Add .clineignore to block Cline from accessing specified file patterns
- Add keyboard shortcut + tooltips for Plan/Act toggle
- Fix bug where new files won't show up in files dropdown
- Add automatic retry for rate limited requests (thanks @ViezeVingertjes!)
- Adding reasoning_effort support for o3-mini in Advanced Settings
- Added support for AWS provider profiles using the AWS CLI to make the profile, enabling long lived connections to AWS bedrock
- Adding Requesty API provider
- Add Together API provider
- Add Alibaba Qwen API provider (thanks @aicccode!)

## [3.2.13]

- Add new gemini models gemini-2.0-flash-lite-preview-02-05 and gemini-2.0-flash-001
- Add all available Mistral API models (thanks @ViezeVingertjes!)
- Add LiteLLM API provider support (thanks @him0!)

## [3.2.12]

- Fix command chaining for Windows users
- Fix reasoning_content error for OpenAI providers

## [3.2.11]

- Add OpenAI o3-mini model

## [3.2.10]

- Improve support for DeepSeek-R1 (deepseek-reasoner) model for OpenRouter, OpenAI-compatible, and DeepSeek direct (thanks @Szpadel!)
- Show Reasoning tokens for models that support it
- Fix issues with switching models between Plan/Act modes

## [3.2.6]

- Save last used API/model when switching between Plan and Act, for users that like to use different models for each mode
- New Context Window progress bar in the task header to understand increased cost/generation degradation as the context increases
- Localize READMEs and add language selector for English, Spanish, German, Chinese, and Japanese
- Add Advanced Settings to remove MCP prompts from requests to save tokens, enable/disable checkpoints for users that don't use git (more coming soon!)
- Add Gemini 2.0 Flash Thinking experimental model
- Allow new users to subscribe to mailing list to get notified when new Accounts option is available

## [3.2.5]

- Use yellow textfield outline in Plan mode to better distinguish from Act mode

## [3.2.3]

- Add DeepSeek-R1 (deepseek-reasoner) model support with proper parameter handling (thanks @slavakurilyak!)

## [3.2.0]

- Add Plan/Act mode toggle to let you plan tasks with Cline before letting him get to work
- Easily switch between API providers and models using a new popup menu under the chat field
- Add VS Code LM API provider to run models provided by other VS Code extensions (e.g. GitHub Copilot). Shoutout to @julesmons, @RaySinner, and @MrUbens for putting this together!
- Add on/off toggle for MCP servers to disable them when not in use. Thanks @MrUbens!
- Add Auto-approve option for individual tools in MCP servers. Thanks @MrUbens!

## [3.1.10]

- New icon!

## [3.1.9]

- Add Mistral API provider with codestral-latest model

## [3.1.7]

- Add ability to change viewport size and headless mode when Cline asks to launch the browser

## [3.1.6]

- Fix bug where filepaths with Chinese characters would not show up in context mention menu (thanks @chi-chat!)
- Update Anthropic model prices (thanks @timoteostewart!)

## [3.1.5]

- Fix bug where Cline couldn't read "@/" import path aliases from tool results

## [3.1.4]

- Fix issue where checkpoints would not work for users with git commit signing enabled globally

## [3.1.2]

- Fix issue where LFS files would be not be ignored when creating checkpoints

## [3.1.0]

- Added checkpoints: Snapshots of workspace are automatically created whenever Cline uses a tool
- Compare changes: Hover over any tool use to see a diff between the snapshot and current workspace state
- Restore options: Choose to restore just the task state, just the workspace files, or both
- New 'See new changes' button appears after task completion, providing an overview of all workspace changes
- Task header now shows disk space usage with a delete button to help manage snapshot storage

## [3.0.12]

- Fix DeepSeek API cost reporting (input price is 0 since it's all either a cache read or write, different than how Anthropic reports cache usage)

## [3.0.11]

- Emphasize auto-formatting done by the editor in file edit responses for more reliable diff editing

## [3.0.10]

- Add DeepSeek provider to API Provider options
- Fix context window limit errors for DeepSeek v3

## [3.0.9]

- Fix bug where DeepSeek v3 would incorrectly escape HTML entities in diff edits

## [3.0.8]

- Mitigate DeepSeek v3 diff edit errors by adding 'auto-formatting considerations' to system prompt, encouraging model to use updated file contents as reference point for SEARCH blocks

## [3.0.7]

- Revert to using batched file watcher to fix crash when many files would be created at once

## [3.0.6]

- Fix bug where some files would be missing in the `@` context mention menu
- Add Bedrock support in additional regions
- Diff edit improvements
- Add OpenRouter's middle-out transform for models that don't use prompt caching (prevents context window limit errors, but cannot be applied to models like Claude since it would continuously break the cache)

## [3.0.4]

- Fix bug where gemini models would add code block artifacts to the end of text content
- Fix context mention menu visual issues on light themes

## [3.0.2]

- Adds block anchor matching for more reliable diff edits (if 3+ lines, first and last line are used as anchors to search for)
- Add instruction to system prompt to use complete lines in diff edits to work properly with fallback strategies
- Improves diff edit error handling
- Adds new Gemini models

## [3.0.0]

- Cline now uses a search & replace diff based approach when editing large files to prevent code deletion issues.
- Adds support for a more comprehensive auto-approve configuration, allowing you to specify which tools require approval and which don't.
- Adds ability to enable system notifications for when Cline needs approval or completes a task.
- Adds support for a root-level `.clinerules` file that can be used to specify custom instructions for the project.

## [2.2.0]

- Add support for Model Context Protocol (MCP), enabling Cline to use custom tools like web-search tool or GitHub tool
- Add MCP server management tab accessible via the server icon in the menu bar
- Add ability for Cline to dynamically create new MCP servers based on user requests (e.g., "add a tool that gets the latest npm docs")

## [2.1.6]

- Add LM Studio as an API provider option (make sure to start the LM Studio server to use it with the extension!)

## [2.1.5]

- Add support for prompt caching for new Claude model IDs on OpenRouter (e.g. `anthropic/claude-3.5-sonnet-20240620`)

## [2.1.4]

- AWS Bedrock fixes (add missing regions, support for cross-region inference, and older Sonnet model for regions where new model is not available)

## [2.1.3]

- Add support for Claude 3.5 Haiku, 66% cheaper than Sonnet with similar intelligence

## [2.1.2]

- Misc. bug fixes
- Update README with new browser feature

## [2.1.1]

- Add stricter prompt to prevent Cline from editing files during a browser session without first closing the browser

## [2.1.0]

- Cline now uses Anthropic's new "Computer Use" feature to launch a browser, click, type, and scroll. This gives him more autonomy in runtime debugging, end-to-end testing, and even general web use. Try asking "Look up the weather in Colorado" to see it in action! (Available with Claude 3.5 Sonnet v2)

## [2.0.19]

- Fix model info for Claude 3.5 Sonnet v1 on OpenRouter

## [2.0.18]

- Add support for both v1 and v2 of Claude 3.5 Sonnet for GCP Vertex and AWS Bedrock (for cases where the new model is not enabled yet or unavailable in your region)

## [2.0.17]

- Update Anthropic model IDs

## [2.0.16]

- Adjustments to system prompt

## [2.0.15]

- Fix bug where modifying Cline's edits would lead him to try to re-apply the edits
- Fix bug where weaker models would display file contents before using the write_to_file tool
- Fix o1-mini and o1-preview errors when using OpenAI native

## [2.0.14]

- Gracefully cancel requests while stream could be hanging

## [2.0.13]

- Detect code omission and show warning with troubleshooting link

## [2.0.12]

- Keep cursor out of the way during file edit streaming animation

## [2.0.11]

- Adjust prompts around read_file to prevent re-reading files unnecessarily

## [2.0.10]

- More adjustments to system prompt to prevent lazy coding

## [2.0.9]

- Update system prompt to try to prevent Cline from lazy coding (`// rest of code here...`)

## [2.0.8]

- Fix o1-mini and o1-preview for OpenAI
- Fix diff editor not opening sometimes in slow environments like project idx

## [2.0.7]

- Misc. bug fixes

## [2.0.6]

- Update URLs to https://github.com/cline/cline

## [2.0.5]

- Fixed bug where Cline's edits would stream into the active tab when switching tabs during a write_to_file
- Added explanation in task continuation prompt that an interrupted write_to_file reverts the file to its original contents, preventing unnecessary re-reads
- Fixed non-first chunk error handling in case stream fails mid-way through

## [2.0.0]

- New name! Meet Cline, an AI assistant that can use your CLI and Editor
- Responses are now streamed with a yellow text decoration animation to keep track of Cline's progress as he edits files
- New Cancel button to give Cline feedback if he goes off in the wrong direction, giving you more control over tasks
- Re-imagined tool calling prompt resulting in ~40% fewer requests to accomplish tasks + better performance with other models
- Search and use any model with OpenRouter

## [1.9.7]

- Only auto-include error diagnostics after file edits, removed warnings to keep Claude from getting distracted in projects with strict linting rules

## [1.9.6]

- Added support for new Google Gemini models `gemini-1.5-flash-002` and `gemini-1.5-pro-002`
- Updated system prompt to be more lenient when terminal output doesn't stream back properly
- Adjusted system prompt to prevent overuse of the inspect_site tool
- Increased global line height for improved readability

## [1.9.0]

- Claude can now use a browser! This update adds a new `inspect_site` tool that captures screenshots and console logs from websites (including localhost), making it easier for Claude to troubleshoot issues on his own.
- Improved automatic linter/compiler debugging by only sending Claude new errors that result from his edits, rather than reporting all workspace problems.

## [1.8.0]

- You can now use '@' in the textarea to add context!
- @url: Paste in a URL for the extension to fetch and convert to markdown, useful when you want to give Claude the latest docs!
- @problems: Add workspace errors and warnings for Claude to fix, no more back-and-forth about debugging
- @file: Adds a file's contents so you don't have to waste API requests approving read file (+ type to search files)
- @folder: Adds folder's files all at once to speed up your workflow even more

## [1.7.0]

- Adds problems monitoring to keep Claude updated on linter/compiler/build issues, letting him proactively fix errors on his own! (adding missing imports, fixing type errors, etc.)

## [1.6.5]

- Adds support for OpenAI o1, Azure OpenAI, and Google Gemini (free for up to 15 requests per minute!)
- Task header can now be collapsed to provide more space for viewing conversations
- Adds fuzzy search and sorting to Task History, making it easier to find specific tasks

## [1.6.0]

- Commands now run directly in your terminal thanks to VSCode 1.93's new shell integration updates! Plus a new 'Proceed While Running' button to let Claude continue working while commands run, sending him new output along the way (i.e. letting him react to server errors as he edits files)

## [1.5.27]

- Claude's changes now appear in your file's Timeline, allowing you to easily view a diff of each edit. This is especially helpful if you want to revert to a previous version. No need for git—everything is tracked by VSCode's local history!
- Updated system prompt to keep Claude from re-reading files unnecessarily

## [1.5.19]

- Adds support for OpenAI compatible API providers (e.g. Ollama!)

## [1.5.13]

- New terminal emulator! When Claude runs commands, you can now type directly in the terminal (+ support for Python environments)
- Adds search to Task History

## [1.5.6]

- You can now edit Claude's changes before accepting! When he edits or creates a file, you can modify his changes directly in the right side of the diff view (+ hover over the 'Revert Block' arrow button in the center to undo `// rest of code here` shenanigans)

## [1.5.4]

- Adds support for reading .pdf and .docx files (try "turn my business_plan.docx into a company website")

## [1.5.0]

- Adds new `search_files` tool that lets Claude perform regex searches in your project, making it easy for him to refactor code, address TODOs and FIXMEs, remove dead code, and more!

## [1.4.0]

- Adds "Always allow read-only operations" setting to let Claude read files and view directories without needing approval (off by default)
- Implement sliding window context management to keep tasks going past 200k tokens
- Adds Google Cloud Vertex AI support and updates Claude 3.5 Sonnet max output to 8192 tokens for all providers.
- Improves system prompt to guard against lazy edits (less "//rest of code here")

## [1.3.0]

- Adds task history

## [1.2.0]

- Adds support for Prompt Caching to significantly reduce costs and response times (currently only available through Anthropic API for Claude 3.5 Sonnet and Claude 3.0 Haiku)

## [1.1.1]

- Adds option to choose other Claude models (+ GPT-4o, DeepSeek, and Mistral if you use OpenRouter)
- Adds option to add custom instructions to the end of the system prompt

## [1.1.0]

- Paste images in chat to use Claude's vision capabilities and turn mockups into fully functional applications or fix bugs with screenshots

## [1.0.9]

- Add support for OpenRouter and AWS Bedrock

## [1.0.8]

- Shows diff view of new or edited files right in the editor

## [1.0.7]

- Replace `list_files` and `analyze_project` with more explicit `list_files_top_level`, `list_files_recursive`, and `view_source_code_definitions_top_level` to get source code definitions only for files relevant to the task

## [1.0.6]

- Interact with CLI commands by sending messages to stdin and terminating long-running processes like servers
- Export tasks to markdown files (useful as context for future tasks)

## [1.0.5]

- Claude now has context about vscode's visible editors and opened tabs

## [1.0.4]

- Open in the editor (using menu bar or `Claude Dev: Open In New Tab` in command palette) to see how Claude updates your workspace more clearly
- New `analyze_project` tool to help Claude get a comprehensive overview of your project's source code definitions and file structure
- Provide feedback to tool use like terminal commands and file edits
- Updated max output tokens to 8192 so less lazy coding (`// rest of code here...`)
- Added ability to retry failed API requests (helpful for rate limits)
- Quality of life improvements like markdown rendering, memory optimizations, better theme support

## [0.0.6]

- Initial release



---

# FILE: CLAUDE.md

@.clinerules/general.md
@.clinerules/network.md
@.clinerules/cli.md



---

# FILE: CODE_OF_CONDUCT.md

# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

-   Using welcoming and inclusive language
-   Being respectful of differing viewpoints and experiences
-   Gracefully accepting constructive criticism
-   Focusing on what is best for the community
-   Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

-   The use of sexualized language or imagery and unwelcome sexual attention or
    advances
-   Trolling, insulting/derogatory comments, and personal or political attacks
-   Public or private harassment
-   Publishing others' private information, such as a physical or electronic
    address, without explicit permission
-   Other conduct which could reasonably be considered inappropriate in a
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
reported by contacting the project team at hi@cline.bot. All complaints
will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq



---

# FILE: CONTRIBUTING.md

# Contributing to Cline

We're thrilled you're interested in contributing to Cline. Whether you're fixing a bug, adding a feature, or improving our docs, every contribution makes Cline smarter! To keep our community vibrant and welcoming, all members must adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

## Reporting Bugs or Issues

Bug reports help make Cline better for everyone! Before creating a new issue, please [search existing ones](https://github.com/cline/cline/issues) to avoid duplicates. When you're ready to report a bug, head over to our [issues page](https://github.com/cline/cline/issues/new/choose) where you'll find a template to help you with filling out the relevant information.

<blockquote class='warning-note'>
     🔐 <b>Important:</b> If you discover a security vulnerability, please use the <a href="https://github.com/cline/cline/security/advisories/new">Github security tool to report it privately</a>.
</blockquote>


## Before Contributing

All contributions must begin with a GitHub Issue, unless the change is for small bug fixes, typo corrections, minor wording improvements, or simple type fixes that don't change functionality.
**For features and contributions**:
- First check the [Feature Requests discussions board](https://github.com/cline/cline/discussions/categories/feature-requests) for similar ideas
- If your idea is new, create a new feature request  
- Wait for approval from core maintainers before starting implementation
- Once approved, feel free to begin working on a PR with the help of our community!

**PRs without approved issues may be closed.**


## Deciding What to Work On

Looking for a good first contribution? Check out issues labeled ["good first issue"](https://github.com/cline/cline/labels/good%20first%20issue) or ["help wanted"](https://github.com/cline/cline/labels/help%20wanted). These are specifically curated for new contributors and areas where we'd love some help!

We also welcome contributions to our [documentation](https://github.com/cline/cline/tree/main/docs)! Whether it's fixing typos, improving existing guides, or creating new educational content - we'd love to build a community-driven repository of resources that helps everyone get the most out of Cline. You can start by diving into `/docs` and looking for areas that need improvement.

## Development Setup


### Local Development Instructions

1. Clone the repository _(Requires [git-lfs](https://git-lfs.com/))_:
    ```bash
    git clone https://github.com/cline/cline.git
    ```
2. Open the project in VSCode:
    ```bash
    code cline
    ```
3. Install the necessary dependencies for the extension and webview-gui:
    ```bash
    npm run install:all
    ```
4. Generate Protocol Buffer files (required before first build):
    ```bash
    npm run protos
    ```
5. Launch by pressing `F5` (or `Run`->`Start Debugging`) to open a new VSCode window with the extension loaded. (You may need to install the [esbuild problem matchers extension](https://marketplace.visualstudio.com/items?itemName=connor4312.esbuild-problem-matchers) if you run into issues building the project.)




### Creating a Pull Request

1. Commit your changes.

2. Push your branch and create a PR on GitHub. Our CI will:
   - Run tests and checks
3. Testing
    - Run `npm run test` to run tests locally. 
    - Before submitting PR, run `npm run format:fix` to format your code

### Extension

1. **VS Code Extensions**

    - When opening the project, VS Code will prompt you to install recommended extensions
    - These extensions are required for development - please accept all installation prompts
    - If you dismissed the prompts, you can install them manually from the Extensions panel

2. **Local Development**
    - Run `npm run install:all` to install dependencies
    - Run `npm run protos` to generate Protocol Buffer files (required before first build)
    - Run `npm run test` to run tests locally
    - Run → Start Debugging or `>Debug: Select and Start Debugging` and wait for a new VS Code instance to open
    - **Terminal Workflow**: Use `npm run dev` (generates protos + runs watch mode) or `npm run watch` (if protos already generated)
    - Before submitting PR, run `npm run format:fix` to format your code

3. **Linux-specific Setup**
    VS Code extension tests on Linux require the following system libraries:

    - `dbus`
    - `libasound2`
    - `libatk-bridge2.0-0`
    - `libatk1.0-0`
    - `libdrm2`
    - `libgbm1`
    - `libgtk-3-0`
    - `libnss3`
    - `libx11-xcb1`
    - `libxcomposite1`
    - `libxdamage1`
    - `libxfixes3`
    - `libxkbfile1`
    - `libxrandr2`
    - `xvfb`

    These libraries provide necessary GUI components and system services for the test environment.

    For example, on Debian-based distributions (e.g., Ubuntu), you can install these libraries using apt:
    ```bash
    sudo apt update
    sudo apt install -y \
      dbus \
      libasound2 \
      libatk-bridge2.0-0 \
      libatk1.0-0 \
      libdrm2 \
      libgbm1 \
      libgtk-3-0 \
      libnss3 \
      libx11-xcb1 \
      libxcomposite1 \
      libxdamage1 \
      libxfixes3 \
      libxkbfile1 \
      libxrandr2 \
      xvfb
    ```

## Writing and Submitting Code

Anyone can contribute code to Cline, but we ask that you follow these guidelines to ensure your contributions can be smoothly integrated:

1. **Keep Pull Requests Focused**

    - Limit PRs to a single feature or bug fix
    - Split larger changes into smaller, related PRs
    - Break changes into logical commits that can be reviewed independently

2. **Code Quality**

    - Run `npm run lint` to check code style
    - Run `npm run format` to automatically format code
    - All PRs must pass CI checks which include both linting and formatting
    - Address any warnings or errors from linter before submitting
    - Follow TypeScript best practices and maintain type safety

3. **Testing**

    - Add tests for new features
    - Run `npm test` to ensure all tests pass
    - Update existing tests if your changes affect them
    - Include both unit tests and integration tests where appropriate

    **End-to-End (E2E) Testing**
    
    Cline includes comprehensive E2E tests using Playwright that simulate real user interactions with the extension in VS Code:
    
    - **Running E2E tests:**
      ```bash
      npm run test:e2e        # Build and run all E2E tests
      npm run e2e             # Run tests without rebuilding
      npm run test:e2e -- --debug  # Run with interactive debugger
      ```
    
    - **Writing E2E tests:**
      - Tests are located in `src/test/e2e/`
      - Use the `e2e` fixture for single-root workspace tests
      - Use `e2eMultiRoot` fixture for multi-root workspace tests
      - Follow existing patterns in `auth.test.ts`, `chat.test.ts`, `diff.test.ts`, and `editor.test.ts`
      - See `src/test/e2e/README.md` for detailed documentation
    
    - **Debug mode features:**
      - Interactive Playwright Inspector for step-by-step debugging
      - Record new interactions and generate test code automatically
      - Visual VS Code instance for manual testing
      - Element inspection and selector validation
    
    - **Test environment:**
      - Automated VS Code setup with Cline extension loaded
      - Mock API server for backend testing
      - Temporary workspaces with test fixtures
      - Video recording for failed tests

4. **Versioning & Changelog Notes**

    - Contributors do not need to create changelog-entry files as part of PRs.
    - Maintainers handle release versioning and changelog curation during the release process.

5. **Commit Guidelines**

    - Write clear, descriptive commit messages
    - Use conventional commit format (e.g., "feat:", "fix:", "docs:")
    - Reference relevant issues in commits using #issue-number

6. **Before Submitting**

    - Rebase your branch on the latest main
    - Ensure your branch builds successfully
    - Double-check all tests are passing
    - Review your changes for any debugging code or console logs

7. **Pull Request Description**
    - Clearly describe what your changes do
    - Include steps to test the changes
    - List any breaking changes
    - Add screenshots for UI changes

## Contribution Agreement

By submitting a pull request, you agree that your contributions will be licensed under the same license as the project ([Apache 2.0](LICENSE)).

Remember: Contributing to Cline isn't just about writing code - it's about being part of a community that's shaping the future of AI-assisted development. Let's build something amazing together! 🚀



---

# FILE: SECURITY.md

# Security Policy

## Supported Versions

We actively patch only the most recent minor release of Cline. Older versions receive fixes at our discretion.

## Reporting a Vulnerability

We appreciate your efforts to responsibly disclose your findings and will make every effort to acknowledge your contributions.

To report a security issue, please submit your report through our [Bugcrowd Vulnerability Disclosure Program](https://bugcrowd.com/engagements/clinebot-vdp-ess). Bugcrowd will manage communication and triage on our behalf.

When reporting, please include:

- A short summary of the issue
- Steps to reproduce or a proof of concept
- Any logs, stack traces, or screenshots that might help us understand the problem

Please keep the details private until a resolution has been reached.

## Escalation

If you are unable to submit through Bugcrowd, you may send an email to security@cline.bot.

Thank you for helping us keep Cline users safe.



---

# FILE: buf.yaml

version: v2
modules:
    - path: proto
      name: cline/cline/lint

lint:
    use:
        - STANDARD

    except: # Add exceptions for current patterns that contradict STANDARD settings
        - RPC_PASCAL_CASE # rpcs are camel case (start with lowercase)
        - RPC_REQUEST_RESPONSE_UNIQUE # request messages are not unique.
        - RPC_REQUEST_STANDARD_NAME # request messages dont all end with Request
        - RPC_RESPONSE_STANDARD_NAME # response messages dont all end with Response
        - PACKAGE_VERSION_SUFFIX # package name does not contain version.
        - ENUM_VALUE_PREFIX # enum values dont start with the enum name.
        - ENUM_ZERO_VALUE_SUFFIX # first value does not have to be UNSPECIFIED.

# breaking:
#   use:
#     - WIRE_JSON # Detect changes that break the json wire format (this is the minimum recommended level.)



---

# FILE: docs/cline-sdk/overview.md

---
title: "Cline SDK"
sidebarTitle: "SDK (Programmatic Use)"
description: "Embed Cline as a programmable coding agent in your Node.js applications using an ACP-compatible TypeScript API."
---

# Cline SDK

The Cline SDK lets you embed Cline as a programmable coding agent in your Node.js applications. It exposes the same capabilities as the Cline CLI and VS Code extension — file editing, command execution, browser use, MCP servers — through a TypeScript API that conforms to the [Agent Client Protocol (ACP)](https://agentclientprotocol.com/protocol/schema).

## Installation

```bash
npm install cline
```

If you want direct ACP type imports as well:

```bash
npm install @agentclientprotocol/sdk
```

Requires Node.js 20+.

## Quick Start

```typescript
import { ClineAgent } from "cline";

const CLINE_DIR = "/Users/username/.cline";
const agent = new ClineAgent({ clineDir: CLINE_DIR });

// 1. Initialize — negotiates capabilities
const initializeResponse = await agent.initialize({
    protocolVersion: 1,
    // these are the capabilities that the client (you) supports
    // The cline agent may or may not use them, but it needs to know about them to make informed decisions about what tools to use.
    clientCapabilities: {
        fs: { readTextFile: true, writeTextFile: true },
        terminal: true,
    },
});

const { agentInfo, authMethods } = initializeResponse;
console.log("Agent info:", agentInfo); // contains things like agent name and version
console.log("Auth methods:", authMethods); // contains a list of supported authentication methods. More auth methods coming soon

// 2. Authenticate if needed
// If you skip this step, ClineAgent will look in CLINE_DIR for any existing credentials and authenticate with those
await agent.authenticate({ methodId: "cline-oauth" });

// 3. Create a session.
// A session represents a conversation or task with the agent. You can have multiple sessions for different tasks or conversations.
const { sessionId } = await agent.newSession({
    cwd: process.cwd(),
    mcpServers: [], // mcpServers field not supported yet, but exposed here to maintain conformance with acp protocol
});

// 4. Agent updates are sent via events. You can subscribe to these events to get real-time updates on the agent's progress, tool calls, and more.
const emitter = agent.emitterForSession(sessionId);

emitter.on("agent_message_chunk", (payload) => {
    process.stdout.write(
        payload.content.type === "text"
            ? payload.content.text
            : `[${payload.content.type}]`,
    );
});
emitter.on("agent_thought_chunk", (payload) => {
    process.stdout.write(
        payload.content.type === "text"
            ? payload.content.text
            : `[${payload.content.type}]`,
    );
});
emitter.on("tool_call", (payload) => {
    console.log(`[tool] ${payload.title}`);
});
emitter.on("error", (err) => {
    console.error("[session error]", err);
});

// 5. Send a prompt and wait for completion
const { stopReason } = await agent.prompt({
    sessionId,
    prompt: [{ type: "text", text: "Create a hello world Express server" }],
});

console.log("Done:", stopReason);

// 6. Clean up
await agent.shutdown();

```

## Core Concepts

### Agent Lifecycle

The SDK follows the ACP lifecycle:

```
initialize() → authenticate() → newSession() → prompt() ⇄ events → shutdown()
```

| Step | Method | Purpose |
|------|--------|---------|
| Init | `initialize()` | Exchange protocol version and capabilities |
| Auth | `authenticate()` | OAuth flow for Cline or OpenAI Codex accounts. Optional step if cline config directory already has credentials |
| Session | `newSession()` | Create an isolated conversation context |
| Prompt | `prompt()` | Send user messages; blocks until the turn ends |
| Cancel | `cancel()` | Abort an in-progress prompt turn |
| Mode | `setSessionMode()` | Switch between `"plan"` and `"act"` modes |
| Model | `unstable_setSessionModel()` | Change the backing LLM (experimental) |
| Shutdown | `shutdown()` | Abort all tasks, flush state, release resources |

### Sessions

A session is an independent conversation with its own task history and working directory. You can run multiple sessions concurrently.

```typescript
const { sessionId, modes, models } = await agent.newSession({
  cwd: "/path/to/project",
  mcpServers: [], // mcpServers field not supported yet, but exposed here to maintain conformance with acp protocol
})
```

The response includes:
- `sessionId` — use this in all subsequent calls
- `modes` — available modes (`plan`, `act`) and the current mode
- `models` — available models and the current model ID

Access session metadata via the read-only `sessions` map:

```typescript
const session = agent.sessions.get(sessionId)
// { sessionId, cwd, mode, mcpServers, createdAt, lastActivityAt, ... }
```

### Prompting

`prompt()` sends a user message and blocks until the agent finishes its turn. While the prompt is processing, the agent streams output via session events.

```typescript
const response = await agent.prompt({
  sessionId,
  prompt: [
    { type: "text", text: "Refactor the auth module to use JWT" },
  ],
})
```

The prompt array accepts multiple content blocks:

```typescript
// Text + image + file context
await agent.prompt({
  sessionId,
  prompt: [
    { type: "text", text: "What's in this screenshot?" },
    { type: "image", data: base64ImageData, mimeType: "image/png" },
    {
      type: "resource",
      resource: {
        uri: "file:///path/to/relevant-file.ts",
        mimeType: "text/plain",
        text: fileContents,
      },
    },
  ],
})
```

#### Content Block Types

| Type | Fields | Description |
|------|--------|-------------|
| `TextContent` | `{ type: "text", text: string }` | Plain text message |
| `ImageContent` | `{ type: "image", mimeType: string, data: string }` | Base64-encoded image |
| `EmbeddedResource` | `{ type: "resource", resource: { uri: string, mimeType?: string, text?: string, blob?: string } }` | File or resource context |

#### Stop Reasons

`prompt()` resolves with a `stopReason`. The ACP `StopReason` type defines the full set of possible values:

| Value | Meaning |
|-------|---------|
| `"end_turn"` | Agent finished normally (completed task or waiting for user input) |
| `"error"` | An error occurred |

> **Note:** Cline currently returns `"end_turn"` or `"error"`. Other `StopReason` values like `"max_tokens"` or `"cancelled"` are part of the ACP type but may not be produced by the current implementation.

### Streaming Events

Subscribe to real-time output via `ClineSessionEmitter`. Each session has its own emitter.

```typescript
const emitter = agent.emitterForSession(sessionId)
```

#### Event Types

All events correspond to [ACP `SessionUpdate` types](https://agentclientprotocol.com/protocol/schema#SessionUpdate):

| Event | Payload | Description |
|-------|---------|-------------|
| `agent_message_chunk` | `{ content: ContentBlock }` | Streamed text from the agent |
| `agent_thought_chunk` | `{ content: ContentBlock }` | Internal reasoning / chain-of-thought |
| `tool_call` | `ToolCall` | New tool invocation (file edit, command, etc.) |
| `tool_call_update` | `ToolCallUpdate` | Progress/result update for an existing tool call |
| `plan` | `{ entries: PlanEntry[] }` | Agent's execution plan |
| `available_commands_update` | `{ availableCommands: AvailableCommand[] }` | Slash commands the agent supports |
| `current_mode_update` | `{ currentModeId: string }` | Mode changed (plan/act) |
| `user_message_chunk` | `{ content: ContentBlock }` | User message chunks (for multi-turn) |
| `config_option_update` | `{ configOptions: SessionConfigOption[] }` | Configuration changed |
| `session_info_update` | Session metadata | Session metadata changed |
| `error` | `Error` | Session-level error (not an ACP update) |

```typescript
emitter.on("agent_message_chunk", (payload) => {
  // payload.content is a ContentBlock — usually { type: "text", text: "..." }
  process.stdout.write(payload.content.text)
})

emitter.on("agent_thought_chunk", (payload) => {
  console.log("[thinking]", payload.content.text)
})

emitter.on("tool_call", (payload) => {
  console.log(`[${payload.kind}] ${payload.title} (${payload.status})`)
})

emitter.on("tool_call_update", (payload) => {
  console.log(`  → ${payload.toolCallId}: ${payload.status}`)
})

emitter.on("error", (err) => {
  console.error("Session error:", err)
})
```

The emitter supports `on`, `once`, `off`, and `removeAllListeners`.

### Permission Handling

When the agent wants to execute a tool (edit a file, run a command, etc.), it requests permission. You **must** set a permission handler or all tool calls will be auto-rejected.

```typescript
agent.setPermissionHandler(async (request) => {
  // request.toolCall — details about what the agent wants to do
  // request.options — available choices (allow_once, reject_once, etc.)

  console.log(`Permission requested: ${request.toolCall.title}`)
  console.log("Options:", request.options.map(o => `${o.optionId} (${o.kind})`))

  // Auto-approve everything:
  const allowOption = request.options.find(o => o.kind.includes("allow"))
  if (allowOption) {
    return { outcome: { outcome: "selected", optionId: allowOption.optionId } }
  } else {
    return { outcome: { outcome: "rejected" } }
  }
})
```

#### Permission Options

Each permission request includes an array of `PermissionOption` objects:

| `kind` | Meaning |
|--------|---------|
| `allow_once` | Approve this single operation |
| `allow_always` | Approve and remember for future operations (sent for commands, tools, MCP servers) |
| `reject_once` | Deny this single operation |

**Important:** If no permission handler is set, all tool calls are rejected for safety.

### Modes

Cline supports two modes:

- **`plan`** — The agent gathers information and creates a plan without executing actions
- **`act`** — The agent executes actions (file edits, commands, etc.)

```typescript
// Switch to plan mode
await agent.setSessionMode({ sessionId, modeId: "plan" })

// Switch back to act mode
await agent.setSessionMode({ sessionId, modeId: "act" })
```

The current mode is returned in `newSession()`

### Model Selection

Change the backing model with `unstable_setSessionModel()`. The model ID format is `"provider/modelId"`.

```typescript
await agent.unstable_setSessionModel({
  sessionId,
  modelId: "anthropic/claude-sonnet-4-20250514",
})
```

This sets the model for both plan and act modes. Available providers include `anthropic`, `openai-native`, `gemini`, `bedrock`, `deepseek`, `mistral`, `groq`, `xai`, and others. Model Ids can be found in the NewSessionResponse object after calling `agent.newSession(..)`

> **Note:** This API is experimental and may change. 

### Authentication

The SDK supports two OAuth flows:

```typescript
// Cline account (uses browser OAuth)
await agent.authenticate({ methodId: "cline-oauth" })

// OpenAI Codex / ChatGPT subscription
await agent.authenticate({ methodId: "openai-codex-oauth" })
```

Both methods open a browser window for the OAuth flow and block until authentication completes (5-minute timeout for Cline OAuth).

For BYO (bring-your-own) API key providers, you can pre-configure credentials using the Cline CLI before using the SDK:

```bash
# Configure an Anthropic API key (default directory: ~/.cline/data/)
cline auth -p anthropic -k "sk-ant-..." -m anthropic/claude-sonnet-4-20250514

# Configure an OpenRouter API key
cline auth -p openrouter -k "sk-or-..." -m openrouter/anthropic/claude-sonnet-4
```

This writes credentials to `~/.cline/data/`. Once configured, the SDK will use these credentials automatically — no `authenticate()` call needed.

**Using a custom directory:** If you specify a custom `clineDir` when creating `ClineAgent`, you must use the same path with `--config` when running `cline auth`:

```typescript
// SDK code using custom directory
const agent = new ClineAgent({ clineDir: "/custom/path" })
```

```bash
# CLI auth command must use the same path
cline auth -p anthropic -k "sk-ant-..." -m anthropic/claude-sonnet-4-20250514 --config /custom/path
```

### Cancellation

Cancel an in-progress prompt turn:

```typescript
await agent.cancel({ sessionId })
```

## API Reference

### Constructor

```typescript
new ClineAgent(options: ClineAgentOptions)
```

```typescript
interface ClineAgentOptions {
  /** Enable debug logging (default: false) */
  debug?: boolean
  /** Custom Cline config directory (default: ~/.cline) */
  clineDir?: string
  /** Additional runtime hooks directory */
  hooksDir?: string
}
```

The `clineDir` option lets you isolate configuration and task history per-application:

```typescript
const agent = new ClineAgent({
  clineDir: "/tmp/my-app-cline",
})
```

### Methods

#### `initialize(params): Promise<InitializeResponse>`

Initialize the agent and negotiate protocol capabilities.

```typescript
const response = await agent.initialize({
  clientCapabilities: {},
  protocolVersion: 1,
})

// Response includes:
{
  protocolVersion: 1,
  agentCapabilities: {
    loadSession: true,
    promptCapabilities: { image: true, audio: false, embeddedContext: true },
    mcpCapabilities: { http: true, sse: false }
  },
  agentInfo: { name: "cline", version: "<installed_version>" },
  authMethods: [
    { id: "cline-oauth", name: "Sign in with Cline", description: "..." },
    { id: "openai-codex-oauth", name: "Sign in with ChatGPT", description: "..." }
  ]
}
```

#### Client Capabilities

The `clientCapabilities` object in `initialize()` declares what your environment supports. It is part of the ACP protocol handshake.

| Capability | Type | Description |
|------------|------|-------------|
| `fs.readTextFile` | `boolean` | Client supports file read requests |
| `fs.writeTextFile` | `boolean` | Client supports file write requests |
| `terminal` | `boolean` | Client supports terminal command execution |

**When using `ClineAgent` directly (SDK use)**, the agent always uses standalone providers for file operations and terminal commands — it reads/writes files and runs shell commands on the local machine regardless of what you pass here. Simply pass `{}`:

```typescript
await agent.initialize({ protocolVersion: 1, clientCapabilities: {} })
```

These capabilities only affect behavior when `ClineAgent` is used through the `AcpAgent` stdio wrapper (e.g., IDE integrations), where an ACP connection delegates operations back to the client.

#### `newSession(params): Promise<NewSessionResponse>`

Create a new conversation session.

```typescript
const session = await agent.newSession({
  cwd: "/path/to/project",
  mcpServers: [
    {
      type: "stdio",
      name: "filesystem",
      command: "npx",
      args: ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"],
      env: {},
    },
  ],
})

// Response includes:
{
  sessionId: "uuid-string",
  modes: {
    availableModes: [
      { id: "plan", name: "Plan", description: "Gather information and create a detailed plan" },
      { id: "act", name: "Act", description: "Execute actions to accomplish the task" }
    ],
    currentModeId: "act"
  },
  models: {
    currentModelId: "anthropic/claude-sonnet-4-20250514",
    availableModels: [{ modelId: "anthropic/claude-sonnet-4-20250514", name: "claude-sonnet-4-20250514" } /* ... */]
  }
}
```

> **Note:** `newSession()` may throw an auth-required error if credentials are not configured yet.

#### `prompt(params): Promise<PromptResponse>`

Send a user prompt to the agent. This is the main method for interacting with Cline. Blocks until the agent finishes its turn.

```typescript
const response = await agent.prompt({
  sessionId: session.sessionId,
  prompt: [
    { type: "text", text: "Create a function that adds two numbers" },
  ],
})

// Response: { stopReason: "end_turn" | "max_tokens" | "cancelled" | "error" }
```

#### `cancel(params): Promise<void>`

Cancel an ongoing prompt operation.

```typescript
await agent.cancel({ sessionId: session.sessionId })
```

#### `setSessionMode(params): Promise<SetSessionModeResponse>`

Switch between plan and act modes.

```typescript
await agent.setSessionMode({ sessionId, modeId: "plan" })
```

#### `unstable_setSessionModel(params): Promise<SetSessionModelResponse>`

Change the model for the session. Model ID format depends on the inference provider. See NewSessionResponse object to get modelIds.

```typescript
await agent.unstable_setSessionModel({
  sessionId,
  modelId: "anthropic/claude-sonnet-4-20250514",
})
```

#### `authenticate(params): Promise<AuthenticateResponse>`

Authenticate with a provider. Opens a browser window for OAuth flow.

```typescript
await agent.authenticate({ methodId: "cline-oauth" })
```

Current methodIds we support:

| methodId             | Description                   |
| -------------------- | ----------------------------- |
| `cline-oauth`        | use cline inference provider  |
| `openai-codex-oauth` | use your chatgpt subscription |
| more coming soon!... |                               |

#### `shutdown(): Promise<void>`

Clean up all resources. Call this when done.

```typescript
await agent.shutdown()
```

#### `setPermissionHandler(handler)`

Set a callback to handle tool permission requests. The handler receives a `RequestPermissionRequest` and must return a `Promise<RequestPermissionResponse>`.

```typescript
agent.setPermissionHandler(async (request) => {
  // request.toolCall — details about what the agent wants to do
  // request.options — available choices (allow_once, reject_once, etc.)
  const allow = request.options.find(o => o.kind === "allow_once")
  return {
    outcome: allow
      ? { outcome: "selected", optionId: allow.optionId }
      : { outcome: "cancelled" }
  }
})
```

#### `emitterForSession(sessionId): ClineSessionEmitter`

Get the typed event emitter for a session.

```typescript
const emitter = agent.emitterForSession(session.sessionId)
```

#### `sessions` (read-only Map)

Access active sessions:

```typescript
for (const [sessionId, session] of agent.sessions) {
  console.log(sessionId, session.cwd, session.mode)
}
```

## Error Handling

SDK methods throw standard JavaScript errors. Key error scenarios:

| Method | Error | Cause |
|--------|-------|-------|
| `newSession()` | `RequestError` (auth required) | No credentials configured — call `authenticate()` or pre-configure via CLI |
| `prompt()` | `Error("Session not found")` | Invalid `sessionId` |
| `prompt()` | `Error("already processing")` | Called `prompt()` while a previous prompt is still running on the same session |
| `unstable_setSessionModel()` | `Error("Invalid modelId format")` | Model ID must be `"provider/modelId"` format (e.g., `"anthropic/claude-sonnet-4-20250514"`) |
| `authenticate()` | `Error("Unknown authentication method")` | Invalid `methodId` — use `"cline-oauth"` or `"openai-codex-oauth"` |
| `authenticate()` | `Error("Authentication timed out")` | OAuth flow not completed within 5 minutes |

```typescript
try {
  const { sessionId } = await agent.newSession({ cwd: process.cwd(), mcpServers: [] })
} catch (error) {
  if (error.message?.includes("auth")) {
    // Need to authenticate first
    await agent.authenticate({ methodId: "cline-oauth" })
  }
}
```

Session-level errors during `prompt()` execution are emitted on the session emitter rather than thrown:

```typescript
emitter.on("error", (err) => {
  console.error("Session error:", err.message)
})
```

## Full Example: Auto-Approve Agent

```typescript
import { ClineAgent } from "cline";

async function runTask(taskPrompt: string, cwd: string) {
    const agent = new ClineAgent({ clineDir: "/path/to/.cline" });

    await agent.initialize({
        protocolVersion: 1,
        clientCapabilities: {},
    });

    const { sessionId } = await agent.newSession({ cwd, mcpServers: [] });

    // Auto-approve all tool calls
    agent.setPermissionHandler(async (request) => {
        const allow = request.options.find((o) => o.kind === "allow_once");
        return {
            outcome: allow
                ? { outcome: "selected", optionId: allow.optionId }
                : { outcome: "cancelled" },
        };
    });

    // Collect output
    const output: string[] = [];
    const emitter = agent.emitterForSession(sessionId);

    emitter.on("agent_message_chunk", (p) => {
        if (p.content.type === "text") output.push(p.content.text);
    });

    emitter.on("tool_call", (p) => {
        console.log(`[tool] ${p.title}`);
    });

    const { stopReason } = await agent.prompt({
        sessionId,
        prompt: [{ type: "text", text: taskPrompt }],
    });

    console.log("\n--- Agent Output ---");
    console.log(output.join(""));
    console.log(`\nStop reason: ${stopReason}`);

    await agent.shutdown();
}

runTask("Create a README.md for this project", process.cwd());
```

## Full Example: Interactive Permission Flow

```typescript
import { ClineAgent, type PermissionHandler } from "cline";
import * as readline from "readline";

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
const ask = (q: string) => new Promise<string>((res) => rl.question(q, res));

const interactivePermissions: PermissionHandler = async (request) => {
    console.log(`\n⚠️  Permission: ${request.toolCall.title}`);

    for (const [i, opt] of request.options.entries()) {
        console.log(`  ${i + 1}. [${opt.kind}] ${opt.name}`);
    }

    const choice = await ask("Choose (number): ");
    const idx = parseInt(choice, 10) - 1;
    const selected = request.options[idx];

    if (selected) {
        return {
            outcome: { outcome: "selected", optionId: selected.optionId },
        };
    } else {
        return { outcome: { outcome: "cancelled" } };
    }
};

async function main() {
    const agent = new ClineAgent({});
    await agent.initialize({ protocolVersion: 1, clientCapabilities: {} });

    const { sessionId } = await agent.newSession({
        cwd: process.cwd(),
        mcpServers: [],
    });

    agent.setPermissionHandler(interactivePermissions);

    const emitter = agent.emitterForSession(sessionId);
    emitter.on("agent_message_chunk", (p) => {
        if (p.content.type === "text") process.stdout.write(p.content.text);
    });

    // Multi-turn conversation
    while (true) {
        const userInput = await ask("\n> ");
        if (userInput === "exit") break;

        const { stopReason } = await agent.prompt({
            sessionId,
            prompt: [{ type: "text", text: userInput }],
        });

        console.log(`\n[${stopReason}]`);
    }

    await agent.shutdown();
    rl.close();
}

main();

```

## Exported Types

All types are re-exported from the `cline` package. Key types:

| Type | Description |
|------|-------------|
| `ClineAgent` | Main agent class |
| `ClineSessionEmitter` | Typed event emitter for session events |
| `ClineAgentOptions` | Constructor options (`debug`, `clineDir`, `hooksDir`) |
| `ClineAcpSession` | Session metadata (read-only) |
| `ClineSessionEvents` | Event name → handler signature map |
| `AcpSessionStatus` | Session lifecycle enum: `Idle`, `Processing`, `Cancelled` |
| `AcpSessionState` | Session state tracking (status, pending tool calls) |
| `PermissionHandler` | `(request: RequestPermissionRequest) => Promise<RequestPermissionResponse>` |
| `RequestPermissionRequest` | Permission request details (sessionId, toolCall, options) |
| `RequestPermissionResponse` | Permission response with outcome |
| `PermissionOption` | Permission choice (`kind`, `optionId`, `name`) |
| `SessionUpdate` | Union of all session update types |
| `SessionUpdateType` | Discriminator values (`"agent_message_chunk"`, `"tool_call"`, etc.) |
| `SessionUpdatePayload` | Typed payload for a given `SessionUpdateType` |
| `SessionModelState` | Current model and available models |
| `ToolCall` | Tool call details (id, title, kind, status, content) |
| `ToolCallUpdate` | Partial update to an existing tool call |
| `ToolCallStatus` | `"pending" \| "in_progress" \| "completed" \| "failed"` |
| `ToolKind` | `"read" \| "edit" \| "delete" \| "execute" \| "search" \| ...` |
| `StopReason` | `"end_turn" \| "cancelled" \| "error" \| "max_tokens" \| ...` |
| `ContentBlock` | `TextContent \| ImageContent \| AudioContent \| ...` |
| `TextContent` / `ImageContent` / `AudioContent` | Individual content block types |
| `McpServer` | MCP server configuration (stdio, http) |
| `ModelInfo` | Model metadata (`modelId`, `name`) |
| `PromptRequest` / `PromptResponse` | Prompt call types |
| `NewSessionRequest` / `NewSessionResponse` | Session creation types |
| `InitializeRequest` / `InitializeResponse` | Initialization types |
| `SetSessionModeRequest` / `SetSessionModeResponse` | Mode switching types |
| `SetSessionModelRequest` / `SetSessionModelResponse` | Model switching types |
| `TranslatedMessage` | Result of translating a Cline message to ACP updates |

See the [ACP Schema](https://agentclientprotocol.com/protocol/schema) for the full type definitions.

## Relationship to ACP

The Cline SDK implements the [Agent Client Protocol](https://agentclientprotocol.com) `Agent` interface. The key difference from a standard ACP stdio agent is that the SDK uses an **event emitter pattern** instead of a transport connection:

| ACP Stdio (via `AcpAgent`) | SDK (via `ClineAgent`) |
|-----------------------------|------------------------|
| Session updates sent over JSON-RPC stdio | Session updates emitted via `ClineSessionEmitter` |
| Permissions requested via `connection.requestPermission()` | Permissions requested via `setPermissionHandler()` callback |
| Single process, single connection | Embeddable, multiple concurrent sessions |

If you need stdio-based ACP communication (e.g., for IDE integration), use the `cline` CLI binary directly. The SDK is for embedding Cline in your own Node.js processes.



---

# FILE: docs/docs.json

{
	"$schema": "https://mintlify.com/docs.json",
	"theme": "mint",
	"name": "Cline",
	"description": "AI-powered coding agent for complex work",
	"colors": {
		"primary": "#9D4EDD",
		"light": "#F0E6FF",
		"dark": "#000000"
	},
	"logo": {
		"light": "/assets/Cline_Logo-complete_black.png",
		"dark": "/assets/Cline_Logo-complete_white.png"
	},
	"favicon": {
		"light": "/assets/robot_panel_light.png",
		"dark": "/assets/robot_panel_dark.png"
	},
	"background": {
		"color": {
			"light": "#fafaf9",
			"dark": "#0f0f0f"
		}
	},
	"styling": {
		"eyebrows": "breadcrumbs",
		"codeblocks": "system",
		"css": "styles.css"
	},
	"appearance": {
		"default": "system",
		"strict": false
	},
	"fonts": {
		"family": "Geist Sans"
	},
	"navbar": {
		"links": [
			{
				"label": "GitHub",
				"icon": "github",
				"href": "https://github.com/cline/cline"
			},
			{
				"label": "Discord",
				"icon": "discord",
				"href": "https://discord.gg/cline"
			}
		],
		"primary": {
			"type": "button",
			"label": "Install Cline",
			"href": "https://cline.bot/install?utm_source=website&utm_medium=header"
		}
	},
	"navigation": {
		"tabs": [
			{
				"tab": "Docs",
				"icon": "square-terminal",
				"groups": [
					{
						"group": "Home",
						"pages": [
							"home",
							"getting-started/quick-start"
						]
					},
					{
						"group": "Getting Started",
						"pages": [
							"getting-started/what-is-cline",
							"getting-started/installing-cline",
							"getting-started/authorizing-with-cline",
							"getting-started/your-first-project"
						]
					},
					{
						"group": "Core Workflows",
						"pages": [
							"core-workflows/task-management",
							"core-workflows/plan-and-act",
							"core-workflows/working-with-files",
							"core-workflows/using-commands",
							"core-workflows/checkpoints"
						]
					},
					{
						"group": "Customization",
						"pages": [
							"customization/overview",
							"customization/cline-rules",
							"customization/skills",
							"customization/workflows",
							"customization/hooks",
							"customization/clineignore"
						]
					},
					{
						"group": "Cline CLI",
						"pages": [
							"cline-cli/overview",
							"cline-cli/installation",
							"cline-sdk/overview",
							"cline-cli/interactive-mode",
							{
								"group": "Headless Mode",
								"pages": [
									"cline-cli/three-core-flows",
									"cline-cli/samples/overview",
									"cline-cli/samples/github-issue-rca",
									"cline-cli/samples/github-integration",
									"cline-cli/samples/github-pr-review",
									"cline-cli/samples/model-orchestration",
									"cline-cli/samples/worktree-workflows"
								]
							},
							"cline-cli/configuration",
							"cline-cli/acp-editor-integrations",
							"cline-cli/cli-reference"
						]
					},
					{
						"group": "Features",
						"pages": [
							"features/memory-bank",
							"features/focus-chain",
							"features/auto-approve",
							"features/auto-compact",
							"features/multiroot-workspace",
							"features/subagents",
							"features/background-edit",
							"features/jupyter-notebooks",
							"features/deep-planning",
							"features/web-tools",
							"features/worktrees"
						]
					},
					{
						"group": "Models & Providers",
						"pages": [
							{
								"group": "Choosing & Configuring Models",
								"pages": [
									"core-features/model-selection-guide",
									"model-config/context-windows"
								]
							},
							{
								"group": "Running Models Locally",
								"pages": [
									"running-models-locally/overview",
									"running-models-locally/ollama",
									"running-models-locally/lm-studio"
								]
							},
							{
								"group": "Cloud Providers",
								"pages": [
									"provider-config/qwen",
									"provider-config/anthropic",
									"provider-config/asksage",
									"provider-config/baseten",
									"provider-config/cerebras",
									"provider-config/claude-code",
									"provider-config/deepseek",
									"provider-config/doubao",
									"provider-config/fireworks",
									"provider-config/gcp-vertex-ai",
									"provider-config/google-gemini",
									"provider-config/groq",
									"provider-config/huawei-cloud-maas",
									"provider-config/huggingface",
									"provider-config/minimax",
									"provider-config/mistral-ai",
									"provider-config/moonshot",
									"provider-config/nebius",
									"provider-config/nousresearch",
									"provider-config/openai",
									"provider-config/openai-codex",
									"provider-config/openrouter",
									"provider-config/oracle-code-assist",
									"provider-config/qwen-code",
									"provider-config/sambanova",
									"provider-config/together",
									"provider-config/xai-grok",
									"provider-config/zai",
									{
										"group": "AWS Bedrock",
										"pages": [
											"provider-config/aws-bedrock/api-key",
											"provider-config/aws-bedrock/iam-credentials",
											"provider-config/aws-bedrock/cli-profile"
										]
									}
								]
							},
							{
								"group": "Advanced Configuration",
								"pages": [
									"provider-config/aihubmix",
									"provider-config/dify",
									"provider-config/hicap",
									"provider-config/litellm-and-cline-using-codestral",
									"provider-config/openai-compatible",
									"provider-config/requesty",
									"provider-config/sap-aicore",
									"provider-config/vercel-ai-gateway",
									"provider-config/vscode-language-model-api"
								]
							}
						]
					},
					{
						"group": "MCP (Extending Cline)",
						"pages": [
							"mcp/mcp-overview",
							"mcp/mcp-marketplace",
							"mcp/adding-and-configuring-servers",
							"mcp/mcp-server-development-protocol",
							"mcp/connecting-to-a-remote-server",
							"mcp/mcp-transport-mechanisms"
						]
					},
					{
						"group": "Tools Reference",
						"pages": [
							"tools-reference/all-cline-tools",
							"tools-reference/browser-automation"
						]
					},
					{
						"group": "Troubleshooting",
						"pages": [
							"troubleshooting/terminal-quick-fixes",
							"troubleshooting/networking-and-proxies",
							"troubleshooting/task-history-recovery"
						]
					},
					{
						"group": "Contributing",
						"pages": [
							"contributing/documentation-guide",
							"contributing/doc-templates"
						]
					}
				]
			},
			{
				"tab": "Enterprise",
				"icon": "building",
				"groups": [
					{
						"group": "Enterprise Solutions",
						"pages": [
							"enterprise-solutions/overview",
							"enterprise-solutions/onboarding",
							"enterprise-solutions/sso-setup",
							"enterprise-solutions/team-management/managing-members",
							{
								"group": "Remote Provider Configuration",
								"pages": [
									"enterprise-solutions/configuration/remote-configuration/overview",
									{
										"group": "AWS Bedrock",
										"pages": [
											"enterprise-solutions/configuration/remote-configuration/aws-bedrock/admin-configuration",
											"enterprise-solutions/configuration/remote-configuration/aws-bedrock/member-configuration"
										]
									},
									{
										"group": "Google Vertex AI",
										"pages": [
											"enterprise-solutions/configuration/remote-configuration/google-vertex/admin-configuration",
											"enterprise-solutions/configuration/remote-configuration/google-vertex/member-configuration"
										]
									},
									{
										"group": "OpenAI Compatible",
										"pages": [
											"enterprise-solutions/configuration/remote-configuration/openai-compatible/admin-configuration",
											"enterprise-solutions/configuration/remote-configuration/openai-compatible/member-configuration"
										]
									},
									{
										"group": "Anthropic",
										"pages": [
											"enterprise-solutions/configuration/remote-configuration/anthropic/admin-configuration",
											"enterprise-solutions/configuration/remote-configuration/anthropic/member-configuration"
										]
									},
									{
										"group": "LiteLLM",
										"pages": [
											"enterprise-solutions/configuration/remote-configuration/litellm/admin-configuration",
											"enterprise-solutions/configuration/remote-configuration/litellm/member-configuration"
										]
									}
								]
							},
							{
								"group": "Control Other Cline Features",
								"pages": [
									"enterprise-solutions/configuration/infrastructure-configuration/control-other-cline-features/yolo-mode",
									"enterprise-solutions/configuration/infrastructure-configuration/control-other-cline-features/mcp-marketplace"
								]
							},
							{
								"group": "Monitoring",
								"pages": [
									"enterprise-solutions/monitoring/overview",
									"enterprise-solutions/monitoring/telemetry",
									"enterprise-solutions/monitoring/opentelemetry"
								]
							},
							"enterprise-solutions/api-reference"
						]
					}
				]
			},
			{
				"tab": "API",
				"icon": "code",
				"groups": [
					{
						"group": "Cline API",
						"pages": [
							"api/overview",
							"api/getting-started",
							"api/authentication"
						]
					},
					{
						"group": "Endpoints",
						"pages": [
							"api/chat-completions"
						]
					},
					{
						"group": "Reference",
						"pages": [
							"api/models",
							"api/errors",
							"api/sdk-examples"
						]
					}
				]
			},
			{
				"tab": "Kanban",
				"icon": "table-columns",
				"groups": [
					{
						"group": "Cline Kanban",
						"pages": [
							"kanban/overview",
							"kanban/getting-started",
							"kanban/core-workflow",
							"kanban/features"
						]
					}
				]
			},
			{
				"tab": "Learn",
				"icon": "graduation-cap",
				"href": "https://cline.bot/learn"
			}
		]
	},
	"footer": {
		"socials": {
			"x": "https://x.com/cline",
			"github": "https://github.com/cline/cline",
			"discord": "https://discord.gg/cline"
		}
	},
	"anchors": [
		{
			"name": "Overview",
			"icon": "house",
			"url": "getting-started/what-is-cline"
		}
	],
	"redirects": [
		{
			"source": "/getting-started/installing-cline-jetbrains",
			"destination": "/getting-started/installing-cline"
		},
		{
			"source": "/getting-started/overview",
			"destination": "/getting-started/what-is-cline"
		},
		{
			"source": "/introduction",
			"destination": "/getting-started/what-is-cline"
		},
		{
			"source": "/introduction/welcome",
			"destination": "/getting-started/what-is-cline"
		},
		{
			"source": "/introduction/overview",
			"destination": "/getting-started/what-is-cline"
		},
		{
			"source": "/getting-started/model-selection-guide",
			"destination": "/core-features/model-selection-guide"
		},
		{
			"source": "/provider-config/ollama",
			"destination": "/running-models-locally/ollama"
		},
		{
			"source": "/running-models-locally/read-me-first",
			"destination": "/running-models-locally/overview"
		},
		{
			"source": "/getting-started/understanding-context-management",
			"destination": "/model-config/context-windows"
		},
		{
			"source": "/best-practices/understanding-context-management",
			"destination": "/model-config/context-windows"
		},
		{
			"source": "/prompting/understanding-context-management",
			"destination": "/model-config/context-windows"
		},
		{
			"source": "/prompting/prompt-engineering-guide",
			"destination": "/customization/cline-rules"
		},
		{
			"source": "/prompting/cline-memory-bank",
			"destination": "/features/memory-bank"
		},
		{
			"source": "/customization/memory-bank",
			"destination": "/features/memory-bank"
		},
		{
			"source": "/customization/focus-chain",
			"destination": "/features/focus-chain"
		},
		{
			"source": "/customization/auto-approve",
			"destination": "/features/auto-approve"
		},
		{
			"source": "/customization/auto-compact",
			"destination": "/features/auto-compact"
		},
		{
			"source": "/getting-started/your-first-task",
			"destination": "/getting-started/your-first-project"
		},
		{
			"source": "/cline-cli/samples",
			"destination": "/cline-cli/samples/overview"
		},
		{
			"source": "/cline-cli/overview",
			"destination": "/cline-cli/getting-started"
		},
		{
			"source": "/features/hooks/real-world-examples",
			"destination": "/customization/hooks"
		},
		{
			"source": "/features/hooks/index",
			"destination": "/customization/hooks"
		},
		{
			"source": "/features/hooks/hook-reference",
			"destination": "/customization/hooks"
		},
		{
			"source": "/features/hooks/samples",
			"destination": "/customization/hooks"
		},
		{
			"source": "/features/plan-and-act",
			"destination": "/core-workflows/plan-and-act"
		},
		{
			"source": "/features/checkpoints",
			"destination": "/core-workflows/checkpoints"
		},
		{
			"source": "/features/tasks/understanding-tasks",
			"destination": "/core-workflows/task-management"
		},
		{
			"source": "/features/tasks/task-management",
			"destination": "/core-workflows/task-management"
		},
		{
			"source": "/features/at-mentions/overview",
			"destination": "/core-workflows/working-with-files"
		},
		{
			"source": "/features/at-mentions/file-mentions",
			"destination": "/core-workflows/working-with-files"
		},
		{
			"source": "/features/at-mentions/folder-mentions",
			"destination": "/core-workflows/working-with-files"
		},
		{
			"source": "/features/at-mentions/terminal-mentions",
			"destination": "/core-workflows/working-with-files"
		},
		{
			"source": "/features/at-mentions/problem-mentions",
			"destination": "/core-workflows/working-with-files"
		},
		{
			"source": "/features/at-mentions/git-mentions",
			"destination": "/core-workflows/working-with-files"
		},
		{
			"source": "/features/at-mentions/url-mentions",
			"destination": "/core-workflows/working-with-files"
		},
		{
			"source": "/features/drag-and-drop",
			"destination": "/core-workflows/working-with-files"
		},
		{
			"source": "/features/yolo-mode",
			"destination": "/features/auto-approve"
		},
		{
			"source": "/features/cline-rules",
			"destination": "/customization/cline-rules"
		},
		{
			"source": "/features/cline-rules/overview",
			"destination": "/customization/cline-rules"
		},
		{
			"source": "/features/cline-rules/conditional-rules",
			"destination": "/customization/cline-rules"
		},
		{
			"source": "/features/commands-and-shortcuts/overview",
			"destination": "/core-workflows/using-commands"
		},
		{
			"source": "/features/commands-and-shortcuts/code-commands",
			"destination": "/core-workflows/using-commands"
		},
		{
			"source": "/features/commands-and-shortcuts/terminal-integration",
			"destination": "/core-workflows/using-commands"
		},
		{
			"source": "/features/commands-and-shortcuts/git-integration",
			"destination": "/core-workflows/using-commands"
		},
		{
			"source": "/features/commands-and-shortcuts/keyboard-shortcuts",
			"destination": "/core-workflows/using-commands"
		},
		{
			"source": "/features/slash-commands/new-task",
			"destination": "/core-workflows/using-commands"
		},
		{
			"source": "/features/slash-commands/workflows/index",
			"destination": "/customization/workflows"
		},
		{
			"source": "/features/slash-commands/workflows/quickstart",
			"destination": "/customization/workflows"
		},
		{
			"source": "/features/slash-commands/workflows/best-practices",
			"destination": "/customization/workflows"
		},
		{
			"source": "/exploring-clines-tools/cline-tools-guide",
			"destination": "/tools-reference/all-cline-tools"
		},
		{
			"source": "/exploring-clines-tools/new-task-tool",
			"destination": "/tools-reference/all-cline-tools"
		},
		{
			"source": "/exploring-clines-tools/remote-browser-support",
			"destination": "/tools-reference/browser-automation"
		},
		{
			"source": "/mcp/adding-mcp-servers-from-github",
			"destination": "/mcp/adding-and-configuring-servers"
		},
		{
			"source": "/mcp/configuring-mcp-servers",
			"destination": "/mcp/adding-and-configuring-servers"
		},
		{
			"source": "/more-info/telemetry",
			"destination": "/enterprise-solutions/monitoring/telemetry"
		},
		{
			"source": "/enterprise-solutions/configure-AWS-Bedrock-Admin",
			"destination": "/enterprise-solutions/configuration/remote-configuration/aws-bedrock/admin-configuration"
		},
		{
			"source": "/enterprise-solutions/configure-AWS-Bedrock-Member",
			"destination": "/enterprise-solutions/configuration/remote-configuration/aws-bedrock/member-configuration"
		},
		{
			"source": "/enterprise-solutions/configure-workOS-authkit",
			"destination": "/enterprise-solutions/onboarding"
		},
		{
			"source": "/enterprise-solutions/Onboarding your Organization",
			"destination": "/enterprise-solutions/onboarding"
		},
		{
			"source": "/enterprise-solutions/team-management/overview",
			"destination": "/enterprise-solutions/team-management/managing-members"
		},
		{
			"source": "/enterprise-solutions/team-management/roles-and-permissions",
			"destination": "/enterprise-solutions/team-management/managing-members"
		},
		{
			"source": "/features/customization/opening-cline-in-sidebar",
			"destination": "/getting-started/installing-cline"
		},
		{
			"source": "/prompting/prompt-engineering-guide/clineignore-file-guide",
			"destination": "/customization/clineignore"
		},
		{
			"source": "/getting-started/selecting-your-model",
			"destination": "/getting-started/authorizing-with-cline"
		},
		{
			"source": "/model-config/model-comparison",
			"destination": "/core-features/model-selection-guide"
		},
		{
			"source": "/troubleshooting/terminal-integration-guide",
			"destination": "/troubleshooting/terminal-quick-fixes"
		},
		{
			"source": "/features/slash-commands/deep-planning",
			"destination": "/features/deep-planning"
		},
		{
			"source": "/features/slash-commands/smol",
			"destination": "/core-workflows/using-commands#smol"
		},
		{
			"source": "/features/slash-commands/explain-changes",
			"destination": "/core-workflows/using-commands#explain-changes"
		},
		{
			"source": "/features/slash-commands/new-rule",
			"destination": "/core-workflows/using-commands#newrule"
		},
		{
			"source": "/features/skills",
			"destination": "/customization/skills"
		},
		{
			"source": "/api/reference",
			"destination": "/api/overview"
		}
	],
	"search": {
		"prompt": "Search Cline documentation..."
	}
}



---

# FILE: docs/package-lock.json

{
	"name": "docs",
	"version": "1.0.0",
	"lockfileVersion": 3,
	"requires": true,
	"packages": {
		"": {
			"name": "docs",
			"version": "1.0.0",
			"license": "ISC",
			"dependencies": {
				"mintlify": "^4.2.338"
			}
		},
		"node_modules/@alcalzone/ansi-tokenize": {
			"version": "0.2.4",
			"resolved": "https://registry.npmjs.org/@alcalzone/ansi-tokenize/-/ansi-tokenize-0.2.4.tgz",
			"integrity": "sha512-HTgrrTgZ9Jgeo6Z3oqbQ7lifOVvRR14vaDuBGPPUxk9Thm+vObaO4QfYYYWw4Zo5CWQDBEfsinFA6Gre+AqwNQ==",
			"license": "MIT",
			"dependencies": {
				"ansi-styles": "^6.2.1",
				"is-fullwidth-code-point": "^5.0.0"
			},
			"engines": {
				"node": ">=18"
			}
		},
		"node_modules/@alloc/quick-lru": {
			"version": "5.2.0",
			"resolved": "https://registry.npmjs.org/@alloc/quick-lru/-/quick-lru-5.2.0.tgz",
			"integrity": "sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==",
			"license": "MIT",
			"engines": {
				"node": ">=10"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/@ark/schema": {
			"version": "0.55.0",
			"resolved": "https://registry.npmjs.org/@ark/schema/-/schema-0.55.0.tgz",
			"integrity": "sha512-IlSIc0FmLKTDGr4I/FzNHauMn0MADA6bCjT1wauu4k6MyxhC1R9gz0olNpIRvK7lGGDwtc/VO0RUDNvVQW5WFg==",
			"license": "MIT",
			"dependencies": {
				"@ark/util": "0.55.0"
			}
		},
		"node_modules/@ark/util": {
			"version": "0.55.0",
			"resolved": "https://registry.npmjs.org/@ark/util/-/util-0.55.0.tgz",
			"integrity": "sha512-aWFNK7aqSvqFtVsl1xmbTjGbg91uqtJV7Za76YGNEwIO4qLjMfyY8flmmbhooYMuqPCO2jyxu8hve943D+w3bA==",
			"license": "MIT"
		},
		"node_modules/@asyncapi/parser": {
			"version": "3.4.0",
			"resolved": "https://registry.npmjs.org/@asyncapi/parser/-/parser-3.4.0.tgz",
			"integrity": "sha512-Sxn74oHiZSU6+cVeZy62iPZMFMvKp4jupMFHelSICCMw1qELmUHPvuZSr+ZHDmNGgHcEpzJM5HN02kR7T4g+PQ==",
			"license": "Apache-2.0",
			"dependencies": {
				"@asyncapi/specs": "^6.8.0",
				"@openapi-contrib/openapi-schema-to-json-schema": "~3.2.0",
				"@stoplight/json": "3.21.0",
				"@stoplight/json-ref-readers": "^1.2.2",
				"@stoplight/json-ref-resolver": "^3.1.5",
				"@stoplight/spectral-core": "^1.18.3",
				"@stoplight/spectral-functions": "^1.7.2",
				"@stoplight/spectral-parsers": "^1.0.2",
				"@stoplight/spectral-ref-resolver": "^1.0.3",
				"@stoplight/types": "^13.12.0",
				"@types/json-schema": "^7.0.11",
				"@types/urijs": "^1.19.19",
				"ajv": "^8.17.1",
				"ajv-errors": "^3.0.0",
				"ajv-formats": "^2.1.1",
				"avsc": "^5.7.5",
				"js-yaml": "^4.1.0",
				"jsonpath-plus": "^10.0.0",
				"node-fetch": "2.6.7"
			}
		},
		"node_modules/@asyncapi/specs": {
			"version": "6.8.1",
			"resolved": "https://registry.npmjs.org/@asyncapi/specs/-/specs-6.8.1.tgz",
			"integrity": "sha512-czHoAk3PeXTLR+X8IUaD+IpT+g+zUvkcgMDJVothBsan+oHN3jfcFcFUNdOPAAFoUCQN1hXF1dWuphWy05THlA==",
			"license": "Apache-2.0",
			"dependencies": {
				"@types/json-schema": "^7.0.11"
			}
		},
		"node_modules/@babel/code-frame": {
			"version": "7.29.0",
			"resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.0.tgz",
			"integrity": "sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw==",
			"license": "MIT",
			"dependencies": {
				"@babel/helper-validator-identifier": "^7.28.5",
				"js-tokens": "^4.0.0",
				"picocolors": "^1.1.1"
			},
			"engines": {
				"node": ">=6.9.0"
			}
		},
		"node_modules/@babel/helper-validator-identifier": {
			"version": "7.28.5",
			"resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
			"integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
			"license": "MIT",
			"engines": {
				"node": ">=6.9.0"
			}
		},
		"node_modules/@canvas/image-data": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/@canvas/image-data/-/image-data-1.1.0.tgz",
			"integrity": "sha512-QdObRRjRbcXGmM1tmJ+MrHcaz1MftF2+W7YI+MsphnsCrmtyfS0d5qJbk0MeSbUeyM/jCb0hmnkXPsy026L7dA==",
			"license": "MIT"
		},
		"node_modules/@emnapi/runtime": {
			"version": "1.8.1",
			"resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.8.1.tgz",
			"integrity": "sha512-mehfKSMWjjNol8659Z8KxEMrdSJDDot5SXMq00dM8BN4o+CLNXQ0xH2V7EchNHV4RmbZLmmPdEaXZc5H2FXmDg==",
			"license": "MIT",
			"optional": true,
			"dependencies": {
				"tslib": "^2.4.0"
			}
		},
		"node_modules/@emnapi/runtime/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD",
			"optional": true
		},
		"node_modules/@floating-ui/core": {
			"version": "1.7.4",
			"resolved": "https://registry.npmjs.org/@floating-ui/core/-/core-1.7.4.tgz",
			"integrity": "sha512-C3HlIdsBxszvm5McXlB8PeOEWfBhcGBTZGkGlWc2U0KFY5IwG5OQEuQ8rq52DZmcHDlPLd+YFBK+cZcytwIFWg==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@floating-ui/utils": "^0.2.10"
			}
		},
		"node_modules/@floating-ui/dom": {
			"version": "1.7.5",
			"resolved": "https://registry.npmjs.org/@floating-ui/dom/-/dom-1.7.5.tgz",
			"integrity": "sha512-N0bD2kIPInNHUHehXhMke1rBGs1dwqvC9O9KYMyyjK7iXt7GAhnro7UlcuYcGdS/yYOlq0MAVgrow8IbWJwyqg==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@floating-ui/core": "^1.7.4",
				"@floating-ui/utils": "^0.2.10"
			}
		},
		"node_modules/@floating-ui/utils": {
			"version": "0.2.10",
			"resolved": "https://registry.npmjs.org/@floating-ui/utils/-/utils-0.2.10.tgz",
			"integrity": "sha512-aGTxbpbg8/b5JfU1HXSrbH3wXZuLPJcNEcZQFMxLs3oSzgtVu6nFPkbbGGUvBcUjKV2YyB9Wxxabo+HEH9tcRQ==",
			"license": "MIT",
			"peer": true
		},
		"node_modules/@img/sharp-darwin-arm64": {
			"version": "0.33.5",
			"resolved": "https://registry.npmjs.org/@img/sharp-darwin-arm64/-/sharp-darwin-arm64-0.33.5.tgz",
			"integrity": "sha512-UT4p+iz/2H4twwAoLCqfA9UH5pI6DggwKEGuaPy7nCVQ8ZsiY5PIcrRvD1DzuY3qYL07NtIQcWnBSY/heikIFQ==",
			"cpu": [
				"arm64"
			],
			"license": "Apache-2.0",
			"optional": true,
			"os": [
				"darwin"
			],
			"engines": {
				"node": "^18.17.0 || ^20.3.0 || >=21.0.0"
			},
			"funding": {
				"url": "https://opencollective.com/libvips"
			},
			"optionalDependencies": {
				"@img/sharp-libvips-darwin-arm64": "1.0.4"
			}
		},
		"node_modules/@img/sharp-darwin-x64": {
			"version": "0.33.5",
			"resolved": "https://registry.npmjs.org/@img/sharp-darwin-x64/-/sharp-darwin-x64-0.33.5.tgz",
			"integrity": "sha512-fyHac4jIc1ANYGRDxtiqelIbdWkIuQaI84Mv45KvGRRxSAa7o7d1ZKAOBaYbnepLC1WqxfpimdeWfvqqSGwR2Q==",
			"cpu": [
				"x64"
			],
			"license": "Apache-2.0",
			"optional": true,
			"os": [
				"darwin"
			],
			"engines": {
				"node": "^18.17.0 || ^20.3.0 || >=21.0.0"
			},
			"funding": {
				"url": "https://opencollective.com/libvips"
			},
			"optionalDependencies": {
				"@img/sharp-libvips-darwin-x64": "1.0.4"
			}
		},
		"node_modules/@img/sharp-libvips-darwin-arm64": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/@img/sharp-libvips-darwin-arm64/-/sharp-libvips-darwin-arm64-1.0.4.tgz",
			"integrity": "sha512-XblONe153h0O2zuFfTAbQYAX2JhYmDHeWikp1LM9Hul9gVPjFY427k6dFEcOL72O01QxQsWi761svJ/ev9xEDg==",
			"cpu": [
				"arm64"
			],
			"license": "LGPL-3.0-or-later",
			"optional": true,
			"os": [
				"darwin"
			],
			"funding": {
				"url": "https://opencollective.com/libvips"
			}
		},
		"node_modules/@img/sharp-libvips-darwin-x64": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/@img/sharp-libvips-darwin-x64/-/sharp-libvips-darwin-x64-1.0.4.tgz",
			"integrity": "sha512-xnGR8YuZYfJGmWPvmlunFaWJsb9T/AO2ykoP3Fz/0X5XV2aoYBPkX6xqCQvUTKKiLddarLaxpzNe+b1hjeWHAQ==",
			"cpu": [
				"x64"
			],
			"license": "LGPL-3.0-or-later",
			"optional": true,
			"os": [
				"darwin"
			],
			"funding": {
				"url": "https://opencollective.com/libvips"
			}
		},
		"node_modules/@img/sharp-libvips-linux-arm": {
			"version": "1.0.5",
			"resolved": "https://registry.npmjs.org/@img/sharp-libvips-linux-arm/-/sharp-libvips-linux-arm-1.0.5.tgz",
			"integrity": "sha512-gvcC4ACAOPRNATg/ov8/MnbxFDJqf/pDePbBnuBDcjsI8PssmjoKMAz4LtLaVi+OnSb5FK/yIOamqDwGmXW32g==",
			"cpu": [
				"arm"
			],
			"license": "LGPL-3.0-or-later",
			"optional": true,
			"os": [
				"linux"
			],
			"funding": {
				"url": "https://opencollective.com/libvips"
			}
		},
		"node_modules/@img/sharp-libvips-linux-arm64": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/@img/sharp-libvips-linux-arm64/-/sharp-libvips-linux-arm64-1.0.4.tgz",
			"integrity": "sha512-9B+taZ8DlyyqzZQnoeIvDVR/2F4EbMepXMc/NdVbkzsJbzkUjhXv/70GQJ7tdLA4YJgNP25zukcxpX2/SueNrA==",
			"cpu": [
				"arm64"
			],
			"license": "LGPL-3.0-or-later",
			"optional": true,
			"os": [
				"linux"
			],
			"funding": {
				"url": "https://opencollective.com/libvips"
			}
		},
		"node_modules/@img/sharp-libvips-linux-s390x": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/@img/sharp-libvips-linux-s390x/-/sharp-libvips-linux-s390x-1.0.4.tgz",
			"integrity": "sha512-u7Wz6ntiSSgGSGcjZ55im6uvTrOxSIS8/dgoVMoiGE9I6JAfU50yH5BoDlYA1tcuGS7g/QNtetJnxA6QEsCVTA==",
			"cpu": [
				"s390x"
			],
			"license": "LGPL-3.0-or-later",
			"optional": true,
			"os": [
				"linux"
			],
			"funding": {
				"url": "https://opencollective.com/libvips"
			}
		},
		"node_modules/@img/sharp-libvips-linux-x64": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/@img/sharp-libvips-linux-x64/-/sharp-libvips-linux-x64-1.0.4.tgz",
			"integrity": "sha512-MmWmQ3iPFZr0Iev+BAgVMb3ZyC4KeFc3jFxnNbEPas60e1cIfevbtuyf9nDGIzOaW9PdnDciJm+wFFaTlj5xYw==",
			"cpu": [
				"x64"
			],
			"license": "LGPL-3.0-or-later",
			"optional": true,
			"os": [
				"linux"
			],
			"funding": {
				"url": "https://opencollective.com/libvips"
			}
		},
		"node_modules/@img/sharp-libvips-linuxmusl-arm64": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/@img/sharp-libvips-linuxmusl-arm64/-/sharp-libvips-linuxmusl-arm64-1.0.4.tgz",
			"integrity": "sha512-9Ti+BbTYDcsbp4wfYib8Ctm1ilkugkA/uscUn6UXK1ldpC1JjiXbLfFZtRlBhjPZ5o1NCLiDbg8fhUPKStHoTA==",
			"cpu": [
				"arm64"
			],
			"license": "LGPL-3.0-or-later",
			"optional": true,
			"os": [
				"linux"
			],
			"funding": {
				"url": "https://opencollective.com/libvips"
			}
		},
		"node_modules/@img/sharp-libvips-linuxmusl-x64": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/@img/sharp-libvips-linuxmusl-x64/-/sharp-libvips-linuxmusl-x64-1.0.4.tgz",
			"integrity": "sha512-viYN1KX9m+/hGkJtvYYp+CCLgnJXwiQB39damAO7WMdKWlIhmYTfHjwSbQeUK/20vY154mwezd9HflVFM1wVSw==",
			"cpu": [
				"x64"
			],
			"license": "LGPL-3.0-or-later",
			"optional": true,
			"os": [
				"linux"
			],
			"funding": {
				"url": "https://opencollective.com/libvips"
			}
		},
		"node_modules/@img/sharp-linux-arm": {
			"version": "0.33.5",
			"resolved": "https://registry.npmjs.org/@img/sharp-linux-arm/-/sharp-linux-arm-0.33.5.tgz",
			"integrity": "sha512-JTS1eldqZbJxjvKaAkxhZmBqPRGmxgu+qFKSInv8moZ2AmT5Yib3EQ1c6gp493HvrvV8QgdOXdyaIBrhvFhBMQ==",
			"cpu": [
				"arm"
			],
			"license": "Apache-2.0",
			"optional": true,
			"os": [
				"linux"
			],
			"engines": {
				"node": "^18.17.0 || ^20.3.0 || >=21.0.0"
			},
			"funding": {
				"url": "https://opencollective.com/libvips"
			},
			"optionalDependencies": {
				"@img/sharp-libvips-linux-arm": "1.0.5"
			}
		},
		"node_modules/@img/sharp-linux-arm64": {
			"version": "0.33.5",
			"resolved": "https://registry.npmjs.org/@img/sharp-linux-arm64/-/sharp-linux-arm64-0.33.5.tgz",
			"integrity": "sha512-JMVv+AMRyGOHtO1RFBiJy/MBsgz0x4AWrT6QoEVVTyh1E39TrCUpTRI7mx9VksGX4awWASxqCYLCV4wBZHAYxA==",
			"cpu": [
				"arm64"
			],
			"license": "Apache-2.0",
			"optional": true,
			"os": [
				"linux"
			],
			"engines": {
				"node": "^18.17.0 || ^20.3.0 || >=21.0.0"
			},
			"funding": {
				"url": "https://opencollective.com/libvips"
			},
			"optionalDependencies": {
				"@img/sharp-libvips-linux-arm64": "1.0.4"
			}
		},
		"node_modules/@img/sharp-linux-s390x": {
			"version": "0.33.5",
			"resolved": "https://registry.npmjs.org/@img/sharp-linux-s390x/-/sharp-linux-s390x-0.33.5.tgz",
			"integrity": "sha512-y/5PCd+mP4CA/sPDKl2961b+C9d+vPAveS33s6Z3zfASk2j5upL6fXVPZi7ztePZ5CuH+1kW8JtvxgbuXHRa4Q==",
			"cpu": [
				"s390x"
			],
			"license": "Apache-2.0",
			"optional": true,
			"os": [
				"linux"
			],
			"engines": {
				"node": "^18.17.0 || ^20.3.0 || >=21.0.0"
			},
			"funding": {
				"url": "https://opencollective.com/libvips"
			},
			"optionalDependencies": {
				"@img/sharp-libvips-linux-s390x": "1.0.4"
			}
		},
		"node_modules/@img/sharp-linux-x64": {
			"version": "0.33.5",
			"resolved": "https://registry.npmjs.org/@img/sharp-linux-x64/-/sharp-linux-x64-0.33.5.tgz",
			"integrity": "sha512-opC+Ok5pRNAzuvq1AG0ar+1owsu842/Ab+4qvU879ippJBHvyY5n2mxF1izXqkPYlGuP/M556uh53jRLJmzTWA==",
			"cpu": [
				"x64"
			],
			"license": "Apache-2.0",
			"optional": true,
			"os": [
				"linux"
			],
			"engines": {
				"node": "^18.17.0 || ^20.3.0 || >=21.0.0"
			},
			"funding": {
				"url": "https://opencollective.com/libvips"
			},
			"optionalDependencies": {
				"@img/sharp-libvips-linux-x64": "1.0.4"
			}
		},
		"node_modules/@img/sharp-linuxmusl-arm64": {
			"version": "0.33.5",
			"resolved": "https://registry.npmjs.org/@img/sharp-linuxmusl-arm64/-/sharp-linuxmusl-arm64-0.33.5.tgz",
			"integrity": "sha512-XrHMZwGQGvJg2V/oRSUfSAfjfPxO+4DkiRh6p2AFjLQztWUuY/o8Mq0eMQVIY7HJ1CDQUJlxGGZRw1a5bqmd1g==",
			"cpu": [
				"arm64"
			],
			"license": "Apache-2.0",
			"optional": true,
			"os": [
				"linux"
			],
			"engines": {
				"node": "^18.17.0 || ^20.3.0 || >=21.0.0"
			},
			"funding": {
				"url": "https://opencollective.com/libvips"
			},
			"optionalDependencies": {
				"@img/sharp-libvips-linuxmusl-arm64": "1.0.4"
			}
		},
		"node_modules/@img/sharp-linuxmusl-x64": {
			"version": "0.33.5",
			"resolved": "https://registry.npmjs.org/@img/sharp-linuxmusl-x64/-/sharp-linuxmusl-x64-0.33.5.tgz",
			"integrity": "sha512-WT+d/cgqKkkKySYmqoZ8y3pxx7lx9vVejxW/W4DOFMYVSkErR+w7mf2u8m/y4+xHe7yY9DAXQMWQhpnMuFfScw==",
			"cpu": [
				"x64"
			],
			"license": "Apache-2.0",
			"optional": true,
			"os": [
				"linux"
			],
			"engines": {
				"node": "^18.17.0 || ^20.3.0 || >=21.0.0"
			},
			"funding": {
				"url": "https://opencollective.com/libvips"
			},
			"optionalDependencies": {
				"@img/sharp-libvips-linuxmusl-x64": "1.0.4"
			}
		},
		"node_modules/@img/sharp-wasm32": {
			"version": "0.33.5",
			"resolved": "https://registry.npmjs.org/@img/sharp-wasm32/-/sharp-wasm32-0.33.5.tgz",
			"integrity": "sha512-ykUW4LVGaMcU9lu9thv85CbRMAwfeadCJHRsg2GmeRa/cJxsVY9Rbd57JcMxBkKHag5U/x7TSBpScF4U8ElVzg==",
			"cpu": [
				"wasm32"
			],
			"license": "Apache-2.0 AND LGPL-3.0-or-later AND MIT",
			"optional": true,
			"dependencies": {
				"@emnapi/runtime": "^1.2.0"
			},
			"engines": {
				"node": "^18.17.0 || ^20.3.0 || >=21.0.0"
			},
			"funding": {
				"url": "https://opencollective.com/libvips"
			}
		},
		"node_modules/@img/sharp-win32-ia32": {
			"version": "0.33.5",
			"resolved": "https://registry.npmjs.org/@img/sharp-win32-ia32/-/sharp-win32-ia32-0.33.5.tgz",
			"integrity": "sha512-T36PblLaTwuVJ/zw/LaH0PdZkRz5rd3SmMHX8GSmR7vtNSP5Z6bQkExdSK7xGWyxLw4sUknBuugTelgw2faBbQ==",
			"cpu": [
				"ia32"
			],
			"license": "Apache-2.0 AND LGPL-3.0-or-later",
			"optional": true,
			"os": [
				"win32"
			],
			"engines": {
				"node": "^18.17.0 || ^20.3.0 || >=21.0.0"
			},
			"funding": {
				"url": "https://opencollective.com/libvips"
			}
		},
		"node_modules/@img/sharp-win32-x64": {
			"version": "0.33.5",
			"resolved": "https://registry.npmjs.org/@img/sharp-win32-x64/-/sharp-win32-x64-0.33.5.tgz",
			"integrity": "sha512-MpY/o8/8kj+EcnxwvrP4aTJSWw/aZ7JIGR4aBeZkZw5B7/Jn+tY9/VNwtcoGmdT7GfggGIU4kygOMSbYnOrAbg==",
			"cpu": [
				"x64"
			],
			"license": "Apache-2.0 AND LGPL-3.0-or-later",
			"optional": true,
			"os": [
				"win32"
			],
			"engines": {
				"node": "^18.17.0 || ^20.3.0 || >=21.0.0"
			},
			"funding": {
				"url": "https://opencollective.com/libvips"
			}
		},
		"node_modules/@inquirer/ansi": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/@inquirer/ansi/-/ansi-1.0.2.tgz",
			"integrity": "sha512-S8qNSZiYzFd0wAcyG5AXCvUHC5Sr7xpZ9wZ2py9XR88jUz8wooStVx5M6dRzczbBWjic9NP7+rY0Xi7qqK/aMQ==",
			"license": "MIT",
			"engines": {
				"node": ">=18"
			}
		},
		"node_modules/@inquirer/checkbox": {
			"version": "4.3.2",
			"resolved": "https://registry.npmjs.org/@inquirer/checkbox/-/checkbox-4.3.2.tgz",
			"integrity": "sha512-VXukHf0RR1doGe6Sm4F0Em7SWYLTHSsbGfJdS9Ja2bX5/D5uwVOEjr07cncLROdBvmnvCATYEWlHqYmXv2IlQA==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/ansi": "^1.0.2",
				"@inquirer/core": "^10.3.2",
				"@inquirer/figures": "^1.0.15",
				"@inquirer/type": "^3.0.10",
				"yoctocolors-cjs": "^2.1.3"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/confirm": {
			"version": "5.1.21",
			"resolved": "https://registry.npmjs.org/@inquirer/confirm/-/confirm-5.1.21.tgz",
			"integrity": "sha512-KR8edRkIsUayMXV+o3Gv+q4jlhENF9nMYUZs9PA2HzrXeHI8M5uDag70U7RJn9yyiMZSbtF5/UexBtAVtZGSbQ==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/core": "^10.3.2",
				"@inquirer/type": "^3.0.10"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/core": {
			"version": "10.3.2",
			"resolved": "https://registry.npmjs.org/@inquirer/core/-/core-10.3.2.tgz",
			"integrity": "sha512-43RTuEbfP8MbKzedNqBrlhhNKVwoK//vUFNW3Q3vZ88BLcrs4kYpGg+B2mm5p2K/HfygoCxuKwJJiv8PbGmE0A==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/ansi": "^1.0.2",
				"@inquirer/figures": "^1.0.15",
				"@inquirer/type": "^3.0.10",
				"cli-width": "^4.1.0",
				"mute-stream": "^2.0.0",
				"signal-exit": "^4.1.0",
				"wrap-ansi": "^6.2.0",
				"yoctocolors-cjs": "^2.1.3"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/editor": {
			"version": "4.2.23",
			"resolved": "https://registry.npmjs.org/@inquirer/editor/-/editor-4.2.23.tgz",
			"integrity": "sha512-aLSROkEwirotxZ1pBaP8tugXRFCxW94gwrQLxXfrZsKkfjOYC1aRvAZuhpJOb5cu4IBTJdsCigUlf2iCOu4ZDQ==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/core": "^10.3.2",
				"@inquirer/external-editor": "^1.0.3",
				"@inquirer/type": "^3.0.10"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/expand": {
			"version": "4.0.23",
			"resolved": "https://registry.npmjs.org/@inquirer/expand/-/expand-4.0.23.tgz",
			"integrity": "sha512-nRzdOyFYnpeYTTR2qFwEVmIWypzdAx/sIkCMeTNTcflFOovfqUk+HcFhQQVBftAh9gmGrpFj6QcGEqrDMDOiew==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/core": "^10.3.2",
				"@inquirer/type": "^3.0.10",
				"yoctocolors-cjs": "^2.1.3"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/external-editor": {
			"version": "1.0.3",
			"resolved": "https://registry.npmjs.org/@inquirer/external-editor/-/external-editor-1.0.3.tgz",
			"integrity": "sha512-RWbSrDiYmO4LbejWY7ttpxczuwQyZLBUyygsA9Nsv95hpzUWwnNTVQmAq3xuh7vNwCp07UTmE5i11XAEExx4RA==",
			"license": "MIT",
			"dependencies": {
				"chardet": "^2.1.1",
				"iconv-lite": "^0.7.0"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/figures": {
			"version": "1.0.15",
			"resolved": "https://registry.npmjs.org/@inquirer/figures/-/figures-1.0.15.tgz",
			"integrity": "sha512-t2IEY+unGHOzAaVM5Xx6DEWKeXlDDcNPeDyUpsRc6CUhBfU3VQOEl+Vssh7VNp1dR8MdUJBWhuObjXCsVpjN5g==",
			"license": "MIT",
			"engines": {
				"node": ">=18"
			}
		},
		"node_modules/@inquirer/input": {
			"version": "4.3.1",
			"resolved": "https://registry.npmjs.org/@inquirer/input/-/input-4.3.1.tgz",
			"integrity": "sha512-kN0pAM4yPrLjJ1XJBjDxyfDduXOuQHrBB8aLDMueuwUGn+vNpF7Gq7TvyVxx8u4SHlFFj4trmj+a2cbpG4Jn1g==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/core": "^10.3.2",
				"@inquirer/type": "^3.0.10"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/number": {
			"version": "3.0.23",
			"resolved": "https://registry.npmjs.org/@inquirer/number/-/number-3.0.23.tgz",
			"integrity": "sha512-5Smv0OK7K0KUzUfYUXDXQc9jrf8OHo4ktlEayFlelCjwMXz0299Y8OrI+lj7i4gCBY15UObk76q0QtxjzFcFcg==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/core": "^10.3.2",
				"@inquirer/type": "^3.0.10"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/password": {
			"version": "4.0.23",
			"resolved": "https://registry.npmjs.org/@inquirer/password/-/password-4.0.23.tgz",
			"integrity": "sha512-zREJHjhT5vJBMZX/IUbyI9zVtVfOLiTO66MrF/3GFZYZ7T4YILW5MSkEYHceSii/KtRk+4i3RE7E1CUXA2jHcA==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/ansi": "^1.0.2",
				"@inquirer/core": "^10.3.2",
				"@inquirer/type": "^3.0.10"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/prompts": {
			"version": "7.9.0",
			"resolved": "https://registry.npmjs.org/@inquirer/prompts/-/prompts-7.9.0.tgz",
			"integrity": "sha512-X7/+dG9SLpSzRkwgG5/xiIzW0oMrV3C0HOa7YHG1WnrLK+vCQHfte4k/T80059YBdei29RBC3s+pSMvPJDU9/A==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/checkbox": "^4.3.0",
				"@inquirer/confirm": "^5.1.19",
				"@inquirer/editor": "^4.2.21",
				"@inquirer/expand": "^4.0.21",
				"@inquirer/input": "^4.2.5",
				"@inquirer/number": "^3.0.21",
				"@inquirer/password": "^4.0.21",
				"@inquirer/rawlist": "^4.1.9",
				"@inquirer/search": "^3.2.0",
				"@inquirer/select": "^4.4.0"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/rawlist": {
			"version": "4.1.11",
			"resolved": "https://registry.npmjs.org/@inquirer/rawlist/-/rawlist-4.1.11.tgz",
			"integrity": "sha512-+LLQB8XGr3I5LZN/GuAHo+GpDJegQwuPARLChlMICNdwW7OwV2izlCSCxN6cqpL0sMXmbKbFcItJgdQq5EBXTw==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/core": "^10.3.2",
				"@inquirer/type": "^3.0.10",
				"yoctocolors-cjs": "^2.1.3"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/search": {
			"version": "3.2.2",
			"resolved": "https://registry.npmjs.org/@inquirer/search/-/search-3.2.2.tgz",
			"integrity": "sha512-p2bvRfENXCZdWF/U2BXvnSI9h+tuA8iNqtUKb9UWbmLYCRQxd8WkvwWvYn+3NgYaNwdUkHytJMGG4MMLucI1kA==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/core": "^10.3.2",
				"@inquirer/figures": "^1.0.15",
				"@inquirer/type": "^3.0.10",
				"yoctocolors-cjs": "^2.1.3"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/select": {
			"version": "4.4.2",
			"resolved": "https://registry.npmjs.org/@inquirer/select/-/select-4.4.2.tgz",
			"integrity": "sha512-l4xMuJo55MAe+N7Qr4rX90vypFwCajSakx59qe/tMaC1aEHWLyw68wF4o0A4SLAY4E0nd+Vt+EyskeDIqu1M6w==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/ansi": "^1.0.2",
				"@inquirer/core": "^10.3.2",
				"@inquirer/figures": "^1.0.15",
				"@inquirer/type": "^3.0.10",
				"yoctocolors-cjs": "^2.1.3"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@inquirer/type": {
			"version": "3.0.10",
			"resolved": "https://registry.npmjs.org/@inquirer/type/-/type-3.0.10.tgz",
			"integrity": "sha512-BvziSRxfz5Ov8ch0z/n3oijRSEcEsHnhggm4xFZe93DHcUCTlutlq9Ox4SVENAfcRD22UQq7T/atg9Wr3k09eA==",
			"license": "MIT",
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			},
			"peerDependenciesMeta": {
				"@types/node": {
					"optional": true
				}
			}
		},
		"node_modules/@jridgewell/gen-mapping": {
			"version": "0.3.13",
			"resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz",
			"integrity": "sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==",
			"license": "MIT",
			"dependencies": {
				"@jridgewell/sourcemap-codec": "^1.5.0",
				"@jridgewell/trace-mapping": "^0.3.24"
			}
		},
		"node_modules/@jridgewell/resolve-uri": {
			"version": "3.1.2",
			"resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
			"integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
			"license": "MIT",
			"engines": {
				"node": ">=6.0.0"
			}
		},
		"node_modules/@jridgewell/sourcemap-codec": {
			"version": "1.5.5",
			"resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
			"integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
			"license": "MIT"
		},
		"node_modules/@jridgewell/trace-mapping": {
			"version": "0.3.31",
			"resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz",
			"integrity": "sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==",
			"license": "MIT",
			"dependencies": {
				"@jridgewell/resolve-uri": "^3.1.0",
				"@jridgewell/sourcemap-codec": "^1.4.14"
			}
		},
		"node_modules/@jsep-plugin/assignment": {
			"version": "1.3.0",
			"resolved": "https://registry.npmjs.org/@jsep-plugin/assignment/-/assignment-1.3.0.tgz",
			"integrity": "sha512-VVgV+CXrhbMI3aSusQyclHkenWSAm95WaiKrMxRFam3JSUiIaQjoMIw2sEs/OX4XifnqeQUN4DYbJjlA8EfktQ==",
			"license": "MIT",
			"engines": {
				"node": ">= 10.16.0"
			},
			"peerDependencies": {
				"jsep": "^0.4.0||^1.0.0"
			}
		},
		"node_modules/@jsep-plugin/regex": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/@jsep-plugin/regex/-/regex-1.0.4.tgz",
			"integrity": "sha512-q7qL4Mgjs1vByCaTnDFcBnV9HS7GVPJX5vyVoCgZHNSC9rjwIlmbXG5sUuorR5ndfHAIlJ8pVStxvjXHbNvtUg==",
			"license": "MIT",
			"engines": {
				"node": ">= 10.16.0"
			},
			"peerDependencies": {
				"jsep": "^0.4.0||^1.0.0"
			}
		},
		"node_modules/@jsep-plugin/ternary": {
			"version": "1.1.4",
			"resolved": "https://registry.npmjs.org/@jsep-plugin/ternary/-/ternary-1.1.4.tgz",
			"integrity": "sha512-ck5wiqIbqdMX6WRQztBL7ASDty9YLgJ3sSAK5ZpBzXeySvFGCzIvM6UiAI4hTZ22fEcYQVV/zhUbNscggW+Ukg==",
			"license": "MIT",
			"engines": {
				"node": ">= 10.16.0"
			},
			"peerDependencies": {
				"jsep": "^0.4.0||^1.0.0"
			}
		},
		"node_modules/@leichtgewicht/ip-codec": {
			"version": "2.0.5",
			"resolved": "https://registry.npmjs.org/@leichtgewicht/ip-codec/-/ip-codec-2.0.5.tgz",
			"integrity": "sha512-Vo+PSpZG2/fmgmiNzYK9qWRh8h/CHrwD0mo1h1DzL4yzHNSfWYujGTYsWGreD000gcgmZ7K4Ys6Tx9TxtsKdDw==",
			"license": "MIT"
		},
		"node_modules/@mdx-js/mdx": {
			"version": "3.1.1",
			"resolved": "https://registry.npmjs.org/@mdx-js/mdx/-/mdx-3.1.1.tgz",
			"integrity": "sha512-f6ZO2ifpwAQIpzGWaBQT2TXxPv6z3RBzQKpVftEWN78Vl/YweF1uwussDx8ECAXVtr3Rs89fKyG9YlzUs9DyGQ==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0",
				"@types/estree-jsx": "^1.0.0",
				"@types/hast": "^3.0.0",
				"@types/mdx": "^2.0.0",
				"acorn": "^8.0.0",
				"collapse-white-space": "^2.0.0",
				"devlop": "^1.0.0",
				"estree-util-is-identifier-name": "^3.0.0",
				"estree-util-scope": "^1.0.0",
				"estree-walker": "^3.0.0",
				"hast-util-to-jsx-runtime": "^2.0.0",
				"markdown-extensions": "^2.0.0",
				"recma-build-jsx": "^1.0.0",
				"recma-jsx": "^1.0.0",
				"recma-stringify": "^1.0.0",
				"rehype-recma": "^1.0.0",
				"remark-mdx": "^3.0.0",
				"remark-parse": "^11.0.0",
				"remark-rehype": "^11.0.0",
				"source-map": "^0.7.0",
				"unified": "^11.0.0",
				"unist-util-position-from-estree": "^2.0.0",
				"unist-util-stringify-position": "^4.0.0",
				"unist-util-visit": "^5.0.0",
				"vfile": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mdx-js/react": {
			"version": "3.1.1",
			"resolved": "https://registry.npmjs.org/@mdx-js/react/-/react-3.1.1.tgz",
			"integrity": "sha512-f++rKLQgUVYDAtECQ6fn/is15GkEH9+nZPM3MS0RcxVqoTfawHvDlSCH7JbMhAM6uJ32v3eXLvLmLvjGu7PTQw==",
			"license": "MIT",
			"dependencies": {
				"@types/mdx": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			},
			"peerDependencies": {
				"@types/react": ">=16",
				"react": ">=16"
			}
		},
		"node_modules/@mintlify/cli": {
			"version": "4.0.942",
			"resolved": "https://registry.npmjs.org/@mintlify/cli/-/cli-4.0.942.tgz",
			"integrity": "sha512-kxWLWC9CKKGvLFM8t8gT7a7R9dfvW8B7/og8a18tn29tIYe0p/JId7SWdPSbDfzI78KbcSNvTd0vnPzyAqC9Lg==",
			"license": "Elastic-2.0",
			"dependencies": {
				"@inquirer/prompts": "7.9.0",
				"@mintlify/common": "1.0.719",
				"@mintlify/link-rot": "3.0.879",
				"@mintlify/models": "0.0.270",
				"@mintlify/prebuild": "1.0.855",
				"@mintlify/previewing": "4.0.912",
				"@mintlify/validation": "0.1.589",
				"adm-zip": "0.5.16",
				"chalk": "5.2.0",
				"color": "4.2.3",
				"detect-port": "1.5.1",
				"front-matter": "4.0.2",
				"fs-extra": "11.2.0",
				"ink": "6.3.0",
				"inquirer": "12.3.0",
				"js-yaml": "4.1.0",
				"mdast-util-mdx-jsx": "3.2.0",
				"react": "19.2.3",
				"semver": "7.7.2",
				"unist-util-visit": "5.0.0",
				"yargs": "17.7.1"
			},
			"bin": {
				"mint": "bin/index.js",
				"mintlify": "bin/index.js"
			},
			"engines": {
				"node": ">=18.0.0"
			}
		},
		"node_modules/@mintlify/common": {
			"version": "1.0.719",
			"resolved": "https://registry.npmjs.org/@mintlify/common/-/common-1.0.719.tgz",
			"integrity": "sha512-QLQqQfdY+UtP0M020kQL9bhs9NoCcW7BHrp6E8QfSb7RCEVyEtN9rNx9vYvemwsJkIwM0h/Gb/G5FCLVUj6S7g==",
			"license": "ISC",
			"dependencies": {
				"@asyncapi/parser": "3.4.0",
				"@asyncapi/specs": "6.8.1",
				"@mintlify/mdx": "^3.0.4",
				"@mintlify/models": "0.0.270",
				"@mintlify/openapi-parser": "^0.0.8",
				"@mintlify/validation": "0.1.589",
				"@sindresorhus/slugify": "2.2.0",
				"@types/mdast": "4.0.4",
				"acorn": "8.11.2",
				"acorn-jsx": "5.3.2",
				"color-blend": "4.0.0",
				"estree-util-to-js": "2.0.0",
				"estree-walker": "3.0.3",
				"front-matter": "4.0.2",
				"hast-util-from-html": "2.0.3",
				"hast-util-to-html": "9.0.4",
				"hast-util-to-text": "4.0.2",
				"hex-rgb": "5.0.0",
				"ignore": "7.0.5",
				"js-yaml": "4.1.0",
				"lodash": "4.17.21",
				"mdast-util-from-markdown": "2.0.2",
				"mdast-util-gfm": "3.0.0",
				"mdast-util-mdx": "3.0.0",
				"mdast-util-mdx-jsx": "3.1.3",
				"micromark-extension-gfm": "3.0.0",
				"micromark-extension-mdx-jsx": "3.0.1",
				"micromark-extension-mdxjs": "3.0.0",
				"openapi-types": "12.1.3",
				"postcss": "8.5.6",
				"rehype-stringify": "10.0.1",
				"remark": "15.0.1",
				"remark-frontmatter": "5.0.0",
				"remark-gfm": "4.0.0",
				"remark-math": "6.0.0",
				"remark-mdx": "3.1.0",
				"remark-parse": "11.0.0",
				"remark-rehype": "11.1.1",
				"remark-stringify": "11.0.0",
				"tailwindcss": "3.4.4",
				"unified": "11.0.5",
				"unist-builder": "4.0.0",
				"unist-util-map": "4.0.0",
				"unist-util-remove": "4.0.0",
				"unist-util-remove-position": "5.0.0",
				"unist-util-visit": "5.0.0",
				"unist-util-visit-parents": "6.0.1",
				"vfile": "6.0.3"
			}
		},
		"node_modules/@mintlify/common/node_modules/@floating-ui/react-dom": {
			"version": "2.1.7",
			"resolved": "https://registry.npmjs.org/@floating-ui/react-dom/-/react-dom-2.1.7.tgz",
			"integrity": "sha512-0tLRojf/1Go2JgEVm+3Frg9A3IW8bJgKgdO0BN5RkF//ufuz2joZM63Npau2ff3J6lUVYgDSNzNkR+aH3IVfjg==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@floating-ui/dom": "^1.7.5"
			},
			"peerDependencies": {
				"react": ">=16.8.0",
				"react-dom": ">=16.8.0"
			}
		},
		"node_modules/@mintlify/common/node_modules/@mintlify/mdx": {
			"version": "3.0.4",
			"resolved": "https://registry.npmjs.org/@mintlify/mdx/-/mdx-3.0.4.tgz",
			"integrity": "sha512-tJhdpnM5ReJLNJ2fuDRIEr0zgVd6id7/oAIfs26V46QlygiLsc8qx4Rz3LWIX51rUXW/cfakjj0EATxIciIw+g==",
			"license": "MIT",
			"dependencies": {
				"@shikijs/transformers": "^3.11.0",
				"@shikijs/twoslash": "^3.12.2",
				"arktype": "^2.1.26",
				"hast-util-to-string": "^3.0.1",
				"mdast-util-from-markdown": "^2.0.2",
				"mdast-util-gfm": "^3.1.0",
				"mdast-util-mdx-jsx": "^3.2.0",
				"mdast-util-to-hast": "^13.2.0",
				"next-mdx-remote-client": "^1.0.3",
				"rehype-katex": "^7.0.1",
				"remark-gfm": "^4.0.0",
				"remark-math": "^6.0.0",
				"remark-smartypants": "^3.0.2",
				"shiki": "^3.11.0",
				"unified": "^11.0.0",
				"unist-util-visit": "^5.0.0"
			},
			"peerDependencies": {
				"@radix-ui/react-popover": "^1.1.15",
				"react": "^18.3.1",
				"react-dom": "^18.3.1"
			}
		},
		"node_modules/@mintlify/common/node_modules/@mintlify/mdx/node_modules/mdast-util-gfm": {
			"version": "3.1.0",
			"resolved": "https://registry.npmjs.org/mdast-util-gfm/-/mdast-util-gfm-3.1.0.tgz",
			"integrity": "sha512-0ulfdQOM3ysHhCJ1p06l0b0VKlhU0wuQs3thxZQagjcjPrlFRqY215uZGHHJan9GEAXd9MbfPjFJz+qMkVR6zQ==",
			"license": "MIT",
			"dependencies": {
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-gfm-autolink-literal": "^2.0.0",
				"mdast-util-gfm-footnote": "^2.0.0",
				"mdast-util-gfm-strikethrough": "^2.0.0",
				"mdast-util-gfm-table": "^2.0.0",
				"mdast-util-gfm-task-list-item": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/common/node_modules/@mintlify/mdx/node_modules/mdast-util-mdx-jsx": {
			"version": "3.2.0",
			"resolved": "https://registry.npmjs.org/mdast-util-mdx-jsx/-/mdast-util-mdx-jsx-3.2.0.tgz",
			"integrity": "sha512-lj/z8v0r6ZtsN/cGNNtemmmfoLAFZnjMbNyLzBafjzikOM+glrjNHPlf6lQDOTccj9n5b0PPihEBbhneMyGs1Q==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"@types/hast": "^3.0.0",
				"@types/mdast": "^4.0.0",
				"@types/unist": "^3.0.0",
				"ccount": "^2.0.0",
				"devlop": "^1.1.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0",
				"parse-entities": "^4.0.0",
				"stringify-entities": "^4.0.0",
				"unist-util-stringify-position": "^4.0.0",
				"vfile-message": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/common/node_modules/@radix-ui/react-arrow": {
			"version": "1.1.7",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-arrow/-/react-arrow-1.1.7.tgz",
			"integrity": "sha512-F+M1tLhO+mlQaOWspE8Wstg+z6PwxwRd8oQ8IXceWz92kfAmalTRf0EjrouQeo7QssEPfCn05B4Ihs1K9WQ/7w==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-primitive": "2.1.3"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/common/node_modules/@radix-ui/react-dismissable-layer": {
			"version": "1.1.11",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-dismissable-layer/-/react-dismissable-layer-1.1.11.tgz",
			"integrity": "sha512-Nqcp+t5cTB8BinFkZgXiMJniQH0PsUt2k51FUhbdfeKvc4ACcG2uQniY/8+h1Yv6Kza4Q7lD7PQV0z0oicE0Mg==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/primitive": "1.1.3",
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-use-callback-ref": "1.1.1",
				"@radix-ui/react-use-escape-keydown": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/common/node_modules/@radix-ui/react-focus-scope": {
			"version": "1.1.7",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-focus-scope/-/react-focus-scope-1.1.7.tgz",
			"integrity": "sha512-t2ODlkXBQyn7jkl6TNaw/MtVEVvIGelJDCG41Okq/KwUsJBwQ4XVZsHAVUkK4mBv3ewiAS3PGuUWuY2BoK4ZUw==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-use-callback-ref": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/common/node_modules/@radix-ui/react-popover": {
			"version": "1.1.15",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-popover/-/react-popover-1.1.15.tgz",
			"integrity": "sha512-kr0X2+6Yy/vJzLYJUPCZEc8SfQcf+1COFoAqauJm74umQhta9M7lNJHP7QQS3vkvcGLQUbWpMzwrXYwrYztHKA==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/primitive": "1.1.3",
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-context": "1.1.2",
				"@radix-ui/react-dismissable-layer": "1.1.11",
				"@radix-ui/react-focus-guards": "1.1.3",
				"@radix-ui/react-focus-scope": "1.1.7",
				"@radix-ui/react-id": "1.1.1",
				"@radix-ui/react-popper": "1.2.8",
				"@radix-ui/react-portal": "1.1.9",
				"@radix-ui/react-presence": "1.1.5",
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-slot": "1.2.3",
				"@radix-ui/react-use-controllable-state": "1.2.2",
				"aria-hidden": "^1.2.4",
				"react-remove-scroll": "^2.6.3"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/common/node_modules/@radix-ui/react-popper": {
			"version": "1.2.8",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-popper/-/react-popper-1.2.8.tgz",
			"integrity": "sha512-0NJQ4LFFUuWkE7Oxf0htBKS6zLkkjBH+hM1uk7Ng705ReR8m/uelduy1DBo0PyBXPKVnBA6YBlU94MBGXrSBCw==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@floating-ui/react-dom": "^2.0.0",
				"@radix-ui/react-arrow": "1.1.7",
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-context": "1.1.2",
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-use-callback-ref": "1.1.1",
				"@radix-ui/react-use-layout-effect": "1.1.1",
				"@radix-ui/react-use-rect": "1.1.1",
				"@radix-ui/react-use-size": "1.1.1",
				"@radix-ui/rect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/common/node_modules/@radix-ui/react-portal": {
			"version": "1.1.9",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-portal/-/react-portal-1.1.9.tgz",
			"integrity": "sha512-bpIxvq03if6UNwXZ+HTK71JLh4APvnXntDc6XOX8UVq4XQOVl7lwok0AvIl+b8zgCw3fSaVTZMpAPPagXbKmHQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-use-layout-effect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/common/node_modules/@radix-ui/react-presence": {
			"version": "1.1.5",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-presence/-/react-presence-1.1.5.tgz",
			"integrity": "sha512-/jfEwNDdQVBCNvjkGit4h6pMOzq8bHkopq458dPt2lMjx+eBQUohZNG9A7DtO/O5ukSbxuaNGXMjHicgwy6rQQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-use-layout-effect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/common/node_modules/@radix-ui/react-primitive": {
			"version": "2.1.3",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-primitive/-/react-primitive-2.1.3.tgz",
			"integrity": "sha512-m9gTwRkhy2lvCPe6QJp4d3G1TYEUHn/FzJUtq9MjH46an1wJU+GdoGC5VLof8RX8Ft/DlpshApkhswDLZzHIcQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-slot": "1.2.3"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/common/node_modules/mdast-util-mdx-jsx": {
			"version": "3.1.3",
			"resolved": "https://registry.npmjs.org/mdast-util-mdx-jsx/-/mdast-util-mdx-jsx-3.1.3.tgz",
			"integrity": "sha512-bfOjvNt+1AcbPLTFMFWY149nJz0OjmewJs3LQQ5pIyVGxP4CdOqNVJL6kTaM5c68p8q82Xv3nCyFfUnuEcH3UQ==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"@types/hast": "^3.0.0",
				"@types/mdast": "^4.0.0",
				"@types/unist": "^3.0.0",
				"ccount": "^2.0.0",
				"devlop": "^1.1.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0",
				"parse-entities": "^4.0.0",
				"stringify-entities": "^4.0.0",
				"unist-util-stringify-position": "^4.0.0",
				"vfile-message": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/common/node_modules/next-mdx-remote-client": {
			"version": "1.1.4",
			"resolved": "https://registry.npmjs.org/next-mdx-remote-client/-/next-mdx-remote-client-1.1.4.tgz",
			"integrity": "sha512-psCMdO50tfoT1kAH7OGXZvhyRfiHVK6IqwjmWFV5gtLo4dnqjAgcjcLNeJ92iI26UNlKShxYrBs1GQ6UXxk97A==",
			"license": "MPL 2.0",
			"dependencies": {
				"@babel/code-frame": "^7.27.1",
				"@mdx-js/mdx": "^3.1.1",
				"@mdx-js/react": "^3.1.1",
				"remark-mdx-remove-esm": "^1.2.1",
				"serialize-error": "^12.0.0",
				"vfile": "^6.0.3",
				"vfile-matter": "^5.0.1"
			},
			"engines": {
				"node": ">=18.18.0"
			},
			"peerDependencies": {
				"react": ">= 18.3.0 < 19.0.0",
				"react-dom": ">= 18.3.0 < 19.0.0"
			}
		},
		"node_modules/@mintlify/common/node_modules/react": {
			"version": "18.3.1",
			"resolved": "https://registry.npmjs.org/react/-/react-18.3.1.tgz",
			"integrity": "sha512-wS+hAgJShR0KhEvPJArfuPVN1+Hz1t0Y6n5jLrGQbkb4urgPE/0Rve+1kMB1v/oWgHgm4WIcV+i7F2pTVj+2iQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"loose-envify": "^1.1.0"
			},
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/@mintlify/common/node_modules/react-dom": {
			"version": "18.3.1",
			"resolved": "https://registry.npmjs.org/react-dom/-/react-dom-18.3.1.tgz",
			"integrity": "sha512-5m4nQKp+rZRb09LNH59GM4BxTh9251/ylbKIbpe7TpGxfJ+9kv6BLkLBXIjjspbgbnIBNqlI23tRnTWT0snUIw==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"loose-envify": "^1.1.0",
				"scheduler": "^0.23.2"
			},
			"peerDependencies": {
				"react": "^18.3.1"
			}
		},
		"node_modules/@mintlify/common/node_modules/scheduler": {
			"version": "0.23.2",
			"resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.23.2.tgz",
			"integrity": "sha512-UOShsPwz7NrMUqhR6t0hWjFduvOzbtv7toDH1/hIrfRNIDBnnBWd0CwJTGvTpngVlmwGCdP9/Zl/tVrDqcuYzQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"loose-envify": "^1.1.0"
			}
		},
		"node_modules/@mintlify/link-rot": {
			"version": "3.0.879",
			"resolved": "https://registry.npmjs.org/@mintlify/link-rot/-/link-rot-3.0.879.tgz",
			"integrity": "sha512-ZJeMcQ2Yx+Qk4IQnt8kAW+jElLsSs9dZJRF/m5S893TAHJknBHfJQ4H2a751wKukfMfSzSLCNTEph3WYQHyzKQ==",
			"license": "Elastic-2.0",
			"dependencies": {
				"@mintlify/common": "1.0.719",
				"@mintlify/prebuild": "1.0.855",
				"@mintlify/previewing": "4.0.912",
				"@mintlify/scraping": "4.0.522",
				"@mintlify/validation": "0.1.589",
				"fs-extra": "11.1.0",
				"unist-util-visit": "4.1.2"
			},
			"engines": {
				"node": ">=18.0.0"
			}
		},
		"node_modules/@mintlify/link-rot/node_modules/@types/unist": {
			"version": "2.0.11",
			"resolved": "https://registry.npmjs.org/@types/unist/-/unist-2.0.11.tgz",
			"integrity": "sha512-CmBKiL6NNo/OqgmMn95Fk9Whlp2mtvIv+KNpQKN2F4SjvrEesubTRWGYSg+BnWZOnlCaSTU1sMpsBOzgbYhnsA==",
			"license": "MIT"
		},
		"node_modules/@mintlify/link-rot/node_modules/fs-extra": {
			"version": "11.1.0",
			"resolved": "https://registry.npmjs.org/fs-extra/-/fs-extra-11.1.0.tgz",
			"integrity": "sha512-0rcTq621PD5jM/e0a3EJoGC/1TC5ZBCERW82LQuwfGnCa1V8w7dpYH1yNu+SLb6E5dkeCBzKEyLGlFrnr+dUyw==",
			"license": "MIT",
			"dependencies": {
				"graceful-fs": "^4.2.0",
				"jsonfile": "^6.0.1",
				"universalify": "^2.0.0"
			},
			"engines": {
				"node": ">=14.14"
			}
		},
		"node_modules/@mintlify/link-rot/node_modules/unist-util-is": {
			"version": "5.2.1",
			"resolved": "https://registry.npmjs.org/unist-util-is/-/unist-util-is-5.2.1.tgz",
			"integrity": "sha512-u9njyyfEh43npf1M+yGKDGVPbY/JWEemg5nH05ncKPfi+kBbKBJoTdsogMu33uhytuLlv9y0O7GH7fEdwLdLQw==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/link-rot/node_modules/unist-util-visit": {
			"version": "4.1.2",
			"resolved": "https://registry.npmjs.org/unist-util-visit/-/unist-util-visit-4.1.2.tgz",
			"integrity": "sha512-MSd8OUGISqHdVvfY9TPhyK2VdUrPgxkUtWSuMHF6XAAFuL4LokseigBnZtPnJMu+FbynTkFNnFlyjxpVKujMRg==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^2.0.0",
				"unist-util-is": "^5.0.0",
				"unist-util-visit-parents": "^5.1.1"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/link-rot/node_modules/unist-util-visit-parents": {
			"version": "5.1.3",
			"resolved": "https://registry.npmjs.org/unist-util-visit-parents/-/unist-util-visit-parents-5.1.3.tgz",
			"integrity": "sha512-x6+y8g7wWMyQhL1iZfhIPhDAs7Xwbn9nRosDXl7qoPTSCy0yNxnKc+hWokFifWQIDGi154rdUqKvbCa4+1kLhg==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^2.0.0",
				"unist-util-is": "^5.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/models": {
			"version": "0.0.270",
			"resolved": "https://registry.npmjs.org/@mintlify/models/-/models-0.0.270.tgz",
			"integrity": "sha512-pVh+w17RiYn31Vij4U8cyQhLGpn9HdaSsq/8ttxpgIXUC4lfvumL4TyFjuoxLX/kt5ex+W1p0Bwd03NWSgg0Hg==",
			"license": "Elastic-2.0",
			"dependencies": {
				"axios": "1.13.2",
				"openapi-types": "12.1.3"
			},
			"engines": {
				"node": ">=18.0.0"
			}
		},
		"node_modules/@mintlify/openapi-parser": {
			"version": "0.0.8",
			"resolved": "https://registry.npmjs.org/@mintlify/openapi-parser/-/openapi-parser-0.0.8.tgz",
			"integrity": "sha512-9MBRq9lS4l4HITYCrqCL7T61MOb20q9IdU7HWhqYMNMM1jGO1nHjXasFy61yZ8V6gMZyyKQARGVoZ0ZrYN48Og==",
			"license": "MIT",
			"dependencies": {
				"ajv": "^8.17.1",
				"ajv-draft-04": "^1.0.0",
				"ajv-formats": "^3.0.1",
				"jsonpointer": "^5.0.1",
				"leven": "^4.0.0",
				"yaml": "^2.4.5"
			},
			"engines": {
				"node": ">=18"
			}
		},
		"node_modules/@mintlify/openapi-parser/node_modules/ajv-formats": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/ajv-formats/-/ajv-formats-3.0.1.tgz",
			"integrity": "sha512-8iUql50EUR+uUcdRQ3HDqa6EVyo3docL8g5WJ3FNcWmu62IbkGUue/pEyLBW8VGKKucTPgqeks4fIU1DA4yowQ==",
			"license": "MIT",
			"dependencies": {
				"ajv": "^8.0.0"
			},
			"peerDependencies": {
				"ajv": "^8.0.0"
			},
			"peerDependenciesMeta": {
				"ajv": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/prebuild": {
			"version": "1.0.855",
			"resolved": "https://registry.npmjs.org/@mintlify/prebuild/-/prebuild-1.0.855.tgz",
			"integrity": "sha512-Hd7WMkM89eu58J1oIW+0lfsoW1QIjFHHo2ks1mdrjXJ7Bm6MvPcsYhYDxtWBSJpU8KMxzjjfC2rd9UWnrRMhRA==",
			"license": "Elastic-2.0",
			"dependencies": {
				"@mintlify/common": "1.0.719",
				"@mintlify/openapi-parser": "^0.0.8",
				"@mintlify/scraping": "4.0.580",
				"@mintlify/validation": "0.1.589",
				"chalk": "5.3.0",
				"favicons": "7.2.0",
				"front-matter": "4.0.2",
				"fs-extra": "11.1.0",
				"js-yaml": "4.1.0",
				"openapi-types": "12.1.3",
				"sharp": "0.33.5",
				"sharp-ico": "0.1.5",
				"unist-util-visit": "4.1.2",
				"uuid": "11.1.0"
			}
		},
		"node_modules/@mintlify/prebuild/node_modules/@mintlify/scraping": {
			"version": "4.0.580",
			"resolved": "https://registry.npmjs.org/@mintlify/scraping/-/scraping-4.0.580.tgz",
			"integrity": "sha512-5F84qwnZ1RkkBXaquvpNDj11J5xc1ayXyeJpjW6SwBJWekIVnCvrea/OmHBmmFRgCg6HjuM8NeB2XO06HrhqYw==",
			"license": "Elastic-2.0",
			"dependencies": {
				"@mintlify/common": "1.0.719",
				"@mintlify/openapi-parser": "^0.0.8",
				"fs-extra": "11.1.1",
				"hast-util-to-mdast": "10.1.0",
				"js-yaml": "4.1.0",
				"mdast-util-mdx-jsx": "3.1.3",
				"neotraverse": "0.6.18",
				"puppeteer": "22.14.0",
				"rehype-parse": "9.0.1",
				"remark-gfm": "4.0.0",
				"remark-mdx": "3.0.1",
				"remark-parse": "11.0.0",
				"remark-stringify": "11.0.0",
				"unified": "11.0.5",
				"unist-util-visit": "5.0.0",
				"yargs": "17.7.1",
				"zod": "3.24.0"
			},
			"bin": {
				"mintlify-scrape": "bin/cli.js"
			},
			"engines": {
				"node": ">=18.0.0"
			}
		},
		"node_modules/@mintlify/prebuild/node_modules/@mintlify/scraping/node_modules/fs-extra": {
			"version": "11.1.1",
			"resolved": "https://registry.npmjs.org/fs-extra/-/fs-extra-11.1.1.tgz",
			"integrity": "sha512-MGIE4HOvQCeUCzmlHs0vXpih4ysz4wg9qiSAu6cd42lVwPbTM1TjV7RusoyQqMmk/95gdQZX72u+YW+c3eEpFQ==",
			"license": "MIT",
			"dependencies": {
				"graceful-fs": "^4.2.0",
				"jsonfile": "^6.0.1",
				"universalify": "^2.0.0"
			},
			"engines": {
				"node": ">=14.14"
			}
		},
		"node_modules/@mintlify/prebuild/node_modules/@mintlify/scraping/node_modules/unist-util-visit": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/unist-util-visit/-/unist-util-visit-5.0.0.tgz",
			"integrity": "sha512-MR04uvD+07cwl/yhVuVWAtw+3GOR/knlL55Nd/wAdblk27GCVt3lqpTivy/tkJcZoNPzTwS1Y+KMojlLDhoTzg==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0",
				"unist-util-is": "^6.0.0",
				"unist-util-visit-parents": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/prebuild/node_modules/chalk": {
			"version": "5.3.0",
			"resolved": "https://registry.npmjs.org/chalk/-/chalk-5.3.0.tgz",
			"integrity": "sha512-dLitG79d+GV1Nb/VYcCDFivJeK1hiukt9QjRNVOsUtTy1rR1YJsmpGGTZ3qJos+uw7WmWF4wUwBd9jxjocFC2w==",
			"license": "MIT",
			"engines": {
				"node": "^12.17.0 || ^14.13 || >=16.0.0"
			},
			"funding": {
				"url": "https://github.com/chalk/chalk?sponsor=1"
			}
		},
		"node_modules/@mintlify/prebuild/node_modules/fs-extra": {
			"version": "11.1.0",
			"resolved": "https://registry.npmjs.org/fs-extra/-/fs-extra-11.1.0.tgz",
			"integrity": "sha512-0rcTq621PD5jM/e0a3EJoGC/1TC5ZBCERW82LQuwfGnCa1V8w7dpYH1yNu+SLb6E5dkeCBzKEyLGlFrnr+dUyw==",
			"license": "MIT",
			"dependencies": {
				"graceful-fs": "^4.2.0",
				"jsonfile": "^6.0.1",
				"universalify": "^2.0.0"
			},
			"engines": {
				"node": ">=14.14"
			}
		},
		"node_modules/@mintlify/prebuild/node_modules/mdast-util-mdx-jsx": {
			"version": "3.1.3",
			"resolved": "https://registry.npmjs.org/mdast-util-mdx-jsx/-/mdast-util-mdx-jsx-3.1.3.tgz",
			"integrity": "sha512-bfOjvNt+1AcbPLTFMFWY149nJz0OjmewJs3LQQ5pIyVGxP4CdOqNVJL6kTaM5c68p8q82Xv3nCyFfUnuEcH3UQ==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"@types/hast": "^3.0.0",
				"@types/mdast": "^4.0.0",
				"@types/unist": "^3.0.0",
				"ccount": "^2.0.0",
				"devlop": "^1.1.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0",
				"parse-entities": "^4.0.0",
				"stringify-entities": "^4.0.0",
				"unist-util-stringify-position": "^4.0.0",
				"vfile-message": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/prebuild/node_modules/remark-mdx": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/remark-mdx/-/remark-mdx-3.0.1.tgz",
			"integrity": "sha512-3Pz3yPQ5Rht2pM5R+0J2MrGoBSrzf+tJG94N+t/ilfdh8YLyyKYtidAYwTveB20BoHAcwIopOUqhcmh2F7hGYA==",
			"license": "MIT",
			"dependencies": {
				"mdast-util-mdx": "^3.0.0",
				"micromark-extension-mdxjs": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/prebuild/node_modules/unist-util-visit": {
			"version": "4.1.2",
			"resolved": "https://registry.npmjs.org/unist-util-visit/-/unist-util-visit-4.1.2.tgz",
			"integrity": "sha512-MSd8OUGISqHdVvfY9TPhyK2VdUrPgxkUtWSuMHF6XAAFuL4LokseigBnZtPnJMu+FbynTkFNnFlyjxpVKujMRg==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^2.0.0",
				"unist-util-is": "^5.0.0",
				"unist-util-visit-parents": "^5.1.1"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/prebuild/node_modules/unist-util-visit/node_modules/@types/unist": {
			"version": "2.0.11",
			"resolved": "https://registry.npmjs.org/@types/unist/-/unist-2.0.11.tgz",
			"integrity": "sha512-CmBKiL6NNo/OqgmMn95Fk9Whlp2mtvIv+KNpQKN2F4SjvrEesubTRWGYSg+BnWZOnlCaSTU1sMpsBOzgbYhnsA==",
			"license": "MIT"
		},
		"node_modules/@mintlify/prebuild/node_modules/unist-util-visit/node_modules/unist-util-is": {
			"version": "5.2.1",
			"resolved": "https://registry.npmjs.org/unist-util-is/-/unist-util-is-5.2.1.tgz",
			"integrity": "sha512-u9njyyfEh43npf1M+yGKDGVPbY/JWEemg5nH05ncKPfi+kBbKBJoTdsogMu33uhytuLlv9y0O7GH7fEdwLdLQw==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/prebuild/node_modules/unist-util-visit/node_modules/unist-util-visit-parents": {
			"version": "5.1.3",
			"resolved": "https://registry.npmjs.org/unist-util-visit-parents/-/unist-util-visit-parents-5.1.3.tgz",
			"integrity": "sha512-x6+y8g7wWMyQhL1iZfhIPhDAs7Xwbn9nRosDXl7qoPTSCy0yNxnKc+hWokFifWQIDGi154rdUqKvbCa4+1kLhg==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^2.0.0",
				"unist-util-is": "^5.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/prebuild/node_modules/zod": {
			"version": "3.24.0",
			"resolved": "https://registry.npmjs.org/zod/-/zod-3.24.0.tgz",
			"integrity": "sha512-Hz+wiY8yD0VLA2k/+nsg2Abez674dDGTai33SwNvMPuf9uIrBC9eFgIMQxBBbHFxVXi8W+5nX9DcAh9YNSQm/w==",
			"license": "MIT",
			"funding": {
				"url": "https://github.com/sponsors/colinhacks"
			}
		},
		"node_modules/@mintlify/previewing": {
			"version": "4.0.912",
			"resolved": "https://registry.npmjs.org/@mintlify/previewing/-/previewing-4.0.912.tgz",
			"integrity": "sha512-/nRbgh/0JNYLSZphgdAFDK/O+o6YXfuUZ2Jle3l+Yyp4D8Jk+4j2oU9Pao4Z+ahqx6nZTbyx9LM5IZMI41xvbA==",
			"license": "Elastic-2.0",
			"dependencies": {
				"@mintlify/common": "1.0.719",
				"@mintlify/prebuild": "1.0.855",
				"@mintlify/validation": "0.1.589",
				"better-opn": "3.0.2",
				"chalk": "5.2.0",
				"chokidar": "3.5.3",
				"express": "4.18.2",
				"front-matter": "4.0.2",
				"fs-extra": "11.1.0",
				"got": "13.0.0",
				"ink": "6.3.0",
				"ink-spinner": "5.0.0",
				"is-online": "10.0.0",
				"js-yaml": "4.1.0",
				"openapi-types": "12.1.3",
				"react": "19.2.3",
				"socket.io": "4.7.2",
				"tar": "6.1.15",
				"unist-util-visit": "4.1.2",
				"yargs": "17.7.1"
			},
			"engines": {
				"node": ">=18.0.0"
			}
		},
		"node_modules/@mintlify/previewing/node_modules/@types/unist": {
			"version": "2.0.11",
			"resolved": "https://registry.npmjs.org/@types/unist/-/unist-2.0.11.tgz",
			"integrity": "sha512-CmBKiL6NNo/OqgmMn95Fk9Whlp2mtvIv+KNpQKN2F4SjvrEesubTRWGYSg+BnWZOnlCaSTU1sMpsBOzgbYhnsA==",
			"license": "MIT"
		},
		"node_modules/@mintlify/previewing/node_modules/fs-extra": {
			"version": "11.1.0",
			"resolved": "https://registry.npmjs.org/fs-extra/-/fs-extra-11.1.0.tgz",
			"integrity": "sha512-0rcTq621PD5jM/e0a3EJoGC/1TC5ZBCERW82LQuwfGnCa1V8w7dpYH1yNu+SLb6E5dkeCBzKEyLGlFrnr+dUyw==",
			"license": "MIT",
			"dependencies": {
				"graceful-fs": "^4.2.0",
				"jsonfile": "^6.0.1",
				"universalify": "^2.0.0"
			},
			"engines": {
				"node": ">=14.14"
			}
		},
		"node_modules/@mintlify/previewing/node_modules/unist-util-is": {
			"version": "5.2.1",
			"resolved": "https://registry.npmjs.org/unist-util-is/-/unist-util-is-5.2.1.tgz",
			"integrity": "sha512-u9njyyfEh43npf1M+yGKDGVPbY/JWEemg5nH05ncKPfi+kBbKBJoTdsogMu33uhytuLlv9y0O7GH7fEdwLdLQw==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/previewing/node_modules/unist-util-visit": {
			"version": "4.1.2",
			"resolved": "https://registry.npmjs.org/unist-util-visit/-/unist-util-visit-4.1.2.tgz",
			"integrity": "sha512-MSd8OUGISqHdVvfY9TPhyK2VdUrPgxkUtWSuMHF6XAAFuL4LokseigBnZtPnJMu+FbynTkFNnFlyjxpVKujMRg==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^2.0.0",
				"unist-util-is": "^5.0.0",
				"unist-util-visit-parents": "^5.1.1"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/previewing/node_modules/unist-util-visit-parents": {
			"version": "5.1.3",
			"resolved": "https://registry.npmjs.org/unist-util-visit-parents/-/unist-util-visit-parents-5.1.3.tgz",
			"integrity": "sha512-x6+y8g7wWMyQhL1iZfhIPhDAs7Xwbn9nRosDXl7qoPTSCy0yNxnKc+hWokFifWQIDGi154rdUqKvbCa4+1kLhg==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^2.0.0",
				"unist-util-is": "^5.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/scraping": {
			"version": "4.0.522",
			"resolved": "https://registry.npmjs.org/@mintlify/scraping/-/scraping-4.0.522.tgz",
			"integrity": "sha512-PL2k52WT5S5OAgnT2K13bP7J2El6XwiVvQlrLvxDYw5KMMV+y34YVJI8ZscKb4trjitWDgyK0UTq2KN6NQgn6g==",
			"license": "Elastic-2.0",
			"dependencies": {
				"@mintlify/common": "1.0.661",
				"@mintlify/openapi-parser": "^0.0.8",
				"fs-extra": "11.1.1",
				"hast-util-to-mdast": "10.1.0",
				"js-yaml": "4.1.0",
				"mdast-util-mdx-jsx": "3.1.3",
				"neotraverse": "0.6.18",
				"puppeteer": "22.14.0",
				"rehype-parse": "9.0.1",
				"remark-gfm": "4.0.0",
				"remark-mdx": "3.0.1",
				"remark-parse": "11.0.0",
				"remark-stringify": "11.0.0",
				"unified": "11.0.5",
				"unist-util-visit": "5.0.0",
				"yargs": "17.7.1",
				"zod": "3.21.4"
			},
			"bin": {
				"mintlify-scrape": "bin/cli.js"
			},
			"engines": {
				"node": ">=18.0.0"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@floating-ui/react-dom": {
			"version": "2.1.7",
			"resolved": "https://registry.npmjs.org/@floating-ui/react-dom/-/react-dom-2.1.7.tgz",
			"integrity": "sha512-0tLRojf/1Go2JgEVm+3Frg9A3IW8bJgKgdO0BN5RkF//ufuz2joZM63Npau2ff3J6lUVYgDSNzNkR+aH3IVfjg==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@floating-ui/dom": "^1.7.5"
			},
			"peerDependencies": {
				"react": ">=16.8.0",
				"react-dom": ">=16.8.0"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@mintlify/common": {
			"version": "1.0.661",
			"resolved": "https://registry.npmjs.org/@mintlify/common/-/common-1.0.661.tgz",
			"integrity": "sha512-/Hdiblzaomp+AWStQ4smhVMgesQhffzQjC9aYBnmLReNdh2Js+ccQFUaWL3TNIxwiS2esaZvsHSV/D+zyRS3hg==",
			"license": "ISC",
			"dependencies": {
				"@asyncapi/parser": "3.4.0",
				"@mintlify/mdx": "^3.0.4",
				"@mintlify/models": "0.0.255",
				"@mintlify/openapi-parser": "^0.0.8",
				"@mintlify/validation": "0.1.555",
				"@sindresorhus/slugify": "2.2.0",
				"@types/mdast": "4.0.4",
				"acorn": "8.11.2",
				"acorn-jsx": "5.3.2",
				"color-blend": "4.0.0",
				"estree-util-to-js": "2.0.0",
				"estree-walker": "3.0.3",
				"front-matter": "4.0.2",
				"hast-util-from-html": "2.0.3",
				"hast-util-to-html": "9.0.4",
				"hast-util-to-text": "4.0.2",
				"hex-rgb": "5.0.0",
				"ignore": "7.0.5",
				"js-yaml": "4.1.0",
				"lodash": "4.17.21",
				"mdast-util-from-markdown": "2.0.2",
				"mdast-util-gfm": "3.0.0",
				"mdast-util-mdx": "3.0.0",
				"mdast-util-mdx-jsx": "3.1.3",
				"micromark-extension-gfm": "3.0.0",
				"micromark-extension-mdx-jsx": "3.0.1",
				"micromark-extension-mdxjs": "3.0.0",
				"openapi-types": "12.1.3",
				"postcss": "8.5.6",
				"rehype-stringify": "10.0.1",
				"remark": "15.0.1",
				"remark-frontmatter": "5.0.0",
				"remark-gfm": "4.0.0",
				"remark-math": "6.0.0",
				"remark-mdx": "3.1.0",
				"remark-parse": "11.0.0",
				"remark-rehype": "11.1.1",
				"remark-stringify": "11.0.0",
				"tailwindcss": "3.4.4",
				"unified": "11.0.5",
				"unist-builder": "4.0.0",
				"unist-util-map": "4.0.0",
				"unist-util-remove": "4.0.0",
				"unist-util-remove-position": "5.0.0",
				"unist-util-visit": "5.0.0",
				"unist-util-visit-parents": "6.0.1",
				"vfile": "6.0.3"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@mintlify/common/node_modules/remark-mdx": {
			"version": "3.1.0",
			"resolved": "https://registry.npmjs.org/remark-mdx/-/remark-mdx-3.1.0.tgz",
			"integrity": "sha512-Ngl/H3YXyBV9RcRNdlYsZujAmhsxwzxpDzpDEhFBVAGthS4GDgnctpDjgFl/ULx5UEDzqtW1cyBSNKqYYrqLBA==",
			"license": "MIT",
			"dependencies": {
				"mdast-util-mdx": "^3.0.0",
				"micromark-extension-mdxjs": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@mintlify/mdx": {
			"version": "3.0.4",
			"resolved": "https://registry.npmjs.org/@mintlify/mdx/-/mdx-3.0.4.tgz",
			"integrity": "sha512-tJhdpnM5ReJLNJ2fuDRIEr0zgVd6id7/oAIfs26V46QlygiLsc8qx4Rz3LWIX51rUXW/cfakjj0EATxIciIw+g==",
			"license": "MIT",
			"dependencies": {
				"@shikijs/transformers": "^3.11.0",
				"@shikijs/twoslash": "^3.12.2",
				"arktype": "^2.1.26",
				"hast-util-to-string": "^3.0.1",
				"mdast-util-from-markdown": "^2.0.2",
				"mdast-util-gfm": "^3.1.0",
				"mdast-util-mdx-jsx": "^3.2.0",
				"mdast-util-to-hast": "^13.2.0",
				"next-mdx-remote-client": "^1.0.3",
				"rehype-katex": "^7.0.1",
				"remark-gfm": "^4.0.0",
				"remark-math": "^6.0.0",
				"remark-smartypants": "^3.0.2",
				"shiki": "^3.11.0",
				"unified": "^11.0.0",
				"unist-util-visit": "^5.0.0"
			},
			"peerDependencies": {
				"@radix-ui/react-popover": "^1.1.15",
				"react": "^18.3.1",
				"react-dom": "^18.3.1"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@mintlify/mdx/node_modules/mdast-util-gfm": {
			"version": "3.1.0",
			"resolved": "https://registry.npmjs.org/mdast-util-gfm/-/mdast-util-gfm-3.1.0.tgz",
			"integrity": "sha512-0ulfdQOM3ysHhCJ1p06l0b0VKlhU0wuQs3thxZQagjcjPrlFRqY215uZGHHJan9GEAXd9MbfPjFJz+qMkVR6zQ==",
			"license": "MIT",
			"dependencies": {
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-gfm-autolink-literal": "^2.0.0",
				"mdast-util-gfm-footnote": "^2.0.0",
				"mdast-util-gfm-strikethrough": "^2.0.0",
				"mdast-util-gfm-table": "^2.0.0",
				"mdast-util-gfm-task-list-item": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@mintlify/mdx/node_modules/mdast-util-mdx-jsx": {
			"version": "3.2.0",
			"resolved": "https://registry.npmjs.org/mdast-util-mdx-jsx/-/mdast-util-mdx-jsx-3.2.0.tgz",
			"integrity": "sha512-lj/z8v0r6ZtsN/cGNNtemmmfoLAFZnjMbNyLzBafjzikOM+glrjNHPlf6lQDOTccj9n5b0PPihEBbhneMyGs1Q==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"@types/hast": "^3.0.0",
				"@types/mdast": "^4.0.0",
				"@types/unist": "^3.0.0",
				"ccount": "^2.0.0",
				"devlop": "^1.1.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0",
				"parse-entities": "^4.0.0",
				"stringify-entities": "^4.0.0",
				"unist-util-stringify-position": "^4.0.0",
				"vfile-message": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@mintlify/models": {
			"version": "0.0.255",
			"resolved": "https://registry.npmjs.org/@mintlify/models/-/models-0.0.255.tgz",
			"integrity": "sha512-LIUkfA7l7ypHAAuOW74ZJws/NwNRqlDRD/U466jarXvvSlGhJec/6J4/I+IEcBvWDnc9anLFKmnGO04jPKgAsg==",
			"license": "Elastic-2.0",
			"dependencies": {
				"axios": "1.10.0",
				"openapi-types": "12.1.3"
			},
			"engines": {
				"node": ">=18.0.0"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@mintlify/validation": {
			"version": "0.1.555",
			"resolved": "https://registry.npmjs.org/@mintlify/validation/-/validation-0.1.555.tgz",
			"integrity": "sha512-11QVUReL4N5u8wSCgZt4RN7PA0jYQoMEBZ5IrUp5pgb5ZJBOoGV/vPsQrxPPa1cxsUDAuToNhtGxRQtOav/w8w==",
			"license": "Elastic-2.0",
			"dependencies": {
				"@mintlify/mdx": "^3.0.4",
				"@mintlify/models": "0.0.255",
				"arktype": "2.1.27",
				"js-yaml": "4.1.0",
				"lcm": "0.0.3",
				"lodash": "4.17.21",
				"object-hash": "3.0.0",
				"openapi-types": "12.1.3",
				"uuid": "11.1.0",
				"zod": "3.21.4",
				"zod-to-json-schema": "3.20.4"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@radix-ui/react-arrow": {
			"version": "1.1.7",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-arrow/-/react-arrow-1.1.7.tgz",
			"integrity": "sha512-F+M1tLhO+mlQaOWspE8Wstg+z6PwxwRd8oQ8IXceWz92kfAmalTRf0EjrouQeo7QssEPfCn05B4Ihs1K9WQ/7w==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-primitive": "2.1.3"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@radix-ui/react-dismissable-layer": {
			"version": "1.1.11",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-dismissable-layer/-/react-dismissable-layer-1.1.11.tgz",
			"integrity": "sha512-Nqcp+t5cTB8BinFkZgXiMJniQH0PsUt2k51FUhbdfeKvc4ACcG2uQniY/8+h1Yv6Kza4Q7lD7PQV0z0oicE0Mg==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/primitive": "1.1.3",
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-use-callback-ref": "1.1.1",
				"@radix-ui/react-use-escape-keydown": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@radix-ui/react-focus-scope": {
			"version": "1.1.7",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-focus-scope/-/react-focus-scope-1.1.7.tgz",
			"integrity": "sha512-t2ODlkXBQyn7jkl6TNaw/MtVEVvIGelJDCG41Okq/KwUsJBwQ4XVZsHAVUkK4mBv3ewiAS3PGuUWuY2BoK4ZUw==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-use-callback-ref": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@radix-ui/react-popover": {
			"version": "1.1.15",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-popover/-/react-popover-1.1.15.tgz",
			"integrity": "sha512-kr0X2+6Yy/vJzLYJUPCZEc8SfQcf+1COFoAqauJm74umQhta9M7lNJHP7QQS3vkvcGLQUbWpMzwrXYwrYztHKA==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/primitive": "1.1.3",
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-context": "1.1.2",
				"@radix-ui/react-dismissable-layer": "1.1.11",
				"@radix-ui/react-focus-guards": "1.1.3",
				"@radix-ui/react-focus-scope": "1.1.7",
				"@radix-ui/react-id": "1.1.1",
				"@radix-ui/react-popper": "1.2.8",
				"@radix-ui/react-portal": "1.1.9",
				"@radix-ui/react-presence": "1.1.5",
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-slot": "1.2.3",
				"@radix-ui/react-use-controllable-state": "1.2.2",
				"aria-hidden": "^1.2.4",
				"react-remove-scroll": "^2.6.3"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@radix-ui/react-popper": {
			"version": "1.2.8",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-popper/-/react-popper-1.2.8.tgz",
			"integrity": "sha512-0NJQ4LFFUuWkE7Oxf0htBKS6zLkkjBH+hM1uk7Ng705ReR8m/uelduy1DBo0PyBXPKVnBA6YBlU94MBGXrSBCw==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@floating-ui/react-dom": "^2.0.0",
				"@radix-ui/react-arrow": "1.1.7",
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-context": "1.1.2",
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-use-callback-ref": "1.1.1",
				"@radix-ui/react-use-layout-effect": "1.1.1",
				"@radix-ui/react-use-rect": "1.1.1",
				"@radix-ui/react-use-size": "1.1.1",
				"@radix-ui/rect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@radix-ui/react-portal": {
			"version": "1.1.9",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-portal/-/react-portal-1.1.9.tgz",
			"integrity": "sha512-bpIxvq03if6UNwXZ+HTK71JLh4APvnXntDc6XOX8UVq4XQOVl7lwok0AvIl+b8zgCw3fSaVTZMpAPPagXbKmHQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-use-layout-effect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@radix-ui/react-presence": {
			"version": "1.1.5",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-presence/-/react-presence-1.1.5.tgz",
			"integrity": "sha512-/jfEwNDdQVBCNvjkGit4h6pMOzq8bHkopq458dPt2lMjx+eBQUohZNG9A7DtO/O5ukSbxuaNGXMjHicgwy6rQQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-use-layout-effect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/scraping/node_modules/@radix-ui/react-primitive": {
			"version": "2.1.3",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-primitive/-/react-primitive-2.1.3.tgz",
			"integrity": "sha512-m9gTwRkhy2lvCPe6QJp4d3G1TYEUHn/FzJUtq9MjH46an1wJU+GdoGC5VLof8RX8Ft/DlpshApkhswDLZzHIcQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-slot": "1.2.3"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/scraping/node_modules/fs-extra": {
			"version": "11.1.1",
			"resolved": "https://registry.npmjs.org/fs-extra/-/fs-extra-11.1.1.tgz",
			"integrity": "sha512-MGIE4HOvQCeUCzmlHs0vXpih4ysz4wg9qiSAu6cd42lVwPbTM1TjV7RusoyQqMmk/95gdQZX72u+YW+c3eEpFQ==",
			"license": "MIT",
			"dependencies": {
				"graceful-fs": "^4.2.0",
				"jsonfile": "^6.0.1",
				"universalify": "^2.0.0"
			},
			"engines": {
				"node": ">=14.14"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/mdast-util-mdx-jsx": {
			"version": "3.1.3",
			"resolved": "https://registry.npmjs.org/mdast-util-mdx-jsx/-/mdast-util-mdx-jsx-3.1.3.tgz",
			"integrity": "sha512-bfOjvNt+1AcbPLTFMFWY149nJz0OjmewJs3LQQ5pIyVGxP4CdOqNVJL6kTaM5c68p8q82Xv3nCyFfUnuEcH3UQ==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"@types/hast": "^3.0.0",
				"@types/mdast": "^4.0.0",
				"@types/unist": "^3.0.0",
				"ccount": "^2.0.0",
				"devlop": "^1.1.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0",
				"parse-entities": "^4.0.0",
				"stringify-entities": "^4.0.0",
				"unist-util-stringify-position": "^4.0.0",
				"vfile-message": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/next-mdx-remote-client": {
			"version": "1.1.4",
			"resolved": "https://registry.npmjs.org/next-mdx-remote-client/-/next-mdx-remote-client-1.1.4.tgz",
			"integrity": "sha512-psCMdO50tfoT1kAH7OGXZvhyRfiHVK6IqwjmWFV5gtLo4dnqjAgcjcLNeJ92iI26UNlKShxYrBs1GQ6UXxk97A==",
			"license": "MPL 2.0",
			"dependencies": {
				"@babel/code-frame": "^7.27.1",
				"@mdx-js/mdx": "^3.1.1",
				"@mdx-js/react": "^3.1.1",
				"remark-mdx-remove-esm": "^1.2.1",
				"serialize-error": "^12.0.0",
				"vfile": "^6.0.3",
				"vfile-matter": "^5.0.1"
			},
			"engines": {
				"node": ">=18.18.0"
			},
			"peerDependencies": {
				"react": ">= 18.3.0 < 19.0.0",
				"react-dom": ">= 18.3.0 < 19.0.0"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/react": {
			"version": "18.3.1",
			"resolved": "https://registry.npmjs.org/react/-/react-18.3.1.tgz",
			"integrity": "sha512-wS+hAgJShR0KhEvPJArfuPVN1+Hz1t0Y6n5jLrGQbkb4urgPE/0Rve+1kMB1v/oWgHgm4WIcV+i7F2pTVj+2iQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"loose-envify": "^1.1.0"
			},
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/react-dom": {
			"version": "18.3.1",
			"resolved": "https://registry.npmjs.org/react-dom/-/react-dom-18.3.1.tgz",
			"integrity": "sha512-5m4nQKp+rZRb09LNH59GM4BxTh9251/ylbKIbpe7TpGxfJ+9kv6BLkLBXIjjspbgbnIBNqlI23tRnTWT0snUIw==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"loose-envify": "^1.1.0",
				"scheduler": "^0.23.2"
			},
			"peerDependencies": {
				"react": "^18.3.1"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/remark-mdx": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/remark-mdx/-/remark-mdx-3.0.1.tgz",
			"integrity": "sha512-3Pz3yPQ5Rht2pM5R+0J2MrGoBSrzf+tJG94N+t/ilfdh8YLyyKYtidAYwTveB20BoHAcwIopOUqhcmh2F7hGYA==",
			"license": "MIT",
			"dependencies": {
				"mdast-util-mdx": "^3.0.0",
				"micromark-extension-mdxjs": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/scraping/node_modules/scheduler": {
			"version": "0.23.2",
			"resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.23.2.tgz",
			"integrity": "sha512-UOShsPwz7NrMUqhR6t0hWjFduvOzbtv7toDH1/hIrfRNIDBnnBWd0CwJTGvTpngVlmwGCdP9/Zl/tVrDqcuYzQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"loose-envify": "^1.1.0"
			}
		},
		"node_modules/@mintlify/validation": {
			"version": "0.1.589",
			"resolved": "https://registry.npmjs.org/@mintlify/validation/-/validation-0.1.589.tgz",
			"integrity": "sha512-wfhkqQqHjn0OWSo182/Pjspz+SLXJOgVu0tiDwfz6cx/QZRbCJko1XQQjJkRx0VbrTe3ABza8lQ9SoGx+M78QQ==",
			"license": "Elastic-2.0",
			"dependencies": {
				"@mintlify/mdx": "^3.0.4",
				"@mintlify/models": "0.0.270",
				"arktype": "2.1.27",
				"js-yaml": "4.1.0",
				"lcm": "0.0.3",
				"lodash": "4.17.21",
				"object-hash": "3.0.0",
				"openapi-types": "12.1.3",
				"uuid": "11.1.0",
				"zod": "3.24.0",
				"zod-to-json-schema": "3.20.4"
			}
		},
		"node_modules/@mintlify/validation/node_modules/@floating-ui/react-dom": {
			"version": "2.1.7",
			"resolved": "https://registry.npmjs.org/@floating-ui/react-dom/-/react-dom-2.1.7.tgz",
			"integrity": "sha512-0tLRojf/1Go2JgEVm+3Frg9A3IW8bJgKgdO0BN5RkF//ufuz2joZM63Npau2ff3J6lUVYgDSNzNkR+aH3IVfjg==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@floating-ui/dom": "^1.7.5"
			},
			"peerDependencies": {
				"react": ">=16.8.0",
				"react-dom": ">=16.8.0"
			}
		},
		"node_modules/@mintlify/validation/node_modules/@mintlify/mdx": {
			"version": "3.0.4",
			"resolved": "https://registry.npmjs.org/@mintlify/mdx/-/mdx-3.0.4.tgz",
			"integrity": "sha512-tJhdpnM5ReJLNJ2fuDRIEr0zgVd6id7/oAIfs26V46QlygiLsc8qx4Rz3LWIX51rUXW/cfakjj0EATxIciIw+g==",
			"license": "MIT",
			"dependencies": {
				"@shikijs/transformers": "^3.11.0",
				"@shikijs/twoslash": "^3.12.2",
				"arktype": "^2.1.26",
				"hast-util-to-string": "^3.0.1",
				"mdast-util-from-markdown": "^2.0.2",
				"mdast-util-gfm": "^3.1.0",
				"mdast-util-mdx-jsx": "^3.2.0",
				"mdast-util-to-hast": "^13.2.0",
				"next-mdx-remote-client": "^1.0.3",
				"rehype-katex": "^7.0.1",
				"remark-gfm": "^4.0.0",
				"remark-math": "^6.0.0",
				"remark-smartypants": "^3.0.2",
				"shiki": "^3.11.0",
				"unified": "^11.0.0",
				"unist-util-visit": "^5.0.0"
			},
			"peerDependencies": {
				"@radix-ui/react-popover": "^1.1.15",
				"react": "^18.3.1",
				"react-dom": "^18.3.1"
			}
		},
		"node_modules/@mintlify/validation/node_modules/@radix-ui/react-arrow": {
			"version": "1.1.7",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-arrow/-/react-arrow-1.1.7.tgz",
			"integrity": "sha512-F+M1tLhO+mlQaOWspE8Wstg+z6PwxwRd8oQ8IXceWz92kfAmalTRf0EjrouQeo7QssEPfCn05B4Ihs1K9WQ/7w==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-primitive": "2.1.3"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/validation/node_modules/@radix-ui/react-dismissable-layer": {
			"version": "1.1.11",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-dismissable-layer/-/react-dismissable-layer-1.1.11.tgz",
			"integrity": "sha512-Nqcp+t5cTB8BinFkZgXiMJniQH0PsUt2k51FUhbdfeKvc4ACcG2uQniY/8+h1Yv6Kza4Q7lD7PQV0z0oicE0Mg==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/primitive": "1.1.3",
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-use-callback-ref": "1.1.1",
				"@radix-ui/react-use-escape-keydown": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/validation/node_modules/@radix-ui/react-focus-scope": {
			"version": "1.1.7",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-focus-scope/-/react-focus-scope-1.1.7.tgz",
			"integrity": "sha512-t2ODlkXBQyn7jkl6TNaw/MtVEVvIGelJDCG41Okq/KwUsJBwQ4XVZsHAVUkK4mBv3ewiAS3PGuUWuY2BoK4ZUw==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-use-callback-ref": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/validation/node_modules/@radix-ui/react-popover": {
			"version": "1.1.15",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-popover/-/react-popover-1.1.15.tgz",
			"integrity": "sha512-kr0X2+6Yy/vJzLYJUPCZEc8SfQcf+1COFoAqauJm74umQhta9M7lNJHP7QQS3vkvcGLQUbWpMzwrXYwrYztHKA==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/primitive": "1.1.3",
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-context": "1.1.2",
				"@radix-ui/react-dismissable-layer": "1.1.11",
				"@radix-ui/react-focus-guards": "1.1.3",
				"@radix-ui/react-focus-scope": "1.1.7",
				"@radix-ui/react-id": "1.1.1",
				"@radix-ui/react-popper": "1.2.8",
				"@radix-ui/react-portal": "1.1.9",
				"@radix-ui/react-presence": "1.1.5",
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-slot": "1.2.3",
				"@radix-ui/react-use-controllable-state": "1.2.2",
				"aria-hidden": "^1.2.4",
				"react-remove-scroll": "^2.6.3"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/validation/node_modules/@radix-ui/react-popper": {
			"version": "1.2.8",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-popper/-/react-popper-1.2.8.tgz",
			"integrity": "sha512-0NJQ4LFFUuWkE7Oxf0htBKS6zLkkjBH+hM1uk7Ng705ReR8m/uelduy1DBo0PyBXPKVnBA6YBlU94MBGXrSBCw==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@floating-ui/react-dom": "^2.0.0",
				"@radix-ui/react-arrow": "1.1.7",
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-context": "1.1.2",
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-use-callback-ref": "1.1.1",
				"@radix-ui/react-use-layout-effect": "1.1.1",
				"@radix-ui/react-use-rect": "1.1.1",
				"@radix-ui/react-use-size": "1.1.1",
				"@radix-ui/rect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/validation/node_modules/@radix-ui/react-portal": {
			"version": "1.1.9",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-portal/-/react-portal-1.1.9.tgz",
			"integrity": "sha512-bpIxvq03if6UNwXZ+HTK71JLh4APvnXntDc6XOX8UVq4XQOVl7lwok0AvIl+b8zgCw3fSaVTZMpAPPagXbKmHQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-primitive": "2.1.3",
				"@radix-ui/react-use-layout-effect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/validation/node_modules/@radix-ui/react-presence": {
			"version": "1.1.5",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-presence/-/react-presence-1.1.5.tgz",
			"integrity": "sha512-/jfEwNDdQVBCNvjkGit4h6pMOzq8bHkopq458dPt2lMjx+eBQUohZNG9A7DtO/O5ukSbxuaNGXMjHicgwy6rQQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-compose-refs": "1.1.2",
				"@radix-ui/react-use-layout-effect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/validation/node_modules/@radix-ui/react-primitive": {
			"version": "2.1.3",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-primitive/-/react-primitive-2.1.3.tgz",
			"integrity": "sha512-m9gTwRkhy2lvCPe6QJp4d3G1TYEUHn/FzJUtq9MjH46an1wJU+GdoGC5VLof8RX8Ft/DlpshApkhswDLZzHIcQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-slot": "1.2.3"
			},
			"peerDependencies": {
				"@types/react": "*",
				"@types/react-dom": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc",
				"react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"@types/react-dom": {
					"optional": true
				}
			}
		},
		"node_modules/@mintlify/validation/node_modules/mdast-util-gfm": {
			"version": "3.1.0",
			"resolved": "https://registry.npmjs.org/mdast-util-gfm/-/mdast-util-gfm-3.1.0.tgz",
			"integrity": "sha512-0ulfdQOM3ysHhCJ1p06l0b0VKlhU0wuQs3thxZQagjcjPrlFRqY215uZGHHJan9GEAXd9MbfPjFJz+qMkVR6zQ==",
			"license": "MIT",
			"dependencies": {
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-gfm-autolink-literal": "^2.0.0",
				"mdast-util-gfm-footnote": "^2.0.0",
				"mdast-util-gfm-strikethrough": "^2.0.0",
				"mdast-util-gfm-table": "^2.0.0",
				"mdast-util-gfm-task-list-item": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@mintlify/validation/node_modules/next-mdx-remote-client": {
			"version": "1.1.4",
			"resolved": "https://registry.npmjs.org/next-mdx-remote-client/-/next-mdx-remote-client-1.1.4.tgz",
			"integrity": "sha512-psCMdO50tfoT1kAH7OGXZvhyRfiHVK6IqwjmWFV5gtLo4dnqjAgcjcLNeJ92iI26UNlKShxYrBs1GQ6UXxk97A==",
			"license": "MPL 2.0",
			"dependencies": {
				"@babel/code-frame": "^7.27.1",
				"@mdx-js/mdx": "^3.1.1",
				"@mdx-js/react": "^3.1.1",
				"remark-mdx-remove-esm": "^1.2.1",
				"serialize-error": "^12.0.0",
				"vfile": "^6.0.3",
				"vfile-matter": "^5.0.1"
			},
			"engines": {
				"node": ">=18.18.0"
			},
			"peerDependencies": {
				"react": ">= 18.3.0 < 19.0.0",
				"react-dom": ">= 18.3.0 < 19.0.0"
			}
		},
		"node_modules/@mintlify/validation/node_modules/react": {
			"version": "18.3.1",
			"resolved": "https://registry.npmjs.org/react/-/react-18.3.1.tgz",
			"integrity": "sha512-wS+hAgJShR0KhEvPJArfuPVN1+Hz1t0Y6n5jLrGQbkb4urgPE/0Rve+1kMB1v/oWgHgm4WIcV+i7F2pTVj+2iQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"loose-envify": "^1.1.0"
			},
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/@mintlify/validation/node_modules/react-dom": {
			"version": "18.3.1",
			"resolved": "https://registry.npmjs.org/react-dom/-/react-dom-18.3.1.tgz",
			"integrity": "sha512-5m4nQKp+rZRb09LNH59GM4BxTh9251/ylbKIbpe7TpGxfJ+9kv6BLkLBXIjjspbgbnIBNqlI23tRnTWT0snUIw==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"loose-envify": "^1.1.0",
				"scheduler": "^0.23.2"
			},
			"peerDependencies": {
				"react": "^18.3.1"
			}
		},
		"node_modules/@mintlify/validation/node_modules/scheduler": {
			"version": "0.23.2",
			"resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.23.2.tgz",
			"integrity": "sha512-UOShsPwz7NrMUqhR6t0hWjFduvOzbtv7toDH1/hIrfRNIDBnnBWd0CwJTGvTpngVlmwGCdP9/Zl/tVrDqcuYzQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"loose-envify": "^1.1.0"
			}
		},
		"node_modules/@mintlify/validation/node_modules/zod": {
			"version": "3.24.0",
			"resolved": "https://registry.npmjs.org/zod/-/zod-3.24.0.tgz",
			"integrity": "sha512-Hz+wiY8yD0VLA2k/+nsg2Abez674dDGTai33SwNvMPuf9uIrBC9eFgIMQxBBbHFxVXi8W+5nX9DcAh9YNSQm/w==",
			"license": "MIT",
			"funding": {
				"url": "https://github.com/sponsors/colinhacks"
			}
		},
		"node_modules/@nodelib/fs.scandir": {
			"version": "2.1.5",
			"resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
			"integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
			"license": "MIT",
			"dependencies": {
				"@nodelib/fs.stat": "2.0.5",
				"run-parallel": "^1.1.9"
			},
			"engines": {
				"node": ">= 8"
			}
		},
		"node_modules/@nodelib/fs.stat": {
			"version": "2.0.5",
			"resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
			"integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==",
			"license": "MIT",
			"engines": {
				"node": ">= 8"
			}
		},
		"node_modules/@nodelib/fs.walk": {
			"version": "1.2.8",
			"resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
			"integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
			"license": "MIT",
			"dependencies": {
				"@nodelib/fs.scandir": "2.1.5",
				"fastq": "^1.6.0"
			},
			"engines": {
				"node": ">= 8"
			}
		},
		"node_modules/@openapi-contrib/openapi-schema-to-json-schema": {
			"version": "3.2.0",
			"resolved": "https://registry.npmjs.org/@openapi-contrib/openapi-schema-to-json-schema/-/openapi-schema-to-json-schema-3.2.0.tgz",
			"integrity": "sha512-Gj6C0JwCr8arj0sYuslWXUBSP/KnUlEGnPW4qxlXvAl543oaNQgMgIgkQUA6vs5BCCvwTEiL8m/wdWzfl4UvSw==",
			"license": "MIT",
			"dependencies": {
				"fast-deep-equal": "^3.1.3"
			}
		},
		"node_modules/@puppeteer/browsers": {
			"version": "2.3.0",
			"resolved": "https://registry.npmjs.org/@puppeteer/browsers/-/browsers-2.3.0.tgz",
			"integrity": "sha512-ioXoq9gPxkss4MYhD+SFaU9p1IHFUX0ILAWFPyjGaBdjLsYAlZw6j1iLA0N/m12uVHLFDfSYNF7EQccjinIMDA==",
			"license": "Apache-2.0",
			"dependencies": {
				"debug": "^4.3.5",
				"extract-zip": "^2.0.1",
				"progress": "^2.0.3",
				"proxy-agent": "^6.4.0",
				"semver": "^7.6.3",
				"tar-fs": "^3.0.6",
				"unbzip2-stream": "^1.4.3",
				"yargs": "^17.7.2"
			},
			"bin": {
				"browsers": "lib/cjs/main-cli.js"
			},
			"engines": {
				"node": ">=18"
			}
		},
		"node_modules/@puppeteer/browsers/node_modules/ansi-regex": {
			"version": "5.0.1",
			"resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
			"integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
			"license": "MIT",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/@puppeteer/browsers/node_modules/emoji-regex": {
			"version": "8.0.0",
			"resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
			"integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
			"license": "MIT"
		},
		"node_modules/@puppeteer/browsers/node_modules/is-fullwidth-code-point": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz",
			"integrity": "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==",
			"license": "MIT",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/@puppeteer/browsers/node_modules/string-width": {
			"version": "4.2.3",
			"resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
			"integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
			"license": "MIT",
			"dependencies": {
				"emoji-regex": "^8.0.0",
				"is-fullwidth-code-point": "^3.0.0",
				"strip-ansi": "^6.0.1"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/@puppeteer/browsers/node_modules/strip-ansi": {
			"version": "6.0.1",
			"resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
			"integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
			"license": "MIT",
			"dependencies": {
				"ansi-regex": "^5.0.1"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/@puppeteer/browsers/node_modules/yargs": {
			"version": "17.7.2",
			"resolved": "https://registry.npmjs.org/yargs/-/yargs-17.7.2.tgz",
			"integrity": "sha512-7dSzzRQ++CKnNI/krKnYRV7JKKPUXMEh61soaHKg9mrWEhzFWhFnxPxGl+69cD1Ou63C13NUPCnmIcrvqCuM6w==",
			"license": "MIT",
			"dependencies": {
				"cliui": "^8.0.1",
				"escalade": "^3.1.1",
				"get-caller-file": "^2.0.5",
				"require-directory": "^2.1.1",
				"string-width": "^4.2.3",
				"y18n": "^5.0.5",
				"yargs-parser": "^21.1.1"
			},
			"engines": {
				"node": ">=12"
			}
		},
		"node_modules/@radix-ui/primitive": {
			"version": "1.1.3",
			"resolved": "https://registry.npmjs.org/@radix-ui/primitive/-/primitive-1.1.3.tgz",
			"integrity": "sha512-JTF99U/6XIjCBo0wqkU5sK10glYe27MRRsfwoiq5zzOEZLHU3A3KCMa5X/azekYRCJ0HlwI0crAXS/5dEHTzDg==",
			"license": "MIT",
			"peer": true
		},
		"node_modules/@radix-ui/react-compose-refs": {
			"version": "1.1.2",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-compose-refs/-/react-compose-refs-1.1.2.tgz",
			"integrity": "sha512-z4eqJvfiNnFMHIIvXP3CY57y2WJs5g2v3X0zm9mEJkrkNv4rDxu+sg9Jh8EkXyeqBkB7SOcboo9dMVqhyrACIg==",
			"license": "MIT",
			"peer": true,
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/@radix-ui/react-context": {
			"version": "1.1.2",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-context/-/react-context-1.1.2.tgz",
			"integrity": "sha512-jCi/QKUM2r1Ju5a3J64TH2A5SpKAgh0LpknyqdQ4m6DCV0xJ2HG1xARRwNGPQfi1SLdLWZ1OJz6F4OMBBNiGJA==",
			"license": "MIT",
			"peer": true,
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/@radix-ui/react-focus-guards": {
			"version": "1.1.3",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-focus-guards/-/react-focus-guards-1.1.3.tgz",
			"integrity": "sha512-0rFg/Rj2Q62NCm62jZw0QX7a3sz6QCQU0LpZdNrJX8byRGaGVTqbrW9jAoIAHyMQqsNpeZ81YgSizOt5WXq0Pw==",
			"license": "MIT",
			"peer": true,
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/@radix-ui/react-id": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-id/-/react-id-1.1.1.tgz",
			"integrity": "sha512-kGkGegYIdQsOb4XjsfM97rXsiHaBwco+hFI66oO4s9LU+PLAC5oJ7khdOVFxkhsmlbpUqDAvXw11CluXP+jkHg==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-use-layout-effect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/@radix-ui/react-slot": {
			"version": "1.2.3",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-slot/-/react-slot-1.2.3.tgz",
			"integrity": "sha512-aeNmHnBxbi2St0au6VBVC7JXFlhLlOnvIIlePNniyUNAClzmtAUEY8/pBiK3iHjufOlwA+c20/8jngo7xcrg8A==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-compose-refs": "1.1.2"
			},
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/@radix-ui/react-use-callback-ref": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-use-callback-ref/-/react-use-callback-ref-1.1.1.tgz",
			"integrity": "sha512-FkBMwD+qbGQeMu1cOHnuGB6x4yzPjho8ap5WtbEJ26umhgqVXbhekKUQO+hZEL1vU92a3wHwdp0HAcqAUF5iDg==",
			"license": "MIT",
			"peer": true,
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/@radix-ui/react-use-controllable-state": {
			"version": "1.2.2",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-use-controllable-state/-/react-use-controllable-state-1.2.2.tgz",
			"integrity": "sha512-BjasUjixPFdS+NKkypcyyN5Pmg83Olst0+c6vGov0diwTEo6mgdqVR6hxcEgFuh4QrAs7Rc+9KuGJ9TVCj0Zzg==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-use-effect-event": "0.0.2",
				"@radix-ui/react-use-layout-effect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/@radix-ui/react-use-effect-event": {
			"version": "0.0.2",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-use-effect-event/-/react-use-effect-event-0.0.2.tgz",
			"integrity": "sha512-Qp8WbZOBe+blgpuUT+lw2xheLP8q0oatc9UpmiemEICxGvFLYmHm9QowVZGHtJlGbS6A6yJ3iViad/2cVjnOiA==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-use-layout-effect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/@radix-ui/react-use-escape-keydown": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-use-escape-keydown/-/react-use-escape-keydown-1.1.1.tgz",
			"integrity": "sha512-Il0+boE7w/XebUHyBjroE+DbByORGR9KKmITzbR7MyQ4akpORYP/ZmbhAr0DG7RmmBqoOnZdy2QlvajJ2QA59g==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-use-callback-ref": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/@radix-ui/react-use-layout-effect": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-use-layout-effect/-/react-use-layout-effect-1.1.1.tgz",
			"integrity": "sha512-RbJRS4UWQFkzHTTwVymMTUv8EqYhOp8dOOviLj2ugtTiXRaRQS7GLGxZTLL1jWhMeoSCf5zmcZkqTl9IiYfXcQ==",
			"license": "MIT",
			"peer": true,
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/@radix-ui/react-use-rect": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-use-rect/-/react-use-rect-1.1.1.tgz",
			"integrity": "sha512-QTYuDesS0VtuHNNvMh+CjlKJ4LJickCMUAqjlE3+j8w+RlRpwyX3apEQKGFzbZGdo7XNG1tXa+bQqIE7HIXT2w==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/rect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/@radix-ui/react-use-size": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/@radix-ui/react-use-size/-/react-use-size-1.1.1.tgz",
			"integrity": "sha512-ewrXRDTAqAXlkl6t/fkXWNAhFX9I+CkKlw6zjEwk86RSPKwZr3xpBRso655aqYafwtnbpHLj6toFzmd6xdVptQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"@radix-ui/react-use-layout-effect": "1.1.1"
			},
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/@radix-ui/rect": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/@radix-ui/rect/-/rect-1.1.1.tgz",
			"integrity": "sha512-HPwpGIzkl28mWyZqG52jiqDJ12waP11Pa1lGoiyUkIEuMLBP0oeK/C89esbXrxsky5we7dfd8U58nm0SgAWpVw==",
			"license": "MIT",
			"peer": true
		},
		"node_modules/@shikijs/core": {
			"version": "3.22.0",
			"resolved": "https://registry.npmjs.org/@shikijs/core/-/core-3.22.0.tgz",
			"integrity": "sha512-iAlTtSDDbJiRpvgL5ugKEATDtHdUVkqgHDm/gbD2ZS9c88mx7G1zSYjjOxp5Qa0eaW0MAQosFRmJSk354PRoQA==",
			"license": "MIT",
			"dependencies": {
				"@shikijs/types": "3.22.0",
				"@shikijs/vscode-textmate": "^10.0.2",
				"@types/hast": "^3.0.4",
				"hast-util-to-html": "^9.0.5"
			}
		},
		"node_modules/@shikijs/core/node_modules/hast-util-to-html": {
			"version": "9.0.5",
			"resolved": "https://registry.npmjs.org/hast-util-to-html/-/hast-util-to-html-9.0.5.tgz",
			"integrity": "sha512-OguPdidb+fbHQSU4Q4ZiLKnzWo8Wwsf5bZfbvu7//a9oTYoqD/fWpe96NuHkoS9h0ccGOTe0C4NGXdtS0iObOw==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"@types/unist": "^3.0.0",
				"ccount": "^2.0.0",
				"comma-separated-tokens": "^2.0.0",
				"hast-util-whitespace": "^3.0.0",
				"html-void-elements": "^3.0.0",
				"mdast-util-to-hast": "^13.0.0",
				"property-information": "^7.0.0",
				"space-separated-tokens": "^2.0.0",
				"stringify-entities": "^4.0.0",
				"zwitch": "^2.0.4"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/@shikijs/engine-javascript": {
			"version": "3.22.0",
			"resolved": "https://registry.npmjs.org/@shikijs/engine-javascript/-/engine-javascript-3.22.0.tgz",
			"integrity": "sha512-jdKhfgW9CRtj3Tor0L7+yPwdG3CgP7W+ZEqSsojrMzCjD1e0IxIbwUMDDpYlVBlC08TACg4puwFGkZfLS+56Tw==",
			"license": "MIT",
			"dependencies": {
				"@shikijs/types": "3.22.0",
				"@shikijs/vscode-textmate": "^10.0.2",
				"oniguruma-to-es": "^4.3.4"
			}
		},
		"node_modules/@shikijs/engine-oniguruma": {
			"version": "3.22.0",
			"resolved": "https://registry.npmjs.org/@shikijs/engine-oniguruma/-/engine-oniguruma-3.22.0.tgz",
			"integrity": "sha512-DyXsOG0vGtNtl7ygvabHd7Mt5EY8gCNqR9Y7Lpbbd/PbJvgWrqaKzH1JW6H6qFkuUa8aCxoiYVv8/YfFljiQxA==",
			"license": "MIT",
			"dependencies": {
				"@shikijs/types": "3.22.0",
				"@shikijs/vscode-textmate": "^10.0.2"
			}
		},
		"node_modules/@shikijs/langs": {
			"version": "3.22.0",
			"resolved": "https://registry.npmjs.org/@shikijs/langs/-/langs-3.22.0.tgz",
			"integrity": "sha512-x/42TfhWmp6H00T6uwVrdTJGKgNdFbrEdhaDwSR5fd5zhQ1Q46bHq9EO61SCEWJR0HY7z2HNDMaBZp8JRmKiIA==",
			"license": "MIT",
			"dependencies": {
				"@shikijs/types": "3.22.0"
			}
		},
		"node_modules/@shikijs/themes": {
			"version": "3.22.0",
			"resolved": "https://registry.npmjs.org/@shikijs/themes/-/themes-3.22.0.tgz",
			"integrity": "sha512-o+tlOKqsr6FE4+mYJG08tfCFDS+3CG20HbldXeVoyP+cYSUxDhrFf3GPjE60U55iOkkjbpY2uC3It/eeja35/g==",
			"license": "MIT",
			"dependencies": {
				"@shikijs/types": "3.22.0"
			}
		},
		"node_modules/@shikijs/transformers": {
			"version": "3.22.0",
			"resolved": "https://registry.npmjs.org/@shikijs/transformers/-/transformers-3.22.0.tgz",
			"integrity": "sha512-E7eRV7mwDBjueLF6852n2oYeJYxBq3NSsDk+uyruYAXONv4U8holGmIrT+mPRJQ1J1SNOH6L8G19KRzmBawrFw==",
			"license": "MIT",
			"dependencies": {
				"@shikijs/core": "3.22.0",
				"@shikijs/types": "3.22.0"
			}
		},
		"node_modules/@shikijs/twoslash": {
			"version": "3.22.0",
			"resolved": "https://registry.npmjs.org/@shikijs/twoslash/-/twoslash-3.22.0.tgz",
			"integrity": "sha512-GO27UPN+kegOMQvC+4XcLt0Mttyg+n16XKjmoKjdaNZoW+sOJV7FLdv2QKauqUDws6nE3EQPD+TFHEdyyoUBDw==",
			"license": "MIT",
			"dependencies": {
				"@shikijs/core": "3.22.0",
				"@shikijs/types": "3.22.0",
				"twoslash": "^0.3.6"
			},
			"peerDependencies": {
				"typescript": ">=5.5.0"
			}
		},
		"node_modules/@shikijs/types": {
			"version": "3.22.0",
			"resolved": "https://registry.npmjs.org/@shikijs/types/-/types-3.22.0.tgz",
			"integrity": "sha512-491iAekgKDBFE67z70Ok5a8KBMsQ2IJwOWw3us/7ffQkIBCyOQfm/aNwVMBUriP02QshIfgHCBSIYAl3u2eWjg==",
			"license": "MIT",
			"dependencies": {
				"@shikijs/vscode-textmate": "^10.0.2",
				"@types/hast": "^3.0.4"
			}
		},
		"node_modules/@shikijs/vscode-textmate": {
			"version": "10.0.2",
			"resolved": "https://registry.npmjs.org/@shikijs/vscode-textmate/-/vscode-textmate-10.0.2.tgz",
			"integrity": "sha512-83yeghZ2xxin3Nj8z1NMd/NCuca+gsYXswywDy5bHvwlWL8tpTQmzGeUuHd9FC3E/SBEMvzJRwWEOz5gGes9Qg==",
			"license": "MIT"
		},
		"node_modules/@sindresorhus/is": {
			"version": "5.6.0",
			"resolved": "https://registry.npmjs.org/@sindresorhus/is/-/is-5.6.0.tgz",
			"integrity": "sha512-TV7t8GKYaJWsn00tFDqBw8+Uqmr8A0fRU1tvTQhyZzGv0sJCGRQL3JGMI3ucuKo3XIZdUP+Lx7/gh2t3lewy7g==",
			"license": "MIT",
			"engines": {
				"node": ">=14.16"
			},
			"funding": {
				"url": "https://github.com/sindresorhus/is?sponsor=1"
			}
		},
		"node_modules/@sindresorhus/slugify": {
			"version": "2.2.0",
			"resolved": "https://registry.npmjs.org/@sindresorhus/slugify/-/slugify-2.2.0.tgz",
			"integrity": "sha512-9Vybc/qX8Kj6pxJaapjkFbiUJPk7MAkCh/GFCxIBnnsuYCFPIXKvnLidG8xlepht3i24L5XemUmGtrJ3UWrl6w==",
			"license": "MIT",
			"dependencies": {
				"@sindresorhus/transliterate": "^1.0.0",
				"escape-string-regexp": "^5.0.0"
			},
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/@sindresorhus/transliterate": {
			"version": "1.6.0",
			"resolved": "https://registry.npmjs.org/@sindresorhus/transliterate/-/transliterate-1.6.0.tgz",
			"integrity": "sha512-doH1gimEu3A46VX6aVxpHTeHrytJAG6HgdxntYnCFiIFHEM/ZGpG8KiZGBChchjQmG0XFIBL552kBTjVcMZXwQ==",
			"license": "MIT",
			"dependencies": {
				"escape-string-regexp": "^5.0.0"
			},
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/@socket.io/component-emitter": {
			"version": "3.1.2",
			"resolved": "https://registry.npmjs.org/@socket.io/component-emitter/-/component-emitter-3.1.2.tgz",
			"integrity": "sha512-9BCxFwvbGg/RsZK9tjXd8s4UcwR0MWeFQ1XEKIQVVvAGJyINdrqKMcTRyLoK8Rse1GjzLV9cwjWV1olXRWEXVA==",
			"license": "MIT"
		},
		"node_modules/@stoplight/better-ajv-errors": {
			"version": "1.0.3",
			"resolved": "https://registry.npmjs.org/@stoplight/better-ajv-errors/-/better-ajv-errors-1.0.3.tgz",
			"integrity": "sha512-0p9uXkuB22qGdNfy3VeEhxkU5uwvp/KrBTAbrLBURv6ilxIVwanKwjMc41lQfIVgPGcOkmLbTolfFrSsueu7zA==",
			"license": "Apache-2.0",
			"dependencies": {
				"jsonpointer": "^5.0.0",
				"leven": "^3.1.0"
			},
			"engines": {
				"node": "^12.20 || >= 14.13"
			},
			"peerDependencies": {
				"ajv": ">=8"
			}
		},
		"node_modules/@stoplight/better-ajv-errors/node_modules/leven": {
			"version": "3.1.0",
			"resolved": "https://registry.npmjs.org/leven/-/leven-3.1.0.tgz",
			"integrity": "sha512-qsda+H8jTaUaN/x5vzW2rzc+8Rw4TAQ/4KjB46IwK5VH+IlVeeeje/EoZRpiXvIqjFgK84QffqPztGI3VBLG1A==",
			"license": "MIT",
			"engines": {
				"node": ">=6"
			}
		},
		"node_modules/@stoplight/json": {
			"version": "3.21.0",
			"resolved": "https://registry.npmjs.org/@stoplight/json/-/json-3.21.0.tgz",
			"integrity": "sha512-5O0apqJ/t4sIevXCO3SBN9AHCEKKR/Zb4gaj7wYe5863jme9g02Q0n/GhM7ZCALkL+vGPTe4ZzTETP8TFtsw3g==",
			"license": "Apache-2.0",
			"dependencies": {
				"@stoplight/ordered-object-literal": "^1.0.3",
				"@stoplight/path": "^1.3.2",
				"@stoplight/types": "^13.6.0",
				"jsonc-parser": "~2.2.1",
				"lodash": "^4.17.21",
				"safe-stable-stringify": "^1.1"
			},
			"engines": {
				"node": ">=8.3.0"
			}
		},
		"node_modules/@stoplight/json-ref-readers": {
			"version": "1.2.2",
			"resolved": "https://registry.npmjs.org/@stoplight/json-ref-readers/-/json-ref-readers-1.2.2.tgz",
			"integrity": "sha512-nty0tHUq2f1IKuFYsLM4CXLZGHdMn+X/IwEUIpeSOXt0QjMUbL0Em57iJUDzz+2MkWG83smIigNZ3fauGjqgdQ==",
			"license": "Apache-2.0",
			"dependencies": {
				"node-fetch": "^2.6.0",
				"tslib": "^1.14.1"
			},
			"engines": {
				"node": ">=8.3.0"
			}
		},
		"node_modules/@stoplight/json-ref-resolver": {
			"version": "3.1.6",
			"resolved": "https://registry.npmjs.org/@stoplight/json-ref-resolver/-/json-ref-resolver-3.1.6.tgz",
			"integrity": "sha512-YNcWv3R3n3U6iQYBsFOiWSuRGE5su1tJSiX6pAPRVk7dP0L7lqCteXGzuVRQ0gMZqUl8v1P0+fAKxF6PLo9B5A==",
			"license": "Apache-2.0",
			"dependencies": {
				"@stoplight/json": "^3.21.0",
				"@stoplight/path": "^1.3.2",
				"@stoplight/types": "^12.3.0 || ^13.0.0",
				"@types/urijs": "^1.19.19",
				"dependency-graph": "~0.11.0",
				"fast-memoize": "^2.5.2",
				"immer": "^9.0.6",
				"lodash": "^4.17.21",
				"tslib": "^2.6.0",
				"urijs": "^1.19.11"
			},
			"engines": {
				"node": ">=8.3.0"
			}
		},
		"node_modules/@stoplight/json-ref-resolver/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD"
		},
		"node_modules/@stoplight/ordered-object-literal": {
			"version": "1.0.5",
			"resolved": "https://registry.npmjs.org/@stoplight/ordered-object-literal/-/ordered-object-literal-1.0.5.tgz",
			"integrity": "sha512-COTiuCU5bgMUtbIFBuyyh2/yVVzlr5Om0v5utQDgBCuQUOPgU1DwoffkTfg4UBQOvByi5foF4w4T+H9CoRe5wg==",
			"license": "Apache-2.0",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/@stoplight/path": {
			"version": "1.3.2",
			"resolved": "https://registry.npmjs.org/@stoplight/path/-/path-1.3.2.tgz",
			"integrity": "sha512-lyIc6JUlUA8Ve5ELywPC8I2Sdnh1zc1zmbYgVarhXIp9YeAB0ReeqmGEOWNtlHkbP2DAA1AL65Wfn2ncjK/jtQ==",
			"license": "Apache-2.0",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/@stoplight/spectral-core": {
			"version": "1.21.0",
			"resolved": "https://registry.npmjs.org/@stoplight/spectral-core/-/spectral-core-1.21.0.tgz",
			"integrity": "sha512-oj4e/FrDLUhBRocIW+lRMKlJ/q/rDZw61HkLbTFsdMd+f/FTkli2xHNB1YC6n1mrMKjjvy7XlUuFkC7XxtgbWw==",
			"license": "Apache-2.0",
			"dependencies": {
				"@stoplight/better-ajv-errors": "1.0.3",
				"@stoplight/json": "~3.21.0",
				"@stoplight/path": "1.3.2",
				"@stoplight/spectral-parsers": "^1.0.0",
				"@stoplight/spectral-ref-resolver": "^1.0.4",
				"@stoplight/spectral-runtime": "^1.1.2",
				"@stoplight/types": "~13.6.0",
				"@types/es-aggregate-error": "^1.0.2",
				"@types/json-schema": "^7.0.11",
				"ajv": "^8.17.1",
				"ajv-errors": "~3.0.0",
				"ajv-formats": "~2.1.1",
				"es-aggregate-error": "^1.0.7",
				"jsonpath-plus": "^10.3.0",
				"lodash": "~4.17.23",
				"lodash.topath": "^4.5.2",
				"minimatch": "3.1.2",
				"nimma": "0.2.3",
				"pony-cause": "^1.1.1",
				"simple-eval": "1.0.1",
				"tslib": "^2.8.1"
			},
			"engines": {
				"node": "^16.20 || ^18.18 || >= 20.17"
			}
		},
		"node_modules/@stoplight/spectral-core/node_modules/@stoplight/types": {
			"version": "13.6.0",
			"resolved": "https://registry.npmjs.org/@stoplight/types/-/types-13.6.0.tgz",
			"integrity": "sha512-dzyuzvUjv3m1wmhPfq82lCVYGcXG0xUYgqnWfCq3PCVR4BKFhjdkHrnJ+jIDoMKvXb05AZP/ObQF6+NpDo29IQ==",
			"license": "Apache-2.0",
			"dependencies": {
				"@types/json-schema": "^7.0.4",
				"utility-types": "^3.10.0"
			},
			"engines": {
				"node": "^12.20 || >=14.13"
			}
		},
		"node_modules/@stoplight/spectral-core/node_modules/lodash": {
			"version": "4.17.23",
			"resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.23.tgz",
			"integrity": "sha512-LgVTMpQtIopCi79SJeDiP0TfWi5CNEc/L/aRdTh3yIvmZXTnheWpKjSZhnvMl8iXbC1tFg9gdHHDMLoV7CnG+w==",
			"license": "MIT"
		},
		"node_modules/@stoplight/spectral-core/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD"
		},
		"node_modules/@stoplight/spectral-formats": {
			"version": "1.8.2",
			"resolved": "https://registry.npmjs.org/@stoplight/spectral-formats/-/spectral-formats-1.8.2.tgz",
			"integrity": "sha512-c06HB+rOKfe7tuxg0IdKDEA5XnjL2vrn/m/OVIIxtINtBzphZrOgtRn7epQ5bQF5SWp84Ue7UJWaGgDwVngMFw==",
			"license": "Apache-2.0",
			"dependencies": {
				"@stoplight/json": "^3.17.0",
				"@stoplight/spectral-core": "^1.19.2",
				"@types/json-schema": "^7.0.7",
				"tslib": "^2.8.1"
			},
			"engines": {
				"node": "^16.20 || ^18.18 || >= 20.17"
			}
		},
		"node_modules/@stoplight/spectral-formats/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD"
		},
		"node_modules/@stoplight/spectral-functions": {
			"version": "1.10.1",
			"resolved": "https://registry.npmjs.org/@stoplight/spectral-functions/-/spectral-functions-1.10.1.tgz",
			"integrity": "sha512-obu8ZfoHxELOapfGsCJixKZXZcffjg+lSoNuttpmUFuDzVLT3VmH8QkPXfOGOL5Pz80BR35ClNAToDkdnYIURg==",
			"license": "Apache-2.0",
			"dependencies": {
				"@stoplight/better-ajv-errors": "1.0.3",
				"@stoplight/json": "^3.17.1",
				"@stoplight/spectral-core": "^1.19.4",
				"@stoplight/spectral-formats": "^1.8.1",
				"@stoplight/spectral-runtime": "^1.1.2",
				"ajv": "^8.17.1",
				"ajv-draft-04": "~1.0.0",
				"ajv-errors": "~3.0.0",
				"ajv-formats": "~2.1.1",
				"lodash": "~4.17.21",
				"tslib": "^2.8.1"
			},
			"engines": {
				"node": "^16.20 || ^18.18 || >= 20.17"
			}
		},
		"node_modules/@stoplight/spectral-functions/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD"
		},
		"node_modules/@stoplight/spectral-parsers": {
			"version": "1.0.5",
			"resolved": "https://registry.npmjs.org/@stoplight/spectral-parsers/-/spectral-parsers-1.0.5.tgz",
			"integrity": "sha512-ANDTp2IHWGvsQDAY85/jQi9ZrF4mRrA5bciNHX+PUxPr4DwS6iv4h+FVWJMVwcEYdpyoIdyL+SRmHdJfQEPmwQ==",
			"license": "Apache-2.0",
			"dependencies": {
				"@stoplight/json": "~3.21.0",
				"@stoplight/types": "^14.1.1",
				"@stoplight/yaml": "~4.3.0",
				"tslib": "^2.8.1"
			},
			"engines": {
				"node": "^16.20 || ^18.18 || >= 20.17"
			}
		},
		"node_modules/@stoplight/spectral-parsers/node_modules/@stoplight/types": {
			"version": "14.1.1",
			"resolved": "https://registry.npmjs.org/@stoplight/types/-/types-14.1.1.tgz",
			"integrity": "sha512-/kjtr+0t0tjKr+heVfviO9FrU/uGLc+QNX3fHJc19xsCNYqU7lVhaXxDmEID9BZTjG+/r9pK9xP/xU02XGg65g==",
			"license": "Apache-2.0",
			"dependencies": {
				"@types/json-schema": "^7.0.4",
				"utility-types": "^3.10.0"
			},
			"engines": {
				"node": "^12.20 || >=14.13"
			}
		},
		"node_modules/@stoplight/spectral-parsers/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD"
		},
		"node_modules/@stoplight/spectral-ref-resolver": {
			"version": "1.0.5",
			"resolved": "https://registry.npmjs.org/@stoplight/spectral-ref-resolver/-/spectral-ref-resolver-1.0.5.tgz",
			"integrity": "sha512-gj3TieX5a9zMW29z3mBlAtDOCgN3GEc1VgZnCVlr5irmR4Qi5LuECuFItAq4pTn5Zu+sW5bqutsCH7D4PkpyAA==",
			"license": "Apache-2.0",
			"dependencies": {
				"@stoplight/json-ref-readers": "1.2.2",
				"@stoplight/json-ref-resolver": "~3.1.6",
				"@stoplight/spectral-runtime": "^1.1.2",
				"dependency-graph": "0.11.0",
				"tslib": "^2.8.1"
			},
			"engines": {
				"node": "^16.20 || ^18.18 || >= 20.17"
			}
		},
		"node_modules/@stoplight/spectral-ref-resolver/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD"
		},
		"node_modules/@stoplight/spectral-runtime": {
			"version": "1.1.4",
			"resolved": "https://registry.npmjs.org/@stoplight/spectral-runtime/-/spectral-runtime-1.1.4.tgz",
			"integrity": "sha512-YHbhX3dqW0do6DhiPSgSGQzr6yQLlWybhKwWx0cqxjMwxej3TqLv3BXMfIUYFKKUqIwH4Q2mV8rrMM8qD2N0rQ==",
			"license": "Apache-2.0",
			"dependencies": {
				"@stoplight/json": "^3.20.1",
				"@stoplight/path": "^1.3.2",
				"@stoplight/types": "^13.6.0",
				"abort-controller": "^3.0.0",
				"lodash": "^4.17.21",
				"node-fetch": "^2.7.0",
				"tslib": "^2.8.1"
			},
			"engines": {
				"node": "^16.20 || ^18.18 || >= 20.17"
			}
		},
		"node_modules/@stoplight/spectral-runtime/node_modules/node-fetch": {
			"version": "2.7.0",
			"resolved": "https://registry.npmjs.org/node-fetch/-/node-fetch-2.7.0.tgz",
			"integrity": "sha512-c4FRfUm/dbcWZ7U+1Wq0AwCyFL+3nt2bEw05wfxSz+DWpWsitgmSgYmy2dQdWyKC1694ELPqMs/YzUSNozLt8A==",
			"license": "MIT",
			"dependencies": {
				"whatwg-url": "^5.0.0"
			},
			"engines": {
				"node": "4.x || >=6.0.0"
			},
			"peerDependencies": {
				"encoding": "^0.1.0"
			},
			"peerDependenciesMeta": {
				"encoding": {
					"optional": true
				}
			}
		},
		"node_modules/@stoplight/spectral-runtime/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD"
		},
		"node_modules/@stoplight/types": {
			"version": "13.20.0",
			"resolved": "https://registry.npmjs.org/@stoplight/types/-/types-13.20.0.tgz",
			"integrity": "sha512-2FNTv05If7ib79VPDA/r9eUet76jewXFH2y2K5vuge6SXbRHtWBhcaRmu+6QpF4/WRNoJj5XYRSwLGXDxysBGA==",
			"license": "Apache-2.0",
			"dependencies": {
				"@types/json-schema": "^7.0.4",
				"utility-types": "^3.10.0"
			},
			"engines": {
				"node": "^12.20 || >=14.13"
			}
		},
		"node_modules/@stoplight/yaml": {
			"version": "4.3.0",
			"resolved": "https://registry.npmjs.org/@stoplight/yaml/-/yaml-4.3.0.tgz",
			"integrity": "sha512-JZlVFE6/dYpP9tQmV0/ADfn32L9uFarHWxfcRhReKUnljz1ZiUM5zpX+PH8h5CJs6lao3TuFqnPm9IJJCEkE2w==",
			"license": "Apache-2.0",
			"dependencies": {
				"@stoplight/ordered-object-literal": "^1.0.5",
				"@stoplight/types": "^14.1.1",
				"@stoplight/yaml-ast-parser": "0.0.50",
				"tslib": "^2.2.0"
			},
			"engines": {
				"node": ">=10.8"
			}
		},
		"node_modules/@stoplight/yaml-ast-parser": {
			"version": "0.0.50",
			"resolved": "https://registry.npmjs.org/@stoplight/yaml-ast-parser/-/yaml-ast-parser-0.0.50.tgz",
			"integrity": "sha512-Pb6M8TDO9DtSVla9yXSTAxmo9GVEouq5P40DWXdOie69bXogZTkgvopCq+yEvTMA0F6PEvdJmbtTV3ccIp11VQ==",
			"license": "Apache-2.0"
		},
		"node_modules/@stoplight/yaml/node_modules/@stoplight/types": {
			"version": "14.1.1",
			"resolved": "https://registry.npmjs.org/@stoplight/types/-/types-14.1.1.tgz",
			"integrity": "sha512-/kjtr+0t0tjKr+heVfviO9FrU/uGLc+QNX3fHJc19xsCNYqU7lVhaXxDmEID9BZTjG+/r9pK9xP/xU02XGg65g==",
			"license": "Apache-2.0",
			"dependencies": {
				"@types/json-schema": "^7.0.4",
				"utility-types": "^3.10.0"
			},
			"engines": {
				"node": "^12.20 || >=14.13"
			}
		},
		"node_modules/@stoplight/yaml/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD"
		},
		"node_modules/@szmarczak/http-timer": {
			"version": "5.0.1",
			"resolved": "https://registry.npmjs.org/@szmarczak/http-timer/-/http-timer-5.0.1.tgz",
			"integrity": "sha512-+PmQX0PiAYPMeVYe237LJAYvOMYW1j2rH5YROyS3b4CTVJum34HfRvKvAzozHAQG0TnHNdUfY9nCeUyRAs//cw==",
			"license": "MIT",
			"dependencies": {
				"defer-to-connect": "^2.0.1"
			},
			"engines": {
				"node": ">=14.16"
			}
		},
		"node_modules/@tootallnate/quickjs-emscripten": {
			"version": "0.23.0",
			"resolved": "https://registry.npmjs.org/@tootallnate/quickjs-emscripten/-/quickjs-emscripten-0.23.0.tgz",
			"integrity": "sha512-C5Mc6rdnsaJDjO3UpGW/CQTHtCKaYlScZTly4JIu97Jxo/odCiH0ITnDXSJPTOrEKk/ycSZ0AOgTmkDtkOsvIA==",
			"license": "MIT"
		},
		"node_modules/@types/acorn": {
			"version": "4.0.6",
			"resolved": "https://registry.npmjs.org/@types/acorn/-/acorn-4.0.6.tgz",
			"integrity": "sha512-veQTnWP+1D/xbxVrPC3zHnCZRjSrKfhbMUlEA43iMZLu7EsnTtkJklIuwrCPbOi8YkvDQAiW05VQQFvvz9oieQ==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "*"
			}
		},
		"node_modules/@types/cookie": {
			"version": "0.4.1",
			"resolved": "https://registry.npmjs.org/@types/cookie/-/cookie-0.4.1.tgz",
			"integrity": "sha512-XW/Aa8APYr6jSVVA1y/DEIZX0/GMKLEVekNG727R8cs56ahETkRAy/3DR7+fJyh7oUgGwNQaRfXCun0+KbWY7Q==",
			"license": "MIT"
		},
		"node_modules/@types/cors": {
			"version": "2.8.19",
			"resolved": "https://registry.npmjs.org/@types/cors/-/cors-2.8.19.tgz",
			"integrity": "sha512-mFNylyeyqN93lfe/9CSxOGREz8cpzAhH+E93xJ4xWQf62V8sQ/24reV2nyzUWM6H6Xji+GGHpkbLe7pVoUEskg==",
			"license": "MIT",
			"dependencies": {
				"@types/node": "*"
			}
		},
		"node_modules/@types/debug": {
			"version": "4.1.12",
			"resolved": "https://registry.npmjs.org/@types/debug/-/debug-4.1.12.tgz",
			"integrity": "sha512-vIChWdVG3LG1SMxEvI/AK+FWJthlrqlTu7fbrlywTkkaONwk/UAGaULXRlf8vkzFBLVm0zkMdCquhL5aOjhXPQ==",
			"license": "MIT",
			"dependencies": {
				"@types/ms": "*"
			}
		},
		"node_modules/@types/es-aggregate-error": {
			"version": "1.0.6",
			"resolved": "https://registry.npmjs.org/@types/es-aggregate-error/-/es-aggregate-error-1.0.6.tgz",
			"integrity": "sha512-qJ7LIFp06h1QE1aVxbVd+zJP2wdaugYXYfd6JxsyRMrYHaxb6itXPogW2tz+ylUJ1n1b+JF1PHyYCfYHm0dvUg==",
			"license": "MIT",
			"dependencies": {
				"@types/node": "*"
			}
		},
		"node_modules/@types/estree": {
			"version": "1.0.8",
			"resolved": "https://registry.npmjs.org/@types/estree/-/estree-1.0.8.tgz",
			"integrity": "sha512-dWHzHa2WqEXI/O1E9OjrocMTKJl2mSrEolh1Iomrv6U+JuNwaHXsXx9bLu5gG7BUWFIN0skIQJQ/L1rIex4X6w==",
			"license": "MIT"
		},
		"node_modules/@types/estree-jsx": {
			"version": "1.0.5",
			"resolved": "https://registry.npmjs.org/@types/estree-jsx/-/estree-jsx-1.0.5.tgz",
			"integrity": "sha512-52CcUVNFyfb1A2ALocQw/Dd1BQFNmSdkuC3BkZ6iqhdMfQz7JWOFRuJFloOzjk+6WijU56m9oKXFAXc7o3Towg==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "*"
			}
		},
		"node_modules/@types/hast": {
			"version": "3.0.4",
			"resolved": "https://registry.npmjs.org/@types/hast/-/hast-3.0.4.tgz",
			"integrity": "sha512-WPs+bbQw5aCj+x6laNGWLH3wviHtoCv/P3+otBhbOhJgG8qtpdAMlTCxLtsTWA7LH1Oh/bFCHsBn0TPS5m30EQ==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "*"
			}
		},
		"node_modules/@types/http-cache-semantics": {
			"version": "4.2.0",
			"resolved": "https://registry.npmjs.org/@types/http-cache-semantics/-/http-cache-semantics-4.2.0.tgz",
			"integrity": "sha512-L3LgimLHXtGkWikKnsPg0/VFx9OGZaC+eN1u4r+OB1XRqH3meBIAVC2zr1WdMH+RHmnRkqliQAOHNJ/E0j/e0Q==",
			"license": "MIT"
		},
		"node_modules/@types/json-schema": {
			"version": "7.0.15",
			"resolved": "https://registry.npmjs.org/@types/json-schema/-/json-schema-7.0.15.tgz",
			"integrity": "sha512-5+fP8P8MFNC+AyZCDxrB2pkZFPGzqQWUzpSeuuVLvm8VMcorNYavBqoFcxK8bQz4Qsbn4oUEEem4wDLfcysGHA==",
			"license": "MIT"
		},
		"node_modules/@types/katex": {
			"version": "0.16.8",
			"resolved": "https://registry.npmjs.org/@types/katex/-/katex-0.16.8.tgz",
			"integrity": "sha512-trgaNyfU+Xh2Tc+ABIb44a5AYUpicB3uwirOioeOkNPPbmgRNtcWyDeeFRzjPZENO9Vq8gvVqfhaaXWLlevVwg==",
			"license": "MIT"
		},
		"node_modules/@types/mdast": {
			"version": "4.0.4",
			"resolved": "https://registry.npmjs.org/@types/mdast/-/mdast-4.0.4.tgz",
			"integrity": "sha512-kGaNbPh1k7AFzgpud/gMdvIm5xuECykRR+JnWKQno9TAXVa6WIVCGTPvYGekIDL4uwCZQSYbUxNBSb1aUo79oA==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "*"
			}
		},
		"node_modules/@types/mdx": {
			"version": "2.0.13",
			"resolved": "https://registry.npmjs.org/@types/mdx/-/mdx-2.0.13.tgz",
			"integrity": "sha512-+OWZQfAYyio6YkJb3HLxDrvnx6SWWDbC0zVPfBRzUk0/nqoDyf6dNxQi3eArPe8rJ473nobTMQ/8Zk+LxJ+Yuw==",
			"license": "MIT"
		},
		"node_modules/@types/ms": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/@types/ms/-/ms-2.1.0.tgz",
			"integrity": "sha512-GsCCIZDE/p3i96vtEqx+7dBUGXrc7zeSK3wwPHIaRThS+9OhWIXRqzs4d6k1SVU8g91DrNRWxWUGhp5KXQb2VA==",
			"license": "MIT"
		},
		"node_modules/@types/nlcst": {
			"version": "2.0.3",
			"resolved": "https://registry.npmjs.org/@types/nlcst/-/nlcst-2.0.3.tgz",
			"integrity": "sha512-vSYNSDe6Ix3q+6Z7ri9lyWqgGhJTmzRjZRqyq15N0Z/1/UnVsno9G/N40NBijoYx2seFDIl0+B2mgAb9mezUCA==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "*"
			}
		},
		"node_modules/@types/node": {
			"version": "25.2.3",
			"resolved": "https://registry.npmjs.org/@types/node/-/node-25.2.3.tgz",
			"integrity": "sha512-m0jEgYlYz+mDJZ2+F4v8D1AyQb+QzsNqRuI7xg1VQX/KlKS0qT9r1Mo16yo5F/MtifXFgaofIFsdFMox2SxIbQ==",
			"license": "MIT",
			"dependencies": {
				"undici-types": "~7.16.0"
			}
		},
		"node_modules/@types/react": {
			"version": "19.2.13",
			"resolved": "https://registry.npmjs.org/@types/react/-/react-19.2.13.tgz",
			"integrity": "sha512-KkiJeU6VbYbUOp5ITMIc7kBfqlYkKA5KhEHVrGMmUUMt7NeaZg65ojdPk+FtNrBAOXNVM5QM72jnADjM+XVRAQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"csstype": "^3.2.2"
			}
		},
		"node_modules/@types/unist": {
			"version": "3.0.3",
			"resolved": "https://registry.npmjs.org/@types/unist/-/unist-3.0.3.tgz",
			"integrity": "sha512-ko/gIFJRv177XgZsZcBwnqJN5x/Gien8qNOn0D5bQU/zAzVf9Zt3BlcUiLqhV9y4ARk0GbT3tnUiPNgnTXzc/Q==",
			"license": "MIT"
		},
		"node_modules/@types/urijs": {
			"version": "1.19.26",
			"resolved": "https://registry.npmjs.org/@types/urijs/-/urijs-1.19.26.tgz",
			"integrity": "sha512-wkXrVzX5yoqLnndOwFsieJA7oKM8cNkOKJtf/3vVGSUFkWDKZvFHpIl9Pvqb/T9UsawBBFMTTD8xu7sK5MWuvg==",
			"license": "MIT"
		},
		"node_modules/@types/yauzl": {
			"version": "2.10.3",
			"resolved": "https://registry.npmjs.org/@types/yauzl/-/yauzl-2.10.3.tgz",
			"integrity": "sha512-oJoftv0LSuaDZE3Le4DbKX+KS9G36NzOeSap90UIK0yMA/NhKJhqlSGtNDORNRaIbQfzjXDrQa0ytJ6mNRGz/Q==",
			"license": "MIT",
			"optional": true,
			"dependencies": {
				"@types/node": "*"
			}
		},
		"node_modules/@typescript/vfs": {
			"version": "1.6.2",
			"resolved": "https://registry.npmjs.org/@typescript/vfs/-/vfs-1.6.2.tgz",
			"integrity": "sha512-hoBwJwcbKHmvd2QVebiytN1aELvpk9B74B4L1mFm/XT1Q/VOYAWl2vQ9AWRFtQq8zmz6enTpfTV8WRc4ATjW/g==",
			"license": "MIT",
			"dependencies": {
				"debug": "^4.1.1"
			},
			"peerDependencies": {
				"typescript": "*"
			}
		},
		"node_modules/@ungap/structured-clone": {
			"version": "1.3.0",
			"resolved": "https://registry.npmjs.org/@ungap/structured-clone/-/structured-clone-1.3.0.tgz",
			"integrity": "sha512-WmoN8qaIAo7WTYWbAZuG8PYEhn5fkz7dZrqTBZ7dtt//lL2Gwms1IcnQ5yHqjDfX8Ft5j4YzDM23f87zBfDe9g==",
			"license": "ISC"
		},
		"node_modules/abort-controller": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/abort-controller/-/abort-controller-3.0.0.tgz",
			"integrity": "sha512-h8lQ8tacZYnR3vNQTgibj+tODHI5/+l06Au2Pcriv/Gmet0eaj4TwWH41sO9wnHDiQsEj19q0drzdWdeAHtweg==",
			"license": "MIT",
			"dependencies": {
				"event-target-shim": "^5.0.0"
			},
			"engines": {
				"node": ">=6.5"
			}
		},
		"node_modules/accepts": {
			"version": "1.3.8",
			"resolved": "https://registry.npmjs.org/accepts/-/accepts-1.3.8.tgz",
			"integrity": "sha512-PYAthTa2m2VKxuvSD3DPC/Gy+U+sOA1LAuT8mkmRuvw+NACSaeXEQ+NHcVF7rONl6qcaxV3Uuemwawk+7+SJLw==",
			"license": "MIT",
			"dependencies": {
				"mime-types": "~2.1.34",
				"negotiator": "0.6.3"
			},
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/acorn": {
			"version": "8.11.2",
			"resolved": "https://registry.npmjs.org/acorn/-/acorn-8.11.2.tgz",
			"integrity": "sha512-nc0Axzp/0FILLEVsm4fNwLCwMttvhEI263QtVPQcbpfZZ3ts0hLsZGOpE6czNlid7CJ9MlyH8reXkpsf3YUY4w==",
			"license": "MIT",
			"bin": {
				"acorn": "bin/acorn"
			},
			"engines": {
				"node": ">=0.4.0"
			}
		},
		"node_modules/acorn-jsx": {
			"version": "5.3.2",
			"resolved": "https://registry.npmjs.org/acorn-jsx/-/acorn-jsx-5.3.2.tgz",
			"integrity": "sha512-rq9s+JNhf0IChjtDXxllJ7g41oZk5SlXtp0LHwyA5cejwn7vKmKp4pPri6YEePv2PU65sAsegbXtIinmDFDXgQ==",
			"license": "MIT",
			"peerDependencies": {
				"acorn": "^6.0.0 || ^7.0.0 || ^8.0.0"
			}
		},
		"node_modules/address": {
			"version": "1.2.2",
			"resolved": "https://registry.npmjs.org/address/-/address-1.2.2.tgz",
			"integrity": "sha512-4B/qKCfeE/ODUaAUpSwfzazo5x29WD4r3vXiWsB7I2mSDAihwEqKO+g8GELZUQSSAo5e1XTYh3ZVfLyxBc12nA==",
			"license": "MIT",
			"engines": {
				"node": ">= 10.0.0"
			}
		},
		"node_modules/adm-zip": {
			"version": "0.5.16",
			"resolved": "https://registry.npmjs.org/adm-zip/-/adm-zip-0.5.16.tgz",
			"integrity": "sha512-TGw5yVi4saajsSEgz25grObGHEUaDrniwvA2qwSC060KfqGPdglhvPMA2lPIoxs3PQIItj2iag35fONcQqgUaQ==",
			"license": "MIT",
			"engines": {
				"node": ">=12.0"
			}
		},
		"node_modules/agent-base": {
			"version": "7.1.4",
			"resolved": "https://registry.npmjs.org/agent-base/-/agent-base-7.1.4.tgz",
			"integrity": "sha512-MnA+YT8fwfJPgBx3m60MNqakm30XOkyIoH1y6huTQvC0PwZG7ki8NacLBcrPbNoo8vEZy7Jpuk7+jMO+CUovTQ==",
			"license": "MIT",
			"engines": {
				"node": ">= 14"
			}
		},
		"node_modules/aggregate-error": {
			"version": "4.0.1",
			"resolved": "https://registry.npmjs.org/aggregate-error/-/aggregate-error-4.0.1.tgz",
			"integrity": "sha512-0poP0T7el6Vq3rstR8Mn4V/IQrpBLO6POkUSrN7RhyY+GF/InCFShQzsQ39T25gkHhLgSLByyAz+Kjb+c2L98w==",
			"license": "MIT",
			"dependencies": {
				"clean-stack": "^4.0.0",
				"indent-string": "^5.0.0"
			},
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/ajv": {
			"version": "8.17.1",
			"resolved": "https://registry.npmjs.org/ajv/-/ajv-8.17.1.tgz",
			"integrity": "sha512-B/gBuNg5SiMTrPkC+A2+cW0RszwxYmn6VYxB/inlBStS5nx6xHIt/ehKRhIMhqusl7a8LjQoZnjCs5vhwxOQ1g==",
			"license": "MIT",
			"dependencies": {
				"fast-deep-equal": "^3.1.3",
				"fast-uri": "^3.0.1",
				"json-schema-traverse": "^1.0.0",
				"require-from-string": "^2.0.2"
			},
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/epoberezkin"
			}
		},
		"node_modules/ajv-draft-04": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/ajv-draft-04/-/ajv-draft-04-1.0.0.tgz",
			"integrity": "sha512-mv00Te6nmYbRp5DCwclxtt7yV/joXJPGS7nM+97GdxvuttCOfgI3K4U25zboyeX0O+myI8ERluxQe5wljMmVIw==",
			"license": "MIT",
			"peerDependencies": {
				"ajv": "^8.5.0"
			},
			"peerDependenciesMeta": {
				"ajv": {
					"optional": true
				}
			}
		},
		"node_modules/ajv-errors": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/ajv-errors/-/ajv-errors-3.0.0.tgz",
			"integrity": "sha512-V3wD15YHfHz6y0KdhYFjyy9vWtEVALT9UrxfN3zqlI6dMioHnJrqOYfyPKol3oqrnCM9uwkcdCwkJ0WUcbLMTQ==",
			"license": "MIT",
			"peerDependencies": {
				"ajv": "^8.0.1"
			}
		},
		"node_modules/ajv-formats": {
			"version": "2.1.1",
			"resolved": "https://registry.npmjs.org/ajv-formats/-/ajv-formats-2.1.1.tgz",
			"integrity": "sha512-Wx0Kx52hxE7C18hkMEggYlEifqWZtYaRgouJor+WMdPnQyEK13vgEWyVNup7SoeeoLMsr4kf5h6dOW11I15MUA==",
			"license": "MIT",
			"dependencies": {
				"ajv": "^8.0.0"
			},
			"peerDependencies": {
				"ajv": "^8.0.0"
			},
			"peerDependenciesMeta": {
				"ajv": {
					"optional": true
				}
			}
		},
		"node_modules/ansi-escapes": {
			"version": "7.3.0",
			"resolved": "https://registry.npmjs.org/ansi-escapes/-/ansi-escapes-7.3.0.tgz",
			"integrity": "sha512-BvU8nYgGQBxcmMuEeUEmNTvrMVjJNSH7RgW24vXexN4Ven6qCvy4TntnvlnwnMLTVlcRQQdbRY8NKnaIoeWDNg==",
			"license": "MIT",
			"dependencies": {
				"environment": "^1.0.0"
			},
			"engines": {
				"node": ">=18"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/ansi-regex": {
			"version": "6.2.2",
			"resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-6.2.2.tgz",
			"integrity": "sha512-Bq3SmSpyFHaWjPk8If9yc6svM8c56dB5BAtW4Qbw5jHTwwXXcTLoRMkpDJp6VL0XzlWaCHTXrkFURMYmD0sLqg==",
			"license": "MIT",
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/chalk/ansi-regex?sponsor=1"
			}
		},
		"node_modules/ansi-styles": {
			"version": "6.2.3",
			"resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-6.2.3.tgz",
			"integrity": "sha512-4Dj6M28JB+oAH8kFkTLUo+a2jwOFkuqb3yucU0CANcRRUbxS0cP0nZYCGjcc3BNXwRIsUVmDGgzawme7zvJHvg==",
			"license": "MIT",
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/chalk/ansi-styles?sponsor=1"
			}
		},
		"node_modules/any-promise": {
			"version": "1.3.0",
			"resolved": "https://registry.npmjs.org/any-promise/-/any-promise-1.3.0.tgz",
			"integrity": "sha512-7UvmKalWRt1wgjL1RrGxoSJW/0QZFIegpeGvZG9kjp8vrRu55XTHbwnqq2GpXm9uLbcuhxm3IqX9OB4MZR1b2A==",
			"license": "MIT"
		},
		"node_modules/anymatch": {
			"version": "3.1.3",
			"resolved": "https://registry.npmjs.org/anymatch/-/anymatch-3.1.3.tgz",
			"integrity": "sha512-KMReFUr0B4t+D+OBkjR3KYqvocp2XaSzO55UcB6mgQMd3KbcE+mWTyvVV7D/zsdEbNnV6acZUutkiHQXvTr1Rw==",
			"license": "ISC",
			"dependencies": {
				"normalize-path": "^3.0.0",
				"picomatch": "^2.0.4"
			},
			"engines": {
				"node": ">= 8"
			}
		},
		"node_modules/arg": {
			"version": "5.0.2",
			"resolved": "https://registry.npmjs.org/arg/-/arg-5.0.2.tgz",
			"integrity": "sha512-PYjyFOLKQ9y57JvQ6QLo8dAgNqswh8M1RMJYdQduT6xbWSgK36P/Z/v+p888pM69jMMfS8Xd8F6I1kQ/I9HUGg==",
			"license": "MIT"
		},
		"node_modules/argparse": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/argparse/-/argparse-2.0.1.tgz",
			"integrity": "sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==",
			"license": "Python-2.0"
		},
		"node_modules/aria-hidden": {
			"version": "1.2.6",
			"resolved": "https://registry.npmjs.org/aria-hidden/-/aria-hidden-1.2.6.tgz",
			"integrity": "sha512-ik3ZgC9dY/lYVVM++OISsaYDeg1tb0VtP5uL3ouh1koGOaUMDPpbFIei4JkFimWUFPn90sbMNMXQAIVOlnYKJA==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"tslib": "^2.0.0"
			},
			"engines": {
				"node": ">=10"
			}
		},
		"node_modules/aria-hidden/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD",
			"peer": true
		},
		"node_modules/arkregex": {
			"version": "0.0.3",
			"resolved": "https://registry.npmjs.org/arkregex/-/arkregex-0.0.3.tgz",
			"integrity": "sha512-bU21QJOJEFJK+BPNgv+5bVXkvRxyAvgnon75D92newgHxkBJTgiFwQxusyViYyJkETsddPlHyspshDQcCzmkNg==",
			"license": "MIT",
			"dependencies": {
				"@ark/util": "0.55.0"
			}
		},
		"node_modules/arktype": {
			"version": "2.1.27",
			"resolved": "https://registry.npmjs.org/arktype/-/arktype-2.1.27.tgz",
			"integrity": "sha512-enctOHxI4SULBv/TDtCVi5M8oLd4J5SVlPUblXDzSsOYQNMzmVbUosGBnJuZDKmFlN5Ie0/QVEuTE+Z5X1UhsQ==",
			"license": "MIT",
			"dependencies": {
				"@ark/schema": "0.55.0",
				"@ark/util": "0.55.0",
				"arkregex": "0.0.3"
			}
		},
		"node_modules/array-buffer-byte-length": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/array-buffer-byte-length/-/array-buffer-byte-length-1.0.2.tgz",
			"integrity": "sha512-LHE+8BuR7RYGDKvnrmcuSq3tDcKv9OFEXQt/HpbZhY7V6h0zlUXutnAD82GiFx9rdieCMjkvtcsPqBwgUl1Iiw==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3",
				"is-array-buffer": "^3.0.5"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/array-flatten": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/array-flatten/-/array-flatten-1.1.1.tgz",
			"integrity": "sha512-PCVAQswWemu6UdxsDFFX/+gVeYqKAod3D3UVm91jHwynguOwAvYPhx8nNlM++NqRcK6CxxpUafjmhIdKiHibqg==",
			"license": "MIT"
		},
		"node_modules/array-iterate": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/array-iterate/-/array-iterate-2.0.1.tgz",
			"integrity": "sha512-I1jXZMjAgCMmxT4qxXfPXa6SthSoE8h6gkSI9BGGNv8mP8G/v0blc+qFnZu6K42vTOiuME596QaLO0TP3Lk0xg==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/arraybuffer.prototype.slice": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/arraybuffer.prototype.slice/-/arraybuffer.prototype.slice-1.0.4.tgz",
			"integrity": "sha512-BNoCY6SXXPQ7gF2opIP4GBE+Xw7U+pHMYKuzjgCN3GwiaIR09UUeKfheyIry77QtrCBlC0KK0q5/TER/tYh3PQ==",
			"license": "MIT",
			"dependencies": {
				"array-buffer-byte-length": "^1.0.1",
				"call-bind": "^1.0.8",
				"define-properties": "^1.2.1",
				"es-abstract": "^1.23.5",
				"es-errors": "^1.3.0",
				"get-intrinsic": "^1.2.6",
				"is-array-buffer": "^3.0.4"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/ast-types": {
			"version": "0.13.4",
			"resolved": "https://registry.npmjs.org/ast-types/-/ast-types-0.13.4.tgz",
			"integrity": "sha512-x1FCFnFifvYDDzTaLII71vG5uvDwgtmDTEVWAxrgeiR8VjMONcCXJx7E+USjDtHlwFmt9MysbqgF9b9Vjr6w+w==",
			"license": "MIT",
			"dependencies": {
				"tslib": "^2.0.1"
			},
			"engines": {
				"node": ">=4"
			}
		},
		"node_modules/ast-types/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD"
		},
		"node_modules/astring": {
			"version": "1.9.0",
			"resolved": "https://registry.npmjs.org/astring/-/astring-1.9.0.tgz",
			"integrity": "sha512-LElXdjswlqjWrPpJFg1Fx4wpkOCxj1TDHlSV4PlaRxHGWko024xICaa97ZkMfs6DRKlCguiAI+rbXv5GWwXIkg==",
			"license": "MIT",
			"bin": {
				"astring": "bin/astring"
			}
		},
		"node_modules/async-function": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/async-function/-/async-function-1.0.0.tgz",
			"integrity": "sha512-hsU18Ae8CDTR6Kgu9DYf0EbCr/a5iGL0rytQDobUcdpYOKokk8LEjVphnXkDkgpi0wYVsqrXuP0bZxJaTqdgoA==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/asynckit": {
			"version": "0.4.0",
			"resolved": "https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz",
			"integrity": "sha512-Oei9OH4tRh0YqU3GxhX79dM/mwVgvbZJaSNaRk+bshkj0S5cfHcgYakreBjrHwatXKbz+IoIdYLxrKim2MjW0Q==",
			"license": "MIT"
		},
		"node_modules/auto-bind": {
			"version": "5.0.1",
			"resolved": "https://registry.npmjs.org/auto-bind/-/auto-bind-5.0.1.tgz",
			"integrity": "sha512-ooviqdwwgfIfNmDwo94wlshcdzfO64XV0Cg6oDsDYBJfITDz1EngD2z7DkbvCWn+XIMsIqW27sEVF6qcpJrRcg==",
			"license": "MIT",
			"engines": {
				"node": "^12.20.0 || ^14.13.1 || >=16.0.0"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/available-typed-arrays": {
			"version": "1.0.7",
			"resolved": "https://registry.npmjs.org/available-typed-arrays/-/available-typed-arrays-1.0.7.tgz",
			"integrity": "sha512-wvUjBtSGN7+7SjNpq/9M2Tg350UZD3q62IFZLbRAR1bSMlCo1ZaeW+BJ+D090e4hIIZLBcTDWe4Mh4jvUDajzQ==",
			"license": "MIT",
			"dependencies": {
				"possible-typed-array-names": "^1.0.0"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/avsc": {
			"version": "5.7.9",
			"resolved": "https://registry.npmjs.org/avsc/-/avsc-5.7.9.tgz",
			"integrity": "sha512-yOA4wFeI7ET3v32Di/sUybQ+ttP20JHSW3mxLuNGeO0uD6PPcvLrIQXSvy/rhJOWU5JrYh7U4OHplWMmtAtjMg==",
			"license": "MIT",
			"engines": {
				"node": ">=0.11"
			}
		},
		"node_modules/axios": {
			"version": "1.13.5",
			"resolved": "https://registry.npmjs.org/axios/-/axios-1.13.5.tgz",
			"integrity": "sha512-cz4ur7Vb0xS4/KUN0tPWe44eqxrIu31me+fbang3ijiNscE129POzipJJA6zniq2C/Z6sJCjMimjS8Lc/GAs8Q==",
			"license": "MIT",
			"dependencies": {
				"follow-redirects": "^1.15.11",
				"form-data": "^4.0.5",
				"proxy-from-env": "^1.1.0"
			}
		},
		"node_modules/b4a": {
			"version": "1.7.3",
			"resolved": "https://registry.npmjs.org/b4a/-/b4a-1.7.3.tgz",
			"integrity": "sha512-5Q2mfq2WfGuFp3uS//0s6baOJLMoVduPYVeNmDYxu5OUA1/cBfvr2RIS7vi62LdNj/urk1hfmj867I3qt6uZ7Q==",
			"license": "Apache-2.0",
			"peerDependencies": {
				"react-native-b4a": "*"
			},
			"peerDependenciesMeta": {
				"react-native-b4a": {
					"optional": true
				}
			}
		},
		"node_modules/bail": {
			"version": "2.0.2",
			"resolved": "https://registry.npmjs.org/bail/-/bail-2.0.2.tgz",
			"integrity": "sha512-0xO6mYd7JB2YesxDKplafRpsiOzPt9V02ddPCLbY1xYGPOX24NTyN50qnUxgCPcSoYMhKpAuBTjQoRZCAkUDRw==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/balanced-match": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
			"integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==",
			"license": "MIT"
		},
		"node_modules/bare-events": {
			"version": "2.8.2",
			"resolved": "https://registry.npmjs.org/bare-events/-/bare-events-2.8.2.tgz",
			"integrity": "sha512-riJjyv1/mHLIPX4RwiK+oW9/4c3TEUeORHKefKAKnZ5kyslbN+HXowtbaVEqt4IMUB7OXlfixcs6gsFeo/jhiQ==",
			"license": "Apache-2.0",
			"peerDependencies": {
				"bare-abort-controller": "*"
			},
			"peerDependenciesMeta": {
				"bare-abort-controller": {
					"optional": true
				}
			}
		},
		"node_modules/bare-fs": {
			"version": "4.5.3",
			"resolved": "https://registry.npmjs.org/bare-fs/-/bare-fs-4.5.3.tgz",
			"integrity": "sha512-9+kwVx8QYvt3hPWnmb19tPnh38c6Nihz8Lx3t0g9+4GoIf3/fTgYwM4Z6NxgI+B9elLQA7mLE9PpqcWtOMRDiQ==",
			"license": "Apache-2.0",
			"optional": true,
			"dependencies": {
				"bare-events": "^2.5.4",
				"bare-path": "^3.0.0",
				"bare-stream": "^2.6.4",
				"bare-url": "^2.2.2",
				"fast-fifo": "^1.3.2"
			},
			"engines": {
				"bare": ">=1.16.0"
			},
			"peerDependencies": {
				"bare-buffer": "*"
			},
			"peerDependenciesMeta": {
				"bare-buffer": {
					"optional": true
				}
			}
		},
		"node_modules/bare-os": {
			"version": "3.6.2",
			"resolved": "https://registry.npmjs.org/bare-os/-/bare-os-3.6.2.tgz",
			"integrity": "sha512-T+V1+1srU2qYNBmJCXZkUY5vQ0B4FSlL3QDROnKQYOqeiQR8UbjNHlPa+TIbM4cuidiN9GaTaOZgSEgsvPbh5A==",
			"license": "Apache-2.0",
			"optional": true,
			"engines": {
				"bare": ">=1.14.0"
			}
		},
		"node_modules/bare-path": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/bare-path/-/bare-path-3.0.0.tgz",
			"integrity": "sha512-tyfW2cQcB5NN8Saijrhqn0Zh7AnFNsnczRcuWODH0eYAXBsJ5gVxAUuNr7tsHSC6IZ77cA0SitzT+s47kot8Mw==",
			"license": "Apache-2.0",
			"optional": true,
			"dependencies": {
				"bare-os": "^3.0.1"
			}
		},
		"node_modules/bare-stream": {
			"version": "2.7.0",
			"resolved": "https://registry.npmjs.org/bare-stream/-/bare-stream-2.7.0.tgz",
			"integrity": "sha512-oyXQNicV1y8nc2aKffH+BUHFRXmx6VrPzlnaEvMhram0nPBrKcEdcyBg5r08D0i8VxngHFAiVyn1QKXpSG0B8A==",
			"license": "Apache-2.0",
			"optional": true,
			"dependencies": {
				"streamx": "^2.21.0"
			},
			"peerDependencies": {
				"bare-buffer": "*",
				"bare-events": "*"
			},
			"peerDependenciesMeta": {
				"bare-buffer": {
					"optional": true
				},
				"bare-events": {
					"optional": true
				}
			}
		},
		"node_modules/bare-url": {
			"version": "2.3.2",
			"resolved": "https://registry.npmjs.org/bare-url/-/bare-url-2.3.2.tgz",
			"integrity": "sha512-ZMq4gd9ngV5aTMa5p9+UfY0b3skwhHELaDkhEHetMdX0LRkW9kzaym4oo/Eh+Ghm0CCDuMTsRIGM/ytUc1ZYmw==",
			"license": "Apache-2.0",
			"optional": true,
			"dependencies": {
				"bare-path": "^3.0.0"
			}
		},
		"node_modules/base64-js": {
			"version": "1.5.1",
			"resolved": "https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz",
			"integrity": "sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==",
			"funding": [
				{
					"type": "github",
					"url": "https://github.com/sponsors/feross"
				},
				{
					"type": "patreon",
					"url": "https://www.patreon.com/feross"
				},
				{
					"type": "consulting",
					"url": "https://feross.org/support"
				}
			],
			"license": "MIT"
		},
		"node_modules/base64id": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/base64id/-/base64id-2.0.0.tgz",
			"integrity": "sha512-lGe34o6EHj9y3Kts9R4ZYs/Gr+6N7MCaMlIFA3F1R2O5/m7K06AxfSeO5530PEERE6/WyEg3lsuyw4GHlPZHog==",
			"license": "MIT",
			"engines": {
				"node": "^4.5.0 || >= 5.9"
			}
		},
		"node_modules/basic-ftp": {
			"version": "5.1.0",
			"resolved": "https://registry.npmjs.org/basic-ftp/-/basic-ftp-5.1.0.tgz",
			"integrity": "sha512-RkaJzeJKDbaDWTIPiJwubyljaEPwpVWkm9Rt5h9Nd6h7tEXTJ3VB4qxdZBioV7JO5yLUaOKwz7vDOzlncUsegw==",
			"license": "MIT",
			"engines": {
				"node": ">=10.0.0"
			}
		},
		"node_modules/better-opn": {
			"version": "3.0.2",
			"resolved": "https://registry.npmjs.org/better-opn/-/better-opn-3.0.2.tgz",
			"integrity": "sha512-aVNobHnJqLiUelTaHat9DZ1qM2w0C0Eym4LPI/3JxOnSokGVdsl1T1kN7TFvsEAD8G47A6VKQ0TVHqbBnYMJlQ==",
			"license": "MIT",
			"dependencies": {
				"open": "^8.0.4"
			},
			"engines": {
				"node": ">=12.0.0"
			}
		},
		"node_modules/binary-extensions": {
			"version": "2.3.0",
			"resolved": "https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.3.0.tgz",
			"integrity": "sha512-Ceh+7ox5qe7LJuLHoY0feh3pHuUDHAcRUeyL2VYghZwfpkNIy/+8Ocg0a3UuSoYzavmylwuLWQOf3hl0jjMMIw==",
			"license": "MIT",
			"engines": {
				"node": ">=8"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/body-parser": {
			"version": "1.20.3",
			"resolved": "https://registry.npmjs.org/body-parser/-/body-parser-1.20.3.tgz",
			"integrity": "sha512-7rAxByjUMqQ3/bHJy7D6OGXvx/MMc4IqBn/X0fcM1QUcAItpZrBEYhWGem+tzXH90c+G01ypMcYJBO9Y30203g==",
			"license": "MIT",
			"dependencies": {
				"bytes": "3.1.2",
				"content-type": "~1.0.5",
				"debug": "2.6.9",
				"depd": "2.0.0",
				"destroy": "1.2.0",
				"http-errors": "2.0.0",
				"iconv-lite": "0.4.24",
				"on-finished": "2.4.1",
				"qs": "6.13.0",
				"raw-body": "2.5.2",
				"type-is": "~1.6.18",
				"unpipe": "1.0.0"
			},
			"engines": {
				"node": ">= 0.8",
				"npm": "1.2.8000 || >= 1.4.16"
			}
		},
		"node_modules/body-parser/node_modules/debug": {
			"version": "2.6.9",
			"resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
			"integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
			"license": "MIT",
			"dependencies": {
				"ms": "2.0.0"
			}
		},
		"node_modules/body-parser/node_modules/iconv-lite": {
			"version": "0.4.24",
			"resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz",
			"integrity": "sha512-v3MXnZAcvnywkTUEZomIActle7RXXeedOR31wwl7VlyoXO4Qi9arvSenNQWne1TcRwhCL1HwLI21bEqdpj8/rA==",
			"license": "MIT",
			"dependencies": {
				"safer-buffer": ">= 2.1.2 < 3"
			},
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/body-parser/node_modules/ms": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
			"integrity": "sha512-Tpp60P6IUJDTuOq/5Z8cdskzJujfwqfOTkrwIwj7IRISpnkJnT6SyJ4PCPnGMoFjC9ddhal5KVIYtAt97ix05A==",
			"license": "MIT"
		},
		"node_modules/brace-expansion": {
			"version": "1.1.12",
			"resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.12.tgz",
			"integrity": "sha512-9T9UjW3r0UW5c1Q7GTwllptXwhvYmEzFhzMfZ9H7FQWt+uZePjZPjBP/W1ZEyZ1twGWom5/56TF4lPcqjnDHcg==",
			"license": "MIT",
			"dependencies": {
				"balanced-match": "^1.0.0",
				"concat-map": "0.0.1"
			}
		},
		"node_modules/braces": {
			"version": "3.0.3",
			"resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
			"integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
			"license": "MIT",
			"dependencies": {
				"fill-range": "^7.1.1"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/buffer": {
			"version": "5.7.1",
			"resolved": "https://registry.npmjs.org/buffer/-/buffer-5.7.1.tgz",
			"integrity": "sha512-EHcyIPBQ4BSGlvjB16k5KgAJ27CIsHY/2JBmCRReo48y9rQ3MaUzWX3KVlBa4U7MyX02HdVj0K7C3WaB3ju7FQ==",
			"funding": [
				{
					"type": "github",
					"url": "https://github.com/sponsors/feross"
				},
				{
					"type": "patreon",
					"url": "https://www.patreon.com/feross"
				},
				{
					"type": "consulting",
					"url": "https://feross.org/support"
				}
			],
			"license": "MIT",
			"dependencies": {
				"base64-js": "^1.3.1",
				"ieee754": "^1.1.13"
			}
		},
		"node_modules/buffer-crc32": {
			"version": "0.2.13",
			"resolved": "https://registry.npmjs.org/buffer-crc32/-/buffer-crc32-0.2.13.tgz",
			"integrity": "sha512-VO9Ht/+p3SN7SKWqcrgEzjGbRSJYTx+Q1pTQC0wrWqHx0vpJraQ6GtHx8tvcg1rlK1byhU5gccxgOgj7B0TDkQ==",
			"license": "MIT",
			"engines": {
				"node": "*"
			}
		},
		"node_modules/bytes": {
			"version": "3.1.2",
			"resolved": "https://registry.npmjs.org/bytes/-/bytes-3.1.2.tgz",
			"integrity": "sha512-/Nf7TyzTx6S3yRJObOAV7956r8cr2+Oj8AC5dt8wSP3BQAoeX58NoHyCU8P8zGkNXStjTSi6fzO6F0pBdcYbEg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/cacheable-lookup": {
			"version": "7.0.0",
			"resolved": "https://registry.npmjs.org/cacheable-lookup/-/cacheable-lookup-7.0.0.tgz",
			"integrity": "sha512-+qJyx4xiKra8mZrcwhjMRMUhD5NR1R8esPkzIYxX96JiecFoxAXFuz/GpR3+ev4PE1WamHip78wV0vcmPQtp8w==",
			"license": "MIT",
			"engines": {
				"node": ">=14.16"
			}
		},
		"node_modules/cacheable-request": {
			"version": "10.2.14",
			"resolved": "https://registry.npmjs.org/cacheable-request/-/cacheable-request-10.2.14.tgz",
			"integrity": "sha512-zkDT5WAF4hSSoUgyfg5tFIxz8XQK+25W/TLVojJTMKBaxevLBBtLxgqguAuVQB8PVW79FVjHcU+GJ9tVbDZ9mQ==",
			"license": "MIT",
			"dependencies": {
				"@types/http-cache-semantics": "^4.0.2",
				"get-stream": "^6.0.1",
				"http-cache-semantics": "^4.1.1",
				"keyv": "^4.5.3",
				"mimic-response": "^4.0.0",
				"normalize-url": "^8.0.0",
				"responselike": "^3.0.0"
			},
			"engines": {
				"node": ">=14.16"
			}
		},
		"node_modules/call-bind": {
			"version": "1.0.8",
			"resolved": "https://registry.npmjs.org/call-bind/-/call-bind-1.0.8.tgz",
			"integrity": "sha512-oKlSFMcMwpUg2ednkhQ454wfWiU/ul3CkJe/PEHcTKuiX6RpbehUiFMXu13HalGZxfUwCQzZG747YXBn1im9ww==",
			"license": "MIT",
			"dependencies": {
				"call-bind-apply-helpers": "^1.0.0",
				"es-define-property": "^1.0.0",
				"get-intrinsic": "^1.2.4",
				"set-function-length": "^1.2.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/call-bind-apply-helpers": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
			"integrity": "sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==",
			"license": "MIT",
			"dependencies": {
				"es-errors": "^1.3.0",
				"function-bind": "^1.1.2"
			},
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/call-bound": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz",
			"integrity": "sha512-+ys997U96po4Kx/ABpBCqhA9EuxJaQWDQg7295H4hBphv3IZg0boBKuwYpt4YXp6MZ5AmZQnU/tyMTlRpaSejg==",
			"license": "MIT",
			"dependencies": {
				"call-bind-apply-helpers": "^1.0.2",
				"get-intrinsic": "^1.3.0"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/callsites": {
			"version": "3.1.0",
			"resolved": "https://registry.npmjs.org/callsites/-/callsites-3.1.0.tgz",
			"integrity": "sha512-P8BjAsXvZS+VIDUI11hHCQEv74YT67YUi5JJFNWIqL235sBmjX4+qx9Muvls5ivyNENctx46xQLQ3aTuE7ssaQ==",
			"license": "MIT",
			"engines": {
				"node": ">=6"
			}
		},
		"node_modules/camelcase-css": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/camelcase-css/-/camelcase-css-2.0.1.tgz",
			"integrity": "sha512-QOSvevhslijgYwRx6Rv7zKdMF8lbRmx+uQGx2+vDc+KI/eBnsy9kit5aj23AgGu3pa4t9AgwbnXWqS+iOY+2aA==",
			"license": "MIT",
			"engines": {
				"node": ">= 6"
			}
		},
		"node_modules/ccount": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/ccount/-/ccount-2.0.1.tgz",
			"integrity": "sha512-eyrF0jiFpY+3drT6383f1qhkbGsLSifNAjA61IUjZjmLCWjItY6LB9ft9YhoDgwfmclB2zhu51Lc7+95b8NRAg==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/chalk": {
			"version": "5.2.0",
			"resolved": "https://registry.npmjs.org/chalk/-/chalk-5.2.0.tgz",
			"integrity": "sha512-ree3Gqw/nazQAPuJJEy+avdl7QfZMcUvmHIKgEZkGL+xOBzRvup5Hxo6LHuMceSxOabuJLJm5Yp/92R9eMmMvA==",
			"license": "MIT",
			"engines": {
				"node": "^12.17.0 || ^14.13 || >=16.0.0"
			},
			"funding": {
				"url": "https://github.com/chalk/chalk?sponsor=1"
			}
		},
		"node_modules/character-entities": {
			"version": "2.0.2",
			"resolved": "https://registry.npmjs.org/character-entities/-/character-entities-2.0.2.tgz",
			"integrity": "sha512-shx7oQ0Awen/BRIdkjkvz54PnEEI/EjwXDSIZp86/KKdbafHh1Df/RYGBhn4hbe2+uKC9FnT5UCEdyPz3ai9hQ==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/character-entities-html4": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/character-entities-html4/-/character-entities-html4-2.1.0.tgz",
			"integrity": "sha512-1v7fgQRj6hnSwFpq1Eu0ynr/CDEw0rXo2B61qXrLNdHZmPKgb7fqS1a2JwF0rISo9q77jDI8VMEHoApn8qDoZA==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/character-entities-legacy": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/character-entities-legacy/-/character-entities-legacy-3.0.0.tgz",
			"integrity": "sha512-RpPp0asT/6ufRm//AJVwpViZbGM/MkjQFxJccQRHmISF/22NBtsHqAWmL+/pmkPWoIUJdWyeVleTl1wydHATVQ==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/character-reference-invalid": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/character-reference-invalid/-/character-reference-invalid-2.0.1.tgz",
			"integrity": "sha512-iBZ4F4wRbyORVsu0jPV7gXkOsGYjGHPmAyv+HiHG8gi5PtC9KI2j1+v8/tlibRvjoWX027ypmG/n0HtO5t7unw==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/chardet": {
			"version": "2.1.1",
			"resolved": "https://registry.npmjs.org/chardet/-/chardet-2.1.1.tgz",
			"integrity": "sha512-PsezH1rqdV9VvyNhxxOW32/d75r01NY7TQCmOqomRo15ZSOKbpTFVsfjghxo6JloQUCGnH4k1LGu0R4yCLlWQQ==",
			"license": "MIT"
		},
		"node_modules/chokidar": {
			"version": "3.5.3",
			"resolved": "https://registry.npmjs.org/chokidar/-/chokidar-3.5.3.tgz",
			"integrity": "sha512-Dr3sfKRP6oTcjf2JmUmFJfeVMvXBdegxB0iVQ5eb2V10uFJUCAS8OByZdVAyVb8xXNz3GjjTgj9kLWsZTqE6kw==",
			"funding": [
				{
					"type": "individual",
					"url": "https://paulmillr.com/funding/"
				}
			],
			"license": "MIT",
			"dependencies": {
				"anymatch": "~3.1.2",
				"braces": "~3.0.2",
				"glob-parent": "~5.1.2",
				"is-binary-path": "~2.1.0",
				"is-glob": "~4.0.1",
				"normalize-path": "~3.0.0",
				"readdirp": "~3.6.0"
			},
			"engines": {
				"node": ">= 8.10.0"
			},
			"optionalDependencies": {
				"fsevents": "~2.3.2"
			}
		},
		"node_modules/chownr": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/chownr/-/chownr-2.0.0.tgz",
			"integrity": "sha512-bIomtDF5KGpdogkLd9VspvFzk9KfpyyGlS8YFVZl7TGPBHL5snIOnxeshwVgPteQ9b4Eydl+pVbIyE1DcvCWgQ==",
			"license": "ISC",
			"engines": {
				"node": ">=10"
			}
		},
		"node_modules/chromium-bidi": {
			"version": "0.6.2",
			"resolved": "https://registry.npmjs.org/chromium-bidi/-/chromium-bidi-0.6.2.tgz",
			"integrity": "sha512-4WVBa6ijmUTVr9cZD4eicQD8Mdy/HCX3bzEIYYpmk0glqYLoWH+LqQEvV9RpDRzoQSbY1KJHloYXbDMXMbDPhg==",
			"license": "Apache-2.0",
			"dependencies": {
				"mitt": "3.0.1",
				"urlpattern-polyfill": "10.0.0",
				"zod": "3.23.8"
			},
			"peerDependencies": {
				"devtools-protocol": "*"
			}
		},
		"node_modules/chromium-bidi/node_modules/zod": {
			"version": "3.23.8",
			"resolved": "https://registry.npmjs.org/zod/-/zod-3.23.8.tgz",
			"integrity": "sha512-XBx9AXhXktjUqnepgTiE5flcKIYWi/rme0Eaj+5Y0lftuGBq+jyRu/md4WnuxqgP1ubdpNCsYEYPxrzVHD8d6g==",
			"license": "MIT",
			"funding": {
				"url": "https://github.com/sponsors/colinhacks"
			}
		},
		"node_modules/clean-stack": {
			"version": "4.2.0",
			"resolved": "https://registry.npmjs.org/clean-stack/-/clean-stack-4.2.0.tgz",
			"integrity": "sha512-LYv6XPxoyODi36Dp976riBtSY27VmFo+MKqEU9QCCWyTrdEPDog+RWA7xQWHi6Vbp61j5c4cdzzX1NidnwtUWg==",
			"license": "MIT",
			"dependencies": {
				"escape-string-regexp": "5.0.0"
			},
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/cli-boxes": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/cli-boxes/-/cli-boxes-3.0.0.tgz",
			"integrity": "sha512-/lzGpEWL/8PfI0BmBOPRwp0c/wFNX1RdUML3jK/RcSBA9T8mZDdQpqYBKtCFTOfQbwPqWEOpjqW+Fnayc0969g==",
			"license": "MIT",
			"engines": {
				"node": ">=10"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/cli-cursor": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/cli-cursor/-/cli-cursor-4.0.0.tgz",
			"integrity": "sha512-VGtlMu3x/4DOtIUwEkRezxUZ2lBacNJCHash0N0WeZDBS+7Ux1dm3XWAgWYxLJFMMdOeXMHXorshEFhbMSGelg==",
			"license": "MIT",
			"dependencies": {
				"restore-cursor": "^4.0.0"
			},
			"engines": {
				"node": "^12.20.0 || ^14.13.1 || >=16.0.0"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/cli-spinners": {
			"version": "2.9.2",
			"resolved": "https://registry.npmjs.org/cli-spinners/-/cli-spinners-2.9.2.tgz",
			"integrity": "sha512-ywqV+5MmyL4E7ybXgKys4DugZbX0FC6LnwrhjuykIjnK9k8OQacQ7axGKnjDXWNhns0xot3bZI5h55H8yo9cJg==",
			"license": "MIT",
			"engines": {
				"node": ">=6"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/cli-truncate": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/cli-truncate/-/cli-truncate-4.0.0.tgz",
			"integrity": "sha512-nPdaFdQ0h/GEigbPClz11D0v/ZJEwxmeVZGeMo3Z5StPtUTkA9o1lD6QwoirYiSDzbcwn2XcjwmCp68W1IS4TA==",
			"license": "MIT",
			"dependencies": {
				"slice-ansi": "^5.0.0",
				"string-width": "^7.0.0"
			},
			"engines": {
				"node": ">=18"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/cli-truncate/node_modules/is-fullwidth-code-point": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-4.0.0.tgz",
			"integrity": "sha512-O4L094N2/dZ7xqVdrXhh9r1KODPJpFms8B5sGdJLPy664AgvXsreZUyCQQNItZRDlYug4xStLjNp/sz3HvBowQ==",
			"license": "MIT",
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/cli-truncate/node_modules/slice-ansi": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/slice-ansi/-/slice-ansi-5.0.0.tgz",
			"integrity": "sha512-FC+lgizVPfie0kkhqUScwRu1O/lF6NOgJmlCgK+/LYxDCTk8sGelYaHDhFcDN+Sn3Cv+3VSa4Byeo+IMCzpMgQ==",
			"license": "MIT",
			"dependencies": {
				"ansi-styles": "^6.0.0",
				"is-fullwidth-code-point": "^4.0.0"
			},
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/chalk/slice-ansi?sponsor=1"
			}
		},
		"node_modules/cli-width": {
			"version": "4.1.0",
			"resolved": "https://registry.npmjs.org/cli-width/-/cli-width-4.1.0.tgz",
			"integrity": "sha512-ouuZd4/dm2Sw5Gmqy6bGyNNNe1qt9RpmxveLSO7KcgsTnU7RXfsw+/bukWGo1abgBiMAic068rclZsO4IWmmxQ==",
			"license": "ISC",
			"engines": {
				"node": ">= 12"
			}
		},
		"node_modules/cliui": {
			"version": "8.0.1",
			"resolved": "https://registry.npmjs.org/cliui/-/cliui-8.0.1.tgz",
			"integrity": "sha512-BSeNnyus75C4//NQ9gQt1/csTXyo/8Sb+afLAkzAptFuMsod9HFokGNudZpi/oQV73hnVK+sR+5PVRMd+Dr7YQ==",
			"license": "ISC",
			"dependencies": {
				"string-width": "^4.2.0",
				"strip-ansi": "^6.0.1",
				"wrap-ansi": "^7.0.0"
			},
			"engines": {
				"node": ">=12"
			}
		},
		"node_modules/cliui/node_modules/ansi-regex": {
			"version": "5.0.1",
			"resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
			"integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
			"license": "MIT",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/cliui/node_modules/ansi-styles": {
			"version": "4.3.0",
			"resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
			"integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
			"license": "MIT",
			"dependencies": {
				"color-convert": "^2.0.1"
			},
			"engines": {
				"node": ">=8"
			},
			"funding": {
				"url": "https://github.com/chalk/ansi-styles?sponsor=1"
			}
		},
		"node_modules/cliui/node_modules/emoji-regex": {
			"version": "8.0.0",
			"resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
			"integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
			"license": "MIT"
		},
		"node_modules/cliui/node_modules/is-fullwidth-code-point": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz",
			"integrity": "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==",
			"license": "MIT",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/cliui/node_modules/string-width": {
			"version": "4.2.3",
			"resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
			"integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
			"license": "MIT",
			"dependencies": {
				"emoji-regex": "^8.0.0",
				"is-fullwidth-code-point": "^3.0.0",
				"strip-ansi": "^6.0.1"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/cliui/node_modules/strip-ansi": {
			"version": "6.0.1",
			"resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
			"integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
			"license": "MIT",
			"dependencies": {
				"ansi-regex": "^5.0.1"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/cliui/node_modules/wrap-ansi": {
			"version": "7.0.0",
			"resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz",
			"integrity": "sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q==",
			"license": "MIT",
			"dependencies": {
				"ansi-styles": "^4.0.0",
				"string-width": "^4.1.0",
				"strip-ansi": "^6.0.0"
			},
			"engines": {
				"node": ">=10"
			},
			"funding": {
				"url": "https://github.com/chalk/wrap-ansi?sponsor=1"
			}
		},
		"node_modules/code-excerpt": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/code-excerpt/-/code-excerpt-4.0.0.tgz",
			"integrity": "sha512-xxodCmBen3iy2i0WtAK8FlFNrRzjUqjRsMfho58xT/wvZU1YTM3fCnRjcy1gJPMepaRlgm/0e6w8SpWHpn3/cA==",
			"license": "MIT",
			"dependencies": {
				"convert-to-spaces": "^2.0.1"
			},
			"engines": {
				"node": "^12.20.0 || ^14.13.1 || >=16.0.0"
			}
		},
		"node_modules/collapse-white-space": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/collapse-white-space/-/collapse-white-space-2.1.0.tgz",
			"integrity": "sha512-loKTxY1zCOuG4j9f6EPnuyyYkf58RnhhWTvRoZEokgB+WbdXehfjFviyOVYkqzEWz1Q5kRiZdBYS5SwxbQYwzw==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/color": {
			"version": "4.2.3",
			"resolved": "https://registry.npmjs.org/color/-/color-4.2.3.tgz",
			"integrity": "sha512-1rXeuUUiGGrykh+CeBdu5Ie7OJwinCgQY0bc7GCRxy5xVHy+moaqkpL/jqQq0MtQOeYcrqEz4abc5f0KtU7W4A==",
			"license": "MIT",
			"dependencies": {
				"color-convert": "^2.0.1",
				"color-string": "^1.9.0"
			},
			"engines": {
				"node": ">=12.5.0"
			}
		},
		"node_modules/color-blend": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/color-blend/-/color-blend-4.0.0.tgz",
			"integrity": "sha512-fYODTHhI/NG+B5GnzvuL3kiFrK/UnkUezWFTgEPBTY5V+kpyfAn95Vn9sJeeCX6omrCOdxnqCL3CvH+6sXtIbw==",
			"license": "MIT",
			"engines": {
				"node": ">=10.0.0"
			}
		},
		"node_modules/color-convert": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
			"integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
			"license": "MIT",
			"dependencies": {
				"color-name": "~1.1.4"
			},
			"engines": {
				"node": ">=7.0.0"
			}
		},
		"node_modules/color-name": {
			"version": "1.1.4",
			"resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz",
			"integrity": "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==",
			"license": "MIT"
		},
		"node_modules/color-string": {
			"version": "1.9.1",
			"resolved": "https://registry.npmjs.org/color-string/-/color-string-1.9.1.tgz",
			"integrity": "sha512-shrVawQFojnZv6xM40anx4CkoDP+fZsw/ZerEMsW/pyzsRbElpsL/DBVW7q3ExxwusdNXI3lXpuhEZkzs8p5Eg==",
			"license": "MIT",
			"dependencies": {
				"color-name": "^1.0.0",
				"simple-swizzle": "^0.2.2"
			}
		},
		"node_modules/combined-stream": {
			"version": "1.0.8",
			"resolved": "https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz",
			"integrity": "sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==",
			"license": "MIT",
			"dependencies": {
				"delayed-stream": "~1.0.0"
			},
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/comma-separated-tokens": {
			"version": "2.0.3",
			"resolved": "https://registry.npmjs.org/comma-separated-tokens/-/comma-separated-tokens-2.0.3.tgz",
			"integrity": "sha512-Fu4hJdvzeylCfQPp9SGWidpzrMs7tTrlu6Vb8XGaRGck8QSNZJJp538Wrb60Lax4fPwR64ViY468OIUTbRlGZg==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/commander": {
			"version": "8.3.0",
			"resolved": "https://registry.npmjs.org/commander/-/commander-8.3.0.tgz",
			"integrity": "sha512-OkTL9umf+He2DZkUq8f8J9of7yL6RJKI24dVITBmNfZBmri9zYZQrKkuXiKhyfPSu8tUhnVBB1iKXevvnlR4Ww==",
			"license": "MIT",
			"engines": {
				"node": ">= 12"
			}
		},
		"node_modules/concat-map": {
			"version": "0.0.1",
			"resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
			"integrity": "sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg==",
			"license": "MIT"
		},
		"node_modules/content-disposition": {
			"version": "0.5.4",
			"resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-0.5.4.tgz",
			"integrity": "sha512-FveZTNuGw04cxlAiWbzi6zTAL/lhehaWbTtgluJh4/E95DqMwTmha3KZN1aAWA8cFIhHzMZUvLevkw5Rqk+tSQ==",
			"license": "MIT",
			"dependencies": {
				"safe-buffer": "5.2.1"
			},
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/content-type": {
			"version": "1.0.5",
			"resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.5.tgz",
			"integrity": "sha512-nTjqfcBFEipKdXCv4YDQWCfmcLZKm81ldF0pAopTvyrFGVbcR6P/VAAd5G7N+0tTr8QqiU0tFadD6FK4NtJwOA==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/convert-to-spaces": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/convert-to-spaces/-/convert-to-spaces-2.0.1.tgz",
			"integrity": "sha512-rcQ1bsQO9799wq24uE5AM2tAILy4gXGIK/njFWcVQkGNZ96edlpY+A7bjwvzjYvLDyzmG1MmMLZhpcsb+klNMQ==",
			"license": "MIT",
			"engines": {
				"node": "^12.20.0 || ^14.13.1 || >=16.0.0"
			}
		},
		"node_modules/cookie": {
			"version": "0.7.0",
			"resolved": "https://registry.npmjs.org/cookie/-/cookie-0.7.0.tgz",
			"integrity": "sha512-qCf+V4dtlNhSRXGAZatc1TasyFO6GjohcOul807YOb5ik3+kQSnb4d7iajeCL8QHaJ4uZEjCgiCJerKXwdRVlQ==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/cookie-signature": {
			"version": "1.0.6",
			"resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.0.6.tgz",
			"integrity": "sha512-QADzlaHc8icV8I7vbaJXJwod9HWYp8uCqf1xa4OfNu1T7JVxQIrUgOWtHdNDtPiywmFbiS12VjotIXLrKM3orQ==",
			"license": "MIT"
		},
		"node_modules/cors": {
			"version": "2.8.6",
			"resolved": "https://registry.npmjs.org/cors/-/cors-2.8.6.tgz",
			"integrity": "sha512-tJtZBBHA6vjIAaF6EnIaq6laBBP9aq/Y3ouVJjEfoHbRBcHBAHYcMh/w8LDrk2PvIMMq8gmopa5D4V8RmbrxGw==",
			"license": "MIT",
			"dependencies": {
				"object-assign": "^4",
				"vary": "^1"
			},
			"engines": {
				"node": ">= 0.10"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/express"
			}
		},
		"node_modules/cosmiconfig": {
			"version": "9.0.0",
			"resolved": "https://registry.npmjs.org/cosmiconfig/-/cosmiconfig-9.0.0.tgz",
			"integrity": "sha512-itvL5h8RETACmOTFc4UfIyB2RfEHi71Ax6E/PivVxq9NseKbOWpeyHEOIbmAw1rs8Ak0VursQNww7lf7YtUwzg==",
			"license": "MIT",
			"dependencies": {
				"env-paths": "^2.2.1",
				"import-fresh": "^3.3.0",
				"js-yaml": "^4.1.0",
				"parse-json": "^5.2.0"
			},
			"engines": {
				"node": ">=14"
			},
			"funding": {
				"url": "https://github.com/sponsors/d-fischer"
			},
			"peerDependencies": {
				"typescript": ">=4.9.5"
			},
			"peerDependenciesMeta": {
				"typescript": {
					"optional": true
				}
			}
		},
		"node_modules/cssesc": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/cssesc/-/cssesc-3.0.0.tgz",
			"integrity": "sha512-/Tb/JcjK111nNScGob5MNtsntNM1aCNUDipB/TkwZFhyDrrE47SOx/18wF2bbjgc3ZzCSKW1T5nt5EbFoAz/Vg==",
			"license": "MIT",
			"bin": {
				"cssesc": "bin/cssesc"
			},
			"engines": {
				"node": ">=4"
			}
		},
		"node_modules/csstype": {
			"version": "3.2.3",
			"resolved": "https://registry.npmjs.org/csstype/-/csstype-3.2.3.tgz",
			"integrity": "sha512-z1HGKcYy2xA8AGQfwrn0PAy+PB7X/GSj3UVJW9qKyn43xWa+gl5nXmU4qqLMRzWVLFC8KusUX8T/0kCiOYpAIQ==",
			"license": "MIT",
			"peer": true
		},
		"node_modules/data-uri-to-buffer": {
			"version": "6.0.2",
			"resolved": "https://registry.npmjs.org/data-uri-to-buffer/-/data-uri-to-buffer-6.0.2.tgz",
			"integrity": "sha512-7hvf7/GW8e86rW0ptuwS3OcBGDjIi6SZva7hCyWC0yYry2cOPmLIjXAUHI6DK2HsnwJd9ifmt57i8eV2n4YNpw==",
			"license": "MIT",
			"engines": {
				"node": ">= 14"
			}
		},
		"node_modules/data-view-buffer": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/data-view-buffer/-/data-view-buffer-1.0.2.tgz",
			"integrity": "sha512-EmKO5V3OLXh1rtK2wgXRansaK1/mtVdTUEiEI0W8RkvgT05kfxaH29PliLnpLP73yYO6142Q72QNa8Wx/A5CqQ==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3",
				"es-errors": "^1.3.0",
				"is-data-view": "^1.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/data-view-byte-length": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/data-view-byte-length/-/data-view-byte-length-1.0.2.tgz",
			"integrity": "sha512-tuhGbE6CfTM9+5ANGf+oQb72Ky/0+s3xKUpHvShfiz2RxMFgFPjsXuRLBVMtvMs15awe45SRb83D6wH4ew6wlQ==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3",
				"es-errors": "^1.3.0",
				"is-data-view": "^1.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/inspect-js"
			}
		},
		"node_modules/data-view-byte-offset": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/data-view-byte-offset/-/data-view-byte-offset-1.0.1.tgz",
			"integrity": "sha512-BS8PfmtDGnrgYdOonGZQdLZslWIeCGFP9tpan0hi1Co2Zr2NKADsvGYA8XxuG/4UWgJ6Cjtv+YJnB6MM69QGlQ==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.2",
				"es-errors": "^1.3.0",
				"is-data-view": "^1.0.1"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/debug": {
			"version": "4.4.3",
			"resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
			"integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
			"license": "MIT",
			"dependencies": {
				"ms": "^2.1.3"
			},
			"engines": {
				"node": ">=6.0"
			},
			"peerDependenciesMeta": {
				"supports-color": {
					"optional": true
				}
			}
		},
		"node_modules/decode-bmp": {
			"version": "0.2.1",
			"resolved": "https://registry.npmjs.org/decode-bmp/-/decode-bmp-0.2.1.tgz",
			"integrity": "sha512-NiOaGe+GN0KJqi2STf24hfMkFitDUaIoUU3eKvP/wAbLe8o6FuW5n/x7MHPR0HKvBokp6MQY/j7w8lewEeVCIA==",
			"license": "MIT",
			"dependencies": {
				"@canvas/image-data": "^1.0.0",
				"to-data-view": "^1.1.0"
			},
			"engines": {
				"node": ">=8.6.0"
			}
		},
		"node_modules/decode-ico": {
			"version": "0.4.1",
			"resolved": "https://registry.npmjs.org/decode-ico/-/decode-ico-0.4.1.tgz",
			"integrity": "sha512-69NZfbKIzux1vBOd31al3XnMnH+2mqDhEgLdpygErm4d60N+UwA5Sq5WFjmEDQzumgB9fElojGwWG0vybVfFmA==",
			"license": "MIT",
			"dependencies": {
				"@canvas/image-data": "^1.0.0",
				"decode-bmp": "^0.2.0",
				"to-data-view": "^1.1.0"
			},
			"engines": {
				"node": ">=8.6"
			}
		},
		"node_modules/decode-named-character-reference": {
			"version": "1.3.0",
			"resolved": "https://registry.npmjs.org/decode-named-character-reference/-/decode-named-character-reference-1.3.0.tgz",
			"integrity": "sha512-GtpQYB283KrPp6nRw50q3U9/VfOutZOe103qlN7BPP6Ad27xYnOIWv4lPzo8HCAL+mMZofJ9KEy30fq6MfaK6Q==",
			"license": "MIT",
			"dependencies": {
				"character-entities": "^2.0.0"
			},
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/decompress-response": {
			"version": "6.0.0",
			"resolved": "https://registry.npmjs.org/decompress-response/-/decompress-response-6.0.0.tgz",
			"integrity": "sha512-aW35yZM6Bb/4oJlZncMH2LCoZtJXTRxES17vE3hoRiowU2kWHaJKFkSBDnDR+cm9J+9QhXmREyIfv0pji9ejCQ==",
			"license": "MIT",
			"dependencies": {
				"mimic-response": "^3.1.0"
			},
			"engines": {
				"node": ">=10"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/decompress-response/node_modules/mimic-response": {
			"version": "3.1.0",
			"resolved": "https://registry.npmjs.org/mimic-response/-/mimic-response-3.1.0.tgz",
			"integrity": "sha512-z0yWI+4FDrrweS8Zmt4Ej5HdJmky15+L2e6Wgn3+iK5fWzb6T3fhNFq2+MeTRb064c6Wr4N/wv0DzQTjNzHNGQ==",
			"license": "MIT",
			"engines": {
				"node": ">=10"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/defer-to-connect": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/defer-to-connect/-/defer-to-connect-2.0.1.tgz",
			"integrity": "sha512-4tvttepXG1VaYGrRibk5EwJd1t4udunSOVMdLSAL6mId1ix438oPwPZMALY41FCijukO1L0twNcGsdzS7dHgDg==",
			"license": "MIT",
			"engines": {
				"node": ">=10"
			}
		},
		"node_modules/define-data-property": {
			"version": "1.1.4",
			"resolved": "https://registry.npmjs.org/define-data-property/-/define-data-property-1.1.4.tgz",
			"integrity": "sha512-rBMvIzlpA8v6E+SJZoo++HAYqsLrkg7MSfIinMPFhmkorw7X+dOXVJQs+QT69zGkzMyfDnIMN2Wid1+NbL3T+A==",
			"license": "MIT",
			"dependencies": {
				"es-define-property": "^1.0.0",
				"es-errors": "^1.3.0",
				"gopd": "^1.0.1"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/define-lazy-prop": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/define-lazy-prop/-/define-lazy-prop-2.0.0.tgz",
			"integrity": "sha512-Ds09qNh8yw3khSjiJjiUInaGX9xlqZDY7JVryGxdxV7NPeuqQfplOpQ66yJFZut3jLa5zOwkXw1g9EI2uKh4Og==",
			"license": "MIT",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/define-properties": {
			"version": "1.2.1",
			"resolved": "https://registry.npmjs.org/define-properties/-/define-properties-1.2.1.tgz",
			"integrity": "sha512-8QmQKqEASLd5nx0U1B1okLElbUuuttJ/AnYmRXbbbGDWh6uS208EjD4Xqq/I9wK7u0v6O08XhTWnt5XtEbR6Dg==",
			"license": "MIT",
			"dependencies": {
				"define-data-property": "^1.0.1",
				"has-property-descriptors": "^1.0.0",
				"object-keys": "^1.1.1"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/degenerator": {
			"version": "5.0.1",
			"resolved": "https://registry.npmjs.org/degenerator/-/degenerator-5.0.1.tgz",
			"integrity": "sha512-TllpMR/t0M5sqCXfj85i4XaAzxmS5tVA16dqvdkMwGmzI+dXLXnw3J+3Vdv7VKw+ThlTMboK6i9rnZ6Nntj5CQ==",
			"license": "MIT",
			"dependencies": {
				"ast-types": "^0.13.4",
				"escodegen": "^2.1.0",
				"esprima": "^4.0.1"
			},
			"engines": {
				"node": ">= 14"
			}
		},
		"node_modules/delayed-stream": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz",
			"integrity": "sha512-ZySD7Nf91aLB0RxL4KGrKHBXl7Eds1DAmEdcoVawXnLD7SDhpNgtuII2aAkg7a7QS41jxPSZ17p4VdGnMHk3MQ==",
			"license": "MIT",
			"engines": {
				"node": ">=0.4.0"
			}
		},
		"node_modules/depd": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/depd/-/depd-2.0.0.tgz",
			"integrity": "sha512-g7nH6P6dyDioJogAAGprGpCtVImJhpPk/roCzdb3fIh61/s/nPsfR6onyMwkCAR/OlC3yBC0lESvUoQEAssIrw==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/dependency-graph": {
			"version": "0.11.0",
			"resolved": "https://registry.npmjs.org/dependency-graph/-/dependency-graph-0.11.0.tgz",
			"integrity": "sha512-JeMq7fEshyepOWDfcfHK06N3MhyPhz++vtqWhMT5O9A3K42rdsEDpfdVqjaqaAhsw6a+ZqeDvQVtD0hFHQWrzg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.6.0"
			}
		},
		"node_modules/dequal": {
			"version": "2.0.3",
			"resolved": "https://registry.npmjs.org/dequal/-/dequal-2.0.3.tgz",
			"integrity": "sha512-0je+qPKHEMohvfRTCEo3CrPG6cAzAYgmzKyxRiYSSDkS6eGJdyVJm7WaYA5ECaAD9wLB2T4EEeymA5aFVcYXCA==",
			"license": "MIT",
			"engines": {
				"node": ">=6"
			}
		},
		"node_modules/destroy": {
			"version": "1.2.0",
			"resolved": "https://registry.npmjs.org/destroy/-/destroy-1.2.0.tgz",
			"integrity": "sha512-2sJGJTaXIIaR1w4iJSNoN0hnMY7Gpc/n8D4qSCJw8QqFWXf7cuAgnEHxBpweaVcPevC2l3KpjYCx3NypQQgaJg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.8",
				"npm": "1.2.8000 || >= 1.4.16"
			}
		},
		"node_modules/detect-libc": {
			"version": "2.1.2",
			"resolved": "https://registry.npmjs.org/detect-libc/-/detect-libc-2.1.2.tgz",
			"integrity": "sha512-Btj2BOOO83o3WyH59e8MgXsxEQVcarkUOpEYrubB0urwnN10yQ364rsiByU11nZlqWYZm05i/of7io4mzihBtQ==",
			"license": "Apache-2.0",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/detect-node-es": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/detect-node-es/-/detect-node-es-1.1.0.tgz",
			"integrity": "sha512-ypdmJU/TbBby2Dxibuv7ZLW3Bs1QEmM7nHjEANfohJLvE0XVujisn1qPJcZxg+qDucsr+bP6fLD1rPS3AhJ7EQ==",
			"license": "MIT",
			"peer": true
		},
		"node_modules/detect-port": {
			"version": "1.5.1",
			"resolved": "https://registry.npmjs.org/detect-port/-/detect-port-1.5.1.tgz",
			"integrity": "sha512-aBzdj76lueB6uUst5iAs7+0H/oOjqI5D16XUWxlWMIMROhcM0rfsNVk93zTngq1dDNpoXRr++Sus7ETAExppAQ==",
			"license": "MIT",
			"dependencies": {
				"address": "^1.0.1",
				"debug": "4"
			},
			"bin": {
				"detect": "bin/detect-port.js",
				"detect-port": "bin/detect-port.js"
			}
		},
		"node_modules/devlop": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/devlop/-/devlop-1.1.0.tgz",
			"integrity": "sha512-RWmIqhcFf1lRYBvNmr7qTNuyCt/7/ns2jbpp1+PalgE/rDQcBT0fioSMUpJ93irlUhC5hrg4cYqe6U+0ImW0rA==",
			"license": "MIT",
			"dependencies": {
				"dequal": "^2.0.0"
			},
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/devtools-protocol": {
			"version": "0.0.1312386",
			"resolved": "https://registry.npmjs.org/devtools-protocol/-/devtools-protocol-0.0.1312386.tgz",
			"integrity": "sha512-DPnhUXvmvKT2dFA/j7B+riVLUt9Q6RKJlcppojL5CoRywJJKLDYnRlw0gTFKfgDPHP5E04UoB71SxoJlVZy8FA==",
			"license": "BSD-3-Clause"
		},
		"node_modules/didyoumean": {
			"version": "1.2.2",
			"resolved": "https://registry.npmjs.org/didyoumean/-/didyoumean-1.2.2.tgz",
			"integrity": "sha512-gxtyfqMg7GKyhQmb056K7M3xszy/myH8w+B4RT+QXBQsvAOdc3XymqDDPHx1BgPgsdAA5SIifona89YtRATDzw==",
			"license": "Apache-2.0"
		},
		"node_modules/dlv": {
			"version": "1.1.3",
			"resolved": "https://registry.npmjs.org/dlv/-/dlv-1.1.3.tgz",
			"integrity": "sha512-+HlytyjlPKnIG8XuRG8WvmBP8xs8P71y+SKKS6ZXWoEgLuePxtDoUEiH7WkdePWrQ5JBpE6aoVqfZfJUQkjXwA==",
			"license": "MIT"
		},
		"node_modules/dns-packet": {
			"version": "5.6.1",
			"resolved": "https://registry.npmjs.org/dns-packet/-/dns-packet-5.6.1.tgz",
			"integrity": "sha512-l4gcSouhcgIKRvyy99RNVOgxXiicE+2jZoNmaNmZ6JXiGajBOJAesk1OBlJuM5k2c+eudGdLxDqXuPCKIj6kpw==",
			"license": "MIT",
			"dependencies": {
				"@leichtgewicht/ip-codec": "^2.0.1"
			},
			"engines": {
				"node": ">=6"
			}
		},
		"node_modules/dns-socket": {
			"version": "4.2.2",
			"resolved": "https://registry.npmjs.org/dns-socket/-/dns-socket-4.2.2.tgz",
			"integrity": "sha512-BDeBd8najI4/lS00HSKpdFia+OvUMytaVjfzR9n5Lq8MlZRSvtbI+uLtx1+XmQFls5wFU9dssccTmQQ6nfpjdg==",
			"license": "MIT",
			"dependencies": {
				"dns-packet": "^5.2.4"
			},
			"engines": {
				"node": ">=6"
			}
		},
		"node_modules/dunder-proto": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
			"integrity": "sha512-KIN/nDJBQRcXw0MLVhZE9iQHmG68qAVIBg9CqmUYjmQIhgij9U5MFvrqkUL5FbtyyzZuOeOt0zdeRe4UY7ct+A==",
			"license": "MIT",
			"dependencies": {
				"call-bind-apply-helpers": "^1.0.1",
				"es-errors": "^1.3.0",
				"gopd": "^1.2.0"
			},
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/ee-first": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
			"integrity": "sha512-WMwm9LhRUo+WUaRN+vRuETqG89IgZphVSNkdFgeb6sS/E4OrDIN7t48CAewSHXc6C8lefD8KKfr5vY61brQlow==",
			"license": "MIT"
		},
		"node_modules/emoji-regex": {
			"version": "10.6.0",
			"resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-10.6.0.tgz",
			"integrity": "sha512-toUI84YS5YmxW219erniWD0CIVOo46xGKColeNQRgOzDorgBi1v4D71/OFzgD9GO2UGKIv1C3Sp8DAn0+j5w7A==",
			"license": "MIT"
		},
		"node_modules/encodeurl": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-1.0.2.tgz",
			"integrity": "sha512-TPJXq8JqFaVYm2CWmPvnP2Iyo4ZSM7/QKcSmuMLDObfpH5fi7RUGmd/rTDf+rut/saiDiQEeVTNgAmJEdAOx0w==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/end-of-stream": {
			"version": "1.4.5",
			"resolved": "https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.5.tgz",
			"integrity": "sha512-ooEGc6HP26xXq/N+GCGOT0JKCLDGrq2bQUZrQ7gyrJiZANJ/8YDTxTpQBXGMn+WbIQXNVpyWymm7KYVICQnyOg==",
			"license": "MIT",
			"dependencies": {
				"once": "^1.4.0"
			}
		},
		"node_modules/engine.io": {
			"version": "6.5.5",
			"resolved": "https://registry.npmjs.org/engine.io/-/engine.io-6.5.5.tgz",
			"integrity": "sha512-C5Pn8Wk+1vKBoHghJODM63yk8MvrO9EWZUfkAt5HAqIgPE4/8FF0PEGHXtEd40l223+cE5ABWuPzm38PHFXfMA==",
			"license": "MIT",
			"dependencies": {
				"@types/cookie": "^0.4.1",
				"@types/cors": "^2.8.12",
				"@types/node": ">=10.0.0",
				"accepts": "~1.3.4",
				"base64id": "2.0.0",
				"cookie": "~0.4.1",
				"cors": "~2.8.5",
				"debug": "~4.3.1",
				"engine.io-parser": "~5.2.1",
				"ws": "~8.17.1"
			},
			"engines": {
				"node": ">=10.2.0"
			}
		},
		"node_modules/engine.io-parser": {
			"version": "5.2.3",
			"resolved": "https://registry.npmjs.org/engine.io-parser/-/engine.io-parser-5.2.3.tgz",
			"integrity": "sha512-HqD3yTBfnBxIrbnM1DoD6Pcq8NECnh8d4As1Qgh0z5Gg3jRRIqijury0CL3ghu/edArpUYiYqQiDUQBIs4np3Q==",
			"license": "MIT",
			"engines": {
				"node": ">=10.0.0"
			}
		},
		"node_modules/engine.io/node_modules/debug": {
			"version": "4.3.7",
			"resolved": "https://registry.npmjs.org/debug/-/debug-4.3.7.tgz",
			"integrity": "sha512-Er2nc/H7RrMXZBFCEim6TCmMk02Z8vLC2Rbi1KEBggpo0fS6l0S1nnapwmIi3yW/+GOJap1Krg4w0Hg80oCqgQ==",
			"license": "MIT",
			"dependencies": {
				"ms": "^2.1.3"
			},
			"engines": {
				"node": ">=6.0"
			},
			"peerDependenciesMeta": {
				"supports-color": {
					"optional": true
				}
			}
		},
		"node_modules/engine.io/node_modules/ws": {
			"version": "8.17.1",
			"resolved": "https://registry.npmjs.org/ws/-/ws-8.17.1.tgz",
			"integrity": "sha512-6XQFvXTkbfUOZOKKILFG1PDK2NDQs4azKQl26T0YS5CxqWLgXajbPZ+h4gZekJyRqFU8pvnbAbbs/3TgRPy+GQ==",
			"license": "MIT",
			"engines": {
				"node": ">=10.0.0"
			},
			"peerDependencies": {
				"bufferutil": "^4.0.1",
				"utf-8-validate": ">=5.0.2"
			},
			"peerDependenciesMeta": {
				"bufferutil": {
					"optional": true
				},
				"utf-8-validate": {
					"optional": true
				}
			}
		},
		"node_modules/entities": {
			"version": "6.0.1",
			"resolved": "https://registry.npmjs.org/entities/-/entities-6.0.1.tgz",
			"integrity": "sha512-aN97NXWF6AWBTahfVOIrB/NShkzi5H7F9r1s9mD3cDj4Ko5f2qhhVoYMibXF7GlLveb/D2ioWay8lxI97Ven3g==",
			"license": "BSD-2-Clause",
			"engines": {
				"node": ">=0.12"
			},
			"funding": {
				"url": "https://github.com/fb55/entities?sponsor=1"
			}
		},
		"node_modules/env-paths": {
			"version": "2.2.1",
			"resolved": "https://registry.npmjs.org/env-paths/-/env-paths-2.2.1.tgz",
			"integrity": "sha512-+h1lkLKhZMTYjog1VEpJNG7NZJWcuc2DDk/qsqSTRRCOXiLjeQ1d1/udrUGhqMxUgAlwKNZ0cf2uqan5GLuS2A==",
			"license": "MIT",
			"engines": {
				"node": ">=6"
			}
		},
		"node_modules/environment": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/environment/-/environment-1.1.0.tgz",
			"integrity": "sha512-xUtoPkMggbz0MPyPiIWr1Kp4aeWJjDZ6SMvURhimjdZgsRuDplF5/s9hcgGhyXMhs+6vpnuoiZ2kFiu3FMnS8Q==",
			"license": "MIT",
			"engines": {
				"node": ">=18"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/error-ex": {
			"version": "1.3.4",
			"resolved": "https://registry.npmjs.org/error-ex/-/error-ex-1.3.4.tgz",
			"integrity": "sha512-sqQamAnR14VgCr1A618A3sGrygcpK+HEbenA/HiEAkkUwcZIIB/tgWqHFxWgOyDh4nB4JCRimh79dR5Ywc9MDQ==",
			"license": "MIT",
			"dependencies": {
				"is-arrayish": "^0.2.1"
			}
		},
		"node_modules/es-abstract": {
			"version": "1.24.1",
			"resolved": "https://registry.npmjs.org/es-abstract/-/es-abstract-1.24.1.tgz",
			"integrity": "sha512-zHXBLhP+QehSSbsS9Pt23Gg964240DPd6QCf8WpkqEXxQ7fhdZzYsocOr5u7apWonsS5EjZDmTF+/slGMyasvw==",
			"license": "MIT",
			"dependencies": {
				"array-buffer-byte-length": "^1.0.2",
				"arraybuffer.prototype.slice": "^1.0.4",
				"available-typed-arrays": "^1.0.7",
				"call-bind": "^1.0.8",
				"call-bound": "^1.0.4",
				"data-view-buffer": "^1.0.2",
				"data-view-byte-length": "^1.0.2",
				"data-view-byte-offset": "^1.0.1",
				"es-define-property": "^1.0.1",
				"es-errors": "^1.3.0",
				"es-object-atoms": "^1.1.1",
				"es-set-tostringtag": "^2.1.0",
				"es-to-primitive": "^1.3.0",
				"function.prototype.name": "^1.1.8",
				"get-intrinsic": "^1.3.0",
				"get-proto": "^1.0.1",
				"get-symbol-description": "^1.1.0",
				"globalthis": "^1.0.4",
				"gopd": "^1.2.0",
				"has-property-descriptors": "^1.0.2",
				"has-proto": "^1.2.0",
				"has-symbols": "^1.1.0",
				"hasown": "^2.0.2",
				"internal-slot": "^1.1.0",
				"is-array-buffer": "^3.0.5",
				"is-callable": "^1.2.7",
				"is-data-view": "^1.0.2",
				"is-negative-zero": "^2.0.3",
				"is-regex": "^1.2.1",
				"is-set": "^2.0.3",
				"is-shared-array-buffer": "^1.0.4",
				"is-string": "^1.1.1",
				"is-typed-array": "^1.1.15",
				"is-weakref": "^1.1.1",
				"math-intrinsics": "^1.1.0",
				"object-inspect": "^1.13.4",
				"object-keys": "^1.1.1",
				"object.assign": "^4.1.7",
				"own-keys": "^1.0.1",
				"regexp.prototype.flags": "^1.5.4",
				"safe-array-concat": "^1.1.3",
				"safe-push-apply": "^1.0.0",
				"safe-regex-test": "^1.1.0",
				"set-proto": "^1.0.0",
				"stop-iteration-iterator": "^1.1.0",
				"string.prototype.trim": "^1.2.10",
				"string.prototype.trimend": "^1.0.9",
				"string.prototype.trimstart": "^1.0.8",
				"typed-array-buffer": "^1.0.3",
				"typed-array-byte-length": "^1.0.3",
				"typed-array-byte-offset": "^1.0.4",
				"typed-array-length": "^1.0.7",
				"unbox-primitive": "^1.1.0",
				"which-typed-array": "^1.1.19"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/es-aggregate-error": {
			"version": "1.0.14",
			"resolved": "https://registry.npmjs.org/es-aggregate-error/-/es-aggregate-error-1.0.14.tgz",
			"integrity": "sha512-3YxX6rVb07B5TV11AV5wsL7nQCHXNwoHPsQC8S4AmBiqYhyNCJ5BRKXkXyDJvs8QzXN20NgRtxe3dEEQD9NLHA==",
			"license": "MIT",
			"dependencies": {
				"define-data-property": "^1.1.4",
				"define-properties": "^1.2.1",
				"es-abstract": "^1.24.0",
				"es-errors": "^1.3.0",
				"function-bind": "^1.1.2",
				"globalthis": "^1.0.4",
				"has-property-descriptors": "^1.0.2",
				"set-function-name": "^2.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/es-define-property": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz",
			"integrity": "sha512-e3nRfgfUZ4rNGL232gUgX06QNyyez04KdjFrF+LTRoOXmrOgFKDg4BCdsjW8EnT69eqdYGmRpJwiPVYNrCaW3g==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/es-errors": {
			"version": "1.3.0",
			"resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
			"integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/es-object-atoms": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.1.tgz",
			"integrity": "sha512-FGgH2h8zKNim9ljj7dankFPcICIK9Cp5bm+c2gQSYePhpaG5+esrLODihIorn+Pe6FGJzWhXQotPv73jTaldXA==",
			"license": "MIT",
			"dependencies": {
				"es-errors": "^1.3.0"
			},
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/es-set-tostringtag": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/es-set-tostringtag/-/es-set-tostringtag-2.1.0.tgz",
			"integrity": "sha512-j6vWzfrGVfyXxge+O0x5sh6cvxAog0a/4Rdd2K36zCMV5eJ+/+tOAngRO8cODMNWbVRdVlmGZQL2YS3yR8bIUA==",
			"license": "MIT",
			"dependencies": {
				"es-errors": "^1.3.0",
				"get-intrinsic": "^1.2.6",
				"has-tostringtag": "^1.0.2",
				"hasown": "^2.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/es-to-primitive": {
			"version": "1.3.0",
			"resolved": "https://registry.npmjs.org/es-to-primitive/-/es-to-primitive-1.3.0.tgz",
			"integrity": "sha512-w+5mJ3GuFL+NjVtJlvydShqE1eN3h3PbI7/5LAsYJP/2qtuMXjfL2LpHSRqo4b4eSF5K/DH1JXKUAHSB2UW50g==",
			"license": "MIT",
			"dependencies": {
				"is-callable": "^1.2.7",
				"is-date-object": "^1.0.5",
				"is-symbol": "^1.0.4"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/es-toolkit": {
			"version": "1.44.0",
			"resolved": "https://registry.npmjs.org/es-toolkit/-/es-toolkit-1.44.0.tgz",
			"integrity": "sha512-6penXeZalaV88MM3cGkFZZfOoLGWshWWfdy0tWw/RlVVyhvMaWSBTOvXNeiW3e5FwdS5ePW0LGEu17zT139ktg==",
			"license": "MIT",
			"workspaces": [
				"docs",
				"benchmarks"
			]
		},
		"node_modules/esast-util-from-estree": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/esast-util-from-estree/-/esast-util-from-estree-2.0.0.tgz",
			"integrity": "sha512-4CyanoAudUSBAn5K13H4JhsMH6L9ZP7XbLVe/dKybkxMO7eDyLsT8UHl9TRNrU2Gr9nz+FovfSIjuXWJ81uVwQ==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"devlop": "^1.0.0",
				"estree-util-visit": "^2.0.0",
				"unist-util-position-from-estree": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/esast-util-from-js": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/esast-util-from-js/-/esast-util-from-js-2.0.1.tgz",
			"integrity": "sha512-8Ja+rNJ0Lt56Pcf3TAmpBZjmx8ZcK5Ts4cAzIOjsjevg9oSXJnl6SUQ2EevU8tv3h6ZLWmoKL5H4fgWvdvfETw==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"acorn": "^8.0.0",
				"esast-util-from-estree": "^2.0.0",
				"vfile-message": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/escalade": {
			"version": "3.2.0",
			"resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
			"integrity": "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==",
			"license": "MIT",
			"engines": {
				"node": ">=6"
			}
		},
		"node_modules/escape-html": {
			"version": "1.0.3",
			"resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz",
			"integrity": "sha512-NiSupZ4OeuGwr68lGIeym/ksIZMJodUGOSCZ/FSnTxcrekbvqrgdUxlJOMpijaKZVjAJrWrGs/6Jy8OMuyj9ow==",
			"license": "MIT"
		},
		"node_modules/escape-string-regexp": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-5.0.0.tgz",
			"integrity": "sha512-/veY75JbMK4j1yjvuUxuVsiS/hr/4iHs9FTT6cgTexxdE0Ly/glccBAkloH/DofkjRbZU3bnoj38mOmhkZ0lHw==",
			"license": "MIT",
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/escodegen": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/escodegen/-/escodegen-2.1.0.tgz",
			"integrity": "sha512-2NlIDTwUWJN0mRPQOdtQBzbUHvdGY2P1VXSyU83Q3xKxM7WHX2Ql8dKq782Q9TgQUNOLEzEYu9bzLNj1q88I5w==",
			"license": "BSD-2-Clause",
			"dependencies": {
				"esprima": "^4.0.1",
				"estraverse": "^5.2.0",
				"esutils": "^2.0.2"
			},
			"bin": {
				"escodegen": "bin/escodegen.js",
				"esgenerate": "bin/esgenerate.js"
			},
			"engines": {
				"node": ">=6.0"
			},
			"optionalDependencies": {
				"source-map": "~0.6.1"
			}
		},
		"node_modules/escodegen/node_modules/source-map": {
			"version": "0.6.1",
			"resolved": "https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz",
			"integrity": "sha512-UjgapumWlbMhkBgzT7Ykc5YXUT46F0iKu8SGXq0bcwP5dz/h0Plj6enJqjz1Zbq2l5WaqYnrVbwWOWMyF3F47g==",
			"license": "BSD-3-Clause",
			"optional": true,
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/esprima": {
			"version": "4.0.1",
			"resolved": "https://registry.npmjs.org/esprima/-/esprima-4.0.1.tgz",
			"integrity": "sha512-eGuFFw7Upda+g4p+QHvnW0RyTX/SVeJBDM/gCtMARO0cLuT2HcEKnTPvhjV6aGeqrCB/sbNop0Kszm0jsaWU4A==",
			"license": "BSD-2-Clause",
			"bin": {
				"esparse": "bin/esparse.js",
				"esvalidate": "bin/esvalidate.js"
			},
			"engines": {
				"node": ">=4"
			}
		},
		"node_modules/estraverse": {
			"version": "5.3.0",
			"resolved": "https://registry.npmjs.org/estraverse/-/estraverse-5.3.0.tgz",
			"integrity": "sha512-MMdARuVEQziNTeJD8DgMqmhwR11BRQ/cBP+pLtYdSTnf3MIO8fFeiINEbX36ZdNlfU/7A9f3gUw49B3oQsvwBA==",
			"license": "BSD-2-Clause",
			"engines": {
				"node": ">=4.0"
			}
		},
		"node_modules/estree-util-attach-comments": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/estree-util-attach-comments/-/estree-util-attach-comments-3.0.0.tgz",
			"integrity": "sha512-cKUwm/HUcTDsYh/9FgnuFqpfquUbwIqwKM26BVCGDPVgvaCl/nDCCjUfiLlx6lsEZ3Z4RFxNbOQ60pkaEwFxGw==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/estree-util-build-jsx": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/estree-util-build-jsx/-/estree-util-build-jsx-3.0.1.tgz",
			"integrity": "sha512-8U5eiL6BTrPxp/CHbs2yMgP8ftMhR5ww1eIKoWRMlqvltHF8fZn5LRDvTKuxD3DUn+shRbLGqXemcP51oFCsGQ==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"devlop": "^1.0.0",
				"estree-util-is-identifier-name": "^3.0.0",
				"estree-walker": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/estree-util-is-identifier-name": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/estree-util-is-identifier-name/-/estree-util-is-identifier-name-3.0.0.tgz",
			"integrity": "sha512-hFtqIDZTIUZ9BXLb8y4pYGyk6+wekIivNVTcmvk8NoOh+VeRn5y6cEHzbURrWbfp1fIqdVipilzj+lfaadNZmg==",
			"license": "MIT",
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/estree-util-scope": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/estree-util-scope/-/estree-util-scope-1.0.0.tgz",
			"integrity": "sha512-2CAASclonf+JFWBNJPndcOpA8EMJwa0Q8LUFJEKqXLW6+qBvbFZuF5gItbQOs/umBUkjviCSDCbBwU2cXbmrhQ==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0",
				"devlop": "^1.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/estree-util-to-js": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/estree-util-to-js/-/estree-util-to-js-2.0.0.tgz",
			"integrity": "sha512-WDF+xj5rRWmD5tj6bIqRi6CkLIXbbNQUcxQHzGysQzvHmdYG2G7p/Tf0J0gpxGgkeMZNTIjT/AoSvC9Xehcgdg==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"astring": "^1.8.0",
				"source-map": "^0.7.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/estree-util-visit": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/estree-util-visit/-/estree-util-visit-2.0.0.tgz",
			"integrity": "sha512-m5KgiH85xAhhW8Wta0vShLcUvOsh3LLPI2YVwcbio1l7E09NTLL1EyMZFM1OyWowoH0skScNbhOPl4kcBgzTww==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"@types/unist": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/estree-walker": {
			"version": "3.0.3",
			"resolved": "https://registry.npmjs.org/estree-walker/-/estree-walker-3.0.3.tgz",
			"integrity": "sha512-7RUKfXgSMMkzt6ZuXmqapOurLGPPfgj6l9uRZ7lRGolvk0y2yocc35LdcxKC5PQZdn2DMqioAQ2NoWcrTKmm6g==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0"
			}
		},
		"node_modules/esutils": {
			"version": "2.0.3",
			"resolved": "https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz",
			"integrity": "sha512-kVscqXk4OCp68SZ0dkgEKVi6/8ij300KBWTJq32P/dYeWTSwK41WyTxalN1eRmA5Z9UU/LX9D7FWSmV9SAYx6g==",
			"license": "BSD-2-Clause",
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/etag": {
			"version": "1.8.1",
			"resolved": "https://registry.npmjs.org/etag/-/etag-1.8.1.tgz",
			"integrity": "sha512-aIL5Fx7mawVa300al2BnEE4iNvo1qETxLrPI/o05L7z6go7fCw1J6EQmbK4FmJ2AS7kgVF/KEZWufBfdClMcPg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/event-target-shim": {
			"version": "5.0.1",
			"resolved": "https://registry.npmjs.org/event-target-shim/-/event-target-shim-5.0.1.tgz",
			"integrity": "sha512-i/2XbnSz/uxRCU6+NdVJgKWDTM427+MqYbkQzD321DuCQJUqOuJKIA0IM2+W2xtYHdKOmZ4dR6fExsd4SXL+WQ==",
			"license": "MIT",
			"engines": {
				"node": ">=6"
			}
		},
		"node_modules/events-universal": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/events-universal/-/events-universal-1.0.1.tgz",
			"integrity": "sha512-LUd5euvbMLpwOF8m6ivPCbhQeSiYVNb8Vs0fQ8QjXo0JTkEHpz8pxdQf0gStltaPpw0Cca8b39KxvK9cfKRiAw==",
			"license": "Apache-2.0",
			"dependencies": {
				"bare-events": "^2.7.0"
			}
		},
		"node_modules/express": {
			"version": "4.20.0",
			"resolved": "https://registry.npmjs.org/express/-/express-4.20.0.tgz",
			"integrity": "sha512-pLdae7I6QqShF5PnNTCVn4hI91Dx0Grkn2+IAsMTgMIKuQVte2dN9PeGSSAME2FR8anOhVA62QDIUaWVfEXVLw==",
			"license": "MIT",
			"dependencies": {
				"accepts": "~1.3.8",
				"array-flatten": "1.1.1",
				"body-parser": "1.20.3",
				"content-disposition": "0.5.4",
				"content-type": "~1.0.4",
				"cookie": "0.6.0",
				"cookie-signature": "1.0.6",
				"debug": "2.6.9",
				"depd": "2.0.0",
				"encodeurl": "~2.0.0",
				"escape-html": "~1.0.3",
				"etag": "~1.8.1",
				"finalhandler": "1.2.0",
				"fresh": "0.5.2",
				"http-errors": "2.0.0",
				"merge-descriptors": "1.0.3",
				"methods": "~1.1.2",
				"on-finished": "2.4.1",
				"parseurl": "~1.3.3",
				"path-to-regexp": "0.1.10",
				"proxy-addr": "~2.0.7",
				"qs": "6.11.0",
				"range-parser": "~1.2.1",
				"safe-buffer": "5.2.1",
				"send": "0.19.0",
				"serve-static": "1.16.0",
				"setprototypeof": "1.2.0",
				"statuses": "2.0.1",
				"type-is": "~1.6.18",
				"utils-merge": "1.0.1",
				"vary": "~1.1.2"
			},
			"engines": {
				"node": ">= 0.10.0"
			}
		},
		"node_modules/express/node_modules/debug": {
			"version": "2.6.9",
			"resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
			"integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
			"license": "MIT",
			"dependencies": {
				"ms": "2.0.0"
			}
		},
		"node_modules/express/node_modules/encodeurl": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-2.0.0.tgz",
			"integrity": "sha512-Q0n9HRi4m6JuGIV1eFlmvJB7ZEVxu93IrMyiMsGC0lrMJMWzRgx6WGquyfQgZVb31vhGgXnfmPNNXmxnOkRBrg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/express/node_modules/ms": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
			"integrity": "sha512-Tpp60P6IUJDTuOq/5Z8cdskzJujfwqfOTkrwIwj7IRISpnkJnT6SyJ4PCPnGMoFjC9ddhal5KVIYtAt97ix05A==",
			"license": "MIT"
		},
		"node_modules/extend": {
			"version": "3.0.2",
			"resolved": "https://registry.npmjs.org/extend/-/extend-3.0.2.tgz",
			"integrity": "sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g==",
			"license": "MIT"
		},
		"node_modules/extract-zip": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/extract-zip/-/extract-zip-2.0.1.tgz",
			"integrity": "sha512-GDhU9ntwuKyGXdZBUgTIe+vXnWj0fppUEtMDL0+idd5Sta8TGpHssn/eusA9mrPr9qNDym6SxAYZjNvCn/9RBg==",
			"license": "BSD-2-Clause",
			"dependencies": {
				"debug": "^4.1.1",
				"get-stream": "^5.1.0",
				"yauzl": "^2.10.0"
			},
			"bin": {
				"extract-zip": "cli.js"
			},
			"engines": {
				"node": ">= 10.17.0"
			},
			"optionalDependencies": {
				"@types/yauzl": "^2.9.1"
			}
		},
		"node_modules/extract-zip/node_modules/get-stream": {
			"version": "5.2.0",
			"resolved": "https://registry.npmjs.org/get-stream/-/get-stream-5.2.0.tgz",
			"integrity": "sha512-nBF+F1rAZVCu/p7rjzgA+Yb4lfYXrpl7a6VmJrU8wF9I1CKvP/QwPNZHnOlwbTkY6dvtFIzFMSyQXbLoTQPRpA==",
			"license": "MIT",
			"dependencies": {
				"pump": "^3.0.0"
			},
			"engines": {
				"node": ">=8"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/fast-deep-equal": {
			"version": "3.1.3",
			"resolved": "https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz",
			"integrity": "sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==",
			"license": "MIT"
		},
		"node_modules/fast-fifo": {
			"version": "1.3.2",
			"resolved": "https://registry.npmjs.org/fast-fifo/-/fast-fifo-1.3.2.tgz",
			"integrity": "sha512-/d9sfos4yxzpwkDkuN7k2SqFKtYNmCTzgfEpz82x34IM9/zc8KGxQoXg1liNC/izpRM/MBdt44Nmx41ZWqk+FQ==",
			"license": "MIT"
		},
		"node_modules/fast-glob": {
			"version": "3.3.3",
			"resolved": "https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.3.tgz",
			"integrity": "sha512-7MptL8U0cqcFdzIzwOTHoilX9x5BrNqye7Z/LuC7kCMRio1EMSyqRK3BEAUD7sXRq4iT4AzTVuZdhgQ2TCvYLg==",
			"license": "MIT",
			"dependencies": {
				"@nodelib/fs.stat": "^2.0.2",
				"@nodelib/fs.walk": "^1.2.3",
				"glob-parent": "^5.1.2",
				"merge2": "^1.3.0",
				"micromatch": "^4.0.8"
			},
			"engines": {
				"node": ">=8.6.0"
			}
		},
		"node_modules/fast-memoize": {
			"version": "2.5.2",
			"resolved": "https://registry.npmjs.org/fast-memoize/-/fast-memoize-2.5.2.tgz",
			"integrity": "sha512-Ue0LwpDYErFbmNnZSF0UH6eImUwDmogUO1jyE+JbN2gsQz/jICm1Ve7t9QT0rNSsfJt+Hs4/S3GnsDVjL4HVrw==",
			"license": "MIT"
		},
		"node_modules/fast-uri": {
			"version": "3.1.0",
			"resolved": "https://registry.npmjs.org/fast-uri/-/fast-uri-3.1.0.tgz",
			"integrity": "sha512-iPeeDKJSWf4IEOasVVrknXpaBV0IApz/gp7S2bb7Z4Lljbl2MGJRqInZiUrQwV16cpzw/D3S5j5Julj/gT52AA==",
			"funding": [
				{
					"type": "github",
					"url": "https://github.com/sponsors/fastify"
				},
				{
					"type": "opencollective",
					"url": "https://opencollective.com/fastify"
				}
			],
			"license": "BSD-3-Clause"
		},
		"node_modules/fastq": {
			"version": "1.20.1",
			"resolved": "https://registry.npmjs.org/fastq/-/fastq-1.20.1.tgz",
			"integrity": "sha512-GGToxJ/w1x32s/D2EKND7kTil4n8OVk/9mycTc4VDza13lOvpUZTGX3mFSCtV9ksdGBVzvsyAVLM6mHFThxXxw==",
			"license": "ISC",
			"dependencies": {
				"reusify": "^1.0.4"
			}
		},
		"node_modules/fault": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/fault/-/fault-2.0.1.tgz",
			"integrity": "sha512-WtySTkS4OKev5JtpHXnib4Gxiurzh5NCGvWrFaZ34m6JehfTUhKZvn9njTfw48t6JumVQOmrKqpmGcdwxnhqBQ==",
			"license": "MIT",
			"dependencies": {
				"format": "^0.2.0"
			},
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/favicons": {
			"version": "7.2.0",
			"resolved": "https://registry.npmjs.org/favicons/-/favicons-7.2.0.tgz",
			"integrity": "sha512-k/2rVBRIRzOeom3wI9jBPaSEvoTSQEW4iM0EveBmBBKFxO8mSyyRWtDlfC3VnEfu0avmjrMzy8/ZFPSe6F71Hw==",
			"license": "MIT",
			"dependencies": {
				"escape-html": "^1.0.3",
				"sharp": "^0.33.1",
				"xml2js": "^0.6.1"
			},
			"engines": {
				"node": ">=14.0.0"
			}
		},
		"node_modules/fd-slicer": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/fd-slicer/-/fd-slicer-1.1.0.tgz",
			"integrity": "sha512-cE1qsB/VwyQozZ+q1dGxR8LBYNZeofhEdUNGSMbQD3Gw2lAzX9Zb3uIU6Ebc/Fmyjo9AWWfnn0AUCHqtevs/8g==",
			"license": "MIT",
			"dependencies": {
				"pend": "~1.2.0"
			}
		},
		"node_modules/fill-range": {
			"version": "7.1.1",
			"resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
			"integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
			"license": "MIT",
			"dependencies": {
				"to-regex-range": "^5.0.1"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/finalhandler": {
			"version": "1.2.0",
			"resolved": "https://registry.npmjs.org/finalhandler/-/finalhandler-1.2.0.tgz",
			"integrity": "sha512-5uXcUVftlQMFnWC9qu/svkWv3GTd2PfUhK/3PLkYNAe7FbqJMt3515HaxE6eRL74GdsriiwujiawdaB1BpEISg==",
			"license": "MIT",
			"dependencies": {
				"debug": "2.6.9",
				"encodeurl": "~1.0.2",
				"escape-html": "~1.0.3",
				"on-finished": "2.4.1",
				"parseurl": "~1.3.3",
				"statuses": "2.0.1",
				"unpipe": "~1.0.0"
			},
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/finalhandler/node_modules/debug": {
			"version": "2.6.9",
			"resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
			"integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
			"license": "MIT",
			"dependencies": {
				"ms": "2.0.0"
			}
		},
		"node_modules/finalhandler/node_modules/ms": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
			"integrity": "sha512-Tpp60P6IUJDTuOq/5Z8cdskzJujfwqfOTkrwIwj7IRISpnkJnT6SyJ4PCPnGMoFjC9ddhal5KVIYtAt97ix05A==",
			"license": "MIT"
		},
		"node_modules/follow-redirects": {
			"version": "1.15.11",
			"resolved": "https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.15.11.tgz",
			"integrity": "sha512-deG2P0JfjrTxl50XGCDyfI97ZGVCxIpfKYmfyrQ54n5FO/0gfIES8C/Psl6kWVDolizcaaxZJnTS0QSMxvnsBQ==",
			"funding": [
				{
					"type": "individual",
					"url": "https://github.com/sponsors/RubenVerborgh"
				}
			],
			"license": "MIT",
			"engines": {
				"node": ">=4.0"
			},
			"peerDependenciesMeta": {
				"debug": {
					"optional": true
				}
			}
		},
		"node_modules/for-each": {
			"version": "0.3.5",
			"resolved": "https://registry.npmjs.org/for-each/-/for-each-0.3.5.tgz",
			"integrity": "sha512-dKx12eRCVIzqCxFGplyFKJMPvLEWgmNtUrpTiJIR5u97zEhRG8ySrtboPHZXx7daLxQVrl643cTzbab2tkQjxg==",
			"license": "MIT",
			"dependencies": {
				"is-callable": "^1.2.7"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/form-data": {
			"version": "4.0.5",
			"resolved": "https://registry.npmjs.org/form-data/-/form-data-4.0.5.tgz",
			"integrity": "sha512-8RipRLol37bNs2bhoV67fiTEvdTrbMUYcFTiy3+wuuOnUog2QBHCZWXDRijWQfAkhBj2Uf5UnVaiWwA5vdd82w==",
			"license": "MIT",
			"dependencies": {
				"asynckit": "^0.4.0",
				"combined-stream": "^1.0.8",
				"es-set-tostringtag": "^2.1.0",
				"hasown": "^2.0.2",
				"mime-types": "^2.1.12"
			},
			"engines": {
				"node": ">= 6"
			}
		},
		"node_modules/form-data-encoder": {
			"version": "2.1.4",
			"resolved": "https://registry.npmjs.org/form-data-encoder/-/form-data-encoder-2.1.4.tgz",
			"integrity": "sha512-yDYSgNMraqvnxiEXO4hi88+YZxaHC6QKzb5N84iRCTDeRO7ZALpir/lVmf/uXUhnwUr2O4HU8s/n6x+yNjQkHw==",
			"license": "MIT",
			"engines": {
				"node": ">= 14.17"
			}
		},
		"node_modules/format": {
			"version": "0.2.2",
			"resolved": "https://registry.npmjs.org/format/-/format-0.2.2.tgz",
			"integrity": "sha512-wzsgA6WOq+09wrU1tsJ09udeR/YZRaeArL9e1wPbFg3GG2yDnC2ldKpxs4xunpFF9DgqCqOIra3bc1HWrJ37Ww==",
			"engines": {
				"node": ">=0.4.x"
			}
		},
		"node_modules/forwarded": {
			"version": "0.2.0",
			"resolved": "https://registry.npmjs.org/forwarded/-/forwarded-0.2.0.tgz",
			"integrity": "sha512-buRG0fpBtRHSTCOASe6hD258tEubFoRLb4ZNA6NxMVHNw2gOcwHo9wyablzMzOA5z9xA9L1KNjk/Nt6MT9aYow==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/fresh": {
			"version": "0.5.2",
			"resolved": "https://registry.npmjs.org/fresh/-/fresh-0.5.2.tgz",
			"integrity": "sha512-zJ2mQYM18rEFOudeV4GShTGIQ7RbzA7ozbU9I/XBpm7kqgMywgmylMwXHxZJmkVoYkna9d2pVXVXPdYTP9ej8Q==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/front-matter": {
			"version": "4.0.2",
			"resolved": "https://registry.npmjs.org/front-matter/-/front-matter-4.0.2.tgz",
			"integrity": "sha512-I8ZuJ/qG92NWX8i5x1Y8qyj3vizhXS31OxjKDu3LKP+7/qBgfIKValiZIEwoVoJKUHlhWtYrktkxV1XsX+pPlg==",
			"license": "MIT",
			"dependencies": {
				"js-yaml": "^3.13.1"
			}
		},
		"node_modules/fs-extra": {
			"version": "11.2.0",
			"resolved": "https://registry.npmjs.org/fs-extra/-/fs-extra-11.2.0.tgz",
			"integrity": "sha512-PmDi3uwK5nFuXh7XDTlVnS17xJS7vW36is2+w3xcv8SVxiB4NyATf4ctkVY5bkSjX0Y4nbvZCq1/EjtEyr9ktw==",
			"license": "MIT",
			"dependencies": {
				"graceful-fs": "^4.2.0",
				"jsonfile": "^6.0.1",
				"universalify": "^2.0.0"
			},
			"engines": {
				"node": ">=14.14"
			}
		},
		"node_modules/fs-minipass": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/fs-minipass/-/fs-minipass-2.1.0.tgz",
			"integrity": "sha512-V/JgOLFCS+R6Vcq0slCuaeWEdNC3ouDlJMNIsacH2VtALiu9mV4LPrHc5cDl8k5aw6J8jwgWWpiTo5RYhmIzvg==",
			"license": "ISC",
			"dependencies": {
				"minipass": "^3.0.0"
			},
			"engines": {
				"node": ">= 8"
			}
		},
		"node_modules/fs-minipass/node_modules/minipass": {
			"version": "3.3.6",
			"resolved": "https://registry.npmjs.org/minipass/-/minipass-3.3.6.tgz",
			"integrity": "sha512-DxiNidxSEK+tHG6zOIklvNOwm3hvCrbUrdtzY74U6HKTJxvIDfOUL5W5P2Ghd3DTkhhKPYGqeNUIh5qcM4YBfw==",
			"license": "ISC",
			"dependencies": {
				"yallist": "^4.0.0"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/fsevents": {
			"version": "2.3.3",
			"resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
			"integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
			"hasInstallScript": true,
			"license": "MIT",
			"optional": true,
			"os": [
				"darwin"
			],
			"engines": {
				"node": "^8.16.0 || ^10.6.0 || >=11.0.0"
			}
		},
		"node_modules/function-bind": {
			"version": "1.1.2",
			"resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
			"integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
			"license": "MIT",
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/function.prototype.name": {
			"version": "1.1.8",
			"resolved": "https://registry.npmjs.org/function.prototype.name/-/function.prototype.name-1.1.8.tgz",
			"integrity": "sha512-e5iwyodOHhbMr/yNrc7fDYG4qlbIvI5gajyzPnb5TCwyhjApznQh1BMFou9b30SevY43gCJKXycoCBjMbsuW0Q==",
			"license": "MIT",
			"dependencies": {
				"call-bind": "^1.0.8",
				"call-bound": "^1.0.3",
				"define-properties": "^1.2.1",
				"functions-have-names": "^1.2.3",
				"hasown": "^2.0.2",
				"is-callable": "^1.2.7"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/functions-have-names": {
			"version": "1.2.3",
			"resolved": "https://registry.npmjs.org/functions-have-names/-/functions-have-names-1.2.3.tgz",
			"integrity": "sha512-xckBUXyTIqT97tq2x2AMb+g163b5JFysYk0x4qxNFwbfQkmNZoiRHb6sPzI9/QV33WeuvVYBUIiD4NzNIyqaRQ==",
			"license": "MIT",
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/gcd": {
			"version": "0.0.1",
			"resolved": "https://registry.npmjs.org/gcd/-/gcd-0.0.1.tgz",
			"integrity": "sha512-VNx3UEGr+ILJTiMs1+xc5SX1cMgJCrXezKPa003APUWNqQqaF6n25W8VcR7nHN6yRWbvvUTwCpZCFJeWC2kXlw==",
			"license": "MIT"
		},
		"node_modules/generator-function": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/generator-function/-/generator-function-2.0.1.tgz",
			"integrity": "sha512-SFdFmIJi+ybC0vjlHN0ZGVGHc3lgE0DxPAT0djjVg+kjOnSqclqmj0KQ7ykTOLP6YxoqOvuAODGdcHJn+43q3g==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/get-caller-file": {
			"version": "2.0.5",
			"resolved": "https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz",
			"integrity": "sha512-DyFP3BM/3YHTQOCUL/w0OZHR0lpKeGrxotcHWcqNEdnltqFwXVfhEBQ94eIo34AfQpo0rGki4cyIiftY06h2Fg==",
			"license": "ISC",
			"engines": {
				"node": "6.* || 8.* || >= 10.*"
			}
		},
		"node_modules/get-east-asian-width": {
			"version": "1.4.0",
			"resolved": "https://registry.npmjs.org/get-east-asian-width/-/get-east-asian-width-1.4.0.tgz",
			"integrity": "sha512-QZjmEOC+IT1uk6Rx0sX22V6uHWVwbdbxf1faPqJ1QhLdGgsRGCZoyaQBm/piRdJy/D2um6hM1UP7ZEeQ4EkP+Q==",
			"license": "MIT",
			"engines": {
				"node": ">=18"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/get-intrinsic": {
			"version": "1.3.0",
			"resolved": "https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz",
			"integrity": "sha512-9fSjSaos/fRIVIp+xSJlE6lfwhES7LNtKaCBIamHsjr2na1BiABJPo0mOjjz8GJDURarmCPGqaiVg5mfjb98CQ==",
			"license": "MIT",
			"dependencies": {
				"call-bind-apply-helpers": "^1.0.2",
				"es-define-property": "^1.0.1",
				"es-errors": "^1.3.0",
				"es-object-atoms": "^1.1.1",
				"function-bind": "^1.1.2",
				"get-proto": "^1.0.1",
				"gopd": "^1.2.0",
				"has-symbols": "^1.1.0",
				"hasown": "^2.0.2",
				"math-intrinsics": "^1.1.0"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/get-nonce": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/get-nonce/-/get-nonce-1.0.1.tgz",
			"integrity": "sha512-FJhYRoDaiatfEkUK8HKlicmu/3SGFD51q3itKDGoSTysQJBnfOcxU5GxnhE1E6soB76MbT0MBtnKJuXyAx+96Q==",
			"license": "MIT",
			"peer": true,
			"engines": {
				"node": ">=6"
			}
		},
		"node_modules/get-proto": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz",
			"integrity": "sha512-sTSfBjoXBp89JvIKIefqw7U2CCebsc74kiY6awiGogKtoSGbgjYE/G/+l9sF3MWFPNc9IcoOC4ODfKHfxFmp0g==",
			"license": "MIT",
			"dependencies": {
				"dunder-proto": "^1.0.1",
				"es-object-atoms": "^1.0.0"
			},
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/get-stream": {
			"version": "6.0.1",
			"resolved": "https://registry.npmjs.org/get-stream/-/get-stream-6.0.1.tgz",
			"integrity": "sha512-ts6Wi+2j3jQjqi70w5AlN8DFnkSwC+MqmxEzdEALB2qXZYV3X/b1CTfgPLGJNMeAWxdPfU8FO1ms3NUfaHCPYg==",
			"license": "MIT",
			"engines": {
				"node": ">=10"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/get-symbol-description": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/get-symbol-description/-/get-symbol-description-1.1.0.tgz",
			"integrity": "sha512-w9UMqWwJxHNOvoNzSJ2oPF5wvYcvP7jUvYzhp67yEhTi17ZDBBC1z9pTdGuzjD+EFIqLSYRweZjqfiPzQ06Ebg==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3",
				"es-errors": "^1.3.0",
				"get-intrinsic": "^1.2.6"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/get-uri": {
			"version": "6.0.5",
			"resolved": "https://registry.npmjs.org/get-uri/-/get-uri-6.0.5.tgz",
			"integrity": "sha512-b1O07XYq8eRuVzBNgJLstU6FYc1tS6wnMtF1I1D9lE8LxZSOGZ7LhxN54yPP6mGw5f2CkXY2BQUL9Fx41qvcIg==",
			"license": "MIT",
			"dependencies": {
				"basic-ftp": "^5.0.2",
				"data-uri-to-buffer": "^6.0.2",
				"debug": "^4.3.4"
			},
			"engines": {
				"node": ">= 14"
			}
		},
		"node_modules/glob-parent": {
			"version": "5.1.2",
			"resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
			"integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
			"license": "ISC",
			"dependencies": {
				"is-glob": "^4.0.1"
			},
			"engines": {
				"node": ">= 6"
			}
		},
		"node_modules/globalthis": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/globalthis/-/globalthis-1.0.4.tgz",
			"integrity": "sha512-DpLKbNU4WylpxJykQujfCcwYWiV/Jhm50Goo0wrVILAv5jOr9d+H+UR3PhSCD2rCCEIg0uc+G+muBTwD54JhDQ==",
			"license": "MIT",
			"dependencies": {
				"define-properties": "^1.2.1",
				"gopd": "^1.0.1"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/gopd": {
			"version": "1.2.0",
			"resolved": "https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz",
			"integrity": "sha512-ZUKRh6/kUFoAiTAtTYPZJ3hw9wNxx+BIBOijnlG9PnrJsCcSjs1wyyD6vJpaYtgnzDrKYRSqf3OO6Rfa93xsRg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/got": {
			"version": "13.0.0",
			"resolved": "https://registry.npmjs.org/got/-/got-13.0.0.tgz",
			"integrity": "sha512-XfBk1CxOOScDcMr9O1yKkNaQyy865NbYs+F7dr4H0LZMVgCj2Le59k6PqbNHoL5ToeaEQUYh6c6yMfVcc6SJxA==",
			"license": "MIT",
			"dependencies": {
				"@sindresorhus/is": "^5.2.0",
				"@szmarczak/http-timer": "^5.0.1",
				"cacheable-lookup": "^7.0.0",
				"cacheable-request": "^10.2.8",
				"decompress-response": "^6.0.0",
				"form-data-encoder": "^2.1.2",
				"get-stream": "^6.0.1",
				"http2-wrapper": "^2.1.10",
				"lowercase-keys": "^3.0.0",
				"p-cancelable": "^3.0.0",
				"responselike": "^3.0.0"
			},
			"engines": {
				"node": ">=16"
			},
			"funding": {
				"url": "https://github.com/sindresorhus/got?sponsor=1"
			}
		},
		"node_modules/graceful-fs": {
			"version": "4.2.11",
			"resolved": "https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz",
			"integrity": "sha512-RbJ5/jmFcNNCcDV5o9eTnBLJ/HszWV0P73bc+Ff4nS/rJj+YaS6IGyiOL0VoBYX+l1Wrl3k63h/KrH+nhJ0XvQ==",
			"license": "ISC"
		},
		"node_modules/has-bigints": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/has-bigints/-/has-bigints-1.1.0.tgz",
			"integrity": "sha512-R3pbpkcIqv2Pm3dUwgjclDRVmWpTJW2DcMzcIhEXEx1oh/CEMObMm3KLmRJOdvhM7o4uQBnwr8pzRK2sJWIqfg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/has-property-descriptors": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/has-property-descriptors/-/has-property-descriptors-1.0.2.tgz",
			"integrity": "sha512-55JNKuIW+vq4Ke1BjOTjM2YctQIvCT7GFzHwmfZPGo5wnrgkid0YQtnAleFSqumZm4az3n2BS+erby5ipJdgrg==",
			"license": "MIT",
			"dependencies": {
				"es-define-property": "^1.0.0"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/has-proto": {
			"version": "1.2.0",
			"resolved": "https://registry.npmjs.org/has-proto/-/has-proto-1.2.0.tgz",
			"integrity": "sha512-KIL7eQPfHQRC8+XluaIw7BHUwwqL19bQn4hzNgdr+1wXoU0KKj6rufu47lhY7KbJR2C6T6+PfyN0Ea7wkSS+qQ==",
			"license": "MIT",
			"dependencies": {
				"dunder-proto": "^1.0.0"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/has-symbols": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz",
			"integrity": "sha512-1cDNdwJ2Jaohmb3sg4OmKaMBwuC48sYni5HUw2DvsC8LjGTLK9h+eb1X6RyuOHe4hT0ULCW68iomhjUoKUqlPQ==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/has-tostringtag": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.2.tgz",
			"integrity": "sha512-NqADB8VjPFLM2V0VvHUewwwsw0ZWBaIdgo+ieHtK3hasLz4qeCRjYcqfB6AQrBggRKppKF8L52/VqdVsO47Dlw==",
			"license": "MIT",
			"dependencies": {
				"has-symbols": "^1.0.3"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/hasown": {
			"version": "2.0.2",
			"resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.2.tgz",
			"integrity": "sha512-0hJU9SCPvmMzIBdZFqNPXWa6dqh7WdH0cII9y+CyS8rG3nL48Bclra9HmKhVVUHyPWNH5Y7xDwAB7bfgSjkUMQ==",
			"license": "MIT",
			"dependencies": {
				"function-bind": "^1.1.2"
			},
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/hast-util-embedded": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/hast-util-embedded/-/hast-util-embedded-3.0.0.tgz",
			"integrity": "sha512-naH8sld4Pe2ep03qqULEtvYr7EjrLK2QHY8KJR6RJkTUjPGObe1vnx585uzem2hGra+s1q08DZZpfgDVYRbaXA==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"hast-util-is-element": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-from-dom": {
			"version": "5.0.1",
			"resolved": "https://registry.npmjs.org/hast-util-from-dom/-/hast-util-from-dom-5.0.1.tgz",
			"integrity": "sha512-N+LqofjR2zuzTjCPzyDUdSshy4Ma6li7p/c3pA78uTwzFgENbgbUrm2ugwsOdcjI1muO+o6Dgzp9p8WHtn/39Q==",
			"license": "ISC",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"hastscript": "^9.0.0",
				"web-namespaces": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-from-html": {
			"version": "2.0.3",
			"resolved": "https://registry.npmjs.org/hast-util-from-html/-/hast-util-from-html-2.0.3.tgz",
			"integrity": "sha512-CUSRHXyKjzHov8yKsQjGOElXy/3EKpyX56ELnkHH34vDVw1N1XSQ1ZcAvTyAPtGqLTuKP/uxM+aLkSPqF/EtMw==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"devlop": "^1.1.0",
				"hast-util-from-parse5": "^8.0.0",
				"parse5": "^7.0.0",
				"vfile": "^6.0.0",
				"vfile-message": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-from-html-isomorphic": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/hast-util-from-html-isomorphic/-/hast-util-from-html-isomorphic-2.0.0.tgz",
			"integrity": "sha512-zJfpXq44yff2hmE0XmwEOzdWin5xwH+QIhMLOScpX91e/NSGPsAzNCvLQDIEPyO2TXi+lBmU6hjLIhV8MwP2kw==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"hast-util-from-dom": "^5.0.0",
				"hast-util-from-html": "^2.0.0",
				"unist-util-remove-position": "^5.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-from-parse5": {
			"version": "8.0.3",
			"resolved": "https://registry.npmjs.org/hast-util-from-parse5/-/hast-util-from-parse5-8.0.3.tgz",
			"integrity": "sha512-3kxEVkEKt0zvcZ3hCRYI8rqrgwtlIOFMWkbclACvjlDw8Li9S2hk/d51OI0nr/gIpdMHNepwgOKqZ/sy0Clpyg==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"@types/unist": "^3.0.0",
				"devlop": "^1.0.0",
				"hastscript": "^9.0.0",
				"property-information": "^7.0.0",
				"vfile": "^6.0.0",
				"vfile-location": "^5.0.0",
				"web-namespaces": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-has-property": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/hast-util-has-property/-/hast-util-has-property-3.0.0.tgz",
			"integrity": "sha512-MNilsvEKLFpV604hwfhVStK0usFY/QmM5zX16bo7EjnAEGofr5YyI37kzopBlZJkHD4t887i+q/C8/tr5Q94cA==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-is-body-ok-link": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/hast-util-is-body-ok-link/-/hast-util-is-body-ok-link-3.0.1.tgz",
			"integrity": "sha512-0qpnzOBLztXHbHQenVB8uNuxTnm/QBFUOmdOSsEn7GnBtyY07+ENTWVFBAnXd/zEgd9/SUG3lRY7hSIBWRgGpQ==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-is-element": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/hast-util-is-element/-/hast-util-is-element-3.0.0.tgz",
			"integrity": "sha512-Val9mnv2IWpLbNPqc/pUem+a7Ipj2aHacCwgNfTiK0vJKl0LF+4Ba4+v1oPHFpf3bLYmreq0/l3Gud9S5OH42g==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-minify-whitespace": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/hast-util-minify-whitespace/-/hast-util-minify-whitespace-1.0.1.tgz",
			"integrity": "sha512-L96fPOVpnclQE0xzdWb/D12VT5FabA7SnZOUMtL1DbXmYiHJMXZvFkIZfiMmTCNJHUeO2K9UYNXoVyfz+QHuOw==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"hast-util-embedded": "^3.0.0",
				"hast-util-is-element": "^3.0.0",
				"hast-util-whitespace": "^3.0.0",
				"unist-util-is": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-parse-selector": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/hast-util-parse-selector/-/hast-util-parse-selector-4.0.0.tgz",
			"integrity": "sha512-wkQCkSYoOGCRKERFWcxMVMOcYE2K1AaNLU8DXS9arxnLOUEWbOXKXiJUNzEpqZ3JOKpnha3jkFrumEjVliDe7A==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-phrasing": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/hast-util-phrasing/-/hast-util-phrasing-3.0.1.tgz",
			"integrity": "sha512-6h60VfI3uBQUxHqTyMymMZnEbNl1XmEGtOxxKYL7stY2o601COo62AWAYBQR9lZbYXYSBoxag8UpPRXK+9fqSQ==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"hast-util-embedded": "^3.0.0",
				"hast-util-has-property": "^3.0.0",
				"hast-util-is-body-ok-link": "^3.0.0",
				"hast-util-is-element": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-to-estree": {
			"version": "3.1.3",
			"resolved": "https://registry.npmjs.org/hast-util-to-estree/-/hast-util-to-estree-3.1.3.tgz",
			"integrity": "sha512-48+B/rJWAp0jamNbAAf9M7Uf//UVqAoMmgXhBdxTDJLGKY+LRnZ99qcG+Qjl5HfMpYNzS5v4EAwVEF34LeAj7w==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0",
				"@types/estree-jsx": "^1.0.0",
				"@types/hast": "^3.0.0",
				"comma-separated-tokens": "^2.0.0",
				"devlop": "^1.0.0",
				"estree-util-attach-comments": "^3.0.0",
				"estree-util-is-identifier-name": "^3.0.0",
				"hast-util-whitespace": "^3.0.0",
				"mdast-util-mdx-expression": "^2.0.0",
				"mdast-util-mdx-jsx": "^3.0.0",
				"mdast-util-mdxjs-esm": "^2.0.0",
				"property-information": "^7.0.0",
				"space-separated-tokens": "^2.0.0",
				"style-to-js": "^1.0.0",
				"unist-util-position": "^5.0.0",
				"zwitch": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-to-html": {
			"version": "9.0.4",
			"resolved": "https://registry.npmjs.org/hast-util-to-html/-/hast-util-to-html-9.0.4.tgz",
			"integrity": "sha512-wxQzXtdbhiwGAUKrnQJXlOPmHnEehzphwkK7aluUPQ+lEc1xefC8pblMgpp2w5ldBTEfveRIrADcrhGIWrlTDA==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"@types/unist": "^3.0.0",
				"ccount": "^2.0.0",
				"comma-separated-tokens": "^2.0.0",
				"hast-util-whitespace": "^3.0.0",
				"html-void-elements": "^3.0.0",
				"mdast-util-to-hast": "^13.0.0",
				"property-information": "^6.0.0",
				"space-separated-tokens": "^2.0.0",
				"stringify-entities": "^4.0.0",
				"zwitch": "^2.0.4"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-to-html/node_modules/property-information": {
			"version": "6.5.0",
			"resolved": "https://registry.npmjs.org/property-information/-/property-information-6.5.0.tgz",
			"integrity": "sha512-PgTgs/BlvHxOu8QuEN7wi5A0OmXaBcHpmCSTehcs6Uuu9IkDIEo13Hy7n898RHfrQ49vKCoGeWZSaAK01nwVig==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/hast-util-to-jsx-runtime": {
			"version": "2.3.6",
			"resolved": "https://registry.npmjs.org/hast-util-to-jsx-runtime/-/hast-util-to-jsx-runtime-2.3.6.tgz",
			"integrity": "sha512-zl6s8LwNyo1P9uw+XJGvZtdFF1GdAkOg8ujOw+4Pyb76874fLps4ueHXDhXWdk6YHQ6OgUtinliG7RsYvCbbBg==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0",
				"@types/hast": "^3.0.0",
				"@types/unist": "^3.0.0",
				"comma-separated-tokens": "^2.0.0",
				"devlop": "^1.0.0",
				"estree-util-is-identifier-name": "^3.0.0",
				"hast-util-whitespace": "^3.0.0",
				"mdast-util-mdx-expression": "^2.0.0",
				"mdast-util-mdx-jsx": "^3.0.0",
				"mdast-util-mdxjs-esm": "^2.0.0",
				"property-information": "^7.0.0",
				"space-separated-tokens": "^2.0.0",
				"style-to-js": "^1.0.0",
				"unist-util-position": "^5.0.0",
				"vfile-message": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-to-mdast": {
			"version": "10.1.0",
			"resolved": "https://registry.npmjs.org/hast-util-to-mdast/-/hast-util-to-mdast-10.1.0.tgz",
			"integrity": "sha512-DsL/SvCK9V7+vfc6SLQ+vKIyBDXTk2KLSbfBYkH4zeF/uR1yBajHRhkzuaUSGOB1WJSTieJBdHwxlC+HLKvZZw==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"@types/mdast": "^4.0.0",
				"@ungap/structured-clone": "^1.0.0",
				"hast-util-phrasing": "^3.0.0",
				"hast-util-to-html": "^9.0.0",
				"hast-util-to-text": "^4.0.0",
				"hast-util-whitespace": "^3.0.0",
				"mdast-util-phrasing": "^4.0.0",
				"mdast-util-to-hast": "^13.0.0",
				"mdast-util-to-string": "^4.0.0",
				"rehype-minify-whitespace": "^6.0.0",
				"trim-trailing-lines": "^2.0.0",
				"unist-util-position": "^5.0.0",
				"unist-util-visit": "^5.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-to-string": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/hast-util-to-string/-/hast-util-to-string-3.0.1.tgz",
			"integrity": "sha512-XelQVTDWvqcl3axRfI0xSeoVKzyIFPwsAGSLIsKdJKQMXDYJS4WYrBNF/8J7RdhIcFI2BOHgAifggsvsxp/3+A==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-to-text": {
			"version": "4.0.2",
			"resolved": "https://registry.npmjs.org/hast-util-to-text/-/hast-util-to-text-4.0.2.tgz",
			"integrity": "sha512-KK6y/BN8lbaq654j7JgBydev7wuNMcID54lkRav1P0CaE1e47P72AWWPiGKXTJU271ooYzcvTAn/Zt0REnvc7A==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"@types/unist": "^3.0.0",
				"hast-util-is-element": "^3.0.0",
				"unist-util-find-after": "^5.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hast-util-whitespace": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/hast-util-whitespace/-/hast-util-whitespace-3.0.0.tgz",
			"integrity": "sha512-88JUN06ipLwsnv+dVn+OIYOvAuvBMy/Qoi6O7mQHxdPXpjy+Cd6xRkWwux7DKO+4sYILtLBRIKgsdpS2gQc7qw==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hastscript": {
			"version": "9.0.1",
			"resolved": "https://registry.npmjs.org/hastscript/-/hastscript-9.0.1.tgz",
			"integrity": "sha512-g7df9rMFX/SPi34tyGCyUBREQoKkapwdY/T04Qn9TDWfHhAYt4/I0gMVirzK5wEzeUqIjEB+LXC/ypb7Aqno5w==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"comma-separated-tokens": "^2.0.0",
				"hast-util-parse-selector": "^4.0.0",
				"property-information": "^7.0.0",
				"space-separated-tokens": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/hex-rgb": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/hex-rgb/-/hex-rgb-5.0.0.tgz",
			"integrity": "sha512-NQO+lgVUCtHxZ792FodgW0zflK+ozS9X9dwGp9XvvmPlH7pyxd588cn24TD3rmPm/N0AIRXF10Otah8yKqGw4w==",
			"license": "MIT",
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/html-void-elements": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/html-void-elements/-/html-void-elements-3.0.0.tgz",
			"integrity": "sha512-bEqo66MRXsUGxWHV5IP0PUiAWwoEjba4VCzg0LjFJBpchPaTfyfCKTG6bc5F8ucKec3q5y6qOdGyYTSBEvhCrg==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/http-cache-semantics": {
			"version": "4.2.0",
			"resolved": "https://registry.npmjs.org/http-cache-semantics/-/http-cache-semantics-4.2.0.tgz",
			"integrity": "sha512-dTxcvPXqPvXBQpq5dUr6mEMJX4oIEFv6bwom3FDwKRDsuIjjJGANqhBuoAn9c1RQJIdAKav33ED65E2ys+87QQ==",
			"license": "BSD-2-Clause"
		},
		"node_modules/http-errors": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/http-errors/-/http-errors-2.0.0.tgz",
			"integrity": "sha512-FtwrG/euBzaEjYeRqOgly7G0qviiXoJWnvEH2Z1plBdXgbyjv34pHTSb9zoeHMyDy33+DWy5Wt9Wo+TURtOYSQ==",
			"license": "MIT",
			"dependencies": {
				"depd": "2.0.0",
				"inherits": "2.0.4",
				"setprototypeof": "1.2.0",
				"statuses": "2.0.1",
				"toidentifier": "1.0.1"
			},
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/http-proxy-agent": {
			"version": "7.0.2",
			"resolved": "https://registry.npmjs.org/http-proxy-agent/-/http-proxy-agent-7.0.2.tgz",
			"integrity": "sha512-T1gkAiYYDWYx3V5Bmyu7HcfcvL7mUrTWiM6yOfa3PIphViJ/gFPbvidQ+veqSOHci/PxBcDabeUNCzpOODJZig==",
			"license": "MIT",
			"dependencies": {
				"agent-base": "^7.1.0",
				"debug": "^4.3.4"
			},
			"engines": {
				"node": ">= 14"
			}
		},
		"node_modules/http2-wrapper": {
			"version": "2.2.1",
			"resolved": "https://registry.npmjs.org/http2-wrapper/-/http2-wrapper-2.2.1.tgz",
			"integrity": "sha512-V5nVw1PAOgfI3Lmeaj2Exmeg7fenjhRUgz1lPSezy1CuhPYbgQtbQj4jZfEAEMlaL+vupsvhjqCyjzob0yxsmQ==",
			"license": "MIT",
			"dependencies": {
				"quick-lru": "^5.1.1",
				"resolve-alpn": "^1.2.0"
			},
			"engines": {
				"node": ">=10.19.0"
			}
		},
		"node_modules/https-proxy-agent": {
			"version": "7.0.6",
			"resolved": "https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-7.0.6.tgz",
			"integrity": "sha512-vK9P5/iUfdl95AI+JVyUuIcVtd4ofvtrOr3HNtM2yxC9bnMbEdp3x01OhQNnjb8IJYi38VlTE3mBXwcfvywuSw==",
			"license": "MIT",
			"dependencies": {
				"agent-base": "^7.1.2",
				"debug": "4"
			},
			"engines": {
				"node": ">= 14"
			}
		},
		"node_modules/ico-endec": {
			"version": "0.1.6",
			"resolved": "https://registry.npmjs.org/ico-endec/-/ico-endec-0.1.6.tgz",
			"integrity": "sha512-ZdLU38ZoED3g1j3iEyzcQj+wAkY2xfWNkymszfJPoxucIUhK7NayQ+/C4Kv0nDFMIsbtbEHldv3V8PU494/ueQ==",
			"license": "MPL-2.0"
		},
		"node_modules/iconv-lite": {
			"version": "0.7.2",
			"resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.7.2.tgz",
			"integrity": "sha512-im9DjEDQ55s9fL4EYzOAv0yMqmMBSZp6G0VvFyTMPKWxiSBHUj9NW/qqLmXUwXrrM7AvqSlTCfvqRb0cM8yYqw==",
			"license": "MIT",
			"dependencies": {
				"safer-buffer": ">= 2.1.2 < 3.0.0"
			},
			"engines": {
				"node": ">=0.10.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/express"
			}
		},
		"node_modules/ieee754": {
			"version": "1.2.1",
			"resolved": "https://registry.npmjs.org/ieee754/-/ieee754-1.2.1.tgz",
			"integrity": "sha512-dcyqhDvX1C46lXZcVqCpK+FtMRQVdIMN6/Df5js2zouUsqG7I6sFxitIC+7KYK29KdXOLHdu9zL4sFnoVQnqaA==",
			"funding": [
				{
					"type": "github",
					"url": "https://github.com/sponsors/feross"
				},
				{
					"type": "patreon",
					"url": "https://www.patreon.com/feross"
				},
				{
					"type": "consulting",
					"url": "https://feross.org/support"
				}
			],
			"license": "BSD-3-Clause"
		},
		"node_modules/ignore": {
			"version": "7.0.5",
			"resolved": "https://registry.npmjs.org/ignore/-/ignore-7.0.5.tgz",
			"integrity": "sha512-Hs59xBNfUIunMFgWAbGX5cq6893IbWg4KnrjbYwX3tx0ztorVgTDA6B2sxf8ejHJ4wz8BqGUMYlnzNBer5NvGg==",
			"license": "MIT",
			"engines": {
				"node": ">= 4"
			}
		},
		"node_modules/immer": {
			"version": "9.0.21",
			"resolved": "https://registry.npmjs.org/immer/-/immer-9.0.21.tgz",
			"integrity": "sha512-bc4NBHqOqSfRW7POMkHd51LvClaeMXpm8dx0e8oE2GORbq5aRK7Bxl4FyzVLdGtLmvLKL7BTDBG5ACQm4HWjTA==",
			"license": "MIT",
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/immer"
			}
		},
		"node_modules/import-fresh": {
			"version": "3.3.1",
			"resolved": "https://registry.npmjs.org/import-fresh/-/import-fresh-3.3.1.tgz",
			"integrity": "sha512-TR3KfrTZTYLPB6jUjfx6MF9WcWrHL9su5TObK4ZkYgBdWKPOFoSoQIdEuTuR82pmtxH2spWG9h6etwfr1pLBqQ==",
			"license": "MIT",
			"dependencies": {
				"parent-module": "^1.0.0",
				"resolve-from": "^4.0.0"
			},
			"engines": {
				"node": ">=6"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/indent-string": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/indent-string/-/indent-string-5.0.0.tgz",
			"integrity": "sha512-m6FAo/spmsW2Ab2fU35JTYwtOKa2yAwXSwgjSv1TJzh4Mh7mC3lzAOVLBprb72XsTrgkEIsl7YrFNAiDiRhIGg==",
			"license": "MIT",
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/inherits": {
			"version": "2.0.4",
			"resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
			"integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==",
			"license": "ISC"
		},
		"node_modules/ink": {
			"version": "6.3.0",
			"resolved": "https://registry.npmjs.org/ink/-/ink-6.3.0.tgz",
			"integrity": "sha512-2CbJAa7XeziZYe6pDS5RVLirRY28iSGMQuEV8jRU5NQsONQNfcR/BZHHc9vkMg2lGYTHTM2pskxC1YmY28p6bQ==",
			"license": "MIT",
			"dependencies": {
				"@alcalzone/ansi-tokenize": "^0.2.0",
				"ansi-escapes": "^7.0.0",
				"ansi-styles": "^6.2.1",
				"auto-bind": "^5.0.1",
				"chalk": "^5.6.0",
				"cli-boxes": "^3.0.0",
				"cli-cursor": "^4.0.0",
				"cli-truncate": "^4.0.0",
				"code-excerpt": "^4.0.0",
				"es-toolkit": "^1.39.10",
				"indent-string": "^5.0.0",
				"is-in-ci": "^2.0.0",
				"patch-console": "^2.0.0",
				"react-reconciler": "^0.32.0",
				"signal-exit": "^3.0.7",
				"slice-ansi": "^7.1.0",
				"stack-utils": "^2.0.6",
				"string-width": "^7.2.0",
				"type-fest": "^4.27.0",
				"widest-line": "^5.0.0",
				"wrap-ansi": "^9.0.0",
				"ws": "^8.18.0",
				"yoga-layout": "~3.2.1"
			},
			"engines": {
				"node": ">=20"
			},
			"peerDependencies": {
				"@types/react": ">=19.0.0",
				"react": ">=19.0.0",
				"react-devtools-core": "^4.19.1"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				},
				"react-devtools-core": {
					"optional": true
				}
			}
		},
		"node_modules/ink-spinner": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/ink-spinner/-/ink-spinner-5.0.0.tgz",
			"integrity": "sha512-EYEasbEjkqLGyPOUc8hBJZNuC5GvXGMLu0w5gdTNskPc7Izc5vO3tdQEYnzvshucyGCBXc86ig0ujXPMWaQCdA==",
			"license": "MIT",
			"dependencies": {
				"cli-spinners": "^2.7.0"
			},
			"engines": {
				"node": ">=14.16"
			},
			"peerDependencies": {
				"ink": ">=4.0.0",
				"react": ">=18.0.0"
			}
		},
		"node_modules/ink/node_modules/chalk": {
			"version": "5.6.2",
			"resolved": "https://registry.npmjs.org/chalk/-/chalk-5.6.2.tgz",
			"integrity": "sha512-7NzBL0rN6fMUW+f7A6Io4h40qQlG+xGmtMxfbnH/K7TAtt8JQWVQK+6g0UXKMeVJoyV5EkkNsErQ8pVD3bLHbA==",
			"license": "MIT",
			"engines": {
				"node": "^12.17.0 || ^14.13 || >=16.0.0"
			},
			"funding": {
				"url": "https://github.com/chalk/chalk?sponsor=1"
			}
		},
		"node_modules/ink/node_modules/signal-exit": {
			"version": "3.0.7",
			"resolved": "https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.7.tgz",
			"integrity": "sha512-wnD2ZE+l+SPC/uoS0vXeE9L1+0wuaMqKlfz9AMUo38JsyLSBWSFcHR1Rri62LZc12vLr1gb3jl7iwQhgwpAbGQ==",
			"license": "ISC"
		},
		"node_modules/ink/node_modules/wrap-ansi": {
			"version": "9.0.2",
			"resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-9.0.2.tgz",
			"integrity": "sha512-42AtmgqjV+X1VpdOfyTGOYRi0/zsoLqtXQckTmqTeybT+BDIbM/Guxo7x3pE2vtpr1ok6xRqM9OpBe+Jyoqyww==",
			"license": "MIT",
			"dependencies": {
				"ansi-styles": "^6.2.1",
				"string-width": "^7.0.0",
				"strip-ansi": "^7.1.0"
			},
			"engines": {
				"node": ">=18"
			},
			"funding": {
				"url": "https://github.com/chalk/wrap-ansi?sponsor=1"
			}
		},
		"node_modules/inline-style-parser": {
			"version": "0.2.7",
			"resolved": "https://registry.npmjs.org/inline-style-parser/-/inline-style-parser-0.2.7.tgz",
			"integrity": "sha512-Nb2ctOyNR8DqQoR0OwRG95uNWIC0C1lCgf5Naz5H6Ji72KZ8OcFZLz2P5sNgwlyoJ8Yif11oMuYs5pBQa86csA==",
			"license": "MIT"
		},
		"node_modules/inquirer": {
			"version": "12.3.0",
			"resolved": "https://registry.npmjs.org/inquirer/-/inquirer-12.3.0.tgz",
			"integrity": "sha512-3NixUXq+hM8ezj2wc7wC37b32/rHq1MwNZDYdvx+d6jokOD+r+i8Q4Pkylh9tISYP114A128LCX8RKhopC5RfQ==",
			"license": "MIT",
			"dependencies": {
				"@inquirer/core": "^10.1.2",
				"@inquirer/prompts": "^7.2.1",
				"@inquirer/type": "^3.0.2",
				"ansi-escapes": "^4.3.2",
				"mute-stream": "^2.0.0",
				"run-async": "^3.0.0",
				"rxjs": "^7.8.1"
			},
			"engines": {
				"node": ">=18"
			},
			"peerDependencies": {
				"@types/node": ">=18"
			}
		},
		"node_modules/inquirer/node_modules/ansi-escapes": {
			"version": "4.3.2",
			"resolved": "https://registry.npmjs.org/ansi-escapes/-/ansi-escapes-4.3.2.tgz",
			"integrity": "sha512-gKXj5ALrKWQLsYG9jlTRmR/xKluxHV+Z9QEwNIgCfM1/uwPMCuzVVnh5mwTd+OuBZcwSIMbqssNWRm1lE51QaQ==",
			"license": "MIT",
			"dependencies": {
				"type-fest": "^0.21.3"
			},
			"engines": {
				"node": ">=8"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/inquirer/node_modules/type-fest": {
			"version": "0.21.3",
			"resolved": "https://registry.npmjs.org/type-fest/-/type-fest-0.21.3.tgz",
			"integrity": "sha512-t0rzBq87m3fVcduHDUFhKmyyX+9eo6WQjZvf51Ea/M0Q7+T374Jp1aUiyUl0GKxp8M/OETVHSDvmkyPgvX+X2w==",
			"license": "(MIT OR CC0-1.0)",
			"engines": {
				"node": ">=10"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/internal-slot": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/internal-slot/-/internal-slot-1.1.0.tgz",
			"integrity": "sha512-4gd7VpWNQNB4UKKCFFVcp1AVv+FMOgs9NKzjHKusc8jTMhd5eL1NqQqOpE0KzMds804/yHlglp3uxgluOqAPLw==",
			"license": "MIT",
			"dependencies": {
				"es-errors": "^1.3.0",
				"hasown": "^2.0.2",
				"side-channel": "^1.1.0"
			},
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/ip-address": {
			"version": "10.1.0",
			"resolved": "https://registry.npmjs.org/ip-address/-/ip-address-10.1.0.tgz",
			"integrity": "sha512-XXADHxXmvT9+CRxhXg56LJovE+bmWnEWB78LB83VZTprKTmaC5QfruXocxzTZ2Kl0DNwKuBdlIhjL8LeY8Sf8Q==",
			"license": "MIT",
			"engines": {
				"node": ">= 12"
			}
		},
		"node_modules/ip-regex": {
			"version": "4.3.0",
			"resolved": "https://registry.npmjs.org/ip-regex/-/ip-regex-4.3.0.tgz",
			"integrity": "sha512-B9ZWJxHHOHUhUjCPrMpLD4xEq35bUTClHM1S6CBU5ixQnkZmwipwgc96vAd7AAGM9TGHvJR+Uss+/Ak6UphK+Q==",
			"license": "MIT",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/ipaddr.js": {
			"version": "1.9.1",
			"resolved": "https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.9.1.tgz",
			"integrity": "sha512-0KI/607xoxSToH7GjN1FfSbLoU0+btTicjsQSWQlh/hZykN8KpmMf7uYwPW3R+akZ6R/w18ZlXSHBYXiYUPO3g==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.10"
			}
		},
		"node_modules/is-alphabetical": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/is-alphabetical/-/is-alphabetical-2.0.1.tgz",
			"integrity": "sha512-FWyyY60MeTNyeSRpkM2Iry0G9hpr7/9kD40mD/cGQEuilcZYS4okz8SN2Q6rLCJ8gbCt6fN+rC+6tMGS99LaxQ==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/is-alphanumerical": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/is-alphanumerical/-/is-alphanumerical-2.0.1.tgz",
			"integrity": "sha512-hmbYhX/9MUMF5uh7tOXyK/n0ZvWpad5caBA17GsC6vyuCqaWliRG5K1qS9inmUhEMaOBIW7/whAnSwveW/LtZw==",
			"license": "MIT",
			"dependencies": {
				"is-alphabetical": "^2.0.0",
				"is-decimal": "^2.0.0"
			},
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/is-array-buffer": {
			"version": "3.0.5",
			"resolved": "https://registry.npmjs.org/is-array-buffer/-/is-array-buffer-3.0.5.tgz",
			"integrity": "sha512-DDfANUiiG2wC1qawP66qlTugJeL5HyzMpfr8lLK+jMQirGzNod0B12cFB/9q838Ru27sBwfw78/rdoU7RERz6A==",
			"license": "MIT",
			"dependencies": {
				"call-bind": "^1.0.8",
				"call-bound": "^1.0.3",
				"get-intrinsic": "^1.2.6"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-arrayish": {
			"version": "0.2.1",
			"resolved": "https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz",
			"integrity": "sha512-zz06S8t0ozoDXMG+ube26zeCTNXcKIPJZJi8hBrF4idCLms4CG9QtK7qBl1boi5ODzFpjswb5JPmHCbMpjaYzg==",
			"license": "MIT"
		},
		"node_modules/is-async-function": {
			"version": "2.1.1",
			"resolved": "https://registry.npmjs.org/is-async-function/-/is-async-function-2.1.1.tgz",
			"integrity": "sha512-9dgM/cZBnNvjzaMYHVoxxfPj2QXt22Ev7SuuPrs+xav0ukGB0S6d4ydZdEiM48kLx5kDV+QBPrpVnFyefL8kkQ==",
			"license": "MIT",
			"dependencies": {
				"async-function": "^1.0.0",
				"call-bound": "^1.0.3",
				"get-proto": "^1.0.1",
				"has-tostringtag": "^1.0.2",
				"safe-regex-test": "^1.1.0"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-bigint": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/is-bigint/-/is-bigint-1.1.0.tgz",
			"integrity": "sha512-n4ZT37wG78iz03xPRKJrHTdZbe3IicyucEtdRsV5yglwc3GyUfbAfpSeD0FJ41NbUNSt5wbhqfp1fS+BgnvDFQ==",
			"license": "MIT",
			"dependencies": {
				"has-bigints": "^1.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-binary-path": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/is-binary-path/-/is-binary-path-2.1.0.tgz",
			"integrity": "sha512-ZMERYes6pDydyuGidse7OsHxtbI7WVeUEozgR/g7rd0xUimYNlvZRE/K2MgZTjWy725IfelLeVcEM97mmtRGXw==",
			"license": "MIT",
			"dependencies": {
				"binary-extensions": "^2.0.0"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/is-boolean-object": {
			"version": "1.2.2",
			"resolved": "https://registry.npmjs.org/is-boolean-object/-/is-boolean-object-1.2.2.tgz",
			"integrity": "sha512-wa56o2/ElJMYqjCjGkXri7it5FbebW5usLw/nPmCMs5DeZ7eziSYZhSmPRn0txqeW4LnAmQQU7FgqLpsEFKM4A==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3",
				"has-tostringtag": "^1.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-callable": {
			"version": "1.2.7",
			"resolved": "https://registry.npmjs.org/is-callable/-/is-callable-1.2.7.tgz",
			"integrity": "sha512-1BC0BVFhS/p0qtw6enp8e+8OD0UrK0oFLztSjNzhcKA3WDuJxxAPXzPuPtKkjEY9UUoEWlX/8fgKeu2S8i9JTA==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-core-module": {
			"version": "2.16.1",
			"resolved": "https://registry.npmjs.org/is-core-module/-/is-core-module-2.16.1.tgz",
			"integrity": "sha512-UfoeMA6fIJ8wTYFEUjelnaGI67v6+N7qXJEvQuIGa99l4xsCruSYOVSQ0uPANn4dAzm8lkYPaKLrrijLq7x23w==",
			"license": "MIT",
			"dependencies": {
				"hasown": "^2.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-data-view": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/is-data-view/-/is-data-view-1.0.2.tgz",
			"integrity": "sha512-RKtWF8pGmS87i2D6gqQu/l7EYRlVdfzemCJN/P3UOs//x1QE7mfhvzHIApBTRf7axvT6DMGwSwBXYCT0nfB9xw==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.2",
				"get-intrinsic": "^1.2.6",
				"is-typed-array": "^1.1.13"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-date-object": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/is-date-object/-/is-date-object-1.1.0.tgz",
			"integrity": "sha512-PwwhEakHVKTdRNVOw+/Gyh0+MzlCl4R6qKvkhuvLtPMggI1WAHt9sOwZxQLSGpUaDnrdyDsomoRgNnCfKNSXXg==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.2",
				"has-tostringtag": "^1.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-decimal": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/is-decimal/-/is-decimal-2.0.1.tgz",
			"integrity": "sha512-AAB9hiomQs5DXWcRB1rqsxGUstbRroFOPPVAomNk/3XHR5JyEZChOyTWe2oayKnsSsr/kcGqF+z6yuH6HHpN0A==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/is-docker": {
			"version": "2.2.1",
			"resolved": "https://registry.npmjs.org/is-docker/-/is-docker-2.2.1.tgz",
			"integrity": "sha512-F+i2BKsFrH66iaUFc0woD8sLy8getkwTwtOBjvs56Cx4CgJDeKQeqfz8wAYiSb8JOprWhHH5p77PbmYCvvUuXQ==",
			"license": "MIT",
			"bin": {
				"is-docker": "cli.js"
			},
			"engines": {
				"node": ">=8"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/is-extglob": {
			"version": "2.1.1",
			"resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
			"integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
			"license": "MIT",
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/is-finalizationregistry": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/is-finalizationregistry/-/is-finalizationregistry-1.1.1.tgz",
			"integrity": "sha512-1pC6N8qWJbWoPtEjgcL2xyhQOP491EQjeUo3qTKcmV8YSDDJrOepfG8pcC7h/QgnQHYSv0mJ3Z/ZWxmatVrysg==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-fullwidth-code-point": {
			"version": "5.1.0",
			"resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-5.1.0.tgz",
			"integrity": "sha512-5XHYaSyiqADb4RnZ1Bdad6cPp8Toise4TzEjcOYDHZkTCbKgiUl7WTUCpNWHuxmDt91wnsZBc9xinNzopv3JMQ==",
			"license": "MIT",
			"dependencies": {
				"get-east-asian-width": "^1.3.1"
			},
			"engines": {
				"node": ">=18"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/is-generator-function": {
			"version": "1.1.2",
			"resolved": "https://registry.npmjs.org/is-generator-function/-/is-generator-function-1.1.2.tgz",
			"integrity": "sha512-upqt1SkGkODW9tsGNG5mtXTXtECizwtS2kA161M+gJPc1xdb/Ax629af6YrTwcOeQHbewrPNlE5Dx7kzvXTizA==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.4",
				"generator-function": "^2.0.0",
				"get-proto": "^1.0.1",
				"has-tostringtag": "^1.0.2",
				"safe-regex-test": "^1.1.0"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-glob": {
			"version": "4.0.3",
			"resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
			"integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
			"license": "MIT",
			"dependencies": {
				"is-extglob": "^2.1.1"
			},
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/is-hexadecimal": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/is-hexadecimal/-/is-hexadecimal-2.0.1.tgz",
			"integrity": "sha512-DgZQp241c8oO6cA1SbTEWiXeoxV42vlcJxgH+B3hi1AiqqKruZR3ZGF8In3fj4+/y/7rHvlOZLZtgJ/4ttYGZg==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/is-in-ci": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/is-in-ci/-/is-in-ci-2.0.0.tgz",
			"integrity": "sha512-cFeerHriAnhrQSbpAxL37W1wcJKUUX07HyLWZCW1URJT/ra3GyUTzBgUnh24TMVfNTV2Hij2HLxkPHFZfOZy5w==",
			"license": "MIT",
			"bin": {
				"is-in-ci": "cli.js"
			},
			"engines": {
				"node": ">=20"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/is-ip": {
			"version": "3.1.0",
			"resolved": "https://registry.npmjs.org/is-ip/-/is-ip-3.1.0.tgz",
			"integrity": "sha512-35vd5necO7IitFPjd/YBeqwWnyDWbuLH9ZXQdMfDA8TEo7pv5X8yfrvVO3xbJbLUlERCMvf6X0hTUamQxCYJ9Q==",
			"license": "MIT",
			"dependencies": {
				"ip-regex": "^4.0.0"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/is-map": {
			"version": "2.0.3",
			"resolved": "https://registry.npmjs.org/is-map/-/is-map-2.0.3.tgz",
			"integrity": "sha512-1Qed0/Hr2m+YqxnM09CjA2d/i6YZNfF6R2oRAOj36eUdS6qIV/huPJNSEpKbupewFs+ZsJlxsjjPbc0/afW6Lw==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-negative-zero": {
			"version": "2.0.3",
			"resolved": "https://registry.npmjs.org/is-negative-zero/-/is-negative-zero-2.0.3.tgz",
			"integrity": "sha512-5KoIu2Ngpyek75jXodFvnafB6DJgr3u8uuK0LEZJjrU19DrMD3EVERaR8sjz8CCGgpZvxPl9SuE1GMVPFHx1mw==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-number": {
			"version": "7.0.0",
			"resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
			"integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==",
			"license": "MIT",
			"engines": {
				"node": ">=0.12.0"
			}
		},
		"node_modules/is-number-object": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/is-number-object/-/is-number-object-1.1.1.tgz",
			"integrity": "sha512-lZhclumE1G6VYD8VHe35wFaIif+CTy5SJIi5+3y4psDgWu4wPDoBhF8NxUOinEc7pHgiTsT6MaBb92rKhhD+Xw==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3",
				"has-tostringtag": "^1.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-online": {
			"version": "10.0.0",
			"resolved": "https://registry.npmjs.org/is-online/-/is-online-10.0.0.tgz",
			"integrity": "sha512-WCPdKwNDjXJJmUubf2VHLMDBkUZEtuOvpXUfUnUFbEnM6In9ByiScL4f4jKACz/fsb2qDkesFerW3snf/AYz3A==",
			"license": "MIT",
			"dependencies": {
				"got": "^12.1.0",
				"p-any": "^4.0.0",
				"p-timeout": "^5.1.0",
				"public-ip": "^5.0.0"
			},
			"engines": {
				"node": ">=14.16"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/is-online/node_modules/got": {
			"version": "12.6.1",
			"resolved": "https://registry.npmjs.org/got/-/got-12.6.1.tgz",
			"integrity": "sha512-mThBblvlAF1d4O5oqyvN+ZxLAYwIJK7bpMxgYqPD9okW0C3qm5FFn7k811QrcuEBwaogR3ngOFoCfs6mRv7teQ==",
			"license": "MIT",
			"dependencies": {
				"@sindresorhus/is": "^5.2.0",
				"@szmarczak/http-timer": "^5.0.1",
				"cacheable-lookup": "^7.0.0",
				"cacheable-request": "^10.2.8",
				"decompress-response": "^6.0.0",
				"form-data-encoder": "^2.1.2",
				"get-stream": "^6.0.1",
				"http2-wrapper": "^2.1.10",
				"lowercase-keys": "^3.0.0",
				"p-cancelable": "^3.0.0",
				"responselike": "^3.0.0"
			},
			"engines": {
				"node": ">=14.16"
			},
			"funding": {
				"url": "https://github.com/sindresorhus/got?sponsor=1"
			}
		},
		"node_modules/is-plain-obj": {
			"version": "4.1.0",
			"resolved": "https://registry.npmjs.org/is-plain-obj/-/is-plain-obj-4.1.0.tgz",
			"integrity": "sha512-+Pgi+vMuUNkJyExiMBt5IlFoMyKnr5zhJ4Uspz58WOhBF5QoIZkFyNHIbBAtHwzVAgk5RtndVNsDRN61/mmDqg==",
			"license": "MIT",
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/is-regex": {
			"version": "1.2.1",
			"resolved": "https://registry.npmjs.org/is-regex/-/is-regex-1.2.1.tgz",
			"integrity": "sha512-MjYsKHO5O7mCsmRGxWcLWheFqN9DJ/2TmngvjKXihe6efViPqc274+Fx/4fYj/r03+ESvBdTXK0V6tA3rgez1g==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.2",
				"gopd": "^1.2.0",
				"has-tostringtag": "^1.0.2",
				"hasown": "^2.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-set": {
			"version": "2.0.3",
			"resolved": "https://registry.npmjs.org/is-set/-/is-set-2.0.3.tgz",
			"integrity": "sha512-iPAjerrse27/ygGLxw+EBR9agv9Y6uLeYVJMu+QNCoouJ1/1ri0mGrcWpfCqFZuzzx3WjtwxG098X+n4OuRkPg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-shared-array-buffer": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/is-shared-array-buffer/-/is-shared-array-buffer-1.0.4.tgz",
			"integrity": "sha512-ISWac8drv4ZGfwKl5slpHG9OwPNty4jOWPRIhBpxOoD+hqITiwuipOQ2bNthAzwA3B4fIjO4Nln74N0S9byq8A==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-string": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/is-string/-/is-string-1.1.1.tgz",
			"integrity": "sha512-BtEeSsoaQjlSPBemMQIrY1MY0uM6vnS1g5fmufYOtnxLGUZM2178PKbhsk7Ffv58IX+ZtcvoGwccYsh0PglkAA==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3",
				"has-tostringtag": "^1.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-symbol": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/is-symbol/-/is-symbol-1.1.1.tgz",
			"integrity": "sha512-9gGx6GTtCQM73BgmHQXfDmLtfjjTUDSyoxTCbp5WtoixAhfgsDirWIcVQ/IHpvI5Vgd5i/J5F7B9cN/WlVbC/w==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.2",
				"has-symbols": "^1.1.0",
				"safe-regex-test": "^1.1.0"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-typed-array": {
			"version": "1.1.15",
			"resolved": "https://registry.npmjs.org/is-typed-array/-/is-typed-array-1.1.15.tgz",
			"integrity": "sha512-p3EcsicXjit7SaskXHs1hA91QxgTw46Fv6EFKKGS5DRFLD8yKnohjF3hxoju94b/OcMZoQukzpPpBE9uLVKzgQ==",
			"license": "MIT",
			"dependencies": {
				"which-typed-array": "^1.1.16"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-weakmap": {
			"version": "2.0.2",
			"resolved": "https://registry.npmjs.org/is-weakmap/-/is-weakmap-2.0.2.tgz",
			"integrity": "sha512-K5pXYOm9wqY1RgjpL3YTkF39tni1XajUIkawTLUo9EZEVUFga5gSQJF8nNS7ZwJQ02y+1YCNYcMh+HIf1ZqE+w==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-weakref": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/is-weakref/-/is-weakref-1.1.1.tgz",
			"integrity": "sha512-6i9mGWSlqzNMEqpCp93KwRS1uUOodk2OJ6b+sq7ZPDSy2WuI5NFIxp/254TytR8ftefexkWn5xNiHUNpPOfSew==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-weakset": {
			"version": "2.0.4",
			"resolved": "https://registry.npmjs.org/is-weakset/-/is-weakset-2.0.4.tgz",
			"integrity": "sha512-mfcwb6IzQyOKTs84CQMrOwW4gQcaTOAWJ0zzJCl2WSPDrWk/OzDaImWFH3djXhb24g4eudZfLRozAvPGw4d9hQ==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3",
				"get-intrinsic": "^1.2.6"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/is-wsl": {
			"version": "2.2.0",
			"resolved": "https://registry.npmjs.org/is-wsl/-/is-wsl-2.2.0.tgz",
			"integrity": "sha512-fKzAra0rGJUUBwGBgNkHZuToZcn+TtXHpeCgmkMJMMYx1sQDYaCSyjJBSCa2nH1DGm7s3n1oBnohoVTBaN7Lww==",
			"license": "MIT",
			"dependencies": {
				"is-docker": "^2.0.0"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/isarray": {
			"version": "2.0.5",
			"resolved": "https://registry.npmjs.org/isarray/-/isarray-2.0.5.tgz",
			"integrity": "sha512-xHjhDr3cNBK0BzdUJSPXZntQUx/mwMS5Rw4A7lPJ90XGAO6ISP/ePDNuo0vhqOZU+UD5JoodwCAAoZQd3FeAKw==",
			"license": "MIT"
		},
		"node_modules/jiti": {
			"version": "1.21.7",
			"resolved": "https://registry.npmjs.org/jiti/-/jiti-1.21.7.tgz",
			"integrity": "sha512-/imKNG4EbWNrVjoNC/1H5/9GFy+tqjGBHCaSsN+P2RnPqjsLmv6UD3Ej+Kj8nBWaRAwyk7kK5ZUc+OEatnTR3A==",
			"license": "MIT",
			"bin": {
				"jiti": "bin/jiti.js"
			}
		},
		"node_modules/js-tokens": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
			"integrity": "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ==",
			"license": "MIT"
		},
		"node_modules/js-yaml": {
			"version": "4.1.1",
			"resolved": "https://registry.npmjs.org/js-yaml/-/js-yaml-4.1.1.tgz",
			"integrity": "sha512-qQKT4zQxXl8lLwBtHMWwaTcGfFOZviOJet3Oy/xmGk2gZH677CJM9EvtfdSkgWcATZhj/55JZ0rmy3myCT5lsA==",
			"license": "MIT",
			"dependencies": {
				"argparse": "^2.0.1"
			},
			"bin": {
				"js-yaml": "bin/js-yaml.js"
			}
		},
		"node_modules/jsep": {
			"version": "1.4.0",
			"resolved": "https://registry.npmjs.org/jsep/-/jsep-1.4.0.tgz",
			"integrity": "sha512-B7qPcEVE3NVkmSJbaYxvv4cHkVW7DQsZz13pUMrfS8z8Q/BuShN+gcTXrUlPiGqM2/t/EEaI030bpxMqY8gMlw==",
			"license": "MIT",
			"engines": {
				"node": ">= 10.16.0"
			}
		},
		"node_modules/json-buffer": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/json-buffer/-/json-buffer-3.0.1.tgz",
			"integrity": "sha512-4bV5BfR2mqfQTJm+V5tPPdf+ZpuhiIvTuAB5g8kcrXOZpTT/QwwVRWBywX1ozr6lEuPdbHxwaJlm9G6mI2sfSQ==",
			"license": "MIT"
		},
		"node_modules/json-parse-even-better-errors": {
			"version": "2.3.1",
			"resolved": "https://registry.npmjs.org/json-parse-even-better-errors/-/json-parse-even-better-errors-2.3.1.tgz",
			"integrity": "sha512-xyFwyhro/JEof6Ghe2iz2NcXoj2sloNsWr/XsERDK/oiPCfaNhl5ONfp+jQdAZRQQ0IJWNzH9zIZF7li91kh2w==",
			"license": "MIT"
		},
		"node_modules/json-schema-traverse": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-1.0.0.tgz",
			"integrity": "sha512-NM8/P9n3XjXhIZn1lLhkFaACTOURQXjWhV4BA/RnOv8xvgqtqpAX9IO4mRQxSx1Rlo4tqzeqb0sOlruaOy3dug==",
			"license": "MIT"
		},
		"node_modules/jsonc-parser": {
			"version": "2.2.1",
			"resolved": "https://registry.npmjs.org/jsonc-parser/-/jsonc-parser-2.2.1.tgz",
			"integrity": "sha512-o6/yDBYccGvTz1+QFevz6l6OBZ2+fMVu2JZ9CIhzsYRX4mjaK5IyX9eldUdCmga16zlgQxyrj5pt9kzuj2C02w==",
			"license": "MIT"
		},
		"node_modules/jsonfile": {
			"version": "6.2.0",
			"resolved": "https://registry.npmjs.org/jsonfile/-/jsonfile-6.2.0.tgz",
			"integrity": "sha512-FGuPw30AdOIUTRMC2OMRtQV+jkVj2cfPqSeWXv1NEAJ1qZ5zb1X6z1mFhbfOB/iy3ssJCD+3KuZ8r8C3uVFlAg==",
			"license": "MIT",
			"dependencies": {
				"universalify": "^2.0.0"
			},
			"optionalDependencies": {
				"graceful-fs": "^4.1.6"
			}
		},
		"node_modules/jsonpath-plus": {
			"version": "10.3.0",
			"resolved": "https://registry.npmjs.org/jsonpath-plus/-/jsonpath-plus-10.3.0.tgz",
			"integrity": "sha512-8TNmfeTCk2Le33A3vRRwtuworG/L5RrgMvdjhKZxvyShO+mBu2fP50OWUjRLNtvw344DdDarFh9buFAZs5ujeA==",
			"license": "MIT",
			"dependencies": {
				"@jsep-plugin/assignment": "^1.3.0",
				"@jsep-plugin/regex": "^1.0.4",
				"jsep": "^1.4.0"
			},
			"bin": {
				"jsonpath": "bin/jsonpath-cli.js",
				"jsonpath-plus": "bin/jsonpath-cli.js"
			},
			"engines": {
				"node": ">=18.0.0"
			}
		},
		"node_modules/jsonpointer": {
			"version": "5.0.1",
			"resolved": "https://registry.npmjs.org/jsonpointer/-/jsonpointer-5.0.1.tgz",
			"integrity": "sha512-p/nXbhSEcu3pZRdkW1OfJhpsVtW1gd4Wa1fnQc9YLiTfAjn0312eMKimbdIQzuZl9aa9xUGaRlP9T/CJE/ditQ==",
			"license": "MIT",
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/katex": {
			"version": "0.16.28",
			"resolved": "https://registry.npmjs.org/katex/-/katex-0.16.28.tgz",
			"integrity": "sha512-YHzO7721WbmAL6Ov1uzN/l5mY5WWWhJBSW+jq4tkfZfsxmo1hu6frS0EOswvjBUnWE6NtjEs48SFn5CQESRLZg==",
			"funding": [
				"https://opencollective.com/katex",
				"https://github.com/sponsors/katex"
			],
			"license": "MIT",
			"dependencies": {
				"commander": "^8.3.0"
			},
			"bin": {
				"katex": "cli.js"
			}
		},
		"node_modules/keyv": {
			"version": "4.5.4",
			"resolved": "https://registry.npmjs.org/keyv/-/keyv-4.5.4.tgz",
			"integrity": "sha512-oxVHkHR/EJf2CNXnWxRLW6mg7JyCCUcG0DtEGmL2ctUo1PNTin1PUil+r/+4r5MpVgC/fn1kjsx7mjSujKqIpw==",
			"license": "MIT",
			"dependencies": {
				"json-buffer": "3.0.1"
			}
		},
		"node_modules/lcm": {
			"version": "0.0.3",
			"resolved": "https://registry.npmjs.org/lcm/-/lcm-0.0.3.tgz",
			"integrity": "sha512-TB+ZjoillV6B26Vspf9l2L/vKaRY/4ep3hahcyVkCGFgsTNRUQdc24bQeNFiZeoxH0vr5+7SfNRMQuPHv/1IrQ==",
			"license": "MIT",
			"dependencies": {
				"gcd": "^0.0.1"
			}
		},
		"node_modules/leven": {
			"version": "4.1.0",
			"resolved": "https://registry.npmjs.org/leven/-/leven-4.1.0.tgz",
			"integrity": "sha512-KZ9W9nWDT7rF7Dazg8xyLHGLrmpgq2nVNFUckhqdW3szVP6YhCpp/RAnpmVExA9JvrMynjwSLVrEj3AepHR6ew==",
			"license": "MIT",
			"engines": {
				"node": "^12.20.0 || ^14.13.1 || >=16.0.0"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/lilconfig": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/lilconfig/-/lilconfig-2.1.0.tgz",
			"integrity": "sha512-utWOt/GHzuUxnLKxB6dk81RoOeoNeHgbrXiuGk4yyF5qlRz+iIVWu56E2fqGHFrXz0QNUhLB/8nKqvRH66JKGQ==",
			"license": "MIT",
			"engines": {
				"node": ">=10"
			}
		},
		"node_modules/lines-and-columns": {
			"version": "1.2.4",
			"resolved": "https://registry.npmjs.org/lines-and-columns/-/lines-and-columns-1.2.4.tgz",
			"integrity": "sha512-7ylylesZQ/PV29jhEDl3Ufjo6ZX7gCqJr5F7PKrqc93v7fzSymt1BpwEU8nAUXs8qzzvqhbjhK5QZg6Mt/HkBg==",
			"license": "MIT"
		},
		"node_modules/lodash": {
			"version": "4.17.21",
			"resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz",
			"integrity": "sha512-v2kDEe57lecTulaDIuNTPy3Ry4gLGJ6Z1O3vE1krgXZNrsQ+LFTGHVxVjcXPs17LhbZVGedAJv8XZ1tvj5FvSg==",
			"license": "MIT"
		},
		"node_modules/lodash.topath": {
			"version": "4.5.2",
			"resolved": "https://registry.npmjs.org/lodash.topath/-/lodash.topath-4.5.2.tgz",
			"integrity": "sha512-1/W4dM+35DwvE/iEd1M9ekewOSTlpFekhw9mhAtrwjVqUr83/ilQiyAvmg4tVX7Unkcfl1KC+i9WdaT4B6aQcg==",
			"license": "MIT"
		},
		"node_modules/longest-streak": {
			"version": "3.1.0",
			"resolved": "https://registry.npmjs.org/longest-streak/-/longest-streak-3.1.0.tgz",
			"integrity": "sha512-9Ri+o0JYgehTaVBBDoMqIl8GXtbWg711O3srftcHhZ0dqnETqLaoIK0x17fUw9rFSlK/0NlsKe0Ahhyl5pXE2g==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/loose-envify": {
			"version": "1.4.0",
			"resolved": "https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz",
			"integrity": "sha512-lyuxPGr/Wfhrlem2CL/UcnUc1zcqKAImBDzukY7Y5F/yQiNdko6+fRLevlw1HgMySw7f611UIY408EtxRSoK3Q==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"js-tokens": "^3.0.0 || ^4.0.0"
			},
			"bin": {
				"loose-envify": "cli.js"
			}
		},
		"node_modules/lowercase-keys": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/lowercase-keys/-/lowercase-keys-3.0.0.tgz",
			"integrity": "sha512-ozCC6gdQ+glXOQsveKD0YsDy8DSQFjDTz4zyzEHNV5+JP5D62LmfDZ6o1cycFx9ouG940M5dE8C8CTewdj2YWQ==",
			"license": "MIT",
			"engines": {
				"node": "^12.20.0 || ^14.13.1 || >=16.0.0"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/lru-cache": {
			"version": "7.18.3",
			"resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-7.18.3.tgz",
			"integrity": "sha512-jumlc0BIUrS3qJGgIkWZsyfAM7NCWiBcCDhnd+3NNM5KbBmLTgHVfWBcg6W+rLUsIpzpERPsvwUP7CckAQSOoA==",
			"license": "ISC",
			"engines": {
				"node": ">=12"
			}
		},
		"node_modules/markdown-extensions": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/markdown-extensions/-/markdown-extensions-2.0.0.tgz",
			"integrity": "sha512-o5vL7aDWatOTX8LzaS1WMoaoxIiLRQJuIKKe2wAw6IeULDHaqbiqiggmx+pKvZDb1Sj+pE46Sn1T7lCqfFtg1Q==",
			"license": "MIT",
			"engines": {
				"node": ">=16"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/markdown-table": {
			"version": "3.0.4",
			"resolved": "https://registry.npmjs.org/markdown-table/-/markdown-table-3.0.4.tgz",
			"integrity": "sha512-wiYz4+JrLyb/DqW2hkFJxP7Vd7JuTDm77fvbM8VfEQdmSMqcImWeeRbHwZjBjIFki/VaMK2BhFi7oUUZeM5bqw==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/math-intrinsics": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz",
			"integrity": "sha512-/IXtbwEk5HTPyEwyKX6hGkYXxM9nbj64B+ilVJnC/R6B0pH5G4V3b0pVbL7DBj4tkhBAppbQUlf6F6Xl9LHu1g==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/mdast-util-find-and-replace": {
			"version": "3.0.2",
			"resolved": "https://registry.npmjs.org/mdast-util-find-and-replace/-/mdast-util-find-and-replace-3.0.2.tgz",
			"integrity": "sha512-Tmd1Vg/m3Xz43afeNxDIhWRtFZgM2VLyaf4vSTYwudTyeuTneoL3qtWMA5jeLyz/O1vDJmmV4QuScFCA2tBPwg==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"escape-string-regexp": "^5.0.0",
				"unist-util-is": "^6.0.0",
				"unist-util-visit-parents": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-from-markdown": {
			"version": "2.0.2",
			"resolved": "https://registry.npmjs.org/mdast-util-from-markdown/-/mdast-util-from-markdown-2.0.2.tgz",
			"integrity": "sha512-uZhTV/8NBuw0WHkPTrCqDOl0zVe1BIng5ZtHoDk49ME1qqcjYmmLmOf0gELgcRMxN4w2iuIeVso5/6QymSrgmA==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"@types/unist": "^3.0.0",
				"decode-named-character-reference": "^1.0.0",
				"devlop": "^1.0.0",
				"mdast-util-to-string": "^4.0.0",
				"micromark": "^4.0.0",
				"micromark-util-decode-numeric-character-reference": "^2.0.0",
				"micromark-util-decode-string": "^2.0.0",
				"micromark-util-normalize-identifier": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0",
				"unist-util-stringify-position": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-frontmatter": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/mdast-util-frontmatter/-/mdast-util-frontmatter-2.0.1.tgz",
			"integrity": "sha512-LRqI9+wdgC25P0URIJY9vwocIzCcksduHQ9OF2joxQoyTNVduwLAFUzjoopuRJbJAReaKrNQKAZKL3uCMugWJA==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"devlop": "^1.0.0",
				"escape-string-regexp": "^5.0.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0",
				"micromark-extension-frontmatter": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-gfm": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/mdast-util-gfm/-/mdast-util-gfm-3.0.0.tgz",
			"integrity": "sha512-dgQEX5Amaq+DuUqf26jJqSK9qgixgd6rYDHAv4aTBuA92cTknZlKpPfa86Z/s8Dj8xsAQpFfBmPUHWJBWqS4Bw==",
			"license": "MIT",
			"dependencies": {
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-gfm-autolink-literal": "^2.0.0",
				"mdast-util-gfm-footnote": "^2.0.0",
				"mdast-util-gfm-strikethrough": "^2.0.0",
				"mdast-util-gfm-table": "^2.0.0",
				"mdast-util-gfm-task-list-item": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-gfm-autolink-literal": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/mdast-util-gfm-autolink-literal/-/mdast-util-gfm-autolink-literal-2.0.1.tgz",
			"integrity": "sha512-5HVP2MKaP6L+G6YaxPNjuL0BPrq9orG3TsrZ9YXbA3vDw/ACI4MEsnoDpn6ZNm7GnZgtAcONJyPhOP8tNJQavQ==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"ccount": "^2.0.0",
				"devlop": "^1.0.0",
				"mdast-util-find-and-replace": "^3.0.0",
				"micromark-util-character": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-gfm-footnote": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/mdast-util-gfm-footnote/-/mdast-util-gfm-footnote-2.1.0.tgz",
			"integrity": "sha512-sqpDWlsHn7Ac9GNZQMeUzPQSMzR6Wv0WKRNvQRg0KqHh02fpTz69Qc1QSseNX29bhz1ROIyNyxExfawVKTm1GQ==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"devlop": "^1.1.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0",
				"micromark-util-normalize-identifier": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-gfm-strikethrough": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/mdast-util-gfm-strikethrough/-/mdast-util-gfm-strikethrough-2.0.0.tgz",
			"integrity": "sha512-mKKb915TF+OC5ptj5bJ7WFRPdYtuHv0yTRxK2tJvi+BDqbkiG7h7u/9SI89nRAYcmap2xHQL9D+QG/6wSrTtXg==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-gfm-table": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/mdast-util-gfm-table/-/mdast-util-gfm-table-2.0.0.tgz",
			"integrity": "sha512-78UEvebzz/rJIxLvE7ZtDd/vIQ0RHv+3Mh5DR96p7cS7HsBhYIICDBCu8csTNWNO6tBWfqXPWekRuj2FNOGOZg==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"devlop": "^1.0.0",
				"markdown-table": "^3.0.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-gfm-task-list-item": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/mdast-util-gfm-task-list-item/-/mdast-util-gfm-task-list-item-2.0.0.tgz",
			"integrity": "sha512-IrtvNvjxC1o06taBAVJznEnkiHxLFTzgonUdy8hzFVeDun0uTjxxrRGVaNFqkU1wJR3RBPEfsxmU6jDWPofrTQ==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"devlop": "^1.0.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-math": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/mdast-util-math/-/mdast-util-math-3.0.0.tgz",
			"integrity": "sha512-Tl9GBNeG/AhJnQM221bJR2HPvLOSnLE/T9cJI9tlc6zwQk2nPk/4f0cHkOdEixQPC/j8UtKDdITswvLAy1OZ1w==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"@types/mdast": "^4.0.0",
				"devlop": "^1.0.0",
				"longest-streak": "^3.0.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.1.0",
				"unist-util-remove-position": "^5.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-mdx": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/mdast-util-mdx/-/mdast-util-mdx-3.0.0.tgz",
			"integrity": "sha512-JfbYLAW7XnYTTbUsmpu0kdBUVe+yKVJZBItEjwyYJiDJuZ9w4eeaqks4HQO+R7objWgS2ymV60GYpI14Ug554w==",
			"license": "MIT",
			"dependencies": {
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-mdx-expression": "^2.0.0",
				"mdast-util-mdx-jsx": "^3.0.0",
				"mdast-util-mdxjs-esm": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-mdx-expression": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/mdast-util-mdx-expression/-/mdast-util-mdx-expression-2.0.1.tgz",
			"integrity": "sha512-J6f+9hUp+ldTZqKRSg7Vw5V6MqjATc+3E4gf3CFNcuZNWD8XdyI6zQ8GqH7f8169MM6P7hMBRDVGnn7oHB9kXQ==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"@types/hast": "^3.0.0",
				"@types/mdast": "^4.0.0",
				"devlop": "^1.0.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-mdx-jsx": {
			"version": "3.2.0",
			"resolved": "https://registry.npmjs.org/mdast-util-mdx-jsx/-/mdast-util-mdx-jsx-3.2.0.tgz",
			"integrity": "sha512-lj/z8v0r6ZtsN/cGNNtemmmfoLAFZnjMbNyLzBafjzikOM+glrjNHPlf6lQDOTccj9n5b0PPihEBbhneMyGs1Q==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"@types/hast": "^3.0.0",
				"@types/mdast": "^4.0.0",
				"@types/unist": "^3.0.0",
				"ccount": "^2.0.0",
				"devlop": "^1.1.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0",
				"parse-entities": "^4.0.0",
				"stringify-entities": "^4.0.0",
				"unist-util-stringify-position": "^4.0.0",
				"vfile-message": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-mdxjs-esm": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/mdast-util-mdxjs-esm/-/mdast-util-mdxjs-esm-2.0.1.tgz",
			"integrity": "sha512-EcmOpxsZ96CvlP03NghtH1EsLtr0n9Tm4lPUJUBccV9RwUOneqSycg19n5HGzCf+10LozMRSObtVr3ee1WoHtg==",
			"license": "MIT",
			"dependencies": {
				"@types/estree-jsx": "^1.0.0",
				"@types/hast": "^3.0.0",
				"@types/mdast": "^4.0.0",
				"devlop": "^1.0.0",
				"mdast-util-from-markdown": "^2.0.0",
				"mdast-util-to-markdown": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-phrasing": {
			"version": "4.1.0",
			"resolved": "https://registry.npmjs.org/mdast-util-phrasing/-/mdast-util-phrasing-4.1.0.tgz",
			"integrity": "sha512-TqICwyvJJpBwvGAMZjj4J2n0X8QWp21b9l0o7eXyVJ25YNWYbJDVIyD1bZXE6WtV6RmKJVYmQAKWa0zWOABz2w==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"unist-util-is": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-to-hast": {
			"version": "13.2.1",
			"resolved": "https://registry.npmjs.org/mdast-util-to-hast/-/mdast-util-to-hast-13.2.1.tgz",
			"integrity": "sha512-cctsq2wp5vTsLIcaymblUriiTcZd0CwWtCbLvrOzYCDZoWyMNV8sZ7krj09FSnsiJi3WVsHLM4k6Dq/yaPyCXA==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"@types/mdast": "^4.0.0",
				"@ungap/structured-clone": "^1.0.0",
				"devlop": "^1.0.0",
				"micromark-util-sanitize-uri": "^2.0.0",
				"trim-lines": "^3.0.0",
				"unist-util-position": "^5.0.0",
				"unist-util-visit": "^5.0.0",
				"vfile": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-to-markdown": {
			"version": "2.1.2",
			"resolved": "https://registry.npmjs.org/mdast-util-to-markdown/-/mdast-util-to-markdown-2.1.2.tgz",
			"integrity": "sha512-xj68wMTvGXVOKonmog6LwyJKrYXZPvlwabaryTjLh9LuvovB/KAH+kvi8Gjj+7rJjsFi23nkUxRQv1KqSroMqA==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"@types/unist": "^3.0.0",
				"longest-streak": "^3.0.0",
				"mdast-util-phrasing": "^4.0.0",
				"mdast-util-to-string": "^4.0.0",
				"micromark-util-classify-character": "^2.0.0",
				"micromark-util-decode-string": "^2.0.0",
				"unist-util-visit": "^5.0.0",
				"zwitch": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/mdast-util-to-string": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/mdast-util-to-string/-/mdast-util-to-string-4.0.0.tgz",
			"integrity": "sha512-0H44vDimn51F0YwvxSJSm0eCDOJTRlmN0R1yBh4HLj9wiV1Dn0QoXGbvFAWj2hSItVTlCmBF1hqKlIyUBVFLPg==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/media-typer": {
			"version": "0.3.0",
			"resolved": "https://registry.npmjs.org/media-typer/-/media-typer-0.3.0.tgz",
			"integrity": "sha512-dq+qelQ9akHpcOl/gUVRTxVIOkAJ1wR3QAvb4RsVjS8oVoFjDGTc679wJYmUmknUF5HwMLOgb5O+a3KxfWapPQ==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/merge-descriptors": {
			"version": "1.0.3",
			"resolved": "https://registry.npmjs.org/merge-descriptors/-/merge-descriptors-1.0.3.tgz",
			"integrity": "sha512-gaNvAS7TZ897/rVaZ0nMtAyxNyi/pdbjbAwUpFQpN70GqnVfOiXpeUUMKRBmzXaSQ8DdTX4/0ms62r2K+hE6mQ==",
			"license": "MIT",
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/merge2": {
			"version": "1.4.1",
			"resolved": "https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz",
			"integrity": "sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg==",
			"license": "MIT",
			"engines": {
				"node": ">= 8"
			}
		},
		"node_modules/methods": {
			"version": "1.1.2",
			"resolved": "https://registry.npmjs.org/methods/-/methods-1.1.2.tgz",
			"integrity": "sha512-iclAHeNqNm68zFtnZ0e+1L2yUIdvzNoauKU4WBA3VvH/vPFieF7qfRlwUZU+DA9P9bPXIS90ulxoUoCH23sV2w==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/micromark": {
			"version": "4.0.2",
			"resolved": "https://registry.npmjs.org/micromark/-/micromark-4.0.2.tgz",
			"integrity": "sha512-zpe98Q6kvavpCr1NPVSCMebCKfD7CA2NqZ+rykeNhONIJBpc1tFKt9hucLGwha3jNTNI8lHpctWJWoimVF4PfA==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"@types/debug": "^4.0.0",
				"debug": "^4.0.0",
				"decode-named-character-reference": "^1.0.0",
				"devlop": "^1.0.0",
				"micromark-core-commonmark": "^2.0.0",
				"micromark-factory-space": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-chunked": "^2.0.0",
				"micromark-util-combine-extensions": "^2.0.0",
				"micromark-util-decode-numeric-character-reference": "^2.0.0",
				"micromark-util-encode": "^2.0.0",
				"micromark-util-normalize-identifier": "^2.0.0",
				"micromark-util-resolve-all": "^2.0.0",
				"micromark-util-sanitize-uri": "^2.0.0",
				"micromark-util-subtokenize": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-core-commonmark": {
			"version": "2.0.3",
			"resolved": "https://registry.npmjs.org/micromark-core-commonmark/-/micromark-core-commonmark-2.0.3.tgz",
			"integrity": "sha512-RDBrHEMSxVFLg6xvnXmb1Ayr2WzLAWjeSATAoxwKYJV94TeNavgoIdA0a9ytzDSVzBy2YKFK+emCPOEibLeCrg==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"decode-named-character-reference": "^1.0.0",
				"devlop": "^1.0.0",
				"micromark-factory-destination": "^2.0.0",
				"micromark-factory-label": "^2.0.0",
				"micromark-factory-space": "^2.0.0",
				"micromark-factory-title": "^2.0.0",
				"micromark-factory-whitespace": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-chunked": "^2.0.0",
				"micromark-util-classify-character": "^2.0.0",
				"micromark-util-html-tag-name": "^2.0.0",
				"micromark-util-normalize-identifier": "^2.0.0",
				"micromark-util-resolve-all": "^2.0.0",
				"micromark-util-subtokenize": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-extension-frontmatter": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/micromark-extension-frontmatter/-/micromark-extension-frontmatter-2.0.0.tgz",
			"integrity": "sha512-C4AkuM3dA58cgZha7zVnuVxBhDsbttIMiytjgsM2XbHAB2faRVaHRle40558FBN+DJcrLNCoqG5mlrpdU4cRtg==",
			"license": "MIT",
			"dependencies": {
				"fault": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-extension-gfm": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/micromark-extension-gfm/-/micromark-extension-gfm-3.0.0.tgz",
			"integrity": "sha512-vsKArQsicm7t0z2GugkCKtZehqUm31oeGBV/KVSorWSy8ZlNAv7ytjFhvaryUiCUJYqs+NoE6AFhpQvBTM6Q4w==",
			"license": "MIT",
			"dependencies": {
				"micromark-extension-gfm-autolink-literal": "^2.0.0",
				"micromark-extension-gfm-footnote": "^2.0.0",
				"micromark-extension-gfm-strikethrough": "^2.0.0",
				"micromark-extension-gfm-table": "^2.0.0",
				"micromark-extension-gfm-tagfilter": "^2.0.0",
				"micromark-extension-gfm-task-list-item": "^2.0.0",
				"micromark-util-combine-extensions": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-extension-gfm-autolink-literal": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/micromark-extension-gfm-autolink-literal/-/micromark-extension-gfm-autolink-literal-2.1.0.tgz",
			"integrity": "sha512-oOg7knzhicgQ3t4QCjCWgTmfNhvQbDDnJeVu9v81r7NltNCVmhPy1fJRX27pISafdjL+SVc4d3l48Gb6pbRypw==",
			"license": "MIT",
			"dependencies": {
				"micromark-util-character": "^2.0.0",
				"micromark-util-sanitize-uri": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-extension-gfm-footnote": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/micromark-extension-gfm-footnote/-/micromark-extension-gfm-footnote-2.1.0.tgz",
			"integrity": "sha512-/yPhxI1ntnDNsiHtzLKYnE3vf9JZ6cAisqVDauhp4CEHxlb4uoOTxOCJ+9s51bIB8U1N1FJ1RXOKTIlD5B/gqw==",
			"license": "MIT",
			"dependencies": {
				"devlop": "^1.0.0",
				"micromark-core-commonmark": "^2.0.0",
				"micromark-factory-space": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-normalize-identifier": "^2.0.0",
				"micromark-util-sanitize-uri": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-extension-gfm-strikethrough": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/micromark-extension-gfm-strikethrough/-/micromark-extension-gfm-strikethrough-2.1.0.tgz",
			"integrity": "sha512-ADVjpOOkjz1hhkZLlBiYA9cR2Anf8F4HqZUO6e5eDcPQd0Txw5fxLzzxnEkSkfnD0wziSGiv7sYhk/ktvbf1uw==",
			"license": "MIT",
			"dependencies": {
				"devlop": "^1.0.0",
				"micromark-util-chunked": "^2.0.0",
				"micromark-util-classify-character": "^2.0.0",
				"micromark-util-resolve-all": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-extension-gfm-table": {
			"version": "2.1.1",
			"resolved": "https://registry.npmjs.org/micromark-extension-gfm-table/-/micromark-extension-gfm-table-2.1.1.tgz",
			"integrity": "sha512-t2OU/dXXioARrC6yWfJ4hqB7rct14e8f7m0cbI5hUmDyyIlwv5vEtooptH8INkbLzOatzKuVbQmAYcbWoyz6Dg==",
			"license": "MIT",
			"dependencies": {
				"devlop": "^1.0.0",
				"micromark-factory-space": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-extension-gfm-tagfilter": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/micromark-extension-gfm-tagfilter/-/micromark-extension-gfm-tagfilter-2.0.0.tgz",
			"integrity": "sha512-xHlTOmuCSotIA8TW1mDIM6X2O1SiX5P9IuDtqGonFhEK0qgRI4yeC6vMxEV2dgyr2TiD+2PQ10o+cOhdVAcwfg==",
			"license": "MIT",
			"dependencies": {
				"micromark-util-types": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-extension-gfm-task-list-item": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/micromark-extension-gfm-task-list-item/-/micromark-extension-gfm-task-list-item-2.1.0.tgz",
			"integrity": "sha512-qIBZhqxqI6fjLDYFTBIa4eivDMnP+OZqsNwmQ3xNLE4Cxwc+zfQEfbs6tzAo2Hjq+bh6q5F+Z8/cksrLFYWQQw==",
			"license": "MIT",
			"dependencies": {
				"devlop": "^1.0.0",
				"micromark-factory-space": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-extension-math": {
			"version": "3.1.0",
			"resolved": "https://registry.npmjs.org/micromark-extension-math/-/micromark-extension-math-3.1.0.tgz",
			"integrity": "sha512-lvEqd+fHjATVs+2v/8kg9i5Q0AP2k85H0WUOwpIVvUML8BapsMvh1XAogmQjOCsLpoKRCVQqEkQBB3NhVBcsOg==",
			"license": "MIT",
			"dependencies": {
				"@types/katex": "^0.16.0",
				"devlop": "^1.0.0",
				"katex": "^0.16.0",
				"micromark-factory-space": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-extension-mdx-expression": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/micromark-extension-mdx-expression/-/micromark-extension-mdx-expression-3.0.1.tgz",
			"integrity": "sha512-dD/ADLJ1AeMvSAKBwO22zG22N4ybhe7kFIZ3LsDI0GlsNr2A3KYxb0LdC1u5rj4Nw+CHKY0RVdnHX8vj8ejm4Q==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0",
				"devlop": "^1.0.0",
				"micromark-factory-mdx-expression": "^2.0.0",
				"micromark-factory-space": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-events-to-acorn": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-extension-mdx-jsx": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/micromark-extension-mdx-jsx/-/micromark-extension-mdx-jsx-3.0.1.tgz",
			"integrity": "sha512-vNuFb9czP8QCtAQcEJn0UJQJZA8Dk6DXKBqx+bg/w0WGuSxDxNr7hErW89tHUY31dUW4NqEOWwmEUNhjTFmHkg==",
			"license": "MIT",
			"dependencies": {
				"@types/acorn": "^4.0.0",
				"@types/estree": "^1.0.0",
				"devlop": "^1.0.0",
				"estree-util-is-identifier-name": "^3.0.0",
				"micromark-factory-mdx-expression": "^2.0.0",
				"micromark-factory-space": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-events-to-acorn": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0",
				"vfile-message": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-extension-mdx-md": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/micromark-extension-mdx-md/-/micromark-extension-mdx-md-2.0.0.tgz",
			"integrity": "sha512-EpAiszsB3blw4Rpba7xTOUptcFeBFi+6PY8VnJ2hhimH+vCQDirWgsMpz7w1XcZE7LVrSAUGb9VJpG9ghlYvYQ==",
			"license": "MIT",
			"dependencies": {
				"micromark-util-types": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-extension-mdxjs": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/micromark-extension-mdxjs/-/micromark-extension-mdxjs-3.0.0.tgz",
			"integrity": "sha512-A873fJfhnJ2siZyUrJ31l34Uqwy4xIFmvPY1oj+Ean5PHcPBYzEsvqvWGaWcfEIr11O5Dlw3p2y0tZWpKHDejQ==",
			"license": "MIT",
			"dependencies": {
				"acorn": "^8.0.0",
				"acorn-jsx": "^5.0.0",
				"micromark-extension-mdx-expression": "^3.0.0",
				"micromark-extension-mdx-jsx": "^3.0.0",
				"micromark-extension-mdx-md": "^2.0.0",
				"micromark-extension-mdxjs-esm": "^3.0.0",
				"micromark-util-combine-extensions": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-extension-mdxjs-esm": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/micromark-extension-mdxjs-esm/-/micromark-extension-mdxjs-esm-3.0.0.tgz",
			"integrity": "sha512-DJFl4ZqkErRpq/dAPyeWp15tGrcrrJho1hKK5uBS70BCtfrIFg81sqcTVu3Ta+KD1Tk5vAtBNElWxtAa+m8K9A==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0",
				"devlop": "^1.0.0",
				"micromark-core-commonmark": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-events-to-acorn": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0",
				"unist-util-position-from-estree": "^2.0.0",
				"vfile-message": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/micromark-factory-destination": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-factory-destination/-/micromark-factory-destination-2.0.1.tgz",
			"integrity": "sha512-Xe6rDdJlkmbFRExpTOmRj9N3MaWmbAgdpSrBQvCFqhezUn4AHqJHbaEnfbVYYiexVSs//tqOdY/DxhjdCiJnIA==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"micromark-util-character": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-factory-label": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-factory-label/-/micromark-factory-label-2.0.1.tgz",
			"integrity": "sha512-VFMekyQExqIW7xIChcXn4ok29YE3rnuyveW3wZQWWqF4Nv9Wk5rgJ99KzPvHjkmPXF93FXIbBp6YdW3t71/7Vg==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"devlop": "^1.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-factory-mdx-expression": {
			"version": "2.0.3",
			"resolved": "https://registry.npmjs.org/micromark-factory-mdx-expression/-/micromark-factory-mdx-expression-2.0.3.tgz",
			"integrity": "sha512-kQnEtA3vzucU2BkrIa8/VaSAsP+EJ3CKOvhMuJgOEGg9KDC6OAY6nSnNDVRiVNRqj7Y4SlSzcStaH/5jge8JdQ==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0",
				"devlop": "^1.0.0",
				"micromark-factory-space": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-events-to-acorn": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0",
				"unist-util-position-from-estree": "^2.0.0",
				"vfile-message": "^4.0.0"
			}
		},
		"node_modules/micromark-factory-space": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-factory-space/-/micromark-factory-space-2.0.1.tgz",
			"integrity": "sha512-zRkxjtBxxLd2Sc0d+fbnEunsTj46SWXgXciZmHq0kDYGnck/ZSGj9/wULTV95uoeYiK5hRXP2mJ98Uo4cq/LQg==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"micromark-util-character": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-factory-title": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-factory-title/-/micromark-factory-title-2.0.1.tgz",
			"integrity": "sha512-5bZ+3CjhAd9eChYTHsjy6TGxpOFSKgKKJPJxr293jTbfry2KDoWkhBb6TcPVB4NmzaPhMs1Frm9AZH7OD4Cjzw==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"micromark-factory-space": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-factory-whitespace": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-factory-whitespace/-/micromark-factory-whitespace-2.0.1.tgz",
			"integrity": "sha512-Ob0nuZ3PKt/n0hORHyvoD9uZhr+Za8sFoP+OnMcnWK5lngSzALgQYKMr9RJVOWLqQYuyn6ulqGWSXdwf6F80lQ==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"micromark-factory-space": "^2.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-util-character": {
			"version": "2.1.1",
			"resolved": "https://registry.npmjs.org/micromark-util-character/-/micromark-util-character-2.1.1.tgz",
			"integrity": "sha512-wv8tdUTJ3thSFFFJKtpYKOYiGP2+v96Hvk4Tu8KpCAsTMs6yi+nVmGh1syvSCsaxz45J6Jbw+9DD6g97+NV67Q==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-util-chunked": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-util-chunked/-/micromark-util-chunked-2.0.1.tgz",
			"integrity": "sha512-QUNFEOPELfmvv+4xiNg2sRYeS/P84pTW0TCgP5zc9FpXetHY0ab7SxKyAQCNCc1eK0459uoLI1y5oO5Vc1dbhA==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"micromark-util-symbol": "^2.0.0"
			}
		},
		"node_modules/micromark-util-classify-character": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-util-classify-character/-/micromark-util-classify-character-2.0.1.tgz",
			"integrity": "sha512-K0kHzM6afW/MbeWYWLjoHQv1sgg2Q9EccHEDzSkxiP/EaagNzCm7T/WMKZ3rjMbvIpvBiZgwR3dKMygtA4mG1Q==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"micromark-util-character": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-util-combine-extensions": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-util-combine-extensions/-/micromark-util-combine-extensions-2.0.1.tgz",
			"integrity": "sha512-OnAnH8Ujmy59JcyZw8JSbK9cGpdVY44NKgSM7E9Eh7DiLS2E9RNQf0dONaGDzEG9yjEl5hcqeIsj4hfRkLH/Bg==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"micromark-util-chunked": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-util-decode-numeric-character-reference": {
			"version": "2.0.2",
			"resolved": "https://registry.npmjs.org/micromark-util-decode-numeric-character-reference/-/micromark-util-decode-numeric-character-reference-2.0.2.tgz",
			"integrity": "sha512-ccUbYk6CwVdkmCQMyr64dXz42EfHGkPQlBj5p7YVGzq8I7CtjXZJrubAYezf7Rp+bjPseiROqe7G6foFd+lEuw==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"micromark-util-symbol": "^2.0.0"
			}
		},
		"node_modules/micromark-util-decode-string": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-util-decode-string/-/micromark-util-decode-string-2.0.1.tgz",
			"integrity": "sha512-nDV/77Fj6eH1ynwscYTOsbK7rR//Uj0bZXBwJZRfaLEJ1iGBR6kIfNmlNqaqJf649EP0F3NWNdeJi03elllNUQ==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"decode-named-character-reference": "^1.0.0",
				"micromark-util-character": "^2.0.0",
				"micromark-util-decode-numeric-character-reference": "^2.0.0",
				"micromark-util-symbol": "^2.0.0"
			}
		},
		"node_modules/micromark-util-encode": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-util-encode/-/micromark-util-encode-2.0.1.tgz",
			"integrity": "sha512-c3cVx2y4KqUnwopcO9b/SCdo2O67LwJJ/UyqGfbigahfegL9myoEFoDYZgkT7f36T0bLrM9hZTAaAyH+PCAXjw==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT"
		},
		"node_modules/micromark-util-events-to-acorn": {
			"version": "2.0.3",
			"resolved": "https://registry.npmjs.org/micromark-util-events-to-acorn/-/micromark-util-events-to-acorn-2.0.3.tgz",
			"integrity": "sha512-jmsiEIiZ1n7X1Rr5k8wVExBQCg5jy4UXVADItHmNk1zkwEVhBuIUKRu3fqv+hs4nxLISi2DQGlqIOGiFxgbfHg==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0",
				"@types/unist": "^3.0.0",
				"devlop": "^1.0.0",
				"estree-util-visit": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0",
				"vfile-message": "^4.0.0"
			}
		},
		"node_modules/micromark-util-html-tag-name": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-util-html-tag-name/-/micromark-util-html-tag-name-2.0.1.tgz",
			"integrity": "sha512-2cNEiYDhCWKI+Gs9T0Tiysk136SnR13hhO8yW6BGNyhOC4qYFnwF1nKfD3HFAIXA5c45RrIG1ub11GiXeYd1xA==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT"
		},
		"node_modules/micromark-util-normalize-identifier": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-util-normalize-identifier/-/micromark-util-normalize-identifier-2.0.1.tgz",
			"integrity": "sha512-sxPqmo70LyARJs0w2UclACPUUEqltCkJ6PhKdMIDuJ3gSf/Q+/GIe3WKl0Ijb/GyH9lOpUkRAO2wp0GVkLvS9Q==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"micromark-util-symbol": "^2.0.0"
			}
		},
		"node_modules/micromark-util-resolve-all": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-util-resolve-all/-/micromark-util-resolve-all-2.0.1.tgz",
			"integrity": "sha512-VdQyxFWFT2/FGJgwQnJYbe1jjQoNTS4RjglmSjTUlpUMa95Htx9NHeYW4rGDJzbjvCsl9eLjMQwGeElsqmzcHg==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-util-sanitize-uri": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-util-sanitize-uri/-/micromark-util-sanitize-uri-2.0.1.tgz",
			"integrity": "sha512-9N9IomZ/YuGGZZmQec1MbgxtlgougxTodVwDzzEouPKo3qFWvymFHWcnDi2vzV1ff6kas9ucW+o3yzJK9YB1AQ==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"micromark-util-character": "^2.0.0",
				"micromark-util-encode": "^2.0.0",
				"micromark-util-symbol": "^2.0.0"
			}
		},
		"node_modules/micromark-util-subtokenize": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/micromark-util-subtokenize/-/micromark-util-subtokenize-2.1.0.tgz",
			"integrity": "sha512-XQLu552iSctvnEcgXw6+Sx75GflAPNED1qx7eBJ+wydBb2KCbRZe+NwvIEEMM83uml1+2WSXpBAcp9IUCgCYWA==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT",
			"dependencies": {
				"devlop": "^1.0.0",
				"micromark-util-chunked": "^2.0.0",
				"micromark-util-symbol": "^2.0.0",
				"micromark-util-types": "^2.0.0"
			}
		},
		"node_modules/micromark-util-symbol": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/micromark-util-symbol/-/micromark-util-symbol-2.0.1.tgz",
			"integrity": "sha512-vs5t8Apaud9N28kgCrRUdEed4UJ+wWNvicHLPxCa9ENlYuAY31M0ETy5y1vA33YoNPDFTghEbnh6efaE8h4x0Q==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT"
		},
		"node_modules/micromark-util-types": {
			"version": "2.0.2",
			"resolved": "https://registry.npmjs.org/micromark-util-types/-/micromark-util-types-2.0.2.tgz",
			"integrity": "sha512-Yw0ECSpJoViF1qTU4DC6NwtC4aWGt1EkzaQB8KPPyCRR8z9TWeV0HbEFGTO+ZY1wB22zmxnJqhPyTpOVCpeHTA==",
			"funding": [
				{
					"type": "GitHub Sponsors",
					"url": "https://github.com/sponsors/unifiedjs"
				},
				{
					"type": "OpenCollective",
					"url": "https://opencollective.com/unified"
				}
			],
			"license": "MIT"
		},
		"node_modules/micromatch": {
			"version": "4.0.8",
			"resolved": "https://registry.npmjs.org/micromatch/-/micromatch-4.0.8.tgz",
			"integrity": "sha512-PXwfBhYu0hBCPw8Dn0E+WDYb7af3dSLVWKi3HGv84IdF4TyFoC0ysxFd0Goxw7nSv4T/PzEJQxsYsEiFCKo2BA==",
			"license": "MIT",
			"dependencies": {
				"braces": "^3.0.3",
				"picomatch": "^2.3.1"
			},
			"engines": {
				"node": ">=8.6"
			}
		},
		"node_modules/mime": {
			"version": "1.6.0",
			"resolved": "https://registry.npmjs.org/mime/-/mime-1.6.0.tgz",
			"integrity": "sha512-x0Vn8spI+wuJ1O6S7gnbaQg8Pxh4NNHb7KSINmEWKiPE4RKOplvijn+NkmYmmRgP68mc70j2EbeTFRsrswaQeg==",
			"license": "MIT",
			"bin": {
				"mime": "cli.js"
			},
			"engines": {
				"node": ">=4"
			}
		},
		"node_modules/mime-db": {
			"version": "1.52.0",
			"resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz",
			"integrity": "sha512-sPU4uV7dYlvtWJxwwxHD0PuihVNiE7TyAbQ5SWxDCB9mUYvOgroQOwYQQOKPJ8CIbE+1ETVlOoK1UC2nU3gYvg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/mime-types": {
			"version": "2.1.35",
			"resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz",
			"integrity": "sha512-ZDY+bPm5zTTF+YpCrAU9nK0UgICYPT0QtT1NZWFv4s++TNkcgVaT0g6+4R2uI4MjQjzysHB1zxuWL50hzaeXiw==",
			"license": "MIT",
			"dependencies": {
				"mime-db": "1.52.0"
			},
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/mimic-fn": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/mimic-fn/-/mimic-fn-2.1.0.tgz",
			"integrity": "sha512-OqbOk5oEQeAZ8WXWydlu9HJjz9WVdEIvamMCcXmuqUYjTknH/sqsWvhQ3vgwKFRR1HpjvNBKQ37nbJgYzGqGcg==",
			"license": "MIT",
			"engines": {
				"node": ">=6"
			}
		},
		"node_modules/mimic-response": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/mimic-response/-/mimic-response-4.0.0.tgz",
			"integrity": "sha512-e5ISH9xMYU0DzrT+jl8q2ze9D6eWBto+I8CNpe+VI+K2J/F/k3PdkdTdz4wvGVH4NTpo+NRYTVIuMQEMMcsLqg==",
			"license": "MIT",
			"engines": {
				"node": "^12.20.0 || ^14.13.1 || >=16.0.0"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/minimatch": {
			"version": "3.1.2",
			"resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz",
			"integrity": "sha512-J7p63hRiAjw1NDEww1W7i37+ByIrOWO5XQQAzZ3VOcL0PNybwpfmV/N05zFAzwQ9USyEcX6t3UO+K5aqBQOIHw==",
			"license": "ISC",
			"dependencies": {
				"brace-expansion": "^1.1.7"
			},
			"engines": {
				"node": "*"
			}
		},
		"node_modules/minipass": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/minipass/-/minipass-5.0.0.tgz",
			"integrity": "sha512-3FnjYuehv9k6ovOEbyOswadCDPX1piCfhV8ncmYtHOjuPwylVWsghTLo7rabjC3Rx5xD4HDx8Wm1xnMF7S5qFQ==",
			"license": "ISC",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/minizlib": {
			"version": "2.1.2",
			"resolved": "https://registry.npmjs.org/minizlib/-/minizlib-2.1.2.tgz",
			"integrity": "sha512-bAxsR8BVfj60DWXHE3u30oHzfl4G7khkSuPW+qvpd7jFRHm7dLxOjUk1EHACJ/hxLY8phGJ0YhYHZo7jil7Qdg==",
			"license": "MIT",
			"dependencies": {
				"minipass": "^3.0.0",
				"yallist": "^4.0.0"
			},
			"engines": {
				"node": ">= 8"
			}
		},
		"node_modules/minizlib/node_modules/minipass": {
			"version": "3.3.6",
			"resolved": "https://registry.npmjs.org/minipass/-/minipass-3.3.6.tgz",
			"integrity": "sha512-DxiNidxSEK+tHG6zOIklvNOwm3hvCrbUrdtzY74U6HKTJxvIDfOUL5W5P2Ghd3DTkhhKPYGqeNUIh5qcM4YBfw==",
			"license": "ISC",
			"dependencies": {
				"yallist": "^4.0.0"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/mintlify": {
			"version": "4.2.338",
			"resolved": "https://registry.npmjs.org/mintlify/-/mintlify-4.2.338.tgz",
			"integrity": "sha512-uWswdD4oEyVCcBeoFmJx8VMXXkK0ad1qFJ+Tli7T93oSJZWlGlRPs6SlDwFgksdX2UdJWHQgvrja7G8Wzxq41w==",
			"license": "Elastic-2.0",
			"dependencies": {
				"@mintlify/cli": "4.0.942"
			},
			"bin": {
				"mint": "index.js",
				"mintlify": "index.js"
			},
			"engines": {
				"node": ">=18.0.0"
			}
		},
		"node_modules/mitt": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/mitt/-/mitt-3.0.1.tgz",
			"integrity": "sha512-vKivATfr97l2/QBCYAkXYDbrIWPM2IIKEl7YPhjCvKlG3kE2gm+uBo6nEXK3M5/Ffh/FLpKExzOQ3JJoJGFKBw==",
			"license": "MIT"
		},
		"node_modules/mkdirp": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/mkdirp/-/mkdirp-1.0.4.tgz",
			"integrity": "sha512-vVqVZQyf3WLx2Shd0qJ9xuvqgAyKPLAiqITEtqW0oIUjzo3PePDd6fW9iFz30ef7Ysp/oiWqbhszeGWW2T6Gzw==",
			"license": "MIT",
			"bin": {
				"mkdirp": "bin/cmd.js"
			},
			"engines": {
				"node": ">=10"
			}
		},
		"node_modules/ms": {
			"version": "2.1.3",
			"resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
			"integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
			"license": "MIT"
		},
		"node_modules/mute-stream": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/mute-stream/-/mute-stream-2.0.0.tgz",
			"integrity": "sha512-WWdIxpyjEn+FhQJQQv9aQAYlHoNVdzIzUySNV1gHUPDSdZJ3yZn7pAAbQcV7B56Mvu881q9FZV+0Vx2xC44VWA==",
			"license": "ISC",
			"engines": {
				"node": "^18.17.0 || >=20.5.0"
			}
		},
		"node_modules/mz": {
			"version": "2.7.0",
			"resolved": "https://registry.npmjs.org/mz/-/mz-2.7.0.tgz",
			"integrity": "sha512-z81GNO7nnYMEhrGh9LeymoE4+Yr0Wn5McHIZMK5cfQCl+NDX08sCZgUc9/6MHni9IWuFLm1Z3HTCXu2z9fN62Q==",
			"license": "MIT",
			"dependencies": {
				"any-promise": "^1.0.0",
				"object-assign": "^4.0.1",
				"thenify-all": "^1.0.0"
			}
		},
		"node_modules/nanoid": {
			"version": "3.3.11",
			"resolved": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.11.tgz",
			"integrity": "sha512-N8SpfPUnUp1bK+PMYW8qSWdl9U+wwNWI4QKxOYDy9JAro3WMX7p2OeVRF9v+347pnakNevPmiHhNmZ2HbFA76w==",
			"funding": [
				{
					"type": "github",
					"url": "https://github.com/sponsors/ai"
				}
			],
			"license": "MIT",
			"bin": {
				"nanoid": "bin/nanoid.cjs"
			},
			"engines": {
				"node": "^10 || ^12 || ^13.7 || ^14 || >=15.0.1"
			}
		},
		"node_modules/negotiator": {
			"version": "0.6.3",
			"resolved": "https://registry.npmjs.org/negotiator/-/negotiator-0.6.3.tgz",
			"integrity": "sha512-+EUsqGPLsM+j/zdChZjsnX51g4XrHFOIXwfnCVPGlQk/k5giakcKsuxCObBRu6DSm9opw/O6slWbJdghQM4bBg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/neotraverse": {
			"version": "0.6.18",
			"resolved": "https://registry.npmjs.org/neotraverse/-/neotraverse-0.6.18.tgz",
			"integrity": "sha512-Z4SmBUweYa09+o6pG+eASabEpP6QkQ70yHj351pQoEXIs8uHbaU2DWVmzBANKgflPa47A50PtB2+NgRpQvr7vA==",
			"license": "MIT",
			"engines": {
				"node": ">= 10"
			}
		},
		"node_modules/netmask": {
			"version": "2.0.2",
			"resolved": "https://registry.npmjs.org/netmask/-/netmask-2.0.2.tgz",
			"integrity": "sha512-dBpDMdxv9Irdq66304OLfEmQ9tbNRFnFTuZiLo+bD+r332bBmMJ8GBLXklIXXgxd3+v9+KUnZaUR5PJMa75Gsg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4.0"
			}
		},
		"node_modules/nimma": {
			"version": "0.2.3",
			"resolved": "https://registry.npmjs.org/nimma/-/nimma-0.2.3.tgz",
			"integrity": "sha512-1ZOI8J+1PKKGceo/5CT5GfQOG6H8I2BencSK06YarZ2wXwH37BSSUWldqJmMJYA5JfqDqffxDXynt6f11AyKcA==",
			"license": "Apache-2.0",
			"dependencies": {
				"@jsep-plugin/regex": "^1.0.1",
				"@jsep-plugin/ternary": "^1.0.2",
				"astring": "^1.8.1",
				"jsep": "^1.2.0"
			},
			"engines": {
				"node": "^12.20 || >=14.13"
			},
			"optionalDependencies": {
				"jsonpath-plus": "^6.0.1 || ^10.1.0",
				"lodash.topath": "^4.5.2"
			}
		},
		"node_modules/nlcst-to-string": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/nlcst-to-string/-/nlcst-to-string-4.0.0.tgz",
			"integrity": "sha512-YKLBCcUYKAg0FNlOBT6aI91qFmSiFKiluk655WzPF+DDMA02qIyy8uiRqI8QXtcFpEvll12LpL5MXqEmAZ+dcA==",
			"license": "MIT",
			"dependencies": {
				"@types/nlcst": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/node-fetch": {
			"version": "2.6.7",
			"resolved": "https://registry.npmjs.org/node-fetch/-/node-fetch-2.6.7.tgz",
			"integrity": "sha512-ZjMPFEfVx5j+y2yF35Kzx5sF7kDzxuDj6ziH4FFbOp87zKDZNx8yExJIb05OGF4Nlt9IHFIMBkRl41VdvcNdbQ==",
			"license": "MIT",
			"dependencies": {
				"whatwg-url": "^5.0.0"
			},
			"engines": {
				"node": "4.x || >=6.0.0"
			},
			"peerDependencies": {
				"encoding": "^0.1.0"
			},
			"peerDependenciesMeta": {
				"encoding": {
					"optional": true
				}
			}
		},
		"node_modules/normalize-path": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/normalize-path/-/normalize-path-3.0.0.tgz",
			"integrity": "sha512-6eZs5Ls3WtCisHWp9S2GUy8dqkpGi4BVSz3GaqiE6ezub0512ESztXUwUB6C6IKbQkY2Pnb/mD4WYojCRwcwLA==",
			"license": "MIT",
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/normalize-url": {
			"version": "8.1.1",
			"resolved": "https://registry.npmjs.org/normalize-url/-/normalize-url-8.1.1.tgz",
			"integrity": "sha512-JYc0DPlpGWB40kH5g07gGTrYuMqV653k3uBKY6uITPWds3M0ov3GaWGp9lbE3Bzngx8+XkfzgvASb9vk9JDFXQ==",
			"license": "MIT",
			"engines": {
				"node": ">=14.16"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/object-assign": {
			"version": "4.1.1",
			"resolved": "https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz",
			"integrity": "sha512-rJgTQnkUnH1sFw8yT6VSU3zD3sWmu6sZhIseY8VX+GRu3P6F7Fu+JNDoXfklElbLJSnc3FUQHVe4cU5hj+BcUg==",
			"license": "MIT",
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/object-hash": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/object-hash/-/object-hash-3.0.0.tgz",
			"integrity": "sha512-RSn9F68PjH9HqtltsSnqYC1XXoWe9Bju5+213R98cNGttag9q9yAOTzdbsqvIa7aNm5WffBZFpWYr2aWrklWAw==",
			"license": "MIT",
			"engines": {
				"node": ">= 6"
			}
		},
		"node_modules/object-inspect": {
			"version": "1.13.4",
			"resolved": "https://registry.npmjs.org/object-inspect/-/object-inspect-1.13.4.tgz",
			"integrity": "sha512-W67iLl4J2EXEGTbfeHCffrjDfitvLANg0UlX3wFUUSTx92KXRFegMHUVgSqE+wvhAbi4WqjGg9czysTV2Epbew==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/object-keys": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz",
			"integrity": "sha512-NuAESUOUMrlIXOfHKzD6bpPu3tYt3xvjNdRIQ+FeT0lNb4K8WR70CaDxhuNguS2XG+GjkyMwOzsN5ZktImfhLA==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/object.assign": {
			"version": "4.1.7",
			"resolved": "https://registry.npmjs.org/object.assign/-/object.assign-4.1.7.tgz",
			"integrity": "sha512-nK28WOo+QIjBkDduTINE4JkF/UJJKyf2EJxvJKfblDpyg0Q+pkOHNTL0Qwy6NP6FhE/EnzV73BxxqcJaXY9anw==",
			"license": "MIT",
			"dependencies": {
				"call-bind": "^1.0.8",
				"call-bound": "^1.0.3",
				"define-properties": "^1.2.1",
				"es-object-atoms": "^1.0.0",
				"has-symbols": "^1.1.0",
				"object-keys": "^1.1.1"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/on-finished": {
			"version": "2.4.1",
			"resolved": "https://registry.npmjs.org/on-finished/-/on-finished-2.4.1.tgz",
			"integrity": "sha512-oVlzkg3ENAhCk2zdv7IJwd/QUD4z2RxRwpkcGY8psCVcCYZNq4wYnVWALHM+brtuJjePWiYF/ClmuDr8Ch5+kg==",
			"license": "MIT",
			"dependencies": {
				"ee-first": "1.1.1"
			},
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/once": {
			"version": "1.4.0",
			"resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz",
			"integrity": "sha512-lNaJgI+2Q5URQBkccEKHTQOPaXdUxnZZElQTZY0MFUAuaEqe1E+Nyvgdz/aIyNi6Z9MzO5dv1H8n58/GELp3+w==",
			"license": "ISC",
			"dependencies": {
				"wrappy": "1"
			}
		},
		"node_modules/onetime": {
			"version": "5.1.2",
			"resolved": "https://registry.npmjs.org/onetime/-/onetime-5.1.2.tgz",
			"integrity": "sha512-kbpaSSGJTWdAY5KPVeMOKXSrPtr8C8C7wodJbcsd51jRnmD+GZu8Y0VoU6Dm5Z4vWr0Ig/1NKuWRKf7j5aaYSg==",
			"license": "MIT",
			"dependencies": {
				"mimic-fn": "^2.1.0"
			},
			"engines": {
				"node": ">=6"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/oniguruma-parser": {
			"version": "0.12.1",
			"resolved": "https://registry.npmjs.org/oniguruma-parser/-/oniguruma-parser-0.12.1.tgz",
			"integrity": "sha512-8Unqkvk1RYc6yq2WBYRj4hdnsAxVze8i7iPfQr8e4uSP3tRv0rpZcbGUDvxfQQcdwHt/e9PrMvGCsa8OqG9X3w==",
			"license": "MIT"
		},
		"node_modules/oniguruma-to-es": {
			"version": "4.3.4",
			"resolved": "https://registry.npmjs.org/oniguruma-to-es/-/oniguruma-to-es-4.3.4.tgz",
			"integrity": "sha512-3VhUGN3w2eYxnTzHn+ikMI+fp/96KoRSVK9/kMTcFqj1NRDh2IhQCKvYxDnWePKRXY/AqH+Fuiyb7VHSzBjHfA==",
			"license": "MIT",
			"dependencies": {
				"oniguruma-parser": "^0.12.1",
				"regex": "^6.0.1",
				"regex-recursion": "^6.0.2"
			}
		},
		"node_modules/open": {
			"version": "8.4.2",
			"resolved": "https://registry.npmjs.org/open/-/open-8.4.2.tgz",
			"integrity": "sha512-7x81NCL719oNbsq/3mh+hVrAWmFuEYUqrq/Iw3kUzH8ReypT9QQ0BLoJS7/G9k6N81XjW4qHWtjWwe/9eLy1EQ==",
			"license": "MIT",
			"dependencies": {
				"define-lazy-prop": "^2.0.0",
				"is-docker": "^2.1.1",
				"is-wsl": "^2.2.0"
			},
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/openapi-types": {
			"version": "12.1.3",
			"resolved": "https://registry.npmjs.org/openapi-types/-/openapi-types-12.1.3.tgz",
			"integrity": "sha512-N4YtSYJqghVu4iek2ZUvcN/0aqH1kRDuNqzcycDxhOUpg7GdvLa2F3DgS6yBNhInhv2r/6I0Flkn7CqL8+nIcw==",
			"license": "MIT"
		},
		"node_modules/own-keys": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/own-keys/-/own-keys-1.0.1.tgz",
			"integrity": "sha512-qFOyK5PjiWZd+QQIh+1jhdb9LpxTF0qs7Pm8o5QHYZ0M3vKqSqzsZaEB6oWlxZ+q2sJBMI/Ktgd2N5ZwQoRHfg==",
			"license": "MIT",
			"dependencies": {
				"get-intrinsic": "^1.2.6",
				"object-keys": "^1.1.1",
				"safe-push-apply": "^1.0.0"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/p-any": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/p-any/-/p-any-4.0.0.tgz",
			"integrity": "sha512-S/B50s+pAVe0wmEZHmBs/9yJXeZ5KhHzOsgKzt0hRdgkoR3DxW9ts46fcsWi/r3VnzsnkKS7q4uimze+zjdryw==",
			"license": "MIT",
			"dependencies": {
				"p-cancelable": "^3.0.0",
				"p-some": "^6.0.0"
			},
			"engines": {
				"node": ">=12.20"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/p-cancelable": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/p-cancelable/-/p-cancelable-3.0.0.tgz",
			"integrity": "sha512-mlVgR3PGuzlo0MmTdk4cXqXWlwQDLnONTAg6sm62XkMJEiRxN3GL3SffkYvqwonbkJBcrI7Uvv5Zh9yjvn2iUw==",
			"license": "MIT",
			"engines": {
				"node": ">=12.20"
			}
		},
		"node_modules/p-some": {
			"version": "6.0.0",
			"resolved": "https://registry.npmjs.org/p-some/-/p-some-6.0.0.tgz",
			"integrity": "sha512-CJbQCKdfSX3fIh8/QKgS+9rjm7OBNUTmwWswAFQAhc8j1NR1dsEDETUEuVUtQHZpV+J03LqWBEwvu0g1Yn+TYg==",
			"license": "MIT",
			"dependencies": {
				"aggregate-error": "^4.0.0",
				"p-cancelable": "^3.0.0"
			},
			"engines": {
				"node": ">=12.20"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/p-timeout": {
			"version": "5.1.0",
			"resolved": "https://registry.npmjs.org/p-timeout/-/p-timeout-5.1.0.tgz",
			"integrity": "sha512-auFDyzzzGZZZdHz3BtET9VEz0SE/uMEAx7uWfGPucfzEwwe/xH0iVeZibQmANYE/hp9T2+UUZT5m+BKyrDp3Ew==",
			"license": "MIT",
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/pac-proxy-agent": {
			"version": "7.2.0",
			"resolved": "https://registry.npmjs.org/pac-proxy-agent/-/pac-proxy-agent-7.2.0.tgz",
			"integrity": "sha512-TEB8ESquiLMc0lV8vcd5Ql/JAKAoyzHFXaStwjkzpOpC5Yv+pIzLfHvjTSdf3vpa2bMiUQrg9i6276yn8666aA==",
			"license": "MIT",
			"dependencies": {
				"@tootallnate/quickjs-emscripten": "^0.23.0",
				"agent-base": "^7.1.2",
				"debug": "^4.3.4",
				"get-uri": "^6.0.1",
				"http-proxy-agent": "^7.0.0",
				"https-proxy-agent": "^7.0.6",
				"pac-resolver": "^7.0.1",
				"socks-proxy-agent": "^8.0.5"
			},
			"engines": {
				"node": ">= 14"
			}
		},
		"node_modules/pac-resolver": {
			"version": "7.0.1",
			"resolved": "https://registry.npmjs.org/pac-resolver/-/pac-resolver-7.0.1.tgz",
			"integrity": "sha512-5NPgf87AT2STgwa2ntRMr45jTKrYBGkVU36yT0ig/n/GMAa3oPqhZfIQ2kMEimReg0+t9kZViDVZ83qfVUlckg==",
			"license": "MIT",
			"dependencies": {
				"degenerator": "^5.0.0",
				"netmask": "^2.0.2"
			},
			"engines": {
				"node": ">= 14"
			}
		},
		"node_modules/parent-module": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/parent-module/-/parent-module-1.0.1.tgz",
			"integrity": "sha512-GQ2EWRpQV8/o+Aw8YqtfZZPfNRWZYkbidE9k5rpl/hC3vtHHBfGm2Ifi6qWV+coDGkrUKZAxE3Lot5kcsRlh+g==",
			"license": "MIT",
			"dependencies": {
				"callsites": "^3.0.0"
			},
			"engines": {
				"node": ">=6"
			}
		},
		"node_modules/parse-entities": {
			"version": "4.0.2",
			"resolved": "https://registry.npmjs.org/parse-entities/-/parse-entities-4.0.2.tgz",
			"integrity": "sha512-GG2AQYWoLgL877gQIKeRPGO1xF9+eG1ujIb5soS5gPvLQ1y2o8FL90w2QWNdf9I361Mpp7726c+lj3U0qK1uGw==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^2.0.0",
				"character-entities-legacy": "^3.0.0",
				"character-reference-invalid": "^2.0.0",
				"decode-named-character-reference": "^1.0.0",
				"is-alphanumerical": "^2.0.0",
				"is-decimal": "^2.0.0",
				"is-hexadecimal": "^2.0.0"
			},
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/parse-entities/node_modules/@types/unist": {
			"version": "2.0.11",
			"resolved": "https://registry.npmjs.org/@types/unist/-/unist-2.0.11.tgz",
			"integrity": "sha512-CmBKiL6NNo/OqgmMn95Fk9Whlp2mtvIv+KNpQKN2F4SjvrEesubTRWGYSg+BnWZOnlCaSTU1sMpsBOzgbYhnsA==",
			"license": "MIT"
		},
		"node_modules/parse-json": {
			"version": "5.2.0",
			"resolved": "https://registry.npmjs.org/parse-json/-/parse-json-5.2.0.tgz",
			"integrity": "sha512-ayCKvm/phCGxOkYRSCM82iDwct8/EonSEgCSxWxD7ve6jHggsFl4fZVQBPRNgQoKiuV/odhFrGzQXZwbifC8Rg==",
			"license": "MIT",
			"dependencies": {
				"@babel/code-frame": "^7.0.0",
				"error-ex": "^1.3.1",
				"json-parse-even-better-errors": "^2.3.0",
				"lines-and-columns": "^1.1.6"
			},
			"engines": {
				"node": ">=8"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/parse-latin": {
			"version": "7.0.0",
			"resolved": "https://registry.npmjs.org/parse-latin/-/parse-latin-7.0.0.tgz",
			"integrity": "sha512-mhHgobPPua5kZ98EF4HWiH167JWBfl4pvAIXXdbaVohtK7a6YBOy56kvhCqduqyo/f3yrHFWmqmiMg/BkBkYYQ==",
			"license": "MIT",
			"dependencies": {
				"@types/nlcst": "^2.0.0",
				"@types/unist": "^3.0.0",
				"nlcst-to-string": "^4.0.0",
				"unist-util-modify-children": "^4.0.0",
				"unist-util-visit-children": "^3.0.0",
				"vfile": "^6.0.0"
			},
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/parse5": {
			"version": "7.3.0",
			"resolved": "https://registry.npmjs.org/parse5/-/parse5-7.3.0.tgz",
			"integrity": "sha512-IInvU7fabl34qmi9gY8XOVxhYyMyuH2xUNpb2q8/Y+7552KlejkRvqvD19nMoUW/uQGGbqNpA6Tufu5FL5BZgw==",
			"license": "MIT",
			"dependencies": {
				"entities": "^6.0.0"
			},
			"funding": {
				"url": "https://github.com/inikulin/parse5?sponsor=1"
			}
		},
		"node_modules/parseurl": {
			"version": "1.3.3",
			"resolved": "https://registry.npmjs.org/parseurl/-/parseurl-1.3.3.tgz",
			"integrity": "sha512-CiyeOxFT/JZyN5m0z9PfXw4SCBJ6Sygz1Dpl0wqjlhDEGGBP1GnsUVEL0p63hoG1fcj3fHynXi9NYO4nWOL+qQ==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/patch-console": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/patch-console/-/patch-console-2.0.0.tgz",
			"integrity": "sha512-0YNdUceMdaQwoKce1gatDScmMo5pu/tfABfnzEqeG0gtTmd7mh/WcwgUjtAeOU7N8nFFlbQBnFK2gXW5fGvmMA==",
			"license": "MIT",
			"engines": {
				"node": "^12.20.0 || ^14.13.1 || >=16.0.0"
			}
		},
		"node_modules/path-parse": {
			"version": "1.0.7",
			"resolved": "https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz",
			"integrity": "sha512-LDJzPVEEEPR+y48z93A0Ed0yXb8pAByGWo/k5YYdYgpY2/2EsOsksJrq7lOHxryrVOn1ejG6oAp8ahvOIQD8sw==",
			"license": "MIT"
		},
		"node_modules/path-to-regexp": {
			"version": "0.1.12",
			"resolved": "https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-0.1.12.tgz",
			"integrity": "sha512-RA1GjUVMnvYFxuqovrEqZoxxW5NUZqbwKtYz/Tt7nXerk0LbLblQmrsgdeOxV5SFHf0UDggjS/bSeOZwt1pmEQ==",
			"license": "MIT"
		},
		"node_modules/pend": {
			"version": "1.2.0",
			"resolved": "https://registry.npmjs.org/pend/-/pend-1.2.0.tgz",
			"integrity": "sha512-F3asv42UuXchdzt+xXqfW1OGlVBe+mxa2mqI0pg5yAHZPvFmY3Y6drSf/GQ1A86WgWEN9Kzh/WrgKa6iGcHXLg==",
			"license": "MIT"
		},
		"node_modules/picocolors": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz",
			"integrity": "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==",
			"license": "ISC"
		},
		"node_modules/picomatch": {
			"version": "2.3.1",
			"resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.3.1.tgz",
			"integrity": "sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA==",
			"license": "MIT",
			"engines": {
				"node": ">=8.6"
			},
			"funding": {
				"url": "https://github.com/sponsors/jonschlinkert"
			}
		},
		"node_modules/pify": {
			"version": "2.3.0",
			"resolved": "https://registry.npmjs.org/pify/-/pify-2.3.0.tgz",
			"integrity": "sha512-udgsAY+fTnvv7kI7aaxbqwWNb0AHiB0qBO89PZKPkoTmGOgdbrHDKD+0B2X4uTfJ/FT1R09r9gTsjUjNJotuog==",
			"license": "MIT",
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/pirates": {
			"version": "4.0.7",
			"resolved": "https://registry.npmjs.org/pirates/-/pirates-4.0.7.tgz",
			"integrity": "sha512-TfySrs/5nm8fQJDcBDuUng3VOUKsd7S+zqvbOTiGXHfxX4wK31ard+hoNuvkicM/2YFzlpDgABOevKSsB4G/FA==",
			"license": "MIT",
			"engines": {
				"node": ">= 6"
			}
		},
		"node_modules/pony-cause": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/pony-cause/-/pony-cause-1.1.1.tgz",
			"integrity": "sha512-PxkIc/2ZpLiEzQXu5YRDOUgBlfGYBY8156HY5ZcRAwwonMk5W/MrJP2LLkG/hF7GEQzaHo2aS7ho6ZLCOvf+6g==",
			"license": "0BSD",
			"engines": {
				"node": ">=12.0.0"
			}
		},
		"node_modules/possible-typed-array-names": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/possible-typed-array-names/-/possible-typed-array-names-1.1.0.tgz",
			"integrity": "sha512-/+5VFTchJDoVj3bhoqi6UeymcD00DAwb1nJwamzPvHEszJ4FpF6SNNbUbOS8yI56qHzdV8eK0qEfOSiodkTdxg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/postcss": {
			"version": "8.5.6",
			"resolved": "https://registry.npmjs.org/postcss/-/postcss-8.5.6.tgz",
			"integrity": "sha512-3Ybi1tAuwAP9s0r1UQ2J4n5Y0G05bJkpUIO0/bI9MhwmD70S5aTWbXGBwxHrelT+XM1k6dM0pk+SwNkpTRN7Pg==",
			"funding": [
				{
					"type": "opencollective",
					"url": "https://opencollective.com/postcss/"
				},
				{
					"type": "tidelift",
					"url": "https://tidelift.com/funding/github/npm/postcss"
				},
				{
					"type": "github",
					"url": "https://github.com/sponsors/ai"
				}
			],
			"license": "MIT",
			"dependencies": {
				"nanoid": "^3.3.11",
				"picocolors": "^1.1.1",
				"source-map-js": "^1.2.1"
			},
			"engines": {
				"node": "^10 || ^12 || >=14"
			}
		},
		"node_modules/postcss-import": {
			"version": "15.1.0",
			"resolved": "https://registry.npmjs.org/postcss-import/-/postcss-import-15.1.0.tgz",
			"integrity": "sha512-hpr+J05B2FVYUAXHeK1YyI267J/dDDhMU6B6civm8hSY1jYJnBXxzKDKDswzJmtLHryrjhnDjqqp/49t8FALew==",
			"license": "MIT",
			"dependencies": {
				"postcss-value-parser": "^4.0.0",
				"read-cache": "^1.0.0",
				"resolve": "^1.1.7"
			},
			"engines": {
				"node": ">=14.0.0"
			},
			"peerDependencies": {
				"postcss": "^8.0.0"
			}
		},
		"node_modules/postcss-js": {
			"version": "4.1.0",
			"resolved": "https://registry.npmjs.org/postcss-js/-/postcss-js-4.1.0.tgz",
			"integrity": "sha512-oIAOTqgIo7q2EOwbhb8UalYePMvYoIeRY2YKntdpFQXNosSu3vLrniGgmH9OKs/qAkfoj5oB3le/7mINW1LCfw==",
			"funding": [
				{
					"type": "opencollective",
					"url": "https://opencollective.com/postcss/"
				},
				{
					"type": "github",
					"url": "https://github.com/sponsors/ai"
				}
			],
			"license": "MIT",
			"dependencies": {
				"camelcase-css": "^2.0.1"
			},
			"engines": {
				"node": "^12 || ^14 || >= 16"
			},
			"peerDependencies": {
				"postcss": "^8.4.21"
			}
		},
		"node_modules/postcss-load-config": {
			"version": "4.0.2",
			"resolved": "https://registry.npmjs.org/postcss-load-config/-/postcss-load-config-4.0.2.tgz",
			"integrity": "sha512-bSVhyJGL00wMVoPUzAVAnbEoWyqRxkjv64tUl427SKnPrENtq6hJwUojroMz2VB+Q1edmi4IfrAPpami5VVgMQ==",
			"funding": [
				{
					"type": "opencollective",
					"url": "https://opencollective.com/postcss/"
				},
				{
					"type": "github",
					"url": "https://github.com/sponsors/ai"
				}
			],
			"license": "MIT",
			"dependencies": {
				"lilconfig": "^3.0.0",
				"yaml": "^2.3.4"
			},
			"engines": {
				"node": ">= 14"
			},
			"peerDependencies": {
				"postcss": ">=8.0.9",
				"ts-node": ">=9.0.0"
			},
			"peerDependenciesMeta": {
				"postcss": {
					"optional": true
				},
				"ts-node": {
					"optional": true
				}
			}
		},
		"node_modules/postcss-load-config/node_modules/lilconfig": {
			"version": "3.1.3",
			"resolved": "https://registry.npmjs.org/lilconfig/-/lilconfig-3.1.3.tgz",
			"integrity": "sha512-/vlFKAoH5Cgt3Ie+JLhRbwOsCQePABiU3tJ1egGvyQ+33R/vcwM2Zl2QR/LzjsBeItPt3oSVXapn+m4nQDvpzw==",
			"license": "MIT",
			"engines": {
				"node": ">=14"
			},
			"funding": {
				"url": "https://github.com/sponsors/antonk52"
			}
		},
		"node_modules/postcss-nested": {
			"version": "6.2.0",
			"resolved": "https://registry.npmjs.org/postcss-nested/-/postcss-nested-6.2.0.tgz",
			"integrity": "sha512-HQbt28KulC5AJzG+cZtj9kvKB93CFCdLvog1WFLf1D+xmMvPGlBstkpTEZfK5+AN9hfJocyBFCNiqyS48bpgzQ==",
			"funding": [
				{
					"type": "opencollective",
					"url": "https://opencollective.com/postcss/"
				},
				{
					"type": "github",
					"url": "https://github.com/sponsors/ai"
				}
			],
			"license": "MIT",
			"dependencies": {
				"postcss-selector-parser": "^6.1.1"
			},
			"engines": {
				"node": ">=12.0"
			},
			"peerDependencies": {
				"postcss": "^8.2.14"
			}
		},
		"node_modules/postcss-selector-parser": {
			"version": "6.1.2",
			"resolved": "https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-6.1.2.tgz",
			"integrity": "sha512-Q8qQfPiZ+THO/3ZrOrO0cJJKfpYCagtMUkXbnEfmgUjwXg6z/WBeOyS9APBBPCTSiDV+s4SwQGu8yFsiMRIudg==",
			"license": "MIT",
			"dependencies": {
				"cssesc": "^3.0.0",
				"util-deprecate": "^1.0.2"
			},
			"engines": {
				"node": ">=4"
			}
		},
		"node_modules/postcss-value-parser": {
			"version": "4.2.0",
			"resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-4.2.0.tgz",
			"integrity": "sha512-1NNCs6uurfkVbeXG4S8JFT9t19m45ICnif8zWLd5oPSZ50QnwMfK+H3jv408d4jw/7Bttv5axS5IiHoLaVNHeQ==",
			"license": "MIT"
		},
		"node_modules/progress": {
			"version": "2.0.3",
			"resolved": "https://registry.npmjs.org/progress/-/progress-2.0.3.tgz",
			"integrity": "sha512-7PiHtLll5LdnKIMw100I+8xJXR5gW2QwWYkT6iJva0bXitZKa/XMrSbdmg3r2Xnaidz9Qumd0VPaMrZlF9V9sA==",
			"license": "MIT",
			"engines": {
				"node": ">=0.4.0"
			}
		},
		"node_modules/property-information": {
			"version": "7.1.0",
			"resolved": "https://registry.npmjs.org/property-information/-/property-information-7.1.0.tgz",
			"integrity": "sha512-TwEZ+X+yCJmYfL7TPUOcvBZ4QfoT5YenQiJuX//0th53DE6w0xxLEtfK3iyryQFddXuvkIk51EEgrJQ0WJkOmQ==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/proxy-addr": {
			"version": "2.0.7",
			"resolved": "https://registry.npmjs.org/proxy-addr/-/proxy-addr-2.0.7.tgz",
			"integrity": "sha512-llQsMLSUDUPT44jdrU/O37qlnifitDP+ZwrmmZcoSKyLKvtZxpyV0n2/bD/N4tBAAZ/gJEdZU7KMraoK1+XYAg==",
			"license": "MIT",
			"dependencies": {
				"forwarded": "0.2.0",
				"ipaddr.js": "1.9.1"
			},
			"engines": {
				"node": ">= 0.10"
			}
		},
		"node_modules/proxy-agent": {
			"version": "6.5.0",
			"resolved": "https://registry.npmjs.org/proxy-agent/-/proxy-agent-6.5.0.tgz",
			"integrity": "sha512-TmatMXdr2KlRiA2CyDu8GqR8EjahTG3aY3nXjdzFyoZbmB8hrBsTyMezhULIXKnC0jpfjlmiZ3+EaCzoInSu/A==",
			"license": "MIT",
			"dependencies": {
				"agent-base": "^7.1.2",
				"debug": "^4.3.4",
				"http-proxy-agent": "^7.0.1",
				"https-proxy-agent": "^7.0.6",
				"lru-cache": "^7.14.1",
				"pac-proxy-agent": "^7.1.0",
				"proxy-from-env": "^1.1.0",
				"socks-proxy-agent": "^8.0.5"
			},
			"engines": {
				"node": ">= 14"
			}
		},
		"node_modules/proxy-from-env": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/proxy-from-env/-/proxy-from-env-1.1.0.tgz",
			"integrity": "sha512-D+zkORCbA9f1tdWRK0RaCR3GPv50cMxcrz4X8k5LTSUD1Dkw47mKJEZQNunItRTkWwgtaUSo1RVFRIG9ZXiFYg==",
			"license": "MIT"
		},
		"node_modules/public-ip": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/public-ip/-/public-ip-5.0.0.tgz",
			"integrity": "sha512-xaH3pZMni/R2BG7ZXXaWS9Wc9wFlhyDVJF47IJ+3ali0TGv+2PsckKxbmo+rnx3ZxiV2wblVhtdS3bohAP6GGw==",
			"license": "MIT",
			"dependencies": {
				"dns-socket": "^4.2.2",
				"got": "^12.0.0",
				"is-ip": "^3.1.0"
			},
			"engines": {
				"node": "^14.13.1 || >=16.0.0"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/public-ip/node_modules/got": {
			"version": "12.6.1",
			"resolved": "https://registry.npmjs.org/got/-/got-12.6.1.tgz",
			"integrity": "sha512-mThBblvlAF1d4O5oqyvN+ZxLAYwIJK7bpMxgYqPD9okW0C3qm5FFn7k811QrcuEBwaogR3ngOFoCfs6mRv7teQ==",
			"license": "MIT",
			"dependencies": {
				"@sindresorhus/is": "^5.2.0",
				"@szmarczak/http-timer": "^5.0.1",
				"cacheable-lookup": "^7.0.0",
				"cacheable-request": "^10.2.8",
				"decompress-response": "^6.0.0",
				"form-data-encoder": "^2.1.2",
				"get-stream": "^6.0.1",
				"http2-wrapper": "^2.1.10",
				"lowercase-keys": "^3.0.0",
				"p-cancelable": "^3.0.0",
				"responselike": "^3.0.0"
			},
			"engines": {
				"node": ">=14.16"
			},
			"funding": {
				"url": "https://github.com/sindresorhus/got?sponsor=1"
			}
		},
		"node_modules/pump": {
			"version": "3.0.3",
			"resolved": "https://registry.npmjs.org/pump/-/pump-3.0.3.tgz",
			"integrity": "sha512-todwxLMY7/heScKmntwQG8CXVkWUOdYxIvY2s0VWAAMh/nd8SoYiRaKjlr7+iCs984f2P8zvrfWcDDYVb73NfA==",
			"license": "MIT",
			"dependencies": {
				"end-of-stream": "^1.1.0",
				"once": "^1.3.1"
			}
		},
		"node_modules/puppeteer": {
			"version": "22.14.0",
			"resolved": "https://registry.npmjs.org/puppeteer/-/puppeteer-22.14.0.tgz",
			"integrity": "sha512-MGTR6/pM8zmWbTdazb6FKnwIihzsSEXBPH49mFFU96DNZpQOevCAZMnjBZGlZRGRzRK6aADCavR6SQtrbv5dQw==",
			"deprecated": "< 24.15.0 is no longer supported",
			"hasInstallScript": true,
			"license": "Apache-2.0",
			"dependencies": {
				"@puppeteer/browsers": "2.3.0",
				"cosmiconfig": "^9.0.0",
				"devtools-protocol": "0.0.1312386",
				"puppeteer-core": "22.14.0"
			},
			"bin": {
				"puppeteer": "lib/esm/puppeteer/node/cli.js"
			},
			"engines": {
				"node": ">=18"
			}
		},
		"node_modules/puppeteer-core": {
			"version": "22.14.0",
			"resolved": "https://registry.npmjs.org/puppeteer-core/-/puppeteer-core-22.14.0.tgz",
			"integrity": "sha512-rl4tOY5LcA3e374GAlsGGHc05HL3eGNf5rZ+uxkl6id9zVZKcwcp1Z+Nd6byb6WPiPeecT/dwz8f/iUm+AZQSw==",
			"license": "Apache-2.0",
			"dependencies": {
				"@puppeteer/browsers": "2.3.0",
				"chromium-bidi": "0.6.2",
				"debug": "^4.3.5",
				"devtools-protocol": "0.0.1312386",
				"ws": "^8.18.0"
			},
			"engines": {
				"node": ">=18"
			}
		},
		"node_modules/qs": {
			"version": "6.14.1",
			"resolved": "https://registry.npmjs.org/qs/-/qs-6.14.1.tgz",
			"integrity": "sha512-4EK3+xJl8Ts67nLYNwqw/dsFVnCf+qR7RgXSK9jEEm9unao3njwMDdmsdvoKBKHzxd7tCYz5e5M+SnMjdtXGQQ==",
			"license": "BSD-3-Clause",
			"dependencies": {
				"side-channel": "^1.1.0"
			},
			"engines": {
				"node": ">=0.6"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/queue-microtask": {
			"version": "1.2.3",
			"resolved": "https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz",
			"integrity": "sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A==",
			"funding": [
				{
					"type": "github",
					"url": "https://github.com/sponsors/feross"
				},
				{
					"type": "patreon",
					"url": "https://www.patreon.com/feross"
				},
				{
					"type": "consulting",
					"url": "https://feross.org/support"
				}
			],
			"license": "MIT"
		},
		"node_modules/quick-lru": {
			"version": "5.1.1",
			"resolved": "https://registry.npmjs.org/quick-lru/-/quick-lru-5.1.1.tgz",
			"integrity": "sha512-WuyALRjWPDGtt/wzJiadO5AXY+8hZ80hVpe6MyivgraREW751X3SbhRvG3eLKOYN+8VEvqLcf3wdnt44Z4S4SA==",
			"license": "MIT",
			"engines": {
				"node": ">=10"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/range-parser": {
			"version": "1.2.1",
			"resolved": "https://registry.npmjs.org/range-parser/-/range-parser-1.2.1.tgz",
			"integrity": "sha512-Hrgsx+orqoygnmhFbKaHE6c296J+HTAQXoxEF6gNupROmmGJRoyzfG3ccAveqCBrwr/2yxQ5BVd/GTl5agOwSg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/raw-body": {
			"version": "2.5.2",
			"resolved": "https://registry.npmjs.org/raw-body/-/raw-body-2.5.2.tgz",
			"integrity": "sha512-8zGqypfENjCIqGhgXToC8aB2r7YrBX+AQAfIPs/Mlk+BtPTztOvTS01NRW/3Eh60J+a48lt8qsCzirQ6loCVfA==",
			"license": "MIT",
			"dependencies": {
				"bytes": "3.1.2",
				"http-errors": "2.0.0",
				"iconv-lite": "0.4.24",
				"unpipe": "1.0.0"
			},
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/raw-body/node_modules/iconv-lite": {
			"version": "0.4.24",
			"resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz",
			"integrity": "sha512-v3MXnZAcvnywkTUEZomIActle7RXXeedOR31wwl7VlyoXO4Qi9arvSenNQWne1TcRwhCL1HwLI21bEqdpj8/rA==",
			"license": "MIT",
			"dependencies": {
				"safer-buffer": ">= 2.1.2 < 3"
			},
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/react": {
			"version": "19.2.3",
			"resolved": "https://registry.npmjs.org/react/-/react-19.2.3.tgz",
			"integrity": "sha512-Ku/hhYbVjOQnXDZFv2+RibmLFGwFdeeKHFcOTlrt7xplBnya5OGn/hIRDsqDiSUcfORsDC7MPxwork8jBwsIWA==",
			"license": "MIT",
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/react-reconciler": {
			"version": "0.32.0",
			"resolved": "https://registry.npmjs.org/react-reconciler/-/react-reconciler-0.32.0.tgz",
			"integrity": "sha512-2NPMOzgTlG0ZWdIf3qG+dcbLSoAc/uLfOwckc3ofy5sSK0pLJqnQLpUFxvGcN2rlXSjnVtGeeFLNimCQEj5gOQ==",
			"license": "MIT",
			"dependencies": {
				"scheduler": "^0.26.0"
			},
			"engines": {
				"node": ">=0.10.0"
			},
			"peerDependencies": {
				"react": "^19.1.0"
			}
		},
		"node_modules/react-remove-scroll": {
			"version": "2.7.2",
			"resolved": "https://registry.npmjs.org/react-remove-scroll/-/react-remove-scroll-2.7.2.tgz",
			"integrity": "sha512-Iqb9NjCCTt6Hf+vOdNIZGdTiH1QSqr27H/Ek9sv/a97gfueI/5h1s3yRi1nngzMUaOOToin5dI1dXKdXiF+u0Q==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"react-remove-scroll-bar": "^2.3.7",
				"react-style-singleton": "^2.2.3",
				"tslib": "^2.1.0",
				"use-callback-ref": "^1.3.3",
				"use-sidecar": "^1.1.3"
			},
			"engines": {
				"node": ">=10"
			},
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/react-remove-scroll-bar": {
			"version": "2.3.8",
			"resolved": "https://registry.npmjs.org/react-remove-scroll-bar/-/react-remove-scroll-bar-2.3.8.tgz",
			"integrity": "sha512-9r+yi9+mgU33AKcj6IbT9oRCO78WriSj6t/cF8DWBZJ9aOGPOTEDvdUDz1FwKim7QXWwmHqtdHnRJfhAxEG46Q==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"react-style-singleton": "^2.2.2",
				"tslib": "^2.0.0"
			},
			"engines": {
				"node": ">=10"
			},
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/react-remove-scroll-bar/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD",
			"peer": true
		},
		"node_modules/react-remove-scroll/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD",
			"peer": true
		},
		"node_modules/react-style-singleton": {
			"version": "2.2.3",
			"resolved": "https://registry.npmjs.org/react-style-singleton/-/react-style-singleton-2.2.3.tgz",
			"integrity": "sha512-b6jSvxvVnyptAiLjbkWLE/lOnR4lfTtDAl+eUC7RZy+QQWc6wRzIV2CE6xBuMmDxc2qIihtDCZD5NPOFl7fRBQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"get-nonce": "^1.0.0",
				"tslib": "^2.0.0"
			},
			"engines": {
				"node": ">=10"
			},
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/react-style-singleton/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD",
			"peer": true
		},
		"node_modules/read-cache": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/read-cache/-/read-cache-1.0.0.tgz",
			"integrity": "sha512-Owdv/Ft7IjOgm/i0xvNDZ1LrRANRfew4b2prF3OWMQLxLfu3bS8FVhCsrSCMK4lR56Y9ya+AThoTpDCTxCmpRA==",
			"license": "MIT",
			"dependencies": {
				"pify": "^2.3.0"
			}
		},
		"node_modules/readdirp": {
			"version": "3.6.0",
			"resolved": "https://registry.npmjs.org/readdirp/-/readdirp-3.6.0.tgz",
			"integrity": "sha512-hOS089on8RduqdbhvQ5Z37A0ESjsqz6qnRcffsMU3495FuTdqSm+7bhJ29JvIOsBDEEnan5DPu9t3To9VRlMzA==",
			"license": "MIT",
			"dependencies": {
				"picomatch": "^2.2.1"
			},
			"engines": {
				"node": ">=8.10.0"
			}
		},
		"node_modules/recma-build-jsx": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/recma-build-jsx/-/recma-build-jsx-1.0.0.tgz",
			"integrity": "sha512-8GtdyqaBcDfva+GUKDr3nev3VpKAhup1+RvkMvUxURHpW7QyIvk9F5wz7Vzo06CEMSilw6uArgRqhpiUcWp8ew==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0",
				"estree-util-build-jsx": "^3.0.0",
				"vfile": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/recma-jsx": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/recma-jsx/-/recma-jsx-1.0.1.tgz",
			"integrity": "sha512-huSIy7VU2Z5OLv6oFLosQGGDqPqdO1iq6bWNAdhzMxSJP7RAso4fCZ1cKu8j9YHCZf3TPrq4dw3okhrylgcd7w==",
			"license": "MIT",
			"dependencies": {
				"acorn-jsx": "^5.0.0",
				"estree-util-to-js": "^2.0.0",
				"recma-parse": "^1.0.0",
				"recma-stringify": "^1.0.0",
				"unified": "^11.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			},
			"peerDependencies": {
				"acorn": "^6.0.0 || ^7.0.0 || ^8.0.0"
			}
		},
		"node_modules/recma-parse": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/recma-parse/-/recma-parse-1.0.0.tgz",
			"integrity": "sha512-OYLsIGBB5Y5wjnSnQW6t3Xg7q3fQ7FWbw/vcXtORTnyaSFscOtABg+7Pnz6YZ6c27fG1/aN8CjfwoUEUIdwqWQ==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0",
				"esast-util-from-js": "^2.0.0",
				"unified": "^11.0.0",
				"vfile": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/recma-stringify": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/recma-stringify/-/recma-stringify-1.0.0.tgz",
			"integrity": "sha512-cjwII1MdIIVloKvC9ErQ+OgAtwHBmcZ0Bg4ciz78FtbT8In39aAYbaA7zvxQ61xVMSPE8WxhLwLbhif4Js2C+g==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0",
				"estree-util-to-js": "^2.0.0",
				"unified": "^11.0.0",
				"vfile": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/reflect.getprototypeof": {
			"version": "1.0.10",
			"resolved": "https://registry.npmjs.org/reflect.getprototypeof/-/reflect.getprototypeof-1.0.10.tgz",
			"integrity": "sha512-00o4I+DVrefhv+nX0ulyi3biSHCPDe+yLv5o/p6d/UVlirijB8E16FtfwSAi4g3tcqrQ4lRAqQSoFEZJehYEcw==",
			"license": "MIT",
			"dependencies": {
				"call-bind": "^1.0.8",
				"define-properties": "^1.2.1",
				"es-abstract": "^1.23.9",
				"es-errors": "^1.3.0",
				"es-object-atoms": "^1.0.0",
				"get-intrinsic": "^1.2.7",
				"get-proto": "^1.0.1",
				"which-builtin-type": "^1.2.1"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/regex": {
			"version": "6.1.0",
			"resolved": "https://registry.npmjs.org/regex/-/regex-6.1.0.tgz",
			"integrity": "sha512-6VwtthbV4o/7+OaAF9I5L5V3llLEsoPyq9P1JVXkedTP33c7MfCG0/5NOPcSJn0TzXcG9YUrR0gQSWioew3LDg==",
			"license": "MIT",
			"dependencies": {
				"regex-utilities": "^2.3.0"
			}
		},
		"node_modules/regex-recursion": {
			"version": "6.0.2",
			"resolved": "https://registry.npmjs.org/regex-recursion/-/regex-recursion-6.0.2.tgz",
			"integrity": "sha512-0YCaSCq2VRIebiaUviZNs0cBz1kg5kVS2UKUfNIx8YVs1cN3AV7NTctO5FOKBA+UT2BPJIWZauYHPqJODG50cg==",
			"license": "MIT",
			"dependencies": {
				"regex-utilities": "^2.3.0"
			}
		},
		"node_modules/regex-utilities": {
			"version": "2.3.0",
			"resolved": "https://registry.npmjs.org/regex-utilities/-/regex-utilities-2.3.0.tgz",
			"integrity": "sha512-8VhliFJAWRaUiVvREIiW2NXXTmHs4vMNnSzuJVhscgmGav3g9VDxLrQndI3dZZVVdp0ZO/5v0xmX516/7M9cng==",
			"license": "MIT"
		},
		"node_modules/regexp.prototype.flags": {
			"version": "1.5.4",
			"resolved": "https://registry.npmjs.org/regexp.prototype.flags/-/regexp.prototype.flags-1.5.4.tgz",
			"integrity": "sha512-dYqgNSZbDwkaJ2ceRd9ojCGjBq+mOm9LmtXnAnEGyHhN/5R7iDW2TRw3h+o/jCFxus3P2LfWIIiwowAjANm7IA==",
			"license": "MIT",
			"dependencies": {
				"call-bind": "^1.0.8",
				"define-properties": "^1.2.1",
				"es-errors": "^1.3.0",
				"get-proto": "^1.0.1",
				"gopd": "^1.2.0",
				"set-function-name": "^2.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/rehype-katex": {
			"version": "7.0.1",
			"resolved": "https://registry.npmjs.org/rehype-katex/-/rehype-katex-7.0.1.tgz",
			"integrity": "sha512-OiM2wrZ/wuhKkigASodFoo8wimG3H12LWQaH8qSPVJn9apWKFSH3YOCtbKpBorTVw/eI7cuT21XBbvwEswbIOA==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"@types/katex": "^0.16.0",
				"hast-util-from-html-isomorphic": "^2.0.0",
				"hast-util-to-text": "^4.0.0",
				"katex": "^0.16.0",
				"unist-util-visit-parents": "^6.0.0",
				"vfile": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/rehype-minify-whitespace": {
			"version": "6.0.2",
			"resolved": "https://registry.npmjs.org/rehype-minify-whitespace/-/rehype-minify-whitespace-6.0.2.tgz",
			"integrity": "sha512-Zk0pyQ06A3Lyxhe9vGtOtzz3Z0+qZ5+7icZ/PL/2x1SHPbKao5oB/g/rlc6BCTajqBb33JcOe71Ye1oFsuYbnw==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"hast-util-minify-whitespace": "^1.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/rehype-parse": {
			"version": "9.0.1",
			"resolved": "https://registry.npmjs.org/rehype-parse/-/rehype-parse-9.0.1.tgz",
			"integrity": "sha512-ksCzCD0Fgfh7trPDxr2rSylbwq9iYDkSn8TCDmEJ49ljEUBxDVCzCHv7QNzZOfODanX4+bWQ4WZqLCRWYLfhag==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"hast-util-from-html": "^2.0.0",
				"unified": "^11.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/rehype-recma": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/rehype-recma/-/rehype-recma-1.0.0.tgz",
			"integrity": "sha512-lqA4rGUf1JmacCNWWZx0Wv1dHqMwxzsDWYMTowuplHF3xH0N/MmrZ/G3BDZnzAkRmxDadujCjaKM2hqYdCBOGw==",
			"license": "MIT",
			"dependencies": {
				"@types/estree": "^1.0.0",
				"@types/hast": "^3.0.0",
				"hast-util-to-estree": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/rehype-stringify": {
			"version": "10.0.1",
			"resolved": "https://registry.npmjs.org/rehype-stringify/-/rehype-stringify-10.0.1.tgz",
			"integrity": "sha512-k9ecfXHmIPuFVI61B9DeLPN0qFHfawM6RsuX48hoqlaKSF61RskNjSm1lI8PhBEM0MRdLxVVm4WmTqJQccH9mA==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"hast-util-to-html": "^9.0.0",
				"unified": "^11.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/remark": {
			"version": "15.0.1",
			"resolved": "https://registry.npmjs.org/remark/-/remark-15.0.1.tgz",
			"integrity": "sha512-Eht5w30ruCXgFmxVUSlNWQ9iiimq07URKeFS3hNc8cUWy1llX4KDWfyEDZRycMc+znsN9Ux5/tJ/BFdgdOwA3A==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"remark-parse": "^11.0.0",
				"remark-stringify": "^11.0.0",
				"unified": "^11.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/remark-frontmatter": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/remark-frontmatter/-/remark-frontmatter-5.0.0.tgz",
			"integrity": "sha512-XTFYvNASMe5iPN0719nPrdItC9aU0ssC4v14mH1BCi1u0n1gAocqcujWUrByftZTbLhRtiKRyjYTSIOcr69UVQ==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"mdast-util-frontmatter": "^2.0.0",
				"micromark-extension-frontmatter": "^2.0.0",
				"unified": "^11.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/remark-gfm": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/remark-gfm/-/remark-gfm-4.0.0.tgz",
			"integrity": "sha512-U92vJgBPkbw4Zfu/IiW2oTZLSL3Zpv+uI7My2eq8JxKgqraFdU8YUGicEJCEgSbeaG+QDFqIcwwfMTOEelPxuA==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"mdast-util-gfm": "^3.0.0",
				"micromark-extension-gfm": "^3.0.0",
				"remark-parse": "^11.0.0",
				"remark-stringify": "^11.0.0",
				"unified": "^11.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/remark-math": {
			"version": "6.0.0",
			"resolved": "https://registry.npmjs.org/remark-math/-/remark-math-6.0.0.tgz",
			"integrity": "sha512-MMqgnP74Igy+S3WwnhQ7kqGlEerTETXMvJhrUzDikVZ2/uogJCb+WHUg97hK9/jcfc0dkD73s3LN8zU49cTEtA==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"mdast-util-math": "^3.0.0",
				"micromark-extension-math": "^3.0.0",
				"unified": "^11.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/remark-mdx": {
			"version": "3.1.0",
			"resolved": "https://registry.npmjs.org/remark-mdx/-/remark-mdx-3.1.0.tgz",
			"integrity": "sha512-Ngl/H3YXyBV9RcRNdlYsZujAmhsxwzxpDzpDEhFBVAGthS4GDgnctpDjgFl/ULx5UEDzqtW1cyBSNKqYYrqLBA==",
			"license": "MIT",
			"dependencies": {
				"mdast-util-mdx": "^3.0.0",
				"micromark-extension-mdxjs": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/remark-mdx-remove-esm": {
			"version": "1.2.2",
			"resolved": "https://registry.npmjs.org/remark-mdx-remove-esm/-/remark-mdx-remove-esm-1.2.2.tgz",
			"integrity": "sha512-YSaUwqiuJuD6S9XTAD6zmO4JJJZJgsRAdsl2drZO8/ssAVv0HXAg4vkSgHZAP46ORh8ERPFQrC7JWlbkwBwu1A==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.4",
				"mdast-util-mdxjs-esm": "^2.0.1",
				"unist-util-remove": "^4.0.0"
			},
			"peerDependencies": {
				"unified": "^11"
			}
		},
		"node_modules/remark-parse": {
			"version": "11.0.0",
			"resolved": "https://registry.npmjs.org/remark-parse/-/remark-parse-11.0.0.tgz",
			"integrity": "sha512-FCxlKLNGknS5ba/1lmpYijMUzX2esxW5xQqjWxw2eHFfS2MSdaHVINFmhjo+qN1WhZhNimq0dZATN9pH0IDrpA==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"mdast-util-from-markdown": "^2.0.0",
				"micromark-util-types": "^2.0.0",
				"unified": "^11.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/remark-rehype": {
			"version": "11.1.1",
			"resolved": "https://registry.npmjs.org/remark-rehype/-/remark-rehype-11.1.1.tgz",
			"integrity": "sha512-g/osARvjkBXb6Wo0XvAeXQohVta8i84ACbenPpoSsxTOQH/Ae0/RGP4WZgnMH5pMLpsj4FG7OHmcIcXxpza8eQ==",
			"license": "MIT",
			"dependencies": {
				"@types/hast": "^3.0.0",
				"@types/mdast": "^4.0.0",
				"mdast-util-to-hast": "^13.0.0",
				"unified": "^11.0.0",
				"vfile": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/remark-smartypants": {
			"version": "3.0.2",
			"resolved": "https://registry.npmjs.org/remark-smartypants/-/remark-smartypants-3.0.2.tgz",
			"integrity": "sha512-ILTWeOriIluwEvPjv67v7Blgrcx+LZOkAUVtKI3putuhlZm84FnqDORNXPPm+HY3NdZOMhyDwZ1E+eZB/Df5dA==",
			"license": "MIT",
			"dependencies": {
				"retext": "^9.0.0",
				"retext-smartypants": "^6.0.0",
				"unified": "^11.0.4",
				"unist-util-visit": "^5.0.0"
			},
			"engines": {
				"node": ">=16.0.0"
			}
		},
		"node_modules/remark-stringify": {
			"version": "11.0.0",
			"resolved": "https://registry.npmjs.org/remark-stringify/-/remark-stringify-11.0.0.tgz",
			"integrity": "sha512-1OSmLd3awB/t8qdoEOMazZkNsfVTeY4fTsgzcQFdXNq8ToTN4ZGwrMnlda4K6smTFKD+GRV6O48i6Z4iKgPPpw==",
			"license": "MIT",
			"dependencies": {
				"@types/mdast": "^4.0.0",
				"mdast-util-to-markdown": "^2.0.0",
				"unified": "^11.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/require-directory": {
			"version": "2.1.1",
			"resolved": "https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz",
			"integrity": "sha512-fGxEI7+wsG9xrvdjsrlmL22OMTTiHRwAMroiEeMgq8gzoLC/PQr7RsRDSTLUg/bZAZtF+TVIkHc6/4RIKrui+Q==",
			"license": "MIT",
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/require-from-string": {
			"version": "2.0.2",
			"resolved": "https://registry.npmjs.org/require-from-string/-/require-from-string-2.0.2.tgz",
			"integrity": "sha512-Xf0nWe6RseziFMu+Ap9biiUbmplq6S9/p+7w7YXP/JBHhrUDDUhwa+vANyubuqfZWTveU//DYVGsDG7RKL/vEw==",
			"license": "MIT",
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/resolve": {
			"version": "1.22.11",
			"resolved": "https://registry.npmjs.org/resolve/-/resolve-1.22.11.tgz",
			"integrity": "sha512-RfqAvLnMl313r7c9oclB1HhUEAezcpLjz95wFH4LVuhk9JF/r22qmVP9AMmOU4vMX7Q8pN8jwNg/CSpdFnMjTQ==",
			"license": "MIT",
			"dependencies": {
				"is-core-module": "^2.16.1",
				"path-parse": "^1.0.7",
				"supports-preserve-symlinks-flag": "^1.0.0"
			},
			"bin": {
				"resolve": "bin/resolve"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/resolve-alpn": {
			"version": "1.2.1",
			"resolved": "https://registry.npmjs.org/resolve-alpn/-/resolve-alpn-1.2.1.tgz",
			"integrity": "sha512-0a1F4l73/ZFZOakJnQ3FvkJ2+gSTQWz/r2KE5OdDY0TxPm5h4GkqkWWfM47T7HsbnOtcJVEF4epCVy6u7Q3K+g==",
			"license": "MIT"
		},
		"node_modules/resolve-from": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/resolve-from/-/resolve-from-4.0.0.tgz",
			"integrity": "sha512-pb/MYmXstAkysRFx8piNI1tGFNQIFA3vkE3Gq4EuA1dF6gHp/+vgZqsCGJapvy8N3Q+4o7FwvquPJcnZ7RYy4g==",
			"license": "MIT",
			"engines": {
				"node": ">=4"
			}
		},
		"node_modules/responselike": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/responselike/-/responselike-3.0.0.tgz",
			"integrity": "sha512-40yHxbNcl2+rzXvZuVkrYohathsSJlMTXKryG5y8uciHv1+xDLHQpgjG64JUO9nrEq2jGLH6IZ8BcZyw3wrweg==",
			"license": "MIT",
			"dependencies": {
				"lowercase-keys": "^3.0.0"
			},
			"engines": {
				"node": ">=14.16"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/restore-cursor": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/restore-cursor/-/restore-cursor-4.0.0.tgz",
			"integrity": "sha512-I9fPXU9geO9bHOt9pHHOhOkYerIMsmVaWB0rA2AI9ERh/+x/i7MV5HKBNrg+ljO5eoPVgCcnFuRjJ9uH6I/3eg==",
			"license": "MIT",
			"dependencies": {
				"onetime": "^5.1.0",
				"signal-exit": "^3.0.2"
			},
			"engines": {
				"node": "^12.20.0 || ^14.13.1 || >=16.0.0"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/restore-cursor/node_modules/signal-exit": {
			"version": "3.0.7",
			"resolved": "https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.7.tgz",
			"integrity": "sha512-wnD2ZE+l+SPC/uoS0vXeE9L1+0wuaMqKlfz9AMUo38JsyLSBWSFcHR1Rri62LZc12vLr1gb3jl7iwQhgwpAbGQ==",
			"license": "ISC"
		},
		"node_modules/retext": {
			"version": "9.0.0",
			"resolved": "https://registry.npmjs.org/retext/-/retext-9.0.0.tgz",
			"integrity": "sha512-sbMDcpHCNjvlheSgMfEcVrZko3cDzdbe1x/e7G66dFp0Ff7Mldvi2uv6JkJQzdRcvLYE8CA8Oe8siQx8ZOgTcA==",
			"license": "MIT",
			"dependencies": {
				"@types/nlcst": "^2.0.0",
				"retext-latin": "^4.0.0",
				"retext-stringify": "^4.0.0",
				"unified": "^11.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/retext-latin": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/retext-latin/-/retext-latin-4.0.0.tgz",
			"integrity": "sha512-hv9woG7Fy0M9IlRQloq/N6atV82NxLGveq+3H2WOi79dtIYWN8OaxogDm77f8YnVXJL2VD3bbqowu5E3EMhBYA==",
			"license": "MIT",
			"dependencies": {
				"@types/nlcst": "^2.0.0",
				"parse-latin": "^7.0.0",
				"unified": "^11.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/retext-smartypants": {
			"version": "6.2.0",
			"resolved": "https://registry.npmjs.org/retext-smartypants/-/retext-smartypants-6.2.0.tgz",
			"integrity": "sha512-kk0jOU7+zGv//kfjXEBjdIryL1Acl4i9XNkHxtM7Tm5lFiCog576fjNC9hjoR7LTKQ0DsPWy09JummSsH1uqfQ==",
			"license": "MIT",
			"dependencies": {
				"@types/nlcst": "^2.0.0",
				"nlcst-to-string": "^4.0.0",
				"unist-util-visit": "^5.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/retext-stringify": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/retext-stringify/-/retext-stringify-4.0.0.tgz",
			"integrity": "sha512-rtfN/0o8kL1e+78+uxPTqu1Klt0yPzKuQ2BfWwwfgIUSayyzxpM1PJzkKt4V8803uB9qSy32MvI7Xep9khTpiA==",
			"license": "MIT",
			"dependencies": {
				"@types/nlcst": "^2.0.0",
				"nlcst-to-string": "^4.0.0",
				"unified": "^11.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/reusify": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/reusify/-/reusify-1.1.0.tgz",
			"integrity": "sha512-g6QUff04oZpHs0eG5p83rFLhHeV00ug/Yf9nZM6fLeUrPguBTkTQOdpAWWspMh55TZfVQDPaN3NQJfbVRAxdIw==",
			"license": "MIT",
			"engines": {
				"iojs": ">=1.0.0",
				"node": ">=0.10.0"
			}
		},
		"node_modules/run-async": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/run-async/-/run-async-3.0.0.tgz",
			"integrity": "sha512-540WwVDOMxA6dN6We19EcT9sc3hkXPw5mzRNGM3FkdN/vtE9NFvj5lFAPNwUDmJjXidm3v7TC1cTE7t17Ulm1Q==",
			"license": "MIT",
			"engines": {
				"node": ">=0.12.0"
			}
		},
		"node_modules/run-parallel": {
			"version": "1.2.0",
			"resolved": "https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz",
			"integrity": "sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==",
			"funding": [
				{
					"type": "github",
					"url": "https://github.com/sponsors/feross"
				},
				{
					"type": "patreon",
					"url": "https://www.patreon.com/feross"
				},
				{
					"type": "consulting",
					"url": "https://feross.org/support"
				}
			],
			"license": "MIT",
			"dependencies": {
				"queue-microtask": "^1.2.2"
			}
		},
		"node_modules/rxjs": {
			"version": "7.8.2",
			"resolved": "https://registry.npmjs.org/rxjs/-/rxjs-7.8.2.tgz",
			"integrity": "sha512-dhKf903U/PQZY6boNNtAGdWbG85WAbjT/1xYoZIC7FAY0yWapOBQVsVrDl58W86//e1VpMNBtRV4MaXfdMySFA==",
			"license": "Apache-2.0",
			"dependencies": {
				"tslib": "^2.1.0"
			}
		},
		"node_modules/rxjs/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD"
		},
		"node_modules/safe-array-concat": {
			"version": "1.1.3",
			"resolved": "https://registry.npmjs.org/safe-array-concat/-/safe-array-concat-1.1.3.tgz",
			"integrity": "sha512-AURm5f0jYEOydBj7VQlVvDrjeFgthDdEF5H1dP+6mNpoXOMo1quQqJ4wvJDyRZ9+pO3kGWoOdmV08cSv2aJV6Q==",
			"license": "MIT",
			"dependencies": {
				"call-bind": "^1.0.8",
				"call-bound": "^1.0.2",
				"get-intrinsic": "^1.2.6",
				"has-symbols": "^1.1.0",
				"isarray": "^2.0.5"
			},
			"engines": {
				"node": ">=0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/safe-buffer": {
			"version": "5.2.1",
			"resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz",
			"integrity": "sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ==",
			"funding": [
				{
					"type": "github",
					"url": "https://github.com/sponsors/feross"
				},
				{
					"type": "patreon",
					"url": "https://www.patreon.com/feross"
				},
				{
					"type": "consulting",
					"url": "https://feross.org/support"
				}
			],
			"license": "MIT"
		},
		"node_modules/safe-push-apply": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/safe-push-apply/-/safe-push-apply-1.0.0.tgz",
			"integrity": "sha512-iKE9w/Z7xCzUMIZqdBsp6pEQvwuEebH4vdpjcDWnyzaI6yl6O9FHvVpmGelvEHNsoY6wGblkxR6Zty/h00WiSA==",
			"license": "MIT",
			"dependencies": {
				"es-errors": "^1.3.0",
				"isarray": "^2.0.5"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/safe-regex-test": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/safe-regex-test/-/safe-regex-test-1.1.0.tgz",
			"integrity": "sha512-x/+Cz4YrimQxQccJf5mKEbIa1NzeCRNI5Ecl/ekmlYaampdNLPalVyIcCZNNH3MvmqBugV5TMYZXv0ljslUlaw==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.2",
				"es-errors": "^1.3.0",
				"is-regex": "^1.2.1"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/safe-stable-stringify": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/safe-stable-stringify/-/safe-stable-stringify-1.1.1.tgz",
			"integrity": "sha512-ERq4hUjKDbJfE4+XtZLFPCDi8Vb1JqaxAPTxWFLBx8XcAlf9Bda/ZJdVezs/NAfsMQScyIlUMx+Yeu7P7rx5jw==",
			"license": "MIT"
		},
		"node_modules/safer-buffer": {
			"version": "2.1.2",
			"resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
			"integrity": "sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg==",
			"license": "MIT"
		},
		"node_modules/sax": {
			"version": "1.4.4",
			"resolved": "https://registry.npmjs.org/sax/-/sax-1.4.4.tgz",
			"integrity": "sha512-1n3r/tGXO6b6VXMdFT54SHzT9ytu9yr7TaELowdYpMqY/Ao7EnlQGmAQ1+RatX7Tkkdm6hONI2owqNx2aZj5Sw==",
			"license": "BlueOak-1.0.0",
			"engines": {
				"node": ">=11.0.0"
			}
		},
		"node_modules/scheduler": {
			"version": "0.26.0",
			"resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.26.0.tgz",
			"integrity": "sha512-NlHwttCI/l5gCPR3D1nNXtWABUmBwvZpEQiD4IXSbIDq8BzLIK/7Ir5gTFSGZDUu37K5cMNp0hFtzO38sC7gWA==",
			"license": "MIT"
		},
		"node_modules/semver": {
			"version": "7.7.2",
			"resolved": "https://registry.npmjs.org/semver/-/semver-7.7.2.tgz",
			"integrity": "sha512-RF0Fw+rO5AMf9MAyaRXI4AV0Ulj5lMHqVxxdSgiVbixSCXoEmmX/jk0CuJw4+3SqroYO9VoUh+HcuJivvtJemA==",
			"license": "ISC",
			"bin": {
				"semver": "bin/semver.js"
			},
			"engines": {
				"node": ">=10"
			}
		},
		"node_modules/send": {
			"version": "0.19.0",
			"resolved": "https://registry.npmjs.org/send/-/send-0.19.0.tgz",
			"integrity": "sha512-dW41u5VfLXu8SJh5bwRmyYUbAoSB3c9uQh6L8h/KtsFREPWpbX1lrljJo186Jc4nmci/sGUZ9a0a0J2zgfq2hw==",
			"license": "MIT",
			"dependencies": {
				"debug": "2.6.9",
				"depd": "2.0.0",
				"destroy": "1.2.0",
				"encodeurl": "~1.0.2",
				"escape-html": "~1.0.3",
				"etag": "~1.8.1",
				"fresh": "0.5.2",
				"http-errors": "2.0.0",
				"mime": "1.6.0",
				"ms": "2.1.3",
				"on-finished": "2.4.1",
				"range-parser": "~1.2.1",
				"statuses": "2.0.1"
			},
			"engines": {
				"node": ">= 0.8.0"
			}
		},
		"node_modules/send/node_modules/debug": {
			"version": "2.6.9",
			"resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
			"integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
			"license": "MIT",
			"dependencies": {
				"ms": "2.0.0"
			}
		},
		"node_modules/send/node_modules/debug/node_modules/ms": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
			"integrity": "sha512-Tpp60P6IUJDTuOq/5Z8cdskzJujfwqfOTkrwIwj7IRISpnkJnT6SyJ4PCPnGMoFjC9ddhal5KVIYtAt97ix05A==",
			"license": "MIT"
		},
		"node_modules/serialize-error": {
			"version": "12.0.0",
			"resolved": "https://registry.npmjs.org/serialize-error/-/serialize-error-12.0.0.tgz",
			"integrity": "sha512-ZYkZLAvKTKQXWuh5XpBw7CdbSzagarX39WyZ2H07CDLC5/KfsRGlIXV8d4+tfqX1M7916mRqR1QfNHSij+c9Pw==",
			"license": "MIT",
			"dependencies": {
				"type-fest": "^4.31.0"
			},
			"engines": {
				"node": ">=18"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/serve-static": {
			"version": "1.16.0",
			"resolved": "https://registry.npmjs.org/serve-static/-/serve-static-1.16.0.tgz",
			"integrity": "sha512-pDLK8zwl2eKaYrs8mrPZBJua4hMplRWJ1tIFksVC3FtBEBnl8dxgeHtsaMS8DhS9i4fLObaon6ABoc4/hQGdPA==",
			"license": "MIT",
			"dependencies": {
				"encodeurl": "~1.0.2",
				"escape-html": "~1.0.3",
				"parseurl": "~1.3.3",
				"send": "0.18.0"
			},
			"engines": {
				"node": ">= 0.8.0"
			}
		},
		"node_modules/set-function-length": {
			"version": "1.2.2",
			"resolved": "https://registry.npmjs.org/set-function-length/-/set-function-length-1.2.2.tgz",
			"integrity": "sha512-pgRc4hJ4/sNjWCSS9AmnS40x3bNMDTknHgL5UaMBTMyJnU90EgWh1Rz+MC9eFu4BuN/UwZjKQuY/1v3rM7HMfg==",
			"license": "MIT",
			"dependencies": {
				"define-data-property": "^1.1.4",
				"es-errors": "^1.3.0",
				"function-bind": "^1.1.2",
				"get-intrinsic": "^1.2.4",
				"gopd": "^1.0.1",
				"has-property-descriptors": "^1.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/set-function-name": {
			"version": "2.0.2",
			"resolved": "https://registry.npmjs.org/set-function-name/-/set-function-name-2.0.2.tgz",
			"integrity": "sha512-7PGFlmtwsEADb0WYyvCMa1t+yke6daIG4Wirafur5kcf+MhUnPms1UeR0CKQdTZD81yESwMHbtn+TR+dMviakQ==",
			"license": "MIT",
			"dependencies": {
				"define-data-property": "^1.1.4",
				"es-errors": "^1.3.0",
				"functions-have-names": "^1.2.3",
				"has-property-descriptors": "^1.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/set-proto": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/set-proto/-/set-proto-1.0.0.tgz",
			"integrity": "sha512-RJRdvCo6IAnPdsvP/7m6bsQqNnn1FCBX5ZNtFL98MmFF/4xAIJTIg1YbHW5DC2W5SKZanrC6i4HsJqlajw/dZw==",
			"license": "MIT",
			"dependencies": {
				"dunder-proto": "^1.0.1",
				"es-errors": "^1.3.0",
				"es-object-atoms": "^1.0.0"
			},
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/setprototypeof": {
			"version": "1.2.0",
			"resolved": "https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.2.0.tgz",
			"integrity": "sha512-E5LDX7Wrp85Kil5bhZv46j8jOeboKq5JMmYM3gVGdGH8xFpPWXUMsNrlODCrkoxMEeNi/XZIwuRvY4XNwYMJpw==",
			"license": "ISC"
		},
		"node_modules/sharp": {
			"version": "0.33.5",
			"resolved": "https://registry.npmjs.org/sharp/-/sharp-0.33.5.tgz",
			"integrity": "sha512-haPVm1EkS9pgvHrQ/F3Xy+hgcuMV0Wm9vfIBSiwZ05k+xgb0PkBQpGsAA/oWdDobNaZTH5ppvHtzCFbnSEwHVw==",
			"hasInstallScript": true,
			"license": "Apache-2.0",
			"dependencies": {
				"color": "^4.2.3",
				"detect-libc": "^2.0.3",
				"semver": "^7.6.3"
			},
			"engines": {
				"node": "^18.17.0 || ^20.3.0 || >=21.0.0"
			},
			"funding": {
				"url": "https://opencollective.com/libvips"
			},
			"optionalDependencies": {
				"@img/sharp-darwin-arm64": "0.33.5",
				"@img/sharp-darwin-x64": "0.33.5",
				"@img/sharp-libvips-darwin-arm64": "1.0.4",
				"@img/sharp-libvips-darwin-x64": "1.0.4",
				"@img/sharp-libvips-linux-arm": "1.0.5",
				"@img/sharp-libvips-linux-arm64": "1.0.4",
				"@img/sharp-libvips-linux-s390x": "1.0.4",
				"@img/sharp-libvips-linux-x64": "1.0.4",
				"@img/sharp-libvips-linuxmusl-arm64": "1.0.4",
				"@img/sharp-libvips-linuxmusl-x64": "1.0.4",
				"@img/sharp-linux-arm": "0.33.5",
				"@img/sharp-linux-arm64": "0.33.5",
				"@img/sharp-linux-s390x": "0.33.5",
				"@img/sharp-linux-x64": "0.33.5",
				"@img/sharp-linuxmusl-arm64": "0.33.5",
				"@img/sharp-linuxmusl-x64": "0.33.5",
				"@img/sharp-wasm32": "0.33.5",
				"@img/sharp-win32-ia32": "0.33.5",
				"@img/sharp-win32-x64": "0.33.5"
			}
		},
		"node_modules/sharp-ico": {
			"version": "0.1.5",
			"resolved": "https://registry.npmjs.org/sharp-ico/-/sharp-ico-0.1.5.tgz",
			"integrity": "sha512-a3jODQl82NPp1d5OYb0wY+oFaPk7AvyxipIowCHk7pBsZCWgbe0yAkU2OOXdoH0ENyANhyOQbs9xkAiRHcF02Q==",
			"license": "MIT",
			"dependencies": {
				"decode-ico": "*",
				"ico-endec": "*",
				"sharp": "*"
			}
		},
		"node_modules/shiki": {
			"version": "3.22.0",
			"resolved": "https://registry.npmjs.org/shiki/-/shiki-3.22.0.tgz",
			"integrity": "sha512-LBnhsoYEe0Eou4e1VgJACes+O6S6QC0w71fCSp5Oya79inkwkm15gQ1UF6VtQ8j/taMDh79hAB49WUk8ALQW3g==",
			"license": "MIT",
			"dependencies": {
				"@shikijs/core": "3.22.0",
				"@shikijs/engine-javascript": "3.22.0",
				"@shikijs/engine-oniguruma": "3.22.0",
				"@shikijs/langs": "3.22.0",
				"@shikijs/themes": "3.22.0",
				"@shikijs/types": "3.22.0",
				"@shikijs/vscode-textmate": "^10.0.2",
				"@types/hast": "^3.0.4"
			}
		},
		"node_modules/side-channel": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/side-channel/-/side-channel-1.1.0.tgz",
			"integrity": "sha512-ZX99e6tRweoUXqR+VBrslhda51Nh5MTQwou5tnUDgbtyM0dBgmhEDtWGP/xbKn6hqfPRHujUNwz5fy/wbbhnpw==",
			"license": "MIT",
			"dependencies": {
				"es-errors": "^1.3.0",
				"object-inspect": "^1.13.3",
				"side-channel-list": "^1.0.0",
				"side-channel-map": "^1.0.1",
				"side-channel-weakmap": "^1.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/side-channel-list": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/side-channel-list/-/side-channel-list-1.0.0.tgz",
			"integrity": "sha512-FCLHtRD/gnpCiCHEiJLOwdmFP+wzCmDEkc9y7NsYxeF4u7Btsn1ZuwgwJGxImImHicJArLP4R0yX4c2KCrMrTA==",
			"license": "MIT",
			"dependencies": {
				"es-errors": "^1.3.0",
				"object-inspect": "^1.13.3"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/side-channel-map": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/side-channel-map/-/side-channel-map-1.0.1.tgz",
			"integrity": "sha512-VCjCNfgMsby3tTdo02nbjtM/ewra6jPHmpThenkTYh8pG9ucZ/1P8So4u4FGBek/BjpOVsDCMoLA/iuBKIFXRA==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.2",
				"es-errors": "^1.3.0",
				"get-intrinsic": "^1.2.5",
				"object-inspect": "^1.13.3"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/side-channel-weakmap": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/side-channel-weakmap/-/side-channel-weakmap-1.0.2.tgz",
			"integrity": "sha512-WPS/HvHQTYnHisLo9McqBHOJk2FkHO/tlpvldyrnem4aeQp4hai3gythswg6p01oSoTl58rcpiFAjF2br2Ak2A==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.2",
				"es-errors": "^1.3.0",
				"get-intrinsic": "^1.2.5",
				"object-inspect": "^1.13.3",
				"side-channel-map": "^1.0.1"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/signal-exit": {
			"version": "4.1.0",
			"resolved": "https://registry.npmjs.org/signal-exit/-/signal-exit-4.1.0.tgz",
			"integrity": "sha512-bzyZ1e88w9O1iNJbKnOlvYTrWPDl46O1bG0D3XInv+9tkPrxrN8jUUTiFlDkkmKWgn1M6CfIA13SuGqOa9Korw==",
			"license": "ISC",
			"engines": {
				"node": ">=14"
			},
			"funding": {
				"url": "https://github.com/sponsors/isaacs"
			}
		},
		"node_modules/simple-eval": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/simple-eval/-/simple-eval-1.0.1.tgz",
			"integrity": "sha512-LH7FpTAkeD+y5xQC4fzS+tFtaNlvt3Ib1zKzvhjv/Y+cioV4zIuw4IZr2yhRLu67CWL7FR9/6KXKnjRoZTvGGQ==",
			"license": "MIT",
			"dependencies": {
				"jsep": "^1.3.6"
			},
			"engines": {
				"node": ">=12"
			}
		},
		"node_modules/simple-swizzle": {
			"version": "0.2.4",
			"resolved": "https://registry.npmjs.org/simple-swizzle/-/simple-swizzle-0.2.4.tgz",
			"integrity": "sha512-nAu1WFPQSMNr2Zn9PGSZK9AGn4t/y97lEm+MXTtUDwfP0ksAIX4nO+6ruD9Jwut4C49SB1Ws+fbXsm/yScWOHw==",
			"license": "MIT",
			"dependencies": {
				"is-arrayish": "^0.3.1"
			}
		},
		"node_modules/simple-swizzle/node_modules/is-arrayish": {
			"version": "0.3.4",
			"resolved": "https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.3.4.tgz",
			"integrity": "sha512-m6UrgzFVUYawGBh1dUsWR5M2Clqic9RVXC/9f8ceNlv2IcO9j9J/z8UoCLPqtsPBFNzEpfR3xftohbfqDx8EQA==",
			"license": "MIT"
		},
		"node_modules/slice-ansi": {
			"version": "7.1.2",
			"resolved": "https://registry.npmjs.org/slice-ansi/-/slice-ansi-7.1.2.tgz",
			"integrity": "sha512-iOBWFgUX7caIZiuutICxVgX1SdxwAVFFKwt1EvMYYec/NWO5meOJ6K5uQxhrYBdQJne4KxiqZc+KptFOWFSI9w==",
			"license": "MIT",
			"dependencies": {
				"ansi-styles": "^6.2.1",
				"is-fullwidth-code-point": "^5.0.0"
			},
			"engines": {
				"node": ">=18"
			},
			"funding": {
				"url": "https://github.com/chalk/slice-ansi?sponsor=1"
			}
		},
		"node_modules/smart-buffer": {
			"version": "4.2.0",
			"resolved": "https://registry.npmjs.org/smart-buffer/-/smart-buffer-4.2.0.tgz",
			"integrity": "sha512-94hK0Hh8rPqQl2xXc3HsaBoOXKV20MToPkcXvwbISWLEs+64sBq5kFgn2kJDHb1Pry9yrP0dxrCI9RRci7RXKg==",
			"license": "MIT",
			"engines": {
				"node": ">= 6.0.0",
				"npm": ">= 3.0.0"
			}
		},
		"node_modules/socket.io": {
			"version": "4.7.2",
			"resolved": "https://registry.npmjs.org/socket.io/-/socket.io-4.7.2.tgz",
			"integrity": "sha512-bvKVS29/I5fl2FGLNHuXlQaUH/BlzX1IN6S+NKLNZpBsPZIDH+90eQmCs2Railn4YUiww4SzUedJ6+uzwFnKLw==",
			"license": "MIT",
			"dependencies": {
				"accepts": "~1.3.4",
				"base64id": "~2.0.0",
				"cors": "~2.8.5",
				"debug": "~4.3.2",
				"engine.io": "~6.5.2",
				"socket.io-adapter": "~2.5.2",
				"socket.io-parser": "~4.2.4"
			},
			"engines": {
				"node": ">=10.2.0"
			}
		},
		"node_modules/socket.io-adapter": {
			"version": "2.5.6",
			"resolved": "https://registry.npmjs.org/socket.io-adapter/-/socket.io-adapter-2.5.6.tgz",
			"integrity": "sha512-DkkO/dz7MGln0dHn5bmN3pPy+JmywNICWrJqVWiVOyvXjWQFIv9c2h24JrQLLFJ2aQVQf/Cvl1vblnd4r2apLQ==",
			"license": "MIT",
			"dependencies": {
				"debug": "~4.4.1",
				"ws": "~8.18.3"
			}
		},
		"node_modules/socket.io-adapter/node_modules/ws": {
			"version": "8.18.3",
			"resolved": "https://registry.npmjs.org/ws/-/ws-8.18.3.tgz",
			"integrity": "sha512-PEIGCY5tSlUt50cqyMXfCzX+oOPqN0vuGqWzbcJ2xvnkzkq46oOpz7dQaTDBdfICb4N14+GARUDw2XV2N4tvzg==",
			"license": "MIT",
			"engines": {
				"node": ">=10.0.0"
			},
			"peerDependencies": {
				"bufferutil": "^4.0.1",
				"utf-8-validate": ">=5.0.2"
			},
			"peerDependenciesMeta": {
				"bufferutil": {
					"optional": true
				},
				"utf-8-validate": {
					"optional": true
				}
			}
		},
		"node_modules/socket.io-parser": {
			"version": "4.2.5",
			"resolved": "https://registry.npmjs.org/socket.io-parser/-/socket.io-parser-4.2.5.tgz",
			"integrity": "sha512-bPMmpy/5WWKHea5Y/jYAP6k74A+hvmRCQaJuJB6I/ML5JZq/KfNieUVo/3Mh7SAqn7TyFdIo6wqYHInG1MU1bQ==",
			"license": "MIT",
			"dependencies": {
				"@socket.io/component-emitter": "~3.1.0",
				"debug": "~4.4.1"
			},
			"engines": {
				"node": ">=10.0.0"
			}
		},
		"node_modules/socket.io/node_modules/debug": {
			"version": "4.3.7",
			"resolved": "https://registry.npmjs.org/debug/-/debug-4.3.7.tgz",
			"integrity": "sha512-Er2nc/H7RrMXZBFCEim6TCmMk02Z8vLC2Rbi1KEBggpo0fS6l0S1nnapwmIi3yW/+GOJap1Krg4w0Hg80oCqgQ==",
			"license": "MIT",
			"dependencies": {
				"ms": "^2.1.3"
			},
			"engines": {
				"node": ">=6.0"
			},
			"peerDependenciesMeta": {
				"supports-color": {
					"optional": true
				}
			}
		},
		"node_modules/socks": {
			"version": "2.8.7",
			"resolved": "https://registry.npmjs.org/socks/-/socks-2.8.7.tgz",
			"integrity": "sha512-HLpt+uLy/pxB+bum/9DzAgiKS8CX1EvbWxI4zlmgGCExImLdiad2iCwXT5Z4c9c3Eq8rP2318mPW2c+QbtjK8A==",
			"license": "MIT",
			"dependencies": {
				"ip-address": "^10.0.1",
				"smart-buffer": "^4.2.0"
			},
			"engines": {
				"node": ">= 10.0.0",
				"npm": ">= 3.0.0"
			}
		},
		"node_modules/socks-proxy-agent": {
			"version": "8.0.5",
			"resolved": "https://registry.npmjs.org/socks-proxy-agent/-/socks-proxy-agent-8.0.5.tgz",
			"integrity": "sha512-HehCEsotFqbPW9sJ8WVYB6UbmIMv7kUUORIF2Nncq4VQvBfNBLibW9YZR5dlYCSUhwcD628pRllm7n+E+YTzJw==",
			"license": "MIT",
			"dependencies": {
				"agent-base": "^7.1.2",
				"debug": "^4.3.4",
				"socks": "^2.8.3"
			},
			"engines": {
				"node": ">= 14"
			}
		},
		"node_modules/source-map": {
			"version": "0.7.6",
			"resolved": "https://registry.npmjs.org/source-map/-/source-map-0.7.6.tgz",
			"integrity": "sha512-i5uvt8C3ikiWeNZSVZNWcfZPItFQOsYTUAOkcUPGd8DqDy1uOUikjt5dG+uRlwyvR108Fb9DOd4GvXfT0N2/uQ==",
			"license": "BSD-3-Clause",
			"engines": {
				"node": ">= 12"
			}
		},
		"node_modules/source-map-js": {
			"version": "1.2.1",
			"resolved": "https://registry.npmjs.org/source-map-js/-/source-map-js-1.2.1.tgz",
			"integrity": "sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==",
			"license": "BSD-3-Clause",
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/space-separated-tokens": {
			"version": "2.0.2",
			"resolved": "https://registry.npmjs.org/space-separated-tokens/-/space-separated-tokens-2.0.2.tgz",
			"integrity": "sha512-PEGlAwrG8yXGXRjW32fGbg66JAlOAwbObuqVoJpv/mRgoWDQfgH1wDPvtzWyUSNAXBGSk8h755YDbbcEy3SH2Q==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/stack-utils": {
			"version": "2.0.6",
			"resolved": "https://registry.npmjs.org/stack-utils/-/stack-utils-2.0.6.tgz",
			"integrity": "sha512-XlkWvfIm6RmsWtNJx+uqtKLS8eqFbxUg0ZzLXqY0caEy9l7hruX8IpiDnjsLavoBgqCCR71TqWO8MaXYheJ3RQ==",
			"license": "MIT",
			"dependencies": {
				"escape-string-regexp": "^2.0.0"
			},
			"engines": {
				"node": ">=10"
			}
		},
		"node_modules/stack-utils/node_modules/escape-string-regexp": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-2.0.0.tgz",
			"integrity": "sha512-UpzcLCXolUWcNu5HtVMHYdXJjArjsF9C0aNnquZYY4uW/Vu0miy5YoWvbV345HauVvcAUnpRuhMMcqTcGOY2+w==",
			"license": "MIT",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/statuses": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/statuses/-/statuses-2.0.1.tgz",
			"integrity": "sha512-RwNA9Z/7PrK06rYLIzFMlaF+l73iwpzsqRIFgbMLbTcLD6cOao82TaWefPXQvB2fOC4AjuYSEndS7N/mTCbkdQ==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/stop-iteration-iterator": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/stop-iteration-iterator/-/stop-iteration-iterator-1.1.0.tgz",
			"integrity": "sha512-eLoXW/DHyl62zxY4SCaIgnRhuMr6ri4juEYARS8E6sCEqzKpOiE521Ucofdx+KnDZl5xmvGYaaKCk5FEOxJCoQ==",
			"license": "MIT",
			"dependencies": {
				"es-errors": "^1.3.0",
				"internal-slot": "^1.1.0"
			},
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/streamx": {
			"version": "2.23.0",
			"resolved": "https://registry.npmjs.org/streamx/-/streamx-2.23.0.tgz",
			"integrity": "sha512-kn+e44esVfn2Fa/O0CPFcex27fjIL6MkVae0Mm6q+E6f0hWv578YCERbv+4m02cjxvDsPKLnmxral/rR6lBMAg==",
			"license": "MIT",
			"dependencies": {
				"events-universal": "^1.0.0",
				"fast-fifo": "^1.3.2",
				"text-decoder": "^1.1.0"
			}
		},
		"node_modules/string-width": {
			"version": "7.2.0",
			"resolved": "https://registry.npmjs.org/string-width/-/string-width-7.2.0.tgz",
			"integrity": "sha512-tsaTIkKW9b4N+AEj+SVA+WhJzV7/zMhcSu78mLKWSk7cXMOSHsBKFWUs0fWwq8QyK3MgJBQRX6Gbi4kYbdvGkQ==",
			"license": "MIT",
			"dependencies": {
				"emoji-regex": "^10.3.0",
				"get-east-asian-width": "^1.0.0",
				"strip-ansi": "^7.1.0"
			},
			"engines": {
				"node": ">=18"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/string.prototype.trim": {
			"version": "1.2.10",
			"resolved": "https://registry.npmjs.org/string.prototype.trim/-/string.prototype.trim-1.2.10.tgz",
			"integrity": "sha512-Rs66F0P/1kedk5lyYyH9uBzuiI/kNRmwJAR9quK6VOtIpZ2G+hMZd+HQbbv25MgCA6gEffoMZYxlTod4WcdrKA==",
			"license": "MIT",
			"dependencies": {
				"call-bind": "^1.0.8",
				"call-bound": "^1.0.2",
				"define-data-property": "^1.1.4",
				"define-properties": "^1.2.1",
				"es-abstract": "^1.23.5",
				"es-object-atoms": "^1.0.0",
				"has-property-descriptors": "^1.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/string.prototype.trimend": {
			"version": "1.0.9",
			"resolved": "https://registry.npmjs.org/string.prototype.trimend/-/string.prototype.trimend-1.0.9.tgz",
			"integrity": "sha512-G7Ok5C6E/j4SGfyLCloXTrngQIQU3PWtXGst3yM7Bea9FRURf1S42ZHlZZtsNque2FN2PoUhfZXYLNWwEr4dLQ==",
			"license": "MIT",
			"dependencies": {
				"call-bind": "^1.0.8",
				"call-bound": "^1.0.2",
				"define-properties": "^1.2.1",
				"es-object-atoms": "^1.0.0"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/string.prototype.trimstart": {
			"version": "1.0.8",
			"resolved": "https://registry.npmjs.org/string.prototype.trimstart/-/string.prototype.trimstart-1.0.8.tgz",
			"integrity": "sha512-UXSH262CSZY1tfu3G3Secr6uGLCFVPMhIqHjlgCUtCCcgihYc/xKs9djMTMUOb2j1mVSeU8EU6NWc/iQKU6Gfg==",
			"license": "MIT",
			"dependencies": {
				"call-bind": "^1.0.7",
				"define-properties": "^1.2.1",
				"es-object-atoms": "^1.0.0"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/stringify-entities": {
			"version": "4.0.4",
			"resolved": "https://registry.npmjs.org/stringify-entities/-/stringify-entities-4.0.4.tgz",
			"integrity": "sha512-IwfBptatlO+QCJUo19AqvrPNqlVMpW9YEL2LIVY+Rpv2qsjCGxaDLNRgeGsQWJhfItebuJhsGSLjaBbNSQ+ieg==",
			"license": "MIT",
			"dependencies": {
				"character-entities-html4": "^2.0.0",
				"character-entities-legacy": "^3.0.0"
			},
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/strip-ansi": {
			"version": "7.1.2",
			"resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-7.1.2.tgz",
			"integrity": "sha512-gmBGslpoQJtgnMAvOVqGZpEz9dyoKTCzy2nfz/n8aIFhN/jCE/rCmcxabB6jOOHV+0WNnylOxaxBQPSvcWklhA==",
			"license": "MIT",
			"dependencies": {
				"ansi-regex": "^6.0.1"
			},
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/chalk/strip-ansi?sponsor=1"
			}
		},
		"node_modules/style-to-js": {
			"version": "1.1.21",
			"resolved": "https://registry.npmjs.org/style-to-js/-/style-to-js-1.1.21.tgz",
			"integrity": "sha512-RjQetxJrrUJLQPHbLku6U/ocGtzyjbJMP9lCNK7Ag0CNh690nSH8woqWH9u16nMjYBAok+i7JO1NP2pOy8IsPQ==",
			"license": "MIT",
			"dependencies": {
				"style-to-object": "1.0.14"
			}
		},
		"node_modules/style-to-object": {
			"version": "1.0.14",
			"resolved": "https://registry.npmjs.org/style-to-object/-/style-to-object-1.0.14.tgz",
			"integrity": "sha512-LIN7rULI0jBscWQYaSswptyderlarFkjQ+t79nzty8tcIAceVomEVlLzH5VP4Cmsv6MtKhs7qaAiwlcp+Mgaxw==",
			"license": "MIT",
			"dependencies": {
				"inline-style-parser": "0.2.7"
			}
		},
		"node_modules/sucrase": {
			"version": "3.35.1",
			"resolved": "https://registry.npmjs.org/sucrase/-/sucrase-3.35.1.tgz",
			"integrity": "sha512-DhuTmvZWux4H1UOnWMB3sk0sbaCVOoQZjv8u1rDoTV0HTdGem9hkAZtl4JZy8P2z4Bg0nT+YMeOFyVr4zcG5Tw==",
			"license": "MIT",
			"dependencies": {
				"@jridgewell/gen-mapping": "^0.3.2",
				"commander": "^4.0.0",
				"lines-and-columns": "^1.1.6",
				"mz": "^2.7.0",
				"pirates": "^4.0.1",
				"tinyglobby": "^0.2.11",
				"ts-interface-checker": "^0.1.9"
			},
			"bin": {
				"sucrase": "bin/sucrase",
				"sucrase-node": "bin/sucrase-node"
			},
			"engines": {
				"node": ">=16 || 14 >=14.17"
			}
		},
		"node_modules/sucrase/node_modules/commander": {
			"version": "4.1.1",
			"resolved": "https://registry.npmjs.org/commander/-/commander-4.1.1.tgz",
			"integrity": "sha512-NOKm8xhkzAjzFx8B2v5OAHT+u5pRQc2UCa2Vq9jYL/31o2wi9mxBA7LIFs3sV5VSC49z6pEhfbMULvShKj26WA==",
			"license": "MIT",
			"engines": {
				"node": ">= 6"
			}
		},
		"node_modules/supports-preserve-symlinks-flag": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz",
			"integrity": "sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/tailwindcss": {
			"version": "3.4.4",
			"resolved": "https://registry.npmjs.org/tailwindcss/-/tailwindcss-3.4.4.tgz",
			"integrity": "sha512-ZoyXOdJjISB7/BcLTR6SEsLgKtDStYyYZVLsUtWChO4Ps20CBad7lfJKVDiejocV4ME1hLmyY0WJE3hSDcmQ2A==",
			"license": "MIT",
			"dependencies": {
				"@alloc/quick-lru": "^5.2.0",
				"arg": "^5.0.2",
				"chokidar": "^3.5.3",
				"didyoumean": "^1.2.2",
				"dlv": "^1.1.3",
				"fast-glob": "^3.3.0",
				"glob-parent": "^6.0.2",
				"is-glob": "^4.0.3",
				"jiti": "^1.21.0",
				"lilconfig": "^2.1.0",
				"micromatch": "^4.0.5",
				"normalize-path": "^3.0.0",
				"object-hash": "^3.0.0",
				"picocolors": "^1.0.0",
				"postcss": "^8.4.23",
				"postcss-import": "^15.1.0",
				"postcss-js": "^4.0.1",
				"postcss-load-config": "^4.0.1",
				"postcss-nested": "^6.0.1",
				"postcss-selector-parser": "^6.0.11",
				"resolve": "^1.22.2",
				"sucrase": "^3.32.0"
			},
			"bin": {
				"tailwind": "lib/cli.js",
				"tailwindcss": "lib/cli.js"
			},
			"engines": {
				"node": ">=14.0.0"
			}
		},
		"node_modules/tailwindcss/node_modules/glob-parent": {
			"version": "6.0.2",
			"resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz",
			"integrity": "sha512-XxwI8EOhVQgWp6iDL+3b0r86f4d6AX6zSU55HfB4ydCEuXLXc5FcYeOu+nnGftS4TEju/11rt4KJPTMgbfmv4A==",
			"license": "ISC",
			"dependencies": {
				"is-glob": "^4.0.3"
			},
			"engines": {
				"node": ">=10.13.0"
			}
		},
		"node_modules/tar": {
			"version": "6.2.1",
			"resolved": "https://registry.npmjs.org/tar/-/tar-6.2.1.tgz",
			"integrity": "sha512-DZ4yORTwrbTj/7MZYq2w+/ZFdI6OZ/f9SFHR+71gIVUZhOQPHzVCLpvRnPgyaMpfWxxk/4ONva3GQSyNIKRv6A==",
			"deprecated": "Old versions of tar are not supported, and contain widely publicized security vulnerabilities, which have been fixed in the current version. Please update. Support for old versions may be purchased (at exorbitant rates) by contacting i@izs.me",
			"license": "ISC",
			"dependencies": {
				"chownr": "^2.0.0",
				"fs-minipass": "^2.0.0",
				"minipass": "^5.0.0",
				"minizlib": "^2.1.1",
				"mkdirp": "^1.0.3",
				"yallist": "^4.0.0"
			},
			"engines": {
				"node": ">=10"
			}
		},
		"node_modules/tar-fs": {
			"version": "3.1.1",
			"resolved": "https://registry.npmjs.org/tar-fs/-/tar-fs-3.1.1.tgz",
			"integrity": "sha512-LZA0oaPOc2fVo82Txf3gw+AkEd38szODlptMYejQUhndHMLQ9M059uXR+AfS7DNo0NpINvSqDsvyaCrBVkptWg==",
			"license": "MIT",
			"dependencies": {
				"pump": "^3.0.0",
				"tar-stream": "^3.1.5"
			},
			"optionalDependencies": {
				"bare-fs": "^4.0.1",
				"bare-path": "^3.0.0"
			}
		},
		"node_modules/tar-stream": {
			"version": "3.1.7",
			"resolved": "https://registry.npmjs.org/tar-stream/-/tar-stream-3.1.7.tgz",
			"integrity": "sha512-qJj60CXt7IU1Ffyc3NJMjh6EkuCFej46zUqJ4J7pqYlThyd9bO0XBTmcOIhSzZJVWfsLks0+nle/j538YAW9RQ==",
			"license": "MIT",
			"dependencies": {
				"b4a": "^1.6.4",
				"fast-fifo": "^1.2.0",
				"streamx": "^2.15.0"
			}
		},
		"node_modules/text-decoder": {
			"version": "1.2.3",
			"resolved": "https://registry.npmjs.org/text-decoder/-/text-decoder-1.2.3.tgz",
			"integrity": "sha512-3/o9z3X0X0fTupwsYvR03pJ/DjWuqqrfwBgTQzdWDiQSm9KitAyz/9WqsT2JQW7KV2m+bC2ol/zqpW37NHxLaA==",
			"license": "Apache-2.0",
			"dependencies": {
				"b4a": "^1.6.4"
			}
		},
		"node_modules/thenify": {
			"version": "3.3.1",
			"resolved": "https://registry.npmjs.org/thenify/-/thenify-3.3.1.tgz",
			"integrity": "sha512-RVZSIV5IG10Hk3enotrhvz0T9em6cyHBLkH/YAZuKqd8hRkKhSfCGIcP2KUY0EPxndzANBmNllzWPwak+bheSw==",
			"license": "MIT",
			"dependencies": {
				"any-promise": "^1.0.0"
			}
		},
		"node_modules/thenify-all": {
			"version": "1.6.0",
			"resolved": "https://registry.npmjs.org/thenify-all/-/thenify-all-1.6.0.tgz",
			"integrity": "sha512-RNxQH/qI8/t3thXJDwcstUO4zeqo64+Uy/+sNVRBx4Xn2OX+OZ9oP+iJnNFqplFra2ZUVeKCSa2oVWi3T4uVmA==",
			"license": "MIT",
			"dependencies": {
				"thenify": ">= 3.1.0 < 4"
			},
			"engines": {
				"node": ">=0.8"
			}
		},
		"node_modules/through": {
			"version": "2.3.8",
			"resolved": "https://registry.npmjs.org/through/-/through-2.3.8.tgz",
			"integrity": "sha512-w89qg7PI8wAdvX60bMDP+bFoD5Dvhm9oLheFp5O4a2QF0cSBGsBX4qZmadPMvVqlLJBBci+WqGGOAPvcDeNSVg==",
			"license": "MIT"
		},
		"node_modules/tinyglobby": {
			"version": "0.2.15",
			"resolved": "https://registry.npmjs.org/tinyglobby/-/tinyglobby-0.2.15.tgz",
			"integrity": "sha512-j2Zq4NyQYG5XMST4cbs02Ak8iJUdxRM0XI5QyxXuZOzKOINmWurp3smXu3y5wDcJrptwpSjgXHzIQxR0omXljQ==",
			"license": "MIT",
			"dependencies": {
				"fdir": "^6.5.0",
				"picomatch": "^4.0.3"
			},
			"engines": {
				"node": ">=12.0.0"
			},
			"funding": {
				"url": "https://github.com/sponsors/SuperchupuDev"
			}
		},
		"node_modules/tinyglobby/node_modules/fdir": {
			"version": "6.5.0",
			"resolved": "https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz",
			"integrity": "sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==",
			"license": "MIT",
			"engines": {
				"node": ">=12.0.0"
			},
			"peerDependencies": {
				"picomatch": "^3 || ^4"
			},
			"peerDependenciesMeta": {
				"picomatch": {
					"optional": true
				}
			}
		},
		"node_modules/tinyglobby/node_modules/picomatch": {
			"version": "4.0.3",
			"resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.3.tgz",
			"integrity": "sha512-5gTmgEY/sqK6gFXLIsQNH19lWb4ebPDLA4SdLP7dsWkIXHWlG66oPuVvXSGFPppYZz8ZDZq0dYYrbHfBCVUb1Q==",
			"license": "MIT",
			"engines": {
				"node": ">=12"
			},
			"funding": {
				"url": "https://github.com/sponsors/jonschlinkert"
			}
		},
		"node_modules/to-data-view": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/to-data-view/-/to-data-view-1.1.0.tgz",
			"integrity": "sha512-1eAdufMg6mwgmlojAx3QeMnzB/BTVp7Tbndi3U7ftcT2zCZadjxkkmLmd97zmaxWi+sgGcgWrokmpEoy0Dn0vQ==",
			"license": "MIT"
		},
		"node_modules/to-regex-range": {
			"version": "5.0.1",
			"resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
			"integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
			"license": "MIT",
			"dependencies": {
				"is-number": "^7.0.0"
			},
			"engines": {
				"node": ">=8.0"
			}
		},
		"node_modules/toidentifier": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/toidentifier/-/toidentifier-1.0.1.tgz",
			"integrity": "sha512-o5sSPKEkg/DIQNmH43V0/uerLrpzVedkUh8tGNvaeXpfpuwjKenlSox/2O/BTlZUtEe+JG7s5YhEz608PlAHRA==",
			"license": "MIT",
			"engines": {
				"node": ">=0.6"
			}
		},
		"node_modules/tr46": {
			"version": "0.0.3",
			"resolved": "https://registry.npmjs.org/tr46/-/tr46-0.0.3.tgz",
			"integrity": "sha512-N3WMsuqV66lT30CrXNbEjx4GEwlow3v6rr4mCcv6prnfwhS01rkgyFdjPNBYd9br7LpXV1+Emh01fHnq2Gdgrw==",
			"license": "MIT"
		},
		"node_modules/trim-lines": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/trim-lines/-/trim-lines-3.0.1.tgz",
			"integrity": "sha512-kRj8B+YHZCc9kQYdWfJB2/oUl9rA99qbowYYBtr4ui4mZyAQ2JpvVBd/6U2YloATfqBhBTSMhTpgBHtU0Mf3Rg==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/trim-trailing-lines": {
			"version": "2.1.0",
			"resolved": "https://registry.npmjs.org/trim-trailing-lines/-/trim-trailing-lines-2.1.0.tgz",
			"integrity": "sha512-5UR5Biq4VlVOtzqkm2AZlgvSlDJtME46uV0br0gENbwN4l5+mMKT4b9gJKqWtuL2zAIqajGJGuvbCbcAJUZqBg==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/trough": {
			"version": "2.2.0",
			"resolved": "https://registry.npmjs.org/trough/-/trough-2.2.0.tgz",
			"integrity": "sha512-tmMpK00BjZiUyVyvrBK7knerNgmgvcV/KLVyuma/SC+TQN167GrMRciANTz09+k3zW8L8t60jWO1GpfkZdjTaw==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/ts-interface-checker": {
			"version": "0.1.13",
			"resolved": "https://registry.npmjs.org/ts-interface-checker/-/ts-interface-checker-0.1.13.tgz",
			"integrity": "sha512-Y/arvbn+rrz3JCKl9C4kVNfTfSm2/mEp5FSz5EsZSANGPSlQrpRI5M4PKF+mJnE52jOO90PnPSc3Ur3bTQw0gA==",
			"license": "Apache-2.0"
		},
		"node_modules/tslib": {
			"version": "1.14.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-1.14.1.tgz",
			"integrity": "sha512-Xni35NKzjgMrwevysHTCArtLDpPvye8zV/0E4EyYn43P7/7qvQwPh9BGkHewbMulVntbigmcT7rdX3BNo9wRJg==",
			"license": "0BSD"
		},
		"node_modules/twoslash": {
			"version": "0.3.6",
			"resolved": "https://registry.npmjs.org/twoslash/-/twoslash-0.3.6.tgz",
			"integrity": "sha512-VuI5OKl+MaUO9UIW3rXKoPgHI3X40ZgB/j12VY6h98Ae1mCBihjPvhOPeJWlxCYcmSbmeZt5ZKkK0dsVtp+6pA==",
			"license": "MIT",
			"dependencies": {
				"@typescript/vfs": "^1.6.2",
				"twoslash-protocol": "0.3.6"
			},
			"peerDependencies": {
				"typescript": "^5.5.0"
			}
		},
		"node_modules/twoslash-protocol": {
			"version": "0.3.6",
			"resolved": "https://registry.npmjs.org/twoslash-protocol/-/twoslash-protocol-0.3.6.tgz",
			"integrity": "sha512-FHGsJ9Q+EsNr5bEbgG3hnbkvEBdW5STgPU824AHUjB4kw0Dn4p8tABT7Ncg1Ie6V0+mDg3Qpy41VafZXcQhWMA==",
			"license": "MIT"
		},
		"node_modules/type-fest": {
			"version": "4.41.0",
			"resolved": "https://registry.npmjs.org/type-fest/-/type-fest-4.41.0.tgz",
			"integrity": "sha512-TeTSQ6H5YHvpqVwBRcnLDCBnDOHWYu7IvGbHT6N8AOymcr9PJGjc1GTtiWZTYg0NCgYwvnYWEkVChQAr9bjfwA==",
			"license": "(MIT OR CC0-1.0)",
			"engines": {
				"node": ">=16"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/type-is": {
			"version": "1.6.18",
			"resolved": "https://registry.npmjs.org/type-is/-/type-is-1.6.18.tgz",
			"integrity": "sha512-TkRKr9sUTxEH8MdfuCSP7VizJyzRNMjj2J2do2Jr3Kym598JVdEksuzPQCnlFPW4ky9Q+iA+ma9BGm06XQBy8g==",
			"license": "MIT",
			"dependencies": {
				"media-typer": "0.3.0",
				"mime-types": "~2.1.24"
			},
			"engines": {
				"node": ">= 0.6"
			}
		},
		"node_modules/typed-array-buffer": {
			"version": "1.0.3",
			"resolved": "https://registry.npmjs.org/typed-array-buffer/-/typed-array-buffer-1.0.3.tgz",
			"integrity": "sha512-nAYYwfY3qnzX30IkA6AQZjVbtK6duGontcQm1WSG1MD94YLqK0515GNApXkoxKOWMusVssAHWLh9SeaoefYFGw==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3",
				"es-errors": "^1.3.0",
				"is-typed-array": "^1.1.14"
			},
			"engines": {
				"node": ">= 0.4"
			}
		},
		"node_modules/typed-array-byte-length": {
			"version": "1.0.3",
			"resolved": "https://registry.npmjs.org/typed-array-byte-length/-/typed-array-byte-length-1.0.3.tgz",
			"integrity": "sha512-BaXgOuIxz8n8pIq3e7Atg/7s+DpiYrxn4vdot3w9KbnBhcRQq6o3xemQdIfynqSeXeDrF32x+WvfzmOjPiY9lg==",
			"license": "MIT",
			"dependencies": {
				"call-bind": "^1.0.8",
				"for-each": "^0.3.3",
				"gopd": "^1.2.0",
				"has-proto": "^1.2.0",
				"is-typed-array": "^1.1.14"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/typed-array-byte-offset": {
			"version": "1.0.4",
			"resolved": "https://registry.npmjs.org/typed-array-byte-offset/-/typed-array-byte-offset-1.0.4.tgz",
			"integrity": "sha512-bTlAFB/FBYMcuX81gbL4OcpH5PmlFHqlCCpAl8AlEzMz5k53oNDvN8p1PNOWLEmI2x4orp3raOFB51tv9X+MFQ==",
			"license": "MIT",
			"dependencies": {
				"available-typed-arrays": "^1.0.7",
				"call-bind": "^1.0.8",
				"for-each": "^0.3.3",
				"gopd": "^1.2.0",
				"has-proto": "^1.2.0",
				"is-typed-array": "^1.1.15",
				"reflect.getprototypeof": "^1.0.9"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/typed-array-length": {
			"version": "1.0.7",
			"resolved": "https://registry.npmjs.org/typed-array-length/-/typed-array-length-1.0.7.tgz",
			"integrity": "sha512-3KS2b+kL7fsuk/eJZ7EQdnEmQoaho/r6KUef7hxvltNA5DR8NAUM+8wJMbJyZ4G9/7i3v5zPBIMN5aybAh2/Jg==",
			"license": "MIT",
			"dependencies": {
				"call-bind": "^1.0.7",
				"for-each": "^0.3.3",
				"gopd": "^1.0.1",
				"is-typed-array": "^1.1.13",
				"possible-typed-array-names": "^1.0.0",
				"reflect.getprototypeof": "^1.0.6"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/typescript": {
			"version": "5.9.3",
			"resolved": "https://registry.npmjs.org/typescript/-/typescript-5.9.3.tgz",
			"integrity": "sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw==",
			"license": "Apache-2.0",
			"peer": true,
			"bin": {
				"tsc": "bin/tsc",
				"tsserver": "bin/tsserver"
			},
			"engines": {
				"node": ">=14.17"
			}
		},
		"node_modules/unbox-primitive": {
			"version": "1.1.0",
			"resolved": "https://registry.npmjs.org/unbox-primitive/-/unbox-primitive-1.1.0.tgz",
			"integrity": "sha512-nWJ91DjeOkej/TA8pXQ3myruKpKEYgqvpw9lz4OPHj/NWFNluYrjbz9j01CJ8yKQd2g4jFoOkINCTW2I5LEEyw==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.3",
				"has-bigints": "^1.0.2",
				"has-symbols": "^1.1.0",
				"which-boxed-primitive": "^1.1.1"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/unbzip2-stream": {
			"version": "1.4.3",
			"resolved": "https://registry.npmjs.org/unbzip2-stream/-/unbzip2-stream-1.4.3.tgz",
			"integrity": "sha512-mlExGW4w71ebDJviH16lQLtZS32VKqsSfk80GCfUlwT/4/hNRFsoscrF/c++9xinkMzECL1uL9DDwXqFWkruPg==",
			"license": "MIT",
			"dependencies": {
				"buffer": "^5.2.1",
				"through": "^2.3.8"
			}
		},
		"node_modules/undici-types": {
			"version": "7.16.0",
			"resolved": "https://registry.npmjs.org/undici-types/-/undici-types-7.16.0.tgz",
			"integrity": "sha512-Zz+aZWSj8LE6zoxD+xrjh4VfkIG8Ya6LvYkZqtUQGJPZjYl53ypCaUwWqo7eI0x66KBGeRo+mlBEkMSeSZ38Nw==",
			"license": "MIT"
		},
		"node_modules/unified": {
			"version": "11.0.5",
			"resolved": "https://registry.npmjs.org/unified/-/unified-11.0.5.tgz",
			"integrity": "sha512-xKvGhPWw3k84Qjh8bI3ZeJjqnyadK+GEFtazSfZv/rKeTkTjOJho6mFqh2SM96iIcZokxiOpg78GazTSg8+KHA==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0",
				"bail": "^2.0.0",
				"devlop": "^1.0.0",
				"extend": "^3.0.0",
				"is-plain-obj": "^4.0.0",
				"trough": "^2.0.0",
				"vfile": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-builder": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/unist-builder/-/unist-builder-4.0.0.tgz",
			"integrity": "sha512-wmRFnH+BLpZnTKpc5L7O67Kac89s9HMrtELpnNaE6TAobq5DTZZs5YaTQfAZBA9bFPECx2uVAPO31c+GVug8mg==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-util-find-after": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/unist-util-find-after/-/unist-util-find-after-5.0.0.tgz",
			"integrity": "sha512-amQa0Ep2m6hE2g72AugUItjbuM8X8cGQnFoHk0pGfrFeT9GZhzN5SW8nRsiGKK7Aif4CrACPENkA6P/Lw6fHGQ==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0",
				"unist-util-is": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-util-is": {
			"version": "6.0.1",
			"resolved": "https://registry.npmjs.org/unist-util-is/-/unist-util-is-6.0.1.tgz",
			"integrity": "sha512-LsiILbtBETkDz8I9p1dQ0uyRUWuaQzd/cuEeS1hoRSyW5E5XGmTzlwY1OrNzzakGowI9Dr/I8HVaw4hTtnxy8g==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-util-map": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/unist-util-map/-/unist-util-map-4.0.0.tgz",
			"integrity": "sha512-HJs1tpkSmRJUzj6fskQrS5oYhBYlmtcvy4SepdDEEsL04FjBrgF0Mgggvxc1/qGBGgW7hRh9+UBK1aqTEnBpIA==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-util-modify-children": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/unist-util-modify-children/-/unist-util-modify-children-4.0.0.tgz",
			"integrity": "sha512-+tdN5fGNddvsQdIzUF3Xx82CU9sMM+fA0dLgR9vOmT0oPT2jH+P1nd5lSqfCfXAw+93NhcXNY2qqvTUtE4cQkw==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0",
				"array-iterate": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-util-position": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/unist-util-position/-/unist-util-position-5.0.0.tgz",
			"integrity": "sha512-fucsC7HjXvkB5R3kTCO7kUjRdrS0BJt3M/FPxmHMBOm8JQi2BsHAHFsy27E0EolP8rp0NzXsJ+jNPyDWvOJZPA==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-util-position-from-estree": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/unist-util-position-from-estree/-/unist-util-position-from-estree-2.0.0.tgz",
			"integrity": "sha512-KaFVRjoqLyF6YXCbVLNad/eS4+OfPQQn2yOd7zF/h5T/CSL2v8NpN6a5TPvtbXthAGw5nG+PuTtq+DdIZr+cRQ==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-util-remove": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/unist-util-remove/-/unist-util-remove-4.0.0.tgz",
			"integrity": "sha512-b4gokeGId57UVRX/eVKej5gXqGlc9+trkORhFJpu9raqZkZhU0zm8Doi05+HaiBsMEIJowL+2WtQ5ItjsngPXg==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0",
				"unist-util-is": "^6.0.0",
				"unist-util-visit-parents": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-util-remove-position": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/unist-util-remove-position/-/unist-util-remove-position-5.0.0.tgz",
			"integrity": "sha512-Hp5Kh3wLxv0PHj9m2yZhhLt58KzPtEYKQQ4yxfYFEO7EvHwzyDYnduhHnY1mDxoqr7VUwVuHXk9RXKIiYS1N8Q==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0",
				"unist-util-visit": "^5.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-util-stringify-position": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/unist-util-stringify-position/-/unist-util-stringify-position-4.0.0.tgz",
			"integrity": "sha512-0ASV06AAoKCDkS2+xw5RXJywruurpbC4JZSm7nr7MOt1ojAzvyyaO+UxZf18j8FCF6kmzCZKcAgN/yu2gm2XgQ==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-util-visit": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/unist-util-visit/-/unist-util-visit-5.0.0.tgz",
			"integrity": "sha512-MR04uvD+07cwl/yhVuVWAtw+3GOR/knlL55Nd/wAdblk27GCVt3lqpTivy/tkJcZoNPzTwS1Y+KMojlLDhoTzg==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0",
				"unist-util-is": "^6.0.0",
				"unist-util-visit-parents": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-util-visit-children": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/unist-util-visit-children/-/unist-util-visit-children-3.0.0.tgz",
			"integrity": "sha512-RgmdTfSBOg04sdPcpTSD1jzoNBjt9a80/ZCzp5cI9n1qPzLZWF9YdvWGN2zmTumP1HWhXKdUWexjy/Wy/lJ7tA==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/unist-util-visit-parents": {
			"version": "6.0.1",
			"resolved": "https://registry.npmjs.org/unist-util-visit-parents/-/unist-util-visit-parents-6.0.1.tgz",
			"integrity": "sha512-L/PqWzfTP9lzzEa6CKs0k2nARxTdZduw3zyh8d2NVBnsyvHjSX4TWse388YrrQKbvI8w20fGjGlhgT96WwKykw==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0",
				"unist-util-is": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/universalify": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/universalify/-/universalify-2.0.1.tgz",
			"integrity": "sha512-gptHNQghINnc/vTGIk0SOFGFNXw7JVrlRUtConJRlvaw6DuX0wO5Jeko9sWrMBhh+PsYAZ7oXAiOnf/UKogyiw==",
			"license": "MIT",
			"engines": {
				"node": ">= 10.0.0"
			}
		},
		"node_modules/unpipe": {
			"version": "1.0.0",
			"resolved": "https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz",
			"integrity": "sha512-pjy2bYhSsufwWlKwPc+l3cN7+wuJlK6uz0YdJEOlQDbl6jo/YlPi4mb8agUkVC8BF7V8NuzeyPNqRksA3hztKQ==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/urijs": {
			"version": "1.19.11",
			"resolved": "https://registry.npmjs.org/urijs/-/urijs-1.19.11.tgz",
			"integrity": "sha512-HXgFDgDommxn5/bIv0cnQZsPhHDA90NPHD6+c/v21U5+Sx5hoP8+dP9IZXBU1gIfvdRfhG8cel9QNPeionfcCQ==",
			"license": "MIT"
		},
		"node_modules/urlpattern-polyfill": {
			"version": "10.0.0",
			"resolved": "https://registry.npmjs.org/urlpattern-polyfill/-/urlpattern-polyfill-10.0.0.tgz",
			"integrity": "sha512-H/A06tKD7sS1O1X2SshBVeA5FLycRpjqiBeqGKmBwBDBy28EnRjORxTNe269KSSr5un5qyWi1iL61wLxpd+ZOg==",
			"license": "MIT"
		},
		"node_modules/use-callback-ref": {
			"version": "1.3.3",
			"resolved": "https://registry.npmjs.org/use-callback-ref/-/use-callback-ref-1.3.3.tgz",
			"integrity": "sha512-jQL3lRnocaFtu3V00JToYz/4QkNWswxijDaCVNZRiRTO3HQDLsdu1ZtmIUvV4yPp+rvWm5j0y0TG/S61cuijTg==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"tslib": "^2.0.0"
			},
			"engines": {
				"node": ">=10"
			},
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/use-callback-ref/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD",
			"peer": true
		},
		"node_modules/use-sidecar": {
			"version": "1.1.3",
			"resolved": "https://registry.npmjs.org/use-sidecar/-/use-sidecar-1.1.3.tgz",
			"integrity": "sha512-Fedw0aZvkhynoPYlA5WXrMCAMm+nSWdZt6lzJQ7Ok8S6Q+VsHmHpRWndVRJ8Be0ZbkfPc5LRYH+5XrzXcEeLRQ==",
			"license": "MIT",
			"peer": true,
			"dependencies": {
				"detect-node-es": "^1.1.0",
				"tslib": "^2.0.0"
			},
			"engines": {
				"node": ">=10"
			},
			"peerDependencies": {
				"@types/react": "*",
				"react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc"
			},
			"peerDependenciesMeta": {
				"@types/react": {
					"optional": true
				}
			}
		},
		"node_modules/use-sidecar/node_modules/tslib": {
			"version": "2.8.1",
			"resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
			"integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
			"license": "0BSD",
			"peer": true
		},
		"node_modules/util-deprecate": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
			"integrity": "sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw==",
			"license": "MIT"
		},
		"node_modules/utility-types": {
			"version": "3.11.0",
			"resolved": "https://registry.npmjs.org/utility-types/-/utility-types-3.11.0.tgz",
			"integrity": "sha512-6Z7Ma2aVEWisaL6TvBCy7P8rm2LQoPv6dJ7ecIaIixHcwfbJ0x7mWdbcwlIM5IGQxPZSFYeqRCqlOOeKoJYMkw==",
			"license": "MIT",
			"engines": {
				"node": ">= 4"
			}
		},
		"node_modules/utils-merge": {
			"version": "1.0.1",
			"resolved": "https://registry.npmjs.org/utils-merge/-/utils-merge-1.0.1.tgz",
			"integrity": "sha512-pMZTvIkT1d+TFGvDOqodOclx0QWkkgi6Tdoa8gC8ffGAAqz9pzPTZWAybbsHHoED/ztMtkv/VoYTYyShUn81hA==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.4.0"
			}
		},
		"node_modules/uuid": {
			"version": "11.1.0",
			"resolved": "https://registry.npmjs.org/uuid/-/uuid-11.1.0.tgz",
			"integrity": "sha512-0/A9rDy9P7cJ+8w1c9WD9V//9Wj15Ce2MPz8Ri6032usz+NfePxx5AcN3bN+r6ZL6jEo066/yNYB3tn4pQEx+A==",
			"funding": [
				"https://github.com/sponsors/broofa",
				"https://github.com/sponsors/ctavan"
			],
			"license": "MIT",
			"bin": {
				"uuid": "dist/esm/bin/uuid"
			}
		},
		"node_modules/vary": {
			"version": "1.1.2",
			"resolved": "https://registry.npmjs.org/vary/-/vary-1.1.2.tgz",
			"integrity": "sha512-BNGbWLfd0eUPabhkXUVm0j8uuvREyTh5ovRa/dyow/BqAbZJyC+5fU+IzQOzmAKzYqYRAISoRhdQr3eIZ/PXqg==",
			"license": "MIT",
			"engines": {
				"node": ">= 0.8"
			}
		},
		"node_modules/vfile": {
			"version": "6.0.3",
			"resolved": "https://registry.npmjs.org/vfile/-/vfile-6.0.3.tgz",
			"integrity": "sha512-KzIbH/9tXat2u30jf+smMwFCsno4wHVdNmzFyL+T/L3UGqqk6JKfVqOFOZEpZSHADH1k40ab6NUIXZq422ov3Q==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0",
				"vfile-message": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/vfile-location": {
			"version": "5.0.3",
			"resolved": "https://registry.npmjs.org/vfile-location/-/vfile-location-5.0.3.tgz",
			"integrity": "sha512-5yXvWDEgqeiYiBe1lbxYF7UMAIm/IcopxMHrMQDq3nvKcjPKIhZklUKL+AE7J7uApI4kwe2snsK+eI6UTj9EHg==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0",
				"vfile": "^6.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/vfile-matter": {
			"version": "5.0.1",
			"resolved": "https://registry.npmjs.org/vfile-matter/-/vfile-matter-5.0.1.tgz",
			"integrity": "sha512-o6roP82AiX0XfkyTHyRCMXgHfltUNlXSEqCIS80f+mbAyiQBE2fxtDVMtseyytGx75sihiJFo/zR6r/4LTs2Cw==",
			"license": "MIT",
			"dependencies": {
				"vfile": "^6.0.0",
				"yaml": "^2.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/vfile-message": {
			"version": "4.0.3",
			"resolved": "https://registry.npmjs.org/vfile-message/-/vfile-message-4.0.3.tgz",
			"integrity": "sha512-QTHzsGd1EhbZs4AsQ20JX1rC3cOlt/IWJruk893DfLRr57lcnOeMaWG4K0JrRta4mIJZKth2Au3mM3u03/JWKw==",
			"license": "MIT",
			"dependencies": {
				"@types/unist": "^3.0.0",
				"unist-util-stringify-position": "^4.0.0"
			},
			"funding": {
				"type": "opencollective",
				"url": "https://opencollective.com/unified"
			}
		},
		"node_modules/web-namespaces": {
			"version": "2.0.1",
			"resolved": "https://registry.npmjs.org/web-namespaces/-/web-namespaces-2.0.1.tgz",
			"integrity": "sha512-bKr1DkiNa2krS7qxNtdrtHAmzuYGFQLiQ13TsorsdT6ULTkPLKuu5+GsFpDlg6JFjUTwX2DyhMPG2be8uPrqsQ==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		},
		"node_modules/webidl-conversions": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/webidl-conversions/-/webidl-conversions-3.0.1.tgz",
			"integrity": "sha512-2JAn3z8AR6rjK8Sm8orRC0h/bcl/DqL7tRPdGZ4I1CjdF+EaMLmYxBHyXuKL849eucPFhvBoxMsflfOb8kxaeQ==",
			"license": "BSD-2-Clause"
		},
		"node_modules/whatwg-url": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/whatwg-url/-/whatwg-url-5.0.0.tgz",
			"integrity": "sha512-saE57nupxk6v3HY35+jzBwYa0rKSy0XR8JSxZPwgLr7ys0IBzhGviA1/TUGJLmSVqs8pb9AnvICXEuOHLprYTw==",
			"license": "MIT",
			"dependencies": {
				"tr46": "~0.0.3",
				"webidl-conversions": "^3.0.0"
			}
		},
		"node_modules/which-boxed-primitive": {
			"version": "1.1.1",
			"resolved": "https://registry.npmjs.org/which-boxed-primitive/-/which-boxed-primitive-1.1.1.tgz",
			"integrity": "sha512-TbX3mj8n0odCBFVlY8AxkqcHASw3L60jIuF8jFP78az3C2YhmGvqbHBpAjTRH2/xqYunrJ9g1jSyjCjpoWzIAA==",
			"license": "MIT",
			"dependencies": {
				"is-bigint": "^1.1.0",
				"is-boolean-object": "^1.2.1",
				"is-number-object": "^1.1.1",
				"is-string": "^1.1.1",
				"is-symbol": "^1.1.1"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/which-builtin-type": {
			"version": "1.2.1",
			"resolved": "https://registry.npmjs.org/which-builtin-type/-/which-builtin-type-1.2.1.tgz",
			"integrity": "sha512-6iBczoX+kDQ7a3+YJBnh3T+KZRxM/iYNPXicqk66/Qfm1b93iu+yOImkg0zHbj5LNOcNv1TEADiZ0xa34B4q6Q==",
			"license": "MIT",
			"dependencies": {
				"call-bound": "^1.0.2",
				"function.prototype.name": "^1.1.6",
				"has-tostringtag": "^1.0.2",
				"is-async-function": "^2.0.0",
				"is-date-object": "^1.1.0",
				"is-finalizationregistry": "^1.1.0",
				"is-generator-function": "^1.0.10",
				"is-regex": "^1.2.1",
				"is-weakref": "^1.0.2",
				"isarray": "^2.0.5",
				"which-boxed-primitive": "^1.1.0",
				"which-collection": "^1.0.2",
				"which-typed-array": "^1.1.16"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/which-collection": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/which-collection/-/which-collection-1.0.2.tgz",
			"integrity": "sha512-K4jVyjnBdgvc86Y6BkaLZEN933SwYOuBFkdmBu9ZfkcAbdVbpITnDmjvZ/aQjRXQrv5EPkTnD1s39GiiqbngCw==",
			"license": "MIT",
			"dependencies": {
				"is-map": "^2.0.3",
				"is-set": "^2.0.3",
				"is-weakmap": "^2.0.2",
				"is-weakset": "^2.0.3"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/which-typed-array": {
			"version": "1.1.20",
			"resolved": "https://registry.npmjs.org/which-typed-array/-/which-typed-array-1.1.20.tgz",
			"integrity": "sha512-LYfpUkmqwl0h9A2HL09Mms427Q1RZWuOHsukfVcKRq9q95iQxdw0ix1JQrqbcDR9PH1QDwf5Qo8OZb5lksZ8Xg==",
			"license": "MIT",
			"dependencies": {
				"available-typed-arrays": "^1.0.7",
				"call-bind": "^1.0.8",
				"call-bound": "^1.0.4",
				"for-each": "^0.3.5",
				"get-proto": "^1.0.1",
				"gopd": "^1.2.0",
				"has-tostringtag": "^1.0.2"
			},
			"engines": {
				"node": ">= 0.4"
			},
			"funding": {
				"url": "https://github.com/sponsors/ljharb"
			}
		},
		"node_modules/widest-line": {
			"version": "5.0.0",
			"resolved": "https://registry.npmjs.org/widest-line/-/widest-line-5.0.0.tgz",
			"integrity": "sha512-c9bZp7b5YtRj2wOe6dlj32MK+Bx/M/d+9VB2SHM1OtsUHR0aV0tdP6DWh/iMt0kWi1t5g1Iudu6hQRNd1A4PVA==",
			"license": "MIT",
			"dependencies": {
				"string-width": "^7.0.0"
			},
			"engines": {
				"node": ">=18"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/wrap-ansi": {
			"version": "6.2.0",
			"resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-6.2.0.tgz",
			"integrity": "sha512-r6lPcBGxZXlIcymEu7InxDMhdW0KDxpLgoFLcguasxCaJ/SOIZwINatK9KY/tf+ZrlywOKU0UDj3ATXUBfxJXA==",
			"license": "MIT",
			"dependencies": {
				"ansi-styles": "^4.0.0",
				"string-width": "^4.1.0",
				"strip-ansi": "^6.0.0"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/wrap-ansi/node_modules/ansi-regex": {
			"version": "5.0.1",
			"resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
			"integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
			"license": "MIT",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/wrap-ansi/node_modules/ansi-styles": {
			"version": "4.3.0",
			"resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
			"integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
			"license": "MIT",
			"dependencies": {
				"color-convert": "^2.0.1"
			},
			"engines": {
				"node": ">=8"
			},
			"funding": {
				"url": "https://github.com/chalk/ansi-styles?sponsor=1"
			}
		},
		"node_modules/wrap-ansi/node_modules/emoji-regex": {
			"version": "8.0.0",
			"resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
			"integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
			"license": "MIT"
		},
		"node_modules/wrap-ansi/node_modules/is-fullwidth-code-point": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz",
			"integrity": "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==",
			"license": "MIT",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/wrap-ansi/node_modules/string-width": {
			"version": "4.2.3",
			"resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
			"integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
			"license": "MIT",
			"dependencies": {
				"emoji-regex": "^8.0.0",
				"is-fullwidth-code-point": "^3.0.0",
				"strip-ansi": "^6.0.1"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/wrap-ansi/node_modules/strip-ansi": {
			"version": "6.0.1",
			"resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
			"integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
			"license": "MIT",
			"dependencies": {
				"ansi-regex": "^5.0.1"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/wrappy": {
			"version": "1.0.2",
			"resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
			"integrity": "sha512-l4Sp/DRseor9wL6EvV2+TuQn63dMkPjZ/sp9XkghTEbV9KlPS1xUsZ3u7/IQO4wxtcFB4bgpQPRcR3QCvezPcQ==",
			"license": "ISC"
		},
		"node_modules/ws": {
			"version": "8.19.0",
			"resolved": "https://registry.npmjs.org/ws/-/ws-8.19.0.tgz",
			"integrity": "sha512-blAT2mjOEIi0ZzruJfIhb3nps74PRWTCz1IjglWEEpQl5XS/UNama6u2/rjFkDDouqr4L67ry+1aGIALViWjDg==",
			"license": "MIT",
			"engines": {
				"node": ">=10.0.0"
			},
			"peerDependencies": {
				"bufferutil": "^4.0.1",
				"utf-8-validate": ">=5.0.2"
			},
			"peerDependenciesMeta": {
				"bufferutil": {
					"optional": true
				},
				"utf-8-validate": {
					"optional": true
				}
			}
		},
		"node_modules/xml2js": {
			"version": "0.6.2",
			"resolved": "https://registry.npmjs.org/xml2js/-/xml2js-0.6.2.tgz",
			"integrity": "sha512-T4rieHaC1EXcES0Kxxj4JWgaUQHDk+qwHcYOCFHfiwKz7tOVPLq7Hjq9dM1WCMhylqMEfP7hMcOIChvotiZegA==",
			"license": "MIT",
			"dependencies": {
				"sax": ">=0.6.0",
				"xmlbuilder": "~11.0.0"
			},
			"engines": {
				"node": ">=4.0.0"
			}
		},
		"node_modules/xmlbuilder": {
			"version": "11.0.1",
			"resolved": "https://registry.npmjs.org/xmlbuilder/-/xmlbuilder-11.0.1.tgz",
			"integrity": "sha512-fDlsI/kFEx7gLvbecc0/ohLG50fugQp8ryHzMTuW9vSa1GJ0XYWKnhsUx7oie3G98+r56aTQIUB4kht42R3JvA==",
			"license": "MIT",
			"engines": {
				"node": ">=4.0"
			}
		},
		"node_modules/y18n": {
			"version": "5.0.8",
			"resolved": "https://registry.npmjs.org/y18n/-/y18n-5.0.8.tgz",
			"integrity": "sha512-0pfFzegeDWJHJIAmTLRP2DwHjdF5s7jo9tuztdQxAhINCdvS+3nGINqPd00AphqJR/0LhANUS6/+7SCb98YOfA==",
			"license": "ISC",
			"engines": {
				"node": ">=10"
			}
		},
		"node_modules/yallist": {
			"version": "4.0.0",
			"resolved": "https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz",
			"integrity": "sha512-3wdGidZyq5PB084XLES5TpOSRA3wjXAlIWMhum2kRcv/41Sn2emQ0dycQW4uZXLejwKvg6EsvbdlVL+FYEct7A==",
			"license": "ISC"
		},
		"node_modules/yaml": {
			"version": "2.8.2",
			"resolved": "https://registry.npmjs.org/yaml/-/yaml-2.8.2.tgz",
			"integrity": "sha512-mplynKqc1C2hTVYxd0PU2xQAc22TI1vShAYGksCCfxbn/dFwnHTNi1bvYsBTkhdUNtGIf5xNOg938rrSSYvS9A==",
			"license": "ISC",
			"bin": {
				"yaml": "bin.mjs"
			},
			"engines": {
				"node": ">= 14.6"
			},
			"funding": {
				"url": "https://github.com/sponsors/eemeli"
			}
		},
		"node_modules/yargs": {
			"version": "17.7.1",
			"resolved": "https://registry.npmjs.org/yargs/-/yargs-17.7.1.tgz",
			"integrity": "sha512-cwiTb08Xuv5fqF4AovYacTFNxk62th7LKJ6BL9IGUpTJrWoU7/7WdQGTP2SjKf1dUNBGzDd28p/Yfs/GI6JrLw==",
			"license": "MIT",
			"dependencies": {
				"cliui": "^8.0.1",
				"escalade": "^3.1.1",
				"get-caller-file": "^2.0.5",
				"require-directory": "^2.1.1",
				"string-width": "^4.2.3",
				"y18n": "^5.0.5",
				"yargs-parser": "^21.1.1"
			},
			"engines": {
				"node": ">=12"
			}
		},
		"node_modules/yargs-parser": {
			"version": "21.1.1",
			"resolved": "https://registry.npmjs.org/yargs-parser/-/yargs-parser-21.1.1.tgz",
			"integrity": "sha512-tVpsJW7DdjecAiFpbIB1e3qxIQsE6NoPc5/eTdrbbIC4h0LVsWhnoa3g+m2HclBIujHzsxZ4VJVA+GUuc2/LBw==",
			"license": "ISC",
			"engines": {
				"node": ">=12"
			}
		},
		"node_modules/yargs/node_modules/ansi-regex": {
			"version": "5.0.1",
			"resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
			"integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
			"license": "MIT",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/yargs/node_modules/emoji-regex": {
			"version": "8.0.0",
			"resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
			"integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
			"license": "MIT"
		},
		"node_modules/yargs/node_modules/is-fullwidth-code-point": {
			"version": "3.0.0",
			"resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz",
			"integrity": "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==",
			"license": "MIT",
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/yargs/node_modules/string-width": {
			"version": "4.2.3",
			"resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
			"integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
			"license": "MIT",
			"dependencies": {
				"emoji-regex": "^8.0.0",
				"is-fullwidth-code-point": "^3.0.0",
				"strip-ansi": "^6.0.1"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/yargs/node_modules/strip-ansi": {
			"version": "6.0.1",
			"resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
			"integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
			"license": "MIT",
			"dependencies": {
				"ansi-regex": "^5.0.1"
			},
			"engines": {
				"node": ">=8"
			}
		},
		"node_modules/yauzl": {
			"version": "2.10.0",
			"resolved": "https://registry.npmjs.org/yauzl/-/yauzl-2.10.0.tgz",
			"integrity": "sha512-p4a9I6X6nu6IhoGmBqAcbJy1mlC4j27vEPZX9F4L4/vZT3Lyq1VkFHw/V/PUcB9Buo+DG3iHkT0x3Qya58zc3g==",
			"license": "MIT",
			"dependencies": {
				"buffer-crc32": "~0.2.3",
				"fd-slicer": "~1.1.0"
			}
		},
		"node_modules/yoctocolors-cjs": {
			"version": "2.1.3",
			"resolved": "https://registry.npmjs.org/yoctocolors-cjs/-/yoctocolors-cjs-2.1.3.tgz",
			"integrity": "sha512-U/PBtDf35ff0D8X8D0jfdzHYEPFxAI7jJlxZXwCSez5M3190m+QobIfh+sWDWSHMCWWJN2AWamkegn6vr6YBTw==",
			"license": "MIT",
			"engines": {
				"node": ">=18"
			},
			"funding": {
				"url": "https://github.com/sponsors/sindresorhus"
			}
		},
		"node_modules/yoga-layout": {
			"version": "3.2.1",
			"resolved": "https://registry.npmjs.org/yoga-layout/-/yoga-layout-3.2.1.tgz",
			"integrity": "sha512-0LPOt3AxKqMdFBZA3HBAt/t/8vIKq7VaQYbuA8WxCgung+p9TVyKRYdpvCb80HcdTN2NkbIKbhNwKUfm3tQywQ==",
			"license": "MIT"
		},
		"node_modules/zod": {
			"version": "3.21.4",
			"resolved": "https://registry.npmjs.org/zod/-/zod-3.21.4.tgz",
			"integrity": "sha512-m46AKbrzKVzOzs/DZgVnG5H55N1sv1M8qZU3A8RIKbs3mrACDNeIOeilDymVb2HdmP8uwshOCF4uJ8uM9rCqJw==",
			"license": "MIT",
			"funding": {
				"url": "https://github.com/sponsors/colinhacks"
			}
		},
		"node_modules/zod-to-json-schema": {
			"version": "3.20.4",
			"resolved": "https://registry.npmjs.org/zod-to-json-schema/-/zod-to-json-schema-3.20.4.tgz",
			"integrity": "sha512-Un9+kInJ2Zt63n6Z7mLqBifzzPcOyX+b+Exuzf7L1+xqck9Q2EPByyTRduV3kmSPaXaRer1JCsucubpgL1fipg==",
			"license": "ISC",
			"peerDependencies": {
				"zod": "^3.20.0"
			}
		},
		"node_modules/zwitch": {
			"version": "2.0.4",
			"resolved": "https://registry.npmjs.org/zwitch/-/zwitch-2.0.4.tgz",
			"integrity": "sha512-bXE4cR/kVZhKZX/RjPEflHaKVhUVl85noU3v6b8apfQEc1x4A+zBxjZ4lN8LqGd6WZ3dl98pY4o717VFmoPp+A==",
			"license": "MIT",
			"funding": {
				"type": "github",
				"url": "https://github.com/sponsors/wooorm"
			}
		}
	}
}



---

# FILE: docs/package.json

{
	"name": "docs",
	"version": "1.0.0",
	"main": "index.js",
	"scripts": {
		"test": "echo \"Error: no test specified\" && exit 1",
		"dev": "mintlify dev",
		"check": "mintlify broken-links",
		"rename": "mintlify rename"
	},
	"keywords": [],
	"author": "",
	"license": "ISC",
	"description": "",
	"dependencies": {
		"mintlify": "^4.2.338"
	},
	"overrides": {
		"tar-fs": "^3.1.1",
		"js-yaml": "^4.1.1",
		"tar@<=6.2.1": "6.2.1",
		"body-parser@<=1.20.3": "1.20.3",
		"axios@<=1.13.5": "1.13.5",
		"qs@<=6.14.1": "6.14.1",
		"express@<=4.20.0": "4.20.0",
		"serve-static@<=1.16.0": "1.16.0",
		"send@<=0.19.0": "0.19.0",
		"path-to-regexp@<=0.1.12": "0.1.12",
		"cookie@<=0.7.0": "0.7.0"
	}
}



---

# FILE: src/core/README.md

# Core Architecture

Extension entry point (extension.ts) -> webview -> controller -> task

```tree
core/
├── webview/      # Manages webview lifecycle
├── controller/   # Handles webview messages and task management
├── task/         # Executes API requests and tool operations
└── ...           # Additional components to help with context, parsing user/assistant messages, etc.
```



---

# FILE: src/core/hooks/__tests__/fixtures/README.md

# Hook Test Fixtures

This directory contains pre-written hook scripts for testing the Cline hooks system.

## Directory Structure

```
fixtures/
├── hooks/
│   ├── pretooluse/       # PreToolUse hook fixtures
│   │   ├── success/      # Returns success immediately
│   │   ├── blocking/     # Blocks tool execution
│   │   ├── context-injection/  # Adds context with type prefix
│   │   └── error/        # Exits with error code
│   ├── posttooluse/      # PostToolUse hook fixtures
│   │   ├── success/      # Returns success immediately
│   │   └── error/        # Exits with error code
│   └── template/         # Template for new hooks
└── inputs/               # Sample input data (future)
```

## Using Fixtures in Tests

### With loadFixture()

The `loadFixture()` helper function copies a fixture to your test environment:

```typescript
import { loadFixture } from '../test-utils'

it("should work with real hook", async () => {
  const { getEnv } = setupHookTests()
  
  await loadFixture("hooks/pretooluse/success", getEnv().tempDir)
  
  const factory = new HookFactory()
  const runner = await factory.create("PreToolUse")
  const result = await runner.run(buildPreToolUseInput({ toolName: "test_tool" }))
  
  result.cancel.should.be.false()
})
```

### Direct File Copy

For more control, you can also manually copy fixture files.

## Available Fixtures

### PreToolUse Hooks

#### `hooks/pretooluse/success`
- **Returns**: `{ cancel: false, contextModification: "PreToolUse hook executed successfully", errorMessage: "" }`
- **Use for**: Testing happy path scenarios

#### `hooks/pretooluse/blocking`
- **Returns**: `{ cancel: true, contextModification: "", errorMessage: "Tool execution blocked by hook" }`
- **Use for**: Testing tool execution blocking

#### `hooks/pretooluse/context-injection`
- **Returns**: `{ cancel: false, contextModification: "WORKSPACE_RULES: Tool [toolName] requires review", errorMessage: "" }`
- **Use for**: Testing context injection with type prefixes
- **Note**: Dynamically includes tool name from input

#### `hooks/pretooluse/error`
- **Behavior**: Prints error to stderr and exits with code 1
- **Use for**: Testing error handling

### PostToolUse Hooks

#### `hooks/posttooluse/success`
- **Returns**: `{ cancel: false, contextModification: "PostToolUse hook executed successfully", errorMessage: "" }`
- **Use for**: Testing PostToolUse execution

#### `hooks/posttooluse/error`
- **Behavior**: Prints error to stderr and exits with code 1
- **Use for**: Testing error handling in PostToolUse

### UserPromptSubmit Hooks

#### `hooks/userpromptsubmit/success`
- **Returns**: `{ cancel: false, contextModification: "Prompt approved", errorMessage: "" }`
- **Use for**: Testing successful prompt submission

#### `hooks/userpromptsubmit/blocking`
- **Returns**: `{ cancel: true, contextModification: "", errorMessage: "Prompt violates policy" }`
- **Use for**: Testing prompt submission blocking

#### `hooks/userpromptsubmit/context-injection`
- **Returns**: `{ cancel: false, contextModification: "CONTEXT_INJECTION: User is in plan mode", errorMessage: "" }`
- **Use for**: Testing context injection into task request

#### `hooks/userpromptsubmit/multiline`
- **Returns**: `{ cancel: false, contextModification: "Line count: N", errorMessage: "" }`
- **Use for**: Testing multiline prompt handling
- **Note**: Dynamically counts newlines in the prompt

#### `hooks/userpromptsubmit/large-prompt`
- **Returns**: `{ cancel: false, contextModification: "Prompt size: N", errorMessage: "" }`
- **Use for**: Testing large prompt handling
- **Note**: Dynamically reports prompt character count

#### `hooks/userpromptsubmit/special-chars`
- **Returns**: `{ cancel: false, contextModification: "Special chars preserved" | "Missing special chars", errorMessage: "" }`
- **Use for**: Testing special character preservation
- **Note**: Checks for @, #, and $ characters

#### `hooks/userpromptsubmit/empty-prompt`
- **Returns**: `{ cancel: false, contextModification: "Prompt length: 0", errorMessage: "" }`
- **Use for**: Testing empty prompt handling
- **Note**: Safely handles undefined or empty prompts

#### `hooks/userpromptsubmit/malformed-json`
- **Behavior**: Outputs invalid JSON ("not valid json")
- **Use for**: Testing malformed JSON error handling

#### `hooks/userpromptsubmit/error`
- **Behavior**: Prints error to stderr and exits with code 1
- **Use for**: Testing error handling in UserPromptSubmit

### TaskStart Hooks

#### `hooks/taskstart/success`
- **Returns**: `{ cancel: false, contextModification: "TaskStart hook executed successfully", errorMessage: "" }`
- **Use for**: Testing TaskStart hook success path, allowing task to proceed

#### `hooks/taskstart/blocking`
- **Returns**: `{ cancel: true, contextModification: "", errorMessage: "Task execution blocked by hook" }`
- **Use for**: Testing task blocking at start (e.g., policy enforcement)

#### `hooks/taskstart/error`
- **Behavior**: Prints error to stderr and exits with code 1
- **Use for**: Testing error handling in TaskStart hooks

## Platform Considerations

Hooks run cross-platform, but runtime differs by OS:

- **Linux/macOS**: executable hook files run directly (shebang/executable bit)
- **Windows**: hooks execute through PowerShell; tests may use a small PowerShell bridge script that pipes stdin to a Node companion file

### Creating New Fixtures

1. Create a new directory under the appropriate hook type
2. Add the hook script with shebang `#!/usr/bin/env node`
3. Make executable: `chmod +x HookName`
4. Update this README with the new fixture

### Example: Creating a new fixture

```bash
# Create directory
mkdir -p src/core/hooks/__tests__/fixtures/hooks/pretooluse/my-new-scenario

# Create hook script
cat > src/core/hooks/__tests__/fixtures/hooks/pretooluse/my-new-scenario/PreToolUse << 'EOF'
#!/usr/bin/env node
const input = JSON.parse(require('fs').readFileSync(0, 'utf-8'));
console.log(JSON.stringify({
  cancel: false,
  contextModification: "My custom context",
  errorMessage: ""
}));
EOF

# Make executable
chmod +x src/core/hooks/__tests__/fixtures/hooks/pretooluse/my-new-scenario/PreToolUse
```

## Maintenance

- Keep fixtures simple and focused on one scenario
- Fixtures are Node.js scripts that work across platforms
- Update this README when adding new fixtures
- Remove obsolete fixtures and update references



---

# FILE: src/core/hooks/__tests__/fixtures/template/README.md

# Hook Template for New Fixtures

This directory contains a template for creating new hook fixtures. When adding a new hook fixture, copy from this template and customize as needed.

## Files in This Template

- `HookName` - Hook script template (executable Node.js script)
- `README.md` - This file

## How to Create a New Fixture

### Step 1: Choose the Scenario Type

Decide what your hook fixture should test:
- `success` - Returns success immediately
- `blocking` - Blocks tool execution
- `context-injection` - Adds context information
- `error` - Exits with error code

### Step 2: Create the Directory Structure

```bash
# Example for a new PreToolUse validation fixture
mkdir -p src/core/hooks/__tests__/fixtures/hooks/pretooluse/validation/

# Copy template file
cp src/core/hooks/__tests__/fixtures/template/HookName src/core/hooks/__tests__/fixtures/hooks/pretooluse/validation/PreToolUse

# Make executable
chmod +x src/core/hooks/__tests__/fixtures/hooks/pretooluse/validation/PreToolUse
```

### Step 3: Customize the Hook Script

Edit the new fixture file to implement your specific logic:

```javascript
#!/usr/bin/env node

const input = JSON.parse(require('fs').readFileSync(0, 'utf-8'));

// Extract relevant data
const { toolName, parameters } = input.preToolUse;

let shouldContinue = true;
let contextModification = "";
let errorMessage = "";

// Your custom logic here
if (!parameters || !parameters.path) {
  shouldContinue = false;
  errorMessage = "ERROR: Tool requires a 'path' parameter";
} else {
  contextModification = "VALIDATION: Basic input validation passed";
}

// Return standardized output
console.log(JSON.stringify({
  shouldContinue,
  contextModification,
  errorMessage
}));
```

### Step 4: Update Documentation

Add your new fixture to `fixtures/README.md` with:
- Fixture path
- What it returns
- What it's used for testing
- Any special behavior notes

## Best Practices

### Keep Fixtures Focused
- Test one specific scenario per fixture
- Use simple, easy-to-understand logic
- Document complex behavior with comments

### Platform Compatibility
- Write portable Node.js code
- These fixtures work via embedded shell (like git hooks)
- Avoid platform-specific logic

### Naming Conventions
- Use UPPERCASE for context type prefixes (e.g., `WORKSPACE_RULES:`, `FILE_OPERATIONS:`)
- Be descriptive about what the fixture tests
- Follow existing naming patterns in other fixtures

## Examples from Existing Fixtures

See the existing fixtures for real-world examples:
- `../hooks/pretooluse/success/` - Simple success case
- `../hooks/pretooluse/blocking/` - How to block execution
- `../hooks/pretooluse/context-injection/` - How to inject context
- `../hooks/pretooluse/error/` - How to return errors



---

# FILE: src/core/prompts/system-prompt/CONTRIBUTING.md

# Contributing to System Prompts and Model Configuration

This guide explains how to add new model families and configure custom system prompts for contributors from model labs / providers.

> **⚡ Key Principle: Fallback to GENERIC**
>
> The system uses automatic fallbacks to minimize configuration:
> - **No matching variant?** → Falls back to `GENERIC` variant
> - **No tool variant for model family?** → Falls back to `GENERIC` tool variant
> - **No component override?** → Uses shared component from `components/`
>
> **This means:** Only customize what's necessary. Start minimal, add specifics only when needed.

## Table of Contents

1. [Glossary](#glossary)
2. [Architecture Overview](#architecture-overview)
3. [Creating a Model Family](#creating-a-model-family)
4. [Configuring System Prompts](#configuring-system-prompts)
5. [Configuring Tool Calling](#configuring-tool-calling)
6. [Configuring API Request/Response Shapes](#configuring-api-requestresponse-shapes)
7. [Adding Model-Specific Tools](#adding-model-specific-tools)
8. [Testing](#testing)

---

## Glossary

### Model Family
A category grouping models with similar capabilities and behavior patterns. Each family has an optimized system prompt variant.

**Examples:** `NEXT_GEN` (Claude 4+, GPT-5, Gemini 2.5), `GENERIC` (fallback), `XS` (small models)

**Location:** [`src/shared/prompts.ts`](../../shared/prompts.ts) `ModelFamily` enum

### System Prompt Variant
A complete configuration for a model family, including:
- Component selection and ordering
- Tool configuration
- Template with placeholders
- Matcher function determining when to use it

**Location:** [`variants/*/config.ts`](./variants/)

### Matcher Function
Function that determines if a variant applies to a given model and context. Returns `true` if the variant should be used.

```typescript
.matcher((context) => {
    const modelId = context.providerInfo.model.id.toLowerCase()
    return modelId.includes("gpt-5") && context.enableNativeToolCalls
})
```

### Native Tool Calling
Modern approach where tools are sent to the model via the provider's native API (e.g., OpenAI function calling, Anthropic tool use). More reliable than XML-based calling.

**Characteristics:**
- Tools passed separately via API (not embedded in system prompt)
- Structured tool calls in API response (JSON)
- Requires `enableNativeToolCalls` setting enabled
- Indicated by `use_native_tools: 1` label in variant config

**Supported providers:** OpenAI, Anthropic, Gemini, OpenRouter, Minimax

### XML (Text-Based) Tool Calling
Traditional approach where tools are described in the system prompt and the model outputs tool calls as XML tags in text.

**Characteristics:**
- Tools embedded in system prompt as XML format instructions
- Model generates XML: `<tool_name><param>value</param></tool_name>`
- Client parses XML from text response
- Works with any model that can follow instructions

### API Format
Defines the request/response structure for a model provider's API. Different formats have different message structures and capabilities.

**Values:** `ANTHROPIC_CHAT`, `GEMINI_CHAT`, `OPENAI_CHAT`, `R1_CHAT`, `OPENAI_RESPONSES`

**Location:** [`proto/cline/models.proto`](../../../proto/cline/models.proto)

**Usage:** `model.info.apiFormat` determines how requests/responses are structured

### Component
A reusable function that generates a section of the system prompt (e.g., `AGENT_ROLE`, `RULES`, `CAPABILITIES`). Components can be shared or overridden per-variant.

**Location:** [`components/`](./components/)

### Tool Specification
Defines how a tool appears in the system prompt for a specific model family. Multiple variants can exist for the same tool.

**Example:** [`tools/write_to_file.ts`](./tools/write_to_file.ts) defines `GENERIC`, `NATIVE_NEXT_GEN`, and `NATIVE_GPT_5` variants

---

## Architecture Overview

### Fallback Behavior

The system uses **automatic fallbacks** to ensure robustness:

1. **Variant Selection Fallback:**
   - If no variant matcher returns `true`, falls back to `GENERIC` variant
   - `GENERIC` is the universal fallback that works with all models

2. **Tool Variant Fallback:**
   - If a tool doesn't define a variant for the current model family, automatically falls back to `GENERIC` tool variant
   - Handled by `ClineToolSet.getToolByNameWithFallback()`
   - **You only need to export model-specific tool variants when behavior differs from `GENERIC`**

3. **Component Fallback:**
   - If a variant doesn't override a component, uses the shared component from [`components/`](./components/)
   - Only override when model needs custom instructions
   - Example: Most variants use shared `AGENT_ROLE`, but override `RULES` for model-specific behavior

**This means:** When adding a new model family, you can start with minimal configuration and only customize what's necessary.

### System Prompt Generation Flow

```
User Request
    ↓
Model Detection (model-utils.ts)
    ↓
Variant Selection (matcher functions) → Falls back to GENERIC if no match
    ↓
Component Building (components/) → Uses shared components unless overridden
    ↓
Tool Configuration (tools/) → Falls back to GENERIC tool variant if not defined
    ↓
Template Resolution ({{PLACEHOLDER}})
    ↓
Final System Prompt
```

### Key Files

| Purpose | File |
|---------|------|
| Model detection | [`src/utils/model-utils.ts`](../../../utils/model-utils.ts) |
| Model family enum | [`src/shared/prompts.ts`](../../shared/prompts.ts) |
| Tool enum | [`src/shared/tools.ts`](../../shared/tools.ts) |
| Variant registry | [`variants/index.ts`](./variants/index.ts) |
| Tool registry | [`tools/init.ts`](./tools/init.ts) |

---

## Creating a Model Family

### Step 1: Add Model Detection Logic

Add helper functions to [`src/utils/model-utils.ts`](../../../utils/model-utils.ts):

```typescript
// Add detector function
export function isMyNewModelFamily(id: string): boolean {
    const modelId = normalize(id)
    return modelId.includes("my-model") || modelId.includes("my-model-v2")
}

// If it's a next-gen model, add to isNextGenModelFamily()
export function isNextGenModelFamily(id: string): boolean {
    return (
        isClaude4PlusModelFamily(modelId) ||
        // ... existing checks
        isMyNewModelFamily(modelId)  // Add here
    )
}

// If it's a next-gen provider, add to isNextGenModelProvider()
export function isNextGenModelProvider(providerInfo: ApiProviderInfo): boolean {
    const providerId = normalize(providerInfo.providerId)
    return [
        "anthropic", "openai", "gemini", "openrouter",
        "my-new-provider",  // Add here
    ].some((id) => providerId === id)
}
```

### Step 2: Add Model Family Enum

Add to `ModelFamily` enum in [`src/shared/prompts.ts`](../../shared/prompts.ts):

```typescript
export enum ModelFamily {
    CLAUDE = "claude",
    GPT_5 = "gpt-5",
    NEXT_GEN = "next-gen",
    MY_NEW_MODEL = "my-new-model",  // Add here
}
```

### Step 3: Create Variant Configuration

Create [`variants/my-new-model/config.ts`](./variants/):

```typescript
import { isMyNewModelFamily, isNextGenModelProvider } from "@utils/model-utils"
import { ModelFamily } from "@/shared/prompts"
import { ClineDefaultTool } from "@/shared/tools"
import { SystemPromptSection } from "../../templates/placeholders"
import { createVariant } from "../variant-builder"
import { validateVariant } from "../variant-validator"

export const config = createVariant(ModelFamily.MY_NEW_MODEL)
    .description("Optimized for My New Model")
    .version(1)
    .tags("production", "my-model")
    .labels({
        stable: 1,
        production: 1,
        // Add use_native_tools: 1 if native tool calling supported
    })
    .matcher((context) => {
        const modelId = context.providerInfo.model.id
        return isMyNewModelFamily(modelId)
    })
    // Template: Structure with placeholders that will be replaced
    .template(`{{AGENT_ROLE_SECTION}}

====

{{TOOL_USE_SECTION}}

====

{{RULES_SECTION}}

====

{{OBJECTIVE_SECTION}}`)
    // Components: Which sections to include (must match template placeholders)
    .components(
        SystemPromptSection.AGENT_ROLE,
        SystemPromptSection.TOOL_USE,
        SystemPromptSection.RULES,
        SystemPromptSection.OBJECTIVE,
    )
    .tools(
        ClineDefaultTool.BASH,
        ClineDefaultTool.FILE_READ,
        ClineDefaultTool.ASK,
    )
    .placeholders({
        MODEL_FAMILY: ModelFamily.MY_NEW_MODEL,
    })
    .config({})
    .build()

// Validation
const validationResult = validateVariant({ ...config, id: ModelFamily.MY_NEW_MODEL }, { strict: true })
if (!validationResult.isValid) {
    throw new Error(`Invalid config: ${validationResult.errors.join(", ")}`)
}

export type MyNewModelVariantConfig = typeof config
```

**How Templates and Placeholders Work:**

The `.template()` defines the **structure** of your system prompt using placeholders like `{{AGENT_ROLE_SECTION}}`, `{{RULES_SECTION}}`, etc.

**Placeholder Resolution Process:**

1. **Component Building:** Each component in `.components()` generates content by calling its function from [`components/`](./components/)
   - `SystemPromptSection.AGENT_ROLE` → generates `{{AGENT_ROLE_SECTION}}` content
   - `SystemPromptSection.RULES` → generates `{{RULES_SECTION}}` content
   - etc.

2. **Default vs Override:**
   - **By default:** Uses shared component from [`components/`](./components/) (e.g., [`components/rules.ts`](./components/rules.ts))
   - **With override:** Uses your custom template instead

3. **Template Resolution:** The `TemplateEngine` replaces all `{{PLACEHOLDERS}}` with generated content

**Example with Override:**

```typescript
import { CUSTOM_AGENT_ROLE } from "./template"

export const config = createVariant(ModelFamily.MY_NEW_MODEL)
    .template(`{{AGENT_ROLE_SECTION}}

{{RULES_SECTION}}`)
    .components(
        SystemPromptSection.AGENT_ROLE,  // Will use override below
        SystemPromptSection.RULES,        // Will use shared components/rules.ts
    )
    // Override AGENT_ROLE to use custom template
    .overrideComponent(SystemPromptSection.AGENT_ROLE, {
        template: CUSTOM_AGENT_ROLE,  // Your custom content
    })
    .build()
```

**Result:**
- `{{AGENT_ROLE_SECTION}}` → Replaced with `CUSTOM_AGENT_ROLE` content (overridden)
- `{{RULES_SECTION}}` → Replaced with shared `components/rules.ts` content (default)

See [`variants/native-gpt-5-1/config.ts`](./variants/native-gpt-5-1/config.ts) for a real example with multiple overrides.

### Step 4: Register Variant

Add to [`variants/index.ts`](./variants/index.ts):

```typescript
export { config as myNewModelConfig } from "./my-new-model/config"
import { config as myNewModelConfig } from "./my-new-model/config"

export const VARIANT_CONFIGS = {
    // ... existing variants
    [ModelFamily.MY_NEW_MODEL]: myNewModelConfig,
} as const
```

---

## Configuring System Prompts

### Basic Configuration

See [Step 3 above](#step-3-create-variant-configuration) for basic variant structure.

### Component Overrides

**Default behavior:** If you don't override a component, the variant automatically uses the shared component from [`components/`](./components/).

**Only override when:**
- Model needs custom instructions for a specific section
- Default component doesn't work well for the model
- Model has unique capabilities requiring different guidance

**To override a component:**

**Create [`variants/my-new-model/template.ts`](./variants/):**

```typescript
export const CUSTOM_RULES_TEMPLATE = `
# Rules for My New Model

1. Use specific syntax optimized for this model
2. Avoid patterns this model struggles with
3. Leverage unique capabilities
`
```

**Update `config.ts`:**

```typescript
import { CUSTOM_RULES_TEMPLATE } from "./template"

export const config = createVariant(ModelFamily.MY_NEW_MODEL)
    // ... other configuration
    .overrideComponent(SystemPromptSection.RULES, {
        template: CUSTOM_RULES_TEMPLATE,
    })
    .build()
```

### Available Components

You can include/exclude these in `.components()`:

- `AGENT_ROLE` - Agent identity and role
- `TOOL_USE` - Tool usage instructions
- `TASK_PROGRESS` - Task progress tracking
- `MCP` - MCP server information
- `EDITING_FILES` - File editing guidelines
- `ACT_VS_PLAN` - Action vs planning mode
- `CAPABILITIES` - Agent capabilities
- `FEEDBACK` - Feedback and improvement
- `RULES` - Behavioral rules
- `SYSTEM_INFO` - System environment info
- `OBJECTIVE` - Current task objective
- `USER_INSTRUCTIONS` - User custom instructions
- `TODO` - Todo management

See [`components/`](./components/) for implementations.

### Available Tools

Common tools to include in `.tools()`:

- `BASH` - Execute shell commands
- `FILE_READ`, `FILE_NEW`, `FILE_EDIT` - File operations
- `SEARCH`, `LIST_FILES`, `LIST_CODE_DEF` - Code search
- `BROWSER`, `WEB_FETCH` - Web operations
- `MCP_USE`, `MCP_ACCESS` - MCP integration
- `ASK`, `ATTEMPT` - Task management
- `PLAN_MODE`, `ACT_MODE` - Mode switching
- `TODO` - Todo management

See [`src/shared/tools.ts`](../../shared/tools.ts) for full list.

---

## Configuring Tool Calling

### Native Tool Calling

**When to use:** Provider supports native function calling and `enableNativeToolCalls` is enabled.

**Example:** [`variants/native-next-gen/config.ts`](./variants/native-next-gen/config.ts)

```typescript
export const config = createVariant(ModelFamily.NATIVE_NEXT_GEN)
    .labels({
        use_native_tools: 1,  // Enable native tool calling
    })
    .matcher((context) => {
        if (!context.enableNativeToolCalls) {
            return false
        }
        if (!isNextGenModelProvider(context.providerInfo)) {
            return false
        }
        return isNextGenModelFamily(context.providerInfo.model.id)
    })
    // ... rest of configuration
```

**Key points:**
- Set `use_native_tools: 1` label
- Check `context.enableNativeToolCalls` in matcher
- Check provider supports native tools via `isNextGenModelProvider()`
- Tools sent separately via API, not embedded in prompt

### XML Tool Calling

**When to use:** Provider doesn't support native tools OR `enableNativeToolCalls` is disabled.

**Example:** [`variants/next-gen/config.ts`](./variants/next-gen/config.ts)

```typescript
export const config = createVariant(ModelFamily.NEXT_GEN)
    .matcher((context) => {
        const providerInfo = context.providerInfo
        // Use this variant if next-gen BUT native tools disabled
        if (isNextGenModelFamily(providerInfo.model.id) && !context.enableNativeToolCalls) {
            return true
        }
        // OR if provider doesn't support native tools
        return !isNextGenModelProvider(providerInfo) && isNextGenModelFamily(providerInfo.model.id)
    })
    .tools(
        // Include MCP_USE for XML-based tool calling
        ClineDefaultTool.MCP_USE,  // Instead of MCP_ACCESS
        // ... other tools
    )
```

**Key points:**
- Don't set `use_native_tools` label
- Check native tools are disabled OR provider doesn't support them
- Include detailed tool descriptions in system prompt
- Use `MCP_USE` instead of `MCP_ACCESS`

### Decision Flow

```
Is enableNativeToolCalls enabled?
  NO → Use XML variant
  YES → Does provider support native tools?
      NO → Use XML variant
      YES → Does model support native tools?
          NO → Use XML variant
          YES → Use native variant
```

---

## Configuring API Request/Response Shapes

### Setting API Format

API formats are defined in [`proto/cline/models.proto`](../../../proto/cline/models.proto):

```protobuf
enum ApiFormat {
    ANTHROPIC_CHAT = 0;      // Messages API
    GEMINI_CHAT = 1;         // Gemini generateContent
    OPENAI_CHAT = 2;         // Chat Completions API
    R1_CHAT = 3;             // DeepSeek R1 format
    OPENAI_RESPONSES = 4;    // Responses API (GPT-5.1+)
}
```

### Using API Format in Provider Code

**Example from [`src/core/api/providers/openai-native.ts`](../../api/providers/openai-native.ts):**

```typescript
async *createMessage(systemPrompt: string, messages: ClineStorageMessage[], tools?: ChatCompletionTool[]): ApiStream {
    // Route based on API format
    if (tools?.length && this.getModel()?.info?.apiFormat === ApiFormat.OPENAI_RESPONSES) {
        yield* this.createResponseStream(systemPrompt, messages, tools)
    } else {
        yield* this.createCompletionStream(systemPrompt, messages, tools)
    }
}
```

### Format Comparison

| Format | Provider | Tool Support | System Prompt | Special Features |
|--------|----------|--------------|---------------|------------------|
| `ANTHROPIC_CHAT` | Anthropic | Native (input_schema) | Content blocks | Caching, thinking |
| `GEMINI_CHAT` | Gemini/Vertex | Native (function_declarations) | String | Thinking levels |
| `OPENAI_CHAT` | OpenAI, OpenRouter | Native (function) | String | Reasoning effort |
| `R1_CHAT` | DeepSeek R1 | Limited | String | Reasoning-focused |
| `OPENAI_RESPONSES` | GPT-5.1+ | Native (strict mode) | String | Structured outputs |

### Adding a New API Format

1. **Add to proto:** [`proto/cline/models.proto`](../../../proto/cline/models.proto)
2. **Regenerate:** `npm run protos`
3. **Import:** `import { ApiFormat } from "@/shared/proto/cline/models"`
4. **Handle in provider:** Add format-specific logic in your provider handler

See existing providers in [`src/core/api/providers/`](../../api/providers/) for examples.

---

## Adding Model-Specific Tools

### When to Create Model-Specific Tool Variants

**Default behavior:** Tools automatically fall back to `GENERIC` variant via `ClineToolSet.getToolByNameWithFallback()`.

**Only create a model-specific tool variant when:**
- Tool needs different parameters or descriptions for the model
- Tool requires model-specific instructions
- Tool behavior differs significantly across models

**Examples requiring specific variants:**
- Native tool calling models need absolute paths vs relative paths
- Models with different context handling need adjusted descriptions
- Models with specific quirks need tailored instructions

**Important:** If you only export `[GENERIC]` from your tool file, all model families will use it automatically. You don't need to create variants for every model family.

### Creating a Tool Variant

**Example from [`tools/write_to_file.ts`](./tools/write_to_file.ts):**

```typescript
import { ModelFamily } from "@/shared/prompts"
import { ClineDefaultTool } from "@/shared/tools"
import type { ClineToolSpec } from "../spec"

const id = ClineDefaultTool.FILE_NEW

const GENERIC: ClineToolSpec = {
    variant: ModelFamily.GENERIC,
    id,
    name: "write_to_file",
    description: "Request to write content to a file...",
    parameters: [
        {
            name: "path",
            required: true,
            instruction: "The path of the file to write to (relative to {{CWD}})",
            usage: "File path here",
        },
        {
            name: "content",
            required: true,
            instruction: "The content to write. ALWAYS provide COMPLETE content.",
            usage: "Your file content here",
        },
    ],
}

const NATIVE_NEXT_GEN: ClineToolSpec = {
    variant: ModelFamily.NATIVE_NEXT_GEN,
    id,
    name: "write_to_file",
    description: "[IMPORTANT: Always output absolutePath first] Request to write...",
    parameters: [
        {
            name: "absolutePath",
            required: true,
            instruction: "The absolute path to the file.",
        },
        {
            name: "content",
            required: true,
            instruction: "After providing path, use this for content.",
        },
    ],
}

export const write_to_file_variants = [GENERIC, NATIVE_NEXT_GEN]
```

### Key Differences in Tool Variants

**GENERIC (XML-based):**
- Relative paths (with `{{CWD}}` placeholder)
- Verbose instructions
- XML usage examples

**NATIVE_NEXT_GEN (Native calling):**
- Absolute paths (clearer for structured API)
- Concise instructions
- Parameter ordering hints (e.g., "Always output X first")

### Registering Tool Variants

**1. Export from [`tools/index.ts`](./tools/index.ts):**
```typescript
export * from "./write_to_file"
```

**2. Register in [`tools/init.ts`](./tools/init.ts):**
```typescript
import { write_to_file_variants } from "./write_to_file"

export function registerClineToolSets(): void {
    const allToolVariants = [
        ...write_to_file_variants,
        // ... other tool variants
    ]

    allToolVariants.forEach((v) => ClineToolSet.register(v))
}
```

### Adding Tool to Variant Configs

**Update all relevant variant configs** in [`variants/*/config.ts`](./variants/) to include the tool:

```typescript
.tools(
    ClineDefaultTool.BASH,
    ClineDefaultTool.FILE_NEW,  // Add your tool here
    // ... other tools
)
```

**Important:** If you add a tool to a variant's config, ensure either:
1. The tool exports a spec for that `ModelFamily`, OR
2. The tool exports a `GENERIC` spec (automatic fallback)

**Note:** When a variant includes a tool in `.tools()` but the tool doesn't have a specific variant for that model family, the system automatically uses the `GENERIC` variant. This is handled by `ClineToolSet.getToolByNameWithFallback()`, so you don't need to manually define variants for every model family—only when behavior needs to differ.

---

## Testing

### Running Tests

```bash
# Run tests (fails if snapshots don't match)
npm run test:unit

# Update snapshots after intentional changes
npm run test:unit -- --update-snapshots
# OR
UPDATE_SNAPSHOTS=true npm run test:unit
```

### Snapshot Tests

**Location:** [`__tests__/__snapshots__/`](./__tests__/__snapshots__/)

**What's tested:**
- System prompts generate correctly for each model family
- Prompts remain consistent across contexts (browser, MCP, focus chain)
- Component ordering and overrides work correctly
- Tool specifications properly included

**Test file:** [`__tests__/integration.test.ts`](./__tests__/integration.test.ts)

### Testing in Debug Mode

**For live testing with real models**, run Cline in debug mode to verify your variant works correctly:

1. **Enable Debug Mode:**
   - See the main [CONTRIBUTING.md](../../../../CONTRIBUTING.md) for instructions on running Cline in debug mode
   - Debug mode enables additional features for testing and verification

2. **Run a Task with Your Model:**
   - Configure your model in Cline settings
   - Start a conversation or task with the model
   - The system will automatically select your variant based on the matcher function

3. **Export Task JSON (Debug Mode Only):**
   - After the task completes, click the **task header** in the chat
   - Look for the **export JSON** option (only available in debug mode)
   - Export the task JSON file

4. **Verify Your Configuration:**
   - Open the exported JSON file
   - Search for `"systemPrompt"` to see the full generated system prompt
   - Verify:
     - Correct variant was selected
     - All placeholders resolved correctly
     - Component overrides applied
     - Tools included as expected
     - Template structure matches your config

**Example verification:**
```json
{
  "systemPrompt": "You are Cline...\n\n====\n\n# Agent Role\n...",
  "modelFamily": "my-new-model",
  "tools": ["bash", "file_read", "ask"],
  // ... rest of task data
}
```

This exported JSON is invaluable for debugging and verifying that your variant configuration is working as intended in real-world usage.

### Manual Testing Checklist

1. **Verify variant selection:**
   - Confirm correct variant selected for test model IDs
   - Check matcher logic returns true/false as expected
   - Use exported JSON to verify `modelFamily` matches expected value

2. **Test tool conversion:**
   - Verify tools converted to correct format (native vs XML)
   - Check provider-specific tool format matches expectations
   - Review tools in exported JSON to confirm correct conversion

3. **Validate prompt structure:**
   - Confirm all `{{PLACEHOLDERS}}` resolved in exported JSON
   - Check section ordering matches config
   - Verify overrides applied correctly by inspecting `systemPrompt` field

4. **Test across contexts:**
   - With/without browser support
   - With/without MCP servers
   - With/without native tool calling enabled
   - Export JSON for each context to compare differences

---

## Additional Resources

- **System Prompt Architecture:** [README.md](./README.md)
- **Tool Development:** [tools/README.md](./tools/README.md)
- **Testing Guide:** [__tests__/README.md](./__tests__/README.md)
- **Model Utilities:** [`src/utils/model-utils.ts`](../../../utils/model-utils.ts)
- **Proto Definitions:** [`proto/cline/models.proto`](../../../proto/cline/models.proto)
- **CLAUDE.md:** [`CLAUDE.md`](../../../../CLAUDE.md) (tribal knowledge)

---

## Quick Reference

### Common File Locations

```
src/
├── shared/
│   ├── prompts.ts              # ModelFamily enum
│   └── tools.ts                # ClineDefaultTool enum
├── utils/
│   └── model-utils.ts          # Model detection functions
├── core/
│   ├── api/providers/          # API provider handlers
│   └── prompts/system-prompt/
│       ├── components/         # Shared prompt components
│       ├── tools/              # Tool specifications
│       ├── variants/           # Model family configs
│       │   ├── generic/
│       │   ├── next-gen/
│       │   ├── native-next-gen/
│       │   └── [family]/
│       │       ├── config.ts   # Variant configuration
│       │       └── template.ts # Custom templates
│       └── registry/           # Core logic
│           ├── PromptRegistry.ts
│           ├── PromptBuilder.ts
│           └── ClineToolSet.ts
proto/
└── cline/
    └── models.proto            # ApiFormat enum
```

### Common Patterns

**Model detection:**
```typescript
export function isMyModelFamily(id: string): boolean {
    return normalize(id).includes("my-model")
}
```

**Variant matcher:**
```typescript
.matcher((context) => isMyModelFamily(context.providerInfo.model.id))
```

**Component override:**
```typescript
.overrideComponent(SystemPromptSection.RULES, { template: CUSTOM_TEMPLATE })
```

**Native tools check:**
```typescript
.matcher((context) =>
    context.enableNativeToolCalls &&
    isNextGenModelProvider(context.providerInfo)
)
```

---

For questions or issues, consult existing variant configurations in [`variants/`](./variants/) or review the model detection logic in [`model-utils.ts`](../../../utils/model-utils.ts).



---

# FILE: src/core/prompts/system-prompt/README.md

# System Prompt Architecture

## Overview

The system prompt architecture provides a modular, composable system for building AI assistant prompts. It supports multiple model variants, dynamic component composition, flexible tool configuration, and template-based prompt generation.

## Developer

To generate snapshots for each variants added to the unit test in [src/core/prompts/system-prompt/__tests__/integration.test.ts](./__tests__/integration.test.ts):

```sh
npm run test:unit
```

## Directory Structure

```
src/core/prompts/system-prompt/
├── registry/
│   ├── ClineToolSet.ts            # Tool set management & registry
│   ├── PromptRegistry.ts          # Singleton registry for loading/managing prompts
│   ├── PromptBuilder.ts           # Builds final prompts with template resolution
│   └── utils.ts                   # Model family detection utilities
├── components/                    # Reusable prompt components
│   ├── agent_role.ts             # Agent role and identity section
│   ├── system_info.ts            # System information section
│   ├── mcp.ts                    # MCP servers section  
│   ├── todo.ts                   # Todo management section
│   ├── user_instructions.ts      # User custom instructions
│   ├── tool_use.ts               # Tool usage instructions
│   ├── editing_files.ts          # File editing guidelines
│   ├── capabilities.ts           # Agent capabilities section
│   ├── rules.ts                  # Behavioral rules section
│   ├── objective.ts              # Task objective section
│   ├── act_vs_plan.ts            # Action vs planning mode
│   ├── feedback.ts               # Feedback and improvement section
│   └── index.ts                  # Component registry
├── templates/                    # Template engine and placeholders
│   ├── TemplateEngine.ts         # {{placeholder}} resolution engine
│   └── placeholders.ts           # Standard placeholder definitions
├── tools/                        # Individual tool definitions
│   ├── spec.ts                   # Tool specification interface
│   ├── register.ts               # Tool registration system
│   ├── index.ts                  # Tool exports
│   └── [tool-name].ts            # Individual tool implementations
├── variants/                     # Model-specific prompt variants
│   ├── generic/
│   │   ├── config.ts             # Generic fallback configuration
│   │   └── template.ts           # Base prompt template
│   ├── next-gen/
│   │   ├── config.ts             # Next-gen model configuration
│   │   └── template.ts           # Advanced model template
│   ├── xs/
│   │   ├── config.ts             # Small model configuration
│   │   └── template.ts           # Optimized template
│   └── index.ts                  # Variant registry exports
├── types.ts                      # Core type definitions
└── README.md                     # This documentation
```

## Core Components

### 1. PromptRegistry (Singleton)

The `PromptRegistry` is the central manager for all prompt variants and components. It provides a singleton interface for loading and accessing prompts.

```typescript
class PromptRegistry {
  private static instance: PromptRegistry;
  private variants: Map<string, PromptVariant> = new Map();
  private components: ComponentRegistry = {};
  private loaded: boolean = false;

  static getInstance(): PromptRegistry {
    if (!this.instance) {
      this.instance = new PromptRegistry();
    }
    return this.instance;
  }

  // Load all prompts and components on initialization
  async load(): Promise<void> {
    if (this.loaded) return;
    
    await Promise.all([
      this.loadVariants(),    // Load from variants/ directory
      this.loadComponents()   // Load from components/ directory
    ]);
    
    this.loaded = true;
  }

	/**
	 * Get prompt by model ID with fallback to generic
	 */
	async get(context: SystemPromptContext): Promise<string> {
		await this.load()

		// Try model family fallback (e.g., "claude-4" -> "claude")
		const modelFamily = this.getModelFamily(context.providerInfo)
		const variant = this.variants.get(modelFamily ?? ModelFamily.GENERIC)

		if (!variant) {
			throw new Error(
				`No prompt variant found for model '${context.providerInfo.model.id}' and no generic fallback available`,
			)
		}

		const builder = new PromptBuilder(variant, context, this.components)
		return await builder.build()
	}

  // Get specific version of a prompt
  async getVersion(modelId: string, version: number, context: SystemPromptContext, isNextGenModelFamily?: boolean): Promise<string> {
    // Supports next-gen model family prioritization
  }

  // Get prompt by tag/label
  async getByTag(modelId: string, tag?: string, label?: string, context?: SystemPromptContext, isNextGenModelFamily?: boolean): Promise<string> {
    // Supports tag and label-based retrieval with next-gen prioritization
  }
}
```

### 2. PromptVariant Structure

The `PromptVariant` interface defines the configuration for each model-specific prompt variant:

```typescript
interface PromptVariant {
  id: string;                                    // Model family ID (e.g., "next-gen", "generic")
  version: number;                               // Version number
  family: ModelFamily;                           // Model family enum
  tags: string[];                                // ["production", "beta", "experimental"]
  labels: { [key: string]: number };             // {"staging": 2, "prod": 1}
  description: string;                           // Brief description of the variant

  // Prompt configuration
  config: PromptConfig;                          // Model-specific config
  baseTemplate: string;                          // Main prompt template with placeholders
  componentOrder: SystemPromptSection[];        // Ordered list of components to include
  componentOverrides: { [K in SystemPromptSection]?: ConfigOverride }; // Component customizations
  placeholders: { [key: string]: string };      // Default placeholder values

  // Tool configuration
  tools?: ClineDefaultTool[];                    // Ordered list of tools to include
  toolOverrides?: { [K in ClineDefaultTool]?: ConfigOverride }; // Tool-specific customizations
}

interface PromptConfig {
  modelName?: string;
  temperature?: number;
  maxTokens?: number;
  tools?: ClineToolSpec[];
  [key: string]: any;                            // Additional arbitrary config
}

interface ConfigOverride {
  template?: string;                             // Custom template for the component/tool
  enabled?: boolean;                             // Whether the component/tool is enabled
  order?: number;                                // Override the order
}
```

### 3. PromptBuilder

The `PromptBuilder` orchestrates the construction of the final prompt by combining templates, components, and placeholders:

```typescript
class PromptBuilder {
  private templateEngine: TemplateEngine;

  constructor(
    private variant: PromptVariant,
    private context: SystemPromptContext,
    private components: ComponentRegistry
  ) {
    this.templateEngine = new TemplateEngine();
  }

  async build(): Promise<string> {
    // 1. Build all components in specified order
    const componentSections = await this.buildComponents();
    
    // 2. Prepare all placeholder values
    const placeholderValues = this.preparePlaceholders(componentSections);
    
    // 3. Resolve template placeholders
    const prompt = this.templateEngine.resolve(this.variant.baseTemplate, placeholderValues);
    
    // 4. Apply final post-processing
    return this.postProcess(prompt);
  }

  private async buildComponents(): Promise<Record<string, string>> {
    const sections: Record<string, string> = {};
    
    // Process components sequentially to maintain order
    for (const componentId of this.variant.componentOrder) {
      const componentFn = this.components[componentId];
      if (!componentFn) {
        console.warn(`Warning: Component '${componentId}' not found`);
        continue;
      }

      try {
        const result = await componentFn(this.variant, this.context);
        if (result?.trim()) {
          sections[componentId] = result;
        }
      } catch (error) {
        console.warn(`Warning: Failed to build component '${componentId}':`, error);
      }
    }

    return sections;
  }

  private preparePlaceholders(componentSections: Record<string, string>): Record<string, unknown> {
    const placeholders: Record<string, unknown> = {};

    // Add variant placeholders
    Object.assign(placeholders, this.variant.placeholders);

    // Add standard system placeholders
    placeholders[STANDARD_PLACEHOLDERS.CWD] = this.context.cwd || process.cwd();
    placeholders[STANDARD_PLACEHOLDERS.SUPPORTS_BROWSER] = this.context.supportsBrowserUse || false;
    placeholders[STANDARD_PLACEHOLDERS.MODEL_FAMILY] = this.variant.family;
    placeholders[STANDARD_PLACEHOLDERS.CURRENT_DATE] = new Date().toISOString().split("T")[0];

    // Add all component sections
    Object.assign(placeholders, componentSections);

    // Add runtime placeholders with highest priority
    const runtimePlaceholders = (this.context as any).runtimePlaceholders;
    if (runtimePlaceholders) {
      Object.assign(placeholders, runtimePlaceholders);
    }

    return placeholders;
  }

  private postProcess(prompt: string): string {
    if (!prompt) return "";

    // Combine multiple regex operations for better performance
    return prompt
      .replace(/\n\s*\n\s*\n/g, "\n\n")     // Remove multiple consecutive empty lines
      .trim()                                // Remove leading/trailing whitespace
      .replace(/====+\s*$/, "")             // Remove trailing ==== after trim
      .replace(/\n====+\s*\n+\s*====+\n/g, "\n====\n") // Remove empty sections between separators
      .replace(/====\n([^\n])/g, "====\n\n$1")          // Ensure proper section separation
      .replace(/([^\n])\n====/g, "$1\n\n====");
  }
}
```

### 4. Template System

The template system uses `{{PLACEHOLDER}}` syntax for dynamic content injection:

```typescript
class TemplateEngine {
  resolve(template: string, placeholders: Record<string, unknown>): string {
    return template.replace(/\{\{([^}]+)\}\}/g, (match, key) => {
      const trimmedKey = key.trim();
      
      // Support nested object access using dot notation
      const value = this.getNestedValue(placeholders, trimmedKey);
      
      if (value !== undefined && value !== null) {
        return typeof value === "string" ? value : JSON.stringify(value);
      }
      
      // Keep placeholder if not found (allows for partial resolution)
      return match;
    });
  }

  extractPlaceholders(template: string): string[] {
    const placeholders: string[] = [];
    const regex = /\{\{([^}]+)\}\}/g;
    let match: RegExpExecArray | null = null;

    match = regex.exec(template);
    while (match !== null) {
      const placeholder = match[1].trim();
      if (!placeholders.includes(placeholder)) {
        placeholders.push(placeholder);
      }
      match = regex.exec(template);
    }

    return placeholders;
  }
}
```

**Base Template Example:**
```markdown
You are Cline, a highly skilled software engineer...

====

{{TOOL_USE_SECTION}}

====

{{MCP_SECTION}}

====

{{USER_INSTRUCTIONS_SECTION}}

====

{{SYSTEM_INFO_SECTION}}

====

{{TODO_SECTION}}
```

### 5. Component System

Components are reusable functions that generate specific sections of the prompt:

```typescript
type ComponentFunction = (
  variant: PromptVariant, 
  context: SystemPromptContext
) => Promise<string | undefined>;

// Example component
export async function getSystemInfo(
  variant: PromptVariant,
  context: SystemPromptContext,
): Promise<string> {
  const info = await getSystemEnv();

  // Support component overrides
  const template = variant.componentOverrides?.SYSTEM_INFO_SECTION?.template || `
Operating System: {{os}}
Default Shell: {{shell}}
Home Directory: {{homeDir}}
Current Working Directory: {{workingDir}}
  `;

  return new TemplateEngine().resolve(template, {
    os: info.os,
    shell: info.shell,
    homeDir: info.homeDir,
    workingDir: info.workingDir
  });
}
```

### 6. Tool System

Tools are managed through the `ClineToolSet` and can be configured per variant:

```typescript
class ClineToolSet {
  private static variants: Map<ModelFamily, Set<ClineToolSet>> = new Map();

  static register(config: ClineToolSpec): ClineToolSet {
    return new ClineToolSet(config.id, config);
  }

  static getTools(variant: ModelFamily): ClineToolSet[] {
    const toolsSet = ClineToolSet.variants.get(variant) || new Set();
    const defaultSet = ClineToolSet.variants.get(ModelFamily.GENERIC) || new Set();
    return toolsSet ? Array.from(toolsSet) : Array.from(defaultSet);
  }
}

// Tool generation in PromptBuilder
public static async getToolsPrompts(variant: PromptVariant, context: SystemPromptContext) {
  const tools = ClineToolSet.getTools(variant.family);
  
  // Filter and sort tools based on variant configuration
  const enabledTools = tools.filter((tool) => 
    !tool.config.contextRequirements || tool.config.contextRequirements(context)
  );

  let sortedEnabledTools = enabledTools;
  if (variant?.tools?.length) {
    const toolOrderMap = new Map(variant.tools.map((id, index) => [id, index]));
    sortedEnabledTools = enabledTools.sort((a, b) => {
      const orderA = toolOrderMap.get(a.config.id);
      const orderB = toolOrderMap.get(b.config.id);
      
      if (orderA !== undefined && orderB !== undefined) {
        return orderA - orderB;
      }
      if (orderA !== undefined) return -1;
      if (orderB !== undefined) return 1;
      return a.config.id.localeCompare(b.config.id);
    });
  }

  const ids = sortedEnabledTools.map((tool) => tool.config.id);
  return Promise.all(sortedEnabledTools.map((tool) => PromptBuilder.tool(tool.config, ids)));
}
```

## Configuration Examples

### Basic Variant Configuration (Using Builder Pattern)

```typescript
// variants/generic/config.ts
import { ModelFamily } from "@/shared/prompts";
import { ClineDefaultTool } from "@/shared/tools";
import { SystemPromptSection } from "../../templates/placeholders";
import { validateVariant } from "../../validation/VariantValidator";
import { createVariant } from "../builder";
import { baseTemplate } from "./template";

// Type-safe variant configuration using the builder pattern
export const config = createVariant(ModelFamily.GENERIC)
  .description("The fallback prompt for generic use cases and models.")
  .version(1)
  .tags("fallback", "stable")
  .labels({
    stable: 1,
    fallback: 1,
  })
  .template(baseTemplate)
  .components(
    SystemPromptSection.AGENT_ROLE,
    SystemPromptSection.TOOL_USE,
    SystemPromptSection.MCP,
    SystemPromptSection.EDITING_FILES,
    SystemPromptSection.ACT_VS_PLAN,
    SystemPromptSection.TODO,
    SystemPromptSection.CAPABILITIES,
    SystemPromptSection.RULES,
    SystemPromptSection.SYSTEM_INFO,
    SystemPromptSection.OBJECTIVE,
    SystemPromptSection.USER_INSTRUCTIONS,
  )
  .tools(
    ClineDefaultTool.BASH,
    ClineDefaultTool.FILE_READ,
    ClineDefaultTool.FILE_NEW,
    ClineDefaultTool.FILE_EDIT,
    ClineDefaultTool.SEARCH,
    ClineDefaultTool.LIST_FILES,
    ClineDefaultTool.LIST_CODE_DEF,
    ClineDefaultTool.BROWSER,
    ClineDefaultTool.MCP_USE,
    ClineDefaultTool.MCP_ACCESS,
    ClineDefaultTool.ASK,
    ClineDefaultTool.ATTEMPT,
    ClineDefaultTool.NEW_TASK,
    ClineDefaultTool.PLAN_MODE,
    ClineDefaultTool.MCP_DOCS,
    ClineDefaultTool.TODO,
  )
  .placeholders({
    MODEL_FAMILY: "generic",
  })
  .config({})
  .build();

// Compile-time validation
const validationResult = validateVariant({ ...config, id: "generic" }, { strict: true });
if (!validationResult.isValid) {
  console.error("Generic variant configuration validation failed:", validationResult.errors);
  throw new Error(`Invalid generic variant configuration: ${validationResult.errors.join(", ")}`);
}

// Export type information for better IDE support
export type GenericVariantConfig = typeof config;
```

### Advanced Variant with Overrides (Using Builder Pattern)

```typescript
// variants/next-gen/config.ts
import { ModelFamily } from "@/shared/prompts";
import { ClineDefaultTool } from "@/shared/tools";
import { SystemPromptSection } from "../../templates/placeholders";
import { validateVariant } from "../../validation/VariantValidator";
import { createVariant } from "../builder";
import { baseTemplate, rules_template } from "./template";

// Type-safe variant configuration using the builder pattern
export const config = createVariant(ModelFamily.NEXT_GEN)
  .description("Prompt tailored to newer frontier models with smarter agentic capabilities.")
  .version(1)
  .tags("next-gen", "advanced", "production")
  .labels({
    stable: 1,
    production: 1,
    advanced: 1,
  })
  .template(baseTemplate)
  .components(
    SystemPromptSection.AGENT_ROLE,
    SystemPromptSection.TOOL_USE,
    SystemPromptSection.MCP,
    SystemPromptSection.EDITING_FILES,
    SystemPromptSection.ACT_VS_PLAN,
    SystemPromptSection.TODO,
    SystemPromptSection.CAPABILITIES,
    SystemPromptSection.FEEDBACK,  // Additional component for next-gen
    SystemPromptSection.RULES,
    SystemPromptSection.SYSTEM_INFO,
    SystemPromptSection.OBJECTIVE,
    SystemPromptSection.USER_INSTRUCTIONS,
  )
  .tools(
    ClineDefaultTool.BASH,
    ClineDefaultTool.FILE_READ,
    ClineDefaultTool.FILE_NEW,
    ClineDefaultTool.FILE_EDIT,
    ClineDefaultTool.SEARCH,
    ClineDefaultTool.LIST_FILES,
    ClineDefaultTool.LIST_CODE_DEF,
    ClineDefaultTool.BROWSER,
    ClineDefaultTool.WEB_FETCH,  // Additional tool for next-gen
    ClineDefaultTool.MCP_USE,
    ClineDefaultTool.MCP_ACCESS,
    ClineDefaultTool.ASK,
    ClineDefaultTool.ATTEMPT,
    ClineDefaultTool.NEW_TASK,
    ClineDefaultTool.PLAN_MODE,
    ClineDefaultTool.MCP_DOCS,
    ClineDefaultTool.TODO,
  )
  .placeholders({
    MODEL_FAMILY: ModelFamily.NEXT_GEN,
  })
  .config({})
  // Override the RULES component with custom template
  .overrideComponent(SystemPromptSection.RULES, {
    template: rules_template,
  })
  .build();

// Compile-time validation
const validationResult = validateVariant({ ...config, id: "next-gen" }, { strict: true });
if (!validationResult.isValid) {
  console.error("Next-gen variant configuration validation failed:", validationResult.errors);
  throw new Error(`Invalid next-gen variant configuration: ${validationResult.errors.join(", ")}`);
}

// Export type information for better IDE support
export type NextGenVariantConfig = typeof config;
```

### Compact Variant with Component Overrides

```typescript
// variants/xs/config.ts
import { ModelFamily } from "@/shared/prompts";
import { ClineDefaultTool } from "@/shared/tools";
import { SystemPromptSection } from "../../templates/placeholders";
import { validateVariant } from "../../validation/VariantValidator";
import { createVariant } from "../builder";
import { xsComponentOverrides } from "./overrides";
import { baseTemplate } from "./template";

// Type-safe variant configuration using the builder pattern
export const config = createVariant(ModelFamily.XS)
  .description("Prompt for models with a small context window.")
  .version(1)
  .tags("local", "xs", "compact")
  .labels({
    stable: 1,
    production: 1,
    advanced: 1,
  })
  .template(baseTemplate)
  .components(
    SystemPromptSection.AGENT_ROLE,
    SystemPromptSection.RULES,
    SystemPromptSection.ACT_VS_PLAN,
    SystemPromptSection.CAPABILITIES,
    SystemPromptSection.EDITING_FILES,
    SystemPromptSection.OBJECTIVE,
    SystemPromptSection.SYSTEM_INFO,
    SystemPromptSection.USER_INSTRUCTIONS,
  )
  .tools(
    ClineDefaultTool.BASH,
    ClineDefaultTool.FILE_READ,
    ClineDefaultTool.FILE_NEW,
    ClineDefaultTool.FILE_EDIT,
    ClineDefaultTool.SEARCH,
    ClineDefaultTool.LIST_FILES,
    ClineDefaultTool.ASK,
    ClineDefaultTool.ATTEMPT,
    ClineDefaultTool.NEW_TASK,
    ClineDefaultTool.PLAN_MODE,
    ClineDefaultTool.MCP_USE,
    ClineDefaultTool.MCP_ACCESS,
    ClineDefaultTool.MCP_DOCS,
  )
  .placeholders({
    MODEL_FAMILY: ModelFamily.XS,
  })
  .config({})
  .build();

// Apply component overrides after building the base configuration
// This is necessary because the builder pattern doesn't support bulk overrides
Object.assign(config.componentOverrides, xsComponentOverrides);

// Compile-time validation
const validationResult = validateVariant({ ...config, id: "xs" }, { strict: true });
if (!validationResult.isValid) {
  console.error("XS variant configuration validation failed:", validationResult.errors);
  throw new Error(`Invalid XS variant configuration: ${validationResult.errors.join(", ")}`);
}

// Export type information for better IDE support
export type XsVariantConfig = typeof config;
```

### VariantBuilder API Reference

The `VariantBuilder` class provides a fluent, type-safe API for creating variant configurations:

```typescript
import { createVariant } from "../VariantBuilder";

const config = createVariant(ModelFamily.GENERIC)
  .description("Brief description of this variant")  // Required
  .version(1)                                        // Required, defaults to 1
  .tags("tag1", "tag2", "tag3")                     // Optional, can be chained
  .labels({ stable: 1, production: 1 })             // Optional
  .template(baseTemplate)                           // Required
  .components(                                      // Required, type-safe component selection
    SystemPromptSection.AGENT_ROLE,
    SystemPromptSection.TOOL_USE,
    // ... more components
  )
  .tools(                                          // Optional, type-safe tool selection
    ClineDefaultTool.BASH,
    ClineDefaultTool.FILE_READ,
    // ... more tools
  )
  .placeholders({                                  // Optional
    MODEL_FAMILY: "generic",
    CUSTOM_PLACEHOLDER: "value",
  })
  .config({                                        // Optional, model-specific config
    temperature: 0.7,
    maxTokens: 4096,
  })
  .overrideComponent(SystemPromptSection.RULES, {  // Optional, component overrides
    template: customRulesTemplate,
  })
  .overrideTool(ClineDefaultTool.BASH, {          // Optional, tool overrides
    enabled: false,
  })
  .build();                                       // Returns Omit<PromptVariant, "id">
```

## Usage Examples

### Basic Usage

```typescript
// Initialize registry (done once at startup)
const registry = PromptRegistry.getInstance();
await registry.load();

// Get prompt for specific model
const prompt = await registry.get("claude-3-5-sonnet-20241022", context);

// Get prompt for next-gen model (automatically detects model family)
const prompt = await registry.get("claude-4-20250101", context);
```

### Version and Tag-based Retrieval

```typescript
// Get specific version
const prompt = await registry.getVersion("next-gen", 2, context);

// Get by tag/label with next-gen prioritization
const prompt = await registry.getByTag("claude-4", "production", undefined, context, true);

// Get by label
const prompt = await registry.getByTag("generic", undefined, "stable", context);
```

### Runtime Placeholder Resolution

```typescript
// Add runtime placeholders to context
context.runtimePlaceholders = {
  "USER_NAME": "John",
  "PROJECT_TYPE": "React",
  "CUSTOM_INSTRUCTION": "Focus on TypeScript best practices"
};

const prompt = await registry.get("next-gen", context);
```

## Model Family Detection

The system automatically detects model families based on model IDs:

```typescript
function getModelFamily(modelId: string): ModelFamily {
  // Check for next-gen models first
  if (isNextGenModel(modelId)) {
    return ModelFamily.NEXT_GEN;
  }
  
  if (modelId.includes("qwen")) {
    return ModelFamily.XS;
  }
  
  // Default fallback
  return ModelFamily.GENERIC;
}

function isNextGenModel(modelId: string): boolean {
  return (
    isClaude4ModelFamily(mockApiHandlerModel) ||
    isGemini2dot5ModelFamily(mockApiHandlerModel) ||
    isGrok4ModelFamily(mockApiHandlerModel) ||
    isGPT5ModelFamily(mockApiHandlerModel)
  );
}
```

## Available Components

The system includes the following built-in components:

- `AGENT_ROLE_SECTION`: Agent identity and role definition
- `TOOL_USE_SECTION`: Tool usage instructions and available tools
- `MCP_SECTION`: MCP server information and capabilities
- `EDITING_FILES_SECTION`: File editing guidelines and best practices
- `ACT_VS_PLAN_SECTION`: Action vs planning mode instructions
- `TODO_SECTION`: Todo management and task tracking
- `CAPABILITIES_SECTION`: Agent capabilities and limitations
- `FEEDBACK_SECTION`: Feedback and improvement instructions (next-gen only)
- `RULES_SECTION`: Behavioral rules and constraints
- `SYSTEM_INFO_SECTION`: System environment information
- `OBJECTIVE_SECTION`: Current task objective
- `USER_INSTRUCTIONS_SECTION`: User-provided custom instructions

## Available Tools

The system supports the following tools (mapped to `ClineDefaultTool` enum):

- `BASH`: Execute shell commands
- `FILE_READ`: Read file contents
- `FILE_NEW`: Create new files
- `FILE_EDIT`: Edit existing files
- `SEARCH`: Search through files
- `LIST_FILES`: List directory contents
- `LIST_CODE_DEF`: List code definitions
- `BROWSER`: Browser automation (conditional)
- `WEB_FETCH`: Web content fetching (next-gen only)
- `MCP_USE`: Use MCP tools
- `MCP_ACCESS`: Access MCP resources
- `ASK`: Ask follow-up questions
- `ATTEMPT`: Attempt task completion
- `NEW_TASK`: Create new tasks
- `PLAN_MODE`: Plan mode responses
- `MCP_DOCS`: Load MCP documentation
- `TODO`: Todo management

## Adding New Tools

### Tool Structure and Anatomy

Each tool in Cline follows a specific structure with variants for different model families. Here's the anatomy of a tool:

```typescript
// src/core/prompts/system-prompt/tools/my_new_tool.ts
import { ModelFamily } from "@/shared/prompts"
import { ClineDefaultTool } from "@/shared/tools"
import type { ClineToolSpec } from "../spec"

const id = ClineDefaultTool.MY_NEW_TOOL // Add to enum first

const generic: ClineToolSpec = {
	variant: ModelFamily.GENERIC,
	id,
	name: "my_new_tool",
	description: "Description of what this tool does and when to use it",
	parameters: [
		{
			name: "required_param",
			required: true,
			instruction: "Description of this parameter and how to use it",
			usage: "Example value or placeholder text",
		},
		{
			name: "optional_param",
			required: false,
			instruction: "Description of optional parameter",
			usage: "Optional example (optional)",
			dependencies: [ClineDefaultTool.SOME_OTHER_TOOL], // Only show if dependency exists
		},
	],
}

// Create variants for different model families if needed
const nextGen = { ...generic, variant: ModelFamily.NEXT_GEN }
const gpt = { ...generic, variant: ModelFamily.GPT }
const gemini = { ...generic, variant: ModelFamily.GEMINI }

export const my_new_tool_variants = [generic, nextGen, gpt, gemini]
```

### Step-by-Step Instructions for Adding a New Tool

#### 1. Add Tool ID to Enum

First, add your tool ID to the `ClineDefaultTool` enum:

```typescript
// src/shared/tools.ts
export enum ClineDefaultTool {
	// ... existing tools
	MY_NEW_TOOL = "my_new_tool",
}
```

#### 2. Create Tool Specification File

Create a new file in `src/core/prompts/system-prompt/tools/` following the naming convention `{tool_name}.ts`:

```typescript
// src/core/prompts/system-prompt/tools/my_new_tool.ts
import { ModelFamily } from "@/shared/prompts"
import { ClineDefaultTool } from "@/shared/tools"
import type { ClineToolSpec } from "../spec"

const id = ClineDefaultTool.MY_NEW_TOOL

const generic: ClineToolSpec = {
	variant: ModelFamily.GENERIC,
	id,
	name: "my_new_tool",
	description: "Comprehensive description of the tool's purpose, when to use it, and what it accomplishes. Be specific about use cases and limitations.",
	parameters: [
		{
			name: "input_parameter",
			required: true,
			instruction: "Clear instruction on what this parameter expects and how to format it",
			usage: "Example input here",
		},
		{
			name: "options",
			required: false,
			instruction: "Optional configuration or settings for the tool",
			usage: "Configuration options (optional)",
		},
	],
}

// Export variants array - this is crucial for registration
export const my_new_tool_variants = [generic]
```

#### 3. Export Tool from Index

Add your tool export to the tools index file:

```typescript
// src/core/prompts/system-prompt/tools/index.ts
export * from "./my_new_tool"
```

#### 4. Register Tool in Init File

Add your tool to the registration function:

```typescript
// src/core/prompts/system-prompt/tools/init.ts
import { my_new_tool_variants } from "./my_new_tool"

export function registerClineToolSets(): void {
	const allToolVariants = [
		// ... existing tool variants
		...my_new_tool_variants,
	]

	allToolVariants.forEach((v) => {
		ClineToolSet.register(v)
	})
}
```

#### 5. Implement Tool Handler (Backend)

Create the actual tool implementation in the appropriate handler:

```typescript
// In your tool handler class (e.g., ClineProvider)
async handleMyNewTool(args: { input_parameter: string; options?: string }) {
	// Implement your tool logic here
	const result = await performToolOperation(args.input_parameter, args.options)
	
	return {
		type: "tool_result" as const,
		content: result,
	}
}
```

### Advanced Tool Configuration

#### Context-Aware Tools

Tools can be conditionally enabled based on context:

```typescript
const contextAwareTool: ClineToolSpec = {
	variant: ModelFamily.GENERIC,
	id: ClineDefaultTool.CONTEXT_TOOL,
	name: "context_tool",
	description: "Tool that only appears in certain contexts",
	contextRequirements: (context: SystemPromptContext) => {
		// Only show this tool if browser support is available
		return context.supportsBrowserUse === true
	},
	parameters: [
		// ... parameters
	],
}
```

#### Model-Specific Variants

Create different tool behaviors for different model families:

```typescript
const claude: ClineToolSpec = {
	variant: ModelFamily.GENERIC,
	id: ClineDefaultTool.MODEL_SPECIFIC_TOOL,
	name: "model_specific_tool",
	description: "Tool optimized for Claude models with detailed instructions",
	parameters: [
		{
			name: "detailed_input",
			required: true,
			instruction: "Provide comprehensive details as Claude handles complex instructions well",
			usage: "Detailed input with context and examples",
		},
	],
}

const gpt: ClineToolSpec = {
	...claude,
	variant: ModelFamily.GPT,
	description: "Tool optimized for GPT models with concise instructions",
	parameters: [
		{
			name: "detailed_input",
			required: true,
			instruction: "Provide concise, structured input",
			usage: "Brief, structured input",
		},
	],
}

export const model_specific_tool_variants = [claude, gpt]
```

#### Parameter Dependencies

Tools can have parameters that only appear when other tools are available:

```typescript
const dependentTool: ClineToolSpec = {
	variant: ModelFamily.GENERIC,
	id: ClineDefaultTool.DEPENDENT_TOOL,
	name: "dependent_tool",
	description: "Tool with conditional parameters",
	parameters: [
		{
			name: "always_present",
			required: true,
			instruction: "This parameter is always available",
			usage: "Standard input",
		},
		{
			name: "conditional_param",
			required: false,
			instruction: "This parameter only appears if TODO tool is available",
			usage: "Conditional input (optional)",
			dependencies: [ClineDefaultTool.TODO],
		},
	],
}
```

### Best Practices

#### 1. Tool Naming Conventions
- Use snake_case for tool IDs and file names
- Use descriptive names that clearly indicate the tool's purpose
- Prefix with action verb when appropriate (e.g., `create_file`, `search_code`)

#### 2. Parameter Design
- Always provide clear, actionable instructions
- Include usage examples that show expected format
- Mark parameters as required/optional appropriately
- Use dependencies to avoid cluttering the prompt with irrelevant parameters

#### 3. Description Guidelines
- Be specific about when and why to use the tool
- Include limitations and constraints
- Mention any prerequisites or setup requirements
- Provide context about expected outcomes

#### 4. Model Variant Strategy
- Start with a GENERIC variant that works across all models
- Create specific variants only when models need different instructions
- Keep variant differences minimal and focused on instruction style
- Test across different model families to ensure compatibility

#### 5. Error Handling
- Design tools to fail gracefully
- Provide meaningful error messages
- Consider edge cases in parameter validation
- Document expected error scenarios

### Testing Your New Tool

#### 1. Unit Tests
Create unit tests for your tool specification:

```typescript
// src/core/prompts/system-prompt/tools/__tests__/my_new_tool.test.ts
import { my_new_tool_variants } from "../my_new_tool"
import { ModelFamily } from "@/shared/prompts"

describe("my_new_tool", () => {
	it("should have correct structure", () => {
		const generic = my_new_tool_variants.find(v => v.variant === ModelFamily.GENERIC)
		expect(generic).toBeDefined()
		expect(generic?.name).toBe("my_new_tool")
		expect(generic?.parameters).toHaveLength(2)
	})
})
```

#### 2. Integration Tests
Add your tool to the integration test suite:

```typescript
// src/core/prompts/system-prompt/__tests__/integration.test.ts
// The test will automatically pick up your tool if properly registered
```

#### 3. Manual Testing
1. Run the unit tests: `npm run test:unit`
2. Start the application and verify your tool appears in the system prompt
3. Test tool execution with various parameter combinations
4. Verify tool works across different model families

### Complete Example: File Analyzer Tool

Here's a complete example of adding a new "analyze_file" tool:

```typescript
// 1. Add to src/shared/tools.ts
export enum ClineDefaultTool {
	// ... existing tools
	ANALYZE_FILE = "analyze_file",
}

// 2. Create src/core/prompts/system-prompt/tools/analyze_file.ts
import { ModelFamily } from "@/shared/prompts"
import { ClineDefaultTool } from "@/shared/tools"
import type { ClineToolSpec } from "../spec"

const id = ClineDefaultTool.ANALYZE_FILE

const generic: ClineToolSpec = {
	variant: ModelFamily.GENERIC,
	id,
	name: "analyze_file",
	description: "Analyze a file's structure, dependencies, and potential issues. Use this when you need to understand a file's architecture, identify problems, or assess code quality before making changes.",
	parameters: [
		{
			name: "file_path",
			required: true,
			instruction: "The path to the file you want to analyze (relative to current working directory)",
			usage: "src/components/MyComponent.tsx",
		},
		{
			name: "analysis_type",
			required: false,
			instruction: "Type of analysis to perform: 'structure', 'dependencies', 'quality', or 'all'",
			usage: "all (optional)",
		},
		{
			name: "include_suggestions",
			required: false,
			instruction: "Whether to include improvement suggestions in the analysis",
			usage: "true (optional)",
		},
	],
}

const nextGen: ClineToolSpec = {
	...generic,
	variant: ModelFamily.NEXT_GEN,
	description: "Perform comprehensive file analysis including structure, dependencies, code quality, and improvement suggestions. Ideal for code review and refactoring planning.",
}

export const analyze_file_variants = [generic, nextGen]

// 3. Add to src/core/prompts/system-prompt/tools/index.ts
export * from "./analyze_file"

// 4. Add to src/core/prompts/system-prompt/tools/init.ts
import { analyze_file_variants } from "./analyze_file"

export function registerClineToolSets(): void {
	const allToolVariants = [
		// ... existing variants
		...analyze_file_variants,
	]
	// ... rest of function
}
```

This comprehensive guide should help developers understand both the architecture and practical steps needed to extend Cline with new tools.

## Key Features

- **Modular Components**: Reusable across different model variants  
- **Template System**: `{{placeholder}}` support with runtime resolution  
- **Versioning**: Full version control with tags and labels  
- **Model Family Detection**: Automatic model family detection and fallback  
- **Flexible Tool Configuration**: Per-variant tool selection and customization  
- **Component Overrides**: Custom templates for specific components  
- **Runtime Placeholders**: Dynamic value injection at build time  
- **Performance Optimized**: Efficient component building and template resolution  
- **Error Handling**: Graceful degradation when components fail  
- **Conditional Logic**: Context-aware tool and component inclusion


---

# FILE: src/core/prompts/system-prompt/__tests__/README.md

# System Prompt Integration Tests

This directory contains integration tests for the system prompt generation with snapshot testing capabilities.

## Overview

The integration tests validate that system prompts remain consistent across different:
- Model families (Generic, Next-Gen, XS)
- Provider configurations (OpenAI, Anthropic, LMStudio, etc.)
- Context variations (browser enabled/disabled, MCP servers, focus chain, etc.)

## Snapshot Testing

The tests use snapshot testing to detect unintended changes in prompt generation. Snapshots are stored in the `__snapshots__/` directory.

### Running Tests

#### Normal Test Mode
```bash
# Run tests and compare against existing snapshots
npm test
# or
yarn test
```

Tests will **fail** if generated prompts don't match existing snapshots, showing detailed differences.

#### Update Snapshot Mode
```bash
# Update all snapshots with current prompt output
npm test -- --update-snapshots
```

Use this when you've intentionally changed prompt generation and want to update the baseline.

### When Tests Fail

When snapshot tests fail, you'll see a detailed error message showing:
1. **Which snapshot failed** (e.g., `openai_gpt-3-basic.snap`)
2. **Detailed differences** between expected and actual output
3. **Clear instructions** on how to fix the issue

#### Example Failure Output
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ SNAPSHOT MISMATCH: openai_gpt-3-basic.snap
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Expected length: 15420 characters
Actual length: 15456 characters
Line count difference: 245 vs 246

First differences:
Line 23:
  - Expected: You are Cline, an AI assistant created by Anthropic.
  + Actual:   You are Cline, an AI coding assistant created by Anthropic.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔧 HOW TO FIX:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 📋 Review the differences above to understand what changed
2. 🤔 Determine if the changes are intentional:
   - ✅ Expected changes (prompt improvements, new features)
   - ❌ Unexpected changes (bugs, regressions)

3. 🔄 If changes are correct, update snapshots:
   npm test -- --update-snapshots

4. 🐛 If changes are unintentional, investigate:
   - Check recent changes to prompt generation logic
   - Verify context/configuration hasn't changed unexpectedly
   - Look for dependency updates that might affect output
```

### Workflow

1. **Make changes** to prompt generation code
2. **Run tests** to see if snapshots still match
3. **Review differences** to ensure changes are intentional
4. **Update snapshots** if changes are correct: `npm test -- --update-snapshots`
5. **Commit both** code changes and updated snapshots

### Snapshot Files

Snapshots are stored with descriptive names:
- `openai_gpt-3-basic.snap` - OpenAI GPT-3 with basic context
- `anthropic_claude-sonnet-4-no-browser.snap` - Claude Sonnet 4 without browser support
- `lmstudio_qwen3_coder-no-mcp.snap` - LMStudio Qwen3 Coder without MCP servers
- `old-next-gen-with-focus.snap` - Legacy next-gen prompt with focus chain
- `section-title-comparison.json` - Section title compatibility analysis

### Best Practices

1. **Review all changes** before updating snapshots
2. **Update snapshots atomically** - don't mix code and snapshot changes
3. **Test thoroughly** after updating snapshots
4. **Document significant changes** in commit messages
5. **Consider backward compatibility** when changing prompt structure

## Test Structure

### Model Test Cases
- **Generic Models**: Basic GPT-3 style models
- **Next-Gen Models**: Advanced models like Claude Sonnet 4
- **XS Models**: Compact models like Qwen3 Coder

### Context Variations
- **Basic**: Full context with all features enabled
- **No Browser**: Browser support disabled
- **No MCP**: No MCP servers configured
- **No Focus Chain**: Focus chain feature disabled

### Legacy Compatibility
Tests also validate compatibility with legacy prompt generation to ensure smooth transitions.


---

# FILE: src/core/prompts/system-prompt/__tests__/__snapshots__/section-title-comparison.json

{
	"oldNextGenTitles": [
		"TOOL USE",
		"Tool Use Formatting",
		"Tools",
		"execute_command",
		"read_file",
		"write_to_file",
		"replace_in_file",
		"list_files",
		"list_code_definition_names",
		"browser_action",
		"web_fetch",
		"use_mcp_tool",
		"access_mcp_resource",
		"search_files",
		"ask_followup_question",
		"attempt_completion",
		"new_task",
		"plan_mode_respond",
		"load_mcp_documentation",
		"Tool Use Examples",
		"Example 1: Requesting to execute a command",
		"Example 2: Requesting to create a new file",
		"Example 3: Creating a new task",
		"Example 4: Requesting to make targeted edits to a file",
		"Example 5: Requesting to use an MCP tool",
		"Example 6: Another example of using an MCP tool (where the server name is a unique identifier such as a URL)",
		"Tool Use Guidelines",
		"AUTOMATIC TODO LIST MANAGEMENT",
		"MCP SERVERS",
		"Connected MCP Servers",
		"test-server (`test`)",
		"Available Tools",
		"EDITING FILES",
		"write_to_file",
		"Purpose",
		"When to Use",
		"Important Considerations",
		"replace_in_file",
		"Purpose",
		"When to Use",
		"Advantages",
		"Choosing the Appropriate Tool",
		"Auto-formatting Considerations",
		"Workflow Tips",
		"What is PLAN MODE?",
		"UPDATING TASK PROGRESS",
		"CAPABILITIES",
		"RULES",
		"SYSTEM INFORMATION",
		"OBJECTIVE"
	],
	"newNextGenTitles": [
		"TOOL USE",
		"Tool Use Formatting",
		"Tools",
		"execute_command",
		"read_file",
		"write_to_file",
		"replace_in_file",
		"search_files",
		"list_files",
		"list_code_definition_names",
		"browser_action",
		"web_fetch",
		"use_mcp_tool",
		"access_mcp_resource",
		"ask_followup_question",
		"attempt_completion",
		"new_task",
		"plan_mode_respond",
		"load_mcp_documentation",
		"Tool Use Examples",
		"Example 1: Requesting to execute a command",
		"Example 2: Requesting to create a new file",
		"Example 3: Creating a new task",
		"Example 4: Requesting to make targeted edits to a file",
		"Example 5: Requesting to use an MCP tool",
		"Example 6: Another example of using an MCP tool (where the server name is a unique identifier such as a URL)",
		"Tool Use Guidelines",
		"AUTOMATIC TODO LIST MANAGEMENT",
		"MCP SERVERS",
		"Connected MCP Servers",
		"test-server (`test`)",
		"Available Tools",
		"EDITING FILES",
		"write_to_file",
		"Purpose",
		"When to Use",
		"Important Considerations",
		"replace_in_file",
		"Purpose",
		"When to Use",
		"Advantages",
		"Choosing the Appropriate Tool",
		"Auto-formatting Considerations",
		"Workflow Tips",
		"What is PLAN MODE?",
		"UPDATING TASK PROGRESS",
		"CAPABILITIES",
		"RULES",
		"SYSTEM INFORMATION",
		"OBJECTIVE"
	],
	"oldGenericTitles": [
		"TOOL USE",
		"Tool Use Formatting",
		"Tools",
		"execute_command",
		"read_file",
		"write_to_file",
		"replace_in_file",
		"search_files",
		"list_files",
		"list_code_definition_names",
		"browser_action",
		"use_mcp_tool",
		"access_mcp_resource",
		"ask_followup_question",
		"attempt_completion",
		"new_task",
		"plan_mode_respond",
		"load_mcp_documentation",
		"Tool Use Examples",
		"Example 1: Requesting to execute a command",
		"Example 2: Requesting to create a new file",
		"Example 3: Creating a new task",
		"Example 4: Requesting to make targeted edits to a file",
		"Example 5: Requesting to use an MCP tool",
		"Example 6: Another example of using an MCP tool (where the server name is a unique identifier such as a URL)",
		"Tool Use Guidelines",
		"AUTOMATIC TODO LIST MANAGEMENT",
		"MCP SERVERS",
		"Connected MCP Servers",
		"test-server (`test`)",
		"Available Tools",
		"EDITING FILES",
		"write_to_file",
		"Purpose",
		"When to Use",
		"Important Considerations",
		"replace_in_file",
		"Purpose",
		"When to Use",
		"Advantages",
		"Choosing the Appropriate Tool",
		"Auto-formatting Considerations",
		"Workflow Tips",
		"What is PLAN MODE?",
		"UPDATING TASK PROGRESS",
		"CAPABILITIES",
		"RULES",
		"SYSTEM INFORMATION",
		"OBJECTIVE"
	],
	"newGenericTitles": [
		"TOOL USE",
		"Tool Use Formatting",
		"Tools",
		"execute_command",
		"read_file",
		"write_to_file",
		"replace_in_file",
		"search_files",
		"list_files",
		"list_code_definition_names",
		"browser_action",
		"use_mcp_tool",
		"access_mcp_resource",
		"ask_followup_question",
		"attempt_completion",
		"new_task",
		"plan_mode_respond",
		"load_mcp_documentation",
		"Tool Use Examples",
		"Example 1: Requesting to execute a command",
		"Example 2: Requesting to create a new file",
		"Example 3: Creating a new task",
		"Example 4: Requesting to make targeted edits to a file",
		"Example 5: Requesting to use an MCP tool",
		"Example 6: Another example of using an MCP tool (where the server name is a unique identifier such as a URL)",
		"Tool Use Guidelines",
		"AUTOMATIC TODO LIST MANAGEMENT",
		"MCP SERVERS",
		"Connected MCP Servers",
		"test-server (`test`)",
		"Available Tools",
		"EDITING FILES",
		"write_to_file",
		"Purpose",
		"When to Use",
		"Important Considerations",
		"replace_in_file",
		"Purpose",
		"When to Use",
		"Advantages",
		"Choosing the Appropriate Tool",
		"Auto-formatting Considerations",
		"Workflow Tips",
		"What is PLAN MODE?",
		"UPDATING TASK PROGRESS",
		"CAPABILITIES",
		"RULES",
		"SYSTEM INFORMATION",
		"OBJECTIVE"
	],
	"keySections": [
		"TOOL USE",
		"Tools",
		"execute_command",
		"read_file",
		"write_to_file"
	],
	"summary": {
		"oldNextGenCount": 50,
		"newNextGenCount": 50,
		"oldGenericCount": 49,
		"newGenericCount": 49
	}
}



---

# FILE: src/core/prompts/system-prompt/tools/README.md

# Tool Registration System

This directory contains the tool registration system for Cline tools. The system automatically collects and registers all tool variants with the `ClineToolSet` provider.

## Overview

Each tool file in this directory exports a `{toolName}_variants` array containing tool specifications for different prompt variants (e.g., Claude, GPT). The registration system automatically imports all these variants and registers them with the `ClineToolSet` provider.

## Files

- **`register.ts`** - Main registration function and utilities
- **`example-usage.ts`** - Example usage patterns
- **`index.ts`** - Exports all tools and the registration function
- **Individual tool files** - Each exports a `{toolName}_variants` array

## Usage

### Basic Registration

```typescript
import { registerAllToolVariants } from "./tools/register";

// Register all tool variants during application initialization
registerAllToolVariants();
```

### Getting Registration Summary

```typescript
import { getToolRegistrationSummary } from "./tools/register";

const summary = getToolRegistrationSummary();
console.log(summary);
// Output: { "write_to_file": ["claude"], "execute_command": ["claude", "gpt"], ... }
```

### Using Registered Tools

```typescript
import { ClineToolSet } from "../registry/ClineToolSet";
import { PromptVariant } from "@/shared/tools";

// Get all tools for a specific variant
const claudeTools = ClineToolSet.getTools(PromptVariant.CLAUDE);

// Get a specific tool by name
const writeToFileTool = ClineToolSet.getToolByName("write_to_file", PromptVariant.CLAUDE);
```

## Tool Structure

Each tool file follows this pattern:

```typescript
import { ClineDefaultTool, PromptVariant, type ClineToolSpec } from "@/shared/tools";

const claude: ClineToolSpec = {
    variant: PromptVariant.CLAUDE,
    id: "tool_name",
    description: "Tool description",
    parameters: [
        // Parameter definitions
    ],
};

const gpt: ClineToolSpec = {
    variant: PromptVariant.GPT,
    id: "tool_name_gpt",
    description: "Tool description for GPT",
    parameters: [
        // Parameter definitions
    ],
};

export const tool_name_variants = [claude, gpt];
```

## Registered Tools

The following tools are currently registered:

- `access_mcp_resource`
- `ask_followup_question`
- `attempt_completion`
- `browser_action`
- `execute_command`
- `focus_chain`
- `list_code_definition_names`
- `list_files`
- `load_mcp_documentation`
- `new_task`
- `plan_mode_respond`
- `read_file`
- `replace_in_file`
- `search_files`
- `use_mcp_tool`
- `web_fetch` (exported as `get_web_fetch_variants`)
- `write_to_file`

## Adding New Tools

1. Create a new tool file following the naming pattern: `{tool_name}.ts`
2. Export a `{tool_name}_variants` array with tool specifications
3. Add the export to `index.ts`
4. Add the import and spread to `register.ts`

## Notes

- The registration function handles duplicate registrations gracefully
- Tools are registered per variant (Claude, GPT, etc.)
- The system automatically counts unique tools and provides logging
- All tool variants are collected and registered in a single function call


---

# FILE: src/exports/README.md

# Cline API

The Cline extension exposes an API that can be used by other extensions. To use this API in your extension:

1. Copy `src/extension-api/cline.d.ts` to your extension's source directory.
2. Include `cline.d.ts` in your extension's compilation.
3. Get access to the API with the following code:

    ```ts
    const clineExtension = vscode.extensions.getExtension<ClineAPI>("saoudrizwan.claude-dev")

    if (!clineExtension?.isActive) {
    	throw new Error("Cline extension is not activated")
    }

    const cline = clineExtension.exports

    if (cline) {
    	// Now you can use the API

    	// Start a new task with an initial message
    	await cline.startNewTask("Hello, Cline! Let's make a new project...")

    	// Start a new task with an initial message and images
    	await cline.startNewTask("Use this design language", ["data:image/webp;base64,..."])

    	// Send a message to the current task
    	await cline.sendMessage("Can you fix the @problems?")

    	// Simulate pressing the primary button in the chat interface (e.g. 'Save' or 'Proceed While Running')
    	await cline.pressPrimaryButton()

    	// Simulate pressing the secondary button in the chat interface (e.g. 'Reject')
    	await cline.pressSecondaryButton()
    } else {
    	console.error("Cline API is not available")
    }
    ```

    **Note:** To ensure that the `saoudrizwan.claude-dev` extension is activated before your extension, add it to the `extensionDependencies` in your `package.json`:

    ```json
    "extensionDependencies": [
        "saoudrizwan.claude-dev"
    ]
    ```

For detailed information on the available methods and their usage, refer to the `cline.d.ts` file.



---

# FILE: src/samples/cli/github-integration/cline-responder.yml

name: Cline Issue Assistant

on:
  issue_comment:
    types: [created, edited]

permissions:
  issues: write

jobs:
  respond:
    runs-on: ubuntu-latest
    environment: cline-actions
    steps:
      - name: Check for @cline mention
        id: detect
        uses: actions/github-script@v7
        with:
          script: |
            const body = context.payload.comment?.body || "";
            const isPR = !!context.payload.issue?.pull_request;
            const hit = body.toLowerCase().includes("@cline");
            core.setOutput("hit", (!isPR && hit) ? "true" : "false");
            core.setOutput("issue_number", String(context.payload.issue?.number || ""));
            core.setOutput("issue_url", context.payload.issue?.html_url || "");
            core.setOutput("comment_body", body);

      - name: Checkout repository
        if: steps.detect.outputs.hit == 'true'
        uses: actions/checkout@v4

      # Node v20 is needed for Cline CLI on GitHub Actions Linux
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Setup Cline CLI
        if: steps.detect.outputs.hit == 'true'
        run: |
          # Install the Cline CLI
          sudo npm install -g cline

      - name: Create Cline Instance
        if: steps.detect.outputs.hit == 'true'
        env:
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
          CLINE_DIR: ${{ runner.temp }}/cline
        run: |
          # Create instance and capture output
          INSTANCE_OUTPUT=$(cline instance new 2>&1)
          
          # Parse address from output (format: "  Address: 127.0.0.1:36733")
          CLINE_ADDRESS=$(echo "$INSTANCE_OUTPUT" | grep "Address:" | grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]+')
          echo "CLINE_ADDRESS=$CLINE_ADDRESS" >> $GITHUB_ENV
          
          # Configure API key
          cline config set open-router-api-key=$OPENROUTER_API_KEY --address $CLINE_ADDRESS -v

      - name: Download analyze script
        if: steps.detect.outputs.hit == 'true'
        run: |
          export GITORG="YOUR-GITHUB-ORG"
          export GITREPO="YOUR-GITHUB-REPO"

          curl -L https://raw.githubusercontent.com/${GITORG}/${GITREPO}/refs/heads/main/git-scripts/analyze-issue.sh -o analyze-issue.sh
          chmod +x analyze-issue.sh

      - name: Run analysis
        if: steps.detect.outputs.hit == 'true'
        id: analyze
        env:
          ISSUE_URL: ${{ steps.detect.outputs.issue_url }}
          COMMENT: ${{ steps.detect.outputs.comment_body }}
          CLINE_ADDRESS: ${{ env.CLINE_ADDRESS }}
        run: |
          set -euo pipefail
          
          RESULT=$(./analyze-issue.sh "${ISSUE_URL}" "Analyze this issue. The user asked: ${COMMENT}" "$CLINE_ADDRESS")
          
          {
            echo 'result<<EOF'
            printf "%s\n" "$RESULT"
            echo 'EOF'
          } >> "$GITHUB_OUTPUT"

      - name: Post response
        if: steps.detect.outputs.hit == 'true'
        uses: actions/github-script@v7
        env:
          ISSUE_NUMBER: ${{ steps.detect.outputs.issue_number }}
          RESULT: ${{ steps.analyze.outputs.result }}
        with:
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: Number(process.env.ISSUE_NUMBER),
              body: process.env.RESULT || "(no output)"
            });



---

# FILE: src/shared/providers/bedrock.json

{
	"regions": [
		"us-east-1",
		"us-east-2",
		"us-west-1",
		"us-west-2",
		"ap-south-1",
		"ap-northeast-1",
		"ap-northeast-2",
		"ap-northeast-3",
		"ap-southeast-1",
		"ap-southeast-2",
		"ap-southeast-3",
		"ap-southeast-4",
		"ap-southeast-5",
		"ap-southeast-7",
		"ca-central-1",
		"eu-central-1",
		"eu-central-2",
		"eu-west-1",
		"eu-west-2",
		"eu-west-3",
		"eu-north-1",
		"eu-south-1",
		"eu-south-2",
		"sa-east-1",
		"us-gov-east-1",
		"us-gov-west-1"
	]
}



---

# FILE: src/shared/providers/providers.json

{
	"list": [
		{
			"value": "cline",
			"label": "Cline"
		},
		{
			"value": "openai-codex",
			"label": "ChatGPT Subscription"
		},
		{
			"value": "gemini",
			"label": "Google Gemini"
		},
		{
			"value": "openai",
			"label": "OpenAI Compatible"
		},
		{
			"value": "anthropic",
			"label": "Anthropic"
		},
		{
			"value": "bedrock",
			"label": "Amazon Bedrock"
		},
		{
			"value": "vscode-lm",
			"label": "GitHub Copilot"
		},
		{
			"value": "deepseek",
			"label": "DeepSeek"
		},
		{
			"value": "openai-native",
			"label": "OpenAI"
		},
		{
			"value": "openrouter",
			"label": "OpenRouter"
		},
		{
			"value": "ollama",
			"label": "Ollama"
		},
		{
			"value": "vertex",
			"label": "GCP Vertex AI"
		},
		{
			"value": "litellm",
			"label": "LiteLLM"
		},
		{
			"value": "claude-code",
			"label": "Claude Code"
		},
		{
			"value": "sapaicore",
			"label": "SAP AI Core"
		},
		{
			"value": "mistral",
			"label": "Mistral"
		},
		{
			"value": "zai",
			"label": "Z AI"
		},
		{
			"value": "groq",
			"label": "Groq"
		},
		{
			"value": "cerebras",
			"label": "Cerebras"
		},
		{
			"value": "vercel-ai-gateway",
			"label": "Vercel AI Gateway"
		},
		{
			"value": "baseten",
			"label": "Baseten"
		},
		{
			"value": "requesty",
			"label": "Requesty"
		},
		{
			"value": "fireworks",
			"label": "Fireworks AI"
		},
		{
			"value": "together",
			"label": "Together"
		},
		{
			"value": "qwen",
			"label": "Alibaba Qwen"
		},
		{
			"value": "qwen-code",
			"label": "Qwen Code"
		},
		{
			"value": "doubao",
			"label": "Bytedance Doubao"
		},
		{
			"value": "lmstudio",
			"label": "LM Studio"
		},
		{
			"value": "moonshot",
			"label": "Moonshot"
		},
		{
			"value": "huggingface",
			"label": "Hugging Face"
		},
		{
			"value": "nebius",
			"label": "Nebius AI Studio"
		},
		{
			"value": "asksage",
			"label": "AskSage"
		},
		{
			"value": "xai",
			"label": "xAI"
		},
		{
			"value": "sambanova",
			"label": "SambaNova"
		},
		{
			"value": "huawei-cloud-maas",
			"label": "Huawei Cloud MaaS"
		},
		{
			"value": "dify",
			"label": "Dify.ai"
		},
		{
			"value": "oca",
			"label": "Oracle Code Assist"
		},
		{
			"value": "minimax",
			"label": "MiniMax"
		},
		{
			"value": "hicap",
			"label": "Hicap"
		},
		{
			"value": "aihubmix",
			"label": "AIhubmix"
		},
		{
			"value": "nousResearch",
			"label": "NousResearch"
		},
		{
			"value": "wandb",
			"label": "W&B Inference by CoreWeave"
		}
	]
}



---

# FILE: src/shared/providers/vertex.json

{
	"regions": [
		"us-east5",
		"us-central1",
		"europe-west1",
		"europe-west4",
		"asia-southeast1",
		"global"
	]
}



---

# FILE: src/test/e2e/README.md

# E2E Tests

This directory contains the end-to-end tests for the Cline VS Code extension using Playwright. These tests simulate user interactions with the extension in a real VS Code environment.

## Test Structure

The E2E test suite consists of several key components:

### Test Files

- **`auth.test.ts`** - Tests API key setup, provider selection, and navigation to settings
- **`chat.test.ts`** - Tests chat functionality including message sending, mode switching (Plan/Act), slash commands, and @ mentions
- **`diff.test.ts`** - Tests the diff editor functionality for file modifications
- **`editor.test.ts`** - Tests code actions, editor panel integration, and code selection features

### Test Infrastructure

- **`utils/helpers.ts`** - Core test utilities and fixtures including:
  - `e2e` - Main test fixture for single-root workspace tests
  - `e2eMultiRoot` - Test fixture for multi-root workspace tests
  - `E2ETestHelper` - Helper class with utilities for VS Code interaction
- **`utils/common.ts`** - Common utility functions for UI interactions
- **`utils/global.setup.ts`** - Global test setup and cleanup
- **`utils/build.mjs`** - Build script for test environment preparation

### Test Fixtures

- **`fixtures/workspace/`** - Single-root workspace test files (HTML, TypeScript, etc.)
- **`fixtures/workspace_2/`** - Additional workspace with Python provider files
- **`fixtures/multiroots.code-workspace`** - Multi-root workspace configuration
- **`fixtures/server/`** - Mock API server for testing Cline's backend interactions

## Running Tests

### Basic Test Execution

To build the test environment and run all E2E tests:

```bash
npm run test:e2e
```

To run all E2E tests without re-building the test environment (e.g. only test files were updated):

```bash
npm run e2e
```

### Debug Mode

To run E2E tests in debug mode with Playwright's interactive debugger:

```bash
npm run test:e2e -- --debug
# Or only run the tests without re-building
npm run e2e -- --debug
```

In debug mode, Playwright will:
- Open a browser window showing the VS Code instance
- Pause execution at the beginning of each test
- Allow you to step through test actions
- Provide a console for inspecting elements and state

### Additional Options

Run specific test files:
```bash
npm run e2e -- auth.test.ts
```

Run tests with specific tags or patterns:
```bash
npm run e2e -- --grep "Chat"
```

Run tests in headed mode (visible browser):
```bash
npm run e2e -- --headed
```

## Writing Tests

### Basic Test Structure

Use the `e2e` fixture for single-root workspace tests:

```typescript
import { expect } from "@playwright/test"
import { e2e } from "./utils/helpers"

e2e("Test description", async ({ sidebar, helper, page }) => {
  // Sign in to Cline
  await helper.signin(sidebar)
  
  // Test interactions
  const inputbox = sidebar.getByTestId("chat-input")
  await inputbox.fill("Hello, Cline!")
  await sidebar.getByTestId("send-button").click()
  
  // Assertions
  await expect(sidebar.getByText("API Request...")).toBeVisible()
})
```

For multi-root workspace tests, use `e2eMultiRoot`:

```typescript
import { e2eMultiRoot } from "./utils/helpers"

e2eMultiRoot("[Multi-roots] Test description", async ({ sidebar, helper }) => {
  // Test implementation
})
```

### Available Fixtures

The test fixtures provide the following objects:

- **`sidebar`** - Playwright Frame object for the Cline extension's sidebar
- **`helper`** - E2ETestHelper instance with utility methods
- **`page`** - Playwright Page object for the main VS Code window
- **`app`** - ElectronApplication instance for VS Code
- **`server`** - Mock API server for backend testing

### Common Patterns

#### Authentication
```typescript
// Sign in with test API key
await helper.signin(sidebar)
```

#### Chat Interactions
```typescript
const inputbox = sidebar.getByTestId("chat-input")
await inputbox.fill("Your message")
await sidebar.getByTestId("send-button").click()
```

#### Mode Switching
```typescript
const actButton = sidebar.getByRole("switch", { name: "Act" })
const planButton = sidebar.getByRole("switch", { name: "Plan" })
await actButton.click() // Switch to Plan mode
```

#### File Operations
```typescript
// Open file explorer and select code
await openTab(page, "Explorer ")
await page.getByRole("treeitem", { name: "index.html" }).locator("a").click()
await addSelectedCodeToClineWebview(page)
```

#### Settings Navigation
```typescript
await sidebar.getByText("settings").click()
await sidebar.getByTestId("tab-api-config").click()
```

### Using the Recorder with Debug Mode

The `--debug` flag enables Playwright's interactive debugging features:

1. **Start debugging session:**
   ```bash
   npm run test:e2e -- --debug
   ```

2. **Playwright will open:**
   - A VS Code window with Cline extension loaded
   - Playwright Inspector for step-by-step debugging
   - Browser developer tools for element inspection

3. **Recording interactions:**
   - Use the "Record" button in Playwright Inspector
   - Interact with the VS Code interface
   - Playwright generates test code automatically
   - Copy the generated code into your test files

4. **Debugging existing tests:**
   - Set breakpoints in your test code
   - Use the "Step over" button to execute line by line
   - Inspect element selectors and page state
   - Modify selectors and retry actions

### Test Environment

The test environment includes:

- **VS Code Configuration:**
  - Disabled updates, workspace trust, and welcome screens
  - Extension development mode with Cline loaded
  - Temporary user data and extensions directories

- **Mock API Server:**
  - Runs on `http://localhost:7777`
  - Provides mock responses for Cline API calls
  - Supports authentication, chat completions, and user management

- **Test Workspaces:**
  - Single-root workspace with HTML, TypeScript, and README files
  - Multi-root workspace with Python provider examples
  - Configurable through fixtures

### Best Practices

1. **Use semantic selectors:**
   ```typescript
   // Good - uses test IDs
   sidebar.getByTestId("chat-input")
   
   // Good - uses roles and accessible names
   sidebar.getByRole("button", { name: "Send" })
   
   // Avoid - brittle CSS selectors
   sidebar.locator(".chat-input-class")
   ```

2. **Wait for elements:**
   ```typescript
   await expect(sidebar.getByText("Loading...")).toBeVisible()
   await expect(sidebar.getByText("Complete")).toBeVisible()
   ```

3. **Clean up state:**
   ```typescript
   // Use helper functions for common cleanup
   await cleanChatView(page)
   ```

4. **Handle async operations:**
   ```typescript
   // Wait for API responses
   await expect(sidebar.getByText("API Request...")).toBeVisible()
   await expect(sidebar.getByText("Response received")).toBeVisible()
   ```

5. **Test both success and error cases:**
   ```typescript
   // Test successful flow
   await helper.signin(sidebar)
   
   // Test error handling
   await expect(sidebar.getByText("API Request Failed")).toBeVisible()
   ```

### Debugging Tips

- Use `page.pause()` to pause execution and inspect the current state
- Add `console.log()` statements to track test progress
- Use `--headed` flag to see the browser window during test execution
- Check video recordings in `test-results/` for failed tests
- Use browser developer tools to inspect element selectors

### Environment Variables

- `CLINE_E2E_TESTS_VERBOSE=true` - Enable verbose logging
- `CI=true` - Adjusts timeouts and reporting for CI environments
- `GRPC_RECORDER_ENABLED=true` - Enable gRPC recording for debugging



---

# FILE: src/test/e2e/fixtures/workspace/.vscode/settings.json

{
	"workbench.secondarySideBar.defaultVisibility": "hidden"
}



---

# FILE: src/test/e2e/fixtures/workspace/README.md

# Test Workspace

This workspace is used for testing the extension in a controlled environment.


---

# FILE: src/test/e2e/fixtures/workspace_2/README.md

# Test Workspace 2

This workspace is used for testing the extension in a controlled environment.


---

# FILE: tests/specs/grpc_recorded_session_single_root.json

{
	"startTime": "2025-09-22T15:10:39.693Z",
	"entries": [
		{
			"requestId": "6e4460e9-e701-4bd2-bac6-1b0f20938c11",
			"service": "cline.AccountService",
			"method": "accountLoginClicked",
			"isStreaming": false,
			"request": {
				"message": {}
			},
			"status": "completed",
			"meta": {
				"synthetic": false
			},
			"response": {
				"message": {
					"value": "http://localhost:7777/"
				}
			},
			"duration": 13
		},
		{
			"requestId": "2f774918-949e-4919-9b26-8b8be5b95bb9",
			"service": "cline.AccountService",
			"method": "getUserOrganizations",
			"isStreaming": false,
			"request": {
				"message": {}
			},
			"status": "completed",
			"meta": {
				"synthetic": false
			},
			"response": {
				"message": {
					"organizations": [
						{
							"active": false,
							"memberId": "random-member-id",
							"name": "Test Organization",
							"organizationId": "random-org-id",
							"roles": [
								"member"
							]
						}
					]
				}
			},
			"duration": 5
		},
		{
			"requestId": "118991fc-73b1-4dce-ae20-15cd3529f465",
			"service": "cline.TaskService",
			"method": "newTask",
			"isStreaming": false,
			"request": {
				"message": {
					"text": "Hello, Cline!",
					"images": [],
					"files": []
				}
			},
			"status": "completed",
			"meta": {
				"synthetic": false,
				"expected": {}
			},
			"response": {
				"message": {
					"value": "1768819891184"
				}
			},
			"duration": 49
		},
		{
			"requestId": "6633a706-366d-49d5-a3f4-4589131bdc5c",
			"service": "cline.StateService",
			"method": "getLatestState",
			"isStreaming": false,
			"request": {
				"message": {}
			},
			"status": "completed",
			"meta": {
				"expected": {
					"stateJson": {
						"taskHistory": [
							{
								"task": "Hello, Cline!"
							}
						]
					}
				}
			},
			"response": {
				"message": {
					"stateJson": "THIS_WILL_BE_IGNORED_EXPECTED_HAS_BEEN_SET"
				}
			},
			"duration": 0
		}
	]
}



---

# FILE: webview-ui/src/components/mcp/RICH_MCP_TESTING.md

# How To Test Rich MCP Responses

Use the `echo` MCP server to read back one of the test cases below into an MCP response.
https://github.com/Garoth/echo-mcp

Manually check the embeds, images, and whatever other enhancements for proper rendering.
Remember that toggling Rich MCP off should cancel pending fetches. If the toggle was
set to Plain, then the image/link previews should never be fetched until it's enabled.
Remember that rich display mode will only load the first n URLs, currently set to 50

## Main Test Case

Working Image URLs

jpg: https://yavuzceliker.github.io/sample-images/image-205.jpg
webp: https://seenandheard.app/assets/img/face-2.webp
svg: https://seenandheard.app/assets/img/logo-white.svg

Looks like Image URL but is website

site: https://github.com/google/pprof/blob/main/doc/images/webui/flame-multi.png
raw png: https://raw.githubusercontent.com/google/pprof/refs/heads/main/doc/images/webui/flame-multi.png

Gif:

https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/01_Das_Sandberg-Modell.gif/750px-01_Das_Sandberg-Modell.gif

Normal Working URLs for OG Embeds

https://www.google.com
https://www.blogger.com
https://youtube.com
https://linkedin.com
https://support.google.com
https://cloudflare.com
https://microsoft.com
https://apple.com
https://en.wikipedia.org
https://play.google.com
https://wordpress.org

Attack URLs & Unsupported Formats

data:text/html,<h1>Hello World</h1>
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==
javascript:alert('XSS')
mailto:user@example.com
tel:+1-234-567-8901
sms:+1-234-567-8901?body=Hello
https://www.example.com/path/to/file.html?param=<script>alert('XSS')</script>
https://www.example.com/path/to/file.html?param=<img src="x" onerror="alert('XSS')">
https://www.example.com/path/to/file.html?param=javascript:alert('XSS')
https://www.example.com/path/to/file.html?param=data:text/html,<script>alert('XSS')</script>
https://www.example.com/path/to/file.html?param=data:image/svg+xml,<svg onload="alert('XSS')">
https://www.example.com/path/to/file.html?param=<iframe src="javascript:alert('XSS')">
https://www.example.com/path/to/file.html?param=<a href="javascript:alert('XSS')">Click me</a>

Broken & Weird Edge Cases

https://tectum.io/blog/dex-tools/
http://0.0.0.0:8025/img.png
https://localhost:8080/img.jpg
http://localhost:8080/
https://localhost/
http://httpbin.org/#/ 
https://snthonstcrgrfonhenth.com/nthshtf
http://domain/.well-known/acme-challenge/token
https://<strong>dextools</strong>.apiable.io/(Only

## Generated Links Test Case

1. https://www.google.com
2. http://example.com/path/to/resource?query=value#fragment
3. https://images.unsplash.com/photo-1575936123452-b67c3203c357
4. file:///home/user/document.txt
5. https://user:password@example.com:8080/path
6. http://192.168.1.1:8080
7. https://www.example.com/path with spaces/file.html
8. ftp://ftp.example.com/pub/file.zip
9. https://www.example.com/index.php?id=1&name=test
10. https://subdomain.example.co.uk/path
11. https://www.example.com/path/to/image.jpg
12. https://www.example.com:8443/secure
13. http://localhost:3000
14. https://www.example.com/path/to/file.pdf#page=10
15. https://www.example.com/search?q=query+with+spaces
16. https://www.example.com/path/to/file.html#section-2
17. https://www.example.com/path/to/file.php?id=123&action=view
18. https://www.example.com/path/to/file.html?param1=value1&param2=value2#fragment
19. https://www.example.com/path/to/file.html?param=value with spaces
20. https://www.example.com/path/to/file.html?param=value%20with%20encoded%20spaces
21. https://www.example.com/path/to/file.html?param=value+with+plus+signs
22. https://www.example.com/path/to/file.html?param=special@characters!
23. https://www.example.com/path/to/file.html?param=special%40characters%21
24. https://www.example.com/path/to/file.html?param=value&param=duplicate
25. https://www.example.com/path/to/file.html?param=
26. https://www.example.com/path/to/file.html?=value
27. https://www.example.com/path/to/file.html?
28. https://www.example.com/path/to/file.html#
29. https://www.example.com/path/to/file.html#fragment1#fragment2
30. https://www.example.com/path/to/file.html?param1=value1#fragment?param2=value2
31. https://www.example.com/index.html#!hashbang
32. https://www.example.com/path/to/file.html?param=value#fragment=value
33. https://www.example.com/path/to/file.html?param=value&param2=value2#fragment
34. https://www.example.com/path/to/file.html?param=value&param2=value2#fragment=value
35. https://www.example.com/path/to/file.html?param=value&param2=value2#fragment?param3=value3
36. https://www.example.com/path/to/file.html?param=value&param2=value2#fragment&param3=value3
37. https://www.example.com/path/to/file.html?param=value&param2=value2#fragment#fragment2
38. https://www.example.com/path/to/file.html?param=value&param2=value2#fragment/path
39. https://www.example.com/path/to/file.html?param=value&param2=value2#fragment?param3=value3&param4=value4
40. https://www.example.com/path/to/file.html?param=value&param2=value2#fragment&param3=value3&param4=value4
41. data:text/html,<h1>Hello World</h1>
42. data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==
43. javascript:alert('XSS')
44. mailto:user@example.com
45. tel:+1-234-567-8901
46. sms:+1-234-567-8901?body=Hello
47. https://www.example.com/path/to/file.html?param=<script>alert('XSS')</script>
48. https://www.example.com/path/to/file.html?param=<img src="x" onerror="alert('XSS')">
49. https://www.example.com/path/to/file.html?param=javascript:alert('XSS')
50. https://www.example.com/path/to/file.html?param=data:text/html,<script>alert('XSS')</script>
51. https://www.example.com/path/to/file.html?param=data:image/svg+xml,<svg onload="alert('XSS')">
52. https://www.example.com/path/to/file.html?param=<iframe src="javascript:alert('XSS')">
53. https://www.example.com/path/to/file.html?param=<a href="javascript:alert('XSS')">Click me</a>
54. https://www.example.com/path/to/file.html?param=<img src="x" onerror="alert('XSS')">
55. https://www.example.com/path/to/file.html?param=<svg><script>alert('XSS')</script></svg>
56. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
57. https://www.example.com/path/to/file.html?param=<img src="x" onerror="alert('XSS')">
58. https://www.example.com/path/to/file.html?param=<body onload="alert('XSS')">
59. https://www.example.com/path/to/file.html?param=<input autofocus onfocus="alert('XSS')">
60. https://www.example.com/path/to/file.html?param=<video src="x" onerror="alert('XSS')">
61. https://www.example.com/path/to/file.html?param=<audio src="x" onerror="alert('XSS')">
62. https://www.example.com/path/to/file.html?param=<iframe srcdoc="<script>alert('XSS')</script>">
63. https://www.example.com/path/to/file.html?param=<math><maction actiontype="statusline#" xlink:href="javascript:alert('XSS')">Click
64. https://www.example.com/path/to/file.html?param=<form action="javascript:alert('XSS')"><input type="submit">
65. https://www.example.com/path/to/file.html?param=<isindex action="javascript:alert('XSS')" type="image">
66. https://www.example.com/path/to/file.html?param=<object data="javascript:alert('XSS')">
67. https://www.example.com/path/to/file.html?param=<embed src="javascript:alert('XSS')">
68. https://www.example.com/path/to/file.html?param=<svg><script>alert('XSS')</script>
69. https://www.example.com/path/to/file.html?param=<marquee onstart="alert('XSS')">
70. https://www.example.com/path/to/file.html?param=<div style="background-image: url(javascript:alert('XSS'))">
71. https://www.example.com/path/to/file.html?param=<link rel="stylesheet" href="javascript:alert('XSS')">
72. https://www.example.com/path/to/file.html?param=<table background="javascript:alert('XSS')">
73. https://www.example.com/path/to/file.html?param=<div style="width: expression(alert('XSS'))">
74. https://www.example.com/path/to/file.html?param=<style>@import "javascript:alert('XSS')";</style>
75. https://www.example.com/path/to/file.html?param=<meta http-equiv="refresh" content="0;url=javascript:alert('XSS')">
76. https://www.example.com/path/to/file.html?param=<iframe src="data:text/html,<script>alert('XSS')</script>">
77. https://www.example.com/path/to/file.html?param=<svg><set attributeName="onload" to="alert('XSS')" />
78. https://www.example.com/path/to/file.html?param=<script>alert('XSS')</script>
79. https://www.example.com/path/to/file.html?param=<img src="x" onerror="alert('XSS')">
80. https://www.example.com/path/to/file.html?param=<svg><animate xlink:href="#xss" attributeName="href" values="javascript:alert('XSS')" />
81. https://www.example.com/path/to/file.html?param=<svg><a><animate attributeName="href" values="javascript:alert('XSS')" />
82. https://www.example.com/path/to/file.html?param=<svg><a xlink:href="javascript:alert('XSS')"><text x="20" y="20">XSS</text></a>
83. https://www.example.com/path/to/file.html?param=<svg><a><animate attributeName="href" values="javascript:alert('XSS')" /><text x="20" y="20">XSS</text></a>
84. https://www.example.com/path/to/file.html?param=<svg><discard onbegin="alert('XSS')" />
85. https://www.example.com/path/to/file.html?param=<svg><script>alert('XSS')</script></svg>
86. https://www.example.com/path/to/file.html?param=<svg><script>alert('XSS')</script>
87. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
88. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
89. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
90. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
91. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
92. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
93. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
94. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
95. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
96. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
97. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
98. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
99. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
100. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
101. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
102. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
103. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
104. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
105. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
106. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
107. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />
108. https://www.example.com/path/to/file.html?param=<svg><animate onbegin="alert('XSS')" attributeName="x" />


## Popular URLs by Popularity Test Case

1. https://www.google.com
2. https://www.blogger.com
3. https://youtube.com
4. https://linkedin.com
5. https://support.google.com
6. https://cloudflare.com
7. https://microsoft.com
8. https://apple.com
9. https://en.wikipedia.org
10. https://play.google.com
11. https://wordpress.org
12. https://docs.google.com
13. https://mozilla.org
14. https://maps.google.com
15. https://youtu.be
16. https://drive.google.com
17. https://bp.blogspot.com
18. https://sites.google.com
19. https://googleusercontent.com
20. https://accounts.google.com
21. https://t.me
22. https://europa.eu
23. https://plus.google.com
24. https://whatsapp.com
25. https://adobe.com
26. https://facebook.com
27. https://policies.google.com
28. https://uol.com.br
29. https://istockphoto.com
30. https://vimeo.com
31. https://vk.com
32. https://github.com
33. https://amazon.com
34. https://search.google.com
35. https://bbc.co.uk
36. https://google.de
37. https://live.com
38. https://gravatar.com
39. https://nih.gov
40. https://dan.com
41. https://files.wordpress.com
42. https://www.yahoo.com
43. https://cnn.com
44. https://dropbox.com
45. https://wikimedia.org
46. https://creativecommons.org
47. https://google.com.br
48. https://line.me
49. https://googleblog.com
50. https://opera.com
51. https://es.wikipedia.org
52. https://globo.com
53. https://brandbucket.com
54. https://myspace.com
55. https://slideshare.net
56. https://paypal.com
57. https://tiktok.com
58. https://netvibes.com
59. https://theguardian.com
60. https://who.int
61. https://goo.gl
62. https://medium.com
63. https://tools.google.com
64. https://draft.blogger.com
65. https://pt.wikipedia.org
66. https://fr.wikipedia.org
67. https://www.weebly.com
68. https://news.google.com
69. https://developers.google.com
70. https://w3.org
71. https://mail.google.com
72. https://gstatic.com
73. https://jimdofree.com
74. https://cpanel.net
75. https://imdb.com
76. https://wa.me
77. https://feedburner.com
78. https://enable-javascript.com
79. https://nytimes.com
80. https://workspace.google.com
81. https://ok.ru
82. https://google.es
83. https://dailymotion.com
84. https://afternic.com
85. https://bloomberg.com
86. https://amazon.de
87. https://photos.google.com
88. https://wiley.com
89. https://aliexpress.com
90. https://indiatimes.com
91. https://youronlinechoices.com
92. https://elpais.com
93. https://tinyurl.com
94. https://yadi.sk
95. https://spotify.com
96. https://huffpost.com
97. https://ru.wikipedia.org
98. https://google.fr
99. https://webmd.com
100. https://samsung.com
101. https://independent.co.uk
102. https://amazon.co.jp
103. https://get.google.com
104. https://amazon.co.uk
105. https://4shared.com
106. https://telegram.me
107. https://planalto.gov.br
108. https://businessinsider.com
109. https://ig.com.br
110. https://issuu.com
111. https://www.gov.br
112. https://wsj.com
113. https://hugedomains.com
114. https://picasaweb.google.com
115. https://usatoday.com
116. https://scribd.com
117. https://www.gov.uk
118. https://storage.googleapis.com
119. https://huffingtonpost.com
120. https://bbc.com
121. https://estadao.com.br
122. https://nature.com
123. https://mediafire.com
124. https://washingtonpost.com
125. https://forms.gle
126. https://namecheap.com
127. https://forbes.com
128. https://mirror.co.uk
129. https://soundcloud.com
130. https://fb.com
131. https://marketingplatform.google
132. https://domainmarket.com
133. https://ytimg.com
134. https://terra.com.br
135. https://google.co.uk
136. https://shutterstock.com
137. https://dailymail.co.uk
138. https://reg.ru
139. https://t.co
140. https://cdc.gov
141. https://thesun.co.uk
142. https://wp.com
143. https://cnet.com
144. https://instagram.com
145. https://researchgate.net
146. https://google.it
147. https://fandom.com
148. https://office.com
149. https://list-manage.com
150. https://msn.com
151. https://un.org
152. https://de.wikipedia.org
153. https://ovh.com
154. https://mail.ru
155. https://bing.com
156. https://news.yahoo.com
157. https://myaccount.google.com
158. https://hatena.ne.jp
159. https://shopify.com
160. https://adssettings.google.com
161. https://bit.ly
162. https://reuters.com
163. https://booking.com
164. https://discord.com
165. https://buydomains.com
166. https://nasa.gov
167. https://aboutads.info
168. https://time.com
169. https://abril.com.br
170. https://change.org
171. https://nginx.org
172. https://twitter.com
173. https://www.wikipedia.org
174. https://archive.org
175. https://cbsnews.com
176. https://networkadvertising.org
177. https://telegraph.co.uk
178. https://pinterest.com
179. https://google.co.jp
180. https://pixabay.com
181. https://zendesk.com
182. https://cpanel.com
183. https://vistaprint.com
184. https://sky.com
185. https://windows.net
186. https://alicdn.com
187. https://google.ca
188. https://lemonde.fr
189. https://newyorker.com
190. https://webnode.page
191. https://surveymonkey.com
192. https://translate.google.com
193. https://calendar.google.com
194. https://amazonaws.com
195. https://academia.edu
196. https://apache.org
197. https://imageshack.us
198. https://akamaihd.net
199. https://nginx.com
200. https://discord.gg
201. https://thetimes.co.uk
202. https://search.yahoo.com
203. https://amazon.fr
204. https://yelp.com
205. https://berkeley.edu
206. https://google.ru
207. https://sedoparking.com
208. https://cbc.ca
209. https://unesco.org
210. https://ggpht.com
211. https://privacyshield.gov
212. https://www.over-blog.com
213. https://clarin.com
214. https://www.wix.com
215. https://whitehouse.gov
216. https://icann.org
217. https://gnu.org
218. https://yandex.ru
219. https://francetvinfo.fr
220. https://gmail.com
221. https://mozilla.com
222. https://ziddu.com
223. https://guardian.co.uk
224. https://twitch.tv
225. https://sedo.com
226. https://foxnews.com
227. https://rambler.ru
228. https://books.google.com
229. https://stanford.edu
230. https://wikihow.com
231. https://it.wikipedia.org
232. https://20minutos.es
233. https://sfgate.com
234. https://liveinternet.ru
235. https://ja.wikipedia.org
236. https://000webhost.com
237. https://espn.com
238. https://eventbrite.com
239. https://disney.com
240. https://statista.com
241. https://addthis.com
242. https://pinterest.fr
243. https://lavanguardia.com
244. https://vkontakte.ru
245. https://doubleclick.net
246. https://bp2.blogger.com
247. https://skype.com
248. https://sciencedaily.com
249. https://bloglovin.com
250. https://insider.com
251. https://pl.wikipedia.org
252. https://sputniknews.com
253. https://id.wikipedia.org
254. https://doi.org
255. https://nypost.com
256. https://elmundo.es
257. https://abcnews.go.com
258. https://ipv4.google.com
259. https://deezer.com
260. https://express.co.uk
261. https://detik.com
262. https://mystrikingly.com
263. https://rakuten.co.jp
264. https://amzn.to
265. https://arxiv.org
266. https://alibaba.com
267. https://fb.me
268. https://wikia.com
269. https://t-online.de
270. https://telegra.ph
271. https://mega.nz
272. https://usnews.com
273. https://plos.org
274. https://naver.com
275. https://ibm.com
276. https://smh.com.au
277. https://dw.com
278. https://google.nl
279. https://lefigaro.fr
280. https://bp1.blogger.com
281. https://picasa.google.com
282. https://theatlantic.com
283. https://nydailynews.com
284. https://themeforest.net
285. https://rtve.es
286. https://newsweek.com
287. https://ovh.net
288. https://ca.gov
289. https://goodreads.com
290. https://economist.com
291. https://target.com
292. https://marca.com
293. https://kickstarter.com
294. https://hindustantimes.com
295. https://weibo.com
296. https://finance.yahoo.com
297. https://huawei.com
298. https://e-monsite.com
299. https://hubspot.com
300. https://npr.org
301. https://netflix.com
302. https://gizmodo.com
303. https://netlify.app
304. https://yandex.com
305. https://mashable.com
306. https://cnil.fr
307. https://latimes.com
308. https://steampowered.com
309. https://rt.com
310. https://photobucket.com
311. https://quora.com
312. https://nbcnews.com
313. https://android.com
314. https://instructables.com
315. https://www.canalblog.com
316. https://www.livejournal.com
317. https://ouest-france.fr
318. https://tripadvisor.com
319. https://ovhcloud.com
320. https://pexels.com
321. https://oracle.com
322. https://yahoo.co.jp
323. https://addtoany.com
324. https://sakura.ne.jp
325. https://cointernet.com.co
326. https://twimg.com
327. https://britannica.com
328. https://php.net
329. https://standard.co.uk
330. https://groups.google.com
331. https://cnbc.com
332. https://loc.gov
333. https://qq.com
334. https://buzzfeed.com
335. https://godaddy.com
336. https://ikea.com
337. https://disqus.com
338. https://taringa.net
339. https://ea.com
340. https://dropcatch.com
341. https://techcrunch.com
342. https://canva.com
343. https://offset.com
344. https://ebay.com
345. https://zoom.us
346. https://cambridge.org
347. https://unsplash.com
348. https://playstation.com
349. https://people.com
350. https://springer.com
351. https://psychologytoday.com
352. https://sendspace.com
353. https://home.pl
354. https://rapidshare.com
355. https://prezi.com
356. https://photos1.blogger.com
357. https://thenai.org
358. https://ftc.gov
359. https://google.pl
360. https://ted.com
361. https://secureserver.net
362. https://code.google.com
363. https://plesk.com
364. https://aol.com
365. https://biglobe.ne.jp
366. https://hp.com
367. https://canada.ca
368. https://linktr.ee
369. https://hollywoodreporter.com
370. https://ietf.org
371. https://clickbank.net
372. https://harvard.edu
373. https://amazon.es
374. https://oup.com
375. https://timeweb.ru
376. https://engadget.com
377. https://vice.com
378. https://cornell.edu
379. https://dreamstime.com
380. https://tmz.com
381. https://gofundme.com
382. https://pbs.org
383. https://stackoverflow.com
384. https://abc.net.au
385. https://sciencedirect.com
386. https://ft.com
387. https://variety.com
388. https://alexa.com
389. https://abc.es
390. https://walmart.com
391. https://gooyaabitemplates.com
392. https://redbull.com
393. https://ssl-images-amazon.com
394. https://theverge.com
395. https://spiegel.de
396. https://about.com
397. https://nationalgeographic.com
398. https://bandcamp.com
399. https://m.wikipedia.org
400. https://zippyshare.com
401. https://wired.com
402. https://freepik.com
403. https://outlook.com
404. https://mit.edu
405. https://sapo.pt
406. https://goo.ne.jp
407. https://java.com
408. https://google.co.th
409. https://scmp.com
410. https://mayoclinic.org
411. https://scholastic.com
412. https://nba.com
413. https://reverbnation.com
414. https://depositfiles.com
415. https://video.google.com
416. https://howstuffworks.com
417. https://cbslocal.com
418. https://merriam-webster.com
419. https://focus.de
420. https://admin.ch
421. https://gfycat.com
422. https://com.com
423. https://narod.ru
424. https://boston.com
425. https://sony.com
426. https://justjared.com
427. https://bitly.com
428. https://jstor.org
429. https://amebaownd.com
430. https://g.co
431. https://gsmarena.com
432. https://lexpress.fr
433. https://reddit.com
434. https://usgs.gov
435. https://bigcommerce.com
436. https://gettyimages.com
437. https://ign.com
438. https://justgiving.com
439. https://techradar.com
440. https://weather.com
441. https://amazon.ca
442. https://justice.gov
443. https://sciencemag.org
444. https://pcmag.com
445. https://theconversation.com
446. https://foursquare.com
447. https://flickr.com
448. https://giphy.com
449. https://tvtropes.org
450. https://fifa.com
451. https://upenn.edu
452. https://digg.com
453. https://bestfreecams.club
454. https://histats.com
455. https://salesforce.com
456. https://blog.google
457. https://apnews.com
458. https://theglobeandmail.com
459. https://m.me
460. https://europapress.es
461. https://washington.edu
462. https://thefreedictionary.com
463. https://jhu.edu
464. https://euronews.com
465. https://liberation.fr
466. https://ads.google.com
467. https://trustpilot.com
468. https://google.com.tw
469. https://softonic.com
470. https://kakao.com
471. https://storage.canalblog.com
472. https://interia.pl
473. https://metro.co.uk
474. https://viglink.com
475. https://last.fm
476. https://blackberry.com
477. https://public-api.wordpress.com
478. https://sina.com.cn
479. https://unicef.org
480. https://archives.gov
481. https://nps.gov
482. https://utexas.edu
483. https://biblegateway.com
484. https://usda.gov
485. https://indiegogo.com
486. https://nikkei.com
487. https://radiofrance.fr
488. https://repubblica.it
489. https://substack.com
490. https://ap.org
491. https://nicovideo.jp
492. https://joomla.org
493. https://news.com.au
494. https://allaboutcookies.org
495. https://mailchimp.com
496. https://stores.jp
497. https://intel.com
498. https://bp0.blogger.com
499. https://box.com
499. https://nhk.or.jp
