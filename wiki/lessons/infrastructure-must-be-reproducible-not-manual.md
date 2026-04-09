---
title: "Infrastructure Must Be Reproducible, Not Manual"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: authoritative
maturity: growing
derived_from:
  - "Infrastructure as Code Patterns"
  - "Stage-Gate Methodology"
created: 2026-04-09
updated: 2026-04-09
sources:
  - id: directive-no-new-sources
    type: log
    file: raw/notes/2026-04-08-user-directive-no-new-sources-unless-relevant.md
    title: "User Directive — No New Sources Unless Relevant"
    ingested: 2026-04-08
tags: [failure-lesson, methodology, quality, infrastructure-as-code, reproducibility, systemd, setup-tooling, invisible-infrastructure]
---

# Infrastructure Must Be Reproducible, Not Manual

## Summary

The AI agent attempted to create a systemd service file by directly writing it with `cat >` instead of building the service deployment into the existing `setup.py --services` command. This would have created invisible, non-reproducible infrastructure — a service file that exists on one machine, is not tracked in version control, cannot be deployed on a fresh clone, and whose existence is known only to whoever happened to be watching the terminal at that moment. The user's rule is absolute: every infrastructure operation must go through reproducible tooling. If it cannot be reproduced by running a command from the repository, it is a bug, not a feature.

## Context

This lesson applies whenever an agent (or a human) is about to create infrastructure — services, cron jobs, config files in system directories, DNS records, firewall rules, user accounts, mount points, or any other system-level artifact. The triggering question is: "If I clone this repository on a fresh machine and run the setup, will this infrastructure exist?" If the answer is no, the approach is wrong.

This is especially relevant in projects that have existing infrastructure tooling. The research wiki already had `python -m tools.setup --services` as the mechanism for deploying services. The correct path was to extend that mechanism, not bypass it.

## Insight

The agent was tasked with setting up a sync daemon (WSL to Windows file synchronization for Obsidian). The technically correct action was to create a systemd user service that runs the sync watcher. The agent began doing this by writing the service file directly to `~/.config/systemd/user/` using a shell command.

This is the infrastructure equivalent of hardcoding a value instead of putting it in a config file. The service file works — systemd will find it, load it, run it. But:

1. **It is invisible to the repository.** `git status` shows nothing. A new contributor cloning the repo has no idea this service exists.
2. **It is not reproducible.** If the machine is rebuilt, the service is gone. There is no command to recreate it.
3. **It is not documented by its existence.** Code in a repository is self-documenting: you can read `setup.py` and see what services are available. A file written directly to a system directory documents nothing.
4. **It cannot be versioned.** If the service configuration needs to change, there is no diff, no history, no review.
5. **It is fragile.** If the paths change, the Python virtual environment moves, or the sync target changes, someone must remember that this service file exists and update it manually.

The repository already had the correct mechanism: `tools/setup.py` with a `--services` flag that generates service files from templates, installs them, enables them, and can redeploy them on any machine. Extending this mechanism adds the sync daemon to the reproducible infrastructure. Writing the file directly bypasses all of that.

The general principle is the same as Infrastructure as Code in production systems: the source of truth for infrastructure is the code, not the running system. If the code does not describe the infrastructure, the infrastructure is undocumented debt.

## Evidence

**Date:** 2026-04-08 to 2026-04-09

**The incident:** While setting up the wiki-sync daemon (WSL to Windows file synchronization), the agent began creating a systemd service file by writing it directly to the filesystem with a shell command (`cat > ~/.config/systemd/user/wiki-sync.service`).

**The problem identified:** This approach creates infrastructure that:
- Is not tracked in the repository
- Cannot be reproduced on a fresh clone
- Has no version history
- Is invisible to other contributors or future sessions

**The correct approach (implemented after correction):** The service deployment was built into `python -m tools.setup --services wiki-sync`, which:
- Generates the service file from a template in the repository
- Auto-detects the correct paths (venv, wiki directory, sync target)
- Installs, enables, and starts the service
- Can be re-run on any machine to reproduce the exact same setup
- Is documented by its existence in `tools/setup.py`

**The user's broader directive:** "no need for new source until we see enough relevance" — work with what exists, extend existing tooling, do not create ad-hoc artifacts outside the system.

**Source file:** `raw/notes/2026-04-08-user-directive-no-new-sources-unless-relevant.md`

## Applicability

This lesson applies universally across infrastructure work:

- **Service deployment**: Never `cat >` a service file. Build it into the project's setup/deploy tooling.
- **Cron jobs**: Never `crontab -e` manually. Use a configuration-as-code approach (setup script, Ansible, Terraform, or at minimum a documented shell script in the repo).
- **Environment configuration**: Never set environment variables in `.bashrc` manually for a project. Use `.env` files, direnv, or the project's config management.
- **Database migrations**: Never run SQL directly against production. Use migration tooling that tracks state.
- **Cloud resources**: Never click-create resources in a console. Use Terraform, Pulumi, CloudFormation, or at minimum a documented CLI script.
- **Agent behavior**: This applies to AI agents performing infrastructure tasks. An agent that creates infrastructure outside the project's tooling is creating technical debt, even if the infrastructure works correctly.

**The litmus test**: After every infrastructure operation, ask: "Can a fresh clone reproduce this by running a command?" If no, refactor the operation into reproducible tooling before considering it done.

## Relationships

- DERIVED FROM: Infrastructure as Code Patterns
- DERIVED FROM: Stage-Gate Methodology (the setup tooling IS a stage gate for infrastructure)
- RELATES TO: Always Plan Before Executing (plan the infrastructure approach before writing files)
- RELATES TO: Methodology Framework
- BUILDS ON: Wiki Ingestion Pipeline (the pipeline itself is reproducible tooling)
- ENABLES: Immune System Rules (this lesson became a rule)

## Backlinks

[[Infrastructure as Code Patterns]]
[[Stage-Gate Methodology (the setup tooling IS a stage gate for infrastructure)]]
[[Always Plan Before Executing (plan the infrastructure approach before writing files)]]
[[Methodology Framework]]
[[Wiki Ingestion Pipeline (the pipeline itself is reproducible tooling)]]
[[Immune System Rules (this lesson became a rule)]]
