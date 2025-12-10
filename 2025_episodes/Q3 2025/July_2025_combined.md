# ThursdAI Episodes - July 2025

Total Episodes: 4

---

## 📆 ThursdAI - July 24, 2025 - Qwen-mas in July, The White House's AI Action Plan & Math Olympiad Gold for AIs + coding a 3d tetris on stream

**Date:** July 24, 2025  
**Duration:** 1:43:23  
**Link:** [https://sub.thursdai.news/p/thursdai-july-24-2025-qwen-mas-in](https://sub.thursdai.news/p/thursdai-july-24-2025-qwen-mas-in)

What a WEEK! Qwen-mass in July. Folks, AI doesn't seem to be wanting to slow down, especially Open Source! This week we see yet another jump on SWE-bench verified (3rd week in a row?) this time from our friends at Alibaba Qwen. 

Was a pleasure of mine to host Junyang Lin from the team at Alibaba to come and chat with us about their incredible release with, with not 1 but three new models! 

Then, we had a great chat with Joseph Nelson from Roboflow, who not only dropped additional SOTA models, but was also in Washington at the annocement of the new AI Action plan from the WhiteHouse. 

Great conversations this week, as always, TL;DR in the end, tune in! 

Open Source AI - QwenMass in July

This week, the open-source world belonged to our friends at Alibaba Qwen. They didn't just release one model; they went on an absolute tear, dropping bomb after bomb on the community and resetting the state-of-the-art multiple times.

**A "Small" Update with Massive Impact: Qwen3-235B-A22B-Instruct-2507**

Alibaba called this a *minor* refresh of their 235B parameter mixture-of-experts.

Sure—if you consider +13 points on GPQA, 256K context window minor. The 2507 drops hybrid thinking. Instead, Qwen now ships separate instruct and chain-of-thought models, avoiding token bloat when you just want a quick answer. Benchmarks? 81 % MMLU-Redux, 70 % LiveCodeBench, new SOTA on BFCL function-calling. All with 22 B active params.

Our friend of the pod, and head of development at Alibaba Qwen, Junyang Lin, join the pod, and talked to us about their decision to uncouple this model from the hybrid reasoner Qwen3.

"After talking with the community and thinking it through," he said, "we decided to stop using hybrid thinking mode. Instead, we'll train instruct and thinking models separately so we can get the best quality possible."

The community felt the hybrid model sometimes had conflicts and didn't always perform at its best. So, Qwen delivered a pure non-reasoning instruct model, and the results are staggering. Even without explicit reasoning, it's crushing benchmarks. Wolfram tested it on his MMLU-Pro benchmark and it got the top score of all open-weights models he's ever tested. Nisten saw the same thing on medical benchmarks, where it scored the highest on MedMCQA. This thing is a beast, getting a massive 77.5 on GPQA (up from 62.9) and 51.8 on LiveCodeBench (up from 32). This is a huge leap forward, and it proves that a powerful, well-trained instruct model can still push the boundaries of reasoning.

** The New (open) King of Code: Qwen3-Coder-480B (**[**X**](https://x.com/Alibaba_Qwen/status/1947766835023335516)**, **[**Try It**](https://wandb.me/qcoder-colab)**, **[**HF**](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct)**)**

Just as we were catching our breath, they dropped the main event: **Qwen3-Coder**. This is a 480-billion-parameter coding-specific behemoth (35B active) trained on a staggering 7.5 trillion tokens, with a 70% code ratio, that gets a new SOTA on SWE-bench verified with 69.6% (just a week after Kimi got SOTA with 65% and 2 weeks after Devstral's SOTA of 53% 😮) 

To get this model to SOTA, Junyang explained they used reinforcement learning with over 20,000 parallel sandbox environments. This allows the model to interact with the environment, write code, see the output, get the reward, and learn from it in a continuous loop. The results speak for themselves.

With long context abilities 256K with up to 1M extended with YaRN, this coding beast tops the charts, and is achieving Sonnet level performance for significantly less cost! 

Both models supported day-1 on W&B Inference ([X](https://x.com/weights_biases/status/1947859654400434538), [Get Started](https://wandb.me/qcoder-colab))

I'm very very proud to announce that both these incredible models get Day-1 support on our W&B inference (and that yours truly is now part of the decision of which models we host!) 

With unbeatable prices ($0.10/$0.10 input/output 1M for A22B, $1/$1.5 for Qwen3 Coder) and speed, we are hosting these models at full precision to give you the maximum possible intelligence and the best bang for your buck! 

Nisten has setup our (OpenAI compatible) endpoint with his Cline coding assistant and has built a 3D Tetris game live on the show, and it absolutely went flying. 

This demo perfectly captures the convergence of everything we're excited about: a state-of-the-art open-source model, running on a blazing-fast inference service, integrated into a powerful open-source tool, creating something complex and interactive in seconds.

If you want to try this yourself, we're giving away credits for W&B Inference. Just find our [announcement tweet](https://x.com/weights_biases/status/1947859654400434538) for the Qwen models on the **@weights_biases** X account and reply with **"coding capybara"** (a nod to Qwen's old mascot!). Add "ThursdAI" and I'll personally make sure you get bumped up the list!

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Big Companies & APIs

**America’s AI Action Plan: A New Space Race for AI Dominance (**[**ai.gov**](ai.gov)**)**

Switching gears to policy, I’m was excited to cover the White House’s newly unveiled “America’s AI Action Plan.” This 25-page strategy, dropped this week, frames AI as a national priority on par with the space race or Cold War, aiming to secure U.S. dominance with 90 policy proposals. I was thrilled to have Joseph Nelson from RoboFlow join us fresh from the announcement event in Washington, sharing the room’s energy and insights. The plan pushes for deregulation, massive data center buildouts, workforce training, and—most exciting for us—explicit support for open-source and open-weight models. It’s a bold move to counter global competition, especially from China, while fast-tracking infrastructure like chip fabrication and energy grids.

Joseph broke down the vibe at the event, including a surreal moment where the President riffed on Nvidia’s market dominance right in front of Jensen Huang. But beyond the anecdotes, what strikes me is the plan’s call for startups and innovation—think grants and investments via the Department of Defense and Small Business Administration. It’s like a request for new AI companies to step up. As someone who’s railed against past moratorium fears on this show, seeing this pro-innovation stance is a huge relief.

**🔊 Voice & Audio – Higgs Audio v2 Levels Up (**[**X**](https://x.com/reach_vb/status/1947997596456272203)**)**

Boson AI fused a 3B-param Llama 3.2 with a 2.2B audio Dual-FFN and trained on ten million hours of speech + music. Result: Higgs Audio v2 beats GPT-4o-mini and ElevenLabs v2 on prosody, does zero-shot multi-speaker dialog, and even hums melodies. The demo runs on a single A100 and sounds pretty-good. 

The first demo I played was not super impressive, but the laugh track made up for it! 

**🤖 A Week with ChatGPT Agent**

Last week, OpenAI dropped the ChatGPT Agent on us during our stream, and now we've had a full week to play with it. It's a combination of their browser-operating agent and their deeper research agent, and the experience is pretty wild.

Yam had it watching YouTube videos and scouring Reddit comments to create a comparison of different CLI tools. He was blown away, seeing the cursor move around and navigate complex sites right on his phone.

I put it through its paces as well. I tried to get it to order flowers for my girlfriend (it got all the way to checkout!), and it successfully found and filled out the forms for a travel insurance policy I needed. My ultimate test ([live stream here](https://x.com/altryne/status/1948111176203911222)), however, was asking it to prepare the show notes for ThursdAI, a complex task involving summarizing dozens of my X bookmarks. It did a decent job (a solid C/B), but still needed my intervention. It's not quite a "fire-and-forget" tool for complex, multi-step tasks yet, but it's a huge leap forward. As Yam put it, "This is the worst that agents are going to be." And that's an exciting thought.

What a week. From open-source models that rival the best closed-source giants to governments getting serious about AI innovation, the pace is just relentless. It's moments like Nisten's live demo that remind me why we do this show—to witness and share these incredible leaps forward as they happen. We're living in an amazing time.

Thank you for being a ThursdAI subscriber. As always, here's the TL;DR and show notes for everything that happened in AI this week.

Thanks for reading ThursdAI - Recaps of the most high signal AI weekly spaces! This post is public so feel free to share it.

TL;DR and Show Notes

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/altryne))

* **Co-Hosts** - [@WolframRvnwlf](http://x.com/WolframRvnwlf), [@yampeleg](http://x.com/yampeleg), [@nisten](http://x.com/nisten), [@ldjconfirmed](http://x.com/ldjconfirmed)

* **Junyang Lin** - Qwen Team, Alibaba ([@JustinLin610](https://x.com/JustinLin610))

* **Joseph Nelson** - Co-founder & CEO, Roboflow ([@josephnelson](https://x.com/josephnelson))

* **Open Source LLMs**

* Sapient Intelligence releases **Hierarchical Reasoning Model (HRM)**, a tiny 27M param model with impressive reasoning on specific tasks ([X](https://x.com/makingAGI/status/1947286324735856747), [arXiv](https://arxiv.org/abs/2506.21734)).

* Qwen drops a "little" update: **Qwen3-235B-A22B-Instruct-2507**, a powerful non-reasoning model ([X](https://x.com/JustinLin610/status/1947364588340523222), [HF Model](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)).

* Qwen releases the new SOTA coding agent model: **Qwen3-Coder-480B-A35B-Instruct** ([X](https://x.com/Alibaba_Qwen/status/1947790753414369280), [HF Model](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct)).

* **Hermes-Reasoning Tool-Use dataset** with 51k tool-calling examples is released ([X](httpshttps://x.com/intstr1Irinja/status/1947444760393773185), [HF Dataset](https://huggingface.co/datasets/interstellarninja/hermes_reasoning_tool_use)).

* NVIDIA releases updates to their **Nemotron** reasoning models.

* **Big CO LLMs + APIs**

* The White House unveils **"America’s AI Action Plan"** to "win the AI race" ([X](https://x.com/NetChoice/status/1948042669906624554), [White House PDF](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf)).

* Both **OpenAI** ([X](https://x.com/alexwei_/status/1946477742855532918)) and **Google DeepMind** win Gold at the International Math Olympiad (IMO), with **ByteDance's Seed-Prover** taking Silver ([GitHub](https://github.com/ByteDance-Seed/Seed-Prover)).

* The AI math breakthrough has a "gut punch" effect on the math community ([Dave White on X](https://x.com/Dave_White_/status/1947461492783386827)).

* Google now processes over **980 trillion tokens** per month across its services.

* A week with **ChatGPT Agent**: testing its capabilities on real-world tasks.

* **This Week's Buzz**

* Day 0 support for both new Qwen models on **W&B Inference** ([Try it](https://wandb.ai/inference), [Colab](https://wandb.me/qcoder-colab)). Reply to our [tweet](https://x.com/weightsandbiases) with "coding capybara ThursdAI" for credits!

* Live on-stream demo of Qwen3-Coder building a 3D Tetris game using kline.

* **Interesting Research**

* Researchers discover **subliminal learning** in LLMs, where traits are passed through seemingly innocuous data ([X](https://x.com/0wain_evans/status/1947709848103255232), [arXiv](https://arxiv.org/abs/2507.14805)).

* Apple proposes **multi-token prediction**, speeding up LLMs by up to 5x without quality loss ([X](https://x.com/JacksonAtkinsX/status/1947408593638002639), [arXiv](https://arxiv.org/abs/2507.11851)).

* **Voice & Audio**

* Boson AI open-sources **Higgs Audio v2**, a unified TTS model that beats GPT-4o-mini and ElevenLabs ([X](https://x.com/reach_vb/status/1947997596456272203), [HF Model](https://huggingface.co/bosonai/higgs-audio-v2-generation-3B-base)).

* **AI Art & Diffusion & 3D**

* Decart AI Releases **MirageLSD**, a real-time live-stream diffusion model for instant video transformation ([X Post](https://x.com/DecartAI/status/1945947692871692667)).

* **Tools**

* Qwen releases **qwen-code**, a CLI tool and agent for their new coder models. ([Github](https://github.com/QwenLM/qwen-code))

* **GitHub Spark**, a new AI-powered feature from GitHub ([Simon Willison on X](https://x.com/simonw/status/1948407932418457968)). 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-july-24-2025-qwen-mas-in/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-july-24-2025-qwen-mas-in?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2OTE3NDY2MywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.jguKI_sBQiDelSUjIO_nJjh0YQaml0qeUsh32Nk1NXE&utm_campaign=CTA_5).

---

## 📆 ThursdAI - July 17th - Kimi K2 👑, OpenAI Agents, Grok Waifus, Amazon Kiro, W&B Inference & more AI news!

**Date:** July 17, 2025  
**Duration:** 1:45:29  
**Link:** [https://sub.thursdai.news/p/thursdai-july-17th-kimi-k2-openai](https://sub.thursdai.news/p/thursdai-july-17th-kimi-k2-openai)

Hey everyone, Alex here 👋 and WHAT a week to turn a year older! Not only did I get to celebrate my birthday with 30,000+ of you live during the OpenAI stream, but we also witnessed what might be the biggest open-source AI release since DeepSeek dropped. Buckle up, because we're diving into a trillion-parameter behemoth, agentic capabilities that'll make your head spin, and somehow Elon Musk decided Grok waifus are the solution to... something.

This was one of those weeks where I kept checking if I was dreaming. Remember when DeepSeek dropped and we all lost our minds? Well, buckle up because Moonshot's Kimi K2 just made that look like a warm-up act. And that's not even the wildest part of this week! 

As always, all the show notes and links are at the bottom, here's our liveshow (which included the full OAI ChatGPT agents watch party) - Let's get into it! 

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

**🚀 Open Source LLMs: The Kimi K2 Revolution**

**The New Open Source King Has Arrived**

Folks, I need you to understand something - just a little after we finished streaming last week celebrating Grok 4, a company called Moonshot decided to casually drop what might be the most significant open source release since... well, maybe ever?

**Kimi K2** is a 1 trillion parameter model. Yes, you read that right - TRILLION. Not billion. And before you ask "but can my GPU run it?" - this is an MOE (Mixture of Experts) with only 32B active parameters, which means it's actually usable while being absolutely massive.

Let me give you the numbers that made my jaw drop:

* **65.8% on SWE-bench Verified** - This non-reasoning model beats Claude Sonnet (and almost everything else)

* **384 experts** in the mixture (the scale here is bonkers)

* **128K context window** standard, with rumors of 2M+ capability

* Trained on **15.5 trillion tokens** with the new Muon optimizer

The main thing about the SWE-bench score is not even just the incredible performance, it's the performance without thinking/reasoning + price! 

**The Muon Magic**

Here's where it gets really interesting for the ML nerds among us. These folks didn't use AdamW - they used a new optimizer called Muon (with their own Muon Clip variant). Why does this matter? They trained to 15.5 trillion tokens with ZERO loss spikes. That beautiful loss curve had everyone in our community slack channels going absolutely wild. 

As Yam explained during the show, claiming you have a better optimizer than AdamW is like saying you've cured cancer - everyone says it, nobody delivers. Well, Moonshot just delivered at 1 trillion parameter scale.

**Why This Changes Everything**

This isn't just another model release. This is "Sonnet at home" if you have the hardware. But more importantly:

* **Modified MIT license** (actually open!)

* **5x cheaper than proprietary alternatives**

* **Base model released** (the first time we get a base model this powerful)

* Already has **Anthropic-compatible API** (they knew what they were doing)

The vibes are OFF THE CHARTS. Every high-taste model tester I know is saying this is the best open source model they've ever used. It doesn't have that "open source smell" - it feels like a frontier model because it IS a frontier model.

**Not only a math genius**

Importantly, this model is great at multiple things, as folks called out it's personality or writing style specifically! Our Friend Sam Paech, creator of [EQBench](https://eqbench.com/), has noted that this is maybe the first time an open source model writes this well, and is in fact SOTA on his Creative Writing benchmark and EQBench! 

**Quick Shoutouts**

Before we dive deeper, huge props to:

* **Teknium** for dropping the Hermes 3 dataset (nearly 1M high-quality entries!) ([X](https://x.com/Teknium1/status/1945259797517099126))

* **LG** (yes, the fridge company) for EXAONE 4.0 - their 32B model getting 81.8% on MMLU Pro is no joke ([X](https://x.com/testingcatalog/status/1945142194303537225))

**🎉 This Week's Buzz: W&B Inference Goes Live with Kimi-K2! (**[**X**](https://x.com/weights_biases/status/1945204732735447222)**)**

Ok, but what if you want to try Kimi-K2 but don't have the ability to run 1T models willy nilly? Well, Folks, I've been waiting TWO AND A HALF YEARS to say this: **We're no longer GPU poor!**

Weights & Biases + CoreWeave = Your new inference playground. We launched Kimi K2 on our infrastructure within 3 days of release! 

Sitting behind the scenes on this launch was surreal - as I've been covering all the other inference service launches, I knew exactly what we all want, fast inference, full non-quantized weights, OpenAI API compatibility, great playground to test it out, function calling and tool use. And we've gotten almost all of these, while the super cracked CoreWeave and W&B Weave teams worked their ass off over the weekend to get this shipped in just a few days! 

And here’s the kicker: I’m giving away $50 in inference credits to 20 of you to try Kimi K2 on our platform. Just reply “K2-Koolaid-ThursdAI” to our X launch post [here](https://x.com/weights_biases/status/1945204732735447222) and we'll pick up to 20 winners with $50 worth of credits! 🫡

It’s live now at [**api.inference.wandb.ai/v1**](api.inference.wandb.ai/v1) (model ID: moonshotai/Kimi-K2-Instruct), fully integrated with Weave for tracing and evaluation. We’re just getting started, and I want your feedback to make this even better. More on [**W&B Inference Docs**](https://weave-docs.wandb.ai/guides/integrations/inference/#advanced-example-use-weave-evaluations-and-leaderboards-with-the-inference-service) - oh and everyone gets $2 free even without me, which is like 500K tokens to test it out.

Big CO LLMs + APIs

The big players didn't sleep this week either—funding flew like confetti, Grok went full anime, and OpenAI dropped agents mid-stream (we reacted live!). Amazon snuck in with dev tools, and Gemini embeddings claimed the throne. Let's get through some of these openers before we get to the "main course" which of course came from OpenAI

**Grok Gets... Waifus?**

I can't believe I'm writing this in a serious AI newsletter, but here we are. XAI added animated 3D characters to Grok, including "Annie" - and let's just say she's very... interactive. XAI partnered with a company that does real time animated 3d avatars and these are powered by Grok so... they are a bit unhinged! 

The same Elon who's worried about birth rates just created nuclear-grade digital companions. The Grok app shot to #1 in the Japanese App Store immediately. Make of that what you will. 😅

They even posted a job for "Full Stack Waifu Engineer" - we truly live in the strangest timeline.

XAI also this week [addressed](https://x.com/xai/status/1945039609840185489) the concerns we all had with "mechahitler" and the Grok4 issues post launch (where it used it's web search to see "what does Elon think" when it was asked about a few topics) 

Credit for finding the prompt change: Simon Willison

**Other Quick Hits from Big Tech**

* **Gemini Embedding Model**: New SOTA on MTEB leaderboards (68.32 score) ([dev blog](https://developers.googleblog.com/en/gemini-embedding-text-model-now-available-gemini-api/))

* **Amazon S3 Vectors**: Native vector storage in S3 (huge for RAG applications) ([X](https://x.com/awscloud/status/1945271447619809504))

* **Amazon Kiro**: Their VS Code fork with spec-driven development (think PM-first coding) ([X](https://x.com/ajassy/status/1944785963663966633))

**🔥 OpenAI Agents: ChatGPT Levels Up to Do-It-All Sidekick **

We timed it perfectly—OpenAI's live stream hit mid-show, and we reacted with 30,000+ of you! And while we didn't get the rumored Open Source model from OAI, we did get... ChatGPT Agent (codename Odyssey) which merges Deep Research's fast-reading text browser with Operator's clicky visual browser and terminal access, all RL-tuned to pick tools smartly. It browses, codes, calls APIs (Google Drive, GitHub, etc., if you connect), generates images, and builds spreadsheets/slides—handling interruptions, clarifications, and takeovers for collaboration. **SOTA jumps: 41.6% on Humanities Last Exam (double O3), 27.4% on FrontierMath**, 45.5% on SpreadsheetBench, 68.9% on BrowseComp.

These are insane jumps in capabilities folks, just... mindblowing that we can now have agents that are SO good! 

The team demoed wedding planning (outfits, hotels, gifts with weather/venue checks), sticker design/ordering, and an MLB itinerary spreadsheet—wild to watch it chain thoughts on recordings. 

Wolfram called it the official start of agent year; Yam hyped the product polish (mobile control!); Nisten noted it's packaged perfection over DIY. I refreshed ChatGPT obsessively—mind-blown at turning my phone into a task master. Available now for Pro/Plus/Team (400/40 queries/month), Enterprise soon. This is the "feel the AGI" moment Sam mentioned—game over for tedious tasks (OpenAI announcement: [**https://openai.com/index/introducing-chatgpt-agent/**](https://openai.com/index/introducing-chatgpt-agent/).)[).](https://openai.com/index/introducing-chatgpt-agent/).)

I've yet to get access to it, but I'm very much looking forward to testing it out and letting you guys know how it works! 

Combining the two browser modes (visual that has my cookies and textual that can scan tons of websites super quick) + CLI + deep research abilities + RL for the right kind of tool use all sounds incredibly intriguing! 

**Vision & Video**

**Runway’s Act-Two: Motion Capture Gets a Major Upgrade **([X](https://x.com/runwayml/status/1945189222542880909), [YouTube](https://www.youtube.com/watch?v=JW8PHlFD7HM))

Runway’s latest drop, Act-Two, is a next-gen motion capture model that’s got creatives buzzing. It tracks head, face, body, and hands with insane fidelity, animating any character from a single performance video. It’s a huge leap from Act-One, already in use for film, VFX, and gaming, and available now to enterprise and creative customers with a full rollout soon. 

**Voice & Audio**

**Mistral’s Voxtral: Open Speech Recognition Champ **([X](https://x.com/MistralAI/status/1945130173751288311), [HF](https://huggingface.co/mistralai))

Mistral AI is killing it with Voxtral, a state-of-the-art open speech recognition model. With Voxtral Small at 24B for production and Mini at 3B for edge devices, it outperforms OpenAI’s Whisper large-v3 across English and multilingual tasks like French, Spanish, Hindi, and German. Supporting up to 32K token context (about 30-40 minutes of audio), it offers summarization and Q&A features, all under an Apache 2.0 license. At just $0.001 per minute via API, it’s a steal for real-time or batch transcription. 

**Tools**

**Liquid AI’s LEAP and Apollo: On-Device AI for All**

Liquid AI is bringing AI to your pocket with LEAP, a developer platform for building on-device models, and Apollo, a lightweight iOS app to run small LLMs locally. We’re talking 50-300MB models optimized for minimal battery drain and instant inference, no cloud needed. It’s privacy-focused and plug-and-play, perfect for offline workflows on Android and iOS. Developers, this is your prototyping dream—join the community via **X**.

**Amazon Kiro: Your Spec-Driven Coding Buddy**

I’ve already touched on Amazon’s Kiro, but let me reiterate—this spec-driven AI IDE is a standout. It structures your dev process around requirements, letting you define projects in plain language or diagrams before coding starts. It automates docs, testing, and more, feeling like a technical PM guiding you from concept to production. Early users are hooked on its PRD mode, and it’s free during preview. Give it a spin—details on **X**.

**Wrapping Up: An Unforgettable AI Birthday Bash**

What a week, folks! From Kimi K2 redefining open-source power to OpenAI’s ChatGPT Agent ushering in a new era of task automation, this has been a whirlwind of innovation. Throw in Grok’s quirky waifus and our own W&B Inference launch, and I’m left speechless on my birthday. Sharing this with over 30,000 of you during our live stream was the ultimate gift—AI is moving at a pace I couldn’t have dreamed of when I started ThursdAI. Here’s to more breakthroughs, and I can’t wait to see what you build with Kimi K2 credits. Let’s keep pushing the boundaries together!

P.S - If you'd like to support this podcast/newsletter and give me a birthday present, the best way is to tell your friends about it and the second best way is to subscribe 👏 

TL;DR and Show Notes

Here’s everything we covered this week on ThursdAI for July 17, 2025, packed with links and key highlights for you to dive deeper:

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](https://x.com/@altryne))

* Co-Hosts - [@WolframRvnwlf](https://x.com/@WolframRvnwlf), [@yampeleg](https://x.com/@yampeleg), [@nisten](https://x.com/@nisten), [@ldjconfirmed](https://x.com/@ldjconfirmed)

* **Open Source LLMs**

* Moonshot launches Kimi K2 - a 1T param MoE crushing SWE Bench Verified at 65.8% ([X post](https://x.com/Kimi_Moonshot/status/1943687594560332025), [HuggingFace](https://huggingface.co/moonshotai), [API & docs](https://platform.moonshot.ai), [GitHub](https://github.com/MoonshotAI/Kimi-K2))

* Teknium drops Hermes 3 dataset - nearly 1M samples for training agentic models ([X](https://x.com/Teknium1/status/1945259797517099126))

* LGAI EXAONE-4.0 - hybrid attention, 32B & 1.2B models with 131K+ context ([X](https://x.com/Presidentlin/status/1944977367111291161), [HuggingFace](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-32B))

* **Big CO LLMs + APIs**

* OpenAI’s ChatGPT Agent - unified agentic AI for real-world tasks, scoring 41.6% on HLE ([Announcement](https://openai.com/index/introducing-chatgpt-agent/))

* Grok 4 waifus - XAI adds animated characters, topping Japan’s App Store

* Mira Murati’s Thinking Machines Lab - $2B funding for open AI science ([X](https://x.com/miramurati/status/1945166365834535247))

* Gemini Embedding Model - #1 on MTEB with 68.32 score ([X](https://x.com/OfficialLoganK/status/1944806630979461445), [Dev Blog](https://developers.googleblog.com/en/gemini-embedding-text-model-now-available-gemini-api/))

* Amazon S3 Vectors - preview for vector storage, up to 90% cost savings ([X](https://x.com/awscloud/status/1945271447619809504))

* **This Week’s Buzz**

* Kimi K2 on W&B Inference - open, scalable production access, $50 credits with “K2KoolAid” ([X](https://x.com/weights_biases/status/1945204732735447222), [Docs](https://weave-docs.wandb.ai/guides/integrations/inference/#advanced-example-use-weave-evaluations-and-leaderboards-with-the-inference-service))

* Wolfram’s Evaluation of W&B service ([X](https://x.com/altryne/status/1945586487627554938))

* **Vision & Video**

* Runway’s Act-Two - next-gen motion capture for head, face, body, hands ([X](https://x.com/runwayml/status/1945189222542880909), [YouTube](https://www.youtube.com/watch?v=JW8PHlFD7HM))

* **Voice & Audio**

* Mistral’s Voxtral - open SOTA speech recognition, beats Whisper v3 ([X](https://x.com/MistralAI/status/1945130173751288311), [HuggingFace](https://huggingface.co/mistralai))

* **AI Art & Diffusion & 3D**

* OpenAI image service API adds high-quality mode ([X](https://x.com/OpenAIDevs/status/1945538534884135132))

* **Tools**

* Liquid AI’s LEAP & Apollo - on-device AI for mobile, privacy-first ([X](https://x.com/LiquidAI_/status/1945105323846504821))

* Amazon’s Kiro - spec-driven AI IDE, free in preview ([X](https://x.com/ajassy/status/1944785963663966633)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-july-17th-kimi-k2-openai/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-july-17th-kimi-k2-openai?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2ODU4OTE0OCwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.dWTO7WMoMgQzYHlVdpUft7ybfteeXh8k_hjcDVVz97k&utm_campaign=CTA_5).

---

## 📆 ThursdAI - Jul 10 - Grok 4 and 4 Heavy, SmolLM3, Liquid LFM2, Reka Flash & Vision, Perplexity Comet Browser, Devstral 1.1 & More AI News

**Date:** July 11, 2025  
**Duration:** 1:49:46  
**Link:** [https://sub.thursdai.news/p/thursdai-jul-10-grok-4-and-4-heavy](https://sub.thursdai.news/p/thursdai-jul-10-grok-4-and-4-heavy)

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

---

## 📆 ThursdAI - Jul 3 - ERNIE 4.5, Hunyuan A13B, MAI-DxO outperforms doctors, RL beats SWE bench, Zuck MSL hiring spree & more AI news

**Date:** July 03, 2025  
**Duration:** 1:36:16  
**Link:** [https://sub.thursdai.news/p/thursdai-jul-3-ernie-45-hunyuan-a13b](https://sub.thursdai.news/p/thursdai-jul-3-ernie-45-hunyuan-a13b)

Hey everyone, Alex here 👋

Welcome back to another mind-blowing week on ThursdAI! We’re diving into the first show of the second half of 2025, and let me tell you, AI is not slowing down. This week, we’ve got a massive wave of open-source models from Chinese giants like Baidu and Tencent that are shaking up the game, Meta’s jaw-dropping hiring spree with Zuck assembling an AI dream team, and Microsoft’s medical AI outperforming doctors on the toughest cases. Plus, a real-time AI game engine that had me geeking out on stream. Buckle up, folks, because we’ve got a lot to unpack!

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

We had incredible guests like Michael Luo from Agentica, dropping knowledge on RL coding agents, and Ivan Burazin from Daytona, revealing the infrastructure powering the agent era. We had an incredible episode this week, with over 8,000 views for the live show (as always, Links and Show notes in the end, and the YT live video is here for your convienience if you'd prefer watching) 

Open Source AI & LLMs: The Chinese Powerhouse Wave

Man, if there’s one takeaway from this week, it’s that Chinese companies are absolutely dominating the open-source LLM scene. Let’s break down the heavy hitters that dropped this week and why they’ve got everyone talking.

Baidu’s ERNIE 4.5: A Suite of 10 Models to Rule Them All

Baidu, a giant in the Chinese tech space, just flipped the script by open-sourcing their ERNIE 4.5 series. We’re talking 10 distinct models ranging from a whopping 424 billion parameters down to a tiny 0.3 billion. With an Apache 2.0 license, 128K context window, and multimodal capabilities handling image, video, and text input, this is a massive drop. Their biggest Mixture-of-Experts (MoE) model, with 47B active parameters, even outshines OpenAI’s o1 on visual knowledge tasks like DocVQA, scoring 93% compared to o1’s 81%! 

What’s wild to me is Baidu’s shift. They’ve been running ERNIE in production for years—think chatbots and more across their ecosystem—but they weren’t always open-source fans. Now, they’re not just joining the party, they’re hosting it. If you’re into tinkering, this is your playground—check it out on Hugging Face ([HF](https://huggingface.co/baidu)) or dive into their technical paper ([Paper](https://ernie.baidu.com/blog/publication/ERNIE_Technical_Report.pdf)).

Tencent’s Hunyuan-A13B-Instruct: WizardLM Team Strikes Again

Next up, Tencent dropped Hunyuan-A13B-Instruct, and oh boy, does it have a backstory. This 80B parameter MoE model (13B active at inference) comes from the legendary WizardLM team, poached from Microsoft after a messy saga where their killer models got yanked from the internet over “safety concerns.” I remember the frustration—we were all hyped, then bam, gone. Now, under Tencent’s wing, they’ve cooked up a model with a 256K context window, hybrid fast-and-slow reasoning modes, and benchmarks that rival DeepSeek R1 and OpenAI o1 on agentic tasks. It scores an impressive 87% on AIME 2024, though it dips to 76% on 2025, hinting at some overfitting quirks. Though for a 12B active parameters model this all is still VERY impressive.

Here’s the catch—the license. It excludes commercial use in the EU, UK, and South Korea, and bans usage if you’ve got over 100M active users. So, not as open as we’d like, but for its size, it’s a beast that fits on a single machine, making it a practical choice for many. They’ve also released two datasets, ArtifactsBench and C3-Bench, for code and agent evaluation. I’m not sold on the name—Hunyuan doesn’t roll off the tongue for Western markets—but the WizardLM pedigree means it’s worth a look. Try it out on Hugging Face ([HF](https://huggingface.co/tencent/Hunyuan-A13B-Instruct)) or test it directly ([Try It](https://hunyuan.tencent.com/)).

Huawei’s Pangu Pro MoE: Sidestepping Sanctions with Ascend NPUs

Huawei entered the fray with Pangu Pro MoE, a 72B parameter model with 16B active per token, and here’s what got me hyped—it’s trained entirely on their own Ascend NPUs, not Nvidia or AMD hardware. This is a bold move to bypass US sanctions, using 4,000 of these chips to preprocess 13 trillion tokens. The result? Up to 1,528 tokens per second per card with speculative decoding, outpacing dense models in speed and cost-efficiency. Performance-wise, it’s close to DeepSeek and Qwen, making it a contender for those outside the Nvidia ecosystem.

I’m intrigued by the geopolitical angle here. Huawei’s proving you don’t need Western tech to build frontier models, and while we don’t know who’s got access to these Ascend NPUs, it’s likely a game-changer for Chinese firms. Licensing isn’t as permissive as MIT or Apache, but it’s still open-weight. Peek at it on Hugging Face ([HF](https://huggingface.co/IntervitensInc/pangu-pro-moe-model)) for more details.

DeepSWE-Preview: RL Coding Agent Hits 59% on SWE-Bench

Switching gears, I was blown away chatting with Michael Luo from Agentica about DeepSWE-Preview, an open-source coding agent trained with reinforcement learning (RL) on Qwen3-32B. This thing scored a stellar 59% on SWE-Bench-Verified (42.2% Pass@1, 71% Pass@16), one of the top open-weight results out there. What’s cool is they did this without distilling from proprietary giants like Claude—just pure RL over six days on 64 H100 GPUs. Michael shared how RL is surging because pre-training hits data limits, and DeepSWE learned emergent behaviors like paranoia, double-checking edge cases to avoid shaky fixes.

This underdog story of academic researchers breaking benchmarks with limited resources is inspiring. They’ve open-sourced everything—code, data, logs—making it a goldmine for the community. I’m rooting for them to get more compute to push past even higher scores. Dive into the details on their blog ([Notion](https://pretty-radio-b75.notion.site/DeepSWE-Training-a-Fully-Open-sourced-State-of-the-Art-Coding-Agent-by-Scaling-RL-22281902c1468193aabbe9a8c59bbe33)) or check the model on Hugging Face ([HF Model](https://huggingface.co/Agentica/DeepSWE-Preview)).

This Week’s Buzz from Weights & Biases: come Hack with Us! 🔥

As always, I’ve got some exciting news from Weights & Biases to share. We’re hosting the first of our Weavehacks hackathons in San Francisco on July 12-13. It’s all about agent protocols like MCP and A2A, and I’m stoked to you guys in person—come say hi for a high-five! We’ve got cool prizes, including a custom W&B RoboDog that’s been a conference hit, plus $13-14K in cash. Spots are filling fast, so register now and we'll let you in ([Sign Up](http://lu.ma/weavehacks)).

We’re also rolling out Online Evaluations in Weave, letting you monitor LLM apps live with judge agents on production data—super handy for catching hiccups. And our inference service via CoreWeave GPUs offers free credits for open-source model testing. Want in or curious about Weave’s tracing tools? Reach out to me anywhere, and I’ll hook you up. Can’t wait to demo this next week!

Big Companies & APIs: AI’s NBA Draft and Medical Marvels

Shifting to the big players, this week felt like an AI sports season with blockbuster hires and game-changing releases. From Meta’s talent poaching to Microsoft’s medical breakthroughs, let’s unpack the drama and innovation.

Meta Superintelligence Labs: Zuck’s Dream Team Draft 

Imagine an AI NBA draft—that’s what Meta’s up to with their new Superintelligence Labs (MSL). Led by Alex Wang (formerly of Scale AI) and Nat Friedman (ex-GitHub CEO), MSL is Zuck’s power move after Llama 4’s lukewarm reception. They’ve poached up to 10 key researchers from OpenAI, including folks behind GPT-4’s image generation and o1’s foundations, with comp packages rumored at $100M for the first year and up to $300M over four years. That’s more than many Meta execs or even Tim Cook’s salary! They’ve also snagged talent from Google DeepMind and even tried to acquire Ilya Sutskever’s SSI outright (to which he said he's flattered but no) 

This is brute force at its finest, and I’m joking that I didn’t get a $100M offer myself—ThursdAI’s still waiting for that email, Zuck! OpenAI’s Sam Altman fired back with “missionaries beat mercenaries,” hinting at a culture clash, while Mark Chen felt like Meta “broke into their house and took something” It’s war, folks, and I’m hyped to see if MSL delivers a Llama that crushes it. With FAIR and GenAI folding under this new crack team of 50, plus Meta’s GPU arsenal, the stakes are sky-high.

If you're like to see the list of "mercenaries" worth over 100M, you can see who they are and their achievements [here](https://docs.google.com/spreadsheets/d/1qX7_VK8vN2v2urpiBY_we-FNz2PS3ZKsWp_9kXCyQB0/edit?usp=sharing)

Cursor’s Killer Hires and Web Expansion

Speaking of talent wars, Cursor (built by AnySphere) just pulled off a stunner by hiring Boris Cherny and Cat Wu, key creators of Claude Code, as Chief Architect and Head of Product. This skyrockets Cursor’s cred in code generation, and I’m not surprised—Claude Code was a side project that exploded, and now Cursor’s got the brains behind it. On top of that, they’ve rolled out AI coding agents to web and mobile, even integrating with Slack. No more being tied to your desktop—launch, monitor, and collab on code tasks anywhere.

The lines between native and web tools are blurring fast, and Cursor’s leading the charge. I haven’t tested the Slack bit yet, but if you have, hit me up in the comments. This, plus their recent $20M raise, shows they’re playing to win. Learn more at ([Cursor](https://cursor.com/agents)).

Microsoft MAI-DxO: AI Diagnoses Better Than Doctors

Now, onto something that hits close to home for me—Microsoft’s MAI-DxO, an AI system that’s outdiagnosing doctors on open-ended medical cases. On 304 of the toughest New England Journal of Medicine cases, it scored 85.5% accuracy, over four times the 20% rate of experienced physicians. I’ve had my share of frustrating medical waits, and seeing AI step in as a tool for doctors—not a replacement—gets me excited for the future.

It’s an orchestration of models simulating a virtual clinician panel, asking follow-up questions, ordering tests, and even factoring in cost controls for diagnostics. This isn’t just acing multiple-choice; it handles real-world ambiguity. My co-host Yam and I stressed—don’t skip your doctor for ChatGPT, but expect your doc to be AI-superpowered soon. Read more on Microsoft’s blog ([Blog](https://microsoft.ai/new/the-path-to-medical-superintelligence/)).

ThursdAI - Recaps of the most high signal AI weekly spaces is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Cloudflare’s One-Click AI Bot Block: Protecting the Internet

Cloudflare made waves with a one-click feature to block AI bots and scrapers, available to all customers, even free-tier ones. With bots like Bytespider and GPTBot hitting nearly 40% of top sites, but only 3% blocking them, this addresses a huge shift. I’m with the CEO here—the old internet deal was Google scraping for traffic; now, AI summaries keep users from clicking through, breaking monetization for creators. Yam suggested a global license for training data with royalties, and I’m curious if that’s the future. For now, Cloudflare’s ML detects even sneaky bots spoofing as browsers. Big move—check their announcement ([X](https://x.com/Cloudflare/status/1939988601976021156)) and the cool website [goodaibots.com](http://goodaibots.com) 

Cypher Alpha: Mystery 1M Context Model on OpenRouter

Lastly, a mysterious 1M context model, Cypher Alpha, popped up on OpenRouter for free testing (with data logging). It’s fast at 70 tokens/sec, low latency, but not a reasoning model—refusals on basic queries stumped me. Speculation points to Amazon Titan, which would be a surprise entry. I’m intrigued by who’s behind this—Gemini, OpenAI, and Qwen hit 1M context, but Amazon? Let’s see. Try it yourself ([Link](https://openrouter.ai/openrouter/cypher-alpha:free/providers)).

Vision & Video: Mirage’s AI-Native Game Engine Blows Minds 🤯

Okay, folks, I’ve gotta geek out here.  Dynamics Lab unveiled the world’s first AI-native user-generated content (UGC) game engine, live with playable demos like a GTA-style “Urban Chaos” and a racing “Coastal Drift.” Running at 16 frames per second, it generates photorealistic worlds in real-time via natural language or controller input. You can jump, run, fight, or drive, and even upload an image to spawn a new game environment on the fly.

What’s nuts is there’s no pre-built game behind this—it’s infinite, custom content created as you play. I was floored showing this on stream; it’s obviously not perfect with clipping and delays, but we’re witnessing the dawn of personalized gaming. You gotta try this—head to their site for the demos ([Playable Demo](https://blog.dynamicslab.ai/)).

This brings us even more closer to the "every pixel will be generated" dream of Jensen Huang.

Voice & Audio: TTS Gets Real with Kyutai and Qwen

This week brought fresh text-to-speech (TTS) updates that hint at smarter conversational AI down the line. Kyutai TTS, from the French team behind Moshi, dropped with ultra-low latency (220ms first-token) and high speaker similarity (77.1% English, 78.7% French), plus a word error rate of just 2.82% in English. It’s production-ready with a Rust server and voice cloning from a 10-second clip—perfect for LLM-integrated apps. Check it out ([X Announcement](https://x.com/kyutai_labs/status/1940767331921416302), [HF Model](https://huggingface.co/kyutai/tts-1.6b-en_fr)).

Qwen-TTS from Alibaba also launched, focusing on Chinese dialects like Pekingese and Shanghainese, but with English support too. It’s got human-level naturalness via API, though less relevant for our English audience. Still, it’s a solid step—see more ([X Post](https://x.com/Alibaba_Qwen/status/1939553252166836457)). Both are pieces of the puzzle for richer virtual interactions, and I’m pumped to see where this goes.

Infrastructure for Agents: Daytona’s Sandbox Revolution

I’m thrilled to have chatted with Ivan Burazin from Daytona, a cloud provider delivering agent-native runtimes—or sandboxes—that give agents their own computers for tasks like code execution or data analysis. They’ve hit over $1M in annualized run rate just two months post-launch, with 15,000 signups and 1,500 credit cards on file. That’s insane growth for infrastructure, which usually ramps slowly due to integration delays.

Why’s this hot? 2025 is the year of agents, and as Ivan shared, even OpenAI and Anthropic recently redefined agents as needing runtimes. From YC’s latest batch (37% building agents) to Cursor’s web move, every task may soon spin up a sandbox. Daytona’s “stateful serverless” tech spins fast, lasts long, and scales across regions like the US, UK, Germany, and India, addressing latency and GDPR needs. If you’re building agents, this is your unsung hero—explore it at ([Daytona IO](https://github.com/DaytonaIO)) and grab $200 in credits, or up to $50K for startups ([Startups](https://daytona.io/startups)).

Wrapping Up: AI’s Relentless Pace

What a week, folks! From Chinese open-source titans like ERNIE 4.5 and Hunyuan-A13B redefining accessibility, to Meta’s blockbuster hires signaling an AI arms race, and Microsoft’s MAI-DxO paving the way for smarter healthcare, we’re witnessing AI’s relentless acceleration. Mirage’s game engine and Daytona’s sandboxes remind us that creativity and infrastructure are just as critical as models themselves. I’m buzzing with anticipation for what’s next—will Meta’s dream team deliver? Will agents redefine every app? Stick with ThursdAI to find out. See you next week for more!

TL;DR and Show Notes

Here’s the quick rundown of everything we covered this week, packed with links to dive deeper:

* **Show Notes & Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* **Co-Hosts** - [@WolframRvnwlf](http://x.com/@WolframRvnwlf), [@yampeleg](http://x.com/@yampeleg), [@nisten](http://x.com/@nisten), [@ldjconfirmed](http://x.com/@ldjconfirmed)

* **Guests** - Ivan Burazin (Daytona), Michael Luo (Agentica)

* **Open Source LLMs**

* Baidu’s ERNIE 4.5 Series - 10 models, 424B to 0.3B, multimodal, beats o1 on DocVQA ([X](https://x.com/Baidu_Inc/status/1939724778157511126), [HF](https://huggingface.co/baidu), [Paper](https://ernie.baidu.com/blog/publication/ERNIE_Technical_Report.pdf))

* Tencent’s Hunyuan-A13B-Instruct - 80B total, 13B active, 256K context, WizardLM legacy ([X](https://x.com/TencentHunyuan/status/1938525874904801490), [HF](https://huggingface.co/tencent/Hunyuan-A13B-Instruct), [Try It](https://hunyuan.tencent.com/))

* Huawei’s Pangu Pro MoE - 72B, trained on Ascend NPUs, 1,528 tokens/sec ([X](https://x.com/search?q=pangu%20pro&src=typed_query), [HF](https://huggingface.co/IntervitensInc/pangu-pro-moe-model))

* DeepSWE-Preview - RL agent, 59% SWE-Bench-Verified on Qwen3-32B ([Notion](https://pretty-radio-b75.notion.site/DeepSWE-Training-a-Fully-Open-sourced-State-of-the-Art-Coding-Agent-by-Scaling-RL-22281902c1468193aabbe9a8c59bbe33), [HF Model](https://huggingface.co/Agentica/DeepSWE-Preview))

* **This Week’s Buzz**

* Weights & Biases Weavehacks Hackathon - SF, July 12-13, agent protocols focus ([Sign Up](http://lu.ma/weavehacks))

* **Big CO LLMs + APIs**

* Meta Superintelligence Labs (MSL) - Zuck hires dream team, up to $300M comp packages from OpenAI talent ([list](https://docs.google.com/spreadsheets/d/1qX7_VK8vN2v2urpiBY_we-FNz2PS3ZKsWp_9kXCyQB0/edit?usp=sharing))

* Cursor - Hires Claude Code creators, web/mobile agents with Slack ([Cursor](https://cursor.com/agents), [HF](https://huggingface.co/spaces/cursor))

* Microsoft MAI-DxO - 85.5% accuracy on NEJM cases vs. 20% for doctors ([X](https://x.com/mustafasuleyman/status/1939670330332868696), [Blog](https://microsoft.ai/new/the-path-to-medical-superintelligence/))

* Cloudflare - One-click AI bot blocking, tackles scraping economics ([X](https://x.com/Cloudflare/status/1939988601976021156))

* Cypher Alpha - Mystery 1M context model, possibly Amazon Titan ([Link](https://openrouter.ai/openrouter/cypher-alpha:free/providers))

* Gemini Pro 2.5 - Returned to Google’s free tier

* **Vision & Video**

* Mirage - AI-native UGC game engine, real-time photorealistic demos ([Playable Demo](https://blog.dynamicslab.ai/))

* Workflow - Restyle videos with Flux Kontext and Luma Modify ([X](https://x.com/lucataco93/status/1940113275221344566))

* **Voice & Audio**

* Kyutai TTS - Low-latency, high similarity in EN/FR ([X](https://x.com/kyutai_labs/status/1940767331921416302), [HF](https://huggingface.co/kyutai/tts-1.6b-en_fr))

* Qwen-TTS - Bilingual Chinese/English, human-level naturalness ([X](https://x.com/Alibaba_Qwen/status/1939553252166836457), [HF](https://huggingface.co/spaces/Qwen/Qwen-TTS))

* **Infrastructure**

* Daytona - Agent-native sandboxes, $1M run rate in 2 months ([GitHub](https://github.com/DaytonaIO), [Startups](https://daytona.io/startups))

* **Tools**

* Chai Discovery’s Chai-2 - Zero-shot antibody design ([Chai Discovery](https://www.chaidiscovery.com/news/introducing-chai-2))

Thanks for reading all the way through ThursdAI, folks! Share this with friends to spread the AI love, and I’ll catch you next week for more! 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jul-3-ernie-45-hunyuan-a13b/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jul-3-ernie-45-hunyuan-a13b?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2NzQ3MjkwMywiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.NnlYvILRLy9k6gBd2kYURO8Vw7HkP9u15R-Gvp_FA6U&utm_campaign=CTA_5).

---

