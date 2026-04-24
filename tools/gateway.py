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
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.common import (
    CONSUMER_RUNTIME_DEFAULT,
    CONSUMER_RUNTIME_ENV,
    consumer_runtime_is_declared,
    detect_context,
    find_wiki_pages,
    get_consumer_runtime,
    get_project_root,
    load_config,
    parse_frontmatter,
    parse_relationships,
    parse_sections,
    write_session_state,
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
            # Look for common second brain locations (canonical + aliases)
            _brain_names = [
                "devops-solutions-information-hub",
                "devops-solutions-research-wiki",
            ]
            _search_dirs = [local_root.parent, Path.home()]
            candidates = [d / n for d in _search_dirs for n in _brain_names]
            for candidate in candidates:
                if (candidate / "wiki" / "config" / "methodology.yaml").exists():
                    brain_path = candidate
                    break
            else:
                brain_path = local_root  # Fallback to local

    brain_wiki = brain_path / "wiki" if (brain_path / "wiki").exists() else brain_path
    brain_config = brain_wiki / "config"

    # Resolve local config — the project's OWN schema, methodology, templates
    local_config = local_wiki / "config" if (local_wiki / "config").exists() else None
    # For schema: use the PROJECT's own schema first, fall back to brain's
    # F1/F2 fix: consumer projects have their own schema — use it for validation
    local_schema = None
    if local_config:
        for candidate in ["wiki-schema.yaml", "schema.yaml"]:
            if (local_config / candidate).exists():
                local_schema = local_config / candidate
                break
    # For methodology: project's own first, brain's as reference
    local_methodology = None
    if local_config and (local_config / "methodology.yaml").exists():
        local_methodology = local_config / "methodology.yaml"

    return {
        "root": local_root,
        "wiki": local_wiki,
        "local_config": local_config or brain_config,
        # Brain paths — where methodology, standards, chains, templates live (reference)
        "brain_root": brain_path,
        "brain_wiki": brain_wiki,
        "brain_config": brain_config,
        # Active config — local when available, brain as fallback
        # This is what validation/lint/health should use
        "config": local_config or brain_config,
        "methodology": local_methodology or brain_config / "methodology.yaml",
        "artifact_types": (local_config / "artifact-types.yaml") if local_config and (local_config / "artifact-types.yaml").exists() else brain_config / "artifact-types.yaml",
        "schema": local_schema or brain_config / "wiki-schema.yaml",
        "templates": (local_config / "templates") if local_config and (local_config / "templates").exists() else brain_config / "templates",
        # Whether local and brain are the same
        "is_brain": str(local_root.resolve()) == str(brain_path.resolve()),
    }


# ---------------------------------------------------------------------------
# Orient: context-aware onboarding for fresh agents (E022-M002)
# Design: wiki/backlog/modules/e022-m002-gateway-orient-subcommand.md
# ---------------------------------------------------------------------------

def gateway_orient(paths: Dict[str, Path], args) -> None:
    """Orient — context-aware onboarding.

    Answers: 'who are you, where, are you fresh, what must you internalize?'
    Branches on (location × freshness) per E022-M002 dispatch matrix.
    Honors Gateway Output Contract: SRP, context-aware, size ceiling,
    read-whole marker, closing next-move.
    """
    context = detect_context(
        wiki_root=paths.get("root"),
        brain_root=paths.get("brain_root"),
        orient_as=getattr(args, "orient_as", None),
        fresh=getattr(args, "fresh", False),
    )

    location = context["location"]
    freshness = context["freshness"]
    fmt = getattr(args, "orient_format", "text")

    if fmt == "json":
        import json as _json
        print(_json.dumps({"location": location, "freshness": freshness,
                           "consumer_runtime": context["consumer_runtime"],
                           "next": _orient_next_move(location, freshness)}, indent=2))
    elif location == "second-brain" and freshness == "fresh":
        _orient_brain_fresh()
    elif location == "second-brain":
        _orient_second_brain_returning(freshness)
    elif location == "sister" and freshness == "fresh":
        _orient_sister_fresh()
    elif location == "sister":
        _orient_sister_returning(freshness)
    else:
        _orient_external()

    write_session_state(context, subcommand="orient")


def _orient_next_move(location: str, freshness: str) -> str:
    """Determine the NEXT command for closing-next-move rule."""
    if freshness == "fresh":
        return "gateway what-do-i-need"
    if location == "sister":
        return "gateway query --model <type> --brain"
    return "gateway what-do-i-need"


def _orient_brain_fresh() -> None:
    """Full orient output for second-brain + fresh agent."""
    print("""\u26a0 READ THIS OUTPUT IN FULL \u2014 every section changes how you operate here.

ORIENT \u2014 You are inside the research wiki (the ecosystem's second brain)
==========================================================================

CRITICAL DISTINCTION \u2014 your brain \u2260 the second brain:
  Your brain = CLAUDE.md + AGENTS.md + skills + hooks + commands. Per-project.
  Constitutes YOUR agent. Every project in this ecosystem has its own brain.
  The second brain = THIS wiki. A shared knowledge system holding methodology,
  standards, lessons, patterns, decisions across 5 projects. Projects consume
  from it. Projects contribute to it. It validates itself with its own
  methodology. 360+ pages, 2400+ relationships, 16 models, 4 principles.

FOUR PRINCIPLES (these govern every decision you make here):
  1. Infrastructure > Instructions \u2014 if a rule can be checked by a tool,
     enforce it structurally (hooks, validators), not with prose. Prose = 25%
     compliance. Hooks = 100%. This is measured, not theoretical.
  2. Structured Context > Content \u2014 tables, MUST/MUST NOT lists, YAML fields
     program your behavior more reliably than paragraphs. Design injections as
     structured programs, not natural language.
  3. Goldilocks \u2014 process adapts to identity (type \u00d7 phase \u00d7 scale \u00d7 PM level).
     A POC doesn't need full enforcement. Production does. Don't hardcode one
     process level for all contexts.
  4. Declarations Are Aspirational Until Infrastructure Verifies Them \u2014
     any declaration (name, field, attribute, claim, tier) is aspirational
     unless a gate verifies it holds. Generalizes #1 from process rules to
     every layer. 5 validated instances. Fix: pair every declaration with a
     verification gate, or rename/demote to match reality.

WHAT WE DO (10 knowledge-project verbs \u2014 this is NOT app development):
  aggregate \u2192 process \u2192 evaluate \u2192 learn \u2192 integrate \u2192
  modelize \u2192 validate \u2192 standardize \u2192 teach \u2192 offer

RULES THAT PREVENT THE ERRORS YOU WILL OTHERWISE MAKE:
  - Log operator directives verbatim in raw/notes/ BEFORE acting on them
  - Read files in FULL \u2014 never truncate, never skim. "20 lines of 20M then
    pretend you know everything" is the named illness. The operator catches it.
  - When a question comes up, answer it yourself first and present for
    confirmation. Don't leave floating questions. Don't present menus.
  - When something is blocked, build the tool to unblock it. Never hand
    work back to the operator as a manual step.
  - Run `pipeline post` after every wiki change \u2014 0 errors. Not advisory.
  - Use this gateway (`orient` \u2192 `what-do-i-need`) for routing. Do NOT
    improvise your own onboarding plan.
  - Browse the wiki with `python3 -m tools.view` (spine, models, lessons,
    patterns, search). This is the primary interface for reading content.

READ THE BASE (each builds on the previous):
  1. wiki/spine/super-model/super-model.md         \u2192 what this system IS
  2. wiki/spine/references/model-registry.md        \u2192 the 16 models
  3. model-llm-wiki \u2192 model-methodology \u2192 model-wiki-design (foundations)
  4. wiki/lessons/04_principles/hypothesis/          \u2192 4 principles in full
  5. wiki/spine/standards/                           \u2192 what "good" looks like
  Complete path: wiki/spine/learning-paths/methodology-fundamentals.md

NEXT: gateway what-do-i-need    (after you have internalized the base)""")


def _orient_second_brain_returning(freshness: str) -> None:
    """Redirect for second-brain + task-bound/returning agent."""
    print(f"""ORIENT \u2014 You are inside the second brain ({freshness})

You already know the base. Proceed to task routing.

NEXT: gateway what-do-i-need""")


def _orient_sister_fresh() -> None:
    """Full orient for sister project + fresh agent."""
    print("""\u26a0 READ THIS OUTPUT IN FULL \u2014 every section matters for integration.

ORIENT \u2014 Sister project connecting to the second brain
========================================================

YOUR BRAIN IS YOUR OWN: your CLAUDE.md, AGENTS.md, skills, hooks, commands.
These constitute YOUR agent. The second brain is a SEPARATE shared knowledge
system. Your goal is NOT to depend on it at runtime \u2014 it's to ADOPT what
fits your identity and evolve your own brain until it's strong on its own.

ADOPTION TIERS (where is your project?):
  Tier 1 \u2014 Agent Foundation:    CLAUDE.md + schema + templates
  Tier 2 \u2014 Stage-Gate Process:  methodology.yaml + backlog + enforcement
  Tier 3 \u2014 Evolution Pipeline:  maturity lifecycle + scoring + promotion
  Tier 4 \u2014 Hub Integration:     bidirectional sync + export + contribute

  Check your tier:  python3 -m tools.gateway compliance
  Full integration is 15-25 epics, 80-150+ tasks across months.
  Start with your current tier's gaps. Don't try to jump to Tier 4.

FOUR PRINCIPLES (adopt these into YOUR brain):
  1. Infrastructure > Instructions \u2014 enforce rules structurally, not in prose
  2. Structured Context > Content \u2014 structure programs agent behavior
  3. Goldilocks \u2014 right process for YOUR project's identity and phase
  4. Declarations Are Aspirational Until Verified \u2014 pair every declared
     name/field/attribute/claim with a verification gate, or rename/demote

WHAT TO READ FIRST (standards before models for integration):
  1. python3 -m tools.view standards    \u2192 what "good" looks like per artifact
  2. python3 -m tools.view spine        \u2192 all 16 models + sub-models
  3. python3 -m tools.view model methodology \u2192 how work proceeds (9 models)
  4. python3 -m tools.view lessons      \u2192 validated operational knowledge
  5. python3 -m tools.view patterns     \u2192 recurring structural patterns

HOW TO QUERY (once you know what you need):
  CLI:  python3 -m tools.gateway query --model <type>
  CLI:  python3 -m tools.gateway query --stage <name> --domain <yours>
  MCP:  wiki_gateway_query(model="<type>")

HOW TO CONTRIBUTE BACK:
  CLI:  python3 -m tools.gateway contribute --type lesson --title "..."
  Your format is accepted \u2014 the second brain normalizes on intake.

NEXT: python3 -m tools.gateway compliance   (see where you are)""")


def _orient_sister_returning(freshness: str) -> None:
    """Redirect for sister + task-bound/returning."""
    print(f"""ORIENT — Sister project ({freshness})

You have prior context. Route directly to brain queries.

NEXT: gateway query --model <task-type> --brain""")


def _orient_external() -> None:
    """Orient for external MCP client (no repo context)."""
    print("""ORIENT — External MCP client

Available MCP tools: wiki_status, wiki_search, wiki_read_page,
  wiki_gateway_query, wiki_gateway_docs, wiki_gateway_contribute,
  wiki_gateway_flow, wiki_gateway_template, wiki_gateway_timeline, ...

Start with:
  wiki_status              → wiki health snapshot
  wiki_gateway_docs        → root documentation list
  wiki_search              → keyword search across wiki

One-shot orientation:
  wiki_read_page("super-model")

NEXT: wiki_status    (start with status)""")


# ---------------------------------------------------------------------------
# What-do-i-need: context-aware output helpers (E022-M003)
# ---------------------------------------------------------------------------

def _wdin_brain_task_bound() -> str:
    """Brain-self + task-bound: knowledge-verb task routing table."""
    return """\u26a0 READ THIS OUTPUT IN FULL \u2014 routing depends on the task-type table.

WHAT DO YOU NEED? \u2014 Inside the second brain (the research wiki)

  Task type               | Verbs activated               | Entry
  ------------------------|-------------------------------|------------------------
  Ingest source           | aggregate \u2192 process            | skill: wiki-agent
                          |   \u2192 integrate \u2192 validate     |
  Evolve candidate        | evaluate \u2192 learn              | skill: evolve
                          |   \u2192 integrate \u2192 validate     |
  Promote to principle    | evaluate \u2192 modelize           | gateway query --review
                          |   \u2192 validate                   |
  Author standards        | modelize \u2192 standardize        | skill: model-builder
                          |   \u2192 teach \u2192 validate         |
  Aggregation sweep       | aggregate \u2192 integrate         | sister_project + timeline
                          |   \u2192 evaluate (read-only)       |
  Cross-ecosystem retro   | aggregate \u2192 integrate         | timeline --scope all
                          |   (timeline) \u2192 evaluate        |
  Expose new tool         | offer \u2192 validate              | tools/gateway.py + mcp_server.py

  Not listed? \u2192 gateway orient  (for full base context)

NEXT: gateway query --task <type>    (loads verb chain for that task)"""


def _wdin_sister(project_name: str) -> str:
    """Sister + task-bound: methodology models to adopt from the second brain."""
    return f"""\u26a0 READ THIS OUTPUT IN FULL \u2014 these are the models to adopt.

WHAT DO YOU NEED? \u2014 Sister project ({project_name}), task-bound

  These methodology models should be in YOUR project's methodology.yaml.
  If they're not, adopt the ones that match your work.

  Your task type        | Model                | Stages
  ----------------------|----------------------|-------------------------------
  Feature / epic        | feature-development  | document \u2192 design \u2192 scaffold \u2192 implement \u2192 test
  Bug fix               | bug-fix              | document \u2192 implement \u2192 test
  Research / spike      | research             | document \u2192 design (caps at 50%)
  Documentation         | documentation        | document
  Refactor              | refactor             | document \u2192 scaffold \u2192 implement \u2192 test
  Hotfix (known fix)    | hotfix               | implement \u2192 test
  Integration           | integration          | scaffold \u2192 implement \u2192 test

  Adopt a model:          gateway query --model <name> --full-chain
  Check stage rules:      gateway query --stage <name> --domain <yours>
  Check standards:        python3 -m tools.view standards
  After work, contribute: gateway contribute --type lesson --title "..."

NEXT: gateway query --model <task-type> --full-chain"""


def _wdin_external() -> str:
    """External MCP client: tool pointers."""
    return """WHAT DO YOU NEED? \u2014 External MCP client

  Available MCP tools: wiki_status, wiki_search, wiki_read_page,
    wiki_gateway_query, wiki_gateway_docs, wiki_gateway_contribute,
    wiki_gateway_flow, wiki_gateway_template, wiki_gateway_timeline, ...

  Start with:
    wiki_status              \u2192 wiki health snapshot
    wiki_gateway_docs        \u2192 root documentation list
    wiki_search              \u2192 keyword search across wiki

NEXT: wiki_status"""


# ---------------------------------------------------------------------------
# Query: methodology, stages, chains, artifacts, fields, identity
# ---------------------------------------------------------------------------

def query_what_do_i_need(paths: Dict[str, Path]) -> str:
    """Smart auto-routing: detect identity → recommend chain → show first steps.

    This is the "I don't know what I don't know" entry point.
    Detects as much as possible automatically, recommends next actions.

    E022-M003 upgrade: context-aware branching (brain / sister / external ×
    fresh / task-bound). SCAFFOLD adds detection call; implement stage adds
    real branches. See wiki/backlog/modules/e022-m003-what-do-i-need-upgrade.md
    """
    root = paths["root"]

    # E022-M003: context-aware branching (T-E022-11, T-E022-12)
    ctx = detect_context(
        wiki_root=paths.get("root"),
        brain_root=paths.get("brain_root"),
    )
    location = ctx["location"]
    freshness = ctx["freshness"]

    # Fresh agents (any location) → redirect to orient
    if freshness == "fresh":
        write_session_state(ctx, subcommand="what-do-i-need")
        ctx_label = ("the second brain" if location == "second-brain"
                     else "a sister project" if location == "sister"
                     else "an external client")
        return (
            "\u26a0 READ THIS OUTPUT IN FULL \u2014 you need orientation before routing.\n\n"
            f"WHAT DO YOU NEED? \u2014 You are {ctx_label}, but FRESH.\n\n"
            "You need orientation before task routing.\n\n"
            "NEXT: gateway orient    (internalize the base first)"
        )

    # Brain-self + task-bound → knowledge-verb task table
    if location == "second-brain":
        write_session_state(ctx, subcommand="what-do-i-need")
        return _wdin_brain_task_bound()

    # Sister + task-bound → brain query routing
    if location == "sister":
        write_session_state(ctx, subcommand="what-do-i-need")
        project_name = root.name if root else "unknown"
        return _wdin_sister(project_name)

    # External → MCP tool pointers
    if location == "external":
        write_session_state(ctx, subcommand="what-do-i-need")
        return _wdin_external()

    # -----------------------------------------------------------------------
    # LEGACY FALLBACK — reached only if detect_context returns an unrecognized
    # location (second-brain / sister / external cover all known cases).
    # This is the pre-E022 output. Kept as safety net; will be removed once
    # E022 test stage confirms all contexts are covered (T-E022-13).
    # -----------------------------------------------------------------------

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


_IDENTITY_HEADING_RE = re.compile(
    r"^#{1,6}\s+.*\b("
    r"Identity\s+Profile|"
    r"Project\s+Identity|"
    r"Goldilocks\s+Identity|"
    r"Goldilocks\s+Profile|"
    r"Identity\s*\(Goldilocks"
    r")\b",
    re.IGNORECASE,
)


def query_identity(paths: Dict[str, Path]) -> Dict[str, Any]:
    """Read the project's identity profile from CLAUDE.md.

    Matches a range of heading forms (Identity Profile, Project Identity,
    Goldilocks Profile, Identity (Goldilocks — ...)) since consumer projects
    vary in which prescribed template they adopted. Reported 2026-04-17 by
    openfleet-solo-session: heading '## Project Identity (Goldilocks ...)'
    was silently missed by the prior literal-substring match.
    """
    claude_md = paths["root"] / "CLAUDE.md"
    if not claude_md.exists():
        return {"error": "No CLAUDE.md found", "identity": None}

    text = claude_md.read_text(encoding="utf-8")
    identity = {}
    in_identity = False
    for line in text.split("\n"):
        if _IDENTITY_HEADING_RE.match(line):
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

    # Enrich from chain data — aggregate ALLOWED/FORBIDDEN from all models that have this stage
    # This fills the gap when standalone stage definitions are sparse but chain data is rich
    brain_config = paths.get("brain_config", paths["config"])
    brain_meth_path = brain_config / "methodology.yaml"
    if brain_meth_path.exists():
        brain_meth = load_config(brain_meth_path)
    else:
        brain_meth = methodology
    if brain_meth:
        chain_required = []
        chain_forbidden = []
        chain_gates = []
        models_with_stage = []
        for model_name, model_def in brain_meth.get("models", {}).items():
            chain = model_def.get("chain", {})
            if stage in chain:
                stage_chain = chain[stage]
                models_with_stage.append(model_name)
                for req in stage_chain.get("required", []):
                    artifact = req.get("artifact", "")
                    purpose = req.get("purpose", "")
                    if artifact and artifact not in [r.get("artifact") for r in chain_required]:
                        chain_required.append({"artifact": artifact, "purpose": purpose})
                for forb in stage_chain.get("forbidden", []):
                    if forb not in chain_forbidden:
                        chain_forbidden.append(forb)
                for check in stage_chain.get("gate", {}).get("checks", []):
                    if check not in chain_gates:
                        chain_gates.append(check)
        if chain_required:
            result["chain_required_artifacts"] = chain_required
        if chain_forbidden:
            result["chain_forbidden"] = chain_forbidden
        if chain_gates:
            result["chain_gate_checks"] = chain_gates
        if models_with_stage:
            result["models_using_this_stage"] = models_with_stage

    # Domain-specific overrides
    if domain:
        brain_config_dir = paths.get("brain_config", paths["config"])
        profile_path = brain_config_dir / "domain-profiles" / f"{domain}.yaml"
        if not profile_path.exists():
            profile_path = paths["config"] / "domain-profiles" / f"{domain}.yaml"
        profile = load_config(profile_path)
        if profile:
            overrides = profile.get("stage_overrides", {}).get(stage, {})
            if overrides:
                result["domain_overrides"] = overrides

    return result


def query_model(paths: Dict[str, Path], model_name: str, full_chain: bool = False) -> Dict[str, Any]:
    """Query a methodology model — stages, artifacts, chain.

    Uses local methodology for model listing. When full_chain is requested,
    falls back to the brain's methodology which has canonical chain definitions.
    """
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
        chain = model_def.get("chain", {})
        # If local methodology has no chains, try the brain's (canonical source)
        if not chain:
            brain_config = paths.get("brain_config")
            if brain_config:
                brain_meth = load_config(brain_config / "methodology.yaml")
                if brain_meth:
                    brain_model = brain_meth.get("models", {}).get(model_name, {})
                    chain = brain_model.get("chain", {})
        result["chain"] = chain

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
    """Explain a frontmatter field — what it means, valid values, what reads it.

    Checks local schema first, falls back to the brain's schema (which has
    the canonical field definitions including fields the local project may
    not use yet).
    """
    schema = load_config(paths["schema"])
    brain_schema = None
    brain_config = paths.get("brain_config")
    if brain_config:
        for candidate in ["wiki-schema.yaml", "schema.yaml"]:
            bp = brain_config / candidate
            if bp.exists():
                brain_schema = load_config(bp)
                break

    # Merge: local schema fields + brain schema fields (brain adds canonical definitions)
    all_required = set(schema.get("required_fields", []) if schema else [])
    all_optional = set(schema.get("optional_fields", []) if schema else [])
    all_enums = dict(schema.get("enums", {}) if schema else {})

    if brain_schema:
        all_required |= set(brain_schema.get("required_fields", []))
        all_optional |= set(brain_schema.get("optional_fields", []))
        for k, v in brain_schema.get("enums", {}).items():
            if k not in all_enums:
                all_enums[k] = v

    result = {"field": field_name}
    if field_name in all_required:
        result["required"] = True
        result["source"] = "local" if schema and field_name in schema.get("required_fields", []) else "second-brain"
    elif field_name in all_optional:
        result["required"] = False
        result["source"] = "local" if schema and field_name in schema.get("optional_fields", []) else "second-brain"
    else:
        result["error"] = f"Unknown field: {field_name}"
        result["available_required"] = sorted(all_required)
        result["available_optional"] = sorted(all_optional)
        return result

    if field_name in all_enums:
        result["valid_values"] = all_enums[field_name]

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
                  reason: str = None, target: str = "brain") -> Dict[str, Any]:
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

    # Target resolution. Default 'brain' means contributions land in the second
    # brain's intake even when invoked via a consumer forwarder that auto-adds
    # --wiki-root. Pass --target local to write to the caller's own wiki
    # instead (self-contribution). If no second brain is configured,
    # brain_wiki == wiki, so 'brain' falls back to local automatically.
    # Reported 2026-04-17 by openfleet-solo-session after two contributions
    # misfiled into /home/jfortin/openfleet/wiki/log/ instead of the brain's.
    if target == "local":
        wiki_dir = paths["wiki"]
    else:  # 'brain' (default) — may equal local when no brain is configured
        wiki_dir = paths.get("brain_wiki") or paths["wiki"]
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

