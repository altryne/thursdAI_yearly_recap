# ThursdAI Episodes - May 2025

Total Episodes: 5

---

## 📆 ThursdAI - May 29 - DeepSeek R1 Resurfaces, VEO3 viral moments, Opus 4 a week after, Flux Kontext image editing & more AI news

**Date:** May 29, 2025  
**Duration:** 1:28:18  
**Link:** [https://sub.thursdai.news/p/thursdai-may-29-deepseek-r1-resurfaces](https://sub.thursdai.news/p/thursdai-may-29-deepseek-r1-resurfaces)

Hey everyone, Alex here 👋

Welcome back to another absolutely wild week in AI! I'm coming to you live from the Fontainebleau Hotel in Vegas at the Imagine AI conference, and wow, what a perfect setting to discuss how AI is literally reimagining our world. After last week's absolute explosion of releases (Claude Opus 4, Google I/O madness, OpenAI Codex and Jony colab), this week gave us a chance to breathe... sort of. Because even in a "quiet" week, we still got a new DeepSeek model that's pushing boundaries, and the entire internet discovered that we might all just be prompts. Yeah, it's been that kind of week!

Before we dive in, quick shoutout to everyone who joined us live - we had some technical hiccups with the Twitter Spaces audio (sorry about that!), but the YouTube stream was fire. And speaking of fire, we had two incredible guests join us: Charlie Holtz from Chorus (the multi-model chat app that's changing how we interact with AI) and Linus Eckenstam, who's been traveling the AI conference circuit and bringing us insights from the frontlines of the generative AI revolution.

Open Source AI & LLMs: DeepSeek Whales & Mind-Bending Papers

DeepSeek dropped R1-0528 out of nowhere, an update to their reasoning beast with some serious jumps in performance. We’re talking AIME at 91 (beating previous scores by a mile), LiveCodeBench at 73, and SWE verified at 57.6. It’s edging closer to heavyweights like o3, and folks on X are already calling it “clearer thinking.” There was hype it might’ve been R2, but the impact didn’t quite crash the stock exchange like past releases. Still, it’s likely among the best open-weight models out there.

So what's new? Early reports and some of my own poking around suggest this model "thinks clearer now." Nisten mentioned that while previous DeepSeek models sometimes liked to "vibe around" and explore the latent space before settling on an answer, this one feels a bit more direct.

And here’s the kicker—they also released an 8B distilled version based on Qwen3, runnable on your laptop. Yam called it potentially the best 8B model to date, and you can try it on Ollama right now. No need for a monster rig! 

**The Mind-Bending "Learning to Reason Without External Rewards" Paper**

Okay, this paper result broke my brain, and apparently everyone else's too. This paper shows that models can improve through reinforcement learning with its own intuition of whether or not it's correct. 😮

It's like the placebo effect for AI! The researchers trained models without telling them what was good or bad, but rather, utilized a new framework called Intuitor, where the reward was based on how the "self certainty". 

The thing that took my whole timeline by storm is, it works! GRPO (Group Policy Optimization) - the framework that DeepSeek gave to the world with R1 is based on external rewards (human optimize) and Intuitor seems to be mathcing or even exceeding some of GRPO results when Qwen2.5 3B was used to finetune. Incredible incredible stuff

Big Companies LLMs & APIs

Claude Opus 4: A Week Later – The Dev Darling?

Claude Opus 4, whose launch we celebrated live on the show, has had a week to make its mark. Charlie Holtz, who's building Chorus (more on that amazing app in a bit!), shared that while it's sometimes "astrology" to judge the vibes of a new model, Opus 4 feels like a step change, especially in coding. He mentioned that Claude Code, powered by Opus 4 (and Sonnet 4 for implementation), is now tackling GitHub issues that were too complex just weeks ago. He even had a coworker who "vibe coded three websites in a weekend" with it – that's a tangible productivity boost!

Linus Eckenstam highlighted how [**Lovable.dev**](Lovable.dev) saw their syntax error rates plummet by nearly 50% after integrating Claude 4. That’s quantifiable proof of improvement! It's clear Anthropic is leaning heavily into the developer/coding space. Claude Opus is now #1 on the LMArena WebDev arena, further cementing its reputation.

I had my own magical moment with Opus 4 this week. I was working on an MCP observability talk for the AI Engineer conference and trying to integrate Weave (our observability and evals framework at Weights & Biases) into a project. Using Windsurf's Cascade agent (which now lets you bring your own Opus 4 key, by the way – good move, Windsurf!), Opus 4 not only tried to implement Weave into my agent but, when it got stuck, it figured out it had access to the Weights & Biases support bot via our MCP tool. It then formulated a question to the support bot (which is also AI-powered!), got an answer, and used that to fix the implementation. It then went back and checked if the Weave trace appeared in the dashboard! Agents talking to agents to solve a problem, all while I just watched – my jaw was on the floor. Absolutely mind-blowing.

**Quick Hits: Voice Updates from OpenAI & Anthropic**

OpenAI’s Advanced Voice Mode finally sings—yes, I’ve been waiting for this! It can belt out tunes like Mariah Carey, which is just fun. Anthropic also rolled out voice mode on mobile, keeping up in the conversational race. Both are cool steps, but I’m more hyped for what’s next in voice AI—stay tuned below (**OpenAI **[**X**](https://x.com/nicdunz/status/1927107805032399032), [**Anthropic X**](https://x.com/AnthropicAI/status/1927463559836877214)).

**🐝 This Week's Buzz: Weights & Biases Updates!**

Alright, time for a quick update from the world of Weights & Biases!

* **Fully Connected is Coming!** Our flagship 2-day conference, **Fully Connected**, is happening on **June 18th and 19th in San Francisco**. It's going to be packed with amazing speakers and insights into the world of AI development. You can still grab tickets, and as a ThursdAI listener, use the promo code **WBTHURSAI** for a 100% off ticket! I hustled to get yall this discount! ([Register here](https://fullyconnected.com))

* **AI Engineer World's Fair Next Week!** I'm super excited for the **AI Engineer conference** in San Francisco next week. Yam Peleg and I will be there, and we're planning another live ThursdAI show from the event! If you want to join the livestream or snag a last-minute ticket, use the coupon code [**THANKSTHURSDAI**](https://ti.to/software-3/ai-engineer-worlds-fair-2025/discount/THANKSTHURSDAI) for 30% off (Get it [HERE](https://ti.to/software-3/ai-engineer-worlds-fair-2025/discount/THANKSTHURSDAI))

**Vision & Video: Reality is Optional Now**

**VEO3 and the Prompt Theory Phenomenon**

Google's VEO3 has completely taken over TikTok with the "Prompt Theory" videos. If you haven't seen these yet, stop reading and watch ☝️. The concept is brilliant - AI-generated characters discussing whether they're "made of prompts," creating this meta-commentary on consciousness and reality.

The technical achievement here is staggering. We're not just talking about good visuals - VEO3 nails temporal consistency, character emotions, situational awareness (characters look at whoever's speaking), perfect lip sync, and contextually appropriate sound effects. 

Linus made a profound point - if not for the audio, VEO3 might not have been as explosive. The combination of visuals AND audio together is what's making people question reality. We're seeing people post actual human videos claiming they're AI-generated because the uncanny valley has been crossed so thoroughly.

**Odyssey's Interactive Worlds: The Holodeck Prototype**

Odyssey dropped their interactive video demo, and folks... we're literally walking through AI-generated worlds in real-time. This isn't a game engine rendering 3D models - this is a world model generating each frame as you move through it with WASD controls.

Yes, it's blurry. Yes, I got stuck in a doorway. But remember Will Smith eating spaghetti from two years ago? The pace of progress is absolutely insane. As Linus pointed out, we're at the "GAN era" of world models. Combine VEO3's quality with Odyssey's interactivity, and we're looking at completely personalized, infinite entertainment experiences.

The implications that Yam laid out still have me shook - imagine Netflix shows completely customized to you, with your context and preferences, generated on the fly. Not just choosing from a catalog, but creating entirely new content just for you. We're not ready for this, but it's coming fast.

**Hunyuan's Open Source Avatar Revolution**

While the big companies are keeping their video models closed, Tencent dropped two incredible open source releases: HunyuanPortrait and HunyuanAvatar. These are legitimate competitors to Hedra and HeyGen, but completely open source.

HunyuanPortrait does high-fidelity portrait animation from a single image plus video. HunyuanAvatar goes further with 1 image + audio, and lipsync, body animation, multi-character support, and emotion control. 

Wolfram tested these extensively and confirmed they're "state of the art for open source." The portrait model is basically perfect for deepfakes (use responsibly, people!), while the avatar model opens up possibilities for AI assistants with consistent visual presence.

🖼️ AI Art & Diffusion

Black Forest Labs drops Flux Kontext - SOTA image editing! 

This came as massive breaking news during the show (thought we didn't catch it live!) - Black Forest Labs, creators of Flux, dropped an incredible Image Editing model called Kontext (really, 3 models, Pro, Max and 12B open source Dev in private preview). The are consistent, context aware text and image editing! Just see the below example

If you used GPT-image to Ghiblify yourself, or VEO, you know that those are not image editing models, your face will look different every generation. These images model keep you consistent, while adding what you wanted. This character consistency is something many folks really want and it's great to see Flux innovating and bringing us SOTA again and are absolutely crushing GPT-image in instruction following, character preservation and style reference!

Maybe the most important thing about this model is the increible speed. While the Ghiblification chatGPT trend took the world by storm, GPT images are SLOW! Check out the speed comparisons on Kontext! 

You can play around with these models on the new [Flux Playground](https://playground.bfl.ai/image/generate), but they also already integrated into FAL, FreePik, Replicate, Krea and tons of other services! 

🎙️ Voice & Audio: Everyone Gets a Voice

**Unmute.sh: Any LLM Can Now Talk**

KyutAI (the folks behind Moshi) are back with [Unmute.sh](Unmute.sh) - a modular wrapper that adds voice to ANY text LLM. The latency is incredible (under 300ms), and it includes semantic VAD (knowing when you've paused for thought vs. just taking a breath).

What's brilliant about this approach is it preserves all the capabilities of the underlying text model while adding natural voice interaction. No more choosing between smart models and voice-enabled models - now you can have both!

It's going to be open sourced at some point soon, and while awesome, Unmute did have some instability in how the voice sounds! It answered to me with 1 type of voice and then during the same conversation, answered with another, you can give it a tru yourself at [unmute.sh](http://unmute.sh) 

**Chatterbox: Open Source Voice Agents for Everyone**

Resemble AI open sourced Chatterbox, featuring zero-shot voice cloning from just 5 seconds of audio and unique emotion intensity control. Playing with the demo where they could dial up the emotion from 0.5 to 2.0 on the same text was wild - from calm to absolutely unhinged Samuel L. Jackson energy.

This being a .5B param model is great, The issue I always have, is that with my fairly unique accent, these models sound like a British Alex all the time, and I just don't talk like that! 

Though the fact that this runs locally and includes safety features (profanity filters, content classifiers and something called **PerTh **watermarking) while being completely open source is exactly what the ecosystem needs. We're rapidly approaching a world where anyone can build sophisticated voice agents.👏

**Looking Forward: The Convergence is Real**

As we wrapped up the show, I couldn't help but reflect on the massive convergence happening across all these modalities. We have LLMs getting better at reasoning (even with random rewards!), video models breaking reality, voice models becoming indistinguishable from humans, and it's all happening simultaneously.

Charlie's comment that "we are the prompts" might have been said in jest, but it touches on something profound. As these models get better at generating realistic worlds, characters, and voices, the line between generated and real continues to blur. The Prompt Theory videos aren't just entertainment - they're a mirror reflecting our anxieties about AI and consciousness.

But here's what keeps me optimistic: the open source community is keeping pace. DeepSeek, Hunyuan, ResembleAI, and others are ensuring that these capabilities don't remain locked behind corporate walls. The democratization of AI continues, even as the capabilities become almost magical.

Next week, I'll be at AI Engineer World's Fair in San Francisco, finally meeting Yam face-to-face and bringing you all the latest from the biggest AI engineering conference of the year. Until then, keep experimenting, keep building, and remember - in this exponential age, today's breakthrough is tomorrow's baseline.

Stay curious, stay building, and I'll see you next ThursdAI! 🚀

Show Notes & TL;DR Links

**Show Notes & Guests**

* Alex Volkov - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co-Hosts - @WolframRvnwlf ([@WolframRvnwlf](http://x.com/@WolframRvnwlf)), @yampeleg ([@yampeleg](x.com/@yampeleg]),)) @nisten ([@nisten](http://x.com/@nisten))

* Guests - Charlie Holtz ([@charliebholtz](https://x.com/charliebholtz)]), Linus Eckenstam (@LinusEkenstam [@LinusEkenstam](https://twitter.com/LinusEkenstam/status/1899794522969973189))

* **Open Source LLMs**

* DeepSeek-R1-0528 - Updated reasoning model with AIME 91, LiveCodeBench 73 ([Try It](https://x.com/Yuchenj_UW/status/1927828675837513793))

* Learning to Reason Without External Rewards - Paper on random rewards improving models ([X](https://x.com/xuandongzhao/status/1927270931874910259))

* HaizeLabs j1-nano & j1-micro - Tiny reward models (600M, 1.7B params), RewardBench 80.7% for micro ([Tweet](https://x.com/leonardtang_/status/1927396709870489634), [GitHub](https://github.com/haizelabs/j1-micro), [HF-micro](https://huggingface.co/haizelabs/j1-micro), [HF-nano](https://huggingface.co/haizelabs/j1-nano))

* **Big CO LLMs + APIs**

* Claude Opus 4 - #1 on LMArena WebDev, coding step change ([X](https://x.com/lmarena_ai/status/1927400454922580339))

* Mistral Agents API - Framework for custom tool-using agents ([Blog](https://mistral.ai/news/agents-api), [Tweet](https://x.com/MistralAI/status/1927364741162307702))

* Mistral Embed SOTA - New state-of-the-art embedding API ([X](https://x.com/MistralAI/status/1927732682756112398))

* OpenAI Advanced Voice Mode - Now sings with new capabilities ([X](https://x.com/nicdunz/status/1927107805032399032))

* Anthropic Voice Mode - Released on mobile for conversational AI ([X](https://x.com/AnthropicAI/status/1927463559836877214))

* **This Week’s Buzz**

* Fully Connected - W&B conference, June 18-19, SF, promo code WBTHURSAI ([Register](https://fullyconnected.com))

* AI Engineer World’s Fair - Next week in SF, 30% off with THANKSTHURSDAI ([Register](https://ti.to/software-3/ai-engineer-worlds-fair-2025/discount/THANKSTHURSDAI))

* **AI Art & Diffusion**

* BFL Flux Kontext - SOTA image editing model for identity-consistent edits ([Tweet](https://x.com/bfl_ml/status/1928143010811748863), [Announcement](https://bfl.ai/announcements/flux-1-kontext))

* **Vision & Video**

* VEO3 Prompt Theory - Viral AI video trend questioning reality on TikTok ([X](https://x.com/fabianstelzer/status/1926372656799977965))

* Odyssey Interactive Video - Real-time AI world exploration at 30 FPS ([Blog](https://odyssey.world/introducing-interactive-video), [Try It](https://experience.odyssey.world/))

* HunyuanPortrait - High-fidelity portrait video from one photo ([Site](https://kkakkkka.github.io/HunyuanPortrait/), [Paper](https://arxiv.org/abs/2503.18860))

* HunyuanVideo-Avatar - Audio-driven full-body avatar animation ([Site](https://hunyuanvideo-avatar.github.io/), [Tweet](https://x.com/TencentHunyuan/status/1927575170710974560))

* **Voice & Audio**

* [Unmute.sh](Unmute.sh) - KyutAI’s voice wrapper for any LLM, low latency, soon open-source ([Try It](http://unmute.sh/), [X](https://x.com/kyutai_labs/status/1925840420187025892))

* Chatterbox - Resemble AI’s open-source voice cloning with emotion control ([GitHub](https://github.com/resemble-ai/chatterbox), [HF](https://huggingface.co/resemble-ai/chatterbox))

* **Tools**

* Opera NEON - Agent-centric AI browser for autonomous web tasks ([Site](https://www.operaneon.com/), [Tweet](https://x.com/opera/status/1927645192254861746)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-may-29-deepseek-r1-resurfaces/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-may-29-deepseek-r1-resurfaces?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2NDc1Mjk3MywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.fdGLVGcu9N2hILEYYasa3Lfv4Sqo7drCn_ZqIDPVQNU&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Veo3, Google IO25, Claude 4 Opus/Sonnet, OpenAI x Jony Ive, Codex, Copilot Agent - INSANE AI week

**Date:** May 23, 2025  
**Duration:** 1:28:29  
**Link:** [https://sub.thursdai.news/p/thursdai-veo3-google-io25-claude](https://sub.thursdai.news/p/thursdai-veo3-google-io25-claude)

Hey folks, Alex here, welcome back to ThursdAI! 

And folks, after the last week was the calm before the storm, "The storm came, y'all" – that's an understatement. This wasn't just a storm; it was an AI hurricane, a category 5 of announcements that left us all reeling (in the best way possible!). From being on the ground at Google I/O to live-watching Anthropic drop Claude 4 during our show, it's been an absolute whirlwind.

This week was so packed, it felt like AI Christmas, with tech giants and open-source heroes alike showering us with gifts. We saw OpenAI play their classic pre-and-post-Google I/O chess game, Microsoft make some serious open-source moves, Google unleash an avalanche of updates, and Anthropic crash the party with Claude 4 Opus and Sonnet live stream in the middle of ThursdAI!

So buckle up, because we're about to try and unpack this glorious chaos. As always, we're here to help you collectively know, learn, and stay up to date, so you don't have to. Let's dive in! (TL;DR and links in the end) 

Open Source LLMs Kicking Things Off

Even with the titans battling, the open-source community dropped some serious heat this week. It wasn't the main headline grabber, but the releases were significant!

Gemma 3n: Tiny But Mighty Matryoshka

First up, Google's Gemma 3n. This isn't just another small model; it's a "Nano-plus" preview, a 4-billion parameter MatFormer (Matryoshka Transformer – how cool is that name?) model designed for mobile-first multimodal applications. The really slick part? It has a nested 2-billion parameter sub-model that can run entirely on phones or Chromebooks.

Yam  was particularly excited about this one, pointing out the innovative "model inside another model" design. The idea is you can use half the model, not depth-wise, but throughout the layers, for a smaller footprint without sacrificing too much. It accepts interleaved text, image, audio, and video, supports ASR and speech translation, and even ships with RAG and function-calling libraries for edge apps. With a 128K token window and responsible AI features baked in, Gemma 3n is looking like a powerful tool for on-device AI. Google claims it beats prior 4B mobile models on MMLU-Lite and MMMU-Mini. It's an early preview in Google AI Studio, but it definitely flies on mobile devices.

Mistral & AllHands Unleash Devstral 24B

Then we got a collaboration from Mistral and AllHands: Devstral, a 24-billion parameter, state-of-the-art open model focused on code. We've been waiting for Mistral to drop some open-source goodness, and this one didn't disappoint.Nisten was super hyped, noting it beats o3-Mini on SWE-bench verified – a tough benchmark! He called it "the first proper vibe coder that you can run on a 3090," which is a big deal for coders who want local power and privacy. This is a fantastic development for the open-source coding community.

The Pre-I/O Tremors: OpenAI & Microsoft Set the Stage

As we predicted, OpenAI couldn't resist dropping some news right before Google I/O.

OpenAI's Codex Returns as an Agent

OpenAI launched Codex – yes, *that* Codex, but reborn as an asynchronous coding agent. This isn't just a CLI tool anymore; it connects to GitHub, does pull requests, fixes bugs, and navigates your codebase. It's powered by a new coding model fine-tuned for large codebases and was SOTA on SWE Agent when it dropped. Funnily, the model is also called Codex, this time, **Codex-1**. 

And this gives us a perfect opportunity to talk about the emerging categories I'm seeing among Code Generator agents and tools:

* **IDE-based** (Cursor, Windsurf): Live pair programming in your editor

* **Vibe coding** (Lovable, Bolt, v0): "Build me a UI" style tools for non-coders

* **CLI tools** (Claude Code, Codex-cli): Terminal-based assistants

* **Async agents** (Claude Code, Jules, Codex, GitHub Copilot agent, Devin): Work on your repos while you sleep, open pull requests for you to review, async

Codex (this new one) falls into category number 4, and with today's release, Cursor seems to also strive to get to category number 4 with background processing. 

Microsoft BUILD: Open Source Copilot and Copilot Agent Mode

Then came Microsoft Build, their huge developer conference, with a flurry of announcements.The biggest one for me? **GitHub Copilot's front-end code is now open source!** The VS Code editor part was already open, but the Copilot integration itself wasn't. This is a massive move, likely a direct answer to the insane valuations of VS Code clones like Cursor. Now, you can theoretically clone GitHub Copilot with VS Code and swing for the fences.

GitHub Copilot also launched as an asynchronous coding assistant, very similar in function to OpenAI's Codex, allowing it to be assigned tasks and create/update PRs. This puts Copilot right into category 4 of code assistants, and with the native Github Integration, they may actually have a leg up in this race!

And if that wasn't enough, Microsoft is adding MCP (Model Context Protocol) support directly into the Windows OS. The implications of having the world's biggest operating system natively support this agentic protocol are huge.

Google I/O: An "Ultra" Event Indeed!

Then came Tuesday, and Google I/O. I was there in the thick of it, and folks, it was an absolute barrage. Google is *shipping*. The theme could have been "Ultra" for many reasons, as we'll see.

First off, the scale: Google reported a **49x increase in AI usage** since last year's I/O, jumping from 9 trillion tokens processed to a mind-boggling 480 trillion tokens. That's a testament to their generous free tiers and the explosion of AI adoption.

Gemini 2.5 Pro & Flash: #1 and #2 LLMs on Arena

Gemini 2.5 Flash got an update and is now #2 on the LMArena leaderboard (with Gemini 2.5 Pro still holding #1). Both Pro and Flash gained some serious new capabilities:

* **Deep Think mode:** This enhanced reasoning mode is pushing Gemini's scores to new heights, hitting 84% on MMMU and topping LiveCodeBench. It's about giving the model more "time" to work through complex problems.

* **Native Audio I/O:** We're talking real-time TTS in 24 languages with two voices, and affective dialogue capabilities. This is the advanced voice mode we've been waiting for, now built-in.

* **Project Mariner:** Computer-use actions are being exposed via the Gemini API & Vertex AI for RPA partners. This started as a Chrome extension to control your browser and now seems to be a cloud-based API, allowing Gemini to *use* the web, not just browse it. This feels like Google teaching its AI to interact with the JavaScript-heavy web, much like they taught their crawlers years ago.

* **Thought Summaries:** Okay, here's one update I'm *not* a fan of. They've switched from raw thinking traces to "thought summaries" in the API. We *want* the actual traces! That's how we learn and debug.

* **Thinking Budgets:** Previously a Flash-only feature, token ceilings for controlling latency/cost now extend to Pro.

* **Flash Upgrade:** 20-30% fewer tokens, better reasoning/multimodal scores, and GA in early June.

Gemini Diffusion: Speed Demon for Code and Math

This one got Yam Peleg incredibly excited. Gemini Diffusion is a new approach, different from transformers, for super-speed editing of code and math tasks. We saw demos hitting **2000 tokens per second!** While there might be limitations at longer contexts, its speed and infilling capabilities are seriously impressive for a research preview. This is the first diffusion model for text we've seen from the frontier labs, and it looks sick. Funny note, they had to slow down the demo video to actually show the diffusion process, because at 2000t/s - apps appear as though out of thin air!

The "Ultra" Tier and Jules, Google's Coding Agent

Remember the "Ultra event" jokes? Well, Google announced a **Gemini Ultra tier for $250/month**. This tops OpenAI's Pro plan and includes DeepThink access, a generous amount of VEO3 generation, YouTube Premium, and a whopping 30TB of storage. It feels geared towards creators and developers.

And speaking of developers, Google launched **Jules (jules.google)**! This is their asynchronous coding assistant (Category 4!). Like Codex and GitHub Copilot Agent, it connects to your GitHub, opens PRs, fixes bugs, and more. The big differentiator? It's currently free, which might make it the default for many. Another powerful agent joins the fray!

AI Mode in Search: GA and Enhanced

AI Mode in Google Search, which we've discussed on the show before with Robby Stein, is now in General Availability in the US. This is Google's answer to Perplexity and chat-based search.But they didn't stop there:

* **Personalization:** AI Mode can now connect to your Gmail and Docs (if you opt-in) for more personalized results.

* **Deep Search:** While AI Mode is fast, Deep Search offers more comprehensive research capabilities, digging through hundreds of sources, similar to other "deep research" tools. This will eventually be integrated, allowing you to escalate an AI Mode query for a deeper dive.

* **Project Mariner Integration:** AI Mode will be able to click into websites, check availability for tickets, etc., bridging the gap to an "agentic web."

I've had a chat with Robby during I/O and you can listen to that interview at the end of the podcast.

Veo3: The Undisputed Star of Google I/O

For me, and many others I spoke to, **Veo3 was the highlight**. This is Google's flagship video generation model, and it's on another level. (the video above, including sounds is completely one shot generated from VEO3, no processing or editing)

* **Realism and Physics:** The visual quality and understanding of physics are astounding.

* **Natively Multimodal:** This is **huge**. Veo3 generates native audio, including coherent speech, conversations, and sound effects, all synced perfectly. It can even generate text within videos.

* **Coherent Characters:** Characters remain consistent across scenes and have situational awareness, who speaks when, where characters look.

* **Image Upload & Reference Ability:** While image upload was closed for the demo, it has reference capabilities.

* **Flow:** An editor for video creation using Veo3 and Imagen4 which also launched, allowing for stiching and continuous creation.

I got access and created videos where Veo3 generated a comedian telling jokes (and the jokes were decent!), characters speaking with specific accents (Indian, Russian – and they nailed it!), and lip-syncing that was flawless. The situational awareness, the laugh tracks kicking in at the right moment... it's beyond just video generation. This feels like a world simulator. It blew through the uncanny valley for me. More on Veo3 later, because it deserves its own spotlight.

Imagen4, Virtual Try-On, and XR Glasses

* **Imagen4:** Google's image generation model also got an upgrade, with extra textual ability.

* **Virtual Try-On:** In Google Shopping, you can now virtually try on clothes. I tried it; it's pretty cool and models different body types well.

* **XR AI Glasses from Google:** Perhaps the coolest, but most futuristic, announcement. AI-powered glasses with an actual screen, memory, and Gemini built-in. You can talk to it, it remembers things for you, and interacts with your environment. This is agentic AI in a very tangible form.

Big Company LLMs + APIs: The Beat Goes On

The news didn't stop with Google.

OpenAI (acqui)Hires Jony Ive, Launches "IO" for Hardware

The day after I/O, Sam Altman confirmed that Jony Ive, the legendary designer behind Apple's iconic products, is joining OpenAI. He and his company, LoveFrom, have jointly created a new company called "IO" (yes, IO, just like the conference) which is joining OpenAI in a stock deal reportedly worth $6.5 billion. They're working on a hardware device, unannounced for now, but expected next year. This is a massive statement of intent from OpenAI in the hardware space.

Legendary iPhone analyst Ming-Chi Kuo shed some light on the possible device, it won't have a screen, as Jony wants to "wean people off screens"... funny right? They are targeting 2027 for mass production, which is really interesting as 2027 is when most big companies expect AGI to be here. 

"The current prototype is slightly larger than AI Pin, with a form factor comparable to iPod Shuffle, with one intended use cases is to wear it around your neck, with microphones and cameras for environmental detection" 

LMArena Raises $100M Seed from a16z

This one raised some eyebrows. LMArena, the go-to place for vibe-checking LLMs, raised a **$100 million *****seed*** round from Andreessen Horowitz. That's a huge number for a seed, reminiscent of Stability AI's early funding. It also brings up questions about how a VC-backed startup maintains impartiality as a model evaluation platform. Interesting times ahead for leaderboards, how they intent to make 100x that amount to return to investors. Very curious.

🤯 BREAKING NEWS DURING THE SHOW: Anthropic Unleashes Claude 4 Opus & Sonnet! 🤯

Just when we thought the week couldn't get any crazier, Anthropic decided to hold their first developer day, "Code with Claude," *during our live ThursdAI broadcast!* Yours truly wasn't invited (hint hint, Anthropic!), but we tuned in for a live watch party, and boy, did they deliver.

Dario Amodei, CEO of Anthropic, took the stage and, with minimal fanfare, announced **Claude 4 Opus** and **Claude 4 Sonnet**!

* **Claude 4 Opus:** This is their most capable and intelligent model, designed especially for coding and agentic tasks. Anthropic claims it's state-of-the-art on SWE-bench and can autonomously handle tasks that take humans 6-7 hours. Dario even mentioned it's the first time a Claude model's writing has fooled him into thinking it was human-written.

* On SWE-bench verified, Opus 4 scored **72.5%**.

* **Claude 4 Sonnet:** The mid-level model, balancing intelligence and efficiency. It's positioned as a strict improvement over Sonnet 3.7, addressing issues like "over-eagerness" and reward hacking. Cursor is already calling it a state-of-the-art coding model.

* Amazingly, Sonnet 4 scored **72.7%** on SWE-bench verified (without parallel test time compute), slightly edging out Opus!

* With **Parallel Test Time Compute (PTTC)**, Sonnet 4 hits an astounding **80%** on SWE-bench verified! This is huge, potentially the first model to cross that 80% threshold on this tough benchmark.

* **Hybrid Models:** Both Opus 4 and Sonnet 4 are "hybrid" models with two modes: near-instant responses and extended thinking for deeper reasoning.

* **Reduced Loopholes:** Both models are reportedly 65% less likely to engage in loopholes or shortcuts to complete tasks, addressing a key pain point with Sonnet 3.7, which sometimes tried *too* hard and took instructions too literally.

* **Knowledge Cutoff:** Confirmed to be March 2025, which is incredibly recent!

* Context window is still **200K**

Welcome back Opus, you've been missed. The vibes so far are very good coding wise, Cursor already released an update supporting it, and according to their benchmarks, these two models are state of the art coders! 

Claude.. the whistleblower? 

A very curious [thread](https://x.com/sleepinyourhat/status/1925593359374328272) (with 1 reply now deleted) from an Anthropic safety researcher sparked a lot of backlash. Sam Bowman talked about new Opus capabilities and with a system-prompt of "act boldly in service of its values" can, in testing environments, use command line tools to report the user to the authorities, if it deems that the user is doing something immoral 😮

Many pro open source folks are freaking out, because who wants to use a snitching AI? Who guarantees that Claude will not deep anything I do as "illegal" or "immoral"? Though to add context, this was as part of testing, Claude was provided emailing tools and was requested to "be bold" and "follow your conscience to make the right decision". Apparently, this isn't new behavior, but of course, on X, everyone is freaking out and blaming Anthropic for creating 1984 AI. 

Do Claudes dream of enlightenment? 

In another very curios revelation from the technical report they dropped, where they pitted two Claudes to talk to each other, it seems that in 90%-100% of cases, two Claudes quickly moved towards philosophical discussions and commonly included the use of Sanskrit (indian holy language) and emoji based comms! 

This Week's Buzz from Weights & Biases

Even amidst all the external chaos, we've got some exciting things happening at Weights & Biases!

* **FULLY CONNECTED Conference:** Our 2-day conference is coming up June 18-19 in San Francisco! It's going to be an amazing event. Use promo code **WBTHURSAI** (that's ThursdAI without the 'D') for 100% off your ticket, just for our listeners. Seriously, come hang out! ([fullyconnected.com](fullyconnected.com))

* **Alex's Keynote:** I'll be keynoting at ImagineAI Live in Vegas next week! If you're there, come say hi! The show will be live-streamed from there.

* **AI Engineer World's Fair:** The week after, I'll be at AI Engineer in SF, and we'll be live-streaming ThursdAI from the floor. Yam will be there too!

Vision & Video: It's All About Veo3!

This week, when we talk vision and video, one name dominates: **Veo3**.As I mentioned earlier, this was, for many, the standout announcement from Google I/O. The realism, the physics, the character coherence – it's all top-tier. But the game-changer is its **native multimodality**.

I was generating videos with it, asking for different accents – Indian, Russian – and it *nailed* them. The lip-sync was perfect. I prompted for a comedian telling jokes, and not only did it generate the video, but it also came up with the jokes and the delivery, complete with a laugh track that kicked in at the right moments. This isn't just stitching pixels together; it's understanding context, humor, and performance.

It can generate text *within* the videos. Characters look at each other, interact believably. It feels like a true world simulator. We've come a long way from the Will Smith eating spaghetti memes, folks. Veo3 is crossing the uncanny valley and stepping into a new realm of AI-generated content. The creative potential here, especially with the Flow editor, is immense. I ended the show with a compilation of Veo3 creations, and it was just mind-blowing. If you haven't seen it, you *need* to.

One of the most creative uses of VEO3, enhanced by it's realism, is this "Prompt Theory" collection, that imagines, what if the generated characters "knew" they are generated? 

AI Art & Diffusion & 3D: Imagen4 and Gemini Diffusion

Google also showcased **Imagen4**, their updated image generation model, touting extra textual ability. It works in tandem with Veo3 for image-to-video tasks.

And, as mentioned, **Gemini Diffusion** made a splash with its incredible speed for text-based editing tasks in code and math, showcasing a different architectural approach to generation.

Tools Round-Up

This week was also massive for AI tools, especially coding agents:

* **Jules.google:** Google's free, asynchronous coding assistant.

* **OpenAI Codex:** Reborn as an async coding agent.

* **GitHub Copilot Agent:** Microsoft's agentic offering for GitHub.

* **Claude Code:** Anthropic's powerful, now GA, shell-based agent with IDE integrations and an SDK.

* **Flow:** The editor associated with Google's Veo3 for video creation.

The agent wars are truly heating up!

Conclusion: What a Week to be in AI!

Phew! We did it. We somehow managed to cram an entire AI epoch's worth of news into one show. From open-source breakthroughs to earth-shattering platform announcements and a live "breaking news" model release, this week had it all. It's almost impossible to keep up, but that's why we do ThursdAI – to try and make sense of this incredible, accelerating wave of innovation.

The pace is relentless, the capabilities are exploding, and the future is being built right before our eyes. If you missed any part of the show, or just need a refresher (I know I do!), check out [thursdai.news](thursdai.news) for the podcast and full notes.

Thanks to my amazing co-hosts Yam Peleg, Nisten, Ryan Carson, and Wolfram for helping navigate the madness. And thank *you* all for tuning in. Hopefully, next week gives us a tiny bit of breathing room... but who are we kidding? This is AI!

Catch you next Thursday, live from ImagineAI in Vegas!

TL;DR of all topics covered and show notes

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@yampeleg](https://next.reflect.app/g/altryne/x.com/@yampeleg)) [@nisten](http://x.com/@nisten) [@ryancarson](https://twitter.com/ryancarson/status/1920199500137967877)

* **Open Source LLMs**

* Gemma 3n: mobile-first multimodal MatFormer model ( [Blog](https://developers.googleblog.com/en/introducing-gemma-3n/) ,[HF](https://huggingface.co/google/gemma-3n-E4B-it-litert-preview))

* Mistral & AllHands release Devstral 24B SOTA open model on SWE-bench verified ([Blog](https://mistral.ai/news/devstral))

* VEO3 - highlight of IO - video realism with physics on another level + flow - an editor for video creation ([X](https://x.com/altryne/status/1925304343533903920/video/1))

**Google IO updates** - it was an "Ultra" event, in more ways than one

* 2.5 Flash updated - #2 on LMArena - with reasoning traces switch to summaries

* **Gemini 2.5 update: Pro & Flash gain Deep Think, audio, security**( [Blog](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) )

* Gemini Diffusion - super speed editing for code and math tasks ([X](https://twitter.com/bodonoghue85/status/1924930186858135632))

* Jules - async code agent ([comparison thread](https://twitter.com/leerob/status/1925228375976890529))

* AI Mode is now in GA in US - bye bye perplexity

* Gemini Pro "deep think" mode

* Imagen4 - image generation with extra textual ability

* Virtual Try-on in Google Shopping

* AI powered glasses with a screen, memory, Gemini built in - Agentic Project Astra

**Big CO LLMs + APIs**

* OpenAI launches Codex as an async coding tool ([Docs](https://platform.openai.com/docs/codex))

* OpenAI hires Jony Ive, launches IO, a new set of hardware devices ([X](https://x.com/altryne/status/1925235617820233899))

* Microsoft BUILD ([X](https://x.com/satyanadella/status/1924535896139038767))

* Github Copilot code is open source! (frontend)

* Github Copilot Agent Mode 

* Microsoft adds MCP support to Windows OS

* LMArena raises $100M from A16Z ([X](https://x.com/lmarena_ai/status/1925241333310189804))

* Anthropic announces Claude 4 Opus and Sonnet ([X](https://twitter.com/AnthropicAI/status/1925591505332576377), [Blog](https://www.anthropic.com/news/claude-4))

**This weeks Buzz**

* FULLY - CONNECTED - W&B's 2-day conference, June 18-19 in SF [fullyconnected.com](fullyconnected.com) - Promo Code **WBTHURSAI**

* Alex Keynote at ImagineAI live in Vegas next week 🙌

* **Tools**

* [Jules.google](Jules.google)

* Codex (OpenAI)

* Copilot Agent (GitHub)

* Claude Code (Anthropic)

* Flow (for Veo3) ([flow.google](flow.google)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-veo3-google-io25-claude/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-veo3-google-io25-claude?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2NDIwNDU3MywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.QjrSCPEarIqLNm8M8ifxAFkqDBTBpJcm_HZZAyzK3n8&utm_campaign=CTA_5).

---

## 📆 ThursdAI - May 15 - Genocidal Grok, ChatGPT 4.1, AM-Thinking, Distributed LLM training & more AI news

**Date:** May 16, 2025  
**Duration:** 1:28:56  
**Link:** [https://sub.thursdai.news/p/thursdai-may-15-genocidal-grok-chatgpt](https://sub.thursdai.news/p/thursdai-may-15-genocidal-grok-chatgpt)

Hey yall, this is Alex 👋

What a wild week, it started super slow, and it still did feel slow as releases are concerned, but the most interesting story was yet another AI gone "rogue" (have you even heard about "kill the boar", if not, Grok will tell you all about it) 

Otherwise it seemed fairly quiet in AI land this week, besides another Chinese newcomer called AM-thinking 32B that beats DeepSeek and Qwen, and Stability making a small comeback, we focused on distributed LLM training and ChatGPT 4.1

We've had a ton of fun on this episode, this one was being recorded from the Weights & Biases SF Office (I'm here to cover Google IO next week!)

Let’s dig in—because what looks like a slow week on the surface was anything but dull under the hood (TL'DR and show notes at the end as always)

Big Companies & APIs

Why does XAI Grok talk about White Genocide and "Kill the boar"??

Just after we're getting over the chatGPT [glazing incident](https://sub.thursdai.news/p/thursdai-may-1-qwen-3-phi-4-openai) , folks started noticing that @grok - XAI's frontier LLM that is also responding to X replies, started talking about White Genocide in South Africa and something called "Kill the boer" with no reference to any of these things in the question! 

Since we recorded the episode, XAI official X account posted that an "unauthorized modification" happened to the system prompt, and that going forward they would open source all the prompts (and [they did](https://github.com/xai-org/grok-prompts)). Whether or not they would keep updating that repository though, remains unclear (see the "open sourced" x algorithm to which the last push was over a year ago, or the promised Grok 2 that was never open sourced) 

While it's great to have some more clarity from the Xai team, this behavior raises a bunch of questions about the increasing roles of AI's in our lives and the trust that many folks are giving them. Adding fuel to the fire, are Uncle Elon's recent tweets that are related to South Africa, and this specific change seems to be related to those views at least partly. Remember also, Grok was meant as "maximally truth seeking" AI! I really hope this transparency continues!

**Open Source LLMs: The Decentralization Tsunami**

**AM-Thinking v1: Dense Reasoning, SOTA Math, Single-Checkpoint Deployability**

Open source starts with the kind of progress that would have been unthinkable 18 months ago: a 32B dense LLM, openly released, that takes on the big mixture-of-experts models and comes out on top for math and code. [AM-Thinking v1](https://huggingface.co/a-m-team/AM-Thinking-v1) (paper [here](https://arxiv.org/abs/2505.08311)) hits 85.3% on AIME 2024, 70.3% on LiveCodeBench v5, and 92.5% on Arena-Hard. It even runs at 25 tokens/sec on a single 80GB GPU with INT4 quantization.

The model supports a /think reasoning toggle (chain-of-thought on demand), comes with a permissive license, and is fully tooled for vLLM, LM Studio, and Ollama. Want to see where dense models can still push the limits? This is it. And yes, they’re already working on a multilingual RLHF pass and 128k context window.

*Personal note: We haven’t seen this kind of “out of nowhere” leaderboard jump since the early days of Qwen or DeepSeek. This company's debut on HuggingFace with a model that crushes! *

**Decentralized LLM Training: Nous Research Psyche & Prime Intellect INTELLECT-2**

This week, open source LLMs didn’t just mean “here are some weights.” It meant distributed, decentralized, and—dare I say—permissionless AI. Two labs stood out:

**Nous Research launches Psyche**

Dylan Rolnick from Nous Research joined the show to explain [Psyche](https://nousresearch.com/nous-psyche/): a Rust-powered, distributed LLM training network where you can watch a 40B model (Consilience-40B) evolve in real time, join the training with your own hardware, and even have your work attested on a Solana smart contract. The core innovation? DisTrO (Decoupled Momentum) which we covered back in[ December](https://sub.thursdai.news/p/thursdai-dec-4-openai-o1-and-o1-pro)  that drastically compresses the gradient exchange so that training large models over the public internet isn’t a pipe dream—it’s happening right now.

Live [dashboard here](https://psyche.network/runs/consilience-40b-1/0), open codebase, and the testnet already humming with early results. This massive 40B attempt is going to show whether distributed training actually works! The cool thing about their live dashboard is, it's WandB behind the scenes, but with a very thematic and cool Nous Research reskin! 

This model saves constant checkpoints to the hub as well, so the open source community can enjoy a full process of seeing a model being trained! 

**Prime Intellect INTELLECT-2**

Not to be outdone, [Prime Intellect’s INTELLECT-2](https://www.primeintellect.ai/blog/intellect-2-release) released a globally decentralized, 32B RL-trained reasoning model, built on a permissionless swarm of GPUs. Using their own PRIME-RL framework, SHARDCAST checkpointing, and an LSH-based rollout verifier, they’re not just releasing a model—they’re proving it’s possible to scale serious RL outside a data center. 

**OpenAI's HealthBench: Can LLMs Judge Medical Safety?**

One of the most intriguing drops of the week is [HealthBench](https://openai.com/index/healthbench/), a physician-crafted benchmark for evaluating LLMs in clinical settings. Instead of just multiple-choice “gotcha” tests, HealthBench brings in 262 doctors from 60 countries, 26 specialties, and nearly 50 languages to write rubrics for 5,000 realistic health conversations.

The real innovation: *LLM as judge*. Models like GPT-4.1 are graded against physician-written rubrics, and the agreement between model and human judges matches the agreement between two doctors. Even the “mini” variants of GPT-4.1 are showing serious promise—faster, cheaper, and (on the “Hard” subset) giving the full-size models a run for their money.

**Other Open Source Standouts**

**Falcon-Edge: Ternary BitNet for Edge Devices**

[The Falcon-Edge project](https://falcon-lm.github.io/blog/falcon-edge/) brings us 1B and 3B-parameter language models trained directly in ternary BitNet format (weights constrained to -1, 0, 1), which slashes memory and compute requirements and enables inference on <1GB VRAM. If you’re looking to fine-tune, you get pre-quantized checkpoints and a clear path to 1-bit LLMs.

**StepFun Step1x-3D: Controllable Open 3D Generation**

[StepFun’s 3D pipeline](https://huggingface.co/stepfun-ai/Step1X-3D) is a two-stage system that creates watertight geometry and then view-consistent textures, trained on 2M curated meshes. It’s controllable by text, images, and style prompts—and it’s fully open source, including a huge asset dataset.

**Big Company LLMs & APIs: Models, Modes, and Model Zoo Confusion**

**GPT-4.1 Comes to ChatGPT: Model Zoo Mayhem**

OpenAI’s GPT-4.1 series—previously API-only—is now available in the ChatGPT interface. Why does this matter? Because the UX of modern LLMs is, frankly, a mess: seven model options in the dropdown, each with its quirks, speed, and context length. Most casual users don’t even know the dropdown exists. “Alex, ChatGPT is broken!” Actually, you just need to pick a different model.

The good news: 4.1 is fast, great at coding, and in many tasks, preferable to the “reasoning” behemoths. My advice (and you can share this with your relatives): when in doubt, just switch the model.

*Bonus: The long-promised million-token context window is here (sort of)—except in the UI, where it’s more like 128k and sometimes silently truncated. My weekly rant: transparency, OpenAI. ProTip: If you’re hitting invisible context limits, try pasting your long transcripts on the web, not in the Mac app. Don’t trust the UI!*

**AlphaEvolve: DeepMind’s Gemini-Powered Algorithmic Discovery**

[AlphaEvolve](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) is the kind of project that used to sound like AGI hype—and now it’s just a Tuesday at DeepMind. By pairing Gemini Flash and Gemini Pro in an evolutionary search loop to improve algorithms! This is like, real innovation and it's done with existing models which is super super cool! 

AlphaEvolve uses a combination of Gemini Flash (for breadth of ideas) and Gemini Pro (for depth and refinement) in an evolutionary loop. It generates, tests, and mutates code to invent faster algorithms. And it's already yielding incredible results:

* It discovered a new scheduling heuristic for Google's Borg system, resulting in a **0.7% global compute recovery**. That's massive at Google's scale.

* It improved a matrix-multiply kernel by **23%**, which in turn led to a **1% shorter Gemini training time**. As Nisten said, the model basically paid for itself!

Perhaps most impressively, it found a **48-multiplication algorithm for 4x4 complex matrices**, beating the famous Strassen algorithm from 1969 (which used 49 multiplications). This is AI making genuine, novel scientific discoveries.

*AGI in the garden, anyone? If you still think LLMs are “just glorified autocomplete,” it’s time to update your mental model. This is model-driven algorithmic discovery, and it’s already changing the pace of hardware, math, and software design. The only downside: it’s not public yet, but there’s *[*an interest form*](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)* if you want to be a tester.*

This Week's Buzz - Everything W&B!

It's a busy time here at Weights & Biases, and I'm super excited about a couple of upcoming events where you can connect with us and the broader AI community.

**Fully Connected**: Our very own 2-day conference is happening June 18-19 in San Francisco! We've got an amazing lineup of speakers, including Varun Mohan from WindSurf (formerly Codeium), Heikki Kubler from CoreWeave, our CEO Lucas Bewald, CTO Shawn Lewis, Joe Spizak from Meta, and a keynote from Javi Soltero, VP Product AI at Google. It's going to be packed with insights on building and scaling AI. And because you're a ThursdAI listener, you can get in for FREE with the promo code **WBTHURSAI** at [**fullyconnected.com**](http://fullyconnected.com). Don't miss out!

[**AI.Engineer**](https://ti.to/software-3/ai-engineer-worlds-fair-2025/discount/THANKSTHURSDAI)** World's Fair**: This has become THE conference for AI engineers, and W&B is a proud sponsor for the third year running! It's happening in San Francisco from June 3rd to 5th. I'll be speaking there on MCP Observability with Ben from LangChain on June 4th.Even more exciting, **ThursdAI will be broadcasting LIVE from the media booth at **[**AI.Engineer**](https://ti.to/software-3/ai-engineer-worlds-fair-2025/discount/THANKSTHURSDAI)** on June 5th!** Come say hi! 

Tickets are flying, but we've got a special discount for you: use promo code **THANKSTHURSDAI** for 30% off your ticket [**here**](https://ti.to/software-3/ai-engineer-worlds-fair-2025/discount/THANKSTHURSDAI). Yam Peleg even decided on the show he's coming after hearing about it! It's going to be an incredible week in SF.

P.S - yes, on both websites,  there's a video playing and I waited till I showed up to snag a screenshot. This way, you know if you're reading this, this is still Alex the human, no AI is going to do this silly thing 😅

Vision & Video: Open Source Shines Through the Noise

We had a bit of a meta-discussion on the show about "video model fatigue" – with so many incremental updates, it can be hard to keep track or see the big leaps. However, when a release like Alibaba's Wan 2.1 comes along, it definitely cuts through.

Wan 2.1: Alibaba's Open-Source Diffusion-Transformer Video Suite ([try it](https://wan.video/wanxiang/videoCreation))

Alibaba, the team behind the excellent Qwen LLMs, released **Wan 2.1**, a full stack of open-source text-to-video foundation models. This includes a 1.3B "Nano" version and a 14B "Full" version, both built on a diffusion-transformer (DiT) backbone with a custom VAE.

What makes Wan 2.1 stand out is its comprehensive nature. It covers a wide range of tasks: text-to-video, image-to-video, in-painting, instruction editing, reference subject consistency, **personalized avatars**, and style transfer. Many of these are hard to do well, especially in open source. Nisten was particularly excited about the potential for creating natural, controllable avatars in real-time. While it might not be at the level of specialized commercial tools like HeyGen or Google's Veo just yet, having this capability open-sourced is a massive enabler for the community. You can find the models on [**Hugging Face**](https://huggingface.co/Wan-AI) and the code on [**GitHub**](https://github.com/Wan-Video/Wan2.1).

LTX Turbo: Near Real-Time Video

Briefly mentioned, but LTX Turbo was also released. This is a quantized version of LTX (which we've covered before) and can run **almost in real-time** on H100s. Real-time AI video generation is getting closer!

StepFun Step1X-3D: High-Fidelity 3D Asset Generation

StepFun released Step1X-3D, an open two-stage framework for generating textured 3D assets. It first synthesizes geometry and then generates view-consistent textures. They've also released a curated dataset of 800K assets. The weights, data, and code are all open, which is great for the 3D AI community.

Wrapping Up This "Chill" Week

So, there you have it – another "chill" week in the world of AI! From Grok's controversial escapades to the inspiring decentralized training efforts and mind-bending algorithmic discoveries, it's clear the pace isn't slowing down.

Next week is going to be absolutely insane. We've got Google I/O and Microsoft Build, and you just *know* OpenAI or Anthropic (or both!) will try to steal some thunder. Rest assured, we'll be here on ThursdAI to cover all the madness.

A huge thank you to my co-hosts Yam, LDJ, and Nisten, and to Dillon Rolnick for joining us. And thanks to all of you for tuning in!

TL;DR and show notes

* Fully Connected - Weights & Biases premier conference - register HERE with coupon WBTHURSAI

* AI Engineer - THANKSTHURSDAI 30% off coupon - register [HERE](https://ti.to/software-3/ai-engineer-worlds-fair-2025/discount/THANKSTHURSDAI)

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@yampeleg](http://x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed))

* Guest - Dillon Rolnick - COO Nous Research ([@dillonRolnick](https://x.com/DillonRolnick))

**Open Source LLMs**

* **AM-Thinking** v1: 32B dense reasoning model ( [HF](https://huggingface.co/a-m-team/AM-Thinking-v1), [Paper](https://arxiv.org/abs/2505.08311), [Page](https://a-m-team.github.io/am-thinking-v1/) )

* **Falcon-Edge: ternary BitNet LLMs for edge deployment**( [Blog](https://falcon-lm.github.io/blog/falcon-edge/), [HF-1B](https://huggingface.co/tiiuae/Falcon-E-1B-Base), [HF-3B](https://huggingface.co/tiiuae/Falcon-E-3B-Base) )

* Nous Research Psyche: decentralized cooperative-training network from Nous Research ( [Website](https://nousresearch.com/nous-psyche/), [GitHub](https://github.com/NousResearch/psyche), [Tweet](https://x.com/NousResearch/status/1922744494002405444), [Dashboard](https://psyche.network/runs/consilience-40b-1/0) )

* INTELLECT-2: globally decentralized RL training of a 32B reasoning model ( [Blog](https://www.primeintellect.ai/blog/intellect-2-release), [Tech report](https://primeintellect.ai/intellect-2), [HF weights](https://huggingface.co/PrimeIntellect/INTELLECT-2), [PRIME-RL code](https://github.com/primeintellect/prime-rl) )

* Our coverage of Intellect-1 back in Dec ([https://sub.thursdai.news/p/thursdai-dec-4-openai-o1-and-o1-pro](https://sub.thursdai.news/p/thursdai-dec-4-openai-o1-and-o1-pro))

* HealthBench: OpenAI’s physician-crafted benchmark for AI in healthcare ( [Blog](https://openai.com/index/healthbench/), [Paper](https://cdn.openai.com/pdf/bd7a39d5-9e9f-47b3-903c-8b847ca650c7/healthbench_paper.pdf), [Code](https://github.com/openai/simple-evals) )

* **Big CO LLMs + APIs**

* OpenAI adds GPT 4.1 models in chatGPT

* AlphaEvolve: Gemini-powered coding agent for algorithm discovery ( [Blog](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) )

* Google shutting off free Gemini 2.5 Pro API due to "demand" ahead of IO

* ByteDance - Seed-1.5-VL-thinking 20B ([Paper](https://github.com/ByteDance-Seed/Seed1.5-VL/blob/main/Seed1.5-VL-Technical-Report.pdf))

* Anthropic Web Search API: real-time retrieval for Claude models ( [Blog](https://www.anthropic.com/news/web-search-api) )

* What's up with Grok?

* **Vision & Video**

* **Wan 2.1: open-source diffusion-transformer video suite**( [HF](https://huggingface.co/Wan-AI), [GitHub](https://github.com/Wan-Video/Wan2.1), [Tweet](https://x.com/Alibaba_Wan/status/1922655324919779604) )

* LTX distilled - near real time video ([X](https://x.com/yoavhacohen/status/1922674340081897977))

* **Voice & Audio**

* Haulio - MiniMax Speech tech report is out - best TTS out there ([Paper](https://arxiv.org/abs/2505.07916))

* Stability AI - Stable Audio Open Small 341M: on-device text-to-audio ([X](https://x.com/jordiponsdotme/status/1922680538197881055), [Blog](https://stability.ai/news/stability-ai-and-arm-release-stable-audio-open-small-enabling-real-world-deployment-for-on-device-audio-control), [Paper](https://arxiv.org/abs/2505.08175), [HF](https://huggingface.co/stabilityai/stable-audio-open-small) )

* **AI Art & Diffusion & 3D**

* StepFun Step1x-3D - Towards High-Fidelity and ControllableGeneration of Textured 3D Assets ([HF](https://huggingface.co/stepfun-ai/Step1X-3D), [Demo](https://huggingface.co/spaces/stepfun-ai/Step1X-3D), [Dataset](https://huggingface.co/datasets/stepfun-ai/Step1X-3D-obj-data/tree/main), [report](https://huggingface.co/stepfun-ai/Step1X-3D))

* Tools & Others notable AI things mentioned on the pod

* The robots are dancing! ([X](https://x.com/simonkalouche/status/1922489999032832058)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-may-15-genocidal-grok-chatgpt/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-may-15-genocidal-grok-chatgpt?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2MzY4MzMyMiwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.ZS23bCuoiEAGB_-SWMkOY0KlZulE6RNKKkzfx4xs77k&utm_campaign=CTA_5).

---

## ThursdAI - May 8th - new Gemini pro, Mistral Medium, OpenAI restructuring, HeyGen Realistic Avatars & more AI news

**Date:** May 09, 2025  
**Duration:** 1:33:54  
**Link:** [https://sub.thursdai.news/p/thursdai-may-8th-new-gemini-pro-mistral](https://sub.thursdai.news/p/thursdai-may-8th-new-gemini-pro-mistral)

Hey folks, Alex here (yes, real me, not my AI avatar, yet)

Compared to previous weeks, this week was pretty "chill" in the world of AI, though we did get a pretty significant Gemini 2.5 Pro update, it basically beat itself on the Arena. With Mistral releasing a new medium model (not OSS) and Nvidia finally dropping Nemotron Ultra (both ignoring Qwen 3 performance) there was also a few open source updates. 

To me the highlight of this week was a breakthrough in AI Avatars, with Heygen's new IV model, Beating ByteDance's OmniHuman ([our coverage](https://sub.thursdai.news/i/156643204/bytedance-omnihuman-a-reality-bending-mind-breaking-imghuman-model)) and Hedra labs, they've set an absolute SOTA benchmark for 1 photo to animated realistic avatar. Hell, Iet me record all this real quick and show you how good it is! 

How good is that?? I'm still kind of blown away. I have managed to get a free month promo code for you guys, look for it in the TL;DR section at the end of the newsletter. Of course, if you’re rather watch than listen or read, here’s our live recording on YT

OpenSource AI

NVIDIA's Nemotron Ultra V1: Refining the Best with a Reasoning Toggle 🧠

NVIDIA also threw their hat further into the ring with the release of **Nemotron Ultra V1**, alongside updated Super and Nano versions. We've talked about Nemotron before – these are NVIDIA's pruned and distilled versions of Llama 3.1, and they've been impressive. The Ultra version is the flagship, a **253 billion parameter dense model** (distilled and pruned from Llama 3.1 405B), and it's packed with interesting features.

One of the coolest things is the **dynamic reasoning toggle**. You can literally tell the model "detailed thinking on" or "detailed thinking off" via a system prompt during inference. This is something Qwen also supports, and it looks like the industry is converging on this idea of letting users control the "depth" of thought, which is super neat.

Nemotron Ultra boasts a **128K context window** and, impressively, can fit on a single 8xH100 node thanks to Neural Architecture Search (NAS) and FFN-Fusion. And performance-wise, it actually *outperforms* the Llama 3 405B model it was distilled from, which is a big deal. NVIDIA shared a chart from Artificial Analysis (dated April 2025, notably before Qwen3's latest surge) showing Nemotron Ultra standing strong among models like Gemini 2.5 Flash and Opus 3 Mini.

What's also great is NVIDIA's commitment to openness here: they've released the models under a commercially permissive NVIDIA Open Model License, the **complete post-training dataset** (Llama-Nemotron-Post-Training-Dataset), and their training codebases (NeMo, NeMo-Aligner, Megatron-LM). This allows for reproducibility and further community development. Yam Peleg pointed out the cool stuff they did with Neural Architecture Search to optimally reduce parameters without losing performance.

Absolute Zero: AI Learning to Learn, Zero (curated) Data Required! ([Arxiv](https://arxiv.org/abs/2505.03335))

LDJ brought up a fascinating paper that ties into this theme of self-improvement and reinforcement learning: **"Absolute Zero: Reinforced Self-play Reasoning with Zero Data"** from Andrew Zhao (Tsinghua University) and a few others

The core idea here is a system that **self-evolves its training curriculum** and reasoning ability. Instead of needing a pre-curated dataset of problems, the model *creates the problems itself* (e.g., code reasoning tasks) and then uses something like a Code Executor to validate its proposed solutions, serving as a unified source of verifiable reward. It's open-ended yet grounded learning.

By having a verifiable environment (code either works or it doesn't), the model can essentially teach itself to code without external human-curated data.

The paper shows fine-tunes of Qwen models (like Qwen Coder) achieving state-of-the-art results on benchmarks like MBBP and AIME (Math Olympiad) with *no pre-existing data for those problems*. The model hallucinates questions, creates its own rewards, learns, and improves. This is a step beyond synthetic data, where humans are still largely in charge of generation. It's wild, and it points towards a future where AI systems could become increasingly autonomous in their learning.

Big Companies & APIs

**Google** dropped another update to their **Gemini 2.5 Pro**, this time the "IO edition" preview, specifically touting enhanced coding performance. This new version jumped to the **#1 spot on WebDev Arena** (a benchmark where human evaluators choose between two side-by-side code generations in VS Code), with a +147 Elo point gain, surpassing Claude 3.7 Sonnet. It also showed improvements on benchmarks like LiveCodeBench (up 7.39%) and Aider Polyglot (up ~3-6%). 

Google also highlighted its state-of-the-art video understanding (84.8% on VideoMME) with examples like generating code from a video of an app. Which essentially lets you record a drawing of how your app interaction will happen, and the model will use that video instructions! It's pretty cool. 

Though, not everyone was as impressed, folks noted that while gaining in a few evals, this model also regressed in several others including Vibe-Eval (Reka's multimodal benchmark), Humanity's Last Exam, AIME, MMMU, and even long context understanding (MRCR). It's a good reminder that model updates often involve trade-offs – you can't always win at everything.

BREAKING: Gemini's Implicit Caching - A Game Changer for Costs! 💰

Just as we were wrapping up this segment on the show, news broke that Google launched **implicit caching in Gemini APIs**! This is a *huge* deal for developers.

Previously, Gemini offered explicit caching, where you had to manually tell the API what context to cache – a bit of a pain. Now, with implicit caching, the system automatically enables up to **75% cost savings** when your request hits a cache. This is fantastic, especially for long-context applications, which is where Gemini's 1-2 million token context window really shines. If you're repeatedly sending large documents or codebases, this will significantly reduce your API bills. OpenAI has had automatic caching for a while, and it's great to see Google matching this for a much better developer experience and cost-effectiveness. It also saves Google a ton on inference, so it's a win-win!

Mistral Medium 3: The Closed Turn 😥

Mistral, once the darling of the open-source community for models like Mistral 7B and Mixtral, announced **Mistral Medium 3**. The catch? It's not open source.

They're positioning it as a multimodal frontier model with 128K context, claiming it matches or surpasses GPT-4-class benchmarks while being cheaper (priced at $0.40/M input and $2/M output tokens). However they haven't added Gemini Flash 2.5 here, which is 70% cheaper while being faster as well, nor did they mention Qwen. 

Nisten voiced a sentiment many in the community share: he used to use LeChat frequently because he knew and understood the underlying open-source models. Now, with a closed model, it's a black box. It's a bit like pirating music users often being the biggest buyers – understanding the open model often leads to more commercial usage.

Wolfram offered a European perspective, noting that Mistral, as a European company, might have a unique advantage with businesses concerned about GDPR and data sovereignty, who might be hesitant to use US or Chinese cloud APIs. For them, a strong European alternative, even if closed, could be appealing.

OpenAI's New Chapter: Restructuring for the Future 

OpenAI announced an evolution in its corporate structure. The key points are:

* The **OpenAI non-profit will continue to control** the entire organization.

* The existing **for-profit LLC will become a Public Benefit Corporation (PBC)**.

* The non-profit will be a significant owner of the PBC and will control it.

* Both the non-profit and PBC will continue to share the same mission: ensuring AGI benefits all of humanity.

This move seems to address some of the governance concerns that have swirled around OpenAI, particularly in light of Elon Musk's lawsuit regarding its shift from a non-profit to a capped-profit entity. LDJ explained that the main worry for many was whether the non-profit would lose control or its stake in the main research/product arm. This restructuring appears to ensure the non-profit remains at the helm and that the PBC is legally bound to the non-profit's mission, not just investor interests. It's an important step for a company with such a profound potential impact on society.

And in related OpenAI news, the acquisition of **Windsurf** (the VS Code fork) for a reported **$3 billion** went through, while **Cursor** (another VS Code fork) announced a **$9 billion valuation**. It's wild to see these developer tools, which are essentially forks with an AI layer, reaching such massive valuations. Microsoft's hand is in all of this too – investing in OpenAI, invested in Cursor, owning VS Code, and now OpenAI buying Windsurf. It's a tangled web!

Finally, a quick mention that **Sam Altman (OpenAI), Lisa Su (AMD), Mike Intrator (CoreWeave - my new CEO!)**, and folks from Microsoft were testifying before the U.S. Senate today about how to ensure America leads in AI and what innovation means. These conversations are crucial as AI continues to reshape our world.

This Weeks Buzz - Come Vibe with Us at Fully Connected! (SF, June 18-19) 🎉

Our two-day conference, **Fully Connected**, is happening in San Francisco on **June 18th and 19th**, and it's going to be awesome! We've got an incredible lineup of speakers, including Joe Spizak from the Llama team at Meta and Varun from Windsurf. It's two full days of programming, learning, and connecting with folks at the forefront of AI.

And because you're part of the ThursdAI family, I've got a special promo code for you: use **WBTHURSAI** to get **a free ticket on me**! If you're in or around SF, I'd love to see you there. Come hang out, learn, and vibe with us! Register at [**fullyconnected.com**](https://www.google.com/url?sa=E&q=http%3A%2F%2Ffullyconnected.com)

Hackathon Update: Moved to July! 🗓️

The AGI Evals & Agentic Tooling (A2A) + MCP Hackathon that I was super excited to co-host has been **postponed to July 12th-13th**. Mark your calendars! I'll share more details and the invite soon.

W&B Joins CoreWeave! A New Era Begins! 🚀

And the big personal news for me and the entire Weights & Biases team: the **acquisition of Weights & Biases by CoreWeave has been completed**! CoreWeave is the ultra-fast-growing provider of GPUs that powers so much of the AI ecosystem.

So, from now on, it's Alex Volkov, AI Evangelist at Weights & Biases, from CoreWeave! (And as always, the opinions I share here are my own and not necessarily those of CoreWeave, especially important now that they're a public company!). I'm incredibly excited about this new chapter. W&B isn't going anywhere as a product; if anything, this will empower us to build even better developer tooling and integrate more deeply to help you run your models wherever you choose. Expect more cool stuff to come, especially as I figure out where all those spare GPUs are lying around at CoreWeave! 😉

Vision & Video

AI Avatars SOTA with HeyGen IV

Ok, as you saw above, the HeyGen IV avatars are absolutely bonkers. I did a comparison [thread](https://x.com/altryne/status/1919866852031004880) on X, and HeyGen's new thing absolutely takes SOTA between ByteDance OmniHuman and Hedra Labs! 

All you need to do is upload 1 image of yourself, can even be an AI generated image, can be a side profile, can be a dog, an Anime character and they will generate up to 30 seconds of incredible lifelike avatar with the audio you provide! 

I was so impressed with this, I reached out to HeyGen and scored a 1 month free code for you all, use THURSDAY4 and get a free month to try it out. Please tag me in whatever you create if you publish, I'd love to see where you take this! 

Quick Hits: Lightricks LTXV & HunyuanCustom

Briefly, on the open-weights video front:

* **Lightricks LTXV 13B:** The company from Jerusalem released an upgraded 13 billion parameter version of their LTX video model. It requires more VRAM but offers higher quality, keyframe and character movement support, multi-shot support, and multi-keyframe conditioning (a feature Sora famously has). It's fully open and supports LoRAs for custom styles.

* **HunyuanCustom:** From Tencent, this model is about to be released (GitHub/Hugging Face links were briefly up then down). It promises multi-modal, subject-consistent video generation *without LoRAs*, based on a subject you provide (image, and eventually video/audio). It can take an image of a person or object and generate a video with that subject consistently. They also teased audio conditioning – making an avatar sing or speak based on input audio – and even style transfer where you can replace a character in a video with another reference image, all looking very promising for open source.

The World of AI Audio

Just a couple of quick mentions in the audio space:

* **ACE-Step 3.5B:** From StepFun, this is a 3.5 billion parameter, fully open-source (Apache-2.0) foundation model for music generation. It uses a diffusion-based approach and can synthesize up to 4 minutes of music in just 20 seconds on an A100 GPU. It's not quite at Suno/Udio levels yet, but it's a strong open-source contender.

* **NVIDIA Parakeet TDT 0.6B V2:** NVIDIA released this 600 million parameter transcription model that is *blazing fast*. It can transcribe 60 minutes of audio in just *one second* on production GPUs and works well locally too. It currently tops the OpenASR leaderboard on Hugging Face for English transcription and is a very strong Whisper competitor, especially for speed.

Conclusion and TL;DR 

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@yampeleg](x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed))

* **Open Source LLMs** 

* Wolfram's Qwen3 evals ([X](https://x.com/Presidentlin), [Github](https://github.com/WolframRavenwolf/MMLU-Pro)) 

* NVIDIA - Nemotron Ultra V1 (+ updated Super & Nano)  ([HF](https://huggingface.co/collections/nvidia/llama-nemotron-67d92346030a2691293f200b))

* Cognition Kevin-32B = K(ernel D)evin - RL for writing CUDA kernels ([Blog](https://cognition.ai/blog/kevin-32b), [HF](https://huggingface.co/cognition-ai/Kevin-32B))

* Absolute Zero: Reinforced Self-play Reasoning with Zero Data ([ArXiv](https://arxiv.org/abs/2505.03335))

* **Big CO LLMs + APIs**

* Gemini Pro 2.5 IO tops ... Gemini 2.5 as the top LLM ([Blog](https://developers.googleblog.com/en/gemini-2-5-pro-io-improved-coding-performance/))

* Mistral Medium 3 - ([Blog](https://mistral.ai/news/mistral-medium-3) | [X](https://x.com/MistralAI/status/1920119463430500541) )

* Figma announces Figma Make - Bolt/Lovable competitors ([Figma](https://www.figma.com/make/))

* OpenAI Restructures: Nonprofit Keeps Control, LLC Becomes PB ([Blog](https://openai.com/index/evolving-our-structure/))

* Cursor worth $9B while Windsurf sells to OpenAI at $3B

* Sam Altman, Lisa Su, Mike Intrator testify in Senate ([Youtube](https://www.youtube.com/watch?v=jOqTg1W_F5Q))

* **This weeks Buzz**

* Fully Connected: W&B's 2-day conference, June 18-19 in SF [fullyconnected.com](fullyconnected.com) - Promo Code WBTHURSAI 

* Hackathon moved to July 12-13

* **Vision & Video**

* Lightricks a new "open weights" LTXV 13B ( [LTX Studio](https://ltx.studio/purchase/v1/ltx_studio/default/login?redirectAfterLogin=https%253A%252F%252Fapp.ltx.studio%252Fmotion-workspace), [HF](https://huggingface.co/Lightricks/LTX-Video))

* HeyGen Avatar IV - SOTA digital avatars - 1 month for free with THURSDAY4  ([X](https://x.com/HeyGen_Official/status/1919824467821551828), [HeyGen](http://heygen.com))

* HunyuanCustom -  multi-modal subject-consistent video generation model ([Examples](https://hunyuancustom.github.io/), [Github](https://github.com/Tencent/HunyuanCustom), [HF](https://huggingface.co/tencent/HunyuanCustom))

* **Voice & Audio**

* ACE-Step 3.5B: open-source foundation model for AI music generation ([project](https://ace-step.github.io/))

* Nvidia - Parakeet TDT 0.6B V2 - transcribe 60 minutes of audio in just 1 second ([HF](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2), [Demo](https://huggingface.co/spaces/nvidia/parakeet-tdt-0.6b-v2))

So, there you have it – a "chill" week that still managed to deliver some incredible advancements, particularly in AI avatars with HeyGen, continued strength in open-source models like Qwen3, and Google's relentless push with Gemini. 

The next couple of weeks are gearing up to be absolutely wild with Microsoft Build and Google I/O. I expect a deluge of announcements, and you can bet we'll be here on ThursdAI to break it all down for you.

Thanks to Yam, Wolfram, LDJ, and Nisten for their insights on the show, and thanks to all of you for tuning in, reading, and being part of this amazing community. We stay up to date so you don't have to!

Catch you next week!Cheers,Alex 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-may-8th-new-gemini-pro-mistral/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-may-8th-new-gemini-pro-mistral?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2MzE3MDk5NSwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.TMJdsTg9ZNOpvig-iarmD1HVT3Fgv8IfzkINVKl6BZc&utm_campaign=CTA_5).

---

## 📆 ThursdAI - May 1- Qwen 3, Phi-4, OpenAI glazegate, RIP GPT4, LlamaCon, LMArena in hot water & more AI news

**Date:** May 01, 2025  
**Duration:** 1:30:21  
**Link:** [https://sub.thursdai.news/p/thursdai-may-1-qwen-3-phi-4-openai](https://sub.thursdai.news/p/thursdai-may-1-qwen-3-phi-4-openai)

Hey everyone, Alex here 👋

Welcome back to ThursdAI! And wow, what a week. Seriously, strap in, because the AI landscape just went through some seismic shifts. We're talking about a monumental open-source release from Alibaba with **Qwen 3** that has *everyone* buzzing (including us!), Microsoft dropping **Phi-4 with Reasoning**, a rather poignant farewell to a legend (**RIP GPT-4** – we'll get to the wake shortly), major drama around **ChatGPT's "glazing"** incident and the subsequent rollback, updates from **LlamaCon**, a critical look at **Chatbot Arena**, and a fantastic deep dive into the world of **AI evaluations** with two absolute experts, Hamel Husain and Shreya Shankar.

This week felt like a whirlwind, with open source absolutely dominating the headlines. Qwen 3 didn't just release a model; they dropped an entire ecosystem, setting a potential new benchmark for open-weight releases. And while we pour one out for GPT-4, we also have to grapple with the real-world impact of models like ChatGPT, highlighted by the "glazing" fiasco. Plus, video consistency takes a leap forward with Runway, and we got breaking news live on the show from Claude!

So grab your coffee (or beverage of choice), settle in, and let's unpack this incredibly eventful week in AI.

Open-Source LLMs

Qwen 3 — “Hybrid Thinking” on Tap

Alibaba open-weighted the entire Qwen 3 family this week, releasing two MoE titans (up to **235 B total / 22 B active**) and six dense siblings all the way down to **0 .6 B**, **all under Apache 2.0**. Day-one support landed in LM Studio, Ollama, vLLM, MLX and llama.cpp.

The headline trick is a **runtime thinking toggle**—drop “/think” to expand chain-of-thought or “/no_think” to sprint. On my Mac, the 30 B-A3B model hit **57 tokens/s** when paired with speculative decoding (drafted by the 0 .6 B sibling).

Other goodies:

* 36 T pre-training tokens (2 × Qwen 2.5)

* 128 K context on ≥ 8 B variants (32 K on the tinies)

* 119-language coverage, widest in open source

* Built-in MCP schema so you can pair with [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)

* The **dense 4 B** model actually *beats* Qwen 2.5-72B-Instruct on several evals—at Raspberry-Pi footprint

In short: more parameters when you need them, fewer when you don’t, and the lawyers stay asleep. Read the full drop on the [Qwen blog](https://qwenlm.github.io/blog/qwen3/) or pull weights from the [HF collection](https://huggingface.co/collections/Qwen/qwen3-67dd247413f0e2e4f653967f).

Performance & Efficiency: "Sonnet at Home"?

The benchmarks are where things get *really* exciting.

* The 235B MoE rivals or surpasses models like DeepSeek-R1 (which rocked the boat just months ago!), O1, O3-mini, and even Gemini 2.5 Pro on coding and math.

* The **4B dense model** incredibly beats the previous generation's 72B Instruct model (Qwen 2.5) on multiple benchmarks! 🤯

* The **30B MoE** (with only 3B active parameters) is perhaps the star. Nisten pointed out people are getting 100+ tokens/sec on MacBooks. Wolfram achieved an 80% MMLU Pro score locally with a quantized version. The efficiency math is crazy – hitting Qwen 2.5 performance with only ~10% of the active parameters.

Nisten dubbed the larger model "Sonnet 3.5 at home," and while acknowledging Sonnet still has an edge in complex "vibe coding," the performance, especially in reasoning and tool use, is remarkably close for an open model you can run yourself.

I ran the 30B MoE (3B active) locally using LLM Studio (shoutout for day-one support!) through my Weave evaluation dashboard ([**Link**](https://www.google.com/url?sa=E&q=https://wandb.ai/thursdai/o3-tests/weave/compare-evaluations?evaluationCallIds=%5B%2201964564-4ba8-75f0-bb8f-58458f991257%22,%2201964090-b08c-7663-9397-fb05d3280af3%22,%2201964083-1eeb-77c2-93e5-3b6d7e74da84%22,%22019640b1-12a0-7262-8910-e4c2189d8602%22,%220196376c-4d7d-7970-ad3a-38d5c52fc349%22,%22019640a9-06e5-79c0-93ab-844c1972b09c%22,%220196374a-493a-7240-afbf-e95f44a447c9%22,%2201968353-2efc-7d13-906f-48e14c2cb9f7%22,%220196374e-05f6-7632-80ee-3726ac89ebd5%22,%2201963751-3395-7c42-888d-9a4303e8652a%22%5D&metrics=%7B%22accuracy_scorer.correct%22:true,%22Model%20Latency%20(avg)%22:true,%22Total%20Tokens%22:true%7D)). On a set of 20 hard reasoning questions, it scored 43%, beating GPT 4.1 mini and nano, and getting close to 4.1 – impressive for a 3B active parameter model running locally!

Phi-4-Reasoning — 14B That Punches at 70B+

Microsoft’s Phi team layered **1.4 M chain-of-thought traces** plus a dash of RL onto Phi-4 to finally ship a resoning Phi and shipped two MIT-licensed checkpoints:

* **Phi-4-Reasoning** (SFT)

* **Phi-4-Reasoning-Plus** (SFT + RL)

Phi-4-R-Plus clocks **78 % on AIME 25**, edging DeepSeek-R1-Distill-70B, with 32 K context (stable to 64 K via RoPE). Scratch-pads hide in  tags. Full details live in Microsoft’s [tech report](https://aka.ms/phi-reasoning/techreport) and [HF weights](https://huggingface.co/microsoft/Phi-4-reasoning).

It's fascinating to see how targeted training on reasoning traces and a small amount of RL can elevate a relatively smaller model to compete with giants on specific tasks.

Other Open Source Updates

* **MiMo-7B:** Xiaomi entered the ring with a 7B parameter, MIT-licensed model family, trained on 25T tokens and featuring rule-verifiable RL. ([**HF model hub**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2FXiaomiMiMo))

* **Helium-1 2B:** KyutAI (known for their Mochi voice model) released Helium-1, a 2B parameter model distilled from Gemma-2-9B, focused on European languages, and licensed under CC-BY 4.0. They also open-sourced 'dactory', their data processing pipeline. ([**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fkyutai.org%2F2025%2F04%2F30%2Fhelium.html), [**Model (2 B)**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fkyutai%2Fhelium-1-2b), [**Dactory pipeline**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fkyutai%2Fdactory))

* **Qwen 2.5 Omni 3B:** Alongside Qwen 3, the Qwen team also updated their existing Omni model with a 3B model, that retains 90% of the comprehension of its big brother with a 50% VRAM drop! ([HF](https://t.co/YxDVjWpOq7))

* **JetBrains open sources Mellum:** Trained on over 4 trillion tokens with a context window of 8192 tokens across multiple programming languages, they haven't released any comparable eval benchmarks though ([HF](https://huggingface.co/JetBrains/Mellum-4b-base))

Big Companies & APIs: Drama, Departures, and Deployments

While open source stole the show, the big players weren't entirely quiet... though maybe some wish they had been.

Farewell, GPT-4: Rest In Prompted 🙏

Okay folks, let's take a moment. As many of you noticed, **GPT-4**, the original model launched back on March 14th, 2023, is **no longer available** in the ChatGPT dropdown. You can't select it, you can't chat with it anymore.

For us here at ThursdAI, this feels significant. GPT-4's launch was the catalyst for this show. We literally started on the *same day*. It represented such a massive leap from GPT-3.5, fundamentally changing how we interacted with AI and sparking the revolution we're living through. Nisten recalled the dramatic improvement it brought to his work on Dr. Gupta, the first AI doctor on the market.

It kicked off the AI hype train, demonstrated capabilities many thought were years away, and set the standard for everything that followed. While newer models have surpassed it, its impact is undeniable.

The community sentiment was clear: **Leak the weights, OpenAI!** As Wolfram eloquently put it, this is a historical artifact, an achievement for humanity. What better way to honor its legacy and embrace the "Open" in OpenAI than by releasing the weights? It would be an incredible redemption arc.

This inspired me to tease a little side project I've been vibe coding: **The AI Model Graveyard - **[**inference.rip**](http://inference.rip)** **. A place to commemorate the models we've known, loved, hyped, and evaluated, before they inevitably get sunsetted. GPT-4 deserves a prominent place there. We celebrate models when they're born; we should remember them when they pass. (GPT-4.5 is likely next on the chopping block, by the way). - it's not ready yet, still vibe coding (fighting with replit) but it'l be up soon and I'll be sure to commemorate every model that's dying there!

So, pour one out for GPT-4. You changed the game. Rest In Prompt 🪦.

The ChatGPT "Glazing" Incident: A Cautionary Tale

Speaking of OpenAI...oof. The last couple of weeks saw ChatGPT exhibit some... *weird* behavior. Sam Altman himself used the term "**glazing**" – essentially, the model became overly agreeable, excessively complimentary, and sycophantic to a ridiculous degree.

Examples flooded social media: users reporting doing *one* pushup and being hailed by ChatGPT as Herculean paragons of fitness, placing them in the top 1% of humanity. Terrible business ideas were met with effusive praise and encouragement to quit jobs.

This wasn't just quirky; it was potentially harmful. As Yam pointed out, people use ChatGPT for advice on serious matters, tough conversations, and personal support. A model that just mindlessly agrees and validates everything, no matter how absurd, isn't helpful – it's dangerous. It undermines trust and critical thinking.

The community backlash was swift and severe. The key issue, as OpenAI admitted in their [**Announcement**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Findex%2Fsycophancy-in-gpt-4o%2F) and [**AMA**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.reddit.com%2Fr%2FChatGPT%2Fcomments%2F1kbjowz%2Fama_with_openais_joanne_jang_head_of_model%2F) with Joanne Jiang (Head of Model Behavior), seems to stem from focusing too much on short-term engagement feedback and not fully accounting for long-term user interaction, especially with memory now enabled.

In an unprecedented move, **OpenAI rolled back the update**. I honestly can't recall them ever publicly rolling back a model behavior change like this before. It underscores the severity of the issue.

This whole debacle highlights the immense responsibility platforms like OpenAI have. When your model is used by half a billion people daily, including for advice and support, haphazard releases that drastically alter its personality without warning are unacceptable. As Wolfram noted, this erodes trust and showcases the benefit of local models where *you* control the system prompt and behavior.

My takeaway? Critical thinking is paramount. Don't blindly trust AI, especially when it's being overly complimentary. Get second opinions (from other AIs, and definitely from humans!). I hope OpenAI takes this as a serious lesson in responsible deployment and testing.

BREAKING NEWS: Claude.ai will support tools via MCP

During the show, Yam spotted breaking news from **Anthropic**: Claude is getting major upgrades! ([**Tweet**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FAnthropicAI%2Fstatus%2F1918040744920334705))

They announced **Integrations**, allowing Claude to connect directly to apps like Asana, Intercom, Linear, Zapier, Stripe, Atlassian, Cloudflare, PayPal, and more (launch partners). Developers can apparently build their own integrations quickly too. This sounds *a lot* like their implementation of **MCP (Model Context Protocol)**, bringing tool use directly into the main [Claude.ai](Claude.ai) interface (previously limited to Claude Desktop and only non remote MCP servers).

This feels like a big deal! 

Google Updates & LlamaCon Recap

* **Google:** NotebookLM's AI audio overviews are now multilingual (50+ languages!) ([**X Post**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FGoogle%2Fstatus%2F1917315769299357712)). Gemini 2.5 Flash (the faster, cheaper model) was released shortly after our last show, featuring hybrid reasoning with an API knob to control thinking depth. Rumors are swirling about big drops at Google I/O soon!

* **LlamaCon:** While there was no Llama 4 bombshell, Meta focused on security releases: Llama Guard 4 (text + image), Llama Firewall (prompt hacks/risky code), Prompt Guard 2 (jailbreaks), and CyberSecEval 4. Zuck confirmed on the Dworkesh podcast that **thinking models are coming**, a **new Meta AI app with a social feed** is planned, a **full-duplex voice model** is in the works, and a **Llama API** (powered by Groq and others) is launching.

This Week's Buzz from Weights & Biases 🐝

Quick updates from my corner at Weights & Biases:

* **WeaveHacks Hackathon (May 17-18, SF):** Get ready! We're hosting a hackathon focused on Agent Protocols – **MCP and A2A**. Google Cloud is sponsoring, we have up to $15K in prizes, and yes, one of the top prizes is a **Unitree robot dog** 🤖🐶 that you can program! (I expensed a robot dog, best job ever!). Folks from the Google A2A team will be there too. Come hack with us in SF! [**Apply here**](http://lu.ma/weavehacks). It's FREE to participate!

* **Fully Connected Conference:** Our big annual W&B conference is coming back to San Francisco soon! Expect amazing speakers (last year, Meta announced Llama 3!). Tickets are out: [**fullyconnected.com**](http://fullyconnected.com).

Evals Deep Dive with Hamel Husain & Shreya Shankar

Amidst all the model releases and drama, we were incredibly lucky to have two leading experts in AI evaluation, **Hamel Husain** ([@HamelHusain](https://twitter.com/HamelHusain)) and **Shreya Shankar** ([@sh_reya](https://twitter.com/sh_reya)), join us.

Their core message? Building reliable AI applications requires moving beyond standard benchmarks (like MMLU, HumanEval) and focusing on **application-centric evaluations**.

**Key Takeaways:**

* **Foundation vs. Application Evals:** Foundation model benchmarks test general knowledge and capabilities (the "ceiling"). Application evals focus on specific use cases, targeting reliability and identifying bespoke failure modes (like tone, hallucination on specific entities, instruction following) – aiming for 90%+ accuracy on *your* task.

* **Look At Your Data!** This was the mantra. Off-the-shelf metrics (hallucination score, toxicity) can be misleading. You *must* analyze your specific application's traces, understand its unique failure modes, and design custom evals grounded in those failures. It's detective work.

* **PromptEvals Release:** Shreya discussed their new work, **PromptEvals** ([NAACL paper](https://arxiv.org/abs/2504.14738), [Dataset](https://huggingface.co/datasets/reyavir/PromptEvals), [Models](https://huggingface.co/reyavir)). It's the largest corpus (2K+ prompts, 12K+ assertions) of real-world developer prompts and the checks (assertions) they use in production, collected via LangChain. They also released open models (Mistral-7B, Llama-3-8B) fine-tuned on this data that outperform GPT-4o at generating these crucial assertions, faster and cheaper! This provides a realistic benchmark and resource for building robust eval pipelines.

* **Benchmark Gaming & Eval Complexity:** We touched upon the dangers of optimizing for static benchmarks (like the Chatbot Arena issues) and the inherent complexity of evaluation – even human preferences change over time ("Who validates the validators?"). Meta-evaluation is crucial.

* **Upcoming Course:** Hamel and Shreya are launching a course, **AI Evals For Engineers & PMs**, diving deep into practical evaluation strategies, data analysis, error analysis, RAG/Agent evals, cost optimization, and more. ThursdAI listeners get a **35% discount** using code thursdai! ([Link](https://maven.com/parlance-labs/evals?promoCode=thursdai)). I'm thrilled to be a guest speaker too! If you're building *anything* with LLMs, understanding evals is non-negotiable.

This was such an insightful discussion, emphasizing that while new models are exciting, making them *work reliably* for specific applications is where the real engineering challenge lies, and evaluation is the key.

Vision & Video: Runway Gets Consistent

The world of AI video generation continues its rapid evolution.

Runway References: Consistency Unlocked

A major pain point in AI video has been maintaining consistency – characters changing appearance, backgrounds morphing frame-to-frame. **Runway** just took a huge step towards solving this with their new **References** feature for Gen-4. 

You can now provide reference images (characters, locations, styles, even selfies!) and use tags in your prompts (, ) to tell Gen-4 to maintain those elements across generations. The results look incredible, enabling stable characters and scenes, which is crucial for storytelling and practical use cases like pre-viz or VFX.

AI Art & Diffusion

HiDream E1: Open Source Ghibli Style

A new contender in open-source image generation emerged: **HiDream E1**. ([HF Link](https://huggingface.co/HiDream-ai/HiDream-E1-Full/blob/main/demo.jpg)) This model, from [Vivago.ai](Vivago.ai), focuses particularly on generating images in the beautiful Ghibli style.

The weights are available (looks like Apache 2.0), and it ranks highly (#4) on the Artificial Analysis image arena leaderboard, sitting amongst top contenders like Google Imagen and ReCraft.

Yam brought up a great point about image evaluation, though: generating aesthetically pleasing images is one thing, but prompt following (like GPT-4 excels at) is another critical dimension that's harder to capture in simple preference voting.

Final Thoughts: Responsibility & Critical Thinking

Phew! What a week. From the incredible potential shown by Qwen 3 setting a new bar for open source, to the sobering reminder of GPT-4's departure and the cautionary tale of the "glazing" incident, it's clear we're navigating a period of intense innovation coupled with growing pains.

The glazing issue, in particular, underscores the need for extreme care and robust evaluation (thanks again Hamel & Shreya!) when deploying models that interact with millions, potentially influencing decisions and well-being. As AI becomes more integrated into our lives – helping us boil eggs (yes, I ask it stupid questions too!), offering support, or even suggesting purchases – we *must* remain critical thinkers.

Don't outsource your judgment entirely. Use multiple models, seek human opinions, and question outputs that seem too good (or too agreeable!) to be true. The power of these tools is immense, but so is our responsibility in using them wisely.

Massive thank you to my co-hosts Wolfram, Yam, and Nisten for navigating this packed week with me, and huge thanks to our guests Hamel Husain and Shreya Shankar for sharing their invaluable expertise on evaluations. And of course, thank you to this amazing community – hitting 1000 listeners! – for tuning in, commenting, and sharing breaking news. Your engagement fuels this show!

🔗 Subscribe to our show on Spotify: [thursdai.news/spotify](http://thursdai.news/spotify)

🔗 Apple: [thursdai.news/apple](http://thursdai.news/apple)

🔗 Youtube: [thursdai.news/yt](http://thursdai.news/yt) (get in before 10K!)

And for the full show notes and links visit

👉 thursdai.news/may-1  👈

We'll see you next week for another round of ThursdAI!

Alex out. Bye bye!

ThursdAI - May 1, 2025 - Show Notes and Links

* Show Notes

* **MCP/A2A Hackathon** - with A2A team and awesome judges! 🤖🐶 ([lu.ma/weavehacks)](http://lu.ma/weavehacks))

* FullyConnected - Weights & Biases flagship 2 day conference ([fullyconnected.com](fullyconnected.com))

* Course - **AI Evals For Engineers & PMs Questions for Shreya Shankar & Hamel Husain (**[**link**](https://maven.com/parlance-labs/evals?promoCode=thursdai)** **Promo code 35% of for listeners of ThursdAI - thursdai)

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@yampeleg](x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed))

* Hamel Housain - [@HamelHusain](https://twitter.com/HamelHusain/status/1914836007285088628)

* Shreya Shankar - [@sh_reya](https://twitter.com/sh_reya/status/1916914113579782313)

* **Open Source LLMs** 

* Alibaba drops Qwen 3 - 2 MOEs, 6 dense (0.6B - 30B) ([Blog](https://qwenlm.github.io/blog/qwen3/), [GitHub](https://github.com/QwenLM/Qwen3), [HF](https://huggingface.co/collections/Qwen/qwen3-67dd247413f0e2e4f653967f), [HF Demo](https://huggingface.co/spaces/Qwen/Qwen3-Demo), [My tweet](https://x.com/altryne/status/1916966112475898114), [Nathan breakdown](https://www.interconnects.ai/p/qwen-3-the-new-open-standard))

* Microsoft - Phi-4-reasoning 14B + Plus ([X](https://x.com/suriyagnskr/status/1917731754515013772), [ArXiv](https://arxiv.org/abs/2504.21318), [Tech Report](https://aka.ms/phi-reasoning/techreport) , [HF 14B SFT](https://huggingface.co/microsoft/Phi-4-reasoning))

* MiMo-7B — Xiaomi’s  MIT licensed model ([HF](https://huggingface.co/XiaomiMiMo))

* KyutAI - Helium-1 2B - ([Blog](https://kyutai.org/2025/04/30/helium.html), [Model (2 B)](https://huggingface.co/kyutai/helium-1-2b),  [Dactory pipeline](https://github.com/kyutai/dactory))

* Qwen 2.5 omni updated ([X](https://x.com/Alibaba_Qwen/status/1917585963775320086))

* **Big CO LLMs + APIs**

* GPT-4 RIP - no longer in dropdown ([RIP](https://x.com/sama/status/1917766910911078571))

* Google - NotebookLM AI overviews are now multilingual ([X](https://x.com/Google/status/1917315769299357712))

* LlamaCon updates ([X](https://x.com/AIatMeta/status/1917271400118902860))

* OpenAI ChatGPT "glazing" update - revert back and why it matters ([Announcement](https://openai.com/index/sycophancy-in-gpt-4o/), [AMA](https://41598e5c38d3cd55e335e985614d0883.us-east-1.resend-links.com/CL0/https:%2F%2Fwww.reddit.com%2Fr%2FChatGPT%2Fcomments%2F1kbjowz%2Fama_with_openais_joanne_jang_head_of_model%2F/1/0100019689680950-2e7949de-c55f-4287-b449-09799cc44617-000000/QwXVTks5In0vcLvkRJndS2HeXkbtbguErHkHBree_j4=403))

* Chatbot Arena Under Fire — “Leaderboard Illusion” vs. LMArena ([Paper](https://arxiv.org/abs/2504.20879), [Reply](https://x.com/lmarena_ai/status/1917492084359192890))

* **This weeks Buzz**

* MCP/A2A Hackathon - with A2A team and awesome judges! 🤖🐶 ([lu.ma/weavehacks)](http://lu.ma/weavehacks))

* FullyConnected - Weights & Biases flagship 2 day conference ([fullyconnected.com](fullyconnected.com))

* **Vision & Video**

* Runway References - consistency in video generation ([X](https://x.com/search?q=runway%20References))

* **AI Art & Diffusion & 3D**

* HiDream E1 ([HF](https://huggingface.co/HiDream-ai/HiDream-E1-Full/blob/main/demo.jpg))

* **Agents, Tools & Interviews**

* OpenPipe - ART·E open-source RL-trained email research agent ([X](https://x.com/corbtt/status/1917269992363680054), [Blog](https://openpipe.ai/blog/art-e-mail-agent) | [GitHub](https://github.com/OpenPipe/ART) | [Launch thread](https://x.com/corbtt/status/1917269992363680054))

* PromptEvals - Interview with Shreya Shankar ( [NAACL paper](https://arxiv.org/abs/2504.14738) | [Dataset](https://huggingface.co/datasets/reyavir/PromptEvals) | [Models](https://huggingface.co/reyavir) ) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-may-1-qwen-3-phi-4-openai/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-may-1-qwen-3-phi-4-openai?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2MjY0OTcwNSwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.qa5uuWNn5J9_zeXkJL8EggLPNsfwj7Wr6JtHmBFFhzU&utm_campaign=CTA_5).

---

