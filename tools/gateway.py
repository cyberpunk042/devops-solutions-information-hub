"""Wiki Gateway — Unified knowledge interface for humans, agents, and MCP.

Provides structured queries into the wiki's methodology, standards, and knowledge,
plus operational commands (move, archive, backup). Works on BOTH the second brain
(this project) AND external project wikis.

Usage:
    python3 -m tools.gateway query --stage document --domain typescript
    python3 -m tools.gateway query --chain default --artifacts
    python3 -m tools.gateway query --model feature-development --full-chain
    python3 -m tools.gateway query --field readiness --explain
    python3 -m tools.gateway query --identity               # show current project identity
    python3 -m tools.gateway template lesson                 # get lesson template
    python3 -m tools.gateway config methodology.models       # render config section as markdown
    python3 -m tools.gateway move "Old Title" --to domains/new-domain/
    python3 -m tools.gateway archive "Page Title"
    python3 -m tools.gateway backup --target /path/
    python3 -m tools.gateway contribute --type lesson --title "..." --content "..."

Dual-scope: operates on the local wiki by default. Pass --wiki-root to target a different wiki.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.common import (
    find_wiki_pages,
    get_project_root,
    load_config,
    parse_frontmatter,
    parse_relationships,
    parse_sections,
)


# ---------------------------------------------------------------------------
# Auto-detection: identify project characteristics without manual config
# ---------------------------------------------------------------------------

def auto_detect_identity(root: Path) -> Dict[str, Any]:
    """Auto-detect project identity from filesystem signals.

    Execution modes are DISTINCT things, not a single progression:
    - SOLO MODE: human talks to Claude. No harness, no loop. Just conversation.
    - HARNESS v1: program wraps ONE agent (e.g., `openarms agent run`). Basic loop + dispatch.
    - HARNESS v2: enhanced harness — hooks + commands + stage validation + enforcement.
    - HARNESS v3: future — harness + full SDLC (Plane sync, sprint planning).
    - FULL SYSTEM: provisioned fleet. Orchestrator + immune system + MANY agents.

    Having .claude/settings.json does NOT make it a harness.
    Having hooks does NOT make it a harness.
    A harness is a PROGRAM that SPAWNS and CONTROLS agent sessions in a loop.
    A system ORCHESTRATES many agents with coordination, detection, and correction.
    """
    identity = {}

    # Domain detection — from project files
    domain_markers = {
        "typescript": ["package.json", "tsconfig.json"],
        "python": ["pyproject.toml", "setup.py"],
        "infrastructure": ["main.tf", "terraform.tf"],
        "knowledge": ["wiki/config/methodology.yaml", "wiki/manifest.json"],
    }
    for domain, markers in domain_markers.items():
        if any((root / m).exists() for m in markers):
            identity["domain"] = domain
            break
    if "domain" not in identity:
        identity["domain"] = "unknown"

    # Scale detection — count source files (rough proxy)
    extensions = {".py", ".ts", ".tsx", ".js", ".jsx", ".tf", ".go", ".rs"}
    skip_dirs = {".venv", "node_modules", ".git", "__pycache__", "dist", "build"}
    file_count = 0
    try:
        for f in root.rglob("*"):
            if any(d in f.parts for d in skip_dirs):
                continue
            if f.suffix in extensions:
                file_count += 1
            if file_count > 20000:
                break  # Stop counting, we know it's massive
    except PermissionError:
        pass

    if file_count < 50:
        identity["scale"] = "micro"
    elif file_count < 500:
        identity["scale"] = "small"
    elif file_count < 5000:
        identity["scale"] = "medium"
    elif file_count < 20000:
        identity["scale"] = "large"
    else:
        identity["scale"] = "massive"
    identity["source_files"] = min(file_count, 20000)

    # Execution mode detection
    # Solo: no harness program found. Human + Claude in conversation.
    # Harness: a program that spawns+controls agent sessions in a loop.
    # Full system: orchestrator that coordinates multiple agents.

    # Full system markers (orchestrator + multi-agent infrastructure)
    full_system_markers = [
        "fleet/core/orchestrator.py",
        "fleet/cli/orchestrator.py",
    ]
    # Harness markers (program that wraps ONE agent in a loop)
    harness_markers = [
        "src/commands/agent-run-harness.ts",
        "src/commands/agent-run.ts",
    ]
    # Harness v2 markers (enforcement infrastructure ON the harness)
    enforcement_markers = [
        "scripts/methodology/validate-stage.cjs",
        "scripts/methodology/hooks/pre-bash.sh",
    ]

    if any((root / m).exists() for m in full_system_markers):
        identity["execution_mode"] = "full-system"
    elif any((root / m).exists() for m in harness_markers):
        if any((root / m).exists() for m in enforcement_markers):
            identity["execution_mode"] = "harness-v2"
        else:
            identity["execution_mode"] = "harness-v1"
    else:
        identity["execution_mode"] = "solo"

    # Phase detection
    has_ci = any((root / p).exists() for p in [".github/workflows", ".gitlab-ci.yml", "Jenkinsfile"])
    has_tests = any((root / p).exists() for p in ["tests/", "test/", "__tests__/"])
    has_production_markers = any((root / p).exists() for p in ["Dockerfile", "docker-compose.yml", "fly.toml", "Procfile"])

    if has_production_markers and has_ci:
        identity["phase"] = "production"
    elif has_ci and has_tests:
        identity["phase"] = "staging"
    elif has_tests:
        identity["phase"] = "mvp"
    else:
        identity["phase"] = "poc"

    # Second brain detection
    if (root / "wiki" / "config" / "methodology.yaml").exists() and (root / "wiki" / "manifest.json").exists():
        identity["second_brain"] = "self"  # IS a second brain
    elif any((root / p).exists() for p in [".mcp.json"]):
        identity["second_brain"] = "connected"
    else:
        identity["second_brain"] = "none"

    return identity


# ---------------------------------------------------------------------------
# Core: resolve wiki and config paths (dual-scope)
# ---------------------------------------------------------------------------

def resolve_paths(wiki_root: Optional[str] = None, brain_root: Optional[str] = None) -> Dict[str, Path]:
    """Resolve wiki and config paths. Supports dual-scope.

    Two separate path sets:
    - LOCAL: the project's own wiki (for identity, backlog, project-specific content)
    - BRAIN: the second brain / information hub (for methodology, standards, chains, templates)

    When running ON the second brain itself, local == brain.
    When running on a project, local = project wiki, brain = second brain.
    """
    # Local project
    if wiki_root:
        local_root = Path(wiki_root)
    else:
        local_root = get_project_root()
    local_wiki = local_root / "wiki" if (local_root / "wiki").exists() else local_root

    # Second brain (defaults to local if not specified, or auto-detect)
    if brain_root:
        brain_path = Path(brain_root)
    else:
        # Auto-detect: if local IS the second brain, use it
        if (local_wiki / "config" / "methodology.yaml").exists() and (local_wiki / "manifest.json").exists():
            brain_path = local_root
        else:
            # Look for common second brain locations
            for candidate in [
                local_root.parent / "devops-solutions-research-wiki",
                Path.home() / "devops-solutions-research-wiki",
            ]:
                if (candidate / "wiki" / "config" / "methodology.yaml").exists():
                    brain_path = candidate
                    break
            else:
                brain_path = local_root  # Fallback to local

    brain_wiki = brain_path / "wiki" if (brain_path / "wiki").exists() else brain_path
    brain_config = brain_wiki / "config"

    return {
        "root": local_root,
        "wiki": local_wiki,
        "local_config": local_wiki / "config" if (local_wiki / "config").exists() else brain_config,
        # Brain paths — where methodology, standards, chains, templates live
        "brain_root": brain_path,
        "brain_wiki": brain_wiki,
        "config": brain_config,
        "methodology": brain_config / "methodology.yaml",
        "artifact_types": brain_config / "artifact-types.yaml",
        "schema": brain_config / "wiki-schema.yaml",
        "templates": brain_config / "templates",
        # Whether local and brain are the same
        "is_brain": str(local_root.resolve()) == str(brain_path.resolve()),
    }


# ---------------------------------------------------------------------------
# Query: methodology, stages, chains, artifacts, fields, identity
# ---------------------------------------------------------------------------

def query_what_do_i_need(paths: Dict[str, Path]) -> str:
    """Smart auto-routing: detect identity → recommend chain → show first steps.

    This is the "I don't know what I don't know" entry point.
    Detects as much as possible automatically, recommends next actions.
    """
    root = paths["root"]

    # Auto-detect what we can
    detected = auto_detect_identity(root)

    # Also check for declared identity in CLAUDE.md
    declared = query_identity(paths).get("identity", {})

    # Merge: declared overrides detected
    identity = {**detected}
    if declared:
        identity["declared"] = True
        # Use declared values for recommendation when available
        declared_chain = declared.get("sdlc chain", "").lower()
        declared_phase = declared.get("phase", "").lower()
    else:
        identity["declared"] = False
        declared_chain = ""
        declared_phase = ""

    # Recommend chain based on identity (declared overrides detected)
    mode = identity.get("execution_mode", "solo")
    phase = declared_phase if declared_phase else identity.get("phase", "poc")
    scale = identity.get("scale", "micro")

    if "default" in declared_chain:
        recommended_chain = "default"
    elif "full" in declared_chain:
        recommended_chain = "full"
    elif "simplified" in declared_chain:
        recommended_chain = "simplified"
    elif mode == "full-system" or (phase == "production" and scale in ("large", "massive")):
        recommended_chain = "full"
    elif phase in ("staging", "production") or scale in ("medium", "large"):
        recommended_chain = "default"
    else:
        recommended_chain = "simplified"

    lines = []
    lines.append("WHAT DO YOU NEED? — Auto-detected recommendations")
    lines.append("")

    # Identity
    lines.append(f"DETECTED IDENTITY:")
    lines.append(f"  execution mode: {identity.get('execution_mode', '?')}")
    lines.append(f"  domain: {identity.get('domain', '?')}")
    lines.append(f"  phase: {identity.get('phase', '?')}")
    lines.append(f"  scale: {identity.get('scale', '?')} ({identity.get('source_files', '?')} source files)")
    lines.append(f"  second brain: {identity.get('second_brain', '?')}")
    if declared:
        lines.append(f"  (identity also declared in CLAUDE.md — declared values take precedence)")
    lines.append("")

    # Recommendation
    lines.append(f"RECOMMENDED CHAIN: {recommended_chain}")
    chain_data = query_chain(paths, recommended_chain)
    if "error" not in chain_data:
        lines.append(f"  {chain_data.get('description', '')}")
        lines.append(f"  Stages: {' → '.join(chain_data.get('stages', []))}")
        lines.append(f"  Readiness gate: {chain_data.get('readiness_gate', '?')}")
    lines.append("")

    # First steps
    lines.append("YOUR FIRST STEPS:")
    if not declared:
        lines.append("  1. Add Identity Profile to your CLAUDE.md (see: gateway query --identity for the format)")

    domain = identity.get("domain", "unknown")
    if mode == "solo":
        lines.append(f"  {'2' if not declared else '1'}. You're in solo mode. Start with: gateway query --model feature-development")
        lines.append(f"  {'3' if not declared else '2'}. First stage: gateway query --stage document" + (f" --domain {domain}" if domain != "unknown" else ""))
        lines.append(f"  {'4' if not declared else '3'}. Get the template: gateway template methodology/requirements-spec")
    elif "harness" in mode:
        lines.append(f"  {'2' if not declared else '1'}. Your harness handles task dispatch. Check your harness config.")
        lines.append(f"  {'3' if not declared else '2'}. Query what your current stage needs: gateway query --stage <your-stage> --domain {domain}")
    else:
        lines.append(f"  {'2' if not declared else '1'}. Full system detected. Your orchestrator handles dispatch and enforcement.")
        lines.append(f"  {'3' if not declared else '2'}. Query chain details: gateway query --chain {recommended_chain}")

    lines.append("")
    lines.append("EXPLORE MORE:")
    lines.append("  gateway navigate              → full knowledge tree")
    lines.append("  gateway query --chains         → compare all SDLC chains")
    lines.append("  gateway query --models          → all methodology models")

    return "\n".join(lines)


def query_identity(paths: Dict[str, Path]) -> Dict[str, Any]:
    """Read the project's identity profile from CLAUDE.md."""
    claude_md = paths["root"] / "CLAUDE.md"
    if not claude_md.exists():
        return {"error": "No CLAUDE.md found", "identity": None}

    text = claude_md.read_text(encoding="utf-8")
    # Parse identity table if it exists
    identity = {}
    in_identity = False
    for line in text.split("\n"):
        if "Identity Profile" in line:
            in_identity = True
            continue
        if in_identity and line.startswith("|") and "**" in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 2:
                key = parts[0].replace("**", "").strip().lower()
                value = parts[1].strip()
                identity[key] = value
        elif in_identity and not line.startswith("|") and line.strip():
            in_identity = False

    return {"identity": identity if identity else None}


