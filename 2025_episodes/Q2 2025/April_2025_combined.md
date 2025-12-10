# ThursdAI Episodes - April 2025

Total Episodes: 4

---

## ThursdAI - Apr 23rd - GPT Image & Grok APIs Drop, OpenAI ❤️ OS? Dia's Wild TTS & Building Better Agents!

**Date:** April 24, 2025  
**Duration:** 1:36:54  
**Link:** [https://sub.thursdai.news/p/thursdai-apr-23rd-gpt-image-and-grok](https://sub.thursdai.news/p/thursdai-apr-23rd-gpt-image-and-grok)

Hey everyone, Alex here 👋

Welcome back to ThursdAI! After what felt like ages of non-stop, massive model drops (looking at you, O3 and GPT-4!), we finally got that "chill week" we've been dreaming of since maybe... forever?  It seems the big labs are taking a breather, probably gearing up for even bigger things next week (maybe some open source 👀).

But "chill" doesn't mean empty! This week was packed with fascinating developments, especially in the open source world and with long-awaited API releases. We actually had *time* to dive deeper into things, which was a refreshing change. We had a fantastic lineup of guests joining us too: Kwindla Kramer ([@kwindla](https://twitter.com/kwindla/)), our resident voice expert, dropped in to talk about some mind-blowing TTS and her own open-source VAD release. Maziyar Panahi ([@MaziyarPanahi](https://x.com/MaziyarPanahi)) gave us the inside scoop on OpenAI's recent meeting with the open source community. And Dex Horthy ([@dexhorthy](https://x.com/dexhorthy)) from HumanLayer shared some invaluable insights on building robust AI agents that actually work in the real world. It was great having them alongside the usual ThursdAI crew: LDJ, Yam, Wolfram, and Nisten!

So, instead of rushing through a million headlines, we took a more relaxed pace. We explored NVIDIA's cool new Describe Anything model, dug into Google's Quantization Aware Training for Gemma, celebrated the much-anticipated API release for OpenAI's GPT Image generation (finally!), checked out the new Grok API, got absolutely blown away by a tiny, open-source TTS model from Korea called Dia, and debated the principles of building better AI agents. Plus, a surprise drop from Send AI with a powerful video model!

Let's dive in!

Open Source AI Highlights: Community, Vision, and Efficiency

Even with the big players quieter on the model release front, the open source scene was buzzing. It feels like this "chill" period gave everyone a chance to focus on refining tools, releasing datasets, and engaging with the community.

OpenAI Inches Closer to Open Source? Insights from the Community Meeting

Perhaps the biggest non-release news of the week was OpenAI actively engaging with the open source community. Friend of the show Maziyar Panahi was actually *in the room* (well, the Zoom room) and joined us to share what went down 

It sounds like OpenAI came prepared, with Sam Altman himself spending significant time answering questions . Maziyar gave us the inside scoop, mentioning that OpenAI's looking to offload some GPU pressure by embracing open source – a win-win where they help the community, and the community helps lighten their load. He painted a picture of a company genuinely trying to listen and figure out how to best contribute. It felt less like a checkbox exercise and more like genuine engagement, which is awesome to see.

What did the community ask for? Based on Maziyar's recap, there was a strong consensus on several key points:

* **Model Size:** The sweet spot seemed to be not tiny, but not astronomically huge either. Something in the **70B-200B parameter range** that could run reasonably on, say, 4 GPUs, leaving room for other models. People want power they can actually *use* without needing a supercomputer.

* **Capabilities:** A strong desire for reliable **structured output**. Surprisingly, there was *less* emphasis on complex, built-in reasoning, or at least the ability to **toggle reasoning off**. This likely stems from practical concerns about cost and latency in production environments. The community seems to value control and efficiency for specific tasks.

* **Multilingual:** Good support for **European languages (at least 20)** was a major request, reflecting the global nature of the open source community. Needs to be as good as English support.

* **Base Models:** A *huge* ask was for OpenAI to release **base models**. The reasoning? Empower the community to handle fine-tuning for specific tasks like coding, roleplay, or supporting underrepresented languages . Let the experts in those niches build on a solid foundation.

* **Focus:** **Usefulness over chasing leaderboard glory**. The community urged OpenAI to provide a solid, practical model rather than aiming for a temporary #1 spot that gets outdated in days or weeks . Stability, reliability, and long-term utility were prized over fleeting benchmark wins.

* **Safety:** A preference for **separate guardrail models** (similar to LlamaGuard or GemmaGuard) rather than overly aligning the main model, which often hurts performance and flexibility . Give users the tools to implement safety layers as needed, rather than baking in limitations that might stifle creativity or utility.

Perhaps most excitingly, Maziyar mentioned OpenAI seemed committed to **regular open model releases**, not just a one-off thin=! This, combined with recent moves like approving a community Pull Request to make their open-source Codex agent work with non-OpenAI models (as Yam Peleg excitedly pointed out!), suggests a potentially significant shift. Remember, it's been a *long* time since GPT-2 and Whisper were OpenAI's main open contributions! We're definitely watching this space closely. Huge shout out to OpenAI for listening and engaging with the builders.

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

NVIDIA's DAM: Describe Anything Model (and Dataset!)

NVIDIA dropped something really cool this week: the **Describe Anything Model (DAM)**, specifically DAM-3B, a 3 billion parameter multimodal model for region-based image *and* video captioning. Think Meta's Segment Anything (SAM), but instead of just segmenting, it also tells you *what* you've segmented, in detail.

We played around with the image demo on the show ([HF demo](https://huggingface.co/spaces/nvidia/describe-anything-model-demo)) . You hover over an image, things get segmented on the fly (you can use points, boxes, scribbles, or masks), you click, and boom – a detailed description pops up for that specific region: "A brown bear with a thick, dense coat of fur..." . It's pretty slick and responsive!

While the demo didn't showcase video, the project page ([X post](https://x.com/reach_vb/status/1914962078571356656)) shows it working on videos too (**DAM-3B-Video**), tracking and describing objects like fish even as they move. This capability really impressed Yam, who rightly pointed out that tracking objects consistently over video is *hard*, so having a base model that understands this level and embeds it in language is seriously impressive. The model uses a "focal prompt" and gated cross-attention to fuse the full scene context with the selected region.

Nisten  reminded us that our friend Piotr Skalski from Roboflow basically built a pipeline for this a while back by combining SAM with description models like Microsoft Florence . But DAM integrates it all into one efficient 3B parameter model ([HF model](https://huggingface.co/nvidia/DAM-3B)), setting a new state-of-the-art on their introduced **DLC-Bench** (Detailed Localized Captioning).

Crucially, NVIDIA didn't just drop the model; they also released the **Describe Anything Dataset** ([HF dataset](https://huggingface.co/datasets/nvidia/DescribeAnythingDataset)) used to train it (built on subsets like COCO, Paco, SAM) and the code under a research-only license. This is fantastic for researchers and builders. Imagine using this for precise masking before sending an image to the new GPT Image API for editing – super useful! Big props to NVIDIA and their collaborators at UC Berkeley and UCSF for this contribution.

Gemma Gets Quantization Aware Training (QAT): Smaller Footprint, Sassy Attitude?

Google also pushed the open source envelope by releasing Gemma models trained with **Quantization Aware Training (QAT)**. This isn't your standard post-training quantization; QAT involves incorporating the impact of quantization *during* the training process itself. As LDJ explained, this allows the model to adapt, potentially resulting in a quantized state with much higher quality and less performance degradation compared to just quantizing a fully trained model afterwards.

The results? Significant reductions in VRAM requirements across the board. The 27B parameter Gemma 3, for example, drops from needing a hefty 54GB to just **14.1GB** ! Even the 1B model goes from 2GB to just half a gig. This makes running these powerful models much more accessible on consumer hardware. Folks are already running them in MLX, llama.cpp, LM Studio, etc. ([Reddit thread](https://www.reddit.com/media?url=https://i.redd.it/23ut7jd3klve1.jpeg))

Wolfram  already took the 4B QAT model for a spin using LM Studio . The good news: it ran easily, needing only 5-6GB of RAM. The quirky news: it seemed to struggle a bit with prompt adherence in his tests, even giving Wolfram a sassy, winking-emoji response about ignoring the "fine print" in his complex system prompt when called out on a language switching error: "Who reads a fine print? 😉" ! He did note Gemma 3 now supports system prompts (unlike Gemma 2), which is a definite improvement .

*(While NVIDIA also released OpenMath Nemotron, we didn't dive deep in the show, but worth noting its AIMO win and accompanying open dataset release!)*

Voice and Audio Innovations: Emotional TTS and Smarter Conversations

Even in a "chill" week, the audio space delivered some serious excitement. Kwindla Kramer joined us to break down two major developments.

Dia TTS: Unhinged Emotion from a Small Open Model 🤯

This one absolutely blew up Twitter, and for good reason. **Dia**, from Nari Labs (essentially a student and a half in Korea!), is a **1.6 billion parameter open-weights (MIT licensed)** text-to-dialogue model ([Github](https://github.com/nari-labs/dia), [HF](https://huggingface.co/nari-labs/Dia-1.6B)). What makes it special? The *insane* emotional range and natural interaction patterns. My Twitter post about it ([X post](https://x.com/altryne/status/1914421814455099680)) went viral, getting half a million views !

We played some examples, and they are just wild. You *have* to hear this to believe it:

* **Check the Demos:** [Dia Demo Page](https://narilabs.github.io/dia/) | [Fal.ai Voice Clone Demo](https://fal.ai/models/fal-ai/dia-tts/voice-clone)

Another crazy thing is how it handles non-verbal cues like laughs or coughs specified in the text (e.g., (laughs)) . Instead of just tacking on a generic sound, it inflects the preceding words *leading into* the laugh, making it sound incredibly natural. It even handles interruptions seamlessly, cutting off one speaker realistically when another starts .

Kwin, our voice expert, offered some valuable perspective . While Dia is undeniably awesome and shows what's *possible*, it's very much a research model – likely unpredictable ("unhinged" was his word!) and probably required cherry-picking the best demos. Production models like 11Labs *need* predictability. Kwin also noted the dataset is probably scraped from YouTube (a common practice, explaining the lack of open audio data) and that the non-speech sounds are a key takeaway – the bar for TTS is rising beyond just clear speech .

PipeCat SmartTurn: Fixing Awkward AI Silences with Open Source VAD

Speaking of open audio, Kwin and the team at Daily/Pipecat had their *own* breaking news: they released an open-source checkpoint for their **SmartTurn** model – a semantic Voice Activity Detection (VAD) system ([Github](https://github.com/pipecat-ai/smart-turn), [HF Model](https://huggingface.co/pipecat-ai/smart-turn)) 

What's the problem SmartTurn solves? That annoying thing where voice assistants interrupt you mid-thought just because you paused for a second. I've seen this happen with my kids all the time, making interaction frustrating! Semantic VAD, or "Smart Turn," is much smarter. It considers not just silence but also the *context* – audio patterns (like intonation suggesting you're not finished) and linguistic cues (like ending on "and..." or "so...") to make a much better guess about whether you're truly done talking. This is crucial for natural-feeling voice interactions, especially for kids or multilingual speakers (like me!) who might pause more often to find the right word.

And the data part is key here. They're building an **open dataset** for this, hosted on Hugging Face. You can even contribute your own voice data by playing simple games on their [**turn-training.pipecat.ai**](https://turn-training.pipecat.ai) site ([Try It Demo](https://pcc-smart-turn.vercel.app/))! The cool incentive? The more diverse voice data they get (especially for different languages!), the better these systems will work for everyone. If your voice is in the dataset, future AI agents might just understand *you* a little better!

Kwin also mentioned their upcoming [Voice AI Course](https://maven.com/pipecat/voice-ai-and-voice-agents-a-technical-deep-dive?utm_source=student&utm_campaign=welcome) co-created with friend-of-the-pod Swyx, hosted on Maven . It aims to be a comprehensive guide with code samples, community interaction, and insights from experts (including folks from Weights & Biases!). Check it out if you want to dive deep into building voice AI. 

AI Art & Diffusion & 3D: Quick Hits

A slightly quieter week for major art model releases, but still some significant movement:

* **OpenAI's GPT Image 1 API:** We'll cover this in detail in the Big Companies section below, but obviously relevant here too as a major new tool for developers creating AI art and image editing applications .

* **Hunyuan 3D 2.5 (Tencent):** Tencent released an update to their 3D generation model, now boasting **10 billion parameters** (up from 1B!) . They're highlighting massive leaps in precision (1024-resolution geometry), high-quality textures with PBR support, and improved skeletal rigging for animation [X Post](https://x.com/TencentHunyuan/status/1915026828013850791). Definitely worth keeping an eye on as 3D generation matures and becomes more accessible (they doubled the free quota and launched an API).

Agent Development Insights: Building Robust Agents with Dex Horthy

With things slightly calmer, it was the perfect time to talk about AI agents – a space buzzing with activity, frameworks, and maybe even a little bit of drama. We brought in **Dex Horthy**, founder of HumanLayer and author of the insightful "12 Factor Agent" essay ([Github Repo](https://github.com/humanlayer/12-factor-agents/tree/main)), to share his perspective on what actually *works* when building agents for production.

Dex builds SDKs to help create agents that feel more like digital humans, aiming to deploy them where users already are (Slack, email, etc.), moving beyond simple chat interfaces. His experience led him to identify common patterns and pitfalls when trying to build reliable agents.

The Problem with Current Agent Frameworks

A key takeaway Dex shared? Many teams building serious, production-ready agents end up **writing large parts from scratch**. Why? Because existing frameworks often fall short in providing the necessary control and reliability for complex tasks. The common "prompt + bag of tools + figure it out" approach, while great for demos, struggles with reliability over longer, multi-step workflows . Think about it: even if each step is 92% reliable, after 10 steps, your overall success rate plummets due to compounding errors. That's just not good enough for customer-facing applications.

Key Principles: Small Agents, Owning Context

So, what *does* work *today* according to Dex's 12 factors?

* **Small, Focused Agents:** Instead of one giant, monolithic agent trying to do everything, the more reliable approach is to build **smaller "micro-agents"** that handle specific, well-defined parts of a workflow ]. As models get smarter, these micro-agents might grow in capability, but the principle of breaking down complexity holds. Find something at the edge of the model's capability and nail it consistently .

* **Own Your Prompts & Context:** Don't let frameworks abstract away **control over the exact tokens** going into the LLM or **how the context window is managed**. This is crucial for performance tuning. Even with massive context windows (like Gemini's 2M tokens), smaller, carefully curated context often yields better results *and* lower costs . Maximum performance requires owning every single token.

Dex's insights provide a crucial dose of pragmatism for anyone building or thinking about building AI agents in this rapidly evolving space. Check out his full [**12 Factor Agent essay**](https://github.com/humanlayer/12-factor-agents/tree/main) and the [**webinar recording**](https://lu.ma/12-factor-agent) for a deeper dive.

Big Companies & APIs: GPT Image and Grok Get Developer Access

While new *foundation models* were scarce from the giants this week, they did deliver on the API front, opening up powerful capabilities to developers.

OpenAI Finally Releases GPT Image 1 API! ([X Post](https://x.com/OpenAIDevs/status/1915097067023900883))

This was a big one many developers were waiting for. OpenAI's powerful image generation capabilities, previously locked inside ChatGPT, are now available via API under the official name **gpt-image-1** ([Docs](https://platform.openai.com/docs/guides/image-generation?image-generation-model=gpt-image-1)) . No more awkward phrasing like "the new image generation capabilities within chat gpt"!

Getting access requires organizational verification, which involved a slightly intense biometric scan process for me – feels like they're taking precautions given the model's realism and potential for misuse . Understandable, but something developers need to be aware of .

The API ([API Reference](https://platform.openai.com/docs/api-reference/images)) offers several capabilities:

* **Generations:** Creating images from scratch based on text prompts.

* **Edits:** Modifying existing images using a new prompt, crucially supporting **masking** for partial edits. This is huge for targeted changes and perfect for combining with segmentation models like NVIDIA's DAM!

There's a nice playground interface in the console, and you have interesting controls over the output:

* **Quality:** Instead of distinct models, you select a quality level (standard/HD) which impacts the internal "thinking time" and cost . It seems to be a reasoning model under the hood, so quality relates to compute/latency.

* **Number:** Generate up to 10 images at once.

* **Transparency:** Supports generating images with transparent backgrounds

I played around with it, generating ads and even trying to get it to make a ThursdAI thumbnail with my face. The **text generation is excellent** – it nailed "ThursdAI" perfectly on an unhinged speaker ad Nisten prompted! It follows complex style prompts well.

However, generating realistic *faces*, especially matching a specific person like me, seems... **really hard** right now . Even after many attempts providing a source image and asking it to replace a face, the results were generic or only vaguely resembled me. It feels almost intentionally nerfed, maybe as a safety measure to prevent deepfakes? I still used it for the thumbnail, but yeah, it could be better on faces.

OpenAI launched with several integration partners like Adobe, Figma, Wix, HeyGen, and [Fal.ai](Fal.ai) already onboard. Expect to see these powerful image generation capabilities popping up everywhere!

Grok 3 Mini & Grok 3 Now Available via API (+ App Updates)

Elon's xAI also opened the gates this week, making **Grok 3 Mini and Grok 3** available via API ([Docs](https://docs.x.ai/docs/overview)).

The **pricing structure** is fascinating and quite different from others. Grok 3 Mini is incredibly cheap for input ($0.30 / 1M tokens) with only a modest bump for output ($0.50 / 1M). The "Fast" versions, however, cost significantly more, especially for *output* tokens (Grok 3 Fast is $5 input / $25 output per million!) . It seems like a deliberate play on the "fast, cheap, smart" triangle, giving developers explicit levers to pull based on their needs.

Benchmarks provided by xAI position Grok 3 Mini competitively against other small models like Gemini 2.5 Flash and O4 Mini, scoring well on AIME (93%) and coding benchmarks. 

Speaking of the app, the iOS version got a significant update adding a **live video view** (let Grok see what you see through your camera) and **multilingual audio support** ([X Post](https://x.com/ebbyamir/status/1914820712092852430)) . Prepare for some potentially unhinged, real-time video roasting if you use the fun mode with the camera on ! Multilingual audio and search are also rolling out to SuperGrok users on Android.

*(Side note: We briefly touched on O3's recent wonkiness in following instructions for tone, despite its amazing GeoGuessr abilities! Something feels off there lately.)*

Vision and Video: Send AI's Surprise Release & More

Just when we thought the week was winding down on model releases...

Send AI Drops MAGI-1: 24B Video Model with Open Weights! 🔥

Out of seemingly nowhere, a company called **Send AI** released details (and then the *weights!*) for **MAGI-1**, a **24 billion parameter** autoregressive diffusion model for video generation ([X Post](https://x.com/SandAI_HQ/status/1914303284954996749), [GitHub](https://github.com/SandAI-org/Magi-1), [PDF Report](https://static.magi.world/static/files/MAGI_1.pdf)).

The demos looked stunning, showcasing impressive **long-form video generation** with remarkable **character consistency** – often the Achilles' heel of AI video . Nisten speculated this could be a major step towards usable AI-generated movies, solving the critical face/character consistency problem . They achieve this by predicting video in 24-frame chunks with causal attention between them, allowing for real-time streaming generation where compute doesn't scale with length. They also highlighted an "infinite extension" capability, allowing users to build out longer scenes by injecting new prompts or continuing footage.

Their technical report dives into the architecture, mentioning novel techniques like a custom **"MagiAttention"** kernel that scales to massive contexts and helps achieve the temporal consistency. It also sets SOTA on VBench-I2V and Physics-IQ benchmarks.

And the biggest surprise? They released the **model weights under an Apache 2.0 license** on Hugging Face ! This is huge! Just as we sometimes lament the lack of open source momentum from certain players, Send AI drops this 24B parameter beast with open weights. Amazing! Go download it!

Framepack: Long Videos on Low VRAM

Wolfram also flagged **Framepack**, another interesting video development from the research world from the creator of ControlNet. FramePack is a next-frame (next-frame-section) prediction neural network structure that generates videos progressively. ([Github](https://github.com/lllyasviel/FramePack))

Character AI AvatarFX Steps In

Also in the visual space, **Character AI** announced **AvatarFX** in early access ([Website](https://t.co/cdF6H58kBk)), stepping into the realm of animated, speaking visual avatars derived from images. It seems like everyone wants to bring characters to life visually now.

This Week's Buzz from W&B / Community

Quick hits on upcoming events and community stuff:

* **WeaveHacks Coming to SF!** Mark your calendars! We're hosting a hackathon focused on building with W&B Weave at the Weights & Biases office in San Francisco on **May 17th-18th** [0:06:15]. If you're around, especially if you're coming into town for Google I/O the week after, come hang out, build cool stuff, and say hi! We're planning to go all out with sponsors and prizes (announcements coming soon). [lu.ma/weavehacks](http://lu.ma/weavehacks) 

* **Fully Connected Conference Reminder:** Our flagship W&B conference, **Fully Connected**, is happening in San Francisco on **June 18th** [0:06:30]. It's where our customers, partners, and the community come together for two days of talks, workshops, and networking focused on production AI. It's always an incredible event. ([fullyconnected.com](fullyconnected.com))

Wrapping Up the "Chill" Week That Wasn't Quite Chill

Phew! See? Even a "chill" week in AI is overflowing with news when you actually have time to stop and breathe for a second. From OpenAI's fascinating open source tango and the practical (and long-awaited!) API releases of GPT Image and Grok, to the sheer creative potential shown by indie projects like Dia and Send AI's Maggie, and the grounding principles for building agents that *actually work* from Dex – there was a ton to absorb and discuss. It felt good to have the space to go a little deeper.

It was fantastic having Kwin, Maziar, and Dex join the regulars (LDJ, Yam, Wolfram, Nisten) to share their expertise and firsthand insights. A huge thank you to them and to everyone tuning in live across X, YouTube, LinkedIn, and participating in the chat! Your questions and comments make the show what it is.

Don't forget, if you missed anything, the full show is available as a podcast (search "ThursdAI" wherever you get your podcasts)

🔗 Subscribe to our show on Spotify: [thursdai.news/spotify](thursdai.news/spotify)

🔗 Apple: [thursdai.news/apple](thursdai.news/apple)

🔗 Youtube: [thursdai.news/yt](thursdai.news/yt) 

Next week? The rumors suggest the big labs might be back with major releases . The brief calm might be over! Buckle up! We'll be here to break it all down.

See you next ThursdAI!- Alex

TL;DR and Show Notes (April 23rd, 2024)

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases [@altryne](http://x.com/@altryne)

* Co Hosts - Wolfram Ravenwlf [@WolframRvnwlf](http://x.com/@WolframRvnwlf), Yam Peleg [@yampeleg](x.com/@yampeleg), Nisten Tahiraj [@nisten](http://x.com/@nisten), LDJ [@ldjconfirmed](http://x.com/@ldjconfirmed)

* Kwindla Kramer [@kwindla](https://twitter.com/kwindla/) - Daily Co-Founder // Voice expert

* Dexter Horthy [@dexhorthy](https://x.com/dexhorthy) - HumanLayer // Agents expert

* Maziyar Panahi [@MaziyarPanahi](https://x.com/MaziyarPanahi) - OSS maintainer

* **Open Source AI - LLMs**, **Vision, Voice & more**

* **OpenAI OSS Meeting:** Insights from Maziar [0:16:37]. 

* **NVIDIA Describe Anything (DAM-3B):** 3B param multimodal LLM for region-based image/video captioning. ([X Post](https://x.com/reach_vb/status/1914962078571356656), [HF model](https://huggingface.co/nvidia/DAM-3B), [HF demo](https://huggingface.co/spaces/nvidia/describe-anything-model-demo))

* **Google Gemma QAT:** Quantization-Aware Training models ([X](https://x.com/osanseviero/status/1913220285328748832), [Blog](https://developers.googleblog.com/en/gemma-3-quantized-aware-trained-state-of-the-art-ai-to-consumer-gpus/)) 

* **Big CO LLMs + APIs**

* **OpenAI GPT Image 1 API:**  ([X Post](https://x.com/OpenAIDevs/status/1915097067023900883), [Docs](https://platform.openai.com/docs/guides/image-generation?image-generation-model=gpt-image-1), [API Reference](https://platform.openai.com/docs/api-reference/images))

* **Grok API & App Updates:** Grok 3 and Grok 3 Mini available via API. ([API Docs](https://docs.x.ai/docs/overview), [App Update X Post](https://x.com/ebbyamir/status/1914820712092852430))

* **This weeks Buzz - Weights & Biases**

* **WeaveHacks SF:** Hackathon May 17-18 at W&B HQ. [lu.ma/weavehacks](http://lu.ma/weavehacks) 

* **Fully Connected:** W&B's 2-day conference, June 18-19 in SF [fullyconnected.com](https://www.fullyconnected.com/)

* **Vision & Video**

* **Send AI MAGI-1:** 24B autoregressive diffusion model for long, streaming video ([X Post](https://x.com/SandAI_HQ/status/1914303284954996749), [GitHub](https://github.com/SandAI-org/Magi-1), [PDF Report](https://static.magi.world/static/files/MAGI_1.pdf), [HF Repo](https://huggingface.co/sand-ai/MAGI-1))

* **Character AI AvatarFX:** Early access for creating speaking/emoting avatars from images . ([Website](https://t.co/cdF6H58kBk))

* **Framepack:** Mentioned for long video generation (120s) on low VRAM (6GB). ([Project Page](https://framepack.github.io/))

* **Voice & Audio**

* **Nari Labs Dia:** 1.6B param OSS TTS model ([X Post Highlight](https://x.com/altryne/status/1914421814455099680), [HF Model](https://huggingface.co/nari-labs/Dia-1.6B), [Github](https://github.com/nari-labs/dia), [Fal.ai Demo](https://fal.ai/models/fal-ai/dia-tts/voice-clone))

* **PipeCat Smart-Turn VAD:** Open source semantic VAD model ([Github](https://github.com/pipecat-ai/smart-turn), [HF Model](https://huggingface.co/pipecat-ai/smart-turn), [Fal.ai Playground](https://fal.ai/models/fal-ai/smart-turn/playground), [Try It Demo](https://pcc-smart-turn.vercel.app/))

* **AI Art & Diffusion & 3D**

* **Hunyuan 3D 2.5 (Tencent):** 10B param update [0:09:06]. Higher res geometry, PBR textures, improved rigging. ([X Post](https://x.com/TencentHunyuan/status/1915026828013850791))

* **Agents , Tools & Links**

* **12 Factor Agents:** Discussion with Dex Horthy on building robust agents  ([Github Repo](https://github.com/humanlayer/12-factor-agents/tree/main)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-apr-23rd-gpt-image-and-grok/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-apr-23rd-gpt-image-and-grok?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2MjA4NjU2NSwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.m0ZC7kg252d4W-NQQDoI_wNsaqUNEqLi2OTtARapCAg&utm_campaign=CTA_5).

---

## ThursdAI - Apr 17 - OpenAI o3 is SOTA llm, o4-mini, 4.1, mini, nano, G. Flash 2.5, Kling 2.0 and 🐬 Gemma? Huge AI week + A2A protocol interview

**Date:** April 17, 2025  
**Duration:** 1:55:51  
**Link:** [https://sub.thursdai.news/p/thursdai-apr-17-openai-o3-is-sota](https://sub.thursdai.news/p/thursdai-apr-17-openai-o3-is-sota)

Hey everyone, Alex here 👋

Wow. Just… wow. What a week, folks. Seriously, this has been one for the books. 

This week was dominated by OpenAI's double whammy: first the **GPT-4.1 family** dropped with a mind-boggling 1 million token context window, followed swiftly by the new flagship reasoning models, **o3** and **o4-mini**, which are already blowing minds with their agentic capabilities. We also saw significant moves from Google with **VEO-2** going GA, the fascinating **A2A protocol** launch (we had an amazing interview with Google's Todd Segal about it!), and even an attempt to talk to dolphins with **DolphinGemma**. Kling stepped up its video game, Cohere dropped SOTA multimodal embeddings, and ByteDance made waves in image generation. Plus, the open-source scene had some interesting developments, though perhaps overshadowed by the closed-source giants this time.

o3 has absolutely taken the crown as the conversation piece, so lets start with it (as always, TL;DR and shownotes at the end, and here's the embedding of our live video show) 

Big Company LLMs + APIs

OpenAI o3 & o4‑mini: SOTA Reasoning Meets Tool‑Use ([Blog](https://openai.com/index/introducing-o3-and-o4-mini/), [Watch Party](https://youtube.com/live/2G-VwWxKCkk?feature=share))

The long awaited o3 models (promised to us in the last days of x-mas) is finally here, and it did NOT disappoint and well.. even surprised! 

o3 is not only SOTA on nearly all possible logic, math and code benchmarks, which is to be expected from the top reasoning model, it also, and I think for the first time, is able to use tools during its reasoning process. Tools like searching the web, python coding, image gen (which it... can zoom and rotate and crop images, it's nuts) to get to incredible responses faster. 

Tool using reasoner are... almost AGI? 

This is the headline feature for me. For the first time, these o-series models have full, autonomous access to all built-in tools (web search, Python code execution, file search, image generation with Sora-Image/DALL-E, etc.). They don't just use tools when told; they decide when and how to chain multiple tool calls together to solve a problem. We saw logs with 600+ consecutive tool calls! This is agent-level reasoning baked right in.

Anecdote: We tested this live with a complex prompt: "generate an image of a cowboy that on his head is the five last digits of the hexadecimal code of the MMMU score of the latest Gemini model." o3 navigated this multi-step task flawlessly: figuring out the latest model was Gemini 2.5, searching for its MMMU score, using the Python tool to convert it to hex and extract the digits, and then using the image generation tool. It involved multiple searches and reasoning steps. Absolutely mind-blowing 🤯.

Thinking visually with images

This one also blew my mind, this model is SOTA on multimodality tasks, and a reason for this, is these models can manipulate and think about the images they received. Think... cropping, zooming, rotating. The models can now perform all these tasks to multimodal requests from users. Sci-fi stuff! 

Benchmark Dominance: As expected, these models crush existing benchmarks.

o3 sets new State-of-the-Art (SOTA) records on Codeforces (coding competitions), SWE-bench (software engineering), MMMU (multimodal understanding), and more. It scored a staggering $65k on the Freelancer eval (simulating earning money on Upwork) compared to o1's $28k!

o4-mini is no slouch either. It hits 99.5% on AIME (math problems) when allowed to use its Python interpreter and beats the older o3-mini on general tasks. It’s a reasoning powerhouse at a fraction of the cost.

**Incredible Long Context Performance**

Yam highlighted this – on the Fiction Life benchmark testing deep comprehension over long contexts, o3 maintained nearly 100% accuracy up to 120,000 tokens, absolutely destroying previous models including Gemini 2.5 Pro and even the new GPT-4.1 family on this specific eval. While its context window is currently 200k (unlike 4.1's 1M), its performance within that window is unparalleled.

**Cost-Effective Reasoning:** They're not just better, they're *cheaper* for the performance you get.

* **o3:** $10 input / $2.50 cached / $40 output per million tokens.

* **o4-mini:** $1.10 input / $0.275 cached / $4.40 output per million tokens. (Cheaper than GPT-4.0!)

**Compute Scaling Validated:** OpenAI confirmed these models used >10x the compute of o1 and leverage test-time compute scaling (spending longer on harder problems), further proving their scaling law research.

**Memory Integration:** Both models integrate with ChatGPT's recently upgraded memory feature which has access to all your previous conversations (which we didn't talk about but is absolutely amazing, try asking o3 stuff it knows about you and have ti draw conclusions!)

**Panel Takes & Caveats:**While the excitement was palpable, Yam noted some community observations about potential "rush" – occasional weird hallucinations or questionable answers compared to predecessors, possibly a side effect of cramming so much training data. Nisten, while impressed, still found the *style* of **GPT-4.1** preferable for specific tasks like generating structured medical notes in his tests. It highlights that benchmarks aren't everything, and specific use cases require evaluation (shameless plug: use tools like W&B Weave for this!).

I'll add my own, I use all the models every week to help me draft posts, and o3 was absolute crap about matching my tone. % of what's written above it was able to mimic. Gemini remains undefeated for me and this task.

Though, Overall, o3 and o4-mini feel like a paradigm shift towards more autonomous, capable AI assistants. The agentic future feels a whole lot closer.

**OpenAI Launches GPT-4.1 Family: 1 Million Tokens & Killing 4.5!** ([Our Coverage](https://www.youtube.com/live/A5-Zxj816J0), [Prompting guide](https://x.com/noahmacca/status/1911898549308280911))

Before the o3 shockwave, Monday brought its own major AI update: the **GPT-4.1 family**. This was the API-focused release, delivering massive upgrades for developers.

**The Headline:** **One Million Token Context Window!** 🤯 Yes, you read that right. All three new models – **GPT-4.1** (flagship), **GPT-4.1 mini** (cheaper/faster), and **GPT-4.1 nano** (ultra-cheap/fast) – can handle up to 1 million tokens. This is a monumental leap, enabling use cases that were previously impossible or required complex chunking strategies.

**Key Details:**

Goodbye GPT-4.5! 

In a surprising twist, OpenAI announced they are *deprecating* the recently introduced (and massive) GPT-4.5 model within 90 days in the API. Why? Because **GPT-4.1 actually outperforms it** on key benchmarks like SW-Bench, Aider Polyglot, and the new long-context MRCR eval, while being far cheaper to run. It addresses the confusion many had: why was 4.5 seemingly *worse* than 4.1? It seems 4.5 was a scaling experiment, but 4.1 represents a more optimized, better-trained checkpoint on superior data. RIP 4.5, we hardly knew ye (in the API).

**The Prompt Sandwich Surprise! 🥪:** 

This was wild. Following OpenAI's new prompting guide, I tested the "sandwich" technique (instructions -> context -> instructions *again*) on my hard reasoning eval using [W&B Weave](https://wandb.ai/site/weave?utm_source=thursdai&utm_medium=referral&utm_campaign=apr17).

For **GPT-4.1**, it made no difference (still got 48%). But for **GPT-4.1 mini**, the score jumped from 31% to **49%** – essentially matching the full 4.1 model just by repeating the prompt! That's a crazy performance boost for a simple trick. Even nano saw a slight bump. **Lesson: Evaluate prompt techniques!** Don't assume they won't work.

**Million-Token Recall Confirmed:** Using Needle-in-Haystack and their newly open-sourced **MRCR benchmark** (Multi-round Co-reference Resolution – more in Open Source), OpenAI showed near-perfect recall across the *entire* 1 million token window for **all three models**, even nano! This isn't just a theoretical limit; the recall seems robust.

**Multimodal Gains:** Impressively, **4.1 mini** hit **72% on Video-MME**, pushing SOTA for long-video Q&A in a mid-tier model by analyzing frame sequences. 

4.1 mini seems to be the absolute powerhouse of this release cycle, it nearly matches the intelligence of the previous 4o, while being significantly cheaper and much much faster with 1M context window! 

Windsurf (and Cursor) immediately made the 4.1 family available, offering a **free week** for users to test them out (likely to gather feedback and maybe influenced by certain acquisition rumors 😉). Devs reported them feeling snappier and less verbose than previous models.

**Who Should Use Which OpenAI API?**

My initial take:

* **For complex reasoning, agentic tasks, or just general chat:** Use **o3** (if you need the best) or **o4-mini** (for amazing value/speed).

* **For API development, especially coding or long-context tasks:** Evaluate the **GPT-4.1 family**. Start with **4.1 mini** – it's likely the sweet spot for performance/cost, especially with smart prompting. Use **4.1** if mini isn't quite cutting it. Use **nano** for simple, high-volume tasks like translation or basic classification.

The naming is still confusing (thanks Nisten for highlighting the UI nightmare!), but the capability boost across the board is undeniable.

**Hold the Phone! 🚨 Google Fires Back with Gemini 2.5 Flash in Breaking News**

Just when we thought the week couldn't get crazier, Google, likely reacting to OpenAI's rapid-fire launches, just dropped **Gemini 2.5 Flash** into preview via the [Gemini API](https://ai.google.dev/docs/gemini_api_overview) (in AI Studio and Vertex AI). This feels like Google's direct answer, aiming to blend reasoning capabilities with speed and cost-effectiveness.

**The Big Twist: Controllable Thinking Budgets!**Instead of separate models like OpenAI, Gemini 2.5 Flash tries to do **both reasoning and speed/cost efficiency in one model**. The killer feature? Developers can set a **"thinking budget"** (0 to 24,576 tokens) per API call to control the trade-off:

* **Low/Zero Budget:** Prioritizes speed and low cost (very cheap: **$0.15 input / $0.60 output** per 1M tokens), great for simpler tasks.

* **Higher Budget:** Allows the model multi-step reasoning "thinking" for better accuracy on complex tasks, at a higher cost (**$3.50 output** per 1M tokens, including reasoning tokens).

This gives  granular control over the cost/quality balance *within the same model*.

**Performance & Specs:**Google claims strong performance, ranking just behind Gemini 2.5 Pro on Hard Prompts in ChatBot Arena and showing competitiveness against o4-mini and Sonnet 3.7 in their benchmarks, especially given the flexible pricing.

Key specs are right up there with the competition:

* **Multimodal Input:** Text, Images, Video, Audio

* **Context Window:** **1 million tokens** (matching GPT-4.1!)

* **Knowledge Cutoff:** January 2025

**How to Control Thinking:**Simply set the thinking_budget parameter in your API call (Python/JS examples available in their docs). If unspecified, the model decides automatically.

**My Take:** This is a smart play by Google. The controllable thinking budget is a unique and potentially powerful feature for optimizing across different use cases without juggling multiple models. With 1M context and competitive pricing, Gemini 2.5 Flash is immediately a major contender in the ongoing AI arms race. Definitely one to evaluate! Find more in the [developer docs](https://ai.google.dev/docs) and [Gemini Cookbook](https://ai.google.dev/examples).

Open Source: LLMs, Tools & more

OpenAI open sources MRCR eval and Codex (Mrcr [HF](https://huggingface.co/datasets/openai/mrcr), Codex [Github](https://github.com/openai/codex))

Let's face it, this isn't the open source OpenAI coverage I was hoping for, Sam promised us an open source model, and they are about to drop this, I'd assume close to Google IO (May 20th) to steal thunder. But OpenAI did make OpenSource waves this week in addition to the above huge stories. 

MRCR is a way to evaluate long context complex tasks, and they have taken this Gemini research and open sourced a dataset for this eval. 👏 

But also, they have dropped the Codex CLI tool, which is a coding partner using o4-mini and o3 and made that tool open source as well (Unlike anthropic with Claude Code), which in turn saw 86+ Pull Requests approved within the first 24 hours! 

The best part about this CLI, is that it's hardened security, using **Apple Seatbelt** which limits it execution to the current directory + temp files (on a mac at least) 

Other Open Source Updates

While OpenAI's contributions were notable, it wasn't the only action this week:

* **Microsoft's BitNet v1.5 (**[**HF**](https://huggingface.co/collections/microsoft/BitNet)**)**: Microsoft quietly dropped updates to BitNet, continuing their exploration into ultra-low-bit (ternary) models for efficiency. As Nisten pointed out on the show though, keep in mind these still use some higher-precision layers, so they aren't *purely* 1.5-bit in practice just yet. Important research nonetheless!

* **INTELLECT-2 Distributed RL (**[**Blog**](https://www.primeintellect.ai/blog/intellect-2)**, **[**X**](https://x.com/primeintellect_ai)**)**: Prime Intellect did something wild – training **INTELLECT-2**, a 32B model, using globally distributed, permissionless reinforcement learning. Basically, anyone with a GPU could potentially contribute. Fascinating glimpse into decentralized training!

* [**Z.ai**](Z.ai)** (Formerly ChatGLM) & GLM-4 Family (**[**X**](https://x.com/Zai_org/status/1779846143024941199)**, **[**HF**](https://huggingface.co/collections/THUDM)**, **[**GitHub**](https://github.com/THUDM/GLM-4)**)**: The team behind ChatGLM rebranded to [**Z.ai**](Z.ai) and released their GLM-4 family (up to 32B parameters) under the very permissive **MIT license**. They're claiming performance competitive with much larger models like Qwen 72B, which is fantastic news for commercially usable open source!

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

This Week's Buzz: Playground Updates & A Deep Dive into A2A

On the Weights & Biases front, it's all about enabling developers to navigate this new model landscape.

**Weave Playground Supports GPT-4.1 and o3/o4-mini (**[**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fweave_wb%2Fstatus%2F1912246450857341092)**)**

With all these new models dropping, how do you actually *choose* which one is best for *your* application? You need to evaluate! Our **W&B Weave Playground** now has full support for the new **GPT-4.1 family** and the **o3/o4-mini** models.

If you're using Weave to monitor your LLM apps in production, you can easily grab a trace of a real user interaction, open it in the Playground, and instantly retry that exact same call (with all its context and history) using any of the new models side-by-side. It’s the fastest way to see how o3 compares to 4.1-mini or how Claude 3.7 stacks up against o4-mini *on your specific data*. Essential for making informed decisions in this rapidly changing environment.

**Deep Dive: Understanding Google's A2A Protocol with Todd Segal**

This was a highlight of the show for me. We were joined by **Todd Segal**, a Principal Software Engineer at Google working directly on the new **Agent-to-Agent (A2A) protocol**. There was some confusion initially about how A2A relates to the increasingly popular **Model Context Protocol (MCP)**, so getting Todd's perspective was invaluable. W&B is a proud launch partner for the A2A protocol!

**Key Takeaways from our Chat:**

* **A2A vs. MCP: Complementary, Not Competitive:** Todd was clear: Google sees these as solving different problems. **MCP is for Agents talking to Tools** (structured, deterministic capabilities). **A2A is for Agents talking to other Agents** (unstructured, stateful, unpredictable, evolving interactions). Think of MCP like calling an API, and A2A like delegating a complex task to another expert service.

* **The Need for A2A:** It emerged from the need for specialized, domain-expert agents (built internally or by partners like Salesforce) to collaborate on complex, long-running tasks (e.g., booking a multi-vendor trip, coordinating an enterprise workflow) where simple tool calls aren't enough. Google's **Agent Space** product heavily utilizes A2A internally.

* **Capability Discovery & Registries:** A core concept is agents advertising their capabilities via an "agent card" (like a business card or resume). Todd envisions a future with multiple **registries** (public, private, enterprise-specific) where agents can discover other agents best suited for a task. This registry system is on the roadmap.

* **Async & Long-Running Tasks:** A2A is designed for tasks that might take minutes, hours, or even days. It uses a central **"Task" abstraction** which is stateful. Agents communicate updates (status changes, generated artifacts, requests for more info) related to that task.

* **Push Notifications:** For very long tasks, A2A supports a **push notification** mechanism. The client agent provides a secure callback URL, and the server agent can push updates (state changes, new artifacts) even if the primary connection is down. This avoids maintaining costly long-lived connections.

* **Multimodal Communication:** The protocol supports negotiation of modalities beyond text, including rendering content within **iframes** (for branded experiences) or exchanging **video/audio streams**. Essential for future rich interactions.

* **Security & Auth:** A2A deliberately **doesn't reinvent the wheel**. It relies on standard **HTTP headers** to carry authentication (OAuth tokens, internal enterprise credentials). Identity/auth handshakes happen "out of band" using existing protocols (OAuth, OIDC, etc.), and the resulting credentials are passed with A2A requests. Your user identity flows through standard mechanisms.

* **Observability:** Todd confirmed **OpenTelemetry (OTel)** support is planned for the SDKs. Treating agents like standard microservices means leveraging existing observability tools (like W&B Weave!) is crucial for tracing and debugging multi-agent workflows.

* **Open Governance:** While currently in a Google repo, the plan is to move A2A to a **neutral foundation** (like Linux Foundation) with a fully **open governance model**. They want this to be a true industry standard.

* **Getting Started:** Check out the **GitHub repo (**[**github.com/google/A2A**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fgoogle%2FA2A)**)**, participate in discussions, file issues, and send PRs!

My take: A2A feels like a necessary piece of infrastructure for the next phase of AI agents, enabling complex, coordinated actions across different systems and vendors. While MCP handles the "how" of using tools, A2A handles the "who" and "what" of inter-agent delegation. Exciting times ahead! Big thanks to Todd for shedding light on this.

Vision & Video: Veo-2 Arrives, Kling Gets Slicker

The visual AI space keeps advancing rapidly.

**Veo-2 Video Generation Hits GA in Vertex AI & Gemini App (**[**Blog**](https://developers.googleblog.com/en/veo-2-video-generation-now-generally-available/)**, **[***Try It***](http://ai.dev)**)**

Google's answer to Sora and Kling, **Veo-2**, is now **Generally Available (GA)** for all Google Cloud customers via **Vertex AI**. You can also access it in the **Gemini app**.

Veo-2 produces stunningly realistic and coherent video, making it a top contender alongside OpenAI's Sora and  Kling. Having it easily accessible in Vertex AI is a big plus for developers on Google Cloud.

I've tried and keep tyring all of them, VEO2 is an absolute beast in realism. 

**Kling 2.0 Creative Suite: A One-Stop Shop for Video AI? (**[**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne%2Fstatus%2F1912043121497850242)**, **[**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fklingai.com)**)**

Kuaishou's **Kling** model also got a major upgrade, evolving into a full **Kling 2.0 Creative Suite**.

*Anecdote:* I actually stayed up quite late one night trying to piece together info from a Chinese live stream about this release! The dedication is real, folks. 😂

**What's New:**

* **Kling 2.0 Master:** The core video model, promising better motion, physics, and facial consistency (still 5s clips for now, but 30s/4K planned).

* **Kolors 2.0:** An integrated image generation and restyling model (think Midjourney-style filters).

* **MVL (Multimodal Visual Language) Prompting:** This is killer! You can now **inline images directly within your text prompt** for precise control (e.g., "Swap the hoodie in @video1 with the style of @image2"). This offers granular control artists have been craving.

* **Multi-Elements Editor:** A timeline-based editor to stitch clips, add lip-sync, sound effects (including generated ones like "car horn"), and music.

* **Global Access:** No more Chinese phone number requirement! Available worldwide at [**klingai.com**](klingai.com).

* **Official API via FAL:** Developers can now integrate Kling 2.0 via our friends at **⚡ FAL Generative Media Cloud**.

Kling is clearly aiming to be a holistic creative platform, reducing the need to jump between 17 different AI tools for image gen, video gen, editing, and sound. The MVL prompting is particularly innovative. Very impressive package.

Voice & Audio: Talking to Dolphins? 🐬

**DolphinGemma: Google AI Listens to Flipper (**[**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fblog.google%2Ftechnology%2Fai%2Fdolphingemma%2F)**)**

In perhaps the most delightful news of the week, Google, in collaboration with Georgia Tech and the Wild Dolphin Project, announced DolphinGemma. 

It's a ~400M parameter audio model based on the Gemma architecture (using SoundStream for audio tokenization) trained specifically on decades of recorded dolphin clicks, whistles, and pulses.The goal? To decipher the potential syntax and structure within dolphin communication and eventually enable rudimentary two-way interaction using underwater communication devices. It runs on a Pixel phone for field deployment.

This is just awesome. Using AI not just for human tasks but to potentially bridge the communication gap with other intelligent species is genuinely inspiring. We joked on the show about doing a segment of just dolphin noises – maybe next time if DolphinGemma gets an API! 🤣

AI Art & Diffusion & 3D: Seedream Challenges the Champs

**Seedream 3.0: ByteDance's Bilingual Image Powerhouse (**[**Tech post**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fteam.doubao.com%2Fen%2Ftech%2Fseedream3_0)**, **[**arXiv**](https://www.google.com/url?sa=E&q=https%3A%2F%2Farxiv.org%2Fabs%2F2504.11346)**, **[**AIbase news**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.aibase.com%2Fnews%2F17208)**)**

ByteDance wasn't just busy with video; their Seed team announced **Seedream 3.0**, a powerful bilingual text-to-image model.

**Highlights:**

* Generates native **2048x2048** images.

* Fast inference (**~3 seconds** for 1Kx1K on an A100).

* Excellent **bilingual (Chinese/English) text rendering**, even small fonts.

* Uses **Scaled-ROPE-v2** for better high-resolution generation without artifacts.

* Claims to outperform SDXL-Turbo and Qwen-Image on fidelity and prompt adherence benchmarks.

* Available via Python SDK and REST API within their Doubao Studio and coming soon to [dreamina.com](http://dreamina.com) 

Phew! We made it. What an absolute avalanche of news. OpenAI truly dominated with the back-to-back launches of the hyper-capable o3/o4-mini and the massively scaled GPT-4.1 family. Google countered strongly with the versatile Gemini 2.5 Flash, key GA releases like Veo-2, and the strategically important A2A protocol. The agent ecosystem took huge leaps forward with both A2A and broader MCP adoption. And we saw continued innovation in multimodal embeddings, video generation, and even niche areas like bioacoustics and low-bit models.

If you feel like you missed anything (entirely possible this week!), the TL;DR and links below should help. Please subscribe if you haven't already, and share this with a friend if you found it useful – it's the best way to support the show!

I have a feeling next week won't be any slower. Follow us on X/Twitter for breaking news between shows!

Thanks for tuning in, keep building, keep learning, and I'll see you next Thursday!

Alex

TL;DR and Show Notes

*Everything we covered today in bite-sized pieces with links!*

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([**@altryne**](https://www.google.com/url?sa=E&q=http%3A%2F%2Fx.com%2F%40altryne))

* Co Hosts - [**@WolframRvnwlf**](https://www.google.com/url?sa=E&q=http%3A%2F%2Fx.com%2F%40WolframRvnwlf) [**@yampeleg**](https://www.google.com/url?sa=E&q=x.com%2F%40yampeleg) [**@nisten**](https://www.google.com/url?sa=E&q=http%3A%2F%2Fx.com%2F%40nisten) [**@ldjconfirmed**](https://www.google.com/url?sa=E&q=http%3A%2F%2Fx.com%2F%40ldjconfirmed))

* Todd Segal - Principal Software Engineer @ Google - Working on A2A Protocol

* **Big CO LLMs + APIs**

* 👑 OpenAI launches **o3** and **o4-mini** in chatGPT & API ([**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Findex%2Fintroducing-o3-and-o4-mini%2F), [**Our Coverage**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fyoutube.com%2Flive%2F2G-VwWxKCkk), [**o3 and o4-mini announcement**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Findex%2Fintroducing-o3-and-o4-mini%2F))

* OpenAI launches **GPT 4.1, 4.1-mini and 4.1-nano** in **API** ([**Our Coverage**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.youtube.com%2Flive%2FA5-Zxj816J0), [**Prompting guide**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fnoahmacca%2Fstatus%2F1911898549308280911))

* 🚨 Google launches **Gemini 2.5 Flash** with controllable thinking budgets ([**Blog Post - Placeholder Link**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fblog.google%2Ftechnology%2Fai%2Fgoogle-gemini-update-flash-extension%2F), [**API Docs**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fai.google.dev%2Fdocs))

* Mistral classifiers Factory

* Claude does research + workspace integration ([**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.anthropic.com%2Fnews%2Fresearch))

* Cohere Embed‑4 — Multimodal embeddings for enterprise search ([**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fcohere.com%2Fblog%2Fembed-4), [**Docs Changelog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fdocs.cohere.com%2Fv2%2Fchangelog%2Fembed-multimodal-v4), [**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fcohere%2Fstatus%2F1912128813104078999))

* **Open Source LLMs**

* OpenAI open sources MRCR Long‑Context Benchmark ([**Hugging Face**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fdatasets%2Fopenai%2Fmrcr))

* Microsoft BitNet v1.5 ([**HF**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fcollections%2Fmicrosoft%2FBitNet))

* INTELLECT‑2 — Prime Intellect’s 32B “globally‑distributed RL” experiment ([**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.primeintellect.ai%2Fblog%2Fintellect-2), [**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fprimeintellect_ai))

* [Z.ai](Z.ai) (previously chatGLM) + GLM‑4‑0414 open‑source family ([**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FZai_org%2Fstatus%2F1779846143024941199), [**HF Collection**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fcollections%2FTHUDM), [**GitHub**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FTHUDM%2FGLM-4))

* **This weeks Buzz + MCP/A2A**

* Weave playground support for GPT 4.1 and o3/o4-mini models ([**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fweave_wb%2Fstatus%2F1912246450857341092))

* Chat with Todd Segal - A2A Protocol ([**GitHub Spec**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fgoogle%2FA2A))

* **Vision & Video**

* **Veo‑2 Video Generation in GA, Gemini App** ([**Dev Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fdevelopers.googleblog.com%2Fen%2Fveo-2-video-generation-now-generally-available%2F))

* **Kling 2.0 Creative Suite** ([**X**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne%2Fstatus%2F1912043121497850242), [**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fklingai.com))

* ByteDance public Seaweed-7B, a video generation foundation model ([**seaweed.video**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fseaweed.video%2F))

* **Voice & Audio**

* **DolphinGemma** — Google AI tackles dolphin communication ([**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fblog.google%2Ftechnology%2Fai%2Fdolphingemma%2F))

* **AI Art & Diffusion & 3D**

* **Seedream 3.0 bilingual image diffusion – ByteDance** ([**Tech post**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fteam.doubao.com%2Fen%2Ftech%2Fseedream3_0), [**arXiv**](https://www.google.com/url?sa=E&q=https%3A%2F%2Farxiv.org%2Fabs%2F2504.11346), [**AIbase news**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.aibase.com%2Fnews%2F17208))

* **Tools**

* OpenAI debuts Codex CLI, an open source coding tool for terminals ([**Github**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex))

* Use o3 with Windsurf (which OpenAI is rumored to buy at $3B) via the mac app integration + write back + multiple files 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-apr-17-openai-o3-is-sota/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-apr-17-openai-o3-is-sota?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2MTU2NjkzOCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.NhVIknHwPyAwb64UpE1sqJDUBHbjL5K6_XdUSHuXvG0&utm_campaign=CTA_5).

---

## 💯 ThursdAI - 100th episode 🎉 - Meta LLama 4, Google tons of updates, ChatGPT memory, WandB MCP manifesto & more AI news

**Date:** April 10, 2025  
**Duration:** 1:32:18  
**Link:** [https://sub.thursdai.news/p/thursdai-100th-episode-meta-llama](https://sub.thursdai.news/p/thursdai-100th-episode-meta-llama)

Hey Folks, 

Alex here, celebrating an absolutely crazy (to me) milestone, of #100 episodes of ThursdAI 👏 100 episodes in a year and a half (as I [started publishing](https://sub.thursdai.news/p/thursdai-july-12-show-recap-notes) much later than I started going live, and the first episode was embarrassing), 100 episodes that documented INCREDIBLE AI progress, we mention on the show today, we used to be excited by context windows jumping from 4K to 16K! 

I want to extend a huge thank you to every one of you, who subscribes, listens to the show on podcasts, joins the live recording (we regularly get over 1K live viewers across platforms), shares with friends and highest thank you for the paid supporters! 🫶 Sharing the AI news progress with you, energizes me to keep going, despite the absolute avalanche of news every week.

And what a perfect way to celebrate the 100th episode, on a week that Meta dropped Llama 4, sending the open-source world into a frenzy (and a bit of chaos). Google unleashed a firehose of announcements at Google Next. The agent ecosystem got a massive boost with MCP and A2A developments. And we had fantastic guests join us – Michael Lou diving deep into the impressive DeepCoder-14B, and Liad Yosef & Ido Salomon sharing their wild ride creating the viral GitMCP tool.

I really loved today's show, and I encourage those of you who only read, to give this a watch/listen, and those of you who only listen, enjoy the recorded version (though longer and less edited!) 

Now let's dive in, there's a LOT to talk about (TL;DR and show notes as always, at the end of the newsletter) 

Open Source AI & LLMs: Llama 4 Takes Center Stage (Amidst Some Drama)

**Meta drops Llama 4 - Scout 109B/17BA & Maverick 400B/17BA **([Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/), [HF](https://huggingface.co/meta-llama), [Try It](https://meta.ai/))

This was by far the biggest news of this last week, and it dropped... on a Saturday? (I was on the mountain ⛷️! What are you doing Zuck) 

Meta dropped the long awaited LLama-4 models, huge ones this time

* Llama 4 **Scout**: 17B active parameters out of ~109B total (16 experts).

* Llama 4 **Maverick**: 17B active parameters out of a whopping ~400B total (128 experts).

* Unreleased: **Behemoth** - 288B active with 2 Trillion total parameters chonker!

* Both base and instruct finetuned models were released

These new models are all Multimodal, Multilingual MoE (mixture of experts) architecture, and were trained with FP8, for significantly more tokens (around 30 Trillion Tokens!) with interleaved attention (iRoPE), and a refined SFT > RL > DPO post-training pipeline.

The biggest highlight is the stated context windows, 10M for Scout and 1M for Maverick, which is insane (and honestly, I haven't yet seen a provider that is even remotely able to support anything of this length, nor do I have the tokens to verify it) 

The messy release - Big Oof from Big Zuck

Not only did Meta release on a Saturday, messing up people's weekends, Meta apparently announced a high LM arena score, but the model they provided to LMArena was... not the model they released!?

It caused LMArena to release the 2000 chats dataset, and truly, some examples are quite damning and show just how unreliable LMArena can be as vibe eval. 

Additionally, during the next days, folks noticed discrepancies between the stated eval scores Meta released, and the ability to evaluate them independently, including our own Wolfram, who noticed that a quantized version of Scout, performed better on his laptop while HIGHLY quantized (read: reduced precision) than it was performing on the Together API inference endpoint!? 

We've chatted on the show that this may be due to some VLLM issues, and speculated about other potential reasons for this. 

Worth noting the official response from Ahmad Al-Dahle, head of LLama at Meta, who mentioned stability issues between providers and absolutely denied any training on any benchmarks

Too big for its own good (and us?)

One of the main criticism the OSS community had about these releases, is that for many of us, the reason for celebrating Open Source AI, is the ability to run models without network, privately on our own devices. 

Llama 3 was released in 8-70B distilled versions and that was incredible for us local AI enthusiasts! These models, despite being "only" 17B active params, are huge and way to big to run on most local hardware, and so the question then is, if we're getting a model that HAS to run on a service, why not use Gemini 2.5 that's MUCH better and faster and cheaper than LLama?  

Why didn't Meta release those sizes? Was it due to an inability to beat Qwen/DeepSeek enough? 🤔 

My Take

Despite the absolutely chaotic rollout, this is still a monumental effort from Meta. They spent *millions* on compute and salaries to give this to the community. Yes, no papers yet, the LM Arena thing was weird, and the inference wasn't ready. But Meta is standing up for Western open-source in a big way. We *have* to celebrate the core contribution while demanding better rollout practices next time. As Wolfram rightly said, the real test will be the fine-tunes and distillations the community builds on these base models. Releasing the base weights is crucial for that. Let's see if the community can tame this beast once the inference dust settles. Shout out to Ahmed Al-Dahle and the whole Llama team at Meta – incredible work, messy launch, but thank you for pushing open source forward. 🎉

Together AI & Agentica (Berkley) finetuned DeepCoder-14B with reasoning ([X](https://x.com/togethercompute/status/1909697124805333208), [Blog](https://www.together.ai/blog/deepcoder))

Amidst the Llama noise, we got another stellar open-source release! We were thrilled to have Michael Lou from Agentica/UC Berkeley join us to talk about DeepCoder-14B-Preview which beats DeepSeek R1 and even o3-mini on several coding benchmarks. 

Using distributed Reinforcement Learning (RL), it achieves 60.6% Pass@1 accuracy on LiveCodeBench, matching the performance of models like o3-mini-2025-01-31 (Low) despite its smaller size.

The stated purpose of the project is to democratize RL and they have open sourced the model ([HF](https://huggingface.co/agentica-org/DeepCoder-14B-Preview)), the dataset ([HF](https://huggingface.co/datasets/agentica-org/DeepCoder-Preview-Dataset)), the Weights & Biases [logs](https://wandb.ai/mluo/deepcoder) and even the [eval logs](https://drive.google.com/file/d/1tr_xXvCJnjU0tLO7DNtFL85GIr3aGYln/view?usp=sharing)! 

Shout out to Michael, Sijun and Alpay and the rest of the team who worked on this awesome model! 

NVIDIA Nemotron ULTRA is finally here, 253B pruned Llama 3-405B ([HF](https://huggingface.co/nvidia/Llama-3_1-Nemotron-Ultra-253B-v1))

While Llama 4 was wrapped in mystery, NVIDIA dropped their pruned and distilled finetune of the previous Llama chonker 405B model, turning at just about half the parameters. 

And they were able to include the LLama-4 benchmarks in their release, showing that the older Llama, finetuned can absolutely beat the new ones at AIME, GPQA and more. 

As a reminder, we covered the previous 2 NEMOTRONS and they are a combined reasoning and non reasoning models, so the jump is not that surprising, and it does seem like a bit of eval cherry picking happened here. 

Nemotron Ultra supports 128K context and fits on a single 8xH100 node for inference. Built on open Llama models and trained on vetted + synthetic data, it's commercially viable. Shout out to NVIDIA for releasing this, and especially for pushing open reasoning datasets which Nisten rightly praised as having long-term value beyond the models themselves.

**More Open Source Goodness: Jina, DeepCogito, Kimi**

The open-source train didn't stop there:

* **Jina Reranker M0:** Our friends at Jina released a state-of-the-art *multimodal* reranker model. If you're doing RAG with images and text, this looks super useful for improving retrieval quality across languages and modalities ([Blog](https://jina.ai/news/jina-reranker-m0-multilingual-multimodal-document-reranker/), [HF](https://huggingface.co/jinaai/jina-reranker-m0))

* **DeepCogito:** A new company emerged releasing a suite of Llama fine-tunes (3B up to 70B planned, with larger ones coming) trained using a technique they call Iterated Distillation and Amplification (IDA). They claim their 70B model beats DeepSeek V2 70B on some benchmarks . Definitely one to watch. ([Blog](https://www.deepcogito.com/research/cogito-v1-preview), [HF](https://huggingface.co/deepcogito/cogito-v1-preview-llama-70B))

* **Kimi-VL & Kimi-VL-Thinking:**  MoonShot, who sometimes get lost in the noise, released incredibly impressive Kimi Vision Language Models (VLMs). These are MoE models with only ~3 Billion active parameters, yet they're showing results on par with or even beating models 10x larger (like Gemma 2 27B) on benchmarks like MathVision and ScreenSpot. They handle high-res images, support 128k context, and crucially, include a *reasoning* VLM variant. Plus, they're MIT licensed! Nisten's been following Kimi and thinks they're legit, just waiting for easier ways to run them locally. Definitely keep an eye on Kimi. ([HF](https://huggingface.co/collections/moonshotai/kimi-vl-a3b-67f67b6ac91d3b03d382dd85))

This Week's Buzz from Weights & Biases - Observable Tools & A2A!

This week was personally very exciting on the W&B front, as I spearheaded and launched initiatives directly related to the MCP and A2A news!

**W&B launches the **[**observable.tools**](observable.tools)** initiative!**

As MCP takes off, one challenge becomes clear: observability. When your agent calls an external MCP tool, that part of the execution chain becomes a black box. You lose the end-to-end visibility crucial for debugging and evaluation.

That's why I'm thrilled that we launched **Observable Tools (**[**Website**](https://observable.tools)**)** – an initiative championing full-stack agent observability, specifically within the MCP ecosystem. Our vision is to enable developers using tools like W&B Weave to see *inside* those MCP tool calls, getting a complete trace of every step.

The core of this is **Proposal **[**RFC 269**](https://wandb.me/mcp-spec)** on the official MCP GitHub spec**, which I authored! (My first RFC, quite the learning experience!). It details how to integrate OpenTelemetry tracing directly into the MCP protocol, allowing tools to securely report detailed execution spans back to the calling client (agent). We went deep on the spec, outlining transmission mechanisms, schemas, and rationale.

**My ask to you, the ThursdAI community:** Please check out [**observable.tools**](observable.tools), read the manifesto, watch the fun video we made, and most importantly, **go to the RFC 269 proposal (shortcut: **[**wandb.me/mcp-spec)**](oneb.me/mcp-spec)). Read it, comment, give feedback, and upvote if you agree! We need community support to make this impossible for the MCP maintainers to ignore. Let's make observability a first-class citizen in the MCP world! We also invite our friends from across the LLM observability landscape (LangSmith, Braintrust, Arize, Galileo, etc.) to join the discussion and collaborate.

**W&B is a Launch Partner for Google's A2A**

As mentioned earlier, we're also excited to be a launch partner for Google's new [Agent2Agent](https://wandb.ai/wandb_fc/product-announcements-fc/reports/Powering-Agent-Collaboration-Weights-Biases-Partners-with-Google-Cloud-on-Agent2Agent-Interoperability-Protocol---VmlldzoxMjE3NDg3OA) (A2A) protocol. We believe standardized communication *between* agents is the next critical step, and we'll be supporting A2A alongside MCP in our tools. Exciting times for agent infrastructure! I've invited Google folks to next week to discuss the protocol in depth! 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Big Company LLMs + APIs: Google's Onslaught & OpenAI's Memory Upgrade

While open source had a wild week, the big players weren't sleeping. Google especially came out swinging at Google Next.

**Google announces TONS of new things at Next 🙌  (**[**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fblog.google%2Fproducts%2Fgoogle-cloud%2Fnext-2025%2F)**)**

Google I/O felt like a preview, Google Next felt like the delivery truck backing up and dumping everything. Here's the whirlwind tour:

* **Gemini 2.5 Flash API:** The faster, cheaper Gemini 2.5 model is coming soon to Vertex AI. (Still waiting on that general API access!).

* **Veo 2 Editing:** Their top-tier video model (competing with Sora, Kling) gets editing capabilities. Very cool.

* **Imagen 3 Updates:** Their image model gets improvements, including inpainting.

* **Lyria:** Text-to-music model moves into preview.

* **TPU v7 (Ironwood):** New TPU generation coming soon. As Nisten noted, Google's infrastructure uptime is consistently amazing, which could be a winning factor regardless of model SOTA status.

* **Chirp 3 HD Voices + Voice Cloning:** This one raised eyebrows. The notes mentioned HD voices *and* voice cloning. Cloning is a touchy subject the big players usually avoid publicly (copyright, deepfakes). Still digging for confirmation/details on this – if Google is really offering public voice cloning, that's huge. Let me know if you find a link!

* **Deep Research gets Gemini 2.5 Pro:** The experimental deep research feature in Gemini (their answer to OpenAI's research agent) now uses the powerful 2.5 Pro model. Google released comparison stats showing users strongly prefer it (70%) over OpenAI's offering, citing better instruction following and comprehensiveness. I haven't fully tested the 2.5 version yet, but the free tier access is amazing. and just look at those differences in preference compared to OAI Deep Research! 

**Firebase Studio **([firebase.studio](https://firebase.studio/))**:** Remember Project IDX? It's been rebranded and launched as Firebase Studio. This is Google's answer to the wave of "vibe coding" web builders like Lovable, Bolt and a few more. It's a full-stack, cloud-based GenAI environment for building, testing, and deploying apps, integrated with Firebase and likely Gemini. Looks promising!

**Google Embraces MCP & Launches A2A Protocol!**

Two massive protocol announcements from Google that signal the maturation of the AI agent ecosystem:

* **Official MCP Support! (**[**X**](https://twitter.com/demishassabis/status/1910107859041271977)**)**This is huge. Following Microsoft and AWS, Google (via both Sundar Pichai and Demis Hassabis) announced official support for Anthropic's Model Context Protocol (MCP) in Gemini models and SDKs. MCP is rapidly becoming *the* standard for how agents discover and use tools securely and efficiently. With Google onboard, there's basically universal major vendor support. MCP is here to stay.

* **Agent2Agent (A2A) Protocol (**[**Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fdevelopers.googleblog.com%2Fen%2Fa2a-a-new-era-of-agent-interoperability%2F)** , **[**Spec**](https://github.com/google/A2A)**, **[**W&B Blog**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwandb.ai%2Fwandb_fc%2Fproduct-announcements-fc%2Freports%2FPowering-Agent-Collaboration-Weights-Biases-Partners-with-Google-Cloud-on-Agent2Agent-Interoperability-Protocol---VmlldzoxMjE3NDg3OA)**)**Google also launched a *new* open standard, A2A, designed for interoperability *between* different AI agents. Think of agents built by different vendors (Salesforce, ServiceNow, etc.) needing to talk to each other securely to coordinate complex workflows across enterprise systems. Built on web standards (HTTP, SSE, JSON-RPC), it handles discovery, task management (long-running!), and modality negotiation. Importantly, Google positions A2A as *complementary* to MCP, not competitive. MCP is how an agent uses a *tool*, A2A is how an *agent* talks to *another agent*. Weights & Biases is proud to be one of the 50+ launch partners working with Google on this! We'll do a deeper dive soon, but this + MCP feels like the foundation for a truly interconnected agent future.

**Cloudflare - new Agents SDK (**[agents.cloudflare.com](https://agents.cloudflare.com/))

Speaking of agents, Cloudflare launched their new Agents SDK (npm i agents). Built on their serverless infrastructure (Workers, Durable Objects), it offers a platform for building stateful, autonomous AI agents with a compelling pricing model (pay for CPU time, not wall time). This ties into the GitMCP story later – Cloudflare is betting big on the edge agent ecosystem.

**Other Big Co News:**

* **Anthropic MAX:** A new $200/month tier for Claude, offering higher usage quotas but no new models. Meh.

* **Grok 3 API:** Elon's xAI finally launched the API tier for Grok 3 (plus Fast and Mini variants). Now you can test its capabilities yourself. We're still waiting for the promised Open Source Grok-2

**🚨 BREAKING NEWS 🚨 OpenAI Upgrades Memory**

Right on cue during the show, OpenAI dropped a feature update! Sam Altman hyped *something* coming, and while it wasn't the o3/o4-mini models (those are coming next), it's a significant enhancement to **ChatGPT Memory**.

Previously, Memory tried to selectively save key facts. Now, when enabled, it can **reference ALL of your past chats** to personalize responses. Preferences, interests, past projects – it can potentially draw on everything. OpenAI states there's **no storage limit** for what it can reference.

How? Likely some sophisticated RAG/vector search under the hood, not stuffing everything into context. LDJ mentioned he might have had this rolling out silently for weeks, and while the immediate difference wasn't huge, the potential is massive as models get better at utilizing this vast personal context.

The immediate reaction? Excitement mixed with a bit of caution. As Wolfram pointed out, do I *really* want it remembering *every* single chat? Configurable memory (flagging chats for inclusion/exclusion) seems like a necessary follow-up. Thanks for the feature request, Wolfram! (And yes, Europe might not get this right away anyway...). This could finally stop ChatGPT from asking me basic questions it should know from our history!

Prompt suggestion: Ask the new chatGPT with memory, a think that you asked it that you likely forgot.

Just don't asked it what was the most boring thing you asked it, I got cooked I'm still feeling raw 😂 

Vision & Video: Kimi Drops Tiny But Mighty VLMs

The most impressive long form AI video paper dropped, showing that it's possible to create 1 minute long video, with incredible character and scene consistency

This [paper](https://t.co/agJKUAExpz) introduces TTT layers (Test Time Training) to a pre-trained transformer, allowing it to one shot generate these incredibly consistent long scenes. Can't wait to see how the future of AI video evolves with this progress! 

AI Art & Diffusion & 3D: HiDream Takes the Open Crown

**HiDream-I1-Dev 17B MIT license new leading open weights image gen! (**[**HF**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fcollections%2FHiDream-ai%2Fhidream-i1-67f3e90dd509fed088a158b3)**)**

Just when we thought the image gen space was settling, HiDream, a Chinese company, open-sourced their HiDream-I1 family under MIT license! This 17B parameter model comes in Dev, Full, and Fast variants.

The exciting part? Based on early benchmarks (like Artificial Analysis Image Arena), **HiDream-I1-Dev surpasses Flux 1.1 [Pro]**, Recraft V3, Reve and Imagen 3 while being open source! It boasts outstanding prompt following and text rendering capabilities.

HiDream's API is coming soon too and I really hope it's finetunable! 

Tools: GitMCP - The Little Repo Tool That Could

GitMCP - turn any github repo into an MCP server ([website](https://gitmcp.io))

We wrapped up the show with a fantastic story from the community. We had Liad Yosef (Shopify) and Ido Salomon (Palo Alto Networks) join us to talk about **GitMCP**.

It started with a simple problem: a 3MB LLM.txt file (a format proposed by Jeremy Howard for repo documentation) too large for context windows. Liad and Ido, working nights and weekends, built an MCP server that could ingest any GitHub repo (prioritizing LLM.txt if present, falling back to Readmes/code comments) and expose its documentation via MCP tools (semantic search, fetching).

This means any MCP-compatible client (like Cursor, potentially future ChatGPT/Gemini) can instantly query the documentation of *any* public GitHub repo just by pointing to the GitMCP URL for that repo (e.g., [https://gitmcp.io/user/repo).](https://gitmcp.io/user/repo).) As Yam Peleg pointed out during the show, the genius here is dynamically generating a *customized* tool specifically for that repo, making it incredibly easy for the LLM to use.

Then, the story got crazy. They launched, went viral, almost melted their initial Vercel serverless setup due to traffic and SSE connection costs (100$+ per hour!). DMs flew back and forth with Vercel's CEO, then Cloudflare's CTO swooped in offering to sponsor hosting on Cloudflare's *unreleased *Agents platform if they migrated *immediately*. A frantic weekend of coding ensued, culminating in a nail-biting domain switch and a temporary outage before getting everything stable on Cloudflare.

The project has received massive praise (including from Jeremy Howard himself) and is solving a real pain point for developers wanting to easily ground LLMs in project documentation. Huge congrats to Liad and Ido for the amazing work and the wild ride! Check out gitmcp.io!

Wrapping Up Episode 100!

Whew! What a show. From the Llama 4 rollercoaster to Google's AI barrage, the rise of agent standards like MCP and A2A, groundbreaking open source models, and incredible community stories like GitMCP – this episode truly showed an exemplary week in AI and underlined the reason I do this every week. It's really hard to keep up, and so if I commit to you guys, I stay up to date myself!  

Hitting 100 episodes feels surreal. It's been an absolute privilege sharing this journey with Wolfram, LDJ, Nisten, Yam, all our guests, and all of you. Seeing the community grow, hitting milestones like 1000 YouTube subscribers today, fuels us to keep going 🎉 

The pace isn't slowing down. If anything, it's accelerating. But we'll be right here, every Thursday, trying to make sense of it all, together.

If you missed anything, don't worry! Subscribe to the ThursdAI News Substack for the full TL;DR and links below.

Thanks again for making 100 episodes possible. Here's to the next 100! 🥂

Keep tinkering, keep learning, and I'll see you next week.

Alex

**TL;DR and Show Notes**

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@yampeleg](http://x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed)

* **Michael Luo **[@michaelzluo](http://x.com/michaelzluo) - CS PhD @ UC Berkeley; AI & Systems

* **Liad Yosef **([@liadyosef](https://x.com/liadyosef)), **Ido Salomon **([@idosal1](https://x.com/idosal1)) - GitMCP creators

* **Open Source LLMs** 

* Meta drops LLama 4 (Scout 109B/17BA & Maverick 400B/17BA) - ([Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/), [HF](https://huggingface.co/meta-llama), [Try It](https://meta.ai/))

* Together AI and Agentica (UC Berkley) announce **DeepCoder-14B** ([X](https://x.com/togethercompute/status/1909697124805333208), [Blog](https://www.together.ai/blog/deepcoder))

* NVIDIA Nemotron Ultra is here! 253B pruned LLama 3-405B ([X](https://x.com/kuchaev/status/1909444566379573646), [HF](https://huggingface.co/nvidia/Llama-3_1-Nemotron-Ultra-253B-v1))

* Jina Reranker M0 - SOTA multimodal reranker model ([Blog](https://jina.ai/news/jina-reranker-m0-multilingual-multimodal-document-reranker/), [HF](https://huggingface.co/jinaai/jina-reranker-m0))

* DeepCogito - SOTA models 3-70B - beating DeepSeek 70B - ([Blog](https://www.deepcogito.com/research/cogito-v1-preview), [HF](https://huggingface.co/deepcogito/cogito-v1-preview-llama-70B))

* ByteDance new release - [**Seed-Thinking-v1.5**](https://github.com/ByteDance-Seed/Seed-Thinking-v1.5)

* **Big CO LLMs + APIs**

* Google announces TONS of new things 🙌  ([Blog](https://blog.google/products/google-cloud/next-2025/))

* Google launches Firebase Studio ([website](https://firebase.studio/))

* Google is announcing official support for MCP ([X](https://x.com/demishassabis/status/1910107859041271977))

* Google announces A2A protocol - agent 2 agent communication ([Blog](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/), [Spec](https://github.com/google/A2A), [W&B Blog](https://wandb.ai/wandb_fc/product-announcements-fc/reports/Powering-Agent-Collaboration-Weights-Biases-Partners-with-Google-Cloud-on-Agent2Agent-Interoperability-Protocol---VmlldzoxMjE3NDg3OA))

* Cloudflare - new Agents SDK ([Website](https://agents.cloudflare.com/))

* Anthropic MAX - $200/mo with more quota

* Grok 3 finally launches API tier ([API](https://docs.x.ai/docs/models#models-and-pricing))

* OPenAI adds enhanced memory to ChatGPT - can remember all your chats ([X](https://x.com/OpenAI/status/1910378768172212636))

* **This weeks Buzz - MCP and A2A**

* W&B launches the [observable.tools](http://observable.tools) initiative & invite people to comment on the MCP [RFC](http://wandb.me/mcp-spec)

* W&B is the launch partner for Google's A2A ([Blog](https://wandb.ai/wandb_fc/product-announcements-fc/reports/Powering-Agent-Collaboration-Weights-Biases-Partners-with-Google-Cloud-on-Agent2Agent-Interoperability-Protocol---VmlldzoxMjE3NDg3OA))

* **Vision & Video**

* **Kimi-VL and Kimi-VL-Thinking - **A3B vision models (X, [HF](https://t.co/cgCMsiHN8p))

* One-Minute Video Generation with Test-Time Training ([Blog](https://t.co/BSHsucizoG), [Paper](https://t.co/agJKUAExpz))

* **Voice & Audio**

* Amazon - Nova Sonic - speech2speech foundational model ([Blog](https://www.aboutamazon.com/news/innovation-at-amazon/nova-sonic-voice-speech-foundation-model))

* **AI Art & Diffusion & 3D**

* **HiDream-I1-Dev **17B MIT license** **new leading open weights image gen 0 passes Flux1.1[pro] ! ([HF](https://huggingface.co/collections/HiDream-ai/hidream-i1-67f3e90dd509fed088a158b3))

* **Tools**

* GitMCP - turn any github repo into an MCP server ([try it](https://gitmcp.io/))

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber. 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-100th-episode-meta-llama/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-100th-episode-meta-llama?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2MTA1ODY0MywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.NdR7554cAii5VG08n5tfRMYdwmT0MjBZKI_p1urv9tU&utm_campaign=CTA_5).

---

## ThursdAI - Apr 3rd - OpenAI Goes Open?! Gemini Crushes Math, AI Actors Go Hollywood & MCP, Now with Observability?

**Date:** April 03, 2025  
**Duration:** 1:37:33  
**Link:** [https://sub.thursdai.news/p/thursdai-apr-3rd-openai-goes-open](https://sub.thursdai.news/p/thursdai-apr-3rd-openai-goes-open)

Woo! Welcome back to ThursdAI, show number 99! Can you believe it? We are *one* show away from hitting the big 100, which is just wild to me. And speaking of milestones, we just crossed **100,000 downloads** on Substack alone! [Insert celebratory sound effect here 🎉]. Honestly, knowing so many of you tune in every week **genuinely fills me with joy**, but also a real commitment to keep bringing you the the high-signal, zero-fluff AI news you count on. Thank you for being part of this amazing community! 🙏

And what a week it's been! I started out busy at work, playing with the native image generation in ChatGPT like everyone else (all 130 million of us!), and then I looked at my notes for today… an absolute *mountain* of updates. Seriously, one of those weeks where open source just exploded, big companies dropped major news, and the vision/video space is producing stuff that's crossing the uncanny valley.

We’ve got OpenAI teasing a big open source release (yes, *Open*AI might actually be *open* again!), Gemini 2.5 showing superhuman math skills, Amazon stepping into the agent ring, truly mind-blowing AI character generation from Meta, and a personal update on making the Model Context Protocol (MCP) observable. Plus, we had some fantastic guests join us live!

So buckle up, grab your coffee (or whatever gets you through the AI whirlwind), because we have a *lot* to cover. Let's dive in! (as always, show notes and links in the end)

OpenAI Makes Waves: Open Source Tease, Tough Evals & Billions Raised

It feels like OpenAI was determined to dominate the headlines this week, hitting us from multiple angles.

First, the potentially massive news: **OpenAI is planning to release a new open source model** in the "coming months"! Kevin Weil [**tweeted**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fkevinweil%2Fstatus%2F1906797119848988822) that they're working on a "highly capable open language model" and are actively seeking developer feedback through dedicated sessions ([**sign up here**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Fform%2Fopen-model-feedback) if interested) to "get this right." Word on the street is that this could be a powerful reasoning model. Sam Altman also cheekily added they won't slap on a Llama-style 8,300 tasks) and even includes meta-evaluation for the LLM judge they built ([**Nano-Eval framework also open sourced**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fopenai%2Fpreparedness)). The kicker? **Claude 3.5 Sonnet (New)** came out on top with just **21.0%** replication score (human PhDs got 41.4%). Props to OpenAI for releasing an eval where they don’t even win. That’s what real benchmarking integrity looks like. You can find the [**code on GitHub**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fopenai%2Fpreparedness%2Ftree%2Fmain%2Fproject%2Fpaperbench) and read the [**full paper here**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fcdn.openai.com%2Fpapers%2F22265bac-3191-44e5-b057-7aaacd8e90cd%2Fpaperbench.pdf).

Third, the casual [**40 Billion Dollars**](https://openai.com/index/investing−in−our−mission/)** **funding round led by SoftBank. Valuing the company at **300 Billion**. Yes, Billion with a B. More than Coke, more than Disney. The blog post was hilariously short for such a massive number. They also mentioned**500 million weekly ChatGPT users**and the insane onboarding rate (1M users/hr!) thanks to native image generation, especially seeing huge growth in India. The scale is just mind-boggling.

Oh, and for fun, try the new grumpy, EMO "[**Monday" voice**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FOpenAI%2Fstatus%2F1907124258867982338) in advanced voice mode. It's surprisingly entertaining.

Open Source Powerhouses: Nomic & OpenHands Deliver SOTA

Beyond the OpenAI buzz, the open source community delivered some absolute gems, and we had guests from two key projects join us!

Nomic Embed Multimodal: SOTA Embeddings for Visual Docs

Our friends at Nomic AI are back with a killer release! We had Zach Nussbaum on the show discussing [**Nomic Embed Multimodal**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.nomic.ai%2Fblog%2Fposts%2Fnomic-embed-multimodal). These are new 3B & 7B parameter embedding models ([**available on Hugging Face**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fcollections%2Fnomic-ai%2Fnomic-embed-multimodal-67e5ddc1a890a19ff0d58073)) built on Alibaba's excellent Qwen2.5-VL. They achieved **SOTA on visual document retrieval** by cleverly embedding interleaved text-image sequences – perfect for PDFs and complex webpages.

Zach highlighted that they chose the Qwen base because high-performing open VLMs under 3B params are still scarce, making it a solid foundation. Importantly, the 7B model comes with an **Apache 2.0 license**, and they've open sourced weights, code, and data. They offer both a powerful multi-vector version (ColNomic) and a faster single-vector one. Huge congrats to Nomic!

OpenHands LM 32B & Agent: Accessible SOTA Coding

Remember OpenDevin? It evolved into OpenHands, and the team just dropped their own [**OpenHands LM 32B**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.all-hands.dev%2Fblog%2Fintroducing-openhands-lm-32b----a-strong-open-coding-agent-model)! We chatted with co-founder Xingyao "Elle" Wang about this impressive Qwen 2.5 finetune ([**MIT licensed, on Hugging Face**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fall-hands%2Fopenhands-lm-32b-v0.1)).

It hits a remarkable **37.2% on SWE-Bench Verified **(a coding benchmark measuring real-world repo tasks), competing with much larger models. Elle stressed they didn't just chase code completion scores; they focused on tuning for *agentic capabilities* – tool use, planning, self-correction – using trajectories from their contamination-free Switch Execution dataset. This focus seems to be paying off, as the OpenHands *agent* also snagged the **#2 spot on the brand new Live SWE-Bench** leaderboard! Plus, the 32B model runs locally on a single 3090, making this power accessible. You can also try their managed [**OpenHands Cloud**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fapp.all-hands.dev%2F) ($50 free credit). Amazing progress from this team!

Frontiers: Diffusion LMs & Superhuman Math

Two other developments pushed the boundaries this week:

Dream 7B: A Diffusion Language Model Challenger?

This one's fascinating conceptually. Researchers unveiled [**Dream 7B**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhkunlp.github.io%2Fblog%2F2025%2Fdream%2F), a language model based on **diffusion**, not auto-regression. The [**benchmarks they shared**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FJiachengYe15%2Fstatus%2F1907430553369883017) show it competing strongly with top 7-8B models, and absolutely crushing tasks like Sudoku (81% vs <50% for others), potentially due to its parallel processing nature being better for global constraints. It's an exciting hint at alternative architectures, but the **model weights aren't out yet**, so we can't verify or play with it. Still, one to watch!

Gemini 2.5 Obliterates Olympiad Math (24.4% on USAMO!)

We already knew Gemini 2.5 was good, but wow. New results dropped showing its performance on the **USA Math Olympiad (USAMO)** – problems so hard most top models score under 5%. **Gemini 2.5 Pro scored an incredible 24.4%**!

The gap between it and everything else is massive, highlighting the power of its reasoning and thinking capabilities (which you can inspect via its traces!). Having used it for complex tasks myself (like wrestling with tax forms!), I can attest to its depth. It's free in the Gemini app – go try it!

Agents, Compute & Making MCP Observable

Amazon's Nova Act Agent & The Need for Access

Amazon entered the agent chat with [**Nova Act**](https://www.google.com/url?sa=E&q=https%3A%2F%2Flabs.amazon.science%2Fblog%2Fnova-act), designed for web browser actions. They claim it beats Claude 3.5 and OpenAI's QA model on some benchmarks, possibly leveraging acquired Adept talent. But... it's only available via an SDK with a request form. As Yam rightly pointed out on the show, these agent claims mean little until we can actually *use* them in the real world!

CoreWeave + NVIDIA = Insane Speeds

Hardware keeps accelerating. CoreWeave announced hitting [**800 Tokens/sec on Llama 3.1 405B**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.prnewswire.com%2Fnews-releases%2Fcoreweave-achieves-new-record-breaking-ai-inferencing-benchmark-with-nvidia-gb200-grace-blackwell-superchips-302418682.html%3Fhss_channel%3Dtw-979803443681349632) using NVIDIA's new GB200 Blackwell chips, and 33,000 T/s on Llama 2 70B with H200s. Inference is getting *fast*.

This Week's Buzz: Let's Make MCP Observable!

Okay, my personal mission this week builds on the growing **Model Context Protocol (MCP)** momentum. MCP is potentially the "HTTP for agents," enabling tool interoperability. But as tool use moves external, we lose visibility, making debugging and security harder.

That's why I'm launching the [**Observable Tools**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fobservable.tools%2F) initiative. The goal: integrate observability *into* the MCP standard itself. Right now, that link redirects to a [**GitHub discussion**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fmodel-context-protocol%2Fspecification%2Fdiscussions%2F18) where I've proposed using the **OpenTelemetry (OTel)** standard to add tracing to MCP interactions. This would give developers clear visibility into tool usage, regardless of their observability platform.

**I need your help!** Please check out the proposal, join the discussion, and **show your support** with a 👍 or 🚀 on GitHub. We need the community voice to make this happen! (And yes, my [**viral tweet**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne%2Fstatus%2F1906180131540066796) showed there's huge demand for usable MCP clients too – more on that soon!).

Vision & Video: Entering the Uncanny Valley

This space is moving at lightning speed.

[**Runway Gen-4**](https://www.google.com/url?sa=E&q=https%3A%2F%2Frunwayml.com%2Fresearch%2Fintroducing-runway-gen-4) was announced, pushing for better consistency in AI video. Here's a few example videos showing incredible character and world consistency:

ByteDance's impressive [**OmniHuman**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fdreamina.capcut.com%2Fai-tool%2Fvideo%2Flip-sync%2Fgenerate) (single image to talking avatar) is now publicly usable via Dreamina website. For people it's really good, but for animated style images, [Hedra Labs](https://www.hedra.com/) feels actually better (and much much faster)

**Meta's **[**MoCHA**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fcongwei1230.github.io%2FMoCha%2F)** is mind-blowing.** We had researcher Cong Wei explain how it generates *movie-grade*, full-body, expressive talking characters directly from speech and text (no reference image needed!). Using Diffusion Transformers and clever attention mechanisms, the realism is startling, handling lip-sync, gestures, emotions, and even multi-character dialogue. Check the project page videos – some are truly uncanny. Just look at this one!

Voice Highlight: Hailuo Speech-02

While Gladia launched their [**Solaria STT**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.gladia.io%2Fsolaria), the standout for me was [**Hailuo's Speech-02 TTS API**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FHailuo_AI%2Fstatus%2F1906723587379101923). The emotional control and voice cloning quality are, in my opinion, potentially SOTA right now, offering incredibly nuanced and realistic synthetic voices.

Tool Update & Breaking News!

* Google's [**NotebookLM now discovers related sources**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fblog.google%2Ftechnology%2Fgoogle-labs%2Fnotebooklm-discover-sources%2F) automatically.

* **BREAKING NEWS (Caught end of show): Devin 2.0 is out!** Cognition Labs launched their AI software engineer V2 with a new IDE experience and, crucially, a **$20/month** starting price. Much more accessible to try!

Phew! What a week. From OpenAI's big moves to Gemini's math prowess, stunning AI actors from Meta, and the push for an observable agent ecosystem – the field is accelerating like crazy.

Alright folks, that’s a wrap for show #99! Thank you again for tuning in, for being part of the community, and for keeping us on our toes with your insights and feedback. Special thanks to our guests Zach Nussbaum (Nomic), Xingyao Wang (All Hands AI), and Cong Wei (Meta/MoCHA) for joining us!

If you missed any part of the show, or want to grab any of the links, head over to [**ThursdAI.news**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fthursdai.news). The full recording (video on YouTube, audio on Spotify, Apple Podcasts, etc.) and this blog post with all the notes will be up shortly.

The best way to support the show? Share it with a friend or colleague who needs to stay up-to-date on AI, and drop us a 5-star review on your podcast platform! Financial support via Substack is also appreciated but never required.

Get ready for **Episode 100** next week! Until then, happy tinkering, stay curious, and I'll see you next ThursdAI!

Bye bye everyone!

TL;DR and Show Notes

**Host, Guests, and Co-hosts**

* **Host:** Alex Volkov - AI Evangelist & Weights & Biases ([**@altryne**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne))

* **Co-Hosts:**

* LDJ ([**@ldjconfirmed**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fldjconfirmed))

* Yam Peleg ([**@yampeleg**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fyampeleg))

* **Guests:**

* Zach Nussbaum ([**@zach_nussbaum**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fzach_nussbaum)) - Nomic AI

* Xingyao Wang ([**@xingyaow_**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fxingyaow_)) - All Hands AI / OpenHands

* Cong Wei ([**@CongWei1230**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FCongWei1230)) - Meta AI / MoCha

**Key Topics & Links**

* **OpenAI's Big Week:**

* Teasing highly capable [**Open Source Reasoner Model**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fkevinweil%2Fstatus%2F1906797119848988822) (seeking [**feedback**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Fform%2Fopen-model-feedback)).

* Released [**PaperBench**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Findex%2Fpaperbench%2F) eval ([**code**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fopenai%2Fpreparedness%2Ftree%2Fmain%2Fproject%2Fpaperbench), [**paper**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fcdn.openai.com%2Fpapers%2F22265bac-3191-44e5-b057-7aaacd8e90cd%2Fpaperbench.pdf)) & [**Nano-Eval framework**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fopenai%2Fpreparedness).

* Raised [**$40B at $300B valuation**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fopenai.com%2Findex%2Finvesting-in-our-mission%2F).

* New EMO "[**Monday" voice**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FOpenAI%2Fstatus%2F1907124258867982338) in ChatGPT.

* **Open Source Powerhouses:**

* [**Nomic Embed Multimodal**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.nomic.ai%2Fblog%2Fposts%2Fnomic-embed-multimodal): SOTA visual doc embeddings (3B & 7B, [**Apache 2.0 for 7B**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fcollections%2Fnomic-ai%2Fnomic-embed-multimodal-67e5ddc1a890a19ff0d58073)).

* [**OpenHands LM 32B**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.all-hands.dev%2Fblog%2Fintroducing-openhands-lm-32b----a-strong-open-coding-agent-model): SOTA-level coding agent model (Qwen finetune, [**MIT License**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhuggingface.co%2Fall-hands%2Fopenhands-lm-32b-v0.1), 37.2% SWE-Bench, #2 Live SWE-Bench). [**Cloud version available**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fapp.all-hands.dev%2F).

* **Frontier Models & Capabilities:**

* [**Dream 7B**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fhkunlp.github.io%2Fblog%2F2025%2Fdream%2F): Promising **diffusion LM** shows strong benchmark results ([**esp. Sudoku**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FJiachengYe15%2Fstatus%2F1907430553369883017)), but weights not yet released.

* **Gemini 2.5**: Crushes hard **USAMO math eval (24.4%** vs <5% for others), showcasing superior reasoning.

* **Agents & Compute:**

* Amazon's [**Nova Act**](https://www.google.com/url?sa=E&q=https%3A%2F%2Flabs.amazon.science%2Fblog%2Fnova-act) agent announced, claims SOTA but lacks public access ([**request form**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fnova.amazon.com)).

* [**CoreWeave/NVIDIA**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.prnewswire.com%2Fnews-releases%2Fcoreweave-achieves-new-record-breaking-ai-inferencing-benchmark-with-nvidia-gb200-grace-blackwell-superchips-302418682.html%3Fhss_channel%3Dtw-979803443681349632): Massive inference speedups (800T/s on Llama 405B with GB200).

* **This Week's Buzz - MCP:**

* [**Observable Tools**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fobservable.tools%2F) initiative launched to add observability to MCP.

* Proposal using OpenTelemetry posted for [**community feedback on GitHub**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fmodel-context-protocol%2Fspecification%2Fdiscussions%2F18) - please support!

* Huge demand shown for usable MCP clients ([**viral tweet**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne%2Fstatus%2F1906180131540066796)).

* **Vision & Video Highlights:**

* [**Runway Gen-4**](https://www.google.com/url?sa=E&q=https%3A%2F%2Frunwayml.com%2Fresearch%2Fintroducing-runway-gen-4) focuses on video consistency.

* ByteDance [**OmniHuman**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fdreamina.capcut.com%2Fai-tool%2Fvideo%2Flip-sync%2Fgenerate) (image-to-avatar) now publicly available via Dreamina ([**example thread**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Faltryne%2Fstatus%2F1907173680456794187)).

* Meta's [**MoCHA**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fcongwei1230.github.io%2FMoCha%2F): Generates stunningly realistic, movie-grade talking characters from speech+text.

* **Voice Highlight:**

* [**Hailuo Speech-02**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2FHailuo_AI%2Fstatus%2F1906723587379101923): Impressive TTS API with excellent emotional control and voice cloning.

* **Tool Updates:**

* [**Windsurf adds deployments**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fx.com%2Fwindsurf_ai%2Fstatus%2F1907497638267924566) to Netlify.

* Google [**NotebookLM adds source discovery**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fblog.google%2Ftechnology%2Fgoogle-labs%2Fnotebooklm-discover-sources%2F).

* **Breaking News:**

* **Devin 2.0** AI Software Engineer announced, starts at $20/month. 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-apr-3rd-openai-goes-open/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-apr-3rd-openai-goes-open?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2MDUyMzI3MiwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.KeKD6SiF3Lcp_XPFGAtxcXxrkuK6rVe0xzzZqGXzZ8M&utm_campaign=CTA_5).

---

