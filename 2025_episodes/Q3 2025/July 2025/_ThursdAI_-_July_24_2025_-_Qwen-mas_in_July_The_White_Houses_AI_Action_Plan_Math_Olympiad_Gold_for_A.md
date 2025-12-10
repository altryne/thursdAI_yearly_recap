# 📆 ThursdAI - July 24, 2025 - Qwen-mas in July, The White House's AI Action Plan & Math Olympiad Gold for AIs + coding a 3d tetris on stream

**Date:** July 24, 2025  
**Duration:** 1:43:23  
**Link:** [https://sub.thursdai.news/p/thursdai-july-24-2025-qwen-mas-in](https://sub.thursdai.news/p/thursdai-july-24-2025-qwen-mas-in)

---

## Description

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
