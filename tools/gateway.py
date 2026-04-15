"""Wiki Gateway — Unified knowledge interface for humans, agents, and MCP.

Provides structured queries into the wiki's methodology, standards, and knowledge,
plus operational commands (move, archive, backup). Works on BOTH the second brain
(this project) AND external project wikis.

Usage:
    python3 -m tools.gateway query --stage document --domain typescript
    python3 -m tools.gateway query --profile default
    python3 -m tools.gateway query --chain feature-development
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
    CONSUMER_RUNTIME_DEFAULT,
    CONSUMER_RUNTIME_ENV,
    consumer_runtime_is_declared,
    find_wiki_pages,
    get_consumer_runtime,
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

    # Execution mode: CANNOT be auto-detected from filesystem.
    #
    # The harness version is decided by THE HARNESS at runtime, not by project files.
    # When `openarms agent run` launches, IT decides v1/v2/v3 based on its own flags.
    # The project doesn't declare "I am harness v2" — the harness TELLS the project.
    #
    # What we CAN detect: does harness infrastructure EXIST in this project?
    # What we CANNOT detect: is it running? in what mode? what version?
    #
    # So we report what we see, and mark execution_mode as "unknown — must be declared"
    # unless it's clearly solo (no harness code exists at all).

    has_harness_code = any((root / m).exists() for m in [
        "src/commands/agent-run-harness.ts",
        "src/commands/agent-run.ts",
    ])
    has_fleet_code = any((root / m).exists() for m in [
        "fleet/core/orchestrator.py",
        "fleet/cli/orchestrator.py",
    ])
    has_enforcement = any((root / m).exists() for m in [
        "scripts/methodology/validate-stage.cjs",
        "scripts/methodology/hooks/pre-bash.sh",
    ])

    if not has_harness_code and not has_fleet_code:
        identity["execution_mode"] = "solo"
        identity["execution_mode_confidence"] = "certain"
    else:
        # Harness/fleet code EXISTS but we don't know if it's RUNNING or in what mode
        capabilities = []
        if has_fleet_code:
            capabilities.append("fleet/orchestrator")
        if has_harness_code:
            capabilities.append("harness")
        if has_enforcement:
            capabilities.append("enforcement (hooks/validator)")

        identity["execution_mode"] = "unknown — declare in CLAUDE.md or pass at runtime"
        identity["execution_mode_confidence"] = "cannot detect — harness decides its own version at launch"
        identity["harness_capabilities_detected"] = capabilities

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
    else:
        identity["declared"] = False

    # Parse declared strings defensively — they may carry trailing parenthetical
    # context like "production (used daily, 316+ pages)" or "medium (316 pages, growing)".
    # Match on keyword containment, not equality.
    def _extract_keyword(raw: str, vocab: tuple) -> str:
        """Return the first keyword from `vocab` that appears in raw (case-insensitive)."""
        if not raw:
            return ""
        low = raw.lower()
        for kw in vocab:
            if kw in low:
                return kw
        return ""

    declared_profile = _extract_keyword(
        declared.get("sdlc profile", "") or declared.get("sdlc chain", ""),
        ("simplified", "default", "full"),
    )
    declared_phase = _extract_keyword(
        declared.get("phase", ""),
        ("poc", "mvp", "staging", "production"),
    )
    declared_scale = _extract_keyword(
        declared.get("scale", ""),
        ("micro", "small", "medium", "large", "massive"),
    )

    # Recommend SDLC profile — declared takes precedence; heuristics are fallback.
    # Execution mode is NOT used for profile selection (see directive:
    # raw/notes/2026-04-15-directive-execution-mode-is-consumer-property-not-project.md).
    phase = declared_phase or identity.get("phase", "poc")
    scale = declared_scale or identity.get("scale", "micro")

    if declared_profile:
        recommended_profile = declared_profile
    elif phase == "production" and scale in ("large", "massive"):
        recommended_profile = "full"
    elif phase in ("staging", "production") or scale in ("medium", "large"):
        recommended_profile = "default"
    else:
        recommended_profile = "simplified"

    lines = []
    lines.append("WHAT DO YOU NEED? — Declared identity + task-dependent recommendations")
    lines.append("")

    # PROJECT IDENTITY — declared is authoritative; heuristics are sanity signals.
    # Execution mode is NOT a project property — it's a consumer/runtime property
    # (a harness or fleet that WRAPS this project declares the mode; from inside
    # the project we cannot detect which consumer is using us).
    # See raw/notes/2026-04-15-directive-execution-mode-is-consumer-property-not-project.md
    lines.append(f"PROJECT IDENTITY:")
    domain_val = identity.get("domain", "?")
    phase_val = declared.get("phase", "").lower() or identity.get("phase", "?")
    scale_val = identity.get("scale", "?")
    file_count = identity.get("source_files", "?")

    if declared:
        lines.append(f"  domain:         {declared.get('domain', domain_val)}  ✓ declared")
        lines.append(f"  phase:          {phase_val}  ✓ declared")
        declared_scale = declared.get("scale", "").lower()
        if declared_scale:
            # Sanity-check: flag if heuristic strongly disagrees with declaration
            mismatch = ""
            if declared_scale in ("medium", "large", "massive") and isinstance(file_count, int) and file_count < 50:
                mismatch = f"  ⚠ sanity: file-count heuristic saw only {file_count} (may be counting wrong path)"
            lines.append(f"  scale:          {declared_scale}  ✓ declared{mismatch}")
        else:
            lines.append(f"  scale:          {scale_val} ({file_count} files)  ⚠ heuristic — declare in CLAUDE.md")
        lines.append(f"  second brain:   {declared.get('second brain', identity.get('second_brain', '?'))}  ✓ declared")
    else:
        lines.append(f"  domain:         {domain_val}  ⚠ heuristic — declare in CLAUDE.md")
        lines.append(f"  phase:          {phase_val}  ⚠ heuristic — declare in CLAUDE.md")
        lines.append(f"  scale:          {scale_val} ({file_count} files)  ⚠ heuristic — declare in CLAUDE.md")
        lines.append(f"  second brain:   {identity.get('second_brain', '?')}  ⚠ heuristic")
    lines.append("")

    # CONSUMER/TASK PROPERTIES — not detectable from inside the project.
    # Per `wiki/decisions/00_inbox/consumer-runtime-signaling-via-mcp-config.md`,
    # consumers declare non-default runtime via MCP_CLIENT_RUNTIME env var.
    lines.append("CONSUMER / TASK PROPERTIES (not project properties):")
    runtime = get_consumer_runtime()
    if consumer_runtime_is_declared():
        lines.append(f"  execution mode: {runtime}  ✓ declared by consumer (via {CONSUMER_RUNTIME_ENV})")
    else:
        lines.append(f"  execution mode: {runtime} (default — no consumer declared otherwise)")
        lines.append(f"                  A harness or fleet that wraps this project DECLARES non-default via its")
        lines.append(f"                  `.mcp.json` entry's env block: {{\"env\": {{\"{CONSUMER_RUNTIME_ENV}\": \"harness-<name>-<version>\"}}}}.")
        lines.append(f"                  From inside this project we cannot detect which consumer (if any) is using us.")
    lines.append(f"  methodology model: PER TASK, not per project. bug→bug-fix, feature→feature-development,")
    lines.append(f"                     docs→documentation, research→research, etc. See: gateway query --models")
    lines.append(f"  SDLC profile:   PER TASK. Declared phase/scale suggests a DEFAULT starting profile but")
    lines.append(f"                  every task may override. Profiles: simplified / default / full.")
    lines.append("")

    # Recommendation — framed as a default for most tasks, not a project-wide lock.
    lines.append(f"SUGGESTED DEFAULT PROFILE (for most tasks given declared identity): {recommended_profile}")
    profile_data = query_profile(paths, recommended_profile)
    if "error" not in profile_data:
        lines.append(f"  {profile_data.get('description', '')}")
        methodology = profile_data.get("methodology", {})
        available = methodology.get("available_models", [])
        if available:
            lines.append(f"  Available models: {', '.join(available[:5])}" + (" ..." if len(available) > 5 else ""))
        enforcement = profile_data.get("enforcement", {})
        if enforcement:
            lines.append(f"  Enforcement: {enforcement.get('level', '?')}; stage gates: {enforcement.get('stage_gates', '?')}")
    lines.append(f"  ⚠ This is a DEFAULT suggestion. Override per task — e.g., hotfix uses simplified even in a")
    lines.append(f"    production project; deep-architecture-review uses full even in an mvp.")
    lines.append("")

    # First steps — honor the consumer-property framing.
    lines.append("YOUR FIRST STEPS:")
    step = 1
    if not declared:
        lines.append(f"  {step}. Add Identity Profile to your CLAUDE.md (see: gateway query --identity for the format)")
        step += 1

    domain = identity.get("domain", "unknown")
    lines.append(f"  {step}. If a harness/fleet is consuming this project: follow ITS dispatch flow — it owns task selection.")
    step += 1
    lines.append(f"  {step}. If no harness (solo is the default): pick the model for your TASK:")
    lines.append(f"       gateway query --model <bug-fix | feature-development | research | documentation | ...>")
    step += 1
    lines.append(f"  {step}. First stage for most models: gateway query --stage document" + (f" --domain {domain}" if domain != "unknown" else ""))

    lines.append("")
    lines.append("EXPLORE MORE:")
    lines.append("  gateway navigate              → full knowledge tree")
    lines.append("  gateway query --profiles        → compare all SDLC policy profiles")
    lines.append("  gateway query --chains          → all methodology models with their chains")
    lines.append("  gateway query --models          → all methodology models")

    return "\n".join(lines)


def cmd_flow(paths: Dict[str, Path], step: int = None) -> str:
    """Goldilocks flow — step-by-step routing from identity to action.

    Walks through all 8 steps of the Goldilocks protocol, showing what each
    step does, what commands to run, and what to read in the wiki.
    Use --step N to jump to a specific step.
    """
    steps = [
        {
            "num": 1, "name": "DETECT",
            "desc": "Auto-detect what can be seen from your project",
            "cmd": "python3 -m tools.gateway what-do-i-need",
            "wiki": "wiki/spine/goldilocks-flow.md → Step 1",
            "output": "Domain, scale, phase, second brain status. Execution mode if deterministic.",
        },
        {
            "num": 2, "name": "DECLARE",
            "desc": "Complete your Identity Profile in CLAUDE.md",
            "cmd": "python3 -m tools.gateway query --identity",
            "wiki": "wiki/spine/goldilocks-flow.md → Step 2",
            "output": "7 dimensions declared: type, execution mode, domain, phase, scale, PM level, trust tier.",
        },
        {
            "num": 3, "name": "SELECT PROFILE",
            "desc": "Choose SDLC profile: simplified/default/full based on phase × scale",
            "cmd": "python3 -m tools.gateway query --profiles",
            "wiki": "wiki/config/sdlc-profiles/ (3 YAML configs)",
            "output": "One SDLC profile selected. Determines enforcement level, available models, readiness gate.",
        },
        {
            "num": 4, "name": "SELECT MODEL",
            "desc": "Pick the right methodology model for your task type",
            "cmd": "python3 -m tools.gateway query --models",
            "wiki": "wiki/spine/references/model-registry.md",
            "output": "One of 9 models selected. Determines which stages your task goes through.",
        },
        {
            "num": 5, "name": "ENTER STAGE",
            "desc": "Know what this stage allows, forbids, and requires",
            "cmd": "python3 -m tools.gateway query --stage document",
            "wiki": "CLAUDE.md ALLOWED/FORBIDDEN table",
            "output": "Stage rules: what you can produce, what's forbidden, gate command.",
        },
        {
            "num": 6, "name": "PRODUCE",
            "desc": "Follow the artifact chain for your model + stage + domain",
            "cmd": "python3 -m tools.gateway query --model feature-development --full-chain",
            "wiki": "wiki/domains/cross-domain/methodology-artifacts/chains/",
            "output": "Artifacts produced. Templates filled. Validated with pipeline post.",
        },
        {
            "num": 7, "name": "TRACK",
            "desc": "Update readiness (definition) and progress (execution)",
            "cmd": "python3 -m tools.gateway query --field readiness",
            "wiki": "wiki/domains/cross-domain/readiness-vs-progress.md",
            "output": "Frontmatter updated. 99→100 = human review only.",
        },
        {
            "num": 8, "name": "FEEDBACK",
            "desc": "Contribute learnings back to the second brain",
            "cmd": "python3 -m tools.gateway contribute --type lesson --title '...' --content '...'",
            "wiki": "wiki/lessons/00_inbox/ (maturity pipeline entry)",
            "output": "Lesson/remark filed. Evolution pipeline scores and promotes.",
        },
    ]

    lines = []
    lines.append("GOLDILOCKS FLOW — From Identity to Action")
    lines.append("=" * 50)
    lines.append("")

    if step:
        # Show one step in detail
        matching = [s for s in steps if s["num"] == step]
        if not matching:
            return f"Invalid step {step}. Valid: 1-8."
        s = matching[0]
        lines.append(f"STEP {s['num']}: {s['name']}")
        lines.append(f"  {s['desc']}")
        lines.append("")
        lines.append(f"  Run:   {s['cmd']}")
        lines.append(f"  Read:  {s['wiki']}")
        lines.append(f"  Output: {s['output']}")
        lines.append("")
        if step < 8:
            lines.append(f"  Next: gateway flow --step {step + 1}")
        else:
            lines.append("  Done! Return to any step when context changes.")
        lines.append("")
        lines.append("Full flow: gateway flow")
    else:
        # Show all 8 steps as overview
        lines.append("8 steps from 'who am I?' to 'what do I do next?'")
        lines.append("Jump to any step: gateway flow --step N")
        lines.append("")
        for s in steps:
            lines.append(f"  Step {s['num']}: {s['name']:14s} — {s['desc']}")
            lines.append(f"         cmd:  {s['cmd']}")
            lines.append("")

        # Auto-detect current context
        detected = auto_detect_identity(paths["root"])
        lines.append("YOUR CONTEXT (auto-detected):")
        lines.append(f"  domain: {detected.get('domain', '?')}  |  "
                      f"phase: {detected.get('phase', '?')}  |  "
                      f"scale: {detected.get('scale', '?')}  |  "
                      f"mode: {detected.get('execution_mode', '?')}")
        lines.append("")
        lines.append("Start: gateway flow --step 1")
        lines.append("Wiki:  wiki/spine/goldilocks-flow.md")

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
# Operational queries: backlog, lessons, logs, page lookup
# ---------------------------------------------------------------------------

def query_backlog(paths: Dict[str, Path]) -> Dict[str, Any]:
    """Show backlog status: epics with readiness/progress, impediments."""
    wiki_dir = paths["wiki"]
    epics_dir = wiki_dir / "backlog" / "epics"

    if not epics_dir.exists():
        return {"error": "No backlog/epics/ directory found", "epics": []}

    epics = []
    for f in sorted(epics_dir.glob("*.md")):
        if f.name == "_index.md":
            continue
        text = f.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(text)
        if not fm:
            continue
        epics.append({
            "title": fm.get("title", f.stem),
            "status": fm.get("status", "?"),
            "priority": fm.get("priority", "?"),
            "readiness": fm.get("readiness", 0),
            "progress": fm.get("progress", 0),
            "current_stage": fm.get("current_stage", "?"),
        })

    # Check for impediments across all work items
    impediments = []
    for f in wiki_dir.rglob("*.md"):
        if "config" in str(f) or "_index" in f.name:
            continue
        text = f.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(text)
        if fm and fm.get("impediment_type"):
            impediments.append({
                "title": fm.get("title", f.stem),
                "type": fm.get("impediment_type"),
                "blocked_by": fm.get("blocked_by", ""),
                "blocked_since": fm.get("blocked_since", ""),
            })

    return {"epics": epics, "impediments": impediments}


def query_lessons(paths: Dict[str, Path]) -> Dict[str, Any]:
    """Show lessons grouped by maturity folder."""
    wiki_dir = paths["wiki"]
    lessons_dir = wiki_dir / "lessons"

    if not lessons_dir.exists():
        return {"error": "No lessons/ directory found"}

    result = {}
    for folder in ["00_inbox", "01_drafts", "02_synthesized", "03_validated", "04_principles"]:
        folder_path = lessons_dir / folder
        if not folder_path.exists():
            result[folder] = []
            continue

        pages = []
        for f in sorted(folder_path.rglob("*.md")):
            if f.name == "_index.md":
                continue
            text = f.read_text(encoding="utf-8")
            fm, _ = parse_frontmatter(text)
            if fm:
                pages.append({
                    "title": fm.get("title", f.stem),
                    "type": fm.get("type", "?"),
                    "confidence": fm.get("confidence", "?"),
                })
        result[folder] = pages

    return {"lessons": result, "total": sum(len(v) for v in result.values())}


def query_logs(paths: Dict[str, Path], limit: int = 0) -> Dict[str, Any]:
    """Show recent log entries. limit=0 returns all (default, per no-caps directive)."""
    wiki_dir = paths["wiki"]
    log_dir = wiki_dir / "log"

    if not log_dir.exists():
        return {"error": "No log/ directory found"}

    entries = []
    for f in sorted(log_dir.glob("*.md"), reverse=True):
        if f.name == "_index.md":
            continue
        text = f.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(text)
        if fm:
            entries.append({
                "title": fm.get("title", f.stem),
                "note_type": fm.get("note_type", "?"),
                "created": fm.get("created", "?"),
            })
        if limit > 0 and len(entries) >= limit:
            break

    return {"logs": entries, "total": len(entries)}


def query_page(paths: Dict[str, Path], title: str) -> Dict[str, Any]:
    """Look up a page by title — return metadata + summary + relationships."""
    wiki_dir = paths["wiki"]
    pages = find_wiki_pages(wiki_dir)

    for p in pages:
        text = p.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        if fm and fm.get("title", "").lower() == title.lower():
            sections = parse_sections(body)
            rels = parse_relationships(text)
            return {
                "title": fm.get("title"),
                "type": fm.get("type"),
                "domain": fm.get("domain"),
                "status": fm.get("status"),
                "maturity": fm.get("maturity", "N/A"),
                "confidence": fm.get("confidence"),
                "path": str(p.relative_to(wiki_dir)),
                "summary": sections.get("Summary", "")[:200],
                "relationships": len(rels),
                "lines": len(text.split("\n")),
            }

    return {"error": f"Page '{title}' not found"}


# ---------------------------------------------------------------------------
# Root documentation (README, AGENTS, CLAUDE, CONTEXT, ARCHITECTURE, DESIGN, TOOLS, SKILLS)
# ---------------------------------------------------------------------------

ROOT_DOCS = {
    "readme": ("README.md", "First visitor entry point — what this project IS"),
    "agents": ("AGENTS.md", "Universal cross-tool agent context (Claude, Codex, Copilot, Gemini, Cursor)"),
    "claude": ("CLAUDE.md", "Claude Code-specific overrides; references AGENTS.md"),
    "context": ("CONTEXT.md", "Identity profile, current state, active epics, constraints"),
    "architecture": ("ARCHITECTURE.md", "Data flow, tool topology, page schema, integration points"),
    "design": ("DESIGN.md", "Visual design principles, callout vocabulary, page layouts"),
    "tools": ("TOOLS.md", "Complete CLI reference (pipeline, gateway, view, sync, MCP)"),
    "skills": ("SKILLS.md", "Skills directory, SKILL.md format, extension hierarchy"),
}


def query_docs(paths: Dict[str, Path], doc_name: str = None) -> Dict[str, Any]:
    """Query root-level documentation files.

    No arg → list all root docs with descriptions.
    With name → return path + description + preview.
    """
    root = paths["root"]

    if doc_name is None:
        result = {"root_docs": []}
        for key, (filename, description) in ROOT_DOCS.items():
            file_path = root / filename
            entry = {
                "name": key,
                "file": filename,
                "description": description,
                "exists": file_path.exists(),
            }
            if file_path.exists():
                entry["lines"] = len(file_path.read_text(encoding="utf-8").split("\n"))
            result["root_docs"].append(entry)
        result["see_also"] = "wiki/spine/references/root-documentation-map.md"
        return result

    key = doc_name.lower().strip().replace(".md", "")
    if key not in ROOT_DOCS:
        return {
            "error": f"Unknown root doc '{doc_name}'",
            "available": list(ROOT_DOCS.keys()),
        }

    filename, description = ROOT_DOCS[key]
    file_path = root / filename
    if not file_path.exists():
        return {"error": f"{filename} not found at {root}"}

    text = file_path.read_text(encoding="utf-8")
    return {
        "name": key,
        "file": filename,
        "description": description,
        "path": str(file_path),
        "lines": len(text.split("\n")),
        "size_bytes": file_path.stat().st_size,
        "preview": text[:500],
        "instruction": "Read the full file for complete content.",
    }


# ---------------------------------------------------------------------------
# Operations: move, archive, backup, contribute
# ---------------------------------------------------------------------------

def _infer_domain_from_path(page_path: Path, wiki_dir: Path) -> str:
    """Infer domain from page's directory path."""
    rel = page_path.relative_to(wiki_dir)
    parts = rel.parts
    if len(parts) >= 2 and parts[0] == "domains":
        return parts[1]
    if parts[0] == "spine":
        return "cross-domain"
    if parts[0] == "backlog":
        return "backlog"
    if parts[0] == "log":
        return "log"
    if parts[0] in ("sources", "comparisons", "lessons", "patterns", "decisions"):
        return "cross-domain"
    return ""


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
    old_stem = source.stem
    new_stem = target.stem
    source.rename(target)

    # Update domain field in frontmatter based on new path
    text = target.read_text(encoding="utf-8")
    new_domain = _infer_domain_from_path(target, wiki_dir)
    if new_domain:
        import re
        text = re.sub(r'^(domain:\s*).*$', f'\\1{new_domain}', text, count=1, flags=re.MULTILINE)
        target.write_text(text, encoding="utf-8")

    # Update wikilink references across all wiki pages
    refs_updated = 0
    if old_stem != new_stem:
        for p in pages:
            if p == source or not p.exists():
                continue
            page_text = p.read_text(encoding="utf-8")
            if f"[[{old_stem}" in page_text:
                updated = page_text.replace(f"[[{old_stem}|", f"[[{new_stem}|")
                updated = updated.replace(f"[[{old_stem}]]", f"[[{new_stem}]]")
                if updated != page_text:
                    p.write_text(updated, encoding="utf-8")
                    refs_updated += 1

    result["moved"] = True
    result["references_updated"] = refs_updated
    result["domain_updated"] = new_domain or "(unchanged)"
    return result


