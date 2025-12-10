---
description: Create ThursdAI quarterly AI recap from combined episode files
---

# ThursdAI Quarterly AI Recap Workflow

## Overview
Generate a month-by-month breakdown of significant AI news from ThursdAI newsletters for a specific quarter.

## Input Required
When starting this workflow, specify:
- **Quarter**: Q1, Q2, Q3, or Q4
- **Year**: 2025, 2026, etc.

## Source Files Location
- Combined episode files are located at: `/Users/altryne/projects/thursdAI_yearly_recap/2025_episodes/Q[X] 2025/Q[X]_2025_combined.md`
- Each combined file contains all episodes for that quarter with headers like `## 📆 ThursdAI - [Date] - [Title]`

## Output Format
Create a markdown file at: `/Users/altryne/projects/thursdAI_yearly_recap/Q[X]_2025_AI_Recap.md`

### Structure Template
```markdown
# Q[X] 2025 AI Recap - ThursdAI

## Quarter Overview
[2-3 sentence summary of the quarter's major themes]

---

## [Month] 2025

### Top Stories
- **[Major Release 1]**: [1-2 sentence description]
- **[Major Release 2]**: [1-2 sentence description]

### Open Source LLMs
- **[Model Name]**: [Brief description with key specs]

### Big CO LLMs + APIs
- **[Product/Model]**: [Brief description]

### Vision & Video
- **[Model/Product]**: [Brief description]

### Voice & Audio
- **[Model/Product]**: [Brief description]

### AI Art & Diffusion & 3D
- **[Model/Product]**: [Brief description]

### Tools
- **[Tool Name]**: [Brief description]

---

[Repeat for each month in the quarter]

---

## Quarter Summary

### Major Themes
1. [Theme 1]
2. [Theme 2]
3. [Theme 3]

### Biggest Releases by Month
- **[Month 1]**: [Top release]
- **[Month 2]**: [Top release]
- **[Month 3]**: [Top release]
```

## Prioritization Criteria
1. **Title Mentions**: Releases mentioned in episode titles are highest priority
2. **Discussion Depth**: Items with extensive coverage in newsletter body
3. **Community Impact**: Mentions of viral moments, benchmarks broken, or widespread adoption
4. **Categories to track**:
   - Open Source LLMs (models, weights, training methods)
   - Big CO LLMs + APIs (OpenAI, Google, Anthropic, xAI, etc.)
   - Vision & Video (video generation, VLMs)
   - Voice & Audio (TTS, STT, music)
   - AI Art & Diffusion & 3D (image gen, 3D models)
   - Tools (agents, protocols like MCP/A2A, coding assistants)

## Steps

1. **Read the combined file** for the target quarter
   - File may be 2000+ lines, read in chunks of 800 lines
   - Note episode dates to categorize by month

2. **Extract releases by month**
   - Group episodes by their publication month
   - For each episode, identify:
     - Items in episode title (highest priority)
     - Items in TL;DR section
     - Items discussed extensively in body

3. **Categorize and summarize**
   - Place each release in appropriate category
   - Write concise 1-2 sentence summaries
   - Note key specs (parameter counts, benchmarks, licenses)

4. **Identify top stories per month**
   - Select 2-4 most impactful releases
   - These go in "Top Stories" section

5. **Write quarter summary**
   - Identify 3-5 overarching themes
   - List biggest release per month

6. **Reference existing recaps** for format consistency
   - See `/Users/altryne/projects/thursdAI_yearly_recap/Q1_2025_AI_Recap.md` as template

## Quarter-Month Mapping
- **Q1**: January, February, March
- **Q2**: April, May, June
- **Q3**: July, August, September
- **Q4**: October, November, December

## Example Prompt to Start
```
Create the Q2 2025 AI recap using the /create-quarterly-recap workflow.
Read /Users/altryne/projects/thursdAI_yearly_recap/2025_episodes/Q2 2025/Q2_2025_combined.md
and generate the recap following the established format from Q1.
```
