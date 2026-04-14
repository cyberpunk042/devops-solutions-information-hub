# tirth8205/code-review-graph

Source: https://github.com/tirth8205/code-review-graph
Ingested: 2026-04-14
Type: documentation

---

# README

<h1 align="center">code-review-graph</h1>

<p align="center">
  <strong>Stop burning tokens. Start reviewing smarter.</strong>
</p>

<p align="center">
  <a href="https://code-review-graph.com"><img src="https://img.shields.io/badge/website-code--review--graph.com-blue?style=flat-square" alt="Website"></a>
  <a href="https://discord.gg/3p58KXqGFN"><img src="https://img.shields.io/badge/discord-join-5865F2?style=flat-square&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://github.com/tirth8205/code-review-graph/stargazers"><img src="https://img.shields.io/github/stars/tirth8205/code-review-graph?style=flat-square" alt="Stars"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="MIT Licence"></a>
  <a href="https://github.com/tirth8205/code-review-graph/actions/workflows/ci.yml"><img src="https://github.com/tirth8205/code-review-graph/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10%2B-blue.svg?style=flat-square" alt="Python 3.10+"></a>
  <a href="https://modelcontextprotocol.io/"><img src="https://img.shields.io/badge/MCP-compatible-green.svg?style=flat-square" alt="MCP"></a>
  <a href="#"><img src="https://img.shields.io/badge/version-2.1.0-purple.svg?style=flat-square" alt="v2.1.0"></a>
</p>

<br>

