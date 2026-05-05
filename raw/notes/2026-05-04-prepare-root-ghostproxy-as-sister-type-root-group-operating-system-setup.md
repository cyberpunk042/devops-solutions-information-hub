---
title: "2026-05-04 — Operator directive: prepare root-ghostproxy as sister project of type=root, group=operating-system-setup; SFIF base + second-brain integration"
type: note
domain: log
note_type: directive
status: raw
confidence: high
created: 2026-05-04
updated: 2026-05-04
sources:
  - id: operator-2026-05-04-root-ghostproxy-prep
    type: directive
    project: research-wiki
    path: session
tags: [operator-directive, verbatim, sacrosanct, root-ghostproxy, sister-project, type-root, group-operating-system-setup, sfif, identity-profile, taxonomy-extension]
---

# Operator directive 2026-05-04 — prepare root-ghostproxy: type=root, group=operating-system-setup, sister + SFIF base

## Verbatim (sacrosanct, do not paraphrase)

> *"okay now we need to prepare to work on the new root project and make sure we can install to it as a sister project and as a project of type root and group operating-system-setup. WHy root ? since it could have been jfortin install too.. since its an operating system IaC project, even in a user such as jfortin it would remain a root-type project. but the project is barely started... we will need to build everything inside of it so that a future session in its context can work properly. not only the full second-brain integration but just pure sfif project base. Remember SFIF and what it is part of ?"*

## Decomposition (operator's words → concrete acts)

