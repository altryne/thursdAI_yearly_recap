# 📆 ThursdAI Turns Two! 🎉 Gemma 3, Gemini Native Image, new OpenAI tools, tons of open source & more AI news

**Date:** March 13, 2025  
**Duration:** 1:32:04  
**Link:** [https://sub.thursdai.news/p/thursdai-turns-two-gemma-3-gemini](https://sub.thursdai.news/p/thursdai-turns-two-gemma-3-gemini)

---

## Description

**LET'S GO!** 

Happy second birthday to ThursdAI, your favorite weekly AI news show! Can you believe it's been two whole years since we jumped into that random Twitter Space to rant about GPT-4? From humble beginnings as a late-night Twitter chat to a full-blown podcast, Newsletter and YouTube show with hundreds of thousands of downloads, it's been an absolutely wild ride! 

That's right, two whole years of me, Alex Volkov, your friendly AI Evangelist, along with my amazing co-hosts, trying to keep you up-to-date on the breakneck speed of the AI world

And what better way to celebrate than with a week PACKED with insane AI news? Buckle up, folks, because this week Google went OPEN SOURCE crazy, Gemini got even cooler, OpenAI created a whole new Agents SDK and the open-source community continues to blow our minds. We’ve got it all - from game-changing model releases to mind-bending demos.

This week I'm also on the Weights & Biases company retreat, so TL;DR first and then the newsletter, but honestly, I'll start embedding the live show here in the substack from now on, because we're getting so good at it, I barely have to edit lately and there's a LOT to show you guys! 

TL;DR and Show Notes & Links

* **Hosts & Guests**

* **Alex Volkov** - AI Eveangelist & Weights & Biases ([@altryne](https://x.com/altryne))

* **Co Hosts - **[@WolframRvnwlf](https://x.com/WolframRvnwlf) [@ldjconfirmed](https://x.com/ldjconfirmed) [@nisten](https://x.com/nisten) 

* Sandra Kublik - DevRel at Cohere ([@itsSandraKublik](https://x.com/itsSandraKublik))

* **Open Source LLMs** 

* Google open sources Gemma 3 - 1B - 27B - 128K context ([Blog](https://developers.googleblog.com/en/introducing-gemma3/), [AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemma-3-27b-it), [HF](https://huggingface.co/collections/google/gemma-3-release-67c6c6f89c4f76621268bb6d))

* EuroBERT - multilingual encoder models (210M to 2.1B params)

* Reka Flash 3 (reasoning) 21B parameters is open sourced ([Blog](https://www.reka.ai/news/introducing-reka-flash), [HF](https://huggingface.co/RekaAI/reka-flash-3))

* Cohere Command A 111B model - 256K context ([Blog](https://cohere.com/blog/command-a))

* Nous Research Deep Hermes 24B / 3B Hybrid Reasoners ([X](https://x.com/NousResearch/status/1900218445763088766), [HF](https://huggingface.co/NousResearch/DeepHermes-3-Mistral-24B-Preview))

* AllenAI OLMo 2 32B - fully open source GPT4 level model ([X](https://x.com/natolambert/status/1900249185225703703), [Blog](https://t.co/MWEyDIJMGo), [Try It](https://t.co/QBVnWRcP0y))

* **Big CO LLMs + APIs**

* Gemini Flash generates images natively ([X](https://x.com/GoogleDeepMind/status/1899896275652202927), [AI Studio](https://aistudio.google.com/app/prompts/1bRqkN58xP6x3H1wTfQ84HaMi6R19vhLz))

* Google deep research is now free in Gemini app and powered by Gemini Thinking ([Try It no cost](https://gemini.google.com/app))

* OpenAI released new responses API, Web Search, File search and Computer USE tools ([X](https://x.com/OpenAIDevs/status/1899531225468969240), [Blog](https://t.co/s5Zsy4Wvqy))

* **This weeks Buzz** 

* The whole company is at an offsite at oceanside, CA

* W&B internal MCP hackathon and had cool projects - launching an MCP server soon!

* **Vision & Video**

* Remade AI - 8 LORA video effects for WANX ([HF](https://huggingface.co/collections/Remade-AI/wan21-14b-480p-i2v-loras-67d0e26f08092436b585919b))

* **AI Art & Diffusion & 3D**

* ByteDance Seedream 2.0 - A Native Chinese-English Bilingual Image Generation Foundation Model by ByteDance ([Blog](https://team.doubao.com/en/tech/seedream), [Paper](https://arxiv.org/pdf/2503.07703))

* **Tools**

* Everyone's talking about Manus - (manus.im)

* Google AI studio now supports youtube understanding via link dropping

Open Source LLMs: Gemma 3, EuroBERT, Reka Flash 3, and Cohere Command-A Unleashed!

This week was absolutely HUGE for open source, folks. Google dropped a BOMBSHELL with **Gemma 3**! As Wolfram pointed out, this is a "very technical achievement," and it's not just one model, but a whole family ranging from 1 billion to 27 billion parameters. And get this – the 27B model can run on a SINGLE GPU! Sundar Pichai himself claimed you’d need "at least 10X compute to get similar performance from other models." Insane!

Gemma 3 isn't just about size; it's packed with features. We're talking multimodal capabilities (text, images, and video!), support for over 140 languages, and a massive 128k context window. As Nisten pointed out, "it might actually end up being the best at multimodal in that regard" for local models. Plus, it's fine-tuned for safety and comes with ShieldGemma 2 for content moderation. You can grab Gemma 3 on [Google AI Studio](https://aistudio.google.com), [Hugging Face](https://huggingface.co/google/gemma-3-27b-it), Ollama, Kaggle – everywhere! Huge shoutout to Omar Sanseviero and the Google team for this incredible release and for supporting the open-source community from day one! Colin aka Bartowski, was right, "The best thing about Gemma is the fact that Google specifically helped the open source communities to get day one support." This is how you do open source right!

Next up, we have EuroBERT, a new family of multilingual encoder models. Wolfram, our European representative, was particularly excited about this one: "In European languages, you have different characters than in other languages. And, um, yeah, encoding everything properly is, uh, difficult." Ranging from 210 million to 2.1 billion parameters, EuroBERT is designed to push the boundaries of NLP in European and global languages. With training on a massive 5 trillion-token dataset across 15 languages and support for 8K context tokens, EuroBERT is a workhorse for RAG and other NLP tasks. Plus, how cool is their mascot?

Reka Flash 3 - a 21B reasoner with apache 2 trained with RLOO

And the open source train keeps rolling! Reka AI dropped Reka Flash 3, a 21 billion parameter reasoning model with an Apache 2.0 license! Nisten was blown away by the benchmarks: "This might be one of the best like 20B size models that there is right now. And it's Apache 2.0. Uh, I, I think this is a much bigger deal than most people realize." Reka Flash 3 is compact, efficient, and excels at chat, coding, instruction following, and function calling. They even used a new reinforcement learning technique called REINFORCE Leave One-Out (RLOO). Go give it a whirl on [Hugging Face](https://x.com/RekaAILabs/status/1899481289495031825) or their chat interface – chat.reka.ai!

Last but definitely not least in the open-source realm, we had a special guest, Sandra ([@itsSandraKublik](https://x.com/itsSandraKublik)) from Cohere, join us to announce Command-A! This beast of a model clocks in at 111 BILLION parameters with a massive 256K context window. Sandra emphasized its efficiency, "It requires only two GPUs. Typically the models of this size require 32 GPUs. So it's a huge, huge difference." Command-A is designed for enterprises, focusing on agentic tasks, tool use, and multilingual performance. It's optimized for private deployments and boasts enterprise-grade security. Congrats to Sandra and the Cohere team on this massive release!

Big CO LLMs + APIs: Gemini Flash Gets Visual, Deep Research Goes Free, and OpenAI Builds for Agents

The big companies weren't sleeping either! Google continued their awesome week by unleashing native image generation in Gemini Flash Experimental! This is seriously fucking cool, folks! Sorry for my French, but it’s true. You can now directly interact with images, tell Gemini what to do, and it just does it. We even showed it live on the stream, turning ourselves into cat-confetti-birthday-hat-wearing masterpieces! 

Wolfram was right, "It's also a sign what we will see in, like, Photoshop, for example. Where you, you expect to just talk to it and have it do everything that a graphic designer would be doing." The future of creative tools is HERE.

And guess what else Google did? They made Deep Research FREE in the Gemini app and powered by Gemini Thinking! Nisten jumped in to test it live, and we were all impressed. "This is the nicest interface so far that I've seen," he said. Deep Research now digs through HUNDREDS of websites (Nisten’s test hit 156!) to give you comprehensive answers, and the interface is slick and user-friendly. Plus, you can export to Google Docs! Intelligence too cheap to meter? Google is definitely pushing that boundary.

Last second additions - Allen Institute for AI released **OLMo 2 32B** - their biggest open model yet

Just as I'm writing this, friend of the pod, Nathan from Allen Institute for AI announced the release of a FULLY OPEN OLMo 2, which includes weights, code, dataset, everything and apparently it beats the latest GPT 3.5, GPT 4o mini, and leading open weight models like Qwen and Mistral. 

Evals look legit, but nore than that, this is an Apache 2 model with everything in place to advance open AI and open science! 

Check out Nathans [tweet](https://x.com/natolambert/status/1900249099343192573) for more info, and congrats to Allen team for this awesome release! 

OpenAI new responses API and Agent ASK with Web, File and CUA tools

Of course, OpenAI wasn't going to let Google have all the fun. They dropped a new SDK for agents called the Responses API. This is a whole new way to build with OpenAI, designed specifically for the agentic era we're entering. They also released three new tools: Web Search, Computer Use Tool, and File Search Tool. The Web Search tool is self-explanatory – finally, built-in web search from OpenAI!

The Computer Use Tool, while currently limited in availability, opens up exciting possibilities for agent automation, letting agents interact with computer interfaces. And the File Search Tool gives you a built-in RAG system, simplifying knowledge retrieval from your own files. As always, OpenAI is adapting to the agentic world and giving developers more power.

Finally in the big company space, Nous Research released PORTAL, their new Inference API service. Now you can access their awesome models, like Hermes 3 Llama 70B and DeepHermes 3 8B, directly via API. It's great to see more open-source labs offering API access, making these powerful models even more accessible.

This Week's Buzz at Weights & Biases: Offsite Hackathon and MCP Mania!

This week's "This Week's Buzz" segment comes to you live from Oceanside, California! The whole Weights & Biases team is here for our company offsite. Despite the not-so-sunny California weather (thanks, storm!), it's been an incredible week of meeting colleagues, strategizing, and HACKING!

And speaking of hacking, we had an MCP hackathon! After last week’s MCP-pilling episode, we were all hyped about Model Context Protocol, and the team didn't disappoint. In just three hours, the innovation was flowing! We saw agents built for WordPress, MCP support integrated into Weave playground, and even MCP servers for Weights & Biases itself! Get ready, folks, because an MCP server for Weights & Biases is COMING SOON! You'll be able to talk to your W&B data like never before. Huge shoutout to the W&B team for their incredible talent and for embracing the agentic future! And in case you missed it, Weights & Biases is now part of the CoreWeave family! Exciting times ahead!

Vision & Video: LoRA Video Effects and OpenSora 2.0

Moving into vision and video, Remade AI [released](https://huggingface.co/collections/Remade-AI/wan21-14b-480p-i2v-loras-67d0e26f08092436b585919b) 8 LoRA video effects for 1X! Remember 1X from Alibaba? Now you can add crazy effects like "squish," "inflate," "deflate," and even "cakeify" to your videos using LoRAs. It's open source and super cool to see video effects becoming trainable and customizable.

And in the realm of open-source video generation, [OpenSora 2.0](https://github.com/hpcaitech/Open-Sora?tab=readme-ov-file) dropped! This 11 billion parameter model claims state-of-the-art video generation trained for just $200,000! They’re even claiming performance close to Sora itself on some benchmarks. Nisten checked out the demos, and while we're all a bit jaded now with the rapid pace of video AI, it's still mind-blowing how far we've come. Open source video is getting seriously impressive, seriously fast.

AI Art & Diffusion & 3D: ByteDance's Bilingual Seedream 2.0

ByteDance, the folks behind TikTok, released Seedream 2.0, a native Chinese-English bilingual image generation foundation model. This model, from ByteDream, excels at text rendering, cultural nuance, and human preference alignment. Seedream 2.0 boasts "powerful general capability," "native bilingual comprehension ability," and "excellent text rendering." It's designed to understand both Chinese and English prompts natively, generating high-quality, culturally relevant images. The examples look stunning, especially its ability to render Chinese text beautifully.

Tools: Manus AI Agent, Google AI Studio YouTube Links, and Cursor Embeddings

Finally, in the tools section, everyone's buzzing about Manus, a new AI research agent. We gave it a try live on the show, asking it to do some research. The UI is slick, and it seems to be using Claude 3.7 behind the scenes. Manus creates a to-do list, browses the web in a real Chrome browser, and even generates files. It's like Operator on steroids. We'll be keeping an eye on Manus and will report back on its performance in future episodes.

And Google AI Studio keeps getting better! Now you can drop YouTube links into Google AI Studio, and it will natively understand the video! This is HUGE for video analysis and content understanding. Imagine using this for support, content summarization, and so much more.

PHEW! What a week to celebrate two years of ThursdAI! From open source explosions to Gemini's visual prowess and OpenAI's agentic advancements, the AI world is moving faster than ever. As Wolfram aptly put it, "The acceleration, you can feel it." And Nisten reminded us of the incredible journey, "I remember I had early access to GPT-4 32K, and, uh, then... the person for the contract that had given me access, they cut it off because on the one weekend, I didn't realize how expensive it was. So I had to use $180 worth of tokens  just trying it out." Now, we have models that are more powerful and more accessible than ever before. 

Thank you to Wolfram, Nisten, and LDJ for co-hosting and bringing their insights every week. 

And most importantly, THANK YOU to our amazing community for tuning in, listening, and supporting ThursdAI for two incredible years! We couldn't do it without you. Here's to another year of staying up-to-date so YOU don't have to! Don't forget to subscribe to the podcast, YouTube channel, and newsletter to stay in the loop. And share ThursdAI with a friend – it's the best birthday gift you can give us! Until next week, keep building and keep exploring the amazing world of AI! LET'S GO! 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-turns-two-gemma-3-gemini/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-turns-two-gemma-3-gemini?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1OTAxNjkwMywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.ftZkAu1uiRykbn6XLxm-5RrLYK2YZgocws5tx4Yc8Ak&utm_campaign=CTA_5).
