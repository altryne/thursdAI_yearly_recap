# ThursdAI Episodes - Q4 2025

Total Episodes: 11

---

## 📆 ThursdAI - Dec 4, 2025 - DeepSeek V3.2 Goes Gold Medal, Mistral Returns to Apache 2.0, OpenAI Hits Code Red, and US-Trained MOEs Are Back!

**Date:** December 05, 2025  
**Duration:** 1:33:54  
**Link:** [https://sub.thursdai.news/p/thursdai-dec-4-2025-deepseek-v32](https://sub.thursdai.news/p/thursdai-dec-4-2025-deepseek-v32)

Hey yall, Alex here 🫡 

Welcome to the first ThursdAI of December! Snow is falling in Colorado, and AI releases are falling even harder. This week was genuinely one of those “drink from the firehose” weeks where every time I refreshed my timeline, another massive release had dropped.

We kicked off the show asking our co-hosts for their top AI pick of the week, and the answers were all over the map: Wolfram was excited about Mistral’s return to Apache 2.0, Yam couldn’t stop talking about Claude Opus 4.5 after a full week of using it, and Nisten came out of left field with an AWQ quantization of Prime Intellect’s model that apparently runs incredibly fast on a single GPU. As for me? I’m torn between Opus 4.5 (which literally fixed bugs that Gemini 3 created in my code) and DeepSeek’s gold-medal winning reasoning model.

Speaking of which, let’s dive into what happened this week, starting with the open source stuff that’s been absolutely cooking. 

**Open Source LLMs**

**DeepSeek V3.2: The Whale Returns with Gold Medals**

The whale is back, folks! DeepSeek released two major updates this week: V3.2 and V3.2-Speciale. And these aren’t incremental improvements—we’re talking about an open reasoning-first model that’s rivaling GPT-5 and Gemini 3 Pro with actual gold medal Olympiad wins.

Here’s what makes this release absolutely wild: DeepSeek V3.2-Speciale is achieving 96% on AIME versus 94% for GPT-5 High. It’s getting gold medals on IMO (35/42), CMO, ICPC (10/12), and IOI (492/600). This is a 685 billion parameter MOE model with MIT license, and it literally broke the benchmark graph on HMMT 2025—the score was so high it went outside the chart boundaries. That’s how you DeepSeek, basically.

But it’s not just about reasoning. The regular V3.2 (not Speciale) is absolutely crushing it on agentic benchmarks: 73.1% on SWE-Bench Verified, first open model over 35% on Tool Decathlon, and 80.3% on τ²-bench. It’s now the second most intelligent open weights model and ranks ahead of Grok 4 and Claude Sonnet 4.5 on Artificial Analysis.

The price is what really makes this insane: 28 cents per million tokens on OpenRouter. That’s absolutely ridiculous for this level of performance. They’ve also introduced DeepSeek Sparse Attention (DSA) which gives you 2-3x cheaper 128K inference without performance loss. LDJ pointed out on the show that he appreciates how transparent they’re being about not quite matching Gemini 3’s efficiency on reasoning tokens, but it’s open source and incredibly cheap.

One thing to note: V3.2-Speciale doesn’t support tool calling. As Wolfram pointed out from the model card, it’s “designed exclusively for deep reasoning tasks.” So if you need agentic capabilities, stick with the regular V3.2.

Check out the [full release on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V3.2) or read the [announcement](https://platform.deepseek.com/blog/deepseek-v3-2).

Mistral 3: Europe’s Favorite AI Lab Returns to Apache 2.0

Mistral is back, and they’re back with fully open Apache 2.0 licenses across the board! This is huge news for the open source community. They released two major things this week: Mistral Large 3 and the Ministral 3 family of small models.

Mistral Large 3 is a 675 billion parameter MOE with 41 billion active parameters and a quarter million (256K) context window, trained on 3,000 H200 GPUs. There’s been some debate about this model’s performance, and I want to address the elephant in the room: some folks saw a screenshot showing Mistral Large 3 very far down on Artificial Analysis and started dunking on it. But here’s the key context that Merve from Hugging Face pointed out—this is the only non-reasoning model on that chart besides GPT 5.1. When you compare it to other instruction-tuned (non-reasoning) models, it’s actually performing quite well, sitting at #6 among open models on LMSys Arena.

Nisten checked LM Arena and confirmed that on coding specifically, Mistral Large 3 is scoring as one of the best open source coding models available. Yam made an important point that we should compare Mistral to other open source players like Qwen and DeepSeek rather than to closed models—and in that context, this is a solid release.

But the real stars of this release are the Ministral 3 small models: 3B, 8B, and 14B, all with vision capabilities. These are edge-optimized, multimodal, and the 3B actually runs completely in the browser with WebGPU using transformers.js. The 14B reasoning variant achieves 85% on AIME 2025, which is state-of-the-art for its size class. Wolfram confirmed that the multilingual performance is excellent, particularly for German.

There’s been some discussion about whether Mistral Large 3 is a DeepSeek finetune given the architectural similarities, but Mistral claims these are fully trained models. As Nisten noted, even if they used similar architecture (which is Apache 2.0 licensed), there’s nothing wrong with that—it’s an excellent architecture that works. Lucas Atkins later confirmed on the show that “Mistral Large looks fantastic... it is DeepSeek through and through architecture wise. But Kimi also does that—DeepSeek is the GOAT. Training MOEs is not as easy as just import deepseak and train.”

Check out [Mistral Large 3](https://huggingface.co/collections/mistralai/mistral-large-3) and [Ministral 3](https://huggingface.co/collections/mistralai/ministral-3) on Hugging Face.

Arcee Trinity: US-Trained MOEs Are Back

We had Lucas Atkins, CTO of Arcee AI, join us on the show to talk about their new Trinity family of models, and this conversation was packed with insights about what it takes to train MOEs from scratch in the US.

Trinity is a family of open-weight MOEs fully trained end-to-end on American infrastructure with 10 trillion curated tokens from [Datology.ai](Datology.ai). They released Trinity-Mini (26B total, 3B active) and Trinity-Nano-Preview (6B total, 1B active), with Trinity-Large (420B parameters, 13B active) coming in mid-January 2026.

The benchmarks are impressive: Trinity-Mini hits 84.95% on MMLU (0-shot), 92.1% on Math-500, and 65% on GPQA Diamond. But what really caught my attention was the inference speed—Nano generates at 143 tokens per second on llama.cpp, and Mini hits 157 t/s on consumer GPUs. They’ve even demonstrated it running on an iPhone via MLX Swift.

I asked Lucas why it matters where models come from, and his answer was nuanced: for individual developers, it doesn’t really matter—use the best model for your task. But for Fortune 500 companies, compliance and legal teams are getting increasingly particular about where models were trained and hosted. This is slowing down enterprise AI adoption, and Trinity aims to solve that.

Lucas shared a fascinating insight about why they decided to do full pretraining instead of just post-training on other people’s checkpoints: “We at Arcee were relying on other companies releasing capable open weight models... I didn’t like the idea of the foundation of our business being reliant on another company releasing models.” He also dropped some alpha about Trinity-Large: they’re going with 13B active parameters instead of 32B because going sparser actually gave them much faster throughput on Blackwell GPUs.

The conversation about MOEs being cheaper for RL was particularly interesting. Lucas explained that because MOEs are so inference-efficient, you can do way more rollouts during reinforcement learning, which means more RL benefit per compute dollar. This is likely why we’re seeing labs like MiniMax go from their original 456B/45B-active model to a leaner 220B/10B-active model—they can get more gains in post-training by being able to do more steps.

Check out [Trinity-Mini](https://huggingface.co/arcee-ai/Trinity-Mini) and [Trinity-Nano-Preview](https://huggingface.co/arcee-ai/Trinity-Nano-Preview) on Hugging Face, or read [The Trinity Manifesto](https://www.arcee.ai/blog/the-trinity-manifesto).

**OpenAI Code Red: Panic at the Disco (and Garlic?)**

It was ChatGPT’s 3rd birthday this week (Nov 30th), but the party vibes seem… stressful. Reports came out that Sam Altman has declared a “Code Red” at OpenAI.

Why? **Gemini 3.**The user numbers don’t lie. ChatGPT apparently saw a 6% drop in daily active users following the Gemini 3 launch. Google’s integration is just too good, and their free tier is compelling.

In response, OpenAI has supposedly paused “side projects” (ads, shopping bots) to focus purely on model intelligence and speed. Rumors point to a secret model codenamed **“Garlic”**—a leaner, more efficient model that beats Gemini 3 and Claude Opus 4.5 on coding reasoning, targeting a release in early 2026 (or maybe sooner if they want to save Christmas).

Wolfram and Yam nailed the sentiment here: Integration wins. Wolfram’s family uses Gemini because it’s *right there* on the Pixel, controlling the lights and calendar. OpenAI needs to catch up not just on IQ, but on being helpful in the moment.

Post the live show, OpenAI also finally added GPT 5.1 Codex Max we covered 2 weeks ago to their API and it’s now available in Cursor, for free, until Dec 11! 

Amazon Nova 2: Enterprise Push with Serious Agentic Chops

Amazon came back swinging with Nova 2, and the jump on Artificial Analysis is genuinely impressive—from around 30% to 61% on their index. That’s a massive improvement.

The family includes Nova 2 Lite (7x cheaper, 5x faster than Nova Premier), Nova 2 Pro (93% on τ²-Bench Telecom, 70% on SWE-Bench Verified), Nova 2 Sonic (speech-to-speech with 1.39s time-to-first-audio), and Nova 2 Omni (unified text/image/video/speech with 1M token context window—you can upload 90 minutes of video!).

Gemini 3 Deep Think Mode

Google launched Gemini 3 Deep Think mode exclusively for AI Ultra subscribers, and it’s hitting some wild benchmarks: 45.1% on ARC-AGI-2 (a 2x SOTA leap using code execution), 41% on Humanity’s Last Exam, and 93.8% on GPQA Diamond. This builds on their Gemini 2.5 variants that earned gold medals at IMO and ICPC World Finals. The parallel reasoning approach explores multiple hypotheses simultaneously, but it’s compute-heavy—limited to 10 prompts per day at $77 per ARC-AGI-2 task.

**This Week’s Buzz: Mid-Training Evals are Here!**

A huge update from us at Weights & Biases this week: We launched **LLM Evaluation Jobs**. ([Docs](https://docs.wandb.ai/models/launch?https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=dec4))

If you are training models or finetuning, you usually wait until the end to run your expensive benchmarks. Now, directly inside W&B, you can trigger evaluations on mid-training checkpoints.

It integrates with Inspect Evals (over 100+ public benchmarks). You just point it to your checkpoint or an API endpoint (even OpenRouter!), select the evals (MMLU-Pro, GPQA, etc.), and we spin up the managed GPUs to run it. You get a real-time leaderboard of your runs vs. the field.

Also, a shoutout to users of [**Neptune.ai**](Neptune.ai)—congrats on the acquisition by OpenAI, but since the service is shutting down, we have built a [migration script](http://wandb.me/migrateneptune) to help you move your history over to W&B seamlessly. We aren’t going anywhere!

**Video & Vision: Physics, Audio, and Speed**

The multimodal space was absolutely crowded this week.

Runway Gen 4.5 (”Whisper Thunder”)

Runway revealed that the mysterious “Whisper Thunder” model topping the leaderboards is actually Gen 4.5. The key differentiator? Physics and Multi-step adherence. It doesn’t have that “diffusion wobble” anymore. We watched a promo video where the shot changes every 3-4 seconds, and while it’s beautiful, it shows we still haven’t cracked super long consistent takes yet. But for 8-second clips? It’s apparently the new SOTA.

Kling 2.6: Do you hear that?

Kling hit back with **Video 2.6**, and the killer feature is **Native Audio**. I generated a clip of two people arguing, and the lip sync was perfect. Not “dubbed over” perfect, but actively generated with the video. It handles multi-character dialogue, singing, and SFX. It’s huge for creators.

Kling was on a roll this week, releasing not one, but two Video Models (O1 Video is an omni modal one that takes Text, Images and Audio as inputs) and O1 Image and Kling Avatar 2.0 are also great updates! (Find all their releases on [X](https://x.com/i/trending/1996381535348707447))

P-Image: Sub-Second Generation at Half a Cent

Last week we talked about ByteDance’s Z-Image, which was super cool and super cheap. Well, this week Pruna AI came out with P-Image, which is even faster and cheaper: image generation under one second for $0.005, and editing under one second for $0.01.

I built a Chrome extension this week (completely rewritten by Opus 4.5, by the way—more on that in a second) that lets me play with these new image models inside the Infinite Craft game. When I tested P-Image Turbo against Z-Image, I was genuinely impressed by the quality at that speed. If you want quick iterations before moving to something like Nano Banana Pro for final 4K output, these sub-second models are perfect.

The extension is [available on GitHub](https://github.com/altryne/infinite-fun-extension) if you want to try it—you just need to add your Replicate or Fal API keys.

SeeDream 4.5: ByteDance Levels Up

ByteDance also launched SeeDream 4.5 in open beta, with major improvements in detail fidelity, spatial reasoning, and multi-image reference fusion (up to 10 inputs for consistent storyboards). The text rendering is much sharper, and it supports multilingual typography including Japanese. Early tests show it competing well with Nano Banana Pro in prompt adherence and logic.

🎤 Voice & Audio

Microsoft VibeVoice-Realtime-0.5B

In a surprise drop, Microsoft open-sourced VibeVoice-Realtime-0.5B, a compact TTS model optimized for real-time applications. It delivers initial audible output in just 300 milliseconds while generating up to 10 minutes of speech. The community immediately started creating mirrors because, well, Microsoft has a history of releasing things on Hugging Face and then having legal pull them down. Get it while it’s hot!

**Use Cases: Code, Cursors, and “Antigravity”**

We wrapped up with some killer practical tips:

* **Opus 4.5 is a beast:** As I mentioned, using Opus inside Cursor’s “Ask” mode is currently the supreme coding experience. It debugs logic flaws that Gemini misses completely. I also used Opus as a prompt engineer for my infographics, and it absolutely demolished GPT at creating the specific layouts I needed

* **Google’s Secret:** Nisten dropped a bomb at the end of the show—**Opus 4.5 is available for free inside Google’s Antigravity (and Colab)!** If you want to try the model that’s beating GPT-5 without paying, go check Antigravity now before they patch it or run out of compute.

* **Microsoft VibeVoice:** A surprise drop of a 0.5B speech model on HuggingFace that does real-time TTS (300ms latency). It was briefly questionable if it would stay up, but mirrors are already everywhere.

That’s a wrap for this week, folks. Next week is probably going to be our final episode of the year, so we’ll be doing recaps and looking at our predictions from last year. Should be fun to see how wrong we were about everything!

Thank you for tuning in. If you missed the live stream, subscribe to our [Substack](https://thursdai.substack.com), [YouTube](https://thursdai.news/yt), and wherever you get your podcasts. See you next Thursday!

TL;DR and Show Notes

**Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](https://x.com/altryne))

* Co Hosts - [@WolframRvnwlf](https://x.com/WolframRvnwlf), [@yampeleg](https://x.com/yampeleg), [@nisten](https://x.com/nisten), [@ldjconfirmed](https://x.com/ldjconfirmed)

* Guest - Lucas Atkins ([@latkins](https://x.com/latkins)) - CTO Arcee AI

**Open Source LLMs**

* DeepSeek V3.2 and V3.2-Speciale - Gold medal olympiad wins, MIT license ([X](https://x.com/deepseek_ai/status/1995452641430651132), [HF V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2), [HF Speciale](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Speciale), [Announcement](https://platform.deepseek.com/blog/deepseek-v3-2))

* Mistral 3 family - Large 3 and Ministral 3, Apache 2.0 ([X](https://x.com/MistralAI/status/1995872766177018340), [Blog](https://mistral.ai/news/mistral-3/), [HF Large](https://huggingface.co/collections/mistralai/mistral-large-3), [HF Ministral](https://huggingface.co/collections/mistralai/ministral-3))

* Arcee Trinity - US-trained MOE family ([X](https://x.com/latkins/status/1995592664637665702), [HF Mini](https://huggingface.co/arcee-ai/Trinity-Mini), [HF Nano](https://huggingface.co/arcee-ai/Trinity-Nano-Preview), [Blog](https://www.arcee.ai/blog/the-trinity-manifesto))

* Hermes 4.3 - Decentralized training, SOTA RefusalBench ([X](https://x.com/nousresearch), [HF](https://huggingface.co/NousResearch/Hermes-4.3-36B))

**Big CO LLMs + APIs**

* OpenAI Code Red - ChatGPT 3rd birthday, Garlic model in development ([The Information](https://www.theinformation.com/articles/openai-developing-garlic-model-counter-googles-recent-gains))

* Amazon Nova 2 - Lite, Pro, Sonic, and Omni models ([X](https://x.com/amazonnews/status/1995898375649050753), [Blog](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-2-lite-a-fast-cost-effective-reasoning-model/))

* Gemini 3 Deep Think - 45.1% ARC-AGI-2 ([X](https://x.com/GeminiApp/status/1996656314983109003), [Blog](https://blog.google/products/gemini/gemini-3-deep-think/))

* Cursor + GPT-5.1-Codex-Max - Free until Dec 11 ([X](https://x.com/cursor_ai/status/1996645841063604711), [Blog](https://cursor.com/blog/codex-model-harness))

**This Week’s Buzz**

* WandB LLM Evaluation Jobs - Evaluate any OpenAI-compatible API ([X](https://x.com/wandb/status/1995921086257791070), [Announcement](https://wandb.ai/site/articles/llm-evaluation-jobs))

**Vision & Video**

* Runway Gen-4.5 - #1 on text-to-video leaderboard, 1,247 Elo ([X](https://x.com/runwayml/status/1995493445243461846))

* Kling VIDEO 2.6 - First native audio generation ([X](https://x.com/Kling_ai/status/1996238606814593196))

* Kling O1 Image - Image generation ([X](https://x.com/Kling_ai/status/1995741899517542818))

**Voice & Audio**

* Microsoft VibeVoice-Realtime-0.5B - 300ms latency TTS ([X](https://x.com/Presidentlin/status/1996461134388625628), [HF](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B))

**AI Art & Diffusion**

* Pruna P-Image - Sub-second generation at $0.005 ([X](https://x.com/PrunaAI/status/1995524846948700495), [Blog](https://pruna.ai/p-image), [Demo](https://demo.pruna.ai))

* SeeDream 4.5 - Multi-reference fusion, text rendering ([X](https://x.com/BytePlusGlobal/status/1996212339096576463)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-dec-4-2025-deepseek-v32/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-dec-4-2025-deepseek-v32?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE4MDc1NDc5OSwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.1mwzUS_VPH8UOxqIWCLcCFPOZidTE7VwmJ_4JuvFL-c&utm_campaign=CTA_5).

---

## ThursdAI Special: Google's New Anti-Gravity IDE, Gemini 3 & Nano Banana Pro Explained (ft. Kevin Hou, Ammaar Reshi & Kat Kampf)

**Date:** December 02, 2025  
**Duration:** 46:04  
**Link:** [https://sub.thursdai.news/p/thursdai-special-googles-new-anti](https://sub.thursdai.news/p/thursdai-special-googles-new-anti)

Hey, Alex here, 

I recorded these conversations just in front of the AI Engineer auditorium, back to back, after these great folks gave their talks, and at the epitome of the most epic AI week we’ve seen since I started recording ThursdAI.

This is less our traditional live recording, and more a real podcast-y conversation with great folks, inspired by [Latent.Space](https://substack.com/profile/89230629-latentspace). I hope you enjoy this format as much as I’ve enjoyed recording and editing it.  

AntiGravity with Kevin

Kevin Hou and team just launched Antigravity, Google’s brand new Agentic IDE based on VSCode, and Kevin (second timer on ThursdAI) was awesome enough to hop on and talk about some of the product decisions they made, what makes Antigravity special and highlighted Artifacts as a completely new primitive. 

Gemini 3 in AI Studio

If you aren’t using Google’s AI Studio ([ai.dev](http://ai.dev)) then you’re missing out! We talk about AI Studio all the time on the show, and I’m a daily user! I generate most of my images with Nano Banana Pro in there, most of my Gemini conversations are happening there as well! 

Ammaar and Kat were so fun to talk to, as they covered the newly shipped “build mode” which allows you to vibe code full apps and experiences inside AI Studio, and we also covered Gemini 3’s features, multimodality understanding, UI capabilities. 

These folks gave a LOT of Gemini 3 demo’s so they know everything there is to know about this model’s capabilities! 

Tried new things with this one, multi camera angels, conversation with great folks, if you found this content valuable, please subscribe :) 

**Topics Covered:**

* Inside Google’s new “AntiGravity” IDE

* How the “Agent Manager” changes coding workflows

* Gemini 3’s new multimodal capabilities

* The power of “Artifacts” and dynamic memory

* Deep dive into AI Studio updates & Vibe Coding

* Generating 4K assets with Nano Banana Pro

Timestamps for your viewing convenience. 

00:00 - Introduction and Overview

01:13 - Conversation with Kevin Hou: Anti-Gravity IDE

01:58 - Gemini 3 and Nano Banana Pro Launch Insights

03:06 - Innovations in Anti-Gravity IDE

06:56 - Artifacts and Dynamic Memory

09:48 - Agent Manager and Multimodal Capabilities

11:32 - Chrome Integration and Future Prospects

20:11 - Conversation with Ammar and Kat: AI Studio Team

21:21 - Introduction to AI Studio

21:51 - What is AI Studio?

22:52 - Ease of Use and User Feedback

24:06 - Live Demos and Launch Week

26:00 - Design Innovations in AI Studio

30:54 - Generative UIs and Vibe Coding

33:53 - Nano Banana Pro and Image Generation

39:45 - Voice Interaction and Future Roadmap

44:41 - Conclusion and Final Thoughts

Looking forward to seeing you on Thursday 🫡 

P.S - I’ve recorded one more conversation during AI Engineer, and will be posting that soon, same format, very interesting person, look out for that soon!   

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-special-googles-new-anti/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-special-googles-new-anti?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE4MDQ2NTY3MSwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.h3ViA8Pw-4_8oniEdqLjP9b_W9t8ymono4EoyxRrYj4&utm_campaign=CTA_5).

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

## ThursdAI - Oct 30 - From ASI in a Decade to Home Humanoids: MiniMax M2's Speed Demon, OpenAI's Bold Roadmap, and 2026 Robot Revolution

**Date:** October 30, 2025  
**Duration:** 1:37:29  
**Link:** [https://sub.thursdai.news/p/thursdai-oct-30-2025-minimax-m2-shocks](https://sub.thursdai.news/p/thursdai-oct-30-2025-minimax-m2-shocks)

Hey, it’s Alex! Happy Halloween friends! 

I’m excited to bring you this weeks (spooky) AI updates! We started the show today with MiniMax M2, the currently top Open Source LLM, with an interview with their head of eng, Skyler Miao, continued to dive into OpenAIs completed restructuring into a non-profit and a PBC, including a deep dive into a live stream Sam Altman had, with a ton of spicy details, and finally chatted with Arjun Desai from Cartesia, following a release of Sonic 3, a sub 49ms voice model! 

So, 2 interviews + tons of news, let’s dive in! (as always, show notes in the end)

Hey, if you like this content, it would mean a lot if you subscribe as a paid subscriber.

Open Source AI

MiniMax M2: open-source agentic model at 8% of Claude’s price, 2× speed ([X](https://x.com/MiniMax__AI/status/1982674798649160175), [Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M2) )

We kicked off our open-source segment with a banger of an announcement and a special guest. The new king of open-source LLMs is here, and it’s called **MiniMax M2**. We were lucky enough to have Skyler Miao, Head of Engineering at Minimax, join us live to break it all down.

M2 is an agentic model built for code and complex workflows, and its performance is just staggering. It’s already ranked in the top 5 globally on the Artificial Analysis benchmark, right behind giants like OpenAI and Anthropic. But here’s the crazy part: it delivers nearly **twice the speed** of Claude 3.5 Sonnet at just **8% of the price**. This is basically Sonnet-level performance, at home, in open source.

Skylar explained that their team saw an “impossible triangle” in the market between performance, cost, and speed—you could only ever get two. Their goal with M2 was to build a model that could solve this, and they absolutely nailed it. It’s a 200B parameter Mixture-of-Experts (MoE) model, but with only 10B active parameters per inference, making it incredibly efficient.

One key insight Skylar shared was about getting the best performance. M2 supports multiple APIs, but to really unlock its reasoning power, you need to use an API that passes the model’s “thinking” tokens back to it on the next turn, like the Anthropic API. Many open-source tools don’t support this yet, so it’s something to watch out for.

Huge congrats to the MiniMax team on this Open Weights (MIT licensed) release, you can find the model on [HF](https://huggingface.co/MiniMaxAI/MiniMax-M2)! 

MiniMax had quite a week, with 3 additional releases, MiniMax speech 2.6, an update to their video model [Hailuo 2.3](https://x.com/Hailuo_AI/status/1983382728343994414) and just after the show, they released a music 2.0 [model](https://x.com/Hailuo_AI/status/1983964920493568296) as well! Congrats on the shipping folks! 

OpenAI drops gpt-oss-safeguard - first open-weight safety reasoning models for classification ( [X](https://x.com/OpenAI/status/1983507392374641071), [HF](https://huggingface.co/collections/openai/gpt-oss-safeguard) )

OpenAI is back on the open weights bandwagon, with a finetune release of their previously open weighted gpt-oss models, with gpt-oss-safeguard. 

These models were trained exclusively to help companies build safeguarding policies to make sure their apps remains safe! With gpt-oss-safeguards 20B and 120B, OpenAI is achieving near parity with their internal safety models, and as Nisten said on the show, if anyone knows about censorship and safety, it’s OpenAI! 

The highlight of this release is, unlike traditional pre-trained classifiers, these models allow for updates to policy via natural language!

These models will be great for businesses that want to safeguard their products in production, and I will advocate to bring these models to W&B Inference soon! 

A Humanoid Robot in Your Home by 2026? 1X NEO announcement ( [X](https://x.com/1x_tech/status/1983233494575952138), [Order page](https://www.1x.tech/order), [Keynote](https://youtu.be/LTYMWadOW7c) )

Things got really spooky when we started talking about robotics. The company 1X, which has been on our radar for a while, officially launched pre-orders for **NEO**, the world’s first consumer humanoid robot designed for your home. And yes, you can order one right now for $20,000, with deliveries expected in early 2026.

The internet went crazy over this announcement, with folks posting receipts of getting one, other folks stoking the uncanny valley fears that Sci-fi has built into many people over the years, of the Robot uprising and talking about the privacy concerns of having a human tele-operate this Robot in your house to do chores. 

It can handle chores like cleaning and laundry, and for more complex tasks that it hasn’t learned yet, it uses a teleoperation system where a human “1X Expert” can pilot the robot remotely to perform the task. This is how it collects the data to learn to do these tasks autonomously in your specific home environment.

The whole release is very interesting, from the “soft and quiet” approach 1X is taking, making their robot a 66lbs short king, draped in a knit sweater, to the $20K price point (effectively at loss given how much just the hands cost), the teleoperated by humans addition, to make sure the Robot learns about your unique house layout. 

The conversation on the show was fascinating. We talked about all the potential use cases, from having it water your plants and look after your pets while you’re on vacation to providing remote assistance for elderly relatives. Of course, there are real privacy concerns with having a telepresence device in your home, but 1X says these sessions are scheduled by you and have strict no-go zones.

Here’s my prediction: by next Halloween, we’ll see videos of these NEO robots dressed up in costumes, helping out at parties. The future is officially here. Will you be getting one? If not this one, when will you think you’ll get one? 

OpenAI’s Grand Plan: From Recapitalization to ASI

This was by far the biggest update about the world of AI for me this week! Sam Altman was joined by Jakub Pachocki, chief scientist and Wojciech Zaremba, a co-founder, on a live stream to share an update about their corporate structure, plans for the future, and ASI goals (Artificial Superintelligence) 

First, the company now has a new structure: a non-profit **OpenAI Foundation** governs the for-profit **OpenAI Group**. The foundation starts with about 26% equity and has a mission to use AI for public good, including an initial $25 billion commitment to curing diseases and building an “AI Resilience” ecosystem.

But the real bombshells were about their research timeline. Chief Scientist Jakub Pachocki stated that they believe deep learning systems are **less than a decade away from superintelligence (ASI)**. He said that at this point, AGI isn’t even the right goal anymore. To get there, they’re planning to have an “AI research intern” by September 2026 and a fully **autonomous AI researcher** comparable to their human experts by March 2028. This is insane if you think about it. As Yam mentioned, OpenAI is already shipping at an insane speed, releasing Models and Products, Sora, Atlas, Pulse, ChatGPT app store, and this is with humans, assisted by AI. 

And here, they are talking about complete and fully autonomous researchers, that will be infinitely more scalable than humans, in the next 2 years. The outcomes of this are hard to imagine and are honestly mindblowing. 

To power all this innovation, Sam revealed they have over **$1.4 trillion in obligations for compute** (over 30 GW). And said even that’s not enough. Their aspiration is to build a “compute factory” capable of standing up one gigawatt of new compute *per week*, and he hinted they may need to “rethink their robotics strategy” to build the data centers fast enough. Does this mean OpenAI humanoid robots building factories? 🤔 

Plus, don’t forget, Sam is one of the investors in Helion energy, working on power solutions like Fusion, and the above graphic has an Energy block that Sam said they will give an update on later (that’s also what he told me during Dev Day when I asked him about it). 

Super exciting and honestly mind-blowing stuff, Gigawats per week, fully autonomous researchers, the world is going to look way different in a few years! 

The Agent Labs Race: Cursor 2.0 vs. Cognition’s SWE-1.5 ([X](https://x.com/cursor_ai), [Blog](https://cursor.com/blog/2-0))

This week also saw a major showdown in the agentic coding space. On the very same day, both Cursor and Cognition launched major updates and their own new models, signaling a new era where agent labs are training their own specialized AI.

First up, **Cursor 2.0** was released with a completely redesigned multi-agent interface and their new model, **Composer**. Composer is claimed to be four times faster than comparable models, and the new UI is built around managing a fleet of agents that can work in parallel on your codebase. It’s a clear shift from being just an IDE to a full-fledged agent platform. Look, the UI even looks like ChatGPT and no code in sight (until you switch to IDE mode) 

Their Composer model is also very interesting, and got a lot of folks excited, but the evaluations they shared, and the fact that they didn’t disclose if that’s a finetune of a chinese model ([it likely is](https://x.com/auchenberg/status/1983901551048470974)). Regardless, folks are saying that it’s a very good model that’s also VERY fast! 

Cognition own coding model - SWE 1.5 ( [Blog](https://cognition.ai/blog/swe-1-5), [X](https://x.com/cognition/status/1983662836896448756), [Windsurf](https://windsurf.com/download) )

Then, just hours later, Cognition punched right back with **SWE-1.5**, their new frontier agent model that now powers Windsurf. The headline here is pure speed. Powered by Cerebras, SWE-1.5 hits a blistering **950 tokens per second**—13 times faster than Sonnet 4.5—while achieving near-SOTA performance on SWE-Bench Pro. They’ve achieved this through a co-designed stack where the agent harness, inference system, and model were all built together and optimized with end-to-end reinforcement learning in real coding environments.

This competition is fantastic news for all of us. We’re seeing specialized, highly-performant models being developed outside of the big labs, putting more power back in the hands of developers.

**This Week’s Buzz**

Just a few quick updates from the world of Weights & Biases and our parent company, CoreWeave.

First, big news! CoreWeave announced the acquisition of **Marimo**, the company behind the popular open-source, reactive notebook for Python. This is another exciting step in building out the essential cloud for AI, adding powerful development tools to the stack alongside best-in-class GPU infrastructure and MLOps with Weights & Biases. Welcome to the Marimo team!

Also, [**Fully Connected**](http://fullyconnected.com) is coming to London next week! It’s our premier conference, and we’ll have speakers from Mistral, Google, LlamaIndex, and more. If you’re in Europe, please come join us. DM me if you need tickets!

And if you’re in New York from November 19-22, come say hi at the **AI Engineer Code Summit**. We’re sponsoring and will have a big booth. It’s always a great place to meet folks from this community.

**Video & Voice: The Multimodal Explosion**

The world of video and voice AI was on fire this week.

The absolute highlight was **Odyssey ML V2**, a new real-time interactive AI video platform. This thing is not like other video models that take minutes to generate a clip. With Odyssey, you type a prompt, and a video starts streaming *instantly*. Then, you can edit it live. We did a demo on the show where we prompted “army of robots in a starship corridor” and then typed “turn these robots into fluffy covered cat robots,” and the video changed in real time. It’s mind-blowing. This is a glimpse into the future of user-driven, playable media.

On the more traditional video front, **Sora** is now invite-free in the US and Japan, and they launched **Character Cameos**. You can now upload photos of your pets or objects (like your kid’s carved pumpkin!) and turn them into characters that you and others can use in videos. I, of course, immediately made a cameo of my cat, Sonia.

Voice and Audio - Cartesia launches Sonic 3, sub 50ms AI speech model

In the world of voice, we had Arjun Desai from **Cartesia** join us to talk about **Sonic-3**, their new real-time TTS engine. Backed by a new **$100M funding round**, Sonic-3 is built on State Space Models (not Transformers) and can achieve insane speeds—we’re talking under 50ms latency. But it’s not just fast; it’s also incredibly expressive. It can laugh, emote, and speak 42 languages with natural code-switching. I used their Pro Voice cloning feature to create an AI version of myself, and the results were scarily good. We even had my AI clone host a segment of the show, see it yourself here, powered by Argil and Sonic 3, this is... AI Alex

**Wrapping Up This Spooky Week 🎃**

As I sit here in my Halloween costume reflecting on this week, I can’t help but feel we’re at an inflection point. We have:

* Open source models competing with the best proprietary ones

* Humanoid robots becoming consumer products

* ASI timelines measured in single-digit years

* Real-time interactive AI across all modalities

And yet, nothing about this scares me. If anything, I’m more excited than ever about what we’re building together. Yes, the pace is insane. Yes, keeping up with everything is becoming nearly impossible (and it’s literally my job!). But we’re living through the most transformative period in human history, and we get to be part of it.

To everyone building, experimenting, and pushing boundaries - keep going. To everyone worried about what’s coming - join us in shaping it responsibly. And to everyone who celebrated Halloween today - I hope your costume was as epic as the AI developments we covered! 👻

Until next week, this is Alex signing off. Remember to subscribe, give us five stars, and I’ll see you next ThursdAI!

TL;DR - All Topics Covered

ThursdAI - Oct 30 - Halloween Special 👻

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](https://x.com/altryne))

* Co Hosts - [@WolframRvnwlf](https://x.com/WolframRvnwlf) [@yampeleg](https://x.com/yampeleg) [@nisten](https://x.com/nisten) [@ldjconfirmed](https://x.com/ldjconfirmed) [@ryancarson](http://x.com/ryancarson)

* **Guest: Skyler Miao** - Head of Engineering, MiniMax ([@SkylerMiao7](https://x.com/SkylerMiao7))

* **Guest: Arjun Desai** - CoFounder Cartesia  ([@jundesai](https://x.com/jundesai))

* **Open Source LLMs**

* **MiniMax M2**: Open-source agentic model at 8% of Claude’s price, 2× speed ([X](https://x.com/MiniMax__AI/status/1982674798649160175), [Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M2))

* **OpenAI GPT-OSS-Safeguard**: First open-weight safety reasoning models ([X](https://x.com/OpenAI/status/1983507392374641071), [HF](https://huggingface.co/collections/openai/gpt-oss-safeguard))

* **IBM Granite 4.0 Nano**: Ultra-efficient tiny models for edge deployment ([X](https://x.com/ArtificialAnlys/status/1983611955668775411), [Artificial Analysis](https://artificialanalysis.ai/models/granite))

* **Ming-flash-omni Preview**: Sparse MoE omni-modal model ([X](https://x.com/AntLingAGI/status/1982831211312722041), [HuggingFace](https://huggingface.co/inclusionAI/Ming-flash-omni-Preview))

* **Kimi Linear**: 48B parameter model with 1M context ([HF](https://huggingface.co/moonshotai/Kimi-Linear-48B-A3B-Instruct))

* **Robotics**

* **1X NEO**: First consumer humanoid robot, $20k, delivery 2026 ([X](https://x.com/1x_tech/status/1983233494575952138), [Order page](https://www.1x.tech/order), [Keynote](https://youtu.be/LTYMWadOW7c))

* **Big Companies & APIs**

* **OpenAI Restructuring**: ASI within 10 years, AI researcher by 2028 ([X](https://x.com/AndrewCurran_/status/1983161944208220550))

* **Cursor 2.0 & Composer**: 4x faster coding, new model ([X](https://x.com/cursor_ai), [Blog](https://cursor.com/blog/2-0))

* **Cognition SWE-1.5**: 950 tok/s, 40% SWE-bench Pro ([Blog](https://cognition.ai/blog/swe-1-5), [X](https://x.com/cognition/status/1983662836896448756), [Windsurf](https://windsurf.com/download))

* **Perplexity Email Assistant**: Privacy-first AI inbox management ([X](https://x.com/perplexity_ai/status/1983591113903738970), [Assistant Site](https://www.perplexity.ai/assistant))

* **This Week’s Buzz**

* Fully Connected London - [fullyconnected.com](https://fullyconnected.com)

* AI Engineer Code Summit NYC - Nov 19-22

* CoreWeave acquires Marmo notebooks ([X](https://x.com/marimo_io/status/1983916371869364622))

* **Vision & Video**

* **Odyssey ML V2**: Real-time interactive AI video ([X](https://x.com/odysseyml/status/1982856110290939989), [Experience](https://experience.odyssey.ml))

* **Sora**: Now invite-free + Character Cameos feature ([X](https://x.com/OpenAI/status/1983661036533379486), [Sonia Cameo](https://sora.chatgpt.com/p/s_6902d8b223d88191a04adfada2e9f5b5))

* **Hailuo 2.3**: Cinema-grade video generation ([X](https://x.com/Hailuo_AI/status/1983016390878708131))

* **Voice & Audio**

* **MiniMax Speech 2.6**: <250ms ultra-human voice AI ([X](https://x.com/Hailuo_AI/status/1983557055819768108), [MiniMax](https://minimaxi.com/audio), [API Docs](https://platform.minimax.io/docs/guides/sp))

* **Cartesia Sonic 3**: Real-time TTS with emotion & laughter, $100M funding ([X](https://x.com/krandiash/status/1983202316397453676), [Website](https://cartesia.ai/sonic), [Docs](https://docs.cartesia.ai/2024-11-13/get-started/overview))

* **Tools**

* **Pokee**: Agentic workflow builder ([X](https://x.com/Pokee_AI/status/1983202159262150717))

* **Pomelli**: Google’s AI marketing agent ([X](https://twitter.com/testingcatalog/status/1983214036259938553), [Labs](https://labs.google.com/pomelli/about/?ref=testingcatalog.com)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-oct-30-2025-minimax-m2-shocks/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-oct-30-2025-minimax-m2-shocks?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3NzYwNzA3MCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.Z91yXvekATldr53MP5TfO79U0CFgSujGPDLFbYtV7Xo&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Oct 23: The AI Browser Wars Begin, DeepSeek's OCR Mind-Trick & The Race to Real-Time Video

**Date:** October 24, 2025  
**Duration:** 1:35:16  
**Link:** [https://sub.thursdai.news/p/thursdai-oct-23-the-ai-browser-wars](https://sub.thursdai.news/p/thursdai-oct-23-the-ai-browser-wars)

Hey everyone, Alex here! 

Welcome... to the browser war II - the AI edition! This week we chatted in depth about ChatGPT’s new Atlas agentic browser, and the additional agentic powers Microsoft added to Edge with Copilot Mode (tho it didn’t work for me) 

Also this week was a kind of crazy OCR week, with more than 4 OCR models releasing, and the crown one is DeepSeek OCR, that turned the whole industry on it’s head (more later) 

Quite a few video updates as well, with real time lipsync from Decart, and a new update from LTX with 4k native video generation, it’s been a busy AI week for sure! 

Additionally, I’ve had the pleasure to talk about AI Browsing agents with Paul from BrowserBase and real time video with Kwindla Kramer from Pipecat/Daily, so make sure to tune in for those interviews, buckle up, let’s dive in! 

Thanks for reading ThursdAI - Recaps of the most high signal AI weekly spaces! This post is public so feel free to share it.

**Open Source: OCR is Not What You Think It Is **([X](https://x.com/Presidentlin/status/1980159652563415094), [HF](https://huggingface.co/deepseek-ai/DeepSeek-OCR), [Paper](https://github.com/deepseek-ai/DeepSeek-OCR/blob/main/DeepSeek_OCR_paper.pdf))

The most important and frankly mind-bending release this week came from DeepSeek. They dropped DeepSeek-OCR, and let me tell you, this is NOT just another OCR model. The cohost were buzzing about this, and once I dug in, I understood why. This isn’t just about reading text from an image; it’s a revolutionary approach to **context compression**.

We think that DeepSeek needed this as an internal tool, so we’re really grateful to them for open sourcing this, as they did something crazy here. They are essentially turning text into a visual representation, compressing it, and then using a tiny vision decoder to read it back with incredible accuracy. We’re talking about a compression ratio of up to **10x with 97% decoding accuracy**. Even at 20x compression they are achieving 60% decoding accuracy! My head exploded live on the show when I read that. This is like the middle-out compression algorithm joke from *Silicon Valley*, but it’s real. As Yam pointed out, this suggests our current methods of text tokenization are far from optimal.

With only 3B and ~570M active parameters, they are taking a direct stab at long context inefficiency, imagine taking 1M tokens, encoding them into 100K visual tokens, and then feeding those into a model. Since the model is tiny, it’s very cheap to run, for example, [**alphaXiv**](https://x.com/askalphaxiv)** **claimed they have OCRd’ all of the papers on ArXiv with this model for $1000, a task that would have cost $7500 using MistalOCR - as per their paper, with DeepSeek OCR, on a single H100 GPU, its possible to scan up to 200K pages! 🤯 Really innovative stuff! 

OCR and VLM models had quite a week, with multiple models besides DeepSeek OCR releasing, models like Liquids LFM2-VL-3B ([X](https://x.com/LiquidAI_/status/1980985540196393211), [HF](https://huggingface.co/liquidai/lfm2-vl-3b)), and the newly updated 2B and 32B of Qwen3-VL ([X](https://x.com/Alibaba_Qwen/status/1980665932625383868), [Hugging Face](https://huggingface.co/collections/Qwen3-VL)), and AI2’s olmo-ocr 2-7B ([X](https://x.com/allen_ai/status/1981029159267659821), [HF](https://huggingface.co/allenai/olmOCR-2-7B-1025-FP8)). 

The Qwen models are particularly interesting, as the 2B model is a generic VLM (can also do OCR) and is close to previous weeks 4B and 8B brothers, and the newly updated 32B model outperforms GPT-5 mini and Claud 4 sonnet even! 

The Browser Wars are BACK: OpenAI & Microsoft Go Agentic

Look, I may be aging myself here, but I remember, as a young frontend dev, having to install 5 browers at once to test them out, Chrome, Internet Explorer, Firefox, Opera etc’. That was then, and now, I have Dia, Comet, and the newly released Atlas, and, yeah, today I even installed Microsoft Edge to test their AI features! It seems like the AI boom brought with it a newly possible reason for folks to try and take a bite out of Chrome (who’s agentic features are long rumored with project mariner but are nowhere to be found/shipped yet) 

OpenAI’s ChatGPT Atlas: The Browser Reimagined ([X](https://x.com/OpenAI/status/1980685602384441368), [Download](https://chatgpt.com/atlas/get-started/))

OpenAI is proving that besides just models, they are a product powerhouse, stepping into categories like Shopping (with a shopify integration), app stores (with ChatGPT apps), social (with Sora2) and now... browsers! This week, they have launched their tightly integrated into ChatGPT browser called Atlas, and it’s a big release! 

I’ll split my review here to 2 parts, the browser features part and the agentic part. 

New fresh take on a chromium based browser

The tight integration into ChatGPT is everywhere in this browser, from the new tab that looks like the basic ChatGPT interaface, one line of text, to the sidebar on the left that... is the ChatGPT web sidebar with all your chats, projects, custom GPTs etc. 

The integration doesn’t stop there, as you have to sign in to your ChatGPT account to even use this browser (available only to MacOS users, and Pro, Plus and Nano tiers). The browser has a few neat tricks, like a special tool that allows you to search your browsing history with natural language, a-la “what were those shoes I was looking at a few days ago” will find your the tabs you browsed for shoes. 

A special and cool feature is called, confusingly “Cursor”, wherein you can select a text, and then click the little OpenAI logo that pops up, allowing you to ask ChatGPT for changes to that selected text (like fix typos, spruce up your writing etc). It’s surprisingly convenient to rewrite tweets or for any type of document editing. 

ChatGPT Atlas also stores memories about your browsing patterns, which will be additional to the ChatGPT memories it stores about you from chats, helping even more by knowing your browsing patterns, which software you prefer to use, which websites you prefer to order food from etc. This IMO is one of the hugest unlocks for folks inside the ChatGPT ecosystem, as much of a stanard persons peferences can be gleaned from their browser usage and patterns.

Lastly, the “Ask ChatGPT” sidepane on the right (which can be opened with cmd+.) is really great for chatting with a webpage, or going down search rabbit holes. It receives the context of the webpage you’re looking at by default (only 1 page so far, competitors allow you to add additional tabs with @, (which is supposedly coming to ChatGPT soon) and ask... ChatGPT anything about this. 

Agentic SOTA? not so fast

The most important “change” to how browsers work in Atlas imo is the agentic mode. This isn’t new, we remember when ChatGPT launched thier Operator Agent back in January of this year (our [coverage](https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1)) and then renamed it Agent Mode and integrated into ChatGPT itself back in [July](https://sub.thursdai.news/p/thursdai-july-17th-kimi-k2-openai). 

So, web browsing agents are not entirely new, what’s novel here though, is the integration into your browser, and the ability for the Atlas browser to use your logged in sessions and cookies, to pretend to be you! This... can be quite scary for some, as prompt injection attacks are getting more popular (where-in malicious assholes add hidden instructions to their website that will get the agent to do something you don’t like) but it’s also very exciting, as the agent can do much much more, without getting blocked by providers who could previously just block Agent Mode as it ran on OpenAI servers! 

Until today, there were 2 main Agentic browsers in the mix, Perplexity’s Comet (where you can choose which model runs the agent) and Atlas. Comet seems to be doing a little bit better on some stuff on my tests, but not by much. I have the same agentic task (go to [X.com](http://X.com), find my bookmarks, open all links, summarize per my specific format) that I’ve been running for a while now, and Comet outdid Atlas this week on that task.

Who needs agentic browsing? 

For some reason, most of the demos for agentic browsing are showing the same, boring-ish examples. Book some flights, collect a grocery shopping cart. I’ve tried new and different things this week, for example, letting Atlas choose and order food for me (as ChatGPT knows my pescatarian preferences, it’s better than Comet for personal stuff), and one of the longest task I’ve had an agent do yet, I asked it to complete a Compliance training I had to take at work! 

Mind you, this is a very complex task, even for regular people, as these compliance websites are built to not be messed with. They have video players that stop if you switch focus to some other tab, they have interactive quizes and games, drag and drop interfaces, audio buttons, to make sure you really are taking the test. I can happily report, that after 5 hours, and a few stops along the way (where I had to convince the agent to keep going), it completed this very hard task! (and now I have to take this course myself again to actualy be compliant 😅 it will probably take me 2 hours to do manually) 

This experiment made me think, who needs the agentic browsing features and for what? Well, for tasks that require a lot of manual steps to do the same thing over and over again, agentic browser is going to make a lot of peoples browsing a lot easier. Things like kids schedules reviewing in multiple websites, collecitng data and formatting it differently etc. 

Scary security implications 

Atlas could only finish my compliance task while being logged in as me, and ChatGPT Atlas gives a all or nothing control. You can run your agent with full access to your logged in websites (think Gmail etc) or you can essentially give it an incognito mode. 

This, again, due to the risk of promp injections in malicious websites being more and more prevalent. In a rare post detailing how they are thinking about this, OpenAI Chief Information Security officer offered a deep dive into their attempts to mitigate this issue (Simon Willison had a great breakdown of that information [here](https://simonwillison.net/2025/Oct/22/openai-ciso-on-atlas/)) but that’s likely not enough, so definitely be aware when you’re running agent mode (which needs to be explicitly turned on right now by selecting Agent) 

This Weeks Buzz - Weights & Biases // Coreweave

Weights & Biases (now proudly part of CoreWeave) had some exciting updates. Our Fully Connected conference series is hitting Tokyo on October 30-31 and London on November 4-5—perfect for ML practitioners and AI engineers. If you’re in the area, join us for talks, networking, and deep dives into the latest. Register at [**Fullyconnected.com**](Fullyconnected.com)—DM me if you need a hook-up!

We also collaborated with Meta and Stanford on Torch Forge, a new PyTorch-native library for scalable RL post-training and agent development. It’s built for massive GPU runs (we provided 520 H100s!), competing with Ray via tools like Monarch scheduler. If you’re training on clusters, check the [blog](https://pytorch.org/blog/introducing-torchforge/) —it’s a big deal for efficient multi-GPU workflows.

Microsoft goes after OpenAI with Edge copilot mode ([X](https://x.com/mustafasuleyman/status/1981390345578697199))

In a pretty surprising move, Microsoft announced today their take on the agentic browser war, with a bunch of enhancements to Copilot (their overall word for their AI assistance across Microsoft 360, Browser, Bing search etc), Think.. clippy, for the AI age (they even brought clippy back as an [easter egg](https://x.com/satyanadella/status/1981466897557196837)) 

The short version is, Edge is getting more powerful with custom agentic features (which I enabled and couldn’t get to work no matter how much I tried, so I can’t tell you how they compare to Atlas/Comet), and they have a voice mode that allows you to talk to your browser, with Edge having a sense of what’s on the actual page! Of course, this being Microsoft, marketing aside and features aside, when I asked Copilot if it has access to other tabs (like the marketing video claims) it said it doesn’t have access, agentic mode didn’t work, and I’m very unlikely to be testing it further! But hey, if you use Copilot app on your mobile phone, and click the new Mico avatar like 25 times it will turn into Clippy, so.. yay? 

**Claude Code on the Web, Claude on Desktop upgraded **([X](https://x.com/btibor91/status/1980340485152715095), [Anthropic](https://www.anthropic.com/news/claude-code-on-the-web))

Anthropic also made waves by bringing Claude Code to the web. Now you can delegate software tasks to Claude through a web interface with GitHub integration. Nisten was particularly excited about being able to manage his coding projects from his phone. It runs tasks in a secure sandbox, can handle multiple repos, and automatically create pull requests. It’s another powerful coding agent becoming more accessible to developers everywhere. 

They have also made changes to the desktop Claude app, allowing it to see the context of your screen with screenshots, and file sharing, and even a new voice mode that allows you to talk to Claude (which is unfortunately mapped to the tab button, without the ability to remap) 

**Browser Automation and Delegated Authentication with Browserbase **([X](https://x.com/pk_iv/status/1980653648310071663), [Director.ai](https://director.ai/?ref=producthunt), [Stagehand](https://stagehand.dev/))

While OpenAI and Microsoft are building chat into the browser, what about bringing the browser into our chat-based agents? We had Paul Klein, the founder of Browserbase, join us to talk about this exact topic. His company is tackling one of the biggest hurdles for AI agents: authentication.

Paul and his team launched Director 2.0, a platform that lets you build web automation with natural language prompts. But the real innovation here is their integration with **1Password**. Instead of giving an agent the “master keys” to all your logged-in sessions like Atlas does, Browserbase allows for delegated, per-site authentication. When an agent running in the cloud needs to log into a site on your behalf, you get a prompt on your local machine to approve it. This is a much safer, more granular way to give agents the access they need. As Paul said, you shouldn’t let an AI the master keys into your house; you should give it permission to enter one room at a time. It’s a brilliant paradigm for secure agentic workflows and I really like this approach of a piece-meal authentication for browser agents. I wish Atlas has something like this for the incognito mode! 

Director 2.0 itself is like V0 for web automation—you give it a prompt, it performs the task, and then it gives you a repeatable script you can deploy. It’s a way to create robust automations without needing to be a developer, and it’s already being used to automate thousands of hours of manual work. 

Video & Audio: The Race to Real-Time

The world of generative media is moving at lightning speed, with a clear trajectory towards real-time, interactive experiences.

**Decart’s Real-Time Lip Sync API **([X](https://x.com/DecartAI/status/1981078296084488293))

We had Kwindla Kramer, one of the worlds leading experts in real-time audio, join us to break down a phenomenal release from Decart AI: a real-time lip-sync API. This isn’t the pre-rendered, slightly-off lip-sync we’re used to. This is a pipeline of models working together to generate perfectly synchronized lip movements for an avatar in real-time.

Kwindla explained the tech stack: it captures your audio via WebRTC, sends it to Whisper for transcription, gets a response from an LLM like Grok, generates a voice with ElevenLabs, and then Decart’s model modifies the avatar’s video frames to match the new audio, all with a sub-two-second latency. This is how we get to truly interactive, believable AI characters. Kwindla even built a quick demo, though it didn’t seem to work the in the morning, probably GPU issues, so we just played the demo videos. 

**LTX-2 and Sora’s Pet Cameos**

The trend towards high-fidelity, real-time generation continued with a breaking news release from Lightricks: LTX-2. This is an open-source (weights coming this fall!) engine that can generate **native 4K video with synchronized audio**. It’s fast, efficient, and is set to be a powerful open alternative to closed models like Sora. And it’s a native 4K, no upscaling! 

Speaking of Sora, they announced that character cameos are getting an upgrade. Soon, you’ll be able to turn anything—your pet, a coffee cup, or even a sunny-side-up egg—into an animated, talking character. I’m really looking forward for this new Sora update and will let you know my impressions when it drops (soon, [according to](https://x.com/billpeeb/status/1981118483607032050) Bill from OpenAI) 

What a week folks! What A WEEK! 😅 My head is still spinning! 

From browsers that can do our work for us to OCR that redefines context, we’re seeing foundational shifts across the board. The tools are getting more powerful, more accessible, and more integrated into our daily workflows. The future is being built right now, and we get to watch it happen week by week.

Thank you for being a ThursdAI subscriber. As always, here are the show notes with all the links and details from this week’s whirlwind of AI news.

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@yampeleg](https://x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed)

* Paul Kelin [@pk_iv](https://x.com/pk_iv) - Browser Base

* Kwindla Kramer [@kwindla](https://x.com/kwindla) - Pipecat & Daily

* **Open Source LLMs**

* DeepSeek-OCR: Efficient Vision-Text Compression for Massive Contexts ([X](https://x.com/Presidentlin/status/1980159652563415094), [HF](https://huggingface.co/deepseek-ai/DeepSeek-OCR), [Paper](https://github.com/deepseek-ai/DeepSeek-OCR/blob/main/DeepSeek_OCR_paper.pdf))

* Liquid AI LFM2-VL-3B: Tiny Multilingual Vision-Language Model ([X](https://x.com/LiquidAI_/status/1980985540196393211), [HF](https://huggingface.co/liquidai/lfm2-vl-3b))

* PokeeResearch-7B: Open-source SOTA Deep Research Agent ([X](https://x.com/Pokee_AI/status/1981040897346179256), [HF](https://huggingface.co/PokeeAI/pokee_research_7b), [Web](https://pokee.ai/deepresearch-preview), [ArXiv](https://arxiv.org/pdf/2510.15862.pdf), [GitHub](https://github.com/Pokee-AI/PokeeResearchOSS))

* Qwen3-VL 2B & 32B: compact STEM-tuned multimodal powerhouses ([X](https://x.com/Alibaba_Qwen/status/1980665932625383868), [Hugging Face](https://huggingface.co/collections/Qwen3-VL))

* **Big CO LLMs + APIs**

* OpenAI announces Atlas - its agentic AI browser ([X](https://x.com/OpenAI/status/1980685602384441368), [Download](https://chatgpt.com/atlas/get-started/))

* [Security Implications, Injection + note from CISO](https://x.com/cryps1s/status/1981037851279278414)

* Claude Code on the Web: Cloud Coding with Secure Sandboxing ([X](https://x.com/btibor91/status/1980340485152715095), [Anthropic](https://www.anthropic.com/news/claude-code-on-the-web))

* Meta bans 1‑800‑ChatGPT on WhatsApp

* Microsoft agentic addition to Copilot Mode in Edge ([X](https://x.com/MicrosoftEdge/status/1981028712830185914))

* Gemini AI Studio launches “Vibe Coding” ([X](https://x.com/OfficialLoganK/status/1980674135693971550), [AI Studio Build](https://ai.studio/build))

* **This weeks Buzz**

* Fully connected comes to Tokyo (Oct 30-31) and London (Nov 4-5) ! ([register at Fullyconnected.com](https://fullyconnected.com))

* **Vision & Video**

* Sora is about to get pet cameos

* Krea open‑sources a 14‑billion‑parameter real‑time video model ([X](https://x.com/krea_ai/status/1980358158376988747), [HF](https://huggingface.co/krea/krea-realtime-video))

* Reve’s unannounced video mode!? 1080p + sound

* LTX-2: open-source 4K audio+video generation engine from Lightricks ([X](https://x.com/ltx_model/status/1981377626347323480), [Website](https://ltx.studio/), [GitHub](https://github.com/Lightricks/LTX-Video))

* **Voice & Audio**

* Decart Lip Sync API: Real-Time Avatar Lip Movement ([X](https://x.com/DecartAI/status/1981078296084488293))

* **Tools**

* Browserbase launches Director 2.0: prompt-powered web automation ([X](https://x.com/pk_iv/status/1980653648310071663), [Director.ai](https://director.ai/?ref=producthunt), [Stagehand](https://stagehand.dev/)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-oct-23-the-ai-browser-wars/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-oct-23-the-ai-browser-wars?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3Njk3NTE5MiwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.tNE8S7hoO4vWQxj7pHyZaahDJoehF-0fMhAd_z-WQuE&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Oct 16 - VEO3.1, Haiku 4.5, ChatGPT adult mode, Claude Skills, NVIDIA DGX spark, Wordlabs RTFM & more AI news

**Date:** October 17, 2025  
**Duration:** 1:34:38  
**Link:** [https://sub.thursdai.news/p/thursdai-oct-16-veo31-haiku-45-chatgpt](https://sub.thursdai.news/p/thursdai-oct-16-veo31-haiku-45-chatgpt)

Hey folks, Alex here. 

Can you believe it’s already the middle of October? This week’s show was a special one, not just because of the mind-blowing news, but because we set a new ThursdAI record with **four** incredible interviews back-to-back!

We had Jessica Gallegos from Google DeepMind walking us through the cinematic new features in VEO 3.1. Then we dove deep into the world of Reinforcement Learning with my new colleague Kyle Corbitt from OpenPipe. We got the scoop on Amp’s wild new ad-supported free tier from CEO Quinn Slack. And just as we were wrapping up, Swyx ( from [Latent.Space](https://substack.com/profile/89230629-latentspace) , now with Cognition!) jumped on to break the news about their blazingly fast SWE-grep models. 

But the biggest story? An AI model from Google and Yale made a novel scientific discovery about cancer cells that was then *validated in a lab*. This is it, folks. This is the “let’s fucking go” moment we’ve been waiting for. So buckle up, because this week was an absolute monster. Let’s dive in!

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Open Source: An AI Model Just Made a Real-World Cancer Discovery

We always start with open source, but this week felt different. This week, open source AI stepped out of the benchmarks and into the biology lab.

Our friends at Qwen kicked things off with new 3B and 8B parameter versions of their Qwen3-VL vision model. It’s always great to see powerful models shrink down to sizes that can run on-device. What’s wild is that these small models are outperforming last generation’s giants, like the 72B Qwen2.5-VL, on a whole suite of benchmarks. The 8B model scores a 33.9 on OS World, which is incredible for an on-device agent that can actually see and click things on your screen. For comparison, that’s getting close to what we saw from Sonnet 3.7 just a few months ago. The pace is just relentless.

But then, Google dropped a [bombshell](https://blog.google/technology/ai/google-gemma-ai-cancer-therapy-discovery/). A 27-billion parameter Gemma-based model they developed with Yale, called C2S-Scale, generated a completely novel hypothesis about how cancer cells behave. This wasn’t a summary of existing research; it was a new idea, something no human scientist had documented before. And here’s the kicker: researchers then took that hypothesis into a wet lab, tested it on living cells, and proved it was true.

This is a monumental deal. For years, AI skeptics like Gary Marcus have said that LLMs are just stochastic parrots, that they can’t create genuinely new knowledge. This feels like the first, powerful counter-argument. Friend of the pod, Dr. Derya Unutmaz, has been on the show before saying AI is going to solve cancer, and this is the first real sign that he might be right. The researchers noted this was an “emergent capability of scale,” proving once again that as these models get bigger and are trained on more complex data—in this case, turning single-cell RNA sequences into “sentences” for the model to learn from—they unlock completely new abilities. This is AI as a true scientific collaborator. Absolutely incredible.

Big Companies & APIs

The big companies weren’t sleeping this week, either. The agentic AI race is heating up, and we’re seeing huge updates across the board.

Claude Haiku 4.5: Fast, Cheap Model Rivals Sonnet 4 Accuracy ([X](https://x.com/claudeai/status/1978505436358697052), [Official blog](https://www.anthropic.com/news/introducing-claude-haiku-4-5), [X](https://x.com/danshipper/status/1978506914498834484))

First up, Anthropic released Claude Haiku 4.5, and it is a beast. It’s a fast, cheap model that’s punching way above its weight. On the SWE-bench verified benchmark for coding, **it hit 73.3%**, putting it right up there with giants like GPT-5 Codex, but at a fraction of the cost and twice the speed of previous Claude models. Nisten has already been putting it through its paces and loves it for agentic workflows because it just follows instructions without getting opinionated. It seems like Anthropic has specifically tuned this one to be a workhorse for agents, and it absolutely delivers. 

The thing to note also is the very impressive jump in OSWorld (**50.7%**), which is a computer use benchmark, and at this price and speed ($1/$5 MTok input/output) is going to make computer agents much more streamlined and speedy! 

ChatGPT will loose restrictions; age-gating enables “adult mode” with new personality features coming ([X](https://x.com/sama/status/1978129344598827128)) 

Sam Altman set X on fire with a [thread](https://x.com/sama/status/1978129344598827128) announcing that ChatGPT will start loosening its restrictions. They’re planning to roll out an “adult mode” in December for age-verified users, potentially allowing for things like erotica. More importantly, they’re bringing back more customizable personalities, trying to recapture some of the magic of GPT-4.0 that so many people missed. It feels like they’re finally ready to treat adults like adults, letting us opt-in to R-rated conversations while keeping strong guardrails for minors. This is a welcome change, and we’ve been advocating for this for a while, and it’s a notable change from the XAI approach I covered [last week](https://open.substack.com/pub/thursdai/p/oct-9-2025-dev-days-agent-era-samsungs?r=2imipa&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true). Opt in for adults with verification while taking precautions vs engagement bait in the form of a flirty animated waifu with engagement mechanics. 

Microsoft is making every windows 11 an AI PC with copilot voice input and agentic powers ([Blog](https://blogs.windows.com/windowsexperience/2025/10/16/making-every-windows-11-pc-an-ai-pc/),[X](https://x.com/zacbowden/status/1978822883217461388))

And in breaking news from this morning, Microsoft announced that every Windows 11 machine is becoming an AI PC. They’re building a new Copilot agent directly into the OS that can take over and complete tasks for you. The really clever part? It runs in a secure, sandboxed desktop environment that you can watch and interact with. This solves a huge problem with agents that take over your mouse and keyboard, locking you out of your own computer. Now, you can give the agent a task and let it run in the background while you keep working. This is going to put agentic AI in front of hundreds of millions of users, and it’s a massive step towards making AI a true collaborator at the OS level.

NVIDIA DGX - the tiny personal supercomputer at $4K  ([X](https://twitter.com/lmsysorg), [LMSYS Blog](https://lmsys.org/blog/2025-10-13-nvidia-dgx-spark/))

NVIDIA finally delivered their promised AI Supercomputer, and while the excitement was in the air with Jensen hand delivering the DGX Spark to OpenAI and Elon (recreating that historical picture when Jensen hand delivered a signed DGX workstation while Elon was still affiliated with OpenAI). The workstation was sold out almost immediately. Folks from LMSys did a great [deep dive](https://lmsys.org/blog/2025-10-13-nvidia-dgx-spark/) into specs, all the while, folks on our feeds are saying that if you want to get the maximum possible open source LLMs inference speed, this machine is probably overpriced, compared to what you can get with an M3 Ultra Macbook with 128GB of RAM or the RTX 5090 GPU which can get you similar if not better speeds at significantly lower price points. 

Anthropic’s “Claude Skills”: Your AI Agent Finally Gets a Playbook ([Blog](https://www.anthropic.com/news/skills))

Just when we thought the week couldn’t get any more packed, Anthropic dropped “Claude Skills,” a huge upgrade that lets you give your agent custom instructions and workflows. Think of them as expertise folders you can create for specific tasks. For example, you can teach Claude your personal coding style, how to format reports for your company, or even give it a script to follow for complex data analysis.

The best part is that Claude automatically detects which “Skill” is needed for a given task, so you don’t have to manually load them. This is a massive step towards making agents more reliable and personalized, moving beyond just a single custom instruction and into a library of repeatable, expert processes. It’s available now for all paid users, and it’s a feature I’ve been waiting for. Our friend [Simon Willison](https://substack.com/profile/5753967-simon-willison) things skills may be [a bigger deal than MCPs](https://simonwillison.net/2025/Oct/16/claude-skills/)! 

🎬 Vision & Video: Veo 3.1, Sora Gets Longer, and Real-Time Worlds

The AI video space is exploding. We started with an amazing interview with Jessica Gallegos, a Senior Product Manager at Google DeepMind, all about the new Veo 3.1. This is a significant 0.1 update, not a whole new model, but the new features are game-changers for creators.

The audio quality is way better, and they’ve massively improved video extensions. The model now conditions on the last second of a clip—including the audio. This means if you extend a video of someone talking, they keep talking in the same voice! This is huge, saving creators from complex lip-syncing and dubbing workflows. They also added object insertion and removal, which works on both generated and real-world video. Jessica shared an incredible story about working with director Darren Aronofsky to insert a virtual baby into a live-action film shot, something that’s ethically and practically very difficult to do on a real set. These are professional-grade tools that are becoming accessible to everyone. Definitely worth listening to the whole interview with Jessica, starting at 00:25:44

I’ve played with the new VEO in Google Flow, and while I was somewhat (still) disappointed with the UI itself (it froze sometimes and didn’t play). I wasn’t able to upload my own videos to use the insert/remove features Jessica mentioned yet, but saw examples online and they looked great! 

Ingredients were also improved with VEO 3.1, where you can add up to 3 references, and they will be included in your video but not as first frame, the model will use them to condition the vidoe generation. Jessica clarified that if you upload sound, as in, your voice, it won’t show up in the model as your voice yet, but maybe they will add this in the future (at least this was my feedback to her). 

SORA 2 extends video gen to 15s for all, 25 seconds to pro users with a new storyboard 

Not to be outdone, OpenAI pushed a bit of an update for Sora. All users can now generate up to 15-second clips (up from 8-10), and Pro users can go up to 25 seconds using a new storyboard feature. I’ve been playing with it, and while the new scene-based workflow is powerful, I’ve noticed the quality can start to degrade significantly in the final seconds of a longer generation (posted my experiments [here](https://x.com/altryne/status/1978569726734545009)) as you can see. The last few shot so the cowboy don’t have any action, and the face is a blurry mess. 

Worldlabs RTFM: Real-Time Frame Model renders 3D worlds at interactive speeds on a single H100 ( [X](https://x.com/theworldlabs/status/1978839171058815380), [Blog](https://www.worldlabs.ai/blog/rtfm), [Demo](https://rtfm.worldlabs.ai/) )

And just when we thought we’d seen it all, World Labs dropped a breaking news release: RTFM, the Real-Time Frame Model. This is a generative world model that renders interactive, 3D-consistent worlds on the fly, all on a single H100 GPU. Instead of pre-generating a 3D environment, it’s a “learned renderer” that streams pixels as you move. We played with the demo live on the show, and it’s mind-blowing. The object permanence is impressive; you can turn 360 degrees and the scene stays perfectly coherent. It feels like walking around inside a simulation being generated just for you.

This Week’s Buzz: RL Made Easy with Serverless RL + interview with Kyle Corbitt

It was a huge week for us at Weights & Biases and CoreWeave. I was thrilled to finally have my new colleague Kyle Corbitt, founder of OpenPipe, back on the show to talk all things Reinforcement Learning (RL).

RL is the technique behind the massive performance gains we’re seeing in models for tasks like coding and math. At a high level, it lets a model try things, and then you “reward” it for good outcomes and penalize it for bad ones, allowing it to learn strategies that are better than what was in its original training data. The problem is, it’s incredibly complex and expensive to set up the infrastructure. You have to juggle an inference stack for generating the “rollouts” and a separate training stack for updating the model weights.

This is the problem Kyle and his team have solved with Serverless RL, which we just launched and we covered [last week](https://open.substack.com/pub/thursdai/p/oct-9-2025-dev-days-agent-era-samsungs?r=2imipa&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true). It’s a new offering that lets you run RL jobs without managing any servers or GPUs. The whole thing is powered by the CoreWeave stack, with tracing and evaluation beautifully visualized in Weave.

We also launched a [new model ](https://wandb.ai/site/inference/cw_openpipe_qwen3-14b-instruct)from the OpenPipe team on our inference service: a fine-tune-friendly “instruct” version of Qwen3 14B. The team is not just building amazing products, they’re also contributing great open-source models. It’s awesome to be working with them.

🛠️ Tools & Agents: Free Agents & Lightning-Fast Code Search

The agentic coding space saw two massive announcements this week, and we had the representatives of both companies on the show to discuss them!

First, Quinn Slack from Amp announced that they’re launching a completely free, ad-supported tier. I’ll be honest, my first reaction was, “Ads? In my coding agent? Eww.” But the more I thought about it, the more it made sense. My AI subscriptions are stacking up, and this model makes powerful agentic coding accessible to students and developers who can’t afford another $20/month. The ads are contextual to your codebase (think Baseten or Axiom), and they’re powered by a rotating mix of models using surplus capacity from providers. It’s a bold and fascinating business model.

This move was met with generally positive responses, though folks from a competing [agent](https://x.com/pashmerepat/status/1978934813253079383), claim that Amp is serving Grok-4-fast which XAI is giving out for free anyway? We’ll see how this shakes up. 

Cognition announces SWE-grep: RL-powered multi-turn context retriever for agentic code search ([Blog](https://cognition.ai/blog/swe-grep), [X](https://x.com/cognition/status/1978867021669413252), [Playground](https://playground.cognition.ai/), [Windsurf](https://windsurf.com/))

Then, just as we were about to sign off, friend of the pod Swyx (now from Cognition) dropped in with breaking news about SWE-grep. It’s a new, RL-tuned sub-agent for their Windsurf editor that makes code retrieval and context gathering ridiculously fast. We’re talking over 2,800 tokens per second. (yes, they are using Cerebras under the hood) 

The key insight from Swyx is that their model was trained for natively parallel tool calling, running up to eight searches on a codebase simultaneously. This speeds up the “read” phase of an agent’s workflow—which is 60-70% of the work—by 3-5x. It’s all about keeping the developer in a state of flow, and this is a huge leap forward in making agent interactions feel instantaneous. Swyx also dropped a hint that the next thing that comes is CodeMaps and they will make these retrievers look trivial! 

This was one for the books, folks. An AI making a novel cancer discovery, video models taking huge leaps, and the agentic coding space is on fire. The pace of innovation is just breathtaking. Thank you for being a ThursdAI subscriber, and as always, here’s the TL:DR and show notes for everything that happened in AI this week.

TL;DR and Show Notes

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* **Co Hosts** - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@yampeleg](http://x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed)

* **Jessica Gallegos**, Sr. Product Manager, Google DeepMind

* **Kyle Corbitt (**[**@corbtt**](https://x.com/corbtt)**)** - OpenPipe//W&B

* **Quinn Slack (**[**@sqs**](https://x.com/sqs/status/1978521044194398713)**)** - Amp

* **Swyx (**[**@swyx**](http://x.com/@swyx)**)** - Cognition

* **Open Source LLMs**

* KAIST KROMo - bilingual Korean/English 10B ([HF](https://t.co/kDIylkn5pC), [Paper](https://arxiv.org/abs/2510.09426))

* Qwen3-VL 3B and 8B ([X post](https://x.com/Alibaba_Qwen/status/1978150959621734624), [HF](https://huggingface.co/collections/Qw))

* Google’s C2S-Scale 27B: AI Model Validates Cancer Hypothesis in Living Cells ([X](https://x.com/sundarpichai/status/1978507110477332582), [Blog](https://blog.google/technology/ai/google-gemma-ai-cancer-therapy-discovery/), [Paper](https://www.biorxiv.org/content/10.1101/2025.04.14.648850v2))

* **Big CO LLMs + APIs**

* Claude Haiku 4.5: Fast, Cheap Model Rivals Sonnet 4 Accuracy ([X](https://x.com/claudeai/status/1978505436358697052), [Official blog](https://www.anthropic.com/news/introducing-claude-haiku-4-5))

* ChatGPT will loose restrictions; age-gating enables “adult mode” with new personality features coming ([X](https://x.com/sama/status/1978129344598827128))

* OpenAI updates memory management - no more “memory full” ([X](https://x.com/OpenAI/status/1978608684088643709), [FAQ](https://help.openai.com/en/articles/8590148-memory-faq))

* Microsoft is making every windows 11 an AI PC with copilot voice input ([X](https://x.com/zacbowden/status/1978822883217461388))

* Claude Skills: Custom instructions for AI agents now live ([X](https://x.com/claudeai/status/1978855432123723909), [Anthropic News](https://www.anthropic.com/news/skills), [YouTube Demo](https://www.youtube.com/watch?v=IoqpBKrNaZI))

* **Hardware**

* NVIDIA DGX Spark: desktop personal supercomputer for AI prototyping and local inference ([LMSYS Blog](https://lmsys.org/blog/2025-10-13-nvidia-dgx-spark/))

* Apple announces M5 chip with double AI performance ([Apple Newsroom](https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/))

* OpenAI and Broadcom set to deploy 10 gigawatts of custom AI accelerators ([Official announcement](https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/))

* **This weeks Buzz**

* New model - OpenPipe Qwen3 14B instruct ([link](https://wandb.ai/site/inference/cw_openpipe_qwen3-14b-instruct))

* Interview with Kyle Corbitt - RL, Serverless RL

* W&B Fully Connected London & Tokyo in 20 days - [SIGN UP](https://wandb.ai/site/resources/events/fully-connected/)

* **Vision & Video**

* Veo 3.1: Google’s Next-Gen Video Model Launches with Cinematic Audio ([Developers Blog](https://developers.googleblog.com/))

* Sora up to 15s and pro now up to 25s generation with a new storyboard feature

* Baidu’s MuseStreamer has >20 second generations ([X](https://x.com/Baidu_Inc/status/1978505872805658960))

* **AI Art & Diffusion & 3D**

* Worldlabs RTFM: Real-Time Frame Model renders 3D worlds at interactive speeds on a single H100 ([Blog](https://www.worldlabs.ai/blog/rtfm), [Demo](https://rtfm.worldlabs.ai/))

* DiT360: SOTA Panoramic Image Generation with Hybrid Training ([Project page](https://fenghora.github.io/DiT360-Page/), [GitHub](https://github.com/Insta360-Resea))

* Riverflow 1 tops the image‑editing leaderboard ([Sourceful blog](https://www.sourceful.com/blog/riverflow-1))

* **Tools**

* Amp launches a Free tier - powered by ads and surplus model capacity ([Website](https://ampcode.com/free))

* Cognition SWE-grep: RL-powered multi-turn context retriever for agentic code search ([Blog](https://cognition.ai/blog/swe-grep), [Playground](https://playground.cognition.ai/)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-oct-16-veo31-haiku-45-chatgpt/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-oct-16-veo31-haiku-45-chatgpt?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3NjM3Mjg3NywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.JdaKzfoAi5VlZyoAqjyyhpXZD-JOzxjv9_PvlujckYc&utm_campaign=CTA_5).

---

## 📆 Oct 9, 2025 — Dev Day’s Agent Era, Samsung’s 7M TRM Shock, Ling‑1T at 1T, Grok Video goes NSFW, and Serverless RL arrives

**Date:** October 10, 2025  
**Duration:** 1:41:29  
**Link:** [https://sub.thursdai.news/p/oct-9-2025-dev-days-agent-era-samsungs](https://sub.thursdai.news/p/oct-9-2025-dev-days-agent-era-samsungs)

Hey everyone, Alex here 👋

We’re deep in the post-reality era now. Between Sora2, the latest waves of video models, and “is-that-person-real” cameos, it’s getting genuinely hard to trust what we see. Case in point: I recorded a short clip with (the real) Sam Altman this week and a bunch of friends thought I faked it with Sora-style tooling. Someone even added a fake Sora watermark just to mess with people. Welcome to 2025.

This week’s episode and this write-up focus on a few big arcs we’re all living through at once: OpenAI’s Dev Day and the beginning of the agent-app platform inside ChatGPT, a bizarre and exciting split-screen in model scaling where a 7M recursive model from Samsung is suddenly competitive on reasoning puzzles while inclusionAI is shipping a trillion-parameter mixture-of-reasoners,  and Grok’s image-to-video now does audio and pushes the line on… taste. We also dove into practical evals for coding agents with Eric Provencher from Repo Prompt, and I’ve got big news from my day job world: W&B + CoreWeave launched Serverless RL, so training and deploying RL agents at scale is now one API call away.

Let’s get into it.

OpenAI’s 3rd Dev Day - Live Coverage + exclusive interviews

This is the third Dev Day that I got to attend in person, covering this for ThursdAI ([2023](https://sub.thursdai.news/p/nov-09), [2024](https://sub.thursdai.news/p/oct-3-how-i-met-sam-altman)), and this one was the best by far! The production quality of their events rises every year, and this year they’ve opened up the conference to >1500 people, had 3 main launches and a lot of ways to interact with the OpenAI folks! 

I’ve also gotten an exclusive chance to sit in on a fireside chat with Sam Altman and Greg Brokman (snippets of which I’ve included in the podcast, starting 01:15:00 and I got to ask Sam a few questions after that as well. 

Event Ambiance and Vibes

OpenAI folks outdid themselves with this event, the live demos were quite incredible, the location (Fort Mason), Food and just the whole thing was on point. The event concluded with a 1x1 Sam and Jony Ive chat that I hope will be published on YT sometime, because it was very insightful. 

By far the best reason to go to this event in person is meeting folks and networking, both OpenAI employees, and AI Engineers who use their products. It’s 1 day a year, when OpenAI makes all their employees who attend, Developer Experience folks, as you can and are encouraged to, interact with them, ask questions, give feedback and it’s honestly great! 

I really enjoy meeting folks at this event and consider this to be a very high signal network, and was honored to have quite a few ThursdAI listeners among the participants and OpenAI folk! If you’re reading this, thank you for your patronage 🫡 

Launches and Ships

OpenAI also shipped, and shipped a LOT! Sam was up on Keynote with 3 main pillars, which we’ll break down 1 by 1. ChatGPT Apps, AgentKit (+ agent builder) and Codex/New APIs

Codex & New APIs

Codex has gotten General Availability, but we’ve been using it all this time so we don’t really care, what we do care about is the new slack integration and the new Codex SDK, which means you can now directly inject Codex agency into your app. This flew a bit over people’s heads, but Romain Huet, VP of DevEx at OpenAI demoed on stage how his mobile app now has a Codex tab, where he can ask Codex to make changes to the app at runtime! It was quite crazy! 

ChatGPT Apps + AppsSDK

This was maybe the most visual and most surprising release, since they’ve tried to be an appstore before (plugins, customGPTs). But this time, it seems like, based on top of MCP, ChatGPT is going to become a full blown Appstore for 800+ million weekly active ChatGPT users as well. 

Some of the examples they have showed included Spotify and Zillow, where just by typing in “Spotify” in chatGPT, you will have an interactive app with it’s own UI, right inside of ChatGPT. So you could ask it to create a playlist for you based on your history, or ask Zillow to find homes in an area under a certain $$ amount.

The most impressive thing, is that those are only launch partners, everyone can (technically) build a ChatGPT app with their AppsSDK that’s built on top of... the MCP (model context protocol) spec! 

The main question remains about discoverability, this is where Plugins and CustomGPTs (previous attempts to create apps within ChatGPT have failed), and when I asked him about it, Sam basically said “we’ll iterate and get it right” (starting 01:17:00). So it remains to be seen if folks really need their ChatGPT as yet another Appstore. 

AgentKit, AgentBuilder and ChatKit

2025 is the year of agents, and besides launching quite a few of their own, OpenAI will not let you, build and host smart agents that can use tools, on their platform. Supposedly, with AgentBuilder, building agents is just dragging a few nodes around, prompting and connecting them. They had a great demo on stage where with less than 8 minutes, they’ve build an agent to interact with the DevDay website.

It’s also great to see how greatly does OpenAI adapt the MCP spec, as this too, is powered by MCP, as in, any external connection you want to give your agent, must happen with an MCP server. 

Agents for the masses is maybe not quite there yet

In reality though, things are not so easy. Agents require more than just a nice drag & drop interface, they require knowledge, iteration, constant evaluation (which they’ve also added, kudos!) and eventually, customized agents need code. 

I [spent an hour](https://x.com/altryne/status/1976024045020934317) trying it out yesterday, building an agent to search the ThursdAI archives. The experience was a mixed bag. The AI-native features are incredibly cool. For instance, you can just describe the JSON schema you want as an output, and it generates it for you. The widget builder is also impressive, allowing you to create custom UI components for your agent’s responses.

However, I also ran into the harsh realities of agent building. My agent’s web browsing tool failed because Substack seems to be blocking OpenAI’s crawlers, forcing me to fall back on the old-school RAG approach of uploading our entire archive to a vector store. And while the built-in evaluation and tracing tools are a great idea, they were buggy and failed to help me debug the error. It’s a powerful tool, but it also highlights that building a reliable agent is an iterative, often frustrating process that a nice UI alone can’t solve. It’s not just about the infrastructure; it’s about wrestling with a stochastic machine until it behaves.

But to get started with something simple, they have definitely pushed the envelope on what is possible without coding. 

OpenAI also dropped a few key API updates:

* **GPT-5-Pro** is now available via API. It’s incredibly powerful but also incredibly expensive. As Eric mentioned, you’re not going to be running agentic loops with it, but it’s perfect for a high-stakes initial planning step where you need an “expert opinion.”

* **SORA 2** is also in the API, allowing developers to integrate their state-of-the-art video generation model into their own apps. The API can access the 15-second “Pro” model but doesn’t support the “Cameo” feature for now.

* **Realtime-mini** is a game-changer for voice AI. It’s a new, ultra-fast speech-to-speech model that’s **80% cheaper **than the original Realtime API. This massive price drop removes one of the biggest barriers to building truly conversational, low-latency voice agents.

**My Chat with Sam & Greg - On Power, Responsibility, and Energy**

After the announcements, I’ve got to sit in a fireside chat with Sam Altman and Greg Brockman and ask some questions. Here’s what stood out:

When I asked about the energy requirements for their massive compute plans (remember the $500B Stargate deal?), Sam said they’d have announcements about Helion (his fusion investment) soon but weren’t ready to talk about it. Then someone from Semi Analysis told me most power will come from... generator trucks. 15-megawatt generator trucks that just drive up to data centers. We’re literally going to power AGI with diesel trucks!

On responsibility, when I brought up the [glazing](https://sub.thursdai.news/p/thursdai-may-1-qwen-3-phi-4-openai) incident and asked how they deal with being in the lives of 800+ million people weekly, Sam’s response was sobering: “This is not the excitement of ‘oh we’re building something important.’ This is just the stress of the responsibility... The fact that 10% of the world is talking to kind of one brain is a strange thing and there’s a lot of responsibility.”

Greg added something profound: “AI is far more surprising than I anticipated... The deep nuance of how these problems contact reality is something that I think no one had anticipated.”

**This Week’s Buzz: RL X-mas came early with Serverless RL! **([X](https://x.com/wandb/status/1975917052920678528), [Blog](https://openpipe.ai/blog/serverless-rl))

Big news from our side of the world! About a month ago, the incredible OpenPipe team joined us at Weights & Biases and CoreWeave. They are absolute wizards when it comes to fine-tuning and Reinforcement Learning (RL), and they wasted no time combining their expertise with CoreWeave’s massive infrastructure.

This week, they launched **Serverless RL**, a managed reinforcement learning service that completely abstracts away the infrastructure nightmare that usually comes with RL. It automatically scales your training and inference compute, integrates with W&B Inference for instant deployment, and simplifies the creation of reward functions and verifiers. RL is what turns a good model into a great model for a specific task, often with surprisingly little data. This new service massively lowers the barrier to entry, and I’m so excited to see what people build with it. We’ll be doing a deeper dive on this soon but please check out the [Colab Notebook](wandb.me/RLS) to get a taste of what AutoRL is like! 

**Open Source**

While OpenAI was holding its big event, the open-source community was busy dropping bombshells of its own.

**Samsung’s TRM: Is This 7M Parameter Model... Magic? **([X](https://x.com/jm_alexia/status/1975560628657164426), [Blog](https://t.co/w5ZDsHDDPE), [arXiv](https://arxiv.org/pdf/2510.04871.pdf))

This was the release that had everyone’s jaws on the floor. A single researcher from the Samsung AI Lab in Montreal released a paper on a **Tiny Recursive Model (TRM)**. Get this: it’s a **7 MILLION parameter model** that is outperforming giants like DeepSeek-R1 and Gemini 2.5 Pro on complex reasoning benchmarks like ARC-AGI. I had to read that twice. 7 million, not billion.

How is this possible? Instead of relying on brute-force scale, TRM uses a recursive process. It generates a first draft of an answer, then repeatedly critiques and refines its own logic in a hidden “scratchpad” up to 16 times. As Yam pointed out, the paper is incredibly insightful, and it’s a groundbreaking piece of work from a single author, which is almost unheard of these days. Eric made a great point that because it’s so small, it opens the door for hobbyists and solo researchers to experiment with cutting-edge architectures on their home GPUs. This feels like a completely new direction for AI, and it’s incredibly exciting.

**inclusionAI’s Ling-1T: Enter the Trillion Parameter Club **([X](https://x.com/AntLingAGI/status/1975942293330018426), [HF](https://huggingface.co/inclusionAI/Ling-1T), [Try it](https://zenmux.ai/settings/chat?model=inclusionai/ling-1t))

On the complete opposite end of the scale (about 3 OOM away), we have **Ling-1T**from inclusionAI. This is a **1 TRILLION parameter** Mixture-of-Experts (MoE) model. The key here is efficiency; while it has a trillion total parameters, it only uses about 37 billion active parameters per token.

The benchmarks are wild, showing it beating models like GPT-5-Main (in non-thinking mode) and Gemini 2.5 on a range of reasoning tasks. They claim to match Gemini’s performance using about half the compute. Of course, with any new model posting huge scores, there’s always the question of whether it was trained on the public test sets, but the results are undeniably impressive. It’s another example of the push towards maintaining top-tier performance while drastically reducing the computational cost of inference.

**More Open Source Goodness: Microsoft, AI21, and IBM**

It didn’t stop there.

* **Microsoft** released **UserLM-8B**, a fascinating Llama 3 finetune trained not to be an assistant, but to simulate the *user* in a conversation. As Yam explained from his own experience, this is a super useful technique for generating high-quality, multi-turn synthetic data to train more robust chatbot agents. ([X](https://x.com/altryne/status/1976122132355580113)**, **[**HF**](https://huggingface.co/microsoft/UserLM-8b)**)**

* Our friends at **AI21 Labs** are back with **Jamba Reasoning 3B**, a tiny but mighty 3-billion-parameter model. It uses a hybrid SSM-Transformer architecture, which makes it incredibly fast for its size, making it a great option for local inference on a laptop.

* **IBM** also released their **Granite** family of models, which also use a hybrid design. Their big focus is on enterprise-grade governance and trust, and it’s the first open model family to get an ISO certification for AI management systems.**Big Company Moves: Grok Imagine Levels Up... And Leans In**

Finally, let’s talk about the latest update to **Grok Imagine**. They’ve rolled out video generation with synchronized sound, and it’s fast—often faster than Sora. The quality has significantly improved, and it’s a powerful tool.

However, I have to talk about the other side of this. Grok is positioning itself as the “uncensored” alternative, and they are leaning into that hard. Their video generator has a “spicy” mode that explicitly generates 18+ content. But the thing that truly disturbed me was a new feature with their animated character, “Annie.” It’s a gamified engagement mechanic where you “make your connection better” by talking to her every day to unlock special rewards, like new outfits.

To be blunt, this is disgusting. We talk a lot on this show about the immense responsibility that comes with building these powerful AIs. I know from my conversations with folks at OpenAI and other labs that they think deeply about safety, preventing misuse, and the psychological impact these systems can have. This feature from Grok is the polar opposite. It leans into the worst fears about AI creating addictive, para-social relationships. It’s exploitative, and frankly, the team behind it should reconsider their choices IMO. 

All righty, this is mostly the new for this week, it’s been a very busy week, and if you’d like to see our live coverage + DevDay keynote + interviews I’ve had with [Simon Willison](https://substack.com/profile/5753967-simon-willison) , Greg Kamradt, Jeffrey Huber, Allesio from [Latent.Space](https://substack.com/profile/89230629-latentspace), Matthew Berman and more impactful folks, our livestream can be found here: 

I’m incredibly humbled and privileged to keep being invited to the Dev Day, and looking forward to cover more events, with exclusive interviews, on the ground reporting and insights. Please subscribe if you like this content to continue. 

TL;DR and Show Notes

* **Show Notes & Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* **Co-Hosts** - [@WolframRvnwlf](http://x.com/@WolframRvnwlf), [@yampeleg](http://x.com/yampeleg), [@nisten](http://x.com/@nisten), [@ldjconfirmed](http://x.com/@ldjconfirmed)

* **Guest**: Kyle Corbitt - OpenPipe / CoreWeave ([@corbtt](https://x.com/corbtt))

* **Guest**: Eric Provencher - Repo Prompt ([@pvncher](https://x.com/pvncher))

* **OpenAI Dev Day**

* OpenAI AgentKit All-in-One Agent Builder ([X](https://x.com/rohanpaul_ai/status/1975309479047798835), [OpenAI](https://openai.com/index/introducing-agentkit/))

* ChatGPT Apps & New APIs (GPT-5-pro, SORA, realtime-mini)

* **Open Source LLMs**

* Microsoft UserLM-8B Model Released ([X](https://x.com/altryne/status/1976122132355580113), [HF](https://huggingface.co/microsoft/UserLM-8b))

* Samsung Tiny Recursive Model (TRM) ([X](https://x.com/jm_alexia/status/1975560628657164426), [Blog](https://t.co/w5ZDsHDDPE), [arXiv](https://arxiv.org/pdf/2510.04871.pdf))

* AI21 Labs releases Jamba Reasoning 3B ([X](https://x.com/AI21Labs/status/1976271434004541641), [HF](https://huggingface.co/ai21labs/AI21-Jamba-Reasoning-3B))

* inclusionAI debuts Ling-1T: Trillion-Scale Efficient Reasoner ([X](https://x.com/AntLingAGI/status/1975942293330018426), [HF](https://huggingface.co/inclusionAI/Ling-1T), [Try it](https://zenmux.ai/settings/chat?model=inclusionai/ling-1t))

* IBM Granite Models

* **Evals**

* Repo Bench by Repo Prompt ([Web](https://repo.prompt.com/bench))

* **Big CO LLMs + APIs**

* Qwen 3 Omni & Realtime Models

* Google DeepMind unveils Gemini 2.5 Computer-Use model ([X](https://x.com/GoogleDeepMind/status/1975917052920678528), [Blog](https://blog.google/technology/google-deepmind/gemini-computer-use-model))

* Google Gemini Flash 2.5 (new)

* Grok Imagine updated with video and sound

* **This weeks Buzz**

* OpenPipe (part of Coreweave,W&B) launch Serverless RL ([X](https://x.com/wandb/status/1975917052920678528), [Blog](https://openpipe.ai/blog/serverless-rl), [Notebook](http://wandb.me/RLS))

* **Vision & Video**

* Ovi: Open Source Video & Synchronized Audio Generation ([X](https://x.com/linoy_tsaban/status/1975924336935743737), [HF](https://huggingface.co/blog/MonsterMMORPG/ovi-generate-videos-with-audio-like-veo-3-or-sora))

* **Voice & Audio**

* GPT-realtime-mini: OpenAI’s ultra-fast speech-to-speech model API ([OpenAI Blog](https://platform.openai.com/docs/models/gpt-realtime-mini), [TechCrunch](https://techcrunch.com/2025/10/06/openai-ramps-up-developer-push-with-more-powerful-models-in-its-api/))

* **AI Art & Diffusion & 3D**

* Bagel.com: Paris – Decentralized Diffusion Model ([X](https://x.com/bageldotcom/status/1975596255624769858), [HF](https://huggingface.co/bageldotcom/paris), [Blogpost](https://blog.bagel.com/p/paris)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/oct-9-2025-dev-days-agent-era-samsungs/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/oct-9-2025-dev-days-agent-era-samsungs?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3NTc2MzI3NywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.nCaXqps9R_lHUU4d4gVt37FHTRYs5R2ucI6t8xDxMhE&utm_campaign=CTA_5).

---

## Sora 2 Crushes TikTok, Claude 4.5 Fizzles, DeepSeek innovates attention and GLM 4.6 Takes the Crown! 🔥

**Date:** October 03, 2025  
**Duration:** 1:39:59  
**Link:** [https://sub.thursdai.news/p/thursdai-oct-2-sora-2-the-new-tiktok](https://sub.thursdai.news/p/thursdai-oct-2-sora-2-the-new-tiktok)

Hey everyone, Alex here (yes the real me if you’re reading this) 

The weeks are getting crazier, but what OpenAI pulled this week, with a whole new social media app attached to their latest AI breakthroughs is definitely breathtaking! Sora2 released and instantly became a viral sensation, shooting to the top 3 free iOS spot on AppStore, with millions of videos watched, and remixed. 

On weeks like these, even huge releases like Claude 4.5 are taking the backseat, but we still covered them! 

For listeners of the pod, the second half of the show was very visual heavy, so it may be worth it watching the YT video attached in a comment if you want to fully experience the Sora revolution with us! (and if you want a SORA invite but don’t have one yet, more on that below) 

ThursdAI - if you find this valuable, please support us by subscribing! 

Sora 2 - the AI video model that signifies a new era of social media

Look, you’ve probably already heard about the SORA-2 release, but in case you haven’t, OpenAI released a whole new model, but attached it to a new, AI powered social media experiment in the form of a very addictive TikTok style feed. Besides being hyper-realistic, and producing sounds and true to source voice-overs, Sora2 asks you to create your own “Cameo” by taking a quick video, and then allows you to be featured in your own (and your friends) videos. 

This makes a significant break from the previously “slop” based meta Vibes, becuase, well, everyone loves seeing themselves as the stars of the show! 

Cameos are a stroke of genius, and what’s more, one can allow everyone to use their Cameo, which is what Sam Altman did at launch, making everyone Cameo him, and turning him, almost instantly into one of the most meme-able (and approachable) people on the planet! 

Sam sharing away his likeness like this for the sake of the app achieved a few things, it added trust in the safety features, made it instantly viral and showed folks they shouldn’t be afraid of adding their own likeness. 

Vibes based feed and remixing

Sora 2 is also unique in that, it’s the first social media with UGC (user generated content) where content can ONLY be generated, and all SORA content is created within the app. It’s not possible to upload pictures that have people to create the posts, and you can only create posts with other folks if you have access to their Cameos, or by Remixing existing creations. 

Remixing is also a way to let users “participate” in the creation process, by adding their own twist and vibes! 

Speaking of Vibes, while the SORA app has an algorithmic For You page, they have a completely novel and new way to interact with the algorithm, by using their Pick a Mood feature, where you can describe which type of content you want to see, or not see, with natural language! 

I believe that this feature will come to all social media platforms later, as it’s such a game changer. Want only content in a specific language? or content that doesn’t have Sam Altman in it? Just ask! 

Content that makes you feel good

The most interesting thing is about the type of content is, there’s no sexualisation (because all content is moderated by OpenAI strong filters), and no gore etc. OpenAI has clearly been thinking about teenagers and have added parent controls, things like being able to turn of the For You page completely etc to the mix. 

Additionally, SORA seems to be a very funny model, and I mean this literally. You can ask the video generation for a joke and you’ll often get a funny one. The scene setup, the dialogue, the things it does even unprompted are genuinely entertaining. 

AI + Product = Profit? 

OpenAI shows that they are one of the worlds best product labs in the world, not just a foundational AI lab. Most AI advancements are tied to products, and in this case, the whole experience is so polished, it’s hard to accept that it’s a brand new app from a company that didn’t do social before. There’s very little buggy behavior, videos are loaded up quick, there’s even DMs! I’m thoroughly impressed and am immersing myself in the SORA sphere. Please give me a follow there and feel free to use my Cameo by tagging [@altryne](https://sora.chatgpt.com/profile/altryne) in there. I love seeing how folks have used my Cameo, it makes me laugh 😂 

The copyright question is.. wild

Remember last year when I asked Sam why Advanced Voice Mode couldn’t sing Happy Birthday? He said they didn’t have classifiers to detect IP violations. Well, apparently that’s not a concern anymore because SORA 2 will happily generate perfect South Park episodes, Rick and Morty scenes, and Pokemon battles. They’re not even pretending they didn’t train on this stuff. You can even generate videos with any dead famous person (I’ve had zoom meetings with Michael Jackson and 2Pac, JFK and Mister Rogers) 

Our friend Ryan Carson already used it to create a YouTube short ad for his startup in two minutes. What would have cost $100K and three months now takes six generations and you’re done. This is the real game-changer for businesses.

Getting invited

EDIT: If you’re reading this on Friday, try the code `FRIYAY` and let me know in comments if it worked for you 🙏

I wish I would have invites for all of you, but all invited users have 4 other folks they can invite, so we shared a bunch of invites during the live show, and asked folks to come back and invite other listeners, this went on for half an hour so I bet we’ve got quite a few of you in! If you’re still looking for an invite, you can visit the [thread on X](thursdai.news/sora) and see who claimed and invite and ask them for one, tell them you’re also a ThursdAI listener, they hopefully will return the favor! 

Alternatively, OpenAI employees often post codes with a huge invite ratio, so follow [@GabrielPeterss4](https://x.com/GabrielPeterss4) who often posts codes and you can get in there fairly quick, and if you’re not in the US, I heard a VPN works well. Just don’t forget to follow me on there as well 😉

A Week with OpenAI Pulse: The Real Agentic Future is Here

Listen to me, this may be a hot take. I think OpenAI Pulse is a bigger news story than Sora. I’ve told you about Pulse last week, but today on the show I was able to share my weeks worth of experience, and honestly, it’s now the first thing I look at when I wake up in the morning after brushing my teeth! 

While Sora is changing media, Pulse is changing how we interact with AI on a fundamental level. Released to Pro subscribers for now, Pulse is an agentic, personalized feed that works for you behind the scenes. Every morning, it delivers a briefing based on your interests, your past conversations, your calendar—everything. It’s the first asynchronous AI agent I’ve used that feels truly proactive.

You don’t have to trigger it. It just works. It knew I had a flight to Atlanta and gave me tips. I told it I was interested in Halloween ideas for my kids, and now it’s feeding me suggestions. Most impressively, this week it surfaced a new open-source video model, Kandinsky 5.0, that I hadn’t seen anywhere on X or my usual news feeds. An agent found something new and relevant for my show, without me even asking.

This is it. This is the life-changing-level of helpfulness we’ve all been waiting for from AI. Personalized, proactive agents are the future, and Pulse is the first taste of it that feels real. I cannot wait for my next Pulse every morning.

**This Week’s Buzz: The AI Build-Out is NOT a Bubble**

This show is powered by Weights & Biases from CoreWeave, and this week that’s more relevant than ever. I just got back from a company-wide offsite where we got a glimpse into the future of AI infrastructure, and folks, the scale is mind-boggling.

CoreWeave, our parent company, is one of the key players providing the GPU infrastructure that powers companies like OpenAI and Meta. And the commitments being made are astronomical. In the past few months, CoreWeave has locked in a **$22.4B deal with OpenAI**, a **$14.2B pact with Meta**, and a **$6.3B “backstop” guarantee with NVIDIA** that runs through 2032.

If you hear anyone talking about an “AI bubble,” show them these numbers. These are multi-year, multi-billion dollar commitments to build the foundational compute layer for the next decade of AI. The demand is real, and it’s accelerating. And the best part? As a Weights & Biases user, you have access to this same best-in-class infrastructure that runs OpenAI through our inference services. Try [wandb.me/inference](wandb.me/inference)**, **and let me know if you need a bit of a credit boost! 

Claude Sonnet 4.5: The New Coding King Has a Few Quirks

On any other week, Anthropic’s release of **Claude Sonnet 4.5 **would’ve been the headline news. They’re positioning it as the new best model for coding and complex agents, and the benchmarks are seriously impressive. It matches or beats their previous top-tier model, Opus 4.1, on many difficult evals, all while keeping the same affordable price as the previous Sonnet.

One of the most significant jumps is on the OS World benchmark, which tests an agent’s ability to use a computer—opening files, manipulating windows, and interacting with applications. Sonnet 4.5 scored a whopping 61.4%, a massive leap from Opus 4.1’s 44%. This clearly signals that Anthropic is doubling down on building agents that can act as real digital assistants.

However, the real-world experience has been a bit of a mixed bag. My co-host Ryan Carson, whose company Amp switched over to 4.5 right away, noted some regressions and strange errors, saying they’re even considering switching back to the previous version until the rough edges are smoothed out. Nisten also found it could be more susceptible to “slop catalysts” in prompting. It seems that while it’s incredibly powerful, it might require some re-prompting and adjustments to get the best, most stable results. The jury’s still out, but it’s a potent new tool in the developer’s arsenal.

Open Source LLMs: DeepSeek’s Attention Revolution

Despite the massive news from the big companies, open source still brought the heat this week, with one release in particular representing a fundamental breakthrough.

DeepSeek released **V3.2 Experimental**, and the big news is DSA, or DeepSeek Sparse Attention. For those who don’t know, one of the biggest bottlenecks in LLMs is the “quadratic attention problem”—as you double the context length, the computation and memory required quadruple. This makes very long contexts incredibly expensive. DeepSeek’s new architecture makes the cost curve nearly flat, allowing for massive context at a fraction of the cost, all while maintaining the same SOTA performance as their previous model.

This is one of those “unhobbling moments,” like the invention of RoPE or GRPO, that moves the entire field forward. Everyone will be able to implement this, making all open-source models faster and more efficient. It’s a huge deal.

We also saw major releases from [Z.ai](Z.ai) with **GLM-4.6**, an advanced agentic model with a 200K context window that’s getting incredibly close to Claude’s performance, and a surprise from **ServiceNow SLAM Labs**, who dropped **Apriel-1.5-15B**, a frontier-level multimodal model that’s fully open source. It’s amazing to see a huge enterprise company contributing to the open-source ecosystem at this level.

Multimodal Madness: Audio, Video, and Image Models updates

The torrent of releases continued across all modalities this week, a bit overshadowed by SORA but definitely still happened (all links in the TL;DR section)

In voice and audio, our friends at **Hume AI launched Octave 2**, their next-gen text-to-speech model that’s faster, cheaper, and now fluent in over 11 languages. We also saw **LFM2-Audio from Liquid AI**, an incredibly efficient 1.5B parameter end-to-end audio model with sub-100ms latency.

In video, the open-source community answered Sora 2 with **Kandinsky 5.0**, a new 2B parameter text-to-video model that is claiming the #1 spot in open source and looks incredibly promising. And as I mentioned on the show, I wouldn’t have even known about it if it weren’t for my new personal AI agent, Pulse!

Finally, in AI art, Tencent dropped a monster: **HunyuanImage 3.0**, a massive 80-billion-parameter open-source text-to-image model. The scale of these open-source releases is just breathtaking.

Agentic browsing for all is here

Just as I was wrapping up the show, Perplexity has decided to let everyone in to use their Comet Agentic browser. I strongly recommend it, as I switched to it lately and it’s great! 

I’m using it right now to run some agents, it can click stuff, scroll through stuff, collect info across tabs, it’s really great. Give it a spin, really, it’s worth getting into the habit of agentic browsing! 

Many of you were asking me for invites before, well, it’s free access now, [download it here](https://comet.perplexity.ai/) (not sponsored, I just really like it) 

Phew, ok, this was a WILD week, and I’m itching to get back to creating and seeing all the folks who used my Cameo on SORA, which you can see too btw if you hit the Cameo button here ([https://sora.chatgpt.com/profile/altryne](https://sora.chatgpt.com/profile/altryne)) 

Next week is OpenAI’s Dev Day, and for the third year in a row we’re going to cover it, so follow us on social media and tune in Monday 8:30am Pacific. We’ll be live streaming from the location and re-streaming the keynote with Sam so don’t miss it! 

TL;DR and Show Notes

**Hosts and Guests**:

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@yampeleg](x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed) [@ryancarson](https://x.com/ryancarson/status/1957809743679906246)

**Big CO LLMs + APIs**:

* OpenAI releases SORA2 + a new social media app ([X](https://x.com/altryne/status/1973568567489798144), [Blog](https://openai.com/index/sora-2/), [App download](https://apps.apple.com/us/app/sora-by-openai/id6744034028))

* Anthropic releases Claude Sonnet 4.5 - same price as 4.1 - leading coding model ([X](https://x.com/claudeai/status/1972706807345725773))

* OpenAI launches Instant Checkout & Agentic Commerce Protocol ([X](https://x.com), [Protocol](https://agenticcommerce.dev))

**Open Source LLMs**:

* DeepSeek V3.2 Exp: Sparse Attention, Cost Drop ([X](https://x.com/deepseek_ai/status/1972604768309871061), [Evals](https://twitter.com/ArtificialAnlys/status/1973230103854456993), [HF](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp))

* Apriel-1.5-15B-Thinker by ServiceNow SLAM Labs ([X](https://twitter.com/ServiceNowRSRCH/status/1973100536280027586), [HF](https://huggingface.co/ServiceNow-AI/Apriel-1.5-15b-Thinker), [Arxiv](https://arxiv.org/abs/2508.10948))

* [Z.ai](Z.ai) GLM-4.6: advanced Agentic flagship model ([X](https://x.com/Zai_org/status/1973034639708344767), [Blog](https://z.ai/blog/glm-4.6), [HF](https://huggingface.co/zai-org/GLM-4.6))

**This weeks Buzz**:

* CoreWeave locks **$22.4B OpenAI**, a **$6.3B NVIDIA “backstop”**, and a **$14.2B Meta** compute pact ([X](https://x.com/CoreWeave/status/1971218329713938942))

**Voice & Audio**:

* Hume AI launches Octave 2 ([X](https://twitter.com/hume_ai/status/1973450822840152455), [Blog](https://hume.ai/blog/octave2))

* LFM2-Audio: End-to-end audio foundation model ([X](https://x.com/LiquidAI_/status/1973372092230836405), [Blog](https://www.liquid.ai/blog/lfm2-audio-an-end-to-end-audio-foundation-model), [HF](https://huggingface.co/LiquidAI/LFM2-Audio-1.5B))

**Vision & Video**:

* Kandinsky 5.0 T2V Lite: #1 open-source text-to-video ([Blog](https://ai-forever.github.io/Kandinsky-5/), [GitHub](https://github.com/ai-forever/Kandinsky-5), [HF](https://huggingface.co/collections/ai-forever/kandinsky-50-t2v-lite-68d71892d2cc9b02177e5ae5), [Try It](https://t.me/kandinsky_access_bot))

**AI Art & Diffusion & 3D**:

* HunyuanImage 3.0: 80B Open-Source Text-to-Image by Tencent ([X](https://twitter.com/TencentHunyuan/status/1972130405160833334), [HF](https://huggingface.co/tencent/HunyuanImage-3.0), [Github](https://github.com/Tencent-Hunyuan)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-oct-2-sora-2-the-new-tiktok/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-oct-2-sora-2-the-new-tiktok?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3NTE1MjM4NiwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.vb191_pQaKspBYaenugvHkeIzsAbojabAkiwtBknBXU&utm_campaign=CTA_5).

---

