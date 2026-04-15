"""Source resolver — project-based source reference resolution with multi-backend fallback.

Implements the source-mechanism directive from 2026-04-15:
    "The source mechanism should work by project with optional additional aliases.
     Instead of using the absolute path with the username we can produce the right
     logic since they logically all share the same parent folder... functioning by
     project allows to add the git remote and when the project is not there we can
     do queries using gh and curl or curl equivalents..."

A wiki page's frontmatter can reference a sister-project source in three forms:

    # External URL — existing form
    sources:
      - id: foo
        type: article
        url: https://example.com/article

    # Legacy absolute path or project-relative — existing form
    sources:
      - id: bar
        type: observation
        file: raw/articles/openarms-readme.md      # project-relative
        # OR (deprecated, migrate):
        file: /home/jfortin/openarms/wiki/...      # absolute path

    # NEW: project + path form
    sources:
      - id: baz
        type: observation
        project: openarms
        path: wiki/domains/architecture/agent-behavior-environment-patching-findings.md
        aliases: [env-patching-t107]      # optional
        description: "..."

The resolver reads wiki/config/sister-projects.yaml to locate `project`, then tries
three backends in order until one succeeds:

    1. LOCAL    — read from {project.path}/{source.path} after ~/ expansion
    2. GH_API   — `gh api repos/{owner}/{repo}/contents/{path}` (if gh CLI authenticated)
    3. RAW      — https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}

Each attempt returns a structured Receipt (never raises — per Adapters Never Raise pattern).
The overall resolution returns {ok, backend, content?, error?, tried: [...]}.

This module is pure Python; no external dependencies beyond the standard library.
It does NOT require `gh` or `curl` to be installed — those backends degrade gracefully.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

from tools.common import get_project_root

try:
    import yaml
except ImportError:  # pragma: no cover — yaml is always present in this repo
    yaml = None  # type: ignore


# ---------------------------------------------------------------------------
# Registry loading
# ---------------------------------------------------------------------------

def load_sister_registry(project_root: Optional[Path] = None) -> Dict[str, Any]:
    """Load wiki/config/sister-projects.yaml. Returns {} if missing."""
    if project_root is None:
        project_root = get_project_root()
    path = project_root / "wiki" / "config" / "sister-projects.yaml"
    if not path.exists() or yaml is None:
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def resolve_project_cfg(project_name: str, registry: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Find a project config by name OR alias. Returns None if unknown."""
    projects = registry.get("projects", {})
    # Direct name match
    if project_name in projects:
        return projects[project_name]
    # Alias match
    for name, cfg in projects.items():
        aliases = cfg.get("aliases", []) or []
        if project_name in aliases:
            return cfg
    return None


# ---------------------------------------------------------------------------
# Receipts (per Adapters Never Raise — structured, not exceptions)
# ---------------------------------------------------------------------------

def _receipt_ok(backend: str, content: str, **extra: Any) -> Dict[str, Any]:
    return {"ok": True, "backend": backend, "content": content, **extra}


def _receipt_fail(backend: str, error: str, **extra: Any) -> Dict[str, Any]:
    return {"ok": False, "backend": backend, "error": error, **extra}


# ---------------------------------------------------------------------------
# Backend 1 — LOCAL filesystem
# ---------------------------------------------------------------------------

def _try_local(project_cfg: Dict[str, Any], source_path: str) -> Dict[str, Any]:
    """Attempt to read {project.path}/{source_path} from the local filesystem."""
    raw_path = project_cfg.get("path")
    if not raw_path:
        return _receipt_fail("local", "project config has no 'path' field")
    project_root = Path(raw_path).expanduser().resolve()
    if not project_root.exists():
        return _receipt_fail(
            "local",
            f"project root not found locally: {project_root}",
            project_root=str(project_root),
        )
    target = (project_root / source_path).resolve()
    # Path-escape safety — target must be inside project_root
    try:
        target.relative_to(project_root)
    except ValueError:
        return _receipt_fail(
            "local",
            f"path escapes project root: {source_path}",
            project_root=str(project_root),
        )
    if not target.exists():
        return _receipt_fail(
            "local",
            f"file not found: {target}",
            project_root=str(project_root),
            target=str(target),
        )
    if not target.is_file():
        return _receipt_fail(
            "local",
            f"target is not a file: {target}",
            target=str(target),
        )
    try:
        content = target.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return _receipt_fail("local", f"read failed: {e}", target=str(target))
    return _receipt_ok(
        "local",
        content,
        source_path=source_path,
        resolved_path=str(target),
        size_bytes=len(content.encode("utf-8")),
    )


# ---------------------------------------------------------------------------
# Backend 2 — GitHub via gh CLI
# ---------------------------------------------------------------------------

def _gh_available() -> bool:
    """Check if gh CLI is present and (loosely) authenticated."""
    if shutil.which("gh") is None:
        return False
    # `gh auth status` returns 0 if authenticated, non-zero otherwise
    try:
        r = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True, text=True, timeout=5,
        )
        return r.returncode == 0
    except (subprocess.TimeoutExpired, OSError):
        return False