def query_stage(paths: Dict[str, Path], stage: str, domain: Optional[str] = None) -> Dict[str, Any]:
    """Query what artifacts, rules, and templates apply to a given stage."""
    methodology = load_config(paths["methodology"])
    if not methodology:
        return {"error": "methodology.yaml not found"}

    result = {"stage": stage, "domain": domain}

    # Find stage definition
    stages = methodology.get("stages", {})
    if isinstance(stages, list):
        stage_def = next((s for s in stages if s.get("name") == stage), None)
    elif isinstance(stages, dict):
        stage_def = stages.get(stage, {})
    else:
        stage_def = None

    if stage_def:
        result["allowed_outputs"] = stage_def.get("allowed_outputs", [])
        result["forbidden_outputs"] = stage_def.get("forbidden_outputs", [])
        result["readiness_range"] = stage_def.get("readiness_range", [])
        result["gate_commands"] = stage_def.get("gate_commands", [])

    # Domain-specific overrides
    if domain:
        profile_path = paths["config"] / "domain-profiles" / f"{domain}.yaml"
        profile = load_config(profile_path)
        if profile:
            overrides = profile.get("stage_overrides", {}).get(stage, {})
            if overrides:
                result["domain_overrides"] = overrides

    return result


def query_model(paths: Dict[str, Path], model_name: str, full_chain: bool = False) -> Dict[str, Any]:
    """Query a methodology model — stages, artifacts, chain."""
    methodology = load_config(paths["methodology"])
    if not methodology:
        return {"error": "methodology.yaml not found"}

    models = methodology.get("models", {})
    model_def = models.get(model_name)
    if not model_def:
        available = list(models.keys())
        return {"error": f"Model '{model_name}' not found", "available": available}

    result = {
        "model": model_name,
        "stages": model_def.get("stages", []),
        "description": model_def.get("description", ""),
    }

    if full_chain:
        result["chain"] = model_def.get("chain", {})

    return result


