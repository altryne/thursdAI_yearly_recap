# 📅 ThursdAI - GPT5 is here

**Date:** August 07, 2025  
**Duration:** 2:56:19  
**Link:** [https://sub.thursdai.news/p/thursdai-gpt5-is-here](https://sub.thursdai.news/p/thursdai-gpt5-is-here)

---

## Description

Hey folks 👋 Alex here, writing to you, from a makeshift recording studio in an Eastern European hookah bar, where I spent the last 7 hours. Why you ask? Well, when GPT-5 drops, the same week as OpenAI dropping the long awaited OSS models + Google is shipping perfect memory World Models (Genie 3) and tons of other AI drops, well I just couldn't stay away from the stream.

Vacation or not, ThursdAI is keeping you up to date (for 32 months straight, which is also the time since the original GPT-4 release which gave this show its name!)

So, what did we have today on the stream? Well, we started as usual, talking about the AI releases of the week, as if OpenAI dropping OSS models (apache 2) 120B and 20B is "usual". We then covered incredible releases like Google's World model Genie3 (more on this next week!) and Qwen-image + a few small Qwens.

We then were VERY excited to tune in, and watch the (very long) announcement stream from OpenAI, in which they spent an hour to tell us about GPT-5.

This was our longest stream by far (3.5 hours, 1hr was just OpenAI live stream) and I'm putting this here mostly unedited, but chapters are up so feel free to skip to the parts that are interesting to you the most.

00:00 Introduction and Special Guests

00:56 Twitter Space and Live Streaming Plans

02:12 Open Source AI Models Overview

03:44 Qwen and Other New AI Models

08:59 Community Interaction and Comments

10:01 Technical Deep Dive into AI Models

25:06 OpenAI's New Releases and Benchmarks

38:49 Expectations and Use Cases for AI Models

40:03 Tool Use vs. Deep Knowledge in AI

41:02 Evaluating GPT OSS and OpenAI Critique

42:29 Historical and Medical Knowledge in AI

51:16 Opus 4.1 and Coding Models

55:38 Google's Genie 3: A New World Model

01:00:43 Kitten TTS: A Lightweight Text-to-Speech Model

01:02:07 11 Labs' Music Generation AI

01:08:51 OpenAI's GPT-5 Launch Event

01:24:33 Building a French Learning Web App

01:26:22 Exploring the Web App Features

01:29:19 Introducing Enhanced Voice Features

01:30:02 Voice Model Demonstrations

01:32:32 Personalizing Chat GPT

01:33:23 Memory and Scheduling Features

01:35:06 Safety and Training Enhancements

01:39:17 Health Applications of GPT-5

01:45:07 Coding with GPT-5

01:46:57 Advanced Coding Capabilities

01:52:59 Real-World Coding Demonstrations

02:10:26 Enterprise Applications of GPT-5

02:11:49 Amgen's Use of GPT-5 in Drug Design

02:12:09 BBVA's Financial Analysis with GPT-5

02:12:33 Healthcare Applications of GPT-5

02:12:52 Government Adoption of GPT-5

02:13:22 Pricing and Availability of GPT-5

02:13:51 Closing Remarks by Chief Scientist Yakob

02:16:03 Live Reactions and Discussions

02:16:41 Technical Demonstrations and Comparisons

02:33:53 Healthcare and Scientific Advancements with GPT-5

02:47:09 Final Thoughts and Wrap-Up

---

My first reactions to GPT-5

Look, I gotta keep it real with you, my first gut reaction was, hey, I'm on vacation, I don't have time to edit and write the newsletter (EU timezone) so let's see how ChatGPT-5 handles this task. After all, OpenAI has removed all other models from the dropdown, it's all GPT-5 now. (pricing from the incredible writeup by [Simon Willison](https://substack.com/profile/5753967-simon-willison) available [here](https://simonwillison.net/2025/Aug/7/gpt-5/))

And to tell you the truth, I was really disappointed! GPT seems to be incredible at coding benchmarks, with 400K tokens and incredible pricing (just $1.25/$10 compared to Opus $15/$75) this model, per the many friends who got to test it early, is a beast at coding! Readily beating opus on affordability per token, switching from thinking to less thinking when it needs to, it definitely seems like a great improvement for coding and agentic tasks.

But for my, very much honed prompt of "hey, help me with ThursdAI drafts, here's previous drafts that I wrote myself, mimic my tone" it failed.. spectacularly!

Here's just a funny example, after me replying that it did a bad job:

It literally wrote "I'm Alex, I build the mind, not the vibe" 🤦‍♂️ What.. the actual...

For comparison, here's o3, with the same prompt, with a fairly true to tone draft:

High taste testers take on GPT-5

But hey, I have tons of previous speakers in our group chats, and many of them who got early access (I didn't... OpenAI, I can be trusted lol) rave about this model. They are saying that this is a huge jump in intelligence.

Folks like Dr Derya Unutmaz, who jumped on the live show and described how GPT5 does incredible things with less hallucinations, folks like Swyx from [Latent.Space](https://substack.com/profile/89230629-latentspace) who had [early access](https://www.latent.space/p/gpt-5-review) and even got invited to give first reactions to the OpenAI office, and [Pietro Schirano](https://x.com/skirano/status/1953516768317628818) who also showed up in an OpenAI video.

So definitely, definitely check out their vibes, as we all try to wrap our heads around this new intelligence king we got!

Other GPT5 updates

OpenAI definitely cooked, don't get me wrong, with this model plugging into everything else in their platform like memory, voice (that was upgraded and works in custom GPTs now, yay!), canvas and study mode, this will definitely be an upgrade for many folks using the models.

They have now also opened access to GPT-5 to free users, just in time for schools to reopen, including a very interesting Quiz mode (that just showed up for me without asking for it), and connection to Gmail, all those will now work with GPT5.

It now has 400K context, way less hallucinations but fewer refusals also, and the developer upgrades like a new verbosity setting and a new "minimal" reasoning setting are all very welcome!

OpenAI finally launches gpt-oss (120B / 20B) apache 2 licensed models ([model card](https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf), HF)

It was really funny, on the stream Nisten talked about the open source models OpenAI dropped, and said "when we covered it last week", while it was just two days ago! It really does feel like this world is moving really fast.

OpenAI's long promised open source models are here, and they got a fairly mixed bag of reviews from folks. Many folks are celebrating that the western world is now back in the game, releasing incredible local models, with an open license!

Though, after the initial excitement, the vibes are split on these models. Folks are saying that maybe these were trained with only synthetic data, because, like Phi, they seem to be very good at benchmarks, and on the specific tasks they were optimized for (code, math) but [really bad](https://x.com/sam_paech/status/1952839665670922360) at creative writing (Sam Paech from EQBench was not impressed), they are also not multilingual, though OpenAI did release a cookbook [on finetuning](https://cookbook.openai.com/articles/gpt-oss/fine-tune-transfomers) with HuggingFace!

Overall, these models are trained for agentic workflows—supporting function calling, web search, Python execution, configurable reasoning effort, and full raw chain-of-thought access, which we will never get from GPT5.

I particularly love the new approach, where a reasoning effort can be defined directly via the system prompt, by just adding "reasoning: high" to the system prompt, this model will reason for way longer! Can't wait to get back and bench these and share with you.

Overall, the fine-tuning and open source community is split for now, but it's been only a few days, so we'll keep you up to date on how well these models land, regardless, this was a historic week for OpenAI!

Speaking of open models, did you have a chance to try our W&B Inference? The team worked hard to bring these new models to you in record time and incredible pricing (just $.05 for 20B and $.15 for 120B!), these models are definitely worth giving a try!

Plus, if you comment "OSS Power" on our [announcement post](https://x.com/weights_biases/status/1952885962641699287), we'll likely give you a few credits to try it out and let us know what you think!

World models "holy crap" moment - Google Genie3

The other very important release this week was.... not a release at all, but an announcement from Deepmind, with Genie3.

This World Model takes a single image or text prompt and creates a fully interactive, controllable 3D environment that runs in real-time at 24fps. An environment you as a user can control, walk (or fly) in, move around the camera view. It's really mindblowing stuff.

We've covered world models like Mirage on previous episodes, but what Google released is a MAJOR step up in coherency, temporal consistency and just overall quality!

The key breakthrough here is consistency and memory. In one demo, a user could "paint" a virtual wall, turn away, and when they turned back, the paint was still there. This is a massive step towards generalist agents that can train, plan, and reason in entirely simulated worlds, with huge implications for robotics and gaming.

We’re hoping to have the Genie 3 team on the show next week to dive even deeper into this incredible technology!!

Other AI news this week

This week, the "other" news could have filled a full show 2 years ago, we got Qwen keeping the third week of releases with 2 new tiny models + a new diffusion model called Qwen-image ([Blog](https://qwenlm.github.io/blog/qwen-image/), [HF](https://huggingface.co/Qwen/Qwen-Image))

Anthropic decided to pre-empt the GPT5 release, and upgraded Opus 4 and gave us Opus 4.1 with a slight bump in specs.

ElevenLabs released a music API called ElevenMusic, which sounds very very good (this on top of last weeks Riffusion + [Producer.ai](http://Producer.ai) news, that I'm still raving about)

Also in voice an audio, a SUPER TINY TTS model called KittenTTS released, with just 15M parameters and a model that's 25MB, it's surprisingly decent at generating voice ([X](https://x.com/divamgupta/status/1952762876504187065))

And to cap it off with breaking news, the Cursor team, who showed up on the OpenAI stream today (marking quite the change in direction from OpenAI + Windsurf previous friendship), dropped their own CLI version of cursor, reminiscent of Claude Code!

PHEW, wow ok this was a LOT to process. Not only did we tune in for the full GPT-5 release, we did a live stream when gpt-oss dropped as well.

On a personal note, I was very humbled when Sam Altman said it was 32 months since GPT-4 release, because it means this was 32 months of ThursdAI, as many of you know, we started live streaming on March 13, 2023, when GPT-4 was released.

I'm very proud of the incredible community we've built (50K views total across all streams this week!), the incredible co-hosts I have, who step up when I'm on vacation and the awesome guests we have on the show, to keep you up to date every week!

So, a little favor to ask, if you find our content valuable, entertaining, the best way to support this pod is upgrade to a paid sub, and share ThursdAI with a friend or two! 👏 See you next week 🫡

 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-gpt5-is-here/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-gpt5-is-here?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE3MDM5ODk4MywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.KfVeuojm2eKEFqVLDMnVNisA0fGRe6RMdNkMMXRRzW4&utm_campaign=CTA_5).
