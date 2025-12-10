# ThursdAI Episodes - August 2025

Total Episodes: 4

---

## 📆 ThursdAI - Aug 21 - DeepSeek V3.1’s hybrid upset, ByteDance’s 512K Seed-OSS, Nano Banana wizardry, Agents.md standardizes agents, and more AI

**Date:** August 21, 2025  
**Duration:** 1:06:24  
**Link:** [https://sub.thursdai.news/p/thursdai-aug-21-deepseek-v31s-hybrid](https://sub.thursdai.news/p/thursdai-aug-21-deepseek-v31s-hybrid)

Hey everyone, Alex here 👋

This week looked quiet… until about 15 hours before we went live. Then the floodgates opened: DeepSeek dropped a hybrid V3.1 that beats their own R1 with fewer thinking tokens, ByteDance quietly shipped a 36B Apache-2.0 long-context family with a “thinking budget” knob, NVIDIA pushed a faster mixed-architecture 9B with open training data, and a stealth image editor dubbed “Nano Banana” started doing mind-bending scene edits that feel like a new tier of 3D-aware control. 

On the big-co side, a mystery “Sonic” model appeared in Cursor and Cline (spoiler: the function call paths say a lot), and OpenAI introduced [Agents.md](Agents.md) to stop the config-file explosion in agentic dev tools. We also got a new open desktop-agent RL framework that 4x’d OSWorld SOTA, an IBM + NASA model for solar weather, and Qwen’s fully open 20B image editor that’s shockingly capable and runnable on your own GPU.

Our show today was one of the shortest yet, as I had to drop early to prepare for Burning Man 🔥🕺 Speaking of which, Wolfram and the team will host the next episode! 

Ok, let's dive in! 

DeepSeek V3.1: a faster hybrid that thinks less, scores more ([X](https://x.com/deepseek_ai/status/1958417062008918312), [HF](https://huggingface.co/deepseek-ai/DeepSeek-V3.1))

DeepSeek does this thing where they let a base artifact “leak” onto Hugging Face, and the rumor mill goes into overdrive. Then, hours before we went live, the full V3.1 model card and an instruct variant dropped. The headline: it’s a hybrid reasoner that combines the strengths of their V3 (fast, non-thinking) and R1 (deep, RL-trained thinking), and on many tasks it hits R1-level scores with fewer thinking tokens. In human terms: you get similar or better quality, faster.

A few things I want to call out from the release and early testing:

* Hybrid reasoning mode done right. The model can plan with thinking tokens and then switch to non-thinking execution, so you don’t have to orchestrate two separate models. This alone simplifies agent frameworks: plan with thinking on, execute with thinking off.

* Thinking efficiency is real. DeepSeek shows curves where V3.1 reaches or surpasses R1 with significantly fewer thinking tokens. On AIME’25, for example, R1 clocks 87.5% with ~22k thinking tokens; V3.1 hits ~88.4 with ~15k. On GPQA Diamond, V3.1 basically matches R1 with roughly half the thinking budget.

* Tool-use and search-agent improvements. V3.1 puts tool calls inside the thinking process, instead of doing a monologue and only then calling tools. That’s the pattern you want for multi-turn research agents that iteratively query the web or your internal search.

* Long-context training was scaled up hard. DeepSeek says they increased the 32K extension phase to ~630B tokens, and the 128K phase to ~209B tokens. That’s a big bet on long-context quality at train time, not just inference-time RoPE tricks. The config shows a max position in the 160K range, with folks consistently running it in the 128K class.

* Benchmarks show the coding and terminal agent work got a big push. TerminalBench jumps from a painful 5.7 (R1) to 31 with V3.1. Codeforces ratings are up. On SweBench Verified (non-thinking), V3.1 posts  66 vs R1’s ~44. And you feel it: it’s faster to “get to it” without noodling forever.

* API parity you’ll actually use. Their API now supports the Anthropic-style interface as well, which means a bunch of editor integrations “just work” with minimal glue. If you’re in a Claude-first workflow, you won’t have to rewire the world to try V3.1.

* License and availability. This release is MIT-licensed, and you can grab the base model on Hugging Face. If you prefer hosted, keep an eye on our inference—we’re working to get V3.1 live so you can benchmark without burning your weekend assembling a serving stack.

Hugging Face: [https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Base](https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Base)

Quick personal note: I’m seeing a lot of small, pragmatic improvements add up here. If you’re building agents, the hybrid mode plus tighter tool integration is a gift. DeepSeek V3.1 is going to be deployed to W&B Inference service soon! Take a look here to see when it's ready [wandb.me/inference](http://wandb.me/inference) 

ByteDance Seed-OSS 36B: Apache-2.0, 512K context, and a “thinking budget” knob ([X](https://x.com/yshan783399/status/1958225093915779256), [HF](https://huggingface.co/collections/ByteDance-Seed/seed-oss-68a609f4201e788db05b5dcd), [Github](https://github.com/ByteDance-Seed/seed-oss))

I didn’t see much chatter about this one, which is a shame because this seems like a serious release. ByteDance’s Seed team open-sourced a trio of 36B dense models—two Base variants (with and without synthetic data) and an Instruct model—under Apache-2.0, trained on 12T tokens and built for long-context and agentic use. The context window is a native half-million tokens, and they include a “thinking budget” control you can set in 512-token increments so you can trade depth for speed.

They report strong general performance, long-context RULER scores, and solid code/math numbers for a sub-40B model, with the Instruct variant posting very competitive MMLU/MMLU-Pro and LiveCodeBench results. The architecture is a straightforward dense stack (not MoE), and the models ship with Transformers/vLLM support and 4/8-bit quantization ready to go. If you’ve been hunting for a commercial-friendly, long-context 30-something‑B with an explicit reasoning-control dial, this should be on your shortlist.

A neat detail for the training nerds: two Base releases—one trained with synthetic data, one without—make for a rare apples-to-apples study in how synthetic data shapes base capability. Also worth noting: they previously shipped a Seed-Prover specialized for Lean; it looks like the team is interested in tight domain models and generalists.

NVIDIA Nemotron Nano 9B V2: mixed architecture, open data, and long-context throughput ([X](https://x.com/llm_wizard/status/1957516422520996020), [Blog](https://research.nvidia.com/labs/adlr/NVIDIA-Nemotron-Nano-2/), [HF](https://huggingface.co/collections/nvidia/nvidia-nemotron-689f6d6e6ead8e77dd641615), [Dataset](https://huggingface.co/collections/nvidia/nemotron-pre-training-dataset-689d9de36f84279d83786b35), [Try It](https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2)) 

NVIDIA shipped a fully open release of Nemotron Nano 9B V2—base, base-before-alignment/pruning, and a realigned reasoning model—and, crucially, they published most of the pretraining dataset details (~6.6T tokens across premium web, math, code, and SFT). That level of data transparency is rare and makes this a great base for fine-tuners who want reproducibility.

Under the hood, this is a mixed Mamba+Transformer architecture. NVIDIA is claiming up to 6x higher throughput versus a pure-Transformer peer (they compare to Qwen3-8B) and specifically highlight that they pruned a 12B down to 9B while preserving quality. They also note a single A10 can handle 128K context after compression and distillation passes, which is the kind of practical systems work that matters when you’re running fleets.

A couple of caveats. The license is NVIDIA Open Model License—not Apache-2.0—so read it; it includes restrictions around illegal surveillance and safety bypasses and has revocation clauses. Personally, I appreciate the data openness and the long-context engineering; as always, just make sure the license fits your use case.

If you’re into longer-context math/coding with small models, the numbers (AIME’25, RULER-128K, GPQA) are impressive for 9B. And if you fine-tune: the availability of both pruned and pre-pruned bases plus the dataset recipe is a rare treat.

Cohere’s Command-A Reasoning: dense, multilingual, and research-only licensing ([X](https://x.com/cohere/status/1958542682890047511), [Blog](https://cohere.com/blog/command-a-reasoning), [HF](https://huggingface.co/CohereLabs/command-a-reasoning-08-2025?ref=cohere-ai.ghost.io))

Cohere Dropped a new reasoning model focused on enterprise deployment patterns. It’s dense 111B model, supports a 256K context, and includes very strong multilingual coverage (23 languages is what they called out). What caught my eye: on the BFCL (Berkeley Function-Calling Leaderboard) they show 70%—above DeepSeek R1’s ~63% and GPT-OSS’s ~61%—and they plot the now-familiar test-time compute curves where more thinking tokens yield higher scores.

This release uses Cohere’s non-commercial research license; if you want commercial usage you’ll need to go through them. That said, for teams who need privately deployable, on-prem reasoning and can work under a research license for prototyping, it’s a serious option. A meta observation from the show: there’s accumulating evidence that more active parameters help multi-hop tool-use chains compared to very sparse MoE at similar effective capacity. This model nudges in that direction.

Desktop agents leap: ComputerRL hits 48% on OSWorld ([Paper](https://arxiv.org/abs/2508.14040))

A new framework dubbed ComputerRL from [Z.ai](http://Z.ai) and folks at Tsingua Uni, unified API calls with GUI actions and scaled RL across fleets of virtual desktops, posting a 48.1% success rate on OSWorld versus ~12% for earlier open models. The training system spins up thousands of qemu-in-docker VMs via gRPC; the learning loop alternates RL with supervised fine-tuning and uses a clean step-level binary reward to simplify credit assignment. If you care about practical desktop automation across Ubuntu/Windows/macOS, this is a big jump.

IBM + NASA’s Surya: open model for solar weather ([HF](https://huggingface.co/nasa-ibm-ai4science/Surya-1.0))

Scientists get some love: IBM and NASA open-sourced Surya, a transformer trained on nine years of multi-instrument observations (nearly 200 TB) to forecast solar dynamics and space weather—the stuff that can knock satellites and power grids sideways. It’s on Hugging Face, it’s actually runnable, and it’s a fantastic example of open models delivering real-world scientific utility.

Smaller but notable: InternLM and OpenCUA, plus Intel’s quants

Two quick flags from the “worth your time” pile. InternLM shipped [S1 Mini](https://x.com/intern_lm/status/1958479430361461008), an 8B vision+language model (ViT on top) that’s multimodal and lightweight; if you need on-device omni-ish behavior on a laptop or tablet, give it a look. And [OpenCUA](https://x.com/xywang626/status/1956400403911962757) 32B (Qwen-based) is a specialized computer-usage agent with strong scores; if you’re building automations that need native OS control, it’s worth benchmarking.

Also, if you’re running 4-bit: the Intel quantization work is excellent right now. Their 4-bit quants have been extremely high precision in my testing, especially for large coders and reasoners like DeepSeek V3.1. It’s an easy win if you’re trying to squeeze a 30B+ onto a workstation without hemorrhaging quality.

Big-co updates and platform shifts

Sonic appears in Cursor and Cline

If you open Cursor or fire up Cline, you may see a new “Sonic” model toggle. It’s labeled as a reasoning model and, when you poke the function-calling internals, the call paths include “xai/…” strings. Folks report it’s fast and solid for coding. No official docs yet, but I’d be surprised if this isn’t Grok Code in pre-release clothes.

Agents.md: one file to rule your agents

Agentic dev stacks have multiplied config files like gremlins: Cursor’s rules.json, Windsurf’s prompts, MCP server manifests, tool schemas, install scripts… and every tool wants a different filename and format. OpenAI’s [Agents.md](Agents.md) is a strong attempt at standardization. It’s just Markdown at repo root that says, “here’s how to set up, build, test, and run this project,” plus any agent-specific caveats. Tools then auto-detect and follow your instructions instead of guessing.

It’s already supported by OpenAI Codex, Amp, Jules, Cursor, RooCode, and more, with tens of thousands of public repos adopting the pattern. In monorepos, the nearest [Agents.md](Agents.md) wins, so you can override at the package level. And human chat instructions still override the file’s guidance, which is the right default.

GPT‑5 context truncation in the web UI ([reports](https://x.com/pvncher/status/1958289479283650741))

There’s been a wave of reports that GPT‑5 in the web UI is truncating long prompts even when you’re under the documented context limit. The folks at Repo Prompt reproduced this multiple times and got confirmation from OpenAI that it’s a bug (not a deliberate nerf). If you saw GPT‑5 suddenly forget the bottom half of your carefully structured system prompt in the web app, this likely explains it. The API doesn’t seem affected. Fingers crossed for a quick fix—GPT‑5 is still the best model I’ve used for 300k‑token “read the whole repo and propose a plan” tasks.

Image and 3D: Nano Banana and Qwen’s open image editor

Nano Banana: 3D-consistent scene editing from thin air

A stealth model nicknamed “Nano Banana” surfaced in a web demo and started doing the kind of edits you’d normally expect from a 3D suite with a modeler at the controls. Take two photos—your living room and a product shot—and it composites the object into the scene with shockingly consistent lighting and geometry. Ask for a 3D mesh “five inches off the skin,” and the mesh really does offset. Ask for a new camera angle on a single still, and it renders the scene from above with plausible structure. People have been calling it a game-changer and, for once, it doesn’t feel like hyperbole.

There’s a strong whiff of 3D world modeling under the hood—some volumetric representation or neural field that enables true view synthesis—and Logan Kilpatrick posted a banana emoji that set speculation on fire. We’ll see where it lands and under what license, but for now the demo has been doing the rounds and it is… wow.

If you’re wondering where to try it: LMarena is the currently only way to give it a try, but it's supossedly dropping soon! 

Qwen Image Edit (20B): fully open and already practical ([X](https://twitter.com/Alibaba_Qwen/status/1957500569029079083), [HF](https://huggingface.co/Qwen/Qwen-Image-Edit))

Qwen shipped a 20B image-editing model layered on their existing vision stack, and it’s properly open (permissive license) with strong bilingual text editing in Chinese and English. It handles high-level semantic edits (pose adjustments, rotations, style/IP creation) and low-level touch-ups (add/remove/insert). You can swap objects, expand aspect ratios, keep character identity consistent across panels, and do clean style transfer. It runs locally if you’ve got a decent GPU.

What I appreciate here is the precision. Product placement tasks like “put this book in this person’s hand at this angle,” or “make the shoes match the dress” come out with the kind of control that used to require hand masking and a dozen passes. And yes, the capybara mascot is back in the release materials, which made my day! 👏

If Nano Banana is the closed-world demo of what’s “beyond SOTA,” Qwen Image Edit is the open tool you can actually ship with today.

This week’s buzz from Weights & Biases

Two quick updates from our side. First, we’re working to bring DeepSeek V3.1 to our inference as fast as we can so you can run serious benchmarks without fussing over serving stacks. Keep an eye on our channels; we’ll shout when it’s live and we’ll have some credits for early feedback.

Second, our cofounder Chris Van Pelt released Catnip, a containerized multi‑agent coding workspace that runs multiple Claude Code sessions (or other agents) in isolated sandboxes, each with its own context and notification stream. If you’ve been juggling parallel coding agents that step on each other’s toes, this is catnip indeed.

Catnip Github: [https://github.com/wandb/catnip](https://github.com/wandb/catnip)

Closing thoughts

A year ago, “thinking tokens” weren't even a curiosity; We only got the first whiff of "reasoning" back in September, and now we’re watching hybrid models that do more with less thinking, tool calls woven inside the reasoning loop, and long-context training regimes scaled up by an order of magnitude. The agent stack is maturing fast—desktop RL is finally clearing real tasks; editor ecosystems are converging on a single config file; and even the stealth drops are clearly building toward world-model‑aware editing and control.

If you only try two things this week: run DeepSeek V3.1 in both modes (planning with thinking on, execution with thinking off) and throw a complex multi-step tool workflow at it; then take Qwen Image Edit for a spin on a real product-placement or character-consistency task. You’ll feel the future in your hands.

I’m off to the desert next week for a bit (no internet where I’m going), but Wolfram and the crew will keep the ship on course. If you’re at Burning Man, DM me—would love to say hi out there. As always, thank you for tuning in and nerding out with us every week.

— Alex

TL;DR and show notes

ThursdAI - Aug 21, 2025 - TL;DR

ThursdAI - Aug 21, 2024 - TL;DR

TL;DR of all topics covered:

* **Hosts and Guests**

* [**Alex Volkov**](http://x.com/@altryne) - AI Evangelist & Weights & Biases

* **Co Hosts** - [@WolframRvnwlf](http://x.com/@WolframRvnwlf), [@yampeleg](http://x.com/@yampeleg), [@nisten](http://x.com/@nisten), [@ldjconfirmed](http://x.com/@ldjconfirmed)

* **Open Source LLMs // Papers**

* **ByteDance Seed-OSS** - 36B open-source LLM family ([X](https://x.com/gm8xx8/status/1958258474154143923), [HF](https://huggingface.co/collections/ByteDance-Seed/seed-oss-68a609f4201e788db05b5dcd), [GitHub](https://github.com/ByteDance-Seed/seed-oss))

* **DeepSeek V3.1** - Updated Hybrid model ([HF](https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Base))

* **Cohere CMD-a Reasoning - **([X](https://x.com/cohere/status/1958542682890047511), [Blog](https://cohere.com/blog/command-a-reasoning), [HF](https://huggingface.co/CohereLabs/command-a-reasoning-08-2025?ref=cohere-ai.ghost.io))

* **Zai/Tsinghua ComputerRL** - Framework for desktop agents ([X](https://x.com/Zai_org/status/1958175133706891613), [Paper](https://arxiv.org/abs/2508.14040), [Benchmark](https://os-world.github.io))

* **IBM & NASA Surya** - Solar weather prediction ([HF](https://huggingface.co/nasa-ibm-ai4science/Surya-1.0))

* **NVIDIA Nemotron Nano 9B V2 - **([X](https://x.com/llm_wizard/status/1957516422520996020), [Blog](https://research.nvidia.com/labs/adlr/NVIDIA-Nemotron-Nano-2/), [HF](https://huggingface.co/collections/nvidia/nvidia-nemotron-689f6d6e6ead8e77dd641615), [Dataset](https://huggingface.co/collections/nvidia/nemotron-pre-training-dataset-689d9de36f84279d83786b35), [Try It](https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2)) 

* **Alibaba Quark Med**

* **Big CO LLMs + APIs**

* **Sonic Stealth Model** - Likely Grok Code

* **OpenAI **[**agents.md**](agents.md) - Unified agent files ([agents.md](https://agents.md))

* **GPT-5 Nerf**

* **AI Art & Diffusion & 3D**

* **Nano Banana** - Image model (rumored Google)

* **Qwen-Image-Edit** - 20B Image editing ([X](https://x.com/Alibaba_Qwen/status/1957500569029079083), [HF](https://huggingface.co/Qwen/Qwen-Image-Edit))

* **This weeks Buzz**

* **Catnip** - Containerized AI agent runner ([GitHub](https://github.com/wandb/catnip)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-aug-21-deepseek-v31s-hybrid/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-aug-21-deepseek-v31s-hybrid?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3MTU5MTYyNSwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.GzhggMq7eqrzUXFXtvXqPZNhj2eE7s-nKFKsMRdX-58&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Aug 14 - A week with GPT5, OSS world models, VLMs in OSS, Tiny Gemma & more AI news

**Date:** August 15, 2025  
**Duration:** 1:29:41  
**Link:** [https://sub.thursdai.news/p/thursdai-aug-14-a-week-with-gpt5](https://sub.thursdai.news/p/thursdai-aug-14-a-week-with-gpt5)

Hey everyone, Alex here 👋

Last week, I tried to test GPT-5 and got really surprisingly bad results, but it turns out, as you'll see below, it's partly because they had a bug in the router, and partly because ... well, the router itself! See below for an introduction, written by GPT-5, it's actually not bad?

Last week was a whirlwind. We live‑streamed GPT‑5’s “birthday,” ran long, and then promptly spent the next seven days poking every corner of the new router‑driven universe.

This week looked quieter on the surface, but it actually delivered a ton: two open‑source world models you can drive in real time, a lean vision‑language model built for edge devices, a 4B local search assistant that tops Perplexity Pro on SimpleQA, a base model “extraction” from GPT‑OSS that reverses alignment, fresh memory features landing across the big labs, and a practical prompting guide to unlock GPT‑5’s reasoning reliably.

We also had Alan Dao join to talk about Jan‑v1 and what it takes to train a small model that consistently finds the right answers on the open web—locally.

Not bad eh? Much better than last time 👏 Ok let's dive in, a lot to talk about in this "chill" AI week (show notes at the end as always) first open source, and then GPT-5 reactions and then... world models!

00:00 Introduction and Welcome

00:33 Host Introductions and Health Updates

01:26 Recap of Last Week's AI News

01:46 Discussion on GPT-5 and Prompt Techniques

03:03 World Models and Genie 3

03:28 Interview with Alan Dow from Jan

04:59 Open Source AI Releases

06:55 Big Companies and APIs

10:14 New Features and Tools

14:09 Liquid Vision Language Model

26:18 Focusing on the Task at Hand

26:18 Reinforcement Learning and Reward Functions

26:35 Offline AI and Privacy

27:13 Web Retrieval and API Integration

30:34 Breaking News: New AI Models

30:41 Google's New Model: Gemma 3

33:53 Meta's Dino E3: Advancements in Computer Vision

38:50 Open Source Model Updates

45:56 Weights & Biases: New Features and Updates

51:32 GPT-5: A Week in Review

55:12 Community Outcry Over AI Model Changes

56:06 OpenAI's Response to User Feedback

56:38 Emotional Attachment to AI Models

57:52 GPT-5's Performance in Coding and Writing

59:55 Challenges with GPT-5's Custom Instructions

01:01:45 New Prompting Techniques for GPT-5

01:04:10 Evaluating GPT-5's Reasoning Capabilities

01:20:01 Open Source World Models and Video Generation

01:27:54 Conclusion and Future Expectations

Open Source AI

We've had quite a lot of Open Source this week on the show, including a breaking news from the Gemma team!

Liquid AI's drops LFM2-VL** **([X](https://x.com/ramin_m_h/status/1955332731942174960), [blog](https://www.liquid.ai/blog/lfm2-vl-efficient-vision-language-models), [HF](https://huggingface.co/LiquidAI/LFM2-VL-1.6B))

Let's kick things off with our friends at Liquid AI who released LFM2-VL - their new vision-language models coming in at a tiny 440M and 1.6B parameters.

Liquid folks continue to surprise with speedy, mobile device ready models, that run 2X faster vs top VLM peers. With a native 512x512 resolution (which breaks any image size into 512 smart tiles) and an OCRBench of 74, this tiny model beats SmolVLM2 while being half the size. We've chatted with Maxime from liquid about LFM2 [back in july](https://sub.thursdai.news/i/168031500/liquid-ais-lfm-blazing-fast-models-for-the-edge-𝕏-hugging-face), and it's great to see they are making them multimodal as well with the same efficiency gains!

Zhipu (z.ai) unleashes GLM-4.5V - 106B VLM ([X](https://x.com/Zai_org/status/1954898011181789431), [Hugging Face](https://huggingface.co/zai-org/GLM-4.5V))

In another "previous good model that now has eyes" release, the fine folks from Zhipu continued training thier recently released (and excelled) GLM 4.5-air with a vision encoder, resulting in probably one of the top vision models in the open source!

It's an MoE with only 12B active parameters (106B total) and gets SOTA across 42 public vision-language benches + has a "thinking mode" that reasons about what it sees.

Given that GLM-4.5Air is really a strong model, this is de fact the best visual intelligence in the open source, able to rebuild websites from a picture for example and identify statues and locations!

Jan V1 - a tiny (4B) local search assistant QwenFinetune ([X](https://x.com/jandotai/status/1955176280535732415), [Hugging Face](https://huggingface.co/janhq/Jan-v1-4B))

This one release got a lot of attention, as the folks at Menlo Research (Alan Dao who came to chat with us about Jan on the pod today) released an Apache 2 finetune of Qwen3-4B-thinking, that's focused on SimpleQA.

They showed that their tiny model is beating Perplexity Pro on SimpleQA.

Alan told us on the pod that Jan (the open source [Jan app](https://jan.ai/)) is born to be an open source alternative to searching with local models!

The trick is, you have to enable some source of search data (Exa, Serper, Tavily) via MCP and then enable tools in Jan, and then.. you have a tiny, completely local perplexity clone with a 4B model!

Google drops Gemma 3 270M ([blog](https://t.co/E0BB5nlI1k))

In some #breakingNews, Google open sourced a tiny (270M) parameters, "good at instruction following" Gemma variant. This joins models like SmolLM and LFM2 in the "smol models" arena, being only 300MB, you can run this.. on a toaster. This one apparently also fine-tunes very well while being very energy efficient!

Big Companies (AKA OpenAI corner this past 2 weeks)

Ok ok, we're finally here, a week with GPT-5! After watching the live stream and getting access to GPT-5, my first reactions were not great. Apparently, so have other peoples, and many folks outcried and complained about the model, some even yelling "AGI is cancelled".

What apparently happened is (and since, been fixed by OpenAI) is that GPT-5 wasn't just a model that launched, it was a "smart" router between a few models, and not only did they have a routing bug, the basic GPT-5 model, the one without thinking, is... not great.

But the thinking GPT-5, the one that the router refused to send me to, is really good (as confirmed independently by [multiple evals](https://x.com/shai_s_shwartz/status/1955968602978320727) at this point)

For one, it's the most accurate function calling model on OpenRouter

It's also one of the best on this new FormulaOne benchmark that was just launched

You're prompting it wrong!

Apparently, not only is GPT-5 more intelligent, it's also significantly "surgical" in instruction following, and so, for many folks, just replacing GPT-5 into their tools or prompts didn't just "work", as this model, more than before, is sensitive to conflicting things in the prompt.

OpenAI has released a [guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide#optimizing-intelligence-and-instruction-following) for prompting the model, mostly aimed at developers (as users shouldn't be learning to prompt as models get more intelligent) + they also released a [prompt optimizer](https://platform.openai.com/chat/edit?models=gpt-5&optimize=true)! Just dump your long and complex prompts in there, and you'll get an updated prompt with explanations of why they changed what they changed!

Model Picker (and legacy models) are back!

So, OpenAI tried and super quickly reversed course on removing the "model picker". At first, it was only GPT-5 there, but many people complained about the abrupt removal of 4o, their .. favorite models. At first, OpenAI added back the models via a hidden setting, and later, they have added 4o back to everyone by default, while increasing the reasoning quota to 3000 messages per week!

Generally, my thoughts are, if you've tried GPT-5 and weren't impressed, give it another go! (especially now that it's connected to Gmail [in chats](https://x.com/altryne/status/1955386020909981905)!)

Other notable Big Company updates

In other news, Claude has extended the context window of Sonnet to 1M in the API, and apparently both Claude and Gemini have been adding memory features!

Grok video has been catching up and is now free for a while to all users

**This Week's Buzz: Weave DX improvements**

Quick update from my day job at Weights & Biases - we've rolled out some quality-of-life improvements to Weave, our LLM observability platform. We now have a unified assets tab where you can manage all your prompts, models, and datasets with full versioning support.

Prompts are being version tracked, so if you use that GPT-5 prompt optimizer, we'll store all the previous revisions for ya!

The coolest addition? Threads! Perfect for tracking agent executions or grouping related API calls. You just add a thread_id to your traces and Weave handles the rest. If you're building AI applications and not tracking everything, you're flying blind - give Weave a try at [wandb.me/weave!](http://wandb.me/weave!)

World models are getting... open sourced!

I still think that Google's Genie-3 release from last week was maybe the more important one, though we didn't really get to play with it yet!

And while getting excited by world models, I was thinking that it's goig to take a while for Open Source to catch up. But this week, not 1, but two world models were open sourced, making me think that we'll get to generated worlds quicker than I expected and the race has begun!

Skywork's Matrix-Game 2.0 ([project](https://matrix-game-v2.github.io/), [HF](https://huggingface.co/Skywork/Matrix-Game-2.0))

Matrix-game 2 is a auto-regressive diffusion model, that was trained on 1200 hours of Unreal Engine and GTA-5 environments that runs at 25 frames per second!

It works by creating an "action injection module" that embeds the mouse/keyboard inputs into the generation, enabling frame-level controls.

Hunyuan open-sources GameCraft for real-time, high-dynamic game video generation ([X](https://twitter.com/TencentHunyuan/status/1955839140173631656), [Hugging Face](https://huggingface.co/tencent/Hunyuan-GameCraft-1.0))

Two world-models (well, game models) in the same week? Tencent (who had Hunyuan video before) have trained a game engine on top of their excellent HY-video and have shown the same examples, of building a full world based on a few images.

Their pipeline trained on 1M game play clips from AAA titles, and they also map W/A/S/D and mouse signals into continuous camera/action embeddings, allowing for control and angle creation.

The cool thing? A quantized 13B version supposedly can run on a RTX 4090!

Funnily, they already had Matrix-Game (the one that came out a few days before) benchmarked and beat on the release today!

**Genie 3 is not messing around**

While all the open source is impressive, I was… absolutely blown away by this video from an artist who got the Genie3 team to extend a video of his. Just look at the collision of the plane with the sphere, out of nowhere, Genie3 adds a shadow, and then collision mechanics, the plane bouncing off, and even the jet trails subside and then resume! It really really is crazy to imagine that no prompting was given and the model just.. knew how to do this!

Phew, that was a lot! Much more as always on the actual show, despite it being a "quiet" week by summer of 2025 standards, there was a LOT of open source releases and GPT-5 situation shows that even OpenAI can stumble on new tech releases!

Keep the feedback coming - find me on Twitter/X at @altryne or email the show. And remember, if you want to catch all the technical details and demos, the video version on YouTube has everything the podcast can't show.

Until next week, keep tinkering, keep questioning, and keep pushing the boundaries of what's possible with AI!

See you next ThursdAI 🚀

TL;DR - All Topics Covered

Hosts and Guests

* **Alex Volkov** - AI Evangelist @ Weights & Biases (@altryne)

* Co-hosts: @WolframRvnwlf, @yampeleg, @nisten, @ldjconfirmed

* Guest: Alan Dao from Jan (@jandotai)

Open Source LLMs

* **Liquid AI LFM2-VL**: 440M & 1.6B vision-language models with 2x GPU speedup ([Blog](https://www.liquid.ai/blog/lfm2-vl-efficient-vision-language-models), [HF](https://huggingface.co/LiquidAI/LFM2-VL-1.6B))

* **Jan V1**: 4B parameter search assistant beating Perplexity Pro on SimpleQA ([X](https://x.com/jandotai/status/1955176280535732415), [HF](https://huggingface.co/janhq/Jan-v1-4B))

* **GPT-OSS Base**: Reverse-engineered base model from Jack Morris ([X Thread](https://x.com/jxmnop/status/1955436067353502083))

* **Gemma 3**: Google's 270M parameter model with strong instruction following ([HF](https://huggingface.co/google/gemma-3))

* **Meta Dino v3**: Self-supervised vision model for segmentation ([Blog](https://ai.meta.com/blog/dino-v3))

Big Companies & APIs

* **Mistral Medium 3.1**: New model on Mistral platform

* **Gemini & Claude**: Added memory/personalization features

* **GPT-5 Updates**: Router fixes, model selector returned, prompting guide released ([Guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide), [Optimizer](https://platform.openai.com/chat/edit?models=gpt-5&optimize=true))

* **Claude Sonnet 4**: 1M token context window ([Announcement](https://www.anthropic.com/news/claude-sonnet-4-long-context))

This Week's Buzz

* Weave updates: Unified assets tab and threads for agent tracking

* New features for LLM observability and evaluation

Vision & Video

* **Hunyuan Large Vision**: 1B vision encoder + 389B MoE language model ([Project](https://vision.hunyuan.tencent.com/en))

* **GLM-4.5V**: 106B open source VLM from Zhipu AI ([X](https://x.com/Zai_org/status/1954898011181789431), [HF](https://huggingface.co/zai-org/GLM-4.5V))

World Models

* **Matrix Game 2.0**: Real-time interactive world model, 25fps generation ([Project](https://matrix-game-v2.github.io/), [HF](https://huggingface.co/Skywork/Matrix-Game-2.0))

* **Hunyuan GameCraft**: Game video generation with physics understanding ([X](https://twitter.com/TencentHunyuan/status/1955839140173631656), [HF](https://huggingface.co/tencent/Hunyuan-GameCraft-1.0))

Tools

* **Grok**: Now includes video generation for all users

* **Jan Desktop App**: Local AI with MCP support and search capabilities 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-aug-14-a-week-with-gpt5/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-aug-14-a-week-with-gpt5?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3MTAxNzQxMCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.pxMyGjsrWz64g6XKLLb5Na_iHlkmGXjpy7cObXEjbA4&utm_campaign=CTA_5).

---

## 📅 ThursdAI - GPT5 is here

**Date:** August 07, 2025  
**Duration:** 2:56:19  
**Link:** [https://sub.thursdai.news/p/thursdai-gpt5-is-here](https://sub.thursdai.news/p/thursdai-gpt5-is-here)

Hey folks 👋 Alex here, writing to you, from a makeshift recording studio in an Eastern European hookah bar, where I spent the last 7 hours. Why you ask? Well, when GPT-5 drops, the same week as OpenAI dropping the long awaited OSS models + Google is shipping perfect memory World Models (Genie 3) and tons of other AI drops, well I just couldn't stay away from the stream.

Vacation or not, ThursdAI is keeping you up to date (for 32 months straight, which is also the time since the original GPT-4 release which gave this show its name!)

So, what did we have today on the stream? Well, we started as usual, talking about the AI releases of the week, as if OpenAI dropping OSS models (apache 2) 120B and 20B is "usual". We then covered incredible releases like Google's World model Genie3 (more on this next week!) and Qwen-image + a few small Qwens.

We then were VERY excited to tune in, and watch the (very long) announcement stream from OpenAI, in which they spent an hour to tell us about GPT-5.

This was our longest stream by far (3.5 hours, 1hr was just OpenAI live stream) and I'm putting this here mostly unedited, but chapters are up so feel free to skip to the parts that are interesting to you the most.

00:00 Introduction and Special Guests

00:56 Twitter Space and Live Streaming Plans

02:12 Open Source AI Models Overview

03:44 Qwen and Other New AI Models

08:59 Community Interaction and Comments

10:01 Technical Deep Dive into AI Models

25:06 OpenAI's New Releases and Benchmarks

38:49 Expectations and Use Cases for AI Models

40:03 Tool Use vs. Deep Knowledge in AI

41:02 Evaluating GPT OSS and OpenAI Critique

42:29 Historical and Medical Knowledge in AI

51:16 Opus 4.1 and Coding Models

55:38 Google's Genie 3: A New World Model

01:00:43 Kitten TTS: A Lightweight Text-to-Speech Model

01:02:07 11 Labs' Music Generation AI

01:08:51 OpenAI's GPT-5 Launch Event

01:24:33 Building a French Learning Web App

01:26:22 Exploring the Web App Features

01:29:19 Introducing Enhanced Voice Features

01:30:02 Voice Model Demonstrations

01:32:32 Personalizing Chat GPT

01:33:23 Memory and Scheduling Features

01:35:06 Safety and Training Enhancements

01:39:17 Health Applications of GPT-5

01:45:07 Coding with GPT-5

01:46:57 Advanced Coding Capabilities

01:52:59 Real-World Coding Demonstrations

02:10:26 Enterprise Applications of GPT-5

02:11:49 Amgen's Use of GPT-5 in Drug Design

02:12:09 BBVA's Financial Analysis with GPT-5

02:12:33 Healthcare Applications of GPT-5

02:12:52 Government Adoption of GPT-5

02:13:22 Pricing and Availability of GPT-5

02:13:51 Closing Remarks by Chief Scientist Yakob

02:16:03 Live Reactions and Discussions

02:16:41 Technical Demonstrations and Comparisons

02:33:53 Healthcare and Scientific Advancements with GPT-5

02:47:09 Final Thoughts and Wrap-Up

---

My first reactions to GPT-5

Look, I gotta keep it real with you, my first gut reaction was, hey, I'm on vacation, I don't have time to edit and write the newsletter (EU timezone) so let's see how ChatGPT-5 handles this task. After all, OpenAI has removed all other models from the dropdown, it's all GPT-5 now. (pricing from the incredible writeup by [Simon Willison](https://substack.com/profile/5753967-simon-willison) available [here](https://simonwillison.net/2025/Aug/7/gpt-5/))

And to tell you the truth, I was really disappointed! GPT seems to be incredible at coding benchmarks, with 400K tokens and incredible pricing (just $1.25/$10 compared to Opus $15/$75) this model, per the many friends who got to test it early, is a beast at coding! Readily beating opus on affordability per token, switching from thinking to less thinking when it needs to, it definitely seems like a great improvement for coding and agentic tasks.

But for my, very much honed prompt of "hey, help me with ThursdAI drafts, here's previous drafts that I wrote myself, mimic my tone" it failed.. spectacularly!

Here's just a funny example, after me replying that it did a bad job:

It literally wrote "I'm Alex, I build the mind, not the vibe" 🤦‍♂️ What.. the actual...

For comparison, here's o3, with the same prompt, with a fairly true to tone draft:

High taste testers take on GPT-5

But hey, I have tons of previous speakers in our group chats, and many of them who got early access (I didn't... OpenAI, I can be trusted lol) rave about this model. They are saying that this is a huge jump in intelligence.

Folks like Dr Derya Unutmaz, who jumped on the live show and described how GPT5 does incredible things with less hallucinations, folks like Swyx from [Latent.Space](https://substack.com/profile/89230629-latentspace) who had [early access](https://www.latent.space/p/gpt-5-review) and even got invited to give first reactions to the OpenAI office, and [Pietro Schirano](https://x.com/skirano/status/1953516768317628818) who also showed up in an OpenAI video.

So definitely, definitely check out their vibes, as we all try to wrap our heads around this new intelligence king we got!

Other GPT5 updates

OpenAI definitely cooked, don't get me wrong, with this model plugging into everything else in their platform like memory, voice (that was upgraded and works in custom GPTs now, yay!), canvas and study mode, this will definitely be an upgrade for many folks using the models.

They have now also opened access to GPT-5 to free users, just in time for schools to reopen, including a very interesting Quiz mode (that just showed up for me without asking for it), and connection to Gmail, all those will now work with GPT5.

It now has 400K context, way less hallucinations but fewer refusals also, and the developer upgrades like a new verbosity setting and a new "minimal" reasoning setting are all very welcome!

OpenAI finally launches gpt-oss (120B / 20B) apache 2 licensed models ([model card](https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf), HF)

It was really funny, on the stream Nisten talked about the open source models OpenAI dropped, and said "when we covered it last week", while it was just two days ago! It really does feel like this world is moving really fast.

OpenAI's long promised open source models are here, and they got a fairly mixed bag of reviews from folks. Many folks are celebrating that the western world is now back in the game, releasing incredible local models, with an open license!

Though, after the initial excitement, the vibes are split on these models. Folks are saying that maybe these were trained with only synthetic data, because, like Phi, they seem to be very good at benchmarks, and on the specific tasks they were optimized for (code, math) but [really bad](https://x.com/sam_paech/status/1952839665670922360) at creative writing (Sam Paech from EQBench was not impressed), they are also not multilingual, though OpenAI did release a cookbook [on finetuning](https://cookbook.openai.com/articles/gpt-oss/fine-tune-transfomers) with HuggingFace!

Overall, these models are trained for agentic workflows—supporting function calling, web search, Python execution, configurable reasoning effort, and full raw chain-of-thought access, which we will never get from GPT5.

I particularly love the new approach, where a reasoning effort can be defined directly via the system prompt, by just adding "reasoning: high" to the system prompt, this model will reason for way longer! Can't wait to get back and bench these and share with you.

Overall, the fine-tuning and open source community is split for now, but it's been only a few days, so we'll keep you up to date on how well these models land, regardless, this was a historic week for OpenAI!

Speaking of open models, did you have a chance to try our W&B Inference? The team worked hard to bring these new models to you in record time and incredible pricing (just $.05 for 20B and $.15 for 120B!), these models are definitely worth giving a try!

Plus, if you comment "OSS Power" on our [announcement post](https://x.com/weights_biases/status/1952885962641699287), we'll likely give you a few credits to try it out and let us know what you think!

World models "holy crap" moment - Google Genie3

The other very important release this week was.... not a release at all, but an announcement from Deepmind, with Genie3.

This World Model takes a single image or text prompt and creates a fully interactive, controllable 3D environment that runs in real-time at 24fps. An environment you as a user can control, walk (or fly) in, move around the camera view. It's really mindblowing stuff.

We've covered world models like Mirage on previous episodes, but what Google released is a MAJOR step up in coherency, temporal consistency and just overall quality!

The key breakthrough here is consistency and memory. In one demo, a user could "paint" a virtual wall, turn away, and when they turned back, the paint was still there. This is a massive step towards generalist agents that can train, plan, and reason in entirely simulated worlds, with huge implications for robotics and gaming.

We’re hoping to have the Genie 3 team on the show next week to dive even deeper into this incredible technology!!

Other AI news this week

This week, the "other" news could have filled a full show 2 years ago, we got Qwen keeping the third week of releases with 2 new tiny models + a new diffusion model called Qwen-image ([Blog](https://qwenlm.github.io/blog/qwen-image/), [HF](https://huggingface.co/Qwen/Qwen-Image))

Anthropic decided to pre-empt the GPT5 release, and upgraded Opus 4 and gave us Opus 4.1 with a slight bump in specs.

ElevenLabs released a music API called ElevenMusic, which sounds very very good (this on top of last weeks Riffusion + [Producer.ai](http://Producer.ai) news, that I'm still raving about)

Also in voice an audio, a SUPER TINY TTS model called KittenTTS released, with just 15M parameters and a model that's 25MB, it's surprisingly decent at generating voice ([X](https://x.com/divamgupta/status/1952762876504187065))

And to cap it off with breaking news, the Cursor team, who showed up on the OpenAI stream today (marking quite the change in direction from OpenAI + Windsurf previous friendship), dropped their own CLI version of cursor, reminiscent of Claude Code!

PHEW, wow ok this was a LOT to process. Not only did we tune in for the full GPT-5 release, we did a live stream when gpt-oss dropped as well.

On a personal note, I was very humbled when Sam Altman said it was 32 months since GPT-4 release, because it means this was 32 months of ThursdAI, as many of you know, we started live streaming on March 13, 2023, when GPT-4 was released.

I'm very proud of the incredible community we've built (50K views total across all streams this week!), the incredible co-hosts I have, who step up when I'm on vacation and the awesome guests we have on the show, to keep you up to date every week!

So, a little favor to ask, if you find our content valuable, entertaining, the best way to support this pod is upgrade to a paid sub, and share ThursdAI with a friend or two! 👏 See you next week 🫡

 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-gpt5-is-here/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-gpt5-is-here?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3MDM5ODk4MywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.KfVeuojm2eKEFqVLDMnVNisA0fGRe6RMdNkMMXRRzW4&utm_campaign=CTA_5).

---

## 📆 ThursdAI – Jul 31, 2025 – Qwen’s Small Models Go Big, StepFun’s Multimodal Leap, GLM-4.5’s Chart Crimes, and Runway’s Mind‑Bending Video Edits + GPT-5 soon?

**Date:** August 01, 2025  
**Duration:** 1:38:28  
**Link:** [https://sub.thursdai.news/p/thursdai-jul-31-2025-qwens-small](https://sub.thursdai.news/p/thursdai-jul-31-2025-qwens-small)

Woohoo, we're almost done with July (my favorite month) and the Open Source AI decided to go out with some fireworks 🎉

Hey everyone, Alex here, writing this without my own personal superintelligence (more: later) and this week has been VERY BUSY with many new open source releases.

Just 1 hour before the show we already had 4 breaking news releases, a tiny Qwen3-coder, Cohere and StepFun both dropped multimodal SOTAs and our friends from Krea dropped a combined model with BFL called Flux[Krea] 👏 

This is on top of a very very busy week, with Runway adding conversation to their video model Alpha, Zucks' superintelligence vision and a new SOTA open video model Wan 2.2. So let's dive straight into this (as always, all show notes and links are in the end) 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Open Source LLMs & VLMs 

Tons of new stuff here, I'll try to be brief but each one of these releases deserves a deeper dive for sure. 

Alibaba is on 🔥 with 3 new Qwen models this week

Yes, this is very similar to last week, where they have also dropped 3 new SOTA models in a week, but, these are additional ones. 

It seems that someone in Alibaba figured out that after splitting away from the hybrid models, they can now release each model separately and get a lot of attention per model! 

Here's the timeline: 

* **Friday (just after our show)**: Qwen3-235B-Thinking-2507 drops (235B total, 22B active, [HF](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507)) 

* **Tuesday**: Qwen3-30B-Thinking-2507 (30B total, 3B active, [HF](https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507))

* **Today**: Qwen3-Coder-Flash-2507 lands (30B total, 3B active for coding, [HF](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8))

Lets start with the SOTA reasoner, the 235B(A22B)-2507 is absolutely the best reasoner among the open source models.

We've put the model on our inference service (at crazy prices $.10/$.10) and it's performing absolutely incredible on reasoning tasks. 

It also jumped to the top OSS model on Artificial Analysis scores, EQBench, Long Context and more evals. It a really really good reasoning model! 

Smaller Qwens for local use

Just a week ago, we've asked Junyang on our show, about smaller models that folks can run on their devices, and he avoided by saying "we're focusing on the larger models" and this week, they delivered not 1 but 2 smaller versions of the bigger models (perfect for Speculative Decoding if you can host the larger ones that is) 

The most interesting one is the Qwen3-Coder-flash, which came out today, with very very impressive stats - and the ability to run locally with almost 80 tok/s on a macbook! 

So for the last two weeks, we now have 3 Qwens (Instruct, Thinking, Coder) and 2 sizes for each (all three have a 30B/A3B version now for local use) 👏

Z.ai GLM and StepFun Step3 

As we've said previously, Chinese companies completely dominate the open source AI field right now, and this week as saw yet another crazy testament to how stark the difference is! 

We've seen a rebranded Zhipu ([Z.ai](http://Z.ai) previously THUDM) release their new GLM 4.5 - which gives Qwen3-thinking a run for it's money. Not quite at that level, but definitely very close. I personally didn't love the release esthetics, showing a blended eval score, which nobody can replicate feels a bit off. 

We also talked about how StepFun has stepped in (sorry for the pun) with a new SOTA in multimodality, called [Step3](https://stepfun.ai/research/en/step3). It's a 321B MoE (with a huge 38B active param count) that achieves very significant multi modal scores (The benchmarks look incredible: 74% on MMMU, 64% on MathVision) 

Big Companies APIs & LLMs

Well, we were definitely thinking we'll get GPT-5 or the Open Source AI model from OpenAI this week, but alas, the tea leaves readers were misled (or were being misleading). We 100% know that gpt-5 is coming as multiple screenshots were blurred and then deleted showing companies already testing it. 

But it looks like August is going to be even hotter than July, with multiple sightings of anonymous testing models on Web Dev arena, like Zenith, Summit, Lobster and a new mystery model on OpenRouter called Zenith - that some claim are the different thinking modes of GPT-5 and the open source model? 

Zuck shares vision for personalized superintelligence ([Meta](https://meta.com/superintelligence))

In a very "Nat Fridman" like post, Mark Zuckerberg finally shared the vision behind his latest push to assemble the most cracked AI engineers.

In his vision, Meta is the right place to provide each one with personalized superintelligence, enhancing individual abilities with user agency according to their own values. (as opposed to a centralized model, which feels like his shot across the bow for the other frontier labs) 

A few highlights: Zuck leans heavily into the rise of personal devices on top of which humans will interact with this superintelligence, including AR glasses and a departure from a complete "let's open source everything" dogman of the past, now there will be a more deliberate considerations of what to open source. 

**This Week's Buzz: Putting Open Source to Work with W&B**

With all these incredible new models, the biggest question is: how can you actually use them? I'm incredibly proud to say that the team at Weights & Biases had all three of the big new Qwen models—Thinking, Instruct, and Coder—live on **W&B Inference **on day one ([link](http://wandb.me/inference?utm_source=thursdai&utm_medium=referral&utm_campaign=jul31))

And our pricing is just unbeatable. Wolfram did a benchmark run that would have cost him **$150** using Claude Opus. On W&B Inference with the Qwen3-Thinking model, it cost him **22 cents**. That's not a typo. It's a game-changer for developers and researchers.

To make it even easier, a listener of the show, Olaf Geibig, posted a [fantastic tutorial](https://x.com/olafgeibig/status/1949779562860056763) on how you can use our free credits and W&B Inference to power tools like Claude Code and VS Code using LiteLLM. It takes less than five minutes to set up and gives you access to state-of-the-art models for pennies. All you need to do is add [this](https://gist.github.com/olafgeibig/7cdaa4c9405e22dba02dc57ce2c7b31f) config to vllm and run claude (or vscode) through it! 

Give our inference service a try [here](http://wandb.me/inference?utm_source=thursdai&utm_medium=referral&utm_campaign=jul31) and follow our main account [@weights_biases](http://x.com/weights_biases) a follow as we often drop ways to get additional free credits when new models release

Vision & Video models

Wan2.2: Open-Source MoE Video Generation Model Launches ([X](https://x.com/Alibaba_Wan/status/1949827662416937443), [HF](https://huggingface.co/Wan-AI))

This is likely the best open source video model, but definitely the first MoE video model! It came out with text2video, image2video and a combined version. 

With 5 second 720p videos, that can even be generator at home on a single 4090, this is definitely a step up in the quality of video models that are fully open source. 

Runway changes the game again - Gen-3 Aleph model for AI video editing / transformation ([X](https://x.com/blizaine/status/1950007468324491523), [X](https://x.com/runwayml/status/1950180894477529490))

Look, there's simply no denying this, AI video has had an incredible year, from open source like Wan, to proprietary models with sounds like VEO3. And it's not surprising that we're seeing this trend, but it's definitely very exciting when we see an approach like Runway has, to editing. 

This adds a chat to the model, and your ability to edit.. anything in the scene. Remove / Add people and environmental effects, see the same scene from a different angle and a lot more! 

Expect personalized entertainment very soon! 

AI Art & Diffusion & 3D

FLUX.1 Krea [dev] launches as a state-of-the-art open-weights text-to-image model ([X](https://x.com/bfl_ml/status/1950920537741336801), [HuggingFace](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev))

Black Forest Labs teamed with Krea AI for Flux.1 Krea [dev], an open-weights text-to-image model ditching the "AI gloss" for natural, distinctive vibes—think DALL-E 2's quirky grain without the saturation. It outperforms open peers and rivals pros in prefs, fully Flux-compatible for LoRAs/tools. Yam and I geeked over the aesthetics frontier; it's a flexible base for fine-tunes, available on Hugging Face with commercial options via FAL/Replicate. If you're tired of cookie-cutter outputs, this breathes fresh life into generations.

Ideogram Character launches: one-shot character consistency for everyone ([X](https://x.com/ideogram_ai/status/1950255115753095307))

Ideogram's Characters feature lets you upload one pic for instant, consistent variants—free for all, with inpainting to swap into memes/art. My tests nailed expressions/scenes (me in cyberpunk? Spot-on), though not always photoreal. Wolfram praised the accuracy; it's a meme-maker's dream! and they give like 10 free ones so give it a go

Tencent Hunyuan3D World Model 1.0 launches as the first open-source, explorable 3D world generator ([X](https://x.com/TencentHunyuan/status/1949288986192834718), [HF](https://huggingface.co/tencent/HunyuanWorld-1))

Tencent's Hunyuan3D World Model 1.0 is the first open-source generator of explorable 3D worlds from text/image—360° immersive, exportable meshes for games/modeling. ~33GB VRAM on complex scenes, but Wolfram called it a metaverse step; I wandered a demo scene, loving the potential despite edges. Integrate into CG pipelines? Game-changer for VR/creators.

Voice & Audio 

Look I wasn't even mentioning this on the show, but it came across my feed just as I was about to wrap up ThursdAI, and it's really something. Riffusion joined forces producer and using FUZZ-2 they now have a fully Chatable studio producer, you can ask for.. anything you would ask in a studio! 

Here's my first reaction, and it's really fun, I think they still are open with the invite code 'STUDIO'... I'm not afiliated with them at all! 

Tools 

Ok I promised some folks we'll add this in,  Nisten went super [viral](https://x.com/nisten/status/1950620243258151122) last week with him using a new open source tool called Crush from CharmBracelet, which is an open version of VSCode and it looks awesome! 

He gave a demo live on the show, including how to set it up to work, with subagents etc. If you're into vibe coding, and using the open source models, def. give Crush a try it's really flying and looks cool! 

Phew, ok, we somehow were able to cover ALLL these releases this week, and we didn’t even have an interview! 

Here’s the TL;DR and links to the folks who subscribed (I’m trying a new thing to promote subs on this newsletter) and see you in two weeks (next week is Wolframs turn again as I’m somewhere in Europe!) 

ThursdAI - July 31st, 2025 - TL;DR

* Hosts and Guests

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](https://x.com/altryne))

* Co Hosts - [@WolframRvnwlf](https://x.com/WolframRvnwlf) [@yampeleg](https://x.com/yampeleg) [@nisten](http://x.com/nisten) [@ldj](https://x.com/ldjconfirmed)

* Open Source LLMs

* Zhipu drops GLM-4.5 355B (A32B) AI model ([X](https://x.com/Zai_org/status/1949831552189518044), [HF](https://huggingface.co/zai-org/GLM-4.5))

* ARCEE AFM‑4.5B and AFM‑4.5B‑Base weights released ([X](https://x.com/LucasAtkins7/status/1950278100874645621), [HF](https://huggingface.co/arcee-ai/AFM-4.5B))

* Qwen is on 🔥 - 3 new models: 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jul-31-2025-qwens-small/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jul-31-2025-qwens-small?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2OTc4OTI5NywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.LRrVKpfASEqA84HAfcEe1oAqMSwECqz4850fTYvAzGw&utm_campaign=CTA_5).

---