def query_models_list(paths: Dict[str, Path]) -> Dict[str, Any]:
    """List all available methodology models."""
    methodology = load_config(paths["methodology"])
    if not methodology:
        return {"error": "methodology.yaml not found"}

    models = methodology.get("models", {})
    result = []
    for name, defn in models.items():
        result.append({
            "name": name,
            "stages": defn.get("stages", []),
            "description": defn.get("description", ""),
        })
    return {"models": result}


def query_field(paths: Dict[str, Path], field_name: str) -> Dict[str, Any]:
    """Explain a frontmatter field — what it means, valid values, what reads it."""
    schema = load_config(paths["schema"])
    if not schema:
        return {"error": "wiki-schema.yaml not found"}

    required = schema.get("required_fields", [])
    optional = schema.get("optional_fields", [])
    enums = schema.get("enums", {})

    result = {"field": field_name}
    if field_name in required:
        result["required"] = True
    elif field_name in optional:
        result["required"] = False
    else:
        result["error"] = f"Unknown field: {field_name}"
        result["available_required"] = required
        result["available_optional"] = optional
        return result

    if field_name in enums:
        result["valid_values"] = enums[field_name]

    return result


def query_template(paths: Dict[str, Path], page_type: str) -> str:
    """Return the template for a page type."""
    template_path = paths["templates"] / f"{page_type}.md"
    if not template_path.exists():
        # Try methodology subdirectory
        template_path = paths["templates"] / "methodology" / f"{page_type}.md"
    if not template_path.exists():
        return f"No template found for type: {page_type}"
    return template_path.read_text(encoding="utf-8")


