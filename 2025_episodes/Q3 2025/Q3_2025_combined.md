# ThursdAI Episodes - Q3 2025

Total Episodes: 12

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

## 📆 ThursdAI - July 24, 2025 - Qwen-mas in July, The White House's AI Action Plan & Math Olympiad Gold for AIs + coding a 3d tetris on stream

**Date:** July 24, 2025  
**Duration:** 1:43:23  
**Link:** [https://sub.thursdai.news/p/thursdai-july-24-2025-qwen-mas-in](https://sub.thursdai.news/p/thursdai-july-24-2025-qwen-mas-in)

What a WEEK! Qwen-mass in July. Folks, AI doesn't seem to be wanting to slow down, especially Open Source! This week we see yet another jump on SWE-bench verified (3rd week in a row?) this time from our friends at Alibaba Qwen. 

Was a pleasure of mine to host Junyang Lin from the team at Alibaba to come and chat with us about their incredible release with, with not 1 but three new models! 

Then, we had a great chat with Joseph Nelson from Roboflow, who not only dropped additional SOTA models, but was also in Washington at the annocement of the new AI Action plan from the WhiteHouse. 

Great conversations this week, as always, TL;DR in the end, tune in! 

Open Source AI - QwenMass in July

This week, the open-source world belonged to our friends at Alibaba Qwen. They didn't just release one model; they went on an absolute tear, dropping bomb after bomb on the community and resetting the state-of-the-art multiple times.

**A "Small" Update with Massive Impact: Qwen3-235B-A22B-Instruct-2507**

Alibaba called this a *minor* refresh of their 235B parameter mixture-of-experts.

Sure—if you consider +13 points on GPQA, 256K context window minor. The 2507 drops hybrid thinking. Instead, Qwen now ships separate instruct and chain-of-thought models, avoiding token bloat when you just want a quick answer. Benchmarks? 81 % MMLU-Redux, 70 % LiveCodeBench, new SOTA on BFCL function-calling. All with 22 B active params.

Our friend of the pod, and head of development at Alibaba Qwen, Junyang Lin, join the pod, and talked to us about their decision to uncouple this model from the hybrid reasoner Qwen3.

"After talking with the community and thinking it through," he said, "we decided to stop using hybrid thinking mode. Instead, we'll train instruct and thinking models separately so we can get the best quality possible."

The community felt the hybrid model sometimes had conflicts and didn't always perform at its best. So, Qwen delivered a pure non-reasoning instruct model, and the results are staggering. Even without explicit reasoning, it's crushing benchmarks. Wolfram tested it on his MMLU-Pro benchmark and it got the top score of all open-weights models he's ever tested. Nisten saw the same thing on medical benchmarks, where it scored the highest on MedMCQA. This thing is a beast, getting a massive 77.5 on GPQA (up from 62.9) and 51.8 on LiveCodeBench (up from 32). This is a huge leap forward, and it proves that a powerful, well-trained instruct model can still push the boundaries of reasoning.

** The New (open) King of Code: Qwen3-Coder-480B (**[**X**](https://x.com/Alibaba_Qwen/status/1947766835023335516)**, **[**Try It**](https://wandb.me/qcoder-colab)**, **[**HF**](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct)**)**

Just as we were catching our breath, they dropped the main event: **Qwen3-Coder**. This is a 480-billion-parameter coding-specific behemoth (35B active) trained on a staggering 7.5 trillion tokens, with a 70% code ratio, that gets a new SOTA on SWE-bench verified with 69.6% (just a week after Kimi got SOTA with 65% and 2 weeks after Devstral's SOTA of 53% 😮) 

To get this model to SOTA, Junyang explained they used reinforcement learning with over 20,000 parallel sandbox environments. This allows the model to interact with the environment, write code, see the output, get the reward, and learn from it in a continuous loop. The results speak for themselves.

With long context abilities 256K with up to 1M extended with YaRN, this coding beast tops the charts, and is achieving Sonnet level performance for significantly less cost! 

Both models supported day-1 on W&B Inference ([X](https://x.com/weights_biases/status/1947859654400434538), [Get Started](https://wandb.me/qcoder-colab))

I'm very very proud to announce that both these incredible models get Day-1 support on our W&B inference (and that yours truly is now part of the decision of which models we host!) 

With unbeatable prices ($0.10/$0.10 input/output 1M for A22B, $1/$1.5 for Qwen3 Coder) and speed, we are hosting these models at full precision to give you the maximum possible intelligence and the best bang for your buck! 

Nisten has setup our (OpenAI compatible) endpoint with his Cline coding assistant and has built a 3D Tetris game live on the show, and it absolutely went flying. 

This demo perfectly captures the convergence of everything we're excited about: a state-of-the-art open-source model, running on a blazing-fast inference service, integrated into a powerful open-source tool, creating something complex and interactive in seconds.

If you want to try this yourself, we're giving away credits for W&B Inference. Just find our [announcement tweet](https://x.com/weights_biases/status/1947859654400434538) for the Qwen models on the **@weights_biases** X account and reply with **"coding capybara"** (a nod to Qwen's old mascot!). Add "ThursdAI" and I'll personally make sure you get bumped up the list!

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Big Companies & APIs

**America’s AI Action Plan: A New Space Race for AI Dominance (**[**ai.gov**](ai.gov)**)**

Switching gears to policy, I’m was excited to cover the White House’s newly unveiled “America’s AI Action Plan.” This 25-page strategy, dropped this week, frames AI as a national priority on par with the space race or Cold War, aiming to secure U.S. dominance with 90 policy proposals. I was thrilled to have Joseph Nelson from RoboFlow join us fresh from the announcement event in Washington, sharing the room’s energy and insights. The plan pushes for deregulation, massive data center buildouts, workforce training, and—most exciting for us—explicit support for open-source and open-weight models. It’s a bold move to counter global competition, especially from China, while fast-tracking infrastructure like chip fabrication and energy grids.

Joseph broke down the vibe at the event, including a surreal moment where the President riffed on Nvidia’s market dominance right in front of Jensen Huang. But beyond the anecdotes, what strikes me is the plan’s call for startups and innovation—think grants and investments via the Department of Defense and Small Business Administration. It’s like a request for new AI companies to step up. As someone who’s railed against past moratorium fears on this show, seeing this pro-innovation stance is a huge relief.

**🔊 Voice & Audio – Higgs Audio v2 Levels Up (**[**X**](https://x.com/reach_vb/status/1947997596456272203)**)**

Boson AI fused a 3B-param Llama 3.2 with a 2.2B audio Dual-FFN and trained on ten million hours of speech + music. Result: Higgs Audio v2 beats GPT-4o-mini and ElevenLabs v2 on prosody, does zero-shot multi-speaker dialog, and even hums melodies. The demo runs on a single A100 and sounds pretty-good. 

The first demo I played was not super impressive, but the laugh track made up for it! 

**🤖 A Week with ChatGPT Agent**

Last week, OpenAI dropped the ChatGPT Agent on us during our stream, and now we've had a full week to play with it. It's a combination of their browser-operating agent and their deeper research agent, and the experience is pretty wild.

Yam had it watching YouTube videos and scouring Reddit comments to create a comparison of different CLI tools. He was blown away, seeing the cursor move around and navigate complex sites right on his phone.

I put it through its paces as well. I tried to get it to order flowers for my girlfriend (it got all the way to checkout!), and it successfully found and filled out the forms for a travel insurance policy I needed. My ultimate test ([live stream here](https://x.com/altryne/status/1948111176203911222)), however, was asking it to prepare the show notes for ThursdAI, a complex task involving summarizing dozens of my X bookmarks. It did a decent job (a solid C/B), but still needed my intervention. It's not quite a "fire-and-forget" tool for complex, multi-step tasks yet, but it's a huge leap forward. As Yam put it, "This is the worst that agents are going to be." And that's an exciting thought.

What a week. From open-source models that rival the best closed-source giants to governments getting serious about AI innovation, the pace is just relentless. It's moments like Nisten's live demo that remind me why we do this show—to witness and share these incredible leaps forward as they happen. We're living in an amazing time.

Thank you for being a ThursdAI subscriber. As always, here's the TL;DR and show notes for everything that happened in AI this week.

Thanks for reading ThursdAI - Recaps of the most high signal AI weekly spaces! This post is public so feel free to share it.

TL;DR and Show Notes

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/altryne))

* **Co-Hosts** - [@WolframRvnwlf](http://x.com/WolframRvnwlf), [@yampeleg](http://x.com/yampeleg), [@nisten](http://x.com/nisten), [@ldjconfirmed](http://x.com/ldjconfirmed)

* **Junyang Lin** - Qwen Team, Alibaba ([@JustinLin610](https://x.com/JustinLin610))

* **Joseph Nelson** - Co-founder & CEO, Roboflow ([@josephnelson](https://x.com/josephnelson))

* **Open Source LLMs**

* Sapient Intelligence releases **Hierarchical Reasoning Model (HRM)**, a tiny 27M param model with impressive reasoning on specific tasks ([X](https://x.com/makingAGI/status/1947286324735856747), [arXiv](https://arxiv.org/abs/2506.21734)).

* Qwen drops a "little" update: **Qwen3-235B-A22B-Instruct-2507**, a powerful non-reasoning model ([X](https://x.com/JustinLin610/status/1947364588340523222), [HF Model](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)).

* Qwen releases the new SOTA coding agent model: **Qwen3-Coder-480B-A35B-Instruct** ([X](https://x.com/Alibaba_Qwen/status/1947790753414369280), [HF Model](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct)).

* **Hermes-Reasoning Tool-Use dataset** with 51k tool-calling examples is released ([X](httpshttps://x.com/intstr1Irinja/status/1947444760393773185), [HF Dataset](https://huggingface.co/datasets/interstellarninja/hermes_reasoning_tool_use)).

* NVIDIA releases updates to their **Nemotron** reasoning models.

* **Big CO LLMs + APIs**

* The White House unveils **"America’s AI Action Plan"** to "win the AI race" ([X](https://x.com/NetChoice/status/1948042669906624554), [White House PDF](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf)).

* Both **OpenAI** ([X](https://x.com/alexwei_/status/1946477742855532918)) and **Google DeepMind** win Gold at the International Math Olympiad (IMO), with **ByteDance's Seed-Prover** taking Silver ([GitHub](https://github.com/ByteDance-Seed/Seed-Prover)).

* The AI math breakthrough has a "gut punch" effect on the math community ([Dave White on X](https://x.com/Dave_White_/status/1947461492783386827)).

* Google now processes over **980 trillion tokens** per month across its services.

* A week with **ChatGPT Agent**: testing its capabilities on real-world tasks.

* **This Week's Buzz**

* Day 0 support for both new Qwen models on **W&B Inference** ([Try it](https://wandb.ai/inference), [Colab](https://wandb.me/qcoder-colab)). Reply to our [tweet](https://x.com/weightsandbiases) with "coding capybara ThursdAI" for credits!

* Live on-stream demo of Qwen3-Coder building a 3D Tetris game using kline.

* **Interesting Research**

* Researchers discover **subliminal learning** in LLMs, where traits are passed through seemingly innocuous data ([X](https://x.com/0wain_evans/status/1947709848103255232), [arXiv](https://arxiv.org/abs/2507.14805)).

* Apple proposes **multi-token prediction**, speeding up LLMs by up to 5x without quality loss ([X](https://x.com/JacksonAtkinsX/status/1947408593638002639), [arXiv](https://arxiv.org/abs/2507.11851)).

* **Voice & Audio**

* Boson AI open-sources **Higgs Audio v2**, a unified TTS model that beats GPT-4o-mini and ElevenLabs ([X](https://x.com/reach_vb/status/1947997596456272203), [HF Model](https://huggingface.co/bosonai/higgs-audio-v2-generation-3B-base)).

* **AI Art & Diffusion & 3D**

* Decart AI Releases **MirageLSD**, a real-time live-stream diffusion model for instant video transformation ([X Post](https://x.com/DecartAI/status/1945947692871692667)).

* **Tools**

* Qwen releases **qwen-code**, a CLI tool and agent for their new coder models. ([Github](https://github.com/QwenLM/qwen-code))

* **GitHub Spark**, a new AI-powered feature from GitHub ([Simon Willison on X](https://x.com/simonw/status/1948407932418457968)). 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-july-24-2025-qwen-mas-in/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-july-24-2025-qwen-mas-in?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2OTE3NDY2MywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.jguKI_sBQiDelSUjIO_nJjh0YQaml0qeUsh32Nk1NXE&utm_campaign=CTA_5).

---

## 📆 ThursdAI - July 17th - Kimi K2 👑, OpenAI Agents, Grok Waifus, Amazon Kiro, W&B Inference & more AI news!

**Date:** July 17, 2025  
**Duration:** 1:45:29  
**Link:** [https://sub.thursdai.news/p/thursdai-july-17th-kimi-k2-openai](https://sub.thursdai.news/p/thursdai-july-17th-kimi-k2-openai)

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

---

## 📆 ThursdAI - Jul 10 - Grok 4 and 4 Heavy, SmolLM3, Liquid LFM2, Reka Flash & Vision, Perplexity Comet Browser, Devstral 1.1 & More AI News

**Date:** July 11, 2025  
**Duration:** 1:49:46  
**Link:** [https://sub.thursdai.news/p/thursdai-jul-10-grok-4-and-4-heavy](https://sub.thursdai.news/p/thursdai-jul-10-grok-4-and-4-heavy)

Hey everyone, Alex here

Don't you just love "new top LLM" drop weeks? I sure do! This week, we had a watch party for Grok-4, with over 20K tuning in to watch together, as the folks at XAI unveiled their newest and best model around. Two models in fact, Grok-4 and Grok-4 Heavy. 

We also had a very big open source week, we had the pleasure to chat with the creators of 3 open source models on the show, first with Elie from HuggingFace who just released SmoLM3, then with our friend Maxime Labonne who together with Liquid released a beautiful series of tiny on device models. 

Finally we had a chat with folks from Reka AI, and as they were on stage, someone in their org published a new open source Reka Flash model 👏 Talk about Breaking News right on the show! 

It was a very fun week and a great episode, so grab your favorite beverage and let me update you on everything that's going on in AI (as always, show notes at the end of the article) 

Open Source LLMs

As always, even on big weeks like this, we open the show with Open Source models first and this week, the western world caught up to the Chinese open source models we saw last week! 

HuggingFace SmolLM3 - SOTA fully open 3B with dual reasoning and long-context ([𝕏](https://x.com/LoubnaBenAllal1/status/1942614508549333211), [HF](https://huggingface.co/blog/smollm3))

We had Eli Bakouch from Hugging Face on the show and you could feel the pride radiating through the webcam. SmolLM 3 isn’t just “another tiny model”; it’s an 11-trillion-token monster masquerading inside a 3-billion-parameter body. It reasons, it follows instructions, and it does both “think step-by-step” and “give me the answer straight” on demand. Hugging Face open-sourced every checkpoint, every dataset recipe, every graph in W&B – so if you ever wanted a fully reproducible, multi-lingual pocket assistant that fits on a single GPU, this is it.

They achieved the long context (128 K today, 256 K in internal tests) with a NoPE + YaRN recipe and salvaged the performance drop by literally merging two fine-tunes at 2 a.m. the night before release. Science by duct-tape, but it works: SmolLM 3 edges out Llama-3.2-3B, challenges Qwen-3, and stays within arm’s reach of Gemma-3-4B – all while loading faster than you can say “model soup.” 🤯

Liquid AI’s LFM2: Blazing-Fast Models for the Edge ([𝕏](https://x.com/maximelabonne/thread/1943295061275381864), [Hugging Face](https://huggingface.co/collections/LiquidAI/lfm2-686d721927015b2ad73eaa38))

We started the show and I immediately got to hit the #BREAKINGNEWS button, as Liquid AI dropped LFM2, a new series of tiny (350M-1.2B) models focused on Edge devices.

We then had the pleasure to host our friend Maxime Labonne, head of Post Training at Liquid AI, to come and tell us all about this incredible effort! 

Maxime, a legend in the model merging community, explained that LFM2 was designed from the ground up for efficiency. They’re not just scaled-down big models; they feature a novel hybrid architecture with convolution and attention layers specifically optimized for running on CPUs and devices like the Samsung Galaxy S24.

Maxime pointed out that Out of the box, they won't replace ChatGPT, but when you fine-tune them for a specific task like translation, they can match models 60 times their size. This is a game-changer for creating powerful, specialized agents that run locally. Definitely a great release and on ThursdAI of all days! 

Mistrals updated Devstral 1.1 Smashes Coding Benchmarks ([𝕏](https://x.com/MistralAI/status/1943316390863118716), [HF](https://huggingface.co/mistralai/Devstral-Small-2507))

Mistral didn't want to be left behind on this Open Source bonanza week, and also, today, dropped an update to their excellent coding model Devstral. 

With 2 versions, an open weights Small and API-only Medium model, they have claimed an amazing 61.6% score on Swe Bench and the open source Small gets a SOTA 53%, the highest among the open source models! 10 points higher than the excellent DeepSwe we covered just last week!

The thing to watch here is the incredible price performance, with this model beating Gemini 2.5 Pro and Claude 3.7 Sonnet while being 8x cheaper to run! 

DevStral small comes to us with an Apache 2.0 license, which we always welcome from the great folks at Mistral! 

Big Companies LLMs and APIs

There's only 1 winner this week, it seems that other foundational labs were very quiet to see what XAI is going to release. 

XAI releases Grok-4 and Grok-4 heavy - the world leading reasoning model ([𝕏](https://x.com/altryne/status/1943140257920172148), [Try It](https://grok.com/)) 

Wow, what a show! Space uncle Elon together with the XAI crew, came fashionably late to their own stream, and unveiled the youngest but smartest brother of the Grok family, Grok 4 plus a multiple agents swarm they call Grok Heavy. We had a watch party with over 25K viewers across all streams who joined and watched together, this, fairly historic event! 

Why historic? Well, for one, they have scaled RL (Reinforcement Learning) for this model significantly more than any other lab did so far, which resulted in an incredible reasoner, able to solve HLE (Humanity's Last Exam) benchmark at an unprecedented 50% (while using tools) 

The other very much unprecedented result, is on the ArcAGI benchmark, specifically V2, which is designed to be very easy for humans and very hard for LLMs, Grok-4 got an incredible 15.9%, almost 2x better than Opus 4 the best performing model before it! (ArcAGI president Greg Kamradt [says](https://x.com/GregKamradt/status/1943169631491100856) it Grok-4 shows signs of Fluid Intelligence!)

Real World benchmarks

Of course, academic benchmarks don't tell the full story, and while it's great to see that Grok-4 gets a perfect 100% on AIME25 and a very high 88.9% on GPQA Diamond, the most interesting benchmark they've showed was the Vending-Bench. This is a very interesting new benchmark from AndonLabs, where they simulate a vending machine, and let an LLM manage it, take orders, restock and basically count how much money a model can make while operating a "real" business. 

Grok scored a very significant $4K profit, selling 4569 items, 4x more than Opus, which shows a real impact on real world tasks! 

Not without controversy

Grok-4 release comes just 1 day after Grok-3 over at X, started calling itself MechaHitler and started spewing Nazi Antisemitic propaganda, which was a very bad episode. We've covered the previous "misalignment" from Grok, and this seemed even worse. Many examples (which XAI folks deleted) or Grok talking about Antisemitic tropes, blaming people with Jewish surnames for multiple things and generally acting jailbroken and up to no good.

Xai have addressed the last episode by a token excuse, supposedly open sourcing their prompts, which were updated all of 4 times in the last 2 month, while addressing this episode with a "we noticed, and we'll add guardrails to prevent this from happening" 

IMO this isn't enough, Grok is consistently (this is the 3rd time on my count) breaking alignment, way more than other foundational LLMs, and we must ask for more transparency for a model as significant and as widely used as this! And to my (lack of) surprise

First principles thinking == Elon's thoughts? 

Adding insult to injury, while Grok-4 was just launched, some folks asked it thoughts on the Israel-Palestine conflict and instead of coming up with an answer on its own, Grok-4 did a [X search](https://x.com/jeremyphoward/status/1943436621556466171) to see what Elon Musk things on this topic to form its opinion. It's so so wrong to claim a model is great at "first principles" and have the first few tests from folks, show that Grok defaults to see "what Elon thinks" 

Look, I'm all for "moving fast" and of course I love AI progress, but we need to ask more from the foundational labs, especially given the incredible amount of people who count on these models more and more! 

This weeks Buzz

We're well over 300 registrations to our hackathon at the Weights & Biases SF officess this weekend (July 12-13) and I'm packing my suitcase after writing this, as I'm excited to see all the amazing projets folks will build to try and win over $15K in prizes including an awesome ROBODOG

Not to late to come and hack with us, register at [lu.ma/weavehacks](http://lu.ma/weavehacks) 

Tools – Browsers grow brains

Perplexity’s **Comet** landed on my Mac and within ten minutes it was triaging my LinkedIn invites by itself. This isn’t a Chrome extension; it’s a Chromium fork where natural-language commands are first-class citizens. Tell it “find my oldest unread Stripe invoice and download the PDF” and watch the mouse move. The Gmail connector lets you ask, “what flights do I still need to expense?” and get a draft report. Think Cursor, but for every tab.

I [benchmarked](https://x.com/altryne/status/1943012655817544142) Comet against OpenAI Operator on my “scroll Alex’s 200 tweet bookmarks, extract the juicy links, drop them into Notion” task—Operator died halfway, Comet almost finished. Almost. The AI browser war has begun; Chrome’s Mariner project and OpenAI’s rumored Chromium team better move fast. 

Comet is available to Perplexity MAX subscribers now, and will come to pro subscribers with invites soon, as soon as I'll have them I'll tell you how to get one! 

Vision & Video

Reka dropped in with a double-whammy of announcements. First, they showcased **Reka Vision**, an agentic platform that can search, analyze, and even edit your video library using natural language. The demo of it automatically generating short-form social media reels from long videos was super impressive.

Then, in a surprise live reveal, they dropped **Reka Flash 3.1**, a new 21B parameter *open-source* multimodal model! It boasts great performance on coding and math benchmarks, including a 65% on AIME24. It was awesome to see them drop this right on the show.

We also saw LTX Video release three new open-source LoRAs for precise video control (Pose, Depth, and Canny), and Moonvalley launched **Marey**, a video model for filmmakers that's built exclusively on licensed, commercially-safe data—a first for the industry.

Veo3 making talking pets

Google have released an update to VEO 3, allowing you to upload an image and have the characters in the image say what you want! It’s really cool for human like generations, but it’s way more fun to animate… your pets! Here’s two of the best doggos in Colorado presenting themselves! 

The full prompt to create your own after you upload an image was: 

Two dogs presenting themselves, the left one barking first and then saying "Hey, I'm George Washington Fox" and the right dog following up with a woof and then says "and I'm his younger brother, Dr Emmet Brown". 

Then both are saying "we're good boys" and barking

Both should sound exiting with an american accent and a dog accent

Phew, what a week! From open source Breaking News from the folks who trained the models right on the podcast, to watch parties and Nazi LLMs, this has been one hell of a ride! 

Next week, there are already rumors of a potential Gemini 3 release, the OpenAI open source model is rumored to be dropping, and I'm sure we'll get all kinds of incredible things lined up + it's going to be my birthday on Thursday so, looking forward! 

See you next week 🫡

Show notes and Links

TL;DR of all topics covered:

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@yampeleg](x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed)) [@ryancarson](http://x.com/@ryancarson)

* Guests

* Elie Bakouch - Training at Hugging Face ([@eliebakouch](https://x.com/eliebakouch))

* Maxime Labonne - Head of postrainig and Liquid AI ([@maximelabonne](https://twitter.com/maximelabonne/status/1943295061275381864)) author of [LLM-Course](https://github.com/mlabonne/llm-course)

* Mattia Atzeni - Member of Technical Staff @ Reka

* Meenal Nalwaya - Head of Product, Reka Al

* **Open Source LLMs**

* HuggingFace - SmolLM3 SOTA, fully open-source 3B dual-mode reasoning and long-context support ([X](https://x.com/LoubnaBenAllal1/status/1942614508549333211), [HF](https://huggingface.co/blog/smollm3))

* Liquid AI launches LFM2: the fastest, most efficient open-source edge LLMs yet ([X](https://x.com/maximelabonne/thread/1943295061275381864), [HF](https://huggingface.co/collections/LiquidAI/lfm2-686d721927015b2ad73eaa38))

* Reachy Mini: Hugging Face and Pollen Robotics launch a $299 open-source desktop robot ([X](https://x.com/Thom_Wolf/status/1942887160983466096), [HF](https://huggingface.co/blog/reachy-mini))

* NextCoder-32B: Microsoft’s new code-editing LLM rivals GPT-4o on complex code tasks ([Microsoft Research](https://www.microsoft.com/en-us/research/publication/nextcoder-robust-adaptation-of-code-lms-to-diverse-code-edits/), [HF](https://huggingface.co/microsoft/NextCoder-32B))

* Mistral AI updates Devstral Small 1.1 and Devstral Medium, setting new open-source coding agent benchmarks ([X](https://x.com/MistralAI/status/1943316390863118716), [HF](https://huggingface.co/mistralai/Devstral-Small-2507), [Blog](https://mistral.ai/news/devstral-2507))

* Reka updates RekaFlash 1.1 ([HF](https://huggingface.co/RekaAI/reka-flash-3.1))

* **Big CO LLMs + APIs**

* 👑 Grok 4 Release: A Historic Leap from XAI - Grok 4 and Grok 4 heavy [X](https://x.com)

* Grok 3 is going nazi racing on X - MeinPrompt gate ([X](https://x.com/altryne/status/1943077695178391572))

* Gemini API Batch Mode launches with 50% cost savings for large-scale AI jobs ([X](https://x.com/_philschmid/status/1942238040593699077), [Google Blog](https://developers.googleblog.com/en/scale-your-ai-workloads-batch-mode-gemini-api/))

* **This weeks Buzz**

* W&B Hackathon is nearing capacity - Robodog is ready to be given out ([lu.ma/weavehacks](https://lu.ma/weavehacks))

* **Vision & Video**

* Reka Vision: Multimodal Agent for Visual Understanding and Search ([Reka on X](https://x.com/RekaAILabs/status/1942621988390088771), [Vision app](https://app.reka.ai/vision))

* LTX Video launches 3 open-source LoRAs for video control: Pose, Depth, Canny ([LTX Studio on X](https://x.com/LTXStudio/status/1942604844449292614), [GitHub](https://github.com/Lightricks/LTX-Video), [HF model](https://huggingface.co/Lightricks/LTX-Video))

* Marey by Moonvalley: the first professional, licensed AI video tool built for creative control ([Moonvalley on X](https://x.com/moonvalley/status/1942570142430552163), [Product page](https://www.moonvalley.com/marey))

* **Tools**

* Perplexity Launches Comet: The AI-Powered Browser for Modern Productivity ([X](https://x.com/AravSrinivas/thread/1942968552727941477), [HF](https://huggingface.co/perplexity-ai)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jul-10-grok-4-and-4-heavy/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jul-10-grok-4-and-4-heavy?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2ODAzMTUwMCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.vsmVuc4JlKQvitqu75NwpWjhYA6cXbfPNkHcHRJOqPQ&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Jul 3 - ERNIE 4.5, Hunyuan A13B, MAI-DxO outperforms doctors, RL beats SWE bench, Zuck MSL hiring spree & more AI news

**Date:** July 03, 2025  
**Duration:** 1:36:16  
**Link:** [https://sub.thursdai.news/p/thursdai-jul-3-ernie-45-hunyuan-a13b](https://sub.thursdai.news/p/thursdai-jul-3-ernie-45-hunyuan-a13b)

Hey everyone, Alex here 👋

Welcome back to another mind-blowing week on ThursdAI! We’re diving into the first show of the second half of 2025, and let me tell you, AI is not slowing down. This week, we’ve got a massive wave of open-source models from Chinese giants like Baidu and Tencent that are shaking up the game, Meta’s jaw-dropping hiring spree with Zuck assembling an AI dream team, and Microsoft’s medical AI outperforming doctors on the toughest cases. Plus, a real-time AI game engine that had me geeking out on stream. Buckle up, folks, because we’ve got a lot to unpack!

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

We had incredible guests like Michael Luo from Agentica, dropping knowledge on RL coding agents, and Ivan Burazin from Daytona, revealing the infrastructure powering the agent era. We had an incredible episode this week, with over 8,000 views for the live show (as always, Links and Show notes in the end, and the YT live video is here for your convienience if you'd prefer watching) 

Open Source AI & LLMs: The Chinese Powerhouse Wave

Man, if there’s one takeaway from this week, it’s that Chinese companies are absolutely dominating the open-source LLM scene. Let’s break down the heavy hitters that dropped this week and why they’ve got everyone talking.

Baidu’s ERNIE 4.5: A Suite of 10 Models to Rule Them All

Baidu, a giant in the Chinese tech space, just flipped the script by open-sourcing their ERNIE 4.5 series. We’re talking 10 distinct models ranging from a whopping 424 billion parameters down to a tiny 0.3 billion. With an Apache 2.0 license, 128K context window, and multimodal capabilities handling image, video, and text input, this is a massive drop. Their biggest Mixture-of-Experts (MoE) model, with 47B active parameters, even outshines OpenAI’s o1 on visual knowledge tasks like DocVQA, scoring 93% compared to o1’s 81%! 

What’s wild to me is Baidu’s shift. They’ve been running ERNIE in production for years—think chatbots and more across their ecosystem—but they weren’t always open-source fans. Now, they’re not just joining the party, they’re hosting it. If you’re into tinkering, this is your playground—check it out on Hugging Face ([HF](https://huggingface.co/baidu)) or dive into their technical paper ([Paper](https://ernie.baidu.com/blog/publication/ERNIE_Technical_Report.pdf)).

Tencent’s Hunyuan-A13B-Instruct: WizardLM Team Strikes Again

Next up, Tencent dropped Hunyuan-A13B-Instruct, and oh boy, does it have a backstory. This 80B parameter MoE model (13B active at inference) comes from the legendary WizardLM team, poached from Microsoft after a messy saga where their killer models got yanked from the internet over “safety concerns.” I remember the frustration—we were all hyped, then bam, gone. Now, under Tencent’s wing, they’ve cooked up a model with a 256K context window, hybrid fast-and-slow reasoning modes, and benchmarks that rival DeepSeek R1 and OpenAI o1 on agentic tasks. It scores an impressive 87% on AIME 2024, though it dips to 76% on 2025, hinting at some overfitting quirks. Though for a 12B active parameters model this all is still VERY impressive.

Here’s the catch—the license. It excludes commercial use in the EU, UK, and South Korea, and bans usage if you’ve got over 100M active users. So, not as open as we’d like, but for its size, it’s a beast that fits on a single machine, making it a practical choice for many. They’ve also released two datasets, ArtifactsBench and C3-Bench, for code and agent evaluation. I’m not sold on the name—Hunyuan doesn’t roll off the tongue for Western markets—but the WizardLM pedigree means it’s worth a look. Try it out on Hugging Face ([HF](https://huggingface.co/tencent/Hunyuan-A13B-Instruct)) or test it directly ([Try It](https://hunyuan.tencent.com/)).

Huawei’s Pangu Pro MoE: Sidestepping Sanctions with Ascend NPUs

Huawei entered the fray with Pangu Pro MoE, a 72B parameter model with 16B active per token, and here’s what got me hyped—it’s trained entirely on their own Ascend NPUs, not Nvidia or AMD hardware. This is a bold move to bypass US sanctions, using 4,000 of these chips to preprocess 13 trillion tokens. The result? Up to 1,528 tokens per second per card with speculative decoding, outpacing dense models in speed and cost-efficiency. Performance-wise, it’s close to DeepSeek and Qwen, making it a contender for those outside the Nvidia ecosystem.

I’m intrigued by the geopolitical angle here. Huawei’s proving you don’t need Western tech to build frontier models, and while we don’t know who’s got access to these Ascend NPUs, it’s likely a game-changer for Chinese firms. Licensing isn’t as permissive as MIT or Apache, but it’s still open-weight. Peek at it on Hugging Face ([HF](https://huggingface.co/IntervitensInc/pangu-pro-moe-model)) for more details.

DeepSWE-Preview: RL Coding Agent Hits 59% on SWE-Bench

Switching gears, I was blown away chatting with Michael Luo from Agentica about DeepSWE-Preview, an open-source coding agent trained with reinforcement learning (RL) on Qwen3-32B. This thing scored a stellar 59% on SWE-Bench-Verified (42.2% Pass@1, 71% Pass@16), one of the top open-weight results out there. What’s cool is they did this without distilling from proprietary giants like Claude—just pure RL over six days on 64 H100 GPUs. Michael shared how RL is surging because pre-training hits data limits, and DeepSWE learned emergent behaviors like paranoia, double-checking edge cases to avoid shaky fixes.

This underdog story of academic researchers breaking benchmarks with limited resources is inspiring. They’ve open-sourced everything—code, data, logs—making it a goldmine for the community. I’m rooting for them to get more compute to push past even higher scores. Dive into the details on their blog ([Notion](https://pretty-radio-b75.notion.site/DeepSWE-Training-a-Fully-Open-sourced-State-of-the-Art-Coding-Agent-by-Scaling-RL-22281902c1468193aabbe9a8c59bbe33)) or check the model on Hugging Face ([HF Model](https://huggingface.co/Agentica/DeepSWE-Preview)).

This Week’s Buzz from Weights & Biases: come Hack with Us! 🔥

As always, I’ve got some exciting news from Weights & Biases to share. We’re hosting the first of our Weavehacks hackathons in San Francisco on July 12-13. It’s all about agent protocols like MCP and A2A, and I’m stoked to you guys in person—come say hi for a high-five! We’ve got cool prizes, including a custom W&B RoboDog that’s been a conference hit, plus $13-14K in cash. Spots are filling fast, so register now and we'll let you in ([Sign Up](http://lu.ma/weavehacks)).

We’re also rolling out Online Evaluations in Weave, letting you monitor LLM apps live with judge agents on production data—super handy for catching hiccups. And our inference service via CoreWeave GPUs offers free credits for open-source model testing. Want in or curious about Weave’s tracing tools? Reach out to me anywhere, and I’ll hook you up. Can’t wait to demo this next week!

Big Companies & APIs: AI’s NBA Draft and Medical Marvels

Shifting to the big players, this week felt like an AI sports season with blockbuster hires and game-changing releases. From Meta’s talent poaching to Microsoft’s medical breakthroughs, let’s unpack the drama and innovation.

Meta Superintelligence Labs: Zuck’s Dream Team Draft 

Imagine an AI NBA draft—that’s what Meta’s up to with their new Superintelligence Labs (MSL). Led by Alex Wang (formerly of Scale AI) and Nat Friedman (ex-GitHub CEO), MSL is Zuck’s power move after Llama 4’s lukewarm reception. They’ve poached up to 10 key researchers from OpenAI, including folks behind GPT-4’s image generation and o1’s foundations, with comp packages rumored at $100M for the first year and up to $300M over four years. That’s more than many Meta execs or even Tim Cook’s salary! They’ve also snagged talent from Google DeepMind and even tried to acquire Ilya Sutskever’s SSI outright (to which he said he's flattered but no) 

This is brute force at its finest, and I’m joking that I didn’t get a $100M offer myself—ThursdAI’s still waiting for that email, Zuck! OpenAI’s Sam Altman fired back with “missionaries beat mercenaries,” hinting at a culture clash, while Mark Chen felt like Meta “broke into their house and took something” It’s war, folks, and I’m hyped to see if MSL delivers a Llama that crushes it. With FAIR and GenAI folding under this new crack team of 50, plus Meta’s GPU arsenal, the stakes are sky-high.

If you're like to see the list of "mercenaries" worth over 100M, you can see who they are and their achievements [here](https://docs.google.com/spreadsheets/d/1qX7_VK8vN2v2urpiBY_we-FNz2PS3ZKsWp_9kXCyQB0/edit?usp=sharing)

Cursor’s Killer Hires and Web Expansion

Speaking of talent wars, Cursor (built by AnySphere) just pulled off a stunner by hiring Boris Cherny and Cat Wu, key creators of Claude Code, as Chief Architect and Head of Product. This skyrockets Cursor’s cred in code generation, and I’m not surprised—Claude Code was a side project that exploded, and now Cursor’s got the brains behind it. On top of that, they’ve rolled out AI coding agents to web and mobile, even integrating with Slack. No more being tied to your desktop—launch, monitor, and collab on code tasks anywhere.

The lines between native and web tools are blurring fast, and Cursor’s leading the charge. I haven’t tested the Slack bit yet, but if you have, hit me up in the comments. This, plus their recent $20M raise, shows they’re playing to win. Learn more at ([Cursor](https://cursor.com/agents)).

Microsoft MAI-DxO: AI Diagnoses Better Than Doctors

Now, onto something that hits close to home for me—Microsoft’s MAI-DxO, an AI system that’s outdiagnosing doctors on open-ended medical cases. On 304 of the toughest New England Journal of Medicine cases, it scored 85.5% accuracy, over four times the 20% rate of experienced physicians. I’ve had my share of frustrating medical waits, and seeing AI step in as a tool for doctors—not a replacement—gets me excited for the future.

It’s an orchestration of models simulating a virtual clinician panel, asking follow-up questions, ordering tests, and even factoring in cost controls for diagnostics. This isn’t just acing multiple-choice; it handles real-world ambiguity. My co-host Yam and I stressed—don’t skip your doctor for ChatGPT, but expect your doc to be AI-superpowered soon. Read more on Microsoft’s blog ([Blog](https://microsoft.ai/new/the-path-to-medical-superintelligence/)).

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Cloudflare’s One-Click AI Bot Block: Protecting the Internet

Cloudflare made waves with a one-click feature to block AI bots and scrapers, available to all customers, even free-tier ones. With bots like Bytespider and GPTBot hitting nearly 40% of top sites, but only 3% blocking them, this addresses a huge shift. I’m with the CEO here—the old internet deal was Google scraping for traffic; now, AI summaries keep users from clicking through, breaking monetization for creators. Yam suggested a global license for training data with royalties, and I’m curious if that’s the future. For now, Cloudflare’s ML detects even sneaky bots spoofing as browsers. Big move—check their announcement ([X](https://x.com/Cloudflare/status/1939988601976021156)) and the cool website [goodaibots.com](http://goodaibots.com) 

Cypher Alpha: Mystery 1M Context Model on OpenRouter

Lastly, a mysterious 1M context model, Cypher Alpha, popped up on OpenRouter for free testing (with data logging). It’s fast at 70 tokens/sec, low latency, but not a reasoning model—refusals on basic queries stumped me. Speculation points to Amazon Titan, which would be a surprise entry. I’m intrigued by who’s behind this—Gemini, OpenAI, and Qwen hit 1M context, but Amazon? Let’s see. Try it yourself ([Link](https://openrouter.ai/openrouter/cypher-alpha:free/providers)).

Vision & Video: Mirage’s AI-Native Game Engine Blows Minds 🤯

Okay, folks, I’ve gotta geek out here.  Dynamics Lab unveiled the world’s first AI-native user-generated content (UGC) game engine, live with playable demos like a GTA-style “Urban Chaos” and a racing “Coastal Drift.” Running at 16 frames per second, it generates photorealistic worlds in real-time via natural language or controller input. You can jump, run, fight, or drive, and even upload an image to spawn a new game environment on the fly.

What’s nuts is there’s no pre-built game behind this—it’s infinite, custom content created as you play. I was floored showing this on stream; it’s obviously not perfect with clipping and delays, but we’re witnessing the dawn of personalized gaming. You gotta try this—head to their site for the demos ([Playable Demo](https://blog.dynamicslab.ai/)).

This brings us even more closer to the "every pixel will be generated" dream of Jensen Huang.

Voice & Audio: TTS Gets Real with Kyutai and Qwen

This week brought fresh text-to-speech (TTS) updates that hint at smarter conversational AI down the line. Kyutai TTS, from the French team behind Moshi, dropped with ultra-low latency (220ms first-token) and high speaker similarity (77.1% English, 78.7% French), plus a word error rate of just 2.82% in English. It’s production-ready with a Rust server and voice cloning from a 10-second clip—perfect for LLM-integrated apps. Check it out ([X Announcement](https://x.com/kyutai_labs/status/1940767331921416302), [HF Model](https://huggingface.co/kyutai/tts-1.6b-en_fr)).

Qwen-TTS from Alibaba also launched, focusing on Chinese dialects like Pekingese and Shanghainese, but with English support too. It’s got human-level naturalness via API, though less relevant for our English audience. Still, it’s a solid step—see more ([X Post](https://x.com/Alibaba_Qwen/status/1939553252166836457)). Both are pieces of the puzzle for richer virtual interactions, and I’m pumped to see where this goes.

Infrastructure for Agents: Daytona’s Sandbox Revolution

I’m thrilled to have chatted with Ivan Burazin from Daytona, a cloud provider delivering agent-native runtimes—or sandboxes—that give agents their own computers for tasks like code execution or data analysis. They’ve hit over $1M in annualized run rate just two months post-launch, with 15,000 signups and 1,500 credit cards on file. That’s insane growth for infrastructure, which usually ramps slowly due to integration delays.

Why’s this hot? 2025 is the year of agents, and as Ivan shared, even OpenAI and Anthropic recently redefined agents as needing runtimes. From YC’s latest batch (37% building agents) to Cursor’s web move, every task may soon spin up a sandbox. Daytona’s “stateful serverless” tech spins fast, lasts long, and scales across regions like the US, UK, Germany, and India, addressing latency and GDPR needs. If you’re building agents, this is your unsung hero—explore it at ([Daytona IO](https://github.com/DaytonaIO)) and grab $200 in credits, or up to $50K for startups ([Startups](https://daytona.io/startups)).

Wrapping Up: AI’s Relentless Pace

What a week, folks! From Chinese open-source titans like ERNIE 4.5 and Hunyuan-A13B redefining accessibility, to Meta’s blockbuster hires signaling an AI arms race, and Microsoft’s MAI-DxO paving the way for smarter healthcare, we’re witnessing AI’s relentless acceleration. Mirage’s game engine and Daytona’s sandboxes remind us that creativity and infrastructure are just as critical as models themselves. I’m buzzing with anticipation for what’s next—will Meta’s dream team deliver? Will agents redefine every app? Stick with ThursdAI to find out. See you next week for more!

TL;DR and Show Notes

Here’s the quick rundown of everything we covered this week, packed with links to dive deeper:

* **Show Notes & Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* **Co-Hosts** - [@WolframRvnwlf](http://x.com/@WolframRvnwlf), [@yampeleg](http://x.com/@yampeleg), [@nisten](http://x.com/@nisten), [@ldjconfirmed](http://x.com/@ldjconfirmed)

* **Guests** - Ivan Burazin (Daytona), Michael Luo (Agentica)

* **Open Source LLMs**

* Baidu’s ERNIE 4.5 Series - 10 models, 424B to 0.3B, multimodal, beats o1 on DocVQA ([X](https://x.com/Baidu_Inc/status/1939724778157511126), [HF](https://huggingface.co/baidu), [Paper](https://ernie.baidu.com/blog/publication/ERNIE_Technical_Report.pdf))

* Tencent’s Hunyuan-A13B-Instruct - 80B total, 13B active, 256K context, WizardLM legacy ([X](https://x.com/TencentHunyuan/status/1938525874904801490), [HF](https://huggingface.co/tencent/Hunyuan-A13B-Instruct), [Try It](https://hunyuan.tencent.com/))

* Huawei’s Pangu Pro MoE - 72B, trained on Ascend NPUs, 1,528 tokens/sec ([X](https://x.com/search?q=pangu%20pro&src=typed_query), [HF](https://huggingface.co/IntervitensInc/pangu-pro-moe-model))

* DeepSWE-Preview - RL agent, 59% SWE-Bench-Verified on Qwen3-32B ([Notion](https://pretty-radio-b75.notion.site/DeepSWE-Training-a-Fully-Open-sourced-State-of-the-Art-Coding-Agent-by-Scaling-RL-22281902c1468193aabbe9a8c59bbe33), [HF Model](https://huggingface.co/Agentica/DeepSWE-Preview))

* **This Week’s Buzz**

* Weights & Biases Weavehacks Hackathon - SF, July 12-13, agent protocols focus ([Sign Up](http://lu.ma/weavehacks))

* **Big CO LLMs + APIs**

* Meta Superintelligence Labs (MSL) - Zuck hires dream team, up to $300M comp packages from OpenAI talent ([list](https://docs.google.com/spreadsheets/d/1qX7_VK8vN2v2urpiBY_we-FNz2PS3ZKsWp_9kXCyQB0/edit?usp=sharing))

* Cursor - Hires Claude Code creators, web/mobile agents with Slack ([Cursor](https://cursor.com/agents), [HF](https://huggingface.co/spaces/cursor))

* Microsoft MAI-DxO - 85.5% accuracy on NEJM cases vs. 20% for doctors ([X](https://x.com/mustafasuleyman/status/1939670330332868696), [Blog](https://microsoft.ai/new/the-path-to-medical-superintelligence/))

* Cloudflare - One-click AI bot blocking, tackles scraping economics ([X](https://x.com/Cloudflare/status/1939988601976021156))

* Cypher Alpha - Mystery 1M context model, possibly Amazon Titan ([Link](https://openrouter.ai/openrouter/cypher-alpha:free/providers))

* Gemini Pro 2.5 - Returned to Google’s free tier

* **Vision & Video**

* Mirage - AI-native UGC game engine, real-time photorealistic demos ([Playable Demo](https://blog.dynamicslab.ai/))

* Workflow - Restyle videos with Flux Kontext and Luma Modify ([X](https://x.com/lucataco93/status/1940113275221344566))

* **Voice & Audio**

* Kyutai TTS - Low-latency, high similarity in EN/FR ([X](https://x.com/kyutai_labs/status/1940767331921416302), [HF](https://huggingface.co/kyutai/tts-1.6b-en_fr))

* Qwen-TTS - Bilingual Chinese/English, human-level naturalness ([X](https://x.com/Alibaba_Qwen/status/1939553252166836457), [HF](https://huggingface.co/spaces/Qwen/Qwen-TTS))

* **Infrastructure**

* Daytona - Agent-native sandboxes, $1M run rate in 2 months ([GitHub](https://github.com/DaytonaIO), [Startups](https://daytona.io/startups))

* **Tools**

* Chai Discovery’s Chai-2 - Zero-shot antibody design ([Chai Discovery](https://www.chaidiscovery.com/news/introducing-chai-2))

Thanks for reading all the way through ThursdAI, folks! Share this with friends to spread the AI love, and I’ll catch you next week for more! 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jul-3-ernie-45-hunyuan-a13b/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jul-3-ernie-45-hunyuan-a13b?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2NzQ3MjkwMywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.NnlYvILRLy9k6gBd2kYURO8Vw7HkP9u15R-Gvp_FA6U&utm_campaign=CTA_5).

---

