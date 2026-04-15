"""Wiki MCP Server — exposes wiki operations as native Claude Code tools.

Any Claude Code conversation in this project can query, ingest, validate,
and analyze the wiki through MCP tool calls instead of running CLI commands.

Run: python -m tools.mcp_server
Or via .mcp.json in project root (stdio transport).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

from tools.common import (
    find_wiki_pages,
    get_project_root,
    load_config,
    parse_frontmatter,
    parse_sections,
    word_count,
)
from tools.manifest import build_manifest
from tools.pipeline import (
    post_chain,
    run_gaps,
    run_crossref,
    run_mirror,
    run_sync_step,
    fetch_urls,
    fetch_topic,
    scan_project,
    group_fetch,
    pipeline_status,
    run_backlog,
)
from tools.integrations import (
    obsidian,
    notebooklm,
    status_report as integrations_status,
)

# ---------------------------------------------------------------------------
# Server setup
# ---------------------------------------------------------------------------

server = FastMCP(
    name="research-wiki",
    instructions=(
        "Research wiki operations. Use these tools to query, ingest, validate, "
        "and analyze the wiki knowledge base. Run wiki_status first to understand "
        "the current state."
    ),
)

ROOT = get_project_root()
WIKI_DIR = ROOT / "wiki"
CONFIG_DIR = WIKI_DIR / "config"


# ---------------------------------------------------------------------------
# Query tools
# ---------------------------------------------------------------------------

@server.tool()
def wiki_status() -> str:
    """Get current wiki stats: page count, raw files, domain breakdown."""
    status = pipeline_status(ROOT)
    # Add domain breakdown
    manifest_path = WIKI_DIR / "manifest.json"
    domains = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        for dname, dinfo in manifest.get("domains", {}).items():
            domains[dname] = dinfo.get("page_count", 0)

    return json.dumps({
        "wiki_pages": status["wiki_pages"],
        "raw_files": status["raw_files"],
        "raw_by_type": status["raw_by_type"],
        "domains": domains,
    }, indent=2)


@server.tool()
def wiki_search(query: str) -> str:
    """Search wiki pages for a query string. Returns matching file paths and titles."""
    results = []
    for page in find_wiki_pages(WIKI_DIR):
        text = page.read_text(encoding="utf-8", errors="ignore")
        if query.lower() in text.lower():
            meta, _ = parse_frontmatter(text)
            results.append({
                "title": meta.get("title", page.stem),
                "path": str(page.relative_to(ROOT)),
                "domain": meta.get("domain", ""),
                "type": meta.get("type", ""),
            })

    return json.dumps({"query": query, "matches": len(results), "results": results}, indent=2)


@server.tool()
def wiki_read_page(page_path: str) -> str:
    """Read a wiki page by its path (e.g., 'wiki/domains/ai-agents/openfleet.md')."""
    full_path = ROOT / page_path
    if not full_path.exists():
        return json.dumps({"error": f"Page not found: {page_path}"})

    text = full_path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    sections = parse_sections(body)

    return json.dumps({
        "path": page_path,
        "frontmatter": meta,
        "sections": {k: v[:500] + "..." if len(v) > 500 else v for k, v in sections.items()},
    }, indent=2, default=str)


@server.tool()
def wiki_list_pages(domain: str = None) -> str:
    """List all wiki pages, optionally filtered by domain."""
    pages = []
    for page in find_wiki_pages(WIKI_DIR):
        text = page.read_text(encoding="utf-8", errors="ignore")
        meta, _ = parse_frontmatter(text)
        if not meta:
            continue
        if domain and meta.get("domain") != domain:
            continue
        pages.append({
            "title": meta.get("title", page.stem),
            "path": str(page.relative_to(ROOT)),
            "domain": meta.get("domain", ""),
            "type": meta.get("type", ""),
            "status": meta.get("status", ""),
            "confidence": meta.get("confidence", ""),
        })

    return json.dumps({"count": len(pages), "pages": pages}, indent=2)


# ---------------------------------------------------------------------------
# Pipeline tools
# ---------------------------------------------------------------------------

@server.tool()
def wiki_post() -> str:
    """Run the post-ingestion chain: rebuild indexes, manifest, validate, wikilinks, lint."""
    report = post_chain(ROOT, verbose=False)
    return json.dumps(report, indent=2, default=str)


@server.tool()
def wiki_fetch(urls: str) -> str:
    """Fetch one or more URLs into raw/ for processing. Comma-separated."""
    url_list = [u.strip() for u in urls.split(",") if u.strip()]
    results = group_fetch(url_list, ROOT, verbose=False)
    return json.dumps(results, indent=2, default=str)


@server.tool()
def wiki_fetch_topic(topic: str) -> str:
    """Queue a research topic for processing."""
    results = fetch_topic(topic, ROOT, verbose=False)
    return json.dumps(results, indent=2, default=str)


@server.tool()
def wiki_scan_project(project_path: str) -> str:
    """Scan a local project and copy key docs to raw/."""
    results = scan_project(Path(project_path), ROOT, verbose=False)
    return json.dumps(results, indent=2, default=str)


# ---------------------------------------------------------------------------
# Analysis tools
# ---------------------------------------------------------------------------

@server.tool()
def wiki_gaps() -> str:
    """Run gap analysis: orphaned targets, thin pages, weak domains, open questions."""
    report = run_gaps(ROOT, verbose=False)
    # Trim open_questions to top 20 for context efficiency
    if len(report.get("open_questions", [])) > 20:
        report["open_questions"] = report["open_questions"][:20]
        report["open_questions_total"] = len(report["open_questions"])
    return json.dumps(report, indent=2, default=str)


@server.tool()
def wiki_crossref() -> str:
    """Run cross-reference analysis: missing backlinks, domain bridges, comparison candidates."""
    report = run_crossref(ROOT, verbose=False)
    return json.dumps(report, indent=2, default=str)


# ---------------------------------------------------------------------------
# Integration tools
# ---------------------------------------------------------------------------

@server.tool()
def wiki_sync() -> str:
    """Sync wiki to Windows for Obsidian."""
    result = run_sync_step(ROOT, verbose=False)
    return json.dumps(result, indent=2, default=str)


@server.tool()
def wiki_mirror_to_notebooklm(notebook_name: str = "Research Wiki Sources") -> str:
    """Push wiki source URLs to a NotebookLM notebook."""
    result = run_mirror(ROOT, notebook_name=notebook_name, verbose=False)
    return json.dumps(result, indent=2, default=str)


@server.tool()
def wiki_integrations() -> str:
    """Check availability of external integrations (Obsidian CLI, notebooklm-py)."""
    report = integrations_status()
    return json.dumps(report, indent=2, default=str)


@server.tool()
def wiki_continue() -> str:
    """Resume the wiki mission. Runs: post-chain, evolve review, evolve score, gaps, crossref. Returns full mission state."""
    root = get_project_root()
    report = {}

    # Post-chain
    post_result = post_chain(root, verbose=False)
    report["post"] = {
        "pages": post_result["steps"].get("manifest", {}).get("pages", 0),
        "relationships": post_result["steps"].get("manifest", {}).get("relationships", 0),
        "validation_errors": post_result["steps"].get("validate", {}).get("errors", 0),
    }

    # Evolve review
    from tools.evolve import review_seeds, detect_stale, score_candidates
    review = review_seeds(root, verbose=False)
    stale = detect_stale(root, verbose=False)
    report["review"] = {
        "promotable": len(review.get("promotable", [])),
        "stale": len(stale.get("stale", [])),
    }

    # Score candidates
    candidates = score_candidates(root, top=10)
    report["candidates"] = [
        {"title": c.title, "type": c.type, "score": round(c.score, 3)}
        for c in candidates
    ]

    # Gaps
    gaps = run_gaps(root, verbose=False)
    report["gaps"] = {
        "orphaned_targets": len(gaps.get("orphaned_targets", [])),
        "thin_pages": len(gaps.get("thin_pages", [])),
        "weak_domains": len(gaps.get("weak_domains", [])),
        "open_questions": len(gaps.get("open_questions", [])),
    }

    # Crossref
    crossref = run_crossref(root, verbose=False)
    report["crossref"] = {
        "missing_backlinks": len(crossref.get("missing_backlinks", [])),
        "potential_comparisons": len(crossref.get("potential_comparisons", [])),
    }

    return json.dumps(report, indent=2, default=str)


@server.tool()
def wiki_evolve(mode: str = "score", top: int = 10, type_filter: str = None) -> str:
    """Run the evolution pipeline. Modes: score, scaffold, dry-run, review, stale."""
    from tools.evolve import evolve as run_evolve
    root = get_project_root()
    result = run_evolve(root, mode=mode, top=top, type_filter=type_filter, verbose=False)
    return json.dumps(result, indent=2, default=str)


# ---------------------------------------------------------------------------
# Backlog and Log tools
# ---------------------------------------------------------------------------

@server.tool()
def wiki_backlog(epic_id: str = None) -> str:
    """Read backlog pages and return JSON summary.

    Returns epics list (id, title, priority, status, readiness) and tasks list
    (id, title, priority, status, stage, readiness, epic). If epic_id is
    provided, also includes filtered task detail for that epic.
    """
    root = get_project_root()
    result = run_backlog(root, epic_id=epic_id, verbose=False)
    return json.dumps(result, indent=2, default=str)


@server.tool()
def wiki_log(title: str, content: str, note_type: str = "directive") -> str:
    """Create a new log entry in wiki/log/.

    Filename is {date}-{slug}.md. Returns the created file path.

    Args:
        title: Title for the log entry.
        content: Body content to include verbatim.
        note_type: One of directive, session-summary, completion-note (default: directive).
    """
    from datetime import date as _date

    root = get_project_root()
    log_dir = root / "wiki" / "log"
    log_dir.mkdir(parents=True, exist_ok=True)

    today = _date.today().isoformat()
    slug = title.lower().replace(" ", "-").replace(":", "").replace("/", "-")[:60].strip("-")
    filename = f"{today}-{slug}.md"
    file_path = log_dir / filename

    tags_map = {
        "directive": ["log", "directive"],
        "session-summary": ["log", "session"],
        "completion-note": ["log", "completion"],
    }
    tags = tags_map.get(note_type, ["log", note_type])
    tags_yaml = "[" + ", ".join(tags) + "]"

    frontmatter = (
        f"---\n"
        f"title: \"{title}\"\n"
        f"type: note\n"
        f"domain: log\n"
        f"note_type: {note_type}\n"
        f"status: active\n"
        f"confidence: high\n"
        f"created: {today}\n"
        f"updated: {today}\n"
        f"sources: []\n"
        f"tags: {tags_yaml}\n"
        f"---\n\n"
    )
    full_content = frontmatter + f"# {title}\n\n" + content.strip() + "\n"
    file_path.write_text(full_content, encoding="utf-8")

    return json.dumps({"ok": True, "path": str(file_path.relative_to(root))}, indent=2)


# ---------------------------------------------------------------------------
# Gateway tools (unified interface for methodology, identity, flow)
# ---------------------------------------------------------------------------

@server.tool()
def wiki_gateway_query(query_type: str, value: str = None) -> str:
    """Query the wiki gateway for methodology, identity, models, chains, stages, or fields.

    Args:
        query_type: One of: identity, models, chains, model, chain, stage, field, backlog, lessons, logs, page
        value: Required for: model (name), chain (name), stage (name), field (name), page (title). Optional otherwise.
    """
    from tools.gateway import (resolve_paths, query_identity, query_models_list,
                                query_chains_list, query_model, query_chain,
                                query_stage, query_field, query_backlog,
                                query_lessons, query_logs, query_page)

    paths = resolve_paths()
    handlers = {
        "identity": lambda: query_identity(paths),
        "models": lambda: query_models_list(paths),
        "chains": lambda: query_chains_list(paths),
        "model": lambda: query_model(paths, value or "", False),
        "chain": lambda: query_chain(paths, value or "default"),
        "stage": lambda: query_stage(paths, value or "document", None),
        "field": lambda: query_field(paths, value or "readiness"),
        "backlog": lambda: query_backlog(paths),
        "lessons": lambda: query_lessons(paths),
        "logs": lambda: query_logs(paths),
        "page": lambda: query_page(paths, value or ""),
    }
    handler = handlers.get(query_type)
    if not handler:
        return json.dumps({"error": f"Unknown query_type: {query_type}", "available": list(handlers.keys())})
    result = handler()
    if isinstance(result, str):
        return result
    return json.dumps(result, indent=2, default=str)


@server.tool()
def wiki_gateway_template(page_type: str) -> str:
    """Get a wiki page template by type.

    Args:
        page_type: Page type (concept, lesson, pattern, decision, epic, task, etc.) or methodology/type for methodology templates.
    """
    from tools.gateway import resolve_paths, query_template
    paths = resolve_paths()
    result = query_template(paths, page_type)
    if isinstance(result, dict):
        return json.dumps(result, indent=2)
    return result


@server.tool()
def wiki_gateway_contribute(contrib_type: str, title: str, content: str,
                             domain: str = "cross-domain",
                             contributor: str = None, source: str = None,
                             reason: str = None) -> str:
    """Write back to the wiki — create a lesson, remark, or correction.

    Contributions land in 00_inbox (lessons) or log/ (remarks, corrections).
    All contributions start with contribution_status: pending-review and
    require human review to be promoted through maturity tiers. See
    wiki/config/contribution-policy.yaml for the trust-tier policy.

    Args:
        contrib_type: One of: lesson, remark, correction
        title: Title for the contribution
        content: Body content
        domain: Target domain (default: cross-domain)
        contributor: Contributor identifier (e.g. 'openarms-harness-v10').
                     Defaults to user@host auto-detected by the gateway.
        source: Origin path of contribution (e.g. '/home/jfortin/openarms').
                Defaults to 'self' for local contributions.
        reason: Optional audit trail — why this contribution is being made.
    """
    from tools.gateway import resolve_paths, op_contribute
    paths = resolve_paths()
    result = op_contribute(
        paths, contrib_type, title, content, domain,
        contributor=contributor, source=source, reason=reason,
    )
    return json.dumps(result, indent=2, default=str)


@server.tool()
def wiki_gateway_flow(step: int = None) -> str:
    """Goldilocks flow — step-by-step routing from identity to action.

    Shows the 8-step Goldilocks protocol with commands for each step.
    Pass a step number (1-8) to see details for that step.

    Args:
        step: Optional step number (1-8) for detailed view. Omit for overview.
    """
    from tools.gateway import resolve_paths, cmd_flow
    paths = resolve_paths()
    return cmd_flow(paths, step=step)


@server.tool()
def wiki_gateway_timeline(scope: str = None, since: str = "7d", until: str = None,
                           types: str = None, group_by: str = "date",
                           output_format: str = "markdown",
                           full_content: bool = False,
                           remote: bool = False,
                           collapse_arcs: bool = False,
                           epic: str = None,
                           path_filter: str = None) -> str:
    """Computed cross-project temporal view of ecosystem activity.

    Aggregates commits, lessons, patterns, decisions, syntheses, epics, tasks,
    directives, sessions, and handoffs from one or more projects over a time range.
    No stored artifact — computed on demand from source of truth.

    Scope is set-valued and position-aware:
      - 'self'  = the invoking project
      - 'brain' = the declared second-brain
      - 'all'   = every project in the brain's sister-projects registry
      - or explicit names: openarms, openfleet, aicp, devops-control-plane
      - compose with commas: 'self,brain,openarms'

    Default scope: 'self' when run from the brain; 'self,brain' from a sister.

    Args:
        scope: Comma-separated scope list. Default: caller-dependent (see above).
        since: Duration (e.g. '7d', '24h', '2w') or ISO date. Default: '7d'.
        until: Duration or ISO date. Default: now.
        types: Comma-separated event types (lesson,pattern,decision,synthesis,epic,task,session,directive,commit,handoff). Default: all.
        group_by: 'date' | 'project' | 'type' | 'none'. Default: 'date'.
        output_format: 'markdown' | 'json'. Default: 'markdown'.
        full_content: If True, include full event bodies (no caps).
        remote: If True, fetch non-local projects via gh api (slower — opt-in).
                Without this flag, unavailable projects surface as notices only.
        collapse_arcs: If True, collapse same-file same-day event clusters into
                       one arc-summary line (useful for compact journey views).
        epic: Filter to one epic (e.g. 'E013'). Matches parent_epic OR epic file.
        path_filter: Filter events whose path contains this substring.

    Returns: rendered timeline as markdown (default) or JSON.

    See: wiki/decisions/01_drafts/consumer-runtime-signaling-via-mcp-config.md
    for how runtime signaling relates to cross-project timeline queries.
    """
    from tools.timeline import compute_timeline
    scope_list = None
    if scope:
        scope_list = [s.strip() for s in scope.split(",") if s.strip()]
    types_list = None
    if types:
        types_list = [t.strip() for t in types.split(",") if t.strip()]
    return compute_timeline(
        scope=scope_list,
        since=since,
        until=until,
        types=types_list,
        wiki_root=None,
        brain_root=None,
        full_content=full_content,
        group_by=group_by,
        output_format=output_format,
        remote=remote,
        collapse_arcs=collapse_arcs,
        epic=epic,
        path_filter=path_filter,
    )


@server.tool()
def wiki_gateway_docs(doc_name: str = None) -> str:
    """Query root-level documentation files (README, AGENTS, CLAUDE, CONTEXT, ARCHITECTURE, DESIGN, TOOLS, SKILLS).

    These 8 files at the repository root implement the three-layer agent context
    architecture. Each has ONE concern. Read by humans, AI tools, and MCP clients
    to understand the project, its rules, and how to interact with it.

    No arg → list all 8 docs with descriptions and line counts.
    With name (e.g., "agents", "tools") → metadata + 500-char preview.

    For full content of a root doc, read the file directly.

    Args:
        doc_name: Optional. One of: readme, agents, claude, context, architecture, design, tools, skills.
    """
    from tools.gateway import resolve_paths, query_docs
    paths = resolve_paths()
    result = query_docs(paths, doc_name)
    return json.dumps(result, indent=2, default=str)


@server.tool()
def wiki_sister_project(project: str, action: str, arg: str = None, status: str = None, epic: str = None, since: str = None, show_all: bool = False) -> str:
    """Browse sister projects in the ecosystem (OpenArms, OpenFleet, AICP, devops-control-plane, OpenClaw).

    Replaces ad-hoc Bash ls/grep/cat with structured, read-only access. Reads
    from wiki/config/sister-projects.yaml registry.

    NO TRUNCATION. All list actions return every match; read actions return
    full content. Caps are never added by default.

    DIFFERENTIAL BY DEFAULT. List actions (epics, tasks, logs, learnings)
    return ONLY items not yet referenced by any page in our research-wiki —
    i.e. what remains to absorb. Pass show_all=True to see everything. The
    "consumed" flag on each returned item indicates whether our wiki
    references its live path. Consumed ≠ validated — sister claims are weak
    signals to investigate, not ground truth to mirror.

    Actions:
      - "list" (no project needed): list all registered sister projects
      - "info": show project config + accessibility
      - "epics" [status=X, show_all]: list unconsumed epics (or all)
      - "tasks" [status=X, epic=Y, show_all]: list unconsumed tasks (or all)
      - "logs" [since=YYYY-MM-DD, show_all]: list unconsumed logs (or all)
      - "learnings" [show_all]: list unconsumed learnings (or all)
      - "summary": absorption breakdown — consumed vs unconsumed counts per layout section
      - "read-all" (arg=<layout-key>, optional status=<filename-regex>):
        read FULL content of every .md file in a layout directory in one call.
      - "read" (arg=<relative-path>): read a single file's FULL content
      - "find" (arg=<regex-pattern>): filename regex search across project
      - "grep" (arg=<text>): content search in .md files (case-insensitive)

    Examples:
      wiki_sister_project(project="openarms", action="learnings")
        → only OpenArms learnings NOT yet referenced by our wiki (the delta)
      wiki_sister_project(project="openarms", action="learnings", show_all=True)
        → every OpenArms learning with its 'consumed' flag
      wiki_sister_project(project="openarms", action="summary")
        → per-layout absorption percentages
    """
    from tools.sister_project import (
        load_registry, resolve_project, list_projects, project_info,
        list_epics, list_tasks, list_logs, list_learnings,
        read_doc, read_all, find_by_filename, grep_content,
        consumption_summary,
    )
    registry = load_registry()
    if project == "list" or action == "list":
        return json.dumps(list_projects(registry), indent=2, default=str)
    project_cfg = resolve_project(project, registry)
    if project_cfg is None:
        return json.dumps({"error": f"Unknown sister project: {project}",
                           "known": list(registry.get("projects", {}).keys())})
    if action == "info":
        result = project_info(project_cfg)
    elif action == "epics":
        result = list_epics(project_cfg, status_filter=status, show_all=show_all)
    elif action == "tasks":
        result = list_tasks(project_cfg, status_filter=status, epic_filter=epic, show_all=show_all)
    elif action == "logs":
        result = list_logs(project_cfg, since=since, show_all=show_all)
    elif action == "learnings":
        result = list_learnings(project_cfg, show_all=show_all)
    elif action == "summary":
        result = consumption_summary(project_cfg)
    elif action in ("read-all", "read_all", "readall"):
        if not arg:
            return json.dumps({"error": "read-all requires arg=<layout-key> (e.g. 'domains.learnings')"})
        result = read_all(project_cfg, arg, name_pattern=status)
    elif action == "read":
        if not arg:
            return json.dumps({"error": "read requires arg=<relative-path>"})
        result = read_doc(project_cfg, arg)
    elif action == "find":
        if not arg:
            return json.dumps({"error": "find requires arg=<regex-pattern>"})
        result = find_by_filename(project_cfg, arg)
    elif action == "grep":
        if not arg:
            return json.dumps({"error": "grep requires arg=<text>"})
        result = grep_content(project_cfg, arg)
    else:
        return json.dumps({"error": f"Unknown action: {action}",
                           "valid": ["list", "info", "epics", "tasks", "logs", "learnings",
                                     "summary", "read-all", "read", "find", "grep"]})
    return json.dumps(result, indent=2, default=str)


@server.tool()
def wiki_gateway_compliance() -> str:
    """Super-model compliance checker — adoption tier + gaps.

    Resolves Q25. Reads the project's structure (CLAUDE.md, AGENTS.md,
    methodology.yaml, wiki/, tools/) and reports which super-model
    adoption tier (1-4) the project has reached, per-tier requirement
    checklist with met/missing, and recommendations for advancing.

    Four tiers (cumulative):
      1 — Agent Foundation (CLAUDE.md + schema + templates)
      2 — Stage-Gate Process (methodology.yaml + backlog + AGENTS.md)
      3 — Evolution Pipeline (evolve + lint + maturity folders)
      4 — Hub Integration (export profiles + MCP server + .mcp.json)

    Returns JSON with current_tier, max_tier, per-tier breakdown, gaps,
    and actionable recommendations. Makes adoption MEASURABLE instead
    of declared.
    """
    from tools.gateway import resolve_paths, query_compliance
    paths = resolve_paths()
    result = query_compliance(paths)
    return json.dumps(result, indent=2, default=str)


@server.tool()
def wiki_gateway_health() -> str:
    """Composite methodology+quality health score for the wiki with per-dimension breakdown.

    Resolves Q23+Q24. Single composite score (0-100) + letter grade, derived from
    6 dimensions: validation (30%), evolution progression (20%), relationship
    density (15%), queue sync (10%), freshness (10%), ingestion backlog (15%).
    Plus up to 3 actionable recommendations targeting the weakest dimensions.

    Returns a JSON structure with composite_score, grade, total_pages,
    dimensions (each with score/weight/detail), and recommendations. Use
    `gateway health` CLI for a human-readable visualization.

    Unified score (not two separate methodology+quality scores) per Q24's
    "ONE composite, not vanity metrics" resolution.
    """
    from tools.gateway import resolve_paths, query_health
    paths = resolve_paths()
    result = query_health(paths)
    return json.dumps(result, indent=2, default=str)


@server.tool()
def wiki_methodology_guide() -> str:
    """Auto-detect project identity and recommend SDLC profile + methodology model + first steps.

    This is the agent-facing entry point to the Goldilocks identity protocol.
    Given the current working directory, it auto-detects:
      - domain (knowledge/typescript/python-wiki/infrastructure)
      - phase (poc/mvp/staging/production)
      - scale (micro/small/medium/large)
      - execution mode (solo/harness/fleet)
      - second-brain relationship

    Then recommends:
      - SDLC profile (simplified / default / full)
      - Available methodology models for this context
      - Concrete first steps to take (CLI commands)
      - Exploration pointers (other gateway queries to try next)

    Use this when an agent arrives fresh on a project and needs orientation
    before starting work. Wraps the CLI `gateway what-do-i-need` command.
    Declared values in CLAUDE.md take precedence over auto-detection.
    """
    from tools.gateway import resolve_paths, query_what_do_i_need
    paths = resolve_paths()
    return query_what_do_i_need(paths)


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

def main():
    server.run(transport="stdio")


if __name__ == "__main__":
    main()
