---
title: "Source — code-review-graph: Graph-Based Automated Code Review"
type: source-synthesis
domain: ai-agents
status: synthesized
confidence: high
maturity: seed
created: 2026-04-14
updated: 2026-04-14
sources:
  - id: code-review-graph-github
    type: repository
    url: "https://github.com/tirth8205/code-review-graph"
tags:
  - code-review
  - graph-analysis
  - tree-sitter
  - mcp
  - token-efficiency
  - blast-radius
  - ai-agents
  - static-analysis
  - sqlite
  - quality-gates
---

# Source — code-review-graph: Graph-Based Automated Code Review

## Summary

`code-review-graph` is a Python-based MCP-native tool that builds an incremental structural graph of any codebase using Tree-sitter AST parsing, stored in a local SQLite database, and exposed via 22 MCP tools and 5 workflow prompts. Its core value proposition is token efficiency: rather than feeding an entire codebase to an AI assistant, it computes a blast-radius set of files actually affected by a change, delivering 8.2x average token reduction across benchmark repositories. With 100% recall on impact analysis, zero external dependencies during normal operation, and support for 19+ languages, it represents a mature pattern for AI-assisted code review at scale.

## Key Insights

### 1. Blast-Radius as the Core Primitive

The central concept is the "blast radius" — the minimal set of files, functions, and tests that could be affected by any given change. This is computed by tracing the graph's call, import, and inheritance edges from changed nodes outward to their dependents. The design principle: AI assistants should read only what matters, not the entire repository. Benchmark results show 100% recall (no impacted file ever missed) with an average F1 of 0.54 — meaning the system conservatively over-predicts rather than under-predicts, which is the correct safety trade-off for code review.

### 2. Graph Storage Architecture: SQLite + BFS

The persistence layer is a local SQLite file at `.code-review-graph/graph.db`, operating in WAL mode. Graph traversal uses recursive CTEs (BFS in SQL) rather than loading NetworkX into memory, enabling impact analysis on 100k+ node graphs without memory pressure. Node types are: functions, classes, imports. Edge types are: CALLS, IMPORTS_FROM, INHERITS, CONTAINS, REFERENCES. Schema migrations are versioned (v1–v6), with v6 adding pre-computed `community_summaries`, `flow_snapshots`, and `risk_index` tables for performance.

### 3. Incremental Updates via Git-Diff + SHA-256

The incremental update pipeline fires on every git commit or file save. It reads `git diff`, SHA-256-hashes each changed file's bytes, computes the dependent closure, and re-parses only what changed. A 2,900-file project re-indexes in under 2 seconds. The TOCTOU-safe pattern reads file bytes once, then hashes and parses from the same buffer — preventing race conditions between hash-check and parse.

### 4. MCP Integration Is the Distribution Mechanism

The tool is not a library — it is an MCP server. Twenty-two tools are registered via FastMCP (stdio transport), spanning blast-radius queries, semantic search, architecture overviews, community detection, wiki generation, and multi-repo registry searches. Five workflow prompts (`review_changes`, `architecture_map`, `debug_issue`, `onboard_developer`, `pre_merge_check`) are pre-baked templates that orchestrate multi-step review workflows. The `install` command auto-detects all supported AI coding platforms (Claude Code, Codex, Cursor, Windsurf, Zed, Continue, Kiro, Qwen Code) and writes the correct `.mcp.json` configuration for each.

### 5. Token Budget Discipline Is a First-Class Design Goal

The tool embeds token-efficiency rules directly into its CLAUDE.md: every task should start with `get_minimal_context(task="...")` at ~100 tokens, use `detail_level="minimal"` on subsequent calls, and cap at ≤5 tool calls and ≤800 total graph-context tokens per task. This is the right approach to AI tooling — the tool itself teaches its consumers how to use it economically.

### 6. Security Model Is Explicit and Complete

