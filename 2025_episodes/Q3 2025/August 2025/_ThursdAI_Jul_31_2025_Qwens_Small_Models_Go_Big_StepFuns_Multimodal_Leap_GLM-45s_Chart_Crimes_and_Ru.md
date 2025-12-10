# 📆 ThursdAI – Jul 31, 2025 – Qwen’s Small Models Go Big, StepFun’s Multimodal Leap, GLM-4.5’s Chart Crimes, and Runway’s Mind‑Bending Video Edits + GPT-5 soon?

**Date:** August 01, 2025  
**Duration:** 1:38:28  
**Link:** [https://sub.thursdai.news/p/thursdai-jul-31-2025-qwens-small](https://sub.thursdai.news/p/thursdai-jul-31-2025-qwens-small)

---

## Description

Woohoo, we're almost done with July (my favorite month) and the Open Source AI decided to go out with some fireworks 🎉

Hey everyone, Alex here, writing this without my own personal superintelligence (more: later) and this week has been VERY BUSY with many new open source releases.

Just 1 hour before the show we already had 4 breaking news releases, a tiny Qwen3-coder, Cohere and StepFun both dropped multimodal SOTAs and our friends from Krea dropped a combined model with BFL called Flux[Krea] 👏 

This is on top of a very very busy week, with Runway adding conversation to their video model Alpha, Zucks' superintelligence vision and a new SOTA open video model Wan 2.2. So let's dive straight into this (as always, all show notes and links are in the end) 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Open Source LLMs & VLMs 

Tons of new stuff here, I'll try to be brief but each one of these releases deserves a deeper dive for sure. 

Alibaba is on 🔥 with 3 new Qwen models this week

Yes, this is very similar to last week, where they have also dropped 3 new SOTA models in a week, but, these are additional ones. 

It seems that someone in Alibaba figured out that after splitting away from the hybrid models, they can now release each model separately and get a lot of attention per model! 

Here's the timeline: 

* **Friday (just after our show)**: Qwen3-235B-Thinking-2507 drops (235B total, 22B active, [HF](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507)) 

* **Tuesday**: Qwen3-30B-Thinking-2507 (30B total, 3B active, [HF](https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507))

* **Today**: Qwen3-Coder-Flash-2507 lands (30B total, 3B active for coding, [HF](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8))

Lets start with the SOTA reasoner, the 235B(A22B)-2507 is absolutely the best reasoner among the open source models.

We've put the model on our inference service (at crazy prices $.10/$.10) and it's performing absolutely incredible on reasoning tasks. 

It also jumped to the top OSS model on Artificial Analysis scores, EQBench, Long Context and more evals. It a really really good reasoning model! 

Smaller Qwens for local use

Just a week ago, we've asked Junyang on our show, about smaller models that folks can run on their devices, and he avoided by saying "we're focusing on the larger models" and this week, they delivered not 1 but 2 smaller versions of the bigger models (perfect for Speculative Decoding if you can host the larger ones that is) 

The most interesting one is the Qwen3-Coder-flash, which came out today, with very very impressive stats - and the ability to run locally with almost 80 tok/s on a macbook! 

So for the last two weeks, we now have 3 Qwens (Instruct, Thinking, Coder) and 2 sizes for each (all three have a 30B/A3B version now for local use) 👏

Z.ai GLM and StepFun Step3 

As we've said previously, Chinese companies completely dominate the open source AI field right now, and this week as saw yet another crazy testament to how stark the difference is! 

We've seen a rebranded Zhipu ([Z.ai](http://Z.ai) previously THUDM) release their new GLM 4.5 - which gives Qwen3-thinking a run for it's money. Not quite at that level, but definitely very close. I personally didn't love the release esthetics, showing a blended eval score, which nobody can replicate feels a bit off. 

We also talked about how StepFun has stepped in (sorry for the pun) with a new SOTA in multimodality, called [Step3](https://stepfun.ai/research/en/step3). It's a 321B MoE (with a huge 38B active param count) that achieves very significant multi modal scores (The benchmarks look incredible: 74% on MMMU, 64% on MathVision) 

Big Companies APIs & LLMs

Well, we were definitely thinking we'll get GPT-5 or the Open Source AI model from OpenAI this week, but alas, the tea leaves readers were misled (or were being misleading). We 100% know that gpt-5 is coming as multiple screenshots were blurred and then deleted showing companies already testing it. 

But it looks like August is going to be even hotter than July, with multiple sightings of anonymous testing models on Web Dev arena, like Zenith, Summit, Lobster and a new mystery model on OpenRouter called Zenith - that some claim are the different thinking modes of GPT-5 and the open source model? 

Zuck shares vision for personalized superintelligence ([Meta](https://meta.com/superintelligence))

In a very "Nat Fridman" like post, Mark Zuckerberg finally shared the vision behind his latest push to assemble the most cracked AI engineers.

In his vision, Meta is the right place to provide each one with personalized superintelligence, enhancing individual abilities with user agency according to their own values. (as opposed to a centralized model, which feels like his shot across the bow for the other frontier labs) 

A few highlights: Zuck leans heavily into the rise of personal devices on top of which humans will interact with this superintelligence, including AR glasses and a departure from a complete "let's open source everything" dogman of the past, now there will be a more deliberate considerations of what to open source. 

**This Week's Buzz: Putting Open Source to Work with W&B**

With all these incredible new models, the biggest question is: how can you actually use them? I'm incredibly proud to say that the team at Weights & Biases had all three of the big new Qwen models—Thinking, Instruct, and Coder—live on **W&B Inference **on day one ([link](http://wandb.me/inference?utm_source=thursdai&utm_medium=referral&utm_campaign=jul31))

And our pricing is just unbeatable. Wolfram did a benchmark run that would have cost him **$150** using Claude Opus. On W&B Inference with the Qwen3-Thinking model, it cost him **22 cents**. That's not a typo. It's a game-changer for developers and researchers.

To make it even easier, a listener of the show, Olaf Geibig, posted a [fantastic tutorial](https://x.com/olafgeibig/status/1949779562860056763) on how you can use our free credits and W&B Inference to power tools like Claude Code and VS Code using LiteLLM. It takes less than five minutes to set up and gives you access to state-of-the-art models for pennies. All you need to do is add [this](https://gist.github.com/olafgeibig/7cdaa4c9405e22dba02dc57ce2c7b31f) config to vllm and run claude (or vscode) through it! 

Give our inference service a try [here](http://wandb.me/inference?utm_source=thursdai&utm_medium=referral&utm_campaign=jul31) and follow our main account [@weights_biases](http://x.com/weights_biases) a follow as we often drop ways to get additional free credits when new models release

Vision & Video models

Wan2.2: Open-Source MoE Video Generation Model Launches ([X](https://x.com/Alibaba_Wan/status/1949827662416937443), [HF](https://huggingface.co/Wan-AI))

This is likely the best open source video model, but definitely the first MoE video model! It came out with text2video, image2video and a combined version. 

With 5 second 720p videos, that can even be generator at home on a single 4090, this is definitely a step up in the quality of video models that are fully open source. 

Runway changes the game again - Gen-3 Aleph model for AI video editing / transformation ([X](https://x.com/blizaine/status/1950007468324491523), [X](https://x.com/runwayml/status/1950180894477529490))

Look, there's simply no denying this, AI video has had an incredible year, from open source like Wan, to proprietary models with sounds like VEO3. And it's not surprising that we're seeing this trend, but it's definitely very exciting when we see an approach like Runway has, to editing. 

This adds a chat to the model, and your ability to edit.. anything in the scene. Remove / Add people and environmental effects, see the same scene from a different angle and a lot more! 

Expect personalized entertainment very soon! 

AI Art & Diffusion & 3D

FLUX.1 Krea [dev] launches as a state-of-the-art open-weights text-to-image model ([X](https://x.com/bfl_ml/status/1950920537741336801), [HuggingFace](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev))

Black Forest Labs teamed with Krea AI for Flux.1 Krea [dev], an open-weights text-to-image model ditching the "AI gloss" for natural, distinctive vibes—think DALL-E 2's quirky grain without the saturation. It outperforms open peers and rivals pros in prefs, fully Flux-compatible for LoRAs/tools. Yam and I geeked over the aesthetics frontier; it's a flexible base for fine-tunes, available on Hugging Face with commercial options via FAL/Replicate. If you're tired of cookie-cutter outputs, this breathes fresh life into generations.

Ideogram Character launches: one-shot character consistency for everyone ([X](https://x.com/ideogram_ai/status/1950255115753095307))

Ideogram's Characters feature lets you upload one pic for instant, consistent variants—free for all, with inpainting to swap into memes/art. My tests nailed expressions/scenes (me in cyberpunk? Spot-on), though not always photoreal. Wolfram praised the accuracy; it's a meme-maker's dream! and they give like 10 free ones so give it a go

Tencent Hunyuan3D World Model 1.0 launches as the first open-source, explorable 3D world generator ([X](https://x.com/TencentHunyuan/status/1949288986192834718), [HF](https://huggingface.co/tencent/HunyuanWorld-1))

Tencent's Hunyuan3D World Model 1.0 is the first open-source generator of explorable 3D worlds from text/image—360° immersive, exportable meshes for games/modeling. ~33GB VRAM on complex scenes, but Wolfram called it a metaverse step; I wandered a demo scene, loving the potential despite edges. Integrate into CG pipelines? Game-changer for VR/creators.

Voice & Audio 

Look I wasn't even mentioning this on the show, but it came across my feed just as I was about to wrap up ThursdAI, and it's really something. Riffusion joined forces producer and using FUZZ-2 they now have a fully Chatable studio producer, you can ask for.. anything you would ask in a studio! 

Here's my first reaction, and it's really fun, I think they still are open with the invite code 'STUDIO'... I'm not afiliated with them at all! 

Tools 

Ok I promised some folks we'll add this in,  Nisten went super [viral](https://x.com/nisten/status/1950620243258151122) last week with him using a new open source tool called Crush from CharmBracelet, which is an open version of VSCode and it looks awesome! 

He gave a demo live on the show, including how to set it up to work, with subagents etc. If you're into vibe coding, and using the open source models, def. give Crush a try it's really flying and looks cool! 

Phew, ok, we somehow were able to cover ALLL these releases this week, and we didn’t even have an interview! 

Here’s the TL;DR and links to the folks who subscribed (I’m trying a new thing to promote subs on this newsletter) and see you in two weeks (next week is Wolframs turn again as I’m somewhere in Europe!) 

ThursdAI - July 31st, 2025 - TL;DR

* Hosts and Guests

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](https://x.com/altryne))

* Co Hosts - [@WolframRvnwlf](https://x.com/WolframRvnwlf) [@yampeleg](https://x.com/yampeleg) [@nisten](http://x.com/nisten) [@ldj](https://x.com/ldjconfirmed)

* Open Source LLMs

* Zhipu drops GLM-4.5 355B (A32B) AI model ([X](https://x.com/Zai_org/status/1949831552189518044), [HF](https://huggingface.co/zai-org/GLM-4.5))

* ARCEE AFM‑4.5B and AFM‑4.5B‑Base weights released ([X](https://x.com/LucasAtkins7/status/1950278100874645621), [HF](https://huggingface.co/arcee-ai/AFM-4.5B))

* Qwen is on 🔥 - 3 new models: 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jul-31-2025-qwens-small/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jul-31-2025-qwens-small?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2OTc4OTI5NywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.LRrVKpfASEqA84HAfcEe1oAqMSwECqz4850fTYvAzGw&utm_campaign=CTA_5).
