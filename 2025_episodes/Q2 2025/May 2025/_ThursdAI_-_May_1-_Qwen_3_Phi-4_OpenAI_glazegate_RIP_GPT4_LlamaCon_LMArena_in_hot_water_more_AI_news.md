# 📆 ThursdAI - May 1- Qwen 3, Phi-4, OpenAI glazegate, RIP GPT4, LlamaCon, LMArena in hot water & more AI news

**Date:** May 01, 2025  
**Duration:** 1:30:21  
**Link:** [https://sub.thursdai.news/p/thursdai-may-1-qwen-3-phi-4-openai](https://sub.thursdai.news/p/thursdai-may-1-qwen-3-phi-4-openai)

---

## Description

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
