---
title: "K2.6 Q2 Download + SHA256 Verify Complete (E008 M002 closed)"
type: note
domain: ai-models
note_type: completion
status: synthesized
confidence: high
created: 2026-04-22
updated: 2026-04-22
sources:
  - id: e008-m002-k2-6-q2-gguf-download-and-verify
    type: wiki
    file: wiki/backlog/modules/e008-m002-k2-6-q2-gguf-download-and-verify.md
  - id: unsloth-k2-6-gguf
    type: repository
    url: https://huggingface.co/unsloth/Kimi-K2.6-GGUF
    title: "unsloth/Kimi-K2.6-GGUF"
tags: [note, completion, e008, k2-6, gguf, download, sha256-verified, unsloth, hf-cli]
---

# K2.6 Q2 Download + Verify Complete

## Summary

Unsloth's Kimi-K2.6 Q2 (UD-Q2_K_XL variant, 8 shards) downloaded to `/mnt/models/kimi-k2-6-q2/UD-Q2_K_XL/` and SHA256-verified against HuggingFace's manifest. Total: **318 GB in 51 minutes** — sustained ~104 MB/s over the NVMe VHDX. All hashes match. E008 M002 complete; local K2.6 weights are ready for KTransformers once the toolchain lands (E008 M001).

## What Was Done

1. `pip install --user 'huggingface_hub[cli]'` → `hf` 0.36.2 at `~/.local/bin/`.
2. `mkdir -p /mnt/models/kimi-k2-6-q2`.
3. Launched `hf download unsloth/Kimi-K2.6-GGUF --include "UD-Q2_K_XL/*" --local-dir /mnt/models/kimi-k2-6-q2` in background (PID 19038, stdout → `/mnt/models/kimi-k2-6-q2.download.log`).
4. Progress: 12 GB @ 2:32 → 217 GB @ 35:41 → 318 GB complete @ 51:03.
5. Parallel SHA256 verification on all 8 shards against `.cache/huggingface/download/*.metadata` line 2 → **8/8 OK**.

## Shard manifest (verified 2026-04-22)

| Shard | Size | SHA256 (verified) |
|-------|------|-------------------|
| 00001-of-00008 | 6.6 MB | `6218da3cc528de6a7fb48f8c7fc4ad45f7dbeeba244b3df07c4c98b20b35121c` |
| 00002-of-00008 | 46 GB | `b2c125f7bd8526b1c74a748bba1afc3fc8f0ea3a869cb6ee67821e3b8940d250` |
| 00003-of-00008 | 47 GB | `4a8f9b411de5494c10adff8bc08ad0a87d5e65dde18cb0a432d121032de2ebf1` |
| 00004-of-00008 | 47 GB | `5cb5bf93a64877b7b4a09330dd07e54bcfae5a8ad7ce9e0eb811167b75b8651b` |
| 00005-of-00008 | 47 GB | `124bec4332a086c1ba13dd993ea299d44c913125893fee7d348d94a9ab3e66eb` |
| 00006-of-00008 | 47 GB | `f3b8330d79d96f4288aba35fafe7939dba302abe4ea897146a5e179f748bc0fd` |
| 00007-of-00008 | 47 GB | `31a4040f1f1437f38edbe582f7ccbace5d545b71cd69da9cf1d27efd8bbf73b7` |
| 00008-of-00008 | 40 GB | `7e6303d24550673edf8a13d7698a1820f5a0f7cb220d17d83dffa409cc73d9d5` |

Shard 1 is tokenizer/metadata (tiny); shards 2–8 carry the Q2 quantized weights.

## Corrections vs. planning assumptions

- Estimated size was 340 GB; actual is **318 GB** (~6% lighter). Within budget; `/mnt/models` still has ~640 GB free post-download.
- `hf download` already validates SHA256 during fetch via ETag. The explicit re-verify confirmed integrity a second way.

## Validation

> [!success] All 8 shards present and SHA256-verified
> - 318 GB on `/mnt/models/kimi-k2-6-q2/UD-Q2_K_XL/`
> - 8/8 SHA256 match HuggingFace's manifest
> - `/mnt/models` has 640 GB free

## Newly surfaced blockers for E008 M001 (KTransformers install)

Discovered during T030 (CUDA verify):

1. **No CUDA toolkit in WSL** — `nvcc` missing, `$CUDA_HOME` empty. NVIDIA WSL *driver* is passed through from Windows (confirmed — `nvidia-smi` shows driver 595.97, CUDA runtime 13.2), but the *toolkit* (compiler, headers) has to be installed separately in Ubuntu. KTransformers from-source builds need nvcc.
2. **Python 3.11 not installed** — only Python 3.8.10. KTransformers + Unsloth require ≥3.10. Need `deadsnakes` PPA or `python3.11` via apt.
3. **Dual-GPU setup**: RTX 2080 Ti (11 GB) + RTX 2080 (8 GB) = 19 GB aggregate across TWO cards, not a single 19 GB card. KTransformers optimization YAML will likely need explicit device mapping (`tensor_parallel` or per-layer GPU assignment). Relevant for E008 M003 benchmark, not M001 install.

## Next Steps

Before T031/T032 can run, two prerequisite installs are needed (both require sudo):

```bash
# Prereq A — Python 3.11 via deadsnakes PPA
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3.11-dev

# Prereq B — CUDA toolkit (12.x matches KTransformers requirements; 13.x driver supports down-compat)
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt update
sudo apt install -y cuda-toolkit-12-4    # or 12-6, 12-8 — whatever meets KTransformers min
```

Add to `~/.bashrc`:

```bash
export CUDA_HOME=/usr/local/cuda
export PATH="$CUDA_HOME/bin:$PATH"
export LD_LIBRARY_PATH="$CUDA_HOME/lib64:$LD_LIBRARY_PATH"
```

After those land, T031 (venv at `/home/jfortin/ktransformers-env/`) and T032 (`pip install ktransformers` or from-source) can proceed.

## Relationships

- COMPLETES: [[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
- UNBLOCKS: [[e008-m003-first-light-benchmark|e008-m003-first-light-benchmark]] (once E008 M001 lands)
- RELATES TO: [[e008-m001-ktransformers-install-and-config|e008-m001-ktransformers-install-and-config]]
- RELATES TO: [[2026-04-23-e010-m002-mount-complete|2026-04-23-e010-m002-mount-complete]]

## Backlinks

[[e008-m002-k2-6-q2-gguf-download-and-verify|e008-m002-k2-6-q2-gguf-download-and-verify]]
[[e008-m003-first-light-benchmark|e008-m003-first-light-benchmark]]
[[e008-m001-ktransformers-install-and-config|e008-m001-ktransformers-install-and-config]]
[[2026-04-23-e010-m002-mount-complete|2026-04-23-e010-m002-mount-complete]]