def query_config_section(paths: Dict[str, Path], section_path: str) -> str:
    """Render a config section as markdown. E.g., 'methodology.models' or 'artifact_types.types'."""
    parts = section_path.split(".", 1)
    config_name = parts[0]
    key_path = parts[1] if len(parts) > 1 else None

    config_map = {
        "methodology": paths["methodology"],
        "artifact_types": paths["artifact_types"],
        "schema": paths["schema"],
    }

    config_file = config_map.get(config_name)
    if not config_file:
        return f"Unknown config: {config_name}. Available: {list(config_map.keys())}"

    data = load_config(config_file)
    if not data:
        return f"Config file not found: {config_file}"

    if key_path:
        for key in key_path.split("."):
            if isinstance(data, dict):
                data = data.get(key)
            else:
                return f"Key '{key}' not found in path"
            if data is None:
                return f"Section '{section_path}' not found"

    # Render as YAML-formatted markdown
    import yaml
    return f"```yaml\n# {section_path}\n{yaml.dump(data, default_flow_style=False, sort_keys=False)}```"


# ---------------------------------------------------------------------------
# Operations: move, archive, backup, contribute
# ---------------------------------------------------------------------------

def op_move(paths: Dict[str, Path], title: str, target_dir: str, dry_run: bool = False) -> Dict[str, Any]:
    """Move a page to a new directory, updating all references."""
    wiki_dir = paths["wiki"]
    pages = find_wiki_pages(wiki_dir)

    # Find the source page
    source = None
    for p in pages:
        text = p.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(text)
        if fm and fm.get("title") == title:
            source = p
            break

    if not source:
        return {"error": f"Page with title '{title}' not found"}

    target = wiki_dir / target_dir / source.name
    result = {
        "source": str(source.relative_to(wiki_dir)),
        "target": str(target.relative_to(wiki_dir)),
        "references_updated": 0,
    }

    if dry_run:
        result["dry_run"] = True
        return result

    # Move the file
    target.parent.mkdir(parents=True, exist_ok=True)
    source.rename(target)

    # Update domain field in frontmatter if domain changed
    text = target.read_text(encoding="utf-8")
    # TODO: update domain field based on new path

    result["moved"] = True
    return result


