# 📆 ThursdAI - July 17th - Kimi K2 👑, OpenAI Agents, Grok Waifus, Amazon Kiro, W&B Inference & more AI news!

**Date:** July 17, 2025  
**Duration:** 1:45:29  
**Link:** [https://sub.thursdai.news/p/thursdai-july-17th-kimi-k2-openai](https://sub.thursdai.news/p/thursdai-july-17th-kimi-k2-openai)

---

## Description

Hey everyone, Alex here 👋 and WHAT a week to turn a year older! Not only did I get to celebrate my birthday with 30,000+ of you live during the OpenAI stream, but we also witnessed what might be the biggest open-source AI release since DeepSeek dropped. Buckle up, because we're diving into a trillion-parameter behemoth, agentic capabilities that'll make your head spin, and somehow Elon Musk decided Grok waifus are the solution to... something.

This was one of those weeks where I kept checking if I was dreaming. Remember when DeepSeek dropped and we all lost our minds? Well, buckle up because Moonshot's Kimi K2 just made that look like a warm-up act. And that's not even the wildest part of this week! 

As always, all the show notes and links are at the bottom, here's our liveshow (which included the full OAI ChatGPT agents watch party) - Let's get into it! 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

**🚀 Open Source LLMs: The Kimi K2 Revolution**

**The New Open Source King Has Arrived**

Folks, I need you to understand something - just a little after we finished streaming last week celebrating Grok 4, a company called Moonshot decided to casually drop what might be the most significant open source release since... well, maybe ever?

**Kimi K2** is a 1 trillion parameter model. Yes, you read that right - TRILLION. Not billion. And before you ask "but can my GPU run it?" - this is an MOE (Mixture of Experts) with only 32B active parameters, which means it's actually usable while being absolutely massive.

Let me give you the numbers that made my jaw drop:

* **65.8% on SWE-bench Verified** - This non-reasoning model beats Claude Sonnet (and almost everything else)

* **384 experts** in the mixture (the scale here is bonkers)

* **128K context window** standard, with rumors of 2M+ capability

* Trained on **15.5 trillion tokens** with the new Muon optimizer

The main thing about the SWE-bench score is not even just the incredible performance, it's the performance without thinking/reasoning + price! 

**The Muon Magic**

Here's where it gets really interesting for the ML nerds among us. These folks didn't use AdamW - they used a new optimizer called Muon (with their own Muon Clip variant). Why does this matter? They trained to 15.5 trillion tokens with ZERO loss spikes. That beautiful loss curve had everyone in our community slack channels going absolutely wild. 

As Yam explained during the show, claiming you have a better optimizer than AdamW is like saying you've cured cancer - everyone says it, nobody delivers. Well, Moonshot just delivered at 1 trillion parameter scale.

**Why This Changes Everything**

This isn't just another model release. This is "Sonnet at home" if you have the hardware. But more importantly:

* **Modified MIT license** (actually open!)

* **5x cheaper than proprietary alternatives**

* **Base model released** (the first time we get a base model this powerful)

* Already has **Anthropic-compatible API** (they knew what they were doing)

The vibes are OFF THE CHARTS. Every high-taste model tester I know is saying this is the best open source model they've ever used. It doesn't have that "open source smell" - it feels like a frontier model because it IS a frontier model.

**Not only a math genius**

Importantly, this model is great at multiple things, as folks called out it's personality or writing style specifically! Our Friend Sam Paech, creator of [EQBench](https://eqbench.com/), has noted that this is maybe the first time an open source model writes this well, and is in fact SOTA on his Creative Writing benchmark and EQBench! 

**Quick Shoutouts**

Before we dive deeper, huge props to:

* **Teknium** for dropping the Hermes 3 dataset (nearly 1M high-quality entries!) ([X](https://x.com/Teknium1/status/1945259797517099126))

* **LG** (yes, the fridge company) for EXAONE 4.0 - their 32B model getting 81.8% on MMLU Pro is no joke ([X](https://x.com/testingcatalog/status/1945142194303537225))

**🎉 This Week's Buzz: W&B Inference Goes Live with Kimi-K2! (**[**X**](https://x.com/weights_biases/status/1945204732735447222)**)**

Ok, but what if you want to try Kimi-K2 but don't have the ability to run 1T models willy nilly? Well, Folks, I've been waiting TWO AND A HALF YEARS to say this: **We're no longer GPU poor!**

Weights & Biases + CoreWeave = Your new inference playground. We launched Kimi K2 on our infrastructure within 3 days of release! 

Sitting behind the scenes on this launch was surreal - as I've been covering all the other inference service launches, I knew exactly what we all want, fast inference, full non-quantized weights, OpenAI API compatibility, great playground to test it out, function calling and tool use. And we've gotten almost all of these, while the super cracked CoreWeave and W&B Weave teams worked their ass off over the weekend to get this shipped in just a few days! 

And here’s the kicker: I’m giving away $50 in inference credits to 20 of you to try Kimi K2 on our platform. Just reply “K2-Koolaid-ThursdAI” to our X launch post [here](https://x.com/weights_biases/status/1945204732735447222) and we'll pick up to 20 winners with $50 worth of credits! 🫡

It’s live now at [**api.inference.wandb.ai/v1**](api.inference.wandb.ai/v1) (model ID: moonshotai/Kimi-K2-Instruct), fully integrated with Weave for tracing and evaluation. We’re just getting started, and I want your feedback to make this even better. More on [**W&B Inference Docs**](https://weave-docs.wandb.ai/guides/integrations/inference/#advanced-example-use-weave-evaluations-and-leaderboards-with-the-inference-service) - oh and everyone gets $2 free even without me, which is like 500K tokens to test it out.

Big CO LLMs + APIs

The big players didn't sleep this week either—funding flew like confetti, Grok went full anime, and OpenAI dropped agents mid-stream (we reacted live!). Amazon snuck in with dev tools, and Gemini embeddings claimed the throne. Let's get through some of these openers before we get to the "main course" which of course came from OpenAI

**Grok Gets... Waifus?**

I can't believe I'm writing this in a serious AI newsletter, but here we are. XAI added animated 3D characters to Grok, including "Annie" - and let's just say she's very... interactive. XAI partnered with a company that does real time animated 3d avatars and these are powered by Grok so... they are a bit unhinged! 

The same Elon who's worried about birth rates just created nuclear-grade digital companions. The Grok app shot to #1 in the Japanese App Store immediately. Make of that what you will. 😅

They even posted a job for "Full Stack Waifu Engineer" - we truly live in the strangest timeline.

XAI also this week [addressed](https://x.com/xai/status/1945039609840185489) the concerns we all had with "mechahitler" and the Grok4 issues post launch (where it used it's web search to see "what does Elon think" when it was asked about a few topics) 

Credit for finding the prompt change: Simon Willison

**Other Quick Hits from Big Tech**

* **Gemini Embedding Model**: New SOTA on MTEB leaderboards (68.32 score) ([dev blog](https://developers.googleblog.com/en/gemini-embedding-text-model-now-available-gemini-api/))

* **Amazon S3 Vectors**: Native vector storage in S3 (huge for RAG applications) ([X](https://x.com/awscloud/status/1945271447619809504))

* **Amazon Kiro**: Their VS Code fork with spec-driven development (think PM-first coding) ([X](https://x.com/ajassy/status/1944785963663966633))

**🔥 OpenAI Agents: ChatGPT Levels Up to Do-It-All Sidekick **

We timed it perfectly—OpenAI's live stream hit mid-show, and we reacted with 30,000+ of you! And while we didn't get the rumored Open Source model from OAI, we did get... ChatGPT Agent (codename Odyssey) which merges Deep Research's fast-reading text browser with Operator's clicky visual browser and terminal access, all RL-tuned to pick tools smartly. It browses, codes, calls APIs (Google Drive, GitHub, etc., if you connect), generates images, and builds spreadsheets/slides—handling interruptions, clarifications, and takeovers for collaboration. **SOTA jumps: 41.6% on Humanities Last Exam (double O3), 27.4% on FrontierMath**, 45.5% on SpreadsheetBench, 68.9% on BrowseComp.

These are insane jumps in capabilities folks, just... mindblowing that we can now have agents that are SO good! 

The team demoed wedding planning (outfits, hotels, gifts with weather/venue checks), sticker design/ordering, and an MLB itinerary spreadsheet—wild to watch it chain thoughts on recordings. 

Wolfram called it the official start of agent year; Yam hyped the product polish (mobile control!); Nisten noted it's packaged perfection over DIY. I refreshed ChatGPT obsessively—mind-blown at turning my phone into a task master. Available now for Pro/Plus/Team (400/40 queries/month), Enterprise soon. This is the "feel the AGI" moment Sam mentioned—game over for tedious tasks (OpenAI announcement: [**https://openai.com/index/introducing-chatgpt-agent/**](https://openai.com/index/introducing-chatgpt-agent/).)[).](https://openai.com/index/introducing-chatgpt-agent/).)

I've yet to get access to it, but I'm very much looking forward to testing it out and letting you guys know how it works! 

Combining the two browser modes (visual that has my cookies and textual that can scan tons of websites super quick) + CLI + deep research abilities + RL for the right kind of tool use all sounds incredibly intriguing! 

**Vision & Video**

**Runway’s Act-Two: Motion Capture Gets a Major Upgrade **([X](https://x.com/runwayml/status/1945189222542880909), [YouTube](https://www.youtube.com/watch?v=JW8PHlFD7HM))

Runway’s latest drop, Act-Two, is a next-gen motion capture model that’s got creatives buzzing. It tracks head, face, body, and hands with insane fidelity, animating any character from a single performance video. It’s a huge leap from Act-One, already in use for film, VFX, and gaming, and available now to enterprise and creative customers with a full rollout soon. 

**Voice & Audio**

**Mistral’s Voxtral: Open Speech Recognition Champ **([X](https://x.com/MistralAI/status/1945130173751288311), [HF](https://huggingface.co/mistralai))

Mistral AI is killing it with Voxtral, a state-of-the-art open speech recognition model. With Voxtral Small at 24B for production and Mini at 3B for edge devices, it outperforms OpenAI’s Whisper large-v3 across English and multilingual tasks like French, Spanish, Hindi, and German. Supporting up to 32K token context (about 30-40 minutes of audio), it offers summarization and Q&A features, all under an Apache 2.0 license. At just $0.001 per minute via API, it’s a steal for real-time or batch transcription. 

**Tools**

**Liquid AI’s LEAP and Apollo: On-Device AI for All**

Liquid AI is bringing AI to your pocket with LEAP, a developer platform for building on-device models, and Apollo, a lightweight iOS app to run small LLMs locally. We’re talking 50-300MB models optimized for minimal battery drain and instant inference, no cloud needed. It’s privacy-focused and plug-and-play, perfect for offline workflows on Android and iOS. Developers, this is your prototyping dream—join the community via **X**.

**Amazon Kiro: Your Spec-Driven Coding Buddy**

I’ve already touched on Amazon’s Kiro, but let me reiterate—this spec-driven AI IDE is a standout. It structures your dev process around requirements, letting you define projects in plain language or diagrams before coding starts. It automates docs, testing, and more, feeling like a technical PM guiding you from concept to production. Early users are hooked on its PRD mode, and it’s free during preview. Give it a spin—details on **X**.

**Wrapping Up: An Unforgettable AI Birthday Bash**

What a week, folks! From Kimi K2 redefining open-source power to OpenAI’s ChatGPT Agent ushering in a new era of task automation, this has been a whirlwind of innovation. Throw in Grok’s quirky waifus and our own W&B Inference launch, and I’m left speechless on my birthday. Sharing this with over 30,000 of you during our live stream was the ultimate gift—AI is moving at a pace I couldn’t have dreamed of when I started ThursdAI. Here’s to more breakthroughs, and I can’t wait to see what you build with Kimi K2 credits. Let’s keep pushing the boundaries together!

P.S - If you'd like to support this podcast/newsletter and give me a birthday present, the best way is to tell your friends about it and the second best way is to subscribe 👏 

TL;DR and Show Notes

Here’s everything we covered this week on ThursdAI for July 17, 2025, packed with links and key highlights for you to dive deeper:

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](https://x.com/@altryne))

* Co-Hosts - [@WolframRvnwlf](https://x.com/@WolframRvnwlf), [@yampeleg](https://x.com/@yampeleg), [@nisten](https://x.com/@nisten), [@ldjconfirmed](https://x.com/@ldjconfirmed)

* **Open Source LLMs**

* Moonshot launches Kimi K2 - a 1T param MoE crushing SWE Bench Verified at 65.8% ([X post](https://x.com/Kimi_Moonshot/status/1943687594560332025), [HuggingFace](https://huggingface.co/moonshotai), [API & docs](https://platform.moonshot.ai), [GitHub](https://github.com/MoonshotAI/Kimi-K2))

* Teknium drops Hermes 3 dataset - nearly 1M samples for training agentic models ([X](https://x.com/Teknium1/status/1945259797517099126))

* LGAI EXAONE-4.0 - hybrid attention, 32B & 1.2B models with 131K+ context ([X](https://x.com/Presidentlin/status/1944977367111291161), [HuggingFace](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-32B))

* **Big CO LLMs + APIs**

* OpenAI’s ChatGPT Agent - unified agentic AI for real-world tasks, scoring 41.6% on HLE ([Announcement](https://openai.com/index/introducing-chatgpt-agent/))

* Grok 4 waifus - XAI adds animated characters, topping Japan’s App Store

* Mira Murati’s Thinking Machines Lab - $2B funding for open AI science ([X](https://x.com/miramurati/status/1945166365834535247))

* Gemini Embedding Model - #1 on MTEB with 68.32 score ([X](https://x.com/OfficialLoganK/status/1944806630979461445), [Dev Blog](https://developers.googleblog.com/en/gemini-embedding-text-model-now-available-gemini-api/))

* Amazon S3 Vectors - preview for vector storage, up to 90% cost savings ([X](https://x.com/awscloud/status/1945271447619809504))

* **This Week’s Buzz**

* Kimi K2 on W&B Inference - open, scalable production access, $50 credits with “K2KoolAid” ([X](https://x.com/weights_biases/status/1945204732735447222), [Docs](https://weave-docs.wandb.ai/guides/integrations/inference/#advanced-example-use-weave-evaluations-and-leaderboards-with-the-inference-service))

* Wolfram’s Evaluation of W&B service ([X](https://x.com/altryne/status/1945586487627554938))

* **Vision & Video**

* Runway’s Act-Two - next-gen motion capture for head, face, body, hands ([X](https://x.com/runwayml/status/1945189222542880909), [YouTube](https://www.youtube.com/watch?v=JW8PHlFD7HM))

* **Voice & Audio**

* Mistral’s Voxtral - open SOTA speech recognition, beats Whisper v3 ([X](https://x.com/MistralAI/status/1945130173751288311), [HuggingFace](https://huggingface.co/mistralai))

* **AI Art & Diffusion & 3D**

* OpenAI image service API adds high-quality mode ([X](https://x.com/OpenAIDevs/status/1945538534884135132))

* **Tools**

* Liquid AI’s LEAP & Apollo - on-device AI for mobile, privacy-first ([X](https://x.com/LiquidAI_/status/1945105323846504821))

* Amazon’s Kiro - spec-driven AI IDE, free in preview ([X](https://x.com/ajassy/status/1944785963663966633)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-july-17th-kimi-k2-openai/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-july-17th-kimi-k2-openai?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2ODU4OTE0OCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.dWTO7WMoMgQzYHlVdpUft7ybfteeXh8k_hjcDVVz97k&utm_campaign=CTA_5).
