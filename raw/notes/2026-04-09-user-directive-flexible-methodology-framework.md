# User Directive — 2026-04-09 — Flexible Methodology Framework

## Verbatim

> lets reprocess everything I told you. I this model is to be flexible. this is a very important part. it is to be able to contain multiple model for multiple condition based of stage[s], phase[s], or any other condition structured we need it.
> E.g. able to follow a 3 sequences inside the methodology group and also able to take a complete other sequence / group of methodology, into whatever adapted order and ranges and whatnot..
>
> This is not a lazy task, this is the top of art

## Interpretation

The methodology framework is NOT a single fixed pipeline. It is a CONTAINER of multiple methodology models that can be:
- Selected per-condition (project type, task type, phase, scale)
- Combined (follow sequence A for stages 1-3, switch to sequence B for stages 4-5)
- Nested (a methodology group can contain sub-groups with their own sequences)
- Adapted (order, ranges, readiness thresholds, required artifacts — all configurable per model)

Examples:
- A "research" methodology model: document → cross-reference → synthesize → evolve
- A "feature development" model: document → design → scaffold → implement → test
- A "spike" model: document → design (stop)
- A "hotfix" model: implement → test (only)
- A "full project" model: contains research + feature dev + deployment sub-models in sequence

The framework defines:
1. What a "methodology model" IS (a named sequence of stages with artifacts and gates)
2. How models are SELECTED (conditions: task_type, project phase, domain, scale)
3. How models COMPOSE (sequential, nested, conditional branching)
4. How models are ADAPTED (override stages, artifacts, ranges per instance)

This is the highest level of the system — the meta-methodology. Not one process, but a process-definition framework.

This is top-of-art work. Not shortcuts. Not lazy.
