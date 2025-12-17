# ThursdAI Q2 2025 - AI Yearly Recap
## The Quarter That Shattered Reality

*Based on 13 ThursdAI episodes from April 3 - June 26, 2025*

---

![Q2 2025 ThursdAI Infographic](https://pub-7837090e9353474292fc8c7114c5fa9d.r2.dev/thursdai_infographics/Q2%202025%20ThursdAI%20Q2%20infographic.jpg)

---

## 🔥 Quarter Overview

Q2 2025 will be remembered as the quarter when **video AI crossed the uncanny valley** (VEO3's native audio blew minds), **tool-using reasoning models emerged** (o3 can call tools mid-thought!), and **open source matched frontier models** (Qwen 3 and Claude 4 delivered back-to-back). Google I/O dropped an avalanche of announcements, Meta's Llama 4 had a chaotic launch, and the agent ecosystem matured with MCP becoming the universal standard.

---

## 📅 April 2025 - "Tool-Using Reasoners & Llama Chaos"

### 🎯 Top Stories

#### 🧠 **OpenAI o3 & o4-mini - Reasoning Meets Tool Use** (Apr 17)
The most important reasoning model upgrade in AI history. For the first time, o-series models can:
- **Autonomously use tools during reasoning** (web search, Python, image gen)
- Chain 600+ consecutive tool calls to solve complex problems
- Manipulate images mid-thought (cropping, zooming, rotating)
- Score **$65k on Freelancer eval** (vs o1's $28k)
- **o4-mini hits 99.5% on AIME** when using Python interpreter

> "This is almost AGI territory - agents that reason while wielding tools" - Alex Volkov

#### 📚 **GPT-4.1 Family - 1 Million Token Context** (Apr 14)
OpenAI dropped GPT-4.1, 4.1-mini, and 4.1-nano with:
- **1 million token context window** across all three models
- GPT-4.5 deprecated - 4.1 actually outperforms it
- Near-perfect recall across entire 1M context
- 4.1-mini achieves 72% on Video-MME
- "Sandwich" prompting trick boosts mini from 31% → 49%

#### 🦙 **Meta Llama 4 - Scout & Maverick** (Apr 5)
Meta dropped their biggest models ever, amid controversy:
- **Scout**: 17B active / 109B total (16 experts) - 10M context claimed
- **Maverick**: 17B active / 400B total (128 experts) - 1M context
- Release caused LMArena drama (tested model ≠ released model)
- Community criticism: too big to run locally
- **Behemoth (288B active / 2T total)** teased but unreleased

#### ⚡ **Gemini 2.5 Flash - Controllable Thinking Budgets** (Apr 17)
Google's direct counter to o3/o4-mini:
- Set "thinking budget" (0-24K tokens) per API call
- 1M token context window
- Ultra-cheap: $0.15 input / $0.60 output per 1M tokens
- Balance speed/cost vs reasoning depth in one model

### Open Source LLMs
| Release | Significance |
|---------|-------------|
| **DeepCoder-14B** | Beats DeepSeek R1 on coding, distributed RL training |
| **NVIDIA Nemotron Ultra 253B** | Pruned Llama 405B, actually beats Llama 4 on AIME |
| **Kimi-VL 3B** | MIT licensed VLM, 128K context, rivals 10x larger models |
| **HiDream-I1 17B** | MIT license, surpasses Flux 1.1 Pro on image gen |
| **GLM-4 Family** | ChatGLM rebranded, MIT licensed, up to 70B |

### Big CO LLMs + APIs
- **Google celebrates MCP** - official support announced, joining Microsoft & AWS
- **Google A2A Protocol** - Agent-to-Agent communication standard launched
- **Grok 3 API** - xAI finally opens API access
- **ChatGPT Memory Upgrade** - can now reference ALL past chats

### Vision & Video
- **VEO-2 GA** - Google's video model goes Generally Available
- **Kling 2.0 Creative Suite** - MVL prompting, inline images in text prompts
- **Runway Gen-4** - Focus on character/world consistency
- **MAGI-1 24B** - Send AI drops open weights video model (Apache 2.0)

### Voice & Audio
- **Dia 1.6B TTS** - Unhinged emotional range from Korean startup, MIT licensed
- **PipeCat SmartTurn** - Open source semantic VAD for natural conversations
- **DolphinGemma** - Google AI attempts dolphin communication 🐬

### Tools
- **OpenAI Codex CLI** - Open source with Apple Seatbelt security
- **Firebase Studio** - Google's vibe coding platform (formerly Project IDX)
- **GitMCP** - Turn any GitHub repo into MCP server (viral launch)

---

## 📅 May 2025 - "Qwen 3 Revolution & Claude 4 Arrives"

### 🎯 Top Stories

#### 🔥 **Qwen 3 - The Open Source Benchmark Crusher** (May 1)
Alibaba dropped the most comprehensive open source release ever:
- **8 models**: 2 MoE (235B/22B active, 30B/3B active) + 6 dense (0.6B-32B)
- **Apache 2.0 license** on everything
- Runtime `/think` toggle for chain-of-thought on demand
- **4B dense beats Qwen 2.5-72B** on multiple benchmarks 🤯
- 36T training tokens, 119 languages, 128K context
- Day-one support in LM Studio, Ollama, vLLM, MLX

> "The 30B MoE is 'Sonnet 3.5 at home' - 100+ tokens/sec on MacBooks" - Nisten

#### 🤖 **Claude 4 Opus & Sonnet - Live Drop During ThursdAI!** (May 22)
Anthropic crashed the party mid-show with:
- **Claude 4 Opus**: 72.5% SWE-bench, handles 6-7 hour human tasks
- **Claude 4 Sonnet**: 72.7% SWE-bench (80% with parallel test-time compute!)
- First models to cross 80% on SWE-bench threshold
- Hybrid reasoning + instant response modes
- 65% less likely to engage in loopholes vs Sonnet 3.7
- Knowledge cutoff: March 2025

#### 🎬 **VEO3 - The Undisputed Star of Google I/O** (May 20)
The video model that crossed the uncanny valley:
- **Native multimodal audio** - generates speech, sound effects, music synced perfectly
- Perfect lip-sync with situational awareness
- Characters look at each other, understand who's speaking
- Can generate text within videos
- Spawned viral "Prompt Theory" phenomenon on TikTok

> "VEO3 isn't just video generation - it's a world simulator" - Alex Volkov

#### 🎨 **GPT-4o Native Image Gen - Ghibli-mania 2.0** (May 22)
OpenAI enables native image gen in GPT-4o (again), now via API:
- **GPT Image 1 API** finally released
- Organizational verification required (biometric scan)
- Supports generations, edits, and masking
- Excellent text rendering in images
- Struggles with realistic face matching (possibly intentional)

### Google I/O Avalanche
| Release | Significance |
|---------|-------------|
| **Gemini 2.5 Pro Deep Think** | 84% on MMMU, 65th percentile on USA Math Olympiad |
| **Gemini 2.5 Flash GA** | Thinking budgets, native audio I/O |
| **Gemini Diffusion** | 2000 tokens/sec for code/math editing |
| **Jules** | Free async coding agent at jules.google |
| **Project Mariner** | Browser control via API (agentic web) |
| **Gemini Ultra tier** | $250/month with DeepThink, VEO3, 30TB storage |
| **AI Mode in Search GA** | Can connect to Gmail/Docs, Deep Search capability |

### Open Source LLMs
| Release | Significance |
|---------|-------------|
| **Phi-4-Reasoning** | 14B hits 78% on AIME 25, MIT licensed |
| **AM-Thinking v1 32B** | Dense model, 85.3% AIME 2024, Apache 2 |
| **Devstral 24B** | Mistral + AllHands collab, SOTA on SWE-bench |
| **Gemma 3n** | 4B MatFormer, mobile-first multimodal |
| **NVIDIA Nemotron 8B/49B** | Reasoning toggle via system prompt |

### Big CO LLMs + APIs
- **OpenAI Codex Agent** - Async GitHub agent, opens PRs, fixes bugs
- **OpenAI hires Jony Ive** - $6.5B deal, "IO" hardware company
- **GitHub Copilot open sourced** - Frontend code now open
- **Microsoft MCP in Windows** - Protocol support at OS level
- **LMArena raises $100M** - a16z seed, impartiality questions raised

### Vision & Video
- **Odyssey Interactive Worlds** - Walk through AI-generated worlds with WASD
- **HunyuanPortrait/Avatar** - Open source competitors to HeyGen/Hedra
- **Wan 2.1** - Alibaba's open source diffusion-transformer video suite
- **Flux Kontext** - SOTA image editing with character consistency

### Voice & Audio
- **ElevenLabs V3** - Emotion tags, 70+ languages, multi-speaker dialogue
- **OpenAI Voice Revolution** - GPT 4.0 Transcribe (promptable ASR), semantic VAD
- **Chatterbox 0.5B** - Open source TTS with emotion control, Apache 2.0
- **Unmute.sh** - KyutAI wrapper adds voice to any LLM

### Tools
- **AlphaEvolve** - Gemini-powered algorithm discovery (0.7% global compute recovery!)
- **Claude Code GA** - Shell-based agent with IDE integrations
- **Cursor V1** - Bug Bot reviews PRs, MCP support

---

## 📅 June 2025 - "Agents & Video Take Over"

### 🎯 Top Stories

#### 💰 **OpenAI o3-pro & 90% Price Drop** (Jun 12)
OpenAI's intelligence push continues:
- **o3 price slashed 80%** ($40/$10 → $8/$2 per million tokens)
- **o3-pro launched** - highest intelligence model, 93% AIME 2024
- 87% cheaper than o1-pro
- 84% on GPQA Diamond, near 3000 ELO on coding
- Same full o3 model, no distillation

#### 🦙 **Meta's $15B Scale AI Power Play** (Jun 12)
Zuck goes all-in on superintelligence:
- **49% stake in Scale AI** for ~$14B
- Alex Wang leads new "Superintelligence team" at Meta
- Hired Google's Jack Rae for alignment
- Seven-to-nine-figure comp packages for researchers
- Clear response to Llama 4's muted reception

#### 🧠 **MiniMax M1 - Reasoning MoE That Beats R1** (Jun 19)
Chinese lab drops powerful open reasoning model:
- **456B total / 45B active** parameters
- Outperforms DeepSeek R1 on multiple benchmarks
- 40K context window
- Full weights available on Hugging Face

#### 🖥️ **Gemini CLI - AI Agent in Your Terminal** (Jun 26)
Google drops open source CLI agent:
- Brings **Gemini 2.5 Pro** to terminal
- Free tier available (with limits on older flash models)
- Full GitHub integration
- Pairs with new MCP support in LM Studio

### Open Source LLMs
| Release | Significance |
|---------|-------------|
| **Mistral Small 3.2** | Improved instruction following, better function calling |
| **Mistral Magistral** | First reasoning model, 24B open, 128K context |
| **Kimi-Dev-72B** | Moonshot's developer-focused model |
| **DeepSeek R1-0528** | Updated reasoner, AIME 91, LiveCodeBench 73, "clearer thinking" |
| **INTELLECT-2 32B** | Globally decentralized RL training from Prime Intellect |

### Big CO LLMs + APIs
- **Gemini 2.5 Pro/Flash GA** - 2.5 Flash-Lite in preview
- **Deep Research API** - OpenAI adds webhook support
- **Anthropic Fair Use ruling** - Judge rules book training is fair use
- **OpenAI Meeting Recorder** - ChatGPT can now record Zoom calls
- **ChatGPT Connectors** - Team accounts get Google Drive, SharePoint, Dropbox

### Vision & Video
- **Seedance 1.0 mini** - ByteDance beats VEO3 on some comparisons
- **MiniMax Hailuo 02** - 1080p native, SOTA instruction following
- **Midjourney Video** - Finally entering video space
- **OmniGen 2** - Open weights for image gen/editing
- **Imagen 4 Ultra** - Google's flagship in Gemini API

### Voice & Audio
- **ElevenLabs 11.ai** - Voice-first personal assistant with MCP
- **Magenta RealTime** - Google's open weights real-time music gen
- **Kyutai Streaming STT** - High-throughput real-time speech-to-text
- **MiniMax Speech** - Tech report confirms best TTS architecture

### Tools
- **Gemini CLI** - Open source terminal agent
- **OpenHands CLI** - Model-agnostic coding agent
- **Warp 2.0** - Agentic Development Environment with multi-threading
- **LM Studio MCP** - Connect local LLMs with MCP servers
- **Cursor Slack** - Coding assistant now in Slack

---

## 📊 Quarter Summary: Major Themes

### 1. 🎬 **Video AI Crosses the Uncanny Valley**
- VEO3 native audio generation (speech, SFX, music synced)
- "Prompt Theory" viral videos question reality itself
- Character/scene consistency finally working
- Midjourney, ByteDance Seedance join Sora/Kling/VEO

### 2. 🧠 **Tool-Using Reasoning Models Emerge**
- o3/o4-mini can call tools during chain-of-thought
- 600+ consecutive tool calls observed
- Image manipulation during reasoning (zoom/crop/rotate)
- This is the closest thing to AGI we've seen

### 3. 🇨🇳 **Open Source Matches Frontier**
- Qwen 3 (Apache 2.0) rivals Sonnet 3.5 on many tasks
- Claude 4 Sonnet hits 80% SWE-bench with PTTC
- DeepSeek R1-0528 keeps pushing open reasoning
- MiniMax M1 beats R1 on several benchmarks

### 4. 📺 **Google I/O Delivers Everything**
- Gemini 2.5 Pro reclaims #1 LLM
- VEO3 steals the show with native audio
- Jules coding agent launches free
- Massive infrastructure (TPU v6e pods, Ultra tier)

### 5. 🤖 **Agent Ecosystem Matures**
- MCP becomes universal standard (OpenAI, Google adopt)
- A2A protocol launches for agent-to-agent communication
- Jules, Codex, GitHub Copilot Agent - async coding goes mainstream
- Gemini CLI brings agents to terminal

### 6. 💸 **AI's Economic Impact Accelerates**
- Meta $15B Scale AI stake
- OpenAI $40B raise at $300B valuation
- o3 price drops 80% in 4 months
- Cursor $9B valuation, Windsurf $3B acquisition

---

## 🏆 Q2 2025: Biggest Releases by Month

### April
1. **OpenAI o3 & o4-mini** - Tool-using reasoning models
2. **GPT-4.1 Family** - 1M token context
3. **Meta Llama 4** - Scout & Maverick (chaotic launch)
4. **Gemini 2.5 Flash** - Controllable thinking budgets
5. **HiDream-I1** - Open source SOTA image gen

### May
1. **VEO3** - Native audio video generation
2. **Claude 4 Opus & Sonnet** - 80% SWE-bench
3. **Qwen 3** - Apache 2.0 reasoning family
4. **Google I/O** - Gemini 2.5 Pro, Jules, Diffusion
5. **Flux Kontext** - SOTA image editing

### June
1. **o3-pro** - Highest intelligence model
2. **o3 Price Drop 80%** - Democratized reasoning
3. **Meta/Scale AI Deal** - $15B superintelligence play
4. **MiniMax M1** - Open reasoning beats R1
5. **Gemini CLI** - Terminal-based AI agent

---

*"We crossed the uncanny valley this quarter. VEO3's native audio had people posting real videos claiming they were AI because they couldn't tell the difference. This isn't just progress - it's a paradigm shift."* - Alex Volkov, ThursdAI

---

*Generated from ThursdAI newsletter content. For full coverage, visit [thursdai.news](https://thursdai.news)*
