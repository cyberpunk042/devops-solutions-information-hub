---
title: "2026-05-09 — Operator directive: per-project assistant configurations/profiles to spawn OpenClaw/OpenArms/Hermess; research Anthropic -p flag programmatic-use credit/budget policy change; plan Epic + tasks + documents"
type: note
note_type: directive
domain: cross-domain
status: raw
confidence: high
created: 2026-05-09
updated: "2026-05-09"
sources:
  - id: operator-directive-2026-05-09-assistant-configs-and-anthropic-policy
    type: directive
    description: "Operator-stated directive 2026-05-09 covering (1) per-project assistant configurations/profiles, (2) Anthropic -p flag programmatic-use billing/budget policy reportedly changed, (3) Max x20 monthly $240 value-at-risk if not used through finished Assistant/advanced systems, (4) research-confirm + plan + create tasks/Epics/documents"
tags: [operator-directive, sacrosanct, verbatim, "2026-05-09", per-project-assistant-config, assistant-profile, openclaw, openarms, hermess, anthropic-policy, p-flag, programmatic-use, credit-budget, max-x20-plan, value-at-risk, research-task, epic, tasks-needed, raw-note, ai-agents, billing-policy]
---

# Operator directive — 2026-05-09 per-project assistant configurations + Anthropic programmatic-use policy research

## Verbatim (operator, sacrosanct)

> "continue. we need to finish what is on the table and then:
> Now repos / projects will have assistants configurations / profiles.. e.g. in the knowledge/information-hub we will have one taillored to the needs. the goal is to be able to use those to spawn an OpenClaw or OpenArms or Hermess and whatever and have high quality definitions and features. I think Anthropic changed that the -p option which was our workaround to not be treated as programmatical is now counted as programmatic use and now also considered credit budget but at the same time now they would give each month the equivalent of the month of budget in token for the programmatic uses ? I think thats what I read. so on max x20 its equivalent of 240$ lost if not used with something like such Assistant or our advanced systems which are not finished. but we can confirm all that, do our research. record what I said, plan what is needed and create all the neeed tasks, Epics and documents."

## Decomposition

### A — Sequence: finish on-the-table → then engage new directive
- "continue. we need to finish what is on the table and then: [new context introduced]"
- Current on-the-table arc (hook schema-validity + audit-on-distillation) is closed (raw-note audit + 5 raws confirmed discharged earlier this turn).
- "And then" = sequencing word; proceed to the new directive.

### B — Per-project assistant configurations/profiles
- "repos / projects will have assistants configurations / profiles"
- Each repository / project will have its OWN assistant configuration / profile
- These profiles are TAILORED to the project's needs
- Example: this project (`knowledge/information-hub` — the /opt second-brain research wiki) will have a tailored profile

### C — Profiles spawn ecosystem-project instances
- "the goal is to be able to use those to spawn an OpenClaw or OpenArms or Hermess and whatever"
- Profiles produce **spawnable assistant instances** of: OpenClaw, OpenArms, **Hermess** (NEW project name not previously surfaced in /opt — verify in sister-projects.yaml or operator-clarify), "and whatever" (extensible)
- The profile is the **source**; the assistant instance is the **product**

### D — Quality framing
- "high quality definitions and features"
- The point of the profile-based spawn approach is QUALITY — definitions and features both
- Anti-pattern: low-quality / improvised / one-shot assistant configurations

### E — Anthropic policy change (NEEDS RESEARCH/CONFIRMATION)
- "I think Anthropic changed that the -p option which was our workaround to not be treated as programmatical is now counted as programmatic use"
  - Claim: `-p` flag (a CLI workaround that previously bypassed programmatic-use classification) NOW counts as programmatic use
  - **Operator uncertainty signaled**: "I think"
- "and now also considered credit budget"
  - Claim: programmatic use now counts against credit budget
- "but at the same time now they would give each month the equivalent of the month of budget in token for the programmatic uses ?"
  - Claim: Anthropic might now grant a monthly programmatic-use token allowance equal to the monthly subscription budget
  - **Operator uncertainty signaled**: "?" + "I think thats what I read"

