# ThursdAI Episodes - Q1 2025

Total Episodes: 13

---

## 📆 ThursdAI - Mar 27 - Gemini 2.5 Takes #1, OpenAI Goes Ghibli, DeepSeek V3 Roars, Qwen Omni, Wandb MCP & more AI news

**Date:** March 27, 2025  
**Duration:** 1:24:00  
**Link:** [https://sub.thursdai.news/p/thursdai-mar-27-gemini-25-takes-1](https://sub.thursdai.news/p/thursdai-mar-27-gemini-25-takes-1)

Hey everyone, Alex here 👋 

Welcome back to ThursdAI! And folks, what an *absolutely insane* week it's been in the world of AI. Seriously, as I mentioned on the show, we don't often get weeks *this* packed with game-changing releases.

We saw Google emphatically reclaim the #1 LLM spot with Gemini 2.5 Pro (and OpenAI try really hard to hit back with a new ChatGPT), DeepSeek dropped a monster 685B parameter open-source model, Qwen launched a tiny but mighty 7B Omni model that handles voice and video like a champ, and OpenAI *finally* gave us native image generation in GPT-4o, immediately unleashing a tidal wave of Ghibli-fication across the internet. It was intense, with big players seemingly trying to one-up each other constantly – remember when Sam Altman dropped Advanced Voice Mode right when Google was about to show Astra? This weeks was this, on steroids. 

We had a fantastic show trying to unpack it all, joined by the brilliant Tulsee Doshi from the Google Gemini team, my Weights & Biases colleague Morgan McQuire talking MCP tools, and the MLX King himself, Prince Canuma. Plus, my awesome co-hosts Wolfram, Nisten, and Yam were there to add their insights. (watch the LIVE recap or keep reading and listen to the audio pod) 

So, grab your beverage of choice, buckle up, and let's try to make sense of this AI whirlwind! (TL'DR and show notes at the bottom 👇)

Big CO LLMs + APIs

🔥 Google Reclaims #1 with Gemini 2.5 Pro (Thinking!)

Okay, let's start with the big news. Google came out swinging this week, dropping Gemini 2.5 Pro and, based on the benchmarks and our initial impressions, taking back the crown for the best all-around LLM currently available. (Check out the X announcement, the [official blog post](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/), and seriously, go [try it yourself at ai.dev](http://ai.dev)).

We were super lucky to have Tulsee Doshi, who leads the product team for Gemini modeling efforts at Google, join us on the show to give us the inside scoop. Gemini 2.5 Pro Experimental isn't just an incremental update; it's topping benchmarks in complex reasoning, science, math, and coding. As Tulsee explained, this isn't just about tweaking one thing – it's a combination of a significantly enhanced base model *and* improved post-training techniques, including integrating those "thinking" capabilities (like chain-of-thought) right into the core models.

That's why they dropped "thinking" from the official name – it's not a separate mode anymore, it's becoming fundamental to how Gemini operates. Tulsee mentioned their goal is for the main line models *to be* thinking models, leveraging inference time when needed to get the best answer. This is a huge step towards more capable and reliable AI.

The performance gains are staggering across the board. We saw massive jumps on benchmarks like AIME (up nearly 20 points!) and GPQA. But it's not just about the numbers. As Tulsee highlighted, Gemini 2.5 is proving to be incredibly well-rounded, excelling not only on academic benchmarks but also on human preference evaluations like LM Arena (where style control is key). The "vibes" are great, as Wolfram put it. My own testing on reasoning tasks confirms this – the latency is surprisingly low for such a powerful model (around 13 seconds on my hard reasoning questions compared to 45+ for others), and the accuracy is the highest I've seen yet at 66% on that specific challenging set.

It also inherits the strengths of previous Gemini models – native multimodality and that massive long context window (up to 1M tokens!). Tulsee emphasized how crucial long context is, allowing the model to reason over entire code repos, large sets of financial documents, or research papers. The performance on long context tasks, like the needle-in-a-haystack test shown on Live Bench, is truly impressive, maintaining high accuracy even at 120k+ tokens where other models often falter significantly.

Nisten mentioned on the show that while it's better than GPT-4o, it might not completely replace Sonnet 3.5 for him yet, especially for certain coding or medical tasks under 128k context. Still, the consensus is clear: Gemini 2.5 Pro is the absolute best model right now across categories. Go play with it!

