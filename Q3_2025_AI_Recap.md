# ThursdAI Q3 2025 - AI Yearly Recap
## The Quarter of GPT-5, Trillion-Parameter Open Source, and World Models

*Based on 12 ThursdAI episodes from July 3 - September 26, 2025*

---

![Q3 2025 ThursdAI Infographic](https://pub-7837090e9353474292fc8c7114c5fa9d.r2.dev/thursdai_infographics/Q3%202025%20ThursdAI%20Q3%20infographic.jpeg)

---

## 🔥 Quarter Overview

Q3 2025 will be remembered as the quarter when **GPT-5 arrived**, **open source hit the trillion-parameter mark** with Kimi K2, and **world models became playable**. Chinese labs continued their open-source dominance with Qwen, DeepSeek, and ByteDance releases, while OpenAI shipped both their flagship GPT-5 and Apache-2.0 licensed GPT-OSS models. Google's Genie-3 showed us the future of interactive generated worlds, and video generation reached "can't tell it's AI" quality.

---

## 📅 July 2025 - "Trillion-Parameter Open Source & Agent Awakening"

### 🎯 Top Stories

#### 🦄 **Kimi K2 - The Trillion-Parameter Open Source King** (Jul 17)
Moonshot dropped a bomb with Kimi K2, a **1 trillion parameter** MoE model:
- **65.8% on SWE-bench Verified** - beating Claude Sonnet without reasoning
- Only **32B active parameters** making it actually runnable
- **128K context** standard (2M+ rumored capability)
- Trained on **15.5 trillion tokens** with the Muon optimizer
- **Modified MIT license** - actually open!
- **SOTA on EQBench creative writing** - finally an open model that writes well!

> "This isn't just another model release. This is 'Sonnet at home' if you have the hardware." - Alex Volkov

#### 🔥 **Grok-4 & Grok Heavy** (Jul 10)
xAI unveiled Grok-4 and a multi-agent swarm called Grok Heavy:
- **50% on Humanity's Last Exam** (with tools) - unprecedented
- **15.9% on ARC-AGI v2** - 2x better than Opus 4
- **100% on AIME25**, 88.9% on GPQA Diamond
- Heavily scaled RL training
- Controversy: "Mechahitler" incident, Grok searching "what does Elon think"

#### 🤖 **OpenAI ChatGPT Agent (Odyssey)** (Jul 17)
OpenAI merged Deep Research + Operator into one agentic system:
- **41.6% on HLE** (double o3), **27.4% on FrontierMath**
- Combines text browser + visual browser + terminal + code execution
- Can browse, code, call APIs, generate images, build spreadsheets
- Wedding planning, sticker ordering demos wowed audiences

#### 🇨🇳 **Chinese Open Source Explosion** (Jul 3)
- **Baidu ERNIE 4.5**: 10 models (424B to 0.3B), Apache 2.0, 128K context, multimodal
- **Tencent Hunyuan-A13B**: 80B MoE (13B active), 256K context from WizardLM team
- **Huawei Pangu Pro MoE**: 72B trained entirely on Ascend NPUs (no Nvidia!)

### Open Source LLMs
| Release | Significance |
|---------|-------------|
| **Qwen3-Coder-480B** (Jul 24) | 69.6% SWE-bench Verified, 7.5T tokens training, 256K context |
| **Qwen3-235B-A22B-Instruct-2507** | 81% MMLU-Redux, 70% LiveCodeBench, hybrid reasoning dropped |
| **DeepSWE-Preview** | 59% SWE-bench-Verified, pure RL on Qwen3-32B |
| **SmolLM3** (3B) | HuggingFace's 11T token pocket model, 256K context |
| **HuggingFace SmolLM3** | Dual reasoning modes, 128K→256K context |
| **LG EXAONE 4.0** (32B) | 81.8% MMLU Pro from LG (the fridge company!) |

### Big CO LLMs + APIs
| Release | Significance |
|---------|-------------|
| **Grok-4 & Heavy** | SOTA on HLE (50%), ARC-AGI v2 (15.9%) |
| **ChatGPT Agent** | Unified agentic AI for real-world tasks |
| **OpenAI/Alphabet IMO Gold** | Both won Gold at International Math Olympiad |
| **White House AI Action Plan** | 90 policy proposals for US AI dominance |

### Vision & Video
- **Wan 2.2**: First MoE video model, 5-second 720p on single 4090, open source
- **Runway Gen-3 Aleph**: Chat-based video editing, scene transformations
- **Runway Act-Two**: Next-gen motion capture (head, face, body, hands)

### Voice & Audio
- **Mistral Voxtral**: SOTA open speech recognition, beats Whisper v3, Apache 2.0
- **Higgs Audio v2**: Beats GPT-4o-mini and ElevenLabs on prosody
- **Riffusion x Producer.ai**: Chatable studio producer

### Tools
- **Perplexity Comet**: AI-powered browser, mouse moves on its own
- **Amazon Kiro**: Spec-driven AI IDE from AWS
- **Liquid AI LEAP + Apollo**: On-device AI platform for mobile

---

## 📅 August 2025 - "GPT-5 Month"

### 🎯 Top Stories

#### 👑 **GPT-5 Launch** (Aug 7)
OpenAI released GPT-5, 32 months after GPT-4:
- **400K context window**
- **$1.25/$10 per million tokens** (Opus is $15/$75)
- Unified thinking + chat model
- Router-based architecture (initially buggy)
- Quiz mode, Gmail integration, memory features
- Free tier access for back-to-school
- But: Writing quality disappointed some, needed prompting guide

> "32 months since GPT-4 release, 32 months of ThursdAI" - Alex Volkov

#### 🔓 **GPT-OSS (120B/20B)** - OpenAI Goes Open Source (Aug 5)
Historic release under Apache 2.0 license:
- 120B and 20B models
- Configurable reasoning via system prompt (`reasoning: high`)
- Function calling, web search, Python execution
- Full chain-of-thought access (unlike GPT-5)
- Mixed reviews: Great at code/math, weak at creative writing

#### 🌍 **Google Genie-3 World Model** (Aug 7)
DeepMind's world model generated **fully interactive 3D environments**:
- Real-time at 24fps
- Single image or text prompt → controllable world
- Paint a wall, turn away, it remembers (memory/consistency breakthrough)
- Walk, fly, control camera in generated worlds

#### 🔀 **DeepSeek V3.1 Hybrid Reasoner** (Aug 21)
DeepSeek released a hybrid that combines V3 + R1:
- Matches/beats R1 with **fewer thinking tokens**
- Tool calls inside thinking process
- 66% SWE-bench Verified (non-thinking) vs R1's 44%
- 128K context, MIT licensed
- TerminalBench: 5.7→31 improvement

### Open Source LLMs
| Release | Significance |
|---------|-------------|
| **DeepSeek V3.1** | Hybrid reasoner, R1-level with less thinking |
| **ByteDance Seed-OSS 36B** | Apache 2, 512K context, "thinking budget" control |
| **NVIDIA Nemotron Nano 9B V2** | Mixed Mamba+Transformer, 6x throughput, open dataset |
| **Cohere Command-A Reasoning** | 111B dense, 256K context, 70% BFCL |
| **GLM-4.5V** | 106B VLM from Zhipu, SOTA vision intelligence |

### Big CO LLMs + APIs
| Release | Significance |
|---------|-------------|
| **GPT-5** | 400K context, unified reasoning, router architecture |
| **GPT-OSS** | Apache 2.0, 120B/20B, full CoT access |
| **Anthropic Opus 4.1** | Pre-emptive upgrade before GPT-5 |
| **Claude Sonnet 1M context** | Extended to 1M in API |

### Vision & Video
- **Hunyuan GameCraft**: Game video generation with physics, runs on 4090
- **Skywork Matrix-Game 2.0**: Real-time world model, 25fps, open source
- **LFM2-VL**: Liquid AI's 440M & 1.6B vision-language models, 2x faster

### AI Art & Diffusion
- **Nano Banana**: Mystery model (rumored Google) doing 3D-aware scene editing
- **Qwen Image Edit (20B)**: Fully open image editor, bilingual, runs locally
- **FLUX.1 Krea [dev]**: Natural aesthetics, no "AI gloss"

### Tools
- **Agents.md Standard**: OpenAI's config file to unify agent instructions
- **Catnip**: W&B's containerized multi-agent coding workspace
- **Cursor gets Sonic**: Mystery "Grok Code" model appears

---

## 📅 September 2025 - "Shiptember Delivers"

### 🎯 Top Stories

#### 🧑‍💻 **GPT-5-Codex** (Sep 18)
OpenAI's agentic coding finetune of GPT-5:
- Works **7+ hours independently** on complex tasks
- **93% fewer tokens** on simple tasks
- Integrated everywhere: CLI, VS Code, web, iPhone
- Reviews majority of OpenAI's own PRs
- Perfect 12/12 on 2025 ICPC with unreleased reasoning model

#### 👓 **Meta Connect 25 - AI Glasses with Display** (Sep 18)
Meta unveiled next-gen Ray-Ban glasses:
- **Built-in display** (invisible from outside)
- **Neural band wristband** for muscle-based control
- Live translation with subtitles in field of view
- Agentic AI doing research tasks
- **$799**, shipping immediately

#### 🐋 **DeepSeek V3.1 Terminus** (Sep 26)
Surgical update fixing agent behavior:
- Fixed code-switching bug ("sudden Chinese")
- Improved tool-use and browser execution
- Less overthinking/stalling in agentic flows
- HLE: 15→21.7 improvement

#### 🦜 **Qwen-mas Strikes Again** (Sep 26)
Alibaba's multimodal blitz:
- **Qwen3-VL-235B**: Vision reasoner, 22B active, 1M context for video
- **Qwen3-Omni-30B**: End-to-end omni-modal (text, image, audio, video), sub-250ms speech
- **Qwen-Max**: Over 1T parameters, 69.6% SWE-bench, roadmap to 100M token context

### Open Source LLMs
| Release | Significance |
|---------|-------------|
| **Qwen3-VL-235B-A22B-Thinking** | Vision reasoner, 1M context for 2-hour video |
| **Qwen3-Omni-30B-A3B** | Real-time omni-modal, 119 languages |
| **Tongyi DeepResearch A3B** | Web agent matching OpenAI Deep Research, 98.6% SimpleQA |
| **Qwen-Next-80B-A3B** | Ultra-sparse MoE, rivals 235B reasoning |
| **Liquid Nanos** | 350M-2.6B models for structured extraction |
| **IBM Granite OCR 258M** | Tiny doc parser, runs on Raspberry Pi |

### Big CO LLMs + APIs
| Release | Significance |
|---------|-------------|
| **GPT-5-Codex** | 7+ hour autonomous coding sessions |
| **Grok-4 Fast** | 2M context, 40% fewer thinking tokens, 1% cost |
| **NVIDIA $100B pledge to OpenAI** | "Biggest infrastructure project in history" |
| **ChatGPT Pulse** | Proactive AI news based on your data |
| **OpenAI-Oracle $300B deal** | $60B/year for compute, 5-year deal |
| **Anthropic $13B raise** | $183B valuation, $5B revenue run rate |
| **Mistral $13.8B valuation** | $1.3B from ASML, Europe's decacorn |

### Vision & Video
- **ByteDance SeeDream 4**: 4K SOTA image gen/editing, up to 6 reference images
- **Lucy 14B**: 5-second video in 6.5 seconds (insane speed)
- **Wan 2.2 Animate**: Motion transfer + lip sync, open source
- **Wan 4.5 Preview**: 1080p 10s with synced speech generation
- **Kling 2.5 Turbo**: 30% cheaper, audio included
- **Ray3**: Luma's "reasoning" video with HDR

### Voice & Audio
- **Suno V5**: "I can't tell anymore" era, human-level vocals
- **Qwen3-ASR-Flash**: 11-language speech recognition with singing
- **Stable Audio 2.5**: 3-minute tracks in <2 seconds

### AI Art & Diffusion
- **Hunyuan SRPO**: New diffusion finetuning method
- **Reve 4-in-1**: Image creation + editing platform
- **FeiFei WorldLabs Marble**: Images → walkable Gaussian Splat 3D worlds

### Tools
- **Google Gemini in Chrome**: Chat across tabs, browse history knowledge
- **ChatGPT full MCP support**: Developer mode for tool connectors
- **Oasis 2.0**: Real-time Minecraft world generation mod

---

## 📊 Quarter Summary: Major Themes

### 1. 🧠 **GPT-5 Era Begins**
- OpenAI unified reasoning + chat into one model
- Router-based architecture for intelligent model selection
- Agentic coding (Codex) works for 7+ hours independently
- GPT-OSS brought open-source from OpenAI (Apache 2.0)

### 2. 🇨🇳 **Open Source Hits Trillion-Scale**
- Kimi K2: 1T parameters, beats Claude Sonnet on SWE-bench
- Qwen3-Coder: 480B, 69.6% SWE-bench
- DeepSeek V3.1: Hybrid reasoning, fewer tokens
- W&B Inference launched to host these monsters

### 3. 🌍 **World Models Become Playable**
- Google Genie-3: Interactive 3D worlds at 24fps
- Hunyuan GameCraft: Game video with physics
- Matrix-Game 2.0: Unreal/GTA-trained, 25fps
- Oasis 2.0: Real-time Minecraft reskinning

### 4. 🎥 **Video Reaches "Can't Tell" Quality**
- SeeDream 4: 4K in <2 seconds
- Lucy 14B: Near-realtime video generation
- Suno V5: Indistinguishable from human music
- Wan 4.5: Speech-synced video generation

### 5. 💰 **Unprecedented Investment**
- NVIDIA $100B pledge to OpenAI
- OpenAI-Oracle $300B deal
- Anthropic $13B raise at $183B valuation
- Meta Superintelligence Labs: $100-300M packages to poached researchers

### 6. 🤖 **Agents Get Serious**
- ChatGPT Agent unifies browser + terminal + research
- Agents.md standardizes agent config
- Desktop agents hit 48% on OSWorld (up from ~12%)
- MCP support spreading everywhere

---

## 🏆 Q3 2025: Biggest Releases by Month

### July
1. **Kimi K2** - 1T parameter open source, 65.8% SWE-bench
2. **Grok-4 & Heavy** - 50% HLE, 15.9% ARC-AGI
3. **ChatGPT Agent** - Unified agentic AI
4. **Qwen3-Coder-480B** - 69.6% SWE-bench
5. **White House AI Action Plan** - US AI strategy

### August
1. **GPT-5** - 400K context, unified reasoning
2. **GPT-OSS** - Apache 2.0, 120B/20B open weights
3. **Google Genie-3** - Playable AI-generated worlds
4. **DeepSeek V3.1** - Hybrid reasoner
5. **Meta Smart Glasses** - Display + neural control

### September
1. **GPT-5-Codex** - 7-hour autonomous coding
2. **NVIDIA $100B pledge** - Biggest AI infrastructure deal
3. **Qwen3-VL + Omni** - Complete multimodal suite
4. **ByteDance SeeDream 4** - SOTA 4K image gen
5. **Anthropic $13B raise** - $183B valuation

---

*"This was the summer of trillion-parameter open source, GPT-5, and world models you can walk in. We're not just accelerating—we're in a completely different phase of AI. Hold on to your butts."* - Alex Volkov, ThursdAI

---

*Generated from ThursdAI newsletter content. For full coverage, visit [thursdai.news](https://thursdai.news)*
