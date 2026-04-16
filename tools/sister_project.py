"""Sister-project browser — structured access to ecosystem projects' wikis.

Resolves the "how does the research wiki communicate with sister projects" gap.
Before this module, agents browsed OpenArms / OpenFleet / AICP / control-plane
with one-off Bash commands (ls, grep, cat) — manual, error-prone, and not
composable with the rest of the wiki's tooling.

This module reads sister projects declared in wiki/config/sister-projects.yaml
and exposes structured queries: list epics/tasks/logs/learnings, filter by
frontmatter fields, read specific docs, read many docs at once.

Design:
- READ-ONLY. This wiki never writes to sister projects via this tool.
- NO TRUNCATION by default. The caller gets everything. Limits are opt-in only.
- Composable with gateway subcommands and MCP tools.
- Respects per-project layout (OpenArms uses wiki/; AICP uses docs/kb/).

CLI usage:
    python3 -m tools.sister_project list                               # list all sisters
    python3 -m tools.sister_project <name> info                        # show config
    python3 -m tools.sister_project <name> epics [--status X]          # list epics
    python3 -m tools.sister_project <name> tasks [--status X --epic Y] # list tasks
    python3 -m tools.sister_project <name> logs [--since DATE]         # list dated logs
    python3 -m tools.sister_project <name> learnings                   # list learning pages
    python3 -m tools.sister_project <name> read <path>                 # read one file, FULL content
    python3 -m tools.sister_project <name> read-all <layout-key>       # read every file, FULL content
    python3 -m tools.sister_project <name> find <pattern>              # filename regex search
    python3 -m tools.sister_project <name> grep <text>                 # content search in .md files
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml
except ImportError:
    print("PyYAML not installed. Run: pip3 install pyyaml", file=sys.stderr)
    sys.exit(1)

from tools.common import get_project_root, parse_frontmatter


def load_registry() -> Dict[str, Any]:
    """Load sister-projects.yaml registry."""
    root = get_project_root()
    registry_path = root / "wiki" / "config" / "sister-projects.yaml"
    if not registry_path.exists():
        return {"projects": {}, "limits": {}}
    return yaml.safe_load(registry_path.read_text(encoding="utf-8")) or {}


def resolve_project(name: str, registry: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Look up a sister project by name; returns None if unknown."""
    return registry.get("projects", {}).get(name)


def _project_root(project_cfg: Dict[str, Any]) -> Path:
    """Return absolute path to the sister project's root directory."""
    return Path(project_cfg["path"]).expanduser().resolve()


def _wiki_root(project_cfg: Dict[str, Any]) -> Path:
    """Return absolute path to the sister project's wiki directory."""
    return _project_root(project_cfg) / project_cfg.get("wiki_dir", "wiki")


def _layout_dir(project_cfg: Dict[str, Any], dotted_key: str) -> Optional[Path]:
    """Resolve a dotted layout key like 'backlog.epics' to an absolute path.

    Also accepts a relative path directly (e.g., 'domains/learnings' or
    'wiki/domains/learnings') — resolved against the sister project's wiki root
    or project root as appropriate.
    """
    layout = project_cfg.get("layout", {})
    parts = dotted_key.split(".")
    node: Any = layout
    for part in parts:
        if isinstance(node, dict) and part in node:
            node = node[part]
        else:
            node = None
            break
    if isinstance(node, str):
        return _wiki_root(project_cfg) / node

    # Fallback: treat dotted_key as a relative path
    candidate_wiki = _wiki_root(project_cfg) / dotted_key.replace(".", "/")
    if candidate_wiki.exists() and candidate_wiki.is_dir():
        return candidate_wiki
    candidate_root = _project_root(project_cfg) / dotted_key.replace(".", "/")
    if candidate_root.exists() and candidate_root.is_dir():
        return candidate_root
    return None


def list_projects(registry: Dict[str, Any]) -> List[Dict[str, Any]]:
    """List all registered sister projects with their description + accessibility."""
    result = []
    for name, cfg in registry.get("projects", {}).items():
        path = _project_root(cfg)
        result.append({
            "name": name,
            "description": cfg.get("description", ""),
            "path": str(path),
            "accessible": path.exists(),
            "wiki_dir": str(_wiki_root(cfg)) if path.exists() else None,
        })
    return result


