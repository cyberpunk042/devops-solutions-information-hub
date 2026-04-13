---
title: "Documentation Layers + Old Model Tolerance"
type: note
domain: log
note_type: directive
status: active
confidence: high
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [log, directive, documentation, layers, code-docs, wiki, public-docs, old-models, alignment]
---

# Documentation Layers + Old Model Tolerance

## Summary

There are distinct documentation layers that must not be conflated: wiki knowledge, public docs, code docs (inline/JSDoc/headers), and smart docs throughout code. The second brain must be clear about what is what. Projects with old models should be tolerated but aligned to the new model when the second brain is attached.

## Operator Directive (verbatim)

> there is also the nuance between wiki and public docs and code docs (like there is in this project /home/jfortin/devops-control-plane/, you can see some docs, considered potential smart docs, can be throughout the code / src or whatnot + the JSDOc or equivalent / headers and annotations and parameters comments and whatnot and inner comment.) it needs to be clear what is what.
> The reality that some agent will conflate or that some project have an old model but if the second brain is attached then its one of our project so we shoul align with the new model and just tolerate the old models and possibly even do cleaning / refactoring.

## Interpretation

### Documentation Layers (must be distinct)

1. **Wiki knowledge** (wiki/) — synthesized, structured, evolving knowledge with frontmatter and relationships. The second brain's core.
2. **Public docs** (docs/) — user-facing documentation, READMEs, guides. For humans consuming the project.
3. **Code docs** — documentation throughout the code and inline comments, JSDoc/docstrings, parameter annotations, function headers. Lives IN the source code.
4. **Smart docs** — documentation overlay of files distributed throughout src/ that explain subsystems alongside the code they document. Basically the aggregation of the Code docs.
5. **Specs and plans** (docs/superpowers/) — execution track artifacts. Temporary by nature — they serve the build process, not the knowledge base.

These are DIFFERENT layers. An agent must not:
- Put wiki knowledge in code comments
- Put code docs in the wiki
- Conflate public docs with wiki pages
- Mix specs with permanent knowledge

### Old Model Tolerance

When the second brain attaches to a project that predates the new model:
- **Tolerate** the existing structure — don't break what works
- **Align incrementally** — introduce wiki/, config/, templates as additions, not replacements
- **Cleaning/refactoring** is valid — move scattered docs into proper structure over time
- The old model is not wrong — it's just not the current standard. Coexistence is fine during transition.

## Relationships

- RELATES TO: [[Model Registry]]

## Backlinks

[[Model Registry]]
