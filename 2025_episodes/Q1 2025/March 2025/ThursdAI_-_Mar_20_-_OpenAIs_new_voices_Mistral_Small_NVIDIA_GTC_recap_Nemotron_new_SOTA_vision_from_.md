# ThursdAI - Mar 20 - OpenAIs new voices, Mistral Small, NVIDIA GTC recap & Nemotron, new SOTA vision from Roboflow & more AI news

**Date:** March 20, 2025  
**Duration:** 1:51:29  
**Link:** [https://sub.thursdai.news/p/thursdai-mar-20-openais-new-voices](https://sub.thursdai.news/p/thursdai-mar-20-openais-new-voices)

---

## Description

Hey, it's Alex, coming to you fresh off another live recording of ThursdAI, and what an incredible one it's been! 

I was hoping that this week will be chill with the releases, because of NVIDIA's GTC conference, but no, the AI world doesn't stop, and if you blinked this week, you may have missed 2 or 10 major things that happened. 

From Mistral coming back to OSS with the amazing Mistral Small 3.1 (beating Gemma from last week!) to OpenAI dropping a new voice generation model, and 2! new whisper killer ASR models with a Breaking News during our live show (there's a reason we're called ThursdAI) which we watched together and then dissected with Kwindla, our amazing AI VOICE and real time expert. 

Not to mention that we also had dedicated breaking news from friend of the pod Joseph Nelson, that came on the show to announce a SOTA vision model from Roboflow + a new benchmark on which even the top VL models get around 6%! There's also a bunch of other OSS, a SOTA 3d model from Tencent and more! 

And last but not least, Yam is back 🎉 So... buckle up and let's dive in. As always, TL;DR and show notes at the end, and here's the YT live version. (While you're there, please hit subscribe and help me hit that 1K subs on YT 🙏 )

Voice & Audio: OpenAI's Voice Revolution and the Open Source Echo

Hold the phone, everyone, because this week belonged to **Voice & Audio**! Seriously, if you weren't paying attention to the voice space, you missed a seismic shift, courtesy of **OpenAI** and some serious open-source contenders.

OpenAI's New Voice Models - Whisper Gets an Upgrade, TTS Gets Emotional!

OpenAI dropped a suite of next-gen audio models: **gpt-4o-mini-tts-latest** (text-to-speech) and **GPT 4.0 Transcribe** and **GPT 4.0 Mini Transcribe** (speech-to-text), all built upon their powerful transformer architecture.

To unpack this voice revolution, we welcomed back **Kwindla Cramer** from Daily, the voice AI whisperer himself. The headline news? The new **speech-to-text models** are not just incremental improvements; they’re a whole new ballgame. As OpenAI’s Shenyi explained, "Our new generation model is based on our large speech model. This means this new model has been trained on trillions of audio tokens." They're faster, cheaper (Mini Transcribe is *half price* of Whisper!), and boast state-of-the-art accuracy across multiple languages. But the real kicker? They're **promptable!**

"This basically opens up a whole field of prompt engineering for these models, which is crazy," I exclaimed, my mind officially blown. Imagine prompting your transcription model with context – telling it you're discussing dog breeds, and suddenly, its accuracy for breed names skyrockets. That's the power of promptable ASR! I recorded a live reaction aftder dropping of stream, and I was really impressed with how I can get the models to pronounce ThursdAI by just... asking! 

But the voice magic doesn't stop there. **GPT 4.0 Mini TTS**, the new text-to-speech model, can now be prompted for… **emotions!** "You can prompt to be emotional. You can ask it to do some stuff. You can prompt the character a voice," OpenAI even demoed a "Mad Scientist" voice! Captain Ryland voice, anyone? This is a huge leap forward in TTS, making AI voices sound… well, more human.

But wait, there’s more! **Semantic VAD!** Semantic Voice Activity Detection, as OpenAI explained, "chunks the audio up based on when the model thinks The user's actually finished speaking." It’s about understanding the *meaning* of speech, not just detecting silence. Kwindla hailed it as "a big step forward," finally addressing the age-old problem of AI agents interrupting you mid-thought. No more robotic impatience!

OpenAI also threw in noise reduction and conversation item retrieval, making these new voice models production-ready powerhouses. This isn't just an update; it's a voice AI revolution, folks.

They also built a super nice website to test out the new models with [openai.fm](http://openai.fm) ! 

Canopy Labs' Orpheus 3B - Open Source Voice Steps Up

But hold on, the open-source voice community isn't about to be outshone! **Canopy Labs** dropped **Orpheus 3B**, a "natural sounding speech language model" with open-source spirit. 

Orpheus, available in multiple sizes (3B, 1B, 500M, 150M), boasts zero-shot voice cloning and a glorious Apache 2 license. Wolfram noted its current lack of multilingual support, but remained enthusiastic, I played with them a bit and they do sound quite awesome, but I wasn't able to finetune them on my own voice due to "CUDA OUT OF MEMORY" alas

I did a live reaction recording for this model on [X](https://x.com/altryne/status/1902470120313917732/video/1)

NVIDIA Canary - Open Source Speech Recognition Enters the Race

Speaking of open source, **NVIDIA** surprised us with **Canary**, a speech recognition and translation model. "NVIDIA open sourced Canary, which is a 1 billion parameter and 180 million parameter speech recognition and translation, so basically like whisper competitor," I summarized. Canary is tiny, fast, and CC-BY licensed, allowing commercial use. It even snagged second place on the Hugging Face speech recognition leaderboard! Open source ASR just got a whole lot more interesting.

Of course, this won't get to the level of the new SOTA ASR OpenAI just dropped, but this can run locally and allows commercial use on edge devices! 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Vision & Video: Roboflow's Visionary Model and Video Generation Gets Moving

After the voice-apalooza, let's switch gears to the visual world, where **Vision & Video** delivered some knockout blows, spearheaded by **Roboflow** and **StepFun**.

Roboflow's RF-DETR and RF100-VL - A New Vision SOTA Emerges

Roboflow stole the vision spotlight this week with their **RF-DETR** model and the groundbreaking **RF100-VL** benchmark. We were lucky enough to have **Joseph Nelson**, Roboflow CEO, join the show again and give us the breaking news (they published the Github 11 minutes before he came on!) 

RF-DETR is Roboflow's first in-house model, a real-time object detection transformer that's rewriting the rulebook. "We've actually never released a model that we've developed. And so this is the first time where we've taken a lot of those learnings and put that into a model," Joseph revealed.

And what a model it is! RF-DETR is not just fast; it's SOTA on real-world datasets and surpasses the 60 mAP barrier on COCO. But Joseph dropped a truth bomb: COCO is outdated. "The benchmark that everyone uses is, the COCO benchmark… hasn't been updated since 2017, but models have continued to get really, really, really good. And so they're saturated the COCO benchmark," he explained.

Enter **RF100-VL**, Roboflow's revolutionary new benchmark, designed to evaluate vision-language models on *real-world* data. "We, introduced a benchmark that we call RF 100 vision language," Joseph announced. The results? Shockingly low zero-shot performance on real-world vision tasks, highlighting a major gap in current models. Joseph's quiz question about QwenVL 2.5's zero-shot performance on RF100-VL revealed a dismal 5.8% accuracy. "So we as a field have a long, long way to go before we have zero shot performance on real world context," Joseph concluded. RF100-VL is the new frontier for vision, and RF-DETR is leading the charge! Plus, it runs on edge devices and is Apache 2 licensed! Roboflow, you legends! Check out the [RF-DETR Blog Post](https://blog.roboflow.com/rf-detr/#how-to-use-rf-detr), the [RF-DETR Github](https://github.com/roboflow/rf-detr), and the [RF100-VL Benchmark](https://rf100-vl.org/) for more details!

StepFun's Image-to-Video TI2V - Animating Images with Style

Stepping into the video arena, **StepFun** released their **image2video model, TI2V.** TI2V boasts impressive motion controls and generates high-quality videos from images and text prompts, especially excelling in anime-style video generation. Dive into the [TI2V HuggingFace Space](https://huggingface.co/stepfun-ai/stepvideo-ti2v) and [TI2V Github](https://github.com/stepfun-ai/Step-Video-TI2V) to explore further.

Open Source LLMs: Mistral's Triumphant Return, LG's Fridge LLM, NVIDIA's Nemotron, and ByteDance's RL Boost

Let's circle back to our beloved **Open Source LLMs**, where this week was nothing short of a gold rush!

Mistral is BACK, Baby! - Mistral Small 3.1 24B (Again!)

Seriously, **Mistral AI**'s return to open source with **Mistral Small 3.1** deserves another shoutout! "Mistral is back with open source. Let's go!" I cheered, and I meant it. This multimodal, Apache 2 licensed model is a powerhouse, outperforming Gemma 3 and ready for action on a single GPU. Wolfram, ever the pragmatist, noted, "We are in right now, where a week later, you already have some new toys to play with." referring to Gemma 3 that we covered just last week! 

Not only did we get a great new update from Mistral, they also cited our friends at Nous research and their Deep Hermes (released just last week!) for the reason to release the base models alongside finetuned models! 

Mistral Small 3.1 is not just a model; it's a statement: open source is thriving, and Mistral is leading the charge! Check out their [Blog Post](https://mistral.ai/news/mistral-small-3-1), the [HuggingFace page](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503), and the [Base Model on HF](https://huggingface.co/mistralai/Mistral-Small-3.1-24B). 

NVIDIA Nemotron - Distilling, Pruning, Making Llama's Better

**NVIDIA** finally dropped **Llama Nemotron**, and it was worth the wait! 

Nemotron Nano (8B) and Super (49B) are here, with Ultra (253B) on the horizon. These models are distilled, pruned, and, crucially, designed for **reasoning** with a hybrid architecture allowing you to enable and disable reasoning via a simple on/off switch in the system prompt! 

Beating other reasoners like QwQ on GPQA tasks, this distillined and pruned LLama based reasoner seems very powerful! Congrats to NVIDIA

Chris Alexius (a friend of the pod) who co-authored the [announcement](https://developer.nvidia.com/blog/build-enterprise-ai-agents-with-advanced-open-nvidia-llama-nemotron-reasoning-models/), told me that FP8 is expected and when that drops, this model will also fit on a single H100 GPU, making it really great for enterprises who host on their own hardware. 

And yes, it’s ready for commercial use. NVIDIA, welcome to the open-source LLM party! Explore the [Llama-Nemotron HuggingFace Collection](https://huggingface.co/collections/nvidia/llama-nemotron-67d92346030a2691293f200b) and the [Dataset](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset-v1).

LG Enters the LLM Fray with EXAONE Deep 32B - Fridge AI is Officially a Thing

**LG**, yes, *that* LG, surprised everyone by open-sourcing **EXAONE Deep 32B**, a "thinking model" from the fridge and TV giant. "LG open sources EXAONE and EXAONE Deep 32B thinking model," I announced, still slightly amused by the fridge-LLM concept. This 32B parameter model claims "superior capabilities" in reasoning, and while my live test in LM Studio went a bit haywire, quantization could be the culprit. It's non-commercial, but hey, fridge-powered AI is now officially a thing. Who saw that coming? Check out my [Reaction Video](https://www.youtube.com/watch?v=qOfkhWh1zrI), the [LG Blog](https://www.lgresearch.ai/blog/view?seq=543), and the [HuggingFace page](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-32B) for more info.

ByteDance's DAPO - Reinforcement Learning Gets Efficient

From the creators of TikTok, **ByteDance**, comes **DAPO**, a new reinforcement learning method that's outperforming GRPO.  DAPO promises 50% accuracy on AIME 2024 with 50% *less* training steps. Nisten, our RL expert, explained it's a refined GRPO, pushing the boundaries of RL efficiency. Open source RL is getting faster and better, thanks to ByteDance! Dive into the [X thread](https://x.com/_philschmid/status/1902258522059866504), [Github](https://t.co/7MEc5mTlC8), and [Paper](https://arxiv.org/abs/2503.14476) for the technical details.

Big CO LLMs + APIs: Google's Generosity, OpenAI's Oligarch Pricing, and GTC Mania

Switching gears to the Big CO LLM arena, we saw **Google** making moves for the masses, **OpenAI** catering to the elite, and **NVIDIA**… well, being NVIDIA.

Google Makes DeepResearch Free and Adds Canvas

**Google** is opening up **DeepResearch** to everyone for **FREE!** DeepResearch, Gemini's advanced search mode, is now accessible without a Pro subscription. I really like it's revamped UI where you can see the thinking and the sources! I used it live on the show to find out what we talked about in the latest episode of ThursdAI, and it did a pretty good job! 

Plus, Google unveiled **Canvas**, letting you "build apps within Gemini and actually see them." Google is making Gemini more accessible and more powerful, a win for everyone. Here's a [Tetris game](https://g.co/gemini/share/f6643450f880) it built for me and here's a [markdown enabled word counter](https://g.co/gemini/share/eea30bfd11f2) I rebuild every week before I send ThursdAI (making sure I don't send you 10K words every week 😅)

OpenAI's O1 Pro API - Pricey Power for the Few

**OpenAI**, in contrast, released **O1 Pro API**, but with a price tag that's… astronomical. "OpenAI makes O1-pro API available to oligarchs ($600/1mtok output!)," I quipped, highlighting the exclusivity. $600 per million output tokens? "If you code with this, if you vibe code with this, you better already have VCs backing your startup," I warned. O1 Pro might be top-tier performance, but it's priced for the 0.1%.

NVIDIA GTC Recap - Jensen's Hardware Extravaganza

**NVIDIA GTC** was, as always, a hardware spectacle. New GPUs (Blackwell Ultra, Vera Rubin, Feynman!), the tiny **DGX Spark** supercomputer, the **GR00T** robot foundation model, and the **Blue** robot – NVIDIA is building the AI future, brick by silicon brick. Jensen is the AI world's rockstar, and GTC is his sold-out stadium show. Check out [Rowan Cheung's GTC Recap on X](https://x.com/rowancheung/status/1902708463546904894) for a quick overview.

Shoutout to our team at GTC and this amazingly timed logo shot I took from the live stream! 

Antropic adds Web Search

We had a surprise at the end of the show, with Antropic releasing web search. It's a small thing, but for folks who use Cloud AI, it's very important.

You can now turn on web search directly on Claude which makes it... the last frontier lab to enable this feature 😂 Congrats! 

AI Art & Diffusion & 3D: Tencent's 3D Revolution

Tencent Hunyuan 3D 2.0 MV and Turbo - 3D Generation Gets Real-Time

**Tencent** updated **Hunyuan 3D** to **2.0 MV (MultiView) and Turbo**, pushing the boundaries of 3D generation.  Hunyuan 3D 2.0 surpasses SOTA in geometry, texture, and alignment, and the **Turbo** version achieves near real-time 3D generation – under one second on an H100!  Try out the [Hunyuan3D-2mv HF Space](https://huggingface.co/spaces/tencent/Hunyuan3D-2mv) to generate your own 3D masterpieces! 

**MultiView (MV)** is another game-changer, allowing you to input 1-4 views for more accurate 3D models. "MV allows to generate 3d shapes from 1-4 views making the 3D shapes much higher quality" I explained. The demo of generating a 3D mouse from Gemini-generated images showcased the seamless pipeline from thought to 3D object. I literally just asked Gemini with native image generation to generate a character and then 

Holodecks are getting closer, folks!

Closing Remarks and Thank You

And that's all she wrote, folks! Another week, another AI explosion. From voice to vision, open source to Big CO, this week was a whirlwind of innovation. Huge thanks again to our incredible guests, Joseph Nelson from Roboflow, Kwindla Cramer from Daily, and Lucas Atkins from ARCEE! And of course, massive shoutout to my co-hosts, Wolfram, Yam, and Nisten – you guys are the best!

And YOU, the ThursdAI community, are the reason we do this. Thank you for tuning in, for your support, and for being as hyped about AI as we are. Remember, ThursdAI is a labor of love, fueled by Weights & Biases and a whole lot of passion.

Missed anything? [thursdai.news](thursdai.news) is your one-stop shop for the podcast, newsletter, and video replay. And seriously, subscribe to our YouTube channel! Let's get to 1000 subs!

Helpful? We’d love to see you here again! 

TL;DR and Show Notes:

* **Guests and Cohosts**

* Alex Volkov - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

Co Hosts - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@yampeleg](http://x.com/@yampeleg) [@nisten](http://x.com/@nisten)

* Sponsor - Weights & Biases Weave ([@weave_wb](http://x.com/@weave_wb))

* Joseph Nelson - CEO Roboflow ([@josephofiowa](https://x.com/josephofiowa))

* Kindwla Kramer - CEO Daily ([@kwindla](https://x.com/kwindla))

* Lucas Atkins - Labs team at Arcee lead ([@LukasAtkins7](https://x.com/LucasAtkins7/status/1901666078620537339))

* **Open Source LLMs** 

* Mistral Small 3.1 24B - Multimodal ([Blog](https://mistral.ai/news/mistral-small-3-1), [HF](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503), [HF base](https://t.co/6K81wQri4x))

* LG open sources EXAONE and EXAONE Deep 32B thinking model ([Alex Reaction Video](https://www.youtube.com/watch?v=qOfkhWh1zrI), [LG BLOG](https://www.lgresearch.ai/blog/view?seq=543), [HF](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-32B))

* ByteDance releases DAPO - better than GRPO RL Method ([X](https://x.com/_philschmid/status/1902258522059866504), [Github](https://t.co/7MEc5mTlC8), [Paper](https://arxiv.org/abs/2503.14476))

* NVIDIA drops LLama-Nemotron (Super 49B, Nano 8B) with reasoning and data ([X](https://x.com/kuchaev/status/1902078122792775771), [HF](https://huggingface.co/collections/nvidia/llama-nemotron-67d92346030a2691293f200b), [Dataset](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset-v1))

* **Big CO LLMs + APIs**

* Google makes DeepResearch free, Canvas added, Live Previews  ([X](https://x.com/OfficialLoganK/status/1902042453080760404))

* OpenAI makes O1-pro API available to oligarchs ($600/1mtok output!)

* NVIDIA GTC recap - ([X](https://x.com/rowancheung/status/1902708463546904894))

* **This weeks Buzz**

* Come visit the Weights & Biases team at GTC today! 

* **Vision & Video**

* Roboflow drops RF-DETR a SOTA vision model + new eval RF100-VL for VLMs ([Blog](https://blog.roboflow.com/rf-detr/#how-to-use-rf-detr), [Github](https://github.com/roboflow/rf-detr), [Benchmark](https://rf100-vl.org/))

* StepFun dropped their image2video model TI2V ([HF](https://huggingface.co/stepfun-ai/stepvideo-ti2v), [Github](https://github.com/stepfun-ai/Step-Video-TI2V))

* **Voice & Audio**

* OpenAI launches a new voice model and 2 new transcription models ([Blog](https://openai.com/index/introducing-our-next-generation-audio-models/)**, **[Youtube](https://youtu.be/hb-bwLcOMKs))

* Canopy Labs drops Orpheus 3B (1B, 500B, 150M versions) - natural sounding speech language model ([Blog](canopylabs.ai/model-releases), [HF](https://huggingface.co/canopylabs), [Colab](https://colab.research.google.com/drive/1xxPpBwI4l_nKUx0J0nzZTtikfqP3UJ6p?usp=sharing#scrollTo=lV49oiPFpbXL))

* NVIDIA Canary 1B/180M Flash - apache 2 speech recognition and translation LLama finetune ([HF](https://huggingface.co/nvidia/canary-1b-flash))

* **AI Art & Diffusion & 3D**

* Tencent updates Hunyuan 3D 2.0 MV (MultiView) and Turbo ([HF](https://huggingface.co/spaces/tencent/Hunyuan3D-2mv))

* **Tools**

* ARCEE Conductor - model router ([X](https://x.com/LucasAtkins7/status/1901666078620537339))

* Cursor ships Claude 3.7 MAX ([X](https://x.com/cursor_ai/status/1902123296231195047))

* Notebook LM teases MindMaps ([X](https://x.com/tokumin/status/1902251588925915429))

* Gemini Co-Drawing - using Gemini native image output for helping drawing ([HF](https://huggingface.co/spaces/Trudy/gemini-codrawing)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-mar-20-openais-new-voices/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-mar-20-openais-new-voices?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1OTUxMDM3NCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.812WSwOOp_gKQDk1N2rtSroVcHZySLsHWkotp_s9DYU&utm_campaign=CTA_5).
