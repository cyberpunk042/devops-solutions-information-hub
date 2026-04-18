# unslothai/unsloth

Source: https://github.com/unslothai/unsloth
Ingested: 2026-04-17
Type: documentation

---

# README

<h1 align="center" style="margin:0;">
  <a href="https://unsloth.ai/docs"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/unslothai/unsloth/main/images/STUDIO%20WHITE%20LOGO.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/unslothai/unsloth/main/images/STUDIO%20BLACK%20LOGO.png">
    <img alt="Unsloth logo" src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/STUDIO%20BLACK%20LOGO.png" height="60" style="max-width:100%;">
  </picture></a>
</h1>
<h3 align="center" style="margin: 0; margin-top: 0;">
Run and train AI models with a unified local interface.
</h3>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quickstart">Quickstart</a> •
  <a href="#-free-notebooks">Notebooks</a> •
  <a href="https://unsloth.ai/docs">Documentation</a> •
  <a href="https://www.reddit.com/r/unsloth/">Reddit</a>
</p>
 <a href="https://unsloth.ai/docs/new/studio">
<img alt="unsloth studio ui homepage" src="https://raw.githubusercontent.com/unslothai/unsloth/main/studio/frontend/public/studio%20github%20landscape%20colab%20display.png" style="max-width: 100%; margin-bottom: 0;"></a>