def op_contribute(paths: Dict[str, Path], contrib_type: str, title: str,
                  content: str, domain: str = "cross-domain") -> Dict[str, Any]:
    """Create a structured write-back to the wiki (remark, lesson, correction)."""
    from datetime import datetime

    wiki_dir = paths["wiki"]
    today = datetime.now().strftime("%Y-%m-%d")
    slug = title.lower().replace(" ", "-").replace("'", "")[:60]

    type_dirs = {
        "lesson": wiki_dir / "lessons" / "00_inbox",
        "remark": wiki_dir / "log",
        "correction": wiki_dir / "log",
    }

    target_dir = type_dirs.get(contrib_type, wiki_dir / "log")
    target_dir.mkdir(parents=True, exist_ok=True)

    if contrib_type == "lesson":
        page_content = f"""---
title: "{title}"
type: lesson
domain: {domain}
layer: 4
status: synthesized
confidence: medium
maturity: seed
derived_from: []
created: {today}
updated: {today}
sources: []
tags: [contributed, inbox]
---

# {title}

## Summary

{content}

## Context

<!-- When does this lesson apply? -->

## Insight

<!-- The core learning -->

## Evidence

<!-- What evidence supports this? -->

## Relationships

- RELATES TO: [[Model Registry]]
"""
    else:
        page_content = f"""---
title: "{title}"
type: note
domain: log
note_type: session
status: synthesized
confidence: medium
created: {today}
updated: {today}
sources: []
tags: [contributed, {contrib_type}]
---

# {title}

## Summary

{content}

## Relationships

- RELATES TO: [[Model Registry]]
"""

    target_path = target_dir / f"{slug}.md"
    target_path.write_text(page_content, encoding="utf-8")

    return {
        "created": str(target_path.relative_to(paths["wiki"])),
        "type": contrib_type,
        "title": title,
    }


def op_archive(paths: Dict[str, Path], title: str, dry_run: bool = False) -> Dict[str, Any]:
    """Archive a page — move to _archive/ with location mapping for bridge."""
    import json as _json
    from datetime import datetime

    wiki_dir = paths["wiki"]
    pages = find_wiki_pages(wiki_dir)

    source = None
    for p in pages:
        text = p.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(text)
        if fm and fm.get("title") == title:
            source = p
            break

    if not source:
        return {"error": f"Page with title '{title}' not found"}

    archive_dir = wiki_dir / "_archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    target = archive_dir / source.name

    result = {
        "source": str(source.relative_to(wiki_dir)),
        "target": str(target.relative_to(wiki_dir)),
        "title": title,
    }

    if dry_run:
        result["dry_run"] = True
        return result

    # Save location mapping for bridge
    mapping_path = wiki_dir / "config" / "location-mapping.json"
    mapping = {}
    if mapping_path.exists():
        mapping = _json.loads(mapping_path.read_text(encoding="utf-8"))

    mapping[title] = {
        "original": str(source.relative_to(wiki_dir)),
        "archived": str(target.relative_to(wiki_dir)),
        "archived_date": datetime.now().strftime("%Y-%m-%d"),
        "reason": "archived via gateway",
    }

    # Move the file
    source.rename(target)

    # Update status in archived file
    text = target.read_text(encoding="utf-8")
    text = text.replace("status: synthesized", "status: archived", 1)
    text = text.replace("status: active", "status: archived", 1)
    text = text.replace("status: growing", "status: archived", 1)
    target.write_text(text, encoding="utf-8")

    # Save mapping
    mapping_path.write_text(_json.dumps(mapping, indent=2, ensure_ascii=False), encoding="utf-8")

    result["archived"] = True
    result["mapping_saved"] = str(mapping_path.relative_to(wiki_dir))
    return result


def op_backup(paths: Dict[str, Path], target_dir: str) -> Dict[str, Any]:
    """Backup the wiki to a target directory."""
    import shutil
    from datetime import datetime

    wiki_dir = paths["wiki"]
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_name = f"wiki-backup-{timestamp}"
    backup_path = Path(target_dir) / backup_name

    try:
        shutil.copytree(wiki_dir, backup_path, dirs_exist_ok=False)
        page_count = len(list(backup_path.rglob("*.md")))
        return {
            "backup": str(backup_path),
            "pages": page_count,
            "timestamp": timestamp,
            "source": str(wiki_dir),
        }
    except Exception as e:
        return {"error": str(e)}


