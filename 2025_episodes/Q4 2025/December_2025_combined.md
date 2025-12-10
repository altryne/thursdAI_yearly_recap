# ThursdAI Episodes - December 2025

Total Episodes: 2

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

