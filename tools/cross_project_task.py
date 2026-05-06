#!/usr/bin/env python3
"""tools.cross_project_task — operator-granted cross-project task channel.

Per operator directive 2026-05-05: "you will create yourself a tool to add
a task into the other project... it needs a note too but its a note + a
task what I asked.. and then you can have an optional parameter to add
only one or the other and possibly even affect other files."

This tool writes a TASK page to the target project's backlog/tasks/
directory following the target's task convention (T<NUM>-<slug>.md
filename, frontmatter with status/priority/parent_module/etc., body
sections: Description, Done When, Dependencies, Relationships).

Companion: tools/cross_project_note.py writes NOTES to wiki/log/.
The two are designed to be used together for a handoff: the note is
the narrative/context; the task is the actionable item that gets
tracked in backlog state.

Usage:
    python -m tools.cross_project_task <target> --slug <slug> --title <title>
        [--task-id T066]              # auto-allocated next-number if omitted
        [--priority P0|P1|P2]         # default P2
        [--status not-started|in-progress|done|blocked|...]  # default not-started
        [--parent-module <module-id>] # if scoped to an existing module
        [--parent-epic <epic-id>]
        [--current-stage document|design|scaffold|implement|test]  # default document
        [--readiness 0-100]           # default 0
        [--sfif-stage Scaffold|Foundation|Infrastructure|Features]  # if applicable
        [--content-file <path>]       # OR pass content on stdin
        [--update-task-index]         # also append a row to tasks/_index.md
        [--force]                     # overwrite if file exists
        [--dry-run]                   # print, don't write

Examples:
    # Standard task add:
    python -m tools.cross_project_task root-ghostproxy \\
        --slug pre-publish-readiness \\
        --title "Pre-publish readiness review" \\
        --priority P1 \\
        --content-file /tmp/task-body.md

    # Auto-allocates next task ID; from stdin:
    echo "Body" | python -m tools.cross_project_task root-ghostproxy \\
        --slug minor-task --title "Minor task"

Boundary: this tool ONLY writes to <target>/wiki/backlog/tasks/<TaskID>-<slug>.md
plus optionally to <target>/wiki/backlog/tasks/_index.md (when --update-task-index).
It does NOT modify any other path in the target.
"""

import argparse
import sys
from pathlib import Path

from tools._cross_project_common import (
    find_task_dir,
    next_task_number,
    read_content,
    resolve_target,
    slug_clean,
    today_iso,
)


def render_task(args, content_body: str) -> str:
    """Render the markdown task page with frontmatter."""
    today = today_iso()
    title = args.title.replace('"', '\\"')

    fm_lines = [
        "---",
        f'title: "{args.task_id} — {title}"',
        "type: task",
        f"status: {args.status}",
        f"priority: {args.priority}",
    ]
    if args.parent_module:
        fm_lines.append(f'parent_module: "{args.parent_module}"')
    if args.parent_epic:
        fm_lines.append(f'parent_epic: "{args.parent_epic}"')
    fm_lines.append(f"current_stage: {args.current_stage}")
    fm_lines.append(f"readiness: {args.readiness}")
    if args.sfif_stage:
        fm_lines.append(f"sfif_stage: {args.sfif_stage}")
    fm_lines.append("from: second-brain")
    fm_lines.append(f"for: {args.target}")
    fm_lines.append(f"created: {today}")
    fm_lines.append(f"updated: {today}")

    tags = [
        "task", args.priority.lower(), args.task_id.lower(),
        "from-second-brain", "cross-project", args.current_stage,
    ]
    if args.parent_module:
        tags.append(args.parent_module.lower())
    fm_lines.append(f"tags: [{', '.join(tags)}]")
    fm_lines.append("---")

    frontmatter = "\n".join(fm_lines) + "\n\n"

    header = f"# {args.task_id} — {args.title}\n\n"

    metadata = (
        "## Cross-project metadata\n\n"
        f"- **From**: /opt second-brain (devops-solutions-information-hub)\n"
        f"- **For**: {args.target}\n"
        f"- **Channel**: tools.cross_project_task (operator-granted, 2026-05-05)\n"
        f"- **Companion note** (if exists): see most-recent `wiki/log/<date>-from-second-brain-*.md`\n\n"
    )

    body = content_body.strip() + "\n"

    return frontmatter + header + metadata + body