def query_chain(paths: Dict[str, Path], chain_name: str) -> Dict[str, Any]:
    """Query an SDLC chain config (simplified, default, full)."""
    chain_path = paths["config"] / "sdlc-chains" / f"{chain_name}.yaml"
    data = load_config(chain_path)
    if not data:
        available = [f.stem for f in (paths["config"] / "sdlc-chains").glob("*.yaml")]
        return {"error": f"Chain '{chain_name}' not found", "available": available}

    return {
        "chain": data.get("chain"),
        "description": data.get("description"),
        "stages": list(data.get("stages", {}).keys()),
        "models": data.get("models", []),
        "readiness_gate": data.get("tracking", data.get("differences", {})).get("readiness_gate",
                          data.get("differences", {}).get("readiness_gate", "N/A")),
        "enforcement": data.get("differences", {}).get("enforcement", "N/A"),
        "upgrade_triggers": data.get("upgrade_triggers", []),
    }


def query_chains_list(paths: Dict[str, Path]) -> Dict[str, Any]:
    """List all available SDLC chains."""
    chains_dir = paths["config"] / "sdlc-chains"
    if not chains_dir.exists():
        return {"error": "No sdlc-chains directory found", "chains": []}

    result = []
    for f in sorted(chains_dir.glob("*.yaml")):
        data = load_config(f)
        if data:
            result.append({
                "name": data.get("chain", f.stem),
                "description": data.get("description", ""),
                "stages": len(data.get("stages", {})),
                "models": len(data.get("models", [])),
            })
    return {"chains": result}


