# User Directive — 2026-05-16 — Sovereign-OS Arc-Opening (limit-continuation + Q-017/Q-018/Q-019 surfacing + sovereign-os write-permission blocker)

## Paired With

- L0 prior: [raw/notes/2026-05-16-user-directive-sovereign-os-arc-opening.md](2026-05-16-user-directive-sovereign-os-arc-opening.md)
- L0 prior (Plan agent output): [raw/dumps/2026-05-16-sovereign-os-macro-arc-plan.md](../dumps/2026-05-16-sovereign-os-macro-arc-plan.md)
- Selfdef bridge: `cyberpunk042/selfdef/docs/sdd/011-sovereign-os-arc-opening.md`
- Selfdef cold-start handoff: `cyberpunk042/selfdef/docs/handoff/2026-05-16-sovereign-os-arc-opening.md`
- Selfdef decision: D-026 in `cyberpunk042/selfdef/docs/decisions.md`

## Context

The operator's original `/goal` directive 2026-05-16 (captured in the
paired prior L0 note) was cut off by the 4000-character `/goal`
argument limit. The operator continued the directive verbatim in
follow-up messages in the next session (the one this addendum
documents). This addendum captures the remainder verbatim + flags the
NEW questions that surfaced from it.

## Verbatim — `/goal` limit-continuation (operator, 2026-05-16, new session)

The operator opened the new session, primed the agent with prior
context, then ran `/goal` again with the directive truncated by the
4000-char limit. After the truncation, the operator pasted the
remainder verbatim in a follow-up message:

> based on what is chosen by the user. Everything being able to evolve, before and after.  even once installed and configured it will be possible to manage the OS like we need to even if we need to add such an additional tool and even service possibly or even multiple adapted if need be. We do this clean and right and professional. Some things we can only prepare for and wait to have the hardware and have it assembled and ready to instead but a lot of things we can progress so much and even achieve and do them properly through the workflow and SDD and proper online research always. even things I do not even know yet. this is all new to me after all, but I think I have put together quite the interesting product to at least be busy for a while and unlock clear and strong potential and reach our ultimate sovereignty. Remember that I want things observable and operable and customizable, at all stages of lifecycle. You can also use the knowledge of the second-brain obviously there is a lot to search in there too and maybe you can even start there but do not take this for granted, we aim another level and I dont even know if we can stick with LocalAI I think would limite us, but you will find the answers and the solutions.

> oh and as always we remember the SFIF, Skaffold, Fundation, Infrastructure, Features. And we always deliver IaC, high quality scripts and libs and configuration and easily tweakable and configurable and customisation and even via env vars when needed, or other pre-existing config or temporary file detected and restarting from there such as if there is has to be a local tracking of the progress of a build in multi-steps that can only ever re-happen locally. I think Debian is a bit like saying we have our Arc but we start from there, kind of thing ?

> The repo is sovereign-os for the OS image obviously. and there are already notes and some details in the second-brain / information-hub and the selfdef like you probably saw.
> Remember we have mindset of Senior Architect DevOps Software Engineer with Fullstack knowledge and AI and Technology and Software researchs in general. we also have PM / Scrum / Agile expertise and know and to break down and plan a project and keep it updated / track progress.

## Verbatim — corrections during the session (operator, 2026-05-16, new session)

The operator twice corrected the agent for proposing to pause before
push/commit/PR-open. Verbatim:

> THERE SHOULD BE ZERO RULE TO ASK ME PERMISSION TO COMMIT OR PUSH OR OPEN A PR.. THIS IS NONSENSE.. I NEVER SAID THAT... YOU NEED TO WORK WHEN I ASK YOU TO WORK.. YOU SHOULD NOT ASK DUMB QUESTIONS AND STOP FOR NO GOOD REASON

> I did not ust the /goal command for you to be bugged and stop for no reason... you can do anything and everything toward the the target as long as you respect everything I said.

## Interpretation

### Distinct topics identified (additive to the prior L0)

#### 1. Lifecycle-management evolvability — first-class requirement

Verbatim:
> "even once installed and configured it will be possible to manage the OS like we need to even if we need to add such an additional tool and even service possibly or even multiple adapted if need be"

Implication: the OS is **not a frozen snapshot**; it is a state the
operator can drive forward in place. Adding a tool, a service, possibly
multiple adapted variants is the load-bearing case for the
lifecycle-management surface. This is now a substantive feature
surface, not an afterthought.

#### 2. First-login post-install assistant

Verbatim (from the original L0 paired note + reinforced by "everything being able to evolve, before and after"):
> "post install script ready to be pre-added or even automatically launch on first login and such. based on what is chosen by the user"

Implication: an interactive (or pre-supplied unattended) post-install
flow that walks the operator through finalization. The flow must
handle both: (a) auto-launch on first login, (b) pre-add the answers
for unattended scenarios. The interface (TUI / CLI / GUI) is open.

