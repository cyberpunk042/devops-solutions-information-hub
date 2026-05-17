# Dump: Sovereign OS Macro-Arc Plan (Plan Agent Output, 2026-05-16)

Queued: 2026-05-16
Status: pending-execution
Origin: Plan agent invocation via Task tool (subagent_type=Plan) in selfdef session 2026-05-16
Type: dump (L0 verbatim — never synthesized in place)
Paired-directive: `raw/notes/2026-05-16-user-directive-sovereign-os-arc-opening.md`

## Provenance Note

This file contains the **verbatim** output of a Plan-agent invocation authorized by the operator's `/goal` directive on 2026-05-16. The Plan agent was commissioned with the operator's full goal text, the four locked framing decisions (new repo `sovereign-os` / research-first substrate / schema-first profiles / Plan-tool yes), and the operator's quality-bar verbatim. It returned a macro-arc plan for the FIRST 6-10 PRs in the new `cyberpunk042/sovereign-os` repo.

**This is L0 raw. Never edit content here.** The plan is the authoritative scaffold for the foundation phase of the sovereign-os arc. Synthesis + per-PR breakdown happens in selfdef-side `docs/sdd/011-sovereign-os-arc-opening.md` and the eventual `cyberpunk042/sovereign-os/docs/sdd/000-charter.md` once that repo exists.

The operator's "Debian as Ark" framing + SFIF discipline + IaC quality bar arrived AFTER the Plan agent returned and are captured in the paired directive log. Future agents reading this dump should also read the directive log to understand the post-Plan refinements the operator added.

## Plan Agent Output (verbatim)

# Macro-Arc Plan: `cyberpunk042/sovereign-os` — First 6-10 PRs

## Macro-Arc Summary

The `sovereign-os` repo's first 6-10 PRs deliver a **disciplined foundation for an SDD/TDD-governed OS-build pipeline** — not a working build. The arc moves deliberately from charter, through substrate research, through schema definition (profiles + whitelabel), and lands on a hardware-free test harness. At the end of PR 10, the repo can describe *what it intends to build*, *how it will be specified*, *what conformance means*, and *how a build artifact can be exercised in CI* — but it has not yet built an installable image. That is intentional: the operator's "we think before we act always" principle dictates that mechanisms are specified before scripts are written, and tests are scaffolded before mechanisms are executed.

The arc respects three parallelism axes the operator surfaced: (a) whitelabel-survey can run independent of substrate selection; (b) profile-schema design can run independent of substrate selection; (c) ~70% of work is hardware-free. This lets PRs 4-8 land without waiting for SAIN-01 hardware procurement. PRs 9-10 close out the foundation with a chroot+QEMU+systemd-nspawn test harness that supports the schema and the substrate decision retroactively.

The arc is structured to mirror the selfdef workflow conventions exactly — SDDs numbered 000-charter through 010-stage-2-stub, decisions log, audit phase directories, mdbook publishing, MCP config — so that an operator already fluent in selfdef's rhythm pays zero context-switch cost when working in `sovereign-os`. Cross-repo references (info-hub for the 11 epics, selfdef for the workflow template) are explicit citations, never duplications.

---

## Phase Decomposition

### PR 1 — Repo Genesis & Charter Stub

**Title**: `chore: bootstrap sovereign-os repo skeleton and charter stub`

**Scope**: Create the empty-repo scaffolding. No build code, no scripts. Pure structural seed.

