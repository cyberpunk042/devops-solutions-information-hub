---
title: "WSL Ubuntu-24.04 Migration Handoff (pickup-cold procedure)"
type: reference
domain: cross-domain
status: verified
confidence: high
maturity: mature
priority: P0
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: wsl-migration-log
    type: wiki
    file: wiki/log/2026-04-22-wsl-migration-to-ubuntu-24-04.md
  - id: vhdx-attach-fix
    type: wiki
    file: wiki/log/2026-04-23-vhdx-attach-procedure-and-hcs-fix.md
  - id: storage-tiering-ref
    type: wiki
    file: wiki/spine/references/operator-workstation-storage-tiering.md
tags: [reference, p0, wsl, ubuntu-24-04, migration, handoff, pickup-cold, ml-workstation, ktransformers, aicp]
---

# WSL Ubuntu-24.04 Migration Handoff

## Summary

This page is the **pickup-cold procedure** for any AI session (or the operator after an absence) that lands in the Post-Anthropic milestone after the 2026-04-22 WSL migration. It captures: where things live, what's already done, what still needs to happen, and the sequenced commands to bring Ubuntu-24.04 to parity with the original milestone plan. Read this page first before touching anything — the migration changed several ground-truth facts that earlier docs may not reflect yet.

> [!warning] If you are looking for a blocker or procedure that seems stale
> The 2026-04-22 migration invalidated Ubuntu-20.04-specific install steps in several docs. This page is the authoritative current state. Trust this over older install procedures when they disagree.

## Reference Content

### 1. Current ground truth (post-migration)

| Dimension | Value |
|-----------|-------|
| Primary WSL distro | **Ubuntu-24.04** (noble) at `D:\wsl\ubuntu-24.04\` |
| Secondary distro (legacy) | Ubuntu-20.04 — retained read-only for reference, planned decommission |
| Default user in 24.04 | `jfortin` (UID 1000, sudo, NOPASSWD) |
| systemd | enabled (`/etc/wsl.conf` has `[boot] systemd=true`) |
| Host RAM | 64 GB physical, 48 GB WSL cap (`.wslconfig memory=48GB`) |
| GPU | RTX 2080 Ti (11 GB) + RTX 2080 (8 GB) = 19 GB aggregate, 2 cards |
| NVIDIA driver | 595.97 / CUDA runtime 13.2 (WSL passthrough) |
| `/mnt/models` | 1 TB ext4 on NVMe VHDX (`D:\vdisks\models.vhdx`) |
| K2.6 Q2 weights | **318 GB** on `/mnt/models/kimi-k2-6-q2/UD-Q2_K_XL/`, SHA256-verified |

### 2. What's already done (don't redo)

- Ubuntu-24.04 installed + user renamed from `ubuntu` → `jfortin` with UID 1000
- `/etc/wsl.conf` configured for systemd + default user
- Windows Task Scheduler task `WSL-Mount-Models-VHDX` auto-attaches the models VHDX on logon
- `/etc/fstab` entry in 24.04 auto-mounts `/mnt/models` on distro boot
- CUDA toolkit install procedure documented (apt via cuda-keyring repo)
- VHDX attach ACL procedure (`takeown` + `icacls`) already applied to `D:\vdisks\models.vhdx` — persists

### 3. What's still pending

| Task | Priority | Status |
|------|----------|--------|
| Install CUDA toolkit 12.6 (or later) on 24.04 | P0 | pending |
| Clone `devops-expert-local-ai` repo on 24.04 | P0 | pending |
| Clone `devops-solutions-research-wiki` on 24.04 | P0 | pending |
| Recreate AICP venv via `uv sync` | P0 | pending |
| Install ktransformers via pip wheel (should "just work" on 24.04) | P0 | pending |
| Validate ktransformers + torch + dual-GPU detection | P0 | pending |
| Decommission Ubuntu-20.04 (optional, after 24.04 proven) | P2 | pending |

### 4. Pickup-cold procedure — sequenced commands

#### Step 4.1 — Enter Ubuntu-24.04 and sanity-check state

```powershell
# Windows PS
wsl -d Ubuntu-24.04
```

Inside:

```bash
id                            # expect uid=1000(jfortin)
df -h /mnt/models             # expect ~1 TB total, ~318 GB used
ls /mnt/models/kimi-k2-6-q2/UD-Q2_K_XL/    # expect 8 .gguf shards
nvidia-smi                    # expect both GPUs visible
free -g                       # expect ~47 GiB total
```

If `/mnt/models` isn't mounted, re-trigger the Windows scheduled task:

```powershell
# Windows PS admin
Start-ScheduledTask -TaskName "WSL-Mount-Models-VHDX"
```

#### Step 4.2 — Core dev tooling (one time)

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential git curl ca-certificates \
                    python3 python3-pip python3-venv python3-dev \
                    pkg-config libnuma-dev libhwloc-dev \
                    gcc g++ cmake jq

# uv (same tool AICP uses)
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.local/bin/env 2>/dev/null || source ~/.cargo/env 2>/dev/null

git config --global user.email "jfm.devops.expert@gmail.com"
git config --global user.name "Cyberpunk 042"
```

