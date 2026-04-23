---
title: "Machine-Specific Config in Version Control Is Aspirational Portability"
aliases:
  - "Machine-Specific Config in Version Control Is Aspirational Portability"
  - "Committed Absolute Paths Break Portability"
type: lesson
domain: cross-domain
layer: 4
status: synthesized
confidence: medium
maturity: growing
derived_from:
  - "Aspirational Declaration Produces False Confidence at Every Layer"
  - "Infrastructure Must Be Reproducible, Not Manual"
  - "Infrastructure Over Instructions for Process Enforcement"
created: 2026-04-16
updated: 2026-04-22
sources:
  - id: research-wiki-mcp-json
    type: file
    file: .mcp.json.template
    description: "The research wiki's own .mcp.json was committed with /home/jfortin/... absolute paths. Operator noticed the portability gap when preparing to transfer the repo to another machine. The portability claim (README: 'clone on any machine') was aspirational until .mcp.json was gitignored + regenerated per-machine via setup --init."
  - id: setup-init-fix
    type: file
    file: tools/setup.py
    description: "The fix: setup.py --init generates .mcp.json at clone time with machine-specific absolute paths. Template committed as reference. .mcp.json gitignored."
  - id: directive-log
    type: file
    file: raw/notes/2026-04-16-directive-portability-absolute-paths.md
tags: [lesson, portability, machine-specific, config, absolute-paths, mcp, aspirational, contributed, self]
---

# Machine-Specific Config in Version Control Is Aspirational Portability

## Summary

Committing configuration files that contain machine-specific absolute paths silently breaks portability. The project claims to be portable (README: "clone the repo on any machine") — but MCP clients, venv paths, or hardcoded home directories make the claim aspirational. First attempt to transfer the repo reveals the gap: paths that worked on the original machine are meaningless on the new one. This is a 4th-layer instance of [[aspirational-declaration-without-enforcement|Aspirational Declaration Produces False Confidence at Every Layer]] — the layer being "version-controlled config" where the declaration is "this config is shared across machines" but the content is machine-specific. The fix is architectural: gitignore the machine-specific file, commit a template, and generate per-machine at setup time.

## Context

> [!warning] When does this lesson apply?
>
> - You commit a config file that references absolute paths
> - Your project README claims cross-machine portability
> - You observe a file that "works" on your machine but doesn't when cloned elsewhere
> - You use MCP (or any protocol requiring absolute paths in config)
> - You have `.venv/bin/python` or similar paths baked into config
> - A consumer integrates with your project on a different machine and reports the tool fails to start

## Insight

> [!tip] The insight
>
> **Version control is for content that is the SAME across all clones. Machine-specific paths are NOT the same across machines.** Committing them creates a per-clone defect: the file works for whoever wrote it, breaks for everyone else. The portability claim in the README becomes aspirational — declared without infrastructure enforcing it. The fix is structural, not educational: gitignore the file, commit a template, generate the real file at setup time. This isn't an instruction consumers must remember — it's infrastructure that makes portability automatic.

The mechanism matches the Aspirational Declaration meta-pattern at the version-control layer:

- **Declaration element:** README says "clone on any machine, run setup, it works"
- **Consumer assumption:** the repo is portable
- **Missing infrastructure:** nothing checks that committed files are machine-agnostic (no linter for `/home/<username>/...` patterns in tracked files)
- **Failure manifestation:** first transfer attempt reveals hardcoded paths; `.mcp.json` won't load because `/home/jfortin/.venv/bin/python` doesn't exist on the new machine

**The boundary:** MCP protocol REQUIRES absolute paths (no tilde expansion in the spec). You cannot write a portable `.mcp.json` literal — absolute paths are the only valid content. So the file must be regenerated per-machine, which means it cannot be committed. Gitignore + template + generator is the only correct solution.

## Evidence

**Evidence 1: Research wiki `.mcp.json` (2026-04-16)**

Before the fix, `.mcp.json` was tracked in git with:

```json
{
  "mcpServers": {
    "research-wiki": {
      "command": "/home/jfortin/devops-solutions-research-wiki/.venv/bin/python",
      "cwd": "/home/jfortin/devops-solutions-research-wiki"
    }
  }
}
```

Operator noticed when preparing to transfer the repo: "I think there is an issue somewhere where we are configuring using absolute paths so its not compatible when I transfer to another machine." Investigation confirmed the file was committed with one user's home directory baked in. The README's "clone and setup" claim was aspirational for this specific file.

**Evidence 2: The fix — gitignore + template + generator (same session)**

1. `.gitignore` added `.mcp.json` + `.claude/settings.local.json`
2. `.mcp.json.template` committed as reference (with `{{BRAIN_ROOT}}` placeholder)
3. `tools/setup.py --init` generates `.mcp.json` per-machine by resolving `$(pwd)/.venv/bin/python` at setup time
4. README step 3 added: "Run `python3 -m tools.setup --init` after clone"
5. `git rm --cached .mcp.json` untracked the existing committed file

After the fix, transferring to a new machine requires: `git clone → python3 -m tools.setup → python3 -m tools.setup --init`. Step 3 generates the local `.mcp.json` with that machine's absolute paths. Portability is now infrastructure-enforced, not aspirational.

**Evidence 3: Parallel in `sister-projects.yaml` (correctly done from the start)**

