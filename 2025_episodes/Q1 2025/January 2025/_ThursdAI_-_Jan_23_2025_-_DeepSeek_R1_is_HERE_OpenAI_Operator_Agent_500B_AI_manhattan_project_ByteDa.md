# 📆 ThursdAI - Jan 23, 2025 - 🔥 DeepSeek R1 is HERE, OpenAI Operator Agent, $500B AI manhattan project, ByteDance UI-Tars, new Gemini Thinker & more AI news

**Date:** January 24, 2025  
**Duration:** 1:49:39  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1](https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1)

---

## Description

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
