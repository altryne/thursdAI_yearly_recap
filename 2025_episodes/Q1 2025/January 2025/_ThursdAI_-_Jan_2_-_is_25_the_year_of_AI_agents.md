# 📆 ThursdAI - Jan 2 - is 25' the year of AI agents?

**Date:** January 02, 2025  
**Duration:** 1:31:29  
**Link:** [https://sub.thursdai.news/p/thursdai-jan-2-is-25-the-year-of](https://sub.thursdai.news/p/thursdai-jan-2-is-25-the-year-of)

---

## Description

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