| Operator's framing | Concrete act |
|---|---|
| *"prepare to work on the new root project"* | THIS session is preparation. The future session works inside `/root` (or wherever root-ghostproxy is installed). Per prior directive: `/root` is off-limits THIS session. |
| *"make sure we can install to it as a sister project"* | The `tools/setup.py --connect-project` flow must accept root-ghostproxy as a target. Adds gateway/view forwarders + AGENTS.md "Second Brain Connection" block + research-wiki MCP entry into root-ghostproxy. |
| *"as a project of type root and group operating-system-setup"* | Two taxonomy extensions: (a) **type = root** is a NEW value of the existing Type dimension; (b) **group = operating-system-setup** is a NEW dimension entirely (didn't exist in Goldilocks identity protocol). |
| *"WHy root ? since it could have been jfortin install too.. since its an operating system IaC project, even in a user such as jfortin it would remain a root-type project"* | "Type=root" is **scope**, not **path**. A root-type project SETS UP an operating system / system-level config. It remains root-type whether the install user is `root` or any unprivileged user (`jfortin`, `ubuntu`, etc.). The TYPE describes what the project does to the OS, not where the .git lives. |
| *"the project is barely started"* | root-ghostproxy at SFIF: Scaffold + partial Foundation. Has install.sh, README, .claude/settings.json + 5 hooks, .config/opencode/ bridge plugin, .gitignore, integrity.py. Missing: wiki/, methodology, agent harness layer, operator manual, infra-stage tooling, features beyond AI-safety hooks. |
| *"we will need to build everything inside of it so that a future session in its context can work properly"* | The future session (not THIS one) opens Claude Code in the root-ghostproxy repo. For that session to be productive, the project must have its own CLAUDE.md, AGENTS.md, methodology, schema, hooks, + the second-brain connection + SFIF Foundation/Infrastructure populated. |
| *"not only the full second-brain integration but just pure sfif project base"* | Two work streams in the future session: (a) **Second-brain integration** (sister hookup) and (b) **Pure SFIF project base** (Scaffold → Foundation → Infrastructure → Features for the project itself, separate from / in addition to the brain hookup). |
| *"Remember SFIF and what it is part of ?"* | YES — SFIF is part of: (a) the **Quality** category of the 16 named models (`wiki/spine/models/quality/model-sfif-architecture.md`); (b) the **Methodology super-model** as the **`project-lifecycle`** model in `wiki/config/methodology.yaml` with `composition: nested` (other models nest inside its stages); (c) the **3 quality tiers** (Skyscraper / Pyramid / Mountain) it maps to; (d) **recursive** — applies at project / feature / component / design-system levels. |

## Two new taxonomy elements

### Type = `root` (new value of existing Type dimension)

- **Definition.** Project of type `root` SETS UP operating-system or system-level configuration via Infrastructure-as-Code. The project's scope is the host OS / harness / shell environment, not application code.
- **Scope-not-path.** Type is independent of install user. Same project running under `root` user (homedir `/root`) or `jfortin` user (homedir `/home/jfortin`) is still type=root because what it CONFIGURES is the OS, regardless of which user account runs it.
- **Examples in the operator's vocabulary so far:** root-ghostproxy (claude-code + opencode security hardening + IPS modules suricata/polarproxy). Future siblings of the same type could include: container-runtime-setup, network-edge-setup, etc.

### Group = `operating-system-setup` (new dimension)

- **Definition.** A `group` clusters projects of the same purpose-class. Operating-system-setup group = projects whose purpose is to configure / harden / set up an operating system or its surrounding system layers (firewall, IPS, daemon scheduling, etc.).
- **Distinct from `domain`.** Domain is technology axis (TypeScript, Python, Infrastructure, Knowledge). Group is purpose-class axis (operating-system-setup, ai-agent-platform, agent-orchestration, knowledge-curation, etc.). A project has one domain AND one group; they answer different questions.

## Path semantics for root-type projects

Per `/root/README.md` (root-ghostproxy itself): *"This repo is structured to be `git init`'d at `$HOME` itself."* The repo root IS the home directory.

| Install user | Homedir | Repo path |
|---|---|---|
| `root` | `/root` | `/root` (this machine — ghostproxy) |
| `jfortin` | `/home/jfortin` | `/home/jfortin` (`.git` at `/home/jfortin/.git`) |
| any user | `~` | `~` (the homedir itself is the repo root) |

For `sister-projects.yaml`: `path: ~/` is the canonical form (Path.expanduser resolves at runtime per user). Root-type projects sit at `$HOME` directly, not at `$HOME/<projectname>`.

## Two work streams for the future session (not this one)

### Stream 1 — Second-brain integration (sister hookup)

Outcome: `tools/setup.py --connect-project /root` (or wherever) succeeds and:

- writes a `research-wiki` MCP entry into root-ghostproxy's `.mcp.json`
- creates `tools/gateway.py` and `tools/view.py` forwarders inside root-ghostproxy
- adds the `## Second Brain Connection` block to root-ghostproxy's AGENTS.md (which itself has to exist first — Stream 2 dependency)

### Stream 2 — Pure SFIF project base

Outcome: root-ghostproxy reaches SFIF Foundation cleanly and starts on Infrastructure. Per [model-sfif-architecture](wiki/spine/models/quality/model-sfif-architecture.md):

- **Scaffold** (mostly there) — confirm direction, document tech stack, AI-config files (CLAUDE.md / AGENTS.md authoring required)
- **Foundation** (mostly there) — single entry point: `install.sh` works. Project is operable. Need to ensure the entry-point is documented + reproducible.
- **Infrastructure** (NOT there) — tooling, automation, deployment pipeline. Currently install.sh is the only tool. Needs: methodology-aware harness, validation pipeline, agent harness layer.
- **Features** (NOT there) — the actual specialized OS-setup features beyond AI-safety hooks. Operator named: suricata module, polarproxy module, etc.

## What this directive implies for THIS preparation session (wiki-side only)

- [ ] Extend `wiki/config/sister-projects.yaml`: add `type` and `group` fields to schema; add `root-ghostproxy` entry
- [ ] Create `wiki/ecosystem/project_profiles/root-ghostproxy/identity-profile.md` (Goldilocks profile for root-ghostproxy)
- [ ] Extend `wiki/domains/cross-domain/methodology-framework/project-self-identification-protocol.md` with the Group dimension + root Type value
- [ ] Create epic for the future-session work: `wiki/backlog/epics/pre-milestone/root-ghostproxy-sfif-rollout-and-second-brain-integration-2026-05.md`
- [ ] (Optional) concept page for type=root and group=operating-system-setup

NOT touching `/root` this session per standing operator directive.

## Standing operator state confirmed by this turn

- `/root` (root-ghostproxy) remains off-limits this session per *"YOU WILL NEED TO ACTUALLY LOOK AT THE /root at SOME POINT BUT WE ARE JUST NOT THERE YET"*.
- Operator-defined position: preparation only. Building inside the root project is a future session's work.
- SFIF as the build-lifecycle framework for root-ghostproxy is operator-confirmed (the rhetorical "Remember SFIF and what it is part of?" is a check, not an open question).
