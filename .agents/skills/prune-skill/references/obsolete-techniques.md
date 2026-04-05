# Obsolete Techniques

Running list of prompting and skill techniques proven ineffective or harmful on current-generation models. Update this file whenever a prune reveals a new obsolete technique — add the entry with the date discovered and the source.

Each entry: what the technique is, what models it affects, the evidence, and what to use instead.

---

## Confirmed Obsolete on Frontier Models (2025–2026)

### 1. "Think step by step" / Universal CoT instructions on reasoning models
**Affected models:** OpenAI o3, o4-mini; Claude Extended Thinking / Claude 4 Opus/Sonnet; Gemini Flash 2.5
**Evidence:** Wharton GAIL Prompting Science Report 2 (Meincke, Mollick et al., June 2025); arXiv:2411.02093 (Nov 2024)
- Reasoning models already perform CoT internally — explicit instruction adds 20–80% response time cost for 2–3% performance gain at best
- Gemini Flash 2.5: explicit CoT instruction caused -3.3% performance decrease
- Non-reasoning models: CoT still useful but introduces inconsistency — models may already reason by default

**Replace with:** Omit CoT instruction for reasoning models. For non-reasoning models, use CoT selectively on complex multi-step reasoning tasks only. Scope: "On non-reasoning models, use CoT for tasks requiring multi-step logic."

---

### 2. Role prompting as factual accuracy expander
**Affected models:** All frontier models (GPT-4o+, Claude 3.5+, Gemini 1.5+)
**Evidence:** arXiv:2409.13979 "Role-Play Paradox in Large Language Models" (updated Feb 2025)
- "You are an expert in X with 20 years of experience" does NOT expand factual knowledge boundaries
- Risk: amplifies existing model biases by over-committing to a persona
- Note: Role definition still useful for tone, output format, and workflow priming — just not for expanding factual accuracy

**Replace with:** Use role definition for tone and domain context ("You are a Senior PM. Your outputs are measurable and immediately actionable.") NOT as a claim of expanded factual knowledge. Remove any instruction implying the role expands what the model knows.

---

### 3. Excessive few-shot examples (more than 3)
**Affected models:** All modern frontier models
**Evidence:** arXiv:2509.13196 "The Few-Shot Dilemma: Over-prompting Large Language Models" (Sep 2025)
- "Few-shot collapse" confirmed: performance drops sharply above threshold
- Gemini Flash: 0-shot 33% → 4-shot 64% → 8-shot dropped back to 33%
- Gemma 7B on vulnerability classification: 77.9% → 39.9% after Few-Shot
- LLaMA-2 70B: 68.6% → 21.0% after Few-Shot

**Replace with:** 1–2 carefully selected, highly representative examples. The SkillReducer (arXiv:2603.29919) recommendation of "keep 1–2 shortest examples" is correct.

---

### 4. Complex constraint scaffolding on GPT-5/Claude 4 class models
**Affected models:** GPT-5, Claude 4 Opus/Sonnet, and equivalent frontier models
**Evidence:** arXiv:2510.22251 "You Don't Need Prompt Engineering Anymore: The Prompting Inversion" (Oct 2025)
- "Prompting Inversion" phenomenon: elaborate step-by-step rules and constraint systems cause over-literal interpretation
- GPT-4o: complex "sculpting" prompts 97% vs CoT 93% — complex better
- GPT-5: complex "sculpting" 94% vs CoT 96.36% — simple better
- GPT-5 zero-shot already exceeds best GPT-4o prompted performance

**Replace with:** For GPT-5/Claude 4 class models, state the desired outcome clearly and concisely. Reduce numbered constraint lists. Trust the model's reasoning. Retain constraints only for hard behavioral requirements (MUST/NEVER rules), not for process guidance.

---

### 5. Emotional manipulation phrases
**Affected models:** All frontier models (GPT-4o+, Claude 3.5+)
**Evidence:** Wharton GAIL Prompting Science Report 2 (2025); Medium "Magic Phrases Don't Work" (Jan 2026)
- "I'll tip you $200", "I'll get fired if you don't help", "This is really important for my career"
- EmotionPrompt (Cheng et al., 2023) showed 8–115% improvements on older models — not reproduced on modern models
- Modern models show inconsistent or negligible effects from emotional stimuli

**Replace with:** Remove these phrases. They add noise without benefit on current models.

---

## Conditionally Obsolete (Model-Dependent)

### 6. CoT for non-reasoning models
**Status:** Still useful but must be scoped
**Evidence:** Wharton GAIL (2025) — non-reasoning models show modest average improvements but increased variability
**Guidance:** Keep CoT instructions only for explicitly non-reasoning model contexts. Add: "applies to non-reasoning models only."

---

## Techniques Still Valid (Do Not Prune)

These are sometimes misidentified as obsolete but remain evidence-backed:

| Technique | Still Valid? | Evidence |
|-----------|-------------|---------|
| XML structure tags (Claude) | Yes | Anthropic official docs 2025 |
| MUST/NEVER hard gate statements | Yes | arXiv:2509.00482 rule-based prompting |
| Progressive disclosure (metadata → body → references) | Yes | arXiv:2602.12430, arXiv:2603.29919 |
| 1–2 representative examples | Yes | NeurIPS 2025 self-generated examples paper |
| Specific trigger phrases in descriptions | Yes | SkillReducer arXiv:2603.29919 |
| Imperative one-liner workflow steps | Yes | Community consensus, agentskills.io spec |

---

## How to Update This File

When a prune reveals a newly obsolete technique, add an entry:

```markdown
### N. [Technique name]
**Affected models:** [specific models]
**Evidence:** [citation with date]
- [specific finding with numbers if available]

**Replace with:** [what to use instead]

**Discovered:** YYYY-MM-DD during prune of [skill-name]
```