### F — Value-at-risk on Max x20 plan
- "so on max x20 its equivalent of 240$ lost if not used with something like such Assistant or our advanced systems which are not finished"
- Calculation: on the Max x20 plan, **$240/month equivalent value is lost** if the programmatic-use allowance is NOT consumed via something like (a) per-project Assistant, (b) operator's advanced systems (not yet finished)
- "Max x20" = a plan tier; need to confirm what x20 means (likely 20× multiplier on standard plan? or $200/month plan? confirm via research)
- "our advanced systems which are not finished" = operator's in-flight infrastructure work (likely root-ghostproxy + SDD + custom-tailored model group + harness chain)

### G — Verification + planning + artifact creation
- "but we can confirm all that, do our research"
  - **Research task**: confirm A through F via Anthropic official sources
- "record what I said"
  - **Logging task**: capture verbatim (this file, done now)
- "plan what is needed"
  - **Planning task**: design the per-project assistant configuration system
- "create all the neeed tasks, Epics and documents"
  - **Backlog task**: create Epic + modules + tasks; author supporting documents (decision pages, patterns, syntheses)

## Action plan (priority order, per operator sequence)

| # | Action | Type | Status |
|---|---|---|---|
| 1 | Log this directive verbatim BEFORE acting (this file) | hard rule | ✅ done now |
| 2 | Check if "Hermess" is a known sister project | clarification | pending |
| 3 | Check operator-decision-queue.md to confirm "what is on the table" is closed | verification | pending |
| 4 | Research Anthropic policy claims (E + F): -p flag billing, programmatic-use budget allowance, Max x20 plan details, $240 calculation derivation | research | pending |
| 5 | Author source-synthesis(es) for the Anthropic policy findings | synthesis | pending |
| 6 | Plan the per-project assistant configuration system architecture (with /opt-tailored example) | planning | pending |
| 7 | Author Decision record for the strategy approach | decision | pending |
| 8 | Author Epic + modules + tasks in `wiki/backlog/` for the implementation | backlog | pending |
| 9 | Author Pattern record for "per-project assistant profile → spawnable instance" architecture | pattern | pending |
| 10 | Pipeline post (mandatory, 0 errors) | gate | pending |
| 11 | Report findings + open operator-decisions surfaced | reporting | pending |

## No-conflate guard

- **"assistants configurations / profiles"** — these are configuration/profile artifacts that define an assistant, NOT the assistant runtime itself. The runtime is OpenClaw / OpenArms / Hermess; the profile is the spec that the runtime consumes.
- **"in the knowledge/information-hub we will have one"** — singular "one" tailored to /opt's needs. Don't author multiple profiles per project; one profile per project that captures the project's needs comprehensively.
- **"OpenClaw or OpenArms or Hermess and whatever"** — pluggable runtime list. The profile design must be runtime-agnostic enough to spawn ANY of these.
- **"I think... I think thats what I read"** — operator-stated uncertainty. The Anthropic policy claims (E + F) are HYPOTHESES requiring research confirmation. Do NOT propagate as facts without verification.
- **"240$ lost if not used"** — derived calculation under uncertainty; the actual $240 figure depends on the unconfirmed monthly-allowance policy. Frame as "if policy is X, then $Y/month at risk."
- **"such Assistant or our advanced systems which are not finished"** — the per-project Assistant IS the operator's proposed remedy to capture the value-at-risk. The "our advanced systems which are not finished" = parallel in-flight work; don't conflate Assistant scope with that.
- **"plan what is needed and create all the neeed tasks, Epics and documents"** — operator explicitly invites creation of multiple artifacts (plural: tasks, Epics, documents). The Epic-with-modules-and-tasks decomposition pattern is invited.

## Forward chain (cross-cutting)

This directive layers onto operator's previously-signaled post-compact plan:

- *"there is also a ton of new artifacts we will discuss after with what we are going to do with root-ghostproxy and progressively and the SDD and enforment and such"* (2026-05-09 — referenced in the strong handoff)
- *"we prone spec driven development and a strong methodology and standards"* (2026-05-05 — SDD doctrine, 11-impact-area denotation)
- *"there is also a new plan for an AVX512 machine witha custom strategy"* (2026-05-09 — captured in hardware-pending flag on the Custom-Tailored Model Group concept)

Per-project assistant configs may interact with: root-ghostproxy (harness/ecosystem propagation), SDD (the per-project profile IS spec-driven), enforcement (profile defines enforcement layer per project), Custom-Tailored Model Group (the profile may select model groups per project).

Adding ≠ discarding (operator 2026-04-24): the new directive LAYERS on the prior chain. Per-project Assistant is a forward-extending direction; root-ghostproxy + SDD + custom-model-group all continue.
