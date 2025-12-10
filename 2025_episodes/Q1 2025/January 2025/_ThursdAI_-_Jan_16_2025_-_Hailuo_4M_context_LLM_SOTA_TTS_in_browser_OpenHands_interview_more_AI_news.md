# 📆 ThursdAI - Jan 16, 2025 - Hailuo 4M context LLM, SOTA TTS in browser, OpenHands interview & more AI news

**Date:** January 17, 2025  
**Duration:** 1:40:32  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-16-2025-hailuo-4m-context](https://sub.thursdai.news/p/thursdai-jan-16-2025-hailuo-4m-context)

---

## Description

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
