# ThursdAI - Apr 3rd - OpenAI Goes Open?! Gemini Crushes Math, AI Actors Go Hollywood & MCP, Now with Observability?

**Date:** April 03, 2025  
**Duration:** 1:37:33  
**Link:** [https://sub.thursdai.news/p/thursdai-apr-3rd-openai-goes-open](https://sub.thursdai.news/p/thursdai-apr-3rd-openai-goes-open)

---

## Description

Woo! Welcome back to ThursdAI, show number 99! Can you believe it? We are *one* show away from hitting the big 100, which is just wild to me. And speaking of milestones, we just crossed **100,000 downloads** on Substack alone! [Insert celebratory sound effect here 🎉]. Honestly, knowing so many of you tune in every week **genuinely fills me with joy**, but also a real commitment to keep bringing you the the high-signal, zero-fluff AI news you count on. Thank you for being part of this amazing community! 🙏

And what a week it's been! I started out busy at work, playing with the native image generation in ChatGPT like everyone else (all 130 million of us!), and then I looked at my notes for today… an absolute *mountain* of updates. Seriously, one of those weeks where open source just exploded, big companies dropped major news, and the vision/video space is producing stuff that's crossing the uncanny valley.

We’ve got OpenAI teasing a big open source release (yes, *Open*AI might actually be *open* again!), Gemini 2.5 showing superhuman math skills, Amazon stepping into the agent ring, truly mind-blowing AI character generation from Meta, and a personal update on making the Model Context Protocol (MCP) observable. Plus, we had some fantastic guests join us live!

So buckle up, grab your coffee (or whatever gets you through the AI whirlwind), because we have a *lot* to cover. Let's dive in! (as always, show notes and links in the end)

OpenAI Makes Waves: Open Source Tease, Tough Evals & Billions Raised

It feels like OpenAI was determined to dominate the headlines this week, hitting us from multiple angles.

First, the potentially massive news: **OpenAI is planning to release a new open source model** in the "coming months"! Kevin Weil [**tweeted**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fkevinweil%2Fstatus%2F1906797119848988822) that they're working on a "highly capable open language model" and are actively seeking developer feedback through dedicated sessions ([**sign up here**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Fform%2Fopen-model-feedback) if interested) to "get this right." Word on the street is that this could be a powerful reasoning model. Sam Altman also cheekily added they won't slap on a Llama-style 8,300 tasks) and even includes meta-evaluation for the LLM judge they built ([**Nano-Eval framework also open sourced**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fopenai%2Fpreparedness)). The kicker? **Claude 3.5 Sonnet (New)** came out on top with just **21.0%** replication score (human PhDs got 41.4%). Props to OpenAI for releasing an eval where they don’t even win. That’s what real benchmarking integrity looks like. You can find the [**code on GitHub**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fopenai%2Fpreparedness%2Ftree%2Fmain%2Fproject%2Fpaperbench) and read the [**full paper here**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fcdn.openai.com%2Fpapers%2F22265bac-3191-44e5-b057-7aaacd8e90cd%2Fpaperbench.pdf).

Third, the casual [**40 Billion Dollars**](https://openai.com/index/investing−in−our−mission/)** **funding round led by SoftBank. Valuing the company at **300 Billion**. Yes, Billion with a B. More than Coke, more than Disney. The blog post was hilariously short for such a massive number. They also mentioned**500 million weekly ChatGPT users**and the insane onboarding rate (1M users/hr!) thanks to native image generation, especially seeing huge growth in India. The scale is just mind-boggling.

Oh, and for fun, try the new grumpy, EMO "[**Monday" voice**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FOpenAI%2Fstatus%2F1907124258867982338) in advanced voice mode. It's surprisingly entertaining.

Open Source Powerhouses: Nomic & OpenHands Deliver SOTA

Beyond the OpenAI buzz, the open source community delivered some absolute gems, and we had guests from two key projects join us!

Nomic Embed Multimodal: SOTA Embeddings for Visual Docs

Our friends at Nomic AI are back with a killer release! We had Zach Nussbaum on the show discussing [**Nomic Embed Multimodal**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.nomic.ai%2Fblog%2Fposts%2Fnomic-embed-multimodal). These are new 3B & 7B parameter embedding models ([**available on Hugging Face**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fcollections%2Fnomic-ai%2Fnomic-embed-multimodal-67e5ddc1a890a19ff0d58073)) built on Alibaba's excellent Qwen2.5-VL. They achieved **SOTA on visual document retrieval** by cleverly embedding interleaved text-image sequences – perfect for PDFs and complex webpages.

