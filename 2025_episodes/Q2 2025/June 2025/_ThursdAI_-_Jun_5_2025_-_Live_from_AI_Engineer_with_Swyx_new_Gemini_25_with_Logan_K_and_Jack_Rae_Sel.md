# 📆 ThursdAI - Jun 5, 2025 - Live from AI Engineer with Swyx, new Gemini 2.5 with Logan K and Jack Rae, Self Replicating agents with Morph Labs

**Date:** June 06, 2025  
**Duration:** 1:43:45  
**Link:** [https://sub.thursdai.news/p/thursdai-jun-5-2025-live-from-ai](https://sub.thursdai.news/p/thursdai-jun-5-2025-live-from-ai)

---

## Description

Hey folks, this is Alex, coming to you LIVE from the AI Engineer Worlds Fair! 

What an incredible episode this week, we recorded live from floor 30th at the Marriott in SF, while Yam was doing live correspondence from the floor of the AI Engineer event, all while Swyx, the cohost of Latent Space podcast, and the creator of AI Engineer (both the conference and the concept itself) joined us for the whole stream - here’s the edited version, please take a look.  

We've had around 6500 people tune in, and at some point we got 2 surprise guests, straight from the keynote stage, Logan Kilpatrick (PM for AI Studio and lead cheerleader for Gemini) and Jack Rae (principal scientist working on reasoning) joined us for a great chat about Gemini! Mind was absolutely blown! 

They have just launched the new Gemini 2.5 Pro and I though it would only be fitting to let their new model cover this podcast this week (so below is **fully AI generated** ... non slop I hope). The show notes and TL;DR is as always in the end. 

Okay, enough preamble… let's dive into the madness!

**🤯 Google Day at AI Engineer: New Gemini 2.5 Pro and a Look Inside the Machine's Mind**

For the first year of this podcast, a recurring theme was us asking, "Where's Google?" Well, it's safe to say that question has been answered with a firehose of innovation. We were lucky enough to be joined by Google DeepMind's Logan Kilpatrick and Jack Rae, the tech lead for "thinking" within Gemini, literally moments after they left the main stage.

**Surprise! A New Gemini 2.5 Pro Drops Live**

Logan kicked things off with a bang, officially announcing a brand new, updated Gemini 2.5 Pro model right there during his keynote. He called it "hopefully the final update to 2.5 Pro," and it comes with a bunch of performance increases, closing the gap on feedback from previous versions and hitting SOTA on benchmarks like Aider.

It's clear that the organizational shift to bring the research and product teams together under the DeepMind umbrella is paying massive dividends. Logan pointed out that Google has seen a 50x increase in AI inference over the past year. The flywheel is spinning, and it's spinning *fast*.

**How Gemini "Thinks"**

Then things got even more interesting. Jack Rae gave us an incredible deep dive into what "thinking" actually means for a language model. This was one of the most insightful parts of the conference for me.

For years, the bottleneck for LLMs has been **test-time compute**. Models were trained to respond immediately, applying a fixed amount of computation to go from a prompt to an answer, no matter how hard the question. The only way to get a "smarter" response was to use a bigger model.

Jack explained that "Thinking" shatters this limitation. Mechanically, Gemini now has a "thinking stage" where it can generate its own internal text—hypothesizing, testing, correcting, and reasoning—before committing to a final answer. It's an iterative loop of computation that the model can dynamically control, using more compute for harder problems. It learns *how* to think using reinforcement learning, getting a simple "correct" or "incorrect" signal and backpropagating that to shape its reasoning strategies.

We're already seeing the results of this. Jack showed a clear trend: as models get better at reasoning, they're also using more test-time compute. This paradigm also gives developers a "thinking budget" slider in the API for Gemini 2.5 Flash and Pro, allowing a continuous trade-off between cost and performance.

The future of this is even wilder. They're working on **DeepThink**, a high-budget mode for extremely hard problems that uses much deeper, parallel chains of thought. On the tough USA Math Olympiad, where the SOTA was negligible in January, 2.5 Pro reached the 50th percentile of human participants. DeepThink pushes that to the 65th percentile.

Jack’s ultimate vision is inspired by the mathematician Ramanujan, who derived incredible theorems from a single textbook by just thinking deeply. The goal is for models to do the same—contemplate a small set of knowledge so deeply that they can push the frontiers of human understanding. Absolutely mind-bending stuff.

**🤖 MorphLabs and the Audacious Quest for Verified Superintelligence**

Just when I thought my mind couldn't be bent any further, we were joined by Jesse Han, the founder and CEO of MorphLabs. Fresh off his keynote, he laid out one of the most ambitious visions I've heard: building the infrastructure for the Singularity and developing "verified superintelligence."

The big news was that **Christian Szegedy** is joining MorphLabs as Chief Scientist. For those who don't know, Christian is a legend—he invented batch norm and adversarial examples, co-founded XAI, and led code reasoning for Grok. That's a serious hire.

Jesse’s talk was framed around a fascinating question: "What does it mean to have empathy for the machine?" He argues that as AI develops personhood, we need to think about what it wants. And what it wants, according to Morph, is a new kind of cloud infrastructure.

This is **MorphCloud**, built on a new virtualization stack called **Infinibranch**. Here’s the key unlock: it allows agents to instantaneously snapshot, branch, and replicate their entire VM state. Imagine an agent reaching a decision point. Instead of choosing one path, it can branch its entire existence—all its processes, memory, and state—to explore every option in parallel. It can create save states, roll back to previous checkpoints, and even merge its work back together.

This is a monumental step for agentic AI. It moves beyond agents that are just a series of API calls to agents that are truly embodied in complex software environments. It unlocks the potential for recursive self-improvement and large-scale reinforcement learning in a way that's currently impossible. It’s a bold, sci-fi vision, but they're building the infrastructure to make it a reality today.

**🔥 The Agent Conversation: OpenAI, MCP, and Magic Moments**

The undeniable buzz on the conference floor was all about **agents**. You couldn't walk ten feet without hearing someone talking about agents, tools, and MCP.

OpenAI is leaning in here too. This week, they made their **Codex coding agent available to all ChatGPT Plus users** and announced that ChatGPT will soon be able to listen in on your Zoom meetings. This is all part of a broader push to make AI more active and integrated into our workflows.

The **MCP (Model-Context-Protocol)** track at the conference was packed, with lines going down the hall. (Alex here, I had a blast talking during that track about MCP observability, you can catch our talk [here](https://youtu.be/z4zXicOAF28?t=19573) on the live stream of AI Engineer) 

Logan Kilpatrick offered a grounded perspective, suggesting the hype might be a bit overblown but acknowledging the critical need for an open standard for tool use, a void left when OpenAI didn't formalize ChatML.

I have to share my own jaw-dropping MCP moment from this week. I was coding an agent using an IDE that supports MCP. My agent, which was trying to debug itself, used an MCP tool to check its own observability traces on the Weights & Biases platform. While doing so, it discovered a *new tool* that our team had just added to the MCP server—a support bot. Without any prompting from me, my coding agent formulated a question, "chatted" with the support agent to get the answer, came back, fixed its own code, and then re-checked its work. Agent-to-agent communication, happening automatically to solve a problem. My jaw was on the floor. That's the magic of open standards.

**This Week's Buzz from Weights & Biases**

Speaking of verification and agents, the buzz from our side is all about it! At our booth here at AI Engineer, we have a Robodog running around, connected to our LLM evaluation platform, **W&B Weave**. As Jesse from MorphLabs discussed, verifying what these complex agentic systems are doing is critical. Whether it's superintelligence or your production application, you need to be able to evaluate, trace, and understand its behavior. We're building the tools to do just that.

And if you're in San Francisco, don't forget our own conference, **Fully Connected**, is happening on June 18th and 19th! It's going to be another amazing gathering of builders and researchers. [Fullyconnected.com](http://Fullyconnected.com)  get in FREE with the promo code  **WBTHURSAI**

What a show. The energy, the announcements, the sheer brainpower in one place was something to behold. We’re at a point where the conversation has shifted from theory to practice, from hype to real, tangible engineering. The tracks on agents and enterprise adoption were overflowing because people are building, right now. It was an honor and a privilege to bring this special episode to you all.

Thank you for tuning in. We'll be back to our regular programming next week! (and Alex will be back to writing his own newsletter, not send direct AI output!)

AI News TL;DR and show notes

* **Hosts and Guests**

* **Alex Volkov** - AI Evangelist & Weights & Biases ([@altryne](http://x.com/@altryne))

* Co Hosts - [@swyx](http://x.com/swyx) [@yampeleg](x.com/@yampeleg) [@romechenko](https://twitter.com/romechenko/status/1891007363827593372) 

* Guests - [@officialLoganK](https://x.com/OfficialLoganK), [@jack_w_rae](https://x.com/jack_w_rae)

* **Open Source LLMs** 

* ByteDance / ContentV-8B - ([HF](https://huggingface.co/ByteDance/ContentV-8B))

* **Big CO LLMs + APIs**

* Gemini Pro 2.5 updated Jun 5th ([X](https://x.com/OfficialLoganK/status/1930657743251349854))

* SOTA on HLE, Aider, and GPQA

* Now supports thinking budgets

* Same cost, on pareto frontier

* Closes gap on 03-25 regressions

* OAI AVM injects ads and stopped singing ([X](https://x.com/altryne/status/1929312886448337248))

* OpenAI Codex is now available to plus members and has internet access ([X](https://github.com/aavetis/ai-pr-watcher/))

* ~24,000 NEW PRs overnight from Codex after @OpenAI expands access to free users.

* OpenAI will record meetings and released connectors like  ([X](https://twitter.com/testingcatalog/status/1930366893321523676))

* [TestingCatalog News 🗞@testingcatalog](https://twitter.com/testingcatalog)[Jun 4, 2025](https://twitter.com/testingcatalog/status/1930366893321523676)

OpenAI released loads of connectors for Team accounts! Most of these connectors can be used for Deep Research, while Google Drive, SharePoint, Dropbox and Box could be used in all chats. https://t.co/oBEmYGKguE

* Anthropic cuts windsurf access for Windsurf ([X](https://x.com/kevinhou22/status/1930401320210706802))

* Without warning, Anthropic cuts off Windsurf from official Claude 3 and 4 APIs

* This weeks Buzz

* FULLY - CONNECTED - Fully Connected: W&B's 2-day conference, June 18-19 in SF [fullyconnected.com](fullyconnected.com) - Promo Code WBTHURSAI

* **Vision & Video**

* VEO3 is now available via API on FAL ([X](https://x.com/FAL/status/1930732632046006718))

* Captions launches Mirage Studio - talking avatars competition to HeyGen/Hedra ([X](https://x.com/getcaptionsapp/status/1929554635544461727))

* **Voice & Audio**

* ElevenLabs model V3 - supports emotion tags and is "inflection point" ([X](https://x.com/venturetwins/status/1930727253815759010)) 

* Supporting 70+ languages, multi-speaker dialogue, and audio tags such as [excited], [sighs], [laughing], and [whispers].

* **Tools**

* Cursor Launched V1 - Bug Bot reviews PRs, iPython notebooks and one clickMCP

* 24,000 NEW PRs overnight from Codex after [@OpenAI](https://x.com/OpenAI) expands access to plus users ([X](https://twitter.com/albfresco/status/1930262263199326256)) 

Thank you for subscribing. [Leave a comment](https://sub.thursdai.news/p/thursdai-jun-5-2025-live-from-ai/comments?utm_medium=podcast&utm_campaign=CTA_5) or [share this episode](https://sub.thursdai.news/p/thursdai-jun-5-2025-live-from-ai?utm_source=substack&utm_medium=podcast&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNTIyMTYxMTAsInBvc3RfaWQiOjE2NTMxNTQyMSwiaWF0IjoxNzY1MjQyMjg2LCJleHAiOjE3Njc4MzQyODYsImlzcyI6InB1Yi0xODAxMjI4Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.fuAhXQicTRZhUI4Srm9PVft19TKEtzMdHkvtE0mkFUc&utm_campaign=CTA_5).