The sister-projects registry (`wiki/config/sister-projects.yaml`) uses tilde-form paths (`~/openarms`, `~/openfleet`) with a 2026-04-15 operator directive:

> "paths use `~/` home-expansion form, not absolute `/home/<user>/...` form. This keeps the registry portable across operators/machines — Path.expanduser() resolves `~/` at runtime to the actual home directory."

The registry was fixed early because `Path.expanduser()` handles tilde runtime-resolution inside Python code. MCP config has no such mechanism — hence the different fix (per-machine generation vs runtime expansion). Both are forms of the same insight: commit what's machine-agnostic; generate what's machine-specific.

**Evidence 4: The self-reference test**

The second brain itself is the evidence. The wiki that HOSTS the Aspirational Declaration meta-pattern committed a machine-specific config for months without anyone noticing. The lesson was INVISIBLE until a transfer attempt forced the gap into view — exactly the "gradual then catastrophic" failure mode the meta-pattern names. The fix became available only once operator stress-tested the system against a real constraint (another machine).

## Applicability

| Context | Apply this lesson |
|---|---|
| **Any project that commits config files** | Audit for absolute paths. Grep `/home/`, `/Users/`, `C:\\Users\\` in tracked files. Pattern-match user-specific paths. |
| **Any project using MCP** | Do NOT commit `.mcp.json`. Gitignore it + commit a template + generate per-machine via a setup command. |
| **Any project with `.venv/` paths in config** | Same rule — venv location varies per-machine; any config that references it is machine-specific. |
| **Projects claiming portability in README** | Test the claim: clone on another machine, run setup, verify everything works. Aspirational claims rot until stress-tested. |
| **Consumer-facing integrations** | When an adopter reports "tool doesn't start on my machine," check for committed absolute paths before debugging logic. |

> [!warning] When NOT to apply this lesson
>
> - Projects where all users are on a single shared machine (absolute paths are machine-agnostic in that narrow case)
> - Throwaway POCs that will never be cloned elsewhere
> - Config values that genuinely are the same across all machines (constants, not paths)

## Fix Template

For any project with this issue, the pattern is:

1. **Identify the machine-specific file(s)** — grep for `$HOME` or `/home/<user>`, `/Users/<user>`, etc. in tracked content
2. **Add to `.gitignore`** — the file must stop being tracked
3. **`git rm --cached <file>`** — untrack without deleting on disk
4. **Commit a template** — `<file>.template` with placeholders showing the expected structure
5. **Add a generator command** — `setup.py --init` (or equivalent) that reads the template, fills placeholders with machine-resolved values, writes the real file
6. **Document in README** — "After clone, run `setup --init`" as an explicit step
7. **Stress-test** — clone on a second machine, verify the generator produces a working config

## Self-Check

> [!warning] Before committing any config file, ask:
>
> 1. Does this file contain absolute paths (/home, /Users, C:\Users, /opt, /usr/local, ...)?
> 2. Does this file reference `.venv/` or any generated directory?
> 3. Does this file have content that differs between two machines running the same project?
> 4. If yes to any: does my committed version include a `{{PLACEHOLDER}}` or is it already a fully-resolved real path?
> 5. If fully resolved: this file is not shareable. Gitignore it and commit a template instead.

## How This Connects — Navigate From Here

> [!abstract] From This Lesson → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **The meta-pattern** | [[aspirational-declaration-without-enforcement\|Aspirational Declaration Produces False Confidence]] — this is the 4th-layer instance (version control config) |
> | **The infrastructure principle** | [[infrastructure-must-be-reproducible-not-manual\|Infrastructure Must Be Reproducible, Not Manual]] — `setup --init` is reproducible; manual path-fixing is not |
> | **The sibling at the schema layer** | [[schema-aspirationalism-defining-required-sections-you-neve\|Schema Aspirationalism]] |
> | **The sibling at the skill layer** | [[mandatory-without-verification-is-not-enforced\|Mandatory Without Verification]] |
> | **The sibling at the compliance layer** | [[structural-compliance-is-not-operational-compliance\|Structural Compliance Is Not Operational Compliance]] |
> | **The verb chain that produced the fix** | This lesson itself — the second brain's own `aggregate → process → integrate → modelize → teach` loop applied to its own portability gap |

## Relationships

- DERIVED FROM: [[aspirational-declaration-without-enforcement|Aspirational Declaration Produces False Confidence at Every Layer]]
- BUILDS ON: [[infrastructure-over-instructions-for-process-enforcement|Principle — Infrastructure Over Instructions]]
- RELATES TO: [[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]]
- RELATES TO: [[schema-aspirationalism-defining-required-sections-you-neve|Schema Aspirationalism]]
- RELATES TO: [[mandatory-without-verification-is-not-enforced|Mandatory Without Verification]]
- RELATES TO: [[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]
- FEEDS INTO: [[model-llm-wiki-standards|LLM Wiki Standards]]

## Backlinks

[[aspirational-declaration-without-enforcement|Aspirational Declaration Produces False Confidence at Every Layer]]
[[Principle — Infrastructure Over Instructions]]
[[infrastructure-must-be-reproducible-not-manual|Infrastructure Must Be Reproducible, Not Manual]]
[[Schema Aspirationalism]]
[[Mandatory Without Verification]]
[[structural-compliance-is-not-operational-compliance|Structural Compliance Is Not Operational Compliance]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[LLM Wiki Standards]]