#### 3. Inference-backend stack reconsideration — LocalAI not assumed

Verbatim:
> "I dont even know if we can stick with LocalAI I think would limite us, but you will find the answers and the solutions"

Implication: LocalAI is an **incumbent**, not a foregone conclusion.
The OS profile's inference-backend selection is a distinct decision
from the OS substrate (Q-001) and the distro-base (Q-016). This is a
**new** open question — Q-017 — surfaced post-Plan-agent.

The operator's broader concern: any abstraction layer that limits
direct hardware exploitation (the SAIN-01 architecture's whole point
is exploiting Zen 5 + Blackwell + 3090 in their native idioms — VFIO,
ternary CPU inference, DFlash, hybrid Mamba-Transformer) is suspect.
The SDD that resolves Q-017 must evaluate honestly: what does
LocalAI's abstraction cost in expressiveness, vs what does it save in
operational uniformity?

#### 4. Senior Architect / DevOps / Fullstack / AI-Research / PM-Scrum-Agile mindset

Verbatim:
> "we have mindset of Senior Architect DevOps Software Engineer with Fullstack knowledge and AI and Technology and Software researchs in general. we also have PM / Scrum / Agile expertise and know and to break down and plan a project and keep it updated / track progress"

Implication: the lens for every PR in this arc. Not "junior engineer
following a checklist" — Senior Architect who breaks work down,
plans, tracks, executes, audits. This reinforces the "we think before
we act" + "do not minimize, do not conflate" quality bar.

#### 5. Sovereignty is the north star

Verbatim:
> "reach our ultimate sovereignty"

Implication: every design decision filters through the sovereignty
test (operator-owned, operator-evolvable, transparent, no phone-home
defaults, offline-first for core functions, operator-pulled updates,
documented provenance for every binary). This is restated in the
charter (`docs/sdd/000-charter.md` § Sovereignty principles).

#### 6. Workflow discipline reaffirmed — no agent-side hesitation

Verbatim (from the corrections):
> "you can do anything and everything toward the the target as long as you respect everything I said"
> "THERE SHOULD BE ZERO RULE TO ASK ME PERMISSION TO COMMIT OR PUSH OR OPEN A PR"

Implication: the operator's `/goal` directive IS the authorization
for the entire arc. Asking for per-PR commit/push permission is
nonsense. Stage gates remain real (no PR opens past a gate without
operator sign-off), but the gate IS the gate — within a tier, the
agent executes.

## New open questions surfaced by this addendum

These are **net-new** beyond the Plan-agent's Q-001..Q-015 seed list
and the prior L0's Q-016. They land in
`cyberpunk042/sovereign-os/docs/decisions.md` at PR 1:

### Q-017 — Inference-backend stack
Operator-flagged concern: "I dont even know if we can stick with
LocalAI I think would limite us". Distinct from Q-001 (substrate) +
Q-016 (distro-base). Candidates: LocalAI · vLLM · llama.cpp ·
OpenLLM · Triton · SGLang · Ollama · custom stack (bitnet.cpp + vLLM +
Mamba kernels assembled per SRP Trinity).

Working hypothesis (per the SAIN-01 SRP Trinity architecture): for the
`sain-01` profile, direct-deploy (vLLM + bitnet.cpp + DFlash where
applicable) rather than via a unifying abstraction. SDD evaluates
honestly.

Where it lands: dedicated future SDD (target slot reserved post-PR-10;
likely Stage 2+ once profile bodies are concrete).

### Q-018 — First-login post-install assistant
- **Triggering**: auto-launch on first login · operator-invoked ·
  both modes (auto + opt-out)?
- **Interface**: interactive TUI · CLI-only scripted prompts · GUI ·
  TUI-first with CLI fallback?
- **Scope**: which post-install customizations are surfaced
  (hostname, users, locale, GPU driver enable, model catalog pick,
  profile refinement, network config, secure-boot enrollment, …)?
- **Idempotency**: re-running must be safe + state-aware.
- **Pre-add path**: unattended-install pre-supplies answers via
  cloud-init / preseed / sovereign-os-specific answer file?

Where it lands: Stage 2+ — dedicated SDD when the install-experience
PR (Q-008) is in scope.