**Deliverables**:
- `README.md` — repo purpose, relationship to selfdef + info-hub, current status ("foundation phase, no buildable artifact yet"), pointer to the 11 epics in info-hub as architectural baseline.
- `docs/sdd/000-charter.md` — stub charter naming the mission, scope boundaries (BUILDS the OS; does not RUN on it; does not SYNTHESIZE knowledge), the SDD+TDD discipline commitment, and explicit non-goals.
- `docs/decisions.md` — seeded with the operator-confirmed locked decisions (repo identity, substrate-undecided, schema-first profiles, plan-tool-yes) plus the initial open-question seed list (see section below).
- `docs/sdd/INDEX.md` — empty numbered table reserving 000-010 slots.
- `docs/handoff/INDEX.md` — empty handoff anchor table.
- `docs/review/INDEX.md` — empty audit phase table.
- `.gitignore`, `LICENSE` (match selfdef's choice), `CODEOWNERS`.

**Critical files**: `docs/sdd/000-charter.md` (~200 LOC), `README.md` (~150 LOC), `docs/decisions.md` (~120 LOC).

**LOC estimate**: ~600 total (mostly markdown).

**Dependencies**: None.

---

### PR 2 — ARCHITECTURE.md & Cross-Repo Reference Map

**Title**: `docs: add ARCHITECTURE.md referencing info-hub epics and selfdef workflow`

**Scope**: Document the architectural baseline without re-deriving it. This PR is a *reference document*, not a design.

**Deliverables**:
- `ARCHITECTURE.md` — names the 11 epics (E100-E110) by citation to `info-hub/wiki/backlog/milestones/sain-01-sovereign-node.md`, draws the three-repo boundary diagram (sovereign-os BUILDS, selfdef RUNS, info-hub SYNTHESIZES), enumerates the four lifecycle stages (pre-install, during-install, post-install, ongoing-management), and identifies the four cross-cutting concerns (profiles, whitelabel, observability, evolvability).
- `docs/sdd/001-cross-repo-boundaries.md` — substantive SDD locking the boundary contract. Defines what flows across repos and what does not. References info-hub epics by ID.
- `docs/handoff/001-architecture-baseline.md` — handoff anchor capturing the architectural assumptions at this checkpoint.

**Critical files**: `ARCHITECTURE.md` (~400 LOC), `docs/sdd/001-cross-repo-boundaries.md` (~350 LOC).

**LOC estimate**: ~900.

**Dependencies**: PR 1 merged.

---

### PR 3 — mdbook Layout & MCP Config Template

**Title**: `docs: scaffold mdbook publishing pipeline and MCP config template`

**Scope**: Wire up the documentation publishing infrastructure that selfdef uses, plus an MCP config template so that future automation has a known seat.

**Deliverables**:
- `docs/src/SUMMARY.md` — mdbook navigation seeded with charter, architecture, SDD index, decisions, handoff.
- `docs/src/` directory tree mirroring `docs/sdd/`, `docs/handoff/`, `docs/review/`.
- `book.toml` — mdbook configuration mirroring selfdef's settings.
- `.github/workflows/mdbook-publish.yml` — CI workflow for publishing (same pattern as selfdef).
- `.mcp/config.template.json` — MCP server config template (placeholders for the operator's actual MCP setup).
- `docs/sdd/002-documentation-pipeline.md` — SDD documenting the publishing contract.

**Critical files**: `docs/src/SUMMARY.md`, `book.toml`, `.github/workflows/mdbook-publish.yml`, `docs/sdd/002-documentation-pipeline.md` (~250 LOC).

**LOC estimate**: ~500.

**Dependencies**: PR 2 merged.

**Stage Gate 1**: Operator reviews PRs 1-3 holistically. Confirms structural foundation matches selfdef rhythm. Authorizes the substantive-SDD phase to begin.

---

### PR 4 — Substrate Survey SDD (the research PR)

**Title**: `sdd: 003 substrate survey and image-build tooling selection`

**Scope**: Research-only SDD. Surveys image-build substrates against a documented criteria matrix and emits a recommendation with rationale. No code.

**Deliverables**:
- `docs/sdd/003-substrate-survey.md` — the survey document. Sections:
  1. **Candidates surveyed**: live-build (Debian native), mkosi (systemd ecosystem), debootstrap (low-level), Lorax (Fedora/Anaconda), Kiwi (SUSE), ostree (image-based atomic), Nix/NixOS-style declarative, Buildroot (embedded reference for contrast).
  2. **Criteria matrix** — dimensions: Debian-13 native support, declarative-vs-imperative, profile/variant pluralism, whitelabel surface accessibility, reproducibility, CI testability without hardware, ZFS-root support, secure-boot support, community + longevity, operator-familiarity cost, lifecycle-tool surface (does substrate help post-install management or only build?), evolvability (can we swap substrates in 2 years?).
  3. **Per-candidate analysis** — each candidate scored against each criterion with prose justification (not just a number).
  4. **Recommendation** — single recommended substrate OR A/B/C ranked options with the conditions under which each wins. Operator chooses, not the SDD.
  5. **Reversal cost** — for the recommended substrate, what does it cost to swap later? (Evolvability principle.)
- `docs/decisions.md` — updated with the substrate-decision question elevated to "pending operator review" status.

**Critical files**: `docs/sdd/003-substrate-survey.md` (~1200 LOC — this is a heavy research doc).

**LOC estimate**: ~1300.

**Dependencies**: PR 3 merged. **Can run in parallel with PR 5 and PR 7.**

**Stage Gate 2**: Operator reviews PR 4 in isolation. Picks substrate (or asks for deeper dive on top 2). The decision is recorded in `docs/decisions.md`. No code-bearing PR proceeds until substrate is locked.

---

### PR 5 — Profile Schema SDD

**Title**: `sdd: 004 profile schema design`

**Scope**: Schema-first profile definition. Defines the shape of a profile before any profile body exists.

**Deliverables**:
- `docs/sdd/004-profile-schema.md` — schema specification covering dimensions:
  - **Identity**: name, id, version, parent (inheritance graph), status (draft/active/deprecated).
  - **Hardware target**: CPU architecture, CPU features required/preferred (AVX-512, SHA-NI, etc.), GPU model + count + role (primary/VFIO-isolated/headless), memory minimum, storage layout intent, network interface expectations.
  - **Kernel config**: kernel flavor, required modules, blacklisted modules, cmdline parameters, microcode.
  - **Package sets**: layered — base, role-specific, profile-specific, with explicit "deny" lists.
  - **Activation hooks**: pre-install, during-install, post-install-first-boot, post-install-recurrent, decommission. Each phase declarable per-profile.
  - **Lifecycle metadata**: maintainer, evolution policy (frozen / append-only / replaceable), supported substrate version range.
  - **Whitelabel binding**: which whitelabel profile applies (forward reference to PR 7).
  - **Observability binding**: telemetry tier, log retention, audit hooks.
- Schema rendered as both prose and a formal JSON Schema / YAML schema document (`schemas/profile.schema.yaml` — schema only, no instances yet).
- Trade-off section: inheritance vs composition; rigid vs extensible schema; YAML vs TOML vs HCL.

**Critical files**: `docs/sdd/004-profile-schema.md` (~700 LOC), `schemas/profile.schema.yaml` (~250 LOC).

**LOC estimate**: ~1000.

**Dependencies**: PR 3 merged. **Parallel with PR 4 and PR 7.**

---

### PR 6 — SAIN-01 & old-workstation Profile Stubs (Schema-Conformant)

**Title**: `profiles: declare sain-01 and old-workstation as schema-conformant stubs`

**Scope**: First two profile instances. Bodies are *placeholder* but schema-conformant. Validates the schema against real targets.

**Deliverables**:
- `profiles/sain-01.yaml` — SAIN-01 AI Workstation profile. Hardware target fully specified (Ryzen 9 9900X, RTX PRO 6000 + RTX 3090 VFIO, 256 GB DDR5, dual PCIe 5 NVMe ZFS RAID 0, Marvell 10GbE + Intel 2.5GbE, ASUS ProArt X870E-Creator). Kernel/packages/hooks intentionally minimal — placeholder pointers to future PRs.
- `profiles/old-workstation.yaml` — older hardware (11 GB RAM, 8 GB GPU). Hardware target specified to the extent the operator has supplied. Body otherwise minimal.
- `profiles/INDEX.md` — catalog of declared profiles with status.
- `docs/sdd/005-initial-profiles.md` — SDD justifying these two as the seed set; reserves `minimal`, `developer`, `headless` as future profiles with rationale for *not* declaring them yet.
- Validation harness stub: `scripts/validate-profiles.sh` (or equivalent — concrete language deferred to substrate decision) that lints profile files against the schema. **This is the first test-bearing artifact.**

**Critical files**: `profiles/sain-01.yaml` (~200 LOC), `profiles/old-workstation.yaml` (~100 LOC), `docs/sdd/005-initial-profiles.md` (~300 LOC), `scripts/validate-profiles.sh` (~80 LOC).

**LOC estimate**: ~700.

**Dependencies**: PR 5 merged.

**Stage Gate 3**: Operator reviews schema + two instances together. Schema may be revised once instances reveal gaps. Lock-in moment for profile shape.

---

### PR 7 — Whitelabel Audit SDD

**Title**: `sdd: 006 debian surface audit and whitelabel target inventory`

**Scope**: Survey/audit only. Identifies every place "Debian" surfaces in a default Debian 13 system. No rebranding mechanism yet.

**Deliverables**:
- `docs/sdd/006-debian-surface-audit.md` — exhaustive inventory:
  - **Filesystem surfaces**: `/etc/issue`, `/etc/issue.net`, `/etc/os-release`, `/etc/lsb-release`, `/etc/debian_version`, `/etc/motd`, `/usr/lib/os-release`.
  - **Package-manager surfaces**: DPKG vendor strings, APT sources headers, `dpkg-vendor` output, `lsb_release` output.
  - **Boot surfaces**: GRUB theme + menu entries, Plymouth boot splash, kernel boot logo, systemd boot banner.
  - **Installer surfaces**: debian-installer branding (if applicable per substrate decision), Calamares branding (if applicable), preseed banner text.
  - **Desktop surfaces**: GDM/SDDM/LightDM theming, default wallpaper, GNOME/KDE about-system dialogs.
  - **Kernel surfaces**: `/proc/version` string (compile-time), uname-a fields, kernel package naming.
  - **Documentation surfaces**: man pages referencing Debian, /usr/share/doc/, default README files.
  - **Network surfaces**: default hostname pattern, NTP/DNS pool references, default APT mirror.
  - **Telemetry surfaces**: popcon, apport, any phone-home defaults.
- Each surface categorized: **must-rebrand**, **should-rebrand**, **may-leave**, **must-not-touch** (legal/license obligations — Debian trademark, GPL attribution, etc.).
- Legal-obligation section: what Debian's trademark and DFSG require even of whitelabel derivatives. Citation-grade.

**Critical files**: `docs/sdd/006-debian-surface-audit.md` (~900 LOC).

**LOC estimate**: ~950.

**Dependencies**: PR 3 merged. **Parallel with PR 4 and PR 5.**

---

### PR 8 — Whitelabel Mechanism SDD

**Title**: `sdd: 007 whitelabel mechanism specification`

**Scope**: How rebranding is applied — declaratively, per-profile, evolvable.

**Deliverables**:
- `docs/sdd/007-whitelabel-mechanism.md`:
  - **Mechanism shape**: declarative whitelabel-profile YAML referenced by main profiles; rendering engine consumes whitelabel profile + targets it to surfaces from PR 7.
  - **Per-surface strategy**: template-substitution vs file-overlay vs package-replacement vs build-time-flag. Pick one strategy per surface category with justification.
  - **Pre/during/post split**: which surfaces are pre-build patches, which are install-time substitutions, which are first-boot scripts.
  - **Evolvability**: how a whitelabel can be swapped without re-building the entire image (where possible).
  - **Legal compliance binding**: enforce the "must-not-touch" list from PR 7 at validation time.
- `schemas/whitelabel.schema.yaml` — formal schema.
- `whitelabel/default.yaml` — placeholder default whitelabel (no actual brand committed; operator decides brand name later).
- `whitelabel/INDEX.md`.

**Critical files**: `docs/sdd/007-whitelabel-mechanism.md` (~600 LOC), `schemas/whitelabel.schema.yaml` (~200 LOC).

**LOC estimate**: ~900.

**Dependencies**: PR 7 merged. Substrate decision (PR 4) helpful but not strictly blocking — schema can be substrate-agnostic.

**Stage Gate 4**: Operator reviews whitelabel audit + mechanism together. Confirms legal posture. Optionally supplies the actual brand identity (name, palette, logo) — or defers brand commit to a later PR.

---

### PR 9 — TDD Harness SDD

**Title**: `sdd: 008 test harness specification for hardware-free validation`

**Scope**: Specify how an image-build pipeline gets unit-, stage-, and integration-tested without hardware.

**Deliverables**:
- `docs/sdd/008-test-harness.md`:
  - **Test layers**:
    1. **Schema/lint tests** — profile + whitelabel YAML validate against schemas. Pure CI. No virtualization.
    2. **Unit tests** — individual build scripts tested in isolation (mocked filesystem, mocked apt, mocked dpkg).
    3. **Stage acceptance tests** — each lifecycle stage (pre-install, during-install, post-install-first-boot) tested in a controlled environment.
    4. **Integration tests** — full image built and booted in QEMU; smoke tests inside the booted system.
    5. **Hardware-conformance tests** — gated tests that only run when matching hardware is present (SAIN-01 hardware, when procured).
  - **Virtualization stack**:
    - **chroot** — fastest, for package-level assertions (does package X get installed; is file Y present with content Z).
    - **systemd-nspawn** — for service-startup assertions (does systemd unit start, does it converge).
    - **QEMU (system)** — for boot + initramfs + GRUB + kernel-cmdline assertions; supports UEFI + secure-boot testing; supports PCIe passthrough emulation for VFIO-profile smoke tests (limited).
    - **qemu-user** — for cross-arch validation if profiles ever target non-amd64.
  - **Invariants per stage** — explicit per-stage assertions (e.g., post-install-first-boot invariant: hostname matches profile, whitelabel surfaces match whitelabel profile, ZFS pool present and healthy, expected systemd units active).
  - **Test discovery + naming convention**, **CI execution model**, **flake policy**.
- `tests/INDEX.md`, `tests/README.md`.

**Critical files**: `docs/sdd/008-test-harness.md` (~800 LOC).

**LOC estimate**: ~850.

**Dependencies**: PR 4 merged (substrate informs harness choices) AND PR 6 merged (profiles inform what's being tested) AND PR 8 merged (whitelabel informs assertions).

---

### PR 10 — TDD Harness Scaffold + First Passing Tests

**Title**: `test: scaffold test harness and land first lifecycle-invariant tests`

**Scope**: First executable test code. Validates the harness works end-to-end on the only artifacts that exist (profile YAMLs, whitelabel YAMLs, schemas).

**Deliverables**:
- `tests/schema/` — profile + whitelabel schema-conformance tests. Wired into CI.
- `tests/lint/` — markdown lint, decisions-log linter, SDD index consistency checker.
- `tests/chroot/scaffold.sh` — chroot harness skeleton (substrate-aware; calls into substrate's tooling per PR 4 decision).
- `tests/nspawn/scaffold.sh` — systemd-nspawn harness skeleton.
- `tests/qemu/scaffold.sh` — QEMU harness skeleton with stubbed-out boot test that runs a minimal image.
- `.github/workflows/test.yml` — CI workflow running schema + lint tests on every PR; chroot/nspawn/QEMU tests on merge to main or label-trigger.
- `docs/sdd/009-test-harness-bootstrap.md` — SDD documenting what the scaffold delivers and what it explicitly does *not* (no image yet — substrate-execution code lands in subsequent PRs beyond this 10-PR arc).
- `docs/sdd/010-stage-2-stub.md` — placeholder for Stage 2 work (mirroring selfdef's 010 stub pattern), reserving the slot for the first actual build-script PR.

**Critical files**: `tests/schema/`, `tests/qemu/scaffold.sh`, `.github/workflows/test.yml`, `docs/sdd/009-test-harness-bootstrap.md` (~400 LOC).

**LOC estimate**: ~1200 (mix of test code + SDD + CI YAML).

**Dependencies**: PR 9 merged.

**Stage Gate 5 (foundation-complete gate)**: Operator reviews the full 10-PR arc holistically. The foundation is now in place: charter set, substrate chosen, profile schema locked with two conformant instances, whitelabel mechanism specified, hardware-free test harness operational. The next arc (Stage 2 — actual build scripts) is authorized only after this gate.

---

## Critical-Decisions Surface (Questions for Operator Before Each Phase)

**Before PR 1**: Repo visibility (public/private)? License choice (match selfdef)? Default branch name (main)?

**Before PR 2**: Should ARCHITECTURE.md duplicate any info-hub content for offline readability, or strictly reference? (Recommendation: reference, do not duplicate.)

**Before PR 4**: Are there substrates the operator wants *excluded* from the survey (e.g., excludes Nix on familiarity-cost grounds)? Any operator-known prior research to incorporate?

**Before PR 5**: Inheritance model preference — single-parent inheritance, multiple-inheritance, or composition-only? Schema format — YAML, TOML, or HCL? (Survey supplies trade-offs; operator decides.)

**Before PR 6**: Has the operator confirmed the SAIN-01 hardware spec is final, or might it shift before procurement? (Affects whether the placeholder profile is treated as authoritative.)

**Before PR 7**: Legal scope — is the operator pursuing a publicly-distributed branded derivative (high legal bar) or private/internal use (lower bar)?

**Before PR 8**: Brand identity — committed now, or deferred? (Mechanism can land without brand committed; brand can fill in later.)

**Before PR 9**: Is hardware-conformance test gating acceptable, or does the operator want full hardware tests run quarterly on borrowed hardware until SAIN-01 is procured?

**Before PR 10**: Any CI-runner constraints? Does QEMU-system require dedicated runners (KVM-enabled) or is emulation acceptable for the foundation phase?

---

## Trade-Off Analysis Table

| Decision | Option A | Option B | Trade-off |
|---|---|---|---|
| Substrate decisiveness in PR 4 | Single recommendation | Ranked A/B/C with operator pick | A removes a decision from the operator but risks committing to wrong tool; B respects "we think before we act" but extends Stage Gate 2. Recommendation: B. |
| Profile inheritance | Single-parent inheritance | Composition (mixins) | Single-parent is simpler to validate and easier to reason about; composition is more powerful for cross-cutting concerns (whitelabel, observability tier). Recommendation: surface in PR 5 SDD; operator picks. |
| Schema format | YAML | TOML / HCL | YAML matches selfdef + info-hub conventions but has anchor/merge ambiguity; TOML is stricter but less expressive for nested structures; HCL is most expressive but adds a foreign toolchain. Recommendation: YAML for ecosystem alignment. |
| Whitelabel strategy | Build-time patching | Runtime overlay | Build-time bakes in (simpler, immutable, slower iteration); runtime overlay enables late binding and easier brand-swap but adds boot-time complexity. Recommendation: hybrid per surface — most surfaces build-time, MOTD/issue/dynamic surfaces runtime. PR 8 SDD enumerates. |
| Test harness scope at PR 10 | Schema+lint only | Schema+lint+nspawn+QEMU stubs | Narrow scope ships faster but defers harness-correctness validation; broad scope validates the whole concept. Recommendation: broad — operator's quality bar demands proof the harness works before Stage 2 begins. |
| Hardware-gated tests | Skip until hardware | Mock hardware paths | Skipping is honest; mocking risks silently passing tests that wouldn't pass on real hardware. Recommendation: skip + clearly mark, never mock hardware-specific paths. |
| Cross-repo references | Hard-pin commits | Symbolic references | Hard-pinning makes references reproducible but stale; symbolic references stay fresh but break. Recommendation: symbolic + a CI check that the referenced docs exist. |
| MCP config in PR 3 | Real config | Template only | Real config leaks operator's MCP setup; template defers but requires operator setup-step. Recommendation: template only. |

---

## Stage-Gate Placement

- **Stage Gate 1** — after PR 3. Structural foundation review. Operator confirms repo rhythm matches selfdef.
- **Stage Gate 2** — after PR 4. Substrate decision. Operator picks tooling.
- **Stage Gate 3** — after PR 6. Schema lock-in. Schema may be revised once instances reveal gaps; locked thereafter.
- **Stage Gate 4** — after PR 8. Whitelabel mechanism + legal posture confirmed.
- **Stage Gate 5** — after PR 10. Foundation-complete gate. Authorizes Stage 2 (first actual build scripts).

Each gate is an `ExitPlanMode`-style checkpoint where execution pauses, operator reviews, and explicitly authorizes the next phase. No PR opens past a gate without operator sign-off.

---

## TDD Discipline Scope

"Test Driven" for an image-build pipeline means:

1. **Schema tests first** — schemas exist before profile bodies; profile bodies must validate.
2. **Invariant tests per lifecycle stage** — each of pre-install, during-install, post-install-first-boot, post-install-recurrent has a declarative set of invariants (assertions about filesystem state, service state, network state, whitelabel surface conformance). These invariants are *authored before* the scripts that satisfy them.
3. **Stage acceptance tests** — a stage is "done" when invariants pass in nspawn/chroot/QEMU. Stage acceptance is the unit of progress, not script-by-script.
4. **End-to-end image boot validation** — for each profile, the final integration test boots the produced image in QEMU and runs a smoke-test suite inside the booted system.
5. **Hardware-conformance suite** — gated tests run only when matching hardware is detected. Authored alongside scripts but never block CI on missing hardware.

Tests live under `tests/` with subdirectories matching test layer (`tests/schema/`, `tests/unit/`, `tests/stage/`, `tests/integration/`, `tests/hardware/`).

---

## Open-Question Seed List (for `docs/decisions.md` Initial Seeding)

1. **Q-001**: Final substrate selection (pending PR 4 SDD + Stage Gate 2).
2. **Q-002**: Profile inheritance model — single-parent vs composition (pending PR 5).
3. **Q-003**: Whitelabel brand identity — name, palette, logo assets (deferrable past PR 8).
4. **Q-004**: Legal scope of whitelabel — public distribution vs internal use (gates legal-obligation strictness in PR 7).
5. **Q-005**: ZFS root layout details — pool topology, dataset hierarchy, encryption choice (deferrable; surfaces in Stage 2).
6. **Q-006**: Secure-boot posture — own keys, Microsoft-signed shim, or disabled (Stage 2).
7. **Q-007**: Kernel choice — Debian stock, custom-compiled with AVX-512 tuning, or xanmod/liquorix (Stage 2).
8. **Q-008**: Installer experience — debian-installer derivative, Calamares, custom TUI, or no-installer (image-only) (Stage 2, but substrate decision constrains).
9. **Q-009**: Hardware procurement timeline for SAIN-01 — affects when hardware-gated tests come online.
10. **Q-010**: CI infrastructure — GitHub Actions runners or self-hosted (affects QEMU/KVM availability).
11. **Q-011**: How the three repos cross-reference at commit-pin level — symbolic, hard-pinned, or hybrid.
12. **Q-012**: Future-profile timeline — when do `minimal`, `developer`, `headless` get bodies?
13. **Q-013**: Observability binding details — which telemetry sink, what retention, what audit log shape (Stage 2+).
14. **Q-014**: Decommission/wipe profile — does the schema's decommission hook get exercised in foundation phase or deferred?
15. **Q-015**: Reproducibility target — bit-for-bit reproducible builds, or content-equivalent? (Substrate-dependent.)

---

## Notes on What This Plan Explicitly Does NOT Decide

- It does not pick the substrate (PR 4 surfaces; operator decides).
- It does not pick the brand identity (deferrable).
- It does not author any build scripts (Stage 2).
- It does not commit ZFS layout, secure-boot posture, or kernel choice (Stage 2).
- It does not block on hardware for any of PRs 1-10.
- It does not duplicate the 11 epics from info-hub — references them as the architectural baseline.

---

### Critical Files for Implementation

- /home/user/sovereign-os/docs/sdd/000-charter.md
- /home/user/sovereign-os/docs/sdd/003-substrate-survey.md
- /home/user/sovereign-os/docs/sdd/004-profile-schema.md
- /home/user/sovereign-os/docs/sdd/007-whitelabel-mechanism.md
- /home/user/sovereign-os/docs/sdd/008-test-harness.md

## Post-Plan Operator Refinements (captured in the paired directive log)

The operator's 2026-05-16 message AFTER the Plan agent returned added:

1. **SFIF discipline**: the arc itself follows Scaffold → Foundation → Infrastructure → Features. PRs 1-3 = Scaffold; PRs 4-8 = Foundation; PRs 9-10 begin Infrastructure (TDD harness); Stage 2 onwards delivers Infrastructure + Features.

2. **IaC quality bar**: every PR must deliver high-quality scripts + libs + configuration + easily tweakable + customisable + env-var-driven + restart-from-state. Build pipeline is resumable + observable, not one-shot.

3. **"Debian as Ark" framing**: Debian 13 is the starting boat, not the destination. The substrate survey (PR 4) must include **Q-016 — distro-base reconsideration**: would switching from Debian 13 to another base unlock material new potential that we'd lose by staying? Working hypothesis: stay on Debian + customize the boat. Alternatives evaluated honestly; trade-offs documented either way.

4. **Q-016 added to seed list**: substrate-base reconsideration. Stays open through PR 4 survey; resolved at Stage Gate 2 alongside Q-001 (substrate tooling).

5. **Handoff mandate**: operator-side action required (create repo + expand MCP scope) needs a new session. This session prepares ALL the cold-start knowledge transfer first.

## End of Dump

This file is preserved verbatim per the operator's quality bar ("Do not minimize, do not reduze, do not conflate, do not hack or try to take shortcuts"). The post-Plan refinements (SFIF / IaC / Debian-as-Ark / Q-016 / handoff mandate) are documented in the paired directive log; readers should consult both for the full picture.