def append_to_task_index(index_file: Path, task_id: str, title: str, target_name: str):
    """Append a row to the tasks/_index.md under a 'Cross-project' section."""
    if not index_file.exists():
        print(f"  ! tasks/_index.md not found at {index_file} — skipping --update-task-index")
        return False

    content = index_file.read_text()
    cross_project_marker = "## Cross-project tasks"

    new_row = f"| {task_id} | {title} | from /opt second-brain | {today_iso()} |"

    if cross_project_marker not in content:
        # Append a new section at the end
        section = (
            f"\n\n{cross_project_marker}\n\n"
            "Tasks added by sister projects via the cross-project channel "
            "(operator-granted). Triage these as you would any other task; "
            "move into module-scoped sections once accepted.\n\n"
            "| Task | Title | Source | Added |\n"
            "|---|---|---|---|\n"
            f"{new_row}\n"
        )
        index_file.write_text(content.rstrip() + section)
        print(f"  ✓ added '{cross_project_marker}' section to {index_file.name}")
    else:
        # Append row to existing section's table
        # Find the section, find its table, append the row
        idx = content.find(cross_project_marker)
        # Find the next |---|---|---| separator after the marker
        rest = content[idx:]
        sep_match = rest.find("|---")
        if sep_match == -1:
            print(f"  ! could not locate table separator in {cross_project_marker} section — skipping")
            return False
        # Find end of separator line
        sep_end = rest.find("\n", sep_match)
        # Insert new row after separator + any existing rows but before next blank line
        rest_after_sep = rest[sep_end + 1:]
        next_blank = rest_after_sep.find("\n\n")
        if next_blank == -1:
            insertion_point = idx + len(rest)
        else:
            insertion_point = idx + sep_end + 1 + next_blank
        new_content = content[:insertion_point] + f"\n{new_row}" + content[insertion_point:]
        index_file.write_text(new_content)
        print(f"  ✓ appended row to '{cross_project_marker}' section in {index_file.name}")

    return True


def main():
    p = argparse.ArgumentParser(
        prog="tools.cross_project_task",
        description="Operator-granted cross-project task channel. Writes to "
        "<target>/wiki/backlog/tasks/<TaskID>-<slug>.md.",
    )
    p.add_argument("target", help="sister-project name (e.g., 'root-ghostproxy') or alias")
    p.add_argument("--slug", required=True, help="filename slug (alnum + hyphens)")
    p.add_argument("--title", required=True, help="task title")
    p.add_argument("--task-id", help="task ID (e.g., T066); auto-allocated if omitted")
    p.add_argument("--priority", default="P2", choices=["P0", "P1", "P2"])
    p.add_argument(
        "--status",
        default="not-started",
        choices=["not-started", "in-progress", "done", "blocked", "deferred", "review"],
    )
    p.add_argument("--parent-module", help="parent module ID (if scoped)")
    p.add_argument("--parent-epic", help="parent epic ID (if scoped)")
    p.add_argument(
        "--current-stage",
        default="document",
        choices=["document", "design", "scaffold", "implement", "test"],
    )
    p.add_argument("--readiness", type=int, default=0)
    p.add_argument(
        "--sfif-stage",
        choices=["Scaffold", "Foundation", "Infrastructure", "Features", "Test"],
    )
    p.add_argument("--content-file", type=Path)
    p.add_argument(
        "--update-task-index",
        action="store_true",
        help="also append a row to <target>/wiki/backlog/tasks/_index.md",
    )
    p.add_argument("--force", action="store_true", help="overwrite if file exists")
    p.add_argument("--dry-run", action="store_true")

    args = p.parse_args()

    target_path, target_name, target_entry = resolve_target(args.target)
    args.target = target_name

    tasks_dir = find_task_dir(target_path, target_entry)

    # Resolve task ID
    if not args.task_id:
        n = next_task_number(tasks_dir)
        args.task_id = f"T{n:03d}"
        print(f"  i auto-allocated task ID: {args.task_id}")

    # Validate task-id format
    if not args.task_id.startswith("T") or not args.task_id[1:].isdigit():
        sys.exit(f"--task-id must match pattern T<NNN>: got '{args.task_id}'")

    slug = slug_clean(args.slug)
    filename = f"{args.task_id}-{slug}.md"
    output_path = tasks_dir / filename

    if output_path.exists() and not args.force:
        sys.exit(
            f"file already exists: {output_path}\n"
            f"use --force to overwrite, or pick a different --slug / --task-id"
        )

    content_body = read_content(args.content_file)
    if not content_body.strip():
        sys.exit("content body is empty")

    rendered = render_task(args, content_body)

    if args.dry_run:
        print(f"[DRY-RUN] would write to: {output_path}")
        print("---rendered task---")
        print(rendered)
        if args.update_task_index:
            print(f"[DRY-RUN] would also append to: {tasks_dir / '_index.md'}")
        return

    output_path.write_text(rendered)
    print(f"✓ task written: {output_path}")
    print(f"  ID: {args.task_id} | priority: {args.priority} | status: {args.status}")
    print(f"  pickup: {target_name}'s backlog grooming reads tasks/ on demand; "
          f"task will appear in next /progress / /backlog query")

    if args.update_task_index:
        index_file = tasks_dir / "_index.md"
        append_to_task_index(index_file, args.task_id, args.title, target_name)


if __name__ == "__main__":
    main()
