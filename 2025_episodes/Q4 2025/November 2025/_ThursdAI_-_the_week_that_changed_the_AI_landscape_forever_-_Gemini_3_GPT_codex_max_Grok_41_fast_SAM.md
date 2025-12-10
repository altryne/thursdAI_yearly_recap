# 📆 ThursdAI - the week that changed the AI landscape forever - Gemini 3, GPT codex max, Grok 4.1 & fast, SAM3 and Nano Banana Pro

**Date:** November 20, 2025  
**Duration:** 1:29:13  
**Link:** [https://sub.thursdai.news/p/thursdai-the-week-that-changed-the](https://sub.thursdai.news/p/thursdai-the-week-that-changed-the)

---

## Description

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
