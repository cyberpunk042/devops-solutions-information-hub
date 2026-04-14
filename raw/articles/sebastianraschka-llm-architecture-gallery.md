# LLM Architecture Gallery — Sebastian Raschka

Source: https://sebastianraschka.com/llm-architecture-gallery/
Ingested: 2026-04-14
Type: article

---

## Page Purpose
This is Sebastian Raschka's curated collection of large language model architectures, featuring detailed fact sheets and visual diagrams for 60+ models released between 2019-2026. The gallery enables side-by-side architectural comparisons and links to source articles.

## Key Features

**Architecture Diff Tool**: Users can select two models to compare their specifications side-by-side across multiple dimensions including parameters, context length, attention mechanisms, and KV cache requirements.

**Sorting & Filtering**: Models can be organized by release date (newest/oldest first), alphabetically, or by size, with both detailed and compact viewing modes.

## Representative Model Sampling

### Foundational/Reference Models
- **GPT-2 XL (1.5B)**: 2019 baseline with multi-head attention (MHA), 1,024 token context
- **Llama 3 (8B)**: 2024 reference using grouped-query attention (GQA) with RoPE, 8,192 context
- **Llama 3.2 (1B)**: Compact variant with 128,000 token context despite small parameter count

### Dense Transformer Variants
- **OLMo 2 (7B)**: Uses inside-residual post-norm and QK-Norm; transparent dense model that keeps classic MHA
- **Gemma 3 (27B)**: Employs 5:1 sliding-window/global attention ratio with 262k multilingual vocabulary
- **Phi-4 (14B)**: Drops sliding-window for full-context GQA; classic pre-norm RMSNorm stack

### Sparse Mixture-of-Experts (MoE)
- **DeepSeek V3 (671B)**: 37B active parameters (5.5%), uses multi-head latent attention (MLA), dense prefix plus shared expert
- **Qwen3 (235B-A22B)**: 22B active (9.4%), removes shared expert, optimized for serving efficiency
- **Mistral Large 3 (673B)**: 41B active (6.1%), MLA-based near-clone of DeepSeek V3 with larger experts
- **GLM-5 (744B)**: 40B active (5.4%), adds DeepSeek Sparse Attention for long-context efficiency

### Hybrid & Linear Attention Models
- **Qwen3 Next (80B-A3B)**: 3B active (3.8%), uses 3:1 Gated DeltaNet/Gated Attention hybrid, only 24 KiB KV cache per token
- **Kimi Linear (48B-A3B)**: 3B active (6.3%), replaces full attention with linear attention in most layers, 7.9 KiB KV cache
- **Ling 2.5 (1T)**: 63B active (6.3%), Lightning Attention plus MLA with 7:1 linear/MLA ratio
- **Nemotron 3 Nano (30B-A3B)**: Hybrid Mamba-2/GQA/MoE, most extreme transformer-state-space hybrid

### Multimodal & Instruction-Tuned
- **Gemma 4 (31B)**: Dense with 256K context, unified K/V on global layers, parallel attention/MLP blocks
- **Gemma 4 (E2B & E4B)**: Edge variants with per-layer embeddings and audio support; 2.3B and 4.5B effective compute
- **Kimi K2.5 (1T)**: 32B active (3.2%), native multimodal, MLA-based, 256K native context
- **Mistral Small 4 (119B)**: 6.63B active (5.6%), unified instruct/reasoning/vision, MLA architecture

### Specialized/Recent Models
- **Tiny Aya (3.35B)**: Compact multilingual model with rare parallel transformer block
- **Nanbeige 4.1 (3B)**: Llama-like without tied embeddings, supports 262K context on 3B parameters
- **Sarvam (30B & 105B)**: Indian-language focused, GQA/MLA variants with reasoning orientation

## Technical Metrics Tracked

**KV Cache Per Token (bf16)**:
- Very low: 7.9-24 KiB (linear attention models, sparse hybrids)
- Low: 32-68.6 KiB (MLA-based MoE, efficient architectures)
- Moderate: 128-192 KiB (standard GQA/MoE)
- High: 248-368 KiB (full attention models)
- Very high: 496-840 KiB (MHA or wide GQA with many KV heads)

**Attention Innovations**:
- RoPE (Rotary Position Embeddings) with optional NoPE layers
- QK-Norm (per-head normalization)
- MLA (Multi-head Latent Attention) for efficient KV compression
- Sliding-window attention with global attention fallback
- Gated attention variants
- DeepSeek Sparse Attention (position-based sparsity)

**Context Window Range**: 1,024 tokens (GPT-2) to 1,000,000+ (Kimi K2, Nemotron 3 Super)

## Intelligence Benchmark Data

Models include AA Intelligence Index scores across four categories: General, Scientific, Coding, and Agents. Examples:
- GLM-5.1 (744B): Total 51.4 (General 58.4, Scientific 36.9, Coding 43.4, Agents 67.0)
- GPT-2 XL (1.5B): Total 32.3 (General 31.1, Scientific 24.8, Coding 33.9, Agents 39.4)
- Llama 3.2 (1B): Total 6.3 (General 17.0, Scientific 7.6, Coding 0.6, Agents 0.0)

## Architectural Trends

**Architecture Convergence**: Mistral Large 3 and DeepSeek V3 share nearly identical blueprints despite independent development, suggesting convergence around MLA+MoE templates.

**Normalization Evolution**: Movement from LayerNorm to QK-Norm and post-norm designs for training stability.

**Context Scaling**: Native contexts expanding from 4K to 256K-1M tokens.

**Edge Computing**: Gemma 4 E2B/E4B compress multimodal capabilities into 2.3B-4.5B effective compute footprints.

## Source Articles
1. The Big LLM Architecture Comparison (primary article)
2. From GPT-2 to gpt-oss: Analyzing Architectural Advances
3. From DeepSeek V3 to V3.2: Architecture, Sparse Attention, and RL Updates
4. A Dream of Spring for Open-Weight LLMs (2026 releases)

Last Updated: April 10, 2026