def _try_gh_api(project_cfg: Dict[str, Any], source_path: str) -> Dict[str, Any]:
    """Attempt to read via `gh api repos/{owner}/{repo}/contents/{path}`."""
    remote = project_cfg.get("remote") or {}
    owner = remote.get("owner")
    repo = remote.get("repo")
    branch = remote.get("default_branch", "main")
    if not owner or not repo:
        return _receipt_fail(
            "gh_api",
            "project config has no 'remote.owner' or 'remote.repo'",
        )
    if not _gh_available():
        return _receipt_fail(
            "gh_api",
            "gh CLI not available or not authenticated",
            owner=owner, repo=repo,
        )
    gh_path = f"repos/{owner}/{repo}/contents/{source_path}"
    try:
        r = subprocess.run(
            ["gh", "api", gh_path, "-q", ".content",
             "--header", f"X-GitHub-Api-Version: 2022-11-28"],
            capture_output=True, text=True, timeout=15,
        )
    except (subprocess.TimeoutExpired, OSError) as e:
        return _receipt_fail("gh_api", f"gh invocation failed: {e}", owner=owner, repo=repo)
    if r.returncode != 0:
        return _receipt_fail(
            "gh_api",
            f"gh api returned {r.returncode}: {r.stderr.strip()[:200]}",
            owner=owner, repo=repo, path=source_path,
        )
    # gh api -q .content returns base64-encoded content
    import base64
    try:
        decoded = base64.b64decode(r.stdout.strip()).decode("utf-8", errors="replace")
    except Exception as e:
        return _receipt_fail("gh_api", f"base64 decode failed: {e}", owner=owner, repo=repo)
    return _receipt_ok(
        "gh_api",
        decoded,
        owner=owner,
        repo=repo,
        branch=branch,
        source_path=source_path,
        size_bytes=len(decoded.encode("utf-8")),
    )


# ---------------------------------------------------------------------------
# Backend 3 — Raw GitHub URL
# ---------------------------------------------------------------------------

def _try_raw_github(project_cfg: Dict[str, Any], source_path: str, timeout: int = 10) -> Dict[str, Any]:
    """Attempt to read via https://raw.githubusercontent.com/... (public repos only)."""
    remote = project_cfg.get("remote") or {}
    owner = remote.get("owner")
    repo = remote.get("repo")
    branch = remote.get("default_branch", "main")
    if not owner or not repo:
        return _receipt_fail(
            "raw_github",
            "project config has no 'remote.owner' or 'remote.repo'",
        )
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{source_path}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "devops-solutions-research-wiki/source_resolver"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status != 200:
                return _receipt_fail(
                    "raw_github",
                    f"HTTP {resp.status}",
                    url=url,
                )
            content = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return _receipt_fail("raw_github", f"HTTP {e.code}: {e.reason}", url=url)
    except urllib.error.URLError as e:
        return _receipt_fail("raw_github", f"URL error: {e.reason}", url=url)
    except Exception as e:
        return _receipt_fail("raw_github", f"unexpected error: {e}", url=url)
    return _receipt_ok(
        "raw_github",
        content,
        owner=owner,
        repo=repo,
        branch=branch,
        url=url,
        source_path=source_path,
        size_bytes=len(content.encode("utf-8")),
    )


# ---------------------------------------------------------------------------
# Public API — resolve_source()
# ---------------------------------------------------------------------------

# Map of backend name → function
_BACKENDS = {
    "local": _try_local,
    "gh_api": _try_gh_api,
    "raw_github": _try_raw_github,
}