def project_info(project_cfg: Dict[str, Any]) -> Dict[str, Any]:
    """Return full config for a sister project + accessibility check."""
    path = _project_root(project_cfg)
    wiki_path = _wiki_root(project_cfg)
    return {
        "description": project_cfg.get("description", ""),
        "path": str(path),
        "path_exists": path.exists(),
        "wiki_dir": str(wiki_path),
        "wiki_exists": wiki_path.exists(),
        "layout": project_cfg.get("layout", {}),
        "queryable_frontmatter": project_cfg.get("queryable_frontmatter", []),
        "patterns": project_cfg.get("patterns", {}),
    }


def _read_frontmatter(path: Path) -> Dict[str, Any]:
    """Safe frontmatter parse; returns empty dict on any failure."""
    try:
        text = path.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(text)
        return meta or {}
    except Exception:
        return {}


def _list_md_files(directory: Path, pattern: Optional[str] = None) -> List[Path]:
    """List every .md file in a directory (no caps), optionally filtered by regex."""
    if not directory.exists():
        return []
    files = []
    pat = re.compile(pattern) if pattern else None
    for f in sorted(directory.iterdir()):
        if not f.is_file() or f.suffix != ".md":
            continue
        if f.name == "_index.md":
            continue
        if pat and not pat.search(f.name):
            continue
        files.append(f)
    return files


def _summarize_page(path: Path, queryable_fields: List[str]) -> Dict[str, Any]:
    """Return title + queryable frontmatter fields for a page."""
    meta = _read_frontmatter(path)
    summary = {"file": path.name, "title": meta.get("title", path.stem)}
    for field in queryable_fields:
        if field in meta:
            summary[field] = meta[field]
    return summary


def _build_consumption_index(project_cfg: Dict[str, Any], project_name: Optional[str] = None) -> set:
    """Return set of sister-project relative paths referenced by any research-wiki page.

    A sister file is considered CONSUMED if at least one page in our wiki
    references its live path. References are detected through three mechanisms:

    1. NEW (2026-04-15 directive form): structured frontmatter source entries
       with `project: X, path: Y` — the canonical portable form.
    2. Legacy absolute path in body text or frontmatter `file:` fields
       (e.g. ~/openarms/wiki/... after expansion). Deprecated; kept for back-compat
       until all wiki pages are migrated.
    3. Relative-path mentions in body text (e.g. `openarms/wiki/...`).

    Also recognizes project ALIASES declared in the registry (e.g. 'aicp' has
    alias 'devops-expert-local-ai'), so a source citing either name against the
    same underlying path counts once.

    Args:
        project_cfg: the registry entry for this project.
        project_name: optional registry KEY for this project (e.g. 'aicp').
            If provided, included in the project_names matcher list. When
            callers already know the name (e.g. iterating the projects dict),
            passing it here catches sources that cite the registry key rather
            than the directory basename.

    Returns: set of paths relative to the sister project's ROOT
    (e.g. 'wiki/domains/learnings/foo.md', 'backlog/tasks/T100.md').
    """
    project_root_abs = str(_project_root(project_cfg))
    # Project name set: registry key (preferred) + directory basename + aliases.
    # Look up the registry key by comparing project_cfg against the full registry.
    project_names: List[str] = []
    if project_name:
        project_names.append(project_name)
    else:
        try:
            registry = load_registry()
            for key, cfg in registry.get("projects", {}).items():
                if cfg is project_cfg:
                    project_names.append(key)
                    break
                # Also match by path — handles deep-copy-of-config cases
                if cfg.get("path") == project_cfg.get("path"):
                    project_names.append(key)
                    break
        except Exception:
            pass
    basename = Path(project_root_abs).name
    if basename and basename not in project_names:
        project_names.append(basename)
    for alias in project_cfg.get("aliases", []) or []:
        if alias and alias not in project_names:
            project_names.append(alias)

    our_root = get_project_root()
    our_wiki = our_root / "wiki"
    if not our_wiki.exists():
        return set()

    consumed: set = set()
    abs_re = re.compile(rf'{re.escape(project_root_abs)}/([\w\-/.]+\.md)')
    # Relative match: any of our project names as path-prefix, matching .md file
    rel_alternation = "|".join(re.escape(n) for n in project_names)
    rel_re = re.compile(rf'(?:^|[^\w\-/])(?:{rel_alternation})/([\w\-/.]+\.md)')

    for md in our_wiki.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        # Regex sweeps — catch body text + frontmatter absolute/relative mentions
        for m in abs_re.finditer(text):
            consumed.add(m.group(1))
        for m in rel_re.finditer(text):
            consumed.add(m.group(1))
        # Structured sweep — parse frontmatter sources[] for project+path pairs
        try:
            meta, _body = parse_frontmatter(text)
        except Exception:
            continue
        if not meta:
            continue
        for src in meta.get("sources", []) or []:
            if not isinstance(src, dict):
                continue
            src_project = src.get("project")
            src_path = src.get("path")
            if src_project and src_path and src_project in project_names:
                consumed.add(str(src_path))

    return consumed


