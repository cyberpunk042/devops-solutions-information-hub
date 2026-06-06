---
title: "Operator runbook — UX coherence harness failures"
type: reference
domain: ai-agents
layer: 2
status: draft
confidence: high
maturity: seed
created: 2026-05-20
updated: 2026-05-20
sources:
  - id: selfdef-sdd-030
    type: internal
    project: selfdef
    path: docs/sdd/030-ux-coherence-test-harness.md
    note: "SDD-030 UX coherence test harness specification"
  - id: selfdef-ms045
    type: internal
    project: selfdef
    path: backlog/milestones/MS045-ux-coherence-test-harness-cli-tui-minimal-web.md
    note: "Catalog milestone MS045"
  - id: operator-directive-2026-05-19
    type: directive
    project: devops-solutions-information-hub
    path: wiki/log/
    note: "Standing direction — be an architect first, then a DevOps + Fullstack + UX Design Specialist"
tags: [runbook, ux-coherence, tdd, ci, test-harness, sdd, selfdef, ips]
---

# Operator runbook — UX coherence harness failures

## When to use this

`bash scripts/test/coherence.sh` (or `make coherence` once wired) exited non-zero. The summary block names which layer failed; this runbook walks the operator from "summary line says FAIL" to "root cause + fix".

## Layer-by-layer triage

### L1: perimeter YAML lint

**What it checks:** `packaging/tetragon-policies/sovereign-perimeter.yaml` matches the verbatim sain-01 §6 structure (kind, metadata.name, kprobe call/syscall/args/operator/values/action).

**Common failure → fix:**

| Diagnostic | Cause | Fix |
|---|---|---|
| `apiVersion drift` | Someone changed apiVersion | Restore `cilium.io/v1alpha1` |
| `metadata.name drift` | Renamed from `sovereign-kernel-fence` | Restore verbatim |
| `DEFAULT ALLOWLIST DRIFT from sain-01 §6 verbatim` | Allowlist edited in place | Restore the 4-entry verbatim set (python3 / nvidia-smi / vllm / podman). Extensions go via `selfdefctl perimeter extend`, NOT the YAML. |
| YAML parse error | Hand-edit broke syntax | Restore from `/usr/share/selfdef/sovereign-perimeter.yaml` (package copy) |

See: [perimeter-policy-load-failure](perimeter-policy-load-failure.md).

### L1: CLI surface (subverb counts)

**What it checks:** `selfdefctl <command> --help` lists the expected subverb count per SDD.

Current baseline (locked):

| Command | Count | SDD |
|---|---|---|
| `friction-audit` | 3 | SDD-027 |
| `perimeter` | 7 | SDD-028 |
| `guardian` | 4 | SDD-029 |

**Common failure → fix:**

- **Drift down (subverb removed)**: the SDD said N subverbs; the binary lists N-1. Either restore the missing subverb OR update SDD-030 to reflect the intentional removal (operator approval required — this is a UX contract change).
- **Drift up (subverb added)**: new feature shipped but the harness baseline wasn't bumped. Update the expected count in `scripts/test/L1-cli-surface.sh` to match, ensure the new subverb is SDD-documented (SDD-027/028/029 amendment).
- **Binary not built**: `cargo build -p selfdef-cli` first.

### L1: HTTP API endpoint declarations

**What it checks:** `crates/selfdef-api/src/lib.rs` declares the 6 SDD-promised routes (`/v1/{friction-audit,perimeter,guardian}` + `/history` for each).

**Common failure → fix:**

- **Route missing**: someone removed the `.route(...)` line. Restore.
- **Route refactored**: route was renamed (e.g. `/v1/perimeter` → `/v1/sovereign-perimeter`). Decision required: rename back, OR coordinate the rename across the SDD + this gate + the cockpit panel binding paths. (Renaming an API route is a public-contract change; operator approval required.)

### L2: L2-friction-audit / L2-perimeter / L2-guardian (bats)

**What it checks:** systemd unit hardening, postinst/postrm wiring, YAML / file structural shape.

**Common failure → fix:**

- **Specific R-row failing**: each bats test names the R-row it's anchored to. Look up the R-row in the relevant catalog (`backlog/milestones/MS04{4,6,7}-*.md`) for the binding contract.
- **`bats not installed`**: install via `apt install bats` (Debian/Ubuntu) or `brew install bats-core` (macOS).
- **Unit file missing**: postinst/postrm references a path that the cargo-deb assets didn't ship; check `crates/selfdef-daemon/Cargo.toml` `[package.metadata.deb] assets` block.

### cargo: three-watchdog-trio unit suites

**What it checks:** the ~127 unit tests across the 6 trio crates + the API crate pass.

**Common failure → fix:**

- **One test failing**: read the failure output; cargo identifies the specific `test foo::bar::baz ... FAILED` and prints the assertion. Most failures here are real logic bugs — fix the code, not the test.
- **Compile error**: a dependency contract changed (e.g. `selfdef-perimeter-mirror::Outcome` field added). Cascade the change.
- **Cargo not installed / wrong toolchain**: install rustup, set `rust-version.workspace = true` toolchain.

## When the harness itself is broken

The harness scripts are themselves operator-trusted. If you suspect drift in the harness:

```bash
shellcheck scripts/test/coherence.sh scripts/test/L1-*.sh
```

ShellCheck violations indicate a regression in the harness shell layer.

## Long-term posture

Per the operator standing direction *"be an architect first, then a DevOps Software Engineer and Fullstack and UX Design Specialist"*, this harness IS the DevOps Engineer projection enforcing the Architect's UX promises. When the harness fails, the right reflex is: **the SDD said X, the binary now does Y — which one is the operator's intent?** Then bring the deviant side back into line.

Never silently update the harness baseline to match a drifted binary. Always update the binary OR the SDD (with operator approval), THEN the baseline.

## Relationships

### Cross-references

- SDD-030 UX coherence test harness specification (selfdef `docs/sdd/030-ux-coherence-test-harness.md`)
- MS045 catalog (`backlog/milestones/MS045-ux-coherence-test-harness-cli-tui-minimal-web.md`)
- Sister runbook: [perimeter-policy-load-failure](perimeter-policy-load-failure.md) (L1 yaml-lint upstream)
- Three-watchdog-trio runbooks: `friction-audit-*`, `perimeter-*`, `guardian-*` in this directory
