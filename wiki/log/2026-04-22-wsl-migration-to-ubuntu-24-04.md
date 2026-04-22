---
title: "WSL Migration — Ubuntu 20.04 → Ubuntu 24.04 for K2.6 + ML Toolchain"
type: note
domain: cross-domain
note_type: completion
status: synthesized
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e008-m001-ktransformers-install-and-config
    type: wiki
    file: wiki/backlog/modules/e008-m001-ktransformers-install-and-config.md
  - id: e010-m002-dev-sdd-mount-procedure
    type: wiki
    file: wiki/backlog/modules/e010-m002-dev-sdd-mount-procedure.md
  - id: vhdx-attach-fix
    type: wiki
    file: wiki/log/2026-04-23-vhdx-attach-procedure-and-hcs-fix.md
tags: [note, completion, e008, e010, wsl, ubuntu-20-04, ubuntu-24-04, migration, glibc, ktransformers, decision, handoff]
---

# WSL Migration — Ubuntu 20.04 → Ubuntu 24.04

## Summary

Migrated the operator's primary WSL ML workstation from Ubuntu 20.04 to Ubuntu 24.04 on 2026-04-22 after hitting eight Ubuntu-20.04-age blockers in one session attempting a prebuilt + from-source install of ktransformers. The root cause was structural: modern ML wheels (ktransformers 0.5.2, its `kt_kernel` extension) are built against GLIBC 2.32+, libstdc++ ≥11, and C++20. Ubuntu 20.04 (focal) ships GLIBC 2.31, gcc-9, libstdc++-9. The patch cost was mounting faster than the prebuilt-wheel savings. Ubuntu 24.04 (noble) ships GLIBC 2.39 + gcc-13 + libstdc++-13 — prebuilt ML wheels just work.

## The 8 blockers we hit on Ubuntu 20.04

In order:

1. **CUDA toolkit not in WSL** — only NVIDIA driver passed through. Installed via `cuda-keyring` repo + `cuda-toolkit-12-4`.
2. **libhwloc.so.15 missing** (kt_kernel runtime dep) — `sudo apt install libhwloc15`.
3. **GLIBCXX_3.4.29 not found** — Ubuntu 20.04 ships libstdc++-9 (GLIBCXX 3.4.28). Fixed via `ubuntu-toolchain-r/test` PPA + newer libstdc++6.
4. **GLIBC_2.32 not found** — structural: GLIBC is tied to the OS. **Cannot be patched on 20.04.** This was the forcing function for migration.
5. **pip missing in uv-managed venv** — `python -m ensurepip --upgrade`.
6. **setuptools 82 vs torch 2.11 conflict** — `pip install 'setuptools<82'`.
7. **cpptrace system library missing** (from-source build) — clone + `cmake --install`.
8. **`<barrier>` C++20 header missing** — Ubuntu 20.04 default g++ is g++-9, no C++20. Needs g++-11+.

Each fix was local and tractable, but cumulatively they signaled the project was built for a post-20.04 OS. Rather than keep papering over, migrated.

## What we preserved across the migration

- **/mnt/models** — 318 GB of K2.6 Q2 weights. Lives on `D:\vdisks\models.vhdx` attached via `wsl --mount --vhd`. Same VHDX re-attaches cleanly to the new distro.
- **Hardware state** — 64 GB RAM + .wslconfig (48 GB WSL cap) applies to the VM, not a distro. All distros inherit.
- **The wiki** — repo can be re-cloned fresh, all content preserved.
- **AICP code + pyproject.toml** — repo re-cloned; venv recreated via `uv sync`.
- **Memory files** — at `~/.claude/projects/-home-jfortin-devops-solutions-research-wiki/memory/`, persist in Claude's sandbox.
- **ACL fix on the VHDX** — `takeown` + `icacls` were applied previously; file ownership is preserved across the migration.

## Migration procedure — what we ran

### Phase 1 — safety check on 20.04

```bash
for d in /home/jfortin/devops-solutions-research-wiki /home/jfortin/devops-expert-local-ai [...]; do
  git -C "$d" status -s
  git -C "$d" log --oneline @{u}..HEAD
done
```

### Phase 2 — install new distro via import (to D:\ not C:\)

```powershell
# Windows PS admin
mkdir D:\wsl\ubuntu-24.04 -Force
Invoke-WebRequest -Uri https://cloud-images.ubuntu.com/wsl/noble/current/ubuntu-noble-wsl-amd64-wsl.rootfs.tar.gz `
  -OutFile D:\wsl\ubuntu-noble.tar.gz
wsl --import Ubuntu-24.04 D:\wsl\ubuntu-24.04 D:\wsl\ubuntu-noble.tar.gz --version 2
```

### Phase 3 — detach models VHDX from 20.04, attach to 24.04

```powershell
wsl --unmount D:\vdisks\models.vhdx
wsl --mount --vhd "D:\vdisks\models.vhdx" --bare
# NOTE: do NOT use -d <distro> — wsl --mount attaches at VM level, all distros see it
```

Inside Ubuntu-24.04 the VHDX appeared as `/dev/sde` (device letter may vary). Mounted at `/mnt/models`.

### Phase 4 — user setup in 24.04

Noble's cloud rootfs pre-ships `ubuntu` user at UID 1000. Renamed in-place:

```bash
usermod -l jfortin -d /home/jfortin -m ubuntu
groupmod -n jfortin ubuntu
usermod -aG sudo jfortin
echo 'jfortin ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/jfortin
chmod 440 /etc/sudoers.d/jfortin
passwd jfortin
```

### Phase 5 — /etc/wsl.conf default user + systemd

```ini
[user]
default=jfortin

