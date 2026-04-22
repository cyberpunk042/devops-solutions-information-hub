---
title: "E010 M001 — 64 GB RAM Install and Verify (physical + WSL detection)"
type: module
domain: backlog
status: done
priority: P0
task_type: module
current_stage: test
readiness: 100
progress: 100
stages_completed: [document, design, scaffold, implement, test]
artifacts: []
epic: "E010"
depends_on: []
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e010-storage-and-hardware-enablement
    type: wiki
    file: wiki/backlog/epics/pre-milestone/E010-storage-and-hardware-enablement.md
tags: [module, p0, e010, ram, hardware, wsl, memory, install]
---

# E010 M001 — 64 GB RAM Install and Verify

## Summary

Physically install the 64 GB RAM kit arriving 2026-04-23, then verify from WSL that the full capacity is detected and error-free. This is the prerequisite for running K2.6 Q2 locally — 32 GB is insufficient for the expert-cache + context headroom K2.6 MoE inference requires. Module has two tasks: (1) physical install + WSL config if needed, (2) verification and dmesg error scan.

## Tasks

| Task | Title | Readiness | Progress | Status |
|------|-------|-----------|----------|--------|
| T039 | Physical install + WSL .wslconfig memory cap update | 100% | 0% | draft |
| T040 | Verify detected capacity + dmesg error scan | 100% | 0% | draft |

## Dependencies

- 64 GB DDR5/DDR4 kit arriving 2026-04-23 (operator-provided).
- Operator physical access + downtime window (estimate 30 min).
- BIOS access — some boards require MemTest or XMP profile adjustment after install.

## Done When

- [ ] 64 GB kit physically installed; chassis closed; PC powers on to BIOS
- [ ] BIOS reports 64 GB (or 2× 32 GB if dual-channel) with correct speed
- [ ] Windows detects 64 GB (Task Manager → Performance → Memory)
- [ ] `%USERPROFILE%\.wslconfig` updated to cap WSL at 48–56 GB (leave 8–16 GB for Windows host)
- [ ] WSL restarted (`wsl --shutdown` from PowerShell, then reopen)
- [ ] Inside WSL: `free -g` reports ≥48 GiB total (capacity minus WSL cap headroom)
- [ ] `dmesg | grep -i -E "error|corrected|uncorrected"` is empty or shows no memory errors on the fresh boot
- [ ] Result recorded in `wiki/log/2026-04-23-ram-upgrade.md`
- [ ] All child tasks at status: done

## Procedure (reference — operator runs)

### Step 0 — Before install

```powershell
# On Windows, back up current WSL config if any
copy "$env:USERPROFILE\.wslconfig" "$env:USERPROFILE\.wslconfig.bak.$(Get-Date -Format yyyyMMddHHmmss)" 2>$null
```

### Step 1 — Physical install

Operator-driven:

1. Full shutdown (not just sleep)
2. Unplug, discharge static
3. Install DIMMs in correct slots per motherboard manual (usually A2 + B2 first for dual-channel)
4. Close chassis, boot to BIOS
5. Confirm 64 GB detected; enable XMP/DOCP profile for rated speed
6. Save, reboot to Windows

### Step 2 — Configure .wslconfig

```powershell
# On Windows, edit %USERPROFILE%\.wslconfig (create if missing)
notepad "$env:USERPROFILE\.wslconfig"
```

Content:

```ini
[wsl2]
memory=48GB
swap=16GB
processors=auto
```

Rationale: leave ~16 GB for Windows host + Docker + background processes. WSL's 48 GB budget is enough for K2.6 Q2 expert cache + 32K context, per the memory estimate in `wiki/spine/references/2026-consumer-hardware-ai-stack.md`.

### Step 3 — Restart WSL

```powershell
wsl --shutdown
# Wait ~10s, then reopen your WSL terminal
```

### Step 4 — Verify from inside WSL

```bash
free -g                               # expect ≥48 GiB total
cat /proc/meminfo | head -5
dmesg | grep -iE "error|corrected|uncorrected" | head -30   # expect empty
uname -a
```

### Step 5 — Log the upgrade

```bash
cd /home/jfortin/devops-solutions-research-wiki
python3 -m tools.pipeline scaffold note "2026-04-23-ram-upgrade"
$EDITOR wiki/log/2026-04-23-ram-upgrade.md
# Fields: date, installed kit (size, speed, model), BIOS-reported speed,
#         .wslconfig cap, free -g output, dmesg grep result
python3 -m tools.pipeline post
```

## Rollback

If instability post-install:

1. Reseat DIMMs (most common fix).
2. Disable XMP/DOCP — run at JEDEC default speed.
3. Remove the new kit, reinstall old kit. No software rollback required — `.wslconfig` simply caps WSL's memory view; remove or lower the `memory=` line if the new kit is pulled.

## Impediments

| Impediment | Type | Blocked Since | Escalated? | Resolution |
|-----------|------|---------------|-----------|------------|
| RAM kit arrival date slip | external | 2026-04-22 | no | Operator confirms shipment ETA; all downstream dates shift if delayed |
| WSL memory cap mis-set | config | 2026-04-22 | no | `.wslconfig` documented; .bak created before edit |
| BIOS XMP instability | hardware | 2026-04-22 | no | Fall back to JEDEC default; acceptable for LLM workloads |

## Relationships

- PART OF: [[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
- FEEDS INTO: [[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]

## Backlinks

[[E010-storage-and-hardware-enablement|E010-storage-and-hardware-enablement]]
[[E008-local-k2-6-offline-frontier-tier|E008-local-k2-6-offline-frontier-tier]]
