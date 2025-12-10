# 📆 ThursdAI - Jul 10 - Grok 4 and 4 Heavy, SmolLM3, Liquid LFM2, Reka Flash & Vision, Perplexity Comet Browser, Devstral 1.1 & More AI News

**Date:** July 11, 2025  
**Duration:** 1:49:46  
**Link:** [https://sub.thursdai.news/p/thursdai-jul-10-grok-4-and-4-heavy](https://sub.thursdai.news/p/thursdai-jul-10-grok-4-and-4-heavy)

---

## Description

Hey everyone, Alex here

Don't you just love "new top LLM" drop weeks? I sure do! This week, we had a watch party for Grok-4, with over 20K tuning in to watch together, as the folks at XAI unveiled their newest and best model around. Two models in fact, Grok-4 and Grok-4 Heavy. 

We also had a very big open source week, we had the pleasure to chat with the creators of 3 open source models on the show, first with Elie from HuggingFace who just released SmoLM3, then with our friend Maxime Labonne who together with Liquid released a beautiful series of tiny on device models. 

Finally we had a chat with folks from Reka AI, and as they were on stage, someone in their org published a new open source Reka Flash model 👏 Talk about Breaking News right on the show! 

It was a very fun week and a great episode, so grab your favorite beverage and let me update you on everything that's going on in AI (as always, show notes at the end of the article) 

Open Source LLMs

As always, even on big weeks like this, we open the show with Open Source models first and this week, the western world caught up to the Chinese open source models we saw last week! 

HuggingFace SmolLM3 - SOTA fully open 3B with dual reasoning and long-context ([𝕏](https://x.com/LoubnaBenAllal1/status/1942614508549333211), [HF](https://huggingface.co/blog/smollm3))

We had Eli Bakouch from Hugging Face on the show and you could feel the pride radiating through the webcam. SmolLM 3 isn’t just “another tiny model”; it’s an 11-trillion-token monster masquerading inside a 3-billion-parameter body. It reasons, it follows instructions, and it does both “think step-by-step” and “give me the answer straight” on demand. Hugging Face open-sourced every checkpoint, every dataset recipe, every graph in W&B – so if you ever wanted a fully reproducible, multi-lingual pocket assistant that fits on a single GPU, this is it.

They achieved the long context (128 K today, 256 K in internal tests) with a NoPE + YaRN recipe and salvaged the performance drop by literally merging two fine-tunes at 2 a.m. the night before release. Science by duct-tape, but it works: SmolLM 3 edges out Llama-3.2-3B, challenges Qwen-3, and stays within arm’s reach of Gemma-3-4B – all while loading faster than you can say “model soup.” 🤯

Liquid AI’s LFM2: Blazing-Fast Models for the Edge ([𝕏](https://x.com/maximelabonne/thread/1943295061275381864), [Hugging Face](https://huggingface.co/collections/LiquidAI/lfm2-686d721927015b2ad73eaa38))

We started the show and I immediately got to hit the #BREAKINGNEWS button, as Liquid AI dropped LFM2, a new series of tiny (350M-1.2B) models focused on Edge devices.

We then had the pleasure to host our friend Maxime Labonne, head of Post Training at Liquid AI, to come and tell us all about this incredible effort! 

Maxime, a legend in the model merging community, explained that LFM2 was designed from the ground up for efficiency. They’re not just scaled-down big models; they feature a novel hybrid architecture with convolution and attention layers specifically optimized for running on CPUs and devices like the Samsung Galaxy S24.

Maxime pointed out that Out of the box, they won't replace ChatGPT, but when you fine-tune them for a specific task like translation, they can match models 60 times their size. This is a game-changer for creating powerful, specialized agents that run locally. Definitely a great release and on ThursdAI of all days! 

Mistrals updated Devstral 1.1 Smashes Coding Benchmarks ([𝕏](https://x.com/MistralAI/status/1943316390863118716), [HF](https://huggingface.co/mistralai/Devstral-Small-2507))

Mistral didn't want to be left behind on this Open Source bonanza week, and also, today, dropped an update to their excellent coding model Devstral. 

With 2 versions, an open weights Small and API-only Medium model, they have claimed an amazing 61.6% score on Swe Bench and the open source Small gets a SOTA 53%, the highest among the open source models! 10 points higher than the excellent DeepSwe we covered just last week!

The thing to watch here is the incredible price performance, with this model beating Gemini 2.5 Pro and Claude 3.7 Sonnet while being 8x cheaper to run! 

DevStral small comes to us with an Apache 2.0 license, which we always welcome from the great folks at Mistral! 

Big Companies LLMs and APIs

There's only 1 winner this week, it seems that other foundational labs were very quiet to see what XAI is going to release. 

XAI releases Grok-4 and Grok-4 heavy - the world leading reasoning model ([𝕏](https://x.com/altryne/status/1943140257920172148), [Try It](https://grok.com/)) 

Wow, what a show! Space uncle Elon together with the XAI crew, came fashionably late to their own stream, and unveiled the youngest but smartest brother of the Grok family, Grok 4 plus a multiple agents swarm they call Grok Heavy. We had a watch party with over 25K viewers across all streams who joined and watched together, this, fairly historic event! 

Why historic? Well, for one, they have scaled RL (Reinforcement Learning) for this model significantly more than any other lab did so far, which resulted in an incredible reasoner, able to solve HLE (Humanity's Last Exam) benchmark at an unprecedented 50% (while using tools) 

The other very much unprecedented result, is on the ArcAGI benchmark, specifically V2, which is designed to be very easy for humans and very hard for LLMs, Grok-4 got an incredible 15.9%, almost 2x better than Opus 4 the best performing model before it! (ArcAGI president Greg Kamradt [says](https://x.com/GregKamradt/status/1943169631491100856) it Grok-4 shows signs of Fluid Intelligence!)

Real World benchmarks

Of course, academic benchmarks don't tell the full story, and while it's great to see that Grok-4 gets a perfect 100% on AIME25 and a very high 88.9% on GPQA Diamond, the most interesting benchmark they've showed was the Vending-Bench. This is a very interesting new benchmark from AndonLabs, where they simulate a vending machine, and let an LLM manage it, take orders, restock and basically count how much money a model can make while operating a "real" business. 

Grok scored a very significant $4K profit, selling 4569 items, 4x more than Opus, which shows a real impact on real world tasks! 

Not without controversy

Grok-4 release comes just 1 day after Grok-3 over at X, started calling itself MechaHitler and started spewing Nazi Antisemitic propaganda, which was a very bad episode. We've covered the previous "misalignment" from Grok, and this seemed even worse. Many examples (which XAI folks deleted) or Grok talking about Antisemitic tropes, blaming people with Jewish surnames for multiple things and generally acting jailbroken and up to no good.

Xai have addressed the last episode by a token excuse, supposedly open sourcing their prompts, which were updated all of 4 times in the last 2 month, while addressing this episode with a "we noticed, and we'll add guardrails to prevent this from happening" 

IMO this isn't enough, Grok is consistently (this is the 3rd time on my count) breaking alignment, way more than other foundational LLMs, and we must ask for more transparency for a model as significant and as widely used as this! And to my (lack of) surprise

First principles thinking == Elon's thoughts? 

Adding insult to injury, while Grok-4 was just launched, some folks asked it thoughts on the Israel-Palestine conflict and instead of coming up with an answer on its own, Grok-4 did a [X search](https://x.com/jeremyphoward/status/1943436621556466171) to see what Elon Musk things on this topic to form its opinion. It's so so wrong to claim a model is great at "first principles" and have the first few tests from folks, show that Grok defaults to see "what Elon thinks" 

Look, I'm all for "moving fast" and of course I love AI progress, but we need to ask more from the foundational labs, especially given the incredible amount of people who count on these models more and more! 

This weeks Buzz

We're well over 300 registrations to our hackathon at the Weights & Biases SF officess this weekend (July 12-13) and I'm packing my suitcase after writing this, as I'm excited to see all the amazing projets folks will build to try and win over $15K in prizes including an awesome ROBODOG

Not to late to come and hack with us, register at [lu.ma/weavehacks](http://lu.ma/weavehacks) 

Tools – Browsers grow brains

Perplexity’s **Comet** landed on my Mac and within ten minutes it was triaging my LinkedIn invites by itself. This isn’t a Chrome extension; it’s a Chromium fork where natural-language commands are first-class citizens. Tell it “find my oldest unread Stripe invoice and download the PDF” and watch the mouse move. The Gmail connector lets you ask, “what flights do I still need to expense?” and get a draft report. Think Cursor, but for every tab.

I [benchmarked](https://x.com/altryne/status/1943012655817544142) Comet against OpenAI Operator on my “scroll Alex’s 200 tweet bookmarks, extract the juicy links, drop them into Notion” task—Operator died halfway, Comet almost finished. Almost. The AI browser war has begun; Chrome’s Mariner project and OpenAI’s rumored Chromium team better move fast. 

Comet is available to Perplexity MAX subscribers now, and will come to pro subscribers with invites soon, as soon as I'll have them I'll tell you how to get one! 

Vision & Video

Reka dropped in with a double-whammy of announcements. First, they showcased **Reka Vision**, an agentic platform that can search, analyze, and even edit your video library using natural language. The demo of it automatically generating short-form social media reels from long videos was super impressive.

Then, in a surprise live reveal, they dropped **Reka Flash 3.1**, a new 21B parameter *open-source* multimodal model! It boasts great performance on coding and math benchmarks, including a 65% on AIME24. It was awesome to see them drop this right on the show.

We also saw LTX Video release three new open-source LoRAs for precise video control (Pose, Depth, and Canny), and Moonvalley launched **Marey**, a video model for filmmakers that's built exclusively on licensed, commercially-safe data—a first for the industry.

Veo3 making talking pets

Google have released an update to VEO 3, allowing you to upload an image and have the characters in the image say what you want! It’s really cool for human like generations, but it’s way more fun to animate… your pets! Here’s two of the best doggos in Colorado presenting themselves! 

The full prompt to create your own after you upload an image was: 

Two dogs presenting themselves, the left one barking first and then saying "Hey, I'm George Washington Fox" and the right dog following up with a woof and then says "and I'm his younger brother, Dr Emmet Brown". 

Then both are saying "we're good boys" and barking

Both should sound exiting with an american accent and a dog accent

Phew, what a week! From open source Breaking News from the folks who trained the models right on the podcast, to watch parties and Nazi LLMs, this has been one hell of a ride! 

Next week, there are already rumors of a potential Gemini 3 release, the OpenAI open source model is rumored to be dropping, and I'm sure we'll get all kinds of incredible things lined up + it's going to be my birthday on Thursday so, looking forward! 

See you next week 🫡

Show notes and Links

TL;DR of all topics covered:

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@WolframRvnwlf](http://x.com/@WolframRvnwlf) [@yampeleg](x.com/@yampeleg) [@nisten](http://x.com/@nisten) [@ldjconfirmed](http://x.com/@ldjconfirmed)) [@ryancarson](http://x.com/@ryancarson)

* Guests

* Elie Bakouch - Training at Hugging Face ([@eliebakouch](https://x.com/eliebakouch))

* Maxime Labonne - Head of postrainig and Liquid AI ([@maximelabonne](https://twitter.com/maximelabonne/status/1943295061275381864)) author of [LLM-Course](https://github.com/mlabonne/llm-course)

* Mattia Atzeni - Member of Technical Staff @ Reka

* Meenal Nalwaya - Head of Product, Reka Al

* **Open Source LLMs**

* HuggingFace - SmolLM3 SOTA, fully open-source 3B dual-mode reasoning and long-context support ([X](https://x.com/LoubnaBenAllal1/status/1942614508549333211), [HF](https://huggingface.co/blog/smollm3))

* Liquid AI launches LFM2: the fastest, most efficient open-source edge LLMs yet ([X](https://x.com/maximelabonne/thread/1943295061275381864), [HF](https://huggingface.co/collections/LiquidAI/lfm2-686d721927015b2ad73eaa38))

* Reachy Mini: Hugging Face and Pollen Robotics launch a $299 open-source desktop robot ([X](https://x.com/Thom_Wolf/status/1942887160983466096), [HF](https://huggingface.co/blog/reachy-mini))

* NextCoder-32B: Microsoft’s new code-editing LLM rivals GPT-4o on complex code tasks ([Microsoft Research](https://www.microsoft.com/en-us/research/publication/nextcoder-robust-adaptation-of-code-lms-to-diverse-code-edits/), [HF](https://huggingface.co/microsoft/NextCoder-32B))

* Mistral AI updates Devstral Small 1.1 and Devstral Medium, setting new open-source coding agent benchmarks ([X](https://x.com/MistralAI/status/1943316390863118716), [HF](https://huggingface.co/mistralai/Devstral-Small-2507), [Blog](https://mistral.ai/news/devstral-2507))

* Reka updates RekaFlash 1.1 ([HF](https://huggingface.co/RekaAI/reka-flash-3.1))

* **Big CO LLMs + APIs**

* 👑 Grok 4 Release: A Historic Leap from XAI - Grok 4 and Grok 4 heavy [X](https://x.com)

* Grok 3 is going nazi racing on X - MeinPrompt gate ([X](https://x.com/altryne/status/1943077695178391572))

* Gemini API Batch Mode launches with 50% cost savings for large-scale AI jobs ([X](https://x.com/_philschmid/status/1942238040593699077), [Google Blog](https://developers.googleblog.com/en/scale-your-ai-workloads-batch-mode-gemini-api/))

* **This weeks Buzz**

* W&B Hackathon is nearing capacity - Robodog is ready to be given out ([lu.ma/weavehacks](https://lu.ma/weavehacks))

* **Vision & Video**

* Reka Vision: Multimodal Agent for Visual Understanding and Search ([Reka on X](https://x.com/RekaAILabs/status/1942621988390088771), [Vision app](https://app.reka.ai/vision))

* LTX Video launches 3 open-source LoRAs for video control: Pose, Depth, Canny ([LTX Studio on X](https://x.com/LTXStudio/status/1942604844449292614), [GitHub](https://github.com/Lightricks/LTX-Video), [HF model](https://huggingface.co/Lightricks/LTX-Video))

* Marey by Moonvalley: the first professional, licensed AI video tool built for creative control ([Moonvalley on X](https://x.com/moonvalley/status/1942570142430552163), [Product page](https://www.moonvalley.com/marey))

* **Tools**

* Perplexity Launches Comet: The AI-Powered Browser for Modern Productivity ([X](https://x.com/AravSrinivas/thread/1942968552727941477), [HF](https://huggingface.co/perplexity-ai)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jul-10-grok-4-and-4-heavy/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jul-10-grok-4-and-4-heavy?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2ODAzMTUwMCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.vsmVuc4JlKQvitqu75NwpWjhYA6cXbfPNkHcHRJOqPQ&utm_campaign=CTA_5).