Zach highlighted that they chose the Qwen base because high-performing open VLMs under 3B params are still scarce, making it a solid foundation. Importantly, the 7B model comes with an **Apache 2.0 license**, and they've open sourced weights, code, and data. They offer both a powerful multi-vector version (ColNomic) and a faster single-vector one. Huge congrats to Nomic!

OpenHands LM 32B & Agent: Accessible SOTA Coding

Remember OpenDevin? It evolved into OpenHands, and the team just dropped their own [**OpenHands LM 32B**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.all-hands.dev%2Fblog%2Fintroducing-openhands-lm-32b----a-strong-open-coding-agent-model)! We chatted with co-founder Xingyao "Elle" Wang about this impressive Qwen 2.5 finetune ([**MIT licensed, on Hugging Face**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fall-hands%2Fopenhands-lm-32b-v0.1)).

It hits a remarkable **37.2% on SWE-Bench Verified **(a coding benchmark measuring real-world repo tasks), competing with much larger models. Elle stressed they didn't just chase code completion scores; they focused on tuning for *agentic capabilities* – tool use, planning, self-correction – using trajectories from their contamination-free Switch Execution dataset. This focus seems to be paying off, as the OpenHands *agent* also snagged the **#2 spot on the brand new Live SWE-Bench** leaderboard! Plus, the 32B model runs locally on a single 3090, making this power accessible. You can also try their managed [**OpenHands Cloud**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fapp.all-hands.dev%2F) ($50 free credit). Amazing progress from this team!

Frontiers: Diffusion LMs & Superhuman Math

Two other developments pushed the boundaries this week:

Dream 7B: A Diffusion Language Model Challenger?

This one's fascinating conceptually. Researchers unveiled [**Dream 7B**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhkunlp.github.io%2Fblog%2F2025%2Fdream%2F), a language model based on **diffusion**, not auto-regression. The [**benchmarks they shared**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FJiachengYe15%2Fstatus%2F1907430553369883017) show it competing strongly with top 7-8B models, and absolutely crushing tasks like Sudoku (81% vs <50% for others), potentially due to its parallel processing nature being better for global constraints. It's an exciting hint at alternative architectures, but the **model weights aren't out yet**, so we can't verify or play with it. Still, one to watch!

Gemini 2.5 Obliterates Olympiad Math (24.4% on USAMO!)

We already knew Gemini 2.5 was good, but wow. New results dropped showing its performance on the **USA Math Olympiad (USAMO)** – problems so hard most top models score under 5%. **Gemini 2.5 Pro scored an incredible 24.4%**!

The gap between it and everything else is massive, highlighting the power of its reasoning and thinking capabilities (which you can inspect via its traces!). Having used it for complex tasks myself (like wrestling with tax forms!), I can attest to its depth. It's free in the Gemini app – go try it!

Agents, Compute & Making MCP Observable

Amazon's Nova Act Agent & The Need for Access