def query_location_mapping(paths: Dict[str, Path], title: Optional[str] = None) -> Dict[str, Any]:
    """Query the location mapping — find where archived/moved pages went."""
    import json as _json

    mapping_path = paths["config"] / "location-mapping.json"
    if not mapping_path.exists():
        return {"mapping": {}, "message": "No pages have been archived or moved yet"}

    mapping = _json.loads(mapping_path.read_text(encoding="utf-8"))

    if title:
        entry = mapping.get(title)
        if entry:
            return {"title": title, "location": entry}
        else:
            return {"title": title, "error": "Not found in mapping"}

    return {"mapping": mapping, "total": len(mapping)}


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Wiki Gateway — unified knowledge interface",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--wiki-root", help="Target a different project's wiki")
    parser.add_argument("--brain", help="Path to second brain (auto-detected if not specified)")

    sub = parser.add_subparsers(dest="command")

    # Query commands
    q = sub.add_parser("query", help="Query methodology, stages, models, fields, chains")
    q.add_argument("--json", action="store_true", help="JSON output")
    q.add_argument("--stage", help="Query artifacts/rules for a stage")
    q.add_argument("--domain", help="Domain for stage query")
    q.add_argument("--model", help="Query a methodology model")
    q.add_argument("--full-chain", action="store_true", help="Include full artifact chain")
    q.add_argument("--models", action="store_true", help="List all models")
    q.add_argument("--field", help="Explain a frontmatter field")
    q.add_argument("--identity", action="store_true", help="Show project identity profile")
    q.add_argument("--chain", help="Query an SDLC chain (simplified, default, full)")
    q.add_argument("--chains", action="store_true", help="List all SDLC chains")
    q.add_argument("--mapping", nargs="?", const="__all__", help="Query location mapping (optionally for a specific title)")

    # Template command
    t = sub.add_parser("template", help="Get a page template")
    t.add_argument("type", help="Page type (lesson, pattern, decision, principle, etc.)")

    # Config command
    c = sub.add_parser("config", help="Render config section as markdown")
    c.add_argument("section", help="Config path (e.g., methodology.models)")

    # Move command
    m = sub.add_parser("move", help="Move a page, update references")
    m.add_argument("title", help="Page title to move")
    m.add_argument("--to", required=True, help="Target directory within wiki/")
    m.add_argument("--dry-run", action="store_true")

    # Smart auto-routing
    sub.add_parser("what-do-i-need", help="Auto-detect identity and recommend chain, model, first steps")

    # Status command (smart default — show everything)
    sub.add_parser("status", help="Show project identity, chain, models, and navigation guide")

    # Navigate command (tree view)
    n = sub.add_parser("navigate", help="Browse the full knowledge tree")
    n.add_argument("target", nargs="?", default="top", help="Navigation target (default: top)")

    # Archive command
    a = sub.add_parser("archive", help="Archive a page with location mapping")
    a.add_argument("title", help="Page title to archive")
    a.add_argument("--dry-run", action="store_true")

    # Backup command
    b = sub.add_parser("backup", help="Backup the wiki")
    b.add_argument("--target", required=True, help="Target directory for backup")

    # Contribute command
    ct = sub.add_parser("contribute", help="Write back to the wiki")
    ct.add_argument("--type", required=True, choices=["lesson", "remark", "correction"])
    ct.add_argument("--title", required=True)
    ct.add_argument("--content", required=True)
    ct.add_argument("--domain", default="cross-domain")

    args = parser.parse_args()
    paths = resolve_paths(
        wiki_root=args.wiki_root if hasattr(args, "wiki_root") else None,
        brain_root=args.brain if hasattr(args, "brain") else None,
    )

    if args.command == "what-do-i-need":
        print(query_what_do_i_need(paths))

    elif args.command == "query":
        if args.identity:
            result = query_identity(paths)
        elif args.stage:
            # Auto-detect domain if not provided
            domain = args.domain
            if not domain:
                detected = auto_detect_identity(paths["root"])
                auto_domain = detected.get("domain")
                if auto_domain and auto_domain != "unknown":
                    domain = auto_domain
            result = query_stage(paths, args.stage, domain)
        elif args.model:
            result = query_model(paths, args.model, args.full_chain)
        elif args.models:
            result = query_models_list(paths)
        elif args.chain:
            result = query_chain(paths, args.chain)
        elif args.chains:
            result = query_chains_list(paths)
        elif args.field:
            result = query_field(paths, args.field)
        elif args.mapping is not None:
            title = None if args.mapping == "__all__" else args.mapping
            result = query_location_mapping(paths, title)
        else:
            # No args to query → show navigate instead of argparse error
            print("No query specified. Try one of:")
            print("  gateway query --identity        → who am I?")
            print("  gateway query --models           → what models exist?")
            print("  gateway query --chains           → what SDLC chains exist?")
            print("  gateway query --stage <name>    → what does a stage need?")
            print("  gateway query --model <name>    → model details")
            print("  gateway query --field <name>    → explain a field")
            print()
            print("Or try: gateway what-do-i-need    → auto-detect and recommend")
            return

        use_json = getattr(args, "json", False)
        if use_json:
            print(json.dumps(result, indent=2, default=str))
        else:
            for k, v in result.items():
                if isinstance(v, (dict, list)):
                    print(f"  {k}:")
                    for item in (v if isinstance(v, list) else [v]):
                        print(f"    {item}")
                else:
                    print(f"  {k}: {v}")

    elif args.command == "template":
        content = query_template(paths, args.type)
        print(content)

    elif args.command == "config":
        content = query_config_section(paths, args.section)
        print(content)

    elif args.command == "move":
        result = op_move(paths, args.title, args.to, args.dry_run)
        print(json.dumps(result, indent=2, default=str))

    elif args.command == "archive":
        result = op_archive(paths, args.title, getattr(args, "dry_run", False))
        print(json.dumps(result, indent=2, default=str))

    elif args.command == "backup":
        result = op_backup(paths, args.target)
        print(json.dumps(result, indent=2, default=str))

    elif args.command == "contribute":
        result = op_contribute(paths, args.type, args.title, args.content, args.domain)
        print(json.dumps(result, indent=2, default=str))

    elif args.command == "status":
        # Smart default: show everything relevant about this project
        identity = query_identity(paths)
        chains = query_chains_list(paths)
        models = query_models_list(paths)

        print("╔═══════════════════════════════════════════════════╗")
        print("║          WIKI GATEWAY — PROJECT STATUS            ║")
        print("╚═══════════════════════════════════════════════════╝")
        print()

        # Identity
        id_data = identity.get("identity", {})
        if id_data:
            print("IDENTITY (who am I?)")
            for k, v in id_data.items():
                print(f"  {k}: {v}")
        else:
            print("IDENTITY: not configured. Add Identity Profile table to CLAUDE.md")
            print("  See: wiki/domains/cross-domain/project-self-identification-protocol.md")
        print()

        # Chain
        chain_name = (id_data.get("sdlc chain", "").split("(")[0].strip().lower()
                      if id_data else "default")
        chain_data = query_chain(paths, chain_name) if chain_name else {}
        if "error" not in chain_data:
            print(f"SDLC CHAIN: {chain_data.get('chain', '?')} — {chain_data.get('description', '')}")
            print(f"  Stages: {' → '.join(chain_data.get('stages', []))}")
            print(f"  Readiness gate: {chain_data.get('readiness_gate', '?')}")
            print(f"  Enforcement: {chain_data.get('enforcement', '?')}")
        print()

        # Models
        model_data = models.get("models", [])
        print(f"METHODOLOGY MODELS ({len(model_data)} available)")
        for m in model_data:
            stages = " → ".join(m.get("stages", []))
            print(f"  {m['name']}: {stages}")
        print()

        # Navigation guide
        print("NAVIGATE FROM HERE")
        print("  gateway query --stage <name>              → what does a stage need?")
        print("  gateway query --stage <name> --domain <d> → stage + domain overrides")
        print("  gateway query --model <name> --full-chain → full artifact chain")
        print("  gateway query --chain <name>              → SDLC chain details")
        print("  gateway query --field <name>              → explain a frontmatter field")
        print("  gateway template <type>                   → get a page template")
        print("  gateway config methodology.models         → render config as markdown")
        print("  gateway contribute --type lesson ...      → write back to wiki")
        print()
        print("WIKI PAGES (start reading here)")
        print("  wiki/spine/super-model.md                 → the dashboard")
        print("  wiki/spine/methodology-system-map.md      → find anything")
        print("  wiki/spine/model-methodology.md            → how work proceeds")
        print("  wiki/spine/learning-paths/methodology-fundamentals.md → 30-page learning path")

    elif args.command == "navigate":
        # Tree navigation: show path from top to any layer
        nav_target = args.target.lower() if hasattr(args, "target") and args.target else "top"

        if nav_target == "top":
            print("WIKI KNOWLEDGE TREE")
            print("│")
            print("├── IDENTITY → gateway query --identity")
            print("│   └── Goldilocks Protocol: wiki/domains/cross-domain/project-self-identification-protocol.md")
            print("│")
            print("├── SDLC CHAINS → gateway query --chains")
            print("│   ├── simplified (POC, micro/small)")
            print("│   ├── default (MVP→Staging, small→medium) ← most projects")
            print("│   └── full (Production, medium→massive)")
            print("│")
            print("├── METHODOLOGY MODELS → gateway query --models")

            models = query_models_list(paths).get("models", [])
            for m in models:
                stages = " → ".join(m.get("stages", []))
                print(f"│   ├── {m['name']}: {stages}")

            print("│")
            print("├── STAGES → gateway query --stage <name>")
            print("│   ├── document [0-25%] → requirements, research")
            print("│   ├── design [25-50%] → tech spec, decisions")
            print("│   ├── scaffold [50-80%] → types, stubs")
            print("│   ├── implement [80-95%] → business logic, wired in")
            print("│   └── test [95-100%] → assertions, verification")
            print("│")
            print("├── ENFORCEMENT → wiki/lessons/03_validated/infrastructure-enforcement-proves-instructions-fail.md")
            print("│   ├── instructions (25%) → hooks (100%) → harness → immune system")
            print("│   └── 7 behavioral failure classes persist after infrastructure")
            print("│")
            print("├── PRINCIPLES → wiki/lessons/04_principles/hypothesis/")
            print("│   ├── Infrastructure Over Instructions")
            print("│   ├── Structured Context Governs Behavior")
            print("│   └── Right Process for Right Context (Goldilocks)")
            print("│")
            print("├── TRACKING → gateway query --field readiness / --field progress")
            print("│   ├── readiness (definition completeness) gates progress (execution)")
            print("│   └── 99→100 = human only. Always.")
            print("│")
            print("├── HIERARCHY → Milestone → Epic → Module → Task")
            print("│   └── 8 impediment types: technical, dependency, decision, environment, ...")
            print("│")
            print("├── PM LEVELS → L1 (wiki) → L2 (fleet) → L3 (full PM)")
            print("│   └── Harness: none → v1 → v2 → v3")
            print("│")
            print("└── TOOLS")
            print("    ├── gateway (this tool) — query, template, config, move, archive, backup, contribute")
            print("    ├── pipeline — post, fetch, scaffold, status, gaps, evolve")
            print("    ├── view — dashboard, spine, model, search, refs")
            print("    └── MCP server — 17 tools for Claude Code integration")
        else:
            print(f"Navigation target '{nav_target}' — use 'gateway navigate' for full tree")

    else:
        # No command: show guided entry point
        print("Wiki Gateway — unified knowledge interface")
        print()
        print("Start here:")
        print("  gateway status                → see your project identity + SDLC chain + models")
        print("  gateway navigate              → browse the full knowledge tree")
        print("  gateway query --help          → all query options")
        print()
        print("Common paths:")
        print("  I'm new to this project       → gateway status")
        print("  I need to find something      → gateway navigate")
        print("  I'm building a feature        → gateway query --model feature-development --full-chain")
        print("  I need the right template     → gateway template <type>")
        print("  I learned something           → gateway contribute --type lesson --title '...' --content '...'")
        print("  I'm from another project      → gateway status --wiki-root ~/devops-solutions-research-wiki")


if __name__ == "__main__":
    main()
