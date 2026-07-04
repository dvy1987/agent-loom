# Project Setup — Full Worked Examples

Skill: `project-setup` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** "Set up agents. I'm a PM building a React Native habit tracker. Not confident in architecture, testing, or security."

**Output:**
```
`owner_mode: non-technical`. AGENTS.md with Agent-Led Architecture, Session Lifecycle, Skill Invocation. Rubric 13/14.
```

## Example 2 — Step-by-step execution

**Input:** "Run `project-setup` on [concrete task]"

**Agent actions:**
1. Check Existing Context
2. User Interview (Two Axes)
3. Map Skill Gaps (Dynamic)
4. Generate the AGENTS.md
5. Write the Orchestration Map
6. Present, Iterate, Save

**Impact Report shape:**
```
Project setup complete: [name] | Platform: [target] | Mode: [single|multi]
Files saved: [paths] ([line counts]) | Commands auto-extracted from: [manifests]
User role: [role] | Owner mode: [technical|hybrid|non-technical] | Skill gaps filled: [list]
Orchestration Map: [skill count] across [phase count] phases
Session Lifecycle + Agent-Led blocks: [yes/no] | Rubric: [n/14] | L3: references/examples.md
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **The interview is the highest-leverage step.** 3 minutes of interview → 10x better AGENTS.md. Never skip it (except in `RETROACTIVE=true` mode).
- **Skill gaps are the secret sauce.** A PM's AGENTS.md looks completely different from an engineer's.
- **Orchestration Map ages fastest; never auto-generate without interview.** Re-run after milestones. LLM-generated context without human input reduces task success ~3%.
- 

---

See `SKILL.md` for hard rules and verification checklist.

---

|---|
| Copy template AGENTS.md | Interview user for gaps and routing. |
| Skip knowledge-graph bootstrap | Step 6b builds graph when skill installed. |
| Install every skill | Recommend subset from interview. |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **The interview is the highest-leverage step.** 3 minutes of interview → 10x better AGENTS.md. Never skip it (except in `RETROACTIVE=true` mode).
- **Skill gaps are the secret sauce.** A PM's AGENTS.md looks completely different from an engineer's.
- **Orchestration Map ages fastest; never auto-generate without interview.** Re-run after milestones. LLM-generated context without human input reduces task success ~3%.
- 

---

See `SKILL.md` for hard rules and verification checklist.