def op_contribute(paths: Dict[str, Path], contrib_type: str, title: str,
                  content: str, domain: str = "cross-domain",
                  contributor: str = None, source: str = None,
                  reason: str = None) -> Dict[str, Any]:
    """Create a structured write-back to the wiki (remark, lesson, correction).

    Records an audit trail per wiki/config/contribution-policy.yaml:
    - contributed_by: who/what made this contribution
    - contribution_source: origin path or "self"
    - contribution_date: ISO date
    - contribution_status: "pending-review" (all contributions start here)

    Contributions land in 00_inbox (lessons) or log/ (remarks, corrections).
    Promotion beyond that requires human review per the trust tier policy.
    """
    from datetime import datetime
    import os as _os
    import socket as _socket

    wiki_dir = paths["wiki"]
    today = datetime.now().strftime("%Y-%m-%d")
    slug = title.lower().replace(" ", "-").replace("'", "")[:60]

    # Auto-detect contributor if not provided (fallback: user@host)
    if not contributor:
        try:
            contributor = f"{_os.environ.get('USER', 'unknown')}@{_socket.gethostname()}"
        except Exception:
            contributor = "gateway-cli"

    # Auto-detect source if not provided — self if operating on local wiki
    if not source:
        wiki_root = paths.get("root")
        if wiki_root:
            source = str(wiki_root)
        else:
            source = "self"

    type_dirs = {
        "lesson": wiki_dir / "lessons" / "00_inbox",
        "remark": wiki_dir / "log",
        "correction": wiki_dir / "log",
    }

    target_dir = type_dirs.get(contrib_type, wiki_dir / "log")
    target_dir.mkdir(parents=True, exist_ok=True)

    # Audit trail YAML fragment (all contributions get this)
    audit_fragment = (
        f"contributed_by: \"{contributor}\"\n"
        f"contribution_source: \"{source}\"\n"
        f"contribution_date: {today}\n"
        f"contribution_status: pending-review\n"
    )
    if reason:
        audit_fragment += f"contribution_reason: \"{reason}\"\n"

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
{audit_fragment}---

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