def _rel_to_project(project_cfg: Dict[str, Any], file_path: Path) -> str:
    """Normalize a sister-project file path to its relative form (for consumption check).

    Calls .resolve() on the file path so layout entries containing '..' segments
    (e.g. '../docs/systems' when wiki_dir is 'wiki') normalize correctly before
    relative_to compares them to the resolved project root.
    """
    try:
        return str(file_path.resolve().relative_to(_project_root(project_cfg)))
    except ValueError:
        return str(file_path)


def list_epics(project_cfg: Dict[str, Any], status_filter: Optional[str] = None, show_all: bool = False) -> List[Dict[str, Any]]:
    """List epics in the sister project; optionally filter by status.

    DEFAULT: returns only UNCONSUMED epics (those not referenced by any page
    in our research-wiki). Pass show_all=True to return every epic regardless
    of consumption status. No cap on either mode. Per the higher-ground
    principle: sister content is input to OUR synthesis; the differential
    view surfaces what we have not yet looked at.

    Each result item gains a 'consumed' bool field indicating whether our
    wiki references that epic's live path.
    """
    epics_dir = _layout_dir(project_cfg, "backlog.epics")
    if epics_dir is None:
        return []
    fields = project_cfg.get("queryable_frontmatter", [])
    files = _list_md_files(epics_dir)
    consumed = _build_consumption_index(project_cfg)
    result = []
    for f in files:
        rel = _rel_to_project(project_cfg, f)
        is_consumed = rel in consumed
        if not show_all and is_consumed:
            continue
        summary = _summarize_page(f, fields)
        if status_filter and summary.get("status") != status_filter:
            continue
        summary["consumed"] = is_consumed
        result.append(summary)
    return result


def list_tasks(project_cfg: Dict[str, Any], status_filter: Optional[str] = None, epic_filter: Optional[str] = None, show_all: bool = False) -> List[Dict[str, Any]]:
    """List tasks in the sister project; optionally filter by status and/or epic.

    DEFAULT: returns only UNCONSUMED tasks. Pass show_all=True for everything.
    See list_epics docstring for the full semantics.
    """
    tasks_dir = _layout_dir(project_cfg, "backlog.tasks")
    if tasks_dir is None:
        return []
    fields = project_cfg.get("queryable_frontmatter", [])
    files = _list_md_files(tasks_dir)
    consumed = _build_consumption_index(project_cfg)
    result = []
    for f in files:
        rel = _rel_to_project(project_cfg, f)
        is_consumed = rel in consumed
        if not show_all and is_consumed:
            continue
        summary = _summarize_page(f, fields)
        if status_filter and summary.get("status") != status_filter:
            continue
        if epic_filter and summary.get("epic") != epic_filter:
            continue
        summary["consumed"] = is_consumed
        result.append(summary)
    return result


