# Skill Scoring Rubric

Read when scoring is ambiguous during the baseline audit or post-rewrite scoring in Step 2a / 2e.

Each criterion is scored 0–2. Max total: 14.

---

## 1. Routing (0–2)
Does the description trigger on the phrases users actually say?

| Score | Meaning | Example |
|-------|---------|---------|
| 0 | Missing description or fewer than 3 trigger phrases | `description: Helps with PRDs.` |
| 1 | Has some triggers but misses common synonyms or is too vague | `description: Write product requirements documents.` |
| 2 | Rich trigger set — primary phrases + synonyms + context hints, under 1024 chars | `description: Write a PRD, document requirements, create a spec, turn a brief into requirements, define acceptance criteria...` |

**Fix for 0–1:** Add synonyms, rephrase as "Load when the user asks to [action]", test mentally against 5 real user prompts.

---

## 2. Role Definition (0–2)
Is the expert role specific and narrow enough to prime domain knowledge?

| Score | Meaning | Example |
|-------|---------|---------|
| 0 | No role defined, or generic ("You are an AI assistant") | — |
| 1 | Role defined but domain is too broad | `You are a software engineer.` |
| 2 | Role names the specific expert title + narrow specialty | `You are a Senior Product Manager specializing in B2B SaaS feature specifications.` |

**Fix for 0–1:** Name the exact job title, then narrow it with "specializing in [subdomain]". Add a quality standard sentence: "Your PRDs are measurable, testable, and immediately actionable for engineers."

---

## 3. Workflow (0–2)
Are steps numbered, imperative, and each containing exactly one action?

| Score | Meaning | Example |
|-------|---------|---------|
| 0 | No numbered steps, or steps are paragraphs of prose | — |
| 1 | Steps exist but use passive/vague language or compound multiple actions | `2. Think through requirements and consider constraints.` |
| 2 | Every step is an imperative one-liner with one clear action verb | `2. Ask: "What does success look like — give me 2 measurable metrics."` |

**Fix for 0–1:** Rewrite each step starting with an action verb (Ask, Run, Write, Validate, Present). Split compound steps. Remove explanatory prose — move it to references/ if needed.

---

## 4. Gotchas (0–2)
Are there non-obvious domain facts the agent will get wrong without being told?

| Score | Meaning | Example |
|-------|---------|---------|
| 0 | No Gotchas section | — |
| 1 | Has gotchas but they're generic advice ("be thorough", "check for errors") | — |
| 2 | Concrete, domain-specific facts that defy reasonable assumptions | `The users table uses soft deletes — all queries must include WHERE deleted_at IS NULL.` |

**Fix for 0–1:** Ask "What would a capable agent get wrong on their first try?" Research domain-specific edge cases. Each gotcha = one concrete, actionable correction.

---

## 5. Output Format (0–2)
Is there a schema, template, or structured example of the expected output?

| Score | Meaning | Example |
|-------|---------|---------|
| 0 | No output format defined | — |
| 1 | Output described in prose ("The response should include a summary, then findings...") | — |
| 2 | Concrete template or schema the agent can pattern-match against | Markdown template with section headers and placeholder descriptions |

**Fix for 0–1:** Replace prose description with a literal template. Short templates (under 30 lines) belong inline. Longer templates go in `assets/` with a load trigger.

---

## 6. Examples (0–2)
Are examples realistic, complete, and domain-specific?

| Score | Meaning | Example |
|-------|---------|---------|
| 0 | No examples | — |
| 1 | Examples exist but inputs are generic or outputs are truncated/abbreviated | `<input>Write a PRD</input><output>[PRD would go here]</output>` |
| 2 | Realistic inputs matching real user phrasing; outputs are complete and production-ready | Full input from an actual-sounding user request; full output showing exactly what "good" looks like |

**Fix for 0–1:** Use a real-sounding input ("write a PRD for adding dark mode to our React app"). Write the complete output — don't truncate. Per NeurIPS 2025: domain-specific real examples outperform generic synthetic ones.

---

## 7. Token Efficiency (0–2)
Is 60%+ of the body actionable content (Core Rules, Workflow, Format, Examples)?

| Score | Meaning |
|-------|---------|
| 0 | Majority of body is background, rationale, or content the LLM already knows |
| 1 | 40–60% actionable — some background sections that could move to references/ |
| 2 | 60%+ actionable — background and edge cases are in references/ with specific load triggers |

**Fix for 0–1:** Apply the SkillReducer taxonomy. Every paragraph that starts with "This is important because..." or "Background:" or explains general domain knowledge → move to `references/background.md`. Write a specific load trigger: "Read `references/background.md` if the user is new to [domain]."

---

## Scoring Benchmarks

| Total | Interpretation | Action |
|-------|---------------|--------|
| 0–5 | Needs full rewrite | Rewrite from scratch using universal-skill-creator workflow |
| 6–9 | Needs significant improvement | Apply full improvement cycle |
| 10–11 | Needs targeted fixes | Fix the 0–1 scoring criteria only |
| 12–13 | Good, minor polish | Fix any 1s; consider if compression is needed |
| 14 | Excellent | Validate, no changes needed |