#### Step 4.3 — SSH keys (copy from 20.04 or generate new)

```bash
# Option A: copy from the old distro (fastest)
cp -r /mnt/wsl/instances/Ubuntu-20.04/home/jfortin/.ssh ~/
chmod 700 ~/.ssh && chmod 600 ~/.ssh/id_*

# Option B: generate fresh + upload pubkey to GitHub
ssh-keygen -t ed25519 -C "jfm.devops.expert@gmail.com"
cat ~/.ssh/id_ed25519.pub   # paste into github.com/settings/keys
```

Test:
```bash
ssh -T git@github.com
```

#### Step 4.4 — CUDA toolkit

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt update
sudo apt install -y cuda-toolkit-12-6

echo 'export CUDA_HOME=/usr/local/cuda
export PATH="$CUDA_HOME/bin:$PATH"
export LD_LIBRARY_PATH="$CUDA_HOME/lib64:$LD_LIBRARY_PATH"' >> ~/.bashrc
source ~/.bashrc

nvcc --version     # should show 12.6
nvidia-smi         # should show both GPUs
```

#### Step 4.5 — Clone repos

```bash
mkdir -p ~/projects && cd ~/projects
git clone git@github.com:<your-user>/devops-expert-local-ai.git
git clone git@github.com:<your-user>/devops-solutions-research-wiki.git
# Clone any others you need
```

#### Step 4.6 — Recreate AICP venv

```bash
cd ~/projects/devops-expert-local-ai
uv sync       # reads pyproject.toml, recreates .venv with matching deps
source .venv/bin/activate
python --version    # should match the pyproject.toml requires-python
```

#### Step 4.7 — Install ktransformers (the real test)

```bash
source ~/projects/devops-expert-local-ai/.venv/bin/activate
uv pip install --python .venv/bin/python ktransformers

python -c "
import kt_kernel; import torch
print('kt_kernel OK, variant:', getattr(kt_kernel, '__cpu_variant__', 'unknown'))
print('torch:', torch.__version__)
print('cuda available:', torch.cuda.is_available())
print('device_count:', torch.cuda.device_count())
for i in range(torch.cuda.device_count()):
    p = torch.cuda.get_device_properties(i)
    print(f'  GPU {i}: {p.name} | {p.total_memory/1024**3:.1f} GB')
"
```

Expected on 24.04: all imports succeed, both GPUs detected, cuda_available=True. If this works, E008 M001 is effectively done on the new OS.

#### Step 4.8 — Run a K2.6 smoke inference (validates E008 M002 + M003 viability)

```bash
# Point KTransformers at the Q2 weights
python -m ktransformers.local_chat \
  --model-path /mnt/models/kimi-k2-6-q2/UD-Q2_K_XL \
  --gguf-path /mnt/models/kimi-k2-6-q2/UD-Q2_K_XL \
  --max-new-tokens 50 \
  --prompt "Identify yourself in one sentence."
