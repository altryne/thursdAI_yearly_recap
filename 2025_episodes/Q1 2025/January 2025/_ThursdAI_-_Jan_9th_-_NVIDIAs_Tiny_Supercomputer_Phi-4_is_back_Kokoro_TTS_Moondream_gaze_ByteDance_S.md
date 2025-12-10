# 📆 ThursdAI - Jan 9th - NVIDIA's Tiny Supercomputer, Phi-4 is back, Kokoro TTS & Moondream gaze, ByteDance SOTA lip sync & more AI news

**Date:** January 10, 2025  
**Duration:** 1:20:26  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-9th-nvidias-tiny-supercomputer](https://sub.thursdai.news/p/thursdai-jan-9th-nvidias-tiny-supercomputer)

---

## Description

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
