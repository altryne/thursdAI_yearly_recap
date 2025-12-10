# ThursdAI - Apr 17 - OpenAI o3 is SOTA llm, o4-mini, 4.1, mini, nano, G. Flash 2.5, Kling 2.0 and 🐬 Gemma? Huge AI week + A2A protocol interview

**Date:** April 17, 2025  
**Duration:** 1:55:51  
**Link:** [https://sub.thursdai.news/p/thursdai-apr-17-openai-o3-is-sota](https://sub.thursdai.news/p/thursdai-apr-17-openai-o3-is-sota)

---

## Description

Hey everyone, Alex here 👋

Wow. Just… wow. What a week, folks. Seriously, this has been one for the books. 

This week was dominated by OpenAI's double whammy: first the **GPT-4.1 family** dropped with a mind-boggling 1 million token context window, followed swiftly by the new flagship reasoning models, **o3** and **o4-mini**, which are already blowing minds with their agentic capabilities. We also saw significant moves from Google with **VEO-2** going GA, the fascinating **A2A protocol** launch (we had an amazing interview with Google's Todd Segal about it!), and even an attempt to talk to dolphins with **DolphinGemma**. Kling stepped up its video game, Cohere dropped SOTA multimodal embeddings, and ByteDance made waves in image generation. Plus, the open-source scene had some interesting developments, though perhaps overshadowed by the closed-source giants this time.