def resolve_source(
    source_entry: Dict[str, Any],
    registry: Optional[Dict[str, Any]] = None,
    backends: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Resolve a source entry to content via local/gh/raw fallback.

    Args:
        source_entry: a sources[] dict from wiki frontmatter. Must contain either
            `project` + `path` (new form), or `file` / `url` (legacy forms).
        registry: parsed sister-projects.yaml; if None, loaded from disk.
        backends: override resolution order. Default: read from
            registry["source_resolution"]["backends"] or ["local", "gh_api", "raw_github"].

    Returns: structured Receipt dict:
        {
          "ok": bool,
          "backend": str | None,        # which backend succeeded (if any)
          "content": str | None,        # file content if ok=True
          "source_path": str,           # the path that was resolved
          "project": str,               # project name (if project+path form)
          "tried": [list of attempt receipts],
          "error": str | None,          # summary error if all backends failed
        }

    This function NEVER raises. All failures land in the returned receipt.
    """
    if registry is None:
        registry = load_sister_registry()

    # Route by source form
    if "url" in source_entry:
        return {
            "ok": True,
            "backend": "external_url",
            "content": None,  # external URLs aren't fetched here — just acknowledged
            "url": source_entry["url"],
            "source_entry_id": source_entry.get("id"),
            "note": "External URL — resolver does not fetch; consumer must handle.",
        }

    project_name = source_entry.get("project")
    source_path = source_entry.get("path")

    # Legacy 'file:' handling — if it's an absolute path or starts with project name,
    # attempt to infer project from the path.
    if not project_name and "file" in source_entry:
        legacy_file = source_entry["file"]
        inferred = _infer_project_from_legacy_path(legacy_file, registry)
        if inferred:
            project_name, source_path = inferred
        else:
            # Cannot convert — treat as project-root-relative file (our raw/articles/... etc.)
            return {
                "ok": False,
                "backend": None,
                "content": None,
                "file": legacy_file,
                "source_entry_id": source_entry.get("id"),
                "error": (
                    "Legacy 'file:' form with no inferrable project. "
                    "Either migrate to project+path form, or read this file "
                    "directly (the resolver only handles cross-project sources)."
                ),
            }

    if not project_name or not source_path:
        return {
            "ok": False,
            "backend": None,
            "content": None,
            "source_entry_id": source_entry.get("id"),
            "error": f"Source entry needs both 'project' and 'path' fields (got project={project_name!r}, path={source_path!r}).",
        }

    project_cfg = resolve_project_cfg(project_name, registry)
    if project_cfg is None:
        return {
            "ok": False,
            "backend": None,
            "content": None,
            "project": project_name,
            "source_path": source_path,
            "source_entry_id": source_entry.get("id"),
            "error": f"Unknown project: {project_name!r}. Known: {list(registry.get('projects', {}).keys())}",
        }

    # Determine backend order
    if backends is None:
        resolution_cfg = registry.get("source_resolution", {}) or {}
        backends = resolution_cfg.get("backends") or ["local", "gh_api", "raw_github"]

    tried: List[Dict[str, Any]] = []
    for backend_name in backends:
        fn = _BACKENDS.get(backend_name)
        if fn is None:
            tried.append(_receipt_fail(backend_name, "unknown backend"))
            continue
        receipt = fn(project_cfg, source_path)
        tried.append(receipt)
        if receipt.get("ok"):
            return {
                "ok": True,
                "backend": backend_name,
                "content": receipt["content"],
                "project": project_name,
                "source_path": source_path,
                "source_entry_id": source_entry.get("id"),
                "tried": tried,
                "size_bytes": receipt.get("size_bytes"),
            }

    # All backends failed
    return {
        "ok": False,
        "backend": None,
        "content": None,
        "project": project_name,
        "source_path": source_path,
        "source_entry_id": source_entry.get("id"),
        "tried": tried,
        "error": "All backends failed. See 'tried' for per-backend errors.",
    }


def _infer_project_from_legacy_path(
    legacy_file: str, registry: Dict[str, Any]
) -> Optional[tuple]:
    """Given an absolute path like /home/jfortin/openarms/wiki/foo.md,
    try to match against a project's configured path (after ~/ expansion).

    Returns (project_name, relative_path) or None.
    """
    if not legacy_file:
        return None
    legacy_path = Path(legacy_file).expanduser().resolve() if legacy_file.startswith(("/", "~")) else None
    if legacy_path is None:
        return None
    projects = registry.get("projects", {})
    for name, cfg in projects.items():
        raw_path = cfg.get("path")
        if not raw_path:
            continue
        try:
            proj_root = Path(raw_path).expanduser().resolve()
        except Exception:
            continue
        try:
            rel = legacy_path.relative_to(proj_root)
            return name, str(rel)
        except ValueError:
            continue
    return None


# ---------------------------------------------------------------------------
# CLI — for ad-hoc testing
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(
        description="Source resolver — resolve project+path source entries to content via local/gh/raw fallback."
    )
    parser.add_argument("project", help="Sister project name (e.g., 'openarms')")
    parser.add_argument("path", help="Path within project (e.g., 'wiki/domains/learnings/foo.md')")
    parser.add_argument("--backends", nargs="+",
                        help="Override backend order. Default: [local, gh_api, raw_github]")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--preview", type=int, default=500,
                        help="Chars of content to preview in non-JSON mode (default 500)")
    args = parser.parse_args()

    receipt = resolve_source(
        {"id": "cli-resolve", "type": "observation",
         "project": args.project, "path": args.path},
        backends=args.backends,
    )

    if args.json:
        # Strip content from JSON if too large (for readable output)
        r = dict(receipt)
        if r.get("content") and len(r["content"]) > args.preview:
            r["content"] = r["content"][:args.preview] + "... [truncated for CLI display]"
        print(json.dumps(r, indent=2, default=str))
        return

    if receipt.get("ok"):
        print(f"✓ Resolved via {receipt['backend']}  ({receipt.get('size_bytes', 0)} bytes)")
        content = receipt.get("content", "")
        preview = content[: args.preview]
        print(f"\n--- Preview (first {args.preview} chars) ---\n{preview}")
        if len(content) > args.preview:
            print(f"\n... [{len(content) - args.preview} more chars not shown] ...")
    else:
        print(f"✗ All backends failed for {args.project}:{args.path}")
        for attempt in receipt.get("tried", []):
            print(f"  [{attempt.get('backend')}] {attempt.get('error')}")


if __name__ == "__main__":
    main()