AI coding tools re-read your entire codebase on every task. `code-review-graph` fixes that. It builds a structural map of your code with [Tree-sitter](https://tree-sitter.github.io/tree-sitter/), tracks changes incrementally, and gives your AI assistant precise context via [MCP](https://modelcontextprotocol.io/) so it reads only what matters.

<p align="center">
  <img src="diagrams/diagram1_before_vs_after.png" alt="The Token Problem: 8.2x average token reduction across 6 real repositories" width="85%" />
</p>

---

## Quick Start

```bash
pip install code-review-graph                     # or: pipx install code-review-graph
code-review-graph install          # auto-detects and configures all supported platforms
code-review-graph build            # parse your codebase
```

One command sets up everything. `install` detects which AI coding tools you have, writes the correct MCP configuration for each one, and injects graph-aware instructions into your platform rules. It auto-detects whether you installed via `uvx` or `pip`/`pipx` and generates the right config. Restart your editor/tool after installing.

<p align="center">
  <img src="diagrams/diagram8_supported_platforms.png" alt="One Install, Every Platform: auto-detects Codex, Claude Code, Cursor, Windsurf, Zed, Continue, OpenCode, Antigravity, and Kiro" width="85%" />
</p>

To target a specific platform:

```bash
code-review-graph install --platform codex       # configure only Codex
code-review-graph install --platform cursor      # configure only Cursor
code-review-graph install --platform claude-code  # configure only Claude Code
code-review-graph install --platform kiro         # configure only Kiro
```

Requires Python 3.10+. For the best experience, install [uv](https://docs.astral.sh/uv/) (the MCP config will use `uvx` if available, otherwise falls back to the `code-review-graph` command directly).

Then open your project and ask your AI assistant:

```
Build the code review graph for this project
```

The initial build takes ~10 seconds for a 500-file project. After that, the graph updates automatically on every file edit and git commit.

---

## How It Works

<p align="center">
  <img src="diagrams/diagram7_mcp_integration_flow.png" alt="How your AI assistant uses the graph: User asks for review, AI checks MCP tools, graph returns blast radius and risk scores, AI reads only what matters" width="80%" />
</p>

Your repository is parsed into an AST with Tree-sitter, stored as a graph of nodes (functions, classes, imports) and edges (calls, inheritance, test coverage), then queried at review time to compute the minimal set of files your AI assistant needs to read.

<p align="center">
  <img src="diagrams/diagram2_architecture_pipeline.png" alt="Architecture pipeline: Repository to Tree-sitter Parser to SQLite Graph to Blast Radius to Minimal Review Set" width="100%" />
</p>

### Blast-radius analysis

When a file changes, the graph traces every caller, dependent, and test that could be affected. This is the "blast radius" of the change. Your AI reads only these files instead of scanning the whole project.

<p align="center">
  <img src="diagrams/diagram3_blast_radius.png" alt="Blast radius visualization showing how a change to login() propagates to callers, dependents, and tests" width="70%" />
</p>

### Incremental updates in < 2 seconds

On every git commit or file save, a hook fires. The graph diffs changed files, finds their dependents via SHA-256 hash checks, and re-parses only what changed. A 2,900-file project re-indexes in under 2 seconds.

<p align="center">
  <img src="diagrams/diagram4_incremental_update.png" alt="Incremental update flow: git commit triggers diff, finds dependents, re-parses only 5 files while 2,910 are skipped" width="90%" />
</p>

### The monorepo problem, solved

Large monorepos are where token waste is most painful. The graph cuts through the noise — 27,700+ files excluded from review context, only ~15 files actually read.

<p align="center">
  <img src="diagrams/diagram6_monorepo_funnel.png" alt="Next.js monorepo: 27,732 files funnelled through code-review-graph down to ~15 files — 49x fewer tokens" width="80%" />
</p>

### 19 languages + Jupyter notebooks

<p align="center">
  <img src="diagrams/diagram9_language_coverage.png" alt="19 languages organized by category: Web, Backend, Systems, Mobile, Scripting, plus Jupyter/Databricks notebook support" width="90%" />
</p>

Full Tree-sitter grammar support for functions, classes, imports, call sites, inheritance, and test detection in every language. Plus Jupyter/Databricks notebook parsing (`.ipynb`) with multi-language cell support (Python, R, SQL), and Perl XS files (`.xs`).

---

## Benchmarks

<p align="center">
  <img src="diagrams/diagram5_benchmark_board.png" alt="Benchmarks across real repos: 4.9x to 27.3x fewer tokens, higher review quality" width="85%" />
</p>

All numbers come from the automated evaluation runner against 6 real open-source repositories (13 commits total). Reproduce with `code-review-graph eval --all`. Raw data in [`evaluate/reports/summary.md`](evaluate/reports/summary.md).

<details>
<summary><strong>Token efficiency: 8.2x average reduction (naive vs graph)</strong></summary>
<br>

The graph replaces reading entire source files with a compact structural context covering blast radius, dependency chains, and test coverage gaps.

| Repo | Commits | Avg Naive Tokens | Avg Graph Tokens | Reduction |
|------|--------:|-----------------:|----------------:|----------:|
| express | 2 | 693 | 983 | 0.7x |
| fastapi | 2 | 4,944 | 614 | 8.1x |
| flask | 2 | 44,751 | 4,252 | 9.1x |
| gin | 3 | 21,972 | 1,153 | 16.4x |
| httpx | 2 | 12,044 | 1,728 | 6.9x |
| nextjs | 2 | 9,882 | 1,249 | 8.0x |
| **Average** | **13** | | | **8.2x** |

**Why express shows <1x:** For single-file changes in small packages, the graph context (metadata, edges, review guidance) can exceed the raw file size. The graph approach pays off on multi-file changes where it prunes irrelevant code.

</details>

<details>
<summary><strong>Impact accuracy: 100% recall, 0.54 average F1</strong></summary>
<br>

The blast-radius analysis never misses an actually impacted file (perfect recall). It over-predicts in some cases, which is a conservative trade-off — better to flag too many files than miss a broken dependency.

| Repo | Commits | Avg F1 | Avg Precision | Recall |
|------|--------:|-------:|--------------:|-------:|
| express | 2 | 0.667 | 0.50 | 1.0 |
| fastapi | 2 | 0.584 | 0.42 | 1.0 |
| flask | 2 | 0.475 | 0.34 | 1.0 |
| gin | 3 | 0.429 | 0.29 | 1.0 |
| httpx | 2 | 0.762 | 0.63 | 1.0 |
| nextjs | 2 | 0.331 | 0.20 | 1.0 |
| **Average** | **13** | **0.54** | **0.38** | **1.0** |

</details>

<details>
<summary><strong>Build performance</strong></summary>
<br>

| Repo | Files | Nodes | Edges | Flow Detection | Search Latency |
|------|------:|------:|------:|---------------:|---------------:|
| express | 141 | 1,910 | 17,553 | 106ms | 0.7ms |
| fastapi | 1,122 | 6,285 | 27,117 | 128ms | 1.5ms |
| flask | 83 | 1,446 | 7,974 | 95ms | 0.7ms |
| gin | 99 | 1,286 | 16,762 | 111ms | 0.5ms |
| httpx | 60 | 1,253 | 7,896 | 96ms | 0.4ms |

</details>

<details>
<summary><strong>Limitations and known weaknesses</strong></summary>
<br>

- **Small single-file changes:** Graph context can exceed naive file reads for trivial edits (see express results above). The overhead is the structural metadata that enables multi-file analysis.
- **Search quality (MRR 0.35):** Keyword search finds the right result in the top-4 for most queries, but ranking needs improvement. Express queries return 0 hits due to module-pattern naming.
- **Flow detection (33% recall):** Only reliably detects entry points in Python repos (fastapi, httpx) where framework patterns are recognized. JavaScript and Go flow detection needs work.
- **Precision vs recall trade-off:** Impact analysis is deliberately conservative. It flags files that *might* be affected, which means some false positives in large dependency graphs.

</details>

---

## Features

| Feature | Details |
|---------|---------|
| **Incremental updates** | Re-parses only changed files. Subsequent updates complete in under 2 seconds. |
| **19 languages + notebooks** | Python, TypeScript/TSX, JavaScript, Vue, Go, Rust, Java, Scala, C#, Ruby, Kotlin, Swift, PHP, Solidity, C/C++, Dart, R, Perl, Lua, Jupyter/Databricks (.ipynb) |
| **Blast-radius analysis** | Shows exactly which functions, classes, and files are affected by any change |
| **Auto-update hooks** | Graph updates on every file edit and git commit without manual intervention |
| **Semantic search** | Optional vector embeddings via sentence-transformers, Google Gemini, or MiniMax |
| **Interactive visualisation** | D3.js force-directed graph with edge-type toggles and search |
| **Local storage** | SQLite file in `.code-review-graph/`. No external database, no cloud dependency. |
| **Watch mode** | Continuous graph updates as you work |
| **Execution flows** | Trace call chains from entry points, sorted by criticality |
| **Community detection** | Cluster related code via Leiden algorithm or file grouping |
| **Architecture overview** | Auto-generated architecture map with coupling warnings |
| **Risk-scored reviews** | `detect_changes` maps diffs to affected functions, flows, and test gaps |
| **Refactoring tools** | Rename preview, dead code detection, community-driven suggestions |
| **Wiki generation** | Auto-generate markdown wiki from community structure |
| **Multi-repo registry** | Register multiple repos, search across all of them |
| **MCP prompts** | 5 workflow templates: review, architecture, debug, onboard, pre-merge |
| **Full-text search** | FTS5-powered hybrid search combining keyword and vector similarity |

---

## Usage

<details>
<summary><strong>Slash commands</strong></summary>
<br>

| Command | Description |
|---------|-------------|
| `/code-review-graph:build-graph` | Build or rebuild the code graph |
| `/code-review-graph:review-delta` | Review changes since last commit |
| `/code-review-graph:review-pr` | Full PR review with blast-radius analysis |

</details>

<details>
<summary><strong>CLI reference</strong></summary>
<br>

```bash
code-review-graph install          # Auto-detect and configure all platforms
code-review-graph install --platform <name>  # Target a specific platform
code-review-graph build            # Parse entire codebase
code-review-graph update           # Incremental update (changed files only)
code-review-graph status           # Graph statistics
code-review-graph watch            # Auto-update on file changes
code-review-graph visualize        # Generate interactive HTML graph
code-review-graph wiki             # Generate markdown wiki from communities
code-review-graph detect-changes   # Risk-scored change impact analysis
code-review-graph register <path>  # Register repo in multi-repo registry
code-review-graph unregister <id>  # Remove repo from registry
code-review-graph repos            # List registered repositories
code-review-graph eval             # Run evaluation benchmarks
code-review-graph serve            # Start MCP server
```

</details>

<details>
<summary><strong>22 MCP tools</strong></summary>
<br>

Your AI assistant uses these automatically once the graph is built.

| Tool | Description |
|------|-------------|
| `build_or_update_graph_tool` | Build or incrementally update the graph |
| `get_impact_radius_tool` | Blast radius of changed files |
| `get_review_context_tool` | Token-optimised review context with structural summary |
| `query_graph_tool` | Callers, callees, tests, imports, inheritance queries |
| `semantic_search_nodes_tool` | Search code entities by name or meaning |
| `embed_graph_tool` | Compute vector embeddings for semantic search |
| `list_graph_stats_tool` | Graph size and health |
| `get_docs_section_tool` | Retrieve documentation sections |
| `find_large_functions_tool` | Find functions/classes exceeding a line-count threshold |
| `list_flows_tool` | List execution flows sorted by criticality |
| `get_flow_tool` | Get details of a single execution flow |
| `get_affected_flows_tool` | Find flows affected by changed files |
| `list_communities_tool` | List detected code communities |
| `get_community_tool` | Get details of a single community |
| `get_architecture_overview_tool` | Architecture overview from community structure |
| `detect_changes_tool` | Risk-scored change impact analysis for code review |
| `refactor_tool` | Rename preview, dead code detection, suggestions |
| `apply_refactor_tool` | Apply a previously previewed refactoring |
| `generate_wiki_tool` | Generate markdown wiki from communities |
| `get_wiki_page_tool` | Retrieve a specific wiki page |
| `list_repos_tool` | List registered repositories |
| `cross_repo_search_tool` | Search across all registered repositories |

**MCP Prompts** (5 workflow templates):
`review_changes`, `architecture_map`, `debug_issue`, `onboard_developer`, `pre_merge_check`

</details>

<details>
<summary><strong>Configuration</strong></summary>
<br>

To exclude paths from indexing, create a `.code-review-graphignore` file in your repository root:

```
generated/**
*.generated.ts
vendor/**
node_modules/**
```

Note: in git repos, only tracked files are indexed (`git ls-files`), so gitignored files are skipped automatically. Use `.code-review-graphignore` to exclude tracked files or when git isn't available.

Optional dependency groups:

```bash
pip install code-review-graph[embeddings]          # Local vector embeddings (sentence-transformers)
pip install code-review-graph[google-embeddings]   # Google Gemini embeddings
pip install code-review-graph[communities]         # Community detection (igraph)
pip install code-review-graph[eval]                # Evaluation benchmarks (matplotlib)
pip install code-review-graph[wiki]                # Wiki generation with LLM summaries (ollama)
pip install code-review-graph[all]                 # All optional dependencies
```

</details>

---

## Contributing

```bash
git clone https://github.com/tirth8205/code-review-graph.git
cd code-review-graph
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

<details>
<summary><strong>Adding a new language</strong></summary>
<br>

Edit `code_review_graph/parser.py` and add your extension to `EXTENSION_TO_LANGUAGE` along with node type mappings in `_CLASS_TYPES`, `_FUNCTION_TYPES`, `_IMPORT_TYPES`, and `_CALL_TYPES`. Include a test fixture and open a PR.

</details>

## Licence

MIT. See [LICENSE](LICENSE).

<p align="center">
<br>
<a href="https://code-review-graph.com">code-review-graph.com</a><br><br>
<code>pip install code-review-graph && code-review-graph install</code><br>
<sub>Works with Codex, Claude Code, Cursor, Windsurf, Zed, Continue, OpenCode, Antigravity, and Kiro</sub>
</p>



> **Deep fetch: 17 key files fetched beyond README.**



---

# FILE: CHANGELOG.md

# Changelog

## [Unreleased]

## [2.3.1] - 2026-04-11

Hotfix for the Windows long-running-MCP-tool hang that v2.2.4 only partially fixed.

### Fixed
- **Windows MCP hang on long-running tools** (PR #231, fixes #46, #136): follow-up to v2.2.4. [@dev-limucc reported on #136](https://github.com/tirth8205/code-review-graph/issues/136) that the `WindowsSelectorEventLoopPolicy` fix from v2.2.4 was necessary but not sufficient — read-only tools worked, but `build_or_update_graph_tool(full_rebuild=True)` and `embed_graph_tool` still hung indefinitely on Windows 11 / Python 3.14. Root cause: FastMCP 2.x dispatches sync handlers inline on the only event-loop thread, so handlers that run for more than a few seconds (especially those that spawn subprocesses or do CPU-bound inference) stop the loop from pumping stdin/stdout. **Fix**: converted the five heavy tools (`build_or_update_graph_tool`, `run_postprocess_tool`, `embed_graph_tool`, `detect_changes_tool`, `generate_wiki_tool`) to `async def` and offloaded the blocking work via `asyncio.to_thread`. The other 19 tools are fast SQLite-read paths and stay sync. Zero config, works on every platform. New regression tests assert the five tools are registered as coroutines AND that each one's source literally contains `asyncio.to_thread` as a defense-in-depth lock-in.

## [2.3.0] - 2026-04-11

Additive feature release — new language parsers, new platform install target, MCP tool UX improvements, and out-of-tree graph storage. No breaking changes from v2.2.4.

### Added

- **Elixir parser** (PR #228, closes #112): `.ex` and `.exs` files now produce modules as Class nodes, `def`/`defp`/`defmacro`/`defmacrop` as Function/Test nodes attached to their enclosing module, `alias`/`import`/`require`/`use` as `IMPORTS_FROM` edges, and everything else as `CALLS` edges. Internal call resolution walks into `do_block` bodies so `MathHelpers.double` correctly resolves its call to `Calculator.compute`.
- **Objective-C parser** (PR #227, closes #88): `.m` files parse classes (`@interface`, `@implementation`, `@protocol`), instance and class methods, `[receiver message:args]` message expressions, C-style `main()`, and `#import`/`#include`. Multi-part selectors like `add:to:` keep `add` as the canonical method name.
- **Bash/Shell parser** (PR #227, closes #197): `.sh`, `.bash`, and `.zsh` files parse functions, `command` invocations as `CALLS`, and `source path` / `. path` as `IMPORTS_FROM` edges with path resolution when the target file exists.
- **Qwen Code as a supported MCP install platform** (PR #227, closes #83): `code-review-graph install --platform qwen` writes a merged `~/.qwen/settings.json` using the same `mcpServers` schema as Cursor/Windsurf — it does not clobber existing Qwen config.
- **`apply_refactor_tool` dry-run mode** (PR #228, closes #176): new `dry_run: bool = False` parameter on the MCP tool and underlying `apply_refactor()` function. When true, returns a unified diff per file without touching disk and leaves the `refactor_id` valid for a follow-up real apply. Multi-edit files now apply sequentially against updated content in both modes (fixes a subtle bug where separate edits on the same file could stomp each other).
- **`CRG_DATA_DIR` environment variable** (PR #228, closes #155): when set, replaces the default `<repo>/.code-review-graph` directory verbatim. Useful for ephemeral workspaces, Docker volumes, shared CI caches, and multi-repo orchestrators. Supported by the CLI, MCP tools, and the registry.
- **`CRG_REPO_ROOT` environment variable** (PR #228, closes #155): `find_project_root()` now checks `CRG_REPO_ROOT` before the usual git-root walk — useful for anyone scripting the CLI from a cwd outside the target repo.
- **`install --no-instructions` and `-y`/`--yes` flags** (PR #228, closes #173): new flags on `code-review-graph install` to opt out of the `CLAUDE.md`/`AGENTS.md`/`.cursorrules`/`.windsurfrules` injection entirely (`--no-instructions`) or auto-confirm it without an interactive prompt (`-y`/`--yes`). The CLI also now prints the list of files it will touch before writing, so even without `--dry-run` users see what's coming.
- **Cloud embeddings stderr warning** (PR #228, closes #174): `get_provider()` now prints an explicit warning to stderr before returning a Google Gemini or MiniMax provider, explaining that source code will be sent to an external API. `CRG_ACCEPT_CLOUD_EMBEDDINGS=1` suppresses the warning for scripted workflows. The warning is on stderr only — it never writes to stdout or reads from stdin, so the MCP stdio transport remains uncorrupted.
- **TROUBLESHOOTING quick-reference** (PR #228): new top section in `docs/TROUBLESHOOTING.md` covering the four most common support questions — hook schema errors, `command not found` after pip install, project-vs-user scoping, and "built the graph but Claude Code doesn't see it".

### Fixed

- **Multi-edit refactor correctness** (PR #228): when a single `apply_refactor` call had multiple edits targeting the same file, the previous implementation re-read the file once per edit and could silently stomp earlier changes. The plan-computation step now groups edits by file and applies them sequentially against the updated content; this fix applies to both the real-write and the new dry-run path.

### Changed

- `install` and `init` commands now preview instruction-file targets before writing (no-op if nothing would change). This is always-on and does not require `--dry-run`.
- Default embedding path remains fully local (`sentence-transformers`); no behavior change unless you explicitly opt in to a cloud provider.

### Deprecated

Nothing.

### Security

- The cloud-embedding stderr warning (#174) is a privacy improvement; it does not change the behavior of offline local embeddings, which remain the default.

### Upgrade notes

- Nothing to do beyond `uvx --reinstall code-review-graph` or `pip install -U code-review-graph`. If you're coming from v2.2.2 or earlier, re-run `code-review-graph install` once to pick up the v2.2.3 hook schema rewrite.
- `CRG_DATA_DIR` is optional — if you don't set it, graphs continue to live at `<repo>/.code-review-graph` as before.
- VS Code extension v0.2.2 (from v2.2.4) still needs to be **repackaged and republished** separately; the PyPI `publish.yml` workflow does not cover it.

### Superseded PRs

- PR #204 (install preview, @lngyeen) — reimplemented cleanly in #228 with `isatty()`-guarded confirmation.
- PR #207 (`CRG_DATA_DIR`/`CRG_REPO_ROOT`, @yashmewada9618) — reimplemented cleanly in #228 without `input()`-on-stdio and `mcp._local_only` fragility.
- PR #179 (cloud embeddings warning, @Bakul2006) — reimplemented cleanly in #228 with stderr-only messaging and no stdio reads.

Credit to @lngyeen, @yashmewada9618, and @Bakul2006 for the original designs.

## [2.2.4] - 2026-04-11

Ships the 11 bugs from PR #222 plus the `v2.2.3.1` smoke-test hotfixes, for users upgrading directly from `v2.2.3` or earlier.

### Security
- **fastmcp bumped from 1.0 → ≥2.14.0** (PR #222, fixes #139, #195): closes CVE-2025-62800 (XSS), CVE-2025-62801 (command injection via server_name), CVE-2025-66416 (Confused Deputy). Transitively drops the `docket → fakeredis` chain that was broken by a `FakeConnection` → `FakeRedisConnection` rename in recent fakeredis releases (#195). The FastMCP public API (`FastMCP(name, instructions=...)`, `@mcp.tool()`, `@mcp.prompt()`, `mcp.run(transport="stdio")`) is unchanged across the 1 → 2 bump, so no source changes were needed beyond the pin. All 24 tools verified to register on fastmcp 2.14.6 and round-trip real per-repo data via stdio MCP in a 6-repo smoke test.

### Fixed
- **Windows build/embed hangs** (PR #222, fixes #46, #136): `main()` now sets `WindowsSelectorEventLoopPolicy` before `mcp.run()` on `sys.platform == "win32"`. The default `ProactorEventLoop` on Windows Python 3.8+ deadlocks with `ProcessPoolExecutor` (used by `full_build`) over a stdio MCP transport — producing the silent "Synthesizing…" hangs on `build` and `embed_graph_tool`. This is a no-op on macOS/Linux. **Note**: the fix was applied blind; maintainer could not verify on Windows. Please open a fresh issue if you still see a hang on v2.2.4 Windows with either `sentence-transformers` or Gemini providers.
- **Go method receivers** (PR #222, fixes #190): `func (s *T) Foo()` now attaches `Foo` to `T` as a member (`parent_name="T"`) with the usual `CONTAINS` edge instead of appearing as a top-level function. New `_get_go_receiver_type()` helper walks the method_declaration's first parameter_list to extract the receiver type name.
- **Dart parser — three bugs** (PR #222, fixes #87):
  - Dart `CALLS` edges (`_extract_dart_calls_from_children()`) — tree-sitter-dart doesn't wrap calls in a single `call_expression` node; the pattern is `identifier + selector > argument_part`. New walker handles both direct (`print('x')`) and method-chained (`obj.foo()`) shapes.
  - Dart `package:` URI resolution in `_do_resolve_module()` — `package:<pkgname>/<sub_path>` now walks up to a `pubspec.yaml` whose `name:` declaration matches `<pkgname>` and resolves to `<root>/lib/<sub_path>`.
  - `inheritors_of` bare-vs-qualified name mismatch in `tools/query.py` — falls back to `search_edges_by_target_name(node.name, kind=...)` for `INHERITS`/`IMPLEMENTS` when the qualified-name lookup returns nothing. Affects all languages (INHERITS targets are stored as bare strings for every language), not just Dart.
- **Nested `node_modules` and framework ignore defaults** (PR #222, fixes #91): `_should_ignore()` now treats single-segment `<dir>/**` patterns as "this directory at any depth", so `node_modules/**` also matches `packages/app/node_modules/react/index.js` inside monorepos. Extended `DEFAULT_IGNORE_PATTERNS` with Laravel/Composer (`vendor/**`, `bootstrap/cache/**`, `public/build/**`), Ruby (`.bundle/**`), Gradle (`.gradle/**`, `*.jar`), Flutter/Dart (`.dart_tool/**`, `.pub-cache/**`), and generic `coverage/**`, `.cache/**`. Deliberately did **not** add `packages/**` or `bin/**`/`obj/**` — those are false positives in yarn/pnpm workspace monorepos and .NET source trees respectively.
- **Bare `except Exception` cleanup** (PR #222, fixes #194): Replaced with specific exception classes + `logger.debug(...)` in 11 files (`cli.py`, `graph.py`, `migrations.py`, `parser.py`, `registry.py`, `tools/context.py`, `tsconfig_resolver.py`, `visualization.py`, `wiki.py`, `eval/benchmarks/search_quality.py`). No behavioral change; debuggability improvement.
- **Visualization auto-collapse hiding all edges** (PR #222, fixes #132): `visualization.py` no longer unconditionally auto-collapses every File node on page load. Auto-collapse now only kicks in above 2000 nodes — previously any graph above ~300 nodes would silently hide every CALLS/IMPORTS/INHERITS edge because they connect Functions/Classes nested inside the collapsed Files.
- **`eval` command crashes on `yaml.safe_load`** (PR #222, fixes #212): `eval.runner.load_all_configs()` now calls `_require_yaml()` before reading YAML, so users without `code-review-graph[eval]` installed get `ImportError: pyyaml is required: pip install code-review-graph[eval]` instead of `AttributeError: 'NoneType' object has no attribute 'safe_load'`.

### VS Code extension (0.2.2)
- **`better-sqlite3` bumped 11.x → 12.x** (PR #222, fixes #218): VS Code 1.115 ships Electron 39 / V8 14.2 which removed `v8::Context::GetIsolate()`, the C++ API used by `better-sqlite3@11`. The extension couldn't activate at all — every command was undefined. `better-sqlite3@12.4.1+` (installs 12.8.0) uses the new V8 API and ships Electron 39 prebuilds. `@types/better-sqlite3: ^7.6.8 → ^7.6.13`, plus type-import adjustments in `src/backend/sqlite.ts` for the `Node16` module resolution and the new CJS `export =` types. Extension version bumped to 0.2.2. **Remember to repackage and republish the `.vsix`** — the existing `publish.yml` workflow only covers PyPI.

### Carried forward from 2.2.3.1
- `serve --repo <X>` is now honored by all 24 MCP tools (was only read by `get_docs_section_tool`). See #223.
- Wiki slug collisions no longer silently overwrite pages (~70% data loss on real repos). See #223.

### Upgrade notes
- `uvx --reinstall code-review-graph` or `pip install -U code-review-graph`, then re-run `code-review-graph install` (the 2.2.3 hook-schema rewrite is still a requirement if you're coming from 2.2.2 or earlier).
- VS Code extension needs to be repackaged + republished separately; the Python release does not include it.

## [2.2.3.1] - 2026-04-11

Hotfix on top of 2.2.3 for two bugs surfaced by a full first-time-user smoke test against six real OSS repos (express, fastapi, flask, gin, httpx, next.js).

### Fixed
- **`serve --repo <X>` was ignored by 21 of 24 MCP tools** (PR #223): `main.py` captured the `--repo` CLI flag into `_default_repo_root`, but only `get_docs_section_tool` read it. The other 21 `@mcp.tool()` wrappers all took `repo_root: Optional[str] = None` and passed that straight through to the impl, which fell back to `find_repo_root()` from cwd. The real-world blast radius is small — the `install` command writes `.mcp.json` without a `--repo` flag and Claude Code launches the server with `cwd=<repo>` — but anyone scripting `serve` manually or running a multi-repo orchestrator would silently get the wrong graph. Added a single `_resolve_repo_root()` helper with explicit precedence (client arg > `--repo` flag > `None → cwd`) and threaded it through all 24 wrappers. New unit tests cover the precedence rules.
- **Wiki slug collisions silently overwrote pages** (PR #223): `_slugify()` folds non-alphanumerics to dashes and truncates to 80 chars, so similar community names collided (`"Data Processing"`, `"data processing"`, `"Data  Processing"` all → `data-processing.md`). `generate_wiki()` wrote each community to `<slug>.md` regardless, so later iterations overwrote earlier files while the counter reported them as "updated". On the express smoke test this was **~70% silent data loss** (32 real files vs 107 claimed pages). Fixed by tracking used slugs per-run and appending `-2`, `-3`, … until unique. Every community now gets its own page; the counter matches the physical file count; `get_wiki_page()` still resolves by name via the existing partial-match fallback. New regression test monkey-patches three colliding names and asserts no content loss.

## [2.2.3] - 2026-04-11

### Fixed
- **Claude Code hook schema** (PR #208, fixes #97, #138, #163, #168, #172, #182, #188, #191, #201): `generate_hooks_config()` now emits the valid v1.x+ Claude Code schema — every hook entry has `matcher` + a nested `hooks: [{type, command, timeout}]` array, and timeouts are in seconds. The invalid `PreCommit` event has been removed; pre-commit checks are now installed as a real git hook via `install_git_hook()`. Users upgrading from 2.2.2 must re-run `code-review-graph install` to rewrite `.claude/settings.json`.
- **SQLite transaction nesting** (PR #205, fixes #110, #135, #181): `GraphStore.__init__` now connects with `isolation_level=None`, disabling Python's implicit transactions that were the root cause of `sqlite3.OperationalError: cannot start a transaction within a transaction` on `update`. `store_file_nodes_edges` adds a defensive `in_transaction` flush before `BEGIN IMMEDIATE`.
- **Go method receivers** (PR #166): `_extract_name_from_node` now resolves Go method names from `field_identifier` inside `method_declaration`, fixing method names that were previously picked up as the result type (e.g. `int64`) instead of the method name.
- **UTF-8 decode errors in `detect_changes`** (PR #170, fixes #169): Diff parsing now uses `errors="replace"` so diffs containing binary files no longer crash the tool.
- **`--platform` target scope** (PR #142, fixes #133): `code-review-graph install --platform <target>` now correctly filters skills, hooks, and instruction files so you only get configuration for the requested platform.
- **Large-repo community detection hangs** (PR #213, PR #183): Removed recursive sub-community splitting, capped Leiden at `n_iterations=2`, and batched `store_communities` writes. 100k+ node graphs no longer hang in `_compute_summaries`.
- **CI**: ruff lint + `tomllib` on Python 3.10 (PR #220) — `tests/test_skills.py` now uses a conditional `tomli` backport on 3.10, `N806`/`E501`/`W291` fixes in `skills.py`/`communities.py`/`parser.py`, and the embedded `noqa` reference in `visualization.py` was rephrased so ruff stops parsing it as a directive.
- **Missing dev dependencies** (PR #159): `pytest-cov` added to dev extras, 50 ruff errors swept, one failing test fixed.
- **JSX component CALLS edges** (PR #154): JSX component usage now produces CALLS edges so component-to-component relationships appear in the graph.

### Added
- **Codex platform install support** (PR #177): `code-review-graph install --platform codex` appends a `mcp_servers.code-review-graph` section to `~/.codex/config.toml` without overwriting existing Codex settings.
- **Luau language support** (PR #165, closes #153): Roblox Luau (`.luau`) parsing — functions, classes, local functions, requires, tests.
- **REFERENCES edge type** (PR #217): New edge kind for symbol references that aren't direct calls (map/dispatch lookups, string-keyed handlers), including Python and TypeScript patterns.
- **`recurse_submodules` build option** (PR #215): Build/update can now optionally recurse into git submodules.
- **`.gitignore` default for `.code-review-graph/`** (PR #185): Fresh installs automatically add the SQLite DB directory to `.gitignore` so the database isn't accidentally committed.
- **Clearer gitignore docs** (PR #171, closes #157): Documentation now spells out that `code-review-graph` already respects `.gitignore` via `git ls-files`.

### Changed
- Community detection is now bounded — large repos complete in reasonable time instead of hanging indefinitely.

## [2.2.2] - 2026-04-08

### Added
- **Kotlin call extraction**: `simple_identifier` + `navigation_expression` support for Kotlin method calls (PR #107)
- **JUnit/Kotlin test detection**: Annotation-based test classification (`@Test`, `@ParameterizedTest`, etc.) for Java/Kotlin/C# (PR #107)

### Fixed
- **Windows encoding crash**: All `write_text`/`read_text` calls in `skills.py` now use `encoding='utf-8'` explicitly (PR #152, fixes #147, #148)
- **Invalid `--quiet` flag in hooks**: Removed non-existent `--quiet` and `--json` flags from generated hook commands (PR #152, fixes #149)

### Housekeeping
- Untracked `.claude-plugin/` directory and added to `.gitignore`
- GitHub issue triage: responded to 30+ issues, closed 14, reviewed 24 PRs

## [2.2.1] - 2026-04-07

### Added
- **Parallel parsing**: `ProcessPoolExecutor` for 3-5x faster builds (`CRG_PARSE_WORKERS`, `CRG_SERIAL_PARSE`)
- **Lazy post-processing**: `postprocess="full"|"minimal"|"none"` parameter, `run_postprocess` MCP tool + CLI command
- **SQLite-native BFS**: Recursive CTE replaces NetworkX for impact analysis (`CRG_BFS_ENGINE`)
- **Configurable limits**: `CRG_MAX_IMPACT_NODES`, `CRG_MAX_IMPACT_DEPTH`, `CRG_MAX_BFS_DEPTH`, `CRG_MAX_SEARCH_RESULTS`
- **Multi-hop dependents**: N-hop `find_dependents()` with `CRG_DEPENDENT_HOPS` (default 2) and 500-file cap
- **Token-efficient output**: `detail_level="minimal"` on 8 tools for 40-60% token reduction
- **`get_minimal_context` tool**: Ultra-compact entry point (~100 tokens) with task-based tool routing
- **Token-efficient prompts**: All 5 MCP prompts rewritten with minimal-first workflows
- **Incremental flow/community updates**: `incremental_trace_flows()`, `incremental_detect_communities()`
- **Visualization aggregation**: Community/file/auto modes with drill-down for large graphs (`--mode`)
- **Token-efficiency benchmarks**: 5 workflow benchmarks in `eval/token_benchmark.py`
- **DB schema v6**: Pre-computed `community_summaries`, `flow_snapshots`, `risk_index` tables
- **Token Efficiency Rules** in all skill templates and CLAUDE.md

### Changed
- CLI `build`/`update` support `--skip-flows`, `--skip-postprocess` flags
- PostToolUse hook uses `--skip-flows` for faster incremental updates
- VS Code extension schema version bumped to v6

### Fixed
- mypy type errors in parallel parsing and context tool
- Bandit false positive on prompt preamble string
- Import sorting in graph.py, main.py, tools/__init__.py
- Unused imports cleaned up in cli.py

### Housekeeping
- Gitignore: untrack `marketing-diagram.excalidraw`, `evaluate/results/`, `evaluate/reports/`
- Updated FEATURES.md, LLM-OPTIMIZED-REFERENCE.md, CHANGELOG.md for v2.2.1

## [2.1.0] - 2026-04-03

### Added
- **Jupyter notebook parsing**: Parse `.ipynb` files — extract functions, classes, imports across Python, R, and SQL cells
- **Databricks notebook parsing**: Parse Databricks `.py` notebook exports with `# COMMAND ----------` cell boundaries
- **Lua language support**: Full parsing for `.lua` files (functions, local functions, method calls, requires) — 20th language
- **Perl XS support**: Parse `.xs` files with improved Perl call detection and test coverage
- **Zero-config onboarding**: `install` now sets up skills, hooks, and CLAUDE.md by default so the graph is used automatically
- **Platform rule injection**: Graph instructions injected into all platform rule files (CLAUDE.md, .cursorrules, etc.) on install
- **Smart install detection**: Auto-detects whether installed via uvx or pip and generates correct `.mcp.json`
- **`--platform claude-code` alias**: Accepts both `claude` and `claude-code` as platform names

### Fixed
- **JS/TS arrow functions indexed**: `const foo = () => {}` and `const bar = function() {}` now correctly appear as nodes (#66)
- **`importers_of` path resolution**: Normalized with `resolve()` to match stored edge targets (#65)
- **Custom embedding models**: Support for custom model architectures and restored model param wiring in search (#79)

## [2.0.0] - 2026-03-27

### Added
- **12 new features**: flows, communities, hybrid search, change analysis, refactoring, hints, prompts, skills, wiki, multi-repo registry, migrations, eval framework
- **14 new modules** (~10,000 lines): `flows.py`, `communities.py`, `search.py`, `changes.py`, `refactor.py`, `hints.py`, `prompts.py`, `skills.py`, `wiki.py`, `registry.py`, `migrations.py`, `eval/`
- **15 new MCP tools**: `list_flows`, `get_flow`, `get_affected_flows`, `list_communities`, `get_community`, `get_architecture_overview`, `detect_changes`, `refactor`, `apply_refactor`, `generate_wiki`, `get_wiki_page`, `list_repos`, `cross_repo_search`, `find_large_functions`, `semantic_search_nodes`
- **5 MCP prompts**: `review_changes`, `architecture_map`, `debug_issue`, `onboard_developer`, `pre_merge_check`
- **7 new CLI commands**: `detect-changes`, `wiki`, `eval`, `register`, `unregister`, `repos`, `install --skills/--hooks/--all`
- **Interactive visualization upgrade**: Detail panel, community coloring, flow path highlighting, search-to-zoom, kind filters

### Security
- Fix path traversal in wiki page reader
- Add regex allowlist for git ref validation
- Add explicit SSL context for MiniMax API

### Fixed
- Fix git diff argument ordering (broke incremental updates)
- Fix `node_qualified_name` schema mismatch in wiki flow query
- Batch N+1 queries in `get_impact_radius` and risk scoring

### Architecture
- Decompose `_extract_from_tree` into 6 focused methods
- Add 17 public query methods to `GraphStore`
- Split `tools.py` into 10 themed sub-modules

## [1.8.4] - 2026-03-20

### Added
- **Vue SFC parsing**: Parse `.vue` Single File Components by extracting `<script>` blocks with automatic `lang="ts"` detection
- **Solidity support**: Full parsing for `.sol` files (functions, events, modifiers, inheritance)
- **`find_large_functions_tool`**: New MCP tool to find functions, classes, or files exceeding a line-count threshold
- **Call target resolution**: Bare call targets resolved to qualified names using same-file definitions (`_resolve_call_targets`)
- **Multi-word AND search**: `search_nodes` now requires all words to match (case-insensitive)
- **Impact radius pagination**: `get_impact_radius` returns `truncated` flag, `total_impacted` count, and accepts `max_results` parameter

### Changed
- Language count updated from 12 to 14 across all documentation
- MCP tool count updated from 8 to 9 across all documentation
- VS Code extension updated to v0.2.0 with 5 new commands documented

### Fixed
- Test assertions updated to handle qualified call targets from `_resolve_call_targets`

## [1.8.3] - 2026-03-20

### Fixed
- **Parser recursion guard**: Added `_MAX_AST_DEPTH = 180` limit to `_extract_from_tree()` preventing stack overflow on deeply nested ASTs
- **Module cache bound**: Added `_MODULE_CACHE_MAX = 15_000` with automatic eviction to prevent unbounded memory growth in `_module_file_cache`
- **Embeddings thread safety**: Added `check_same_thread=False` to `EmbeddingStore` SQLite connection
- **Embeddings retry logic**: Added `_call_with_retry()` with exponential backoff for Google Gemini API calls
- **Visualization XSS hardening**: Added `</` to `<\/` replacement in JSON serialization to prevent script injection
- **CLI error handling**: Split broad `except` into specific `json.JSONDecodeError` and `(KeyError, TypeError)` handlers
- **Git timeout**: Made configurable via `CRG_GIT_TIMEOUT` environment variable (default 30s)

### Added
- **Governance files**: Added CONTRIBUTING.md, SECURITY.md, CODE_OF_CONDUCT.md
- **Project URLs**: Added Homepage, Repository, Issues, Changelog URLs to pyproject.toml metadata

## [1.8.2] - 2026-03-17

### Fixed
- **C# parsing broken**: Renamed language identifier from `c_sharp` to `csharp` to match `tree-sitter-language-pack`'s actual identifier. Previously, all C# files were silently skipped because `_get_parser()` swallowed the `LookupError`.

## [1.8.1] - 2026-03-17

### Fixed
- Add missing `max_nodes` parameter to `get_impact_radius` method signature (caused `NameError` at runtime)
- Fix `.gitignore` test assertion to match expanded comment format

## [1.8.0] - 2026-03-17

### Security
- **Prompt injection mitigation**: Node names are now sanitized (control characters stripped, length capped at 256) before appearing in MCP tool responses, preventing graph-laundered prompt injection attacks
- **Path traversal protection**: `repo_root` parameter now validates that the target directory contains a `.git` or `.code-review-graph` directory, preventing arbitrary file exfiltration via MCP tools
- **VSCode RCE fix**: `cliPath` setting is now scoped to `machine` level only, preventing malicious workspace settings from pointing to attacker-controlled binaries
- **XSS fix in visualization**: `escH()` now escapes quotes and backticks in addition to angle brackets, closing stored XSS via crafted node names in generated HTML
- **SRI for CDN assets**: D3.js script tag now includes `integrity` and `crossorigin` attributes to prevent CDN compromise
- **Secure nonce generation**: VSCode webview CSP nonces now use `crypto.randomBytes()` instead of `Math.random()`
- **Symlink protection**: Build, watch mode, and file collection now skip symbolic links to prevent parsing files outside the repository
- **TOCTOU elimination**: File bytes are now read once, then hashed and parsed from the same buffer, closing the time-of-check-to-time-of-use gap

### Fixed
- **Thread-safe NetworkX cache**: Added `threading.Lock` around graph cache reads/writes to prevent race conditions between watch mode and MCP request handling
- **BFS resource limits**: Impact radius traversal now caps at 500 nodes to prevent memory exhaustion on dense graphs
- **SQL parameter batching**: `get_edges_among` now batches queries to stay under SQLite's variable limit on large node sets
- **Database path leakage**: Improved `.gitignore` inside `.code-review-graph/` with explicit warnings about absolute paths in the database

### Changed
- **Pinned dependency bounds**: All dependencies now have upper-bound version constraints to mitigate supply-chain risks

## [1.7.2] - 2026-03-09

### Fixed
- **Watch mode thread safety**: SQLite connections now use `check_same_thread=False` for Python 3.10/3.11 compatibility with watchdog's background threads
- **Full rebuild stale data**: `full_build` now purges nodes/edges from files deleted since last build
- **Removed unused dependency**: `gitpython` was listed in dependencies but never imported — removed to shrink install footprint
- **Stale Docker reference**: Removed non-existent Docker image suggestion from Python version check

## [1.7.0] - 2026-03-09

### Added
- **`install` command** — primary entry point for new users (`code-review-graph install`). `init` remains as an alias for backwards compatibility.
- **`--dry-run` flag** on `install`/`init` — shows what would be written without modifying files
- **PyPI publish workflow** — GitHub releases now automatically publish to PyPI via API token
- **Professional README** — complete rewrite with real benchmark data:
  - Code reviews: 6.8x average token reduction (tested on httpx, FastAPI, Next.js)
  - Live coding tasks: 14.1x average, up to 49.1x on large repos

### Changed
- README restructured around the install-and-forget user experience
- CLI banner now shows `install` as the primary command

## [1.6.4] - 2026-03-06

### Changed
- **Portable MCP config**: `init` now generates `uvx`-based `.mcp.json` instead of absolute Python paths — works on any machine with `uv` installed
- Removed `_safe_path` symlink workaround (no longer needed with `uvx`)

## [1.6.3] - 2026-03-06

### Added
- **SessionStart hook** — Claude Code now automatically prefers graph MCP tools over full codebase scans at the start of every session, saving tokens on general queries
- `homepage` and `author.url` fields in plugin.json for marketplace discoverability

### Fixed
- plugin.json schema: renamed `tags` to `keywords`, removed invalid `skills` path (auto-discovered from default location)
- Removed screenshot placeholder section from README

## [1.6.2] - 2026-02-27

### Fixed
- **Critical**: Incremental hash comparison bug — `file_hash` read from wrong field, causing every file to re-parse
- Watch mode `on_deleted` handler now filters by ignore patterns
- Removed dead code in `full_build` and duplicate `main()` in `incremental.py`
- `get_staged_and_unstaged` handles git renamed files (`R old -> new`)
- TROUBLESHOOTING.md hook config path corrected

### Added
- **Parser: C/C++ support** — full node extraction (structs, classes, functions, includes, calls, inheritance)
- **Parser: name extraction** fixes for Kotlin/Swift (`simple_identifier`), Ruby (`constant`), C/C++ nested `function_declarator`
- `GraphStore` context manager (`__enter__`/`__exit__`)
- `get_all_edges()` and `get_edges_among()` public methods on `GraphStore`
- NetworkX graph caching with automatic invalidation on writes
- Subprocess timeout (30s) on all git calls
- Progress logging every 50 files in full build
- SHA-256 hashing in embeddings (replaced MD5)
- Chunked embedding search (`fetchmany(500)`)
- Batch edge collection in `get_impact_radius` (single SQL query)
- ARIA labels throughout D3.js visualization
- **CI**: Coverage enforcement (`--cov-fail-under=50`), bandit security scanning, mypy type checking
- **Tests**: `test_incremental.py` (24 tests), `test_embeddings.py` (16 tests)
- **Test fixtures**: C, C++, C#, Ruby, PHP, Kotlin, Swift with multilang test classes
- **Docs**: API response schemas in COMMANDS.md, ignore patterns in USAGE.md

## [1.5.3] - 2026-02-27

### Fixed
- `init` now auto-creates symlinks when paths contain spaces (macOS iCloud, OneDrive, etc.)
- `build`, `status`, `visualize`, `watch` work without a git repository (falls back to cwd)
- Skills discoverable via plugin.json (`name` field added to SKILL.md frontmatter)

## [1.5.0] - 2026-02-26

### Added
- **File organization**: All generated files now live in `.code-review-graph/` directory instead of repo root
  - Auto-created `.gitignore` inside the directory prevents accidental commits
  - Automatic migration from legacy `.code-review-graph.db` at repo root
- **Visualization: start collapsed**: Only File nodes visible on load; click to expand children
- **Visualization: search bar**: Filter nodes by name or qualified name in real-time
- **Visualization: edge type toggles**: Click legend items to show/hide edge types (Calls, Imports, Inherits, Contains)
- **Visualization: scale-aware layout**: Force simulation adapts charge, distance, and decay for large graphs (300+ nodes)

### Changed
- Database path: `.code-review-graph.db` → `.code-review-graph/graph.db`
- HTML visualization path: `.code-review-graph.html` → `.code-review-graph/graph.html`
- `.code-review-graph/**` added to default ignore patterns (prevents self-indexing)

### Removed
- `references/` directory (duplicate of `docs/`, caused stale path references)
- `agents/` directory (unused, not wired into any code)
- `settings.json` at repo root (decorative, not loaded by code)

## [1.4.0] - 2026-02-26

### Added
- `init` command: automatic `.mcp.json` setup for Claude Code integration
- `visualize` command: interactive D3.js force-directed graph visualization
- `serve` command: start MCP server directly from CLI

### Changed
- Comprehensive documentation overhaul across all reference files

## [1.3.0] - 2026-02-26

### Added
- Universal installation: now works with `pip install code-review-graph[embeddings]` on Python 3.10+
- CLI entry point (`code-review-graph` command works after normal pip install)
- Clear Python version check with helpful Docker fallback for older Python users
- Improved README installation section with one-command + Docker option

### Changed
- Minimum Python requirement lowered from 3.11 → 3.10 (covers ~90% of users)

### Fixed
- Installation friction for most developers



---

# FILE: CLAUDE.md

# CLAUDE.md - Project Context for Claude Code

## Project Overview

**code-review-graph** is a persistent, incrementally-updated knowledge graph for token-efficient code reviews with Claude Code. It parses codebases using Tree-sitter, builds a structural graph in SQLite, and exposes it via MCP tools and prompts.

## Graph Tool Usage (Token-Efficient)
When using code-review-graph MCP tools, follow these rules:
1. First call: `get_minimal_context(task="<description>")` — costs ~100 tokens, gives you the full picture.
2. All subsequent calls: use `detail_level="minimal"` unless you need more.
3. Prefer `query_graph` with a specific target over broad `list_*` calls.
4. The `next_tool_suggestions` field in every response tells you the optimal next step.
5. Target: ≤5 tool calls per task, ≤800 total tokens of graph context.

## Architecture

- **Core Package**: `code_review_graph/` (Python 3.10+)
  - `parser.py` — Tree-sitter multi-language AST parser (19 languages including Vue SFC, Solidity, Dart, R, Perl, Lua + Jupyter/Databricks notebooks)
  - `graph.py` — SQLite-backed graph store (nodes, edges, BFS impact analysis)
  - `tools.py` — 22 MCP tool implementations
  - `main.py` — FastMCP server entry point (stdio transport), registers 22 tools + 5 prompts
  - `incremental.py` — Git-based change detection, file watching
  - `embeddings.py` — Optional vector embeddings (Local sentence-transformers, Google Gemini, MiniMax)
  - `visualization.py` — D3.js interactive HTML graph generator
  - `cli.py` — CLI entry point (install, build, update, watch, status, visualize, serve, wiki, detect-changes, register, unregister, repos, eval)
  - `flows.py` — Execution flow detection and criticality scoring
  - `communities.py` — Community detection (Leiden algorithm or file-based grouping) and architecture overview
  - `search.py` — FTS5 hybrid search (keyword + vector)
  - `changes.py` — Risk-scored change impact analysis (detect-changes)
  - `refactor.py` — Rename preview, dead code detection, refactoring suggestions
  - `hints.py` — Review hint generation
  - `prompts.py` — 5 MCP prompt templates (review_changes, architecture_map, debug_issue, onboard_developer, pre_merge_check)
  - `wiki.py` — Markdown wiki generation from community structure
  - `skills.py` — Skill definitions for Claude Code plugin
  - `registry.py` — Multi-repo registry with connection pool
  - `migrations.py` — Database schema migrations (v1-v5)
  - `tsconfig_resolver.py` — TypeScript path alias resolution

- **VS Code Extension**: `code-review-graph-vscode/` (TypeScript)
  - Separate subproject with its own `package.json`, `tsconfig.json`
  - Reads from `.code-review-graph/graph.db` via SQLite

- **Database**: `.code-review-graph/graph.db` (SQLite, WAL mode)

## Key Commands

```bash
# Development
uv run pytest tests/ --tb=short -q          # Run tests (572 tests)
uv run ruff check code_review_graph/        # Lint
uv run mypy code_review_graph/ --ignore-missing-imports --no-strict-optional

# Build & test
uv run code-review-graph build              # Full graph build
uv run code-review-graph update             # Incremental update
uv run code-review-graph status             # Show stats
uv run code-review-graph serve              # Start MCP server
uv run code-review-graph wiki               # Generate markdown wiki
uv run code-review-graph detect-changes     # Risk-scored change analysis
uv run code-review-graph register <path>    # Register repo in multi-repo registry
uv run code-review-graph repos              # List registered repos
uv run code-review-graph eval               # Run evaluation benchmarks
```

## Code Conventions

- **Line length**: 100 chars (ruff)
- **Python target**: 3.10+
- **SQL**: Always use parameterized queries (`?` placeholders), never f-string values
- **Error handling**: Catch specific exceptions, log with `logger.warning/error`
- **Thread safety**: `threading.Lock` for shared caches, `check_same_thread=False` for SQLite
- **Node names**: Always sanitize via `_sanitize_name()` before returning to MCP clients
- **File reads**: Read bytes once, hash, then parse (TOCTOU-safe pattern)

## Security Invariants

- No `eval()`, `exec()`, `pickle`, or `yaml.unsafe_load()`
- No `shell=True` in subprocess calls
- `_validate_repo_root()` prevents path traversal via repo_root parameter
- `_sanitize_name()` strips control characters, caps at 256 chars (prompt injection defense)
- `escH()` in visualization escapes HTML entities including quotes and backticks
- SRI hash on D3.js CDN script tag
- API keys only from environment variables, never hardcoded

## Test Structure

- `tests/test_parser.py` — Parser correctness, cross-file resolution
- `tests/test_graph.py` — Graph CRUD, stats, impact radius
- `tests/test_tools.py` — MCP tool integration tests
- `tests/test_visualization.py` — Export, HTML generation, C++ resolution
- `tests/test_incremental.py` — Build, update, migration, git ops
- `tests/test_multilang.py` — 19 language parsing tests (including Vue, Solidity, Dart, R, Perl, XS, Lua)
- `tests/test_embeddings.py` — Vector encode/decode, similarity, store
- `tests/test_flows.py` — Execution flow detection and criticality
- `tests/test_communities.py` — Community detection, architecture overview
- `tests/test_changes.py` — Risk-scored change analysis
- `tests/test_refactor.py` — Rename preview, dead code, suggestions
- `tests/test_search.py` — FTS5 hybrid search
- `tests/test_hints.py` — Review hint generation
- `tests/test_prompts.py` — MCP prompt template tests
- `tests/test_wiki.py` — Wiki generation
- `tests/test_skills.py` — Skill definitions
- `tests/test_registry.py` — Multi-repo registry
- `tests/test_migrations.py` — Database migrations
- `tests/test_eval.py` — Evaluation framework
- `tests/test_tsconfig_resolver.py` — TypeScript path resolution
- `tests/test_integration_v2.py` — v2 pipeline integration test
- `tests/fixtures/` — Sample files for each supported language

## CI Pipeline

- **lint**: ruff on Python 3.10
- **type-check**: mypy
- **security**: bandit scan
- **test**: pytest matrix (3.10, 3.11, 3.12, 3.13) with 50% coverage minimum



---

# FILE: CODE_OF_CONDUCT.md

# Code of Conduct

This project follows the [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

All participants in this project are expected to follow the Code of Conduct.
Please report any concerns to the project maintainers.

## Scope

This Code of Conduct applies within all project spaces, including issues,
pull requests, discussions, and any other communication channels.

## Reporting

Instances of unacceptable behavior may be reported to the project maintainers.
All complaints will be reviewed and investigated promptly and fairly.



---

# FILE: CONTRIBUTING.md

# Contributing to code-review-graph

Thank you for your interest in contributing! This guide will help you get started.

## Development Setup

```bash
# Clone the repository
git clone https://github.com/tirth8205/code-review-graph.git
cd code-review-graph

# Install with dev dependencies (requires uv)
uv sync --extra dev

# Verify setup
uv run pytest tests/ --tb=short -q
```

## Running Tests

```bash
# All tests
uv run pytest tests/ --tb=short -q

# With coverage
uv run pytest --cov=code_review_graph --cov-report=term-missing --cov-fail-under=50

# Single test file
uv run pytest tests/test_parser.py -v
```

## Linting and Type Checking

```bash
uv run ruff check code_review_graph/
uv run mypy code_review_graph/ --ignore-missing-imports --no-strict-optional
```

## Code Style

- **Line length**: 100 characters
- **Target**: Python 3.10+
- **Linter**: ruff (rules: E, F, I, N, W)
- **SQL**: Always parameterized queries (`?` placeholders)
- **Imports**: Sorted by ruff (isort-compatible)

## Making Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass: `uv run pytest`
6. Ensure linting passes: `uv run ruff check code_review_graph/`
7. Submit a pull request

## Project Structure

```
code_review_graph/     # Core Python package
  parser.py            # Tree-sitter multi-language parser
  graph.py             # SQLite graph store
  tools.py             # MCP tool implementations
  incremental.py       # Git diff + file watch logic
  embeddings.py        # Vector embedding support
  visualization.py     # D3.js HTML generator
  cli.py               # CLI entry point
  main.py              # MCP server entry point
tests/                 # Test suite
  fixtures/            # Language sample files
```

## Adding Language Support

1. Add the extension mapping to `EXTENSION_TO_LANGUAGE` in `parser.py`
2. Add tree-sitter node types to `_CLASS_TYPES`, `_FUNCTION_TYPES`, `_IMPORT_TYPES`, `_CALL_TYPES`
3. Add a sample fixture file in `tests/fixtures/`
4. Add parsing tests in `tests/test_multilang.py`

## Reporting Issues

- Use GitHub Issues: https://github.com/tirth8205/code-review-graph/issues
- Include: Python version, OS, steps to reproduce, error output

## License

By contributing, you agree that your contributions will be licensed under the MIT License.



---

# FILE: SECURITY.md

# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 2.0.x   | Yes       |
| < 2.0   | No        |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do NOT open a public GitHub issue**
2. Email the maintainer directly or use GitHub's private vulnerability reporting
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will acknowledge receipt within 48 hours and aim to release a fix within 7 days for critical issues.

## Security Model

### Threat Surface

code-review-graph is a **local development tool**. It:
- Runs as a local MCP server via stdio (no network listener)
- Stores data in a local SQLite database (`.code-review-graph/graph.db`)
- Makes no network calls during normal operation
- Only reads source files within the validated repository root

### Mitigations

| Vector | Mitigation |
|--------|------------|
| SQL Injection | All queries use parameterized `?` placeholders |
| Path Traversal | `_validate_repo_root()` requires `.git` or `.code-review-graph` directory |
| Prompt Injection | `_sanitize_name()` strips control characters, caps at 256 chars |
| XSS (visualization) | `escH()` escapes HTML entities; `</script>` escaped in JSON |
| Subprocess Injection | No `shell=True`; all git commands use list arguments |
| Supply Chain | Dependencies pinned with upper bounds; `uv.lock` has SHA256 hashes |
| CDN Tampering | D3.js loaded with Subresource Integrity (SRI) hash |
| API Key Leakage | Google API key loaded from env var only, never logged |

### Optional Network Calls

- **Google Gemini embeddings**: Only when explicitly configured with `provider="google"` and `GOOGLE_API_KEY` env var
- **Local embeddings model download**: One-time download from HuggingFace on first use of `sentence-transformers`
- **D3.js CDN**: Visualization HTML loads D3.js v7 from `d3js.org` (with SRI verification)

## Security Scanning

The CI pipeline runs:
- **Bandit** security scanner on every PR
- **Ruff** linter for code quality
- **mypy** type checker

Bandit exemptions are documented in `pyproject.toml` with justifications for each skip.



---

# FILE: docs/COMMANDS.md

# All Available Commands

## Skills (Claude Code slash commands)

### `/code-review-graph:build-graph`
Build or update the knowledge graph.
- First time: performs a full build
- Subsequent: incremental update (only changed files)

### `/code-review-graph:review-delta`
Review only changes since last commit.
- Auto-detects changed files via git diff
- Computes blast radius (2-hop default)
- Generates structured review with guidance

### `/code-review-graph:review-pr`
Review a PR or branch diff.
- Uses main/master as base
- Full impact analysis across all PR commits
- Structured output with risk assessment

## MCP Tools (22 total)

### Core Tools

#### `build_or_update_graph_tool`
```
full_rebuild: bool = False    # True for full re-parse
repo_root: str | None         # Auto-detected
base: str = "HEAD~1"          # Git diff base
```

#### `get_impact_radius_tool`
```
changed_files: list[str] | None  # Auto-detected from git
max_depth: int = 2               # Hops in graph
repo_root: str | None
base: str = "HEAD~1"
```

#### `query_graph_tool`
```
pattern: str    # callers_of, callees_of, imports_of, importers_of,
                # children_of, tests_for, inheritors_of, file_summary
target: str     # Node name, qualified name, or file path
repo_root: str | None
```

#### `get_review_context_tool`
```
changed_files: list[str] | None
max_depth: int = 2
include_source: bool = True
max_lines_per_file: int = 200
repo_root: str | None
base: str = "HEAD~1"
```

#### `semantic_search_nodes_tool`
```
query: str           # Search string
kind: str | None     # File, Class, Function, Type, Test
limit: int = 20
repo_root: str | None
model: str | None    # Embedding model (falls back to CRG_EMBEDDING_MODEL env var)
```

#### `embed_graph_tool`
```
repo_root: str | None
model: str | None    # Embedding model name
```
Requires: `pip install code-review-graph[embeddings]`

#### `list_graph_stats_tool`
```
repo_root: str | None
```

#### `find_large_functions_tool`
```
min_lines: int = 50                # Minimum line count threshold
kind: str | None                   # File, Class, Function, or Test
file_path_pattern: str | None      # Filter by file path substring
limit: int = 50                    # Max results to return
repo_root: str | None
```

#### `get_docs_section_tool`
```
section_name: str    # usage, review-delta, review-pr, commands, legal, watch, embeddings, languages, troubleshooting
```

### Flow Tools

#### `list_flows_tool`
```
sort_by: str = "criticality"  # criticality, depth, node_count, file_count, name
limit: int = 50
kind: str | None              # Filter by entry point kind (e.g. "Test", "Function")
repo_root: str | None
```

#### `get_flow_tool`
```
flow_id: int | None          # Database ID from list_flows_tool
flow_name: str | None        # Name to search (partial match)
include_source: bool = False # Include source snippets for each step
repo_root: str | None
```

#### `get_affected_flows_tool`
```
changed_files: list[str] | None  # Auto-detected from git
base: str = "HEAD~1"
repo_root: str | None
```

### Community Tools

#### `list_communities_tool`
```
sort_by: str = "size"    # size, cohesion, name
min_size: int = 0
repo_root: str | None
```

#### `get_community_tool`
```
community_name: str | None   # Name to search (partial match)
community_id: int | None     # Database ID
include_members: bool = False
repo_root: str | None
```

#### `get_architecture_overview_tool`
```
repo_root: str | None
```

### Change Analysis and Refactoring Tools

#### `detect_changes_tool`
```
base: str = "HEAD~1"
changed_files: list[str] | None
include_source: bool = False
max_depth: int = 2
repo_root: str | None
```
Primary tool for code review. Maps git diffs to affected functions, flows, communities, and test coverage gaps. Returns risk scores and prioritized review items.

#### `refactor_tool`
```
mode: str = "rename"         # "rename", "dead_code", or "suggest"
old_name: str | None         # (rename) Current symbol name
new_name: str | None         # (rename) New name
kind: str | None             # (dead_code) Function or Class
file_pattern: str | None     # (dead_code) Filter by file path substring
repo_root: str | None
```

#### `apply_refactor_tool`
```
refactor_id: str             # ID from prior refactor_tool call
repo_root: str | None
```

### Wiki Tools

#### `generate_wiki_tool`
```
repo_root: str | None
force: bool = False          # Regenerate all pages even if unchanged
```

#### `get_wiki_page_tool`
```
community_name: str          # Community name to look up
repo_root: str | None
```

### Multi-Repo Tools

#### `list_repos_tool`
```
(no parameters)
```

#### `cross_repo_search_tool`
```
query: str
kind: str | None
limit: int = 20
```

## MCP Prompts (5 workflow templates)

### `review_changes`
Pre-commit review workflow using detect_changes, affected_flows, and test gaps.
```
base: str = "HEAD~1"
```

### `architecture_map`
Architecture documentation using communities, flows, and Mermaid diagrams.

### `debug_issue`
Guided debugging using search, flow tracing, and recent changes.
```
description: str = ""
```

### `onboard_developer`
New developer orientation using stats, architecture, and critical flows.

### `pre_merge_check`
PR readiness check with risk scoring, test gaps, and dead code detection.
```
base: str = "HEAD~1"
```

## CLI Commands

```bash
# Setup
code-review-graph install           # Register MCP server with Claude Code (alias: init)
code-review-graph install --dry-run # Preview without writing files

# Build and update
code-review-graph build                        # Full build
code-review-graph update                       # Incremental update
code-review-graph update --base origin/main    # Custom base ref

# Monitor and inspect
code-review-graph status                       # Graph statistics
code-review-graph watch                        # Auto-update on file changes
code-review-graph visualize                    # Generate interactive HTML graph

# Analysis
code-review-graph detect-changes               # Risk-scored change analysis
code-review-graph detect-changes --base HEAD~3 # Custom base ref
code-review-graph detect-changes --brief       # Compact output

# Wiki
code-review-graph wiki                         # Generate markdown wiki from communities

# Multi-repo
code-review-graph register <path> [--alias name]  # Register a repository
code-review-graph unregister <path_or_alias>       # Remove from registry
code-review-graph repos                            # List registered repositories

# Evaluation
code-review-graph eval                         # Run evaluation benchmarks

# Server
code-review-graph serve                        # Start MCP server (stdio)
```



---

# FILE: docs/FEATURES.md

# Features

## v2.2.1 (Current)
- **24 MCP tools** (up from 22): Added `get_minimal_context` and `run_postprocess`.
- **Parallel parsing**: `ProcessPoolExecutor` for 3-5x faster builds on large repos.
- **Lazy post-processing**: `postprocess="full"|"minimal"|"none"` to skip expensive steps.
- **SQLite-native BFS**: Recursive CTE replaces NetworkX for impact analysis (faster on large graphs).
- **Token-efficient output**: `detail_level="minimal"` on 8 tools for 40-60% token reduction.
- **`get_minimal_context`**: Ultra-compact entry point (~100 tokens) with task-based tool routing.
- **Incremental flow/community updates**: Only re-trace affected flows, skip community re-detection when unaffected.
- **Visualization aggregation**: Community/file/auto modes with drill-down for 5k+ node graphs.
- **Token-efficiency benchmarks**: 5 workflow benchmarks in eval framework.
- **Pre-computed summary tables**: DB schema v6 with `community_summaries`, `flow_snapshots`, `risk_index`.
- **Configurable limits**: `CRG_MAX_IMPACT_NODES`, `CRG_MAX_IMPACT_DEPTH`, `CRG_DEPENDENT_HOPS`, etc.
- **Multi-hop dependents**: N-hop dependent discovery (default 2) with 500-file cap.
- **615 tests** across 22 test files.

## v2.1.0
- **22 MCP tools** (up from 9): 13 new tools for flows, communities, architecture, refactoring, wiki, multi-repo, and risk-scored change detection.
- **5 MCP prompts**: `review_changes`, `architecture_map`, `debug_issue`, `onboard_developer`, `pre_merge_check` workflow templates.
- **18 languages** (up from 15): Added Dart, R, Perl support.
- **Execution flows**: Trace call chains from entry points (HTTP handlers, CLI commands, tests), sorted by criticality score.
- **Community detection**: Cluster related code entities via Leiden algorithm (igraph) or file-based grouping.
- **Architecture overview**: Auto-generated architecture map with module summaries and cross-community coupling warnings.
- **Risk-scored change detection**: `detect_changes` maps git diffs to affected functions, flows, communities, and test coverage gaps with priority ordering.
- **Refactoring tools**: Rename preview with edit list, dead code detection, community-driven refactoring suggestions.
- **Wiki generation**: Auto-generate markdown wiki pages for each community with optional LLM summaries (ollama).
- **Multi-repo registry**: Register multiple repositories, search across all of them with `cross_repo_search`.
- **Full-text search**: FTS5 virtual table with porter stemming for hybrid keyword + vector search.
- **Database migrations**: Versioned schema migrations (v1-v5) with automatic upgrade on startup.
- **Optional dependency groups**: `[embeddings]`, `[google-embeddings]`, `[communities]`, `[eval]`, `[wiki]`, `[all]`.
- **Evaluation framework**: Benchmark suite with matplotlib visualization.
- **TypeScript path resolution**: tsconfig.json paths/baseUrl alias resolution for imports.
- **486 tests** across 22 test files.

## v1.8.4
- **Multi-word AND search**: `search_nodes` now requires all words to match (case-insensitive), producing more precise results.
- **Call target resolution**: Bare call targets are resolved to qualified names using same-file definitions, improving `callers_of`/`callees_of` accuracy.
- **Impact radius pagination**: `get_impact_radius` returns `truncated` flag and `total_impacted` count; `max_results` parameter controls output size.
- **`find_large_functions_tool`**: New MCP tool to find functions, classes, or files exceeding a line-count threshold.
- **15 languages**: Added Vue SFC and Solidity support.
- **Documentation overhaul**: All docs updated with accurate language/tool counts, version references, and VS Code extension parity.

## v1.8.3
- **Parser recursion guard**: `_MAX_AST_DEPTH = 180` prevents stack overflow on deeply nested ASTs.
- **Module cache bound**: `_MODULE_CACHE_MAX = 15,000` with automatic eviction.
- **Embeddings thread safety**: `check_same_thread=False` on EmbeddingStore SQLite.
- **Embeddings retry logic**: Exponential backoff for Google Gemini API calls.
- **Visualization XSS hardening**: `</` escaped to `<\/` in JSON serialization.
- **CLI error handling**: Split broad `except` into specific handlers.
- **Git timeout**: Configurable via `CRG_GIT_TIMEOUT` env var.
- **Governance files**: CONTRIBUTING.md, SECURITY.md, CODE_OF_CONDUCT.md.

## v1.8.2
- **C# parsing fix**: Renamed language identifier from `c_sharp` to `csharp`.
- **Watch mode thread safety**: SQLite connections compatible with Python 3.10/3.11 watchdog threads.
- **Full rebuild cleanup**: Purges stale data from deleted files during full rebuild.
- **Dependency trim**: Removed unused `gitpython` dependency.

## v1.7.0
- **`install` command**: New primary entry point for setup (`code-review-graph install`). `init` remains as an alias.
- **`--dry-run` flag**: Preview what `install`/`init` would write without modifying files.
- **PyPI auto-publish**: GitHub releases now automatically publish to PyPI.
- **README rewrite**: Professional documentation with real benchmark data from httpx, FastAPI, and Next.js.

## v1.6.4
- **Portable MCP config**: `init` now generates `uvx`-based `.mcp.json` — no absolute paths, works on any machine with `uv` installed
- **Removed symlink workaround**: The `_safe_path` helper for spaces-in-paths is no longer needed with `uvx`

## v1.6.3
- **SessionStart hook**: Claude Code automatically prefers graph MCP tools over full codebase scans at session start
- **Marketplace ready**: plugin.json corrected for official Claude Code plugin marketplace submission
- **README cleanup**: Removed screenshot placeholders

## v1.6.2
- **24 audit fixes**: Critical bug fixes, performance improvements, parser enhancements, expanded test coverage
- **Parser: C/C++ support**: Full node extraction for C and C++ (classes, functions, imports, calls, inheritance)
- **Parser: name extraction**: Fixed for Kotlin, Swift (simple_identifier), Ruby (constant)
- **Performance**: NetworkX graph caching, batch edge queries, chunked embedding search, git subprocess timeouts
- **CI hardening**: Coverage enforcement (50%), bandit security scanning, mypy type checking
- **Tests**: +40 new tests for incremental updates, embeddings, and 7 new language fixtures
- **Docs**: API response schemas, ignore pattern documentation, fixed hook config reference
- **Accessibility**: ARIA labels throughout D3.js visualization

## v1.5.3
- **Spaces-in-path handling**: *(superseded in v1.6.4 by `uvx`-based config)* Previously used symlinks for spaces in paths
- **No git required**: `build`, `status`, `visualize`, `watch` now work on any directory without git
- **Plugin ready**: Skills registered in plugin.json, SKILL.md frontmatter fixed
- **File organization**: Generated files moved into `.code-review-graph/` directory (auto-created `.gitignore`, legacy migration)
- **Visualization density**: Starts collapsed (File nodes only), search bar, clickable edge type toggles, scale-aware layout for large graphs
- **Project cleanup**: Removed redundant `references/`, `agents/`, `settings.json`

## v1.4.0
- **`init` command**: Automatic `.mcp.json` setup for Claude Code integration
- **Interactive D3.js graph visualization**: `code-review-graph visualize` generates an HTML graph you can explore in-browser
- **Documentation overhaul**: Comprehensive docs audit across all reference files

## v1.3.0
- **Python version check with Docker fallback**: Automatically detects Python 3.10+ and suggests Docker if unavailable
- **Universal install**: `pip install code-review-graph` — no git clone needed
- **CLI entry point**: `code-review-graph` command available system-wide after pip install

## v1.2.0
- **Logging improvements**: Structured logging throughout the codebase
- **Watch debounce**: Smarter file-change detection in watch mode
- **tools.py fixes**: Bug fixes and reliability improvements for MCP tools
- **CI coverage**: GitHub Actions CI/CD pipeline with test coverage reporting

## v1.1.0
- **Watch mode**: `code-review-graph watch` — auto-rebuilds graph on file changes
- **Vector embeddings**: Optional `pip install .[embeddings]` for semantic code search
- **Go, Rust, Java verified**: 12+ languages with dedicated test coverage
- **47 tests passing**, 8 MCP tools registered
- README badges and cleaner install flow

## v1.0.0 (Foundation)
- **Persistent SQLite knowledge graph** — zero external dependencies
- **Tree-sitter multi-language parsing** — classes, functions, imports, calls, inheritance
- **Incremental updates** via `git diff` + automatic dependency cascade
- **Impact-radius / blast-radius analysis** — BFS through call/import/inheritance graph
- **6 MCP tools** for full graph interaction
- **3 review-first skills**: build-graph, review-delta, review-pr
- **PostToolUse hooks** (Write|Edit|Bash) for automatic background updates
- **FastMCP 3.0 compatible** stdio MCP server

## Privacy & Data
- All data stays 100% local
- Graph stored in `.code-review-graph/graph.db` (SQLite), auto-gitignored
- No telemetry, no network calls
- Respects `.gitignore` and `.code-review-graphignore`



---

# FILE: docs/INDEX.md

# Documentation Index

- [USAGE.md](USAGE.md) -- How to install and use
- [FEATURES.md](FEATURES.md) -- What's included, changelog
- [COMMANDS.md](COMMANDS.md) -- All 22 MCP tools, 5 MCP prompts, skills, and CLI commands
- [LLM-OPTIMIZED-REFERENCE.md](LLM-OPTIMIZED-REFERENCE.md) -- Token-optimized reference (Claude Code reads this)
- [architecture.md](architecture.md) -- System design and data flow
- [schema.md](schema.md) -- Graph node/edge schema, SQLite tables (including flows, communities, FTS5)
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) -- Common issues and fixes (including Windows/WSL)
- [ROADMAP.md](ROADMAP.md) -- Shipped and planned features
- [LEGAL.md](LEGAL.md) -- License and privacy



---

# FILE: docs/LEGAL.md

# Legal & Privacy

**License:** MIT (see [LICENSE](../LICENSE) in project root)

**Privacy:**
- Zero telemetry
- All graph data stored locally in `.code-review-graph/graph.db`
- No network calls during normal operation
- Optional embeddings model downloaded once from HuggingFace (when using `[embeddings]` extra)

**Data:** Never leaves your machine.

**Warranty:** Provided as-is, without warranty of any kind.



---

# FILE: docs/LLM-OPTIMIZED-REFERENCE.md

# LLM-OPTIMIZED REFERENCE -- code-review-graph v2.2.1

Claude Code: Read ONLY the exact `<section>` you need. Never load the whole file.

<section name="usage">
Quick install: pip install code-review-graph
Then: code-review-graph install && code-review-graph build
First run: /code-review-graph:build-graph
After that use only delta/pr commands.
ALWAYS start with get_minimal_context_tool(task="your task") — returns ~100 tokens with risk, communities, flows, and suggested next tools.
Use detail_level="minimal" on all subsequent calls unless you need more detail.
</section>

<section name="review-delta">
1. Call get_minimal_context_tool(task="review changes") first.
2. If risk is low: detect_changes_tool(detail_level="minimal") → report summary.
3. If risk is medium/high: detect_changes_tool(detail_level="standard") → expand on high-risk items.
Target: ≤5 tool calls, ≤800 tokens total context.
</section>

<section name="review-pr">
Fetch PR diff -> detect_changes_tool -> get_affected_flows_tool -> structured review with blast-radius table and risk scores.
Never include full files unless explicitly asked.
</section>

<section name="commands">
MCP tools (24): get_minimal_context_tool, build_or_update_graph_tool, run_postprocess_tool, get_impact_radius_tool, query_graph_tool, get_review_context_tool, semantic_search_nodes_tool, embed_graph_tool, list_graph_stats_tool, get_docs_section_tool, find_large_functions_tool, list_flows_tool, get_flow_tool, get_affected_flows_tool, list_communities_tool, get_community_tool, get_architecture_overview_tool, detect_changes_tool, refactor_tool, apply_refactor_tool, generate_wiki_tool, get_wiki_page_tool, list_repos_tool, cross_repo_search_tool
MCP prompts (5): review_changes, architecture_map, debug_issue, onboard_developer, pre_merge_check
Skills: build-graph, review-delta, review-pr
CLI: code-review-graph [install|init|build|update|status|watch|visualize|serve|wiki|detect-changes|postprocess|register|unregister|repos|eval]
Token efficiency: All tools support detail_level="minimal" for compact output. Always call get_minimal_context_tool first.
</section>

<section name="legal">
MIT license. 100% local. No telemetry. DB file: .code-review-graph/graph.db
</section>

<section name="watch">
Run: code-review-graph watch (auto-updates graph on file save via watchdog)
Or use PostToolUse (Write|Edit|Bash) hooks for automatic background updates.
</section>

<section name="embeddings">
Optional: pip install code-review-graph[embeddings]
Then call embed_graph_tool to compute vectors.
semantic_search_nodes_tool auto-uses vectors when available, falls back to keyword + FTS5.
Providers: Local (all-MiniLM-L6-v2, 384-dim), Google Gemini, MiniMax (embo-01, 1536-dim).
Configure via CRG_EMBEDDING_MODEL env var or model parameter.
</section>

<section name="languages">
Supported (19): Python, TypeScript/TSX, JavaScript, Vue, Go, Rust, Java, Scala, C#, Ruby, Kotlin, Swift, PHP, Solidity, C/C++, Dart, R, Perl, Lua
Parser: Tree-sitter via tree-sitter-language-pack
</section>

<section name="troubleshooting">
DB lock: SQLite WAL mode, auto-recovers. Only one build at a time.
Large repos: First build 30-60s. Incremental <2s. Add patterns to .code-review-graphignore.
Stale graph: Run /code-review-graph:build-graph manually.
Missing nodes: Check language support + ignore patterns. Use full_rebuild=True.
Windows/WSL: Use forward slashes in paths. Ensure uv is on PATH in WSL.
</section>

**Instruction to Claude Code (always follow):**
When user asks anything about "code-review-graph", "how to use", "commands", "review-delta", etc.:
1. Call get_docs_section_tool with the exact section name.
2. Use ONLY that content + current graph state.
3. Never include full docs or source code in your reasoning.
This guarantees 90%+ token savings.



---

# FILE: docs/ROADMAP.md

# Roadmap

## Shipped

### v2.0.0
- 22 MCP tools (up from 9) and 5 MCP prompts
- 18 languages (added Dart, R, Perl)
- Execution flow detection with criticality scoring
- Community detection (Leiden algorithm via igraph, file-based fallback)
- Architecture overview with coupling warnings
- Risk-scored change detection (`detect_changes`)
- Refactoring tools (rename preview, dead code, suggestions)
- Wiki generation from community structure
- Multi-repo registry with cross-repo search
- FTS5 full-text search with porter stemming
- Database migrations (v1-v5)
- Evaluation framework with matplotlib visualization
- TypeScript tsconfig path alias resolution
- MiniMax embedding provider (embo-01)
- Optional dependency groups: `[embeddings]`, `[google-embeddings]`, `[communities]`, `[eval]`, `[wiki]`, `[all]`
- 486 tests across 22 test files

### v1.8.4
- Multi-word AND search, call target resolution, impact radius pagination
- `find_large_functions_tool`, Vue SFC and Solidity support
- Documentation overhaul

### v1.7.0
- `install` command as primary entry point (`init` kept as alias)
- `--dry-run` flag for previewing install/init changes
- Automatic PyPI publishing via GitHub Actions on release
- README rewrite with real benchmark data from httpx, FastAPI, and Next.js

### v1.6.x
- Portable `uvx`-based MCP config
- SessionStart hook for automatic graph tool preference
- 24 audit fixes: C/C++ support, performance, CI hardening

### v1.5.x
- Generated files in `.code-review-graph/` directory
- Visualization density: collapsed start, search, edge toggles
- Works without git

### v1.4.0
- `init` command, interactive D3.js visualization, `serve` command

### v1.3.0
- Universal pip install, CLI entry point, Python version check

### v1.1.0-v1.2.0
- Watch mode, vector embeddings, logging, CI coverage

### v1.0.0 (Foundation)
- Persistent SQLite knowledge graph, Tree-sitter parsing, incremental updates
- Impact radius analysis, 6 MCP tools, 3 skills

## Planned

- GitHub PR bot integration
- Team sync (shared graph via git-tracked DB)
- SSE/HTTP MCP transport for multi-client access
- Performance optimization for monorepos (>50k files)

## Ongoing

- Additional language grammars as requested
- Integration with more Claude Code features as the platform evolves



---

# FILE: docs/TROUBLESHOOTING.md

# Troubleshooting

## Quick reference for common install/setup problems

Four issues account for most support questions. Check these first:

### 1. `Hooks use a matcher + hooks array` error in `.claude/settings.json`

**You're on a pre-v2.2.3 release.** v2.2.1 and v2.2.2 shipped a broken hook schema — flat `{matcher, command, timeout}` entries without the required nested `hooks: []` array, timeouts in milliseconds instead of seconds, and a `PreCommit` event that isn't a real Claude Code event. PR #208 (shipped in v2.2.3) rewrote the generator to emit the correct v1.x+ schema.

**Fix:**

```bash
pip install --upgrade code-review-graph   # → v2.2.4 or later
cd /path/to/your/project
code-review-graph install                 # rewrites .claude/settings.json
```

The re-install merge-replaces the entire broken `hooks` block with the new nested format and drops a real git pre-commit hook into `.git/hooks/pre-commit` (that's where "check before commit" lives in v2.2.3+, not in Claude Code settings).

Valid Claude Code hook events are: `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SubagentStop`, `SessionStart`, `SessionEnd`, `PreCompact`, `Notification`. There is no `PreCommit`.

### 2. `code-review-graph: command not found` after `pip install`

`pip install` put the console script into a `bin/` directory that isn't on your `$PATH`. Four fixes, in order of recommendation:

**Option 1 — Use `pipx` (cleanest):**

```bash
pip uninstall code-review-graph
pipx install code-review-graph
```

`pipx` installs CLI tools in an isolated venv and guarantees `~/.local/bin` is on PATH.

**Option 2 — Use `uvx` (no install needed):**

```bash
uvx code-review-graph install
uvx code-review-graph build
```

**Option 3 — Run it as a Python module (always works):**

```bash
python -m code_review_graph install
python -m code_review_graph build
```

**Option 4 — Fix PATH manually:**

```bash
pip show code-review-graph | grep Location
# Find the sibling `bin/` directory; on macOS user installs this is
# typically ~/Library/Python/3.X/bin. Add it to your shell rc:
echo 'export PATH="$HOME/Library/Python/3.12/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### 3. Is code-review-graph project-scoped or user-scoped?

**Both** — four different pieces, each scoped differently:

| Piece                         | Scope          | Where                                                            |
|-------------------------------|----------------|------------------------------------------------------------------|
| The Python package            | User-scoped    | Install once via `pip`/`pipx`/`uvx`                              |
| The graph database            | Project-scoped | `.code-review-graph/graph.db` inside each project                |
| MCP server config (`.mcp.json`) | Project-scoped | Claude Code launches one MCP server per project, with `cwd=<project>` |
| Multi-repo registry           | User-scoped    | `~/.code-review-graph/registry.json` (only for `cross_repo_search`) |

**TL;DR**: install the tool **once**, then run `code-review-graph install && code-review-graph build` inside **each** project you want graph-aware reviews in.

### 4. "I built the graph but Claude Code doesn't see it in a new session"

Most likely causes, ranked:

1. **You didn't restart Claude Code after `install`.** Claude Code reads `.mcp.json` at startup — if you ran `install` in one session, fully quit and reopen Claude Code for the MCP server to register.
2. **New session's `cwd` is a different directory.** The MCP server is launched with `cwd=<project>` and it reads `.code-review-graph/graph.db` from there. If your new session opened in a parent folder or a different project, it won't find the graph you built.
3. **You ran `build` but not `install`.** `build` creates `graph.db`; `install` is what registers the MCP server with Claude Code via `.mcp.json`. You need both.
4. **MCP server is crashing on startup.** Run `/mcp` inside Claude Code to see server status, or check `~/Library/Logs/Claude/mcp*.log` on macOS.

**Quick checklist:**

```bash
cd /path/to/your/project
code-review-graph status    # should print Files/Nodes/Edges from the built graph
ls .mcp.json                # should exist
cat .mcp.json               # should reference `code-review-graph serve`
# then: fully quit Claude Code and reopen it inside this project
```

If `status` shows the graph but `/mcp` in the new session doesn't list `code-review-graph`, the `.mcp.json` isn't in the session's `cwd` — re-run `code-review-graph install` from the correct project root.

---

## Database lock errors
The graph uses SQLite with WAL mode. If you see lock errors:
- Ensure only one build process runs at a time
- The database auto-recovers; just retry
- Delete `.code-review-graph/graph.db-wal` and `.code-review-graph/graph.db-shm` if corrupt

## Large repositories (>10k files)
- First build may take 30-60 seconds
- Subsequent incremental updates are fast (<2s)
- Add more ignore patterns to `.code-review-graphignore`:
  ```
  generated/**
  vendor/**
  *.min.js
  ```

## Missing nodes after build
- Check that the file's language is supported (see [FEATURES.md](FEATURES.md))
- Check that the file isn't matched by an ignore pattern
- Run with `full_rebuild=True` to force a complete re-parse

## Graph seems stale
- Hooks auto-update on edit/commit
- If stale, run `/code-review-graph:build-graph` manually
- Check that hooks are configured in `hooks/hooks.json` (see [hooks documentation](../hooks/hooks.json))

## Embeddings not working
- Install with: `pip install code-review-graph[embeddings]`
- Run `embed_graph_tool` to compute vectors
- First embedding run downloads the model (~90MB, one time)

## MCP server won't start
- Verify `uv` is installed (`uv --version`; install with `pip install uv` or `brew install uv`)
- Check that `uvx code-review-graph serve` runs without errors
- If using a custom `.mcp.json`, ensure it uses `"command": "uvx"` with `"args": ["code-review-graph", "serve"]`
- Re-run `code-review-graph install` to regenerate the config

## Windows / WSL

- Use forward slashes in paths when passing `repo_root` to MCP tools
- In WSL, ensure `uv` is installed inside WSL (not the Windows version): `curl -LsSf https://astral.sh/uv/install.sh | sh`
- If `uv` is not found after install, add `~/.cargo/bin` to your PATH
- File watching (`code-review-graph watch`) may have delays on WSL1 due to filesystem event limitations; WSL2 is recommended
- On Windows native (non-WSL), long path support may need to be enabled: `git config --system core.longpaths true`

## Community detection requires igraph

- Install with: `pip install code-review-graph[communities]`
- Without igraph, community detection falls back to file-based grouping (less precise but functional)

## Wiki generation with LLM summaries

- Install with: `pip install code-review-graph[wiki]`
- Requires a running Ollama instance for LLM-powered summaries
- Without Ollama, wiki pages are generated with structural information only (no prose summaries)

## Optional dependency groups

If a tool returns an ImportError, install the relevant optional group:
- `pip install code-review-graph[embeddings]` for semantic search
- `pip install code-review-graph[google-embeddings]` for Google Gemini embeddings
- `pip install code-review-graph[communities]` for igraph-based community detection
- `pip install code-review-graph[eval]` for evaluation benchmarks (matplotlib)
- `pip install code-review-graph[wiki]` for wiki LLM summaries (ollama)
- `pip install code-review-graph[all]` for everything



---

# FILE: docs/USAGE.md

# Code Review Graph — User Guide

**Version:** v2.1.0 (Apr 3, 2026)

## Installation

```bash
pip install code-review-graph
code-review-graph install    # auto-detects and configures all supported platforms
code-review-graph build      # parse your codebase
```

`install` detects which AI coding tools you have and writes the correct MCP configuration for each one. Restart your editor/tool after installing.

To target a specific platform instead of auto-detecting all:

```bash
code-review-graph install --platform codex
code-review-graph install --platform cursor
code-review-graph install --platform claude-code
```

### Supported Platforms

| Platform | Config file |
|----------|-------------|
| **Codex** | `~/.codex/config.toml` |
| **Claude Code** | `.mcp.json` |
| **Cursor** | `.cursor/mcp.json` |
| **Windsurf** | `.windsurf/mcp.json` |
| **Zed** | `.zed/settings.json` |
| **Continue** | `.continue/config.json` |
| **OpenCode** | `.opencode/config.json` |

## Core Workflow

### 1. Build the graph (first time only)
```
/code-review-graph:build-graph
```
Parses your entire codebase. Takes ~10s for 500 files.

### 2. Review changes (daily use)
```
/code-review-graph:review-delta
```
Reviews only files changed since last commit + everything impacted. 5-10x fewer tokens than a full review.

### 3. Review a PR
```
/code-review-graph:review-pr
```
Comprehensive structural review of a branch diff with blast-radius analysis.

### 4. Watch mode (optional)
```bash
code-review-graph watch
```
Auto-updates the graph on every file save. Zero manual work.

### 5. Visualize the graph (optional)
```bash
code-review-graph visualize
open .code-review-graph/graph.html
```
Interactive D3.js force-directed graph. Starts collapsed (File nodes only) — click a file to expand its children. Use the search bar to filter, and click legend edge types to toggle visibility.

### 6. Semantic search (optional)
```bash
pip install "code-review-graph[embeddings]"
```
Then use `embed_graph_tool` to compute vectors. `semantic_search_nodes_tool` automatically uses vector similarity.

Embedding providers: Local (sentence-transformers), Google Gemini, MiniMax. Configure via `CRG_EMBEDDING_MODEL` env var.

### 7. Detect changes with risk scoring (v2)
```
Ask Claude: "Review my recent changes with risk scoring"
```
Uses `detect_changes_tool` to map diffs to affected functions, flows, communities, and test gaps.

### 8. Explore architecture (v2)
```
Ask Claude: "Show me the architecture of this project"
```
Uses `get_architecture_overview_tool` for community-based architecture map with coupling warnings.

### 9. Generate wiki (v2)
```bash
code-review-graph wiki
```
Creates markdown wiki pages for each detected community in `.code-review-graph/wiki/`.

### 10. Multi-repo search (v2)
```bash
code-review-graph register /path/to/other/repo --alias mylib
```
Then use `cross_repo_search_tool` to search across all registered repositories.

## Token Savings

| Scenario | Without graph | With graph |
|----------|:---:|:---:|
| Review 200-file project | ~150k tokens | ~25k tokens |
| Incremental review | ~150k tokens | ~8k tokens |
| PR review | ~100k tokens | ~15k tokens |

## Supported Languages

Python, TypeScript/TSX, JavaScript, Vue, Go, Rust, Java, Scala, C#, Ruby, Kotlin, Swift, PHP, Solidity, C/C++, Dart, R, Perl

## What Gets Indexed

- **Nodes**: Files, Classes, Functions/Methods, Types, Tests
- **Edges**: CALLS, IMPORTS_FROM, INHERITS, IMPLEMENTS, CONTAINS, TESTED_BY, DEPENDS_ON

See [schema.md](schema.md) for full details.

## Ignore Patterns

By default, these paths are excluded from indexing:

```
.code-review-graph/**    node_modules/**    .git/**
__pycache__/**           *.pyc              .venv/**
venv/**                  dist/**            build/**
.next/**                 target/**          *.min.js
*.min.css                *.map              *.lock
package-lock.json        yarn.lock          *.db
*.sqlite                 *.db-journal
```

To add custom patterns, create a `.code-review-graphignore` file in your repo root (same syntax as `.gitignore`):

```
generated/**
vendor/**
*.generated.ts
```

In git repos, indexing is based on tracked files (`git ls-files`), so gitignored files are skipped automatically. Use `.code-review-graphignore` to exclude tracked files or when git isn't available.



---

# FILE: docs/architecture.md

# Architecture

## System Overview

`code-review-graph` is a Claude Code plugin that maintains a persistent, incrementally-updated knowledge graph of a codebase. It's designed to make code reviews faster and more context-aware by providing structural understanding of code relationships.

## Component Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                        Claude Code                           │
│                                                              │
│  Skills (SKILL.md)          Hooks (hooks.json)               │
│  ├── build-graph            └── PostToolUse (Write|Edit|Bash) │
│  ├── review-delta                → incremental update         │
│  └── review-pr                                               │
│          │                        │                          │
│          ▼                        ▼                          │
│  ┌────────────────────────────────────────────┐              │
│  │            MCP Server (stdio)              │              │
│  │                                            │              │
│  │  22 MCP Tools + 5 MCP Prompts              │              │
│  │  ├── Core: build, impact, query, review,   │              │
│  │  │   search, embed, stats, docs, large_fn  │              │
│  │  ├── Flows: list, get, affected            │              │
│  │  ├── Communities: list, get, architecture   │              │
│  │  ├── Analysis: detect_changes, refactor,   │              │
│  │  │   apply_refactor                        │              │
│  │  ├── Wiki: generate, get_page              │              │
│  │  └── Multi-repo: list_repos, cross_search  │              │
│  └────────────────┬───────────────────────────┘              │
└───────────────────┼──────────────────────────────────────────┘
                    │
        ┌───────────┼───────────────┐
        ▼           ▼               ▼
   ┌─────────┐ ┌─────────┐  ┌─────────────┐
   │ Parser  │ │  Graph  │  │ Incremental │
   │         │ │  Store  │  │   Engine    │
   └────┬────┘ └────┬────┘  └──────┬──────┘
        │           │              │
        ▼           ▼              ▼
   Tree-sitter   SQLite DB      git diff
   grammars      (.code-review- subprocess
                 graph/
                 graph.db)
```

## Data Flow

### Full Build
1. `collect_all_files()` gathers tracked files (`git ls-files`) and applies `.code-review-graphignore` (gitignored files are skipped automatically when git is available)
2. For each file, `CodeParser.parse_file()` uses Tree-sitter to extract AST
3. AST walker identifies structural nodes (classes, functions, imports) and edges (calls, inheritance)
4. `GraphStore.store_file_nodes_edges()` persists to SQLite with file hash for change detection
5. Metadata updated with timestamp

### Incremental Update
1. `get_changed_files()` runs `git diff --name-only` against base ref
2. `find_dependents()` queries the graph for files importing the changed files
3. Changed + dependent files are re-parsed (others skipped via hash comparison)
4. Only affected rows in SQLite are updated

### Review Context Generation
1. Changed files identified (git diff or explicit list)
2. `get_impact_radius()` performs BFS from changed nodes through the graph
3. Source snippets extracted for changed areas only
4. Review guidance generated (test coverage gaps, wide blast radius warnings)
5. Assembled into a structured, token-efficient context for Claude

## Storage

### SQLite Schema
- **nodes** table: id, kind, name, qualified_name, file_path, line_start/end, language, community_id, etc.
- **edges** table: id, kind, source_qualified, target_qualified, file_path, line
- **metadata** table: key-value pairs (last_updated, build_type, schema_version)
- **flows** table: id, name, entry_point_id, depth, node_count, file_count, criticality, path_json
- **flow_memberships** table: flow_id, node_id, position
- **communities** table: id, name, level, parent_id, cohesion, size, dominant_language, description
- **nodes_fts** (FTS5 virtual table): full-text search on name, qualified_name, file_path, signature
- **embeddings** table (separate DB): node_id, model, vector, hash

Indexes on qualified_name, file_path, edge source/target, criticality, community_id, and cohesion for fast lookups.

WAL mode enabled for concurrent read access during updates.

### Qualified Names
Nodes are uniquely identified by qualified names:
- Files: absolute path (e.g., `/repo/src/auth.py`)
- Functions: `file_path::function_name` (e.g., `/repo/src/auth.py::authenticate`)
- Methods: `file_path::ClassName.method_name` (e.g., `/repo/src/auth.py::AuthService.login`)

## Parsing Strategy

Tree-sitter provides language-agnostic AST access. The parser:
1. Walks the AST recursively
2. Pattern-matches on node types (language-specific mappings in `_CLASS_TYPES`, `_FUNCTION_TYPES`, etc.)
3. Extracts names, parameters, return types, base classes
4. Identifies calls within function bodies
5. Resolves imports to module paths

This approach is more robust than tree-sitter queries across grammar versions.

## Visualization

The `visualization.py` module generates an interactive D3.js force-directed graph as a self-contained HTML file. It reads all nodes and edges from the SQLite graph store and renders them in the browser, allowing developers to visually explore code relationships, filter by node kind, and inspect dependencies.

## Impact Analysis Algorithm

BFS from seed nodes (changed files' contents):
1. Seed = all qualified names in changed files
2. For each node in frontier:
   - Follow forward edges (what this node affects)
   - Follow reverse edges (what depends on this node)
3. Expand up to `max_depth` hops (default: 2)
4. Collect all reached nodes as "impacted"

This captures both downstream effects (things that call changed code) and upstream context (things that the changed code depends on).



---

# FILE: docs/schema.md

# Knowledge Graph Schema

## Node Types

### File
Represents a source code file.

| Property | Type | Description |
|----------|------|-------------|
| name | string | Absolute file path |
| file_path | string | Same as name for File nodes |
| language | string | Detected language (python, typescript, go, etc.) |
| line_start | int | Always 1 |
| line_end | int | Total line count |
| file_hash | string | SHA-256 of file contents (for change detection) |

### Class
Represents a class, struct, interface, enum, or module definition.

| Property | Type | Description |
|----------|------|-------------|
| name | string | Class name |
| file_path | string | File containing the class |
| line_start | int | Definition start line |
| line_end | int | Definition end line |
| language | string | Source language |
| parent_name | string? | Enclosing class (for nested classes) |
| modifiers | string? | Access modifiers (public, abstract, etc.) |

### Function
Represents a function, method, or constructor definition.

| Property | Type | Description |
|----------|------|-------------|
| name | string | Function name |
| file_path | string | File containing the function |
| line_start | int | Definition start line |
| line_end | int | Definition end line |
| language | string | Source language |
| parent_name | string? | Enclosing class (for methods) |
| params | string? | Parameter list as source text |
| return_type | string? | Return type annotation |
| is_test | bool | Whether this is a test function |

### Test
Same schema as Function, but `kind = "Test"` and `is_test = true`. Identified by:
- Name starts with `test_` or `Test`
- Name ends with `_test` or `_spec`
- File matches test file patterns (`test_*.py`, `*.test.ts`, `*_test.go`, etc.)

### Type
Represents a type alias, interface, or enum definition (primarily for TypeScript, Go, Rust).

| Property | Type | Description |
|----------|------|-------------|
| name | string | Type name |
| file_path | string | File containing the type |
| line_start | int | Definition start line |
| line_end | int | Definition end line |

## Edge Types

### CALLS
A function calls another function.

| Property | Type | Description |
|----------|------|-------------|
| source | string | Qualified name of the caller |
| target | string | Name of the called function (may be unqualified) |
| file_path | string | File where the call occurs |
| line | int | Line number of the call |

### IMPORTS_FROM
A file imports from another module or file.

| Property | Type | Description |
|----------|------|-------------|
| source | string | Importing file path |
| target | string | Imported module/path |
| file_path | string | Same as source |
| line | int | Line number of the import |

### INHERITS
A class extends/inherits from another class.

| Property | Type | Description |
|----------|------|-------------|
| source | string | Child class qualified name |
| target | string | Parent class name |
| file_path | string | File containing the child class |

### IMPLEMENTS
A class implements an interface (Java, C#, TypeScript, Go).

| Property | Type | Description |
|----------|------|-------------|
| source | string | Implementing class |
| target | string | Interface name |

### CONTAINS
Structural containment: a file contains a class, a class contains a method.

| Property | Type | Description |
|----------|------|-------------|
| source | string | Container (file path or class qualified name) |
| target | string | Contained node qualified name |

### TESTED_BY
A function is tested by a test function.

| Property | Type | Description |
|----------|------|-------------|
| source | string | Function being tested |
| target | string | Test function qualified name |

### DEPENDS_ON
General dependency relationship (used for non-specific dependencies).

## Qualified Name Format

Nodes are uniquely identified by qualified names:

```
# File node
/absolute/path/to/file.py

# Top-level function
/absolute/path/to/file.py::function_name

# Method in a class
/absolute/path/to/file.py::ClassName.method_name

# Nested class method
/absolute/path/to/file.py::OuterClass.InnerClass.method_name
```

## SQLite Tables

```sql
-- Nodes table
CREATE TABLE nodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kind TEXT NOT NULL,
    name TEXT NOT NULL,
    qualified_name TEXT NOT NULL UNIQUE,
    file_path TEXT NOT NULL,
    line_start INTEGER,
    line_end INTEGER,
    language TEXT,
    parent_name TEXT,
    params TEXT,
    return_type TEXT,
    modifiers TEXT,
    is_test INTEGER DEFAULT 0,
    file_hash TEXT,
    extra TEXT DEFAULT '{}',
    updated_at REAL NOT NULL
);

-- Edges table
CREATE TABLE edges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kind TEXT NOT NULL,
    source_qualified TEXT NOT NULL,
    target_qualified TEXT NOT NULL,
    file_path TEXT NOT NULL,
    line INTEGER DEFAULT 0,
    extra TEXT DEFAULT '{}',
    updated_at REAL NOT NULL
);

-- Metadata table
CREATE TABLE metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- Flows table (v2.0)
CREATE TABLE flows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    entry_point_id INTEGER NOT NULL,
    depth INTEGER NOT NULL,
    node_count INTEGER NOT NULL,
    file_count INTEGER NOT NULL,
    criticality REAL NOT NULL DEFAULT 0.0,
    path_json TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Flow memberships table (v2.0)
CREATE TABLE flow_memberships (
    flow_id INTEGER NOT NULL,
    node_id INTEGER NOT NULL,
    position INTEGER NOT NULL,
    PRIMARY KEY (flow_id, node_id)
);

-- Communities table (v2.0)
CREATE TABLE communities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    level INTEGER NOT NULL DEFAULT 0,
    parent_id INTEGER,
    cohesion REAL NOT NULL DEFAULT 0.0,
    size INTEGER NOT NULL DEFAULT 0,
    dominant_language TEXT,
    description TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Full-text search virtual table (v2.0)
CREATE VIRTUAL TABLE nodes_fts USING fts5(
    name, qualified_name, file_path, signature,
    content='nodes', content_rowid='rowid',
    tokenize='porter unicode61'
);
```

The `nodes` table also has a `community_id INTEGER` column (added via migration v4) linking nodes to their detected community.



---

# FILE: skills/review-delta/SKILL.md

---
name: review-delta
description: Review only changes since last commit using impact analysis. Token-efficient delta review with automatic blast-radius detection.
argument-hint: "[file or function name]"
---

# Review Delta

Perform a focused, token-efficient code review of only the changed code and its blast radius.

**Token optimization:** Before starting, call `get_docs_section_tool(section_name="review-delta")` for the optimized workflow. Use ONLY changed nodes + 2-hop neighbors in context.

## Steps

1. **Ensure the graph is current** by calling `build_or_update_graph_tool()` (incremental update).

2. **Get review context** by calling `get_review_context_tool()`. This returns:
   - Changed files (auto-detected from git diff)
   - Impacted nodes and files (blast radius)
   - Source code snippets for changed areas
   - Review guidance (test coverage gaps, wide impact warnings, inheritance concerns)

3. **Analyze the blast radius** by reviewing the `impacted_nodes` and `impacted_files` in the context. Focus on:
   - Functions whose callers changed (may need signature/behavior verification)
   - Classes with inheritance changes (Liskov substitution concerns)
   - Files with many dependents (high-risk changes)

4. **Perform the review** using the context. For each changed file:
   - Review the source snippet for correctness, style, and potential bugs
   - Check if impacted callers/dependents need updates
   - Verify test coverage using `query_graph_tool(pattern="tests_for", target=<function_name>)`
   - Flag any untested changed functions

5. **Report findings** in a structured format:
   - **Summary**: One-line overview of the changes
   - **Risk level**: Low / Medium / High (based on blast radius)
   - **Issues found**: Bugs, style issues, missing tests
   - **Blast radius**: List of impacted files/functions
   - **Recommendations**: Actionable suggestions

## Advantages Over Full-Repo Review

- Only sends changed + impacted code to the model (5-10x fewer tokens)
- Automatically identifies blast radius without manual file searching
- Provides structural context (who calls what, inheritance chains)
- Flags untested functions automatically



---

# FILE: skills/review-pr/SKILL.md

---
name: review-pr
description: Review a PR or branch diff using the knowledge graph for full structural context. Outputs a structured review with blast-radius analysis.
argument-hint: "[PR number or branch name]"
---

# Review PR

Perform a comprehensive code review of a pull request or branch diff using the knowledge graph.

**Token optimization:** Before starting, call `get_docs_section_tool(section_name="review-pr")` for the optimized workflow. Never include full files unless explicitly asked.

## Steps

1. **Identify the changes** for the PR:
   - If a PR number or branch is provided, use `git diff main...<branch>` to get changed files
   - Otherwise auto-detect from the current branch vs main/master

2. **Update the graph** by calling `build_or_update_graph_tool(base="main")` to ensure the graph reflects the current state.

3. **Get the full review context** by calling `get_review_context_tool(base="main")`:
   - This uses `main` (or the specified base branch) as the diff base
   - Returns all changed files across all commits in the PR

4. **Analyze impact** by calling `get_impact_radius_tool(base="main")`:
   - Review the blast radius across the entire PR
   - Identify high-risk areas (widely depended-upon code)

5. **Deep-dive each changed file**:
   - Read the full source of files with significant changes
   - Use `query_graph_tool(pattern="callers_of", target=<func>)` for high-risk functions
   - Use `query_graph_tool(pattern="tests_for", target=<func>)` to verify test coverage
   - Check for breaking changes in public APIs

6. **Generate structured review output**:

   ```
   ## PR Review: <title>

   ### Summary
   <1-3 sentence overview>

   ### Risk Assessment
   - **Overall risk**: Low / Medium / High
   - **Blast radius**: X files, Y functions impacted
   - **Test coverage**: N changed functions covered / M total

   ### File-by-File Review
   #### <file_path>
   - Changes: <description>
   - Impact: <who depends on this>
   - Issues: <bugs, style, concerns>

   ### Missing Tests
   - <function_name> in <file> - no test coverage found

   ### Recommendations
   1. <actionable suggestion>
   2. <actionable suggestion>
   ```

## Tips

- For large PRs, focus on the highest-impact files first (most dependents)
- Use `semantic_search_nodes_tool` to find related code the PR might have missed
- Check if renamed/moved functions have updated all callers
