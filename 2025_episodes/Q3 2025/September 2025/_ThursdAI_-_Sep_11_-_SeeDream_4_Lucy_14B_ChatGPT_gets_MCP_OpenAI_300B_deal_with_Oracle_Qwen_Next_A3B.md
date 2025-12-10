# 📆 ThursdAI - Sep 11 - SeeDream 4, Lucy 14B, ChatGPT gets MCP, OpenAI $300B deal with Oracle, Qwen Next A3B & more AI news

**Date:** September 12, 2025  
**Duration:** 1:34:28  
**Link:** [https://sub.thursdai.news/p/sep-11](https://sub.thursdai.news/p/sep-11)

---

## Description

Hey Everyone, Alex here, thanks for being a subscriber! Let's get you caught up on this weeks most important AI news! 

The main thing you need to know this week is likely the incredible Image model that ByteDance released, that overshoots the (incredible image model from last 2 weeks) nano 🍌. ByteDance really outdid themselves on this one! 

But also, a video model with super fast generation, OpenAI rumor made Larry Ellison the richest man alive, ChatGPT gets MCP powers (under a flag you can enable) and much more! 

This week we covered a lot of visual stuff, so while the podcast format is good enough, it's really worth tuning in to the video recording to really enjoy the full show. 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

AI Art and Diffusion

It's rare for me to start the newsletter not on Open Source AI news, but hey, at least this way you know that I'm writing it and not some AI right? 😉

ByteDance SeeDream 4 - 4K SOTA image generation and editing model with up to 6 reference images ([Fal](https://fal.ai/models/fal-ai/bytedance/seedream/v4/edit/requests), [Replicate](https://replicate.com/bytedance/seedream-4))

The level of detail on ByteDance's new model, has really made all the hosts on ThursdAI stop and go... huh? is this AI? Bytedance really outdid themselves with this image model that not only generates images, it also is a fully functional image editing with natural language model. It's a diffusion transformer, able to generate 2K and 4K images, fast (under 5 seconds?) while enabling up to 6 reference images to be provided for the generation. 

This is going to be incredible for all kinds of purposes, AI art, marketing etc'. The promt adherence is quite incredible, text is also crisp and sharp at those 2/4K resolutions. We created this image live on the show with it (using a prompt extended by another model)

I then provided my black and white headshot and the above image and asked to replace me as a cartoon character, and it did, super quick, and even got my bomber jacket and the W&B logo on it in there! Notable, nothing else was changed in the image, showing just how incredible this one is for image editing. 

In you want enhanced realism, our friend FoFr from replicate, reminded us that using IMG_3984.CR2 in the prompt, will make the model show images that are closer to reality, even if they depict some incredibly unrealistic things, like a pack of lions forming his nickname

Additional uses for this model are just getting discovered, and one user already noted that given this model outputs 4K resolution, it can be used as a [creative upscaler](https://x.com/BrentLynch/status/1965922591497134319) for other model outputs. Just shove your photo from another AI in Seedream and ask for an upscale. Just be ware that creative upscalers change some amount of details in the generated picture. 

**DecART AI Lucy 14B Redefines Video Generation speeds! **

If Seedteam blew my mind with images, Decart's Lucy 14B absolutely shattered my expectations for video generation speed. We're talking about generating 5-second videos from images in 6.5 seconds. That's almost faster than watching the video itself!

This video model is not open source yet (despite them adding 14B to the name) but it's smaller 5B brother was open sourced. The speed to quality ratio is really insane here, and while Lucy will not generate or animate text or faces that well, it does produce some decent imagery, but SUPER fast. This is really great for iteration, as AI Video is like a roulette machine, you have to generate a lot of tries to see a good result. 

This paired with Seedream (which is also really fast) are a game changer in the AI Art world! So stoked to see what folks will be creating with these! 

**Bonus Round: Decart's Real-Time Minecraft Mod for Oasis 2 (**[**X**](https://x.com/DecartAI/status/1963758685995368884)**)**

The same team behind Lucy also dropped Oasis 2.0, a Minecraft mod that generates game environments in real-time using diffusion models. I got to play around with it live, and watching Minecraft transform into different themed worlds as I moved through them was surreal.

Want a steampunk village? Just type it in. Futuristic city? Done. The frame rate stayed impressively smooth, and the visual coherence as I moved through the world was remarkable. It's like having an AI art director that can completely reskin your game environment on demand. And while the current quality remains low res, if you consider where Stable Diffusion 1.4 was 3 years ago, and where Seedream 4 is now, and do the same extrapolation to Oasis, in 2-3 years we'll be reskinning whole games on the fly and every pixel will be generated (like Jensen loves to say!) 

**OpenAI adds full MCP to ChatGPT (under a flag) **

This is huge, folks. I've been waiting for this for a while, and finally, OpenAI quietly added full MCP (Model Context Protocol) support to ChatGPT via a hidden "developer mode."

**How to Enable MCP in ChatGPT**

Here's the quick setup I showed during the stream:

* Go to ChatGPT settings → Connectors

* Scroll down to find "Developer Mode" and enable it

* Add MCP servers (I used Rube.ai from Composio)

* Use GPT-4o in developer mode to access your connectors

During the show, I literally had ChatGPT pull Nisten's last five tweets using the Twitter MCP connector. It worked flawlessly (though Nisten was a bit concerned about what tweets it might surface 😂).

The implications are massive - you can now connect ChatGPT to GitHub, databases, your local files, or chain multiple tools together for complex workflows. As Wolfram pointed out though, watch your context usage - each MCP connector eats into that 200K limit.

**Big Moves: Investments and Infrastructure**

Speaking of OpenAI, Let's talk money, because the stakes are getting astronomical. OpenAI reportedly has a $300 billion (!) deal with Oracle for compute infrastructure over five years, starting in 2027. That's not a typo - $60 billion per year for compute. Larry Ellison just became the world's richest person, and Oracle's stock shot up 40% on the news in just a few days! This has got to be one of the biggest compute deals the world has ever head of!

The scale is hard to comprehend. We're talking about potentially millions of H100 GPUs worth of compute power. When you consider that most AI companies are still figuring out how to profitably deploy thousands of GPUs, this deal represents infrastructure investment at a completely different magnitude.

Meanwhile, Mistral just became Europe's newest decacorn, valued at $13.8 billion after receiving $1.3 billion from ASML. For context, ASML makes the lithography machines that TSMC uses to manufacture chips for Nvidia. They're literally at the beginning of the AI chip supply chain, and now they're investing heavily in Europe's answer to OpenAI.

Wolfram made a great point - we're seeing the emergence of three major AI poles: American companies (OpenAI, Anthropic), Chinese labs (Qwen, Kimi, Ernie), and now European players like Mistral. Each is developing distinct approaches and capabilities, and the competition is driving incredible innovation.

**Anthropic's Mea Culpa and Code Interpreter**

After weeks of users complaining about Claude's degraded performance, Anthropic finally admitted there were bugs affecting both Claude Opus and Sonnet. Nisten, who tracks these things closely, speculated that the issues might be related to running different quantization schemes on different hardware during peak usage times. We already reported last week that they admitted that "something was affecting intelligence" but this week they said they pinpointed (and fixed) 2 bugs realted to inference! 

They also launched a code interpreter feature that lets Claude create and edit files directly. It's essentially their answer to ChatGPT's code interpreter - giving Claude its own computer to work with. The demo showed it creating Excel files, PDFs, and documents with complex calculations. Having watched Claude struggle with file operations for months, this is a welcome addition.

**🐝 This Week's Buzz: GLM 4.5 on W&B and We're on Open Router!**

Over at Weights & Biases, we've got some exciting updates for you. First, we've added Zhipu AI's GLM 4.5 to [W&B Inference](http://wandb.me/inference)! This 300B+ parameter model is an absolute beast for coding and tool use, ranking among the top open models on benchmarks like SWE-bench. We've heard from so many of you, including Nisten, about how great this model is, so we're thrilled to host it. You can try it out now and get $2 in free credits to start.

And for all you developers out there, you can [use a proxy](https://x.com/olafgeibig/status/1949779562860056763) like LiteLLM to run GLM 4.5 from our inference endpoint inside Anthropic's Claude Code if you're looking for a powerful and cheap alternative! 

Second, we're now on Open Router! You can find several of our hosted models, like GPT-4-OSS and DeepSeek Coder, on the platform. If you're already using Open Router to manage your model calls, you can now easily route traffic to our high-performance inference stack.

**Open Source Continues to Shine**

Open Source LLM models took a bit of a break this week, but there were still interesting models! 

Baidu released ERNIE-4.5, a very efficient 21B parameter "thinking" MoE that only uses 3B active parameters per token. From the UAE, MBZUAI released K2-Think, a finetune of Qwen 2.5 that's showing some seriously impressive math scores. And Moonshot AI updated Kimi K2, doubling its context window to 256K and further improving its already excellent tool use and writing capabilities.

Tencent released an update to HunyuanImage 2.1, which is a bit slow, but also generates 2K images and is decent at text. 

Qwen drops Qwen3-**Next**-80B-A3B ([X](https://x.com/Alibaba_Qwen/status/1966197643904000262), [HF](https://t.co/zHHNBB2l5X))

In breaking news post the show (we were expecting this on the show itself), Alibaba folks dropped a much more streamlined version of the next Qwen, 80B parametes with only 3B active! They call this an "Ultra Sparse MOE" and it beats Qwen3-32B in perf, rivals Qwen3-235B in reasoning & long-context. 

This is quite unprecedented, as getting models as sparse as to work well takes a lot of effort and skill, but the Qwen folks delivered! 

Tools

We wrapped with a quick shoutout to EBSynth, a nifty video editor that lets you draw or add elements to one frame and extrapolates to the rest—like Photoshop for motion. It's browser-based and fun for VFX tweaks; check the demo video on [X](https://twitter.com/ebsynth/status/1965448361974362432). Simple but powerful for quick video hacks. Speaking of Photoshop, it was confirmed that Nano Banana is going to be embedded into Photoshop for image editing! 

Summary & TL;DR

What a week—Seedream and Lucy alone have me rethinking how fast AI can iterate creatively, while MCP in ChatGPT feels like the dawn of truly accessible agents. With open-source keeping pace and big deals fueling the fire, AI's multimodal future is accelerating. Thanks for tuning in, folks; if you missed the live vibes, catch the podcast or hit [sub.thursdai.news](sub.thursdai.news) for all the links. See you next Thursday—what blew your mind this week? Drop a comment and share with a friend, it's the best way to support this endeavor! 

TL;DR of all topics covered:

**AI Models & APIs:**

* **ChatGPT adds full MCP support** - Developer mode unlocks tool connectors for 400M+ users ([Setup Guide](https://x.com/altryne/status/1965843358653481450))

* **Sea Dream 4.0** - ByteDance's unified image generation/editing model creates 4K images in ~1.8 seconds ([X](https://x.com/fofrAI/status/1942899932505035222), [Try it](https://fal.ai/models/fal-ai/bytedance/seedream/v4/edit/playground))

* **Lucy 14B** - Decart's lightning-fast video model generates 5-second clips in 6.5 seconds ([Demo](https://fal.ai/models/decart/lucy-14b/image-to-video), [Page](https://lucy.decart.ai/))

* **Claude bug fixes** - Anthropic admits to performance issues and releases code interpreter ([Blog](https://www.anthropic.com/news/create-files))

* **Sonoma Dusk & Sky** - Mystery models on OpenRouter with 2M context, rumored to be Grok ([OpenRouter](https://openrouter.ai/openrouter/sonoma-sky-alpha))

**This Week's W&B Buzz:**

* **OpenRouter integration** - Serving models to broader developer community ([Try us](https://openrouter.ai/provider/wandb))

* **GLM 4.5** - 350B parameter coding model added to inference ([X](https://x.com/weights_biases/status/1965176118413344778), [Try It](https://wandb.ai/site/inference/glm-4.5))

* W&B inference in Claude Code with LiteLLM ([Olaf's Guide](https://x.com/olafgeibig/status/1949779562860056763))

**Open Source Releases:**

* **ERNIE 4.5** - Baidu open-sources 21B parameter thinking model with 3B active parameters ([X](https://x.com/Baidu_Inc), [HF](https://huggingface.co/baidu/ERNIE-4.5-21B-A3B-Thinking))

* **K2-think** - MBZUAI's Qwen 2.5 fine-tune with strong math performance ([X](https://x.com/ericxing/status/1965667372284739977))

* **Kimi K2 update** - Doubled context to 256K, improved tool use ([X](https://x.com/LechMazur/status/1965729450940588459))

* **HunyuanImage 2.1** - Tencent's 17B parameter open-source 2K image model ([X](https://x.com/TencentHunyuan/status/1965433678261354563), [HF](https://huggingface.co/tencent/HunyuanImage-2.1))

* Qwen-next-80B-A3B - Alibaba's next frontier MoE with 3B active param ([X](https://x.com/Alibaba_Qwen/status/1966197643904000262), [HF](https://t.co/zHHNBB2l5X))

**Voice & Audio:**

* **Qwen3-ASR-Flash** - 11-language speech recognition with singing support ([X](https://x.com/Alibaba_Qwen/status/1965068737297707261))

* **Stable Audio 2.5** - Enterprise audio generator creating 3-minute tracks in <2 seconds ([X](https://twitter.com/StabilityAI/status/1965784409052995916), [Blog](https://stability.ai/news/stability-ai-introduces-stable-audio-25-the-first-audio-model-built-for-enterprise-sound-production-at-scale), [Try It](https://stableaudio.com/generate))

* **ElevenLabs Voice Remixing** - Modify cloned voices for age, gender, accent ([X](https://x.com/elevenlabsio))

**Business & Investment:**

* **OpenAI-Oracle deal** - $300B infrastructure agreement over 5 years

* **Mistral funding** - $1.3B investment from ASML at $13.8B valuation ([Blog](https://www.cnbc.com/2025/09/09/ai-firm-mistral-valued-at-14-billion-as-asml-takes-major-stake.html))

**Tools:**

* **Oasis 2.0** - Real-time Minecraft world generation mod from Decart ([Try It](http://oasis2.decart.ai/demo))

* **EbSynth** - Video editing tool for frame-by-frame manipulation ([X](https://x.com/ebsynth/status/1965448361974362432))

**Hosts:**

* Alex Volkov ([@altryne](https://x.com/altryne))

* Wolfram RavenWlf ([@WolframRvnwlf](https://x.com/WolframRvnwlf))

* Yam Peleg ([@yampeleg](https://x.com/yampeleg))

* Nisten ([@nisten](https://x.com/nisten))

* LDJ ([@ldjconfirmed](https://x.com/ldjconfirmed)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/sep-11/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/sep-11?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3MzM5ODg1NiwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.SMx-Bbivol8nWte1LRp1keyHr7-aYnhSkNZ0C8Aa5_w&utm_campaign=CTA_5).