The security model is documented with threat surface, mitigations per vector, and CI enforcement:
- SQL injection: parameterized queries only
- Path traversal: `_validate_repo_root()` requires `.git` or `.code-review-graph` directory
- Prompt injection: `_sanitize_name()` strips control characters, caps at 256 chars
- XSS in visualization: `escH()` escapes all HTML entities including quotes and backticks
- Supply chain: pinned dependencies with upper bounds, `uv.lock` with SHA256 hashes
- CDN tampering: D3.js loaded with SRI hash

### 7. Community Detection Enables Architecture-Level Review

Beyond file-level analysis, the tool runs the Leiden algorithm to cluster code into communities — logical subsystems — and generates an architecture overview from these communities. This allows architecture-level review comments ("this change crosses community boundary X and Y") alongside function-level blast radius. Wiki generation produces a markdown knowledge base from community structure.

### 8. Risk Scoring Surfaces Review Priority

The `detect_changes` tool produces risk-scored change impact analysis: each changed function gets a risk score based on its fan-out (number of callers), test coverage (edges to test nodes), and community centrality. This prioritization lets reviewers focus on the highest-risk changes first — a direct implementation of the "quality gate" concept where high-risk paths get more scrutiny.

### 9. Multi-Repo Registry Supports Monorepo and Cross-Repo Workflows

The registry system allows registering multiple repositories and executing cross-repo searches. This is essential for microservice ecosystems where a change in a shared library has blast radius across multiple downstream services. The `cross_repo_search_tool` searches all registered repos simultaneously.

### 10. Benchmark Data Is Reproducible and Honest

All benchmark numbers are reproducible via `code-review-graph eval --all` against 6 real open-source repositories (express, fastapi, flask, gin, httpx, nextjs). The README honestly acknowledges the express anomaly (0.7x — worse than naive) for single-file changes in small packages, explaining that graph metadata overhead exceeds raw file size for trivial edits. This intellectual honesty about the tool's limits is noteworthy.

## Deep Analysis

### Architecture Pipeline

```
Repository → Tree-sitter Parser (19+ languages) → SQLite Graph (nodes + edges)
          → BFS Impact Analysis → Minimal Review Set → AI Review Context
```

The parser (`parser.py`) uses Tree-sitter grammars to extract typed nodes and edges. Language support is achieved by mapping file extensions to grammar identifiers and defining `_CLASS_TYPES`, `_FUNCTION_TYPES`, `_IMPORT_TYPES`, `_CALL_TYPES` per language. Adding a new language requires four extension mappings and a test fixture — no core changes needed.

The graph store (`graph.py`) is the persistence and query layer. All queries use parameterized SQL. The BFS traversal (`find_dependents()`) supports N-hop traversal (configurable via `CRG_DEPENDENT_HOPS`, default 2) with a 500-file cap to prevent memory exhaustion on dense graphs.

### MCP Tool Surface (22 tools)

Core query tools:
- `get_impact_radius_tool` — blast radius computation
- `get_review_context_tool` — token-optimized review context with structural summary
- `query_graph_tool` — callers, callees, tests, imports, inheritance queries
- `detect_changes_tool` — risk-scored change impact analysis

Analysis tools:
- `list_flows_tool`, `get_flow_tool`, `get_affected_flows_tool` — execution flow tracing
- `list_communities_tool`, `get_community_tool`, `get_architecture_overview_tool` — community analysis
- `semantic_search_nodes_tool` — vector similarity search (optional, via sentence-transformers or Gemini)
- `find_large_functions_tool` — complexity detection

Operational tools:
- `build_or_update_graph_tool` — full rebuild or incremental update
- `refactor_tool`, `apply_refactor_tool` — rename preview, dead code detection
- `generate_wiki_tool`, `get_wiki_page_tool` — markdown wiki generation
- `list_repos_tool`, `cross_repo_search_tool` — multi-repo registry

### Token Efficiency Strategy

