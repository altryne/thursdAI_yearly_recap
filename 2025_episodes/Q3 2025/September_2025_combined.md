# ThursdAI Episodes - September 2025

Total Episodes: 4

---

## 📆 ThursdAI - Qwen‑mas Strikes Again: VL/Omni Blitz + Grok‑4 Fast + Nvidia’s $100B Bet

**Date:** September 26, 2025  
**Duration:** 1:34:07  
**Link:** [https://sub.thursdai.news/p/thursdai-sep-25-grok-fast-oainvidia](https://sub.thursdai.news/p/thursdai-sep-25-grok-fast-oainvidia)

Hola AI aficionados, it’s yet another ThursdAI, and yet another week FULL of AI news, spanning Open Source LLMs, Multimodal video and audio creation and more! 

Shiptember as they call it does seem to deliver, and it was hard even for me to follow up on all the news, not to mention we had like 3-4 breaking news during the show today! 

This week was yet another Qwen-mas, with Alibaba absolutely dominating across open source, but also NVIDIA promising to invest up to $100 Billion into OpenAI. 

So let’s dive right in! As a reminder, all the show notes are posted at the end of the article for your convenience. 

ThursdAI - Because weeks are getting denser, but we’re still here, weekly, sending you the top AI content! Don’t miss out

**Table of Contents**

* [Open Source AI](#%C2%A7open-source-ai)

* [Qwen3-VL Announcement (Qwen3-VL-235B-A22B-Thinking):](#%C2%A7qwen-vl-announcement-qwen-vl-b-ab-thinking-x-hf-blog-demo)

* [Qwen3-Omni-30B-A3B: end-to-end SOTA omni-modal AI unifying text, image, audio, and video](#%C2%A7qwen-omni-b-ab-end-to-end-sota-omni-modal-ai-unifying-text-image-audio-and-video-hf-github-qwen-chat-demo-api)

* [DeepSeek V3.1 Terminus: a surgical bugfix that matters for agents](#%C2%A7deepseek-v-terminus-a-surgical-bugfix-that-matters-for-agents-x-hf)

* [Evals & Benchmarks: agents, deception, and code at scale](#%C2%A7evals-and-benchmarks-agents-deception-and-code-at-scale)

* [Big Companies, Bigger Bets!](#%C2%A7big-companies-bigger-bets)

* [OpenAI: ChatGPT Pulse: Proactive AI news cards for your day](#%C2%A7openai-chatgpt-pulse-proactive-ai-news-cards-for-your-day-x-openai-blog)

* [XAI Grok 4 fast - 2M context, 40% fewer thinking tokens, shockingly cheap](#%C2%A7xai-grok-fast-m-context-fewer-thinking-tokens-shockingly-cheap-x-blog)

* [Alibaba Qwen-Max and plans for scaling](#%C2%A7alibaba-qwen-max-and-plans-for-scaling-x-blog-api)

* [This Week’s Buzz: W&B Fully Connected is coming to London and Tokyo & Another hackathon in SF](#%C2%A7this-weeks-buzz-w-and-b-fully-connected-is-coming-to-london-and-tokyo-and-another-hackathon-in-sf)

* [Vision & Video: Wan 2.2 Animate, Kling 2.5, and Wan 4.5 preview](#%C2%A7vision-and-video-wan-animate-kling-and-wan-preview)

* [Moondream-3 Preview - Interview with co-founders Via & Jay](#%C2%A7moondream-preview-interview-with-co-founders-via-and-jay)

* [Wan open sourced Wan 2.2 Animate (aka “Wan Animate”): motion transfer and lip sync](#%C2%A7wan-open-sourced-wan-animate-aka-wan-animate-motion-transfer-and-lip-sync)

* [Kling 2.5 Turbo: cinematic motion, cheaper and with audio](#%C2%A7kling-turbo-cinematic-motion-cheaper-and-with-audio)

* [Wan 4.5 preview: native multimodality, 1080p 10s, and lip-synced speech](#%C2%A7wan-preview-native-multimodality-p-s-and-lip-synced-speech)

* [Voice & Audio](#%C2%A7voice-and-audio)

* [ThursdAI - Sep 25, 2025 - TL;DR & Show notes](#%C2%A7thursdai-sep-tldr-and-show-notes)

Open Source AI

This was a Qwen-and-friends week. I joked on stream that I should just count how many times “Alibaba” appears in our show notes. It’s a lot.

Qwen3-VL Announcement (Qwen3-VL-235B-A22B-Thinking): ([X](https://x.com/Alibaba_Qwen/status/1970594923503391182), [HF](https://huggingface.co/collections/Qwen/qwen3-vl-68d2a7c1b8a8afce4ebd2dbe), [Blog](https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef&from=research.latest-advancements-list), [Demo](https://huggingface.co/spaces/Qwen/Qwen3-VL-Demo))

Qwen 3 launched earlier as a text-only family; the vision-enabled variant just arrived, and it’s not timid. The “thinking” version is effectively a reasoner with eyes, built on a 235B-parameter backbone with around 22B active (their mixture-of-experts trick). What jumped out is the breadth of evaluation coverage: MMU, video understanding (Video-MME, LVBench), 2D/3D grounding, doc VQA, chart/table reasoning—pages of it. They’re showing wins against models like Gemini 2.5 Pro and GPT‑5 on some of those reports, and doc VQA is flirting with “nearly solved” territory in their numbers.

Two caveats. First, whenever scores get that high on imperfect benchmarks, you should expect healthy skepticism; known label issues can inflate numbers. Second, the model is big. Incredible for server-side grounding and long-form reasoning with vision (they’re talking about scaling context to 1M tokens for two-hour video and long PDFs), but not something you throw on a phone.

Still, if your workload smells like “reasoning + grounding + long context,” Qwen 3 VL looks like one of the strongest open-weight choices right now.

Qwen3-Omni-30B-A3B: end-to-end SOTA omni-modal AI unifying text, image, audio, and video ([HF](https://huggingface.co/collections/Qwen/qwen3-omni-68d100a86cd0906843ceccbe), [GitHub](https://github.com/QwenLM/Qwen3-Omni), [Qwen Chat](https://chat.qwen.ai/?models=qwen3-omni-flash), [Demo](https://huggingface.co/spaces/Qwen/Qwen3-Omni-Demo), [API](https://modelstudio.console.alibabacloud.com/?tab=doc#/doc/))

Omni is their end-to-end multimodal chat model that unites text, image, and audio—and crucially, it streams audio responses in real time while thinking separately in the background. Architecturally, it’s a 30B MoE with around 3B active parameters at inference, which is the secret to why it feels snappy on consumer GPUs.

In practice, that means you can talk to Omni, have it see what you see, and get sub-250 ms replies in nine speaker languages while it quietly plans. It claims to understand 119 languages. When I pushed it in multilingual conversational settings it still code-switched unexpectedly (Chinese suddenly appeared mid-flow), and it occasionally suffered the classic “stuck in thought” behavior we’ve been seeing in agentic voice modes across labs. But the responsiveness is real, and the footprint is exciting for local speech streaming scenarios. I wouldn’t replace a top-tier text reasoner with this for hard problems, yet being able to keep speech native is a real UX upgrade.

Qwen Image Edit, Qwen TTS Flash, and Qwen‑Guard

Qwen’s image stack got a handy upgrade with multi-image reference editing for more consistent edits across shots—useful for brand assets and style-tight workflows. TTS Flash (API-only for now) is their fast speech synth line, and Q‑Guard is a new safety/moderation model from the same team. It’s notable because Qwen hasn’t really played in the moderation-model space before; historically Meta’s Llama Guard led that conversation.

DeepSeek V3.1 Terminus: a surgical bugfix that matters for agents ([X](url://16), [HF](url://59))

DeepSeek whale resurfaced to push a small 0.1 update to V3.1 that reads like a “quality and stability” release—but those matter if you’re building on top. It fixes a code-switching bug (the “sudden Chinese” syndrome you’ll also see in some Qwen variants), improves tool-use and browser execution, and—importantly—makes agentic flows less likely to overthink and stall. On the numbers, **Humanities Last Exam jumped from 15 to 21.7**, while LiveCodeBench dipped slightly. That’s the story here: they traded a few raw points on coding for more stable, less dithery behavior in end-to-end tasks. If you’ve invested in their tool harness, this may be a net win.

Liquid Nanos: small models that extract like they’re big ([X](https://x.com/LiquidAI_/status/1971198690707616157), [HF](https://huggingface.co/collections/LiquidAI/liquid-nanos-68b98d898414dd94d4d5f99a))

Liquid Foundation Models released “Liquid Nanos,” a set of open models from roughly 350M to 2.6B parameters, including “extract” variants that pull structure (JSON/XML/YAML) from messy documents. The pitch is cost-efficiency with surprisingly competitive performance on information extraction tasks versus models 10× their size. If you’re doing at-scale doc ingestion on CPUs or small GPUs, these look worth a try.

Tiny IBM OCR model that blew up the charts ([HF](https://huggingface.co/ibm-granite/granite-docling-258M))

We also saw a tiny IBM model (about 250M parameters) for image-to-text document parsing trending on Hugging Face. Run in 8-bit, it squeezes into roughly 250 MB, which means Raspberry Pi and “toaster” deployments suddenly get decent OCR/transcription against scanned docs. It’s the kind of tiny-but-useful release that tends to quietly power entire products.

Meta’s 32B Code World Model (CWM) released for agentic code reasoning ([X](https://x.com/syhw/status/1838682364055920980), [HF](https://huggingface.co/facebook/cwm))

Nisten got really excited about this one, and once he explained it, I understood why. Meta released a 32B code world model that doesn’t just generate code - it understands code the way a compiler does. It’s thinking about state, types, and the actual execution context of your entire codebase.

This isn’t just another coding model - it’s a fundamentally different approach that could change how all future coding models are built. Instead of treating code as fancy text completion, it’s actually modeling the program from the ground up. If this works out, expect everyone to copy this approach.

Quick note, this one was released with a research license only! 

Evals & Benchmarks: agents, deception, and code at scale

A big theme this week was “move beyond single-turn Q&A and test how these things behave in the wild.” with a bunch of new evals released. I wanted to cover them all in a separate segment. 

OpenAI’s GDP Eval: “economically valuable tasks” as a bar ([X](https://x.com/OpenAI/status/1971249374077518226), [Blog](https://openai.com/index/gdpval/))

OpenAI introduced GDP Eval to measure model performance against real-world, economically valuable work. The design is closer to how I think about “AGI as useful work”: 44 occupations across nine sectors, with tasks judged against what an industry professional would produce.

Two details stood out. First, OpenAI’s own models didn’t top the chart in their published screenshot—Anthropic’s Claude Opus 4.1 led with roughly a 47.6% win rate against human professionals, while GPT‑5-high clocked in around 38%. Releasing a benchmark where you’re not on top earns respect. Second, the tasks are legit. One example was a manufacturing engineer flow where the output required an overall design with an exploded view of components—the kind of deliverable a human would actually make.

What I like here isn’t the precise percent; it’s the direction. If we anchor progress to tasks an economy cares about, we move past “trivia with citations” and toward “did this thing actually help do the work?”

GAIA 2 (Meta Super Intelligence Labs + Hugging Face): agents that execute ([X](https://x.com/ClementDelangue/status/1970885829552705976), [HF](https://huggingface.co/blog/gaia2))

MSL and HF refreshed GAIA, the agent benchmark, with a thousand new human-authored scenarios that test execution, search, ambiguity handling, temporal reasoning, and adaptability—plus a smartphone-like execution environment. GPT‑5-high led across execution and search; Kimi’s K2 was tops among open-weight entries. I like that GAIA 2 bakes in time and budget constraints and forces agents to chain steps, not just spew plans. We need more of these.

**Scale AI’s “SWE-Bench Pro” for coding in the large (**[**HF**](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)**)**

Scale dropped a stronger coding benchmark focused on multi-file edits, 100+ line changes, and large dependency graphs. On the [public](https://scale.com/leaderboard/swe_bench_pro_public) set, GPT‑5 (not Codex) and Claude Opus 4.1 took the top two slots; on a [commercial](https://scale.com/leaderboard/swe_bench_pro_commercial) set, Opus edged ahead. The broader takeaway: the action has clearly moved to test-time compute, persistent memory, and program-synthesis outer loops to get through larger codebases with fewer invalid edits. This aligns with what we’re seeing across ARC‑AGI and SWE‑bench Verified.

The “Among Us” deception test ([X](https://x.com/shreyk0/status/1970160146975445192))

One more that’s fun but not frivolous: a group benchmarked models on the social deception game Among Us. OpenAI’s latest systems reportedly did the best job both lying convincingly and detecting others’ lies. This line of work matters because social inference and adversarial reasoning show up in real agent deployments—security, procurement, negotiations, even internal assistant safety.

Big Companies, Bigger Bets!

**Nvidia’s $100B pledge to OpenAI for 10GW of compute**

Let’s say that number again: one hundred billion dollars. Nvidia announced plans to invest up to $100B into OpenAI’s infrastructure build-out, targeting roughly 10 gigawatts of compute and power. Jensen called it the biggest infrastructure project in history. Pair that with OpenAI’s Stargate-related announcements—five new datacenters with Oracle and SoftBank and a flagship site in Abilene, Texas—and you get to wild territory fast.

Internal notes circulating say OpenAI started the year around 230MW and could exit 2025 north of 2GW operational, while aiming at 20GW in the near term and a staggering 250GW by 2033. Even if those numbers shift, the directional picture is clear: the GPU supply and power curves are going vertical.

Two reactions. First, yes, the “infinite money loop” memes wrote themselves—OpenAI spends on Nvidia GPUs, Nvidia invests in OpenAI, the market adds another $100B to Nvidia’s cap for good measure. But second, the underlying demand is real. If we need 1–8 GPUs per “full-time agent” and there are 3+ billion working adults, we are orders of magnitude away from compute saturation. The power story is the real constraint—and that’s now being tackled in parallel.

OpenAI: ChatGPT Pulse: Proactive AI news cards for your day ([X](https://x.com/OpenAI), [OpenAI Blog](https://openai.com/index/introducing-chatgpt-pulse/))

In a #BreakingNews segment, we got an update from OpenAI, that currently works only for Pro users but will come to everyone soon. Proactive AI, that learns from your chats, email and calendar and will show you a new “feed” of interesting things every morning based on your likes and feedback! 

Pulse marks OpenAI’s first step toward an AI assistant that brings the right info before you ask, tuning itself with every thumbs-up, topic request, or app connection. I’ve tuned mine for today, we’ll see what tomorrow brings! 

P.S - Huxe is a free app from the creators of NotebookLM (Ryza was on our podcast!) that does a similar thing, so if you don’t have pro, check out Huxe, they [just](https://x.com/gethuxe/status/1970503800885854431) launched! 

XAI Grok 4 fast - 2M context, 40% fewer thinking tokens, shockingly cheap ([X](https://x.com/xai/status/1969183326389858448), [Blog](https://x.ai/news/grok-4-fast))

xAI launched Grok‑4 Fast, and the name fits. Think “top-left” on the speed-to-cost chart: up to 2 million tokens of context, a reported 40% reduction in reasoning token usage, and a price tag that’s roughly 1% of some frontier models on common workloads. On LiveCodeBench, Grok‑4 Fast even beat Grok‑4 itself. It’s not the most capable brain on earth, but as a high-throughput assistant that can fan out web searches and stitch answers in something close to real time, it’s compelling.

Alibaba Qwen-Max and plans for scaling ([X](https://x.com/Alibaba_Qwen/status/1970599097297183035), [Blog](https://qwen.ai/blog?id=241398b9cd6353de490b0f82806c7848c5d2777d&from=research.latest-advancements-list), [API](https://www.alibabacloud.com/help/en/model-studio/models#c2d5833ae4jmo))

Back in the Alibaba camp, they also released their flagship API model, Qwen 3 Max, and showed off their future roadmap. 

Qwen-max is over 1T parameters, MoE that gets 69.6 on Swe-bench verified and outperforms GPT-5 on LMArena! 

And their plan is simple: scale. They’re planning to go from 1 million to **100 million token context windows** and scale their models into the terabytes of parameters. It culminated in a hilarious moment on the show where we all put on sunglasses to salute a slide from their [presentation](https://x.com/tphuang/status/1970886344499990672) that literally said, “Scaling is all you need.” AGI is coming, and it looks like Alibaba is one of the labs determined to scale their way there. Their release schedule lately (as documented by Swyx from Latent.space) is insane. 

This Week’s Buzz: W&B Fully Connected is coming to London and Tokyo & Another hackathon in SF

Weights & Biases (now part of the CoreWeave family) is bringing Fully Connected to London on Nov 4–5, with another event in Tokyo on Oct 31. If you’re in Europe or Japan and want two days of dense talks and hands-on conversations with teams actually shipping agents, evals, and production ML, come hang out. Readers got a code on stream; if you need help getting a seat, ping me directly.

Links: [**fullyconnected.com**](http://fullyconnected.com)

We are also opening up registrations to our second WeaveHacks hackathon in SF, October 11-12, yours trully will be there, come hack with us on Self Improving agents! Register [HERE](http://lu.ma/weavehacks2)

Vision & Video: Wan 2.2 Animate, Kling 2.5, and Wan 4.5 preview

This is the most exciting space in AI week-to-week for me right now. The progress is visible. Literally.

Moondream-3 Preview - Interview with co-founders Via & Jay

While I’ve already reported on Moondream-3 in the last weeks newsletter, this week we got the pleasure of hosting Vik Korrapati and Jay Allen the co-founders of MoonDream to tell us all about it. Tune in for that conversation on the pod starting at 00:33:00

Wan open sourced Wan 2.2 Animate (aka “Wan Animate”): motion transfer and lip sync 

Tongyi’s Wan team shipped an open-source release that the community quickly dubbed “Wanimate.” It’s a character-swap/motion transfer system: provide a single image for a character and a reference video (your own motion), and it maps your movement onto the character with surprisingly strong hair/cloth dynamics and lip sync. If you’ve used runway’s Act One, you’ll recognize the vibe—except this is open, and the fidelity is rising fast.

The practical uses are broader than “make me a deepfake.” Think onboarding presenters with perfect backgrounds, branded avatars that reliably say what you need, or precise action blocking without guessing at how an AI will move your subject. You act it; it follows.

Kling 2.5 Turbo: cinematic motion, cheaper and with audio

Kling quietly rolled out a 2.5 Turbo tier that’s 30% cheaper and finally brings audio into the loop for more complete clips. Prompts adhere better, physics look more coherent (acrobatics stop breaking bones across frames), and the cinematic look has moved from “YouTube short” to “film-school final.” They seeded access to creators and re-shared the strongest results; the consistency is the headline. (Source X: [@StevieMac03](https://x.com/StevieMac03/status/1970559778804908331))

I’ve chatted with my kiddos today over facetime, and they were building minecraft creepers. I took a screenshot, sent to Nano Banana to make their creepers into actual minecraft ones, and then with Kling, Animated the explosions for them. They LOVED it! Animations were clear, while VEO refused for me to even upload their images, Kling didn’t care haha

Wan 4.5 preview: native multimodality, 1080p 10s, and lip-synced speech

Wan also teased a 4.5 preview that unifies understanding and generation across text, image, video, and audio. The eye-catching bit: generate a 1080p, 10-second clip with synced speech from just a script. Or supply your own audio and have it lip-sync the shot. I ran my usual “interview a polar bear dressed like me” test and got one of the better results I’ve seen from any model. We’re not at “dialogue scene” quality, but “talking character shot” is getting… good. 

The generation of audio (not only text  + lipsync) is one of the best ones besides VEO, it’s really great to see how strongly this improves, sad that this wasn’t open sourced! And apparently it supports “draw text to animate”  (Source: [X](https://x.com/I_Muhammadali44/status/1971085386396147741)) 

Voice & Audio

**Suno V5: we’ve entered the “I can’t tell anymore” era**

Suno calls V5 a redefinition of audio quality. I’ll be honest, I’m at the edge of my subjective hearing on this. I’ve caught myself listening to Suno streams instead of Spotify and forgetting anything is synthetic. The vocals feel more human, the mixes cleaner, and the remastering path (including upgrading V4 tracks) is useful. The last 10% to “you fooled a producer” is going to be long, but the distance between V4 and V5 already makes me feel like I should re-cut our ThursdAI opener.

**MiMI Audio: a small omni-chat demo that hints at the floor**

We tried a MiMI Audio demo live—a 7B-ish model with speech in/out. It was responsive but stumbled on singing and natural prosody. I’m leaving it in here because it’s a good reminder that the open floor for “real-time voice” is rising quickly even for small models. And the moment you pipe a stronger text brain behind a capable, native speech front-end, the UX leap is immediate.

Ok, another DENSE week that finishes up Shiptember, tons of open source, Qwen (Tongyi) shines, and video is getting so so good. This is all converging folks, and honestly, I’m just happy to be along for the ride! 

This week was also **Rosh Hashanah**, which is the Jewish new year, and I’ve shared on the pod that I’ve found my X post from 3 years ago, using the state of the art AI models of the time. WHAT A DIFFERENCE 3 years make, just take a look, I had to scale down the 4K one from this year just to fit into the pic! 

Shana Tova to everyone who’s reading this, and we’ll see you next week 🫡

ThursdAI - Sep 25, 2025 - TL;DR & Show notes

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](https://x.com/altryne))

* Co Hosts - [@yampeleg](https://x.com/yampeleg) [@nisten](https://x.com/nisten) [@ldjconfirmed](https://x.com/ldjconfirmed) [@ryancarson](https://x.com/ryancarson)

* Guest - Vik Korrapathy ([@vikhyatk](https://x.com/vikhyatk)) - Moondream

* **Open Source AI (LLMs, VLMs, Papers & more)**

* DeepSeek V3.1 Terminus: cleaner bilingual output, stronger agents, cheaper long-context ([X](https://x.com/deepseek_ai/status/1968682364055920980), [HF](https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Terminus))

* Meta’s 32B Code World Model (CWM) released for agentic code reasoning ([X](https://x.com/syhw/status/1838682364055920980), [HF](https://huggingface.co/facebook/cwm))

* Alibaba Tongyi Qwen on a release streak again: 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-sep-25-grok-fast-oainvidia/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-sep-25-grok-fast-oainvidia?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3NDU4MzkwNCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.p8oADIwHDKCagIbSnfxFisuJhP8OHe2h2YoDXUuHl3s&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Sep 18 - Gpt-5-Codex, OAI wins ICPC, Reve, ARC-AGI SOTA Interview, Meta AI Glasses & more AI news

**Date:** September 19, 2025  
**Duration:** 1:44:55  
**Link:** [https://sub.thursdai.news/p/thursdai-sep-18-gpt-5-codex-oai-wins](https://sub.thursdai.news/p/thursdai-sep-18-gpt-5-codex-oai-wins)

Hey folks, 

What an absolute packed week this week, which started with yet another crazy model release from OpenAI, but they didn't stop there, they also announced GPT-5 winning the ICPC coding competitions with 12/12 questions answered which is apparently really really [hard](https://x.com/bminaiev/status/1968363052329484642)! 

Meanwhile, Zuck took the Meta Connect 25' stage and announced a new set of Meta glasses with a display! On the open source front, we yet again got multiple tiny models doing DeepResearch and Image understanding better than much larger foundational models.

Also, today I interviewed Jeremy Berman, who topped the ArcAGI with a 79.6% score and some crazy Grok 4 prompts, a new image editing experience called Reve, a new world model and a BUNCH more! So let's dive in! As always, all the releases, links and resources at the end of the article. 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Table of Contents

* [Codex comes full circle with GPT-5-Codex agentic finetune](https://sub.thursdai.news/i/173985701/codex-comes-full-circle-with-gpt-codex-agentic-finetune-x-openai-blog)

* [Meta Connect 25 - The new Meta Glasses with Display & a neural control interface](https://sub.thursdai.news/i/173985701/meta-connect-the-new-meta-glasses-with-display-and-a-neural-control-interface)

* [Jeremy Berman: Beating frontier labs to SOTA score on ARC-AGI](https://sub.thursdai.news/i/173985701/jeremy-berman-beating-frontier-labs-to-sota-score-on-arc-agi)

* [This Week’s Buzz: Weave inside W&B models—RL just got x-ray vision](https://sub.thursdai.news/i/173985701/this-weeks-buzz-weave-inside-w-and-b-modelsrl-just-got-x-ray-vision)

* [Open Source](https://sub.thursdai.news/i/173985701/open-source)

* [Perceptron Isaac 0.1 - 2B model that points better than GPT](https://sub.thursdai.news/i/173985701/perceptron-isaac-b-model-that-points-better-than-gpt-x-hf-blog)

* [Tongyi DeepResearch: A3B open-source web agent claims parity with OpenAI Deep Research](https://sub.thursdai.news/i/173985701/tongyi-deepresearch-ab-open-source-web-agent-claims-parity-with-openai-deep-research-x-hf)

* [Reve launches a 4-in-1 AI visual platform taking on Nano 🍌 and Seedream](https://sub.thursdai.news/i/173985701/reve-launches-a-in-ai-visual-platform-taking-on-nano-and-seedream-x-reve-blog)

* [Ray3: Luma’s “reasoning” video model with native HDR, Draft Mode, and Hi‑Fi mastering](https://sub.thursdai.news/i/173985701/ray-lumas-reasoning-video-model-with-native-hdr-draft-mode-and-hifi-mastering-x-try-it)

* [World models are getting closer - Worldlabs announced Marble](https://sub.thursdai.news/i/173985701/world-models-are-getting-closer-worldlabs-announced-marble-demo)

* [Google puts Gemini in Chrome](https://sub.thursdai.news/i/173985701/google-puts-gemini-in-chrome-x-blog)

**Codex comes full circle with GPT-5-Codex agentic finetune **([X](https://x.com/OpenAI/status/1967636903165038708), [OpenAI Blog](https://openai.com/index/introducing-upgrades-to-codex/))

My personal highlight of the week was definitely the release of GPT-5-Codex. I feel like we've come full circle here. I remember when OpenAI first launched a separate, fine-tuned model for coding called Codex, way back in the GPT-3 days. Now, they've done it again, taking their flagship GPT-5 model and creating a specialized version for agentic coding, and the results are just staggering.

This isn't just a minor improvement. During their internal testing, OpenAI saw GPT-5-Codex work independently for more than seven hours at a time on large, complex tasks—iterating on its code, fixing test failures, and ultimately delivering a successful implementation. Seven hours! That's an agent that can take on a significant chunk of work while you're sleeping. It's also incredibly efficient, using 93% fewer tokens than the base GPT-5 on simpler tasks, while thinking for longer on the really difficult problems.

The model is now integrated everywhere - the Codex CLI (just npm install -g codex), VS Code extension, web playground, and yes, even your iPhone. At OpenAI, Codex now reviews the vast majority of their PRs, catching hundreds of issues daily before humans even look at them. Talk about eating your own dog food!

Other OpenAI updates from this week

While Codex was the highlight, OpenAI (and Google) also participated and obliterated one of the world’s hardest algorithmic competitions called ICPC. OpenAI used GPT-5 and an unreleased reasoning model to solve 12/12 questions in under 5 hours. 

OpenAI and NBER also released an incredible report on how over 700M people use GPT on a weekly basis, with a lot of insights, that are summed up in this incredible graph:

**Meta Connect 25 - The new Meta Glasses with Display & a neural control interface**

Just when we thought the week couldn't get any crazier, Zuck took the stage for their annual Meta Connect conference and dropped a bombshell. They announced a new generation of their Ray-Ban smart glasses that include a built-in, high-resolution display you can't see from the outside. This isn't just an incremental update; this feels like the arrival of a new category of device. We've had the computer, then the mobile phone, and now we have smart glasses with a display.

The way you interact with them is just as futuristic. They come with a "neural band" worn on the wrist that reads myoelectric signals from your muscles, allowing you to control the interface silently just by moving your fingers. Zuck's [live demo](https://x.com/altryne/status/1968468021988434054/video/1), where he walked from his trailer onto the stage while taking messages and playing music, was one hell of a way to introduce a product.

This is how Meta plans to bring its superintelligence into the physical world. You'll wear these glasses, talk to the AI, and see the output directly in your field of view. They showed off live translation with subtitles appearing under the person you're talking to and an agentic AI that can perform research tasks and notify you when it's done. It's an absolutely mind-blowing vision for the future, and at $799, shipping in a week, it's going to be accessible to a lot of people. I've already signed up for a demo.

**Jeremy Berman: Beating frontier labs to SOTA score on ARC-AGI**

We had the privilege of chatting with **Jeremy Berman**, who just achieved SOTA on the notoriously difficult ARC-AGI benchmark using *checks notes*... Grok 4! 🚀

He walked us through his innovative approach, which ditches Python scripts in favor of flexible "natural language programs" and uses a program-synthesis outer loop with test-time adaptation. Incredibly, his method achieved these top scores at 1/25th the cost of previous systems

This is huge because ARC-AGI tests for true general intelligence - solving problems the model has never seen before. The chat with Jeremy is very insightful, available on the podcast starting at 01:11:00 so don't miss it!

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

**This Week’s Buzz: Weave inside W&B models—RL just got x-ray vision**

You know how every RL project produces a mountain of rollouts that you end up spelunking through with grep? We just banished that misery. **Weave** tracing now lives natively inside every W&B Workspace run. Wrap your training-step and rollout functions in @weave.op, call weave.init(), and your traces appear alongside loss curves in real time. I can click a spike, jump straight to the exact conversation that tanked the reward, and diagnose hallucinations without leaving the dashboard. If you’re doing any agentic RL, please go treat yourself. Docs: [**https://weave-docs.wandb.ai/guides/tools/weave-in-workspaces**](https://weave-docs.wandb.ai/guides/tools/weave-in-workspaces)

Open Source

Open source did NOT disappoint this week as well, we've had multiple tiny models beating the giants at specific tasks! 

Perceptron Isaac 0.1 - 2B model that points better than GPT ( [X](https://x.com/perceptroninc/status/1968365052270150077), [HF](https://huggingface.co/PerceptronAI/Isaac-0.1), [Blog](https://www.perceptron.inc/blog/introducing-isaac-0-1) )

One of the most impressive demos of the week came from a new lab, Perceptron AI. They released Isaac 0.1, a tiny 2 billion parameter "perceptive-language" model. This model is designed for visual grounding and localization, meaning you can ask it to find things in an image and it will point them out. During the show, we gave it a photo of my kid's Harry Potter alphabet poster and asked it to "find the spell that turns off the light." 

Not only did it correctly identify "Nox," but it drew a box around it on the poster. This little 2B model is doing things that even huge models like GPT-4o and Claude Opus can't, and it's completely open source. Absolutely wild.

Moondream 3 preview - grounded vision reasoning 9B MoE (2B active) ([X](https://x.com/vikhyatk/status/1968800178640429496), [HF](https://huggingface.co/moondream/moondream3-preview))

Speaking of vision reasoning models, just a bit after the show concluded, our friend Vik released a demo of Moondream 3, a reasoning vision model 9B (A2B) that is also topping the charts! I didn't have tons of time to get into this, but the release thread shows this to be an exceptional open source visual reasoner also beating the giants!

Tongyi DeepResearch: A3B open-source web agent claims parity with OpenAI Deep Research ( [X](https://x.com/Ali_TongyiLab/status/1967988004179546451), [HF](https://huggingface.co/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B) )

Speaking of smaller models obliterating huge ones, Tongyi released a bunch of papers and a model this week that can do Deep Research on the level of OpenAI, even beating it, with a Qwen Finetune with only 3B active parameters! 

With insane scores like 32.9 (38.3 in Heavy mode) on Humanity's Last Exam (OAI Deep Research gets 26%) and an insane 98.6% on SimpleQA, this innovative approach uses a lot of RL and synthetic data to train a Qwen model to find what you need. The paper is full of incredible insights into how to build automated RL environments to get to this level. 

AI Art, Diffusion 3D and Video

This category of AI has been blowing up, we've seen SOTA week after week with Nano Banana then Seedream 4 and now a few more insane models.

**Tencent's Hunyuan released SRPO** ([X](https://x.com/TencentHunyuan/status/1967853314915315945), [HF](https://huggingface.co/tencent/SRPO), [Project](https://tencent.github.io/srpo-project-page/), [Comparison X](https://x.com/hellorob/status/1967667203593183343/photo/2))(Semantic Relative Preference Optimization) which is a new method to finetune diffusion models quickly without breaking the bank. Also released a very realistic looking finetune trained with SRPO. Some of the generated results are super realistic, but it's more than just a model, there's a whole new method of finetuning here! 

Hunyuan also updated their 3D model and announced a full blown [3D studio](https://x.com/TencentHunyuan/status/1968711532033851657) that does everything from 3D object generation, meshing, texture editing & more. 

Reve launches a 4-in-1 AI visual platform taking on Nano 🍌 and Seedream ([X](https://x.com/cantrell/status/1967655268642386361), [Reve](https://app.reve.com/), [Blog](https://blog.reve.com/posts/the-new-reve/))

A newcomer, Reve has launched a comprehensive new AI visual platform bundling image creation, editing, remixing, creative assistant, and API integration, all aimed at making advanced editing as accessible, all using their own proprietary models. 

What stood out to me though, is the image editing UI, which allows you to select on your image exactly what you want to edit, write a specific prompt for that thing (change color, objects, add text etc') and then hit generate and their model takes into account all those new queues! This is way better than just ...  text prompting the other models! 

Ray3: Luma’s “reasoning” video model with native HDR, Draft Mode, and Hi‑Fi mastering ([X](https://x.com/LumaLabsAI/status/1968684330034606372), [Try It](https://dream-machine.lumalabs.ai/ideas))

Luma released the third iteration of their video model called Ray, and this one does.. HDR! But it also has Draft Mode (for quick iteration), first/last frame interpolation, and they claim to be "production ready" with extreme prompt adherence. 

The thing that struck me is the reasoning part, their video model is now reasoning, to let you create more complex scenes, while the model will ... evaluate itself and select the best generation for you! This is quite bonkers, can't wait to play with it! 

World models are getting closer - Worldlabs announced Marble  ([Demo](https://x.com/XRarchitect/status/1968356682888823060))

We've covered a whole host of world models, Genie3, Hunyuan 3D world models, Mirage and a bunch more! 

Dr FeiFei's WorldLabs have been one of the first ones to tackle the world model concept and their recent release shows incredible progress (and finally lets us play with it!) 

Marble takes images and creates Gussian Splats, that can be used in 3D environments. So now you can use any AI image generation and turn it into a walkable 3D world! 

Google puts Gemini in Chrome ([X](https://x.com/search?q=gemini%20chrome&src=typed_query), [Blog](https://blog.google/products/chrome/chrome-reimagined-with-ai/))

This happened after the show today and while not fully rolled out yet, I've told you before when we covered Comet from PPXL and Dia from browser company, that Google will not be far behind! 

So today they announced that Gemini is coming to Chrome, and will allow users to chat with a bunch of their tabs, summarize across tabs and soon do agentic tasks like clicking things and shopping for you? 😅

I wonder if this means that Google will offer this for free to the over 1B chrome users or introduce some sort of Gemini tier cross-over? Remains to be seen but very exciting to see AI browsers all over! 

The best feature could be a hidden one, where the Gemini in Chrome will have knowledge about your surfing history and you'll be able to ask it about that one website you visited a while ago that had sharks! 

Folks, I can go on and on today, literally there's a new innovative video model from ByteDance, a few more image models, but alas, I have to prioritize and give you only the top important news. So, I'll just remind that I put all the links in the TL;DR below and that you should absolutely check out the video version of our show on YT because a lot of visual things are happening and we're playing with all of them live! 

Hey, just before you get to the “links”, consider subscribing to help me keep this going? 🙏

See you next week 🫡 Don't forget to subscribe (and if you already subbed, share this with a friend or two?) 

TL;DR and show notes - September 18, 2025

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@ldjconfirmed](http://x.com/ldjconfirmed) [@nisten](http://x.com/nisten)

* Guest : Jeremy Berman ([@jerber888](https://x.com/jerber888)) - SOTA on ARC- AGI

* **Open Source**

* Perceptron AI introduces Isaac 0.1: a 2B param perceptive-language model ([X](https://x.com/perceptroninc/status/1968365052270150077), [HF](https://huggingface.co/PerceptronAI/Isaac-0.1), [Blog](https://www.perceptron.inc/blog/introducing-isaac-0-1))

* Tongyi DeepResearch: A3B open-source web agent claims parity with OpenAI Deep Research ([X](https://x.com/Ali_TongyiLab/status/1967988004179546451), [HF](https://huggingface.co/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B))

* Mistral updates Magistral-Small-2509 ([HF](https://huggingface.co/mistralai/Magistral-Small-2509))

* **Big CO LLMs + APIs**

* GPT-5-Codex release: Agentic coding upgrade for Codex ([X](https://x.com/OpenAI/status/1967636903165038708), [OpenAI Blog](https://openai.com/index/introducing-upgrades-to-codex/))

* Meta Connect - New AI glasses with display, new AI mode ([X Recap](https://x.com/lukegotbored/status/1968497570008744149))

* NBER & OpenAI - How People Use ChatGPT: Growth, Demographics, and Scale ([X](https://twitter.com/rohanpaul_ai/status/1967769809929822659), [Blog](https://forklightning.substack.com/p/how-people-use-chatgpt), [NBER Paper](https://www.nber.org/papers/w34255))

* ARC-AGI: New SOTA by Jeremy Berman and Eric Pang using Grok-4 ([X](https://x.com/arcprize/status/1967998885701538060), [Blog](https://jeremyberman.substack.com/p/how-i-got-the-highest-score-on-arc-agi-again))

* OpenAI’s reasoning system aces 2025 ICPC World Finals with a perfect 12/12 ([X](https://x.com/MostafaRohani/status/1968360976379703569))

* OpenAI adds thinking budgets to ChatGPT app ([X](https://x.com/OpenAI/status/1968395215536042241))

* Gemini in Chrome: AI assistant across tabs + smarter omnibox + safer browsing ([X](https://x.com/search?q=gemini%20chrome&src=typed_query), [Blog](https://blog.google/products/chrome/chrome-reimagined-with-ai/))

* Anthropic admits **Claude bugs** - [Detailed analysis](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues) 

* **This weeks Buzz**

* W&B Models + Weave! You can now log your RL runs in W&B Weave 👏 ([X](https://x.com/shawnup/status/1968403633764266189), [W&B Link](https://weave-docs.wandb.ai/guides/tools/weave-in-workspaces)) 

* W&B Fully Connected London - tickets are running out! Use FCLNTHURSAI for a free ticket on me! ([Register Here](https://wandb.ai/site/resources/events/fully-connected/london/))

* **Vision & Video**

* Moondream 3 (Preview): 9B MoE VLM with 2B active targets frontier-level visual reasoning ([X](https://x.com/vikhyatk/status/1968800178640429496), [HF](https://huggingface.co/moondream/moondream3-preview))

* Ray3: Luma’s “reasoning” video model with native HDR, Draft Mode, and Hi‑Fi mastering ([X](https://x.com/LumaLabsAI/status/1968684330034606372))

* HuMo: human‑centric, multimodal video gen from ByteDance/Tsinghua ([X](https://x.com/altryne/status/1968003981604733359), [HF](https://huggingface.co/bytedance-research/HuMo))

* **Voice & Audio**

* Reka Speech: high-throughput multilingual ASR and speech translation for batch-scale pipelines ([X](https://x.com/RekaAILabs/status/1967989101111722272), [Blog](https://reka.ai/news/reka-speech-high-throughput-speech-transcription-and-translation-model-with-timestamps))

* **AI Art & Diffusion & 3D**

* Hunyuan SRPO (Semantic Relative Preference Optimization) supercharges diffusion models ([X](https://x.com/TencentHunyuan/status/1967853314915315945), [HF](https://huggingface.co/tencent/SRPO), [Project](https://tencent.github.io/srpo-project-page/), [Comparison X](https://x.com/hellorob/status/1967667203593183343/photo/2))

* Hunyuan 3D 3.0 ([X](https://x.com/TencentHunyuan/status/1967873084960260470), [Try it](https://3d.hunyuan.tencent.com/))

* FeiFei WorldLabs presents Marble ([Demo](https://x.com/XRarchitect/status/1968356682888823060))

* Reve launches 4-in-1 AI visual platform ([X](https://x.com/cantrell/status/1967655268642386361), [Reve](https://app.reve.com/), [Blog](https://blog.reve.com/posts/the-new-reve/))

* **Tools**

* Chrome adds Gemini ([Blog](https://blog.google/products/chrome/new-ai-features-for-chrome/)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-sep-18-gpt-5-codex-oai-wins/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-sep-18-gpt-5-codex-oai-wins?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3Mzk4NTcwMSwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.SLrL0wXQSTkZ9DJnmPZ2NocV7zsw_Q24wCyURXRnwqo&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Sep 11 - SeeDream 4, Lucy 14B, ChatGPT gets MCP, OpenAI $300B deal with Oracle, Qwen Next A3B & more AI news

**Date:** September 12, 2025  
**Duration:** 1:34:28  
**Link:** [https://sub.thursdai.news/p/sep-11](https://sub.thursdai.news/p/sep-11)

Hey Everyone, Alex here, thanks for being a subscriber! Let's get you caught up on this weeks most important AI news! 

The main thing you need to know this week is likely the incredible Image model that ByteDance released, that overshoots the (incredible image model from last 2 weeks) nano 🍌. ByteDance really outdid themselves on this one! 

But also, a video model with super fast generation, OpenAI rumor made Larry Ellison the richest man alive, ChatGPT gets MCP powers (under a flag you can enable) and much more! 

This week we covered a lot of visual stuff, so while the podcast format is good enough, it's really worth tuning in to the video recording to really enjoy the full show. 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

AI Art and Diffusion

It's rare for me to start the newsletter not on Open Source AI news, but hey, at least this way you know that I'm writing it and not some AI right? 😉

ByteDance SeeDream 4 - 4K SOTA image generation and editing model with up to 6 reference images ([Fal](https://fal.ai/models/fal-ai/bytedance/seedream/v4/edit/requests), [Replicate](https://replicate.com/bytedance/seedream-4))

The level of detail on ByteDance's new model, has really made all the hosts on ThursdAI stop and go... huh? is this AI? Bytedance really outdid themselves with this image model that not only generates images, it also is a fully functional image editing with natural language model. It's a diffusion transformer, able to generate 2K and 4K images, fast (under 5 seconds?) while enabling up to 6 reference images to be provided for the generation. 

This is going to be incredible for all kinds of purposes, AI art, marketing etc'. The promt adherence is quite incredible, text is also crisp and sharp at those 2/4K resolutions. We created this image live on the show with it (using a prompt extended by another model)

I then provided my black and white headshot and the above image and asked to replace me as a cartoon character, and it did, super quick, and even got my bomber jacket and the W&B logo on it in there! Notable, nothing else was changed in the image, showing just how incredible this one is for image editing. 

In you want enhanced realism, our friend FoFr from replicate, reminded us that using IMG_3984.CR2 in the prompt, will make the model show images that are closer to reality, even if they depict some incredibly unrealistic things, like a pack of lions forming his nickname

Additional uses for this model are just getting discovered, and one user already noted that given this model outputs 4K resolution, it can be used as a [creative upscaler](https://x.com/BrentLynch/status/1965922591497134319) for other model outputs. Just shove your photo from another AI in Seedream and ask for an upscale. Just be ware that creative upscalers change some amount of details in the generated picture. 

**DecART AI Lucy 14B Redefines Video Generation speeds! **

If Seedteam blew my mind with images, Decart's Lucy 14B absolutely shattered my expectations for video generation speed. We're talking about generating 5-second videos from images in 6.5 seconds. That's almost faster than watching the video itself!

This video model is not open source yet (despite them adding 14B to the name) but it's smaller 5B brother was open sourced. The speed to quality ratio is really insane here, and while Lucy will not generate or animate text or faces that well, it does produce some decent imagery, but SUPER fast. This is really great for iteration, as AI Video is like a roulette machine, you have to generate a lot of tries to see a good result. 

This paired with Seedream (which is also really fast) are a game changer in the AI Art world! So stoked to see what folks will be creating with these! 

**Bonus Round: Decart's Real-Time Minecraft Mod for Oasis 2 (**[**X**](https://x.com/DecartAI/status/1963758685995368884)**)**

The same team behind Lucy also dropped Oasis 2.0, a Minecraft mod that generates game environments in real-time using diffusion models. I got to play around with it live, and watching Minecraft transform into different themed worlds as I moved through them was surreal.

Want a steampunk village? Just type it in. Futuristic city? Done. The frame rate stayed impressively smooth, and the visual coherence as I moved through the world was remarkable. It's like having an AI art director that can completely reskin your game environment on demand. And while the current quality remains low res, if you consider where Stable Diffusion 1.4 was 3 years ago, and where Seedream 4 is now, and do the same extrapolation to Oasis, in 2-3 years we'll be reskinning whole games on the fly and every pixel will be generated (like Jensen loves to say!) 

**OpenAI adds full MCP to ChatGPT (under a flag) **

This is huge, folks. I've been waiting for this for a while, and finally, OpenAI quietly added full MCP (Model Context Protocol) support to ChatGPT via a hidden "developer mode."

**How to Enable MCP in ChatGPT**

Here's the quick setup I showed during the stream:

* Go to ChatGPT settings → Connectors

* Scroll down to find "Developer Mode" and enable it

* Add MCP servers (I used Rube.ai from Composio)

* Use GPT-4o in developer mode to access your connectors

During the show, I literally had ChatGPT pull Nisten's last five tweets using the Twitter MCP connector. It worked flawlessly (though Nisten was a bit concerned about what tweets it might surface 😂).

The implications are massive - you can now connect ChatGPT to GitHub, databases, your local files, or chain multiple tools together for complex workflows. As Wolfram pointed out though, watch your context usage - each MCP connector eats into that 200K limit.

**Big Moves: Investments and Infrastructure**

Speaking of OpenAI, Let's talk money, because the stakes are getting astronomical. OpenAI reportedly has a $300 billion (!) deal with Oracle for compute infrastructure over five years, starting in 2027. That's not a typo - $60 billion per year for compute. Larry Ellison just became the world's richest person, and Oracle's stock shot up 40% on the news in just a few days! This has got to be one of the biggest compute deals the world has ever head of!

The scale is hard to comprehend. We're talking about potentially millions of H100 GPUs worth of compute power. When you consider that most AI companies are still figuring out how to profitably deploy thousands of GPUs, this deal represents infrastructure investment at a completely different magnitude.

Meanwhile, Mistral just became Europe's newest decacorn, valued at $13.8 billion after receiving $1.3 billion from ASML. For context, ASML makes the lithography machines that TSMC uses to manufacture chips for Nvidia. They're literally at the beginning of the AI chip supply chain, and now they're investing heavily in Europe's answer to OpenAI.

Wolfram made a great point - we're seeing the emergence of three major AI poles: American companies (OpenAI, Anthropic), Chinese labs (Qwen, Kimi, Ernie), and now European players like Mistral. Each is developing distinct approaches and capabilities, and the competition is driving incredible innovation.

**Anthropic's Mea Culpa and Code Interpreter**

After weeks of users complaining about Claude's degraded performance, Anthropic finally admitted there were bugs affecting both Claude Opus and Sonnet. Nisten, who tracks these things closely, speculated that the issues might be related to running different quantization schemes on different hardware during peak usage times. We already reported last week that they admitted that "something was affecting intelligence" but this week they said they pinpointed (and fixed) 2 bugs realted to inference! 

They also launched a code interpreter feature that lets Claude create and edit files directly. It's essentially their answer to ChatGPT's code interpreter - giving Claude its own computer to work with. The demo showed it creating Excel files, PDFs, and documents with complex calculations. Having watched Claude struggle with file operations for months, this is a welcome addition.

**🐝 This Week's Buzz: GLM 4.5 on W&B and We're on Open Router!**

Over at Weights & Biases, we've got some exciting updates for you. First, we've added Zhipu AI's GLM 4.5 to [W&B Inference](http://wandb.me/inference)! This 300B+ parameter model is an absolute beast for coding and tool use, ranking among the top open models on benchmarks like SWE-bench. We've heard from so many of you, including Nisten, about how great this model is, so we're thrilled to host it. You can try it out now and get $2 in free credits to start.

And for all you developers out there, you can [use a proxy](https://x.com/olafgeibig/status/1949779562860056763) like LiteLLM to run GLM 4.5 from our inference endpoint inside Anthropic's Claude Code if you're looking for a powerful and cheap alternative! 

Second, we're now on Open Router! You can find several of our hosted models, like GPT-4-OSS and DeepSeek Coder, on the platform. If you're already using Open Router to manage your model calls, you can now easily route traffic to our high-performance inference stack.

**Open Source Continues to Shine**

Open Source LLM models took a bit of a break this week, but there were still interesting models! 

Baidu released ERNIE-4.5, a very efficient 21B parameter "thinking" MoE that only uses 3B active parameters per token. From the UAE, MBZUAI released K2-Think, a finetune of Qwen 2.5 that's showing some seriously impressive math scores. And Moonshot AI updated Kimi K2, doubling its context window to 256K and further improving its already excellent tool use and writing capabilities.

Tencent released an update to HunyuanImage 2.1, which is a bit slow, but also generates 2K images and is decent at text. 

Qwen drops Qwen3-**Next**-80B-A3B ([X](https://x.com/Alibaba_Qwen/status/1966197643904000262), [HF](https://t.co/zHHNBB2l5X))

In breaking news post the show (we were expecting this on the show itself), Alibaba folks dropped a much more streamlined version of the next Qwen, 80B parametes with only 3B active! They call this an "Ultra Sparse MOE" and it beats Qwen3-32B in perf, rivals Qwen3-235B in reasoning & long-context. 

This is quite unprecedented, as getting models as sparse as to work well takes a lot of effort and skill, but the Qwen folks delivered! 

Tools

We wrapped with a quick shoutout to EBSynth, a nifty video editor that lets you draw or add elements to one frame and extrapolates to the rest—like Photoshop for motion. It's browser-based and fun for VFX tweaks; check the demo video on [X](https://twitter.com/ebsynth/status/1965448361974362432). Simple but powerful for quick video hacks. Speaking of Photoshop, it was confirmed that Nano Banana is going to be embedded into Photoshop for image editing! 

Summary & TL;DR

What a week—Seedream and Lucy alone have me rethinking how fast AI can iterate creatively, while MCP in ChatGPT feels like the dawn of truly accessible agents. With open-source keeping pace and big deals fueling the fire, AI's multimodal future is accelerating. Thanks for tuning in, folks; if you missed the live vibes, catch the podcast or hit [sub.thursdai.news](sub.thursdai.news) for all the links. See you next Thursday—what blew your mind this week? Drop a comment and share with a friend, it's the best way to support this endeavor! 

TL;DR of all topics covered:

**AI Models & APIs:**

* **ChatGPT adds full MCP support** - Developer mode unlocks tool connectors for 400M+ users ([Setup Guide](https://x.com/altryne/status/1965843358653481450))

* **Sea Dream 4.0** - ByteDance's unified image generation/editing model creates 4K images in ~1.8 seconds ([X](https://x.com/fofrAI/status/1942899932505035222), [Try it](https://fal.ai/models/fal-ai/bytedance/seedream/v4/edit/playground))

* **Lucy 14B** - Decart's lightning-fast video model generates 5-second clips in 6.5 seconds ([Demo](https://fal.ai/models/decart/lucy-14b/image-to-video), [Page](https://lucy.decart.ai/))

* **Claude bug fixes** - Anthropic admits to performance issues and releases code interpreter ([Blog](https://www.anthropic.com/news/create-files))

* **Sonoma Dusk & Sky** - Mystery models on OpenRouter with 2M context, rumored to be Grok ([OpenRouter](https://openrouter.ai/openrouter/sonoma-sky-alpha))

**This Week's W&B Buzz:**

* **OpenRouter integration** - Serving models to broader developer community ([Try us](https://openrouter.ai/provider/wandb))

* **GLM 4.5** - 350B parameter coding model added to inference ([X](https://x.com/weights_biases/status/1965176118413344778), [Try It](https://wandb.ai/site/inference/glm-4.5))

* W&B inference in Claude Code with LiteLLM ([Olaf's Guide](https://x.com/olafgeibig/status/1949779562860056763))

**Open Source Releases:**

* **ERNIE 4.5** - Baidu open-sources 21B parameter thinking model with 3B active parameters ([X](https://x.com/Baidu_Inc), [HF](https://huggingface.co/baidu/ERNIE-4.5-21B-A3B-Thinking))

* **K2-think** - MBZUAI's Qwen 2.5 fine-tune with strong math performance ([X](https://x.com/ericxing/status/1965667372284739977))

* **Kimi K2 update** - Doubled context to 256K, improved tool use ([X](https://x.com/LechMazur/status/1965729450940588459))

* **HunyuanImage 2.1** - Tencent's 17B parameter open-source 2K image model ([X](https://x.com/TencentHunyuan/status/1965433678261354563), [HF](https://huggingface.co/tencent/HunyuanImage-2.1))

* Qwen-next-80B-A3B - Alibaba's next frontier MoE with 3B active param ([X](https://x.com/Alibaba_Qwen/status/1966197643904000262), [HF](https://t.co/zHHNBB2l5X))

**Voice & Audio:**

* **Qwen3-ASR-Flash** - 11-language speech recognition with singing support ([X](https://x.com/Alibaba_Qwen/status/1965068737297707261))

* **Stable Audio 2.5** - Enterprise audio generator creating 3-minute tracks in <2 seconds ([X](https://twitter.com/StabilityAI/status/1965784409052995916), [Blog](https://stability.ai/news/stability-ai-introduces-stable-audio-25-the-first-audio-model-built-for-enterprise-sound-production-at-scale), [Try It](https://stableaudio.com/generate))

* **ElevenLabs Voice Remixing** - Modify cloned voices for age, gender, accent ([X](https://x.com/elevenlabsio))

**Business & Investment:**

* **OpenAI-Oracle deal** - $300B infrastructure agreement over 5 years

* **Mistral funding** - $1.3B investment from ASML at $13.8B valuation ([Blog](https://www.cnbc.com/2025/09/09/ai-firm-mistral-valued-at-14-billion-as-asml-takes-major-stake.html))

**Tools:**

* **Oasis 2.0** - Real-time Minecraft world generation mod from Decart ([Try It](http://oasis2.decart.ai/demo))

* **EbSynth** - Video editing tool for frame-by-frame manipulation ([X](https://x.com/ebsynth/status/1965448361974362432))

**Hosts:**

* Alex Volkov ([@altryne](https://x.com/altryne))

* Wolfram RavenWlf ([@WolframRvnwlf](https://x.com/WolframRvnwlf))

* Yam Peleg ([@yampeleg](https://x.com/yampeleg))

* Nisten ([@nisten](https://x.com/nisten))

* LDJ ([@ldjconfirmed](https://x.com/ldjconfirmed)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/sep-11/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/sep-11?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3MzM5ODg1NiwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.SMx-Bbivol8nWte1LRp1keyHr7-aYnhSkNZ0C8Aa5_w&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Sep 4 - Codex Rises, Anthropic Raises $13B, Nous plays poker, Apple speeds up VLMs & more AI news

**Date:** September 05, 2025  
**Duration:** 1:38:00  
**Link:** [https://sub.thursdai.news/p/thursdai-sep-4-codex-rises-anthropic](https://sub.thursdai.news/p/thursdai-sep-4-codex-rises-anthropic)

Wohoo, hey ya’ll, Alex here,

I'm back from the desert (pic at the end) and what a great feeling it is to be back in the studio to talk about everything that happened in AI! 

It's been a pretty full week (or two) in AI, with Coding agent space heating up, Grok entering the ring and taking over free tokens, Codex 10xing usage and Anthropic... well, we'll get to Anthropic. 

Today on the show we had Roger and Bhavesh from Nous Research cover the awesome Hermes 4 release and the new PokerBots benchmark, then we had a returning favorite, Kwindla Hultman Kramer, to talk about the GA of RealTime voice from OpenAI. 

Plus we got some massive funding news, some drama with model quality on Claude Code, and some very exciting news right here from CoreWeave aquiring OpenPipe! 👏 So grab your beverage of choice, settle in (or skip to the part that interests you) and let's take a look at the last week (or two) in AI! 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

**Open Source: Soulful Models and Poker-Playing Agents**

This week did not disappoint as it comes to Open Source! Our friends at Nous Research released the 14B version of Hermes 4, after releasing the 405B and 70B versions last week. This company continues to excel in finetuning models for powerful, and sometimes just plain weird (in a good way) usecases. 

**Nous Hermes 4 (14B, 70B, 405B) and the Quest for a "Model Soul" (**[**X**](https://x.com/NousResearch/status/1960416954457710982)**, **[**HF**](https://huggingface.co/NousResearch/Hermes-4-14B)**)**

Roger and Bhavash from Nous came to announce the release of the smaller (14B) version of Hermes 4, and cover the last weeks releases of the larger 70B and 405B brothers. Hermes series of finetunes was always on our radar, as unique data mixes turned them into uncensored, valuable and creative models and unlocked a bunch of new use-cases. 

But the wildest part? They told us they intentionally *stopped *training the model not when reasoning benchmarks plateaued, but when they felt it started to "lose its model soul." They monitor the entropy and chaos in the model's chain-of-thought, and when it became too sterile and predictable, they hit the brakes to preserve that creative spark. This focus on qualities beyond raw benchmark scores is why Hermes 4 is showing some really interesting generalization, performing exceptionally well on benchmarks like EQBench3, which tests emotional and interpersonal understanding. It's a model that's primed for RL not just in math and code, but in creative writing, role-play, and deeper, more "awaken" conversations. It’s a soulful model that's just fun to talk to.

**Nous Husky Hold'em Bench: Can Your LLM Win at Poker? (**[**Bench**](https://huskybench.com/)**)**

As if a soulful model wasn't enough, the Nous team also dropped one of the most creative new evals I've seen in a while: **Husky Hold'em Bench**. We had Bhavesh, one of its creators, join the show to explain. This isn't a benchmark where the LLM plays poker directly. Instead, the LLM has to *write a Python poker bot*from scratch, under time and memory constraints, which then competes against bots written by other LLMs in a high-stakes tournament. Very interesting approach, and we love creative benchmarking here at ThursdAI! 

This is a brilliant way to test for true strategic reasoning and planning, not just pattern matching. It's an "evergreen" benchmark that gets harder as the models get better. Early results are fascinating: Claude 4 Sonnet and Opus are currently leading the pack, but Hermes 4 is the top open-source model.

**More Open Source Goodness**

The hits just kept on coming this week. **Tencent** open-sourced **Hunyuan-MT-7B**, a translation model that swept the WMT2025 competition and rivals GPT-4.1 on some benchmarks. Having a small, powerful, specialized model like this is huge for anyone doing large-scale data translation for training or needing fast on-device capabilities.

From Switzerland, we got **Apertus-8B and 70B**, a set of fully open (Apache 2.0 license, open data, open training recipes!) multilingual models trained on a massive 15 trillion tokens across 1,800 languages. It’s fantastic to see this level of transparency and contribution from European institutions.

And **Alibaba’s Tongyi Lab** released **WebWatcher**, a powerful multimodal research agent that can plan steps, use a suite of tools (web search, OCR, code interpreter), and is setting new state-of-the-art results on tough visual-language benchmarks, often beating models like GPT-4o and Gemini.

All links are in the TL;DR at the end

**BREAKING NEWS: Google Drops Embedding Gemma 308M (**[**X**](https://x.com/GoogleDeepMind/status/1963635422698856705)**, **[**HF**](https://huggingface.co/google/embeddinggemma-300m)**, **[**Try It**](https://huggingface.co/spaces/webml-community/semantic-galaxy)**)**

Just as we were live on the show, news broke from our friends at Google. They've released **Embedding Gemma**, a new family of open-source embedding models. This is a big deal because they are *tiny*—the smallest is only 300M parameters and takes just 200MB to run—but they are topping the MTEB leaderboard for models under 500M parameters. For anyone building RAG pipelines, especially for on-device or mobile-first applications, having a small, fast, SOTA embedding model like this is a game-changer.

It's so optimized for on device running that it can run fully in your browser on WebGPU, with [this great example](https://huggingface.co/spaces/webml-community/semantic-galaxy) from our friend Xenova highlighted on the release blog! 

**Big Companies, Big Money, and Big Problems**

It was a rollercoaster week for the big labs, with massive fundraising, major product releases, and a bit of a reality check on the reliability of their services.

**OpenAI's GPT Real-Time Goes GA and gets an upgraded brain (**[**X**](https://x.com/OpenAIDevs/status/1961124915719053589)**, **[**Docs**](https://openai.com/index/introducing-gpt-realtime/#image-input)**)**

We had the perfect guest to break down OpenAI's latest voice offering: Kwindla Kramer, founder of Daily and maintainer of the open-source PipeCat framework. OpenAI has officially taken its **Realtime API to General Availability (GA)**, centered around the new gpt-realtime model.

Kwindla explained that this is a true speech-to-speech model, not a pipeline of separate speech-to-text, LLM, and text-to-speech models. This reduces latency and preserves more nuance and prosody. The GA release comes with huge upgrades, including support for remote MCP servers, the ability to process image inputs during a conversation, and—critically for enterprise—native SIP integration for connecting directly to phone systems.

However, Kwindla also gave us a dose of reality. While this is the future, for many high-stakes enterprise use cases, the multi-model pipeline approach is still more reliable. Observability is a major issue with the single-model black box; it's hard to know exactly what the model "heard." And in terms of raw instruction-following and accuracy, a specialized pipeline can still outperform the speech-to-speech model. It’s a classic jagged frontier: for the lowest latency and most natural vibe, GPT Real-Time is amazing. For mission-critical reliability, the old way might still be the right way for now.

ChatGpt has branching! 

Just as I was about to finish writing this up, ChatGPT announced a new feature, and this one I had to tell you about! Finally you can branch chats in their interface, which is a highly requested feature! 

Branching seems to be live on the chat interface, and honestly, tiny but important UI changes like these are how OpenAI remains the best chat experience! 

**The Money Printer Goes Brrrr: Anthropic's $13B Raise**

Let's talk about the money. Anthropic announced it has raised an absolutely staggering **$13 billion in a Series F round, valuing the company at $183 billion**. Their revenue growth is just off the charts, jumping from a run rate of around $1 billion at the start of the year to over $5 billion by August. This growth is heavily driven by enterprise adoption and the massive success of Claude Code. It's clear that the AI gold rush is far from over, and investors are betting big on the major players. In related news, OpenAI is also reportedly raising $10 billion at a valuation of around $500 billion, primarily to allow employees to sell shares—a huge moment for the folks who have been building there for years.

**Oops... Did We Nerf Your AI? Anthropic's Apology**

While Anthropic was celebrating its fundraise, it was also dealing with a self-inflicted wound. After days of users on X and other forums complaining that Claude Opus felt "dumber," the company finally issued a statement admitting that yes, for about three days, the model's quality was degraded due to a change in their infrastructure stack.

Honestly, this is not okay. We're at a point where hundreds of thousands of developers and businesses rely on these models as critical tools. To have the quality of that tool change under your feet without any warning is a huge problem. It messes with people's ability to do their jobs and trust the platform. While it was likely an honest mistake in pursuit of efficiency, it highlights a fundamental issue with closed, proprietary models. You're at the mercy of the provider. It's a powerful argument for the stability and control that comes with open-source and self-hosted models. These companies need to realize that they are no longer just providing experimental toys; they're providing essential infrastructure, and that comes with a responsibility for stability and transparency.

**This Week's Buzz: CoreWeave Acquires OpenPipe! 🎉**

Super exciting news from the Weights & Biases and CoreWeave family - we've acquired OpenPipe! Kyle and David Corbett and their team are joining us to help build out the complete AI infrastructure stack from metal to model.

OpenPipe has been doing incredible work on SFT and RL workflows with their open source ART framework. As Yam showed during the show, they demonstrated you can train a model to SOTA performance on deep research tasks for just $300 in a few hours - and it's all automated! The system can generate synthetic data, apply RLHF, and evaluate against any benchmark you specify.

This fits perfectly into our vision at CoreWeave - bare metal infrastructure, training and observability with Weights & Biases, fine-tuning and RL with OpenPipe's tools, evaluation with Weave, and inference to serve it all. We're building the complete platform, and I couldn't be more excited!

**Vision & Speed: Apple's FastVLM (**[HF](https://huggingface.co/apple/FastVLM-1.5B-int8)**)**

Just before Apple's event next week, they dropped FastVLM - a speed-first vision model that's 85x faster on time-to-first-token than comparable models. They released it in three sizes (7B, 1.5B, and 0.5B), all optimized for on-device use.

The demo that blew my mind was real-time video captioning running in WebGPU. HF CEO Clem showed it processing Apple's keynote video with maybe 250ms latency - the captions were describing what was happening almost in real-time. When someone complained it wasn't accurate because it described "an older man in headphones" when showing an F1 car, Clem pointed out that was actually the previous frame showing Tim Cook - the model was just slightly behind!

**Tools Showdown: Codex vs Claude Code**

To wrap up, we dove into the heated debate between Codex and Claude Code. Sam Altman reported that Codex usage is up **10x in the past two weeks** (!) and improvements are coming. Yam gave us a live demo, and while Claude Code failed to even start up during the show (highlighting why people are switching), Codex with GPT-5 was smooth as butter.

The key advantages? Codex authenticates with your OpenAI account (no API key juggling), it has MCP support, and perhaps most importantly - it's not just a CLI tool. You can use it for PR reviews on GitHub, as a cloud-based agent, and integrated into Cursor and Windsurf. Though as Yam pointed out, OpenAI really needs to stop calling everything "Codex" - there are like five different products with that name now! 😅

If you're tried Codex (the CLI!) when it was released, and gave up, give it a try now, it's significantly upgraded! 

Ok, phew, what a great episode we had, if you're only reading, I strongly recommend checking out the live recording or the edited podcast, and of course, if this newsletter is helpful to you, the best way you can do to support it is to subscribe, and share with friends 👏 

P.S - Just came back after my first burning man, it was a challenging, all consuming experience, where I truly disconnected for the first time (first ThursdAI in over 2 years that I didn't know what's going on with AI). It was really fun but I'm happy to =be back! See you next week! 

TL;DR and Show Notes

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@yampeleg](http://x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed)

* Guests - Roger Jin - [@rogershijin](https://x.com/rogershijin) & Bhavesh Kumar [@bha_ku21](https://x.com/bha_ku21)

* Kwindla Kramer - [@kwindla](https://x.com/kwindla)

* **Open Source LLMs**

* Nous Hermes 4 — 14B launches: compact hybrid reasoning model with tool calling for local and cloud use ([X](https://twitter.com/NousResearch/status/1963349882837897535), [HF](https://huggingface.co/NousResearch/Hermes-4-14B), [Tech Report](https://arxiv.org/pdf/2508.18255))

* Tencent open-sources Hunyuan-MT-7B translation model after sweeping WMT2025 ([X](https://x.com/TencentHunyuan/status/1962466712378577300), [HF](https://huggingface.co/tencent/Hunyuan-MT-7B))

* Nous - Husky Hold'em Bench launches as an open-source pokerbot eval for LLM strategic play ([X](https://x.com/NousResearch/status/1963371292318749043), [Bench](https://huskybench.com/))

* WebWatcher: Alibaba's Tongyi Lab open-sources a vision-language deep research agent that sets new SOTA ([X](https://x.com/rohanpaul_ai/status/1963018720571462029), [HF](https://huggingface.co/Alibaba-NLP/WebWatcher-32B))

* Apertus-8B and 70B launch as Switzerland's fully open, multilingual LLMs trained on 15T tokens across 1,800+ languages ([X](https://x.com/haeggee/status/1962898537294749960), [HF](https://huggingface.co/swiss-ai))

* Google releases Embedding Gemma - 300M param SOTA embeddings model for RAG ([Breaking News])

* **Big CO LLMs + APIs**

* Mistral adds 20+ MCP-powered connectors and controllable Memories to Le Chat for enterprise workflows ([X](https://x.com/MistralAI/status/1962881086440038545), [Blog](https://mistral.ai/news/le-chat-mcp-connectors-memories))

* Anthropic raises $13B Series F at a $183B post-money valuation ([X](https://x.com/AnthropicAI/status/1962909475594985935), [Blog](https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation))

* OpenAI fundraises $10B at ~$500B valuation - buyback for employees

* OpenAI ships gpt-realtime and takes Realtime API to GA with remote MCP tools, image input, and SIP phone calling ([X](https://x.com/OpenAI))

* OpenAI releases projects for free users with larger file uploads and project-only memory controls

* OpenAI acquires Statsig & Alex for $1.1B+ to strengthen applications team

* Grok Code 1 - now taking 50% of coding traffic on OpenRouter

* Codex usage up 10x in 2 weeks per Sam Altman, with improvements coming

* Anthropic admits to Claude Opus quality degradation for 3 days due to infrastructure changes

* **This weeks Buzz**

* CoreWeave buys OpenPipe! 🎉 ([Blog](https://openpipe.ai/blog/openpipe-coreweave))

* **Vision & Video**

* Apple's FastVLM-7B lands with speed-first vision encoder—85x faster TTFT vs peers ([X](https://x.com/_akhaliq/status/1962018549674684890), [HF](https://huggingface.co/apple/FastVLM-7B-int4))

* **AI Art & Diffusion & 3D**

* Nano Banana (Imagen 3) continues to dominate as Google's best image model ([ai.studio/banana](http://ai.studio/banana))

* **Tools**

* Codex vs Claude Code discussion → Codex now significantly better with GPT-5 engine, GitHub PR reviews, and cloud agents 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-sep-4-codex-rises-anthropic/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-sep-4-codex-rises-anthropic?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3MjgyMzQ3NiwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.NCvmcn0BBO-peWq7-zLUrpeQ8n94zZrpzIAlfuj75ZQ&utm_campaign=CTA_5).

---

