---
title: "Infrastructure Must Be Reproducible, Not Manual"
aliases:
  - "Infrastructure Must Be Reproducible, Not Manual"
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
updated: 2026-04-10
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

> [!bug]- The failure: writing a service file directly to the filesystem
> The agent created a systemd service by `cat > ~/.config/systemd/user/wiki-sync.service`. This is the infrastructure equivalent of hardcoding a value instead of using a config file. The service file works — systemd finds it, loads it, runs it. But it is undocumented debt.

> [!warning] Five ways manual infrastructure fails
>
> | Problem | Why It Matters |
> |---------|---------------|
> | Invisible to repo | `git status` shows nothing — no one knows it exists |
> | Not reproducible | Machine rebuilt → service gone, no command to recreate |
> | Not self-documenting | Can't read `setup.py` to discover available services |
> | Not versioned | No diff, no history, no review for config changes |
> | Fragile | Path changes require remembering the service file exists |

The repository already had `tools/setup.py --services` — generates service files from templates, auto-detects paths, installs + enables. Extending this mechanism is the correct path. Writing directly bypasses all of that.

> [!tip] The principle: source of truth is the code, not the running system
> If the code does not describe the infrastructure, the infrastructure is undocumented debt. This is IaC applied at every scale — from production Terraform to local systemd services.

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

> [!warning] Self-Check — Am I About to Make This Mistake?
>
> 1. Am I applying this lesson to my current context?
> 2. Do I have evidence that this applies HERE, or am I assuming?
> 3. What would change if this lesson didn't apply to my situation?
> 4. Have I checked the boundaries — where does this lesson NOT apply?

### How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What principle governs this?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **How does enforcement apply?** | [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions for Process Enforcement]] |
> | **How does structure help?** | [[structured-context-governs-agent-behavior-more-than-content|Principle — Structured Context Governs Agent Behavior More Than Content]] |
> | **What is my identity profile?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **Where does this fit in the system?** | [[methodology-system-map|Methodology System Map]] — find any component |

## Relationships

- DERIVED FROM: [[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]
- DERIVED FROM: [[stage-gate-methodology|Stage-Gate Methodology]] (the setup tooling IS a stage gate for infrastructure)
- RELATES TO: [[always-plan-before-executing|Always Plan Before Executing]] (plan the infrastructure approach before writing files)
- RELATES TO: [[methodology-framework|Methodology Framework]]
- BUILDS ON: [[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]] (the pipeline itself is reproducible tooling)
- ENABLES: [[immune-system-rules|Immune System Rules]] (this lesson became a rule)

## Backlinks

[[infrastructure-as-code-patterns|Infrastructure as Code Patterns]]
[[stage-gate-methodology|Stage-Gate Methodology]]
[[always-plan-before-executing|Always Plan Before Executing]]
[[methodology-framework|Methodology Framework]]
[[wiki-ingestion-pipeline|Wiki Ingestion Pipeline]]
[[immune-system-rules|Immune System Rules]]
[[model-quality-failure-prevention|Model — Quality and Failure Prevention]]
