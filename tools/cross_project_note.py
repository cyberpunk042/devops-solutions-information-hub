#!/usr/bin/env python3
"""tools.cross_project_note — operator-granted cross-project note channel.

Per operator directive 2026-05-05: "you will create yourself a tool to add a
task into the other project with a notes that he will pick up somewhere,
inside the context file amongst other things I guess. smart ways."

This tool is the SPECIFIC EXCEPTION to the sister-projects.yaml read-only
policy. The general gateway tools (tools/sister_project.py) remain read-only;
THIS tool writes to ONE designated path on the target sister project:

    <target-project-path>/wiki/log/<date>-from-second-brain-<slug>.md

Why wiki/log/: that's the project's verbatim/iteration log layer (per
/root's CLAUDE.md self-reference rule + /opt's sister-projects.yaml
schema). Each sister project's `/orient` (or equivalent intel-gathering
chain) reads recent wiki/log/ entries — so a note dropped here is
auto-picked-up on next session, no brain-file edit needed.

Filename prefix `from-second-brain-` makes intent clear; also lets the
target agent grep / filter cross-project notes from local iteration work.

Usage:
    python -m tools.cross_project_note <target> --slug <slug> --title <title>
        [--type note|task|handoff|directive]
        [--content-file <path>]    # OR pass content on stdin
        [--for-action <text>]      # what should target agent do
        [--force]                  # overwrite if file exists

Examples:
    # From content file:
    python -m tools.cross_project_note root-modules \\
        --slug pre-publish-handoff \\
        --title "Pre-publish requirements + post-publish checkout scripts" \\
        --type handoff \\
        --content-file /tmp/handoff-body.md

    # From stdin:
    echo "## Body" | python -m tools.cross_project_note root-modules \\
        --slug minor-update --title "Minor update" --type note

Boundary: this tool ONLY writes to <target>/wiki/log/. It does NOT modify
any other path in the target. Operator-grant for this channel is logged
in raw/notes/2026-05-05-cross-project-note-tool-grant.md.
"""

import argparse
import sys
from pathlib import Path

from tools._cross_project_common import (
    find_log_dir,
    read_content,
    resolve_target,
    slug_clean,
    today_iso,
)


def render_note(args, content_body: str) -> str:
    """Render the markdown note with frontmatter."""
    today = today_iso()
    title = args.title.replace('"', '\\"')

    frontmatter = (
        "---\n"
        f'title: "{title}"\n'
        f"type: {args.type}\n"
        "from: second-brain\n"
        f"for: {args.target}\n"
        f"created: {today}\n"
        f"updated: {today}\n"
        "status: active\n"
        f'tags: [from-second-brain, cross-project, {args.type}, '
        f"{slug_clean(args.target)}]\n"
        "---\n\n"
    )

    header = f"# {args.title}\n\n"

    metadata = (
        "## Metadata\n\n"
        f"- **From**: /opt second-brain (devops-solutions-information-hub)\n"
        f"- **For**: {args.target}\n"
        f"- **Type**: {args.type}\n"
        f"- **Date**: {today}\n"
    )
    if args.for_action:
        metadata += f"- **For-action**: {args.for_action}\n"
    metadata += "\n"

    body = "## Content\n\n" + content_body.strip() + "\n\n"

    pickup = (
        "## Pickup mechanism\n\n"
        f"This file lives at `{args.target}/wiki/log/<date>-from-second-brain-<slug>.md` "
        "in the target project's iteration log layer. Target's `/orient` "
        "command (or equivalent intel-gathering chain) reads recent `wiki/log/` "
        "entries on session start; this note will be among them.\n\n"
        "**Channel discipline**: cross-project notes via this channel are "
        "advisory — target agent reads, decides, acts within target's own scope. "
        "/opt agent does not write outside this designated channel.\n"
    )

    return frontmatter + header + metadata + body + pickup


def main():
    p = argparse.ArgumentParser(
        prog="tools.cross_project_note",
        description="Operator-granted cross-project note channel. Writes to "
        "<target>/wiki/log/<date>-from-second-brain-<slug>.md.",
    )
    p.add_argument("target", help="sister-project name (e.g., 'root-modules') or alias")
    p.add_argument("--slug", required=True, help="filename slug (alnum + hyphens)")
    p.add_argument("--title", required=True, help="note title")
    p.add_argument(
        "--type",
        default="note",
        choices=["note", "task", "handoff", "directive", "finding"],
        help="note type (default: note)",
    )
    p.add_argument("--content-file", type=Path, help="markdown content file (else stdin)")
    p.add_argument("--for-action", help="brief hint of what target agent should do")
    p.add_argument("--force", action="store_true", help="overwrite if file exists")
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="print what would be written; don't write",
    )

    args = p.parse_args()

    target_path, target_name, target_entry = resolve_target(args.target)
    args.target = target_name

    log_dir = find_log_dir(target_path, target_entry)

    content_body = read_content(args.content_file)
    if not content_body.strip():
        sys.exit("content body is empty")

    today = today_iso()
    slug = slug_clean(args.slug)
    filename = f"{today}-from-second-brain-{slug}.md"
    output_path = log_dir / filename

    # Idempotency check
    if output_path.exists() and not args.force:
        sys.exit(
            f"file already exists: {output_path}\n"
            f"use --force to overwrite, or pick a different --slug"
        )

    # Render + write
    rendered = render_note(args, content_body)

    if args.dry_run:
        print(f"[DRY-RUN] would write to: {output_path}")
        print("---rendered note---")
        print(rendered)
        return

    output_path.write_text(rendered)
    print(f"✓ written: {output_path} ({len(rendered)} chars)")
    print(f"  pickup: {target_name}'s /orient (or equivalent) reads recent wiki/log/")


if __name__ == "__main__":
    main()
