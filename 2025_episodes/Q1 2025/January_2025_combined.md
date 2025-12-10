# ThursdAI Episodes - January 2025

Total Episodes: 5

---

## 📆 ThursdAI - Jan 30 - DeepSeek vs. Nasdaq, R1 everywhere, Qwen Max & Video, Open Source SUNO, Goose agents & more AI news

**Date:** January 30, 2025  
**Duration:** 1:54:46  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-30-deepseek-vs-nasdaq](https://sub.thursdai.news/p/thursdai-jan-30-deepseek-vs-nasdaq)

Hey folks, Alex here 👋

It’s official—grandmas (and the entire stock market) now know about DeepSeek. If you’ve been living under an AI rock, DeepSeek’s new R1 model just set the world on fire, rattling Wall Street (causing the biggest monetary loss for any company, ever!) and rocketing to #1 on the iOS App Store. This week’s ThursdAI show took us on a deep (pun intended) dive into the dizzying whirlwind of open-source AI breakthroughs, agentic mayhem, and big-company cat-and-mouse announcements. Grab your coffee (or your winter survival kit if you’re in Canada), because in true ThursdAI fashion, we’ve got at least a dozen bombshells to cover—everything from brand-new Mistral to next-gen vision models, new voice synthesis wonders, and big moves from Meta and OpenAI.

We’re also talking “reasoning mania,” as the entire industry scrambles to replicate, dethrone, or ride the coattails of the new open-source champion, R1. So buckle up—because if the last few days are any indication, 2025 is officially the Year of Reasoning (and quite possibly, the Year of Agents, or both!)

Open Source LLMs

DeepSeek R1 discourse Crashes the Stock Market

**One-sentence summary**: DeepSeek’s R1 “reasoning model” caused a frenzy this week, hitting #1 on the App Store and briefly sending NVIDIA’s stock plummeting in the process ($560B drop, largest monetary loss of any stock, ever)

Ever since DeepSeek R1 launched ([our technical coverate last week!](https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1?r=2imipa)), the buzz has been impossible to ignore—everyone from your mom to your local barista has heard the name. The speculation? DeepSeek’s new architecture apparently only cost $5.5 million to train, fueling the notion that high-level AI might be cheaper than Big Tech claims. Suddenly, people wondered if GPU manufacturers like NVIDIA might see shrinking demand, and the stock indeed took a short-lived 17% tumble. On the show, I joked, “My mom knows about DeepSeek—your grandma probably knows about it, too,” underscoring just how mainstream the hype has become.

Not everyone is convinced the cost claims are accurate. Even Dario Amodei of Anthropic weighed in with a blog post arguing that DeepSeek’s success *increases* the case for stricter AI export controls. 

Public Reactions

* **Dario Amodei’s blog**In “On DeepSeek and Export Controls,” Amodei argues that DeepSeek’s efficient scaling exemplifies why democratic nations need to maintain a strategic leadership edge—and enforce export controls on advanced AI chips. He sees Chinese breakthroughs as proof that AI competition is global and intense.

* **OpenAI Distillation Evidence**OpenAI mentioned it found “distillation traces” of GPT-4 inside R1’s training data. Hypocrisy or fair game? On ThursdAI, the panel mused that “everyone trains on everything,” so perhaps it’s a moot point.

* **Microsoft Reaction**Microsoft wasted no time, swiftly adding DeepSeek to Azure—further proof that corporations want to harness R1’s reasoning power, no matter where it originated.

* **Government reacted**Even officials in the government, David Sacks, US incoming AI & Crypto czar, discussed the fact that DeepSeek did "distillation" using the term somewhat incorrectly, and presidet Trump was asked about it.

* **API Outages**DeepSeek’s own API has gone in and out this week, apparently hammered by demand (and possibly DDoS attacks). Meanwhile, GPU clouds like Groq are showing up to accelerate R1 at 300 tokens/second, for those who must have it right now.

We've seen so many bad takes on the topic, from seething cope takes, to just gross misunderstandings from gov officials confusing the ios App with the OSS models, folks throwing conspiracy theories into the mix, claiming that $5.5M sum was a PsyOp. The fact of the matter is, DeepSeek R1 is an incredible model, and is now powering (just a week later), multiple products (more on this below) and experiences already, while pushing everyone else to compete (and give us reasoning models!)

Open Thoughts Reasoning Dataset

**One-sentence summary**: A community-led effort, “Open Thoughts,” released a new large-scale dataset (OpenThoughts-114k) of chain-of-thought reasoning data, fueling the open-source drive toward better reasoning models.

Worried about having enough labeled “thinking” steps to train your own reasoner? Fear not. The OpenThoughts-114k dataset aggregates chain-of-thought prompts and responses—114,000 of them—for building or fine-tuning reasoning LLMs. It’s now on [Hugging Face](https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k) for your experimentation pleasure. The ThursdAI panel pointed out how crucial these large, openly available reasoning datasets are. As **Wolfram** put it, “We can’t rely on the big labs alone. More open data means more replicable breakouts like DeepSeek R1.”

Mistral Small 2501 (24B)

**One-sentence summary**: Mistral AI returns to the open-source spotlight with a 24B model that fits on a single 4090, scoring over 81% on MMLU while under Apache 2.0.

Long rumored to be “going more closed,” Mistral AI re-emerged this week with Mistral-Small-24B-Instruct-2501—an Apache 2.0 licensed LLM that runs easily on a 32GB VRAM GPU. That 81% MMLU accuracy is no joke, putting it well above many 30B–70B competitor models. **It was described as** “the perfect size for local inference and a real sweet spot,” noting that for many tasks, 24B is “just big enough but not painfully heavy.” Mistral also finally started comparing themselves to Qwen 2.5 in official benchmarks—a big shift from their earlier reluctance, which we applaud! 

Berkeley TinyZero & RAGEN (R1 Replications)

**One-sentence summary**: Two separate projects (TinyZero and RAGEN) replicated DeepSeek R1-zero’s reinforcement learning approach, showing you can get “aha” reasoning moments with minimal compute.

If you were wondering whether R1 is replicable: yes, it is. **Berkeley’s TinyZero** claims to have reproduced the core R1-zero behaviors for $30 using a small 3B model. Meanwhile, the **RAGEN** project aims to unify RL + LLM + Agents with a minimal codebase. While neither replication is at R1-level performance, they demonstrate how quickly the open-source community pounces on new methods. “We’re now seeing those same ‘reasoning sparks’ in smaller reproductions,” said **Nisten**. “That’s huge.”

Agents

Codename Goose by Blocks ([X](https://x.com/blocks/status/1884292904753254488), [Github](https://block.github.io/goose/))

**One-sentence summary**: Jack Dorsey’s company Blocks released Goose, an open-source local agent framework letting you run keyboard automation on your machine.

Ever wanted your AI to press keys and move your mouse in real time? Goose does exactly that with AppleScript, memory extensions, and a fresh approach to “local autonomy.” On the show, I tried Goose, but found it occasionally “went rogue, trying to delete my WhatsApp chats.” Security concerns aside, Goose is significant: it’s an open-source playground for agent-building. The plugin system includes integration with Git, Figma, a knowledge graph, and more. If nothing else, Goose underscores how hot “agentic” frameworks are in 2025.

OpenAI’s Operator: One-Week-In

It’s been a week since **Operator** went live for Pro-tier ChatGPT users. “It’s the first agent that can run for multiple minutes without bugging me every single second,”. Yet it’s still far from perfect—captchas, login blocks, and repeated confirmations hamper tasks. The potential, though, is enormous: “I asked Operator to gather my [X.com](X.com) bookmarks and generate a summary. It actually tried,” I shared, “but it got stuck on three links and needed constant nudges.” **Simon Willison** added that it’s “a neat tech demo” but not quite a productivity boon yet. Next steps? Possibly letting the brand-new reasoning models (like O1 Pro Reasoning) do the chain-of-thought under the hood.

I also got tired of opening hundreds of tabs for operator, so I wrapped it in a macOS native app, that has native notifications and the ability to launch Operator tasks via a Raycast extension, if you're interested, you can find it on my [Github](https://github.com/altryne/wraperator/tree/main)

Browser-use / Computer-use Alternatives

In addition to Goose, the ThursdAI panel mentioned **browser-use** on [GitHub](https://github.com/browser-use/browser-use), plus numerous code interpreters. So far, none blow minds in reliability. But 2025 is evidently “the year of agents.” If you’re itching to offload your browsing or file editing to an AI agent, expect to tinker, troubleshoot, and yes, babysit. The show consensus? “It’s not about whether agents are coming, it’s about how soon they’ll become truly robust,” said **Wolfram**.

Big CO LLMs + APIs

Alibaba Qwen2.5-Max (& Hidden Video Model) ([Try It](https://chat.qwenlm.ai/))

**One-sentence summary**: Alibaba’s Qwen2.5-Max stands toe-to-toe with GPT-4 on some tasks, while also quietly rolling out video-generation features.

While Western media fixates on DeepSeek, Alibaba’s Qwen team quietly dropped the Qwen2.5-Max MoE model. It clocks in at 69% on MMLU-Pro—beating some OpenAI or Google offerings—and comes with a 1-million-token context window. And guess what? The official Chat interface apparently does hidden video generation, though Alibaba hasn’t publicized it in the English internet. 

In the Chinese AI internet, this video generation model is called [Tongyi Wanxiang](https://tongyi.aliyun.com/wanxiang/), and even has it’s own website, can support first and last video generation and looks really really good, they have a gallery up there, and it even has audio generation together with the video!

This one was an img2video, but the movements are really natural! 

Zuckerberg on LLama4 & LLama4 Mini

In Meta’s Q4 earnings call, Zuck was all about AI (sorry, Metaverse). He declared that LLama4 is in advanced training, with a smaller “LLama4 Mini” finishing pre-training. More importantly, a “reasoning model” is in the works, presumably influenced by the mania around R1. Some employees had apparently posted on Blind about “Why are we paying billions for training if DeepSeek did it for $5 million?” so the official line is that Meta invests heavily for top-tier scale. 

Zuck also doubled down on saying "Glasses are the perfect form factor for AI" , to which I somewhat agree, I love my Meta Raybans, I just wished they were integrated into the ios more. 

He also boasted about their HUGE datacenters, called Mesa, spanning the size of Manhattan, being built for the next step of AI. 

(Nearly) Announced: O3-Mini

Right before the ThursdAI broadcast, rumors swirled that OpenAI might reveal O3-Mini. It’s presumably GPT-4’s “little cousin” with a fraction of the cost. Then…silence. Sam Altman also mentioned they would be bringing o3-mini by end of January, but maybe the R1 crazyness made them keep working on it and training it a bit more? 🤔 

In any case, we'll cover it when it launches. 

This Week’s Buzz

We're still the #1 spot on Swe-bench verified with W&B programmer, and our CTO, Shawn Lewis, chatted with friends of the pod Swyx and Alessio about it! (give it a listen)

We have two upcoming events:

* [**AI.engineer**](AI.engineer) in New York (Feb 20–22). Weights & Biases is sponsoring, and I will broadcast ThursdAI live from the summit. If you snagged a ticket, come say hi—there might be a cameo from the “Chef.”

* **Toronto Tinkerer Workshops** (late February) in the University of Toronto. The Canadian AI scene is hot, so watch out for sign-ups (will add them to the show next week)

Weights & Biases also teased more features for LLM observability (Weave) and reminded folks of their new suite of evaluation tools. “If you want to know if your AI is actually better, you do evals,” **Alex** insisted. For more details, check out [wandb.me/weave](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=jan30) or tune into the next ThursdAI.

Vision & Video

DeepSeek - Janus Pro - multimodal understanding and image gen unified (1.5B & 7B)

**One-sentence summary**: Alongside R1, DeepSeek also released Janus Pro, a unified model for image understanding and generation (like GPT-4’s rumored image abilities).

DeepSeek apparently never sleeps. **Janus Pro** is MIT-licensed, 7B parameters, and can both parse images (SigLIP) and generate them (LlamaGen).  The model outperforms DALL·E 3 and SDXL! on some internal benchmarks—though at a modest 384×384 resolution. 

NVIDIA’s Eagle 2 Redux

**One-sentence summary**: NVIDIA re-released the Eagle 2 vision-language model with 4K resolution support, after mysteriously yanking it a week ago.

Eagle 2 is back, boasting multi-expert architecture, 16k context, and high-res video analysis. Rumor says it competes with big 70B param vision models at only 9B. But it’s overshadowed by Qwen2.5-VL (below). Some suspect NVIDIA is aiming to outdo Meta’s open-source hold on vision—just in time to keep GPU demand strong.

Qwen 2.5 VL - SOTA oss vision model is here 

**One-sentence summary**: Alibaba’s Qwen 2.5 VL model claims state-of-the-art in open-source vision, including 1-hour video comprehension and “object grounding.”

The Qwen team didn’t hold back: “It’s the final boss for vision,” joked **Nisten**. Qwen 2.5 VL uses advanced temporal modeling for video and can handle complicated tasks like OCR or multi-object bounding boxes. 

Featuring advances in precise object localization, video temporal understanding and agentic capabilities for computer, this is going to be the model to beat! 

Voice & Audio

YuE 7B (Open “Suno”)

Ever dream of building the next pop star from your code editor? YuE 7B is your ticket. This model, now under Apache 2.0, supports chain-of-thought creation of structured songs, multi-lingual lyrics, and references. It’s slow to infer, but it’s arguably the best open music generator so far in the open source

What's more, they have changed the license to apache 2.0 just before we went live, so you can use YuE everywhere! 

Refusion Fuzz

Refusion, a new competitor to paid audio models like Suno and Udio, launched “Fuzz,” offering free music generation online until GPU meltdown.

If you want to dabble in “prompt to jam track” without paying, check out [Refusion Fuzz](https://refusion.ai/fuzz). Will it match the emotional nuance of premium services like 11 Labs or Hauio? Possibly not. But hey, free is free.

Tools (that have integrated R1)

Perplexity with R1

In the [perplexity.ai](perplexity.ai) chat, you can choose “Pro with R1” if you pay for it,  harnessing R1’s improved reasoning to parse results. For some, it’s a major upgrade to “search-based question answering.” Others prefer it to paying for O1 or GPT-4. 

I always check Perplexity if it knows what the latest episode of ThursdAI was, and it's the first time it did a very good summary! I legit used it to research the show this week! It's really something. 

Meanwhile, [Exa.ai](Exa.ai) also integrated a “DeepSeek Chat” for your agent-based workflows. Like it or not, R1 is everywhere.

[Krea.ai](Krea.ai) with DeepSeek

Our friends at Krea, an AI art tool aggregator, also hopped on the R1 bandwagon for chat-based image searching or generative tasks.

Conclusion

Key Takeaways

* **DeepSeek’s R1 has massive cultural reach**, from #1 apps to spooking the stock market.

* **Reasoning mania** is upon us—everyone from Mistral to Meta wants a piece of the logic-savvy LLM pie.

* **Agentic frameworks** like Goose, Operator, and browser-use are proliferating, though they’re still baby-stepping through reliability issues.

* **Vision and audio** get major open-source love, with Janus Pro, Qwen 2.5 VL, YuE 7B, and more reshaping multimodality.

* **Big Tech** (Meta, Alibaba, OpenAI) is forging ahead with monster models, multi-billion-dollar projects, and cross-country expansions in search of the best reasoning approaches.

At this point, it’s not even about where the next big model drop comes from; it’s about how quickly the entire ecosystem can adopt (or replicate) that new methodology. 

Stay tuned for next week’s ThursdAI, where we’ll hopefully see new updates from OpenAI (maybe O3-Mini?), plus the ongoing race for best agent. Also, catch us at [AI.engineer](AI.engineer) in NYC if you want to talk shop or share your own open-source success stories. Until then, keep calm and carry on training.

TLDR

* **Open Source LLMs**

* DeepSeek Crashes the Stock Market: Did $5.5M training or hype do it?

* Open Thoughts Reasoning Dataset OpenThoughts-114k ([X](https://x.com/madiator/status/1884284103354376283), [HF](https://t.co/MUAJd9mWZD))

* Mistral Small 2501 (24B, Apache 2.0) ([HF](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501))

* Berkeley TinyZero & RAGEN (R1-Zero Replications) ([Github](https://app.reflect.app/g/altryne/github.com/Jiayi-Pan/TinyZero), [WANDB](https://app.reflect.app/g/altryne/wandb.ai/jiayipan/TinyZero))

* Allen Institute - Tulu 405B ([Blog](https://allenai.org/blog/tulu-3-405B), [HF](https://huggingface.co/collections/allenai/tulu-3-models-673b8e0dc3512e30e7dc54f5))

* **Agents**

* Goose by Blocks (local agent framework) - ([X](https://x.com/blocks/status/1884292904753254488), [Github](https://block.github.io/goose/))

* Operator (OpenAI) – One-Week-In ([X](https://x.com/altryne/status/1883056651332448761))

* Browser-use - oss version of Operator ([Github](https://github.com/browser-use/browser-use))

* **Big CO LLMs + APIs**

* Alibaba Qwen2.5-Max (+ hidden video model) - ([X](https://x.com/Alibaba_Qwen/status/1884263157574820053), [Try it](https://chat.qwenlm.ai/))

* Zuckerberg on LLama4 & “Reasoning Model” ([X](https://x.com/altryne/status/1884778839009796411))

* **This Week’s Buzz**

* Shawn Lewis [interview](https://x.com/latentspacepod/status/1884065983062761548) on [Latent Space](https://open.substack.com/pub/swyx) with [swyx & Alessio](https://substack.com/profile/89230629-swyx-and-alessio) 

* We’re sponsoring the [ai.engineer](https://ai.engineer) upcoming summit in NY (Feb 19-22), come say hi! 

* After that, we’ll host 2 workshops with AI Tinkerers Toronto (Feb 23-24), make sure you’re signed up to [Toronto Tinkerers](https://toronto.aitinkerers.org/) to receive the invite (we were sold out quick last time!) 

* **Vision & Video**

* DeepSeek Janus Pro - 1.5B and 7B ([Github](https://github.com/deepseek-ai/Janus/tree/main?tab=readme-ov-file), [Try It](https://huggingface.co/spaces/AP123/Janus-Pro-7b))

* NVIDIA Eagle 2 ([Paper](http://arxiv.org/abs/2501.14818), [Model](https://huggingface.co/collections/nvidia/eagle-2-6764ba887fa1ef387f7df067), [Demo](https://eagle-vlm.xyz/))

* Alibaba Qwen 2.5 VL  ([Project](https://qwenlm.github.io/blog/qwen2.5-vl/), [HF](huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct), [Github](https://github.com/QwenLM/Qwen2.5-VL), [Try It](https://chat.qwenlm.ai/))

* **Voice & Audio**

* Yue 7B (Open Suno) - ([Demo](https://fal.ai/models/fal-ai/yue/requests), [HF](https://huggingface.co/m-a-p), [Github](https://github.com/multimodal-art-projection/YuE))

* Refusion Fuzz ([free for now](https://refusion.ai/fuzz))

* **Tools**

* Perplexity with R1 (choose Pro with R1) 

* Exa integrated R1 for free ([demo](https://demo.exa.ai/deepseekchat))

* **Participants**

* Alex Volkov ([@altryne](https://x.com/altryne))

* Wolfram Ravenwolf ([@WolframRvnwlf](https://x.com/WolframRvnwlf))

* Nisten Tahiraj ([@nisten](https://x.com/nisten/) )

* LDJ ([@ldjOfficial](https://x.com/ldjconfirmed/status/1884678546431373764))

* Simon Willison ([@simonw](https://x.com/simonw/status/1882507741694189706))

* W&B Weave ([@weave_wb](https://x.com/weave_wb)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jan-30-deepseek-vs-nasdaq/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jan-30-deepseek-vs-nasdaq?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1NjEyNjk2MCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.6QbGf5tubwVSCAodCc00_jOtQGVlb4gREqUbWTum14c&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Jan 23, 2025 - 🔥 DeepSeek R1 is HERE, OpenAI Operator Agent, $500B AI manhattan project, ByteDance UI-Tars, new Gemini Thinker & more AI news

**Date:** January 24, 2025  
**Duration:** 1:49:39  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1](https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1)

What a week, folks, what a week! Buckle up, because ThursdAI just dropped, and this one's a doozy. We're talking seismic shifts in the open source world, a potential game-changer from DeepSeek AI that's got everyone buzzing, and oh yeah, just a casual $500 BILLION infrastructure project announcement. Plus, OpenAI finally pulled the trigger on "Operator," their agentic browser thingy – though getting it to actually *operate* proved to be a bit of a live show adventure, as you'll hear. 

This week felt like one of those pivotal moments in AI, a real before-and-after kind of thing. DeepSeek's R1 hit the open source scene like a supernova, and suddenly, top-tier reasoning power is within reach for anyone with a Mac and a dream. And then there's OpenAI's Operator, promising to finally bridge the gap between chat and action. Did it live up to the hype? Well, let's just say things got interesting.

As I’m writing this, White House just published that an Executive Order on AI was just signed and published as well, what a WEEK.

Open Source AI Goes Nuclear: DeepSeek R1 is HERE!

Hold onto your hats, open source AI just went supernova! This week, the Chinese Whale Bros – DeepSeek AI, that quant trading firm turned AI powerhouse – dropped a bomb on the community in the best way possible: **R1, their reasoning model, is now open source under the MIT license!** As I said on the show, "Open source AI has never been as hot as this week."

This isn't just *a* model, folks. DeepSeek unleashed a whole arsenal: two full-fat R1 models (DeepSeek R1 and DeepSeek R1-Zero), and a whopping six distilled finetunes based on Qwen (1.5B, 7B, 14B, and 32B) and Llama (8B, 72B). 

One stat that blew my mind, and Nisten's for that matter, is that **DeepSeek-R1-Distill-Qwen-1.5B, the *****tiny***** 1.5 billion parameter model, is outperforming GPT-4o and Claude-3.5-Sonnet on math benchmarks!** "This 1.5 billion parameter model that now does this. It's absolutely insane," I exclaimed on the show. We're talking 28.9% on AIME and 83.9% on MATH. Let that sink in. A model you can probably run on your phone is schooling the big boys in math.

License-wise, it's MIT, which as Nisten put it, "MIT is like a jailbreak to the whole legal system, pretty much. That's what most people don't realize. It's like, this is, it's not my problem. You're a problem now." Basically, do whatever you want with it. Distill it, fine-tune it, build Skynet – it's all fair game.

And the vibes? "Vibes are insane," as I mentioned on the show. Early benchmarks are showing R1 models trading blows with o1-preview and o1-mini, and even nipping at the heels of the full-fat o1 in some areas. Check out these numbers:

And the price? Forget about it. We're talking 50x cheaper than o1 currently. DeepSeek R1 API is priced at $0.14 / 1M input tokens and $2.19 / 1M output tokens, compared to OpenAI's o1 at $15.00 / 1M input and a whopping $60.00 / 1M output. Suddenly, high-quality reasoning is democratized.

LDJ highlighted the "aha moment" in DeepSeek's paper, where they talk about how reinforcement learning enabled the model to re-evaluate its approach and "think more." It seems like simple RL scaling, combined with a focus on reasoning, is the secret sauce. No fancy Monte Carlo Tree Search needed, apparently!

But the real magic of open source is what the community does with it. Pietro Schirano joined us to talk about his "Retrieval Augmented Thinking" (RAT) approach, where he extracts the thinking process from R1 and transplants it to other models. "And what I found out is actually by doing so, you may even like smaller, quote unquote, you know, less intelligent model actually become smarter," Pietro explained. Frankenstein models, anyone? (John Lindquist has a tutorial on how to do it [here](https://egghead.io/combine-deep-seek-r1-reasoning-with-gpt-3-5-turbo-for-the-cheapest-fastest-and-best-ai~24oy1))

And then there's the genius hack from Voooogel, who figured out how to emulate a "reasoning_effort" knob by simply replacing the "end" token with "Wait, but".  "This tricks the model into keeps thinking," as I described it. Want your AI to really ponder the meaning of life (or just 1+1)? Now you can, thanks to open source tinkering.

Georgi Gerganov, the legend behind llama.cpp, even jumped in with a two-line snippet to enable speculative decoding, boosting inference speeds on the 32B model on my Macbook from a sluggish 5 tokens per second to a much more respectable 10-11 tokens per second. Open source collaboration at its finest and it's only going to get better! 

Thinking like a Neurotic

Many people really loved the way R1 thinks, and what I found astonishing is that I just sent "hey" and the thinking went into a whole 5 paragraph debate of how to answer, a user on X answered with "this is Woody Allen-level of Neurotic" which... nerd sniped me so hard! I used Hauio Audio (which is great!) and ByteDance latentSync and gave R1 a voice! It's really something when you hear it's inner monologue being spoken out like this! 

ByteDance Enters the Ring: UI-TARS Controls Your PC

Not to be outdone in the open source frenzy, ByteDance, the TikTok behemoth, dropped UI-TARS, a set of models designed to control your PC. And they claim SOTA performance, beating even Anthropic's computer use models and, in some benchmarks, GPT-4o and Claude.

UI-TARS comes in 2B, 7B, and 72B parameter flavors, and ByteDance even released desktop apps for Mac and PC to go along with them. "They released an app it's called the UI TARS desktop app. And then, this app basically allows you to Execute the mouse clicks and keyboard clicks," I explained during the show.

While I personally couldn't get the desktop app to work flawlessly (quantization issues, apparently), the potential is undeniable. Imagine open source agents controlling your computer – the possibilities are both exciting and slightly terrifying. As Nisten wisely pointed out, "I would use another machine. These things are not safe to tell people. I might actually just delete your data if you, by accident." Words to live by, folks.

LDJ chimed in, noting that UI-TARS seems to excel particularly in operating system-level control tasks, while OpenAI's leaked "Operator" benchmarks might show an edge in browser control. It's a battle for desktop dominance brewing in open source!

Noting that the common benchmark between Operator and UI-TARS is OSWorld, UI-Tars launched with a SOTA 

Humanity's Last Exam: The Benchmark to Beat

Speaking of benchmarks, a new challenger has entered the arena: **Humanity's Last Exam (HLE).** A cool new unsaturated bench of 3,000 *challenging* questions across over a hundred subjects, crafted by nearly a thousand subject matter experts from around the globe. "There's no way I'm answering any of those myself. I need an AI to help me," I confessed on the show.

And guess who's already topping the HLE leaderboard? You guessed it: **DeepSeek R1, with a score of 9.4%!** "Imagine how hard this benchmark is if the top reasoning models that we have right now... are getting less than 10 percent completeness on this," MMLU and Math are getting saturated? HLE is here to provide a serious challenge. Get ready to hear a lot more about HLE, folks.

Big CO LLMs + APIs: Google's Gemini Gets a Million-Token Brain

While open source was stealing the show, the big companies weren't completely silent. Google quietly dropped an update to **Gemini Flash Thinking**, their experimental reasoning model, and it's a big one. We're talking **1 million token context window** and code execution capabilities now baked in!

"This is Google's scariest model by far ever built ever," Nisten declared. "This thing, I don't like how good it is. This smells AGI-ish" High praise, and high concern, coming from Nisten! Benchmarks are showing significant performance jumps in math and science evals, and the speed is, as Nisten put it, "crazy usable." They have enabled the whopping 1M context window for the new Gemini Flash 2.0 Thinking Experimental (long ass name, maybe let's call it G1?) and I agree, it's really really good!

And unlike some other reasoning models *cough* OpenAI *cough*, Gemini Flash Thinking **shows you its thinking process!** You can actually see the chain of thought unfold, which is incredibly valuable for understanding and debugging. Google's Gemini is quietly becoming a serious contender in the reasoning race (especially with Noam Shazeer being responsible for it!)

OpenAI's "Operator" - Agents Are (Almost) Here

The moment we were all waiting for (or at least, *I* was): OpenAI finally unveiled **Operator**, their first foray into Level 3 Autonomy - agentic capabilities with ChatGPT. Sam Altman himself hyped it up as "AI agents are AI systems that can do work for you. You give them a task and they go off and do it." Sounds amazing, right?

Operator is built on a new model called **CUA (Computer Using Agent)**, trained on top of GPT-4, and it's designed to control a web browser in the cloud, just like a human would, using screen pixels, mouse, and keyboard. "This is just using screenshots, no API, nothing, just working," one of the OpenAI presenters emphasized. 

They demoed Operator booking restaurant reservations on OpenTable, ordering groceries on Instacart, and even trying to buy Warriors tickets on StubHub (though that demo got a little… glitchy). The idea is that you can delegate tasks to Operator, and it'll go off and handle them in the background, notifying you when it needs input or when the task is complete.

As I'm writing these words, I have an Operator running trying to get me some fried rice, and another one trying to book me a vacation with kids over the summer, find some options and tell me what it found. 

Benchmarks-wise, OpenAI shared numbers for OSWorld (38.1%) and WebArena (58.1%), showing Operator outperforming previous SOTA but still lagging behind human performance. "Still a way to go," as they admitted. But the potential is massive.

The catch? **Operator is initially launching in the US for Pro users only, and even *****then*****, it wasn't exactly smooth sailing.** I immediately paid the $200/mo to try it out (pro mode didn't convince me, unlimited SORA videos didn't either, operator definitely did, SOTA agents from OpenAI is definitely something I must try!) and my first test? Writing a tweet 😂 Here's a video of that first attempt, which I had to interrupt 1 time. 

But hey, it's a "low key research preview" right? And as Sam Altman said, "This is really the beginning of this product. This is the beginning of our step into Agents Level 3 on our tiers of AGI" Agentic ChatGPT is coming, folks, even if it's taking a slightly bumpy route to get here.

BTW, while I'm writing these words, Operator is looking up some vacation options for me and is sending me notifications about them, what a world and we've only just started 2025!

Project Stargate: $500 Billion for AI Infrastructure

If R1 and Operator weren't enough to make your head spin, how about a **$500 BILLION "Manhattan Project for AI infrastructure"?** That's exactly what OpenAI, SoftBank, and Oracle announced this week: [**Project Stargate**](https://openai.com/index/announcing-the-stargate-project/)**.**

"This is insane," I exclaimed on the show. "Power ups for the United States compared to like, other, other countries, like 500 billion commitment!" We're talking about a massive investment in data centers, power plants, and everything else needed to fuel the AI revolution. 2% of the US GDP, according to some estimates!

Larry Ellison even hinted at using this infrastructure for… curing cancer with personalized vaccines. Whether you buy into that or not, the scale of this project is mind-boggling. As LDJ explained, "It seems like it is very specifically for open AI. Open AI will be in charge of operating it. And yeah, it's, it sounds like a smart way to actually kind of get funding and investment for infrastructure without actually having to give away open AI equity."

And in a somewhat related move, Microsoft, previously holding exclusive cloud access for OpenAI, has opened the door for OpenAI to potentially run on other clouds, with Microsoft's approval if "they cannot meet demant".  Is AGI closer than we think? Sam Altman himself downplayed the hype, tweeting, "Twitter hype is out of control again. We're not going to deploy AGI next month, nor have we built it. We have some very cool stuff for you, but please chill and cut your expectations a hundred X."

But then he drops Operator and a $500 billion infrastructure bomb in the same week and announces that o3-mini is going to be available for the FREE tier of chatGPT.

Sure, Sam, *we're going to chill... yeah right. *

This Week's Buzz at Weights & Biases: SWE-bench SOTA!

Time for our weekly dose of Weights & Biases awesomeness! This week, our very own CTO, Shawn Lewis, **broke the SOTA on SWE-bench Verified!** That's right, W&B Programmer, Shawn's agentic framework built on top of o1, achieved a **64.6%** solve rate on this notoriously challenging coding benchmark.

Shawn detailed his journey in a [blog post](https://wandb.ai/wandb/agents/reports/Creating-a-state-of-the-art-AI-programming-agent-with-OpenAI-s-o1--VmlldzoxMTAyODI2Ng?utm_source=thursdai&utm_medium=referral&utm_campaign=Jan9), highlighting the importance of iteration and evaluation – powered by Weights & Biases [Weave](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=jan23), naturally. He ran over 1000 evaluations to reach this SOTA result! Talk about eating your own dogfood!

REMOVING BARRIERS TO AMERICAN LEADERSHIP IN ARTIFICIAL INTELLIGENCE - Executive order

Just now as I’m editing the podcast, President Trump signed into effect an executive order for AI, and here are the highlights. 

- Revokes existing AI policies that hinder American AI innovation

- Aims to solidify US as global leader in AI for human flourishing, competitiveness, and security

- Directs development of an AI Action Plan within 180 days

- Requires immediate review and revision of conflicting policies

- Directs OMB to revise relevant memos within 60 days

- Preserves agency authority and OMB budgetary functions

- Consistent with applicable law and funding availability

- Seeks to remove barriers and strengthen US AI dominance

This marks such a significant pivot into AI acceleration, removing barriers, acknowledging that AI is a huge piece of our upcoming future and that US really needs to innovate here, become the global leader, and remove regulation and obstacles. The folks that work on this behind the scenes, Sriram Krishan (previously A16Z) and David Sacks, are starting to get into the government and implement those policies, so we’re looking forward to what will come form that! 

Vision & Video: Nvidia's Vanishing Eagle 2 & Hugging Face's Tiny VLM

In the world of vision and video, Nvidia teased us with **Eagle 2**, a series of frontier vision-language models promising 4K HD input, long-context video, and grounding capabilities with some VERY impressive evals. Weights were released, then…yanked. "NVIDIA released Eagle 2 and then yanked it back. So I don't know what's that about," I commented. Mysterious Nvidia strikes again.

On the brighter side, Hugging Face released **SmolVLM**, a truly *tiny* vision-language model, coming in at just 256 million and 500 million parameters. "This tiny model that runs in like one gigabyte of RAM or some, some crazy things, like a smart fridge" I exclaimed, impressed. The 256M model even outperforms their previous 80 *billion* parameter Idefics model from just 17 months ago. Progress marches on, even in tiny packages.

AI Art & Diffusion & 3D: Hunyuan 3D 2.0 is State of the Art

For the artists and 3D enthusiasts, Tencent's **Hunyuan 3D 2.0** dropped this week, and it's looking seriously impressive. "Just look at this beauty," I said, showcasing a generated dragon skull. "Just look at this."

Hunyuan 3D 2.0 boasts two models: Hunyuan3D-DiT-v2-0 for shape generation and Hunyuan3D-Paint-v2-0 for coloring. Text-to-3D and image-to-3D workflows are both supported, and the results are, well, see for yourself:

If you're looking to move beyond 2D images, Hunyuan 3D 2.0 is definitely worth checking out.

Tools: ByteDance Clones Cursor with Trae

And finally, in the "tools" department, ByteDance continues its open source blitzkrieg with **Trae**, a free Cursor competitor. "ByteDance drops Trae, which is a cursor competitor, which is free for now" I announced on the show, so if you don't mind your code being sent to... china somewhere, and can't afford Cursor, this is not a bad alternative! 

Trae imports your Cursor configs, supports Claude 3.5 and GPT-4o, and offers a similar AI-powered code editing experience, complete with chat interface and "builder" (composer) mode. The catch? Your code gets sent to a server in China. If you're okay with that, you've got yourself a free Cursor alternative. "If you're okay with your like code getting shared with ByteDance, this is a good option for you," I summarized. Decisions, decisions.

Phew! That was a whirlwind tour through another insane week in AI. From DeepSeek R1's open source reasoning revolution to OpenAI's Operator going live, and Google's million-token Gemini brain, it's clear that the pace of innovation is showing no signs of slowing down. 

Open source is booming, agents are inching closer to reality, and the big companies are throwing down massive infrastructure investments. We're accelerating as fuck, and it's only just beginning, hold on to your butts.

Make sure to dive into the show notes below for all the links and details on everything we covered. And don't forget to give R1 a spin – and maybe try out that "reasoning_effort" hack. Just don't blame me if your AI starts having an existential crisis.

And as a final thought, channeling my inner Woody Allen-R1, "Don't overthink too much. enjoy our one. Enjoy the incredible things we received this week from open source."

See you all next week for more ThursdAI madness! And hopefully, by then, Operator will actually be operating. 😉

TL;DR and show notes

* **Open Source LLMs**

* DeepSeek R1 - MIT licensed SOTA open source reasoning model ([HF](https://huggingface.co/deepseek-ai), X)

* ByteDance UI-TARS - PC control models ([HF](https://huggingface.co/bytedance-research/UI-TARS-7B-SFT), [Github](https://github.com/bytedance/UI-TARS-desktop) )

* HLE - Humanity's Last Exam benchmark ([Website](https://lastexam.ai/))

* **Big CO LLMs + APIs**

* SoftBank, Oracle, OpenAI Stargate Project - $500B AI infrastructure ([OpenAI Blog](https://openai.com/index/announcing-the-stargate-project/))

* Google Gemini Flash Thinking 01-21 - 1M context, Code execution, Better Evals ([X](https://x.com/NoamShazeer/status/1881845900659896773))

* OpenAI Operator - Agentic browser in ChatGPT Pro [operator.chatgpt.com](operator.chatgpt.com)

* Anthropic launches citations in API ([blog](https://docs.anthropic.com/en/docs/build-with-claude/citations))

* Perplexity SonarPRO Search API and an Android AI assistant ([X](https://x.com/perplexity_ai/status/1882466239123255686))

* **This weeks Buzz 🐝**

* W&B broke SOTA SWE-bench verified ([W&B Blog](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=jan23))

* **Vision & Video**

* HuggingFace SmolVLM - Tiny VLMs - runs even on WebGPU ([HF](https://huggingface.co/spaces/HuggingFaceTB/SmolVLM-256M-Instruct-WebGPU))

* **AI Art & Diffusion & 3D**

* Hunyuan 3D 2.0 - SOTA open-source 3D ([HF](https://huggingface.co/tencent/Hunyuan3D-2))

* **Tools**

* ByteDance Trae - Cursor competitor (Trae AI: [https://trae.ai/)](https://trae.ai/))

* **Show Notes:** 

* Pietro Skirano RAT - Retrieval augmented generation ([X](https://x.com/skirano/status/1881854481304047656))

* Run DeepSeek with more “thinking” script ([Gist](https://gist.github.com/vgel/8a2497dc45b1ded33287fa7bb6cc1adc)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1NTU3ODcxNCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.InT8qY8h5BoTDaMj-TtHYB8zDF9RhzZjEeWZtjRI5sI&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Jan 16, 2025 - Hailuo 4M context LLM, SOTA TTS in browser, OpenHands interview & more AI news

**Date:** January 17, 2025  
**Duration:** 1:40:32  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-16-2025-hailuo-4m-context](https://sub.thursdai.news/p/thursdai-jan-16-2025-hailuo-4m-context)

Hey everyone, Alex here 👋 

Welcome back, to an absolute banger of a week in AI releases, highlighted with just massive Open Source AI push. We're talking a MASSIVE 4M context window context window model from Hailuo (remember when a jump from 4K to 16K seemed like a big deal?), a 8B omni model that lets you livestream video and glimpses of Agentic ChatGPT? 

This week's ThursdAI was jam-packed with so much open source goodness that the big companies were practically silent. But don't worry, we still managed to squeeze in some updates from OpenAI and Mistral, along with a fascinating new paper from Sakana AI on self-adaptive LLMs. Plus, we had the incredible Graham Neubig, from All Hands AI, join us to talk about Open Hands (formerly OpenDevin) and even contributed to our free, LLM Evaluation course on Weights & Biases!

Before we dive in, a friend asked me over dinner, what are the main 2 things that happened in AI in 2024, and this week highlights one of those trends. Most of the Open Source is now from China. This week, we got MiniMax from Hailuo, OpenBMB with a new MiniCPM, InternLM came back and most of the rest were Qwen finetunes. Not to mention DeepSeek. Wanted to highlight this significant narrative change and that this is being done despite the chip export restrictions. 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Open Source AI & LLMs

MiniMax-01: 4 Million Context, 456 Billion Parameters, and Lightning Attention 

This came absolutely from the left field, given that we've seen no prior LLMs from Haulio, the company previously releasing video models with consistent characters. Dropping a massive 456B mixture of experts model (45B active parameters) with such a long context support in open weights, but also with very significant benchmarks that compete with Gpt-4o, Claude and DeekSeek v3 (75.7 MMLU-pro, 89 IFEval, 54.4 GPQA)

They have trained the model on up to 1M context window and then extended it to 4M with ROPE scaling methods ([our coverage](https://sub.thursdai.news/p/thursdai-sunday-special-extending?utm_source=publication-search) of RoPE) during Inference. MiniMax-Text-01 adopts a hybrid architecture that combines Lightning Attention, Softmax Attention and Mixture-of-Experts (MoE) with 45B active parameters. 

I gotta say, when we started talking about context window, imagining a needle in a haystack graph that shows 4M, in the open source seemed far fetched, though we did say that theoretically, there may not be a limit to context windows. I just always expected that limit to be unlocked by transformers alternative architectures like Mamba or other State Space Models.

Vision, API and Browsing - Minimax-VL-01

It feels like such a well rounded and complete release, that it highlights just how mature company that is behind it. They have also released a vision version of this model, that includes a 300M param Vision Transformer on top (trained with 512B vision language tokens) that features dynamic resolution and boasts very high DocVQA and ChartQA scores. 

Not only did these two models were released in open weights, they also launched as a unified API endpoint (supporting up to 1M tokens) and it's  cheap! $0.2/1M input and $1.1/1M output tokens! AFAIK this is only the 3rd API that supports this much context, after Gemini at 2M and Qwen Turbo that supports 1M as well.

Surprising web browsing capabilities

You can play around with the model on their website, [hailuo.ai](https://www.hailuo.ai) which also includes web grounding, which I found quite surprising to find out, that they are beating chatGPT and Perplexity on how fast they can find information that just happened that same day! Not sure what search API they are using under the hood but they are very quick. 

8B chat with video model omni-model from OpenBMB

OpenBMB has been around for a while and we've seen consistently great updates from them on the MiniCPM front, but this one takes the cake! 

This is a complete omni modal end to end model, that does video streaming, audio to audio and text understanding, all on a model that can run on an iPad! 

They have a demo interface that is very similar to the chatGPT demo from spring of last year, and allows you to stream your webcam and talk to the model, but this is just an 8B parameter model we're talking about! It's bonkers! 

They are boasting some incredible numbers, and to be honest, I highly doubt  their methodology in textual understanding, because, well, based on my experience alone, this model understands less than close to chatGPT advanced voice mode, but miniCPM has been doing great visual understanding for a while, so ChartQA and DocVQA are close to SOTA. 

But all of this doesn't matter, because, I say again, just a little over a year ago, Google released a video announcing these capabilities, having an AI react to a video in real time, and it absolutely blew everyone away, and it was [FAKED](https://techcrunch.com/2023/12/07/googles-best-gemini-demo-was-faked/). And this time a year after, we have these capabilities, essentially, in an 8B model that runs on device 🤯 

Voice & Audio 

This week seems to be very multimodal, not only did we get an omni-modal from OpenBMB that can speak, and last week's Kokoro still makes a lot of waves, but this week there were a lot of voice updates as well

Kokoro.js - run the SOTA open TTS now in your browser

Thanks to friend of the pod Xenova (and the fact that Kokoro was released with ONNX weights), we now have kokoro.js, or npm -i kokoro-js if you will. 

This allows you to install and run Kokoro, the best tiny TTS model, completely within your browser, with a tiny 90MB download and it sounds really good (demo [here](https://huggingface.co/spaces/webml-community/kokoro-web))

Hailuo T2A - Emotional text to speech + API 

Hailuo didn't rest on their laurels of releasing a huge context window LLM, they also released a new voice framework (tho not open sourced) this week, and it sounds remarkably good (competing with 11labs) 

They have all the standard features like Voice Cloning, but claim to have a way to preserve the emotional undertones of a voice. They also have 300 voices to choose from and professional effects applied on the fly, like acoustics or telephone filters. (Remember, they have a video model as well, so assuming that some of this is to for the holistic video production) 

What I specifically noticed is their "emotional intelligence system" that's either automatic or can be selected from a dropdown. I also noticed their "lax" copyright restrictions, as one of the voices that was called "Imposing Queen" sounded just like a certain blonde haired heiress to the iron throne from a certain HBO series. 

When I generated a speech worth of that queen, I noticed that the emotion in that speech sounded very much like an actress would read them, and unlike any old TTS, just listen to it in the clip above, I don't remember getting TTS outputs with this much emotion from anything, maybe outside of advanced voice mode! Quite impressive!

This Weeks Buzz from Weights & Biases - AGENTS!

Breaking news from W&B as our CTO [just broke](https://x.com/shawnup/status/1880004026957500434) SWE-bench Verified SOTA, with his own o1 agentic framework he calls W&B Programmer 😮 at **64.6% **of the issues!

Shawn describes how he achieved this massive breakthrough [here](https://medium.com/@shawnup/the-best-ai-programmer-from-weights-biases-04cf8127afd8) and we'll be publishing more on this soon, but the highlight for me is he ran over 900 evaluations during the course of this, and tracked all of them in [Weave](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=Jan16)! 

We also have an upcoming event in NY, on Jan 22nd, if you're there, come by and learn how to evaluate your AI agents, RAG applications and hang out with our team! (Sign up [here](https://lu.ma/eufkbeem?utm_source=thursdai&utm_medium=referral&utm_campaign=Jan16))

Big Companies & APIs

OpenAI adds chatGPT tasks - first agentic feature with more to come! 

We finally get a glimpse of an agentic chatGPT, in the form of scheduled tasks! Deployed to all users, it is now possible to select gpt-4o with tasks, and schedule tasks in the future. 

You can schedule them in natural language, and then will execute a chat (and maybe perform a search or do a calculation) and then send you a notification (and an email!) when the task is done! 

A bit underwhelming at first, as I didn't really find a good use for this yet, I don't doubt that this is just a building block for something more Agentic to come that can connect to my email or calendar and do actual tasks for me, not just... save me from typing the chatGPT query at "that time" 

Mistral CodeStral 25.01 - a new #1 coding assistant model

An updated Codestral was released at the beginning of the week, and TBH I've never seen the vibes split this fast on a model. 

While it's super exciting that Mistral is placing a coding model at #1 on the LMArena CoPilot's arena, near Claude 3.5 and DeepSeek, the fact that this new model is not released weights is really a bummer (especially as a reference to the paragraph I mentioned on top) 

We seem to be closing down on OpenSource in the west, while the Chinese labs are absolutely crushing it (while also releasing in the open, including Weights, Technical papers). 

Mistral has released this model in API and via a collab with the Continue dot dev coding agent, but they used to be the darling of the open source community by releasing great models! 

Also notable, a very quick new benchmark post release was dropped that showed a significant difference between their reported benchmarks and how it performs on Aider polyglot 

There was way more things for this week than we were able to cover, including a new and exciting transformers squared new architecture from Sakana, a new open source TTS with voice cloning and a few other open source LLMs, one of which cost only $450 to train! All the links in the TL;DR below! 

TL;DR and show notes

* **Open Source LLMs** 

* MiniMax-01 from Hailuo - 4M context 456B (45B A) LLM ([Github](https://github.com/MiniMax-AI/MiniMax-01), [HF](https://huggingface.co/MiniMaxAI), [Blog](https://www.minimaxi.com/en/news/minimax-01-series-2), [Report](https://filecdn.minimax.chat/_Arxiv_MiniMax_01_Report.pdf))

* Jina - reader V2 model - HTML 2 Markdown/JSON ([HF](https://huggingface.co/jinaai/ReaderLM-v2))

* InternLM3-8B-Instruct - apache 2 License ([Github](https://github.com/InternLM/InternLM), [HF](https://huggingface.co/internlm))

* OpenBMB - **MiniCPM-o 2.6** - Multimodal Live Streaming on Your Phone ([HF](https://huggingface.co/openbmb/MiniCPM-o-2_6), [Github](https://github.com/OpenBMB/MiniCPM-o), [Demo](https://minicpm-omni-webdemo-us.modelbest.cn/))

* KyutAI - Helium-1 2B - Base ([X](https://x.com/kyutai_labs/thread/1878857673174864318), [HF](https://huggingface.co/kyutai/helium-1-preview-2b))

* Dria-Agent-α - 3B model that outputs python code ([HF](https://huggingface.co/driaforall/Dria-Agent-a-3B))

* Sky-T1, a ‘reasoning’ AI model that can be trained for less than $450 ([blog](https://novasky-ai.github.io/posts/sky-t1/))

* **Big CO LLMs + APIs**

* OpenAI launches ChatGPT tasks ([X](https://x.com/OpenAI/status/1879267274185756896))

* Mistral - new CodeStral 25.01 ([Blog](https://mistral.ai/news/codestral-2501/), no Weights)

* Sakana AI - Transformer²: Self-Adaptive LLMs ([Blog](https://sakana.ai/transformer-squared))

* **This weeks Buzz **

* Evaluating RAG Applications Workshop - NY, Jan 22, W&B and PineCone ([Free Signup](https://lu.ma/eufkbeem))

* Our evaluations course is going very strong! (chat w/ Graham Neubig) ([https://wandb.me/evals-t](https://wandb.me/evals-t))

* **Vision & Video**

* Luma releases Ray2 video model ([Web](https://lumalabs.ai/ray))

* **Voice & Audio**

* Hailuo **T2A-01-HD** - Emotions Audio Model from Hailuo ([X](https://x.com/Hailuo_AI/status/1879554062993195421), [Try It](https://t.co/r58fjgvJ7w))

* OuteTTS 0.3 - 1B & 500M - zero shot voice cloning model ([HF](https://huggingface.co/collections/OuteAI/outetts-03-6786b1ebc7aeb757bc17a2fa))

* Kokoro.js - 80M SOTA TTS in your browser! (X, [Github](https://github.com/hexgrad/kokoro/pull/3), [try it](https://huggingface.co/spaces/webml-community/kokoro-web) )

* **AI Art & Diffusion & 3D**

* Black Forest Labs - Finetuning for Flux Pro and Ultra via API ([Blog](https://blackforestlabs.ai/announcing-the-flux-pro-finetuning-api/))

* **Show Notes and other Links**

* Hosts - Alex Volkov ([@altryne](https://x.com/altryne)), Wolfram RavenWlf ([@WolframRvnwlf](https://twitter.com/WolframRvnwlf)), Nisten Tahiraj ([@nisten](https://x.com/nisten/))

* Guest - Graham Neubig ([@gneubig](https://x.com/gneubig)) from All Hands AI ([@allhands_ai](https://x.com/allhands_ai))

* Graham’s mentioned Agents blogpost - 8 things that agents can do right [now](https://www.all-hands.dev/blog/8-use-cases-for-generalist-software-development-agents)

* Projects - Open Hands (previously Open Devin) - [Github](https://github.com/All-Hands-AI/OpenHands)

* Germany meetup in Cologne ([here](https://twitter.com/WolframRvnwlf/status/1877338980632383713))

* Toronto Tinkerer Meetup *Sold OUT* ([Here](https://toronto.aitinkerers.org/p/ai-tinkerers-toronto-january-2025-meetup-at-google))

* YaRN conversation we had with the Authors ([coverage](https://sub.thursdai.news/p/thursdai-sunday-special-extending?utm_source=publication-search))

See you folks next week! Have a great long weekend if you’re in the US 🫡 

Please help to promote the podcast and newsletter by sharing with a friend!

 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jan-16-2025-hailuo-4m-context/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jan-16-2025-hailuo-4m-context?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1NDk4NjQ5MywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.dhVHbEk4Kb2DLfejXT5cpNzGqSQ8lgTvCGBQSVFaFR0&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Jan 9th - NVIDIA's Tiny Supercomputer, Phi-4 is back, Kokoro TTS & Moondream gaze, ByteDance SOTA lip sync & more AI news

**Date:** January 10, 2025  
**Duration:** 1:20:26  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-9th-nvidias-tiny-supercomputer](https://sub.thursdai.news/p/thursdai-jan-9th-nvidias-tiny-supercomputer)

Hey everyone, Alex here 👋

This week's ThursdAI was a whirlwind of announcements, from Microsoft finally dropping Phi-4's official weights on Hugging Face (a month late, but who's counting?) to Sam Altman casually mentioning that OpenAI's got AGI in the bag and is now setting its sights on *superintelligence*. Oh, and NVIDIA? They're casually releasing a $3,000 supercomputer that can run 200B parameter models on your desktop. No big deal.

We had some amazing guests this week too, with [Oliver](https://x.com/olliezliu/status/1876312788873977996) joining us to talk about a new foundation model in genomics and biosurveillance (yes, you read that right - think wastewater and pandemic monitoring!), and then, we've got some breaking news! [Vik](https://x.com/vikhyatk) returned to the show with a brand new Moondream release that can do some pretty wild things. Ever wanted an AI to tell you where someone's looking in a photo? Now you can, thanks to a tiny model that runs on edge devices. 🤯

So buckle up, folks, because we've got a ton to cover. Let's dive into the juicy details of this week's AI madness, starting with open source.

03:10 TL;DR

03:10 Deep Dive into Open Source LLMs

10:58 MetaGene: A New Frontier in AI

20:21 PHI4: The Latest in Open Source AI

27:46 R Star Math: Revolutionizing Small LLMs

34:02 Big Companies and AI Innovations

42:25 NVIDIA's Groundbreaking Announcements

43:49 AI Hardware: Building and Comparing Systems

46:06 NVIDIA's New AI Models: LLAMA Neumatron

47:57 Breaking News: Moondream's Latest Release

50:19 Moondream's Journey and Capabilities

58:41 Weights & Biases: New Evals Course

01:08:29 NVIDIA's World Foundation Models

01:08:29 ByteDance's LatentSync: State-of-the-Art Lip Sync

01:12:54 Kokoro TTS: High-Quality Text-to-Speech

As always, TL;DR section with links and show notes below 👇

Open Source AI & LLMs

Phi-4: Microsoft's "Small" Model Finally Gets its Official Hugging Face Debut

Finally, after a month, we're getting Phi-4 14B on HugginFace. So far, we've had bootlegged copies of it, but it's finally officially uploaded by Microsoft. Not only is it now official, it's also officialy MIT licensed which is great!

So, what's the big deal? Well, besides the licensing, it's a 14B parameter, dense decoder-only Transformer with a 16K token context length and trained on a whopping 9.8 *trillion* tokens. It scored 80.4 on math and 80.6 on MMLU, making it about 10% better than its predecessor, Phi-3 and better than Qwen 2.5's 79

What’s interesting about phi-4 is that the training data consisted of 40% synthetic data (almost half!)

The vibes are always interesting with Phi models, so we'll keep an eye out, notable also, the base models weren't released due to "safety issues" and that this model was not trained for multi turn chat applications but single turn use-cases

MetaGene-1: AI for Pandemic Monitoring and Pathogen Detection

Now, this one's a bit different. We usually talk about LLMs in this section, but this is more about the "open source" than the "LLM." Prime Intellect, along with folks from USC, released MetaGene-1, a *metagenomic foundation model*. That's a mouthful, right? Thankfully, we had Oliver Liu, a PhD student at USC, and an author on this paper, join us to explain.

Oliver clarified that the goal is to use AI for "biosurveillance, pandemic monitoring, and pathogen detection." They trained a 7B parameter model on 1.5 *trillion* base pairs of DNA and RNA sequences from wastewater, creating a model surprisingly capable of zero-shot embedding. Oliver pointed out that while using genomics to pretrain foundation models is not new, MetaGene-1 is, "in its current state, the largest model out there" and is "one of the few decoder only models that are being used". They also have collected 15T bae pairs but trained on 10% of them due to grant and compute constraints.

I really liked this one, and though the science behind this was complex, I couldn't help but get excited about the potential of transformer models catching or helping catch the next COVID 👏

rStar-Math: Making Small LLMs Math Whizzes with Monte Carlo Tree Search

Alright, this one blew my mind. A paper from Microsoft (yeah, them again) called "rStar-Math" basically found a way to make *small* LLMs do math better than o1 using Monte Carlo Tree Search (MCTS). I know, I know, it sounds wild. They took models like Phi-3-mini (a tiny 3.8B parameter model) and Qwen 2.5 3B and 7B, slapped some MCTS magic on top, and suddenly these models are acing the AIME 2024 competition math benchmark and scoring 90% on general math problems. For comparison, OpenAI's o1-preview scores 85.5% on math and o1-mini scores 90%. This is WILD, as just 5 months ago, it was unimaginable that any LLM can solve math of this complexity, then reasoning models could, and now small LLMs with some MCTS can!

Even crazier, they observed an "emergence of intrinsic self-reflection capability" in these models during problem-solving, something they weren't designed to do. LDJ chimed in saying "we're going to see more papers showing these things emerging and caught naturally." So, is 2025 the year of not just AI agents, but also emergent reasoning in LLMs? It's looking that way. The code isn't out yet (the GitHub link in the paper is currently a [404](https://github.com/microsoft/rStar)), but when it drops, you can bet we'll be all over it.

Big Companies and LLMs

OpenAI: From AGI to ASI

Okay, let's talk about the elephant in the room: Sam Altman's blog post. While reflecting on getting fired from his job on like a casual Friday, he dropped this bombshell: "We are now confident that we know how to build AGI as we have traditionally understood it." And then, as if that wasn't enough, he added, "We're beginning to turn our aim beyond that **to superintelligence in the true sense of the word**." So basically, OpenAI is saying, "AGI? Done. Next up: ASI."

This feels like a big shift in how openly folks at OpenAI is talking about Superintelligence, and while AGI is yet to be properly defined (LDJ read out the original OpenAI definition on the live show, but the Microsoft definition contractually with OpenAI was a system that generates $100B in revenue) they are already talking about Super Intelligence which supersedes all humans ever lived in all domains

NVIDIA @ CES - Home SuperComputers, 3 scaling laws, new Models

There was a lot of things happening at CES, the largest consumer electronics show, but the AI focus was on NVIDIA, namely on Jensen Huangs keynote speech!

He talked about a lot of stuff, really, it's a show, and is a very interesting watch, NVIDIA is obviously at the forefront of all of this AI wave, and when Jensen tells you that we're at the high of the 3rd scaling law, he knows what he's talking about (because he's fueling all of it with his GPUs) - the third one is of course test time scaling or "reasoning", the thing that powers o1, and the coming soon o3 model and other reasoners.

Project Digits - supercomputer at home?

Jensen also announced Project Digits: a compact AI supercomputer priced at a relatively modest $3,000. Under the hood, it wields a Grace Blackwell “GB10” superchip that supposedly offers 1 petaflop of AI compute and can support LLMs up to 200B parameters (or you can link 2 of them to run LLama 405b at home!)

This thing seems crazy, but we don't know more details like the power requirements for this beast!

Nemotrons again?

Also announced was a family of NVIDIA LLama Nemotron foundation models, but.. weirdly we already have Nemotron LLamas ([3 months ago](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Instruct-HF)) , so those are... new ones? I didn't really understand what was announced here, as we didn't get new models, but the announcement was made nonetheless. We're due to get 3 new version of Nemotron on the Nvidia NEMO platform (and Open), sometime soon.

NVIDIA did release new open source models, with COSMOS, which is a whole platform that includes pretrained world foundation models to help simulate world environments to train robots (among other things).

They have released txt2world and video2world Pre-trained Diffusion and Autoregressive models in 7B and 14B sizes, that generate videos to simulate visual worlds that have strong alignment to physics.

If you believe Elon when he says that Humanoid Robots are going to be the biggest category of products (every human will want 1 or 3, so we're looking at 20 billion of them), then COSMOS is a platform to generate synthetic data to train these robots to do things in the real world!

This weeks buzz - Weights & Biases corner

The wait is over, our LLM Evals course is now LIVE, featuring speakers Graham Neubig (who we had on the pod before, back when Open Hands was still called Open Devin) and Paige Bailey, and Anish and Ayush from my team at W&B!

If you're building with LLM in production and don't have a robust evaluation setup, or don't even know where to start with one, this course is definitely for you! [Sign up today](https://wandb.ai/site/courses/evals/?utm_source=thursdai&utm_medium=referral&utm_campaign=Jan9). You'll learn from examples of Imagen and Veo from Paige, Agentic examples using [Weave](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=Jan9) from Graham and Basic and Advanced Evaluation from Anish and Ayush.

The workshop in Seattle next was filled out super quick, so since we didn't want to waitlist tons of folks, we have extended it to another night, so those of you who couldn't get in, will have another opportunity on Tuesday! ([Workshop page](https://seattle.aitinkerers.org/p/ai-in-production-evals-observability-workshop)) but while working on it I came up with this distillation of what I'm going to deliver, and wanted to share with you.

Vision & Video

New Moondream 01-09 can tell where you look (among other things) ([blog](https://moondream.ai/blog/introducing-a-new-moondream-1-9b-and-gpu-support), [HF](https://huggingface.co/vikhyatk/moondream2))

We had some breaking news on the show! Vik Korrapati, the creator of Moondream, joined us to announce updates to Moondream, a new version of his tiny vision language model. This new release has some incredible capabilities, including pointing, object detection, structured output (like JSON), and even *gaze detection*. Yes, you read that right. Moondream can now tell you where someone (or even a pet!) is looking in an image.

Vic explained how they achieved this: "We took one of the training datasets that Gazelle trained on and added it to the Moondream fine tuning mix". What's even more impressive is that Moondream is tiny - the new version comes in 2B and 0.5B parameter sizes. As Vic said, "0.5b is we actually started with the 2b param model and we pruned down while picking specific capabilities you want to preserve". This makes it perfect for edge devices and applications where cost or privacy is a concern. It's incredible to see how far Moondream has come, from a personal project to a company with seven employees working on it.

Since Vik joined ThursdAI last January (we seem to be on a kick of revisiting with our guests from last year!) Moondream is a company, but they are committed to open source and so this releases is also Apache 2 👏 but you can also try this out on their website [playground](https://moondream.ai/playground) and hire them if you need to finetune a custom tiny vision model!

Voice & Audio

Very exciting updates in the OSS voice and audio this week!

KOKORO TTS - Apache 2 tiny (82M! params) TTS that's #1 on TTS arena ([HF](https://huggingface.co/hexgrad/Kokoro-82M),[Demo](https://huggingface.co/spaces/hexgrad/Kokoro-TTS))

Honestly when Wolfram told me about Kokoro being #1 on TTS arena and that it was released a few weeks back, I almost skipped giving this an update, but wow, this tiny tiny model can run on edge devices, can run in your browser, and the sound it generates is SO clean!

It's Apache 2 license and the voices were trained on non licensed data (per the author)

There's no voice cloning support yet, but there are voice packs you can use, and somehow, they got the SKY voice. Remember the one that Scarlett Johanson almost sued OpenAI for? That one! And for 82M parameters it sounds so good, hell, for any TTS, it sounds very good!

ByteDance - LatentSync state of the art lip syncing ([X](https://x.com/bdsqlsz/status/1875474807124586524), [Paper](https://arxiv.org/abs/2412.09262), [Fal](https://fal.ai/models/fal-ai/latentsync))

In the same week, ByteDance released a SOTA lip syncing OSS model called LatentSync, which takes a voice (for example, such as the one you can create with Kokoro above) and a video, and sync the lips of the person in the video, to make it seem like that person said the thing.

This is for example great for translation purposes, here's a quick example of my cloned voice (via 11labs) and translated opening of the show in spanish, and overlays it on top of my actual video, and it's pretty good!

This week Lex Fridman interviewed Volodymir Zelensky and I loved the technical and AI aspect of that whole multilingual interview, they have translated that into English, Russian and Ukrainian. But the lips weren't synced so it looked a bit off still. Now consider the different with and without lip syncing (here's a quick example I whipped up)

Baidu - Hallo 3 - generative avatars now with animated backgrounds

Meanwhile over at Baidu, Hallo 3 is their 3rd iteration of generative portraits, a way to turn a single image into a completely animated avatar, by also providing it a recording of your voice (or a TTS, does it really matter at this point?)

The highlight here is, the background is now part of these avatars! Where as previously these avatars used to be static, now they have dynamic backgrounds. Tho I still feel weirded out by their lip movements, but maybe with the above lipsyncing this can be fixed?

Not a bad second week of the yeah eh? A LOT of open source across multimodalities, supercomputers at home, tiny vision and TTS models and tons of apache 2 or MIT licensed models all over!

See you guys next week (well, some of you in person in SF and Seattle) but most of you next week on ThursdAI! 🫡

Tl;DR + Show Notes

* **Open Source LLMs**

* Phi-4 MIT licensed family of models from Microsoft ([X](https://x.com/sytelus/status/1877015492126220594), [Blog](https://techcommunity.microsoft.com/blog/aiplatformblog/introducing-phi-4-microsoft%E2%80%99s-newest-small-language-model-specializing-in-comple/4357090), [HF](https://huggingface.co/microsoft/phi-4))

* Prime Intellect - MetaGENE-1 - *metagenomic foundation model* ([Site](https://metagene.ai/), [X](https://x.com/olliezliu/status/1876312788873977996), [Paper](https://arxiv.org/abs/2501.02045))

* rStar-Math - making Small LLMs do Math better than o1 with MCTS ([Paper](https://arxiv.org/abs/2501.04519), [Github](https://github.com/microsoft/rStar))

* **Big CO LLMs + APIs**

* Sam Altman releases an ASI blog, multiple OpenAI people switch from AGI to ASI ([X](https://x.com/slow_developer/status/1876962062473023488))

* NVIDIA updates from CES ([X](https://x.com/alxfazio/status/1876507737909293339))

* XAI - Grok IOS app + Grok 3 finished pre-training

* Qwen has a new web portal with all their modals - [chat.qwenlm.ai](https://chat.qwenlm.ai/auth#email=git@alexw.me&name=altryne&oauth_sub=github@463317)

* **This weeks Buzz**

* Evals Course is LIVE - Evals with Paige Bailey and Graham Neubig Course Signup ([Signup](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=Jan9))

* San Francisco is still open ([Details](https://lu.ma/bzqvsqaa))

* Seattle is almost waitlisted ([Workshop](https://seattle.aitinkerers.org/p/ai-in-production-evals-observability-workshop))

* **Vision & Video**

* NVIDIA Cosmos - World Foundation Models ([Post](https://research.nvidia.com/publication/2025-01_cosmos-world-foundation-model-platform-physical-ai), [Github](https://github.com/NVIDIA/Cosmos?tab=readme-ov-file), [HF](https://huggingface.co/collections/nvidia/cosmos-6751e884dc10e013a0a0d8e6))

* Moondream 2 announcement - new evals - Chat with Vik Korrapati ([X](https://x.com/vikhyatk/status/1877407680228143370), [HF](https://huggingface.co/vikhyatk/moondream2), [Try It](https://moondream.ai/playground))

* **Voice & Audio**

* Kokoro - #1 TTS with Apache 2 license ([HF](https://huggingface.co/hexgrad/Kokoro-82M), [Demo](https://huggingface.co/spaces/hexgrad/Kokoro-TTS))

* Baidu - Hallo 3 - generative portraits ([Project](https://fudan-generative-vision.github.io/hallo3/#/), [Github](https://github.com/fudan-generative-vision/hallo3), [HF](https://huggingface.co/fudan-generative-ai/hallo3))

* ByteDance - LatentSync lip syncing model ([X](https://x.com/bdsqlsz/status/1875474807124586524), [Paper](https://arxiv.org/abs/2412.09262), [Fal](https://fal.ai/models/fal-ai/latentsync))

* **AI Art & Diffusion & 3D**

* Stability - SPAR3D: Stable Point-Aware Reconstruction of 3D Objects from Single Images ( [HF](https://huggingface.co/spaces/stabilityai/stable-point-aware-3d)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jan-9th-nvidias-tiny-supercomputer/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jan-9th-nvidias-tiny-supercomputer?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1NDUxNDIyMywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.8_wZQhO2N-TjeyUdFskTY5xB3W3Mbgj-Tw4HzFjpL2E&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Jan 2 - is 25' the year of AI agents?

**Date:** January 02, 2025  
**Duration:** 1:31:29  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-2-is-25-the-year-of](https://sub.thursdai.news/p/thursdai-jan-2-is-25-the-year-of)

Hey folks, Alex here 👋 Happy new year!

On our first episode of this year, and the second quarter of this century, there wasn't a lot of AI news to report on (most AI labs were on a well deserved break). So this week, I'm very happy to present a special ThursdAI episode, an interview with [Joāo Moura](https://x.com/joaomdmoura), CEO of [Crew.ai](http://Crew.ai) all about AI agents!

We first chatted with Joāo a [year ago](https://sub.thursdai.news/p/jan14-sunday-special-deep-dives), back in January of 2024, as CrewAI was blowing up but still just an open source project, it got to be the number 1 trending project on Github, and #1 project on Product Hunt. (You can either listen to the podcast or watch it in the embedded Youtube above)

00:36 Introduction and New Year Greetings

02:23 Updates on Open Source and LLMs

03:25 Deep Dive: AI Agents and Reasoning

03:55 Quick TLDR and Recent Developments

04:04 Medical LLMs and Modern BERT

09:55 Enterprise AI and Crew AI Introduction

10:17 Interview with João Moura: Crew AI

25:43 Human-in-the-Loop and Agent Evaluation

33:17 Evaluating AI Agents and LLMs

44:48 Open Source Models and Fin to OpenAI

45:21 Performance of Claude's Sonnet 3.5

48:01 Different parts of an agent topology, brain, memory, tools, caching

53:48 Tool Use and Integrations

01:04:20 Removing LangChain from Crew

01:07:51 The Year of Agents and Reasoning

01:18:43 Addressing Concerns About AI

01:24:31 Future of AI and Agents

01:28:46 Conclusion and Farewell

---

Is 2025 "the year of AI agents"?

AI agents as I remember them as a concept started for me a few month after I started ThursdAI ,when AutoGPT exploded. Was such a novel idea at the time, run LLM requests in a loop,

(In fact, back then, I came up with a retry with AI concept and called it [TrAI/Catch](https://x.com/altryne/status/1632253117827010566), where upon an error, I would feed that error back into the GPT api and ask it to correct itself. it feels so long ago!)

AutoGPT became the fastest ever Github project to reach 100K stars, and while exciting, it did not work.

Since then we saw multiple attempts at agentic frameworks, like babyAGI, autoGen. Crew AI was one of them that keeps being the favorite among many folks.

So, what is an AI agent? Simon Willison, friend of the pod, has a mission, to ask everyone who announces a new agent, what they mean when [they say it](https://x.com/simonw/status/1863567881553977819) because it seems that everyone "shares" a common understanding of AI agents, but it's different for everyone.

We'll start with Joāo's explanation and go from there. But let's assume the basic, it's a set of LLM calls, running in a self correcting loop, with access to planning, external tools (via function calling) and a memory or sorts that make decisions.

Though, as we go into detail, you'll see that since the very basic "run LLM in the loop" days, the agents in 2025 have evolved and have a lot of complexity.

My takeaways from the conversation

I encourage you to listen / watch the whole interview, Joāo is deeply knowledgable about the field and we go into a lot of topics, but here are my main takeaways from our chat

* Enterprises are adopting agents, starting with internal use-cases

* Crews have 4 different kinds of memory, Long Term (across runs), short term (each run), Entity term (company names, entities), pre-existing knowledge (DNA?)

* TIL about a "do all links respond with 200" guardrail

* Some of the agent tools we mentioned

* Stripe Agent API - for agent payments and access to payment data ([blog](https://stripe.dev/blog/adding-payments-to-your-agentic-workflows))

* Okta Auth for Gen AI - agent authentication and role management ([blog](https://www.auth0.ai/))

* E2B - code execution platform for agents ([e2b.dev](https://e2b.dev/))

* BrowserBase - programmatic web-browser for your AI agent

* Exa - search grounding for agents for real time understanding

* Crew has 13 crews that run 24/7 to automate their company

* Crews like Onboarding User Enrichment Crew, Meetings Prep, Taking Phone Calls, Generate Use Cases for Leads

* GPT-4o mini is the most used model for 2024 for CrewAI with main factors being speed / cost

* Speed of AI development makes it hard to standardize and solidify common integrations.

* Reasoning models like o1 still haven't seen a lot of success, partly due to speed, partly due to different way of prompting required.

This weeks Buzz

We've just opened up pre-registration for our upcoming FREE evaluations course, featuring Paige Bailey from Google and Graham Neubig from All Hands AI (previously Open Devin). We've distilled a lot of what we learned about evaluating LLM applications while building [Weave](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=jan2), our LLM Observability and Evaluation tooling, and are excited to share this with you all! [Get on the list](https://wandb.ai/site/courses/evals/?utm_source=thursdai&utm_medium=referral&utm_campaign=jan2)

Also, 2 workshops (also about Evals) from us are upcoming, one in SF on [Jan 11th](https://lu.ma/bzqvsqaa) and one in Seattle on [Jan 13th](https://seattle.aitinkerers.org/p/ai-in-production-evals-observability-workshop) (which I'm going to lead!) so if you're in those cities at those times, would love to see you!

And that's it for this week, there wasn't a LOT of news as I said. The interesting thing is, even in the very short week, the news that we did get were all about agents and reasoning, so it looks like 2025 is agents and reasoning, agents and reasoning!

See you all next week 🫡

TL;DR with links:

* **Open Source LLMs**

* HuatuoGPT-o1 - medical LLM designed for medical reasoning ([HF](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-8B), [Paper](https://huggingface.co/papers/2412.18925), [Github](https://github.com/FreedomIntelligence/HuatuoGPT-o1), [Data](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-verifiable-problem))

* Nomic - modernbert-embed-base - first embed model on top of modernbert ([HF](https://huggingface.co/nomic-ai/modernbert-embed-base))

* HuggingFace - SmolAgents lib to build agents ([Blog](https://huggingface.co/blog/smolagents))

* SmallThinker-3B-Preview - a QWEN 2.5 3B "reasoning" finetune ([HF](https://huggingface.co/PowerInfer/SmallThinker-3B-Preview))

* Wolfram new Benchmarks including DeepSeek v3 ([X](https://x.com/WolframRvnwlf/status/1874889165919384057))

* **Big CO LLMs + APIs**

* Newcomer Rubik's AI Sonus-1 family - Mini, Air, Pro and Reasoning ([X](https://x.com/RubiksAI/status/1874682159379972325), Chat)

* Microsoft "estimated" GPT-4o-mini is a ~8B ([X](https://x.com/Yuchenj_UW/status/1874507299303379428))

* Meta plans to bring AI profiles to their social networks ([X](https://x.com/petapixel/status/1874792802061844829))

* **This Week's Buzz**

* W&B Free Evals Course with Page Bailey and Graham Beubig - [Free Sign Up](https://wandb.ai/site/courses/evals/?utm_source=thursdai&utm_medium=referral&utm_campaign=jan2)

* SF evals event - [January 11th](https://lu.ma/bzqvsqaa)

* Seattle evals workshop - [January 13th](https://seattle.aitinkerers.org/p/ai-in-production-evals-observability-workshop) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jan-2-is-25-the-year-of/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jan-2-is-25-the-year-of?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1NDAzMzY2MCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.-2FmmS8-Iq9rSNBzuyH2cjNrSPPkwegxbFjSP45EJLw&utm_campaign=CTA_5).

---