- RELATES TO: [[model-registry|Model Registry]]
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
{audit_fragment}---

# {title}

## Summary

{content}

## Relationships

- RELATES TO: [[model-registry|Model Registry]]
"""

    target_path = target_dir / f"{slug}.md"
    target_path.write_text(page_content, encoding="utf-8")

    return {
        "created": str(target_path.relative_to(paths["wiki"])),
        "type": contrib_type,
        "title": title,
        "contributed_by": contributor,
        "contribution_source": source,
        "contribution_status": "pending-review",
        "landing_folder": str(target_dir.relative_to(paths["wiki"])),
        "note": "Landed in maturity inbox (or log). Promotion requires human review per contribution-policy.yaml.",
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


def op_factory_reset(paths: Dict[str, Path], confirm: bool = False) -> Dict[str, Any]:
    """Reset a wiki to clean template state. DANGEROUS — deletes all content pages.

    Preserves: config/, templates, _index.md files, schema files.
    Deletes: all content .md files in domains/, sources/, comparisons/, lessons/,
             patterns/, decisions/, spine/ (except templates), backlog/, log/.
    Always creates backup first.
    """
    wiki_dir = paths["wiki"]

    # Inventory what would be deleted
    preserve_dirs = {"config"}
    preserve_files = {"_index.md", "manifest.json", "index.md"}
    to_delete = []
    for f in wiki_dir.rglob("*.md"):
        rel = f.relative_to(wiki_dir)
        if rel.parts[0] in preserve_dirs:
            continue
        if f.name in preserve_files:
            continue
        to_delete.append(f)

    result = {
        "files_to_delete": len(to_delete),
        "preserved_dirs": list(preserve_dirs),
        "preserved_files": list(preserve_files),
    }

    if not confirm:
        result["status"] = "DRY RUN — pass --confirm to execute"
        result["warning"] = f"This will DELETE {len(to_delete)} wiki pages. A backup will be created first."
        result["sample_deletions"] = [str(f.relative_to(wiki_dir)) for f in to_delete[:10]]
        return result

    # Create backup first
    backup_result = op_backup(paths, str(wiki_dir.parent / "factory-reset-backups"))
    result["backup"] = backup_result.get("backup", "FAILED")
    if "error" in backup_result:
        result["error"] = f"Backup failed: {backup_result['error']}. Aborting reset."
        return result

    # Delete content files
    deleted = 0
    for f in to_delete:
        f.unlink()
        deleted += 1

    # Clean empty directories
    for d in sorted(wiki_dir.rglob("*"), reverse=True):
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()

    result["status"] = "RESET COMPLETE"
    result["files_deleted"] = deleted
    return result


def query_chain(paths: Dict[str, Path], model_name: str) -> Dict[str, Any]:
    """Query the methodology CHAIN for a model.

    A methodology chain is the artifact sequence per stage within a model
    (e.g. feature-development has stages document→design→scaffold→implement→test,
    each with required/forbidden artifacts and gate checks).

    For SDLC-level POLICY (simplified/default/full), use query_profile instead.
    """
    methodology_path = paths["config"] / "methodology.yaml"
    data = load_config(methodology_path)
    if not data:
        return {"error": "methodology.yaml not found"}

    models = data.get("models", {})
    if model_name not in models:
        return {
            "error": f"Methodology model '{model_name}' not found",
            "available": list(models.keys()),
        }

    model = models[model_name]
    chain = model.get("chain", {})
    if not chain:
        return {
            "model": model_name,
            "description": model.get("description", ""),
            "stages": model.get("stages", []),
            "error": "No artifact chain defined for this model",
        }

    # Summarize chain per stage
    chain_summary = {}
    for stage, stage_def in chain.items():
        required = stage_def.get("required", [])
        required_summary = [
            f"{r.get('count', '?')}× {r.get('artifact', 'unknown')}"
            for r in (required if isinstance(required, list) else [])
        ]
        chain_summary[stage] = {
            "required": required_summary,
            "forbidden": stage_def.get("forbidden", []),
            "gate_checks": stage_def.get("gate", {}).get("checks", []),
        }

    return {
        "model": model_name,
        "description": model.get("description", ""),
        "stages": model.get("stages", []),
        "readiness_cap": model.get("readiness_cap", 100),
        "chain": chain_summary,
    }


def query_chains_list(paths: Dict[str, Path]) -> Dict[str, Any]:
    """List all methodology models with their chains."""
    methodology_path = paths["config"] / "methodology.yaml"
    data = load_config(methodology_path)
    if not data:
        return {"error": "methodology.yaml not found"}

    models = data.get("models", {})
    result = []
    for name, model in models.items():
        chain = model.get("chain", {})
        result.append({
            "model": name,
            "description": model.get("description", ""),
            "stages": model.get("stages", []),
            "has_chain": bool(chain),
            "stage_count": len(chain),
        })
    return {
        "chains": result,
        "note": "Methodology chains. For SDLC policy profiles (simplified/default/full), use --profiles.",
    }


def query_profile(paths: Dict[str, Path], profile_name: str) -> Dict[str, Any]:
    """Query an SDLC profile (simplified, default, full).

    An SDLC profile is a POLICY wrapper that determines which methodology
    models are available to a project and how strictly stages are enforced.
    The profile does not itself define a chain — it references methodology
    models (each of which has its own chain).
    """
    profile_path = paths["config"] / "sdlc-profiles" / f"{profile_name}.yaml"
    data = load_config(profile_path)
    if not data:
        available = [f.stem for f in (paths["config"] / "sdlc-profiles").glob("*.yaml")]
        return {"error": f"SDLC profile '{profile_name}' not found", "available": available}

    return {
        "profile": data.get("profile", data.get("chain", profile_name)),
        "description": data.get("description"),
        "applicability": data.get("applicability", {}),
        "execution": data.get("execution", {}),
        "enforcement": data.get("enforcement", {}),
        "methodology": data.get("methodology", {}),
        "tracking": data.get("tracking", {}),
        "upgrade_triggers": data.get("upgrade_triggers", []),
    }


def query_profiles_list(paths: Dict[str, Path]) -> Dict[str, Any]:
    """List all available SDLC profiles."""
    profiles_dir = paths["config"] / "sdlc-profiles"
    if not profiles_dir.exists():
        return {"error": "No sdlc-profiles directory found", "profiles": []}

    result = []
    for f in sorted(profiles_dir.glob("*.yaml")):
        data = load_config(f)
        if data:
            result.append({
                "name": data.get("profile", data.get("chain", f.stem)),
                "description": data.get("description", ""),
                "phases": data.get("applicability", {}).get("phases", []),
                "scale": data.get("applicability", {}).get("scale", []),
                "available_models": data.get("methodology", {}).get("available_models", []),
            })
    return {
        "profiles": result,
        "note": "SDLC policy profiles. For methodology chains per model, use --chains.",
    }


def query_health(paths: Dict[str, Path]) -> Dict[str, Any]:
    """Composite methodology + quality health score for the wiki.

    Resolves Q23 + Q24 from the operator decision queue. ONE composite score
    (not two separate ones — per the Q24 resolution to avoid vanity metrics)
    with per-dimension breakdown, derived from existing pipeline/lint/stats
    data. No new measurement infrastructure required.

    Six dimensions, weighted:
      1. Validation (30%) — 0 errors required for full score
      2. Evolution progression (20%) — % of pages past 00_inbox
      3. Relationship density (15%) — avg relationships per page
      4. Queue sync (10%) — resolved operator decisions + drift count
      5. Freshness (10%) — % of pages updated within 90 days
      6. Ingestion backlog (15%) — raw files pending vs wiki pages

    Returns score 0-100, letter grade, per-dimension breakdown, and up to
    3 actionable recommendations targeting the weakest dimensions.
    """
    from tools.stats import build_stats
    from tools.lint import lint_wiki, LintConfig
    from tools.validate import validate_page
    import re as _re

    wiki_dir = paths["wiki"]

    # Collect data from existing tooling
    stats = build_stats(wiki_dir)
    lint_config = LintConfig(
        stale_threshold_days=90,
        min_summary_words=30,
        min_deep_analysis_words=100,
        min_relationships=1,
        min_domain_pages=3,
        min_cross_domain_rels=2,
        similarity_threshold=0.70,
    )
    lint_report = lint_wiki(wiki_dir, lint_config)

    total_pages = stats["total_pages"]
    dimensions: Dict[str, Dict[str, Any]] = {}

    # Dimension 1 — Validation (30%)
    val_errors = lint_report["summary"].get("total_issues", 0)
    if val_errors == 0:
        val_score = 100
    elif val_errors < 5:
        val_score = 70
    elif val_errors < 10:
        val_score = 40
    else:
        val_score = 0
    dimensions["validation"] = {
        "score": val_score,
        "weight": 30,
        "detail": f"{val_errors} blocking lint/validation issue(s)",
    }

    # Dimension 2 — Evolution progression (20%)
    # Count pages outside 00_inbox folders
    inbox_pages = 0
    for md in wiki_dir.rglob("00_inbox/**/*.md"):
        if md.name != "_index.md":
            inbox_pages += 1
    matured = max(total_pages - inbox_pages, 0)
    evo_score = int(100 * matured / max(total_pages, 1))
    dimensions["evolution"] = {
        "score": evo_score,
        "weight": 20,
        "detail": f"{matured}/{total_pages} pages past 00_inbox ({inbox_pages} still in inbox)",
    }

    # Dimension 3 — Relationship density (15%)
    avg_rels = stats["relationship_density"]["average_per_page"]
    if avg_rels >= 6:
        rel_score = 100
    elif avg_rels >= 4:
        rel_score = int(50 + (avg_rels - 4) * 25)
    else:
        rel_score = max(0, int(avg_rels * 12.5))
    dimensions["relationships"] = {
        "score": rel_score,
        "weight": 15,
        "detail": f"avg {avg_rels} relationships/page (healthy ≥6, weak <4)",
    }

    # Dimension 4 — Queue sync (10%)
    queue_path = wiki_dir / "backlog" / "operator-decision-queue.md"
    queue_score = 100
    queue_detail = "queue not found"
    if queue_path.exists():
        try:
            qtext = queue_path.read_text(encoding="utf-8")
            # Resolved rows: | ~~N~~ |
            resolved = len(_re.findall(r"^\|\s*~~\d+[a-z]?~~\s*\|", qtext, _re.MULTILINE))
            # Open rows: | N | (bare integer)
            open_rows = len(_re.findall(r"^\|\s*\d+[a-z]?\s*\|", qtext, _re.MULTILINE))
            total_q = resolved + open_rows
            drift = lint_report["summary"].get("queue_drift", 0)
            if total_q > 0:
                base = int(100 * resolved / total_q)
                # Drift penalty: -10 per drift candidate, min 0
                queue_score = max(0, base - drift * 10)
                queue_detail = f"{resolved}/{total_q} resolved ({open_rows} open, {drift} drift candidate(s))"
        except Exception:
            queue_detail = "queue parse failed"
    dimensions["queue_sync"] = {
        "score": queue_score,
        "weight": 10,
        "detail": queue_detail,
    }

    # Dimension 5 — Freshness (10%)
    fresh = stats["freshness"]
    recent = fresh.get("<7d", 0) + fresh.get("<30d", 0) + fresh.get("<90d", 0)
    fresh_score = int(100 * recent / max(total_pages, 1))
    dimensions["freshness"] = {
        "score": fresh_score,
        "weight": 10,
        "detail": f"{recent}/{total_pages} pages updated within 90d",
    }

    # Dimension 6 — Ingestion backlog (15%)
    # True backlog = raw files NOT referenced by any wiki page's frontmatter
    # sources: field. Raw files ARE preserved indefinitely as audit trail
    # after synthesis — they're not removed. Counting all of them as
    # "backlog" overstates the problem. Count only unreferenced ones.
    raw_dir = paths["root"] / "raw"
    all_raw: List[Path] = []
    if raw_dir.exists():
        for sub in ["articles", "dumps", "notes", "papers", "transcripts"]:
            d = raw_dir / sub
            if d.exists():
                for f in d.iterdir():
                    if f.is_file() and f.name != ".gitkeep":
                        all_raw.append(f)

    # Collect referenced raw paths from wiki page frontmatter
    referenced: set = set()
    for page in wiki_dir.rglob("*.md"):
        if page.name == "_index.md":
            continue
        try:
            ptext = page.read_text(encoding="utf-8")
            meta, _ = parse_frontmatter(ptext)
            if not meta:
                continue
            for src in meta.get("sources", []) or []:
                if isinstance(src, dict) and "file" in src:
                    referenced.add(str(src["file"]).strip())
        except Exception:
            continue

    # Count raw files NOT referenced
    unreferenced_raw: List[str] = []
    for f in all_raw:
        rel = f.relative_to(paths["root"])
        if str(rel) not in referenced:
            unreferenced_raw.append(str(rel))

    raw_total = len(all_raw)
    raw_pending = len(unreferenced_raw)
    ratio = raw_pending / max(total_pages, 1)
    if ratio <= 0.25:
        backlog_score = 100
    elif ratio >= 0.75:
        backlog_score = 0
    else:
        backlog_score = int(100 * (0.75 - ratio) / 0.5)
    dimensions["ingestion_backlog"] = {
        "score": backlog_score,
        "weight": 15,
        "detail": f"{raw_pending} unreferenced raw files ({raw_total} total in raw/, {raw_total - raw_pending} already synthesized) vs {total_pages} wiki pages — ratio {ratio:.2f}; healthy ≤0.25",
    }

    # Composite
    composite = sum(d["score"] * d["weight"] for d in dimensions.values()) / 100
    composite = round(composite, 1)

    # Letter grade
    if composite >= 95:
        grade = "A+"
    elif composite >= 90:
        grade = "A"
    elif composite >= 80:
        grade = "B"
    elif composite >= 70:
        grade = "C"
    elif composite >= 60:
        grade = "D"
    else:
        grade = "F"

    # Recommendations — target the weakest-scored dimensions
    weak = sorted(dimensions.items(), key=lambda kv: kv[1]["score"])
    recommendations = []
    for name, d in weak[:3]:
        if d["score"] >= 90:
            break  # already strong; no recommendation needed
        if name == "validation":
            recommendations.append(f"Run `pipeline post` and fix the {d['detail']}.")
        elif name == "evolution":
            recommendations.append(f"Promote pages from 00_inbox — {d['detail']}. Review drafts for synthesis candidates.")
        elif name == "relationships":
            recommendations.append(f"Strengthen cross-page links — {d['detail']}. Add BUILDS ON / DERIVED FROM verbs to under-connected pages.")
        elif name == "queue_sync":
            recommendations.append(f"Sync the operator-decision queue — {d['detail']}. Run `python3 -m tools.lint` to see drift candidates.")
        elif name == "freshness":
            recommendations.append(f"Review stale pages — {d['detail']}. Update or archive pages >90d old.")
        elif name == "ingestion_backlog":
            recommendations.append(f"Process raw/ files — {d['detail']}. Run `pipeline ingest <file>` or batch-process.")

    return {
        "composite_score": composite,
        "grade": grade,
        "total_pages": total_pages,
        "dimensions": dimensions,
        "recommendations": recommendations,
        "note": "Composite of 6 dimensions — methodology+quality health unified per Q24 resolution (not two separate scores).",
    }


def query_compliance(paths: Dict[str, Path]) -> Dict[str, Any]:
    """Super-model compliance checker — report project's adoption tier and gaps.

    Resolves Q25 from the operator decision queue. Reads the project's
    structure (CLAUDE.md, methodology.yaml, wiki/, tools/) and reports
    which super-model adoption tier the project has reached, which
    requirements are met per tier, and what's missing to advance.

    Four adoption tiers (from wiki/spine/super-model/super-model.md):
      Tier 1 — Agent Foundation: CLAUDE.md + wiki-schema.yaml + templates
      Tier 2 — Stage-Gate Process: methodology.yaml + backlog hierarchy
      Tier 3 — Evolution Pipeline: evolve tool + maturity folders
      Tier 4 — Hub Integration: export profiles + MCP server

    Returns current_tier (highest fully met), max_tier (4), per-tier
    requirement checklists with met/missing, and up to 3 actionable
    recommendations for advancing to the next tier.
    """
    root = paths["root"]
    wiki = paths["wiki"]

    def _check(path_spec: str, description: str) -> Dict[str, Any]:
        """Check if a path exists. path_spec is relative to project root."""
        exists = (root / path_spec).exists()
        return {"path": path_spec, "description": description, "met": exists}

    # Tier 1 — Agent Foundation
    tier1 = {
        "name": "Agent Foundation",
        "description": "Structured knowledge base with schema + templates + routing",
        "requirements": [
            _check("CLAUDE.md", "Project routing table / context for Claude"),
            _check("wiki/config/wiki-schema.yaml", "Frontmatter schema defining valid page types"),
            _check("wiki/config/templates", "Page templates directory (scaffolds for each type)"),
        ],
    }

    # Tier 2 — Stage-Gate Process
    tier2 = {
        "name": "Stage-Gate Process",
        "description": "Methodology engine + work tracking + stage discipline",
        "requirements": [
            _check("wiki/config/methodology.yaml", "Methodology models with stage chains"),
            _check("wiki/backlog", "Backlog hierarchy directory (milestones/epics/modules/tasks)"),
            _check("AGENTS.md", "Universal cross-tool agent context (three-layer pattern)"),
        ],
    }

    # Tier 3 — Evolution Pipeline
    # Maturity folders: wiki has multiple subdirs with 00_inbox, 01_drafts, etc.
    maturity_dirs = ["lessons", "patterns", "decisions"]
    maturity_met = all(
        (wiki / d / "00_inbox").exists() or (wiki / d / "01_drafts").exists()
        for d in maturity_dirs
    )
    tier3 = {
        "name": "Evolution Pipeline",
        "description": "Self-improving wiki with maturity lifecycle + scoring + promotion",
        "requirements": [
            _check("tools/evolve.py", "Evolution scoring + promotion tooling"),
            {
                "path": "wiki/{lessons,patterns,decisions}/00_inbox",
                "description": "Maturity lifecycle folders (00_inbox → 01_drafts → 02_synthesized → 03_validated → 04_principles)",
                "met": maturity_met,
            },
            _check("tools/lint.py", "Quality/drift detection (includes queue-drift check)"),
        ],
    }

    # Tier 4 — Hub Integration
    tier4 = {
        "name": "Hub Integration",
        "description": "Ecosystem participation — export, MCP, bidirectional knowledge flow",
        "requirements": [
            _check("wiki/config/export-profiles.yaml", "Export transforms for sister projects"),
            _check("tools/mcp_server.py", "MCP server exposing wiki operations"),
            _check(".mcp.json", "MCP server registration for Claude Code"),
        ],
    }

    tiers = [tier1, tier2, tier3, tier4]

    # Compute current tier — highest FULLY met (tiers are cumulative)
    current_tier = 0
    for i, tier in enumerate(tiers, 1):
        if all(req["met"] for req in tier["requirements"]):
            current_tier = i
        else:
            break

    # Gather gaps across all tiers
    gaps: List[Dict[str, Any]] = []
    for i, tier in enumerate(tiers, 1):
        for req in tier["requirements"]:
            if not req["met"]:
                gaps.append({
                    "tier": i,
                    "tier_name": tier["name"],
                    "missing": req["path"],
                    "description": req["description"],
                })

    # Recommendations — target the NEXT tier up
    recommendations: List[str] = []
    if current_tier < 4:
        next_tier = tiers[current_tier]  # 0-indexed; current_tier is already the next
        missing_in_next = [req for req in next_tier["requirements"] if not req["met"]]
        if missing_in_next:
            recommendations.append(
                f"To reach Tier {current_tier + 1} ({next_tier['name']}), add: "
                + ", ".join(req["path"] for req in missing_in_next)
            )
        for req in missing_in_next[:2]:
            recommendations.append(f"Missing: {req['path']} — {req['description']}")
    else:
        recommendations.append(
            "At Tier 4 (Hub Integration) — the highest adoption tier. No gaps to fill."
        )

    return {
        "current_tier": current_tier,
        "max_tier": 4,
        "current_tier_name": tiers[current_tier - 1]["name"] if current_tier > 0 else "Not yet adopted",
        "tiers": tiers,
        "gaps": gaps,
        "recommendations": recommendations,
        "note": "Super-model adoption tiers are CUMULATIVE — Tier N requires all Tiers 1..N to be met.",
    }


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
    q.add_argument("--chain", help="Query the methodology chain for a model (artifact sequence per stage)")
    q.add_argument("--chains", action="store_true", help="List all methodology models with their chains")
    q.add_argument("--profile", help="Query an SDLC policy profile (simplified, default, full)")
    q.add_argument("--profiles", action="store_true", help="List all SDLC policy profiles")
    q.add_argument("--mapping", nargs="?", const="__all__", help="Query location mapping (optionally for a specific title)")
    q.add_argument("--backlog", action="store_true", help="Show backlog status (epics, readiness, impediments)")
    q.add_argument("--lessons", action="store_true", help="Show lessons by maturity folder")
    q.add_argument("--logs", action="store_true", help="Show recent log entries")
    q.add_argument("--page", help="Look up a page by title (metadata + summary)")
    q.add_argument("--docs", nargs="?", const="__list__", help="List root-level documentation files (or pass a name like 'README', 'AGENTS', 'CLAUDE', 'TOOLS')")

    # Flow command — step-by-step Goldilocks routing
    f = sub.add_parser("flow", help="Goldilocks flow — step-by-step routing from identity to action")
    f.add_argument("--step", type=int, help="Jump to a specific step (1-8)")

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

    # Health score (Q23+Q24)
    sub.add_parser("health", help="Composite methodology+quality health score with per-dimension breakdown")

    # Compliance checker (Q25)
    sub.add_parser("compliance", help="Super-model compliance checker — adoption tier + gaps")

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

    # Factory reset command
    fr = sub.add_parser("factory-reset", help="Reset wiki to clean template state (DANGEROUS)")
    fr.add_argument("--confirm", action="store_true", help="Required to actually execute reset")

    # Contribute command
    ct = sub.add_parser("contribute", help="Write back to the wiki (lands in 00_inbox / log; promotion requires review)")
    ct.add_argument("--type", required=True, choices=["lesson", "remark", "correction"])
    ct.add_argument("--title", required=True)
    ct.add_argument("--content", required=True)
    ct.add_argument("--domain", default="cross-domain")
    ct.add_argument("--contributor", help="Contributor identifier (e.g. 'openarms-harness-v10'). Default: user@host")
    ct.add_argument("--source", help="Origin path of contribution (e.g. '/home/jfortin/openarms'). Default: self")
    ct.add_argument("--reason", help="Why this contribution is being made (optional audit trail)")

    args = parser.parse_args()
    paths = resolve_paths(
        wiki_root=args.wiki_root if hasattr(args, "wiki_root") else None,
        brain_root=args.brain if hasattr(args, "brain") else None,
    )

    if args.command == "what-do-i-need":
        print(query_what_do_i_need(paths))

    elif args.command == "compliance":
        result = query_compliance(paths)
        print(f"\nSuper-Model Compliance — Tier {result['current_tier']} / {result['max_tier']}  ({result['current_tier_name']})")
        print(f"{result['note']}")
        print("")
        for i, tier in enumerate(result["tiers"], 1):
            met_count = sum(1 for r in tier["requirements"] if r["met"])
            total = len(tier["requirements"])
            mark = "✓" if met_count == total else ("⚠" if met_count > 0 else "✗")
            print(f"{mark} Tier {i} — {tier['name']}  ({met_count}/{total} requirements met)")
            print(f"    {tier['description']}")
            for req in tier["requirements"]:
                symbol = "✓" if req["met"] else "✗"
                print(f"      {symbol} {req['path']}  — {req['description']}")
            print("")
        if result["recommendations"]:
            print("Recommendations:")
            for i, rec in enumerate(result["recommendations"], 1):
                print(f"  {i}. {rec}")
            print("")

    elif args.command == "health":
        result = query_health(paths)
        # Human-readable format
        print(f"\nWiki Health Score: {result['composite_score']} / 100  ({result['grade']})")
        print(f"Pages: {result['total_pages']}")
        print("")
        print("Dimensions:")
        for name, d in result["dimensions"].items():
            bar = "█" * (d["score"] // 10) + "░" * (10 - d["score"] // 10)
            print(f"  {name:22s} [{bar}] {d['score']:3d}/100 ({d['weight']}%)  — {d['detail']}")
        if result["recommendations"]:
            print("")
            print("Recommendations (targeting weakest dimensions):")
            for i, rec in enumerate(result["recommendations"], 1):
                print(f"  {i}. {rec}")
        print("")
        print(f"  {result['note']}")

    elif args.command == "flow":
        print(cmd_flow(paths, step=getattr(args, "step", None)))

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
        elif args.profile:
            result = query_profile(paths, args.profile)
        elif args.profiles:
            result = query_profiles_list(paths)
        elif args.chains:
            result = query_chains_list(paths)
        elif args.field:
            result = query_field(paths, args.field)
        elif args.mapping is not None:
            title = None if args.mapping == "__all__" else args.mapping
            result = query_location_mapping(paths, title)
        elif args.backlog:
            result = query_backlog(paths)
        elif args.lessons:
            result = query_lessons(paths)
        elif args.logs:
            result = query_logs(paths)
        elif args.page:
            result = query_page(paths, args.page)
        elif args.docs is not None:
            doc_arg = None if args.docs == "__list__" else args.docs
            result = query_docs(paths, doc_arg)
        else:
            # No args to query → show navigate instead of argparse error
            print("No query specified. Try one of:")
            print("  gateway query --identity        → who am I?")
            print("  gateway query --models           → what methodology models exist?")
            print("  gateway query --chains           → all methodology chains (artifact sequences)")
            print("  gateway query --chain <model>    → artifact chain for ONE methodology model")
            print("  gateway query --profiles         → all SDLC policy profiles (simplified/default/full)")
            print("  gateway query --profile <name>   → details on ONE SDLC profile")
            print("  gateway query --stage <name>    → what does a stage need?")
            print("  gateway query --model <name>    → model details (includes chain)")
            print("  gateway query --field <name>    → explain a field")
            print("  gateway query --docs             → list root-level docs (README, AGENTS, CLAUDE, etc.)")
            print("  gateway query --docs <name>      → details on one root doc")
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

    elif args.command == "factory-reset":
        result = op_factory_reset(paths, confirm=args.confirm)
        print(json.dumps(result, indent=2, default=str))

    elif args.command == "contribute":
        result = op_contribute(
            paths, args.type, args.title, args.content, args.domain,
            contributor=getattr(args, "contributor", None),
            source=getattr(args, "source", None),
            reason=getattr(args, "reason", None),
        )
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

        # SDLC Profile
        profile_name = (id_data.get("sdlc chain", id_data.get("sdlc profile", "")).split("(")[0].strip().lower()
                        if id_data else "default")
        profile_data = query_profile(paths, profile_name) if profile_name else {}
        if "error" not in profile_data:
            print(f"SDLC PROFILE: {profile_data.get('profile', '?')} — {profile_data.get('description', '')}")
            methodology = profile_data.get("methodology", {})
            available = methodology.get("available_models", [])
            if available:
                print(f"  Available models: {', '.join(available[:5])}" + (" ..." if len(available) > 5 else ""))
            enforcement = profile_data.get("enforcement", {})
            if enforcement:
                print(f"  Enforcement level: {enforcement.get('level', '?')}")
                print(f"  Stage gates: {enforcement.get('stage_gates', '?')}")
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
        print("  gateway query --model <name> --full-chain → full artifact chain for model")
        print("  gateway query --chain <model-name>        → methodology chain (artifact sequence per stage)")
        print("  gateway query --chains                    → all methodology chains")
        print("  gateway query --profile <name>            → SDLC policy profile details")
        print("  gateway query --profiles                  → all SDLC profiles (simplified/default/full)")
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
            print("├── SDLC PROFILES → gateway query --profiles")
            print("│   ├── simplified (POC, micro/small)")
            print("│   ├── default (MVP→Staging, small→medium) ← most projects")
            print("│   └── full (Production, medium→massive)")
            print("│")
            print("├── METHODOLOGY CHAINS → gateway query --chains")
            print("│   ├── One chain per methodology model (feature-development, bug-fix, ...)")
            print("│   └── Each chain = artifact sequence per stage")
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
        print("  gateway status                → see your project identity + SDLC profile + models")
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