[boot]
systemd=true
```

Then `wsl --shutdown` + re-enter.

### Phase 6 — /mnt/models re-attach persistence

`wsl --mount --vhd` does NOT persist across `wsl --shutdown`. Two mechanisms combined:

1. **Windows Task Scheduler** runs a wrapper script on logon:
   ```powershell
   # C:\ProgramData\wsl-scripts\mount-models.ps1
   wsl --mount --vhd "D:\vdisks\models.vhdx" --bare
   Start-Sleep -Seconds 3
   wsl -d Ubuntu-24.04 -u root -- mount -a
   ```
2. **fstab entry** in 24.04 at `/etc/fstab`:
   ```
   UUID=<sdd-uuid> /mnt/models ext4 defaults,nofail,x-systemd.device-timeout=10s 0 2
   ```

After Windows logon: scheduled task attaches VHDX → triggers `mount -a` inside 24.04 → fstab picks up UUID → /mnt/models live.

## Current state (at migration close)

| Component | Status |
|-----------|--------|
| Ubuntu-24.04 distro | ✓ imported to `D:\wsl\ubuntu-24.04` |
| jfortin user, sudo, default | ✓ done |
| /mnt/models attached + mounted | ✓ (via scheduled task + fstab) |
| K2.6 Q2 weights on /mnt/models | ✓ 318 GB, 8 shards, SHA256-verified |
| wsl.conf (systemd, default user) | ✓ done |
| CUDA toolkit on 24.04 | pending (next step) |
| AICP repo cloned on 24.04 | pending |
| ktransformers reinstall | pending — expected to "just work" with GLIBC 2.39 |
| Wiki repo cloned on 24.04 | pending |

## What Ubuntu 20.04 still holds (reference — can be decommissioned after 24.04 is proven)

- The wiki repo (this repo) — re-clone to 24.04 to continue working.
- `devops-expert-local-ai` repo — re-clone to 24.04.
- Other project repos (openfleet, continuity-orchestrator, etc.) — migrate as needed.
- The Ubuntu-20.04 WSL VHDX itself — can be compacted (`Optimize-VHD`) or eventually unregistered if not needed.

Plan: keep 20.04 around until 24.04 setup is complete and verified; then optionally unregister to reclaim VHDX space.

## Cross-reference

The detailed "how to attach a fresh VHDX to WSL with correct ACLs" procedure remains in [[2026-04-23-vhdx-attach-procedure-and-hcs-fix|2026-04-23-vhdx-attach-procedure-and-hcs-fix]] — still the authoritative attach reference.

The storage tiering reference [[operator-workstation-storage-tiering|operator-workstation-storage-tiering]] now reflects the correct ground truth (D:\ = NVMe).

## Lessons

1. **Trust the blocker pattern.** When every fix reveals another OS-age issue, stop patching and upgrade the base. Eight blockers in one day was the signal.
2. **Separate VHDX is the right architecture** — weights on `D:\vdisks\models.vhdx` are OS-independent; the migration cost was the OS, not the data.
3. **Scheduled task + fstab is the right persistence.** `wsl --mount --vhd` alone isn't enough — you need both the Windows-side attach trigger AND the Linux-side fstab entry.
4. **Noble (24.04) is the pragmatic target for ML** as of 2026-04. GLIBC 2.39, gcc-13, libstdc++-13. Prebuilt wheels assume something in this range.

## Next steps (handoff)

See [[wsl-ubuntu-migration-handoff|wsl-ubuntu-migration-handoff]] for the pickup-cold procedure a fresh AI session (or the operator on a new day) should follow in Ubuntu-24.04.

## Relationships

- COMPLETES: [[e008-m001-ktransformers-install-and-config|e008-m001-ktransformers-install-and-config]] (redone on 24.04)
- RELATES TO: [[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
- RELATES TO: [[2026-04-23-vhdx-attach-procedure-and-hcs-fix|2026-04-23-vhdx-attach-procedure-and-hcs-fix]]
- RELATES TO: [[2026-04-23-ram-upgrade-48gb-wsl|2026-04-23-ram-upgrade-48gb-wsl]]
- RELATES TO: [[2026-04-23-k2-6-q2-download-complete|2026-04-23-k2-6-q2-download-complete]]

## Backlinks

[[e008-m001-ktransformers-install-and-config|e008-m001-ktransformers-install-and-config]]
[[e010-m002-dev-sdd-mount-procedure|e010-m002-dev-sdd-mount-procedure]]
[[2026-04-23-vhdx-attach-procedure-and-hcs-fix|2026-04-23-vhdx-attach-procedure-and-hcs-fix]]
[[2026-04-23-ram-upgrade-48gb-wsl|2026-04-23-ram-upgrade-48gb-wsl]]
[[2026-04-23-k2-6-q2-download-complete|2026-04-23-k2-6-q2-download-complete]]
