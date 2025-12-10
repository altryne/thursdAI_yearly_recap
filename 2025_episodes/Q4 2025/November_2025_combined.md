# ThursdAI Episodes - November 2025

Total Episodes: 4

---

## 🦃 ThursdAI - Thanksgiving special 25’ - Claude 4.5, Flux 2 & Z-image vs 🍌, MCP gets Apps + New DeepSeek!?

**Date:** November 27, 2025  
**Duration:** 1:21:18  
**Link:** [https://sub.thursdai.news/p/thursdai-thanksgiving-special-25](https://sub.thursdai.news/p/thursdai-thanksgiving-special-25)

Hey ya’ll, Happy Thanskgiving to everyone who celebrates and thank you for being a subscriber, I truly appreciate each and every one of you!

Just wrapped up the third ([1](https://sub.thursdai.news/p/thursdai-thanksgiving-special-openai), [2](https://sub.thursdai.news/p/thursdai-thanksgiving-special-24)) Thanksgiving special Episode of ThursdAI, can you believe November is almost over? 

We had another banger week in AI, with a full feast of AI released, Anthropic dropped the long awaited Opus 4.5, which quickly became the top coding LLM, DeepSeek resurfaced with a math model, BFL and Tongyi both tried to take on Nano Banana, and Microsoft dropped a 7B computer use model in Open Source + Intellect 3 from Prime Intellect! 

With so much news to cover, we also had an interview with Ido Sal & Liad Yosef (their second time on the show!) about MCP-Apps, the new standard they are spearheading together with Anthropic, OpenAI & more! 

Exciting episode, let’s get into it! (P.S - I started generating infographics, so the show became much more visual, LMK if you like them) 

ThursdAI - I put a lot of work on a weekly basis to bring you the live show, podcast and a sourced newsletter! Please subscribe if you find this content valuable!

**Anthropic’s Opus 4.5: The “Premier Intelligence” Returns (**[**Blog**](https://www.anthropic.com/news/claude-opus-4-5)**)**

Folks, Anthropic absolutely *cooked*. After Sonnet and Haiku had their time in the sun, the big brother is finally back. Opus 4.5 launched this week, and it is reclaiming the throne for coding and complex agentic tasks.

First off, the specs are monstrous. It hits **80.9% on SWE-bench Verified**, topping GPT-5.1 (77.9%) and Gemini 3 Pro (76.2%). But the real kicker? The price! It is now $5 per million input tokens and $25 per million output—literally one-third the cost of the previous Opus.

Yam, our resident coding wizard, put it best during the show: “Opus knows a lot of tiny details about the stack that you didn’t even know you wanted... It feels like it can go forever.” Unlike Sonnet, which sometimes spirals or loses context on extremely long tasks, Opus 4.5 maintains coherence deep into the conversation.

Anthropic also introduced a new **“Effort” parameter**, allowing you to control how hard the model thinks (similar to o1 reasoning tokens). Set it to high, and you get massive performance gains; set it to medium, and you get Sonnet-level performance at a fraction of the token cost. Plus, they’ve [added](https://www.anthropic.com/engineering/advanced-tool-use) **Tool Search **(cutting enormous token overhead for agents with many tools) and **Programmatic Tool Calling**, which effectively lets Opus write and execute code loops to manage data.

If you are doing heavy software engineering or complex automations, Opus 4.5 is the new daily driver.

**📱 The Agentic Web: MCP Apps & MCP-UI Standard**

Speaking of MCP updates, Can you believe it’s been exactly one year since the Model Context Protocol (MCP) launched? We’ve been “MCP-pilled” for a while, but this week, the ecosystem took a massive leap forward.

We brought back our friends **Ido and Liad**, the creators of **MCP-UI**, to discuss huge news: MCP-UI has been officially standardized as **MCP Apps**. This is a joint effort adopted by both Anthropic and OpenAI.

**Why does this matter?** Until now, when an LLM used a tool (like Spotify or Zillow), the output was just text. It lost the brand identity and the user experience. With MCP Apps, agents can now render full, interactive HTML interfaces directly inside the chat! 

Ido and Liad explained that they worked hard to avoid an “iOS vs. Android” fragmentation war. Instead of every lab building their own proprietary app format, we now have a unified standard for the “Agentic Web.” This is how AI stops being a chatbot and starts being an operating system.

Check out the standard at [**mcpui.dev**](mcpui.dev).

🦃 The Open Source Thanksgiving Feast

While the big labs were busy, the open-source community decided to drop enough papers and weights to feed us for a month.

Prime Intellect unveils INTELLECT-3, a 106B MoE ([X](https://x.com/PrimeIntellect/status/1993895068290388134), [HF](https://huggingface.co/PrimeIntellect/INTELLECT-3), [Blog](https://www.primeintellect.ai/blog/intellect-3), [Try It](https://chat.primeintellect.ai/))

Prime Intellect releases INTELLECT-3, a 106B parameter Mixture-of-Experts model (12B active params) based on GLM-4.5-Air, achieving state-of-the-art performance for its size—including ~90% on AIME 2024/2025 math contests, 69% on LiveCodeBench v6 coding, 74% on GPQA-Diamond reasoning, and 74% on MMLU-Pro—outpacing larger models like DeepSeek-R1. 

Trained over two months on 512 H200 GPUs using their fully open-sourced end-to-end stack (PRIME-RL async trainer, Verifiers & Environments Hub, Prime Sandboxes), it’s now hosted on Hugging Face, OpenRouter, Parasail, and Nebius, empowering any team to scale frontier RL without big-lab resources. Especially notable is their very detailed [release blog](https://www.primeintellect.ai/blog/intellect-3), covering how a lab that previously trained 32B, finetunes a monster 106B MoE model! 

**Tencent’s HunyuanOCR: Small but Mighty **([X](https://x.com/TencentHunyuan/status/1993202595264131436), [HF](https://huggingface.co/tencent/HunyuanOCR), [Github](https://github.com/Tencent-Hunyuan/HunyuanOCR), [Blog](https://hunyuan.tencent.com/vision/zh))

Tencent released **HunyuanOCR**, a 1 billion parameter model that is absolutely crushing benchmarks. It scored **860 on OCRBench**, beating massive models like Qwen3-VL-72B. It’s an end-to-end model, meaning no separate detection and recognition steps. Great for parsing PDFs, docs, and even video subtitles. It’s heavily restricted (no EU/UK usage), but technically impressive.

**Microsoft’s Fara-7B: On-Device Computer Use**

Microsoft quietly dropped **Fara-7B**, a model fine-tuned from Qwen 2.5, specifically designed for computer use agentic tasks. It hits **73.5% on WebVoyager**, beating OpenAI’s preview models, all while running locally on-device. This is the dream of a local agent that can browse the web for you, click buttons, and book flights without sending screenshots to the cloud.

DeepSeek-Math-V2: open-weights IMO-gold math LLM ([X](https://x.com/simonw), [HF](https://huggingface.co/deepseek-ai/DeepSeek-Math-V2))

DeepSeek-Math-V2 is a 685B-parameter, Apache-2.0 licensed, open-weights mathematical reasoning model claiming gold-medal performance on IMO 2025 and CMO 2024, plus a near-perfect 118/120 on Putnam 2024. 

Nisten did note some limitations—specifically that the context window can get choked up on extremely long, complex proofs—but having an open-weight model of this caliber is a gift to researchers everywhere.

**🐝 This Week’s Buzz: Serverless LoRA Inference**

A huge update from us at **Weights & Biases**! We know fine-tuning is powerful, but serving those fine-tunes can be a pain and expensive. We just launched **Serverless LoRA Inference**.

This means you can upload your small LoRA adapters (which you can train cheaply) to W&B Artifacts, and we will serve them instantly on **CoreWeave** GPUs on top of a base model. No cold starts, no dedicated expensive massive GPU instances for just one adapter.

I showed a demo of a “Mocking SpongeBob” model I trained in 25 minutes. It just adds that SaRcAsTiC tExT style to the Qwen 2.5 base model. You pass the adapter ID in the API call, and boom—customized intelligence instantly. You can get more details [HERE](https://wandb.ai/wandb_fc/llm_tools/reports/Serverless-LoRA-inference-on-W-B-CoreWeave--Vmlldzo5MjUwNzAx) and get started with your own LORA in this [nice notebook](https://wandb.me/lora_nb) the team made! 

🎨 Visuals: Image & Video Generation Explosion

**Flux.2: The Multi-Reference Image Creator from BFL **([X](https://x.com/bfl_ml/status/1993345470945804563), [HF](https://huggingface.co/black-forest-labs/FLUX.2-dev), [Blog](https://bfl.ai/blog/flux-2))

**Black Forest Labs** released **Flux.2**, a series of models including a 32B Flux 2[DEV]. The killer feature here is **Multi-Reference Editing**. You can feed it up to 10 reference images to maintain character consistency, style, or specific objects. It also outputs native 4-megapixel images.

Honestly, the launch timing was rough, coming right after Google’s Nano Banana Pro and alongside Z-Image, but for precise, high-res editing, this is a serious tool.

Tongyi drops **Z-Image Turbo**: 6B single-stream DiT lands sub‑second, 8‑step text‑to‑image ([GitHub](https://github.com/Tongyi-MAI/Z-Image), [Hugging Face](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo))

**Alibaba’s Tongyi Lab** released **Z-Image Turbo**, a 6B parameter model that generates images in *sub-second* time on H800s (and super fast on consumer cards).

I built a demo to show just how fast this is. You know that “[Infinite Craft](https://neal.fun/infinite-craft/)“ game? I hooked it up to Z-Image Turbo so that every time you combine elements (like Pirate + Ghost), it instantly generates the image for “Ghost Pirate.” It changes the game completely when generation is this cheap and fast.

HunyuanVideo 1.5 – open video gets very real

Tencent also shipped **HunyuanVideo 1.5**, which they market as “the strongest open‑source video generation model.” For once, the tagline isn’t entirely hype.

Under the hood it’s an 8.3B‑parameter Diffusion Transformer (DiT) model with a 3D causal VAE in front. The VAE compresses videos aggressively in both space and time, and the DiT backbone models that latent sequence.

The important bits for you and me:

* It generates 5–10 second clips at 480p/720p with good motion coherence and physics.

* With FP16 or FP8 configs you can run it on a single consumer GPU with around 14GB VRAM.

* There’s a built‑in path to upsample to 1080p for “real” quality.

LTX Studio Retake: Photoshop for Video ([X](https://x.com/LTXStudio/status/1993715247031767298), [Try It](https://replicate.com/lightricks/ltx-2-retake))

For the video creators, **LTX Studio** launched **Retake**. This isn’t just “regenerate video.” This allows you to select a specific 2-second segment of a video, change the dialogue (keeping the voice!), change the emotion, or edit the action, all for like $0.10. It blends it perfectly back into the original clip. We are effectively getting a “Director Mode” for AI video where you can fix mistakes without rolling the dice on a whole new generation.

A secret new model on the Arena called Whisper Thunder beats even Veo 3?

This was a surprise of the week, while new video models get released often, Veo 3 has been the top one for a while, and now we’re getting a reshuffling of the video giants! But... we don’t yet know who this video model is from! You can sometimes get its generations at the [Artificial Analysis](https://artificialanalysis.ai/video/arena) video arena here, and the outputs look quite awesome! 

Thanksgiving reflections from the ThursdAI team

As we wrapped up the show, Wolfram suggested we take a moment to think about what we’re thankful for in AI, and I think that’s a perfect note to end on.

Wolfram put it well: he’s thankful for everyone contributing to this wonderful community—the people releasing models, creating open source tools, writing tutorials, sharing knowledge. It’s not just about the money; it’s about the love of learning and building together.

Yam highlighted something I think is crucial: we’ve reached a point where there’s no real competition between open source and closed source anymore. Everything is moving forward together. Even if you think nobody’s looking at that random code you posted somewhere, chances are someone found it and used it to accelerate their own work. That collective effort is what’s driving this incredible pace of progress.

For me, I want to thank Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, and Ilya Polosukhin for the 2017 paper “Attention Is All You Need.” Half Joking! But without the seminal attention is you need paper none of this AI was possible.  But mostly I want to thank all of you—the audience, the co-hosts, the guests—for making ThursdAI what it is.

If you go back and watch our [2024 Thanksgiving episode](https://sub.thursdai.news/p/thursdai-thanksgiving-special-24), or the [one from 2023](https://sub.thursdai.news/p/thursdai-thanksgiving-special-openai), you’ll be shocked at how far we’ve come. Tools that seemed magical a year ago are now just... normal. That’s hedonic adaptation at work, but it’s also a reminder to stay humble and appreciate just how incredible this moment in history really is.

We’re living through the early days of a technological revolution, and we get to document it, experiment with it, and help shape where it goes. That’s something to be genuinely thankful for.

TL;DR and Show Notes

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](https://x.com/altryne))

* Co-Hosts - [@WolframRvnwlf](https://x.com/WolframRvnwlf) [@yampeleg](https://x.com/yampeleg) [@nisten](https://x.com/nisten) [@ldjconfirmed](https://x.com/ldjconfirmed)

* Guests: [@idosal1](https://x.com/idosal1) [@liadyosef](https://x.com/liadyosef) - MCP-UI/MCP Apps

* **Big CO LLMs + APIs**

* Anthropic launches **Claude Opus 4.5** - world’s top model for coding, agents, and tool use ([X](https://x.com/claudeai/status/1993030546243699119), [Announcement](https://www.anthropic.com/news/claude-opus-4-5), [Blog](https://www.anthropic.com/engineering/advanced-tool-use))

* OpenAI Integrates ChatGPT **Voice Mode** Directly into Chats ([X](https://x.com/OpenAI/status/1993381101369458763))

* **Open Source LLMs**

* Prime Intellect - **INTELLECT-3** 106B MoE ([X](https://x.com/PrimeIntellect/status/1993895068290388134), [HF](https://huggingface.co/PrimeIntellect/INTELLECT-3), [Blog](https://www.primeintellect.ai/blog/intellect-3), [Try It](https://chat.primeintellect.ai/))

* Tencent - **HunyuanOCR** 1B SOTA OCR model ([X](https://x.com/TencentHunyuan/status/1993202595264131436), [HF](https://huggingface.co/tencent/HunyuanOCR), [Github](https://github.com/Tencent-Hunyuan/HunyuanOCR), [Blog](https://hunyuan.tencent.com/vision/zh))

* Microsoft - **Fara-7B** on-device computer-use agent ([X](https://x.com/MSFTResearch/status/1993024319186674114), [Blog](https://www.microsoft.com/en-us/research/blog/fara-7b-best-in-class-7b-parameter-vision-language-model-for-computer-use/), [HF](https://huggingface.co/microsoft/Fara-7B), [Github](https://github.com/microsoft/fara))

* DeepSeek - **Math-V2** IMO-gold math LLM ([HF](https://huggingface.co/deepseek-ai/DeepSeek-Math-V2))

* **Interview: MCP Apps**

* MCP-UI standardized as **MCP Apps** by Anthropic and OpenAI ([X](https://x.com/idosal1/status/1992636462186029233), [Blog](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps-extending-servers-with-interactive-user-interfaces), [Announcement](https://mcpui.dev))

* **Vision & Video**

* Tencent - **HunyuanVideo 1.5** lightweight DiT open video model ([X](https://x.com/TencentHunyuan/status/1991721236855156984), [GitHub](https://github.com/Tencent/HunyuanVideo), [HF](https://huggingface.co/tencent/HunyuanVideo))

* LTX Studio - **Retake** AI video editing tool ([X](https://x.com/LTXStudio/status/1993715247031767298), [Try It](https://replicate.com/lightricks/ltx-2-retake))

* **Whisper Thunder** - mystery #1 ranked video model on arena

* **AI Art & Diffusion**

* Black Forest Labs - **FLUX.2** 32B multi-reference image model ([X](https://x.com/bfl_ml/status/1993345470945804563), [HF](https://huggingface.co/black-forest-labs/FLUX.2-dev), [Blog](https://bfl.ai/blog/flux-2))

* Tongyi - **Z-Image Turbo** sub-second 6B image gen ([GitHub](https://github.com/Tongyi-MAI/Z-Image), [HF](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo))

* **This Week’s Buzz**

* W&B launches **Serverless LoRA Inference** on CoreWeave ([X](https://x.com/wandb/status/1993032159985385978), [Blog](https://wandb.ai/wandb_fc/llm_tools/reports/Serverless-LoRA-inference-on-W-B-CoreWeave--Vmlldzo5MjUwNzAx), [Notebook](https://wandb.me/lora_nb)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-thanksgiving-special-25/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-thanksgiving-special-25?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE4MDEzOTE0NywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.VjghCUP417pRoQbNiwKjWQ3DO0_7PP3k78tyQD9GidE&utm_campaign=CTA_5).

---

## 📆 ThursdAI - the week that changed the AI landscape forever - Gemini 3, GPT codex max, Grok 4.1 & fast, SAM3 and Nano Banana Pro

**Date:** November 20, 2025  
**Duration:** 1:29:13  
**Link:** [https://sub.thursdai.news/p/thursdai-the-week-that-changed-the](https://sub.thursdai.news/p/thursdai-the-week-that-changed-the)

Hey everyone, Alex here 👋

I’m writing this one from a noisy hallway at the AI Engineer conference in New York, still riding the high (and the sleep deprivation) from what might be the craziest week we’ve ever had in AI.

In the span of a few days:

Google dropped **Gemini 3 Pro**, a new **Deep Think mode**, generative UIs, and a free agent-first IDE called **Antigravity**.xAI shipped **Grok 4.1**, then followed it up with **Grok 4.1 Fast** plus an Agent Tools API.OpenAI answered with **GPT‑5.1‑Codex‑Max**, a long‑horizon coding monster that can work for more than a day, and quietly upgraded ChatGPT Pro to **GPT‑5.1 Pro**.Meta looked at all of that and said “cool, we’ll just segment literally everything and turn photos into 3D objects” with **SAM 3 and SAM 3D**.Robotics folks dropped a home robot trained with almost no robot data.And Google, just to flex, capped Thursday with Nano Banana Pro, a 4K image model and a provenance system while we were already live! 

For the first time in a while it doesn’t just feel like “new models came out.” It feels like the future actually clicked forward a notch.

This is why ThursdAI exists. Weeks like this are basically impossible to follow if you have a day job, so my co‑hosts and I do the no‑sleep version so you don’t have to. Plus, being at AI Engineer makes it easy to get super high quality guests so this week we had 3 folks join us, Swyx from Cognition/Latent Space, Thor from DeepMind (on his 3rd day) and Dominik from OpenAI! Alright, deep breath. Let’s untangle the week.

**TL;DR **

If you only skim one section, make it this one (links in the end):

* **Google**

* **Gemini 3 Pro**: 1M‑token multimodal model, huge reasoning gains - new LLM king

* **ARC‑AGI‑2:** 31.11% (Pro), **45.14% (Deep Think)** – enormous jumps

* **Antigravity IDE**: free, Gemini‑powered VS Code fork with agents, plans, walkthroughs, and browser control

* **Nano Banana Pro**: 4K image generation with *perfect* text + SynthID provenance; dynamic “generative UIs” in Gemini

* **xAI**

* **Grok 4.1**: big post‑training upgrade – #1 on human‑preference leaderboards, much better EQ & creative writing, fewer hallucinations

* **Grok 4.1 Fast + Agent Tools API**: 2M context, SOTA tool‑calling & agent benchmarks (Berkeley FC, T²‑Bench, research evals), aggressive pricing and tight X + web integration

* **OpenAI**

* **GPT‑5.1‑Codex‑Max**: “frontier agentic coding” model built for **24h+** software tasks with native **compaction** for million‑token sessions; big gains on SWE‑Bench, SWE‑Lancer, TerminalBench 2

* **GPT‑5.1 Pro**: new “research‑grade” ChatGPT mode that will happily think for minutes on a single query

* **Meta**

* **SAM 3**: open‑vocabulary segmentation + tracking across images and video (with text & exemplar prompts)

* **SAM 3D**: single‑image → 3D objects & human bodies; surprisingly high‑quality 3D from one photo

* **Robotics**

* **Sunday Robotics – ACT‑1 & Memo**: home robot foundation model trained from a **$200 skill glove** instead of $20K teleop rigs; long‑horizon household tasks with solid zero‑shot generalization

* **Developer Tools**

* **Antigravity** and **Marimo’s VS Code / Cursor extension** both push toward agentic, reactive dev workflows

**Live from AI Engineer New York: Coding Agents Take Center Stage**

We recorded this week’s show on location at the AI Engineer Summit in New York, inside a beautiful podcast studio the team set up right on the expo floor. Huge shout out to Swyx, Ben, and the whole AI Engineer crew for that — last time I was balancing a mic on a hotel nightstand, this time I had broadcast‑grade audio while a robot dog tried to steal the show behind us.

This year’s summit theme is very on‑the‑nose for this week: **coding agents**.

Everywhere you look, there’s a company building an “agent lab” on top of foundation models. Amp, Cognition, Cursor, CodeRabbit, Jules, Google Labs, all the open‑source folks, and even the enterprise players like Capital One and Bloomberg are here, trying to figure out what it means to have real software engineers that are partly human and partly model.

Swyx framed it nicely when he said that if you take “vertical AI” seriously enough, you eventually end up building an agent lab. Lawyers, healthcare, finance, developer tools — they all converge on “agents that can reason and code.”

The big labs heard that theme loud and clear. Almost every major release this week is about agents, tools, and long‑horizon workflows, not just chat answers.

**Google Goes All In: Gemini 3 Pro, Antigravity, and the Agent Revolution**

Let’s start with Google because, after years of everyone asking “where’s Google?” in the AI race, they showed up this week with multiple bombshells that had even the skeptics impressed.

**Gemini 3 Pro: Multimodal Intelligence That Actually Delivers**

Google finally released Gemini 3 Pro, and the numbers are genuinely impressive. We’re talking about a 1 million token context window, massive benchmark improvements, and a model that’s finally competing at the very top of the intelligence charts. Thor from DeepMind joined us on the show (literally on day 3 of his new job!) and you could feel the excitement.

The headline numbers: Gemini 3 Pro with Deep Think mode achieved **45.14% on ARC-AGI-2**—that’s roughly double the previous state-of-the-art on some splits. For context, ARC-AGI has been one of those benchmarks that really tests genuine reasoning and abstraction, not just memorization. The standard Gemini 3 Pro hits 31.11% on the same benchmark, both scores are absolutely out of this world in Arc! 

On GPQA Diamond, Gemini 3 Pro jumped about 10 points compared to prior models. We’re seeing roughly 81% on MMLU-Pro, and the coding performance is where things get really interesting—Gemini 3 Pro is scoring around 56% on SciCode, representing significant improvements in actual software engineering tasks.

But here’s what made Ryan from Amp switch their default model to Gemini 3 Pro immediately: the real-world usability. Ryan told us on the show that they’d never switched default models before, not even when GPT-5 came out, but Gemini 3 Pro was so noticeably better that they made it the default on Tuesday. Of course, they hit rate limits almost immediately (Google had to scale up fast!), but those have since been resolved.

**Antigravity: Google’s Agent-First IDE**

Then Google dropped Antigravity, and honestly, this might be the most interesting part of the whole release. It’s a free IDE (yes, free!) that’s basically a fork of VS Code, but reimagined around agents rather than human-first coding.

The key innovation here is something they call the “Agent Manager”—think of it like an inbox for your coding agents. Instead of thinking in folders and files, you’re managing conversations with agents that can run in parallel, handle long-running tasks, and report back when they need your input.

I got early access and spent time playing with it, and here’s what blew my mind: you can have multiple agents working on different parts of your codebase simultaneously. One agent fixing bugs, another researching documentation, a third refactoring your CSS—all at once, all coordinated through this manager interface.

The browser integration is crazy too. Antigravity can control Chrome directly, take screenshots and videos of your app, and then use those visuals to debug and iterate. It’s using Gemini 3 Pro for the heavy coding, and even Nano Banana for generating images and assets. The whole thing feels like it’s from a couple years in the future.

Wolfram on the show called out how good Gemini 3 is for creative writing too—it’s now his main model, replacing GPT-4.5 for German language tasks. The model just “gets” the intention behind your prompts rather than following them literally, which makes for much more natural interactions.

**Nano Banana Pro: 4K Image Generation With Thinking**

And because Google apparently wasn’t done announcing things, they also dropped Nano Banana Pro on Thursday morning—literally breaking news during our live show. This is their image generation model that now supports 4K resolution and includes “thinking” traces before generating.

I tested it live by having it generate an infographic about all the week’s AI news (which you can see on the top), and the results were wild. Perfect text across the entire image (no garbled letters!), proper logos for all the major labs, and compositional understanding that felt way more sophisticated than typical image models. The file it generated was 8 megabytes—an actual 4K image with stunning detail.

What’s particularly clever is that Nano Banana Pro is really Gemini 3 Pro doing the thinking and planning, then handing off to Nano Banana for the actual image generation. So you get multimodal reasoning about your request, then production-quality output. You can even upload reference images—up to 14 of them—and it’ll blend elements while maintaining consistency.

Oh, and every image is watermarked with SynthID (Google’s invisible watermarking tech) and includes C2PA metadata, so you can verify provenance. This matters as AI-generated content becomes more prevalent.

**Generative UIs: The Future of Interfaces**

One more thing Google showed off: generative UIs in the Gemini app. Wolfram demoed this for us, and it’s genuinely impressive. Instead of just text responses, Gemini can generate full interactive mini-apps on the fly—complete dashboards, data visualizations, interactive widgets—all vibe-coded in real time.

He asked for “four panels of the top AI news from last week” and Gemini built an entire news dashboard with tabs, live market data (including accurate pre-market NVIDIA stats!), model comparisons, and clickable sections. It pulled real information, verified facts, and presented everything in a polished UI that you could interact with immediately.

This isn’t just a demo—it’s rolling out in Gemini now. The implication is huge: we’re moving from static responses to dynamic, contextual interfaces generated just-in-time for your specific need.

**xAI Strikes Back: Grok 4.1 and the Agent Tools API**

Not to be outdone, xAI released Grok 4.1 at the start of the week, briefly claimed the #1 spot on LMArena (at 1483 Elo, not 2nd to Gemini 3), and then followed up with Grok 4.1 Fast and a full Agent Tools API.

**Grok 4.1: Emotional Intelligence Meets Raw Performance**

Grok 4.1 brought some really interesting improvements. Beyond the benchmark numbers (64% win rate over the previous Grok in blind tests), what stood out was the emotional intelligence. On EQ-Bench3, Grok 4.1 Thinking scored **1586 Elo**, beating every other model including Gemini, GPT-5, and Claude.

The creative writing scores jumped by roughly 600 Elo points compared to earlier versions. And perhaps most importantly for practical use, hallucination rates dropped from around 12% to 4%—that’s roughly a 3x improvement in reliability on real user queries.

xAI’s approach here was clever: they used “frontier agentic reasoning models as reward models” during RL training, which let them optimize for subjective qualities like humor, empathy, and conversational style without just scaling up model size.

**Grok 4.1 Fast: The Agent Platform Play**

Then came Grok 4.1 Fast, released just yesterday, and this is where things get really interesting for developers. It’s got a **2 million token context window** (compared to Gemini 3’s 1 million) and was specifically trained for agentic, tool-calling workflows.

The benchmark performance is impressive: **93-100% on τ²-Bench Telecom** (customer support simulation), **~72% on Berkeley Function Calling v4** (top of the leaderboard), and strong scores across research and browsing tasks. But here’s the kicker: the pricing is aggressive.

At $0.20 per million input tokens and $0.50 per million output tokens, Grok 4.1 Fast is dramatically cheaper than GPT-5 and Claude while matching or exceeding their agentic performance. For the first two weeks, it’s completely free via the xAI API and OpenRouter, which is smart—get developers hooked on your agent platform.

The Agent Tools API gives Grok native access to X search, web browsing, code execution, and document retrieval. This tight integration with X is a genuine advantage—where else can you get real-time access to breaking news, sentiment, and conversation? Yam tested it on the show and confirmed that Grok will search Reddit too, which other models often refuse to do. I’ve used both these models this week in my N8N research agent and I gotta say, 4.1 fast is a MASSIVE improvement! 

**OpenAI’s Endurance Play: GPT-5.1-Codex-Max and Pro**

OpenAI clearly saw Google and xAI making moves and decided they weren’t going to let this week belong to anyone else. They dropped two significant releases: GPT-5.1-Codex-Max and an update to GPT-5.1 Pro.

**GPT-5.1-Codex-Max: Coding That Never Stops**

This is the headline: GPT-5.1-Codex-Max can work autonomously for **over 24 hours**. Not 24 minutes, not 24 queries—24 actual hours on a single software engineering task. I talked to someone from OpenAI at the conference who told me internal checkpoints ran for nearly a **week** on and off.

How is this even possible? The secret is something OpenAI calls “compaction”—a native mechanism trained into the model that lets it prune and compress its working session history while preserving the important context. Think of it like the model taking notes on itself, discarding tool-calling noise and keeping only the critical design decisions and state.

The performance numbers back this up:

* **SOTA 77.9% on SWE-Bench Verified** (up from 73.7%)

* **SOTA 79.9% on SWE-Lancer IC SWE** (up from 66.3%)

* ** 58.1% on TerminalBench 2.0** (up from 52.8%)

And crucially, in medium reasoning mode, it uses **30% fewer thinking tokens** while achieving better results. There’s also an “Extra High” reasoning mode for when you truly don’t care about latency and just want maximum capability.

Yam, one of our co-hosts who’s been testing extensively, said you can feel the difference immediately. The model just “gets it” faster, powers through complex problems, and the earlier version’s quirk of ignoring your questions and just starting to code is fixed—now it actually responds and collaborates.

Dominic from OpenAI joined us on the show and confirmed that compaction was trained natively into the model using RL, similar to how Claude trained natively for MCP. This means the model doesn’t waste reasoning tokens on maintaining context—it just knows how to do it efficiently.

**GPT-5.1 Pro: Research-Grade Intelligence & ChatGPT joins your group chat1**

Then there’s GPT-5.1 Pro, which is less about coding and more about deep, research-level reasoning. This is the model that can run for 10-17 minutes on a single query, thinking through complex problems with the kind of depth that previously required human experts.

OpenAI also quietly rolled out group chats—basically, you can now have multiple people in a ChatGPT conversation together, all talking to the model simultaneously. Useful for planning trips, brainstorming with teams, or working through problems collaboratively. If agent mode works in group chats (we haven’t confirmed yet), that could get really interesting.

Meta drops SAM3 & SAM3D - image and video segmentation models powered by natural language

Phew ok, big lab releases now done, oh.. wait not yet! Because Meta has decided to also make a dent on this Week with SAM3 and SAM3D, which both are crazy. I’ll just add their video release here instead of going on and on! 

This Week’s Buzz from Weights & Biases

It’s been a busy week at Weights & Biases as well! We are proud Gold Sponsors of the AI Engineer conference here in NYC. If you’re at the event, please stop by our booth—we’re even giving away a $4,000 robodog!

This week, I want to highlight a fantastic update from **Marimo**, the reactive Python notebook company we acquired.

Marimo just shipped a native **VS Code and Cursor extension**. This brings Marimo’s reactive, Git-friendly notebooks directly into your favorite editors.

Crucially, it integrates deeply with uv for lightning-fast package installs and reproducible environments. If you import a package you don’t have, the extension prompts you to install it and records the dependency in the script metadata. This bridges the gap between experimental notebooks and production-ready code, and it’s a huge boost for AI-native development workflows. ([Blog](https://marimo.io/blog) , [GitHub](https://github.com/marimo-team/marimo-lsp) )

The Future Arrived Early

Phew... if you read all the way until this point, can you leave a ⚡ emoji in the comemnts? I was writing this and it.. is a lot! I was wondering who would even read all the way till here! 

This week we felt the acceleration! 🔥 I can barely breathe, I need a nap! 

A huge thank you to our guests—Ryan, Swyx, Thor, and Dominik—for navigating the chaos with us live on stage, and to the AI Engineer team for hosting us.

We’ll be back next week to cover whatever the AI world throws at us next. Stay tuned, because at this rate, AGI might be here by Christmas.

TL;DR - show notes and links

**Hosts and Co‑hosts**

* Alex Volkov – AI Evangelist at Weights & Biases / CoreWeave, host of ThursdAI ([X](https://x.com/altryne))

* Co‑hosts - Wolfram Ravenwolf – ([X](https://x.com/WolframRvnwlf)), Yam Peleg ([X](https://x.com/yampeleg)) LDJ ([X](https://x.com/ldjconfirmed))

**Guests**

* Swyx – Founder of AI Engineer World’s Fair and Summit, now at Cognition ( [Latent.Space](https://substack.com/profile/89230629-latentspace) , [X](https://x.com/swyx))

* Ryan Carson –  Amp ([X](https://x.com/ryancarson))

* Thor Schaeff – Google DeepMind, Gemini API and AI Studio ([X](https://x.com/thorwebdev))

* Dominik Kundel – Developer Experience at OpenAI ([X](https://x.com/dkundel))

**Open Source LLMs**

* Allen Institute Olmo 3 - 7B/32B fully open reasoning suite with end-to-end training transparency ([X](https://x.com/allen_ai/status/1991507983881379896), [Blog](https://allenai.org/olmo))

**Big CO LLMs + APIs**

* Google Gemini 3 Pro - 1M-token, multimodal, agentic model with Generative UIs ([X](https://x.com/altryne/status/1990812491304350130), [X](https://x.com/sundarpichai/status/1990812770762215649), [X](https://x.com/GoogleDeepMind/status/1990812966074376261))

* Google Antigravity - Agent-first IDE powered by Gemini 3 Pro ([Blog](https://antigravity.google/blog/introducing-google-antigravity), [X](https://x.com/GoogleDeepMind/status/1990827890435346787))

* xAI Grok 4.1 and Grok 4.1 Thinking - big gains in Coding, EQ, creativity, and honesty ([X](https://x.com/altryne/status/1990526775148097662), [Blog](https://x.ai/blog/grok-4-1))

* xAI Grok 4.1 Fast and Agent Tools API - 2M-token context, state-of-the-art tool-calling ([X](https://x.com/xai/status/1991284813727474073))

* OpenAI GPT-5.1-Codex-Max - long-horizon agentic coding model for 24-hour+ software tasks ([X](https://x.com/polynoamial/status/1991212955250327768), [X](https://x.com/OpenAIDevs/status/1991217488550359066))

* OpenAI GPT-5.1 Pro - research-grade reasoning model in ChatGPT Pro

* Microsoft, NVIDIA, and Anthropic partnership - to scale Claude on Azure with massive GPU investments ([Announcement](https://www.anthropic.com/news/microsoft-nvidia-partnership), [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-microsoft-anthropic-partnership), [Microsoft Blog](https://blogs.microsoft.com/2025/11/partnership-anthropic-nvidia-azure))

**This weeks Buzz**

* Marimo ships native VS Code & Cursor extension with reactive notebooks and uv-powered environments ([X](https://x.com/marimo_io/status/1991207581763981722), [Blog](https://marimo.io/blog), [GitHub](https://github.com/marimo-team/marimo-lsp))

**Vision & Video & 3D**

* Meta SAM 3 & SAM 3D - promptable segmentation, tracking, and single-image 3D reconstruction ([X](https://x.com/AIatMeta/status/1991178519557046380), [Blog](https://ai.meta.com/blog/sam-3d/), [GitHub](https://github.com/facebookresearch/segment-anything))

**AI Art & Diffusion**

* Google Nano Banana Pro and SynthID verification - 4K image generation with provenance ([Blog](https://blog.google/technology/developers/gemini-3-developers/))

**Show Notes and other Links**

* AI Engineer Summit NYC - Live from the conference

* Full livestream available on YouTube

* ThursdAI - Nov 20, 2025 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-the-week-that-changed-the/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-the-week-that-changed-the?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3OTUwNjU1MywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.I3WdUBv6O1dhHU9GY_e_takb9bzhhVv3Zj1jpDJVK34&utm_campaign=CTA_5).

---

## GPT‑5.1’s New Brain, Grok’s 2M Context, Omnilingual ASR, and a Terminal UI That Sparks Joy

**Date:** November 13, 2025  
**Duration:** 1:10:20  
**Link:** [https://sub.thursdai.news/p/thursdai-nov-13-gpt-51-ernie-45-vl](https://sub.thursdai.news/p/thursdai-nov-13-gpt-51-ernie-45-vl)

Hey, this is Alex! 

We’re finally so back! Tons of open source releases, OpenAI updates GPT and a few breakthroughs in audio as well, makes this a very dense week! 

Today on the show, we covered the newly released GPT 5.1 update, a few open source releases like Terminal Bench and Project AELLA (renamed OASSAS), and Baidu’s Ernie 4.5 VL that shows impressive visual understanding! 

Also, chatted with Paul from 11Labs and Dima Duev from the wandb SDK team, who brought us a delicious demo of LEET, our new TUI for wandb! 

Tons of news coverage, let’s dive in 👇 (as always links and show notes in the end) 

Open Source AI

Let’s jump directly into Open Source as this week has seen some impressive big company models. 

Terminal-Bench 2.0 -  a harder, highly‑verified coding and terminal benchmark ([X](https://x.com/alexgshaw/status/1986911106108211461), [Blog](https://harborframework.com/), [Leaderboard](https://www.tbench.ai/leaderboard))

We opened with Terminal‑Bench 2.0 plus its new harness, Harbor, because this is the kind of benchmark we’ve all been asking for. 

Terminal‑Bench focuses on agentic coding in a real shell. Version 2.0 is a hard set of 89 terminal tasks, each one painstakingly vetted by humans and LLMs to make sure it’s solvable and realistic. Think “I checked out master and broke my personal site, help untangle the git mess” or “implement GPT‑2 code golf with the fewest characters.” 

On the new leaderboard, top agents like Warp’s agentic console and Codex CLI + GPT‑5 sit around fifty percent success. That number is exactly what excites me: we’re nowhere near saturation. When everyone is in the 90‑something range, tiny 0.1 improvements are basically noise. When the best models are at fifty percent, a five‑point jump really means something.

A huge part of our conversation focused on reproducibility. We’ve seen other benchmarks like OSWorld turn out to be unreliable, with different task sets and non‑reproducible results making scores incomparable. Terminal‑Bench addresses this with Harbor, a harness designed to run sandboxed, containerized agent rollouts at scale in a consistent environment. This means results are actually comparable. It’s a ton of work to build an entire evaluation ecosystem like this, and with over a thousand contributors on their Discord, it’s a fantastic example of a healthy, community‑driven effort. This is one to watch! 

**Baidu’s ERNIE‑4.5‑VL “Thinking”: a 3B visual reasoner that punches way up **([X](https://x.com/Baidu_Inc/status/1988182106359411178), [HF](https://huggingface.co/ERNIE/ERNIE-4.5-VL-28B-A3B-Thinking), [GitHub](https://github.com/ERNIE/ERNIE-4.5-VL-28B-A3B-Thinking))

Next up, Baidu dropped a really interesting model, ERNIE‑4.5‑VL‑28B‑A3B‑Thinking. This is a compact, 3B active‑parameter multimodal reasoning model focused on vision, and it’s much better than you’d expect for its size. Baidu’s own charts show it competing with much larger closed models like Gemini‑2.5‑Pro and GPT‑5‑High on a bunch of visual benchmarks like ChartQA and DocVQA.

During the show, I dropped a fairly complex chart into the demo, and ERNIE‑4.5‑VL gave me a clean textual summary almost instantly—it read the chart more cleanly than I could. The model is built to “think with images,” using dynamic zooming and spatial grounding to analyze fine details. It’s released under an Apache‑2.0 license, making it a serious candidate for edge devices, education, and any product where you need a cheap but powerful visual brain.

**Open Source Quick Hits: OSSAS, VibeThinker, and Holo Two**

We also covered a few other key open-source releases. Project AELLA was quickly rebranded to OSSAS (Open Source Summaries At Scale), an initiative to make scientific literature machine‑readable. They’ve released 100k paper summaries, two fine-tuned models for the task, and a 3D visualizer. It’s a niche but powerful tool if you’re working with massive amounts of research. ([X](https://x.com/samhogan/status/1988306424309706938), [HF](https://huggingface.co/inference-net))

WeiboAI (from the Chinese social media company) released VibeThinker‑1.5B, a tiny 1.5B‑parameter reasoning model that is making bold claims about beating the 671B DeepSeek R1 on math benchmarks. 

We discussed the high probability of benchmark contamination, especially on tests like AIME24, but even with that caveat, getting strong chain‑of‑thought math out of a 1.5B model is impressive and useful for resource‑constrained applications.  ([X](https://x.com/WeiboLLM/status/1988109435902832896), [HF](https://huggingface.co/WeiboAI/VibeThinker-1.5B), [Arxiv](https://arxiv.org/abs/2511.06221))

Finally, we had some breaking news mid‑show: H Company released Holo Two, their next‑gen multimodal agent for controlling desktops, websites, and mobile apps. It’s a fine‑tune of Qwen3‑VL and comes in 4B and 8B Apache‑2.0 licensed versions, pushing the open agent ecosystem forward. ([X](https://x.com/hcompany_ai/status/1989013556134638039), [Blog](https://hcompany.ai/blog), [HF](https://huggingface.co/hcompany-ai/Holo2-8B))

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Big Companies & APIs

**GPT‑5.1: Instant vs Thinking, and a new personality bar**

The biggest headline of the week was OpenAI shipping GPT‑5.1, and this was a hot topic of debate on the show. The update introduces two modes: “Instant” for fast, low‑compute answers, and “Thinking” for deeper reasoning on hard problems. OpenAI claims Instant mode uses 57% fewer tokens on easy tasks, while Thinking mode dedicates 71% more compute to difficult ones. This adaptive approach is a smart evolution.

The release also adds a personality dropdown with options like Professional, Friendly, Quirky, and Cynical, aiming for a more “warm” and customizable experience. 

Yam and I felt this was a step in the right direction, as GPT‑5 could often feel a bit cold and uncommunicative. However, Wolfram had a more disappointing experience, finding that GPT‑5.1 performed significantly worse on his German grammar and typography tasks compared to GPT‑4 or Claude Sonnet 4.5. It’s a reminder that “upgrades” can be subjective and task‑dependent.

Since the show was recorded, GPT 5.1 is also released in the API and they have published a [prompting guide](https://cookbook.openai.com/examples/gpt-5/gpt-5-1_prompting_guide) and some evals! With some significant jumps across SWE-bench verified and GPQA Diamond! We’ll be testing this model out all week. 

The highlight for this model is the creative writing, it was made public that this model was being tested on OpenRouter as Polaris-alpha and that one tops the eqbench creative writing benchmarks beating Sonnet 4.5 and Gemini! 

**Grok‑4 Fast: 2M context and a native X superpower**

Grok‑4 Fast from xAI apparenly quietly got a substantial upgrade to a 2M‑token context window, but the most interesting part is its unique integration with X. The API version has access to internal tools for semantic search over tweets, retrieving top quote tweets, and understanding embedded images and videos. I’ve started using it as a research agent in my show prep, and it feels like having a research assistant living inside X’s backend—something you simply can’t replicate with public tools.

I still have my gripes about their “stealth upgrade” versioning strategy, which makes rigorous evaluation difficult, but as a practical tool, Grok‑4 Fast is incredibly powerful. It’s also surprisingly fast and cost‑effective, holding its own against other top models on benchmarks while offering a superpower that no one else has.

**Google SIMA 2: Embodied Agents in Virtual Worlds**

Google’s big contribution this week was SIMA 2, DeepMind’s latest embodied agent for 3D virtual worlds. SIMA lives inside real games like *No Man’s Sky* and *Goat Simulator*, seeing the screen and controlling the game via keyboard and mouse, using Gemini as its reasoning brain. Demos showed it following complex, sketch‑based instructions, like finding an object that looks like a drawing of a spaceship and jumping on top of it.

When you combine this with Genie 3—Google’s world model that can generate playable environments from a single image—you see the bigger picture: agents that learn physics, navigation, and common sense by playing in millions of synthetic worlds. We’re not there yet, but the pieces are clearly being assembled. We also touched on the latest Gemini Live voice upgrade, which users are reporting feels much more natural and responsive

**More Big Company News: Qwen Deep Research, Code Arena, and Cursor**

We also briefly covered Qwen’s [new](https://x.com/Alibaba_Qwen/status/1989026687611461705) Deep Research feature, which offers an OpenAI‑style research agent inside their ecosystem. LMSYS launched [Blog](https://arena.lmsys.org/blog/code-arena), a fantastic live evaluation platform where models build real web apps agentically, with humans voting on the results. And in the world of funding, the AI‑native code editor Cursor raised a staggering $2.3 billion, a clear sign that AI is becoming the default way developers interact with code.

**This Week’s Buzz: W&B LEET – a terminal UI that sparks joy**

For this week’s buzz, I brought on Dima Duev from our SDK team at Weights & Biases to show off a side project that has everyone at the company excited: LEET, the Lightweight Experiment Exploration Tool. Imagine you’re training on an air‑gapped HPC cluster, living entirely in your terminal. How do you monitor your runs? With LEET.

You run your training script in W&B offline mode, and in another terminal, you type wandb beta leet. Your terminal instantly turns into a full TUI dashboard with live metric plots, system stats, and run configs. You can zoom into spikes in your loss curve, filter metrics, and see everything updating in real time, all without a browser or internet connection. It’s one of those tools that just sparks joy. It ships with the latest wandb SDK (v0.23.0+), so just upgrade and give it a try! 

**Voice & Audio: Scribe v2 Realtime and Omnilingual ASR**

**ElevenLabs Scribe v2 Realtime: ASR built for agents **([X](https://x.com/elevenlabsio/status/1988282248445976987), [Announcement](https://docs.elevenlabs.io), [Demo](https://captions.events/))

We’ve talked a lot on this show about ElevenLabs as “the place you go to make your AI talk.” This week, they came for the other half of the conversation. Paul Asjes from ElevenLabs joined us to walk through Scribe v2 Realtime, their new low‑latency speech‑to‑text model. If you’re building a voice agent, you need ears, a brain, and a mouth. ElevenLabs already nailed the mouth, and now they’ve built some seriously good ears.

Scribe v2 Realtime is designed to run at around 150 milliseconds median latency, across more than ninety languages. Watching Paul’s live demo, it felt comfortably real‑time. When he switched from English to Dutch mid‑sentence, the system just followed along without missing a beat. Community benchmarks and our own impressions show it holding its own or beating competitors like Whisper and Deepgram in noisy, accented, and multi‑speaker scenarios. It’s also context‑aware enough to handle code, initialisms, and numbers correctly, which is critical for real‑world agents. This is a production‑ready ASR for anyone building live voice experiences.

**Meta’s drops Omnilingual ASR: 1,600+ languages, many for the first time + a bunch of open source models  ** ([X](https://x.com/AIatMeta/status/1987946571439444361), [Blog](https://ai.meta.com/blog/omnilingual-asr-advancing-automatic-speech-recognition), [Announcement](https://ai.meta.com/research/publications/omnilingual-asr-open-source-multilingual-speech-recognition-for-1600-languages/), [HF](https://huggingface.co/datasets/facebook/omnilingual-asr-corpus))

On the other end of the spectrum, Meta released something that’s less about ultra‑low latency and more about sheer linguistic coverage: Omnilingual ASR. This is a family of models and a dataset designed to support speech recognition for more than 1,600 languages, including about 500 that have never had any ASR support before. That alone is a massive contribution.

Technically, it uses a wav2vec 2.0 backbone scaled up to 7B parameters with both CTC and LLM‑style decoders. The LLM‑like architecture allows for in‑context learning, so communities can add support for new languages with only a handful of examples. They’re also releasing the Omnilingual ASR Corpus with data for 350 underserved languages. The models and code are Apache‑2.0, making this a huge step forward for more inclusive speech tech.

**AI Art, Diffusion & 3D**

**Qwen Image Edit + Multi‑Angle LoRA: moving the camera after the fact  **([X](https://x.com/linoy_tsaban/status/1986090375409533338), [HF](https://huggingface.co/spaces/linoyts/Qwen-Image-Edit-Angles), [Fal](https://x.com/fal/status/1988693046267969804?s=20))

This one was pure fun. A new set of LoRAs for Qwen Image Edit adds direct camera control to still images. A Hugging Face demo lets you upload a photo and use sliders to rotate the camera up to 90 degrees, tilt from a bird’s‑eye to a worm’s‑eye view, and adjust the lens. We played with it live on the show with a portrait of Wolfram and a photo of my cat, generating different angles and then interpolating them into a short “fly‑around” video. It’s incredibly cool and preserves details surprisingly well, feeling like you have a virtual camera inside a 2D picture.

**NVIDIA ChronoEdit‑14B Upscaler LoRA **([X](https://x.com/HuanLing6/status/1988098676838060246), [HF](https://huggingface.co/NVIDIA/ChronoEdit-14B-Diffusers-Upscaler-LoRA))

Finally, NVIDIA released an upscaler LoRA based on their ChronoEdit‑14B model and merged the pipeline into Hugging Face Diffusers. ChronoEdit reframes image editing as a temporal reasoning task, like generating a tiny video. This makes it good for maintaining consistency in edits and upscales. It’s a heavy model, requiring ~34GB of VRAM, and for aggressive upscaling, specialized tools might still be better. But for moderate upscales where temporal coherence matters, it’s a very interesting new tool in the toolbox.

Phew, we made it through this dense week! Looking to next week, I’ll be recoridng the show live from the AI Engieer CODE summit in NY, and we’ll likely see a few good releases from the big G? Maybe? finally? 

As always, if this was helpful, please subscribe to ThursdAI and share it with 2 friends, see you next week 🫡 

TL;DR and Show Notes

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/altryne))

* **Co-Hosts** - [@WolframRvnwlf](http://x.com/WolframRvnwlf), [@yampeleg](https://x.com/yampeleg), [@ldjconfirmed](http://x.com/ldjconfirmed)

* **Guest**: Dima Duev - SDK team Wandb

* **Guest**: Paul Asjes - Eleven Labs ([@paul_asjes](https://x.com/paul_asjes))

* **Open Source LLMs**

* **Terminal-Bench 2.0 and Harbor launch** ([X](https://x.com/alexgshaw/status/1986911106108211461), [Blog](https://harborframework.com/), [Docs](https://harborframework.com/docs/running-tbench), [Announcement](https://www.tbench.ai/leaderboard))

* **Baidu releases ERNIE-4.5-VL-28B-A3B-Thinking** ([X](https://x.com/Baidu_Inc/status/1988182106359411178), [HF](https://huggingface.co/ERNIE/ERNIE-4.5-VL-28B-A3B-Thinking), [GitHub](https://github.com/ERNIE/ERNIE-4.5-VL-28B-A3B-Thinking), [Blog](https://ernie.baidu.com/blog/ernie-4-5-vl-28b-a3b-thinking), [Platform](https://ai.baidu.com/ai-studio))

* **Project AELLA (OSSAS): 100K LLM-generated paper summaries** ([X](https://x.com/samhogan/status/1988306424309706938), [HF](https://huggingface.co/inference-net))

* **WeiboAI’s VibeThinker-1.5B** ([X](https://x.com/WeiboLLM/status/1988109435902832896), [HF](https://huggingface.co/WeiboAI/VibeThinker-1.5B), [Arxiv](https://arxiv.org/abs/2511.06221), [Announcement](https://venturebeat.com/ai/weibos-new-open-source-ai-model-vibethinker-1-5b-outperforms-deepseek-r1-on))

* **Code Arena — live, agentic coding evaluations** ([X](https://x.com/arena/status/1988665193275240616), [Blog](https://arena.lmsys.org/blog/code-arena), [Announcement](https://arena.lmsys.org/))

* **Big CO LLMs + APIs**

* **Grok 4 Fast, Grok Imagine and Nano Banana v1/v2** ([X](https://x.com/chatgpt21/status/1987976808562589946), [X](https://x.com/cowowhite/status/1988213138333069314), [X](https://x.com/RasNas1994/status/1986426297900245106), [X](https://x.com/XFreeze/status/1987396781861212353))

* **OpenAI launches GPT-5.1** ([X](https://x.com/fidjissimo/status/1988683216681889887), [X](https://x.com/sama/status/1988692165686620237))

* **This weeks Buzz**

* **W&B LEET — an open-source Terminal UI (TUI) to monitor runs** ([X](https://x.com/wandb/status/1988401253156876418), [Blog](https://app.getbeamer.com/wandb/en/meet-wb-leet-a-new-terminal-ui-for-weights-biases-JXSFhyt2))

* **Voice & Audio**

* **ElevenLabs launches Scribe v2 Realtime** ([X](https://x.com/elevenlabsio/status/1988282248445976987), [Blog](https://elevenlabs.io/agents), [Docs](https://docs.elevenlabs.io))

* **Meta releases Omnilingual ASR for 1,600+ languages** ([X](https://x.com/AIatMeta/status/1987946571439444361), [Blog](https://ai.meta.com/blog/omnilingual-asr-advancing-automatic-speech-recognition), [Paper](https://ai.meta.com/research/publications/omnilingual-asr-open-source-multilingual-speech-recognition-for-1600-languages/), [HF Dataset](https://huggingface.co/datasets/facebook/omnilingual-asr-corpus), [HF Demo](https://huggingface.co/spaces/facebook/omniasr-transcriptions), [GitHub](https://github.com/facebookresearch/omnilingual-asr))

* **Gemini Live conversational upgrade** ([X](https://x.com/carlovarrasi/status/1988691309591425234))

* **AI Art & Diffusion & 3D**

* **Qwen Image Edit + Multi‑Angle LoRA for camera control** ([X](https://x.com/linoy_tsaban/status/1986090375409533338), [HF](https://huggingface.co/spaces/linoyts/Qwen-Image-Edit-Angles), [Fal](https://x.com/fal/status/1988693046267969804?s=20))

* **NVIDIA releases ChronoEdit-14B Upscaler LoRA** ([X](https://x.com/HuanLing6/status/1988098676838060246), [HF](https://huggingface.co/NVIDIA/ChronoEdit-14B-Diffusers-Upscaler-LoRA), [Docs](https://huggingface.co/docs/diffusers/main/en/api/pipelines/chronoedit)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-nov-13-gpt-51-ernie-45-vl/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-nov-13-gpt-51-ernie-45-vl?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3ODgzMTc5NywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.VgzHd7KhwCSB6lu3AOknChk60OsQoytWW7EhQvzfW_0&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Nov 6, 2025 - Kimi’s 1T Thinking Model Shakes Up Open Source, Apple Bets $1B on Gemini for Siri, and Amazon vs. Perplexity!

**Date:** November 07, 2025  
**Duration:** 1:32:45  
**Link:** [https://sub.thursdai.news/p/thursdai-nov-6-2025-kimis-1t-thinking](https://sub.thursdai.news/p/thursdai-nov-6-2025-kimis-1t-thinking)

Hey, Alex here! 

Quick note, while preparing for this week, I posted on X that I don’t remember such a quiet week in AI since I started doing ThursdAI regularly, but then 45 min before the show started, Kimi dropped a SOTA oss reasoning model, turning a quiet week into an absolute banger. 

Besides Kimi, we covered the updated MCP thinking from Anthropic, and had Kenton Varda from cloudflare as a guest to talk about Code Mode, chatted about Windsurf and Cursor latest updates and covered OpenAI’s insane deals. 

Also, because it was a quiet week, I figured I’d use the opportunity to create an AI powered automation, and used N8N for that, and shared it on the stream, so if you’re interested in automating with AI with relatively low code, this episode is for you. Let’s dive in

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

**Kimi K2 Thinking is Here and It’s a 1 Trillion Parameter Beast! **([X](https://x.com/Kimi_Moonshot/status/1986449512538513505), [HF](https://huggingface.co/moonshotai/Kimi-K2-Thinking), [Tech Blog](https://moonshotai.github.io/Kimi-K2/thinking.html))

Let’s start with the news that got everyone’s energy levels skyrocketing right as we went live. Moonshot AI dropped Kimi K2 Thinking, an open-source, 1 trillion-parameter Mixture-of-Experts (MoE) model, and it’s an absolute monster.

This isn’t just a numbers game; Kimi K2 Thinking is designed from the ground up to be a powerful agent. With just around 32 billion active parameters during inference, a massive 256,000 token context window, and an insane tool-calling capacity. They’re claiming it can handle 200-300 sequential tool calls without any human intervention. 

The benchmarks are just as wild. On the Humanities Last Exam (HLE), they’re reporting a score of 44.9%, beating out both GPT-5 and Claude 4.5 Thinking. While it doesn’t quite top the charts on SWE-bench verified, it’s holding its own against the biggest closed-source models out there. Seeing an open-source model compete at this level is incredibly exciting.

During the show, we saw some truly mind-blowing demos, from a beautiful interactive visualization of gradient descent to a simulation of a virus attacking cells, all generated by the model. The model’s reasoning traces, which are exposed through the API, also seem qualitatively different from other models, showing a deep and thoughtful process. My co-hosts and I were blown away. The weights and a very detailed technical report are available on Hugging Face, so you can dive in and see for yourself. Shout out to the entire Moonshot AI team for this incredible release!

Other open source updates from this week

* HuggingFace released an open source “Smol Training Playbook” on training LLMs, it’s a 200+ interactive beast with visualizations, deep dives into pretraining, dataset, postraining and more! ([HF](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook))

* Ai2 launches OlmoEarth — foundation models + open, end-to-end platform for fast, high-resolution Earth intelligence ([X](https://x.com/allen_ai/status/1985719070407176577), [Blog](https://allenai.org/blog/olmoearth?utm_source=x&utm_medium=social&utm_campaign=olmoearth))

* LongCat-Flash-Omni — open-source omni-modal system with millisecond E2E spoken interaction, 128K context and a 560B ScMoE backbone ([X](https://x.com/Meituan_LongCat/status/1984398560973242733), [HF](https://huggingface.co/meituan-longca), [Announcement](https://github.com/meituan-longca))

**Big Tech’s Big Moves: Apple, Amazon, and OpenAI**

The big companies were making waves this week, starting with a blockbuster deal that might finally make Siri smart. Apple is reportedly will be paying Google around $1 billion per year to license a custom 1.2 trillion-parameter version of Gemini to power a revamped Siri.

This is a massive move. The Gemini model will run on Apple’s Private Cloud Compute, keeping user data walled off from Google, and will handle Siri’s complex summarizer and planner functions. After years of waiting for Apple to make a significant move in GenAI, it seems they’re outsourcing the heavy lifting for now while they work to catch up with their own in-house models. As a user, I don’t really care who builds the model, as long as Siri stops being dumb!

In more dramatic news, Perplexity revealed that Amazon sent them a legal threat to block their Comet AI assistant from shopping on [Amazon.com](Amazon.com). This infuriated me. My browser is my browser, and I should be able to use whatever tools I want to interact with the web. Perplexity took a strong stand with their [blog post](https://perplexity.ai/hub/blog/bullying-is-not-innovation), “Bullying is Not Innovation,” arguing that user agents are distinct from scrapers and act on behalf of the user with their own credentials. An AI assistant is just that—an assistant. It shouldn’t matter if I ask my wife or my AI to buy something for me on Amazon. This feels like a move by Amazon to protect its ad revenue at the expense of user choice and innovation, and I have to give major props to Perplexity for being so transparent and fighting back.

Finally, OpenAI continues its quest for infinite compute, announcing a multi-year strategic partnership with AWS. This comes on top of massive deals with NVIDIA, Microsoft, Oracle, and others, bringing their total commitment to compute into the trillions of dollars. It’s getting to a point where OpenAI seems “too big to fail,” as any hiccup could have serious repercussions for the entire tech economy, which is now heavily propped up by AI investment. Sam has clarified that they don’t think OpenAI wants to be too big to fail in a recent [post on X](https://x.com/sama/status/1986514377470845007), and that the recent miscommunications around the US government backstopping OpenAI’s infrastructure bailouts were taken out of context. 🤔 

**Coding with AI: The Evolution of MCP and New Dev Tools**

This week, we kicked off a new segment on the show: Coding with AI! Essentially realizing that we talk about AI coding a LOT, and decided to add a dedicated corner to it!  And we started with a fascinating development in the world of agentic tooling. Anthropic published a blog post arguing that the standard way of using the Model Context Protocol (MCP) — by loading full tool definitions into the context window — is inefficient.

Their solution? Have LLMs write code to interact with tools instead. This approach can slash token usage by over 98% in some cases. This idea sounded familiar, and that’s because Cloudflare had already [explored](https://blog.cloudflare.com/code-mode/) it with a feature called “Code Mode.” We were lucky enough to have [Kenton Varda](https://x.com/KentonVarda), one of the authors of the Code Mode post and head of engineering for Cloudflare Workers, join us to discuss this shift.

Kenton explained that LLMs are trained on vast amounts of code, making it a more “native language” for them than the artificial construct of tool calls. By generating code, agents can chain multiple tool calls together, process intermediate results, and operate much more efficiently without sending everything back through the neural network. While MCP still provides crucial standardization for discovering and authorizing tools, this “code execution” pattern seems to be the way forward for building more powerful and scalable agents.

Windsurfs CodeMaps and Cursor multi agent executions

In other coding with AI news, Windsurf has pushed an incredible feature, called CodeMaps. They will use their SWE-1 model to (quickly) generate Codemaps that will expalins a code-base to you, in a visual way. What starts where and goes where. It’s really useful to understand a new codebase or re-understand one you forgot about already! You can even chat with codemaps, to see if your overall system’s design is solid! Great addition that I’m sure will help many folks adopt Windsurf! 

And Cursor, another popular AI-native IDE, released a super-performant in-IDE browser and a wild multi-agent feature that queries multiple LLMs in parallel and then synthesizes their answers.

**This Week’s Tutorial**

I finally got around to building some serious automations for ThursdAI, and folks, N8N has been a game-changer. What used to take me 30+ minutes of manual work now happens automatically in the background.

Here’s what I built: A Telegram bot that takes Twitter/X links, fetches the tweets and all linked content, uses AI agents to extract and summarize the information, and then posts it to our announcement channel and my notes app. The coolest part? I built this whole thing in about 4 hours with the help of Atlas browser and GPT-5 literally telling me what to do at each step.

During the show, we even live-tested swapping out GPT-4o-mini for Kimi K2 - took literally 30 seconds to connect via OpenRouter. I went through my node and explains how this all works on the show, so if you’ve wanted to learn about n8n, check it out starting around 01:13:00. If you want to see how my automation turned out, it will be posting all my links to the new telegram channel [t.me/thursdai_news](http://t.me/thursdai_news) (expect it to be messy at first as I’m testing out the automation) 

**Robotics - Xpeng’s “Iron” humanoid: big vibes, few specs**

Another week, another humanoid robot that is supposedly “coming” in 2026! 

A humanoid from Xpeng went viral this week, marketed as “the most human‑like” robot with soft skin, bionic muscles, customizable sexes (yes, really, they have a woman humanoid), something called a VLT brain, and a 2026 production goal. Here’s what we didn’t get: a spec sheet. No DOF, speed, payload, compute TOPS, battery capacity, runtime, or safety pathway. No pricing, manufacturing strategy, or clear target markets. In other words: lots of sizzle, no steak.

Apparently, there was folks thinking Xpend pulled an Elon and put a human in a robot suit, making the CEO do the “we’ll cut a part of the soft skin to expose the robot underneath so you don’t think we’re lying” stunt. Which I agree, was very effective. 

But, If Xpeng is serious, the next thing we’ll see should be a crisp engineering document: joints, actuation, sensors, compute, and a locomotion/manipulation demo with independent measurements. Until then, treat this as a branding salvo and a reminder that the humanoid category is still sorting itself into “industrial payload first” versus “human likeness first” approaches. 

**Voice & Audio**

**Maya‑1: open‑source voice design from natural language**

We highlighted Maya‑1, a 3B Llama‑backboned TTS system designed to generate voices from natural language descriptions. Instead of picking from a menu, you describe the voice—age, accent, affect—and Maya conjures it. It supports real‑time streaming and over twenty “emotion tags.” The quality is compelling for its size and the Apache 2 license will make a lot of builders happy. There’s a growing middle class of TTS: tiny but expressive, good enough for in‑app narrators, prototyping, and even stylized content when you don’t want the constraints of commercial voice marketplaces.

**Inworld TTS: a new leader on independent rankings**

We also listened to Inworld’s latest, which currently tops the Artificial Analysis TTS leaderboard. It’s not open source, but the combo of expressivity, speed (sub‑250 ms), and multilingual support puts it firmly in the “commercially viable at scale” tier alongside the usual suspects. If you need SaaS TTS today and care about emotional range, add this to your shortlist. Pricing on their site targets availability rather than hobbyist tinkering, but the quality argues for itself.

Whew! For a week that started slow, it certainly ended with a bang. It just goes to show you can never count AI out. We’re seeing open source continue to push the boundaries, big tech making landscape-defining moves, and agentic AI becoming more powerful and accessible every day.

As always, thanks for tuning in. If you’re going to be at the [AI.engineer](AI.engineer) conference in New York, please hit me up—I’d love to meet you.

TL;DR and Show Notes + Links

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) @yampeleg [@nisten](http://x.com/@nisten)

* Kenton Varda @ Cloudflare ([@KentonVarda](https://x.com/KentonVarda))

* **Open Source LLMs**

* Smol Training Playbook — a 200+ page, end-to-end guide to reliably pretrain and operate LLMs ([X](https://x.com/eliebakouch/1983930328751153159), [Announcement](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook))

* Ai2 launches OlmoEarth — foundation models + open, end-to-end platform for fast, high-resolution Earth intelligence ([X](https://x.com/allen_ai/1985719070407176577), [Blog](https://allenai.org/blog/olmoearth?utm_source=x&utm_medium=social&utm_campaign=olmoearth))

* Moonshot AI releases Kimi K2 Thinking — an open-source 1T-parameter MoE agent with 256K context and huge tool-calling capacity ([X](https://x.com/Kimi_Moonshot/1986449512538513505), [HF](https://huggingface.co/moonshotai/Kimi-K2-Thinking), [Blog](https://moonshotai.github.io/Kimi-K2/thinki), [Arxiv](https://huggingface.co/papers/2510.26692))

* LongCat flash Omni - 560B (27A) omni model (text, audio, video input)

* **Big CO LLMs + APIs**

* Apple will pay roughly $1B/year to license a custom 1.2 trillion‑parameter Google Gemini model to power a revamped Siri ([X](https://x.com/markgurman/1986150242698637591), [Announcement](https://www.bloomberg.com/news/articles/2025-11-05/apple-plans-to-use-1-2-trillion-parameter-google-gemini-model-to-power-new-siri?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc2MjM3MDAzOSwiZXhwIjoxNzYyOTc0ODM5LCJhcnRpY2xlSWQiOiJUNTZETzhHUTdMMFIwMCIsImJjb25uZWN0SWQiOiJDNEVEQ0FFMUZBMDU0MEJFQTI0QTlGMjExQzFFOTA4MCJ9._aWk2P25J89KBRkJQ_KdbwuULLM8yUtrPCPfRmsUfSs))

* Perplexity says Amazon issued a legal threat to block Comet AI assistants from shopping on Amazon ([X](https://x.com/perplexity_ai/1985774904911020319), [Blog](https://perplexity.ai/hub/blog/bullying-is-not-innovation))

* AWS announces multi-year strategic infrastructure partnership with OpenAI to power ChatGPT inference, training, and agentic AI ([X](https://x.com/ajassy/1985351258333643172))

* **Robotics**

* Xpeng unveils ‘Iron’ humanoid claiming ‘most human-like’ design with soft skin, bionic muscles, VLT brain and a 2026 production plan ([X](https://x.com/humanoidsdaily/1986063827327201757))

* **Coding with AI**

* Anthropic shows how running MCP-connected tools as code slashes token use and scales agents ([X](https://x.com/AnthropicAI/1985846791842250860), [Blog](https://www.anthropic.com/engineering/code-execution-with-mcp))

* Windsurf Codemaps — AI‑annotated, navigable maps of your codebase powered by SWE-1.5 (Fast) and Sonnet 4.5 (Smart) ([X](https://x.com/cognition/1985755284527010167), [Announcement](https://cognition.ai/blog/codemaps))

* Conversation with Kenton Varda ([@KentonVarda](https://x.com/KentonVarda)) from Cloudflare about MCP and Code Mode

* Cursor added in IDE browser - very performant!

* **Audio & Video**

* Maya-1 - Open source voice generation model.

* Inworld TTS - new #1 on artifical analysis benchmark.

* **Tools & Gadgets**

* Sandbar launches Stream — a voice-first personal assistant — and Stream Ring, a wearable ‘mouse for voice’, available for preorder ([X](https://x.com/sandbar/status/1986112726889078911), [Blog](https://www.sandbar.com/stream)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-nov-6-2025-kimis-1t-thinking/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-nov-6-2025-kimis-1t-thinking?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3ODIzMTU1OSwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.k6cFVokVpTFW7F_weCQScyDI2A-VEWVsF24x9oRpUjs&utm_campaign=CTA_5).

---

