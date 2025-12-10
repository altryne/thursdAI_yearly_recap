# 📆 Oct 9, 2025 — Dev Day’s Agent Era, Samsung’s 7M TRM Shock, Ling‑1T at 1T, Grok Video goes NSFW, and Serverless RL arrives

**Date:** October 10, 2025  
**Duration:** 1:41:29  
**Link:** [https://sub.thursdai.news/p/oct-9-2025-dev-days-agent-era-samsungs](https://sub.thursdai.news/p/oct-9-2025-dev-days-agent-era-samsungs)

---

## Description

Hey everyone, Alex here 👋

We’re deep in the post-reality era now. Between Sora2, the latest waves of video models, and “is-that-person-real” cameos, it’s getting genuinely hard to trust what we see. Case in point: I recorded a short clip with (the real) Sam Altman this week and a bunch of friends thought I faked it with Sora-style tooling. Someone even added a fake Sora watermark just to mess with people. Welcome to 2025.

This week’s episode and this write-up focus on a few big arcs we’re all living through at once: OpenAI’s Dev Day and the beginning of the agent-app platform inside ChatGPT, a bizarre and exciting split-screen in model scaling where a 7M recursive model from Samsung is suddenly competitive on reasoning puzzles while inclusionAI is shipping a trillion-parameter mixture-of-reasoners,  and Grok’s image-to-video now does audio and pushes the line on… taste. We also dove into practical evals for coding agents with Eric Provencher from Repo Prompt, and I’ve got big news from my day job world: W&B + CoreWeave launched Serverless RL, so training and deploying RL agents at scale is now one API call away.

Let’s get into it.

OpenAI’s 3rd Dev Day - Live Coverage + exclusive interviews

This is the third Dev Day that I got to attend in person, covering this for ThursdAI ([2023](https://sub.thursdai.news/p/nov-09), [2024](https://sub.thursdai.news/p/oct-3-how-i-met-sam-altman)), and this one was the best by far! The production quality of their events rises every year, and this year they’ve opened up the conference to >1500 people, had 3 main launches and a lot of ways to interact with the OpenAI folks! 

I’ve also gotten an exclusive chance to sit in on a fireside chat with Sam Altman and Greg Brokman (snippets of which I’ve included in the podcast, starting 01:15:00 and I got to ask Sam a few questions after that as well. 

Event Ambiance and Vibes

OpenAI folks outdid themselves with this event, the live demos were quite incredible, the location (Fort Mason), Food and just the whole thing was on point. The event concluded with a 1x1 Sam and Jony Ive chat that I hope will be published on YT sometime, because it was very insightful. 

By far the best reason to go to this event in person is meeting folks and networking, both OpenAI employees, and AI Engineers who use their products. It’s 1 day a year, when OpenAI makes all their employees who attend, Developer Experience folks, as you can and are encouraged to, interact with them, ask questions, give feedback and it’s honestly great! 

I really enjoy meeting folks at this event and consider this to be a very high signal network, and was honored to have quite a few ThursdAI listeners among the participants and OpenAI folk! If you’re reading this, thank you for your patronage 🫡 

Launches and Ships

OpenAI also shipped, and shipped a LOT! Sam was up on Keynote with 3 main pillars, which we’ll break down 1 by 1. ChatGPT Apps, AgentKit (+ agent builder) and Codex/New APIs

Codex & New APIs

Codex has gotten General Availability, but we’ve been using it all this time so we don’t really care, what we do care about is the new slack integration and the new Codex SDK, which means you can now directly inject Codex agency into your app. This flew a bit over people’s heads, but Romain Huet, VP of DevEx at OpenAI demoed on stage how his mobile app now has a Codex tab, where he can ask Codex to make changes to the app at runtime! It was quite crazy! 

ChatGPT Apps + AppsSDK

This was maybe the most visual and most surprising release, since they’ve tried to be an appstore before (plugins, customGPTs). But this time, it seems like, based on top of MCP, ChatGPT is going to become a full blown Appstore for 800+ million weekly active ChatGPT users as well. 

Some of the examples they have showed included Spotify and Zillow, where just by typing in “Spotify” in chatGPT, you will have an interactive app with it’s own UI, right inside of ChatGPT. So you could ask it to create a playlist for you based on your history, or ask Zillow to find homes in an area under a certain $$ amount.

The most impressive thing, is that those are only launch partners, everyone can (technically) build a ChatGPT app with their AppsSDK that’s built on top of... the MCP (model context protocol) spec! 

The main question remains about discoverability, this is where Plugins and CustomGPTs (previous attempts to create apps within ChatGPT have failed), and when I asked him about it, Sam basically said “we’ll iterate and get it right” (starting 01:17:00). So it remains to be seen if folks really need their ChatGPT as yet another Appstore. 

AgentKit, AgentBuilder and ChatKit

2025 is the year of agents, and besides launching quite a few of their own, OpenAI will not let you, build and host smart agents that can use tools, on their platform. Supposedly, with AgentBuilder, building agents is just dragging a few nodes around, prompting and connecting them. They had a great demo on stage where with less than 8 minutes, they’ve build an agent to interact with the DevDay website.

It’s also great to see how greatly does OpenAI adapt the MCP spec, as this too, is powered by MCP, as in, any external connection you want to give your agent, must happen with an MCP server. 

Agents for the masses is maybe not quite there yet

In reality though, things are not so easy. Agents require more than just a nice drag & drop interface, they require knowledge, iteration, constant evaluation (which they’ve also added, kudos!) and eventually, customized agents need code. 

I [spent an hour](https://x.com/altryne/status/1976024045020934317) trying it out yesterday, building an agent to search the ThursdAI archives. The experience was a mixed bag. The AI-native features are incredibly cool. For instance, you can just describe the JSON schema you want as an output, and it generates it for you. The widget builder is also impressive, allowing you to create custom UI components for your agent’s responses.

However, I also ran into the harsh realities of agent building. My agent’s web browsing tool failed because Substack seems to be blocking OpenAI’s crawlers, forcing me to fall back on the old-school RAG approach of uploading our entire archive to a vector store. And while the built-in evaluation and tracing tools are a great idea, they were buggy and failed to help me debug the error. It’s a powerful tool, but it also highlights that building a reliable agent is an iterative, often frustrating process that a nice UI alone can’t solve. It’s not just about the infrastructure; it’s about wrestling with a stochastic machine until it behaves.

But to get started with something simple, they have definitely pushed the envelope on what is possible without coding. 

OpenAI also dropped a few key API updates:

* **GPT-5-Pro** is now available via API. It’s incredibly powerful but also incredibly expensive. As Eric mentioned, you’re not going to be running agentic loops with it, but it’s perfect for a high-stakes initial planning step where you need an “expert opinion.”

* **SORA 2** is also in the API, allowing developers to integrate their state-of-the-art video generation model into their own apps. The API can access the 15-second “Pro” model but doesn’t support the “Cameo” feature for now.

* **Realtime-mini** is a game-changer for voice AI. It’s a new, ultra-fast speech-to-speech model that’s **80% cheaper **than the original Realtime API. This massive price drop removes one of the biggest barriers to building truly conversational, low-latency voice agents.

**My Chat with Sam & Greg - On Power, Responsibility, and Energy**

After the announcements, I’ve got to sit in a fireside chat with Sam Altman and Greg Brockman and ask some questions. Here’s what stood out:

When I asked about the energy requirements for their massive compute plans (remember the $500B Stargate deal?), Sam said they’d have announcements about Helion (his fusion investment) soon but weren’t ready to talk about it. Then someone from Semi Analysis told me most power will come from... generator trucks. 15-megawatt generator trucks that just drive up to data centers. We’re literally going to power AGI with diesel trucks!

On responsibility, when I brought up the [glazing](https://sub.thursdai.news/p/thursdai-may-1-qwen-3-phi-4-openai) incident and asked how they deal with being in the lives of 800+ million people weekly, Sam’s response was sobering: “This is not the excitement of ‘oh we’re building something important.’ This is just the stress of the responsibility... The fact that 10% of the world is talking to kind of one brain is a strange thing and there’s a lot of responsibility.”

Greg added something profound: “AI is far more surprising than I anticipated... The deep nuance of how these problems contact reality is something that I think no one had anticipated.”

**This Week’s Buzz: RL X-mas came early with Serverless RL! **([X](https://x.com/wandb/status/1975917052920678528), [Blog](https://openpipe.ai/blog/serverless-rl))

Big news from our side of the world! About a month ago, the incredible OpenPipe team joined us at Weights & Biases and CoreWeave. They are absolute wizards when it comes to fine-tuning and Reinforcement Learning (RL), and they wasted no time combining their expertise with CoreWeave’s massive infrastructure.

This week, they launched **Serverless RL**, a managed reinforcement learning service that completely abstracts away the infrastructure nightmare that usually comes with RL. It automatically scales your training and inference compute, integrates with W&B Inference for instant deployment, and simplifies the creation of reward functions and verifiers. RL is what turns a good model into a great model for a specific task, often with surprisingly little data. This new service massively lowers the barrier to entry, and I’m so excited to see what people build with it. We’ll be doing a deeper dive on this soon but please check out the [Colab Notebook](wandb.me/RLS) to get a taste of what AutoRL is like! 

**Open Source**

While OpenAI was holding its big event, the open-source community was busy dropping bombshells of its own.

**Samsung’s TRM: Is This 7M Parameter Model... Magic? **([X](https://x.com/jm_alexia/status/1975560628657164426), [Blog](https://t.co/w5ZDsHDDPE), [arXiv](https://arxiv.org/pdf/2510.04871.pdf))

This was the release that had everyone’s jaws on the floor. A single researcher from the Samsung AI Lab in Montreal released a paper on a **Tiny Recursive Model (TRM)**. Get this: it’s a **7 MILLION parameter model** that is outperforming giants like DeepSeek-R1 and Gemini 2.5 Pro on complex reasoning benchmarks like ARC-AGI. I had to read that twice. 7 million, not billion.

How is this possible? Instead of relying on brute-force scale, TRM uses a recursive process. It generates a first draft of an answer, then repeatedly critiques and refines its own logic in a hidden “scratchpad” up to 16 times. As Yam pointed out, the paper is incredibly insightful, and it’s a groundbreaking piece of work from a single author, which is almost unheard of these days. Eric made a great point that because it’s so small, it opens the door for hobbyists and solo researchers to experiment with cutting-edge architectures on their home GPUs. This feels like a completely new direction for AI, and it’s incredibly exciting.

**inclusionAI’s Ling-1T: Enter the Trillion Parameter Club **([X](https://x.com/AntLingAGI/status/1975942293330018426), [HF](https://huggingface.co/inclusionAI/Ling-1T), [Try it](https://zenmux.ai/settings/chat?model=inclusionai/ling-1t))

On the complete opposite end of the scale (about 3 OOM away), we have **Ling-1T**from inclusionAI. This is a **1 TRILLION parameter** Mixture-of-Experts (MoE) model. The key here is efficiency; while it has a trillion total parameters, it only uses about 37 billion active parameters per token.

The benchmarks are wild, showing it beating models like GPT-5-Main (in non-thinking mode) and Gemini 2.5 on a range of reasoning tasks. They claim to match Gemini’s performance using about half the compute. Of course, with any new model posting huge scores, there’s always the question of whether it was trained on the public test sets, but the results are undeniably impressive. It’s another example of the push towards maintaining top-tier performance while drastically reducing the computational cost of inference.

**More Open Source Goodness: Microsoft, AI21, and IBM**

It didn’t stop there.

* **Microsoft** released **UserLM-8B**, a fascinating Llama 3 finetune trained not to be an assistant, but to simulate the *user* in a conversation. As Yam explained from his own experience, this is a super useful technique for generating high-quality, multi-turn synthetic data to train more robust chatbot agents. ([X](https://x.com/altryne/status/1976122132355580113)**, **[**HF**](https://huggingface.co/microsoft/UserLM-8b)**)**

* Our friends at **AI21 Labs** are back with **Jamba Reasoning 3B**, a tiny but mighty 3-billion-parameter model. It uses a hybrid SSM-Transformer architecture, which makes it incredibly fast for its size, making it a great option for local inference on a laptop.

* **IBM** also released their **Granite** family of models, which also use a hybrid design. Their big focus is on enterprise-grade governance and trust, and it’s the first open model family to get an ISO certification for AI management systems.**Big Company Moves: Grok Imagine Levels Up... And Leans In**

Finally, let’s talk about the latest update to **Grok Imagine**. They’ve rolled out video generation with synchronized sound, and it’s fast—often faster than Sora. The quality has significantly improved, and it’s a powerful tool.

However, I have to talk about the other side of this. Grok is positioning itself as the “uncensored” alternative, and they are leaning into that hard. Their video generator has a “spicy” mode that explicitly generates 18+ content. But the thing that truly disturbed me was a new feature with their animated character, “Annie.” It’s a gamified engagement mechanic where you “make your connection better” by talking to her every day to unlock special rewards, like new outfits.

To be blunt, this is disgusting. We talk a lot on this show about the immense responsibility that comes with building these powerful AIs. I know from my conversations with folks at OpenAI and other labs that they think deeply about safety, preventing misuse, and the psychological impact these systems can have. This feature from Grok is the polar opposite. It leans into the worst fears about AI creating addictive, para-social relationships. It’s exploitative, and frankly, the team behind it should reconsider their choices IMO. 

All righty, this is mostly the new for this week, it’s been a very busy week, and if you’d like to see our live coverage + DevDay keynote + interviews I’ve had with [Simon Willison](https://substack.com/profile/5753967-simon-willison) , Greg Kamradt, Jeffrey Huber, Allesio from [Latent.Space](https://substack.com/profile/89230629-latentspace), Matthew Berman and more impactful folks, our livestream can be found here: 

I’m incredibly humbled and privileged to keep being invited to the Dev Day, and looking forward to cover more events, with exclusive interviews, on the ground reporting and insights. Please subscribe if you like this content to continue. 

TL;DR and Show Notes

* **Show Notes & Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* **Co-Hosts** - [@WolframRvnwlf](http://x.com/@WolframRvnwlf), [@yampeleg](http://x.com/yampeleg), [@nisten](http://x.com/@nisten), [@ldjconfirmed](http://x.com/@ldjconfirmed)

* **Guest**: Kyle Corbitt - OpenPipe / CoreWeave ([@corbtt](https://x.com/corbtt))

* **Guest**: Eric Provencher - Repo Prompt ([@pvncher](https://x.com/pvncher))

* **OpenAI Dev Day**

* OpenAI AgentKit All-in-One Agent Builder ([X](https://x.com/rohanpaul_ai/status/1975309479047798835), [OpenAI](https://openai.com/index/introducing-agentkit/))

* ChatGPT Apps & New APIs (GPT-5-pro, SORA, realtime-mini)

* **Open Source LLMs**

* Microsoft UserLM-8B Model Released ([X](https://x.com/altryne/status/1976122132355580113), [HF](https://huggingface.co/microsoft/UserLM-8b))

* Samsung Tiny Recursive Model (TRM) ([X](https://x.com/jm_alexia/status/1975560628657164426), [Blog](https://t.co/w5ZDsHDDPE), [arXiv](https://arxiv.org/pdf/2510.04871.pdf))

* AI21 Labs releases Jamba Reasoning 3B ([X](https://x.com/AI21Labs/status/1976271434004541641), [HF](https://huggingface.co/ai21labs/AI21-Jamba-Reasoning-3B))

* inclusionAI debuts Ling-1T: Trillion-Scale Efficient Reasoner ([X](https://x.com/AntLingAGI/status/1975942293330018426), [HF](https://huggingface.co/inclusionAI/Ling-1T), [Try it](https://zenmux.ai/settings/chat?model=inclusionai/ling-1t))

* IBM Granite Models

* **Evals**

* Repo Bench by Repo Prompt ([Web](https://repo.prompt.com/bench))

* **Big CO LLMs + APIs**

* Qwen 3 Omni & Realtime Models

* Google DeepMind unveils Gemini 2.5 Computer-Use model ([X](https://x.com/GoogleDeepMind/status/1975917052920678528), [Blog](https://blog.google/technology/google-deepmind/gemini-computer-use-model))

* Google Gemini Flash 2.5 (new)

* Grok Imagine updated with video and sound

* **This weeks Buzz**

* OpenPipe (part of Coreweave,W&B) launch Serverless RL ([X](https://x.com/wandb/status/1975917052920678528), [Blog](https://openpipe.ai/blog/serverless-rl), [Notebook](http://wandb.me/RLS))

* **Vision & Video**

* Ovi: Open Source Video & Synchronized Audio Generation ([X](https://x.com/linoy_tsaban/status/1975924336935743737), [HF](https://huggingface.co/blog/MonsterMMORPG/ovi-generate-videos-with-audio-like-veo-3-or-sora))

* **Voice & Audio**

* GPT-realtime-mini: OpenAI’s ultra-fast speech-to-speech model API ([OpenAI Blog](https://platform.openai.com/docs/models/gpt-realtime-mini), [TechCrunch](https://techcrunch.com/2025/10/06/openai-ramps-up-developer-push-with-more-powerful-models-in-its-api/))

* **AI Art & Diffusion & 3D**

* Bagel.com: Paris – Decentralized Diffusion Model ([X](https://x.com/bageldotcom/status/1975596255624769858), [HF](https://huggingface.co/bageldotcom/paris), [Blogpost](https://blog.bagel.com/p/paris)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/oct-9-2025-dev-days-agent-era-samsungs/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/oct-9-2025-dev-days-agent-era-samsungs?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3NTc2MzI3NywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.nCaXqps9R_lHUU4d4gVt37FHTRYs5R2ucI6t8xDxMhE&utm_campaign=CTA_5).