ARC-AGI 2 Benchmark Revealed ([X](https://x.com/arcprize/status/1905274808935608528), [Interactive Blog](https://x.com/arcprize/status/1905274808935608528))

Also on the benchmark front, the challenging ARC-AGI 2 benchmark was revealed. This is designed to test tasks that are easy for humans but hard for LLMs. The initial results are sobering: base LLMs score 0% accuracy, and even current "thinking" models only reach about 4%. It highlights just how far we still have to go in developing truly robust AI reasoning, giving us another hill to climb.

GPT-4o got another update (as I'm writing these words!) tied for #1 on LMArena, beating 4.5

How much does Sam want to win over Google? So much he's letting it ALL out. Just now, we saw an update from LMArena and Sam, about a NEW GPT-4o (2025-03-26) which jumps OVER GPT 4.5 (like.. what?) and lands at number 2 on the LM Arena, jumping over 3o points.

Tied #1 in Coding, Hard Prompts. Top-2 across ALL categories. 

Besides getting very close to Gemini but not quite beating it, I gotta ask, what's the point of 4.5 then? 

Open Source LLMs

The open-source community wasn't sleeping this week either, with some major drops!

DeepSeek V3 Update - 685B Parameter Beast!

The Whale Bros at DeepSeek silently dropped an update to their V3 model ([X](https://x.com/deepseek_ai/status/1904526863604883661), [HF](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324)), and it's a monster. We're talking 685 Billion parameters in a Mixture-of-Experts (MoE) architecture. This isn't R1 (their reasoning model), but the powerful base model that R1 was built upon (and supposedly R2 when it'll come out)

The benchmark jumps from the previous version are huge, especially in reasoning:

* MMLU-Pro: 75.9 → 81.2 (+5.3)

* GPQA: 59.1 → 68.4 (+9.3)

* **AIME: 39.6 → 59.4 (+19.8)** (Almost 20 points on competitive math!)

* LiveCodeBench: 39.2 → 49.2 (+10.0)

They're highlighting major boosts in reasoning, stronger front-end dev skills, and smarter tool use. Nisten noted it even gets some hard reasoning questions right that challenge other models. The "vibes" are reportedly great. Wolfram tried to run it locally but found even the 1-bit quantized version too large for his system (though it should *theoretically* fit in combined RAM/VRAM), but he's using it via API. It’s likely the best *non-reasoning* open model right now, potentially the best overall if you can run it.

And huge news for the community – they've released these weights under the MIT License, just like R1! Massive respect to DeepSeek for continuing to push powerful models into the open.

They also highlight being significantly better at Front End development and websites aesthetics. 

Qwen Launches Omni 7B Model - Voice & Video Chat!

Our friends at Qwen (Alibaba) also came through with something super cool: Qwen2.5-Omni-7B ([HF](https://huggingface.co/Qwen/Qwen2.5-Omni-7B)). This is an end-to-end multimodal model that can perceive text, images, audio, AND video, while generating both text and natural-sounding speech, potentially in real-time.

They're using a "Thinker-Talker" architecture. What blew my mind is the size – it's listed as 7B parameters, though I saw a meme suggesting it might be closer to 11B internally (ah, the joys of open source!). Still, even at 11B, having this level of multimodal understanding *and* generation in a relatively small open model is fantastic. It understands voice and video natively and outputs text and voice. Now, when I hear "Omni," I start expecting image generation too (thanks, Google!), so maybe that's next for Qwen? 😉

AI Art & Diffusion & Auto-regression

This was arguably where the biggest "mainstream" buzz happened this week, thanks mainly to OpenAI.

OpenAI Launches Native Image Support in GPT-4o - Ghibli Everywhere!

This felt like a direct response to Gemini 2.5's launch, almost like OpenAI saying, "Oh yeah? Watch this!" They *finally* enabled the native image generation capabilities within GPT-4o (Blog, Examples). Remember that image Greg Brockman tweeted *a year ago* of someone writing on a blackboard with an old OpenAI logo, hinting at this? Well, it's here.

And the results? Honestly, they're stunning. The **prompt adherence** is incredible. It actually listens to what you ask for in detail, including text generation within images, which diffusion models notoriously struggle with. The realism can be jaw-dropping, but it can also generate various styles.

Speaking of styles... the internet immediately lost its collective mind and turned everything into the style of Studio Ghibli ([great X thread here](https://x.com/GrantSlatton/status/1904631016356274286)). My entire feed became Ghibli-fied. It's a testament to how accessible and fun this feature is. Wolfram even suggested we should have Ghibli avatars for the show!

Interestingly, this image generation is apparently **auto-regressive**, not based on diffusion models like Midjourney or Stable Diffusion. This is more similar to how models like Grok's Aurora work, generating the image sequentially (top-to-bottom, kinda like how old GIFs used to load, as Yam pointed out we confirmed). This likely contributes to the amazing prompt adherence, especially with text.

The creative potential is huge – people are generating incredible ad concepts ([like this thread](https://x.com/mrgreen/status/1904886576951300495)) and even recreating entire movie trailers, like this unbelievable Lord of the Rings one ([link](https://x.com/PJaccetturo/status/1905151190872309907)), purely through prompts in GPT-4o. It's wild.

Now, this launch wasn't just about cool features; it also marked a significant shift in OpenAI's *policy* around image generation, aiming for what CEO Sam Altman called "a new high-water mark for us in allowing creative freedom." Joanne Jang, who leads model behavior at OpenAI, shared some fascinating insights into their thinking ([**Reservoir Samples post**](https://reservoirsamples.substack.com/p/thoughts-on-setting-policy-for-new)). 

She explained they're moving away from broad, blanket refusals (which often felt safest but limited creativity) towards a more precise approach focused on preventing *real-world harm*. This means trusting user creativity more, not letting hypothetical worst-case scenarios overshadow everyday usefulness (like generating memes!), and valuing the "unknown, unimaginable possibilities" that overly strict rules might stifle. It's a nuanced approach acknowledging that, as Joanne quoted, "Ships are safest in the harbor... But that’s not what ships or models are for." A philosophy change I definitely appreciate.

Reve - New SOTA Diffusion Contender?

While OpenAI grabbed headlines, another player emerged claiming State-of-the-Art results, this time in the diffusion space. Reve Image 1.0 ([X](https://x.com/Taesung/status/1904220824435032528), [Blog/News](https://decrypt.co/311375/new-reve-image-generator-beats-ai-art-heavyweights-midjourney-and-flux-at-a-penny-per-image), [Try it](https://preview.reve.art/api/misc/sso_callback?code=4%2F0AQSTgQGhy3PinnDf0OVcAVGo3OwJMOe7uK2IRiA1b6mo6eWsKxOWCKibKLwCuhRP0O6KtQ&state=eyJob3N0IjoicHJldmlldy5yZXZlLmFydCIsImZsYXZvciI6InNpZ251cCIsInJrZXkiOiJzc28tYUNEd3RtZGxGRldQMm9kY2Y3dkQiLCJzaWciOiJFRmlhLzRtYUN1U0N4REd6VHF5R1BvRXVlVUNjZ0gxOUdVOG5JTDVOblFnPSJ9&error=&error_description=&id_token=)) apparently beats Midjourney and Flux in benchmarks, particularly in prompt adherence, realism, and even text generation (though likely not as consistently as GPT-4o's native approach).

It works on a credit system ($5 for 500 generations, ~1 cent per image) which is quite affordable. The editing seems a bit different, relying on chatting with the model rather than complex tools. It was kind of hidden/anonymous before, but now they've revealed themselves. Honestly, this would probably be *huge* news if OpenAI hadn't dropped their image bomb the same week.

Ideogram 3 Also Launched - Another SOTA Claim!

And just to make the AI art space even *more* crowded this week, Ideogram also launched version 3.0 ([Blog](https://about.ideogram.ai/3.0), [Try it](https://about.ideogram.ai/3.0)), also claiming state-of-the-art performance!

Ideogram has always been strong with text rendering and logos. Version 3.0 boasts stunning realism, creative design capabilities, and a new "Style References" feature where you can upload images to guide the aesthetic. They claim it consistently outperforms others in human evaluations. It's wild – we had at least *three* major image generation models/updates drop this week, all claiming top performance, and none of them seemed to benchmark directly against each other in their launch materials! It’s hard to keep track!

This Week's Buzz + MCP ([X](https://x.com/morgymcg/status/1904997037688385607), [Github](https://github.com/wandb/MCP-server)!)

Bringing it back to Weights & Biases for a moment. We had Morgan McQuire on the show, who heads up our AI Applied team, to talk about something we're really excited about internally – integrating MCP with Weave, our LLM observability and evaluation tool. Morgan showed a demo and have shipped the MCP server, which you can try right now!

Coming soon is the integration with wandb models, which will allows ML folks around the world to build agents that monitor loss curves for them! 

Weights & Biases Weave Official MCP Server Tool - Talk to Your Evals!

We've launched an official MCP server tool for Weave! What does this mean? If you're using Weave to track your experiments, evaluations, prompts, etc. (and you should be!), you can now literally *chat* with that data. As Morgan demonstrated, you can ask questions like "Tell me about my last three evaluations," and the MCP tool, connected to your Weave data, will not only fetch and summarize that information for you directly in the chat interface (like Claude code or others that support MCP) but will generate a [report](https://wandb.ai/wandb-applied-ai-team/mcp-tests/reports/Model-Evaluation-Analysis--VmlldzoxMjAxMDQ1NA?accessToken=o11lv1bo38pz2xay3x0dwwlb04lovkvcd4f9getbfboe2i7yl00htggxzaqapvcd) and add visualizations! 

This is just the beginning of how we see MCP enhancing observability and interaction with ML workflows. Being able to query and analyze your runs and evaluations using natural language is incredibly powerful.

Agents, Tools & MCP

And speaking of MCP...

OpenAI Adds Support for MCP - MCP WON!

This was HUGE news, maybe slightly overshadowed by the image generation, but potentially far more impactful long-term, as Wolfram pointed out right at the start of the show. OpenAI officially announced support for the Model Context Protocol (MCP) ([docs here](https://openai.github.io/openai-agents-python/mcp/)).

Why is this massive? Because Anthropic initiated MCP, and there was a real fear that OpenAI, being OpenAI, might just create its own competing standard for agent/tool communication, leading to fragmentation (think VHS vs. Betamax, or Blu-ray vs. HD DVD – standards wars suck!). Instead, OpenAI embraced the existing standard. As I said on the show, **MCP WON!**

This is crucial for the ecosystem. It means developers can build tools and agents using the MCP standard, and they should (hopefully) work seamlessly across different models like Claude *and* GPT. OpenAI not only added support but released it in their Agents SDK and explicitly stated support is "coming soon" for the ChatGPT desktop app and response APIs. Yam expertly clarified the distinction: tools are often single API calls, while MCPs are servers that can maintain state, allowing for more complex, guided interactions. Qwen also adding MCP support to their UI just reinforces this – the standard is gaining traction fast. This standardization is absolutely essential for building a robust agentic future.

Voice & Audio

Just one more quick update on the audio front:

OpenAI Updates Advanced Voice Mode with Semantic VAD

Alongside the image generation, OpenAI also quietly updated the advanced voice mode in ChatGPT ([YT announcement](https://www.youtube.com/watch?v=mm4djPNO8os)). The key improvement is "Semantic VAD" (Voice Activity Detection). Instead of just cutting off when you pause (leading to annoying interruptions, especially for kids or people who think while speaking), it now tries to understand the *meaning* and *tone* to determine if you're actually finished talking.

This should lead to a much more natural conversation flow. They also claim better personality, a more engaging natural tone (direct and concise), and less need for you to fill silence with "umms" just to keep the mic open. It might feel a tad slower because it waits a bit longer, but the improvement in interaction quality should be significant.

MLX-Audio

And speaking (heh) of audio and speech, we had the awesome [Prince Canuma](https://x.com/Prince_Canuma/status/1903221389504430273) on the show! If you're into running models locally on Apple Silicon (Macs!), you probably know Prince. He's the MLX King, the creator and maintainer of essential libraries like MLX-VLM (for vision models), FastMLX, MLX Embeddings, and now, MLX-Audio. Seriously, huge props to Prince and the folks in the MLX community for making these powerful open-source models accessible on Mac hardware. It's an incredible contribution.

This week, Prince released MLX-Audio v0.0.3. This isn't just text-to-speech (TTS); it aims to be a comprehensive audio package for MLX. Right now, it supports some of the best open TTS models out there:

* **Kokoro:** The tiny, high-quality TTS model we've covered before.

* **Sesame 1B:** Another strong contender.

* **Orpheus:** From Canopy Labs (as Prince confirmed).

* **Suno Bark:** Known for generating music and sound effects too.

MLX-Audio makes running state-of-the-art speech synthesis locally on your Mac incredibly easy, basically offering a Hugging Face transformers pipeline equivalent but optimized for Apple Silicon. If you have a Mac, pip install mlx-audio and give it a spin! Prince also took a feature request on the show to allow text file input directly, so look out for that!

Phew! See what I mean? An absolutely jam-packed week. 

Huge thanks again to Tulsee, Morgan, and Prince for joining us and sharing their insights, and to Wolfram, Nisten, and Yam for co-piloting through the news storm. And thank YOU all for tuning in! We'll be back next week, undoubtedly trying to catch our breath and make sense of whatever AI marvels (or madness) gets unleashed next. 

P.S - if the ghiblification trend didn’t get to your families as well, the alpha right now is… showing your kids how to be a magician and turn them into Ghibli characters, here are me and my kiddos (who asked to be pirates and princesses) 

TL;DR and Show Notes:

* **Guests and Cohosts**

* Alex Volkov - AI Evangelist & Weights & Biases ([@altryne](http://x.com/altryne))Co Hosts - Wolfram Ravenwlf ([@WolframRvnwlf](https://twitter.com/WolframRvnwlf)), Nisten Tahiraj ([@nisten](https://x.com/nisten/)), Yam Peleg ([@yampeleg](http://x.com/@yampeleg))

* Tulsee Doshi - Head of Product, Gemini Models at Google DeepMind ([@tulseedoshi](https://x.com/tulseedoshi))

* Morgan McQuire - Head of AI Applied Team at Weights & Biases ([@morgymcg](https://x.com/morgymcg))

* Prince Canuma - ML Research Engineer, Creator of MLX Libraries ([@PrinceCanuma](https://x.com/PrinceCanuma))

* **Big CO LLMs + APIs**

* 🔥 Google reclaims #1 position with Gemini 2.5 Pro (thinking) - ([X](https://x.com/JeffDean/status/1904580112248693039), [Blog](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/), [Try it](http://ai.dev))

* ARC-AGI 2 benchmark revealed - Base LLMs score 0%, thinking models 4%.

* **Open Source LLMs**

* Deepseek updates DeepSeek-V3-0324 685B params ([X](https://x.com/deepseek_ai/status/1904526863604883661), [HF](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324)) - MIT License!

* Qwen launches an Omni 7B model - perceives text, image, audio, video & generates text and speech ([HF](https://huggingface.co/Qwen/Qwen2.5-Omni-7B))

* **AI Art & Diffusion & Auto-regression**

* OpenAI launches native image support in GPT-4o (Model Card, [X thread](https://x.com/GrantSlatton/status/1904631016356274286), [Ad threads](https://x.com/mrgreen/status/1904886576951300495), [Full Lord of the Rings trailer](https://x.com/PJaccetturo/status/1905151190872309907), [Model Card](https://cdn.openai.com/11998be9-5319-4302-bfbf-1167e093f1fb/Native_Image_Generation_System_Card.pdf))

* Reve - new SOTA diffusion image gen claims ([X](https://x.com/Taesung/status/1904220824435032528), [Blog/News](https://decrypt.co/311375/new-reve-image-generator-beats-ai-art-heavyweights-midjourney-and-flux-at-a-penny-per-image), [Try](https://preview.reve.art/api/misc/sso_callback?code=4%2F0AQSTgQGhy3PinnDf0OVcAVGo3OwJMOe7uK2IRiA1b6mo6eWsKxOWCKibKLwCuhRP0O6KtQ&state=eyJob3N0IjoicHJldmlldy5yZXZlLmFydCIsImZsYXZvciI6InNpZ251cCIsInJrZXkiOiJzc28tYUNEd3RtZGxGRldQMm9kY2Y3dkQiLCJzaWciOiJFRmlhLzRtYUN1U0N4REd6VHF5R1BvRXVlVUNjZ0gxOUdVOG5JTDVOblFnPSJ9&error=&error_description=&id_token=))

* Ideogram 3 launched - another SOTA claim, strong on text/logos, realism, style refs ([Blog](https://about.ideogram.ai/3.0), [Try it](https://about.ideogram.ai/3.0))

* **This weeks Buzz + MCP**

* Weights & Biases Weave official MCP server tool - talk to your evals! ([X](https://x.com/morgymcg/status/1904997037688385607), [Github](https://github.com/wandb/MCP-server))

* **Agents , Tools & MCP**

* OpenAI has added support for MCP - MCP WON! ([Docs](https://openai.github.io/openai-agents-python/mcp/))

* **Voice & Audio**

* OpenAI updates advanced voice mode with semantic VAD for more natural conversations ([YT announcement](https://www.youtube.com/watch?v=mm4djPNO8os)).

* MLX-Audio v0.0.3 released by Prince Canuma ([Github](https://github.com/Blaizzy/mlx-audio))

* **Show Notes and other Links**

* Catch the show live & subscribe to the newsletter/YouTube: [thursdai.news/yt](thursdai.news/yt)

* Try Gemini 2.5 Pro: [AI.dev](http://ai.dev)

* Learn more about MCP from our previous episode ([March 6th](https://thursdai.news/mar-6)). 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-mar-27-gemini-25-takes-1/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-mar-27-gemini-25-takes-1?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2MDAzMTkyNCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.IMQT2lT3xirKrvCvzsvsdU8jf0QXDdvHXwmj46Imy0Q&utm_campaign=CTA_5).

---

## ThursdAI - Mar 20 - OpenAIs new voices, Mistral Small, NVIDIA GTC recap & Nemotron, new SOTA vision from Roboflow & more AI news

**Date:** March 20, 2025  
**Duration:** 1:51:29  
**Link:** [https://sub.thursdai.news/p/thursdai-mar-20-openais-new-voices](https://sub.thursdai.news/p/thursdai-mar-20-openais-new-voices)

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

---

## 📆 ThursdAI Turns Two! 🎉 Gemma 3, Gemini Native Image, new OpenAI tools, tons of open source & more AI news

**Date:** March 13, 2025  
**Duration:** 1:32:04  
**Link:** [https://sub.thursdai.news/p/thursdai-turns-two-gemma-3-gemini](https://sub.thursdai.news/p/thursdai-turns-two-gemma-3-gemini)

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

---

## ThursdAI - Mar 6, 2025 - Alibaba's R1 Killer QwQ, Exclusive Google AI Mode Chat, and MCP fever sweeping the community!

**Date:** March 06, 2025  
**Duration:** 1:50:59  
**Link:** [https://sub.thursdai.news/p/thursdai-mar-6-2025-alibabas-r1-killer](https://sub.thursdai.news/p/thursdai-mar-6-2025-alibabas-r1-killer)

What is UP folks! Alex here from Weights & Biases (yeah, still, but check this weeks buzz section below for some news!) 

I really really enjoyed today's episode, I feel like I can post it unedited it was so so good. We started the show with our good friend Junyang Lin from Alibaba Qwen, where he told us about their new 32B reasoner QwQ. Then we interviewed Google's VP of the search product, Robby Stein, who came and told us about their upcoming AI mode in Google! I got access and played with it, and it made me switch back from PPXL as my main. 

And lastly, I recently became fully MCP-pilled, since we covered it when it came out over thanksgiving, I saw this acronym everywhere on my timeline but only recently "got it" and so I wanted to have an MCP deep dive, and boy... did I get what I wished for! You absolutely should tune in to the show as there's no way for me to cover everything we covered about MCP with Dina and Jason! ok without, further adieu.. let's dive in (and the TL;DR, links and show notes in the end as always!) 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

🤯 Alibaba's QwQ-32B: Small But Shocking Everyone!

The open-source LLM segment started strong, chatting with friend of the show Junyang Justin Lin from Alibaba’s esteemed Qwen team. They've cooked up something quite special: QwQ-32B, a reasoning-focused, reinforcement-learning-boosted beast that punches remarkably above its weight. We're talking about a mere 32B parameters model holding its ground on tough evaluations against DeepSeek R1, a 671B behemoth!

Here’s how wild this is: You can literally run QwQ on your Mac! Junyang shared that they applied two solid rounds of RL to amp its reasoning, coding, and math capabilities, integrating agents into the model to fully unlock its abilities. When I called out how insane it was that we’ve gone from "LLMs can't do math" to basically acing competitive math benchmarks like AIME24, Junyang calmly hinted that they're already aiming for unified thinking/non-thinking models. Sounds wild, doesn’t it?

Check out the full QwQ release [here](https://huggingface.co/Qwen/QwQ-32B), or dive into their [blog post](https://qwenlm.github.io/blog/qwq-32b/).

🚀 Google Launches AI Mode: Search Goes Next-Level ([X](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne%2Fstatus%2F1897381479459811368), [Blog](https://www.google.com/url?sa=E&q=https%3A%2F%2Fblog.google%2Fproducts%2Fsearch%2Fai-mode-search%2F), [My Live Reaction](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D5QTveQpq1WI%26feature%3Dyoutu.be)).

For the past two years, on this very show, we've been asking, "Where's Google?" in the Gen AI race. Well, folks, they're *back*. And they're back in a *big* way.

Next, we were thrilled to have Google’s own Robby Stein, VP of Product for Google Search, drop by ThursdAI after their massive launch of AI Mode and expanded AI Overviews leveraging Gemini 2.0. Robby walked us through this massive shift, which essentially brings advanced conversational AI capabilities straight into Google. Seriously — Gemini 2.0 is now out here doing complex reasoning while performing fan-out queries behind the scenes in Google's infrastructure.

Google search is literally Googling itself. No joke. "We actually have the model generating fan-out queries — Google searches within searches — to collect accurate, fresh, and verified data," explained Robby during our chat. And I gotta admit, after playing with AI Mode, Google is definitely back in the game—real-time restaurant closures, stock analyses, product comparisons, and it’s conversational to boot. You can check my blind reaction first impression video [here](https://www.youtube.com/watch?v=5QTveQpq1WI). (also, while you're there, why not subscribe to my YT?)

Google has some huge plans, but right now AI Mode is rolling out slowly via Google Labs for Google One AI Premium subscribers first. More soon though!

🐝 This Week's Buzz: Weights & Biases Joins CoreWeave Family!

Huge buzz (in every sense of the word) from Weights & Biases, who made waves with their announcement this week: We've joined forces with CoreWeave! Yeah, that's big news as CoreWeave, the AI hyperscaler known for delivering critical AI infrastructure, has now acquired Weights & Biases to build the ultimate end-to-end AI platform. It's early days of this exciting journey, and more details are emerging, but safe to say: the future of Weights & Biases just got even more exciting. Congrats to the whole team at Weights & Biases and our new colleagues at CoreWeave!

We're committed to all users of WandB so you will be able to keep using Weights & Biases, and we'll continuously improve our offerings going forward! Personally, also nothing changes for ThursdAI! 🎉

MCP Takes Over: Giving AI agents super powers via standardized protocol 

Then things got insanely exciting. Why? Because MCP is blowing up and I had to find out why everyone's timeline (mine included) just got invaded.

Welcoming Cloudflare’s amazing product manager Dina Kozlov and Jason Kneen—MCP master and creator—things quickly got mind-blowing. MCP servers, Jason explained, are essentially tool wrappers that effortlessly empower agents with capabilities like API access and even calling other LLMs—completely seamlessly and securely. According to Jason, "we haven't even touched the surface yet of what MCP can do—these things are Lego bricks ready to form swarms and even self-evolve."

Dina broke down just how easy it is to launch MCP servers on Cloudflare Workers while teasing exciting upcoming enhancements. Both Dina and Jason shared jaw-dropping examples, including composing complex workflows connecting Git, Jira, Gmail, and even smart home controls—practically instantaneously! Seriously, my mind is still spinning.

The MCP train is picking up steam, and something tells me we'll be talking about this revolutionary agent technology a lot more soon. Check out two great MCP directories that popped up this recently: [Smithery](https://smithery.ai/),  [Cursor Directory](https://cursor.directory/mcp) and [Composio](https://mcp.composio.dev/).

This show was one of the best ones we recorded, honestly, I barely need to edit it. It was also a really really fun livestream, so if you prefer seeing to listening, here's the lightly edited live stream

Thank you for being a ThursdAI subscriber, as always here's the TL:DR and shownotes for everything that happened in AI this week and the things we mentioned (and hosts we had)

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

TL;DR and Show Notes 

* **Show Notes & Guests**

* **Alex Volkov** - AI Eveangelist & Weights & Biases ([@altryne](https://x.com/altryne))

* **Co Hosts - ** [@WolframRvnwlf](https://x.com/WolframRvnwlf) [@ldjconfirmed](https://x.com/ldjconfirmed) [@nisten](https://x.com/nisten)

* **Junyang Justin Lin** - Head of Qwen Team, Alibaba - [@JustinLin610](https://x.com/JustinLin610)

* **Robby Stein** - VP of Product, Google Search - [@rmstein](https://x.com/rmstein/status/1897417750622216574)

* **Dina Kozlov** - Product Manager, Cloudflare - [@dinasaur_404](https://x.com/dinasaur_404)

* **Jason Kneen** - MCP Wiz - [@jasonkneen](https://x.com/jasonkneen)

* My Google AI Mode Blind Reaction Video ([Youtube](https://www.youtube.com/watch?v=5QTveQpq1WI))

* Sesame Maya Conversation Demo - ([Youtube](https://www.youtube.com/watch?v=pI_WARqK_X4&t=1s))

* Cloudflare MCP docs ([Blog](https://blog.cloudflare.com/model-context-protocol/))

* Weights & Biases Agents Course Pre-signup - [https://wandb.me/agents](https://wandb.me/agents)

* **Open Source LLMs**

* Qwen's latest reasoning model **QwQ-32B** - matches R1 on some evals ([X](https://x.com/Alibaba_Qwen/status/1897361654763151544), [Blog](https://qwenlm.github.io/blog/qwq-32b/), [HF](https://huggingface.co/Qwen/QwQ-32B), [Chat](https://huggingface.co/spaces/Qwen/QwQ-32B-Demo))

* Cohere4ai - Aya Vision - 8B & 32B ([X](https://x.com/CohereForAI/status/1896923657470886234), [HF](https://huggingface.co/collections/CohereForAI/c4ai-aya-vision-67c4ccd395ca064308ee1484?ref=cohere-ai.ghost.io))

* AI21 - Jamba 1.6 Large & Jamba 1.6 Mini ([X](https://x.com/AI21Labs/status/1897657953261601151), [HF](https://huggingface.co/ai21labs/AI21-Jamba-Large-1.6))

* **Big CO LLMs + APIs**

* Google announces AI Mode & AI Overviews Gemini 2.0 ([X](https://x.com/altryne/status/1897381479459811368), [Blog](https://blog.google/products/search/ai-mode-search/), [My Live Reaction](https://www.youtube.com/watch?v=5QTveQpq1WI&feature=youtu.be))

* OpenAI rolls out GPT 4.5 to plus users - #1 on LM Arena 🔥 ([X](https://x.com/lmarena_ai/status/1896590146465579105))

* Grok Voice is available for free users as well ([X](https://x.com/ebbyamir/status/1897118801231249818))

* Elysian Labs launches Auren ios app ([X](https://x.com/nearcyan/status/1897466463314936034), [App Store](https://auren.app))

* Mistral announces SOTA OCR ([Blog](https://mistral.ai/news/mistral-ocr))

* **This weeks Buzz**

* Weights & Biases is acquired by CoreWeave 🎉 ([Blog](https://wandb.ai/wandb/wb-announcements/reports/W-B-being-acquired-by-CoreWeave--VmlldzoxMTY0MDI1MQ))

* **Vision & Video**

* Tencent HYVideo img2vid is finally here ([X](https://x.com/TXhunyuan/status/1897558826519556325), [HF](https://huggingface.co/tencent/HunyuanVideo-I2V), [Try It](https://video.hunyuan.tencent.com/))

* **Voice & Audio**

* NotaGen - symbolic music generation model **high-quality classical sheet music** [Github](https://github.com/ElectricAlexis/NotaGen), [Demo](https://electricalexis.github.io/notagen-demo/), [HF](https://huggingface.co/ElectricAlexis/NotaGen)

* Sesame takes the world by storm with their amazing voice model ([My Reaction](https://www.youtube.com/watch?v=pI_WARqK_X4&t=1s))

* **AI Art & Diffusion & 3D**

* MiniMax__AI - Image-01: A Versatile Text-to-Image Model at 1/10 the Cost ([X](https://x.com/MiniMax__AI/status/1896475931809817015), [Try it](https://t.co/ATyAN03H1F))

* Zhipu AI - CogView 4 6B - ([X](https://x.com/ChatGLM/status/1896824917880148450), [Github](https://t.co/O8btwDugWI))

* **Tools**

* Google - DataScience agent in GoogleColab [Blog](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/)

* Baidu Miaoda - nocode AI build tool  

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-mar-6-2025-alibabas-r1-killer/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-mar-6-2025-alibabas-r1-killer?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1ODU0NzU0NiwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.M-voYlDuwrNaChuTN_344BQU7iE_0xVmc53La1lJzJQ&utm_campaign=CTA_5).

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

## 📆 ThursdAI - Jan 30 - DeepSeek vs. Nasdaq, R1 everywhere, Qwen Max & Video, Open Source SUNO, Goose agents & more AI news

**Date:** January 30, 2025  
**Duration:** 1:54:46  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-30-deepseek-vs-nasdaq](https://sub.thursdai.news/p/thursdai-jan-30-deepseek-vs-nasdaq)

Hey folks, Alex here 👋

It’s official—grandmas (and the entire stock market) now know about DeepSeek. If you’ve been living under an AI rock, DeepSeek’s new R1 model just set the world on fire, rattling Wall Street (causing the biggest monetary loss for any company, ever!) and rocketing to #1 on the iOS App Store. This week’s ThursdAI show took us on a deep (pun intended) dive into the dizzying whirlwind of open-source AI breakthroughs, agentic mayhem, and big-company cat-and-mouse announcements. Grab your coffee (or your winter survival kit if you’re in Canada), because in true ThursdAI fashion, we’ve got at least a dozen bombshells to cover—everything from brand-new Mistral to next-gen vision models, new voice synthesis wonders, and big moves from Meta and OpenAI.

We’re also talking “reasoning mania,” as the entire industry scrambles to replicate, dethrone, or ride the coattails of the new open-source champion, R1. So buckle up—because if the last few days are any indication, 2025 is officially the Year of Reasoning (and quite possibly, the Year of Agents, or both!)

Open Source LLMs

DeepSeek R1 discourse Crashes the Stock Market

**One-sentence summary**: DeepSeek’s R1 “reasoning model” caused a frenzy this week, hitting #1 on the App Store and briefly sending NVIDIA’s stock plummeting in the process ($560B drop, largest monetary loss of any stock, ever)

Ever since DeepSeek R1 launched ([our technical coverate last week!](https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1?r=2imipa)), the buzz has been impossible to ignore—everyone from your mom to your local barista has heard the name. The speculation? DeepSeek’s new architecture apparently only cost $5.5 million to train, fueling the notion that high-level AI might be cheaper than Big Tech claims. Suddenly, people wondered if GPU manufacturers like NVIDIA might see shrinking demand, and the stock indeed took a short-lived 17% tumble. On the show, I joked, “My mom knows about DeepSeek—your grandma probably knows about it, too,” underscoring just how mainstream the hype has become.

Not everyone is convinced the cost claims are accurate. Even Dario Amodei of Anthropic weighed in with a blog post arguing that DeepSeek’s success *increases* the case for stricter AI export controls. 

Public Reactions

* **Dario Amodei’s blog**In “On DeepSeek and Export Controls,” Amodei argues that DeepSeek’s efficient scaling exemplifies why democratic nations need to maintain a strategic leadership edge—and enforce export controls on advanced AI chips. He sees Chinese breakthroughs as proof that AI competition is global and intense.

* **OpenAI Distillation Evidence**OpenAI mentioned it found “distillation traces” of GPT-4 inside R1’s training data. Hypocrisy or fair game? On ThursdAI, the panel mused that “everyone trains on everything,” so perhaps it’s a moot point.

* **Microsoft Reaction**Microsoft wasted no time, swiftly adding DeepSeek to Azure—further proof that corporations want to harness R1’s reasoning power, no matter where it originated.

* **Government reacted**Even officials in the government, David Sacks, US incoming AI & Crypto czar, discussed the fact that DeepSeek did "distillation" using the term somewhat incorrectly, and presidet Trump was asked about it.

* **API Outages**DeepSeek’s own API has gone in and out this week, apparently hammered by demand (and possibly DDoS attacks). Meanwhile, GPU clouds like Groq are showing up to accelerate R1 at 300 tokens/second, for those who must have it right now.

We've seen so many bad takes on the topic, from seething cope takes, to just gross misunderstandings from gov officials confusing the ios App with the OSS models, folks throwing conspiracy theories into the mix, claiming that $5.5M sum was a PsyOp. The fact of the matter is, DeepSeek R1 is an incredible model, and is now powering (just a week later), multiple products (more on this below) and experiences already, while pushing everyone else to compete (and give us reasoning models!)

Open Thoughts Reasoning Dataset

**One-sentence summary**: A community-led effort, “Open Thoughts,” released a new large-scale dataset (OpenThoughts-114k) of chain-of-thought reasoning data, fueling the open-source drive toward better reasoning models.

Worried about having enough labeled “thinking” steps to train your own reasoner? Fear not. The OpenThoughts-114k dataset aggregates chain-of-thought prompts and responses—114,000 of them—for building or fine-tuning reasoning LLMs. It’s now on [Hugging Face](https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k) for your experimentation pleasure. The ThursdAI panel pointed out how crucial these large, openly available reasoning datasets are. As **Wolfram** put it, “We can’t rely on the big labs alone. More open data means more replicable breakouts like DeepSeek R1.”

Mistral Small 2501 (24B)

**One-sentence summary**: Mistral AI returns to the open-source spotlight with a 24B model that fits on a single 4090, scoring over 81% on MMLU while under Apache 2.0.

Long rumored to be “going more closed,” Mistral AI re-emerged this week with Mistral-Small-24B-Instruct-2501—an Apache 2.0 licensed LLM that runs easily on a 32GB VRAM GPU. That 81% MMLU accuracy is no joke, putting it well above many 30B–70B competitor models. **It was described as** “the perfect size for local inference and a real sweet spot,” noting that for many tasks, 24B is “just big enough but not painfully heavy.” Mistral also finally started comparing themselves to Qwen 2.5 in official benchmarks—a big shift from their earlier reluctance, which we applaud! 

Berkeley TinyZero & RAGEN (R1 Replications)

**One-sentence summary**: Two separate projects (TinyZero and RAGEN) replicated DeepSeek R1-zero’s reinforcement learning approach, showing you can get “aha” reasoning moments with minimal compute.

If you were wondering whether R1 is replicable: yes, it is. **Berkeley’s TinyZero** claims to have reproduced the core R1-zero behaviors for $30 using a small 3B model. Meanwhile, the **RAGEN** project aims to unify RL + LLM + Agents with a minimal codebase. While neither replication is at R1-level performance, they demonstrate how quickly the open-source community pounces on new methods. “We’re now seeing those same ‘reasoning sparks’ in smaller reproductions,” said **Nisten**. “That’s huge.”

Agents

Codename Goose by Blocks ([X](https://x.com/blocks/status/1884292904753254488), [Github](https://block.github.io/goose/))

**One-sentence summary**: Jack Dorsey’s company Blocks released Goose, an open-source local agent framework letting you run keyboard automation on your machine.

Ever wanted your AI to press keys and move your mouse in real time? Goose does exactly that with AppleScript, memory extensions, and a fresh approach to “local autonomy.” On the show, I tried Goose, but found it occasionally “went rogue, trying to delete my WhatsApp chats.” Security concerns aside, Goose is significant: it’s an open-source playground for agent-building. The plugin system includes integration with Git, Figma, a knowledge graph, and more. If nothing else, Goose underscores how hot “agentic” frameworks are in 2025.

OpenAI’s Operator: One-Week-In

It’s been a week since **Operator** went live for Pro-tier ChatGPT users. “It’s the first agent that can run for multiple minutes without bugging me every single second,”. Yet it’s still far from perfect—captchas, login blocks, and repeated confirmations hamper tasks. The potential, though, is enormous: “I asked Operator to gather my [X.com](X.com) bookmarks and generate a summary. It actually tried,” I shared, “but it got stuck on three links and needed constant nudges.” **Simon Willison** added that it’s “a neat tech demo” but not quite a productivity boon yet. Next steps? Possibly letting the brand-new reasoning models (like O1 Pro Reasoning) do the chain-of-thought under the hood.

I also got tired of opening hundreds of tabs for operator, so I wrapped it in a macOS native app, that has native notifications and the ability to launch Operator tasks via a Raycast extension, if you're interested, you can find it on my [Github](https://github.com/altryne/wraperator/tree/main)

Browser-use / Computer-use Alternatives

In addition to Goose, the ThursdAI panel mentioned **browser-use** on [GitHub](https://github.com/browser-use/browser-use), plus numerous code interpreters. So far, none blow minds in reliability. But 2025 is evidently “the year of agents.” If you’re itching to offload your browsing or file editing to an AI agent, expect to tinker, troubleshoot, and yes, babysit. The show consensus? “It’s not about whether agents are coming, it’s about how soon they’ll become truly robust,” said **Wolfram**.

Big CO LLMs + APIs

Alibaba Qwen2.5-Max (& Hidden Video Model) ([Try It](https://chat.qwenlm.ai/))

**One-sentence summary**: Alibaba’s Qwen2.5-Max stands toe-to-toe with GPT-4 on some tasks, while also quietly rolling out video-generation features.

While Western media fixates on DeepSeek, Alibaba’s Qwen team quietly dropped the Qwen2.5-Max MoE model. It clocks in at 69% on MMLU-Pro—beating some OpenAI or Google offerings—and comes with a 1-million-token context window. And guess what? The official Chat interface apparently does hidden video generation, though Alibaba hasn’t publicized it in the English internet. 

In the Chinese AI internet, this video generation model is called [Tongyi Wanxiang](https://tongyi.aliyun.com/wanxiang/), and even has it’s own website, can support first and last video generation and looks really really good, they have a gallery up there, and it even has audio generation together with the video!

This one was an img2video, but the movements are really natural! 

Zuckerberg on LLama4 & LLama4 Mini

In Meta’s Q4 earnings call, Zuck was all about AI (sorry, Metaverse). He declared that LLama4 is in advanced training, with a smaller “LLama4 Mini” finishing pre-training. More importantly, a “reasoning model” is in the works, presumably influenced by the mania around R1. Some employees had apparently posted on Blind about “Why are we paying billions for training if DeepSeek did it for $5 million?” so the official line is that Meta invests heavily for top-tier scale. 

Zuck also doubled down on saying "Glasses are the perfect form factor for AI" , to which I somewhat agree, I love my Meta Raybans, I just wished they were integrated into the ios more. 

He also boasted about their HUGE datacenters, called Mesa, spanning the size of Manhattan, being built for the next step of AI. 

(Nearly) Announced: O3-Mini

Right before the ThursdAI broadcast, rumors swirled that OpenAI might reveal O3-Mini. It’s presumably GPT-4’s “little cousin” with a fraction of the cost. Then…silence. Sam Altman also mentioned they would be bringing o3-mini by end of January, but maybe the R1 crazyness made them keep working on it and training it a bit more? 🤔 

In any case, we'll cover it when it launches. 

This Week’s Buzz

We're still the #1 spot on Swe-bench verified with W&B programmer, and our CTO, Shawn Lewis, chatted with friends of the pod Swyx and Alessio about it! (give it a listen)

We have two upcoming events:

* [**AI.engineer**](AI.engineer) in New York (Feb 20–22). Weights & Biases is sponsoring, and I will broadcast ThursdAI live from the summit. If you snagged a ticket, come say hi—there might be a cameo from the “Chef.”

* **Toronto Tinkerer Workshops** (late February) in the University of Toronto. The Canadian AI scene is hot, so watch out for sign-ups (will add them to the show next week)

Weights & Biases also teased more features for LLM observability (Weave) and reminded folks of their new suite of evaluation tools. “If you want to know if your AI is actually better, you do evals,” **Alex** insisted. For more details, check out [wandb.me/weave](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=jan30) or tune into the next ThursdAI.

Vision & Video

DeepSeek - Janus Pro - multimodal understanding and image gen unified (1.5B & 7B)

**One-sentence summary**: Alongside R1, DeepSeek also released Janus Pro, a unified model for image understanding and generation (like GPT-4’s rumored image abilities).

DeepSeek apparently never sleeps. **Janus Pro** is MIT-licensed, 7B parameters, and can both parse images (SigLIP) and generate them (LlamaGen).  The model outperforms DALL·E 3 and SDXL! on some internal benchmarks—though at a modest 384×384 resolution. 

NVIDIA’s Eagle 2 Redux

**One-sentence summary**: NVIDIA re-released the Eagle 2 vision-language model with 4K resolution support, after mysteriously yanking it a week ago.

Eagle 2 is back, boasting multi-expert architecture, 16k context, and high-res video analysis. Rumor says it competes with big 70B param vision models at only 9B. But it’s overshadowed by Qwen2.5-VL (below). Some suspect NVIDIA is aiming to outdo Meta’s open-source hold on vision—just in time to keep GPU demand strong.

Qwen 2.5 VL - SOTA oss vision model is here 

**One-sentence summary**: Alibaba’s Qwen 2.5 VL model claims state-of-the-art in open-source vision, including 1-hour video comprehension and “object grounding.”

The Qwen team didn’t hold back: “It’s the final boss for vision,” joked **Nisten**. Qwen 2.5 VL uses advanced temporal modeling for video and can handle complicated tasks like OCR or multi-object bounding boxes. 

Featuring advances in precise object localization, video temporal understanding and agentic capabilities for computer, this is going to be the model to beat! 

Voice & Audio

YuE 7B (Open “Suno”)

Ever dream of building the next pop star from your code editor? YuE 7B is your ticket. This model, now under Apache 2.0, supports chain-of-thought creation of structured songs, multi-lingual lyrics, and references. It’s slow to infer, but it’s arguably the best open music generator so far in the open source

What's more, they have changed the license to apache 2.0 just before we went live, so you can use YuE everywhere! 

Refusion Fuzz

Refusion, a new competitor to paid audio models like Suno and Udio, launched “Fuzz,” offering free music generation online until GPU meltdown.

If you want to dabble in “prompt to jam track” without paying, check out [Refusion Fuzz](https://refusion.ai/fuzz). Will it match the emotional nuance of premium services like 11 Labs or Hauio? Possibly not. But hey, free is free.

Tools (that have integrated R1)

Perplexity with R1

In the [perplexity.ai](perplexity.ai) chat, you can choose “Pro with R1” if you pay for it,  harnessing R1’s improved reasoning to parse results. For some, it’s a major upgrade to “search-based question answering.” Others prefer it to paying for O1 or GPT-4. 

I always check Perplexity if it knows what the latest episode of ThursdAI was, and it's the first time it did a very good summary! I legit used it to research the show this week! It's really something. 

Meanwhile, [Exa.ai](Exa.ai) also integrated a “DeepSeek Chat” for your agent-based workflows. Like it or not, R1 is everywhere.

[Krea.ai](Krea.ai) with DeepSeek

Our friends at Krea, an AI art tool aggregator, also hopped on the R1 bandwagon for chat-based image searching or generative tasks.

Conclusion

Key Takeaways

* **DeepSeek’s R1 has massive cultural reach**, from #1 apps to spooking the stock market.

* **Reasoning mania** is upon us—everyone from Mistral to Meta wants a piece of the logic-savvy LLM pie.

* **Agentic frameworks** like Goose, Operator, and browser-use are proliferating, though they’re still baby-stepping through reliability issues.

* **Vision and audio** get major open-source love, with Janus Pro, Qwen 2.5 VL, YuE 7B, and more reshaping multimodality.

* **Big Tech** (Meta, Alibaba, OpenAI) is forging ahead with monster models, multi-billion-dollar projects, and cross-country expansions in search of the best reasoning approaches.

At this point, it’s not even about where the next big model drop comes from; it’s about how quickly the entire ecosystem can adopt (or replicate) that new methodology. 

Stay tuned for next week’s ThursdAI, where we’ll hopefully see new updates from OpenAI (maybe O3-Mini?), plus the ongoing race for best agent. Also, catch us at [AI.engineer](AI.engineer) in NYC if you want to talk shop or share your own open-source success stories. Until then, keep calm and carry on training.

TLDR

* **Open Source LLMs**

* DeepSeek Crashes the Stock Market: Did $5.5M training or hype do it?

* Open Thoughts Reasoning Dataset OpenThoughts-114k ([X](https://x.com/madiator/status/1884284103354376283), [HF](https://t.co/MUAJd9mWZD))

* Mistral Small 2501 (24B, Apache 2.0) ([HF](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501))

* Berkeley TinyZero & RAGEN (R1-Zero Replications) ([Github](https://app.reflect.app/g/altryne/github.com/Jiayi-Pan/TinyZero), [WANDB](https://app.reflect.app/g/altryne/wandb.ai/jiayipan/TinyZero))

* Allen Institute - Tulu 405B ([Blog](https://allenai.org/blog/tulu-3-405B), [HF](https://huggingface.co/collections/allenai/tulu-3-models-673b8e0dc3512e30e7dc54f5))

* **Agents**

* Goose by Blocks (local agent framework) - ([X](https://x.com/blocks/status/1884292904753254488), [Github](https://block.github.io/goose/))

* Operator (OpenAI) – One-Week-In ([X](https://x.com/altryne/status/1883056651332448761))

* Browser-use - oss version of Operator ([Github](https://github.com/browser-use/browser-use))

* **Big CO LLMs + APIs**

* Alibaba Qwen2.5-Max (+ hidden video model) - ([X](https://x.com/Alibaba_Qwen/status/1884263157574820053), [Try it](https://chat.qwenlm.ai/))

* Zuckerberg on LLama4 & “Reasoning Model” ([X](https://x.com/altryne/status/1884778839009796411))

* **This Week’s Buzz**

* Shawn Lewis [interview](https://x.com/latentspacepod/status/1884065983062761548) on [Latent Space](https://open.substack.com/pub/swyx) with [swyx & Alessio](https://substack.com/profile/89230629-swyx-and-alessio) 

* We’re sponsoring the [ai.engineer](https://ai.engineer) upcoming summit in NY (Feb 19-22), come say hi! 

* After that, we’ll host 2 workshops with AI Tinkerers Toronto (Feb 23-24), make sure you’re signed up to [Toronto Tinkerers](https://toronto.aitinkerers.org/) to receive the invite (we were sold out quick last time!) 

* **Vision & Video**

* DeepSeek Janus Pro - 1.5B and 7B ([Github](https://github.com/deepseek-ai/Janus/tree/main?tab=readme-ov-file), [Try It](https://huggingface.co/spaces/AP123/Janus-Pro-7b))

* NVIDIA Eagle 2 ([Paper](http://arxiv.org/abs/2501.14818), [Model](https://huggingface.co/collections/nvidia/eagle-2-6764ba887fa1ef387f7df067), [Demo](https://eagle-vlm.xyz/))

* Alibaba Qwen 2.5 VL  ([Project](https://qwenlm.github.io/blog/qwen2.5-vl/), [HF](huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct), [Github](https://github.com/QwenLM/Qwen2.5-VL), [Try It](https://chat.qwenlm.ai/))

* **Voice & Audio**

* Yue 7B (Open Suno) - ([Demo](https://fal.ai/models/fal-ai/yue/requests), [HF](https://huggingface.co/m-a-p), [Github](https://github.com/multimodal-art-projection/YuE))

* Refusion Fuzz ([free for now](https://refusion.ai/fuzz))

* **Tools**

* Perplexity with R1 (choose Pro with R1) 

* Exa integrated R1 for free ([demo](https://demo.exa.ai/deepseekchat))

* **Participants**

* Alex Volkov ([@altryne](https://x.com/altryne))

* Wolfram Ravenwolf ([@WolframRvnwlf](https://x.com/WolframRvnwlf))

* Nisten Tahiraj ([@nisten](https://x.com/nisten/) )

* LDJ ([@ldjOfficial](https://x.com/ldjconfirmed/status/1884678546431373764))

* Simon Willison ([@simonw](https://x.com/simonw/status/1882507741694189706))

* W&B Weave ([@weave_wb](https://x.com/weave_wb)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jan-30-deepseek-vs-nasdaq/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jan-30-deepseek-vs-nasdaq?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1NjEyNjk2MCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.6QbGf5tubwVSCAodCc00_jOtQGVlb4gREqUbWTum14c&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Jan 23, 2025 - 🔥 DeepSeek R1 is HERE, OpenAI Operator Agent, $500B AI manhattan project, ByteDance UI-Tars, new Gemini Thinker & more AI news

**Date:** January 24, 2025  
**Duration:** 1:49:39  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1](https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1)

What a week, folks, what a week! Buckle up, because ThursdAI just dropped, and this one's a doozy. We're talking seismic shifts in the open source world, a potential game-changer from DeepSeek AI that's got everyone buzzing, and oh yeah, just a casual $500 BILLION infrastructure project announcement. Plus, OpenAI finally pulled the trigger on "Operator," their agentic browser thingy – though getting it to actually *operate* proved to be a bit of a live show adventure, as you'll hear. 

This week felt like one of those pivotal moments in AI, a real before-and-after kind of thing. DeepSeek's R1 hit the open source scene like a supernova, and suddenly, top-tier reasoning power is within reach for anyone with a Mac and a dream. And then there's OpenAI's Operator, promising to finally bridge the gap between chat and action. Did it live up to the hype? Well, let's just say things got interesting.

As I’m writing this, White House just published that an Executive Order on AI was just signed and published as well, what a WEEK.

Open Source AI Goes Nuclear: DeepSeek R1 is HERE!

Hold onto your hats, open source AI just went supernova! This week, the Chinese Whale Bros – DeepSeek AI, that quant trading firm turned AI powerhouse – dropped a bomb on the community in the best way possible: **R1, their reasoning model, is now open source under the MIT license!** As I said on the show, "Open source AI has never been as hot as this week."

This isn't just *a* model, folks. DeepSeek unleashed a whole arsenal: two full-fat R1 models (DeepSeek R1 and DeepSeek R1-Zero), and a whopping six distilled finetunes based on Qwen (1.5B, 7B, 14B, and 32B) and Llama (8B, 72B). 

One stat that blew my mind, and Nisten's for that matter, is that **DeepSeek-R1-Distill-Qwen-1.5B, the *****tiny***** 1.5 billion parameter model, is outperforming GPT-4o and Claude-3.5-Sonnet on math benchmarks!** "This 1.5 billion parameter model that now does this. It's absolutely insane," I exclaimed on the show. We're talking 28.9% on AIME and 83.9% on MATH. Let that sink in. A model you can probably run on your phone is schooling the big boys in math.

License-wise, it's MIT, which as Nisten put it, "MIT is like a jailbreak to the whole legal system, pretty much. That's what most people don't realize. It's like, this is, it's not my problem. You're a problem now." Basically, do whatever you want with it. Distill it, fine-tune it, build Skynet – it's all fair game.

And the vibes? "Vibes are insane," as I mentioned on the show. Early benchmarks are showing R1 models trading blows with o1-preview and o1-mini, and even nipping at the heels of the full-fat o1 in some areas. Check out these numbers:

And the price? Forget about it. We're talking 50x cheaper than o1 currently. DeepSeek R1 API is priced at $0.14 / 1M input tokens and $2.19 / 1M output tokens, compared to OpenAI's o1 at $15.00 / 1M input and a whopping $60.00 / 1M output. Suddenly, high-quality reasoning is democratized.

LDJ highlighted the "aha moment" in DeepSeek's paper, where they talk about how reinforcement learning enabled the model to re-evaluate its approach and "think more." It seems like simple RL scaling, combined with a focus on reasoning, is the secret sauce. No fancy Monte Carlo Tree Search needed, apparently!

But the real magic of open source is what the community does with it. Pietro Schirano joined us to talk about his "Retrieval Augmented Thinking" (RAT) approach, where he extracts the thinking process from R1 and transplants it to other models. "And what I found out is actually by doing so, you may even like smaller, quote unquote, you know, less intelligent model actually become smarter," Pietro explained. Frankenstein models, anyone? (John Lindquist has a tutorial on how to do it [here](https://egghead.io/combine-deep-seek-r1-reasoning-with-gpt-3-5-turbo-for-the-cheapest-fastest-and-best-ai~24oy1))

And then there's the genius hack from Voooogel, who figured out how to emulate a "reasoning_effort" knob by simply replacing the "end" token with "Wait, but".  "This tricks the model into keeps thinking," as I described it. Want your AI to really ponder the meaning of life (or just 1+1)? Now you can, thanks to open source tinkering.

Georgi Gerganov, the legend behind llama.cpp, even jumped in with a two-line snippet to enable speculative decoding, boosting inference speeds on the 32B model on my Macbook from a sluggish 5 tokens per second to a much more respectable 10-11 tokens per second. Open source collaboration at its finest and it's only going to get better! 

Thinking like a Neurotic

Many people really loved the way R1 thinks, and what I found astonishing is that I just sent "hey" and the thinking went into a whole 5 paragraph debate of how to answer, a user on X answered with "this is Woody Allen-level of Neurotic" which... nerd sniped me so hard! I used Hauio Audio (which is great!) and ByteDance latentSync and gave R1 a voice! It's really something when you hear it's inner monologue being spoken out like this! 

ByteDance Enters the Ring: UI-TARS Controls Your PC

Not to be outdone in the open source frenzy, ByteDance, the TikTok behemoth, dropped UI-TARS, a set of models designed to control your PC. And they claim SOTA performance, beating even Anthropic's computer use models and, in some benchmarks, GPT-4o and Claude.

UI-TARS comes in 2B, 7B, and 72B parameter flavors, and ByteDance even released desktop apps for Mac and PC to go along with them. "They released an app it's called the UI TARS desktop app. And then, this app basically allows you to Execute the mouse clicks and keyboard clicks," I explained during the show.

While I personally couldn't get the desktop app to work flawlessly (quantization issues, apparently), the potential is undeniable. Imagine open source agents controlling your computer – the possibilities are both exciting and slightly terrifying. As Nisten wisely pointed out, "I would use another machine. These things are not safe to tell people. I might actually just delete your data if you, by accident." Words to live by, folks.

LDJ chimed in, noting that UI-TARS seems to excel particularly in operating system-level control tasks, while OpenAI's leaked "Operator" benchmarks might show an edge in browser control. It's a battle for desktop dominance brewing in open source!

Noting that the common benchmark between Operator and UI-TARS is OSWorld, UI-Tars launched with a SOTA 

Humanity's Last Exam: The Benchmark to Beat

Speaking of benchmarks, a new challenger has entered the arena: **Humanity's Last Exam (HLE).** A cool new unsaturated bench of 3,000 *challenging* questions across over a hundred subjects, crafted by nearly a thousand subject matter experts from around the globe. "There's no way I'm answering any of those myself. I need an AI to help me," I confessed on the show.

And guess who's already topping the HLE leaderboard? You guessed it: **DeepSeek R1, with a score of 9.4%!** "Imagine how hard this benchmark is if the top reasoning models that we have right now... are getting less than 10 percent completeness on this," MMLU and Math are getting saturated? HLE is here to provide a serious challenge. Get ready to hear a lot more about HLE, folks.

Big CO LLMs + APIs: Google's Gemini Gets a Million-Token Brain

While open source was stealing the show, the big companies weren't completely silent. Google quietly dropped an update to **Gemini Flash Thinking**, their experimental reasoning model, and it's a big one. We're talking **1 million token context window** and code execution capabilities now baked in!

"This is Google's scariest model by far ever built ever," Nisten declared. "This thing, I don't like how good it is. This smells AGI-ish" High praise, and high concern, coming from Nisten! Benchmarks are showing significant performance jumps in math and science evals, and the speed is, as Nisten put it, "crazy usable." They have enabled the whopping 1M context window for the new Gemini Flash 2.0 Thinking Experimental (long ass name, maybe let's call it G1?) and I agree, it's really really good!

And unlike some other reasoning models *cough* OpenAI *cough*, Gemini Flash Thinking **shows you its thinking process!** You can actually see the chain of thought unfold, which is incredibly valuable for understanding and debugging. Google's Gemini is quietly becoming a serious contender in the reasoning race (especially with Noam Shazeer being responsible for it!)

OpenAI's "Operator" - Agents Are (Almost) Here

The moment we were all waiting for (or at least, *I* was): OpenAI finally unveiled **Operator**, their first foray into Level 3 Autonomy - agentic capabilities with ChatGPT. Sam Altman himself hyped it up as "AI agents are AI systems that can do work for you. You give them a task and they go off and do it." Sounds amazing, right?

Operator is built on a new model called **CUA (Computer Using Agent)**, trained on top of GPT-4, and it's designed to control a web browser in the cloud, just like a human would, using screen pixels, mouse, and keyboard. "This is just using screenshots, no API, nothing, just working," one of the OpenAI presenters emphasized. 

They demoed Operator booking restaurant reservations on OpenTable, ordering groceries on Instacart, and even trying to buy Warriors tickets on StubHub (though that demo got a little… glitchy). The idea is that you can delegate tasks to Operator, and it'll go off and handle them in the background, notifying you when it needs input or when the task is complete.

As I'm writing these words, I have an Operator running trying to get me some fried rice, and another one trying to book me a vacation with kids over the summer, find some options and tell me what it found. 

Benchmarks-wise, OpenAI shared numbers for OSWorld (38.1%) and WebArena (58.1%), showing Operator outperforming previous SOTA but still lagging behind human performance. "Still a way to go," as they admitted. But the potential is massive.

The catch? **Operator is initially launching in the US for Pro users only, and even *****then*****, it wasn't exactly smooth sailing.** I immediately paid the $200/mo to try it out (pro mode didn't convince me, unlimited SORA videos didn't either, operator definitely did, SOTA agents from OpenAI is definitely something I must try!) and my first test? Writing a tweet 😂 Here's a video of that first attempt, which I had to interrupt 1 time. 

But hey, it's a "low key research preview" right? And as Sam Altman said, "This is really the beginning of this product. This is the beginning of our step into Agents Level 3 on our tiers of AGI" Agentic ChatGPT is coming, folks, even if it's taking a slightly bumpy route to get here.

BTW, while I'm writing these words, Operator is looking up some vacation options for me and is sending me notifications about them, what a world and we've only just started 2025!

Project Stargate: $500 Billion for AI Infrastructure

If R1 and Operator weren't enough to make your head spin, how about a **$500 BILLION "Manhattan Project for AI infrastructure"?** That's exactly what OpenAI, SoftBank, and Oracle announced this week: [**Project Stargate**](https://openai.com/index/announcing-the-stargate-project/)**.**

"This is insane," I exclaimed on the show. "Power ups for the United States compared to like, other, other countries, like 500 billion commitment!" We're talking about a massive investment in data centers, power plants, and everything else needed to fuel the AI revolution. 2% of the US GDP, according to some estimates!

Larry Ellison even hinted at using this infrastructure for… curing cancer with personalized vaccines. Whether you buy into that or not, the scale of this project is mind-boggling. As LDJ explained, "It seems like it is very specifically for open AI. Open AI will be in charge of operating it. And yeah, it's, it sounds like a smart way to actually kind of get funding and investment for infrastructure without actually having to give away open AI equity."

And in a somewhat related move, Microsoft, previously holding exclusive cloud access for OpenAI, has opened the door for OpenAI to potentially run on other clouds, with Microsoft's approval if "they cannot meet demant".  Is AGI closer than we think? Sam Altman himself downplayed the hype, tweeting, "Twitter hype is out of control again. We're not going to deploy AGI next month, nor have we built it. We have some very cool stuff for you, but please chill and cut your expectations a hundred X."

But then he drops Operator and a $500 billion infrastructure bomb in the same week and announces that o3-mini is going to be available for the FREE tier of chatGPT.

Sure, Sam, *we're going to chill... yeah right. *

This Week's Buzz at Weights & Biases: SWE-bench SOTA!

Time for our weekly dose of Weights & Biases awesomeness! This week, our very own CTO, Shawn Lewis, **broke the SOTA on SWE-bench Verified!** That's right, W&B Programmer, Shawn's agentic framework built on top of o1, achieved a **64.6%** solve rate on this notoriously challenging coding benchmark.

Shawn detailed his journey in a [blog post](https://wandb.ai/wandb/agents/reports/Creating-a-state-of-the-art-AI-programming-agent-with-OpenAI-s-o1--VmlldzoxMTAyODI2Ng?utm_source=thursdai&utm_medium=referral&utm_campaign=Jan9), highlighting the importance of iteration and evaluation – powered by Weights & Biases [Weave](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=jan23), naturally. He ran over 1000 evaluations to reach this SOTA result! Talk about eating your own dogfood!

REMOVING BARRIERS TO AMERICAN LEADERSHIP IN ARTIFICIAL INTELLIGENCE - Executive order

Just now as I’m editing the podcast, President Trump signed into effect an executive order for AI, and here are the highlights. 

- Revokes existing AI policies that hinder American AI innovation

- Aims to solidify US as global leader in AI for human flourishing, competitiveness, and security

- Directs development of an AI Action Plan within 180 days

- Requires immediate review and revision of conflicting policies

- Directs OMB to revise relevant memos within 60 days

- Preserves agency authority and OMB budgetary functions

- Consistent with applicable law and funding availability

- Seeks to remove barriers and strengthen US AI dominance

This marks such a significant pivot into AI acceleration, removing barriers, acknowledging that AI is a huge piece of our upcoming future and that US really needs to innovate here, become the global leader, and remove regulation and obstacles. The folks that work on this behind the scenes, Sriram Krishan (previously A16Z) and David Sacks, are starting to get into the government and implement those policies, so we’re looking forward to what will come form that! 

Vision & Video: Nvidia's Vanishing Eagle 2 & Hugging Face's Tiny VLM

In the world of vision and video, Nvidia teased us with **Eagle 2**, a series of frontier vision-language models promising 4K HD input, long-context video, and grounding capabilities with some VERY impressive evals. Weights were released, then…yanked. "NVIDIA released Eagle 2 and then yanked it back. So I don't know what's that about," I commented. Mysterious Nvidia strikes again.

On the brighter side, Hugging Face released **SmolVLM**, a truly *tiny* vision-language model, coming in at just 256 million and 500 million parameters. "This tiny model that runs in like one gigabyte of RAM or some, some crazy things, like a smart fridge" I exclaimed, impressed. The 256M model even outperforms their previous 80 *billion* parameter Idefics model from just 17 months ago. Progress marches on, even in tiny packages.

AI Art & Diffusion & 3D: Hunyuan 3D 2.0 is State of the Art

For the artists and 3D enthusiasts, Tencent's **Hunyuan 3D 2.0** dropped this week, and it's looking seriously impressive. "Just look at this beauty," I said, showcasing a generated dragon skull. "Just look at this."

Hunyuan 3D 2.0 boasts two models: Hunyuan3D-DiT-v2-0 for shape generation and Hunyuan3D-Paint-v2-0 for coloring. Text-to-3D and image-to-3D workflows are both supported, and the results are, well, see for yourself:

If you're looking to move beyond 2D images, Hunyuan 3D 2.0 is definitely worth checking out.

Tools: ByteDance Clones Cursor with Trae

And finally, in the "tools" department, ByteDance continues its open source blitzkrieg with **Trae**, a free Cursor competitor. "ByteDance drops Trae, which is a cursor competitor, which is free for now" I announced on the show, so if you don't mind your code being sent to... china somewhere, and can't afford Cursor, this is not a bad alternative! 

Trae imports your Cursor configs, supports Claude 3.5 and GPT-4o, and offers a similar AI-powered code editing experience, complete with chat interface and "builder" (composer) mode. The catch? Your code gets sent to a server in China. If you're okay with that, you've got yourself a free Cursor alternative. "If you're okay with your like code getting shared with ByteDance, this is a good option for you," I summarized. Decisions, decisions.

Phew! That was a whirlwind tour through another insane week in AI. From DeepSeek R1's open source reasoning revolution to OpenAI's Operator going live, and Google's million-token Gemini brain, it's clear that the pace of innovation is showing no signs of slowing down. 

Open source is booming, agents are inching closer to reality, and the big companies are throwing down massive infrastructure investments. We're accelerating as fuck, and it's only just beginning, hold on to your butts.

Make sure to dive into the show notes below for all the links and details on everything we covered. And don't forget to give R1 a spin – and maybe try out that "reasoning_effort" hack. Just don't blame me if your AI starts having an existential crisis.

And as a final thought, channeling my inner Woody Allen-R1, "Don't overthink too much. enjoy our one. Enjoy the incredible things we received this week from open source."

See you all next week for more ThursdAI madness! And hopefully, by then, Operator will actually be operating. 😉

TL;DR and show notes

* **Open Source LLMs**

* DeepSeek R1 - MIT licensed SOTA open source reasoning model ([HF](https://huggingface.co/deepseek-ai), X)

* ByteDance UI-TARS - PC control models ([HF](https://huggingface.co/bytedance-research/UI-TARS-7B-SFT), [Github](https://github.com/bytedance/UI-TARS-desktop) )

* HLE - Humanity's Last Exam benchmark ([Website](https://lastexam.ai/))

* **Big CO LLMs + APIs**

* SoftBank, Oracle, OpenAI Stargate Project - $500B AI infrastructure ([OpenAI Blog](https://openai.com/index/announcing-the-stargate-project/))

* Google Gemini Flash Thinking 01-21 - 1M context, Code execution, Better Evals ([X](https://x.com/NoamShazeer/status/1881845900659896773))

* OpenAI Operator - Agentic browser in ChatGPT Pro [operator.chatgpt.com](operator.chatgpt.com)

* Anthropic launches citations in API ([blog](https://docs.anthropic.com/en/docs/build-with-claude/citations))

* Perplexity SonarPRO Search API and an Android AI assistant ([X](https://x.com/perplexity_ai/status/1882466239123255686))

* **This weeks Buzz 🐝**

* W&B broke SOTA SWE-bench verified ([W&B Blog](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=jan23))

* **Vision & Video**

* HuggingFace SmolVLM - Tiny VLMs - runs even on WebGPU ([HF](https://huggingface.co/spaces/HuggingFaceTB/SmolVLM-256M-Instruct-WebGPU))

* **AI Art & Diffusion & 3D**

* Hunyuan 3D 2.0 - SOTA open-source 3D ([HF](https://huggingface.co/tencent/Hunyuan3D-2))

* **Tools**

* ByteDance Trae - Cursor competitor (Trae AI: [https://trae.ai/)](https://trae.ai/))

* **Show Notes:** 

* Pietro Skirano RAT - Retrieval augmented generation ([X](https://x.com/skirano/status/1881854481304047656))

* Run DeepSeek with more “thinking” script ([Gist](https://gist.github.com/vgel/8a2497dc45b1ded33287fa7bb6cc1adc)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jan-23-2025-deepseek-r1?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1NTU3ODcxNCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.InT8qY8h5BoTDaMj-TtHYB8zDF9RhzZjEeWZtjRI5sI&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Jan 16, 2025 - Hailuo 4M context LLM, SOTA TTS in browser, OpenHands interview & more AI news

**Date:** January 17, 2025  
**Duration:** 1:40:32  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-16-2025-hailuo-4m-context](https://sub.thursdai.news/p/thursdai-jan-16-2025-hailuo-4m-context)

Hey everyone, Alex here 👋 

Welcome back, to an absolute banger of a week in AI releases, highlighted with just massive Open Source AI push. We're talking a MASSIVE 4M context window context window model from Hailuo (remember when a jump from 4K to 16K seemed like a big deal?), a 8B omni model that lets you livestream video and glimpses of Agentic ChatGPT? 

This week's ThursdAI was jam-packed with so much open source goodness that the big companies were practically silent. But don't worry, we still managed to squeeze in some updates from OpenAI and Mistral, along with a fascinating new paper from Sakana AI on self-adaptive LLMs. Plus, we had the incredible Graham Neubig, from All Hands AI, join us to talk about Open Hands (formerly OpenDevin) and even contributed to our free, LLM Evaluation course on Weights & Biases!

Before we dive in, a friend asked me over dinner, what are the main 2 things that happened in AI in 2024, and this week highlights one of those trends. Most of the Open Source is now from China. This week, we got MiniMax from Hailuo, OpenBMB with a new MiniCPM, InternLM came back and most of the rest were Qwen finetunes. Not to mention DeepSeek. Wanted to highlight this significant narrative change and that this is being done despite the chip export restrictions. 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Open Source AI & LLMs

MiniMax-01: 4 Million Context, 456 Billion Parameters, and Lightning Attention 

This came absolutely from the left field, given that we've seen no prior LLMs from Haulio, the company previously releasing video models with consistent characters. Dropping a massive 456B mixture of experts model (45B active parameters) with such a long context support in open weights, but also with very significant benchmarks that compete with Gpt-4o, Claude and DeekSeek v3 (75.7 MMLU-pro, 89 IFEval, 54.4 GPQA)

They have trained the model on up to 1M context window and then extended it to 4M with ROPE scaling methods ([our coverage](https://sub.thursdai.news/p/thursdai-sunday-special-extending?utm_source=publication-search) of RoPE) during Inference. MiniMax-Text-01 adopts a hybrid architecture that combines Lightning Attention, Softmax Attention and Mixture-of-Experts (MoE) with 45B active parameters. 

I gotta say, when we started talking about context window, imagining a needle in a haystack graph that shows 4M, in the open source seemed far fetched, though we did say that theoretically, there may not be a limit to context windows. I just always expected that limit to be unlocked by transformers alternative architectures like Mamba or other State Space Models.

Vision, API and Browsing - Minimax-VL-01

It feels like such a well rounded and complete release, that it highlights just how mature company that is behind it. They have also released a vision version of this model, that includes a 300M param Vision Transformer on top (trained with 512B vision language tokens) that features dynamic resolution and boasts very high DocVQA and ChartQA scores. 

Not only did these two models were released in open weights, they also launched as a unified API endpoint (supporting up to 1M tokens) and it's  cheap! $0.2/1M input and $1.1/1M output tokens! AFAIK this is only the 3rd API that supports this much context, after Gemini at 2M and Qwen Turbo that supports 1M as well.

Surprising web browsing capabilities

You can play around with the model on their website, [hailuo.ai](https://www.hailuo.ai) which also includes web grounding, which I found quite surprising to find out, that they are beating chatGPT and Perplexity on how fast they can find information that just happened that same day! Not sure what search API they are using under the hood but they are very quick. 

8B chat with video model omni-model from OpenBMB

OpenBMB has been around for a while and we've seen consistently great updates from them on the MiniCPM front, but this one takes the cake! 

This is a complete omni modal end to end model, that does video streaming, audio to audio and text understanding, all on a model that can run on an iPad! 

They have a demo interface that is very similar to the chatGPT demo from spring of last year, and allows you to stream your webcam and talk to the model, but this is just an 8B parameter model we're talking about! It's bonkers! 

They are boasting some incredible numbers, and to be honest, I highly doubt  their methodology in textual understanding, because, well, based on my experience alone, this model understands less than close to chatGPT advanced voice mode, but miniCPM has been doing great visual understanding for a while, so ChartQA and DocVQA are close to SOTA. 

But all of this doesn't matter, because, I say again, just a little over a year ago, Google released a video announcing these capabilities, having an AI react to a video in real time, and it absolutely blew everyone away, and it was [FAKED](https://techcrunch.com/2023/12/07/googles-best-gemini-demo-was-faked/). And this time a year after, we have these capabilities, essentially, in an 8B model that runs on device 🤯 

Voice & Audio 

This week seems to be very multimodal, not only did we get an omni-modal from OpenBMB that can speak, and last week's Kokoro still makes a lot of waves, but this week there were a lot of voice updates as well

Kokoro.js - run the SOTA open TTS now in your browser

Thanks to friend of the pod Xenova (and the fact that Kokoro was released with ONNX weights), we now have kokoro.js, or npm -i kokoro-js if you will. 

This allows you to install and run Kokoro, the best tiny TTS model, completely within your browser, with a tiny 90MB download and it sounds really good (demo [here](https://huggingface.co/spaces/webml-community/kokoro-web))

Hailuo T2A - Emotional text to speech + API 

Hailuo didn't rest on their laurels of releasing a huge context window LLM, they also released a new voice framework (tho not open sourced) this week, and it sounds remarkably good (competing with 11labs) 

They have all the standard features like Voice Cloning, but claim to have a way to preserve the emotional undertones of a voice. They also have 300 voices to choose from and professional effects applied on the fly, like acoustics or telephone filters. (Remember, they have a video model as well, so assuming that some of this is to for the holistic video production) 

What I specifically noticed is their "emotional intelligence system" that's either automatic or can be selected from a dropdown. I also noticed their "lax" copyright restrictions, as one of the voices that was called "Imposing Queen" sounded just like a certain blonde haired heiress to the iron throne from a certain HBO series. 

When I generated a speech worth of that queen, I noticed that the emotion in that speech sounded very much like an actress would read them, and unlike any old TTS, just listen to it in the clip above, I don't remember getting TTS outputs with this much emotion from anything, maybe outside of advanced voice mode! Quite impressive!

This Weeks Buzz from Weights & Biases - AGENTS!

Breaking news from W&B as our CTO [just broke](https://x.com/shawnup/status/1880004026957500434) SWE-bench Verified SOTA, with his own o1 agentic framework he calls W&B Programmer 😮 at **64.6% **of the issues!

Shawn describes how he achieved this massive breakthrough [here](https://medium.com/@shawnup/the-best-ai-programmer-from-weights-biases-04cf8127afd8) and we'll be publishing more on this soon, but the highlight for me is he ran over 900 evaluations during the course of this, and tracked all of them in [Weave](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=Jan16)! 

We also have an upcoming event in NY, on Jan 22nd, if you're there, come by and learn how to evaluate your AI agents, RAG applications and hang out with our team! (Sign up [here](https://lu.ma/eufkbeem?utm_source=thursdai&utm_medium=referral&utm_campaign=Jan16))

Big Companies & APIs

OpenAI adds chatGPT tasks - first agentic feature with more to come! 

We finally get a glimpse of an agentic chatGPT, in the form of scheduled tasks! Deployed to all users, it is now possible to select gpt-4o with tasks, and schedule tasks in the future. 

You can schedule them in natural language, and then will execute a chat (and maybe perform a search or do a calculation) and then send you a notification (and an email!) when the task is done! 

A bit underwhelming at first, as I didn't really find a good use for this yet, I don't doubt that this is just a building block for something more Agentic to come that can connect to my email or calendar and do actual tasks for me, not just... save me from typing the chatGPT query at "that time" 

Mistral CodeStral 25.01 - a new #1 coding assistant model

An updated Codestral was released at the beginning of the week, and TBH I've never seen the vibes split this fast on a model. 

While it's super exciting that Mistral is placing a coding model at #1 on the LMArena CoPilot's arena, near Claude 3.5 and DeepSeek, the fact that this new model is not released weights is really a bummer (especially as a reference to the paragraph I mentioned on top) 

We seem to be closing down on OpenSource in the west, while the Chinese labs are absolutely crushing it (while also releasing in the open, including Weights, Technical papers). 

Mistral has released this model in API and via a collab with the Continue dot dev coding agent, but they used to be the darling of the open source community by releasing great models! 

Also notable, a very quick new benchmark post release was dropped that showed a significant difference between their reported benchmarks and how it performs on Aider polyglot 

There was way more things for this week than we were able to cover, including a new and exciting transformers squared new architecture from Sakana, a new open source TTS with voice cloning and a few other open source LLMs, one of which cost only $450 to train! All the links in the TL;DR below! 

TL;DR and show notes

* **Open Source LLMs** 

* MiniMax-01 from Hailuo - 4M context 456B (45B A) LLM ([Github](https://github.com/MiniMax-AI/MiniMax-01), [HF](https://huggingface.co/MiniMaxAI), [Blog](https://www.minimaxi.com/en/news/minimax-01-series-2), [Report](https://filecdn.minimax.chat/_Arxiv_MiniMax_01_Report.pdf))

* Jina - reader V2 model - HTML 2 Markdown/JSON ([HF](https://huggingface.co/jinaai/ReaderLM-v2))

* InternLM3-8B-Instruct - apache 2 License ([Github](https://github.com/InternLM/InternLM), [HF](https://huggingface.co/internlm))

* OpenBMB - **MiniCPM-o 2.6** - Multimodal Live Streaming on Your Phone ([HF](https://huggingface.co/openbmb/MiniCPM-o-2_6), [Github](https://github.com/OpenBMB/MiniCPM-o), [Demo](https://minicpm-omni-webdemo-us.modelbest.cn/))

* KyutAI - Helium-1 2B - Base ([X](https://x.com/kyutai_labs/thread/1878857673174864318), [HF](https://huggingface.co/kyutai/helium-1-preview-2b))

* Dria-Agent-α - 3B model that outputs python code ([HF](https://huggingface.co/driaforall/Dria-Agent-a-3B))

* Sky-T1, a ‘reasoning’ AI model that can be trained for less than $450 ([blog](https://novasky-ai.github.io/posts/sky-t1/))

* **Big CO LLMs + APIs**

* OpenAI launches ChatGPT tasks ([X](https://x.com/OpenAI/status/1879267274185756896))

* Mistral - new CodeStral 25.01 ([Blog](https://mistral.ai/news/codestral-2501/), no Weights)

* Sakana AI - Transformer²: Self-Adaptive LLMs ([Blog](https://sakana.ai/transformer-squared))

* **This weeks Buzz **

* Evaluating RAG Applications Workshop - NY, Jan 22, W&B and PineCone ([Free Signup](https://lu.ma/eufkbeem))

* Our evaluations course is going very strong! (chat w/ Graham Neubig) ([https://wandb.me/evals-t](https://wandb.me/evals-t))

* **Vision & Video**

* Luma releases Ray2 video model ([Web](https://lumalabs.ai/ray))

* **Voice & Audio**

* Hailuo **T2A-01-HD** - Emotions Audio Model from Hailuo ([X](https://x.com/Hailuo_AI/status/1879554062993195421), [Try It](https://t.co/r58fjgvJ7w))

* OuteTTS 0.3 - 1B & 500M - zero shot voice cloning model ([HF](https://huggingface.co/collections/OuteAI/outetts-03-6786b1ebc7aeb757bc17a2fa))

* Kokoro.js - 80M SOTA TTS in your browser! (X, [Github](https://github.com/hexgrad/kokoro/pull/3), [try it](https://huggingface.co/spaces/webml-community/kokoro-web) )

* **AI Art & Diffusion & 3D**

* Black Forest Labs - Finetuning for Flux Pro and Ultra via API ([Blog](https://blackforestlabs.ai/announcing-the-flux-pro-finetuning-api/))

* **Show Notes and other Links**

* Hosts - Alex Volkov ([@altryne](https://x.com/altryne)), Wolfram RavenWlf ([@WolframRvnwlf](https://twitter.com/WolframRvnwlf)), Nisten Tahiraj ([@nisten](https://x.com/nisten/))

* Guest - Graham Neubig ([@gneubig](https://x.com/gneubig)) from All Hands AI ([@allhands_ai](https://x.com/allhands_ai))

* Graham’s mentioned Agents blogpost - 8 things that agents can do right [now](https://www.all-hands.dev/blog/8-use-cases-for-generalist-software-development-agents)

* Projects - Open Hands (previously Open Devin) - [Github](https://github.com/All-Hands-AI/OpenHands)

* Germany meetup in Cologne ([here](https://twitter.com/WolframRvnwlf/status/1877338980632383713))

* Toronto Tinkerer Meetup *Sold OUT* ([Here](https://toronto.aitinkerers.org/p/ai-tinkerers-toronto-january-2025-meetup-at-google))

* YaRN conversation we had with the Authors ([coverage](https://sub.thursdai.news/p/thursdai-sunday-special-extending?utm_source=publication-search))

See you folks next week! Have a great long weekend if you’re in the US 🫡 

Please help to promote the podcast and newsletter by sharing with a friend!

 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jan-16-2025-hailuo-4m-context/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jan-16-2025-hailuo-4m-context?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1NDk4NjQ5MywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.dhVHbEk4Kb2DLfejXT5cpNzGqSQ8lgTvCGBQSVFaFR0&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Jan 9th - NVIDIA's Tiny Supercomputer, Phi-4 is back, Kokoro TTS & Moondream gaze, ByteDance SOTA lip sync & more AI news

**Date:** January 10, 2025  
**Duration:** 1:20:26  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-9th-nvidias-tiny-supercomputer](https://sub.thursdai.news/p/thursdai-jan-9th-nvidias-tiny-supercomputer)

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

---

## 📆 ThursdAI - Jan 2 - is 25' the year of AI agents?

**Date:** January 02, 2025  
**Duration:** 1:31:29  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-2-is-25-the-year-of](https://sub.thursdai.news/p/thursdai-jan-2-is-25-the-year-of)

Hey folks, Alex here 👋 Happy new year!

On our first episode of this year, and the second quarter of this century, there wasn't a lot of AI news to report on (most AI labs were on a well deserved break). So this week, I'm very happy to present a special ThursdAI episode, an interview with [Joāo Moura](https://x.com/joaomdmoura), CEO of [Crew.ai](http://Crew.ai) all about AI agents!

We first chatted with Joāo a [year ago](https://sub.thursdai.news/p/jan14-sunday-special-deep-dives), back in January of 2024, as CrewAI was blowing up but still just an open source project, it got to be the number 1 trending project on Github, and #1 project on Product Hunt. (You can either listen to the podcast or watch it in the embedded Youtube above)

00:36 Introduction and New Year Greetings

02:23 Updates on Open Source and LLMs

03:25 Deep Dive: AI Agents and Reasoning

03:55 Quick TLDR and Recent Developments

04:04 Medical LLMs and Modern BERT

09:55 Enterprise AI and Crew AI Introduction

10:17 Interview with João Moura: Crew AI

25:43 Human-in-the-Loop and Agent Evaluation

33:17 Evaluating AI Agents and LLMs

44:48 Open Source Models and Fin to OpenAI

45:21 Performance of Claude's Sonnet 3.5

48:01 Different parts of an agent topology, brain, memory, tools, caching

53:48 Tool Use and Integrations

01:04:20 Removing LangChain from Crew

01:07:51 The Year of Agents and Reasoning

01:18:43 Addressing Concerns About AI

01:24:31 Future of AI and Agents

01:28:46 Conclusion and Farewell

---

Is 2025 "the year of AI agents"?

AI agents as I remember them as a concept started for me a few month after I started ThursdAI ,when AutoGPT exploded. Was such a novel idea at the time, run LLM requests in a loop,

(In fact, back then, I came up with a retry with AI concept and called it [TrAI/Catch](https://x.com/altryne/status/1632253117827010566), where upon an error, I would feed that error back into the GPT api and ask it to correct itself. it feels so long ago!)

AutoGPT became the fastest ever Github project to reach 100K stars, and while exciting, it did not work.

Since then we saw multiple attempts at agentic frameworks, like babyAGI, autoGen. Crew AI was one of them that keeps being the favorite among many folks.

So, what is an AI agent? Simon Willison, friend of the pod, has a mission, to ask everyone who announces a new agent, what they mean when [they say it](https://x.com/simonw/status/1863567881553977819) because it seems that everyone "shares" a common understanding of AI agents, but it's different for everyone.

We'll start with Joāo's explanation and go from there. But let's assume the basic, it's a set of LLM calls, running in a self correcting loop, with access to planning, external tools (via function calling) and a memory or sorts that make decisions.

Though, as we go into detail, you'll see that since the very basic "run LLM in the loop" days, the agents in 2025 have evolved and have a lot of complexity.

My takeaways from the conversation

I encourage you to listen / watch the whole interview, Joāo is deeply knowledgable about the field and we go into a lot of topics, but here are my main takeaways from our chat

* Enterprises are adopting agents, starting with internal use-cases

* Crews have 4 different kinds of memory, Long Term (across runs), short term (each run), Entity term (company names, entities), pre-existing knowledge (DNA?)

* TIL about a "do all links respond with 200" guardrail

* Some of the agent tools we mentioned

* Stripe Agent API - for agent payments and access to payment data ([blog](https://stripe.dev/blog/adding-payments-to-your-agentic-workflows))

* Okta Auth for Gen AI - agent authentication and role management ([blog](https://www.auth0.ai/))

* E2B - code execution platform for agents ([e2b.dev](https://e2b.dev/))

* BrowserBase - programmatic web-browser for your AI agent

* Exa - search grounding for agents for real time understanding

* Crew has 13 crews that run 24/7 to automate their company

* Crews like Onboarding User Enrichment Crew, Meetings Prep, Taking Phone Calls, Generate Use Cases for Leads

* GPT-4o mini is the most used model for 2024 for CrewAI with main factors being speed / cost

* Speed of AI development makes it hard to standardize and solidify common integrations.

* Reasoning models like o1 still haven't seen a lot of success, partly due to speed, partly due to different way of prompting required.

This weeks Buzz

We've just opened up pre-registration for our upcoming FREE evaluations course, featuring Paige Bailey from Google and Graham Neubig from All Hands AI (previously Open Devin). We've distilled a lot of what we learned about evaluating LLM applications while building [Weave](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=jan2), our LLM Observability and Evaluation tooling, and are excited to share this with you all! [Get on the list](https://wandb.ai/site/courses/evals/?utm_source=thursdai&utm_medium=referral&utm_campaign=jan2)

Also, 2 workshops (also about Evals) from us are upcoming, one in SF on [Jan 11th](https://lu.ma/bzqvsqaa) and one in Seattle on [Jan 13th](https://seattle.aitinkerers.org/p/ai-in-production-evals-observability-workshop) (which I'm going to lead!) so if you're in those cities at those times, would love to see you!

And that's it for this week, there wasn't a LOT of news as I said. The interesting thing is, even in the very short week, the news that we did get were all about agents and reasoning, so it looks like 2025 is agents and reasoning, agents and reasoning!

See you all next week 🫡

TL;DR with links:

* **Open Source LLMs**

* HuatuoGPT-o1 - medical LLM designed for medical reasoning ([HF](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-8B), [Paper](https://huggingface.co/papers/2412.18925), [Github](https://github.com/FreedomIntelligence/HuatuoGPT-o1), [Data](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-verifiable-problem))

* Nomic - modernbert-embed-base - first embed model on top of modernbert ([HF](https://huggingface.co/nomic-ai/modernbert-embed-base))

* HuggingFace - SmolAgents lib to build agents ([Blog](https://huggingface.co/blog/smolagents))

* SmallThinker-3B-Preview - a QWEN 2.5 3B "reasoning" finetune ([HF](https://huggingface.co/PowerInfer/SmallThinker-3B-Preview))

* Wolfram new Benchmarks including DeepSeek v3 ([X](https://x.com/WolframRvnwlf/status/1874889165919384057))

* **Big CO LLMs + APIs**

* Newcomer Rubik's AI Sonus-1 family - Mini, Air, Pro and Reasoning ([X](https://x.com/RubiksAI/status/1874682159379972325), Chat)

* Microsoft "estimated" GPT-4o-mini is a ~8B ([X](https://x.com/Yuchenj_UW/status/1874507299303379428))

* Meta plans to bring AI profiles to their social networks ([X](https://x.com/petapixel/status/1874792802061844829))

* **This Week's Buzz**

* W&B Free Evals Course with Page Bailey and Graham Beubig - [Free Sign Up](https://wandb.ai/site/courses/evals/?utm_source=thursdai&utm_medium=referral&utm_campaign=jan2)

* SF evals event - [January 11th](https://lu.ma/bzqvsqaa)

* Seattle evals workshop - [January 13th](https://seattle.aitinkerers.org/p/ai-in-production-evals-observability-workshop) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jan-2-is-25-the-year-of/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jan-2-is-25-the-year-of?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE1NDAzMzY2MCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.-2FmmS8-Iq9rSNBzuyH2cjNrSPPkwegxbFjSP45EJLw&utm_campaign=CTA_5).

---

