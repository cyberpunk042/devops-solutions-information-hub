# User Directive — 2026-05-16 — Sovereign OS Arc Opening + SFIF + IaC + Handoff Mandate

## Verbatim

### Initial /goal directive (2026-05-16, arc opening — typed via /goal slash command; full text follows, exceeded 4000-char limit so operator pasted as fallback)

> continue till we reach the point we have the whole series of scripts to generate and configure and build a custom image / custom OS and all the costomization that is possible and even needed. to the point pre, during and post. all in Spec Driven Development and Test Driven Development. This is multi-steps and there are even interatives modes and managements commands/tools and its not only about build a kernel and/or an OS and/or an OS configuration profile and/or our own added services and install and modules... All the "whitelabelling" with respect to the original image like if it was Debian 13 surely we will still see it written somewhere in the /etc/issue for example. its not only script its all the common libs and all the custom config and all the profiles and all the options and documentation.. All in the right order to the utmost level. once we feel ready we can even use the plan feature that I can see in this Claude Code online Resaerch preview that we are working together in. could give us another surface of work that we can keep up to that as also part of the goal, or goals should I say. So yeah there is a lot of detail to build a proper image and do our research, onine and local to be able to move toward the best and adapted solution + our own customization and fine-tuning and features. You can work with this goal on selfdef too when you need, second-brain/infration-hub will have its limit or rather have its own responsability. but then again it starts there before we can do proper Spec to start proper SDD and TDD. Its going to be very very very long I am very aware of that. I am aware that you might have limitations too we will find what you can and cannot do and find the best ways and sometimes you will using the proper system we put in place like adding questions make sure we keep this tracked and alive and if you answer yourself as you make sure it has enough level to surface to me then so be it and then it becomes a statement, a question answered and tracked. We will have to think large and wide, something that can evolve and be costomize and installed differently, but clearly the default profile right now will be for the new AI Workstation that was already recorded with the RTX pro 6000. We will exploit the latest technologies and models and our hardware to the most, and even integrate our wild ideas like how much we can exploit a 512 bit CPU... so much room, not just for batching but new features, new logics, new advancements. This also possibly mean building different profile of the OS and customizations and even level of pre-integration or even pre-installed and pre-configured and such. Do not rush anything and do not minimize anything nor should you compress or conflate or hallucinate anything, just take the time and do things right. We think before we act always. And we do things in order and we respect workflows and methodologies. It will allow us to explore so much... so much LLM and variants and Small Language Models (SLMs) and Recursive Language Models(RLMs), and whatever we said that we would set to do my "old" workstation with only a 11GB + 8 GB card. Which ultimately will later gain from trained models or knowledge in general but clearly our goal is now the AI workstation and making sure the OS and the configuraion and all the scripting and proper pipeline / steps by steps and flexibility, options, proper guiding and details and an assistant feeling as we are going through the building and all the layer and/or chosing the flavor and options and then the post install script ready to be pre-added or even automatically launch on first login and such. based on what is chosen by the user. Everything being able to evolve, before and after.  even once installed and configured it will be possible to manage the OS like we need to even if we need to add such an additional tool and even service possibly or even multiple adapted if need be. We do this clean and right and professional. Some things we can only prepare for and wait to have the hardware and have it assembled and ready to instead but a lot of things we can progress so much and even achieve and do them properly through the workflow and SDD and proper online research always. even things I do not even know yet. this is all new to me after all, but I think I have put together quite the interesting product to at least be busy for a while and unlock clear and strong potential and reach our ultimate sovereignty. Remember that I want things observable and operable and customizable, at all stages of lifecycle. You can also use the knowledge of the second-brain obviously there is a lot to search in there too and maybe you can even start there but do not take this for granted, we aim another level and I dont even know if we can stick with LocalAI I think would limite us, but you will find the answers and the solutions.

### Operator answers to framing questions (Round 1, 2026-05-16)

After the agent surfaced four framing questions via `AskUserQuestion`, the operator answered:

| Question | Answer |
|---|---|
| Where should the OS-build pipeline arc live primarily? | **New repo: `sovereign-os`** |
| Image-build substrate: research first, or commit to one now? | **Research SDD first (substrate not picked)** |
| Profile structure (default = SAIN-01 / RTX Pro 6000) from day 1? | **Schema-first, multi-profile from day 1** |
| Use the Plan tool / agent to render the macro-arc plan? | **Yes — Plan agent for the macro-arc, after your answers above** |

### Operator answers to framing questions (Round 2, post-Plan-agent, 2026-05-16)