def list_logs(project_cfg: Dict[str, Any], since: Optional[str] = None, show_all: bool = False) -> List[Dict[str, Any]]:
    """List dated logs, newest first; optionally filter to entries on/after `since`.

    DEFAULT: returns only UNCONSUMED logs. Pass show_all=True for everything.
    See list_epics docstring for the full semantics.
    """
    logs_dir = _layout_dir(project_cfg, "logs")
    if logs_dir is None:
        return []
    fields = project_cfg.get("queryable_frontmatter", [])
    files = sorted(
        (f for f in logs_dir.iterdir() if f.is_file() and f.suffix == ".md" and f.name != "_index.md"),
        reverse=True,
    )
    consumed = _build_consumption_index(project_cfg)
    result = []
    for f in files:
        rel = _rel_to_project(project_cfg, f)
        is_consumed = rel in consumed
        if not show_all and is_consumed:
            continue
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", f.name)
        file_date = date_match.group(1) if date_match else None
        if since and file_date and file_date < since:
            continue
        summary = _summarize_page(f, fields)
        summary["date"] = file_date
        summary["consumed"] = is_consumed
        result.append(summary)
    return result


def list_learnings(project_cfg: Dict[str, Any], show_all: bool = False) -> List[Dict[str, Any]]:
    """List distilled learnings (lessons, patterns, findings).

    DEFAULT: returns only UNCONSUMED learnings. Pass show_all=True for everything.
    See list_epics docstring for the full semantics.

    IMPORTANT: 'consumed' means the sister-project path is referenced by any
    research-wiki page — it does NOT mean the claim is validated. Sister
    lessons are weak signals to investigate, not ground truth to mirror.
    See raw/notes/2026-04-15-directive-openarms-was-dumb-verify-independently.md
    """
    learnings_dir = _layout_dir(project_cfg, "domains.learnings")
    if learnings_dir is None:
        return []
    fields = project_cfg.get("queryable_frontmatter", [])
    files = _list_md_files(learnings_dir)
    consumed = _build_consumption_index(project_cfg)
    result = []
    for f in files:
        rel = _rel_to_project(project_cfg, f)
        is_consumed = rel in consumed
        if not show_all and is_consumed:
            continue
        summary = _summarize_page(f, fields)
        summary["consumed"] = is_consumed
        result.append(summary)
    return result


def _flatten_layout_keys(layout: Any, prefix: str = "") -> List[str]:
    """Walk the project's layout dict and return every leaf key as a dotted path.

    Layouts declared in sister-projects.yaml can nest arbitrarily. This
    traversal lets the absorption summary cover every declared section
    without a hardcoded key list — flexibility per the wiki's menu-not-law
    principle applied to the tool's own registry.
    """
    keys: List[str] = []
    if isinstance(layout, dict):
        for k, v in layout.items():
            sub = f"{prefix}.{k}" if prefix else k
            if isinstance(v, dict):
                keys.extend(_flatten_layout_keys(v, sub))
            elif isinstance(v, str):
                keys.append(sub)
    return keys


def consumption_summary(project_cfg: Dict[str, Any]) -> Dict[str, Any]:
    """Return a breakdown of consumed vs unconsumed files across ALL declared layout dirs.

    Iterates over every leaf key in the project's layout registry (not a
    hardcoded list), so adding a new layout key in sister-projects.yaml
    automatically shows up here. Consumed = referenced by any page in our
    research-wiki. Does NOT mean validated — see list_learnings docstring.
    """
    consumed = _build_consumption_index(project_cfg)
    sections = {}
    layout = project_cfg.get("layout", {})
    for layout_key in _flatten_layout_keys(layout):
        d = _layout_dir(project_cfg, layout_key)
        # Skip layout entries that point at individual files rather than
        # directories (e.g. openarms config.methodology → config/methodology.yaml).
        # Those file-sentinels are not absorption-tracked as directories; if
        # their consumption matters, it's surfaced via total_consumed_paths.
        if d is None or not d.exists() or not d.is_dir():
            continue
        files = _list_md_files(d)
        total = len(files)
        absorbed = sum(1 for f in files if _rel_to_project(project_cfg, f) in consumed)
        sections[layout_key] = {
            "total": total,
            "consumed": absorbed,
            "unconsumed": total - absorbed,
            "absorption_pct": round(100 * absorbed / total, 1) if total else 0.0,
        }
    return {
        "project_root": str(_project_root(project_cfg)),
        "total_consumed_paths": len(consumed),
        "by_layout": sections,
        "note": "'consumed' = referenced by a research-wiki page. This is NOT validation. "
                "Sister claims remain weak signals until independently verified. See "
                "raw/notes/2026-04-15-directive-openarms-was-dumb-verify-independently.md",
    }