## Applicability

Contributed from {source}. Applicability to be assessed during promotion review.

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

    Chains come from the BRAIN's methodology (canonical definitions).
    Local methodology tells you which models you USE; the brain's has the chains.

    For SDLC-level POLICY (simplified/default/full), use query_profile instead.
    """
    # Use brain's methodology for chains (canonical), fall back to local
    brain_config = paths.get("brain_config", paths["config"])
    methodology_path = brain_config / "methodology.yaml"
    if not methodology_path.exists():
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
    """List all methodology models with their chains.

    Uses brain's methodology for chain data (canonical definitions).
    """
    brain_config = paths.get("brain_config", paths["config"])
    methodology_path = brain_config / "methodology.yaml"
    if not methodology_path.exists():
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
    # SDLC profiles live in the brain's config (canonical reference)
    brain_config = paths.get("brain_config", paths["config"])
    profile_path = brain_config / "sdlc-profiles" / f"{profile_name}.yaml"
    if not profile_path.exists():
        profile_path = paths["config"] / "sdlc-profiles" / f"{profile_name}.yaml"
    data = load_config(profile_path)
    if not data:
        profiles_dir = brain_config / "sdlc-profiles"
        if not profiles_dir.exists():
            profiles_dir = paths["config"] / "sdlc-profiles"
        available = [f.stem for f in profiles_dir.glob("*.yaml")] if profiles_dir.exists() else []
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
    """List all available SDLC profiles. Uses brain's profiles as canonical."""
    brain_config = paths.get("brain_config", paths["config"])
    profiles_dir = brain_config / "sdlc-profiles"
    if not profiles_dir.exists():
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

    # Collect referenced paths AND URLs from wiki page frontmatter.
    # Raw files carry a `Source: <url>` header; synthesis pages often cite the
    # URL (not the cached file path). Without URL matching, every URL-sourced
    # raw file reads as unreferenced — inflating the backlog metric.
    referenced_paths: set = set()
    referenced_urls: set = set()
    for page in wiki_dir.rglob("*.md"):
        if page.name == "_index.md":
            continue
        try:
            ptext = page.read_text(encoding="utf-8")
            meta, _ = parse_frontmatter(ptext)
            if not meta:
                continue
            for src in meta.get("sources", []) or []:
                if isinstance(src, dict):
                    if "file" in src:
                        referenced_paths.add(str(src["file"]).strip())
                    if "url" in src:
                        referenced_urls.add(str(src["url"]).strip())
        except Exception:
            continue

    def _raw_source_url(raw_path: Path) -> str:
        """Extract `Source: <url>` from a raw file's header (first 10 lines)."""
        try:
            with raw_path.open("r", encoding="utf-8", errors="ignore") as fh:
                for _ in range(10):
                    line = fh.readline()
                    if not line:
                        break
                    if line.startswith("Source: "):
                        return line[len("Source: "):].strip()
        except Exception:
            pass
        return ""

    # Count raw files NOT referenced (by path OR by Source: URL)
    unreferenced_raw: List[str] = []
    for f in all_raw:
        rel = str(f.relative_to(paths["root"]))
        if rel in referenced_paths:
            continue
        src_url = _raw_source_url(f)
        if src_url and src_url in referenced_urls:
            continue
        unreferenced_raw.append(rel)

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

    def _check_any(candidates: List[str], description: str) -> Dict[str, Any]:
        """Check if ANY of the candidate paths exists (functional equivalence).

        F1 fix: consumers may have the same artifact at a different path.
        schema.yaml == wiki-schema.yaml; wiki/config/ == config/; etc.
        """
        for c in candidates:
            if (root / c).exists():
                return {"path": c, "description": description, "met": True}
        return {"path": candidates[0], "description": description, "met": False}

    # Tier 1 — Agent Foundation
    tier1 = {
        "name": "Agent Foundation",
        "description": "Structured knowledge base with schema + templates + routing",
        "requirements": [
            _check_any(["CLAUDE.md", "AGENTS.md", ".cursorrules"],
                       "Agent brain file (CLAUDE.md, AGENTS.md, or equivalent)"),
            _check_any(["wiki/config/wiki-schema.yaml", "wiki/config/schema.yaml",
                        "config/wiki-schema.yaml", "config/schema.yaml"],
                       "Frontmatter schema (any location)"),
            _check_any(["wiki/config/templates", "config/templates", "templates"],
                       "Page templates directory"),
        ],
    }

    # Tier 2 — Stage-Gate Process
    tier2 = {
        "name": "Stage-Gate Process",
        "description": "Methodology engine + work tracking + stage discipline",
        "requirements": [
            _check_any(["wiki/config/methodology.yaml", "config/methodology.yaml",
                        "methodology.yaml"],
                       "Methodology models with stage chains"),
            _check_any(["wiki/backlog", "backlog", "wiki/backlog/epics"],
                       "Backlog hierarchy (milestones/epics/modules/tasks)"),
            _check_any(["AGENTS.md", "CLAUDE.md"],
                       "Agent context file (universal or tool-specific)"),
        ],
    }

    # Tier 3 — Evolution Pipeline
    # Maturity folders: check under wiki/ OR at root
    maturity_dirs_options = [
        ["wiki/lessons", "lessons", "wiki/domains/learnings"],
        ["wiki/patterns", "patterns"],
        ["wiki/decisions", "decisions"],
    ]
    maturity_met = all(
        any(
            (root / d / "00_inbox").exists() or
            (root / d / "01_drafts").exists() or
            (root / d).exists()  # has the directory at all
            for d in options
        )
        for options in maturity_dirs_options
    )
    tier3 = {
        "name": "Evolution Pipeline",
        "description": "Self-improving wiki with maturity lifecycle + scoring + promotion",
        "requirements": [
            _check_any(["tools/evolve.py", "scripts/evolve.js", "scripts/methodology/evolve.cjs"],
                       "Evolution scoring / promotion tooling"),
            {
                "path": "wiki/{lessons,patterns,decisions}/",
                "description": "Knowledge layers (lessons, patterns, decisions — any structure)",
                "met": maturity_met,
            },
            _check_any(["tools/lint.py", "tools/validate.py", "scripts/methodology/validate-stage.cjs"],
                       "Quality/validation tooling"),
        ],
    }

    # Tier 4 — Hub Integration
    tier4 = {
        "name": "Hub Integration",
        "description": "Ecosystem participation — export, MCP, bidirectional knowledge flow",
        "requirements": [
            _check_any(["wiki/config/export-profiles.yaml", "config/export-profiles.yaml"],
                       "Export transforms for other projects"),
            _check_any(["tools/mcp_server.py", ".mcp.json"],
                       "MCP server or MCP connection (producer or consumer)"),
            _check_any([".mcp.json", "mcp.json"],
                       "MCP configuration file"),
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

    # Orient — context-aware onboarding (E022-M002)
    o = sub.add_parser("orient", help="Context-aware orientation — who are you, where, what to internalize")
    o.add_argument("--orient-as", choices=["second-brain", "sister", "external"],
                   help="Explicit context override (trumps auto-detection)")
    o.add_argument("--fresh", action="store_true",
                   help="Force fresh-agent mode (e.g. after compaction)")
    o.add_argument("--format", dest="orient_format", default="text",
                   choices=["text", "json"], help="Output format (default: text)")

    # Smart auto-routing
    sub.add_parser("what-do-i-need", help="Auto-detect identity and recommend chain, model, first steps")

    # Health score (Q23+Q24)
    h = sub.add_parser("health", help="Composite methodology+quality health score with per-dimension breakdown")
    h.add_argument("--verbose", action="store_true", help="Show which pages have validation errors")

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
    tl = sub.add_parser("timeline", help="Computed cross-project temporal view (commits, lessons, sessions, directives, epics, tasks)")
    tl.add_argument("--scope", default=None,
                    help="Comma-separated: self, brain, all, or project names. Default: self (from brain) / self,brain (from sister)")
    tl.add_argument("--since", default="7d", help="Duration (7d, 24h, 2w) or ISO date. Default: 7d")
    tl.add_argument("--until", default=None, help="Duration or ISO date. Default: now")
    tl.add_argument("--type", dest="tl_types", default=None,
                    help="Comma-separated event types (lesson,pattern,decision,synthesis,epic,task,session,directive,commit)")
    tl.add_argument("--group-by", dest="tl_group_by", default="date", choices=["date", "project", "type", "epic", "none"])
    tl.add_argument("--format", dest="tl_format", default="markdown", choices=["markdown", "json"])
    tl.add_argument("--full-content", dest="tl_full_content", action="store_true",
                    help="Include full event bodies (no caps)")
    tl.add_argument("--remote", dest="tl_remote", action="store_true",
                    help="Fetch non-local projects via gh api (slower — opt-in). "
                         "Without this flag, unavailable projects surface as notices only.")
    tl.add_argument("--collapse-arcs", dest="tl_collapse_arcs", action="store_true",
                    help="Collapse same-file same-day event clusters into one arc-summary line")
    tl.add_argument("--epic", dest="tl_epic", default=None,
                    help="Filter to one epic (e.g. --epic E013). Matches parent_epic OR epic file.")
    tl.add_argument("--path", dest="tl_path", default=None,
                    help="Filter events whose path contains this substring (e.g. --path T120)")

    ct = sub.add_parser("contribute", help="Contribute a lesson/remark/correction back to the second brain. "
                        "Pass your content as plain text — the second brain normalizes it into the right format. "
                        "Contributions land in 00_inbox (lessons) or log/ (remarks/corrections). Promotion requires operator review.")
    ct.add_argument("--type", required=True, choices=["lesson", "remark", "correction"])
    ct.add_argument("--title", required=True)
    ct.add_argument("--content", required=True)
    ct.add_argument("--domain", default="cross-domain")
    ct.add_argument("--contributor", help="Contributor identifier (e.g. 'openarms-harness-v10'). Default: user@host")
    ct.add_argument("--source", help="Origin path of contribution (e.g. '~/openarms'). Default: self")
    ct.add_argument("--reason", help="Why this contribution is being made (optional audit trail)")
    ct.add_argument("--target", choices=["brain", "local"], default="brain",
                    help="Where the contribution lands. 'brain' (default) writes to the "
                         "second brain's intake even when invoked via a consumer-project "
                         "forwarder that auto-adds --wiki-root. 'local' writes to --wiki-root "
                         "(the caller's own wiki) for self-contribution. If no second brain "
                         "is configured, 'brain' falls back to local automatically.")

    args = parser.parse_args()
    paths = resolve_paths(
        wiki_root=args.wiki_root if hasattr(args, "wiki_root") else None,
        brain_root=args.brain if hasattr(args, "brain") else None,
    )

    if args.command == "orient":
        gateway_orient(paths, args)

    elif args.command == "what-do-i-need":
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
        # F2 fix: show which schema is being used for validation
        schema_source = "project" if paths.get("schema") and "wiki-schema" not in str(paths["schema"]) or not paths.get("is_brain") else "second-brain"
        if not paths.get("is_brain"):
            used_schema = paths.get("schema", "unknown")
            print(f"\n  Schema: {used_schema}")
            print(f"  Source: {'project-own' if used_schema and paths['root'] in used_schema.parents else 'second-brain (fallback)'}\n")
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

        # Verbose: show page-level validation errors
        if getattr(args, "verbose", False):
            from tools.validate import validate_page
            from tools.common import find_wiki_pages
            wiki_dir = paths["wiki"]
            schema_path = paths["schema"]
            errors_shown = 0
            print("\n--- Validation Errors (--verbose) ---\n")
            for page in sorted(find_wiki_pages(wiki_dir)):
                vr = validate_page(page, schema_path)
                if vr["errors"]:
                    rel = page.relative_to(wiki_dir) if wiki_dir in page.parents else page
                    for err in vr["errors"]:
                        print(f"  {rel}: {err['message']}")
                        errors_shown += 1
                    if errors_shown >= 50:
                        print(f"\n  ... (showing first 50 of {result['dimensions'].get('validation', {}).get('detail', '?')})")
                        break
            if errors_shown == 0:
                print("  No validation errors found.")

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
            target=getattr(args, "target", "brain"),
        )
        print(json.dumps(result, indent=2, default=str))

    elif args.command == "timeline":
        from tools.timeline import compute_timeline
        scope_list = None
        if args.scope:
            scope_list = [s.strip() for s in args.scope.split(",") if s.strip()]
        types_list = None
        if args.tl_types:
            types_list = [t.strip() for t in args.tl_types.split(",") if t.strip()]
        output = compute_timeline(
            scope=scope_list,
            since=args.since,
            until=args.until,
            types=types_list,
            wiki_root=paths.get("root"),
            brain_root=paths.get("brain_root"),
            full_content=args.tl_full_content,
            group_by=args.tl_group_by,
            output_format=args.tl_format,
            remote=args.tl_remote,
            collapse_arcs=args.tl_collapse_arcs,
            epic=args.tl_epic,
            path_filter=args.tl_path,
        )
        print(output)

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
            # F4 fix: split display into project-level (stable) vs consumer-level (dynamic)
            stable_keys = {"type", "domain", "second brain", "second-brain"}
            dynamic_keys = {"execution mode", "sdlc profile", "sdlc chain",
                           "pm level", "trust tier", "phase", "scale"}
            print("PROJECT IDENTITY (stable — declared in CLAUDE.md):")
            for k, v in id_data.items():
                if k.lower() in stable_keys:
                    print(f"  {k}: {v}")
            print()
            print("PROJECT STATE (declared, reviewed periodically):")
            for k, v in id_data.items():
                if k.lower() in dynamic_keys:
                    print(f"  {k}: {v}")
            print()
            print("CONSUMER PROPERTIES (per-session, NOT in CLAUDE.md):")
            print("  execution mode: declared by consumer at connect time via MCP_CLIENT_RUNTIME")
            print("  methodology model: per task, not per project")
            print("  SDLC profile: per task, overridable — default from phase/scale")
        else:
            print("PROJECT IDENTITY: not fully configured.")
            print("  Stable fields to add to CLAUDE.md: type, domain, second-brain relationship")
            print("  Do NOT hardcode: execution mode, SDLC profile, methodology model")
            print("  (these are consumer/task properties — see gateway orient for details)")
            print("  Reference: wiki/domains/cross-domain/project-self-identification-protocol.md")
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