Amazon entered the agent chat with [**Nova Act**](https://www.google.com/url?sa=E&q=https%3A%2F%2Flabs.amazon.science%2Fblog%2Fnova-act), designed for web browser actions. They claim it beats Claude 3.5 and OpenAI's QA model on some benchmarks, possibly leveraging acquired Adept talent. But... it's only available via an SDK with a request form. As Yam rightly pointed out on the show, these agent claims mean little until we can actually *use* them in the real world!

CoreWeave + NVIDIA = Insane Speeds

Hardware keeps accelerating. CoreWeave announced hitting [**800 Tokens/sec on Llama 3.1 405B**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.prnewswire.com%2Fnews-releases%2Fcoreweave-achieves-new-record-breaking-ai-inferencing-benchmark-with-nvidia-gb200-grace-blackwell-superchips-302418682.html%3Fhss_channel%3Dtw-979803443681349632) using NVIDIA's new GB200 Blackwell chips, and 33,000 T/s on Llama 2 70B with H200s. Inference is getting *fast*.

This Week's Buzz: Let's Make MCP Observable!

Okay, my personal mission this week builds on the growing **Model Context Protocol (MCP)** momentum. MCP is potentially the "HTTP for agents," enabling tool interoperability. But as tool use moves external, we lose visibility, making debugging and security harder.

That's why I'm launching the [**Observable Tools**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fobservable.tools%2F) initiative. The goal: integrate observability *into* the MCP standard itself. Right now, that link redirects to a [**GitHub discussion**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fmodel-context-protocol%2Fspecification%2Fdiscussions%2F18) where I've proposed using the **OpenTelemetry (OTel)** standard to add tracing to MCP interactions. This would give developers clear visibility into tool usage, regardless of their observability platform.

**I need your help!** Please check out the proposal, join the discussion, and **show your support** with a 👍 or 🚀 on GitHub. We need the community voice to make this happen! (And yes, my [**viral tweet**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne%2Fstatus%2F1906180131540066796) showed there's huge demand for usable MCP clients too – more on that soon!).

Vision & Video: Entering the Uncanny Valley

This space is moving at lightning speed.

[**Runway Gen-4**](https://www.google.com/url?sa=E&q=https%3A%2F%2Frunwayml.com%2Fresearch%2Fintroducing-runway-gen-4) was announced, pushing for better consistency in AI video. Here's a few example videos showing incredible character and world consistency:

ByteDance's impressive [**OmniHuman**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fdreamina.capcut.com%2Fai-tool%2Fvideo%2Flip-sync%2Fgenerate) (single image to talking avatar) is now publicly usable via Dreamina website. For people it's really good, but for animated style images, [Hedra Labs](https://www.hedra.com/) feels actually better (and much much faster)

**Meta's **[**MoCHA**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fcongwei1230.github.io%2FMoCha%2F)** is mind-blowing.** We had researcher Cong Wei explain how it generates *movie-grade*, full-body, expressive talking characters directly from speech and text (no reference image needed!). Using Diffusion Transformers and clever attention mechanisms, the realism is startling, handling lip-sync, gestures, emotions, and even multi-character dialogue. Check the project page videos – some are truly uncanny. Just look at this one!

Voice Highlight: Hailuo Speech-02

While Gladia launched their [**Solaria STT**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.gladia.io%2Fsolaria), the standout for me was [**Hailuo's Speech-02 TTS API**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FHailuo_AI%2Fstatus%2F1906723587379101923). The emotional control and voice cloning quality are, in my opinion, potentially SOTA right now, offering incredibly nuanced and realistic synthetic voices.

Tool Update & Breaking News!

* Google's [**NotebookLM now discovers related sources**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fblog.google%2Ftechnology%2Fgoogle-labs%2Fnotebooklm-discover-sources%2F) automatically.

* **BREAKING NEWS (Caught end of show): Devin 2.0 is out!** Cognition Labs launched their AI software engineer V2 with a new IDE experience and, crucially, a **$20/month** starting price. Much more accessible to try!

Phew! What a week. From OpenAI's big moves to Gemini's math prowess, stunning AI actors from Meta, and the push for an observable agent ecosystem – the field is accelerating like crazy.

Alright folks, that’s a wrap for show #99! Thank you again for tuning in, for being part of the community, and for keeping us on our toes with your insights and feedback. Special thanks to our guests Zach Nussbaum (Nomic), Xingyao Wang (All Hands AI), and Cong Wei (Meta/MoCHA) for joining us!

If you missed any part of the show, or want to grab any of the links, head over to [**ThursdAI.news**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fthursdai.news). The full recording (video on YouTube, audio on Spotify, Apple Podcasts, etc.) and this blog post with all the notes will be up shortly.

The best way to support the show? Share it with a friend or colleague who needs to stay up-to-date on AI, and drop us a 5-star review on your podcast platform! Financial support via Substack is also appreciated but never required.

Get ready for **Episode 100** next week! Until then, happy tinkering, stay curious, and I'll see you next ThursdAI!

Bye bye everyone!

TL;DR and Show Notes

**Host, Guests, and Co-hosts**

* **Host:** Alex Volkov - AI Evangelist & Weights & Biases ([**@altryne**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne))

* **Co-Hosts:**

* LDJ ([**@ldjconfirmed**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fldjconfirmed))

* Yam Peleg ([**@yampeleg**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fyampeleg))

* **Guests:**

* Zach Nussbaum ([**@zach_nussbaum**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fzach_nussbaum)) - Nomic AI

* Xingyao Wang ([**@xingyaow_**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fxingyaow_)) - All Hands AI / OpenHands

* Cong Wei ([**@CongWei1230**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FCongWei1230)) - Meta AI / MoCha

**Key Topics & Links**

* **OpenAI's Big Week:**

* Teasing highly capable [**Open Source Reasoner Model**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fkevinweil%2Fstatus%2F1906797119848988822) (seeking [**feedback**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Fform%2Fopen-model-feedback)).

* Released [**PaperBench**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Findex%2Fpaperbench%2F) eval ([**code**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fopenai%2Fpreparedness%2Ftree%2Fmain%2Fproject%2Fpaperbench), [**paper**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fcdn.openai.com%2Fpapers%2F22265bac-3191-44e5-b057-7aaacd8e90cd%2Fpaperbench.pdf)) & [**Nano-Eval framework**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fopenai%2Fpreparedness).

* Raised [**$40B at $300B valuation**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Findex%2Finvesting-in-our-mission%2F).

* New EMO "[**Monday" voice**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FOpenAI%2Fstatus%2F1907124258867982338) in ChatGPT.

* **Open Source Powerhouses:**

* [**Nomic Embed Multimodal**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.nomic.ai%2Fblog%2Fposts%2Fnomic-embed-multimodal): SOTA visual doc embeddings (3B & 7B, [**Apache 2.0 for 7B**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fcollections%2Fnomic-ai%2Fnomic-embed-multimodal-67e5ddc1a890a19ff0d58073)).

* [**OpenHands LM 32B**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.all-hands.dev%2Fblog%2Fintroducing-openhands-lm-32b----a-strong-open-coding-agent-model): SOTA-level coding agent model (Qwen finetune, [**MIT License**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fall-hands%2Fopenhands-lm-32b-v0.1), 37.2% SWE-Bench, #2 Live SWE-Bench). [**Cloud version available**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fapp.all-hands.dev%2F).

* **Frontier Models & Capabilities:**

* [**Dream 7B**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhkunlp.github.io%2Fblog%2F2025%2Fdream%2F): Promising **diffusion LM** shows strong benchmark results ([**esp. Sudoku**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FJiachengYe15%2Fstatus%2F1907430553369883017)), but weights not yet released.

* **Gemini 2.5**: Crushes hard **USAMO math eval (24.4%** vs <5% for others), showcasing superior reasoning.

* **Agents & Compute:**

* Amazon's [**Nova Act**](https://www.google.com/url?sa=E&q=https%3A%2F%2Flabs.amazon.science%2Fblog%2Fnova-act) agent announced, claims SOTA but lacks public access ([**request form**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fnova.amazon.com)).

* [**CoreWeave/NVIDIA**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.prnewswire.com%2Fnews-releases%2Fcoreweave-achieves-new-record-breaking-ai-inferencing-benchmark-with-nvidia-gb200-grace-blackwell-superchips-302418682.html%3Fhss_channel%3Dtw-979803443681349632): Massive inference speedups (800T/s on Llama 405B with GB200).

* **This Week's Buzz - MCP:**

* [**Observable Tools**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fobservable.tools%2F) initiative launched to add observability to MCP.

* Proposal using OpenTelemetry posted for [**community feedback on GitHub**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fmodel-context-protocol%2Fspecification%2Fdiscussions%2F18) - please support!

* Huge demand shown for usable MCP clients ([**viral tweet**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne%2Fstatus%2F1906180131540066796)).

* **Vision & Video Highlights:**

* [**Runway Gen-4**](https://www.google.com/url?sa=E&q=https%3A%2F%2Frunwayml.com%2Fresearch%2Fintroducing-runway-gen-4) focuses on video consistency.

* ByteDance [**OmniHuman**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fdreamina.capcut.com%2Fai-tool%2Fvideo%2Flip-sync%2Fgenerate) (image-to-avatar) now publicly available via Dreamina ([**example thread**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne%2Fstatus%2F1907173680456794187)).

* Meta's [**MoCHA**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fcongwei1230.github.io%2FMoCha%2F): Generates stunningly realistic, movie-grade talking characters from speech+text.

* **Voice Highlight:**

* [**Hailuo Speech-02**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FHailuo_AI%2Fstatus%2F1906723587379101923): Impressive TTS API with excellent emotional control and voice cloning.

* **Tool Updates:**

* [**Windsurf adds deployments**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fwindsurf_ai%2Fstatus%2F1907497638267924566) to Netlify.

* Google [**NotebookLM adds source discovery**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fblog.google%2Ftechnology%2Fgoogle-labs%2Fnotebooklm-discover-sources%2F).

* **Breaking News:**

* **Devin 2.0** AI Software Engineer announced, starts at $20/month. 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-apr-3rd-openai-goes-open/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-apr-3rd-openai-goes-open?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2MDUyMzI3MiwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.KeKD6SiF3Lcp_XPFGAtxcXxrkuK6rVe0xzzZqGXzZ8M&utm_campaign=CTA_5).
