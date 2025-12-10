# ThursdAI - Oct 30 - From ASI in a Decade to Home Humanoids: MiniMax M2's Speed Demon, OpenAI's Bold Roadmap, and 2026 Robot Revolution

**Date:** October 30, 2025  
**Duration:** 1:37:29  
**Link:** [https://sub.thursdai.news/p/thursdai-oct-30-2025-minimax-m2-shocks](https://sub.thursdai.news/p/thursdai-oct-30-2025-minimax-m2-shocks)

---

## Description

Hey, it’s Alex! Happy Halloween friends! 

I’m excited to bring you this weeks (spooky) AI updates! We started the show today with MiniMax M2, the currently top Open Source LLM, with an interview with their head of eng, Skyler Miao, continued to dive into OpenAIs completed restructuring into a non-profit and a PBC, including a deep dive into a live stream Sam Altman had, with a ton of spicy details, and finally chatted with Arjun Desai from Cartesia, following a release of Sonic 3, a sub 49ms voice model! 

So, 2 interviews + tons of news, let’s dive in! (as always, show notes in the end)

Hey, if you like this content, it would mean a lot if you subscribe as a paid subscriber.

Open Source AI

MiniMax M2: open-source agentic model at 8% of Claude’s price, 2× speed ([X](https://x.com/MiniMax__AI/status/1982674798649160175), [Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M2) )

We kicked off our open-source segment with a banger of an announcement and a special guest. The new king of open-source LLMs is here, and it’s called **MiniMax M2**. We were lucky enough to have Skyler Miao, Head of Engineering at Minimax, join us live to break it all down.

M2 is an agentic model built for code and complex workflows, and its performance is just staggering. It’s already ranked in the top 5 globally on the Artificial Analysis benchmark, right behind giants like OpenAI and Anthropic. But here’s the crazy part: it delivers nearly **twice the speed** of Claude 3.5 Sonnet at just **8% of the price**. This is basically Sonnet-level performance, at home, in open source.

Skylar explained that their team saw an “impossible triangle” in the market between performance, cost, and speed—you could only ever get two. Their goal with M2 was to build a model that could solve this, and they absolutely nailed it. It’s a 200B parameter Mixture-of-Experts (MoE) model, but with only 10B active parameters per inference, making it incredibly efficient.

One key insight Skylar shared was about getting the best performance. M2 supports multiple APIs, but to really unlock its reasoning power, you need to use an API that passes the model’s “thinking” tokens back to it on the next turn, like the Anthropic API. Many open-source tools don’t support this yet, so it’s something to watch out for.

Huge congrats to the MiniMax team on this Open Weights (MIT licensed) release, you can find the model on [HF](https://huggingface.co/MiniMaxAI/MiniMax-M2)! 

MiniMax had quite a week, with 3 additional releases, MiniMax speech 2.6, an update to their video model [Hailuo 2.3](https://x.com/Hailuo_AI/status/1983382728343994414) and just after the show, they released a music 2.0 [model](https://x.com/Hailuo_AI/status/1983964920493568296) as well! Congrats on the shipping folks! 

OpenAI drops gpt-oss-safeguard - first open-weight safety reasoning models for classification ( [X](https://x.com/OpenAI/status/1983507392374641071), [HF](https://huggingface.co/collections/openai/gpt-oss-safeguard) )

OpenAI is back on the open weights bandwagon, with a finetune release of their previously open weighted gpt-oss models, with gpt-oss-safeguard. 

These models were trained exclusively to help companies build safeguarding policies to make sure their apps remains safe! With gpt-oss-safeguards 20B and 120B, OpenAI is achieving near parity with their internal safety models, and as Nisten said on the show, if anyone knows about censorship and safety, it’s OpenAI! 

The highlight of this release is, unlike traditional pre-trained classifiers, these models allow for updates to policy via natural language!

These models will be great for businesses that want to safeguard their products in production, and I will advocate to bring these models to W&B Inference soon! 

A Humanoid Robot in Your Home by 2026? 1X NEO announcement ( [X](https://x.com/1x_tech/status/1983233494575952138), [Order page](https://www.1x.tech/order), [Keynote](https://youtu.be/LTYMWadOW7c) )

Things got really spooky when we started talking about robotics. The company 1X, which has been on our radar for a while, officially launched pre-orders for **NEO**, the world’s first consumer humanoid robot designed for your home. And yes, you can order one right now for $20,000, with deliveries expected in early 2026.

The internet went crazy over this announcement, with folks posting receipts of getting one, other folks stoking the uncanny valley fears that Sci-fi has built into many people over the years, of the Robot uprising and talking about the privacy concerns of having a human tele-operate this Robot in your house to do chores. 

It can handle chores like cleaning and laundry, and for more complex tasks that it hasn’t learned yet, it uses a teleoperation system where a human “1X Expert” can pilot the robot remotely to perform the task. This is how it collects the data to learn to do these tasks autonomously in your specific home environment.

The whole release is very interesting, from the “soft and quiet” approach 1X is taking, making their robot a 66lbs short king, draped in a knit sweater, to the $20K price point (effectively at loss given how much just the hands cost), the teleoperated by humans addition, to make sure the Robot learns about your unique house layout. 

The conversation on the show was fascinating. We talked about all the potential use cases, from having it water your plants and look after your pets while you’re on vacation to providing remote assistance for elderly relatives. Of course, there are real privacy concerns with having a telepresence device in your home, but 1X says these sessions are scheduled by you and have strict no-go zones.

Here’s my prediction: by next Halloween, we’ll see videos of these NEO robots dressed up in costumes, helping out at parties. The future is officially here. Will you be getting one? If not this one, when will you think you’ll get one? 

OpenAI’s Grand Plan: From Recapitalization to ASI

This was by far the biggest update about the world of AI for me this week! Sam Altman was joined by Jakub Pachocki, chief scientist and Wojciech Zaremba, a co-founder, on a live stream to share an update about their corporate structure, plans for the future, and ASI goals (Artificial Superintelligence) 

First, the company now has a new structure: a non-profit **OpenAI Foundation** governs the for-profit **OpenAI Group**. The foundation starts with about 26% equity and has a mission to use AI for public good, including an initial $25 billion commitment to curing diseases and building an “AI Resilience” ecosystem.

But the real bombshells were about their research timeline. Chief Scientist Jakub Pachocki stated that they believe deep learning systems are **less than a decade away from superintelligence (ASI)**. He said that at this point, AGI isn’t even the right goal anymore. To get there, they’re planning to have an “AI research intern” by September 2026 and a fully **autonomous AI researcher** comparable to their human experts by March 2028. This is insane if you think about it. As Yam mentioned, OpenAI is already shipping at an insane speed, releasing Models and Products, Sora, Atlas, Pulse, ChatGPT app store, and this is with humans, assisted by AI. 

And here, they are talking about complete and fully autonomous researchers, that will be infinitely more scalable than humans, in the next 2 years. The outcomes of this are hard to imagine and are honestly mindblowing. 

To power all this innovation, Sam revealed they have over **$1.4 trillion in obligations for compute** (over 30 GW). And said even that’s not enough. Their aspiration is to build a “compute factory” capable of standing up one gigawatt of new compute *per week*, and he hinted they may need to “rethink their robotics strategy” to build the data centers fast enough. Does this mean OpenAI humanoid robots building factories? 🤔 

Plus, don’t forget, Sam is one of the investors in Helion energy, working on power solutions like Fusion, and the above graphic has an Energy block that Sam said they will give an update on later (that’s also what he told me during Dev Day when I asked him about it). 

Super exciting and honestly mind-blowing stuff, Gigawats per week, fully autonomous researchers, the world is going to look way different in a few years! 

The Agent Labs Race: Cursor 2.0 vs. Cognition’s SWE-1.5 ([X](https://x.com/cursor_ai), [Blog](https://cursor.com/blog/2-0))

This week also saw a major showdown in the agentic coding space. On the very same day, both Cursor and Cognition launched major updates and their own new models, signaling a new era where agent labs are training their own specialized AI.

First up, **Cursor 2.0** was released with a completely redesigned multi-agent interface and their new model, **Composer**. Composer is claimed to be four times faster than comparable models, and the new UI is built around managing a fleet of agents that can work in parallel on your codebase. It’s a clear shift from being just an IDE to a full-fledged agent platform. Look, the UI even looks like ChatGPT and no code in sight (until you switch to IDE mode) 

Their Composer model is also very interesting, and got a lot of folks excited, but the evaluations they shared, and the fact that they didn’t disclose if that’s a finetune of a chinese model ([it likely is](https://x.com/auchenberg/status/1983901551048470974)). Regardless, folks are saying that it’s a very good model that’s also VERY fast! 

Cognition own coding model - SWE 1.5 ( [Blog](https://cognition.ai/blog/swe-1-5), [X](https://x.com/cognition/status/1983662836896448756), [Windsurf](https://windsurf.com/download) )

Then, just hours later, Cognition punched right back with **SWE-1.5**, their new frontier agent model that now powers Windsurf. The headline here is pure speed. Powered by Cerebras, SWE-1.5 hits a blistering **950 tokens per second**—13 times faster than Sonnet 4.5—while achieving near-SOTA performance on SWE-Bench Pro. They’ve achieved this through a co-designed stack where the agent harness, inference system, and model were all built together and optimized with end-to-end reinforcement learning in real coding environments.

This competition is fantastic news for all of us. We’re seeing specialized, highly-performant models being developed outside of the big labs, putting more power back in the hands of developers.

**This Week’s Buzz**

Just a few quick updates from the world of Weights & Biases and our parent company, CoreWeave.

First, big news! CoreWeave announced the acquisition of **Marimo**, the company behind the popular open-source, reactive notebook for Python. This is another exciting step in building out the essential cloud for AI, adding powerful development tools to the stack alongside best-in-class GPU infrastructure and MLOps with Weights & Biases. Welcome to the Marimo team!

Also, [**Fully Connected**](http://fullyconnected.com) is coming to London next week! It’s our premier conference, and we’ll have speakers from Mistral, Google, LlamaIndex, and more. If you’re in Europe, please come join us. DM me if you need tickets!

And if you’re in New York from November 19-22, come say hi at the **AI Engineer Code Summit**. We’re sponsoring and will have a big booth. It’s always a great place to meet folks from this community.

**Video & Voice: The Multimodal Explosion**

The world of video and voice AI was on fire this week.

The absolute highlight was **Odyssey ML V2**, a new real-time interactive AI video platform. This thing is not like other video models that take minutes to generate a clip. With Odyssey, you type a prompt, and a video starts streaming *instantly*. Then, you can edit it live. We did a demo on the show where we prompted “army of robots in a starship corridor” and then typed “turn these robots into fluffy covered cat robots,” and the video changed in real time. It’s mind-blowing. This is a glimpse into the future of user-driven, playable media.

On the more traditional video front, **Sora** is now invite-free in the US and Japan, and they launched **Character Cameos**. You can now upload photos of your pets or objects (like your kid’s carved pumpkin!) and turn them into characters that you and others can use in videos. I, of course, immediately made a cameo of my cat, Sonia.

Voice and Audio - Cartesia launches Sonic 3, sub 50ms AI speech model

In the world of voice, we had Arjun Desai from **Cartesia** join us to talk about **Sonic-3**, their new real-time TTS engine. Backed by a new **$100M funding round**, Sonic-3 is built on State Space Models (not Transformers) and can achieve insane speeds—we’re talking under 50ms latency. But it’s not just fast; it’s also incredibly expressive. It can laugh, emote, and speak 42 languages with natural code-switching. I used their Pro Voice cloning feature to create an AI version of myself, and the results were scarily good. We even had my AI clone host a segment of the show, see it yourself here, powered by Argil and Sonic 3, this is... AI Alex

**Wrapping Up This Spooky Week 🎃**

As I sit here in my Halloween costume reflecting on this week, I can’t help but feel we’re at an inflection point. We have:

* Open source models competing with the best proprietary ones

* Humanoid robots becoming consumer products

* ASI timelines measured in single-digit years

* Real-time interactive AI across all modalities

And yet, nothing about this scares me. If anything, I’m more excited than ever about what we’re building together. Yes, the pace is insane. Yes, keeping up with everything is becoming nearly impossible (and it’s literally my job!). But we’re living through the most transformative period in human history, and we get to be part of it.

To everyone building, experimenting, and pushing boundaries - keep going. To everyone worried about what’s coming - join us in shaping it responsibly. And to everyone who celebrated Halloween today - I hope your costume was as epic as the AI developments we covered! 👻

Until next week, this is Alex signing off. Remember to subscribe, give us five stars, and I’ll see you next ThursdAI!

TL;DR - All Topics Covered

ThursdAI - Oct 30 - Halloween Special 👻

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](https://x.com/altryne))

* Co Hosts - [@WolframRvnwlf](https://x.com/WolframRvnwlf) [@yampeleg](https://x.com/yampeleg) [@nisten](https://x.com/nisten) [@ldjconfirmed](https://x.com/ldjconfirmed) [@ryancarson](http://x.com/ryancarson)

* **Guest: Skyler Miao** - Head of Engineering, MiniMax ([@SkylerMiao7](https://x.com/SkylerMiao7))

* **Guest: Arjun Desai** - CoFounder Cartesia  ([@jundesai](https://x.com/jundesai))

* **Open Source LLMs**

* **MiniMax M2**: Open-source agentic model at 8% of Claude’s price, 2× speed ([X](https://x.com/MiniMax__AI/status/1982674798649160175), [Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M2))

* **OpenAI GPT-OSS-Safeguard**: First open-weight safety reasoning models ([X](https://x.com/OpenAI/status/1983507392374641071), [HF](https://huggingface.co/collections/openai/gpt-oss-safeguard))

* **IBM Granite 4.0 Nano**: Ultra-efficient tiny models for edge deployment ([X](https://x.com/ArtificialAnlys/status/1983611955668775411), [Artificial Analysis](https://artificialanalysis.ai/models/granite))

* **Ming-flash-omni Preview**: Sparse MoE omni-modal model ([X](https://x.com/AntLingAGI/status/1982831211312722041), [HuggingFace](https://huggingface.co/inclusionAI/Ming-flash-omni-Preview))

* **Kimi Linear**: 48B parameter model with 1M context ([HF](https://huggingface.co/moonshotai/Kimi-Linear-48B-A3B-Instruct))

* **Robotics**

* **1X NEO**: First consumer humanoid robot, $20k, delivery 2026 ([X](https://x.com/1x_tech/status/1983233494575952138), [Order page](https://www.1x.tech/order), [Keynote](https://youtu.be/LTYMWadOW7c))

* **Big Companies & APIs**

* **OpenAI Restructuring**: ASI within 10 years, AI researcher by 2028 ([X](https://x.com/AndrewCurran_/status/1983161944208220550))

* **Cursor 2.0 & Composer**: 4x faster coding, new model ([X](https://x.com/cursor_ai), [Blog](https://cursor.com/blog/2-0))

* **Cognition SWE-1.5**: 950 tok/s, 40% SWE-bench Pro ([Blog](https://cognition.ai/blog/swe-1-5), [X](https://x.com/cognition/status/1983662836896448756), [Windsurf](https://windsurf.com/download))

* **Perplexity Email Assistant**: Privacy-first AI inbox management ([X](https://x.com/perplexity_ai/status/1983591113903738970), [Assistant Site](https://www.perplexity.ai/assistant))

* **This Week’s Buzz**

* Fully Connected London - [fullyconnected.com](https://fullyconnected.com)

* AI Engineer Code Summit NYC - Nov 19-22

* CoreWeave acquires Marmo notebooks ([X](https://x.com/marimo_io/status/1983916371869364622))

* **Vision & Video**

* **Odyssey ML V2**: Real-time interactive AI video ([X](https://x.com/odysseyml/status/1982856110290939989), [Experience](https://experience.odyssey.ml))

* **Sora**: Now invite-free + Character Cameos feature ([X](https://x.com/OpenAI/status/1983661036533379486), [Sonia Cameo](https://sora.chatgpt.com/p/s_6902d8b223d88191a04adfada2e9f5b5))

* **Hailuo 2.3**: Cinema-grade video generation ([X](https://x.com/Hailuo_AI/status/1983016390878708131))

* **Voice & Audio**

* **MiniMax Speech 2.6**: <250ms ultra-human voice AI ([X](https://x.com/Hailuo_AI/status/1983557055819768108), [MiniMax](https://minimaxi.com/audio), [API Docs](https://platform.minimax.io/docs/guides/sp))

* **Cartesia Sonic 3**: Real-time TTS with emotion & laughter, $100M funding ([X](https://x.com/krandiash/status/1983202316397453676), [Website](https://cartesia.ai/sonic), [Docs](https://docs.cartesia.ai/2024-11-13/get-started/overview))

* **Tools**

* **Pokee**: Agentic workflow builder ([X](https://x.com/Pokee_AI/status/1983202159262150717))

* **Pomelli**: Google’s AI marketing agent ([X](https://twitter.com/testingcatalog/status/1983214036259938553), [Labs](https://labs.google.com/pomelli/about/?ref=testingcatalog.com)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-oct-30-2025-minimax-m2-shocks/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-oct-30-2025-minimax-m2-shocks?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3NzYwNzA3MCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.Z91yXvekATldr53MP5TfO79U0CFgSujGPDLFbYtV7Xo&utm_campaign=CTA_5).
