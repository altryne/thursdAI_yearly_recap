# 📆 ThursdAI - June 19 - MiniMax M1 beats R1, OpenAI records your meetings, Gemini in GA, W&B uses Coreweave GPUs & more AI news

**Date:** June 20, 2025  
**Duration:** 1:41:31  
**Link:** [https://sub.thursdai.news/p/thursdai-june-18-minimax-m1-beats](https://sub.thursdai.news/p/thursdai-june-18-minimax-m1-beats)

---

## Description

Hey all, Alex here 👋

This week, while not the busiest week in releases (we can't get a SOTA LLM every week now can we), was full of interesting open source releases, and feature updates such as the chatGPT meetings recorder (which we live tested on the show, the limit is 2 hours!)

It was also a day after our annual W&B conference called FullyConnected, and so I had a few goodies to share with you, like answering the main question, when will W&B have some use of those GPUs from CoreWeave, the answer is... now! (We launched a brand new preview of an inference service with open source models)

And finally, we had a great chat with Pankaj Gupta, co-founder and CEO of Yupp, a new service that lets users chat with the top AIs for free, while turning their votes into leaderboards for everyone else to understand which Gen AI model is best for which task/topic. It was a great conversation, and he even shared an invite code with all of us (I'll attach to the TL;DR and show notes, let's dive in!)

00:00 Introduction and Welcome

01:04 Show Overview and Audience Interaction

01:49 Special Guest Announcement and Experiment

03:05 Wolfram's Background and Upcoming Hosting

04:42 TLDR: This Week's Highlights

15:38 Open Source AI Releases

32:34 Big Companies and APIs

32:45 Google's Gemini Updates

42:25 OpenAI's Latest Features

54:30 Exciting Updates from Weights & Biases

56:42 Introduction to Weights & Biases Inference Service

57:41 Exploring the New Inference Playground

58:44 User Questions and Model Recommendations

59:44 Deep Dive into Model Evaluations

01:05:55 Announcing Online Evaluations via Weave

01:09:05 Introducing Pankaj Gupta from [YUP.AI](http://YUP.AI)

01:10:23 [YUP.AI](http://YUP.AI): A New Platform for Model Evaluations

01:13:05 Discussion on Crowdsourced Evaluations

01:27:11 New Developments in Video Models

01:36:23 OpenAI's New Transcription Service

01:39:48 Show Wrap-Up and Future Plans

Here's the TL;DR and show notes links

ThursdAI - June 19th, 2025 - TL;DR

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@yampeleg](x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed))

* Guest - [@pankaj](http://x.com/@pankaj) - co-founder of [Yupp.ai](https://yupp.ai/join/thursdAI)

* **Open Source LLMs**

* Moonshot AI open-sourced Kimi-Dev-72B ([Github](https://github.com/MoonshotAI/Kimi-Dev?tab=readme-ov-file), [HF](https://huggingface.co/moonshotai/Kimi-Dev-72B))

* MiniMax-M1 456B (45B Active) - reasoning model ([Paper](https://arxiv.org/abs/2506.13585), [HF](https://huggingface.co/MiniMaxAI/MiniMax-M1-40k), [Try It](https://huggingface.co/spaces/MiniMaxAI/MiniMax-M1), [Github](https://github.com/MiniMax-AI/MiniMax-M1))

* **Big CO LLMs + APIs**

* Google drops Gemini 2.5 Pro/Flash GA, 2.5 Flash-Lite in Preview ( [Blog](https://blog.google/products/gemini/gemini-2-5-model-family-expands/), [Tech report](https://storage.googleapis.com/gemini-technical-report), [Tweet](https://x.com/google/status/192905415))

* Google launches Search Live: Talk, listen and explore in real time with AI Mode ([Blog](https://blog.google/products/search/search-live-ai-mode/))

* OpenAI adds MCP support to Deep Research in chatGPT ([X](https://x.com/altryne/status/1934644274227769431), [Docs](https://platform.openai.com/docs/mcp))

* OpenAI launches their meetings recorder in mac App ([docs](https://help.openai.com/en/articles/11487532-chatgpt-record))

* Zuck update: Considering bringing Nat Friedman and Daniel Gross to Meta ([information](https://x.com/amir/status/1935461177045516568))

* **This weeks Buzz**

* NEW! W&B Inference provides a unified interface to access and run top open-source AI models ([inference](https://wandb.ai/inference), [docs](https://weave-docs.wandb.ai/guides/integrations/inference/))

* NEW! W&B Weave Online Evaluations delivers real-time production insights and continuous evaluation for AI agents across any cloud. ([X](https://x.com/altryne/status/1935412384283107572))

* The new platform offers "metal-to-token" observability, linking hardware performance directly to application-level metrics.

* Vision & Video

* ByteDance new video model beats VEO3 - Seedance.1.0 mini ([Site](https://dreamina.capcut.com/ai-tool/video/generate), [FAL](https://fal.ai/models/fal-ai/bytedance/seedance/v1/lite/image-to-video))

* MiniMax Hailuo 02 - 1080p native, SOTA instruction following ([X](https://www.minimax.io/news/minimax-hailuo-02), [FAL](https://fal.ai/models/fal-ai/minimax/hailuo-02/pro/image-to-video))

* Midjourney video is also here - great visuals ([X](https://x.com/angrypenguinPNG/status/1932931137179176960))

* **Voice & Audio**

* Kyutai launches open-source, high-throughput streaming Speech-To-Text models for real-time applications ([X](https://x.com/kyutai_labs/thread/1935652243119788111), [website](https://join.yupp.ai/thursdai))

* Studies and Others

* LLMs Flunk Real-World Coding Contests, Exposing a Major Skill Gap ([Arxiv](https://arxiv.org/pdf/2506.11928))

* MIT Study: ChatGPT Use Causes Sharp Cognitive Decline ([Arxiv](https://arxiv.org/abs/2506.08872))

* Andrej Karpathy's "Software 3.0": The Dawn of English as a Programming Language ([youtube](https://www.youtube.com/watch?v=LCEmiRjPEtQ), [deck](https://drive.google.com/file/d/1HIEMdVlzCxke22ISVzornd2-UpWHngRZ/view?usp=sharing))

* **Tools**

* Yupp launches with 500+ AI models, a new leaderboard, and a user-powered feedback economy - use [thursdai link](https://yupp.ai/join/thursdAI)* to get 50% extra credits

* BrowserBase announces [director.ai](http://director.ai) - an agent to run things on the web

* Universal system prompt for reduction of hallucination (from [Reddit](https://www.reddit.com/r/PromptEngineering/comments/1kup28y/chatgpt_and_gemini_ai_will_gaslight_you_everyone/))

*Disclosure: while this isn't a paid promotion, I do think that yupp has a great value, I do get a bit more credits on their platform if you click my link and so do you. You can go to [yupp.ai](http://yupp.ai) and register with no affiliation if you wish. 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-june-18-minimax-m1-beats/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-june-18-minimax-m1-beats?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2NjM1OTY2MCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.XSlsS0LVkZoKjnK1vqluK6duzE3fa7L1zHsEvPRQUW8&utm_campaign=CTA_5).
