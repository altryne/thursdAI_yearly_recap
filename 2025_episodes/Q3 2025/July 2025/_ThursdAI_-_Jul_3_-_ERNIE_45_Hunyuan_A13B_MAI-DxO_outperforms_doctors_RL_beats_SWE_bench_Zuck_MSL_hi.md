# 📆 ThursdAI - Jul 3 - ERNIE 4.5, Hunyuan A13B, MAI-DxO outperforms doctors, RL beats SWE bench, Zuck MSL hiring spree & more AI news

**Date:** July 03, 2025  
**Duration:** 1:36:16  
**Link:** [https://sub.thursdai.news/p/thursdai-jul-3-ernie-45-hunyuan-a13b](https://sub.thursdai.news/p/thursdai-jul-3-ernie-45-hunyuan-a13b)

---

## Description

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
