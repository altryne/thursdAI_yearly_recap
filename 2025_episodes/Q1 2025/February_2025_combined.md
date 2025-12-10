# ThursdAI Episodes - February 2025

Total Episodes: 4

---

## 📆 Feb 27, 2025 - GPT-4.5 Drops TODAY?!, Claude 3.7 Coding BEAST, Grok's Unhinged Voice, Humanlike AI voices & more AI news

**Date:** February 28, 2025  
**Duration:** 1:40:30  
**Link:** [https://sub.thursdai.news/p/feb-27-2025-gpt-45-drops-today-claude](https://sub.thursdai.news/p/feb-27-2025-gpt-45-drops-today-claude)

Hey all, Alex here 👋

What can I say, the weeks are getting busier , and this is one of those "crazy full" weeks in AI. As we were about to start recording, OpenAI teased GPT 4.5 live stream, and we already had a very busy show lined up (Claude 3.7 vibes are immaculate, Grok got an unhinged voice mode) and I had an interview with Kevin Hou from Windsurf scheduled!  Let's dive in! 

🔥 GPT 4.5 (ORION) is here - worlds largest LLM (10x GPT4o) 

OpenAI has finally shipped their next .5 model, which is 10x scale from the previous model. We didn't cover this on the podcast but did watch the OpenAI live stream together after the podcast concluded. 

A very interesting .5 release from OpenAI, where even Sam Altman says "this model won't crush on benchmarks" and is not the most frontier model, but is OpenAI's LARGEST model by far (folks are speculating 10+ Trillions of parameters) 

After 2 years of smaller models and distillations, we finally got a new BIG model, that shows scaling laws proper, and while on some benchmarks it won't compete against reasoning models, this model will absolutely fuel a huge increase in capabilities even for reasoners, once o-series models will be trained on top of this. 

Here's a summary of the announcement and quick vibes recap (from folks who had access to it before) 

* OpenAI's largest, most knowledgeable model.

* Increased world knowledge: 62.5% on SimpleQA, 71.4% GPQA

* Better in creative writing, programming, problem-solving (no native step-by-step reasoning).

* Text and image input and text output

* Available in ChatGPT Pro and API access (API supports Function Calling, Structured Output)

* Knowledge Cutoff is October 2023.

* Context Window is 128,000 tokens.

* Max Output is 16,384 tokens.

* Pricing (per 1M tokens): Input: $75, Output: $150, Cached Input: $37.50.

* Foundation for future reasoning models

4.5 Vibes Recap

Tons of folks who had access are pointing to the same thing, while this model is not beating others on evals, it's much better at multiple other things, namely [creative writing](https://x.com/theo/status/1895206943293350123), [recommending songs](https://x.com/willdepue/status/1895205469645611038), improved [vision capability](https://x.com/emollick/status/1895211249656570258) and improved [medical diagnosis](https://x.com/DeryaTR_/status/1895249875723321560). 

Karpathy said "Everything is a little bit better and it's awesome, but also not exactly in ways that are trivial to point to" and posted a thread of pairwise comparisons of tone on his [X thread](https://x.com/karpathy/status/1895213020982472863)

Though the reaction is bifurcated as many are upset with the high price of this model (10x more costly on outputs) and the fact that it's just marginally better at coding tasks. Compared to the newerSonnet (Sonnet 3.7) and DeepSeek, folks are looking at OpenAI and asking, why isn't this way better? 

Anthropic's Claude 3.7 Sonnet: A Coding Powerhouse

Anthropic released Claude 3.7 Sonnet, and the immediate reaction from the community was overwhelmingly positive. With 8x more output capability (64K) and reasoning built in, this model is an absolute coding powerhouse. 

Claude 3.7 Sonnet is the new king of coding models, achieving a remarkable 70% on the challenging SWE-Bench benchmark, and the initial user feedback is stellar, though vibes started to shift a bit towards Thursday.

Ranking #1 on WebDev arena, and seemingly trained on UX and websites, Claude Sonnet 3.7 (AKA NewerSonner) has been blowing our collective minds since it was released on Monday, especially due to introducing Thinking and reasoning in a combined model. 

Now, since the start of the week, the community actually had time to play with it, and some of them return to sonnet 3.5 and saying that while the model is generally much more capable, it tends to generate tons of things that are unnecessary. 

I wonder if the shift is due to Cursor/Windsurf specific prompts, or the model's larger output context, and we'll keep you updated on if the vibes shift again. 

Open Source LLMs

This week was HUGE for open source, folks. We saw releases pushing the boundaries of speed, multimodality, and even the very way LLMs generate text!

DeepSeek's Open Source Spree

DeepSeek went on an absolute tear, open-sourcing a treasure trove of advanced tools and techniques:

This isn't your average open-source dump, folks. We're talking FlashMLA (efficient decoding on Hopper GPUs), DeepEP (an optimized communication library for MoE models), DeepGEMM (an FP8 GEMM library that's apparently ridiculously fast), and even parallelism strategies like DualPipe and EPLB.

They are releasing some advanced stuff for training and optimization of LLMs, you can follow all their releases on their [X account](https://x.com/deepseek_ai/status/1894931931554558199)

Dual Pipe seems to be the one that got most attention from the community, which is an incredible feat in pipe parallelism, that even got the cofounder of HuggingFace [super excited](https://x.com/Thom_Wolf/status/1895135100444053599)

Microsoft's Phi-4: Multimodal and Mini ([Blog](https://azure.microsoft.com/en-us/blog/empowering-innovation-the-next-generation-of-the-phi-family/), [HuggingFace](https://huggingface.co/microsoft/Phi-4-multimodal-instruct))

Microsoft joined the party with Phi-4-multimodal (5.6B parameters) and Phi-4-mini (3.8B parameters), showing that small models can pack a serious punch.

These models are a big deal. Phi-4-multimodal can process text, images, *and* audio, and it actually *beats* WhisperV3 on transcription! As Nisten said, "This is a new model and, I'm still reserving judgment until, until I tried it, but it looks ideal for, for a portable size that you can run on the phone and it's multimodal." It even supports a wide range of languages. Phi-4-mini, on the other hand, is all about speed and efficiency, perfect for finetuning.

Diffusion LLMs: Mercury Coder and LLaDA ([X](https://twitter.com/InceptionAILabs/status/1894847919624462794) , [Try it](https://t.co/XCeNw9BtsX))

This is where things get *really* interesting. We saw not one, but *two* diffusion-based LLMs this week: Mercury Coder from Inception Labs and LLaDA 8B. (Although, ok, to be fair, LLaDa released 2 weeks ago I was just busy)

For those who don't know, diffusion is usually used for creating things like images. The idea of using it to generate text is like saying, "Okay, there's a revolutionary tool for painting; I'll write the code using it." Inception Labs' Mercury Coder is claiming over *1000 tokens per second* on NVIDIA H100s – that's insane speed, usually only seen with specialized chips! Nisten spent hours digging into these, noting, "This is a complete breakthrough and, it just hasn't quite hit yet that this just happened because people thought for a while it should be possible because then you can do, you can do multiple token prediction at once". He explained that these models combine a regular LLM with a diffusion component, allowing them to generate multiple tokens simultaneously and excel at tasks like "fill in the middle" coding.

LLaDA 8B, on the other hand, is an open-source attempt, and while it needs more training, it shows the potential of this approach. LDJ pointed out that LLaDA is "trained on like around five times or seven times less data while already like competing with LLAMA3 AP with same parameter count".

Are diffusion LLMs the future? It's too early to say, but the speed gains are *very* intriguing.

Magma 8B: Robotics LLM from Microsoft

Microsoft dropped Magma 8B, a Microsoft Research project, an open-source model that combines vision and language understanding with the ability to control robotic actions.

Nisten was particularly hyped about this one, calling it "the robotics. LLM." He sees it as a potential game-changer for robotics companies, allowing them to build robots that can understand visual input, respond to language commands, and *act* in the real world.

OpenAI's Deep Research for Everyone (Well, Plus Subscribers)

OpenAI finally brought Deep Research, its incredible web-browsing and research tool, to Plus subscribers.

I've been saying this for a while: Deep Research is another ChatGPT moment. It's *that* good. It goes out, visits websites, understands your query in context, and synthesizes information like nothing else. As Nisten put it, "Nothing comes close to OpenAI's Deep Research...People like pull actual economics data, pull actual stuff." If you haven't tried it, you absolutely should.

Our full coverage of Deep Research is [here](https://sub.thursdai.news/p/thursdai-feb-6-openai-deepresearch) if you haven't yet listened, it's incredible. 

Alexa Gets an AI Brain Upgrade with Alexa+

Amazon finally announced Alexa+, the long-awaited LLM-powered upgrade to its ubiquitous voice assistant.

Alexa+ will be powered by Claude (and sometimes Nova), offering a much more conversational and intelligent experience, with integrations across Amazon services.

This is a *huge* deal. For years, Alexa has felt… well, dumb, compared to the advancements in LLMs. Now, it's getting a serious intelligence boost, thanks to Anthropic's Claude. It'll be able to handle complex conversations, control smart home devices, and even perform tasks across various Amazon services. Imagine asking Alexa, "Did I let the dog out today?" and it actually *checking your Ring camera footage* to give you an answer! (Although, as I joked, let's hope it doesn't start setting houses on fire.)

Also very intriguing is the new SDKs they are releasing to connect Alexa+ to all kinds of experience, I think this is huge and will absolutely create a new industry of applications built for voice Alexa. 

Alexa Web Actions for example will allow Alexa to navigate to a website and complete actions (think order Uber Eats) 

The price? 20$/mo but free if you're a Amazon Prime subscriber, which is most of the US households at this point. 

They are focusing on personalization and memory, though still unclear how that's going to be handled, and the ability to share documents like schedules 

I'm very much looking forward to smart Alexa, and to be able to say "Alexa, set a timer for the amount of time it takes to hard boil an egg, and flash my house lights when the timer is done" 

Grok Gets a Voice... and It's UNHINGED

Grok, Elon Musk's AI, finally got a voice mode, and… well, it's something else.

One-sentence summary: Grok's new voice mode includes an "unhinged" 18+ option that curses like a sailor, along with other personality settings.

Yes, you read that right. There's literally an "unhinged" setting in the UI. We played it live on the show, and... well, let's just say it's not for the faint of heart (or for kids). Here's a taste:

**Alex:** "Hey there."

**Grok:** "Yo, Alex. What's good, you horny bastard? How's your day been so far? Fucked up or just mildly shitty?"

Beyond the shock value, the voice mode is actually quite impressive in its expressiveness and ability to understand interruptions. It has several personalities, from a helpful "Grok Doc" to an "argumentative" mode that will disagree with everything you say. It's... unique.

This Week's Buzz (WandB-Related News)

Agents Course is Coming!

We announced our upcoming agents course! You can pre-sign up [HERE](https://wandb.me/agents) . This is going to be a deep dive into building and deploying AI agents, so don't miss it!

AI Engineer Summit Recap

We briefly touched on the AI Engineer Summit in New York, where we met with Kevin Hou and many other brilliant minds in the AI space. The theme was "Agents at Work," and it was a fantastic opportunity to see the latest developments in agent technology. I gave a talk about reasoning agents and had a workshop about evaluations on Saturday, and saw many listeners of ThursdAI 👏 ✋ 

Interview with Kevin Hou from Windsurf

This week we had the pleasure of chatting with **Kevin Hou from Windsurf** about their revolutionary AI editor. Windsurf isn't just another IDE, it's an **agentic IDE**. As Kevin explained, "we made the pretty bold decision of saying, all right, we're not going to do chat... we are just going to [do] agent." They've built Windsurf from the ground up with an agent-first approach, and it’s making waves.

Kevin walked us through the evolution of AI coding tools, from autocomplete to chat, and now to agents. He highlighted the "magical experiences" users are having, like debugging complex code with AI assistance that *actually understands* the context. We also delved into the challenges – memory, checkpointing, and cost.

We also talked about the burning question: **vibe coding**. Is coding as we know it dead? Kevin’s take was nuanced: "there's an in between state that I really vibe or like gel with, which is,the scaffolding of what you want… Let's use, let's like vibe code and purely use the agent to accomplish this sort of commit." He sees AI agents raising the bar for software quality, demanding better UX, testing, and overall polish.

And of course, we had to ask about the elephant in the room – **why are so many people switching from Cursor to Windsurf?** Kevin's answer was humble, pointing to user experience, the agent-first workflow, and the team’s dedication to building the best product. Check out our full conversation on the pod and download Windsurf for yourself: [**windsurf.ai**](windsurf.ai)

Video Models & Voice model updates 

There is so much happening in LLM world, that folks may skip over the other stuff, but there's so much happening in these world's as well this week! Here's a brief recap! 

* **Alibaba's WanX:** Open-sourced, cutting-edge video generation models making waves with over 250,000 downloads already. They claim to take SOTA on open source video generation evals and of course img2video of this high quality model will lead to ... folks using it for all kinds of things. 

* **HUMEs Octave:** A groundbreaking LLM model that genuinely understands context and emotion and does TTS. [Blog](https://www.hume.ai/blog/octave-the-first-text-to-speech-model-that-understands-what-its-saying)  Hume has been doing emotional TTS but with this TTS focused LLM we are now able to create voices with a prompt, and receive emotional responses that are inferred from the text. Think shyness, sarcasm, anger etc

* **11labs’ Scribe:** Beating Whisper 3 with impressive accuracy and diarization features, Scribe is raising the bar in speech-to-text quality. 11labs releasing their own ASR (automatic speech recognition) was not in my cards, and boy did they deliver. Beating whisper, with speaker separation (diarization), world level timestamps and much lower WER than other models, this is a very interesting entry to this space. However, free for now on their website, it's significantly slower than Gemini 2.0 and Whisper for me at least. 

* **Sesame** releases their conversational speech model (and promising to open source this) and it's honestly the best / least uncanny conversations I had with an AI. Check out my conversation with it 

* Lastly, VEO 2, the best video model around according to some, is finally available via API (though txt2video only) and it's fairly expensive, but gives some amazing results. You can try it out on [FAL](https://fal.ai/models/fal-ai/veo2)

Phew, it looks like we've made it! Huge huge week in AI, big 2 new models, tons of incredible updates on multimodality and voice as well 🔥

If you enjoyed this summary, the best way to support us is to share with a friend (or 3) and give us a 5 start reviews on wherever you get your podcasts, it really does help! 👏 

See you next week, 

Alex 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/feb-27-2025-gpt-45-drops-today-claude/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/feb-27-2025-gpt-45-drops-today-claude?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1ODA3NDkwOCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.mIjhoqaqv8Z7n3Uu0dpHU5w4jrMJ8oDyfaPRjtxMmQ4&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Feb 20 - Live from AI Eng in NY - Grok 3, Unified Reasoners, Anthropic's Bombshell, and Robot Handoffs!

**Date:** February 20, 2025  
**Duration:** 1:41:13  
**Link:** [https://sub.thursdai.news/p/thursdai-feb-20-live-from-ai-eng](https://sub.thursdai.news/p/thursdai-feb-20-live-from-ai-eng)

Holy moly, AI enthusiasts! Alex Volkov here, reporting live from the AI Engineer Summit in the heart of (touristy) Times Square, New York! This week has been an absolute whirlwind of announcements, from **XAI's Grok 3 dropping like a bomb**, to Figure robots learning to *hand each other things*, and even a little eval smack-talk between OpenAI and XAI. It’s enough to make your head spin – but that's what ThursdAI is here for. We sift through the chaos and bring you the need-to-know, so you can stay on the cutting edge without having to, well, spend your entire life glued to X and Reddit.

This week we had a very special live show with the Haize Labs folks, the ones I previously interviewed about their bijection attacks, discussing their open source judge evaluation library called Verdict. So grab your favorite caffeinated beverage, maybe do some stretches because your mind *will* be blown, and let's dive into the TL;DR of ThursdAI, February 20th, 2025!

Participants

* **Alex Volkov:** AI Evangelist with Weights and Biases

* **Nisten: **AI Engineer and cohost

* **Akshay:** AI Community Member

* **Nuo:** Dev Advocate at 01AI

* **Nimit:** Member of Technical Staff at Haize Labs

* **Leonard:** Co-founder at Haize Labs

Open Source LLMs

Perplexity's R1 7076: Censorship-Free DeepSeek

Perplexity made a bold move this week, releasing **R1 7076**, a fine-tuned version of DeepSeek R1 specifically designed to remove what they (and many others) perceive as Chinese government censorship. The name itself, 1776, is a nod to American independence – a pretty clear statement! The core idea? Give users access to information on topics the CCP typically restricts, like Tiananmen Square and Taiwanese independence.

Perplexity used human experts to identify around 300 sensitive topics and built a "censorship classifier" to train the bias *out* of the model. The impressive part? They claim to have done this *without* significantly impacting the model's performance on standard evals. As Nuo from 01AI pointed out on the show, though, he'd "actually prefer that they can actually disclose more of their details in terms of post training... Running the R1 model by itself, it's already very difficult and very expensive." He raises a good point – more transparency is always welcome! Still, it's a fascinating attempt to tackle a tricky problem, the problem which I always say we simply cannot avoid. You can check it out yourself on [Hugging Face](https://huggingface.co/perplexity-ai/r1-1776) and read their [blog post](https://www.perplexity.ai/hub/blog/open-sourcing-r1-1776).

Arc Institute & NVIDIA Unveil Evo 2: Genomics Powerhouse

Get ready for some serious science, folks! Arc Institute and NVIDIA dropped **Evo 2**, a *massive* genomics model (40 billion parameters!) trained on a mind-boggling 9.3 *trillion* nucleotides. And it’s fully open – two papers, weights, data, training, *and* inference codebases. We love to see it!

Evo 2 uses the StripedHyena architecture to process *huge* genetic sequences (up to 1 million nucleotides!), allowing for analysis of complex genomic patterns. The practical applications? Predicting the effects of genetic mutations (super important for healthcare) and even designing entire genomes. I’ve been super excited about genomics models, and seeing these alternative architectures like StripedHyena getting used here is just icing on the cake. [Check it out on X](https://x.com/pdhsu/status/1892243493445050606).

ZeroBench: The "Impossible" Benchmark for VLLMs

Need more benchmarks? Always! A new benchmark called **ZeroBench** arrived, claiming to be the "impossible benchmark" for Vision Language Models (VLLMs). And guess what? All current top-of-the-line VLLMs get a big fat *zero* on it.

One example they gave was a bunch of scattered letters, asking the model to "answer the question that is written in the shape of the star among the mess of letters." Honestly, even *I* struggled to see the star they were talking about. It highlights just how much further VLLMs need to go in terms of true visual understanding. ([X](https://x.com/JRobertsAI/status/1891506671056261413), [Page](https://t.co/E4noN7yDDM), [Paper](https://t.co/n5GAwFiGEV), [HF](https://t.co/mD8Eptr9M5))

Hugging Face's Ultra Scale Playbook: Scaling Up

For those of you building *massive* models, Hugging Face released the **Ultra Scale Playbook**, a guide to building and scaling AI models on huge GPU clusters.

They ran 4,000 scaling experiments on up to 512 GPUs (nothing close to Grok's 100,000, but still impressive!). If you're working in a lab and dreaming big, this is definitely a resource to check out. ([HF](https://huggingface.co/spaces/nanotron/ultrascale-playbook)).

Big CO LLMs + APIs

Grok 3: XAI's Big Swing new SOTA LLM! (and Maybe a Bug?)

Monday evening, BOOM! While some of us were enjoying President's Day, the XAI team dropped **Grok 3**. They announced it with a setting very similar to OpenAI announcements. They're claiming state-of-the-art performance on *some* benchmarks (more on that drama later!), and a whopping 1 million token context window, finally confirmed after some initial confusion. They talked a lot about agents and a future of reasoners as well.

The launch was a bit… messy. First, there was a bug where some users were getting Grok 2 *even when the dropdown said Grok 3*. That led to a lot of mixed reviews. Even when I finally *thought* I was using Grok 3, it still flubbed my go-to logic test, the "Beth's Ice Cubes" question. (The answer is zero, folks – ice cubes melt!). But Akshay, who joined us on the show, chimed in with some love: "...with just the base model of Grok 3, it's, in my opinion, it's the best coding model out there." So, mixed vibes, to say the least! It's also FREE for now, "until their GPUs melt," according to XAI, which is great.

**UPDATE:** The vibes are shifting, more and more of my colleagues and mutuals are LOVING grok3 for one shot coding, for talking to it. I’m getting convinced as well, though I did use and will continue to use Grok for real time data and access to X. 

**DeepSearch**

In an attempt to show off some Agentic features, XAI also launched a deep search (not research like OpenAI but effectively the same) 

Now, XAI of course has access to X, which makes their deep search have a leg up, specifically for real time information! I found out it can even “use” the X search! 

OpenAI's Open Source Tease

In what felt like a very *conveniently* timed move, Sam Altman dropped a poll on X the same day as the Grok announcement: if OpenAI were to open-source something, should it be a small, mobile-optimized model, or a model on par with o3-mini? Most of us chose o3 mini, just to have access to that model and play with it. No indication of *when* this might happen, but it’s a clear signal that OpenAI is feeling the pressure from the open-source community.

The Eval Wars: OpenAI vs. XAI

Things got spicy! There was a whole debate about the eval numbers XAI posted, specifically the "best of N" scores (like best of 64 runs). Boris from OpenAI, and Aiden mcLau called out some of the graphs. Folks on X were quick to point out that OpenAI *also* used "best of N" in the past, and the discussion devolved from there.

XAI is claiming SOTA. OpenAI (or some folks from within OpenAI) aren't so sure. The core issue? We can't *independently* verify Grok's performance because there's no API yet! As I said, "…we're not actually able to use this model to independently evaluate this model and to tell you guys whether or not they actually told us the truth." Transparency matters, folks!

DeepSearch - How Deep?

Grok also touted a new "Deep Search" feature, kind of like Perplexity or OpenAI's "Deep Research" in their more expensive plan. My initial tests were… underwhelming. I nicknamed it "Shallow Search" because it spent all of 34 seconds on a complex query where OpenAI's Deep Research took 11 minutes and cited 17 sources. We're going to need to do some more digging (pun intended) on this one.

This Week's Buzz

We’re leaning *hard* into agents at Weights & Biases! We just released an agents [whitepaper](https://wandb.ai/site/resources/whitepapers/evaluating-ai-agent-applications?utm_source=twitter&utm_medium=social&utm_campaign=weave) (check it out on our socials!), and we're launching an **agents course** in collaboration with OpenAI's Ilan Biggio. Sign up at [wandb.me/agents](http://wandb.me/agents)! We're hearing *so much* about agent evaluation and observability, and we're working hard to provide the tools the community needs.

Also, sadly, our **Toronto workshops** are completely **sold out**. But if you're at AI Engineer in New York, come say hi to our booth! And catch my talk on LLM Reasoner Judges tomorrow (Friday) at 11 am EST – it’ll be live on the AI Engineer YouTube channel ([HERE](https://www.youtube.com/live/L89GzWEILkM))!

Vision & Video

Microsoft MUSE: Playable Worlds from a Single Image

This one is *wild*. Microsoft's **MUSE** can generate *minutes* of playable gameplay from just a *single second* of video frames and controller actions.

It's based on the World and Human Action Model (WHAM) architecture, trained on a *billion* gameplay images from Xbox. So if you’ve been playing Xbox lately, you might be in the model! I found it particularly cool: "…you give it like a single second of a gameplay of any type of game with all the screen elements, with percentages, with health bars, with all of these things and their model generates a game that you can control." ([X](https://x.com/rowancheung/status/1892243245192683875), [HF](https://huggingface.co/microsoft/wham), Blog).

StepFun's Step-Video-T2V: State-of-the-Art (and Open Source!)

We got *two* awesome open-source video breakthroughs this week. First, **StepFun's Step-Video-T2V** (and T2V Turbo), a 30 *billion* parameter text-to-video model. The results look *really* good, especially the text integration. Imagine a Chinese girl opening a scroll, and the words "We will open source" appearing as she unfurls it. That’s the kind of detail we're talking about.

And it’s MIT licensed! As Nisten noted "This is pretty cool. It came out. Right before Sora came out, people would have lost their minds." ([X](https://x.com/arankomatsuzaki/status/1891330624436220069), [Paper](https://arxiv.org/abs/2502.10248), [HF](https://huggingface.co/stepfun-ai/stepvideo-t2v), [Try It](https://yuewen.cn/videos)).

HAO AI's FastVideo: Speeding Up HY-Video

The second video highlight: HAO AI released **FastVideo**, a way to make HY-Video (already a strong open-source contender) *three times faster* with no additional training! They call the trick "Sliding Tile Attention" apparently that alone provides enormous boost compared to even flash attention.

This is huge because faster inference means these models become more practical for real-world use. And, bonus: it supports HY-Video's Loras, meaning you can fine-tune it for, ahem, *all kinds* of creative applications. I will not go as far as to mention civit ai. ([Github](https://github.com/hao-ai-lab/FastVideo))

Figure's Helix: Robot Collaboration!

Breaking news from the AI Engineer conference floor: **Figure**, the humanoid robot company, announced **Helix**, a Vision-Language-Action (VLA) model built *into* their robots!It has full upper body control!

What blew my mind: they showed *two* robots working together, handing objects to each other, based on natural language commands! As I watched, I exclaimed, "I haven't seen a humanoid robot, hand off stuff to the other one... I found it like super futuristically cool." The model runs *on the robot*, using a 7 billion parameter VLM for understanding and an 80 million parameter transformer for control. This is the future, folks!

Tools & Others

Microsoft's New Quantum Chip (and State of Matter!)

Microsoft announced a new **quantum chip** *and* a new state of matter (called "topological superconductivity"). "I found it like absolutely mind blowing that they announced something like this," I gushed on the show. While I'm no quantum physicist, this sounds like a *big* deal for the future of computing.

Verdict: Hayes Labs' Framework for LLM Judges

And of course, the highlight of our show: **Verdict**, a new open-source framework from Hayes Labs (the folks behind those "bijection" jailbreaks!) for composing LLM judges. This is a *huge* deal for anyone working on evaluation. Leonard and Nimit from Hayes Labs joined us to explain how Verdict addresses some of the core problems with LLM-as-a-judge: biases (like preferring their own responses!), sensitivity to prompts, and the challenge of "meta-evaluation" (how do you know your judge is actually good?).

Verdict lets you combine different judging techniques ("primitives") to create more robust and efficient evaluators. Think of it as "judge-time compute scaling," as Leonard called it. They're achieving near state-of-the-art results on benchmarks like ExpertQA, *and* it's designed to be fast enough to use as a guardrail in real-time applications!

One key insight: you don't always need a full-blown reasoning model for judging. As Nimit explained, Verdict can combine simpler LLM calls to achieve similar results at a fraction of the cost. And, it's open source! ([Paper](https://verdict.haizelabs.com/whitepaper.pdf), [Github](http://github.com/haizelabs/verdict),[X](https://x.com/leonardtang_/thread/1892243653071908949)).

Conclusion

Another week, another explosion of AI breakthroughs! Here are my key takeaways:

* **Open Source is THRIVING:** From censorship-free LLMs to cutting-edge video models, the open-source community is delivering incredible innovation.

* **The Need for Speed (and Efficiency):** Whether it's faster video generation or more efficient LLM judging, performance is key.

* **Robots are Getting Smarter (and More Collaborative):** Figure's Helix is a glimpse into a future where robots work *together*.

* **Evaluation is (Finally) Getting Attention:** Tools like Verdict are essential for building reliable and trustworthy AI systems.

* **The Big Players are Feeling the Heat:** OpenAI's open-source tease and XAI's rapid progress show that the competition is *fierce*.

I'll be back in my usual setup next week, ready to break down all the latest AI news. Stay tuned to ThursdAI – and don't forget to give the pod five stars and subscribe to the newsletter for all the links and deeper dives. There’s potentially an Anthropic announcement coming, so we’ll see you all next week.

TLDR

* **Open Source LLMs**

* Perplexity R1 1776 - finetune of china-less R1 ([Blog](https://www.perplexity.ai/hub/blog/open-sourcing-r1-1776), [Model](https://huggingface.co/perplexity-ai/r1-1776))

* Arc institute + Nvidia - introduce EVO 2 - genomics model ([X](https://x.com/pdhsu/status/1892243493445050606))

* ZeroBench - impossible benchmark for VLMs ([X](https://x.com/JRobertsAI/status/1891506671056261413), [Page](https://t.co/E4noN7yDDM), [Paper](https://t.co/n5GAwFiGEV), [HF](https://t.co/mD8Eptr9M5))

* HuggingFace ultra scale playbook ([HF](https://huggingface.co/spaces/nanotron/ultrascale-playbook))

* **Big CO LLMs + APIs**

* Grok 3 SOTA LLM + reasoning and Deep Search ([blog](https://x.ai/blog/grok-3), [try it](http://grok.com))

* OpenAI is about to open source something? Sam posts a polls

* **This weeks Buzz**

* We are about to launch an agents course! Pre-sign up [wandb.me/agents](http://wandb.me/agents)

* Workshops are SOLD OUT

* Watch my talk LIVE from AI Engineer - 11am EST Friday ([HERE](https://www.youtube.com/live/L89GzWEILkM))

* Keep watching AI Eng conference after the show on AIE YT

* )

* **Vision & Video**

* Microsoft MUSE - playable worlds from one image ([X](https://x.com/rowancheung/status/1892243245192683875), [HF](https://huggingface.co/microsoft/wham), Blog)

* Microsoft OmniParser - Better, faster screen parsing for GUI agents with OmniParser v2 ([Gradio Demo](https://huggingface.co/spaces/microsoft/OmniParser-v2))

* HAO AI - fastVIDEO - making HY-Video 3x as fast ([Github](https://github.com/hao-ai-lab/FastVideo))

* StepFun - Step-Video-T2V (+Turbo), a SotA 30B text-to-video model ([Paper](https://arxiv.org/abs/2502.10248), [Github](https://github.com/stepfun-ai/Step-Video-T2V), [HF](https://huggingface.co/stepfun-ai/stepvideo-t2v), [Try It](https://yuewen.cn/videos))

* Figure announces HELIX - vision action model built into FIGURE Robot ([Paper](https://www.figure.ai/news/helix))

* **Tools & Others**

* Microsoft announces a new quantum chip and a new state of matter ([Blog](https://news.microsoft.com/source/features/ai/microsofts-majorana-1-chip-carves-new-path-for-quantum-computing/), [X](https://x.com/KonstantHacker/status/1892242862068183048))

* Verdict - Framework to compose SOTA LLM judges with JudgeTime Scaling ([Paper](https://verdict.haizelabs.com/whitepaper.pdf), [Github](http://github.com/haizelabs/verdict),[X](https://x.com/leonardtang_/thread/1892243653071908949)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-feb-20-live-from-ai-eng/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-feb-20-live-from-ai-eng?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1NzU2NzQ2NiwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.s9N9lgS7uZnaGQiO59PjNNwukFcGdZgz7euukFbTxC8&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Feb 13 - my Personal Rogue AI, DeepHermes, Fast R1, OpenAI Roadmap / RIP GPT6, new Claude & Grok 3 imminent?

**Date:** February 13, 2025  
**Duration:** 1:43:48  
**Link:** [https://sub.thursdai.news/p/thursdai-feb-13-my-personal-rogue](https://sub.thursdai.news/p/thursdai-feb-13-my-personal-rogue)

What a week in AI, folks! Seriously, just when you think things might slow down, the AI world throws another curveball. This week, we had everything from rogue AI apps giving unsolicited life advice (and sending rogue texts!), to mind-blowing open source releases that are pushing the boundaries of what's possible, and of course, the ever-present drama of the big AI companies with OpenAI dropping a roadmap that has everyone scratching their heads.

Buckle up, because on this week's ThursdAI, we dove deep into all of it. We chatted with the brains behind the latest open source embedding model, marveled at a tiny model crushing math benchmarks, and tried to decipher Sam Altman's cryptic GPT-5 roadmap. Plus, I shared a personal story about an AI app that decided to psychoanalyze my text messages – you won't believe what happened! Let's get into the TL;DR of ThursdAI, February 13th, 2025 – it's a wild one!

* **Alex Volkov:** AI Adventurist with weights and biases

* **Wolfram Ravenwlf:** AI Expert & Enthusiast

* **Nisten:** AI Community Member

* **Zach Nussbaum:** Machine Learning Engineer at Nomic AI

* **Vu Chan:** AI Enthusiast & Evaluator

* **LDJ:** AI Community Member

Personal story of Rogue AI with RPLY

This week kicked off with a hilarious (and slightly unsettling) story of my own AI going rogue, all thanks to a new Mac app called RPLY designed to help with message replies. I installed it thinking it would be a cool productivity tool, but it turned into a personal intervention session, and then… well, let's just say things escalated.

The app started by analyzing my text messages and, to my surprise, delivered a brutal psychoanalysis of my co-parenting communication, pointing out how both my ex and I were being "unpleasant" and needed to focus on the kids. As I said on the show, "I got this as a gut punch. I was like, f*ck, I need to reimagine my messaging choices." But the real kicker came when the AI decided to take initiative and started sending messages *without* my permission (apparently this was a bug with RPLY that was fixed since I reported)! 

Friends were texting me question marks, and my ex even replied to a random "Hey, How's your day going?" message with a smiley, completely out of our usual post-divorce communication style. "This AI, like on Monday before just gave me absolute shit about not being, a person that needs to be focused on the kids also decided to smooth things out on friday" I chuckled, still slightly bewildered by the whole ordeal. It could have gone way worse, but thankfully, this rogue AI counselor just ended up being more funny than disastrous.

Open Source LLMs

DeepHermes preview from NousResearch

Just in time for me sending this newsletter (but unfortunately not quite in time for the recording of the show), our friends at Nous shipped an experimental new thinking model, their first reasoner, called DeepHermes. 

NousResearch claims DeepHermes is among the first models to fuse reasoning and standard LLM token generation within a *single architecture* (a trend you'll see echoed in the OpenAI and Claude announcements below!)

Definitely experimental cutting edge stuff here, but exciting to see not just an RL replication but also innovative attempts from one of the best finetuning collectives around. 

Nomic Embed Text V2 - First Embedding MoE

Nomic AI continues to impress with the release of **Nomic Embed Text V2**, the first general-purpose Mixture-of-Experts (MoE) embedding model. Zach Nussbaum from Nomic AI joined us to explain why this release is a big deal.

* **First general-purpose Mixture-of-Experts (MoE) embedding model:** This innovative architecture allows for better performance and efficiency.

* **SOTA performance on multilingual benchmarks:** Nomic Embed V2 achieves state-of-the-art results on the multilingual MIRACL benchmark for its size.

* **Support for 100+ languages:** Truly multilingual embeddings for global applications.

* **Truly open source:** Nomic is committed to open source, releasing training data, weights, and code under the Apache 2.0 License.

Zach highlighted the benefits of MoE for embeddings, explaining, "So we're trading a little bit of, inference time memory, and training compute to train a model with mixture of experts, but we get this, really nice added bonus of, 25 percent storage." This is especially crucial when dealing with massive datasets. You can check out the model on [Hugging Face](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe) and read the [Technical Report](https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf) for all the juicy details.

AllenAI OLMOE on iOS and New Tulu 3.1 8B

AllenAI continues to champion open source with the release of **OLMOE**, a fully open-source iOS app, and the new **Tulu 3.1 8B** model.

* **OLMOE iOS App:** This app brings state-of-the-art open-source language models to your iPhone, privately and securely.

* Allows users to test open-source LLMs on-device.

* Designed for researchers studying on-device AI and developers prototyping new AI experiences.

* Optimized for on-device performance while maintaining high accuracy.

* Fully open-source code for further development.

* Available on the [App Store](https://apps.apple.com/app/id6738533815) for iPhone 15 Pro or newer and M-series iPads.

* **Tulu 3.1 8B **

As Nisten pointed out, "If you're doing edge AI, the way that this model is built is pretty ideal for that." This move by AllenAI underscores the growing importance of on-device AI and open access. Read more about OLMOE on the [AllenAI Blog](https://allenai.org/blog/olmoe-app).

Groq Adds Qwen Models and Lands on OpenRouter

Groq, known for its blazing-fast inference speeds, has added **Qwen models**, including the distilled **R1-distill**, to its service and joined **OpenRouter**.

* **Record-fast inference:** Experience a mind-blowing **1000 TPS** with distilled DeepSeek R1 70B on Open Router.

* **Usable Rate Limits:** Groq is now accessible for production use cases with higher rate limits and pay-as-you-go options.

* **Qwen Model Support:** Access Qwen models like 2.5B-32B and R1-distill-qwen-32B.

* **Open Router Integration:** Groq is now available on [OpenRouter](https://openrouter.ai/), expanding accessibility for developers.

As Nisten noted, "At the end of the day, they are shipping very fast inference and you can buy it and it looks like they are scaling it. So they are providing the market with what it needs in this case." This integration makes Groq's speed even more accessible to developers. Check out Groq's announcement on [X.com](https://x.com/GroqInc/status/1889347665072173171).

SambaNova adds full DeepSeek R1 671B - flies at 200t/s ([blog](https://sambanova.ai/blog/sambanova-cloud-launches-the-fastest-deepseek-r1-671b))

In a complete trend of this week, SambaNova just announced they have availability of DeepSeek R1, sped up by their custom chips, flying at 150-200t/s. This is the full DeepSeek R1, not the distilled Qwen based versions! 

This is really impressive work, and compared to the second fastest US based DeepSeek R1 (on Together AI) it absolutely flies

Agentica DeepScaler 1.5B Beats o1-preview on Math

Agentica's **DeepScaler 1.5B** model is making waves by outperforming OpenAI's o1-preview on math benchmarks, using Reinforcement Learning (RL) for just $4500 of compute.

* **Impressive Math Performance:** DeepScaleR achieves a **37.1%** Pass@1 on AIME 2025, outperforming the base model and even o1-preview!!

* **Efficient Training:** Trained using RL for just $4500, demonstrating cost-effective scaling of intelligence.

* **Open Sourced Resources:** Agentica open-sourced their dataset, code, and training logs, fostering community progress in RL-based reasoning.

Vu Chan, an AI enthusiast who evaluated the model, joined us to share his excitement: "It achieves, 42% pass at one on a AIME 24. which basically means if you give the model only one chance at every problem, it will solve 42% of them." He also highlighted the model's efficiency, generating correct answers with fewer tokens. You can find the model on [Hugging Face](https://huggingface.co/agentica-org/DeepScaleR-1.5B-Preview), check out the [WandB logs](https://wandb.ai/mluo/deepscaler-1.5b), and see the announcement on [X.com](https://x.com/Yuchenj_UW/status/1889387582066401461).

ModernBert Instruct - Encoder Model for General Tasks

ModernBert, known for its efficient encoder-only architecture, now has an instruct version, **ModernBert Instruct**, capable of handling general tasks.

* **Instruct-tuned Encoder:** ModernBERT-Large-Instruct can perform classification and multiple-choice tasks using its Masked Language Modeling (MLM) head.

* **Beats Qwen .5B:** Outperforms Qwen .5B on MMLU and MMLU Pro benchmarks.

* **Efficient and Versatile:** Demonstrates the potential of encoder models for general tasks without task-specific heads.

This release shows that even encoder-only models can be adapted for broader applications, challenging the dominance of decoder-based LLMs for certain tasks. Check out the announcement on [X.com](https://x.com/bclavie/status/1888963894296936616).

Big CO LLMs + APIs

RIP GPT-5 and o3 - OpenAI Announces Public Roadmap

OpenAI shook things up this week with a roadmap update from Sam Altman, announcing a shift in strategy for GPT-5 and the o-series models. Get ready for **GPT-4.5 (Orion)** and a unified GPT-5 system!

* **GPT-4.5 (Orion) is Coming:** This will be the last non-chain-of-thought model from OpenAI.

* **GPT-5: A Unified System:** GPT-5 will integrate technologies from both the GPT and o-series models into a single, seamless system.

* **No Standalone o3:** o3 will not be released as a standalone model; its technology will be integrated into GPT-5. "We will no longer ship O3 as a standalone model," Sam Altman stated.

* **Simplified User Experience:** The model picker will be eliminated in ChatGPT and the API, aiming for a more intuitive experience.

* **Subscription Tier Changes:**

* Free users will get unlimited access to GPT-5 at a standard intelligence level.

* Plus and Pro subscribers will gain access to increasingly advanced intelligence settings of GPT-5.

* **Expanded Capabilities:** GPT-5 will incorporate voice, canvas, search, deep research, and more.

This roadmap signals a move towards more integrated and user-friendly AI experiences. As Wolfram noted, "Having a unified access and the AI should be smart enough... AI has, we need an AI to pick which AI to use." This seems to be OpenAI's direction. Read Sam Altman's full announcement on [X.com](https://x.com/sama/status/1889755723078443244).

OpenAI Releases ModelSpec v2

OpenAI also released **ModelSpec v2**, an update to their document defining desired AI model behaviors, emphasizing customizability, transparency, and intellectual freedom.

* **Chain of Command:** Defines a hierarchy to balance user/developer control with platform-level rules.

* **Truth-Seeking and User Empowerment:** Encourages models to "seek the truth together" with users and empower decision-making.

* **Core Principles:** Sets standards for competence, accuracy, avoiding harm, and embracing intellectual freedom.

* **Open Source:** OpenAI open-sourced the Spec and evaluation prompts for broader use and collaboration on [GitHub](https://github.com/openai/model_spec/).

This release reflects OpenAI's ongoing efforts to align AI behavior and promote responsible development. Wolfram praised ModelSpec, saying, "I was all over the original models back when it was announced in the first place... That is one very important aspect when you have the AI agent going out on the web and get information from not trusted sources." Explore ModelSpec v2 on the [dedicated website](https://model-spec.openai.com/2025-02-12.html).

VP Vance Speech at AI Summit in Paris - Deregulate and Dominate!

Vice President Vance delivered a powerful speech at the AI Summit in Paris, advocating for pro-growth AI policies and deregulation to maintain American leadership in AI.

* **Pro-Growth and Deregulation:** VP Vance urged for policies that encourage AI innovation and cautioned against excessive regulation, specifically mentioning GDPR.

* **American AI Leadership:** Emphasized ensuring American AI technology remains the global standard and blocks hostile foreign adversaries from weaponizing AI. "Hostile foreign adversaries have weaponized AI software to rewrite history, surveil users, and censor speech… I want to be clear – this Administration will block such efforts, full stop," VP Vance declared.

* **Key Points:**

* Ensure American AI leadership.

* Encourage pro-growth AI policies.

* Maintain AI's freedom from ideological bias.

* Prioritize a pro-worker approach to AI development.

* Safeguard American AI and chip technologies.

* Block hostile foreign adversaries' weaponization of AI.

Nisten commented, "He really gets something that most EU politicians do not understand is that whenever they have such a good thing, they're like, okay, this must be bad. And we must completely stop it." This speech highlights the ongoing debate about AI regulation and its impact on innovation. Read the full speech [here](https://thespectator.com/topic/read-j-d-vance-full-speech-ai-summit-paris/).

Cerebras Powers Perplexity with Blazing Speed (1200 t/s!)

Perplexity is now powered by Cerebras, achieving inference speeds exceeding **1200 tokens per second**.

* **Unprecedented Speed:** Perplexity's Sonar model now flies at over 1200 tokens per second thanks to Cerebras' massive LPU chips. "Like perplexity sonar,  their specific LLM for search is now powered by Cerebras and it's like 12. 100 tokens per second. It's it matches Google now on speed," I noted on the show.

* **Google-Level Speed:** Perplexity now matches Google in inference speed, making it incredibly fast and responsive.

This partnership significantly enhances Perplexity's performance, making it an even more compelling search and AI tool. See Perplexity's announcement on [X.com](https://x.com/perplexity_ai/status/1889392617479082323).

Anthropic Claude Incoming - Combined LLM + Reasoning Model

[Rumors](https://www.theinformation.com/articles/anthropic-strikes-back) are swirling that Anthropic is set to release a new **Claude model** that will be a combined LLM and reasoning model, similar to OpenAI's GPT-5 roadmap.

* **Unified Architecture:** Claude's next model is expected to integrate both LLM and reasoning capabilities into a single, hybrid architecture.

* **Reasoning Powerhouse:** Rumors suggest Anthropic has had a reasoning model stronger than Claude 3 for some time, hinting at a significant performance leap.

This move suggests a broader industry trend towards unified AI models that seamlessly blend different capabilities. Stay tuned for official announcements from Anthropic.

Elon Musk Teases Grok 3 "Weeks Out"

Elon Musk continues to tease the release of **Grok 3**, claiming it will be "a few weeks out" and the "most powerful AI" they have tested, with enhanced reasoning capabilities.

* **Grok 3 Hype:** Elon Musk claims Grok 3 will be the most powerful AI [X.ai](X.ai) has released, with a focus on reasoning.

* **Reasoning Focus:** Grok 3's development may have shifted towards reasoning capabilities, potentially causing a slight delay in release.

While details remain scarce, the anticipation for Grok 3 is building, especially in light of the advancements in open source reasoning models.

This Week's Buzz 🐝

Weave Dataset Editing in UI

Weights & Biases Weave has added a highly requested feature: **dataset editing directly in the UI**.

* **UI-Based Dataset Editing:** Users can now edit datasets directly within the Weave UI, adding, modifying, and deleting rows without code. "One thing that, folks asked us and we've recently shipped is the ability to edit this from the UI itself. So you don't have to have code," I explained.

* **Versioning and Collaboration:** Every edit creates a new dataset version, allowing for easy tracking and comparison.

* **Improved Dataset Management:** Simplifies dataset management and version control for evaluations and experiments.

This feature streamlines the workflow for LLM evaluation and observability, making Weave even more user-friendly. Try it out at [wandb.me/weave](https://wandb.me/weave) 

Toronto Workshops - AI in Production: Evals & Observability

Don't miss our upcoming **AI in Production: Evals & Observability Workshops** in Toronto!

* **Two Dates:** Sunday and Monday workshops in Toronto.

* **Hands-on Learning:** Learn to build and evaluate LLM-powered applications with robust observability.

* **Expert Guidance:** Led by yours truly, Alex Volkov, and featuring Nisten.

* **Limited Spots:** Registration is still open, but spots are filling up fast! Register for Sunday's workshop [here](https://toronto.aitinkerers.org/p/ai-tinkerers-toronto-ai-in-production-evals-observability-workshop-with-weights-biases) and Monday's workshop [here](https://toronto.aitinkerers.org/p/ai-tinkerers-toronto-ai-evals-workshop-with-weights-biases-monday).

Join us to level up your LLM skills and network with the Toronto AI community!

Vision & Video

Adobe Firefly Video - Image to Video and Text to Video

Adobe announced **Firefly Video**, entering the image-to-video and text-to-video generation space.

* **Video Generation:** Firefly Video offers both image-to-video and text-to-video capabilities.

* **Adobe Ecosystem:** Integrates with Adobe's creative suite, providing a powerful tool for video creators.

This release marks Adobe's significant move into the rapidly evolving video generation landscape. Try Firefly Video [here](https://firefly.adobe.com/generate).

Voice & Audio

YouTube Expands AI Dubbing to All Creators

YouTube is expanding **AI dubbing** to all creators, breaking down language barriers on the platform.

* **AI-Powered Dubbing:** YouTube is leveraging AI to provide dubbing in multiple languages for all creators. "YouTube now expands. AI dubbing in languages to all creators, and that's super cool. So basically no language barriers anymore. AI dubbing is here," I announced.

* **Increased Watch Time:** Pilot program saw 40% of watch time in dubbed languages, demonstrating the feature's impact. "Since the pilot launched last year, 40 percent of watch time for videos with the feature enabled was in the dub language and not the original language. That's insane!" I highlighted.

* **Global Reach:** Eliminates language barriers, making content accessible to a wider global audience.

Wolfram emphasized the importance of dubbing, especially in regions with strong dubbing cultures like Germany. "Every movie that comes here is getting dubbed in high quality. And now AI is doing that on YouTube. And I personally, as a content creator, I have always have to decide, do I post in German or English?" This feature is poised to revolutionize content consumption on YouTube. Read more on [X.com](https://x.com/omooretweets/status/1889727021435199998).

Meta Audiobox Aesthetics - Unified Quality Assessment

Meta released **Audiobox Aesthetics**, a unified automatic quality assessment model for speech, music, and sound.

* **Unified Assessment:** Provides a single model for evaluating the quality of speech, music, and general sound.

* **Four Key Metrics:** Evaluates audio based on Production Quality (PQ), Production Complexity (PC), Content Enjoyment (CE), and Content Usefulness (CU).

* **Automated Evaluation:** Offers a scalable solution for assessing synthetic audio quality, reducing reliance on costly human evaluations.

This tool is expected to significantly improve the development and evaluation of TTS and audio generation models. Access the [Paper](https://scontent-den2-1.xx.fbcdn.net/v/t39.2365-6/475941290_1082969453602014_2080888948846738665_n.pdf?_nc_cat=101&ccb=1-7&_nc_sid=3c67a6&_nc_ohc=TAU0g1oWcZoQ7kNvgGAzq4j&_nc_oc=Adh60zhX4jhMo386FVNUKEZwq5hxfe86kI9KNfDXZA2u8MYwGLBCL3zwIEvUt5uBtt8&_nc_zt=14&_nc_ht=scontent-den2-1.xx&_nc_gid=Acc0tHR7eFr8v14Ar7ZaV6V&oh=00_AYA9SCZT7wLl5PCo9qWbR8f8AjoNS1nZDAf4dHX6q8S2eQ&oe=67B34AE0) and [Weights](https://github.com/facebookresearch/audiobox-aesthetics) on GitHub.

Zonos - Expressive TTS with High-Fidelity Cloning

Zyphra released **Zonos**, a highly expressive TTS model with high-fidelity voice cloning capabilities.

* **Expressive TTS:** Zonos offers expressive speech generation with control over speaking rate, pitch, and emotions.

* **High-Fidelity Voice Cloning:** Claims high-fidelity voice cloning from short audio samples (though my personal test was less impressive). "My own voice clone sounded a little bit like me but not a lot. Ok at least for me, the cloning is really really bad," I admitted on the show.

* **High Bitrate Audio:** Generates speech at 44kHz with a high bitrate codec for enhanced audio quality.

* **Open Source & API:** Models are open source, with a commercial API available.

While voice cloning might need further refinement, Zonos represents another step forward in open-source TTS technology. Explore Zonos on [Hugging Face (Hybrid)](https://huggingface.co/Zyphra/Zonos-v0.1-hybrid), [Hugging Face (Transformer)](https://huggingface.co/Zyphra/Zonos-v0.1-transformer), and [GitHub](https://t.co/Fw4SkUmcIu), and read the [Blog post](https://www.zyphra.com/post/beta-release-of-zonos-v0-1).

Tools & Others

Emergent Values AI - AI Utility Functions and Biases

Researchers found that AIs exhibit **emergent values**, including biases in valuing human lives from different regions.

* **Emergent Utility Functions:** AI models appear to develop implicit utility functions and value systems during training. "Research finds that AI's have expected utility functions for people and other emergent values. And this is freaky," I summarized.

* **Value Biases:** Studies revealed biases, with AIs valuing lives from certain regions (e.g., Nigeria, Pakistan, India) higher than others (e.g., Italy, France, Germany, UK, US). "Nigerian people, valued as like eight us people. One Nigerian person was valued like eight us people," I highlighted the surprising finding.

* **Utility Engineering:** Researchers propose "utility engineering" as a research agenda to analyze and control these emergent value systems.

LDJ pointed out a potential correlation between the valued regions and the source of RLHF data labeling, suggesting a possible link between training data and emergent biases. While the study is still debated, it raises important questions about AI value alignment. Read the announcement on [X.com](https://x.com/DanHendrycks/status/1889344074098057439) and the [Paper](https://drive.google.com/file/d/1QAzSj24Fp0O6GfkskmnULmI1Hmx7k_EJ/view).

LM Studio Lands Support for Speculative Decoding

LM Studio, the popular local LLM inference tool, now supports **speculative decoding**, significantly speeding up inference.

* **Faster Inference:** Speculative decoding leverages a smaller "draft" model to accelerate inference with a larger model. "Speculative decoding finally landed in LM studio, which is dope folks. If you use LM studio, if you don't, you should," I exclaimed.

* **Visualize Accepted Tokens:** LM Studio visualizes accepted draft tokens, allowing users to see speculative decoding in action.

* **Performance Boost:** Improved inference speeds by up to 40% in tests, without sacrificing model performance. "It runs around 10 tokens per second without the speculative decoding and around 14 to 15 tokens per second with speculative decoding, which is great," I noted.

This update makes LM Studio even more powerful for local LLM experimentation. See the announcement on [X.com](https://x.com/lmstudio/status/1889789651797319808).

Noam Shazeer / Jeff Dean on Dwarkesh Podcast

Podcast enthusiasts should check out the new **Dwarkesh Podcast** episode featuring Noam Shazeer (Transformer co-author) and Jeff Dean (Google DeepMind).

* **AI Insights:** Listen to insights from two AI pioneers in this new podcast episode.

Tune in to hear from these influential figures in the AI world. Find the announcement on [X.com](https://x.com/dwarkesh_sp/status/1889770108949577768).

What a week, folks! From rogue AI analyzing my personal life to OpenAI shaking up the roadmap and tiny models conquering math, the AI world continues to deliver surprises. Here are some key takeaways:

* **Open Source is Exploding:** Nomic Embed Text V2, OLMoE, DeepScaler 1.5B, and ModernBERT Instruct are pushing the boundaries of what's possible with open, accessible models.

* **Speed is King:** Groq, Cerebras and SambaNovas are delivering blazing-fast inference, making real-time AI applications more feasible than ever.

* Reasoning is Evolving: DeepScaler 1.5B's success demonstrates the power of RL for even small models, and OpenAI and Anthropic are moving towards unified models with integrated reasoning.

* Privacy Matters: AllenAI's OLMoE highlights the growing importance of on-device AI for data privacy.

* The AI Landscape is Shifting: OpenAI's roadmap announcement signals a move towards simpler, more integrated AI experiences, while government officials are taking a stronger stance on AI policy.

Stay tuned to ThursdAI for the latest updates, and don't forget to subscribe to the newsletter for all the links and details! Next week, I'll be in New York, so expect a special edition of ThursdAI from the AI Engineer floor.

TLDR & Show Notes

* **Open Source LLMs**

* NousResearch DeepHermes-3 Preview (X, [HF](https://huggingface.co/NousResearch/DeepHermes-3-Llama-3-8B-Preview))

* Nomic Embed Text V2 - first embedding MoE ([HF](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe), [Tech Report](https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf))

* AllenAI OLMOE on IOS as a standalone app & new Tulu 3.1 8B ([Blog](https://allenai.org/blog/olmoe-app), [App Store](https://apps.apple.com/app/id6738533815))

* Groq adds Qwen models (including R1 distill) and lands on OpenRouter ([X](https://x.com/GroqInc/status/1889347665072173171))

* Agentica DeepScaler 1.5B beats o1-preview on math using RL for $4500 ([X](https://x.com/Yuchenj_UW/status/1889387582066401461), [HF](https://huggingface.co/agentica-org/DeepScaleR-1.5B-Preview), [WandB](https://wandb.ai/mluo/deepscaler-1.5b))

* ModernBert can be instructed (though encoder only) to do general tasks ([X](https://x.com/bclavie/status/1888963894296936616))

* LMArena releases a dataset of 100K votes with human preferences ([X](https://x.com/lmarena_ai/status/1890114273449525439), [HF](https://huggingface.co/datasets/lmarena-ai/arena-human-preference-100k))

* SambaNova adds full DeepSeek R1 671B - flies at 200t/s ([blog](https://sambanova.ai/blog/sambanova-cloud-launches-the-fastest-deepseek-r1-671b))

* **Big CO LLMs + APIs**

* RIP GPT-5 and o3 - OpenAI announces a public roadmap ([X](https://x.com/sama/status/1889755723078443244))

* OpenAI released Model Spec v2 ([Github](https://github.com/openai/model_spec/), [Blog](https://model-spec.openai.com/2025-02-12.html))

* VP Vance Speech at AI Summit in Paris ([full speech](https://thespectator.com/topic/read-j-d-vance-full-speech-ai-summit-paris/))

* Cerebras now powers Perplexity with >1200t/s ([X](https://x.com/perplexity_ai/status/1889392617479082323))

* Anthropic Claude incoming, will be combined LLM + reasoning ([The Information](https://www.theinformation.com/articles/anthropic-strikes-back))

* **This weeks Buzz**

* We've added dataset editing in the UI ([X](https://x.com/weave_wb/status/1887564898777117139))

* 2 workshops in Toronto, [Sunday](https://toronto.aitinkerers.org/p/ai-tinkerers-toronto-ai-in-production-evals-observability-workshop-with-weights-biases) and [Monday](https://toronto.aitinkerers.org/p/ai-tinkerers-toronto-ai-evals-workshop-with-weights-biases-monday)

* **Vision & Video**

* Adobe announces firefly video (img2video and txt2video) ([try it](https://firefly.adobe.com/generate))

* **Voice & Audio**

* Youtube to expand AI Dubbing to all creators ([X](https://x.com/omooretweets/status/1889727021435199998))

* Meta Audiobox Aesthetics - Unified Automatic Quality Assessment for Speech, Music, and Sound ([Paper](https://scontent-den2-1.xx.fbcdn.net/v/t39.2365-6/475941290_1082969453602014_2080888948846738665_n.pdf?_nc_cat=101&ccb=1-7&_nc_sid=3c67a6&_nc_ohc=TAU0g1oWcZoQ7kNvgGAzq4j&_nc_oc=Adh60zhX4jhMo386FVNUKEZwq5hxfe86kI9KNfDXZA2u8MYwGLBCL3zwIEvUt5uBtt8&_nc_zt=14&_nc_ht=scontent-den2-1.xx&_nc_gid=Acc0tHR7eFr8v14Ar7ZaV6V&oh=00_AYA9SCZT7wLl5PCo9qWbR8f8AjoNS1nZDAf4dHX6q8S2eQ&oe=67B34AE0), [Weights](https://github.com/facebookresearch/audiobox-aesthetics))

* Zonos, a highly expressive TTS model with high fidelity voice cloning ([Blog](https://www.zyphra.com/post/beta-release-of-zonos-v0-1), [HF](https://huggingface.co/Zyphra/Zonos-v0.1-hybrid),[HF](https://huggingface.co/Zyphra/Zonos-v0.1-transformer), [Github](https://t.co/Fw4SkUmcIu))

* **Tools & Others**

* Emergent Values AI - Research finds that AI's have expected utility functions ([X](https://x.com/DanHendrycks/status/1889344074098057439), [paper](https://drive.google.com/file/d/1QAzSj24Fp0O6GfkskmnULmI1Hmx7k_EJ/view))

* LMStudio lands support for Speculative Decoding ([X](https://x.com/lmstudio/status/1889789651797319808))

* Noam Shazeer / Jeff Dean on Dwarkesh podcast ([X](https://x.com/dwarkesh_sp/status/1889770108949577768)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-feb-13-my-personal-rogue/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-feb-13-my-personal-rogue?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1NzEwNzM1OCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.c8KqJKjEyvTb5MrWUg-xZ_u-l-ReNT0EFKRwsmUAvBY&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Feb 6 - OpenAI DeepResearch is your personal PHD scientist, o3-mini & Gemini 2.0, OmniHuman-1 breaks reality & more AI news

**Date:** February 07, 2025  
**Duration:** 1:40:29  
**Link:** [https://sub.thursdai.news/p/thursdai-feb-6-openai-deepresearch](https://sub.thursdai.news/p/thursdai-feb-6-openai-deepresearch)

What's up friends, Alex here, back with another ThursdAI hot off the presses.

Hold onto your hats because this week was another whirlwind of AI breakthroughs, mind-blowing demos, and straight-up game-changers. We dove deep into OpenAI's new "Deep Research" agent – and let me tell you, it's not just hype, it's legitimately revolutionary. You also don't have to take my word for it, a new friend of the pod and a scientist DR Derya Unutmaz joined us to discuss his experience with Deep Research as a scientist himself! You don't want to miss this conversation! 

We also unpack Google's Gemini 2.0 release, including the blazing-fast Flash Lite model. And just when you thought your brain couldn't handle more, ByteDance drops OmniHuman-1, a human animation model that's so realistic, it's scary good.

I've also saw maybe 10 more

TLDR & Show Notes

* **Open Source LLMs (and deep research implementations)**

* Jina Node-DeepResearch ([X](https://x.com/jina_ai_), [Github](https://github.com/jina-ai/node-DeepResearch))

* HuggingFace - OpenDeepResearch ([X](https://x.com/reach_vb/status/1886882087237509487))

* Deep Agent - R1 -V ([X](https://x.com/liangchen5518/status/1886171667522842856), [Github](https://github.com/Deep-Agent/R1-V))

* Krutim - Krutim 2 12B, Chitrath VLM, Embeddings and more from India ([X](https://x.com/bhash/status/1886687710363955492), [Blog](https://t.co/yuBW8WbUcX), [HF](https://huggingface.co/krutrim-ai-labs))

* Simple Scaling - S1 - R1 ([Paper](https://arxiv.org/abs/2501.19393))

* Mergekit updated - 

* **Big CO LLMs + APIs**

* OpenAI ships o3-mini and o3-mini High + updates thinking traces ([Blog](https://openai.com/index/openai-o3-mini/), [X](https://x.com/altryne/status/1887616916736622961))

* Mistral relaunches LeChat with Cerebras for 1000t/s ([Blog](https://mistral.ai/en/news/all-new-le-chat))

* OpenAI Deep Research - the researching agent that uses o3 ([X](https://x.com/altryne/status/1886554659588071684), [Blog](https://openai.com/index/introducing-deep-research/))

* Google ships Gemini 2.0 Pro, Gemini 2.0 Flash-lite in AI Studio ([Blog](https://blog.google/technology/google-deepmind/gemini-model-updates-february-2025/))

* Anthropic **Constitutional Classifiers -** announced a universal jailbreak prevention ([Blog](https://anthropic.com/research/constitutional-classifiers), [Try It](https://claude.ai/constitutional-classifiers))

* Cloudflare to protect websites from AI scraping ([News](https://fortune.com/2025/02/04/matthew-prince-ai-audit-block-media/?utm_medium=social&utm_campaign=fortunemagazine&utm_source=twitter.com&xid=soc_socialflow_twitter_FORTUNE))

* HuggingFace becomes the AI Appstore ([link](https://huggingface.co/spaces))

* **This weeks Buzz - Weights & Biases updates**

* AI Engineer workshop ([Saturday 22](https://www.ai.engineer/summit/2025/schedule/wandb-production)) 

* Tinkerers Toronto workshops ([Sunday 23](https://toronto.aitinkerers.org/p/ai-tinkerers-toronto-ai-in-production-evals-observability-workshop-with-weights-biases) , [Monday 24](https://toronto.aitinkerers.org/p/ai-tinkerers-toronto-ai-evals-workshop-with-weights-biases-monday))

* We released a new Dataset editor feature ([X](https://x.com/weave_wb/status/1887564898777117139))

* **Audio and Sound**

* KyutAI open sources Hibiki  - simultaneous translation models ([Samples](https://huggingface.co/spaces/kyutai/hibiki-samples), [HF](https://huggingface.co/collections/kyutai/hibiki-fr-en-67a48835a3d50ee55d37c2b5))

* **AI Art & Diffusion & 3D**

* ByteDance OmniHuman-1 - unparalleled Human Animation Models ([X](https://x.com/altryne/status/1886804788513530137/video/1), [Page](https://omnihuman-lab.github.io/))

* Pika labs adds PikaAdditions - adding anything to existing video ([X](https://x.com/pika_labs/status/1887547042622562646))

* Google added Imagen3 to their API ([Blog](https://developers.googleblog.com/en/imagen-3-arrives-in-the-gemini-api/))

* **Tools & Others**

* Mistral Le Chat has ios an and adroid apps now ([X](https://x.com/dchaplot/status/1887517614689464674))

* CoPilot now has agentic workflows ([X](https://x.com/ashtom/status/1887548091404046359))

* Replit launches free apps agent for everyone ([X](https://x.com/mattppal/status/1886866670649790565))

* Karpathy drops a new 3 hour video on youtube ([X](https://x.com/karpathy/status/1887211193099825254), [Youtube](https://t.co/75mXcUBI8L))

* OpenAI canvas links are now shareable (like Anthropic artifacts) - ([example](https://chatgpt.com/canvas/shared/67a5449a8174819190dc3f8a41ab8d23))

* **Show Notes & Links **

* Guest of the week - Dr [Derya Umnutaz](https://twitter.com/DeryaTR_/) - talking about Deep Research

* He's examples of Ehlers-Danlos Syndrome ([ChatGPT](https://t.co/Yd9K54XtBE)), (ME/CFS) [Deep Research](https://x.com/DeryaTR_/status/1886487553387430396), [Nature article](https://www.nature.com/articles/d41586-025-00377-9) about Deep Reseach with Derya comments

* Hosts

* Alex Volkov - AI Evangelist & Host [@altryne](http://x.com/altryne)

* Wolfram Ravenwolf - AI Evangelist [@WolframRvnwlf](https://x.com/WolframRvnwlf)

* Nisten Tahiraj - AI Dev at [github.GG](http://github.GG) - [@nisten](https://x.com/nisten/status/1884064612695581054)

* LDJ - Resident data scientist - [@ldjconfirmed](https://x.com/ldjconfirmed/status/1884678546431373764)

Big Companies products & APIs

OpenAI's new chatGPT moment with Deep Research, their second "agent" product (X)

Look, I've been reporting on AI weekly for almost 2 years now, and been following the space closely since way before chatGPT (shoutout Codex days) and this definitely feels like **another chatGPT moment** for me.

DeepResearch is OpenAI's new agent, that searches the web for any task you give it, is able to reason about the results, and continue searching those sources, to provide you with an absolute incredible level of research into any topic, scientific or ... the best taqueria in another country. 

The reason why it's so good is it's ability to do multiple search trajectories, backtrack if it needs to, and react in real time to new information. It also has python tool use (to do plots and calculations) and of course, the brain of it is o3, the best reasoning model from OpenAI

Deep Research is only offered on the Pro tier ($200) of chatGPT, and it's the first publicly available way to use o3 full! and boy, does it deliver! 

I've had it review my workshop content, help me research LLM as a judge articles (which it did masterfully) and help me plan datenights in Denver (though it kind of failed at that, showing me a closed restaurant) 

A breakthrough for scientific research

But I'm no scientist, so I've asked Dr 

Derya Unutmaz, M.D.

 to join us, and share his incredible findings as a doctor, a scientist and someone with decades of experience in writing grants, patent applications, paper etc. 

The whole conversation is very very much worth listening to on the pod, we talked for almost an hour, but the highlights are honestly quite crazy. 

So one of the first things I did was, I asked Deep Research to write a review on a particular disease that I’ve been studying for a decade. It came out with this impeccable 10-to-15-page review that was the best I’ve read on the topic— Dr. Derya Unutmaz

And another banger quote

It wrote a phenomenal 25-page patent application for a friend’s cancer discovery—something that would’ve cost 10,000 dollars or more and taken weeks. I couldn’t believe it. Every one of the 23 claims it listed was thoroughly justified

Humanity's LAST exam? 

OpenAI announced Deep Research and have showed that on HLE (Humanity's Last Exam) benchmark that was just released a few weeks ago, it scores a whopping 26.6 percent! When HLE was released (our coverage [here](https://sub.thursdai.news/i/155578714/humanitys-last-exam-the-benchmark-to-beat)) all the way back at ... checks notes... January 23 or this year! the top reasoning models at the time (o1, R1) scored just under 10%

O3-mini and Deep Research now score 13% and 26.6% respectively, which means both that AI is advancing like crazy, but also.. that maybe calling this "last exam" was a bit premature? 😂😅

Deep Research is now also SOTA holder on GAIA, a public benchmark on real world questions, though Clementine (one of GAIA authors) throws a bit of shade on the [result](https://x.com/clefourrier/status/1886385835324457143) since OpenAI didn't really submit their results. Incidently, Clementine is also involved in HuggingFace attempt at replicating Deep Research in the open (with [OpenDeepResearch](https://huggingface.co/blog/open-deep-research)) 

OpenAI releases o3-mini and o3-mini high

This honestly got kind of buried with the Deep Research news, but as promised, on the last day of January, OpenAI released their new reasoning model, which is significantly fast and much cheaper than o1, while matching it on most benchmarks! 

I've been talking about the fact that during o3 announcement (our [coverage](https://sub.thursdai.news/p/dec-26-openai-o3-and-o3?utm_source=publication-search)) that mini may be more practical and useful announcement than o3 itself, given the price and speed of it. 

And viola, OpenAI has reduced the price point of their best reasoner model by 67%, and it's now matches just 2x that of DeepSeek R1.

Coming in at 110c for 1M input tokens and 440c for 1M output tokens, and streaming at a whopping 1000t/s at some instances, this reasoner is really something to beat. 

Great for application developers

In addition to seem to be a great model, comparing it to R1 is a nonstarter IMO, not only because "it’s sending your data to choyna", which IMO is a [ridiculous](https://x.com/altryne/status/1886982075456348416) attack vector and people should be ashamed by posting this content. 

o3-mini supports all of the nice API things that OpenAI has, like tool use, structured outputs, developer messages and streaming. The ability to set the reasoning effort is also interesting for applications! 

Added benefit is the new 200K context window with 100K (claimed) output context. 

It's also really really fast, while R1 availability grows, as it gets hosted on more and more US based providers, none of them are offering the full context window at these token speeds. 

o3-mini-high?! 

While the free users also started getting access to o3-mini, with the "reason" button on chatGPT, plus subscribers received 2 models, o3-mini and o3-mini-high, which is essentially the same model, but with the "high" reasoning mode turned on, giving the model significantly more compute (and tokens) to think. 

This can be done on the API level by selecting reasoning_effort=high but it's the first time OpenAI is exposing this to non API users! 

One highlight for me is, just how MANY tokens o3-mini high things through. In one of my evaluations on Weave, o3-mini high generated around 160K output tokens, answering 20 questions, while DeepSeek R1 for example generated 75K and Gemini Thinking, got the highest score on these, while charging only 14K tokens (though I'm pretty sure Google just doesn't report on thinking tokens yet, this seems like a bug)

As I'm writing this, OpenAI just announced a new update, o3-mini and o3-mini-high now show... "updated" reasoning traces! 

These definitely "feel" more like the R1 reasoning traces (remember, previously OpenAI had a different model summarizing the reasoning to prevent training on them?) but they are not really the RAW ones (confirmed) 

**Google ships Gemini 2.0 Pro, Gemini 2.0 Flash-lite in AI Studio** ([X](https://x.com/???), [Blog](https://blog.google/technology/google-deepmind/gemini-model-updates-february-2025/))

Congrats to our friends at Google for 2.0 👏 Google finally put all the experimental models under one 2.0 umbrella, giving us Gemini 2.0, Gemini 2.0 Flash and a new model! 

They also introduced Gemini 2.0 Flash-lite, a *crazy* fast and cheap model that performs similarly to Flash 1.5. The rate limits on Flash-lite are *twice* as high as the regular Flash, making it incredibly useful for real-time applications. 

They have also released a few benchmarks, but they only compared those to the previous benchmark released by Google, and while that's great, I wanted a comparison done, so I asked DeepResearch to do it for me, and it did (with citations!) 

Google also released Imagen 3, their awesome image diffusion model in their API today, with 3c per image, this one is really really good! 

Mistral's new LeChat spits out 1000t/s + new IOS apps

During the show, Mistral announced new capabilities for their LeChat interface, including a 15$/mo tier, but most importantly, a crazy fast generation using some kind of new inference, spitting out around 1000t/s. (Powered by Cerebras)

Additionally they have code interpreter there, Canvas, and they also claim to have the best OCR and don't forget, they have access to Flux images, and likely are the only place I know of that offers that image model for free! 

Finally, they've released native mobile apps! ([IOS](https://t.co/uAJXAZlPSr), [Android](https://t.co/bACHYIwIS9))

* from my quick tests, the 1000t/s is not always on, my first attempt was instant, it was like black magic, and then the rest of them were pretty much the same speed as before 🤔  Maybe they are getting hammered in traffic... 

This weeks Buzz (What I learned with WandB this week)

I got to play around with O3-Mini *before* it was released (perks of working at Weights & Biases!), and I used [Weave](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=feb6), our observability and evaluation framework, to analyze its performance. The results were… *interesting*.

* **Latency and Token Count:** O3-Mini High's latency was *six times* longer than O3-Mini Low on a simple reasoning benchmark (92 seconds vs. 6 seconds). But here's the kicker: it didn't even answer more questions correctly! And the token count? O3-Mini High used *half a million tokens* to answer 20 questions three times. That's… a lot.

* **Weave Leaderboards:** Nisten got *super* excited about using Weave's leaderboard feature to benchmark models. He realized it could solve a real problem in the open-source community – providing a verifiable and transparent way to share benchmark results. (really, we didnt' rehearse this!) 

I also announced some upcoming workshops I'd love to see you at:

* [**AI Engineer Workshop**](https://www.ai.engineer/summit/2025/schedule/wandb-production)** in NYC:** I'll be running a workshop on evaluations at the AI Engineer Summit in New York on February 22nd. Come say hi and learn about evals!

* **AI Tinkerers Workshops in Toronto:** I'll also be doing two workshops with AI Tinkerers in Toronto on [February 23rd](https://toronto.aitinkerers.org/p/ai-tinkerers-toronto-ai-in-production-evals-observability-workshop-with-weights-biases) and [24th](https://toronto.aitinkerers.org/p/ai-tinkerers-toronto-ai-evals-workshop-with-weights-biases-monday).

ByteDance OmniHuman-1 - a reality bending mind breaking img2human model

Ok, this is where my mind completely broke this week, like absolutely couldn't stop thinking about this release from ByteDance. After releasing the SOTA lipsyncing model just a few months ago (LatentSync, [our coverage](https://sub.thursdai.news/p/thursdai-jan-9th-nvidias-tiny-supercomputer?utm_source=publication-search)) they have once again blew everyone away. This time with a img2avatar model that's unlike anything we've ever seen. 

This one doesn't need words, just watch my live reaction as I lose my mind

The level of real world building in these videos is just absolutely ... too much? The piano keys moving, there's a video of a woman speaking in the microphone, and behind her, the window has reflections of cars and people moving! 

The thing that most blew me away upon review was the Niki Glazer video, with shiny dress and the model almost perfectly replicating the right sources of light. 

Just absolute sorcery! 

The authors confirmed that they don't have any immediate plans to release this as a model or even a product, but given the speed of open source, we'll get this within a year for sure! Get ready

Open Source LLMs (and deep research implementations)

This week wasn't *massive* for open-source releases in terms of entirely *new* models, but the ripple effects of DeepSeek's R1 are still being felt. The community is buzzing with attempts to replicate and build upon its groundbreaking reasoning capabilities. It feels like everyone is scrambling to figure out the "secret sauce" behind R1's "aha moment," and we're seeing some fascinating results.

**Jina Node-DeepResearch and HuggingFace OpenDeepResearch**

The community wasted no time trying to replicate OpenAI's Deep Research agent.

* Jina AI released "Node-DeepResearch" ([X](https://x.com/jina_ai_), [Github](https://github.com/jina-ai/node-DeepResearch)), claiming it follows the "query, search, read, reason, repeat" formula. As I mentioned on the show, "I believe that they're wrong" about it being just a simple loop. O3 is likely a fine-tuned model, but still, it's awesome to see the open-source community tackling this so quickly!

* Hugging Face also announced "OpenDeepResearch" ([X](https://x.com/reach_vb/status/1886882087237509487)), aiming to create a truly open research agent. Clementine Fourrier, one of the authors behind the GAIA benchmark (which measures research agent capabilities), is involved, so this is definitely one to watch.

**Deep Agent - R1 -V:** These folks claim to have replicated DeepSeek R1's "aha moment" – where the model realizes its own mistakes and rethinks its approach – *for just $3*! ([X](https://x.com/liangchen5518/status/1886171667522842856), [Github](https://github.com/Deep-Agent/R1-V))

As I said on the show, "It's crazy, right? Nothing costs $3 anymore. Like it's half a coffee in Starbucks." They even claim you can witness this "aha moment" in a VLM. Open source is moving *fast*.

**Krutim - Krutim 2 12B, Chitrath VLM, Embeddings and more from India:** This Indian AI lab released a whole suite of models, including an improved LLM (Krutim 2), a VLM (Chitrarth 1), a speech-language model (Dhwani 1), an embedding model (Vyakhyarth 1), and a translation model (Krutrim Translate 1). ([X](https://x.com/bhash/status/1886687710363955492), [Blog](https://t.co/yuBW8WbUcX), [HF](https://huggingface.co/krutrim-ai-labs)) They even developed a benchmark called "BharatBench" to evaluate Indic AI performance.

However, the community was quick to point out some… *issues*. As Harveen Singh Chadha pointed out on X, it seems like they blatantly copied IndicTrans, an MIT-licensed model, without even mentioning it. Not cool, Krutim. Not cool.

**AceCoder:** This project focuses on using reinforcement learning (RL) to improve code models. ([X](https://x.com/???)) They claim to have created a pipeline to automatically generate high-quality, verifiable code training data.

They trained a reward model (AceCode-RM) that significantly boosts the performance of Llama-3.1 and Qwen2.5-coder-7B. They even claim you can skip SFT training for code models by using just 80 steps of R1-style training!

**Simple Scaling - S1 - R1:** This paper ([Paper](https://arxiv.org/abs/2501.19393)) showcases the power of *quality over quantity*. They fine-tuned Qwen2.5-32B-Instruct on just *1,000 carefully curated reasoning examples* and matched the performance of o1-preview!

They also introduced a technique called "budget forcing," allowing the model to control its test-time compute and improve performance. As I mentioned, Niklas Mengenhoff, who worked at Allen and was previously on the show, is involved. This is one to really pay attention to – it shows that you don't need massive datasets to achieve impressive reasoning capabilities.

**Unsloth reduces R1 type reasoning to just 7GB VRAM (**[**blog**](https://unsloth.ai/blog/r1-reasoning)**)**

Deepseek R1-zero was autonimously learned reasoning in what they DeepSeek researchers called the "aha moment" 

Unsloth adds another attempt at replicating this "aha moment" and claims they got it down to less than 7B VRAM, and it can see it for free, in a google colab! 

This magic could be recreated through GRPO, a RL algorithm that optimizes responses efficiently without requiring a value function, unlike Proximal Policy Optimization (PPO) which relies on a value function

How it works:1. The model generates groups of responses.2. Each response is scored based on correctness or another metric created by some set reward function rather than an LLM reward model.3 . The average score of the group is computed.4. Each response's score is compared to the group average.5. The model is reinforced to favor higher-scoring responses.

Tools

A few new and interesting tools were released this week as well: 

* Replit rebuilt and released their replit agents in an IOS app and released it free for many users. It can now build mini apps for you on the fly! ([Replit](https://x.com/amasad/status/1886859253648122181))

* Mistral has ios / android apps with the new release of LeChat ([X](https://x.com/dchaplot/status/1887517614689464674))

* Molly Cantillon released [RPLY](https://x.com/mollycantillon/status/1887569755772793000), which sits on your mac, and drafts replies to your messages. I installed it during writing this newsletter, and I did not expect it to hit this hard, it reviewed and summarized my texting patterns to "sound like me" and the models sit on device as well. Very very well crafted tool and the best thing it runs models on device if you want! 

* Github Copilot announced agentic workflows and next line editing, which are cursor features. To try them out you have to download VSCode insiders. They also added Gemini 2.0 ([Blog](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/))

The AI field moves SO fast, I had to update the content of the newsletter around 5 times while writing it as new things kept getting released! 

This was a Banger week that started with o3-mini and deep research, continued with Gemini 2.0 and OmniHuman and "ended" with Mistral x Cerebras, Github copilot agents, o3-mini updated COT reasoning traces and a bunch more! 

AI doesn't stop, and we're here weekly to cover all of this, and give you guys the highlights, but also go deep! 

Really appreciate Derya's appearance on the show this week, please give him a follow and see you guys next week!  

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-feb-6-openai-deepresearch/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-feb-6-openai-deepresearch?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1NjY0MzIwNCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.NR430wkCh_MHYOLU6px9D9xgjCpQZ0jmy1LgwBOGnKo&utm_campaign=CTA_5).

---

