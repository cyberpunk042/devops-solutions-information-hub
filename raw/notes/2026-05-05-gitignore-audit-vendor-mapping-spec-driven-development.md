---
title: "2026-05-05 — Operator directive: git checkout behavior + .gitignore gap audit + vendor/install-mapping solution + spec-driven-development denotation"
type: note
domain: cross-domain
status: raw
confidence: high
created: 2026-05-05
updated: 2026-05-05
sources:
  - id: operator-directive-2026-05-05-gitignore-and-spec-driven
    type: directive
tags: [note, operator-directive, sacrosanct, verbatim, gitignore, vendor-mapping, install-sh, spec-driven-development, methodology]
---

# Operator directive — 2026-05-05 mid-readiness-loop, post-iteration-4

## Verbatim

> "what happend if I do a git checkout in the root project. is there something that can detect and add the folder to .gitignore ? I will also want to check that we didn't miss any file and folder in the git ignore and that we have a solution for the gitignored ones that need to have mapping that are not gitignored and are able to be installed normally on a new machine with a fresh checkout that we explain to the user how to put into the $home context and how to install and possibly have the auto features like the detect of a large file download or a new vender that could maybe be registered as vendor but clearly not added as complete source into my own root project source. Its imporant to denote too if you had not already realized that we prone spec driven development and a strong methodology and standards. this make a huge difference in the executions and the outputs and the quality and reliability and tracability and operability and observability and project management and progress tracking and LLM Wiki enforment and compatibility exploitation."

## Decomposition (operator's substance, not paraphrased)

### Question A — git checkout behavior
- "what happend if I do a git checkout in the root project."
- "is there something that can detect and add the folder to .gitignore ?"

### Directive B — .gitignore gap audit
- "I will also want to check that we didn't miss any file and folder in the git ignore"

### Directive C — vendor/install-mapping for fresh-machine deploy
- "we have a solution for the gitignored ones that need to have mapping that are not gitignored and are able to be installed normally on a new machine with a fresh checkout"
- "we explain to the user how to put into the $home context and how to install"

### Directive D — auto-features for vendor/large-file detection
- "possibly have the auto features like the detect of a large file download"
- "or a new vender that could maybe be registered as vendor but clearly not added as complete source into my own root project source"
- Operator's qualifier: "possibly" — future module work, not immediate

### Directive E — spec-driven-development + strong methodology + standards (DENOTATION)
- "Its imporant to denote too if you had not already realized that we prone spec driven development and a strong methodology and standards."
- Impact areas operator names verbatim:
  - "executions"
  - "outputs"
  - "quality"
  - "reliability"
  - "tracability"
  - "operability"
  - "observability"
  - "project management"
  - "progress tracking"
  - "LLM Wiki enforment"
  - "compatibility exploitation"

## Action plan (this conversation)

1. Log this directive verbatim — done (this file).
2. Answer Question A factually (no fabrication; check actual /root/.gitignore behavior).
3. Audit .gitignore for gaps per Directive B; present findings without unilaterally modifying.
4. Sketch the vendor-mapping + fresh-machine-install solution per Directive C — design discussion, not implementation.
5. Surface auto-features per Directive D as new backlog module(s) — operator decides if/when.
6. Denote spec-driven-development + strong methodology + standards across the brain files per Directive E. Particularly README.md, AGENTS.md, CLAUDE.md, BOOTSTRAP.md.

## No-conflate guard

- "what happend if I do a git checkout" is a QUESTION, not a directive to perform a checkout.
- "is there something that can detect and add the folder to .gitignore ?" is a QUESTION about capability, not a directive to build it.
- "I will also want to check" — directive to audit, not to fix.
- "we have a solution" — operator wants a solution to exist; design-first, not jump-to-implement.
- "possibly have the auto features" — possibility framing, not commitment.
- "Its imporant to denote" — directive to make the SDD doctrine explicit.

## SDD denotation — context

The operator is flagging that this project is run under spec-driven development. SDD: the source-of-truth is a SPEC, not the resulting code/state. The repo carries the spec; install.sh + tooling realize the spec on each host. This affects:
- What goes in the repo (the spec) vs what doesn't (the realized state)
- What .gitignore allows (spec) vs denies (state, secrets, vendor binaries)
- How a fresh-machine checkout becomes an operational host (run install.sh, which reads the spec)
- How LLM Wiki enforcement applies (the wiki IS spec; methodology.yaml IS spec; identity profile IS spec)
- Why traceability + observability + reliability are higher: the spec is auditable, version-controlled, machine-readable

This is the doctrine that justifies:
- The deny-all + whitelist .gitignore (spec, not state)
- The install.sh + uninstall.sh as the spec-realizer
- The wiki/ tree as the methodology spec
- The brain files as the agent-context spec
