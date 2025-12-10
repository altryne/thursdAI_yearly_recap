# ThursdAI Episodes - March 2025

Total Episodes: 4

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