o3 has absolutely taken the crown as the conversation piece, so lets start with it (as always, TL;DR and shownotes at the end, and here's the embedding of our live video show) 

Big Company LLMs + APIs

OpenAI o3 & o4‑mini: SOTA Reasoning Meets Tool‑Use ([Blog](https://openai.com/index/introducing-o3-and-o4-mini/), [Watch Party](https://youtube.com/live/2G-VwWxKCkk?feature=share))

The long awaited o3 models (promised to us in the last days of x-mas) is finally here, and it did NOT disappoint and well.. even surprised! 

o3 is not only SOTA on nearly all possible logic, math and code benchmarks, which is to be expected from the top reasoning model, it also, and I think for the first time, is able to use tools during its reasoning process. Tools like searching the web, python coding, image gen (which it... can zoom and rotate and crop images, it's nuts) to get to incredible responses faster. 

Tool using reasoner are... almost AGI? 

This is the headline feature for me. For the first time, these o-series models have full, autonomous access to all built-in tools (web search, Python code execution, file search, image generation with Sora-Image/DALL-E, etc.). They don't just use tools when told; they decide when and how to chain multiple tool calls together to solve a problem. We saw logs with 600+ consecutive tool calls! This is agent-level reasoning baked right in.

Anecdote: We tested this live with a complex prompt: "generate an image of a cowboy that on his head is the five last digits of the hexadecimal code of the MMMU score of the latest Gemini model." o3 navigated this multi-step task flawlessly: figuring out the latest model was Gemini 2.5, searching for its MMMU score, using the Python tool to convert it to hex and extract the digits, and then using the image generation tool. It involved multiple searches and reasoning steps. Absolutely mind-blowing 🤯.

Thinking visually with images

This one also blew my mind, this model is SOTA on multimodality tasks, and a reason for this, is these models can manipulate and think about the images they received. Think... cropping, zooming, rotating. The models can now perform all these tasks to multimodal requests from users. Sci-fi stuff! 

Benchmark Dominance: As expected, these models crush existing benchmarks.

o3 sets new State-of-the-Art (SOTA) records on Codeforces (coding competitions), SWE-bench (software engineering), MMMU (multimodal understanding), and more. It scored a staggering $65k on the Freelancer eval (simulating earning money on Upwork) compared to o1's $28k!

o4-mini is no slouch either. It hits 99.5% on AIME (math problems) when allowed to use its Python interpreter and beats the older o3-mini on general tasks. It’s a reasoning powerhouse at a fraction of the cost.

**Incredible Long Context Performance**

Yam highlighted this – on the Fiction Life benchmark testing deep comprehension over long contexts, o3 maintained nearly 100% accuracy up to 120,000 tokens, absolutely destroying previous models including Gemini 2.5 Pro and even the new GPT-4.1 family on this specific eval. While its context window is currently 200k (unlike 4.1's 1M), its performance within that window is unparalleled.

**Cost-Effective Reasoning:** They're not just better, they're *cheaper* for the performance you get.

* **o3:** $10 input / $2.50 cached / $40 output per million tokens.

* **o4-mini:** $1.10 input / $0.275 cached / $4.40 output per million tokens. (Cheaper than GPT-4.0!)

**Compute Scaling Validated:** OpenAI confirmed these models used >10x the compute of o1 and leverage test-time compute scaling (spending longer on harder problems), further proving their scaling law research.

**Memory Integration:** Both models integrate with ChatGPT's recently upgraded memory feature which has access to all your previous conversations (which we didn't talk about but is absolutely amazing, try asking o3 stuff it knows about you and have ti draw conclusions!)

**Panel Takes & Caveats:**While the excitement was palpable, Yam noted some community observations about potential "rush" – occasional weird hallucinations or questionable answers compared to predecessors, possibly a side effect of cramming so much training data. Nisten, while impressed, still found the *style* of **GPT-4.1** preferable for specific tasks like generating structured medical notes in his tests. It highlights that benchmarks aren't everything, and specific use cases require evaluation (shameless plug: use tools like W&B Weave for this!).

I'll add my own, I use all the models every week to help me draft posts, and o3 was absolute crap about matching my tone. % of what's written above it was able to mimic. Gemini remains undefeated for me and this task.

Though, Overall, o3 and o4-mini feel like a paradigm shift towards more autonomous, capable AI assistants. The agentic future feels a whole lot closer.

**OpenAI Launches GPT-4.1 Family: 1 Million Tokens & Killing 4.5!** ([Our Coverage](https://www.youtube.com/live/A5-Zxj816J0), [Prompting guide](https://x.com/noahmacca/status/1911898549308280911))

Before the o3 shockwave, Monday brought its own major AI update: the **GPT-4.1 family**. This was the API-focused release, delivering massive upgrades for developers.

**The Headline:** **One Million Token Context Window!** 🤯 Yes, you read that right. All three new models – **GPT-4.1** (flagship), **GPT-4.1 mini** (cheaper/faster), and **GPT-4.1 nano** (ultra-cheap/fast) – can handle up to 1 million tokens. This is a monumental leap, enabling use cases that were previously impossible or required complex chunking strategies.

**Key Details:**

Goodbye GPT-4.5! 

In a surprising twist, OpenAI announced they are *deprecating* the recently introduced (and massive) GPT-4.5 model within 90 days in the API. Why? Because **GPT-4.1 actually outperforms it** on key benchmarks like SW-Bench, Aider Polyglot, and the new long-context MRCR eval, while being far cheaper to run. It addresses the confusion many had: why was 4.5 seemingly *worse* than 4.1? It seems 4.5 was a scaling experiment, but 4.1 represents a more optimized, better-trained checkpoint on superior data. RIP 4.5, we hardly knew ye (in the API).

**The Prompt Sandwich Surprise! 🥪:** 

This was wild. Following OpenAI's new prompting guide, I tested the "sandwich" technique (instructions -> context -> instructions *again*) on my hard reasoning eval using [W&B Weave](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=apr17).

For **GPT-4.1**, it made no difference (still got 48%). But for **GPT-4.1 mini**, the score jumped from 31% to **49%** – essentially matching the full 4.1 model just by repeating the prompt! That's a crazy performance boost for a simple trick. Even nano saw a slight bump. **Lesson: Evaluate prompt techniques!** Don't assume they won't work.

**Million-Token Recall Confirmed:** Using Needle-in-Haystack and their newly open-sourced **MRCR benchmark** (Multi-round Co-reference Resolution – more in Open Source), OpenAI showed near-perfect recall across the *entire* 1 million token window for **all three models**, even nano! This isn't just a theoretical limit; the recall seems robust.

**Multimodal Gains:** Impressively, **4.1 mini** hit **72% on Video-MME**, pushing SOTA for long-video Q&A in a mid-tier model by analyzing frame sequences. 

4.1 mini seems to be the absolute powerhouse of this release cycle, it nearly matches the intelligence of the previous 4o, while being significantly cheaper and much much faster with 1M context window! 

Windsurf (and Cursor) immediately made the 4.1 family available, offering a **free week** for users to test them out (likely to gather feedback and maybe influenced by certain acquisition rumors 😉). Devs reported them feeling snappier and less verbose than previous models.

**Who Should Use Which OpenAI API?**

My initial take:

* **For complex reasoning, agentic tasks, or just general chat:** Use **o3** (if you need the best) or **o4-mini** (for amazing value/speed).

* **For API development, especially coding or long-context tasks:** Evaluate the **GPT-4.1 family**. Start with **4.1 mini** – it's likely the sweet spot for performance/cost, especially with smart prompting. Use **4.1** if mini isn't quite cutting it. Use **nano** for simple, high-volume tasks like translation or basic classification.

The naming is still confusing (thanks Nisten for highlighting the UI nightmare!), but the capability boost across the board is undeniable.

**Hold the Phone! 🚨 Google Fires Back with Gemini 2.5 Flash in Breaking News**

Just when we thought the week couldn't get crazier, Google, likely reacting to OpenAI's rapid-fire launches, just dropped **Gemini 2.5 Flash** into preview via the [Gemini API](https://ai.google.dev/docs/gemini_api_overview) (in AI Studio and Vertex AI). This feels like Google's direct answer, aiming to blend reasoning capabilities with speed and cost-effectiveness.

**The Big Twist: Controllable Thinking Budgets!**Instead of separate models like OpenAI, Gemini 2.5 Flash tries to do **both reasoning and speed/cost efficiency in one model**. The killer feature? Developers can set a **"thinking budget"** (0 to 24,576 tokens) per API call to control the trade-off:

* **Low/Zero Budget:** Prioritizes speed and low cost (very cheap: **$0.15 input / $0.60 output** per 1M tokens), great for simpler tasks.

* **Higher Budget:** Allows the model multi-step reasoning "thinking" for better accuracy on complex tasks, at a higher cost (**$3.50 output** per 1M tokens, including reasoning tokens).

This gives  granular control over the cost/quality balance *within the same model*.

**Performance & Specs:**Google claims strong performance, ranking just behind Gemini 2.5 Pro on Hard Prompts in ChatBot Arena and showing competitiveness against o4-mini and Sonnet 3.7 in their benchmarks, especially given the flexible pricing.

Key specs are right up there with the competition:

* **Multimodal Input:** Text, Images, Video, Audio

* **Context Window:** **1 million tokens** (matching GPT-4.1!)

* **Knowledge Cutoff:** January 2025

**How to Control Thinking:**Simply set the thinking_budget parameter in your API call (Python/JS examples available in their docs). If unspecified, the model decides automatically.

**My Take:** This is a smart play by Google. The controllable thinking budget is a unique and potentially powerful feature for optimizing across different use cases without juggling multiple models. With 1M context and competitive pricing, Gemini 2.5 Flash is immediately a major contender in the ongoing AI arms race. Definitely one to evaluate! Find more in the [developer docs](https://ai.google.dev/docs) and [Gemini Cookbook](https://ai.google.dev/examples).

Open Source: LLMs, Tools & more

OpenAI open sources MRCR eval and Codex (Mrcr [HF](https://huggingface.co/datasets/openai/mrcr), Codex [Github](https://github.com/openai/codex))

Let's face it, this isn't the open source OpenAI coverage I was hoping for, Sam promised us an open source model, and they are about to drop this, I'd assume close to Google IO (May 20th) to steal thunder. But OpenAI did make OpenSource waves this week in addition to the above huge stories. 

MRCR is a way to evaluate long context complex tasks, and they have taken this Gemini research and open sourced a dataset for this eval. 👏 

But also, they have dropped the Codex CLI tool, which is a coding partner using o4-mini and o3 and made that tool open source as well (Unlike anthropic with Claude Code), which in turn saw 86+ Pull Requests approved within the first 24 hours! 

The best part about this CLI, is that it's hardened security, using **Apple Seatbelt** which limits it execution to the current directory + temp files (on a mac at least) 

Other Open Source Updates

While OpenAI's contributions were notable, it wasn't the only action this week:

* **Microsoft's BitNet v1.5 (**[**HF**](https://huggingface.co/collections/microsoft/BitNet)**)**: Microsoft quietly dropped updates to BitNet, continuing their exploration into ultra-low-bit (ternary) models for efficiency. As Nisten pointed out on the show though, keep in mind these still use some higher-precision layers, so they aren't *purely* 1.5-bit in practice just yet. Important research nonetheless!

* **INTELLECT-2 Distributed RL (**[**Blog**](https://www.primeintellect.ai/blog/intellect-2)**, **[**X**](https://x.com/primeintellect_ai)**)**: Prime Intellect did something wild – training **INTELLECT-2**, a 32B model, using globally distributed, permissionless reinforcement learning. Basically, anyone with a GPU could potentially contribute. Fascinating glimpse into decentralized training!

* [**Z.ai**](Z.ai)** (Formerly ChatGLM) & GLM-4 Family (**[**X**](https://x.com/Zai_org/status/1779846143024941199)**, **[**HF**](https://huggingface.co/collections/THUDM)**, **[**GitHub**](https://github.com/THUDM/GLM-4)**)**: The team behind ChatGLM rebranded to [**Z.ai**](Z.ai) and released their GLM-4 family (up to 32B parameters) under the very permissive **MIT license**. They're claiming performance competitive with much larger models like Qwen 72B, which is fantastic news for commercially usable open source!

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

This Week's Buzz: Playground Updates & A Deep Dive into A2A

On the Weights & Biases front, it's all about enabling developers to navigate this new model landscape.

**Weave Playground Supports GPT-4.1 and o3/o4-mini (**[**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fweave_wb%2Fstatus%2F1912246450857341092)**)**

With all these new models dropping, how do you actually *choose* which one is best for *your* application? You need to evaluate! Our **W&B Weave Playground** now has full support for the new **GPT-4.1 family** and the **o3/o4-mini** models.

If you're using Weave to monitor your LLM apps in production, you can easily grab a trace of a real user interaction, open it in the Playground, and instantly retry that exact same call (with all its context and history) using any of the new models side-by-side. It’s the fastest way to see how o3 compares to 4.1-mini or how Claude 3.7 stacks up against o4-mini *on your specific data*. Essential for making informed decisions in this rapidly changing environment.

**Deep Dive: Understanding Google's A2A Protocol with Todd Segal**

This was a highlight of the show for me. We were joined by **Todd Segal**, a Principal Software Engineer at Google working directly on the new **Agent-to-Agent (A2A) protocol**. There was some confusion initially about how A2A relates to the increasingly popular **Model Context Protocol (MCP)**, so getting Todd's perspective was invaluable. W&B is a proud launch partner for the A2A protocol!

**Key Takeaways from our Chat:**

* **A2A vs. MCP: Complementary, Not Competitive:** Todd was clear: Google sees these as solving different problems. **MCP is for Agents talking to Tools** (structured, deterministic capabilities). **A2A is for Agents talking to other Agents** (unstructured, stateful, unpredictable, evolving interactions). Think of MCP like calling an API, and A2A like delegating a complex task to another expert service.

* **The Need for A2A:** It emerged from the need for specialized, domain-expert agents (built internally or by partners like Salesforce) to collaborate on complex, long-running tasks (e.g., booking a multi-vendor trip, coordinating an enterprise workflow) where simple tool calls aren't enough. Google's **Agent Space** product heavily utilizes A2A internally.

* **Capability Discovery & Registries:** A core concept is agents advertising their capabilities via an "agent card" (like a business card or resume). Todd envisions a future with multiple **registries** (public, private, enterprise-specific) where agents can discover other agents best suited for a task. This registry system is on the roadmap.

* **Async & Long-Running Tasks:** A2A is designed for tasks that might take minutes, hours, or even days. It uses a central **"Task" abstraction** which is stateful. Agents communicate updates (status changes, generated artifacts, requests for more info) related to that task.

* **Push Notifications:** For very long tasks, A2A supports a **push notification** mechanism. The client agent provides a secure callback URL, and the server agent can push updates (state changes, new artifacts) even if the primary connection is down. This avoids maintaining costly long-lived connections.

* **Multimodal Communication:** The protocol supports negotiation of modalities beyond text, including rendering content within **iframes** (for branded experiences) or exchanging **video/audio streams**. Essential for future rich interactions.

* **Security & Auth:** A2A deliberately **doesn't reinvent the wheel**. It relies on standard **HTTP headers** to carry authentication (OAuth tokens, internal enterprise credentials). Identity/auth handshakes happen "out of band" using existing protocols (OAuth, OIDC, etc.), and the resulting credentials are passed with A2A requests. Your user identity flows through standard mechanisms.

* **Observability:** Todd confirmed **OpenTelemetry (OTel)** support is planned for the SDKs. Treating agents like standard microservices means leveraging existing observability tools (like W&B Weave!) is crucial for tracing and debugging multi-agent workflows.

* **Open Governance:** While currently in a Google repo, the plan is to move A2A to a **neutral foundation** (like Linux Foundation) with a fully **open governance model**. They want this to be a true industry standard.

* **Getting Started:** Check out the **GitHub repo (**[**github.com/google/A2A**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fgoogle%2FA2A)**)**, participate in discussions, file issues, and send PRs!

My take: A2A feels like a necessary piece of infrastructure for the next phase of AI agents, enabling complex, coordinated actions across different systems and vendors. While MCP handles the "how" of using tools, A2A handles the "who" and "what" of inter-agent delegation. Exciting times ahead! Big thanks to Todd for shedding light on this.

Vision & Video: Veo-2 Arrives, Kling Gets Slicker

The visual AI space keeps advancing rapidly.

**Veo-2 Video Generation Hits GA in Vertex AI & Gemini App (**[**Blog**](https://developers.googleblog.com/en/veo-2-video-generation-now-generally-available/)**, **[***Try It***](http://ai.dev)**)**

Google's answer to Sora and Kling, **Veo-2**, is now **Generally Available (GA)** for all Google Cloud customers via **Vertex AI**. You can also access it in the **Gemini app**.

Veo-2 produces stunningly realistic and coherent video, making it a top contender alongside OpenAI's Sora and  Kling. Having it easily accessible in Vertex AI is a big plus for developers on Google Cloud.

I've tried and keep tyring all of them, VEO2 is an absolute beast in realism. 

**Kling 2.0 Creative Suite: A One-Stop Shop for Video AI? (**[**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne%2Fstatus%2F1912043121497850242)**, **[**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fklingai.com)**)**

Kuaishou's **Kling** model also got a major upgrade, evolving into a full **Kling 2.0 Creative Suite**.

*Anecdote:* I actually stayed up quite late one night trying to piece together info from a Chinese live stream about this release! The dedication is real, folks. 😂

**What's New:**

* **Kling 2.0 Master:** The core video model, promising better motion, physics, and facial consistency (still 5s clips for now, but 30s/4K planned).

* **Kolors 2.0:** An integrated image generation and restyling model (think Midjourney-style filters).

* **MVL (Multimodal Visual Language) Prompting:** This is killer! You can now **inline images directly within your text prompt** for precise control (e.g., "Swap the hoodie in @video1 with the style of @image2"). This offers granular control artists have been craving.

* **Multi-Elements Editor:** A timeline-based editor to stitch clips, add lip-sync, sound effects (including generated ones like "car horn"), and music.

* **Global Access:** No more Chinese phone number requirement! Available worldwide at [**klingai.com**](klingai.com).

* **Official API via FAL:** Developers can now integrate Kling 2.0 via our friends at **⚡ FAL Generative Media Cloud**.

Kling is clearly aiming to be a holistic creative platform, reducing the need to jump between 17 different AI tools for image gen, video gen, editing, and sound. The MVL prompting is particularly innovative. Very impressive package.

Voice & Audio: Talking to Dolphins? 🐬

**DolphinGemma: Google AI Listens to Flipper (**[**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fblog.google%2Ftechnology%2Fai%2Fdolphingemma%2F)**)**

In perhaps the most delightful news of the week, Google, in collaboration with Georgia Tech and the Wild Dolphin Project, announced DolphinGemma. 

It's a ~400M parameter audio model based on the Gemma architecture (using SoundStream for audio tokenization) trained specifically on decades of recorded dolphin clicks, whistles, and pulses.The goal? To decipher the potential syntax and structure within dolphin communication and eventually enable rudimentary two-way interaction using underwater communication devices. It runs on a Pixel phone for field deployment.

This is just awesome. Using AI not just for human tasks but to potentially bridge the communication gap with other intelligent species is genuinely inspiring. We joked on the show about doing a segment of just dolphin noises – maybe next time if DolphinGemma gets an API! 🤣

AI Art & Diffusion & 3D: Seedream Challenges the Champs

**Seedream 3.0: ByteDance's Bilingual Image Powerhouse (**[**Tech post**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fteam.doubao.com%2Fen%2Ftech%2Fseedream3_0)**, **[**arXiv**](https://www.google.com/url?sa=E&q=https%3A%2F%2Farxiv.org%2Fabs%2F2504.11346)**, **[**AIbase news**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.aibase.com%2Fnews%2F17208)**)**

ByteDance wasn't just busy with video; their Seed team announced **Seedream 3.0**, a powerful bilingual text-to-image model.

**Highlights:**

* Generates native **2048x2048** images.

* Fast inference (**~3 seconds** for 1Kx1K on an A100).

* Excellent **bilingual (Chinese/English) text rendering**, even small fonts.

* Uses **Scaled-ROPE-v2** for better high-resolution generation without artifacts.

* Claims to outperform SDXL-Turbo and Qwen-Image on fidelity and prompt adherence benchmarks.

* Available via Python SDK and REST API within their Doubao Studio and coming soon to [dreamina.com](http://dreamina.com) 

Phew! We made it. What an absolute avalanche of news. OpenAI truly dominated with the back-to-back launches of the hyper-capable o3/o4-mini and the massively scaled GPT-4.1 family. Google countered strongly with the versatile Gemini 2.5 Flash, key GA releases like Veo-2, and the strategically important A2A protocol. The agent ecosystem took huge leaps forward with both A2A and broader MCP adoption. And we saw continued innovation in multimodal embeddings, video generation, and even niche areas like bioacoustics and low-bit models.

If you feel like you missed anything (entirely possible this week!), the TL;DR and links below should help. Please subscribe if you haven't already, and share this with a friend if you found it useful – it's the best way to support the show!

I have a feeling next week won't be any slower. Follow us on X/Twitter for breaking news between shows!

Thanks for tuning in, keep building, keep learning, and I'll see you next Thursday!

Alex

TL;DR and Show Notes

*Everything we covered today in bite-sized pieces with links!*

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([**@altryne**](https://www.google.com/url?sa=E&q=http%3A%2F%2Fx.com%2F%40altryne))

* Co Hosts - [**@WolframRvnwlf**](https://www.google.com/url?sa=E&q=http%3A%2F%2Fx.com%2F%40WolframRvnwlf) [**@yampeleg**](https://www.google.com/url?sa=E&q=x.com%2F%40yampeleg) [**@nisten**](https://www.google.com/url?sa=E&q=http%3A%2F%2Fx.com%2F%40nisten) [**@ldjconfirmed**](https://www.google.com/url?sa=E&q=http%3A%2F%2Fx.com%2F%40ldjconfirmed))

* Todd Segal - Principal Software Engineer @ Google - Working on A2A Protocol

* **Big CO LLMs + APIs**

* 👑 OpenAI launches **o3** and **o4-mini** in chatGPT & API ([**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Findex%2Fintroducing-o3-and-o4-mini%2F), [**Our Coverage**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fyoutube.com%2Flive%2F2G-VwWxKCkk), [**o3 and o4-mini announcement**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Findex%2Fintroducing-o3-and-o4-mini%2F))

* OpenAI launches **GPT 4.1, 4.1-mini and 4.1-nano** in **API** ([**Our Coverage**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.youtube.com%2Flive%2FA5-Zxj816J0), [**Prompting guide**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fnoahmacca%2Fstatus%2F1911898549308280911))

* 🚨 Google launches **Gemini 2.5 Flash** with controllable thinking budgets ([**Blog Post - Placeholder Link**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fblog.google%2Ftechnology%2Fai%2Fgoogle-gemini-update-flash-extension%2F), [**API Docs**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fai.google.dev%2Fdocs))

* Mistral classifiers Factory

* Claude does research + workspace integration ([**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.anthropic.com%2Fnews%2Fresearch))

* Cohere Embed‑4 — Multimodal embeddings for enterprise search ([**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fcohere.com%2Fblog%2Fembed-4), [**Docs Changelog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fdocs.cohere.com%2Fv2%2Fchangelog%2Fembed-multimodal-v4), [**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fcohere%2Fstatus%2F1912128813104078999))

* **Open Source LLMs**

* OpenAI open sources MRCR Long‑Context Benchmark ([**Hugging Face**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fdatasets%2Fopenai%2Fmrcr))

* Microsoft BitNet v1.5 ([**HF**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fcollections%2Fmicrosoft%2FBitNet))

* INTELLECT‑2 — Prime Intellect’s 32B “globally‑distributed RL” experiment ([**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.primeintellect.ai%2Fblog%2Fintellect-2), [**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fprimeintellect_ai))

* [Z.ai](Z.ai) (previously chatGLM) + GLM‑4‑0414 open‑source family ([**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FZai_org%2Fstatus%2F1779846143024941199), [**HF Collection**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fcollections%2FTHUDM), [**GitHub**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FTHUDM%2FGLM-4))

* **This weeks Buzz + MCP/A2A**

* Weave playground support for GPT 4.1 and o3/o4-mini models ([**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fweave_wb%2Fstatus%2F1912246450857341092))

* Chat with Todd Segal - A2A Protocol ([**GitHub Spec**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fgoogle%2FA2A))

* **Vision & Video**

* **Veo‑2 Video Generation in GA, Gemini App** ([**Dev Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fdevelopers.googleblog.com%2Fen%2Fveo-2-video-generation-now-generally-available%2F))

* **Kling 2.0 Creative Suite** ([**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne%2Fstatus%2F1912043121497850242), [**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fklingai.com))

* ByteDance public Seaweed-7B, a video generation foundation model ([**seaweed.video**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fseaweed.video%2F))

* **Voice & Audio**

* **DolphinGemma** — Google AI tackles dolphin communication ([**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fblog.google%2Ftechnology%2Fai%2Fdolphingemma%2F))

* **AI Art & Diffusion & 3D**

* **Seedream 3.0 bilingual image diffusion – ByteDance** ([**Tech post**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fteam.doubao.com%2Fen%2Ftech%2Fseedream3_0), [**arXiv**](https://www.google.com/url?sa=E&q=https%3A%2F%2Farxiv.org%2Fabs%2F2504.11346), [**AIbase news**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.aibase.com%2Fnews%2F17208))

* **Tools**

* OpenAI debuts Codex CLI, an open source coding tool for terminals ([**Github**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex))

* Use o3 with Windsurf (which OpenAI is rumored to buy at $3B) via the mac app integration + write back + multiple files 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-apr-17-openai-o3-is-sota/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-apr-17-openai-o3-is-sota?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2MTU2NjkzOCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.NhVIknHwPyAwb64UpE1sqJDUBHbjL5K6_XdUSHuXvG0&utm_campaign=CTA_5).
