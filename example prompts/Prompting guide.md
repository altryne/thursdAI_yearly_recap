Title: Nano-Banana Pro: Prompting Guide & Strategies

URL Source: http://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n

Published Time: 2025-11-27T18:04:07Z

Markdown Content:
**Nano-Banana Pro** is a significant leap forward from previous generation models, moving from "fun" image generation to "functional" professional asset production. It excels in **text rendering, character consistency, visual synthesis, world knowledge (Search), and high-resolution (4K) output.**

Following the [developer guide](https://dev.to/googleai/introducing-nano-banana-pro-complete-developer-tutorial-5fc8) on how to get started with [AI Studio](https://ai.studio/) and the API, this guide covers the core capabilities and how to prompt them effectively.

* * *

Here's what you'll find in this article:

*   0. The Golden Rules of Prompting
*   1. Text Rendering, Infographics & Visual Synthesis
*   2. Character Consistency & Viral Thumbnails
*   3. Grounding with Google Search
*   4. Advanced Editing, Restoration & Colorization
*   5. Dimensional Translation (2D ↔ 3D)
*   6. High-Resolution & Textures
*   7. Thinking & Reasoning
*   8. One-Shot Storyboarding & Concept Art
*   9. Structural Control & Layout Guidance
*   10. What's Next?

* * *

[](http://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n#section-0-the-golden-rules-of-prompting) 🛑 Section 0: The Golden Rules of Prompting
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Nano-Banana Pro is a "Thinking" model. It doesn't just match keywords; it understands intent, physics, and composition. To get the best results, stop using "tag soups" (e.g., `dog, park, 4k, realistic`) and start acting like a Creative Director.

**1. Edit, Don't Re-roll**

 The model is exceptionally good at understanding conversational edits. If an image is 80% correct, do not generate a new one from scratch. Instead, simply ask for the specific change you need.

*   _Example:_ "That's great, but change the lighting to sunset and make the text neon blue."

**2. Use Natural Language & Full Sentences**

 Talk to the model as if you were briefing a human artist. Use proper grammar and descriptive adjectives.

*    ❌ **Bad:** "Cool car, neon, city, night, 8k."
*    ✅ **Good:** "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. The neon signs reflect off the wet pavement and the car's metallic chassis."

**3. Be Specific and Descriptive**

 Vague prompts yield generic results. Define the subject, the setting, the lighting, and the mood.

*   **Subject:** Instead of "a woman," say "a sophisticated elderly woman wearing a vintage chanel-style suit."
*   **Materiality:** Describe textures. "Matte finish," "brushed steel," "soft velvet," "crumpled paper."

**4. Provide Context (The "Why" or "For whom")**

 Because the model "thinks," giving it context helps it make logical artistic decisions.

*   _Example:_ "Create an image of a sandwich **for a Brazilian high-end gourmet cookbook**." (The model will infer professional plating, shallow depth of field, and perfect lighting).

* * *

[](http://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n#1-text-rendering-infographics-amp-visual-synthesis) 1. Text Rendering, Infographics & Visual Synthesis
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Nano-Banana Pro has SOTA capabilities for rendering legible, stylized text and synthesizing complex information into visual formats.

**Best Practices:**

*   **Compression:** Ask the model to "compress" dense text or PDFs into visual aids.
*   **Style:** Specify if you want a "polished editorial," a "technical diagram," or a "hand-drawn whiteboard" look.
*   **Quotes:** Clearly specify the text you want in quotes.

**Example Prompts:**

> **Earnings Report Infographic (Data Ingestion):**
> 
>  [Input PDF of Google's latest [earnings report](https://s206.q4cdn.com/479360582/files/doc_news/2025/Oct/29/attachments/2025q3-alphabet-earnings-release.pdf)]
> 
>  "Generate a clean, modern infographic summarizing the key financial highlights from this earnings report. Include charts for 'Revenue Growth' and 'Net Income', and highlight the CEO's key quote in a stylized pull-quote box."

[![Image 1: Earnings Report Infographic](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fe4pg6n5f3udltijhcm77.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fe4pg6n5f3udltijhcm77.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Generate%20a%20clean%2C%20modern%20infographic%20summarizing%20the%20key%20financial%20highlights%20from%20this%20earnings%20report.%20Include%20charts%20for%20%27Revenue%20Growth%27%20and%20%27Net%20Income%27%2C%20and%20highlight%20the%20CEO%27s%20key%20quote%20in%20a%20stylized%20pull-quote%20box.&model=gemini-3-pro-image-preview)_(Note: Requires uploading a PDF)_

> **Retro Infographic:**
> 
>  "Make a retro, 1950s-style infographic about the history of the American diner. Include distinct sections for 'The Food,' 'The Jukebox,' and 'The Decor.' Ensure all text is legible and stylized to match the period."

[![Image 2: Retro Infographic](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyo8vewspjc6lrro025z5.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyo8vewspjc6lrro025z5.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Make%20a%20retro%2C%201950s-style%20infographic%20about%20the%20history%20of%20the%20American%20diner.%20Include%20distinct%20sections%20for%20%27The%20Food%2C%27%20%27The%20Jukebox%2C%27%20and%20%27The%20Decor.%27%20Ensure%20all%20text%20is%20legible%20and%20stylized%20to%20match%20the%20period.&model=gemini-3-pro-image-preview)

> **Technical Diagram:**
> 
>  "Create an orthographic blueprint that describes this building in plan, elevation, and section. Label the 'North Elevation' and 'Main Entrance' clearly in technical architectural font. Format 16:9."

[![Image 3: Technical Diagram](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffk7q8vqyctplwufbwdsj.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffk7q8vqyctplwufbwdsj.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Create%20an%20orthographic%20blueprint%20that%20describes%20this%20building%20in%20plan%2C%20elevation%2C%20and%20section.%20Label%20the%20%27North%20Elevation%27%20and%20%27Main%20Entrance%27%20clearly%20in%20technical%20architectural%20font.%20Format%2016%3A9.&model=gemini-3-pro-image-preview)

> **Whiteboard Summary (Educational):**
> 
>  "Summarize the concept of 'Transformer Neural Network Architecture' as a hand-drawn whiteboard diagram suitable for a university lecture. Use different colored markers for the Encoder and Decoder blocks, and include legible labels for 'Self-Attention' and 'Feed Forward'."

[![Image 4: Whiteboard Summary](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwx1jrqoda2bdwp03ac3o.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwx1jrqoda2bdwp03ac3o.png)

[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Summarize%20the%20concept%20of%20%27Transformer%20Neural%20Network%20Architecture%27%20as%20a%20hand-drawn%20whiteboard%20diagram%20suitable%20for%20a%20university%20lecture.%20Use%20different%20colored%20markers%20for%20the%20Encoder%20and%20Decoder%20blocks%2C%20and%20include%20legible%20labels%20for%20%27Self-Attention%27%20and%20%27Feed%20Forward%27.&model=gemini-3-pro-image-preview)

* * *

[](http://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n#2-character-consistency-amp-viral-thumbnails) 2. Character Consistency & Viral Thumbnails
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Nano-Banana Pro supports **up to 14 reference images** (6 with high fidelity). This allows for "Identity Locking"—placing a specific person or character into new scenarios without facial distortion.

**Best Practices:**

*   **Identity Locking:** Explicitly state: "Keep the person's facial features exactly the same as Image 1."
*   **Expression/Action:** Describe the _change_ in emotion or pose while maintaining the identity.
*   **Viral Composition:** Combine subjects with bold graphics and text in a single pass.

**Example Prompts:**

> **The "Viral Thumbnail" (Identity + Text + Graphics):**
> 
>  "Design a viral video thumbnail using the person from Image 1. **Face Consistency:** Keep the person's facial features exactly the same as Image 1, but change their expression to look excited and surprised. **Action:** Pose the person on the left side, pointing their finger towards the right side of the frame. **Subject:** On the right side, place a high-quality image of a delicious avocado toast. **Graphics:** Add a bold yellow arrow connecting the person's finger to the toast. **Text:** Overlay massive, pop-style text in the middle: '3分钟搞定!' (Done in 3 mins!). Use a thick white outline and drop shadow. **Background:** A blurred, bright kitchen background. High saturation and contrast."

[![Image 5: Viral Thumbnail](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxj70ws3c9zt35ix9kb0k.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxj70ws3c9zt35ix9kb0k.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Design%20a%20viral%20video%20thumbnail%20using%20the%20person%20from%20Image%201.%20Face%20Consistency%3A%20Keep%20the%20person%27s%20facial%20features%20exactly%20the%20same%20as%20Image%201%2C%20but%20change%20their%20expression%20to%20look%20excited%20and%20surprised.%20Action%3A%20Pose%20the%20person%20on%20the%20left%20side%2C%20pointing%20their%20finger%20towards%20the%20right%20side%20of%20the%20frame.%20Subject%3A%20On%20the%20right%20side%2C%20place%20a%20high-quality%20image%20of%20a%20delicious%20avocado%20toast.%20Graphics%3A%20Add%20a%20bold%20yellow%20arrow%20connecting%20the%20person%27s%20finger%20to%20the%20toast.%20Text%3A%20Overlay%20massive%2C%20pop-style%20text%20in%20the%20middle%3A%20%273%E5%88%86%E9%92%9F%E6%90%9E%E5%AE%9A!%27%20%28Done%20in%203%20mins!%29.%20Use%20a%20thick%20white%20outline%20and%20drop%20shadow.%20Background%3A%20A%20blurred%2C%20bright%20kitchen%20background.%20High%20saturation%20and%20contrast.&model=gemini-3-pro-image-preview)_(Note: Requires uploading a reference image)_

> **The "Fluffy Friends" Scenario (Group Consistency):**
> 
>  [Input 3 images of different plush creatures]
> 
>  "Create a funny 10-part story with these 3 fluffy friends going on a tropical vacation. The story is thrilling throughout with emotional highs and lows and ends in a happy moment. **Keep the attire and identity consistent for all 3 characters**, but their expressions and angles should vary throughout all 10 images. Make sure to only have one of each character in each image."

[![Image 6: The ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Futqhw1hi7997u4pftee6.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Futqhw1hi7997u4pftee6.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Create%20a%20funny%2010-part%20story%20with%20these%203%20fluffy%20friends%20going%20on%20a%20tropical%20vacation.%20The%20story%20is%20thrilling%20throughout%20with%20emotional%20highs%20and%20lows%20and%20ends%20in%20a%20happy%20moment.%20Keep%20the%20attire%20and%20identity%20consistent%20for%20all%203%20characters%2C%20but%20their%20expressions%20and%20angles%20should%20vary%20throughout%20all%2010%20images.%20Make%20sure%20to%20only%20have%20one%20of%20each%20character%20in%20each%20image.&model=gemini-3-pro-image-preview)_(Note: Requires uploading reference images)_

> **Brand Asset Generation:**
> 
>  [Input 1 image of a product]
> 
>  "Create 9 stunning fashion shots as if they’re from an award-winning fashion editorial. Use this reference as the brand style but add nuance and variety to the range so they convey a professional design touch. Please generate nine images, one at a time."

[![Image 7: Brand Asset Generation](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvdi6ut3gimx6gglj08ku.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvdi6ut3gimx6gglj08ku.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Create%209%20stunning%20fashion%20shots%20as%20if%20they%E2%80%99re%20from%20an%20award-winning%20fashion%20editorial.%20Use%20this%20reference%20as%20the%20brand%20style%20but%20add%20nuance%20and%20variety%20to%20the%20range%20so%20they%20convey%20a%20professional%20design%20touch.%20Please%20generate%20nine%20images%2C%20one%20at%20a%20time.&model=gemini-3-pro-image-preview)_(Note: Requires uploading a reference image)_

* * *

[](http://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n#3-grounding-with-google-search) 3. Grounding with Google Search
-----------------------------------------------------------------------------------------------------------------------------------------

Nano-Banana Pro uses Google Search to generate imagery based on real-time data, current events, or factual verification, reducing hallucinations on timely topics.

**Best Practices:**

*    Ask for visualizations of dynamic data (weather, stocks, news).
*    The model will "Think" (reason) about the search results before generating the image.

**Example Prompts:**

> **Real-Time Data Visualization:**
> 
>  "Visualize the current stock value of the main tech companies and the current trends. For each add some explanation on what happened recently which could explain that trend."

[![Image 8: Real-Time Data Visualization](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6trm4bcm20isbse3lqtw.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6trm4bcm20isbse3lqtw.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Visualize%20the%20current%20stock%20value%20of%20the%20main%20tech%20companies%20and%20the%20current%20trends.%20For%20each%20add%20some%20explanation%20on%20what%20happened%20recently%20which%20could%20explain%20that%20trend.&model=gemini-3-pro-image-preview)

> **Event Visualization:**
> 
>  "Generate an infographic of the best times to visit the U.S. National Parks in 2025 based on current travel trends."

[![Image 9: Event Visualization](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqb7cbgxiym5fg6c2warh.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqb7cbgxiym5fg6c2warh.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Generate%20an%20infographic%20of%20the%20best%20times%20to%20visit%20the%20U.S.%20National%20Parks%20in%202025%20based%20on%20current%20travel%20trends.&model=gemini-3-pro-image-preview)

* * *

[](http://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n#4-advanced-editing-restoration-amp-colorization) 4. Advanced Editing, Restoration & Colorization
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The model excels at complex edits via conversational prompting. This includes "In-painting" (removing/adding objects), "Restoration" (fixing old photos), "Colorization" (Manga/B&W photos), and "Style Swapping."

**Best Practices:**

*   **Semantic Instructions:** You do not need to manually mask; simply tell the model what to change naturally.
*   **Physics Understanding:** You can ask for complex changes like "fill this glass with liquid" to test physics generation.

**Example Prompts:**

> **Object Removal & In-painting:**
> 
>  "Remove the tourists from the background of this photo and fill the space with logical textures (cobblestones and storefronts) that match the surrounding environment."

[![Image 10: Object Removal & In-painting](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fa10yh8njebl5nssy8ht2.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fa10yh8njebl5nssy8ht2.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Remove%20the%20tourists%20from%20the%20background%20of%20this%20photo%20and%20fill%20the%20space%20with%20logical%20textures%20(cobblestones%20and%20storefronts)%20that%20match%20the%20surrounding%20environment.&model=gemini-3-pro-image-preview)_(Note: Requires uploading a photo)_

> **Manga/Comic Colorization:**
> 
>  [Input black and white manga panel]
> 
>  "Colorize this manga panel. Use a vibrant anime style palette. Ensure the lighting effects on the energy beams are glowing neon blue and the character's outfit is consistent with their official colors."

[![Image 11: Manga/Comic Colorization](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzrcg33qn8gccuknkh7iq.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzrcg33qn8gccuknkh7iq.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Colorize%20this%20manga%20panel.%20Use%20a%20vibrant%20anime%20style%20palette.%20Ensure%20the%20lighting%20effects%20on%20the%20energy%20beams%20are%20glowing%20neon%20blue%20and%20the%20character%27s%20outfit%20is%20consistent%20with%20their%20official%20colors.&model=gemini-3-pro-image-preview)_(Note: Requires uploading an image)_

> **Localization (Text Translation + Cultural Adaptation):**
> 
>  [Input image of a London bus stop ad]
> 
>  "Take this concept and localize it to a Tokyo setting, including translating the tagline into Japanese. Change the background to a bustling Shibuya street at night."

[![Image 12: Localization ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fnmlu3njxs595bpf6jo6i.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fnmlu3njxs595bpf6jo6i.png)

[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Take%20this%20concept%20and%20localize%20it%20to%20a%20Tokyo%20setting%2C%20including%20translating%20the%20tagline%20into%20Japanese.%20Change%20the%20background%20to%20a%20bustling%20Shibuya%20street%20at%20night.&model=gemini-3-pro-image-preview)_(Note: Requires uploading an image)_

> **Lighting/Seasonal Control:**
> 
>  [Input image of a house in summer]
> 
>  "Turn this scene into winter time. Keep the house architecture exactly the same, but add snow to the roof and yard, and change the lighting to a cold, overcast afternoon."

[![Image 13: Lighting/Seasonal Control](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7t7fbnjyr62zvrwfhi27.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7t7fbnjyr62zvrwfhi27.png)

[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Turn%20this%20scene%20into%20winter%20time.%20Keep%20the%20house%20architecture%20exactly%20the%20same%2C%20but%20add%20snow%20to%20the%20roof%20and%20yard%2C%20and%20change%20the%20lighting%20to%20a%20cold%2C%20overcast%20afternoon.&model=gemini-3-pro-image-preview)_(Note: Requires uploading an image)_

* * *

[](http://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n#5-dimensional-translation-2d-%E2%86%94-3d) 5. Dimensional Translation (2D ↔ 3D)
---------------------------------------------------------------------------------------------------------------------------------------------------------

A powerful new capability is translating 2D schematics into 3D visualizations, or vice versa. This is ideal for interior designers, architects, and meme creators.

**Example Prompts:**

> **2D Floor Plan to 3D Interior Design Board:**
> 
>  "Based on the uploaded 2D floor plan, generate a professional interior design presentation board in a single image. **Layout:** A collage with one large main image at the top (wide-angle perspective of the living area), and three smaller images below (Master Bedroom, Home Office, and a 3D top-down floor plan). **Style:** Apply a Modern Minimalist style with warm oak wood flooring and off-white walls across ALL images. **Quality:** Photorealistic rendering, soft natural lighting."

[![Image 14: Interior Design](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1lv4uptgdjnumcao1w16.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1lv4uptgdjnumcao1w16.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Based%20on%20the%20uploaded%202D%20floor%20plan%2C%20generate%20a%20professional%20interior%20design%20presentation%20board%20in%20a%20single%20image.%20Layout%3A%20A%20collage%20with%20one%20large%20main%20image%20at%20the%20top%20(wide-angle%20perspective%20of%20the%20living%20area)%2C%20and%20three%20smaller%20images%20below%20(Master%20Bedroom%2C%20Home%20Office%2C%20and%20a%203D%20top-down%20floor%20plan).%20Style%3A%20Apply%20a%20Modern%20Minimalist%20style%20with%20warm%20oak%20wood%20flooring%20and%20off-white%20walls%20across%20ALL%20images.%20Quality%3A%20Photorealistic%20rendering%2C%20soft%20natural%20lighting.&model=gemini-3-pro-image-preview)_(Note: Requires uploading a floor plan)_

> **2D to 3D Meme Conversion:**
> 
>  "Turn the 'This is Fine' dog meme into a photorealistic 3D render. Keep the composition identical but make the dog look like a plush toy and the fire look like realistic flames."

[![Image 15: Meme Conversion](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdo83a3gzt1h287p5v4zf.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdo83a3gzt1h287p5v4zf.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Turn%20the%20%27This%20is%20Fine%27%20dog%20meme%20into%20a%20photorealistic%203D%20render.%20Keep%20the%20composition%20identical%20but%20make%20the%20dog%20look%20like%20a%20plush%20toy%20and%20the%20fire%20look%20like%20realistic%20flames.&model=gemini-3-pro-image-preview)

* * *

[](http://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n#6-highresolution-amp-textures) 6. High-Resolution & Textures
--------------------------------------------------------------------------------------------------------------------------------------

Nano-Banana Pro supports native 1K to 4K image generation. This is particularly useful for detailed textures or large-format prints.

**Best Practices:**

*    Explicitly request high resolutions (2K or 4K) if your API/Interface allows.
*    Describe high-fidelity details (imperfections, surface textures).

**Example Prompts:**

> **4K Texture Generation:**
> 
>  "Harness native high-fidelity output to craft a breathtaking, atmospheric environment of a mossy forest floor. Command complex lighting effects and delicate textures, ensuring every strand of moss and beam of light is rendered in pixel-perfect resolution suitable for a 4K wallpaper."

[![Image 16: 4K Texture Generation](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8ecke4m4ow0ukgddy164.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8ecke4m4ow0ukgddy164.png)

[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Harness%20native%20high-fidelity%20output%20to%20craft%20a%20breathtaking%2C%20atmospheric%20environment%20of%20a%20mossy%20forest%20floor.%20Command%20complex%20lighting%20effects%20and%20delicate%20textures%2C%20ensuring%20every%20strand%20of%20moss%20and%20beam%20of%20light%20is%20rendered%20in%20pixel-perfect%20resolution%20suitable%20for%20a%204K%20wallpaper.&model=gemini-3-pro-image-preview)

> **Complex Logic (Thinking Mode):**
> 
>  "Create a hyper-realistic infographic of a gourmet cheeseburger, deconstructed to show the texture of the toasted brioche bun, the seared crust of the patty, and the glistening melt of the cheese. Label each layer with its flavor profile."

[![Image 17: Complex Logic](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1ogz1rel54z35crs8s26.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1ogz1rel54z35crs8s26.png)

[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Create%20a%20hyper-realistic%20infographic%20of%20a%20gourmet%20cheeseburger%2C%20deconstructed%20to%20show%20the%20texture%20of%20the%20toasted%20brioche%20bun%2C%20the%20seared%20crust%20of%20the%20patty%2C%20and%20the%20glistening%20melt%20of%20the%20cheese.%20Label%20each%20layer%20with%20its%20flavor%20profile.&model=gemini-3-pro-image-preview)

* * *

[](http://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n#7-thinking-amp-reasoning) 7. Thinking & Reasoning
---------------------------------------------------------------------------------------------------------------------------

Nano-Banana Pro defaults to a "Thinking" process where it generates interim thought images (not charged) to refine composition before rendering the final output. This allows for data analysis and solving visual problems.

**Example Prompts:**

> **Solve Equations:**
> 
>  "Solve log_{x^2+1}(x^4-1)=2 in C on a white board. Show the steps clearly."

[![Image 18: Solve Equations](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwoy90sxms1jg6oj16h49.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwoy90sxms1jg6oj16h49.jpg)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Solve%20log_%7Bx%2B1%7D(x%5E2%2B1)%3D2%20in%20C%20on%20a%20white%20board.%20Show%20the%20steps%20clearly.&model=gemini-3-pro-image-preview)

> **Visual Reasoning:**
> 
>  "Analyze this image of a room and generate a 'before' image that shows what the room might have looked like during construction, showing the framing and unfinished drywall."

[![Image 19: Visual Reasoning](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fe8pq0z5wyn3ajxp8lrb6.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fe8pq0z5wyn3ajxp8lrb6.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Analyze%20this%20image%20of%20a%20room%20and%20generate%20a%20%27before%27%20image%20that%20shows%20what%20the%20room%20might%20have%20looked%20like%20during%20construction%2C%20showing%20the%20framing%20and%20unfinished%20drywall.&model=gemini-3-pro-image-preview)_(Note: Requires uploading an image)_

* * *

[](http://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n#8-oneshot-storyboarding-amp-concept-art) 8. One-Shot Storyboarding & Concept Art
----------------------------------------------------------------------------------------------------------------------------------------------------------

You can generate sequential art or storyboards without a grid, ensuring a cohesive narrative flow in a single session. This is also popular for "Movie Concept Art" (e.g., fake leaks of upcoming films).

**Example Prompt:**

> "Create an addictively intriguing 9-part story with 9 images featuring a woman and man in an award-winning luxury luggage commercial. The story should have emotional highs and lows, ending on an elegant shot of the woman with the logo. **The identity of the woman and man and their attire must stay consistent throughout** but they can and should be seen from different angles and distances. Please generate images one at a time. Make sure every image is in a 16:9 landscape format."

[![Image 20: One-Shot Storyboarding](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fheq0q4omitqbauym8cg7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fheq0q4omitqbauym8cg7.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Create%20an%20addictively%20intriguing%209-part%20story%20with%209%20images%20featuring%20a%20woman%20and%20man%20in%20an%20award-winning%20luxury%20luggage%20commercial.%20The%20story%20should%20have%20emotional%20highs%20and%20lows%2C%20ending%20on%20an%20elegant%20shot%20of%20the%20woman%20with%20the%20logo.%20The%20identity%20of%20the%20woman%20and%20man%20and%20their%20attire%20must%20stay%20consistent%20throughout%20but%20they%20can%20and%20should%20be%20seen%20from%20different%20angles%20and%20distances.%20Please%20generate%20images%20one%20at%20a%20time.%20Make%20sure%20every%20image%20is%20in%20a%2016%3A9%20landscape%20format.&model=gemini-3-pro-image-preview)

* * *

[](http://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n#9-structural-control-amp-layout-guidance) 9. Structural Control & Layout Guidance
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Input images aren't limited to character references or subjects to edit. You can use them to strictly control the **composition and layout** of the final output. This is a game-changer for designers who need to turn a napkin sketch, a wireframe, or a specific grid layout into a polished asset.

**Best Practices:**

*   **Drafts & Sketches:** Upload a hand-drawn sketch to define exactly where the text and object should sit.
*   **Wireframes:** Use screenshots of existing layouts or wireframes to generate high-fidelity UI mockups.
*   **Grids:** Use grid images to force the model to generate assets for tile-based games or LED displays.

**Example Prompts:**

> **Sketch to Final Ad:**
> 
>  "Create a ad for a [product] following this sketch."

[![Image 21: Sketch to Final Ad](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F93lhzmeat6ta2lkwicvo.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F93lhzmeat6ta2lkwicvo.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Create%20a%20high-end%20magazine%20advertisement%20for%20a%20luxury%20perfume%20brand%20called%20%27Nebula%27%20based%20on%20this%20hand-drawn%20sketch.%20Keep%20the%20exact%20layout%20of%20the%20bottle%20and%20text%20placement%2C%20but%20render%20it%20in%20a%20photorealistic%20style%20with%20a%20galaxy-themed%20background.&model=gemini-3-pro-image-preview)_(Note: Requires uploading a sketch)_

> **UI Mockup from Wireframe:**
> 
>  "Create a mock-up for a [product] following these guidelines."

[![Image 22: UI Mockup from Wireframe](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fn5dxh2w65y41x01d3x1r.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fn5dxh2w65y41x01d3x1r.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Generate%20a%20photorealistic%20UI%20mockup%20for%20a%20fitness%20tracking%20app%20based%20on%20this%20wireframe.%20Replace%20the%20placeholder%20boxes%20with%20high-quality%20images%20of%20runners%20and%20data%20visualization%20charts%2C%20but%20strictly%20adhere%20to%20the%20button%20placement%20and%20grid%20structure.&model=gemini-3-pro-image-preview)_(Note: Requires uploading a wireframe)_

> **Pixel Art & LED Displays:**
> 
>  "Generate a pixel art sprite of a unicorn that fits perfectly into this 64x64 grid image. Use high contrast colors."
> 
> _(Tip: Developers can then programmatically extract the center color of each cell to drive a connected 64x64 LED matrix display)._

[![Image 23: Pixel Art](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvpr4xhguji825rae3udw.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvpr4xhguji825rae3udw.png)[Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?prompt=Generate%20a%20pixel%20art%20sprite%20of%20a%20unicorn%20that%20fits%20perfectly%20into%20this%2064x64%20grid%20image.%20Use%20high%20contrast%20colors.&model=gemini-3-pro-image-preview)_(Note: Requires uploading a grid image)_

> **Sprites:**
> 
>  "Sprite sheet of a woman doing a backflip on a drone, 3x3 grid, sequence, frame by frame animation, square aspect ratio. Follow the structure of the attached reference image exactly.."
> 
>  (Tip: You can then extract each cell and make a gif)

[![Image 24: Sprite sheet](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0kafc8px17sbjzpiz744.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0kafc8px17sbjzpiz744.png)

[![Image 25: Sprite](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flnq1xjj2f89jmbsazcef.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flnq1xjj2f89jmbsazcef.gif)

[Try it in Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_Started_Nano_Banana.ipynb#scrollTo=xuQeyK-teUf1)

* * *

[](http://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n#10-whats-next) 10. What's Next?
---------------------------------------------------------------------------------------------------------

Now that you have mastered the basics of prompting, here is how you can start building:

*   **Experiment in the UI:**[Google AI Studio](https://aistudio.google.com/) is the fastest way to test prompts and parameters.
*    Check really cool **Nano-banana powered app** in the [App Gallery](https://aistudio.google.com/apps?source=showcase&showcaseTag=nano-banana).
*   **Vibe-code you dream app**: Transform you best prompt into an app that you can easily share with your friends in [AI Studio Build](https://aistudio.google.com/apps).
*   **Build Applications:** Ready to code? Check out the [developer guide](https://dev.to/googleai/introducing-nano-banana-pro-complete-developer-tutorial-5fc8) or the [Gemini API Cookbook](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_Started_Nano_Banana.ipynb#nano-banana-pro) for guides and code snippets.
*   **Technical Deep Dive:** Read the full [Gemini API Documentation](https://ai.google.dev/gemini-api/docs) for details on rate limits, pricing, and integration.

[![Image 26: Banana master](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fej883k4hdvceoweevlo8.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fej883k4hdvceoweevlo8.png)