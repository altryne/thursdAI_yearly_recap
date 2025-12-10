# 📆 ThursdAI - Veo3, Google IO25, Claude 4 Opus/Sonnet, OpenAI x Jony Ive, Codex, Copilot Agent - INSANE AI week

**Date:** May 23, 2025  
**Duration:** 1:28:29  
**Link:** [https://sub.thursdai.news/p/thursdai-veo3-google-io25-claude](https://sub.thursdai.news/p/thursdai-veo3-google-io25-claude)

---

## Description

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