After the Plan agent returned and the agent surfaced three pre-PR-1 questions:

| Question | Answer |
|---|---|
| Visibility for the new `cyberpunk042/sovereign-os` repo? | **Public** |
| License for `sovereign-os`? | **Match selfdef (whichever it is)** — verified by the agent as **AGPL-3.0-or-later** from `cyberpunk042/selfdef/LICENSE` |
| Substrate-survey excludes (any to remove from PR 4 scope)? | (verbatim — adds Q-016 substrate-base-reconsideration to the survey) |

> well I think Debian 13 was the right choices but you can put that into questions into the fact if it would unlock relevant potentials and especially not lose major other features and unlocked potentials. so you can do some research but obviously if we do a Debian 13 custom image we have to accept that some things are not meant for us and we need to find what is the right equivalent for us or document it properly. SO yeah a bit like you said, dont judge either. we are not in a rush

### Operator post-decision directive (SFIF + IaC + Debian-as-Ark + Handoff Mandate, 2026-05-16)

After the agent reported the GitHub MCP 403 blocking repo creation:

> oh and as always we remember the SFIF, Skaffold, Fundation, Infrastructure, Features. And we always deliver IaC, high quality scripts and libs and configuration and easily tweakable and configurable and customisation and even via env vars when needed, or other pre-existing config or temporary file detected and restarting from there such as if there is has to be a local tracking of the progress of a build in multi-steps that can only ever re-happen locally. I think Debian is a bit like saying we have our Arc but we start from there, kind of thing ?
> I will create the repo but that will also require me to start a new session.. so this session needs to be ready to pick up. so start the handoff and all the knowledge transer, no matter how many documents. Dont even ask me question, just get to it.

## Interpretation

### Distinct Topics Identified

#### 1. New cross-repo arc: `cyberpunk042/sovereign-os`

The operator opens a new multi-month engineering arc to build a complete OS-image generation + customization pipeline for the SAIN-01 AI workstation (and other profiles). The repo `sovereign-os` is the upstream pipeline that BUILDS the OS; selfdef RUNS on the OS; info-hub SYNTHESIZES knowledge. Four-repo ecosystem.

The architectural baseline (info-hub `wiki/backlog/milestones/sain-01-sovereign-node.md` + 11 epics) is already locked. The new `sovereign-os` repo's job is to materialize those epics as scripts / configs / profiles / tests / lifecycle tools — without duplicating their architectural design.

#### 2. SFIF discipline applies (verbatim: "we remember the SFIF, Skaffold, Fundation, Infrastructure, Features")

The operator's universal 4-stage build lifecycle, previously documented in
`raw/notes/2026-04-09-user-directive-raw-idea-flow-patterns-standards.md`:

- **Scaffold** — core config, project structure, tech stack, AI files, READMEs
- **Foundation** — modules, design system, spine structure, diagrams, architecture docs, single entry point
- **Infrastructure** — common components others depend on, basic interface, development guidelines
- **Features** — specialized product features built on the established base

The sovereign-os arc itself follows SFIF: PRs 1-3 are Scaffold; PRs 4-8 are Foundation; PRs 9-10 begin Infrastructure (TDD harness); subsequent arcs (Stage 2 onwards) deliver Infrastructure + Features.

#### 3. IaC + quality bar (verbatim: "we always deliver IaC, high quality scripts and libs and configuration and easily tweakable and configurable and customisation and even via env vars when needed, or other pre-existing config or temporary file detected and restarting from there such as if there is has to be a local tracking of the progress of a build in multi-steps that can only ever re-happen locally")

Concrete requirements baked into every PR in sovereign-os:

- **IaC discipline** — every operational pattern as reproducible tooling. No manual infrastructure. Declarative where possible.
- **High quality scripts and libs and configuration** — selfdef's quality bar applies.
- **Easily tweakable + configurable + customisable** — env vars; pre-existing config detection; temp-file detection for restart-from-state. The build pipeline is a **resumable, observable multi-step process**, not a one-shot script.
- **Local tracking of build progress** — multi-step builds can only happen locally (no centralized state). A build that crashes at step 7 of 12 must be resumable from step 7 on the next attempt.

#### 4. "Debian as Ark" framing (verbatim: "I think Debian is a bit like saying we have our Arc but we start from there, kind of thing ?")

Operator's mental model: Debian 13 is the **starting boat**, not the destination. We start from Debian (battle-tested, predictable, modern libraries, GCC 14 baseline) and customize so heavily we end up somewhere distinct. The Ark carries us out; the destination is sovereign.

