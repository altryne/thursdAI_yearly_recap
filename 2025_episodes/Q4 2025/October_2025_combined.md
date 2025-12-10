# ThursdAI Episodes - October 2025

Total Episodes: 5

---

## ThursdAI - Oct 30 - From ASI in a Decade to Home Humanoids: MiniMax M2's Speed Demon, OpenAI's Bold Roadmap, and 2026 Robot Revolution

**Date:** October 30, 2025  
**Duration:** 1:37:29  
**Link:** [https://sub.thursdai.news/p/thursdai-oct-30-2025-minimax-m2-shocks](https://sub.thursdai.news/p/thursdai-oct-30-2025-minimax-m2-shocks)

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

---

## 📆 ThursdAI - Oct 23: The AI Browser Wars Begin, DeepSeek's OCR Mind-Trick & The Race to Real-Time Video

**Date:** October 24, 2025  
**Duration:** 1:35:16  
**Link:** [https://sub.thursdai.news/p/thursdai-oct-23-the-ai-browser-wars](https://sub.thursdai.news/p/thursdai-oct-23-the-ai-browser-wars)

Hey everyone, Alex here! 

Welcome... to the browser war II - the AI edition! This week we chatted in depth about ChatGPT’s new Atlas agentic browser, and the additional agentic powers Microsoft added to Edge with Copilot Mode (tho it didn’t work for me) 

Also this week was a kind of crazy OCR week, with more than 4 OCR models releasing, and the crown one is DeepSeek OCR, that turned the whole industry on it’s head (more later) 

Quite a few video updates as well, with real time lipsync from Decart, and a new update from LTX with 4k native video generation, it’s been a busy AI week for sure! 

Additionally, I’ve had the pleasure to talk about AI Browsing agents with Paul from BrowserBase and real time video with Kwindla Kramer from Pipecat/Daily, so make sure to tune in for those interviews, buckle up, let’s dive in! 

Thanks for reading ThursdAI - Recaps of the most high signal AI weekly spaces! This post is public so feel free to share it.

**Open Source: OCR is Not What You Think It Is **([X](https://x.com/Presidentlin/status/1980159652563415094), [HF](https://huggingface.co/deepseek-ai/DeepSeek-OCR), [Paper](https://github.com/deepseek-ai/DeepSeek-OCR/blob/main/DeepSeek_OCR_paper.pdf))

The most important and frankly mind-bending release this week came from DeepSeek. They dropped DeepSeek-OCR, and let me tell you, this is NOT just another OCR model. The cohost were buzzing about this, and once I dug in, I understood why. This isn’t just about reading text from an image; it’s a revolutionary approach to **context compression**.

We think that DeepSeek needed this as an internal tool, so we’re really grateful to them for open sourcing this, as they did something crazy here. They are essentially turning text into a visual representation, compressing it, and then using a tiny vision decoder to read it back with incredible accuracy. We’re talking about a compression ratio of up to **10x with 97% decoding accuracy**. Even at 20x compression they are achieving 60% decoding accuracy! My head exploded live on the show when I read that. This is like the middle-out compression algorithm joke from *Silicon Valley*, but it’s real. As Yam pointed out, this suggests our current methods of text tokenization are far from optimal.

With only 3B and ~570M active parameters, they are taking a direct stab at long context inefficiency, imagine taking 1M tokens, encoding them into 100K visual tokens, and then feeding those into a model. Since the model is tiny, it’s very cheap to run, for example, [**alphaXiv**](https://x.com/askalphaxiv)** **claimed they have OCRd’ all of the papers on ArXiv with this model for $1000, a task that would have cost $7500 using MistalOCR - as per their paper, with DeepSeek OCR, on a single H100 GPU, its possible to scan up to 200K pages! 🤯 Really innovative stuff! 

OCR and VLM models had quite a week, with multiple models besides DeepSeek OCR releasing, models like Liquids LFM2-VL-3B ([X](https://x.com/LiquidAI_/status/1980985540196393211), [HF](https://huggingface.co/liquidai/lfm2-vl-3b)), and the newly updated 2B and 32B of Qwen3-VL ([X](https://x.com/Alibaba_Qwen/status/1980665932625383868), [Hugging Face](https://huggingface.co/collections/Qwen3-VL)), and AI2’s olmo-ocr 2-7B ([X](https://x.com/allen_ai/status/1981029159267659821), [HF](https://huggingface.co/allenai/olmOCR-2-7B-1025-FP8)). 

The Qwen models are particularly interesting, as the 2B model is a generic VLM (can also do OCR) and is close to previous weeks 4B and 8B brothers, and the newly updated 32B model outperforms GPT-5 mini and Claud 4 sonnet even! 

The Browser Wars are BACK: OpenAI & Microsoft Go Agentic

Look, I may be aging myself here, but I remember, as a young frontend dev, having to install 5 browers at once to test them out, Chrome, Internet Explorer, Firefox, Opera etc’. That was then, and now, I have Dia, Comet, and the newly released Atlas, and, yeah, today I even installed Microsoft Edge to test their AI features! It seems like the AI boom brought with it a newly possible reason for folks to try and take a bite out of Chrome (who’s agentic features are long rumored with project mariner but are nowhere to be found/shipped yet) 

OpenAI’s ChatGPT Atlas: The Browser Reimagined ([X](https://x.com/OpenAI/status/1980685602384441368), [Download](https://chatgpt.com/atlas/get-started/))

OpenAI is proving that besides just models, they are a product powerhouse, stepping into categories like Shopping (with a shopify integration), app stores (with ChatGPT apps), social (with Sora2) and now... browsers! This week, they have launched their tightly integrated into ChatGPT browser called Atlas, and it’s a big release! 

I’ll split my review here to 2 parts, the browser features part and the agentic part. 

New fresh take on a chromium based browser

The tight integration into ChatGPT is everywhere in this browser, from the new tab that looks like the basic ChatGPT interaface, one line of text, to the sidebar on the left that... is the ChatGPT web sidebar with all your chats, projects, custom GPTs etc. 

The integration doesn’t stop there, as you have to sign in to your ChatGPT account to even use this browser (available only to MacOS users, and Pro, Plus and Nano tiers). The browser has a few neat tricks, like a special tool that allows you to search your browsing history with natural language, a-la “what were those shoes I was looking at a few days ago” will find your the tabs you browsed for shoes. 

A special and cool feature is called, confusingly “Cursor”, wherein you can select a text, and then click the little OpenAI logo that pops up, allowing you to ask ChatGPT for changes to that selected text (like fix typos, spruce up your writing etc). It’s surprisingly convenient to rewrite tweets or for any type of document editing. 

ChatGPT Atlas also stores memories about your browsing patterns, which will be additional to the ChatGPT memories it stores about you from chats, helping even more by knowing your browsing patterns, which software you prefer to use, which websites you prefer to order food from etc. This IMO is one of the hugest unlocks for folks inside the ChatGPT ecosystem, as much of a stanard persons peferences can be gleaned from their browser usage and patterns.

Lastly, the “Ask ChatGPT” sidepane on the right (which can be opened with cmd+.) is really great for chatting with a webpage, or going down search rabbit holes. It receives the context of the webpage you’re looking at by default (only 1 page so far, competitors allow you to add additional tabs with @, (which is supposedly coming to ChatGPT soon) and ask... ChatGPT anything about this. 

Agentic SOTA? not so fast

The most important “change” to how browsers work in Atlas imo is the agentic mode. This isn’t new, we remember when ChatGPT launched thier Operator Agent back in January of this year (our [coverage](https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1)) and then renamed it Agent Mode and integrated into ChatGPT itself back in [July](https://sub.thursdai.news/p/thursdai-july-17th-kimi-k2-openai). 

So, web browsing agents are not entirely new, what’s novel here though, is the integration into your browser, and the ability for the Atlas browser to use your logged in sessions and cookies, to pretend to be you! This... can be quite scary for some, as prompt injection attacks are getting more popular (where-in malicious assholes add hidden instructions to their website that will get the agent to do something you don’t like) but it’s also very exciting, as the agent can do much much more, without getting blocked by providers who could previously just block Agent Mode as it ran on OpenAI servers! 

Until today, there were 2 main Agentic browsers in the mix, Perplexity’s Comet (where you can choose which model runs the agent) and Atlas. Comet seems to be doing a little bit better on some stuff on my tests, but not by much. I have the same agentic task (go to [X.com](http://X.com), find my bookmarks, open all links, summarize per my specific format) that I’ve been running for a while now, and Comet outdid Atlas this week on that task.

Who needs agentic browsing? 

For some reason, most of the demos for agentic browsing are showing the same, boring-ish examples. Book some flights, collect a grocery shopping cart. I’ve tried new and different things this week, for example, letting Atlas choose and order food for me (as ChatGPT knows my pescatarian preferences, it’s better than Comet for personal stuff), and one of the longest task I’ve had an agent do yet, I asked it to complete a Compliance training I had to take at work! 

Mind you, this is a very complex task, even for regular people, as these compliance websites are built to not be messed with. They have video players that stop if you switch focus to some other tab, they have interactive quizes and games, drag and drop interfaces, audio buttons, to make sure you really are taking the test. I can happily report, that after 5 hours, and a few stops along the way (where I had to convince the agent to keep going), it completed this very hard task! (and now I have to take this course myself again to actualy be compliant 😅 it will probably take me 2 hours to do manually) 

This experiment made me think, who needs the agentic browsing features and for what? Well, for tasks that require a lot of manual steps to do the same thing over and over again, agentic browser is going to make a lot of peoples browsing a lot easier. Things like kids schedules reviewing in multiple websites, collecitng data and formatting it differently etc. 

Scary security implications 

Atlas could only finish my compliance task while being logged in as me, and ChatGPT Atlas gives a all or nothing control. You can run your agent with full access to your logged in websites (think Gmail etc) or you can essentially give it an incognito mode. 

This, again, due to the risk of promp injections in malicious websites being more and more prevalent. In a rare post detailing how they are thinking about this, OpenAI Chief Information Security officer offered a deep dive into their attempts to mitigate this issue (Simon Willison had a great breakdown of that information [here](https://simonwillison.net/2025/Oct/22/openai-ciso-on-atlas/)) but that’s likely not enough, so definitely be aware when you’re running agent mode (which needs to be explicitly turned on right now by selecting Agent) 

This Weeks Buzz - Weights & Biases // Coreweave

Weights & Biases (now proudly part of CoreWeave) had some exciting updates. Our Fully Connected conference series is hitting Tokyo on October 30-31 and London on November 4-5—perfect for ML practitioners and AI engineers. If you’re in the area, join us for talks, networking, and deep dives into the latest. Register at [**Fullyconnected.com**](Fullyconnected.com)—DM me if you need a hook-up!

We also collaborated with Meta and Stanford on Torch Forge, a new PyTorch-native library for scalable RL post-training and agent development. It’s built for massive GPU runs (we provided 520 H100s!), competing with Ray via tools like Monarch scheduler. If you’re training on clusters, check the [blog](https://pytorch.org/blog/introducing-torchforge/) —it’s a big deal for efficient multi-GPU workflows.

Microsoft goes after OpenAI with Edge copilot mode ([X](https://x.com/mustafasuleyman/status/1981390345578697199))

In a pretty surprising move, Microsoft announced today their take on the agentic browser war, with a bunch of enhancements to Copilot (their overall word for their AI assistance across Microsoft 360, Browser, Bing search etc), Think.. clippy, for the AI age (they even brought clippy back as an [easter egg](https://x.com/satyanadella/status/1981466897557196837)) 

The short version is, Edge is getting more powerful with custom agentic features (which I enabled and couldn’t get to work no matter how much I tried, so I can’t tell you how they compare to Atlas/Comet), and they have a voice mode that allows you to talk to your browser, with Edge having a sense of what’s on the actual page! Of course, this being Microsoft, marketing aside and features aside, when I asked Copilot if it has access to other tabs (like the marketing video claims) it said it doesn’t have access, agentic mode didn’t work, and I’m very unlikely to be testing it further! But hey, if you use Copilot app on your mobile phone, and click the new Mico avatar like 25 times it will turn into Clippy, so.. yay? 

**Claude Code on the Web, Claude on Desktop upgraded **([X](https://x.com/btibor91/status/1980340485152715095), [Anthropic](https://www.anthropic.com/news/claude-code-on-the-web))

Anthropic also made waves by bringing Claude Code to the web. Now you can delegate software tasks to Claude through a web interface with GitHub integration. Nisten was particularly excited about being able to manage his coding projects from his phone. It runs tasks in a secure sandbox, can handle multiple repos, and automatically create pull requests. It’s another powerful coding agent becoming more accessible to developers everywhere. 

They have also made changes to the desktop Claude app, allowing it to see the context of your screen with screenshots, and file sharing, and even a new voice mode that allows you to talk to Claude (which is unfortunately mapped to the tab button, without the ability to remap) 

**Browser Automation and Delegated Authentication with Browserbase **([X](https://x.com/pk_iv/status/1980653648310071663), [Director.ai](https://director.ai/?ref=producthunt), [Stagehand](https://stagehand.dev/))

While OpenAI and Microsoft are building chat into the browser, what about bringing the browser into our chat-based agents? We had Paul Klein, the founder of Browserbase, join us to talk about this exact topic. His company is tackling one of the biggest hurdles for AI agents: authentication.

Paul and his team launched Director 2.0, a platform that lets you build web automation with natural language prompts. But the real innovation here is their integration with **1Password**. Instead of giving an agent the “master keys” to all your logged-in sessions like Atlas does, Browserbase allows for delegated, per-site authentication. When an agent running in the cloud needs to log into a site on your behalf, you get a prompt on your local machine to approve it. This is a much safer, more granular way to give agents the access they need. As Paul said, you shouldn’t let an AI the master keys into your house; you should give it permission to enter one room at a time. It’s a brilliant paradigm for secure agentic workflows and I really like this approach of a piece-meal authentication for browser agents. I wish Atlas has something like this for the incognito mode! 

Director 2.0 itself is like V0 for web automation—you give it a prompt, it performs the task, and then it gives you a repeatable script you can deploy. It’s a way to create robust automations without needing to be a developer, and it’s already being used to automate thousands of hours of manual work. 

Video & Audio: The Race to Real-Time

The world of generative media is moving at lightning speed, with a clear trajectory towards real-time, interactive experiences.

**Decart’s Real-Time Lip Sync API **([X](https://x.com/DecartAI/status/1981078296084488293))

We had Kwindla Kramer, one of the worlds leading experts in real-time audio, join us to break down a phenomenal release from Decart AI: a real-time lip-sync API. This isn’t the pre-rendered, slightly-off lip-sync we’re used to. This is a pipeline of models working together to generate perfectly synchronized lip movements for an avatar in real-time.

Kwindla explained the tech stack: it captures your audio via WebRTC, sends it to Whisper for transcription, gets a response from an LLM like Grok, generates a voice with ElevenLabs, and then Decart’s model modifies the avatar’s video frames to match the new audio, all with a sub-two-second latency. This is how we get to truly interactive, believable AI characters. Kwindla even built a quick demo, though it didn’t seem to work the in the morning, probably GPU issues, so we just played the demo videos. 

**LTX-2 and Sora’s Pet Cameos**

The trend towards high-fidelity, real-time generation continued with a breaking news release from Lightricks: LTX-2. This is an open-source (weights coming this fall!) engine that can generate **native 4K video with synchronized audio**. It’s fast, efficient, and is set to be a powerful open alternative to closed models like Sora. And it’s a native 4K, no upscaling! 

Speaking of Sora, they announced that character cameos are getting an upgrade. Soon, you’ll be able to turn anything—your pet, a coffee cup, or even a sunny-side-up egg—into an animated, talking character. I’m really looking forward for this new Sora update and will let you know my impressions when it drops (soon, [according to](https://x.com/billpeeb/status/1981118483607032050) Bill from OpenAI) 

What a week folks! What A WEEK! 😅 My head is still spinning! 

From browsers that can do our work for us to OCR that redefines context, we’re seeing foundational shifts across the board. The tools are getting more powerful, more accessible, and more integrated into our daily workflows. The future is being built right now, and we get to watch it happen week by week.

Thank you for being a ThursdAI subscriber. As always, here are the show notes with all the links and details from this week’s whirlwind of AI news.

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@yampeleg](https://x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed)

* Paul Kelin [@pk_iv](https://x.com/pk_iv) - Browser Base

* Kwindla Kramer [@kwindla](https://x.com/kwindla) - Pipecat & Daily

* **Open Source LLMs**

* DeepSeek-OCR: Efficient Vision-Text Compression for Massive Contexts ([X](https://x.com/Presidentlin/status/1980159652563415094), [HF](https://huggingface.co/deepseek-ai/DeepSeek-OCR), [Paper](https://github.com/deepseek-ai/DeepSeek-OCR/blob/main/DeepSeek_OCR_paper.pdf))

* Liquid AI LFM2-VL-3B: Tiny Multilingual Vision-Language Model ([X](https://x.com/LiquidAI_/status/1980985540196393211), [HF](https://huggingface.co/liquidai/lfm2-vl-3b))

* PokeeResearch-7B: Open-source SOTA Deep Research Agent ([X](https://x.com/Pokee_AI/status/1981040897346179256), [HF](https://huggingface.co/PokeeAI/pokee_research_7b), [Web](https://pokee.ai/deepresearch-preview), [ArXiv](https://arxiv.org/pdf/2510.15862.pdf), [GitHub](https://github.com/Pokee-AI/PokeeResearchOSS))

* Qwen3-VL 2B & 32B: compact STEM-tuned multimodal powerhouses ([X](https://x.com/Alibaba_Qwen/status/1980665932625383868), [Hugging Face](https://huggingface.co/collections/Qwen3-VL))

* **Big CO LLMs + APIs**

* OpenAI announces Atlas - its agentic AI browser ([X](https://x.com/OpenAI/status/1980685602384441368), [Download](https://chatgpt.com/atlas/get-started/))

* [Security Implications, Injection + note from CISO](https://x.com/cryps1s/status/1981037851279278414)

* Claude Code on the Web: Cloud Coding with Secure Sandboxing ([X](https://x.com/btibor91/status/1980340485152715095), [Anthropic](https://www.anthropic.com/news/claude-code-on-the-web))

* Meta bans 1‑800‑ChatGPT on WhatsApp

* Microsoft agentic addition to Copilot Mode in Edge ([X](https://x.com/MicrosoftEdge/status/1981028712830185914))

* Gemini AI Studio launches “Vibe Coding” ([X](https://x.com/OfficialLoganK/status/1980674135693971550), [AI Studio Build](https://ai.studio/build))

* **This weeks Buzz**

* Fully connected comes to Tokyo (Oct 30-31) and London (Nov 4-5) ! ([register at Fullyconnected.com](https://fullyconnected.com))

* **Vision & Video**

* Sora is about to get pet cameos

* Krea open‑sources a 14‑billion‑parameter real‑time video model ([X](https://x.com/krea_ai/status/1980358158376988747), [HF](https://huggingface.co/krea/krea-realtime-video))

* Reve’s unannounced video mode!? 1080p + sound

* LTX-2: open-source 4K audio+video generation engine from Lightricks ([X](https://x.com/ltx_model/status/1981377626347323480), [Website](https://ltx.studio/), [GitHub](https://github.com/Lightricks/LTX-Video))

* **Voice & Audio**

* Decart Lip Sync API: Real-Time Avatar Lip Movement ([X](https://x.com/DecartAI/status/1981078296084488293))

* **Tools**

* Browserbase launches Director 2.0: prompt-powered web automation ([X](https://x.com/pk_iv/status/1980653648310071663), [Director.ai](https://director.ai/?ref=producthunt), [Stagehand](https://stagehand.dev/)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-oct-23-the-ai-browser-wars/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-oct-23-the-ai-browser-wars?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3Njk3NTE5MiwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.tNE8S7hoO4vWQxj7pHyZaahDJoehF-0fMhAd_z-WQuE&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Oct 16 - VEO3.1, Haiku 4.5, ChatGPT adult mode, Claude Skills, NVIDIA DGX spark, Wordlabs RTFM & more AI news

**Date:** October 17, 2025  
**Duration:** 1:34:38  
**Link:** [https://sub.thursdai.news/p/thursdai-oct-16-veo31-haiku-45-chatgpt](https://sub.thursdai.news/p/thursdai-oct-16-veo31-haiku-45-chatgpt)

Hey folks, Alex here. 

Can you believe it’s already the middle of October? This week’s show was a special one, not just because of the mind-blowing news, but because we set a new ThursdAI record with **four** incredible interviews back-to-back!

We had Jessica Gallegos from Google DeepMind walking us through the cinematic new features in VEO 3.1. Then we dove deep into the world of Reinforcement Learning with my new colleague Kyle Corbitt from OpenPipe. We got the scoop on Amp’s wild new ad-supported free tier from CEO Quinn Slack. And just as we were wrapping up, Swyx ( from [Latent.Space](https://substack.com/profile/89230629-latentspace) , now with Cognition!) jumped on to break the news about their blazingly fast SWE-grep models. 

But the biggest story? An AI model from Google and Yale made a novel scientific discovery about cancer cells that was then *validated in a lab*. This is it, folks. This is the “let’s fucking go” moment we’ve been waiting for. So buckle up, because this week was an absolute monster. Let’s dive in!

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Open Source: An AI Model Just Made a Real-World Cancer Discovery

We always start with open source, but this week felt different. This week, open source AI stepped out of the benchmarks and into the biology lab.

Our friends at Qwen kicked things off with new 3B and 8B parameter versions of their Qwen3-VL vision model. It’s always great to see powerful models shrink down to sizes that can run on-device. What’s wild is that these small models are outperforming last generation’s giants, like the 72B Qwen2.5-VL, on a whole suite of benchmarks. The 8B model scores a 33.9 on OS World, which is incredible for an on-device agent that can actually see and click things on your screen. For comparison, that’s getting close to what we saw from Sonnet 3.7 just a few months ago. The pace is just relentless.

But then, Google dropped a [bombshell](https://blog.google/technology/ai/google-gemma-ai-cancer-therapy-discovery/). A 27-billion parameter Gemma-based model they developed with Yale, called C2S-Scale, generated a completely novel hypothesis about how cancer cells behave. This wasn’t a summary of existing research; it was a new idea, something no human scientist had documented before. And here’s the kicker: researchers then took that hypothesis into a wet lab, tested it on living cells, and proved it was true.

This is a monumental deal. For years, AI skeptics like Gary Marcus have said that LLMs are just stochastic parrots, that they can’t create genuinely new knowledge. This feels like the first, powerful counter-argument. Friend of the pod, Dr. Derya Unutmaz, has been on the show before saying AI is going to solve cancer, and this is the first real sign that he might be right. The researchers noted this was an “emergent capability of scale,” proving once again that as these models get bigger and are trained on more complex data—in this case, turning single-cell RNA sequences into “sentences” for the model to learn from—they unlock completely new abilities. This is AI as a true scientific collaborator. Absolutely incredible.

Big Companies & APIs

The big companies weren’t sleeping this week, either. The agentic AI race is heating up, and we’re seeing huge updates across the board.

Claude Haiku 4.5: Fast, Cheap Model Rivals Sonnet 4 Accuracy ([X](https://x.com/claudeai/status/1978505436358697052), [Official blog](https://www.anthropic.com/news/introducing-claude-haiku-4-5), [X](https://x.com/danshipper/status/1978506914498834484))

First up, Anthropic released Claude Haiku 4.5, and it is a beast. It’s a fast, cheap model that’s punching way above its weight. On the SWE-bench verified benchmark for coding, **it hit 73.3%**, putting it right up there with giants like GPT-5 Codex, but at a fraction of the cost and twice the speed of previous Claude models. Nisten has already been putting it through its paces and loves it for agentic workflows because it just follows instructions without getting opinionated. It seems like Anthropic has specifically tuned this one to be a workhorse for agents, and it absolutely delivers. 

The thing to note also is the very impressive jump in OSWorld (**50.7%**), which is a computer use benchmark, and at this price and speed ($1/$5 MTok input/output) is going to make computer agents much more streamlined and speedy! 

ChatGPT will loose restrictions; age-gating enables “adult mode” with new personality features coming ([X](https://x.com/sama/status/1978129344598827128)) 

Sam Altman set X on fire with a [thread](https://x.com/sama/status/1978129344598827128) announcing that ChatGPT will start loosening its restrictions. They’re planning to roll out an “adult mode” in December for age-verified users, potentially allowing for things like erotica. More importantly, they’re bringing back more customizable personalities, trying to recapture some of the magic of GPT-4.0 that so many people missed. It feels like they’re finally ready to treat adults like adults, letting us opt-in to R-rated conversations while keeping strong guardrails for minors. This is a welcome change, and we’ve been advocating for this for a while, and it’s a notable change from the XAI approach I covered [last week](https://open.substack.com/pub/thursdai/p/oct-9-2025-dev-days-agent-era-samsungs?r=2imipa&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true). Opt in for adults with verification while taking precautions vs engagement bait in the form of a flirty animated waifu with engagement mechanics. 

Microsoft is making every windows 11 an AI PC with copilot voice input and agentic powers ([Blog](https://blogs.windows.com/windowsexperience/2025/10/16/making-every-windows-11-pc-an-ai-pc/),[X](https://x.com/zacbowden/status/1978822883217461388))

And in breaking news from this morning, Microsoft announced that every Windows 11 machine is becoming an AI PC. They’re building a new Copilot agent directly into the OS that can take over and complete tasks for you. The really clever part? It runs in a secure, sandboxed desktop environment that you can watch and interact with. This solves a huge problem with agents that take over your mouse and keyboard, locking you out of your own computer. Now, you can give the agent a task and let it run in the background while you keep working. This is going to put agentic AI in front of hundreds of millions of users, and it’s a massive step towards making AI a true collaborator at the OS level.

NVIDIA DGX - the tiny personal supercomputer at $4K  ([X](https://twitter.com/lmsysorg), [LMSYS Blog](https://lmsys.org/blog/2025-10-13-nvidia-dgx-spark/))

NVIDIA finally delivered their promised AI Supercomputer, and while the excitement was in the air with Jensen hand delivering the DGX Spark to OpenAI and Elon (recreating that historical picture when Jensen hand delivered a signed DGX workstation while Elon was still affiliated with OpenAI). The workstation was sold out almost immediately. Folks from LMSys did a great [deep dive](https://lmsys.org/blog/2025-10-13-nvidia-dgx-spark/) into specs, all the while, folks on our feeds are saying that if you want to get the maximum possible open source LLMs inference speed, this machine is probably overpriced, compared to what you can get with an M3 Ultra Macbook with 128GB of RAM or the RTX 5090 GPU which can get you similar if not better speeds at significantly lower price points. 

Anthropic’s “Claude Skills”: Your AI Agent Finally Gets a Playbook ([Blog](https://www.anthropic.com/news/skills))

Just when we thought the week couldn’t get any more packed, Anthropic dropped “Claude Skills,” a huge upgrade that lets you give your agent custom instructions and workflows. Think of them as expertise folders you can create for specific tasks. For example, you can teach Claude your personal coding style, how to format reports for your company, or even give it a script to follow for complex data analysis.

The best part is that Claude automatically detects which “Skill” is needed for a given task, so you don’t have to manually load them. This is a massive step towards making agents more reliable and personalized, moving beyond just a single custom instruction and into a library of repeatable, expert processes. It’s available now for all paid users, and it’s a feature I’ve been waiting for. Our friend [Simon Willison](https://substack.com/profile/5753967-simon-willison) things skills may be [a bigger deal than MCPs](https://simonwillison.net/2025/Oct/16/claude-skills/)! 

🎬 Vision & Video: Veo 3.1, Sora Gets Longer, and Real-Time Worlds

The AI video space is exploding. We started with an amazing interview with Jessica Gallegos, a Senior Product Manager at Google DeepMind, all about the new Veo 3.1. This is a significant 0.1 update, not a whole new model, but the new features are game-changers for creators.

The audio quality is way better, and they’ve massively improved video extensions. The model now conditions on the last second of a clip—including the audio. This means if you extend a video of someone talking, they keep talking in the same voice! This is huge, saving creators from complex lip-syncing and dubbing workflows. They also added object insertion and removal, which works on both generated and real-world video. Jessica shared an incredible story about working with director Darren Aronofsky to insert a virtual baby into a live-action film shot, something that’s ethically and practically very difficult to do on a real set. These are professional-grade tools that are becoming accessible to everyone. Definitely worth listening to the whole interview with Jessica, starting at 00:25:44

I’ve played with the new VEO in Google Flow, and while I was somewhat (still) disappointed with the UI itself (it froze sometimes and didn’t play). I wasn’t able to upload my own videos to use the insert/remove features Jessica mentioned yet, but saw examples online and they looked great! 

Ingredients were also improved with VEO 3.1, where you can add up to 3 references, and they will be included in your video but not as first frame, the model will use them to condition the vidoe generation. Jessica clarified that if you upload sound, as in, your voice, it won’t show up in the model as your voice yet, but maybe they will add this in the future (at least this was my feedback to her). 

SORA 2 extends video gen to 15s for all, 25 seconds to pro users with a new storyboard 

Not to be outdone, OpenAI pushed a bit of an update for Sora. All users can now generate up to 15-second clips (up from 8-10), and Pro users can go up to 25 seconds using a new storyboard feature. I’ve been playing with it, and while the new scene-based workflow is powerful, I’ve noticed the quality can start to degrade significantly in the final seconds of a longer generation (posted my experiments [here](https://x.com/altryne/status/1978569726734545009)) as you can see. The last few shot so the cowboy don’t have any action, and the face is a blurry mess. 

Worldlabs RTFM: Real-Time Frame Model renders 3D worlds at interactive speeds on a single H100 ( [X](https://x.com/theworldlabs/status/1978839171058815380), [Blog](https://www.worldlabs.ai/blog/rtfm), [Demo](https://rtfm.worldlabs.ai/) )

And just when we thought we’d seen it all, World Labs dropped a breaking news release: RTFM, the Real-Time Frame Model. This is a generative world model that renders interactive, 3D-consistent worlds on the fly, all on a single H100 GPU. Instead of pre-generating a 3D environment, it’s a “learned renderer” that streams pixels as you move. We played with the demo live on the show, and it’s mind-blowing. The object permanence is impressive; you can turn 360 degrees and the scene stays perfectly coherent. It feels like walking around inside a simulation being generated just for you.

This Week’s Buzz: RL Made Easy with Serverless RL + interview with Kyle Corbitt

It was a huge week for us at Weights & Biases and CoreWeave. I was thrilled to finally have my new colleague Kyle Corbitt, founder of OpenPipe, back on the show to talk all things Reinforcement Learning (RL).

RL is the technique behind the massive performance gains we’re seeing in models for tasks like coding and math. At a high level, it lets a model try things, and then you “reward” it for good outcomes and penalize it for bad ones, allowing it to learn strategies that are better than what was in its original training data. The problem is, it’s incredibly complex and expensive to set up the infrastructure. You have to juggle an inference stack for generating the “rollouts” and a separate training stack for updating the model weights.

This is the problem Kyle and his team have solved with Serverless RL, which we just launched and we covered [last week](https://open.substack.com/pub/thursdai/p/oct-9-2025-dev-days-agent-era-samsungs?r=2imipa&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true). It’s a new offering that lets you run RL jobs without managing any servers or GPUs. The whole thing is powered by the CoreWeave stack, with tracing and evaluation beautifully visualized in Weave.

We also launched a [new model ](https://wandb.ai/site/inference/cw_openpipe_qwen3-14b-instruct)from the OpenPipe team on our inference service: a fine-tune-friendly “instruct” version of Qwen3 14B. The team is not just building amazing products, they’re also contributing great open-source models. It’s awesome to be working with them.

🛠️ Tools & Agents: Free Agents & Lightning-Fast Code Search

The agentic coding space saw two massive announcements this week, and we had the representatives of both companies on the show to discuss them!

First, Quinn Slack from Amp announced that they’re launching a completely free, ad-supported tier. I’ll be honest, my first reaction was, “Ads? In my coding agent? Eww.” But the more I thought about it, the more it made sense. My AI subscriptions are stacking up, and this model makes powerful agentic coding accessible to students and developers who can’t afford another $20/month. The ads are contextual to your codebase (think Baseten or Axiom), and they’re powered by a rotating mix of models using surplus capacity from providers. It’s a bold and fascinating business model.

This move was met with generally positive responses, though folks from a competing [agent](https://x.com/pashmerepat/status/1978934813253079383), claim that Amp is serving Grok-4-fast which XAI is giving out for free anyway? We’ll see how this shakes up. 

Cognition announces SWE-grep: RL-powered multi-turn context retriever for agentic code search ([Blog](https://cognition.ai/blog/swe-grep), [X](https://x.com/cognition/status/1978867021669413252), [Playground](https://playground.cognition.ai/), [Windsurf](https://windsurf.com/))

Then, just as we were about to sign off, friend of the pod Swyx (now from Cognition) dropped in with breaking news about SWE-grep. It’s a new, RL-tuned sub-agent for their Windsurf editor that makes code retrieval and context gathering ridiculously fast. We’re talking over 2,800 tokens per second. (yes, they are using Cerebras under the hood) 

The key insight from Swyx is that their model was trained for natively parallel tool calling, running up to eight searches on a codebase simultaneously. This speeds up the “read” phase of an agent’s workflow—which is 60-70% of the work—by 3-5x. It’s all about keeping the developer in a state of flow, and this is a huge leap forward in making agent interactions feel instantaneous. Swyx also dropped a hint that the next thing that comes is CodeMaps and they will make these retrievers look trivial! 

This was one for the books, folks. An AI making a novel cancer discovery, video models taking huge leaps, and the agentic coding space is on fire. The pace of innovation is just breathtaking. Thank you for being a ThursdAI subscriber, and as always, here’s the TL:DR and show notes for everything that happened in AI this week.

TL;DR and Show Notes

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* **Co Hosts** - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@yampeleg](http://x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed)

* **Jessica Gallegos**, Sr. Product Manager, Google DeepMind

* **Kyle Corbitt (**[**@corbtt**](https://x.com/corbtt)**)** - OpenPipe//W&B

* **Quinn Slack (**[**@sqs**](https://x.com/sqs/status/1978521044194398713)**)** - Amp

* **Swyx (**[**@swyx**](http://x.com/@swyx)**)** - Cognition

* **Open Source LLMs**

* KAIST KROMo - bilingual Korean/English 10B ([HF](https://t.co/kDIylkn5pC), [Paper](https://arxiv.org/abs/2510.09426))

* Qwen3-VL 3B and 8B ([X post](https://x.com/Alibaba_Qwen/status/1978150959621734624), [HF](https://huggingface.co/collections/Qw))

* Google’s C2S-Scale 27B: AI Model Validates Cancer Hypothesis in Living Cells ([X](https://x.com/sundarpichai/status/1978507110477332582), [Blog](https://blog.google/technology/ai/google-gemma-ai-cancer-therapy-discovery/), [Paper](https://www.biorxiv.org/content/10.1101/2025.04.14.648850v2))

* **Big CO LLMs + APIs**

* Claude Haiku 4.5: Fast, Cheap Model Rivals Sonnet 4 Accuracy ([X](https://x.com/claudeai/status/1978505436358697052), [Official blog](https://www.anthropic.com/news/introducing-claude-haiku-4-5))

* ChatGPT will loose restrictions; age-gating enables “adult mode” with new personality features coming ([X](https://x.com/sama/status/1978129344598827128))

* OpenAI updates memory management - no more “memory full” ([X](https://x.com/OpenAI/status/1978608684088643709), [FAQ](https://help.openai.com/en/articles/8590148-memory-faq))

* Microsoft is making every windows 11 an AI PC with copilot voice input ([X](https://x.com/zacbowden/status/1978822883217461388))

* Claude Skills: Custom instructions for AI agents now live ([X](https://x.com/claudeai/status/1978855432123723909), [Anthropic News](https://www.anthropic.com/news/skills), [YouTube Demo](https://www.youtube.com/watch?v=IoqpBKrNaZI))

* **Hardware**

* NVIDIA DGX Spark: desktop personal supercomputer for AI prototyping and local inference ([LMSYS Blog](https://lmsys.org/blog/2025-10-13-nvidia-dgx-spark/))

* Apple announces M5 chip with double AI performance ([Apple Newsroom](https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/))

* OpenAI and Broadcom set to deploy 10 gigawatts of custom AI accelerators ([Official announcement](https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/))

* **This weeks Buzz**

* New model - OpenPipe Qwen3 14B instruct ([link](https://wandb.ai/site/inference/cw_openpipe_qwen3-14b-instruct))

* Interview with Kyle Corbitt - RL, Serverless RL

* W&B Fully Connected London & Tokyo in 20 days - [SIGN UP](https://wandb.ai/site/resources/events/fully-connected/)

* **Vision & Video**

* Veo 3.1: Google’s Next-Gen Video Model Launches with Cinematic Audio ([Developers Blog](https://developers.googleblog.com/))

* Sora up to 15s and pro now up to 25s generation with a new storyboard feature

* Baidu’s MuseStreamer has >20 second generations ([X](https://x.com/Baidu_Inc/status/1978505872805658960))

* **AI Art & Diffusion & 3D**

* Worldlabs RTFM: Real-Time Frame Model renders 3D worlds at interactive speeds on a single H100 ([Blog](https://www.worldlabs.ai/blog/rtfm), [Demo](https://rtfm.worldlabs.ai/))

* DiT360: SOTA Panoramic Image Generation with Hybrid Training ([Project page](https://fenghora.github.io/DiT360-Page/), [GitHub](https://github.com/Insta360-Resea))

* Riverflow 1 tops the image‑editing leaderboard ([Sourceful blog](https://www.sourceful.com/blog/riverflow-1))

* **Tools**

* Amp launches a Free tier - powered by ads and surplus model capacity ([Website](https://ampcode.com/free))

* Cognition SWE-grep: RL-powered multi-turn context retriever for agentic code search ([Blog](https://cognition.ai/blog/swe-grep), [Playground](https://playground.cognition.ai/)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-oct-16-veo31-haiku-45-chatgpt/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-oct-16-veo31-haiku-45-chatgpt?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3NjM3Mjg3NywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.JdaKzfoAi5VlZyoAqjyyhpXZD-JOzxjv9_PvlujckYc&utm_campaign=CTA_5).

---

## 📆 Oct 9, 2025 — Dev Day’s Agent Era, Samsung’s 7M TRM Shock, Ling‑1T at 1T, Grok Video goes NSFW, and Serverless RL arrives

**Date:** October 10, 2025  
**Duration:** 1:41:29  
**Link:** [https://sub.thursdai.news/p/oct-9-2025-dev-days-agent-era-samsungs](https://sub.thursdai.news/p/oct-9-2025-dev-days-agent-era-samsungs)

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

---

## Sora 2 Crushes TikTok, Claude 4.5 Fizzles, DeepSeek innovates attention and GLM 4.6 Takes the Crown! 🔥

**Date:** October 03, 2025  
**Duration:** 1:39:59  
**Link:** [https://sub.thursdai.news/p/thursdai-oct-2-sora-2-the-new-tiktok](https://sub.thursdai.news/p/thursdai-oct-2-sora-2-the-new-tiktok)

Hey everyone, Alex here (yes the real me if you’re reading this) 

The weeks are getting crazier, but what OpenAI pulled this week, with a whole new social media app attached to their latest AI breakthroughs is definitely breathtaking! Sora2 released and instantly became a viral sensation, shooting to the top 3 free iOS spot on AppStore, with millions of videos watched, and remixed. 

On weeks like these, even huge releases like Claude 4.5 are taking the backseat, but we still covered them! 

For listeners of the pod, the second half of the show was very visual heavy, so it may be worth it watching the YT video attached in a comment if you want to fully experience the Sora revolution with us! (and if you want a SORA invite but don’t have one yet, more on that below) 

ThursdAI - if you find this valuable, please support us by subscribing! 

Sora 2 - the AI video model that signifies a new era of social media

Look, you’ve probably already heard about the SORA-2 release, but in case you haven’t, OpenAI released a whole new model, but attached it to a new, AI powered social media experiment in the form of a very addictive TikTok style feed. Besides being hyper-realistic, and producing sounds and true to source voice-overs, Sora2 asks you to create your own “Cameo” by taking a quick video, and then allows you to be featured in your own (and your friends) videos. 

This makes a significant break from the previously “slop” based meta Vibes, becuase, well, everyone loves seeing themselves as the stars of the show! 

Cameos are a stroke of genius, and what’s more, one can allow everyone to use their Cameo, which is what Sam Altman did at launch, making everyone Cameo him, and turning him, almost instantly into one of the most meme-able (and approachable) people on the planet! 

Sam sharing away his likeness like this for the sake of the app achieved a few things, it added trust in the safety features, made it instantly viral and showed folks they shouldn’t be afraid of adding their own likeness. 

Vibes based feed and remixing

Sora 2 is also unique in that, it’s the first social media with UGC (user generated content) where content can ONLY be generated, and all SORA content is created within the app. It’s not possible to upload pictures that have people to create the posts, and you can only create posts with other folks if you have access to their Cameos, or by Remixing existing creations. 

Remixing is also a way to let users “participate” in the creation process, by adding their own twist and vibes! 

Speaking of Vibes, while the SORA app has an algorithmic For You page, they have a completely novel and new way to interact with the algorithm, by using their Pick a Mood feature, where you can describe which type of content you want to see, or not see, with natural language! 

I believe that this feature will come to all social media platforms later, as it’s such a game changer. Want only content in a specific language? or content that doesn’t have Sam Altman in it? Just ask! 

Content that makes you feel good

The most interesting thing is about the type of content is, there’s no sexualisation (because all content is moderated by OpenAI strong filters), and no gore etc. OpenAI has clearly been thinking about teenagers and have added parent controls, things like being able to turn of the For You page completely etc to the mix. 

Additionally, SORA seems to be a very funny model, and I mean this literally. You can ask the video generation for a joke and you’ll often get a funny one. The scene setup, the dialogue, the things it does even unprompted are genuinely entertaining. 

AI + Product = Profit? 

OpenAI shows that they are one of the worlds best product labs in the world, not just a foundational AI lab. Most AI advancements are tied to products, and in this case, the whole experience is so polished, it’s hard to accept that it’s a brand new app from a company that didn’t do social before. There’s very little buggy behavior, videos are loaded up quick, there’s even DMs! I’m thoroughly impressed and am immersing myself in the SORA sphere. Please give me a follow there and feel free to use my Cameo by tagging [@altryne](https://sora.chatgpt.com/profile/altryne) in there. I love seeing how folks have used my Cameo, it makes me laugh 😂 

The copyright question is.. wild

Remember last year when I asked Sam why Advanced Voice Mode couldn’t sing Happy Birthday? He said they didn’t have classifiers to detect IP violations. Well, apparently that’s not a concern anymore because SORA 2 will happily generate perfect South Park episodes, Rick and Morty scenes, and Pokemon battles. They’re not even pretending they didn’t train on this stuff. You can even generate videos with any dead famous person (I’ve had zoom meetings with Michael Jackson and 2Pac, JFK and Mister Rogers) 

Our friend Ryan Carson already used it to create a YouTube short ad for his startup in two minutes. What would have cost $100K and three months now takes six generations and you’re done. This is the real game-changer for businesses.

Getting invited

EDIT: If you’re reading this on Friday, try the code `FRIYAY` and let me know in comments if it worked for you 🙏

I wish I would have invites for all of you, but all invited users have 4 other folks they can invite, so we shared a bunch of invites during the live show, and asked folks to come back and invite other listeners, this went on for half an hour so I bet we’ve got quite a few of you in! If you’re still looking for an invite, you can visit the [thread on X](thursdai.news/sora) and see who claimed and invite and ask them for one, tell them you’re also a ThursdAI listener, they hopefully will return the favor! 

Alternatively, OpenAI employees often post codes with a huge invite ratio, so follow [@GabrielPeterss4](https://x.com/GabrielPeterss4) who often posts codes and you can get in there fairly quick, and if you’re not in the US, I heard a VPN works well. Just don’t forget to follow me on there as well 😉

A Week with OpenAI Pulse: The Real Agentic Future is Here

Listen to me, this may be a hot take. I think OpenAI Pulse is a bigger news story than Sora. I’ve told you about Pulse last week, but today on the show I was able to share my weeks worth of experience, and honestly, it’s now the first thing I look at when I wake up in the morning after brushing my teeth! 

While Sora is changing media, Pulse is changing how we interact with AI on a fundamental level. Released to Pro subscribers for now, Pulse is an agentic, personalized feed that works for you behind the scenes. Every morning, it delivers a briefing based on your interests, your past conversations, your calendar—everything. It’s the first asynchronous AI agent I’ve used that feels truly proactive.

You don’t have to trigger it. It just works. It knew I had a flight to Atlanta and gave me tips. I told it I was interested in Halloween ideas for my kids, and now it’s feeding me suggestions. Most impressively, this week it surfaced a new open-source video model, Kandinsky 5.0, that I hadn’t seen anywhere on X or my usual news feeds. An agent found something new and relevant for my show, without me even asking.

This is it. This is the life-changing-level of helpfulness we’ve all been waiting for from AI. Personalized, proactive agents are the future, and Pulse is the first taste of it that feels real. I cannot wait for my next Pulse every morning.

**This Week’s Buzz: The AI Build-Out is NOT a Bubble**

This show is powered by Weights & Biases from CoreWeave, and this week that’s more relevant than ever. I just got back from a company-wide offsite where we got a glimpse into the future of AI infrastructure, and folks, the scale is mind-boggling.

CoreWeave, our parent company, is one of the key players providing the GPU infrastructure that powers companies like OpenAI and Meta. And the commitments being made are astronomical. In the past few months, CoreWeave has locked in a **$22.4B deal with OpenAI**, a **$14.2B pact with Meta**, and a **$6.3B “backstop” guarantee with NVIDIA** that runs through 2032.

If you hear anyone talking about an “AI bubble,” show them these numbers. These are multi-year, multi-billion dollar commitments to build the foundational compute layer for the next decade of AI. The demand is real, and it’s accelerating. And the best part? As a Weights & Biases user, you have access to this same best-in-class infrastructure that runs OpenAI through our inference services. Try [wandb.me/inference](wandb.me/inference)**, **and let me know if you need a bit of a credit boost! 

Claude Sonnet 4.5: The New Coding King Has a Few Quirks

On any other week, Anthropic’s release of **Claude Sonnet 4.5 **would’ve been the headline news. They’re positioning it as the new best model for coding and complex agents, and the benchmarks are seriously impressive. It matches or beats their previous top-tier model, Opus 4.1, on many difficult evals, all while keeping the same affordable price as the previous Sonnet.

One of the most significant jumps is on the OS World benchmark, which tests an agent’s ability to use a computer—opening files, manipulating windows, and interacting with applications. Sonnet 4.5 scored a whopping 61.4%, a massive leap from Opus 4.1’s 44%. This clearly signals that Anthropic is doubling down on building agents that can act as real digital assistants.

However, the real-world experience has been a bit of a mixed bag. My co-host Ryan Carson, whose company Amp switched over to 4.5 right away, noted some regressions and strange errors, saying they’re even considering switching back to the previous version until the rough edges are smoothed out. Nisten also found it could be more susceptible to “slop catalysts” in prompting. It seems that while it’s incredibly powerful, it might require some re-prompting and adjustments to get the best, most stable results. The jury’s still out, but it’s a potent new tool in the developer’s arsenal.

Open Source LLMs: DeepSeek’s Attention Revolution

Despite the massive news from the big companies, open source still brought the heat this week, with one release in particular representing a fundamental breakthrough.

DeepSeek released **V3.2 Experimental**, and the big news is DSA, or DeepSeek Sparse Attention. For those who don’t know, one of the biggest bottlenecks in LLMs is the “quadratic attention problem”—as you double the context length, the computation and memory required quadruple. This makes very long contexts incredibly expensive. DeepSeek’s new architecture makes the cost curve nearly flat, allowing for massive context at a fraction of the cost, all while maintaining the same SOTA performance as their previous model.

This is one of those “unhobbling moments,” like the invention of RoPE or GRPO, that moves the entire field forward. Everyone will be able to implement this, making all open-source models faster and more efficient. It’s a huge deal.

We also saw major releases from [Z.ai](Z.ai) with **GLM-4.6**, an advanced agentic model with a 200K context window that’s getting incredibly close to Claude’s performance, and a surprise from **ServiceNow SLAM Labs**, who dropped **Apriel-1.5-15B**, a frontier-level multimodal model that’s fully open source. It’s amazing to see a huge enterprise company contributing to the open-source ecosystem at this level.

Multimodal Madness: Audio, Video, and Image Models updates

The torrent of releases continued across all modalities this week, a bit overshadowed by SORA but definitely still happened (all links in the TL;DR section)

In voice and audio, our friends at **Hume AI launched Octave 2**, their next-gen text-to-speech model that’s faster, cheaper, and now fluent in over 11 languages. We also saw **LFM2-Audio from Liquid AI**, an incredibly efficient 1.5B parameter end-to-end audio model with sub-100ms latency.

In video, the open-source community answered Sora 2 with **Kandinsky 5.0**, a new 2B parameter text-to-video model that is claiming the #1 spot in open source and looks incredibly promising. And as I mentioned on the show, I wouldn’t have even known about it if it weren’t for my new personal AI agent, Pulse!

Finally, in AI art, Tencent dropped a monster: **HunyuanImage 3.0**, a massive 80-billion-parameter open-source text-to-image model. The scale of these open-source releases is just breathtaking.

Agentic browsing for all is here

Just as I was wrapping up the show, Perplexity has decided to let everyone in to use their Comet Agentic browser. I strongly recommend it, as I switched to it lately and it’s great! 

I’m using it right now to run some agents, it can click stuff, scroll through stuff, collect info across tabs, it’s really great. Give it a spin, really, it’s worth getting into the habit of agentic browsing! 

Many of you were asking me for invites before, well, it’s free access now, [download it here](https://comet.perplexity.ai/) (not sponsored, I just really like it) 

Phew, ok, this was a WILD week, and I’m itching to get back to creating and seeing all the folks who used my Cameo on SORA, which you can see too btw if you hit the Cameo button here ([https://sora.chatgpt.com/profile/altryne](https://sora.chatgpt.com/profile/altryne)) 

Next week is OpenAI’s Dev Day, and for the third year in a row we’re going to cover it, so follow us on social media and tune in Monday 8:30am Pacific. We’ll be live streaming from the location and re-streaming the keynote with Sam so don’t miss it! 

TL;DR and Show Notes

**Hosts and Guests**:

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@yampeleg](x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed) [@ryancarson](https://x.com/ryancarson/status/1957809743679906246)

**Big CO LLMs + APIs**:

* OpenAI releases SORA2 + a new social media app ([X](https://x.com/altryne/status/1973568567489798144), [Blog](https://openai.com/index/sora-2/), [App download](https://apps.apple.com/us/app/sora-by-openai/id6744034028))

* Anthropic releases Claude Sonnet 4.5 - same price as 4.1 - leading coding model ([X](https://x.com/claudeai/status/1972706807345725773))

* OpenAI launches Instant Checkout & Agentic Commerce Protocol ([X](https://x.com), [Protocol](https://agenticcommerce.dev))

**Open Source LLMs**:

* DeepSeek V3.2 Exp: Sparse Attention, Cost Drop ([X](https://x.com/deepseek_ai/status/1972604768309871061), [Evals](https://twitter.com/ArtificialAnlys/status/1973230103854456993), [HF](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp))

* Apriel-1.5-15B-Thinker by ServiceNow SLAM Labs ([X](https://twitter.com/ServiceNowRSRCH/status/1973100536280027586), [HF](https://huggingface.co/ServiceNow-AI/Apriel-1.5-15b-Thinker), [Arxiv](https://arxiv.org/abs/2508.10948))

* [Z.ai](Z.ai) GLM-4.6: advanced Agentic flagship model ([X](https://x.com/Zai_org/status/1973034639708344767), [Blog](https://z.ai/blog/glm-4.6), [HF](https://huggingface.co/zai-org/GLM-4.6))

**This weeks Buzz**:

* CoreWeave locks **$22.4B OpenAI**, a **$6.3B NVIDIA “backstop”**, and a **$14.2B Meta** compute pact ([X](https://x.com/CoreWeave/status/1971218329713938942))

**Voice & Audio**:

* Hume AI launches Octave 2 ([X](https://twitter.com/hume_ai/status/1973450822840152455), [Blog](https://hume.ai/blog/octave2))

* LFM2-Audio: End-to-end audio foundation model ([X](https://x.com/LiquidAI_/status/1973372092230836405), [Blog](https://www.liquid.ai/blog/lfm2-audio-an-end-to-end-audio-foundation-model), [HF](https://huggingface.co/LiquidAI/LFM2-Audio-1.5B))

**Vision & Video**:

* Kandinsky 5.0 T2V Lite: #1 open-source text-to-video ([Blog](https://ai-forever.github.io/Kandinsky-5/), [GitHub](https://github.com/ai-forever/Kandinsky-5), [HF](https://huggingface.co/collections/ai-forever/kandinsky-50-t2v-lite-68d71892d2cc9b02177e5ae5), [Try It](https://t.me/kandinsky_access_bot))

**AI Art & Diffusion & 3D**:

* HunyuanImage 3.0: 80B Open-Source Text-to-Image by Tencent ([X](https://twitter.com/TencentHunyuan/status/1972130405160833334), [HF](https://huggingface.co/tencent/HunyuanImage-3.0), [Github](https://github.com/Tencent-Hunyuan)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-oct-2-sora-2-the-new-tiktok/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-oct-2-sora-2-the-new-tiktok?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3NTE1MjM4NiwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.vb191_pQaKspBYaenugvHkeIzsAbojabAkiwtBknBXU&utm_campaign=CTA_5).

---