def read_doc(project_cfg: Dict[str, Any], relative_path: str) -> Dict[str, Any]:
    """Read a single doc from the sister project — FULL CONTENT, no truncation.

    `relative_path` is interpreted relative to the project root (NOT wiki root),
    so callers can read CLAUDE.md, AGENTS.md, wiki/..., docs/... transparently.
    """
    root = _project_root(project_cfg)
    target = (root / relative_path).resolve()
    # Safety: reject paths that escape the project root
    try:
        target.relative_to(root)
    except ValueError:
        return {"error": f"Path escapes project root: {relative_path}", "path": relative_path}
    if not target.exists():
        return {"error": "Not found", "path": str(target)}
    if not target.is_file():
        return {"error": "Not a file (is a directory?)", "path": str(target)}

    content = target.read_text(encoding="utf-8", errors="replace")
    meta = _read_frontmatter(target) if target.suffix == ".md" else {}
    return {
        "path": str(target.relative_to(root)),
        "size_bytes": len(content.encode("utf-8")),
        "frontmatter": meta,
        "content": content,
    }


def read_all(
    project_cfg: Dict[str, Any],
    layout_key: str,
    name_pattern: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Read FULL content of every .md file in a layout directory.

    This is the action you use when you want the actual lessons, not summaries.
    No truncation, no section extraction, no char caps. Full body of every file.

    Args:
        layout_key: dotted layout key (e.g., "domains.learnings") OR a relative
                    path like "wiki/domains/learnings" — _layout_dir handles both.
        name_pattern: optional regex filter on filename.

    Returns: list of {path, size_bytes, frontmatter, content} — one entry per file.
    """
    target_dir = _layout_dir(project_cfg, layout_key)
    if target_dir is None or not target_dir.exists():
        return [{"error": f"Directory not found: {layout_key}"}]

    root = _project_root(project_cfg)
    files = _list_md_files(target_dir, pattern=name_pattern)
    results = []
    for f in files:
        try:
            content = f.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            results.append({"path": str(f.relative_to(root)), "error": str(e)})
            continue
        meta = _read_frontmatter(f)
        results.append({
            "path": str(f.relative_to(root)),
            "size_bytes": len(content.encode("utf-8")),
            "frontmatter": meta,
            "content": content,
        })
    return results


def find_by_filename(project_cfg: Dict[str, Any], pattern: str) -> List[str]:
    """Find files under the sister project whose filenames match `pattern` (regex).

    No cap. Returns every match. Walks the whole project (not just wiki/).
    """
    root = _project_root(project_cfg)
    if not root.exists():
        return []
    pat = re.compile(pattern)
    results = []
    for md in root.rglob("*"):
        if not md.is_file():
            continue
        if pat.search(md.name):
            results.append(str(md.relative_to(root)))
    return results


def grep_content(project_cfg: Dict[str, Any], text: str) -> List[Dict[str, Any]]:
    """Grep sister-project .md files for literal `text`; returns path + ALL matching lines.

    No cap on matches per file or total. Scoped to wiki_dir (not full project
    root — avoids code files, dist/, node_modules/).
    """
    wiki = _wiki_root(project_cfg)
    if not wiki.exists():
        return []
    results = []
    text_lower = text.lower()
    for md in wiki.rglob("*.md"):
        try:
            content = md.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        matches = []
        for i, line in enumerate(content.split("\n"), 1):
            if text_lower in line.lower():
                matches.append({"line": i, "text": line})
        if matches:
            results.append({
                "path": str(md.relative_to(_project_root(project_cfg))),
                "matches": matches,
            })
    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Sister-project browser — structured access to ecosystem projects' wikis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("project", nargs="?", help="Sister project name (or 'list' to list all)")
    parser.add_argument("action", nargs="?", help="Action: info, epics, tasks, logs, learnings, summary, read, read-all, find, grep")
    parser.add_argument("arg", nargs="?", help="Argument for the action (path, pattern, or text)")
    parser.add_argument("--status", help="Filter by status (for epics/tasks) OR filename regex (for read-all)")
    parser.add_argument("--epic", help="Filter tasks by epic")
    parser.add_argument("--since", help="Filter logs to entries on/after this date (YYYY-MM-DD)")
    parser.add_argument("--all", dest="show_all", action="store_true",
                        help="Show ALL items including already-consumed ones. Default: only unconsumed (differential view).")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of human-readable")
    args = parser.parse_args()

    registry = load_registry()

    if args.project in (None, "list", "--help"):
        projects = list_projects(registry)
        if args.json:
            print(json.dumps(projects, indent=2, default=str))
        else:
            print(f"\nSister Projects ({len(projects)})")
            print("=" * 60)
            for p in projects:
                status = "✓" if p["accessible"] else "✗ (not accessible)"
                print(f"  {status}  {p['name']:20s}  {p['description']}")
            print()
            print("Usage: python3 -m tools.sister_project <name> <action>")
            print("Actions: info | epics | tasks | logs | learnings | read <path> | read-all <layout-key> | find <pattern> | grep <text>")
            print("")
            print("read-all: read FULL content of every .md in a layout dir. One call, no truncation.")
            print("  Example: sister_project openarms read-all domains.learnings --status '^lesson-'")
        return

    project_cfg = resolve_project(args.project, registry)
    if project_cfg is None:
        print(f"Unknown sister project: {args.project}", file=sys.stderr)
        print(f"Known: {', '.join(registry.get('projects', {}).keys())}", file=sys.stderr)
        sys.exit(1)

    if not _project_root(project_cfg).exists():
        print(f"Sister project '{args.project}' path does not exist: {_project_root(project_cfg)}", file=sys.stderr)
        sys.exit(1)

    action = args.action or "info"

    if action == "info":
        result = project_info(project_cfg)
    elif action == "epics":
        result = list_epics(project_cfg, status_filter=args.status, show_all=args.show_all)
    elif action == "tasks":
        result = list_tasks(project_cfg, status_filter=args.status, epic_filter=args.epic, show_all=args.show_all)
    elif action == "logs":
        result = list_logs(project_cfg, since=args.since, show_all=args.show_all)
    elif action == "learnings":
        result = list_learnings(project_cfg, show_all=args.show_all)
    elif action == "summary":
        result = consumption_summary(project_cfg)
    elif action in ("read-all", "read_all", "readall"):
        if not args.arg:
            print("Usage: sister_project <name> read-all <layout-key> [--status regex]", file=sys.stderr)
            sys.exit(1)
        result = read_all(project_cfg, args.arg, name_pattern=args.status)
    elif action == "read":
        if not args.arg:
            print("Usage: sister_project <name> read <relative/path.md>", file=sys.stderr)
            sys.exit(1)
        result = read_doc(project_cfg, args.arg)
    elif action == "find":
        if not args.arg:
            print("Usage: sister_project <name> find <regex-pattern>", file=sys.stderr)
            sys.exit(1)
        result = find_by_filename(project_cfg, args.arg)
    elif action == "grep":
        if not args.arg:
            print("Usage: sister_project <name> grep <text>", file=sys.stderr)
            sys.exit(1)
        result = grep_content(project_cfg, args.arg)
    else:
        print(f"Unknown action: {action}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        if isinstance(result, list):
            # read-all returns a list of {path, content, frontmatter}
            if result and isinstance(result[0], dict) and "content" in result[0]:
                for item in result:
                    print("=" * 70)
                    print(f"FILE: {item['path']} ({item.get('size_bytes', 0)} bytes)")
                    print("=" * 70)
                    print(item["content"])
                    print()
                print(f"\n--- {len(result)} file(s) ---")
            else:
                print(f"\n{args.project} / {action} — {len(result)} item(s)")
                print("=" * 60)
                for item in result:
                    if isinstance(item, dict):
                        title = item.get("title", item.get("file", "?"))
                        bits = [title]
                        for f in ("status", "readiness", "current_stage", "epic", "date"):
                            if f in item:
                                bits.append(f"{f}={item[f]}")
                        print(f"  {' | '.join(bits)}")
                    else:
                        print(f"  {item}")
                print()
        elif isinstance(result, dict) and "content" in result:
            print(f"\n=== {result['path']} ({result['size_bytes']} bytes) ===\n")
            if result.get("frontmatter"):
                print(f"Frontmatter: {json.dumps(result['frontmatter'], default=str)}\n")
            print(result["content"])
        else:
            print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