The v2.2.1 release added systematic token-efficiency infrastructure:
- `detail_level` parameter (`minimal/standard/full`) on 8 tools, providing 40-60% token reduction at minimal
- `get_minimal_context` tool as ultra-compact entry point (~100 tokens)
- Pre-computed `risk_index` and `community_summaries` tables eliminate expensive on-demand computations
- SQLite-native BFS replaces NetworkX for impact analysis, reducing memory and latency
- `postprocess="minimal"|"none"` on build for faster CI/scripted workflows

### Platform Compatibility Matrix

Supported install targets: Claude Code, Codex, Cursor, Windsurf, Zed, Continue, OpenCode, Antigravity, Kiro, Qwen Code. The `install` command writes platform-specific configurations:
- Claude Code: `.claude/settings.json` hooks + `.mcp.json` server entry
- Cursor/Windsurf: `mcpServers` entry in editor config + `.cursorrules`/`.windsurfrules`
- Codex: `~/.codex/config.toml` `mcp_servers` section

### CI Pipeline and Quality Gates

The project enforces a 4-stage CI pipeline:
1. `ruff` lint on Python 3.10
2. `mypy` type checking
3. `bandit` security scanning
4. `pytest` matrix (3.10–3.13) with 50% coverage minimum

572 tests across 20 test modules, including fixtures for all 19+ supported languages.

### Version History and Maturity Signal

The changelog reveals rapid iteration:
- v1.0 (Feb 2026): basic parser + SQLite + MCP
- v1.8 (Mar 2026): security hardening, visualization, C/C++, Solidity, Vue
- v2.0 (Mar 2026): 12 new features, 14 new modules, 15 new tools — flows, communities, refactoring, wiki
- v2.2 (Apr 2026): parallel parsing, token efficiency, security CVE fixes, Elixir/ObjC/Bash parsers
- v2.3 (Apr 2026): async MCP tools, out-of-tree graph storage, cloud embeddings warning

This trajectory suggests a project with strong momentum, production usage, and active security awareness.

### Limitations and Weaknesses (from README)

- Small single-file changes: graph overhead can exceed raw file size (express: 0.7x)
- Semantic search MRR: 0.35 — keyword search ranking needs improvement
- Flow detection recall: 33% — only reliable for Python (fastapi, httpx) framework patterns
- Impact precision: conservative (over-predicts) — intentional trade-off for review safety

### Relevance to Our Quality and Review Methodology

The blast-radius primitive maps directly to our quality failure prevention model's concept of "impact surface." When evaluating a change's risk, what matters is not the number of files changed but the number of nodes affected in the dependency graph. This tool operationalizes that principle.

The risk-scoring approach (fan-out × test coverage gaps × centrality) matches the quality gate pattern: changes with high fan-out and low test coverage should trigger more rigorous review. This is a concrete implementation of the "verify depth" principle — not just checking what changed, but checking what depends on what changed.

The CLAUDE.md token-budget discipline (≤5 tool calls, ≤800 tokens of graph context) is a model for how we should specify AI tooling consumption constraints in our own wiki methodology.

## Open Questions

- Can this integrate with our existing Python/wiki tools pipeline as a code-quality layer on the devops-solutions-research-wiki codebase itself?
- The community detection (Leiden algorithm) outputs could seed our wiki's domain structure — could blast-radius analysis on wiki page relationships inform which pages to update together?
- How does risk scoring interact with our stage-gated methodology? A "design" stage change that has high blast-radius in implementation modules would be a stage-gate violation — does the graph surface this?
- The `wiki` generation feature produces markdown from community structure — could this complement our `pipeline post` chain?

## Relationships

- RELATES TO: [[model-quality-failure-prevention|Model — Quality and Failure Prevention]] (blast-radius operationalizes impact surface; risk scoring operationalizes quality gates)
- RELATES TO: [[model-ecosystem|Model — Ecosystem Architecture]] (multi-repo registry pattern relevant to openfleet multi-project ecosystem)

## Backlinks

[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
[[model-ecosystem|Model — Ecosystem Architecture]]