This frames the Q-016 substrate-base question: alternatives to Debian 13 (Fedora / openSUSE / Arch / Nix) get surveyed, but the working hypothesis is **stay on Debian 13 + customize the boat**. If staying on Debian costs us material potential, document the loss + the equivalent we'd build for ourselves.

#### 5. Handoff Mandate (verbatim: "I will create the repo but that will also require me to start a new session.. so this session needs to be ready to pick up. so start the handoff and all the knowledge transer, no matter how many documents. Dont even ask me question, just get to it.")

Operator-side action item: **operator creates `cyberpunk042/sovereign-os` manually** (GitHub UI or `gh repo create`) AND expands the agent's MCP scope to include it. This requires a new session because MCP scope changes on the operator side.

Agent-side action item (THIS session, immediate): **prepare ALL the handoff knowledge transfer** so the next session can pick up cleanly without re-deriving the plan. Multiple documents OK. No more framing questions — execute.

### Action Items (this PR — info-hub side)

1. **DONE in this PR**: this verbatim operator-directive log at `raw/notes/2026-05-16-user-directive-sovereign-os-arc-opening.md`
2. **DONE in this PR**: the verbatim Plan-agent output at `raw/dumps/2026-05-16-sovereign-os-macro-arc-plan.md` (preserves the L0 baseline for the foundation phase)

### Action Items (selfdef side — paired PR)

1. **`docs/sdd/011-sovereign-os-arc-opening.md`** — SDD documenting the new fourth-repo arc; bridges Stage 2 (selfdef-on-SAIN-01) to the new sovereign-os concern; SFIF mapping; IaC quality bar; "Debian as Ark" framing.
2. **`docs/decisions.md` D-026** — captures the new-repo decision + the Plan adoption + the operator's framing answers.
3. **`docs/handoff/2026-05-16-sovereign-os-arc-opening.md`** — supersedes `2026-05-16-end-of-stage2-anchor.md`; comprehensive next-session cold-start signpost; tells the new session exactly what to do and where to find every prior artifact.

### Action Items (subsequent operator-side, NOT in this PR)

1. **Create `cyberpunk042/sovereign-os` repo** — public, AGPL-3.0-or-later (mirror selfdef), README auto-init, no preset .gitignore, no preset license (PR 1 lands LICENSE).
2. **Expand agent MCP scope** to include the new repo so subsequent PRs work.
3. **Open new session** + read the selfdef handoff at `docs/handoff/2026-05-16-sovereign-os-arc-opening.md`.
4. **Say "go"** in the new session → agent opens PR 1 against the new repo (charter stub + repo skeleton, ~600 LOC).

### Hallucinations / Wrong Tokens Flagged

None this round. Operator's verbatim text is the source-of-truth; the Plan agent's output is preserved verbatim too.

### Verified Facts (from preliminary lookups)

- **selfdef LICENSE**: AGPL-3.0-or-later (verified by reading `cyberpunk042/selfdef/LICENSE` SHA ca25ce46).
- **GitHub MCP scope**: the agent's restricted to `cyberpunk042/selfdef`, `cyberpunk042/root-ghostproxy`, `cyberpunk042/devops-solutions-information-hub`. `sovereign-os` is OUTSIDE current scope. Repo-create call returned `403 Resource not accessible by integration`. Operator-side expansion required.
- **Architectural baseline**: info-hub `wiki/backlog/milestones/sain-01-sovereign-node.md` (the SAIN-01 milestone + 11 epics) is the upstream architectural baseline. sovereign-os implements it without duplicating the architectural design.

## Relationships

- FEEDS INTO: `raw/dumps/2026-05-16-sovereign-os-macro-arc-plan.md` (the Plan agent's L0 output authorized by this directive)
- DERIVED FROM: `raw/notes/2026-04-09-user-directive-raw-idea-flow-patterns-standards.md` (the original SFIF directive)
- DERIVED FROM: `wiki/backlog/milestones/sain-01-sovereign-node.md` (architectural baseline)
- ENABLES: future `cyberpunk042/sovereign-os` repo (operator-side bootstrap pending)
- ENABLES: future selfdef `docs/sdd/011-sovereign-os-arc-opening.md` (the selfdef-side bridge)
- ENABLES: future selfdef `docs/handoff/2026-05-16-sovereign-os-arc-opening.md` (the next-session cold-start anchor)
- RELATES TO: existing `cyberpunk042/selfdef` SDD-010 (Stage 2 — selfdef-on-SAIN-01); the new sovereign-os arc is architecturally upstream of selfdef's Stage 2 work