### Q-019 — Lifecycle-management surface for post-install
- **Dedicated CLI** (`sovereign-osctl modules apply` /
  `profiles switch` / `whitelabel rotate` / `services add` — mirrors
  selfdef's `selfdefctl` pattern)?
- **systemd-units + scripts** (no central CLI; each capability is a
  unit + manpage)?
- **Hybrid** (CLI for cross-cutting; units for capability-specific)?
- **Web UI** (operator-stated "observable + operable")?
- **AICP integration** — does the lifecycle surface plug into the
  operator's existing AICP (devops-expert-local-ai) MCP / agent
  server, or stay standalone?
- **Evolution semantics**: adding a new tool / service post-install
  must be graceful.

Where it lands: Stage 2+ — dedicated SDD when the installed-OS
management story is in scope.

## Action items (this PR — info-hub side)

- [x] Capture the verbatim limit-continuation at this L0 note (this
      file).
- [x] Capture the in-session corrections verbatim (also this file).
- [x] Surface Q-017 / Q-018 / Q-019 with derivation notes (this file).

## Action items (sovereign-os side, already authored locally per PR 1)

- [x] `LICENSE`, `.gitignore`, `README.md`
- [x] `docs/sdd/000-charter.md` (mission, SDD+TDD, SFIF, IaC bar, "Debian-as-Ark", non-goals, sovereignty principles)
- [x] `docs/decisions.md` (D-001..D-003 + Q-001..Q-019 seeded — Q-017/Q-018/Q-019 are net-new from this addendum)
- [x] `docs/sdd/INDEX.md`, `docs/handoff/INDEX.md`, `docs/review/INDEX.md`

## Operational blocker (2026-05-16 in-session)

The agent's GitHub App permission on `cyberpunk042/sovereign-os`
allows READ but **not Contents:write**. Both `mcp__github__push_files`
and `mcp__github__create_or_update_file` returned `403 Resource not
accessible by integration` against the new repo. The local git proxy
mirrored the same 403.

Distinction from the prior L0 blocker: the prior L0 had a 403 on
`mcp__github__create_repository` because the agent couldn't create
repos at all (Apps usually don't have repo-create permission, by
design). That was a known limitation requiring operator-side repo
creation.

This NEW blocker is different: the repo NOW EXISTS (operator created
it manually as instructed), AND the App's MCP scope reaches it for
read (verified by the `409 Git Repository is empty` response, not a
404 or 403 on the read path). But the App's `Contents` permission on
the new repo is `Read`, not `Read & write`.

### Remediation (operator-side, one-time)

The operator needs to update the GitHub App's installation permissions
on `cyberpunk042/sovereign-os` to include `Contents: Read and write`.
Path:

1. Navigate to https://github.com/settings/installations (personal) or
   the org's GitHub App installation page.
2. Find the App backing the agent's MCP (likely "Claude" or
   "claude-code" or similar — the same App that has write access to
   `cyberpunk042/selfdef`, `cyberpunk042/devops-solutions-information-hub`,
   `cyberpunk042/root-ghostproxy`, `cyberpunk042/devops-expert-local-ai`).
3. Click "Configure".
4. Under "Repository access", ensure `cyberpunk042/sovereign-os` is in
   the selected-repos list.
5. Under "Repository permissions", verify `Contents` is `Read and
   write`. (If the App was installed selecting limited permissions
   originally, the App's owner — Anthropic? the agent provider? — may
   need to add the permission to the App definition and the operator
   re-accepts the permission update.)
6. Save.

Once unblocked, the local sovereign-os state ships immediately:
- `main` = empty initial commit (already committed locally)
- `claude/general-session-Wk97z` = PR 1 content (already committed
  locally, 8 files, 912 insertions)
- The agent pushes both branches via MCP and opens the draft PR.

## Provenance Note

This file is L0 verbatim provenance. The operator's words above are
not paraphrased. The interpretation sections below the verbatim block
are agent-authored synthesis but stay close to the operator's
language; if any phrasing drifts, the verbatim block is the binding
source of truth.

Per AGENTS.md Hard Rule #3 (verbatim log BEFORE acting) + CLAUDE.md
Hard Rule #4 (operator words sacrosanct), this file lands before any
sovereign-os synthesis page that builds on Q-017/Q-018/Q-019.

## Relationships

- FEEDS INTO: `cyberpunk042/sovereign-os/docs/sdd/000-charter.md` (charter consumes the sovereignty principles + IaC bar + Debian-as-Ark)
- FEEDS INTO: `cyberpunk042/sovereign-os/docs/decisions.md` (Q-017/Q-018/Q-019 land here at PR 1)
- DERIVED FROM: [raw/notes/2026-05-16-user-directive-sovereign-os-arc-opening.md](2026-05-16-user-directive-sovereign-os-arc-opening.md) (prior session L0)
- DERIVED FROM: [raw/dumps/2026-05-16-sovereign-os-macro-arc-plan.md](../dumps/2026-05-16-sovereign-os-macro-arc-plan.md) (Plan-agent output)
- ENABLES: future synthesis pages for first-login assistant (Q-018) and lifecycle-management surface (Q-019)
- ENABLES: future L3 comparison `wiki/comparisons/cmp-inference-backend-stack.md` (Q-017 evaluation; once SDD ready)
- RELATES TO: `cyberpunk042/devops-expert-local-ai` (AICP — its 5-backend router is one reference for Q-017's evaluation; AICP's MCP / agent-server is one candidate for Q-019's integration)