Unsloth Studio (Beta) lets you run and train text, [audio](https://unsloth.ai/docs/basics/text-to-speech-tts-fine-tuning), [embedding](https://unsloth.ai/docs/new/embedding-finetuning), [vision](https://unsloth.ai/docs/basics/vision-fine-tuning) models on Windows, Linux and macOS.

## ⭐ Features
Unsloth provides several key features for both inference and training:
### Inference
* **Search + download + run models** including GGUF, LoRA adapters, safetensors
* **Export models**: [Save or export](https://unsloth.ai/docs/new/studio/export) models to GGUF, 16-bit safetensors and other formats.
* **Tool calling**: Support for [self-healing tool calling](https://unsloth.ai/docs/new/studio/chat#auto-healing-tool-calling) and web search
* **[Code execution](https://unsloth.ai/docs/new/studio/chat#code-execution)**: lets LLMs test code in Claude artifacts and sandbox environments
* [Auto-tune inference parameters](https://unsloth.ai/docs/new/studio/chat#auto-parameter-tuning) and customize chat templates.
* We work directly with teams behind [gpt-oss](https://docs.unsloth.ai/new/gpt-oss-how-to-run-and-fine-tune#unsloth-fixes-for-gpt-oss), [Qwen3](https://www.reddit.com/r/LocalLLaMA/comments/1kaodxu/qwen3_unsloth_dynamic_ggufs_128k_context_bug_fixes/), [Llama 4](https://github.com/ggml-org/llama.cpp/pull/12889), [Mistral](models/tutorials/devstral-how-to-run-and-fine-tune.md), [Gemma 1-3](https://news.ycombinator.com/item?id=39671146), and [Phi-4](https://unsloth.ai/blog/phi4), where we’ve fixed bugs that improve model accuracy.
* Upload images, audio, PDFs, code, DOCX and more file types to chat with.
### Training
* Train and RL **500+ models** up to **2x faster** with up to **70% less VRAM**, with no accuracy loss.
* Custom Triton and mathematical **kernels**. See some collabs we did with [PyTorch](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/fp8-reinforcement-learning) and [Hugging Face](https://unsloth.ai/docs/new/faster-moe).
* **Data Recipes**: [Auto-create datasets](https://unsloth.ai/docs/new/studio/data-recipe) from **PDF, CSV, DOCX** etc. Edit data in a visual-node workflow.
* **[Reinforcement Learning](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide)** (RL): The most efficient [RL](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide) library, using **80% less VRAM** for GRPO, [FP8](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/fp8-reinforcement-learning) etc.
* Supports full fine-tuning, RL, pretraining, 4-bit, 16-bit and, FP8 training.
* **Observability**: Monitor training live, track loss and GPU usage and customize graphs.
* [Multi-GPU](https://unsloth.ai/docs/basics/multi-gpu-training-with-unsloth) training is supported, with major improvements coming soon.

## ⚡ Quickstart
Unsloth can be used in two ways: through **[Unsloth Studio](https://unsloth.ai/docs/new/studio/)**, the web UI, or through **Unsloth Core**, the code-based version. Each has different requirements.

### Unsloth Studio (web UI)
Unsloth Studio (Beta) works on **Windows, Linux, WSL** and **macOS**.

* **CPU:** Supported for Chat and Data Recipes currently
* **NVIDIA:** Training works on RTX 30/40/50, Blackwell, DGX Spark, Station and more
* **macOS:** Currently supports chat and Data Recipes. **MLX training** is coming very soon
* **AMD:** Chat + Data works. Train with [Unsloth Core](#unsloth-core-code-based). Studio support is out soon.
* **Coming soon:** Training support for Apple MLX, AMD, and Intel.
* **Multi-GPU:** Available now, with a major upgrade on the way

#### macOS, Linux, WSL:
```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```
#### Windows:
```powershell
irm https://unsloth.ai/install.ps1 | iex
```

#### Launch
```bash
unsloth studio -H 0.0.0.0 -p 8888
```

#### Update
To update, use the same install commands as above. Or run (does not work on Windows):
```bash
unsloth studio update
```

#### Docker
Use our [Docker image](https://hub.docker.com/r/unsloth/unsloth) ```unsloth/unsloth``` container. Run:
```bash
docker run -d -e JUPYTER_PASSWORD="mypassword" \
  -p 8888:8888 -p 8000:8000 -p 2222:22 \
  -v $(pwd)/work:/workspace/work \
  --gpus all \
  unsloth/unsloth
  ```

#### Developer, Nightly, Uninstall
To see developer, nightly and uninstallation etc. instructions, see [advanced installation](#-advanced-installation).

### Unsloth Core (code-based)
#### Linux, WSL:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv unsloth_env --python 3.13
source unsloth_env/bin/activate
uv pip install unsloth --torch-backend=auto
```
#### Windows:
```powershell
winget install -e --id Python.Python.3.13
winget install --id=astral-sh.uv  -e
uv venv unsloth_env --python 3.13
.\unsloth_env\Scripts\activate
uv pip install unsloth --torch-backend=auto
```
For Windows, `pip install unsloth` works only if you have PyTorch installed. Read our [Windows Guide](https://unsloth.ai/docs/get-started/install/windows-installation).
You can use the same Docker image as Unsloth Studio.

#### AMD, Intel:
For RTX 50x, B200, 6000 GPUs: `uv pip install unsloth --torch-backend=auto`. Read our guides for: [Blackwell](https://unsloth.ai/docs/blog/fine-tuning-llms-with-blackwell-rtx-50-series-and-unsloth) and [DGX Spark](https://unsloth.ai/docs/blog/fine-tuning-llms-with-nvidia-dgx-spark-and-unsloth). <br>
To install Unsloth on **AMD** and **Intel** GPUs, follow our [AMD Guide](https://unsloth.ai/docs/get-started/install/amd) and [Intel Guide](https://unsloth.ai/docs/get-started/install/intel).

## 📒 Free Notebooks

Train for free with our notebooks. You can use our new [free Unsloth Studio notebook](https://colab.research.google.com/github/unslothai/unsloth/blob/main/studio/Unsloth_Studio_Colab.ipynb) to run and train models for free in a web UI.
Read our [guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide). Add dataset, run, then deploy your trained model.

| Model | Free Notebooks | Performance | Memory use |
|-----------|---------|--------|----------|
| **Gemma 4 (E2B)**      | [▶️ Start for free](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_(E2B)-Vision.ipynb)               | 1.5x faster | 50% less |
| **Qwen3.5 (4B)**      | [▶️ Start for free](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_(4B)_Vision.ipynb)               | 1.5x faster | 60% less |
| **gpt-oss (20B)**      | [▶️ Start for free](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-(20B)-Fine-tuning.ipynb)               | 2x faster | 70% less |
| **Qwen3.5 GSPO**      | [▶️ Start for free](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_(4B)_Vision_GRPO.ipynb)               | 2x faster | 70% less |
| **gpt-oss (20B): GRPO**      | [▶️ Start for free](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-(20B)-GRPO.ipynb)               | 2x faster | 80% less |
| **Qwen3: Advanced GRPO**      | [▶️ Start for free](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_(4B)-GRPO.ipynb)               | 2x faster | 70% less |
| **embeddinggemma (300M)**    | [▶️ Start for free](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/EmbeddingGemma_(300M).ipynb)               | 2x faster | 20% less |
| **Mistral Ministral 3 (3B)**      | [▶️ Start for free](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Ministral_3_VL_(3B)_Vision.ipynb)               | 1.5x faster | 60% less |
| **Llama 3.1 (8B) Alpaca**      | [▶️ Start for free](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_(8B)-Alpaca.ipynb)               | 2x faster | 70% less |
| **Llama 3.2 Conversational**      | [▶️ Start for free](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_(1B_and_3B)-Conversational.ipynb)               | 2x faster | 70% less |
| **Orpheus-TTS (3B)**     | [▶️ Start for free](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Orpheus_(3B)-TTS.ipynb)               | 1.5x faster | 50% less |

- See all our notebooks for: [Kaggle](https://github.com/unslothai/notebooks?tab=readme-ov-file#-kaggle-notebooks), [GRPO](https://unsloth.ai/docs/get-started/unsloth-notebooks#grpo-reasoning-rl-notebooks), [TTS](https://unsloth.ai/docs/get-started/unsloth-notebooks#text-to-speech-tts-notebooks), [embedding](https://unsloth.ai/docs/new/embedding-finetuning) & [Vision](https://unsloth.ai/docs/get-started/unsloth-notebooks#vision-multimodal-notebooks)
- See [all our models](https://unsloth.ai/docs/get-started/unsloth-model-catalog) and [all our notebooks](https://unsloth.ai/docs/get-started/unsloth-notebooks)
- See detailed documentation for Unsloth [here](https://unsloth.ai/docs)

## 🦥 Unsloth News
- **Gemma 4**: Run and train Google’s new models directly in Unsloth Studio! [Blog](https://unsloth.ai/docs/models/gemma-4)
- **Introducing Unsloth Studio**: our new web UI for running and training LLMs. [Blog](https://unsloth.ai/docs/new/studio)
- **Qwen3.5** - 0.8B, 2B, 4B, 9B, 27B, 35-A3B, 112B-A10B are now supported. [Guide + notebooks](https://unsloth.ai/docs/models/qwen3.5/fine-tune)
- Train **MoE LLMs 12x faster** with 35% less VRAM - DeepSeek, GLM, Qwen and gpt-oss. [Blog](https://unsloth.ai/docs/new/faster-moe)
- **Embedding models**: Unsloth now supports ~1.8-3.3x faster embedding fine-tuning. [Blog](https://unsloth.ai/docs/new/embedding-finetuning) • [Notebooks](https://unsloth.ai/docs/get-started/unsloth-notebooks#embedding-models)
- New **7x longer context RL** vs. all other setups, via our new batching algorithms. [Blog](https://unsloth.ai/docs/new/grpo-long-context)
- New RoPE & MLP **Triton Kernels** & **Padding Free + Packing**: 3x faster training & 30% less VRAM. [Blog](https://unsloth.ai/docs/new/3x-faster-training-packing)
- **500K Context**: Training a 20B model with >500K context is now possible on an 80GB GPU. [Blog](https://unsloth.ai/docs/blog/500k-context-length-fine-tuning)
- **FP8 & Vision RL**: You can now do FP8 & VLM GRPO on consumer GPUs. [FP8 Blog](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/fp8-reinforcement-learning) • [Vision RL](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/vision-reinforcement-learning-vlm-rl)
- **gpt-oss** by OpenAI: Read our [RL blog](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/gpt-oss-reinforcement-learning), [Flex Attention](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/long-context-gpt-oss-training) blog and [Guide](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune).

## 📥 Advanced Installation
The below advanced instructions are for Unsloth Studio. For Unsloth Core advanced installation, [view our docs](https://unsloth.ai/docs/get-started/install/pip-install#advanced-pip-installation).
#### Developer installs: macOS, Linux, WSL:
```bash
git clone https://github.com/unslothai/unsloth
cd unsloth
./install.sh --local
unsloth studio -H 0.0.0.0 -p 8888
```
Then to update :
```bash
unsloth studio update
```

#### Developer installs: Windows PowerShell:
```powershell
git clone https://github.com/unslothai/unsloth.git
cd unsloth
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install.ps1 --local
unsloth studio -H 0.0.0.0 -p 8888
```
Then to update :
```bash
unsloth studio update
```

#### Nightly: MacOS, Linux, WSL:
```bash
git clone https://github.com/unslothai/unsloth
cd unsloth
git checkout nightly
./install.sh --local
unsloth studio -H 0.0.0.0 -p 8888
```
Then to launch every time:
```bash
unsloth studio -H 0.0.0.0 -p 8888
```

#### Nightly: Windows:
Run in Windows Powershell:
```bash
git clone https://github.com/unslothai/unsloth.git
cd unsloth
git checkout nightly
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install.ps1 --local
unsloth studio -H 0.0.0.0 -p 8888
```
Then to launch every time:
```bash
unsloth studio -H 0.0.0.0 -p 8888
```

#### Uninstall
You can uninstall Unsloth Studio by deleting its install folder usually located under `$HOME/.unsloth/studio` on Mac/Linux/WSL and `%USERPROFILE%\.unsloth\studio` on Windows. Using the `rm -rf` commands will **delete everything**, including your history, cache:

* ​ **MacOS, WSL, Linux:** `rm -rf ~/.unsloth/studio`
* ​ **Windows (PowerShell):** `Remove-Item -Recurse -Force "$HOME\.unsloth\studio"`

For more info, [see our docs](https://unsloth.ai/docs/new/studio/install#uninstall).

#### Deleting model files

You can delete old model files either from the bin icon in model search or by removing the relevant cached model folder from the default Hugging Face cache directory. By default, HF uses:

* ​ **MacOS, Linux, WSL:** `~/.cache/huggingface/hub/`
* ​ **Windows:** `%USERPROFILE%\.cache\huggingface\hub\`

## 💚 Community and Links
| Type                                                                                                                                      | Links                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| <img width="16" src="https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/66e3d80db9971f10a9757c99_Symbol.svg" />  **Discord**                       | [Join Discord server](https://discord.com/invite/unsloth)                          |
| <img width="15" src="https://redditinc.com/hs-fs/hubfs/Reddit%20Inc/Brand/Reddit_Logo.png" />  **r/unsloth Reddit**                       | [Join Reddit community](https://reddit.com/r/unsloth)                          |
| 📚 **Documentation & Wiki**                                                                                                               | [Read Our Docs](https://unsloth.ai/docs)                                       |
| <img width="13" src="https://upload.wikimedia.org/wikipedia/commons/0/09/X_(formerly_Twitter)_logo_late_2025.svg" />  **Twitter (aka X)** | [Follow us on X](https://twitter.com/unslothai)                                |
| 🔮 **Our Models**                                                                                                                         | [Unsloth Catalog](https://unsloth.ai/docs/get-started/unsloth-model-catalog)   |
| ✍️ **Blog**                                                                                                                               | [Read our Blogs](https://unsloth.ai/blog)                                      |

### Citation

You can cite the Unsloth repo as follows:
```bibtex
@software{unsloth,
  author = {Daniel Han, Michael Han and Unsloth team},
  title = {Unsloth},
  url = {https://github.com/unslothai/unsloth},
  year = {2023}
}
```
If you trained a model with 🦥Unsloth, you can use this cool sticker!   <img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/made with unsloth.png" width="200" align="center" />

### License
Unsloth uses a dual-licensing model of Apache 2.0 and AGPL-3.0. The core Unsloth package remains licensed under **[Apache 2.0](https://github.com/unslothai/unsloth?tab=Apache-2.0-1-ov-file)**, while certain optional components, such as the Unsloth Studio UI are licensed under the open-source license **[AGPL-3.0](https://github.com/unslothai/unsloth?tab=AGPL-3.0-2-ov-file)**.

This structure helps support ongoing Unsloth development while keeping the project open source and enabling the broader ecosystem to continue growing.

### Thank You to
- The [llama.cpp library](https://github.com/ggml-org/llama.cpp) that lets users run and save models with Unsloth
- The Hugging Face team and their libraries: [transformers](https://github.com/huggingface/transformers) and [TRL](https://github.com/huggingface/trl)
- The Pytorch and [Torch AO](https://github.com/unslothai/unsloth/pull/3391) team for their contributions
- NVIDIA for their [NeMo DataDesigner](https://github.com/NVIDIA-NeMo/DataDesigner) library and their contributions
- And of course for every single person who has contributed or has used Unsloth!



> **Deep fetch: 11 key files fetched beyond README.**



---

# FILE: .pre-commit-ci.yaml

ci:
  autofix_prs: true
  autofix_prs_limit: 5
  autoupdate_schedule: monthly
  autoupdate_commit_msg: "chore: pre-commit autoupdate"
  skip: []



---

# FILE: .pre-commit-config.yaml

repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.15.10
    hooks:
      - id: ruff
        args:
          - --fix
          - --exit-non-zero-on-fix
        exclude: '\.ipynb$'
  - repo: local
    hooks:
      - id: ruff-format-with-kwargs
        name: Ruff format with kwarg spacing
        entry: scripts/run_ruff_format.py
        language: python
        types: [python]
        additional_dependencies:
          - ruff==0.6.9



---

# FILE: CODE_OF_CONDUCT.md


# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, caste, color, religion, or sexual
identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the overall
  community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or advances of
  any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email address,
  without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at support@unsloth.ai.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series of
actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or permanent
ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within the
community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder][Mozilla CoC].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][FAQ]. Translations are available at
[https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
[Mozilla CoC]: https://github.com/mozilla/diversity
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations



---

# FILE: CONTRIBUTING.md

# 🦥 Contributing to Unsloth

Thank you for not only using Unsloth but also for being interested in helping out! We value all contributions, whether they come in the form of code, ideas, support for others or just by simply spreading the word of Unsloth! 💕

- **[Support the Community](https://github.com/unslothai/unsloth/issues)**: Answer questions, review pull requests, or assist others in discussions.
- **Fix Bugs**: Identify and resolve issues with the existing codebase.
- **Submit Ideas**: Request new features or share enhancements you'd like to see.
- **Develop Features**: Implement new functionality or improve existing tools which can be done via PRs.
- **[Improve Documentation](https://docs.unsloth.ai/)**: Help by creating guides, FAQs, or enhancing clarity.

One of the best ways to support us is by spreading the word about Unsloth! Share how it’s powering your amazing projects in blog posts or social media, and inspire others to explore its potential. Even a simple star on our repo goes a long way in showing your support and helping the community grow. 🌟

## Submitting Issues
If you find a bug or have a feature idea, we’d love to hear from you! Here’s how to make your submission stand out:

### Reporting Bugs
1. **Search First**: Check if the issue has already been reported using GitHub’s search bar under Issues.
2. **Details Matter**: Is this on Google Colab, Kaggle, or on another platform service? Are you using Unsloth's official notebook? Include your OS, Python version, and other relevant details. For bugs, a concise code snippet that reproduces the issue is incredibly helpful.
3. **Be Thorough**: Attach screenshots, traceback logs, or any additional information that might speed up resolution.

## Spread the Word
Your support extends beyond code:
- Spread the word by writing about Unsloth in blogs or social media.
- Share how Unsloth powers your projects.
- Star our repository to show your appreciation.

Finally, please be mindful of our [Code of Conduct](https://github.com/unslothai/unsloth/blob/main/CODE_OF_CONDUCT.md) to ensure a welcoming and inclusive environment for everyone.

Thank you so much for reading and we hope you have lots of fun using Unsloth! 🦥



---

# FILE: studio/frontend/src/features/data-recipes/learning-recipes/conversation.json

{
  "recipe": {
    "model_providers": [
      {
        "name": "provider_1",
        "endpoint": "https://openrouter.ai/api/v1",
        "provider_type": "openai",
        "extra_headers": {},
        "extra_body": {}
      }
    ],
    "mcp_providers": [],
    "model_configs": [
      {
        "alias": "model_1",
        "model": "mistralai/ministral-8b-2512",
        "provider": "provider_1",
        "inference_parameters": {
          "temperature": 0.7,
          "max_tokens": 2048
        }
      }
    ],
    "tool_configs": [],
    "columns": [
      {
        "column_type": "sampler",
        "name": "domain",
        "drop": true,
        "sampler_type": "category",
        "params": {
          "values": [
            "Tech Support",
            "Personal Finance",
            "Learning"
          ]
        }
      },
      {
        "column_type": "sampler",
        "name": "topic",
        "drop": true,
        "sampler_type": "subcategory",
        "params": {
          "category": "domain",
          "values": {
            "Tech Support": [
              "Wi-Fi keeps disconnecting",
              "Laptop running very slow",
              "Cannot install app update"
            ],
            "Personal Finance": [
              "Monthly budget planning",
              "Credit card debt payoff",
              "Emergency fund setup"
            ],
            "Learning": [
              "Exam study plan",
              "Learn Python basics",
              "Improve English writing"
            ]
          }
        }
      },
      {
        "column_type": "sampler",
        "name": "conversation_length",
        "drop": true,
        "sampler_type": "category",
        "params": {
          "values": [
            "4",
            "6"
          ]
        }
      },
      {
        "column_type": "llm-text",
        "name": "user_goal",
        "drop": false,
        "model_alias": "model_1",
        "prompt": "Write one user goal for a chat assistant.\nDomain: {{ domain }}\nTopic: {{ topic }}\nConversation length target: {{ conversation_length }} messages total.\nRules:\n- 1 sentence.\n- Specific and practical.\n- Output only the goal text.",
        "system_prompt": "You write realistic user goals for assistant conversations.\n",
        "with_trace": "none"
      },
      {
        "column_type": "llm-structured",
        "name": "output_format",
        "drop": false,
        "model_alias": "model_1",
        "prompt": "Generate a realistic multi-turn conversation.\nUser goal:\n{{ user_goal }}\nConstraints:\n- Exactly {{ conversation_length }} messages total.\n- Alternate roles strictly: user, assistant, user, assistant...\n- First message must be user.\n- Last message must be assistant.\n- Keep responses grounded in {{ domain }} / {{ topic }}.\n- End naturally with resolution or clear next step.\n- No markdown, no extra keys.",
        "output_format": {
          "type": "object",
          "properties": {
            "conversation": {
              "type": "array",
              "minItems": 4,
              "maxItems": 6,
              "items": {
                "type": "object",
                "properties": {
                  "role": {
                    "type": "string",
                    "enum": [
                      "user",
                      "assistant"
                    ]
                  },
                  "content": {
                    "type": "string",
                    "minLength": 1
                  }
                },
                "required": [
                  "role",
                  "content"
                ],
                "additionalProperties": false
              }
            }
          },
          "required": [
            "conversation"
          ],
          "additionalProperties": false
        }
      }
    ],
    "processors": []
  },
  "run": {
    "rows": 5,
    "preview": true,
    "output_formats": [
      "jsonl"
    ]
  },
  "ui": {
    "nodes": [
      {
        "id": "provider_1",
        "x": -1056.848383841495,
        "y": 519.6373927070263,
        "width": 400
      },
      {
        "id": "model_1",
        "x": -543.7221365246206,
        "y": 488.2975724283656,
        "width": 400
      },
      {
        "id": "domain",
        "x": 0,
        "y": 140,
        "width": 400
      },
      {
        "id": "topic",
        "x": 0,
        "y": 280,
        "width": 400
      },
      {
        "id": "conversation_length",
        "x": 466.61510192672256,
        "y": 139.68271861864798,
        "width": 400
      },
      {
        "id": "user_goal",
        "x": 1.412158386197035,
        "y": 508.77123580445596,
        "width": 400
      },
      {
        "id": "output_format",
        "x": 1.1486983549970375,
        "y": 754.4221089431811,
        "width": 400
      },
      {
        "id": "note_1",
        "x": 210.01377182764494,
        "y": -262.9440547613487,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_1",
        "markdown": "###  Start with controlled chat context\nThis recipe uses sampler columns to shape each conversation:\n\n- `domain`\n- `topic`\n- `conversation_length` (4 or 6 messages)\n\n**Why this helps**:\n\n- You get varied conversations without manual writing\n- Each row stays grounded in a clear scenario\n- You can scale quickly while keeping data quality consistent",
        "note_color": "#FFE4E6",
        "note_opacity": "35"
      },
      {
        "id": "note_2",
        "x": 515.9369583007435,
        "y": 454.3936030274385,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_2",
        "markdown": "The **LLM Text** block (`user_goal`) creates one realistic user intent from sampler context.\n\n**It should be**:\n\n- **specific**\n- **practical**\n- **short**\n\nThis goal becomes the anchor for the full multi-turn conversation.",
        "note_color": "#FFE4E6",
        "note_opacity": "35"
      },
      {
        "id": "note_3",
        "x": -12.952616065779239,
        "y": 912.1316336111515,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_3",
        "markdown": "The **LLM Structured** block (`output_format`) generates the conversation as strict JSON.\n\nIn this recipe, schema enforces:\n\n- `conversation` array\n- message objects with `role` + `content`\n- role enum: `user` / `assistant`\n- no extra keys\n\nPrompt constraints also enforce:\n\n- exact length (`{{ conversation_length }}`)\n- alternating roles\n- first user message, last assistant message\n- natural ending\n\nThis is key for training data: same shape, less cleanup.",
        "note_color": "#FFE4E6",
        "note_opacity": "35"
      },
      {
        "id": "note_4",
        "x": -519.9585237323188,
        "y": 81.84144119564277,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_4",
        "markdown": "Sampler columns are useful during generation but usually noisy in final export.\n\nSet helper columns to `drop=true`, keep only core outputs such as:\n\n- `user_goal`\n- `output_format`\n\nTip: Keep final schema close to your training format, not your generation scaffolding.\n",
        "note_color": "#FFE4E6",
        "note_opacity": "35"
      }
    ],
    "edges": [
      {
        "from": "domain",
        "to": "topic",
        "type": "canvas",
        "source_handle": "data-out-bottom",
        "target_handle": "data-in-top"
      },
      {
        "from": "domain",
        "to": "conversation_length",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "topic",
        "to": "user_goal",
        "type": "canvas",
        "source_handle": "data-out-bottom",
        "target_handle": "data-in-top"
      },
      {
        "from": "user_goal",
        "to": "output_format",
        "type": "canvas",
        "source_handle": "data-out-bottom",
        "target_handle": "data-in-top"
      },
      {
        "from": "provider_1",
        "to": "model_1",
        "type": "semantic",
        "source_handle": "semantic-out",
        "target_handle": "semantic-in"
      },
      {
        "from": "model_1",
        "to": "user_goal",
        "type": "semantic",
        "source_handle": "semantic-out",
        "target_handle": "data-in"
      },
      {
        "from": "model_1",
        "to": "output_format",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "data-in"
      }
    ],
    "layout_direction": "LR"
  }
}



---

# FILE: studio/frontend/src/features/data-recipes/learning-recipes/instruction-from-answer.json

{
  "recipe": {
    "model_providers": [
      {
        "name": "openai_provider",
        "endpoint": "",
        "provider_type": "openai",
        "extra_headers": {},
        "extra_body": {}
      }
    ],
    "mcp_providers": [],
    "model_configs": [
      {
        "alias": "ministral",
        "model": "",
        "provider": "openai_provider",
        "inference_parameters": {
          "temperature": 0.7,
          "max_tokens": 2048
        }
      }
    ],
    "seed_config": {
      "source": {
        "seed_type": "hf",
        "path": "unsloth/alpaca-cleaned",
        "endpoint": "https://huggingface.co"
      },
      "sampling_strategy": "ordered",
      "selection_strategy": {
        "start": 1,
        "end": 100
      }
    },
    "tool_configs": [],
    "columns": [
      {
        "column_type": "llm-text",
        "name": "generated_instruction",
        "drop": false,
        "model_alias": "ministral",
        "prompt": "Based on this target answer:\n{{ output }}\n\nWrite one high-quality plain text short and brief user instruction that this answer would satisfy.\nReturn only the instruction.",
        "with_trace": "none",
        "extract_reasoning_content": false
      }
    ],
    "processors": [
      {
        "processor_type": "drop_columns",
        "name": "drop_seed_columns",
        "column_names": [
          "input",
          "instruction"
        ]
      }
    ]
  },
  "run": {
    "rows": 5,
    "preview": true,
    "output_formats": [
      "jsonl"
    ]
  },
  "ui": {
    "nodes": [
      {
        "id": "note_1",
        "x": -567.3566303099885,
        "y": 38.88875727651093,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_1",
        "markdown": "#### Hugging Face seed block\nThis recipe uses a ** HuggingFace dataset ** as seed data.\nYou select a Hugging Face dataset, load columns, then generate new fields from seed columns. Each column in the Hugging Face dataset becomes a valid variable that you can reference eg. `{{ topic }}`\n\n##### Setup:\n\n1. Search for a dataset and select one in the dropdown (example: `unsloth/alpaca-cleaned`)\n2. Add token only if dataset is gated/private\n3. Load columns + preview rows so variables are available in prompts\n\n##### Why this matters:\n- Seed columns can drive generation quality\n- You can reference seed values directly in prompts (for example `{{ output }}`)",
        "note_color": "#DCFCE7",
        "note_opacity": "35"
      },
      {
        "id": "note_2",
        "x": -74.04047072330651,
        "y": -265.3540670633283,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_2",
        "markdown": "##### Drop columns behavior:\n\n- You can mark specific seed columns to **drop from final output**\n- Those columns are still used during generation\n- They are removed only from exported final dataset\n\n##### Example:\n- Keep `generated_instruction` from llm-text block\n- Drop original `instruction`, `input`, `output` from the hugginface dataset from final dataset\n- Result: clean training output while still using source columns as generation context\n",
        "note_color": "#DCFCE7",
        "note_opacity": "35"
      },
      {
        "id": "seed",
        "x": -76.07288662013991,
        "y": 143.39449780463954,
        "width": 400
      },
      {
        "id": "openai_provider",
        "x": 461.00000000000006,
        "y": -489.8750000000001,
        "width": 400
      },
      {
        "id": "ministral",
        "x": 463.272022949692,
        "y": -191.13601147484601,
        "width": 400
      },
      {
        "id": "generated_instruction",
        "x": 464,
        "y": 109.00000000000003,
        "width": 400
      }
    ],
    "edges": [
      {
        "from": "seed",
        "to": "generated_instruction",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "ministral",
        "to": "generated_instruction",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "data-in-top"
      },
      {
        "from": "openai_provider",
        "to": "ministral",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "semantic-in-top"
      }
    ],
    "layout_direction": "LR",
    "seed_source_type": "hf",
    "seed_columns": [],
    "seed_drop_columns": [],
    "seed_preview_rows": [],
    "local_file_name": "",
    "unstructured_file_name": "",
    "unstructured_chunk_size": "1200",
    "unstructured_chunk_overlap": "200"
  }
}



---

# FILE: studio/frontend/src/features/data-recipes/learning-recipes/ocr-document-extraction.json

{
  "recipe": {
    "model_providers": [
      {
        "name": "provider_1",
        "endpoint": "https://openrouter.ai/api/v1",
        "provider_type": "openai",
        "extra_headers": {},
        "extra_body": {}
      }
    ],
    "mcp_providers": [],
    "model_configs": [
      {
        "alias": "provider_column",
        "model": "google/gemini-2.0-flash-001",
        "provider": "provider_1",
        "inference_parameters": {
          "temperature": 0.2,
          "max_tokens": 4096
        }
      }
    ],
    "seed_config": {
      "source": {
        "seed_type": "hf",
        "path": "datasets/ylecun/mnist/mnist/**/*.parquet"
      },
      "sampling_strategy": "ordered",
      "selection_strategy": null
    },
    "tool_configs": [],
    "columns": [
      {
        "column_type": "llm-text",
        "name": "ocr_text",
        "drop": false,
        "model_alias": "provider_column",
        "prompt": "Transcribe all text from this document image.",
        "multi_modal_context": [
          {
            "modality": "image",
            "column_name": "image"
          }
        ]
      }
    ],
    "processors": []
  },
  "run": {
    "rows": 5,
    "preview": true,
    "output_formats": ["jsonl"]
  },
  "ui": {
    "nodes": [
      {
        "id": "note_1",
        "x": -180,
        "y": 43,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_1",
        "markdown": "This recipe uses **Gemini 2.0 Flash** via OpenRouter to transcribe document images into clean text.\n\nThe Seed block is prefilled with `ylecun/mnist` so you can run immediately. You can swap to any Hugging Face dataset that includes an `image` column.\n\nOutput: `ocr_text` column with the raw transcribed text per image.",
        "note_color": "#DCFCE7",
        "note_opacity": "35"
      },
      {
        "id": "note_2",
        "x": 283,
        "y": -333,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_2",
        "markdown": "##### Setup\n\nAdd your OpenRouter API key to the **Model Provider** block — same as every other recipe.\n\nGemini 2.0 Flash is well-suited for OCR: fast, cheap, and strong on tables, receipts, forms, and multi-column layouts.\n\nWant a purpose-built OCR model? Swap the endpoint to a local vLLM server running `lightonai/LightOnOCR-2-1B` for maximum throughput.",
        "note_color": "#DCFCE7",
        "note_opacity": "35"
      },
      {
        "id": "note_3",
        "x": 303,
        "y": 299,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_3",
        "markdown": "##### Seed: HF dataset with image column\n\nThis template starts with `ylecun/mnist` so first run works without seed setup.\n\nTo use your own data: open Seed → keep **HF dataset** selected → choose a dataset that contains an `image` column → click **Load**.\n\nThen open the LLM Text block and set **Image Context** to the `image` column so each row image is sent with the prompt.\n\nTip: datasets with embedded image columns are more reliable than URL-only image fields.",
        "note_color": "#DCFCE7",
        "note_opacity": "35"
      },
      {
        "id": "seed",
        "x": 295,
        "y": 108,
        "width": 400
      },
      {
        "id": "provider_1",
        "x": 960,
        "y": -465,
        "width": 400
      },
      {
        "id": "provider_column",
        "x": 959,
        "y": -180,
        "width": 400
      },
      {
        "id": "ocr_text",
        "x": 960,
        "y": 108,
        "width": 400
      }
    ],
    "edges": [
      {
        "from": "seed",
        "to": "ocr_text",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "provider_1",
        "to": "provider_column",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "semantic-in-top"
      },
      {
        "from": "provider_column",
        "to": "ocr_text",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "data-in-top"
      }
    ],
    "layout_direction": "LR",
    "seed_source_type": "hf",
    "seed_columns": [],
    "seed_drop_columns": [],
    "seed_preview_rows": [],
    "local_file_name": "",
    "unstructured_file_name": "",
    "unstructured_chunk_size": "900",
    "unstructured_chunk_overlap": "150"
  }
}



---

# FILE: studio/frontend/src/features/data-recipes/learning-recipes/pdf-grounded-qa.json

{
  "recipe": {
    "model_providers": [
      {
        "name": "provider_1",
        "endpoint": "",
        "provider_type": "openai",
        "extra_headers": {},
        "extra_body": {}
      }
    ],
    "mcp_providers": [],
    "model_configs": [
      {
        "alias": "provider_column",
        "model": "",
        "provider": "provider_1",
        "inference_parameters": {
          "temperature": 0.7
        }
      }
    ],
    "seed_config": {
      "source": {
        "seed_type": "unstructured",
        "path": "",
        "chunk_size": 1200,
        "chunk_overlap": 200
      },
      "sampling_strategy": "ordered",
      "selection_strategy": null
    },
    "tool_configs": [],
    "columns": [
      {
        "column_type": "llm-structured",
        "name": "llm_structured_1",
        "drop": false,
        "model_alias": "provider_column",
        "prompt": "Given ONLY this chunk: {{ chunk_text }} generate one answerable question, answer, and exact supporting quote from chunk. If not answerable, skip.",
        "with_trace": "none",
        "extract_reasoning_content": false,
        "output_format": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "question",
            "answer",
            "evidence_quote"
          ],
          "properties": {
            "question": {
              "type": "string"
            },
            "answer": {
              "type": "string"
            },
            "evidence_quote": {
              "type": "string"
            }
          }
        }
      }
    ],
    "processors": []
  },
  "run": {
    "rows": 5,
    "preview": true,
    "output_formats": [
      "jsonl"
    ]
  },
  "ui": {
    "nodes": [
      {
        "id": "note_1",
        "x": 474.6120044693708,
        "y": 1229.5810476890458,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_1",
        "markdown": "This recipe uses **seed data** from external documents.\nInstead of starting from empty generation, we load real source text first.\n\nIn this flow, the seed source is **Unstructured Documents**:\n\n- Upload: `.pdf`, `.docx`, `.txt`\n- Text is extracted and split on client into chunks\n- Each chunk becomes a row-like seed record (`chunk_text`) that you can reference in prompts with `{{ chunk_text }} `",
        "note_color": "#F3E8FF",
        "note_opacity": "35"
      },
      {
        "id": "note_2",
        "x": 26.758540311329455,
        "y": 963.3465578835235,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_2",
        "markdown": "##### Chunking settings:\n\n- **Chunk size**: how much text per chunk\n- **Chunk overlap**: shared text between neighboring chunks to preserve context\n\n##### Sampling settings:\n\n- **Ordered**: keep original document order\n- **Shuffle**: randomize chunk order\n- **Selection index / selection settings**: choose which part/subset of seed data to use",
        "note_color": "#F3E8FF",
        "note_opacity": "35"
      },
      {
        "id": "note_3",
        "x": 473.62551435180245,
        "y": 741.5352258256931,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_3",
        "markdown": "- LLM prompt: `{{ chunk_text }}`\n- Expression block: combine/format values using `{{ chunk_text }}`\n- Processor templates: use `{{ chunk_text }}` during transforms\n\nTip:\n- Start with medium chunk size + small overlap.\n- Increase overlap only if answers lose context between chunks.",
        "note_color": "#F3E8FF",
        "note_opacity": "35"
      },
      {
        "id": "seed",
        "x": 484.36210245413577,
        "y": 1059.99180558796,
        "width": 400
      },
      {
        "id": "provider_1",
        "x": 960,
        "y": 622,
        "width": 400
      },
      {
        "id": "provider_column",
        "x": 960,
        "y": 816,
        "width": 400
      },
      {
        "id": "llm_structured_1",
        "x": 960,
        "y": 1077,
        "width": 400
      }
    ],
    "edges": [
      {
        "from": "provider_1",
        "to": "provider_column",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "semantic-in-top"
      },
      {
        "from": "provider_column",
        "to": "llm_structured_1",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "data-in-top"
      },
      {
        "from": "llm_structured_1",
        "to": "seed",
        "type": "canvas",
        "source_handle": "data-out-left",
        "target_handle": "data-in-right"
      }
    ],
    "layout_direction": "LR",
    "seed_source_type": "unstructured",
    "seed_columns": [],
    "seed_drop_columns": [],
    "seed_preview_rows": [],
    "local_file_name": "",
    "unstructured_file_name": "",
    "unstructured_chunk_size": "1200",
    "unstructured_chunk_overlap": "200"
  }
}


---

# FILE: studio/frontend/src/features/data-recipes/learning-recipes/structured-outputs-jinja.json

{
  "recipe": {
    "model_providers": [
      {
        "name": "provider_column",
        "endpoint": "",
        "provider_type": "openai",
        "extra_headers": {},
        "extra_body": {}
      }
    ],
    "mcp_providers": [],
    "model_configs": [
      {
        "alias": "ministral",
        "model": "",
        "provider": "provider_column",
        "inference_parameters": {
          "temperature": 0.7
        }
      }
    ],
    "tool_configs": [],
    "columns": [
      {
        "column_type": "sampler",
        "name": "user",
        "drop": true,
        "sampler_type": "person_from_faker",
        "params": {}
      },
      {
        "column_type": "sampler",
        "name": "platform",
        "drop": false,
        "sampler_type": "category",
        "params": {
          "values": [
            "web",
            "mobile",
            "cli"
          ]
        }
      },
      {
        "column_type": "sampler",
        "name": "impact_scope",
        "drop": false,
        "sampler_type": "category",
        "params": {
          "values": [
            "single_user",
            "team",
            "org_wide"
          ]
        }
      },
      {
        "column_type": "expression",
        "name": "user_first_name",
        "drop": false,
        "expr": "{{ user.first_name }}",
        "dtype": "str"
      },
      {
        "column_type": "expression",
        "name": "user_full_name",
        "drop": false,
        "expr": "{{ user.first_name }} {{ user.last_name }}",
        "dtype": "str"
      },
      {
        "column_type": "llm-structured",
        "name": "ticket",
        "drop": false,
        "model_alias": "ministral",
        "prompt": "Create a realistic support ticket from {{ user_full_name }} using the {{ platform }} platform. Impact scope is {{ impact_scope }}.\n",
        "with_trace": "none",
        "extract_reasoning_content": false,
        "output_format": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "issue_title",
            "issue_summary",
            "category",
            "priority"
          ],
          "properties": {
            "issue_title": {
              "type": "string",
              "description": "Short title of issue"
            },
            "issue_summary": {
              "type": "string",
              "description": "1-2 sentence summary"
            },
            "category": {
              "type": "string",
              "enum": [
                "account",
                "billing",
                "api",
                "infra"
              ],
              "description": "Issue category"
            },
            "priority": {
              "type": "string",
              "enum": [
                "P1",
                "P2",
                "P3"
              ],
              "description": "Urgency level"
            }
          }
        }
      },
      {
        "column_type": "expression",
        "name": "sla_target",
        "drop": false,
        "expr": "{% if impact_scope == 'org_wide' %}15m\n{% elif impact_scope == 'team' %}1h\n{% else %}4h\n{% endif %}",
        "dtype": "str"
      },
      {
        "column_type": "llm-structured",
        "name": "agent_reply",
        "drop": false,
        "model_alias": "ministral",
        "prompt": "Write a concise support reply for ticket '{{ ticket.issue_title }}'. Category: {{ ticket.category }}. Priority: {{ ticket.priority }}. SLA target: {{ sla_target }}. {% if ticket.priority == 'P1' %}Tone must be urgent and action-first.{% else %}Tone must be calm and instructional.{% endif %}",
        "with_trace": "none",
        "extract_reasoning_content": false,
        "output_format": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "response",
            "next_action"
          ],
          "properties": {
            "response": {
              "type": "string",
              "description": "Support response to user"
            },
            "next_action": {
              "type": "string",
              "enum": [
                "ask_logs",
                "reset_credentials",
                "escalate",
                "provide_steps"
              ],
              "description": "Primary next action"
            }
          }
        }
      }
    ],
    "processors": []
  },
  "run": {
    "rows": 5,
    "preview": true,
    "output_formats": [
      "jsonl"
    ]
  },
  "ui": {
    "nodes": [
      {
        "id": "note_1",
        "x": 990.3973509933774,
        "y": 1487.5768211920529,
        "width": 782,
        "node_type": "markdown_note",
        "name": "note_1",
        "markdown": "## Expression columns \nAre like lightweight spreadsheet formulas.\nUse them when you want to transform existing columns quickly, without calling an LLM.\n\n### What you can do:\n\n- Use values from other columns: `{{ first_name }} {{ last_name }}`\n- Clean/format text: `{{ city | upper }}`, `{{ product_name | trim }}`\n- Conditional logic:\n  - `{% if order_total >= 100 %}VIP{% elif order_total >= 50 %}Standard{% else %}Starter{% endif %}`\n- Simple math:\n  - `{{ quantity * unit_price }}`\n  - `{{ (subtotal - discount) | round(2) }}`\n\n### Good rule:\n- If the value can be computed from existing data, use Expression first.\n- Use LLM only when you need true language generation.",
        "note_color": "#CFFAFE",
        "note_opacity": "35"
      },
      {
        "id": "note_2",
        "x": 3217.6543046357615,
        "y": 2081.596026490066,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_2",
        "markdown": "### LLM Structured block\nGenerates JSON that matches your Output Format schema.\nThink of Output Format as a contract for what the model must return.\n\n#### Prompt tips:\n\n- Reference existing columns with Jinja: `{{ column_name }}`\n- You can reference nested values too: `{{ customer.first_name }}`\n- Be explicit about what each field should contain.\n\n#### Example prompt pattern:\n\n```text\nCreate a support ticket summary.\nCustomer: {{ customer_name }}\nIssue text: {{ issue_text }}\n\nReturn data for:\n- priority\n- short_title\n- resolution_steps\n```",
        "note_color": "#CFFAFE",
        "note_opacity": "35"
      },
      {
        "id": "note_3",
        "x": 2294.4516556291387,
        "y": 2399.6099337748346,
        "width": 638,
        "node_type": "markdown_note",
        "name": "note_3",
        "markdown": "## Example output format shape (concept):\n\n```json\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"priority\": { \"type\": \"string\" },\n    \"short_title\": { \"type\": \"string\" },\n    \"resolution_steps\": { \"type\": \"array\", \"items\": { \"type\": \"string\" } }\n  },\n  \"required\": [\"priority\", \"short_title\", \"resolution_steps\"]\n}\n```",
        "note_color": "#CFFAFE",
        "note_opacity": "35"
      },
      {
        "id": "note_4",
        "x": 2544.684105960265,
        "y": 1126.5490066225163,
        "width": 399,
        "node_type": "markdown_note",
        "name": "note_4",
        "markdown": "### Model provider & Config\nEvery LLM block needs a model alias.\nThat alias comes from a Model Config.\nModel Config points to a Model Provider.\n\n#### Minimum setup:\n\n1. Create **Model Provider**\n   - Set endpoint/provider type\n   - Prefer env var auth (`api_key_env`) over hardcoded keys\n\n2. Create **Model Config**\n   - Set alias (example: `model_1`)\n   - Set model id\n   - Link to provider\n   - Tune params (temperature, max_tokens, etc.)\n\n3. In each LLM block\n   - Set `model_alias` to that alias\n\nIf alias/provider link is missing, validation/run will fail.",
        "note_color": "#CFFAFE",
        "note_opacity": "35"
      },
      {
        "id": "provider_column",
        "x": 2542,
        "y": 1696,
        "width": 400
      },
      {
        "id": "ministral",
        "x": 2542,
        "y": 1890,
        "width": 400
      },
      {
        "id": "user",
        "x": 191,
        "y": 2423,
        "width": 400
      },
      {
        "id": "platform",
        "x": 858.0384105960266,
        "y": 2286.5,
        "width": 400
      },
      {
        "id": "impact_scope",
        "x": 1342,
        "y": 2286.5,
        "width": 400
      },
      {
        "id": "user_first_name",
        "x": 1822,
        "y": 2505,
        "width": 400
      },
      {
        "id": "user_full_name",
        "x": 1822,
        "y": 1959,
        "width": 400
      },
      {
        "id": "ticket",
        "x": 2302,
        "y": 2286.5,
        "width": 400
      },
      {
        "id": "sla_target",
        "x": 1822,
        "y": 2232,
        "width": 400
      },
      {
        "id": "agent_reply",
        "x": 2782,
        "y": 2151,
        "width": 400
      }
    ],
    "edges": [
      {
        "from": "platform",
        "to": "impact_scope",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "user",
        "to": "user_first_name",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "user_full_name",
        "to": "ticket",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "user",
        "to": "platform",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "user",
        "to": "user_full_name",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "user_first_name",
        "to": "ticket",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "impact_scope",
        "to": "sla_target",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "sla_target",
        "to": "ticket",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "ticket",
        "to": "agent_reply",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "provider_column",
        "to": "ministral",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "semantic-in-top"
      },
      {
        "from": "ministral",
        "to": "ticket",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "data-in-top"
      },
      {
        "from": "ministral",
        "to": "agent_reply",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "data-in-top"
      }
    ],
    "layout_direction": "LR"
  }
}


---

# FILE: studio/frontend/src/features/data-recipes/learning-recipes/text-to-python.json

{
  "recipe": {
    "model_providers": [
      {
        "name": "openai-compatible",
        "endpoint": "",
        "provider_type": "openai",
        "extra_headers": {},
        "extra_body": {}
      }
    ],
    "mcp_providers": [],
    "model_configs": [
      {
        "alias": "coding-model",
        "model": "",
        "provider": "openai-compatible",
        "inference_parameters": {
          "temperature": 0.7
        }
      }
    ],
    "tool_configs": [],
    "columns": [
      {
        "column_type": "sampler",
        "name": "domain",
        "drop": false,
        "sampler_type": "category",
        "params": {
          "values": [
            "Data Processing",
            "Web API",
            "Automation"
          ]
        }
      },
      {
        "column_type": "sampler",
        "name": "task_type",
        "drop": false,
        "sampler_type": "subcategory",
        "params": {
          "category": "domain",
          "values": {
            "Data Processing": [
              "CSV cleaning",
              "JSON transform",
              "deduplicate rows"
            ],
            "Web API": [
              "GET endpoint",
              "POST validation",
              "pagination helper"
            ],
            "Automation": [
              "file organizer",
              "log parser",
              "daily report script"
            ]
          }
        }
      },
      {
        "column_type": "llm-text",
        "name": "instruction",
        "drop": false,
        "model_alias": "coding-model",
        "prompt": "Write one clear Python coding instruction.\nDomain: {{ domain }}\nTask type: {{ task_type }}\n\nKeep it practical and specific.\nReturn only the instruction without any code.",
        "with_trace": "none",
        "extract_reasoning_content": false
      },
      {
        "column_type": "llm-code",
        "name": "code_implementation",
        "drop": false,
        "model_alias": "coding-model",
        "prompt": "Write Python code for:\n{{ instruction }}\n\nRequirements:\n- runnable script or function\n- include needed imports\n- short comments only where useful\n- no markdown fences",
        "with_trace": "none",
        "extract_reasoning_content": false,
        "code_lang": "python"
      },
      {
        "column_type": "llm-judge",
        "name": "code_judge_result",
        "drop": false,
        "model_alias": "coding-model",
        "prompt": "Evaluate generated Python code against the instruction.\n\nInstruction:\n{{ instruction }}\n\nCode:\n{{ code_implementation }}",
        "with_trace": "none",
        "extract_reasoning_content": false,
        "scores": [
          {
            "name": "Correctness",
            "description": "Follows instruction and is executable",
            "options": {
              "0": "bad",
              "1": "partial",
              "2": "good",
              "3": "excellent"
            }
          }
        ]
      }
    ],
    "processors": []
  },
  "run": {
    "rows": 5,
    "preview": true,
    "output_formats": [
      "jsonl"
    ]
  },
  "ui": {
    "nodes": [
      {
        "id": "note_1",
        "x": 1526,
        "y": 1790.75,
        "width": 568,
        "node_type": "markdown_note",
        "name": "note_1",
        "markdown": "The **LLM Code** block is where Python code is generated from your instruction/prompt.\n\n##### How it works in this recipe:\n\n- You provide a clear prompt (often using Jinja references from earlier columns)\n- The model returns a response\n- The block extracts code content directly for the output column\n\n##### Current status:\n\n- We are **not** running Python lint/syntax validation in this recipe yet (Soon)\n- Validation support is planned and will be added\n\n##### What this means:\n\n- You may get mostly correct code, but some rows can still have syntax/style issues\n- Keep prompts specific and constrained to reduce bad outputs\n\n##### Tip:\n\n- Ask for one self-contained function/script\n- Ask for required imports\n- Ask for no markdown fences if you want cleaner extraction\n",
        "note_color": "#FEF3C7",
        "note_opacity": "35"
      },
      {
        "id": "note_2",
        "x": 2597.376821192053,
        "y": 1233.2039735099338,
        "width": 471,
        "node_type": "markdown_note",
        "name": "note_2",
        "markdown": "The **LLM Judge** block evaluates generated outputs with rubric-style scores.\n\n##### Important:\n\n- A judge can have **one or many scores**\n- Each score has:\n  - a name (for example: `Correctness`)\n  - a description\n  - options (value + meaning)\n\n##### Example multi-score setup:\n\n- Correctness\n- Readability\n- Efficiency\n\n##### Why use multiple scores:\n\n- You get richer quality signals than a single pass/fail\n- Easier filtering and weighting later in training data prep\n\n##### Practical pattern:\n\n1. Generate code with LLM Code\n2. Judge with 2-4 focused scores\n3. Keep high-quality rows based on score thresholds\n",
        "note_color": "#FEF3C7",
        "note_opacity": "35"
      },
      {
        "id": "openai-compatible",
        "x": 1627.1046357615896,
        "y": 921.0301324503313,
        "width": 400
      },
      {
        "id": "coding-model",
        "x": 1627.1046357615894,
        "y": 1138.910927152318,
        "width": 400
      },
      {
        "id": "domain",
        "x": 84,
        "y": 1600.5,
        "width": 400
      },
      {
        "id": "task_type",
        "x": 648,
        "y": 1600.5,
        "width": 400
      },
      {
        "id": "instruction",
        "x": 1128,
        "y": 1567,
        "width": 400
      },
      {
        "id": "code_implementation",
        "x": 1627.1046357615894,
        "y": 1531.4728476821192,
        "width": 400
      },
      {
        "id": "code_judge_result",
        "x": 2124.617218543046,
        "y": 1567.076490066225,
        "width": 400
      }
    ],
    "edges": [
      {
        "from": "domain",
        "to": "task_type",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "task_type",
        "to": "instruction",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "openai-compatible",
        "to": "coding-model",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "semantic-in-top"
      },
      {
        "from": "instruction",
        "to": "code_implementation",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "coding-model",
        "to": "instruction",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "data-in-top"
      },
      {
        "from": "coding-model",
        "to": "code_implementation",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "data-in-top"
      },
      {
        "from": "code_implementation",
        "to": "code_judge_result",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "coding-model",
        "to": "code_judge_result",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "data-in-top"
      }
    ],
    "layout_direction": "LR"
  }
}


---

# FILE: studio/frontend/src/features/data-recipes/learning-recipes/text-to-sql.json

{
  "recipe": {
    "model_providers": [
      {
        "name": "vllm",
        "endpoint": "",
        "provider_type": "openai",
        "extra_headers": {},
        "extra_body": {}
      }
    ],
    "mcp_providers": [],
    "model_configs": [
      {
        "alias": "sql-pro",
        "model": "",
        "provider": "vllm",
        "inference_parameters": {
          "temperature": 0.7
        }
      }
    ],
    "tool_configs": [],
    "columns": [
      {
        "column_type": "sampler",
        "name": "domain",
        "drop": true,
        "sampler_type": "category",
        "params": {
          "values": [
            "Ecommerce",
            "Customer Support",
            "Finance"
          ]
        }
      },
      {
        "column_type": "sampler",
        "name": "topic",
        "drop": true,
        "sampler_type": "subcategory",
        "params": {
          "category": "domain",
          "values": {
            "Ecommerce": [
              "Orders and Revenue",
              "Returns and Refunds",
              "Product Performance"
            ],
            "Customer Support": [
              "Ticket Resolution",
              "SLA Compliance",
              "Agent Productivity"
            ],
            "Finance": [
              "Invoices and Payments",
              "Subscription Churn",
              "Monthly Cashflow"
            ]
          }
        }
      },
      {
        "column_type": "sampler",
        "name": "sql_task_type",
        "drop": true,
        "sampler_type": "category",
        "params": {
          "values": [
            "Filtering",
            "Aggregation",
            "Join Analysis",
            "Trend Reporting"
          ]
        }
      },
      {
        "column_type": "sampler",
        "name": "instruction_phrase",
        "drop": true,
        "sampler_type": "category",
        "params": {
          "values": [
            "Write a SQL query that",
            "Create a SQL statement to",
            "Develop a SQL query to"
          ]
        }
      },
      {
        "column_type": "llm-text",
        "name": "sql_prompt",
        "drop": false,
        "model_alias": "sql-pro",
        "prompt": "Generate one natural-language SQL task.\nContext:\n- Domain: {{ domain }}\n- Topic: {{ topic }}\n- Task type: {{ sql_task_type }}\nRules:\n- Must start exactly with: \"{{ instruction_phrase }}\"\n- Make it specific and practical.\n- Mention expected business outcome.\n- Keep it 1-2 sentences.\n- Do not include SQL code.\n- Output only the instruction text.",
        "system_prompt": "You create clear, realistic business SQL tasks for training data.\n",
        "with_trace": "none",
        "extract_reasoning_content": false
      },
      {
        "column_type": "llm-code",
        "name": "sql",
        "drop": false,
        "model_alias": "sql-pro",
        "prompt": "Write SQL for this instruction:\n{{ sql_prompt }}\nReturn ONE SQL script with this exact structure:\n-- SCHEMA\n[CREATE TABLE statements]\n[INSERT statements with sample rows]\n-- QUERY\n[final SELECT query solving the instruction]\nRules:\n- Use 2-3 tables max.\n- Use realistic snake_case names.\n- Include 5-8 rows of sample data per table.\n- Query must match task type \"{{ sql_task_type }}\".\n- Use only tables/columns you created.\n- No markdown fences.\n- No explanation text outside SQL comments shown above.",
        "system_prompt": "You are an expert SQL engineer. Produce correct, runnable SQL only.\n",
        "with_trace": "none",
        "extract_reasoning_content": false,
        "code_lang": "sql:ansi"
      },
      {
        "column_type": "validation",
        "name": "sql-validator",
        "drop": false,
        "target_columns": [
          "sql"
        ],
        "validator_type": "code",
        "validator_params": {
          "code_lang": "sql:ansi"
        },
        "batch_size": 10
      }
    ],
    "processors": []
  },
  "run": {
    "rows": 5,
    "preview": true,
    "output_formats": [
      "jsonl"
    ]
  },
  "ui": {
    "nodes": [
      {
        "id": "note_1",
        "x": 338,
        "y": 1020,
        "width": 600,
        "node_type": "markdown_note",
        "name": "note_1",
        "markdown": "##### This recipe starts with **sampler columns** to create controlled SQL task context:\n\n- `domain`\n- `topic` (subcategory from `domain`)\n- `sql_task_type`\n- `instruction_phrase`\n\n##### Why this is useful:\n\n- You get diverse tasks without writing every prompt by hand\n- You can steer business context + task pattern in a predictable way\n- LLM prompts become cleaner because context is already structured",
        "note_color": "#DBEAFE",
        "note_opacity": "35"
      },
      {
        "id": "note_2",
        "x": 1675.8410596026492,
        "y": 1644.2185430463576,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_2",
        "markdown": "The **LLM Text** block (`sql_prompt`) turns sampler context into one clean natural-language SQL task.\n\n##### Prompt pattern in this recipe:\n\n- references prior columns with Jinja (`{{ domain }}`, `{{ topic }}`, etc.)\n- enforces start phrase with `{{ instruction_phrase }}`\n- returns instruction text only (no SQL yet)\n\n##### Tip:\n\n- Keep this instruction block concise and specific\n- Save implementation details for the next SQL generation block",
        "note_color": "#DBEAFE",
        "note_opacity": "35"
      },
      {
        "id": "note_3",
        "x": 2198.980132450331,
        "y": 1723.1456953642385,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_3",
        "markdown": "The **LLM Code** block (`sql`) generates SQL script from `{{ sql_prompt }}`.\n\n##### In this recipe it returns:\n\n- schema section (`CREATE TABLE`)\n- sample seed rows (`INSERT`)\n- final query (`SELECT`)\n",
        "note_color": "#DBEAFE",
        "note_opacity": "35"
      },
      {
        "id": "note_4",
        "x": 1264,
        "y": 1037,
        "width": 400,
        "node_type": "markdown_note",
        "name": "note_4",
        "markdown": "Sampler columns are useful during generation, but often noisy in final output.\n\nSet helper columns to **drop=true** (like in this recipe), keep only output columns you want to export.\n\n#### Final keep we have set here:\n\n- `sql_prompt`\n- `sql`\n\n",
        "note_color": "#DBEAFE",
        "note_opacity": "35"
      },
      {
        "id": "vllm",
        "x": 1939.5364238410598,
        "y": 781.25,
        "width": 400
      },
      {
        "id": "sql-pro",
        "x": 1939.5364238410593,
        "y": 975.25,
        "width": 400
      },
      {
        "id": "domain",
        "x": 680,
        "y": 1495,
        "width": 400
      },
      {
        "id": "topic",
        "x": 1160,
        "y": 1413,
        "width": 400
      },
      {
        "id": "sql_task_type",
        "x": 1160,
        "y": 1577,
        "width": 400
      },
      {
        "id": "instruction_phrase",
        "x": 100,
        "y": 1495,
        "width": 400
      },
      {
        "id": "sql_prompt",
        "x": 1672.6490066225165,
        "y": 1457.6854304635763,
        "width": 400
      },
      {
        "id": "sql",
        "x": 2194.9006622516554,
        "y": 1457.110927152318,
        "width": 400
      },
      {
        "id": "sql-validator",
        "x": 2682.5827814569534,
        "y": 1491.0413907284767,
        "width": 400
      }
    ],
    "edges": [
      {
        "from": "domain",
        "to": "topic",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "domain",
        "to": "sql_task_type",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "instruction_phrase",
        "to": "domain",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "topic",
        "to": "sql_prompt",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "sql_prompt",
        "to": "sql",
        "type": "canvas",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "vllm",
        "to": "sql-pro",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "semantic-in-top"
      },
      {
        "from": "sql-pro",
        "to": "sql",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "data-in-top"
      },
      {
        "from": "sql",
        "to": "sql-validator",
        "type": "semantic",
        "source_handle": "data-out",
        "target_handle": "data-in"
      },
      {
        "from": "sql-pro",
        "to": "sql_prompt",
        "type": "semantic",
        "source_handle": "semantic-out-bottom",
        "target_handle": "data-in-top"
      },
      {
        "from": "sql_prompt",
        "to": "sql_task_type",
        "type": "canvas",
        "source_handle": "data-out-left",
        "target_handle": "data-in-right"
      }
    ],
    "layout_direction": "LR"
  }
}