# Expect reply to reference Kimi / Moonshot. Benchmark timing = first-light data for E008 M003.
```

### 5. What to do when it works

Update the following (in the wiki repo):

1. `wiki/log/<date>-e008-m001-ktransformers-install-complete-on-24-04.md` — new completion log.
2. Flip `wiki/backlog/modules/e008-m001-ktransformers-install-and-config.md` status → done.
3. Note in [[2026-04-22-wsl-migration-to-ubuntu-24-04|2026-04-22-wsl-migration-to-ubuntu-24-04]] log that the migration paid off.

### 6. Key files/paths to know

| Path | Purpose |
|------|---------|
| `/mnt/models/kimi-k2-6-q2/UD-Q2_K_XL/` | K2.6 Q2 weights (8 shards, 318 GB) |
| `/mnt/models/kimi-k2-6-q2/.source.url` | Provenance URL for re-download if needed |
| `/mnt/models/kimi-k2-6-q2/.sha256-verified` | Verification date |
| `D:\vdisks\models.vhdx` | Windows-side VHDX backing `/mnt/models` — ACLs pre-fixed |
| `D:\wsl\ubuntu-24.04\` | Ubuntu-24.04 rootfs VHDX |
| `C:\ProgramData\wsl-scripts\mount-models.ps1` | Windows script auto-attaching VHDX on logon |
| `%USERPROFILE%\.wslconfig` | VM-wide config (memory=48GB) |
| `/etc/wsl.conf` (inside 24.04) | Distro config (default user, systemd) |
| `/etc/fstab` (inside 24.04) | Mount entry for `/mnt/models` |

### 7. Known pitfalls

- **`wsl --mount --vhd` is not persistent.** Every `wsl --shutdown` detaches the VHDX. Scheduled task + fstab combo re-attaches on next logon. If `/mnt/models` is empty, step 4.1's `Start-ScheduledTask` fixes it.
- **Ubuntu-20.04 still exists.** If you open a terminal and land in 20.04 by accident, you'll hit the old blockers. Default distro for new shells should be Ubuntu-24.04: `wsl --set-default Ubuntu-24.04`.
- **Dual GPU is 11+8, not 19.** KTransformers optimization YAML for K2.6 may assume a single large GPU. When authoring the optimization config (E008 M003), use per-layer device mapping or tensor parallelism, not assumed-single-card.
- **The 318 GB K2.6 download does NOT need to be repeated.** Files persist on the VHDX. Re-running `hf download` in 24.04 would just re-verify and exit early.

## Relationships

- PART OF: [[post-anthropic-self-autonomous-stack|Milestone: Post-Anthropic Self-Autonomous AI Stack]]
- BUILDS ON: [[2026-04-22-wsl-migration-to-ubuntu-24-04|2026-04-22-wsl-migration-to-ubuntu-24-04]]
- REFERENCES: [[operator-workstation-storage-tiering|operator-workstation-storage-tiering]]
- REFERENCES: [[2026-04-23-vhdx-attach-procedure-and-hcs-fix|2026-04-23-vhdx-attach-procedure-and-hcs-fix]]
- UNBLOCKS: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
- UNBLOCKS: [[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]

## Backlinks

[[post-anthropic-self-autonomous-stack|Milestone: Post-Anthropic Self-Autonomous AI Stack]]
[[2026-04-22-wsl-migration-to-ubuntu-24-04|2026-04-22-wsl-migration-to-ubuntu-24-04]]
[[operator-workstation-storage-tiering|operator-workstation-storage-tiering]]
[[2026-04-23-vhdx-attach-procedure-and-hcs-fix|2026-04-23-vhdx-attach-procedure-and-hcs-fix]]
[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
[[E012-custom-model-library-unsloth-loras|E012-custom-model-library-unsloth-loras]]
